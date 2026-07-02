---
object_id: SCR-HOM-HCV-001
atlas_id: SCR-HOM-HCV-001
title: Hidden Cave Entrance
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-HCV-001
rpg_maker_map_name: DGN_HiddenCave_Entrance
relationships:
  located_in:
    - LOC-HCV-001
  implements:
    - IMP-HOM-003
---

# SCR-HOM-HCV-001 — Hidden Cave Entrance

## Purpose

Hidden Cave Entrance transitions the player from forbidden hill to sacred trial space.

It should feel like a natural cave at first, with small signs that something intentionally shaped it.

---

## Map Intent

Compact cave entry screen with one forward path into the trial area.

Recommended approximate size:

```text
24 x 24 tiles
```

---

## Required Visual Elements

- Cave mouth / entry passage.
- Reflective stone or glassy mineral patches.
- Subtle geometric wall carvings.
- Dim blue-white accent light.
- Clear forward passage to trial chamber.
- Return passage to Skyreach Hill.

---

## Required Events

| Event | Purpose |
|---|---|
| First Entry Event | Sets `J1_HiddenCave_Entered` |
| Transfer to Skyreach Hill | Exit back to SCR-HOM-SKY-001 |
| Transfer to Trial Chamber | Leads to SCR-HOM-HCV-002 |
| Optional Wall Carving Examine | Hints at challenge-response without using jargon |

---

## Switches Used

```text
J1_HiddenCave_Entered
```

---

## Audio

Use sparse cave ambience. Reduce melody compared to Skyreach Hill.

---

## Encounters

None required in first pass.

---

## Acceptance Criteria

- Entering the cave sets the correct switch.
- Player can return to Skyreach Hill.
- Player can proceed to the trial chamber.
- Visual design feels sacred before technical.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Hidden Cave Entrance screen object |
