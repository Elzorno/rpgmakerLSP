# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-002.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map002.json`

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
| Event Anchors | 12 | 0 | 0 |
| Map Shape | 7 | 0 | 0 |
| Transfer Anchors | 4 | 0 | 0 |

## Findings

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-ASH-002 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=7 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map002.json |
| found | Map Shape | `MAP-002` | Map ID 2 | map_id=2 |
| found | Map Shape | `MAP-003` | Width 17 | width=17 |
| found | Map Shape | `MAP-004` | Height 13 | height=13 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=1326 |
| found | Map Shape | `MAP-006` | Display name Elara House Interior | displayName=Elara House Interior |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-ASH-002-001 |
| found | Transfer Anchors | `TRN-HOM-001` | Event `TRN-HOM-001 Elara House exit` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-001-POS` | `TRN-HOM-001 Elara House exit` at (8, 12) | actual=(8, 12) |
| found | Transfer Anchors | `TRN-HOM-001-TRACE` | `TRN-HOM-001 Elara House exit` preserves TRN-HOM-001 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-001-TILE` | `TRN-HOM-001 Elara House exit` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-001` | Event `Player Start` exists | event exists |
| found | Event Anchors | `EVT-HOM-001-POS` | `Player Start` at (8, 6) | actual=(8, 6) |
| found | Event Anchors | `EVT-HOM-001-TRACE` | `Player Start` preserves EVT-HOM-001 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-001-TILE` | `Player Start` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-002` | Event `Elara Intro Dialogue` exists | event exists |
| found | Event Anchors | `EVT-HOM-002-POS` | `Elara Intro Dialogue` at (8, 4) | actual=(8, 4) |
| found | Event Anchors | `EVT-HOM-002-TRACE` | `Elara Intro Dialogue` preserves EVT-HOM-002 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-002-TILE` | `Elara Intro Dialogue` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `INT-ASH-ELARA-KEEPSAKE` | Event `INT-ASH-ELARA-KEEPSAKE Keepsake Shelf` exists | event exists |
| found | Event Anchors | `INT-ASH-ELARA-KEEPSAKE-POS` | `INT-ASH-ELARA-KEEPSAKE Keepsake Shelf` at (13, 4) | actual=(13, 4) |
| found | Event Anchors | `INT-ASH-ELARA-KEEPSAKE-TRACE` | `INT-ASH-ELARA-KEEPSAKE Keepsake Shelf` preserves INT-ASH-ELARA-KEEPSAKE | Atlas ID present in name, note, or comments |
| found | Event Anchors | `INT-ASH-ELARA-KEEPSAKE-TILE` | `INT-ASH-ELARA-KEEPSAKE Keepsake Shelf` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=0 encounter=0 none=1 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
