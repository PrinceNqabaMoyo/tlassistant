"""Unit tests for South African Naming & Enterprise Generation Engine.

Verifies:
1. Deterministic repeatability with seeded PRNG.
2. Statistical demographic proportionality across ethnic groups.
3. Complete 9-province geographic coverage with regional towns and sectors.
4. Enterprise forms and legal suffixes.
5. Blacklist enforcement (zero verbatim past exam or real commercial brands).
6. Backward compatibility with existing generators.
"""
import random
import sys
from collections import Counter
from pathlib import Path
import unittest

# Ensure caps-ai-backend is on python path
BACKEND_DIR = Path(__file__).resolve().parent.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.utils.sa_naming_engine import (
    DEMOGRAPHIC_WEIGHTS,
    PROVINCES_AND_HUBS,
    BLACK_LISTED_VERBATIM_NAMES,
    generate_sa_person,
    generate_sa_enterprise,
    pick_demographic_group,
    pick_person_name,
    pick_person_names,
    pick_business_name,
    pick_business_names,
    pick_sa_scenario,
    pick_surname,
)


class TestSaNamingEngine(unittest.TestCase):
    def test_deterministic_repeatability(self):
        """Identical seeds must produce byte-identical person and enterprise outputs."""
        r1 = random.Random(42)
        r2 = random.Random(42)

        p1 = generate_sa_person(r1)
        p2 = generate_sa_person(r2)
        self.assertEqual(p1, p2, "generate_sa_person must be strictly deterministic with same seed")

        e1 = generate_sa_enterprise(r1)
        e2 = generate_sa_enterprise(r2)
        self.assertEqual(e1, e2, "generate_sa_enterprise must be strictly deterministic with same seed")

    def test_distinct_seeds_produce_variation(self):
        """Different seeds must yield distinct characters and enterprises."""
        r1 = random.Random(101)
        r2 = random.Random(202)

        p1 = generate_sa_person(r1)
        p2 = generate_sa_person(r2)
        self.assertTrue(p1["full_name"] != p2["full_name"] or p1["ethnic_group"] != p2["ethnic_group"])

    def test_demographic_proportionality(self):
        """Verify that sampling 10,000 individuals statistically adheres to SA demographic weights."""
        r = random.Random(999)
        n_samples = 10000
        counts = Counter()

        for _ in range(n_samples):
            person = generate_sa_person(r)
            counts[person["ethnic_group"]] += 1

        # Check that proportions fall within acceptable confidence bounds (tolerance +/- 3.5%)
        expected_weights = dict(DEMOGRAPHIC_WEIGHTS)
        for group, expected_prop in expected_weights.items():
            actual_prop = counts[group] / n_samples
            self.assertLess(
                abs(actual_prop - expected_prop),
                0.035,
                f"Demographic group '{group}' actual proportion {actual_prop:.4f} "
                f"diverges from expected {expected_prop:.4f} beyond tolerance"
            )

    def test_nine_provinces_geographic_coverage(self):
        """Verify all 9 provinces are represented with realistic municipal hubs."""
        r = random.Random(777)
        provinces_seen = set()
        towns_seen = set()

        for _ in range(300):
            ent = generate_sa_enterprise(r)
            provinces_seen.add(ent["province"])
            towns_seen.add(ent["town"])

        expected_provinces = set(PROVINCES_AND_HUBS.keys())
        self.assertEqual(provinces_seen, expected_provinces)
        self.assertGreaterEqual(len(towns_seen), 30)

    def test_enterprise_forms_and_legal_suffixes(self):
        """Verify all South African enterprise forms and legal suffixes are supported."""
        r = random.Random(555)
        forms_seen = set()

        for _ in range(200):
            ent = generate_sa_enterprise(r)
            forms_seen.add(ent["form"])
            if ent["form"] == "Private Company":
                self.assertIn("(Pty) Ltd", ent["business_name"])
            elif ent["form"] == "Close Corporation":
                self.assertIn("CC", ent["business_name"])
            elif ent["form"] == "Public Company":
                self.assertIn("Ltd", ent["business_name"])

        self.assertIn("Sole Trader", forms_seen)
        self.assertIn("Partnership", forms_seen)
        self.assertIn("Private Company", forms_seen)
        self.assertIn("Close Corporation", forms_seen)

    def test_blacklist_exclusion(self):
        """Verify zero overlap with blacklisted past-paper or real commercial entities."""
        r = random.Random(12345)
        for _ in range(1000):
            b_name = pick_business_name(r).lower()
            for forbidden in BLACK_LISTED_VERBATIM_NAMES:
                self.assertNotEqual(forbidden, b_name, f"Forbidden brand name '{forbidden}' was generated!")

    def test_legacy_drop_in_compatibility(self):
        """Verify drop-in compatibility functions conform to expected contracts."""
        r = random.Random(888)

        scenario = pick_sa_scenario(r)
        self.assertIn("business", scenario)
        self.assertIn("owner", scenario)
        self.assertIn("industry", scenario)
        self.assertIn("town", scenario)
        self.assertIn("province", scenario)
        self.assertGreater(len(scenario["business"]), 0)

        people = pick_person_names(r, k=5)
        self.assertEqual(len(people), 5)
        self.assertEqual(len(set(people)), 5)  # All unique

        businesses = pick_business_names(r, k=4)
        self.assertEqual(len(businesses), 4)
        self.assertEqual(len(set(businesses)), 4)  # All unique

        surname = pick_surname(r)
        self.assertIsInstance(surname, str)
        self.assertGreater(len(surname), 1)


if __name__ == "__main__":
    unittest.main()
