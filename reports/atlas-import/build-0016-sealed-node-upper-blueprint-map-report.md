# BUILD-0016 - Generate Sealed Node Upper Blueprint and Map

## Summary

BUILD-0016 created the engine-independent Atlas blueprint for `SCR-HOM-SND-001` and generated the clean RPG Maker MZ `DGN_SealedNode_Upper` map from it.

The generated map preserves the existing Sealed Node First Entry event, return transfer, and forward transfer event pages while moving them to blueprint coordinates. This order also extended the blueprint exporter and audit tooling to support Atlas Region 4 node encounter zones.

## Files Inspected

- `../TheLastSwordProtocol-Atlas/atlas/docs/02_World/Screens/Home_Island/SCR_HOM_SND_001_Sealed_Node_Upper.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Asset_Mapping/Home_Island_Tileset_Assignment_Matrix.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Event_Specs/Home_Island/Home_Island_Executable_Event_Specs.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Implementation_Packets/Home_Island/IMP_HOM_012_Build_Glassfield_And_Sealed_Node_Screens.md`
- `tools/atlas-import/generate_map_from_blueprint.py`
- `tools/atlas-import/audit_blueprint_round_trip.py`
- `../TheLastSwordProtocol-Game/data/Map009.json`

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SND-001.blueprint.json`
- `reports/atlas-import/build-0016-sealed-node-upper-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0016-glassfield-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0016-sword-sanctum-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0016-hidden-cave-trials-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0016-hidden-cave-entrance-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0016-skyreach-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0016-ashford-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0016-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0016-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0016-sealed-node-upper-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `tools/atlas-import/audit_blueprint_round_trip.py`
- `../TheLastSwordProtocol-Game/data/Map009.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-SND-001-001`
- Atlas screen: `SCR-HOM-SND-001`
- RPG Maker target: `DGN_SealedNode_Upper`
- Dimensions: `34 x 30`
- Encounter policy: optional low-frequency node encounters, troop 1 and troop 2
- Region policy:
  - Region 4 node encounter corridor
  - Region 5 first-entry/return safe zone
- Transfers:
  - `TRN-HOM-018` return to Glassfield at `(17, 29)`
  - `TRN-HOM-019` proceed to Sealed Node Core Path at `(17, 1)`
- Main anchor:
  - `EVT-HOM-019` Sealed Node First Entry at `(17, 25)`

## Commands Run

```bash
/usr/bin/python3 -m py_compile tools/atlas-import/generate_map_from_blueprint.py tools/atlas-import/audit_blueprint_round_trip.py tools/atlas-import/audit_vertical_slice_playthrough.py tools/atlas-import/audit_rpgmaker_data.py tools/atlas-import/validate_atlas_export.py
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SND-001.blueprint.json
/usr/bin/python3 tools/atlas-import/generate_map_from_blueprint.py --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SND-001.blueprint.json
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0016-sealed-node-upper-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SND-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0016-glassfield-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-GLS-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0016-sword-sanctum-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-003.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0016-hidden-cave-trials-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-002.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0016-hidden-cave-entrance-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0016-skyreach-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SKY-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0016-ashford-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_vertical_slice_playthrough.py reports/atlas-import/build-0016-vertical-slice-playthrough-audit.md --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_rpgmaker_data.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json reports/atlas-import/build-0016-clean-skeleton-data-audit.md --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/validate_atlas_export.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Game/data/Map009.json
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Game/data/MapInfos.json
/usr/bin/python3 ../TheLastSwordProtocol-Atlas/atlas-tools/cli/atlas.py validate
```

## Validation Result

- Sealed Node Upper round-trip audit: found 25, missing 0, warning 0
- Glassfield regression audit: found 29, missing 0, warning 0
- Sword Sanctum regression audit: found 21, missing 0, warning 0
- Hidden Cave Trials regression audit: found 61, missing 0, warning 0
- Hidden Cave Entrance regression audit: found 29, missing 0, warning 0
- Skyreach regression audit: found 29, missing 0, warning 0
- Ashford regression audit: found 73, missing 0, warning 0
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No RPG Maker project files outside `data/Map009.json` were modified.
- The exporter and round-trip audit now support `node_encounter` blueprint regions, which export to RPG Maker Region 4 per the Home Island tileset matrix.
- Existing event command pages were preserved; this order generated map layout, region policy, and anchor placement only.
