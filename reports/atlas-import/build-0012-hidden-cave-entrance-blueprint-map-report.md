# BUILD-0012 - Generate Hidden Cave Entrance Blueprint and Map

## Completed

- Created an engine-independent Atlas map blueprint for `SCR-HOM-HCV-001` / Hidden Cave Entrance.
- Extended the map generator to support Hidden Cave Entrance.
- Generated `Map005.json` from `BP-SCR-HOM-HCV-001-001`.
- Preserved executable first-entry and transfer event logic.
- Added an optional wall-carving examine placeholder from the screen specification.
- Refined safe-region export policy so Ashford remains Region 0 only while non-village safe staging maps can emit Region 5.

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-001.blueprint.json`
- `reports/atlas-import/build-0012-hidden-cave-entrance-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0012-skyreach-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0012-ashford-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0012-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0012-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0012-hidden-cave-entrance-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `tools/atlas-import/audit_blueprint_round_trip.py`
- `../TheLastSwordProtocol-Game/data/Map005.json`
- `.agents/task-board.md`

## Source Blueprint

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-HCV-001.blueprint.json`
- Blueprint ID: `BP-SCR-HOM-HCV-001-001`
- Atlas screen: `SCR-HOM-HCV-001`

## Generated Map

- Target map: `../TheLastSwordProtocol-Game/data/Map005.json`
- Map ID: `5`
- Map name: `DGN_HiddenCave_Entrance`
- Display name: `Hidden Cave Entrance`
- Dimensions: `24 x 24`
- Tileset: existing RPG Maker MZ tileset ID `4` / Atlas placeholder tileset `Dungeon`
- Region IDs painted by exporter policy: `5` for safe/no-encounter staging
- Encounter list: empty

## Events Generated Or Updated

Created:

- `INT-HCV-WALL-CARVING Wall Carving` at `(17, 10)`

Updated while preserving executable event pages:

- `Hidden Cave First Entry` at `(12, 18)`
- `TRN-HOM-010 Exit cave` at `(12, 23)`
- `TRN-HOM-011 Enter trials` at `(12, 1)`

## Validation Result

- Hidden Cave Entrance blueprint round-trip audit: PASS, found 29, missing 0, warnings 0.
- Skyreach regression round-trip audit: PASS, found 29, missing 0, warnings 0.
- Ashford regression round-trip audit: PASS, found 73, missing 0, warnings 0.
- Vertical-slice playthrough audit: PASS, found 81, missing 0, warnings 0, not machine-checkable 1.
- Clean skeleton data audit: PASS, found 335, missing 0, warnings 0, not machine-checkable 1.
- Python compile: PASS.
- Atlas export validation: PASS.
- RPG Maker JSON parse checks: PASS.
- Atlas validation: PASS, 0 errors, 0 warnings.

## Remaining Limitations

- The generated cave uses placeholder tile IDs and existing dungeon tileset assignments.
- The wall-carving event is traceable but intentionally contains no final lore/dialogue.
- Inbound transfer coordinates remain valid but should be refined during a later route polish/playtest pass.

## Recommendation For Next Build Order

`BUILD-0013 - Generate Hidden Cave Trials Blueprint and Map`: extend blueprint-driven generation to `SCR-HOM-HCV-002`, preserving Body/Mind/Heart trial events, Sanctum Gate, Region 5 trial/event staging, and transfer structure.
