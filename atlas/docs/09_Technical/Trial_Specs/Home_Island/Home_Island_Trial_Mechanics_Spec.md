---
atlas_id: ATLAS-TEC-057
title: Home Island Body Mind Heart Trial Mechanics Spec
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-052
  - ATLAS-TEC-053
  - ATLAS-TEC-054
  - ATLAS-TEC-055
  - IMP-HOM-011
related:
  - SCR-HOM-HCV-002
  - SCR-HOM-HCV-003
  - QST-HOM-002
---

# Home Island Body Mind Heart Trial Mechanics Spec

## Objective

Define the Body, Mind, and Heart trial mechanics clearly enough for RPG Maker MZ implementation in the Home Island vertical slice.

These mechanics are first-playable event specifications. They do not add final dialogue, new lore, or custom plugin requirements.

---

## Source References

| ID | Reference |
|---|---|
| `ATLAS-TEC-052` | Truth Layer Diagram |
| `ATLAS-TEC-053` | Home Island Vertical Slice Readiness Review |
| `ATLAS-TEC-054` | RPG Maker Event Specification Standard |
| `ATLAS-TEC-055` | Home Island Executable Event Specs |
| `SCR-HOM-HCV-002` | Hidden Cave Trials |
| `SCR-HOM-HCV-003` | Sword Sanctum |
| `QST-HOM-002` | The Sword Awakens |
| `IMP-HOM-011` | Build Skyreach and Hidden Cave Screens |

---

## Design Constraints

- Use RPG Maker MZ map events, switches, variables, self switches, movement routes, Show Choices, Show Text placeholders, and transfer commands only.
- Do not require custom plugins.
- Do not use final dialogue.
- Do not introduce permanent failure.
- Do not explain the hidden cybersecurity layer directly to the player.
- Keep each trial distinct and short enough for the opening vertical slice.

---

## Truth Layer Mapping

| Trial | Story Layer | Gameplay Layer | Hidden Truth | RPG Maker Implementation |
|---|---|---|---|---|
| Body | Kai proves he will move forward despite fear | Timed-feeling movement hazard with reset | Basic presence and safety validation | Floor triggers, reset transfer, success switch |
| Mind | Kai proves attention and observation | Three-marker pattern sequence | Challenge-response pattern check | Sequence variable and marker events |
| Heart | Kai proves intent without receiving full explanation | Choice/intent prompt with no permanent fail | Trust and intent evaluation | Show Choices, intent variable, success switch |

The player should experience these as quiet cave trials. Atlas understands them as degraded validation steps, but the vertical slice should not stop to explain that technical meaning.

---

## Shared State

### Required Switches

Use the existing Journey I switches:

```text
J1_Trial_Body_Clear
J1_Trial_Mind_Clear
J1_Trial_Heart_Clear
```

### Required Variables

Use variable slots from the puzzle/dungeon range defined by `ATLAS-TEC-054`.

| Variable Name | Range | Initial Value | Use |
|---|---:|---:|---|
| Trial_Body_Attempts | 81-120 | 0 | Counts Body Trial resets for testing and debugging |
| Trial_Mind_SequenceStep | 81-120 | 0 | Tracks current Mind Trial marker progress |
| Trial_Heart_IntentChoice | 81-120 | 0 | Stores the selected Heart Trial intent |

These variables do not need to be shown to the player.

### Common Event Candidates

| Common Event | Required? | Purpose |
|---|---:|---|
| CE_Trial_Complete_Chime | Optional | Plays the shared trial completion chime and flash |
| CE_Trial_Reset | Optional | Standard short reset feedback before repositioning Kai |
| CE_Archive_MessageDisplay | Optional | Displays short archive/system placeholders if already available |

If these common events are not implemented, use direct event commands listed below.

---

## Trial Layout Requirements

All three trials live on `SCR-HOM-HCV-002 / DGN_HiddenCave_Trials`.

Recommended layout:

| Area | Placement |
|---|---|
| Body Trial | Left or lower-left chamber with a start tile, three hazard tiles, and one finish marker |
| Mind Trial | Center chamber with one start plaque and three interactable markers |
| Heart Trial | Right or lower-right chamber with one reflection pedestal |
| Sanctum Gate | North or central exit gated by all three trial switches |

The map may be one room divided by visual sections. The mechanics should remain evented, not tileset-dependent.

---

## Body Trial

### Purpose

Body proves action and courage. It asks the player to cross a short obstacle lane and accept a harmless reset if they step wrong.

### RPG Maker Mechanic

The player begins at a visible start tile, crosses a short lane, avoids three hazard/reset tiles, and touches the finish marker.

No combat is required for the first playable Body Trial. This resolves the earlier open question in favor of an event-only obstacle so trial readiness does not depend on encounter tuning.

### Events

| Event ID | Event Name | Trigger | Priority | Purpose |
|---|---|---|---|---|
| EVT-HOM-012 | EVT-HOM-012 Body Trial Finish | Player Touch | Below Characters | Completes Body Trial |
| EVT-HOM-012A | EVT-HOM-012A Body Trial Reset 1 | Player Touch | Below Characters | Resets player to Body start |
| EVT-HOM-012B | EVT-HOM-012B Body Trial Reset 2 | Player Touch | Below Characters | Resets player to Body start |
| EVT-HOM-012C | EVT-HOM-012C Body Trial Reset 3 | Player Touch | Below Characters | Resets player to Body start |

The suffix events may remain implementation-local helpers, but their event names must include `EVT-HOM-012` so reports can trace them to the Body Trial.

### Body Finish Event Pages

| Page | Condition | Trigger | Commands | Completion |
|---|---|---|---|---|
| 1 | `J1_Trial_Body_Clear` OFF | Player Touch | Comment `ATLAS EVT-HOM-012 BODY_SUCCESS`; Play SE completion chime or call `CE_Trial_Complete_Chime`; Show Text `PH-DLG-TRIAL-COMPLETE`; Control Switch `J1_Trial_Body_Clear = ON` | Body trial complete |
| 2 | `J1_Trial_Body_Clear` ON | Player Touch | Optional Show Text `This trial is complete.` or no command | No repeat |

RPG Maker page order:

- Page 1 default.
- Page 2 conditioned on `J1_Trial_Body_Clear` and placed after Page 1.

### Body Reset Event Pages

| Page | Condition | Trigger | Commands | Completion |
|---|---|---|---|---|
| 1 | `J1_Trial_Body_Clear` OFF | Player Touch | Comment `ATLAS EVT-HOM-012 BODY_RESET`; Control Variables `Trial_Body_Attempts += 1`; Play SE failure/soft chime placeholder; Transfer Player to Body Trial start tile on same map; optional Show Text `The path asks you to try again.` | Player returns to start |
| 2 | `J1_Trial_Body_Clear` ON | Player Touch | No command or harmless pass-through | Reset disabled after completion |

Failure behavior:

- No HP loss.
- No game over.
- No permanent state.
- Player can retry immediately.

---

## Mind Trial

### Purpose

Mind proves attention. It asks the player to observe a short pattern and repeat it using three markers.

### RPG Maker Mechanic

The player interacts with a start plaque that displays the sequence:

```text
Left marker -> Right marker -> Center marker
```

Then the player must interact with the markers in that order.

### Events

| Event ID | Event Name | Trigger | Priority | Purpose |
|---|---|---|---|---|
| EVT-HOM-013 | EVT-HOM-013 Mind Trial Start Plaque | Action Button | Same as Characters | Shows sequence and resets progress |
| EVT-HOM-013A | EVT-HOM-013A Mind Marker Left | Action Button | Same as Characters | First marker |
| EVT-HOM-013B | EVT-HOM-013B Mind Marker Right | Action Button | Same as Characters | Second marker |
| EVT-HOM-013C | EVT-HOM-013C Mind Marker Center | Action Button | Same as Characters | Third marker and success |

### Mind Start Plaque Pages

| Page | Condition | Trigger | Commands | Completion |
|---|---|---|---|---|
| 1 | `J1_Trial_Mind_Clear` OFF | Action Button | Comment `ATLAS EVT-HOM-013 MIND_START`; Control Variable `Trial_Mind_SequenceStep = 0`; Show Text `Observe the order: left, right, center.` | Sequence shown |
| 2 | `J1_Trial_Mind_Clear` ON | Action Button | Show Text `This trial is complete.` or no command | No repeat |

### Marker Logic

| Marker Event | Correct Variable Before Interaction | Correct Commands | Wrong Commands |
|---|---:|---|---|
| EVT-HOM-013A Left | 0 | Play SE confirm; Control Variable `Trial_Mind_SequenceStep = 1` | Control Variable `Trial_Mind_SequenceStep = 0`; Show Text reset hint |
| EVT-HOM-013B Right | 1 | Play SE confirm; Control Variable `Trial_Mind_SequenceStep = 2` | Control Variable `Trial_Mind_SequenceStep = 0`; Show Text reset hint |
| EVT-HOM-013C Center | 2 | Play SE completion chime or call `CE_Trial_Complete_Chime`; Control Variable `Trial_Mind_SequenceStep = 3`; Control Switch `J1_Trial_Mind_Clear = ON`; Show Text `PH-DLG-TRIAL-COMPLETE` | Control Variable `Trial_Mind_SequenceStep = 0`; Show Text reset hint |

Each marker should have two pages:

| Page | Condition | Commands |
|---|---|---|
| 1 | `J1_Trial_Mind_Clear` OFF | Runs marker logic above |
| 2 | `J1_Trial_Mind_Clear` ON | No command or complete-state text |

Failure/reset behavior:

- Wrong marker resets `Trial_Mind_SequenceStep` to 0.
- No HP loss.
- No permanent failure.
- The start plaque can always re-display the sequence before completion.

---

## Heart Trial

### Purpose

Heart proves intent. It asks the player to choose why Kai reaches for the Sword without requiring final dialogue or a lore reveal.

### RPG Maker Mechanic

The player interacts with one reflection pedestal. The event shows a short placeholder prompt and three choices.

Choices:

| Choice | Variable Value | Result |
|---|---:|---|
| Protect home | 1 | Success |
| Seek the truth | 2 | Success |
| Turn back for now | 3 | Reset / no completion |

Both success choices are valid for the vertical slice. The third choice lets a cautious player leave without failing.

### Heart Event Pages

| Page | Condition | Trigger | Commands | Completion |
|---|---|---|---|---|
| 1 | `J1_Trial_Heart_Clear` OFF | Action Button | Comment `ATLAS EVT-HOM-014 HEART_PROMPT`; Show Text placeholder prompt; Show Choices `Protect home / Seek the truth / Turn back for now`; for choice 1 set `Trial_Heart_IntentChoice = 1`, switch ON; for choice 2 set `Trial_Heart_IntentChoice = 2`, switch ON; for choice 3 set `Trial_Heart_IntentChoice = 3`, show reset text, switch remains OFF | Heart trial complete only on choices 1 or 2 |
| 2 | `J1_Trial_Heart_Clear` ON | Action Button | Show Text `This trial is complete.` or no command | No repeat |

Success commands for choices 1 and 2:

```text
Play SE completion chime or call CE_Trial_Complete_Chime
Show Text PH-DLG-TRIAL-COMPLETE
Control Switch J1_Trial_Heart_Clear = ON
```

Failure/reset behavior:

- Choosing `Turn back for now` does not punish the player.
- The player can interact again and choose a success option.
- Do not branch into final dialogue or flashback imagery in this first pass.

---

## Sanctum Gate Dependency

`EVT-HOM-015 / TRN-HOM-013` remains the gate from `SCR-HOM-HCV-002` to `SCR-HOM-HCV-003`.

Gate condition:

```text
J1_Trial_Body_Clear = ON
J1_Trial_Mind_Clear = ON
J1_Trial_Heart_Clear = ON
```

When all three switches are ON, the transfer to the Sword Sanctum is available.

---

## Implementation Checklist

- Body Trial can be completed with movement and reset events only.
- Mind Trial can be completed by interacting with left, right, center markers in sequence.
- Heart Trial can be completed by choosing either approved intent option.
- Wrong Body/Mind actions reset only the local trial state.
- Heart Trial has a non-completion choice that lets the player back out.
- Each trial switch turns ON only once.
- The sanctum gate opens only after all three trial switches are ON.
- No trial can softlock the player.

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
| 0.1 | Initial Home Island Body, Mind, and Heart trial mechanics specification |
