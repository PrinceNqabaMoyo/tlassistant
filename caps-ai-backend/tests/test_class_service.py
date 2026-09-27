"""
Unit Tests for Teacher LMS Cockpit & Class Service (Phase D4)
Tests 6-character join code generation, class creation, and student enrollment.
"""

import unittest
from app.services.class_service import (
    generate_join_code,
    create_class,
    join_class_by_code,
    list_classes_for_teacher,
    get_class_roster,
)


class TestClassService(unittest.TestCase):
    def test_join_code_format(self):
        code = generate_join_code("Mathematics")
        self.assertEqual(len(code), 6)
        self.assertTrue(code.isupper() or code.isalnum())
        # Ensure ambiguous chars are excluded
        for bad_char in ["0", "O", "1", "I", "L"]:
            self.assertNotIn(bad_char, code)

    def test_create_and_join_class_flow(self):
        teacher_id = "tch_test_101"
        teacher_name = "Mr. Sithole"
        class_name = "Grade 10 Mathematics Alpha"
        
        # 1. Teacher creates class
        created = create_class(
            teacher_id=teacher_id,
            teacher_name=teacher_name,
            class_name=class_name,
            subject="Mathematics",
            grade="10",
        )
        self.assertIn("classId", created)
        self.assertEqual(len(created["joinCode"]), 6)
        join_code = created["joinCode"]

        # 2. Student joins by code
        student_id = "std_lerato_202"
        student_name = "Lerato Dlamini"
        success, res = join_class_by_code(
            student_id=student_id,
            student_name=student_name,
            join_code=join_code,
        )
        self.assertTrue(success)
        self.assertFalse(res["already_enrolled"])
        self.assertEqual(res["class"]["studentCount"], 1)

        # 3. Student re-joins (idempotency check)
        success2, res2 = join_class_by_code(
            student_id=student_id,
            student_name=student_name,
            join_code=join_code.lower(), # case-insensitive test
        )
        self.assertTrue(success2)
        self.assertTrue(res2["already_enrolled"])

        # 4. Invalid join code
        bad_success, bad_res = join_class_by_code(
            student_id="std_303",
            student_name="Thabo",
            join_code="ZZZZZZ",
        )
        self.assertFalse(bad_success)
        self.assertEqual(bad_res["error"], "INVALID_JOIN_CODE")

        # 5. Teacher lists classes
        teacher_classes = list_classes_for_teacher(teacher_id)
        self.assertTrue(len(teacher_classes) >= 1)
        self.assertEqual(teacher_classes[0]["classId"], created["classId"])

        # 6. Get roster
        roster = get_class_roster(created["classId"])
        self.assertIsNotNone(roster)
        self.assertEqual(roster["studentCount"], 1)
        self.assertEqual(roster["students"][0]["studentName"], "Lerato Dlamini")


if __name__ == "__main__":
    unittest.main()
