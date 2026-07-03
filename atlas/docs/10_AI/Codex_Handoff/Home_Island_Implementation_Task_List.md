---
atlas_id: ATLAS-AI-012
title: Home Island Implementation Task List
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-045
related:
  - ATLAS-AI-010
---

# Home Island Implementation Task List

This document converts the Home Island backlog into Codex-sized work units.

Each task should be small enough to implement, test, and report on without needing to reinterpret the whole Atlas.

---

## Codex Working Rule

Codex should work one task at a time.

Each task must end with:

```markdown
## Implementation Report

### Completed
### Files Changed
### Atlas IDs Implemented
### Test Steps Performed
### Issues / Questions
```

---

## Task 001 — Create Journey I State Objects

Read:

- `IMP-HOM-002`
- `ATLAS-TEC-044`

Goal:

Create or reserve Journey I switches and variables in RPG Maker MZ data.

Acceptance:

- All required `J1_*` switches exist.
- `Current_Journey`, `Archive_Recovery_Percent`, and `Current_Relay_Count` exist.
- No duplicate state names are introduced.

---

## Task 002 — Build Elara House

Read:

- `SCR-HOM-ASH-002`
- `IMP-HOM-010`
- `ATLAS-STY-010`

Goal:

Create the starting interior and Elara event scaffold.

Acceptance:

- New game starts in Elara House.
- Elara is interactable.
- Exit transfer works.

---

## Task 003 — Build Ashford Exterior

Read:

- `SCR-HOM-ASH-001`
- `ATLAS-TEC-041`
- `ATLAS-TEC-042`

Goal:

Create Ashford Exterior with placeholder NPCs, hidden item, and routes.

Acceptance:

- Required NPCs exist.
- Hidden item works once.
- Transfers to Elara House and Shop work.
- Skyreach route is gated.

---

## Task 004 — Build Ashford Shop

Read:

- `SCR-HOM-ASH-003`

Goal:

Create simple shop interior and shopkeeper placeholder.

Acceptance:

- Player can enter/exit.
- Shopkeeper event works.

---

## Task 005 — Build Skyreach Hill

Read:

- `SCR-HOM-SKY-001`
- `IMP-HOM-011`

Goal:

Create gated route to Hidden Cave.

Acceptance:

- Route is blocked before `J1_Skyreach_AccessOpen`.
- Route opens after switch.
- Hidden Cave transfer works.

---

## Task 006 — Build Hidden Cave Trial Route

Read:

- `SCR-HOM-HCV-001`
- `SCR-HOM-HCV-002`
- `SCR-HOM-HCV-003`

Goal:

Create Hidden Cave entrance, trials, and Sword Sanctum.

Acceptance:

- Three trial switches can be set.
- Sword pedestal requires all trials.
- Sword event sets archive recovery to 3.

---

## Task 007 — Build Glassfield and Sealed Node

Read:

- `SCR-HOM-GLS-001`
- `SCR-HOM-SND-001`
- `SCR-HOM-SND-002`
- `SCR-HOM-SND-003`
- `SCR-HOM-SND-004`

Goal:

Create the Journey I climax dungeon path.

Acceptance:

- Glassfield requires Sword.
- Guardian battle resolves.
- Relay core event sets Node Seven offline and archive recovery to 5.

---

## Task 008 — Build Rustshore Departure

Read:

- `SCR-HOM-RST-001`
- `SCR-HOM-RST-002`
- `IMP-HOM-013`

Goal:

Create mainland departure gate and transition.

Acceptance:

- Boat blocked before unlock.
- Boat available after unlock.
- Departure sets `Current_Journey = 2`.

---

## Task 009 — Create Home Island Enemy Database

Read:

- `IMP-HOM-005`
- monster objects under `06_Monsters/Home_Island/`

Goal:

Create first enemy and troop database entries.

Acceptance:

- Meadow Gel, Ash Rat, Marsh Gel, and Node Seven Guardian exist.
- Test battles work.

---

## Task 010 — End-to-End Playtest

Read:

- `ATLAS-TEC-030`
- `ATLAS-TEC-043`

Goal:

Run a full new-game playtest from Elara House to Journey II start.

Acceptance:

- No manual switch changes required.
- No softlocks.
- Final state matches checklist.

---

## Task Discipline

Do not expand scope while implementing.

If a missing design decision blocks work, report the missing Atlas ID and stop rather than inventing permanent canon.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Codex-sized Home Island task list |
