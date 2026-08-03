# YAO / 001

Working on reliable **agent systems**, **LLM post-training infrastructure**, and **Model Context Protocol (MCP) tooling** with Python.

我关注 AI Agent、LLM 后训练与 MCP 生态，并通过开源协作把工程问题变成可验证的实验。

## Selected upstream work

- **[FastMCP](https://github.com/PrefectHQ/fastmcp)** · [merged PR #4704: CodeMode error propagation](https://github.com/PrefectHQ/fastmcp/pull/4704) — Fixed tool-error propagation so sandboxed CodeMode programs can catch failed tool calls while uncaught failures still surface correctly.
- **[AReaL](https://github.com/areal-project/AReaL)** · [open draft PR #1571: TMS teardown](https://github.com/areal-project/AReaL/pull/1571) — Proposed race-safe teardown after TMS offload, covering idempotent FSDP cleanup, ordered worker shutdown, and verified process-group termination.
- **[TRL](https://github.com/huggingface/trl)** · [open draft PR #6615: activation offloading](https://github.com/huggingface/trl/pull/6615) — Proposed opt-in activation offloading for GRPO and RLOO trainers, with step-scoped lifecycle management, tests, and documentation.

## Current questions

- How should agent runtimes recover from tool, state, and process failures?
- How can offloading make RL post-training more memory-efficient without obscuring failure modes?
- How should MCP tools preserve clear contracts and error semantics across execution boundaries?

## Working with

Python · PyTorch · FSDP · RL post-training · distributed systems · MCP
