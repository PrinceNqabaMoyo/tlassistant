"""
Unit Tests for Trial & Subscription Manager (Phase D2)
Tests 14-day countdown calculations, tier permissions, and hard paywall gates.
"""

import unittest
from datetime import datetime, timezone, timedelta

from app.services.trial_manager import (
    compute_trial_status,
    check_feature_access,
    TRIAL_DURATION_DAYS,
)


class TestTrialManager(unittest.TestCase):
    def test_new_user_trial_active(self):
        now = datetime(2026, 9, 20, 12, 0, 0, tzinfo=timezone.utc)
        profile = {
            "subscription_tier": "trial",
            "trial_started_at": now.isoformat(),
            "trial_ends_at": (now + timedelta(days=14)).isoformat(),
        }
        status = compute_trial_status(profile, now=now)
        self.assertEqual(status["tier"], "trial")
        self.assertTrue(status["is_active"])
        self.assertFalse(status["trial_expired"])
        self.assertEqual(status["days_remaining"], 14)
        self.assertTrue(status["permissions"]["modes"] == ["scaffold", "practice"])

    def test_trial_countdown_midway(self):
        now = datetime(2026, 9, 20, 12, 0, 0, tzinfo=timezone.utc)
        started_at = now - timedelta(days=6)
        ends_at = started_at + timedelta(days=14)
        profile = {
            "subscription_tier": "trial",
            "trial_started_at": started_at.isoformat(),
            "trial_ends_at": ends_at.isoformat(),
        }
        status = compute_trial_status(profile, now=now)
        self.assertEqual(status["tier"], "trial")
        self.assertEqual(status["days_remaining"], 8)
        self.assertFalse(status["trial_expired"])

    def test_trial_expired(self):
        now = datetime(2026, 9, 20, 12, 0, 0, tzinfo=timezone.utc)
        started_at = now - timedelta(days=15)
        ends_at = started_at + timedelta(days=14)
        profile = {
            "subscription_tier": "trial",
            "trial_started_at": started_at.isoformat(),
            "trial_ends_at": ends_at.isoformat(),
        }
        status = compute_trial_status(profile, now=now)
        self.assertEqual(status["tier"], "trial_expired")
        self.assertFalse(status["is_active"])
        self.assertTrue(status["trial_expired"])
        self.assertEqual(status["days_remaining"], 0)

        # Feature gate check
        allowed, error_payload = check_feature_access(profile, "practice")
        self.assertFalse(allowed)
        self.assertEqual(error_payload["code"], 403)
        self.assertEqual(error_payload["error"], "TRIAL_EXPIRED")

    def test_subscribed_user_standard(self):
        now = datetime(2026, 9, 20, 12, 0, 0, tzinfo=timezone.utc)
        profile = {
            "subscription_tier": "standard",
            "subscription_ends_at": (now + timedelta(days=25)).isoformat(),
        }
        status = compute_trial_status(profile, now=now)
        self.assertEqual(status["tier"], "standard")
        self.assertTrue(status["is_active"])
        self.assertFalse(status["trial_expired"])
        self.assertEqual(status["days_remaining"], 25)

        # Allows assessment
        allowed, _ = check_feature_access(profile, "assessment")
        self.assertTrue(allowed)

        # Blocks Pro tutor
        allowed, error_payload = check_feature_access(profile, "socratic_agent")
        self.assertFalse(allowed)
        self.assertEqual(error_payload["error"], "PRO_TIER_REQUIRED")

    def test_subscribed_user_pro(self):
        now = datetime(2026, 9, 20, 12, 0, 0, tzinfo=timezone.utc)
        profile = {
            "subscription_tier": "pro",
            "subscription_ends_at": (now + timedelta(days=30)).isoformat(),
        }
        status = compute_trial_status(profile, now=now)
        self.assertEqual(status["tier"], "pro")
        self.assertTrue(status["is_active"])

        # Allows all
        allowed, _ = check_feature_access(profile, "assessment")
        self.assertTrue(allowed)
        allowed, _ = check_feature_access(profile, "socratic_agent")
        self.assertTrue(allowed)

    def test_school_license_validation_and_activation(self):
        from app.services.trial_manager import validate_school_license, activate_school_license

        # Valid format SCH-2026-CAPS-9081
        valid, err, details = validate_school_license("SCH-2026-CAPS-9081")
        self.assertTrue(valid)
        self.assertIsNone(err)
        self.assertEqual(details["tier"], "school")
        self.assertEqual(details["duration_days"], 365)

        # Valid format FUNDILE-SCH-7721
        valid2, err2, details2 = validate_school_license("FUNDILE-SCH-7721")
        self.assertTrue(valid2)
        self.assertIsNone(err2)

        # Invalid format
        invalid, err_msg, _ = validate_school_license("INVALID-CODE-123")
        self.assertFalse(invalid)
        self.assertIn("Invalid school license format", err_msg)

        # Full activation
        profile = {"subscription_tier": "trial"}
        ok, res = activate_school_license(profile, "SCH-2026-CAPS-9081", "Rondebosch Boys High")
        self.assertTrue(ok)
        self.assertEqual(profile["subscription_tier"], "school")
        self.assertEqual(profile["school_name"], "Rondebosch Boys High")
        self.assertEqual(res["status"]["tier"], "school")
        self.assertTrue(res["status"]["permissions"]["allow_teacher_dashboard"])


if __name__ == "__main__":
    unittest.main()

