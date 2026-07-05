# BUILD-0015 - Generate Glassfield Ruins Exterior Blueprint and Map

## Summary

BUILD-0015 created the engine-independent Atlas blueprint for `SCR-HOM-GLS-001` and generated the clean RPG Maker MZ `DGN_Glassfield_Ruins_Exterior` map from it.

The generated map preserves the existing Glassfield Seal, Surface Fragment, return transfer, and Sealed Node transfer event pages while moving them to blueprint coordinates. It also applies the Atlas encounter policy for optional low-risk Home Field encounters plus a safe Region 5 zone around the sealed entrance.

## Files Inspected

- `../TheLastSwordProtocol-Atlas/atlas/docs/02_World/Screens/Home_Island/SCR_HOM_GLS_001_Glassfield_Ruins_Exterior.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Flow/Home_Island_Screen_Flow.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Registries/Home_Island_Screen_Registry.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Registries/Home_Island_Transfer_Registry.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Registries/Home_Island_Event_Registry.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Event_Specs/Home_Island/Home_Island_Executable_Event_Specs.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Asset_Mapping/Home_Island_Tileset_Assignment_Matrix.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Database_Specs/Home_Island/Home_Island_Combat_Database_Spec.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Implementation_Packets/Home_Island/IMP_HOM_012_Build_Glassfield_And_Sealed_Node_Screens.md`
- `tools/atlas-import/generate_map_from_blueprint.py`
- `tools/atlas-import/audit_blueprint_round_trip.py`
- `../TheLastSwordProtocol-Game/data/Map008.json`

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-GLS-001.blueprint.json`
- `reports/atlas-import/build-0015-glassfield-ruins-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0015-sword-sanctum-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0015-hidden-cave-trials-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0015-hidden-cave-entrance-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0015-skyreach-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0015-ashford-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0015-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0015-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0015-glassfield-ruins-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `../TheLastSwordProtocol-Game/data/Map008.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-GLS-001-001`
- Atlas screen: `SCR-HOM-GLS-001`
- RPG Maker target: `DGN_Glassfield_Ruins_Exterior`
- Dimensions: `42 x 34`
- Encounter policy: optional Home Field encounters, troop 1 and troop 3
- Region policy:
  - Region 1 exterior encounter field
  - Region 5 sealed entrance safe zone
- Transfers:
  - `TRN-HOM-016` return to Ashford-side island route at `(0, 26)`
  - `TRN-HOM-017` enter Sealed Node at `(22, 1)`, gated by `J1_Glassfield_SealOpened`
- Main anchors:
  - `EVT-HOM-017` Glassfield Seal at `(22, 5)`
  - `EVT-HOM-018` Surface Fragment at `(12, 18)`

## Commands Run

```bash
/usr/bin/python3 -m py_compile tools/atlas-import/generate_map_from_blueprint.py tools/atlas-import/audit_blueprint_round_trip.py tools/atlas-import/audit_vertical_slice_playthrough.py tools/atlas-import/audit_rpgmaker_data.py tools/atlas-import/validate_atlas_export.py
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-GLS-001.blueprint.json
/usr/bin/python3 tools/atlas-import/generate_map_from_blueprint.py --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-GLS-001.blueprint.json
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0015-glassfield-ruins-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-GLS-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0015-sword-sanctum-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-003.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0015-hidden-cave-trials-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-002.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0015-hidden-cave-entrance-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0015-skyreach-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SKY-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0015-ashford-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_vertical_slice_playthrough.py reports/atlas-import/build-0015-vertical-slice-playthrough-audit.md --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_rpgmaker_data.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json reports/atlas-import/build-0015-clean-skeleton-data-audit.md --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/validate_atlas_export.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Game/data/Map008.json
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Game/data/MapInfos.json
/usr/bin/python3 ../TheLastSwordProtocol-Atlas/atlas-tools/cli/atlas.py validate
```

## Validation Result

- Glassfield Ruins round-trip audit: found 29, missing 0, warning 0
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

- No RPG Maker project files outside `data/Map008.json` were modified.
- Existing event command pages were preserved; this order generated map layout, region policy, and anchor placement only.
- Runtime visual inspection in RPG Maker remains useful before treating generated map layout as final production geometry.
