# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-002.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map006.json`

## Summary

- Found: 61
- Missing: 0
- Present with warning: 0
- Total findings: 61

## Category Summary

| Category | Found | Missing | Warning |
|---|---:|---:|---:|
| Blueprint Contract | 3 | 0 | 0 |
| Encounter Policy | 3 | 0 | 0 |
| Event Anchors | 40 | 0 | 0 |
| Map Shape | 7 | 0 | 0 |
| Transfer Anchors | 8 | 0 | 0 |

## Findings

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-HCV-002 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=9 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map006.json |
| found | Map Shape | `MAP-002` | Map ID 6 | map_id=6 |
| found | Map Shape | `MAP-003` | Width 40 | width=40 |
| found | Map Shape | `MAP-004` | Height 32 | height=32 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=7680 |
| found | Map Shape | `MAP-006` | Display name Hidden Cave Trials | displayName=Hidden Cave Trials |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-HCV-002-001 |
| found | Transfer Anchors | `TRN-HOM-012` | Event `TRN-HOM-012 Return to entrance` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-012-POS` | `TRN-HOM-012 Return to entrance` at (20, 31) | actual=(20, 31) |
| found | Transfer Anchors | `TRN-HOM-012-TRACE` | `TRN-HOM-012 Return to entrance` preserves TRN-HOM-012 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-012-TILE` | `TRN-HOM-012 Return to entrance` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-013` | Event `TRN-HOM-013 Enter Sword Sanctum` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-013-POS` | `TRN-HOM-013 Enter Sword Sanctum` at (20, 0) | actual=(20, 0) |
| found | Transfer Anchors | `TRN-HOM-013-TRACE` | `TRN-HOM-013 Enter Sword Sanctum` preserves TRN-HOM-013 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-013-TILE` | `TRN-HOM-013 Enter Sword Sanctum` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-012` | Event `Body Trial` exists | event exists |
| found | Event Anchors | `EVT-HOM-012-POS` | `Body Trial` at (12, 20) | actual=(12, 20) |
| found | Event Anchors | `EVT-HOM-012-TRACE` | `Body Trial` preserves EVT-HOM-012 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-012-TILE` | `Body Trial` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-012A` | Event `EVT-HOM-012A Body Trial Reset 1` exists | event exists |
| found | Event Anchors | `EVT-HOM-012A-POS` | `EVT-HOM-012A Body Trial Reset 1` at (7, 18) | actual=(7, 18) |
| found | Event Anchors | `EVT-HOM-012A-TRACE` | `EVT-HOM-012A Body Trial Reset 1` preserves EVT-HOM-012A | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-012A-TILE` | `EVT-HOM-012A Body Trial Reset 1` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-012B` | Event `EVT-HOM-012B Body Trial Reset 2` exists | event exists |
| found | Event Anchors | `EVT-HOM-012B-POS` | `EVT-HOM-012B Body Trial Reset 2` at (9, 18) | actual=(9, 18) |
| found | Event Anchors | `EVT-HOM-012B-TRACE` | `EVT-HOM-012B Body Trial Reset 2` preserves EVT-HOM-012B | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-012B-TILE` | `EVT-HOM-012B Body Trial Reset 2` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-012C` | Event `EVT-HOM-012C Body Trial Reset 3` exists | event exists |
| found | Event Anchors | `EVT-HOM-012C-POS` | `EVT-HOM-012C Body Trial Reset 3` at (11, 18) | actual=(11, 18) |
| found | Event Anchors | `EVT-HOM-012C-TRACE` | `EVT-HOM-012C Body Trial Reset 3` preserves EVT-HOM-012C | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-012C-TILE` | `EVT-HOM-012C Body Trial Reset 3` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-013` | Event `Mind Trial` exists | event exists |
| found | Event Anchors | `EVT-HOM-013-POS` | `Mind Trial` at (20, 16) | actual=(20, 16) |
| found | Event Anchors | `EVT-HOM-013-TRACE` | `Mind Trial` preserves EVT-HOM-013 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-013-TILE` | `Mind Trial` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-013A` | Event `EVT-HOM-013A Mind Marker Left` exists | event exists |
| found | Event Anchors | `EVT-HOM-013A-POS` | `EVT-HOM-013A Mind Marker Left` at (17, 15) | actual=(17, 15) |
| found | Event Anchors | `EVT-HOM-013A-TRACE` | `EVT-HOM-013A Mind Marker Left` preserves EVT-HOM-013A | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-013A-TILE` | `EVT-HOM-013A Mind Marker Left` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-013B` | Event `EVT-HOM-013B Mind Marker Right` exists | event exists |
| found | Event Anchors | `EVT-HOM-013B-POS` | `EVT-HOM-013B Mind Marker Right` at (23, 15) | actual=(23, 15) |
| found | Event Anchors | `EVT-HOM-013B-TRACE` | `EVT-HOM-013B Mind Marker Right` preserves EVT-HOM-013B | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-013B-TILE` | `EVT-HOM-013B Mind Marker Right` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-013C` | Event `EVT-HOM-013C Mind Marker Center` exists | event exists |
| found | Event Anchors | `EVT-HOM-013C-POS` | `EVT-HOM-013C Mind Marker Center` at (20, 13) | actual=(20, 13) |
| found | Event Anchors | `EVT-HOM-013C-TRACE` | `EVT-HOM-013C Mind Marker Center` preserves EVT-HOM-013C | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-013C-TILE` | `EVT-HOM-013C Mind Marker Center` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-014` | Event `Heart Trial` exists | event exists |
| found | Event Anchors | `EVT-HOM-014-POS` | `Heart Trial` at (31, 20) | actual=(31, 20) |
| found | Event Anchors | `EVT-HOM-014-TRACE` | `Heart Trial` preserves EVT-HOM-014 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-014-TILE` | `Heart Trial` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-015` | Event `Sanctum Gate` exists | event exists |
| found | Event Anchors | `EVT-HOM-015-POS` | `Sanctum Gate` at (20, 6) | actual=(20, 6) |
| found | Event Anchors | `EVT-HOM-015-TRACE` | `Sanctum Gate` preserves EVT-HOM-015 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-015-TILE` | `Sanctum Gate` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
