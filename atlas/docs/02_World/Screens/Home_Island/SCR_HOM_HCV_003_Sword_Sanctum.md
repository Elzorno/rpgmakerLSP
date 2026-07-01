---
object_id: SCR-HOM-HCV-003
atlas_id: SCR-HOM-HCV-003
title: Sword Sanctum
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-HCV-001
rpg_maker_map_name: DGN_HiddenCave_Sanctum
relationships:
  located_in:
    - LOC-HCV-001
  contains:
    - ITM-SWD-001
  implements:
    - IMP-HOM-003
---

# SCR-HOM-HCV-003 — Sword Sanctum

## Purpose

Sword Sanctum is the first major transformation screen of the game.

Kai obtains the Sword / Project Excalibur here.

---

## Map Intent

A small sacred inner chamber focused entirely on the Sword pedestal.

Recommended approximate size:

```text
23 x 19 tiles
```

---

## Required Visual Elements

- Central Sword pedestal.
- Symmetrical chamber layout.
- Geometric floor markings.
- Dim blue-white light.
- Stone/glass panels that can later read as old-world interface surfaces.
- Clear exit back to trial chamber.

---

## Required Events

| Event | Purpose |
|---|---|
| Sword Pedestal | Main acquisition/authentication event |
| Archive Text | Displays first archive recovery message |
| Transfer Back | Returns to SCR-HOM-HCV-002 |

---

## Sword Pedestal Requirements

Before all trial switches are ON, pedestal should give a clue and not award the Sword.

After all trial switches are ON:

```text
J1_Sword_Obtained = ON
Archive_Recovery_Percent = 3
```

Suggested text:

```text
AUTHORIZATION ACCEPTED
ARCHIVE RECOVERY: 3%
```

---

## Switches Used

```text
J1_Trial_Body_Clear
J1_Trial_Mind_Clear
J1_Trial_Heart_Clear
J1_Sword_Obtained
SYS_ProtocolSkills_Unlocked
```

---

## Variables Used

```text
Archive_Recovery_Percent
```

---

## Audio

Reduce or stop music before the pedestal interaction.

Use Sword authentication sound cue during acquisition.

---

## Encounters

None.

---

## Acceptance Criteria

- Pedestal checks all three trial switches.
- Sword is awarded once.
- Archive recovery becomes 3.
- Event cannot be repeated for duplicate reward.
- Player can leave after acquisition.
- Moment feels sacred and mysterious rather than fully explained.

---

## Open Questions

- Should `SYS_ProtocolSkills_Unlocked` turn ON here or after Node Seven?
- Should the Sword be added as weapon, key item, or both?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Sword Sanctum screen object |
