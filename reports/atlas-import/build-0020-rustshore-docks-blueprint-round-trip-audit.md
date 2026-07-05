# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-RST-001.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map013.json`

## Summary

- Found: 33
- Missing: 0
- Present with warning: 0
- Total findings: 33

## Category Summary

| Category | Found | Missing | Warning |
|---|---:|---:|---:|
| Blueprint Contract | 3 | 0 | 0 |
| Encounter Policy | 3 | 0 | 0 |
| Event Anchors | 12 | 0 | 0 |
| Map Shape | 7 | 0 | 0 |
| Transfer Anchors | 8 | 0 | 0 |

## Findings

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-RST-001 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=10 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map013.json |
| found | Map Shape | `MAP-002` | Map ID 13 | map_id=13 |
| found | Map Shape | `MAP-003` | Width 34 | width=34 |
| found | Map Shape | `MAP-004` | Height 26 | height=26 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=5304 |
| found | Map Shape | `MAP-006` | Display name Rustshore Docks | displayName=Rustshore Docks |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-RST-001-001 |
| found | Transfer Anchors | `TRN-HOM-008` | Event `TRN-HOM-008 Return from Rustshore route` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-008-POS` | `TRN-HOM-008 Return from Rustshore route` at (0, 18) | actual=(0, 18) |
| found | Transfer Anchors | `TRN-HOM-008-TRACE` | `TRN-HOM-008 Return from Rustshore route` preserves TRN-HOM-008 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-008-TILE` | `TRN-HOM-008 Return from Rustshore route` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-025` | Event `TRN-HOM-025 Begin departure` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-025-POS` | `TRN-HOM-025 Begin departure` at (30, 14) | actual=(30, 14) |
| found | Transfer Anchors | `TRN-HOM-025-TRACE` | `TRN-HOM-025 Begin departure` preserves TRN-HOM-025 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-025-TILE` | `TRN-HOM-025 Begin departure` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-023` | Event `Dockmaster` exists | event exists |
| found | Event Anchors | `EVT-HOM-023-POS` | `Dockmaster` at (17, 13) | actual=(17, 13) |
| found | Event Anchors | `EVT-HOM-023-TRACE` | `Dockmaster` preserves EVT-HOM-023 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-023-TILE` | `Dockmaster` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-024` | Event `Lighthouse Examine` exists | event exists |
| found | Event Anchors | `EVT-HOM-024-POS` | `Lighthouse Examine` at (7, 9) | actual=(7, 9) |
| found | Event Anchors | `EVT-HOM-024-TRACE` | `Lighthouse Examine` preserves EVT-HOM-024 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-024-TILE` | `Lighthouse Examine` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-025` | Event `Boat Transfer` exists | event exists |
| found | Event Anchors | `EVT-HOM-025-POS` | `Boat Transfer` at (28, 14) | actual=(28, 14) |
| found | Event Anchors | `EVT-HOM-025-TRACE` | `Boat Transfer` preserves EVT-HOM-025 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-025-TILE` | `Boat Transfer` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=0 encounter=0 none=1 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
