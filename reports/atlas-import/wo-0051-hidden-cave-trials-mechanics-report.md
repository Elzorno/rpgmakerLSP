# WO-0051 Implementation Report — Hidden Cave Trials Mechanics (Partial: Event Wiring Pass)

Session budget was constrained (~30% remaining), so this pass scoped to the mechanic
that was actually blocking playability — the Body/Mind trial event logic — and
deferred the Maps005-007 hand-built terrain, which is a much larger, open-ended
piece better done with a full budget and render-verification loop (see
[[feedback-iterative-compiler-render-loop]]).

## Completed

- Wired `EVT-HOM-012A/B/C` (Body Trial reset tiles, Map006 events 7/8/9) per
  `ATLAS-TEC-057`: each is now Player Touch / Below Characters, increments
  `Trial_Body_Attempts`, plays a soft failure SE, and instantly repositions Kai to
  the Body Trial start tile (Map006 `(9, 16)`, chosen just south of the
  `DEC-SCR-HOM-HCV-002-BODY-TRIAL-CHAMBER-BOUNDARY` marker at `(9, 15)` and north of
  the hazard row at `y=18`, since no explicit "start tile" event exists in the map —
  documenting this coordinate choice here since it isn't written down anywhere else).
  A second page (gated on `J1_Trial_Body_Clear` ON) makes the tiles harmless
  pass-throughs once the trial is cleared, per spec.
- Wired `EVT-HOM-013A/B/C` (Mind Trial markers Left/Right/Center, Map006 events
  10/11/12) as the actual left-right-center sequence check against
  `Trial_Mind_SequenceStep` (var 51): each marker validates the required prior step,
  plays a confirm SE and advances the step on success, or resets the step to 0 with a
  buzz + hint text on a wrong marker. The Center marker carries the full completion
  cascade (chime, animation, `J1_Trial_Mind_Clear` ON, the two completion text lines,
  the nested all-trials-clear check that sets `J1_HiddenCave_AllTrialsClear`) — this
  is the same cascade block that used to live on the plaque event, moved here.
- **Fixed a real bug found while doing this**: `EVT-HOM-013` (the Mind Trial start
  plaque, Map006 event 2) was previously wired to complete the whole Mind Trial the
  instant the player interacted with it — it set `Trial_Mind_SequenceStep = 3` and
  `J1_Trial_Mind_Clear = ON` directly, with no marker interaction required at all.
  That meant the marker sequence the spec calls for was decorative; touching the
  plaque alone finished the trial. This was silent because the plaque's own logic
  looked complete in isolation — nothing exercised the actual markers before now.
  Rewired the plaque to only reset `Trial_Mind_SequenceStep` to 0 and show the
  "Observe the order" text, matching `ATLAS-TEC-057`'s `MIND_START` page spec; its
  "already complete" page now checks `J1_Trial_Mind_Clear` (switch 5) instead of a
  self switch, since nothing sets a self switch on this event anymore.
- Confirmed Body Trial's finish tile (Map006 event 1, `EVT-HOM-012`) and the Heart
  Trial (event 3, `EVT-HOM-014`) were already correctly wired per spec in an earlier
  pass — no changes made to those.

## Files Modified

- `TheLastSwordProtocol-Game/data/Map006.json` — events 2, 7, 8, 9, 10, 11, 12
  (Mind Trial plaque, Body reset tiles, Mind markers).

## Files Created

- This report.

## Player-Visible Progress

Hidden Cave's Body and Mind trials are now real obstacles instead of pass-through
gates: stepping on a Body hazard tile bounces Kai back to the start of the lane
(with an attempt counter for later debugging), and the Mind Trial genuinely
requires pressing the left, right, then center markers in order — a wrong marker
resets progress instead of silently doing nothing. The Heart Trial and both trials'
sanctum-gate interaction were already correct and untouched.

## Commands Run

```
/usr/bin/python3 atlas-tools/cli/atlas.py validate
cd ../rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
cd ../rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/hidden-cave-trials-route-audit.md --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

## Validation Result

- `atlas.py validate`: 0 errors, 0 warnings (179 files scanned).
- Map ownership audit: Map005/006/007 remain `generated` (pipeline-writable) as
  expected — not flipped to `hand_authored` since their terrain was not built this
  pass. No hand-authored maps were touched.
- Route audit: `found=228 missing=21 warning=9`. All TRN-HOM-012/013 entries (the
  only route-audit rows that touch Map006) report `found`; every `missing`/`warning`
  row is pre-existing noise unrelated to this change (Fogfen/Glassfield/Rustshore
  reachability-tool gaps, and Map001/026/027 orphan-transfer warnings from other
  work). This audit tool checks map transfers/reachability, not trial event logic,
  so it can't verify the new Body/Mind wiring directly — that needs an actual
  runtime playtest.

## Remaining Issues / Questions

- **Maps005-007 terrain is still bare `generated` scaffolding** — Required Task 3/4
  from WO-0051 (hand-build the terrain from the screen specs + SVG layout guides,
  then flip the ledger to `hand_authored`) is not done. This is the larger remaining
  piece of this work order.
- The Body Trial start-tile coordinate `(9, 16)` was inferred from nearby decoration
  event positions, not from an authoritative source — worth confirming against the
  SVG layout guide (`SCR-HOM-HCV-002-layout-guide.svg`) once someone can view it, or
  simply adjusting after a playtest if it lands somewhere odd.
- No runtime playtest has been done on this pass (no engine available in this
  session) — the event-command wiring was hand-verified against `ATLAS-TEC-057`
  and dumped/inspected structurally, but hasn't been run in RPG Maker MZ itself.
  WO-0047 (Gate A runtime playtest) is already open/blocked on Chris for the same
  reason; this trial mechanic should get the same treatment before calling it
  certified.
- Do not commit (per WO-0051 instruction) — changes are left in the working tree.
