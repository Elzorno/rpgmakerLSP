---
object_id: QST-HOM-002
atlas_id: QST-HOM-002
title: The Sword Awakens
object_type: Quest
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
journey: JRN-001
relationships:
  starts_at:
    - LOC-ASH-001
  involves:
    - CHR-KAI-001
    - NPC-ELA-001
  requires:
    - QST-HOM-001
  rewards:
    - ITM-SWD-001
---

# The Sword Awakens

This quest sends Kai to Skyreach Hill and the Hidden Cave, where Project Excalibur authenticates him.

---

## Purpose

This quest transforms the game from village exploration into mythic adventure while preserving mystery.

---

## Story Role

After the tremor/signal event, Kai follows warnings and curiosity toward Skyreach Hill. In the Hidden Cave, he completes the trials and obtains the Sword.

---

## Objectives

1. Receive or infer that Skyreach Hill must be investigated.
2. Reach Skyreach Hill.
3. Enter the Hidden Cave.
4. Complete the trial chambers.
5. Approach the Sword pedestal.
6. Trigger authentication and archive recovery.
7. Return with the Sword.

---

## Completion Conditions

Quest completes when `J1_Sword_Obtained` is true and `Archive_Recovery_Percent` is set to 3.

---

## Rewards

| ID | Reward | Notes |
|---|---|---|
| ITM-SWD-001 | The Sword / Project Excalibur | Central artifact |

---

## Dialogue Beats

- Elara warns Kai not to treat the hill as a game.
- The cave feels like a sacred place, not a machine yet.
- The Sword does not fully explain itself.
- Archive text should be short and mysterious.

Suggested archive text:

```text
AUTHORIZATION ACCEPTED
ARCHIVE RECOVERY: 3%
```

---

## Switches

```text
J1_Skyreach_AccessOpen
J1_HiddenCave_Entered
J1_Trial_Body_Clear
J1_Trial_Mind_Clear
J1_Trial_Heart_Clear
J1_Sword_Obtained
```

---

## Variables

```text
Archive_Recovery_Percent = 3
```

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| requires | QST-HOM-001 | Opening must complete first |
| advances_quest | LOC-SKY-001 | Skyreach Hill path |
| advances_quest | LOC-HCV-001 | Hidden Cave trial site |
| rewards | ITM-SWD-001 | Sword obtained |
| unlocks | QST-HOM-003 | Opens path to Node Seven |

---

## RPG Maker Implementation Notes

Use map events for trials. Avoid complex plugins.

The Sword awakening can be handled with show text, screen tint, sound effect, animation, switch, and variable update.

---

## Playtest Checklist

- Player knows why to go to Skyreach Hill.
- Trials are understandable.
- Sword acquisition feels important.
- Archive text appears cleanly.
- Quest transitions into Glassfield / Sealed Node objective.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Sword Awakens quest object |
