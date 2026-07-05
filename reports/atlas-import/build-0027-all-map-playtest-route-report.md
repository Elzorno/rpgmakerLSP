# BUILD-0027 - All-Map Playtest Route Audit

## Summary

BUILD-0027 added and ran a read-only audit for all Atlas Home Island transfer routes in the clean RPG Maker MZ project.

Result: GO. All 30 Atlas Home Island transfer IDs resolve to RPG Maker events, every checked transfer command targets the expected map, all transfer destinations are in bounds, and all 16 registered Home Island screens are reachable from the configured new-game start map.

## Files Created

- `tools/atlas-import/audit_all_map_routes.py`
- `reports/atlas-import/build-0027-all-map-route-audit.md`
- `reports/atlas-import/build-0027-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0027-clean-skeleton-data-audit.md`
- `reports/atlas-import/build-0027-atlas-export-validation.md`
- `reports/atlas-import/build-0027-all-map-playtest-route-report.md`

## Files Modified

- `.agents/task-board.md`
- `.agents/outbox/codex.md`

## Audit Coverage

- Transfer source maps resolve for all Atlas transfers.
- Transfer events exist on their source maps.
- Transfer events are placed in source map bounds.
- Transfer events sit on concrete nonzero base tiles.
- Transfer targets resolve to RPG Maker maps, including the Journey II placeholder.
- Transfer commands target expected maps.
- Transfer destination coordinates are in target map bounds.
- Home Island screen graph reachability is checked from `System.json` start map.
- Orphan `TRN-HOM-*` event hygiene is checked.

## Validation Result

- All-map route audit: found 258, missing 0, warning 0
- Reachability: all 16 registered Home Island screens reachable from `SCR-HOM-ASH-002`
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- This is a JSON-level route audit, not a hands-on RPG Maker runtime playtest.
- Story gates are ignored for reachability, because the audit is checking whether transfer-command paths exist, not whether the player has set the required switches at a specific moment.
- No RPG Maker data files, Atlas content files, or game assets were modified.
