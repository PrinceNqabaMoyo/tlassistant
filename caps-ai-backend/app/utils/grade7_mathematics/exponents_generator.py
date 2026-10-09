"""
Grade 7 Mathematics - Exponents, Squares & Cubes Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Directly grounded in curriculum_docs/Mathematics_Gr7/END OF YEAR EXAM 2018.md (Q2.1.2, Q2.1.7, Q5.2.2)
and curriculum_docs/Mathematics_Gr7/Exponents Studio.md.

Archetypes Covered:
1. Squares and Square Roots (up to 15^2)
2. Cubes and Cube Roots (up to 10^3)
3. Combined Arithmetic with Powers and Roots (e.g. sqrt(144) - 2^2 + cbrt(27) = 11, Exam Q2.1.7)
4. Elementary Power Equations (e.g. x^2 = 64 => x = 8, Exam Q5.2.2)
"""

from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


# ============================================================================
# ARCHETYPE 1: Squares & Square Roots
# ============================================================================

def _generate_squares_and_roots(rng: random.Random) -> Dict[str, Any]:
    """
    Squares and square roots of integers up to 15.
    """
    is_root = rng.choice([True, False])
    base = rng.randint(2, 15)
    sq = base * base

    if is_root:
        prompt = f"Calculate the value of:\n\n\\[ \\sqrt{{{sq}}} \\]"
        sol = (
            f"Step 1: Identify the number that, when multiplied by itself, gives {sq}.\n\n"
            f"Since \\({base} \\times {base} = {base}^2 = {sq}\\),\n\n"
            f"\\[ \\sqrt{{{sq}}} = {base} \\]"
        )
        ans = str(base)
        ans_latex = str(base)
        t1 = f"What positive number multiplied by itself gives {sq}?"
        t2 = f"{base} × {base} = {sq}."
        t3 = f"\\sqrt{{{sq}}} = {base}."
        subskill = "square_root_calculation"
    else:
        prompt = f"Calculate the value of:\n\n\\[ {base}^2 \\]"
        sol = (
            f"Step 1: Expand the power as repeated multiplication:\n"
            f"\\[ {base}^2 = {base} \\times {base} \\]\n\n"
            f"Step 2: Multiply:\n"
            f"\\[ {base} \\times {base} = {sq} \\]"
        )
        ans = str(sq)
        ans_latex = str(sq)
        t1 = f"A number squared means multiplying the number by itself."
        t2 = f"Calculate {base} × {base}."
        t3 = f"{base} × {base} = {sq}."
        subskill = "square_calculation"

    return {
        "id": f"g7_math_exp_sq_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans_latex,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 2,
        "subskill": subskill,
        "learning_objective_id": "math_g7_exp_squares_roots",
        "misconception_tags": ["multiply_by_two_instead_of_squaring"],
        "diagnostic_tags": ["exponents", "squares", "square_roots"],
        "minimum_mastery_score": 75,
        "keywords": ["square", "square root", "exponent", "power of 2"],
        "marking_schema": {
            "total_marks": 1,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct evaluation of power/root ({ans})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "strict"
        },
        "hints": {
            "tier_1": t1,
            "tier_2": t2,
            "tier_3": t3
        }
    }


# ============================================================================
# ARCHETYPE 2: Cubes & Cube Roots
# ============================================================================

def _generate_cubes_and_roots(rng: random.Random) -> Dict[str, Any]:
    """
    Cubes and cube roots of integers up to 10.
    """
    is_root = rng.choice([True, False])
    base = rng.randint(2, 6)
    cube = base ** 3

    if is_root:
        prompt = f"Calculate the value of:\n\n\\[ \\sqrt[3]{{{cube}}} \\]"
        sol = (
            f"Step 1: Identify the number that multiplied by itself three times gives {cube}.\n\n"
            f"Since \\({base} \\times {base} \\times {base} = {base}^3 = {cube}\\),\n\n"
            f"\\[ \\sqrt[3]{{{cube}}} = {base} \\]"
        )
        ans = str(base)
        ans_latex = str(base)
        t1 = f"What number multiplied by itself 3 times gives {cube}?"
        t2 = f"{base} × {base} × {base} = {cube}."
        t3 = f"\\sqrt[3]{{{cube}}} = {base}."
        subskill = "cube_root_calculation"
    else:
        prompt = f"Calculate the value of:\n\n\\[ {base}^3 \\]"
        sol = (
            f"Step 1: Expand as repeated multiplication:\n"
            f"\\[ {base}^3 = {base} \\times {base} \\times {base} \\]\n\n"
            f"Step 2: Multiply step-by-step:\n"
            f"\\({base} \\times {base} = {base * base}\\)\n"
            f"\\({base * base} \\times {base} = {cube}\\)."
        )
        ans = str(cube)
        ans_latex = str(cube)
        t1 = f"Cubing a number means multiplying the number by itself three times."
        t2 = f"Calculate {base} × {base} × {base}."
        t3 = f"{base} × {base} × {base} = {cube}."
        subskill = "cube_calculation"

    return {
        "id": f"g7_math_exp_cb_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans_latex,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 2,
        "subskill": subskill,
        "learning_objective_id": "math_g7_exp_cubes_roots",
        "misconception_tags": ["multiply_by_three_instead_of_cubing"],
        "diagnostic_tags": ["exponents", "cubes", "cube_roots"],
        "minimum_mastery_score": 75,
        "keywords": ["cube", "cube root", "power of 3"],
        "marking_schema": {
            "total_marks": 1,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct evaluation ({ans})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "strict"
        },
        "hints": {
            "tier_1": t1,
            "tier_2": t2,
            "tier_3": t3
        }
    }


# ============================================================================
# ARCHETYPE 3: Combined Operations (Exam Q2.1.7)
# ============================================================================

def _generate_combined_powers_roots(rng: random.Random) -> Dict[str, Any]:
    """
    Combined operations with powers and roots.
    Exam Q2.1.7: sqrt(144) - 2^2 + cbrt(27) = 12 - 4 + 3 = 11.
    """
    # Square root term
    r_base = rng.choice([6, 8, 9, 10, 11, 12])
    sq_term = r_base * r_base

    # Power term
    p_base = rng.choice([2, 3, 4])
    p_exp = 2
    p_val = p_base ** p_exp

    # Cube root term
    c_base = rng.choice([1, 2, 3, 4, 5])
    cb_term = c_base ** 3

    # Operations: sqrt - pow + cbrt
    result = r_base - p_val + c_base

    prompt = (
        f"Simplify the following numerical expression. Show all steps:\n\n"
        f"\\[ \\sqrt{{{sq_term}}} - {p_base}^{{{p_exp}}} + \\sqrt[3]{{{cb_term}}} \\]"
    )

    sol = (
        f"Step 1: Evaluate each power and root term separately:\n"
        f"\\(\\sqrt{{{sq_term}}} = {r_base}\\)\n"
        f"\\({p_base}^{{{p_exp}}} = {p_val}\\)\n"
        f"\\(\\sqrt[3]{{{cb_term}}} = {c_base}\\)\n\n"
        f"Step 2: Substitute evaluated values into the expression:\n"
        f"\\[ {r_base} - {p_val} + {c_base} \\]\n\n"
        f"Step 3: Perform subtraction and addition from left to right:\n"
        f"\\({r_base} - {p_val} = {r_base - p_val}\\)\n"
        f"\\({r_base - p_val} + {c_base} = {result}\\)."
    )

    return {
        "id": f"g7_math_exp_comb_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(result),
        "answer_latex": str(result),
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 3,
        "subskill": "combined_powers_roots",
        "learning_objective_id": "math_g7_exp_combined_eval",
        "misconception_tags": [
            "order_of_operations_order_error",
            "multiply_by_two_instead_of_squaring"
        ],
        "diagnostic_tags": ["exponents", "combined_operations", "order_of_operations"],
        "minimum_mastery_score": 75,
        "keywords": ["square root", "cube root", "power", "simplify", "order of operations"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct evaluation of sqrt({sq_term}) = {r_base}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct evaluation of {p_base}^2 = {p_val} and cbrt({cb_term}) = {c_base}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct final calculated answer ({result})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"First find the value of each root and power, then do the addition and subtraction.",
            "tier_2": f"\\sqrt{{{sq_term}}} = {r_base}, {p_base}^2 = {p_val}, \\sqrt[3]{{{cb_term}}} = {c_base}. Then compute {r_base} - {p_val} + {c_base}.",
            "tier_3": f"{r_base} - {p_val} + {c_base} = {result}."
        }
    }


# ============================================================================
# ARCHETYPE 4: Power Equations (Exam Q5.2.2)
# ============================================================================

def _generate_power_equation(rng: random.Random) -> Dict[str, Any]:
    """
    Solving simple power equations.
    Exam Q5.2.2: x^2 = 64 => x = 8.
    """
    is_cube = rng.choice([False, True])
    var = rng.choice(["x", "y", "a", "b"])

    if is_cube:
        root = rng.choice([2, 3, 4, 5])
        val = root ** 3
        prompt = (
            f"Solve for \\({var}\\):\n\n"
            f"\\[ {var}^3 = {val} \\]"
        )
        sol = (
            f"Step 1: Take the cube root of both sides:\n"
            f"\\[ {var} = \\sqrt[3]{{{val}}} \\]\n\n"
            f"Step 2: Since \\({root}^3 = {val}\\),\n"
            f"\\[ {var} = {root} \\]"
        )
        t1 = f"Take the cube root of {val}."
        t2 = f"What number multiplied by itself 3 times equals {val}?"
        t3 = f"{var} = {root}."
    else:
        root = rng.choice([4, 5, 6, 7, 8, 9, 10, 11, 12])
        val = root ** 2
        prompt = (
            f"Solve for \\({var}\\) (where \\({var} > 0\\)):\n\n"
            f"\\[ {var}^2 = {val} \\]"
        )
        sol = (
            f"Step 1: Take the square root of both sides:\n"
            f"\\[ {var} = \\sqrt{{{val}}} \\]\n\n"
            f"Step 2: Since \\({root}^2 = {val}\\),\n"
            f"\\[ {var} = {root} \\]"
        )
        t1 = f"Take the square root of {val}."
        t2 = f"What number multiplied by itself equals {val}?"
        t3 = f"{var} = {root}."

    return {
        "id": f"g7_math_exp_eq_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(root),
        "answer_latex": f"{var} = {root}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 2,
        "subskill": "solve_power_equation",
        "learning_objective_id": "math_g7_exp_equations",
        "misconception_tags": ["divide_by_exponent_instead_of_root"],
        "diagnostic_tags": ["exponents", "equations", "roots"],
        "minimum_mastery_score": 75,
        "keywords": ["solve for x", "power equation", "square root", "cube root"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"Taking root of constant term", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct solution value ({root})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": t1,
            "tier_2": t2,
            "tier_3": t3
        }
    }


# ============================================================================
# MASTER GENERATE FUNCTION (6-Pillar Contract)
# ============================================================================

def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Exponents Question Generator.
    Supports atomic micro-drills:
    - mode="elementary_squares": Squares & square roots
    - mode="elementary_cubes": Cubes & cube roots
    - mode="elementary_combined": Mixed expressions with powers/roots
    - mode="elementary_equations": Power equations (x^2 = k)
    - mode="compound": Full authentic exam mix
    """
    rng = _rng(seed)
    questions = []

    for _ in range(count):
        if mode == "elementary_squares" or subskill == "squares":
            q = _generate_squares_and_roots(rng)
        elif mode == "elementary_cubes" or subskill == "cubes":
            q = _generate_cubes_and_roots(rng)
        elif mode == "elementary_combined" or subskill == "combined":
            q = _generate_combined_powers_roots(rng)
        elif mode == "elementary_equations" or subskill == "equations":
            q = _generate_power_equation(rng)
        else: # compound: pick across all archetypes
            archetype = rng.choice([
                lambda: _generate_squares_and_roots(rng),
                lambda: _generate_cubes_and_roots(rng),
                lambda: _generate_combined_powers_roots(rng),
                lambda: _generate_power_equation(rng)
            ])
            q = archetype()
        questions.append(q)

    return questions
