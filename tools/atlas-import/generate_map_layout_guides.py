#!/usr/bin/env python3
"""Generate SVG layout guide images from Atlas map blueprints."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BLUEPRINT_DIR = ROOT.parent / "TheLastSwordProtocol-Atlas" / "atlas-tools" / "mapgen" / "prototype"
DEFAULT_OUTPUT_DIR = ROOT / "reports" / "atlas-import" / "map-guides"
DEFAULT_REPORT = ROOT / "reports" / "atlas-import" / "build-0041-map-layout-guide-images-report.md"

TILE = 18
MARGIN = 26
RIGHT_PANEL = 275
HEADER = 56
FOOTER = 24

COLORS = {
    "background": "#f7f3e7",
    "grid": "#d8d0bd",
    "walkable": "#d9e9c8",
    "blocked": "#726658",
    "conditional": "#eddc91",
    "decorative": "#d9d2c3",
    "obstacle": "#5b4c42",
    "traversable": "#76a9e0",
    "safe": "#bde3c4",
    "encounter": "#e8a6a1",
    "event": "#d0b2e8",
    "trial": "#aac8ff",
    "cinematic": "#f4c891",
    "hazard": "#e57c73",
    "transfer": "#225ea8",
    "npc": "#2a9d8f",
    "treasure": "#c47f00",
    "anchor": "#7b2cbf",
    "text": "#241f1a",
    "muted": "#685f55",
    "path": "#8a6f47",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blueprint-dir", default=str(DEFAULT_BLUEPRINT_DIR), help="Directory containing *.blueprint.json files.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Directory for generated SVG guide images.")
    parser.add_argument("--report", default=str(DEFAULT_REPORT), help="Markdown report path.")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def shape_center(area: dict[str, Any]) -> tuple[float, float]:
    shape = area.get("shape")
    if shape == "point":
        return float(area["x"]), float(area["y"])
    if shape == "rect":
        return float(area["x"]) + float(area["w"]) / 2, float(area["y"]) + float(area["h"]) / 2
    if shape == "polyline":
        points = area.get("points", [])
        if points:
            index = len(points) // 2
            return float(points[index][0]), float(points[index][1])
    return 0.0, 0.0


def sx(x: float) -> float:
    return MARGIN + x * TILE


def sy(y: float) -> float:
    return HEADER + y * TILE


def svg_text(x: float, y: float, text: str, *, size: int = 11, weight: str = "400", color: str = COLORS["text"]) -> str:
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" fill="{color}">{esc(text)}</text>'


def svg_rect(area: dict[str, Any], color: str, *, opacity: float = 1.0, stroke: str = "none", dash: str = "") -> str:
    x = sx(float(area["x"]))
    y = sy(float(area["y"]))
    w = float(area["w"]) * TILE
    h = float(area["h"]) * TILE
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'fill="{color}" fill-opacity="{opacity}" stroke="{stroke}" stroke-width="1"{dash_attr}/>'
    )


def svg_polyline(area: dict[str, Any], color: str, *, width: int = 4, opacity: float = 1.0) -> str:
    points = " ".join(f"{sx(float(x)):.1f},{sy(float(y)):.1f}" for x, y in area.get("points", []))
    return f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"/>'


def draw_area(area: dict[str, Any], color: str, *, opacity: float = 1.0, stroke: str = "none", dash: str = "") -> list[str]:
    shape = area.get("shape")
    if shape == "rect":
        return [svg_rect(area, color, opacity=opacity, stroke=stroke, dash=dash)]
    if shape == "point":
        x, y = shape_center(area)
        return [f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="5" fill="{color}" fill-opacity="{opacity}" stroke="{stroke}" stroke-width="1"/>']
    if shape == "polyline":
        return [svg_polyline(area, color, opacity=opacity)]
    return []


def draw_marker(area: dict[str, Any], label: str, color: str, shape: str) -> list[str]:
    x, y = shape_center(area)
    px, py = sx(x), sy(y)
    label_text = label[:24]
    out: list[str] = []
    if shape == "square":
        out.append(f'<rect x="{px - 6:.1f}" y="{py - 6:.1f}" width="12" height="12" rx="1" fill="{color}" stroke="#1b1714" stroke-width="1"/>')
    elif shape == "diamond":
        points = f"{px:.1f},{py - 8:.1f} {px + 8:.1f},{py:.1f} {px:.1f},{py + 8:.1f} {px - 8:.1f},{py:.1f}"
        out.append(f'<polygon points="{points}" fill="{color}" stroke="#1b1714" stroke-width="1"/>')
    elif shape == "triangle":
        points = f"{px:.1f},{py - 8:.1f} {px + 8:.1f},{py + 7:.1f} {px - 8:.1f},{py + 7:.1f}"
        out.append(f'<polygon points="{points}" fill="{color}" stroke="#1b1714" stroke-width="1"/>')
    else:
        out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="7" fill="{color}" stroke="#1b1714" stroke-width="1"/>')
    out.append(f'<rect x="{px + 8:.1f}" y="{py - 9:.1f}" width="{max(44, len(label_text) * 6.2):.1f}" height="14" rx="2" fill="#fffaf0" fill-opacity="0.86"/>')
    out.append(svg_text(px + 11, py + 2, label_text, size=10, color=COLORS["text"]))
    return out


def movement_color(movement: str) -> str:
    return COLORS.get(movement, COLORS["decorative"])


def region_color(region_type: str) -> str:
    return COLORS.get(region_type, COLORS["event"])


def guide_filename(blueprint: dict[str, Any]) -> str:
    return f"{blueprint['atlas_screen_id']}-layout-guide.svg"


def render_guide(blueprint: dict[str, Any]) -> str:
    width_tiles = int(blueprint["dimensions"]["width"])
    height_tiles = int(blueprint["dimensions"]["height"])
    map_w = width_tiles * TILE
    map_h = height_tiles * TILE
    svg_w = MARGIN * 2 + map_w + RIGHT_PANEL
    svg_h = HEADER + map_h + FOOTER
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}">',
        '<rect width="100%" height="100%" fill="#fbf8ef"/>',
        svg_text(MARGIN, 26, f"{blueprint['atlas_screen_id']} - {blueprint['title']}", size=18, weight="700"),
        svg_text(MARGIN, 44, blueprint.get("map_intent", {}).get("critical_path_role", "layout guide"), size=11, color=COLORS["muted"]),
        f'<rect x="{MARGIN}" y="{HEADER}" width="{map_w}" height="{map_h}" fill="{COLORS["background"]}" stroke="#332b25" stroke-width="2"/>',
    ]

    for x in range(width_tiles + 1):
        out.append(f'<line x1="{sx(x):.1f}" y1="{HEADER}" x2="{sx(x):.1f}" y2="{HEADER + map_h}" stroke="{COLORS["grid"]}" stroke-width="0.5"/>')
    for y in range(height_tiles + 1):
        out.append(f'<line x1="{MARGIN}" y1="{sy(y):.1f}" x2="{MARGIN + map_w}" y2="{sy(y):.1f}" stroke="{COLORS["grid"]}" stroke-width="0.5"/>')

    for terrain in blueprint.get("terrain", []):
        area = terrain.get("area", {})
        movement = str(terrain.get("movement", "decorative"))
        opacity = 0.58 if movement != "blocked" else 0.72
        out.extend(draw_area(area, movement_color(movement), opacity=opacity, stroke="#6c6258" if movement == "blocked" else "none"))

    for traversable in blueprint.get("traversable_areas", []):
        out.extend(draw_area(traversable.get("area", {}), COLORS["traversable"], opacity=0.14, stroke=COLORS["traversable"], dash="4 3"))

    for region in blueprint.get("enemy_regions", []):
        area = region.get("area", {})
        color = region_color(str(region.get("region_type", "event")))
        out.extend(draw_area(area, color, opacity=0.24, stroke=color, dash="5 4"))

    for obstacle in blueprint.get("obstacles", []):
        if obstacle.get("blocking"):
            out.extend(draw_area(obstacle.get("area", {}), COLORS["obstacle"], opacity=0.82, stroke="#2b241f"))

    for terrain in blueprint.get("terrain", []):
        if terrain.get("area", {}).get("shape") == "polyline":
            out.extend(draw_area(terrain["area"], COLORS["path"], opacity=0.92))

    for transfer in blueprint.get("transfer_points", []):
        out.extend(draw_marker(transfer.get("anchor", {}), transfer.get("transfer_id", "TRN"), COLORS["transfer"], "triangle"))
    for npc in blueprint.get("npc_spawns", []):
        out.extend(draw_marker(npc.get("anchor", {}), npc.get("event_id") or npc.get("local_anchor_id") or npc.get("npc_role", "NPC"), COLORS["npc"], "circle"))
    for treasure in blueprint.get("treasure_locations", []):
        out.extend(draw_marker(treasure.get("anchor", {}), treasure.get("event_id") or treasure.get("object_id") or "Treasure", COLORS["treasure"], "square"))
    for anchor in blueprint.get("event_anchors", []):
        out.extend(draw_marker(anchor.get("anchor", {}), anchor.get("event_id") or anchor.get("local_anchor_id") or "Event", COLORS["anchor"], "diamond"))

    panel_x = MARGIN + map_w + 28
    panel_y = HEADER
    out.append(svg_text(panel_x, panel_y + 4, "Legend", size=16, weight="700"))
    legend = [
        ("Walkable", COLORS["walkable"], "rect"),
        ("Blocked", COLORS["blocked"], "rect"),
        ("Conditional", COLORS["conditional"], "rect"),
        ("Traversable zone", COLORS["traversable"], "outline"),
        ("Encounter / special region", COLORS["encounter"], "outline"),
        ("Transfer", COLORS["transfer"], "triangle"),
        ("NPC", COLORS["npc"], "circle"),
        ("Treasure", COLORS["treasure"], "square"),
        ("Event anchor", COLORS["anchor"], "diamond"),
    ]
    y = panel_y + 28
    for label, color, marker in legend:
        if marker == "rect":
            out.append(f'<rect x="{panel_x}" y="{y - 11}" width="14" height="14" fill="{color}" stroke="#1b1714" stroke-width="1"/>')
        elif marker == "outline":
            out.append(f'<rect x="{panel_x}" y="{y - 11}" width="14" height="14" fill="{color}" fill-opacity="0.25" stroke="{color}" stroke-width="2" stroke-dasharray="3 2"/>')
        elif marker == "triangle":
            out.append(f'<polygon points="{panel_x + 7},{y - 13} {panel_x + 15},{y + 1} {panel_x - 1},{y + 1}" fill="{color}" stroke="#1b1714" stroke-width="1"/>')
        elif marker == "square":
            out.append(f'<rect x="{panel_x + 1}" y="{y - 12}" width="13" height="13" fill="{color}" stroke="#1b1714" stroke-width="1"/>')
        elif marker == "diamond":
            out.append(f'<polygon points="{panel_x + 7},{y - 14} {panel_x + 15},{y - 6} {panel_x + 7},{y + 2} {panel_x - 1},{y - 6}" fill="{color}" stroke="#1b1714" stroke-width="1"/>')
        else:
            out.append(f'<circle cx="{panel_x + 7}" cy="{y - 5}" r="7" fill="{color}" stroke="#1b1714" stroke-width="1"/>')
        out.append(svg_text(panel_x + 24, y, label, size=11))
        y += 22

    intent = blueprint.get("map_intent", {}).get("purpose", "")
    biome = blueprint.get("biome", {}).get("visual_tone", "")
    out.append(svg_text(panel_x, y + 14, "Intent", size=14, weight="700"))
    for line in wrap_text(intent, 37)[:4]:
        y += 18
        out.append(svg_text(panel_x, y + 14, line, size=10, color=COLORS["muted"]))
    out.append(svg_text(panel_x, y + 42, "Visual Tone", size=14, weight="700"))
    y += 46
    for line in wrap_text(biome, 37)[:4]:
        y += 14
        out.append(svg_text(panel_x, y, line, size=10, color=COLORS["muted"]))

    out.append(svg_text(MARGIN, svg_h - 8, f"Generated from {blueprint['blueprint_id']} - guide only, not final art", size=10, color=COLORS["muted"]))
    out.append("</svg>")
    return "\n".join(out) + "\n"


def wrap_text(text: str, width: int) -> list[str]:
    words = str(text).split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        if sum(len(item) + 1 for item in current) + len(word) > width and current:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines


def build_report(output_dir: Path, generated: list[tuple[str, str, str]]) -> str:
    lines = [
        "# BUILD-0041 - Atlas Map Layout Guide Images Report",
        "",
        "## Objective",
        "",
        "Generate visual guide images from Atlas Home Island map blueprints.",
        "",
        "## Output",
        "",
        f"- Guide directory: `{output_dir}`",
        f"- Guide images generated: {len(generated)}",
        "- Format: SVG, one image per blueprint",
        "",
        "## Guide Contents",
        "",
        "- terrain movement categories",
        "- blocked obstacles",
        "- traversable zones",
        "- encounter/special regions",
        "- transfer markers",
        "- NPC markers",
        "- treasure markers",
        "- event anchor markers",
        "- legend and map intent notes",
        "",
        "## Generated Guides",
        "",
    ]
    for screen_id, title, file_name in generated:
        lines.append(f"- `{screen_id}` - {title}: `reports/atlas-import/map-guides/{file_name}`")
    lines.extend([
        "",
        "## Notes",
        "",
        "- These are guide images, not final art.",
        "- RPG Maker project data was not modified by BUILD-0041.",
        "- Atlas IDs remain visible where they help trace markers back to canonical specs.",
    ])
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    blueprint_dir = Path(args.blueprint_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    report_path = Path(args.report).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    generated: list[tuple[str, str, str]] = []
    for path in sorted(blueprint_dir.glob("*.blueprint.json")):
        blueprint = load_json(path)
        file_name = guide_filename(blueprint)
        (output_dir / file_name).write_text(render_guide(blueprint), encoding="utf-8")
        generated.append((blueprint["atlas_screen_id"], blueprint["title"], file_name))

    report_path.write_text(build_report(output_dir, generated), encoding="utf-8")
    print(f"blueprint_dir={blueprint_dir}")
    print(f"output_dir={output_dir}")
    print(f"guides_generated={len(generated)}")
    print(f"report={report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
