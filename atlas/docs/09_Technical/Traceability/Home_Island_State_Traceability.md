---
atlas_id: ATLAS-TEC-044
title: Home Island State Traceability
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - IMP-HOM-002
  - ATLAS-TEC-042
related:
  - ATLAS-TEC-030
---

# Home Island State Traceability

This document traces Home Island switches and variables to the events and screens that use them.

---

## Purpose

This document answers:

> Which event sets or reads each Journey I switch or variable?

This helps Codex avoid duplicate state names and helps testers find broken progression logic.

---

## Switch Traceability

| State | Set By | Read By | Purpose |
|---|---|---|---|
| J1_Ashford_IntroComplete | EVT-HOM-002 or EVT-HOM-009 | Ashford NPC event pages | Tracks opening progression |
| J1_Tremor_Event | EVT-HOM-009 | Ashford NPCs, Skyreach access logic | Marks first story disruption |
| J1_Skyreach_AccessOpen | EVT-HOM-009 | TRN-HOM-005, EVT-HOM-010 | Opens northern route |
| J1_HiddenCave_Entered | EVT-HOM-011 | Hidden Cave dialogue/state checks | Tracks first cave entry |
| J1_Trial_Body_Clear | EVT-HOM-012 | EVT-HOM-015, EVT-HOM-016 | Body trial completion |
| J1_Trial_Mind_Clear | EVT-HOM-013 | EVT-HOM-015, EVT-HOM-016 | Mind trial completion |
| J1_Trial_Heart_Clear | EVT-HOM-014 | EVT-HOM-015, EVT-HOM-016 | Heart trial completion |
| J1_Sword_Obtained | EVT-HOM-016 | Glassfield seal, Ashford NPCs, future skill logic | Sword acquisition |
| SYS_ProtocolSkills_Unlocked | EVT-HOM-016 or later relay event | Battle/menu systems | Protocol skill availability |
| J1_Glassfield_SealOpened | EVT-HOM-017 | TRN-HOM-017 | Opens Sealed Node entrance |
| J1_SealedNode_Entered | EVT-HOM-019 | Sealed Node logic | Tracks dungeon entry |
| J1_CorePath_DoorOpened | EVT-HOM-020 | Core path door event | Optional simple door state |
| J1_Node07_GuardianDefeated | EVT-HOM-021 | TRN-HOM-023, EVT-HOM-022 | Allows relay core access |
| J1_Node07_Offline | EVT-HOM-022 | Ashford NPCs, Rustshore dockmaster | Node Seven resolution |
| J1_Mainland_TravelUnlocked | EVT-HOM-022 | EVT-HOM-023, EVT-HOM-025 | Enables mainland departure |
| NPC_Ashford_PostNode07 | EVT-HOM-022 | Ashford NPC event pages | Post-climax town dialogue |

---

## Variable Traceability

| Variable | Set By | Read By | Purpose |
|---|---|---|---|
| Current_Journey | EVT-HOM-026 | UI/debug/story checks | Tracks major story movement |
| Archive_Recovery_Percent | EVT-HOM-016, EVT-HOM-022 | Archive display, story checks | Tracks recovered archive state |
| Current_Relay_Count | EVT-HOM-022 | Relay progress checks | Tracks resolved relay count |

---

## Critical State Progression

```text
J1_Tremor_Event
→ J1_Skyreach_AccessOpen
→ J1_HiddenCave_Entered
→ J1_Trial_Body_Clear / J1_Trial_Mind_Clear / J1_Trial_Heart_Clear
→ J1_Sword_Obtained
→ J1_Glassfield_SealOpened
→ J1_SealedNode_Entered
→ J1_Node07_GuardianDefeated
→ J1_Node07_Offline
→ J1_Mainland_TravelUnlocked
→ Current_Journey = 2
```

---

## Validation Rules

- No new Journey I switch should be created without adding it here.
- A story gate must list both the event that sets it and the transfer/event that reads it.
- If a switch exists but has no reader, remove it or document future use.
- If a switch has multiple setters, document why.

---

## Open Questions

- Should `SYS_ProtocolSkills_Unlocked` be set at Sword acquisition or Node Seven resolution?
- Should `J1_Ashford_IntroComplete` be set by Elara dialogue or by the tremor event?
- Should `J1_CorePath_DoorOpened` remain canonical or be implementation-local?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island state traceability document |
