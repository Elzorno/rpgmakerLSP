# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SND-004.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map012.json`

## Summary

- Found: 21
- Missing: 0
- Present with warning: 0
- Total findings: 21

## Category Summary

| Category | Found | Missing | Warning |
|---|---:|---:|---:|
| Blueprint Contract | 3 | 0 | 0 |
| Encounter Policy | 3 | 0 | 0 |
| Event Anchors | 4 | 0 | 0 |
| Map Shape | 7 | 0 | 0 |
| Transfer Anchors | 4 | 0 | 0 |

## Findings

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-SND-004 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=8 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map012.json |
| found | Map Shape | `MAP-002` | Map ID 12 | map_id=12 |
| found | Map Shape | `MAP-003` | Width 23 | width=23 |
| found | Map Shape | `MAP-004` | Height 19 | height=19 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=2622 |
| found | Map Shape | `MAP-006` | Display name Relay Node Seven Core | displayName=Relay Node Seven Core |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-SND-004-001 |
| found | Transfer Anchors | `TRN-HOM-024` | Event `TRN-HOM-024 Return from relay core` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-024-POS` | `TRN-HOM-024 Return from relay core` at (11, 18) | actual=(11, 18) |
| found | Transfer Anchors | `TRN-HOM-024-TRACE` | `TRN-HOM-024 Return from relay core` preserves TRN-HOM-024 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-024-TILE` | `TRN-HOM-024 Return from relay core` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-022` | Event `Relay Core` exists | event exists |
| found | Event Anchors | `EVT-HOM-022-POS` | `Relay Core` at (11, 8) | actual=(11, 8) |
| found | Event Anchors | `EVT-HOM-022-TRACE` | `Relay Core` preserves EVT-HOM-022 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-022-TILE` | `Relay Core` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
