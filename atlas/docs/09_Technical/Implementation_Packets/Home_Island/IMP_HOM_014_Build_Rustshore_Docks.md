---
object_id: IMP-HOM-014
atlas_id: IMP-HOM-014
title: Build Rustshore Docks
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - LOC-RST-001
    - SCR-HOM-RST-001
  requires:
    - IMP-HOM-002
    - IMP-HOM-013
    - ATLAS-TEC-043
    - ATLAS-TEC-052
    - ATLAS-TEC-055
---

# Implementation Packet: Build Rustshore Docks

## Objective

Create the implementation-facing production packet for Rustshore Docks as the Home Island harbor screen and mainland travel gate.

This packet focuses on the dock screen itself. The separate mainland departure transition remains covered by `IMP-HOM-013`.

---

## Traceability

| Source | Role |
|---|---|
| LOC-RST-001 | Location object for Rustshore Docks |
| SCR-HOM-RST-001 | Screen object for the dock map |
| IMP-HOM-013 | Existing packet for mainland departure transition |
| ATLAS-TEC-031 | Identifies Rustshore Docks as a known packet gap |
| ATLAS-TEC-043 | Defines Home Island screen flow and mainland departure gate |
| ATLAS-TEC-052 | Confirms story, gameplay, hidden truth, and implementation layer alignment |
| ATLAS-TEC-055 | Defines executable Rustshore event pages |

---

## Screens To Build

| Screen ID | Map Name | Purpose |
|---|---|---|
| SCR-HOM-RST-001 | TWN_Rustshore_Docks | Dock screen, lighthouse detail, boat gate, and route back to Home Island |

---

## Build Order

1. Create or confirm `TWN_Rustshore_Docks`.
2. Add return transfer to the Home Island route / Ashford route.
3. Add dockmaster event with locked and unlocked travel states.
4. Add boat transfer event gated by `J1_Mainland_TravelUnlocked`.
5. Add lighthouse examine event as a subtle old-world signal clue.
6. Connect available departure flow to `SCR-HOM-RST-002` when the unlock switch is ON.

---

## Required Transfers

| From | To | Condition |
|---|---|---|
| Home Island route / Ashford route | SCR-HOM-RST-001 | Available when the player can reach Rustshore |
| SCR-HOM-RST-001 | Home Island route / Ashford route | Always available |
| SCR-HOM-RST-001 | SCR-HOM-RST-002 | Requires `J1_Mainland_TravelUnlocked` |

---

## Required Events

| Event | Purpose |
|---|---|
| Dockmaster | Explains why travel is blocked or available |
| Boat Transfer | Sends player to mainland departure transition after unlock |
| Lighthouse Examine | Shows subtle old-world signal behavior without technical exposition |
| Transfer Back | Returns player to the island route |

---

## Required Story Logic

- Before Node Seven resolution, boat travel is unavailable.
- After Node Seven resolution, mainland travel becomes available.
- Dockmaster state should reflect `J1_Mainland_TravelUnlocked`.
- The lighthouse should support the Truth Layer Diagram's rule that fantasy-facing details can quietly point to hidden infrastructure.

---

## Required Switches

```text
J1_Node07_Offline
J1_Mainland_TravelUnlocked
```

---

## Implementation Notes

- Do not require a custom plugin.
- Keep the harbor readable as a normal coastal location first.
- Use `SCR-HOM-RST-001` acceptance criteria as the production authority for required visual elements.
- Keep the hidden cybersecurity layer subtle: the lighthouse can imply old signal behavior, but it should not explain relay architecture directly.
- If `SCR-HOM-RST-002` is not implemented yet, mark the transfer destination clearly as a placeholder rather than inventing a Journey II map.

---

## Acceptance Criteria

- Player can enter and leave Rustshore Docks.
- Dockmaster blocks travel before `J1_Mainland_TravelUnlocked`.
- Boat transfer is unavailable before unlock and available after unlock.
- Lighthouse examine event exists and reinforces hidden technology subtly.
- The screen has no random encounters.
- Transfer to `SCR-HOM-RST-002` is clearly wired or marked as a placeholder.

---

## Playtest Steps

1. Enter Rustshore Docks before Node Seven resolution.
2. Confirm dockmaster blocks mainland departure.
3. Confirm return transfer works.
4. Examine the lighthouse.
5. Turn `J1_Mainland_TravelUnlocked` ON through the Node Seven sequence or debug.
6. Return to the dockmaster and confirm travel is available.
7. Trigger boat transfer and confirm it targets `SCR-HOM-RST-002` or a clearly marked placeholder.

---

## Open Questions

- Should the dockmaster become a formal NPC object in a later Atlas pass?
- Should lighthouse behavior visibly change after Node Seven, or remain flavor only?
- Should Journey II start at Coalmouth directly or a mainland landing screen?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Rustshore Docks implementation packet |
