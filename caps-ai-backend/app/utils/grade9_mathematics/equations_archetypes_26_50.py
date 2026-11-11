"""Grade 9 Mathematics - Algebraic Equations 1 Archetypes (26 to 50).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Equations 1.md
  - curriculum_docs/Mathematics_Gr9/Equations Studio.md

Covers:
  - Contextual word problems (age problems, taxi/fare costs, perimeter contexts)
  - Quadratic equations solved by factorisation (common factor, difference of squares, trinomials, RHS rearrangement)
  - Exponential equations (base 2, 3, 5, 10, linear exponents, negative exponents)
  - Simple algebraic fraction equations (cross multiplication and single denominators)
  - Error analysis: transposition sign error, division by variable losing zero root
  - Geometric applications (Pythagoras theorem equation)
  - Compound multi-step equation challenges
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_word_problem_age_relation(rng: random.Random) -> Dict[str, Any]:
    """Word problem: Father's age is 3 times child's age plus 4."""
    child_age = rng.choice([10, 11, 12, 13])
    father_age = 3 * child_age + 4

    return {
        "subskill": "26_word_problem_age_relation",
        "question_text": (
            f"A father is currently ${father_age}$ years old. His age is $4$ years more than three times his daughter's age.\n\n"
            f"Set up an equation and find the daughter's age:"
        ),
        "correct_answer": str(child_age),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up equation: 3x + 4 = {father_age}", "marks": 1},
            {"step": f"Solve: 3x = {father_age - 4} => x = {child_age}", "marks": 1},
        ],
        "hints": [
            "Let the daughter's age be $x$.",
            f"Equation: $3x + 4 = {father_age}$.",
            f"$3x = {father_age - 4} \\implies x = {child_age}$.",
        ],
    }


def arch_27_word_problem_taxi_fare_linear(rng: random.Random) -> Dict[str, Any]:
    """Word problem: Taxi fare is base fee + rate per km."""
    base = 30
    rate = 12
    km = rng.choice([8, 10, 15, 20])
    total = base + rate * km

    return {
        "subskill": "27_word_problem_taxi_fare_linear",
        "question_text": (
            f"A metered taxi charges a base call-out fee of $\\text{{R}}{base}$ plus $\\text{{R}}{rate}$ per kilometre travelled.\n"
            f"If a passenger's total fare came to $\\text{{R}}{total}$, how many kilometres ($d$) did they travel?"
        ),
        "correct_answer": str(km),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up equation: {base} + {rate}d = {total}", "marks": 1},
            {"step": f"Solve: {rate}d = {total - base} => d = {km}", "marks": 1},
        ],
        "hints": [
            f"Cost equation: ${base} + {rate}d = {total}$.",
            f"Subtract base fee: ${rate}d = {total - base}$.",
            f"Divide by rate: $d = {km}\\text{{ km}}$.",
        ],
    }


def arch_28_word_problem_perimeter_isosceles_triangle(rng: random.Random) -> Dict[str, Any]:
    """Word problem: Isosceles triangle with two equal sides of length 2x and base 10."""
    x_val = rng.choice([5, 6, 7])
    # sides: 2x, 2x, 10. Perimeter = 4x + 10
    p = 4 * x_val + 10

    return {
        "subskill": "28_word_problem_perimeter_isosceles_triangle",
        "question_text": (
            f"An isosceles triangle has two equal sides of length $2x\\text{{ cm}}$ and a base of $10\\text{{ cm}}$.\n"
            f"If the perimeter of the triangle is ${p}\\text{{ cm}}$, solve for $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up perimeter equation: 2x + 2x + 10 = {p}", "marks": 1},
            {"step": f"Solve: 4x = {p - 10} => x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Perimeter is the sum of all three sides: $2x + 2x + 10 = {p}$.",
            f"$4x + 10 = {p} \\implies 4x = {p - 10}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_29_quadratic_equation_factorised_two_positive_roots(rng: random.Random) -> Dict[str, Any]:
    """Factorised quadratic: (x - p)(x - q) = 0. Find the larger root."""
    p = rng.choice([2, 3])
    q = rng.choice([5, 7, 8])
    ans = max(p, q)

    return {
        "subskill": "29_quadratic_equation_factorised_two_positive_roots",
        "question_text": (
            f"Solve the quadratic equation:\n$$(x - {p})(x - {q}) = 0$$\n\n"
            f"State the **larger** of the two solutions for $x$:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply zero product property: x - {p} = 0 or x - {q} = 0", "marks": 1},
            {"step": f"Roots are x = {p} or x = {q}; larger root is {ans}", "marks": 1},
        ],
        "hints": [
            "Zero Product Property: If $A \\times B = 0$, then $A = 0$ or $B = 0$.",
            f"$x - {p} = 0 \\implies x = {p}$, or $x - {q} = 0 \\implies x = {q}$.",
            f"The larger solution is ${ans}$.",
        ],
    }


def arch_30_quadratic_equation_factorised_mixed_roots(rng: random.Random) -> Dict[str, Any]:
    """Factorised quadratic with mixed signs: (x + p)(x - q) = 0. Find negative root."""
    p = rng.choice([3, 4, 6])
    q = rng.choice([2, 5, 7])
    ans = -p

    return {
        "subskill": "30_quadratic_equation_factorised_mixed_roots",
        "question_text": (
            f"Solve the equation:\n$$(x + {p})(x - {q}) = 0$$\n\n"
            f"State the **negative solution** for $x$:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set x + {p} = 0 => x = -{p}", "marks": 1},
        ],
        "hints": [
            f"Set each factor to zero: $x + {p} = 0$ or $x - {q} = 0$.",
            f"$x = -{p}$ or $x = {q}$.",
            f"The negative root is ${ans}$.",
        ],
    }


def arch_31_quadratic_equation_common_factor(rng: random.Random) -> Dict[str, Any]:
    """Quadratic: x^2 - kx = 0. Find the non-zero root."""
    k = rng.choice([4, 6, 7, 8, 9])

    return {
        "subskill": "31_quadratic_equation_common_factor",
        "question_text": (
            f"Solve the equation by factorisation:\n$$x^2 - {k}x = 0$$\n\n"
            f"State the **non-zero solution** for $x$:"
        ),
        "correct_answer": str(k),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise by taking out common factor x: x(x - {k}) = 0", "marks": 1},
            {"step": f"Identify non-zero root: x = {k}", "marks": 1},
        ],
        "hints": [
            f"Factorise: $x(x - {k}) = 0$.",
            f"This gives $x = 0$ or $x - {k} = 0 \\implies x = {k}$.",
            f"The non-zero solution is ${k}$.",
        ],
    }


def arch_32_quadratic_equation_difference_of_squares_positive_root(rng: random.Random) -> Dict[str, Any]:
    """Difference of squares equation: x^2 - k^2 = 0. State positive root."""
    k = rng.choice([5, 6, 7, 8, 9, 10, 11])
    k2 = k**2

    return {
        "subskill": "32_quadratic_equation_difference_of_squares_positive_root",
        "question_text": (
            f"Solve for $x$:\n$$x^2 - {k2} = 0$$\n\n"
            f"State the **positive root**:"
        ),
        "correct_answer": str(k),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise: (x - {k})(x + {k}) = 0", "marks": 1},
            {"step": f"Positive root is x = {k}", "marks": 1},
        ],
        "hints": [
            f"Factorise as a difference of squares: $(x - {k})(x + {k}) = 0$.",
            f"Solutions are $x = {k}$ or $x = -{k}$.",
            f"The positive root is ${k}$.",
        ],
    }


def arch_33_quadratic_equation_difference_of_squares_with_coefficient(rng: random.Random) -> Dict[str, Any]:
    """Solve 4x^2 - 36 = 0. State positive root."""
    ans = 3

    return {
        "subskill": "33_quadratic_equation_difference_of_squares_with_coefficient",
        "question_text": (
            f"Solve the quadratic equation:\n$$4x^2 - 36 = 0$$\n\n"
            f"State the positive solution for $x$:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Divide by 4 or factorise: 4(x^2 - 9) = 0", "marks": 1},
            {"step": f"Solve x^2 = 9 => x = {ans}", "marks": 1},
        ],
        "hints": [
            "Divide both sides by 4: $x^2 - 9 = 0$.",
            "Factorise: $(x - 3)(x + 3) = 0$.",
            f"The positive solution is ${ans}$.",
        ],
    }


def arch_34_quadratic_equation_trinomial_standard_form(rng: random.Random) -> Dict[str, Any]:
    """Solve x^2 - (p+q)x + pq = 0. State larger root."""
    p = rng.choice([2, 3])
    q = rng.choice([4, 5, 6])
    mid = p + q
    last = p * q
    ans = max(p, q)

    return {
        "subskill": "34_quadratic_equation_trinomial_standard_form",
        "question_text": (
            f"Solve the quadratic equation by factorisation:\n"
            f"$$x^2 - {mid}x + {last} = 0$$\n\n"
            f"State the **larger** of the two roots:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise trinomial: (x - {p})(x - {q}) = 0", "marks": 1},
            {"step": f"State larger root: {ans}", "marks": 1},
        ],
        "hints": [
            f"Factorise: two numbers multiplying to ${last}$ and adding to $-{mid}$ are $-{p}$ and $-{q}$.",
            f"$(x - {p})(x - {q}) = 0 \\implies x = {p}$ or $x = {q}$.",
            f"The larger root is ${ans}$.",
        ],
    }


def arch_35_quadratic_equation_trinomial_mixed_signs(rng: random.Random) -> Dict[str, Any]:
    """Solve x^2 + (p-q)x - pq = 0. State positive root."""
    p = 5
    q = 3
    # x^2 + 2x - 15 = 0 => (x + 5)(x - 3) = 0 => x = 3 or -5
    ans = q

    return {
        "subskill": "35_quadratic_equation_trinomial_mixed_signs",
        "question_text": (
            f"Solve the equation:\n$$x^2 + 2x - 15 = 0$$\n\n"
            f"Enter the **positive solution** for $x$:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Factorise: (x + 5)(x - 3) = 0", "marks": 1},
            {"step": f"Identify positive root: x = {ans}", "marks": 1},
        ],
        "hints": [
            "Factorise the trinomial: $(x + 5)(x - 3) = 0$.",
            "This gives $x = -5$ or $x = 3$.",
            f"The positive root is ${ans}$.",
        ],
    }


def arch_36_quadratic_equation_rhs_non_zero_rearrange(rng: random.Random) -> Dict[str, Any]:
    """Solve x^2 + 5x = 24 by standard form rearrangement. State positive root."""
    ans = 3

    return {
        "subskill": "36_quadratic_equation_rhs_non_zero_rearrange",
        "question_text": (
            f"Solve for $x$ by first writing the quadratic in standard form $ax^2 + bx + c = 0$:\n"
            f"$$x^2 + 5x = 24$$\n\n"
            f"Enter the positive root:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Rearrange to standard form: x^2 + 5x - 24 = 0", "marks": 1},
            {"step": f"Factorise (x + 8)(x - 3) = 0 to find positive root x = {ans}", "marks": 1},
        ],
        "hints": [
            "Before factorising, the equation must equal zero! Subtract 24: $x^2 + 5x - 24 = 0$.",
            "Factorise: $(x + 8)(x - 3) = 0$.",
            f"Roots are $x = -8$ or $x = 3$. Positive root is ${ans}$.",
        ],
    }


def arch_37_quadratic_equation_perfect_square(rng: random.Random) -> Dict[str, Any]:
    """Solve x^2 - 2kx + k^2 = 0. Single repeated root."""
    k = rng.choice([4, 6, 7, 8])
    mid = 2 * k
    last = k**2

    return {
        "subskill": "37_quadratic_equation_perfect_square",
        "question_text": (
            f"Solve the quadratic equation:\n$$x^2 - {mid}x + {last} = 0$$\n\n"
            f"State the single repeated root for $x$:"
        ),
        "correct_answer": str(k),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise as perfect square: (x - {k})^2 = 0", "marks": 1},
            {"step": f"State root x = {k}", "marks": 1},
        ],
        "hints": [
            f"Factorise: $(x - {k})(x - {k}) = (x - {k})^2 = 0$.",
            f"Set $x - {k} = 0$.",
            f"$x = {k}$.",
        ],
    }


def arch_38_exponential_equation_base_two_integer(rng: random.Random) -> Dict[str, Any]:
    """Solve 2^x = 2^k."""
    k = rng.choice([3, 4, 5, 6])
    val = 2**k

    return {
        "subskill": "38_exponential_equation_base_two_integer",
        "question_text": (
            f"Solve the exponential equation:\n$$2^x = {val}$$"
        ),
        "correct_answer": str(k),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Express {val} as power of 2: 2^{k}", "marks": 1},
            {"step": f"Equate exponents: x = {k}", "marks": 1},
        ],
        "hints": [
            f"Express the right-hand side in base 2: ${val} = 2^{{{k}}}$.",
            f"Since the bases are equal ($2^x = 2^{{{k}}}$), equate the exponents.",
            f"$x = {k}$.",
        ],
    }


def arch_39_exponential_equation_base_three_integer(rng: random.Random) -> Dict[str, Any]:
    """Solve 3^x = 3^k."""
    k = rng.choice([2, 3, 4])
    val = 3**k

    return {
        "subskill": "39_exponential_equation_base_three_integer",
        "question_text": (
            f"Solve for $x$:\n$$3^x = {val}$$"
        ),
        "correct_answer": str(k),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Express {val} as 3^{k}", "marks": 1},
            {"step": f"Equate exponents: x = {k}", "marks": 1},
        ],
        "hints": [
            f"${val} = 3^{{{k}}}$.",
            f"If $3^x = 3^{{{k}}}$, then $x = {k}$.",
        ],
    }


def arch_40_exponential_equation_base_five_integer(rng: random.Random) -> Dict[str, Any]:
    """Solve 5^x = 5^k."""
    k = rng.choice([2, 3, 4])
    val = 5**k

    return {
        "subskill": "40_exponential_equation_base_five_integer",
        "question_text": (
            f"Solve the exponential equation:\n$$5^x = {val}$$"
        ),
        "correct_answer": str(k),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Express {val} as 5^{k}", "marks": 1},
            {"step": f"State x = {k}", "marks": 1},
        ],
        "hints": [
            f"${val} = 5^{{{k}}}$.",
            f"$x = {k}$.",
        ],
    }


def arch_41_exponential_equation_linear_exponent(rng: random.Random) -> Dict[str, Any]:
    """Solve 2^{x + 1} = 2^k."""
    k = rng.choice([4, 5, 6])
    val = 2**k
    ans = k - 1

    return {
        "subskill": "41_exponential_equation_linear_exponent",
        "question_text": (
            f"Solve for $x$:\n$$2^{{x + 1}} = {val}$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Rewrite RHS: 2^{{x + 1}} = 2^{k}", "marks": 1},
            {"step": f"Equate exponents: x + 1 = {k} => x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Write ${val}$ as a power of 2: ${val} = 2^{{{k}}}$.",
            f"Equate exponents: $x + 1 = {k}$.",
            f"$x = {k} - 1 = {ans}$.",
        ],
    }


def arch_42_exponential_equation_negative_exponent(rng: random.Random) -> Dict[str, Any]:
    """Solve 3^x = 1/9 => x = -2."""
    ans = -2

    return {
        "subskill": "42_exponential_equation_negative_exponent",
        "question_text": (
            f"Solve for $x$:\n$$3^x = \\frac{{1}}{{9}}$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Rewrite 1/9 as 1/3^2 = 3^(-2)", "marks": 1},
            {"step": f"Equate exponents: x = {ans}", "marks": 1},
        ],
        "hints": [
            "Use the negative exponent rule: $\\frac{1}{a^n} = a^{-n}$.",
            "$\\frac{1}{9} = \\frac{1}{3^2} = 3^{-2}$.",
            f"Therefore, $3^x = 3^{{-2}} \\implies x = {ans}$.",
        ],
    }


def arch_43_exponential_equation_fractional_base(rng: random.Random) -> Dict[str, Any]:
    """Solve (1/2)^x = 8 => x = -3."""
    ans = -3

    return {
        "subskill": "43_exponential_equation_fractional_base",
        "question_text": (
            f"Solve for $x$:\n$$\\left(\\frac{{1}}{{2}}\\right)^x = 8$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Rewrite LHS as 2^(-x) and RHS as 2^3", "marks": 1},
            {"step": f"Equate exponents: -x = 3 => x = {ans}", "marks": 1},
        ],
        "hints": [
            "$\\frac{1}{2} = 2^{-1}$, so $\\left(\\frac{1}{2}\\right)^x = 2^{-x}$.",
            "$8 = 2^3$.",
            f"$2^{{-x}} = 2^3 \\implies -x = 3 \\implies x = {ans}$.",
        ],
    }


def arch_44_exponential_equation_base_ten_powers(rng: random.Random) -> Dict[str, Any]:
    """Solve 10^{2x} = 10000 => 2x = 4 => x = 2."""
    ans = 2

    return {
        "subskill": "44_exponential_equation_base_ten_powers",
        "question_text": (
            f"Solve the equation:\n$$10^{{2x}} = 10\\,000$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Rewrite 10 000 as 10^4", "marks": 1},
            {"step": f"Equate exponents: 2x = 4 => x = {ans}", "marks": 1},
        ],
        "hints": [
            "$10\\,000 = 10^4$.",
            "Equate exponents: $2x = 4$.",
            f"$x = {ans}$.",
        ],
    }


def arch_45_equation_with_algebraic_fraction_cross_multiplication(rng: random.Random) -> Dict[str, Any]:
    """Solve (x + 2)/3 = (x - 1)/2 => 2(x + 2) = 3(x - 1) => x = 7."""
    ans = 7

    return {
        "subskill": "45_equation_with_algebraic_fraction_cross_multiplication",
        "question_text": (
            f"Solve for $x$ using cross-multiplication:\n"
            f"$$\\frac{{x + 2}}{{3}} = \\frac{{x - 1}}{{2}}$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Cross-multiply: 2(x + 2) = 3(x - 1)", "marks": 1},
            {"step": "Expand: 2x + 4 = 3x - 3", "marks": 1},
            {"step": f"Solve: x = {ans}", "marks": 1},
        ],
        "hints": [
            "Multiply across denominators: $2(x + 2) = 3(x - 1)$.",
            "Expand brackets: $2x + 4 = 3x - 3$.",
            f"Rearrange: $4 + 3 = 3x - 2x \\implies x = {ans}$.",
        ],
    }


def arch_46_equation_with_single_fraction_term(rng: random.Random) -> Dict[str, Any]:
    """Solve (2x - 3)/5 = 3 => 2x - 3 = 15 => x = 9."""
    ans = 9

    return {
        "subskill": "46_equation_with_single_fraction_term",
        "question_text": (
            f"Solve for $x$:\n$$\\frac{{2x - 3}}{{5}} = 3$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Multiply both sides by 5: 2x - 3 = 15", "marks": 1},
            {"step": f"Solve: 2x = 18 => x = {ans}", "marks": 1},
        ],
        "hints": [
            "Multiply both sides by 5 to clear the fraction: $2x - 3 = 3 \\times 5 = 15$.",
            "Add 3: $2x = 18$.",
            f"Divide by 2: $x = {ans}$.",
        ],
    }


def arch_47_error_analysis_diagnosing_sign_error_in_transposition(rng: random.Random) -> Dict[str, Any]:
    """Diagnose sign error when transposing: 3x + 5 = 20 solved as 3x = 25."""
    ans = 5

    return {
        "subskill": "47_error_analysis_diagnosing_sign_error_in_transposition",
        "question_text": (
            f"A learner wrote:\n"
            f"$$3x + 5 = 20$$\n"
            f"$$3x = 20 + 5 = 25$$\n"
            f"Identify the error and calculate the **correct value** of $x$:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that +5 should become -5 when transposed: 3x = 20 - 5 = 15", "marks": 1},
            {"step": f"Calculate correct value: x = {ans}", "marks": 1},
        ],
        "hints": [
            "When moving a term across the equals sign, its sign must invert: $+5$ becomes $-5$.",
            "Correct step: $3x = 20 - 5 = 15$.",
            f"$x = {ans}$.",
        ],
    }


def arch_48_error_analysis_diagnosing_division_by_zero_variable(rng: random.Random) -> Dict[str, Any]:
    """Explain why dividing by x in x^2 = 5x loses root x = 0."""
    ans = 0

    return {
        "subskill": "48_error_analysis_diagnosing_division_by_zero_variable",
        "question_text": (
            f"In solving $x^2 = 5x$, a learner divided both sides by $x$ to get $x = 5$.\n\n"
            f"By dividing by $x$, the learner lost a valid solution. State the **lost solution** for $x$:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify the lost root from dividing by variable: x = {ans}", "marks": 1},
        ],
        "hints": [
            "You cannot divide by a variable that could equal zero.",
            "Correct method: $x^2 - 5x = 0 \\implies x(x - 5) = 0$.",
            f"This gives two solutions: $x = 5$ or $x = {ans}$. The lost solution is ${ans}$.",
        ],
    }


def arch_49_geometric_application_pythagoras_equation(rng: random.Random) -> Dict[str, Any]:
    """Solve right triangle equation: x^2 + 12^2 = 13^2 => x = 5."""
    ans = 5

    return {
        "subskill": "49_geometric_application_pythagoras_equation",
        "question_text": (
            f"In a right-angled triangle, the hypotenuse is $13\\text{{ cm}}$ and one side is $12\\text{{ cm}}$.\n"
            f"Using the Theorem of Pythagoras $x^2 + 12^2 = 13^2$, solve for the positive side length $x$ (in cm):"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Evaluate squares: x^2 + 144 = 169", "marks": 1},
            {"step": f"Subtract: x^2 = 25 => x = {ans}", "marks": 1},
        ],
        "hints": [
            "$x^2 + 144 = 169$.",
            "$x^2 = 169 - 144 = 25$.",
            f"$x = \\sqrt{{25}} = {ans}$.",
        ],
    }


def arch_50_compound_multi_step_equation_solving_challenge(rng: random.Random) -> Dict[str, Any]:
    """Compound equation: 3(2x - 1) - 2(x + 4) = 17 => 6x - 3 - 2x - 8 = 17 => 4x - 11 = 17 => 4x = 28 => x = 7."""
    ans = 7

    return {
        "subskill": "50_compound_multi_step_equation_solving_challenge",
        "question_text": (
            f"Solve the compound linear equation:\n"
            f"$$3(2x - 1) - 2(x + 4) = 17$$\n\n"
            f"Find $x$."
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Expand brackets: 6x - 3 - 2x - 8 = 17", "marks": 1},
            {"step": "Combine like terms: 4x - 11 = 17", "marks": 1},
            {"step": f"Solve: 4x = 28 => x = {ans}", "marks": 1},
        ],
        "hints": [
            "Expand both brackets carefully: $6x - 3 - 2x - 8 = 17$.",
            "Combine like terms: $4x - 11 = 17$.",
            f"Add 11: $4x = 28 \\implies x = {ans}$.",
        ],
    }
