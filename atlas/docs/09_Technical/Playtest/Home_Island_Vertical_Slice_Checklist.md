---
atlas_id: ATLAS-TEC-030
title: Home Island Vertical Slice Playtest Checklist
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
dependencies:
  - IMP-HOM-009
related:
  - REG-HOM-001
  - JRN-001
---

# Home Island Vertical Slice Playtest Checklist

This checklist defines the first full playtest path for the Home Island vertical slice.

---

## Purpose

This checklist verifies that the first playable Journey I build works from start to finish without manual intervention.

---

## Setup

Start a new game.

Do not manually toggle switches or variables unless testing a specific failure state.

---

## Expected Initial State

| State | Expected Value |
|---|---|
| Current_Journey | 1 |
| Archive_Recovery_Percent | 0 |
| Current_Relay_Count | 0 |
| J1_Sword_Obtained | OFF |
| J1_Node07_Offline | OFF |
| J1_Mainland_TravelUnlocked | OFF |

---

## Playtest Path

### 1. Ashford Start

- [ ] Player starts in correct location.
- [ ] Elara is present and interactable.
- [ ] At least six Ashford NPCs are interactable.
- [ ] Player can enter and exit required interiors.
- [ ] Hidden item behind warm-stone vent can be found once.

### 2. Tremor Event

- [ ] Player can trigger the opening progression event.
- [ ] `J1_Tremor_Event` turns ON.
- [ ] `J1_Skyreach_AccessOpen` turns ON.
- [ ] Ashford dialogue changes after tremor.

### 3. Skyreach Hill

- [ ] Skyreach path is blocked before access switch.
- [ ] Skyreach path opens after access switch.
- [ ] Player can reach Hidden Cave entrance.

### 4. Hidden Cave / Sword

- [ ] Player can enter Hidden Cave.
- [ ] `J1_HiddenCave_Entered` turns ON.
- [ ] Body trial can be completed.
- [ ] Mind trial can be completed.
- [ ] Heart trial can be completed.
- [ ] Sword pedestal requires completed trials.
- [ ] Sword acquisition turns `J1_Sword_Obtained` ON.
- [ ] `Archive_Recovery_Percent` becomes 3.

### 5. Glassfield Ruins

- [ ] Glassfield seal blocks progress before Sword.
- [ ] Glassfield seal opens after Sword.
- [ ] `J1_Glassfield_SealOpened` turns ON.
- [ ] Player can enter Sealed Node.

### 6. Sealed Node

- [ ] `J1_SealedNode_Entered` turns ON.
- [ ] Player can reach guardian encounter.
- [ ] Guardian battle starts correctly.
- [ ] Guardian defeat turns `J1_Node07_GuardianDefeated` ON.
- [ ] Player can access relay core after guardian defeat.

### 7. Node Seven Shutdown

- [ ] Relay core event triggers after guardian defeat.
- [ ] `J1_Node07_Offline` turns ON.
- [ ] `Archive_Recovery_Percent` becomes 5.
- [ ] `Current_Relay_Count` becomes 1.
- [ ] `J1_Mainland_TravelUnlocked` turns ON.
- [ ] `NPC_Ashford_PostNode07` turns ON.

### 8. Post-Node Ashford

- [ ] Ashford NPCs reflect post-node state.
- [ ] Elara has post-node dialogue.
- [ ] Rustshore/mainland travel state is available for next sprint.

---

## Failure Checks

- [ ] Player cannot softlock before Sword acquisition.
- [ ] Player cannot enter Sealed Node without Sword.
- [ ] Player cannot shut down Node Seven before guardian defeat.
- [ ] Hidden item cannot be collected repeatedly.
- [ ] Missing placeholder assets do not crash the game.

---

## Review Outcome

| Result | Meaning |
|---|---|
| Pass | Slice is playable from start to Node Seven shutdown |
| Pass With Issues | Playable, but polish or minor bugs remain |
| Fail | Progression blocked or major state logic broken |

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island vertical slice checklist |
