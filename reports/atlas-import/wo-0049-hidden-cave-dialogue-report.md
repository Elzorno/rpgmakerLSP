# WO-0049 Implementation Report — Apply Approved Skyreach Hidden Cave Dialogue To Events

Work order: `WO-0049-apply-approved-skyreach-hidden-cave-dialogue-to-events.md`
Packet: `ATLAS-STY-012` (Skyreach and Hidden Cave Dialogue Packet, Approved) | Maps: `Map004` (already done in WO-0048), `Map005` (Hidden Cave Entrance), `Map006` (Hidden Cave Trials), `Map007` (Sword Sanctum)
Date: 2026-07-10

## Completed

1. **Map004 (Skyreach)** — already fully text-complete from WO-0048; confirmed zero remaining placeholders, no changes needed.

2. **Map005 (Hidden Cave Entrance)**:
   - `Hidden Cave First Entry` (event 1) — applied `PH-DLG-HCV-FIRST-ENTRY`.
   - `Wall Carving` (event 4) — applied `PH-DLG-HCV-CARVING`; added the missing second (self-switch-gated repeat) page, matching the one-time/repeat examine pattern already established for Ashford's shop cabinet and Skyreach's geometric stones.

3. **Map006 (Hidden Cave Trials)**:
   - Body/Mind Trial finish text — applied the `PH-DLG-TRIAL-COMPLETE` Body/Mind variants.
   - Heart Trial — applied the Heart-variant finish text to both accepted choices (Protect home / Seek truth, per the packet: "both intents are accepted; the trial honors honesty, not one answer") and `PH-DLG-TRIAL-HEART-RESET` to Turn back. **Also added the `PH-DLG-TRIAL-HEART-PROMPT` text that was missing entirely** — the event had a Show Choices menu with no prompt text before it. First attempt at this introduced a real bug (see below); rebuilt the event's command list explicitly to fix it.
   - `Sanctum Gate` (event 4) locked text — applied `PH-DLG-HCV-GATE-LOCKED`.
   - `TRN-HOM-013 Enter Sword Sanctum` (event 6) — unified its three separate locked-branch messages ("Heart/Mind/Body Trial Required") to the same `PH-DLG-HCV-GATE-LOCKED` line, per the packet's explicit instruction to "keep count-agnostic so it reads correctly whichever trials remain."
   - **Found and fixed a real progression-breaking bug**: `Sanctum Gate` (`EVT-HOM-015`) was a single unconditional page with `through: false` — it would have permanently blocked the only path to the Sanctum even after all three trials were cleared, since nothing ever changed its state. Registered a new switch, `J1_HiddenCave_AllTrialsClear` (switch 17, added to `System.json`), set by each of the Body/Mind/Heart trial completion events via a nested three-switch check once all of them read ON (order-independent — whichever trial finishes last is the one that actually sets it). Gave the Sanctum Gate a second page, gated on that switch, with `through: true`. This is the same failure mode as the Skyreach Gate bug fixed in WO-0048, caught the same way.

4. **Map007 (Sword Sanctum)**: the `Sword Pedestal` event's single placeholder line was replaced with the full `PH-DLG-SWD-AWAKENING` beat sequence from the packet — Beat 1 (approach/touch, 1 box), Beat 2 (three vision-caption boxes, no speaker), Beat 3 (the two exact archive strings, `AUTHORIZATION ACCEPTED` / `ARCHIVE RECOVERY: 3%`, wrapped around the existing Sword/item/switch/variable-grant commands in the position the executable event spec calls for), Beat 4 (waking, 1 box). Added Fadeout before Beat 2 and Fadein before Beat 4 per the packet's staging notes ("Beat 2's vision lines display over darkness/flash"); the existing SE/animation cue stayed near Beat 1/2 as the "authentication cue... lands between Beats 1 and 2."

## Files Modified

- `TheLastSwordProtocol-Game/data/Map005.json`, `Map006.json`, `Map007.json` — dialogue applied; Map006 also gets the Sanctum Gate fix.
- `TheLastSwordProtocol-Game/data/System.json` — registered switch 17, `J1_HiddenCave_AllTrialsClear`.
- `TheLastSwordProtocol-Game/map_ownership.json` — notes on maps 5/6/7 (still `generated`, terrain untouched).
- `TheLastSwordProtocol-Atlas/atlas/planning/workorder_queue.json` — retired the candidate with a completion note.

## Files Created

- `TheLastSwordProtocol-Atlas/atlas/workorders/WO-0049-apply-approved-skyreach-hidden-cave-dialogue-to-events.md` (planner-generated).
- `rpgmakerLSP/reports/atlas-import/skyreach-hidden-cave-dialogue-event-command-audit.md`.
- `rpgmakerLSP/reports/atlas-import/wo-0049-hcv-route-audit.md`.
- `rpgmakerLSP/reports/atlas-import/wo-0049-hidden-cave-dialogue-report.md` (this report).

## Player-Visible Progress

Every dialogue slot across the Hidden Cave route now speaks in the approved voice instead of `[Placeholder]` text: the first-entry threshold moment, the wall carving's foreshadowing, all three trials' prompts and finish lines, the sanctum gate, and — the biggest single beat in Journey I so far — the full Sword awakening sequence (hand on hilt, three fragmented vision captions, the archive authorization text, waking with the Sword). Functionally, the trials → sanctum progression now actually works: previously, clearing all three trials would not have opened the sanctum door at all.

## Commands Run

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py next        # generated WO-0049
/usr/bin/python3 atlas-tools/cli/atlas.py validate
python3 tools/atlas-import/audit_event_command_coverage.py reports/atlas-import/skyreach-hidden-cave-dialogue-event-command-audit.md \
    --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/wo-0049-hcv-route-audit.md \
    --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
grep -o '\[Placeholder\][^"]*' ../TheLastSwordProtocol-Game/data/Map004.json ../TheLastSwordProtocol-Game/data/Map005.json \
    ../TheLastSwordProtocol-Game/data/Map006.json ../TheLastSwordProtocol-Game/data/Map007.json
```

## Validation Result

- Atlas validation: **0 errors, 0 warnings**.
- Event command coverage audit: **found=204, missing=0, warning=0**.
- Route audit: **found=228, missing=21, warning=9** — identical totals to every prior baseline this session; no regression.
- `grep [Placeholder]`: zero matches across Map004-007.
- All touched JSON files parse cleanly.
- Manually traced the Heart Trial and Sanctum Gate logic by hand (no engine runtime available): the all-clear switch check is order-independent (each trial's own completion event checks all three switches, so whichever trial finishes last is the one that sets switch 17, regardless of completion order), and RPG Maker's highest-satisfied-page rule means the Sanctum Gate correctly falls back to the locked page whenever switch 17 is off and to the open page when it's on.

## Remaining Issues / Questions

- **A self-caught mistake worth recording**: my first attempt at the Heart Trial edit had a real bug — I inserted the missing prompt text via one pass and then ran a second pass that replaced "the next placeholder text run" without accounting for the prompt I'd just added, which shifted every subsequent replacement by one slot (the prompt got overwritten with finish text, "Seek truth" got the reset text, "Turn back" never got replaced at all). Caught it by reading the actual resulting command list before moving on, and rebuilt the event's command list explicitly instead of patching further. No corrupted state was left in the file.
- Body/Mind Trial reset-tile mechanics (`EVT-HOM-012A/B/C` movement-lane reset tiles, `EVT-HOM-013A/B/C` Left/Right/Center mind markers) are still empty stub events with zero wired commands — per `ATLAS-TEC-057` these need real mechanics (movement lanes, sequence tracking), which is map-building work, not dialogue. Flagging as the next concrete gap before Hidden Cave is actually playable, not just readable.
- Maps 5-7 are still on bare generated terrain (no hand-built rooms yet) — this WO was dialogue-only per its constraints ("do not change map geometry").
- Human runtime playtest is still the real gate, same as everything else this session — this is a data-level and manually-traced-logic audit, not a substitute for walking the trials in the engine.
- Not committed.
