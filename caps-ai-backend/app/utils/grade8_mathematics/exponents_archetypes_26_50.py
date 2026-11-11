"""
Grade 8 Mathematics - Exponents Generator (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/03. Exponents.md.
"""
from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 3 (Cont.): Law 5 & Nested Laws (26 - 28)
# ==============================================================================

def arch_26_power_of_a_quotient_with_coefficients(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.choice([2, 3])
    c2 = rng.choice([4, 5]) if c1 != 4 else 5
    while math.gcd(c1, c2) != 1:
        c2 += 1
    exp_a = rng.randint(2, 3)
    exp_b = rng.randint(2, 3)
    k = 2
    c1_sq = c1 ** k
    c2_sq = c2 ** k
    a_pow = exp_a * k
    b_pow = exp_b * k
    ans = f"({c1_sq}a^{a_pow})/({c2_sq}b^{b_pow})"

    prompt = (
        f"Simplify the expression by raising the entire quotient to the power:\n\n"
        f"$$\\left(\\frac{{{c1}a^{{{exp_a}}}}}{{{c2}b^{{{exp_b}}}}}\\right)^{{{k}}}$$"
    )
    sol = (
        f"**Step 1:** Raise the numerator to power {k}: $({c1}a^{{{exp_a}}})^{{{k}}} = {c1_sq}a^{{{a_pow}}}$ [1 Mark].\n\n"
        f"**Step 2:** Raise the denominator to power {k}: $({c2}b^{{{exp_b}}})^{{{k}}} = {c2_sq}b^{{{b_pow}}}$ [1 Mark].\n\n"
        f"$$\\therefore \\frac{{{c1_sq}a^{{{a_pow}}}}}{{{c2_sq}b^{{{b_pow}}}}}$$"
    )
    return {
        "id": f"g8_exp_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "26_power_of_a_quotient_with_coefficients",
        "hints": {
            "tier_1": f"Square the top and square the bottom: {c1}² = {c1_sq} and {c2}² = {c2_sq}.",
            "tier_2": f"Multiply variable exponents by {k}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["fraction_power_coefficient_squaring_omitted"]
    }


def arch_27_nested_powers_and_products(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 3)
    b = rng.randint(2, 3)
    c = 2
    tot = a * b * c
    ans = f"x^{tot}"

    prompt = (
        f"Simplify the nested power expression to a single power of $x$:\n\n"
        f"$$\\left[(x^{{{a}}})^{{{b}}}\\right]^{{{c}}}$$"
    )
    sol = (
        f"**Step 1:** Multiply all exponents successively:\n"
        f"$$\\left[(x^{{{a}}})^{{{b}}}\\right]^{{{c}}} = x^{{{a} \\times {b} \\times {c}}} = x^{{{tot}}}$$ [2 Marks]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "27_nested_powers_and_products",
        "hints": {
            "tier_1": "Multiply all nested powers together.",
            "tier_2": f"{a} × {b} × {c} = {tot}.",
            "tier_3": f"x^{tot}."
        },
        "misconception_tags": ["nested_power_multiplication_slip"]
    }


def arch_28_combined_laws_expansion(rng: random.Random) -> Dict[str, Any]:
    c = 2
    k = 3
    c_pow = c ** k  # 8
    e_x = 2
    e_top = e_x * k  # 6
    e_add = 4
    num_tot = e_top + e_add  # 10
    d = 4
    e_den = 5
    c_final = c_pow // d  # 2
    ans_exp = num_tot - e_den  # 5
    ans = f"{c_final}x^{ans_exp}"

    prompt = (
        f"Simplify the complex algebraic fraction by applying exponent laws step-by-step:\n\n"
        f"$$\\frac{{({c}x^{{{e_x}}})^{{{k}}} \\cdot x^{{{e_add}}}}}{{{d}x^{{{e_den}}}}}$$"
    )
    sol = (
        f"**Step 1:** Expand the bracket in the numerator: $({c}x^{{{e_x}}})^{{{k}}} = {c_pow}x^{{{e_top}}}$ [1 Mark].\n\n"
        f"**Step 2:** Combine numerator terms: ${c_pow}x^{{{e_top}}} \\cdot x^{{{e_add}}} = {c_pow}x^{{{num_tot}}}$ [1 Mark].\n\n"
        f"**Step 3:** Divide by denominator: $\\frac{{{c_pow}x^{{{num_tot}}}}}{{{d}x^{{{e_den}}}}} = {c_final}x^{{{ans_exp}}}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "28_combined_laws_expansion",
        "hints": {
            "tier_1": "Expand the bracket power first.",
            "tier_2": f"({c}x^{e_x})^{k} = {c_pow}x^{e_top}.",
            "tier_3": f"Numerator is {c_pow}x^{num_tot}. Final result is {ans}."
        },
        "misconception_tags": ["combined_laws_bracket_expansion_error"]
    }


# ==============================================================================
# CLUSTER 4: Negative Bases & Sign Rules (29 - 36)
# ==============================================================================

def arch_29_negative_base_even_power(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5])
    exp = rng.choice([2, 4])
    ans = base ** exp

    prompt = (
        f"Evaluate the power with a negative base:\n\n"
        f"$$(-{base})^{{{exp}}}$$\n\n"
        f"Explain why an even power of a negative number is always positive."
    )
    sol = (
        f"**Step 1:** The base is inside brackets, so the negative sign is raised to the power: $(-{base})^{{{exp}}}$ [1 Mark].\n\n"
        f"**Step 2:** Because the exponent {exp} is even, negative signs pair up to form positive products: $(-1)^{{{exp}}} = +1$.\n"
        f"$$(-{base})^{{{exp}}} = +{ans}$$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "29_negative_base_even_power",
        "hints": {
            "tier_1": "An even power of a negative number produces a positive answer.",
            "tier_2": f"Calculate {base}^{exp}.",
            "tier_3": f"(-{base})^{exp} = {ans}."
        },
        "misconception_tags": ["negative_base_even_power_negative_slip"]
    }


def arch_30_negative_base_odd_power(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5])
    exp = rng.choice([3, 5])
    ans = -(base ** exp)

    prompt = (
        f"Calculate the value of:\n\n"
        f"$$(-{base})^{{{exp}}}$$\n\n"
        f"State the sign rule for odd powers of negative numbers."
    )
    sol = (
        f"**Step 1:** An odd power of a negative base is always negative: $(-1)^{{{exp}}} = -1$ [1 Mark: Rule].\n\n"
        f"**Step 2:** Calculate: $$-({base}^{{{exp}}}) = {ans}$$ [1 Mark: Calculation].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "30_negative_base_odd_power",
        "hints": {
            "tier_1": "An odd number of negative factors leaves one negative unpaired.",
            "tier_2": f"The answer is negative: -({base}^{exp}).",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["negative_base_odd_power_positive_error"]
    }


def arch_31_unbracketed_negative_base_even_power(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5])
    exp = rng.choice([2, 4])
    ans = -(base ** exp)

    prompt = (
        f"Evaluate the expression:\n\n"
        f"$$-{base}^{{{exp}}}$$\n\n"
        f"Explain why the answer is negative even though the exponent is even."
    )
    sol = (
        f"**Step 1:** Without brackets, the exponent {exp} applies only to the base {base}, not to the preceding minus sign [1 Mark].\n\n"
        f"**Step 2:** Calculate: $$-({base}^{{{exp}}}) = -({base ** exp}) = {ans}$$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "31_unbracketed_negative_base_even_power",
        "hints": {
            "tier_1": "The negative sign is outside the power operation.",
            "tier_2": f"-{base}^{exp} means -({base}^{exp}).",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["unbracketed_power_sign_misapplication"]
    }


def arch_32_comparing_bracketed_and_unbracketed_powers(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([3, 4, 6])
    p1 = base ** 2
    p2 = -(base ** 2)

    prompt = (
        f"Compare the values of the two expressions:\n\n"
        f"$$\\text{{A}} = (-{base})^2 \\quad \\text{{and}} \\quad \\text{{B}} = -{base}^2$$\n\n"
        f"1. Calculate the value of expression A.\n"
        f"2. Calculate the value of expression B.\n"
        f"3. State whether A and B are equal or unequal."
    )
    sol = (
        f"**Step 1:** $\\text{{A}} = (-{base})^2 = +{p1}$ [1 Mark].\n\n"
        f"**Step 2:** $\\text{{B}} = -{base}^2 = -({p1}) = {p2}$ [1 Mark].\n\n"
        f"**Step 3:** $\\text{{A}} \\neq \\text{{B}}$ because ${p1} \\neq {p2}$ [1 Mark].\n\n"
        f"$$\\therefore \\text{{A}} = {p1}, \\quad \\text{{B}} = {p2} \\text{{ (Unequal)}}$$"
    )
    ans = f"1. A = {p1}; 2. B = {p2}; 3. Unequal"
    return {
        "id": f"g8_exp_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "32_comparing_bracketed_and_unbracketed_powers",
        "hints": {
            "tier_1": "(-base)² has base -base (positive result). -base² is negative of base² (negative result).",
            "tier_2": f"A = {p1}, B = {p2}.",
            "tier_3": f"They are unequal: {p1} ≠ {p2}."
        },
        "misconception_tags": ["bracket_omission_equivalence_misbelief"]
    }


def arch_33_negative_base_with_variables(rng: random.Random) -> Dict[str, Any]:
    ans1 = "-x^3"
    ans2 = "x^4"

    prompt = (
        f"Simplify the following two algebraic powers by removing brackets:\n\n"
        f"1. $$(-x)^3$$\n"
        f"2. $$(-x)^4$$"
    )
    sol = (
        f"**Step 1:** $(-x)^3 = (-1)^3 x^3 = -x^3$ [1 Mark].\n\n"
        f"**Step 2:** $(-x)^4 = (-1)^4 x^4 = +x^4 = x^4$ [1 Mark].\n\n"
        f"$$\\therefore 1. -x^3, \\quad 2. x^4$$"
    )
    ans = f"1. {ans1}; 2. {ans2}"
    return {
        "id": f"g8_exp_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "33_negative_base_with_variables",
        "hints": {
            "tier_1": "Odd powers keep the negative sign; even powers eliminate the negative sign.",
            "tier_2": "(-1)³ = -1 and (-1)⁴ = 1.",
            "tier_3": "1. -x³; 2. x⁴."
        },
        "misconception_tags": ["variable_negative_base_sign_slip"]
    }


def arch_34_power_of_negative_coefficient_product(rng: random.Random) -> Dict[str, Any]:
    c = 2
    e_x = 2
    outer = rng.choice([3, 4])
    c_pow = (-c) ** outer
    x_pow = e_x * outer
    ans = f"{c_pow}x^{x_pow}"

    prompt = (
        f"Expand and simplify:\n\n"
        f"$$(-{c}x^{{{e_x}}})^{{{outer}}}$$"
    )
    sol = (
        f"**Step 1:** Raise the negative coefficient to power {outer}: $(-{c})^{{{outer}}} = {c_pow}$ [1 Mark].\n\n"
        f"**Step 2:** Raise $x^{{{e_x}}}$ to power {outer}: $(x^{{{e_x}}})^{{{outer}}} = x^{{{x_pow}}}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "34_power_of_negative_coefficient_product",
        "hints": {
            "tier_1": f"Calculate (-{c})^{outer} first.",
            "tier_2": f"Multiply the x-exponent by {outer}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["negative_coefficient_power_distribution_error"]
    }


def arch_35_sum_and_difference_of_negative_base_powers(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    b = rng.choice([2, 3])
    t1 = -(a ** 3)  # (-a)^3
    t2 = b ** 2  # (-b)^2
    ans = t1 + t2

    prompt = (
        f"Evaluate the expression showing the numerical value of each term:\n\n"
        f"$$(-{a})^3 + (-{b})^2$$"
    )
    sol = (
        f"**Step 1:** $(-{a})^3 = {t1}$ [1 Mark].\n\n"
        f"**Step 2:** $(-{b})^2 = +{t2}$ [1 Mark].\n\n"
        f"**Step 3:** Sum: ${t1} + {t2} = {ans}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "35_sum_and_difference_of_negative_base_powers",
        "hints": {
            "tier_1": "Calculate each power independently before adding.",
            "tier_2": f"(-{a})³ = {t1} and (-{b})² = {t2}.",
            "tier_3": f"{t1} + {t2} = {ans}."
        },
        "misconception_tags": ["adding_powers_before_evaluating"]
    }


def arch_36_multiplication_of_powers_with_negative_bases(rng: random.Random) -> Dict[str, Any]:
    base = 2
    e1 = rng.randint(2, 3)
    e2 = rng.randint(2, 3)
    tot = e1 + e2
    val = (-base) ** tot

    prompt = (
        f"Apply the product law of exponents to simplify:\n\n"
        f"$$(-{base})^{{{e1}}} \\times (-{base})^{{{e2}}}$$\n\n"
        f"Write your answer in single-power form, and determine its final integer value."
    )
    sol = (
        f"**Step 1:** Bases are identical ($(-{base})$), so add the exponents: $(-{base})^{{{e1} + {e2}}} = (-{base})^{{{tot}}}$ [1 Mark].\n\n"
        f"**Step 2:** Evaluate: $(-{base})^{{{tot}}} = {val}$ [1 Mark].\n\n"
        f"$$\\therefore (-{base})^{{{tot}}} = {val}$$"
    )
    ans = f"(-{base})^{tot} = {val}"
    return {
        "id": f"g8_exp_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "36_multiplication_of_powers_with_negative_bases",
        "hints": {
            "tier_1": "Keep the base (-2) and add exponents.",
            "tier_2": f"Exponent = {e1} + {e2} = {tot}.",
            "tier_3": f"(-{base})^{tot} = {val}."
        },
        "misconception_tags": ["dropping_negative_base_bracket"]
    }


# ==============================================================================
# CLUSTER 5: Roots of Exponential Expressions & Prime Bases (37 - 42)
# ==============================================================================

def arch_37_square_root_of_exponential_monomial(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(2, 6)
    even_exp = 2 * k
    ans = f"x^{k}"

    prompt = (
        f"Simplify the square root of the power expression:\n\n"
        f"$$\\sqrt{{x^{{{even_exp}}}}}$$"
    )
    sol = (
        f"**Step 1:** Taking the square root of a power divides its exponent by 2:\n"
        f"$$\\sqrt{{x^{{{even_exp}}}}} = (x^{{{even_exp}}})^{{\\frac{{1}}{{2}}}} = x^{{\\frac{{{even_exp}}}{{2}}}} = x^{{{k}}}$$ [2 Marks]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "37_square_root_of_exponential_monomial",
        "hints": {
            "tier_1": "Divide the exponent by 2.",
            "tier_2": f"{even_exp} / 2 = {k}.",
            "tier_3": f"x^{k}."
        },
        "misconception_tags": ["taking_square_root_of_exponent_instead_of_halving"]
    }


def arch_38_square_root_with_numerical_coefficient(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([4, 6, 8, 9, 10, 12])
    c_sq = c ** 2
    kx = rng.randint(2, 4)
    ky = rng.randint(2, 4)
    ex = 2 * kx
    ey = 2 * ky
    ans = f"{c}x^{kx}y^{ky}"

    prompt = (
        f"Determine the square root of the monomial:\n\n"
        f"$$\\sqrt{{{c_sq}x^{{{ex}}}y^{{{ey}}}}}$$"
    )
    sol = (
        f"**Step 1:** Square root of coefficient: $\\sqrt{{{c_sq}}} = {c}$ [1 Mark].\n\n"
        f"**Step 2:** Halve the variable exponents: $\\sqrt{{x^{{{ex}}}}} = x^{{{kx}}}$ and $\\sqrt{{y^{{{ey}}}}} = y^{{{ky}}}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "38_square_root_with_numerical_coefficient",
        "hints": {
            "tier_1": "Take the square root of the number and halve each variable exponent.",
            "tier_2": f"sqrt({c_sq}) = {c}; x-power = {kx}, y-power = {ky}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["halving_coefficient_instead_of_square_root"]
    }


def arch_39_cube_root_of_exponential_monomial(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(2, 5)
    triple_exp = 3 * k
    ans = f"x^{k}"

    prompt = (
        f"Simplify the cube root expression:\n\n"
        f"$$\\sqrt[3]{{x^{{{triple_exp}}}}}$$"
    )
    sol = (
        f"**Step 1:** Taking the cube root divides the exponent by 3:\n"
        f"$$\\sqrt[3]{{x^{{{triple_exp}}}}} = x^{{\\frac{{{triple_exp}}}{{3}}}} = x^{{{k}}}$$ [2 Marks]\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "39_cube_root_of_exponential_monomial",
        "hints": {
            "tier_1": "Divide the exponent by 3.",
            "tier_2": f"{triple_exp} / 3 = {k}.",
            "tier_3": f"x^{k}."
        },
        "misconception_tags": ["cube_root_exponent_division_slip"]
    }


def arch_40_cube_root_with_numerical_coefficient(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 4, 5])
    c_cube = c ** 3
    ka = rng.randint(2, 4)
    kb = rng.randint(2, 4)
    ea = 3 * ka
    eb = 3 * kb
    ans = f"{c}a^{ka}b^{kb}"

    prompt = (
        f"Find the cube root:\n\n"
        f"$$\\sqrt[3]{{{c_cube}a^{{{ea}}}b^{{{eb}}}}}$$"
    )
    sol = (
        f"**Step 1:** Cube root of coefficient: $\\sqrt[3]{{{c_cube}}} = {c}$ [1 Mark].\n\n"
        f"**Step 2:** Divide exponents by 3: $a^{{{ea} \\div 3}} = a^{{{ka}}}$ and $b^{{{eb} \\div 3}} = b^{{{kb}}}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "40_cube_root_with_numerical_coefficient",
        "hints": {
            "tier_1": f"Cube root of {c_cube} is {c}.",
            "tier_2": f"Divide powers: {ea}/3 = {ka} and {eb}/3 = {kb}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["dividing_coefficient_by_3_instead_of_cube_root"]
    }


def arch_41_cube_root_of_negative_exponential_expression(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 4, 5])
    c_cube = c ** 3
    k = rng.randint(2, 4)
    ex = 3 * k
    ans = f"-{c}x^{k}"

    prompt = (
        f"Evaluate the cube root containing a negative monomial:\n\n"
        f"$$\\sqrt[3]{{-{c_cube}x^{{{ex}}}}}$$"
    )
    sol = (
        f"**Step 1:** Cube root of negative coefficient: $\\sqrt[3]{{-{c_cube}}} = -{c}$ [1 Mark].\n\n"
        f"**Step 2:** Cube root of variable power: $x^{{{ex} \\div 3}} = x^{{{k}}}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "41_cube_root_of_negative_exponential_expression",
        "hints": {
            "tier_1": "The cube root of a negative number is negative.",
            "tier_2": f"sqrt3(-{c_cube}) = -{c}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["negative_cube_root_declared_non_real"]
    }


def arch_42_rewriting_bases_as_prime_factors(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Express the product in terms of powers of base 2:\n\n"
        f"$$8^x \\cdot 4^x$$\n\n"
        f"Show how rewriting 8 and 4 as powers of 2 leads to a simplified single base-2 power."
    )
    sol = (
        f"**Step 1:** Rewrite composite bases as prime powers of 2:\n"
        f"$$8 = 2^3 \\implies 8^x = (2^3)^x = 2^{{3x}}$$\n"
        f"$$4 = 2^2 \\implies 4^x = (2^2)^x = 2^{{2x}}$$ [1 Mark]\n\n"
        f"**Step 2:** Multiply by adding exponents:\n"
        f"$$2^{{3x}} \\cdot 2^{{2x}} = 2^{{3x + 2x}} = 2^{{5x}}$$ [1 Mark]\n\n"
        f"$$\\therefore 2^{{5x}}$$"
    )
    ans = "2^(5x)"
    return {
        "id": f"g8_exp_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "42_rewriting_bases_as_prime_factors",
        "hints": {
            "tier_1": "Write 8 as 2³ and 4 as 2².",
            "tier_2": "2^(3x) × 2^(2x) = 2^(3x + 2x).",
            "tier_3": "2^(5x)."
        },
        "misconception_tags": ["multiplying_unlike_bases_without_prime_factorisation"]
    }


# ==============================================================================
# CLUSTER 6: Scientific Notation & Exponential Equations (43 - 50)
# ==============================================================================

def arch_43_ordinary_number_to_scientific_notation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2.5, 3.8, 4.2, 5.6, 7.5, 8.4, 9.1])
    k = rng.randint(4, 7)
    val = int(a * (10 ** k))
    ans = f"{a} × 10^{k}"

    prompt = (
        f"Write the whole number **{val:,}** in scientific notation ($A \\times 10^k$, where $1 \\le A < 10$)."
    )
    sol = (
        f"**Step 1:** Place the decimal point after the first non-zero digit to get $A = {a}$ [1 Mark].\n\n"
        f"**Step 2:** Count the number of places the decimal point moved: $k = {k}$ places to the left.\n"
        f"$${val:,} = {a} \\times 10^{{{k}}}$$ [1 Mark]\n\n"
        f"$$\\therefore {a} \\times 10^{{{k}}}$$"
    )
    return {
        "id": f"g8_exp_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "43_ordinary_number_to_scientific_notation",
        "hints": {
            "tier_1": "Scientific notation requires 1 ≤ A < 10.",
            "tier_2": f"Place decimal after first digit: {a}.",
            "tier_3": f"{val:,} = {ans}."
        },
        "misconception_tags": ["scientific_notation_first_factor_not_between_1_and_10"]
    }


def arch_44_scientific_notation_to_ordinary_number(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([1.8, 2.4, 3.6, 4.5, 6.2, 7.9])
    k = rng.randint(4, 6)
    val = int(a * (10 ** k))

    prompt = (
        f"Convert the scientific notation number into an ordinary whole number:\n\n"
        f"$${a} \\times 10^{{{k}}}$$"
    )
    sol = (
        f"**Step 1:** Move the decimal point ${k}$ places to the right [1 Mark].\n\n"
        f"**Step 2:** ${a} \\times 10^{{{k}}} = {val:,}$ [1 Mark].\n\n"
        f"$$\\therefore {val:,}$$"
    )
    ans = f"{val:,}"
    return {
        "id": f"g8_exp_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "44_scientific_notation_to_ordinary_number",
        "hints": {
            "tier_1": f"Multiply {a} by 10^{k} by moving the decimal point {k} places right.",
            "tier_2": f"Fill empty places with zeros.",
            "tier_3": f"{val:,}."
        },
        "misconception_tags": ["decimal_shift_zero_counting_error"]
    }


def arch_45_comparing_two_numbers_in_scientific_notation(rng: random.Random) -> Dict[str, Any]:
    k1 = rng.randint(5, 7)
    k2 = k1 + 1
    a1 = rng.choice([6.5, 7.2, 8.4])
    a2 = rng.choice([1.5, 2.1, 3.0])

    prompt = (
        f"Compare the two numbers written in scientific notation:\n\n"
        f"$$\\text{{A}} = {a1} \\times 10^{{{k1}}} \\quad \\text{{and}} \\quad \\text{{B}} = {a2} \\times 10^{{{k2}}}$$\n\n"
        f"State which number is larger and give a mathematical reason based on the powers of 10."
    )
    sol = (
        f"**Step 1:** Compare the exponents of 10: $10^{{{k2}}} > 10^{{{k1}}}$ by a factor of 10 [1 Mark: Reason].\n\n"
        f"**Step 2:** Because B has a higher order of magnitude, **B is greater than A** [1 Mark: Answer].\n\n"
        f"$$\\therefore \\text{{B is greater than A}}$$ ($${a2} \\times 10^{{{k2}}} > {a1} \\times 10^{{{k1}}}$$)"
    )
    ans = "B is greater than A (higher power of 10)"
    return {
        "id": f"g8_exp_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "45_comparing_two_numbers_in_scientific_notation",
        "hints": {
            "tier_1": "Look at the exponent of 10 first. A higher exponent indicates a larger number.",
            "tier_2": f"10^{k2} is 10 times larger than 10^{k1}.",
            "tier_3": "B is larger."
        },
        "misconception_tags": ["comparing_first_factors_ignoring_exponent"]
    }


def arch_46_multiplying_numbers_in_scientific_notation(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.randint(2, 4)
    a2 = rng.randint(2, 3)
    k1 = rng.randint(3, 5)
    k2 = rng.randint(3, 5)
    prod_a = a1 * a2
    tot_k = k1 + k2
    ans = f"{prod_a} × 10^{tot_k}"

    prompt = (
        f"Multiply the two numbers and write your answer in scientific notation:\n\n"
        f"$$({a1} \\times 10^{{{k1}}}) \\times ({a2} \\times 10^{{{k2}}})$$"
    )
    sol = (
        f"**Step 1:** Multiply the numerical factors: ${a1} \\times {a2} = {prod_a}$ [1 Mark].\n\n"
        f"**Step 2:** Multiply the powers of 10 by adding exponents: $10^{{{k1}}} \\times 10^{{{k2}}} = 10^{{{k1} + {k2}}} = 10^{{{tot_k}}}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "46_multiplying_numbers_in_scientific_notation",
        "hints": {
            "tier_1": "Multiply coefficients and add exponents of 10.",
            "tier_2": f"{a1} × {a2} = {prod_a}; exponents {k1} + {k2} = {tot_k}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["scientific_multiplication_multiplying_exponents_error"]
    }


def arch_47_dividing_numbers_in_scientific_notation(rng: random.Random) -> Dict[str, Any]:
    a2 = rng.choice([2, 3, 4])
    quot_a = rng.choice([2, 3, 4])
    a1 = a2 * quot_a
    k1 = rng.randint(6, 9)
    k2 = rng.randint(2, 4)
    k_diff = k1 - k2
    ans = f"{quot_a} × 10^{k_diff}"

    prompt = (
        f"Calculate the quotient, expressing the result in scientific notation:\n\n"
        f"$$\\frac{{{a1} \\times 10^{{{k1}}}}}{{{a2} \\times 10^{{{k2}}}}}$$"
    )
    sol = (
        f"**Step 1:** Divide the numerical factors: $\\frac{{{a1}}}{{{a2}}} = {quot_a}$ [1 Mark].\n\n"
        f"**Step 2:** Subtract the exponents of 10: $10^{{{k1} - {k2}}} = 10^{{{k_diff}}}$ [1 Mark].\n\n"
        f"$$\\therefore {ans}$$"
    )
    return {
        "id": f"g8_exp_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "47_dividing_numbers_in_scientific_notation",
        "hints": {
            "tier_1": "Divide coefficients and subtract exponents of 10.",
            "tier_2": f"{a1} ÷ {a2} = {quot_a}; {k1} - {k2} = {k_diff}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["scientific_division_adding_exponents_slip"]
    }


def arch_48_solving_exponential_equation_same_base(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7])
    target_exp = rng.randint(3, 7)

    prompt = (
        f"Solve for $x$ in the exponential equation:\n\n"
        f"$${base}^x = {base}^{{{target_exp}}}$$\n\n"
        f"State the principle that justifies your solution."
    )
    sol = (
        f"**Step 1:** Principle of equating exponents: If $a^x = a^y$ and $a > 0, a \\neq 1$, then $x = y$ [1 Mark: Principle].\n\n"
        f"**Step 2:** Equate exponents: $x = {target_exp}$ [1 Mark: Answer].\n\n"
        f"$$\\therefore x = {target_exp}$$"
    )
    ans = str(target_exp)
    return {
        "id": f"g8_exp_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "48_solving_exponential_equation_same_base",
        "hints": {
            "tier_1": "When the bases on both sides of the equation are equal, set the exponents equal.",
            "tier_2": f"Base is {base} on both sides.",
            "tier_3": f"x = {target_exp}."
        },
        "misconception_tags": ["dividing_both_sides_by_base_error"]
    }


def arch_49_solving_exponential_equation_converting_base(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([(2, 4, 16), (2, 5, 32), (3, 3, 27), (3, 4, 81), (5, 3, 125)])
    base, ans, rhs = pair

    prompt = (
        f"Solve for $x$:\n\n"
        f"$${base}^x = {rhs}$$\n\n"
        f"Show how converting {rhs} to a power of {base} allows you to solve the equation."
    )
    sol = (
        f"**Step 1:** Express the right-hand side as a power of base {base}:\n"
        f"$${rhs} = {base}^{{{ans}}}$$ [1 Mark]\n\n"
        f"**Step 2:** Equate the exponents:\n"
        f"$${base}^x = {base}^{{{ans}}} \\implies x = {ans}$$ [1 Mark]\n\n"
        f"$$\\therefore x = {ans}$$"
    )
    return {
        "id": f"g8_exp_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "49_solving_exponential_equation_converting_base",
        "hints": {
            "tier_1": f"Write {rhs} as a power with base {base}.",
            "tier_2": f"{base}^{ans} = {rhs}.",
            "tier_3": f"x = {ans}."
        },
        "misconception_tags": ["dividing_target_by_base_instead_of_power"]
    }


def arch_50_solving_exponential_equation_with_linear_exponent(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3])
    k = rng.randint(3, 5)
    c = rng.randint(1, 2)
    ans = k - c  # x + c = k => x = k - c
    rhs = base ** k

    prompt = (
        f"Solve for $x$ in the exponential equation:\n\n"
        f"$${base}^{{x + {c}}} = {rhs}$$\n\n"
        f"Show all steps of equating bases and solving the resulting linear equation."
    )
    sol = (
        f"**Step 1:** Rewrite {rhs} as a power of {base}:\n"
        f"$${rhs} = {base}^{{{k}}}$$ [1 Mark]\n\n"
        f"**Step 2:** Equate the exponents:\n"
        f"$$x + {c} = {k}$$ [1 Mark]\n\n"
        f"**Step 3:** Solve for $x$:\n"
        f"$$x = {k} - {c} = {ans}$$ [1 Mark]\n\n"
        f"$$\\therefore x = {ans}$$"
    )
    return {
        "id": f"g8_exp_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": str(ans),
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 1,
        "subskill": "50_solving_exponential_equation_with_linear_exponent",
        "hints": {
            "tier_1": f"Write {rhs} as {base}^{k}.",
            "tier_2": f"Set exponents equal: x + {c} = {k}.",
            "tier_3": f"x = {ans}."
        },
        "misconception_tags": ["linear_exponent_transposition_error"]
    }
