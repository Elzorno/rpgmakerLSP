# Home Island RPG Maker Data Readiness Audit

This report compares the Atlas Home Island export against current RPG Maker MZ data files.

The audit is read-only. It does not modify RPG Maker JSON, maps, events, assets, or project settings.

## Export Metadata

- Export: `home-island`
- Schema: `1.0.0`
- Generated: `2026-07-04T14:20:41+00:00`
- Source repo: `TheLastSwordProtocol-Atlas`
- Source commit: `bc3598b`

## Summary

- Found: 22
- Missing: 91
- Present with warning: 39
- Not machine-checkable yet: 1
- Total findings: 153

## Category Summary

| Category | Found | Missing | Warning | Not Machine-Checkable |
|---|---:|---:|---:|---:|
| Actor | 1 | 0 | 0 | 0 |
| Animations | 14 | 0 | 0 | 1 |
| Armor | 0 | 0 | 1 | 0 |
| Atlas Events | 0 | 31 | 0 | 0 |
| Class | 0 | 0 | 1 | 0 |
| Common Events | 0 | 6 | 0 | 0 |
| Enemy | 0 | 0 | 4 | 0 |
| Item | 0 | 0 | 1 | 0 |
| Key Item | 0 | 1 | 0 | 0 |
| Maps | 0 | 16 | 0 | 0 |
| Skill | 1 | 0 | 6 | 0 |
| Skill Details | 0 | 0 | 7 | 0 |
| State | 0 | 0 | 4 | 0 |
| Tilesets | 5 | 0 | 0 | 0 |
| Transfers | 0 | 30 | 0 | 0 |
| Trial State | 0 | 6 | 0 | 0 |
| Troop | 0 | 0 | 6 | 0 |
| Troop Details | 0 | 0 | 6 | 0 |
| Troop Event Pages | 1 | 1 | 1 | 0 |
| Weapon | 0 | 0 | 2 | 0 |

## Findings

### Actor

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Actor | `CHR-KAI-001` | Actor 1 - Kai | Actors.json id 1 matches name |

### Animations

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Animations | `1` | Animation 1 - Hit Physical | Animation row name matches |
| found | Animations | `6` | Animation 6 - Slash Physical | Animation row name matches |
| found | Animations | `16` | Animation 16 - Claw Physical | Animation row name matches |
| found | Animations | `35` | Animation 35 - Fog | Animation row name matches |
| found | Animations | `39` | Animation 39 - Bodyslam | Animation row name matches |
| found | Animations | `40` | Animation 40 - Flash | Animation row name matches |
| found | Animations | `41` | Animation 41 - Heal One 1 | Animation row name matches |
| found | Animations | `43` | Animation 43 - Heal All 1 | Animation row name matches |
| found | Animations | `51` | Animation 51 - Power up 1 | Animation row name matches |
| found | Animations | `54` | Animation 54 - Power down 1 | Animation row name matches |
| found | Animations | `106` | Animation 106 - Neutral One 1 | Animation row name matches |
| found | Animations | `115` | Animation 115 - Laser One | Animation row name matches |
| found | Animations | `117` | Animation 117 - Light Pillar 1 | Animation row name matches |
| found | Animations | `120` | Animation 120 - Radiation | Animation row name matches |
| not machine-checkable yet | Animations | `None` | Animation None - No animation | Atlas explicitly allows no RPG Maker animation |

### Armor

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| present with warning | Armor | `CHR-KAI-001` | Armor 1 - Plain Clothes | ID 1 is named '-----Armors'; expected name not found elsewhere |

### Atlas Events

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| missing | Atlas Events | `EVT-HOM-001` | SCR-HOM-ASH-002 - Player Start | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-002` | SCR-HOM-ASH-002 - Elara Intro Dialogue | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-003` | SCR-HOM-ASH-001 - Child Near Old Panel | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-004` | SCR-HOM-ASH-001 - Farmer With Warm Stones | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-005` | SCR-HOM-ASH-001 - Skyreach Joker | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-006` | SCR-HOM-ASH-001 - Dock Messenger | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-007` | SCR-HOM-ASH-001 - Hidden Item | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-008` | SCR-HOM-ASH-003 - Shopkeeper | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-009` | SCR-HOM-ASH-001 - Tremor Trigger | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-010` | SCR-HOM-SKY-001 - Skyreach Gate | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-011` | SCR-HOM-HCV-001 - Hidden Cave First Entry | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-012` | SCR-HOM-HCV-002 - Body Trial | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-013` | SCR-HOM-HCV-002 - Mind Trial | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-014` | SCR-HOM-HCV-002 - Heart Trial | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-015` | SCR-HOM-HCV-002 - Sanctum Gate | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-016` | SCR-HOM-HCV-003 - Sword Pedestal | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-017` | SCR-HOM-GLS-001 - Glassfield Seal | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-018` | SCR-HOM-GLS-001 - Surface Fragment | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-019` | SCR-HOM-SND-001 - Sealed Node First Entry | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-020` | SCR-HOM-SND-002 - Core Path Door | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-021` | SCR-HOM-SND-003 - Node Seven Guardian | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-022` | SCR-HOM-SND-004 - Relay Core | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-023` | SCR-HOM-RST-001 - Dockmaster | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-024` | SCR-HOM-RST-001 - Lighthouse Examine | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-025` | SCR-HOM-RST-001 - Boat Transfer | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-026` | SCR-HOM-RST-002 - Departure Sequence | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-027` | SCR-HOM-FOG-001 - Fogfen Entry / Exit Transfer | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-028` | SCR-HOM-FOG-001 - Hidden Item Landmark | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-029` | SCR-HOM-FOG-001 - Signal-Tick Reed Pool | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-030` | SCR-HOM-FOG-002 - Deeper Marsh Return Transfer | Source screen map is missing from MapInfos.json |
| missing | Atlas Events | `EVT-HOM-031` | SCR-HOM-FOG-002 - Signal Pool / Cable Cluster Examine | Source screen map is missing from MapInfos.json |

### Class

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| present with warning | Class | `CHR-KAI-001` | Class 1 - Sword Bearer | ID 1 is named 'Swordsman'; expected name not found elsewhere |

### Common Events

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| missing | Common Events | `CE-ARCHIVE-MSG` | CE-ARCHIVE-MSG - Archive Message Display | No common event with matching name |
| missing | Common Events | `CE-SWORD-AUTH` | CE-SWORD-AUTH - Sword Authentication | No common event with matching name |
| missing | Common Events | `CE-RELAY-RESOLVE` | CE-RELAY-RESOLVE - Relay Resolution | No common event with matching name |
| missing | Common Events | `CE-SCREEN-FADE` | CE-SCREEN-FADE - Screen Transition Helper | No common event with matching name |
| missing | Common Events | `CE_Trial_Complete_Chime` | CE_Trial_Complete_Chime - Trial Completion Chime | No common event with matching name |
| missing | Common Events | `CE_Trial_Reset` | CE_Trial_Reset - Trial Reset Feedback | No common event with matching name |

### Enemy

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| present with warning | Enemy | `MON-GEL-001` | Enemy 1 - Meadow Gel | ID 1 is named 'Goblin'; expected name not found elsewhere |
| present with warning | Enemy | `MON-RAT-001` | Enemy 2 - Ash Rat | ID 2 is named 'Gnome'; expected name not found elsewhere |
| present with warning | Enemy | `MON-GEL-002` | Enemy 3 - Marsh Gel | ID 3 is named 'Crow'; expected name not found elsewhere |
| present with warning | Enemy | `BOS-N07-001` | Enemy 10 - Node Seven Guardian | ID 10 is named 'Static Gnawrat'; expected name not found elsewhere |

### Item

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| present with warning | Item | `Prototype item` | Item 1 - Potion | ID 1 is named '-----Reserved'; expected name exists at id(s): 7 |

### Key Item

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| missing | Key Item | `Sword truth layer` | Key Item 201 - Sword / Project Excalibur | Items.json has no row at id 201 |

### Maps

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| missing | Maps | `SCR-HOM-ASH-001` | TWN_Ashford_Exterior | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-ASH-002` | INT_Ashford_ElaraHouse | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-ASH-003` | INT_Ashford_Shop | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-SKY-001` | DGN_SkyreachHill_Path | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-HCV-001` | DGN_HiddenCave_Entrance | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-HCV-002` | DGN_HiddenCave_Trials | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-HCV-003` | DGN_HiddenCave_Sanctum | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-GLS-001` | DGN_Glassfield_Ruins_Exterior | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-SND-001` | DGN_SealedNode_Upper | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-SND-002` | DGN_SealedNode_CorePath | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-SND-003` | DGN_SealedNode_Guardian | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-SND-004` | DGN_SealedNode_RelayCore | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-RST-001` | TWN_Rustshore_Docks | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-RST-002` | CUT_Mainland_Departure | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-FOG-001` | FLD_Fogfen_Marsh_Field | No MapInfos entry with this map name |
| missing | Maps | `SCR-HOM-FOG-002` | FLD_Fogfen_Deeper_Marsh_Pocket | No MapInfos entry with this map name |

### Skill

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Skill | `Engine default` | Skill 1 - Attack | Skills.json id 1 matches name |
| present with warning | Skill | `MON-RAT-001` | Skill 101 - Nibble | ID 101 is named 'Fire III'; expected name not found elsewhere |
| present with warning | Skill | `MON-GEL-002` | Skill 102 - Murk Bubble | ID 102 is named ''; expected name not found elsewhere |
| present with warning | Skill | `BOS-N07-001` | Skill 110 - Strike | ID 110 is named ''; expected name not found elsewhere |
| present with warning | Skill | `BOS-N07-001` | Skill 111 - Pulse Guard | ID 111 is named 'Blizzard I'; expected name not found elsewhere |
| present with warning | Skill | `BOS-N07-001` | Skill 112 - Warning Tone | ID 112 is named 'Blizzard II'; expected name not found elsewhere |
| present with warning | Skill | `BOS-N07-001` | Skill 113 - Relay Burst | ID 113 is named 'Blizzard III'; expected name not found elsewhere |

### Skill Details

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| present with warning | Skill Details | `1` | Skill 1 - Attack | animationId is -1, expected '6' |
| present with warning | Skill Details | `101` | Skill 101 - Nibble | name is 'Fire III'; animationId is 67, expected '16' |
| present with warning | Skill Details | `102` | Skill 102 - Murk Bubble | name is ''; animationId is 0, expected '35' |
| present with warning | Skill Details | `110` | Skill 110 - Strike | name is ''; animationId is 0, expected '6' |
| present with warning | Skill Details | `111` | Skill 111 - Pulse Guard | name is 'Blizzard I'; animationId is 73, expected '51' |
| present with warning | Skill Details | `112` | Skill 112 - Warning Tone | name is 'Blizzard II'; animationId is 74, expected '106' |
| present with warning | Skill Details | `113` | Skill 113 - Relay Burst | name is 'Blizzard III'; animationId is 75, expected '115' |

### State

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| present with warning | State | `Engine default` | State 1 - Knockout | ID 1 is named 'Dead'; expected name not found elsewhere |
| present with warning | State | `MON-GEL-002` | State 11 - Signal-Slick | ID 11 is named ''; expected name not found elsewhere |
| present with warning | State | `BOS-N07-001` | State 12 - Pulse Guard | ID 12 is named 'Paralysis'; expected name not found elsewhere |
| present with warning | State | `BOS-N07-001` | State 13 - Charging | ID 13 is named 'Stun'; expected name not found elsewhere |

### Tilesets

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Tilesets | `Outside` | Outside | Tilesets.json id(s): 2 |
| found | Tilesets | `Inside` | Inside | Tilesets.json id(s): 3 |
| found | Tilesets | `Dungeon` | Dungeon | Tilesets.json id(s): 4 |
| found | Tilesets | `SF Outside` | SF Outside | Tilesets.json id(s): 5 |
| found | Tilesets | `SF Inside` | SF Inside | Tilesets.json id(s): 6 |

### Transfers

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| missing | Transfers | `TRN-HOM-001` | SCR-HOM-ASH-002 -> SCR-HOM-ASH-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-002` | SCR-HOM-ASH-001 -> SCR-HOM-ASH-002 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-003` | SCR-HOM-ASH-001 -> SCR-HOM-ASH-003 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-004` | SCR-HOM-ASH-003 -> SCR-HOM-ASH-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-005` | SCR-HOM-ASH-001 -> SCR-HOM-SKY-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-006` | SCR-HOM-SKY-001 -> SCR-HOM-ASH-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-007` | SCR-HOM-ASH-001 -> SCR-HOM-RST-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-008` | SCR-HOM-RST-001 -> SCR-HOM-ASH-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-009` | SCR-HOM-SKY-001 -> SCR-HOM-HCV-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-010` | SCR-HOM-HCV-001 -> SCR-HOM-SKY-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-011` | SCR-HOM-HCV-001 -> SCR-HOM-HCV-002 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-012` | SCR-HOM-HCV-002 -> SCR-HOM-HCV-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-013` | SCR-HOM-HCV-002 -> SCR-HOM-HCV-003 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-014` | SCR-HOM-HCV-003 -> SCR-HOM-HCV-002 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-015` | SCR-HOM-ASH-001 -> SCR-HOM-GLS-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-016` | SCR-HOM-GLS-001 -> SCR-HOM-ASH-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-017` | SCR-HOM-GLS-001 -> SCR-HOM-SND-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-018` | SCR-HOM-SND-001 -> SCR-HOM-GLS-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-019` | SCR-HOM-SND-001 -> SCR-HOM-SND-002 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-020` | SCR-HOM-SND-002 -> SCR-HOM-SND-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-021` | SCR-HOM-SND-002 -> SCR-HOM-SND-003 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-022` | SCR-HOM-SND-003 -> SCR-HOM-SND-002 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-023` | SCR-HOM-SND-003 -> SCR-HOM-SND-004 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-024` | SCR-HOM-SND-004 -> SCR-HOM-SND-003 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-025` | SCR-HOM-RST-001 -> SCR-HOM-RST-002 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-026` | SCR-HOM-RST-002 -> Journey II start | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-027` | SCR-HOM-ASH-001 -> SCR-HOM-FOG-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-028` | SCR-HOM-FOG-001 -> SCR-HOM-ASH-001 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-029` | SCR-HOM-FOG-001 -> SCR-HOM-FOG-002 | Source screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-030` | SCR-HOM-FOG-002 -> SCR-HOM-FOG-001 | Source screen map is missing from MapInfos.json |

### Trial State

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| missing | Trial State | `J1_Trial_Body_Clear` | J1_Trial_Body_Clear | Switch name not found in System.json |
| missing | Trial State | `J1_Trial_Mind_Clear` | J1_Trial_Mind_Clear | Switch name not found in System.json |
| missing | Trial State | `J1_Trial_Heart_Clear` | J1_Trial_Heart_Clear | Switch name not found in System.json |
| missing | Trial State | `Trial_Body_Attempts` | Trial_Body_Attempts | Variable name not found in System.json |
| missing | Trial State | `Trial_Mind_SequenceStep` | Trial_Mind_SequenceStep | Variable name not found in System.json |
| missing | Trial State | `Trial_Heart_IntentChoice` | Trial_Heart_IntentChoice | Variable name not found in System.json |

### Troop

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| present with warning | Troop | `MON-GEL-001` | Troop 1 - HOM Field 1 | ID 1 is named 'Goblin*2'; expected name not found elsewhere |
| present with warning | Troop | `MON-GEL-001` | Troop 2 - HOM Field 2 | ID 2 is named 'Gnome*2'; expected name not found elsewhere |
| present with warning | Troop | `MON-RAT-001, MON-GEL-001` | Troop 3 - HOM Field 3 | ID 3 is named 'Crow*2'; expected name not found elsewhere |
| present with warning | Troop | `MON-GEL-002` | Troop 4 - HOM Fogfen 1 | ID 4 is named 'Treant'; expected name not found elsewhere |
| present with warning | Troop | `MON-GEL-002, MON-RAT-001` | Troop 5 - HOM Fogfen 2 | ID 5 is named 'Hi_monster'; expected name not found elsewhere |
| present with warning | Troop | `BOS-N07-001` | Troop 10 - HOM Node Boss | ID 10 is named 'NEMESIS Dragon Placeholder'; expected name not found elsewhere |

### Troop Details

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| present with warning | Troop Details | `1` | Troop 1 - HOM Field 1 | Troop row name is 'Goblin*2' |
| present with warning | Troop Details | `2` | Troop 2 - HOM Field 2 | Troop row name is 'Gnome*2' |
| present with warning | Troop Details | `3` | Troop 3 - HOM Field 3 | Troop row name is 'Crow*2' |
| present with warning | Troop Details | `4` | Troop 4 - HOM Fogfen 1 | Troop row name is 'Treant' |
| present with warning | Troop Details | `5` | Troop 5 - HOM Fogfen 2 | Troop row name is 'Hi_monster' |
| present with warning | Troop Details | `10` | Troop 10 - HOM Node Boss | Troop row name is 'NEMESIS Dragon Placeholder' |

### Troop Event Pages

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Troop Event Pages | `1-5` | Troop 1-5 event page None | Troops 1-5 have no non-empty event page commands |
| present with warning | Troop Event Pages | `10` | Troop 10 event page 1 | Optional troop page exists but contains no placeholder commands |
| missing | Troop Event Pages | `10` | Troop 10 event page 2 | Expected page 2; troop has 1 page(s) |

### Weapon

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| present with warning | Weapon | `CHR-KAI-001` | Weapon 1 - Practice Sword | ID 1 is named 'Short Sword'; expected name not found elsewhere |
| present with warning | Weapon | `Sword truth layer` | Weapon 2 - Sword / Project Excalibur | ID 2 is named 'Long Sword'; expected name not found elsewhere |

## Notes

- `missing` means the expected Atlas row or map name was not found in the current RPG Maker data.
- `present with warning` usually means an ID exists but its name differs from Atlas, or the expected name exists at a different ID.
- `not machine-checkable yet` is reserved for export expectations that explicitly do not map to an RPG Maker database row, such as `Animation None`.
- Write-capable import behavior remains out of scope.
