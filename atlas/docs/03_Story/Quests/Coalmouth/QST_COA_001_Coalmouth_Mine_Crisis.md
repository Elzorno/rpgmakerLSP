---
object_id: QST-COA-001
atlas_id: QST-COA-001
title: Coalmouth Mine Crisis
object_type: Quest
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
journey: JRN-002
relationships:
  starts_at:
    - LOC-COA-001
  involves:
    - CHR-KAI-001
    - CHR-VER-001
  requires:
    - QST-HOM-003
  rewards: []
---

# Coalmouth Mine Crisis

Coalmouth Mine Crisis is the first mainland regional quest and the introduction of Vera.

---

## Purpose

This quest shows that the world’s problems are connected to broken old systems and that each region misunderstands those systems through local culture.

---

## Story Role

After leaving Home Island, Kai arrives in Coalmouth and finds a town whose livelihood is failing because the mine machinery is behaving unpredictably.

Vera helps Kai understand that the problem is not a spirit’s anger, but a pattern of broken commands.

---

## Starting Conditions

Requires completion of Home Island core arc:

```text
J1_Node07_Offline = ON
J1_Mainland_TravelUnlocked = ON
```

---

## Objectives

1. Arrive in Coalmouth.
2. Learn that the mine is unsafe.
3. Meet Vera.
4. Gain access to the mine.
5. Investigate machinery behaving strangely.
6. Reach the relay/control chamber.
7. Defeat or disable the mine guardian.
8. Stabilize or isolate Node Six.
9. Return to town and confirm the mine is safer.

---

## Key NPCs

| ID | Name | Role |
|---|---|---|
| CHR-KAI-001 | Kai | Sword bearer |
| CHR-VER-001 | Vera | Practical machinery expert |

---

## Key Locations

| ID | Location | Role |
|---|---|---|
| LOC-COA-001 | Coalmouth | Quest start and town consequence |
| LOC-CMN-001 | Coalmouth Mine | Main dungeon |
| REL-006 | Relay Node Six | Hidden system objective |

---

## Completion Conditions

Draft completion state:

```text
QST_COA_001_Complete = ON
J2_Node06_Stabilized = ON
Current_Relay_Count = 2
Archive_Recovery_Percent = 10 or 12
```

---

## Dialogue Beats

- Miners describe the problem as spirits or curses.
- Vera describes it as a rhythm that changed.
- Kai recognizes archive behavior from Node Seven but still lacks vocabulary.
- Node Six response should echo Node Seven while using different wording.

---

## Switches

```text
J2_Coalmouth_Arrived
J2_Vera_Met
J2_Coalmouth_MineAccess
J2_Mine_ControlRoomReached
J2_Node06_GuardianDefeated
J2_Node06_Stabilized
QST_COA_001_Complete
```

---

## Variables

```text
Archive_Recovery_Percent
Current_Relay_Count
Current_Journey
```

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| requires | QST-HOM-003 | Home Island arc must be complete |
| starts_at | LOC-COA-001 | Quest starts in town |
| involves | CHR-VER-001 | Vera is central |
| advances_quest | LOC-CMN-001 | Mine dungeon objective |
| completes_quest | REL-006 | Node Six stabilized/isolated |

---

## RPG Maker Implementation Notes

Use evented machinery and simple switches. Do not create a complex simulation.

---

## Open Questions

- Is Node Six stabilized rather than offline?
- Does Vera join as guest or full actor during this quest?
- What exact archive percentage follows completion?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Coalmouth Mine Crisis quest object |
