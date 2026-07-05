# BUILD-0013 - Generate Hidden Cave Trials Blueprint and Map

## Summary

BUILD-0013 created the engine-independent Atlas blueprint for `SCR-HOM-HCV-002` and generated the clean RPG Maker MZ `DGN_HiddenCave_Trials` map from it.

The generated map preserves the executable event logic already present in the clean skeleton while moving the trial, transfer, and gate anchors to blueprint coordinates. It also adds the local helper anchors required by `ATLAS-TEC-057` for Body reset tiles and Mind marker interactions.

## Files Inspected

- `../TheLastSwordProtocol-Atlas/atlas/docs/02_World/Screens/Home_Island/SCR_HOM_HCV_002_Hidden_Cave_Trials.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Trial_Specs/Home_Island/Home_Island_Trial_Mechanics_Spec.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Event_Specs/Home_Island/Home_Island_Executable_Event_Specs.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Asset_Mapping/Home_Island_Tileset_Assignment_Matrix.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Registries/Home_Island_Event_Registry.md`
- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-001.blueprint.json`
- `tools/atlas-import/generate_map_from_blueprint.py`
- `tools/atlas-import/audit_blueprint_round_trip.py`
- `../TheLastSwordProtocol-Game/data/Map006.json`

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-002.blueprint.json`
- `reports/atlas-import/build-0013-hidden-cave-trials-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0013-hidden-cave-entrance-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0013-skyreach-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0013-ashford-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0013-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0013-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0013-hidden-cave-trials-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `../TheLastSwordProtocol-Game/data/Map006.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-HCV-002-001`
- Atlas screen: `SCR-HOM-HCV-002`
- RPG Maker target: `DGN_HiddenCave_Trials`
- Dimensions: `40 x 32`
- Encounter policy: no random encounters
- Region policy: Region 5 safe/story zone
- Transfers:
  - `TRN-HOM-012` return to Hidden Cave Entrance at `(20, 31)`
  - `TRN-HOM-013` gated Sword Sanctum entry at `(20, 0)`
- Main anchors:
  - `EVT-HOM-012` Body Trial at `(12, 20)`
  - `EVT-HOM-013` Mind Trial at `(20, 16)`
  - `EVT-HOM-014` Heart Trial at `(31, 20)`
  - `EVT-HOM-015` Sanctum Gate at `(20, 6)`
- Helper anchors:
  - `EVT-HOM-012A/B/C` Body reset tiles
  - `EVT-HOM-013A/B/C` Mind marker tiles

## Commands Run

```bash
/usr/bin/python3 -m py_compile tools/atlas-import/generate_map_from_blueprint.py tools/atlas-import/audit_blueprint_round_trip.py tools/atlas-import/audit_vertical_slice_playthrough.py tools/atlas-import/audit_rpgmaker_data.py tools/atlas-import/validate_atlas_export.py
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-002.blueprint.json
/usr/bin/python3 tools/atlas-import/generate_map_from_blueprint.py --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-002.blueprint.json
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0013-hidden-cave-trials-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-002.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0013-hidden-cave-entrance-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0013-skyreach-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SKY-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_blueprint_round_trip.py reports/atlas-import/build-0013-ashford-regression-blueprint-round-trip-audit.md --blueprint ../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-001.blueprint.json --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_vertical_slice_playthrough.py reports/atlas-import/build-0013-vertical-slice-playthrough-audit.md --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_rpgmaker_data.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json reports/atlas-import/build-0013-clean-skeleton-data-audit.md --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/validate_atlas_export.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Game/data/Map006.json
/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Game/data/MapInfos.json
/usr/bin/python3 ../TheLastSwordProtocol-Atlas/atlas-tools/cli/atlas.py validate
```

## Validation Result

- Hidden Cave Trials round-trip audit: found 61, missing 0, warning 0
- Hidden Cave Entrance regression audit: found 29, missing 0, warning 0
- Skyreach regression audit: found 29, missing 0, warning 0
- Ashford regression audit: found 73, missing 0, warning 0
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No RPG Maker project files outside `data/Map006.json` were modified.
- Existing executable event pages for Body Trial, Mind Trial, Heart Trial, Sanctum Gate, and both transfers were preserved.
- The newly created Body reset and Mind marker helper events are blueprint anchors with placeholder pages. Full helper command logic remains a later implementation task unless explicitly required by the next build order.
