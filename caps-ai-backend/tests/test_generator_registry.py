"""
Unit tests for Generator Registry completeness and multi-subject variant generation.
"""
import unittest
from app.services.generator_registry import ALL_GENERATORS, generate_variant


class TestGeneratorRegistry(unittest.TestCase):
    def test_registry_size(self):
        """Verify that generator registry contains at least 80 registered subject generators."""
        self.assertGreaterEqual(len(ALL_GENERATORS), 80)

    def test_grade10_accounting_generators(self):
        """Verify Grade 10 Accounting generation."""
        res = generate_variant("grade10_accounting_vat", seed=42)
        self.assertIsInstance(res, list)
        self.assertGreaterEqual(len(res), 1)

    def test_grade11_accounting_generators(self):
        """Verify Grade 11 Accounting generation."""
        res = generate_variant("grade11_accounting_fixed_assets", seed=101)
        self.assertIsInstance(res, list)
        self.assertGreaterEqual(len(res), 1)

    def test_grade12_accounting_generators(self):
        """Verify Grade 12 Accounting generation."""
        res = generate_variant("grade12_accounting_cash_flow", seed=202)
        self.assertIsInstance(res, list)
        self.assertGreaterEqual(len(res), 1)

    def test_grade10_math_generators(self):
        """Verify Grade 10 Mathematics generation."""
        res = generate_variant("grade10_math_trigonometry", seed=77)
        self.assertIsInstance(res, list)
        self.assertGreaterEqual(len(res), 1)

    def test_science_generators(self):
        """Verify Physical & Life Sciences generation."""
        res_mech = generate_variant("physical_sciences_mechanics", seed=12)
        self.assertIsInstance(res_mech, list)
        self.assertGreaterEqual(len(res_mech), 1)

        res_gen = generate_variant("life_sciences_genetics", seed=34)
        self.assertIsInstance(res_gen, list)
        self.assertGreaterEqual(len(res_gen), 1)

    def test_unregistered_topic_raises_error(self):
        """Verify unknown topic raises ValueError."""
        with self.assertRaises(ValueError):
            generate_variant("non_existent_topic_xyz")


if __name__ == "__main__":
    unittest.main()
