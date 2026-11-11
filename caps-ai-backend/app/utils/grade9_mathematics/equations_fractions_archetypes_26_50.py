"""Grade 9 Mathematics - Equations 2 (Quadratics, Formulas & Word Problems) Archetypes (26 to 50).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Equations 2.md
  - curriculum_docs/Mathematics_Gr9/Equations Studio.md

Covers:
  - Error analysis: negative distribution in algebraic fractions
  - Quadratic equations solved by factorisation:
    - Zero product property (already factored, mixed signs, leading coefficients)
    - Common factor extraction (x^2 - kx = 0, ax^2 + bx = 0, negative leading terms)
    - Difference of two squares (x^2 - a^2 = 0, a^2*x^2 - b^2 = 0, common factor first)
    - Standard trinomials x^2 + bx + c = 0 (both positive roots, both negative roots, opposite signs)
    - Perfect square trinomials
    - Quadratic equations requiring rearrangement to standard form
    - Expanding brackets first then factorising
    - Geometric area model leading to quadratic equation (SVG)
    - Error analysis: dividing by variable and losing zero root
  - Literal equations & formula rearrangement with fractions:
    - Velocity formula: v = d/t (solve for t)
    - Area of a triangle: A = 1/2*b*h (solve for h)
    - Temperature formula: C = 5/9*(F - 32) (solve for F)
    - Linear rational equation: y = (ax + b)/c (solve for x)
  - Contextual word problems with fractions:
    - Fractional age relationships
    - Number problems with fractions
    - Speed, distance, and time round-trip equations
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .equations_fractions_svg import draw_quadratic_rectangle_area_svg


def arch_26_error_analysis_sign_error_distributing_negative_fraction(rng: random.Random) -> Dict[str, Any]:
    """Error analysis: student forgot to change sign when distributing negative bracket."""
    d1, d2, lcd = 2, 3, 6
    a = rng.choice([1, 2, 3])
    b = rng.choice([2, 4, 6])
    k = rng.choice([4, 5, 6])
    # Correct: 3(x + a) - 2(x - b) = 6k => 3x + 3a - 2x + 2b = 6k => x + 3a + 2b = 6k => x = 6k - 3a - 2b
    correct_x = 6 * k - 3 * a - 2 * b

    return {
        "subskill": "26_error_analysis_sign_error_distributing_negative_fraction",
        "question_text": (
            f"A learner attempted to solve the following equation:\n"
            f"$$\\frac{{x + {a}}}{{2}} - \\frac{{x - {b}}}{{3}} = {k}$$\n\n"
            f"**Learner's Working:**\n"
            f"Step 1: $3(x + {a}) - 2(x - {b}) = {lcd * k}$\n"
            f"Step 2: $3x + {3 * a} - 2x - {2 * b} = {lcd * k}$\n"
            f"Step 3: $x + {3 * a - 2 * b} = {lcd * k} \\implies x = {lcd * k - (3 * a - 2 * b)}$\n\n"
            f"Explain the sign error made in Step 2, and determine the correct value of $x$."
        ),
        "correct_answer": str(correct_x),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify error: -2 * (-{b}) equals +{2 * b}, not -{2 * b}", "marks": 1},
            {"step": f"Correct distribution: 3x + {3 * a} - 2x + {2 * b} = {lcd * k}", "marks": 1},
            {"step": f"Accurate final answer: x = {correct_x}", "marks": 1},
        ],
        "hints": [
            f"In Step 2, distributing $-2$ into $-(x - {b})$ gives $-2x + {2 * b}$ because a negative times a negative is positive.",
            f"The correct expanded equation is $x + {3 * a} + {2 * b} = {lcd * k}$.",
            f"$x = {lcd * k} - {3 * a} - {2 * b} = {correct_x}$.",
        ],
    }


def arch_27_quadratic_zero_product_already_factorised(rng: random.Random) -> Dict[str, Any]:
    """Solve already factorised quadratic (x - p)(x - q) = 0. State larger root."""
    p = rng.choice([2, 3, 4])
    q = rng.choice([6, 7, 8, 9])
    larger_root = max(p, q)

    return {
        "subskill": "27_quadratic_zero_product_already_factorised",
        "question_text": (
            f"Solve the quadratic equation using the Zero Product Property:\n"
            f"$$(x - {p})(x - {q}) = 0$$\n\n"
            f"State the **larger root** (larger solution for $x$):"
        ),
        "correct_answer": str(larger_root),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Apply zero product rule: x - {p} = 0 or x - {q} = 0", "marks": 1},
            {"step": f"Identify solutions x = {p} or x = {q}; larger is {larger_root}", "marks": 1},
        ],
        "hints": [
            "If the product of two factors is zero, at least one factor must equal zero.",
            f"$x - {p} = 0 \\implies x = {p}$, or $x - {q} = 0 \\implies x = {q}$.",
            f"The larger solution is ${larger_root}$.",
        ],
    }


def arch_28_quadratic_zero_product_mixed_signs(rng: random.Random) -> Dict[str, Any]:
    """Solve (x + p)(x - q) = 0. State positive root."""
    p = rng.choice([2, 3, 4, 5])
    q = rng.choice([6, 7, 8, 9])

    return {
        "subskill": "28_quadratic_zero_product_mixed_signs",
        "question_text": (
            f"Solve for $x$:\n"
            f"$$(x + {p})(x - {q}) = 0$$\n\n"
            f"State the **positive solution** for $x$:"
        ),
        "correct_answer": str(q),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set each factor to 0: x + {p} = 0 or x - {q} = 0", "marks": 1},
            {"step": f"State solutions x = -{p} or x = {q}; positive is {q}", "marks": 1},
        ],
        "hints": [
            f"Set each bracket equal to zero: $x + {p} = 0$ or $x - {q} = 0$.",
            f"$x = -{p}$ or $x = {q}$.",
            f"The positive root is ${q}$.",
        ],
    }


def arch_29_quadratic_zero_product_with_leading_coefficient(rng: random.Random) -> Dict[str, Any]:
    """Solve (2x - p)(x + q) = 0. State positive root."""
    # 2x - p = 0 => x = p/2. Let p be an even number so root is integer
    p_half = rng.choice([2, 3, 4, 5])
    p = 2 * p_half
    q = rng.choice([3, 5, 7])

    return {
        "subskill": "29_quadratic_zero_product_with_leading_coefficient",
        "question_text": (
            f"Solve the equation for $x$:\n"
            f"$$(2x - {p})(x + {q}) = 0$$\n\n"
            f"State the **positive solution** for $x$:"
        ),
        "correct_answer": str(p_half),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set factors to zero: 2x - {p} = 0 or x + {q} = 0", "marks": 1},
            {"step": f"Solve for x: 2x = {p} => x = {p_half}", "marks": 1},
        ],
        "hints": [
            f"Set each factor to zero: $2x - {p} = 0$ or $x + {q} = 0$.",
            f"$2x = {p} \\implies x = {p} \\div 2 = {p_half}$, or $x = -{q}$.",
            f"The positive solution is ${p_half}$.",
        ],
    }


def arch_30_quadratic_common_factor_monomial(rng: random.Random) -> Dict[str, Any]:
    """Solve x^2 - ax = 0. State non-zero root."""
    a = rng.choice([3, 4, 5, 6, 7, 8, 9])

    return {
        "subskill": "30_quadratic_common_factor_monomial",
        "question_text": (
            f"Solve the quadratic equation by factorisation:\n"
            f"$$x^2 - {a}x = 0$$\n\n"
            f"State the **non-zero root**:"
        ),
        "correct_answer": str(a),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Take out highest common factor x: x(x - {a}) = 0", "marks": 1},
            {"step": f"State solutions x = 0 or x = {a}; non-zero root is {a}", "marks": 1},
        ],
        "hints": [
            f"Never divide across by $x$! Factor out the common factor $x$: $x(x - {a}) = 0$.",
            f"By the zero product rule, $x = 0$ or $x - {a} = 0 \\implies x = {a}$.",
            f"The non-zero root is ${a}$.",
        ],
    }


def arch_31_quadratic_common_factor_with_coefficient(rng: random.Random) -> Dict[str, Any]:
    """Solve 3x^2 - bx = 0 where b is multiple of 3. State non-zero root."""
    c = rng.choice([2, 3, 4, 5, 6])
    b = 3 * c

    return {
        "subskill": "31_quadratic_common_factor_with_coefficient",
        "question_text": (
            f"Solve the quadratic equation:\n"
            f"$$3x^2 - {b}x = 0$$\n\n"
            f"State the **non-zero solution** for $x$:"
        ),
        "correct_answer": str(c),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise by taking out common factor 3x: 3x(x - {c}) = 0", "marks": 1},
            {"step": f"State non-zero root: x = {c}", "marks": 1},
        ],
        "hints": [
            f"Factor out $3x$: $3x(x - {c}) = 0$.",
            f"Either $3x = 0 \\implies x = 0$, or $x - {c} = 0 \\implies x = {c}$.",
            f"The non-zero solution is ${c}$.",
        ],
    }


def arch_32_quadratic_common_factor_negative_leading(rng: random.Random) -> Dict[str, Any]:
    """Solve -x^2 + ax = 0. State non-zero root."""
    a = rng.choice([4, 5, 6, 7, 8, 9])

    return {
        "subskill": "32_quadratic_common_factor_negative_leading",
        "question_text": (
            f"Solve for $x$:\n"
            f"$$-x^2 + {a}x = 0$$\n\n"
            f"State the **positive solution**:"
        ),
        "correct_answer": str(a),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply by -1 or factorise: -x(x - {a}) = 0", "marks": 1},
            {"step": f"Solve: x = 0 or x = {a}; positive solution is {a}", "marks": 1},
        ],
        "hints": [
            f"Multiply through by $-1$ to get $x^2 - {a}x = 0$, or factor out $-x$: $-x(x - {a}) = 0$.",
            f"The solutions are $x = 0$ or $x = {a}$.",
            f"The positive root is ${a}$.",
        ],
    }


def arch_33_quadratic_difference_of_squares_basic(rng: random.Random) -> Dict[str, Any]:
    """Solve x^2 - a^2 = 0. State positive root."""
    a = rng.choice([4, 5, 6, 7, 8, 9, 10, 12])
    a2 = a * a

    return {
        "subskill": "33_quadratic_difference_of_squares_basic",
        "question_text": (
            f"Solve the equation using the difference of two squares:\n"
            f"$$x^2 - {a2} = 0$$\n\n"
            f"State the **positive root**:"
        ),
        "correct_answer": str(a),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise as difference of squares: (x - {a})(x + {a}) = 0", "marks": 1},
            {"step": f"State solutions x = {a} or x = -{a}; positive root is {a}", "marks": 1},
        ],
        "hints": [
            f"Factorise: $(x - {a})(x + {a}) = 0$.",
            f"Set each factor to zero: $x = {a}$ or $x = -{a}$.",
            f"The positive root is ${a}$.",
        ],
    }


def arch_34_quadratic_difference_of_squares_with_coefficient(rng: random.Random) -> Dict[str, Any]:
    """Solve 4x^2 - b^2 = 0. State positive root."""
    # (2x - b)(2x + b) = 0 => x = b/2. Pick even b
    b_half = rng.choice([2, 3, 4, 5])
    b = 2 * b_half
    b2 = b * b

    return {
        "subskill": "34_quadratic_difference_of_squares_with_coefficient",
        "question_text": (
            f"Solve the quadratic equation:\n"
            f"$$4x^2 - {b2} = 0$$\n\n"
            f"State the **positive solution** for $x$:"
        ),
        "correct_answer": str(b_half),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise difference of squares: (2x - {b})(2x + {b}) = 0", "marks": 1},
            {"step": f"Solve for positive root: 2x = {b} => x = {b_half}", "marks": 1},
        ],
        "hints": [
            f"Factorise as $(2x - {b})(2x + {b}) = 0$.",
            f"Set $2x - {b} = 0 \\implies 2x = {b} \\implies x = {b_half}$.",
            f"The positive solution is ${b_half}$.",
        ],
    }


def arch_35_quadratic_difference_of_squares_common_factor_first(rng: random.Random) -> Dict[str, Any]:
    """Solve kx^2 - k*a^2 = 0 by taking out common factor first. State positive root."""
    k = rng.choice([2, 3, 5])
    a = rng.choice([3, 4, 5, 6])
    ka2 = k * a * a

    return {
        "subskill": "35_quadratic_difference_of_squares_common_factor_first",
        "question_text": (
            f"Solve for $x$ by factorising:\n"
            f"$${k}x^2 - {ka2} = 0$$\n\n"
            f"State the **positive root**:"
        ),
        "correct_answer": str(a),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Extract common factor {k}: {k}(x^2 - {a * a}) = 0", "marks": 1},
            {"step": f"Factorise difference of squares: {k}(x - {a})(x + {a}) = 0", "marks": 1},
            {"step": f"Identify positive root: x = {a}", "marks": 1},
        ],
        "hints": [
            f"Extract the common factor of ${k}$ first: ${k}(x^2 - {a * a}) = 0$.",
            f"Factorise the bracket as a difference of squares: ${k}(x - {a})(x + {a}) = 0$.",
            f"The roots are $x = \\pm {a}$; the positive root is ${a}$.",
        ],
    }


def arch_36_quadratic_trinomial_standard_both_positive(rng: random.Random) -> Dict[str, Any]:
    """Solve x^2 - (p+q)x + pq = 0. State larger root."""
    p = rng.choice([2, 3, 4])
    q = rng.choice([5, 6, 7, 8])
    b = p + q
    c = p * q
    larger_root = max(p, q)

    return {
        "subskill": "36_quadratic_trinomial_standard_both_positive",
        "question_text": (
            f"Solve the trinomial quadratic equation by factorisation:\n"
            f"$$x^2 - {b}x + {c} = 0$$\n\n"
            f"State the **larger root**:"
        ),
        "correct_answer": str(larger_root),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise trinomial: (x - {p})(x - {q}) = 0", "marks": 1},
            {"step": f"State solutions x = {p} or x = {q}; larger is {larger_root}", "marks": 1},
        ],
        "hints": [
            f"Find two numbers that multiply to $+{c}$ and add up to $-{b}$.",
            f"The factors are $-{p}$ and $-{q}$: $(x - {p})(x - {q}) = 0$.",
            f"Solutions are $x = {p}$ or $x = {q}$. The larger root is ${larger_root}$.",
        ],
    }


def arch_37_quadratic_trinomial_standard_both_negative(rng: random.Random) -> Dict[str, Any]:
    """Solve x^2 + (p+q)x + pq = 0. State root with larger magnitude."""
    p = rng.choice([1, 2, 3])
    q = rng.choice([4, 5, 6, 7])
    b = p + q
    c = p * q
    ans = -max(p, q)

    return {
        "subskill": "37_quadratic_trinomial_standard_both_negative",
        "question_text": (
            f"Solve for $x$ by factorising:\n"
            f"$$x^2 + {b}x + {c} = 0$$\n\n"
            f"State the **smaller solution** (most negative root) for $x$:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise into two binomials: (x + {p})(x + {q}) = 0", "marks": 1},
            {"step": f"State solutions x = -{p} or x = -{q}; smaller root is {ans}", "marks": 1},
        ],
        "hints": [
            f"Find two numbers that multiply to $+{c}$ and add up to $+{b}$.",
            f"The factors are $+{p}$ and $+{q}$: $(x + {p})(x + {q}) = 0$.",
            f"Roots are $x = -{p}$ or $x = -{q}$. The smaller value is ${ans}$.",
        ],
    }


def arch_38_quadratic_trinomial_standard_opposite_signs(rng: random.Random) -> Dict[str, Any]:
    """Solve x^2 + bx - c = 0 where factors have opposite signs. State positive root."""
    pos_root = rng.choice([5, 6, 7, 8])
    neg_root = rng.choice([2, 3, 4])
    # (x - pos_root)(x + neg_root) = 0 => x^2 - (pos_root - neg_root)x - pos_root*neg_root = 0
    diff = pos_root - neg_root
    prod = pos_root * neg_root
    sign_str = f"- {diff}x" if diff > 0 else f"+ {-diff}x"

    return {
        "subskill": "38_quadratic_trinomial_standard_opposite_signs",
        "question_text": (
            f"Solve the quadratic equation:\n"
            f"$$x^2 {sign_str} - {prod} = 0$$\n\n"
            f"State the **positive root**:"
        ),
        "correct_answer": str(pos_root),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise: (x - {pos_root})(x + {neg_root}) = 0", "marks": 1},
            {"step": f"State solutions x = {pos_root} or x = -{neg_root}; positive is {pos_root}", "marks": 1},
        ],
        "hints": [
            f"Find two factors of $-{prod}$ that add up to $-{diff}$.",
            f"The factors are $-{pos_root}$ and $+{neg_root}$: $(x - {pos_root})(x + {neg_root}) = 0$.",
            f"The positive root is ${pos_root}$.",
        ],
    }


def arch_39_quadratic_trinomial_perfect_square(rng: random.Random) -> Dict[str, Any]:
    """Solve perfect square quadratic: x^2 - 2ax + a^2 = 0."""
    a = rng.choice([3, 4, 5, 6, 7, 8, 9])
    two_a = 2 * a
    a2 = a * a

    return {
        "subskill": "39_quadratic_trinomial_perfect_square",
        "question_text": (
            f"Solve the quadratic equation for $x$:\n"
            f"$$x^2 - {two_a}x + {a2} = 0$$\n\n"
            f"State the value of the equal roots:"
        ),
        "correct_answer": str(a),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Factorise as perfect square: (x - {a})^2 = 0", "marks": 1},
            {"step": f"State repeated root: x = {a}", "marks": 1},
        ],
        "hints": [
            f"Notice that the first term is $x^2$ and the constant term is ${a}^2$.",
            f"Factorise as a perfect square: $(x - {a})^2 = 0$.",
            f"$x - {a} = 0 \\implies x = {a}$.",
        ],
    }


def arch_40_quadratic_rearrange_rhs_to_standard_form(rng: random.Random) -> Dict[str, Any]:
    """Solve x^2 + bx = c by first rearranging to x^2 + bx - c = 0. State positive root."""
    pos_root = rng.choice([4, 5, 6, 7])
    neg_root = rng.choice([1, 2, 3])
    # (x - pos_root)(x + neg_root) = 0 => x^2 - (pos_root - neg_root)x = pos_root * neg_root
    diff = pos_root - neg_root
    prod = pos_root * neg_root

    return {
        "subskill": "40_quadratic_rearrange_rhs_to_standard_form",
        "question_text": (
            f"Solve for $x$ by first writing the equation in standard form ($ax^2 + bx + c = 0$):\n"
            f"$$x^2 - {diff}x = {prod}$$\n\n"
            f"State the **positive solution**:"
        ),
        "correct_answer": str(pos_root),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Rearrange to standard form: x^2 - {diff}x - {prod} = 0", "marks": 1},
            {"step": f"Factorise trinomial: (x - {pos_root})(x + {neg_root}) = 0", "marks": 1},
            {"step": f"State positive solution: x = {pos_root}", "marks": 1},
        ],
        "hints": [
            f"Subtract ${prod}$ from both sides to achieve standard form: $x^2 - {diff}x - {prod} = 0$.",
            f"Factorise: $(x - {pos_root})(x + {neg_root}) = 0$.",
            f"The positive root is ${pos_root}$.",
        ],
    }


def arch_41_quadratic_expand_brackets_then_factorise(rng: random.Random) -> Dict[str, Any]:
    """Solve x(x + a) = b. Expand first, rearrange, factorise. State positive root."""
    pos_root = rng.choice([3, 4, 5, 6])
    neg_root = rng.choice([1, 2])
    # (x - pos_root)(x + neg_root) = 0 => x^2 + (neg_root - pos_root)x - pos*neg = 0
    # Let a = pos_root - neg_root > 0, so x(x - a) = b
    a = pos_root - neg_root
    b = pos_root * neg_root

    return {
        "subskill": "41_quadratic_expand_brackets_then_factorise",
        "question_text": (
            f"Solve the equation for $x$:\n"
            f"$$x(x - {a}) = {b}$$\n\n"
            f"State the **positive solution**:"
        ),
        "correct_answer": str(pos_root),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Expand brackets: x^2 - {a}x = {b}", "marks": 1},
            {"step": f"Rearrange to standard form: x^2 - {a}x - {b} = 0", "marks": 1},
            {"step": f"Factorise and solve: (x - {pos_root})(x + {neg_root}) = 0 => x = {pos_root}", "marks": 1},
        ],
        "hints": [
            f"Expand the left side: $x^2 - {a}x = {b}$.",
            f"Transpose ${b}$ to the left: $x^2 - {a}x - {b} = 0$.",
            f"Factorise: $(x - {pos_root})(x + {neg_root}) = 0 \\implies x = {pos_root}$.",
        ],
    }


def arch_42_quadratic_geometric_area_rectangle_svg(rng: random.Random) -> Dict[str, Any]:
    """Geometric rectangle area problem leading to quadratic equation (SVG)."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([4, 5, 6, 7])
    extra = rng.choice([2, 3, 5])
    # Length = x + extra, Width = x. Area = x(x + extra)
    area = x_val * (x_val + extra)

    length_label = f"Length = x + {extra} cm"
    width_label = "Width = x cm"
    area_label = f"{area} cm²"
    svg = draw_quadratic_rectangle_area_svg(length_label, width_label, area_label, seed=seed)

    return {
        "subskill": "42_quadratic_geometric_area_rectangle_svg",
        "question_text": (
            f"A rectangular garden has length $(x + {extra})\\text{{ cm}}$, width $x\\text{{ cm}}$, "
            f"and an area of ${area}\\text{{ cm}}^2$.\n\n"
            f"Set up a quadratic equation and solve for the positive dimension $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Set up area formula: x(x + {extra}) = {area}", "marks": 1},
            {"step": f"Rearrange to standard form: x^2 + {extra}x - {area} = 0", "marks": 1},
            {"step": f"Factorise: (x - {x_val})(x + {x_val + extra}) = 0", "marks": 1},
            {"step": f"Discard negative dimension and state x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"$\\text{{Area}} = \\text{{length}} \\times \\text{{width}} \\implies x(x + {extra}) = {area}$.",
            f"Standard form: $x^2 + {extra}x - {area} = 0$.",
            f"Factorise: $(x - {x_val})(x + {x_val + extra}) = 0 \\implies x = {x_val}\\text{{ cm}}$ (length must be positive).",
        ],
    }


def arch_43_error_analysis_divided_by_variable_lost_zero_root(rng: random.Random) -> Dict[str, Any]:
    """Error analysis: student divided by x in x^2 = ax and lost the root x = 0."""
    a = rng.choice([5, 6, 7, 8, 9])

    return {
        "subskill": "43_error_analysis_divided_by_variable_lost_zero_root",
        "question_text": (
            f"A learner was asked to solve the equation:\n"
            f"$$x^2 = {a}x$$\n\n"
            f"The learner divided both sides by $x$ and concluded that $x = {a}$ is the only solution.\n"
            f"State the other valid solution that the learner eliminated by dividing by $x$:"
        ),
        "correct_answer": "0",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Explain that dividing by x is mathematically invalid because x could be zero", "marks": 1},
            {"step": f"Rearrange to standard form: x^2 - {a}x = 0 => x(x - {a}) = 0", "marks": 1},
            {"step": "State the lost solution: x = 0", "marks": 1},
        ],
        "hints": [
            "You cannot divide by a variable because the variable could equal $0$, causing division by zero.",
            f"Rearrange to standard form: $x^2 - {a}x = 0 \\implies x(x - {a}) = 0$.",
            "This yields two solutions: $x = 0$ or $x = a$. The eliminated solution is $0$.",
        ],
    }


def arch_44_literal_equation_subject_linear_fraction_simple(rng: random.Random) -> Dict[str, Any]:
    """Literal equation: v = d/t. Make t the subject, then evaluate for given values."""
    v = rng.choice([40, 50, 60, 80])
    t_val = rng.choice([2, 3, 4, 5])
    d = v * t_val

    return {
        "subskill": "44_literal_equation_subject_linear_fraction_simple",
        "question_text": (
            f"The speed formula is given by $v = \\frac{{d}}{{t}}$, where $v$ is velocity, $d$ is distance, and $t$ is time.\n\n"
            f"1. Make $t$ the subject of the formula ($t = \\frac{{d}}{{v}}$).\n"
            f"2. Calculate the value of $t$ (in hours) when $d = {d}\\text{{ km}}$ and $v = {v}\\text{{ km/h}}$:"
        ),
        "correct_answer": str(t_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Multiply by t: vt = d", "marks": 1},
            {"step": "Divide by v: t = d/v", "marks": 1},
            {"step": f"Substitute values: t = {d} / {v} = {t_val}", "marks": 1},
        ],
        "hints": [
            "Multiply both sides by $t$: $v \\times t = d$.",
            "Divide both sides by $v$: $t = \\frac{d}{v}$.",
            f"Substitute $d = {d}$ and $v = {v}$: $t = {d} \\div {v} = {t_val}$.",
        ],
    }


def arch_45_literal_equation_subject_triangle_area_fraction(rng: random.Random) -> Dict[str, Any]:
    """Literal equation: A = 1/2*b*h. Make h the subject, then evaluate."""
    b = rng.choice([6, 8, 10, 12])
    h_val = rng.choice([4, 5, 7, 9])
    area = (b * h_val) // 2

    return {
        "subskill": "45_literal_equation_subject_triangle_area_fraction",
        "question_text": (
            f"The area of a triangle is given by the formula $A = \\frac{{1}}{{2}}bh$.\n\n"
            f"1. Make the height $h$ the subject of the formula ($h = \\frac{{2A}}{{b}}$).\n"
            f"2. Calculate $h$ when $A = {area}\\text{{ cm}}^2$ and base $b = {b}\\text{{ cm}}$:"
        ),
        "correct_answer": str(h_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Multiply both sides by 2: 2A = bh", "marks": 1},
            {"step": "Divide both sides by b: h = 2A/b", "marks": 1},
            {"step": f"Calculate h: 2({area}) / {b} = {h_val}", "marks": 1},
        ],
        "hints": [
            "Multiply both sides by $2$ to clear the fraction: $2A = bh$.",
            "Divide both sides by base $b$: $h = \\frac{2A}{b}$.",
            f"Substitute $A = {area}$ and $b = {b}$: $h = \\frac{{2 \\times {area}}}{{{b}}} = {h_val}$.",
        ],
    }


def arch_46_literal_equation_subject_temperature_conversion(rng: random.Random) -> Dict[str, Any]:
    """Literal equation: C = 5/9*(F - 32). Make F subject, evaluate for integer result."""
    c_val = rng.choice([15, 20, 25, 30, 35])
    # F = 9/5*C + 32
    f_val = (9 * c_val) // 5 + 32

    return {
        "subskill": "46_literal_equation_subject_temperature_conversion",
        "question_text": (
            f"The formula to convert Fahrenheit ($F$) to Celsius ($C$) is:\n"
            f"$$C = \\frac{{5}}{{9}}(F - 32)$$\n\n"
            f"1. Make $F$ the subject of the formula.\n"
            f"2. Calculate the temperature in Fahrenheit ($F$) when $C = {c_val}^\\circ\\text{{C}}$:"
        ),
        "correct_answer": str(f_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Multiply both sides by 9/5: (9/5)C = F - 32", "marks": 1},
            {"step": "Add 32 to both sides: F = (9/5)C + 32", "marks": 1},
            {"step": f"Substitute C = {c_val} and calculate: F = {f_val}", "marks": 1},
        ],
        "hints": [
            "Multiply both sides by $\\frac{9}{5}$: $\\frac{9}{5}C = F - 32$.",
            "Add $32$ to both sides: $F = \\frac{9}{5}C + 32$.",
            f"Substitute $C = {c_val}$: $F = \\frac{{9 \\times {c_val}}}{{5}} + 32 = {(9 * c_val)//5} + 32 = {f_val}$.",
        ],
    }


def arch_47_literal_equation_subject_linear_rational_expression(rng: random.Random) -> Dict[str, Any]:
    """Literal equation: y = (ax + b)/c. Make x the subject, evaluate."""
    a = rng.choice([2, 3, 4])
    c = rng.choice([3, 5])
    b = rng.choice([1, 2, 4])
    x_val = rng.choice([3, 4, 5])
    # cy = ax + b => y = (ax + b)/c. Ensure ax + b is multiple of c
    if (a * x_val + b) % c != 0:
        b = c - ((a * x_val) % c)
    y_val = (a * x_val + b) // c

    return {
        "subskill": "47_literal_equation_subject_linear_rational_expression",
        "question_text": (
            f"Given the formula $y = \\frac{{{a}x + {b}}}{{{c}}}$:\n\n"
            f"1. Make $x$ the subject of the formula ($x = \\frac{{{c}y - {b}}}{{{a}}}$).\n"
            f"2. Calculate the value of $x$ when $y = {y_val}$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Clear denominator: {c}y = {a}x + {b}", "marks": 1},
            {"step": f"Transpose and isolate x: x = ({c}y - {b}) / {a}", "marks": 1},
            {"step": f"Substitute y = {y_val} to find x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Multiply both sides by ${c}$: ${c}y = {a}x + {b}$.",
            f"Subtract ${b}$: ${a}x = ${c}y - {b} \\implies x = \\frac{{{c}y - {b}}}{{{a}}}$.",
            f"Substitute $y = {y_val}$: $x = ({c} \\times {y_val} - {b}) \\div {a} = {x_val}$.",
        ],
    }


def arch_48_word_problem_fractional_age_relation(rng: random.Random) -> Dict[str, Any]:
    """Word problem: Amanda's age is 1/3 of Jan's age. Sum of ages is S. Find Jan's age."""
    # j + 1/3 j = 4/3 j = S => j = 3S/4
    mult = rng.choice([6, 7, 8, 9, 10])
    s = 4 * mult
    jan_age = 3 * mult

    return {
        "subskill": "48_word_problem_fractional_age_relation",
        "question_text": (
            f"Amanda's age is one-third ($\\frac{{1}}{{3}}$) of her older brother Jan's age.\n"
            f"The sum of their ages is ${s}$ years.\n\n"
            f"Set up an equation with fractions and calculate Jan's age in years:"
        ),
        "correct_answer": str(jan_age),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Define Jan's age as j and set up equation: j + (1/3)j = {s}", "marks": 1},
            {"step": f"Combine fractional terms: (4/3)j = {s}", "marks": 1},
            {"step": f"Solve for Jan's age: j = {jan_age}", "marks": 1},
        ],
        "hints": [
            "Let Jan's age be $j$. Then Amanda's age is $\\frac{1}{3}j$.",
            f"Sum equation: $j + \\frac{{1}}{{3}}j = {s} \\implies \\frac{{4}}{{3}}j = {s}$.",
            f"Multiply by $3$ and divide by $4$: $j = \\frac{{3 \\times {s}}}{{4}} = {jan_age}$.",
        ],
    }


def arch_49_word_problem_fractional_number_sum(rng: random.Random) -> Dict[str, Any]:
    """Word problem: A number increased by 1/4 of itself equals K. Find the number."""
    # x + x/4 = 5x/4 = K => x = 4K/5
    mult = rng.choice([5, 6, 7, 8, 9, 11])
    k = 5 * mult
    x_val = 4 * mult

    return {
        "subskill": "49_word_problem_fractional_number_sum",
        "question_text": (
            f"A number is increased by one-fourth ($\\frac{{1}}{{4}}$) of itself, resulting in ${k}$.\n\n"
            f"Set up a linear equation and determine the original number:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up equation: x + (1/4)x = {k}", "marks": 1},
            {"step": f"Combine fractions: (5/4)x = {k}", "marks": 1},
            {"step": f"Solve for x: x = (4/5) * {k} = {x_val}", "marks": 1},
        ],
        "hints": [
            "Let the unknown number be $x$.",
            f"$x + \\frac{{x}}{{4}} = {k} \\implies \\frac{{5x}}{{4}} = {k}$.",
            f"Multiply by $4$ and divide by $5$: $x = \\frac{{4 \\times {k}}}{{5}} = {x_val}$.",
        ],
    }


def arch_50_word_problem_speed_distance_time_fractional(rng: random.Random) -> Dict[str, Any]:
    """Word problem: d/10 + d/15 = T. Find one-way distance d."""
    # (3d + 2d)/30 = 5d/30 = d/6 = T => d = 6T
    t = rng.choice([2, 3, 4, 5])
    d_val = 6 * t

    return {
        "subskill": "50_word_problem_speed_distance_time_fractional",
        "question_text": (
            f"A delivery cyclist travels a distance of $d\\text{{ km}}$ uphill at $10\\text{{ km/h}}$, "
            f"and returns along the same route downhill at $15\\text{{ km/h}}$.\n"
            f"The total journey took ${t}\\text{{ hours}}$.\n\n"
            f"Given the time equation $$\\frac{{d}}{{10}} + \\frac{{d}}{{15}} = {t}$$\n"
            f"Calculate the one-way distance $d$ in kilometres:"
        ),
        "correct_answer": str(d_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply through by LCD = 30: 3d + 2d = {30 * t}", "marks": 1},
            {"step": f"Combine like terms: 5d = {30 * t}", "marks": 1},
            {"step": f"Solve for distance: d = {d_val}", "marks": 1},
        ],
        "hints": [
            "Find the Lowest Common Denominator of $10$ and $15$, which is $30$.",
            f"Multiply every term by $30$: $3d + 2d = 30 \\times {t} = {30 * t}$.",
            f"$5d = {30 * t} \\implies d = {30 * t} \\div 5 = {d_val}\\text{{ km}}$.",
        ],
    }
