# Atlas Import Tools

These tools let the RPG Maker MZ project consume structured exports from the Atlas repository.

## Verified Tile Palettes (WO-0060)

WO-0060 palettes live in `tile-palettes/` and remain
`generated_pending_live_review` until Chris confirms them in RPG Maker. Rebuild
them with `generate_wo0060_palettes.py`; validate them with
`validate_tile_palette.py` against the clean target project and the labeled
contact sheets in AtlasStudio.

The verifier is read-only and fails closed on guessed semantics, incomplete
StylePack coverage, missing provenance, stale source hashes, tile-address
errors, and passability/layer/adjacency drift. It does not write map data.

WO-0061's `mapplan_candidate_compiler.py` consumes those verified palettes and
writes only to a target project whose ownership ledger marks the requested map
`generated`. `generate_wo0061_fixtures.py` rebuilds the disposable temperate
and coastal comparison candidates under `reports/atlas-import/wo0061/`; there
is intentionally no production-promotion command.

WO-0062 extends AtlasStudio's existing `QualityAuditor` with non-bypassable
candidate hard gates and a separate advisory classic-JRPG rubric.
`generate_wo0062_gallery.py` produces the ten-candidate labeled contact sheet
under `reports/atlas-import/wo0062/`. `record_wo0062_review.py` records a human
accept/reject decision without changing scores or applying production promotion.

## Map Ownership Guard (WO-0031)

Every write-capable script in this toolchain (`apply_*.py`, `create_clean_skeleton.py`, `generate_map_from_blueprint.py`) consults the per-map ownership ledger `map_ownership.json` at the target project root (via `map_ownership_guard.py`) before writing any `data/MapXXX.json`:

- Only maps with ledger state `generated` may be written; `hand_authored` and `locked` maps are skipped with a loud `OWNERSHIP GUARD:` report line.
- **Fail safe:** a missing, unreadable, or malformed ledger — or an unlisted map id — means that map is NOT writable. `create_clean_skeleton.py --force` additionally refuses to delete an existing target whose ledger is missing or lists any non-`generated` map.
- `create_clean_skeleton.py` writes a fresh all-`generated` ledger into new skeletons; scripts that create brand-new map files register them in the ledger as `generated`.
- Audit the ledger state read-only at any time:

```bash
/usr/bin/python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
```

Flip a map's state to `hand_authored` in the ledger the moment manual editor work on it begins. See `../TheLastSwordProtocol-Game/AGENTS.md` for the full ownership contract and manual map build workflow.

WO-0018 is validation-only. The importer must not mutate RPG Maker JSON, maps, events, assets, or project settings.

## Validate Home Island Export

Run from the RPG Maker repository:

```bash
/usr/bin/python3 tools/atlas-import/validate_atlas_export.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

The validator checks the export schema and reports the expected RPG Maker resources implied by Atlas.

Atlas IDs remain canonical. RPG Maker map IDs, event numbers, and database positions remain implementation details unless Atlas explicitly assigns them.

## Generate Home Island Implementation Checklist

Run from the RPG Maker repository:

```bash
/usr/bin/python3 tools/atlas-import/generate_implementation_checklist.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

Output:

```text
reports/atlas-import/home-island-implementation-checklist.md
```

The checklist is a read-only Markdown build tracker. It does not modify RPG Maker data files.

## Audit RPG Maker Data Readiness

Run from the RPG Maker repository:

```bash
/usr/bin/python3 tools/atlas-import/audit_rpgmaker_data.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

Output:

```text
reports/atlas-import/home-island-data-readiness-audit.md
```

The audit compares Atlas export expectations against current RPG Maker `data/*.json` files and reports found, missing, warning, and not-machine-checkable items. It is read-only.

The audit parses database rows, map names, map event names, transfer event commands, switch names, variable names, common events, and troop event pages.

To audit a different RPG Maker project root, pass `--project-root`:

```bash
/usr/bin/python3 tools/atlas-import/audit_rpgmaker_data.py ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json reports/atlas-import/target-audit.md --project-root ../TheLastSwordProtocol-Game
```

## Create Clean Skeleton

Run from the legacy RPG Maker repository:

```bash
/usr/bin/python3 tools/atlas-import/create_clean_skeleton.py --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json --target ../TheLastSwordProtocol-Game
```

The generator creates a clean sibling RPG Maker MZ project with Atlas-reserved Home Island maps, database rows, switches, variables, and common event placeholders. It refuses to replace an existing target unless `--force` is supplied.

## Apply Event Placeholders

Run from the legacy RPG Maker repository:

```bash
/usr/bin/python3 tools/atlas-import/apply_event_placeholders.py --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json --project-root ../TheLastSwordProtocol-Game
```

The applier writes Atlas-named placeholder map events, transfer command events, and Node Seven troop event placeholders into the clean skeleton. It does not modify the legacy RPG Maker project.

## Apply Executable Event Logic

Run from the legacy RPG Maker repository after event placeholders exist:

```bash
/usr/bin/python3 tools/atlas-import/apply_executable_event_logic.py --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json --project-root ../TheLastSwordProtocol-Game
```

The applier replaces clean-skeleton placeholder markers with executable RPG Maker MZ event command pages for Home Island events, transfers, trial gates, treasure pickups, shop placeholder behavior, the Node Seven boss, relay restoration, and departure flow. It preserves placeholder dialogue IDs instead of writing final story text.

## Apply Placeholder Map Layouts

Run from the legacy RPG Maker repository after executable events exist:

```bash
/usr/bin/python3 tools/atlas-import/apply_map_layouts.py --project-root ../TheLastSwordProtocol-Game
```

The applier paints first-playable placeholder terrain, Atlas region IDs, encounter lists, and event coordinates for the 16 Home Island maps in the clean skeleton. It uses the Atlas tileset assignment matrix and does not create final art assets.

## Apply Audio Hooks

Run from the legacy RPG Maker repository after placeholder layouts exist:

```bash
/usr/bin/python3 tools/atlas-import/apply_audio_hooks.py --project-root ../TheLastSwordProtocol-Game
```

The applier assigns existing RTP placeholder BGM/BGS files to Home Island maps and adds Play SE hooks to major story, reward, trial, relay, and signal events. It verifies referenced audio files exist before writing.

## Apply Animation Feedback

Run from the legacy RPG Maker repository after audio hooks exist:

```bash
/usr/bin/python3 tools/atlas-import/apply_animation_feedback.py --project-root ../TheLastSwordProtocol-Game
```

The applier adds first-playable Show Animation commands to Home Island story, reward, trial, relay, and signal events plus common feedback events. It verifies referenced animation database rows exist before writing.

## Audit Vertical Slice Playthrough

Run from the legacy RPG Maker repository after animation feedback exists:

```bash
/usr/bin/python3 tools/atlas-import/audit_vertical_slice_playthrough.py reports/atlas-import/build-0008-vertical-slice-playthrough-audit.md --project-root ../TheLastSwordProtocol-Game
```

The audit is read-only. It checks the machine-visible Home Island critical path from new game start through the Journey II placeholder, including transfer targets, gated route switches, trial completion switches, Sword acquisition, Node Seven boss/relay state, and Rustshore departure.

## Generate the WO-0063 Settlement Slice

Generate labeled `Outside` tileset contact sheets, then compile the disposable
temperate/coastal settlement candidates:

```bash
python3 tools/atlas-import/generate_wo0063_contact_sheets.py
python3 tools/atlas-import/generate_wo0063_settlement.py
```

Outputs live only under `reports/atlas-import/wo0063/`. Each recorded seed has
the engine-neutral MapPlan, ASCII/SVG structural previews, isolated RPG Maker
fixture candidate, manifest, route diagnostics, quality result, and render.
`settlement-gallery.png` compares all six candidates. These are non-canon,
remain `generated_pending_review`, and have no production-promotion path.
