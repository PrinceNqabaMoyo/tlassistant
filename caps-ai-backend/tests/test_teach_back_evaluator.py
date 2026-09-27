import unittest
from app.services.teach_back_evaluator import evaluate_teach_back

class TestTeachBackEvaluator(unittest.TestCase):
    def test_accounting_crj_debit_mastery(self):
        explanation = "Bank is an asset of the business, and whenever money is received, assets increase on the debit side."
        res = evaluate_teach_back(
            subject="Accounting",
            topic="Cash Receipts Journal",
            subskill="Bank Debit Posting",
            student_explanation=explanation,
            misconception_tag="debit_credit_inversion"
        )
        self.assertTrue(res["is_mastered"])
        self.assertEqual(res["status"], "mastered")
        self.assertEqual(res["xp_awarded"], 25)

    def test_accounting_vat_misconception_trap(self):
        explanation = "We keep the VAT because VAT is income and profit for the business."
        res = evaluate_teach_back(
            subject="Accounting",
            topic="VAT Calculation",
            subskill="Net vs Gross",
            student_explanation=explanation,
            misconception_tag="net_vs_gross_vat"
        )
        self.assertFalse(res["is_mastered"])
        self.assertEqual(res["status"], "misconception_detected")
        self.assertIn("Watch out for a common trap", res["socratic_feedback"])

    def test_math_inequality_division_mastery(self):
        explanation = "When dividing by a negative number, you must reverse the inequality sign because numbers switch direction on the number line."
        res = evaluate_teach_back(
            subject="Mathematics",
            topic="Inequalities",
            subskill="Division by negative",
            student_explanation=explanation,
            misconception_tag="inequality_division_negative"
        )
        self.assertTrue(res["is_mastered"])
        self.assertEqual(res["status"], "mastered")
        self.assertIn("reverse", res["socratic_feedback"].lower())

    def test_brief_explanation_handling(self):
        res = evaluate_teach_back(
            subject="Mathematics",
            topic="Inequalities",
            subskill="Rules",
            student_explanation="flip sign",
            misconception_tag="inequality_division_negative"
        )
        self.assertFalse(res["is_mastered"])
        self.assertEqual(res["status"], "partial")

if __name__ == "__main__":
    unittest.main()
