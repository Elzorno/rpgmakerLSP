---
atlas_id: ATLAS-TEC-055
title: Home Island Executable Event Specs
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-041
  - ATLAS-TEC-042
  - ATLAS-TEC-044
  - ATLAS-TEC-052
  - ATLAS-TEC-054
  - ATLAS-TEC-057
related:
  - IMP-HOM-010
  - IMP-HOM-011
  - IMP-HOM-012
  - IMP-HOM-013
  - IMP-HOM-014
  - IMP-HOM-015
---

# Home Island Executable Event Specs

## Purpose

This document converts the Home Island event registry into RPG Maker MZ-ready event specifications.

Use `ATLAS-TEC-054` as the event standard. This page supplies the Home Island-specific event names, screens, triggers, page conditions, switches, variables, command sequences, transfer destinations, and placeholder dialogue IDs.

No final dialogue or new lore is defined here.

---

## Implementation Rules

- Every event name begins with its Atlas event ID, transfer ID, object ID, or NPC ID.
- Dialogue placeholders use `PH-DLG-*` identifiers until final text exists.
- `Self Switch A` means local completed/collected/exhausted state.
- Transfer event commands may call `CE-SCREEN-FADE` if that common event exists; otherwise use direct Fadeout, Transfer Player, Fadein commands.
- Archive or old-system text may call `CE-ARCHIVE-MSG` if that common event exists; otherwise use direct Show Text placeholder commands.
- Save/recovery points may call `CE_SaveShrine_ArchiveSync` if that common event exists.

---

## Dialogue Placeholder IDs

| Placeholder ID | Use |
|---|---|
| PH-DLG-ELARA-INTRO | Elara default opening line from `ATLAS-STY-010` |
| PH-DLG-ELARA-POST-NODE | Elara post-Node Seven line from `ATLAS-STY-010` |
| PH-DLG-ASH-CHILD-INTRO | Child near old panel intro line from `ATLAS-STY-010` |
| PH-DLG-ASH-CHILD-TREMOR | Child near old panel after tremor line from `ATLAS-STY-010` |
| PH-DLG-ASH-FARMER-INTRO | Farmer intro line from `ATLAS-STY-010` |
| PH-DLG-ASH-FARMER-SWORD | Farmer after Sword line from `ATLAS-STY-010` |
| PH-DLG-ASH-JOKER-INTRO | Skyreach Joker intro/taboo line from `ATLAS-STY-010` |
| PH-DLG-ASH-MSG-INTRO | Dock Messenger intro/Rustshore foreshadow line from `ATLAS-STY-010` |
| PH-DLG-SHOP-GREETING | Shopkeeper greeting from `ATLAS-STY-010` |
| PH-DLG-DOCKMASTER-LOCKED | Dockmaster travel-blocked placeholder |
| PH-DLG-DOCKMASTER-UNLOCKED | Dockmaster travel-available placeholder |
| PH-DLG-SIGNAL-CLUE | Nontechnical environmental signal clue |
| PH-DLG-TRIAL-COMPLETE | Generic trial completion placeholder |

---

## Common Event Candidates

| Common Event ID | Required? | Purpose |
|---|---:|---|
| CE-SCREEN-FADE | Optional | Reusable fade and transfer wrapper |
| CE-ARCHIVE-MSG | Optional | Reusable old-system message display |
| CE-SWORD-AUTH | Optional | Sword authentication presentation |
| CE-RELAY-RESOLVE | Optional | Relay shutdown presentation |
| CE_SaveShrine_ArchiveSync | Optional | Save/recovery shrine behavior |
| CE_Trial_Complete_Chime | Optional | Shared trial completion chime/flash from `ATLAS-TEC-057` |
| CE_Trial_Reset | Optional | Shared harmless trial reset feedback from `ATLAS-TEC-057` |

If a common event is not implemented yet, use the direct commands listed in the event specs.

---

## Transfer Event Specs

All transfers follow `ATLAS-TEC-054` section 3.5.

Standard command sequence for open transfer pages:

```text
Comment: ATLAS <Transfer ID> open transfer
Fadeout Screen
Transfer Player: <destination map>
Fadein Screen
```

Standard command sequence for locked transfer pages:

```text
Comment: ATLAS <Transfer ID> locked transfer
Show Text: <placeholder locked message>
```

| Transfer ID | Event Name | Source Screen / Map | Destination | Trigger | Priority | Pages | Conditions / Commands |
|---|---|---|---|---|---|---:|---|
| TRN-HOM-001 | TRN-HOM-001 To Ashford Exterior | SCR-HOM-ASH-002 / INT_Ashford_ElaraHouse | TWN_Ashford_Exterior | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-002 | TRN-HOM-002 To Elara House | SCR-HOM-ASH-001 / TWN_Ashford_Exterior | INT_Ashford_ElaraHouse | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-003 | TRN-HOM-003 To Ashford Shop | SCR-HOM-ASH-001 / TWN_Ashford_Exterior | INT_Ashford_Shop | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-004 | TRN-HOM-004 To Ashford Exterior | SCR-HOM-ASH-003 / INT_Ashford_Shop | TWN_Ashford_Exterior | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-005 | TRN-HOM-005 To Skyreach | SCR-HOM-ASH-001 / TWN_Ashford_Exterior | DGN_SkyreachHill_Path | Player Touch | Below Characters | 2 | Page 1 locked when `J1_Skyreach_AccessOpen` OFF; Page 2 open when ON |
| TRN-HOM-006 | TRN-HOM-006 To Ashford Route | SCR-HOM-SKY-001 / DGN_SkyreachHill_Path | TWN_Ashford_Exterior | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-007 | TRN-HOM-007 To Rustshore | SCR-HOM-ASH-001 / TWN_Ashford_Exterior | TWN_Rustshore_Docks | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-008 | TRN-HOM-008 To Ashford Route | SCR-HOM-RST-001 / TWN_Rustshore_Docks | TWN_Ashford_Exterior | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-009 | TRN-HOM-009 To Hidden Cave | SCR-HOM-SKY-001 / DGN_SkyreachHill_Path | DGN_HiddenCave_Entrance | Player Touch | Below Characters | 1 | Page 1 always open; route already gated by TRN-HOM-005 |
| TRN-HOM-010 | TRN-HOM-010 To Skyreach | SCR-HOM-HCV-001 / DGN_HiddenCave_Entrance | DGN_SkyreachHill_Path | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-011 | TRN-HOM-011 To Trials | SCR-HOM-HCV-001 / DGN_HiddenCave_Entrance | DGN_HiddenCave_Trials | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-012 | TRN-HOM-012 To Cave Entrance | SCR-HOM-HCV-002 / DGN_HiddenCave_Trials | DGN_HiddenCave_Entrance | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-013 | TRN-HOM-013 To Sword Sanctum | SCR-HOM-HCV-002 / DGN_HiddenCave_Trials | DGN_HiddenCave_Sanctum | Player Touch | Below Characters | 2 | Page 1 locked unless all trial switches ON; Page 2 open when all trial switches ON |
| TRN-HOM-014 | TRN-HOM-014 To Trials | SCR-HOM-HCV-003 / DGN_HiddenCave_Sanctum | DGN_HiddenCave_Trials | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-015 | TRN-HOM-015 To Glassfield | SCR-HOM-ASH-001 / TWN_Ashford_Exterior | DGN_Glassfield_Ruins_Exterior | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-016 | TRN-HOM-016 To Ashford Route | SCR-HOM-GLS-001 / DGN_Glassfield_Ruins_Exterior | TWN_Ashford_Exterior | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-017 | TRN-HOM-017 To Sealed Node | SCR-HOM-GLS-001 / DGN_Glassfield_Ruins_Exterior | DGN_SealedNode_Upper | Player Touch | Below Characters | 2 | Page 1 locked when `J1_Glassfield_SealOpened` OFF; Page 2 open when ON |
| TRN-HOM-018 | TRN-HOM-018 To Glassfield | SCR-HOM-SND-001 / DGN_SealedNode_Upper | DGN_Glassfield_Ruins_Exterior | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-019 | TRN-HOM-019 To Core Path | SCR-HOM-SND-001 / DGN_SealedNode_Upper | DGN_SealedNode_CorePath | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-020 | TRN-HOM-020 To Upper Node | SCR-HOM-SND-002 / DGN_SealedNode_CorePath | DGN_SealedNode_Upper | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-021 | TRN-HOM-021 To Guardian | SCR-HOM-SND-002 / DGN_SealedNode_CorePath | DGN_SealedNode_Guardian | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-022 | TRN-HOM-022 To Core Path | SCR-HOM-SND-003 / DGN_SealedNode_Guardian | DGN_SealedNode_CorePath | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-023 | TRN-HOM-023 To Relay Core | SCR-HOM-SND-003 / DGN_SealedNode_Guardian | DGN_SealedNode_RelayCore | Player Touch | Below Characters | 2 | Page 1 locked when `J1_Node07_GuardianDefeated` OFF; Page 2 open when ON |
| TRN-HOM-024 | TRN-HOM-024 To Guardian | SCR-HOM-SND-004 / DGN_SealedNode_RelayCore | DGN_SealedNode_Guardian | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-025 | TRN-HOM-025 To Departure | SCR-HOM-RST-001 / TWN_Rustshore_Docks | CUT_Mainland_Departure | Action Button | Same as Characters | 2 | Page 1 locked when `J1_Mainland_TravelUnlocked` OFF; Page 2 asks confirmation and transfers when ON |
| TRN-HOM-026 | TRN-HOM-026 To Journey II Start | SCR-HOM-RST-002 / CUT_Mainland_Departure | Journey II start placeholder | Autorun | Same as Characters | 1 | Page 1 sets `Current_Journey = 2`, then transfers to labeled placeholder or future Coalmouth entry |
| TRN-HOM-027 | TRN-HOM-027 To Fogfen | SCR-HOM-ASH-001 / TWN_Ashford_Exterior | FLD_Fogfen_Marsh_Field | Player Touch | Below Characters | 1 | Page 1 always open optional transfer |
| TRN-HOM-028 | TRN-HOM-028 To Ashford Route | SCR-HOM-FOG-001 / FLD_Fogfen_Marsh_Field | TWN_Ashford_Exterior | Player Touch | Below Characters | 1 | Page 1 always open transfer |
| TRN-HOM-029 | TRN-HOM-029 To Deeper Marsh | SCR-HOM-FOG-001 / FLD_Fogfen_Marsh_Field | FLD_Fogfen_Deeper_Marsh_Pocket | Player Touch | Below Characters | 1 | Page 1 always open optional transfer |
| TRN-HOM-030 | TRN-HOM-030 To Marsh Field | SCR-HOM-FOG-002 / FLD_Fogfen_Deeper_Marsh_Pocket | FLD_Fogfen_Marsh_Field | Player Touch | Below Characters | 1 | Page 1 always open transfer |

Completion condition for every transfer: the player arrives at the destination map and can return where the registry defines a return path.

---

## Ashford Event Specs

### EVT-HOM-001 — Player Start

| Field | Value |
|---|---|
| Event Name | EVT-HOM-001 Player Start |
| Screen / Map | SCR-HOM-ASH-002 / INT_Ashford_ElaraHouse |
| Standard | ATLAS-TEC-054 section 3.8 |
| Trigger | Autorun or engine start position plus optional Autorun |
| Priority | Same as Characters if evented; otherwise not applicable |
| Page Count | 2 if intro evented |
| Switches | `J1_Ashford_IntroComplete` |
| Variables | `Current_Journey = 1`, `Archive_Recovery_Percent = 0`, `Current_Relay_Count = 0` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_Ashford_IntroComplete` OFF | Comment `ATLAS EVT-HOM-001`; set variables to initial values if not already set; optional Show Text `PH-DLG-ELARA-INTRO`; Control Switch `J1_Ashford_IntroComplete = ON` | Intro complete |
| 2 | `J1_Ashford_IntroComplete` ON | No autorun commands | Event inactive |

### EVT-HOM-002 — Elara Intro Dialogue

| Field | Value |
|---|---|
| Event Name | NPC-ELA-001 Elara |
| Screen / Map | SCR-HOM-ASH-002 / INT_Ashford_ElaraHouse |
| Standard | ATLAS-TEC-054 section 3.4 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 4 |
| Switches | `J1_Tremor_Event`, `J1_Sword_Obtained`, `NPC_Ashford_PostNode07` |
| Variables | None |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | None | Comment `ATLAS NPC-ELA-001 STATE_01_INTRO`; Show Text `PH-DLG-ELARA-INTRO` | Dialogue closes |
| 2 | `J1_Tremor_Event` ON | Comment `ATLAS NPC-ELA-001 STATE_02_AFTER_TREMOR`; Show Text from `ATLAS-STY-010` tremor placeholder | Dialogue closes |
| 3 | `J1_Sword_Obtained` ON | Comment `ATLAS NPC-ELA-001 STATE_03_AFTER_SWORD`; Show Text from `ATLAS-STY-010` Sword placeholder | Dialogue closes |
| 4 | `NPC_Ashford_PostNode07` ON | Comment `ATLAS NPC-ELA-001 STATE_04_AFTER_NODE07`; Show Text `PH-DLG-ELARA-POST-NODE` | Dialogue closes |

### EVT-HOM-003 to EVT-HOM-006 — Ashford NPC Conversations

All Ashford placeholder NPCs follow `ATLAS-TEC-054` section 3.4.

| Event ID | Event Name | Screen / Map | Trigger | Priority | Pages | Page Conditions / Dialogue |
|---|---|---|---|---|---:|---|
| EVT-HOM-003 | NPC-ASH-CHD-001 Child Near Old Panel | SCR-HOM-ASH-001 / TWN_Ashford_Exterior | Action Button | Same as Characters | 2 | Page 1 none, Show Text `PH-DLG-ASH-CHILD-INTRO`; Page 2 `J1_Tremor_Event` ON, Show Text `PH-DLG-ASH-CHILD-TREMOR` |
| EVT-HOM-004 | NPC-ASH-FRM-001 Farmer With Warm Stones | SCR-HOM-ASH-001 / TWN_Ashford_Exterior | Action Button | Same as Characters | 2 | Page 1 none, Show Text `PH-DLG-ASH-FARMER-INTRO`; Page 2 `J1_Sword_Obtained` ON, Show Text `PH-DLG-ASH-FARMER-SWORD` |
| EVT-HOM-005 | NPC-ASH-JOK-001 Skyreach Joker | SCR-HOM-ASH-001 / TWN_Ashford_Exterior | Action Button | Same as Characters | 2 | Page 1 none, Show Text `PH-DLG-ASH-JOKER-INTRO`; Page 2 `J1_Skyreach_AccessOpen` ON, Show Text approved post-tremor placeholder |
| EVT-HOM-006 | NPC-ASH-MSG-001 Dock Messenger | SCR-HOM-ASH-001 / TWN_Ashford_Exterior | Action Button | Same as Characters | 2 | Page 1 none, Show Text `PH-DLG-ASH-MSG-INTRO`; Page 2 `J1_Mainland_TravelUnlocked` ON, Show Text approved travel-ready placeholder |

Completion condition: dialogue closes without setting story-critical switches.

### EVT-HOM-007 — Ashford Hidden Item

| Field | Value |
|---|---|
| Event Name | EVT-HOM-007 Hidden Item |
| Screen / Map | SCR-HOM-ASH-001 / TWN_Ashford_Exterior |
| Standard | ATLAS-TEC-054 section 3.6 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 2 |
| Self Switches | Self Switch A |
| Variables | None |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | Self Switch A OFF | Comment `ATLAS EVT-HOM-007`; Play SE `Item` placeholder; Change Items approved minor reward +1; Show Text `Found an item.`; Control Self Switch A = ON | Reward collected once |
| 2 | Self Switch A ON | Show Text `Nothing else is hidden here.` or no command | Cannot recollect |

### EVT-HOM-008 — Ashford Shopkeeper

| Field | Value |
|---|---|
| Event Name | NPC-ASH-SHP-001 Shopkeeper |
| Screen / Map | SCR-HOM-ASH-003 / INT_Ashford_Shop |
| Standard | ATLAS-TEC-054 section 3.7 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 2 |
| Switches | `NPC_Ashford_PostNode07` optional |
| Variables | None |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | None | Comment `ATLAS EVT-HOM-008`; Show Text `PH-DLG-SHOP-GREETING`; Show Choices `Buy / Not now`; Buy: Shop Processing approved starter inventory or placeholder message; Not now: Show Text short farewell | Shop closes |
| 2 | `NPC_Ashford_PostNode07` ON | Same as Page 1 with approved post-node greeting; inventory unchanged unless later economy spec changes it | Shop closes |

### EVT-HOM-009 — Tremor Trigger

| Field | Value |
|---|---|
| Event Name | EVT-HOM-009 Tremor Trigger |
| Screen / Map | SCR-HOM-ASH-001 / TWN_Ashford_Exterior |
| Standard | ATLAS-TEC-054 section 3.8 |
| Trigger | Player Touch or Autorun from explicit route tile |
| Priority | Same as Characters |
| Page Count | 2 |
| Switches | `J1_Tremor_Event`, `J1_Skyreach_AccessOpen` |
| Variables | None |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_Tremor_Event` OFF | Comment `ATLAS EVT-HOM-009`; Fadeout Screen; Play SE `SFX-HOM-002` placeholder; Screen Shake; Fadein Screen; Control Switch `J1_Tremor_Event = ON`; Control Switch `J1_Skyreach_AccessOpen = ON` | Skyreach route opens |
| 2 | `J1_Tremor_Event` ON | No commands or route flavor text | No repeat |

---

## Skyreach and Hidden Cave Event Specs

### EVT-HOM-010 — Skyreach Gate

| Field | Value |
|---|---|
| Event Name | EVT-HOM-010 Skyreach Gate |
| Screen / Map | SCR-HOM-SKY-001 / DGN_SkyreachHill_Path or SCR-HOM-ASH-001 route edge |
| Standard | ATLAS-TEC-054 sections 3.5 and 3.4 |
| Trigger | Player Touch |
| Priority | Below Characters for transfer tile, Same as Characters for blocker |
| Page Count | 2 |
| Switches | `J1_Skyreach_AccessOpen` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_Skyreach_AccessOpen` OFF | Comment `ATLAS EVT-HOM-010`; Show Text approved blocked-path placeholder; no transfer | Player remains outside |
| 2 | `J1_Skyreach_AccessOpen` ON | Run `TRN-HOM-005` open transfer or remove blocker | Player can reach Skyreach |

### EVT-HOM-011 — Hidden Cave First Entry

| Field | Value |
|---|---|
| Event Name | EVT-HOM-011 Hidden Cave First Entry |
| Screen / Map | SCR-HOM-HCV-001 / DGN_HiddenCave_Entrance |
| Standard | ATLAS-TEC-054 section 3.8 |
| Trigger | Player Touch |
| Priority | Below Characters |
| Page Count | 2 |
| Switches | `J1_HiddenCave_Entered` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_HiddenCave_Entered` OFF | Comment `ATLAS EVT-HOM-011`; optional Show Text short cave-entry placeholder; Control Switch `J1_HiddenCave_Entered = ON` | Cave entry tracked |
| 2 | `J1_HiddenCave_Entered` ON | No commands | No repeat |

### EVT-HOM-012 to EVT-HOM-014 — Trial Events

These events follow `ATLAS-TEC-054` section 3.9 and the executable mechanics in `ATLAS-TEC-057`.

| Event ID | Event Name | Screen / Map | Mechanic | Trigger | Priority | Completion |
|---|---|---|---|---|---|---|
| EVT-HOM-012 | EVT-HOM-012 Body Trial Finish plus reset helpers | SCR-HOM-HCV-002 / DGN_HiddenCave_Trials | Movement lane with harmless reset tiles | Player Touch | Below Characters | Control Switch `J1_Trial_Body_Clear = ON` |
| EVT-HOM-013 | EVT-HOM-013 Mind Trial Start Plaque plus marker helpers | SCR-HOM-HCV-002 / DGN_HiddenCave_Trials | Left, right, center marker sequence | Action Button | Same as Characters | Control Switch `J1_Trial_Mind_Clear = ON` |
| EVT-HOM-014 | EVT-HOM-014 Heart Trial Pedestal | SCR-HOM-HCV-002 / DGN_HiddenCave_Trials | Intent choice prompt | Action Button | Same as Characters | Control Switch `J1_Trial_Heart_Clear = ON` |

Required trial variables from `ATLAS-TEC-057`:

```text
Trial_Body_Attempts
Trial_Mind_SequenceStep
Trial_Heart_IntentChoice
```

Page pattern for each completed-state trial event:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | Relevant trial switch OFF | Comment `ATLAS <Event ID>`; run the mechanic-specific commands in `ATLAS-TEC-057` | Trial switch ON when success condition is met |
| 2 | Relevant trial switch ON | Show Text `This trial is complete.` or no command | No repeat |

Failure and reset behavior:

- Body reset tiles increment `Trial_Body_Attempts` and return Kai to the Body Trial start tile.
- Mind marker mistakes reset `Trial_Mind_SequenceStep` to 0.
- Heart choice `Turn back for now` sets `Trial_Heart_IntentChoice = 3` and leaves `J1_Trial_Heart_Clear` OFF.
- No trial causes HP loss, game over, or permanent failure in the vertical slice.

### EVT-HOM-015 — Sanctum Gate

| Field | Value |
|---|---|
| Event Name | EVT-HOM-015 Sanctum Gate |
| Screen / Map | SCR-HOM-HCV-002 / DGN_HiddenCave_Trials |
| Standard | ATLAS-TEC-054 section 3.5 |
| Trigger | Player Touch |
| Priority | Below Characters |
| Page Count | 2 |
| Switches | `J1_Trial_Body_Clear`, `J1_Trial_Mind_Clear`, `J1_Trial_Heart_Clear` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | Any trial switch OFF | Comment `ATLAS EVT-HOM-015 locked`; Show Text `Three trials remain unfinished.` | Player remains in trials |
| 2 | All trial switches ON | Comment `ATLAS TRN-HOM-013`; Fadeout; Transfer Player `DGN_HiddenCave_Sanctum`; Fadein | Player enters sanctum |

### EVT-HOM-016 — Sword Pedestal

| Field | Value |
|---|---|
| Event Name | EVT-HOM-016 Sword Pedestal |
| Screen / Map | SCR-HOM-HCV-003 / DGN_HiddenCave_Sanctum |
| Standard | ATLAS-TEC-054 sections 3.8 and 3.9 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 3 |
| Switches | `J1_Sword_Obtained`, `SYS_ProtocolSkills_Unlocked` |
| Variables | `Archive_Recovery_Percent = 3` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | Any trial switch OFF | Comment `ATLAS EVT-HOM-016 incomplete`; Show Text `The pedestal is silent.` | No state change |
| 2 | All trial switches ON and `J1_Sword_Obtained` OFF | Comment `ATLAS EVT-HOM-016 Sword authentication`; Fadeout; Play SE `SFX-HOM-003` placeholder; optional Flash Screen; Show Text `AUTHORIZATION ACCEPTED`; Change Items/Weapons approved Sword entry; Control Switch `J1_Sword_Obtained = ON`; Control Switch `SYS_ProtocolSkills_Unlocked = ON` if design chooses immediate unlock; Control Variable `Archive_Recovery_Percent = 3`; Fadein | Sword obtained once |
| 3 | `J1_Sword_Obtained` ON | Show Text `ARCHIVE RECOVERY: 3%` or no command | No repeat |

---

## Glassfield and Sealed Node Event Specs

### EVT-HOM-017 — Glassfield Seal

| Field | Value |
|---|---|
| Event Name | EVT-HOM-017 Glassfield Seal |
| Screen / Map | SCR-HOM-GLS-001 / DGN_Glassfield_Ruins_Exterior |
| Standard | ATLAS-TEC-054 sections 3.5 and 3.8 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 3 |
| Switches | `J1_Sword_Obtained`, `J1_Glassfield_SealOpened` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_Sword_Obtained` OFF | Comment `ATLAS EVT-HOM-017 locked`; Show Text approved missing-Sword placeholder | Seal remains closed |
| 2 | `J1_Sword_Obtained` ON and `J1_Glassfield_SealOpened` OFF | Comment `ATLAS EVT-HOM-017 open seal`; Play SE `SFX-HOM-005` placeholder; optional screen flash; Control Switch `J1_Glassfield_SealOpened = ON`; Show Text short access placeholder | Sealed Node entrance opens |
| 3 | `J1_Glassfield_SealOpened` ON | Show Text optional open-seal placeholder or run `TRN-HOM-017` transfer if placed on same tile | Entrance remains open |

### EVT-HOM-018 — Surface Fragment

| Field | Value |
|---|---|
| Event Name | EVT-HOM-018 Surface Fragment |
| Screen / Map | SCR-HOM-GLS-001 / DGN_Glassfield_Ruins_Exterior |
| Standard | ATLAS-TEC-054 section 3.4 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 2 |
| Self Switches | Self Switch A |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | Self Switch A OFF | Comment `ATLAS EVT-HOM-018`; Play SE `SFX-HOM-004` placeholder; Show Text approved optional warning placeholder; Control Self Switch A = ON | Fragment examined |
| 2 | Self Switch A ON | Show Text optional quiet fragment placeholder or no command | No repeat reward |

### EVT-HOM-019 — Sealed Node First Entry

| Field | Value |
|---|---|
| Event Name | EVT-HOM-019 Sealed Node First Entry |
| Screen / Map | SCR-HOM-SND-001 / DGN_SealedNode_Upper |
| Standard | ATLAS-TEC-054 section 3.8 |
| Trigger | Player Touch |
| Priority | Below Characters |
| Page Count | 2 |
| Switches | `J1_SealedNode_Entered` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_SealedNode_Entered` OFF | Comment `ATLAS EVT-HOM-019`; optional Show Text archive distortion placeholder; Control Switch `J1_SealedNode_Entered = ON` | Entry tracked |
| 2 | `J1_SealedNode_Entered` ON | No commands | No repeat |

### EVT-HOM-020 — Core Path Door

| Field | Value |
|---|---|
| Event Name | EVT-HOM-020 Core Path Door |
| Screen / Map | SCR-HOM-SND-002 / DGN_SealedNode_CorePath |
| Standard | ATLAS-TEC-054 section 3.5 |
| Trigger | Action Button or Player Touch |
| Priority | Same as Characters or Below Characters |
| Page Count | 2 |
| Switches | `J1_CorePath_DoorOpened` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_CorePath_DoorOpened` OFF | Comment `ATLAS EVT-HOM-020`; Play SE door/access placeholder; Control Switch `J1_CorePath_DoorOpened = ON`; Transfer or open local route | Door opens |
| 2 | `J1_CorePath_DoorOpened` ON | Route remains passable or transfers forward | Door stays open |

### EVT-HOM-021 — Node Seven Guardian

| Field | Value |
|---|---|
| Event Name | EVT-HOM-021 Node Seven Guardian |
| Screen / Map | SCR-HOM-SND-003 / DGN_SealedNode_Guardian |
| Standard | ATLAS-TEC-054 section 3.10 |
| Trigger | Action Button or Player Touch |
| Priority | Same as Characters |
| Page Count | 2 |
| Switches | `J1_Node07_GuardianDefeated` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_Node07_GuardianDefeated` OFF | Comment `ATLAS EVT-HOM-021 BOS-N07-001`; Show Text minimal warning placeholder; Battle Processing approved Node Seven Guardian troop; If Win: Control Switch `J1_Node07_GuardianDefeated = ON`; If Lose: Game Over or recover to safe point, per implementation test policy | Guardian defeated switch ON |
| 2 | `J1_Node07_GuardianDefeated` ON | Boss graphic gone or inactive; route to relay core available through `TRN-HOM-023` | Boss does not respawn |

### EVT-HOM-022 — Relay Core

| Field | Value |
|---|---|
| Event Name | EVT-HOM-022 Relay Core |
| Screen / Map | SCR-HOM-SND-004 / DGN_SealedNode_RelayCore |
| Standard | ATLAS-TEC-054 section 3.8 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 3 |
| Switches | `J1_Node07_GuardianDefeated`, `J1_Node07_Offline`, `J1_Mainland_TravelUnlocked`, `NPC_Ashford_PostNode07` |
| Variables | `Archive_Recovery_Percent = 5`, `Current_Relay_Count = 1` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_Node07_GuardianDefeated` OFF | Show Text `The core does not respond.` | No state change |
| 2 | Guardian defeated ON and `J1_Node07_Offline` OFF | Comment `ATLAS EVT-HOM-022 relay shutdown`; Play SE `SFX-HOM-006` placeholder; optional Flash/Fade; Show Text `NODE SEVEN: OFFLINE`; Control Switch `J1_Node07_Offline = ON`; Control Switch `J1_Mainland_TravelUnlocked = ON`; Control Switch `NPC_Ashford_PostNode07 = ON`; Control Variable `Archive_Recovery_Percent = 5`; Control Variable `Current_Relay_Count = 1` | Node Seven resolved |
| 3 | `J1_Node07_Offline` ON | Show Text `ARCHIVE RECOVERY: 5%` or no command | No repeat |

---

## Rustshore Event Specs

### EVT-HOM-023 — Dockmaster

| Field | Value |
|---|---|
| Event Name | EVT-HOM-023 Dockmaster |
| Screen / Map | SCR-HOM-RST-001 / TWN_Rustshore_Docks |
| Standard | ATLAS-TEC-054 section 3.4 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 2 |
| Switches | `J1_Mainland_TravelUnlocked` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_Mainland_TravelUnlocked` OFF | Comment `ATLAS EVT-HOM-023 locked`; Show Text `PH-DLG-DOCKMASTER-LOCKED` | Travel remains blocked |
| 2 | `J1_Mainland_TravelUnlocked` ON | Comment `ATLAS EVT-HOM-023 unlocked`; Show Text `PH-DLG-DOCKMASTER-UNLOCKED`; optionally direct player to boat event | Player understands travel is available |

### EVT-HOM-024 — Lighthouse Examine

| Field | Value |
|---|---|
| Event Name | EVT-HOM-024 Lighthouse Examine |
| Screen / Map | SCR-HOM-RST-001 / TWN_Rustshore_Docks |
| Standard | ATLAS-TEC-054 section 3.4 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 2 |
| Self Switches | Self Switch A optional |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | Self Switch A OFF | Comment `ATLAS EVT-HOM-024 ATLAS-TEC-052`; Play SE `SFX-HOM-007` placeholder; Show Text subtle lighthouse signal placeholder; Control Self Switch A = ON | Flavor examined |
| 2 | Self Switch A ON | Show Text shorter repeated lighthouse placeholder | Repeat interaction safe |

### EVT-HOM-025 — Boat Transfer

| Field | Value |
|---|---|
| Event Name | EVT-HOM-025 Boat Transfer |
| Screen / Map | SCR-HOM-RST-001 / TWN_Rustshore_Docks |
| Standard | ATLAS-TEC-054 sections 3.5 and 3.8 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 2 |
| Switches | `J1_Mainland_TravelUnlocked` |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | `J1_Mainland_TravelUnlocked` OFF | Comment `ATLAS EVT-HOM-025 locked`; Show Text `PH-DLG-DOCKMASTER-LOCKED` | No transfer |
| 2 | `J1_Mainland_TravelUnlocked` ON | Comment `ATLAS EVT-HOM-025 TRN-HOM-025`; Show Choices `Depart / Stay`; Depart: Fadeout, Transfer Player `CUT_Mainland_Departure`, Fadein; Stay: no command | Player chooses departure or remains |

### EVT-HOM-026 — Departure Sequence

| Field | Value |
|---|---|
| Event Name | EVT-HOM-026 Departure Sequence |
| Screen / Map | SCR-HOM-RST-002 / CUT_Mainland_Departure |
| Standard | ATLAS-TEC-054 section 3.8 |
| Trigger | Autorun |
| Priority | Same as Characters |
| Page Count | 2 |
| Variables | `Current_Journey = 2` |
| Self Switches | Self Switch A |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | Self Switch A OFF | Comment `ATLAS EVT-HOM-026 TRN-HOM-026`; Fadeout; Control Variable `Current_Journey = 2`; Show Text short departure placeholder; Transfer Player Journey II placeholder or future Coalmouth entry; Control Self Switch A = ON if remaining on this map | Journey II starts |
| 2 | Self Switch A ON | No autorun commands | No loop |

---

## Optional Fogfen Event Specs

### EVT-HOM-027 and EVT-HOM-030 — Fogfen Transfer Events

Use the transfer specs for `TRN-HOM-027`, `TRN-HOM-028`, `TRN-HOM-029`, and `TRN-HOM-030`.

Completion condition: player can enter Fogfen, reach the deeper pocket, return to the field, and return to Ashford route.

### EVT-HOM-028 — Fogfen Hidden Item Landmark

| Field | Value |
|---|---|
| Event Name | OBJ-HOM-FOG-005 Hidden Item Landmark |
| Screen / Map | SCR-HOM-FOG-001 / FLD_Fogfen_Marsh_Field |
| Standard | ATLAS-TEC-054 section 3.6 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 2 |
| Self Switches | Self Switch A |

Pages:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | Self Switch A OFF | Comment `ATLAS EVT-HOM-028 OBJ-HOM-FOG-005`; Play SE `Item`; Change Items approved early-game reward +1; Show Text `Found an item.`; Control Self Switch A = ON | Reward collected once |
| 2 | Self Switch A ON | Show Text `Nothing else is hidden here.` or no command | No repeat |

### EVT-HOM-029 and EVT-HOM-031 — Fogfen Signal Examine Events

| Event ID | Event Name | Screen / Map | Trigger | Priority | Pages | Commands | Completion |
|---|---|---|---|---|---:|---|---|
| EVT-HOM-029 | OBJ-HOM-FOG-003 Signal-Tick Reed Pool | SCR-HOM-FOG-001 / FLD_Fogfen_Marsh_Field | Action Button | Same as Characters | 2 | Page 1 Self Switch A OFF: Play SE subtle hum placeholder, Show Text `PH-DLG-SIGNAL-CLUE`, Self Switch A ON; Page 2 shorter repeat text | Clue examined |
| EVT-HOM-031 | OBJ-HOM-FOG-008 Signal Pool / Cable Cluster Examine | SCR-HOM-FOG-002 / FLD_Fogfen_Deeper_Marsh_Pocket | Action Button | Same as Characters | 2 | Page 1 Self Switch A OFF: Play SE subtle hum placeholder, Show Text `PH-DLG-SIGNAL-CLUE`, Self Switch A ON; Page 2 shorter repeat text | Clue examined |

No critical-path switch may depend on these events.

---

## Save / Recovery Point Spec

Home Island does not require a save point to clear the current vertical slice, but implementation may add one without inventing new lore if it follows `ATLAS-TEC-054` section 3.11 and `ATLAS-TEC-052`.

| Field | Value |
|---|---|
| Event Name | EVT-HOM-SAVE-001 Archive Shrine Save Point |
| Screen / Map | Preferred: SCR-HOM-ASH-001 or SCR-HOM-HCV-001 |
| Trigger | Action Button |
| Priority | Same as Characters |
| Page Count | 1 |
| Switches | None |
| Variables | None unless `CE_SaveShrine_ArchiveSync` later requires one |

Page:

| Page | Condition | Commands | Completion |
|---|---|---|---|
| 1 | None | Comment `ATLAS EVT-HOM-SAVE-001`; Show Text approved save placeholder; optional Recover All if packet allows; Save Processing; optional call `CE_SaveShrine_ArchiveSync` | Save menu closes |

This event must not advance story state.

---

## Event Categories Completed

| Category | Status |
|---|---|
| Map transfers | Complete for TRN-HOM-001 through TRN-HOM-030 |
| Treasure / collectibles | Complete for Ashford and Fogfen required hidden items |
| Save / recovery point | Optional executable pattern defined |
| Core NPC interactions | Complete for Elara, Ashford placeholder NPCs, Shopkeeper, Dockmaster |
| Trial entry / exit events | Complete with executable Body, Mind, and Heart mechanics from `ATLAS-TEC-057` |
| Required story gates | Complete for Skyreach, Sanctum, Glassfield, Guardian, Relay, Rustshore |
| Optional Fogfen events | Complete for transfers, hidden item, and signal clues |

---

## Remaining Event-Spec Gaps

The event-page blocker from `ATLAS-TEC-053` is cleared for the current Home Island vertical slice at the Atlas specification level.

Remaining gaps are not event-page specification blockers:

| Gap | Why It Remains |
|---|---|
| Final Body / Mind / Heart polish | `ATLAS-TEC-057` clears first-playable mechanics; final dialogue and presentation polish remain non-blocking |
| Combat balance tuning | `ATLAS-TEC-056` clears first-playable combat rows; final numeric tuning remains non-blocking |
| Tileset assignments | Tracked separately as the Asset Mapping blocker |
| Final animation polish | `ATLAS-TEC-060` clears first-playable animation IDs; custom VFX remain non-blocking polish |
| Final dialogue | Placeholder dialogue is allowed for first implementation |

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
| 0.1 | Initial executable Home Island event specs |
| 0.2 | Linked executable trial mechanics from ATLAS-TEC-057 |
