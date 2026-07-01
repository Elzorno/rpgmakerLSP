---
object_id: IMP-COA-002
atlas_id: IMP-COA-002
title: Build Coalmouth State System
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - QST-COA-001
    - REL-006
  requires:
    - IMP-HOM-009
    - ATLAS-TEC-020
---

# Implementation Packet: Build Coalmouth State System

## Objective

Create the RPG Maker MZ switches and variables needed to support the Coalmouth Mine Crisis and Relay Node Six.

---

## Atlas References

| ID | Reference |
|---|---|
| QST-COA-001 | Coalmouth Mine Crisis |
| REL-006 | Relay Node Six |
| CHR-VER-001 | Vera |
| JRN-002 | Journey II — The Forgotten World |

---

## Required Switches

```text
J2_Coalmouth_Arrived
J2_Vera_Met
J2_Vera_Joined
J2_Coalmouth_MineAccess
J2_Mine_Entered
J2_Mine_RailSwitchSolved
J2_Mine_ControlRoomReached
J2_Node06_GuardianDefeated
J2_Node06_Stabilized
QST_COA_001_Complete
NPC_Coalmouth_PostNode06
```

---

## Required Variables

```text
Current_Journey
Archive_Recovery_Percent
Current_Relay_Count
```

Suggested values:

```text
Current_Journey = 2 after mainland arrival
Archive_Recovery_Percent = 10 after Node Six stabilization
Current_Relay_Count = 2 after Node Six stabilization
```

---

## State Transition Table

| Event | Switch / Variable Change |
|---|---|
| Arrive in Coalmouth | J2_Coalmouth_Arrived = ON; Current_Journey = 2 |
| Meet Vera | J2_Vera_Met = ON |
| Vera joins/investigates | J2_Vera_Joined = ON |
| Mine access granted | J2_Coalmouth_MineAccess = ON |
| Enter mine | J2_Mine_Entered = ON |
| Solve rail switch | J2_Mine_RailSwitchSolved = ON |
| Reach control room | J2_Mine_ControlRoomReached = ON |
| Defeat Iron Foreman | J2_Node06_GuardianDefeated = ON |
| Stabilize Node Six | J2_Node06_Stabilized = ON; Archive_Recovery_Percent = 10; Current_Relay_Count = 2 |
| Return to town | QST_COA_001_Complete = ON; NPC_Coalmouth_PostNode06 = ON |

---

## Common Event Candidates

```text
CE_RelayNode_Stabilize
CE_MineMachine_Pulse
CE_Vera_ToolPrompt
CE_Archive_MessageDisplay
```

---

## Acceptance Criteria

- Coalmouth state names are canonical and reusable.
- Quest and NPC packets can reference the same switches.
- Node Six can differ from Node Seven by using STABILIZED/ISOLATED instead of OFFLINE.
- Future Codex work does not invent duplicate Coalmouth state names.

---

## Open Questions

- Should the final state be `J2_Node06_Stabilized` or `J2_Node06_Isolated`?
- Should Vera joining be guest-only or full party state?
- Should `Archive_Recovery_Percent` become 10 or 12?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Coalmouth state system packet |
