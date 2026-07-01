---
object_id: IMP-COA-003
atlas_id: IMP-COA-003
title: Build Coalmouth NPC Dialogue
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - ATLAS-STY-020
    - ATLAS-CHR-020
  requires:
    - IMP-COA-002
---

# Implementation Packet: Build Coalmouth NPC Dialogue

## Objective

Implement first-pass Coalmouth NPC dialogue scaffolding in RPG Maker MZ.

---

## Atlas References

| ID | Reference |
|---|---|
| ATLAS-STY-020 | Coalmouth Dialogue Packet |
| ATLAS-CHR-020 | Coalmouth NPC Roster |
| CHR-VER-001 | Vera |
| QST-COA-001 | Coalmouth Mine Crisis |

---

## Scope

Included:

- Vera event pages.
- Placeholder NPC dialogue for Coalmouth town roles.
- State-aware dialogue before and after Node Six.
- Event comments referencing Atlas source documents.

Out of scope:

- Final polished dialogue.
- Portraits/faces.
- Optional side quests.

---

## Required NPC Events

| Event | Required States |
|---|---|
| Vera | Arrival, Mine Lockdown, Investigating, After Node Six |
| Foreman | Arrival, Mine Lockdown, After Node Six |
| Worried Miner | Arrival, After Node Six |
| Injured Worker | Mine Lockdown |
| Old Railkeeper | Arrival, Investigating |
| Rhythm Child | Arrival, Mine Lockdown |
| Shopkeeper | Arrival, After Node Six |

---

## Required Switches

```text
J2_Coalmouth_Arrived
J2_Vera_Met
J2_Vera_Joined
J2_Coalmouth_MineAccess
J2_Node06_Stabilized
NPC_Coalmouth_PostNode06
```

---

## Dialogue Implementation Rule

Use sample lines from `ATLAS-STY-020` as placeholders.

Do not use terms like ICS, SCADA, authentication, or relay in ordinary Coalmouth NPC dialogue.

Vera may describe real technical logic through plain language.

---

## Acceptance Criteria

- Vera has state-aware dialogue.
- Coalmouth NPCs reinforce mine crisis.
- NPCs change after Node Six stabilization.
- Dialogue remains respectful toward workers and their beliefs.
- No dialogue reveals NEMESIS or full old-world truth early.

---

## Playtest Steps

1. Enter Coalmouth and talk to all NPCs.
2. Toggle `J2_Vera_Met` and retest Vera.
3. Toggle `J2_Coalmouth_MineAccess` and retest Foreman/Vera.
4. Toggle `J2_Node06_Stabilized` and retest town dialogue.
5. Confirm no NPC event blocks progress.

---

## Open Questions

- Should Vera require an introductory cutscene?
- Should the foreman be named before implementation?
- Should the injured worker later provide a side quest?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Coalmouth NPC dialogue implementation packet |
