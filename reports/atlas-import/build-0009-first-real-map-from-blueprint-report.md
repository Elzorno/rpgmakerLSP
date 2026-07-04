# BUILD-0009 - Generate First Real Map From Atlas Blueprint

## Completed

- Corrected the mistakenly numbered Atlas record by marking `WO-0021 - Generate First Real Map From Atlas Blueprint` as superseded by `BUILD-0009`.
- Implemented a guarded RPG Maker MZ map generator at `tools/atlas-import/generate_map_from_blueprint.py`.
- Generated the first real Ashford Exterior map from the Atlas blueprint `BP-SCR-HOM-ASH-001-001`.
- Preserved existing executable event logic for current clean-skeleton Ashford events and transfers.
- Added missing blueprint placeholder anchors for the Village Elder, warm-stone vent, and old panel.
- Confirmed Ashford remains a safe/no-encounter village map.

## Files Inspected

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/README.md`
- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/blueprint_schema.md`
- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/layout_generator.md`
- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/object_placement.md`
- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/exporter_interface.md`
- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-001.blueprint.json`
- `../TheLastSwordProtocol-Atlas/atlas/docs/02_World/Screens/Home_Island/SCR_HOM_ASH_001_Ashford_Exterior.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Registries/Home_Island_Screen_Registry.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Registries/Home_Island_Transfer_Registry.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Registries/Home_Island_Event_Registry.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Asset_Mapping/Home_Island_Tileset_Assignment_Matrix.md`
- `../TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Event_Specs/Home_Island/Home_Island_Executable_Event_Specs.md`
- `../TheLastSwordProtocol-Game/data/MapInfos.json`
- `../TheLastSwordProtocol-Game/data/Map001.json`
- `../TheLastSwordProtocol-Game/data/Map002.json`
- `../TheLastSwordProtocol-Game/data/Tilesets.json`

## Files Created

- `tools/atlas-import/generate_map_from_blueprint.py`
- `reports/atlas-import/build-0009-first-real-map-from-blueprint-report.md`
- `reports/atlas-import/build-0009-vertical-slice-playthrough-audit.md`

## Files Modified

- `../TheLastSwordProtocol-Atlas/atlas/workorders/WO-0021-generate-first-real-map-from-atlas-blueprint.md`
- `../TheLastSwordProtocol-Game/data/Map001.json`
- `.agents/task-board.md`

## Source Blueprint

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-001.blueprint.json`
- Blueprint ID: `BP-SCR-HOM-ASH-001-001`
- Atlas screen: `SCR-HOM-ASH-001`

## Generated Map

- Target map: `../TheLastSwordProtocol-Game/data/Map001.json`
- Map ID: `1`
- Map name: `TWN_Ashford_Exterior`
- Display name: `Ashford Exterior`
- Dimensions: `40 x 32`
- Tileset: existing RPG Maker MZ tileset ID `2` / Atlas placeholder tileset `Outside`
- Encounter policy: no random encounters, `encounterList: []`

`Map001.json` was replaced safely without a backup because the prior map was a generated clean-skeleton placeholder for the same Atlas screen, not hand-authored production map data. Existing executable event pages were retained and moved to blueprint coordinates.

## Events Generated

Created placeholder events:

- `Village Elder Placeholder` at `(25, 15)`
- `INT-ASH-WARM-STONE-VENT Warm-Stone Vent` at `(9, 16)`
- `INT-ASH-OLD-PANEL Old Panel` at `(7, 9)`

Updated existing events while preserving executable command lists:

- `Child Near Old Panel` at `(7, 11)`
- `Farmer With Warm Stones` at `(11, 18)`
- `Skyreach Joker` at `(22, 5)`
- `Dock Messenger` at `(17, 25)`
- `Hidden Item` at `(9, 20)`
- `Tremor Trigger` at `(20, 9)`

## Transfer Anchors Generated

- `TRN-HOM-002 Enter Elara House` at `(17, 27)`
- `TRN-HOM-003 Enter Ashford Shop` at `(30, 18)`
- `TRN-HOM-005 North path to Skyreach` at `(20, 0)`
- `TRN-HOM-007 South/east route to Rustshore` at `(18, 31)`
- `TRN-HOM-015 Route to Glassfield` at `(39, 9)`
- `TRN-HOM-027 Optional east route to Fogfen Marsh Field` at `(39, 23)`

## Validation Result

- `/usr/bin/python3 -m py_compile tools/atlas-import/*.py` - PASS
- `/usr/bin/python3 tools/atlas-import/validate_atlas_export.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json` - PASS
- `/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Game/data/MapInfos.json` - PASS
- `/usr/bin/python3 -m json.tool ../TheLastSwordProtocol-Game/data/Map001.json` - PASS
- `/usr/bin/python3 ../TheLastSwordProtocol-Atlas/atlas-tools/cli/atlas.py validate` - PASS, 0 errors, 0 warnings
- `/usr/bin/python3 tools/atlas-import/audit_vertical_slice_playthrough.py reports/atlas-import/build-0009-vertical-slice-playthrough-audit.md --project-root ../TheLastSwordProtocol-Game` - PASS, found 81, missing 0, warning 0, not machine-checkable 1

## Remaining Limitations

- The generated layout is still placeholder-art based. It uses existing RPG Maker tileset IDs as an export detail, while Atlas remains engine-independent.
- Return transfers from other maps still land at their existing coordinates on the enlarged Ashford map. They remain valid, but a later placement polish pass should align inbound return coordinates with the new blueprint scale.
- The vertical-slice audit is JSON-based. Manual RPG Maker runtime playtest remains required for timing, feel, and visual inspection.

## Recommendation For Next Build Order

`BUILD-0010 - Atlas Blueprint Round-Trip Audit`: add a read-only audit that compares generated RPG Maker map geometry/events back against the source blueprint so future map generation can be verified without manual JSON inspection.
