"""
Unit Tests for SAMO Olympiad Leaderboard Service (Layer F)
"""

import unittest
from app.services import leaderboard_service


class TestLeaderboardService(unittest.TestCase):
    def setUp(self):
        # Reset sample entries
        leaderboard_service._LEADERBOARD_STORE = {
            e["user_id"]: dict(e) for e in leaderboard_service.DEFAULT_LEADERBOARD_ENTRIES
        }

    def test_default_leaderboard_retrieval(self):
        """Verify fetching unconstrained leaderboard returns top learners."""
        res = leaderboard_service.get_leaderboard(division="all", province="all")
        self.assertTrue(res["success"])
        self.assertGreater(len(res["leaderboard"]), 0)
        # Verify sorted by rank
        ranks = [e["rank"] for e in res["leaderboard"]]
        self.assertEqual(ranks, sorted(ranks))

    def test_division_filtering(self):
        """Verify Junior vs Senior division filtering."""
        res_junior = leaderboard_service.get_leaderboard(division="junior")
        self.assertTrue(res_junior["success"])
        for e in res_junior["leaderboard"]:
            self.assertEqual(e["division"], "Junior")

        res_senior = leaderboard_service.get_leaderboard(division="senior")
        self.assertTrue(res_senior["success"])
        for e in res_senior["leaderboard"]:
            self.assertEqual(e["division"], "Senior")

    def test_province_filtering(self):
        """Verify filtering by South African province."""
        res_gp = leaderboard_service.get_leaderboard(province="Gauteng")
        self.assertTrue(res_gp["success"])
        for e in res_gp["leaderboard"]:
            self.assertEqual(e["province"], "Gauteng")

    def test_user_update_and_opt_out(self):
        """Verify updating a learner score and toggling opt-in privacy."""
        user_id = "test_learner_42"
        entry = leaderboard_service.update_user_leaderboard_entry(
            user_id=user_id,
            name="Thabo Ndlovu",
            school="Pretoria Boys High",
            province="Gauteng",
            division="Senior",
            score=94,
            solved=52,
            is_opted_in=True
        )
        self.assertEqual(entry["initials"], "TN")
        self.assertEqual(entry["tier"], "Top 5%")

        # Check in leaderboard
        res = leaderboard_service.get_leaderboard(current_user_id=user_id)
        user_standing = res["current_user_standing"]
        self.assertIsNotNone(user_standing)
        self.assertEqual(user_standing["score"], 94)

        # Opt out
        opt_res = leaderboard_service.set_user_opt_in_status(user_id, False)
        self.assertTrue(opt_res)

        # Other users should not see the opted-out user
        res_public = leaderboard_service.get_leaderboard(current_user_id="other_user")
        public_ids = [e["user_id"] for e in res_public["leaderboard"]]
        self.assertNotIn(user_id, public_ids)


if __name__ == "__main__":
    unittest.main()
