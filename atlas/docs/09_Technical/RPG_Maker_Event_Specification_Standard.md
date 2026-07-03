---
atlas_id: ATLAS-TEC-054
title: RPG Maker Event Specification Standard
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-001
  - ATLAS-TEC-020
related:
  - ATLAS-TEC-053
---

# RPG Maker Event Specification Standard

## Purpose

This standard defines how Atlas event requirements become RPG Maker MZ event pages.

Implementation packets should reference this document instead of redefining common event logic.

Example:

```text
Build this NPC using ATLAS-TEC-054 section 3.4.
```

---

## 1. Event Identity

### 1.1 Event Naming Convention

Every important RPG Maker map event should use a readable name that starts with its Atlas event ID when one exists.

Format:

```text
EVT-HOM-009 Tremor Trigger
TRN-HOM-005 To Skyreach
OBJ-HOM-FOG-005 Hidden Item Landmark
NPC-ELA-001 Elara
```

If no Atlas ID exists yet, use a temporary implementation name with `TMP_`:

```text
TMP_Debug_Return
TMP_Blocker_Message
```

Temporary events must not be used for story-critical logic unless the implementation report lists them as follow-up work.

### 1.2 Event ID Policy

Use Atlas IDs for design identity and RPG Maker event numbers only for engine placement.

Rules:

1. Atlas event IDs remain stable.
2. RPG Maker event numbers may change.
3. Implementation reports must cite Atlas IDs, not RPG Maker event numbers.
4. Every critical-path event must appear in the appropriate event registry.
5. Optional flavor events need Atlas IDs only when they touch switches, variables, rewards, combat, memory fragments, or permanent state.

---

## 2. State Usage

### 2.1 Self Switch Usage

Use self switches for local event state only.

Allowed uses:

| Self Switch | Standard Use |
|---|---|
| A | Collected, completed, opened, or exhausted local event |
| B | Alternate local state, such as examined once but not resolved |
| C | Local puzzle step only when it does not affect another event |
| D | Reserved for local fallback or debug reset during prototype work |

Do not use self switches for:

- story progression,
- route gates,
- quest completion,
- boss defeat that affects another screen,
- NPC dialogue state shared across maps.

### 2.2 Global Switch Usage

Use global switches for world, story, route, quest, and shared NPC state.

Required format:

```text
J1_Sword_Obtained
J1_Node07_Offline
NPC_Ashford_PostNode07
SYS_ProtocolSkills_Unlocked
```

Rules:

1. Name switches before implementation.
2. Add every story-critical switch to a traceability document.
3. Use positive names when possible.
4. Do not create vague names such as `Door Open`, `Boss Dead`, or `Switch 42`.
5. A switch with multiple setters must be documented.

### 2.3 Variable Ranges

Use variables for values that can change repeatedly or be compared.

Project-level variable ranges:

| Range | Use |
|---|---|
| 1-20 | Global story variables |
| 21-40 | Journey progress variables |
| 41-80 | Gameplay system variables |
| 81-120 | Puzzle and dungeon variables |
| 121-160 | NPC or relationship variables |
| 161-200 | Debug and temporary implementation variables |

Important variables should use readable names:

```text
Current_Journey
Archive_Recovery_Percent
Current_Relay_Count
```

Do not use variables for binary state when a switch is clearer.

### 2.4 Common Event Usage

Use common events for repeated logic.

Good common event candidates:

```text
CE_Archive_MessageDisplay
CE_Screen_FadeTransfer
CE_SaveShrine_ArchiveSync
CE_RelayNode_Shutdown
CE_Sword_AccessCheck
```

Rules:

1. Use common events when the same command pattern appears three or more times.
2. Keep common events small and named by purpose.
3. Avoid common events that depend on hidden map-specific assumptions.
4. Document required input switches, variables, or event context.

---

## 3. Event Page Rules

### 3.1 Page Ordering Rules

RPG Maker evaluates higher-numbered valid pages first.

Atlas event specs should list pages from lowest priority to highest priority, then clearly mark the RPG Maker page order.

Default order:

| Page | Use |
|---|---|
| Page 1 | Default / unresolved state |
| Page 2 | Progressed state |
| Page 3 | Completed state |
| Page 4+ | Special override, debug, or rare branch |

Rules:

1. Completed state pages should usually have the highest active page number.
2. A page with no condition must be Page 1 unless deliberately used as a fallback.
3. Do not leave critical events with only a blank highest-priority page.
4. If page order matters, the spec must say so.

### 3.2 Trigger Standards

| Trigger | Use |
|---|---|
| Action Button | NPCs, signs, treasure, doors, examine points, save points |
| Player Touch | transfers, hazards, route gates that activate on stepping |
| Event Touch | moving blockers or patrols |
| Autorun | cutscenes that must complete before player control returns |
| Parallel | ambient or repeated checks only when unavoidable |

Avoid parallel events unless there is no simpler switch or event-page solution.

### 3.3 Priority Standards

| Priority | Use |
|---|---|
| Below Characters | transfer tiles, floor triggers, pressure plates |
| Same as Characters | NPCs, signs, chests, doors, blockers, examine points |
| Above Characters | visual-only overhead elements |

### 3.4 NPC Conversation Standard

NPC events should use story-state pages rather than branching deeply inside one page.

Required NPC page pattern:

| RPG Maker Page | Condition | Trigger | Contents |
|---|---|---|---|
| 1 | None | Action Button | Intro/default dialogue |
| 2 | Mid-story switch | Action Button | Changed dialogue |
| 3 | Late-story switch | Action Button | Final or post-event dialogue |

Rules:

1. One event page should usually represent one story state.
2. Each page should start with a comment citing the Atlas ID and state.
3. NPCs should not set story-critical switches unless the implementation packet explicitly says so.
4. Use short message boxes.
5. If final dialogue is not ready, use approved placeholder lines from the relevant dialogue packet.

### 3.5 Transfer Event Standard

Transfer events should be simple, directional, and traceable to a transfer ID.

Required transfer page pattern:

| RPG Maker Page | Condition | Trigger | Priority | Contents |
|---|---|---|---|---|
| 1 | None or route open switch | Player Touch | Below Characters | Fade out, transfer player, fade in |
| 2 | Route locked switch or missing requirement | Player Touch or Action Button | Below/Same | Block message, no transfer |

Rules:

1. Every directional transfer needs a transfer ID.
2. Doorways normally need two transfer IDs: out and back.
3. Gated transfers must name the gate switch.
4. One-way transfers must be called out in the implementation packet.
5. Transfer events should not contain long cutscenes.

### 3.6 Treasure Chest Standard

Treasure events should use self switches unless the reward affects world state.

Required chest page pattern:

| RPG Maker Page | Condition | Trigger | Contents |
|---|---|---|---|
| 1 | Self Switch A OFF | Action Button | Play SE, change graphic/open, add item, show message, Self Switch A ON |
| 2 | Self Switch A ON | Action Button | Empty chest message or no message |

Rules:

1. Use Self Switch A for local collected state.
2. Use a global switch only for unique story items or quest items.
3. The item and quantity must be named in the event spec.
4. Hidden treasure should still have an Atlas object ID when it is required by a packet.

### 3.7 Shop Event Standard

Shop events should be NPC conversation events with a shop branch.

Required shop page pattern:

| RPG Maker Page | Condition | Trigger | Contents |
|---|---|---|---|
| 1 | None | Action Button | Greeting, choice, Shop Processing, farewell |
| 2 | Later story state if needed | Action Button | Updated greeting, same shop or changed shop |

Rules:

1. The shop inventory must be listed in the screen or packet.
2. Shops should not silently change inventory unless tied to a documented state.
3. If economy data is not ready, use a placeholder message instead of inventing permanent stock.

### 3.8 Cutscene Event Standard

Cutscenes should be short, switch-driven, and resumable after completion.

Required cutscene page pattern:

| RPG Maker Page | Condition | Trigger | Contents |
|---|---|---|---|
| 1 | Cutscene completion switch OFF | Autorun | Fade/move/dialogue/SFX/state updates/completion switch ON |
| 2 | Cutscene completion switch ON | Action Button or None | Inactive or post-cutscene interaction |

Rules:

1. Every autorun cutscene must turn on a completion switch or self switch.
2. Use comments before complex command blocks.
3. Keep long cutscenes split into small eventable beats.
4. Do not leave the player in an autorun loop.

### 3.9 Trial Event Standard

Trial events are reusable challenge patterns for Body, Mind, Heart, or later equivalent systems.

Required trial page pattern:

| RPG Maker Page | Condition | Trigger | Contents |
|---|---|---|---|
| 1 | Trial clear switch OFF | Action Button / Player Touch | Explain prompt, run challenge, set clear switch on success |
| 2 | Trial clear switch ON | Action Button | Completed message or inactive state |

Rules:

1. Each trial must name its success condition.
2. Each trial must state whether failure is possible.
3. Each trial must define reset behavior.
4. Trial completion should use global switches when it gates another event.
5. Trial text should be minimal unless a dialogue packet provides final writing.

### 3.10 Boss Event Standard

Boss events should separate pre-battle gate, battle processing, defeat state, and post-battle access.

Required boss page pattern:

| RPG Maker Page | Condition | Trigger | Contents |
|---|---|---|---|
| 1 | Boss defeated switch OFF | Action Button or Player Touch | Warning, Battle Processing, defeat branch sets boss switch |
| 2 | Boss defeated switch ON | Action Button or None | Boss gone, route open, post-battle text if needed |

Rules:

1. Every boss must have a boss defeated switch.
2. The troop ID must be specified.
3. Loss behavior must be specified.
4. Bosses must not respawn unless the packet explicitly says they do.
5. Any route unlocked by the boss must read the boss defeated switch.

### 3.11 Save Point Standard

Save points represent shrines, archive terminals, safe camps, or other Atlas-approved recovery points.

Required save point page pattern:

| RPG Maker Page | Condition | Trigger | Contents |
|---|---|---|---|
| 1 | None | Action Button | Optional message, optional recovery, Save Processing, optional archive sync |

Rules:

1. Save points should be interactable, not automatic, unless a packet explicitly requires an autosave-like flow.
2. Recovery is optional and must be specified.
3. Archive-themed save points should call or mimic `CE_SaveShrine_ArchiveSync` when that common event exists.
4. Save points must not advance story state unless the packet says so.

---

## 4. Example Event Pages

### 4.1 Example Transfer Event

```text
Event Name: TRN-HOM-005 To Skyreach
Atlas IDs: TRN-HOM-005, EVT-HOM-010
Priority: Below Characters
Trigger: Player Touch

Page 1: Locked
Condition: J1_Skyreach_AccessOpen is OFF
Commands:
  - Comment: ATLAS TRN-HOM-005 locked route
  - Show Text: The north path is still blocked.

Page 2: Open
Condition: J1_Skyreach_AccessOpen is ON
Commands:
  - Comment: ATLAS TRN-HOM-005 transfer
  - Fadeout Screen
  - Transfer Player: DGN_SkyreachHill_Path
  - Fadein Screen
```

### 4.2 Example NPC Event

```text
Event Name: NPC-ELA-001 Elara
Atlas IDs: NPC-ELA-001, EVT-HOM-002
Priority: Same as Characters
Trigger: Action Button

Page 1: Intro
Condition: None
Commands:
  - Comment: ATLAS NPC-ELA-001 STATE_01_INTRO
  - Show Text: approved intro or placeholder line

Page 2: After Node Seven
Condition: NPC_Ashford_PostNode07 is ON
Commands:
  - Comment: ATLAS NPC-ELA-001 STATE_04_AFTER_NODE07
  - Show Text: approved post-node or placeholder line
```

### 4.3 Example Treasure Event

```text
Event Name: OBJ-HOM-FOG-005 Hidden Item Landmark
Atlas IDs: OBJ-HOM-FOG-005
Priority: Same as Characters
Trigger: Action Button

Page 1: Uncollected
Condition: Self Switch A is OFF
Commands:
  - Comment: ATLAS OBJ-HOM-FOG-005 reward
  - Play SE: Item
  - Change Items: Potion + 1
  - Show Text: Found a Potion.
  - Control Self Switch A = ON

Page 2: Collected
Condition: Self Switch A is ON
Commands:
  - Show Text: Nothing else is hidden here.
```

### 4.4 Example Shop Event

```text
Event Name: NPC-ASH-SHP-001 Shopkeeper
Atlas IDs: EVT-HOM-008
Priority: Same as Characters
Trigger: Action Button

Page 1: Default Shop
Condition: None
Commands:
  - Comment: ATLAS EVT-HOM-008 shop processing
  - Show Text: Take a look around.
  - Show Choices: Buy / Not now
  - When Buy:
      - Shop Processing: approved inventory list
  - When Not now:
      - Show Text: Travel safe.
```

### 4.5 Example Cutscene Event

```text
Event Name: EVT-HOM-009 Tremor Trigger
Atlas IDs: EVT-HOM-009
Priority: Same as Characters
Trigger: Autorun

Page 1: Tremor Not Played
Condition: J1_Tremor_Event is OFF
Commands:
  - Comment: ATLAS EVT-HOM-009 tremor sequence
  - Fadeout Screen
  - Play SE: SFX-HOM-002 placeholder
  - Screen Shake
  - Control Switch J1_Tremor_Event = ON
  - Control Switch J1_Skyreach_AccessOpen = ON
  - Fadein Screen

Page 2: Tremor Played
Condition: J1_Tremor_Event is ON
Commands:
  - Comment: Tremor complete; no autorun
```

### 4.6 Example Trial Event

```text
Event Name: EVT-HOM-012 Body Trial
Atlas IDs: EVT-HOM-012
Priority: Same as Characters
Trigger: Action Button

Page 1: Trial Incomplete
Condition: J1_Trial_Body_Clear is OFF
Commands:
  - Comment: ATLAS EVT-HOM-012 body trial
  - Run approved challenge
  - If success:
      - Control Switch J1_Trial_Body_Clear = ON
      - Show Text: Trial complete.
  - If failure:
      - Reset local trial state

Page 2: Trial Complete
Condition: J1_Trial_Body_Clear is ON
Commands:
  - Show Text: This trial is complete.
```

### 4.7 Example Boss Event

```text
Event Name: EVT-HOM-021 Node Seven Guardian
Atlas IDs: EVT-HOM-021, BOS-N07-001
Priority: Same as Characters
Trigger: Action Button or Player Touch

Page 1: Boss Active
Condition: J1_Node07_GuardianDefeated is OFF
Commands:
  - Comment: ATLAS EVT-HOM-021 guardian battle
  - Battle Processing: approved Node Seven Guardian troop
  - If Win:
      - Control Switch J1_Node07_GuardianDefeated = ON
  - If Lose:
      - Run approved loss behavior

Page 2: Boss Defeated
Condition: J1_Node07_GuardianDefeated is ON
Commands:
  - Comment: Guardian defeated; route to relay core is open
```

### 4.8 Example Save Point Event

```text
Event Name: CE_SaveShrine_ArchiveSync or local save shrine
Atlas IDs: save point object ID if assigned
Priority: Same as Characters
Trigger: Action Button

Page 1: Save Available
Condition: None
Commands:
  - Comment: ATLAS save point standard
  - Show Text: The shrine is quiet and steady.
  - Recover All: Party, if specified
  - Save Processing
```

---

## 5. Implementation Packet Citation Rules

Implementation packets should cite this standard by section.

Examples:

```text
Build all transfer events using ATLAS-TEC-054 section 3.5.
Build the shopkeeper using ATLAS-TEC-054 section 3.7.
Build the guardian encounter using ATLAS-TEC-054 section 3.10.
```

If a packet needs to deviate from this standard, it must say why.

---

## 6. Follow-On Priorities

This standard unblocks the next production layers in this order:

1. Combat database specification: actors, classes, enemies, troops, skills, states, animations, items, weapons, armor, and system settings.
2. Trial framework: repeatable Body, Mind, and Heart mechanics.
3. Asset mapping: tilesets, character sprites, animations, audio, and sound effects.

Do not assign final assets before the relevant gameplay system is stable enough to receive them.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial RPG Maker event specification standard |
