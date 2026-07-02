---
object_id: SCR-HOM-RST-002
atlas_id: SCR-HOM-RST-002
title: Mainland Departure
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-RST-001
rpg_maker_map_name: CUT_Mainland_Departure
relationships:
  located_in:
    - LOC-RST-001
  implements:
    - IMP-HOM-013
  unlocks:
    - JRN-002
---

# SCR-HOM-RST-002 — Mainland Departure

## Purpose

Mainland Departure is the transition from Journey I to Journey II.

It should give Home Island emotional closure without becoming a long cutscene.

---

## Screen Type

This may be either:

- a small dock/boat cutscene map, or
- an event sequence on Rustshore Docks.

Use a separate screen object so the transition remains production-trackable.

---

## Required Beats

1. Player chooses to depart.
2. Dockmaster confirms route is safe enough.
3. Optional Elara farewell if not already handled in Ashford.
4. Boat leaves Home Island.
5. Short transition text or fade.
6. Journey II begins.

---

## Required State Change

On departure:

```text
Current_Journey = 2
```

Optional future state:

```text
J2_Coalmouth_Arrived = ON
```

Only set Coalmouth arrival if the next implemented map is Coalmouth.

---

## Required Events

| Event | Purpose |
|---|---|
| Departure Choice | Confirms player wants to leave |
| Boat Cutscene | Short transition |
| Journey Update | Sets Journey II state |
| Transfer | Moves player to mainland / Coalmouth entry |

---

## Switches Used

```text
J1_Mainland_TravelUnlocked
```

---

## Variables Used

```text
Current_Journey
```

---

## Audio

Use coastal theme, then short transition cue.

No extended cinematic music required in first pass.

---

## Acceptance Criteria

- Player cannot trigger departure before mainland travel is unlocked.
- Player receives a confirmation prompt before leaving.
- Departure sets `Current_Journey = 2`.
- Transfer destination is clearly marked for Journey II implementation.
- Sequence is short and replay-safe.

---

## Open Questions

- Should Elara appear at the dock for farewell?
- Should the player be warned that mainland content is not implemented in prototype builds?
- Should departure go directly to Coalmouth or to a small world map landing screen?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Mainland Departure screen object |
