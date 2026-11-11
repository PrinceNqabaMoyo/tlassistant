"""Grade 9 Mathematics - Exponents Archetypes 26 to 50.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 1/03. Exponents.md:
Scientific notation addition/subtraction, prime base factorisation, exponential equations,
reciprocals, roots, algebraic factoring with powers, and multi-step simplification.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .exponents_svg import (
    draw_power_growth_tree_svg,
)


# ----------------------------------------------------------------------
# 26. Scientific Notation: Addition with Same Powers of Ten
# ----------------------------------------------------------------------
def arch_26_scientific_notation_addition_same_powers_of_ten(rng: random.Random) -> Dict[str, Any]:
    a = round(rng.uniform(1.5, 4.5), 1)
    b = round(rng.uniform(1.2, 3.8), 1)
    p = rng.randint(4, 7)
    tot = round(a + b, 1)

    a_str = f"{a:.1f}".replace(".", ",")
    b_str = f"{b:.1f}".replace(".", ",")
    tot_str = f"{tot:.1f}".replace(".", ",")
    ans = f"{tot_str} \\times 10^{{{p}}}"

    prompt = (
        f"Calculate the sum, expressing the final answer in scientific notation:\n\n"
        f"\\[ ({a_str} \\times 10^{{{p}}}) + ({b_str} \\times 10^{{{p}}}) \\]"
    )
    sol = (
        f"**Addition with Matching Exponents:**\n"
        f"Factor out \\(10^{{{p}}}\\):\n"
        f"\\[ ({a_str} + {b_str}) \\times 10^{{{p}}} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_sci_add_same_{rng.randint(100000, 999999)}",
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
            {"desc": f"Add coefficients: {a_str} + {b_str} = {tot_str}", "marks": 1},
            {"desc": f"Retain common power of 10: {ans}", "marks": 1},
        ],
        "hints": [
            "Since both numbers have the same power of 10, simply add the leading decimals.",
            f"Add {a_str} + {b_str}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 27. Scientific Notation: Addition with Different Powers of Ten
# ----------------------------------------------------------------------
def arch_27_scientific_notation_addition_different_powers_of_ten(rng: random.Random) -> Dict[str, Any]:
    # e.g., 2,4 x 10^5 + 3,0 x 10^4 = 2,4 x 10^5 + 0,3 x 10^5 = 2,7 x 10^5
    a = round(rng.choice([2.4, 3.5, 4.2, 5.1]), 1)
    b = round(rng.choice([3.0, 4.0, 6.0]), 1)
    p = rng.randint(4, 6)

    b_scaled = round(b / 10, 2)
    tot = round(a + b_scaled, 2)

    a_str = f"{a:.1f}".replace(".", ",")
    b_str = f"{b:.1f}".replace(".", ",")
    tot_str = f"{tot:.2f}".rstrip("0").rstrip(".").replace(".", ",")
    ans = f"{tot_str} \\times 10^{{{p}}}"

    prompt = (
        f"Calculate the sum and express your answer in scientific notation:\n\n"
        f"\\[ ({a_str} \\times 10^{{{p}}}) + ({b_str} \\times 10^{{{p - 1}}}) \\]"
    )
    sol = (
        f"**Adjusting Powers of Ten:**\n"
        f"Rewrite \\({b_str} \\times 10^{{{p - 1}}}\\) as \\({b_scaled:.2f} \\times 10^{{{p}}}\\).\n"
        f"Add: \\(({a_str} + {b_scaled:.2f}) \\times 10^{{{p}}} = {ans}\\)."
    )
    return {
        "id": f"g9_exp_sci_add_diff_{rng.randint(100000, 999999)}",
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
            {"desc": "Convert smaller power of 10 to match larger exponent", "marks": 1},
            {"desc": f"State final sum in scientific notation: {ans}", "marks": 1},
        ],
        "hints": [
            f"Convert {b_str} * 10^{p-1} to have an exponent of {p}.",
            "Add the decimal parts.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 28. Simplify Exponential Fraction: Combining Product and Quotient
# ----------------------------------------------------------------------
def arch_28_simplify_exponential_fraction_combining_product_quotient(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["a", "x", "p", "m"])
    p1 = rng.randint(2, 5)
    p2 = rng.randint(4, 7)
    p3 = rng.randint(1, 3)
    p4 = rng.randint(1, 3)

    num_tot = p1 + p2
    den_tot = p3 + p4
    net = num_tot - den_tot

    ans = f"{var}^{{{net}}}" if net > 1 else (var if net == 1 else "1")
    prompt = (
        f"Simplify the expression to a single power of \\({var}\\):\n\n"
        f"\\[ \\frac{{{var}^{{{p1}}} \\cdot {var}^{{{p2}}}}}{{{var}^{{{p3}}} \\cdot {var}^{{{p4}}}}} \\]"
    )
    sol = (
        f"**Combining Exponent Laws:**\n"
        f"1. Numerator: \\({var}^{{{p1} + {p2}}} = {var}^{{{num_tot}}}\\).\n"
        f"2. Denominator: \\({var}^{{{p3} + {p4}}} = {var}^{{{den_tot}}}\\).\n"
        f"3. Quotient: \\({var}^{{{num_tot} - {den_tot}}} = {ans}\\)."
    )
    return {
        "id": f"g9_exp_comb_prod_quot_{rng.randint(100000, 999999)}",
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
            {"desc": f"Add exponents in top ({num_tot}) and bottom ({den_tot})", "marks": 1},
            {"desc": f"Subtract to obtain {ans}", "marks": 1},
        ],
        "hints": [
            "Use the product law on top and bottom first.",
            "Then use the quotient law.",
            f"Simplified result: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 29. Simplify Expression: Nested Powers and Negative Indices
# ----------------------------------------------------------------------
def arch_29_simplify_expression_nested_powers_and_negative_indices(rng: random.Random) -> Dict[str, Any]:
    var = rng.choice(["x", "y", "a"])
    p1 = -rng.randint(2, 4)
    p2 = rng.randint(2, 3)
    p3 = rng.choice([2, 3])

    tot = abs(p1 * p2 * p3)
    ans = f"\\frac{{1}}{{{var}^{{{tot}}}}}"

    prompt = (
        f"Simplify the nested power expression, writing the final answer with a positive exponent:\n\n"
        f"\\[ [({var}^{{{p1}}})^{{{p2}}}]^{{{p3}}} \\]"
    )
    sol = (
        f"**Nested Power of a Power:**\n"
        f"Multiply all exponents together:\n"
        f"\\[ ({p1}) \\times ({p2}) \\times ({p3}) = -{tot} \\]\n"
        f"Write with positive exponent: \\({var}^{{-{tot}}} = {ans}\\)."
    )
    return {
        "id": f"g9_exp_nested_powers_{rng.randint(100000, 999999)}",
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
            {"desc": f"Multiply exponents to get -{tot}", "marks": 1},
            {"desc": f"Express with positive exponent {ans}", "marks": 1},
        ],
        "hints": [
            "Multiply all three exponents together.",
            "Apply the reciprocal rule for the negative exponent.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 30. Simplify Compound Fraction: Multi-Variable with Negative Indices
# ----------------------------------------------------------------------
def arch_30_simplify_compound_fraction_multi_variable_with_negative_indices(rng: random.Random) -> Dict[str, Any]:
    # ((2 x^2 y^-3)^3) / (4 x^-1 y^2) = (8 x^6 y^-9) / (4 x^-1 y^2) = 2 x^7 / y^11
    c_pow = 8
    c_den = 4
    net_c = 2
    x_top = 6
    x_bot = -1
    net_x = 7
    y_top = -9
    y_bot = 2
    net_y = 11

    ans = f"\\frac{{{net_c}x^{{{net_x}}}}}{{y^{{{net_y}}}}}"
    prompt = (
        f"Simplify completely and write your answer with positive exponents only:\n\n"
        f"\\[ \\frac{{(2x^2 y^{{-3}})^3}}{{4x^{{-1}} y^2}} \\]"
    )
    sol = (
        f"**Compound Simplification:**\n"
        f"1. Numerator power: \\((2x^2 y^{{-3}})^3 = 8x^6 y^{{-9}}\\).\n"
        f"2. Coefficients: \\(8 \\div 4 = 2\\).\n"
        f"3. \\(x\\) power: \\(x^{{6 - (-1)}} = x^7\\).\n"
        f"4. \\(y\\) power: \\(y^{{-9 - 2}} = y^{{-11}} = \\frac{{1}}{{y^{{11}}}}\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_exp_compound_frac_{rng.randint(100000, 999999)}",
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
        "marks": 3,
        "marking_schema": [
            {"desc": "Expand numerator power correctly: 8x^6 y^-9", "marks": 1},
            {"desc": "Simplify coefficients and variable exponents", "marks": 1},
            {"desc": f"Final answer with positive exponents: {ans}", "marks": 1},
        ],
        "hints": [
            "Apply the power of 3 to the entire numerator first.",
            "Divide matching variables by subtracting exponents.",
            f"Simplified: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 31. Prime Base Factorization: Numerical Expression
# ----------------------------------------------------------------------
def arch_31_prime_base_factorization_numerical_expression(rng: random.Random) -> Dict[str, Any]:
    # e.g., (2^5 * 4^2) / (8^2) = (2^5 * 2^4) / 2^6 = 2^9 / 2^6 = 2^3 = 8
    p1 = 5
    p2 = 2  # 4^2 = 2^4
    p3 = 2  # 8^2 = 2^6
    tot_num = 5 + 4  # 9
    tot_den = 6
    net_p = 3
    ans = 8

    prompt = (
        f"Simplify by first expressing all numbers in terms of their prime base \\(2\\):\n\n"
        f"\\[ \\frac{{2^5 \\times 4^2}}{{8^2}} \\]"
    )
    sol = (
        f"**Prime Factorisation (Base 2):**\n"
        f"\\(4 = 2^2 \\implies 4^2 = (2^2)^2 = 2^4\\).\n"
        f"\\(8 = 2^3 \\implies 8^2 = (2^3)^2 = 2^6\\).\n"
        f"Expression: \\(\\frac{{2^5 \\times 2^4}}{{2^6}} = \\frac{{2^9}}{{2^6}} = 2^3 = {ans}\\)."
    )
    return {
        "id": f"g9_exp_prime_base_num_{rng.randint(100000, 999999)}",
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
        "marks": 3,
        "marking_schema": [
            {"desc": "Convert 4 and 8 into powers of 2", "marks": 1},
            {"desc": "Apply exponent laws to combine powers", "marks": 1},
            {"desc": f"State evaluated integer {ans}", "marks": 1},
        ],
        "hints": [
            "Replace 4 with 2^2 and 8 with 2^3.",
            "Use the product law on top and quotient law to simplify.",
            f"Final evaluated answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 32. Prime Base Factorization: Mixed Bases 2, 3, 5
# ----------------------------------------------------------------------
def arch_32_prime_base_factorization_mixed_bases_2_3_5(rng: random.Random) -> Dict[str, Any]:
    # e.g., (6^2 * 10^3) / (15^2 * 2^5) = (2^2 * 3^2 * 2^3 * 5^3) / (3^2 * 5^2 * 2^5)
    # 2: 2^5 / 2^5 = 1
    # 3: 3^2 / 3^2 = 1
    # 5: 5^3 / 5^2 = 5
    ans = 5
    prompt = (
        f"Simplify the numerical expression by decomposing all composite bases into prime factors:\n\n"
        f"\\[ \\frac{{6^2 \\times 10^3}}{{15^2 \\times 2^5}} \\]"
    )
    sol = (
        f"**Prime Factor Decomposition:**\n"
        f"\\(6 = 2 \\times 3 \\implies 6^2 = 2^2 \\times 3^2\\).\n"
        f"\\(10 = 2 \\times 5 \\implies 10^3 = 2^3 \\times 5^3\\).\n"
        f"\\(15 = 3 \\times 5 \\implies 15^2 = 3^2 \\times 5^2\\).\n\n"
        f"Substitute:\n"
        f"\\[ \\frac{{(2^2 \\times 3^2) \\times (2^3 \\times 5^3)}}{{(3^2 \\times 5^2) \\times 2^5}} = \\frac{{2^5 \\times 3^2 \\times 5^3}}{{2^5 \\times 3^2 \\times 5^2}} = 5^1 = {ans} \\]"
    )
    return {
        "id": f"g9_exp_prime_mixed_{rng.randint(100000, 999999)}",
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
        "marks": 3,
        "marking_schema": [
            {"desc": "Decompose 6, 10, 15 into prime bases (2, 3, 5)", "marks": 1},
            {"desc": "Group powers for base 2, base 3, base 5", "marks": 1},
            {"desc": f"Evaluate final integer {ans}", "marks": 1},
        ],
        "hints": [
            "6 = 2 * 3, 10 = 2 * 5, 15 = 3 * 5.",
            "Group and cancel like prime bases.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 33. Exponential Growth Branching Problem
# ----------------------------------------------------------------------
def arch_33_exponential_growth_branching_problem(rng: random.Random) -> Dict[str, Any]:
    base = 2
    levels = 3
    svg = draw_power_growth_tree_svg(base=base, levels=levels, seed=rng.randint(1, 9999))
    target_stage = rng.choice([5, 6, 7])
    ans = base ** target_stage

    prompt = (
        f"Consider the binary branching model illustrated below, where each node divides into \\(2\\) branches at each subsequent stage.\n\n"
        f"Using exponential notation, calculate the total number of individuals produced at **Stage {target_stage}**."
    )
    sol = (
        f"**Exponential Growth Formula:**\n"
        f"At stage \\(n\\), population \\(P = 2^n\\).\n"
        f"At stage {target_stage}:\n"
        f"\\[ P = 2^{{{target_stage}}} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_growth_tree_{rng.randint(100000, 999999)}",
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
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marks": 2,
        "marking_schema": [
            {"desc": f"State exponential formula 2^{target_stage}", "marks": 1},
            {"desc": f"Calculate evaluated value {ans}", "marks": 1},
        ],
        "hints": [
            "Each stage doubles the previous amount.",
            f"Calculate 2^{target_stage}.",
            f"Total nodes: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 34. Exponential Equation: Simple Monomial Equating Bases
# ----------------------------------------------------------------------
def arch_34_exponential_equation_simple_monomial_equating_bases(rng: random.Random) -> Dict[str, Any]:
    b = 2
    x_val = rng.randint(3, 7)
    val = b ** x_val

    prompt = (
        f"Solve for \\(x\\):\n\n"
        f"\\[ 2^x = {val} \\]"
    )
    sol = (
        f"**Equating Bases Rule (if \\(a^x = a^y\\) then \\(x = y\\)):**\n"
        f"Express \\({val}\\) as a power of 2: \\({val} = 2^{{{x_val}}}\\).\n"
        f"Therefore: \\(2^x = 2^{{{x_val}}} \\implies x = {x_val}\\)."
    )
    return {
        "id": f"g9_exp_eq_simple_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(x_val),
        "expected_answer": str(x_val),
        "sample_answer": str(x_val),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Rewrite {val} as 2^{x_val}", "marks": 1},
            {"desc": f"Equate exponents to yield x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Write {val} as 2 to some power.",
            "Once bases are identical, equate the powers.",
            f"Solution: x = {x_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 35. Exponential Equation: Base 3 and Base 5
# ----------------------------------------------------------------------
def arch_35_exponential_equation_base_3_and_base_5(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([3, 5])
    x_val = rng.randint(2, 4)
    val = base ** x_val

    prompt = (
        f"Solve for \\(x\\):\n\n"
        f"\\[ {base}^x = {val} \\]"
    )
    sol = (
        f"**Equating Bases:**\n"
        f"\\({val} = {base}^{{{x_val}}}\\).\n"
        f"\\({base}^x = {base}^{{{x_val}}} \\implies x = {x_val}\\)."
    )
    return {
        "id": f"g9_exp_eq_b35_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(x_val),
        "expected_answer": str(x_val),
        "sample_answer": str(x_val),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Express {val} as {base}^{x_val}", "marks": 1},
            {"desc": f"State x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Express {val} with base {base}.",
            f"x = {x_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 36. Exponential Equation: Fractional Value Negative Solution
# ----------------------------------------------------------------------
def arch_36_exponential_equation_fractional_value_negative_solution(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5])
    exp_pos = rng.randint(2, 4)
    denom = base ** exp_pos
    ans = -exp_pos

    prompt = (
        f"Solve for \\(x\\):\n\n"
        f"\\[ {base}^x = \\frac{{1}}{{{denom}}} \\]"
    )
    sol = (
        f"**Negative Exponent Conversion:**\n"
        f"\\(\\frac{{1}}{{{denom}}} = \\frac{{1}}{{{base}^{{{exp_pos}}}}} = {base}^{{-{exp_pos}}}\\).\n"
        f"\\({base}^x = {base}^{{-{exp_pos}}} \\implies x = {ans}\\)."
    )
    return {
        "id": f"g9_exp_eq_frac_val_{rng.randint(100000, 999999)}",
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
            {"desc": f"Rewrite 1/{denom} as {base}^(-{exp_pos})", "marks": 1},
            {"desc": f"Equate exponents to yield x = {ans}", "marks": 1},
        ],
        "hints": [
            "Use negative exponents to express fractions with power form.",
            f"1/{denom} = {base}^(-{exp_pos}).",
            f"Answer: x = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 37. Exponential Equation: Fractional Base
# ----------------------------------------------------------------------
def arch_37_exponential_equation_fractional_base(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 5])
    p = rng.randint(2, 4)
    val = b ** p
    ans = -p

    prompt = (
        f"Solve for \\(x\\):\n\n"
        f"\\[ \\left(\\frac{{1}}{{{b}}}\\right)^x = {val} \\]"
    )
    sol = (
        f"**Fractional Base Inversion:**\n"
        f"\\(\\left(\\frac{{1}}{{{b}}}\\right)^x = (b^{{-1}})^x = {b}^{{-x}}\\).\n"
        f"\\({val} = {b}^{{{p}}}\\).\n"
        f"\\({b}^{{-x}} = {b}^{{{p}}} \\implies -x = {p} \\implies x = {ans}\\)."
    )
    return {
        "id": f"g9_exp_eq_frac_base_{rng.randint(100000, 999999)}",
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
            {"desc": f"Express (1/{b})^x as {b}^(-x)", "marks": 1},
            {"desc": f"Solve -x = {p} to get x = {ans}", "marks": 1},
        ],
        "hints": [
            f"(1/{b})^x = {b}^(-x).",
            f"Express {val} as {b}^{p}.",
            f"Answer: x = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 38. Exponential Equation: Linear Expression in Exponent
# ----------------------------------------------------------------------
def arch_38_exponential_equation_linear_expression_in_exponent(rng: random.Random) -> Dict[str, Any]:
    base = 2
    offset = rng.randint(1, 4)
    tot_p = rng.randint(4, 7)
    val = base ** tot_p
    ans = tot_p - offset

    prompt = (
        f"Solve for \\(x\\):\n\n"
        f"\\[ 2^{{x + {offset}}} = {val} \\]"
    )
    sol = (
        f"**Linear Exponent Equation:**\n"
        f"1. Express \\({val}\\) with base 2: \\({val} = 2^{{{tot_p}}}\\).\n"
        f"2. Equate exponents: \\(x + {offset} = {tot_p}\\).\n"
        f"3. Solve: \\(x = {tot_p} - {offset} = {ans}\\)."
    )
    return {
        "id": f"g9_exp_eq_lin_exp_{rng.randint(100000, 999999)}",
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
            {"desc": f"Equate powers: x + {offset} = {tot_p}", "marks": 1},
            {"desc": f"Solve for x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Write {val} as 2^{tot_p}.",
            f"Set the exponent x + {offset} equal to {tot_p}.",
            f"Solution: x = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 39. Exponential Equation: Linear Expression with Multiplier
# ----------------------------------------------------------------------
def arch_39_exponential_equation_linear_expression_both_sides(rng: random.Random) -> Dict[str, Any]:
    # 3^(2x - 1) = 27 -> 2x - 1 = 3 -> 2x = 4 -> x = 2
    # 3^(2x - 1) = 81 -> 2x - 1 = 4 -> not clean; let's ensure clean int:
    cases = [
        (3, 2, -1, 27, 3, 2),  # 3^(2x-1) = 27 => 2x-1=3 => x=2
        (2, 3, -1, 32, 5, 2),  # 2^(3x-1) = 32 => 3x-1=5 => x=2
        (5, 2, 1, 125, 3, 1),  # 5^(2x+1) = 125 => 2x+1=3 => x=1
        (2, 2, 2, 64, 6, 2),   # 2^(2x+2) = 64 => 2x+2=6 => x=2
    ]
    base, m_coeff, offset, rhs, rhs_pow, ans = rng.choice(cases)
    sign = "+" if offset > 0 else "-"
    abs_off = abs(offset)

    prompt = (
        f"Solve for \\(x\\):\n\n"
        f"\\[ {base}^{{{m_coeff}x {sign} {abs_off}}} = {rhs} \\]"
    )
    sol = (
        f"**Equating Exponents:**\n"
        f"\\({rhs} = {base}^{{{rhs_pow}}}\\).\n"
        f"\\({m_coeff}x {sign} {abs_off} = {rhs_pow}\\)\n"
        f"\\({m_coeff}x = {rhs_pow - offset} \\implies x = {ans}\\)."
    )
    return {
        "id": f"g9_exp_eq_lin_mult_{rng.randint(100000, 999999)}",
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
        "marks": 3,
        "marking_schema": [
            {"desc": f"Express {rhs} as {base}^{rhs_pow}", "marks": 1},
            {"desc": f"Form linear equation {m_coeff}x {sign} {abs_off} = {rhs_pow}", "marks": 1},
            {"desc": f"Solve for x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Rewrite {rhs} in base {base}.",
            "Equate the exponents and solve the linear equation.",
            f"Answer: x = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 40. Exponential Equation: Composite Base Reduction
# ----------------------------------------------------------------------
def arch_40_exponential_equation_composite_base_reduction(rng: random.Random) -> Dict[str, Any]:
    # 4^(x - 1) = 64 -> (2^2)^(x-1) = 2^6 -> 2x - 2 = 6 -> 2x = 8 -> x = 4
    # Or 4^(x-1) = 4^3 => x-1=3 => x=4
    # Let's do 4^(x+1) = 32 -> (2^2)^(x+1) = 2^5 -> 2x+2 = 5 (fractional)
    # 4^(x-1) = 32 -> 2^(2x-2) = 2^5 -> 2x-2=5 (fractional)
    # Clean integer: 4^(2x - 1) = 64 => (4)^3 => 2x-1=3 => x=2
    cases = [
        (4, "2x - 1", 64, 4, 3, 2),  # 4^(2x-1) = 64 -> 2x-1=3 -> x=2
        (9, "x + 1", 81, 9, 2, 1),   # 9^(x+1) = 81 -> x+1=2 -> x=1
        (8, "x - 1", 64, 8, 2, 3),   # 8^(x-1) = 64 -> x-1=2 -> x=3
    ]
    base, exp_expr, rhs, c_base, pwr, ans = rng.choice(cases)

    prompt = (
        f"Solve for \\(x\\):\n\n"
        f"\\[ {base}^{{{exp_expr}}} = {rhs} \\]"
    )
    sol = (
        f"**Equating Bases:**\n"
        f"\\({rhs} = {base}^{{{pwr}}}\\).\n"
        f"\\({exp_expr} = {pwr}\\).\n"
        f"Solving for \\(x\\) gives \\(x = {ans}\\)."
    )
    return {
        "id": f"g9_exp_eq_comp_base_{rng.randint(100000, 999999)}",
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
            {"desc": f"Express {rhs} as {base}^{pwr}", "marks": 1},
            {"desc": f"Solve equation for x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Write {rhs} with base {base}.",
            "Equate exponents and solve for x.",
            f"Solution: x = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 41. Exponential Equation: Coefficient Division First
# ----------------------------------------------------------------------
def arch_41_exponential_equation_coefficient_division_first(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([3, 5, 7])
    b = 2
    x_val = rng.randint(3, 5)
    pow_val = b ** x_val
    rhs = c * pow_val

    prompt = (
        f"Solve for \\(x\\) by isolating the exponential term first:\n\n"
        f"\\[ {c} \\cdot 2^x = {rhs} \\]"
    )
    sol = (
        f"**Isolating Exponential Power:**\n"
        f"1. Divide both sides by {c}: \\(2^x = \\frac{{{rhs}}}{{{c}}} = {pow_val}\\).\n"
        f"2. Equate bases: \\(2^x = 2^{{{x_val}}} \\implies x = {x_val}\\)."
    )
    return {
        "id": f"g9_exp_eq_coeff_first_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(x_val),
        "expected_answer": str(x_val),
        "sample_answer": str(x_val),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Divide by {c} to isolate 2^x = {pow_val}", "marks": 1},
            {"desc": f"Solve for x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"First divide both sides by {c}.",
            f"Then write {pow_val} as 2^x.",
            f"Result: x = {x_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 42. Exponential Equation: Equating Exponent to Zero
# ----------------------------------------------------------------------
def arch_42_exponential_equation_equating_exponent_to_zero(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([5, 7, 11])
    ans = rng.randint(2, 6)
    mult = 2
    const = mult * ans

    prompt = (
        f"Solve for \\(x\\):\n\n"
        f"\\[ {base}^{{{mult}x - {const}}} = 1 \\]"
    )
    sol = (
        f"**Zero Exponent Identity (\\(a^0 = 1\\)):**\n"
        f"Write \\(1\\) as \\({base}^0\\):\n"
        f"\\[ {base}^{{{mult}x - {const}}} = {base}^0 \\]\n"
        f"Equate exponents: \\({mult}x - {const} = 0 \\implies {mult}x = {const} \\implies x = {ans}\\)."
    )
    return {
        "id": f"g9_exp_eq_zero_rhs_{rng.randint(100000, 999999)}",
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
            {"desc": f"Rewrite 1 as {base}^0", "marks": 1},
            {"desc": f"Solve {mult}x - {const} = 0 to get x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Any base to the power of 0 equals 1: 1 = {base}^0.",
            f"Set the exponent {mult}x - {const} equal to 0.",
            f"Solution: x = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 43. Exponential Equation: Negative Base and Sign
# ----------------------------------------------------------------------
def arch_43_exponential_equation_negative_base_and_sign(rng: random.Random) -> Dict[str, Any]:
    ans = rng.choice([3, 5])
    rhs = (-2) ** ans

    prompt = (
        f"Solve for \\(x\\):\n\n"
        f"\\[ (-2)^x = {rhs} \\]"
    )
    sol = (
        f"**Negative Base Equating:**\n"
        f"\\({rhs} = (-2)^{{{ans}}}\\).\n"
        f"Therefore: \\((-2)^x = (-2)^{{{ans}}} \\implies x = {ans}\\)."
    )
    return {
        "id": f"g9_exp_eq_neg_base_{rng.randint(100000, 999999)}",
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
            {"desc": f"Express {rhs} as (-2)^{ans}", "marks": 1},
            {"desc": f"State x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Express {rhs} as a power of -2.",
            f"x = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 44. Exponential Equation: Distinguishing Root vs Exponential Form
# ----------------------------------------------------------------------
def arch_44_exponential_equation_root_form(rng: random.Random) -> Dict[str, Any]:
    # Compare solving: x^3 = 64 (power equation -> take root) vs 3^x = 81 (exponential equation)
    ans1 = 4
    ans2 = 4

    prompt = (
        f"Solve both equations for \\(x\\), explaining the different method applied to each:\n\n"
        f"1. \\(x^3 = 64\\)\n"
        f"2. \\(3^x = 81\\)"
    )
    sol = (
        f"**Power vs Exponential Equations:**\n"
        f"1. Variable is in the BASE: \\(x^3 = 64 \\implies x = \\sqrt[3]{{64}} = {ans1}\\).\n"
        f"2. Variable is in the EXPONENT: \\(3^x = 81 \\implies 3^x = 3^4 \\implies x = {ans2}\\)."
    )
    return {
        "id": f"g9_exp_eq_root_vs_exp_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"1) x = {ans1}; 2) x = {ans2}",
        "expected_answer": f"1) x = {ans1}; 2) x = {ans2}",
        "sample_answer": f"1) x = {ans1}; 2) x = {ans2}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Solve base equation x = cbrt(64) = {ans1}", "marks": 1},
            {"desc": f"Solve exponential equation 3^x = 3^4 => x = {ans2}", "marks": 1},
        ],
        "hints": [
            "For x^3 = 64, take the cube root.",
            "For 3^x = 81, equate bases.",
            f"Solutions: x = {ans1} and x = {ans2}.",
        ],
    }


# ----------------------------------------------------------------------
# 45. Exponential Equation: Reciprocal Fractional Linear
# ----------------------------------------------------------------------
def arch_45_exponential_equation_reciprocal_fractional_linear(rng: random.Random) -> Dict[str, Any]:
    # 5^(2x + 1) = 1/125 -> 2x+1 = -3 -> 2x = -4 -> x = -2
    ans = -2
    prompt = (
        f"Solve for \\(x\\):\n\n"
        f"\\[ 5^{{2x + 1}} = \\frac{{1}}{{125}} \\]"
    )
    sol = (
        f"**Reciprocal Base:**\n"
        f"\\(\\frac{{1}}{{125}} = \\frac{{1}}{{5^3}} = 5^{{-3}}\\).\n"
        f"\\(5^{{2x + 1}} = 5^{{-3}} \\implies 2x + 1 = -3 \\implies 2x = -4 \\implies x = {ans}\\)."
    )
    return {
        "id": f"g9_exp_eq_recip_lin_{rng.randint(100000, 999999)}",
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
            {"desc": "Express 1/125 as 5^-3", "marks": 1},
            {"desc": f"Solve 2x + 1 = -3 to get x = {ans}", "marks": 1},
        ],
        "hints": [
            "Rewrite 1/125 as 5^-3.",
            "Set 2x + 1 = -3.",
            f"Solution: x = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 46. Compound Algebraic Fraction: Factorisation of Terms
# ----------------------------------------------------------------------
def arch_46_compound_algebraic_fraction_factorisation_terms(rng: random.Random) -> Dict[str, Any]:
    # e.g., (2^(x+2) - 2^x) / 2^x = (2^x * (2^2 - 1)) / 2^x = 4 - 1 = 3
    # Or with 3: (3^(x+1) + 3^x) / 3^x = (3^x * (3 + 1)) / 3^x = 4
    cases = [
        (2, 2, "-", 3, "2^2 - 1 = 4 - 1 = 3"),
        (3, 1, "+", 4, "3^1 + 1 = 3 + 1 = 4"),
        (2, 3, "-", 7, "2^3 - 1 = 8 - 1 = 7"),
        (5, 1, "+", 6, "5^1 + 1 = 5 + 1 = 6"),
    ]
    b, p, op, ans, sol_step = rng.choice(cases)

    prompt = (
        f"Simplify the algebraic fraction by taking out the common factor \\({b}^x\\):\n\n"
        f"\\[ \\frac{{{b}^{{x + {p}}} {op} {b}^x}}{{{b}^x}} \\]"
    )
    sol = (
        f"**Factorising Common Power:**\n"
        f"1. Factor out \\({b}^x\\) in the numerator:\n"
        f"\\[ \\frac{{{b}^x ({b}^{{{p}}} {op} 1)}}{{{b}^x}} \\]\n"
        f"2. Cancel \\({b}^x\\):\n"
        f"\\[ = {b}^{{{p}}} {op} 1 = {sol_step} = {ans} \\]"
    )
    return {
        "id": f"g9_exp_factor_common_{rng.randint(100000, 999999)}",
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
        "marks": 3,
        "marking_schema": [
            {"desc": f"Factor out common factor {b}^x", "marks": 1},
            {"desc": f"Cancel {b}^x from numerator and denominator", "marks": 1},
            {"desc": f"Evaluate numerical remainder {ans}", "marks": 1},
        ],
        "hints": [
            f"Take out {b}^x as a common factor in the numerator.",
            f"Cancel {b}^x.",
            f"Final integer value: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 47. Error Analysis: Diagnosing Product Law Base Multiplication
# ----------------------------------------------------------------------
def arch_47_error_analysis_diagnosing_product_law_base_multiplication(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3])
    p1 = rng.randint(2, 4)
    p2 = rng.randint(2, 4)
    correct_p = p1 + p2
    flawed_b = b * b

    prompt = (
        f"A learner solved the following problem:\n\n"
        f"\\[ {b}^{{{p1}}} \\times {b}^{{{p2}}} = {flawed_b}^{{{correct_p}}} \\]\n\n"
        f"Identify the conceptual misunderstanding and provide the correct simplified answer in power form."
    )
    ans = f"{b}^{{{correct_p}}}"
    sol = (
        f"**Error Analysis:**\n"
        f"1. Error: The learner multiplied the bases \\({b} \\times {b} = {flawed_b}\\). "
        f"Under the product law, the base remains unchanged.\n"
        f"2. Correct evaluation: \\({b}^{{{p1}}} \\times {b}^{{{p2}}} = {b}^{{{p1} + {p2}}} = {ans}\\)."
    )
    return {
        "id": f"g9_exp_err_prod_base_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Do not multiply bases; Correct: {ans}",
        "expected_answer": f"Do not multiply bases; Correct: {ans}",
        "sample_answer": f"Do not multiply bases; Correct: {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify incorrect base multiplication", "marks": 1},
            {"desc": f"Provide correct power {ans}", "marks": 1},
        ],
        "hints": [
            "In a^m * a^n = a^(m+n), the base does not change.",
            f"Keep base {b} and add exponents.",
            f"Correct: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 48. Error Analysis: Diagnosing Power of Power Addition
# ----------------------------------------------------------------------
def arch_48_error_analysis_diagnosing_power_of_power_addition(rng: random.Random) -> Dict[str, Any]:
    var = "x"
    p1 = rng.randint(2, 4)
    p2 = rng.randint(3, 5)
    flawed_p = p1 + p2
    correct_p = p1 * p2

    prompt = (
        f"A learner simplified \\(({var}^{{{p1}}})^{{{p2}}}\\) as \\({var}^{{{flawed_p}}}\\).\n\n"
        f"Explain why this answer is incorrect and state the correct expression."
    )
    ans = f"{var}^{{{correct_p}}}"
    sol = (
        f"**Error Analysis:**\n"
        f"1. Error: The learner added exponents \\({p1} + {p2} = {flawed_p}\\) instead of multiplying them.\n"
        f"2. Correct: \\(({var}^{{{p1}}})^{{{p2}}} = {var}^{{{p1} \\times {p2}}} = {ans}\\)."
    )
    return {
        "id": f"g9_exp_err_pow_pow_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Exponents must be multiplied, not added; Correct: {ans}",
        "expected_answer": f"Exponents must be multiplied, not added; Correct: {ans}",
        "sample_answer": f"Exponents must be multiplied, not added; Correct: {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Explain that exponents must be multiplied", "marks": 1},
            {"desc": f"State correct power {ans}", "marks": 1},
        ],
        "hints": [
            "Raising a power to a power requires multiplication of indices.",
            f"Multiply {p1} * {p2}.",
            f"Correct: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 49. Error Analysis: Diagnosing Negative Sign Outside Brackets
# ----------------------------------------------------------------------
def arch_49_error_analysis_diagnosing_negative_sign_outside_brackets(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([3, 4, 5, 6])
    val = base ** 2

    prompt = (
        f"A learner claimed that \\(-{base}^2 = {val}\\).\n\n"
        f"Explain the learner's misconception and state the correct evaluated value."
    )
    ans = str(-val)
    sol = (
        f"**Misconception Analysis:**\n"
        f"1. Misconception: The learner treated \\(-{base}^2\\) as \\((- {base})^2\\).\n"
        f"2. Correct Rule: Without brackets, exponentiation takes precedence over negation (BODMAS):\n"
        f"\\[ -{base}^2 = -({base}^2) = -({val}) = {ans} \\]"
    )
    return {
        "id": f"g9_exp_err_neg_sign_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Without brackets negation occurs after power; Correct: {ans}",
        "expected_answer": f"Without brackets negation occurs after power; Correct: {ans}",
        "sample_answer": f"Without brackets negation occurs after power; Correct: {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Explain that power applies only to base without brackets", "marks": 1},
            {"desc": f"State correct value {ans}", "marks": 1},
        ],
        "hints": [
            "Powers come before negation in BODMAS.",
            f"-{base}^2 = -({val}).",
            f"Correct: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 50. Compound Multi-Step Exponential Simplification Challenge
# ----------------------------------------------------------------------
def arch_50_compound_multi_step_exponential_simplification_challenge(rng: random.Random) -> Dict[str, Any]:
    # e.g., (3 a^2 b^-1)^2 * (2 a^-1 b^3) / (6 a^2 b)
    # Num: (9 a^4 b^-2) * (2 a^-1 b^3) = 18 a^3 b^1
    # Den: 6 a^2 b^1
    # Quot: 3 a^1 = 3a
    ans = "3a"

    prompt = (
        f"Simplify the multi-step algebraic expression completely:\n\n"
        f"\\[ \\frac{{(3a^2 b^{{-1}})^2 \\cdot (2a^{{-1}} b^3)}}{{6a^2 b}} \\]"
    )
    sol = (
        f"**Comprehensive Simplification:**\n"
        f"1. Expand power: \\((3a^2 b^{{-1}})^2 = 9a^4 b^{{-2}}\\).\n"
        f"2. Multiply numerator: \\((9a^4 b^{{-2}})(2a^{{-1}} b^3) = 18a^3 b^1\\).\n"
        f"3. Divide by denominator: \\(\\frac{{18a^3 b}}{{6a^2 b}} = 3a\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_exp_compound_challenge_{rng.randint(100000, 999999)}",
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
        "marks": 3,
        "marking_schema": [
            {"desc": "Expand numerator power correctly: 9a^4 b^-2", "marks": 1},
            {"desc": "Multiply numerator terms: 18a^3 b", "marks": 1},
            {"desc": f"Divide by denominator to get {ans}", "marks": 1},
        ],
        "hints": [
            "Work from inside out: expand power of product first.",
            "Multiply numerator terms together.",
            f"Final simplified form: {ans}.",
        ],
    }
