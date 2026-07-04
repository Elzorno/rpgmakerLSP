# WO-0021 - RPG Maker Clean Skeleton Strategy

## Decision

Recommendation: **GO clean skeleton / NO GO current project**.

Home Island implementation should continue in a clean RPG Maker MZ project skeleton that consumes the Atlas export. The current RPG Maker project should remain as legacy prototype/reference material until specific assets, plugins, or proven event patterns are intentionally migrated.

Next work order: **BUILD-0001 - Create Clean RPG Maker MZ Project Skeleton From Atlas Export**.

## Current Data Audit Summary

Source report:

```text
reports/atlas-import/home-island-data-readiness-audit.md
```

Audit totals:

| Status | Count |
|---|---:|
| Found | 21 |
| Missing | 17 |
| Present with warning | 38 |
| Not machine-checkable yet | 71 |
| Total findings | 147 |

Key audit results:

- Actor `1` is already `Kai`.
- All 16 Atlas Home Island map names are missing from `data/MapInfos.json`.
- Current `data/MapInfos.json` contains legacy/default maps such as `Castle`, `World 1`, `Village 1`, `House 2`, and `Stone Cave`.
- Atlas tileset placeholder names exist: `Outside`, `Inside`, `Dungeon`, `SF Outside`, and `SF Inside`.
- Atlas animation IDs are available for first playable testing, except the explicit `None` row that means no animation is required.
- Class, enemy, troop, state, item, weapon, and armor IDs expected by Atlas are mostly occupied by default or legacy rows.
- Transfers, Atlas events, trial state checks, and troop event pages are not machine-checkable yet because the current audit does not parse map event commands, switch ranges, variables, or common event command lists.

High-impact mismatches:

| Category | Atlas expectation | Current project state |
|---|---|---|
| Maps | 16 Home Island maps named from Atlas screen registry | 0 matching map names |
| Class | `Class 1 - Sword Bearer` | `Class 1 - Swordsman` |
| Enemies | IDs `1`, `2`, `3`, `10` reserved for Home Island enemies | Occupied by default/legacy enemies |
| Troops | IDs `1`-`5`, `10` reserved for Home Island troops | Occupied by default/legacy troops |
| Skills | IDs `101`, `102`, `110`-`113` reserved for Home Island enemy/boss skills | Occupied by default magic rows or blank rows |
| States | IDs `1`, `11`-`13` reserved for Home Island states | Occupied by default/legacy states |
| Items | `Item 1 - Potion`, `Key Item 201 - Sword / Project Excalibur` | Potion is at ID `7`; key item `201` is missing |
| Equipment | `Weapon 1`, `Weapon 2`, `Armor 1` reserved for Home Island | Occupied by default rows |

## Risks Of Using Current Project

### ID Collision Risk

Atlas now has explicit database expectations. The current project already uses many of those IDs for default or prototype rows, so implementing Atlas in place would require either destructive overwrites or a broad remapping layer. Both paths add avoidable risk before the vertical slice has a stable baseline.

### Map Identity Risk

Atlas names every Home Island screen. The current project has 32 maps, but none of the 16 Home Island map names are present. Reusing existing maps would require manual interpretation of which legacy map corresponds to which Atlas screen. That is exactly the kind of ambiguity the Atlas export/import split is supposed to remove.

### Event State Risk

The current `System.json` switch list contains legacy chamber and later-area switches such as `Chamber 1 Complete`, `Sword Obtained`, `Mine Authorized`, and `Broadcast Engine Defeated`. Atlas needs a clean Journey 1 state range so Home Island gates, trials, node resolution, and mainland departure can be audited deterministically.

### Prototype Contamination Risk

The current project contains useful prototype work, but it mixes default RPG Maker content, early implementation experiments, and Atlas-directed data. Continuing in place makes every automated importer more dangerous because it cannot easily distinguish intentional canon rows from old scaffolding.

### Auditability Risk

WO-0020 already shows many findings as warnings instead of simple found/missing rows because existing IDs are populated with different names. A clean skeleton turns future audits into direct comparisons: either the Atlas row exists at the reserved ID, or it does not.

## Clean Skeleton Requirements

BUILD-0001 should create or initialize a clean RPG Maker MZ project skeleton with these requirements:

- Preserve a valid RPG Maker MZ project structure and required base JSON files.
- Keep `data/*.json` minimal, parseable, and intentionally reserved for Atlas import.
- Do not copy legacy maps, troops, enemies, skills, switches, or variables into the skeleton by default.
- Include only required engine defaults plus Atlas-reserved rows.
- Preserve built-in RTP asset references where Atlas allows placeholders.
- Use Atlas export as the source of truth for Home Island maps, transfer expectations, database rows, tileset placeholders, and animation placeholders.
- Keep import/build tools read-only until a separate guarded writer work order defines backups, dry-run mode, and rollback behavior.
- Maintain the current project as `legacy/reference`, not as the active Atlas build target.

Minimum skeleton directories:

```text
data/
audio/
effects/
fonts/
icon/
img/
js/
movies/
save/
```

Minimum skeleton files:

```text
game.rmmzproject
data/Actors.json
data/Animations.json
data/Armors.json
data/Classes.json
data/CommonEvents.json
data/Enemies.json
data/Items.json
data/Map001.json
data/MapInfos.json
data/Skills.json
data/States.json
data/System.json
data/Tilesets.json
data/Troops.json
data/Weapons.json
js/plugins.js
```

## Database ID Reservation Plan

The clean skeleton should reserve the Atlas-exported Home Island database IDs exactly. This keeps implementation packets, event specs, combat specs, and audit tools aligned.

| Database | Reserved IDs | Required Home Island rows |
|---|---|---|
| Actors | `1` | `Kai` |
| Classes | `1` | `Sword Bearer` |
| Enemies | `1`-`3`, `10` | `Meadow Gel`, `Ash Rat`, `Marsh Gel`, `Node Seven Guardian` |
| Troops | `1`-`5`, `10` | `HOM Field 1`, `HOM Field 2`, `HOM Field 3`, `HOM Fogfen 1`, `HOM Fogfen 2`, `HOM Node Boss` |
| Skills | `1`, `101`-`113` | `Attack`, `Nibble`, `Murk Bubble`, `Strike`, `Pulse Guard`, `Warning Tone`, `Relay Burst` |
| States | `1`, `11`-`13` | `Knockout`, `Signal-Slick`, `Pulse Guard`, `Charging` |
| Items | `1`, `201` | `Potion`, `Sword / Project Excalibur` as key item |
| Weapons | `1`-`2` | `Practice Sword`, `Sword / Project Excalibur` |
| Armors | `1` | `Plain Clothes` |
| Tilesets | `2`-`6` | `Outside`, `Inside`, `Dungeon`, `SF Outside`, `SF Inside` placeholders |
| Animations | `1`, `6`, `16`, `35`, `39`, `40`, `41`, `43`, `51`, `54`, `106`, `115`, `117`, `120` | Placeholder-compatible RPG Maker MZ animations |

Recommended expansion ranges:

| Database | Range | Purpose |
|---|---:|---|
| Actors | `1`-`20` | Journey 1 actors and test-only support actors |
| Classes | `1`-`20` | Journey 1 classes |
| Enemies | `1`-`99` | Home Island and Journey 1 enemies |
| Troops | `1`-`99` | Home Island and Journey 1 troop groups |
| Skills | `1`-`99` | Actor, item, and system skills |
| Skills | `100`-`149` | Home Island enemy and boss skills |
| States | `1`-`49` | Core combat and Home Island states |
| Items | `1`-`99` | Consumables and testing items |
| Items | `200`-`249` | Key items and story-gate items |
| Weapons | `1`-`49` | Home Island and Journey 1 weapons |
| Armors | `1`-`49` | Home Island and Journey 1 armor |
| Common Events | `1`-`49` | Core Atlas common events |

## Map ID Reservation Plan

Reserve map IDs from the Atlas Home Island screen order. A clean skeleton can create placeholder maps with these names immediately, even before final layout work.

| Map ID | Atlas screen | RPG Maker map name |
|---:|---|---|
| `1` | `SCR-HOM-ASH-001` | `TWN_Ashford_Exterior` |
| `2` | `SCR-HOM-ASH-002` | `INT_Ashford_ElaraHouse` |
| `3` | `SCR-HOM-ASH-003` | `INT_Ashford_Shop` |
| `4` | `SCR-HOM-SKY-001` | `DGN_SkyreachHill_Path` |
| `5` | `SCR-HOM-HCV-001` | `DGN_HiddenCave_Entrance` |
| `6` | `SCR-HOM-HCV-002` | `DGN_HiddenCave_Trials` |
| `7` | `SCR-HOM-HCV-003` | `DGN_HiddenCave_Sanctum` |
| `8` | `SCR-HOM-GLS-001` | `DGN_Glassfield_Ruins_Exterior` |
| `9` | `SCR-HOM-SND-001` | `DGN_SealedNode_Upper` |
| `10` | `SCR-HOM-SND-002` | `DGN_SealedNode_CorePath` |
| `11` | `SCR-HOM-SND-003` | `DGN_SealedNode_Guardian` |
| `12` | `SCR-HOM-SND-004` | `DGN_SealedNode_RelayCore` |
| `13` | `SCR-HOM-RST-001` | `TWN_Rustshore_Docks` |
| `14` | `SCR-HOM-RST-002` | `CUT_Mainland_Departure` |
| `15` | `SCR-HOM-FOG-001` | `FLD_Fogfen_Marsh_Field` |
| `16` | `SCR-HOM-FOG-002` | `FLD_Fogfen_Deeper_Marsh_Pocket` |

Recommended expansion ranges:

| Map range | Purpose |
|---:|---|
| `1`-`49` | Home Island vertical slice |
| `50`-`99` | Journey 2 / mainland entry |
| `100`-`149` | Later Journey 2 interiors and dungeons |
| `150`-`199` | Test maps and debug harnesses |

## Switch, Variable, And Common Event Ranges

The current project has legacy switches and almost no named variables. The clean skeleton should reserve named ranges before any event implementation begins.

### Switches

| Range | Purpose |
|---:|---|
| `1`-`49` | Journey 1 story and gate switches |
| `50`-`79` | Home Island trial switches |
| `80`-`99` | Home Island optional/collection switches |
| `100`-`149` | Combat and encounter switches |
| `150`-`199` | Debug/test switches |

Initial switch names:

| ID | Name |
|---:|---|
| `1` | `J1_Tremor_Event` |
| `2` | `J1_Skyreach_AccessOpen` |
| `3` | `J1_HiddenCave_Entered` |
| `4` | `J1_Trial_Body_Clear` |
| `5` | `J1_Trial_Mind_Clear` |
| `6` | `J1_Trial_Heart_Clear` |
| `7` | `J1_Sword_Obtained` |
| `8` | `J1_Glassfield_SealOpened` |
| `9` | `J1_SealedNode_Entered` |
| `10` | `J1_CorePath_DoorOpened` |
| `11` | `J1_Node07_GuardianDefeated` |
| `12` | `J1_Node07_RelayRestored` |
| `13` | `J1_Mainland_TravelUnlocked` |
| `14` | `J1_Departure_Confirmed` |
| `50` | `Trial_Body_Active` |
| `51` | `Trial_Mind_Active` |
| `52` | `Trial_Heart_Active` |

### Variables

| Range | Purpose |
|---:|---|
| `1`-`49` | Journey and story state |
| `50`-`79` | Trial mechanics |
| `80`-`99` | Encounter and region support |
| `100`-`149` | Debug/test variables |

Initial variable names:

| ID | Name |
|---:|---|
| `1` | `Current_Journey` |
| `2` | `Archive_Recovery_Percent` |
| `50` | `Trial_Body_Attempts` |
| `51` | `Trial_Mind_SequenceStep` |
| `52` | `Trial_Heart_IntentChoice` |
| `80` | `Current_Encounter_Zone` |

### Common Events

| ID | Name | Source |
|---:|---|---|
| `1` | `CE_Archive_Message_Display` | Atlas export common event candidate `CE-ARCHIVE-MSG` |
| `2` | `CE_Sword_Authentication` | Atlas export common event candidate `CE-SWORD-AUTH` |
| `3` | `CE_Relay_Resolution` | Atlas export common event candidate `CE-RELAY-RESOLVE` |
| `4` | `CE_Screen_Transition_Helper` | Atlas export common event candidate `CE-SCREEN-FADE` |
| `5` | `CE_Trial_Complete_Chime` | Atlas export common event candidate `CE_Trial_Complete_Chime` |
| `6` | `CE_Trial_Reset_Feedback` | Atlas export common event candidate `CE_Trial_Reset` |

## Migration Recommendation

Final decision: **GO clean skeleton / NO GO current project**.

Rationale:

- The current project is valuable as a prototype and reference, but it is not clean enough to be the Atlas implementation baseline.
- Atlas now specifies enough map, database, event, transfer, tileset, animation, switch, variable, and common event expectations to justify a clean build target.
- A clean skeleton reduces importer risk because ID collisions become structural failures rather than subjective cleanup choices.
- Keeping the legacy project intact preserves earlier experiments without letting them contaminate the Atlas-first implementation path.

BUILD-0001 should create the clean skeleton in a separate project/repository location and should not rewrite the current RPG Maker project in place.

## BUILD-0001 Acceptance Gate

Before any write-capable Atlas importer is allowed, BUILD-0001 should prove:

- The skeleton opens as a valid RPG Maker MZ project.
- All required `data/*.json` files parse as valid JSON.
- `MapInfos.json` contains the 16 reserved Home Island maps by exact name.
- Reserved database IDs contain the Atlas rows or explicit placeholder rows with matching names.
- `System.json` contains the reserved switch and variable names.
- `CommonEvents.json` contains the reserved common event placeholders.
- The WO-0020 audit tool runs against the skeleton and reports no missing maps or reserved database rows.
- Any remaining warnings are limited to accepted placeholder detail, not ID/name collisions.
