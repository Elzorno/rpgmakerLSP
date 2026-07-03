---
object_id: SCR-HOM-FOG-002
atlas_id: SCR-HOM-FOG-002
title: Deeper Marsh Pocket
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-FOG-001
rpg_maker_map_name: FLD_Fogfen_Deeper_Marsh_Pocket
relationships:
  located_in:
    - LOC-FOG-001
  implements:
    - IMP-HOM-015
  connects_to:
    - SCR-HOM-FOG-001
---

# Screen: Deeper Marsh Pocket

## Purpose

Deeper Marsh Pocket is a small optional Fogfen branch used for a stronger environmental hint, a contained reward, and a safe return to the main marsh field.

It must not introduce a required story gate or unsupported mechanic.

---

## Map Intent

Create a compact marsh pocket with denser reeds, deeper water edges, a submerged cable cluster, and a visibly strange pool or signal disturbance.

Recommended RPG Maker map size: small pocket map, approximately 20x18 to 24x20 tiles.

The map should feel like a short detour from `SCR-HOM-FOG-001`, not a dungeon.

---

## Required Visual Elements

- dense reeds shaping a short loop or pocket,
- darker water or mud edges,
- submerged cable cluster,
- one signal pool or flickering reflection,
- optional reward cache near a landmark,
- clear return route back to Fogfen Marsh Field.

---

## Required Screen Objects

| Object ID | Type | Purpose | Traceability |
|---|---|---|---|
| OBJ-HOM-FOG-006 | Transition Point | Return transfer from Deeper Marsh Pocket to Fogfen Marsh Field | SCR-HOM-FOG-001, IMP-HOM-015 |
| OBJ-HOM-FOG-007 | Interactive Object | Submerged cable cluster examine event | LOC-FOG-001, ATLAS-TEC-052 |
| OBJ-HOM-FOG-008 | Interactive Object | Signal pool examine event for the strongest Fogfen clue | LOC-FOG-001, ATLAS-TEC-052, IMP-HOM-015 |
| OBJ-HOM-FOG-009 | Collectible Location | Optional reward cache for deeper exploration | SYS-EXPLORATION-001, IMP-HOM-015 |
| HZD-HOM-FOG-002 | Environmental Hazard | Deep reed choke point or slow passage | LOC-FOG-001, IMP-HOM-015 |
| ENC-HOM-FOG-002 | Encounter Region | Slightly denser optional marsh encounter region | IMP-HOM-005, IMP-HOM-015 |

---

## NPC Placement

No required NPC is placed on this screen.

Do not place critical dialogue here unless a later story packet makes Fogfen required.

---

## Environmental Hazards

| Hazard ID | Behavior | Notes |
|---|---|---|
| HZD-HOM-FOG-002 | Slows movement or narrows passage through dense reeds | Should communicate depth and unease without creating a trap |

---

## Treasure / Collectibles

| Object ID | Reward Role | Notes |
|---|---|---|
| OBJ-HOM-FOG-009 | Optional deeper-marsh reward | Use an existing early-game item or resource; do not add new item lore here |

---

## Transition Points

| Object ID | From | To | Rule |
|---|---|---|---|
| OBJ-HOM-FOG-006 / TRN-HOM-030 | SCR-HOM-FOG-002 | SCR-HOM-FOG-001 | Must always allow return |

---

## Quest Triggers

No required quest trigger is placed on this screen.

The signal pool examine event may set an optional discovery flag if needed for implementation tracking, but no critical-path switch may depend on it.

---

## Encounter Guidance

Use the same supported enemy pool as `SCR-HOM-FOG-001`.

This pocket may slightly increase encounter density, but it should remain early-game safe.

---

## Truth Layer Alignment

| Layer | Screen Expression |
|---|---|
| Story Layer | A deeper wetland pocket where the marsh's wrongness is easier to notice |
| Gameplay Layer | Optional detour, return transfer, environmental examine event, and reward cache |
| Cybersecurity / Hidden Layer | Submerged infrastructure and signal disturbance are implied through the environment |
| Implementation Layer | Compact RPG Maker map, return transfer, examine events, encounter region, reward event |

---

## Acceptance Criteria

- Player can return to `SCR-HOM-FOG-001` at any time.
- The screen contains no critical-path story gate.
- Signal and cable objects are environmental clues only.
- Optional reward does not require new item lore.
- Encounter setup uses Home Island-supported enemies only.

---

## Open Questions

- Should this pocket be accessible immediately, or after a future exploration tutorial?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Deeper Marsh Pocket screen object specification |
