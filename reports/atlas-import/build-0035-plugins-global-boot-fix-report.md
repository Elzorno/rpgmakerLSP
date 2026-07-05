# BUILD-0035 - RPG Maker Plugins Global Boot Fix

## Summary

BUILD-0035 fixes the runtime boot blocker reported during playtest:

```text
$plugins is not defined
```

RPG Maker MZ expects `js/plugins.js` to define the global `var $plugins = [...]`. The clean skeleton project had `js/plugins.js` containing only a raw JSON array (`[]`), so `main.js` failed at `PluginManager.setup($plugins)`.

## Fix

- Updated current clean game file:
  - `../TheLastSwordProtocol-Game/js/plugins.js`
- Updated clean skeleton generator:
  - `tools/atlas-import/create_clean_skeleton.py`

The generated/current file now contains:

```js
var $plugins = [];
```

## Verification

- `node --check ../TheLastSwordProtocol-Game/js/plugins.js`: PASS
- Node VM check: `$plugins` exists and is an array with length 0
- `tools/atlas-import/create_clean_skeleton.py` py_compile: PASS
- All RPG Maker JS files passed `node --check`
- All RPG Maker `data/*.json` files parsed
- HTTP check served `/js/plugins.js` as `var $plugins = [];`

## Validation Result

- Event-command coverage audit: found 204, missing 0, warning 0
- All-map route audit: found 258, missing 0, warning 0
- Vertical-slice playthrough audit: found 81, missing 0, warning 0, unknown 1
- Clean skeleton data audit: found 335, missing 0, warning 0, unknown 1
- Atlas export validation: PASS
- Atlas validation: 0 errors, 0 warnings

## Notes

- No plugin behavior was added.
- The project still has an empty plugin list; it is now represented in RPG Maker's expected JavaScript format.
- This should resolve the reported `$plugins is not defined` boot error.
