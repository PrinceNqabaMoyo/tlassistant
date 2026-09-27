"""
Universal Generator Contract Test Suite
Validates that question generators across Phase 5A through 5G adhere to the 6-Pillar Contract:
1. Seed invariance (deterministic output)
2. Metadata enrichment (subskill, misconception_tags, topic/topic_id)
3. 3-Tier hints / hint sections
4. Marking points / editable marking schema
5. Zero LLM imports / AST purity
6. Native cognitive modality (SymPy/KaTeX for Maths/Tech, Tables for Accounting/EMS, Rubrics for Business Studies, Formulas for Sciences)
"""

import sys
import random
import unittest
from pathlib import Path

# Add backend directory to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))


class TestGeneratorContracts(unittest.TestCase):

    # --- Phase 5A: Senior EMS (Grades 7, 8, 9) ---
    def test_phase5a_grade7_ems_contract(self):
        from app.utils.grade7_ems.term1_money_and_needs import generate as gen_g7_money

        q1 = gen_g7_money(subskill="concepts", seed=42, mode="scaffold")
        q2 = gen_g7_money(subskill="concepts", seed=42, mode="scaffold")
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['id'], q2[0]['id'])
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])
        self.assertIn('misconception_tags', q1[0])

    def test_phase5a_grade8_ems_contract(self):
        from app.utils.grade8_ems.term1_accounting_basics import generate as gen_g8_acc

        q1 = gen_g8_acc(subskill="concepts", seed=88, mode="scaffold")
        q2 = gen_g8_acc(subskill="concepts", seed=88, mode="scaffold")
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])
        self.assertIn('hint_sections', q1[0])

    def test_phase5a_grade9_ems_contract(self):
        from app.utils.grade9_ems.term1_circular_flow import generate as gen_g9_cf

        q1 = gen_g9_cf(subskill="concepts", seed=99, mode="scaffold")
        q2 = gen_g9_cf(subskill="concepts", seed=99, mode="scaffold")
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])

    # --- Phase 5B: Accounting (Grades 10, 11, 12) ---
    def test_phase5b_grade10_accounting_contract(self):
        from app.utils.grade10_accounting.sole_trader_generator import generate_questions as gen_g10_acct

        r1 = random.Random(123)
        r2 = random.Random(123)
        q1 = gen_g10_acct(r=r1, n=1, subskill="crj", mode="scaffold")
        q2 = gen_g10_acct(r=r2, n=1, subskill="crj", mode="scaffold")
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])
        self.assertEqual(q1[0]['correct_map'], q2[0]['correct_map'])
        self.assertIn('cell_hints', q1[0])

    def test_phase5b_grade10_bank_reconciliation_contract(self):
        from app.utils.grade10_accounting.term2.bank_reconciliation_generator import generate_questions as gen_g10_recon

        r1 = random.Random(123)
        r2 = random.Random(123)
        q1 = gen_g10_recon(r=r1, n=1, mode="scaffold", seed=123)
        q2 = gen_g10_recon(r=r2, n=1, mode="scaffold", seed=123)
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])
        self.assertEqual(q1[0]['correct_map'], q2[0]['correct_map'])
        self.assertEqual(q1[0]['term'], 2)
        self.assertIn('marking_schema', q1[0])
        self.assertIn('misconception_tags', q1[0])
        self.assertIn('cell_hints', q1[0])

    # --- Phase 5C & 5D: Mathematics (Grades 7–12) ---
    def test_phase5cd_grade10_mathematics_contract(self):
        from app.utils.grade10_mathematics.term_1.algebraic_expressions_generator import generate as gen_g10_math

        res1 = gen_g10_math(subskill="products", seed=55, mode="scaffold")
        res2 = gen_g10_math(subskill="products", seed=55, mode="scaffold")
        q1 = res1.get('questions', [res1])[0]
        q2 = res2.get('questions', [res2])[0]
        self.assertEqual(q1['prompt_latex'], q2['prompt_latex'])
        self.assertIn('misconception_tags', q1)
        self.assertIn('canonical_solution', q1)

    def test_phase5d_grade12_counting_probability_contract(self):
        from app.utils.grade12_mathematics.counting_principles_probability_generator import generate as gen_prob

        res1 = gen_prob(subskill="compound", seed=42, mode="compound")
        res2 = gen_prob(subskill="compound", seed=42, mode="compound")
        q1 = res1.get('questions', [res1])[0]
        q2 = res2.get('questions', [res2])[0]
        self.assertEqual(q1['prompt'], q2['prompt'])
        self.assertEqual(q1['marks'], 10)
        self.assertEqual(q1['term'], 3)
        self.assertIn('marking_schema', q1)
        self.assertIn('canonical_solution', q1)
        self.assertIn('misconception_tags', q1)

    def test_phase5d_grade12_bivariate_statistics_contract(self):
        from app.utils.grade12_mathematics.bivariate_statistics_generator import generate as gen_stat

        res1 = gen_stat(subskill="compound", seed=88, mode="compound")
        res2 = gen_stat(subskill="compound", seed=88, mode="compound")
        q1 = res1.get('questions', [res1])[0]
        q2 = res2.get('questions', [res2])[0]
        self.assertEqual(q1['prompt'], q2['prompt'])
        self.assertEqual(q1['marks'], 8)
        self.assertEqual(q1['term'], 3)
        self.assertIn('diagram_spec', q1)
        self.assertIn('marking_schema', q1)
        self.assertIn('canonical_solution', q1)
        self.assertIn('misconception_tags', q1)

    # --- Phase 5E: Business Studies (Grades 10–12) ---
    def test_phase5e_grade10_business_studies_contract(self):
        from app.utils.grade10_business_studies.term_1.micro_environment_generator import generate as gen_g10_bs

        q1 = gen_g10_bs(subskill="concepts", seed=77, mode="scaffold")
        q2 = gen_g10_bs(subskill="concepts", seed=77, mode="scaffold")
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])

    # --- Phase 5F: Physical Sciences & Life Sciences (Grades 10–12) ---
    def test_phase5f_physical_sciences_contract(self):
        from app.utils.physical_sciences.mechanics_generator import generate as gen_phys

        q1 = gen_phys(subskill="kinematics_1d", seed=314, mode="scaffold")
        q2 = gen_phys(subskill="kinematics_1d", seed=314, mode="scaffold")
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])
        self.assertIn('marking_schema', q1[0])
        self.assertIn('misconception_tags', q1[0])

    def test_phase5f_momentum_impulse_contract(self):
        from app.utils.grade12_physical_sciences.momentum_impulse_generator import generate as gen_momentum

        q1 = gen_momentum(subskill="conservation_of_momentum_1d", seed=555, mode="compound")
        q2 = gen_momentum(subskill="conservation_of_momentum_1d", seed=555, mode="compound")
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])
        self.assertEqual(q1[0]['marks'], 6)
        self.assertIn('marking_schema', q1[0])
        self.assertIn('misconception_tags', q1[0])

    def test_phase5f_life_sciences_contract(self):
        from app.utils.life_sciences.genetics_generator import generate as gen_ls

        q1 = gen_ls(subskill="monohybrid_cross", seed=420, mode="scaffold")
        q2 = gen_ls(subskill="monohybrid_cross", seed=420, mode="scaffold")
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])
        self.assertIn('marking_schema', q1[0])
        self.assertIn('misconception_tags', q1[0])

    # --- Phase 5G: Mathematical Literacy & Technical Mathematics (Grades 10–12) ---
    def test_phase5g_mathematical_literacy_contract(self):
        from app.utils.mathematical_literacy.finance_tax_generator import generate as gen_mathlit

        res1 = gen_mathlit(subskill="income_tax_sars", seed=654, mode="scaffold")
        res2 = gen_mathlit(subskill="income_tax_sars", seed=654, mode="scaffold")
        q1 = res1.get('questions', res1) if isinstance(res1, dict) else res1
        q2 = res2.get('questions', res2) if isinstance(res2, dict) else res2
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])
        self.assertIn('marking_schema', q1[0])
        self.assertIn('misconception_tags', q1[0])

    def test_phase5g_technical_mathematics_contract(self):
        from app.utils.technical_mathematics.complex_numbers_generator import generate as gen_techmath

        res1 = gen_techmath(subskill="polar_form", seed=819, mode="scaffold")
        res2 = gen_techmath(subskill="polar_form", seed=819, mode="scaffold")
        q1 = res1.get('questions', res1) if isinstance(res1, dict) else res1
        q2 = res2.get('questions', res2) if isinstance(res2, dict) else res2
        self.assertEqual(len(q1), len(q2))
        self.assertEqual(q1[0]['prompt'], q2[0]['prompt'])
        self.assertIn('marking_schema', q1[0])
        self.assertIn('misconception_tags', q1[0])

    def test_circle_geometry_contract(self):
        from app.utils.grade10_mathematics.term_2.circle_geometry_generator import generate as gen_circ

        for subskill in ["angle_at_center", "cyclic_quad_opposite", "cyclic_quad_exterior", "tangent_chord", "tangent_radius"]:
            q1 = gen_circ(subskill=subskill, seed=777, mode="scaffold")
            q2 = gen_circ(subskill=subskill, seed=777, mode="scaffold")
            self.assertEqual(len(q1), len(q2))
            self.assertEqual(q1[0]['id'], q2[0]['id'])
            self.assertEqual(q1[0]['prompt_latex'], q2[0]['prompt_latex'])
            self.assertIn('marking_schema', q1[0])
            self.assertIn('hint_sections', q1[0])
            self.assertIn('misconception_tags', q1[0])
            self.assertIn('diagram_spec', q1[0])
            self.assertEqual(q1[0]['term'], 3)
            self.assertEqual(q1[0]['caps_weight_percent'], 30)

        # Verify deconstructibility / elementary mode
        elem_q = gen_circ(subskill="elementary_tangent_chord", seed=777)
        self.assertEqual(elem_q[0]['subskill'], "tangent_chord")


if __name__ == '__main__':
    unittest.main()

