"""Grade 9 Mathematics - Algebraic Equations with Fractions and Quadratic Factorisation Generator.
Covers:
  - Linear equations with algebraic fractions (clearing denominators)
  - Equations of the form (x + a)/b - (x - c)/d = k
  - Quadratic equations solvable by factorisation: x^2 + bx + c = 0 -> (x - p)(x - q) = 0
  - Quadratic equations with common factor: ax^2 + bx = 0 -> x(ax + b) = 0

Follows South African CAPS curriculum specifications and the 6-Pillar Generator Contract.
Strictly zero-LLM, deterministic execution.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def generate_grade9_equations_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> Dict[str, Any]:
    r = _rng(seed)
    subskill = mode if mode.startswith("elementary_") else "equations_fractions_quadratics"

    archetype = r.choice(["fraction_linear_lcd", "fraction_simple_cross", "quadratic_trinomial", "quadratic_common_factor"])
    if subskill == "elementary_lcd":
        archetype = "fraction_simple_cross"
    elif subskill == "elementary_zero_product":
        archetype = "quadratic_common_factor"

    if archetype == "fraction_simple_cross":
        a = r.choice([2, 3, 4, 5, 7])
        b = r.choice([2, 3, 4, 5])
        c = r.choice([2, 3, 4, 6])
        sign = r.choice(["+", "-"])
        const_term = a if sign == "+" else -a
        sol = b * c - const_term

        expr_str = rf"\frac{{x {sign} {a}}}{{{b}}} = {c}"
        prompt = f"Solve for \\(x\\):\n$${expr_str}$$"
        sample_answer = rf"\frac{{x {sign} {a}}}{{{b}}} = {c} \implies x {sign} {a} = {b * c} \implies x = {sol}"

        return {
            "id": f"g9_eq_frac_cross_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-9",
            "topic": "Algebraic Equations",
            "subskill": "equations_fraction_cross",
            "learning_objective_id": "g9_eq_fraction_cross",
            "archetype": "fraction_simple_cross",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": str(sol),
            "marks": 2,
            "marking_schema": {
                "total_marks": 2,
                "marking_points": [
                    {"id": "mp_1", "desc": "Multiplying through by denominator", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Correct final value of x", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "sign_error", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Clear the fraction first by multiplying both sides by the denominator.",
                "tier_2": rf"Multiply both sides by ${b}$: $x {sign} {a} = {b * c}$.",
                "tier_3": rf"Transpose ${a}$: $x = {b * c} {'-' if sign == '+' else '+'} {a} = {sol}$.",
            },
            "misconception_tags": ["forgot_multiply_rhs", "sign_error_on_transposition"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 2,
            "mode": mode,
            "difficulty": "easy",
        }

    elif archetype == "fraction_linear_lcd":
        d1, d2, lcd, m1, m2 = 2, 3, 6, 3, 2
        a, b = 1, 2
        rhs_val = r.choice([2, 3, 4])
        # 3(x + 1) - 2(x - 2) = 6*rhs => x + 3 + 4 = 6*rhs => x + 7 = 6*rhs
        sol = 6 * rhs_val - 7

        expr_str = rf"\frac{{x + {a}}}{{{d1}}} - \frac{{x - {b}}}{{{d2}}} = {rhs_val}"
        prompt = f"Solve for \\(x\\) by finding the Lowest Common Denominator (LCD):\n$${expr_str}$$"
        sample_answer = (
            rf"\text{{LCD}} = {lcd}\\\ "
            rf"{m1}(x + {a}) - {m2}(x - {b}) = {lcd * rhs_val}\\\ "
            rf"{m1}x + {m1 * a} - {m2}x + {m2 * b} = {lcd * rhs_val}\\\ "
            rf"x + {m1 * a + m2 * b} = {lcd * rhs_val}\\\ "
            rf"x = {sol}"
        )

        return {
            "id": f"g9_eq_frac_lcd_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-9",
            "topic": "Algebraic Equations",
            "subskill": "equations_fractions_lcd",
            "learning_objective_id": "g9_eq_fractions_lcd",
            "archetype": "fraction_linear_lcd",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": str(sol),
            "marks": 4,
            "marking_schema": {
                "total_marks": 4,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Correct LCD = {lcd} and multiplying every term", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Accurate distribution of negative bracket -(x - 2)", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Grouping and combining like terms", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": "Final accurate answer for x", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "sign_error_distributing_negative", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": f"Identify the Lowest Common Denominator of the fractions, which is ${lcd}$.",
                "tier_2": rf"Multiply every single term across both sides by ${lcd}$: ${m1}(x + {a}) - {m2}(x - {b}) = {lcd * rhs_val}$.",
                "tier_3": rf"Distribute carefully: ${m1}x + {m1*a} - {m2}x + {m2*b} = {lcd*rhs_val}$. Group like terms to get $x = {sol}$.",
            },
            "misconception_tags": ["sign_error_distributing_negative", "forgot_multiply_rhs", "common_denominator_error"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 4,
            "mode": mode,
            "difficulty": "medium",
        }

    elif archetype == "quadratic_trinomial":
        p = r.choice([2, 3, 4, 5])
        q = r.choice([1, 2, 3, 6])
        b_coeff = -(p + q)
        c_const = p * q

        prompt = f"Solve for \\(x\\) by factorising:\n$$x^2 {b_coeff}x + {c_const} = 0$$"
        sample_answer = rf"x^2 {b_coeff}x + {c_const} = 0 \implies (x - {p})(x - {q}) = 0 \implies x = {p} \text{{ or }} x = {q}"

        return {
            "id": f"g9_eq_quad_trinomial_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-9",
            "topic": "Algebraic Equations",
            "subskill": "quadratic_equations_factorisation",
            "learning_objective_id": "g9_eq_quad_factorise",
            "archetype": "quadratic_trinomial",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"x = {p} or x = {q}",
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Factorising into two binomials (x - {p})(x - {q}) = 0", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Applying the Zero Product Property", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Both correct solutions x = {p} and x = {q}", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "omitted_second_root", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": f"Find two numbers that multiply to $+{c_const}$ and add together to give ${b_coeff}$.",
                "tier_2": rf"The factors are $-{p}$ and $-{q}$. Write as $(x - {p})(x - {q}) = 0$.",
                "tier_3": rf"Set each bracket to zero: $x - {p} = 0 \implies x = {p}$, or $x - {q} = 0 \implies x = {q}$.",
            },
            "misconception_tags": ["factor_pair_sign_inversion", "omitted_second_root", "sign_error_on_root"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }

    else:
        # ax^2 + bx = 0 -> x(ax + b) = 0
        a_val = r.choice([2, 3, 5])
        b_val = r.choice([4, 6, 9, 10, 15])
        gcd_val = math.gcd(a_val, b_val)
        a_val //= gcd_val
        b_val //= gcd_val
        if a_val == 1:
            a_val = 2
            b_val = 6

        prompt = f"Solve for \\(x\\):\n$${a_val}x^2 + {b_val}x = 0$$"
        root2_str = f"-{b_val}/{a_val}" if a_val != 1 else str(-b_val)
        sample_answer = rf"{a_val}x^2 + {b_val}x = 0 \implies x({a_val}x + {b_val}) = 0 \implies x = 0 \text{{ or }} x = -\frac{{{b_val}}}{{{a_val}}}"

        return {
            "id": f"g9_eq_quad_common_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-9",
            "topic": "Algebraic Equations",
            "subskill": "quadratic_equations_common_factor",
            "learning_objective_id": "g9_eq_quad_common_factor",
            "archetype": "quadratic_common_factor",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"x = 0 or x = {root2_str}",
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Extracting common factor x({a_val}x + {b_val}) = 0", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "First solution x = 0", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Second solution x = -{b_val}/{a_val}", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "divided_by_x_and_lost_zero_root", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Never divide across by x! That removes the valid root x = 0. Extract x as a common factor instead.",
                "tier_2": rf"Factor out $x$: $x({a_val}x + {b_val}) = 0$.",
                "tier_3": rf"Set each factor to zero: $x = 0$ or ${a_val}x = -{b_val} \implies x = -\frac{{{b_val}}}{{{a_val}}}$.",
            },
            "misconception_tags": ["divided_by_x_and_lost_zero_root", "omitted_zero_root", "sign_error"],
            "term": 2,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> List[Dict[str, Any]]:
    base_seed = seed if seed is not None else 42
    return [
        generate_grade9_equations_question(
            seed=base_seed + i,
            difficulty=difficulty,
            mode=mode,
        )
        for i in range(count)
    ]
