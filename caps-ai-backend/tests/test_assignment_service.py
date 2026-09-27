import unittest
from app.services.assignment_service import (
    create_assignment,
    get_class_assignments,
    get_student_assignments,
    submit_assignment,
    get_assignment_submissions
)

class TestAssignmentService(unittest.TestCase):
    def test_create_and_get_assignment(self):
        asg = create_assignment(
            class_id="cls_test_grade10",
            teacher_id="tch_001",
            title="Term 2 Trial Run",
            subject="Accounting",
            grade="10",
            topic="Bank Reconciliation",
            question_count=4,
            due_date="2026-09-30"
        )
        self.assertIn("assignment_id", asg)
        self.assertEqual(asg["class_id"], "cls_test_grade10")
        
        class_asgs = get_class_assignments("cls_test_grade10")
        self.assertTrue(any(a["assignment_id"] == asg["assignment_id"] for a in class_asgs))

    def test_student_lifecycle_and_submission(self):
        asg = create_assignment(
            class_id="cls_hw_math",
            teacher_id="tch_002",
            title="Factoring Practice",
            subject="Mathematics",
            grade="10",
            topic="Algebra",
            question_count=5
        )
        asg_id = asg["assignment_id"]

        # 1. Student initially has it pending
        pending = get_student_assignments("student_999", class_ids=["cls_hw_math"])
        target = next((p for p in pending if p["assignment_id"] == asg_id), None)
        self.assertIsNotNone(target)
        self.assertFalse(target["is_submitted"])
        self.assertEqual(target["status"], "pending")

        # 2. Student submits assignment
        sub_res = submit_assignment(asg_id, "student_999", "Thabo N.", 90)
        self.assertTrue(sub_res["recorded"])
        self.assertEqual(sub_res["submission"]["score"], 90)

        # 3. Mark book has submission
        subs = get_assignment_submissions(asg_id)
        self.assertEqual(len(subs), 1)
        self.assertEqual(subs[0]["student_id"], "student_999")

        # 4. Student now sees it completed
        completed = get_student_assignments("student_999", class_ids=["cls_hw_math"])
        target_done = next((p for p in completed if p["assignment_id"] == asg_id), None)
        self.assertTrue(target_done["is_submitted"])
        self.assertEqual(target_done["score"], 90)

if __name__ == "__main__":
    unittest.main()
