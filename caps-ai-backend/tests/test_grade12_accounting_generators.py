"""Grade 12 Accounting Comprehensive Test Suite.
Validates Cash Flow Statement Generator and Financial Indicators Generator
against the official CAPS NSC Paper 1 exam ceiling, 2D tabular schema, cell typing,
deduction rules, misconception tags, adaptive scaffolding sub-drills, and registry routing.
"""
from __future__ import annotations

from pathlib import Path
import sys
import unittest

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.services.generator_registry import generate_variant, resolve_generator_key
from app.utils.grade12_accounting.cash_flow_statement_generator import (
    generate as gen_cfs,
    generate_questions as gen_cfs_questions,
)
from app.utils.grade12_accounting.financial_indicators_generator import (
    generate as gen_indicators,
    generate_questions as gen_ind_questions,
)


class TestGrade12AccountingGenerators(unittest.TestCase):
    """Rigorous contract, determinism, schema, and pedagogical validation for Grade 12 Accounting."""

    # =========================================================================
    # CASH FLOW STATEMENT GENERATOR TESTS
    # =========================================================================
    def test_cfs_determinism(self):
        """Verifies that identical seeds produce identical questions and solutions."""
        res1 = gen_cfs(mode="compound", seed=42)
        res2 = gen_cfs(mode="compound", seed=42)
        q1 = res1["questions"][0]
        q2 = res2["questions"][0]

        self.assertEqual(q1["prompt"], q2["prompt"])
        self.assertEqual(q1["correct_map"], q2["correct_map"])
        self.assertEqual(q1["ideal_answer"], q2["ideal_answer"])

    def test_cfs_compound_exam_ceiling_structure(self):
        """Validates the 15-mark NSC Paper 1 Cash Flow Statement 2D tabular schema."""
        res = gen_cfs(mode="compound", seed=101)
        q = res["questions"][0]

        self.assertEqual(q["marks"], 15)
        self.assertEqual(q["mode"], "compound")
        self.assertEqual(q["subskill"], "cash_flow_statement")
        self.assertEqual(q["question_type"], "table_completion")

        # 2D Tabular Schema
        self.assertIn("headers", q)
        self.assertEqual(len(q["headers"]), 2)
        self.assertIn("rows", q)
        self.assertGreaterEqual(len(q["rows"]), 18)

        # Check cell coordinates and types
        must_be_empty_found = False
        required_found = False
        given_found = False

        for row in q["rows"]:
            for cell in row:
                self.assertIn("coordinate", cell)
                self.assertTrue(cell["coordinate"].startswith("t0_r"))
                self.assertIn("type", cell)
                self.assertIn(cell["type"], ["given", "required", "must_be_empty"])
                if cell["type"] == "must_be_empty":
                    must_be_empty_found = True
                    self.assertEqual(cell["value"], "")
                elif cell["type"] == "required":
                    required_found = True
                elif cell["type"] == "given":
                    given_found = True

        self.assertTrue(must_be_empty_found, "Must include must_be_empty header cells.")
        self.assertTrue(required_found, "Must include required data cells.")
        self.assertTrue(given_found, "Must include given cells.")

        # Deduction rules
        deductions = {d["rule"]: d["penalty"] for d in q["marking_schema"]["deductions"]}
        self.assertIn("must_be_empty_filled", deductions)
        self.assertEqual(deductions["must_be_empty_filled"], -1)
        self.assertIn("added_instead_of_subtracted_dividends_paid", deductions)
        self.assertIn("forgot_negative_tax_paid", deductions)
        self.assertIn("omitted_fixed_asset_disposal_proceeds", deductions)

        # Misconception tags
        tags = q["misconception_tags"]
        self.assertIn("added_instead_of_subtracted_dividends_paid", tags)
        self.assertIn("forgot_negative_tax_paid", tags)
        self.assertIn("inverted_working_capital_inventory", tags)
        self.assertIn("omitted_fixed_asset_disposal_proceeds", tags)

        # Marking schema total
        self.assertEqual(q["marking_schema"]["total_marks"], 15)

    def test_cfs_scaffolding_taxation_paid_subdrill(self):
        """Validates elementary_taxation_paid sub-drill (4 marks)."""
        res = gen_cfs(mode="elementary_taxation_paid", seed=55)
        q = res["questions"][0]

        self.assertEqual(q["marks"], 4)
        self.assertEqual(q["subskill"], "elementary_taxation_paid")
        self.assertEqual(q["marking_schema"]["total_marks"], 4)
        self.assertIn("forgot_negative_tax_paid", q["misconception_tags"])
        self.assertIn("t0_r4_c1", q["correct_map"])
        self.assertTrue(q["correct_map"]["t0_r4_c1"].startswith("(") and q["correct_map"]["t0_r4_c1"].endswith(")"))

    def test_cfs_scaffolding_dividends_paid_subdrill(self):
        """Validates elementary_dividends_paid sub-drill (4 marks)."""
        res = gen_cfs(mode="elementary_dividends_paid", seed=66)
        q = res["questions"][0]

        self.assertEqual(q["marks"], 4)
        self.assertEqual(q["subskill"], "elementary_dividends_paid")
        self.assertEqual(q["marking_schema"]["total_marks"], 4)
        self.assertIn("added_instead_of_subtracted_dividends_paid", q["misconception_tags"])
        self.assertIn("t0_r4_c1", q["correct_map"])
        self.assertTrue(q["correct_map"]["t0_r4_c1"].startswith("(") and q["correct_map"]["t0_r4_c1"].endswith(")"))

    def test_cfs_scaffolding_working_capital_subdrill(self):
        """Validates elementary_working_capital sub-drill (4 marks)."""
        res = gen_cfs(mode="elementary_working_capital", seed=77)
        q = res["questions"][0]

        self.assertEqual(q["marks"], 4)
        self.assertEqual(q["subskill"], "elementary_working_capital")
        self.assertEqual(q["marking_schema"]["total_marks"], 4)
        self.assertIn("inverted_working_capital_inventory", q["misconception_tags"])
        self.assertIn("t0_r3_c1", q["correct_map"])

    # =========================================================================
    # FINANCIAL INDICATORS GENERATOR TESTS
    # =========================================================================
    def test_indicators_determinism(self):
        """Verifies deterministic output for Financial Indicators."""
        res1 = gen_indicators(mode="compound", seed=88)
        res2 = gen_indicators(mode="compound", seed=88)
        q1 = res1["questions"][0]
        q2 = res2["questions"][0]

        self.assertEqual(q1["prompt"], q2["prompt"])
        self.assertEqual(q1["correct_map"], q2["correct_map"])
        self.assertEqual(q1["ideal_answer"], q2["ideal_answer"])

    def test_indicators_compound_exam_ceiling_structure(self):
        """Validates the 12-mark NSC Financial Indicators exam ceiling."""
        res = gen_indicators(mode="compound", seed=99)
        q = res["questions"][0]

        self.assertEqual(q["marks"], 12)
        self.assertEqual(q["mode"], "compound")
        self.assertEqual(q["subskill"], "financial_indicators")
        self.assertEqual(q["question_type"], "table_completion")

        # Table schema checks
        self.assertIn("headers", q)
        self.assertIn("rows", q)
        self.assertEqual(q["marking_schema"]["total_marks"], 12)

        # Check section header rows are must_be_empty
        empty_coords = [
            cell["coordinate"]
            for row in q["rows"]
            for cell in row
            if cell.get("type") == "must_be_empty"
        ]
        self.assertGreater(len(empty_coords), 0)
        for coord in empty_coords:
            self.assertEqual(q["correct_map"][coord], "")

        # Check deduction rules
        deductions = {d["rule"]: d["penalty"] for d in q["marking_schema"]["deductions"]}
        self.assertIn("must_be_empty_filled", deductions)
        self.assertEqual(deductions["must_be_empty_filled"], -1)

        # Check required indicators are present in hints and marking points
        marking_descs = " ".join(mp["desc"] for mp in q["marking_schema"]["marking_points"])
        self.assertIn("Current ratio", marking_descs)
        self.assertIn("Acid-test ratio", marking_descs)
        self.assertIn("Debtors collection", marking_descs)
        self.assertIn("Creditors payment", marking_descs)
        self.assertIn("Debt-equity ratio", marking_descs)
        self.assertIn("ROSHE", marking_descs)
        self.assertIn("Earnings per share", marking_descs)
        self.assertIn("Dividends per share", marking_descs)

        # Commentary questions included
        self.assertIn("mp_comm_liq", [mp["id"] for mp in q["marking_schema"]["marking_points"]])
        self.assertIn("mp_comm_gear", [mp["id"] for mp in q["marking_schema"]["marking_points"]])
        self.assertIn("mp_comm_ret", [mp["id"] for mp in q["marking_schema"]["marking_points"]])

    def test_indicators_scaffolding_acid_test_subdrill(self):
        """Validates elementary_acid_test sub-drill (3 marks)."""
        res = gen_indicators(mode="elementary_acid_test", seed=123)
        q = res["questions"][0]

        self.assertEqual(q["marks"], 3)
        self.assertEqual(q["subskill"], "elementary_acid_test")
        self.assertEqual(q["marking_schema"]["total_marks"], 3)
        self.assertIn("included_inventory_in_acid_test", q["misconception_tags"])
        self.assertIn("1", q["correct_map"]["t0_r1_c1"])

    def test_indicators_scaffolding_debt_equity_subdrill(self):
        """Validates elementary_debt_equity sub-drill (4 marks)."""
        res = gen_indicators(mode="elementary_debt_equity", seed=234)
        q = res["questions"][0]

        self.assertEqual(q["marks"], 4)
        self.assertEqual(q["subskill"], "elementary_debt_equity")
        self.assertEqual(q["marking_schema"]["total_marks"], 4)
        self.assertIn("inverted_debt_equity_ratio", q["misconception_tags"])
        self.assertIn(": 1", q["correct_map"]["t0_r0_c1"])

    def test_indicators_scaffolding_roshe_subdrill(self):
        """Validates elementary_roshe_calc sub-drill (4 marks)."""
        res = gen_indicators(mode="elementary_roshe_calc", seed=345)
        q = res["questions"][0]

        self.assertEqual(q["marks"], 4)
        self.assertEqual(q["subskill"], "elementary_roshe_calc")
        self.assertEqual(q["marking_schema"]["total_marks"], 4)
        self.assertIn("used_closing_equity_instead_of_average", q["misconception_tags"])
        self.assertTrue(q["correct_map"]["t0_r1_c1"].endswith("%"))

    # =========================================================================
    # GENERATOR REGISTRY ROUTING & TOPIC ALIASES TESTS
    # =========================================================================
    def test_registry_topic_alias_resolution(self):
        """Verifies full topic alias resolution in the Central Generator Registry."""
        cfs_aliases = [
            "cash flow statement",
            "cash flow statements",
            "cash flow",
            "cash generated from operations",
            "taxation paid",
            "dividends paid",
            "working capital changes",
        ]
        for alias in cfs_aliases:
            key = resolve_generator_key(alias, grade="12", subject="Accounting")
            self.assertEqual(
                key,
                "grade12_accounting_cash_flow_statement",
                f"Alias '{alias}' failed to resolve to CFS generator.",
            )

        indicator_aliases = [
            "financial indicators",
            "financial ratios",
            "analysis and interpretation of financial statements",
            "analysis of financial statements",
            "interpretation of financial statements",
            "current ratio",
            "acid test ratio",
            "debtors collection period",
            "creditors payment period",
            "debt equity ratio",
            "gearing",
            "roshe",
            "return on shareholders equity",
            "earnings per share",
            "dividends per share",
        ]
        for alias in indicator_aliases:
            key = resolve_generator_key(alias, grade="12", subject="Accounting")
            self.assertEqual(
                key,
                "grade12_accounting_financial_indicators",
                f"Alias '{alias}' failed to resolve to Financial Indicators generator.",
            )

    def test_master_generate_variant_dispatch(self):
        """Tests end-to-end question generation and normalization through generate_variant."""
        questions_cfs = generate_variant(
            topic="cash flow statement",
            grade="12",
            subject="Accounting",
            count=1,
            seed=500,
        )
        self.assertEqual(len(questions_cfs), 1)
        self.assertEqual(questions_cfs[0]["marks"], 15)
        self.assertEqual(questions_cfs[0]["suggested_duration_mins"], 25)

        questions_ind = generate_variant(
            topic="financial indicators",
            grade="12",
            subject="Accounting",
            count=1,
            seed=600,
        )
        self.assertEqual(len(questions_ind), 1)
        self.assertEqual(questions_ind[0]["marks"], 12)
        self.assertEqual(questions_ind[0]["suggested_duration_mins"], 20)


if __name__ == "__main__":
    unittest.main()
