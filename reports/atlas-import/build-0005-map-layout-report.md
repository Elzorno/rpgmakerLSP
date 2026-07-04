# BUILD-0005 - Home Island Placeholder Map Layout Report

## Completed

BUILD-0005 painted first-playable placeholder layouts for the clean Home Island skeleton.

Implemented:

- Placeholder base terrain for all 16 Home Island maps.
- Opened traversable tiles under every Atlas-relevant event and transfer.
- First-pass path markings for village routes, cave corridors, node corridors, Rustshore dock flow, and Fogfen branch flow.
- Atlas region IDs from `ATLAS-TEC-059`:
  - Region 1 for Home Field / Glassfield encounter zones.
  - Region 2 for Fogfen encounter zones.
  - Region 3 for Fogfen slow/dense bog markers.
  - Region 4 for Sealed Node approach encounter zones.
  - Region 5 for story/no-random-encounter zones.
- Encounter lists only where Atlas allows first-playable random encounters.
- Event and transfer placement for 61 Atlas-relevant map events.

This pass does not create final art assets or final map composition. It creates a deterministic first-playable topology that can be tested and iterated.

## Files Modified

- `tools/atlas-import/audit_rpgmaker_data.py`
- `tools/atlas-import/README.md`
- `../TheLastSwordProtocol-Game/data/Map001.json`
- `../TheLastSwordProtocol-Game/data/Map002.json`
- `../TheLastSwordProtocol-Game/data/Map003.json`
- `../TheLastSwordProtocol-Game/data/Map004.json`
- `../TheLastSwordProtocol-Game/data/Map005.json`
- `../TheLastSwordProtocol-Game/data/Map006.json`
- `../TheLastSwordProtocol-Game/data/Map007.json`
- `../TheLastSwordProtocol-Game/data/Map008.json`
- `../TheLastSwordProtocol-Game/data/Map009.json`
- `../TheLastSwordProtocol-Game/data/Map010.json`
- `../TheLastSwordProtocol-Game/data/Map011.json`
- `../TheLastSwordProtocol-Game/data/Map012.json`
- `../TheLastSwordProtocol-Game/data/Map013.json`
- `../TheLastSwordProtocol-Game/data/Map014.json`
- `../TheLastSwordProtocol-Game/data/Map015.json`
- `../TheLastSwordProtocol-Game/data/Map016.json`

## Files Created

- `tools/atlas-import/apply_map_layouts.py`
- `reports/atlas-import/build-0005-clean-skeleton-layout-audit.md`
- `reports/atlas-import/build-0005-map-layout-report.md`

## Verification

Commands run:

```bash
/usr/bin/python3 -m py_compile tools/atlas-import/audit_rpgmaker_data.py tools/atlas-import/apply_map_layouts.py tools/atlas-import/apply_executable_event_logic.py tools/atlas-import/apply_event_placeholders.py tools/atlas-import/create_clean_skeleton.py tools/atlas-import/validate_atlas_export.py tools/atlas-import/generate_implementation_checklist.py
/usr/bin/python3 tools/atlas-import/apply_map_layouts.py --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/audit_rpgmaker_data.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json reports/atlas-import/build-0005-clean-skeleton-layout-audit.md --project-root ../TheLastSwordProtocol-Game
node -e "const fs=require('fs'),p='../TheLastSwordProtocol-Game/data'; for (const f of fs.readdirSync(p).filter(x=>x.endsWith('.json'))) JSON.parse(fs.readFileSync(p+'/'+f,'utf8')); console.log('json-ok')"
/usr/bin/python3 tools/atlas-import/apply_map_layouts.py --project-root ../TheLastSwordProtocol-Game
/usr/bin/python3 tools/atlas-import/validate_atlas_export.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
/usr/bin/python3 ../TheLastSwordProtocol-Atlas/atlas-tools/cli/atlas.py validate
/usr/bin/python3 atlas-tools/cli/atlas.py validate
```

Results:

- Python compile checks passed.
- Layout applier first run: `maps_updated=16 events_moved=61`.
- Event-tile passability correction run: `maps_updated=16 events_moved=0`.
- Layout applier final idempotence run: `maps_updated=0 events_moved=0`.
- Clean skeleton JSON parse check passed with `json-ok`.
- Clean skeleton audit: `found=277 missing=0 warning=0 unknown=1`.
- Atlas export validation: `PASS`.
- Sibling Atlas validation: `Errors: 0`, `Warnings: 0`.
- Repo-local Atlas validation: `Errors: 0`, `Warnings: 0`.

## Remaining Issues

- The one audit unknown is still the intentional Atlas `Animation None` fallback.
- Final art, detailed final map dressing, final audio, and final playtest balancing remain outside BUILD-0005.
- The next build-order surface is likely audio hooks or animation/event feedback application in the clean skeleton, followed by a vertical-slice playthrough audit.
