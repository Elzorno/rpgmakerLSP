# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-003.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map003.json`

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
| Event Anchors | 8 | 0 | 0 |
| Map Shape | 7 | 0 | 0 |
| Transfer Anchors | 4 | 0 | 0 |

## Findings

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-ASH-003 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=7 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map003.json |
| found | Map Shape | `MAP-002` | Map ID 3 | map_id=3 |
| found | Map Shape | `MAP-003` | Width 17 | width=17 |
| found | Map Shape | `MAP-004` | Height 13 | height=13 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=1326 |
| found | Map Shape | `MAP-006` | Display name Ashford Shop Interior | displayName=Ashford Shop Interior |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-ASH-003-001 |
| found | Transfer Anchors | `TRN-HOM-004` | Event `TRN-HOM-004 Shop exit` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-004-POS` | `TRN-HOM-004 Shop exit` at (8, 12) | actual=(8, 12) |
| found | Transfer Anchors | `TRN-HOM-004-TRACE` | `TRN-HOM-004 Shop exit` preserves TRN-HOM-004 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-004-TILE` | `TRN-HOM-004 Shop exit` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-008` | Event `Shopkeeper` exists | event exists |
| found | Event Anchors | `EVT-HOM-008-POS` | `Shopkeeper` at (8, 5) | actual=(8, 5) |
| found | Event Anchors | `EVT-HOM-008-TRACE` | `Shopkeeper` preserves EVT-HOM-008 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-008-TILE` | `Shopkeeper` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `INT-ASH-SHOP-CABINET` | Event `INT-ASH-SHOP-CABINET Metal Cabinet` exists | event exists |
| found | Event Anchors | `INT-ASH-SHOP-CABINET-POS` | `INT-ASH-SHOP-CABINET Metal Cabinet` at (12, 4) | actual=(12, 4) |
| found | Event Anchors | `INT-ASH-SHOP-CABINET-TRACE` | `INT-ASH-SHOP-CABINET Metal Cabinet` preserves INT-ASH-SHOP-CABINET | Atlas ID present in name, note, or comments |
| found | Event Anchors | `INT-ASH-SHOP-CABINET-TILE` | `INT-ASH-SHOP-CABINET Metal Cabinet` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=0 encounter=0 none=1 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
