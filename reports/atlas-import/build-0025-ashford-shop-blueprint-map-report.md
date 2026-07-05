# BUILD-0025 - Generate Ashford Shop Interior Blueprint and Map

## Summary

BUILD-0025 created the engine-independent Atlas blueprint for `SCR-HOM-ASH-003` and generated the clean RPG Maker MZ `INT_Ashford_Shop` map from it.

The generated map keeps Ashford Shop as a small starter shop: shopkeeper interaction, exit transfer to Ashford Exterior, and a local optional metal cabinet examine anchor from the screen spec. Existing event pages were preserved.

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-ASH-003.blueprint.json`
- `reports/atlas-import/build-0025-ashford-shop-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0025-elara-house-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0025-ashford-exterior-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0025-relay-core-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0025-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0025-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0025-atlas-export-validation.md`
- `reports/atlas-import/build-0025-ashford-shop-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `../TheLastSwordProtocol-Game/data/Map003.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-ASH-003-001`
- Atlas screen: `SCR-HOM-ASH-003`
- RPG Maker target: `INT_Ashford_Shop`
- Dimensions: `17 x 13`
- Encounter policy: Region 0 only, no random encounters
- Transfer: `TRN-HOM-004` at `(8, 12)`
- Event anchor: `EVT-HOM-008` Shopkeeper at `(8, 5)`
- Local examine anchor: `INT-ASH-SHOP-CABINET` at `(12, 4)`

## Validation Result

- Ashford Shop round-trip audit: found 25, missing 0, warning 0
- Elara House regression audit: found 29, missing 0, warning 0
- Ashford Exterior regression audit: found 73, missing 0, warning 0
- Relay Core regression audit: found 21, missing 0, warning 0
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No RPG Maker project files outside `data/Map003.json` were modified.
- The optional cabinet event uses a local Atlas anchor, `INT-ASH-SHOP-CABINET`, because the screen spec calls for an optional cabinet examine but no separate event-registry ID exists.
- No final dialogue, lore, item inventory changes, or shop balance changes were added.
