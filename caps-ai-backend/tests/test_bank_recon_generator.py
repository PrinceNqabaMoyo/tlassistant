from __future__ import annotations

import random
import sys
import unittest
from pathlib import Path

# Add backend directory to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.utils.grade10_accounting.term2.bank_reconciliation_generator import (
    generate_questions as gen_bank_recon,
    MISCONCEPTION_DEBIT_CREDIT_INVERSION,
    MISCONCEPTION_TIMING_VS_ERROR_CONFUSION,
)
from app.services.generator_registry import generate_variant, ALL_GENERATORS


class TestBankReconciliationGenerator(unittest.TestCase):
    """Test suite for CAPS Grade 10 Accounting Term 2 Bank Reconciliation generator."""

    def test_seed_determinism(self):
        """Pillar 1/2: Validates seed invariance and reproducibility."""
        r1 = random.Random(42)
        r2 = random.Random(42)

        q1 = gen_bank_recon(r=r1, n=1, mode="scaffold", seed=42)
        q2 = gen_bank_recon(r=r2, n=1, mode="scaffold", seed=42)

        self.assertEqual(len(q1), 1)
        self.assertEqual(len(q2), 1)
        self.assertEqual(q1[0]["prompt"], q2[0]["prompt"])
        self.assertEqual(q1[0]["correct_map"], q2[0]["correct_map"])
        self.assertEqual(q1[0]["headers"], q2[0]["headers"])

    def test_six_pillar_contract_compliance(self):
        """Validates all 6 pillars of the Generator Architecture Contract."""
        r = random.Random(100)
        questions = gen_bank_recon(r=r, n=1, mode="scaffold", seed=100)
        self.assertTrue(len(questions) > 0)
        q = questions[0]

        # Pillar 1: Calendar & Pacing Metadata
        self.assertEqual(q.get("term"), 2)
        self.assertEqual(q.get("caps_weight_percent"), 20)
        self.assertGreaterEqual(q.get("suggested_duration_mins", 0), 5)
        self.assertEqual(q.get("learning_objective_id"), "acct_g10_t2_bank_reconciliation")

        # Pillar 3: Standardized Misconceptions
        self.assertIn("misconception_tags", q)
        self.assertIn(MISCONCEPTION_DEBIT_CREDIT_INVERSION, q["misconception_tags"])
        self.assertIn(MISCONCEPTION_TIMING_VS_ERROR_CONFUSION, q["misconception_tags"])

        # Pillar 4: Teacher-Editable Marking Schema
        self.assertIn("marking_schema", q)
        schema = q["marking_schema"]
        self.assertIn("total_marks", schema)
        self.assertIn("marking_points", schema)
        self.assertIn("deductions", schema)
        self.assertEqual(schema.get("carry_forward_rule"), "consequential_accuracy")
        self.assertTrue(all(mp.get("editable") for mp in schema["marking_points"]))

        # Pillar 5: 3-Tier Pre-baked Hints
        self.assertIn("hint_sections", q)
        self.assertIn("tier1_location", q["hint_sections"])
        self.assertIn("tier2_directional_rule", q["hint_sections"])
        self.assertIn("tier3_worked_step", q["hint_sections"])
        self.assertIn("cell_hints", q)
        self.assertGreater(len(q["cell_hints"]), 0)

        # Pillar 6: Native Tabular Modality
        self.assertEqual(q.get("question_type"), "table_completion")
        self.assertIn("headers", q)
        self.assertIn("rows", q)
        self.assertIn("correct_map", q)
        # Check cell coordinates
        sample_cell = q["rows"][0][0]
        self.assertIn("coordinate", sample_cell)
        self.assertTrue(sample_cell["coordinate"].startswith("t0_r0_c0"))

    def test_deconstructibility_elementary_journals_mode(self):
        """Pillar 2: Elementary atomic sub-drill for CRJ and CPJ supplementary updates."""
        r = random.Random(200)
        questions = gen_bank_recon(r=r, n=1, subskill="crj_cpj", mode="elementary_crj_cpj_supplementary", seed=200)
        self.assertEqual(len(questions), 1)
        q = questions[0]
        self.assertEqual(q.get("term"), 2)
        self.assertIn("CRJ", q["prompt"])
        self.assertIn("CPJ", q["prompt"])
        self.assertIn("t0_r0_c3", q["correct_map"])
        self.assertIn("t0_r1_c3", q["correct_map"])

    def test_deconstructibility_elementary_classification_mode(self):
        """Pillar 2: Elementary atomic sub-drill for timing difference vs journal adjustment classification."""
        r = random.Random(300)
        questions = gen_bank_recon(r=r, n=1, subskill="classification", mode="elementary_outstanding_items", seed=300)
        self.assertEqual(len(questions), 1)
        q = questions[0]
        self.assertIn("Classification", q["headers"])
        self.assertTrue(any(coord.endswith("_c1") for coord in q["correct_map"].keys()))

    def test_generator_registry_integration(self):
        """Validates generator registration in ALL_GENERATORS and generate_variant."""
        self.assertIn("grade10_accounting_bank_reconciliation", ALL_GENERATORS)

        res = generate_variant(
            topic="grade10_accounting_bank_reconciliation",
            subskill="concepts",
            difficulty="medium",
            count=1,
            seed=555,
        )
        self.assertIsInstance(res, list)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["term"], 2)
        self.assertEqual(res[0]["subject"], "Accounting")


if __name__ == "__main__":
    unittest.main()
