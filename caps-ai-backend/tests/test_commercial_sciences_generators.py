"""Commercial Sciences Comprehensive Test Suite.
Validates Grade 8 EMS, Grade 9 EMS, Grade 10 Accounting Bank Reconciliation,
and Grade 12 Accounting Cost Accounting against the 6-Pillar Generator Contract.
Also runs full AST purity checks across all Commercial Sciences generators.
"""
from __future__ import annotations

import ast
import glob
import os
from pathlib import Path
import random
import sys
import unittest

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Grade 8 EMS
from app.utils.grade8_ems import generate_topic_questions as gen_g8_topic
from app.utils.grade8_ems import (
    term1_accounting_basics as g8_basics,
    term1_source_documents as g8_docs,
    term1_general_ledger as g8_gl,
    term2_accounting_cycle as g8_cycle,
    term2_crj as g8_crj,
    term3_cpj_and_crj as g8_cpj,
)

# Grade 9 EMS
from app.utils.grade9_ems import generate_topic_questions as gen_g9_topic
from app.utils.grade9_ems import (
    term1_crj_cpj as g9_crj_cpj,
    term1_general_ledger as g9_gl,
    term1_economy as g9_econ,
    term3_trade_unions as g9_unions,
    term2_debtors_journal as g9_dj,
    term3_creditors_journal as g9_cj,
)

# Grade 10 Accounting
from app.utils.grade10_accounting.term2.bank_reconciliation_generator import (
    generate_questions as gen_bank_recon,
    MISCONCEPTION_DEBIT_CREDIT_INVERSION,
    MISCONCEPTION_TIMING_VS_ERROR_CONFUSION,
)

# Grade 12 Accounting
from app.utils.grade12_accounting.cost_accounting_generator import (
    generate as gen_cost_accounting,
)
from app.utils.grade12_accounting.cash_flow_statement_generator import (
    generate as gen_cash_flow,
)
from app.utils.grade12_accounting.financial_indicators_generator import (
    generate as gen_financial_indicators,
)


class TestCommercialSciencesGenerators(unittest.TestCase):
    """Rigorous contract, determinism, and tabular format tests for Commercial Sciences."""

    # =========================================================================
    # GRADE 8 EMS TESTS
    # =========================================================================
    def test_grade8_ems_determinism(self):
        """Validates seed determinism for Grade 8 EMS generators."""
        q1 = gen_g8_topic("term1_general_ledger", subskill="trial_balance", seed=42)
        q2 = gen_g8_topic("term1_general_ledger", subskill="trial_balance", seed=42)
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]["prompt"], q2[0]["prompt"])
        self.assertEqual(q1[0]["correct_map"], q2[0]["correct_map"])

        q3 = gen_g8_topic("term1_general_ledger", subskill="dead_clic", seed=55)
        q4 = gen_g8_topic("term1_general_ledger", subskill="dead_clic", seed=55)
        self.assertEqual(q3[0]["correct_map"], q4[0]["correct_map"])

    def test_grade8_ems_general_ledger_trial_balance_modality(self):
        """Ensures Grade 8 General Ledger and Trial Balance conform to 2D tabular modality."""
        questions = gen_g8_topic("term1_general_ledger", subskill="trial_balance", seed=100)
        self.assertEqual(len(questions), 1)
        q = questions[0]
        self.assertEqual(q["question_type"], "table_completion")
        self.assertIn("headers", q)
        self.assertIn("rows", q)
        self.assertIn("correct_map", q)
        self.assertIn("marking_schema", q)
        self.assertIn("misconception_tags", q)

        # Verify cell schema
        first_cell = q["rows"][0][0]
        self.assertIn("coordinate", first_cell)
        self.assertIn("type", first_cell)
        self.assertIn(first_cell["type"], ["given", "required", "must_be_empty"])

    def test_grade8_ems_source_docs_and_cycle_coverage(self):
        """Ensures Grade 8 source documents and accounting cycle are fully dispatchable."""
        q_docs = gen_g8_topic("term1_source_documents", seed=77)
        self.assertGreaterEqual(len(q_docs), 1)
        self.assertIn("hint_sections", q_docs[0])

        q_cycle = gen_g8_topic("term2_accounting_cycle", seed=88)
        self.assertGreaterEqual(len(q_cycle), 1)
        self.assertIn("prompt", q_cycle[0])
        self.assertGreater(len(q_cycle[0]["prompt"]), 10)

    # =========================================================================
    # GRADE 9 EMS TESTS
    # =========================================================================
    def test_grade9_ems_cost_of_sales_drill(self):
        """Validates elementary Cost of Sales calculations using 'What I WANT / What I HAVE' formula."""
        q1 = gen_g9_topic("term1_crj_cpj", subskill="cost_of_sales", seed=42)
        q2 = gen_g9_topic("term1_crj_cpj", subskill="cost_of_sales", seed=42)
        self.assertEqual(len(q1), 1)
        self.assertEqual(q1[0]["prompt"], q2[0]["prompt"])
        self.assertEqual(q1[0]["correct_map"], q2[0]["correct_map"])
        self.assertIn("Mark-up", q1[0]["prompt"])
        self.assertIn("misconception_tags", q1[0])

    def test_grade9_ems_trading_cycle_equation_drill(self):
        """Validates trading cycle effect on the Accounting Equation (A = OE + L)."""
        q = gen_g9_topic("term1_crj_cpj", subskill="trading_equation", seed=33)
        self.assertEqual(len(q), 1)
        item = q[0]
        self.assertIn("Accounting Equation", item["title"])
        self.assertIn("t0_r1_c1", item["correct_map"])
        self.assertEqual(item["correct_map"]["t0_r1_c1"], "Bank")
        self.assertEqual(item["correct_map"]["t0_r1_c2"], "Sales")
        self.assertEqual(item["correct_map"]["t0_r2_c1"], "Cost of Sales")
        self.assertEqual(item["correct_map"]["t0_r2_c2"], "Trading Stock")

    def test_grade9_ems_general_ledger_trading_stock(self):
        """Validates 2D tabular Trading Stock account in General Ledger."""
        q = gen_g9_topic("term1_general_ledger", subskill="trading_stock_ledger", seed=50)
        self.assertEqual(len(q), 1)
        item = q[0]
        self.assertEqual(item["question_type"], "table_completion")
        self.assertIn("Trading Stock", item["title"])
        self.assertIn("t0_r1_c7", item["correct_map"])  # Balance c/d
        self.assertIn("marking_schema", item)

    def test_grade9_ems_economic_systems_matrix(self):
        """Validates the economic systems comparative matrix generator."""
        q = gen_g9_topic("term1_economy", subskill="economic_systems_matrix", seed=10)
        self.assertEqual(len(q), 1)
        item = q[0]
        self.assertEqual(item["question_type"], "table_completion")
        self.assertIn("Planned Economy", item["headers"])
        self.assertIn("Market Economy", item["headers"])
        self.assertIn("Mixed Economy", item["headers"][3])

    def test_grade9_ems_trade_unions_roles_responsibilities(self):
        """Validates trade unions roles vs responsibilities table drill."""
        q = gen_g9_topic("term3_trade_unions", subskill="roles_vs_responsibilities", seed=25)
        self.assertEqual(len(q), 1)
        item = q[0]
        self.assertEqual(item["question_type"], "table_completion")
        self.assertIn("Role vs Responsibility", item["headers"][2])
        self.assertIn("t0_r0_c2", item["correct_map"])

    # =========================================================================
    # GRADE 10 ACCOUNTING BANK RECONCILIATION TESTS
    # =========================================================================
    def test_grade10_bank_reconciliation_2d_tabular(self):
        """Ensures Grade 10 Bank Reconciliation statement conforms to exact exam formats."""
        r = random.Random(123)
        questions = gen_bank_recon(r=r, n=1, mode="compound", seed=123)
        self.assertEqual(len(questions), 1)
        q = questions[0]

        # Check 2D tabular coordinates
        self.assertEqual(q["question_type"], "table_completion")
        self.assertIn("Debit (R)", q["headers"])
        self.assertIn("Credit (R)", q["headers"])
        self.assertTrue(any("t0_r0_c1" in k or "t0_r0_c2" in k for k in q["correct_map"]))

        # Check deduction rules & misconception tags
        self.assertIn("deductions", q["marking_schema"])
        deduction_rules = [d["rule"] for d in q["marking_schema"]["deductions"]]
        self.assertIn("must_be_empty_filled", deduction_rules)

        self.assertIn(MISCONCEPTION_DEBIT_CREDIT_INVERSION, q["misconception_tags"])
        self.assertIn(MISCONCEPTION_TIMING_VS_ERROR_CONFUSION, q["misconception_tags"])

        # Check cell types
        cell_types = {cell["type"] for row in q["rows"] for cell in row}
        self.assertTrue("required" in cell_types or "must_be_empty" in cell_types)
        self.assertIn("given", cell_types)

    # =========================================================================
    # GRADE 12 ACCOUNTING COST ACCOUNTING TESTS
    # =========================================================================
    def test_grade12_cost_accounting_compound_2d_tabular(self):
        """Ensures Grade 12 Production Cost Statement matches NSC Paper 2 standards."""
        res = gen_cost_accounting(mode="compound", seed=42)
        self.assertIn("questions", res)
        self.assertEqual(len(res["questions"]), 1)
        q = res["questions"][0]

        self.assertEqual(q["question_type"], "table_completion")
        self.assertEqual(q["headers"], ["Production Cost Statement", "Amount (R)"])

        # Check coordinates and cell types
        self.assertIn("t0_r0_c1", q["correct_map"])
        first_editable = q["rows"][0][1]
        self.assertEqual(first_editable["coordinate"], "t0_r0_c1")
        self.assertEqual(first_editable["type"], "required")

        # Check deduction rules & misconception tags
        deduction_rules = [d["rule"] for d in q["marking_schema"]["deductions"]]
        self.assertIn("must_be_empty_filled", deduction_rules)
        self.assertIn("added_closing_wip_instead_of_subtracting", deduction_rules)

        self.assertIn("added_closing_wip_instead_of_subtracting", q["misconception_tags"])
        self.assertIn("omitted_factory_overhead_note", q["misconception_tags"])

    def test_grade12_cost_accounting_elementary_drills(self):
        """Validates all Grade 12 Cost Accounting elementary sub-drills."""
        # Prime cost
        res_prime = gen_cost_accounting(mode="elementary_prime_cost", seed=10)
        self.assertEqual(res_prime["questions"][0]["subskill"], "elementary_prime_cost")
        self.assertIn("Prime Cost", res_prime["questions"][0]["sample_answer"])

        # Factory Overhead note
        res_foh = gen_cost_accounting(mode="elementary_factory_overhead", seed=20)
        self.assertEqual(res_foh["questions"][0]["subskill"], "elementary_factory_overhead")
        self.assertEqual(res_foh["questions"][0]["question_type"], "table_completion")

        # WIP adjustment
        res_wip = gen_cost_accounting(mode="elementary_wip_adjustment", seed=30)
        self.assertEqual(res_wip["questions"][0]["subskill"], "elementary_wip_adjustment")
        self.assertIn("Cost of Finished Goods", res_wip["questions"][0]["ideal_answer"])

        # Break-Even Point
        res_bep = gen_cost_accounting(mode="elementary_break_even_calc", seed=40)
        self.assertEqual(res_bep["questions"][0]["subskill"], "elementary_break_even_calc")
        self.assertIn("BEP", res_bep["questions"][0]["ideal_answer"])

    def test_grade12_cash_flow_statement_exam_ceiling(self):
        """Validates Grade 12 Cash Flow Statement 15-mark exam ceiling and scaffolding."""
        res = gen_cash_flow(mode="compound", seed=42)
        q = res["questions"][0]
        self.assertEqual(q["marks"], 15)
        self.assertEqual(q["question_type"], "table_completion")
        self.assertIn("must_be_empty_filled", [d["rule"] for d in q["marking_schema"]["deductions"]])
        self.assertIn("added_instead_of_subtracted_dividends_paid", q["misconception_tags"])
        self.assertIn("forgot_negative_tax_paid", q["misconception_tags"])
        self.assertIn("inverted_working_capital_inventory", q["misconception_tags"])
        self.assertIn("omitted_fixed_asset_disposal_proceeds", q["misconception_tags"])

        # Check sub-drills
        res_tax = gen_cash_flow(mode="elementary_taxation_paid", seed=50)
        self.assertEqual(res_tax["questions"][0]["marks"], 4)
        res_div = gen_cash_flow(mode="elementary_dividends_paid", seed=60)
        self.assertEqual(res_div["questions"][0]["marks"], 4)
        res_wc = gen_cash_flow(mode="elementary_working_capital", seed=70)
        self.assertEqual(res_wc["questions"][0]["marks"], 4)

    def test_grade12_financial_indicators_exam_ceiling(self):
        """Validates Grade 12 Financial Indicators 12-mark exam ceiling and scaffolding."""
        res = gen_financial_indicators(mode="compound", seed=42)
        q = res["questions"][0]
        self.assertEqual(q["marks"], 12)
        self.assertEqual(q["question_type"], "table_completion")
        self.assertIn("must_be_empty_filled", [d["rule"] for d in q["marking_schema"]["deductions"]])
        self.assertIn("included_inventory_in_acid_test", q["misconception_tags"])
        self.assertIn("inverted_debt_equity_ratio", q["misconception_tags"])
        self.assertIn("used_closing_equity_instead_of_average", q["misconception_tags"])

        # Check sub-drills
        res_acid = gen_financial_indicators(mode="elementary_acid_test", seed=50)
        self.assertEqual(res_acid["questions"][0]["marks"], 3)
        res_de = gen_financial_indicators(mode="elementary_debt_equity", seed=60)
        self.assertEqual(res_de["questions"][0]["marks"], 4)
        res_roshe = gen_financial_indicators(mode="elementary_roshe_calc", seed=70)
        self.assertEqual(res_roshe["questions"][0]["marks"], 4)

    # =========================================================================
    # UNIVERSAL AST PURITY & NO-LLM CHECK ACROSS COMMERCIAL SCIENCES
    # =========================================================================
    def test_commercial_sciences_ast_purity(self):
        """Verifies zero LLM imports and 100% AST parseability across all Commercial Sciences generators."""
        comm_dirs = [
            BASE_DIR / "app/utils/grade7_ems",
            BASE_DIR / "app/utils/grade8_ems",
            BASE_DIR / "app/utils/grade9_ems",
            BASE_DIR / "app/utils/grade10_accounting",
            BASE_DIR / "app/utils/grade11_accounting",
            BASE_DIR / "app/utils/grade12_accounting",
            BASE_DIR / "app/utils/grade10_business_studies",
            BASE_DIR / "app/utils/grade11_business_studies",
            BASE_DIR / "app/utils/grade12_business_studies",
        ]
        forbidden_modules = {"openai", "anthropic", "google.generativeai", "langchain", "cohere", "litellm", "transformers"}

        total_files = 0
        for d in comm_dirs:
            for py_path in d.glob("**/*.py"):
                if "__pycache__" in str(py_path):
                    continue
                total_files += 1
                with open(py_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Verify AST parseability
                try:
                    tree = ast.parse(content, filename=str(py_path))
                except Exception as e:
                    self.fail(f"Syntax error in {py_path}: {e}")

                # Verify zero forbidden LLM imports
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            root_pkg = alias.name.split(".")[0]
                            self.assertNotIn(root_pkg, forbidden_modules, f"Forbidden LLM import '{alias.name}' in {py_path}")
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            root_pkg = node.module.split(".")[0]
                            self.assertNotIn(root_pkg, forbidden_modules, f"Forbidden LLM import from '{node.module}' in {py_path}")

        self.assertGreaterEqual(total_files, 150, "Should have inspected at least 150 Commercial Sciences generator files.")


if __name__ == "__main__":
    unittest.main()
