---
object_id: IMP-HOM-003
atlas_id: IMP-HOM-003
title: Build Sword Awakening Sequence
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - QST-HOM-002
    - LOC-SKY-001
    - LOC-HCV-001
    - ITM-SWD-001
  requires:
    - IMP-HOM-002
---

# Implementation Packet: Build Sword Awakening Sequence

## Objective

Create the playable RPG Maker MZ sequence where Kai reaches Skyreach Hill, enters the Hidden Cave, completes the trials, and obtains the Sword / Project Excalibur.

---

## Atlas References

| ID | Reference |
|---|---|
| LOC-SKY-001 | Skyreach Hill |
| LOC-HCV-001 | Hidden Cave / Excalibur Vaultlet |
| ITM-SWD-001 | The Sword / Project Excalibur |
| QST-HOM-002 | The Sword Awakens |
| IMP-HOM-002 | Journey I State System |

---

## Scope

Included:

- Skyreach Hill access gate.
- Hidden Cave entrance.
- Three simple trial rooms or placeholder trial events.
- Sword pedestal event.
- Archive recovery text.
- Sword key item / weapon acquisition.
- State updates.

Out of scope:

- Final cutscene art.
- Final dungeon tileset polish.
- Final music.
- Advanced puzzle mechanics.

---

## Required Maps

```text
DGN_SkyreachHill_Path
DGN_HiddenCave_Entrance
DGN_HiddenCave_TrialBody
DGN_HiddenCave_TrialMind
DGN_HiddenCave_TrialHeart
DGN_HiddenCave_Sanctum
```

If map count needs to be smaller for first implementation, combine the trial rooms into one map with separated sections.

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
Archive_Recovery_Percent = 3 after Sword awakening
```

---

## Event Logic

### Skyreach Access

Before `J1_Skyreach_AccessOpen`, block the path with NPC warning, terrain, or narrative event.

After the switch is on, allow entry.

### Trial Events

Use simple evented trials:

1. Body trial: small combat or movement challenge.
2. Mind trial: simple observation/pattern interaction.
3. Heart trial: short choice or memory-like moment.

Each trial sets its corresponding switch.

### Sword Pedestal

Requirements:

- All three trial switches ON.
- Player interacts with pedestal.
- Screen fade or flash.
- Sound effect.
- Text:

```text
AUTHORIZATION ACCEPTED
ARCHIVE RECOVERY: 3%
```

Then:

```text
J1_Sword_Obtained = ON
Archive_Recovery_Percent = 3
```

Add Sword as key item and/or weapon depending on implementation decision.

---

## Acceptance Criteria

- Player can access Skyreach only after correct story state.
- Player can enter Hidden Cave.
- All three trials can be completed.
- Sword pedestal does nothing or gives clue before trials are complete.
- Sword acquisition sets required switches and variable.
- Player can leave the cave after acquisition.

---

## Playtest Steps

1. Set `J1_Skyreach_AccessOpen` ON.
2. Enter Skyreach Hill.
3. Enter Hidden Cave.
4. Complete all trials.
5. Interact with Sword pedestal.
6. Confirm item acquisition.
7. Confirm `J1_Sword_Obtained` ON.
8. Confirm `Archive_Recovery_Percent` = 3.

---

## Open Questions

- Should the body trial use a real enemy or event-only obstacle?
- Should Protocol Skills unlock immediately here or after Node Seven?
- Should the Sword be both weapon and key item?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Sword awakening implementation packet |
