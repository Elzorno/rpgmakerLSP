# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SND-003.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map011.json`

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
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-SND-003 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=9 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map011.json |
| found | Map Shape | `MAP-002` | Map ID 11 | map_id=11 |
| found | Map Shape | `MAP-003` | Width 27 | width=27 |
| found | Map Shape | `MAP-004` | Height 23 | height=23 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=3726 |
| found | Map Shape | `MAP-006` | Display name Sealed Node Guardian Chamber | displayName=Sealed Node Guardian Chamber |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-SND-003-001 |
| found | Transfer Anchors | `TRN-HOM-022` | Event `TRN-HOM-022 Return to core path` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-022-POS` | `TRN-HOM-022 Return to core path` at (13, 22) | actual=(13, 22) |
| found | Transfer Anchors | `TRN-HOM-022-TRACE` | `TRN-HOM-022 Return to core path` preserves TRN-HOM-022 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-022-TILE` | `TRN-HOM-022 Return to core path` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-023` | Event `TRN-HOM-023 Enter relay core` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-023-POS` | `TRN-HOM-023 Enter relay core` at (13, 0) | actual=(13, 0) |
| found | Transfer Anchors | `TRN-HOM-023-TRACE` | `TRN-HOM-023 Enter relay core` preserves TRN-HOM-023 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-023-TILE` | `TRN-HOM-023 Enter relay core` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-021` | Event `Node Seven Guardian` exists | event exists |
| found | Event Anchors | `EVT-HOM-021-POS` | `Node Seven Guardian` at (13, 11) | actual=(13, 11) |
| found | Event Anchors | `EVT-HOM-021-TRACE` | `Node Seven Guardian` preserves EVT-HOM-021 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-021-TILE` | `Node Seven Guardian` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
