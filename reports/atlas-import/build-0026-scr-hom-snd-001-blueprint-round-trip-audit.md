# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SND-001.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map009.json`

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
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-SND-001 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=9 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map009.json |
| found | Map Shape | `MAP-002` | Map ID 9 | map_id=9 |
| found | Map Shape | `MAP-003` | Width 34 | width=34 |
| found | Map Shape | `MAP-004` | Height 30 | height=30 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=6120 |
| found | Map Shape | `MAP-006` | Display name Sealed Node Upper | displayName=Sealed Node Upper |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-SND-001-001 |
| found | Transfer Anchors | `TRN-HOM-018` | Event `TRN-HOM-018 Exit Sealed Node` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-018-POS` | `TRN-HOM-018 Exit Sealed Node` at (17, 29) | actual=(17, 29) |
| found | Transfer Anchors | `TRN-HOM-018-TRACE` | `TRN-HOM-018 Exit Sealed Node` preserves TRN-HOM-018 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-018-TILE` | `TRN-HOM-018 Exit Sealed Node` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-019` | Event `TRN-HOM-019 Proceed deeper` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-019-POS` | `TRN-HOM-019 Proceed deeper` at (17, 1) | actual=(17, 1) |
| found | Transfer Anchors | `TRN-HOM-019-TRACE` | `TRN-HOM-019 Proceed deeper` preserves TRN-HOM-019 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-019-TILE` | `TRN-HOM-019 Proceed deeper` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-019` | Event `Sealed Node First Entry` exists | event exists |
| found | Event Anchors | `EVT-HOM-019-POS` | `Sealed Node First Entry` at (17, 25) | actual=(17, 25) |
| found | Event Anchors | `EVT-HOM-019-TRACE` | `Sealed Node First Entry` preserves EVT-HOM-019 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-019-TILE` | `Sealed Node First Entry` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=1 none=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[{'regionSet': [4], 'troopId': 1, 'weight': 3}, {'regionSet': [4], 'troopId': 2, 'weight': 2}] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[4, 5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
