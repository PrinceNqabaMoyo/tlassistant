"""Grade 9 Mathematics - Factorisation & Algebraic Expressions 2 Archetypes (01 to 25).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 1/06. Algebraic expressions 2.md
  - curriculum_docs/Mathematics_Gr9/Algebraic Expressions Studio.md

Covers:
  - Common factor extraction (numerical, variable, negative, trinomial HCF)
  - Binomial common factor and the sign-change rule (y - x) = -(x - y)
  - Difference of two squares (basic, leading coefficient, two variables, higher powers)
  - Common factor first followed by difference of squares
  - Quadratic trinomials (all 4 sign combinations and perfect squares)
  - Common factor first followed by trinomial factorisation
  - Factorisation by grouping in pairs (4 terms, standard and with sign change)
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .factorisation_svg import (
    draw_factorisation_area_model_svg,
    draw_factorisation_rectangle_svg,
)


def arch_01_hcf_numerical_monomial_extraction(rng: random.Random) -> Dict[str, Any]:
    """Extract an integer common factor: k*x + k*c = k(x + c)."""
    k = rng.choice([3, 4, 5, 6, 7, 8])
    c = rng.choice([2, 3, 4, 5, 7])
    kc = k * c
    expr = f"{k}x + {kc}"
    ans = f"{k}(x + {c})"

    return {
        "subskill": "01_hcf_numerical_monomial_extraction",
        "question_text": (
            f"Factorise fully by taking out the highest common factor (HCF):\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify highest common factor HCF = {k}", "marks": 1},
            {"step": f"Write in factored form: {ans}", "marks": 1},
        ],
        "hints": [
            f"Find the largest integer that divides both ${k}$ and ${kc}$.",
            f"The HCF is ${k}$. Divide each term by ${k}$: ${k}x \\div {k} = x$ and ${kc} \\div {k} = {c}$.",
            f"The factorised form is ${ans}$.",
        ],
    }


def arch_02_hcf_variable_monomial_extraction(rng: random.Random) -> Dict[str, Any]:
    """Extract variable common factor: x^2 + c*x = x(x + c)."""
    c = rng.choice([3, 4, 6, 7, 9])
    sign = rng.choice(["+", "-"])
    expr = f"x^2 {sign} {c}x"
    ans = f"x(x {sign} {c})"

    return {
        "subskill": "02_hcf_variable_monomial_extraction",
        "question_text": (
            f"Factorise completely by extracting the common variable factor:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify common variable factor x", "marks": 1},
            {"step": f"Write factored expression: {ans}", "marks": 1},
        ],
        "hints": [
            "Both terms contain the variable $x$. Take out $x$ to the lowest power (which is $x^1$).",
            f"Divide each term by $x$: $x^2 \\div x = x$, and ${sign}{c}x \\div x = {sign}{c}$.",
            f"Factored form is ${ans}$.",
        ],
    }


def arch_03_hcf_combined_numerical_and_variable(rng: random.Random) -> Dict[str, Any]:
    """Extract common monomial ax: a*b*x^2 + a*c*x = a*x(b*x + c)."""
    a = rng.choice([2, 3, 4, 5])
    b = rng.choice([2, 3])
    c = rng.choice([3, 5, 7])
    ab = a * b
    ac = a * c
    expr = f"{ab}x^2 + {ac}x"
    ans = f"{a}x({b}x + {c})"

    return {
        "subskill": "03_hcf_combined_numerical_and_variable",
        "question_text": (
            f"Factorise completely by taking out the highest common factor:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Determine HCF = {a}x", "marks": 1},
            {"step": f"Divide each term by {a}x to obtain ({b}x + {c})", "marks": 1},
        ],
        "hints": [
            f"Find the numerical HCF of ${ab}$ and ${ac}$, which is ${a}$.",
            f"Both terms also contain $x$, so the full HCF is ${a}x$.",
            f"Divide through by ${a}x$: ${ans}$.",
        ],
    }


def arch_04_hcf_negative_leading_coefficient_extraction(rng: random.Random) -> Dict[str, Any]:
    """Factor out negative common factor: -k*x - k*c = -k(x + c)."""
    k = rng.choice([2, 3, 4, 5])
    c = rng.choice([3, 4, 6, 7])
    kc = k * c
    expr = f"-{k}x - {kc}"
    ans = f"-{k}(x + {c})"

    return {
        "subskill": "04_hcf_negative_leading_coefficient_extraction",
        "question_text": (
            f"Factorise fully by taking out a **negative** common factor:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factor out -{k} as common factor", "marks": 1},
            {"step": f"Ensure signs inside bracket become positive: {ans}", "marks": 1},
        ],
        "hints": [
            f"When you factor out a negative number ($-{k}$), all terms inside the brackets change sign.",
            f"$-{k}x \\div (-{k}) = +x$ and $-{kc} \\div (-{k}) = +{c}$.",
            f"Factored form is ${ans}$.",
        ],
    }


def arch_05_hcf_trinomial_common_factor(rng: random.Random) -> Dict[str, Any]:
    """Extract HCF from three terms: k*x^3 + k*a*x^2 - k*b*x = k*x(x^2 + a*x - b)."""
    k = rng.choice([2, 3, 5])
    a = rng.choice([2, 4])
    b = rng.choice([3, 6])
    t1 = k
    t2 = k * a
    t3 = k * b
    expr = f"{t1}x^3 + {t2}x^2 - {t3}x"
    ans = f"{k}x(x^2 + {a}x - {b})"

    return {
        "subskill": "05_hcf_trinomial_common_factor",
        "question_text": (
            f"Factorise by extracting the highest common factor from all three terms:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify HCF of all three terms as {k}x", "marks": 1},
            {"step": f"Divide each term by {k}x to get (x^2 + {a}x - {b})", "marks": 1},
        ],
        "hints": [
            f"Inspect all three terms: each has a numerical factor divisible by ${k}$ and at least one factor of $x$.",
            f"Take out ${k}x$: $\\frac{{{t1}x^3}}{{{k}x}} = x^2$, $\\frac{{{t2}x^2}}{{{k}x}} = {a}x$, $-\\frac{{{t3}x}}{{{k}x}} = -{b}$.",
            f"The result is ${ans}$.",
        ],
    }


def arch_06_hcf_binomial_bracket_common_factor(rng: random.Random) -> Dict[str, Any]:
    """Extract common binomial bracket: a(x + y) + b(x + y) = (x + y)(a + b)."""
    a = rng.choice([2, 3, 5, 7])
    b = rng.choice([4, 6, 8])
    expr = f"{a}(x + y) + {b}(x + y)"
    ans = f"({a + b})(x + y)"

    return {
        "subskill": "06_hcf_binomial_bracket_common_factor",
        "question_text": (
            f"Factorise and simplify completely:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify (x + y) as the common binomial factor", "marks": 1},
            {"step": f"Combine coefficients ({a} + {b}) to obtain {ans}", "marks": 1},
        ],
        "hints": [
            "Notice that the binomial bracket $(x + y)$ appears in both terms as a common factor.",
            f"Factor out $(x + y)$: $(x + y)({a} + {b})$.",
            f"Combine numerical coefficients: ${a} + {b} = {a + b}$. Answer is ${ans}$.",
        ],
    }


def arch_07_hcf_binomial_bracket_with_negative_sign(rng: random.Random) -> Dict[str, Any]:
    """Extract binomial bracket: x(a - b) - y(a - b) = (a - b)(x - y)."""
    expr = "x(a - b) - y(a - b)"
    ans = "(a - b)(x - y)"

    return {
        "subskill": "07_hcf_binomial_bracket_with_negative_sign",
        "question_text": (
            f"Factorise completely by removing the common binomial bracket:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify (a - b) as common binomial factor", "marks": 1},
            {"step": f"Write remaining factors as (x - y): {ans}", "marks": 1},
        ],
        "hints": [
            "Both terms share the exact same bracket $(a - b)$.",
            "Take out $(a - b)$ in front, and collect the remaining terms in the second bracket: $(x - y)$.",
            f"Result: ${ans}$.",
        ],
    }


def arch_08_hcf_bracket_sign_change_rule(rng: random.Random) -> Dict[str, Any]:
    """Apply sign change rule (y - x) = -(x - y) to factorise: a(x - y) + b(y - x)."""
    a = rng.choice([3, 4, 5])
    b = rng.choice([2, 6, 7])
    expr = f"{a}(x - y) + {b}(y - x)"
    ans = f"({a - b})(x - y)" if a - b != 1 else "(x - y)"

    return {
        "subskill": "08_hcf_bracket_sign_change_rule",
        "question_text": (
            f"Factorise fully by applying the **sign-change rule**:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply sign-change rule: {b}(y - x) = -{b}(x - y)", "marks": 1},
            {"step": f"Combine common bracket (x - y): ({a} - {b})(x - y) = {ans}", "marks": 1},
        ],
        "hints": [
            "Notice that $(y - x) = -(x - y)$.",
            f"Change the second term: $+{b}(y - x)$ becomes $-{b}(x - y)$.",
            f"Now factor out $(x - y)$: $({a} - {b})(x - y) = {ans}$.",
        ],
    }


def arch_09_difference_of_two_squares_basic(rng: random.Random) -> Dict[str, Any]:
    """Difference of two squares: x^2 - k^2 = (x - k)(x + k)."""
    k = rng.choice([4, 5, 6, 7, 8, 9, 10, 11, 12])
    k2 = k**2
    expr = f"x^2 - {k2}"
    ans = f"(x - {k})(x + {k})"

    return {
        "subskill": "09_difference_of_two_squares_basic",
        "question_text": (
            f"Factorise the difference of two squares:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recognize x^2 - {k2} as a difference of squares: x^2 - ({k})^2", "marks": 1},
            {"step": f"Write factors: {ans}", "marks": 1},
        ],
        "hints": [
            "Difference of squares formula: $A^2 - B^2 = (A - B)(A + B)$.",
            f"Here $A = x$ and $B = \\sqrt{{{k2}}} = {k}$.",
            f"The factors are ${ans}$.",
        ],
    }


def arch_10_difference_of_two_squares_large_perfect_square(rng: random.Random) -> Dict[str, Any]:
    """Difference of two squares with larger squares (13^2 to 20^2)."""
    k = rng.choice([13, 14, 15, 16, 20])
    k2 = k**2
    expr = f"x^2 - {k2}"
    ans = f"(x - {k})(x + {k})"

    return {
        "subskill": "10_difference_of_two_squares_large_perfect_square",
        "question_text": (
            f"Factorise completely:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify square root of {k2} as {k}", "marks": 1},
            {"step": f"Factorise as (x - {k})(x + {k})", "marks": 1},
        ],
        "hints": [
            f"Find the square root of ${k2}$: $\\sqrt{{{k2}}} = {k}$.",
            f"Use the identity $x^2 - {k}^2 = (x - {k})(x + {k})$.",
            f"Answer: ${ans}$.",
        ],
    }


def arch_11_difference_of_two_squares_with_leading_coefficient(rng: random.Random) -> Dict[str, Any]:
    """Difference of squares: a^2 x^2 - b^2 = (ax - b)(ax + b)."""
    a = rng.choice([2, 3, 5])
    b = rng.choice([3, 5, 7])
    while a == b:
        b = rng.choice([3, 5, 7])
    a2 = a**2
    b2 = b**2
    expr = f"{a2}x^2 - {b2}"
    ans = f"({a}x - {b})({a}x + {b})"

    return {
        "subskill": "11_difference_of_two_squares_with_leading_coefficient",
        "question_text": (
            f"Factorise fully:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Take square root of first term: sqrt({a2}x^2) = {a}x", "marks": 1},
            {"step": f"Take square root of second term: sqrt({b2}) = {b}", "marks": 1},
            {"step": f"Write factors: {ans}", "marks": 1},
        ],
        "hints": [
            f"Square root of ${a2}x^2$ is ${a}x$.",
            f"Square root of ${b2}$ is ${b}$.",
            f"Apply $(A - B)(A + B)$: ${ans}$.",
        ],
    }


def arch_12_difference_of_two_squares_two_variables(rng: random.Random) -> Dict[str, Any]:
    """Difference of squares with two variables: a^2 x^2 - b^2 y^2."""
    a = rng.choice([3, 4, 7])
    b = rng.choice([2, 5, 6])
    a2 = a**2
    b2 = b**2
    expr = f"{a2}x^2 - {b2}y^2"
    ans = f"({a}x - {b}y)({a}x + {b}y)"

    return {
        "subskill": "12_difference_of_two_squares_two_variables",
        "question_text": (
            f"Factorise completely:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recognize difference of squares with two variables: ({a}x)^2 - ({b}y)^2", "marks": 1},
            {"step": f"Write factors: {ans}", "marks": 1},
        ],
        "hints": [
            f"First term: $({a}x)^2$; Second term: $({b}y)^2$.",
            f"Apply $(A - B)(A + B)$: $({a}x - {b}y)({a}x + {b}y)$.",
            f"Answer is ${ans}$.",
        ],
    }


def arch_13_difference_of_two_squares_higher_even_power(rng: random.Random) -> Dict[str, Any]:
    """Difference of squares: x^4 - 81 = (x^2 - 9)(x^2 + 9) = (x - 3)(x + 3)(x^2 + 9)."""
    k = rng.choice([2, 3])
    k4 = k**4
    k2 = k**2
    expr = f"x^4 - {k4}"
    ans = f"(x - {k})(x + {k})(x^2 + {k2})"

    return {
        "subskill": "13_difference_of_two_squares_higher_even_power",
        "question_text": (
            f"Factorise **completely** (do not leave any factor that can still be factorised):\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"First factorisation: (x^2 - {k2})(x^2 + {k2})", "marks": 1},
            {"step": f"Factorise (x^2 - {k2}) further: (x - {k})(x + {k})", "marks": 1},
            {"step": f"State final completely factored form: {ans}", "marks": 1},
        ],
        "hints": [
            f"First step: $x^4 - {k4} = (x^2 - {k2})(x^2 + {k2})$.",
            f"Crucial check: $(x^2 - {k2})$ is another difference of squares! $(x^2 - {k2}) = (x - {k})(x + {k})$.",
            f"Note that the sum of squares $(x^2 + {k2})$ cannot be factorised further. Answer is ${ans}$.",
        ],
    }


def arch_14_common_factor_first_then_difference_of_squares(rng: random.Random) -> Dict[str, Any]:
    """Common factor first, then difference of squares: k*x^2 - k*b^2 = k(x - b)(x + b)."""
    k = rng.choice([2, 3, 5])
    b = rng.choice([3, 4, 5])
    b2 = b**2
    kb2 = k * b2
    expr = f"{k}x^2 - {kb2}"
    ans = f"{k}(x - {b})(x + {b})"

    return {
        "subskill": "14_common_factor_first_then_difference_of_squares",
        "question_text": (
            f"Factorise completely by first taking out the common factor:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Extract common factor {k}: {k}(x^2 - {b2})", "marks": 1},
            {"step": f"Factorise difference of squares: {ans}", "marks": 1},
        ],
        "hints": [
            f"Always check for a common factor first! Both terms are divisible by ${k}$.",
            f"Take out ${k}$: ${k}(x^2 - {b2})$.",
            f"Now factorise $x^2 - {b2}$: $(x - {b})(x + {b})$. Full answer is ${ans}$.",
        ],
    }


def arch_15_trinomial_factorisation_positive_sum_positive_product(rng: random.Random) -> Dict[str, Any]:
    """Trinomial with both signs positive: x^2 + (p+q)x + pq = (x + p)(x + q)."""
    p = rng.choice([2, 3, 4])
    q = rng.choice([5, 6, 7])
    mid = p + q
    last = p * q
    expr = f"x^2 + {mid}x + {last}"
    ans = f"(x + {p})(x + {q})"

    return {
        "subskill": "15_trinomial_factorisation_positive_sum_positive_product",
        "question_text": (
            f"Factorise the quadratic trinomial:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Find two factors of {last} that add to {mid}: {p} and {q}", "marks": 1},
            {"step": f"Write factorised form: {ans}", "marks": 1},
        ],
        "hints": [
            f"Look for two numbers that multiply to give ${last}$ and add together to give ${mid}$.",
            f"The factors are ${p}$ and ${q}$ because ${p} \\times {q} = {last}$ and ${p} + {q} = {mid}$.",
            f"The factors are ${ans}$.",
        ],
    }


def arch_16_trinomial_factorisation_negative_sum_positive_product(rng: random.Random) -> Dict[str, Any]:
    """Trinomial with negative sum, positive product: x^2 - (p+q)x + pq = (x - p)(x - q)."""
    p = rng.choice([2, 3, 4])
    q = rng.choice([4, 5, 7])
    mid = p + q
    last = p * q
    expr = f"x^2 - {mid}x + {last}"
    ans = f"(x - {p})(x - {q})"

    return {
        "subskill": "16_trinomial_factorisation_negative_sum_positive_product",
        "question_text": (
            f"Factorise the quadratic trinomial:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify two negative factors of +{last} that add to -{mid}: -{p} and -{q}", "marks": 1},
            {"step": f"Write factorised form: {ans}", "marks": 1},
        ],
        "hints": [
            f"Since the last term is positive (+{last}) and the middle term is negative (-{mid}), both factors must be negative.",
            f"Two numbers that multiply to ${last}$ and add to $-{mid}$ are $-{p}$ and $-{q}$.",
            f"The factorised result is ${ans}$.",
        ],
    }


def arch_17_trinomial_factorisation_positive_sum_negative_product(rng: random.Random) -> Dict[str, Any]:
    """Trinomial with positive sum, negative product: x^2 + (p-q)x - pq = (x + p)(x - q)."""
    p = rng.choice([6, 7, 8, 9])
    q = rng.choice([2, 3, 4, 5])
    while p <= q:
        p += 2
    mid = p - q
    last = p * q
    expr = f"x^2 + {mid}x - {last}"
    ans = f"(x + {p})(x - {q})"

    return {
        "subskill": "17_trinomial_factorisation_positive_sum_negative_product",
        "question_text": (
            f"Factorise the trinomial:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Find factors of -{last} with difference {mid}: +{p} and -{q}", "marks": 1},
            {"step": f"Write factors: {ans}", "marks": 1},
        ],
        "hints": [
            f"Because the last term is negative (-{last}), the factors have opposite signs.",
            f"The larger factor must be positive because the middle term is $+{mid}x$.",
            f"Numbers are $+{p}$ and $-{q}$: ${ans}$.",
        ],
    }


def arch_18_trinomial_factorisation_negative_sum_negative_product(rng: random.Random) -> Dict[str, Any]:
    """Trinomial with negative sum, negative product: x^2 - (p-q)x - pq = (x - p)(x + q)."""
    p = rng.choice([6, 7, 8, 9])
    q = rng.choice([2, 3, 4, 5])
    while p <= q:
        p += 2
    mid = p - q
    last = p * q
    expr = f"x^2 - {mid}x - {last}"
    ans = f"(x - {p})(x + {q})"

    return {
        "subskill": "18_trinomial_factorisation_negative_sum_negative_product",
        "question_text": (
            f"Factorise:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Find factors of -{last} adding to -{mid}: -{p} and +{q}", "marks": 1},
            {"step": f"Write factors: {ans}", "marks": 1},
        ],
        "hints": [
            f"Opposite signs needed because product is $-{last}$.",
            f"The negative factor must have a larger absolute value because the middle term is $-{mid}$.",
            f"Factors: $-{p}$ and $+{q}$, giving ${ans}$.",
        ],
    }


def arch_19_trinomial_factorisation_perfect_square_sum(rng: random.Random) -> Dict[str, Any]:
    """Perfect square trinomial: x^2 + 2kx + k^2 = (x + k)^2."""
    k = rng.choice([3, 4, 5, 6, 7, 8])
    mid = 2 * k
    last = k**2
    expr = f"x^2 + {mid}x + {last}"
    ans = f"(x + {k})^2"

    return {
        "subskill": "19_trinomial_factorisation_perfect_square_sum",
        "question_text": (
            f"Factorise the perfect square trinomial:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recognize perfect square pattern (x + k)^2 with k = {k}", "marks": 1},
            {"step": f"Write as squared binomial: {ans}", "marks": 1},
        ],
        "hints": [
            f"Notice that the last term is a perfect square: ${last} = {k}^2$.",
            f"The middle term is double the square root: $2 \\times {k} = {mid}$.",
            f"Therefore, this is a perfect square: ${ans}$.",
        ],
    }


def arch_20_trinomial_factorisation_perfect_square_difference(rng: random.Random) -> Dict[str, Any]:
    """Perfect square trinomial difference: x^2 - 2kx + k^2 = (x - k)^2."""
    k = rng.choice([3, 4, 5, 6, 7, 8])
    mid = 2 * k
    last = k**2
    expr = f"x^2 - {mid}x + {last}"
    ans = f"(x - {k})^2"

    return {
        "subskill": "20_trinomial_factorisation_perfect_square_difference",
        "question_text": (
            f"Factorise completely:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify perfect square difference pattern: (x - {k})^2", "marks": 1},
        ],
        "hints": [
            f"First term is $x^2$, last term is $(-{k})^2 = {last}$.",
            f"Middle term is $-2 \\times {k} \\times x = -{mid}x$.",
            f"The factorised form is ${ans}$.",
        ],
    }


def arch_21_common_factor_first_then_trinomial_factorisation(rng: random.Random) -> Dict[str, Any]:
    """Extract common factor then factorise trinomial: a(x^2 + (p+q)x + pq)."""
    a = rng.choice([2, 3, 5])
    p = rng.choice([2, 3])
    q = rng.choice([4, 5])
    mid = p + q
    last = p * q

    t1 = a
    t2 = a * mid
    t3 = a * last
    expr = f"{t1}x^2 + {t2}x + {t3}"
    ans = f"{a}(x + {p})(x + {q})"

    return {
        "subskill": "21_common_factor_first_then_trinomial_factorisation",
        "question_text": (
            f"Factorise completely by first extracting the common factor:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factor out common factor {a}: {a}(x^2 + {mid}x + {last})", "marks": 1},
            {"step": f"Factorise quadratic trinomial: {ans}", "marks": 1},
        ],
        "hints": [
            f"Notice every coefficient is divisible by ${a}$. Factor out ${a}$ first: ${a}(x^2 + {mid}x + {last})$.",
            f"Now factorise the trinomial inside: $(x + {p})(x + {q})$.",
            f"The final completely factored expression is ${ans}$.",
        ],
    }


def arch_22_negative_common_factor_then_trinomial(rng: random.Random) -> Dict[str, Any]:
    """Factor out -1 then factorise trinomial: -x^2 - (p+q)x - pq = -(x + p)(x + q)."""
    p = rng.choice([2, 3])
    q = rng.choice([4, 5])
    mid = p + q
    last = p * q
    expr = f"-x^2 - {mid}x - {last}"
    ans = f"-(x + {p})(x + {q})"

    return {
        "subskill": "22_negative_common_factor_then_trinomial",
        "question_text": (
            f"Factorise completely by first removing the negative sign:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factor out -1: -(x^2 + {mid}x + {last})", "marks": 1},
            {"step": f"Factorise trinomial inside: {ans}", "marks": 1},
        ],
        "hints": [
            f"Factor out $-1$ from the entire expression: $-(x^2 + {mid}x + {last})$.",
            f"Factorise the positive trinomial: $(x + {p})(x + {q})$.",
            f"Keep the minus sign in front: ${ans}$.",
        ],
    }


def arch_23_factorise_by_grouping_four_terms_basic(rng: random.Random) -> Dict[str, Any]:
    """Factorise 4 terms by grouping: ax + ay + bx + by = (x + y)(a + b)."""
    expr = "ax + ay + bx + by"
    ans = "(x + y)(a + b)"

    return {
        "subskill": "23_factorise_by_grouping_four_terms_basic",
        "question_text": (
            f"Factorise by grouping into pairs:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Group in pairs: a(x + y) + b(x + y)", "marks": 1},
            {"step": f"Factor out common binomial (x + y): {ans}", "marks": 1},
        ],
        "hints": [
            "Group the first two terms and the last two terms: $(ax + ay) + (bx + by)$.",
            "Factor out $a$ from the first pair and $b$ from the second pair: $a(x + y) + b(x + y)$.",
            f"Now factor out the common binomial $(x + y)$: ${ans}$.",
        ],
    }


def arch_24_factorise_by_grouping_with_negative_middle_terms(rng: random.Random) -> Dict[str, Any]:
    """Grouping with negative signs: mx - my + nx - ny = (x - y)(m + n)."""
    expr = "mx - my + nx - ny"
    ans = "(x - y)(m + n)"

    return {
        "subskill": "24_factorise_by_grouping_with_negative_middle_terms",
        "question_text": (
            f"Factorise the four-term expression by grouping:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Group pairs: m(x - y) + n(x - y)", "marks": 1},
            {"step": f"Factor out common bracket: {ans}", "marks": 1},
        ],
        "hints": [
            "Group as $(mx - my) + (nx - ny)$.",
            "Extract $m$ and $n$: $m(x - y) + n(x - y)$.",
            f"Result is ${ans}$.",
        ],
    }


def arch_25_factorise_by_grouping_with_sign_change_needed(rng: random.Random) -> Dict[str, Any]:
    """Grouping with sign change on second pair: ax - ay - bx + by = (x - y)(a - b)."""
    expr = "ax - ay - bx + by"
    ans = "(x - y)(a - b)"

    return {
        "subskill": "25_factorise_by_grouping_with_sign_change_needed",
        "question_text": (
            f"Factorise by grouping in pairs (pay careful attention to signs):\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Factor first pair: a(x - y)", "marks": 1},
            {"step": "Factor out -b from second pair: -b(x - y)", "marks": 1},
            {"step": f"State final factors: {ans}", "marks": 1},
        ],
        "hints": [
            "Factor first pair: $a(x - y)$.",
            "For the second pair $-bx + by$, take out $-b$ so that the sign inside flips: $-b(x - y)$.",
            f"Both terms now share $(x - y)$, giving ${ans}$.",
        ],
    }
