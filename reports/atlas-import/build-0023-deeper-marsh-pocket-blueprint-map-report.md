# BUILD-0023 - Generate Deeper Marsh Pocket Blueprint and Map

## Summary

BUILD-0023 created the engine-independent Atlas blueprint for `SCR-HOM-FOG-002` and generated the clean RPG Maker MZ `FLD_Fogfen_Deeper_Marsh_Pocket` map from it.

The generated map keeps the pocket as a compact optional detour: an always-open return transfer, a signal pool / cable cluster examine event, an optional reward cache, Region 2 Fogfen encounters, Region 3 slow bog markers, and Region 5 safety near the return path.

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-FOG-002.blueprint.json`
- `reports/atlas-import/build-0023-deeper-marsh-pocket-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0023-fogfen-marsh-field-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0023-rustshore-docks-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0023-relay-core-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0023-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0023-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0023-atlas-export-validation.md`
- `reports/atlas-import/build-0023-deeper-marsh-pocket-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `../TheLastSwordProtocol-Game/data/Map016.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-FOG-002-001`
- Atlas screen: `SCR-HOM-FOG-002`
- RPG Maker target: `FLD_Fogfen_Deeper_Marsh_Pocket`
- Dimensions: `24 x 20`
- Encounter policy: Region 2, troops 4 and 5 with slightly denser deeper-pocket weighting
- Hazard policy: Region 3 dense reed / slow bog marker
- Safety policy: Region 5 near the return transfer
- Transfer: `TRN-HOM-030` at `(0, 15)`
- Reward cache: `OBJ-HOM-FOG-009` at `(8, 13)`
- Event anchors: `EVT-HOM-030` at `(2, 15)`, `EVT-HOM-031` at `(14, 9)`

## Validation Result

- Deeper Marsh Pocket round-trip audit: found 29, missing 0, warning 0
- Fogfen Marsh Field regression audit: found 33, missing 0, warning 0
- Rustshore Docks regression audit: found 33, missing 0, warning 0
- Relay Core regression audit: found 21, missing 0, warning 0
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No RPG Maker project files outside `data/Map016.json` were modified.
- Existing return and signal/cable event pages were preserved.
- The optional reward cache was generated as a new event named `Deeper Marsh Reward Cache` using object ID `OBJ-HOM-FOG-009`, because Atlas defines the cache as a screen object but does not currently assign it a separate event-registry ID.
