# BUILD-0002 - Read-Only Map/Event Parser For Atlas Audit

## Summary

BUILD-0002 upgraded the Atlas RPG Maker data audit from database-only comparison to read-only event-aware parsing.

The audit now checks:

- RPG Maker map files listed by `MapInfos.json`
- map event names against Atlas event expectations
- transfer commands using RPG Maker event command code `201`
- trial switch names in `System.json`
- trial variable names in `System.json`
- common event placeholders in `CommonEvents.json`
- troop event page presence and whether pages contain non-empty commands

The audit remains read-only. It does not modify RPG Maker JSON, maps, events, assets, project settings, Atlas content, or the clean skeleton.

## Files Updated

```text
tools/atlas-import/audit_rpgmaker_data.py
reports/atlas-import/home-island-data-readiness-audit.md
reports/atlas-import/build-0002-clean-skeleton-event-audit.md
```

## Parser Behavior

### Map Events

For each Atlas event, the parser:

1. resolves the Atlas screen to the RPG Maker map name,
2. resolves the map name through `MapInfos.json`,
3. loads the matching `Map###.json`,
4. checks whether an event with the expected Atlas event name exists on that map.

### Transfers

For each Atlas transfer, the parser:

1. resolves the source and target screens to RPG Maker map IDs,
2. loads the source `Map###.json`,
3. scans event pages for RPG Maker transfer command code `201`,
4. checks whether any transfer command targets the expected map ID.

### Trial State

The parser now checks the Atlas trial switches and variables directly against `System.json`.

### Common Events

The parser checks Atlas common event candidates against `CommonEvents.json` by candidate ID and display name.

### Troop Event Pages

The parser checks whether expected troop event pages exist and whether optional placeholder pages contain command bodies.

## Audit Results

Legacy project audit:

```text
found=22 missing=91 warning=39 unknown=1
```

Clean skeleton audit:

```text
found=89 missing=62 warning=1 unknown=1
```

The one remaining `unknown` is the Atlas `Animation None` row. It means no RPG Maker animation is required, not a parser failure.

## Clean Skeleton Findings

Resolved by BUILD-0002 parser:

- Trial state is now machine-checked and found.
- Common events are now machine-checked and found.
- Troop event pages are now machine-checked.
- Atlas events are now concrete missing rows instead of unknown rows.
- Transfers are now concrete missing rows instead of unknown rows.

Remaining clean skeleton build blockers:

| Category | Missing | Meaning |
|---|---:|---|
| Atlas Events | 31 | The clean skeleton maps do not yet contain Atlas-named event placeholders. |
| Transfers | 30 | The clean skeleton maps do not yet contain transfer command events. |
| Common Events | 0 | All Atlas common event placeholders are present. |
| Trial State | 0 | Required trial switches and variables are present. |
| Troop Event Pages | 1 | Troop 10 page 2 is not present yet. |

Remaining clean skeleton warning:

```text
Troop 10 event page 1 exists but contains no optional placeholder commands.
```

## BUILD-0002 Gate

Result: **PASS**.

The audit no longer hides Home Island event/transfer readiness behind `not machine-checkable yet`. It now identifies the next implementation surface directly:

- create Atlas-named map event placeholders,
- create transfer command events,
- add the second optional Node Seven troop event page,
- add optional placeholder commands to Node Seven troop page 1.

## Recommended Next Step

Proceed to **BUILD-0003 - Generate Atlas Event And Transfer Placeholders In Clean Skeleton**.

BUILD-0003 should target only the clean skeleton repository and should remain mechanically generated from the Atlas export. It should not modify the legacy `rpgmakerLSP/data/*.json` files.
