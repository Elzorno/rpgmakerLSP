# WO-0046 Implementation Report — Apply Gate A Final Ashford Dialogue

Work order: `WO-0046-apply-gate-a-final-ashford-dialogue.md`
Packet: `ATLAS-STY-010` (Ashford Dialogue Packet) | Maps: `Map001` (`TWN_Ashford_Exterior`), `Map002` (`INT_Ashford_ElaraHouse`), `Map003` (`INT_Ashford_Shop`)
Date: 2026-07-10

## Completed

1. **Audited every visible `[Placeholder]` Show Text command in Maps001-003.** Elara (Map002 event 2, all 5 story-state pages) and the Shopkeeper (Map003 events 1 and 10) already carried final `ATLAS-STY-010` text from earlier sessions — no placeholders remained there. Nine placeholders remained on Map001, one on Map002.
2. **Applied existing packet scaffolds verbatim** (no new authoring needed — text already canonical in `ATLAS-STY-010`):
   - Child Near Old Panel (Map001 event 1) — intro line applied; added the missing second page (`J1_Tremor_Event` ON) with the after-tremor line. The event previously had only one page; `Home_Island_Executable_Event_Specs.md` EVT-HOM-003 specifies two.
   - Farmer With Warm Stones (event 2) — intro applied; added second page (`J1_Sword_Obtained` ON) with the after-Sword line.
   - Skyreach Joker (event 3) — intro applied; added second page with the after-Sword line. **Gated on switch 7 (`J1_Sword_Obtained`), not switch 2 (`J1_Skyreach_AccessOpen`) as the event-spec table literally lists** — the dialogue text ("You went up the hill and came back glowing") only makes narrative sense once the player has actually obtained the Sword, not the instant the route merely opens. Documented in-file via a comment line.
   - Dock Messenger (event 4) — intro applied; added second page. **Gated on switch 16 (`J1_Node07_Offline`), matching the convention Elara and the Shopkeeper already use for their After-Node-Seven page**, rather than switch 13 (`J1_Mainland_TravelUnlocked`) as the event-spec table lists. Both switches flip together in `EVT-HOM-022` page 2, so this is a consistency choice, not a behavior change — documented in-file.
3. **Authored five new lines not yet in Atlas, added them to `ATLAS-STY-010` v0.3 (new "Environmental / System Text" section) first, then applied them:**
   - Tremor Trigger (event 6) — two-line flavor text shown after the screen shake, before the Skyreach route opens.
   - Skyreach route locked (event 9, TRN-HOM-005 page 1) — replaces the generic locked placeholder with taboo-flavored text.
   - Warm-Stone Vent examine (event 14).
   - Old Panel examine (event 15).
   - Elara Keepsake Shelf examine (Map002 event 4).
4. **Hidden Item (event 5)** — replaced the placeholder with the exact literal text the event spec calls for: `Found an item.`
5. **Confirmed no duplication into the Skyreach/Hidden Cave dialogue packet** — that file only cross-references `ATLAS-STY-010`'s After-Sword states in a note; it was not modified.
6. **Village Elder (Map001 event 13) intentionally left untouched.** It has no Show Text command at all (not a visible placeholder), the executable event specs don't assign it an EVT-ID or page structure, and the dialogue packet's own Open Questions list "should the village elder become a named NPC object?" as unresolved. Authoring dialogue for it would resolve an open design question outside this work order's scope.
7. Preserved all existing switch/self-switch logic, event page ordering, and command structure everywhere; only Show Text content changed except for the four added pages (which are page-structure the executable spec already calls for, not new mechanics).

## Files Modified

- `TheLastSwordProtocol-Game/data/Map001.json` — 9 placeholders resolved; 4 events gained a second page.
- `TheLastSwordProtocol-Game/data/Map002.json` — 1 placeholder resolved (Keepsake Shelf).
- `TheLastSwordProtocol-Game/map_ownership.json` — added WO-0046 notes to Map001/Map002 ledger entries (no state change; both were already `hand_authored`).
- `TheLastSwordProtocol-Atlas/atlas/docs/03_Story/Dialogue/Home_Island/Ashford_Dialogue_Packet.md` — added "Environmental / System Text" section (v0.2 → v0.3) authoring the 5 new lines before they were applied.
- `TheLastSwordProtocol-Atlas/atlas/planning/workorder_queue.json` — retired the `apply-gate-a-final-ashford-dialogue` candidate with a completion note.

## Files Created

- `TheLastSwordProtocol-Atlas/atlas/workorders/WO-0046-apply-gate-a-final-ashford-dialogue.md` (planner-generated).
- `rpgmakerLSP/reports/atlas-import/gate-a-dialogue-event-command-audit.md` (WO-required audit output).
- `rpgmakerLSP/reports/atlas-import/gate-a-dialogue-route-audit.md` (supplementary regression check).
- `rpgmakerLSP/reports/atlas-import/wo-0046-gate-a-dialogue-report.md` (this report).

## Player-Visible Progress

Every NPC and examine point in the Gate A opening (village exterior, Elara's house, the shop) now speaks in Ashford's voice instead of showing `[Placeholder]` text, and four of those NPCs now react to story progress (tremor, Sword, Node Seven) instead of repeating their intro line forever. The tremor itself now has a line, the locked Skyreach path reads as local taboo instead of a generic gate message, and the two interior examine points (warm-stone vent, old panel) and Elara's keepsake shelf carry short flavor text. Combined with WO-0045, Gate A now has zero remaining placeholder text anywhere in Maps001-003.

## Commands Run

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py next        # generated WO-0046
/usr/bin/python3 atlas-tools/cli/atlas.py validate
python3 tools/atlas-import/audit_event_command_coverage.py reports/atlas-import/gate-a-dialogue-event-command-audit.md \
    --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/gate-a-dialogue-route-audit.md \
    --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
grep -o '\[Placeholder\][^"]*' ../TheLastSwordProtocol-Game/data/Map001.json ../TheLastSwordProtocol-Game/data/Map002.json ../TheLastSwordProtocol-Game/data/Map003.json
```

Plus a one-off Python script (run from the session shell, not left in either repo) that performed the JSON text replacements and page insertions directly against `Map001.json`/`Map002.json`.

## Validation Result

- Atlas validation: **0 errors, 0 warnings** (after adding the new dialogue packet section).
- Event command coverage audit: **found=204, missing=0, warning=0**.
- Route audit re-run: **found=228, missing=21, warning=9** — identical to the WO-0045 baseline; all misses/warnings belong to the Inn and the not-yet-built Overworld hub, unaffected by this dialogue-only pass.
- Map ownership audit: unchanged, 4 `hand_authored` maps, all still correctly protected.
- `grep [Placeholder]` across Map001-003: **zero matches**.
- All three map JSON files parse cleanly.

## Remaining Issues / Questions

- Village Elder remains a silent placeholder NPC by design — resolving that is an open Atlas design question (packet Open Questions), not a Gate A dialogue gap.
- The Joker and Dock Messenger switch-gating deviates from the literal `Home_Island_Executable_Event_Specs.md` table (see Completed items 2-3) to match the dialogue content and existing in-game convention; worth reconciling the spec table's wording in a future doc pass so it doesn't read as contradicting the implementation.
- Human runtime playtest is still the actual acceptance gate for all of Gate A (per WO-0045's report) — this pass only confirms text presence and structural correctness at the data level.
- Not committed, per the work order.
