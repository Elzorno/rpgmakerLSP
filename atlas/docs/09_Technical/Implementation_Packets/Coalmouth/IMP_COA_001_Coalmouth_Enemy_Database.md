---
object_id: IMP-COA-001
atlas_id: IMP-COA-001
title: Build Coalmouth Enemy Database
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - MON-GEL-003
    - MON-GLM-001
    - MON-SCP-001
    - BOS-N06-001
  requires:
    - ATLAS-MON-001
    - ATLAS-TEC-020
---

# Implementation Packet: Build Coalmouth Enemy Database

## Objective

Create the first RPG Maker MZ enemy database entries and troop recommendations for Coalmouth Region.

---

## Atlas References

| ID | Reference |
|---|---|
| MON-GEL-003 | Soot Gel |
| MON-GLM-001 | Coal Golem |
| MON-SCP-001 | Mine Scorpion |
| BOS-N06-001 | Iron Foreman |
| LOC-CMN-001 | Coalmouth Mine |

---

## Scope

Included:

- three common enemy entries,
- one boss entry,
- troop recommendations,
- first-pass skill list,
- encounter placement guidance.

Out of scope:

- final balance,
- final battler art,
- final animations,
- final drop tuning.

---

## Enemy Entries

| Suggested Enemy ID | Object ID | Name | Role |
|---|---|---|---|
| 11 | MON-GEL-003 | Soot Gel | Basic mine enemy |
| 12 | MON-SCP-001 | Mine Scorpion | Status-pressure enemy |
| 13 | MON-GLM-001 | Coal Golem | Slow defensive construct |
| 20 | BOS-N06-001 | Iron Foreman | Coalmouth boss |

---

## Troop Recommendations

| Suggested Troop | Composition | Use |
|---|---|---|
| Coalmouth Mine 1 | 1 Soot Gel | Basic intro encounter |
| Coalmouth Mine 2 | 2 Soot Gels | Group fight |
| Coalmouth Mine 3 | 1 Mine Scorpion | Status tutorial |
| Coalmouth Mine 4 | 1 Soot Gel + 1 Mine Scorpion | Mixed threat |
| Coalmouth Mine 5 | 1 Coal Golem | Heavy enemy tutorial |
| Coalmouth Boss | 1 Iron Foreman | Node Six climax |

---

## Skill Requirements

```text
Soot Gel: Attack, Soot Puff
Mine Scorpion: Sting, Pinch, Venom Prick
Coal Golem: Heavy Strike, Brace, Coal Toss
Iron Foreman: Overtime Order, Piston Slam, Warning Bell, Shift Collapse
```

---

## Balance Philosophy

Coalmouth enemies should be a clear step above Home Island but still readable.

The player should learn that mainland encounters require more resource management and attention to enemy roles.

---

## Required Assets

| Object ID | Asset Need |
|---|---|
| MON-GEL-003 | Battler image |
| MON-SCP-001 | Battler image |
| MON-GLM-001 | Battler image |
| BOS-N06-001 | Boss battler image |

---

## Acceptance Criteria

- Coalmouth enemies exist in RPG Maker database.
- Troops exist for test battles.
- Iron Foreman can be used in QST-COA-001 boss event.
- Enemy roles are distinct and readable.

---

## Open Questions

- Should Mine Scorpion poison be active in the first implementation?
- Should Coal Golem have a tool weakness tied to Vera?
- Should Iron Foreman summon common enemies or stay solo?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Coalmouth enemy database packet |
