---
object_id: SCR-HOM-SND-001
atlas_id: SCR-HOM-SND-001
title: Sealed Node Upper
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-SND-001
rpg_maker_map_name: DGN_SealedNode_Upper
relationships:
  located_in:
    - LOC-SND-001
  implements:
    - IMP-HOM-004
---

# SCR-HOM-SND-001 — Sealed Node Upper

## Purpose

Sealed Node Upper is the first underground screen beneath Glassfield Ruins.

It should begin as cave and ruin, then hint that the player is entering old-world infrastructure.

---

## Map Intent

A short entry dungeon screen that introduces Sealed Node tone and leads toward the core path.

Recommended approximate size:

```text
34 x 30 tiles
```

---

## Required Visual Elements

- Stone corridor entry from Glassfield.
- Cracked walls with embedded metal or glass.
- Faint red unstable lights deeper in.
- One simple gate or obstacle.
- Clear forward route to core path.

---

## Required Events

| Event | Purpose |
|---|---|
| First Entry Event | Sets `J1_SealedNode_Entered` |
| Optional Archive Distortion | Short mysterious text or sound |
| Transfer Up | Returns to Glassfield Ruins Exterior |
| Transfer Forward | Leads to SCR-HOM-SND-002 |

---

## Switches Used

```text
J1_SealedNode_Entered
```

---

## Audio

Use Sealed Node ambience: low hum, cave drip, and distant pulse.

---

## Encounters

Optional low-frequency encounters.

Recommended first-pass enemies:

- Ash Rat
- Meadow Gel
- optional early construct later

---

## Acceptance Criteria

- First entry sets correct switch.
- Player can return to Glassfield.
- Player can proceed deeper.
- Screen visually transitions from natural cave to system ruin.
- No puzzle complexity yet.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Sealed Node Upper screen object |
