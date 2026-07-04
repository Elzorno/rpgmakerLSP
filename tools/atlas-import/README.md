# Atlas Import Tools

These tools let the RPG Maker MZ project consume structured exports from the Atlas repository.

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
