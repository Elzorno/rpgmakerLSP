---
atlas_id: ATLAS-TEC-058
title: RPG Maker MZ Vertical Slice Build Pipeline
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-010
  - ATLAS-TEC-020
  - ATLAS-TEC-040
  - ATLAS-TEC-041
  - ATLAS-TEC-042
  - ATLAS-TEC-052
  - ATLAS-TEC-053
  - ATLAS-TEC-054
  - ATLAS-TEC-055
  - ATLAS-TEC-056
  - ATLAS-TEC-057
  - ATLAS-TEC-059
  - ATLAS-TEC-060
related:
  - IMP-HOM-009
  - ATLAS-AUD-010
  - ATLAS-ART-010
  - ATLAS-ART-011
---

# RPG Maker MZ Vertical Slice Build Pipeline

## Objective

Define the implementation pipeline that maps Atlas artifacts directly to RPG Maker MZ project resources for the Home Island vertical slice.

This document does not implement the game. It is the translation layer a developer or implementation agent should use before editing RPG Maker MZ project files.

---

## Source Documents

| ID | Source | Role |
|---|---|---|
| `ATLAS-TEC-010` | Atlas Concordance | Visible fantasy to hidden reality to implementation mapping |
| `ATLAS-TEC-020` | RPG Maker MZ Bible | RPG Maker naming, database, event, and asset standards |
| `ATLAS-TEC-040` | Home Island Screen Registry | Canonical screen and map inventory |
| `ATLAS-TEC-041` | Home Island Transfer Registry | Canonical transfer graph |
| `ATLAS-TEC-042` | Home Island Event Registry | Canonical event inventory |
| `ATLAS-TEC-052` | Truth Layer Diagram | Story, gameplay, hidden truth, and implementation layer alignment |
| `ATLAS-TEC-053` | Home Island Vertical Slice Readiness Review | Current blocker list and readiness criteria |
| `ATLAS-TEC-054` | RPG Maker Event Specification Standard | Reusable event page standard |
| `ATLAS-TEC-055` | Home Island Executable Event Specs | RPG Maker-ready Home Island event pages |
| `ATLAS-TEC-056` | Home Island Combat Database Spec | RPG Maker-ready combat database rows |
| `ATLAS-TEC-057` | Home Island Body Mind Heart Trial Mechanics Spec | RPG Maker-ready trial mechanics |
| `ATLAS-TEC-059` | Home Island Tileset Assignment Matrix | RPG Maker-ready placeholder tileset, passability, and region guidance |
| `ATLAS-TEC-060` | Home Island Animation Assignment Matrix | RPG Maker-ready placeholder animation assignments |
| `IMP-HOM-009` | Home Island Sprint Assembly | Existing implementation packet ordering |

---

## Translation Rule

Build from Atlas identity outward.

Implementation files may use RPG Maker map IDs, event numbers, and database row numbers, but implementation reports and comments should cite Atlas IDs first.

Recommended event comment pattern:

```text
ATLAS <Atlas ID> <purpose>
```

Examples:

```text
ATLAS TRN-HOM-013 Sanctum gate transfer
ATLAS EVT-HOM-021 Node Seven Guardian battle
ATLAS MON-GEL-002 Marsh Gel database row
```

---

## Atlas To RPG Maker Translation Layer

| Atlas Artifact | RPG Maker MZ Target | Primary Atlas Source | Implementation Rule |
|---|---|---|---|
| Region | Map grouping, folder/order convention, implementation milestone | Region docs, `ATLAS-TEC-040` | Use region/screen IDs for reporting even when RPG Maker only stores map IDs |
| Location | Map group, BGM/BGS assignment group, asset folder | Location docs, `ATLAS-AUD-010`, `IMP-HOM-007` | Use location as production grouping, not a single RPG Maker object |
| Screen | Map | `ATLAS-TEC-040` | Create one RPG Maker map for each listed `SCR-HOM-*` unless an implementation packet explicitly combines maps |
| Screen object | Map event | Screen object docs, `ATLAS-TEC-042` | Name important events with Atlas IDs; use self switches only for local object state |
| NPC | Event with story-state pages | `ATLAS-TEC-042`, `ATLAS-TEC-055` | Follow `ATLAS-TEC-054` section 3.4; use pages instead of deep one-page branching |
| Story trigger | Autorun, Player Touch, Action Button, or conditional event page | `ATLAS-TEC-055` | Use the trigger and page conditions from the executable event specs |
| Dialogue ID or placeholder | Show Text command | `ATLAS-TEC-055`, dialogue packets | Use placeholder IDs until final lines are approved |
| Transfer | Transfer Player event | `ATLAS-TEC-041`, `ATLAS-TEC-055` | Each transfer event should map to one `TRN-HOM-*` ID |
| Trial | Event pages plus optional common events | `ATLAS-TEC-057` | Build Body, Mind, and Heart exactly from the trial spec; common events are optional helpers |
| Quest state | Switch and variable chain | `IMP-HOM-002`, quest docs | Use canonical Journey I switch and variable names |
| Enemy | Enemy database row | `ATLAS-TEC-056`, monster docs | Use stable enemy IDs from `ATLAS-TEC-056` |
| Troop | Troop database row | `ATLAS-TEC-056` | Use troop IDs and compositions from the combat spec |
| Skill | Skill database row | `ATLAS-TEC-056` | Use formulas, effects, and placeholder animation policy from the combat spec |
| Item | Item database row | `ATLAS-TEC-056` | Use item IDs and effects from the combat spec |
| Key item | Item database key-item row | `ATLAS-TEC-056`, `ATLAS-TEC-052` | The Sword can be represented as key item plus weapon row |
| Weapon | Weapon database row | `ATLAS-TEC-056` | Use Practice Sword and Sword rows from the combat spec |
| Armor | Armor database row | `ATLAS-TEC-056` | Use Plain Clothes starter row from the combat spec |
| State | State database row | `ATLAS-TEC-056` | Use Signal-Slick, Pulse Guard, and Charging rows as specified |
| Animation reference | Animation database row | `ATLAS-TEC-060` | Use approved placeholder animation IDs for first playable; final VFX remains polish |
| Tileset assignment | Tileset database row and map tileset setting | `ATLAS-TEC-059`, `IMP-HOM-007` | Use approved placeholder tilesets for first playable; final tiles remain polish |
| Region definition | Region IDs painted on maps | `ATLAS-TEC-059`, `ATLAS-TEC-056` | Use matrix region IDs only where encounter or hazard marking is needed |
| Encounter zone | Map encounter table, region ID, or evented battle | `ATLAS-TEC-056` | Use first-pass encounter placement from the combat spec |
| Audio cue | BGM/BGS/SE settings and event commands | `ATLAS-AUD-010`, `IMP-HOM-008` | Use placeholder files by approved cue names until final assets exist |
| Battler prompt | Enemy battler image | `ATLAS-ART-010` | Use placeholder battlers if final generated assets are not ready |
| Location art prompt | Tileset, parallax, and mapping reference | `IMP-HOM-007`, `ATLAS-ART-011` | Use placeholders until tile/parallax assets are assigned |

---

## Build Order

This order is for Home Island first playable implementation using approved placeholder tilesets and animations.

| Stage | Build Step | Atlas Dependencies | Output |
|---:|---|---|---|
| 1 | Create or verify Journey I switches and variables | `IMP-HOM-002`, `ATLAS-TEC-054`, `ATLAS-TEC-057` | Switches and variables available to all events |
| 2 | Populate core database rows | `ATLAS-TEC-020`, `ATLAS-TEC-056` | Actor, class, item, weapon, armor, skill, state, enemy, and troop rows |
| 3 | Configure system settings | `ATLAS-TEC-020`, `ATLAS-TEC-056` | Starting party, side-view/default battle assumptions, test battle readiness |
| 4 | Configure tilesets | `ATLAS-TEC-059`, `IMP-HOM-007` | Placeholder tileset database rows and map tileset assignments |
| 5 | Create Home Island maps | `ATLAS-TEC-040`, screen docs, implementation packets | RPG Maker maps named from registry map names |
| 6 | Paint passability and region data | `ATLAS-TEC-059`, screen docs, encounter placement from `ATLAS-TEC-056` | Traversable maps, blocked edges, optional encounter regions |
| 7 | Add transfer events | `ATLAS-TEC-041`, `ATLAS-TEC-055` | Working transfer graph from Ashford through Rustshore and optional Fogfen |
| 8 | Add player start and state bootstrap | `ATLAS-TEC-055`, `IMP-HOM-002` | New game starts in Elara House with initial state set |
| 9 | Add NPC and shop events | `ATLAS-TEC-042`, `ATLAS-TEC-054`, `ATLAS-TEC-055`, dialogue packets | NPC pages, shop placeholder, story-state dialogue pages |
| 10 | Add treasure, examine, save, and recovery events | `ATLAS-TEC-042`, `ATLAS-TEC-055` | Self-switch rewards, optional save/recovery point |
| 11 | Add story gates and cutscene triggers | `ATLAS-TEC-055`, quest docs | Tremor, Skyreach gate, Sword pedestal, Glassfield seal, relay resolution |
| 12 | Add trial mechanics | `ATLAS-TEC-057`, `ATLAS-TEC-055` | Body, Mind, and Heart trials playable without softlocks |
| 13 | Add encounters and boss battle | `ATLAS-TEC-056`, `ATLAS-TEC-055` | Map encounters and Node Seven Guardian battle flow |
| 14 | Add audio hooks | `ATLAS-AUD-010`, `IMP-HOM-008` | Placeholder BGM/BGS/SE commands assigned |
| 15 | Add animation references | `ATLAS-TEC-060`, `ATLAS-TEC-053` | Story, trial, feedback, item, and combat animations assigned |
| 16 | Full vertical slice playtest | `ATLAS-TEC-053`, playtest checklist | Verified playable route from new game to mainland travel unlock |
| 17 | Implementation report | `ATLAS-TEC-001`, `ATLAS-TEC-053` | Files changed, Atlas IDs implemented, blockers, validation result |

Home Island has no remaining Atlas readiness blockers after `ATLAS-TEC-060`; final art/VFX polish remains separate from first playable readiness.

---

## Database Population Order

Populate databases before map events that reference them.

| Order | Database Area | Atlas Source | Notes |
|---:|---|---|---|
| 1 | Actors | `ATLAS-TEC-056`, `CHR-KAI-001` | Actor 1 Kai |
| 2 | Classes | `ATLAS-TEC-056` | Class 1 Sword Bearer |
| 3 | Items and Key Items | `ATLAS-TEC-056`, `ATLAS-TEC-052` | Potion and Sword key item rows |
| 4 | Weapons | `ATLAS-TEC-056` | Practice Sword and Sword rows |
| 5 | Armor | `ATLAS-TEC-056` | Plain Clothes starter row |
| 6 | States | `ATLAS-TEC-056` | Knockout default plus Signal-Slick, Pulse Guard, Charging |
| 7 | Skills | `ATLAS-TEC-056` | Enemy skills and default Attack assumptions |
| 8 | Enemies | `ATLAS-TEC-056`, monster docs | Meadow Gel, Ash Rat, Marsh Gel, Node Seven Guardian |
| 9 | Troops | `ATLAS-TEC-056` | Field, Fogfen, and Node Boss troops |
| 10 | Animations | `ATLAS-TEC-060` | Placeholder assignments are ready for first playable testing |
| 11 | Tilesets | `ATLAS-TEC-059` | Placeholder assignments are ready for first playable testing |
| 12 | System settings | `ATLAS-TEC-020`, `ATLAS-TEC-056` | Starting party, battle mode assumptions, test targets |

---

## Event Build Pipeline

Use `ATLAS-TEC-054` for event standards and `ATLAS-TEC-055` for Home Island event pages.

| Order | Event Category | Atlas Source | Build Notes |
|---:|---|---|---|
| 1 | Transfers | `ATLAS-TEC-041`, `ATLAS-TEC-055` | Build open transfers first, then gated transfers |
| 2 | Player start | `ATLAS-TEC-055`, `IMP-HOM-002` | Establish Journey I variables and opening switch |
| 3 | NPC interactions | `ATLAS-TEC-042`, `ATLAS-TEC-055` | Use story-state pages and placeholder dialogue IDs |
| 4 | Treasure and collectibles | `ATLAS-TEC-042`, `ATLAS-TEC-055` | Use Self Switch A for collected state |
| 5 | Shops | `ATLAS-TEC-054`, `ATLAS-TEC-055` | Implement Ashford shop with placeholder inventory until economy spec expands |
| 6 | Inns and recovery | `ATLAS-TEC-054`, Gameplay Systems Bible | No required inn blocker; Elara House or save/recovery point can cover first pass if specified |
| 7 | Save points | `ATLAS-TEC-054`, `ATLAS-TEC-055` | Optional executable save/recovery pattern exists |
| 8 | Story gates | `ATLAS-TEC-055`, quest docs | Skyreach, Sanctum, Glassfield, Guardian, Rustshore gates |
| 9 | Trial events | `ATLAS-TEC-057`, `ATLAS-TEC-055` | Body, Mind, Heart, and Sanctum gate |
| 10 | Cutscenes | `ATLAS-TEC-054`, `ATLAS-TEC-055` | Keep short and switch-driven; final dialogue is not required for first pass |
| 11 | Boss encounters | `ATLAS-TEC-056`, `ATLAS-TEC-055` | Node Seven Guardian troop and defeat branch |
| 12 | Relay resolution | `ATLAS-TEC-055`, `ATLAS-TEC-052` | Archive variable, Node Seven offline, mainland travel unlock |

Event implementation reports must list the Atlas event IDs completed, not RPG Maker event numbers.

---

## Map Build Pipeline

| Order | Map Group | Registry Source | Implementation Packets |
|---:|---|---|---|
| 1 | Ashford | `ATLAS-TEC-040` | `IMP-HOM-010`, `IMP-HOM-001`, `IMP-HOM-006` |
| 2 | Skyreach and Hidden Cave | `ATLAS-TEC-040` | `IMP-HOM-011`, `IMP-HOM-003` |
| 3 | Glassfield and Sealed Node | `ATLAS-TEC-040` | `IMP-HOM-012`, `IMP-HOM-004` |
| 4 | Rustshore departure | `ATLAS-TEC-040` | `IMP-HOM-013`, `IMP-HOM-014` |
| 5 | Optional Fogfen branch | `ATLAS-TEC-040` | `IMP-HOM-015` |
| 6 | Home Island route links | `ATLAS-TEC-041` | `IMP-HOM-016` |

Every implemented map should be checked against:

- map name in `ATLAS-TEC-040`,
- transfer IDs in `ATLAS-TEC-041`,
- events in `ATLAS-TEC-042`,
- executable pages in `ATLAS-TEC-055`.

---

## Asset Dependency Matrix

| Asset Type | Depends On | Blocks First Playable? | Placeholder Policy | Atlas Source |
|---|---|---:|---|---|
| Tilesets | Tileset assignment matrix, location art pipeline | No | Use approved RTP/prototype tilesets from `ATLAS-TEC-059`; final custom tiles are polish | `ATLAS-TEC-059`, `IMP-HOM-007` |
| Character sprites | NPC roster, event registry, screen docs | No | Use RPG Maker placeholder sprites if event identity is named | `ATLAS-TEC-042`, character docs |
| Face graphics | Dialogue packets and NPC specs | No | Omit or use placeholder faces; final dialogue is not blocked | Dialogue packets, `ATLAS-TEC-055` |
| Enemy sprites | Enemy database, battler prompt packet | No | Use placeholder battlers if row IDs are stable | `ATLAS-TEC-056`, `ATLAS-ART-010` |
| Animations | Animation assignment matrix | No | Use approved RTP/prototype animations from `ATLAS-TEC-060`; final custom VFX are polish | `ATLAS-TEC-060` |
| Audio music | Location audio cue packet | No | Use placeholder BGM names from audio packet | `ATLAS-AUD-010`, `IMP-HOM-008` |
| Sound effects | Event specs and audio cue packet | No | Use placeholder SE hooks; avoid missing-file crashes | `ATLAS-AUD-010`, `ATLAS-TEC-055` |
| Battlebacks | Map group, encounter location, tileset/art direction | No | Use default or placeholder battlebacks for first tests | `ATLAS-TEC-056`, `IMP-HOM-007` |
| Parallax assets | Location art pipeline | No | Not required for first playable unless a future packet mandates parallax mapping | `IMP-HOM-007` |

Current blocking asset dependencies:

- None for first playable testing.

---

## Placeholder Rules

Allowed placeholders:

- final dialogue,
- NPC sprites,
- face graphics,
- battlers,
- BGM/BGS,
- sound effects,
- battlebacks,
- parallax references,
- balance tuning values after first-pass rows exist.

Not allowed as vague placeholders:

- Atlas IDs,
- map names listed in the screen registry,
- switch names,
- variable names,
- transfer IDs,
- event names for story-critical events,
- enemy/troop/skill/state IDs already defined in `ATLAS-TEC-056`,
- trial variables and trial switch behavior from `ATLAS-TEC-057`.

---

## Verification Checklist

### Atlas Preflight

- [ ] Run `/usr/bin/python3 atlas-tools/cli/atlas.py validate`.
- [ ] Confirm validation returns 0 errors and 0 warnings.
- [ ] Confirm `ATLAS-TEC-053` has no unresolved blocker except known active blockers for the current work pass.

### Database

- [ ] Actor 1 Kai exists.
- [ ] Class 1 Sword Bearer exists.
- [ ] Potion, Sword key item, Practice Sword, Sword weapon, and Plain Clothes exist.
- [ ] Signal-Slick, Pulse Guard, and Charging states exist.
- [ ] Skills 101, 102, 110, 111, 112, and 113 exist.
- [ ] Enemies 1, 2, 3, and 10 exist.
- [ ] Troops 1, 2, 3, 4, 5, and 10 exist.

### Maps And Transfers

- [ ] Every screen in `ATLAS-TEC-040` has a corresponding RPG Maker map or documented intentional exception.
- [ ] Every required transfer in `ATLAS-TEC-041` works in both intended directions.
- [ ] Gated transfers respect their switches.
- [ ] No transfer strands the player unless the registry marks it as a deliberate cutscene transition.

### Events

- [ ] Every event in `ATLAS-TEC-042` exists or is documented as intentionally deferred.
- [ ] Event pages follow `ATLAS-TEC-054`.
- [ ] Home Island event command sequences match `ATLAS-TEC-055`.
- [ ] Body, Mind, and Heart trials match `ATLAS-TEC-057`.
- [ ] Treasure and hidden items use self-switches and cannot be collected repeatedly.
- [ ] NPC pages change by story state where required.
- [ ] Shop, save, recovery, boss, and relay events do not softlock the player.

### Encounters

- [ ] Field and Fogfen encounter troops can be tested.
- [ ] Node Seven Guardian battle starts from the event spec.
- [ ] Boss defeat sets `J1_Node07_GuardianDefeated`.
- [ ] Relay core is unreachable until guardian defeat.

### Assets

- [ ] Tileset assignments are present once the tileset matrix exists.
- [ ] Animation IDs from `ATLAS-TEC-060` are present for required combat, story, trial, feedback, and recovery beats.
- [ ] Placeholder sprites, battlers, battlebacks, BGM, BGS, and SE files are present or omitted safely.
- [ ] No event references a missing required asset file.

### Story Progression

- [ ] New game starts in Elara House.
- [ ] Tremor opens Skyreach access.
- [ ] Hidden Cave entry sets `J1_HiddenCave_Entered`.
- [ ] All three trial switches can turn ON.
- [ ] Sword pedestal grants Sword state and sets `Archive_Recovery_Percent = 3`.
- [ ] Glassfield seal opens only after Sword acquisition.
- [ ] Node Seven shutdown sets archive recovery and mainland travel state.
- [ ] Rustshore departure can advance to the Journey II placeholder.

### Save And Load

- [ ] Saving is possible at the approved point or via debug during first implementation testing.
- [ ] Loading preserves Journey I switches and variables.
- [ ] Loading after Sword acquisition, Guardian defeat, and Node Seven shutdown does not break transfer or event pages.

---

## Remaining Implementation Blockers

Per `ATLAS-TEC-053`, Home Island is build-ready from Atlas alone for first playable testing.

Final custom tilesets, animations, audio, sprites, battlers, dialogue polish, and balance tuning remain non-blocking production polish unless a later work order changes the target from first playable to final asset production.

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
| 0.1 | Initial RPG Maker MZ vertical slice build pipeline |
