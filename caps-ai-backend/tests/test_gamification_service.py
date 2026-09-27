"""
Unit Tests for Gamification Service & Challenge Gate Attempt Engine (Layer E)
"""

import unittest
from app.services import gamification_service


class TestGamificationService(unittest.TestCase):
    def test_calculate_gamification_state_basic(self):
        """Verify baseline gamification calculation without cheating/inflation."""
        profile = {"earned_badges": [], "xp_ledger": {}}
        mastery = {"quadratic_factoring": 0.85, "foil_expansion": 0.90}
        state = gamification_service.calculate_gamification_state(
            student_profile=profile,
            subject="Mathematics",
            mastery_snapshot=mastery,
            completed_topics=["algebraic_expressions"],
            term=1
        )
        self.assertGreater(state["total_ungameable_xp"], 0)
        self.assertGreaterEqual(state["level"], 1)
        self.assertEqual(state["subskills_mastered_count"], 2)

    def test_record_challenge_attempt_success_and_medal(self):
        """Verify challenge gate attempt earns Gold medal at 95% and awards XP once."""
        profile = {"earned_badges": [], "xp_ledger": {}}
        res = gamification_service.record_challenge_attempt(
            student_profile=profile,
            challenge_id="ch_alg_01",
            subject="Mathematics",
            topic_id="algebraic_expressions",
            score=19,
            total_marks=20
        )
        self.assertTrue(res["passed"])
        self.assertEqual(res["medal_awarded"], "gold")
        self.assertEqual(res["xp_earned"], 350)
        self.assertIsNotNone(res["new_badge"])
        self.assertEqual(res["new_badge"]["grade"], "gold")

        # Second attempt should not duplicate XP or badge
        res_repeat = gamification_service.record_challenge_attempt(
            student_profile=profile,
            challenge_id="ch_alg_01",
            subject="Mathematics",
            topic_id="algebraic_expressions",
            score=20,
            total_marks=20
        )
        self.assertTrue(res_repeat["passed"])
        self.assertEqual(res_repeat["xp_earned"], 0)  # Ungameable: zero inflation on repeat
        self.assertIsNone(res_repeat["new_badge"])

    def test_record_challenge_attempt_failure(self):
        """Verify failing score does not earn medal or XP."""
        profile = {"earned_badges": [], "xp_ledger": {}}
        res = gamification_service.record_challenge_attempt(
            student_profile=profile,
            challenge_id="ch_alg_02",
            subject="Mathematics",
            topic_id="algebraic_expressions",
            score=8,
            total_marks=20
        )
        self.assertFalse(res["passed"])
        self.assertIsNone(res["medal_awarded"])
        self.assertEqual(res["xp_earned"], 0)

    def test_archive_academic_year(self):
        """Verify grade year rollover archives credentials into longitudinal portfolio."""
        profile = {
            "current_grade": "9",
            "earned_badges": [{"id": "medal_math_alg", "title": "Algebra Silver Medal"}],
            "total_ungameable_xp": 1450,
            "academic_portfolio": {}
        }
        res = gamification_service.archive_academic_year(
            student_profile=profile,
            completed_year=2025,
            completed_grade="9",
            next_grade="10"
        )
        self.assertTrue(res["success"])
        self.assertEqual(profile["current_grade"], "10")
        self.assertIn("2025", profile["academic_portfolio"])
        archived_year = profile["academic_portfolio"]["2025"]
        self.assertEqual(archived_year["grade"], "9")
        self.assertEqual(len(archived_year["badges"]), 1)
        self.assertEqual(archived_year["xp_accumulated"], 1450)


if __name__ == "__main__":
    unittest.main()
