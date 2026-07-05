# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-GLS-001.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map008.json`

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
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-GLS-001 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=10 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map008.json |
| found | Map Shape | `MAP-002` | Map ID 8 | map_id=8 |
| found | Map Shape | `MAP-003` | Width 42 | width=42 |
| found | Map Shape | `MAP-004` | Height 34 | height=34 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=8568 |
| found | Map Shape | `MAP-006` | Display name Glassfield Ruins Exterior | displayName=Glassfield Ruins Exterior |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-GLS-001-001 |
| found | Transfer Anchors | `TRN-HOM-016` | Event `TRN-HOM-016 Return from Glassfield` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-016-POS` | `TRN-HOM-016 Return from Glassfield` at (0, 26) | actual=(0, 26) |
| found | Transfer Anchors | `TRN-HOM-016-TRACE` | `TRN-HOM-016 Return from Glassfield` preserves TRN-HOM-016 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-016-TILE` | `TRN-HOM-016 Return from Glassfield` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-017` | Event `TRN-HOM-017 Enter Sealed Node` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-017-POS` | `TRN-HOM-017 Enter Sealed Node` at (22, 1) | actual=(22, 1) |
| found | Transfer Anchors | `TRN-HOM-017-TRACE` | `TRN-HOM-017 Enter Sealed Node` preserves TRN-HOM-017 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-017-TILE` | `TRN-HOM-017 Enter Sealed Node` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-017` | Event `Glassfield Seal` exists | event exists |
| found | Event Anchors | `EVT-HOM-017-POS` | `Glassfield Seal` at (22, 5) | actual=(22, 5) |
| found | Event Anchors | `EVT-HOM-017-TRACE` | `Glassfield Seal` preserves EVT-HOM-017 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-017-TILE` | `Glassfield Seal` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-018` | Event `Surface Fragment` exists | event exists |
| found | Event Anchors | `EVT-HOM-018-POS` | `Surface Fragment` at (12, 18) | actual=(12, 18) |
| found | Event Anchors | `EVT-HOM-018-TRACE` | `Surface Fragment` preserves EVT-HOM-018 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-018-TILE` | `Surface Fragment` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=1 none=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[{'regionSet': [1], 'troopId': 1, 'weight': 4}, {'regionSet': [1], 'troopId': 3, 'weight': 3}] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[1, 5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
