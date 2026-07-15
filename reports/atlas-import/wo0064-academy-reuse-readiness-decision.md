# WO-0064 — Academy Reuse Readiness Decision (Independent Evaluation)

Reviewer: Claude Code (Independent Academy Evaluation), reviewing Codex's `WO-0063`
First Generated Settlement Vertical Slice. This is a genuinely independent
review, not a rubber stamp of `WO-0063`'s own self-reported "6/6 hard-pass" —
every claim below was checked directly against the actual evidence
(`rpgmakerLSP/reports/atlas-import/wo0063/`), not taken on the strength of the
prior report's prose.

## Evidence Reviewed

- All 6 candidate renders (`candidate.render.png`), full resolution, not just the gallery thumbnail.
- All 6 `settlement.map_plan.json`, diffed pairwise (same-style-different-seed, and same-seed-different-style).
- All 6 `quality.json` advisory/hard-gate results.
- All 6 `candidate.diagnostics.json` route audits.
- All 6 `candidate.manifest.json` provenance/ownership records.
- The actual scoring implementation, `AtlasStudio/atlas-tools/mapgen/compiler/quality_auditor.py::audit_generated_candidate` (read directly, not inferred from its output).
- Both exterior `TilePalette` instances (`temperate.exterior.palette.json`, `coastal.exterior.palette.json`).
- Re-ran `tools/atlas-import/generate_wo0063_settlement.py` from a full backup and diffed the entire output tree against the pre-existing one.
- `settlement.structural.txt` (ASCII zone map) for the zone legend behind the render.
- `fixture-project/map_ownership.json` for ownership-boundary confirmation.

## Findings

Each finding cites the specific candidate/seed, the exact evidence, and the
specific rule it bears on — not a vague impression.

### F1 — Reproducibility: CONFIRMED, no caveats

Re-ran `generate_wo0063_settlement.py` against a full backup of
`reports/atlas-import/wo0063/`. `diff -rq` across the entire regenerated tree
(6 candidates x 9 files each, plus palettes/gallery/index) reported **zero
differences**. `WO-0063`'s "exact regeneration from recorded seed and
versions" acceptance criterion holds, independently verified, not just trusted.

### F2 — Hard gates: CONFIRMED, genuinely robust

`quality_auditor.py`'s hard-gate checks (reachability, interaction-ring
completeness, connector/zone alignment, obstacle clearance, transfer
round-trip identity, event-anchor identity, RPG Maker shape validity, tile
provenance against the verified palette, manifest/provenance completeness)
are real structural checks, not proxies — read the source directly to confirm
each one tests what its name claims. All 6 candidates pass all of them
(`hard_findings: []` in every `quality.json`; `route_audit.result: "pass"`,
zero `interaction_ring_failures` in every `candidate.diagnostics.json`).
Ownership boundaries are correctly scoped: each candidate's own
`fixture-project/map_ownership.json` marks its single disposable `Map001` as
`generated`, isolated inside the report tree — the real `TheLastSwordProtocol-Game`
project was not touched by this review or by `WO-0063`.

### F3 — Advisory "doctrine" checks are coarse structural proxies, not doctrine measurements

Read `quality_auditor.py:283-296` directly. Every advisory check is a cheap
structural proxy, not a measurement of the actual classic-JRPG doctrine text
in `academy/knowledge/classic-jrpg-feel.md`:

- `compact_meaningful_travel` = `width <= 30 and height <= 24 and traversable_areas non-empty`. This is a **pure size gate**. It has nothing to do with whether "longer travel earns its duration through danger, anticipation, discovery, or narrative pressure" (the doctrine's actual wording). All 6 candidates are 40x30 (confirmed in `settlement.map_plan.json.dimensions`), which fails only because 40 > 30 — a size fact, not a pacing judgment.
- `curiosity_hook` = `landmark or optional_branch`, where `landmark` is `any(item.get("dominant") for item in plan["landmark_slots"])` — **the exact same boolean that separately satisfies `dominant_landmark`**. In every one of these 6 candidates, the only `dominant: true` landmark is the well plaza (`civic_well_landmark`). That means `curiosity_hook: True` in every `quality.json` is driven entirely by the well, and provides **zero independent evidence** that the actual `CURIOSITY-GARDEN` zone (a separate, non-dominant `event_anchor`) reads as a curiosity hook at all. See F5 below for what that zone actually looks like.
- `compression_release` = `obstacles exist and reachable_cells >= half of interior` — presence-of-furniture plus a reachability floor, not a measurement of "alternate confined connectors with rooms, squares, vistas... to control tension," which is what the doctrine actually asks for.
- `selective_density` = `0.01 <= obstacle_area_fraction <= 0.35` — a very wide band (1%-35%). All 6 candidates measure `0.0789` (7.89%), comfortably inside the band but close to its low end.
- `immediate_place_identity` = `len({binding role in palette if role in {"floor","wall","landmark","edge_dressing"}}) >= 3`. **This check is comparing against the wrong vocabulary for this palette.** Both exterior palettes (`temperate.exterior.palette.json`, `coastal.exterior.palette.json`) actually use the role set `{ground, road, building, threshold, landmark, service, dressing}` — a legitimately rich 7-role vocabulary — but the check only recognizes the literal strings `floor`/`wall`/`edge_dressing` (interior-palette vocabulary from `WO-0060`), which this exterior palette doesn't use at all (it uses `ground`/`building`/`dressing` instead). Only `landmark` overlaps, so the check counts 1, not the true 7, and fails. **This reads as a bug in `quality_auditor.py`, not a genuine identity failure** — flagged for Codex's reproducibility/evidence audit specifically, since fixing the role-name mismatch (or generalizing the check) would very likely flip this result without changing the candidate at all, which is exactly the kind of scoring-artifact risk `WO-0064`'s acceptance criteria ask to be caught.

**Conclusion on F3:** none of the 5 "True" advisory checks should be read as
confirmed doctrine compliance, and the 1 "False" identity check (`immediate_place_identity`)
should not be read as a confirmed doctrine failure either — it is more likely
a scoring bug. This is precisely why `WO-0064` requires an independent human
visual pass rather than trusting the score in isolation. See F4-F6 for that
independent pass.

### F4 — Independent visual finding: Shop/Inn/House are not visually distinguishable as building types

Direct inspection of `temperate-seed-6301/candidate.render.png` (full
resolution, not the gallery thumbnail): all three service buildings (Shop at
~x=9,y=8-14; Inn at ~x=30,y=8-14; House at ~x=9,y=19-25) use **the same
building sprite/silhouette**, differentiated only by a small overlay: the Shop
carries a shield-and-`!` sign icon, the Inn carries an "INN" text label, and
**the House carries no sign or icon at all** — it is identified only by
process of elimination (the one building with neither icon nor label). This
directly contradicts `classic-jrpg-feel.md`'s "Readable place identity"
requirement ("their routes, edges, focal objects, and room rhythms should
read differently") at the building level, and falls noticeably short of this
project's own already-accepted bar: Ashford's hand-built Elara House, Shop,
and Inn (`Map001`-adjacent buildings, accepted earlier this session) are
visually distinct structures, not one shared shell with a signboard swapped.
Reproducible in all 6 renders — not seed-dependent.

### F5 — Independent visual finding: the curiosity hook is an undressed placeholder

`settlement.structural.txt`'s zone legend identifies zone `7 = curiosity_garden`,
and `settlement.map_plan.json.event_anchors` places a
`CURIOSITY-GARDEN` / `optional_curiosity_hook` anchor at `(30, 21)`. In the
actual render, that position is a **bare unstyled magenta event-marker
square** sitting in open ground near three small generic flower sprites —
visually identical in treatment to the plain door-transfer markers under each
building's threshold, with no distinct prop, no chest, no NPC, and no ground
texture change to mark it as worth investigating. This does not meet the
doctrine's actual bar for a curiosity hook ("a reason to exist: reward,
shortcut, character moment, world detail, risk, or a visible deferred goal")
— there is nothing at that location a player could perceive as a hook rather
than an empty corner of the field. As F3 notes, the automated `curiosity_hook: True`
result does not contradict this finding, because it isn't actually measuring
this zone. Reproducible in all 6 renders.

### F6 — Independent visual finding: three of six candidates are structurally duplicate, not diverse

Diffed `settlement.map_plan.json` pairwise across the three temperate seeds.
`temperate-seed-6301` and `temperate-seed-6303` select the **identical**
`variant_id: "standard"` with no rotation or reflection — their `MapPlan`s
are structurally identical (only `blueprint_id`/`generation_seed`/manifest-ref
metadata differ). `temperate-seed-6302` selects `variant_id: "mirrored"`
(shop/inn plots swapped left-right around the civic spine) — a real but
minor difference, and one that is barely perceptible in a top-down render
where Shop and Inn already look like the same building (see F4). **Net
result: of the 3 seeds tested, only 2 distinct visual layouts actually
exist**, and the specific pairing tested (6301/6303) happened to collide.
This is not disclosed anywhere in `WO-0063`'s own report, which describes
"six disposable candidates" without noting that half of them are
near-duplicates of the other half. Likely cause: `LAY-SETTLEMENT-CIVIC-SPINE`
has very few authored variants (plausibly only 2) relative to the number of
seeds being used to demonstrate variety — the same class of issue this
project's `WO-0059` report flagged for `LAY-INTERIOR-SHOP`/`INN`/`HOUSE`
before more tiers were authored.

### F7 — Independent visual finding: real, but the honest, disclosed kind

The temperate/coastal comparison genuinely works: diffing
`temperate-seed-6301` against `coastal-seed-6301` (same seed) shows **zero
structural differences** — the entire delta is ground color (green vs. pale
tan) and a road edge-trim treatment (a thin white fringe appears around roads
in the coastal variant only). Buildings and road tiles themselves are pixel-identical
between styles. This is a genuine pass of "the same `MapPlan` reads visibly
as two different environments" — achieved exactly as the architecture
promises (structure fixed, style substituted) — but it is a **shallow**
pass: the distinction is ground-color-only, with no coastal-specific building
or road material, which is exactly the limitation `WO-0060`'s own study
document already disclosed (no purpose-built coastal props exist in this
asset library). Not a new problem; correctly anticipated in advance.

### F8 — Density reading echoes a previously-confirmed human finding on this project

`obstacle_density: 0.0789` (7.89%) is technically inside the automated
`selective_density` passing band (1%-35%), but independent visual inspection
of the render shows a very open, sparsely dressed field: 4 corner trees, a
handful of flowers, one well, three generic buildings. This is worth flagging
specifically because **this exact failure mode was already raised as a real
human playtest finding on this project**: `WO-0047`'s Gate A playtest
(`rpgmakerLSP/reports/atlas-import/wo-0047-gate-a-lives-playtest-fix-pass-report.md`)
recorded Chris's own direct feedback that Ashford's hand-built exterior "feels
barren" compared to Dragon Quest's density of searchable objects and NPCs
with stories. This generated settlement has no searchable objects, no NPCs,
and even less decoration than the since-fixed Ashford exterior. The automated
check passing on a technicality does not mean this risk is closed.

## GO / CONDITIONAL GO / NO-GO

**CONDITIONAL GO.**

The underlying architecture is sound and should not be discarded or
re-designed: determinism is real and independently verified (F1), the hard
safety gates are genuine and all pass (F2), ownership/provenance boundaries
are correctly scoped, and the temperate/coastal style substitution mechanism
works exactly as designed (F7). This is not a NO-GO — nothing here indicates
the compiler, assembler, or contract is broken.

It is also not a clean GO. Three concrete, falsifiable content-quality gaps
(F4, F5, F6) and one scoring-tool bug (F3's `immediate_place_identity`
mismatch) should be addressed — or at minimum explicitly acknowledged and
scoped as known limitations — before this system is trusted to generate
dungeon content or anything approaching production output. None of these
require an architecture change; all four are bounded, specific fixes.

**This recommendation does not substitute for `WO-0063`'s own still-outstanding
requirement**: Chris has not yet performed the live RPG Maker MZ visual and
passability inspection recorded in `WO-0063`'s "Live Review Result" (still
"Pending" as of this review). Per `WO-0064`'s own acceptance criteria, "No
dungeon work begins without Chris's approval of the readiness decision" —
this document is the readiness *decision recommendation*, not that approval.

## Required Remediation (bounded, not architectural)

1. **F4**: give House a distinguishing sign/icon (matching Shop's and Inn's
   existing treatment), or otherwise visually differentiate the three
   building exteriors — even a roof-color or trim variation per archetype
   would clear this.
2. **F5**: bind a real prop (not a bare event marker) to the curiosity-garden
   anchor, or add a `landmark_slots` entry for it so it gets the same
   dominant-landmark treatment the well plaza gets.
3. **F6**: author at least one more `LAY-SETTLEMENT-CIVIC-SPINE` variant (or
   widen the existing variants' weight distribution) so 3 seeds reliably
   produce 3 distinct layouts, and disclose the current variant count in any
   future candidate-gallery report rather than only reporting seed count.
4. **F3**: fix `quality_auditor.py`'s `immediate_place_identity` check to
   read the palette's actual role vocabulary (or generalize the check to not
   hardcode interior-palette role names) — a scoring-only fix, does not touch
   any candidate content.
5. **F8** (softer, worth tracking not blocking): consider whether a
   settlement vertical slice should ship with any searchable/NPC placeholder
   density hook, given this project's own recorded human feedback on exactly
   this failure mode.

None of these require touching the `MapIntent`/`GameplayGraph`/`BuildingArchetype`/
`LayoutFamily`/`Connector`/`Module`/`StylePack`/`MapPlan`/`GenerationManifest`
contract itself (`WO-0056`) or the assembler's core algorithm (`WO-0058`).

## Recommended Next Work Order

**Do not start dungeon-grammar work yet.** Recommend a short, bounded
follow-up (could be scoped as part of `WO-0063`'s own remediation rather than
a new number) addressing items 1-4 above, followed by Chris's still-pending
live RPG Maker review of at least one candidate. Dungeon generation is a
reasonable next investment once that remediation lands and Chris's live
review is recorded — not before, per this decision's own CONDITIONAL GO
status and `WO-0064`'s acceptance criteria.

## Commands Run

```bash
cd rpgmakerLSP
cp -r reports/atlas-import/wo0063 /tmp/wo0063_before
python3 tools/atlas-import/generate_wo0063_settlement.py
diff -rq reports/atlas-import/wo0063 /tmp/wo0063_before   # 0 differences
```

Plus direct reads of `quality_auditor.py`, all 6 `quality.json`/`candidate.diagnostics.json`/
`candidate.manifest.json` files, both exterior palettes, `settlement.structural.txt`,
and full-resolution visual inspection of all 6 `candidate.render.png` files.

## Validation Result

- Reproducibility: independently re-verified, 0 diff across full output tree.
- Hard gates: independently re-verified by reading `quality_auditor.py` source, not just trusting `quality.json` output — all 6 candidates genuinely pass.
- `atlas.py validate`: see `WO-0064`'s own Implementation Report in the work order file (this review touched no `atlas/docs/` files).

## Remaining Issues / Questions

- Chris's live RPG Maker MZ review (`WO-0063` task 6) is still outstanding — this document does not close that requirement.
- The `quality_auditor.py` role-vocabulary bug (F3) should be confirmed with Codex directly, since it's their tooling; this review reads the source but did not modify it (evaluation-only, per `WO-0064`'s own constraints).
- This review did not evaluate `WO-0062`'s interior-only candidate gallery in the same depth — scoped to `WO-0063`'s settlement slice specifically, per `WO-0064`'s dependency on `WO-0063`.
