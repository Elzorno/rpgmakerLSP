---
object_id: SCR-HOM-SND-003
atlas_id: SCR-HOM-SND-003
title: Sealed Node Guardian Chamber
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-SND-001
rpg_maker_map_name: DGN_SealedNode_Guardian
relationships:
  located_in:
    - LOC-SND-001
  contains:
    - BOS-N07-001
  implements:
    - IMP-HOM-004
---

# SCR-HOM-SND-003 — Sealed Node Guardian Chamber

## Purpose

This screen hosts the Journey I boss encounter against the Node Seven Guardian.

## Map Intent

A compact boss chamber before the relay core.

Recommended approximate size: 27 x 23 tiles.

## Required Visual Elements

- Central open combat area.
- Guardian placement point.
- Closed-looking passage toward relay core.
- Old stone and machine details blended together.
- Strong visual focus on the guardian.

## Required Events

| Event | Purpose |
|---|---|
| Guardian Event | Starts boss battle |
| Post-Battle State | Sets guardian defeated switch |
| Transfer Back | Returns to SCR-HOM-SND-002 |
| Transfer Forward | Leads to SCR-HOM-SND-004 after guardian defeat |

## Boss Logic

Defeating the guardian should set:

```text
J1_Node07_GuardianDefeated
```

Forward transfer to the relay core should require this switch.

## Switches Used

```text
J1_Node07_GuardianDefeated
```

## Audio

Use boss battle BGM placeholder for battle.

After battle, return to Sealed Node ambience.

## Acceptance Criteria

- Boss battle starts correctly.
- Victory sets the correct switch.
- Relay core path is blocked before victory.
- Player can proceed after victory.
- Boss does not respawn after defeat unless intentionally reset.

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Guardian Chamber screen object |
