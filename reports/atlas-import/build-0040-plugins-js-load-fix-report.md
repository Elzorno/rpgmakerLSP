# BUILD-0040 - RPG Maker plugins.js Load Fix

## Objective

Fix the RPG Maker MZ boot/editor blocker reported as `unable to read plugins.js`.

## User Report

RPG Maker would not load the clean project and reported that it was unable to read `plugins.js`.

## Project

- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`
- File: `js/plugins.js`

## Finding

The clean game project's `js/plugins.js` existed and evaluated as JavaScript, but it used the minimal one-line form:

```js
var $plugins = [];
```

RPG Maker normally writes this file in a multi-line generated format. To reduce editor/runtime compatibility risk, BUILD-0040 normalizes the clean skeleton output to RPG Maker's native generated shape.

## Fix

- Updated `tools/atlas-import/create_clean_skeleton.py` so future clean skeleton generation writes RPG Maker-style `plugins.js`.
- Updated `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game/js/plugins.js` to the same normalized format.
- Attempted to clear macOS extended attributes from the file. macOS retained `com.apple.provenance`; this is common on newer macOS and the file remained readable by local HTTP and JavaScript evaluation.

## Verification

- `plugins.js` evaluates and defines `$plugins` as an array.
- Local HTTP fetch of `/js/plugins.js` returns `200`.
- RPG Maker data JSON still parses.
- Atlas validation remains clean.

## Runtime Status

Fixed at file/data level. Needs user runtime confirmation in RPG Maker MZ.
