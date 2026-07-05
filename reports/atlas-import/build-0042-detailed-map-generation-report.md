# BUILD-0042 - Improved RPG Maker Map Generator Detail Report

## Objective

Improve generated RPG Maker MZ maps so they are more useful than basic scaffolds while preserving Atlas canon and first-playable safety.

## Implementation

- Updated `tools/atlas-import/generate_map_from_blueprint.py`.
- Added deterministic `DEC-*` decorative landmark events derived from blueprint obstacles and selected terrain zones.
- Decorative landmarks use existing project character assets only.
- Decorative landmarks are below-character, noninteractive guide markers.
- Existing Atlas transfer, NPC, treasure, and event anchors remain authoritative.
- Collision cleanup still clears upper-layer tiles above blocked base terrain.

## Maps Regenerated

All 16 Home Island maps were regenerated from Atlas blueprints.

| Map | Display Name | Decorative Landmarks | Total Events |
|---|---|---:|---:|
| `Map001.json` | Ashford Exterior | 7 | 22 |
| `Map002.json` | Elara House Interior | 6 | 10 |
| `Map003.json` | Ashford Shop Interior | 7 | 10 |
| `Map004.json` | Skyreach Hill Path | 5 | 9 |
| `Map005.json` | Hidden Cave Entrance | 5 | 9 |
| `Map006.json` | Hidden Cave Trials | 7 | 19 |
| `Map007.json` | Sword Sanctum | 5 | 7 |
| `Map008.json` | Glassfield Ruins Exterior | 6 | 10 |
| `Map009.json` | Sealed Node Upper | 5 | 8 |
| `Map010.json` | Sealed Node Core Path | 5 | 8 |
| `Map011.json` | Sealed Node Guardian Chamber | 5 | 8 |
| `Map012.json` | Relay Node Seven Core | 4 | 6 |
| `Map013.json` | Rustshore Docks | 6 | 11 |
| `Map014.json` | Mainland Departure | 3 | 5 |
| `Map015.json` | Fogfen Marsh Field | 8 | 13 |
| `Map016.json` | Deeper Marsh Pocket | 8 | 12 |

## Result

- Decorative landmark events created/updated: 92
- Event pages checked after regeneration: 191
- Blank event images after regeneration: 0
- Missing character assets after regeneration: 0
- Blocked base tiles with upper-layer overrides: 0

## Validation

- `py_compile` passed for `generate_map_from_blueprint.py`.
- RPG Maker data JSON parses successfully.
- Event command coverage: found=204 missing=0 warning=0
- All-map route audit: found=258 missing=0 warning=0
- Vertical-slice playthrough audit: found=81 missing=0 warning=0 unknown=1
- Clean skeleton data audit: found=335 missing=0 warning=0 unknown=1
- Atlas validation: 0 errors, 0 warnings

## Notes

- This is still placeholder map detail, not final art.
- The next runtime pass should evaluate whether the added decorative landmarks improve orientation without cluttering routes.
