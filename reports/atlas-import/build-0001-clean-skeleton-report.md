# BUILD-0001 - Clean RPG Maker MZ Project Skeleton From Atlas Export

## Summary

BUILD-0001 created a clean sibling RPG Maker MZ project skeleton at:

```text
../TheLastSwordProtocol-Game
```

The skeleton was generated from:

```text
../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

Skeleton repository commit:

```text
4fc236b Initial clean RPG Maker MZ skeleton
```

The legacy `rpgmakerLSP` project was not rewritten in place. Its existing RPG Maker `data/*.json`, maps, events, assets, and project settings were not modified.

## Files And Directories Created In The Skeleton

Project root:

```text
README.md
atlas_skeleton_manifest.json
game.rmmzproject
index.html
package.json
```

Runtime/support directories:

```text
audio/
css/
effects/
fonts/
icon/
img/
js/
movies/
save/
```

RPG Maker data files:

```text
data/Actors.json
data/Animations.json
data/Armors.json
data/Classes.json
data/CommonEvents.json
data/Enemies.json
data/Items.json
data/Map001.json
data/Map002.json
data/Map003.json
data/Map004.json
data/Map005.json
data/Map006.json
data/Map007.json
data/Map008.json
data/Map009.json
data/Map010.json
data/Map011.json
data/Map012.json
data/Map013.json
data/Map014.json
data/Map015.json
data/Map016.json
data/MapInfos.json
data/Skills.json
data/States.json
data/System.json
data/Tilesets.json
data/Troops.json
data/Weapons.json
```

## Atlas Reservations Applied

Maps:

- 16 Home Island maps were created from the Atlas screen registry.
- Map IDs `1` through `16` match the WO-0021 reservation plan.
- New game start is set to map `2`, coordinates `(8, 6)`, matching the Elara House start target.

Database:

- Actor `1`: `Kai`
- Class `1`: `Sword Bearer`
- Enemies `1`, `2`, `3`, `10`: Home Island enemy rows
- Troops `1`-`5`, `10`: Home Island troop rows
- Skills `1`, `101`, `102`, `110`-`113`: Home Island combat rows
- States `1`, `11`-`13`: Home Island state rows
- Items `1`, `201`: Potion and Sword / Project Excalibur key item
- Weapons `1`, `2`: Practice Sword and Sword / Project Excalibur
- Armor `1`: Plain Clothes
- Tilesets `2`-`6`: RTP placeholder tilesets from the Atlas assignment matrix
- Animations: Atlas-required placeholder animation IDs

State ranges:

- Switches `1`-`200` were initialized with the WO-0021 reserved names.
- Variables `1`-`150` were initialized with the WO-0021 reserved names.
- Common Events `1`-`6` were initialized as Atlas placeholder common events.

## Tooling Added Or Updated

Added:

```text
tools/atlas-import/create_clean_skeleton.py
```

Updated:

```text
tools/atlas-import/audit_rpgmaker_data.py
tools/atlas-import/README.md
```

The audit tool now supports:

```text
--project-root
```

This allows the same read-only audit to compare Atlas export expectations against either the legacy project or the clean skeleton.

## Validation Result

JSON parse check:

```text
json-ok files=30
```

Generated map registry:

```text
1:TWN_Ashford_Exterior
2:INT_Ashford_ElaraHouse
3:INT_Ashford_Shop
4:DGN_SkyreachHill_Path
5:DGN_HiddenCave_Entrance
6:DGN_HiddenCave_Trials
7:DGN_HiddenCave_Sanctum
8:DGN_Glassfield_Ruins_Exterior
9:DGN_SealedNode_Upper
10:DGN_SealedNode_CorePath
11:DGN_SealedNode_Guardian
12:DGN_SealedNode_RelayCore
13:TWN_Rustshore_Docks
14:CUT_Mainland_Departure
15:FLD_Fogfen_Marsh_Field
16:FLD_Fogfen_Deeper_Marsh_Pocket
```

Clean skeleton audit:

```text
found=76 missing=0 warning=0 unknown=71
```

The remaining `unknown` findings are expected. They are the event, transfer, trial-state, and troop-event-page checks that require future RPG Maker event-command parsing. They are not map/database ID conflicts.

## BUILD-0001 Gate

Result: **PASS**.

The clean skeleton removes the WO-0020 map/database collision blockers:

- Missing maps reduced from `16` to `0`.
- Database ID/name warnings reduced from `38` to `0`.
- Missing database rows reduced from `17` to `0`.

## Recommended Next Step

Proceed to **BUILD-0002 - Add Read-Only Map/Event Parser For Atlas Audit** or **BUILD-0002 - Begin Guarded Atlas Apply Tool For Clean Skeleton**.

The safer next step is the read-only parser. It would reduce the remaining `unknown=71` findings by checking map events, transfer commands, switches, variables, common events, and troop event pages before any write-capable importer is introduced.
