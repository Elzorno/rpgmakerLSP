---
object_id: IMP-HOM-015
atlas_id: IMP-HOM-015
title: Build Fogfen Marsh
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - LOC-FOG-001
    - SCR-HOM-FOG-001
    - SCR-HOM-FOG-002
  requires:
    - IMP-HOM-002
    - IMP-HOM-005
    - ATLAS-TEC-031
    - ATLAS-TEC-052
    - ATLAS-TEC-055
---

# Implementation Packet: Build Fogfen Marsh

## Objective

Create the implementation-facing production packet for Fogfen Marsh as optional Home Island exploration content.

Fogfen should provide early combat practice, optional discovery, and a restrained environmental hint that old signals affect living things.

---

## Traceability

| Source | Role |
|---|---|
| LOC-FOG-001 | Location object for Fogfen Marsh |
| SCR-HOM-FOG-001 | Main Fogfen Marsh Field screen object |
| SCR-HOM-FOG-002 | Deeper Marsh Pocket screen object |
| ATLAS-TEC-031 | Identifies Fogfen Marsh as a known packet gap |
| ATLAS-TEC-032 | Places optional Fogfen side content in the parking lot |
| IMP-HOM-005 | Home Island enemy database packet for early enemies |
| ATLAS-TEC-052 | Defines layer discipline for story, gameplay, hidden truth, and implementation |
| ATLAS-TEC-055 | Defines executable Fogfen event pages |

---

## Screens To Build

| Screen ID | RPG Maker Map Name | Purpose |
|---|---|
| SCR-HOM-FOG-001 | FLD_Fogfen_Marsh_Field | Main optional marsh exploration map |
| SCR-HOM-FOG-002 | FLD_Fogfen_Deeper_Marsh_Pocket | Small optional landmark / hidden item pocket |

---

## Build Order

1. Create `SCR-HOM-FOG-001` using `FLD_Fogfen_Marsh_Field`.
2. Add entry and exit transfer event `OBJ-HOM-FOG-001` from the Home Island route.
3. Create `SCR-HOM-FOG-002` using `FLD_Fogfen_Deeper_Marsh_Pocket`.
4. Wire `OBJ-HOM-FOG-002` and `OBJ-HOM-FOG-006` as the round-trip transfer pair between the two Fogfen screens.
5. Add optional hidden item landmarks `OBJ-HOM-FOG-005` and, if desired, `OBJ-HOM-FOG-009`.
6. Add low-level encounter setup or event encounters using existing Home Island enemy definitions.
7. Add environmental clue text through `OBJ-HOM-FOG-003`, `OBJ-HOM-FOG-007`, or `OBJ-HOM-FOG-008` that points to signal disturbance without direct technical exposition.

---

## Encounter Guidance

Use only enemies already supported by Atlas or existing Home Island enemy packets.

Recommended options from `LOC-FOG-001`:

- Marsh Gel,
- Ash Rat,
- Field Crow if available,
- small marsh predator if later defined.

Do not invent a new enemy family in this packet.

---

## Required Events

| Event / Object ID | Purpose |
|---|---|
| OBJ-HOM-FOG-001 / TRN-HOM-027 / TRN-HOM-028 | Brings player into the marsh from the Home Island route and returns them safely |
| OBJ-HOM-FOG-002 / TRN-HOM-029 | Transfers from Fogfen Marsh Field to Deeper Marsh Pocket |
| OBJ-HOM-FOG-006 / TRN-HOM-030 | Returns from Deeper Marsh Pocket to Fogfen Marsh Field |
| OBJ-HOM-FOG-005 | Rewards optional exploration in the main field |
| OBJ-HOM-FOG-009 | Optional deeper-marsh reward cache |
| OBJ-HOM-FOG-003 / OBJ-HOM-FOG-008 | Foreshadows old infrastructure through environmental behavior |

---

## Truth Layer Alignment

Fogfen's visible layer is a misty wetland villagers avoid at dusk.

Its hidden layer is residual old-world signal or electromagnetic disturbance affecting wildlife and the environment.

Its gameplay layer is optional exploration, simple combat practice, and hidden-item reward.

Its implementation layer should use maps, transfers, event text, enemy encounters, and item events.

---

## Acceptance Criteria

- Fogfen is clearly optional unless a later story packet makes it required.
- Player can enter and leave without becoming trapped.
- At least one optional reward exists.
- Encounter setup uses existing or Atlas-supported enemies.
- Environmental clue supports the hidden signal idea without new lore.
- `SCR-HOM-FOG-001` and `SCR-HOM-FOG-002` are implemented or explicitly scheduled.

---

## Playtest Steps

1. Enter Fogfen from the Home Island route through `OBJ-HOM-FOG-001`.
2. Confirm exit path works.
3. Transfer from `SCR-HOM-FOG-001` to `SCR-HOM-FOG-002` and back.
4. Trigger at least one encounter if encounters are enabled.
5. Find the hidden item landmark.
6. Examine the signal clue.
7. Confirm the player can return to the main Home Island route.

---

## Open Questions

- Should Marsh Gel introduce the first status-effect tutorial?
- Should Fogfen remain fully optional for the vertical slice?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Fogfen Marsh implementation packet |
| 0.2 | Added canonical Fogfen screen object references |
