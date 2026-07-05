# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-001.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map001.json`

## Summary

- Found: 73
- Missing: 0
- Present with warning: 0
- Total findings: 73

## Category Summary

| Category | Found | Missing | Warning |
|---|---:|---:|---:|
| Blueprint Contract | 3 | 0 | 0 |
| Encounter Policy | 3 | 0 | 0 |
| Event Anchors | 12 | 0 | 0 |
| Map Shape | 7 | 0 | 0 |
| NPC Anchors | 20 | 0 | 0 |
| Transfer Anchors | 24 | 0 | 0 |
| Treasure Anchors | 4 | 0 | 0 |

## Findings

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-ASH-001 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=8 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map001.json |
| found | Map Shape | `MAP-002` | Map ID 1 | map_id=1 |
| found | Map Shape | `MAP-003` | Width 40 | width=40 |
| found | Map Shape | `MAP-004` | Height 32 | height=32 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=7680 |
| found | Map Shape | `MAP-006` | Display name Ashford Exterior | displayName=Ashford Exterior |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-ASH-001-001 |
| found | Transfer Anchors | `TRN-HOM-002` | Event `TRN-HOM-002 Enter Elara House` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-002-POS` | `TRN-HOM-002 Enter Elara House` at (17, 27) | actual=(17, 27) |
| found | Transfer Anchors | `TRN-HOM-002-TRACE` | `TRN-HOM-002 Enter Elara House` preserves TRN-HOM-002 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-002-TILE` | `TRN-HOM-002 Enter Elara House` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-003` | Event `TRN-HOM-003 Enter Ashford Shop` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-003-POS` | `TRN-HOM-003 Enter Ashford Shop` at (30, 18) | actual=(30, 18) |
| found | Transfer Anchors | `TRN-HOM-003-TRACE` | `TRN-HOM-003 Enter Ashford Shop` preserves TRN-HOM-003 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-003-TILE` | `TRN-HOM-003 Enter Ashford Shop` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-005` | Event `TRN-HOM-005 North path to Skyreach` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-005-POS` | `TRN-HOM-005 North path to Skyreach` at (20, 0) | actual=(20, 0) |
| found | Transfer Anchors | `TRN-HOM-005-TRACE` | `TRN-HOM-005 North path to Skyreach` preserves TRN-HOM-005 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-005-TILE` | `TRN-HOM-005 North path to Skyreach` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-007` | Event `TRN-HOM-007 South/east route to Rustshore` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-007-POS` | `TRN-HOM-007 South/east route to Rustshore` at (18, 31) | actual=(18, 31) |
| found | Transfer Anchors | `TRN-HOM-007-TRACE` | `TRN-HOM-007 South/east route to Rustshore` preserves TRN-HOM-007 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-007-TILE` | `TRN-HOM-007 South/east route to Rustshore` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-015` | Event `TRN-HOM-015 Route to Glassfield` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-015-POS` | `TRN-HOM-015 Route to Glassfield` at (39, 9) | actual=(39, 9) |
| found | Transfer Anchors | `TRN-HOM-015-TRACE` | `TRN-HOM-015 Route to Glassfield` preserves TRN-HOM-015 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-015-TILE` | `TRN-HOM-015 Route to Glassfield` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-027` | Event `TRN-HOM-027 Optional east route to Fogfen Marsh Field` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-027-POS` | `TRN-HOM-027 Optional east route to Fogfen Marsh Field` at (39, 23) | actual=(39, 23) |
| found | Transfer Anchors | `TRN-HOM-027-TRACE` | `TRN-HOM-027 Optional east route to Fogfen Marsh Field` preserves TRN-HOM-027 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-027-TILE` | `TRN-HOM-027 Optional east route to Fogfen Marsh Field` has a concrete tile | layer0 tile=2836 |
| found | NPC Anchors | `EVT-HOM-003` | Event `Child Near Old Panel` exists | event exists |
| found | NPC Anchors | `EVT-HOM-003-POS` | `Child Near Old Panel` at (7, 11) | actual=(7, 11) |
| found | NPC Anchors | `EVT-HOM-003-TRACE` | `Child Near Old Panel` preserves EVT-HOM-003 | Atlas ID present in name, note, or comments |
| found | NPC Anchors | `EVT-HOM-003-TILE` | `Child Near Old Panel` has a concrete tile | layer0 tile=2836 |
| found | NPC Anchors | `EVT-HOM-004` | Event `Farmer With Warm Stones` exists | event exists |
| found | NPC Anchors | `EVT-HOM-004-POS` | `Farmer With Warm Stones` at (11, 18) | actual=(11, 18) |
| found | NPC Anchors | `EVT-HOM-004-TRACE` | `Farmer With Warm Stones` preserves EVT-HOM-004 | Atlas ID present in name, note, or comments |
| found | NPC Anchors | `EVT-HOM-004-TILE` | `Farmer With Warm Stones` has a concrete tile | layer0 tile=2836 |
| found | NPC Anchors | `EVT-HOM-005` | Event `Skyreach Joker` exists | event exists |
| found | NPC Anchors | `EVT-HOM-005-POS` | `Skyreach Joker` at (22, 5) | actual=(22, 5) |
| found | NPC Anchors | `EVT-HOM-005-TRACE` | `Skyreach Joker` preserves EVT-HOM-005 | Atlas ID present in name, note, or comments |
| found | NPC Anchors | `EVT-HOM-005-TILE` | `Skyreach Joker` has a concrete tile | layer0 tile=2836 |
| found | NPC Anchors | `EVT-HOM-006` | Event `Dock Messenger` exists | event exists |
| found | NPC Anchors | `EVT-HOM-006-POS` | `Dock Messenger` at (17, 25) | actual=(17, 25) |
| found | NPC Anchors | `EVT-HOM-006-TRACE` | `Dock Messenger` preserves EVT-HOM-006 | Atlas ID present in name, note, or comments |
| found | NPC Anchors | `EVT-HOM-006-TILE` | `Dock Messenger` has a concrete tile | layer0 tile=2836 |
| found | NPC Anchors | `NPC-ASH-ELD-PLACEHOLDER` | Event `Village Elder Placeholder` exists | event exists |
| found | NPC Anchors | `NPC-ASH-ELD-PLACEHOLDER-POS` | `Village Elder Placeholder` at (25, 15) | actual=(25, 15) |
| found | NPC Anchors | `NPC-ASH-ELD-PLACEHOLDER-TRACE` | `Village Elder Placeholder` preserves NPC-ASH-ELD-PLACEHOLDER | Atlas ID present in name, note, or comments |
| found | NPC Anchors | `NPC-ASH-ELD-PLACEHOLDER-TILE` | `Village Elder Placeholder` has a concrete tile | layer0 tile=2836 |
| found | Treasure Anchors | `EVT-HOM-007` | Event `Hidden Item` exists | event exists |
| found | Treasure Anchors | `EVT-HOM-007-POS` | `Hidden Item` at (9, 20) | actual=(9, 20) |
| found | Treasure Anchors | `EVT-HOM-007-TRACE` | `Hidden Item` preserves EVT-HOM-007 | Atlas ID present in name, note, or comments |
| found | Treasure Anchors | `EVT-HOM-007-TILE` | `Hidden Item` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-009` | Event `Tremor Trigger` exists | event exists |
| found | Event Anchors | `EVT-HOM-009-POS` | `Tremor Trigger` at (20, 9) | actual=(20, 9) |
| found | Event Anchors | `EVT-HOM-009-TRACE` | `Tremor Trigger` preserves EVT-HOM-009 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-009-TILE` | `Tremor Trigger` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `INT-ASH-WARM-STONE-VENT` | Event `INT-ASH-WARM-STONE-VENT Warm-Stone Vent` exists | event exists |
| found | Event Anchors | `INT-ASH-WARM-STONE-VENT-POS` | `INT-ASH-WARM-STONE-VENT Warm-Stone Vent` at (9, 16) | actual=(9, 16) |
| found | Event Anchors | `INT-ASH-WARM-STONE-VENT-TRACE` | `INT-ASH-WARM-STONE-VENT Warm-Stone Vent` preserves INT-ASH-WARM-STONE-VENT | Atlas ID present in name, note, or comments |
| found | Event Anchors | `INT-ASH-WARM-STONE-VENT-TILE` | `INT-ASH-WARM-STONE-VENT Warm-Stone Vent` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `INT-ASH-OLD-PANEL` | Event `INT-ASH-OLD-PANEL Old Panel` exists | event exists |
| found | Event Anchors | `INT-ASH-OLD-PANEL-POS` | `INT-ASH-OLD-PANEL Old Panel` at (7, 9) | actual=(7, 9) |
| found | Event Anchors | `INT-ASH-OLD-PANEL-TRACE` | `INT-ASH-OLD-PANEL Old Panel` preserves INT-ASH-OLD-PANEL | Atlas ID present in name, note, or comments |
| found | Event Anchors | `INT-ASH-OLD-PANEL-TILE` | `INT-ASH-OLD-PANEL Old Panel` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=0 none=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
