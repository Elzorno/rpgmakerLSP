# BUILD-0021 - Generate Mainland Departure Blueprint and Map

## Summary

BUILD-0021 created the engine-independent Atlas blueprint for `SCR-HOM-RST-002` and generated the clean RPG Maker MZ `CUT_Mainland_Departure` map from it.

The generated map preserves the existing Departure Sequence and Journey II placeholder transfer event pages while moving them to blueprint coordinates. The blueprint keeps the destination explicitly marked as a Journey II placeholder rather than inventing Coalmouth routing.

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-RST-002.blueprint.json`
- `reports/atlas-import/build-0021-mainland-departure-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0021-rustshore-docks-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0021-relay-core-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0021-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0021-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0021-mainland-departure-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `../TheLastSwordProtocol-Game/data/Map014.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-RST-002-001`
- Atlas screen: `SCR-HOM-RST-002`
- RPG Maker target: `CUT_Mainland_Departure`
- Dimensions: `23 x 17`
- Encounter policy: none
- Region policy: Region 5 cutscene/story zone
- Transfer: `TRN-HOM-026` Journey II placeholder at `(11, 1)`
- Main anchor: `EVT-HOM-026` Departure Sequence at `(11, 10)`

## Validation Result

- Mainland Departure round-trip audit: found 21, missing 0, warning 0
- Rustshore Docks regression audit: found 33, missing 0, warning 0
- Relay Core regression audit: found 21, missing 0, warning 0
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No RPG Maker project files outside `data/Map014.json` were modified.
- Existing event command pages were preserved; this order generated map layout, safe region policy, and anchor placement only.
- Journey II destination remains intentionally placeholder-labeled per Atlas open questions.
