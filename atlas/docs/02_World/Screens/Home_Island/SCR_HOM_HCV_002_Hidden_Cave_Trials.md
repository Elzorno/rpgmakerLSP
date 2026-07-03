---
object_id: SCR-HOM-HCV-002
atlas_id: SCR-HOM-HCV-002
title: Hidden Cave Trials
object_type: Screen
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-HCV-001
rpg_maker_map_name: DGN_HiddenCave_Trials
relationships:
  located_in:
    - LOC-HCV-001
  implements:
    - IMP-HOM-003
  requires:
    - ATLAS-TEC-057
---

# SCR-HOM-HCV-002 — Hidden Cave Trials

## Purpose

Hidden Cave Trials is the first structured challenge space tied to the Sword.

The trials should feel like ritual tests while quietly functioning as degraded identity and readiness checks.

---

## Map Intent

One map divided into three small trial sections for the first implementation.

Recommended approximate size:

```text
40 x 32 tiles
```

---

## Trial Sections

| Trial | Fantasy Purpose | Hidden Reality | Switch |
|---|---|---|---|
| Body | Prove courage/action | Basic safety and presence validation | J1_Trial_Body_Clear |
| Mind | Prove attention | Pattern recognition / challenge response | J1_Trial_Mind_Clear |
| Heart | Prove intent | Trust / intent evaluation | J1_Trial_Heart_Clear |

---

## Required Events

| Event | Purpose |
|---|---|
| Body Trial Event | Short combat, movement, or obstacle challenge |
| Mind Trial Event | Simple observation/pattern interaction |
| Heart Trial Event | Choice, memory, or mercy-themed prompt |
| Trial Completion Gates | Prevent sanctum access until trials complete |
| Transfer to Sanctum | Leads to SCR-HOM-HCV-003 |
| Transfer to Entrance | Leads back to SCR-HOM-HCV-001 |

---

## Implementation Rule

Keep the trials simple. They should be implementable with events, switches, text, movement routes, and optional basic battles.

Do not use custom plugins for this first pass.

Use `ATLAS-TEC-057` for the RPG Maker-ready mechanics, variables, event pages, success conditions, and reset behavior.

---

## Switches Used

```text
J1_Trial_Body_Clear
J1_Trial_Mind_Clear
J1_Trial_Heart_Clear
```

---

## Audio

Use quiet cave ambience with subtle chime after each trial completion.

---

## Encounters

No encounter is required for the first-playable Body Trial. `ATLAS-TEC-057` resolves the Body Trial as an event-only movement/reset challenge.

---

## Acceptance Criteria

- Each trial can be completed once.
- Each trial sets its correct switch.
- Sanctum access is blocked until all three trial switches are ON.
- Player can return to entrance.
- No trial can softlock the player.

---

## Resolved Questions

| Question | Resolution |
|---|---|
| Should Body Trial use a real enemy or event-only obstacle? | Use an event-only movement/reset obstacle for the vertical slice. |
| Should Heart Trial include Elara memory imagery, or remain abstract? | Keep the Heart Trial abstract with placeholder intent choices; do not add final memory imagery in the first playable. |

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Hidden Cave Trials screen object |
| 0.2 | Linked executable Body, Mind, and Heart trial mechanics from ATLAS-TEC-057 |
