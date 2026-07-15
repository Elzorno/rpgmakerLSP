from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


HERE = Path(__file__).resolve()
IMPORT_ROOT = HERE.parents[1]
REPO = HERE.parents[3]
WORKSPACE = REPO.parent
STUDIO = WORKSPACE / "AtlasStudio"
sys.path.insert(0, str(STUDIO / "atlas-tools/mapgen/compiler"))
from quality_auditor import QualityAuditor  # noqa: E402


REPORT = REPO / "reports/atlas-import/wo0061/temperate"
PLAN_PATH = STUDIO / "atlas-tools/mapgen/compiler/prototypes/wo0059/shop-compact-seed-1.map_plan.json"
PALETTE_PATH = IMPORT_ROOT / "tile-palettes/temperate-village-interior.palette.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class QualityGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.plan = load(PLAN_PATH)
        cls.map_json = load(REPORT / "fixture-project/data/Map001.json")
        cls.manifest = load(REPORT / "candidate.manifest.json")
        cls.diagnostics = load(REPORT / "candidate.diagnostics.json")
        cls.palette = load(PALETTE_PATH)
        cls.auditor = QualityAuditor()

    def audit(self, plan=None, map_json=None, manifest=None, diagnostics=None):
        return self.auditor.audit_generated_candidate(
            plan=plan or copy.deepcopy(self.plan), map_json=map_json or copy.deepcopy(self.map_json),
            manifest=manifest or copy.deepcopy(self.manifest), diagnostics=diagnostics or copy.deepcopy(self.diagnostics),
            palette=copy.deepcopy(self.palette),
        )

    def test_known_good_candidate_passes_hard_gates(self) -> None:
        result = self.audit()
        self.assertTrue(result["hard_passed"], result["hard_findings"])
        self.assertGreaterEqual(result["advisory"]["score"], 70)
        self.assertEqual("not_applied", result["promotion"])

    def test_every_negative_control_fails_for_intended_reason(self) -> None:
        suite = load(IMPORT_ROOT / "wo0062-negative-controls.json")
        for control in suite["controls"]:
            with self.subTest(control=control["id"]):
                plan, map_json = copy.deepcopy(self.plan), copy.deepcopy(self.map_json)
                manifest, diagnostics = copy.deepcopy(self.manifest), copy.deepcopy(self.diagnostics)
                name = control["id"]
                if name == "reachability": diagnostics["route_audit"]["result"] = "fail"
                elif name == "interaction_ring": diagnostics["route_audit"]["interaction_ring_failures"] = ["anchor"]
                elif name == "isolated_pockets": diagnostics["route_audit"]["reachable_cells"] = 0
                elif name == "connector_alignment": plan["traversable_areas"][0]["to_zone"] = "missing-zone"
                elif name == "clearance": plan["obstacles"][0]["area"]["x"] = 999
                elif name == "transfer_round_trip": manifest["round_trip_contract"] = "unknown"
                elif name == "event_anchor": map_json["events"][2]["name"] = "lost-anchor"
                elif name == "rpgmaker_shape": map_json["data"].pop()
                elif name == "tile_family": map_json["data"][0] = 999
                elif name == "manifest_completeness": del manifest["provenance"]["render_sha256"]
                result = self.audit(plan, map_json, manifest, diagnostics)
                codes = {item["code"] for item in result["hard_findings"]}
                self.assertIn(control["expected_code"], codes)

    def test_human_rejection_is_independent_of_passing_score(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["human_review"] = {"status": "recorded", "decision": "rejected", "reviewer": "Chris", "reviewed_at": "2026-07-13", "notes": "visual rejection"}
        result = self.audit(manifest=manifest)
        self.assertTrue(result["hard_passed"])
        self.assertEqual("rejected", result["human_review"]["decision"])
        self.assertEqual("not_applied", result["promotion"])

    def test_advisory_score_cannot_bypass_hard_failure(self) -> None:
        diagnostics = copy.deepcopy(self.diagnostics)
        diagnostics["route_audit"]["result"] = "fail"
        result = self.audit(diagnostics=diagnostics)
        self.assertFalse(result["hard_passed"])
        self.assertGreaterEqual(result["advisory"]["score"], 70)

    def test_classic_jrpg_checks_are_falsifiable(self) -> None:
        plan = copy.deepcopy(self.plan)
        plan["landmark_slots"] = []
        plan["obstacles"] = []
        plan["traversable_areas"] = []
        result = self.audit(plan=plan)
        checks = result["advisory"]["checks"]
        self.assertFalse(checks["dominant_landmark"])
        self.assertFalse(checks["compact_meaningful_travel"])
        self.assertFalse(checks["curiosity_hook"])
        self.assertFalse(checks["compression_release"])
        self.assertFalse(checks["selective_density"])


if __name__ == "__main__":
    unittest.main()
