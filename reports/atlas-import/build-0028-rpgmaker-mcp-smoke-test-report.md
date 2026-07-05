# BUILD-0028 - RPG Maker MZ MCP Smoke Test

## Summary

BUILD-0028 verified that the RPG Maker MZ MCP server is callable from this Codex session and is pointed at the clean game repository.

Result: GO. The MCP returned the expected game title, Home Island switches, and Home Island variables from `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`.

## MCP Checks

- `mcp__rpgmaker_mz.get_game_title`: returned `The Last Sword Protocol`
- `mcp__rpgmaker_mz.get_switches`: returned expected Journey I switch names, including `J1_Tremor_Event`, `J1_Skyreach_AccessOpen`, `J1_Sword_Obtained`, `J1_Node07_RelayRestored`, and `J1_Mainland_TravelUnlocked`
- `mcp__rpgmaker_mz.get_variables`: returned expected variable names, including `Current_Journey`, `Archive_Recovery_Percent`, `Trial_Body_Attempts`, `Trial_Mind_SequenceStep`, `Trial_Heart_IntentChoice`, and `Current_Encounter_Zone`

## Local Config Checks

- `codex mcp list`: `rpgmaker-mz` enabled
- `codex mcp get rpgmaker-mz`: command `node`, args `.codex/rpgmaker-mz-mcp-launcher.cjs`, `RPGMAKER_PROJECT_PATH` present
- `.codex/rpgmaker-mz-mcp-launcher.cjs`: default project path is `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`

## Local Data Checks

- `System.json` title: `The Last Sword Protocol`
- Start position: map 2 at `(8, 6)`
- Switches 1-14 match Journey I progression switches
- Variables 1-2 match `Current_Journey` and `Archive_Recovery_Percent`
- Variables 50-52 match Body / Mind / Heart trial variables

## Validation Result

- MCP smoke test: PASS
- All-map route audit: found 258, missing 0, warning 0
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- This smoke test proves MCP connectivity and read access to the clean game repo.
- It does not launch the RPG Maker editor or run an in-engine playtest.
- No RPG Maker data files, Atlas content files, or game assets were modified.
