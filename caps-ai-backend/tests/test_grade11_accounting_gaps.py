"""Grade 11 Accounting Gaps Test Suite (Sprint 2).
Validates:
1. Partnerships Financial Statements Generator (mode="compound" 15-mark ceiling + 3 sub-drills).
2. Inventory Valuation Generator (mode="compound" 12-mark ceiling + 2 sub-drills).
3. 2D tabular schema with cell coordinates, cell types (required, given, must_be_empty), and deduction rules.
4. Standardized misconception tags.
5. Generator Registry resolution and topic aliases.
6. 100% AST purity and deterministic execution.
"""
from __future__ import annotations

import ast
from pathlib import Path
import random
import sys
import unittest

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.utils.grade11_accounting.partnerships_financial_statements_generator import (
    generate as gen_partnerships,
    generate_questions as gen_part_questions,
    MISCONCEPTION_DRAWINGS_ADDED,
    MISCONCEPTION_OMITTED_INTEREST,
    MISCONCEPTION_INVERTED_RATIO,
    MISCONCEPTION_SALARY_INCREASE,
)
from app.utils.grade11_accounting.inventory_valuation_generator import (
    generate as gen_inventory,
    generate_questions as gen_inv_questions,
    MISCONCEPTION_CARRIAGE,
    MISCONCEPTION_FIFO_OLDEST,
    MISCONCEPTION_OMITTED_OPENING,
    MISCONCEPTION_SIMPLE_AVG,
)
from app.services.generator_registry import (
    ALL_GENERATORS,
    GRADE11_ACCOUNTING_GENERATORS,
    generate_variant,
    resolve_generator_key,
)


class TestGrade11AccountingGaps(unittest.TestCase):
    """Rigorous tests for Grade 11 Accounting Partnerships and Inventory Valuation."""

    # =========================================================================
    # PARTNERSHIPS FINANCIAL STATEMENTS TESTS
    # =========================================================================
    def test_partnerships_determinism(self):
        """Verifies deterministic generation with seeded PRNG."""
        res1 = gen_partnerships(seed=42)
        res2 = gen_partnerships(seed=42)
        self.assertEqual(len(res1["questions"]), 1)
        self.assertEqual(len(res2["questions"]), 1)
        q1 = res1["questions"][0]
        q2 = res2["questions"][0]
        self.assertEqual(q1["prompt"], q2["prompt"])
        self.assertEqual(q1["correct_map"], q2["correct_map"])
        self.assertEqual(q1["ideal_answer"], q2["ideal_answer"])

        # Different seeds generate distinct scenarios
        res3 = gen_partnerships(seed=999)
        q3 = res3["questions"][0]
        self.assertNotEqual(q1["correct_map"], q3["correct_map"])

    def test_partnerships_compound_exam_ceiling(self):
        """Verifies 15-mark compound exam ceiling for Current Accounts Note."""
        res = gen_partnerships(mode="compound", seed=101)
        q = res["questions"][0]

        # 15 marks
        self.assertEqual(q["marks"], 15)
        self.assertEqual(q["question_type"], "table_completion")
        self.assertEqual(q["topic"], "Partnerships")

        # 2D tabular headers and rows
        self.assertEqual(len(q["headers"]), 4)
        self.assertEqual(q["headers"][0], "Current Accounts Note")
        self.assertEqual(q["headers"][3], "Total")
        self.assertGreaterEqual(len(q["rows"]), 8)

        # Coordinates check
        self.assertIn("t0_r0_c1", q["correct_map"])
        self.assertIn("t0_r1_c1", q["correct_map"])
        self.assertIn("t0_r6_c1", q["correct_map"])  # Drawings
        self.assertIn("t0_r9_c1", q["correct_map"])  # Closing balance

        # Cell types schema check
        cell_types = {cell["type"] for row in q["rows"] for cell in row}
        self.assertIn("required", cell_types)
        self.assertIn("given", cell_types)
        self.assertIn("must_be_empty", cell_types)

        # Deduction rules
        deduction_rules = [d["rule"] for d in q["marking_schema"]["deductions"]]
        self.assertIn("must_be_empty_filled", deduction_rules)
        self.assertIn("added_instead_of_subtracted_drawings", deduction_rules)
        self.assertIn("omitted_interest_on_capital", deduction_rules)
        self.assertIn("inverted_profit_sharing_ratio", deduction_rules)
        self.assertIn("forgot_salary_increase_months", deduction_rules)

        # Misconception tags
        self.assertIn(MISCONCEPTION_DRAWINGS_ADDED, q["misconception_tags"])
        self.assertIn(MISCONCEPTION_OMITTED_INTEREST, q["misconception_tags"])
        self.assertIn(MISCONCEPTION_INVERTED_RATIO, q["misconception_tags"])
        self.assertIn(MISCONCEPTION_SALARY_INCREASE, q["misconception_tags"])

        # Hints presence
        self.assertIn("tier1_location", q["hints"])
        self.assertIn("tier2_directional_rule", q["hints"])
        self.assertIn("tier3_worked_step", q["hints"])

    def test_partnerships_elementary_subdrills(self):
        """Verifies adaptive scaffolding sub-drills for Partnerships."""
        # 1. Elementary Interest on Capital
        res_ioc = gen_partnerships(subskill="elementary_interest_on_capital", seed=201)
        q_ioc = res_ioc["questions"][0]
        self.assertEqual(q_ioc["marks"], 4)
        self.assertEqual(q_ioc["subskill"], "elementary_interest_on_capital")
        self.assertIn("interest_on_capital", q_ioc["correct_map"])
        self.assertIn(MISCONCEPTION_OMITTED_INTEREST, q_ioc["misconception_tags"])

        # 2. Elementary Salaries & Bonus
        res_sal = gen_partnerships(subskill="elementary_salaries_bonus", seed=202)
        q_sal = res_sal["questions"][0]
        self.assertEqual(q_sal["marks"], 4)
        self.assertEqual(q_sal["subskill"], "elementary_salaries_bonus")
        self.assertIn("total_salary", q_sal["correct_map"])
        self.assertIn(MISCONCEPTION_SALARY_INCREASE, q_sal["misconception_tags"])

        # 3. Elementary Profit Share Ratio
        res_ratio = gen_partnerships(subskill="elementary_profit_share_ratio", seed=203)
        q_ratio = res_ratio["questions"][0]
        self.assertEqual(q_ratio["marks"], 3)
        self.assertEqual(q_ratio["subskill"], "elementary_profit_share_ratio")
        self.assertIn("remaining_profit", q_ratio["correct_map"])
        self.assertIn("share_partner_a", q_ratio["correct_map"])
        self.assertIn(MISCONCEPTION_INVERTED_RATIO, q_ratio["misconception_tags"])

    # =========================================================================
    # INVENTORY VALUATION TESTS
    # =========================================================================
    def test_inventory_determinism(self):
        """Verifies deterministic generation of inventory valuation questions."""
        res1 = gen_inventory(seed=77)
        res2 = gen_inventory(seed=77)
        self.assertEqual(len(res1["questions"]), 1)
        self.assertEqual(res1["questions"][0]["correct_map"], res2["questions"][0]["correct_map"])

        res3 = gen_inventory(seed=888)
        self.assertNotEqual(res1["questions"][0]["correct_map"], res3["questions"][0]["correct_map"])

    def test_inventory_compound_exam_ceiling(self):
        """Verifies 12-mark compound exam ceiling for FIFO vs Weighted Average."""
        res = gen_inventory(mode="compound", seed=105)
        q = res["questions"][0]

        # 12 marks
        self.assertEqual(q["marks"], 12)
        self.assertEqual(q["question_type"], "table_completion")
        self.assertEqual(q["topic"], "Inventory Valuation")

        # 2D tabular headers and rows
        self.assertEqual(q["headers"], ["Inventory Valuation Method", "Closing Stock (R)", "Cost of Sales (R)", "Gross Profit (R)"])
        self.assertEqual(len(q["rows"]), 3)

        # Coordinates check
        self.assertIn("t0_r0_c1", q["correct_map"])  # FIFO closing
        self.assertIn("t0_r0_c2", q["correct_map"])  # FIFO COS
        self.assertIn("t0_r0_c3", q["correct_map"])  # FIFO GP
        self.assertIn("t0_r1_c1", q["correct_map"])  # WAvg closing
        self.assertIn("t0_r1_c2", q["correct_map"])  # WAvg COS
        self.assertIn("t0_r1_c3", q["correct_map"])  # WAvg GP
        self.assertIn("t0_r2_c2", q["correct_map"])  # must_be_empty cell

        # Cell types check
        cell_types = {cell["type"] for row in q["rows"] for cell in row}
        self.assertIn("required", cell_types)
        self.assertIn("given", cell_types)
        self.assertIn("must_be_empty", cell_types)

        # Deduction rules & misconception tags
        deduction_rules = [d["rule"] for d in q["marking_schema"]["deductions"]]
        self.assertIn("must_be_empty_filled", deduction_rules)
        self.assertIn("allocated_carriage_incorrectly", deduction_rules)
        self.assertIn("used_oldest_stock_for_fifo_closing", deduction_rules)
        self.assertIn("omitted_opening_stock_in_weighted_avg", deduction_rules)
        self.assertIn("simple_average_instead_of_weighted_average", deduction_rules)

        self.assertIn(MISCONCEPTION_CARRIAGE, q["misconception_tags"])
        self.assertIn(MISCONCEPTION_FIFO_OLDEST, q["misconception_tags"])
        self.assertIn(MISCONCEPTION_OMITTED_OPENING, q["misconception_tags"])
        self.assertIn(MISCONCEPTION_SIMPLE_AVG, q["misconception_tags"])

        # Qualitative analysis check in prompt and ideal answer
        self.assertIn("Net Profit", q["ideal_answer"])
        self.assertIn("tax", q["ideal_answer"].lower())

    def test_inventory_elementary_subdrills(self):
        """Verifies adaptive scaffolding sub-drills for Inventory Valuation."""
        # 1. FIFO Closing Stock
        res_fifo = gen_inventory(subskill="elementary_fifo_closing_stock", seed=301)
        q_fifo = res_fifo["questions"][0]
        self.assertEqual(q_fifo["marks"], 3)
        self.assertEqual(q_fifo["subskill"], "elementary_fifo_closing_stock")
        self.assertIn("fifo_closing_inventory_value", q_fifo["correct_map"])
        self.assertIn(MISCONCEPTION_FIFO_OLDEST, q_fifo["misconception_tags"])

        # 2. Weighted Average Unit Cost
        res_wavg = gen_inventory(subskill="elementary_weighted_avg_unit_cost", seed=302)
        q_wavg = res_wavg["questions"][0]
        self.assertEqual(q_wavg["marks"], 3)
        self.assertEqual(q_wavg["subskill"], "elementary_weighted_avg_unit_cost")
        self.assertIn("weighted_avg_unit_cost", q_wavg["correct_map"])
        self.assertIn(MISCONCEPTION_CARRIAGE, q_wavg["misconception_tags"])

    # =========================================================================
    # REGISTRY INTEGRATION & ALIASES TESTS
    # =========================================================================
    def test_registry_registration_and_aliases(self):
        """Ensures both generators are registered in GRADE11_ACCOUNTING_GENERATORS, ALL_GENERATORS, and TOPIC_ALIASES."""
        self.assertIn("grade11_accounting_partnerships_financial_statements", GRADE11_ACCOUNTING_GENERATORS)
        self.assertIn("grade11_accounting_partnerships_financial_statements", ALL_GENERATORS)
        self.assertIn("grade11_accounting_inventory_valuation", GRADE11_ACCOUNTING_GENERATORS)
        self.assertIn("grade11_accounting_inventory_valuation", ALL_GENERATORS)

        # Test alias resolution
        self.assertEqual(
            resolve_generator_key("partnerships financial statements", grade="11", subject="Accounting"),
            "grade11_accounting_partnerships_financial_statements",
        )
        self.assertEqual(
            resolve_generator_key("appropriation account", grade="11", subject="Accounting"),
            "grade11_accounting_partnerships_financial_statements",
        )
        self.assertEqual(
            resolve_generator_key("current accounts note", grade="11", subject="Accounting"),
            "grade11_accounting_partnerships_financial_statements",
        )
        self.assertEqual(
            resolve_generator_key("inventory valuation", grade="11", subject="Accounting"),
            "grade11_accounting_inventory_valuation",
        )
        self.assertEqual(
            resolve_generator_key("fifo", grade="11", subject="Accounting"),
            "grade11_accounting_inventory_valuation",
        )
        self.assertEqual(
            resolve_generator_key("weighted average", grade="11", subject="Accounting"),
            "grade11_accounting_inventory_valuation",
        )

        # Test generate_variant dispatching
        var_part = generate_variant("partnerships financial statements", grade="11", subject="Accounting", seed=10)
        self.assertIsInstance(var_part, list)
        self.assertGreaterEqual(len(var_part), 1)
        self.assertEqual(var_part[0]["topic"], "Partnerships")

        var_inv = generate_variant("inventory valuation", grade="11", subject="Accounting", seed=20)
        self.assertIsInstance(var_inv, list)
        self.assertGreaterEqual(len(var_inv), 1)
        self.assertEqual(var_inv[0]["topic"], "Inventory Valuation")

    # =========================================================================
    # AST PURITY CHECK
    # =========================================================================
    def test_ast_purity_grade11_accounting_generators(self):
        """Ensures 100% AST purity and zero LLM/network imports in both generators."""
        forbidden_imports = {
            "openai", "anthropic", "groq", "google.generativeai", "langchain",
            "requests", "httpx", "aiohttp", "urllib.request", "socket"
        }

        files_to_check = [
            BASE_DIR / "app" / "utils" / "grade11_accounting" / "partnerships_financial_statements_generator.py",
            BASE_DIR / "app" / "utils" / "grade11_accounting" / "inventory_valuation_generator.py",
        ]

        for filepath in files_to_check:
            self.assertTrue(filepath.exists(), f"File {filepath} must exist")
            with open(filepath, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read(), filename=str(filepath))

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        for forbidden in forbidden_imports:
                            self.assertNotIn(forbidden, alias.name, f"Forbidden import {alias.name} in {filepath}")
                elif isinstance(node, ast.ImportFrom):
                    mod = node.module or ""
                    for forbidden in forbidden_imports:
                        self.assertNotIn(forbidden, mod, f"Forbidden from-import {mod} in {filepath}")


if __name__ == "__main__":
    unittest.main()
