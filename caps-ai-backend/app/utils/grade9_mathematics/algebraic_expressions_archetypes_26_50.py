"""Grade 9 Mathematics - Algebraic Expressions 1 Archetypes (26 to 50).
Grounded strictly in:
  - curriculum_docs/Mathematics_Gr9/Algebraic Expressions Studio.md
  - curriculum_docs_auto/Mathematics_Gr9/Term 1/06. Algebraic expressions 1.md

Covers:
  - Distributive law with variable monomials and trinomials
  - Combining multiple distributed brackets (sum and difference)
  - Binomial products (FOIL method with various sign patterns and leading coefficients)
  - Squaring binomials (ax ± b)^2 and the difference of two squares (x - y)(x + y)
  - Division of polynomials by integers and monomials (single and multi-variable)
  - Roots of monomials (square roots and cube roots)
  - Error analysis: missing middle term in binomial square, sign distribution error
  - Geometric applications (area of rectangle with binomial dimensions)
  - Compound multi-step algebraic manipulation challenges
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .algebraic_expressions_svg import (
    draw_algebraic_flow_diagram_svg,
    draw_algebraic_rectangle_svg,
)


def arch_26_distributive_law_monomial_times_trinomial(rng: random.Random) -> Dict[str, Any]:
    """Expand monomial times trinomial: a(bx^2 + cx + d)."""
    a = rng.choice([2, 3, 4])
    b = rng.choice([2, 3, 5])
    c = rng.choice([-6, -4, 3, 7])
    d = rng.choice([-8, -5, 4, 9])
    tot_b = a * b
    tot_c = a * c
    tot_d = a * d

    sc = f"- {abs(c)}" if c < 0 else f"+ {c}"
    sd = f"- {abs(d)}" if d < 0 else f"+ {d}"
    expr = f"{a}({b}x^2 {sc}x {sd})"

    stot_c = f"- {abs(tot_c)}" if tot_c < 0 else f"+ {tot_c}"
    stot_d = f"- {abs(tot_d)}" if tot_d < 0 else f"+ {tot_d}"
    ans = f"{tot_b}x^2 {stot_c}x {stot_d}"

    return {
        "subskill": "26_distributive_law_monomial_times_trinomial",
        "question_text": (
            f"Expand and simplify by applying the distributive property:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply {a} by {b}x^2 = {tot_b}x^2", "marks": 1},
            {"step": f"Multiply {a} by {c}x = {tot_c}x", "marks": 1},
            {"step": f"Multiply {a} by {d} = {tot_d}", "marks": 1},
        ],
        "hints": [
            f"Multiply the constant ${a}$ by each of the three terms inside the bracket.",
            f"${a} \\times {b}x^2 = {tot_b}x^2$, ${a} \\times ({c}x) = {tot_c}x$, ${a} \\times ({d}) = {tot_d}$.",
            f"The final expanded expression is ${ans}$.",
        ],
    }


def arch_27_distributive_law_variable_monomial_times_binomial(rng: random.Random) -> Dict[str, Any]:
    """Expand variable monomial times binomial: ax(bx + c) = abx^2 + acx."""
    a = rng.choice([2, 3, 5])
    b = rng.choice([3, 4, 6])
    c = rng.choice([-7, -5, 4, 8])
    tot_x2 = a * b
    tot_x = a * c

    sc = f"- {abs(c)}" if c < 0 else f"+ {c}"
    expr = f"{a}x({b}x {sc})"
    stot_x = f"- {abs(tot_x)}" if tot_x < 0 else f"+ {tot_x}"
    ans = f"{tot_x2}x^2 {stot_x}x"

    return {
        "subskill": "27_distributive_law_variable_monomial_times_binomial",
        "question_text": (
            f"Expand the expression:\n$${expr}$$\n\n"
            f"Write your answer in standard form."
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply {a}x by {b}x = {tot_x2}x^2", "marks": 1},
            {"step": f"Multiply {a}x by {c} = {tot_x}x", "marks": 1},
        ],
        "hints": [
            f"Remember laws of exponents: $x \\times x = x^2$.",
            f"${a}x \\times {b}x = {tot_x2}x^2$ and ${a}x \\times ({c}) = {tot_x}x$.",
            f"The expanded result is ${ans}$.",
        ],
    }


def arch_28_expand_and_simplify_two_bracketed_expressions_sum(rng: random.Random) -> Dict[str, Any]:
    """Expand and simplify sum of two distributed brackets: a(x + b) + c(x + d)."""
    a, c = rng.choice([2, 3, 4]), rng.choice([2, 3, 5])
    b, d = rng.choice([3, 4, 5]), rng.choice([-6, -2, 4])
    sd = f"- {abs(d)}" if d < 0 else f"+ {d}"
    expr = f"{a}(x + {b}) + {c}(x {sd})"

    tot_x = a + c
    tot_const = a * b + c * d
    s_const = f"- {abs(tot_const)}" if tot_const < 0 else f"+ {tot_const}"
    ans = f"{tot_x}x {s_const}"

    return {
        "subskill": "28_expand_and_simplify_two_bracketed_expressions_sum",
        "question_text": (
            f"Expand the brackets and simplify the like terms:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Expand first bracket: {a}x + {a * b}", "marks": 1},
            {"step": f"Expand second bracket: {c}x + {c * d}", "marks": 1},
            {"step": f"Combine like terms: {tot_x}x {s_const}", "marks": 1},
        ],
        "hints": [
            f"Expand first bracket: ${a}(x + {b}) = {a}x + {a * b}$.",
            f"Expand second bracket: ${c}(x {sd}) = {c}x + ({c * d})$.",
            f"Combine like terms: $({a} + {c})x + ({a * b} + {c * d}) = {ans}$.",
        ],
    }


def arch_29_expand_and_simplify_two_bracketed_expressions_difference(rng: random.Random) -> Dict[str, Any]:
    """Expand and simplify difference of two brackets: a(bx + c) - d(ex - f)."""
    a = rng.choice([3, 4, 5])
    b = 2
    c = rng.choice([1, 3, 4])
    d = rng.choice([2, 3])
    e = 1
    f = rng.choice([3, 5])

    expr = f"{a}({b}x + {c}) - {d}(x - {f})"
    tot_x = a * b - d * e
    tot_const = a * c + d * f  # -d * -f = +df
    s_const = f"- {abs(tot_const)}" if tot_const < 0 else f"+ {tot_const}"
    ans = f"{tot_x}x {s_const}"

    return {
        "subskill": "29_expand_and_simplify_two_bracketed_expressions_difference",
        "question_text": (
            f"Expand and simplify by collecting like terms:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Expand first bracket: {a * b}x + {a * c}", "marks": 1},
            {"step": f"Expand second bracket with negative: -{d}x + {d * f}", "marks": 1},
            {"step": f"Combine like terms: {tot_x}x {s_const}", "marks": 1},
        ],
        "hints": [
            f"First bracket gives ${a * b}x + {a * c}$.",
            f"Second bracket has a minus outside: $-{d}(x - {f}) = -{d}x + {d * f}$.",
            f"Combine like terms: $({a * b} - {d})x + ({a * c} + {d * f}) = {ans}$.",
        ],
    }


def arch_30_binomial_product_positive_terms_foil(rng: random.Random) -> Dict[str, Any]:
    """FOIL expansion with positive constants: (x + p)(x + q)."""
    p = rng.choice([2, 3, 4, 5])
    q = rng.choice([6, 7, 8, 9])
    mid = p + q
    last = p * q
    ans = f"x^2 + {mid}x + {last}"

    return {
        "subskill": "30_binomial_product_positive_terms_foil",
        "question_text": (
            f"Expand and simplify the product of two binomials:\n$$(x + {p})(x + {q})$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply FOIL: First = x^2, Outer = {q}x, Inner = {p}x, Last = {last}", "marks": 1},
            {"step": f"Combine middle like terms: ({p} + {q})x = {mid}x", "marks": 1},
            {"step": f"State final trinomial: {ans}", "marks": 1},
        ],
        "hints": [
            "Use the FOIL rule (First, Outside, Inside, Last).",
            f"First: $x \\times x = x^2$, Outside: $x \\times {q} = {q}x$, Inside: ${p} \\times x = {p}x$, Last: ${p} \\times {q} = {last}$.",
            f"Combine the like terms ${p}x + {q}x = {mid}x$. Result is ${ans}$.",
        ],
    }


def arch_31_binomial_product_mixed_signs_foil(rng: random.Random) -> Dict[str, Any]:
    """FOIL expansion with mixed signs: (x + p)(x - q)."""
    p = rng.choice([4, 6, 8, 9])
    q = rng.choice([2, 3, 5, 7])
    while p == q:
        q = rng.choice([2, 3, 5, 7])
    mid = p - q
    last = p * q
    s_mid = f"- {abs(mid)}" if mid < 0 else f"+ {mid}"
    ans = f"x^2 {s_mid}x - {last}"

    return {
        "subskill": "31_binomial_product_mixed_signs_foil",
        "question_text": (
            f"Expand and simplify:\n$$(x + {p})(x - {q})$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply binomials: x^2 - {q}x + {p}x - {last}", "marks": 1},
            {"step": f"Combine middle terms: ({p} - {q})x = {mid}x", "marks": 1},
        ],
        "hints": [
            f"First: $x^2$.",
            f"Outer + Inner: $-{q}x + {p}x = {mid}x$.",
            f"Last: ${p} \\times (-{q}) = -{last}$. Result is ${ans}$.",
        ],
    }


def arch_32_binomial_product_both_negative_signs_foil(rng: random.Random) -> Dict[str, Any]:
    """FOIL expansion where both constants are negative: (x - p)(x - q)."""
    p = rng.choice([2, 3, 4])
    q = rng.choice([5, 6, 7])
    mid = -(p + q)
    last = p * q
    ans = f"x^2 - {abs(mid)}x + {last}"

    return {
        "subskill": "32_binomial_product_both_negative_signs_foil",
        "question_text": (
            f"Expand and simplify:\n$$(x - {p})(x - {q})$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply terms: x^2 - {q}x - {p}x + {last}", "marks": 1},
            {"step": f"Combine negative middle terms: -{abs(mid)}x", "marks": 1},
            {"step": f"State final trinomial: {ans}", "marks": 1},
        ],
        "hints": [
            f"Remember: negative $\\times$ negative is positive for the last term: $(-{p}) \\times (-{q}) = +{last}$.",
            f"Middle term adds two negatives: $-{p}x - {q}x = -{abs(mid)}x$.",
            f"The final expanded trinomial is ${ans}$.",
        ],
    }


def arch_33_binomial_product_leading_coefficients_greater_than_one(rng: random.Random) -> Dict[str, Any]:
    """FOIL with coefficients > 1: (ax + b)(cx + d)."""
    a = rng.choice([2, 3])
    c = rng.choice([2, 4, 5])
    b = rng.choice([1, 3, 5])
    d = rng.choice([-4, -2, 3, 4])

    first = a * c
    outer = a * d
    inner = b * c
    mid = outer + inner
    last = b * d

    sd = f"- {abs(d)}" if d < 0 else f"+ {d}"
    expr = f"({a}x + {b})({c}x {sd})"
    s_mid = f"- {abs(mid)}" if mid < 0 else f"+ {mid}"
    s_last = f"- {abs(last)}" if last < 0 else f"+ {last}"
    ans = f"{first}x^2 {s_mid}x {s_last}"

    return {
        "subskill": "33_binomial_product_leading_coefficients_greater_than_one",
        "question_text": (
            f"Expand and simplify:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply first terms: {a}x * {c}x = {first}x^2", "marks": 1},
            {"step": f"Combine outer and inner terms: ({outer} + {inner})x = {mid}x", "marks": 1},
            {"step": f"Multiply last terms: {b} * ({d}) = {last}", "marks": 1},
        ],
        "hints": [
            f"First: ${a}x \\times {c}x = {first}x^2$.",
            f"Outer + Inner: ${a}x \\times ({d}) + {b} \\times {c}x = {outer}x + {inner}x = {mid}x$.",
            f"Last: ${b} \\times ({d}) = {last}$. Combined: ${ans}$.",
        ],
    }


def arch_34_square_of_binomial_sum_ax_plus_b_squared(rng: random.Random) -> Dict[str, Any]:
    """Squaring a sum binomial: (ax + b)^2 = a^2 x^2 + 2abx + b^2."""
    a = rng.choice([1, 2, 3])
    b = rng.choice([3, 4, 5, 7])
    a2 = a**2
    mid = 2 * a * b
    b2 = b**2
    a_str = f"{a}x" if a > 1 else "x"
    a2_str = f"{a2}x^2" if a > 1 else "x^2"
    ans = f"{a2_str} + {mid}x + {b2}"

    return {
        "subskill": "34_square_of_binomial_sum_ax_plus_b_squared",
        "question_text": (
            f"Expand and simplify the square of the binomial:\n$$({a_str} + {b})^2$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Square the first term: ({a_str})^2 = {a2_str}", "marks": 1},
            {"step": f"Double the product of the terms: 2 * ({a_str}) * ({b}) = {mid}x", "marks": 1},
            {"step": f"Square the last term: ({b})^2 = {b2}", "marks": 1},
        ],
        "hints": [
            "Use the formula for squaring a binomial: $(A + B)^2 = A^2 + 2AB + B^2$.",
            f"First term squared: $({a_str})^2 = {a2_str}$.",
            f"Middle term: $2 \\times ({a_str}) \\times {b} = {mid}x$. Last term: ${b}^2 = {b2}$. Result: ${ans}$.",
        ],
    }


def arch_35_square_of_binomial_difference_ax_minus_b_squared(rng: random.Random) -> Dict[str, Any]:
    """Squaring a difference binomial: (ax - b)^2 = a^2 x^2 - 2abx + b^2."""
    a = rng.choice([2, 3, 4])
    b = rng.choice([1, 2, 3, 5])
    a2 = a**2
    mid = 2 * a * b
    b2 = b**2
    ans = f"{a2}x^2 - {mid}x + {b2}"

    return {
        "subskill": "35_square_of_binomial_difference_ax_minus_b_squared",
        "question_text": (
            f"Expand and simplify:\n$$({a}x - {b})^2$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Square first term: ({a}x)^2 = {a2}x^2", "marks": 1},
            {"step": f"Middle term: 2 * ({a}x) * (-{b}) = -{mid}x", "marks": 1},
            {"step": f"Square last term: (-{b})^2 = +{b2}", "marks": 1},
        ],
        "hints": [
            "Rule: $(A - B)^2 = A^2 - 2AB + B^2$.",
            f"First term: $({a}x)^2 = {a2}x^2$.",
            f"Middle term: $-2 \\times ({a}x) \\times {b} = -{mid}x$. Last term: $(-{b})^2 = +{b2}$. Total: ${ans}$.",
        ],
    }


def arch_36_product_of_sum_and_difference_difference_of_two_squares(rng: random.Random) -> Dict[str, Any]:
    """Difference of two squares expansion: (ax - b)(ax + b) = a^2 x^2 - b^2."""
    a = rng.choice([1, 2, 3, 5])
    b = rng.choice([2, 4, 6, 7])
    a2 = a**2
    b2 = b**2
    a_str = f"{a}x" if a > 1 else "x"
    a2_str = f"{a2}x^2" if a > 1 else "x^2"
    ans = f"{a2_str} - {b2}"

    return {
        "subskill": "36_product_of_sum_and_difference_difference_of_two_squares",
        "question_text": (
            f"Expand and simplify the product:\n$$({a_str} - {b})({a_str} + {b})$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recognize difference of two squares form (A - B)(A + B) = A^2 - B^2", "marks": 1},
            {"step": f"Compute ({a_str})^2 - ({b})^2 = {ans}", "marks": 1},
        ],
        "hints": [
            "The product of a sum and difference of the same two terms yields a difference of squares: $(A - B)(A + B) = A^2 - B^2$.",
            "Notice the outer and inner products cancel out completely ($+Abx - Abx = 0$).",
            f"Result is $({a_str})^2 - ({b})^2 = {ans}$.",
        ],
    }


def arch_37_expand_and_simplify_binomial_product_minus_squared_binomial(rng: random.Random) -> Dict[str, Any]:
    """Compound expansion: (x + p)(x + q) - (x + r)^2."""
    p, q = 3, 5
    r = 2
    # (x+3)(x+5) = x^2 + 8x + 15
    # (x+2)^2 = x^2 + 4x + 4
    # diff = (8 - 4)x + (15 - 4) = 4x + 11
    mid1 = p + q
    last1 = p * q
    mid2 = 2 * r
    last2 = r**2

    final_x = mid1 - mid2
    final_c = last1 - last2
    ans = f"{final_x}x + {final_c}"

    return {
        "subskill": "37_expand_and_simplify_binomial_product_minus_squared_binomial",
        "question_text": (
            f"Expand and simplify completely:\n$$(x + {p})(x + {q}) - (x + {r})^2$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Expand (x + {p})(x + {q}) = x^2 + {mid1}x + {last1}", "marks": 1},
            {"step": f"Expand (x + {r})^2 = x^2 + {mid2}x + {last2}", "marks": 1},
            {"step": f"Subtract polynomials and combine like terms to obtain {ans}", "marks": 1},
        ],
        "hints": [
            f"Expand the first product: $(x + {p})(x + {q}) = x^2 + {mid1}x + {last1}$.",
            f"Expand the second square: $(x + {r})^2 = x^2 + {mid2}x + {last2}$.",
            f"Subtract: $(x^2 + {mid1}x + {last1}) - (x^2 + {mid2}x + {last2}) = {ans}$.",
        ],
    }


def arch_38_divide_monomial_by_monomial_integer_coefficients(rng: random.Random) -> Dict[str, Any]:
    """Divide monomial by monomial with integer quotient: (a x^n) / (b x^m)."""
    b = rng.choice([2, 3, 4, 5])
    q = rng.choice([3, 4, 6, 7])
    a = b * q
    m = rng.choice([1, 2])
    n = m + rng.choice([1, 2, 3])
    diff_p = n - m
    p_str = f"x^{diff_p}" if diff_p > 1 else "x"
    ans = f"{q}{p_str}"

    return {
        "subskill": "38_divide_monomial_by_monomial_integer_coefficients",
        "question_text": (
            f"Simplify the algebraic quotient:\n$$\\frac{{{a}x^{n}}}{{{b}x^{m}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide coefficients: {a} / {b} = {q}", "marks": 1},
            {"step": f"Subtract exponents: x^({n} - {m}) = {p_str}", "marks": 1},
        ],
        "hints": [
            "Divide the numerical coefficients first, then subtract the powers of the variable (laws of exponents).",
            f"Coefficients: $\\frac{{{a}}}{{{b}}} = {q}$.",
            f"Variables: $x^{{{n} - {m}}} = {p_str}$. Result is ${ans}$.",
        ],
    }


def arch_39_divide_monomial_by_monomial_fractional_reduction(rng: random.Random) -> Dict[str, Any]:
    """Divide multi-variable monomial: (a x^2 y) / (b x y)."""
    b = rng.choice([2, 3, 5])
    k = rng.choice([2, 3, 4])
    a = b * k
    ans = f"{k}x"

    return {
        "subskill": "39_divide_monomial_by_monomial_fractional_reduction",
        "question_text": (
            f"Simplify the expression:\n$$\\frac{{{a}x^2 y}}{{{b}x y}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide numbers: {a} / {b} = {k}", "marks": 1},
            {"step": "Simplify x^2 / x = x and y / y = 1", "marks": 1},
        ],
        "hints": [
            f"Divide numbers: ${a} \\div {b} = {k}$.",
            f"Divide variables: $x^2 \\div x = x$, and $y \\div y = 1$.",
            f"The final simplified answer is ${ans}$.",
        ],
    }


def arch_40_divide_binomial_by_integer_constant(rng: random.Random) -> Dict[str, Any]:
    """Divide binomial by an integer constant: (ax + b) / c."""
    c = rng.choice([2, 3, 4, 5])
    m = rng.choice([2, 3, 4])
    k = rng.choice([3, 5, 7])
    a = c * m
    b = c * k
    ans = f"{m}x + {k}"

    return {
        "subskill": "40_divide_binomial_by_integer_constant",
        "question_text": (
            f"Simplify by dividing each term in the numerator by the denominator:\n"
            f"$$\\frac{{{a}x + {b}}}{{{c}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Split fraction: ({a}x / {c}) + ({b} / {c})", "marks": 1},
            {"step": f"Simplify each term to obtain {ans}", "marks": 1},
        ],
        "hints": [
            f"Split into two fractions over the common denominator: $\\frac{{{a}x}}{{{c}}} + \\frac{{{b}}}{{{c}}}$.",
            f"Divide each term: $\\frac{{{a}x}}{{{c}}} = {m}x$ and $\\frac{{{b}}}{{{c}}} = {k}$.",
            f"The answer is ${ans}$.",
        ],
    }


def arch_41_divide_binomial_by_monomial_single_variable(rng: random.Random) -> Dict[str, Any]:
    """Divide binomial by variable monomial: (ax^3 + bx^2) / (cx)."""
    c = rng.choice([2, 3])
    q1 = rng.choice([2, 3, 4])
    q2 = rng.choice([3, 5, 7])
    a = c * q1
    b = c * q2
    ans = f"{q1}x^2 + {q2}x"

    return {
        "subskill": "41_divide_binomial_by_monomial_single_variable",
        "question_text": (
            f"Divide the polynomial by the monomial:\n$$\\frac{{{a}x^3 + {b}x^2}}{{{c}x}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide first term: {a}x^3 / {c}x = {q1}x^2", "marks": 1},
            {"step": f"Divide second term: {b}x^2 / {c}x = {q2}x", "marks": 1},
        ],
        "hints": [
            f"Separate each term: $\\frac{{{a}x^3}}{{{c}x}} + \\frac{{{b}x^2}}{{{c}x}}$.",
            f"Simplify exponents: $x^3 \\div x = x^2$ and $x^2 \\div x = x$.",
            f"Result is ${ans}$.",
        ],
    }


def arch_42_divide_trinomial_by_monomial_single_variable(rng: random.Random) -> Dict[str, Any]:
    """Divide trinomial by monomial: (ax^4 - bx^3 + cx^2) / (dx^2)."""
    d = rng.choice([2, 3])
    q1 = rng.choice([2, 3, 5])
    q2 = rng.choice([3, 4, 6])
    q3 = rng.choice([4, 5, 7])
    a = d * q1
    b = d * q2
    c = d * q3
    ans = f"{q1}x^2 - {q2}x + {q3}"

    return {
        "subskill": "42_divide_trinomial_by_monomial_single_variable",
        "question_text": (
            f"Simplify the algebraic quotient:\n$$\\frac{{{a}x^4 - {b}x^3 + {c}x^2}}{{{d}x^2}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide {a}x^4 / {d}x^2 = {q1}x^2", "marks": 1},
            {"step": f"Divide -{b}x^3 / {d}x^2 = -{q2}x", "marks": 1},
            {"step": f"Divide {c}x^2 / {d}x^2 = {q3}", "marks": 1},
        ],
        "hints": [
            f"Divide each of the three numerator terms by ${d}x^2$.",
            f"Terms become ${q1}x^2$, $-{q2}x$, and ${q3}$.",
            f"Combined answer: ${ans}$.",
        ],
    }


def arch_43_divide_polynomial_by_monomial_two_variables(rng: random.Random) -> Dict[str, Any]:
    """Divide multi-variable polynomial: (a x^2 y + b x y^2) / (c xy)."""
    c = rng.choice([2, 3])
    q1 = rng.choice([3, 4, 5])
    q2 = rng.choice([2, 6, 7])
    a = c * q1
    b = c * q2
    ans = f"{q1}x + {q2}y"

    return {
        "subskill": "43_divide_polynomial_by_monomial_two_variables",
        "question_text": (
            f"Simplify:\n$$\\frac{{{a}x^2 y + {b}x y^2}}{{{c}xy}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide first term: {a}x^2 y / {c}xy = {q1}x", "marks": 1},
            {"step": f"Divide second term: {b}x y^2 / {c}xy = {q2}y", "marks": 1},
        ],
        "hints": [
            f"Write as $\\frac{{{a}x^2 y}}{{{c}xy}} + \\frac{{{b}x y^2}}{{{c}xy}}$.",
            f"First term leaves ${q1}x$ (the $y$'s cancel); second term leaves ${q2}y$ (the $x$'s cancel).",
            f"Result is ${ans}$.",
        ],
    }


def arch_44_simplify_quotient_with_bracket_in_numerator(rng: random.Random) -> Dict[str, Any]:
    """Simplify quotient with factored numerator: (a(x + b)) / c."""
    c = rng.choice([2, 3, 4])
    k = rng.choice([2, 3, 5])
    a = c * k
    b = rng.choice([3, 4, 5])
    ans = f"{k}x + {k * b}"

    return {
        "subskill": "44_simplify_quotient_with_bracket_in_numerator",
        "question_text": (
            f"Simplify by canceling common factors and expanding:\n$$\\frac{{{a}(x + {b})}}{{{c}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Cancel common factor: {a} / {c} = {k}", "marks": 1},
            {"step": f"Distribute {k} into (x + {b}) to get {ans}", "marks": 1},
        ],
        "hints": [
            f"Cancel the integer outside the bracket with the denominator: $\\frac{{{a}}}{{{c}}} = {k}$.",
            f"Now multiply ${k}$ by $(x + {b})$.",
            f"${k} \\times x + {k} \\times {b} = {ans}$.",
        ],
    }


def arch_45_square_root_of_monomial_with_even_exponents(rng: random.Random) -> Dict[str, Any]:
    """Determine the square root of a monomial: sqrt(k^2 x^4)."""
    k = rng.choice([3, 4, 5, 6, 7, 8, 9, 10])
    k2 = k**2
    p = rng.choice([2, 4, 6])
    half_p = p // 2
    p_str = f"x^{half_p}" if half_p > 1 else "x"
    ans = f"{k}{p_str}"

    return {
        "subskill": "45_square_root_of_monomial_with_even_exponents",
        "question_text": (
            f"Simplify the root of the monomial:\n$$\\sqrt{{{k2}x^{p}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Square root of number: sqrt({k2}) = {k}", "marks": 1},
            {"step": f"Halve the exponent: {p} / 2 = {half_p}", "marks": 1},
        ],
        "hints": [
            "Take the square root of the coefficient, and divide the variable's exponent by 2.",
            f"$\\sqrt{{{k2}}} = {k}$ because ${k}^2 = {k2}$.",
            f"$\\sqrt{{x^{{{p}}}}} = x^{{{p} \\div 2}} = {p_str}$. Result is ${ans}$.",
        ],
    }


def arch_46_cube_root_of_monomial_with_multiples_of_three_exponents(rng: random.Random) -> Dict[str, Any]:
    """Determine the cube root of a monomial: cbrt(k^3 x^6)."""
    k = rng.choice([2, 3, 4, 5])
    k3 = k**3
    p = rng.choice([3, 6, 9])
    third_p = p // 3
    p_str = f"x^{third_p}" if third_p > 1 else "x"
    ans = f"{k}{p_str}"

    return {
        "subskill": "46_cube_root_of_monomial_with_multiples_of_three_exponents",
        "question_text": (
            f"Simplify the cube root expression:\n$$\\sqrt[3]{{{k3}x^{p}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Cube root of coefficient: cbrt({k3}) = {k}", "marks": 1},
            {"step": f"Divide exponent by 3: {p} / 3 = {third_p}", "marks": 1},
        ],
        "hints": [
            "Take the cube root of the coefficient, and divide the exponent by 3.",
            f"$\\sqrt[3]{{{k3}}} = {k}$ since ${k}^3 = {k3}$.",
            f"Divide exponent: ${p} \\div 3 = {third_p}$, so $x^{{{third_p}}}$. Answer is ${ans}$.",
        ],
    }


def arch_47_error_analysis_diagnosing_squared_binomial_middle_term_omission(rng: random.Random) -> Dict[str, Any]:
    """Diagnose missing middle term in (x + a)^2."""
    a = rng.choice([3, 4, 5, 6, 7])
    a2 = a**2
    correct_mid = 2 * a
    ans = f"+{correct_mid}x"

    return {
        "subskill": "47_error_analysis_diagnosing_squared_binomial_middle_term_omission",
        "question_text": (
            f"A learner wrote the following expansion in a test:\n"
            f"$$(x + {a})^2 = x^2 + {a2}$$\n\n"
            f"The learner omitted the middle term. State the **missing middle term** (including its sign and variable, e.g. +{correct_mid}x)."
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify middle term of (x + a)^2 is 2ax = {ans}", "marks": 1},
        ],
        "hints": [
            f"Remember $(x + {a})^2 = (x + {a})(x + {a}) = x^2 + {a}x + {a}x + {a2}$.",
            f"The middle term comes from adding the outer and inner products: ${a}x + {a}x = +{correct_mid}x$.",
            f"The missing middle term is ${ans}$.",
        ],
    }


def arch_48_error_analysis_diagnosing_sign_error_in_subtraction_of_polynomial(rng: random.Random) -> Dict[str, Any]:
    """Diagnose sign error when distributing negative into (bx - c)."""
    b = rng.choice([3, 4, 5])
    c = rng.choice([6, 7, 8])
    ans = f"-{b}x + {c}"

    return {
        "subskill": "48_error_analysis_diagnosing_sign_error_in_subtraction_of_polynomial",
        "question_text": (
            f"A student incorrectly expanded $-({b}x - {c})$ as $-{b}x - {c}$.\n\n"
            f"Write down the **correct expansion**."
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Distribute negative sign: -({b}x) - (-{c}) = -{b}x + {c}", "marks": 1},
        ],
        "hints": [
            "A negative outside brackets multiplies both terms inside: $-1 \\times {b}x = -{b}x$ and $-1 \\times (-{c}) = +{c}$.",
            "Negative multiplied by negative gives a positive sign.",
            f"The correct expansion is ${ans}$.",
        ],
    }


def arch_49_geometric_application_area_of_rectangle_with_binomial_dimensions(rng: random.Random) -> Dict[str, Any]:
    """Area of rectangle with binomial sides (x + a) and (x + b) in expanded form."""
    seed = rng.randint(1, 1_000_000)
    a = rng.choice([2, 3, 4])
    b = rng.choice([5, 6, 7])
    len_str = f"x + {b}"
    wid_str = f"x + {a}"
    mid = a + b
    last = a * b
    ans = f"x^2 + {mid}x + {last}"
    svg = draw_algebraic_rectangle_svg(len_str, wid_str, seed=seed)

    return {
        "subskill": "49_geometric_application_area_of_rectangle_with_binomial_dimensions",
        "question_text": (
            f"A rectangular garden has length $({len_str})\\text{{ m}}$ and width $({wid_str})\\text{{ m}}$.\n\n"
            f"Write an expanded and simplified algebraic expression for the **area** of the garden in terms of $x$."
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Write formula for area: ({len_str})({wid_str})", "marks": 1},
            {"step": f"Expand using FOIL: x^2 + {a}x + {b}x + {last}", "marks": 1},
            {"step": f"Combine like terms to get {ans}", "marks": 1},
        ],
        "hints": [
            f"$\\text{{Area}} = \\text{{length}} \\times \\text{{width}} = ({len_str})({wid_str})$.",
            f"Use FOIL: $x^2 + {a}x + {b}x + {last}$.",
            f"Combine like terms: ${ans}$.",
        ],
    }


def arch_50_compound_multi_step_algebraic_expansion_and_evaluation_challenge(rng: random.Random) -> Dict[str, Any]:
    """Multi-step algebraic challenge: expand 2(x + a)(x - a) + 3(x + b) and evaluate at x = 2."""
    a = rng.choice([2, 3])
    b = rng.choice([3, 4])
    x_val = 2
    # 2(x^2 - a^2) + 3x + 3b = 2x^2 + 3x + (3b - 2a^2)
    # Evaluate at x = 2:
    val = 2 * (x_val**2 - a**2) + 3 * (x_val + b)

    return {
        "subskill": "50_compound_multi_step_algebraic_expansion_and_evaluation_challenge",
        "question_text": (
            f"Consider the compound expression:\n"
            f"$$E(x) = 2(x - {a})(x + {a}) + 3(x + {b})$$\n\n"
            f"Evaluate the exact numerical value of $E({x_val})$."
        ),
        "correct_answer": str(val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Evaluate difference of squares at x = {x_val}: 2(({x_val})^2 - {a**2}) = 2({x_val**2 - a**2}) = {2 * (x_val**2 - a**2)}", "marks": 1},
            {"step": f"Evaluate linear part at x = {x_val}: 3({x_val} + {b}) = 3({x_val + b}) = {3 * (x_val + b)}", "marks": 1},
            {"step": f"Sum components: {val}", "marks": 1},
        ],
        "hints": [
            f"You can substitute $x = {x_val}$ directly into each part.",
            f"First part: $2({x_val} - {a})({x_val} + {a}) = 2({x_val**2 - a**2}) = {2 * (x_val**2 - a**2)}$.",
            f"Second part: $3({x_val} + {b}) = {3 * (x_val + b)}$. Sum is ${val}$.",
        ],
    }
