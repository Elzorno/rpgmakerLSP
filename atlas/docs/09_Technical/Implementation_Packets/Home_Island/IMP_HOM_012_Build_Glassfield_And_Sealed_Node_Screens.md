---
object_id: IMP-HOM-012
atlas_id: IMP-HOM-012
title: Build Glassfield and Sealed Node Screens
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - SCR-HOM-GLS-001
    - SCR-HOM-SND-001
    - SCR-HOM-SND-002
    - SCR-HOM-SND-003
    - SCR-HOM-SND-004
  requires:
    - IMP-HOM-002
    - IMP-HOM-004
    - IMP-HOM-011
    - ATLAS-TEC-055
---

# Implementation Packet: Build Glassfield and Sealed Node Screens

## Objective

Create the screen-level production plan for the Journey I climax route from Glassfield Ruins through Relay Node Seven.

---

## Screens To Build

| Screen ID | Map Name | Purpose |
|---|---|---|
| SCR-HOM-GLS-001 | DGN_Glassfield_Ruins_Exterior | Surface ruins and sealed entry |
| SCR-HOM-SND-001 | DGN_SealedNode_Upper | First underground node area |
| SCR-HOM-SND-002 | DGN_SealedNode_CorePath | Connector toward boss chamber |
| SCR-HOM-SND-003 | DGN_SealedNode_Guardian | Node Seven Guardian battle |
| SCR-HOM-SND-004 | DGN_SealedNode_RelayCore | Relay Node Seven resolution |

---

## Build Order

1. SCR-HOM-GLS-001
2. SCR-HOM-SND-001
3. SCR-HOM-SND-002
4. SCR-HOM-SND-003
5. SCR-HOM-SND-004

---

## Required Transfers

| From | To |
|---|---|
| SCR-HOM-GLS-001 | island route / Ashford route |
| SCR-HOM-GLS-001 | SCR-HOM-SND-001 after seal opens |
| SCR-HOM-SND-001 | SCR-HOM-GLS-001 |
| SCR-HOM-SND-001 | SCR-HOM-SND-002 |
| SCR-HOM-SND-002 | SCR-HOM-SND-001 |
| SCR-HOM-SND-002 | SCR-HOM-SND-003 |
| SCR-HOM-SND-003 | SCR-HOM-SND-002 |
| SCR-HOM-SND-003 | SCR-HOM-SND-004 after guardian defeat |
| SCR-HOM-SND-004 | SCR-HOM-SND-003 |

---

## Required Story Logic

- Glassfield lower entrance requires `J1_Sword_Obtained`.
- Opening the lower entrance sets `J1_Glassfield_SealOpened`.
- Entering Sealed Node sets `J1_SealedNode_Entered`.
- Defeating the guardian sets `J1_Node07_GuardianDefeated`.
- Relay event sets Node Seven and mainland travel states.
- Event pages follow `ATLAS-TEC-055`.

---

## Acceptance Criteria

- Player cannot enter Sealed Node before obtaining the Sword.
- Player can move through all Sealed Node screens in order.
- Guardian blocks relay chamber access until defeated.
- Relay event updates archive recovery and mainland travel state.
- Player can return after completion.
- No screen requires custom plugins.

---

## Playtest Steps

1. Visit Glassfield before Sword and confirm lower entrance is unavailable.
2. Obtain Sword.
3. Return to Glassfield and open lower entrance.
4. Enter Sealed Node.
5. Reach guardian chamber.
6. Defeat guardian.
7. Resolve Relay Node Seven.
8. Confirm `Archive_Recovery_Percent = 5` and `J1_Mainland_TravelUnlocked = ON`.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Glassfield and Sealed Node screen implementation packet |
