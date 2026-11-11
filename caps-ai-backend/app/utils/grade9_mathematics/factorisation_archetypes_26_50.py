"""Grade 9 Mathematics - Factorisation & Algebraic Expressions 2 Archetypes (26 to 50).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 1/06. Algebraic expressions 2.md
  - curriculum_docs/Mathematics_Gr9/Algebraic Expressions Studio.md

Covers:
  - Grouping with rearrangement
  - Simplifying algebraic fractions via factorisation (common factor, difference of squares, trinomials)
  - Fraction operations: multiplication, division with reciprocals, addition/subtraction with LCD
  - Sign-change cancellation in fractions
  - Area model tiles (SVG) and geometric applications (rectangle/square dimensions)
  - Error analysis: illegal fraction canceling, sum of squares misconception, wrong trinomial factors
  - Numerical evaluation via factorisation shortcuts and compound multi-step challenges
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .factorisation_svg import (
    draw_factorisation_area_model_svg,
    draw_factorisation_rectangle_svg,
)


def arch_26_factorise_by_grouping_requiring_rearrangement(rng: random.Random) -> Dict[str, Any]:
    """Grouping where terms are jumbled: x^2 + ky + kx + xy = (x + k)(x + y)."""
    k = rng.choice([2, 3, 5, 7])
    expr = f"x^2 + {k}y + {k}x + xy"
    ans = f"(x + {k})(x + y)"

    return {
        "subskill": "26_factorise_by_grouping_requiring_rearrangement",
        "question_text": (
            f"Rearrange the terms and factorise by grouping:\n$${expr}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Rearrange terms: (x^2 + kx) + (xy + ky)", "marks": 1},
            {"step": f"Factor pairs: x(x + {k}) + y(x + {k})", "marks": 1},
            {"step": f"State final factors: {ans}", "marks": 1},
        ],
        "hints": [
            f"Group terms that share common factors: $(x^2 + {k}x) + (xy + {k}y)$.",
            f"Factorise each pair: $x(x + {k}) + y(x + {k})$.",
            f"Take out the common bracket $(x + {k})$: ${ans}$.",
        ],
    }


def arch_27_algebraic_fraction_simplify_monomial_over_monomial(rng: random.Random) -> Dict[str, Any]:
    """Simplify monomial fraction: (a x^3 y) / (b x y) = q x^2."""
    b = rng.choice([2, 3, 4])
    q = rng.choice([3, 4, 5, 7])
    a = b * q
    ans = f"{q}x^2"

    return {
        "subskill": "27_algebraic_fraction_simplify_monomial_over_monomial",
        "question_text": (
            f"Simplify the algebraic fraction:\n$$\\frac{{{a}x^3 y}}{{{b}xy}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide coefficients: {a} / {b} = {q}", "marks": 1},
            {"step": "Simplify variables: x^3 / x = x^2 and y / y = 1", "marks": 1},
        ],
        "hints": [
            f"Divide numbers: ${a} \\div {b} = {q}$.",
            "Divide powers of $x$: $x^{3 - 1} = x^2$. The $y$ in numerator and denominator cancels out ($y \\div y = 1$).",
            f"Result is ${ans}$.",
        ],
    }


def arch_28_algebraic_fraction_common_factor_numerator_cancel(rng: random.Random) -> Dict[str, Any]:
    """Simplify fraction by extracting HCF from numerator and canceling denominator: (kx + kc) / k."""
    k = rng.choice([2, 3, 4, 5, 6])
    c = rng.choice([3, 4, 7, 8])
    kc = k * c
    ans = f"x + {c}"

    return {
        "subskill": "28_algebraic_fraction_common_factor_numerator_cancel",
        "question_text": (
            f"Simplify the fraction by factorising the numerator first:\n$$\\frac{{{k}x + {kc}}}{{{k}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise numerator: {k}(x + {c})", "marks": 1},
            {"step": f"Cancel common factor {k} to obtain {ans}", "marks": 1},
        ],
        "hints": [
            f"Extract the common factor ${k}$ from the numerator: $\\frac{{{k}(x + {c})}}{{{k}}}$.",
            f"Cancel the factor ${k}$ in numerator and denominator.",
            f"The simplified answer is ${ans}$.",
        ],
    }


def arch_29_algebraic_fraction_common_factor_cancel_binomial(rng: random.Random) -> Dict[str, Any]:
    """Simplify fraction where entire binomial cancels: (kx + kc) / (x + c) = k."""
    k = rng.choice([3, 4, 5, 7, 8])
    c = rng.choice([2, 5, 6, 9])
    kc = k * c

    return {
        "subskill": "29_algebraic_fraction_common_factor_cancel_binomial",
        "question_text": (
            f"Simplify the algebraic fraction completely:\n$$\\frac{{{k}x + {kc}}}{{x + {c}}}$$"
        ),
        "correct_answer": str(k),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise numerator: {k}(x + {c})", "marks": 1},
            {"step": f"Cancel (x + {c}) leaving {k}", "marks": 1},
        ],
        "hints": [
            f"Factor the numerator: ${k}x + {kc} = {k}(x + {c})$.",
            f"Notice that the binomial $(x + {c})$ is identical in both numerator and denominator.",
            f"Canceling $(x + {c})$ leaves ${k}$.",
        ],
    }


def arch_30_algebraic_fraction_difference_of_squares_cancel(rng: random.Random) -> Dict[str, Any]:
    """Difference of squares in numerator canceling denominator: (x^2 - k^2) / (x - k) = x + k."""
    k = rng.choice([3, 4, 5, 6, 7, 8, 9])
    k2 = k**2
    ans = f"x + {k}"

    return {
        "subskill": "30_algebraic_fraction_difference_of_squares_cancel",
        "question_text": (
            f"Simplify the fraction by factorising:\n$$\\frac{{x^2 - {k2}}}{{x - {k}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise numerator as difference of squares: (x - {k})(x + {k})", "marks": 1},
            {"step": f"Cancel (x - {k}) leaving {ans}", "marks": 1},
        ],
        "hints": [
            f"Factor the numerator using difference of squares: $x^2 - {k2} = (x - {k})(x + {k})$.",
            f"Cancel the common bracket $(x - {k})$ from numerator and denominator.",
            f"The result is ${ans}$.",
        ],
    }


def arch_31_algebraic_fraction_difference_of_squares_cancel_plus(rng: random.Random) -> Dict[str, Any]:
    """Difference of squares canceling (x + k): (x^2 - k^2) / (x + k) = x - k."""
    k = rng.choice([2, 4, 6, 7, 8, 10])
    k2 = k**2
    ans = f"x - {k}"

    return {
        "subskill": "31_algebraic_fraction_difference_of_squares_cancel_plus",
        "question_text": (
            f"Simplify:\n$$\\frac{{x^2 - {k2}}}{{x + {k}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise numerator: (x - {k})(x + {k})", "marks": 1},
            {"step": f"Cancel (x + {k}) to leave {ans}", "marks": 1},
        ],
        "hints": [
            f"Numerator factors to $(x - {k})(x + {k})$.",
            f"Cancel $(x + {k})$: leaving ${ans}$.",
        ],
    }


def arch_32_algebraic_fraction_trinomial_cancel_numerator(rng: random.Random) -> Dict[str, Any]:
    """Factorise trinomial in numerator and cancel: (x^2 + (p+q)x + pq) / (x + p) = x + q."""
    p = rng.choice([2, 3, 4])
    q = rng.choice([5, 6, 7])
    mid = p + q
    last = p * q
    ans = f"x + {q}"

    return {
        "subskill": "32_algebraic_fraction_trinomial_cancel_numerator",
        "question_text": (
            f"Simplify the algebraic fraction by factorising the trinomial:\n$$\\frac{{x^2 + {mid}x + {last}}}{{x + {p}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise numerator: (x + {p})(x + {q})", "marks": 1},
            {"step": f"Cancel (x + {p}) to get {ans}", "marks": 1},
        ],
        "hints": [
            f"Factorise the numerator: two numbers that multiply to ${last}$ and add to ${mid}$ are ${p}$ and ${q}$.",
            f"Numerator becomes $(x + {p})(x + {q})$.",
            f"Cancel the $(x + {p})$ bracket with the denominator: ${ans}$.",
        ],
    }


def arch_33_algebraic_fraction_trinomial_cancel_denominator(rng: random.Random) -> Dict[str, Any]:
    """Factorise trinomial in denominator and cancel: (x - p) / (x^2 - (p+q)x + pq) = 1/(x - q)."""
    p = rng.choice([2, 3])
    q = rng.choice([4, 5, 6])
    mid = p + q
    last = p * q
    ans = f"1/(x - {q})"

    return {
        "subskill": "33_algebraic_fraction_trinomial_cancel_denominator",
        "question_text": (
            f"Simplify the fraction completely:\n$$\\frac{{x - {p}}}{{x^2 - {mid}x + {last}}}$$\n\n"
            f"(Write your answer in the form 1/(x - {q}))."
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise denominator: (x - {p})(x - {q})", "marks": 1},
            {"step": f"Cancel (x - {p}) leaving 1 in numerator: {ans}", "marks": 1},
        ],
        "hints": [
            f"Factorise the denominator: $x^2 - {mid}x + {last} = (x - {p})(x - {q})$.",
            f"Cancel $(x - {p})$ from both top and bottom.",
            f"Remember: when the entire numerator cancels, $1$ remains in the numerator: ${ans}$.",
        ],
    }


def arch_34_algebraic_fraction_trinomial_over_trinomial_cancel(rng: random.Random) -> Dict[str, Any]:
    """Factorise trinomial over trinomial: ((x+p)(x+q)) / ((x+p)(x-r)) = (x+q)/(x-r)."""
    p = rng.choice([2, 3])
    q = rng.choice([4, 5])
    r = rng.choice([1, 6])

    num_mid = p + q
    num_last = p * q
    den_mid = p - r
    den_last = p * r

    s_den_mid = f"- {abs(den_mid)}" if den_mid < 0 else f"+ {den_mid}"
    ans = f"(x + {q})/(x - {r})"

    return {
        "subskill": "34_algebraic_fraction_trinomial_over_trinomial_cancel",
        "question_text": (
            f"Simplify the fraction by factorising both numerator and denominator:\n"
            f"$$\\frac{{x^2 + {num_mid}x + {num_last}}}{{x^2 {s_den_mid}x - {den_last}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise numerator: (x + {p})(x + {q})", "marks": 1},
            {"step": f"Factorise denominator: (x + {p})(x - {r})", "marks": 1},
            {"step": f"Cancel common factor (x + {p}) to obtain {ans}", "marks": 1},
        ],
        "hints": [
            f"Numerator factors to $(x + {p})(x + {q})$.",
            f"Denominator factors to $(x + {p})(x - {r})$.",
            f"Cancel the common bracket $(x + {p})$: ${ans}$.",
        ],
    }


def arch_35_algebraic_fraction_sign_change_cancellation(rng: random.Random) -> Dict[str, Any]:
    """Simplify (x - k) / (k - x) = -1."""
    k = rng.choice([3, 4, 7, 8, 12])

    return {
        "subskill": "35_algebraic_fraction_sign_change_cancellation",
        "question_text": (
            f"Simplify the algebraic fraction completely:\n$$\\frac{{x - {k}}}{{{k} - x}}$$"
        ),
        "correct_answer": "-1",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factor out -1 from denominator: ({k} - x) = -(x - {k})", "marks": 1},
            {"step": f"Cancel (x - {k}) to leave -1", "marks": 1},
        ],
        "hints": [
            f"Notice that ${k} - x = -(x - {k})$.",
            f"Rewrite the fraction: $\\frac{{x - {k}}}{{-(x - {k})}}$.",
            f"Canceling $(x - {k})$ leaves $\\frac{{1}}{{-1}} = -1$.",
        ],
    }


def arch_36_algebraic_fraction_multiplication_cancel_common_factors(rng: random.Random) -> Dict[str, Any]:
    """Multiply algebraic fractions with cancellation: (x+2)/(x-3) * (x-3)/(x+5) = (x+2)/(x+5)."""
    p, q, r = 2, 3, 5
    ans = f"(x + {p})/(x + {r})"

    return {
        "subskill": "36_algebraic_fraction_multiplication_cancel_common_factors",
        "question_text": (
            f"Multiply and simplify the fractions:\n"
            f"$$\\frac{{x + {p}}}{{x - {q}}} \\times \\frac{{x - {q}}}{{x + {r}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Cancel diagonal common factor (x - {q})", "marks": 1},
            {"step": f"Multiply remaining numerators and denominators: {ans}", "marks": 1},
        ],
        "hints": [
            f"Observe the common factor $(x - {q})$ in numerator and denominator across the multiplication.",
            "Cross-cancel $(x - {q})$.",
            f"Result: ${ans}$.",
        ],
    }


def arch_37_algebraic_fraction_division_multiply_by_reciprocal(rng: random.Random) -> Dict[str, Any]:
    """Divide algebraic fractions: (x^2 - k^2)/(x + m) / (x - k)/(x + m) = x + k."""
    k = rng.choice([2, 3, 4, 5])
    m = rng.choice([6, 7, 8])
    k2 = k**2
    ans = f"x + {k}"

    return {
        "subskill": "37_algebraic_fraction_division_multiply_by_reciprocal",
        "question_text": (
            f"Perform the division and simplify:\n"
            f"$$\\frac{{x^2 - {k2}}}{{x + {m}}} \\div \\frac{{x - {k}}}{{x + {m}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Invert divisor and multiply: ((x^2 - {k2}) / (x + {m})) * ((x + {m}) / (x - {k}))", "marks": 1},
            {"step": f"Factorise difference of squares: (x - {k})(x + {k})", "marks": 1},
            {"step": f"Cancel common factors to obtain {ans}", "marks": 1},
        ],
        "hints": [
            f"Change division to multiplication by inverting the second fraction: $\\times \\frac{{x + {m}}}{{x - {k}}}$.",
            f"Factorise $x^2 - {k2} = (x - {k})(x + {k})$.",
            f"Cancel $(x + {m})$ and $(x - {k})$, leaving ${ans}$.",
        ],
    }


def arch_38_algebraic_fraction_addition_like_denominators(rng: random.Random) -> Dict[str, Any]:
    """Add fractions with like denominators: 2x/(x+c) + 2c/(x+c) = 2."""
    c = rng.choice([3, 4, 5, 6])
    ans = "2"

    return {
        "subskill": "38_algebraic_fraction_addition_like_denominators",
        "question_text": (
            f"Add the algebraic fractions and simplify:\n"
            f"$$\\frac{{2x}}{{x + {c}}} + \\frac{{{2 * c}}}{{x + {c}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Combine over common denominator: (2x + {2 * c}) / (x + {c})", "marks": 1},
            {"step": f"Factorise numerator: 2(x + {c})", "marks": 1},
            {"step": "Cancel (x + c) leaving 2", "marks": 1},
        ],
        "hints": [
            f"Since denominators are identical, combine numerators: $\\frac{{2x + {2 * c}}}{{x + {c}}}$.",
            f"Factorise the numerator: $2(x + {c})$.",
            f"Cancel $(x + {c})$: result is ${ans}$.",
        ],
    }


def arch_39_algebraic_fraction_subtraction_like_denominators(rng: random.Random) -> Dict[str, Any]:
    """Subtract fractions with like denominators: x^2/(x-k) - k^2/(x-k) = x + k."""
    k = rng.choice([3, 4, 5, 7])
    k2 = k**2
    ans = f"x + {k}"

    return {
        "subskill": "39_algebraic_fraction_subtraction_like_denominators",
        "question_text": (
            f"Subtract and simplify:\n"
            f"$$\\frac{{x^2}}{{x - {k}}} - \\frac{{{k2}}}{{x - {k}}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Combine over common denominator: (x^2 - {k2}) / (x - {k})", "marks": 1},
            {"step": f"Factorise difference of squares: (x - {k})(x + {k})", "marks": 1},
            {"step": f"Cancel (x - {k}) to get {ans}", "marks": 1},
        ],
        "hints": [
            f"Combine numerators: $\\frac{{x^2 - {k2}}}{{x - {k}}}$.",
            f"Factorise numerator: $(x - {k})(x + {k})$.",
            f"Cancel $(x - {k})$: ${ans}$.",
        ],
    }


def arch_40_algebraic_fraction_addition_monomial_denominators_lcd(rng: random.Random) -> Dict[str, Any]:
    """Add fractions with different monomial denominators: a/x + b/(2x) = (2a + b)/(2x)."""
    a = rng.choice([2, 3, 5])
    b = rng.choice([1, 3, 7])
    num = 2 * a + b
    ans = f"{num}/(2x)"

    return {
        "subskill": "40_algebraic_fraction_addition_monomial_denominators_lcd",
        "question_text": (
            f"Add the fractions by finding the Lowest Common Denominator (LCD):\n"
            f"$$\\frac{{{a}}}{{x}} + \\frac{{{b}}}{{2x}}$$\n\n"
            f"(Write your answer as a single simplified fraction, e.g. {num}/(2x))."
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify LCD = 2x", "marks": 1},
            {"step": f"Convert first fraction: ({a} * 2) / (2x) = {2 * a} / (2x)", "marks": 1},
            {"step": f"Add numerators: {num} / (2x)", "marks": 1},
        ],
        "hints": [
            "The denominators are $x$ and $2x$. The Lowest Common Denominator is $2x$.",
            f"Multiply top and bottom of the first fraction by 2: $\\frac{{{2 * a}}}{{2x}}$.",
            f"Add numerators: $\\frac{{{2 * a} + {b}}}{{2x}} = {ans}$.",
        ],
    }


def arch_41_algebraic_fraction_subtraction_monomial_denominators_lcd(rng: random.Random) -> Dict[str, Any]:
    """Subtract fractions with monomial denominators: a/(2x) - b/(4x) = (2a - b)/(4x)."""
    a = rng.choice([3, 5, 7])
    b = rng.choice([1, 3])
    num = 2 * a - b
    ans = f"{num}/(4x)"

    return {
        "subskill": "41_algebraic_fraction_subtraction_monomial_denominators_lcd",
        "question_text": (
            f"Subtract and express as a single fraction in simplest form:\n"
            f"$$\\frac{{{a}}}{{2x}} - \\frac{{{b}}}{{4x}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify LCD = 4x", "marks": 1},
            {"step": f"Convert first fraction: {2 * a} / (4x)", "marks": 1},
            {"step": f"Subtract numerators: {ans}", "marks": 1},
        ],
        "hints": [
            "The LCD for $2x$ and $4x$ is $4x$.",
            f"Multiply top and bottom of first fraction by 2: $\\frac{{{2 * a}}}{{4x}}$.",
            f"Subtract: $\\frac{{{2 * a} - {b}}}{{4x}} = {ans}$.",
        ],
    }


def arch_42_algebraic_tile_area_model_find_missing_binomial_dimension(rng: random.Random) -> Dict[str, Any]:
    """Visual area model (SVG) to find missing binomial dimension."""
    seed = rng.randint(1, 1_000_000)
    p = rng.choice([2, 3, 4])
    q = rng.choice([3, 5, 7])
    # Model shows x^2, qx, px, pq
    svg = draw_factorisation_area_model_svg(
        dim_top_1="x",
        dim_top_2=f"+{q}",
        dim_left_1="x",
        dim_left_2=f"+{p}",
        cell_tl="x²",
        cell_tr=f"{q}x",
        cell_bl=f"{p}x",
        cell_br=str(p * q),
        seed=seed,
    )
    ans = f"x + {q}"

    return {
        "subskill": "42_algebraic_tile_area_model_find_missing_binomial_dimension",
        "question_text": (
            f"The area model below represents the factorisation of the trinomial $x^2 + {p + q}x + {p * q}$.\n\n"
            f"If the vertical side is $(x + {p})$, state the **horizontal top binomial dimension**:"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Identify top dimension from cells x^2 and {q}x: {ans}", "marks": 1},
        ],
        "hints": [
            f"Inspect the top row of the area model: it contains cells of area $x^2$ and ${q}x$.",
            f"Since the height is $x$, the top widths must be $x$ and ${q}$.",
            f"The horizontal binomial is ${ans}$.",
        ],
    }


def arch_43_geometric_application_find_width_given_area_and_length(rng: random.Random) -> Dict[str, Any]:
    """Given rectangular area x^2 + (p+q)x + pq and length x + p, find width x + q."""
    seed = rng.randint(1, 1_000_000)
    p = rng.choice([2, 3, 4])
    q = rng.choice([5, 6, 7])
    mid = p + q
    last = p * q
    area_str = f"x^2 + {mid}x + {last}"
    length_str = f"x + {p}"
    ans = f"x + {q}"
    svg = draw_factorisation_rectangle_svg(area_str, length_str, "?", seed=seed)

    return {
        "subskill": "43_geometric_application_find_width_given_area_and_length",
        "question_text": (
            f"A rectangular field has an area of $({area_str})\\text{{ m}}^2$ and a length of $({length_str})\\text{{ m}}$.\n\n"
            f"Determine an algebraic expression for the **breadth** of the field in terms of $x$."
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Factorise area: ({length_str})({ans})", "marks": 1},
            {"step": f"Identify missing breadth: {ans}", "marks": 1},
        ],
        "hints": [
            "Breadth = Area / Length.",
            f"Factorise the area trinomial: $x^2 + {mid}x + {last} = ({length_str})(x + {q})$.",
            f"Divide by length $({length_str})$ to find the breadth: ${ans}$.",
        ],
    }


def arch_44_geometric_application_square_area_to_side_length(rng: random.Random) -> Dict[str, Any]:
    """Find side length of square given area as a perfect square: x^2 + 2kx + k^2."""
    seed = rng.randint(1, 1_000_000)
    k = rng.choice([3, 4, 5, 6, 8])
    mid = 2 * k
    last = k**2
    area_str = f"x^2 + {mid}x + {last}"
    ans = f"x + {k}"
    svg = draw_factorisation_rectangle_svg(area_str, "?", "?", seed=seed)

    return {
        "subskill": "44_geometric_application_square_area_to_side_length",
        "question_text": (
            f"A square solar panel has an area given by:\n$$\\text{{Area}} = ({area_str})\\text{{ cm}}^2$$\n\n"
            f"State the **side length** of the square in terms of $x$."
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Recognize perfect square trinomial (x + {k})^2", "marks": 1},
            {"step": f"Take square root to find side length: {ans}", "marks": 1},
        ],
        "hints": [
            "For a square, $\\text{{Area}} = \\text{{side}}^2$, so $\\text{{side}} = \\sqrt{{\\text{{Area}}}}$.",
            f"Factorise the area: $x^2 + {mid}x + {last} = (x + {k})^2$.",
            f"The side length is ${ans}\\text{{ cm}}$.",
        ],
    }


def arch_45_error_analysis_diagnosing_illegal_fraction_term_canceling(rng: random.Random) -> Dict[str, Any]:
    """Diagnose illegal canceling of terms across addition in fractions."""
    k = rng.choice([3, 4, 5, 6])

    return {
        "subskill": "45_error_analysis_diagnosing_illegal_fraction_term_canceling",
        "question_text": (
            f"A learner attempts to simplify the fraction:\n"
            f"$$\\frac{{x + {k}}}{{{k}}}$$\n"
            f"by canceling the number ${k}$ and writing the answer as $x$.\n\n"
            f"Is the learner's simplification **correct** or **incorrect**?"
        ),
        "correct_answer": "incorrect",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that individual terms cannot be canceled across addition: incorrect", "marks": 1},
        ],
        "hints": [
            "In a fraction, only common factors of the entire numerator and entire denominator can be canceled.",
            f"In $x + {k}$, the ${k}$ is a term connected by addition, not a factor multiplying the entire numerator.",
            "The learner's method is incorrect.",
        ],
    }


def arch_46_error_analysis_diagnosing_difference_of_squares_sign_error(rng: random.Random) -> Dict[str, Any]:
    """Diagnose why sum of squares x^2 + 16 cannot be factored over reals."""
    k = rng.choice([4, 9, 16, 25, 36])

    return {
        "subskill": "46_error_analysis_diagnosing_difference_of_squares_sign_error",
        "question_text": (
            f"A student claims that the expression $x^2 + {k}$ can be factorised as a difference of two squares.\n\n"
            f"Can the sum of two squares $x^2 + {k}$ be factorised into real linear binomials? "
            f"(Answer **yes** or **no**)."
        ),
        "correct_answer": "no",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that sum of squares cannot be factorised over real numbers: no", "marks": 1},
        ],
        "hints": [
            "The difference of squares rule applies ONLY when there is a minus sign between the terms ($A^2 - B^2$).",
            f"$(x - \\sqrt{{{k}}})(x + \\sqrt{{{k}}}) = x^2 - {k}$, NOT $x^2 + {k}$.",
            "The answer is no.",
        ],
    }


def arch_47_error_analysis_diagnosing_wrong_factors_in_trinomial(rng: random.Random) -> Dict[str, Any]:
    """Correct the factors of x^2 + 7x + 12 when learner chose 6 and 2."""
    expr = "x^2 + 7x + 12"
    ans = "(x + 3)(x + 4)"

    return {
        "subskill": "47_error_analysis_diagnosing_wrong_factors_in_trinomial",
        "question_text": (
            f"A learner factorised $${expr}$$ as $(x + 6)(x + 2)$ because $6 \\times 2 = 12$.\n\n"
            f"State the **correct factorisation** that also adds up to $7x$:"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recognize that 6 + 2 = 8 != 7", "marks": 1},
            {"step": f"Provide correct factors 3 and 4: {ans}", "marks": 1},
        ],
        "hints": [
            "The factors must multiply to 12 AND add to 7.",
            "$6 + 2 = 8$, which is incorrect. But $3 + 4 = 7$ and $3 \\times 4 = 12$.",
            f"The correct factorisation is ${ans}$.",
        ],
    }


def arch_48_evaluate_factored_expression_numerical_shortcut(rng: random.Random) -> Dict[str, Any]:
    """Use difference of squares to compute a^2 - b^2 without calculator."""
    a = rng.choice([51, 52, 53, 54, 55])
    b = rng.choice([49, 48, 47, 46, 45])
    diff = a - b
    sum_val = a + b
    val = diff * sum_val

    return {
        "subskill": "48_evaluate_factored_expression_numerical_shortcut",
        "question_text": (
            f"Use the difference of two squares identity $a^2 - b^2 = (a - b)(a + b)$ to evaluate:\n"
            f"$${a}^2 - {b}^2$$\n\n"
            f"Calculate the exact numerical value."
        ),
        "correct_answer": str(val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply identity: ({a} - {b})({a} + {b}) = ({diff})({sum_val})", "marks": 1},
            {"step": f"Multiply: {diff} * {sum_val} = {val}", "marks": 1},
        ],
        "hints": [
            f"Apply $(a - b)(a + b)$: $({a} - {b})({a} + {b})$.",
            f"Calculate each bracket: ${a} - {b} = {diff}$ and ${a} + {b} = {sum_val}$.",
            f"Multiply: ${diff} \\times {sum_val} = {val}$.",
        ],
    }


def arch_49_compound_factorisation_difference_of_squares_with_binomial_terms(rng: random.Random) -> Dict[str, Any]:
    """Difference of squares where first term is a binomial: (x + a)^2 - b^2."""
    a = 1
    b = rng.choice([3, 4, 5])
    b2 = b**2
    p1 = a - b
    p2 = a + b
    s_p1 = f"- {abs(p1)}" if p1 < 0 else f"+ {p1}"
    ans = f"(x {s_p1})(x + {p2})"

    return {
        "subskill": "49_compound_factorisation_difference_of_squares_with_binomial_terms",
        "question_text": (
            f"Factorise completely using the difference of two squares:\n$$(x + {a})^2 - {b2}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply difference of squares: [(x + {a}) - {b}][(x + {a}) + {b}]", "marks": 1},
            {"step": f"Simplify each bracket: {ans}", "marks": 1},
        ],
        "hints": [
            f"Treat $(x + {a})$ as $A$ and $\\sqrt{{{b2}}} = {b}$ as $B$.",
            f"Apply $(A - B)(A + B)$: $[(x + {a}) - {b}][(x + {a}) + {b}]$.",
            f"Simplify inside each bracket: $(x {s_p1})(x + {p2})$.",
        ],
    }


def arch_50_compound_multi_step_factorisation_and_simplification_challenge(rng: random.Random) -> Dict[str, Any]:
    """Compound algebraic fraction challenge: (x^2 - 9)/(x + 3) * (x + 2)/(x - 3)."""
    ans = "x + 2"

    return {
        "subskill": "50_compound_multi_step_factorisation_and_simplification_challenge",
        "question_text": (
            f"Simplify the compound expression completely:\n"
            f"$$\\frac{{x^2 - 9}}{{x + 3}} \\times \\frac{{x + 2}}{{x - 3}}$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Factorise x^2 - 9 into (x - 3)(x + 3)", "marks": 1},
            {"step": "Cancel common factors (x + 3) and (x - 3) across the product", "marks": 1},
            {"step": f"State final simplified result: {ans}", "marks": 1},
        ],
        "hints": [
            "Factorise $x^2 - 9 = (x - 3)(x + 3)$.",
            "Substitute into the product: $\\frac{{(x - 3)(x + 3)}}{{x + 3}} \\times \\frac{{x + 2}}{{x - 3}}$.",
            f"Cancel $(x + 3)$ and $(x - 3)$ from top and bottom. What remains is ${ans}$.",
        ],
    }
