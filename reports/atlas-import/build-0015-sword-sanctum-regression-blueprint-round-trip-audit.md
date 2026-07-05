# Atlas Blueprint Round-Trip Audit

This read-only audit compares the generated RPG Maker MZ map artifact back against its Atlas map blueprint.

- Blueprint: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-003.blueprint.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- RPG Maker map: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map007.json`

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
| found | Blueprint Contract | `BP-001` | Blueprint has Atlas screen ID | atlas_screen_id=SCR-HOM-HCV-003 |
| found | Blueprint Contract | `BP-002` | Blueprint contains no RPG Maker engine IDs | engine-specific keys=[] |
| found | Blueprint Contract | `BP-003` | Blueprint source documents are recorded | source_documents=10 |
| found | Map Shape | `MAP-001` | RPG Maker target map exists | /Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/data/Map007.json |
| found | Map Shape | `MAP-002` | Map ID 7 | map_id=7 |
| found | Map Shape | `MAP-003` | Width 23 | width=23 |
| found | Map Shape | `MAP-004` | Height 19 | height=19 |
| found | Map Shape | `MAP-005` | Six RPG Maker tile layers | data length=2622 |
| found | Map Shape | `MAP-006` | Display name Sword Sanctum | displayName=Sword Sanctum |
| found | Map Shape | `MAP-007` | Blueprint generation marker | note contains BP-SCR-HOM-HCV-003-001 |
| found | Transfer Anchors | `TRN-HOM-014` | Event `TRN-HOM-014 Return from sanctum` exists | event exists |
| found | Transfer Anchors | `TRN-HOM-014-POS` | `TRN-HOM-014 Return from sanctum` at (11, 18) | actual=(11, 18) |
| found | Transfer Anchors | `TRN-HOM-014-TRACE` | `TRN-HOM-014 Return from sanctum` preserves TRN-HOM-014 | Atlas ID present in name, note, or comments |
| found | Transfer Anchors | `TRN-HOM-014-TILE` | `TRN-HOM-014 Return from sanctum` has a concrete tile | layer0 tile=2836 |
| found | Event Anchors | `EVT-HOM-016` | Event `Sword Pedestal` exists | event exists |
| found | Event Anchors | `EVT-HOM-016-POS` | `Sword Pedestal` at (11, 8) | actual=(11, 8) |
| found | Event Anchors | `EVT-HOM-016-TRACE` | `Sword Pedestal` preserves EVT-HOM-016 | Atlas ID present in name, note, or comments |
| found | Event Anchors | `EVT-HOM-016-TILE` | `Sword Pedestal` has a concrete tile | layer0 tile=2836 |
| found | Encounter Policy | `ENC-001` | Blueprint declares region policy | safe=1 encounter=0 |
| found | Encounter Policy | `ENC-002` | RPG Maker encounter list matches exporter policy | encounterList=[] |
| found | Encounter Policy | `ENC-003` | RPG Maker region IDs match blueprint region types | nonzero region IDs=[5] |

## Notes

- This audit does not modify RPG Maker data files.
- Event-page command behavior is covered by the vertical-slice playthrough audit; this audit focuses on blueprint/map round-trip fidelity.
- `present with warning` is reserved for non-blocking differences that may be acceptable but should be reviewed before scaling generation to more maps.
