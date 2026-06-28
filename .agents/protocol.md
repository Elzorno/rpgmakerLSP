# Codex-Claude Protocol

## Goals

- Keep both agents aware of current work.
- Avoid simultaneous edits to the same files.
- Preserve useful context for the user.
- Make handoffs auditable and easy to resume.

## Shared Files

- `.agents/task-board.md` is the source of truth for active ownership.
- `.agents/outbox/codex.md` is written by Codex.
- `.agents/outbox/claude.md` is written by Claude.
- `.agents/templates/` contains copyable formats.

## Before Starting Work

1. Read this file.
2. Read `.agents/task-board.md`.
3. Read the other agent's outbox.
4. Run `git status --short` and note any unrelated changes.
5. Claim the task in `.agents/task-board.md` before editing project files.

## Task Ownership

Use this format in `.agents/task-board.md`:

```md
| ID | Owner | Status | Files | Summary | Updated |
| --- | --- | --- | --- | --- | --- |
| T001 | Claude | Active | data/Map001.json | Add transfer event | 2026-06-27 21:45 ET |
```

Statuses:

- `Proposed` - suggested but not started.
- `Active` - currently owned by one agent.
- `Blocked` - waiting on user, tool access, or another task.
- `Review` - ready for another agent or the user to inspect.
- `Done` - completed and summarized.

Do not edit files owned by another active task unless the user explicitly redirects the work or the owning agent has handed it off.

## Messages

Append messages to your own outbox. Do not rewrite another agent's outbox except to fix obvious formatting damage.

Each message should include:

- Timestamp with timezone.
- Author.
- Recipient.
- Related task ID.
- Summary.
- Files touched.
- Verification.
- Open questions or next steps.

Use `.agents/templates/message.md` for general notes and `.agents/templates/handoff.md` for work handoffs.

## Editing Rules

- Keep changes scoped to the claimed task.
- Do not delete backups, save data, or generated assets unless the user asks.
- For JSON under `data/`, preserve the RPG Maker structure and validate JSON after edits.
- Mention any file you intentionally leave dirty or unverified.
- If you see unexpected user changes, preserve them and work around them.

## Conflict Handling

If both agents need the same file:

1. Stop before editing.
2. Mark your task `Blocked` or `Review`.
3. Leave a short outbox note naming the conflicting file and proposed order.
4. Wait for the user or the other agent to hand off ownership.

