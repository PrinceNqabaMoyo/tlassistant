"""Unit Tests for Grade 11 Mathematics Sprint 2 Gaps:
- Finance, Growth and Decay (NSC Paper 1 Questions 6 & 7)
- Probability & Contingency Tables (NSC Paper 1 Questions 8 & 9)
- Statistics: Summaries, Ogive Curves & Dispersion (NSC Paper 2 Questions 1 & 2)
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

from app.utils.grade11_mathematics.finance_growth_decay_generator import (
    generate as gen_finance,
    _build_compound_finance_exam,
    _build_depreciation_drill,
    _build_effective_rate_drill,
    _build_timeline_step_drill,
)
from app.utils.grade11_mathematics.probability_contingency_generator import (
    generate as gen_probability,
    _build_compound_probability_exam,
    _build_contingency_table_drill,
    _build_mutually_exclusive_drill,
    _build_independent_events_drill,
)
from app.utils.grade11_mathematics.statistics_summary_ogive_generator import (
    generate as gen_statistics,
    _build_compound_statistics_exam,
    _build_five_number_summary_drill,
    _build_iqr_outlier_drill,
    _build_skewness_analysis_drill,
)
from app.services.generator_registry import (
    get_generator_for_topic,
    resolve_generator_key,
    ALL_GENERATORS,
)


class TestGrade11FinanceGenerator(unittest.TestCase):
    """Tests for finance_growth_decay_generator."""

    def test_seed_determinism(self):
        """Pillar 1: Identical seeds produce byte-identical questions."""
        q1 = gen_finance(seed=42, mode="compound")
        q2 = gen_finance(seed=42, mode="compound")
        self.assertEqual(q1["questions"][0]["prompt"], q2["questions"][0]["prompt"])
        self.assertEqual(q1["questions"][0]["answer_latex"], q2["questions"][0]["answer_latex"])
        self.assertEqual(q1["questions"][0]["marks"], q2["questions"][0]["marks"])
        self.assertEqual(q1["questions"][0]["subskill"], q2["questions"][0]["subskill"])

    def test_compound_exam_ceiling_10_marks(self):
        """Compound exam questions must total 10 marks and cover NSC Paper 1 multi-step procedures."""
        for seed in [101, 202, 303, 404]:
            res = gen_finance(seed=seed, mode="compound")
            q = res["questions"][0]
            self.assertEqual(q["marks"], 10)
            self.assertEqual(q["marking_schema"]["total_marks"], 10)
            self.assertEqual(len(q["marking_schema"]["marking_points"]), 10)
            self.assertIn("QUESTION 1", q["prompt"])
            self.assertIn("canonical_solution", q)
            self.assertGreater(len(q["canonical_solution"]["steps"]), 3)
            # Diagram spec check
            self.assertIn("diagram_spec", q)
            self.assertEqual(q["diagram_spec"]["kind"], "timeline_finance")
            self.assertIn("events", q["diagram_spec"])

    def test_deconstructibility_subdrills(self):
        """Pillar 2: Verify all elementary scaffolding sub-drills total 3 or 4 marks."""
        subdrills = [
            ("elementary_depreciation", 3),
            ("elementary_effective_rate", 3),
            ("elementary_timeline_step", 4),
        ]
        for mode_name, expected_marks in subdrills:
            res = gen_finance(seed=777, mode=mode_name)
            q = res["questions"][0]
            self.assertEqual(q["subskill"], mode_name)
            self.assertEqual(q["marks"], expected_marks)
            self.assertEqual(q["marking_schema"]["total_marks"], expected_marks)
            self.assertEqual(len(q["marking_schema"]["marking_points"]), expected_marks)

    def test_misconception_tags_and_metadata(self):
        """Pillar 3 & 4: Validates term, caps_weight_percent, and misconception tags."""
        res = gen_finance(seed=555, mode="elementary_effective_rate")
        q = res["questions"][0]
        self.assertEqual(q["term"], 3)
        self.assertEqual(q["caps_weight_percent"], 15)
        self.assertIn("inverted_compounding_frequency", q["misconception_tags"])

    def test_3_tier_hints(self):
        """Pillar 5: Both hint_sections and 3-tier hints list must be populated."""
        res = gen_finance(seed=888, mode="elementary_timeline_step")
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

    def test_comma_decimals_in_latex(self):
        """Pillar 6: South African comma decimal convention ({,}) in LaTeX."""
        res = gen_finance(seed=123, mode="compound")
        q = res["questions"][0]
        self.assertIn(r"\%", q["answer_latex"])
        # Should not have raw unbracketed period decimals in money or percent output
        self.assertNotIn(".0", q["answer_latex"])


class TestGrade11ProbabilityGenerator(unittest.TestCase):
    """Tests for probability_contingency_generator."""

    def test_seed_determinism(self):
        """Pillar 1: Identical seeds produce byte-identical questions."""
        q1 = gen_probability(seed=42, mode="compound")
        q2 = gen_probability(seed=42, mode="compound")
        self.assertEqual(q1["questions"][0]["prompt"], q2["questions"][0]["prompt"])
        self.assertEqual(q1["questions"][0]["answer_latex"], q2["questions"][0]["answer_latex"])
        self.assertEqual(q1["questions"][0]["marks"], q2["questions"][0]["marks"])
        self.assertEqual(q1["questions"][0]["subskill"], q2["questions"][0]["subskill"])

    def test_compound_exam_ceiling_10_marks(self):
        """Compound exam questions must total 10 marks covering contingency tables and tree diagrams."""
        for seed in [101, 202, 303, 404]:
            res = gen_probability(seed=seed, mode="compound")
            q = res["questions"][0]
            self.assertEqual(q["marks"], 10)
            self.assertEqual(q["marking_schema"]["total_marks"], 10)
            self.assertEqual(len(q["marking_schema"]["marking_points"]), 10)
            self.assertIn("QUESTION 2", q["prompt"])
            self.assertIn("canonical_solution", q)
            self.assertGreaterEqual(len(q["canonical_solution"]["steps"]), 4)
            # Diagram spec must include table and tree
            self.assertIn("diagram_spec", q)
            self.assertEqual(q["diagram_spec"]["kind"], "contingency_table_and_tree")
            self.assertIn("table", q["diagram_spec"])
            self.assertIn("tree", q["diagram_spec"])

    def test_deconstructibility_subdrills(self):
        """Pillar 2: Verify all elementary scaffolding sub-drills total 3 marks."""
        subdrills = [
            ("elementary_contingency_table", 3),
            ("elementary_mutually_exclusive_test", 3),
            ("elementary_independent_events", 3),
        ]
        for mode_name, expected_marks in subdrills:
            res = gen_probability(seed=314, mode=mode_name)
            q = res["questions"][0]
            self.assertEqual(q["subskill"], mode_name)
            self.assertEqual(q["marks"], expected_marks)
            self.assertEqual(q["marking_schema"]["total_marks"], expected_marks)
            self.assertEqual(len(q["marking_schema"]["marking_points"]), expected_marks)

    def test_misconception_tags_and_metadata(self):
        """Pillar 3 & 4: Validates term, caps_weight_percent, and misconception tags."""
        res = gen_probability(seed=456, mode="elementary_independent_events")
        q = res["questions"][0]
        self.assertEqual(q["term"], 3)
        self.assertEqual(q["caps_weight_percent"], 15)
        self.assertIn("confused_mutually_exclusive_with_independent", q["misconception_tags"])

    def test_3_tier_hints(self):
        """Pillar 5: Both hint_sections and 3-tier hints list must be populated."""
        res = gen_probability(seed=999, mode="elementary_mutually_exclusive_test")
        q = res["questions"][0]
        self.assertIn("hint_sections", q)
        self.assertIn("1_nudge", q["hint_sections"])
        self.assertIn("2_concept", q["hint_sections"])
        self.assertIn("3_breakdown", q["hint_sections"])
        self.assertIn("hints", q)
        self.assertEqual(len(q["hints"]), 3)


class TestGrade11StatisticsGenerator(unittest.TestCase):
    """Tests for statistics_summary_ogive_generator."""

    def test_seed_determinism(self):
        """Pillar 1: Identical seeds produce byte-identical questions."""
        q1 = gen_statistics(seed=42, mode="compound")
        q2 = gen_statistics(seed=42, mode="compound")
        self.assertEqual(q1["questions"][0]["prompt"], q2["questions"][0]["prompt"])
        self.assertEqual(q1["questions"][0]["answer_latex"], q2["questions"][0]["answer_latex"])
        self.assertEqual(q1["questions"][0]["marks"], q2["questions"][0]["marks"])
        self.assertEqual(q1["questions"][0]["subskill"], q2["questions"][0]["subskill"])

    def test_compound_exam_ceiling_10_marks(self):
        """Compound exam questions must total 10 marks covering five-number summary, outlier test, skewness, ogive, and std dev."""
        for seed in [111, 222, 333, 444]:
            res = gen_statistics(seed=seed, mode="compound")
            q = res["questions"][0]
            self.assertEqual(q["marks"], 10)
            self.assertEqual(q["marking_schema"]["total_marks"], 10)
            self.assertEqual(len(q["marking_schema"]["marking_points"]), 10)
            self.assertIn("QUESTION 3", q["prompt"])
            self.assertIn("canonical_solution", q)
            self.assertGreaterEqual(len(q["canonical_solution"]["steps"]), 4)
            # Diagram spec must include box and ogive
            self.assertIn("diagram_spec", q)
            self.assertEqual(q["diagram_spec"]["kind"], "statistics_box_and_ogive")
            self.assertIn("box_and_whisker", q["diagram_spec"])
            self.assertIn("ogive_curve", q["diagram_spec"])

    def test_deconstructibility_subdrills(self):
        """Pillar 2: Verify all elementary scaffolding sub-drills total 3 marks."""
        subdrills = [
            ("elementary_five_number_summary", 3),
            ("elementary_iqr_outlier", 3),
            ("elementary_skewness_analysis", 3),
        ]
        for mode_name, expected_marks in subdrills:
            res = gen_statistics(seed=555, mode=mode_name)
            q = res["questions"][0]
            self.assertEqual(q["subskill"], mode_name)
            self.assertEqual(q["marks"], expected_marks)
            self.assertEqual(q["marking_schema"]["total_marks"], expected_marks)
            self.assertEqual(len(q["marking_schema"]["marking_points"]), expected_marks)

    def test_misconception_tags_and_metadata(self):
        """Pillar 3 & 4: Validates term, caps_weight_percent, and misconception tags."""
        res = gen_statistics(seed=777, mode="elementary_iqr_outlier")
        q = res["questions"][0]
        self.assertEqual(q["term"], 4)
        self.assertEqual(q["caps_weight_percent"], 15)
        self.assertIn("used_semi_iqr_instead_of_1.5_iqr", q["misconception_tags"])

    def test_3_tier_hints(self):
        """Pillar 5: Both hint_sections and 3-tier hints list must be populated."""
        res = gen_statistics(seed=888, mode="elementary_skewness_analysis")
        q = res["questions"][0]
        self.assertIn("hint_sections", q)
        self.assertIn("1_nudge", q["hint_sections"])
        self.assertIn("2_concept", q["hint_sections"])
        self.assertIn("3_breakdown", q["hint_sections"])
        self.assertIn("hints", q)
        self.assertEqual(len(q["hints"]), 3)


class TestGrade11RegistryResolution(unittest.TestCase):
    """Tests registration and topic alias resolution for Grade 11 Mathematics."""

    def test_topic_aliases_resolution(self):
        aliases = [
            ("finance growth and decay", "grade11_math_finance_growth_decay"),
            ("depreciation", "grade11_math_finance_growth_decay"),
            ("effective rate", "grade11_math_finance_growth_decay"),
            ("probability contingency", "grade11_math_probability_contingency"),
            ("contingency tables", "grade11_math_probability_contingency"),
            ("independent events", "grade11_math_probability_contingency"),
            ("statistics summary ogive", "grade11_math_statistics_summary_ogive"),
            ("five-number summary", "grade11_math_statistics_summary_ogive"),
            ("ogive", "grade11_math_statistics_summary_ogive"),
            ("box and whisker", "grade11_math_statistics_summary_ogive"),
        ]
        for human_name, expected_key in aliases:
            resolved = resolve_generator_key(human_name, grade="11", subject="Mathematics")
            self.assertEqual(resolved, expected_key, f"Failed resolving alias '{human_name}'")

    def test_direct_generation_from_registry(self):
        """Verify generation directly from registered keys in ALL_GENERATORS."""
        keys = [
            "grade11_math_finance",
            "grade11_math_finance_growth_decay",
            "grade11_math_probability",
            "grade11_math_probability_contingency",
            "grade11_math_statistics",
            "grade11_math_statistics_summary_ogive",
        ]
        for topic_key in keys:
            self.assertIn(topic_key, ALL_GENERATORS)
            gen_fn = get_generator_for_topic(topic_key)
            self.assertIsNotNone(gen_fn)
            output = gen_fn(count=1, seed=42)
            self.assertIn("questions", output)
            self.assertEqual(len(output["questions"]), 1)
            q = output["questions"][0]
            self.assertEqual(q["grade"], "grade-11")
            self.assertEqual(q["subject"], "mathematics")


if __name__ == "__main__":
    unittest.main()
