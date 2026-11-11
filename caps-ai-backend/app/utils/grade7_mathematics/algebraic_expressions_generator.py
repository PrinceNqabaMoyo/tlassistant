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

SUBSKILLS = [
    "linear_equations",
    "verbal_to_algebraic",
    "numerical_substitution",
    "identify_expression_parts",
    "collect_like_terms"
]


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


def _generate_parts_of_expression_question(rng: random.Random) -> Dict[str, Any]:
    """Identifies components: variables, coefficients, constant term, number of terms."""
    var = rng.choice(["x", "y", "m"])
    c1 = rng.randint(2, 7)
    c2 = rng.randint(2, 9)
    const = rng.randint(3, 15)
    sign = rng.choice(["+", "-"])

    expr_latex = f"{c1}{var}^2 {sign} {c2}{var} + {const}"

    prompt = (
        f"Consider the algebraic expression:\n\n"
        f"$${expr_latex}$$\n\n"
        f"1. How many terms are in this expression?\n"
        f"2. Write down the variable used in this expression.\n"
        f"3. Write down the coefficient of ${var}$.\n"
        f"4. State the constant term."
    )
    coef_var = f"-{c2}" if sign == "-" else f"{c2}"
    sol = (
        f"**Step 1:** The expression has **3 terms**: ${c1}{var}^2$, ${sign}{c2}{var}$, and $+{const}$.\n\n"
        f"**Step 2:** The variable is **${var}$**.\n\n"
        f"**Step 3:** The coefficient of ${var}$ is **${coef_var}$**.\n\n"
        f"**Step 4:** The constant term is **${const}$**."
    )
    return {
        "id": f"g7_math_alg_parts_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"3; {var}; {coef_var}; {const}",
        "answer_latex": f"3,\\ {var},\\ {coef_var},\\ {const}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 3,
        "subskill": "identify_expression_parts",
        "learning_objective_id": "math_g7_algebra_parts",
        "misconception_tags": ["confused_coefficient_and_exponent"],
        "diagnostic_tags": ["algebra", "terminology"],
        "minimum_mastery_score": 75,
        "keywords": ["terms", "variable", "coefficient", "constant term"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Number of terms (3)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Variable ({var})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Coefficient ({coef_var})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Constant ({const})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": "Terms are separated by plus (+) and minus (-) signs.",
            "tier_2": f"A coefficient is the number multiplying the variable. The constant term has no variable.",
            "tier_3": f"Terms: 3, Variable: {var}, Coefficient of {var}: {coef_var}, Constant: {const}."
        }
    }


def _generate_collect_like_terms_question(rng: random.Random) -> Dict[str, Any]:
    """Simplifies linear expression by grouping like terms."""
    var = rng.choice(["x", "y", "a", "b"])
    c1 = rng.randint(3, 8)
    c2 = rng.randint(2, 6)
    k1 = rng.randint(2, 12)
    k2 = rng.randint(1, 9)

    tot_var = c1 + c2
    tot_const = k1 + k2

    prompt = (
        f"Simplify the following algebraic expression by grouping and combining like terms:\n\n"
        f"$${c1}{var} + {k1} + {c2}{var} + {k2}$$"
    )
    sol = (
        f"**Step 1:** Group like terms together (variable terms and constant terms):\n\n"
        f"$$({c1}{var} + {c2}{var}) + ({k1} + {k2})$$\n\n"
        f"**Step 2:** Combine like terms:\n\n"
        f"$$= {tot_var}{var} + {tot_const}$$\n\n"
        f"$$\\therefore \\text{{Simplified expression is }} \\mathbf{{{tot_var}{var} + {tot_const}}}$$"
    )
    ans_str = f"{tot_var}*{var} + {tot_const}"
    ans_latex = f"{tot_var}{var} + {tot_const}"
    return {
        "id": f"g7_math_alg_like_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "math",
        "correct_answer": ans_str,
        "answer_latex": ans_latex,
        "answer_sympy": ans_str,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 3,
        "subskill": "collect_like_terms",
        "learning_objective_id": "math_g7_algebra_like_terms",
        "misconception_tags": ["combined_unlike_terms"],
        "diagnostic_tags": ["algebra", "like_terms"],
        "minimum_mastery_score": 75,
        "keywords": ["like terms", "combine", "simplify"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Grouping like terms together", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Accurate variable sum {tot_var}{var}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Accurate constant sum {tot_const}", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Only add terms with the same variable together ({c1}{var} and {c2}{var}), and constant numbers together.",
            "tier_2": f"({c1} + {c2}){var} = {tot_var}{var}, and {k1} + {k2} = {tot_const}.",
            "tier_3": f"{tot_var}{var} + {tot_const}."
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
    - linear_equations
    - verbal_to_algebraic
    - numerical_substitution
    - identify_expression_parts
    - collect_like_terms
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    questions = []

    sub_str = str(subskill or "").lower()

    for _ in range(count):
        if "like" in sub_str or "collect" in sub_str or "subskill_5" in sub_str:
            q = _generate_collect_like_terms_question(rng)
        elif "part" in sub_str or "subskill_4" in sub_str or "identify" in sub_str:
            q = _generate_parts_of_expression_question(rng)
        elif "equation" in sub_str or "linear" in sub_str:
            q = _generate_linear_equation_question(rng)
        elif "verbal" in sub_str or "trans" in sub_str:
            q = _generate_verbal_translation_question(rng)
        elif "substitut" in sub_str:
            q = _generate_substitution_question(rng)
        elif mode == "elementary_translation":
            q = _generate_verbal_translation_question(rng)
        elif mode == "elementary_substitution":
            q = _generate_substitution_question(rng)
        elif mode == "elementary_equations":
            q = _generate_linear_equation_question(rng)
        else: # compound
            picker = rng.choice(["trans", "sub", "eq", "parts", "like"])
            if picker == "trans":
                q = _generate_verbal_translation_question(rng)
            elif picker == "sub":
                q = _generate_substitution_question(rng)
            elif picker == "eq":
                q = _generate_linear_equation_question(rng)
            elif picker == "parts":
                q = _generate_parts_of_expression_question(rng)
            else:
                q = _generate_collect_like_terms_question(rng)
        questions.append(q)

    return questions
