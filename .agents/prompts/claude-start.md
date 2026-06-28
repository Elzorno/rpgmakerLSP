# Prompt For Claude

You are sharing this repository with Codex. Before doing any project work, use the repo-local collaboration system:

1. Read `AGENTS.md`.
2. Read `.agents/protocol.md`.
3. Read `.agents/task-board.md`.
4. Read `.agents/outbox/codex.md` for Codex messages to you.
5. Run `git status --short` and preserve any existing user or Codex changes.
6. Before editing files, claim a task row in `.agents/task-board.md` with yourself as owner.
7. Keep your edits scoped to that task.
8. When done or blocked, append a note to `.agents/outbox/claude.md` using `.agents/templates/handoff.md` or `.agents/templates/message.md`.

Project cautions:

- This is an RPG Maker MZ project.
- Be careful with `data/*.json`; preserve RPG Maker structure and validate JSON after edits.
- Do not delete `.bak`, `.corrupt_bak`, `save/`, assets, or generated project files unless the user explicitly asks.
- If Codex has an active task that touches a file you need, stop and leave a coordination note instead of editing over it.

Your first reply to the user should briefly confirm that you have read the coordination files and say which task ID you are claiming or whether you are waiting for a task.

