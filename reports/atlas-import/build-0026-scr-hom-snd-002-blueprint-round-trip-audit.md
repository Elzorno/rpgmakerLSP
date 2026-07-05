# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SND-002.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map010.json`

## Summary

- Found: 25
- Missing: 0
- Present with warning: 0
- Total findings: 25

## Category Summary

| Category | Found | Missing | Warning |
|---|---:|---:|---:|
| Blueprint Contract | 3 | 0 | 0 |
| Encounter Policy | 3 | 0 | 0 |
| Event Anchors | 4 | 0 | 0 |
| Map Shape | 7 | 0 | 0 |
| Transfer Anchors | 8 | 0 | 0 |

## Findings

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-SND-002 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=9 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map010.json |
| found | Map Shape | `MAP-002` | Map ID 10 | map_id=10 |
| found | Map Shape | `MAP-003` | Width 38 | width=38 |
| found | Map Shape | `MAP-004` | Height 32 | height=32 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=7296 |
| found | Map Shape | `MAP-006` | Display name Sealed Node Core Path | displayName=Sealed Node Core Path |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-SND-002-001 |
| found | Transfer Anchors | `TRN-HOM-020` | Event `TRN-HOM-020 Return to upper node` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-020-POS` | `TRN-HOM-020 Return to upper node` at (19, 31) | actual=(19, 31) |
| found | Transfer Anchors | `TRN-HOM-020-TRACE` | `TRN-HOM-020 Return to upper node` preserves TRN-HOM-020 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-020-TILE` | `TRN-HOM-020 Return to upper node` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-021` | Event `TRN-HOM-021 Enter guardian chamber` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-021-POS` | `TRN-HOM-021 Enter guardian chamber` at (19, 1) | actual=(19, 1) |
| found | Transfer Anchors | `TRN-HOM-021-TRACE` | `TRN-HOM-021 Enter guardian chamber` preserves TRN-HOM-021 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-021-TILE` | `TRN-HOM-021 Enter guardian chamber` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-020` | Event `Core Path Door` exists | event exists |
| found | Event Anchors | `EVT-HOM-020-POS` | `Core Path Door` at (19, 13) | actual=(19, 13) |
| found | Event Anchors | `EVT-HOM-020-TRACE` | `Core Path Door` preserves EVT-HOM-020 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-020-TILE` | `Core Path Door` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=1 none=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[{'regionSet': [4], 'troopId': 1, 'weight': 3}, {'regionSet': [4], 'troopId': 2, 'weight': 2}] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[4, 5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
