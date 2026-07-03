---
object_id: IMP-HOM-011
atlas_id: IMP-HOM-011
title: Build Skyreach and Hidden Cave Screens
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - SCR-HOM-SKY-001
    - SCR-HOM-HCV-001
    - SCR-HOM-HCV-002
    - SCR-HOM-HCV-003
  requires:
    - IMP-HOM-002
    - IMP-HOM-003
    - IMP-HOM-010
    - ATLAS-TEC-055
---

# Implementation Packet: Build Skyreach and Hidden Cave Screens

## Objective

Convert the Sword awakening route into screen-level RPG Maker MZ production tasks.

This packet builds the path from Ashford's northern route through Skyreach Hill, Hidden Cave, the three trials, and the Sword Sanctum.

---

## Screens To Build

| Screen ID | Map Name | Purpose |
|---|---|---|
| SCR-HOM-SKY-001 | DGN_SkyreachHill_Path | Forbidden hill route |
| SCR-HOM-HCV-001 | DGN_HiddenCave_Entrance | Cave entry and first switch |
| SCR-HOM-HCV-002 | DGN_HiddenCave_Trials | Three trial chambers |
| SCR-HOM-HCV-003 | DGN_HiddenCave_Sanctum | Sword pedestal / authentication |

---

## Build Order

1. SCR-HOM-SKY-001 — Skyreach Hill Path
2. SCR-HOM-HCV-001 — Hidden Cave Entrance
3. SCR-HOM-HCV-002 — Hidden Cave Trials
4. SCR-HOM-HCV-003 — Sword Sanctum

---

## Required Transfers

| From | To |
|---|---|
| SCR-HOM-ASH-001 | SCR-HOM-SKY-001 |
| SCR-HOM-SKY-001 | SCR-HOM-ASH-001 or island route |
| SCR-HOM-SKY-001 | SCR-HOM-HCV-001 |
| SCR-HOM-HCV-001 | SCR-HOM-SKY-001 |
| SCR-HOM-HCV-001 | SCR-HOM-HCV-002 |
| SCR-HOM-HCV-002 | SCR-HOM-HCV-001 |
| SCR-HOM-HCV-002 | SCR-HOM-HCV-003 |
| SCR-HOM-HCV-003 | SCR-HOM-HCV-002 |

---

## Required Story Logic

- Skyreach access gated by `J1_Skyreach_AccessOpen`.
- Hidden Cave entry sets `J1_HiddenCave_Entered`.
- Three trials set their individual switches.
- Sword pedestal requires all three trial switches.
- Sword event sets `J1_Sword_Obtained` and `Archive_Recovery_Percent = 3`.
- Event pages follow `ATLAS-TEC-055`.

---

## Required Switches

```text
J1_Skyreach_AccessOpen
J1_HiddenCave_Entered
J1_Trial_Body_Clear
J1_Trial_Mind_Clear
J1_Trial_Heart_Clear
J1_Sword_Obtained
SYS_ProtocolSkills_Unlocked
```

---

## Required Variables

```text
Archive_Recovery_Percent
```

---

## Acceptance Criteria

- Player can reach Skyreach after the access switch turns ON.
- Player can enter Hidden Cave.
- All three trials can be completed.
- Sword pedestal is gated correctly.
- Sword can only be obtained once.
- Archive recovery updates to 3.
- Player can leave the cave after Sword acquisition.
- No custom plugins required.

---

## Playtest Steps

1. Start from Ashford with `J1_Skyreach_AccessOpen` OFF and confirm route is blocked.
2. Turn `J1_Skyreach_AccessOpen` ON through story event or debug.
3. Enter Skyreach Hill.
4. Enter Hidden Cave.
5. Complete Body, Mind, and Heart trials.
6. Enter Sword Sanctum.
7. Interact with pedestal.
8. Confirm Sword acquisition and archive recovery update.
9. Return to Ashford route.

---

## Open Questions

- Should the Body Trial use the first actual combat encounter outside random battles?
- Should Heart Trial reference Elara visually or only through text?
- Should Protocol Skills unlock now or at Node Seven?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Skyreach and Hidden Cave screen implementation packet |
