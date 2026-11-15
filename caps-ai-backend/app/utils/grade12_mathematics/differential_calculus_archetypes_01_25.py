"""Grade 12 Mathematics - Differential Calculus Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/Mathematics_Gr12/Term 1/04. Differential calculus.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional
import sympy as sp

from .sequences_series_archetypes_01_25 import _svg_spec


def _mcq_q(
    rng: random.Random,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 3,
    curriculum_ref: str = "Term 1 > Differential Calculus",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    opts = [correct] + distractors[:3]
    rng.shuffle(opts)
    q: Dict[str, Any] = {
        "id": qid,
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "multiple_choice",
        "prompt": prompt,
        "options": opts,
        "expected_answer": correct,
        "sample_answer": correct,
        "worked_solution": worked_solution,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct selection: {correct}", "marks": marks, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "misconception_tags": misconception_tags,
        "curriculum_reference": curriculum_ref,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
        q["modality"] = "diagram"
    return q


def _calc_q(
    rng: random.Random,
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    expected_value: str,
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 4,
    curriculum_ref: str = "Term 1 > Differential Calculus",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": qid,
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": expected_value,
        "sample_answer": expected_value,
        "worked_solution": worked_solution,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{i+1}", "desc": pt, "marks": 1, "editable": True}
                for i, pt in enumerate(worked_solution.strip().split("\n")[:marks])
            ] or [{"id": "mp_1", "desc": f"Accurate calculation: {expected_value}", "marks": marks, "editable": True}],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "misconception_tags": misconception_tags,
        "curriculum_reference": curriculum_ref,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
        q["modality"] = "diagram"
    return q


# ==============================================================================
# Archetypes 01 - 25
# ==============================================================================

def arch_01_limit_of_function_direct_substitution(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-3, -2, -1, 2, 3, 4])
    c2 = rng.choice([-4, -2, 2, 3, 5])
    c1 = rng.choice([-3, 1, 2])
    c0 = rng.choice([-6, -1, 4, 7])
    # f(x) = c1*x^2 + c2*x + c0
    ans_val = c1 * (a ** 2) + c2 * a + c0
    prompt = (
        f"Evaluate the limit by direct substitution:\n\n"
        f"$$\\lim_{{x \\to {a}}} \\left( {c1 if c1 != 1 else ''}x^2 {'+' if c2 >= 0 else '-'} {abs(c2)}x {'+' if c0 >= 0 else '-'} {abs(c0)} \\right)$$"
    )
    ans = str(ans_val)
    sol = (
        f"Step 1: Direct substitution is valid since the polynomial is continuous everywhere:\n"
        f"$$\\lim_{{x \\to {a}}} \\left( {c1 if c1 != 1 else ''}x^2 {'+' if c2 >= 0 else '-'} {abs(c2)}x {'+' if c0 >= 0 else '-'} {abs(c0)} \\right) "
        f"= {c1}({a})^2 {'+' if c2 >= 0 else '-'} {abs(c2)}({a}) {'+' if c0 >= 0 else '-'} {abs(c0)}$$\n"
        f"Step 2: Calculate numerical value:\n"
        f"$$= {c1 * (a**2)} {'+' if (c2*a) >= 0 else '-'} {abs(c2*a)} {'+' if c0 >= 0 else '-'} {abs(c0)} = {ans_val}$$."
    )
    return _calc_q(
        rng, f"g12_calc_01_{rng.randint(100000, 999999)}", "01_limit_of_function_direct_substitution",
        "Limit of Polynomial by Direct Substitution", prompt, ans, sol,
        {"tier_1": f"Substitute x = {a} directly into the polynomial expression.",
         "tier_2": f"Calculate {c1}({a})^2 + ({c2})({a}) + ({c0}).",
         "tier_3": f"The limit evaluates to {ans_val}."},
        ["arithmetic_error_in_polynomial_substitution"]
    )


def arch_02_limit_indeterminate_factorisation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-4, -3, -2, 2, 3, 5])
    b = rng.choice([-5, -1, 1, 4, 6])
    while b == a or b == -a:
        b = rng.choice([-6, 2, 7])
    # Numerator = (x - a)(x + b) = x^2 + (b - a)x - ab
    mid = b - a
    const = -a * b
    # lim x->a of (x^2 + mid*x + const) / (x - a) = a + b
    ans_val = a + b
    prompt = (
        f"Evaluate the limit:\n\n"
        f"$$\\lim_{{x \\to {a}}} \\frac{{x^2 {'+' if mid >= 0 else '-'} {abs(mid)}x {'+' if const >= 0 else '-'} {abs(const)}}}{{x {'-' if a >= 0 else '+'} {abs(a)}}}$$"
    )
    ans = str(ans_val)
    sol = (
        f"Step 1: Direct substitution yields $\\frac{{0}}{{0}}$ (indeterminate form), requiring factorisation.\n"
        f"Step 2: Factorise the numerator:\n"
        f"$$x^2 {'+' if mid >= 0 else '-'} {abs(mid)}x {'+' if const >= 0 else '-'} {abs(const)} = (x {'-' if a >= 0 else '+'} {abs(a)})(x {'+' if b >= 0 else '-'} {abs(b)})$$\n"
        f"Step 3: Cancel common factor $(x {'-' if a >= 0 else '+'} {abs(a)})$ for $x \\ne {a}$:\n"
        f"$$\\lim_{{x \\to {a}}} (x {'+' if b >= 0 else '-'} {abs(b)}) = {a} {'+' if b >= 0 else '-'} {abs(b)} = {ans_val}$$."
    )
    return _calc_q(
        rng, f"g12_calc_02_{rng.randint(100000, 999999)}", "02_limit_indeterminate_factorisation",
        "Evaluating Indeterminate Limit by Factorisation", prompt, ans, sol,
        {"tier_1": f"Factorise the quadratic numerator to cancel the (x - {a}) factor in the denominator.",
         "tier_2": f"The numerator factorises to (x - {a})(x + {b}). Cancel (x - {a}) and evaluate at x = {a}.",
         "tier_3": f"Result is {ans_val}."},
        ["divided_by_zero_without_cancelling_common_factor"]
    )


def arch_03_limit_rationalise_numerator(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([1, 4, 9, 16, 25])
    root_c = int(math.isqrt(c))
    # lim_{x -> 0} (sqrt(x + c) - root_c) / x
    # = lim_{x -> 0} ((x + c) - c) / (x * (sqrt(x + c) + root_c)) = 1 / (2 * root_c)
    denom = 2 * root_c
    prompt = (
        f"Evaluate the limit by rationalising the numerator:\n\n"
        f"$$\\lim_{{x \\to 0}} \\frac{{\\sqrt{{x + {c}}} - {root_c}}}{{x}}$$"
    )
    correct = f"1/{denom}"
    distractors = [
        f"1/{root_c}",
        f"{root_c}",
        "0",
    ]
    sol = (
        f"Step 1: Multiply numerator and denominator by the conjugate $(\\sqrt{{x + {c}}} + {root_c})$:\n"
        f"$$\\lim_{{x \\to 0}} \\frac{{(\\sqrt{{x + {c}}} - {root_c})(\\sqrt{{x + {c}}} + {root_c})}}{{x(\\sqrt{{x + {c}}} + {root_c})}}$$\n"
        f"Step 2: Simplify the numerator:\n"
        f"$$(\\sqrt{{x + {c}}})^2 - ({root_c})^2 = (x + {c}) - {c} = x$$\n"
        f"Step 3: Cancel $x$ for $x \\ne 0$ and evaluate the limit as $x \\to 0$:\n"
        f"$$\\lim_{{x \\to 0}} \\frac{{1}}{{\\sqrt{{x + {c}}} + {root_c}}} = \\frac{{1}}{{\\sqrt{{{c}}} + {root_c}}} = \\frac{{1}}{{{root_c} + {root_c}}} = \\frac{{1}}{{{denom}}}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_03_{rng.randint(100000, 999999)}", "03_limit_rationalise_numerator",
        "Limit Involving Square Roots and Rationalisation", prompt, correct, distractors, sol,
        {"tier_1": "Multiply both numerator and denominator by the conjugate sqrt(x + c) + root_c.",
         "tier_2": "The numerator becomes x, which cancels with the x in the denominator.",
         "tier_3": correct},
        ["incorrect_conjugate_multiplication"]
    )


def arch_04_average_gradient_secant_line(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3])
    b = rng.choice([-4, -2, 1, 3])
    c = rng.choice([-5, 2, 6])
    x1 = rng.choice([1, 2])
    x2 = x1 + rng.choice([2, 3])
    # f(x) = a*x^2 + b*x + c
    y1 = a * (x1 ** 2) + b * x1 + c
    y2 = a * (x2 ** 2) + b * x2 + c
    # Average gradient = (y2 - y1) / (x2 - x1)
    m_avg = (y2 - y1) / (x2 - x1)
    ans_val = int(m_avg) if m_avg == int(m_avg) else round(m_avg, 2)
    prompt = (
        f"Given the quadratic function $f(x) = {a if a != 1 else ''}x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c >= 0 else '-'} {abs(c)}$:\n\n"
        f"Calculate the average gradient of the curve between the points where $x = {x1}$ and $x = {x2}$."
    )
    ans = str(ans_val)
    sol = (
        f"Step 1: Compute function values at the boundary points:\n"
        f"$$f({x1}) = {a}({x1})^2 {'+' if b >= 0 else '-'} {abs(b)}({x1}) {'+' if c >= 0 else '-'} {abs(c)} = {y1}$$\n"
        f"$$f({x2}) = {a}({x2})^2 {'+' if b >= 0 else '-'} {abs(b)}({x2}) {'+' if c >= 0 else '-'} {abs(c)} = {y2}$$\n"
        f"Step 2: Apply the average gradient formula:\n"
        f"$$\\text{{Average gradient}} = \\frac{{f({x2}) - f({x1})}}{{{x2} - {x1}}} = \\frac{{{y2} - {y1}}}{{{x2 - x1}}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {ans_val}$$."
    )
    return _calc_q(
        rng, f"g12_calc_04_{rng.randint(100000, 999999)}", "04_average_gradient_secant_line",
        "Average Gradient of Quadratic Curve Between Two Points", prompt, ans, sol,
        {"tier_1": "Calculate f(x1) and f(x2), then use formula m = [f(x2) - f(x1)] / (x2 - x1).",
         "tier_2": f"f({x1}) = {y1} and f({x2}) = {y2}. Subtract and divide by {x2 - x1}.",
         "tier_3": f"Average gradient is {ans_val}."},
        ["confused_average_gradient_with_instantaneous_derivative"]
    )


def arch_05_average_gradient_interval_notation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-2, -1, 1, 2])
    k = rng.choice([-3, 5, 8])
    x1 = rng.choice([-2, -1, 0, 1])
    x2 = x1 + rng.choice([2, 4])
    # f(x) = a*x^2 + k
    y1 = a * (x1 ** 2) + k
    y2 = a * (x2 ** 2) + k
    m_avg = (y2 - y1) / (x2 - x1)
    ans_val = int(m_avg) if m_avg == int(m_avg) else round(m_avg, 2)
    prompt = (
        f"Determine the average rate of change of $g(x) = {a if a != 1 else ''}x^2 {'+' if k >= 0 else '-'} {abs(k)}$ "
        f"over the closed interval $[{x1};\\ {x2}]$."
    )
    ans = str(ans_val)
    sol = (
        f"Step 1: Calculate endpoints of the interval:\n"
        f"$$g({x1}) = {a}({x1})^2 {'+' if k >= 0 else '-'} {abs(k)} = {y1}$$\n"
        f"$$g({x2}) = {a}({x2})^2 {'+' if k >= 0 else '-'} {abs(k)} = {y2}$$\n"
        f"Step 2: Calculate average rate of change:\n"
        f"$$\\frac{{g({x2}) - g({x1})}}{{{x2} - ({x1})}} = \\frac{{{y2} - {y1}}}{{{x2 - x1}}} = {ans_val}$$."
    )
    return _calc_q(
        rng, f"g12_calc_05_{rng.randint(100000, 999999)}", "05_average_gradient_interval_notation",
        "Average Rate of Change Over a Closed Interval", prompt, ans, sol,
        {"tier_1": f"The interval [{x1}; {x2}] means from x = {x1} to x = {x2}.",
         "tier_2": f"Find [g({x2}) - g({x1})] / ({x2} - {x1}).",
         "tier_3": f"Result is {ans_val}."},
        ["subtracted_endpoints_in_wrong_order"]
    )


def arch_06_first_principles_linear_function(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([-5, -3, -2, 2, 4, 7])
    c = rng.choice([-8, -4, 3, 9])
    prompt = (
        f"Differentiate $f(x) = {m}x {'+' if c >= 0 else '-'} {abs(c)}$ from first principles."
    )
    correct = f"f'(x) = {m}"
    distractors = [
        f"f'(x) = {m}x",
        f"f'(x) = {m} + {c}",
        f"f'(x) = 0",
    ]
    sol = (
        f"Step 1: State the definition of derivative from first principles:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} \\frac{{f(x+h) - f(x)}}{{h}}$$\n"
        f"Step 2: Substitute $f(x+h) = {m}(x+h) {'+' if c >= 0 else '-'} {abs(c)}$:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} \\frac{{({m}x + {m}h {'+' if c >= 0 else '-'} {abs(c)}) - ({m}x {'+' if c >= 0 else '-'} {abs(c)})}}{{h}}$$\n"
        f"Step 3: Simplify numerator:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} \\frac{{{m}h}}{{h}}$$\n"
        f"Step 4: Divide by $h$ and evaluate the limit as $h \\to 0$:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} ({m}) = {m}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_06_{rng.randint(100000, 999999)}", "06_first_principles_linear_function",
        "Differentiation of Linear Function from First Principles", prompt, correct, distractors, sol,
        {"tier_1": "Apply f'(x) = lim_{h -> 0} [f(x+h) - f(x)] / h.",
         "tier_2": f"Expand {m}(x+h) + {c} - ({m}x + {c}). The terms without h cancel out, leaving {m}h / h.",
         "tier_3": correct},
        ["retained_h_after_evaluating_limit"]
    )


def arch_07_first_principles_monic_quadratic(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([-7, -3, 2, 5, 8])
    prompt = (
        f"Given $f(x) = x^2 {'+' if c >= 0 else '-'} {abs(c)}$, determine $f'(x)$ from first principles."
    )
    correct = "f'(x) = 2x"
    distractors = [
        f"f'(x) = 2x + {c}",
        "f'(x) = x",
        "f'(x) = 2x + h",
    ]
    sol = (
        f"Step 1: Definition formula:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} \\frac{{f(x+h) - f(x)}}{{h}}$$\n"
        f"Step 2: Substitution:\n"
        f"$$f(x+h) = (x+h)^2 {'+' if c >= 0 else '-'} {abs(c)} = x^2 + 2xh + h^2 {'+' if c >= 0 else '-'} {abs(c)}$$\n"
        f"$$f(x+h) - f(x) = (x^2 + 2xh + h^2 {'+' if c >= 0 else '-'} {abs(c)}) - (x^2 {'+' if c >= 0 else '-'} {abs(c)}) = 2xh + h^2$$\n"
        f"Step 3: Factor out $h$ and divide:\n"
        f"$$\\frac{{h(2x + h)}}{{h}} = 2x + h$$\n"
        f"Step 4: Take the limit as $h \\to 0$:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} (2x + h) = 2x$$."
    )
    return _mcq_q(
        rng, f"g12_calc_07_{rng.randint(100000, 999999)}", "07_first_principles_monic_quadratic",
        "Differentiation of Monic Quadratic from First Principles", prompt, correct, distractors, sol,
        {"tier_1": "Expand (x + h)^2 as x^2 + 2xh + h^2.",
         "tier_2": "Subtract f(x), factor h out of 2xh + h^2, and divide through by h.",
         "tier_3": correct},
        ["forgot_cross_term_in_binomial_expansion"]
    )


def arch_08_first_principles_general_quadratic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.choice([-5, -3, 2, 4])
    c = rng.choice([-6, 1, 7])
    # f(x) = a*x^2 + b*x + c  =>  f'(x) = 2a*x + b
    two_a = 2 * a
    correct = f"f'(x) = {two_a}x {'+' if b >= 0 else '-'} {abs(b)}"
    distractors = [
        f"f'(x) = {a}x {'+' if b >= 0 else '-'} {abs(b)}",
        f"f'(x) = {two_a}x",
        f"f'(x) = {two_a}x {'+' if b >= 0 else '-'} {abs(b)} + {c}",
    ]
    prompt = (
        f"Determine $f'(x)$ from first principles if $f(x) = {a}x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c >= 0 else '-'} {abs(c)}$."
    )
    sol = (
        f"Step 1: State definition:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} \\frac{{f(x+h) - f(x)}}{{h}}$$\n"
        f"Step 2: Expand $f(x+h)$:\n"
        f"$$f(x+h) = {a}(x+h)^2 {'+' if b >= 0 else '-'} {abs(b)}(x+h) {'+' if c >= 0 else '-'} {abs(c)}$$\n"
        f"$$= {a}(x^2 + 2xh + h^2) {'+' if b >= 0 else '-'} {abs(b)}x {'+' if b >= 0 else '-'} {abs(b)}h {'+' if c >= 0 else '-'} {abs(c)}$$\n"
        f"$$= {a}x^2 + {two_a}xh + {a}h^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if b >= 0 else '-'} {abs(b)}h {'+' if c >= 0 else '-'} {abs(c)}$$\n"
        f"Step 3: Subtract $f(x)$ and factor $h$:\n"
        f"$$f(x+h) - f(x) = {two_a}xh + {a}h^2 {'+' if b >= 0 else '-'} {abs(b)}h = h({two_a}x + {a}h {'+' if b >= 0 else '-'} {abs(b)})$$\n"
        f"Step 4: Cancel $h$ and evaluate limit as $h \\to 0$:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} ({two_a}x + {a}h {'+' if b >= 0 else '-'} {abs(b)}) = {two_a}x {'+' if b >= 0 else '-'} {abs(b)}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_08_{rng.randint(100000, 999999)}", "08_first_principles_general_quadratic",
        "Differentiation of General Quadratic from First Principles", prompt, correct, distractors, sol,
        {"tier_1": "Write down the definition formula: lim_{h -> 0} [f(x+h) - f(x)] / h.",
         "tier_2": f"Substitute (x+h) for every x, expand carefully, subtract f(x), factorise h, and let h = 0.",
         "tier_3": correct},
        ["dropped_limit_symbol_prematurely", "incorrect_distribution_over_binomial"]
    )


def arch_09_first_principles_negative_leading_coeff(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3])
    b = rng.choice([-4, -2, 3, 5])
    # f(x) = -a*x^2 + b*x  =>  f'(x) = -2a*x + b
    two_a = 2 * a
    correct = f"f'(x) = -{two_a}x {'+' if b >= 0 else '-'} {abs(b)}"
    distractors = [
        f"f'(x) = {two_a}x {'+' if b >= 0 else '-'} {abs(b)}",
        f"f'(x) = -{two_a}x",
        f"f'(x) = -{a}x {'+' if b >= 0 else '-'} {abs(b)}",
    ]
    prompt = (
        f"Given $f(x) = -{a if a != 1 else ''}x^2 {'+' if b >= 0 else '-'} {abs(b)}x$, determine $f'(x)$ using first principles."
    )
    sol = (
        f"Step 1: Formula: $f'(x) = \\lim_{{h \\to 0}} \\frac{{f(x+h) - f(x)}}{{h}}$\n"
        f"Step 2: $f(x+h) = -{a if a != 1 else ''}(x^2 + 2xh + h^2) {'+' if b >= 0 else '-'} {abs(b)}(x+h)$\n"
        f"$$= -{a if a != 1 else ''}x^2 - {two_a}xh - {a if a != 1 else ''}h^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if b >= 0 else '-'} {abs(b)}h$$\n"
        f"Step 3: $f(x+h) - f(x) = -{two_a}xh - {a if a != 1 else ''}h^2 {'+' if b >= 0 else '-'} {abs(b)}h = h(-{two_a}x - {a if a != 1 else ''}h {'+' if b >= 0 else '-'} {abs(b)})$\n"
        f"Step 4: $\\lim_{{h \\to 0}} (-{two_a}x - {a if a != 1 else ''}h {'+' if b >= 0 else '-'} {abs(b)}) = -{two_a}x {'+' if b >= 0 else '-'} {abs(b)}$."
    )
    return _mcq_q(
        rng, f"g12_calc_09_{rng.randint(100000, 999999)}", "09_first_principles_negative_leading_coeff",
        "First Principles with Negative Leading Coefficient", prompt, correct, distractors, sol,
        {"tier_1": "Carefully distribute the negative sign: -(x+h)^2 = -x^2 - 2xh - h^2.",
         "tier_2": "Factor out h from numerator and cancel with denominator.",
         "tier_3": correct},
        ["sign_error_distributing_negative_leading_coefficient"]
    )


def arch_10_first_principles_hyperbolic_fraction(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2, 3, 4, 5])
    # f(x) = k / x  =>  f'(x) = -k / x^2
    correct = f"f'(x) = -{k} / x^2"
    distractors = [
        f"f'(x) = {k} / x^2",
        f"f'(x) = -{k} / x",
        f"f'(x) = -1 / ({k}x^2)",
    ]
    prompt = (
        f"Differentiate $f(x) = \\frac{{{k}}}{{x}}$ from first principles."
    )
    sol = (
        f"Step 1: Formula: $f'(x) = \\lim_{{h \\to 0}} \\frac{{f(x+h) - f(x)}}{{h}}$\n"
        f"Step 2: Substitute and find common denominator in numerator:\n"
        f"$$f(x+h) - f(x) = \\frac{{{k}}}{{x+h}} - \\frac{{{k}}}{{x}} = \\frac{{{k}x - {k}(x+h)}}{{x(x+h)}} = \\frac{{{k}x - {k}x - {k}h}}{{x(x+h)}} = \\frac{{-{k}h}}{{x(x+h)}}$$\n"
        f"Step 3: Divide by $h$:\n"
        f"$$\\frac{{f(x+h) - f(x)}}{{h}} = \\frac{{-{k}h}}{{h \\cdot x(x+h)}} = \\frac{{-{k}}}{{x(x+h)}}$$\n"
        f"Step 4: Take the limit as $h \\to 0$:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} \\frac{{-{k}}}{{x(x+h)}} = \\frac{{-{k}}}{{x(x+0)}} = -\\frac{{{k}}}{{x^2}}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_10_{rng.randint(100000, 999999)}", "10_first_principles_hyperbolic_fraction",
        "Differentiation of Hyperbolic Function from First Principles", prompt, correct, distractors, sol,
        {"tier_1": "Find a common denominator x(x+h) for the two fractions in the numerator.",
         "tier_2": "The numerator becomes kx - k(x+h) = -kh. Then cancel h with the denominator.",
         "tier_3": correct},
        ["failed_to_find_common_denominator"]
    )


def arch_11_first_principles_cubic_monic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2])
    three_a = 3 * a
    correct = f"f'(x) = {three_a if three_a != 1 else ''}x^2"
    distractors = [
        f"f'(x) = {a}x^2",
        f"f'(x) = {three_a}x",
        f"f'(x) = {three_a}x^3",
    ]
    prompt = (
        f"Determine $f'(x)$ from first principles if $f(x) = {a if a != 1 else ''}x^3$."
    )
    sol = (
        f"Step 1: Formula: $f'(x) = \\lim_{{h \\to 0}} \\frac{{f(x+h) - f(x)}}{{h}}$\n"
        f"Step 2: Expand $(x+h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$:\n"
        f"$$f(x+h) - f(x) = {a if a != 1 else ''}(x^3 + 3x^2h + 3xh^2 + h^3) - {a if a != 1 else ''}x^3 = {three_a}x^2h + {3*a}xh^2 + {a}h^3$$\n"
        f"Step 3: Factor out $h$:\n"
        f"$$= h({three_a}x^2 + {3*a}xh + {a}h^2)$$\n"
        f"Step 4: Cancel $h$ and evaluate limit as $h \\to 0$:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} ({three_a}x^2 + {3*a}xh + {a}h^2) = {three_a}x^2$$."
    )
    return _mcq_q(
        rng, f"g12_calc_11_{rng.randint(100000, 999999)}", "11_first_principles_cubic_monic",
        "Differentiation of Monic Cubic from First Principles", prompt, correct, distractors, sol,
        {"tier_1": "Recall binomial expansion: (x+h)^3 = x^3 + 3x^2h + 3xh^2 + h^3.",
         "tier_2": "Subtract x^3, factor out h, and let h approach 0.",
         "tier_3": correct},
        ["incorrect_binomial_expansion_of_cubic"]
    )


def arch_12_first_principles_evaluate_at_specific_point(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3])
    b = rng.choice([-3, 2, 4])
    x0 = rng.choice([-2, 1, 3])
    # f(x) = a*x^2 + b*x  =>  f'(x) = 2a*x + b  =>  f'(x0) = 2a*x0 + b
    slope = 2 * a * x0 + b
    prompt = (
        f"Given $f(x) = {a if a != 1 else ''}x^2 {'+' if b >= 0 else '-'} {abs(b)}x$:\n\n"
        f"1. Determine the derivative $f'(x)$ from first principles.\n"
        f"2. Hence, calculate the value of $f'({x0})$."
    )
    ans = str(slope)
    sol = (
        f"Step 1: First principles derivative:\n"
        f"$$f'(x) = \\lim_{{h \\to 0}} \\frac{{f(x+h) - f(x)}}{{h}} = {2*a}x {'+' if b >= 0 else '-'} {abs(b)}$$\n"
        f"Step 2: Evaluate at $x = {x0}$:\n"
        f"$$f'({x0}) = {2*a}({x0}) {'+' if b >= 0 else '-'} {abs(b)} = {slope}$$."
    )
    return _calc_q(
        rng, f"g12_calc_12_{rng.randint(100000, 999999)}", "12_first_principles_evaluate_at_specific_point",
        "Derivative Evaluated at a Specific Point Using First Principles", prompt, ans, sol,
        {"tier_1": f"First find f'(x) = {2*a}x + ({b}), then substitute x = {x0}.",
         "tier_2": f"Calculate {2*a}({x0}) + ({b}).",
         "tier_3": f"f'({x0}) = {slope}."},
        ["substituted_x_value_before_taking_derivative"]
    )


def arch_13_power_rule_polynomial_terms(rng: random.Random) -> Dict[str, Any]:
    c3 = rng.choice([2, 3, 4])
    c2 = rng.choice([-5, -3, 3, 5])
    c1 = rng.choice([-8, 4, 7])
    c0 = rng.choice([-9, 6, 12])
    # f(x) = c3*x^3 + c2*x^2 + c1*x + c0  =>  f'(x) = 3*c3*x^2 + 2*c2*x + c1
    d2 = 3 * c3
    d1 = 2 * c2
    d0 = c1
    correct = f"{d2}x^2 {'+' if d1 >= 0 else '-'} {abs(d1)}x {'+' if d0 >= 0 else '-'} {abs(d0)}"
    distractors = [
        f"{c3}x^2 {'+' if c2 >= 0 else '-'} {abs(c2)}x {'+' if c1 >= 0 else '-'} {abs(c1)}",
        f"{d2}x^3 {'+' if d1 >= 0 else '-'} {abs(d1)}x^2 {'+' if d0 >= 0 else '-'} {abs(d0)}x",
        f"{d2}x^2 {'+' if d1 >= 0 else '-'} {abs(d1)}x",
    ]
    prompt = (
        f"Determine the derivative $\\frac{{dy}}{{dx}}$ using the rules of differentiation:\n\n"
        f"$$y = {c3}x^3 {'+' if c2 >= 0 else '-'} {abs(c2)}x^2 {'+' if c1 >= 0 else '-'} {abs(c1)}x {'+' if c0 >= 0 else '-'} {abs(c0)}$$"
    )
    sol = (
        f"Step 1: Apply the power rule $\\frac{{d}}{{dx}}[x^n] = n x^{{n-1}}$ to each term:\n"
        f"$$\\frac{{d}}{{dx}}[{c3}x^3] = 3 \\cdot {c3} x^2 = {d2}x^2$$\n"
        f"$$\\frac{{d}}{{dx}}[{c2}x^2] = 2 \\cdot ({c2}) x = {d1}x$$\n"
        f"$$\\frac{{d}}{{dx}}[{c1}x] = {c1}$$\n"
        f"$$\\frac{{d}}{{dx}}[{c0}] = 0$$\n"
        f"Step 2: Combine terms:\n"
        f"$$\\frac{{dy}}{{dx}} = {correct}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_13_{rng.randint(100000, 999999)}", "13_power_rule_polynomial_terms",
        "Power Rule Differentiation of Cubic Polynomial", prompt, correct, distractors, sol,
        {"tier_1": "Multiply each coefficient by the power of x and decrease the power by 1.",
         "tier_2": "The derivative of a constant term is 0.",
         "tier_3": correct},
        ["forgot_to_differentiate_constant_to_zero"]
    )


def arch_14_derivative_notation_d_dx_and_dy_dx(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 5, 6])
    coeff = rng.choice([2, 3, 7])
    # D_x [coeff * x^n - 8x] = n * coeff * x^(n-1) - 8
    prod = n * coeff
    deg = n - 1
    correct = f"{prod}x^{deg} - 8"
    distractors = [
        f"{coeff}x^{deg} - 8",
        f"{prod}x^{n} - 8",
        f"{prod}x^{deg}",
    ]
    prompt = (
        f"Evaluate the derivative using operator notation:\n\n"
        f"$$D_x \\left[ {coeff}x^{{{n}}} - 8x \\right]$$"
    )
    sol = (
        f"Step 1: $D_x$ denotes differentiation with respect to $x$.\n"
        f"Step 2: Apply the power rule:\n"
        f"$$D_x[{coeff}x^{{{n}}}] = {coeff} \\cdot {n} x^{{{n-1}}} = {prod}x^{{{deg}}}$$\n"
        f"$$D_x[-8x] = -8$$\n"
        f"Result: ${correct}$."
    )
    return _mcq_q(
        rng, f"g12_calc_14_{rng.randint(100000, 999999)}", "14_derivative_notation_d_dx_and_dy_dx",
        "Differentiation Using Operator Notation D_x", prompt, correct, distractors, sol,
        {"tier_1": "D_x means differentiate the expression inside brackets with respect to x.",
         "tier_2": f"Differentiate {coeff}x^{n} using power rule: {coeff} * {n} * x^{n-1}.",
         "tier_3": correct},
        ["confused_operator_notation_with_multiplication"]
    )


def arch_15_differentiation_negative_exponents(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    p = rng.choice([2, 3])
    # y = a / x^p = a * x^(-p)  =>  dy/dx = -a*p * x^(-p-1) = -(a*p) / x^(p+1)
    ap = a * p
    p1 = p + 1
    correct = f"-{ap} / x^{p1}"
    distractors = [
        f"-{a} / x^{p1}",
        f"{ap} / x^{p1}",
        f"-{ap} / x^{p}",
    ]
    prompt = (
        f"Differentiate $y = \\frac{{{a}}}{{x^{{{p}}}}}$ with respect to $x$ and express your answer with a positive exponent."
    )
    sol = (
        f"Step 1: Rewrite the fraction using a negative exponent:\n"
        f"$$y = {a}x^{{-{p}}}$$\n"
        f"Step 2: Differentiate using the power rule:\n"
        f"$$\\frac{{dy}}{{dx}} = {a} \\cdot (-{p}) x^{{-{p}-1}} = -{ap}x^{{-{p1}}}$$\n"
        f"Step 3: Convert back to positive exponent format:\n"
        f"$$\\frac{{dy}}{{dx}} = -\\frac{{{ap}}}{{x^{{{p1}}}}}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_15_{rng.randint(100000, 999999)}", "15_differentiation_negative_exponents",
        "Differentiation with Negative Exponents", prompt, correct, distractors, sol,
        {"tier_1": "Rewrite 1/x^p as x^(-p) before differentiating.",
         "tier_2": f"Multiply by -{p} and subtract 1 from the power to get -{p+1}.",
         "tier_3": correct},
        ["subtracted_one_incorrectly_from_negative_exponent"]
    )


def arch_16_differentiation_fractional_surd_exponents(rng: random.Random) -> Dict[str, Any]:
    # f(x) = sqrt(x) + x^3  =>  f'(x) = 1/(2*sqrt(x)) + 3x^2
    c = rng.choice([2, 4, 6])
    # f(x) = c * sqrt(x) = c * x^(1/2)  =>  f'(x) = (c/2) * x^(-1/2) = (c/2) / sqrt(x)
    half_c = c // 2
    correct = f"{half_c} / sqrt(x)" if half_c != 1 else "1 / sqrt(x)"
    distractors = [
        f"{c} / sqrt(x)",
        f"{half_c} sqrt(x)",
        f"1 / (2x)",
    ]
    prompt = (
        f"Determine $\\frac{{d}}{{dx}} \\left[ {c}\\sqrt{{x}} \\right]$."
    )
    sol = (
        f"Step 1: Convert radical to rational exponent form:\n"
        f"$$f(x) = {c}x^{{1/2}}$$\n"
        f"Step 2: Apply the power rule:\n"
        f"$$f'(x) = {c} \\cdot \\frac{{1}}{{2}} x^{{1/2 - 1}} = {half_c} x^{{-1/2}}$$\n"
        f"Step 3: Express in surd form with positive exponent:\n"
        f"$$f'(x) = \\frac{{{half_c}}}{{\\sqrt{{x}}}}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_16_{rng.randint(100000, 999999)}", "16_differentiation_fractional_surd_exponents",
        "Differentiation of Radical Terms with Fractional Exponents", prompt, correct, distractors, sol,
        {"tier_1": "Convert sqrt(x) into x^(1/2).",
         "tier_2": f"Power rule: (1/2) * x^(1/2 - 1) = (1/2)x^(-1/2) = 1/(2*sqrt(x)).",
         "tier_3": correct},
        ["incorrect_fractional_subtraction_for_exponent"]
    )


def arch_17_algebraic_expansion_before_differentiation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    b = rng.choice([-4, -1, 1, 3])
    # y = (ax + b)^2 = a^2 x^2 + 2ab x + b^2
    # dy/dx = 2a^2 x + 2ab
    a2 = a ** 2
    two_ab = 2 * a * b
    two_a2 = 2 * a2
    correct = f"{two_a2}x {'+' if two_ab >= 0 else '-'} {abs(two_ab)}"
    distractors = [
        f"{a2}x {'+' if two_ab >= 0 else '-'} {abs(two_ab)}",
        f"{two_a2}x",
        f"{a}x {'+' if b >= 0 else '-'} {abs(b)}",
    ]
    prompt = (
        f"Differentiate with respect to $x$ by first expanding the expression:\n\n"
        f"$$y = ({a}x {'+' if b >= 0 else '-'} {abs(b)})^2$$"
    )
    sol = (
        f"Step 1: Expand the squared binomial before differentiating:\n"
        f"$$y = ({a}x)^2 + 2({a}x)({b}) + ({b})^2 = {a2}x^2 {'+' if two_ab >= 0 else '-'} {abs(two_ab)}x + {b**2}$$\n"
        f"Step 2: Differentiate term by term:\n"
        f"$$\\frac{{dy}}{{dx}} = 2({a2})x {'+' if two_ab >= 0 else '-'} {abs(two_ab)} = {correct}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_17_{rng.randint(100000, 999999)}", "17_algebraic_expansion_before_differentiation",
        "Algebraic Binomial Expansion Prior to Differentiation", prompt, correct, distractors, sol,
        {"tier_1": "Expand (ax + b)^2 into quadratic standard form before applying the power rule.",
         "tier_2": f"Expansion gives {a2}x^2 + ({two_ab})x + {b**2}. Differentiate term-by-term.",
         "tier_3": correct},
        ["differentiated_inside_brackets_without_expanding"]
    )


def arch_18_algebraic_splitting_denominator_before_diff(rng: random.Random) -> Dict[str, Any]:
    c3 = rng.choice([2, 4, 6])
    c2 = rng.choice([-9, -3, 3, 9])
    c1 = rng.choice([-8, 4, 8])
    # f(x) = (c3*x^3 + c2*x^2 + c1*x) / x = c3*x^2 + c2*x + c1
    # f'(x) = 2*c3*x + c2
    two_c3 = 2 * c3
    correct = f"{two_c3}x {'+' if c2 >= 0 else '-'} {abs(c2)}"
    distractors = [
        f"{c3}x {'+' if c2 >= 0 else '-'} {abs(c2)}",
        f"{two_c3}x^2 {'+' if c2 >= 0 else '-'} {abs(c2)}x",
        f"{two_c3}x",
    ]
    prompt = (
        f"Determine $\\frac{{dy}}{{dx}}$ by splitting the fraction:\n\n"
        f"$$y = \\frac{{{c3}x^3 {'+' if c2 >= 0 else '-'} {abs(c2)}x^2 {'+' if c1 >= 0 else '-'} {abs(c1)}x}}{{x}}$$"
    )
    sol = (
        f"Step 1: Divide each term in the numerator by the denominator $x$:\n"
        f"$$y = \\frac{{{c3}x^3}}{{x}} {'+' if c2 >= 0 else '-'} \\frac{{{abs(c2)}x^2}}{{x}} {'+' if c1 >= 0 else '-'} \\frac{{{abs(c1)}x}}{{x}} = {c3}x^2 {'+' if c2 >= 0 else '-'} {abs(c2)}x {'+' if c1 >= 0 else '-'} {abs(c1)}$$\n"
        f"Step 2: Differentiate the resulting polynomial:\n"
        f"$$\\frac{{dy}}{{dx}} = {two_c3}x {'+' if c2 >= 0 else '-'} {abs(c2)}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_18_{rng.randint(100000, 999999)}", "18_algebraic_splitting_denominator_before_diff",
        "Splitting Monomial Denominator Before Differentiating", prompt, correct, distractors, sol,
        {"tier_1": "Divide each term in the numerator by x before differentiating.",
         "tier_2": f"y simplifies to {c3}x^2 + ({c2})x + ({c1}). Differentiate using power rule.",
         "tier_3": correct},
        ["attempted_quotient_rule_with_arithmetic_errors"]
    )


def arch_19_algebraic_factorisation_cancelling_before_diff(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    a3 = a ** 3
    # y = (x^3 - a^3) / (x - a) = x^2 + a*x + a^2
    # dy/dx = 2x + a
    correct = f"2x + {a}"
    distractors = [
        f"3x^2 - {a3}",
        f"2x - {a}",
        f"3x^2 / 1",
    ]
    prompt = (
        f"Determine $f'(x)$ if $f(x) = \\frac{{x^3 - {a3}}}{{x - {a}}}$ for $x \\ne {a}$."
    )
    sol = (
        f"Step 1: Factorise the difference of cubes in the numerator:\n"
        f"$$x^3 - {a3} = (x - {a})(x^2 + {a}x + {a**2})$$\n"
        f"Step 2: Cancel $(x - {a})$ for $x \\ne {a}$:\n"
        f"$$f(x) = x^2 + {a}x + {a**2}$$\n"
        f"Step 3: Differentiate the simplified quadratic:\n"
        f"$$f'(x) = 2x + {a}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_19_{rng.randint(100000, 999999)}", "19_algebraic_factorisation_cancelling_before_diff",
        "Difference of Cubes Factorisation Prior to Differentiation", prompt, correct, distractors, sol,
        {"tier_1": "Factorise the difference of cubes: x^3 - a^3 = (x - a)(x^2 + ax + a^2).",
         "tier_2": "Cancel the denominator and differentiate x^2 + ax + a^2.",
         "tier_3": correct},
        ["differentiated_numerator_and_denominator_separately"]
    )


def arch_20_derivative_at_given_x_numerical_value(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3])
    b = rng.choice([-6, -2, 4, 8])
    c = rng.choice([-5, 3, 7])
    x0 = rng.choice([-3, -1, 2, 4])
    # f(x) = a*x^2 + b*x + c  =>  f'(x) = 2a*x + b  =>  f'(x0) = 2a*x0 + b
    slope = 2 * a * x0 + b
    prompt = (
        f"Given $f(x) = {a if a != 1 else ''}x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c >= 0 else '-'} {abs(c)}$:\n\n"
        f"Calculate the gradient of the curve at the point where $x = {x0}$."
    )
    ans = str(slope)
    sol = (
        f"Step 1: Find the derivative $f'(x)$ using the power rule:\n"
        f"$$f'(x) = {2*a}x {'+' if b >= 0 else '-'} {abs(b)}$$\n"
        f"Step 2: Substitute $x = {x0}$:\n"
        f"$$f'({x0}) = {2*a}({x0}) {'+' if b >= 0 else '-'} {abs(b)} = {slope}$$."
    )
    return _calc_q(
        rng, f"g12_calc_20_{rng.randint(100000, 999999)}", "20_derivative_at_given_x_numerical_value",
        "Calculating Curve Gradient at a Given x-Value", prompt, ans, sol,
        {"tier_1": f"Find f'(x) = {2*a}x + ({b}).",
         "tier_2": f"Substitute x = {x0} into f'(x).",
         "tier_3": f"Gradient is {slope}."},
        ["confused_gradient_with_y_coordinate"]
    )


def arch_21_solve_x_for_given_derivative_value(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3])
    b = rng.choice([-4, -2, 2, 6])
    c = rng.choice([-3, 5])
    # f(x) = a*x^2 + b*x + c  =>  f'(x) = 2a*x + b
    # Target slope m
    x_target = rng.choice([-3, -2, 1, 3, 5])
    m_target = 2 * a * x_target + b
    prompt = (
        f"Given $f(x) = {a if a != 1 else ''}x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c >= 0 else '-'} {abs(c)}$:\n\n"
        f"Determine the value of $x$ for which the gradient of $f$ is equal to ${m_target}$."
    )
    ans = str(x_target)
    sol = (
        f"Step 1: Find the derivative expression:\n"
        f"$$f'(x) = {2*a}x {'+' if b >= 0 else '-'} {abs(b)}$$\n"
        f"Step 2: Equate $f'(x)$ to the given gradient ${m_target}$ and solve for $x$:\n"
        f"$${2*a}x {'+' if b >= 0 else '-'} {abs(b)} = {m_target}$$\n"
        f"$${2*a}x = {m_target - b} \\implies x = {x_target}$$."
    )
    return _calc_q(
        rng, f"g12_calc_21_{rng.randint(100000, 999999)}", "21_solve_x_for_given_derivative_value",
        "Solving for x Corresponding to a Given Gradient", prompt, ans, sol,
        {"tier_1": "Find f'(x) and set f'(x) equal to the given gradient.",
         "tier_2": f"{2*a}x + ({b}) = {m_target}. Solve this linear equation for x.",
         "tier_3": f"x = {x_target}."},
        ["equated_f_instead_of_f_prime_to_gradient"]
    )


def arch_22_gradient_of_tangent_to_curve(rng: random.Random) -> Dict[str, Any]:
    c3 = rng.choice([1, 2])
    c1 = rng.choice([-5, -3, 3, 6])
    x0 = rng.choice([-2, -1, 1, 2])
    # f(x) = c3*x^3 + c1*x  =>  f'(x) = 3*c3*x^2 + c1
    m_tangent = 3 * c3 * (x0 ** 2) + c1
    prompt = (
        f"Find the gradient of the tangent to the cubic curve $y = {c3 if c3 != 1 else ''}x^3 {'+' if c1 >= 0 else '-'} {abs(c1)}x$ "
        f"at the point where $x = {x0}$."
    )
    ans = str(m_tangent)
    sol = (
        f"Step 1: Differentiate to find the gradient function $\\frac{{dy}}{{dx}}$:\n"
        f"$$\\frac{{dy}}{{dx}} = {3*c3}x^2 {'+' if c1 >= 0 else '-'} {abs(c1)}$$\n"
        f"Step 2: Evaluate the derivative at $x = {x0}$:\n"
        f"$$m = {3*c3}({x0})^2 {'+' if c1 >= 0 else '-'} {abs(c1)} = {3*c3 * (x0**2)} {'+' if c1 >= 0 else '-'} {abs(c1)} = {m_tangent}$$."
    )
    return _calc_q(
        rng, f"g12_calc_22_{rng.randint(100000, 999999)}", "22_gradient_of_tangent_to_curve",
        "Gradient of Tangent to Cubic Curve at Given Point", prompt, ans, sol,
        {"tier_1": "The gradient of the tangent is given by the derivative dy/dx evaluated at x = x0.",
         "tier_2": f"Find dy/dx = {3*c3}x^2 + ({c1}) and substitute x = {x0}.",
         "tier_3": f"m = {m_tangent}."},
        ["evaluated_original_function_instead_of_derivative"]
    )


def arch_23_equation_of_tangent_line_to_parabola(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2])
    b = rng.choice([-3, 2, 4])
    c = rng.choice([-4, 1, 5])
    x0 = rng.choice([-2, 1, 2])
    # y = a*x^2 + b*x + c
    y0 = a * (x0 ** 2) + b * x0 + c
    m = 2 * a * x0 + b
    # Tangent: y - y0 = m(x - x0)  =>  y = m*x + (y0 - m*x0)
    c_line = y0 - m * x0
    correct = f"y = {m}x {'+' if c_line >= 0 else '-'} {abs(c_line)}"
    distractors = [
        f"y = {m}x {'-' if c_line >= 0 else '+'} {abs(c_line)}",
        f"y = {2*a}x {'+' if c_line >= 0 else '-'} {abs(c_line)}",
        f"y = -{m}x {'+' if c_line >= 0 else '-'} {abs(c_line)}",
    ]
    prompt = (
        f"Determine the equation of the tangent line to the parabola "
        f"$f(x) = {a if a != 1 else ''}x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c >= 0 else '-'} {abs(c)}$ "
        f"at the point where $x = {x0}$. Express your answer in the form $y = mx + c$."
    )
    sol = (
        f"Step 1: Calculate the $y$-coordinate of the point of contact:\n"
        f"$$y_0 = f({x0}) = {a}({x0})^2 {'+' if b >= 0 else '-'} {abs(b)}({x0}) {'+' if c >= 0 else '-'} {abs(c)} = {y0}$$\n"
        f"Point of contact is $({x0};\\ {y0})$.\n"
        f"Step 2: Differentiate to find gradient $m$:\n"
        f"$$f'(x) = {2*a}x {'+' if b >= 0 else '-'} {abs(b)}$$\n"
        f"$$m = f'({x0}) = {2*a}({x0}) {'+' if b >= 0 else '-'} {abs(b)} = {m}$$\n"
        f"Step 3: Use point-slope equation $y - y_0 = m(x - x_0)$:\n"
        f"$$y - ({y0}) = {m}(x - ({x0}))$$\n"
        f"$$y = {m}x - {m * x0} + {y0} = {correct}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_23_{rng.randint(100000, 999999)}", "23_equation_of_tangent_line_to_parabola",
        "Equation of Tangent Line to Parabola in Slope-Intercept Form", prompt, correct, distractors, sol,
        {"tier_1": "1. Find y0 by substituting x0 into f(x). 2. Find m = f'(x0). 3. Use y - y0 = m(x - x0).",
         "tier_2": f"Point is ({x0}, {y0}) and slope is {m}. Solve y = {m}x + c.",
         "tier_3": correct},
        ["sign_error_in_point_slope_formula"]
    )


def arch_24_equation_of_tangent_line_to_cubic(rng: random.Random) -> Dict[str, Any]:
    # f(x) = x^3 - 3x + 2 at x = 2
    # f'(x) = 3x^2 - 3
    x0 = rng.choice([-1, 0, 1, 2])
    k = rng.choice([2, 3])
    # f(x) = x^3 - k*x + 1
    y0 = (x0 ** 3) - k * x0 + 1
    m = 3 * (x0 ** 2) - k
    c_line = y0 - m * x0
    correct = f"y = {m}x {'+' if c_line >= 0 else '-'} {abs(c_line)}"
    distractors = [
        f"y = {m}x {'-' if c_line >= 0 else '+'} {abs(c_line)}",
        f"y = {3*(x0**2)}x + 1",
        f"y = -{m}x {'+' if c_line >= 0 else '-'} {abs(c_line)}",
    ]
    prompt = (
        f"Find the equation of the tangent line to the cubic function $y = x^3 - {k}x + 1$ "
        f"at the point where $x = {x0}$."
    )
    sol = (
        f"Step 1: Point of tangency:\n"
        f"$$y_0 = ({x0})^3 - {k}({x0}) + 1 = {y0} \\implies ({x0};\\ {y0})$$\n"
        f"Step 2: Gradient of tangent:\n"
        f"$$y' = 3x^2 - {k}$$\n"
        f"$$m = 3({x0})^2 - {k} = {m}$$\n"
        f"Step 3: Tangent line equation:\n"
        f"$$y - ({y0}) = {m}(x - ({x0})) \\implies {correct}$$."
    )
    return _mcq_q(
        rng, f"g12_calc_24_{rng.randint(100000, 999999)}", "24_equation_of_tangent_line_to_cubic",
        "Equation of Tangent Line to Cubic Function", prompt, correct, distractors, sol,
        {"tier_1": "Find y0 by substituting x0 into the cubic equation.",
         "tier_2": f"Find m = 3({x0})^2 - {k} and use y - y0 = m(x - x0).",
         "tier_3": correct},
        ["forgot_to_evaluate_point_on_cubic"]
    )


def arch_25_tangent_parallel_to_given_linear_equation(rng: random.Random) -> Dict[str, Any]:
    # Curve: y = x^2 - 4x + 1
    # Line: y = 2x + 7  =>  m = 2  =>  2x - 4 = 2  =>  2x = 6  =>  x = 3
    a = 1
    b = rng.choice([-6, -4, 2, 4])
    m_line = rng.choice([-2, 2, 4, 6])
    # 2*a*x + b = m_line => 2x = m_line - b => ensure even
    while (m_line - b) % 2 != 0:
        m_line += 1
    x_contact = (m_line - b) // 2
    c_curve = rng.choice([-3, 1, 5])
    y_contact = (x_contact ** 2) + b * x_contact + c_curve
    c_line = rng.choice([-8, 3, 11])
    prompt = (
        f"A curve has equation $f(x) = x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c_curve >= 0 else '-'} {abs(c_curve)}$.\n\n"
        f"Determine the coordinates of the point on the curve where the tangent line is parallel to the straight line $y = {m_line}x {'+' if c_line >= 0 else '-'} {abs(c_line)}$."
    )
    correct = f"({x_contact}; {y_contact})"
    distractors = [
        f"({x_contact}; {-y_contact})",
        f"({-x_contact}; {y_contact})",
        f"({m_line}; {c_line})",
    ]
    sol = (
        f"Step 1: Parallel lines have equal gradients:\n"
        f"The straight line has gradient $m = {m_line}$.\n"
        f"Step 2: Differentiate the curve and equate $f'(x) = {m_line}$:\n"
        f"$$f'(x) = 2x {'+' if b >= 0 else '-'} {abs(b)}$$\n"
        f"$$2x {'+' if b >= 0 else '-'} {abs(b)} = {m_line}$$\n"
        f"$$2x = {m_line - b} \\implies x = {x_contact}$$\n"
        f"Step 3: Find the $y$-coordinate on the curve:\n"
        f"$$y = ({x_contact})^2 {'+' if b >= 0 else '-'} {abs(b)}({x_contact}) {'+' if c_curve >= 0 else '-'} {abs(c_curve)} = {y_contact}$$\n"
        f"The point of contact is $({x_contact};\\ {y_contact})$."
    )
    return _mcq_q(
        rng, f"g12_calc_25_{rng.randint(100000, 999999)}", "25_tangent_parallel_to_given_linear_equation",
        "Point of Tangency Parallel to Given Linear Equation", prompt, correct, distractors, sol,
        {"tier_1": f"Parallel means equal gradients: set f'(x) = {m_line}.",
         "tier_2": f"Solve 2x + ({b}) = {m_line} to find x = {x_contact}, then substitute into f(x) for y.",
         "tier_3": correct},
        ["substituted_x_into_straight_line_instead_of_curve"]
    )


# ==============================================================================
# Subskills Dictionary and Builders Mapping for 01 - 25
# ==============================================================================

BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_limit_of_function_direct_substitution": arch_01_limit_of_function_direct_substitution,
    "02_limit_indeterminate_factorisation": arch_02_limit_indeterminate_factorisation,
    "03_limit_rationalise_numerator": arch_03_limit_rationalise_numerator,
    "04_average_gradient_secant_line": arch_04_average_gradient_secant_line,
    "05_average_gradient_interval_notation": arch_05_average_gradient_interval_notation,
    "06_first_principles_linear_function": arch_06_first_principles_linear_function,
    "07_first_principles_monic_quadratic": arch_07_first_principles_monic_quadratic,
    "08_first_principles_general_quadratic": arch_08_first_principles_general_quadratic,
    "09_first_principles_negative_leading_coeff": arch_09_first_principles_negative_leading_coeff,
    "10_first_principles_hyperbolic_fraction": arch_10_first_principles_hyperbolic_fraction,
    "11_first_principles_cubic_monic": arch_11_first_principles_cubic_monic,
    "12_first_principles_evaluate_at_specific_point": arch_12_first_principles_evaluate_at_specific_point,
    "13_power_rule_polynomial_terms": arch_13_power_rule_polynomial_terms,
    "14_derivative_notation_d_dx_and_dy_dx": arch_14_derivative_notation_d_dx_and_dy_dx,
    "15_differentiation_negative_exponents": arch_15_differentiation_negative_exponents,
    "16_differentiation_fractional_surd_exponents": arch_16_differentiation_fractional_surd_exponents,
    "17_algebraic_expansion_before_differentiation": arch_17_algebraic_expansion_before_differentiation,
    "18_algebraic_splitting_denominator_before_diff": arch_18_algebraic_splitting_denominator_before_diff,
    "19_algebraic_factorisation_cancelling_before_diff": arch_19_algebraic_factorisation_cancelling_before_diff,
    "20_derivative_at_given_x_numerical_value": arch_20_derivative_at_given_x_numerical_value,
    "21_solve_x_for_given_derivative_value": arch_21_solve_x_for_given_derivative_value,
    "22_gradient_of_tangent_to_curve": arch_22_gradient_of_tangent_to_curve,
    "23_equation_of_tangent_line_to_parabola": arch_23_equation_of_tangent_line_to_parabola,
    "24_equation_of_tangent_line_to_cubic": arch_24_equation_of_tangent_line_to_cubic,
    "25_tangent_parallel_to_given_linear_equation": arch_25_tangent_parallel_to_given_linear_equation,
}

SUBSKILLS_01_25: Dict[str, str] = {
    "01_limit_of_function_direct_substitution": "Limit of Polynomial by Direct Substitution",
    "02_limit_indeterminate_factorisation": "Evaluating Indeterminate Limit by Factorisation",
    "03_limit_rationalise_numerator": "Limit Involving Square Roots and Rationalisation",
    "04_average_gradient_secant_line": "Average Gradient of Quadratic Curve Between Two Points",
    "05_average_gradient_interval_notation": "Average Rate of Change Over a Closed Interval",
    "06_first_principles_linear_function": "Differentiation of Linear Function from First Principles",
    "07_first_principles_monic_quadratic": "Differentiation of Monic Quadratic from First Principles",
    "08_first_principles_general_quadratic": "Differentiation of General Quadratic from First Principles",
    "09_first_principles_negative_leading_coeff": "First Principles with Negative Leading Coefficient",
    "10_first_principles_hyperbolic_fraction": "Differentiation of Hyperbolic Function from First Principles",
    "11_first_principles_cubic_monic": "Differentiation of Monic Cubic from First Principles",
    "12_first_principles_evaluate_at_specific_point": "Derivative Evaluated at a Specific Point Using First Principles",
    "13_power_rule_polynomial_terms": "Power Rule Differentiation of Cubic Polynomial",
    "14_derivative_notation_d_dx_and_dy_dx": "Differentiation Using Operator Notation D_x",
    "15_differentiation_negative_exponents": "Differentiation with Negative Exponents",
    "16_differentiation_fractional_surd_exponents": "Differentiation of Radical Terms with Fractional Exponents",
    "17_algebraic_expansion_before_differentiation": "Algebraic Binomial Expansion Prior to Differentiation",
    "18_algebraic_splitting_denominator_before_diff": "Splitting Monomial Denominator Before Differentiating",
    "19_algebraic_factorisation_cancelling_before_diff": "Difference of Cubes Factorisation Prior to Differentiation",
    "20_derivative_at_given_x_numerical_value": "Calculating Curve Gradient at a Given x-Value",
    "21_solve_x_for_given_derivative_value": "Solving for x Corresponding to a Given Gradient",
    "22_gradient_of_tangent_to_curve": "Gradient of Tangent to Cubic Curve at Given Point",
    "23_equation_of_tangent_line_to_parabola": "Equation of Tangent Line to Parabola in Slope-Intercept Form",
    "24_equation_of_tangent_line_to_cubic": "Equation of Tangent Line to Cubic Function",
    "25_tangent_parallel_to_given_linear_equation": "Point of Tangency Parallel to Given Linear Equation",
}
