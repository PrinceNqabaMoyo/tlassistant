"""
Unit Tests for Grade 10 Mathematics Term 2 Analytical Geometry Generator
Verifies compliance with the 6-pillar universal generator contract.
"""

import unittest
from app.utils.grade10_mathematics.term_2.analytical_geometry_generator import (
    generate_analytical_geometry_question
)


class TestAnalyticalGeometryGenerator(unittest.TestCase):
    def test_seed_determinism(self):
        """Verify identical seeds produce byte-identical questions."""
        q1 = generate_analytical_geometry_question(seed=12345, mode="compound")
        q2 = generate_analytical_geometry_question(seed=12345, mode="compound")
        self.assertEqual(q1["prompt"], q2["prompt"])
        self.assertEqual(q1["answer_latex"], q2["answer_latex"])
        self.assertEqual(q1["subskill"], q2["subskill"])

    def test_deconstructibility_modes(self):
        """Verify all atomic sub-drills can be deconstructed independently."""
        modes = [
            ("elementary_distance", "distance_formula"),
            ("elementary_midpoint", "midpoint_formula"),
            ("elementary_gradient", "gradient_formula"),
            ("elementary_parallel_perpendicular", "parallel_perpendicular")
        ]
        for mode, expected_subskill in modes:
            q = generate_analytical_geometry_question(seed=999, mode=mode)
            self.assertEqual(q["subskill"], expected_subskill)
            self.assertIn("prompt", q)
            self.assertGreater(len(q["hints"]), 0)

    def test_pillar1_term_metadata(self):
        """Pillar 1: Term & Calendar Metadata."""
        q = generate_analytical_geometry_question(seed=42)
        self.assertEqual(q["term"], 2)
        self.assertEqual(q["caps_weight_percent"], 15)
        self.assertGreaterEqual(q["suggested_duration_mins"], 2)

    def test_pillar3_misconception_taxonomy(self):
        """Pillar 3: Standardized Misconception Tags."""
        q = generate_analytical_geometry_question(seed=777, mode="elementary_distance")
        self.assertIn("forgot_square_root", q["misconception_tags"])

        q_grad = generate_analytical_geometry_question(seed=888, mode="elementary_gradient")
        self.assertIn("inversion_dx_dy", q_grad["misconception_tags"])

    def test_pillar4_marking_schema(self):
        """Pillar 4: Teacher-Editable Marking Schema."""
        q = generate_analytical_geometry_question(seed=101, mode="elementary_distance")
        schema = q["marking_schema"]
        self.assertIn("total_marks", schema)
        self.assertIn("marking_points", schema)
        self.assertGreater(len(schema["marking_points"]), 0)
        self.assertTrue(schema["marking_points"][0]["editable"])

    def test_pillar5_three_tier_hints(self):
        """Pillar 5: Deterministic 3-Tier Pre-baked Hints."""
        q = generate_analytical_geometry_question(seed=202, mode="elementary_midpoint")
        hints = q["hints"]
        self.assertEqual(len(hints), 3)
        self.assertEqual(hints[0]["tier"], 1)
        self.assertEqual(hints[1]["tier"], 2)
        self.assertEqual(hints[2]["tier"], 3)


if __name__ == "__main__":
    unittest.main()
