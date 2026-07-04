---
atlas_id: ATLAS-TEC-060
title: Home Island Animation Assignment Matrix
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-020
  - ATLAS-TEC-053
  - ATLAS-TEC-055
  - ATLAS-TEC-056
  - ATLAS-TEC-057
  - ATLAS-TEC-058
related:
  - ATLAS-AUD-010
  - ATLAS-TEC-052
  - IMP-HOM-004
  - IMP-HOM-005
  - IMP-HOM-008
  - IMP-HOM-011
---

# Home Island Animation Assignment Matrix

## Objective

Assign every Home Island first-playable combat, story, trial, and feedback beat to an RPG Maker MZ animation database ID or approved no-animation fallback.

This document does not create final art assets or modify RPG Maker project files.

---

## Source References

| ID | Reference |
|---|---|
| `ATLAS-TEC-020` | RPG Maker MZ Bible |
| `ATLAS-TEC-052` | Truth Layer Diagram |
| `ATLAS-TEC-053` | Home Island Vertical Slice Readiness Review |
| `ATLAS-TEC-055` | Home Island Executable Event Specs |
| `ATLAS-TEC-056` | Home Island Combat Database Spec |
| `ATLAS-TEC-057` | Home Island Body Mind Heart Trial Mechanics Spec |
| `ATLAS-TEC-058` | RPG Maker MZ Vertical Slice Build Pipeline |
| `ATLAS-AUD-010` | Home Island Audio Cue Packet |

---

## Placeholder Animation Policy

Use existing RPG Maker MZ animation database rows for first playable testing. These rows are approved placeholders, not final VFX art.

| Rule | Requirement |
|---|---|
| Combat readability first | The player must understand hit, buff, warning, burst, and recovery beats. |
| Story clarity first | Sword, seal, and relay events may use simple flash/light animations plus SE hooks. |
| No missing references | Every skill/event that calls an animation must use an existing RPG Maker animation ID from this matrix. |
| Final polish later | Final custom animations remain non-blocking polish after this matrix. |
| No invented mechanics | Animation choices must not add new damage, status, lore, or gameplay behavior. |

Approved no-animation fallback:

```text
No RPG Maker animation; use screen flash, screen shake, tint, fade, Show Text, and/or Play SE from the event spec.
```

---

## Core Animation IDs

These existing RPG Maker MZ animation rows are approved for Home Island first playable use.

| Animation ID | Animation Name | Approved Use |
|---:|---|---|
| 1 | Hit Physical | Generic impact, enemy basic hit fallback |
| 6 | Slash Physical | Kai sword attack, Guardian Strike |
| 16 | Claw Physical | Ash Rat attack and Nibble |
| 35 | Fog | Murk Bubble and signal/marsh haze |
| 39 | Bodyslam | Gel basic attack |
| 40 | Flash | Story flash, trial confirm, reward feedback |
| 41 | Heal One 1 | Potion and single-target recovery |
| 43 | Heal All 1 | Save/recovery shrine or whole-party recovery |
| 51 | Power up 1 | Pulse Guard and positive activation |
| 54 | Power down 1 | Harmless trial reset or failed input feedback |
| 106 | Neutral One 1 | Archive message or neutral old-system pulse |
| 115 | Laser One | Relay Burst and focused old-system beam |
| 117 | Light Pillar 1 | Sword authentication and major access confirmation |
| 120 | Radiation | Node Seven shutdown or large relay discharge |

---

## Combat Animation Matrix

| Beat | RPG Maker Animation ID | Animation Name | Use Case | Source Atlas Document | Required Sound Effect | Fallback Placeholder Policy |
|---|---:|---|---|---|---|---|
| Basic attack / Kai sword hit | 6 | Slash Physical | Actor Attack skill and Sword weapon attack | `ATLAS-TEC-056` | Engine default attack SE | Use ID 1 Hit Physical if Slash is visually wrong in the active battle mode |
| Meadow Gel attack | 39 | Bodyslam | Meadow Gel basic attack | `ATLAS-TEC-056`, `MON-GEL-001` | Engine default enemy hit SE | Use ID 1 Hit Physical |
| Ash Rat attack | 16 | Claw Physical | Ash Rat basic attack | `ATLAS-TEC-056`, `MON-RAT-001` | Engine default enemy hit SE | Use ID 1 Hit Physical |
| Ash Rat Nibble | 16 | Claw Physical | Skill 101 Nibble | `ATLAS-TEC-056` | Engine default enemy hit SE | Use ID 1 Hit Physical |
| Marsh Gel attack | 39 | Bodyslam | Marsh Gel basic attack | `ATLAS-TEC-056`, `MON-GEL-002` | Engine default enemy hit SE | Use ID 1 Hit Physical |
| Murk Bubble | 35 | Fog | Skill 102 Murk Bubble and Signal-Slick application | `ATLAS-TEC-056`, `ATLAS-TEC-052` | Optional `SFX-HOM-004` if reused as subtle archive/static cue; otherwise engine default | Use ID 54 Power down 1 for debuff readability |
| Node Seven Guardian Strike | 6 | Slash Physical | Skill 110 Strike | `ATLAS-TEC-056`, `BOS-N07-001` | Engine default enemy hit SE | Use ID 1 Hit Physical |
| Pulse Guard | 51 | Power up 1 | Skill 111 Pulse Guard and State 12 application | `ATLAS-TEC-056` | Optional short guard/pulse SE if available | Use ID 40 Flash |
| Warning Tone | 106 | Neutral One 1 | Skill 112 Warning Tone and State 13 Charging | `ATLAS-TEC-056`, `ATLAS-AUD-010` | Use warning-tone placeholder or `SFX-HOM-004` if no dedicated SE exists | Use ID 40 Flash plus Show Text/battle message |
| Relay Burst | 115 | Laser One | Skill 113 Relay Burst | `ATLAS-TEC-056` | Optional relay pulse SE; do not require final asset | Use ID 120 Radiation if Laser One is unavailable |
| Potion item use | 41 | Heal One 1 | Item 1 Potion | `ATLAS-TEC-056` | Engine item/heal SE | Use no animation plus item SE |
| Save/recovery point | 43 | Heal All 1 | Optional save/recovery shrine behavior | `ATLAS-TEC-055`, `ATLAS-TEC-052` | Optional `SFX-HOM-004` archive chime | Use ID 40 Flash or no animation |
| Encounter start / alert | 40 | Flash | Optional screen/map alert before evented battle | `ATLAS-TEC-055`, `ATLAS-TEC-056` | Optional alert SE; no required Home Island cue | Use screen flash only |
| Victory / reward feedback | 40 | Flash | Treasure, trial completion, optional reward cache, post-boss confirmation | `ATLAS-TEC-055`, `ATLAS-TEC-057` | Engine item/victory SE or completion chime | Use Play SE only |

---

## Story And Event Animation Matrix

| Beat | RPG Maker Animation ID | Animation Name | Use Case | Source Atlas Document | Required Sound Effect | Fallback Placeholder Policy |
|---|---:|---|---|---|---|---|
| Tremor event | None | No animation | Ashford tremor trigger uses screen shake/fade | `ATLAS-TEC-055`, `ATLAS-AUD-010` | `SFX-HOM-002` | Screen Shake plus Play SE; no animation required |
| Hidden Cave first entry | 40 | Flash | Optional short cave-entry pulse | `ATLAS-TEC-055` | Optional cave/ambient chime | No animation; Show Text only |
| Body Trial success | 40 | Flash | Completion feedback for `J1_Trial_Body_Clear` | `ATLAS-TEC-057` | Completion chime or `CE_Trial_Complete_Chime` | Play SE and Show Text only |
| Body Trial reset | 54 | Power down 1 | Harmless reset feedback before repositioning Kai | `ATLAS-TEC-057` | Soft failure chime placeholder | Play SE only |
| Mind Trial correct marker | 40 | Flash | Correct marker confirmation | `ATLAS-TEC-057` | Confirm SE placeholder | Play SE only |
| Mind Trial wrong marker | 54 | Power down 1 | Wrong marker/reset feedback | `ATLAS-TEC-057` | Soft failure chime placeholder | Play SE and reset text only |
| Mind Trial completion | 40 | Flash | Completion feedback for `J1_Trial_Mind_Clear` | `ATLAS-TEC-057` | Completion chime or `CE_Trial_Complete_Chime` | Play SE and Show Text only |
| Heart Trial choice prompt | None | No animation | Reflection pedestal prompt | `ATLAS-TEC-057` | None required | Show Choices only |
| Heart Trial completion | 117 | Light Pillar 1 | Intent accepted / `J1_Trial_Heart_Clear` | `ATLAS-TEC-057`, `ATLAS-TEC-052` | Completion chime or `CE_Trial_Complete_Chime` | ID 40 Flash |
| Sanctum gate opens | 117 | Light Pillar 1 | All trials complete, transfer to Sword Sanctum available | `ATLAS-TEC-055`, `ATLAS-TEC-057` | Optional access chime | Fade/transfer only |
| Sword authentication | 117 | Light Pillar 1 | Sword pedestal acceptance and Sword acquisition | `ATLAS-TEC-055`, `ATLAS-AUD-010`, `ATLAS-TEC-052` | `SFX-HOM-003` | Screen Flash plus Play SE |
| Archive message | 106 | Neutral One 1 | `AUTHORIZATION ACCEPTED`, archive recovery text, relay status text | `ATLAS-TEC-055`, `ATLAS-AUD-010` | `SFX-HOM-004` | Play SE and Show Text only |
| Glassfield seal opens | 117 | Light Pillar 1 | Seal accepts Sword and opens lower entrance | `ATLAS-TEC-055`, `ATLAS-AUD-010` | `SFX-HOM-005` | Screen Flash plus Play SE |
| Guardian battle start | 40 | Flash | Optional evented pre-battle alert | `ATLAS-TEC-055`, `ATLAS-TEC-056` | Optional alert SE | Battle Processing directly |
| Guardian defeated | 40 | Flash | Post-battle switch confirmation | `ATLAS-TEC-055` | Engine victory fanfare or completion SE | No animation; switch update only |
| Relay core activation | 106 | Neutral One 1 | Relay device interaction before shutdown | `ATLAS-TEC-055`, `ATLAS-TEC-052` | `SFX-HOM-004` optional |
| Node Seven shutdown | 120 | Radiation | Relay Node Seven shutdown and authority revocation beat | `ATLAS-TEC-055`, `ATLAS-AUD-010`, `ATLAS-TEC-052` | `SFX-HOM-006` | Screen Flash/Fade plus Play SE |
| Lighthouse settles | 40 | Flash | Optional Rustshore lighthouse feedback after Node Seven | `ATLAS-AUD-010`, Rustshore screen spec | `SFX-HOM-007` | Play SE only |
| Mainland departure fade | None | No animation | Boat departure cutscene/fade | `ATLAS-TEC-055` | Optional coastal transition cue | Fadeout/Transfer/Fadein only |

---

## Common Event Animation Guidance

| Common Event | Animation ID | Animation Name | Notes |
|---|---:|---|---|
| `CE_Trial_Complete_Chime` | 40 | Flash | Shared success pulse for Body and Mind; Heart may use ID 117 if the event wants stronger emphasis |
| `CE_Trial_Reset` | 54 | Power down 1 | Harmless failure/reset feedback only |
| `CE-ARCHIVE-MSG` / `CE_Archive_MessageDisplay` | 106 | Neutral One 1 | Pair with `SFX-HOM-004` when available |
| `CE-SWORD-AUTH` / `CE_Sword_Authentication` | 117 | Light Pillar 1 | Pair with `SFX-HOM-003` |
| `CE-RELAY-RESOLVE` / `CE_RelayNode_Shutdown` | 120 | Radiation | Pair with `SFX-HOM-006` |
| `CE_SaveShrine_ArchiveSync` | 43 | Heal All 1 | Optional for save/recovery point |

If a common event is not implemented, use the direct animation command listed in the story/event matrix.

---

## Missing Final Animation Assets

These final effects are not produced yet. They do not block first playable testing because approved RPG Maker placeholder IDs are assigned above.

| Missing Final Asset | Current Placeholder | First-Playable Status |
|---|---|---|
| Custom Sword authentication light/authentication effect | ID 117 Light Pillar 1 | Non-blocking polish |
| Custom Glassfield seal opening access effect | ID 117 Light Pillar 1 | Non-blocking polish |
| Custom Node Seven shutdown relay effect | ID 120 Radiation | Non-blocking polish |
| Custom Murk Bubble signal/marsh effect | ID 35 Fog | Non-blocking polish |
| Custom Pulse Guard shield pulse | ID 51 Power up 1 | Non-blocking polish |
| Custom Warning Tone telegraph | ID 106 Neutral One 1 | Non-blocking polish |
| Custom Relay Burst beam | ID 115 Laser One | Non-blocking polish |
| Custom Body/Mind/Heart trial feedback | IDs 40, 54, 117 | Non-blocking polish |
| Custom reward/treasure sparkle | ID 40 Flash | Non-blocking polish |

---

## Implementation Checklist

- Assign combat skills in `ATLAS-TEC-056` to the animation IDs in this matrix.
- Keep `Warning Tone` visually distinct from `Relay Burst`.
- Pair `Sword authentication`, `Glassfield seal opens`, and `Node Seven shutdown` with their required Home Island SFX cues.
- Use no-animation fallback only where this matrix explicitly permits it.
- Do not create new animation database rows for first playable testing unless a later implementation task requests final VFX production.
- Record any final custom replacement as polish in the implementation report.

---

## Build-Readiness Decision

`BLK-HOM-005` is cleared for first playable testing by this matrix.

Final custom Home Island animation production remains non-blocking asset polish unless a later work order changes the target from placeholder playability to final VFX production.

---

## Validation

Run:

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py validate
```

Expected result:

- 0 errors,
- 0 warnings.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island animation assignment matrix |
