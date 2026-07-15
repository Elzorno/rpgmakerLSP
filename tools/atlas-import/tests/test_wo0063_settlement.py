from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve()
REPO = HERE.parents[3]
GENERATOR = REPO / "tools/atlas-import/generate_wo0063_settlement.py"
OUTPUT = REPO / "reports/atlas-import/wo0063"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


spec = importlib.util.spec_from_file_location("wo0063_settlement", GENERATOR)
generator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(generator)


class SettlementVerticalSliceTests(unittest.TestCase):
    def test_semantic_plan_has_required_settlement_parts(self) -> None:
        plan = generator.build_plan(6301)
        roles = {item["terrain_type"] for item in plan["terrain"]}
        obstacle_names = {item["name"] for item in plan["obstacles"]}
        anchors = {item["local_anchor_id"] for item in plan["event_anchors"]}
        self.assertTrue({"entry_threshold", "civic_spine", "landmark_plaza", "shop_plot", "inn_plot", "house_plot", "curiosity_garden"} <= roles)
        self.assertEqual({"building_shop", "building_inn", "building_house"}, obstacle_names)
        self.assertTrue({"DOOR-SHOP", "DOOR-INN", "DOOR-HOUSE", "CURIOSITY-GARDEN"} <= anchors)
        self.assertEqual("civic_well_landmark", plan["landmark_slots"][0]["landmark_tag"])
        self.assertEqual("primary_landmark", plan["validation"]["assembly_order"][0])

    def test_same_seed_preserves_semantics_across_biomes(self) -> None:
        self.assertEqual(generator.build_plan(6302), generator.build_plan(6302))
        temperate = load(OUTPUT / "candidates/temperate-seed-6302/settlement.map_plan.json")
        coastal = load(OUTPUT / "candidates/coastal-seed-6302/settlement.map_plan.json")
        self.assertEqual(temperate, coastal)

    def test_gallery_contains_six_disposable_hard_pass_candidates(self) -> None:
        index = load(OUTPUT / "index.json")
        self.assertEqual(6, index["candidate_count"])
        self.assertTrue(all(item["hard_passed"] for item in index["candidates"]))
        self.assertTrue(all(item["promotion"] == "not_applied" for item in index["candidates"]))
        for item in index["candidates"]:
            root = OUTPUT / "candidates" / item["candidate_id"]
            ownership = load(root / "fixture-project/map_ownership.json")
            diagnostics = load(root / "candidate.diagnostics.json")
            manifest = load(root / "candidate.manifest.json")
            self.assertEqual("generated", ownership["maps"]["1"]["state"])
            self.assertEqual("pass", diagnostics["route_audit"]["result"])
            self.assertEqual([], diagnostics["route_audit"]["interaction_ring_failures"])
            self.assertEqual("pending", manifest["human_review"]["status"])
            self.assertTrue((root / "settlement.structural.txt").is_file())
            self.assertTrue((root / "settlement.structural.svg").is_file())

    def test_candidate_retains_all_semantic_event_identities(self) -> None:
        root = OUTPUT / "candidates/temperate-seed-6301"
        plan = load(root / "settlement.map_plan.json")
        candidate = load(root / "fixture-project/data/Map001.json")
        expected = {item["transfer_id"] for item in plan["transfer_points"]} | {item["local_anchor_id"] for item in plan["event_anchors"]}
        actual = {item["name"] for item in candidate["events"] if item}
        self.assertTrue(expected <= actual)


if __name__ == "__main__":
    unittest.main()
