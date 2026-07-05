# BUILD-0020 - Generate Rustshore Docks Blueprint and Map

## Summary

BUILD-0020 created the engine-independent Atlas blueprint for `SCR-HOM-RST-001` and generated the clean RPG Maker MZ `TWN_Rustshore_Docks` map from it.

The generated map preserves the existing Dockmaster, Lighthouse Examine, Boat Transfer, return transfer, and mainland departure transfer event pages while moving them to blueprint coordinates. This order also added explicit `none` region-policy support to the round-trip audit so Region 0-only maps can be represented without painting Region 5.

## Files Created

- `../TheLastSwordProtocol-Atlas/atlas-tools/mapgen/prototype/SCR-HOM-RST-001.blueprint.json`
- `reports/atlas-import/build-0020-rustshore-docks-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0020-*-regression-blueprint-round-trip-audit.md`
- `reports/atlas-import/build-0020-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0020-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0020-rustshore-docks-blueprint-map-report.md`

## Files Modified

- `tools/atlas-import/generate_map_from_blueprint.py`
- `tools/atlas-import/audit_blueprint_round_trip.py`
- `../TheLastSwordProtocol-Game/data/Map013.json`
- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Blueprint Summary

- Blueprint ID: `BP-SCR-HOM-RST-001-001`
- Atlas screen: `SCR-HOM-RST-001`
- RPG Maker target: `TWN_Rustshore_Docks`
- Dimensions: `34 x 26`
- Encounter policy: none
- Region policy: explicit Region 0/no painted region policy
- Transfers:
  - `TRN-HOM-008` return to Ashford-side route at `(0, 18)`
  - `TRN-HOM-025` begin mainland departure at `(30, 14)`
- Main anchors:
  - `EVT-HOM-023` Dockmaster at `(17, 13)`
  - `EVT-HOM-024` Lighthouse Examine at `(7, 9)`
  - `EVT-HOM-025` Boat Transfer at `(28, 14)`

## Validation Result

- Rustshore Docks round-trip audit: found 33, missing 0, warning 0
- Blueprint regression audits: 0 missing, 0 warnings
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No RPG Maker project files outside `data/Map013.json` were modified.
- Existing event command pages were preserved; this order generated map layout, region policy, and anchor placement only.
- Runtime visual inspection in RPG Maker remains useful before treating generated map layout as final production geometry.
