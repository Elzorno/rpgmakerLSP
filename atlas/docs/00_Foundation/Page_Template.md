---
atlas_id: ATLAS-FND-005
title: Page Template
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Applicable
dependencies:
  - ATLAS-FND-004
related:
  - ATLAS-FND-003
---

# Page Template

Use this template when creating new Atlas pages.

---

## Template

```markdown
---
atlas_id: ATLAS-XXX-000
title: Page Title
status: Draft
version: 0.1
canonical: false
owner: Creative Director
implementation_status: Not Started
dependencies: []
related: []
---

# Page Title

## Purpose

What question does this page answer?

## Scope

What is included and excluded?

## Canonical Decisions

List the decisions this page establishes.

## Design Layer

What does the player experience?

## Hidden Layer

What is actually happening beneath the fantasy presentation?

## Production Layer

How should this influence implementation, art, writing, or AI tasks?

## Related Pages

- Link to related Atlas pages.

## Open Questions

- List unresolved decisions.

## Future Expansion

- List planned additions.

## Implementation Tasks

- List tasks for Codex, Claude, art generation, or RPG Maker.

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial draft |
```

---

## Page Design Rule

Every Atlas page should answer one primary question.

If a page tries to answer too many unrelated questions, split it.

---

## Layer Rule

When possible, pages should distinguish between:

1. **Design Layer** — what the player sees.
2. **Hidden Layer** — what is actually true in the world.
3. **Production Layer** — how contributors implement it.

This keeps Atlas useful for writers, artists, programmers, and AI agents.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial page template |
