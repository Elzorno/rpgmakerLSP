---
atlas_id: ATLAS-AI-011
title: Home Island Codex Task Breakdown
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
dependencies:
  - ATLAS-AI-010
  - ATLAS-TEC-032
related:
  - IMP-HOM-009
---

# Home Island Codex Task Breakdown

This document converts the Home Island backlog into a practical Codex execution sequence.

---

## Purpose

This handoff gives Codex a safe order of operations and prevents large, risky, hard-to-review changes.

---

## Working Rule

Codex should implement one task group at a time and report back before continuing.

Do not combine map creation, database work, dialogue, and battle logic in one large opaque change.

---

## Task Group 1 — State Backbone

Source: `IMP-HOM-002`

Build:

- Journey I switches.
- Journey I variables.
- Any helper common events needed for archive text placeholders.

Report:

- switch names created,
- variable names created,
- common events created,
- any ID conflicts.

---

## Task Group 2 — Ashford Shell

Source: `IMP-HOM-001`

Build:

- Ashford exterior placeholder map.
- Elara house interior.
- basic transfers.
- starting position.
- hidden item event.

Report:

- maps created,
- transfer events created,
- player start location,
- hidden item implementation.

---

## Task Group 3 — Ashford NPCs

Source: `IMP-HOM-006`

Build:

- Elara event pages.
- six placeholder village NPCs.
- dialogue switch conditions.

Report:

- NPC events created,
- states implemented,
- any dialogue still placeholder.

---

## Task Group 4 — Enemy Database

Source: `IMP-HOM-005`

Build:

- Meadow Gel.
- Ash Rat.
- Marsh Gel.
- Node Seven Guardian placeholder.
- first test troops.

Report:

- enemy IDs used,
- troop IDs used,
- placeholder battlers used,
- early balance concerns.

---

## Task Group 5 — Sword Sequence

Source: `IMP-HOM-003`

Build:

- Skyreach Hill map.
- Hidden Cave map or maps.
- trial events.
- Sword pedestal event.
- archive recovery to 3%.

Report:

- maps created,
- trial logic,
- item/weapon handling for the Sword,
- archive variable update.

---

## Task Group 6 — Node Seven Sequence

Source: `IMP-HOM-004`

Build:

- Glassfield Ruins map.
- Sealed Node map or maps.
- boss event.
- relay shutdown event.
- archive recovery to 5%.
- mainland travel unlock switch.

Report:

- maps created,
- boss event behavior,
- relay core event behavior,
- final switch and variable state.

---

## Task Group 7 — Hooks and Review

Sources:

- `IMP-HOM-008`
- `ATLAS-TEC-030`

Build:

- placeholder audio hooks.
- run through vertical slice checklist.

Report using:

```markdown
# Codex Report

## Task Group Completed

## Files Changed

## Maps Created

## Database Entries

## Switches / Variables

## Playtest Result

## Problems

## Next Recommended Task Group
```

---

## Stop Conditions

Codex should stop and ask for direction if:

- a required Atlas object is missing,
- canonical switch names conflict with existing game data,
- the current project structure does not match assumptions,
- a plugin would be required,
- a change would delete prototype work.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Codex task breakdown |
