"""Technical Mathematics Grade 12 - Complex Numbers Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/TechnicalMathematics_Gr12/Term 1/01. Complex numbers.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional
import sympy as sp


def _svg_spec(svg_body: str, width: int = 400, height: int = 300) -> Dict[str, Any]:
    return {
        "kind": "inline_svg",
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="100%" height="{height}" style="background:#ffffff;border-radius:8px;border:1px solid #cbd5e1;">'
            f'{svg_body}</svg>'
        ),
        "diagram_role": "context",
    }


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
    curriculum_ref: str = "Term 1 > Complex Numbers",
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
    curriculum_ref: str = "Term 1 > Complex Numbers",
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

def arch_01_powers_of_i_simplification(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(5, 75)
    rem = k % 4
    mapping = {0: "1", 1: "i", 2: "-1", 3: "-i"}
    correct = mapping[rem]
    distractors = [v for k_val, v in mapping.items() if v != correct]

    prompt = (
        f"Simplify the following expression using the cyclic powers of the imaginary unit $i$:\n\n"
        f"$$i^{{{k}}}$$"
    )
    sol = (
        f"Step 1: The powers of $i$ repeat every cycle of 4:\n"
        f"$$i^1 = i, \\quad i^2 = -1, \\quad i^3 = -i, \\quad i^4 = 1$$\n"
        f"Step 2: Divide the exponent by 4:\n"
        f"$${k} = 4 \\times {k // 4} + {rem}$$\n"
        f"Step 3: Evaluate:\n"
        f"$$i^{{{k}}} = (i^4)^{{{k // 4}}} \\times i^{{{rem}}} = (1)^{{{k // 4}}} \\times i^{{{rem}}} = {correct}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_01_{rng.randint(100000, 999999)}", "01_powers_of_i_simplification",
        "Simplifying Higher Powers of Imaginary Unit", prompt, correct, distractors, sol,
        {"tier_1": "Divide the exponent by 4 to find the remainder.",
         "tier_2": f"{k} divided by 4 leaves remainder {rem}. Recall i^0=1, i^1=i, i^2=-1, i^3=-i.",
         "tier_3": correct},
        ["forgot_powers_of_i_cycle_modulo_4"]
    )


def arch_02_powers_of_i_linear_combination(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.choice([-3, 2, 4])
    c2 = rng.choice([-4, -2, 3, 5])
    p1 = rng.choice([5, 9, 13, 17])   # rem 1 -> i
    p2 = rng.choice([6, 10, 14, 18])  # rem 2 -> -1
    # Expression = c1*i^p1 + c2*i^p2 = c1*i + c2*(-1) = -c2 + c1*i
    real_part = -c2
    imag_part = c1
    correct = f"{real_part} {'+' if imag_part >= 0 else '-'} {abs(imag_part)}i"
    distractors = [
        f"{-real_part} {'+' if imag_part >= 0 else '-'} {abs(imag_part)}i",
        f"{real_part} {'-' if imag_part >= 0 else '+'} {abs(imag_part)}i",
        f"{c1 + c2}i",
    ]
    prompt = (
        f"Simplify the following expression and write your answer in standard rectangular form ($a + bi$):\n\n"
        f"$${c1}i^{{{p1}}} {'+' if c2 >= 0 else '-'} {abs(c2)}i^{{{p2}}}$$"
    )
    sol = (
        f"Step 1: Simplify each power of $i$ individually:\n"
        f"$$i^{{{p1}}} = i^1 = i$$\n"
        f"$$i^{{{p2}}} = i^2 = -1$$\n"
        f"Step 2: Substitute back into the expression:\n"
        f"$${c1}(i) {'+' if c2 >= 0 else '-'} {abs(c2)}(-1) = {c1}i {'-' if c2 >= 0 else '+'} {abs(c2)} = {correct}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_02_{rng.randint(100000, 999999)}", "02_powers_of_i_linear_combination",
        "Linear Combination of Cyclic Powers of i", prompt, correct, distractors, sol,
        {"tier_1": f"Reduce i^{{{p1}}} and i^{{{p2}}} by dividing their exponents by 4.",
         "tier_2": f"i^{{{p1}}} = i and i^{{{p2}}} = -1. Substitute and write as real + imaginary.",
         "tier_3": correct},
        ["confused_real_and_imaginary_components_in_powers_of_i"]
    )


def arch_03_even_roots_of_negative_real_numbers(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
    sqrt_n = int(math.isqrt(n))
    correct = f"{sqrt_n}i"
    distractors = [
        f"-{sqrt_n}",
        f"{sqrt_n}",
        f"-{sqrt_n}i",
    ]
    prompt = (
        f"Express $\\sqrt{{-{n}}}$ as an imaginary number in terms of $i$."
    )
    sol = (
        f"Step 1: Use the property of radicals $\\sqrt{{-a}} = \\sqrt{{a}} \\cdot \\sqrt{{-1}}$:\n"
        f"$$\\sqrt{{-{n}}} = \\sqrt{{{n}}} \\times \\sqrt{{-1}}$$\n"
        f"Step 2: Substitute $\\sqrt{{-1}} = i$ and evaluate $\\sqrt{{{n}}} = {sqrt_n}$:\n"
        f"$$= {sqrt_n}i$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_03_{rng.randint(100000, 999999)}", "03_even_roots_of_negative_real_numbers",
        "Even Roots of Negative Real Numbers", prompt, correct, distractors, sol,
        {"tier_1": "Rewrite sqrt(-n) as sqrt(n) * sqrt(-1).",
         "tier_2": f"sqrt({n}) = {sqrt_n} and sqrt(-1) = i.",
         "tier_3": correct},
        ["omitted_imaginary_unit_when_taking_square_root_of_negative"]
    )


def arch_04_addition_and_subtraction_rectangular(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(-8, 8)
    b = rng.choice([-7, -5, -3, 3, 5, 7])
    c = rng.randint(-8, 8)
    d = rng.choice([-6, -4, -2, 2, 4, 6])
    is_sub = rng.choice([True, False])

    if is_sub:
        r_ans = a - c
        i_ans = b - d
        op_sym = "-"
    else:
        r_ans = a + c
        i_ans = b + d
        op_sym = "+"

    correct = f"{r_ans} {'+' if i_ans >= 0 else '-'} {abs(i_ans)}i"
    distractors = [
        f"{r_ans} {'-' if i_ans >= 0 else '+'} {abs(i_ans)}i",
        f"{-r_ans} {'+' if i_ans >= 0 else '-'} {abs(i_ans)}i",
        f"{r_ans + i_ans}i",
    ]
    prompt = (
        f"Calculate and express in rectangular form ($a + bi$):\n\n"
        f"$$({a} {'+' if b >= 0 else '-'} {abs(b)}i) {op_sym} ({c} {'+' if d >= 0 else '-'} {abs(d)}i)$$"
    )
    sol = (
        f"Step 1: Group real and imaginary parts:\n"
        f"$$\\text{{Real part: }} ({a}) {op_sym} ({c}) = {r_ans}$$\n"
        f"$$\\text{{Imaginary part: }} ({b}i) {op_sym} ({d}i) = ({b} {op_sym} ({d}))i = {i_ans}i$$\n"
        f"Step 2: Combine in standard form:\n"
        f"$$= {correct}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_04_{rng.randint(100000, 999999)}", "04_addition_and_subtraction_rectangular",
        "Addition and Subtraction of Complex Numbers in Rectangular Form", prompt, correct, distractors, sol,
        {"tier_1": "Add/subtract real parts together, and imaginary parts together.",
         "tier_2": f"Real: {a} {op_sym} ({c}). Imaginary: {b} {op_sym} ({d}).",
         "tier_3": correct},
        ["mixed_real_and_imaginary_terms_in_addition"]
    )


def arch_05_scalar_multiplication_rectangular(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    a = rng.choice([-6, -4, 3, 5, 7])
    b = rng.choice([-7, -3, 2, 6])
    ra = k * a
    ib = k * b
    correct = f"{ra} {'+' if ib >= 0 else '-'} {abs(ib)}i"
    distractors = [
        f"{ra} {'-' if ib >= 0 else '+'} {abs(ib)}i",
        f"{a} {'+' if ib >= 0 else '-'} {abs(ib)}i",
        f"{ra} {'+' if b >= 0 else '-'} {abs(b)}i",
    ]
    prompt = (
        f"Simplify the scalar product:\n\n"
        f"$${k}({a} {'+' if b >= 0 else '-'} {abs(b)}i)$$"
    )
    sol = (
        f"Step 1: Distribute the scalar factor ${k}$ across both the real and imaginary components:\n"
        f"$$= ({k} \\times {a}) + ({k} \\times {b}i)$$\n"
        f"Step 2: Simplify:\n"
        f"$$= {ra} {'+' if ib >= 0 else '-'} {abs(ib)}i$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_05_{rng.randint(100000, 999999)}", "05_scalar_multiplication_rectangular",
        "Scalar Multiplication of Complex Numbers", prompt, correct, distractors, sol,
        {"tier_1": f"Distribute {k} to both {a} and {b}i.",
         "tier_2": f"{k} * {a} = {ra}, and {k} * {b}i = {ib}i.",
         "tier_3": correct},
        ["forgot_to_multiply_imaginary_part_by_scalar"]
    )


def arch_06_multiplication_monomial_times_binomial(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([-4, -3, -2, 2, 3, 4])
    a = rng.choice([-5, -2, 3, 6])
    b = rng.choice([-6, -4, 2, 5])
    # k*i * (a + b*i) = k*a*i + k*b*i^2 = -k*b + k*a*i
    real_part = -k * b
    imag_part = k * a
    correct = f"{real_part} {'+' if imag_part >= 0 else '-'} {abs(imag_part)}i"
    distractors = [
        f"{-real_part} {'+' if imag_part >= 0 else '-'} {abs(imag_part)}i",
        f"{real_part} {'-' if imag_part >= 0 else '+'} {abs(imag_part)}i",
        f"{imag_part} {'+' if real_part >= 0 else '-'} {abs(real_part)}i",
    ]
    prompt = (
        f"Multiply and simplify into standard rectangular form $a + bi$:\n\n"
        f"$${k}i({a} {'+' if b >= 0 else '-'} {abs(b)}i)$$"
    )
    sol = (
        f"Step 1: Distribute ${k}i$ into the bracket:\n"
        f"$$= ({k}i)({a}) + ({k}i)({b}i) = {k*a}i + {k*b}i^2$$\n"
        f"Step 2: Replace $i^2$ with $-1$:\n"
        f"$$= {k*a}i + {k*b}(-1) = {-k*b} {'+' if k*a >= 0 else '-'} {abs(k*a)}i = {correct}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_06_{rng.randint(100000, 999999)}", "06_multiplication_monomial_times_binomial",
        "Monomial Imaginary Term Multiplied by Binomial Complex Number", prompt, correct, distractors, sol,
        {"tier_1": f"Distribute {k}i to both terms, remembering that i * i = i^2 = -1.",
         "tier_2": f"The term with i^2 becomes {k*b} * (-1) = {-k*b}.",
         "tier_3": correct},
        ["forgot_that_i_squared_equals_negative_one"]
    )


def arch_07_multiplication_binomial_times_binomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-4, -2, 2, 3, 5])
    b = rng.choice([-5, -3, 1, 4])
    c = rng.choice([-3, 1, 2, 4])
    d = rng.choice([-4, -2, 3, 5])
    # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
    r_val = a * c - b * d
    i_val = a * d + b * c
    correct = f"{r_val} {'+' if i_val >= 0 else '-'} {abs(i_val)}i"
    distractors = [
        f"{a*c + b*d} {'+' if i_val >= 0 else '-'} {abs(i_val)}i",
        f"{r_val} {'-' if i_val >= 0 else '+'} {abs(i_val)}i",
        f"{a*c} {'+' if b*d >= 0 else '-'} {abs(b*d)}i",
    ]
    prompt = (
        f"Expand and simplify the product of two complex numbers:\n\n"
        f"$$({a} {'+' if b >= 0 else '-'} {abs(b)}i)({c} {'+' if d >= 0 else '-'} {abs(d)}i)$$"
    )
    sol = (
        f"Step 1: Use the FOIL method:\n"
        f"$$\\text{{First: }} ({a})({c}) = {a*c}$$\n"
        f"$$\\text{{Outer: }} ({a})({d}i) = {a*d}i$$\n"
        f"$$\\text{{Inner: }} ({b}i)({c}) = {b*c}i$$\n"
        f"$$\\text{{Last: }} ({b}i)({d}i) = {b*d}i^2 = {b*d}(-1) = {-b*d}$$\n"
        f"Step 2: Group real and imaginary parts:\n"
        f"$$\\text{{Real: }} {a*c} + ({-b*d}) = {r_val}$$\n"
        f"$$\\text{{Imaginary: }} {a*d}i + {b*c}i = {i_val}i$$\n"
        f"Result: ${correct}$."
    )
    return _mcq_q(
        rng, f"tech_cplx_07_{rng.randint(100000, 999999)}", "07_multiplication_binomial_times_binomial",
        "Multiplication of Two Complex Numbers via FOIL", prompt, correct, distractors, sol,
        {"tier_1": "Multiply using FOIL, then replace i^2 with -1.",
         "tier_2": f"Real part = {a}*{c} - ({b}*{d}) = {r_val}. Imaginary part = {a}*{d} + ({b}*{c}) = {i_val}.",
         "tier_3": correct},
        ["failed_to_change_sign_when_evaluating_i_squared"]
    )


def arch_08_squaring_complex_binomial(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-5, -3, 2, 4, 6])
    b = rng.choice([-4, -2, 3, 5])
    # (a + bi)^2 = (a^2 - b^2) + 2ab*i
    r_val = a**2 - b**2
    i_val = 2 * a * b
    correct = f"{r_val} {'+' if i_val >= 0 else '-'} {abs(i_val)}i"
    distractors = [
        f"{a**2 + b**2} {'+' if i_val >= 0 else '-'} {abs(i_val)}i",
        f"{r_val} {'-' if i_val >= 0 else '+'} {abs(i_val)}i",
        f"{a**2} {'+' if b**2 >= 0 else '-'} {abs(b**2)}i",
    ]
    prompt = (
        f"Expand and simplify into rectangular form:\n\n"
        f"$$({a} {'+' if b >= 0 else '-'} {abs(b)}i)^2$$"
    )
    sol = (
        f"Step 1: Apply the binomial square expansion $(x + y)^2 = x^2 + 2xy + y^2$:\n"
        f"$$({a})^2 + 2({a})({b}i) + ({b}i)^2$$\n"
        f"Step 2: Simplify each term:\n"
        f"$$= {a**2} + ({2*a*b})i + {b**2}i^2$$\n"
        f"Step 3: Replace $i^2 = -1$:\n"
        f"$$= {a**2} + ({i_val})i - {b**2} = ({a**2 - b**2}) {'+' if i_val >= 0 else '-'} {abs(i_val)}i = {correct}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_08_{rng.randint(100000, 999999)}", "08_squaring_complex_binomial",
        "Squaring a Complex Binomial", prompt, correct, distractors, sol,
        {"tier_1": "Recall: (a + bi)^2 = a^2 + 2abi + b^2*i^2 = (a^2 - b^2) + 2abi.",
         "tier_2": f"Calculate {a}^2 - ({b})^2 = {r_val}, and 2*({a})*({b}) = {i_val}.",
         "tier_3": correct},
        ["forgot_middle_cross_product_term_when_squaring"]
    )


def arch_09_difference_of_squares_identity(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.choice([1, 2, 5])
    # (a + bi)^2 - (a - bi)^2 = 4ab*i
    ans_coeff = 4 * a * b
    correct = f"{ans_coeff}i"
    distractors = [
        f"{ans_coeff}",
        f"-{ans_coeff}i",
        "0",
    ]
    prompt = (
        f"Simplify the following expression completely:\n\n"
        f"$$({a} + {b}i)^2 - ({a} - {b}i)^2$$"
    )
    sol = (
        f"Step 1: Expand $(a + bi)^2$ and $(a - bi)^2$:\n"
        f"$$({a} + {b}i)^2 = ({a**2 - b**2}) + {2*a*b}i$$\n"
        f"$$({a} - {b}i)^2 = ({a**2 - b**2}) - {2*a*b}i$$\n"
        f"Step 2: Subtract the two expansions:\n"
        f"$$[({a**2 - b**2}) + {2*a*b}i] - [({a**2 - b**2}) - {2*a*b}i]$$\n"
        f"$$= {2*a*b}i - (-{2*a*b}i) = {ans_coeff}i$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_09_{rng.randint(100000, 999999)}", "09_difference_of_squares_identity",
        "Difference of Squared Conjugate Binomials", prompt, correct, distractors, sol,
        {"tier_1": "Use the algebraic identity: (x + y)^2 - (x - y)^2 = 4xy.",
         "tier_2": f"Here x = {a} and y = {b}i, so 4 * ({a}) * ({b}i) = {ans_coeff}i.",
         "tier_3": correct},
        ["sign_error_in_difference_of_two_squares"]
    )


def arch_10_complex_conjugate_definition(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-7, -4, 3, 5, 8])
    b = rng.choice([-8, -6, 2, 4, 9])
    # z = a + bi => \bar{z} = a - bi
    # Sometimes present as bi + a
    reversed_order = rng.choice([True, False])
    if reversed_order:
        z_disp = f"{b}i {'+' if a >= 0 else '-'} {abs(a)}"
    else:
        z_disp = f"{a} {'+' if b >= 0 else '-'} {abs(b)}i"

    correct = f"{a} {'-' if b >= 0 else '+'} {abs(b)}i"
    distractors = [
        f"{-a} {'+' if b >= 0 else '-'} {abs(b)}i",
        f"{-a} {'-' if b >= 0 else '+'} {abs(b)}i",
        f"{b} {'+' if a >= 0 else '-'} {abs(a)}i",
    ]
    prompt = (
        f"State the complex conjugate $\\bar{{z}}$ of the complex number $z = {z_disp}$."
    )
    sol = (
        f"Step 1: Write the complex number in standard form $z = a + bi$:\n"
        f"$$\\text{{Real part: }} a = {a}, \\quad \\text{{Imaginary part: }} b = {b}$$\n"
        f"Step 2: The complex conjugate $\\bar{{z}}$ is obtained by changing ONLY the sign of the imaginary part ($a - bi$):\n"
        f"$$\\bar{{z}} = {correct}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_10_{rng.randint(100000, 999999)}", "10_complex_conjugate_definition",
        "Determination of Complex Conjugate", prompt, correct, distractors, sol,
        {"tier_1": "The complex conjugate changes the sign of the imaginary term only.",
         "tier_2": f"Real part {a} stays unchanged. Imaginary term {b}i becomes {-b}i.",
         "tier_3": correct},
        ["changed_sign_of_real_part_in_conjugate"]
    )


def arch_11_product_of_complex_number_and_conjugate(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-6, -5, -4, -3, 3, 4, 5, 6])
    b = rng.choice([-7, -4, -2, 2, 4, 7])
    # z * \bar{z} = a^2 + b^2
    ans_val = a**2 + b**2
    prompt = (
        f"Given $z = {a} {'+' if b >= 0 else '-'} {abs(b)}i$:\n\n"
        f"Calculate the product of $z$ and its complex conjugate $\\bar{{z}}$ (i.e. $z \\cdot \\bar{{z}}$)."
    )
    ans = str(ans_val)
    sol = (
        f"Step 1: Write down the complex conjugate:\n"
        f"$$\\bar{{z}} = {a} {'-' if b >= 0 else '+'} {abs(b)}i$$\n"
        f"Step 2: Multiply $z$ by $\\bar{{z}}$:\n"
        f"$$z \\cdot \\bar{{z}} = ({a} {'+' if b >= 0 else '-'} {abs(b)}i)({a} {'-' if b >= 0 else '+'} {abs(b)}i)$$\n"
        f"$$= ({a})^2 - ({b}i)^2 = {a**2} - ({b**2})(-1) = {a**2} + {b**2} = {ans_val}$$\n"
        f"Note: The product of any complex number and its conjugate is always a non-negative real number equal to $|z|^2$."
    )
    return _calc_q(
        rng, f"tech_cplx_11_{rng.randint(100000, 999999)}", "11_product_of_complex_number_and_conjugate",
        "Product of Complex Number with its Conjugate", prompt, ans, sol,
        {"tier_1": "Recall: z * conj(z) = a^2 + b^2.",
         "tier_2": f"Calculate ({a})^2 + ({b})^2.",
         "tier_3": f"Product is {ans_val}."},
        ["included_imaginary_term_in_product_with_conjugate"]
    )


def arch_12_division_pure_imaginary_denominator(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 4, 6])
    b = rng.choice([3, 6, 9])
    # (a + bi) / i = (a + bi)*(-i) / 1 = -ai - b*i^2 = b - ai
    correct = f"{b} - {a}i"
    distractors = [
        f"-{b} - {a}i",
        f"{b} + {a}i",
        f"{a} - {b}i",
    ]
    prompt = (
        f"Divide and simplify into rectangular form:\n\n"
        f"$$\\frac{{{a} + {b}i}}{{i}}$$"
    )
    sol = (
        f"Step 1: Multiply numerator and denominator by the conjugate of the denominator ($-i$):\n"
        f"$$= \\frac{{{a} + {b}i}}{{i}} \\times \\frac{{-i}}{{-i}} = \\frac{{- {a}i - {b}i^2}}{{-i^2}}$$\n"
        f"Step 2: Substitute $i^2 = -1$:\n"
        f"$$= \\frac{{- {a}i - {b}(-1)}}{{-(-1)}} = \\frac{{{b} - {a}i}}{{1}} = {correct}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_12_{rng.randint(100000, 999999)}", "12_division_pure_imaginary_denominator",
        "Division by a Pure Imaginary Number", prompt, correct, distractors, sol,
        {"tier_1": "Multiply numerator and denominator by -i (or divide each term by i).",
         "tier_2": "a/i = -ai and bi/i = b.",
         "tier_3": correct},
        ["forgot_sign_change_when_multiplying_by_negative_i"]
    )


def arch_13_division_monic_denominator(rng: random.Random) -> Dict[str, Any]:
    # (a + bi) / (1 + i) = (a + bi)(1 - i) / 2 = ((a + b) + (b - a)i) / 2
    # Choose a, b so a+b and b-a are even
    a = rng.choice([1, 3, 5])
    b = rng.choice([1, 3, 5])
    r_num = a + b
    i_num = b - a
    r_val = r_num // 2
    i_val = i_num // 2
    correct = f"{r_val} {'+' if i_val >= 0 else '-'} {abs(i_val)}i" if i_val != 0 else str(r_val)
    distractors = [
        f"{r_val} {'-' if i_val >= 0 else '+'} {abs(i_val)}i" if i_val != 0 else f"{r_val} + i",
        f"{r_num} {'+' if i_num >= 0 else '-'} {abs(i_num)}i",
        f"{a} + {b}i",
    ]
    prompt = (
        f"Perform the division and express in rectangular form ($a + bi$):\n\n"
        f"$$\\frac{{{a} + {b}i}}{{1 + i}}$$"
    )
    sol = (
        f"Step 1: Multiply numerator and denominator by the conjugate $(1 - i)$:\n"
        f"$$\\frac{{({a} + {b}i)(1 - i)}}{{(1 + i)(1 - i)}}$$\n"
        f"Step 2: Expand denominator:\n"
        f"$$(1)^2 + (1)^2 = 1 + 1 = 2$$\n"
        f"Step 3: Expand numerator:\n"
        f"$$({a} + {b}i)(1 - i) = {a} - {a}i + {b}i - {b}i^2 = ({a} + {b}) + ({b} - {a})i = {r_num} {'+' if i_num >= 0 else '-'} {abs(i_num)}i$$\n"
        f"Step 4: Divide each term by 2:\n"
        f"$$= \\frac{{{r_num}}}{{2}} {'+' if i_num >= 0 else '-'} \\frac{{{abs(i_num)}}}{{2}}i = {correct}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_13_{rng.randint(100000, 999999)}", "13_division_monic_denominator",
        "Complex Number Division with Binomial Denominator", prompt, correct, distractors, sol,
        {"tier_1": "Multiply numerator and denominator by conjugate (1 - i).",
         "tier_2": "The denominator becomes 1^2 + 1^2 = 2. Divide each term by 2.",
         "tier_3": correct},
        ["divided_by_denominator_without_multiplying_by_conjugate"]
    )


def arch_14_division_general_complex_numbers(rng: random.Random) -> Dict[str, Any]:
    # (a + bi) / (c + di). Let c = 2, d = 1 => c^2 + d^2 = 5
    # Numerator (a + bi)(2 - i) = (2a + b) + (2b - a)i
    a = rng.choice([1, 2, 3, 4])
    b = rng.choice([-3, -1, 2, 4])
    c, d = 2, 1
    denom = c**2 + d**2  # 5
    num_r = a * c + b * d
    num_i = b * c - a * d
    correct = f"({num_r} {'+' if num_i >= 0 else '-'} {abs(num_i)}i) / 5"
    distractors = [
        f"({num_r} {'-' if num_i >= 0 else '+'} {abs(num_i)}i) / 5",
        f"({a*c} {'+' if b*d >= 0 else '-'} {abs(b*d)}i) / 5",
        f"{num_r} {'+' if num_i >= 0 else '-'} {abs(num_i)}i",
    ]
    prompt = (
        f"Simplify the complex fraction into standard form:\n\n"
        f"$$\\frac{{{a} {'+' if b >= 0 else '-'} {abs(b)}i}}{{2 + i}}$$"
    )
    sol = (
        f"Step 1: Multiply numerator and denominator by the conjugate $(2 - i)$:\n"
        f"$$\\frac{{({a} {'+' if b >= 0 else '-'} {abs(b)}i)(2 - i)}}{{(2 + i)(2 - i)}}$$\n"
        f"Step 2: Simplify denominator:\n"
        f"$$(2)^2 + (1)^2 = 4 + 1 = 5$$\n"
        f"Step 3: Expand numerator:\n"
        f"$$= ({a})(2) + ({a})(-i) + ({b}i)(2) + ({b}i)(-i) = {2*a} - {a}i + {2*b}i - {b}i^2$$\n"
        f"$$= ({2*a + b}) + ({2*b - a})i = {num_r} {'+' if num_i >= 0 else '-'} {abs(num_i)}i$$\n"
        f"Result: ${correct}$."
    )
    return _mcq_q(
        rng, f"tech_cplx_14_{rng.randint(100000, 999999)}", "14_division_general_complex_numbers",
        "Division of General Complex Numbers", prompt, correct, distractors, sol,
        {"tier_1": "Multiply numerator and denominator by the conjugate of the denominator (2 - i).",
         "tier_2": f"Denominator is 2^2 + 1^2 = 5. Expand the numerator.",
         "tier_3": correct},
        ["forgot_to_multiply_numerator_by_conjugate"]
    )


def arch_15_simplifying_complex_fraction_sum(rng: random.Random) -> Dict[str, Any]:
    # 1/(1+i) + 1/(1-i) = (1-i + 1+i)/2 = 2/2 = 1
    # Or k/(1+i) + k/(1-i) = 2k/2 = k
    k = rng.choice([1, 2, 3, 4, 5])
    correct = str(k)
    distractors = [
        f"{k}i",
        f"2{k}",
        "0",
    ]
    prompt = (
        f"Simplify the following sum of complex fractions:\n\n"
        f"$$\\frac{{{k}}}{{1 + i}} + \\frac{{{k}}}{{1 - i}}$$"
    )
    sol = (
        f"Step 1: Find the common denominator $(1 + i)(1 - i)$:\n"
        f"$$\\text{{Common denominator}} = 1^2 - i^2 = 1 - (-1) = 2$$\n"
        f"Step 2: Combine numerators:\n"
        f"$$= \\frac{{{k}(1 - i) + {k}(1 + i)}}{{2}} = \\frac{{{k} - {k}i + {k} + {k}i}}{{2}} = \\frac{{{2*k}}}{{2}} = {k}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_15_{rng.randint(100000, 999999)}", "15_simplifying_complex_fraction_sum",
        "Sum of Conjugate Complex Fractions", prompt, correct, distractors, sol,
        {"tier_1": "Find a common denominator: (1+i)(1-i) = 2.",
         "tier_2": f"Combine the numerators: {k}(1-i) + {k}(1+i) = {2*k}.",
         "tier_3": correct},
        ["retained_imaginary_term_in_conjugate_sum"]
    )


def arch_16_equality_of_two_complex_numbers_linear(rng: random.Random) -> Dict[str, Any]:
    # (x + y) + (x - y)i = a + bi
    # Solve system: x + y = a, x - y = b => 2x = a + b => x = (a+b)/2, y = (a-b)/2
    x_val = rng.choice([-3, -1, 2, 4, 5])
    y_val = rng.choice([-4, -2, 1, 3])
    a = x_val + y_val
    b = x_val - y_val
    prompt = (
        f"Given that $x, y \\in \\mathbb{{R}}$, solve for $x$ and $y$ in the equation:\n\n"
        f"$$(x + y) + (x - y)i = {a} {'+' if b >= 0 else '-'} {abs(b)}i$$"
    )
    ans = f"x = {x_val}, y = {y_val}"
    sol = (
        f"Step 1: Equate real parts and imaginary parts separately:\n"
        f"$$\\text{{Real parts: }} x + y = {a} \\quad \\text{{(Equation 1)}}$$\n"
        f"$$\\text{{Imaginary parts: }} x - y = {b} \\quad \\text{{(Equation 2)}}$$\n"
        f"Step 2: Add Equation 1 and Equation 2 to eliminate $y$:\n"
        f"$$2x = {a} + ({b}) = {a + b} \\implies x = {x_val}$$\n"
        f"Step 3: Substitute $x = {x_val}$ into Equation 1:\n"
        f"$${x_val} + y = {a} \\implies y = {a} - ({x_val}) = {y_val}$$\n"
        f"Solution: $x = {x_val}$ and $y = {y_val}$."
    )
    return _calc_q(
        rng, f"tech_cplx_16_{rng.randint(100000, 999999)}", "16_equality_of_two_complex_numbers_linear",
        "Solving Simultaneous Equations via Equality of Complex Numbers", prompt, ans, sol,
        {"tier_1": "Two complex numbers are equal if and only if their real parts are equal AND their imaginary parts are equal.",
         "tier_2": f"Set x + y = {a} and x - y = {b}. Solve simultaneously.",
         "tier_3": f"x = {x_val}, y = {y_val}."},
        ["equated_real_part_to_imaginary_part"]
    )


def arch_17_equality_of_complex_numbers_with_multiplication(rng: random.Random) -> Dict[str, Any]:
    # (x + 2i)(3 - i) = a + bi
    # 3x - xi + 6i - 2i^2 = (3x + 2) + (6 - x)i
    x_ans = rng.choice([-3, -1, 1, 2, 4])
    real_target = 3 * x_ans + 2
    imag_target = 6 - x_ans
    prompt = (
        f"Determine the real value of $x$ that satisfies the equation:\n\n"
        f"$$(x + 2i)(3 - i) = {real_target} {'+' if imag_target >= 0 else '-'} {abs(imag_target)}i$$"
    )
    ans = str(x_ans)
    sol = (
        f"Step 1: Expand the left-hand side:\n"
        f"$$(x + 2i)(3 - i) = 3x - xi + 6i - 2i^2 = 3x - xi + 6i + 2 = (3x + 2) + (6 - x)i$$\n"
        f"Step 2: Equate real parts:\n"
        f"$$3x + 2 = {real_target} \\implies 3x = {real_target - 2} \\implies x = {x_ans}$$\n"
        f"Step 3: Verify using imaginary parts:\n"
        f"$$6 - x = {imag_target} \\implies x = 6 - ({imag_target}) = {x_ans}$$\n"
        f"Thus $x = {x_ans}$."
    )
    return _calc_q(
        rng, f"tech_cplx_17_{rng.randint(100000, 999999)}", "17_equality_of_complex_numbers_with_multiplication",
        "Solving for Unknown Variable in Complex Equality", prompt, ans, sol,
        {"tier_1": "Expand the left side using FOIL, collect real and imaginary parts, and equate.",
         "tier_2": f"3x + 2 = {real_target}, solve for x.",
         "tier_3": f"x = {x_ans}."},
        ["arithmetic_error_expanding_brackets_with_imaginary_unit"]
    )


def arch_18_argand_diagram_coordinates_and_quadrant(rng: random.Random) -> Dict[str, Any]:
    quad = rng.choice([1, 2, 3, 4])
    if quad == 1:
        a, b = rng.randint(2, 6), rng.randint(2, 6)
    elif quad == 2:
        a, b = -rng.randint(2, 6), rng.randint(2, 6)
    elif quad == 3:
        a, b = -rng.randint(2, 6), -rng.randint(2, 6)
    else:
        a, b = rng.randint(2, 6), -rng.randint(2, 6)

    correct = f"({a}; {b}) in Quadrant {quad}"
    distractors = [
        f"({b}; {a}) in Quadrant {quad}",
        f"({a}; {-b}) in Quadrant {(quad % 4) + 1}",
        f"({-a}; {b}) in Quadrant {((quad + 1) % 4) + 1}",
    ]
    prompt = (
        f"A complex number is given by $z = {a} {'+' if b >= 0 else '-'} {abs(b)}i$.\n\n"
        f"State the Cartesian coordinates of $z$ on the Argand plane and identify the quadrant in which it lies."
    )
    sol = (
        f"Step 1: On the Argand plane, the horizontal axis represents the Real part ($\\text{{Re}}$) "
        f"and the vertical axis represents the Imaginary part ($\\text{{Im}}$):\n"
        f"$$x = \\text{{Re}}(z) = {a}, \\quad y = \\text{{Im}}(z) = {b}$$\n"
        f"Coordinates: $({a};\\ {b})$.\n"
        f"Step 2: Identify the quadrant:\n"
        f"Since $x {'> 0' if a > 0 else '< 0'}$ and $y {'> 0' if b > 0 else '< 0'}$, the point lies in Quadrant {quad}."
    )
    return _mcq_q(
        rng, f"tech_cplx_18_{rng.randint(100000, 999999)}", "18_argand_diagram_coordinates_and_quadrant",
        "Argand Diagram Coordinates and Quadrant Location", prompt, correct, distractors, sol,
        {"tier_1": "The real part is plotted on the horizontal axis; the imaginary coefficient is on the vertical axis.",
         "tier_2": f"Point is ({a}; {b}). Check signs to identify Quadrant {quad}.",
         "tier_3": correct},
        ["swapped_real_and_imaginary_coordinates_on_argand_plane"]
    )


def arch_19_argand_diagram_vector_representation_svg(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5])
    b = rng.choice([2, 3, 4])
    # SVG coordinates
    origin_x, origin_y = 120, 180
    scale = 22
    pt_x = origin_x + a * scale
    pt_y = origin_y - b * scale

    ref_id = rng.randint(10, 99)
    stroke_col = rng.choice(["#2563eb", "#1d4ed8", "#3b82f6"])

    svg_body = (
        f'<line x1="30" y1="{origin_y}" x2="360" y2="{origin_y}" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="365" y="{origin_y + 4}" font-size="11" fill="#475569">Re</text>'
        f'<line x1="{origin_x}" y1="20" x2="{origin_x}" y2="260" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="{origin_x - 12}" y="15" font-size="11" fill="#475569">Im</text>'
        f'<line x1="{origin_x}" y1="{origin_y}" x2="{pt_x}" y2="{pt_y}" stroke="{stroke_col}" stroke-width="2.5" marker-end="url(#arrow)"/>'
        f'<line x1="{pt_x}" y1="{origin_y}" x2="{pt_x}" y2="{pt_y}" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<line x1="{origin_x}" y1="{pt_y}" x2="{pt_x}" y2="{pt_y}" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<circle cx="{pt_x}" cy="{pt_y}" r="4" fill="#dc2626"/>'
        f'<text x="{pt_x + 8}" y="{pt_y}" font-size="11" font-weight="bold" fill="#dc2626">P({a}; {b})</text>'
        f'<text x="240" y="30" font-size="11" font-weight="bold" fill="{stroke_col}">z = {a} + {b}i [Ref #{ref_id}]</text>'
    )
    prompt = (
        f"The visual display presents the vector representation of a complex number $z$ [Ref #{ref_id}] on the Argand plane shown.\n\n"
        f"1. Read the coordinates of point $P$ from the diagram.\n"
        f"2. Write down the complex number $z$ in rectangular form $a + bi$."
    )
    correct = f"z = {a} + {b}i"
    distractors = [
        f"z = {b} + {a}i",
        f"z = {a} - {b}i",
        f"z = -{a} + {b}i",
    ]
    sol = (
        f"Step 1: Read the projection on the Real axis (horizontal): $\\text{{Re}} = {a}$.\n"
        f"Step 2: Read the projection on the Imaginary axis (vertical): $\\text{{Im}} = {b}$.\n"
        f"Step 3: Express in standard form:\n"
        f"$$z = {a} + {b}i$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_19_{rng.randint(100000, 999999)}", "19_argand_diagram_vector_representation_svg",
        "Vector Representation on Argand Diagram", prompt, correct, distractors, sol,
        {"tier_1": "Read the real coordinate from the horizontal axis and the imaginary from the vertical axis.",
         "tier_2": f"Point P is at ({a}; {b}), so z = {a} + {b}i.",
         "tier_3": correct},
        ["confused_real_and_imaginary_axes_in_reading_vector"],
        diagram_spec=_svg_spec(svg_body, 420, 280)
    )


def arch_20_modulus_calculation_exact_surd(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([-7, -5, -3, 3, 5, 7])
    b = rng.choice([-6, -4, -2, 2, 4, 6])
    r_sq = a**2 + b**2
    r_surd = sp.sqrt(r_sq)
    surd_str = sp.latex(r_surd)
    prompt = (
        f"Calculate the modulus $|z|$ of the complex number $z = {a} {'+' if b >= 0 else '-'} {abs(b)}i$.\n\n"
        f"Express your answer in simplest surd form."
    )
    ans = f"|z| = {surd_str}"
    sol = (
        f"Step 1: Apply the modulus formula $|z| = \\sqrt{{a^2 + b^2}}$:\n"
        f"$$|z| = \\sqrt{{({a})^2 + ({b})^2}}$$\n"
        f"Step 2: Calculate the sum of squares:\n"
        f"$$|z| = \\sqrt{{{a**2} + {b**2}}} = \\sqrt{{{r_sq}}}$$\n"
        f"Step 3: Express in simplest surd form:\n"
        f"$$|z| = {surd_str}$$."
    )
    return _calc_q(
        rng, f"tech_cplx_20_{rng.randint(100000, 999999)}", "20_modulus_calculation_exact_surd",
        "Exact Surd Modulus of Complex Number", prompt, ans, sol,
        {"tier_1": "Modulus formula: |z| = sqrt(a^2 + b^2).",
         "tier_2": f"|z| = sqrt({a**2} + {b**2}) = sqrt({r_sq}). Simplify the surd.",
         "tier_3": f"|z| = {surd_str}."},
        ["included_i_squared_inside_modulus_root"]
    )


def arch_21_modulus_special_pythagorean_triples(rng: random.Random) -> Dict[str, Any]:
    triples = [
        (3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (7, 24, 25)
    ]
    a_base, b_base, c_mod = rng.choice(triples)
    s1 = rng.choice([-1, 1])
    s2 = rng.choice([-1, 1])
    a = a_base * s1
    b = b_base * s2
    prompt = (
        f"Determine the modulus $|z|$ of the complex number $z = {a} {'+' if b >= 0 else '-'} {abs(b)}i$."
    )
    ans = str(c_mod)
    sol = (
        f"Step 1: Apply the modulus formula:\n"
        f"$$|z| = \\sqrt{{a^2 + b^2}} = \\sqrt{{({a})^2 + ({b})^2}}$$\n"
        f"Step 2: Calculate numerical value:\n"
        f"$$|z| = \\sqrt{{{a**2} + {b**2}}} = \\sqrt{{{c_mod**2}}} = {c_mod}$$."
    )
    return _calc_q(
        rng, f"tech_cplx_21_{rng.randint(100000, 999999)}", "21_modulus_special_pythagorean_triples",
        "Modulus with Integer Pythagorean Triple", prompt, ans, sol,
        {"tier_1": f"Calculate sqrt({a}^2 + {b}^2).",
         "tier_2": f"sqrt({a**2 + b**2}) is an exact integer.",
         "tier_3": f"|z| = {c_mod}."},
        ["squared_negative_number_to_negative_result"]
    )


def arch_22_argument_first_quadrant_degrees(rng: random.Random) -> Dict[str, Any]:
    # Special exact angle in Q1: 30, 45, 60
    angle_choice = rng.choice([30, 45, 60])
    if angle_choice == 30:
        z_str = "\\sqrt{3} + i"
        theta_ans = "30^\\circ"
    elif angle_choice == 45:
        z_str = "1 + i"
        theta_ans = "45^\\circ"
    else:
        z_str = "1 + \\sqrt{3}i"
        theta_ans = "60^\\circ"

    prompt = (
        f"Determine the argument $\\theta$ (where $0^\\circ \\le \\theta < 360^\\circ$) "
        f"of the complex number $z = {z_str}$."
    )
    correct = f"theta = {theta_ans}"
    distractors = [
        "theta = 15^\\circ",
        "theta = 90^\\circ",
        "theta = 45^\\circ" if angle_choice != 45 else "theta = 30^\\circ",
    ]
    sol = (
        f"Step 1: Both real and imaginary parts are positive, so $z$ lies in Quadrant 1:\n"
        f"$$\\tan \\theta = \\frac{{b}}{{a}}$$\n"
        f"Step 2: Evaluate the inverse tangent for special angle:\n"
        f"$$\\theta = \\arctan\\left(\\frac{{b}}{{a}}\\right) = {theta_ans}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_22_{rng.randint(100000, 999999)}", "22_argument_first_quadrant_degrees",
        "Argument of Complex Number in First Quadrant", prompt, correct, distractors, sol,
        {"tier_1": "Use tan(theta) = b / a.",
         "tier_2": f"For {z_str}, identify the special angle in quadrant 1.",
         "tier_3": correct},
        ["confused_special_angles_30_and_60"]
    )


def arch_23_argument_quadrants_two_three_four(rng: random.Random) -> Dict[str, Any]:
    quad = rng.choice([2, 3, 4])
    if quad == 2:
        # z = -1 + i => alpha = 45, theta = 180 - 45 = 135
        z_str = "-1 + i"
        theta_ans = "135^\\circ"
        quad_sol = "Quadrant 2: \\theta = 180^\\circ - 45^\\circ = 135^\\circ"
    elif quad == 3:
        # z = -1 - i => alpha = 45, theta = 180 + 45 = 225
        z_str = "-1 - i"
        theta_ans = "225^\\circ"
        quad_sol = "Quadrant 3: \\theta = 180^\\circ + 45^\\circ = 225^\\circ"
    else:
        # z = 1 - i => alpha = 45, theta = 360 - 45 = 315
        z_str = "1 - i"
        theta_ans = "315^\\circ"
        quad_sol = "Quadrant 4: \\theta = 360^\\circ - 45^\\circ = 315^\\circ"

    prompt = (
        f"Determine the argument $\\theta$ (in degrees, where $0^\\circ \\le \\theta < 360^\\circ$) "
        f"of the complex number $z = {z_str}$."
    )
    correct = f"theta = {theta_ans}"
    distractors = [
        "theta = 45^\\circ",
        "theta = -45^\\circ",
        "theta = 180^\\circ",
    ]
    sol = (
        f"Step 1: Find the reference angle $\\alpha$:\n"
        f"$$\\tan \\alpha = \\left| \\frac{{b}}{{a}} \\right| = \\frac{{1}}{{1}} = 1 \\implies \\alpha = 45^\\circ$$\n"
        f"Step 2: Determine the quadrant and apply the CAST rule:\n"
        f"{quad_sol}."
    )
    return _mcq_q(
        rng, f"tech_cplx_23_{rng.randint(100000, 999999)}", "23_argument_quadrants_two_three_four",
        "Argument Calculation Across Quadrants 2, 3, and 4", prompt, correct, distractors, sol,
        {"tier_1": "Find reference angle alpha = arctan|b/a|, then adjust for quadrant (Q2: 180-alpha, Q3: 180+alpha, Q4: 360-alpha).",
         "tier_2": f"z = {z_str} lies in Quadrant {quad}.",
         "tier_3": correct},
        ["omitted_quadrant_adjustment_for_argument"]
    )


def arch_24_rectangular_to_polar_conversion(rng: random.Random) -> Dict[str, Any]:
    # Special exact polar form:
    # 1. z = 1 + i => r = sqrt(2), theta = 45
    # 2. z = -1 + i => r = sqrt(2), theta = 135
    # 3. z = -sqrt(3) + i => r = 2, theta = 150
    # 4. z = 1 - sqrt(3)i => r = 2, theta = 300
    choice = rng.choice([1, 2, 3, 4])
    if choice == 1:
        z_str = "1 + i"
        r_str = "\\sqrt{2}"
        theta_val = 45
    elif choice == 2:
        z_str = "-1 + i"
        r_str = "\\sqrt{2}"
        theta_val = 135
    elif choice == 3:
        z_str = "-\\sqrt{3} + i"
        r_str = "2"
        theta_val = 150
    else:
        z_str = "1 - \\sqrt{3}i"
        r_str = "2"
        theta_val = 300

    correct = f"z = {r_str}(\\cos {theta_val}^\\circ + i\\sin {theta_val}^\\circ)"
    distractors = [
        f"z = {r_str}(\\cos {theta_val}^\\circ - i\\sin {theta_val}^\\circ)",
        f"z = {r_str}(\\sin {theta_val}^\\circ + i\\cos {theta_val}^\\circ)",
        f"z = 2(\\cos {theta_val}^\\circ + i\\sin {theta_val}^\\circ)" if r_str != "2" else f"z = \\sqrt{{2}}(\\cos {theta_val}^\\circ + i\\sin {theta_val}^\\circ)",
    ]
    prompt = (
        f"Convert the complex number $z = {z_str}$ from rectangular form to trigonometric (polar) form $z = r(\\cos \\theta + i\\sin \\theta)$."
    )
    sol = (
        f"Step 1: Calculate the modulus $r$:\n"
        f"$$r = |z| = \\sqrt{{a^2 + b^2}} = {r_str}$$\n"
        f"Step 2: Calculate the argument $\\theta$:\n"
        f"$$\\theta = {theta_val}^\\circ$$\n"
        f"Step 3: Write in polar form:\n"
        f"$$z = {correct}$$."
    )
    return _mcq_q(
        rng, f"tech_cplx_24_{rng.randint(100000, 999999)}", "24_rectangular_to_polar_conversion",
        "Conversion from Rectangular to Polar Trigonometric Form", prompt, correct, distractors, sol,
        {"tier_1": "Find modulus r = sqrt(a^2 + b^2) and argument theta, then write r(cos theta + i sin theta).",
         "tier_2": f"For {z_str}, r = {r_str} and theta = {theta_val} degrees.",
         "tier_3": correct},
        ["swapped_sine_and_cosine_in_polar_form"]
    )


def arch_25_polar_to_rectangular_conversion(rng: random.Random) -> Dict[str, Any]:
    # r = 4, theta = 30 => 4(sqrt(3)/2 + 1/2 i) = 2*sqrt(3) + 2i
    # r = 2, theta = 45 => 2(sqrt(2)/2 + sqrt(2)/2 i) = sqrt(2) + sqrt(2)i
    # r = 6, theta = 60 => 6(1/2 + sqrt(3)/2 i) = 3 + 3*sqrt(3)i
    # r = 5, theta = 180 => -5
    choice = rng.choice([1, 2, 3, 4])
    if choice == 1:
        r_val = 4
        theta_val = 30
        correct = "2\\sqrt{3} + 2i"
        sol_expand = "4(\\frac{\\sqrt{3}}{2} + \\frac{1}{2}i) = 2\\sqrt{3} + 2i"
    elif choice == 2:
        r_val = 2
        theta_val = 45
        correct = "\\sqrt{2} + \\sqrt{2}i"
        sol_expand = "2(\\frac{\\sqrt{2}}{2} + \\frac{\\sqrt{2}}{2}i) = \\sqrt{2} + \\sqrt{2}i"
    elif choice == 3:
        r_val = 6
        theta_val = 60
        correct = "3 + 3\\sqrt{3}i"
        sol_expand = "6(\\frac{1}{2} + \\frac{\\sqrt{3}}{2}i) = 3 + 3\\sqrt{3}i"
    else:
        r_val = 5
        theta_val = 180
        correct = "-5"
        sol_expand = "5(-1 + 0i) = -5"

    distractors = [
        f"{r_val} + {theta_val}i",
        f"\\sqrt{{{r_val}}} + \\sqrt{{{theta_val}}}i",
        "1 + i",
    ]
    prompt = (
        f"Convert $z = {r_val}(\\cos {theta_val}^\\circ + i\\sin {theta_val}^\\circ)$ from polar form into standard rectangular form ($a + bi$)."
    )
    sol = (
        f"Step 1: Evaluate the trigonometric ratios for $\\theta = {theta_val}^\\circ$:\n"
        f"$$\\cos {theta_val}^\\circ \\quad \\text{{and}} \\quad \\sin {theta_val}^\\circ$$\n"
        f"Step 2: Distribute $r = {r_val}$:\n"
        f"$$z = {sol_expand}$$\n"
        f"Rectangular form: ${correct}$."
    )
    return _mcq_q(
        rng, f"tech_cplx_25_{rng.randint(100000, 999999)}", "25_polar_to_rectangular_conversion",
        "Conversion from Polar to Rectangular Form", prompt, correct, distractors, sol,
        {"tier_1": "Calculate a = r * cos(theta) and b = r * sin(theta).",
         "tier_2": f"Evaluate cos({theta_val}) and sin({theta_val}) using special angles, then multiply by {r_val}.",
         "tier_3": correct},
        ["forgot_to_distribute_modulus_r_to_both_terms"]
    )


# ==============================================================================
# Subskills Dictionary and Builders Mapping for 01 - 25
# ==============================================================================

BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_powers_of_i_simplification": arch_01_powers_of_i_simplification,
    "02_powers_of_i_linear_combination": arch_02_powers_of_i_linear_combination,
    "03_even_roots_of_negative_real_numbers": arch_03_even_roots_of_negative_real_numbers,
    "04_addition_and_subtraction_rectangular": arch_04_addition_and_subtraction_rectangular,
    "05_scalar_multiplication_rectangular": arch_05_scalar_multiplication_rectangular,
    "06_multiplication_monomial_times_binomial": arch_06_multiplication_monomial_times_binomial,
    "07_multiplication_binomial_times_binomial": arch_07_multiplication_binomial_times_binomial,
    "08_squaring_complex_binomial": arch_08_squaring_complex_binomial,
    "09_difference_of_squares_identity": arch_09_difference_of_squares_identity,
    "10_complex_conjugate_definition": arch_10_complex_conjugate_definition,
    "11_product_of_complex_number_and_conjugate": arch_11_product_of_complex_number_and_conjugate,
    "12_division_pure_imaginary_denominator": arch_12_division_pure_imaginary_denominator,
    "13_division_monic_denominator": arch_13_division_monic_denominator,
    "14_division_general_complex_numbers": arch_14_division_general_complex_numbers,
    "15_simplifying_complex_fraction_sum": arch_15_simplifying_complex_fraction_sum,
    "16_equality_of_two_complex_numbers_linear": arch_16_equality_of_two_complex_numbers_linear,
    "17_equality_of_complex_numbers_with_multiplication": arch_17_equality_of_complex_numbers_with_multiplication,
    "18_argand_diagram_coordinates_and_quadrant": arch_18_argand_diagram_coordinates_and_quadrant,
    "19_argand_diagram_vector_representation_svg": arch_19_argand_diagram_vector_representation_svg,
    "20_modulus_calculation_exact_surd": arch_20_modulus_calculation_exact_surd,
    "21_modulus_special_pythagorean_triples": arch_21_modulus_special_pythagorean_triples,
    "22_argument_first_quadrant_degrees": arch_22_argument_first_quadrant_degrees,
    "23_argument_quadrants_two_three_four": arch_23_argument_quadrants_two_three_four,
    "24_rectangular_to_polar_conversion": arch_24_rectangular_to_polar_conversion,
    "25_polar_to_rectangular_conversion": arch_25_polar_to_rectangular_conversion,
}

SUBSKILLS_01_25: Dict[str, str] = {
    "01_powers_of_i_simplification": "Simplifying Higher Powers of Imaginary Unit",
    "02_powers_of_i_linear_combination": "Linear Combination of Cyclic Powers of i",
    "03_even_roots_of_negative_real_numbers": "Even Roots of Negative Real Numbers",
    "04_addition_and_subtraction_rectangular": "Addition and Subtraction of Complex Numbers in Rectangular Form",
    "05_scalar_multiplication_rectangular": "Scalar Multiplication of Complex Numbers",
    "06_multiplication_monomial_times_binomial": "Monomial Imaginary Term Multiplied by Binomial Complex Number",
    "07_multiplication_binomial_times_binomial": "Multiplication of Two Complex Numbers via FOIL",
    "08_squaring_complex_binomial": "Squaring a Complex Binomial",
    "09_difference_of_squares_identity": "Difference of Squared Conjugate Binomials",
    "10_complex_conjugate_definition": "Determination of Complex Conjugate",
    "11_product_of_complex_number_and_conjugate": "Product of Complex Number with its Conjugate",
    "12_division_pure_imaginary_denominator": "Division by a Pure Imaginary Number",
    "13_division_monic_denominator": "Complex Number Division with Binomial Denominator",
    "14_division_general_complex_numbers": "Division of General Complex Numbers",
    "15_simplifying_complex_fraction_sum": "Sum of Conjugate Complex Fractions",
    "16_equality_of_two_complex_numbers_linear": "Solving Simultaneous Equations via Equality of Complex Numbers",
    "17_equality_of_complex_numbers_with_multiplication": "Solving for Unknown Variable in Complex Equality",
    "18_argand_diagram_coordinates_and_quadrant": "Argand Diagram Coordinates and Quadrant Location",
    "19_argand_diagram_vector_representation_svg": "Vector Representation on Argand Diagram",
    "20_modulus_calculation_exact_surd": "Exact Surd Modulus of Complex Number",
    "21_modulus_special_pythagorean_triples": "Modulus with Integer Pythagorean Triple",
    "22_argument_first_quadrant_degrees": "Argument of Complex Number in First Quadrant",
    "23_argument_quadrants_two_three_four": "Argument Calculation Across Quadrants 2, 3, and 4",
    "24_rectangular_to_polar_conversion": "Conversion from Rectangular to Polar Trigonometric Form",
    "25_polar_to_rectangular_conversion": "Conversion from Polar to Rectangular Form",
}
