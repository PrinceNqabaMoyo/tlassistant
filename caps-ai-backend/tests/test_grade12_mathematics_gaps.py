"""Unit Tests for Grade 12 Mathematics Sprint 1 Gaps:
- Counting Principles & Probability (NSC Paper 1 Questions 10 & 11)
- Bivariate Statistics & Regression (NSC Paper 2 Question 1)
Verifies full compliance with the 6-Pillar Universal Generator Contract,
SymPy determinism, South African comma decimals, JSXGraph diagram specs,
and registry resolution.
"""

import sys
import unittest
from pathlib import Path

# Add backend directory to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.utils.grade12_mathematics.counting_principles_probability_generator import (
    generate as gen_probability,
    _build_compound_seating_venn,
    _build_compound_digits_independence,
    _build_factorial_calc,
    _build_grouping_restriction,
    _build_independence_test,
)
from app.utils.grade12_mathematics.bivariate_statistics_generator import (
    generate as gen_statistics,
    _build_compound_bivariate_statistics,
    _build_mean_points,
    _build_correlation_interpretation,
    classify_correlation,
)
from app.services.generator_registry import (
    get_generator_for_topic,
    resolve_generator_key,
    ALL_GENERATORS,
)


class TestGrade12CountingProbabilityGenerator(unittest.TestCase):
    """Tests for counting_principles_probability_generator."""

    def test_seed_determinism(self):
        """Pillar 1: Identical seeds produce byte-identical questions."""
        q1 = gen_probability(seed=42, mode="compound")
        q2 = gen_probability(seed=42, mode="compound")
        self.assertEqual(q1["questions"][0]["prompt"], q2["questions"][0]["prompt"])
        self.assertEqual(q1["questions"][0]["answer_latex"], q2["questions"][0]["answer_latex"])
        self.assertEqual(q1["questions"][0]["marks"], q2["questions"][0]["marks"])
        self.assertEqual(q1["questions"][0]["subskill"], q2["questions"][0]["subskill"])

    def test_compound_exam_ceiling_10_marks(self):
        """Compound exam questions must total 10 marks and cover NSC Paper 1 multi-step procedures."""
        for seed in [101, 202, 303, 404]:
            res = gen_probability(seed=seed, mode="compound")
            q = res["questions"][0]
            self.assertEqual(q["marks"], 10)
            self.assertEqual(q["marking_schema"]["total_marks"], 10)
            self.assertEqual(len(q["marking_schema"]["marking_points"]), 10)
            self.assertIn("QUESTION", q["prompt"])
            self.assertIn("canonical_solution", q)
            self.assertGreater(len(q["canonical_solution"]["steps"]), 3)

    def test_seating_venn_variation_diagram_spec(self):
        """Seating arrangements + Venn diagram variation must include JSXGraph venn_3_sets spec."""
        res = gen_probability(seed=101, mode="compound_seating_venn")
        q = res["questions"][0]
        self.assertEqual(q["marks"], 10)
        self.assertIn("diagram_spec", q)
        spec = q["diagram_spec"]
        self.assertEqual(spec["kind"], "venn_3_sets")
        self.assertIn("labels", spec)
        self.assertIn("only_R", spec["labels"])
        self.assertIn("all_three", spec["labels"])

    def test_deconstructibility_subdrills_3_marks(self):
        """Pillar 2: Verify all elementary scaffolding sub-drills total 3 marks."""
        subdrills = [
            ("elementary_factorial_calc", 3),
            ("elementary_grouping_restriction", 3),
            ("elementary_independence_test", 3),
        ]
        for mode_name, expected_marks in subdrills:
            res = gen_probability(seed=777, mode=mode_name)
            q = res["questions"][0]
            self.assertEqual(q["subskill"], mode_name)
            self.assertEqual(q["marks"], expected_marks)
            self.assertEqual(q["marking_schema"]["total_marks"], expected_marks)
            self.assertEqual(len(q["marking_schema"]["marking_points"]), expected_marks)

    def test_misconception_tags_and_metadata(self):
        """Pillar 3 & 4: Validates term, caps_weight_percent, and misconception tags."""
        res = gen_probability(seed=555, mode="elementary_independence_test")
        q = res["questions"][0]
        self.assertEqual(q["term"], 3)
        self.assertEqual(q["caps_weight_percent"], 15)
        self.assertIn("confused_mutually_exclusive_with_independent", q["misconception_tags"])

    def test_3_tier_hints(self):
        """Pillar 5: Both hint_sections and 3-tier hints list must be populated."""
        res = gen_probability(seed=888, mode="elementary_grouping_restriction")
        q = res["questions"][0]
        self.assertIn("hint_sections", q)
        self.assertIn("1_nudge", q["hint_sections"])
        self.assertIn("2_concept", q["hint_sections"])
        self.assertIn("3_breakdown", q["hint_sections"])
        self.assertIn("hints", q)
        self.assertEqual(len(q["hints"]), 3)
        self.assertEqual(q["hints"][0]["tier"], 1)
        self.assertEqual(q["hints"][1]["tier"], 2)
        self.assertEqual(q["hints"][2]["tier"], 3)


class TestGrade12BivariateStatisticsGenerator(unittest.TestCase):
    """Tests for bivariate_statistics_generator."""

    def test_seed_determinism(self):
        """Pillar 1: Identical seeds produce byte-identical questions."""
        q1 = gen_statistics(seed=99, mode="compound")
        q2 = gen_statistics(seed=99, mode="compound")
        self.assertEqual(q1["questions"][0]["prompt"], q2["questions"][0]["prompt"])
        self.assertEqual(q1["questions"][0]["answer_latex"], q2["questions"][0]["answer_latex"])
        self.assertEqual(q1["questions"][0]["marks"], q2["questions"][0]["marks"])
        self.assertEqual(q1["questions"][0]["subskill"], q2["questions"][0]["subskill"])

    def test_compound_exam_ceiling_8_marks(self):
        """Compound exam questions must total 8 marks with regression, correlation, prediction, and outlier."""
        for seed in [12, 34, 56, 78]:
            res = gen_statistics(seed=seed, mode="compound")
            q = res["questions"][0]
            self.assertEqual(q["marks"], 8)
            self.assertEqual(q["marking_schema"]["total_marks"], 8)
            self.assertEqual(len(q["marking_schema"]["marking_points"]), 8)
            self.assertIn("1.1", q["prompt"])
            self.assertIn("1.2", q["prompt"])
            self.assertIn("1.3", q["prompt"])
            self.assertIn("1.4", q["prompt"])
            # Diagram spec must be present with scatter plot and regression line
            self.assertIn("diagram_spec", q)
            spec = q["diagram_spec"]
            self.assertEqual(spec["kind"], "scatter_plot_regression")
            self.assertIn("points", spec)
            self.assertIn("outlier", spec)
            self.assertIn("centroid", spec)
            self.assertIn("regression_line", spec)

    def test_deconstructibility_subdrills_3_marks(self):
        """Pillar 2: Scaffolding sub-drills total 3 marks."""
        subdrills = [
            ("elementary_mean_points", 3),
            ("elementary_correlation_interpretation", 3),
        ]
        for mode_name, expected_marks in subdrills:
            res = gen_statistics(seed=314, mode=mode_name)
            q = res["questions"][0]
            self.assertEqual(q["subskill"], mode_name)
            self.assertEqual(q["marks"], expected_marks)
            self.assertEqual(q["marking_schema"]["total_marks"], expected_marks)
            self.assertEqual(len(q["marking_schema"]["marking_points"]), expected_marks)

    def test_correlation_classification(self):
        """Verifies strict CAPS correlation classification bands."""
        self.assertEqual(classify_correlation(0.95), ("positive", "very strong", "very strong positive correlation"))
        self.assertEqual(classify_correlation(0.82), ("positive", "strong", "strong positive correlation"))
        self.assertEqual(classify_correlation(0.60), ("positive", "moderate", "moderate positive correlation"))
        self.assertEqual(classify_correlation(0.35), ("positive", "weak", "weak positive correlation"))
        self.assertEqual(classify_correlation(-0.85), ("negative", "strong", "strong negative correlation"))
        self.assertEqual(classify_correlation(-0.95), ("negative", "very strong", "very strong negative correlation"))

    def test_comma_decimals_in_latex(self):
        """Pillar 6: South African comma decimal convention ({,}) in LaTeX."""
        res = gen_statistics(seed=123, mode="compound")
        q = res["questions"][0]
        # In LaTeX, decimals should use {,}
        self.assertIn(r"\hat{y}", q["answer_latex"])
        # Should not have raw un-bracketed period decimals in latex string
        ans_latex = q["answer_latex"]
        self.assertNotIn(".0", ans_latex)


class TestRegistryResolution(unittest.TestCase):
    """Tests registration and topic alias resolution."""

    def test_topic_aliases_resolution(self):
        aliases = [
            ("counting principles", "grade12_math_counting_probability"),
            ("fundamental counting principle", "grade12_math_counting_probability"),
            ("probability", "grade12_math_counting_probability"),
            ("venn diagrams", "grade12_math_counting_probability"),
            ("bivariate statistics", "grade12_math_bivariate_statistics"),
            ("statistics", "grade12_math_bivariate_statistics"),
            ("regression", "grade12_math_bivariate_statistics"),
            ("least squares regression", "grade12_math_bivariate_statistics"),
            ("correlation coefficient", "grade12_math_bivariate_statistics"),
        ]
        for human_name, expected_key in aliases:
            resolved = resolve_generator_key(human_name, grade="12", subject="Mathematics")
            self.assertEqual(resolved, expected_key, f"Failed resolving alias '{human_name}'")

    def test_direct_generation_from_registry(self):
        for topic_key in ["grade12_math_counting_probability", "grade12_math_bivariate_statistics"]:
            self.assertIn(topic_key, ALL_GENERATORS)
            gen_fn = get_generator_for_topic(topic_key)
            self.assertIsNotNone(gen_fn)
            output = gen_fn(count=1, seed=42)
            self.assertIn("questions", output)
            self.assertEqual(len(output["questions"]), 1)


if __name__ == "__main__":
    unittest.main()
