# WO-0047 Implementation Report — Gate A Ashford Lives Playtest Fix Pass

Date: 2026-07-13

## Completed

- Ran the required Gate A playtest (human-executed by Chris, ~5 minutes: new game → Elara House → Ashford Exterior → the tremor/Skyreach beat). Findings recorded in `rpgmakerLSP/reports/atlas-import/wo-0047-gate-a-playtest-log.md`.
- Fixed the Tremor Trigger's pacing: it was an Autorun event (`trigger: 3`), firing the instant the Ashford Exterior map loads regardless of player position — reported as "forced." Changed to Player Touch (`trigger: 1`) at the same map position, which already sits along the natural route north toward Skyreach, so the beat now happens when the player actually walks that way rather than the moment they step outside.
- Upgraded "Village Elder Placeholder" (previously a single page with no dialogue at all — an NPC that did nothing when talked to) into a real two-page NPC using the already-approved `Ashford_Dialogue_Packet.md` lines, plus a newly authored distant-lands lore line ("Beyond Rustshore the water keeps going farther than any of us have sailed...") addressing the specific "NPCs with stories about far-away lands you will see later" feedback.
- Added four visible, searchable DQ-style treasure objects to Ashford Exterior (pot near Elara's house, crate near the shop, barrel by the farmyard, jug near the well) using real tile graphics (`Outside_B.png` pot/barrel/crate/tub, the same file already sampled for this session's Skyreach/Glassfield decoration pass), each granting a small one-time reward (Potion or gold).

## Files Modified

- `TheLastSwordProtocol-Game/data/Map001.json` — Tremor Trigger pacing fix, Village Elder dialogue, 4 new treasure events.

## Files Created

- `rpgmakerLSP/reports/atlas-import/wo-0047-gate-a-playtest-log.md`
- `rpgmakerLSP/reports/atlas-import/wo-0047-gate-a-route-audit.md`
- `rpgmakerLSP/reports/atlas-import/gate-a-event-command-audit.md`
- This report.

## Minutes Playable

~5 minutes confirmed playable this pass (new game through the tremor beat), same scope as the original Gate A target. The two findings reported were pacing/content-density issues, not runtime blockers (no crash, softlock, or broken transfer) — both are now fixed within Gate A's existing scope.

## Commands Run

```bash
cd TheLastSwordProtocol-Atlas && /usr/bin/python3 atlas-tools/cli/atlas.py validate
cd rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/wo-0047-gate-a-route-audit.md \
  --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
cd rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_event_command_coverage.py reports/atlas-import/gate-a-event-command-audit.md
cd rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
```

## Validation Result

- `atlas.py validate`: 0 errors, 0 warnings.
- Route audit: `found=228 missing=21 warning=9`, identical to the existing project baseline — no regressions.
- Event command coverage audit: `found=204 missing=0 warning=0`.
- Ownership audit: Map001 remains `hand_authored`, correctly pipeline-protected.
- BFS reachability (scratchpad check): all 4 new treasure events reachable; tremor trigger's new position confirmed on the player's natural route.

## Remaining Issues / Questions

- Fixes were verified via JSON inspection, an engine-faithful tile renderer, and BFS reachability — not yet by a second live human playthrough. Given this project's standing render-first discipline, a live look (in the editor or in-game) at the new pot/barrel/crate graphics and the repositioned tremor beat is the honest next step before calling this fully confirmed, same caution already applied to this session's other terrain work.
- Only Ashford Exterior was addressed. Elara House, the Shop, and the Inn interiors weren't re-inspected for the same density concern — a searchable wardrobe/dresser inside Elara's house was considered but not added, and would be a reasonable next small pass.
- No new items were introduced; new treasures reuse the existing Potion item and gold, keeping this pass scoped to fixing what was reported rather than expanding the item roster.
- Not committed, per this session's standing practice.
