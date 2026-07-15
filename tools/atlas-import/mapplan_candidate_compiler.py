#!/usr/bin/env python3
"""Compile an engine-neutral MapPlan into a guarded RPG Maker MZ candidate.

This adapter writes only to a caller-supplied project whose ownership ledger
marks the target map generated. Production promotion is intentionally absent.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import tempfile
from collections import deque
from pathlib import Path
from typing import Any

from autotile import paint_region
from map_ownership_guard import load_ledger, map_write_allowed, skip_message
from validate_tile_palette import verify_palette


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(payload, handle, ensure_ascii=False, separators=(",", ":"))
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def event_page(commands: list[dict[str, Any]], *, trigger: int, priority: int = 1) -> dict[str, Any]:
    return {
        "conditions": {"actorId": 1, "actorValid": False, "itemId": 1, "itemValid": False,
                       "selfSwitchCh": "A", "selfSwitchValid": False, "switch1Id": 1,
                       "switch1Valid": False, "switch2Id": 1, "switch2Valid": False,
                       "variableId": 1, "variableValid": False, "variableValue": 0},
        "directionFix": False,
        "image": {"characterName": "", "characterIndex": 0, "direction": 2, "pattern": 1, "tileId": 0},
        "list": commands + [{"code": 0, "indent": 0, "parameters": []}],
        "moveFrequency": 3, "moveRoute": {"list": [{"code": 0, "indent": 0, "parameters": []}],
        "repeat": True, "skippable": False, "wait": False}, "moveSpeed": 3, "moveType": 0,
        "priorityType": priority, "stepAnime": False, "through": False, "trigger": trigger, "walkAnime": True,
    }


class CandidateError(ValueError):
    pass


class CandidateCompiler:
    def __init__(self, plan: dict[str, Any], palette: dict[str, Any], style: dict[str, Any], flags: list[int]):
        self.plan, self.palette, self.style, self.flags = plan, palette, style, flags
        self.width = int(plan["dimensions"]["width"]) + 2
        self.height = int(plan["dimensions"]["height"]) + 2
        self.data = [0] * (self.width * self.height * 6)
        self.collision_cells: set[tuple[int, int]] = set()
        self.diagnostics: list[dict[str, Any]] = []
        self.bindings: dict[str, list[dict[str, Any]]] = {}
        for binding in palette["bindings"]:
            self.bindings.setdefault(binding["visual_tag"], []).append(binding)

    def index(self, x: int, y: int, layer: int) -> int:
        return (layer * self.height + y) * self.width + x

    def set_tile(self, x: int, y: int, layer: int, tile_id: int) -> None:
        if 0 <= x < self.width and 0 <= y < self.height:
            self.data[self.index(x, y, layer)] = int(tile_id)

    def binding(self, tag: str, component: str | None = None) -> dict[str, Any]:
        resolved_tag = tag
        if resolved_tag == "bed_desk_nook":
            resolved_tag = "striped_cabana_bed" if "striped_cabana_bed" in self.bindings else "quilted_wood_frame_bed"
            self.diagnostics.append({"code": "module_style_resolution", "from_tag": tag, "to_tag": resolved_tag})
        if resolved_tag not in self.bindings:
            substitution = next((item for item in self.style.get("biome_substitution", []) if item.get("from_tag") == tag), None)
            if substitution:
                resolved_tag = substitution["to_tag"]
                self.diagnostics.append({"code": "biome_substitution", "from_tag": tag, "to_tag": resolved_tag})
        choices = self.bindings.get(resolved_tag, [])
        if component:
            choices = [choice for choice in choices if choice.get("component") == component]
        if not choices:
            raise CandidateError(f"no verified palette binding for {tag!r}" + (f" component {component!r}" if component else ""))
        return choices[0]

    @staticmethod
    def point(anchor: dict[str, Any]) -> tuple[int, int]:
        return int(anchor["x"]) + 1, int(anchor["y"]) + 1

    def paint_shell(self) -> None:
        floor_tag = self.style["vocabulary"]["floor"][0]
        wall_tag = self.style["vocabulary"]["wall"][0]
        floor = self.binding(floor_tag)
        wall = self.binding(wall_tag)
        interior = {(x, y) for y in range(1, self.height - 1) for x in range(1, self.width - 1)}
        paint_region(self.set_tile, interior, floor["source_index"]["index"], 0)
        shell = {(x, y) for x in range(self.width) for y in range(self.height)
                 if x in {0, self.width - 1} or y in {0, self.height - 1}}
        paint_region(self.set_tile, shell, wall["source_index"]["index"], 1)
        self.collision_cells = shell
        threshold = self.binding(self.style["vocabulary"]["threshold"][0])
        for transfer in self.plan.get("transfer_points", []):
            x, y = self.point(transfer["anchor"])
            self.set_tile(x, y, 1, threshold["tile_id"])

    def paint_semantics(self) -> None:
        role_ids: dict[str, int] = {}
        for terrain in self.plan.get("terrain", []):
            role = terrain["terrain_type"]
            role_ids.setdefault(role, len(role_ids) + 1)
            area = terrain["area"]
            for y in range(int(area["y"]) + 1, int(area["y"] + area["h"]) + 1):
                for x in range(int(area["x"]) + 1, int(area["x"] + area["w"]) + 1):
                    self.set_tile(x, y, 5, role_ids[role])
        for obstacle in self.plan.get("obstacles", []):
            binding = self.binding(obstacle["name"])
            area = obstacle["area"]
            cells = [(x, y) for y in range(int(area["y"]) + 1, int(area["y"] + area["h"]) + 1)
                     for x in range(int(area["x"]) + 1, int(area["x"] + area["w"]) + 1)]
            components = self.bindings.get(obstacle["name"], [])
            for index, (x, y) in enumerate(cells):
                chosen = components[min(index, len(components) - 1)] if components else binding
                self.set_tile(x, y, 2, chosen["tile_id"])
        for landmark in self.plan.get("landmark_slots", []):
            binding = self.binding(landmark["landmark_tag"])
            x, y = self.point(landmark["anchor"])
            self.set_tile(x, y, 2, binding["tile_id"])

    def build_events(self) -> list[Any]:
        events: list[Any] = [None]
        for transfer in self.plan.get("transfer_points", []):
            event_id = len(events)
            x, y = self.point(transfer["anchor"])
            identity = transfer["transfer_id"]
            comments = [
                {"code": 108, "indent": 0, "parameters": [f"Atlas generated transfer identity: {identity}"]},
                {"code": 408, "indent": 0, "parameters": [f"Placement intent: {transfer['placement_intent']}; destination unresolved by MapPlan, no transfer command authored."]},
            ]
            events.append({"id": event_id, "name": identity, "note": "Generated candidate transfer placeholder",
                           "pages": [event_page(comments, trigger=1, priority=0)], "x": x, "y": y})
        for anchor in self.plan.get("event_anchors", []):
            event_id = len(events)
            x, y = self.point(anchor["anchor"])
            identity = anchor["local_anchor_id"]
            comments = [
                {"code": 108, "indent": 0, "parameters": [f"Atlas generated event identity: {identity}"]},
                {"code": 408, "indent": 0, "parameters": [f"Trigger intent: {anchor['trigger_intent']}; no unsupported dialogue or gameplay authored."]},
            ]
            events.append({"id": event_id, "name": identity, "note": "Generated candidate event anchor",
                           "pages": [event_page(comments, trigger=0)], "x": x, "y": y})
        for x, y in sorted(self.collision_cells, key=lambda point: (point[1], point[0])):
            event_id = len(events)
            events.append({"id": event_id, "name": f"ADAPTER-COLLISION-{x}-{y}",
                           "note": "Adapter shell collision blocker; invisible and non-interactive",
                           "pages": [event_page([], trigger=0)], "x": x, "y": y})
        return events

    def blocked(self, x: int, y: int) -> bool:
        if (x, y) in self.collision_cells:
            return True
        for layer_id in (3, 2, 1, 0):
            tile = self.data[self.index(x, y, layer_id)]
            if not tile:
                continue
            flag = self.flags[tile]
            if flag & 0x10:
                continue
            return (flag & 0x0F) == 0x0F
        return True

    def audit_routes(self, events: list[Any]) -> dict[str, Any]:
        transfer_points = [self.point(item["anchor"]) for item in self.plan.get("transfer_points", [])]
        if not transfer_points:
            raise CandidateError("candidate has no transfer point to serve as route origin")
        start = transfer_points[0]
        if self.blocked(*start):
            raise CandidateError(f"transfer origin {start} is blocked")
        reached = {start}
        queue = deque([start])
        while queue:
            x, y = queue.popleft()
            for point in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                px, py = point
                if 0 <= px < self.width and 0 <= py < self.height and point not in reached and not self.blocked(px, py):
                    reached.add(point)
                    queue.append(point)
        failures = []
        for event in events[1:]:
            if event["name"].startswith("ADAPTER-COLLISION-"):
                continue
            point = (event["x"], event["y"])
            ring = {(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)}
            if point not in reached and not (ring & reached):
                failures.append(event["name"])
        for terrain in self.plan.get("terrain", []):
            area = terrain["area"]
            cells = {(x, y) for y in range(int(area["y"]) + 1, int(area["y"] + area["h"]) + 1)
                     for x in range(int(area["x"]) + 1, int(area["x"] + area["w"]) + 1)}
            if not (cells & reached):
                failures.append(terrain["terrain_id"])
        if failures:
            raise CandidateError("unreachable required interaction/zone targets: " + ", ".join(failures))
        return {"origin": list(start), "reachable_cells": len(reached), "interaction_ring_failures": [], "result": "pass"}

    def compile(self) -> tuple[dict[str, Any], dict[str, Any]]:
        self.paint_shell()
        self.paint_semantics()
        events = self.build_events()
        route_audit = self.audit_routes(events)
        payload = {
            "autoplayBgm": False, "autoplayBgs": False, "battleback1Name": "", "battleback2Name": "",
            "bgm": {"name": "", "pan": 0, "pitch": 100, "volume": 90},
            "bgs": {"name": "", "pan": 0, "pitch": 100, "volume": 90},
            "disableDashing": False, "displayName": self.plan["title"], "encounterList": [], "encounterStep": 30,
            "height": self.height, "note": f"WO-0061 candidate; source {self.plan['blueprint_id']}; palette {self.palette['tile_palette_id']}",
            "parallaxLoopX": False, "parallaxLoopY": False, "parallaxName": "", "parallaxShow": True,
            "parallaxSx": 0, "parallaxSy": 0, "scrollType": 0, "specifyBattleback": False,
            "tilesetId": int(self.palette["tileset_id"]), "width": self.width, "data": self.data, "events": events,
        }
        return payload, route_audit


def render_candidate(renderer_path: Path, source_project: Path, map_path: Path, tilesets_path: Path, output: Path) -> None:
    spec = importlib.util.spec_from_file_location("wo0060_render_map", renderer_path)
    if spec is None or spec.loader is None:
        raise CandidateError(f"cannot load renderer {renderer_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.GAME = str(source_project)
    module.render_map(str(map_path), str(tilesets_path), str(output))


def compile_candidate(args: argparse.Namespace) -> dict[str, Any]:
    ledger = load_ledger(args.target_project)
    if not map_write_allowed(ledger, args.map_id):
        raise CandidateError(skip_message(ledger, args.map_id, "mapplan_candidate_compiler"))
    plan, palette, style = load(args.map_plan), load(args.palette), load(args.style_pack)
    contact_root = args.contact_root
    findings = verify_palette(palette, style_pack=style, project_root=args.source_project, contact_root=contact_root)
    if findings:
        raise CandidateError("palette verification failed: " + "; ".join(f"{item.code}: {item.message}" for item in findings))
    tilesets_path = args.source_project / "data" / "Tilesets.json"
    tilesets = load(tilesets_path)
    tileset = tilesets[int(palette["tileset_id"])]
    compiler = CandidateCompiler(plan, palette, style, tileset["flags"])
    map_payload, route_audit = compiler.compile()
    map_path = args.target_project / "data" / f"Map{args.map_id:03d}.json"
    manifest_path = args.output_dir / "candidate.manifest.json"
    diagnostics_path = args.output_dir / "candidate.diagnostics.json"
    render_path = args.output_dir / "candidate.render.png"
    atomic_json(map_path, map_payload)
    manifest = {
        "schema_version": "0.1", "status": "generated_pending_review", "map_plan": str(args.map_plan),
        "palette": str(args.palette), "style_pack": str(args.style_pack), "candidate_map": str(map_path),
        "render": str(render_path), "promotion": "not_applied", "ownership_state": "generated",
        "round_trip_contract": "fixture_unbound_safe",
        "human_review": {"status": "pending", "decision": None, "reviewer": None, "reviewed_at": None, "notes": None},
    }
    atomic_json(diagnostics_path, {"schema_version": "0.1", "route_audit": route_audit, "errors": [], "warnings": compiler.diagnostics})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    render_candidate(args.renderer, args.source_project, map_path, tilesets_path, render_path)
    manifest["provenance"] = {
        "map_plan_sha256": sha256(args.map_plan), "palette_sha256": sha256(args.palette),
        "style_pack_sha256": sha256(args.style_pack), "candidate_map_sha256": sha256(map_path),
        "render_sha256": sha256(render_path), "tilesets_sha256": sha256(tilesets_path),
    }
    atomic_json(manifest_path, manifest)
    return {"map": map_path, "manifest": manifest_path, "diagnostics": diagnostics_path, "render": render_path,
            "route_audit": route_audit, "dimensions": [map_payload["width"], map_payload["height"]],
            "events": len(map_payload["events"]) - 1, "data_length": len(map_payload["data"])}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--map-plan", type=Path, required=True)
    value.add_argument("--palette", type=Path, required=True)
    value.add_argument("--style-pack", type=Path, required=True)
    value.add_argument("--source-project", type=Path, required=True)
    value.add_argument("--target-project", type=Path, required=True)
    value.add_argument("--map-id", type=int, required=True)
    value.add_argument("--output-dir", type=Path, required=True)
    value.add_argument("--contact-root", type=Path, required=True)
    value.add_argument("--renderer", type=Path, required=True)
    return value


def main() -> int:
    args = parser().parse_args()
    try:
        result = compile_candidate(args)
    except CandidateError as exc:
        print(f"REFUSED: {exc}")
        return 1
    print(json.dumps({key: str(value) if isinstance(value, Path) else value for key, value in result.items()}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
