"""
Grade 7 Mathematics - Algebraic Expressions and Equations Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.

Topics Covered (Grade 7 Term 2):
- Algebraic language: variables, constants, coefficients, and terms
- Translating verbal descriptions into algebraic expressions
- Evaluating expressions by numerical substitution
- Solving basic linear equations by inspection and inverse operations
"""

from __future__ import annotations
import random
from typing import Any, Dict, List, Optional
import sympy as sp


def _generate_verbal_translation_question(rng: random.Random) -> Dict[str, Any]:
    """Translates verbal statements into algebraic expressions."""
    var = rng.choice(["x", "y", "m", "n", "p"])
    coef = rng.randint(2, 6)
    const = rng.randint(3, 12)
    operation = rng.choice(["add", "subtract", "divide"])

    if operation == "add":
        phrase = f"Write an algebraic expression for: **Add {const} to {coef} times a number {var}**."
        expr_latex = f"{coef}{var} + {const}"
        expr_str = f"{coef}*{var} + {const}"
        sol = f"**Step 1:** '{coef} times a number {var}' is written as ${coef}{var}$.\n\n**Step 2:** 'Add {const}' means $+ {const}$.\n\n$$\\therefore {expr_latex}$$"
    elif operation == "subtract":
        phrase = f"Write an algebraic expression for: **Subtract {const} from {coef} times a number {var}**."
        expr_latex = f"{coef}{var} - {const}"
        expr_str = f"{coef}*{var} - {const}"
        sol = f"**Step 1:** '{coef} times a number {var}' is written as ${coef}{var}$.\n\n**Step 2:** 'Subtract {const} from it' means $- {const}$.\n\n$$\\therefore {expr_latex}$$"
    else:
        phrase = f"Write an algebraic expression for: **Divide the sum of a number {var} and {const} by {coef}**."
        expr_latex = f"\\frac{{{var} + {const}}}{{{coef}}}"
        expr_str = f"({var} + {const})/{coef}"
        sol = f"**Step 1:** 'The sum of a number {var} and {const}' is written as $({var} + {const})$.\n\n**Step 2:** 'Divide by {coef}' means $$\\frac{{{var} + {const}}}{{{coef}}}$$"

    return {
        "id": f"g7_math_alg_trans_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": phrase,
        "prompt_latex": phrase,
        "answer_mode": "math",
        "correct_answer": expr_str,
        "answer_latex": expr_latex,
        "answer_sympy": expr_str,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 2,
        "subskill": "verbal_to_algebraic",
        "learning_objective_id": "math_g7_algebra_translation",
        "misconception_tags": [
            "subtraction_order_inversion",
            "omitted_grouping_brackets_in_division"
        ],
        "diagnostic_tags": ["algebraic_syntax", "variable_abstraction"],
        "minimum_mastery_score": 75,
        "keywords": ["algebraic expression", "variable", "coefficient", "sum"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct variable and coefficient setup", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct operator and constant term", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Identify the variable ({var}) and the operations being performed on it.",
            "tier_2": "Be careful with subtraction order: 'subtract 5 from 2x' means 2x - 5, not 5 - 2x.",
            "tier_3": f"The expression is {expr_latex}."
        }
    }


def _generate_substitution_question(rng: random.Random) -> Dict[str, Any]:
    """Generates algebraic substitution questions."""
    var = rng.choice(["x", "y", "a", "b"])
    val = rng.randint(2, 6)
    c1 = rng.randint(2, 5)
    c2 = rng.randint(1, 9)
    sign = rng.choice(["+", "-"])

    if sign == "+":
        result = c1 * val + c2
        expr_latex = f"{c1}{var} + {c2}"
    else:
        result = c1 * val - c2
        expr_latex = f"{c1}{var} - {c2}"

    prompt = f"If **${var} = {val}$**, determine the value of the algebraic expression:\n\n$${expr_latex}$$"

    sol = (
        f"**Step 1:** Substitute ${var} = {val}$ in place of the variable:\n\n"
        f"$$= {c1}({val}) {'+' if sign == '+' else '-'} {c2}$$\n\n"
        f"**Step 2:** Multiply first (order of operations):\n\n"
        f"$$= {c1*val} {'+' if sign == '+' else '-'} {c2}$$\n\n"
        f"**Step 3:** Perform the addition/subtraction:\n\n"
        f"$$= {result}$$"
    )

    return {
        "id": f"g7_math_alg_sub_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(result),
        "answer_latex": str(result),
        "answer_sympy": str(result),
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 2,
        "subskill": "numerical_substitution",
        "learning_objective_id": "math_g7_algebra_substitution",
        "misconception_tags": [
            "order_of_operations_bodmas_violation",
            "concatenation_instead_of_multiplication"
        ],
        "diagnostic_tags": ["substitution_fluency", "order_of_operations"],
        "minimum_mastery_score": 80,
        "keywords": ["substitution", "evaluate", "expression value"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Accurate bracketed substitution", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct evaluated numerical answer", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Replace {var} with ({val}) and use BODMAS (multiply before adding/subtracting).",
            "tier_2": f"Calculate {c1} * {val} first, then apply the {sign} {c2}.",
            "tier_3": f"{c1}({val}) {'+' if sign == '+' else '-'} {c2} = {result}."
        }
    }


def _generate_linear_equation_question(rng: random.Random) -> Dict[str, Any]:
    """Generates Grade 7 linear equation questions (e.g. 2x + 5 = 17 or x/3 - 2 = 4)."""
    var = rng.choice(["x", "y", "m"])
    x_val = rng.randint(2, 9)
    coef = rng.randint(2, 5)
    const = rng.randint(1, 15)
    rhs = coef * x_val + const

    prompt = f"Solve the following linear equation for **${var}$** using inverse operations:\n\n$${coef}{var} + {const} = {rhs}$$"

    sol = (
        f"**Step 1:** Subtract ${const}$ from both sides of the equation (inverse of addition):\n\n"
        f"$${coef}{var} = {rhs} - {const}$$\n\n"
        f"$${coef}{var} = {rhs - const}$$\n\n"
        f"**Step 2:** Divide both sides by ${coef}$ (inverse of multiplication):\n\n"
        f"$${var} = \\frac{{{rhs - const}}}{{{coef}}}$$\n\n"
        f"$$\\therefore {var} = {x_val}$$"
    )

    return {
        "id": f"g7_math_alg_eq_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(x_val),
        "answer_latex": f"{var} = {x_val}",
        "answer_sympy": str(x_val),
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": "linear_equations",
        "learning_objective_id": "math_g7_algebra_equations",
        "misconception_tags": [
            "inverse_operation_sign_inversion",
            "divided_before_subtracting_constant"
        ],
        "diagnostic_tags": ["equation_solving", "inverse_operations"],
        "minimum_mastery_score": 75,
        "keywords": ["linear equation", "solve for x", "inverse operations"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Subtracting constant from both sides", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Dividing by coefficient on both sides", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Accurate solution for variable", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Isolate the term containing {var} by subtracting {const} from both sides first.",
            "tier_2": f"After subtracting, you have {coef}{var} = {rhs - const}. Now divide both sides by {coef}.",
            "tier_3": f"{var} = {x_val}."
        }
    }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Algebraic Expressions & Equations Question Generator.
    Supports atomic micro-drills:
    - mode="elementary_translation"
    - mode="elementary_substitution"
    - mode="elementary_equations"
    - mode="compound"
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions = []

    for _ in range(count):
        if mode == "elementary_translation" or subskill == "translation":
            q = _generate_verbal_translation_question(rng)
        elif mode == "elementary_substitution" or subskill == "substitution":
            q = _generate_substitution_question(rng)
        elif mode == "elementary_equations" or subskill == "equations":
            q = _generate_linear_equation_question(rng)
        else: # compound
            picker = rng.choice(["trans", "sub", "eq"])
            if picker == "trans":
                q = _generate_verbal_translation_question(rng)
            elif picker == "sub":
                q = _generate_substitution_question(rng)
            else:
                q = _generate_linear_equation_question(rng)
        questions.append(q)

    return questions
