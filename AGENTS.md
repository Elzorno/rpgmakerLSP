# Agent Collaboration Guide

This repository is shared by Codex and Claude. Use the repo-local coordination files in `.agents/` before making changes.

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

