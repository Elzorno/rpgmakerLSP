# Ashford Exterior MapVision Candidate (WO-0073)

Date: 2026-07-15
Canon: `MV-HOM-ASH-001@0.1` / `AVCP-HOM-ASH-001` / `IMP-HOM-017@0.2`
Status: **Rejected by Chris on 2026-07-15.** Not installed. Production
`Map001.json` was not read for writing and was not modified.

## Human Decision

Rejected. Chris found the candidate still reads as mechanical/procedural,
with no organic flow -- "built by a machine, no soul" -- and that paths do
not line up with building doors. Direct comparison against the reference
maps confirms it is not close. Recorded via
`quality_gate.apply_human_decision(..., decided_by="Chris")` in
`gate_evidence.json`.

This is the **third** independent rejection carrying essentially this same
complaint (WO-0024's original auto-generated overworld; the 2026-07-14 v2
hand-authored-tile rebuild; now this MapVision/TileAssembly candidate) across
three structurally different generation approaches. The one concretely named,
isolated bug -- path connectors drawn zone-center-to-zone-center instead of
door-anchor-to-door-anchor -- is fixable on its own. "Mechanical / no organic
flow / no soul" points at something deeper: `SemanticAssembler`'s placement
model (axis-aligned rectangular zones, compass-direction BFS adjacency,
straight-line paths) can place individually-correct, Chris-approved
assemblies while still composing them into a grid-of-boxes layout, because
organic curvature, irregular offsets, and non-orthogonal massing are not
expressible in that model at all -- not parameters it got wrong this time.
Worth a direct conversation with Chris about algorithm-level investment
before a fourth attempt on the same underlying placement approach. See the
WO-0073 work-order file's "Root-cause read" section for the full argument.

## What this is

The first Ashford candidate produced through the new MapVision/TileAssembly
compiler pipeline (WO-0071/0072) rather than hand-authored tiles
(`build_ashford_exterior_candidate.py`, the 2026-07-14 v2 rebuild, human-
rejected) or the original hand-built production `Map001.json`. Geometry comes
from `SemanticAssembler` resolving a new production-scale Ashford
archetype/graph (`ARCH-EXTERIOR-ASHFORD-PRODUCTION`, 40x32) against the real,
approved `MV-HOM-ASH-001` MapVision and the real Ashford `TileAssembly`
catalog. Every building and most landmarks are verified, catalog-enabled
assemblies Chris already approved during WO-0070 — not hand-placed or
guessed tiles.

Built by Claude Code in one continuous session (WO-0071 -> WO-0072 -> WO-0073),
without Codex, at Chris's direction ("proceed" after each prior work order).

## Human decision

**Not yet made.** This report and the render below are the input to that
decision, not a recommendation to install. Per WO-0073's own constraints, no
automatic promotion happens regardless of how this looks; only Chris can
accept it, and only a later, separate, explicit step would install it over
`Map001.json`.

## Render

`ashford-mapvision-candidate-render.png` — composited from the real
production tileset (`Outside`, `tilesetId: 2`) using the same renderer
(`compiler/style_study/wo0060/render_map.py`) the v2 rebuild used. Magenta
boxes mark event positions (renderer convention; not in-game visuals).

## What is real vs. what is a known gap

**Real, verified, not invented:**
- Elara House, Shop, Inn, and Elder House are the exact Chris-approved
  authored-kit assemblies (`TASM-ASHFORD-ELARA-HOUSE-AUTHORED`,
  `-SHOP-AUTHORED`, `-INN-AUTHORED`, `-ELDER-HOUSE-AUTHORED`), composited
  tile-for-tile from their own verified `layered_cells` — no tile ID in any
  building was computed or guessed by this script, only relocated.
- The warm-stone vent is the Chris-approved `TASM-ASHFORD-WARM-VENT-AUTHORED`.
  Its own collision mask is used directly.
- The two broadleaf trees are the reference kit's verified, complete
  `TASM-ASHFORD-TREE-BROADLEAF-01` (2x2, canopy+trunk) — the exact fix for
  the v2 candidate's documented half-tree rejection.
- All 27 current Map001 events are preserved **byte-for-byte** in their
  pages/conditions/command lists (verified programmatically: only `x`/`y`
  differ from production `Map001.json`). Their new positions come from an
  explicit, auditable per-event mapping
  (`build_ashford_mapvision_candidate.py::EVENT_RECONCILIATION`), not
  inferred or hand-picked. The hidden item is placed exactly 4 tiles south of
  the warm-stone vent's actual composited position, per `CA-ASH-HIDDEN`.
- Door-linked transfers (Elara House, Shop, Inn) use each building's own
  verified door anchor, not a generic zone-center point.
- The WO-0072 dual gate passes both audits independently: structural (route/
  connector/manifest) and visual-proxy (complete/verified assemblies,
  building-height cap, family differentiation, dominant landmark) —
  see `gate_evidence.json`. `not_yet_automatable` lists the 9 AVCP
  constraints that need an actual blind-human-panel render review (first-
  camera salience, color/material share, density/path-rhythm), which this
  gate does not and cannot claim to satisfy automatically.
- A conservative BFS route audit from Elara House's door reaches 1120 cells
  and finds zero unreachable events (`route_audit.json`).

**Known gaps, not silently hidden:**
- The roofed well, humming panel, and patched-metal fence
  (`ASH-CUSTOM-WELL-ROOFED-01`, `ASH-CUSTOM-PANEL-01`, `ASH-CUSTOM-FENCE-01`)
  are **not visually composited**. Their art lives on the human-approved
  custom tileset `Ashford_Custom_B.png`, which is not yet registered as a
  tileset B-sheet in the production Game's `Tilesets.json`. Registering a new
  tileset slot is a real production configuration change and was kept out of
  scope for a disposable candidate — see `pending_custom_tileset_registration.json`.
  Their footprints are reserved (marked impassable) so the route audit stays
  honest about their eventual presence, but they render as plain ground here.
  The WO-0072 gate's `visual_proxy` pass reflects that Chris already approved
  these *bindings*, not that this specific render shows them — those are two
  different, both-true statements.
- The Elder House has a facade and door graphic but **no working transfer
  event**: `TRN-HOM-040` is reserved, not yet built in production Map001
  (only 27 events exist today, none of them an Elder House door), and adding
  a new event would violate WO-0073's "do not invent canon" constraint.
- Path connections between buildings are simple straight-line connectors
  between zone centers (a structural/audit-focused simplification), not a
  hand-tuned curved civic spine like IMP-HOM-017 describes or the v2
  candidate attempted. `AVCP-HOM-ASH-001`'s `ASH-PATH-003`/`ASH-RHYTHM-001`
  (bend count, compression/release) are in `not_yet_automatable` for exactly
  this reason.
- The Elder House's two trees (forest_edge zone) sit immediately adjacent to
  its roofline with no visual buffer — geometrically correct (their zone
  does not overlap the building's), but tight enough to be worth Chris's own
  eye before calling it settled; `AVCP-HOM-ASH-001`'s density/negative-space
  constraints are human-review, not hard-gated.
- `village_cottage` has zero catalog-enabled candidates today (both
  reference-kit variants remain `study_only`) and is not part of this
  candidate, matching MV-HOM-ASH-001's own "non-enterable village cottages"
  requirement being left for a future authoring pass.

## Real bugs found and fixed while building this (not Ashford-specific hacks)

Building a production-scale, many-zone, many-event candidate exercised paths
WO-0071's smaller disposable fixture never hit. All fixes are in the shared
`assembler.py`/`tile_assembly_catalog.py`, verified against the existing
54-test compiler suite (unaffected) plus new coverage:

1. **Entry-zone south-anchoring**: `_place_zones` hardcodes the entry zone
   flush against the map's south edge, so it only has 3 usable placement
   sides, not 4 — invisible in WO-0071's small fixture (whose entry zone had
   only 2 children) but a hard placement failure once arrival_domestic needed
   4. Fixed by moving `route_south`'s beats onto `arrival_domestic` itself
   (which also matches production Map001's real geography: the south route
   mouth and Dock Messenger already sit right next to Elara's door).
2. **Beat collision**: every beat in a zone previously collapsed onto that
   zone's exact center point — harmless with one beat per zone (every prior
   fixture) but a real bug with several (an NPC, a treasure object, and a
   decoration event all landing on the identical tile). Fixed with
   `_distribute_beat_points`, which spreads a zone's beats across distinct
   interior cells, excluding any cell already occupied by a module or
   landmark placed in the same zone. Verified: zero duplicate event
   positions in the final candidate (was 5 duplicate pairs before the fix).
3. **Zone-vs-footprint sizing**: a zone whose `min_area` is smaller than its
   own building module's footprint leaves zero free space for that
   building's own frontage beats (crate, sign, etc.) — found on
   `shop_frontage`. Fixed by sizing zones generously above their module's
   footprint when they carry their own beats.

None of these are Ashford-only patches; they are corrected in the shared
compiler code and covered by the existing test suite.

## Files

- `Map001.mapvision-candidate.json` — the disposable candidate map (never
  written to `TheLastSwordProtocol-Game`).
- `map_plan.json` — the engine-neutral MapPlan this candidate was serialized
  from, with `tile_assembly_*` provenance on every obstacle/landmark.
- `generation_manifest.json` — provenance: seed, archetype/layout_family/
  MapVision refs, and every TileAssembly binding used.
- `gate_evidence.json` — WO-0072 dual-gate result plus concept/render
  references and the pending human decision block.
- `route_audit.json` — BFS reachability and event-placement audit.
- `structural_preview.txt` — engine-neutral ASCII zone layout.
- `pending_custom_tileset_registration.json` — the 3 assembly IDs whose art
  needs a Tilesets.json B-sheet registration before they can render.
- `ashford-mapvision-candidate-render.png` — the render above.

## Disposition

Preserve as evidence for WO-0073/WO-0074. Do not install over production
`Map001.json` without Chris's explicit acceptance recorded via
`quality_gate.apply_human_decision(..., decided_by="Chris")`, and even then
only as a separate, deliberate installation step this report does not take.
