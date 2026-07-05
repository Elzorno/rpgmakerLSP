# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-FOG-001.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map015.json`

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
| Event Anchors | 8 | 0 | 0 |
| Map Shape | 7 | 0 | 0 |
| Transfer Anchors | 8 | 0 | 0 |
| Treasure Anchors | 4 | 0 | 0 |

## Findings

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-FOG-001 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=8 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map015.json |
| found | Map Shape | `MAP-002` | Map ID 15 | map_id=15 |
| found | Map Shape | `MAP-003` | Width 40 | width=40 |
| found | Map Shape | `MAP-004` | Height 32 | height=32 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=7680 |
| found | Map Shape | `MAP-006` | Display name Fogfen Marsh Field | displayName=Fogfen Marsh Field |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-FOG-001-001 |
| found | Transfer Anchors | `TRN-HOM-028` | Event `TRN-HOM-028 Return from Fogfen to Ashford-side route` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-028-POS` | `TRN-HOM-028 Return from Fogfen to Ashford-side route` at (0, 26) | actual=(0, 26) |
| found | Transfer Anchors | `TRN-HOM-028-TRACE` | `TRN-HOM-028 Return from Fogfen to Ashford-side route` preserves TRN-HOM-028 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-028-TILE` | `TRN-HOM-028 Return from Fogfen to Ashford-side route` has a concrete tile | layer0 tile=2836 |
| found | Transfer Anchors | `TRN-HOM-029` | Event `TRN-HOM-029 Optional deeper marsh branch` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-029-POS` | `TRN-HOM-029 Optional deeper marsh branch` at (39, 8) | actual=(39, 8) |
| found | Transfer Anchors | `TRN-HOM-029-TRACE` | `TRN-HOM-029 Optional deeper marsh branch` preserves TRN-HOM-029 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-029-TILE` | `TRN-HOM-029 Optional deeper marsh branch` has a concrete tile | layer0 tile=2836 |
| found | Treasure Anchors | `EVT-HOM-028` | Event `Hidden Item Landmark` exists | event exists |
| found | Treasure Anchors | `EVT-HOM-028-POS` | `Hidden Item Landmark` at (12, 22) | actual=(12, 22) |
| found | Treasure Anchors | `EVT-HOM-028-TRACE` | `Hidden Item Landmark` preserves EVT-HOM-028 | Atlas ID present in name, note, or comments |
| found | Treasure Anchors | `EVT-HOM-028-TILE` | `Hidden Item Landmark` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-027` | Event `Fogfen Entry / Exit Transfer` exists | event exists |
| found | Event Anchors | `EVT-HOM-027-POS` | `Fogfen Entry / Exit Transfer` at (2, 26) | actual=(2, 26) |
| found | Event Anchors | `EVT-HOM-027-TRACE` | `Fogfen Entry / Exit Transfer` preserves EVT-HOM-027 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-027-TILE` | `Fogfen Entry / Exit Transfer` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-029` | Event `Signal-Tick Reed Pool` exists | event exists |
| found | Event Anchors | `EVT-HOM-029-POS` | `Signal-Tick Reed Pool` at (26, 12) | actual=(26, 12) |
| found | Event Anchors | `EVT-HOM-029-TRACE` | `Signal-Tick Reed Pool` preserves EVT-HOM-029 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-029-TILE` | `Signal-Tick Reed Pool` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=2 encounter=2 none=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[{'regionSet': [2], 'troopId': 4, 'weight': 5}, {'regionSet': [2], 'troopId': 5, 'weight': 4}] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[2, 3, 5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
