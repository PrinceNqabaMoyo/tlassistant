"""Grade 12 Mathematics - Functions and Polynomials Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/Mathematics_Gr12/Term 1/02. Functions.md and 03. Polynomials.md.
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
    curriculum_ref: str = "Term 1 > Functions and Inverses",
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
    curriculum_ref: str = "Term 1 > Functions and Inverses",
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


# =========================================================================== #
# Archetypes 01 - 25
# =========================================================================== #

def arch_01_function_definition_vertical_line_test(rng: random.Random) -> Dict[str, Any]:
    relation_type = rng.choice(["parabola_sideways", "circle", "parabola_standard", "hyperbola"])
    if relation_type in ("parabola_sideways", "circle"):
        rel_name = "x = y^2" if relation_type == "parabola_sideways" else "x^2 + y^2 = 16"
        is_func = False
        reason = "A vertical line x = k (for k > 0) intersects the curve at more than one point (one x-value corresponds to two y-values)"
    else:
        rel_name = "y = 2x^2 - 3" if relation_type == "parabola_standard" else "y = 3/x"
        is_func = True
        reason = "Every vertical line intersects the curve at most once (each x-value in the domain maps to exactly one y-value)"

    prompt = (
        f"Consider the relation defined by the equation ${rel_name}$.\n\n"
        f"1. Is this relation a function? State YES or NO.\n"
        f"2. Justify your answer using the vertical line test and the definition of a function."
    )
    correct = f"{'YES' if is_func else 'NO'} — {reason}"
    distractors = [
        f"{'NO' if is_func else 'YES'} — {'Every relation with real coefficients is automatically a function' if is_func else 'It passes the vertical line test everywhere'}",
        f"{'YES' if is_func else 'NO'} — Because it has x-intercepts",
        f"{'NO' if is_func else 'YES'} — Because it has a turning point",
    ]
    sol = (
        f"Step 1: Definition of a function:\n"
        f"A relation is a function if and only if each element of the domain maps to exactly one element of the range.\n"
        f"Step 2: Vertical Line Test for ${rel_name}$:\n"
        f"{reason}.\n"
        f"Conclusion: {'It is a function.' if is_func else 'It is NOT a function.'}"
    )
    return _mcq_q(
        rng, f"g12_fn_01_{rng.randint(100000, 999999)}", "01_function_definition_vertical_line_test",
        "Function Definition and Vertical Line Test", prompt, correct, distractors, sol,
        {"tier_1": "Recall the vertical line test: if any vertical line touches the curve twice, it is NOT a function.",
         "tier_2": f"Test vertical lines on ${rel_name}$.",
         "tier_3": correct},
        ["confuses_vertical_and_horizontal_line_tests"]
    )


def arch_02_horizontal_line_test_invertibility(rng: random.Random) -> Dict[str, Any]:
    fn_choice = rng.choice(["quadratic", "linear", "exponential", "cubic_monic"])
    if fn_choice == "quadratic":
        fn_name = "f(x) = 2x^2"
        is_one_to_one = False
        inv_is_func = False
        detail = "f is many-to-one; horizontal lines y = k (k > 0) cut the curve twice, so f^-1 is NOT a function"
    elif fn_choice == "linear":
        fn_name = "f(x) = 3x - 5"
        is_one_to_one = True
        inv_is_func = True
        detail = "f is one-to-one; every horizontal line cuts the curve at most once, so f^-1 IS a function"
    elif fn_choice == "exponential":
        fn_name = "f(x) = 2^x"
        is_one_to_one = True
        inv_is_func = True
        detail = "f is one-to-one; horizontal lines cut at most once, so f^-1 (the logarithm) IS a function"
    else:
        fn_name = "f(x) = x^3"
        is_one_to_one = True
        inv_is_func = True
        detail = "f is strictly increasing and one-to-one, so f^-1 IS a function"

    prompt = (
        f"Given the function ${fn_name}$ defined for all $x \\in \\mathbb{{R}}$:\n\n"
        f"Apply the horizontal line test to determine whether ${fn_name}$ is one-to-one, and deduce whether its inverse $f^{{-1}}$ is a function."
    )
    correct = detail
    distractors = [
        f"f is one-to-one and f^-1 is NOT a function",
        f"f is many-to-one and f^-1 IS a function",
        f"f is neither one-to-one nor many-to-one",
    ]
    sol = (
        f"Step 1: Horizontal Line Test principle:\n"
        f"If every horizontal line intersects the curve of $f(x)$ at most once, then $f(x)$ is one-to-one, which guarantees that its inverse $f^{{-1}}$ will pass the vertical line test and be a function.\n"
        f"Step 2: Analysis for ${fn_name}$:\n"
        f"{detail}."
    )
    return _mcq_q(
        rng, f"g12_fn_02_{rng.randint(100000, 999999)}", "02_horizontal_line_test_invertibility",
        "Horizontal Line Test and Invertibility", prompt, correct, distractors, sol,
        {"tier_1": "The horizontal line test determines whether the inverse of a function will be a function.",
         "tier_2": f"Does any horizontal line cross ${fn_name}$ at more than one point?",
         "tier_3": correct},
        ["confuses_one_to_one_with_many_to_one"]
    )


def arch_03_linear_function_inverse_equation(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([-4, -3, -2, 2, 3, 5])
    c = rng.choice([-6, -4, 2, 5, 8])
    # y = m*x + c  =>  x = m*y + c  =>  y = (x - c)/m = (1/m)*x - c/m
    prompt = (
        f"Given the linear function $f(x) = {m}x {'+' if c >= 0 else '-'} {abs(c)}$:\n\n"
        f"Determine the equation of the inverse function $f^{{-1}}(x)$ in the form $y = mx + c$."
    )
    # Formulate string
    c_inv = -c
    correct = f"y = (x {'+' if c_inv >= 0 else '-'} {abs(c_inv)}) / {m}"
    distractors = [
        f"y = {m}x {'-' if c >= 0 else '+'} {abs(c)}",
        f"y = -{m}x {'+' if c >= 0 else '-'} {abs(c)}",
        f"y = (x {'-' if c_inv >= 0 else '+'} {abs(c_inv)}) / {m}",
    ]
    sol = (
        f"Step 1: Write $y = {m}x {'+' if c >= 0 else '-'} {abs(c)}$.\n"
        f"Step 2: To find the inverse, swap $x$ and $y$:\n"
        f"$$x = {m}y {'+' if c >= 0 else '-'} {abs(c)}$$\n"
        f"Step 3: Make $y$ the subject of the formula:\n"
        f"$${m}y = x {'-' if c >= 0 else '+'} {abs(c)}$$\n"
        f"$$y = \\frac{{x {'-' if c >= 0 else '+'} {abs(c)}}}{{{m}}} = {correct}$$."
    )
    return _mcq_q(
        rng, f"g12_fn_03_{rng.randint(100000, 999999)}", "03_linear_function_inverse_equation",
        "Equation of Linear Function Inverse", prompt, correct, distractors, sol,
        {"tier_1": "Interchange x and y in the original equation and solve for y.",
         "tier_2": f"x = {m}y + ({c}). Subtract {c} and divide by {m}.",
         "tier_3": correct},
        ["forgot_to_swap_variables_before_rearranging"]
    )


def arch_04_linear_function_inverse_coordinates(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([-4, -2, 1, 3, 5])
    m = rng.choice([2, 3, 4])
    c = rng.choice([-3, 2, 4])
    q = m * p + c
    prompt = (
        f"The point $A({p};\\ {q})$ lies on the linear function $f(x) = {m}x {'+' if c >= 0 else '-'} {abs(c)}$.\n\n"
        f"1. State the coordinates of the corresponding point $A'$ on the inverse $f^{{-1}}(x)$.\n"
        f"2. Write down the $y$-intercept and $x$-intercept of $f^{{-1}}(x)$."
    )
    # f has y-intercept (0, c) and x-intercept (-c/m, 0)
    # f^-1 has y-intercept (-c/m, 0) becomes (0, -c/m), and x-intercept (c, 0)
    correct = f"A'({q}; {p}); x-intercept is ({c}; 0); y-intercept is (0; {-c/m:.2f})"
    distractors = [
        f"A'({-p}; {-q}); x-intercept is (0; {c}); y-intercept is ({-c/m:.2f}; 0)",
        f"A'({p}; {-q}); x-intercept is ({c}; 0); y-intercept is (0; {c/m:.2f})",
        f"A'({q}; {p}); x-intercept is (0; {c}); y-intercept is ({-c/m:.2f}; 0)",
    ]
    sol = (
        f"Step 1: Point reflection:\n"
        f"Any point $(x; y)$ on $f$ reflects across the line of symmetry $y = x$ to become $(y; x)$ on $f^{{-1}}$.\n"
        f"Thus $A({p};\\ {q}) \\implies A'({q};\\ {p})$.\n"
        f"Step 2: Intercepts:\n"
        f"The $y$-intercept of $f$ is $(0;\\ {c})$, which becomes the $x$-intercept of $f^{{-1}}$: $({c};\\ 0)$.\n"
        f"The $x$-intercept of $f$ is $(\\frac{{{-c}}}{{{m}}};\\ 0)$, which becomes the $y$-intercept of $f^{{-1}}$: $(0;\\ \\frac{{{-c}}}{{{m}}} = { -c/m:.2f})$."
    )
    return _mcq_q(
        rng, f"g12_fn_04_{rng.randint(100000, 999999)}", "04_linear_function_inverse_coordinates",
        "Coordinate Transformations for Linear Inverses", prompt, correct, distractors, sol,
        {"tier_1": "Reflecting across y = x simply swaps the x- and y-coordinates: (x, y) becomes (y, x).",
         "tier_2": f"Point A({p}, {q}) becomes A'({q}, {p}). Swapping also swaps intercepts.",
         "tier_3": correct},
        ["inverted_signs_instead_of_swapping_coordinates"]
    )


def arch_05_linear_function_inverse_line_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    # f(x) = mx + c. Intersects f^-1 on the line y = x.
    # mx + c = x => (m - 1)x = -c => x = -c / (m - 1).
    m = rng.choice([2, 3, 4])
    k_mult = rng.choice([-4, -2, 2, 3])
    # Choose c so x is integer: c = -k_mult * (m - 1)
    c = -k_mult * (m - 1)
    x_int = k_mult
    y_int = k_mult
    prompt = (
        f"Given the linear function $f(x) = {m}x {'+' if c >= 0 else '-'} {abs(c)}$ and its inverse $f^{{-1}}(x)$:\n\n"
        f"1. Name the line of symmetry between $f(x)$ and $f^{{-1}}(x)$.\n"
        f"2. Calculate the coordinates of the point where $f(x)$ and $f^{{-1}}(x)$ intersect each other."
    )
    correct = f"Line of symmetry is y = x; Intersection point is ({x_int}; {y_int})"
    distractors = [
        f"Line of symmetry is y = -x; Intersection point is ({-x_int}; {y_int})",
        f"Line of symmetry is y = 0; Intersection point is ({x_int}; 0)",
        f"Line of symmetry is x = 0; Intersection point is (0; {y_int})",
    ]
    sol = (
        f"Step 1: A function and its inverse are reflections of each other in the line of symmetry $y = x$.\n"
        f"Step 2: Point of intersection:\n"
        f"Since $f$ and $f^{{-1}}$ meet on the line $y = x$, we equate $f(x) = x$:\n"
        f"$${m}x {'+' if c >= 0 else '-'} {abs(c)} = x$$\n"
        f"$${m - 1}x = {-c} \\implies x = {x_int}$$\n"
        f"Since $y = x$, $y = {y_int}$. Point of intersection is $({x_int};\\ {y_int})$."
    )
    return _mcq_q(
        rng, f"g12_fn_05_{rng.randint(100000, 999999)}", "05_linear_function_inverse_line_of_symmetry",
        "Line of Symmetry and Intersection of Function with Inverse", prompt, correct, distractors, sol,
        {"tier_1": "A function and its inverse always reflect across the line y = x.",
         "tier_2": f"Equate {m}x + ({c}) = x and solve for x.",
         "tier_3": correct},
        ["confused_line_of_symmetry_with_axes"]
    )


def arch_06_quadratic_inverse_equation_full(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3, 4])
    prompt = (
        f"Given the parabola $f(x) = {a if a != 1 else ''}x^2$ for all $x \\in \\mathbb{{R}}$:\n\n"
        f"Determine the algebraic equation of the inverse relation $f^{{-1}}$."
    )
    correct = f"y = \\pm \\sqrt{{x / {a}}}" if a != 1 else "y = \\pm \\sqrt{x}"
    distractors = [
        f"y = \\sqrt{{x / {a}}}" if a != 1 else "y = \\sqrt{x}",
        f"y = -\\sqrt{{x / {a}}}" if a != 1 else "y = -\\sqrt{x}",
        f"y = {a if a != 1 else ''} \\sqrt{{x}}",
    ]
    sol = (
        f"Step 1: Write $y = {a if a != 1 else ''}x^2$.\n"
        f"Step 2: Swap $x$ and $y$ to determine the inverse:\n"
        f"$$x = {a if a != 1 else ''}y^2$$\n"
        f"Step 3: Solve for $y$:\n"
        f"$$y^2 = \\frac{{x}}{{{a}}}$$\n"
        f"$$y = \\pm \\sqrt{{\\frac{{x}}{{{a}}}}} = {correct}$$\n"
        f"(Notice the plus-or-minus sign is mandatory when taking square root of both sides)."
    )
    return _mcq_q(
        rng, f"g12_fn_06_{rng.randint(100000, 999999)}", "06_quadratic_inverse_equation_full",
        "Full Inverse Relation of a Parabola", prompt, correct, distractors, sol,
        {"tier_1": "Swap x and y to get x = a*y^2.",
         "tier_2": "Taking square root introduces both positive and negative roots: plus-or-minus.",
         "tier_3": correct},
        ["omitted_plus_minus_when_taking_square_root"]
    )


def arch_07_quadratic_inverse_why_not_function(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3])
    x_test = rng.choice([4, 9, 16])
    y_pos = math.sqrt(x_test / a) if a == 1 else math.sqrt(x_test / a)
    prompt = (
        f"Explain why the inverse relation $x = {a if a != 1 else ''}y^2$ ($y = \\pm \\sqrt{{x / {a if a != 1 else ''}}}$) "
        f"is **not** a function for the domain $x > 0$."
    )
    correct = "For any input x > 0, there are two distinct output values (+sqrt(x/a) and -sqrt(x/a)), violating the one-to-one or many-to-one definition of a function"
    distractors = [
        "Because quadratic functions can never have inverses under any circumstances",
        "Because the domain of x contains negative numbers",
        "Because square root relations are vertical lines",
    ]
    sol = (
        f"Step 1: Recall the definition of a function:\n"
        f"A relation is a function if each element in the domain is mapped to exactly one element in the range.\n"
        f"Step 2: Evaluate at $x = {x_test}$:\n"
        f"$y = \\pm \\sqrt{{{x_test} / {a}}}$ gives both $y = +\\sqrt{{{x_test / a:.2f}}}$ and $y = -\\sqrt{{{x_test / a:.2f}}}$.\n"
        f"Since a single $x$ produces two different $y$ values, the vertical line test fails, so it is NOT a function."
    )
    return _mcq_q(
        rng, f"g12_fn_07_{rng.randint(100000, 999999)}", "07_quadratic_inverse_why_not_function",
        "Why Quadratic Inverse Fails Function Definition", prompt, correct, distractors, sol,
        {"tier_1": "A relation is a function only if each input x produces exactly ONE output y.",
         "tier_2": "The plus-or-minus sign gives two outputs for every positive x.",
         "tier_3": correct},
        ["assumed_parabola_inverse_is_always_a_function"]
    )


def arch_08_quadratic_domain_restriction_positive(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3, 4])
    prompt = (
        f"Given $f(x) = {a if a != 1 else ''}x^2$ with domain restricted to $x \\ge 0$:\n\n"
        f"1. Is the inverse $f^{{-1}}$ now a function?\n"
        f"2. Write down the equation and domain of $f^{{-1}}(x)$."
    )
    correct = f"Yes, a function; equation is y = \\sqrt{{x / {a}}}; domain is x >= 0" if a != 1 else "Yes, a function; equation is y = \\sqrt{x}; domain is x >= 0"
    distractors = [
        f"Yes, a function; equation is y = -\\sqrt{{x / {a}}}; domain is x <= 0" if a != 1 else "Yes, a function; equation is y = -\\sqrt{x}; domain is x <= 0",
        f"No, not a function; equation is y = \\pm \\sqrt{{x / {a}}}; domain is x >= 0" if a != 1 else "No, not a function; equation is y = \\pm \\sqrt{x}; domain is x >= 0",
        f"Yes, a function; equation is y = {a if a != 1 else ''}x^2; domain is x >= 0",
    ]
    sol = (
        f"Step 1: Restricting the domain of $f$ to $x \\ge 0$ makes $f$ one-to-one (the right half of the parabola).\n"
        f"Step 2: Range of $f(x)$ for $x \\ge 0$ is $y \\ge 0$.\n"
        f"Step 3: On the inverse, domain and range interchange:\n"
        f"Domain of $f^{{-1}}$ is $x \\ge 0$; range is $y \\ge 0$.\n"
        f"Because $y \\ge 0$, we select the positive root: $y = {correct.split(';')[1].replace('equation is ', '').strip()}$."
    )
    return _mcq_q(
        rng, f"g12_fn_08_{rng.randint(100000, 999999)}", "08_quadratic_domain_restriction_positive",
        "Quadratic Invertibility with Domain Restriction x >= 0", prompt, correct, distractors, sol,
        {"tier_1": "Restricting x >= 0 keeps only the positive branch of the inverse square root.",
         "tier_2": "The inverse is the upper half: y = +sqrt(x/a) with domain x >= 0.",
         "tier_3": correct},
        ["forgot_to_drop_negative_root_after_restriction"]
    )


def arch_09_quadratic_domain_restriction_negative(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1, 2, 3])
    prompt = (
        f"The domain of $f(x) = {a if a != 1 else ''}x^2$ is restricted to $x \\le 0$.\n\n"
        f"Determine the equation and range of the inverse function $f^{{-1}}(x)$."
    )
    eq_str = f"y = -\\sqrt{{x / {a}}}" if a != 1 else "y = -\\sqrt{x}"
    correct = f"{eq_str}; range is y <= 0 (domain x >= 0)"
    distractors = [
        f"y = \\sqrt{{x / {a}}}; range is y >= 0",
        f"y = \\pm \\sqrt{{x / {a}}}; range is y in R",
        f"y = -{a if a != 1 else ''}x^2; range is y <= 0",
    ]
    sol = (
        f"Step 1: Domain of $f$ is $x \\le 0$, range of $f$ is $y \\ge 0$.\n"
        f"Step 2: Interchanging domain and range for $f^{{-1}}$:\n"
        f"Domain of $f^{{-1}}$ is $x \\ge 0$, and range of $f^{{-1}}$ is $y \\le 0$.\n"
        f"Step 3: Since $y \\le 0$, we must choose the negative branch:\n"
        f"$${eq_str}$$."
    )
    return _mcq_q(
        rng, f"g12_fn_09_{rng.randint(100000, 999999)}", "09_quadratic_domain_restriction_negative",
        "Quadratic Invertibility with Domain Restriction x <= 0", prompt, correct, distractors, sol,
        {"tier_1": "When original domain is x <= 0, the range of the inverse must be y <= 0.",
         "tier_2": f"Select the negative root: y = -sqrt(x / {a}).",
         "tier_3": correct},
        ["chose_positive_root_for_negative_domain_branch"]
    )


def arch_10_quadratic_with_vertical_shift_inverse(rng: random.Random) -> Dict[str, Any]:
    q_shift = rng.choice([-4, -2, 1, 3, 5])
    # f(x) = x^2 + q for x >= 0
    # y = x^2 + q => x = y^2 + q => y^2 = x - q => y = sqrt(x - q)
    prompt = (
        f"Given $f(x) = x^2 {'+' if q_shift >= 0 else '-'} {abs(q_shift)}$ for $x \\ge 0$:\n\n"
        f"1. Determine the equation of $f^{{-1}}(x)$.\n"
        f"2. State the domain of $f^{{-1}}(x)$."
    )
    correct = f"y = \\sqrt{{x {'-' if q_shift >= 0 else '+'} {abs(q_shift)}}}; domain is x >= {q_shift}"
    distractors = [
        f"y = \\sqrt{{x {'+' if q_shift >= 0 else '-'} {abs(q_shift)}}}; domain is x >= {-q_shift}",
        f"y = \\pm \\sqrt{{x {'-' if q_shift >= 0 else '+'} {abs(q_shift)}}}; domain is x in R",
        f"y = x^2 {'-' if q_shift >= 0 else '+'} {abs(q_shift)}; domain is x >= 0",
    ]
    sol = (
        f"Step 1: Write $y = x^2 {'+' if q_shift >= 0 else '-'} {abs(q_shift)}$.\n"
        f"Step 2: Swap $x$ and $y$:\n"
        f"$$x = y^2 {'+' if q_shift >= 0 else '-'} {abs(q_shift)}$$\n"
        f"$$y^2 = x {'-' if q_shift >= 0 else '+'} {abs(q_shift)}$$\n"
        f"Step 3: Because domain of $f$ is $x \\ge 0$, range of $f^{{-1}}$ is $y \\ge 0$:\n"
        f"$$y = \\sqrt{{x {'-' if q_shift >= 0 else '+'} {abs(q_shift)}}}$$\n"
        f"Step 4: Domain of $f^{{-1}}$ equals range of $f$, which is $x \\ge {q_shift}$."
    )
    return _mcq_q(
        rng, f"g12_fn_10_{rng.randint(100000, 999999)}", "10_quadratic_with_vertical_shift_inverse",
        "Inverse of Shifted Parabola with Domain Restriction", prompt, correct, distractors, sol,
        {"tier_1": f"Swap x and y: x = y^2 + ({q_shift}). Isolate y^2.",
         "tier_2": f"Domain of the inverse is x >= {q_shift} because the expression under the square root must be non-negative.",
         "tier_3": correct},
        ["sign_error_shifting_under_radical"]
    )


def arch_11_quadratic_turning_point_and_axis_of_symmetry_inverse(rng: random.Random) -> Dict[str, Any]:
    q_val = rng.choice([-5, -3, 2, 4, 7])
    prompt = (
        f"The parabola $f(x) = 2x^2 {'+' if q_val >= 0 else '-'} {abs(q_val)}$ has a turning point at $(0;\\ {q_val})$ "
        f"and axis of symmetry $x = 0$.\n\n"
        f"What are the turning point and axis of symmetry of its inverse relation $f^{{-1}}$?"
    )
    correct = f"Turning point is ({q_val}; 0); axis of symmetry is y = 0"
    distractors = [
        f"Turning point is (0; {-q_val}); axis of symmetry is x = 0",
        f"Turning point is ({-q_val}; 0); axis of symmetry is y = 0",
        f"Turning point is ({q_val}; 0); axis of symmetry is x = {q_val}",
    ]
    sol = (
        f"Step 1: Reflection across $y = x$ swaps all coordinates $(x; y) \\leftrightarrow (y; x)$.\n"
        f"Step 2: Turning point $(0;\\ {q_val})$ becomes $({q_val};\\ 0)$.\n"
        f"Step 3: Vertical line of symmetry $x = 0$ becomes the horizontal line $y = 0$ (the x-axis)."
    )
    return _mcq_q(
        rng, f"g12_fn_11_{rng.randint(100000, 999999)}", "11_quadratic_turning_point_and_axis_of_symmetry_inverse",
        "Turning Point and Symmetry Reflection for Parabola Inverse", prompt, correct, distractors, sol,
        {"tier_1": "Reflecting across the line y = x swaps (x, y) coordinates and changes vertical lines into horizontal lines.",
         "tier_2": f"(0, {q_val}) reflects to ({q_val}, 0), and x = 0 reflects to y = 0.",
         "tier_3": correct},
        ["failed_to_swap_turning_point_coordinates"]
    )


def arch_12_exponential_inverse_as_logarithm_equation(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 5, 10])
    prompt = (
        f"Given the exponential function $f(x) = {b}^x$:\n\n"
        f"1. Determine the algebraic equation of the inverse function $f^{{-1}}(x)$.\n"
        f"2. Write down the $y$-intercept of $f(x)$ and the $x$-intercept of $f^{{-1}}(x)$."
    )
    correct = f"f^-1(x) = log_{{{b}}}(x); f has y-intercept (0; 1); f^-1 has x-intercept (1; 0)"
    distractors = [
        f"f^-1(x) = {b}^{{-x}}; f has y-intercept (0; 1); f^-1 has x-intercept (-1; 0)",
        f"f^-1(x) = log_{{10}}(x); f has y-intercept (1; 0); f^-1 has x-intercept (0; 1)",
        f"f^-1(x) = x / {b}; f has y-intercept (0; 1); f^-1 has x-intercept (1; 0)",
    ]
    sol = (
        f"Step 1: Write $y = {b}^x$.\n"
        f"Step 2: Swap $x$ and $y$:\n"
        f"$$x = {b}^y$$\n"
        f"Step 3: Convert from exponential form to logarithmic form:\n"
        f"$$y = \\log_{{{b}}}(x)$$\n"
        f"Step 4: Intercepts:\n"
        f"$f(0) = {b}^0 = 1 \\implies (0;\\ 1)$.\n"
        f"Reflecting $(0;\\ 1)$ in $y = x$ gives $x$-intercept $(1;\\ 0)$ for $f^{{-1}}$."
    )
    return _mcq_q(
        rng, f"g12_fn_12_{rng.randint(100000, 999999)}", "12_exponential_inverse_as_logarithm_equation",
        "Logarithm as Inverse of Exponential Function", prompt, correct, distractors, sol,
        {"tier_1": "Recall the definition of a logarithm: x = b^y is equivalent to y = log_b(x).",
         "tier_2": f"Here base is {b}, so inverse is y = log_{{{b}}}(x).",
         "tier_3": correct},
        ["confused_inverse_with_reciprocal_exponential"]
    )


def arch_13_exponential_inverse_fractional_base(rng: random.Random) -> Dict[str, Any]:
    den = rng.choice([2, 3, 4, 5])
    prompt = (
        f"Consider the decreasing exponential function $f(x) = \\left(\\frac{{1}}{{{den}}}\\right)^x$.\n\n"
        f"Determine the equation of the inverse function $f^{{-1}}(x)$, and state whether $f^{{-1}}(x)$ is increasing or decreasing."
    )
    correct = f"f^-1(x) = log_{{1/{den}}}(x) = -log_{{{den}}}(x); decreasing function"
    distractors = [
        f"f^-1(x) = log_{{{den}}}(x); increasing function",
        f"f^-1(x) = {den}^x; increasing function",
        f"f^-1(x) = -{den}^x; decreasing function",
    ]
    sol = (
        f"Step 1: Swap $x$ and $y$:\n"
        f"$$x = \\left(\\frac{{1}}{{{den}}}\\right)^y$$\n"
        f"Step 2: By definition of logarithm:\n"
        f"$$y = \\log_{{1/{den}}}(x) = \\frac{{\\log x}}{{\\log(1/{den})}} = \\frac{{\\log x}}{{-\\log {den}}} = -\\log_{{{den}}}(x)$$\n"
        f"Step 3: Because the base is between $0$ and $1$ ($0 < \\frac{{1}}{{{den}}} < 1$), both $f$ and $f^{{-1}}$ are strictly decreasing functions."
    )
    return _mcq_q(
        rng, f"g12_fn_13_{rng.randint(100000, 999999)}", "13_exponential_inverse_fractional_base",
        "Logarithmic Inverse with Fractional Base", prompt, correct, distractors, sol,
        {"tier_1": "For base 0 < b < 1, the logarithm is log_{1/den}(x) = -log_{den}(x).",
         "tier_2": "Functions with bases 0 < b < 1 are decreasing across their domains.",
         "tier_3": correct},
        ["assumed_log_with_fractional_base_is_increasing"]
    )


def arch_14_exponential_and_log_domain_and_range(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4])
    prompt = (
        f"Compare the domain and range of $f(x) = {b}^x$ with the domain and range of its inverse $f^{{-1}}(x) = \\log_{{{b}}}(x)$."
    )
    correct = f"f: Domain x in R, Range y > 0; f^-1: Domain x > 0, Range y in R"
    distractors = [
        f"f: Domain x > 0, Range y in R; f^-1: Domain x in R, Range y > 0",
        f"f: Domain x in R, Range y >= 0; f^-1: Domain x >= 0, Range y in R",
        f"Both f and f^-1 have Domain x in R and Range y in R",
    ]
    sol = (
        f"Step 1: For exponential $f(x) = {b}^x$:\n"
        f"Any real exponent is valid $\\implies$ Domain: $x \\in \\mathbb{{R}}$.\n"
        f"A positive base raised to any power is strictly positive $\\implies$ Range: $y > 0$.\n"
        f"Step 2: For inverse $f^{{-1}}(x) = \\log_{{{b}}}(x)$, domain and range interchange:\n"
        f"Domain of $f^{{-1}}$: $x > 0$.\n"
        f"Range of $f^{{-1}}$: $y \\in \\mathbb{{R}}$."
    )
    return _mcq_q(
        rng, f"g12_fn_14_{rng.randint(100000, 999999)}", "14_exponential_and_log_domain_and_range",
        "Domain and Range of Exponential vs Logarithmic Functions", prompt, correct, distractors, sol,
        {"tier_1": "Recall that the domain of f becomes the range of f^-1, and the range of f becomes the domain of f^-1.",
         "tier_2": f"{b}^x is never zero or negative, so range is y > 0. Therefore log base {b} requires x > 0.",
         "tier_3": correct},
        ["included_zero_in_domain_of_logarithm"]
    )


def arch_15_exponential_and_log_asymptote_interchange(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 5])
    prompt = (
        f"State the equations of the asymptotes for $f(x) = {b}^x$ and $f^{{-1}}(x) = \\log_{{{b}}}(x)$, "
        f"and explain how they relate under reflection across the line $y = x$."
    )
    correct = f"f has horizontal asymptote y = 0; f^-1 has vertical asymptote x = 0 (interchanged by reflection in y = x)"
    distractors = [
        f"f has vertical asymptote x = 0; f^-1 has horizontal asymptote y = 0",
        f"f has asymptote y = 1; f^-1 has asymptote x = 1",
        f"Neither function has an asymptote",
    ]
    sol = (
        f"Step 1: As $x \\to -\\infty$, ${b}^x \\to 0$, giving horizontal asymptote $y = 0$ (the x-axis).\n"
        f"Step 2: Under reflection in $y = x$, horizontal lines $y = k$ become vertical lines $x = k$.\n"
        f"Thus $y = 0$ reflects into the vertical asymptote $x = 0$ (the y-axis) for $\\log_{{{b}}}(x)$."
    )
    return _mcq_q(
        rng, f"g12_fn_15_{rng.randint(100000, 999999)}", "15_exponential_and_log_asymptote_interchange",
        "Asymptote Interchange Under Reflection", prompt, correct, distractors, sol,
        {"tier_1": "Horizontal lines y = k reflect in y = x to become vertical lines x = k.",
         "tier_2": "The asymptote y = 0 of the exponential function becomes the vertical line x = 0 for the logarithm.",
         "tier_3": correct},
        ["swapped_horizontal_and_vertical_asymptotes"]
    )


def arch_16_exponential_with_vertical_shift_inverse(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3])
    q = rng.choice([-3, -2, 2, 4])
    prompt = (
        f"Given the shifted exponential function $f(x) = {b}^x {'+' if q >= 0 else '-'} {abs(q)}$:\n\n"
        f"1. Determine the equation of the inverse function $f^{{-1}}(x)$.\n"
        f"2. State the equation of the vertical asymptote of $f^{{-1}}(x)$."
    )
    correct = f"f^-1(x) = log_{{{b}}}(x {'-' if q >= 0 else '+'} {abs(q)}); vertical asymptote is x = {q}"
    distractors = [
        f"f^-1(x) = log_{{{b}}}(x {'+' if q >= 0 else '-'} {abs(q)}); vertical asymptote is x = {-q}",
        f"f^-1(x) = log_{{{b}}}(x) {'-' if q >= 0 else '+'} {abs(q)}; vertical asymptote is x = 0",
        f"f^-1(x) = {b}^{{x - {q}}}; vertical asymptote is y = {q}",
    ]
    sol = (
        f"Step 1: Write $y = {b}^x {'+' if q >= 0 else '-'} {abs(q)}$.\n"
        f"Step 2: Swap $x$ and $y$:\n"
        f"$$x = {b}^y {'+' if q >= 0 else '-'} {abs(q)}$$\n"
        f"$${b}^y = x {'-' if q >= 0 else '+'} {abs(q)}$$\n"
        f"Step 3: Convert to logarithmic form:\n"
        f"$$y = \\log_{{{b}}}(x {'-' if q >= 0 else '+'} {abs(q)})$$\n"
        f"Step 4: Horizontal asymptote of $f$ is $y = {q}$, which reflects into vertical asymptote $x = {q}$ for $f^{{-1}}$."
    )
    return _mcq_q(
        rng, f"g12_fn_16_{rng.randint(100000, 999999)}", "16_exponential_with_vertical_shift_inverse",
        "Inverse of Shifted Exponential Function", prompt, correct, distractors, sol,
        {"tier_1": f"Isolate the exponential term: {b}^y = x - ({q}).",
         "tier_2": f"Take log base {b}: y = log_{{{b}}}(x - ({q})). The argument must be > 0, so asymptote is x = {q}.",
         "tier_3": correct},
        ["forgot_to_shift_argument_inside_logarithm"]
    )


def arch_17_log_function_find_base_from_point(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4, 5])
    y_val = rng.choice([2, 3])
    x_val = b ** y_val
    prompt = (
        f"The logarithmic function $f(x) = \\log_b(x)$ passes through the point $P({x_val};\\ {y_val})$.\n\n"
        f"Calculate the value of the base $b$."
    )
    ans = f"b = {b}"
    sol = (
        f"Step 1: Substitute the coordinates $x = {x_val}$ and $y = {y_val}$ into $y = \\log_b(x)$:\n"
        f"$${y_val} = \\log_b({x_val})$$\n"
        f"Step 2: Convert to exponential form:\n"
        f"$$b^{{{y_val}}} = {x_val}$$\n"
        f"Step 3: Solve for $b$:\n"
        f"$$b = \\sqrt[{y_val}]{{{x_val}}} = {b}$$."
    )
    return _calc_q(
        rng, f"g12_fn_17_{rng.randint(100000, 999999)}", "17_log_function_find_base_from_point",
        "Determining Logarithmic Base from a Known Point", prompt, ans, sol,
        {"tier_1": f"Substitute x = {x_val} and y = {y_val} into y = log_b(x).",
         "tier_2": f"Rewrite as b^{{{y_val}}} = {x_val} and take the {y_val}-th root.",
         "tier_3": f"b = {b}."},
        ["confused_base_with_power"]
    )


def arch_18_exponential_function_find_base_from_point(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4, 5])
    x_val = rng.choice([2, 3])
    y_val = b ** x_val
    prompt = (
        f"The exponential function $f(x) = a^x$ passes through the point $Q({x_val};\\ {y_val})$.\n\n"
        f"Calculate the value of the base $a$."
    )
    ans = f"a = {b}"
    sol = (
        f"Step 1: Substitute $x = {x_val}$ and $y = {y_val}$ into $y = a^x$:\n"
        f"$${y_val} = a^{{{x_val}}}$$\n"
        f"Step 2: Solve for $a$:\n"
        f"$$a = \\sqrt[{x_val}]{{{y_val}}} = {b}$$."
    )
    return _calc_q(
        rng, f"g12_fn_18_{rng.randint(100000, 999999)}", "18_exponential_function_find_base_from_point",
        "Determining Exponential Base from a Known Point", prompt, ans, sol,
        {"tier_1": f"Substitute x = {x_val} and y = {y_val} into y = a^x.",
         "tier_2": f"Take the {x_val}-th root of {y_val}.",
         "tier_3": f"a = {b}."},
        ["divided_by_exponent_instead_of_taking_root"]
    )


def arch_19_log_function_evaluate_exact_values(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 5])
    power = rng.choice([-3, -2, 3, 4])
    if power < 0:
        val_str = f"1/{b**abs(power)}"
    else:
        val_str = str(b**power)
    prompt = (
        f"Without using a calculator, evaluate the exact numerical value of:\n"
        f"$$\\log_{{{b}}}\\left({val_str}\\right)$$"
    )
    ans = str(power)
    sol = (
        f"Step 1: Let $y = \\log_{{{b}}}\\left({val_str}\\right)$.\n"
        f"Step 2: Convert to exponential form: ${b}^y = {val_str}$.\n"
        f"Step 3: Express ${val_str}$ as a power of ${b}$:\n"
        f"$${val_str} = {b}^{{{power}}}$$\n"
        f"Step 4: Equating exponents gives $y = {power}$."
    )
    return _calc_q(
        rng, f"g12_fn_19_{rng.randint(100000, 999999)}", "19_log_function_evaluate_exact_values",
        "Evaluating Exact Logarithms without Calculator", prompt, ans, sol,
        {"tier_1": f"Express {val_str} as {b}^k.",
         "tier_2": f"log_b(b^k) = k.",
         "tier_3": f"Value = {power}."},
        ["incorrect_sign_for_fractional_log_argument"]
    )


def arch_20_log_laws_simplification_in_functions(rng: random.Random) -> Dict[str, Any]:
    # log_b(A) + log_b(B) - log_b(C) = log_b(A*B/C)
    b = rng.choice([2, 3, 10])
    p1 = rng.choice([2, 3])
    p2 = rng.choice([1, 2])
    total_pow = p1 + p2
    arg1 = b**p1
    arg2 = b**p2
    prompt = (
        f"Simplify the following logarithmic expression using logarithm laws:\n"
        f"$$\\log_{{{b}}}({arg1}) + \\log_{{{b}}}({arg2})$$"
    )
    ans = str(total_pow)
    sol = (
        f"Step 1: Apply the product rule of logarithms: $\\log_b(M) + \\log_b(N) = \\log_b(M \\times N)$:\n"
        f"$$\\log_{{{b}}}({arg1} \\times {arg2}) = \\log_{{{b}}}({arg1 * arg2})$$\n"
        f"Step 2: Since ${arg1 * arg2} = {b}^{{{total_pow}}}$, we evaluate:\n"
        f"$$\\log_{{{b}}}({b}^{{{total_pow}}}) = {total_pow}$."
    )
    return _calc_q(
        rng, f"g12_fn_20_{rng.randint(100000, 999999)}", "20_log_laws_simplification_in_functions",
        "Simplifying Expressions with Logarithm Product Law", prompt, ans, sol,
        {"tier_1": "Apply the product law: log(A) + log(B) = log(A * B).",
         "tier_2": f"Multiply {arg1} * {arg2} = {arg1 * arg2}, then express as a power of {b}.",
         "tier_3": f"Value = {total_pow}."},
        ["added_arguments_instead_of_multiplying_log_arguments"]
    )


def arch_21_change_of_base_rule_logarithms(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 5])
    k = rng.choice([7, 11, 13])
    prompt = (
        f"Use the change of base formula to express $\\log_{{{b}}}({k})$ in terms of common base $10$ logarithms ($\\log$)."
    )
    correct = f"\\log({k}) / \\log({b})"
    distractors = [
        f"\\log({b}) / \\log({k})",
        f"\\log({k} - {b})",
        f"\\log({k}) \\times \\log({b})",
    ]
    sol = (
        f"Step 1: State the change of base formula:\n"
        f"$$\\log_b(a) = \\frac{{\\log_c(a)}}{{\\log_c(b)}}$$\n"
        f"Step 2: For base $c = 10$:\n"
        f"$$\\log_{{{b}}}({k}) = \\frac{{\\log({k})}}{{\\log({b})}} = {correct}$$."
    )
    return _mcq_q(
        rng, f"g12_fn_21_{rng.randint(100000, 999999)}", "21_change_of_base_rule_logarithms",
        "Applying the Change of Base Rule", prompt, correct, distractors, sol,
        {"tier_1": "Recall: log_b(a) = log(a) / log(b).",
         "tier_2": f"Numerator is log({k}) and denominator is log({b}).",
         "tier_3": correct},
        ["inverted_numerator_and_denominator_in_change_of_base"]
    )


def arch_22_solving_exponential_equations_using_logs(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 5])
    target = rng.choice([15, 20, 50, 75])
    prompt = (
        f"Solve for $x$ correct to two decimal places:\n"
        f"$${b}^x = {target}$$"
    )
    ans_val = round(math.log(target) / math.log(b), 2)
    ans = f"x = {ans_val:.2f}".replace(".", "{,}")
    sol = (
        f"Step 1: Take logarithms of both sides:\n"
        f"$$\\log({b}^x) = \\log({target})$$\n"
        f"Step 2: Apply the power rule: $x \\log({b}) = \\log({target})$.\n"
        f"Step 3: Solve for $x$:\n"
        f"$$x = \\frac{{\\log({target})}}{{\\log({b})}} \\approx {ans_val:.2f}$$."
    )
    return _calc_q(
        rng, f"g12_fn_22_{rng.randint(100000, 999999)}", "22_solving_exponential_equations_using_logs",
        "Solving Exponential Equations via Logarithms", prompt, ans, sol,
        {"tier_1": "Take log on both sides and bring the exponent x down to the front.",
         "tier_2": f"x = log({target}) / log({b}).",
         "tier_3": f"x = {ans_val:.2f}."},
        ["divided_target_by_base_instead_of_using_logs"]
    )


def arch_23_solving_logarithmic_equations_basic(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4])
    p = rng.choice([2, 3])
    rhs = b ** p
    c_offset = rng.choice([1, 3, 5])
    # log_b(2x - c_offset) = p => 2x - c_offset = b^p => 2x = b^p + c_offset
    # make sure 2x is even
    if (rhs + c_offset) % 2 != 0:
        c_offset += 1
    x_val = (rhs + c_offset) // 2
    prompt = (
        f"Solve for $x$ in the equation:\n"
        f"$$\\log_{{{b}}}(2x - {c_offset}) = {p}$$"
    )
    ans = f"x = {x_val}"
    sol = (
        f"Step 1: Convert to exponential form:\n"
        f"$$2x - {c_offset} = {b}^{{{p}}}$$\n"
        f"Step 2: Compute RHS: ${b}^{{{p}}} = {rhs}$.\n"
        f"Step 3: Solve the linear equation:\n"
        f"$$2x = {rhs} + {c_offset} = {rhs + c_offset} \\implies x = {x_val}$$.\n"
        f"Step 4: Check validity: $2({x_val}) - {c_offset} = {rhs} > 0$ (valid)."
    )
    return _calc_q(
        rng, f"g12_fn_23_{rng.randint(100000, 999999)}", "23_solving_logarithmic_equations_basic",
        "Solving Elementary Logarithmic Equations", prompt, ans, sol,
        {"tier_1": f"Rewrite in exponential form: 2x - {c_offset} = {b}^{{{p}}}.",
         "tier_2": f"Add {c_offset} to {rhs} and divide by 2.",
         "tier_3": f"x = {x_val}."},
        ["forgot_to_convert_to_exponential_form"]
    )


def arch_24_inverse_functions_reflection_svg(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3])
    svg_body = (
        f'<line x1="50" y1="200" x2="350" y2="200" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<line x1="200" y1="50" x2="200" y2="230" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<line x1="60" y1="220" x2="340" y2="60" stroke="#e2e8f0" stroke-width="1.5" stroke-dasharray="4,4"/>'
        f'<path d="M 60,195 Q 160,190 200,160 T 260,60" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<path d="M 195,220 Q 190,160 160,200 T 60,260" fill="none" stroke="#16a34a" stroke-width="2.5"/>'
        f'<circle cx="200" cy="160" r="4" fill="#2563eb"/><text x="175" y="155" font-size="10" fill="#1e40af">(0; 1)</text>'
        f'<circle cx="160" cy="200" r="4" fill="#16a34a"/><text x="165" y="215" font-size="10" fill="#15803d">(1; 0)</text>'
        f'<text x="270" y="55" font-size="11" font-weight="bold" fill="#2563eb">y = {b}^x</text>'
        f'<text x="235" y="225" font-size="11" font-weight="bold" fill="#16a34a">y = log_{b}(x)</text>'
        f'<text x="320" y="75" font-size="10" fill="#64748b">y = x</text>'
    )
    prompt = (
        f"The visual display presents the graphs of $f(x) = {b}^x$, the line of symmetry $y = x$, "
        f"and the inverse $f^{{-1}}(x) = \\log_{{{b}}}(x)$.\n\n"
        f"1. Explain how the coordinate $(0;\\ 1)$ on $f(x)$ transforms onto $f^{{-1}}(x)$.\n"
        f"2. State the geometric relationship between any point $(a;\\ b)$ on $f$ and $(b;\\ a)$ on $f^{{-1}}$."
    )
    correct = "(0; 1) reflects across y = x to become (1; 0); every point (a; b) has its coordinates interchanged to (b; a) via reflection across y = x"
    distractors = [
        "(0; 1) reflects across the y-axis to become (0; -1); coordinates negate",
        "(0; 1) translates horizontally by 1 unit to (1; 1)",
        "(0; 1) rotates 90 degrees to become (-1; 0)",
    ]
    sol = (
        f"Step 1: Point transformation:\n"
        f"Under reflection in the line of symmetry $y = x$, coordinates swap positions: $(x;\\ y) \\to (y;\\ x)$.\n"
        f"Thus the $y$-intercept $(0;\\ 1)$ on $f$ reflects to the $x$-intercept $(1;\\ 0)$ on $f^{{-1}}$.\n"
        f"Step 2: Any point $(a;\\ b)$ on $f$ corresponds to $(b;\\ a)$ on $f^{{-1}}$."
    )
    return _mcq_q(
        rng, f"g12_fn_24_{rng.randint(100000, 999999)}", "24_inverse_functions_reflection_svg",
        "Visual Symmetrical Reflection of Exponential and Logarithm", prompt, correct, distractors, sol,
        {"tier_1": "Look at the axis intercepts and how the line y = x acts as a mirror.",
         "tier_2": "Point (0, 1) reflects to (1, 0) across y = x.",
         "tier_3": correct},
        ["confused_reflection_in_y_equals_x_with_axis_reflection"],
        diagram_spec=_svg_spec(svg_body, 580, 240)
    )


def arch_25_parabola_and_inverse_branches_svg(rng: random.Random) -> Dict[str, Any]:
    coeff_a = rng.choice([1, 2, 3])
    parab_str = f"y = {coeff_a}x^2" if coeff_a != 1 else "y = x^2"
    inv_str = f"y = +\\sqrt{{x/{coeff_a}}}" if coeff_a != 1 else "y = +\\sqrt{x}"
    inv_neg = f"y = -\\sqrt{{x/{coeff_a}}}" if coeff_a != 1 else "y = -\\sqrt{x}"
    svg_body = (
        f'<line x1="40" y1="180" x2="360" y2="180" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<line x1="200" y1="40" x2="200" y2="230" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<line x1="60" y1="210" x2="330" y2="50" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4,4"/>'
        f'<path d="M 120,60 Q 200,240 280,60" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<path d="M 320,100 Q 140,180 320,260" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="3,3"/>'
        f'<path d="M 200,180 Q 260,180 320,100" fill="none" stroke="#16a34a" stroke-width="2.5"/>'
        f'<text x="290" y="55" font-size="11" font-weight="bold" fill="#2563eb">{parab_str}</text>'
        f'<text x="325" y="95" font-size="11" font-weight="bold" fill="#16a34a">{inv_str} (x >= 0)</text>'
        f'<text x="325" y="235" font-size="11" font-weight="bold" fill="#dc2626">{inv_neg}</text>'
        f'<text x="310" y="45" font-size="10" fill="#64748b">y = x</text>'
    )
    prompt = (
        f"The visual plot illustrates the parabola ${parab_str}$, the line $y = x$, and the two branches of its inverse "
        f"${inv_str}$ and ${inv_neg}$.\n\n"
        f"Why must the domain of $f(x) = {coeff_a if coeff_a != 1 else ''}x^2$ be restricted to $x \\ge 0$ (or $x \\le 0$) for the inverse to be a function?"
    )
    correct = "Because without domain restriction, the inverse relation has two y-values for each x > 0 and fails the vertical line test"
    distractors = [
        "Because negative numbers have real square roots",
        "Because the parabola has no turning point",
        "Because domain restrictions eliminate the line of symmetry y = x",
    ]
    sol = (
        f"Step 1: Unrestricted parabola $y = x^2$ is many-to-one because $f(-x) = f(x)$.\n"
        f"Step 2: Its full inverse $x = y^2$ is one-to-many, containing both upper branch $y = +\\sqrt{{x}}$ and lower branch $y = -\\sqrt{{x}}$.\n"
        f"Step 3: Restricting domain to $x \\ge 0$ retains only the upper branch $y = \\sqrt{{x}}$, making the inverse one-to-one and therefore a valid function."
    )
    return _mcq_q(
        rng, f"g12_fn_25_{rng.randint(100000, 999999)}", "25_parabola_and_inverse_branches_svg",
        "Visual Demonstration of Parabola Domain Restriction", prompt, correct, distractors, sol,
        {"tier_1": "Notice how the full sideways parabola has two branches that fail the vertical line test.",
         "tier_2": "Restricting x >= 0 keeps only the green upper branch y = sqrt(x).",
         "tier_3": correct},
        ["failed_to_recognise_vertical_line_test_failure_on_full_inverse"],
        diagram_spec=_svg_spec(svg_body, 580, 250)
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_function_definition_vertical_line_test": arch_01_function_definition_vertical_line_test,
    "02_horizontal_line_test_invertibility": arch_02_horizontal_line_test_invertibility,
    "03_linear_function_inverse_equation": arch_03_linear_function_inverse_equation,
    "04_linear_function_inverse_coordinates": arch_04_linear_function_inverse_coordinates,
    "05_linear_function_inverse_line_of_symmetry": arch_05_linear_function_inverse_line_of_symmetry,
    "06_quadratic_inverse_equation_full": arch_06_quadratic_inverse_equation_full,
    "07_quadratic_inverse_why_not_function": arch_07_quadratic_inverse_why_not_function,
    "08_quadratic_domain_restriction_positive": arch_08_quadratic_domain_restriction_positive,
    "09_quadratic_domain_restriction_negative": arch_09_quadratic_domain_restriction_negative,
    "10_quadratic_with_vertical_shift_inverse": arch_10_quadratic_with_vertical_shift_inverse,
    "11_quadratic_turning_point_and_axis_of_symmetry_inverse": arch_11_quadratic_turning_point_and_axis_of_symmetry_inverse,
    "12_exponential_inverse_as_logarithm_equation": arch_12_exponential_inverse_as_logarithm_equation,
    "13_exponential_inverse_fractional_base": arch_13_exponential_inverse_fractional_base,
    "14_exponential_and_log_domain_and_range": arch_14_exponential_and_log_domain_and_range,
    "15_exponential_and_log_asymptote_interchange": arch_15_exponential_and_log_asymptote_interchange,
    "16_exponential_with_vertical_shift_inverse": arch_16_exponential_with_vertical_shift_inverse,
    "17_log_function_find_base_from_point": arch_17_log_function_find_base_from_point,
    "18_exponential_function_find_base_from_point": arch_18_exponential_function_find_base_from_point,
    "19_log_function_evaluate_exact_values": arch_19_log_function_evaluate_exact_values,
    "20_log_laws_simplification_in_functions": arch_20_log_laws_simplification_in_functions,
    "21_change_of_base_rule_logarithms": arch_21_change_of_base_rule_logarithms,
    "22_solving_exponential_equations_using_logs": arch_22_solving_exponential_equations_using_logs,
    "23_solving_logarithmic_equations_basic": arch_23_solving_logarithmic_equations_basic,
    "24_inverse_functions_reflection_svg": arch_24_inverse_functions_reflection_svg,
    "25_parabola_and_inverse_branches_svg": arch_25_parabola_and_inverse_branches_svg,
}
