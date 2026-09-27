"""
Unit tests for Grade 12 Physical Sciences - Momentum and Impulse Question Generator.
Validates the 6-Pillar Generator Contract:
1. Seed invariance and deterministic execution
2. Compound 6-mark collision questions (1D momentum conservation + elasticity test)
3. Compound 5-mark impulse questions (Newton's 2nd Law in terms of momentum + safety threshold)
4. Elementary sub-drills (elementary_momentum, elementary_change_momentum, elementary_impulse)
5. Marking schema with [M] and [A] marks, unit and direction deductions
6. Central Generator Registry routing and normalization
"""

import sys
import unittest
from pathlib import Path

# Add backend directory to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.utils.grade12_physical_sciences import momentum_impulse_generator as gen
from app.services.generator_registry import generate_variant, resolve_generator_key


class TestMomentumImpulseGenerator(unittest.TestCase):

    def test_seed_invariance(self):
        """Calling generate with identical seeds must produce identical results."""
        q1 = gen.generate(seed=777, count=3)
        q2 = gen.generate(seed=777, count=3)
        
        self.assertEqual(len(q1), len(q2))
        for item1, item2 in zip(q1, q2):
            self.assertEqual(item1["id"], item2["id"])
            self.assertEqual(item1["prompt"], item2["prompt"])
            self.assertEqual(item1["sample_answer"], item2["sample_answer"])
            self.assertEqual(item1["ideal_answer"], item2["ideal_answer"])
            self.assertEqual(item1["marks"], item2["marks"])

    def test_distinct_seeds_produce_variation(self):
        """Different seeds must produce different questions/parameters."""
        q1 = gen.generate(seed=101, count=1)[0]
        q2 = gen.generate(seed=999, count=1)[0]
        self.assertNotEqual(q1["id"], q2["id"])

    def test_compound_collision_contract(self):
        """Compound 6-mark collision questions must satisfy all 6-pillar requirements."""
        questions = gen.generate(subskill="conservation_of_momentum_1d", count=5, seed=123)
        
        for q in questions:
            self.assertEqual(q["marks"], 6)
            self.assertEqual(q["term"], 1)
            self.assertEqual(q["caps_weight_percent"], 15)
            self.assertEqual(q["topic"], "Momentum and Impulse")
            
            # Check marking schema
            schema = q["marking_schema"]
            self.assertEqual(schema["total_marks"], 6)
            self.assertGreaterEqual(len(schema["marking_points"]), 4)
            points_sum = sum(mp["marks"] for mp in schema["marking_points"])
            self.assertEqual(points_sum, 6)
            
            # Verify [M] and [A] descriptors in marking points
            desc_text = " ".join(mp["desc"] for mp in schema["marking_points"])
            self.assertIn("[M]", desc_text)
            self.assertIn("[A]", desc_text)
            
            # Verify deductions
            deduction_rules = [d["rule"] for d in schema.get("deductions", [])]
            self.assertIn("omitted_or_wrong_unit", deduction_rules)
            self.assertIn("omitted_vector_direction", deduction_rules)
            
            # Check 3-tier hints
            hints = q["hints"]
            self.assertIn("tier_1", hints)
            self.assertIn("tier_2", hints)
            self.assertIn("tier_3", hints)
            
            # Check kinetic energy elasticity content
            self.assertTrue(
                "ELASTIC" in q["prompt"] or "elastic" in q["prompt"].lower() or "kinetic energy" in q["prompt"].lower()
            )
            self.assertTrue(
                "ELASTIC" in q["sample_answer"] or "INELASTIC" in q["sample_answer"]
            )

    def test_compound_impulse_contract(self):
        """Compound 5-mark impulse questions must satisfy Newton's 2nd law requirements."""
        questions = gen.generate(subskill="impulse_newton_second_law", count=5, seed=456)
        
        for q in questions:
            self.assertEqual(q["marks"], 5)
            self.assertEqual(q["term"], 1)
            self.assertEqual(q["caps_weight_percent"], 15)
            self.assertEqual(q["topic"], "Momentum and Impulse")
            
            schema = q["marking_schema"]
            self.assertEqual(schema["total_marks"], 5)
            points_sum = sum(mp["marks"] for mp in schema["marking_points"])
            self.assertEqual(points_sum, 5)
            
            # Verify [M] and [A] markers
            desc_text = " ".join(mp["desc"] for mp in schema["marking_points"])
            self.assertIn("[M]", desc_text)
            self.assertIn("[A]", desc_text)
            
            # Check 3-tier hints
            hints = q["hints"]
            self.assertIn("tier_1", hints)
            self.assertIn("tier_2", hints)
            self.assertIn("tier_3", hints)
            
            # Check impulse and force content
            self.assertIn("F_net", q["prompt"])
            self.assertIn("misconception_tags", q)

    def test_elementary_sub_drills(self):
        """Elementary drills must scaffold basic p=mv, delta_p, and impulse calculations."""
        # 1. elementary_momentum (p = mv)
        elem_p = gen.generate(mode="elementary_momentum", count=3, seed=50)[0]
        self.assertEqual(elem_p["marks"], 3)
        self.assertEqual(elem_p["subskill"], "elementary_momentum")
        self.assertIn("p = m v", elem_p["sample_answer"])
        self.assertEqual(elem_p["marking_schema"]["total_marks"], 3)

        # 2. elementary_change_momentum (delta_p = m*delta_v)
        elem_dp = gen.generate(mode="elementary_change_momentum", count=3, seed=60)[0]
        self.assertEqual(elem_dp["marks"], 3)
        self.assertEqual(elem_dp["subskill"], "elementary_change_momentum")
        self.assertIn(r"\Delta p = m(v_f - v_i)", elem_dp["sample_answer"])
        self.assertEqual(elem_dp["marking_schema"]["total_marks"], 3)

        # 3. elementary_impulse (Impulse = F_net * dt)
        elem_imp = gen.generate(mode="elementary_impulse", count=3, seed=70)[0]
        self.assertEqual(elem_imp["marks"], 3)
        self.assertEqual(elem_imp["subskill"], "elementary_impulse")
        self.assertIn(r"F_{\text{net}} \Delta t", elem_imp["sample_answer"])
        self.assertEqual(elem_imp["marking_schema"]["total_marks"], 3)

    def test_registry_integration(self):
        """Generator registry must resolve topic aliases and normalize question results."""
        # 1. Key resolution tests
        self.assertEqual(resolve_generator_key("Momentum and Impulse", grade="12", subject="Physical Sciences"), "physical_sciences_momentum_impulse")
        self.assertEqual(resolve_generator_key("momentum & impulse", grade="12", subject="Physical Sciences"), "physical_sciences_momentum_impulse")
        self.assertEqual(resolve_generator_key("collisions", grade="12", subject="Physical Sciences"), "physical_sciences_momentum_impulse")
        self.assertEqual(resolve_generator_key("conservation of momentum", grade="12", subject="Physical Sciences"), "physical_sciences_momentum_impulse")
        self.assertEqual(resolve_generator_key("impulse", grade="12", subject="Physical Sciences"), "physical_sciences_momentum_impulse")

        # 2. Variant generation via central registry
        res_compound = generate_variant(
            topic="Momentum and Impulse",
            grade="12",
            subject="Physical Sciences",
            count=2,
            seed=42
        )
        self.assertEqual(len(res_compound), 2)
        self.assertEqual(res_compound[0]["term"], 1)
        self.assertEqual(res_compound[0]["caps_weight_percent"], 15)

        # 3. Variant generation for elementary subskills
        res_elem = generate_variant(
            topic="Momentum and Impulse",
            subskill="elementary_momentum",
            grade="12",
            subject="Physical Sciences",
            seed=42
        )
        self.assertEqual(len(res_elem), 1)
        self.assertEqual(res_elem[0]["subskill"], "elementary_momentum")
        self.assertEqual(res_elem[0]["marks"], 3)


if __name__ == "__main__":
    unittest.main()
