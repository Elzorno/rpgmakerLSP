# BUILD-0003 - Atlas Event And Transfer Placeholders

## Summary

BUILD-0003 generated Atlas event and transfer placeholders in the clean RPG Maker MZ skeleton:

```text
../TheLastSwordProtocol-Game
```

The legacy RPG Maker project was not modified.

## Tooling Added

```text
tools/atlas-import/apply_event_placeholders.py
```

The applier consumes:

```text
../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

and writes placeholder RPG Maker events into the clean skeleton only.

## Generated Skeleton Changes

Created or updated:

- 31 Atlas-named map event placeholders
- 30 transfer command events
- 2 Node Seven troop event page placeholders
- 1 external target map for the Journey II handoff:

```text
data/Map050.json
MapInfos id 50: JRN2_Landing_Placeholder
```

The Journey II target is intentionally a placeholder. It exists so the Home Island departure transfer can resolve to a concrete RPG Maker map ID without defining Journey II content.

## Event Placeholder Policy

Each Atlas event placeholder:

- is named exactly from the Atlas export event name,
- includes comment commands with the Atlas event ID and required state result,
- includes a non-executing placeholder plugin command marker,
- applies simple switch/variable placeholders only when the Atlas export states an explicit result.

No final dialogue, lore, map layout, combat behavior, or scene design was invented.

## Transfer Placeholder Policy

Each transfer placeholder:

- is named with its Atlas transfer ID and notes,
- includes comment commands with the Atlas transfer condition,
- includes RPG Maker transfer command code `201`,
- targets the expected RPG Maker map ID.

## Audit Result

Clean skeleton audit after BUILD-0003:

```text
found=152 missing=0 warning=0 unknown=1
```

The remaining `unknown=1` is intentional:

```text
Animation None
```

Atlas explicitly allows no RPG Maker animation for that row.

## BUILD-0003 Gate

Result: **PASS**.

The clean skeleton now has machine-visible placeholders for:

- all Atlas Home Island maps,
- all required database rows,
- all common event candidates,
- all trial switches and variables,
- all Atlas event names,
- all transfer commands,
- all expected troop event pages.

## Recommended Next Step

Proceed to **BUILD-0004 - Fill Executable Event Page Logic In Clean Skeleton**.

BUILD-0004 should replace placeholder command markers with executable RPG Maker event command sequences, starting with:

- player start,
- core map transfers,
- required story gates,
- trial entry/clear events,
- Node Seven guardian battle,
- departure sequence.
