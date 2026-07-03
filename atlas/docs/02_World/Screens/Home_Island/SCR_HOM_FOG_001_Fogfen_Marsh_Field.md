---
object_id: SCR-HOM-FOG-001
atlas_id: SCR-HOM-FOG-001
title: Fogfen Marsh Field
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-FOG-001
rpg_maker_map_name: FLD_Fogfen_Marsh_Field
relationships:
  located_in:
    - LOC-FOG-001
  implements:
    - IMP-HOM-015
  connects_to:
    - SCR-HOM-FOG-002
---

# Screen: Fogfen Marsh Field

## Purpose

Fogfen Marsh Field is the main optional exploration screen for Fogfen Marsh.

It gives the player early combat practice, a hidden reward, and a restrained environmental clue that old signals disturb the marsh.

---

## Map Intent

Create a misty wetland field with reeds, shallow water, bent trees, muted green ground, and faint blue-white or pale violet signal glows.

Recommended RPG Maker map size: medium field map, approximately 36x30 to 40x32 tiles.

The player should be able to enter, explore a few side pockets, find the deeper marsh transition, and return without the screen becoming a critical-path gate.

---

## Required Visual Elements

- shallow water channels,
- reed walls that guide paths,
- one bent tree or broken post near the hidden item,
- one exposed or submerged cable landmark,
- one faintly glowing pool or reed cluster for the signal clue,
- mist or muted lighting consistent with `LOC-FOG-001`.

---

## Required Screen Objects

| Object ID | Type | Purpose | Traceability |
|---|---|---|---|
| OBJ-HOM-FOG-001 | Transition Point | Entry and exit marker linking Fogfen Marsh Field to the Home Island route | LOC-FOG-001, IMP-HOM-015, ATLAS-TEC-043 |
| OBJ-HOM-FOG-002 | Transition Point | Transfer from Fogfen Marsh Field to Deeper Marsh Pocket | LOC-FOG-001, IMP-HOM-015 |
| OBJ-HOM-FOG-003 | Interactive Object | Signal-tick reed pool examine event | LOC-FOG-001, ATLAS-TEC-052, IMP-HOM-015 |
| OBJ-HOM-FOG-004 | Interactive Object | Bent cable landmark used as the environmental signpost | LOC-FOG-001, ATLAS-TEC-052 |
| OBJ-HOM-FOG-005 | Collectible Location | Hidden item landmark tied to optional exploration | LOC-FOG-001, SYS-EXPLORATION-001, IMP-HOM-015 |
| HZD-HOM-FOG-001 | Environmental Hazard | Shallow bog slow-tile region or pathing choke point | LOC-FOG-001, IMP-HOM-015 |
| ENC-HOM-FOG-001 | Encounter Region | Low-level marsh encounter region using Atlas-supported Home Island enemies | IMP-HOM-005, IMP-HOM-015 |

---

## NPC Placement

No required NPC is placed on this screen.

If a later packet adds an NPC clue for the hidden item, place that NPC near the Home Island route side of `OBJ-HOM-FOG-001` so Fogfen remains optional and easy to exit.

---

## Environmental Hazards

| Hazard ID | Behavior | Notes |
|---|---|---|
| HZD-HOM-FOG-001 | Slows or narrows movement through shallow bog tiles | Do not damage the player in the first pass unless a later packet explicitly requires it |

---

## Treasure / Collectibles

| Object ID | Reward Role | Notes |
|---|---|---|
| OBJ-HOM-FOG-005 | Optional hidden item | Use a small early-game reward already supported by implementation inventory standards |

The hidden item should be discoverable from the landmark layout, not required for critical progression.

---

## Transition Points

| Object ID | From | To | Rule |
|---|---|---|---|
| OBJ-HOM-FOG-001 / TRN-HOM-027 | Home Island route or Ashford-side route hub | SCR-HOM-FOG-001 | Optional entry route |
| OBJ-HOM-FOG-001 / TRN-HOM-028 | SCR-HOM-FOG-001 | Home Island route or Ashford-side route hub | Must always allow return |
| OBJ-HOM-FOG-002 / TRN-HOM-029 | SCR-HOM-FOG-001 | SCR-HOM-FOG-002 | Optional branch; no story gate |

---

## Quest Triggers

No required quest trigger is placed on this screen.

The signal clue may set an optional exploration flag if implementation needs one, but it must not block the Journey I critical path.

---

## Encounter Guidance

Use only enemies already supported by Atlas or Home Island enemy packets.

Preferred encounter pool:

- Marsh Gel,
- Ash Rat,
- Field Crow if available in implementation,
- no new enemy family.

---

## Truth Layer Alignment

| Layer | Screen Expression |
|---|---|
| Story Layer | A marsh that villagers avoid because it feels subtly wrong |
| Gameplay Layer | Optional exploration, simple combat practice, hidden reward, and safe return |
| Cybersecurity / Hidden Layer | Signal disturbance appears only as environmental behavior, not direct exposition |
| Implementation Layer | RPG Maker map, transfer events, examine events, encounter regions, self-switch hidden item |

---

## Acceptance Criteria

- Player can enter and leave without becoming trapped.
- `OBJ-HOM-FOG-001` and `OBJ-HOM-FOG-002` transfer targets are clear.
- At least one optional hidden item landmark exists.
- The signal clue supports `LOC-FOG-001` and `ATLAS-TEC-052` without adding new lore.
- Encounter setup uses Home Island-supported enemies only.
- Fogfen remains optional and does not gate the critical path.

---

## Open Questions

- Should a future packet add an NPC clue before the player enters Fogfen?
- Should Marsh Gel introduce a status-effect tutorial later?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Fogfen Marsh Field screen object specification |
