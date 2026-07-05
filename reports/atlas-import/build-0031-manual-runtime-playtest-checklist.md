# BUILD-0031 - Manual Runtime Playtest Checklist

## Goal

Verify the generated Home Island vertical slice inside RPG Maker MZ or a packaged runtime.

JSON audits have passed, but they cannot prove player feel, collision, event timing, visual readability, or battle pacing. This checklist is the runtime gate for those items.

## Preconditions

- Open `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game` in RPG Maker MZ.
- Start a new playtest from the configured start position.
- Do not manually set switches or variables unless a checkpoint explicitly says to test a gated state.
- Record failures with map name, event name, coordinates, observed behavior, and screenshot if possible.

## Smoke Checks

| Check | Expected Result | Status |
|---|---|---|
| New game launches | Game starts in Elara House at map 2, coordinate `(8, 6)` | Not Run |
| Player can move | Player is not stuck on the start tile | Not Run |
| Menu opens | Default menu opens and closes without crash | Not Run |
| Save disabled/enabled policy | Save behavior matches project defaults or Atlas save-point policy | Not Run |

## Critical Route

| Step | Action | Expected Result | Status |
|---:|---|---|---|
| 1 | Trigger Player Start in Elara House | Intro placeholder runs once; no loop lock | Not Run |
| 2 | Talk to Elara | Elara placeholder interaction displays | Not Run |
| 3 | Use Elara House exit | Transfers to Ashford Exterior | Not Run |
| 4 | Trigger Ashford Tremor | Tremor event opens Skyreach access | Not Run |
| 5 | Use Skyreach transfer | Transfers to Skyreach Hill Path when gate is open | Not Run |
| 6 | Enter Hidden Cave | Hidden Cave entrance transfer works | Not Run |
| 7 | Enter trial chamber | Transfers to Hidden Cave Trials | Not Run |
| 8 | Complete Body Trial | Body clear switch is set; no softlock | Not Run |
| 9 | Complete Mind Trial | Mind clear switch is set; no softlock | Not Run |
| 10 | Complete Heart Trial | Heart clear switch is set or reset feedback behaves correctly | Not Run |
| 11 | Enter Sword Sanctum | Gate opens only when trial switches are clear | Not Run |
| 12 | Use Sword Pedestal | Sword/item placeholder reward runs once | Not Run |
| 13 | Return to Ashford then route to Glassfield | Transfers remain usable after Sword event | Not Run |
| 14 | Open Glassfield Seal | Seal event opens Sealed Node access | Not Run |
| 15 | Traverse Sealed Node Upper/Core/Guardian | Forward and return transfers work | Not Run |
| 16 | Fight Node Seven Guardian | Battle starts, resolves, and sets defeat switch | Not Run |
| 17 | Enter Relay Core | Gate opens after Guardian defeat | Not Run |
| 18 | Trigger Relay Core | Relay restoration and mainland unlock placeholders run once | Not Run |
| 19 | Travel to Rustshore | Rustshore transfer works from Ashford route | Not Run |
| 20 | Begin departure | Departure gate respects mainland unlock and reaches Mainland Departure | Not Run |
| 21 | Trigger Mainland Departure | Journey II placeholder transfer works or clearly reaches placeholder map | Not Run |

## Optional Routes

| Route | Expected Result | Status |
|---|---|---|
| Ashford Shop entry and exit | Player can enter shop, talk to shopkeeper, and return to Ashford | Not Run |
| Fogfen Marsh Field entry and return | Player can enter optional Fogfen and return to Ashford route | Not Run |
| Deeper Marsh branch | Player can enter Deeper Marsh Pocket and return to Fogfen Marsh Field | Not Run |
| Rustshore return | Player can return from Rustshore to Ashford route | Not Run |
| Sealed Node backtracking | All return transfers work without trapping player | Not Run |

## Local Examine Events

| Event | Expected Result | Status |
|---|---|---|
| Warm-Stone Vent | Placeholder examine text appears | Not Run |
| Old Panel | Placeholder examine text appears | Not Run |
| Elara Keepsake Shelf | Placeholder examine text appears | Not Run |
| Shop Metal Cabinet | Placeholder examine text appears | Not Run |
| Skyreach Geometric Stones | Placeholder examine text appears | Not Run |
| Hidden Cave Wall Carving | Placeholder examine text appears | Not Run |
| Deeper Marsh Reward Cache | Potion reward fires once; repeat page does not grant again | Not Run |

## Map And Collision Checks

| Area | Expected Result | Status |
|---|---|---|
| Ashford Exterior | Paths are readable; transfers are discoverable; player cannot walk through intended blockers | Not Run |
| Interiors | Exit tiles are clear; furniture blocks are sensible | Not Run |
| Skyreach | Critical path to Hidden Cave is readable | Not Run |
| Hidden Cave | Trial path, sanctum gate, and return paths are readable | Not Run |
| Glassfield | Seal and Sealed Node entry are discoverable | Not Run |
| Sealed Node | Core path and boss route are readable | Not Run |
| Rustshore | Dockmaster, lighthouse, boat/departure area are readable | Not Run |
| Fogfen | Encounter zones do not trap player; optional branch remains escapable | Not Run |

## Combat Checks

| Encounter | Expected Result | Status |
|---|---|---|
| Home field random encounter | Encounter starts in expected regions and is survivable | Not Run |
| Fogfen random encounter | Fogfen troops appear in Region 2 and remain early-game safe | Not Run |
| Node Seven Guardian | Boss troop starts, can be defeated, and exits battle cleanly | Not Run |

## Evidence To Record

- RPG Maker MZ version.
- Playtest date and tester.
- Any plugins enabled at runtime.
- First blocking failure, if any.
- Screenshots for collision, transfer, or event timing issues.
- Final decision: GO / NO GO for next implementation stage.

## Current Status

Not Run.

This checklist is ready for manual execution. No runtime playtest was performed during BUILD-0031.
