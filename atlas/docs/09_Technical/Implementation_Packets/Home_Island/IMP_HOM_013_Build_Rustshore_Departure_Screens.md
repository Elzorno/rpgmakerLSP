---
object_id: IMP-HOM-013
atlas_id: IMP-HOM-013
title: Build Rustshore Departure Screens
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - SCR-HOM-RST-001
    - SCR-HOM-RST-002
  requires:
    - IMP-HOM-002
    - IMP-HOM-004
    - IMP-HOM-012
    - ATLAS-TEC-055
---

# Implementation Packet: Build Rustshore Departure Screens

## Objective

Create the screen-level production plan for Rustshore Docks and the Journey I to Journey II departure transition.

---

## Screens To Build

| Screen ID | Map Name | Purpose |
|---|---|---|
| SCR-HOM-RST-001 | TWN_Rustshore_Docks | Dock screen and mainland travel gate |
| SCR-HOM-RST-002 | CUT_Mainland_Departure | Short transition into Journey II |

---

## Build Order

1. SCR-HOM-RST-001 — Rustshore Docks
2. SCR-HOM-RST-002 — Mainland Departure

---

## Required Transfers

| From | To |
|---|---|
| Home Island route / Ashford route | SCR-HOM-RST-001 |
| SCR-HOM-RST-001 | Home Island route / Ashford route |
| SCR-HOM-RST-001 | SCR-HOM-RST-002 after confirmation and unlock |
| SCR-HOM-RST-002 | Journey II starting destination |

---

## Required Story Logic

- Boat transfer is blocked before `J1_Mainland_TravelUnlocked`.
- Boat transfer becomes available after Node Seven resolution.
- Departure asks for confirmation.
- Departure sets `Current_Journey = 2`.
- Transfer destination should point to the first Journey II implementation target when available.
- Event pages follow `ATLAS-TEC-055`.

---

## Required Switches

```text
J1_Node07_Offline
J1_Mainland_TravelUnlocked
```

---

## Required Variables

```text
Current_Journey
```

---

## Acceptance Criteria

- Player can visit Rustshore before Node Seven is resolved.
- Mainland departure is blocked before unlock.
- Mainland departure is available after unlock.
- Departure confirmation prevents accidental transition.
- Current Journey updates to Journey II.
- First Journey II transfer target is clearly marked even if placeholder.

---

## Playtest Steps

1. Visit Rustshore before Node Seven and confirm boat is blocked.
2. Complete Node Seven sequence.
3. Return to Rustshore.
4. Confirm dockmaster dialogue changed.
5. Choose to depart.
6. Confirm `Current_Journey = 2`.
7. Confirm transfer to Journey II placeholder or Coalmouth entry.

---

## Open Questions

- Should Elara farewell occur in Ashford or at Rustshore?
- Should departure include a save prompt?
- Should the next map be Coalmouth directly or a mainland landing screen?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Rustshore departure implementation packet |
