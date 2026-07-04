---
atlas_id: ATLAS-TEC-059
title: Home Island Tileset Assignment Matrix
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-020
  - ATLAS-TEC-040
  - ATLAS-TEC-041
  - ATLAS-TEC-042
  - ATLAS-TEC-053
  - ATLAS-TEC-056
  - ATLAS-TEC-058
related:
  - ATLAS-ART-011
  - IMP-HOM-007
  - IMP-HOM-010
  - IMP-HOM-011
  - IMP-HOM-012
  - IMP-HOM-013
  - IMP-HOM-014
  - IMP-HOM-015
  - IMP-HOM-016
---

# Home Island Tileset Assignment Matrix

## Objective

Assign every Home Island screen to an RPG Maker MZ tileset or approved placeholder tileset so the vertical slice can be mapped, traversed, region-painted, evented, and playtested without waiting for final art.

This document does not create final art assets or modify RPG Maker project files.

---

## Source References

| ID | Reference |
|---|---|
| `ATLAS-TEC-020` | RPG Maker MZ Bible |
| `ATLAS-TEC-040` | Home Island Screen Registry |
| `ATLAS-TEC-041` | Home Island Transfer Registry |
| `ATLAS-TEC-042` | Home Island Event Registry |
| `ATLAS-TEC-053` | Home Island Vertical Slice Readiness Review |
| `ATLAS-TEC-056` | Home Island Combat Database Spec |
| `ATLAS-TEC-058` | RPG Maker MZ Vertical Slice Build Pipeline |
| `ATLAS-ART-011` | Home Island Location Art Prompt Packet |
| `IMP-HOM-007` | Build Home Island Location Art Pipeline |

---

## Placeholder Tileset Policy

Use existing RPG Maker MZ/prototype tilesets for first playable testing.

| Placeholder Tileset | Current RPG Maker Role | Approved Use |
|---|---|---|
| `Outside` | Standard exterior/town/nature tileset | Ashford exterior, Skyreach, Rustshore, Fogfen placeholder maps |
| `Inside` | Standard interior tileset | Elara House and Ashford Shop |
| `Dungeon` | Standard cave/dungeon tileset | Hidden Cave and cave-forward ruin spaces |
| `SF Outside` | Science-fiction exterior tileset | Glassfield old-world exterior placeholder details |
| `SF Inside` | Science-fiction interior tileset | Sealed Node old-world infrastructure placeholder details |

Final custom Home Island tilesets remain desired polish. They do not block first playable testing once this matrix is followed.

---

## Region ID Policy

Region IDs are implementation aids for encounter and special-tile marking. Use them only where they simplify testing.

| Region ID | Use | Notes |
|---:|---|---|
| 0 | Default / no special region | Standard RPG Maker unpainted region |
| 1 | Home field encounter region | Use with Home Field troops from `ATLAS-TEC-056` |
| 2 | Fogfen encounter region | Use with Fogfen troops from `ATLAS-TEC-056` |
| 3 | Fogfen slow bog / dense reed hazard marker | Optional; can also be represented with pathing and passability only |
| 4 | Sealed Node encounter region | Use for low-frequency optional encounters in node approach maps |
| 5 | No-random encounter story/event zone marker | Optional marker for boss chambers, sanctums, and cutscene spaces |

If implementation uses evented encounters instead of map encounter regions, keep these IDs as documentation markers and do not create parallel-process encounter logic without a separate implementation packet.

---

## Tileset Assignment Matrix

| Screen ID | RPG Maker Map Target | Placeholder Tileset | Required Terrain Types | Passability Needs | Region ID Requirements | Encounter Zone Requirements | Transfer / Event Placement Notes |
|---|---|---|---|---|---|---|---|
| `SCR-HOM-ASH-001` | `TWN_Ashford_Exterior` | `Outside` | Village ground, paths, gardens, fences, house exteriors, warm-stone vent, reused metal panels | Houses/fences/vents block; paths clear; north and south/east exits readable | Region 0 only; no encounter regions inside village | None; no random encounters in village | Place Elara House, Shop, optional Elder House transfers; hidden item four steps south of warm-stone vent; NPCs around village center |
| `SCR-HOM-ASH-002` | `INT_Ashford_ElaraHouse` | `Inside` | Cozy home floor/walls, bed, table/chair, hearth or warm-stone equivalent, shelf/keepsake | Walls/furniture block; exit tile clear; player start has free movement | Region 0 only | None | Player start, Elara event, exit transfer, optional keepsake/bookshelf examine |
| `SCR-HOM-ASH-003` | `INT_Ashford_Shop` | `Inside` | Shop floor/walls, counter, shelves, crates/barrels, metal cabinet placeholder | Counter blocks except shopkeeper interaction side; shelves/cabinet block; exit clear | Region 0 only | None | Shopkeeper behind or near counter; exit transfer back to Ashford |
| `SCR-HOM-SKY-001` | `DGN_SkyreachHill_Path` | `Outside` | Hill path, tall grass, wind-swept stones, cliff/overlook, cave entrance, geometric carved stones | Cliff/stone edges block; winding route clear; cave mouth transfer visible | Region 1 optional for very light field encounters; Region 5 near cave/gate if no encounters desired | Optional low-frequency Home Field troops only | Gate/warning near route entry; transfer to Hidden Cave at cave mouth; return transfer to Ashford route |
| `SCR-HOM-HCV-001` | `DGN_HiddenCave_Entrance` | `Dungeon` | Cave floor/walls, entry passage, subtle carved panels, dim blue-white accents | Cave walls block; forward path clear; entry/exit transfers readable | Region 0; Region 5 optional | None preferred | First-entry event near entry; transfer back to Skyreach; transfer forward to trials |
| `SCR-HOM-HCV-002` | `DGN_HiddenCave_Trials` | `Dungeon` | Cave chamber, three separated trial spaces, floor markings, hazard/reset tiles, marker plaques, sanctum gate | Trial boundaries block; Body hazard tiles are passable event triggers; sanctum gate path blocked until trials clear | Region 5 recommended; no random encounters | None | Place Body lane/reset events, Mind markers, Heart pedestal, return transfer, and gated sanctum transfer per `ATLAS-TEC-057` |
| `SCR-HOM-HCV-003` | `DGN_HiddenCave_Sanctum` | `Dungeon` | Small sanctum, central pedestal, symmetrical floor, glass/stone panels, blue-white light | Walls/pedestal block; interaction tile in front of pedestal clear; exit clear | Region 5 recommended | None | Sword pedestal centered; archive text presentation; transfer back to trials |
| `SCR-HOM-GLS-001` | `DGN_Glassfield_Ruins_Exterior` | `SF Outside` | Cracked glass-like panels, concrete/stone ruin, grass/flowers, metal ribs, sealed lower entrance | Ruin edges/ribs block; exploration loop clear; sealed entrance blocks until opened | Region 1 optional for low-risk outside encounters; Region 5 around seal if needed | Optional Home Field troops: Meadow Gel, Ash Rat | Place sealed entrance event, surface fragment, return route, and transfer down after seal opens |
| `SCR-HOM-SND-001` | `DGN_SealedNode_Upper` | `SF Inside` | Stone corridor, embedded metal/glass, cave-machine walls, faint warning lights, simple obstacle | Walls/machinery block; return and forward routes clear | Region 4 optional for low-frequency node encounters; Region 5 near first-entry event | Optional low-frequency Ash Rat/Meadow Gel until construct enemies are defined | First-entry event near entrance; transfer up to Glassfield; transfer forward to core path |
| `SCR-HOM-SND-002` | `DGN_SealedNode_CorePath` | `SF Inside` | Cave-machine connector, cables, glass/metal surfaces, relay-line markings, simple door | Walls/cables block; door event controls forward route; back route clear | Region 4 optional; Region 5 around sealed door if no random encounters desired | Optional one or two simple encounters | Place simple sealed door, transfer back, transfer forward to guardian |
| `SCR-HOM-SND-003` | `DGN_SealedNode_Guardian` | `SF Inside` | Compact boss chamber, central combat space, guardian focal point, closed relay passage | Chamber edge blocks; guardian event blocks before defeat; relay passage blocked until switch | Region 5 recommended | No random encounters; boss event only | Guardian event centered; transfer back; forward transfer appears/unlocks after `J1_Node07_GuardianDefeated` |
| `SCR-HOM-SND-004` | `DGN_SealedNode_RelayCore` | `SF Inside` | Small relay chamber, central relay device, blue-white light, symmetrical old-world floor | Walls/device block; interaction point clear; return route clear | Region 5 recommended | None | Relay device centered; archive message event; transfer back to guardian |
| `SCR-HOM-RST-001` | `TWN_Rustshore_Docks` | `Outside` | Shoreline, wooden dock, boat, hut, lighthouse, sea grass, coastal path | Water blocks except dock/boat interaction; dock edges clear but bounded; return path clear | Region 0 only | None | Dockmaster near hut/boat; boat transfer gated by mainland travel switch; lighthouse examine; return transfer |
| `SCR-HOM-RST-002` | `CUT_Mainland_Departure` | `Outside` | Small dock/boat cutscene area or reused dock strip | Keep path limited; avoid open exploration if cutscene map | Region 5 recommended | None | Autorun/choice departure sequence; transfer to Journey II placeholder |
| `SCR-HOM-FOG-001` | `FLD_Fogfen_Marsh_Field` | `Outside` | Reeds, shallow water, mud, bent tree/post, cable landmark, glowing pool, marsh paths | Deep water/reed walls block; shallow bog may be slow/choke path; entry/exit always clear | Region 2 for marsh encounters; Region 3 for slow bog markers; Region 5 near transfers | Fogfen troops 4 and 5 from `ATLAS-TEC-056` | Entry/exit transfer, deeper marsh transfer, signal clue, cable landmark, hidden item, optional hazard markers |
| `SCR-HOM-FOG-002` | `FLD_Fogfen_Deeper_Marsh_Pocket` | `Outside` | Dense reeds, darker water/mud, submerged cable cluster, signal pool, reward cache | Dense reeds/deep water block; return route always clear; slow choke optional | Region 2 for marsh encounters; Region 3 for dense/slow passage; Region 5 near return transfer | Slightly denser Fogfen troops 4 and 5; still early-game safe | Return transfer, signal pool examine, cable cluster examine, optional reward cache |

---

## Required Terrain By Location

| Location | Required Terrain Set | Placeholder Source | Final Asset Need |
|---|---|---|---|
| Ashford | Village paths, garden patches, timber/stone buildings, fences, warm-stone vent, reused metal panels | `Outside`, `Inside` | Custom Ashford village tiles with subtle old-world salvage |
| Skyreach Hill | Grass, cliffs, stones, carved geometric ruins, cave mouth | `Outside` | Custom sacred-hill and carved-stone accents |
| Hidden Cave | Cave walls/floors, reflective stone, trial markings, pedestal chamber accents | `Dungeon` | Custom Hidden Cave tiles with blue-white interface accents |
| Glassfield Ruins | Cracked glass-like panels, broken concrete, flowers/grass, metal ribs, sealed lower entrance | `SF Outside` | Custom ruin/glassfield tiles |
| Sealed Node | Cave-machine walls, glass/metal panels, cables, warning lights, relay device floor | `SF Inside` | Custom Sealed Node infrastructure tiles |
| Rustshore | Shoreline, docks, boat, hut, lighthouse, sea grass | `Outside` | Custom coastal dock/lighthouse tiles |
| Fogfen | Reeds, shallow water, mud, bent trees, cable landmarks, signal pools | `Outside` | Custom marsh/reed/signal-glow tiles |

---

## Missing Tileset Assets

These final assets are missing or not assigned as final art. They do not block first playable testing because approved placeholders are assigned above.

| Missing Asset | Needed For | First-Playable Status |
|---|---|---|
| Home Island village exterior tiles | Ashford | Use `Outside` |
| Home Island cozy interior/shop tiles | Elara House, Ashford Shop | Use `Inside` |
| Skyreach hill carved-stone accents | Skyreach Hill | Use `Outside` with stone/ruin substitutions |
| Hidden Cave reflective/sanctum tiles | Hidden Cave maps | Use `Dungeon` |
| Glassfield cracked glass/concrete/metal-rib tiles | Glassfield Ruins | Use `SF Outside` |
| Sealed Node cave-machine infrastructure tiles | Sealed Node maps | Use `SF Inside` |
| Rustshore dock/lighthouse coastal tiles | Rustshore | Use `Outside` |
| Fogfen marsh reed/cable/signal-pool tiles | Fogfen | Use `Outside` |

---

## First Playable Passability Rules

- Every transfer route must be reachable with clear walking paths.
- Every critical event must have at least one adjacent interaction tile.
- Decorative old-world panels, vents, relay devices, and cables should block movement unless explicitly used as floor markings.
- Water is impassable except shallow marsh tiles marked for passable choke paths.
- Body Trial reset tiles in `SCR-HOM-HCV-002` must be passable Player Touch events.
- Boss and relay chambers should avoid random encounters.
- Optional Fogfen slow bog behavior may be implemented with visual chokepoints only if region-based slow logic is not available.

---

## Encounter Zone Rules

| Zone | Screens | Troops | Notes |
|---|---|---|---|
| Home Field | `SCR-HOM-SKY-001`, optional parts of `SCR-HOM-GLS-001` | Troops 1, 2, 3 from `ATLAS-TEC-056` | Low frequency; do not interrupt early story flow |
| Fogfen | `SCR-HOM-FOG-001`, `SCR-HOM-FOG-002` | Troops 4, 5 from `ATLAS-TEC-056` | Optional branch; keep safe and escapable |
| Sealed Node | `SCR-HOM-SND-001`, `SCR-HOM-SND-002` | Existing Home Field troops or no random encounters until construct enemies exist | Use sparingly; boss is the main combat beat |
| Boss | `SCR-HOM-SND-003` | Troop 10 from `ATLAS-TEC-056` | Evented battle only |
| Safe / Story | Ashford, interiors, Hidden Cave trials/sanctum, Rustshore, Relay Core, cutscene map | None | No random encounters |

---

## Implementation Checklist

- Create or verify RPG Maker tileset database rows for `Outside`, `Inside`, `Dungeon`, `SF Outside`, and `SF Inside`.
- Assign every `SCR-HOM-*` map to the placeholder tileset listed in this matrix.
- Paint passability before placing events.
- Paint encounter regions only on maps that have encounter zones in this matrix.
- Keep all safe/story maps encounter-free.
- Place transfers after passability is confirmed.
- Place story events after transfer routes are testable.
- Log any final-art substitution as polish, not as a first-playable blocker.

---

## Build-Readiness Decision

`BLK-HOM-004` is cleared for first playable testing by this matrix.

Final custom Home Island tileset production remains non-blocking asset polish unless a later work order changes the visual target from placeholder playability to final-art production.

---

## Validation

Run:

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py validate
```

Expected result:

- 0 errors,
- 0 warnings.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island tileset assignment matrix |
