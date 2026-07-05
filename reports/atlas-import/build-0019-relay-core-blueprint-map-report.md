# BUILD-0019 - Generate Relay Node Seven Core Blueprint and Map

## Summary

BUILD-0019 created the engine-independent Atlas blueprint for `SCR-HOM-SND-004` and generated the clean RPG Maker MZ `DGN_SealedNode_RelayCore` map from it.

The generated map preserves the existing Relay Core event and return transfer event pages while moving them to blueprint coordinates. The map is safe/story-only with no random encounters.

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-SND-004.blueprint.json`
- `reports/atlas-import/build-0019-relay-core-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0019-*-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0019-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0019-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0019-relay-core-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `../TheLastSwordProtocol-Game/data/Map012.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-SND-004-001`
- Atlas screen: `SCR-HOM-SND-004`
- RPG Maker target: `DGN_SealedNode_RelayCore`
- Dimensions: `23 x 19`
- Encounter policy: no random encounters
- Region policy: Region 5 safe/story zone
- Transfer: `TRN-HOM-024` return to Guardian Chamber at `(11, 18)`
- Main anchor: `EVT-HOM-022` Relay Core at `(11, 8)`

## Validation Result

- Relay Core round-trip audit: found 21, missing 0, warning 0
- Blueprint regression audits: 0 missing, 0 warnings
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No RPG Maker project files outside `data/Map012.json` were modified.
- Existing event command pages were preserved; this order generated map layout, safe region policy, and anchor placement only.
