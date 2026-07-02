---
object_id: IMP-HOM-002
atlas_id: IMP-HOM-002
title: Build Journey I State System
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - JRN-001
    - QST-HOM-001
    - QST-HOM-002
    - QST-HOM-003
  requires:
    - ATLAS-TEC-020
    - ATLAS-GME-001
---

# Implementation Packet: Build Journey I State System

## Objective

Create the RPG Maker MZ switches and variables needed to support Journey I from Ashford opening through Node Seven shutdown.

This packet does not build all maps. It defines the state backbone that later map/event packets should use.

---

## Atlas References

| ID | Reference |
|---|---|
| JRN-001 | Journey I — The Dreamer |
| QST-HOM-001 | Home Island Opening |
| QST-HOM-002 | The Sword Awakens |
| QST-HOM-003 | Node Seven Offline |
| ITM-SWD-001 | The Sword / Project Excalibur |
| REL-007 | Relay Node Seven |
| ATLAS-TEC-020 | RPG Maker MZ Bible |

---

## Scope

Included:

- Journey I switch list.
- Journey I variable list.
- Naming standard.
- Expected state transitions.
- Acceptance criteria for future event implementation.

Out of scope:

- Map design.
- Final cutscenes.
- Enemy database work.
- Final dialogue.

---

## Required Switches

```text
J1_Ashford_IntroComplete
J1_Tremor_Event
J1_Skyreach_AccessOpen
J1_HiddenCave_Entered
J1_Trial_Body_Clear
J1_Trial_Mind_Clear
J1_Trial_Heart_Clear
J1_Sword_Obtained
J1_Glassfield_SealOpened
J1_SealedNode_Entered
J1_Node07_GuardianDefeated
J1_Node07_Offline
J1_Mainland_TravelUnlocked
NPC_Ashford_PostNode07
SYS_ProtocolSkills_Unlocked
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
Current_Journey = 1
Archive_Recovery_Percent = 0 at game start
Archive_Recovery_Percent = 3 after Sword awakening
Archive_Recovery_Percent = 5 after Node Seven shutdown
Current_Relay_Count = 1 after Node Seven shutdown
```

---

## State Transition Table

| Event | Switch / Variable Change |
|---|---|
| Ashford intro complete | J1_Ashford_IntroComplete = ON |
| Tremor event | J1_Tremor_Event = ON; J1_Skyreach_AccessOpen = ON |
| Enter Hidden Cave | J1_HiddenCave_Entered = ON |
| Complete body trial | J1_Trial_Body_Clear = ON |
| Complete mind trial | J1_Trial_Mind_Clear = ON |
| Complete heart trial | J1_Trial_Heart_Clear = ON |
| Obtain Sword | J1_Sword_Obtained = ON; Archive_Recovery_Percent = 3 |
| Open Glassfield seal | J1_Glassfield_SealOpened = ON |
| Enter Sealed Node | J1_SealedNode_Entered = ON |
| Defeat Node guardian | J1_Node07_GuardianDefeated = ON |
| Shut down Node Seven | J1_Node07_Offline = ON; Archive_Recovery_Percent = 5; Current_Relay_Count = 1 |
| Unlock mainland travel | J1_Mainland_TravelUnlocked = ON; NPC_Ashford_PostNode07 = ON |

---

## Common Event Candidates

```text
CE_Archive_MessageDisplay
CE_Sword_Authentication
CE_RelayNode_Shutdown
CE_Update_Journey_State
```

These do not need to be fully implemented in this packet, but reserve their names for later.

---

## Acceptance Criteria

- All Journey I switches exist with clear names.
- All Journey I variables exist with clear names.
- No vague switch names are used.
- Later implementation packets can reference these states without inventing new names.
- Codex can map these names to RPG Maker data IDs in a future implementation pass.

---

## Playtest Steps

This packet is primarily data/state setup.

Future playtest should confirm:

1. Switch names exist.
2. Variables exist.
3. Events can reference the same names consistently.
4. No duplicate state names are created.

---

## Out of Scope

Do not implement full story sequence here. This packet only establishes the canonical state model.

---

## Open Questions

- Should `Archive_Recovery_Percent` display to the player every time it changes?
- Should `Current_Journey` be visible only to implementation or used in-game?
- Should `SYS_ProtocolSkills_Unlocked` turn on immediately with Sword acquisition or after the first relay shutdown?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Journey I state system implementation packet |
