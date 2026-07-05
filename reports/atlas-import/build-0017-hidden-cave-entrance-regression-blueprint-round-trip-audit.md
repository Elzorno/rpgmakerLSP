# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-001.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map005.json`

## Summary

- Found: 29
- Missing: 0
- Present with warning: 0
- Total findings: 29

## Category Summary

| Category | Found | Missing | Warning |
|---|---:|---:|---:|
| Blueprint Contract | 3 | 0 | 0 |
| Encounter Policy | 3 | 0 | 0 |
| Event Anchors | 8 | 0 | 0 |
| Map Shape | 7 | 0 | 0 |
| Transfer Anchors | 8 | 0 | 0 |

## Findings

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-HCV-001 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=8 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map005.json |
| found | Map Shape | `MAP-002` | Map ID 5 | map_id=5 |
| found | Map Shape | `MAP-003` | Width 24 | width=24 |
| found | Map Shape | `MAP-004` | Height 24 | height=24 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=3456 |
| found | Map Shape | `MAP-006` | Display name Hidden Cave Entrance | displayName=Hidden Cave Entrance |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-HCV-001-001 |
| found | Transfer Anchors | `TRN-HOM-010` | Event `TRN-HOM-010 Exit cave` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-010-POS` | `TRN-HOM-010 Exit cave` at (12, 23) | actual=(12, 23) |
| found | Transfer Anchors | `TRN-HOM-010-TRACE` | `TRN-HOM-010 Exit cave` preserves TRN-HOM-010 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-010-TILE` | `TRN-HOM-010 Exit cave` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-011` | Event `TRN-HOM-011 Enter trials` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-011-POS` | `TRN-HOM-011 Enter trials` at (12, 1) | actual=(12, 1) |
| found | Transfer Anchors | `TRN-HOM-011-TRACE` | `TRN-HOM-011 Enter trials` preserves TRN-HOM-011 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-011-TILE` | `TRN-HOM-011 Enter trials` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-011` | Event `Hidden Cave First Entry` exists | event exists |
| found | Event Anchors | `EVT-HOM-011-POS` | `Hidden Cave First Entry` at (12, 18) | actual=(12, 18) |
| found | Event Anchors | `EVT-HOM-011-TRACE` | `Hidden Cave First Entry` preserves EVT-HOM-011 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-011-TILE` | `Hidden Cave First Entry` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `INT-HCV-WALL-CARVING` | Event `INT-HCV-WALL-CARVING Wall Carving` exists | event exists |
| found | Event Anchors | `INT-HCV-WALL-CARVING-POS` | `INT-HCV-WALL-CARVING Wall Carving` at (17, 10) | actual=(17, 10) |
| found | Event Anchors | `INT-HCV-WALL-CARVING-TRACE` | `INT-HCV-WALL-CARVING Wall Carving` preserves INT-HCV-WALL-CARVING | Atlas ID present in name, note, or comments |
| found | Event Anchors | `INT-HCV-WALL-CARVING-TILE` | `INT-HCV-WALL-CARVING Wall Carving` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
