# BUILD-0014 - Generate Sword Sanctum Blueprint and Map

## Summary

BUILD-0014 created the engine-independent Atlas blueprint for `SCR-HOM-HCV-003` and generated the clean RPG Maker MZ `DGN_HiddenCave_Sanctum` map from it.

The generated map preserves the existing Sword Pedestal and return transfer event pages while moving them to blueprint coordinates and resizing the map to the Atlas-specified sanctum dimensions.

## Files Inspected

- `../TheLastSwordProtocol-Atlas/atlas/docs/02_World/Screens/Home_Island/SCR_HOM_HCV_003_Sword_Sanctum.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Event_Specs/Home_Island/Home_Island_Executable_Event_Specs.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Registries/Home_Island_Transfer_Registry.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Registries/Home_Island_Event_Registry.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Asset_Mapping/Home_Island_Tileset_Assignment_Matrix.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Asset_Mapping/Home_Island_Animation_Assignment_Matrix.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Implementation_Packets/Home_Island/IMP_HOM_003_Build_Sword_Awakening_Sequence.md`
- `tools/atlas-import/generate_map_from_blueprint.py`
- `tools/atlas-import/audit_blueprint_round_trip.py`
- `../TheLastSwordProtocol-Game/data/Map007.json`

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-003.blueprint.json`
- `reports/atlas-import/build-0014-sword-sanctum-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0014-hidden-cave-trials-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0014-hidden-cave-entrance-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0014-skyreach-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0014-ashford-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0014-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0014-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0014-sword-sanctum-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `../TheLastSwordProtocol-Game/data/Map007.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-HCV-003-001`
- Atlas screen: `SCR-HOM-HCV-003`
- RPG Maker target: `DGN_HiddenCave_Sanctum`
- Dimensions: `23 x 19`
- Encounter policy: no random encounters
- Region policy: Region 5 safe/story zone
- Transfer:
  - `TRN-HOM-014` return to Hidden Cave Trials at `(11, 18)`
- Main anchor:
  - `EVT-HOM-016` Sword Pedestal at `(11, 8)`

## Commands Run

```bash
/usr/bin/python3 -m py_compile tools/atlas-import/generate_map_from_blueprint.py tools/atlas-import/audit_blueprint_round_trip.py tools/atlas-import/audit_vertical_slice_playthrough.py tools/atlas-import/audit_rpgmaker_data.py tools/atlas-import/validate_atlas_export.py
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-003.blueprint.json
/usr/bin/python3 tools/atlas-import/generate_map_from_blueprint.py --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-003.blueprint.json
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0014-sword-sanctum-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-003.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0014-hidden-cave-trials-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-002.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0014-hidden-cave-entrance-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0014-skyreach-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SKY-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0014-ashford-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_vertical_slice_playthrough.py reports/atlas-import/build-0014-vertical-slice-playthrough-audit.md --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_rpgmaker_data.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json reports/atlas-import/build-0014-clean-skeleton-data-audit.md --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/validate_atlas_export.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Game/data/Map007.json
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Game/data/MapInfos.json
/usr/bin/python3 ../TheLastSwordProtocol-Atlas/atlas-tools/cli/atlas.py validate
```

## Validation Result

- Sword Sanctum round-trip audit: found 21, missing 0, warning 0
- Hidden Cave Trials regression audit: found 61, missing 0, warning 0
- Hidden Cave Entrance regression audit: found 29, missing 0, warning 0
- Skyreach regression audit: found 29, missing 0, warning 0
- Ashford regression audit: found 73, missing 0, warning 0
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No RPG Maker project files outside `data/Map007.json` were modified.
- The existing Sword Pedestal event currently has two pages in the clean skeleton. This build order did not change event command logic or resolve the Atlas open design questions about exact Sword item form and protocol skill unlock timing.
- Runtime visual inspection in RPG Maker remains useful before treating generated map layout as final production geometry.
