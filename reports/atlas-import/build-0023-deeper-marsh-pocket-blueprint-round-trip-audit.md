# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-FOG-002.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map016.json`

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
| Transfer Anchors | 4 | 0 | 0 |
| Treasure Anchors | 4 | 0 | 0 |

## Findings

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-FOG-002 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=8 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map016.json |
| found | Map Shape | `MAP-002` | Map ID 16 | map_id=16 |
| found | Map Shape | `MAP-003` | Width 24 | width=24 |
| found | Map Shape | `MAP-004` | Height 20 | height=20 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=2880 |
| found | Map Shape | `MAP-006` | Display name Deeper Marsh Pocket | displayName=Deeper Marsh Pocket |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-FOG-002-001 |
| found | Transfer Anchors | `TRN-HOM-030` | Event `TRN-HOM-030 Return from deeper marsh pocket` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-030-POS` | `TRN-HOM-030 Return from deeper marsh pocket` at (0, 15) | actual=(0, 15) |
| found | Transfer Anchors | `TRN-HOM-030-TRACE` | `TRN-HOM-030 Return from deeper marsh pocket` preserves TRN-HOM-030 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-030-TILE` | `TRN-HOM-030 Return from deeper marsh pocket` has a concrete tile | layer0 tile=2836 |
| found | Treasure Anchors | `OBJ-HOM-FOG-009` | Event `Deeper Marsh Reward Cache` exists | event exists |
| found | Treasure Anchors | `OBJ-HOM-FOG-009-POS` | `Deeper Marsh Reward Cache` at (8, 13) | actual=(8, 13) |
| found | Treasure Anchors | `OBJ-HOM-FOG-009-TRACE` | `Deeper Marsh Reward Cache` preserves OBJ-HOM-FOG-009 | Atlas ID present in name, note, or comments |
| found | Treasure Anchors | `OBJ-HOM-FOG-009-TILE` | `Deeper Marsh Reward Cache` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-030` | Event `Deeper Marsh Return Transfer` exists | event exists |
| found | Event Anchors | `EVT-HOM-030-POS` | `Deeper Marsh Return Transfer` at (2, 15) | actual=(2, 15) |
| found | Event Anchors | `EVT-HOM-030-TRACE` | `Deeper Marsh Return Transfer` preserves EVT-HOM-030 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-030-TILE` | `Deeper Marsh Return Transfer` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-031` | Event `Signal Pool / Cable Cluster Examine` exists | event exists |
| found | Event Anchors | `EVT-HOM-031-POS` | `Signal Pool / Cable Cluster Examine` at (14, 9) | actual=(14, 9) |
| found | Event Anchors | `EVT-HOM-031-TRACE` | `Signal Pool / Cable Cluster Examine` preserves EVT-HOM-031 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-031-TILE` | `Signal Pool / Cable Cluster Examine` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=2 none=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[{'regionSet': [2], 'troopId': 4, 'weight': 4}, {'regionSet': [2], 'troopId': 5, 'weight': 5}] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[2, 3, 5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
