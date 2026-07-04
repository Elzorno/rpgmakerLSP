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
