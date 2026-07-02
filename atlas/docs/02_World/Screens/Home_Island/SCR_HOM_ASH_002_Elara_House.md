---
object_id: SCR-HOM-ASH-002
atlas_id: SCR-HOM-ASH-002
title: Elara House Interior
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-ASH-001
rpg_maker_map_name: INT_Ashford_ElaraHouse
relationships:
  located_in:
    - LOC-ASH-001
  contains:
    - NPC-ELA-001
  implements:
    - IMP-HOM-001
    - IMP-HOM-006
---

# SCR-HOM-ASH-002 — Elara House Interior

## Purpose

Elara House is the emotional starting room of the game.

It should communicate family, safety, memory, and quiet warnings.

---

## Map Intent

Small cozy interior.

Recommended approximate size:

```text
17 x 13 tiles
```

---

## Required Visual Elements

- Kai's bed or sleeping area.
- Elara's chair or table.
- Hearth or warm-stone equivalent.
- Family shelf / old keepsake.
- Small old-world object treated as decoration.
- Exit to Ashford Exterior.

---

## Required Events

| Event | Purpose |
|---|---|
| Player Start | New game begins here unless changed later |
| Elara | Main opening interaction |
| Transfer Exit | Leads to SCR-HOM-ASH-001 |
| Optional Bookshelf/Keepsake | Small lore line |

---

## Elara Dialogue States

Use `ATLAS-STY-010` as source.

Required states:

```text
Intro
After Tremor
After Sword
After Node Seven
Before Mainland Departure
```

---

## Switches Used

```text
J1_Ashford_IntroComplete
J1_Tremor_Event
J1_Sword_Obtained
J1_Node07_Offline
J1_Mainland_TravelUnlocked
```

---

## Audio

Use Ashford interior or town BGM placeholder.

No battle music.

---

## Encounters

None.

---

## Transfer Points

| Destination | Condition |
|---|---|
| SCR-HOM-ASH-001 Ashford Exterior | Always available after intro dialogue, or immediately if free-start design is chosen |

---

## Acceptance Criteria

- New game can start here.
- Elara is interactable.
- Exit works.
- Dialogue can change by story switch.
- Room feels safe and personal.

---

## Open Questions

- Should the player be required to talk to Elara before leaving?
- Should Elara give a starting item?
- Should the old keepsake foreshadow Project Excalibur?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Elara House screen object |
