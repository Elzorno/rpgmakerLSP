The Last Sword Protocol — Ancestor Cave Tileset for RPG Maker MZ
=================================================================

Drop the PNG files into your project folder:
  img/tilesets/

Create a new database tileset named:
  Tileset 09 — Ancestor Cave

Assign these image slots:
  A1: LSP_Cave_A1.png              768 × 576
  A2: LSP_Cave_A2.png              768 × 576
  A3: LSP_Cave_A3_blank.png        768 × 384  (optional blank placeholder)
  A4: LSP_Cave_A4.png              768 × 720
  A5: LSP_Cave_A5.png              384 × 768
  B : LSP_Chamber2_Terminals.png   768 × 768  (top-left tile intentionally transparent)
  C : LSP_Cave_C.png               768 × 768

Recommended MZ flags:
  O      Floors, catwalks, glow strips, shallow floor decals.
  X      Walls, pillars, boulders, rubble, terminals, gauntlet rig, mirror, pedestal.
  Star   Light shaft, radial glow decal, hanging cables, banners, ceiling stalactites.
  Counter flag: terminal banks and console-like control rigs.

Design notes:
  - Built from the spec's sacred tomb + dormant old-world technology direction.
  - Every powered concept has a dormant or lower-energy counterpart where possible.
  - Signature glow is #36B4EC. Chamber accents: amber for the gauntlet, violet for the mirror, blue-white for the pedestal.
  - This is a first-pass production tileset generated to MZ sheet dimensions. It is ready to import, but you may still want to hand-tune passability and autotile behavior in the database after mapping tests.

Files included:
  LSP_Cave_A1.png
  LSP_Cave_A2.png
  LSP_Cave_A3_blank.png
  LSP_Cave_A4.png
  LSP_Cave_A5.png
  LSP_Chamber2_Terminals.png
  LSP_Cave_C.png
  LSP_Ancestor_Cave_preview.png
  LSP_Cave_MZ_manifest.json
