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

- Found: 89
- Missing: 62
- Present with warning: 1
- Not machine-checkable yet: 1
- Total findings: 153

## Category Summary

| Category | Found | Missing | Warning | Not Machine-Checkable |
|---|---:|---:|---:|---:|
| Actor | 1 | 0 | 0 | 0 |
| Animations | 14 | 0 | 0 | 1 |
| Armor | 1 | 0 | 0 | 0 |
| Atlas Events | 0 | 31 | 0 | 0 |
| Class | 1 | 0 | 0 | 0 |
| Common Events | 6 | 0 | 0 | 0 |
| Enemy | 4 | 0 | 0 | 0 |
| Item | 1 | 0 | 0 | 0 |
| Key Item | 1 | 0 | 0 | 0 |
| Maps | 16 | 0 | 0 | 0 |
| Skill | 7 | 0 | 0 | 0 |
| Skill Details | 7 | 0 | 0 | 0 |
| State | 4 | 0 | 0 | 0 |
| Tilesets | 5 | 0 | 0 | 0 |
| Transfers | 0 | 30 | 0 | 0 |
| Trial State | 6 | 0 | 0 | 0 |
| Troop | 6 | 0 | 0 | 0 |
| Troop Details | 6 | 0 | 0 | 0 |
| Troop Event Pages | 1 | 1 | 1 | 0 |
| Weapon | 2 | 0 | 0 | 0 |

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
| found | Armor | `CHR-KAI-001` | Armor 1 - Plain Clothes | Armors.json id 1 matches name |

### Atlas Events

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| missing | Atlas Events | `EVT-HOM-001` | SCR-HOM-ASH-002 - Player Start | No event named 'Player Start' on map 2 |
| missing | Atlas Events | `EVT-HOM-002` | SCR-HOM-ASH-002 - Elara Intro Dialogue | No event named 'Elara Intro Dialogue' on map 2 |
| missing | Atlas Events | `EVT-HOM-003` | SCR-HOM-ASH-001 - Child Near Old Panel | No event named 'Child Near Old Panel' on map 1 |
| missing | Atlas Events | `EVT-HOM-004` | SCR-HOM-ASH-001 - Farmer With Warm Stones | No event named 'Farmer With Warm Stones' on map 1 |
| missing | Atlas Events | `EVT-HOM-005` | SCR-HOM-ASH-001 - Skyreach Joker | No event named 'Skyreach Joker' on map 1 |
| missing | Atlas Events | `EVT-HOM-006` | SCR-HOM-ASH-001 - Dock Messenger | No event named 'Dock Messenger' on map 1 |
| missing | Atlas Events | `EVT-HOM-007` | SCR-HOM-ASH-001 - Hidden Item | No event named 'Hidden Item' on map 1 |
| missing | Atlas Events | `EVT-HOM-008` | SCR-HOM-ASH-003 - Shopkeeper | No event named 'Shopkeeper' on map 3 |
| missing | Atlas Events | `EVT-HOM-009` | SCR-HOM-ASH-001 - Tremor Trigger | No event named 'Tremor Trigger' on map 1 |
| missing | Atlas Events | `EVT-HOM-010` | SCR-HOM-SKY-001 - Skyreach Gate | No event named 'Skyreach Gate' on map 4 |
| missing | Atlas Events | `EVT-HOM-011` | SCR-HOM-HCV-001 - Hidden Cave First Entry | No event named 'Hidden Cave First Entry' on map 5 |
| missing | Atlas Events | `EVT-HOM-012` | SCR-HOM-HCV-002 - Body Trial | No event named 'Body Trial' on map 6 |
| missing | Atlas Events | `EVT-HOM-013` | SCR-HOM-HCV-002 - Mind Trial | No event named 'Mind Trial' on map 6 |
| missing | Atlas Events | `EVT-HOM-014` | SCR-HOM-HCV-002 - Heart Trial | No event named 'Heart Trial' on map 6 |
| missing | Atlas Events | `EVT-HOM-015` | SCR-HOM-HCV-002 - Sanctum Gate | No event named 'Sanctum Gate' on map 6 |
| missing | Atlas Events | `EVT-HOM-016` | SCR-HOM-HCV-003 - Sword Pedestal | No event named 'Sword Pedestal' on map 7 |
| missing | Atlas Events | `EVT-HOM-017` | SCR-HOM-GLS-001 - Glassfield Seal | No event named 'Glassfield Seal' on map 8 |
| missing | Atlas Events | `EVT-HOM-018` | SCR-HOM-GLS-001 - Surface Fragment | No event named 'Surface Fragment' on map 8 |
| missing | Atlas Events | `EVT-HOM-019` | SCR-HOM-SND-001 - Sealed Node First Entry | No event named 'Sealed Node First Entry' on map 9 |
| missing | Atlas Events | `EVT-HOM-020` | SCR-HOM-SND-002 - Core Path Door | No event named 'Core Path Door' on map 10 |
| missing | Atlas Events | `EVT-HOM-021` | SCR-HOM-SND-003 - Node Seven Guardian | No event named 'Node Seven Guardian' on map 11 |
| missing | Atlas Events | `EVT-HOM-022` | SCR-HOM-SND-004 - Relay Core | No event named 'Relay Core' on map 12 |
| missing | Atlas Events | `EVT-HOM-023` | SCR-HOM-RST-001 - Dockmaster | No event named 'Dockmaster' on map 13 |
| missing | Atlas Events | `EVT-HOM-024` | SCR-HOM-RST-001 - Lighthouse Examine | No event named 'Lighthouse Examine' on map 13 |
| missing | Atlas Events | `EVT-HOM-025` | SCR-HOM-RST-001 - Boat Transfer | No event named 'Boat Transfer' on map 13 |
| missing | Atlas Events | `EVT-HOM-026` | SCR-HOM-RST-002 - Departure Sequence | No event named 'Departure Sequence' on map 14 |
| missing | Atlas Events | `EVT-HOM-027` | SCR-HOM-FOG-001 - Fogfen Entry / Exit Transfer | No event named 'Fogfen Entry / Exit Transfer' on map 15 |
| missing | Atlas Events | `EVT-HOM-028` | SCR-HOM-FOG-001 - Hidden Item Landmark | No event named 'Hidden Item Landmark' on map 15 |
| missing | Atlas Events | `EVT-HOM-029` | SCR-HOM-FOG-001 - Signal-Tick Reed Pool | No event named 'Signal-Tick Reed Pool' on map 15 |
| missing | Atlas Events | `EVT-HOM-030` | SCR-HOM-FOG-002 - Deeper Marsh Return Transfer | No event named 'Deeper Marsh Return Transfer' on map 16 |
| missing | Atlas Events | `EVT-HOM-031` | SCR-HOM-FOG-002 - Signal Pool / Cable Cluster Examine | No event named 'Signal Pool / Cable Cluster Examine' on map 16 |

### Class

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Class | `CHR-KAI-001` | Class 1 - Sword Bearer | Classes.json id 1 matches name |

### Common Events

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Common Events | `CE-ARCHIVE-MSG` | CE-ARCHIVE-MSG - Archive Message Display | CommonEvents.json id(s): 1 |
| found | Common Events | `CE-SWORD-AUTH` | CE-SWORD-AUTH - Sword Authentication | CommonEvents.json id(s): 2 |
| found | Common Events | `CE-RELAY-RESOLVE` | CE-RELAY-RESOLVE - Relay Resolution | CommonEvents.json id(s): 3 |
| found | Common Events | `CE-SCREEN-FADE` | CE-SCREEN-FADE - Screen Transition Helper | CommonEvents.json id(s): 4 |
| found | Common Events | `CE_Trial_Complete_Chime` | CE_Trial_Complete_Chime - Trial Completion Chime | CommonEvents.json id(s): 5 |
| found | Common Events | `CE_Trial_Reset` | CE_Trial_Reset - Trial Reset Feedback | CommonEvents.json id(s): 6 |

### Enemy

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Enemy | `MON-GEL-001` | Enemy 1 - Meadow Gel | Enemies.json id 1 matches name |
| found | Enemy | `MON-RAT-001` | Enemy 2 - Ash Rat | Enemies.json id 2 matches name |
| found | Enemy | `MON-GEL-002` | Enemy 3 - Marsh Gel | Enemies.json id 3 matches name |
| found | Enemy | `BOS-N07-001` | Enemy 10 - Node Seven Guardian | Enemies.json id 10 matches name |

### Item

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Item | `Prototype item` | Item 1 - Potion | Items.json id 1 matches name |

### Key Item

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Key Item | `Sword truth layer` | Key Item 201 - Sword / Project Excalibur | Items.json id 201 matches name |

### Maps

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Maps | `SCR-HOM-ASH-001` | TWN_Ashford_Exterior | MapInfos id(s): 1 |
| found | Maps | `SCR-HOM-ASH-002` | INT_Ashford_ElaraHouse | MapInfos id(s): 2 |
| found | Maps | `SCR-HOM-ASH-003` | INT_Ashford_Shop | MapInfos id(s): 3 |
| found | Maps | `SCR-HOM-SKY-001` | DGN_SkyreachHill_Path | MapInfos id(s): 4 |
| found | Maps | `SCR-HOM-HCV-001` | DGN_HiddenCave_Entrance | MapInfos id(s): 5 |
| found | Maps | `SCR-HOM-HCV-002` | DGN_HiddenCave_Trials | MapInfos id(s): 6 |
| found | Maps | `SCR-HOM-HCV-003` | DGN_HiddenCave_Sanctum | MapInfos id(s): 7 |
| found | Maps | `SCR-HOM-GLS-001` | DGN_Glassfield_Ruins_Exterior | MapInfos id(s): 8 |
| found | Maps | `SCR-HOM-SND-001` | DGN_SealedNode_Upper | MapInfos id(s): 9 |
| found | Maps | `SCR-HOM-SND-002` | DGN_SealedNode_CorePath | MapInfos id(s): 10 |
| found | Maps | `SCR-HOM-SND-003` | DGN_SealedNode_Guardian | MapInfos id(s): 11 |
| found | Maps | `SCR-HOM-SND-004` | DGN_SealedNode_RelayCore | MapInfos id(s): 12 |
| found | Maps | `SCR-HOM-RST-001` | TWN_Rustshore_Docks | MapInfos id(s): 13 |
| found | Maps | `SCR-HOM-RST-002` | CUT_Mainland_Departure | MapInfos id(s): 14 |
| found | Maps | `SCR-HOM-FOG-001` | FLD_Fogfen_Marsh_Field | MapInfos id(s): 15 |
| found | Maps | `SCR-HOM-FOG-002` | FLD_Fogfen_Deeper_Marsh_Pocket | MapInfos id(s): 16 |

### Skill

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Skill | `Engine default` | Skill 1 - Attack | Skills.json id 1 matches name |
| found | Skill | `MON-RAT-001` | Skill 101 - Nibble | Skills.json id 101 matches name |
| found | Skill | `MON-GEL-002` | Skill 102 - Murk Bubble | Skills.json id 102 matches name |
| found | Skill | `BOS-N07-001` | Skill 110 - Strike | Skills.json id 110 matches name |
| found | Skill | `BOS-N07-001` | Skill 111 - Pulse Guard | Skills.json id 111 matches name |
| found | Skill | `BOS-N07-001` | Skill 112 - Warning Tone | Skills.json id 112 matches name |
| found | Skill | `BOS-N07-001` | Skill 113 - Relay Burst | Skills.json id 113 matches name |

### Skill Details

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Skill Details | `1` | Skill 1 - Attack | Name and animation ID match |
| found | Skill Details | `101` | Skill 101 - Nibble | Name and animation ID match |
| found | Skill Details | `102` | Skill 102 - Murk Bubble | Name and animation ID match |
| found | Skill Details | `110` | Skill 110 - Strike | Name and animation ID match |
| found | Skill Details | `111` | Skill 111 - Pulse Guard | Name and animation ID match |
| found | Skill Details | `112` | Skill 112 - Warning Tone | Name and animation ID match |
| found | Skill Details | `113` | Skill 113 - Relay Burst | Name and animation ID match |

### State

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | State | `Engine default` | State 1 - Knockout | States.json id 1 matches name |
| found | State | `MON-GEL-002` | State 11 - Signal-Slick | States.json id 11 matches name |
| found | State | `BOS-N07-001` | State 12 - Pulse Guard | States.json id 12 matches name |
| found | State | `BOS-N07-001` | State 13 - Charging | States.json id 13 matches name |

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
| missing | Transfers | `TRN-HOM-001` | SCR-HOM-ASH-002 -> SCR-HOM-ASH-001 | No transfer command from map 2 to map 1 |
| missing | Transfers | `TRN-HOM-002` | SCR-HOM-ASH-001 -> SCR-HOM-ASH-002 | No transfer command from map 1 to map 2 |
| missing | Transfers | `TRN-HOM-003` | SCR-HOM-ASH-001 -> SCR-HOM-ASH-003 | No transfer command from map 1 to map 3 |
| missing | Transfers | `TRN-HOM-004` | SCR-HOM-ASH-003 -> SCR-HOM-ASH-001 | No transfer command from map 3 to map 1 |
| missing | Transfers | `TRN-HOM-005` | SCR-HOM-ASH-001 -> SCR-HOM-SKY-001 | No transfer command from map 1 to map 4 |
| missing | Transfers | `TRN-HOM-006` | SCR-HOM-SKY-001 -> SCR-HOM-ASH-001 | No transfer command from map 4 to map 1 |
| missing | Transfers | `TRN-HOM-007` | SCR-HOM-ASH-001 -> SCR-HOM-RST-001 | No transfer command from map 1 to map 13 |
| missing | Transfers | `TRN-HOM-008` | SCR-HOM-RST-001 -> SCR-HOM-ASH-001 | No transfer command from map 13 to map 1 |
| missing | Transfers | `TRN-HOM-009` | SCR-HOM-SKY-001 -> SCR-HOM-HCV-001 | No transfer command from map 4 to map 5 |
| missing | Transfers | `TRN-HOM-010` | SCR-HOM-HCV-001 -> SCR-HOM-SKY-001 | No transfer command from map 5 to map 4 |
| missing | Transfers | `TRN-HOM-011` | SCR-HOM-HCV-001 -> SCR-HOM-HCV-002 | No transfer command from map 5 to map 6 |
| missing | Transfers | `TRN-HOM-012` | SCR-HOM-HCV-002 -> SCR-HOM-HCV-001 | No transfer command from map 6 to map 5 |
| missing | Transfers | `TRN-HOM-013` | SCR-HOM-HCV-002 -> SCR-HOM-HCV-003 | No transfer command from map 6 to map 7 |
| missing | Transfers | `TRN-HOM-014` | SCR-HOM-HCV-003 -> SCR-HOM-HCV-002 | No transfer command from map 7 to map 6 |
| missing | Transfers | `TRN-HOM-015` | SCR-HOM-ASH-001 -> SCR-HOM-GLS-001 | No transfer command from map 1 to map 8 |
| missing | Transfers | `TRN-HOM-016` | SCR-HOM-GLS-001 -> SCR-HOM-ASH-001 | No transfer command from map 8 to map 1 |
| missing | Transfers | `TRN-HOM-017` | SCR-HOM-GLS-001 -> SCR-HOM-SND-001 | No transfer command from map 8 to map 9 |
| missing | Transfers | `TRN-HOM-018` | SCR-HOM-SND-001 -> SCR-HOM-GLS-001 | No transfer command from map 9 to map 8 |
| missing | Transfers | `TRN-HOM-019` | SCR-HOM-SND-001 -> SCR-HOM-SND-002 | No transfer command from map 9 to map 10 |
| missing | Transfers | `TRN-HOM-020` | SCR-HOM-SND-002 -> SCR-HOM-SND-001 | No transfer command from map 10 to map 9 |
| missing | Transfers | `TRN-HOM-021` | SCR-HOM-SND-002 -> SCR-HOM-SND-003 | No transfer command from map 10 to map 11 |
| missing | Transfers | `TRN-HOM-022` | SCR-HOM-SND-003 -> SCR-HOM-SND-002 | No transfer command from map 11 to map 10 |
| missing | Transfers | `TRN-HOM-023` | SCR-HOM-SND-003 -> SCR-HOM-SND-004 | No transfer command from map 11 to map 12 |
| missing | Transfers | `TRN-HOM-024` | SCR-HOM-SND-004 -> SCR-HOM-SND-003 | No transfer command from map 12 to map 11 |
| missing | Transfers | `TRN-HOM-025` | SCR-HOM-RST-001 -> SCR-HOM-RST-002 | No transfer command from map 13 to map 14 |
| missing | Transfers | `TRN-HOM-026` | SCR-HOM-RST-002 -> Journey II start | Target screen map is missing from MapInfos.json |
| missing | Transfers | `TRN-HOM-027` | SCR-HOM-ASH-001 -> SCR-HOM-FOG-001 | No transfer command from map 1 to map 15 |
| missing | Transfers | `TRN-HOM-028` | SCR-HOM-FOG-001 -> SCR-HOM-ASH-001 | No transfer command from map 15 to map 1 |
| missing | Transfers | `TRN-HOM-029` | SCR-HOM-FOG-001 -> SCR-HOM-FOG-002 | No transfer command from map 15 to map 16 |
| missing | Transfers | `TRN-HOM-030` | SCR-HOM-FOG-002 -> SCR-HOM-FOG-001 | No transfer command from map 16 to map 15 |

### Trial State

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Trial State | `J1_Trial_Body_Clear` | J1_Trial_Body_Clear | System.json switch 4 |
| found | Trial State | `J1_Trial_Mind_Clear` | J1_Trial_Mind_Clear | System.json switch 5 |
| found | Trial State | `J1_Trial_Heart_Clear` | J1_Trial_Heart_Clear | System.json switch 6 |
| found | Trial State | `Trial_Body_Attempts` | Trial_Body_Attempts | System.json variable 50 |
| found | Trial State | `Trial_Mind_SequenceStep` | Trial_Mind_SequenceStep | System.json variable 51 |
| found | Trial State | `Trial_Heart_IntentChoice` | Trial_Heart_IntentChoice | System.json variable 52 |

### Troop

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Troop | `MON-GEL-001` | Troop 1 - HOM Field 1 | Troops.json id 1 matches name |
| found | Troop | `MON-GEL-001` | Troop 2 - HOM Field 2 | Troops.json id 2 matches name |
| found | Troop | `MON-RAT-001, MON-GEL-001` | Troop 3 - HOM Field 3 | Troops.json id 3 matches name |
| found | Troop | `MON-GEL-002` | Troop 4 - HOM Fogfen 1 | Troops.json id 4 matches name |
| found | Troop | `MON-GEL-002, MON-RAT-001` | Troop 5 - HOM Fogfen 2 | Troops.json id 5 matches name |
| found | Troop | `BOS-N07-001` | Troop 10 - HOM Node Boss | Troops.json id 10 matches name |

### Troop Details

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Troop Details | `1` | Troop 1 - HOM Field 1 | Troop row name matches |
| found | Troop Details | `2` | Troop 2 - HOM Field 2 | Troop row name matches |
| found | Troop Details | `3` | Troop 3 - HOM Field 3 | Troop row name matches |
| found | Troop Details | `4` | Troop 4 - HOM Fogfen 1 | Troop row name matches |
| found | Troop Details | `5` | Troop 5 - HOM Fogfen 2 | Troop row name matches |
| found | Troop Details | `10` | Troop 10 - HOM Node Boss | Troop row name matches |

### Troop Event Pages

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Troop Event Pages | `1-5` | Troop 1-5 event page None | Troops 1-5 have no non-empty event page commands |
| present with warning | Troop Event Pages | `10` | Troop 10 event page 1 | Optional troop page exists but contains no placeholder commands |
| missing | Troop Event Pages | `10` | Troop 10 event page 2 | Expected page 2; troop has 1 page(s) |

### Weapon

| Status | Category | Atlas / Expected ID | Expected | Detail |
|---|---|---|---|---|
| found | Weapon | `CHR-KAI-001` | Weapon 1 - Practice Sword | Weapons.json id 1 matches name |
| found | Weapon | `Sword truth layer` | Weapon 2 - Sword / Project Excalibur | Weapons.json id 2 matches name |

## Notes

- `missing` means the expected Atlas row or map name was not found in the current RPG Maker data.
- `present with warning` usually means an ID exists but its name differs from Atlas, or the expected name exists at a different ID.
- `not machine-checkable yet` is reserved for export expectations that explicitly do not map to an RPG Maker database row, such as `Animation None`.
- Write-capable import behavior remains out of scope.
