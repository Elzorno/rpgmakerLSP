---
object_id: SCR-HOM-SND-004
atlas_id: SCR-HOM-SND-004
title: Relay Node Seven Core
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-SND-001
rpg_maker_map_name: DGN_SealedNode_RelayCore
relationships:
  located_in:
    - LOC-SND-001
  contains:
    - REL-007
  implements:
    - IMP-HOM-004
---

# SCR-HOM-SND-004 — Relay Node Seven Core

## Purpose

This is the Journey I resolution screen. Kai uses the Sword at Relay Node Seven and the mainland travel state becomes available.

## Map Intent

A small focused chamber with the relay device at the center.

Recommended approximate size: 23 x 19 tiles.

## Required Visual Elements

- Central relay device.
- Blue-white light.
- Symmetrical old-world chamber shape.
- Return path to guardian chamber.

## Required Events

| Event | Purpose |
|---|---|
| Relay Device | Resolves Node Seven |
| Archive Message | Shows node status and archive recovery |
| Transfer Back | Returns to SCR-HOM-SND-003 |

## Event Result

On interaction after guardian defeat:

```text
J1_Node07_Offline = ON
Archive_Recovery_Percent = 5
Current_Relay_Count = 1
J1_Mainland_TravelUnlocked = ON
NPC_Ashford_PostNode07 = ON
```

Suggested message:

```text
NODE SEVEN: OFFLINE
ARCHIVE RECOVERY: 5%
```

## Acceptance Criteria

- Event can only complete once.
- Required switches and variables update.
- Archive message displays clearly.
- Mainland travel state unlocks.
- Player can return after the event.

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Relay Node Seven Core screen object |
