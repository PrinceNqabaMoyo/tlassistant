"""
Unit tests for Olympiad Generator and Service (Layer F)
"""
import unittest
from app.utils.olympiad.olympiad_generator import generate_olympiad_problem
from app.services import olympiad_service


class TestOlympiadService(unittest.TestCase):
    def test_olympiad_number_theory_generation(self):
        prob = generate_olympiad_problem(category="number_theory", seed=42)
        self.assertIn("samo_", prob["id"])
        self.assertEqual(prob["category"], "number_theory")
        self.assertEqual(len(prob["options"]), 5)
        self.assertIn(prob["correct_index"], range(5))
        self.assertIn("hint", prob)
        self.assertGreaterEqual(len(prob["solution_steps"]), 1)

    def test_olympiad_combinatorics_generation(self):
        prob = generate_olympiad_problem(category="combinatorics", seed=77)
        self.assertEqual(prob["category"], "combinatorics")
        self.assertEqual(len(prob["options"]), 5)

    def test_olympiad_geometry_generation(self):
        prob = generate_olympiad_problem(category="geometry", seed=88)
        self.assertEqual(prob["category"], "geometry")
        self.assertEqual(len(prob["options"]), 5)

    def test_olympiad_algebra_generation(self):
        prob = generate_olympiad_problem(category="algebra", seed=99)
        self.assertEqual(prob["category"], "algebra")
        self.assertEqual(len(prob["options"]), 5)

    def test_caps_mastery_gate(self):
        # Qualified user
        res_unlocked = olympiad_service.check_caps_mastery_gate("user_1", ["topic_medal_silver_trig"])
        self.assertTrue(res_unlocked["unlocked"])

        # Unqualified user
        res_locked = olympiad_service.check_caps_mastery_gate("user_2", ["topic_medal_bronze_accounting"])
        self.assertFalse(res_locked["unlocked"])

    def test_submit_answer_scoring(self):
        user_id = "user_olympiad_test"
        # Correct answer
        res_correct = olympiad_service.submit_answer(user_id, "p_1", selected_index=2, correct_index=2)
        self.assertTrue(res_correct["is_correct"])
        self.assertEqual(res_correct["xp_awarded"], 100)

        # Incorrect answer
        res_wrong = olympiad_service.submit_answer(user_id, "p_2", selected_index=1, correct_index=3)
        self.assertFalse(res_wrong["is_correct"])
        self.assertEqual(res_wrong["xp_awarded"], 10)

    def test_technique_library_retrieval(self):
        techs = olympiad_service.get_technique_library()
        self.assertGreaterEqual(len(techs), 4)
        tech_ids = [t["id"] for t in techs]
        self.assertIn("tech_pigeonhole", tech_ids)
        self.assertIn("tech_modular_arithmetic", tech_ids)


if __name__ == "__main__":
    unittest.main()
