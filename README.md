# YAO / 001

**Research Intern @ Institute of Automation, Chinese Academy of Sciences (CASIA)**

I work on **embodied intelligence and world models**, **robot learning and reinforcement learning**, and next-generation **agentic architectures for embodied systems**.

我目前在中国科学院自动化研究所实习，主要围绕具身智能与世界模型、机器人学习与强化学习，以及面向 Agentic 的下一代具身智能架构开展研究。

[Research homepage](https://yao-001.github.io/) · [Email](mailto:yaoyaoguonan@outlook.com)

## Research focus

- **Embodied intelligence & world models** — connecting predictive representations with long-horizon planning, causal reasoning, and closed-loop control.
- **Robot learning & reinforcement learning** — learning robust policies from offline data and continued interaction under real-world constraints.
- **Agentic embodied architectures** — coordinating perception, memory, planning, tools, and action in open-ended environments.

## Selected upstream work

- **[FastMCP](https://github.com/PrefectHQ/fastmcp)** · [merged PR #4704: CodeMode error propagation](https://github.com/PrefectHQ/fastmcp/pull/4704) — Made failed tool calls catchable inside sandboxed CodeMode programs while preserving clear uncaught-error semantics.
- **[verl](https://github.com/verl-project/verl)** · [merged PR #7204: per-turn LLM token tracing](https://github.com/verl-project/verl/pull/7204) — Added decoded prompt and response text to asynchronous agent-loop traces for MLflow, Weave, and Trackio.
- **[AReno](https://github.com/inclusionAI/AReno)** · [merged PR #473: native attention GPU equivalence](https://github.com/inclusionAI/AReno/pull/473) — Built numerical checks for varlen prefill and paged decode kernels against an independent PyTorch SDPA reference.
- **[AReaL](https://github.com/areal-project/AReaL)** · [merged PR #1578: TMS launcher reliability](https://github.com/areal-project/AReaL/pull/1578) — Fixed an `LD_PRELOAD` conflict that broke multi-GPU TMS offload lifecycle operations.
- **[AReaL](https://github.com/areal-project/AReaL)** · [open draft PR #1571: race-safe TMS teardown](https://github.com/areal-project/AReaL/pull/1571) — Proposed idempotent FSDP cleanup, ordered worker shutdown, and verified process-group termination after offload.

## Recent upstream PRs

<!-- recent-prs:start -->
- **MERGED** · [inclusionAI/AReno#473](https://github.com/inclusionAI/AReno/pull/473) — test: add native attention GPU equivalence checks
- **OPEN** · [inclusionAI/AReno#472](https://github.com/inclusionAI/AReno/pull/472) — docs(agentic): define trajectory observability contract
- **OPEN** · [inclusionAI/AReno#471](https://github.com/inclusionAI/AReno/pull/471) — build: adopt file-backed dynamic package version
- **OPEN** · [alibaba/open-code-review#848](https://github.com/alibaba/open-code-review/pull/848) — fix(viewer): show running status for active sessions
- **MERGED** · [areal-project/AReaL#1578](https://github.com/areal-project/AReaL/pull/1578) — fix(infra): preserve LD\_PRELOAD in local launchers
<!-- recent-prs:end -->

## Current questions

- How can world models become part of the embodied decision loop rather than remain passive prediction modules?
- How should robots combine offline experience with online reinforcement learning to improve safely and continually?
- What abstractions should coordinate perception, memory, planning, tools, and action in the next generation of agentic embodied systems?

## Working with

Python · PyTorch · FSDP · reinforcement learning · robot learning · RL post-training · distributed systems · MCP
