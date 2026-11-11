"""Grade 9 Mathematics - Exponents Archetypes 01 to 25.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 1/03. Exponents.md:
Laws of exponents (Product, Quotient, Power of a Power, Power of Product/Quotient,
Zero and Negative exponents, Sign rules, Rational exponents, and Scientific Notation).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .exponents_svg import (
    draw_scientific_scale_comparison_svg,
)


# ----------------------------------------------------------------------
# 01. Product Law: Single Variable Positive Indices
# ----------------------------------------------------------------------
def arch_01_product_law_single_variable_positive_indices(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "a", "m", "p"])
    p1 = rng.randint(2, 7)
    p2 = rng.randint(2, 8)
    ans_p = p1 + p2

    prompt = (
        f"Simplify using the product law of exponents, leaving your answer in exponential form:\n\n"
        f"\\[ {var}^{{{p1}}} \\cdot {var}^{{{p2}}} \\]"
    )
    ans = f"{var}^{{{ans_p}}}"
    sol = (
        f"**Product Law (Same Base):**\n"
        f"Keep base and add exponents: \\({var}^{{{p1} + {p2}}} = {ans}\\)."
    )
    return {
        "id": f"g9_exp_prod_single_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Add exponents to get {ans}", "marks": 1},
        ],
        "hints": [
            "When multiplying terms with the same base, add their exponents: a^m * a^n = a^(m+n).",
            f"Add {p1} + {p2}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 02. Product Law: Numerical Base Same Base
# ----------------------------------------------------------------------
def arch_02_product_law_numerical_base_same_base(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7])
    p1 = rng.randint(2, 5)
    p2 = rng.randint(2, 5)
    ans_p = p1 + p2

    ans = f"{base}^{{{ans_p}}}"
    prompt = (
        f"Simplify using the product rule of exponents. Leave your answer in power form:\n\n"
        f"\\[ {base}^{{{p1}}} \\times {base}^{{{p2}}} \\]"
    )
    sol = (
        f"**Product Rule with Numerical Base:**\n"
        f"Do NOT multiply the bases together. Keep base \\({base}\\) unchanged and add powers:\n"
        f"\\[ {base}^{{{p1}}} \\times {base}^{{{p2}}} = {base}^{{{p1} + {p2}}} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_prod_num_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Keep base {base} and sum exponents: {ans}", "marks": 1},
        ],
        "hints": [
            "Do not multiply base by base.",
            f"Keep base {base} and add the powers {p1} + {p2}.",
            f"Answer in power form: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 03. Product Law: Coefficients and Multiple Variables
# ----------------------------------------------------------------------
def arch_03_product_law_coefficients_and_multiple_variables(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(2, 6)
    c2 = rng.randint(2, 5)
    coeff = c1 * c2

    x1, x2 = rng.randint(1, 4), rng.randint(2, 5)
    y1, y2 = rng.randint(2, 5), rng.randint(1, 4)
    tot_x = x1 + x2
    tot_y = y1 + y2

    x1_str = f"x^{{{x1}}}" if x1 > 1 else "x"
    x2_str = f"x^{{{x2}}}" if x2 > 1 else "x"
    y1_str = f"y^{{{y1}}}" if y1 > 1 else "y"
    y2_str = f"y^{{{y2}}}" if y2 > 1 else "y"

    ans = f"{coeff}x^{{{tot_x}}}y^{{{tot_y}}}"
    prompt = (
        f"Simplify the algebraic product completely:\n\n"
        f"\\[ ({c1}{x1_str}{y1_str})({c2}{x2_str}{y2_str}) \\]"
    )
    sol = (
        f"**Coefficients and Exponents:**\n"
        f"1. Coefficients: \\({c1} \\times {c2} = {coeff}\\).\n"
        f"2. \\(x\\) exponents: \\({x1} + {x2} = {tot_x}\\).\n"
        f"3. \\(y\\) exponents: \\({y1} + {y2} = {tot_y}\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_exp_prod_coeff_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Multiply coefficients {c1} * {c2} = {coeff}", "marks": 1},
            {"desc": f"Sum like variable powers to obtain {ans}", "marks": 1},
        ],
        "hints": [
            "Multiply the numbers in front.",
            "Add the exponents of matching letters.",
            f"Final product: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 04. Quotient Law: Single Variable Positive Result
# ----------------------------------------------------------------------
def arch_04_quotient_law_single_variable_positive_result(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["a", "b", "x", "k", "t"])
    diff = rng.randint(2, 6)
    p2 = rng.randint(2, 5)
    p1 = p2 + diff

    ans = f"{var}^{{{diff}}}"
    prompt = (
        f"Simplify using the quotient law of exponents:\n\n"
        f"\\[ \\frac{{{var}^{{{p1}}}}}{{{var}^{{{p2}}}}} \\]"
    )
    sol = (
        f"**Quotient Law (Same Base):**\n"
        f"Subtract denominator exponent from numerator exponent:\n"
        f"\\[ {var}^{{{p1} - {p2}}} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_quot_single_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Subtract exponents: {ans}", "marks": 1},
        ],
        "hints": [
            "When dividing powers with the same base, subtract exponents: a^m / a^n = a^(m-n).",
            f"Subtract {p1} - {p2}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 05. Quotient Law: Coefficients and Multiple Variables
# ----------------------------------------------------------------------
def arch_05_quotient_law_coefficients_and_multiple_variables(rng: random.Random) -> Dict[str, Any]:
    c_den = rng.choice([2, 3, 4, 5])
    c_mult = rng.choice([2, 3, 4, 6])
    c_num = c_den * c_mult

    x_diff = rng.randint(2, 5)
    x_den = rng.randint(1, 3)
    x_num = x_den + x_diff

    y_diff = rng.randint(1, 4)
    y_den = rng.randint(1, 3)
    y_num = y_den + y_diff

    y_diff_str = f"y^{{{y_diff}}}" if y_diff > 1 else "y"
    ans = f"{c_mult}x^{{{x_diff}}}{y_diff_str}"

    prompt = (
        f"Simplify the fraction completely using the quotient law:\n\n"
        f"\\[ \\frac{{{c_num}x^{{{x_num}}}y^{{{y_num}}}}}{{{c_den}x^{{{x_den}}}y^{{{y_den}}}}} \\]"
    )
    sol = (
        f"**Quotient Simplification:**\n"
        f"1. Coefficients: \\({c_num} \\div {c_den} = {c_mult}\\).\n"
        f"2. \\(x\\) exponents: \\({x_num} - {x_den} = {x_diff}\\).\n"
        f"3. \\(y\\) exponents: \\({y_num} - {y_den} = {y_diff}\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_exp_quot_coeff_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Divide coefficients {c_num} / {c_den} = {c_mult}", "marks": 1},
            {"desc": f"Subtract variable exponents to get {ans}", "marks": 1},
        ],
        "hints": [
            "Divide the numerical coefficients.",
            "Subtract exponents for each variable.",
            f"Simplified: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 06. Power of a Power: Single Variable
# ----------------------------------------------------------------------
def arch_06_power_of_a_power_single_variable(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "m", "p"])
    p1 = rng.randint(2, 5)
    p2 = rng.randint(2, 6)
    ans_p = p1 * p2

    ans = f"{var}^{{{ans_p}}}"
    prompt = (
        f"Simplify using the power of a power law:\n\n"
        f"\\[ ({var}^{{{p1}}})^{{{p2}}} \\]"
    )
    sol = (
        f"**Power of a Power Law:**\n"
        f"Multiply the exponents together:\n"
        f"\\[ ({var}^{{{p1}}})^{{{p2}}} = {var}^{{{p1} \\times {p2}}} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_pow_pow_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Multiply exponents to yield {ans}", "marks": 1},
        ],
        "hints": [
            "When raising a power to a power, multiply exponents: (a^m)^n = a^(m*n).",
            f"Multiply {p1} * {p2}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 07. Power of a Product: Coefficients and Variables
# ----------------------------------------------------------------------
def arch_07_power_of_a_product_coefficients_and_variables(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3])
    outer = rng.choice([2, 3, 4])
    px = rng.randint(1, 3)
    py = rng.randint(2, 4)

    c_pow = c ** outer
    tot_x = px * outer
    tot_y = py * outer

    px_str = f"x^{{{px}}}" if px > 1 else "x"
    ans = f"{c_pow}x^{{{tot_x}}}y^{{{tot_y}}}"

    prompt = (
        f"Simplify by raising every factor in the product to the outside exponent:\n\n"
        f"\\[ ({c}{px_str}y^{{{py}}})^{{{outer}}} \\]"
    )
    sol = (
        f"**Power of a Product Law:**\n"
        f"Apply exponent \\({outer}\\) to each factor inside:\n"
        f"1. \\({c}^{{{outer}}} = {c_pow}\\).\n"
        f"2. \\(({px_str})^{{{outer}}} = x^{{{tot_x}}}\\).\n"
        f"3. \\((y^{{{py}}})^{{{outer}}} = y^{{{tot_y}}}\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_exp_pow_prod_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Raise coefficient {c}^{outer} = {c_pow}", "marks": 1},
            {"desc": f"Multiply variable exponents to yield {ans}", "marks": 1},
        ],
        "hints": [
            f"Do not forget to raise the number {c} to the power {outer}.",
            "Multiply the exponent of each variable by the outside exponent.",
            f"Result: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 08. Power of a Quotient: Fractional Base
# ----------------------------------------------------------------------
def arch_08_power_of_a_quotient_fractional_base(rng: random.Random) -> Dict[str, Any]:
    c_num = rng.choice([2, 3])
    c_den = 5 if c_num == 2 else 4
    outer = rng.choice([2, 3])
    px = rng.randint(2, 4)
    py = rng.randint(1, 3)

    num_pow = c_num ** outer
    den_pow = c_den ** outer
    tot_x = px * outer
    tot_y = py * outer

    py_str = f"b^{{{py}}}" if py > 1 else "b"
    ans = f"\\frac{{{num_pow}a^{{{tot_x}}}}}{{{den_pow}b^{{{tot_y}}}}}"

    prompt = (
        f"Simplify using the power of a quotient law:\n\n"
        f"\\[ \\left(\\frac{{{c_num}a^{{{px}}}}}{{{c_den}{py_str}}}\\right)^{{{outer}}} \\]"
    )
    sol = (
        f"**Power of a Quotient:**\n"
        f"Raise numerator and denominator to power \\({outer}\\):\n"
        f"\\[ = \\frac{{{c_num}^{{{outer}}} (a^{{{px}}})^{{{outer}}}}}{{{c_den}^{{{outer}}} ({py_str})^{{{outer}}}}} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_pow_quot_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Raise numerator to power: {num_pow}a^{tot_x}", "marks": 1},
            {"desc": f"Raise denominator to power: {den_pow}b^{tot_y}", "marks": 1},
        ],
        "hints": [
            "Apply the power to both the top and bottom terms.",
            f"Numerator: {c_num}^{outer} = {num_pow}.",
            f"Result: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 09. Zero Exponent Law: Individual and Bracketed
# ----------------------------------------------------------------------
def arch_09_zero_exponent_law_individual_and_bracketed(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(3, 9)
    cases = [
        (f"({c}x)^0", "1", f"The entire bracket is raised to 0: ({c}x)^0 = 1"),
        (f"{c}x^0", f"{c}", f"Only x is raised to 0: {c} \\times (1) = {c}"),
        (f"-{c}^0", "-1", f"The negative is outside the power: -( {c}^0 ) = -(1) = -1"),
        (f"(-{c})^0", "1", f"The bracketed negative base raised to 0: (-{c})^0 = 1"),
    ]
    expr, ans, sol_exp = rng.choice(cases)

    prompt = (
        f"Evaluate the expression using the zero exponent law (where \\(x \\neq 0\\)):\n\n"
        f"\\[ {expr} \\]"
    )
    sol = (
        f"**Zero Exponent Rule (\\(a^0 = 1\\) for \\(a \\neq 0\\)):**\n"
        f"{sol_exp}.\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_exp_zero_law_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct evaluation {ans}", "marks": 1},
        ],
        "hints": [
            "Any non-zero quantity raised to the power of 0 equals 1.",
            "Pay close attention to whether the brackets encompass the coefficient or sign.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 10. Negative Exponent Definition: Single Variable
# ----------------------------------------------------------------------
def arch_10_negative_exponent_definition_single_variable(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "a", "m"])
    n = rng.randint(2, 6)

    ans = f"\\frac{{1}}{{{var}^{{{n}}}}}"
    prompt = (
        f"Rewrite \\({var}^{{-{n}}}\\) with a positive exponent."
    )
    sol = (
        f"**Negative Exponent Law:**\n"
        f"\\(a^{{-n}} = \\frac{{1}}{{a^n}}\\).\n"
        f"Therefore: \\({var}^{{-{n}}} = {ans}\\)."
    )
    return {
        "id": f"g9_exp_neg_def_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Rewrite with positive power: {ans}", "marks": 1},
        ],
        "hints": [
            "A negative exponent means the reciprocal of the power.",
            f"Move {var} to the denominator with a positive power {n}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 11. Negative Exponent: Numerical Evaluation
# ----------------------------------------------------------------------
def arch_11_negative_exponent_numerical_evaluation(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (2, 3, 8, "2^{-3} = \\frac{1}{2^3} = \\frac{1}{8}"),
        (2, 4, 16, "2^{-4} = \\frac{1}{2^4} = \\frac{1}{16}"),
        (3, 2, 9, "3^{-2} = \\frac{1}{3^2} = \\frac{1}{9}"),
        (5, 2, 25, "5^{-2} = \\frac{1}{5^2} = \\frac{1}{25}"),
        (10, 3, 1000, "10^{-3} = \\frac{1}{10^3} = \\frac{1}{1000}"),
    ]
    b, p, val, sol_step = rng.choice(cases)
    ans = f"\\frac{{1}}{{{val}}}"

    prompt = (
        f"Evaluate the numerical power, expressing the final answer as a common fraction:\n\n"
        f"\\[ {b}^{{-{p}}} \\]"
    )
    sol = (
        f"**Numerical Negative Exponent:**\n"
        f"\\[ {sol_step} \\]"
    )
    return {
        "id": f"g9_exp_neg_num_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Write as 1 / {b}^{p}", "marks": 1},
            {"desc": f"Evaluate power to yield {ans}", "marks": 1},
        ],
        "hints": [
            f"Rewrite {b}^(-{p}) as 1 / ({b}^{p}).",
            f"Calculate {b}^{p}.",
            f"Result: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 12. Negative Exponent in Denominator: Reciprocal
# ----------------------------------------------------------------------
def arch_12_negative_exponent_in_denominator_reciprocal(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 5])
    p = rng.randint(2, 5)
    var = rng.choice(["x", "y", "m"])

    ans = f"{c}{var}^{{{p}}}"
    prompt = (
        f"Simplify by writing with a positive exponent:\n\n"
        f"\\[ \\frac{{{c}}}{{{var}^{{-{p}}}}} \\]"
    )
    sol = (
        f"**Reciprocal Identity:**\n"
        f"\\(\\frac{{1}}{{a^{{-n}}}} = a^n\\).\n"
        f"Therefore: \\(\\frac{{{c}}}{{{var}^{{-{p}}}}} = {ans}\\)."
    )
    return {
        "id": f"g9_exp_neg_denom_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Move to numerator with positive power: {ans}", "marks": 1},
        ],
        "hints": [
            "A negative power in the denominator moves to the numerator as a positive power.",
            f"Coefficient {c} remains in the numerator.",
            f"Result: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 13. Negative Exponent: Fractional Base Inversion
# ----------------------------------------------------------------------
def arch_13_negative_exponent_fractional_base_inversion(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (2, 3, 2, 9, 4),
        (3, 4, 2, 16, 9),
        (2, 5, 2, 25, 4),
        (1, 3, 3, 27, 1),
    ]
    n, d, p, ans_num, ans_den = rng.choice(cases)

    ans = f"\\frac{{{ans_num}}}{{{ans_den}}}" if ans_den > 1 else f"{ans_num}"
    prompt = (
        f"Evaluate the power with a fractional base:\n\n"
        f"\\[ \\left(\\frac{{{n}}}{{{d}}}\\right)^{{-{p}}} \\]"
    )
    sol = (
        f"**Inverting Fractional Base:**\n"
        f"\\(\\left(\\frac{{a}}{{b}}\\right)^{{-n}} = \\left(\\frac{{b}}{{a}}\\right)^n\\).\n"
        f"\\(\\left(\\frac{{{d}}}{{{n}}}\\right)^{{{p}}} = \\frac{{{ans_num}}}{{{ans_den}}} = {ans}\\)."
    )
    return {
        "id": f"g9_exp_neg_frac_base_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Invert fraction to ({d}/{n})^{p}", "marks": 1},
            {"desc": f"Evaluate powers to yield {ans}", "marks": 1},
        ],
        "hints": [
            "Flip the fraction inside to turn the exponent positive.",
            f"Evaluate ({d}/{n})^{p}.",
            f"Result: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 14. Express Expression with Positive Exponents Only
# ----------------------------------------------------------------------
def arch_14_express_expression_with_positive_exponents_only(rng: random.Random) -> Dict[str, Any]:
    # e.g., (4 a^-2 b^3) / (8 a^3 b^-2) = b^5 / (2 a^5)
    c1, c2 = 4, 8
    pa1, pa2 = -2, 3
    pb1, pb2 = 3, -2

    tot_a = pa2 - pa1  # 5 in denominator
    tot_b = pb1 - pb2  # 5 in numerator
    ans = f"\\frac{{b^{{{tot_b}}}}}{{2a^{{{tot_a}}}}}"

    prompt = (
        f"Simplify and write your final answer using **positive exponents only**:\n\n"
        f"\\[ \\frac{{4a^{{-2}}b^3}}{{8a^3 b^{{-2}}}} \\]"
    )
    sol = (
        f"**Positive Exponents Conversion:**\n"
        f"1. Coefficients: \\(\\frac{{4}}{{8}} = \\frac{{1}}{{2}}\\).\n"
        f"2. \\(a\\) terms: \\(a^{{-2 - 3}} = a^{{-5}} = \\frac{{1}}{{a^5}}\\).\n"
        f"3. \\(b\\) terms: \\(b^{{3 - (-2)}} = b^5\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_exp_pos_only_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Simplify coefficients to 1/2", "marks": 1},
            {"desc": f"Shift negative powers to yield {ans}", "marks": 1},
        ],
        "hints": [
            "Subtract exponents: top minus bottom.",
            "Move any negative powers to the opposite side of the fraction bar.",
            f"Simplified: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 15. Distinguish Sign Power: Bracketed vs Unbracketed Even
# ----------------------------------------------------------------------
def arch_15_distinguish_sign_power_bracketed_vs_unbracketed_even(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5])
    p = rng.choice([2, 4])
    val = base ** p

    ans_bracketed = val
    ans_unbracketed = -val

    prompt = (
        f"Evaluate and explain the difference between the following two expressions:\n\n"
        f"1. \\((- {base})^{{{p}}}\\)\n"
        f"2. \\(- {base}^{{{p}}}\\)"
    )
    sol = (
        f"**Sign Rules with Even Powers:**\n"
        f"1. In \\((- {base})^{{{p}}}\\), the negative sign is part of the base being multiplied {p} times:\n"
        f"   \\((- {base})^{{{p}}} = {ans_bracketed}\\) (positive).\n"
        f"2. In \\(- {base}^{{{p}}}\\), only \\({base}\\) is raised to power \\({p}\\), then negated:\n"
        f"   \\(- {base}^{{{p}}} = -({val}) = {ans_unbracketed}\\) (negative)."
    )
    return {
        "id": f"g9_exp_sign_even_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"(-{base})^{p} = {ans_bracketed}; -{base}^{p} = {ans_unbracketed}",
        "expected_answer": f"(-{base})^{p} = {ans_bracketed}; -{base}^{p} = {ans_unbracketed}",
        "sample_answer": f"(-{base})^{p} = {ans_bracketed}; -{base}^{p} = {ans_unbracketed}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Evaluate bracketed power: {ans_bracketed}", "marks": 1},
            {"desc": f"Evaluate unbracketed power: {ans_unbracketed}", "marks": 1},
        ],
        "hints": [
            "An even power of a negative number in brackets is positive.",
            "Without brackets, calculate the power first, then apply the negative sign.",
            f"Results: {ans_bracketed} and {ans_unbracketed}.",
        ],
    }


# ----------------------------------------------------------------------
# 16. Distinguish Sign Power: Bracketed Odd
# ----------------------------------------------------------------------
def arch_16_distinguish_sign_power_bracketed_odd(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3])
    p = rng.choice([3, 5])
    val = base ** p

    ans = -val
    prompt = (
        f"Evaluate the power with an odd exponent:\n\n"
        f"\\[ (- {base})^{{{p}}} \\]"
    )
    sol = (
        f"**Odd Power of Negative Base:**\n"
        f"Multiplying an odd number of negative signs yields a negative result:\n"
        f"\\[ (- {base})^{{{p}}} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_sign_odd_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "expected_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct negative evaluation {ans}", "marks": 1},
        ],
        "hints": [
            "A negative base raised to an odd power is always negative.",
            f"Calculate {base}^{p} and attach a minus sign.",
            f"Result: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 17. Rational Exponent: Unit Fraction Roots
# ----------------------------------------------------------------------
def arch_17_rational_exponent_unit_fraction_square_and_cube_roots(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (16, "1/2", 4, "\\sqrt{16} = 4"),
        (25, "1/2", 5, "\\sqrt{25} = 5"),
        (64, "1/2", 8, "\\sqrt{64} = 8"),
        (27, "1/3", 3, "\\sqrt[3]{27} = 3"),
        (64, "1/3", 4, "\\sqrt[3]{64} = 4"),
        (125, "1/3", 5, "\\sqrt[3]{125} = 5"),
    ]
    base, exp_str, ans, sol_step = rng.choice(cases)

    prompt = (
        f"Evaluate the expression with a rational exponent by converting to radical form:\n\n"
        f"\\[ {base}^{{\\frac{{{exp_str.split('/')[0]}}}{{{exp_str.split('/')[1]}}}}} \\]"
    )
    sol = (
        f"**Rational Exponents Law (\\(a^{{\\frac{{1}}{{n}}}} = \\sqrt[n]{{a}}\\)):**\n"
        f"\\[ {base}^{{\\frac{{{exp_str.split('/')[0]}}}{{{exp_str.split('/')[1]}}}}} = {sol_step} \\]"
    )
    return {
        "id": f"g9_exp_rat_unit_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "expected_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Convert rational exponent to radical form", "marks": 1},
            {"desc": f"Evaluate exact root {ans}", "marks": 1},
        ],
        "hints": [
            "An exponent of 1/2 means square root; 1/3 means cube root.",
            f"Find the root of {base}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 18. Rational Exponent: m/n Numerical Evaluation
# ----------------------------------------------------------------------
def arch_18_rational_exponent_m_over_n_numerical_evaluation(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (8, 2, 3, 4, "(\\sqrt[3]{8})^2 = 2^2 = 4"),
        (27, 2, 3, 9, "(\\sqrt[3]{27})^2 = 3^2 = 9"),
        (16, 3, 4, 8, "(\\sqrt[4]{16})^3 = 2^3 = 8"),
        (25, 3, 2, 125, "(\\sqrt{25})^3 = 5^3 = 125"),
    ]
    b, m, n, ans, sol_step = rng.choice(cases)

    prompt = (
        f"Evaluate without a calculator:\n\n"
        f"\\[ {b}^{{\\frac{{{m}}}{{{n}}}}} \\]"
    )
    sol = (
        f"**Rational Exponents (\\(a^{{\\frac{{m}}{{n}}}} = (\\sqrt[n]{{a}})^m\\)):**\n"
        f"\\[ {b}^{{\\frac{{{m}}}{{{n}}}}} = {sol_step} \\]"
    )
    return {
        "id": f"g9_exp_rat_mn_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "expected_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Take {n}-th root first", "marks": 1},
            {"desc": f"Raise root to power {m} to yield {ans}", "marks": 1},
        ],
        "hints": [
            f"Take the {n}th root of {b} first.",
            f"Then raise that result to the power of {m}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 19. Rational Exponent: Negative Fraction
# ----------------------------------------------------------------------
def arch_19_rational_exponent_negative_fraction(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (16, 1, 2, "\\frac{1}{4}", "\\frac{1}{16^{1/2}} = \\frac{1}{4}"),
        (27, 2, 3, "\\frac{1}{9}", "\\frac{1}{27^{2/3}} = \\frac{1}{(\\sqrt[3]{27})^2} = \\frac{1}{9}"),
        (8, 2, 3, "\\frac{1}{4}", "\\frac{1}{8^{2/3}} = \\frac{1}{(\\sqrt[3]{8})^2} = \\frac{1}{4}"),
        (64, 1, 3, "\\frac{1}{4}", "\\frac{1}{\\sqrt[3]{64}} = \\frac{1}{4}"),
    ]
    b, m, n, ans, sol_step = rng.choice(cases)

    prompt = (
        f"Evaluate the power with a negative rational exponent:\n\n"
        f"\\[ {b}^{{-\\frac{{{m}}}{{{n}}}}} \\]"
    )
    sol = (
        f"**Negative Rational Exponent:**\n"
        f"\\[ {b}^{{-\\frac{{{m}}}{{{n}}}}} = {sol_step} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_rat_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Invert expression using reciprocal rule", "marks": 1},
            {"desc": f"Evaluate rational root to obtain {ans}", "marks": 1},
        ],
        "hints": [
            "Use the negative exponent rule to write as 1 / (base^power).",
            "Evaluate the root and power in the denominator.",
            f"Result: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 20. Scientific Notation: Convert Large Numbers to Standard Form
# ----------------------------------------------------------------------
def arch_20_scientific_notation_convert_large_numbers_standard_form(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (450000000, "4{,}5 \\times 10^8", "450 000 000"),
        (3800000, "3{,}8 \\times 10^6", "3 800 000"),
        (125000000, "1{,}25 \\times 10^8", "125 000 000"),
        (6020000000, "6{,}02 \\times 10^9", "6 020 000 000"),
    ]
    val, ans, val_str = rng.choice(cases)

    prompt = (
        f"Write the number \\({val_str}\\) in scientific notation (standard form \\(A \\times 10^k\\) where \\(1 \\le A < 10\\))."
    )
    sol = (
        f"**Scientific Notation (Large Number):**\n"
        f"Place decimal comma after the first non-zero digit:\n"
        f"\\[ {val_str} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_sci_large_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct scientific notation {ans}", "marks": 1},
        ],
        "hints": [
            "Move the comma so that only one non-zero digit is before it.",
            "Count how many places the comma moved: that is the exponent of 10.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 21. Scientific Notation: Convert Small Decimals to Standard Form
# ----------------------------------------------------------------------
def arch_21_scientific_notation_convert_small_decimals_standard_form(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("0{,}00034", "3{,}4 \\times 10^{-4}", 4),
        ("0{,}000058", "5{,}8 \\times 10^{-5}", 5),
        ("0{,}0072", "7{,}2 \\times 10^{-3}", 3),
        ("0{,}0000019", "1{,}9 \\times 10^{-6}", 6),
    ]
    val_str, ans, places = rng.choice(cases)

    prompt = (
        f"Write the small decimal \\({val_str}\\) in scientific notation."
    )
    sol = (
        f"**Scientific Notation (Small Number):**\n"
        f"Shift comma {places} places right to place after first non-zero digit:\n"
        f"\\[ {val_str} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_sci_small_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct negative power scientific notation {ans}", "marks": 1},
        ],
        "hints": [
            "For numbers between 0 and 1, the exponent of 10 is negative.",
            f"Move the comma {places} places to the right.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 22. Scientific Notation: Expand to Ordinary Decimal
# ----------------------------------------------------------------------
def arch_22_scientific_notation_expand_to_ordinary_decimal(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("3{,}45 \\times 10^5", "345 000"),
        ("1{,}8 \\times 10^4", "18 000"),
        ("5{,}2 \\times 10^{-3}", "0{,}0052"),
        ("8{,}04 \\times 10^{-4}", "0{,}000804"),
    ]
    sci_str, ans = rng.choice(cases)

    prompt = (
        f"Write the scientific notation number \\({sci_str}\\) in ordinary decimal notation."
    )
    sol = (
        f"**Expanding Scientific Notation:**\n"
        f"Multiply by the power of 10:\n"
        f"\\[ {sci_str} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_sci_expand_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Correct standard expansion {ans}", "marks": 1},
        ],
        "hints": [
            "Positive power moves the comma right; negative power moves it left.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 23. Scientific Notation: Multiplication of Two Numbers
# ----------------------------------------------------------------------
def arch_23_scientific_notation_multiplication_of_two_numbers(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2.0, 3.0, 4.0])
    b = rng.choice([2.0, 3.0])
    p1 = rng.randint(3, 6)
    p2 = rng.randint(2, 5)

    prod_coeff = a * b
    tot_p = p1 + p2

    a_str = f"{a:.1f}".replace(".", ",")
    b_str = f"{b:.1f}".replace(".", ",")
    prod_c_str = f"{prod_coeff:.1f}".replace(".", ",")
    ans = f"{prod_c_str} \\times 10^{{{tot_p}}}"

    prompt = (
        f"Calculate and express your answer in scientific notation:\n\n"
        f"\\[ ({a_str} \\times 10^{{{p1}}}) \\times ({b_str} \\times 10^{{{p2}}}) \\]"
    )
    sol = (
        f"**Multiplication in Scientific Notation:**\n"
        f"1. Multiply coefficients: \\({a_str} \\times {b_str} = {prod_c_str}\\).\n"
        f"2. Add powers of 10: \\(10^{{{p1}}} \\times 10^{{{p2}}} = 10^{{{tot_p}}}\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_exp_sci_mul_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Multiply coefficients to get {prod_c_str}", "marks": 1},
            {"desc": f"Add exponents of 10 to get 10^{tot_p}", "marks": 1},
        ],
        "hints": [
            "Multiply the decimal parts together.",
            "Add the powers of 10.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 24. Scientific Notation: Division of Two Numbers
# ----------------------------------------------------------------------
def arch_24_scientific_notation_division_of_two_numbers(rng: random.Random) -> Dict[str, Any]:
    div = rng.choice([2.0, 3.0, 4.0])
    quot = rng.choice([2.0, 3.0, 4.0])
    num = div * quot

    p1 = rng.randint(6, 9)
    p2 = rng.randint(2, 4)
    p_diff = p1 - p2

    num_str = f"{num:.1f}".replace(".", ",")
    div_str = f"{div:.1f}".replace(".", ",")
    quot_str = f"{quot:.1f}".replace(".", ",")
    ans = f"{quot_str} \\times 10^{{{p_diff}}}"

    prompt = (
        f"Calculate the quotient, leaving your answer in scientific notation:\n\n"
        f"\\[ \\frac{{{num_str} \\times 10^{{{p1}}}}}{{{div_str} \\times 10^{{{p2}}}}} \\]"
    )
    sol = (
        f"**Division in Scientific Notation:**\n"
        f"1. Divide coefficients: \\(\\frac{{{num_str}}}{{{div_str}}} = {quot_str}\\).\n"
        f"2. Subtract powers of 10: \\(10^{{{p1} - {p2}}} = 10^{{{p_diff}}}\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_exp_sci_div_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Divide coefficients to get {quot_str}", "marks": 1},
            {"desc": f"Subtract exponents of 10 to get 10^{p_diff}", "marks": 1},
        ],
        "hints": [
            "Divide the leading decimal numbers.",
            "Subtract the bottom power of 10 from the top power of 10.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 25. Scientific Scale: Order of Magnitude Comparison
# ----------------------------------------------------------------------
def arch_25_scientific_scale_order_of_magnitude_comparison(rng: random.Random) -> Dict[str, Any]:
    items = [
        ("Red Blood Cell", "7 × 10^-6 m", -6),
        ("Bacterium", "1 × 10^-6 m", -6),
        ("Dust Mite", "1 × 10^-4 m", -4),
        ("Grain of Sand", "1 × 10^-3 m", -3),
    ]
    svg = draw_scientific_scale_comparison_svg(items, seed=rng.randint(1, 9999))
    ans = "10^3"

    prompt = (
        f"Consider the scientific orders-of-magnitude scale comparison below.\n\n"
        f"How many times larger is the length of a Grain of Sand (\\(10^{{-3}}\\text{{ m}}\\)) "
        f"compared to a Bacterium (\\(10^{{-6}}\\text{{ m}}\\))? Express as a power of 10."
    )
    sol = (
        f"**Order of Magnitude Ratio:**\n"
        f"\\[ \\text{{Ratio}} = \\frac{{10^{{-3}}}}{{10^{{-6}}}} = 10^{{-3 - (-6)}} = 10^3 = 1000 \\text{{ times}} \\]"
    )
    return {
        "id": f"g9_exp_sci_scale_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marks": 2,
        "marking_schema": [
            {"desc": "Divide powers of 10: 10^(-3) / 10^(-6)", "marks": 1},
            {"desc": f"State ratio as power of 10: {ans}", "marks": 1},
        ],
        "hints": [
            "Divide the larger measurement by the smaller measurement.",
            "Subtract exponents: -3 - (-6).",
            f"Ratio is {ans}.",
        ],
    }
