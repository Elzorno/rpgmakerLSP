# BUILD-0024 - Generate Elara House Interior Blueprint and Map

## Summary

BUILD-0024 created the engine-independent Atlas blueprint for `SCR-HOM-ASH-002` and generated the clean RPG Maker MZ `INT_Ashford_ElaraHouse` map from it.

The generated map keeps Elara House as the starting room: player start, Elara intro interaction, exit transfer to Ashford Exterior, and a local keepsake/bookshelf examine anchor from the screen spec. Existing event pages were preserved.

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-002.blueprint.json`
- `reports/atlas-import/build-0024-elara-house-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0024-ashford-exterior-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0024-fogfen-marsh-field-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0024-relay-core-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0024-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0024-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0024-atlas-export-validation.md`
- `reports/atlas-import/build-0024-elara-house-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `../TheLastSwordProtocol-Game/data/Map002.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-ASH-002-001`
- Atlas screen: `SCR-HOM-ASH-002`
- RPG Maker target: `INT_Ashford_ElaraHouse`
- Dimensions: `17 x 13`
- Encounter policy: Region 0 only, no random encounters
- Transfer: `TRN-HOM-001` at `(8, 12)`
- Event anchors: `EVT-HOM-001` at `(8, 6)`, `EVT-HOM-002` at `(8, 4)`
- Local examine anchor: `INT-ASH-ELARA-KEEPSAKE` at `(13, 4)`

## Validation Result

- Elara House round-trip audit: found 29, missing 0, warning 0
- Ashford Exterior regression audit: found 73, missing 0, warning 0
- Fogfen Marsh Field regression audit: found 33, missing 0, warning 0
- Relay Core regression audit: found 21, missing 0, warning 0
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No RPG Maker project files outside `data/Map002.json` were modified.
- The keepsake/bookshelf event uses a local Atlas anchor, `INT-ASH-ELARA-KEEPSAKE`, because the screen spec calls for an optional bookshelf/keepsake but no separate event-registry ID exists.
- No final dialogue, lore, or item grant was added.
