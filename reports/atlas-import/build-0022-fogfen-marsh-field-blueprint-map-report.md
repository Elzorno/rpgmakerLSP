# BUILD-0022 - Generate Fogfen Marsh Field Blueprint and Map

## Summary

BUILD-0022 created the engine-independent Atlas blueprint for `SCR-HOM-FOG-001` and generated the clean RPG Maker MZ `FLD_Fogfen_Marsh_Field` map from it.

The generated map keeps Fogfen optional and grounded in the Atlas screen spec: a safe Ashford return, an optional deeper-marsh transfer, a hidden-item landmark, a signal-tick reed pool, Region 2 marsh encounters, Region 3 slow bog markers, and Region 5 safety near transfers.

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-FOG-001.blueprint.json`
- `reports/atlas-import/build-0022-fogfen-marsh-field-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0022-mainland-departure-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0022-rustshore-docks-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0022-relay-core-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0022-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0022-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0022-atlas-export-validation.md`
- `reports/atlas-import/build-0022-fogfen-marsh-field-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `../TheLastSwordProtocol-Game/data/Map015.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-FOG-001-001`
- Atlas screen: `SCR-HOM-FOG-001`
- RPG Maker target: `FLD_Fogfen_Marsh_Field`
- Dimensions: `40 x 32`
- Encounter policy: Region 2, troops 4 and 5
- Hazard policy: Region 3 slow bog marker
- Safety policy: Region 5 near transfer areas
- Transfers: `TRN-HOM-028` at `(0, 26)`, `TRN-HOM-029` at `(39, 8)`
- Treasure anchor: `EVT-HOM-028` Hidden Item Landmark at `(12, 22)`
- Event anchors: `EVT-HOM-027` at `(2, 26)`, `EVT-HOM-029` at `(26, 12)`

## Validation Result

- Fogfen Marsh Field round-trip audit: found 33, missing 0, warning 0
- Mainland Departure regression audit: found 21, missing 0, warning 0
- Rustshore Docks regression audit: found 33, missing 0, warning 0
- Relay Core regression audit: found 21, missing 0, warning 0
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No RPG Maker project files outside `data/Map015.json` were modified.
- Existing Fogfen event pages were preserved; this order generated map layout, region policy, encounter policy, and anchor placement only.
- An initial rerun of the clean-skeleton and export audits used the wrong argument order and failed before auditing data. Both commands were rerun with the correct export-first argument order and passed.
