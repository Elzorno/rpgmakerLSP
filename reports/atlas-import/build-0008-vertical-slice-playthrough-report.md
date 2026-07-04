# BUILD-0008 - Home Island Vertical Slice Playthrough Audit Report

## Completed

BUILD-0008 added and ran a read-only vertical-slice playthrough audit for the clean Home Island skeleton.

The audit checks the machine-visible route from new game start through the Journey II placeholder:

- New game starts in Elara House.
- Elara House exits to Ashford.
- Tremor opens Skyreach access.
- Skyreach and Hidden Cave gates are reachable.
- Body, Mind, and Heart trial switches can turn on.
- Sword Sanctum transfer checks all three trial switches.
- Sword pedestal grants Sword state, Sword key item, Sword weapon, and archive recovery.
- Glassfield seal opens the Sealed Node path.
- Node Seven Guardian starts troop 10 and sets defeat state.
- Relay Core restores Node Seven and unlocks mainland travel.
- Rustshore departure reaches the departure map.
- Departure sequence advances `Current_Journey = 2`.
- Final transfer reaches the Journey II placeholder map.
- Required return transfers are present so the player is not stranded before departure.

No game data was modified by BUILD-0008.

## Files Modified

- `tools/atlas-import/README.md`

## Files Created

- `tools/atlas-import/audit_vertical_slice_playthrough.py`
- `reports/atlas-import/build-0008-vertical-slice-playthrough-audit.md`
- `reports/atlas-import/build-0008-clean-skeleton-readiness-audit.md`
- `reports/atlas-import/build-0008-vertical-slice-playthrough-report.md`

## Verification

Commands run:

```bash
/usr/bin/python3 -m py_compile tools/atlas-import/audit_vertical_slice_playthrough.py tools/atlas-import/audit_rpgmaker_data.py tools/atlas-import/apply_animation_feedback.py tools/atlas-import/apply_audio_hooks.py tools/atlas-import/apply_map_layouts.py tools/atlas-import/apply_executable_event_logic.py tools/atlas-import/apply_event_placeholders.py tools/atlas-import/create_clean_skeleton.py tools/atlas-import/validate_atlas_export.py tools/atlas-import/generate_implementation_checklist.py
/usr/bin/python3 tools/atlas-import/audit_vertical_slice_playthrough.py reports/atlas-import/build-0008-vertical-slice-playthrough-audit.md --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_rpgmaker_data.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json reports/atlas-import/build-0008-clean-skeleton-readiness-audit.md --project-root ../TheLastSwordProtocol-Game
node -e "const fs=require('fs'),p='../TheLastSwordProtocol-Game/data'; for (const f of fs.readdirSync(p).filter(x=>x.endsWith('.json'))) JSON.parse(fs.readFileSync(p+'/'+f,'utf8')); console.log('json-ok')"
/usr/bin/python3 tools/atlas-import/validate_atlas_export.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
/usr/bin/python3 ../TheLastSwordProtocol-Atlas/atlas-tools/cli/atlas.py validate
/usr/bin/python3 atlas-tools/cli/atlas.py validate
```

Results:

- Python compile checks passed.
- Vertical-slice playthrough audit: `found=81 missing=0 warning=0 unknown=1`.
- Clean skeleton readiness audit: `found=335 missing=0 warning=0 unknown=1`.
- Clean skeleton JSON parse check passed with `json-ok`.
- Atlas export validation: `PASS`.
- Sibling Atlas validation: `Errors: 0`, `Warnings: 0`.
- Repo-local Atlas validation: `Errors: 0`, `Warnings: 0`.

## Remaining Issues

- The playthrough audit has one expected unknown: hands-on RPG Maker runtime feel, input timing, and visual/audio timing still require an actual manual playtest.
- No machine-visible Home Island route blockers remain in the clean skeleton.
- The next build-order surface should be either a manual-runtime playtest pass or a guarded runtime smoke-test workflow if RPG Maker execution becomes available.
