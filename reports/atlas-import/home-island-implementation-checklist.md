# Home Island RPG Maker Implementation Checklist

Generated from the Atlas Home Island export.

## Export Metadata

- Export: `home-island`
- Schema: `1.0.0`
- Generated: `2026-07-04T14:20:41+00:00`
- Source repo: `TheLastSwordProtocol-Atlas`
- Source commit: `bc3598b`
- Source branch: `main`
- Production decision: `GO - Begin RPG Maker MZ implementation.`

## Read-Only Rule

This checklist is generated from Atlas. It does not modify RPG Maker JSON, maps, events, assets, or project settings.

## Map / Screen Checklist

- [ ] `SCR-HOM-ASH-001` `TWN_Ashford_Exterior` - Ashford Exterior using tileset `Outside`
  - Location: `LOC-ASH-001`
  - Implementation packet: `IMP-HOM-010`
  - Terrain: Village ground, paths, gardens, fences, house exteriors, warm-stone vent, reused metal panels
  - Passability: Houses/fences/vents block; paths clear; north and south/east exits readable
  - Regions: Region 0 only; no encounter regions inside village
  - Encounter zones: None; no random encounters in village
  - Placement notes: Place Elara House, Shop, optional Elder House transfers; hidden item four steps south of warm-stone vent; NPCs around village center
- [ ] `SCR-HOM-ASH-002` `INT_Ashford_ElaraHouse` - Elara House Interior using tileset `Inside`
  - Location: `LOC-ASH-001`
  - Implementation packet: `IMP-HOM-010`
  - Terrain: Cozy home floor/walls, bed, table/chair, hearth or warm-stone equivalent, shelf/keepsake
  - Passability: Walls/furniture block; exit tile clear; player start has free movement
  - Regions: Region 0 only
  - Encounter zones: None
  - Placement notes: Player start, Elara event, exit transfer, optional keepsake/bookshelf examine
- [ ] `SCR-HOM-ASH-003` `INT_Ashford_Shop` - Ashford Shop Interior using tileset `Inside`
  - Location: `LOC-ASH-001`
  - Implementation packet: `IMP-HOM-010`
  - Terrain: Shop floor/walls, counter, shelves, crates/barrels, metal cabinet placeholder
  - Passability: Counter blocks except shopkeeper interaction side; shelves/cabinet block; exit clear
  - Regions: Region 0 only
  - Encounter zones: None
  - Placement notes: Shopkeeper behind or near counter; exit transfer back to Ashford
- [ ] `SCR-HOM-SKY-001` `DGN_SkyreachHill_Path` - Skyreach Hill Path using tileset `Outside`
  - Location: `LOC-SKY-001`
  - Implementation packet: `IMP-HOM-011`
  - Terrain: Hill path, tall grass, wind-swept stones, cliff/overlook, cave entrance, geometric carved stones
  - Passability: Cliff/stone edges block; winding route clear; cave mouth transfer visible
  - Regions: Region 1 optional for very light field encounters; Region 5 near cave/gate if no encounters desired
  - Encounter zones: Optional low-frequency Home Field troops only
  - Placement notes: Gate/warning near route entry; transfer to Hidden Cave at cave mouth; return transfer to Ashford route
- [ ] `SCR-HOM-HCV-001` `DGN_HiddenCave_Entrance` - Hidden Cave Entrance using tileset `Dungeon`
  - Location: `LOC-HCV-001`
  - Implementation packet: `IMP-HOM-011`
  - Terrain: Cave floor/walls, entry passage, subtle carved panels, dim blue-white accents
  - Passability: Cave walls block; forward path clear; entry/exit transfers readable
  - Regions: Region 0; Region 5 optional
  - Encounter zones: None preferred
  - Placement notes: First-entry event near entry; transfer back to Skyreach; transfer forward to trials
- [ ] `SCR-HOM-HCV-002` `DGN_HiddenCave_Trials` - Hidden Cave Trials using tileset `Dungeon`
  - Location: `LOC-HCV-001`
  - Implementation packet: `IMP-HOM-011`
  - Terrain: Cave chamber, three separated trial spaces, floor markings, hazard/reset tiles, marker plaques, sanctum gate
  - Passability: Trial boundaries block; Body hazard tiles are passable event triggers; sanctum gate path blocked until trials clear
  - Regions: Region 5 recommended; no random encounters
  - Encounter zones: None
  - Placement notes: Place Body lane/reset events, Mind markers, Heart pedestal, return transfer, and gated sanctum transfer per ATLAS-TEC-057
- [ ] `SCR-HOM-HCV-003` `DGN_HiddenCave_Sanctum` - Sword Sanctum using tileset `Dungeon`
  - Location: `LOC-HCV-001`
  - Implementation packet: `IMP-HOM-011`
  - Terrain: Small sanctum, central pedestal, symmetrical floor, glass/stone panels, blue-white light
  - Passability: Walls/pedestal block; interaction tile in front of pedestal clear; exit clear
  - Regions: Region 5 recommended
  - Encounter zones: None
  - Placement notes: Sword pedestal centered; archive text presentation; transfer back to trials
- [ ] `SCR-HOM-GLS-001` `DGN_Glassfield_Ruins_Exterior` - Glassfield Ruins Exterior using tileset `SF Outside`
  - Location: `LOC-GLS-001`
  - Implementation packet: `IMP-HOM-012`
  - Terrain: Cracked glass-like panels, concrete/stone ruin, grass/flowers, metal ribs, sealed lower entrance
  - Passability: Ruin edges/ribs block; exploration loop clear; sealed entrance blocks until opened
  - Regions: Region 1 optional for low-risk outside encounters; Region 5 around seal if needed
  - Encounter zones: Optional Home Field troops: Meadow Gel, Ash Rat
  - Placement notes: Place sealed entrance event, surface fragment, return route, and transfer down after seal opens
- [ ] `SCR-HOM-SND-001` `DGN_SealedNode_Upper` - Sealed Node Upper using tileset `SF Inside`
  - Location: `LOC-SND-001`
  - Implementation packet: `IMP-HOM-012`
  - Terrain: Stone corridor, embedded metal/glass, cave-machine walls, faint warning lights, simple obstacle
  - Passability: Walls/machinery block; return and forward routes clear
  - Regions: Region 4 optional for low-frequency node encounters; Region 5 near first-entry event
  - Encounter zones: Optional low-frequency Ash Rat/Meadow Gel until construct enemies are defined
  - Placement notes: First-entry event near entrance; transfer up to Glassfield; transfer forward to core path
- [ ] `SCR-HOM-SND-002` `DGN_SealedNode_CorePath` - Sealed Node Core Path using tileset `SF Inside`
  - Location: `LOC-SND-001`
  - Implementation packet: `IMP-HOM-012`
  - Terrain: Cave-machine connector, cables, glass/metal surfaces, relay-line markings, simple door
  - Passability: Walls/cables block; door event controls forward route; back route clear
  - Regions: Region 4 optional; Region 5 around sealed door if no random encounters desired
  - Encounter zones: Optional one or two simple encounters
  - Placement notes: Place simple sealed door, transfer back, transfer forward to guardian
- [ ] `SCR-HOM-SND-003` `DGN_SealedNode_Guardian` - Guardian Chamber using tileset `SF Inside`
  - Location: `LOC-SND-001`
  - Implementation packet: `IMP-HOM-012`
  - Terrain: Compact boss chamber, central combat space, guardian focal point, closed relay passage
  - Passability: Chamber edge blocks; guardian event blocks before defeat; relay passage blocked until switch
  - Regions: Region 5 recommended
  - Encounter zones: No random encounters; boss event only
  - Placement notes: Guardian event centered; transfer back; forward transfer appears/unlocks after J1_Node07_GuardianDefeated
- [ ] `SCR-HOM-SND-004` `DGN_SealedNode_RelayCore` - Relay Node Seven Core using tileset `SF Inside`
  - Location: `LOC-SND-001`
  - Implementation packet: `IMP-HOM-012`
  - Terrain: Small relay chamber, central relay device, blue-white light, symmetrical old-world floor
  - Passability: Walls/device block; interaction point clear; return route clear
  - Regions: Region 5 recommended
  - Encounter zones: None
  - Placement notes: Relay device centered; archive message event; transfer back to guardian
- [ ] `SCR-HOM-RST-001` `TWN_Rustshore_Docks` - Rustshore Docks using tileset `Outside`
  - Location: `LOC-RST-001`
  - Implementation packet: `IMP-HOM-013`
  - Terrain: Shoreline, wooden dock, boat, hut, lighthouse, sea grass, coastal path
  - Passability: Water blocks except dock/boat interaction; dock edges clear but bounded; return path clear
  - Regions: Region 0 only
  - Encounter zones: None
  - Placement notes: Dockmaster near hut/boat; boat transfer gated by mainland travel switch; lighthouse examine; return transfer
- [ ] `SCR-HOM-RST-002` `CUT_Mainland_Departure` - Mainland Departure using tileset `Outside`
  - Location: `LOC-RST-001`
  - Implementation packet: `IMP-HOM-013`
  - Terrain: Small dock/boat cutscene area or reused dock strip
  - Passability: Keep path limited; avoid open exploration if cutscene map
  - Regions: Region 5 recommended
  - Encounter zones: None
  - Placement notes: Autorun/choice departure sequence; transfer to Journey II placeholder
- [ ] `SCR-HOM-FOG-001` `FLD_Fogfen_Marsh_Field` - Fogfen Marsh Field using tileset `Outside`
  - Location: `LOC-FOG-001`
  - Implementation packet: `IMP-HOM-015`
  - Terrain: Reeds, shallow water, mud, bent tree/post, cable landmark, glowing pool, marsh paths
  - Passability: Deep water/reed walls block; shallow bog may be slow/choke path; entry/exit always clear
  - Regions: Region 2 for marsh encounters; Region 3 for slow bog markers; Region 5 near transfers
  - Encounter zones: Fogfen troops 4 and 5 from ATLAS-TEC-056
  - Placement notes: Entry/exit transfer, deeper marsh transfer, signal clue, cable landmark, hidden item, optional hazard markers
- [ ] `SCR-HOM-FOG-002` `FLD_Fogfen_Deeper_Marsh_Pocket` - Deeper Marsh Pocket using tileset `Outside`
  - Location: `LOC-FOG-001`
  - Implementation packet: `IMP-HOM-015`
  - Terrain: Dense reeds, darker water/mud, submerged cable cluster, signal pool, reward cache
  - Passability: Dense reeds/deep water block; return route always clear; slow choke optional
  - Regions: Region 2 for marsh encounters; Region 3 for dense/slow passage; Region 5 near return transfer
  - Encounter zones: Slightly denser Fogfen troops 4 and 5; still early-game safe
  - Placement notes: Return transfer, signal pool examine, cable cluster examine, optional reward cache

## Transfer Event Checklist

- [ ] `TRN-HOM-001` from `SCR-HOM-ASH-002` to `SCR-HOM-ASH-001` when `Always or after intro` - Elara House exit
- [ ] `TRN-HOM-002` from `SCR-HOM-ASH-001` to `SCR-HOM-ASH-002` when `Always` - Enter Elara House
- [ ] `TRN-HOM-003` from `SCR-HOM-ASH-001` to `SCR-HOM-ASH-003` when `Always` - Enter Ashford Shop
- [ ] `TRN-HOM-004` from `SCR-HOM-ASH-003` to `SCR-HOM-ASH-001` when `Always` - Shop exit
- [ ] `TRN-HOM-005` from `SCR-HOM-ASH-001` to `SCR-HOM-SKY-001` when `Requires J1_Skyreach_AccessOpen` - North path to Skyreach
- [ ] `TRN-HOM-006` from `SCR-HOM-SKY-001` to `SCR-HOM-ASH-001` when `Always` - Return from Skyreach route
- [ ] `TRN-HOM-007` from `SCR-HOM-ASH-001` to `SCR-HOM-RST-001` when `Always` - South/east route to Rustshore
- [ ] `TRN-HOM-008` from `SCR-HOM-RST-001` to `SCR-HOM-ASH-001` when `Always` - Return from Rustshore route
- [ ] `TRN-HOM-009` from `SCR-HOM-SKY-001` to `SCR-HOM-HCV-001` when `Requires J1_Skyreach_AccessOpen` - Enter Hidden Cave
- [ ] `TRN-HOM-010` from `SCR-HOM-HCV-001` to `SCR-HOM-SKY-001` when `Always` - Exit cave
- [ ] `TRN-HOM-011` from `SCR-HOM-HCV-001` to `SCR-HOM-HCV-002` when `Always` - Enter trials
- [ ] `TRN-HOM-012` from `SCR-HOM-HCV-002` to `SCR-HOM-HCV-001` when `Always` - Return to entrance
- [ ] `TRN-HOM-013` from `SCR-HOM-HCV-002` to `SCR-HOM-HCV-003` when `Requires all trial switches` - Enter Sword Sanctum
- [ ] `TRN-HOM-014` from `SCR-HOM-HCV-003` to `SCR-HOM-HCV-002` when `Always` - Return from sanctum
- [ ] `TRN-HOM-015` from `SCR-HOM-ASH-001` to `SCR-HOM-GLS-001` when `Always or island route` - Route to Glassfield
- [ ] `TRN-HOM-016` from `SCR-HOM-GLS-001` to `SCR-HOM-ASH-001` when `Always` - Return from Glassfield
- [ ] `TRN-HOM-017` from `SCR-HOM-GLS-001` to `SCR-HOM-SND-001` when `Requires J1_Glassfield_SealOpened` - Enter Sealed Node
- [ ] `TRN-HOM-018` from `SCR-HOM-SND-001` to `SCR-HOM-GLS-001` when `Always` - Exit Sealed Node
- [ ] `TRN-HOM-019` from `SCR-HOM-SND-001` to `SCR-HOM-SND-002` when `Always` - Proceed deeper
- [ ] `TRN-HOM-020` from `SCR-HOM-SND-002` to `SCR-HOM-SND-001` when `Always` - Return to upper node
- [ ] `TRN-HOM-021` from `SCR-HOM-SND-002` to `SCR-HOM-SND-003` when `Always` - Enter guardian chamber
- [ ] `TRN-HOM-022` from `SCR-HOM-SND-003` to `SCR-HOM-SND-002` when `Always` - Return to core path
- [ ] `TRN-HOM-023` from `SCR-HOM-SND-003` to `SCR-HOM-SND-004` when `Requires J1_Node07_GuardianDefeated` - Enter relay core
- [ ] `TRN-HOM-024` from `SCR-HOM-SND-004` to `SCR-HOM-SND-003` when `Always` - Return from relay core
- [ ] `TRN-HOM-025` from `SCR-HOM-RST-001` to `SCR-HOM-RST-002` when `Requires J1_Mainland_TravelUnlocked and player confirmation` - Begin departure
- [ ] `TRN-HOM-026` from `SCR-HOM-RST-002` to `Journey II start` when `Current_Journey = 2` - Destination TBD: Coalmouth or landing screen
- [ ] `TRN-HOM-027` from `SCR-HOM-ASH-001` to `SCR-HOM-FOG-001` when `Always or island route` - Optional east route to Fogfen Marsh Field
- [ ] `TRN-HOM-028` from `SCR-HOM-FOG-001` to `SCR-HOM-ASH-001` when `Always` - Return from Fogfen to Ashford-side route
- [ ] `TRN-HOM-029` from `SCR-HOM-FOG-001` to `SCR-HOM-FOG-002` when `Always` - Optional deeper marsh branch
- [ ] `TRN-HOM-030` from `SCR-HOM-FOG-002` to `SCR-HOM-FOG-001` when `Always` - Return from deeper marsh pocket

## Atlas Event Checklist

- [ ] `EVT-HOM-001` on `SCR-HOM-ASH-002` - Player Start (New game begins here)
- [ ] `EVT-HOM-002` on `SCR-HOM-ASH-002` - Elara Intro Dialogue (Supports story-state pages)
- [ ] `EVT-HOM-003` on `SCR-HOM-ASH-001` - Child Near Old Panel (Dialogue changes after tremor)
- [ ] `EVT-HOM-004` on `SCR-HOM-ASH-001` - Farmer With Warm Stones (Dialogue changes after Sword)
- [ ] `EVT-HOM-005` on `SCR-HOM-ASH-001` - Skyreach Joker (Reinforces hill taboo)
- [ ] `EVT-HOM-006` on `SCR-HOM-ASH-001` - Dock Messenger (Foreshadows Rustshore)
- [ ] `EVT-HOM-007` on `SCR-HOM-ASH-001` - Hidden Item (Self-switch after collection)
- [ ] `EVT-HOM-008` on `SCR-HOM-ASH-003` - Shopkeeper (Shop or placeholder process)
- [ ] `EVT-HOM-009` on `SCR-HOM-ASH-001` - Tremor Trigger (Sets J1_Tremor_Event and J1_Skyreach_AccessOpen)
- [ ] `EVT-HOM-010` on `SCR-HOM-SKY-001` - Skyreach Gate (Blocks until J1_Skyreach_AccessOpen)
- [ ] `EVT-HOM-011` on `SCR-HOM-HCV-001` - Hidden Cave First Entry (Sets J1_HiddenCave_Entered)
- [ ] `EVT-HOM-012` on `SCR-HOM-HCV-002` - Body Trial (Sets J1_Trial_Body_Clear)
- [ ] `EVT-HOM-013` on `SCR-HOM-HCV-002` - Mind Trial (Sets J1_Trial_Mind_Clear)
- [ ] `EVT-HOM-014` on `SCR-HOM-HCV-002` - Heart Trial (Sets J1_Trial_Heart_Clear)
- [ ] `EVT-HOM-015` on `SCR-HOM-HCV-002` - Sanctum Gate (Requires all trial switches)
- [ ] `EVT-HOM-016` on `SCR-HOM-HCV-003` - Sword Pedestal (Sets J1_Sword_Obtained and Archive_Recovery_Percent = 3)
- [ ] `EVT-HOM-017` on `SCR-HOM-GLS-001` - Glassfield Seal (Requires Sword, sets J1_Glassfield_SealOpened)
- [ ] `EVT-HOM-018` on `SCR-HOM-GLS-001` - Surface Fragment (Optional memory warning)
- [ ] `EVT-HOM-019` on `SCR-HOM-SND-001` - Sealed Node First Entry (Sets J1_SealedNode_Entered)
- [ ] `EVT-HOM-020` on `SCR-HOM-SND-002` - Core Path Door (Sets J1_CorePath_DoorOpened if used)
- [ ] `EVT-HOM-021` on `SCR-HOM-SND-003` - Node Seven Guardian (Starts boss, sets J1_Node07_GuardianDefeated)
- [ ] `EVT-HOM-022` on `SCR-HOM-SND-004` - Relay Core (Sets Node Seven and mainland unlock states)
- [ ] `EVT-HOM-023` on `SCR-HOM-RST-001` - Dockmaster (Blocks or permits departure by state)
- [ ] `EVT-HOM-024` on `SCR-HOM-RST-001` - Lighthouse Examine (Subtle old-world signal flavor)
- [ ] `EVT-HOM-025` on `SCR-HOM-RST-001` - Boat Transfer (Requires J1_Mainland_TravelUnlocked and confirmation)
- [ ] `EVT-HOM-026` on `SCR-HOM-RST-002` - Departure Sequence (Sets Current_Journey = 2)
- [ ] `EVT-HOM-027` on `SCR-HOM-FOG-001` - Fogfen Entry / Exit Transfer (Always available optional branch transfer)
- [ ] `EVT-HOM-028` on `SCR-HOM-FOG-001` - Hidden Item Landmark (Self-switch after collection)
- [ ] `EVT-HOM-029` on `SCR-HOM-FOG-001` - Signal-Tick Reed Pool (Optional environmental clue only)
- [ ] `EVT-HOM-030` on `SCR-HOM-FOG-002` - Deeper Marsh Return Transfer (Always returns to SCR-HOM-FOG-001)
- [ ] `EVT-HOM-031` on `SCR-HOM-FOG-002` - Signal Pool / Cable Cluster Examine (Optional environmental clue only)

### Common Event Candidates

- [ ] `CE-ARCHIVE-MSG` - Archive Message Display: Reusable old-system text display
- [ ] `CE-SWORD-AUTH` - Sword Authentication: Sword acquisition sequence support
- [ ] `CE-RELAY-RESOLVE` - Relay Resolution: Shared relay status update pattern
- [ ] `CE-SCREEN-FADE` - Screen Transition Helper: Reusable fade and transfer support
- [ ] `CE_Trial_Complete_Chime` - Trial Completion Chime: Optional shared completion feedback from ATLAS-TEC-057
- [ ] `CE_Trial_Reset` - Trial Reset Feedback: Optional shared harmless trial reset feedback from ATLAS-TEC-057

## Combat Database Checklist

### Database Allocation

- [ ] Actor `1` - Kai (Atlas: `CHR-KAI-001`; Required starting actor)
- [ ] Class `1` - Sword Bearer (Atlas: `CHR-KAI-001`; First-pass balanced class label)
- [ ] Enemy `1` - Meadow Gel (Atlas: `MON-GEL-001`; Basic starter enemy)
- [ ] Enemy `2` - Ash Rat (Atlas: `MON-RAT-001`; Faster starter enemy)
- [ ] Enemy `3` - Marsh Gel (Atlas: `MON-GEL-002`; Early debuff variant)
- [ ] Enemy `10` - Node Seven Guardian (Atlas: `BOS-N07-001`; Journey I boss)
- [ ] Troop `1` - HOM Field 1 (Atlas: `MON-GEL-001`; One Meadow Gel)
- [ ] Troop `2` - HOM Field 2 (Atlas: `MON-GEL-001`; Two Meadow Gels)
- [ ] Troop `3` - HOM Field 3 (Atlas: `MON-RAT-001, MON-GEL-001`; Ash Rat plus Meadow Gel)
- [ ] Troop `4` - HOM Fogfen 1 (Atlas: `MON-GEL-002`; One Marsh Gel)
- [ ] Troop `5` - HOM Fogfen 2 (Atlas: `MON-GEL-002, MON-RAT-001`; Marsh Gel plus Ash Rat)
- [ ] Troop `10` - HOM Node Boss (Atlas: `BOS-N07-001`; One Node Seven Guardian)
- [ ] Skill `1` - Attack (Atlas: `Engine default`; Basic physical attack)
- [ ] Skill `101` - Nibble (Atlas: `MON-RAT-001`; Ash Rat pressure skill)
- [ ] Skill `102` - Murk Bubble (Atlas: `MON-GEL-002`; Low-risk signal debuff skill)
- [ ] Skill `110` - Strike (Atlas: `BOS-N07-001`; Guardian basic attack)
- [ ] Skill `111` - Pulse Guard (Atlas: `BOS-N07-001`; Guardian defensive action)
- [ ] Skill `112` - Warning Tone (Atlas: `BOS-N07-001`; Guardian telegraph action)
- [ ] Skill `113` - Relay Burst (Atlas: `BOS-N07-001`; Guardian heavy action)
- [ ] State `1` - Knockout (Atlas: `Engine default`; Use standard KO behavior)
- [ ] State `11` - Signal-Slick (Atlas: `MON-GEL-002`; Light accuracy debuff)
- [ ] State `12` - Pulse Guard (Atlas: `BOS-N07-001`; Temporary defense buff)
- [ ] State `13` - Charging (Atlas: `BOS-N07-001`; Telegraph marker for Relay Burst)
- [ ] Item `1` - Potion (Atlas: `Prototype item`; Basic early recovery item)
- [ ] Key Item `201` - Sword / Project Excalibur (Atlas: `Sword truth layer`; Story key item paired with weapon row)
- [ ] Weapon `1` - Practice Sword (Atlas: `CHR-KAI-001`; Starting weapon)
- [ ] Weapon `2` - Sword / Project Excalibur (Atlas: `Sword truth layer`; Story weapon after Sword acquisition)
- [ ] Armor `1` - Plain Clothes (Atlas: `CHR-KAI-001`; Starting armor)

### Skills

- [ ] Skill `1` Attack - animation `6`, formula/effects: Engine default / Normal attack
- [ ] Skill `101` Nibble - animation `16`, formula/effects: a.atk * 3 - b.def * 2 / None
- [ ] Skill `102` Murk Bubble - animation `35`, formula/effects: a.mat * 2 + a.atk - b.mdf / Add State 11 at 30%
- [ ] Skill `110` Strike - animation `6`, formula/effects: a.atk * 4 - b.def * 2 / None
- [ ] Skill `111` Pulse Guard - animation `51`, formula/effects: 0 / Add State 12 at 100%
- [ ] Skill `112` Warning Tone - animation `106`, formula/effects: 0 / Add State 13 at 100%
- [ ] Skill `113` Relay Burst - animation `115`, formula/effects: a.atk * 4 + a.mat * 2 - b.mdf * 2 / Remove State 13 from user if practical

### Troops

- [ ] Troop `1` HOM Field 1 - 1x Enemy 1 Meadow Gel
- [ ] Troop `2` HOM Field 2 - 2x Enemy 1 Meadow Gel
- [ ] Troop `3` HOM Field 3 - 1x Enemy 2 Ash Rat, 1x Enemy 1 Meadow Gel
- [ ] Troop `4` HOM Fogfen 1 - 1x Enemy 3 Marsh Gel
- [ ] Troop `5` HOM Fogfen 2 - 1x Enemy 3 Marsh Gel, 1x Enemy 2 Ash Rat
- [ ] Troop `10` HOM Node Boss - 1x Enemy 10 Node Seven Guardian
- [ ] Troop event page `1-5` page `None` - None: No troop event pages required
- [ ] Troop event page `10` page `1` - Turn 0: Optional battle text placeholder: BOSS_NODE_SEVEN_OPENING_PLACEHOLDER
- [ ] Troop event page `10` page `2` - Enemy HP 0% to 50%: Optional battle text placeholder: BOSS_NODE_SEVEN_HALF_HP_PLACEHOLDER

### Encounter Placement

- [ ] Ashford outskirts and early field paths - Troop 1, Troop 2, Troop 3
- [ ] Fogfen Marsh traversable screens - Troop 4, Troop 5
- [ ] Glassfield approach - Troop 1, Troop 3
- [ ] Sealed Node - Troop 10 only

## Trial Mechanics Checklist

Source: `atlas/docs/09_Technical/Trial_Specs/Home_Island/Home_Island_Trial_Mechanics_Spec.md`

- [ ] Implement trial event/gate `EVT-HOM-012` from Atlas trial mechanics
- [ ] Implement trial event/gate `EVT-HOM-013` from Atlas trial mechanics
- [ ] Implement trial event/gate `EVT-HOM-014` from Atlas trial mechanics
- [ ] Implement trial event/gate `EVT-HOM-015` from Atlas trial mechanics
- [ ] Create or verify switch `J1_Trial_Body_Clear`
- [ ] Create or verify switch `J1_Trial_Mind_Clear`
- [ ] Create or verify switch `J1_Trial_Heart_Clear`
- [ ] Create or verify variable `Trial_Body_Attempts`
- [ ] Create or verify variable `Trial_Mind_SequenceStep`
- [ ] Create or verify variable `Trial_Heart_IntentChoice`

## Animation Assignment Checklist

### Core Animation IDs

- [ ] Animation `1` Hit Physical - Generic impact, enemy basic hit fallback
- [ ] Animation `6` Slash Physical - Kai sword attack, Guardian Strike
- [ ] Animation `16` Claw Physical - Ash Rat attack and Nibble
- [ ] Animation `35` Fog - Murk Bubble and signal/marsh haze
- [ ] Animation `39` Bodyslam - Gel basic attack
- [ ] Animation `40` Flash - Story flash, trial confirm, reward feedback
- [ ] Animation `41` Heal One 1 - Potion and single-target recovery
- [ ] Animation `43` Heal All 1 - Save/recovery shrine or whole-party recovery
- [ ] Animation `51` Power up 1 - Pulse Guard and positive activation
- [ ] Animation `54` Power down 1 - Harmless trial reset or failed input feedback
- [ ] Animation `106` Neutral One 1 - Archive message or neutral old-system pulse
- [ ] Animation `115` Laser One - Relay Burst and focused old-system beam
- [ ] Animation `117` Light Pillar 1 - Sword authentication and major access confirmation
- [ ] Animation `120` Radiation - Node Seven shutdown or large relay discharge

### Combat Animation Beats

- [ ] Basic attack / Kai sword hit - animation `6` Slash Physical (Actor Attack skill and Sword weapon attack)
- [ ] Meadow Gel attack - animation `39` Bodyslam (Meadow Gel basic attack)
- [ ] Ash Rat attack - animation `16` Claw Physical (Ash Rat basic attack)
- [ ] Ash Rat Nibble - animation `16` Claw Physical (Skill 101 Nibble)
- [ ] Marsh Gel attack - animation `39` Bodyslam (Marsh Gel basic attack)
- [ ] Murk Bubble - animation `35` Fog (Skill 102 Murk Bubble and Signal-Slick application)
- [ ] Node Seven Guardian Strike - animation `6` Slash Physical (Skill 110 Strike)
- [ ] Pulse Guard - animation `51` Power up 1 (Skill 111 Pulse Guard and State 12 application)
- [ ] Warning Tone - animation `106` Neutral One 1 (Skill 112 Warning Tone and State 13 Charging)
- [ ] Relay Burst - animation `115` Laser One (Skill 113 Relay Burst)
- [ ] Potion item use - animation `41` Heal One 1 (Item 1 Potion)
- [ ] Save/recovery point - animation `43` Heal All 1 (Optional save/recovery shrine behavior)
- [ ] Encounter start / alert - animation `40` Flash (Optional screen/map alert before evented battle)
- [ ] Victory / reward feedback - animation `40` Flash (Treasure, trial completion, optional reward cache, post-boss confirmation)

### Story / Event Animation Beats

- [ ] Tremor event - animation `None` No animation (Ashford tremor trigger uses screen shake/fade)
- [ ] Hidden Cave first entry - animation `40` Flash (Optional short cave-entry pulse)
- [ ] Body Trial success - animation `40` Flash (Completion feedback for J1_Trial_Body_Clear)
- [ ] Body Trial reset - animation `54` Power down 1 (Harmless reset feedback before repositioning Kai)
- [ ] Mind Trial correct marker - animation `40` Flash (Correct marker confirmation)
- [ ] Mind Trial wrong marker - animation `54` Power down 1 (Wrong marker/reset feedback)
- [ ] Mind Trial completion - animation `40` Flash (Completion feedback for J1_Trial_Mind_Clear)
- [ ] Heart Trial choice prompt - animation `None` No animation (Reflection pedestal prompt)
- [ ] Heart Trial completion - animation `117` Light Pillar 1 (Intent accepted / J1_Trial_Heart_Clear)
- [ ] Sanctum gate opens - animation `117` Light Pillar 1 (All trials complete, transfer to Sword Sanctum available)
- [ ] Sword authentication - animation `117` Light Pillar 1 (Sword pedestal acceptance and Sword acquisition)
- [ ] Archive message - animation `106` Neutral One 1 (AUTHORIZATION ACCEPTED, archive recovery text, relay status text)
- [ ] Glassfield seal opens - animation `117` Light Pillar 1 (Seal accepts Sword and opens lower entrance)
- [ ] Guardian battle start - animation `40` Flash (Optional evented pre-battle alert)
- [ ] Guardian defeated - animation `40` Flash (Post-battle switch confirmation)
- [ ] Node Seven shutdown - animation `120` Radiation (Relay Node Seven shutdown and authority revocation beat)
- [ ] Lighthouse settles - animation `40` Flash (Optional Rustshore lighthouse feedback after Node Seven)
- [ ] Mainland departure fade - animation `None` No animation (Boat departure cutscene/fade)

## Implementation Report Prompts

- [ ] List Atlas IDs implemented.
- [ ] List RPG Maker maps created or modified.
- [ ] List RPG Maker database rows created or modified.
- [ ] List transfer IDs implemented.
- [ ] List event IDs implemented.
- [ ] List placeholder assets used.
- [ ] List playtest route covered.
- [ ] List blockers, defects, or Atlas gaps discovered.
- [ ] Confirm no implementation-only design decisions were made without Atlas follow-up.
