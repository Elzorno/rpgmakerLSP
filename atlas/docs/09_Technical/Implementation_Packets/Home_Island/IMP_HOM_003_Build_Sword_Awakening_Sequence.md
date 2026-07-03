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
    - ATLAS-TEC-057
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
| ATLAS-TEC-057 | Home Island Body Mind Heart Trial Mechanics Spec |

---

## Scope

Included:

- Skyreach Hill access gate.
- Hidden Cave entrance.
- Three simple trial rooms or evented trial sections using `ATLAS-TEC-057`.
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
Trial_Body_Attempts
Trial_Mind_SequenceStep
Trial_Heart_IntentChoice
```

---

## Event Logic

### Skyreach Access

Before `J1_Skyreach_AccessOpen`, block the path with NPC warning, terrain, or narrative event.

After the switch is on, allow entry.

### Trial Events

Use the executable evented trials from `ATLAS-TEC-057`:

1. Body trial: movement lane with harmless reset tiles.
2. Mind trial: left, right, center marker sequence.
3. Heart trial: abstract intent choice prompt.

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
- Trial mechanics follow `ATLAS-TEC-057`.
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

## Resolved Questions

| Question | Resolution |
|---|---|
| Should the body trial use a real enemy or event-only obstacle? | Use the event-only movement/reset Body Trial from `ATLAS-TEC-057`. |
| Should Protocol Skills unlock immediately here or after Node Seven? | Still governed by the Sword pedestal/event implementation decision in `ATLAS-TEC-055`; not changed by trial mechanics. |
| Should the Sword be both weapon and key item? | Use the combat database/Truth Layer guidance from `ATLAS-TEC-056` and `ATLAS-TEC-052`; not changed by trial mechanics. |

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Sword awakening implementation packet |
| 0.2 | Linked executable Body, Mind, and Heart trial mechanics from ATLAS-TEC-057 |
