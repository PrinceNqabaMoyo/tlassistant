"""
Challenge Generator & Canonical Assessment Engine (Layer E)
Manages canonical challenge seeds, topic milestone challenges, and term tests.
Ensures every student faces an identical, reproducible, standardized assessment
to earn certified Topic Medals and Term Trophies.
"""

from typing import Dict, Any, List, Optional


CANONICAL_CHALLENGES: Dict[str, Dict[str, Any]] = {
    # 1. Mathematics Grade 10
    "mathematics_10_algebraic_expressions": {
        "id": "mathematics_10_algebraic_expressions",
        "title": "Algebraic Expressions Topic Challenge",
        "subject": "Mathematics",
        "grade": "10",
        "term": 1,
        "seed": 101,
        "duration_mins": 15,
        "total_marks": 15,
        "passing_score": 0.80,
        "archetype": "algebraic_expressions",
        "questions": [
            {
                "id": "q1",
                "question_text": "Expand and simplify the binomial product: (2x - 3)(3x + 4)",
                "marks": 4,
                "solution": "6x^2 + 8x - 9x - 12 = 6x^2 - x - 12",
                "type": "math_symbolic"
            },
            {
                "id": "q2",
                "question_text": "Factorise completely by grouping: 3ax - 6ay + 2bx - 4by",
                "marks": 4,
                "solution": "3a(x - 2y) + 2b(x - 2y) = (3a + 2b)(x - 2y)",
                "type": "math_symbolic"
            },
            {
                "id": "q3",
                "question_text": "Factorise the quadratic trinomial: x^2 - 7x + 12",
                "marks": 3,
                "solution": "(x - 3)(x - 4)",
                "type": "math_symbolic"
            },
            {
                "id": "q4",
                "question_text": "Simplify without a calculator: (x^2 - 9)/(2x + 6)",
                "marks": 4,
                "solution": "[(x - 3)(x + 3)] / [2(x + 3)] = (x - 3)/2",
                "type": "math_symbolic"
            }
        ]
    },

    "mathematics_10_equations_inequalities": {
        "id": "mathematics_10_equations_inequalities",
        "title": "Equations & Inequalities Challenge",
        "subject": "Mathematics",
        "grade": "10",
        "term": 1,
        "seed": 102,
        "duration_mins": 15,
        "total_marks": 15,
        "passing_score": 0.80,
        "archetype": "equations_inequalities",
        "questions": [
            {
                "id": "q1",
                "question_text": "Solve for x: 3(x - 2) + 5 = 2(2x + 1)",
                "marks": 4,
                "solution": "3x - 6 + 5 = 4x + 2 => 3x - 1 = 4x + 2 => -x = 3 => x = -3",
                "type": "math_symbolic"
            },
            {
                "id": "q2",
                "question_text": "Solve the quadratic equation: x^2 - 5x - 6 = 0",
                "marks": 4,
                "solution": "(x - 6)(x + 1) = 0 => x = 6 or x = -1",
                "type": "math_symbolic"
            },
            {
                "id": "q3",
                "question_text": "Solve the linear inequality and represent on a number line: -2x + 4 <= 10",
                "marks": 4,
                "solution": "-2x <= 6 => x >= -3 (sign reverses when dividing by negative)",
                "type": "math_symbolic"
            },
            {
                "id": "q4",
                "question_text": "Solve simultaneous equations: x + y = 7 and 2x - y = 8",
                "marks": 3,
                "solution": "Adding: 3x = 15 => x = 5. Substituting: y = 2.",
                "type": "math_symbolic"
            }
        ]
    },

    # 2. Accounting Grade 10
    "accounting_10_sole_trader_crj": {
        "id": "accounting_10_sole_trader_crj",
        "title": "Cash Receipts Journal (15% VAT) Challenge",
        "subject": "Accounting",
        "grade": "10",
        "term": 1,
        "seed": 201,
        "duration_mins": 15,
        "total_marks": 12,
        "passing_score": 0.80,
        "archetype": "crj_vat",
        "questions": [
            {
                "id": "q1",
                "question_text": "Record Day 4: Cash sales of merchandise per CRT R2,300 (VAT inclusive). Cost of sales R1,600.",
                "marks": 4,
                "solution": "Bank: R2,300 | Sales: R2,000 | Output VAT: R300 | Cost of Sales: R1,600",
                "type": "journal_entry"
            },
            {
                "id": "q2",
                "question_text": "Record Day 11: Received R1,500 cash from tenant for monthly rent. Issue Receipt 45.",
                "marks": 4,
                "solution": "Details: Rent Income | Bank: R1,500 | Sundry Accounts: R1,500 (Rent Income)",
                "type": "journal_entry"
            },
            {
                "id": "q3",
                "question_text": "Record Day 18: Owner deposited R10,000 direct capital contribution into business bank account.",
                "marks": 4,
                "solution": "Details: Capital | Bank: R10,000 | Sundry Accounts: R10,000 (Capital)",
                "type": "journal_entry"
            }
        ]
    },

    # 3. Physical Sciences Grade 10
    "physical_sciences_10_mechanics_kinematics": {
        "id": "physical_sciences_10_mechanics_kinematics",
        "title": "1D Motion & Kinematics Challenge",
        "subject": "Physical Sciences",
        "grade": "10",
        "term": 1,
        "seed": 301,
        "duration_mins": 15,
        "total_marks": 15,
        "passing_score": 0.80,
        "archetype": "kinematics",
        "questions": [
            {
                "id": "q1",
                "question_text": "A vehicle accelerates uniformly from 5 m/s to 25 m/s over 10 seconds. Calculate acceleration.",
                "marks": 4,
                "solution": "a = (vf - vi) / delta_t = (25 - 5) / 10 = 2.0 m/s^2",
                "type": "physics_numeric"
            },
            {
                "id": "q2",
                "question_text": "Calculate the total displacement of the vehicle during these 10 seconds.",
                "marks": 5,
                "solution": "delta_x = vi*t + 0.5*a*t^2 = 5(10) + 0.5(2)(100) = 50 + 100 = 150 m",
                "type": "physics_numeric"
            },
            {
                "id": "q3",
                "question_text": "A stone is dropped from a cliff and hits the ground 3 seconds later. Calculate cliff height (g = 9.8 m/s^2).",
                "marks": 6,
                "solution": "delta_y = 0 + 0.5(9.8)(3^2) = 0.5(9.8)(9) = 44.1 m",
                "type": "physics_numeric"
            }
        ]
    },

    # 4. Life Sciences Grade 10
    "life_sciences_10_genetics": {
        "id": "life_sciences_10_genetics",
        "title": "Monohybrid Crosses & Punnett Squares Challenge",
        "subject": "Life Sciences",
        "grade": "10",
        "term": 1,
        "seed": 401,
        "duration_mins": 15,
        "total_marks": 15,
        "passing_score": 0.80,
        "archetype": "genetics",
        "questions": [
            {
                "id": "q1",
                "question_text": "Define the terms 'Heterozygous' and 'Phenotype' according to CAPS curriculum.",
                "marks": 4,
                "solution": "Heterozygous: possessing two different alleles for a gene. Phenotype: physical observable manifestation of a genetic trait.",
                "type": "rubric_text"
            },
            {
                "id": "q2",
                "question_text": "A heterozygous purple pea plant (Pp) is crossed with a white plant (pp). Complete the Punnett cross and determine offspring phenotypic ratio.",
                "marks": 6,
                "solution": "Gametes: P, p cross p, p => Offspring: 50% Pp (Purple), 50% pp (White). Ratio: 1:1.",
                "type": "punnett_cross"
            },
            {
                "id": "q3",
                "question_text": "What is the probability of having a white-flowered offspring from this cross?",
                "marks": 5,
                "solution": "2 out of 4 squares = 50% or 0.5 probability.",
                "type": "numeric"
            }
        ]
    }
}


# Pre-defined South African CAPS Curriculum Trees for Visual ProgressMap
CURRICULUM_TREES: Dict[str, Dict[str, Any]] = {
    "Mathematics": {
        "10": {
            "terms": [
                {
                    "term": 1,
                    "name": "Term 1: Algebraic Foundations",
                    "nodes": [
                        {
                            "id": "alg_exp",
                            "title": "Algebraic Expressions",
                            "subskills": ["Products (FOIL)", "Common Factors", "Difference of Squares", "Quadratic Trinomials"],
                            "challenge_id": "mathematics_10_algebraic_expressions",
                            "status": "mastered",
                            "mastery_score": 92,
                            "medal": "gold",
                            "prerequisites": []
                        },
                        {
                            "id": "eq_ineq",
                            "title": "Equations & Inequalities",
                            "subskills": ["Linear Equations", "Quadratic Equations", "Simultaneous Equations", "Linear Inequalities"],
                            "challenge_id": "mathematics_10_equations_inequalities",
                            "status": "unlocked",
                            "mastery_score": 74,
                            "medal": "bronze",
                            "prerequisites": ["alg_exp"]
                        },
                        {
                            "id": "trig_1",
                            "title": "Trigonometry Basics",
                            "subskills": ["Right-Angled Triangle Ratios", "Definitions (sin, cos, tan)", "Special Angles (30, 45, 60)", "Two-Dimensional Problems"],
                            "challenge_id": "mathematics_10_trigonometry",
                            "status": "unlocked",
                            "mastery_score": 62,
                            "medal": None,
                            "prerequisites": ["eq_ineq"]
                        },
                        {
                            "id": "term_1_exam",
                            "title": "Term 1 Milestone Exam",
                            "subskills": ["All Term 1 Topics"],
                            "challenge_id": "mathematics_10_term_1",
                            "status": "locked",
                            "mastery_score": 0,
                            "medal": None,
                            "is_term_trophy": True,
                            "prerequisites": ["trig_1"]
                        }
                    ]
                },
                {
                    "term": 2,
                    "name": "Term 2: Functions & Analytical Geometry",
                    "nodes": [
                        {
                            "id": "functions_linear",
                            "title": "Functions: Straight Line & Parabola",
                            "subskills": ["Gradient", "Axis Intercepts", "Turning Point", "Domain & Range"],
                            "status": "locked",
                            "mastery_score": 0,
                            "prerequisites": ["term_1_exam"]
                        },
                        {
                            "id": "analytical_geom",
                            "title": "Analytical Geometry",
                            "subskills": ["Distance Formula", "Midpoint Formula", "Gradient of Line"],
                            "status": "locked",
                            "mastery_score": 0,
                            "prerequisites": ["functions_linear"]
                        }
                    ]
                }
            ]
        }
    },

    "Accounting": {
        "10": {
            "terms": [
                {
                    "term": 1,
                    "name": "Term 1: Sole Trader Accounting Cycle",
                    "nodes": [
                        {
                            "id": "crj_vat",
                            "title": "Cash Receipts Journal & 15% VAT",
                            "subskills": ["Cash Sales", "Output VAT 15%", "Cost of Sales", "Sundry Accounts"],
                            "challenge_id": "accounting_10_sole_trader_crj",
                            "status": "mastered",
                            "mastery_score": 88,
                            "medal": "silver",
                            "prerequisites": []
                        },
                        {
                            "id": "cpj_vat",
                            "title": "Cash Payments Journal",
                            "subskills": ["Cheque/EFT Payments", "Trading Stock Purchases", "Input VAT", "Sundry Expenses"],
                            "status": "unlocked",
                            "mastery_score": 70,
                            "medal": "bronze",
                            "prerequisites": ["crj_vat"]
                        },
                        {
                            "id": "gl_posting",
                            "title": "General Ledger Accounts",
                            "subskills": ["Posting from CRJ/CPJ", "Balancing Accounts", "Trial Balance Extraction"],
                            "status": "unlocked",
                            "mastery_score": 60,
                            "medal": None,
                            "prerequisites": ["cpj_vat"]
                        },
                        {
                            "id": "term_1_acct_exam",
                            "title": "Term 1 Sole Trader Trophy Exam",
                            "subskills": ["Full CRJ, CPJ, General Ledger"],
                            "status": "locked",
                            "mastery_score": 0,
                            "is_term_trophy": True,
                            "prerequisites": ["gl_posting"]
                        }
                    ]
                }
            ]
        }
    }
}


def get_canonical_challenge(challenge_key: str) -> Optional[Dict[str, Any]]:
    """Returns the standardized challenge payload with questions and pass criteria."""
    if challenge_key in CANONICAL_CHALLENGES:
        return CANONICAL_CHALLENGES[challenge_key]
    return CANONICAL_CHALLENGES["mathematics_10_algebraic_expressions"]


def evaluate_challenge_submission(challenge_key: str, score_percentage: float) -> Dict[str, Any]:
    """
    Evaluates a completed challenge and awards credentials deterministically.
    Score >= 95% -> Gold Medal (+350 XP)
    Score >= 80% -> Silver Medal (+200 XP)
    Score >= 60% -> Bronze Medal (+100 XP)
    """
    passed = score_percentage >= 0.60
    medal_grade = None
    xp_awarded = 0

    if score_percentage >= 0.95:
        medal_grade = "gold"
        xp_awarded = 350
    elif score_percentage >= 0.80:
        medal_grade = "silver"
        xp_awarded = 200
    elif score_percentage >= 0.60:
        medal_grade = "bronze"
        xp_awarded = 100

    return {
        "passed": passed,
        "score_percentage": round(score_percentage * 100, 1),
        "medal_grade": medal_grade,
        "xp_awarded": xp_awarded,
        "feedback": (
            f"Outstanding mastery! You earned the {medal_grade.title()} Medal and +{xp_awarded} Ungameable XP."
            if passed
            else "You scored below the 60% credential threshold. Review prerequisites and reattempt."
        )
    }


def get_curriculum_tree(subject: str, grade: str = "10") -> Dict[str, Any]:
    """Retrieves the visual skill tree for a given subject and grade."""
    subj_data = CURRICULUM_TREES.get(subject, CURRICULUM_TREES["Mathematics"])
    grade_data = subj_data.get(grade, subj_data.get("10", {}))
    return grade_data
