---
object_id: IMP-HOM-010
atlas_id: IMP-HOM-010
title: Build Ashford Screens
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - SCR-HOM-ASH-001
    - SCR-HOM-ASH-002
    - SCR-HOM-ASH-003
  requires:
    - IMP-HOM-001
    - IMP-HOM-002
    - IMP-HOM-006
---

# Implementation Packet: Build Ashford Screens

## Objective

Convert the Ashford location object into screen-level RPG Maker MZ production tasks.

This packet supersedes vague “build Ashford” work with exact screen targets.

---

## Screens To Build

| Screen ID | Map Name | Purpose |
|---|---|---|
| SCR-HOM-ASH-001 | TWN_Ashford_Exterior | Main village exterior |
| SCR-HOM-ASH-002 | INT_Ashford_ElaraHouse | Starting interior / Elara dialogue |
| SCR-HOM-ASH-003 | INT_Ashford_Shop | Basic shop and preparation |

---

## Build Order

1. SCR-HOM-ASH-002 — Elara House Interior
2. SCR-HOM-ASH-001 — Ashford Exterior
3. SCR-HOM-ASH-003 — Ashford Shop Interior

Starting inside Elara House gives the opening sequence the strongest emotional anchor.

---

## Required Transfers

| From | To |
|---|---|
| SCR-HOM-ASH-002 | SCR-HOM-ASH-001 |
| SCR-HOM-ASH-001 | SCR-HOM-ASH-002 |
| SCR-HOM-ASH-001 | SCR-HOM-ASH-003 |
| SCR-HOM-ASH-003 | SCR-HOM-ASH-001 |

---

## Required Systems

- Story-state dialogue pages.
- Hidden item self-switch.
- North route gate for Skyreach access.
- Shop processing placeholder.
- Audio placeholders.

---

## Acceptance Criteria

- New game can start in Elara House.
- Player can exit to Ashford Exterior.
- Player can enter and exit Ashford Shop.
- Required NPC placeholders exist on Ashford Exterior.
- Elara has event pages prepared for story states.
- Hidden item works once.
- No transfer loops trap the player.

---

## Playtest Steps

1. Start new game in SCR-HOM-ASH-002.
2. Talk to Elara.
3. Exit to SCR-HOM-ASH-001.
4. Speak to all exterior NPC placeholders.
5. Find hidden item.
6. Enter SCR-HOM-ASH-003.
7. Use or test shopkeeper placeholder.
8. Return to exterior.
9. Confirm north route can be gated.

---

## Open Questions

- Should Elder House be screen 004 now or later?
- Should Ashford Inn exist, or should Elara House remain the only early rest point?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Ashford screen implementation packet |
