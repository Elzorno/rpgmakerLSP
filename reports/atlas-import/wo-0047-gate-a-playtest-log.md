# WO-0047 - Gate A Playtest Log

## Test Session

- Tester: Chris (Production Director)
- Date: 2026-07-13
- Scope: New game start through Elara House intro, Ashford Exterior, and the tremor/Skyreach route-opening beat.
- Minutes played: ~5

## Findings

| ID | Severity | Summary |
|---|---|---|
| PT-20260713-001 | Medium | Town feels barren. Compared explicitly to Dragon Quest-style density: pots/wardrobes with hidden treasure, NPCs with stories about far-away lands the player will see later. Ashford Exterior had only one hidden-item event and one inert placeholder NPC (Village Elder) prior to this pass. |
| PT-20260713-002 | Medium | Tremor Trigger (EVT-HOM-009) reads as forced: it is an Autorun event, so it fires the instant the player's Ashford Exterior map loads, regardless of where the player is standing — before they've had any chance to explore or meet NPCs. After it fires, nothing further happens (self-switch-gated, one-shot), which read as "then nothing more" even though several NPCs (Elara, Child Near Old Panel) do have working after-tremor dialogue pages — the instant autorun meant the player never got a "before" state to notice a difference against. |

## Fixes Applied This Pass

- **PT-20260713-002**: Changed EVT-HOM-009's trigger from Autorun (3) to Player Touch (1), same map position (20,9), which already sits along the natural route north toward Skyreach. The beat now fires when the player actually walks that way, after having had the chance to explore the plaza and meet NPCs first — giving the after-tremor NPC reactions (which already existed and already worked) something to contrast against.
- **PT-20260713-001**: Upgraded "Village Elder Placeholder" (previously a single inert page — talking to it produced no text at all) into a real NPC using the already-approved Ashford Dialogue Packet lines, plus a new authored line giving a distant-lands lore hook ("Beyond Rustshore the water keeps going farther than any of us have sailed...") per the direct request for DQ-style NPC foreshadowing. Added 4 new visible, searchable treasure objects to Ashford Exterior (a pot near Elara's house, a crate near the shop, a barrel by the farmyard, a jug near the well), each granting a small item or gold reward once, using real tile graphics (Outside_B pot/barrel/crate/tub, sampled from the same contact sheet used for the Skyreach/Glassfield decoration pass) rather than the existing invisible-tile convention.

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
- Route audit: `found=228 missing=21 warning=9`, unchanged from the existing project baseline.
- Event command coverage audit: `found=204 missing=0 warning=0`.
- Ownership audit: Map001 remains `hand_authored`, correctly pipeline-protected.
- BFS reachability: 856 reachable cells from the house-exit spawn area; all 4 new treasure events and the repositioned tremor trigger confirmed reachable/functional-position.

## Remaining Issues / Questions

- This pass addressed Ashford Exterior specifically (what was actually played). Elara House, the Shop, and the Inn interiors were not re-inspected for the same "barren" concern and may warrant the same DQ-density pass later (a searchable wardrobe/dresser inside Elara's house was suggested but not yet added).
- Not yet re-confirmed by an actual second human playthrough — the fixes address the two reported findings mechanically and pass all automated checks, but per this project's own standing discipline (`AtlasStudio` Academy rendering-pipeline / render-first workflow), a live-editor or live-game look at the new pot/barrel/crate graphics and the repositioned tremor beat is the honest next step before calling this fully confirmed.
- No new item types were introduced (new treasures grant the existing Potion item or gold) — expanding the item roster was judged out of scope for a playtest-fix pass.
