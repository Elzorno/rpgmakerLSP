# Agent Collaboration Guide

This repository is shared by Codex and Claude. Use the repo-local coordination files in `.agents/` before making changes.

## Repository Status (read this first)

- **Canon lives in the sibling repository `../TheLastSwordProtocol-Atlas/`.** All story, world, gameplay, and design truth comes from its `atlas/docs/` tree. Do not read canon from this repository.
- This repository is **legacy reference** plus, temporarily, the **atlas-import toolchain host** (`tools/atlas-import/` and its `reports/atlas-import/` outputs) until that toolchain is relocated into the Atlas repo (plan item A5).
- The local `atlas/` directory is a retired stale fork — it now contains only a pointer README (WO-0029). Documents elsewhere in this repo may carry superseded pre-v1.1 canon; where they conflict with the Atlas repo, the Atlas repo wins.
- The clean game implementation target is `../TheLastSwordProtocol-Game/`, not this repo's `data/`.

## Required Workflow

1. Read `.agents/protocol.md`.
2. Check `.agents/task-board.md` for current ownership and blockers.
3. Check the other agent's outbox:
   - Codex reads `.agents/outbox/claude.md`.
   - Claude reads `.agents/outbox/codex.md`.
4. Before editing files, claim the work in `.agents/task-board.md`.
5. After finishing, append a handoff note to your own outbox.

## Project Notes

- This is an RPG Maker MZ project. Core data lives under `data/`, plugins under `js/plugins/`, and project docs at the repo root.
- Treat generated RPG Maker JSON carefully. Prefer small targeted edits, validate JSON after changing it, and avoid broad formatting rewrites.
- Existing backup files such as `*.bak` and `*.corrupt_bak` may be user-created recovery evidence. Do not delete them unless explicitly asked.

