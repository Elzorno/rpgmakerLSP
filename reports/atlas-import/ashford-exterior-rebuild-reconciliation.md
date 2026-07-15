# Ashford Exterior Rebuild Reconciliation

Date: 2026-07-14  
Target: `SCR-HOM-ASH-001` / `TheLastSwordProtocol-Game/data/Map001.json`  
Scope: Design reconciliation only; Map001 was not modified.

## Outcome

The supplied classic-JRPG village guide is approved as an influence, not as a
replacement for Ashford canon. `SCR-HOM-ASH-001` v0.2 and `IMP-HOM-017` v0.2
are the reconciled sources for the later rebuild.

## Reconciliation Matrix

| Supplied guide element | Canon evidence | Disposition | Rebuild instruction |
|---|---|---|---|
| 60x50 map | SCR-HOM-ASH-001 and IMP-HOM-017 recommend a compact approximately 40x32 first town | Rejected | Keep Map001 exactly 40x32 |
| West/north/east cliff enclosure; south-only opening | Canon requires north Skyreach, east Glassfield/Fogfen, and south Rustshore routes | Adapted | Use partial cliff/tree valley framing with four deliberate route openings |
| Curving packed road | Canon requires a common path and readable navigation | Adopted | South road curves into the square and branches visibly to every building and exit |
| Central roofed well and worn square | Compatible with warm ordinary village tone; current map already has well dressing | Adopted | Make the well the ordinary civic landmark without displacing the vent/panel identity landmarks |
| Northeastern natural stream | No canonical Ashford river; old factory heat/water infrastructure is established | Adapted | Optional narrow old-facility drainage channel on the east; never dominant or route-blocking |
| White plaster and slate cottages | Canon describes timber homes and repurposed old metal | Adapted | Timber-dominant shells with pale plaster infill, dark roofs, and reused metal details |
| Largest Inn north/northwest | DDR-0005 authorizes the Inn and TRN-HOM-031 | Adopted | Largest public façade, visually distinct from Shop/Elara doors, with a working Map026 round trip |
| Shop porch and supply clutter | Compatible with canonical Shop | Adopted | Add porch, barrels, crates, and sacks without changing inventory or event logic |
| Blacksmith workshop, forge, hammer loop | No canonical Ashford blacksmith, service, event, or dialogue | Adapted/deferred | Silent visual repair shed only; no NPC, forge service, hammer loop, inventory, or story beat |
| Three to four residential cottages | Ashford is a small lived-in village; only specified interiors may be enterable | Adapted | Two or three non-enterable cottage shells plus Elara House; no fake functional doors |
| Farms, gardens, coop, firewood, orchard | Canon explicitly requires gardens and farmer/warm-stone texture | Adopted | Compact southwest farm/garden cluster that preserves the hidden-item clue and walkability |
| Dense ancient forest boundary | Compatible with Home Island and Skyreach direction | Adopted | Dense tree/cliff framing with readable exit corridors and no hidden transfer edges |
| Generic distant ancient pillars | Canon old world is factory/maintenance infrastructure used as ordinary scrap | Adapted | Broken factory ribs, maintenance frames, and panel fragments; technology remains subtle |
| Day/night tint, lantern/window swapping, BGS transitions | No project-wide system is established for this rebuild | Deferred | Do not invent local systems; future system requires its own canon/work order |
| Chimney smoke particles | Not required and would add a local event system | Deferred | Static chimneys allowed; animated smoke only under a later system decision |
| Town1-style peaceful BGM and zero encounters | Existing Map001 uses Town1 and canon requires no encounters | Adopted | Preserve current BGM and zero-encounter behavior |

## Canon That Must Survive Unchanged

- Functional transfers: `TRN-HOM-002`, `003`, `005`, `007`, `015`, `027`, and
  `031`, including Skyreach gating and current downstream destinations.
- Required events and their authored pages: Child, Farmer, Skyreach Joker, Dock
  Messenger, Hidden Item, Tremor Trigger, Village Elder, vent, and panel.
- The hidden item remains exactly four steps south of the warm-stone vent.
- Elara House, Shop, and Inn doors round-trip to their existing interiors.
- Existing searchable pot, crate, barrel, and jug events remain available.
- No random encounters and no new story, named NPC, quest, service, switch, or
  local environmental system.
- Map001 remains `hand_authored`; no generator may rewrite it.

## Rebuild Sequence

1. Snapshot and audit the current Map001 event/transfer payloads.
2. Rebuild terrain and façades at 40x32 around frozen semantic anchors.
3. Reposition anchors only where required by the new geometry; never rewrite
   their behavior merely for layout convenience.
4. Verify every door, NPC, examine event, hidden item, and boundary transfer by
   passability-aware reachability.
5. Render the result and compare it against the reconciled brief.
6. Perform a live RPG Maker MZ visual and runtime review before acceptance.

## Approval Boundary

This reconciliation authorizes a narrowly scoped hand-authored Map001 rebuild.
It does not authorize automatic production-map generation, a map-size increase,
new canon, or changes to interior maps. The production map has intentionally not
been touched during this reconciliation pass.
