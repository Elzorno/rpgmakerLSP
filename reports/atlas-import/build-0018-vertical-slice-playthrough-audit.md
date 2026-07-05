# BUILD-0008 - Home Island Vertical Slice Playthrough Audit

This read-only audit checks the clean RPG Maker MZ skeleton for a machine-visible Home Island route from new game start to the Journey II placeholder.

- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`

## Summary

- Found: 81
- Missing: 0
- Present with warning: 0
- Not machine-checkable yet: 1
- Total findings: 82

## Category Summary

| Category | Found | Missing | Warning | Not Machine-Checkable |
|---|---:|---:|---:|---:|
| Critical Route | 31 | 0 | 0 | 0 |
| Critical Route Effects | 39 | 0 | 0 | 0 |
| Manual Runtime Scope | 0 | 0 | 0 | 1 |
| Return Transfers | 9 | 0 | 0 | 0 |
| Start State | 2 | 0 | 0 | 0 |

## Findings

### Critical Route

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Critical Route | `ROUTE-001` | Map 2 event Player Start | Event id 1 at (8, 6) |
| found | Critical Route | `ROUTE-002` | Map 2 event TRN-HOM-001 Elara House exit | Event id 3 at (8, 12) |
| found | Critical Route | `ROUTE-003` | Map 1 event Tremor Trigger | Event id 6 at (20, 9) |
| found | Critical Route | `ROUTE-004` | Map 1 event TRN-HOM-005 North path to Skyreach | Event id 9 at (20, 0) |
| found | Critical Route | `ROUTE-005` | Map 4 event TRN-HOM-009 Enter Hidden Cave | Event id 3 at (15, 1) |
| found | Critical Route | `ROUTE-006` | Map 5 event Hidden Cave First Entry | Event id 1 at (12, 18) |
| found | Critical Route | `ROUTE-007` | Map 5 event TRN-HOM-011 Enter trials | Event id 3 at (12, 1) |
| found | Critical Route | `ROUTE-008` | Map 6 event Body Trial | Event id 1 at (12, 20) |
| found | Critical Route | `ROUTE-009` | Map 6 event Mind Trial | Event id 2 at (20, 16) |
| found | Critical Route | `ROUTE-010` | Map 6 event Heart Trial | Event id 3 at (31, 20) |
| found | Critical Route | `ROUTE-011` | Map 6 event TRN-HOM-013 Enter Sword Sanctum | Event id 6 at (20, 0) |
| found | Critical Route | `ROUTE-012` | Map 7 event Sword Pedestal | Event id 1 at (11, 8) |
| found | Critical Route | `ROUTE-013` | Map 8 event Glassfield Seal | Event id 1 at (22, 5) |
| found | Critical Route | `ROUTE-014` | Map 8 event TRN-HOM-017 Enter Sealed Node | Event id 4 at (22, 1) |
| found | Critical Route | `ROUTE-015` | Map 9 event Sealed Node First Entry | Event id 1 at (17, 25) |
| found | Critical Route | `ROUTE-016` | Map 10 event Core Path Door | Event id 1 at (19, 13) |
| found | Critical Route | `ROUTE-017` | Map 11 event Node Seven Guardian | Event id 1 at (13, 11) |
| found | Critical Route | `ROUTE-018` | Map 11 event TRN-HOM-023 Enter relay core | Event id 3 at (13, 0) |
| found | Critical Route | `ROUTE-019` | Map 12 event Relay Core | Event id 1 at (8, 5) |
| found | Critical Route | `ROUTE-020` | Map 13 event TRN-HOM-025 Begin departure | Event id 5 at (14, 8) |
| found | Critical Route | `ROUTE-021` | Map 14 event Departure Sequence | Event id 1 at (8, 6) |
| found | Critical Route | `ROUTE-022` | Map 14 event TRN-HOM-026 Destination TBD: Coalmouth or landing screen | Event id 2 at (8, 0) |
| found | Critical Route | `RETURN-001` | Map 7 event TRN-HOM-014 Return from sanctum | Event id 2 at (11, 18) |
| found | Critical Route | `RETURN-002` | Map 6 event TRN-HOM-012 Return to entrance | Event id 5 at (20, 31) |
| found | Critical Route | `RETURN-003` | Map 5 event TRN-HOM-010 Exit cave | Event id 2 at (12, 23) |
| found | Critical Route | `RETURN-004` | Map 4 event TRN-HOM-006 Return from Skyreach route | Event id 2 at (15, 39) |
| found | Critical Route | `RETURN-005` | Map 9 event TRN-HOM-018 Exit Sealed Node | Event id 2 at (17, 29) |
| found | Critical Route | `RETURN-006` | Map 10 event TRN-HOM-020 Return to upper node | Event id 2 at (19, 31) |
| found | Critical Route | `RETURN-007` | Map 11 event TRN-HOM-022 Return to core path | Event id 2 at (13, 22) |
| found | Critical Route | `RETURN-008` | Map 12 event TRN-HOM-024 Return from relay core | Event id 2 at (8, 12) |
| found | Critical Route | `RETURN-009` | Map 13 event TRN-HOM-008 Return from Rustshore route | Event id 4 at (0, 9) |

### Critical Route Effects

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Critical Route Effects | `ROUTE-001` | Player Start: Current_Journey = 1 | Current_Journey = 1 |
| found | Critical Route Effects | `ROUTE-001` | Player Start: Archive_Recovery_Percent = 0 | Archive_Recovery_Percent = 0 |
| found | Critical Route Effects | `ROUTE-002` | TRN-HOM-001 Elara House exit: Transfer to Ashford Exterior | Transfer to Ashford Exterior |
| found | Critical Route Effects | `ROUTE-003` | Tremor Trigger: J1_Tremor_Event ON | J1_Tremor_Event ON |
| found | Critical Route Effects | `ROUTE-003` | Tremor Trigger: J1_Skyreach_AccessOpen ON | J1_Skyreach_AccessOpen ON |
| found | Critical Route Effects | `ROUTE-004` | TRN-HOM-005 North path to Skyreach: Transfer to Skyreach | Transfer to Skyreach |
| found | Critical Route Effects | `ROUTE-004` | TRN-HOM-005 North path to Skyreach: Gate requires J1_Skyreach_AccessOpen | Gate requires J1_Skyreach_AccessOpen |
| found | Critical Route Effects | `ROUTE-005` | TRN-HOM-009 Enter Hidden Cave: Transfer to Hidden Cave | Transfer to Hidden Cave |
| found | Critical Route Effects | `ROUTE-005` | TRN-HOM-009 Enter Hidden Cave: Gate requires J1_Skyreach_AccessOpen | Gate requires J1_Skyreach_AccessOpen |
| found | Critical Route Effects | `ROUTE-006` | Hidden Cave First Entry: J1_HiddenCave_Entered ON | J1_HiddenCave_Entered ON |
| found | Critical Route Effects | `ROUTE-007` | TRN-HOM-011 Enter trials: Transfer to Hidden Cave Trials | Transfer to Hidden Cave Trials |
| found | Critical Route Effects | `ROUTE-008` | Body Trial: J1_Trial_Body_Clear ON | J1_Trial_Body_Clear ON |
| found | Critical Route Effects | `ROUTE-009` | Mind Trial: J1_Trial_Mind_Clear ON | J1_Trial_Mind_Clear ON |
| found | Critical Route Effects | `ROUTE-010` | Heart Trial: J1_Trial_Heart_Clear ON | J1_Trial_Heart_Clear ON |
| found | Critical Route Effects | `ROUTE-011` | TRN-HOM-013 Enter Sword Sanctum: Transfer to Sword Sanctum | Transfer to Sword Sanctum |
| found | Critical Route Effects | `ROUTE-011` | TRN-HOM-013 Enter Sword Sanctum: Checks Body trial | Checks Body trial |
| found | Critical Route Effects | `ROUTE-011` | TRN-HOM-013 Enter Sword Sanctum: Checks Mind trial | Checks Mind trial |
| found | Critical Route Effects | `ROUTE-011` | TRN-HOM-013 Enter Sword Sanctum: Checks Heart trial | Checks Heart trial |
| found | Critical Route Effects | `ROUTE-012` | Sword Pedestal: J1_Sword_Obtained ON | J1_Sword_Obtained ON |
| found | Critical Route Effects | `ROUTE-012` | Sword Pedestal: Archive_Recovery_Percent = 3 | Archive_Recovery_Percent = 3 |
| found | Critical Route Effects | `ROUTE-012` | Sword Pedestal: Sword key item gained | Sword key item gained |
| found | Critical Route Effects | `ROUTE-012` | Sword Pedestal: Sword weapon gained | Sword weapon gained |
| found | Critical Route Effects | `ROUTE-013` | Glassfield Seal: J1_Glassfield_SealOpened ON | J1_Glassfield_SealOpened ON |
| found | Critical Route Effects | `ROUTE-014` | TRN-HOM-017 Enter Sealed Node: Transfer to Sealed Node Upper | Transfer to Sealed Node Upper |
| found | Critical Route Effects | `ROUTE-014` | TRN-HOM-017 Enter Sealed Node: Gate requires J1_Glassfield_SealOpened | Gate requires J1_Glassfield_SealOpened |
| found | Critical Route Effects | `ROUTE-015` | Sealed Node First Entry: J1_SealedNode_Entered ON | J1_SealedNode_Entered ON |
| found | Critical Route Effects | `ROUTE-016` | Core Path Door: J1_CorePath_DoorOpened ON | J1_CorePath_DoorOpened ON |
| found | Critical Route Effects | `ROUTE-017` | Node Seven Guardian: Battle Processing troop 10 | Battle Processing troop 10 |
| found | Critical Route Effects | `ROUTE-017` | Node Seven Guardian: J1_Node07_GuardianDefeated ON | J1_Node07_GuardianDefeated ON |
| found | Critical Route Effects | `ROUTE-018` | TRN-HOM-023 Enter relay core: Transfer to Relay Core | Transfer to Relay Core |
| found | Critical Route Effects | `ROUTE-018` | TRN-HOM-023 Enter relay core: Gate requires J1_Node07_GuardianDefeated | Gate requires J1_Node07_GuardianDefeated |
| found | Critical Route Effects | `ROUTE-019` | Relay Core: J1_Node07_RelayRestored ON | J1_Node07_RelayRestored ON |
| found | Critical Route Effects | `ROUTE-019` | Relay Core: J1_Mainland_TravelUnlocked ON | J1_Mainland_TravelUnlocked ON |
| found | Critical Route Effects | `ROUTE-019` | Relay Core: Archive_Recovery_Percent = 5 | Archive_Recovery_Percent = 5 |
| found | Critical Route Effects | `ROUTE-020` | TRN-HOM-025 Begin departure: Transfer to departure map | Transfer to departure map |
| found | Critical Route Effects | `ROUTE-020` | TRN-HOM-025 Begin departure: Checks J1_Mainland_TravelUnlocked | Checks J1_Mainland_TravelUnlocked |
| found | Critical Route Effects | `ROUTE-020` | TRN-HOM-025 Begin departure: J1_Departure_Confirmed ON | J1_Departure_Confirmed ON |
| found | Critical Route Effects | `ROUTE-021` | Departure Sequence: Current_Journey = 2 | Current_Journey = 2 |
| found | Critical Route Effects | `ROUTE-022` | TRN-HOM-026 Destination TBD: Coalmouth or landing screen: Transfer to Journey II placeholder | Transfer to Journey II placeholder |

### Manual Runtime Scope

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| not machine-checkable yet | Manual Runtime Scope | `MANUAL-001` | Manual RPG Maker runtime playthrough | JSON audit proves route structure; hands-on runtime timing/input feel still requires RPG Maker playtest. |

### Return Transfers

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Return Transfers | `RETURN-001` | TRN-HOM-014 Return from sanctum: transfer to map 6 | Transfer to map 6 |
| found | Return Transfers | `RETURN-002` | TRN-HOM-012 Return to entrance: transfer to map 5 | Transfer to map 5 |
| found | Return Transfers | `RETURN-003` | TRN-HOM-010 Exit cave: transfer to map 4 | Transfer to map 4 |
| found | Return Transfers | `RETURN-004` | TRN-HOM-006 Return from Skyreach route: transfer to map 1 | Transfer to map 1 |
| found | Return Transfers | `RETURN-005` | TRN-HOM-018 Exit Sealed Node: transfer to map 8 | Transfer to map 8 |
| found | Return Transfers | `RETURN-006` | TRN-HOM-020 Return to upper node: transfer to map 9 | Transfer to map 9 |
| found | Return Transfers | `RETURN-007` | TRN-HOM-022 Return to core path: transfer to map 10 | Transfer to map 10 |
| found | Return Transfers | `RETURN-008` | TRN-HOM-024 Return from relay core: transfer to map 11 | Transfer to map 11 |
| found | Return Transfers | `RETURN-009` | TRN-HOM-008 Return from Rustshore route: transfer to map 1 | Transfer to map 1 |

### Start State

| Status | Category | Check ID | Expected | Detail |
|---|---|---|---|---|
| found | Start State | `START-001` | Start map is Elara House map 2 | startMapId=2 |
| found | Start State | `START-002` | Start coordinate is within map bounds | start=(8, 6) |

## Notes

- `missing` means a critical route event, transfer, switch, variable, battle, or reward command was not found.
- `not machine-checkable yet` is limited to hands-on RPG Maker runtime playtest feel and timing.
- This audit does not modify RPG Maker data files.
