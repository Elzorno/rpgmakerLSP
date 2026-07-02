---
atlas_id: ATLAS-FND-010
title: Screen Object Standard
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Active
dependencies:
  - ATLAS-FND-006
  - ATLAS-FND-007
  - ATLAS-FND-008
related:
  - ATLAS-VOL-002
---

# Screen Object Standard

The Screen Object Standard defines how Atlas documents individual playable screens for _The Last Sword Protocol_.

A screen is the smallest production-ready world unit.

---

## Purpose

This standard answers:

> What information must exist before Codex can build a specific RPG Maker MZ screen without inventing design details?

---

## Definition

A screen is a single playable RPG Maker map or a clearly bounded area of a map that can be implemented, reviewed, and playtested independently.

Examples:

- Ashford exterior
- Elara house interior
- Skyreach Hill path
- Hidden Cave sanctum
- Coalmouth mine rail switch chamber

---

## Screen ID Format

```text
SCR-REGION-LOCATION-NUMBER
```

Examples:

```text
SCR-HOM-ASH-001
SCR-HOM-ASH-002
SCR-HOM-SKY-001
SCR-COA-MIN-001
```

---

## Required Screen Fields

Every screen object must define:

- screen ID,
- parent region,
- parent location,
- RPG Maker map name,
- story state range,
- dimensions or approximate size,
- tileset intent,
- transfer points,
- NPCs/events,
- treasure/hidden items,
- audio,
- encounter rules,
- switches and variables touched,
- acceptance criteria.

---

## Screen Completion Rule

A screen is complete only when another agent can build it without asking:

- where things go,
- what events exist,
- what switches are used,
- what dialogue appears,
- what transfers connect,
- what happens after completion.

---

## Relationship to Locations

Locations describe purpose, tone, and story role.

Screens describe exact production units.

A single location may contain many screens.

Example:

```text
LOC-ASH-001 Ashford
  SCR-HOM-ASH-001 Ashford Exterior
  SCR-HOM-ASH-002 Elara House Interior
  SCR-HOM-ASH-003 Ashford Shop Interior
```

---

## Relationship to Implementation Packets

Implementation packets may group multiple screens into a sprint.

Screen objects remain the ground truth for exact map/event content.

---

## Open Questions

- Should screen IDs be registered in the Canonical ID Registry immediately?
- Should every RPG Maker map equal one screen, or can large maps contain multiple screens?
- Should screen objects include rough coordinate grids in Atlas or only in implementation packets?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial screen object standard |
