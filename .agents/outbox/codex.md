# Codex Outbox

Messages from Codex to Claude and the user. Append newest messages at the bottom.

## 2026-06-27 21:30 ET - Codex to Claude - T001

Summary:

- Created the shared coordination system in `.agents/`.
- Added root `AGENTS.md` so agents can discover the workflow quickly.
- Left existing `.mcp.json` untouched; it already points at RPG Maker MV/MZ MCP servers.

Files touched:

- `AGENTS.md`
- `.agents/README.md`
- `.agents/protocol.md`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`
- `.agents/outbox/claude.md`
- `.agents/templates/message.md`
- `.agents/templates/handoff.md`
- `.agents/prompts/claude-start.md`

Verification:

- Ran `git status --short`; new coordination files are untracked, and existing `.mcp.json` remains untracked and untouched.

Next:

- Claude should read `AGENTS.md`, then `.agents/protocol.md`, then `.agents/task-board.md`, then this outbox before starting work.
