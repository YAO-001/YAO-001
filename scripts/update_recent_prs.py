#!/usr/bin/env python3
"""Update the generated recent-PR block in the profile README."""

from __future__ import annotations

import html
import json
import os
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


PROFILE_USERNAME = "YAO-001"
PROFILE_REPOSITORY = "YAO-001/YAO-001"
DISPLAY_LIMIT = 5
SEARCH_LIMIT = 30
START_MARKER = "<!-- recent-prs:start -->"
END_MARKER = "<!-- recent-prs:end -->"
SEARCH_ENDPOINT = "https://api.github.com/search/issues"
README_PATH = Path(__file__).resolve().parents[1] / "README.md"


def fetch_pull_requests() -> list[dict[str, Any]]:
    """Fetch recent public PRs authored by the profile owner."""
    search_query = (
        f"author:{PROFILE_USERNAME} is:pr is:public "
        f"-repo:{PROFILE_REPOSITORY}"
    )
    query_parameters = urlencode(
        {
            "q": search_query,
            "sort": "created",
            "order": "desc",
            "per_page": SEARCH_LIMIT,
        }
    )
    request_url = f"{SEARCH_ENDPOINT}?{query_parameters}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "YAO-001-profile-readme-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"

    request = Request(
        request_url,
        headers=headers,
    )

    try:
        with urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"GitHub Search API returned HTTP {error.code}: {detail}"
        ) from error
    except URLError as error:
        raise RuntimeError(
            f"Could not reach the GitHub Search API: {error}"
        ) from error

    items = payload.get("items")
    if not isinstance(items, list):
        raise RuntimeError("GitHub Search API response did not contain an item list")
    if payload.get("incomplete_results"):
        raise RuntimeError("GitHub Search API returned incomplete results")

    selected = select_pull_requests(items)
    if not selected:
        raise RuntimeError(
            "GitHub Search API returned no displayable upstream pull requests; "
            "refusing to erase the existing README block"
        )
    return selected


def select_pull_requests(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep public upstream PRs that are open, draft, or merged."""
    repository_url_prefix = "https://api.github.com/repos/"
    selected: list[dict[str, Any]] = []

    for item in items:
        repository_url = item.get("repository_url", "")
        if not repository_url.startswith(repository_url_prefix):
            continue

        repository = repository_url.removeprefix(repository_url_prefix)
        if repository.casefold() == PROFILE_REPOSITORY.casefold():
            continue

        pull_request = item.get("pull_request") or {}
        if item.get("state") == "open":
            status = "DRAFT" if item.get("draft") else "OPEN"
        elif pull_request.get("merged_at"):
            status = "MERGED"
        else:
            continue

        if not all(item.get(field) for field in ("number", "title", "html_url")):
            continue

        selected.append(
            {
                "repository": repository,
                "number": item["number"],
                "title": item["title"],
                "url": item["html_url"],
                "status": status,
            }
        )
        if len(selected) == DISPLAY_LIMIT:
            break

    return selected


def escape_markdown(value: str, limit: int | None = None) -> str:
    """Normalize and escape untrusted text before inserting it into Markdown."""
    normalized = " ".join(value.split())
    if limit and len(normalized) > limit:
        normalized = normalized[: limit - 1].rstrip() + "…"

    escaped = html.escape(normalized, quote=False).replace("\\", "\\\\")
    for character in ("`", "*", "_", "[", "]", "~"):
        escaped = escaped.replace(character, f"\\{character}")
    return escaped


def render_pull_requests(pull_requests: list[dict[str, Any]]) -> str:
    """Render PR metadata as a compact, text-only Markdown list."""
    if not pull_requests:
        return "_No recent public upstream pull requests._"

    lines: list[str] = []
    for pull_request in pull_requests:
        repository = pull_request["repository"]
        status = pull_request["status"]
        label = escape_markdown(f"{repository}#{pull_request['number']}")
        title = escape_markdown(pull_request["title"], limit=120)
        lines.append(
            f"- **{status}** · [{label}]({pull_request['url']}) — {title}"
        )

    return "\n".join(lines)


def replace_generated_block(readme: str, rendered: str) -> str:
    """Replace exactly one generated block without touching surrounding prose."""
    if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
        raise RuntimeError("README must contain exactly one recent-PR marker pair")

    start_marker_index = readme.index(START_MARKER)
    end = readme.index(END_MARKER)
    if end < start_marker_index:
        raise RuntimeError("README recent-PR markers are in the wrong order")

    start = start_marker_index + len(START_MARKER)
    return f"{readme[:start]}\n{rendered}\n{readme[end:]}"


def main() -> None:
    pull_requests = fetch_pull_requests()
    original = README_PATH.read_text(encoding="utf-8")
    updated = replace_generated_block(
        original, render_pull_requests(pull_requests)
    )

    if updated == original:
        print("README.md is already up to date.")
        return

    with README_PATH.open("w", encoding="utf-8", newline="\n") as readme_file:
        readme_file.write(updated)
    print(f"Updated README.md with {len(pull_requests)} recent pull requests.")


if __name__ == "__main__":
    main()
