# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SKY-001.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map004.json`

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
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-SKY-001 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=8 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map004.json |
| found | Map Shape | `MAP-002` | Map ID 4 | map_id=4 |
| found | Map Shape | `MAP-003` | Width 30 | width=30 |
| found | Map Shape | `MAP-004` | Height 40 | height=40 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=7200 |
| found | Map Shape | `MAP-006` | Display name Skyreach Hill Path | displayName=Skyreach Hill Path |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-SKY-001-001 |
| found | Transfer Anchors | `TRN-HOM-006` | Event `TRN-HOM-006 Return from Skyreach route` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-006-POS` | `TRN-HOM-006 Return from Skyreach route` at (15, 39) | actual=(15, 39) |
| found | Transfer Anchors | `TRN-HOM-006-TRACE` | `TRN-HOM-006 Return from Skyreach route` preserves TRN-HOM-006 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-006-TILE` | `TRN-HOM-006 Return from Skyreach route` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-009` | Event `TRN-HOM-009 Enter Hidden Cave` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-009-POS` | `TRN-HOM-009 Enter Hidden Cave` at (15, 1) | actual=(15, 1) |
| found | Transfer Anchors | `TRN-HOM-009-TRACE` | `TRN-HOM-009 Enter Hidden Cave` preserves TRN-HOM-009 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-009-TILE` | `TRN-HOM-009 Enter Hidden Cave` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-010` | Event `Skyreach Gate` exists | event exists |
| found | Event Anchors | `EVT-HOM-010-POS` | `Skyreach Gate` at (15, 9) | actual=(15, 9) |
| found | Event Anchors | `EVT-HOM-010-TRACE` | `Skyreach Gate` preserves EVT-HOM-010 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-010-TILE` | `Skyreach Gate` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `INT-SKY-GEOMETRIC-STONES` | Event `INT-SKY-GEOMETRIC-STONES Geometric Stones` exists | event exists |
| found | Event Anchors | `INT-SKY-GEOMETRIC-STONES-POS` | `INT-SKY-GEOMETRIC-STONES Geometric Stones` at (20, 17) | actual=(20, 17) |
| found | Event Anchors | `INT-SKY-GEOMETRIC-STONES-TRACE` | `INT-SKY-GEOMETRIC-STONES Geometric Stones` preserves INT-SKY-GEOMETRIC-STONES | Atlas ID present in name, note, or comments |
| found | Event Anchors | `INT-SKY-GEOMETRIC-STONES-TILE` | `INT-SKY-GEOMETRIC-STONES Geometric Stones` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=1 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[{'regionSet': [1], 'troopId': 1, 'weight': 5}, {'regionSet': [1], 'troopId': 2, 'weight': 4}, {'regionSet': [1], 'troopId': 3, 'weight': 3}] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[1, 5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
