# BUILD-0027 - All-Map Playtest Route Audit

This read-only audit checks Atlas Home Island transfer expectations against current RPG Maker MZ map data.

- Atlas export: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-exports/home-island.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`

## Summary

- Found: 228
- Missing: 21
- Present with warning: 9
- Total findings: 258

## Category Summary

| Category | Found | Missing | Warning |
|---|---:|---:|---:|
| Reachability | 4 | 13 | 0 |
| Transfer Command | 44 | 8 | 0 |
| Transfer Event | 90 | 0 | 0 |
| Transfer Hygiene | 0 | 0 | 9 |
| Transfer Source | 60 | 0 | 0 |
| Transfer Target | 30 | 0 | 0 |

## Findings

### Reachability

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Reachability | `REACH-START` | Game start map resolves to Home Island screen | startMapId=2 start_screen=SCR-HOM-ASH-002 |
| found | Reachability | `REACH-SCR-HOM-ASH-001` | SCR-HOM-ASH-001 reachable from SCR-HOM-ASH-002 | reachable screens=3 |
| found | Reachability | `REACH-SCR-HOM-ASH-002` | SCR-HOM-ASH-002 reachable from SCR-HOM-ASH-002 | reachable screens=3 |
| found | Reachability | `REACH-SCR-HOM-ASH-003` | SCR-HOM-ASH-003 reachable from SCR-HOM-ASH-002 | reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-FOG-001` | SCR-HOM-FOG-001 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-FOG-002` | SCR-HOM-FOG-002 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-GLS-001` | SCR-HOM-GLS-001 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-HCV-001` | SCR-HOM-HCV-001 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-HCV-002` | SCR-HOM-HCV-002 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-HCV-003` | SCR-HOM-HCV-003 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-RST-001` | SCR-HOM-RST-001 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-RST-002` | SCR-HOM-RST-002 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-SKY-001` | SCR-HOM-SKY-001 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-SND-001` | SCR-HOM-SND-001 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-SND-002` | SCR-HOM-SND-002 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-SND-003` | SCR-HOM-SND-003 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |
| missing | Reachability | `REACH-SCR-HOM-SND-004` | SCR-HOM-SND-004 reachable from SCR-HOM-ASH-002 | Expected reachable screens=3 |

### Transfer Command

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Transfer Command | `TRN-HOM-001-CMD` | TRN-HOM-001 transfers to map 1 | transfer command to map 1 |
| found | Transfer Command | `TRN-HOM-001-DEST` | TRN-HOM-001 destination coordinate is in bounds | (17, 28) in 40x32=True |
| found | Transfer Command | `TRN-HOM-002-CMD` | TRN-HOM-002 transfers to map 2 | transfer command to map 2 |
| found | Transfer Command | `TRN-HOM-002-DEST` | TRN-HOM-002 destination coordinate is in bounds | (8, 11) in 17x13=True |
| found | Transfer Command | `TRN-HOM-003-CMD` | TRN-HOM-003 transfers to map 3 | transfer command to map 3 |
| found | Transfer Command | `TRN-HOM-003-DEST` | TRN-HOM-003 destination coordinate is in bounds | (8, 6) in 17x13=True |
| found | Transfer Command | `TRN-HOM-004-CMD` | TRN-HOM-004 transfers to map 1 | transfer command to map 1 |
| found | Transfer Command | `TRN-HOM-004-DEST` | TRN-HOM-004 destination coordinate is in bounds | (30, 19) in 40x32=True |
| missing | Transfer Command | `TRN-HOM-005-CMD` | TRN-HOM-005 transfers to map 4 | Expected transfer command to map 4 |
| missing | Transfer Command | `TRN-HOM-006-CMD` | TRN-HOM-006 transfers to map 1 | Expected transfer command to map 1 |
| missing | Transfer Command | `TRN-HOM-007-CMD` | TRN-HOM-007 transfers to map 13 | Expected transfer command to map 13 |
| missing | Transfer Command | `TRN-HOM-008-CMD` | TRN-HOM-008 transfers to map 1 | Expected transfer command to map 1 |
| found | Transfer Command | `TRN-HOM-009-CMD` | TRN-HOM-009 transfers to map 5 | transfer command to map 5 |
| found | Transfer Command | `TRN-HOM-009-DEST` | TRN-HOM-009 destination coordinate is in bounds | (8, 6) in 24x24=True |
| found | Transfer Command | `TRN-HOM-010-CMD` | TRN-HOM-010 transfers to map 4 | transfer command to map 4 |
| found | Transfer Command | `TRN-HOM-010-DEST` | TRN-HOM-010 destination coordinate is in bounds | (8, 6) in 30x40=True |
| found | Transfer Command | `TRN-HOM-011-CMD` | TRN-HOM-011 transfers to map 6 | transfer command to map 6 |
| found | Transfer Command | `TRN-HOM-011-DEST` | TRN-HOM-011 destination coordinate is in bounds | (8, 6) in 40x32=True |
| found | Transfer Command | `TRN-HOM-012-CMD` | TRN-HOM-012 transfers to map 5 | transfer command to map 5 |
| found | Transfer Command | `TRN-HOM-012-DEST` | TRN-HOM-012 destination coordinate is in bounds | (8, 6) in 24x24=True |
| found | Transfer Command | `TRN-HOM-013-CMD` | TRN-HOM-013 transfers to map 7 | transfer command to map 7 |
| found | Transfer Command | `TRN-HOM-013-DEST` | TRN-HOM-013 destination coordinate is in bounds | (8, 6) in 23x19=True |
| found | Transfer Command | `TRN-HOM-014-CMD` | TRN-HOM-014 transfers to map 6 | transfer command to map 6 |
| found | Transfer Command | `TRN-HOM-014-DEST` | TRN-HOM-014 destination coordinate is in bounds | (8, 6) in 40x32=True |
| missing | Transfer Command | `TRN-HOM-015-CMD` | TRN-HOM-015 transfers to map 8 | Expected transfer command to map 8 |
| missing | Transfer Command | `TRN-HOM-016-CMD` | TRN-HOM-016 transfers to map 1 | Expected transfer command to map 1 |
| found | Transfer Command | `TRN-HOM-017-CMD` | TRN-HOM-017 transfers to map 9 | transfer command to map 9 |
| found | Transfer Command | `TRN-HOM-017-DEST` | TRN-HOM-017 destination coordinate is in bounds | (8, 6) in 34x30=True |
| found | Transfer Command | `TRN-HOM-018-CMD` | TRN-HOM-018 transfers to map 8 | transfer command to map 8 |
| found | Transfer Command | `TRN-HOM-018-DEST` | TRN-HOM-018 destination coordinate is in bounds | (8, 6) in 42x34=True |
| found | Transfer Command | `TRN-HOM-019-CMD` | TRN-HOM-019 transfers to map 10 | transfer command to map 10 |
| found | Transfer Command | `TRN-HOM-019-DEST` | TRN-HOM-019 destination coordinate is in bounds | (8, 6) in 38x32=True |
| found | Transfer Command | `TRN-HOM-020-CMD` | TRN-HOM-020 transfers to map 9 | transfer command to map 9 |
| found | Transfer Command | `TRN-HOM-020-DEST` | TRN-HOM-020 destination coordinate is in bounds | (8, 6) in 34x30=True |
| found | Transfer Command | `TRN-HOM-021-CMD` | TRN-HOM-021 transfers to map 11 | transfer command to map 11 |
| found | Transfer Command | `TRN-HOM-021-DEST` | TRN-HOM-021 destination coordinate is in bounds | (8, 6) in 27x23=True |
| found | Transfer Command | `TRN-HOM-022-CMD` | TRN-HOM-022 transfers to map 10 | transfer command to map 10 |
| found | Transfer Command | `TRN-HOM-022-DEST` | TRN-HOM-022 destination coordinate is in bounds | (8, 6) in 38x32=True |
| found | Transfer Command | `TRN-HOM-023-CMD` | TRN-HOM-023 transfers to map 12 | transfer command to map 12 |
| found | Transfer Command | `TRN-HOM-023-DEST` | TRN-HOM-023 destination coordinate is in bounds | (8, 6) in 23x19=True |
| found | Transfer Command | `TRN-HOM-024-CMD` | TRN-HOM-024 transfers to map 11 | transfer command to map 11 |
| found | Transfer Command | `TRN-HOM-024-DEST` | TRN-HOM-024 destination coordinate is in bounds | (8, 6) in 27x23=True |
| found | Transfer Command | `TRN-HOM-025-CMD` | TRN-HOM-025 transfers to map 14 | transfer command to map 14 |
| found | Transfer Command | `TRN-HOM-025-DEST` | TRN-HOM-025 destination coordinate is in bounds | (8, 6) in 23x17=True |
| found | Transfer Command | `TRN-HOM-026-CMD` | TRN-HOM-026 transfers to map 50 | transfer command to map 50 |
| found | Transfer Command | `TRN-HOM-026-DEST` | TRN-HOM-026 destination coordinate is in bounds | (8, 6) in 17x13=True |
| missing | Transfer Command | `TRN-HOM-027-CMD` | TRN-HOM-027 transfers to map 15 | Expected transfer command to map 15 |
| missing | Transfer Command | `TRN-HOM-028-CMD` | TRN-HOM-028 transfers to map 1 | Expected transfer command to map 1 |
| found | Transfer Command | `TRN-HOM-029-CMD` | TRN-HOM-029 transfers to map 16 | transfer command to map 16 |
| found | Transfer Command | `TRN-HOM-029-DEST` | TRN-HOM-029 destination coordinate is in bounds | (8, 6) in 24x20=True |
| found | Transfer Command | `TRN-HOM-030-CMD` | TRN-HOM-030 transfers to map 15 | transfer command to map 15 |
| found | Transfer Command | `TRN-HOM-030-DEST` | TRN-HOM-030 destination coordinate is in bounds | (8, 6) in 40x32=True |

### Transfer Event

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Transfer Event | `TRN-HOM-001` | TRN-HOM-001 event exists on SCR-HOM-ASH-002 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-001-POS` | TRN-HOM-001 event is in source map bounds | event position=(8, 12) source size=17x13 |
| found | Transfer Event | `TRN-HOM-001-TILE` | TRN-HOM-001 event sits on concrete tile | layer0 tile=2860 |
| found | Transfer Event | `TRN-HOM-002` | TRN-HOM-002 event exists on SCR-HOM-ASH-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-002-POS` | TRN-HOM-002 event is in source map bounds | event position=(17, 27) source size=40x32 |
| found | Transfer Event | `TRN-HOM-002-TILE` | TRN-HOM-002 event sits on concrete tile | layer0 tile=2844 |
| found | Transfer Event | `TRN-HOM-003` | TRN-HOM-003 event exists on SCR-HOM-ASH-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-003-POS` | TRN-HOM-003 event is in source map bounds | event position=(30, 18) source size=40x32 |
| found | Transfer Event | `TRN-HOM-003-TILE` | TRN-HOM-003 event sits on concrete tile | layer0 tile=2960 |
| found | Transfer Event | `TRN-HOM-004` | TRN-HOM-004 event exists on SCR-HOM-ASH-003 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-004-POS` | TRN-HOM-004 event is in source map bounds | event position=(8, 8) source size=17x13 |
| found | Transfer Event | `TRN-HOM-004-TILE` | TRN-HOM-004 event sits on concrete tile | layer0 tile=2860 |
| found | Transfer Event | `TRN-HOM-005` | TRN-HOM-005 event exists on SCR-HOM-ASH-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-005-POS` | TRN-HOM-005 event is in source map bounds | event position=(20, 0) source size=40x32 |
| found | Transfer Event | `TRN-HOM-005-TILE` | TRN-HOM-005 event sits on concrete tile | layer0 tile=2954 |
| found | Transfer Event | `TRN-HOM-006` | TRN-HOM-006 event exists on SCR-HOM-SKY-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-006-POS` | TRN-HOM-006 event is in source map bounds | event position=(15, 39) source size=30x40 |
| found | Transfer Event | `TRN-HOM-006-TILE` | TRN-HOM-006 event sits on concrete tile | layer0 tile=2849 |
| found | Transfer Event | `TRN-HOM-007` | TRN-HOM-007 event exists on SCR-HOM-ASH-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-007-POS` | TRN-HOM-007 event is in source map bounds | event position=(18, 31) source size=40x32 |
| found | Transfer Event | `TRN-HOM-007-TILE` | TRN-HOM-007 event sits on concrete tile | layer0 tile=2956 |
| found | Transfer Event | `TRN-HOM-008` | TRN-HOM-008 event exists on SCR-HOM-RST-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-008-POS` | TRN-HOM-008 event is in source map bounds | event position=(0, 18) source size=34x26 |
| found | Transfer Event | `TRN-HOM-008-TILE` | TRN-HOM-008 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-009` | TRN-HOM-009 event exists on SCR-HOM-SKY-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-009-POS` | TRN-HOM-009 event is in source map bounds | event position=(15, 1) source size=30x40 |
| found | Transfer Event | `TRN-HOM-009-TILE` | TRN-HOM-009 event sits on concrete tile | layer0 tile=2849 |
| found | Transfer Event | `TRN-HOM-010` | TRN-HOM-010 event exists on SCR-HOM-HCV-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-010-POS` | TRN-HOM-010 event is in source map bounds | event position=(12, 23) source size=24x24 |
| found | Transfer Event | `TRN-HOM-010-TILE` | TRN-HOM-010 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-011` | TRN-HOM-011 event exists on SCR-HOM-HCV-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-011-POS` | TRN-HOM-011 event is in source map bounds | event position=(12, 1) source size=24x24 |
| found | Transfer Event | `TRN-HOM-011-TILE` | TRN-HOM-011 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-012` | TRN-HOM-012 event exists on SCR-HOM-HCV-002 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-012-POS` | TRN-HOM-012 event is in source map bounds | event position=(20, 31) source size=40x32 |
| found | Transfer Event | `TRN-HOM-012-TILE` | TRN-HOM-012 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-013` | TRN-HOM-013 event exists on SCR-HOM-HCV-002 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-013-POS` | TRN-HOM-013 event is in source map bounds | event position=(20, 0) source size=40x32 |
| found | Transfer Event | `TRN-HOM-013-TILE` | TRN-HOM-013 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-014` | TRN-HOM-014 event exists on SCR-HOM-HCV-003 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-014-POS` | TRN-HOM-014 event is in source map bounds | event position=(11, 18) source size=23x19 |
| found | Transfer Event | `TRN-HOM-014-TILE` | TRN-HOM-014 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-015` | TRN-HOM-015 event exists on SCR-HOM-ASH-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-015-POS` | TRN-HOM-015 event is in source map bounds | event position=(39, 9) source size=40x32 |
| found | Transfer Event | `TRN-HOM-015-TILE` | TRN-HOM-015 event sits on concrete tile | layer0 tile=2955 |
| found | Transfer Event | `TRN-HOM-016` | TRN-HOM-016 event exists on SCR-HOM-GLS-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-016-POS` | TRN-HOM-016 event is in source map bounds | event position=(0, 26) source size=42x34 |
| found | Transfer Event | `TRN-HOM-016-TILE` | TRN-HOM-016 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-017` | TRN-HOM-017 event exists on SCR-HOM-GLS-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-017-POS` | TRN-HOM-017 event is in source map bounds | event position=(22, 1) source size=42x34 |
| found | Transfer Event | `TRN-HOM-017-TILE` | TRN-HOM-017 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-018` | TRN-HOM-018 event exists on SCR-HOM-SND-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-018-POS` | TRN-HOM-018 event is in source map bounds | event position=(17, 29) source size=34x30 |
| found | Transfer Event | `TRN-HOM-018-TILE` | TRN-HOM-018 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-019` | TRN-HOM-019 event exists on SCR-HOM-SND-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-019-POS` | TRN-HOM-019 event is in source map bounds | event position=(17, 1) source size=34x30 |
| found | Transfer Event | `TRN-HOM-019-TILE` | TRN-HOM-019 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-020` | TRN-HOM-020 event exists on SCR-HOM-SND-002 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-020-POS` | TRN-HOM-020 event is in source map bounds | event position=(19, 31) source size=38x32 |
| found | Transfer Event | `TRN-HOM-020-TILE` | TRN-HOM-020 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-021` | TRN-HOM-021 event exists on SCR-HOM-SND-002 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-021-POS` | TRN-HOM-021 event is in source map bounds | event position=(19, 1) source size=38x32 |
| found | Transfer Event | `TRN-HOM-021-TILE` | TRN-HOM-021 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-022` | TRN-HOM-022 event exists on SCR-HOM-SND-003 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-022-POS` | TRN-HOM-022 event is in source map bounds | event position=(13, 22) source size=27x23 |
| found | Transfer Event | `TRN-HOM-022-TILE` | TRN-HOM-022 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-023` | TRN-HOM-023 event exists on SCR-HOM-SND-003 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-023-POS` | TRN-HOM-023 event is in source map bounds | event position=(13, 0) source size=27x23 |
| found | Transfer Event | `TRN-HOM-023-TILE` | TRN-HOM-023 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-024` | TRN-HOM-024 event exists on SCR-HOM-SND-004 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-024-POS` | TRN-HOM-024 event is in source map bounds | event position=(11, 18) source size=23x19 |
| found | Transfer Event | `TRN-HOM-024-TILE` | TRN-HOM-024 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-025` | TRN-HOM-025 event exists on SCR-HOM-RST-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-025-POS` | TRN-HOM-025 event is in source map bounds | event position=(30, 14) source size=34x26 |
| found | Transfer Event | `TRN-HOM-025-TILE` | TRN-HOM-025 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-026` | TRN-HOM-026 event exists on SCR-HOM-RST-002 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-026-POS` | TRN-HOM-026 event is in source map bounds | event position=(11, 1) source size=23x17 |
| found | Transfer Event | `TRN-HOM-026-TILE` | TRN-HOM-026 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-027` | TRN-HOM-027 event exists on SCR-HOM-ASH-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-027-POS` | TRN-HOM-027 event is in source map bounds | event position=(39, 23) source size=40x32 |
| found | Transfer Event | `TRN-HOM-027-TILE` | TRN-HOM-027 event sits on concrete tile | layer0 tile=2955 |
| found | Transfer Event | `TRN-HOM-028` | TRN-HOM-028 event exists on SCR-HOM-FOG-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-028-POS` | TRN-HOM-028 event is in source map bounds | event position=(0, 26) source size=40x32 |
| found | Transfer Event | `TRN-HOM-028-TILE` | TRN-HOM-028 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-029` | TRN-HOM-029 event exists on SCR-HOM-FOG-001 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-029-POS` | TRN-HOM-029 event is in source map bounds | event position=(39, 8) source size=40x32 |
| found | Transfer Event | `TRN-HOM-029-TILE` | TRN-HOM-029 event sits on concrete tile | layer0 tile=2836 |
| found | Transfer Event | `TRN-HOM-030` | TRN-HOM-030 event exists on SCR-HOM-FOG-002 | event containing transfer ID |
| found | Transfer Event | `TRN-HOM-030-POS` | TRN-HOM-030 event is in source map bounds | event position=(0, 15) source size=24x20 |
| found | Transfer Event | `TRN-HOM-030-TILE` | TRN-HOM-030 event sits on concrete tile | layer0 tile=2836 |

### Transfer Hygiene

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| present with warning | Transfer Hygiene | `ORPHAN-1-23` | No orphan transfer events | TRN-HOM-031 Enter Ashford Inn on map 1 not present in Atlas export |
| present with warning | Transfer Hygiene | `ORPHAN-26-2` | No orphan transfer events | TRN-HOM-032 Inn exit on map 26 not present in Atlas export |
| present with warning | Transfer Hygiene | `ORPHAN-27-1` | No orphan transfer events | TRN-HOM-033 Overworld to Ashford on map 27 not present in Atlas export |
| present with warning | Transfer Hygiene | `ORPHAN-27-2` | No orphan transfer events | TRN-HOM-034 Overworld to Rustshore Docks on map 27 not present in Atlas export |
| present with warning | Transfer Hygiene | `ORPHAN-27-3` | No orphan transfer events | TRN-HOM-035 Overworld to Fogfen Marsh on map 27 not present in Atlas export |
| present with warning | Transfer Hygiene | `ORPHAN-27-4` | No orphan transfer events | TRN-HOM-036 Overworld to Glassfield Ruins on map 27 not present in Atlas export |
| present with warning | Transfer Hygiene | `ORPHAN-27-5` | No orphan transfer events | TRN-HOM-037 Overworld to Skyreach Hill on map 27 not present in Atlas export |
| present with warning | Transfer Hygiene | `ORPHAN-27-6` | No orphan transfer events | TRN-HOM-038 Hidden Cave Reveal Stub on map 27 not present in Atlas export |
| present with warning | Transfer Hygiene | `ORPHAN-27-7` | No orphan transfer events | TRN-HOM-039 Sealed Node Gate Stub on map 27 not present in Atlas export |

### Transfer Source

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Transfer Source | `TRN-HOM-001-SRC` | SCR-HOM-ASH-002 has RPG Maker map | source map for SCR-HOM-ASH-002 |
| found | Transfer Source | `TRN-HOM-001-MAP` | Map 2 JSON exists | Map002.json exists |
| found | Transfer Source | `TRN-HOM-002-SRC` | SCR-HOM-ASH-001 has RPG Maker map | source map for SCR-HOM-ASH-001 |
| found | Transfer Source | `TRN-HOM-002-MAP` | Map 1 JSON exists | Map001.json exists |
| found | Transfer Source | `TRN-HOM-003-SRC` | SCR-HOM-ASH-001 has RPG Maker map | source map for SCR-HOM-ASH-001 |
| found | Transfer Source | `TRN-HOM-003-MAP` | Map 1 JSON exists | Map001.json exists |
| found | Transfer Source | `TRN-HOM-004-SRC` | SCR-HOM-ASH-003 has RPG Maker map | source map for SCR-HOM-ASH-003 |
| found | Transfer Source | `TRN-HOM-004-MAP` | Map 3 JSON exists | Map003.json exists |
| found | Transfer Source | `TRN-HOM-005-SRC` | SCR-HOM-ASH-001 has RPG Maker map | source map for SCR-HOM-ASH-001 |
| found | Transfer Source | `TRN-HOM-005-MAP` | Map 1 JSON exists | Map001.json exists |
| found | Transfer Source | `TRN-HOM-006-SRC` | SCR-HOM-SKY-001 has RPG Maker map | source map for SCR-HOM-SKY-001 |
| found | Transfer Source | `TRN-HOM-006-MAP` | Map 4 JSON exists | Map004.json exists |
| found | Transfer Source | `TRN-HOM-007-SRC` | SCR-HOM-ASH-001 has RPG Maker map | source map for SCR-HOM-ASH-001 |
| found | Transfer Source | `TRN-HOM-007-MAP` | Map 1 JSON exists | Map001.json exists |
| found | Transfer Source | `TRN-HOM-008-SRC` | SCR-HOM-RST-001 has RPG Maker map | source map for SCR-HOM-RST-001 |
| found | Transfer Source | `TRN-HOM-008-MAP` | Map 13 JSON exists | Map013.json exists |
| found | Transfer Source | `TRN-HOM-009-SRC` | SCR-HOM-SKY-001 has RPG Maker map | source map for SCR-HOM-SKY-001 |
| found | Transfer Source | `TRN-HOM-009-MAP` | Map 4 JSON exists | Map004.json exists |
| found | Transfer Source | `TRN-HOM-010-SRC` | SCR-HOM-HCV-001 has RPG Maker map | source map for SCR-HOM-HCV-001 |
| found | Transfer Source | `TRN-HOM-010-MAP` | Map 5 JSON exists | Map005.json exists |
| found | Transfer Source | `TRN-HOM-011-SRC` | SCR-HOM-HCV-001 has RPG Maker map | source map for SCR-HOM-HCV-001 |
| found | Transfer Source | `TRN-HOM-011-MAP` | Map 5 JSON exists | Map005.json exists |
| found | Transfer Source | `TRN-HOM-012-SRC` | SCR-HOM-HCV-002 has RPG Maker map | source map for SCR-HOM-HCV-002 |
| found | Transfer Source | `TRN-HOM-012-MAP` | Map 6 JSON exists | Map006.json exists |
| found | Transfer Source | `TRN-HOM-013-SRC` | SCR-HOM-HCV-002 has RPG Maker map | source map for SCR-HOM-HCV-002 |
| found | Transfer Source | `TRN-HOM-013-MAP` | Map 6 JSON exists | Map006.json exists |
| found | Transfer Source | `TRN-HOM-014-SRC` | SCR-HOM-HCV-003 has RPG Maker map | source map for SCR-HOM-HCV-003 |
| found | Transfer Source | `TRN-HOM-014-MAP` | Map 7 JSON exists | Map007.json exists |
| found | Transfer Source | `TRN-HOM-015-SRC` | SCR-HOM-ASH-001 has RPG Maker map | source map for SCR-HOM-ASH-001 |
| found | Transfer Source | `TRN-HOM-015-MAP` | Map 1 JSON exists | Map001.json exists |
| found | Transfer Source | `TRN-HOM-016-SRC` | SCR-HOM-GLS-001 has RPG Maker map | source map for SCR-HOM-GLS-001 |
| found | Transfer Source | `TRN-HOM-016-MAP` | Map 8 JSON exists | Map008.json exists |
| found | Transfer Source | `TRN-HOM-017-SRC` | SCR-HOM-GLS-001 has RPG Maker map | source map for SCR-HOM-GLS-001 |
| found | Transfer Source | `TRN-HOM-017-MAP` | Map 8 JSON exists | Map008.json exists |
| found | Transfer Source | `TRN-HOM-018-SRC` | SCR-HOM-SND-001 has RPG Maker map | source map for SCR-HOM-SND-001 |
| found | Transfer Source | `TRN-HOM-018-MAP` | Map 9 JSON exists | Map009.json exists |
| found | Transfer Source | `TRN-HOM-019-SRC` | SCR-HOM-SND-001 has RPG Maker map | source map for SCR-HOM-SND-001 |
| found | Transfer Source | `TRN-HOM-019-MAP` | Map 9 JSON exists | Map009.json exists |
| found | Transfer Source | `TRN-HOM-020-SRC` | SCR-HOM-SND-002 has RPG Maker map | source map for SCR-HOM-SND-002 |
| found | Transfer Source | `TRN-HOM-020-MAP` | Map 10 JSON exists | Map010.json exists |
| found | Transfer Source | `TRN-HOM-021-SRC` | SCR-HOM-SND-002 has RPG Maker map | source map for SCR-HOM-SND-002 |
| found | Transfer Source | `TRN-HOM-021-MAP` | Map 10 JSON exists | Map010.json exists |
| found | Transfer Source | `TRN-HOM-022-SRC` | SCR-HOM-SND-003 has RPG Maker map | source map for SCR-HOM-SND-003 |
| found | Transfer Source | `TRN-HOM-022-MAP` | Map 11 JSON exists | Map011.json exists |
| found | Transfer Source | `TRN-HOM-023-SRC` | SCR-HOM-SND-003 has RPG Maker map | source map for SCR-HOM-SND-003 |
| found | Transfer Source | `TRN-HOM-023-MAP` | Map 11 JSON exists | Map011.json exists |
| found | Transfer Source | `TRN-HOM-024-SRC` | SCR-HOM-SND-004 has RPG Maker map | source map for SCR-HOM-SND-004 |
| found | Transfer Source | `TRN-HOM-024-MAP` | Map 12 JSON exists | Map012.json exists |
| found | Transfer Source | `TRN-HOM-025-SRC` | SCR-HOM-RST-001 has RPG Maker map | source map for SCR-HOM-RST-001 |
| found | Transfer Source | `TRN-HOM-025-MAP` | Map 13 JSON exists | Map013.json exists |
| found | Transfer Source | `TRN-HOM-026-SRC` | SCR-HOM-RST-002 has RPG Maker map | source map for SCR-HOM-RST-002 |
| found | Transfer Source | `TRN-HOM-026-MAP` | Map 14 JSON exists | Map014.json exists |
| found | Transfer Source | `TRN-HOM-027-SRC` | SCR-HOM-ASH-001 has RPG Maker map | source map for SCR-HOM-ASH-001 |
| found | Transfer Source | `TRN-HOM-027-MAP` | Map 1 JSON exists | Map001.json exists |
| found | Transfer Source | `TRN-HOM-028-SRC` | SCR-HOM-FOG-001 has RPG Maker map | source map for SCR-HOM-FOG-001 |
| found | Transfer Source | `TRN-HOM-028-MAP` | Map 15 JSON exists | Map015.json exists |
| found | Transfer Source | `TRN-HOM-029-SRC` | SCR-HOM-FOG-001 has RPG Maker map | source map for SCR-HOM-FOG-001 |
| found | Transfer Source | `TRN-HOM-029-MAP` | Map 15 JSON exists | Map015.json exists |
| found | Transfer Source | `TRN-HOM-030-SRC` | SCR-HOM-FOG-002 has RPG Maker map | source map for SCR-HOM-FOG-002 |
| found | Transfer Source | `TRN-HOM-030-MAP` | Map 16 JSON exists | Map016.json exists |

### Transfer Target

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Transfer Target | `TRN-HOM-001-TARGET` | SCR-HOM-ASH-001 resolves to RPG Maker map | target=SCR-HOM-ASH-001 |
| found | Transfer Target | `TRN-HOM-002-TARGET` | SCR-HOM-ASH-002 resolves to RPG Maker map | target=SCR-HOM-ASH-002 |
| found | Transfer Target | `TRN-HOM-003-TARGET` | SCR-HOM-ASH-003 resolves to RPG Maker map | target=SCR-HOM-ASH-003 |
| found | Transfer Target | `TRN-HOM-004-TARGET` | SCR-HOM-ASH-001 resolves to RPG Maker map | target=SCR-HOM-ASH-001 |
| found | Transfer Target | `TRN-HOM-005-TARGET` | SCR-HOM-SKY-001 resolves to RPG Maker map | target=SCR-HOM-SKY-001 |
| found | Transfer Target | `TRN-HOM-006-TARGET` | SCR-HOM-ASH-001 resolves to RPG Maker map | target=SCR-HOM-ASH-001 |
| found | Transfer Target | `TRN-HOM-007-TARGET` | SCR-HOM-RST-001 resolves to RPG Maker map | target=SCR-HOM-RST-001 |
| found | Transfer Target | `TRN-HOM-008-TARGET` | SCR-HOM-ASH-001 resolves to RPG Maker map | target=SCR-HOM-ASH-001 |
| found | Transfer Target | `TRN-HOM-009-TARGET` | SCR-HOM-HCV-001 resolves to RPG Maker map | target=SCR-HOM-HCV-001 |
| found | Transfer Target | `TRN-HOM-010-TARGET` | SCR-HOM-SKY-001 resolves to RPG Maker map | target=SCR-HOM-SKY-001 |
| found | Transfer Target | `TRN-HOM-011-TARGET` | SCR-HOM-HCV-002 resolves to RPG Maker map | target=SCR-HOM-HCV-002 |
| found | Transfer Target | `TRN-HOM-012-TARGET` | SCR-HOM-HCV-001 resolves to RPG Maker map | target=SCR-HOM-HCV-001 |
| found | Transfer Target | `TRN-HOM-013-TARGET` | SCR-HOM-HCV-003 resolves to RPG Maker map | target=SCR-HOM-HCV-003 |
| found | Transfer Target | `TRN-HOM-014-TARGET` | SCR-HOM-HCV-002 resolves to RPG Maker map | target=SCR-HOM-HCV-002 |
| found | Transfer Target | `TRN-HOM-015-TARGET` | SCR-HOM-GLS-001 resolves to RPG Maker map | target=SCR-HOM-GLS-001 |
| found | Transfer Target | `TRN-HOM-016-TARGET` | SCR-HOM-ASH-001 resolves to RPG Maker map | target=SCR-HOM-ASH-001 |
| found | Transfer Target | `TRN-HOM-017-TARGET` | SCR-HOM-SND-001 resolves to RPG Maker map | target=SCR-HOM-SND-001 |
| found | Transfer Target | `TRN-HOM-018-TARGET` | SCR-HOM-GLS-001 resolves to RPG Maker map | target=SCR-HOM-GLS-001 |
| found | Transfer Target | `TRN-HOM-019-TARGET` | SCR-HOM-SND-002 resolves to RPG Maker map | target=SCR-HOM-SND-002 |
| found | Transfer Target | `TRN-HOM-020-TARGET` | SCR-HOM-SND-001 resolves to RPG Maker map | target=SCR-HOM-SND-001 |
| found | Transfer Target | `TRN-HOM-021-TARGET` | SCR-HOM-SND-003 resolves to RPG Maker map | target=SCR-HOM-SND-003 |
| found | Transfer Target | `TRN-HOM-022-TARGET` | SCR-HOM-SND-002 resolves to RPG Maker map | target=SCR-HOM-SND-002 |
| found | Transfer Target | `TRN-HOM-023-TARGET` | SCR-HOM-SND-004 resolves to RPG Maker map | target=SCR-HOM-SND-004 |
| found | Transfer Target | `TRN-HOM-024-TARGET` | SCR-HOM-SND-003 resolves to RPG Maker map | target=SCR-HOM-SND-003 |
| found | Transfer Target | `TRN-HOM-025-TARGET` | SCR-HOM-RST-002 resolves to RPG Maker map | target=SCR-HOM-RST-002 |
| found | Transfer Target | `TRN-HOM-026-TARGET` | Journey II start resolves to RPG Maker map | target=Journey II start |
| found | Transfer Target | `TRN-HOM-027-TARGET` | SCR-HOM-FOG-001 resolves to RPG Maker map | target=SCR-HOM-FOG-001 |
| found | Transfer Target | `TRN-HOM-028-TARGET` | SCR-HOM-ASH-001 resolves to RPG Maker map | target=SCR-HOM-ASH-001 |
| found | Transfer Target | `TRN-HOM-029-TARGET` | SCR-HOM-FOG-002 resolves to RPG Maker map | target=SCR-HOM-FOG-002 |
| found | Transfer Target | `TRN-HOM-030-TARGET` | SCR-HOM-FOG-001 resolves to RPG Maker map | target=SCR-HOM-FOG-001 |

## Notes

- This audit follows transfer commands found in RPG Maker JSON; it does not simulate player collision, switch timing, or runtime plugin behavior.
- A reachable screen means at least one directed transfer-command path exists from the configured start map, ignoring story gates.
- This audit does not modify RPG Maker data files.
