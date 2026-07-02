---
object_id: SCR-HOM-SND-002
atlas_id: SCR-HOM-SND-002
title: Sealed Node Core Path
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-SND-001
rpg_maker_map_name: DGN_SealedNode_CorePath
relationships:
  located_in:
    - LOC-SND-001
  implements:
    - IMP-HOM-004
---

# SCR-HOM-SND-002 — Sealed Node Core Path

## Purpose

This screen moves the player from cave-like ruins into the first clearly artificial space beneath Glassfield.

## Map Intent

A short dungeon connector that leads from the upper node area to the guardian chamber.

Recommended approximate size: 38 x 32 tiles.

## Required Visual Elements

- Cave walls mixed with old panels.
- Cable-like roots in the walls.
- Glass or metal surfaces.
- Faint relay-line markings.
- One simple sealed door.

## Required Events

| Event | Purpose |
|---|---|
| Sealed Door | Simple interaction gate |
| Transfer Back | Returns to SCR-HOM-SND-001 |
| Transfer Forward | Leads to SCR-HOM-SND-003 |

## Switches Used

```text
J1_SealedNode_Entered
J1_CorePath_DoorOpened
```

## Encounters

Use one or two simple encounters if needed.

## Acceptance Criteria

- Player can reach the guardian chamber.
- Player can return to the previous screen.
- Any door logic is simple and event-driven.
- No softlock risk.

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Sealed Node Core Path screen object |
