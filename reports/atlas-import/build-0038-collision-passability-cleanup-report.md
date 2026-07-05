# BUILD-0038 - Collision Passability Cleanup Report

## Objective

Remove passable upper-layer tiles from cells whose base terrain is blocked by the RPG Maker tileset flags.

## Project

- Project root: `/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game`

## Result

- Maps changed: 10
- Upper-layer tiles cleared: 490

## Cause

Generated layouts could paint blocked base terrain, then leave a passable layer-1 terrain/path tile above it. RPG Maker MZ checks upper layers before the base layer, so those cells could become passable even though the layout intended them to block movement.

## Maps Updated

- `Map001.json`: 239 upper-layer tile(s) cleared
- `Map002.json`: 15 upper-layer tile(s) cleared
- `Map003.json`: 13 upper-layer tile(s) cleared
- `Map004.json`: 102 upper-layer tile(s) cleared
- `Map006.json`: 1 upper-layer tile(s) cleared
- `Map008.json`: 32 upper-layer tile(s) cleared
- `Map009.json`: 3 upper-layer tile(s) cleared
- `Map013.json`: 22 upper-layer tile(s) cleared
- `Map015.json`: 54 upper-layer tile(s) cleared
- `Map016.json`: 9 upper-layer tile(s) cleared

## Sample Cleared Tiles

- `Map001.json` (0, 0) layer 1: cleared tile 2836
- `Map001.json` (1, 0) layer 1: cleared tile 2836
- `Map001.json` (2, 0) layer 1: cleared tile 2836
- `Map001.json` (3, 0) layer 1: cleared tile 2836
- `Map001.json` (4, 0) layer 1: cleared tile 2836
- `Map001.json` (5, 0) layer 1: cleared tile 2836
- `Map001.json` (6, 0) layer 1: cleared tile 2836
- `Map001.json` (7, 0) layer 1: cleared tile 2836
- `Map001.json` (8, 0) layer 1: cleared tile 2836
- `Map001.json` (9, 0) layer 1: cleared tile 2836
- `Map001.json` (10, 0) layer 1: cleared tile 2836
- `Map001.json` (11, 0) layer 1: cleared tile 2836
- `Map001.json` (12, 0) layer 1: cleared tile 2836
- `Map001.json` (13, 0) layer 1: cleared tile 2836
- `Map001.json` (14, 0) layer 1: cleared tile 2836
- `Map001.json` (15, 0) layer 1: cleared tile 2836
- `Map001.json` (16, 0) layer 1: cleared tile 2836
- `Map001.json` (17, 0) layer 1: cleared tile 2836
- `Map001.json` (18, 0) layer 1: cleared tile 2836
- `Map001.json` (19, 0) layer 1: cleared tile 2836
- `Map001.json` (21, 0) layer 1: cleared tile 2836
- `Map001.json` (22, 0) layer 1: cleared tile 2836
- `Map001.json` (23, 0) layer 1: cleared tile 2836
- `Map001.json` (24, 0) layer 1: cleared tile 2836
- `Map001.json` (25, 0) layer 1: cleared tile 2836
- Additional cleared tiles omitted from sample list.
