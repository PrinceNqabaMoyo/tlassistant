"""
Unit tests for notification_service.py (Phase D5)
"""
import unittest
from app.services import notification_service


class TestNotificationService(unittest.TestCase):
    def test_dispatch_and_get_notifications(self):
        user_id = "test_user_notif_01"
        notif = notification_service.dispatch_notification(
            user_id=user_id,
            title="Test Streak",
            message="Keep up the great work!",
            notif_type="streak_reminder",
        )
        self.assertIsNotNone(notif["id"])
        self.assertEqual(notif["title"], "Test Streak")
        self.assertFalse(notif["read"])

        all_notifs = notification_service.get_user_notifications(user_id)
        self.assertGreaterEqual(len(all_notifs), 1)

    def test_mark_read_and_mark_all_read(self):
        user_id = "test_user_notif_02"
        n1 = notification_service.dispatch_notification(user_id, "N1", "M1")
        n2 = notification_service.dispatch_notification(user_id, "N2", "M2")

        # Mark single
        res = notification_service.mark_notification_read(user_id, n1["id"])
        self.assertTrue(res)

        unread = notification_service.get_user_notifications(user_id, unread_only=True)
        self.assertTrue(all(n["id"] != n1["id"] for n in unread))

        # Mark all
        count = notification_service.mark_all_read(user_id)
        self.assertGreaterEqual(count, 1)
        remaining_unread = notification_service.get_user_notifications(user_id, unread_only=True)
        self.assertEqual(len(remaining_unread), 0)

    def test_whatsapp_parent_digest_formatting(self):
        text = notification_service.format_whatsapp_parent_digest(
            student_name="Thabo Ndlovu",
            subject="Accounting",
            grade="10",
            score=84.5,
            focus_area="VAT Output Calculation",
            streak_days=5,
        )
        self.assertIn("Thabo Ndlovu", text)
        self.assertIn("Grade 10 Accounting", text)
        self.assertIn("84.5%", text)
        self.assertIn("VAT Output Calculation", text)

    def test_whatsapp_class_broadcast_formatting(self):
        text = notification_service.format_whatsapp_class_broadcast(
            teacher_name="Mr. Smith",
            class_name="Grade 10 Accounting 10A",
            announcement="Complete Exercise 3 before Friday.",
            join_code="ACC9B2",
            due_date="Friday 14:00",
        )
        self.assertIn("Mr. Smith", text)
        self.assertIn("ACC9B2", text)
        self.assertIn("Grade 10 Accounting 10A", text)


if __name__ == "__main__":
    unittest.main()
