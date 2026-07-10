# BUILD-0030 - Event Command Coverage Audit

This read-only audit checks whether Atlas events, Atlas transfers, and generated local anchors have executable RPG Maker event commands.

- Atlas export: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Atlas/atlas-exports/home-island.json`
- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`

## Summary

- Found: 204
- Missing: 0
- Present with warning: 0
- Total findings: 204

## Category Summary

| Category | Found | Missing | Warning |
|---|---:|---:|---:|
| Atlas Event Commands | 93 | 0 | 0 |
| Local Anchor Commands | 21 | 0 | 0 |
| Transfer Commands | 90 | 0 | 0 |

## Findings

### Atlas Event Commands

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Atlas Event Commands | `EVT-HOM-001` | EVT-HOM-001 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-001-EXEC` | EVT-HOM-001 has executable commands | codes=121x1, 122x2 |
| found | Atlas Event Commands | `EVT-HOM-001-REQ` | EVT-HOM-001 includes required command family | codes=121x1, 122x2 |
| found | Atlas Event Commands | `EVT-HOM-002` | EVT-HOM-002 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-002-EXEC` | EVT-HOM-002 has executable commands | codes=101x6, 401x15 |
| found | Atlas Event Commands | `EVT-HOM-002-REQ` | EVT-HOM-002 includes required command family | codes=101x6, 401x15 |
| found | Atlas Event Commands | `EVT-HOM-003` | EVT-HOM-003 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-003-EXEC` | EVT-HOM-003 has executable commands | codes=101x2, 401x5 |
| found | Atlas Event Commands | `EVT-HOM-003-REQ` | EVT-HOM-003 includes required command family | codes=101x2, 401x5 |
| found | Atlas Event Commands | `EVT-HOM-004` | EVT-HOM-004 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-004-EXEC` | EVT-HOM-004 has executable commands | codes=101x2, 401x7 |
| found | Atlas Event Commands | `EVT-HOM-004-REQ` | EVT-HOM-004 includes required command family | codes=101x2, 401x7 |
| found | Atlas Event Commands | `EVT-HOM-005` | EVT-HOM-005 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-005-EXEC` | EVT-HOM-005 has executable commands | codes=101x3, 401x8 |
| found | Atlas Event Commands | `EVT-HOM-005-REQ` | EVT-HOM-005 includes required command family | codes=101x3, 401x8 |
| found | Atlas Event Commands | `EVT-HOM-006` | EVT-HOM-006 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-006-EXEC` | EVT-HOM-006 has executable commands | codes=101x2, 401x5 |
| found | Atlas Event Commands | `EVT-HOM-006-REQ` | EVT-HOM-006 includes required command family | codes=101x2, 401x5 |
| found | Atlas Event Commands | `EVT-HOM-007` | EVT-HOM-007 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-007-EXEC` | EVT-HOM-007 has executable commands | codes=101x1, 123x1, 126x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-007-REQ` | EVT-HOM-007 includes required command family | codes=101x1, 123x1, 126x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-008` | EVT-HOM-008 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-008-EXEC` | EVT-HOM-008 has executable commands | codes=101x2, 302x2, 401x6 |
| found | Atlas Event Commands | `EVT-HOM-008-REQ` | EVT-HOM-008 includes required command family | codes=101x2, 302x2, 401x6 |
| found | Atlas Event Commands | `EVT-HOM-009` | EVT-HOM-009 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-009-EXEC` | EVT-HOM-009 has executable commands | codes=101x1, 121x2, 123x1, 250x1, 401x2 |
| found | Atlas Event Commands | `EVT-HOM-009-REQ` | EVT-HOM-009 includes required command family | codes=101x1, 121x2, 123x1, 250x1, 401x2 |
| found | Atlas Event Commands | `EVT-HOM-010` | EVT-HOM-010 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-010-EXEC` | EVT-HOM-010 has executable commands | codes=101x1, 401x3 |
| found | Atlas Event Commands | `EVT-HOM-010-REQ` | EVT-HOM-010 includes required command family | codes=101x1, 401x3 |
| found | Atlas Event Commands | `EVT-HOM-011` | EVT-HOM-011 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-011-EXEC` | EVT-HOM-011 has executable commands | codes=101x1, 121x1, 123x1, 212x1, 401x3 |
| found | Atlas Event Commands | `EVT-HOM-011-REQ` | EVT-HOM-011 includes required command family | codes=101x1, 121x1, 123x1, 212x1, 401x3 |
| found | Atlas Event Commands | `EVT-HOM-012` | EVT-HOM-012 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-012-EXEC` | EVT-HOM-012 has executable commands | codes=101x1, 111x3, 117x1, 121x4, 122x1, 123x1, 212x1, 250x1, 401x2, 412x3 |
| found | Atlas Event Commands | `EVT-HOM-012-REQ` | EVT-HOM-012 includes required command family | codes=101x1, 111x3, 117x1, 121x4, 122x1, 123x1, 212x1, 250x1, 401x2, 412x3 |
| found | Atlas Event Commands | `EVT-HOM-013` | EVT-HOM-013 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-013-EXEC` | EVT-HOM-013 has executable commands | codes=101x1, 111x3, 117x1, 121x4, 122x1, 123x1, 212x1, 250x1, 401x2, 412x3 |
| found | Atlas Event Commands | `EVT-HOM-013-REQ` | EVT-HOM-013 includes required command family | codes=101x1, 111x3, 117x1, 121x4, 122x1, 123x1, 212x1, 250x1, 401x2, 412x3 |
| found | Atlas Event Commands | `EVT-HOM-014` | EVT-HOM-014 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-014-EXEC` | EVT-HOM-014 has executable commands | codes=101x4, 102x1, 111x6, 117x3, 121x8, 122x3, 123x2, 212x1, 250x1, 401x8, 402x3, 404x1, 412x6 |
| found | Atlas Event Commands | `EVT-HOM-014-REQ` | EVT-HOM-014 includes required command family | codes=101x4, 102x1, 111x6, 117x3, 121x8, 122x3, 123x2, 212x1, 250x1, 401x8, 402x3, 404x1, 412x6 |
| found | Atlas Event Commands | `EVT-HOM-015` | EVT-HOM-015 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-015-EXEC` | EVT-HOM-015 has executable commands | codes=101x1, 212x1, 401x2 |
| found | Atlas Event Commands | `EVT-HOM-015-REQ` | EVT-HOM-015 includes required command family | codes=101x1, 212x1, 401x2 |
| found | Atlas Event Commands | `EVT-HOM-016` | EVT-HOM-016 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-016-EXEC` | EVT-HOM-016 has executable commands | codes=101x7, 121x1, 122x1, 123x1, 126x1, 127x1, 212x1, 221x1, 222x1, 250x1, 401x11 |
| found | Atlas Event Commands | `EVT-HOM-016-REQ` | EVT-HOM-016 includes required command family | codes=101x7, 121x1, 122x1, 123x1, 126x1, 127x1, 212x1, 221x1, 222x1, 250x1, 401x11 |
| found | Atlas Event Commands | `EVT-HOM-017` | EVT-HOM-017 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-017-EXEC` | EVT-HOM-017 has executable commands | codes=101x1, 121x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-017-REQ` | EVT-HOM-017 includes required command family | codes=101x1, 121x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-018` | EVT-HOM-018 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-018-EXEC` | EVT-HOM-018 has executable commands | codes=101x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-018-REQ` | EVT-HOM-018 includes required command family | codes=101x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-019` | EVT-HOM-019 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-019-EXEC` | EVT-HOM-019 has executable commands | codes=101x1, 121x1, 123x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-019-REQ` | EVT-HOM-019 includes required command family | codes=101x1, 121x1, 123x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-020` | EVT-HOM-020 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-020-EXEC` | EVT-HOM-020 has executable commands | codes=101x1, 121x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-020-REQ` | EVT-HOM-020 includes required command family | codes=101x1, 121x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-021` | EVT-HOM-021 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-021-EXEC` | EVT-HOM-021 has executable commands | codes=101x1, 121x1, 123x1, 212x1, 250x1, 301x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-021-REQ` | EVT-HOM-021 includes required command family | codes=101x1, 121x1, 123x1, 212x1, 250x1, 301x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-022` | EVT-HOM-022 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-022-EXEC` | EVT-HOM-022 has executable commands | codes=101x1, 121x2, 122x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-022-REQ` | EVT-HOM-022 includes required command family | codes=101x1, 121x2, 122x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-023` | EVT-HOM-023 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-023-EXEC` | EVT-HOM-023 has executable commands | codes=101x2, 111x1, 401x2, 411x1, 412x1 |
| found | Atlas Event Commands | `EVT-HOM-023-REQ` | EVT-HOM-023 includes required command family | codes=101x2, 111x1, 401x2, 411x1, 412x1 |
| found | Atlas Event Commands | `EVT-HOM-024` | EVT-HOM-024 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-024-EXEC` | EVT-HOM-024 has executable commands | codes=101x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-024-REQ` | EVT-HOM-024 includes required command family | codes=101x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-025` | EVT-HOM-025 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-025-EXEC` | EVT-HOM-025 has executable commands | codes=101x4, 102x1, 111x1, 121x1, 401x4, 402x2, 404x1, 411x1, 412x1 |
| found | Atlas Event Commands | `EVT-HOM-025-REQ` | EVT-HOM-025 includes required command family | codes=101x4, 102x1, 111x1, 121x1, 401x4, 402x2, 404x1, 411x1, 412x1 |
| found | Atlas Event Commands | `EVT-HOM-026` | EVT-HOM-026 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-026-EXEC` | EVT-HOM-026 has executable commands | codes=101x1, 122x1, 123x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-026-REQ` | EVT-HOM-026 includes required command family | codes=101x1, 122x1, 123x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-027` | EVT-HOM-027 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-027-EXEC` | EVT-HOM-027 has executable commands | codes=101x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-027-REQ` | EVT-HOM-027 includes required command family | codes=101x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-028` | EVT-HOM-028 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-028-EXEC` | EVT-HOM-028 has executable commands | codes=101x1, 123x1, 126x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-028-REQ` | EVT-HOM-028 includes required command family | codes=101x1, 123x1, 126x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-029` | EVT-HOM-029 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-029-EXEC` | EVT-HOM-029 has executable commands | codes=101x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-029-REQ` | EVT-HOM-029 includes required command family | codes=101x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-030` | EVT-HOM-030 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-030-EXEC` | EVT-HOM-030 has executable commands | codes=101x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-030-REQ` | EVT-HOM-030 includes required command family | codes=101x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-031` | EVT-HOM-031 event exists | event found |
| found | Atlas Event Commands | `EVT-HOM-031-EXEC` | EVT-HOM-031 has executable commands | codes=101x1, 123x1, 212x1, 250x1, 401x1 |
| found | Atlas Event Commands | `EVT-HOM-031-REQ` | EVT-HOM-031 includes required command family | codes=101x1, 123x1, 212x1, 250x1, 401x1 |

### Local Anchor Commands

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Local Anchor Commands | `INT-ASH-WARM-STONE-VENT` | INT-ASH-WARM-STONE-VENT event exists | event found |
| found | Local Anchor Commands | `INT-ASH-WARM-STONE-VENT-EXEC` | INT-ASH-WARM-STONE-VENT has executable commands | codes=101x1, 401x2 |
| found | Local Anchor Commands | `INT-ASH-WARM-STONE-VENT-REQ` | INT-ASH-WARM-STONE-VENT includes required command family | codes=101x1, 401x2 |
| found | Local Anchor Commands | `INT-ASH-OLD-PANEL` | INT-ASH-OLD-PANEL event exists | event found |
| found | Local Anchor Commands | `INT-ASH-OLD-PANEL-EXEC` | INT-ASH-OLD-PANEL has executable commands | codes=101x1, 401x2 |
| found | Local Anchor Commands | `INT-ASH-OLD-PANEL-REQ` | INT-ASH-OLD-PANEL includes required command family | codes=101x1, 401x2 |
| found | Local Anchor Commands | `INT-ASH-ELARA-KEEPSAKE` | INT-ASH-ELARA-KEEPSAKE event exists | event found |
| found | Local Anchor Commands | `INT-ASH-ELARA-KEEPSAKE-EXEC` | INT-ASH-ELARA-KEEPSAKE has executable commands | codes=101x1, 401x3 |
| found | Local Anchor Commands | `INT-ASH-ELARA-KEEPSAKE-REQ` | INT-ASH-ELARA-KEEPSAKE includes required command family | codes=101x1, 401x3 |
| found | Local Anchor Commands | `INT-ASH-SHOP-CABINET` | INT-ASH-SHOP-CABINET event exists | event found |
| found | Local Anchor Commands | `INT-ASH-SHOP-CABINET-EXEC` | INT-ASH-SHOP-CABINET has executable commands | codes=101x1, 401x2 |
| found | Local Anchor Commands | `INT-ASH-SHOP-CABINET-REQ` | INT-ASH-SHOP-CABINET includes required command family | codes=101x1, 401x2 |
| found | Local Anchor Commands | `INT-SKY-GEOMETRIC-STONES` | INT-SKY-GEOMETRIC-STONES event exists | event found |
| found | Local Anchor Commands | `INT-SKY-GEOMETRIC-STONES-EXEC` | INT-SKY-GEOMETRIC-STONES has executable commands | codes=101x2, 123x1, 401x4 |
| found | Local Anchor Commands | `INT-SKY-GEOMETRIC-STONES-REQ` | INT-SKY-GEOMETRIC-STONES includes required command family | codes=101x2, 123x1, 401x4 |
| found | Local Anchor Commands | `INT-HCV-WALL-CARVING` | INT-HCV-WALL-CARVING event exists | event found |
| found | Local Anchor Commands | `INT-HCV-WALL-CARVING-EXEC` | INT-HCV-WALL-CARVING has executable commands | codes=101x2, 123x1, 401x4 |
| found | Local Anchor Commands | `INT-HCV-WALL-CARVING-REQ` | INT-HCV-WALL-CARVING includes required command family | codes=101x2, 123x1, 401x4 |
| found | Local Anchor Commands | `OBJ-HOM-FOG-009` | OBJ-HOM-FOG-009 event exists | event found |
| found | Local Anchor Commands | `OBJ-HOM-FOG-009-EXEC` | OBJ-HOM-FOG-009 has executable commands | codes=101x2, 123x1, 126x1, 401x2 |
| found | Local Anchor Commands | `OBJ-HOM-FOG-009-REQ` | OBJ-HOM-FOG-009 includes required command family | codes=101x2, 123x1, 126x1, 401x2 |

### Transfer Commands

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Transfer Commands | `TRN-HOM-001` | TRN-HOM-001 event exists | event found |
| found | Transfer Commands | `TRN-HOM-001-EXEC` | TRN-HOM-001 has executable commands | codes=201x1 |
| found | Transfer Commands | `TRN-HOM-001-REQ` | TRN-HOM-001 includes required command family | codes=201x1 |
| found | Transfer Commands | `TRN-HOM-002` | TRN-HOM-002 event exists | event found |
| found | Transfer Commands | `TRN-HOM-002-EXEC` | TRN-HOM-002 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-002-REQ` | TRN-HOM-002 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-003` | TRN-HOM-003 event exists | event found |
| found | Transfer Commands | `TRN-HOM-003-EXEC` | TRN-HOM-003 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-003-REQ` | TRN-HOM-003 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-004` | TRN-HOM-004 event exists | event found |
| found | Transfer Commands | `TRN-HOM-004-EXEC` | TRN-HOM-004 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-004-REQ` | TRN-HOM-004 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-005` | TRN-HOM-005 event exists | event found |
| found | Transfer Commands | `TRN-HOM-005-EXEC` | TRN-HOM-005 has executable commands | codes=101x1, 201x1, 221x1, 222x1, 401x2 |
| found | Transfer Commands | `TRN-HOM-005-REQ` | TRN-HOM-005 includes required command family | codes=101x1, 201x1, 221x1, 222x1, 401x2 |
| found | Transfer Commands | `TRN-HOM-006` | TRN-HOM-006 event exists | event found |
| found | Transfer Commands | `TRN-HOM-006-EXEC` | TRN-HOM-006 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-006-REQ` | TRN-HOM-006 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-007` | TRN-HOM-007 event exists | event found |
| found | Transfer Commands | `TRN-HOM-007-EXEC` | TRN-HOM-007 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-007-REQ` | TRN-HOM-007 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-008` | TRN-HOM-008 event exists | event found |
| found | Transfer Commands | `TRN-HOM-008-EXEC` | TRN-HOM-008 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-008-REQ` | TRN-HOM-008 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-009` | TRN-HOM-009 event exists | event found |
| found | Transfer Commands | `TRN-HOM-009-EXEC` | TRN-HOM-009 has executable commands | codes=101x1, 201x1, 221x1, 222x1, 401x1 |
| found | Transfer Commands | `TRN-HOM-009-REQ` | TRN-HOM-009 includes required command family | codes=101x1, 201x1, 221x1, 222x1, 401x1 |
| found | Transfer Commands | `TRN-HOM-010` | TRN-HOM-010 event exists | event found |
| found | Transfer Commands | `TRN-HOM-010-EXEC` | TRN-HOM-010 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-010-REQ` | TRN-HOM-010 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-011` | TRN-HOM-011 event exists | event found |
| found | Transfer Commands | `TRN-HOM-011-EXEC` | TRN-HOM-011 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-011-REQ` | TRN-HOM-011 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-012` | TRN-HOM-012 event exists | event found |
| found | Transfer Commands | `TRN-HOM-012-EXEC` | TRN-HOM-012 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-012-REQ` | TRN-HOM-012 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-013` | TRN-HOM-013 event exists | event found |
| found | Transfer Commands | `TRN-HOM-013-EXEC` | TRN-HOM-013 has executable commands | codes=101x3, 111x3, 201x1, 221x1, 222x1, 401x6, 411x3, 412x3 |
| found | Transfer Commands | `TRN-HOM-013-REQ` | TRN-HOM-013 includes required command family | codes=101x3, 111x3, 201x1, 221x1, 222x1, 401x6, 411x3, 412x3 |
| found | Transfer Commands | `TRN-HOM-014` | TRN-HOM-014 event exists | event found |
| found | Transfer Commands | `TRN-HOM-014-EXEC` | TRN-HOM-014 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-014-REQ` | TRN-HOM-014 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-015` | TRN-HOM-015 event exists | event found |
| found | Transfer Commands | `TRN-HOM-015-EXEC` | TRN-HOM-015 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-015-REQ` | TRN-HOM-015 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-016` | TRN-HOM-016 event exists | event found |
| found | Transfer Commands | `TRN-HOM-016-EXEC` | TRN-HOM-016 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-016-REQ` | TRN-HOM-016 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-017` | TRN-HOM-017 event exists | event found |
| found | Transfer Commands | `TRN-HOM-017-EXEC` | TRN-HOM-017 has executable commands | codes=101x1, 201x1, 221x1, 222x1, 401x1 |
| found | Transfer Commands | `TRN-HOM-017-REQ` | TRN-HOM-017 includes required command family | codes=101x1, 201x1, 221x1, 222x1, 401x1 |
| found | Transfer Commands | `TRN-HOM-018` | TRN-HOM-018 event exists | event found |
| found | Transfer Commands | `TRN-HOM-018-EXEC` | TRN-HOM-018 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-018-REQ` | TRN-HOM-018 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-019` | TRN-HOM-019 event exists | event found |
| found | Transfer Commands | `TRN-HOM-019-EXEC` | TRN-HOM-019 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-019-REQ` | TRN-HOM-019 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-020` | TRN-HOM-020 event exists | event found |
| found | Transfer Commands | `TRN-HOM-020-EXEC` | TRN-HOM-020 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-020-REQ` | TRN-HOM-020 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-021` | TRN-HOM-021 event exists | event found |
| found | Transfer Commands | `TRN-HOM-021-EXEC` | TRN-HOM-021 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-021-REQ` | TRN-HOM-021 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-022` | TRN-HOM-022 event exists | event found |
| found | Transfer Commands | `TRN-HOM-022-EXEC` | TRN-HOM-022 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-022-REQ` | TRN-HOM-022 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-023` | TRN-HOM-023 event exists | event found |
| found | Transfer Commands | `TRN-HOM-023-EXEC` | TRN-HOM-023 has executable commands | codes=101x1, 201x1, 221x1, 222x1, 401x1 |
| found | Transfer Commands | `TRN-HOM-023-REQ` | TRN-HOM-023 includes required command family | codes=101x1, 201x1, 221x1, 222x1, 401x1 |
| found | Transfer Commands | `TRN-HOM-024` | TRN-HOM-024 event exists | event found |
| found | Transfer Commands | `TRN-HOM-024-EXEC` | TRN-HOM-024 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-024-REQ` | TRN-HOM-024 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-025` | TRN-HOM-025 event exists | event found |
| found | Transfer Commands | `TRN-HOM-025-EXEC` | TRN-HOM-025 has executable commands | codes=101x3, 102x1, 111x1, 121x1, 201x1, 221x1, 222x1, 401x3, 402x2, 404x1, 411x1, 412x1 |
| found | Transfer Commands | `TRN-HOM-025-REQ` | TRN-HOM-025 includes required command family | codes=101x3, 102x1, 111x1, 121x1, 201x1, 221x1, 222x1, 401x3, 402x2, 404x1, 411x1, 412x1 |
| found | Transfer Commands | `TRN-HOM-026` | TRN-HOM-026 event exists | event found |
| found | Transfer Commands | `TRN-HOM-026-EXEC` | TRN-HOM-026 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-026-REQ` | TRN-HOM-026 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-027` | TRN-HOM-027 event exists | event found |
| found | Transfer Commands | `TRN-HOM-027-EXEC` | TRN-HOM-027 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-027-REQ` | TRN-HOM-027 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-028` | TRN-HOM-028 event exists | event found |
| found | Transfer Commands | `TRN-HOM-028-EXEC` | TRN-HOM-028 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-028-REQ` | TRN-HOM-028 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-029` | TRN-HOM-029 event exists | event found |
| found | Transfer Commands | `TRN-HOM-029-EXEC` | TRN-HOM-029 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-029-REQ` | TRN-HOM-029 includes required command family | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-030` | TRN-HOM-030 event exists | event found |
| found | Transfer Commands | `TRN-HOM-030-EXEC` | TRN-HOM-030 has executable commands | codes=201x1, 221x1, 222x1 |
| found | Transfer Commands | `TRN-HOM-030-REQ` | TRN-HOM-030 includes required command family | codes=201x1, 221x1, 222x1 |

## Notes

- Executable commands are commands beyond comments and event terminators.
- The audit checks command-family presence, not final dialogue quality or runtime timing.
- This audit does not modify RPG Maker data files.
