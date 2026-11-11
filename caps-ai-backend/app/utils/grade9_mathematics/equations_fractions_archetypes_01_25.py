"""Grade 9 Mathematics - Equations 2 (Fractions & Rational Equations) Archetypes (01 to 25).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Equations 2.md
  - curriculum_docs/Mathematics_Gr9/Equations Studio.md

Covers:
  - Linear equations with monomial denominators: x/b = c, x/b + a = c, x/b - a = c
  - Binomial numerators: (x + a)/b = c, (ax + b)/c = d
  - Balance scale visual models with fractions (SVG)
  - Fractions on both sides and clearing denominators using LCD
  - Sum and difference of algebraic fractions with monomial denominators
  - The negative binomial distribution trap: -(x - c)/d
  - Three algebraic fractions with LCD
  - Equations with constant integer terms requiring LCD multiplication
  - Cross multiplication forms: (ax + b)/c = (dx + e)/f and a/(x + b) = c/d
  - Distributive law with fractional coefficients: 1/a(bx + c) = d
  - Geometric perimeter problems with fractional dimensions (SVG)
  - Error analysis: diagnosing the RHS LCD omission error
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .equations_fractions_svg import (
    draw_fraction_balance_scale_svg,
    draw_fraction_rectangle_perimeter_svg,
)


def arch_01_fraction_linear_basic_monomial_denominator(rng: random.Random) -> Dict[str, Any]:
    """Solve basic linear equation with monomial denominator: x/b = c."""
    b = rng.choice([2, 3, 4, 5, 6, 7, 8])
    c = rng.choice([-11, -9, -7, -5, 4, 6, 7, 8, 9, 12])
    ans = b * c

    return {
        "subskill": "01_fraction_linear_basic_monomial_denominator",
        "question_text": (
            f"Solve the linear equation for $x$:\n"
            f"$$\\frac{{x}}{{{b}}} = {c}$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply both sides by {b}: x = {c} * {b}", "marks": 1},
            {"step": f"State final answer x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Clear the fraction by applying the multiplicative inverse of $\\frac{{1}}{{{b}}}$.",
            f"Multiply both sides of the equation by ${b}$: $x = {c} \\times {b}$.",
            f"$x = {ans}$.",
        ],
    }


def arch_02_fraction_linear_two_step_additive(rng: random.Random) -> Dict[str, Any]:
    """Solve two-step linear equation with fraction: x/b + a = c."""
    b = rng.choice([2, 3, 4, 5, 6])
    a = rng.choice([3, 4, 5, 7, 8, 9])
    k = rng.choice([2, 3, 4, 5, 6])
    c = a + k
    ans = b * k

    return {
        "subskill": "02_fraction_linear_two_step_additive",
        "question_text": (
            f"Solve for $x$:\n"
            f"$$\\frac{{x}}{{{b}}} + {a} = {c}$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Subtract {a} from both sides: x/{b} = {c - a}", "marks": 1},
            {"step": f"Multiply both sides by {b}: x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Isolate the fraction term first by subtracting ${a}$ from both sides.",
            f"$\\frac{{x}}{{{b}}} = {c} - {a} = {k}$.",
            f"Multiply both sides by ${b}$: $x = {k} \\times {b} = {ans}$.",
        ],
    }


def arch_03_fraction_linear_two_step_subtractive(rng: random.Random) -> Dict[str, Any]:
    """Solve two-step linear equation with subtraction: x/b - a = c."""
    b = rng.choice([3, 4, 5, 6, 7])
    a = rng.choice([2, 4, 5, 6, 8])
    c = rng.choice([1, 2, 3, 5, 7])
    k = a + c
    ans = b * k

    return {
        "subskill": "03_fraction_linear_two_step_subtractive",
        "question_text": (
            f"Solve for $x$:\n"
            f"$$\\frac{{x}}{{{b}}} - {a} = {c}$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Add {a} to both sides: x/{b} = {k}", "marks": 1},
            {"step": f"Multiply both sides by {b}: x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Add ${a}$ to both sides to isolate the fraction term.",
            f"$\\frac{{x}}{{{b}}} = {c} + {a} = {k}$.",
            f"Multiply both sides by ${b}$: $x = {k} \\times {b} = {ans}$.",
        ],
    }


def arch_04_fraction_linear_binomial_numerator_simple(rng: random.Random) -> Dict[str, Any]:
    """Solve linear equation with binomial numerator: (x + a)/b = c."""
    b = rng.choice([2, 3, 4, 5, 6])
    c = rng.choice([3, 4, 5, 6, 7])
    a = rng.choice([1, 2, 4, 5, 7])
    ans = b * c - a

    return {
        "subskill": "04_fraction_linear_binomial_numerator_simple",
        "question_text": (
            f"Solve for $x$:\n"
            f"$$\\frac{{x + {a}}}{{{b}}} = {c}$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply both sides by {b}: x + {a} = {b * c}", "marks": 1},
            {"step": f"Subtract {a} to solve for x: x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Multiply both sides of the equation by denominator ${b}$ to clear the fraction.",
            f"$x + {a} = {b} \\times {c} = {b * c}$.",
            f"Subtract ${a}$ from both sides: $x = {b * c} - {a} = {ans}$.",
        ],
    }


def arch_05_fraction_linear_binomial_numerator_subtraction(rng: random.Random) -> Dict[str, Any]:
    """Solve linear equation with subtracted binomial numerator: (x - a)/b = c."""
    b = rng.choice([2, 3, 4, 5, 7])
    c = rng.choice([2, 3, 4, 6, 8])
    a = rng.choice([3, 5, 7, 9, 11])
    ans = b * c + a

    return {
        "subskill": "05_fraction_linear_binomial_numerator_subtraction",
        "question_text": (
            f"Solve for $x$:\n"
            f"$$\\frac{{x - {a}}}{{{b}}} = {c}$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply both sides by {b}: x - {a} = {b * c}", "marks": 1},
            {"step": f"Add {a} to both sides: x = {ans}", "marks": 1},
        ],
        "hints": [
            f"Multiply both sides by ${b}$ to eliminate the denominator.",
            f"$x - {a} = {b} \\times {c} = {b * c}$.",
            f"Add ${a}$ to both sides: $x = {b * c} + {a} = {ans}$.",
        ],
    }


def arch_06_fraction_linear_coefficient_binomial_numerator(rng: random.Random) -> Dict[str, Any]:
    """Solve (ax + b)/c = d where a > 1."""
    a = rng.choice([2, 3, 4, 5])
    x_val = rng.choice([2, 3, 4, 5, 6])
    c = rng.choice([2, 3, 4, 5])
    d = rng.choice([3, 4, 5, 6, 7])
    cd = c * d
    b = cd - a * x_val
    if b <= 0:
        d = d + 3
        cd = c * d
        b = cd - a * x_val

    return {
        "subskill": "06_fraction_linear_coefficient_binomial_numerator",
        "question_text": (
            f"Solve the equation for $x$:\n"
            f"$$\\frac{{{a}x + {b}}}{{{c}}} = {d}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply both sides by {c}: {a}x + {b} = {cd}", "marks": 1},
            {"step": f"Transpose constant: {a}x = {cd - b}", "marks": 1},
            {"step": f"Divide by {a}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Multiply both sides by ${c}$: ${a}x + {b} = {d} \\times {c} = {cd}$.",
            f"Subtract ${b}$ from both sides: ${a}x = {cd} - {b} = {cd - b}$.",
            f"Divide by ${a}$: $x = {cd - b} \\div {a} = {x_val}$.",
        ],
    }


def arch_07_fraction_linear_coefficient_negative_binomial(rng: random.Random) -> Dict[str, Any]:
    """Solve (ax - b)/c = d with negative solution or terms."""
    a = rng.choice([2, 3, 4])
    x_val = rng.choice([-5, -4, -3, -2])
    b = rng.choice([2, 3, 4, 5])
    numerator = a * x_val - b
    c = rng.choice([2, 3, 5])
    # Adjust d so equation holds: d = numerator / c
    d = numerator // c
    b = a * x_val - c * d

    return {
        "subskill": "07_fraction_linear_coefficient_negative_binomial",
        "question_text": (
            f"Solve for $x$:\n"
            f"$$\\frac{{{a}x - {b}}}{{{c}}} = {d}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply both sides by {c}: {a}x - {b} = {c * d}", "marks": 1},
            {"step": f"Add {b} to both sides: {a}x = {c * d + b}", "marks": 1},
            {"step": f"Divide by {a}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Clear the denominator by multiplying both sides by ${c}$: ${a}x - {b} = {c * d}$.",
            f"Add ${b}$ to both sides: ${a}x = {c * d} + {b} = {c * d + b}$.",
            f"Divide by ${a}$: $x = {c * d + b} \\div {a} = {x_val}$.",
        ],
    }


def arch_08_fraction_balance_scale_model_visual(rng: random.Random) -> Dict[str, Any]:
    """Balance scale visual model with fractional unknown weight (SVG)."""
    seed = rng.randint(1, 1_000_000)
    b = rng.choice([3, 4, 5])
    a = rng.choice([2, 4, 6])
    k = rng.choice([3, 4, 5])
    c = a + k
    x_val = b * k

    left_label = f"x/{b} + {a}"
    right_label = str(c)
    svg = draw_fraction_balance_scale_svg(left_label, right_label, seed=seed)

    return {
        "subskill": "08_fraction_balance_scale_model_visual",
        "question_text": (
            f"The beam scale below is in balance, representing the equation $$\\frac{{x}}{{{b}}} + {a} = {c}$$.\n\n"
            f"Find the value of the unknown $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Subtract {a} from both pans: x/{b} = {c - a}", "marks": 1},
            {"step": f"Multiply by {b} to find x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Remove ${a}$ from both sides of the balance: $\\frac{{x}}{{{b}}} = {c} - {a} = {k}$.",
            f"Multiply by ${b}$ to find the total value of block $x$: $x = {k} \\times {b}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_09_fraction_linear_both_sides_monomial(rng: random.Random) -> Dict[str, Any]:
    """Solve equation with fractions on both sides: x/b = x/d + k."""
    b, d = 2, 3
    lcd = 6
    k = rng.choice([2, 3, 4, 5, 7])
    # x/2 - x/3 = k => (3x - 2x)/6 = k => x/6 = k => x = 6k
    x_val = lcd * k

    return {
        "subskill": "09_fraction_linear_both_sides_monomial",
        "question_text": (
            f"Solve the equation for $x$:\n"
            f"$$\\frac{{x}}{{{b}}} = \\frac{{x}}{{{d}}} + {k}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify LCD = {lcd} and multiply all terms: {d}x = {b}x + {lcd * k}", "marks": 1},
            {"step": f"Subtract {b}x from both sides: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Multiply every term across both sides by the Lowest Common Denominator (LCD), which is ${lcd}$.",
            f"${d}x = {b}x + {lcd * k}$.",
            f"Subtract ${b}x$ from both sides to obtain $x = {x_val}$.",
        ],
    }


def arch_10_fraction_linear_sum_two_fractions_same_denominator(rng: random.Random) -> Dict[str, Any]:
    """Solve sum of fractions with same denominator: x/a + cx/a = b."""
    a = rng.choice([3, 4, 5, 6, 7])
    c_coeff = rng.choice([2, 3, 4])
    mult = rng.choice([2, 3, 4, 5])
    # (1 + c_coeff)*x / a = b => let x = mult * a => b = (1 + c_coeff)*mult
    x_val = mult * a
    b_val = (1 + c_coeff) * mult

    return {
        "subskill": "10_fraction_linear_sum_two_fractions_same_denominator",
        "question_text": (
            f"Solve for $x$:\n"
            f"$$\\frac{{x}}{{{a}}} + \\frac{{{c_coeff}x}}{{{a}}} = {b_val}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Combine numerators over common denominator {a}: {(1 + c_coeff)}x / {a} = {b_val}", "marks": 1},
            {"step": f"Multiply by {a} and solve: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Since the denominators are both ${a}$, combine the numerators: $\\frac{{x + {c_coeff}x}}{{{a}}} = \\frac{{{1 + c_coeff}x}}{{{a}}} = {b_val}$.",
            f"Multiply both sides by ${a}$: ${1 + c_coeff}x = {b_val * a}$.",
            f"Divide by ${1 + c_coeff}$: $x = {b_val * a} \\div {1 + c_coeff} = {x_val}$.",
        ],
    }


def arch_11_fraction_linear_sum_two_fractions_lcd_coprime(rng: random.Random) -> Dict[str, Any]:
    """Solve x/a + x/b = c where gcd(a, b) = 1."""
    a, b = rng.choice([(2, 3), (3, 4), (2, 5), (3, 5)])
    lcd = a * b
    k = rng.choice([1, 2, 3, 4])
    # (b*x + a*x) / lcd = c => (a + b)x = lcd * c => let c = k * (a + b) => x = k * lcd
    c_val = k * (a + b)
    x_val = k * lcd

    return {
        "subskill": "11_fraction_linear_sum_two_fractions_lcd_coprime",
        "question_text": (
            f"Solve for $x$ by finding the Lowest Common Denominator:\n"
            f"$$\\frac{{x}}{{{a}}} + \\frac{{x}}{{{b}}} = {c_val}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify LCD = {lcd} and multiply all terms: {b}x + {a}x = {lcd * c_val}", "marks": 1},
            {"step": f"Combine like terms: {a + b}x = {lcd * c_val}", "marks": 1},
            {"step": f"Divide by {a + b}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"The Lowest Common Denominator of ${a}$ and ${b}$ is ${lcd}$.",
            f"Multiply every term by ${lcd}$: ${b}x + ${a}x = {lcd * c_val}$.",
            f"${a + b}x = {lcd * c_val} \\implies x = {x_val}$.",
        ],
    }


def arch_12_fraction_linear_diff_two_fractions_lcd(rng: random.Random) -> Dict[str, Any]:
    """Solve x/a - x/b = c where a < b."""
    a, b = rng.choice([(2, 3), (3, 4), (2, 5), (4, 5)])
    lcd = a * b
    diff = b - a
    k = rng.choice([1, 2, 3, 4])
    c_val = k * diff
    x_val = k * lcd

    return {
        "subskill": "12_fraction_linear_diff_two_fractions_lcd",
        "question_text": (
            f"Solve for $x$:\n"
            f"$$\\frac{{x}}{{{a}}} - \\frac{{x}}{{{b}}} = {c_val}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply every term by LCD = {lcd}: {b}x - {a}x = {lcd * c_val}", "marks": 1},
            {"step": f"Simplify and divide: {diff}x = {lcd * c_val} => x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Multiply every term across both sides by the LCD ${lcd}$.",
            f"${b}x - {a}x = {lcd} \\times {c_val} = {lcd * c_val}$.",
            f"${diff}x = {lcd * c_val} \\implies x = {x_val}$.",
        ],
    }


def arch_13_fraction_linear_binomial_numerators_add_lcd(rng: random.Random) -> Dict[str, Any]:
    """Solve (x + a)/2 + (x + b)/3 = k."""
    d1, d2, lcd = 2, 3, 6
    x_val = rng.choice([1, 2, 3, 4, 5, 6])
    # x and a must have same parity so 5x + 3a is even
    a_candidates = [val for val in [1, 2, 3, 4, 5] if (x_val + val) % 2 == 0]
    a = rng.choice(a_candidates)
    # 2b % 3 == -(5x + 3a) % 3
    b_candidates = [val for val in [1, 2, 3] if (5 * x_val + 3 * a + 2 * val) % 3 == 0]
    b = rng.choice(b_candidates)
    k = (5 * x_val + 3 * a + 2 * b) // 6

    return {
        "subskill": "13_fraction_linear_binomial_numerators_add_lcd",
        "question_text": (
            f"Solve the linear equation using the Lowest Common Denominator:\n"
            f"$$\\frac{{x + {a}}}{{{d1}}} + \\frac{{x + {b}}}{{{d2}}} = {k}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply every term by LCD = {lcd}: {d2}(x + {a}) + {d1}(x + {b}) = {lcd * k}", "marks": 1},
            {"step": f"Expand brackets: {d2}x + {d2 * a} + {d1}x + {d1 * b} = {lcd * k}", "marks": 1},
            {"step": f"Combine like terms: 5x + {d2 * a + d1 * b} = {lcd * k}", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Identify the LCD of ${d1}$ and ${d2}$, which is ${lcd}$.",
            f"Multiply each term by ${lcd}$: ${d2}(x + {a}) + {d1}(x + {b}) = {lcd * k}$.",
            f"Expand brackets, group like terms, and solve to get $x = {x_val}$.",
        ],
    }


def arch_14_fraction_linear_binomial_numerators_sub_negative_distrib(rng: random.Random) -> Dict[str, Any]:
    """Solve (x + a)/2 - (x - b)/3 = k (tests distribution of negative bracket)."""
    d1, d2, lcd = 2, 3, 6
    a = rng.choice([1, 2, 3, 4])
    b = rng.choice([1, 2, 3, 5])
    k = rng.choice([3, 4, 5, 6])
    # 3(x + a) - 2(x - b) = 6k => 3x + 3a - 2x + 2b = 6k => x + 3a + 2b = 6k
    x_val = 6 * k - 3 * a - 2 * b

    return {
        "subskill": "14_fraction_linear_binomial_numerators_sub_negative_distrib",
        "question_text": (
            f"Solve for $x$, paying careful attention to the signs:\n"
            f"$$\\frac{{x + {a}}}{{{d1}}} - \\frac{{x - {b}}}{{{d2}}} = {k}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply through by LCD = {lcd}: {d2}(x + {a}) - {d1}(x - {b}) = {lcd * k}", "marks": 1},
            {"step": f"Correct distribution of negative bracket: {d2}x + {d2 * a} - {d1}x + {d1 * b} = {lcd * k}", "marks": 1},
            {"step": f"Group terms: x + {d2 * a + d1 * b} = {lcd * k}", "marks": 1},
            {"step": f"State final answer x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Multiply every term across both sides by ${lcd}$: ${d2}(x + {a}) - {d1}(x - {b}) = {lcd * k}$.",
            f"Be very careful with the minus sign: $-{d1}(x - {b}) = -{d1}x + {d1 * b}$.",
            f"Combine terms: $x + {d2 * a + d1 * b} = {lcd * k} \\implies x = {x_val}$.",
        ],
    }


def arch_15_fraction_linear_binomial_numerators_diff_lcd_multiple(rng: random.Random) -> Dict[str, Any]:
    """Solve (2x - a)/3 - (x + b)/4 = k."""
    d1, d2, lcd = 3, 4, 12
    a = rng.choice([1, 2, 4, 5])
    k = rng.choice([2, 3, 4])
    # 4(2x - a) - 3(x + b) = 12k => 8x - 4a - 3x - 3b = 12k => 5x - 4a - 3b = 12k => 5x = 12k + 4a + 3b
    # Find b in 1..5 such that (12k + 4a + 3b) % 5 == 0
    rem = (12 * k + 4 * a) % 5
    b_candidates = [val for val in range(1, 6) if (3 * val) % 5 == (5 - rem) % 5]
    b = b_candidates[0]
    x_val = (12 * k + 4 * a + 3 * b) // 5

    return {
        "subskill": "15_fraction_linear_binomial_numerators_diff_lcd_multiple",
        "question_text": (
            f"Solve the following equation for $x$:\n"
            f"$$\\frac{{2x - {a}}}{{{d1}}} - \\frac{{x + {b}}}{{{d2}}} = {k}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply both sides by LCD = {lcd}: 4(2x - {a}) - 3(x + {b}) = {lcd * k}", "marks": 1},
            {"step": f"Expand brackets: 8x - {4 * a} - 3x - {3 * b} = {lcd * k}", "marks": 1},
            {"step": f"Collect like terms: 5x = {12 * k + 4 * a + 3 * b}", "marks": 1},
            {"step": f"Divide by 5: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Find the LCD of ${d1}$ and ${d2}$, which is ${lcd}$.",
            f"Multiply through by ${lcd}$: $4(2x - {a}) - 3(x + {b}) = {lcd * k}$.",
            f"Distribute: $8x - {4 * a} - 3x - {3 * b} = {lcd * k} \\implies 5x = {12 * k + 4 * a + 3 * b} \\implies x = {x_val}$.",
        ],
    }


def arch_16_fraction_linear_three_fractions_lcd(rng: random.Random) -> Dict[str, Any]:
    """Solve linear equation with three fractions: x/2 + x/3 - x/6 = k."""
    # (3x + 2x - x) / 6 = 4x/6 = 2x/3 = k => x = 3k/2
    m = rng.choice([2, 4, 6, 8, 10])
    k = m
    x_val = (3 * k) // 2

    return {
        "subskill": "16_fraction_linear_three_fractions_lcd",
        "question_text": (
            f"Solve for $x$ by clearing denominators with the LCD:\n"
            f"$$\\frac{{x}}{{2}} + \\frac{{x}}{{3}} - \\frac{{x}}{{6}} = {k}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify LCD = 6 and multiply each fraction by 6: 3x + 2x - x = 6k", "marks": 1},
            {"step": f"Simplify left-hand side: 4x = {6 * k}", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            "The Lowest Common Denominator of $2, 3,$ and $6$ is $6$.",
            f"Multiply every term by $6$: $3x + 2x - x = 6 \\times {k} = {6 * k}$.",
            f"Combine terms: $4x = {6 * k} \\implies x = {x_val}$.",
        ],
    }


def arch_17_fraction_linear_constant_term_clearing(rng: random.Random) -> Dict[str, Any]:
    """Solve (x - a)/2 + c = (x + d)/3 (highlighting multiplying constant c by LCD)."""
    d1, d2, lcd = 2, 3, 6
    a = rng.choice([2, 3, 4])
    d = rng.choice([3, 4, 5])
    c = rng.choice([2, 3, 4])
    # 3(x - a) + 6c = 2(x + d) => 3x - 3a + 6c = 2x + 2d => x = 2d + 3a - 6c
    # To keep x > 0, ensure 2d + 3a > 6c
    if 2 * d + 3 * a <= 6 * c:
        c = 1
    x_val = 2 * d + 3 * a - 6 * c

    return {
        "subskill": "17_fraction_linear_constant_term_clearing",
        "question_text": (
            f"Solve the equation for $x$:\n"
            f"$$\\frac{{x - {a}}}{{{d1}}} + {c} = \\frac{{x + {d}}}{{{d2}}}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply every term (including constant {c}) by LCD = {lcd}: 3(x - {a}) + {lcd * c} = 2(x + {d})", "marks": 1},
            {"step": f"Expand brackets: 3x - {3 * a} + {6 * c} = 2x + {2 * d}", "marks": 1},
            {"step": f"Transpose and solve: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Multiply every single term across the equation by the LCD ${lcd}$. Remember that ${c} \\times {lcd} = {6 * c}$.",
            f"$3(x - {a}) + {6 * c} = 2(x + {d})$.",
            f"$3x - {3 * a} + {6 * c} = 2x + {2 * d} \\implies x = {x_val}$.",
        ],
    }


def arch_18_fraction_cross_multiplication_basic(rng: random.Random) -> Dict[str, Any]:
    """Solve (x + a)/3 = (x - c)/2 using cross-multiplication."""
    b, d = 3, 2
    a = rng.choice([2, 3, 4, 5])
    c = rng.choice([1, 2, 3, 4])
    # 2(x + a) = 3(x - c) => 2x + 2a = 3x - 3c => x = 2a + 3c
    x_val = 2 * a + 3 * c

    return {
        "subskill": "18_fraction_cross_multiplication_basic",
        "question_text": (
            f"Solve for $x$ using cross-multiplication:\n"
            f"$$\\frac{{x + {a}}}{{{b}}} = \\frac{{x - {c}}}{{{d}}}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Cross-multiply: {d}(x + {a}) = {b}(x - {c})", "marks": 1},
            {"step": f"Expand both sides: {d}x + {d * a} = {b}x - {b * c}", "marks": 1},
            {"step": f"Group x terms and solve: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Apply cross-multiplication: ${d}(x + {a}) = ${b}(x - {c})$.",
            f"Expand both sides: ${d}x + {d * a} = ${b}x - {b * c}$.",
            f"Subtract ${d}x$ from both sides and add ${b * c}$: $x = {2 * a} + {3 * c} = {x_val}$.",
        ],
    }


def arch_19_fraction_cross_multiplication_coefficients(rng: random.Random) -> Dict[str, Any]:
    """Solve (2x + a)/5 = (x + b)/2 using cross-multiplication."""
    # 2(2x + a) = 5(x + b) => 4x + 2a = 5x + 5b => x = 2a - 5b
    b = rng.choice([1, 2])
    a = rng.choice([7, 8, 9, 10])
    x_val = 2 * a - 5 * b

    return {
        "subskill": "19_fraction_cross_multiplication_coefficients",
        "question_text": (
            f"Solve the equation for $x$:\n"
            f"$$\\frac{{2x + {a}}}{{5}} = \\frac{{x + {b}}}{{2}}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Cross-multiply: 2(2x + {a}) = 5(x + {b})", "marks": 1},
            {"step": f"Expand: 4x + {2 * a} = 5x + {5 * b}", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Cross-multiply: $2(2x + {a}) = 5(x + {b})$.",
            f"Distribute: $4x + {2 * a} = 5x + {5 * b}$.",
            f"Transpose $4x$ to the right: $x = {2 * a} - {5 * b} = {x_val}$.",
        ],
    }


def arch_20_fraction_cross_multiplication_variable_denominator(rng: random.Random) -> Dict[str, Any]:
    """Solve a/(x + b) = c/d where variable is in denominator."""
    c, d = 2, 5
    mult = rng.choice([2, 3, 4, 6])
    a = c * mult
    # a / (x + b) = c / d => c(x + b) = a*d => x + b = a*d / c = mult * d
    b = rng.choice([1, 2, 3, 4])
    x_val = mult * d - b

    return {
        "subskill": "20_fraction_cross_multiplication_variable_denominator",
        "question_text": (
            f"Solve for $x$ (where $x \\neq -{b}$):\n"
            f"$$\\frac{{{a}}}{{x + {b}}} = \\frac{{{c}}}{{{d}}}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Cross-multiply: {c}(x + {b}) = {a} * {d}", "marks": 1},
            {"step": f"Expand: {c}x + {c * b} = {a * d}", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Cross-multiply to remove fractions: ${c}(x + {b}) = {a} \\times {d} = {a * d}$.",
            f"${c}x + {c * b} = {a * d} \\implies {c}x = {a * d - c * b}$.",
            f"Divide by ${c}$: $x = {x_val}$.",
        ],
    }


def arch_21_fraction_cross_multiplication_both_variable_denominators(rng: random.Random) -> Dict[str, Any]:
    """Solve a/(x + b) = c/(x - d) with variable in both denominators."""
    a, c = 4, 3
    # 4(x - d) = 3(x + b) => 4x - 4d = 3x + 3b => x = 3b + 4d
    b = rng.choice([1, 2, 3])
    d = rng.choice([1, 2, 3])
    x_val = 3 * b + 4 * d

    return {
        "subskill": "21_fraction_cross_multiplication_both_variable_denominators",
        "question_text": (
            f"Solve for $x$ (with restrictions $x \\neq -{b}$ and $x \\neq {d}$):\n"
            f"$$\\frac{{{a}}}{{x + {b}}} = \\frac{{{c}}}{{x - {d}}}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Cross-multiply: {a}(x - {d}) = {c}(x + {b})", "marks": 1},
            {"step": f"Expand brackets: {a}x - {a * d} = {c}x + {c * b}", "marks": 1},
            {"step": f"Group terms and solve: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Cross-multiply: ${a}(x - {d}) = ${c}(x + {b})$.",
            f"Distribute: ${a}x - {a * d} = ${c}x + {c * b}$.",
            f"Subtract ${c}x$ and add ${a * d}$: $x = {3 * b} + {4 * d} = {x_val}$.",
        ],
    }


def arch_22_fraction_brackets_distributive_monomial(rng: random.Random) -> Dict[str, Any]:
    """Solve 1/a * (bx + c) = d."""
    a = rng.choice([2, 3, 4, 5])
    b = rng.choice([2, 3, 4])
    x_val = rng.choice([2, 3, 4, 5])
    c = rng.choice([1, 3, 5])
    # bx + c = a*d => d = (bx + c)/a => choose c such that bx + c is divisible by a
    # Let d in 3..8, then bx + c = a*d => c = a*d - b*x
    d = rng.choice([4, 5, 6, 7])
    ad = a * d
    c = ad - b * x_val
    if c <= 0:
        d = d + 4
        ad = a * d
        c = ad - b * x_val

    return {
        "subskill": "22_fraction_brackets_distributive_monomial",
        "question_text": (
            f"Solve the equation for $x$:\n"
            f"$$\\frac{{1}}{{{a}}}({b}x + {c}) = {d}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply both sides by {a}: {b}x + {c} = {ad}", "marks": 1},
            {"step": f"Subtract {c}: {b}x = {ad - c}", "marks": 1},
            {"step": f"Divide by {b}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Multiply both sides of the equation by ${a}$ to eliminate the outer fraction.",
            f"${b}x + {c} = {d} \\times {a} = {ad}$.",
            f"Subtract ${c}$ and divide by ${b}$: $x = ({ad} - {c}) \\div {b} = {x_val}$.",
        ],
    }


def arch_23_fraction_brackets_expanded_with_lcd(rng: random.Random) -> Dict[str, Any]:
    """Solve 1/2(x - a) + 1/3(x + b) = c."""
    d1, d2, lcd = 2, 3, 6
    x_val = rng.choice([2, 4, 6, 8])
    # x and a must have same parity so 5x - 3a is even
    a_candidates = [val for val in [1, 2, 3, 4, 5] if (x_val - val) % 2 == 0]
    a = rng.choice(a_candidates)
    b_candidates = [val for val in [1, 2, 3] if (5 * x_val - 3 * a + 2 * val) % 3 == 0]
    b = rng.choice(b_candidates)
    c = (5 * x_val - 3 * a + 2 * b) // 6

    return {
        "subskill": "23_fraction_brackets_expanded_with_lcd",
        "question_text": (
            f"Solve the equation for $x$:\n"
            f"$$\\frac{{1}}{{2}}(x - {a}) + \\frac{{1}}{{3}}(x + {b}) = {c}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply every term by LCD = {lcd}: 3(x - {a}) + 2(x + {b}) = {lcd * c}", "marks": 1},
            {"step": f"Expand brackets: 3x - {3 * a} + 2x + {2 * b} = {lcd * c}", "marks": 1},
            {"step": f"Combine like terms and solve: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Multiply every term by the LCD ${lcd}$: $3(x - {a}) + 2(x + {b}) = {lcd * c}$.",
            f"Distribute: $3x - {3 * a} + 2x + {2 * b} = {lcd * c} \\implies 5x + {2 * b - 3 * a} = {lcd * c}$.",
            f"Solve for $x$: $x = {x_val}$.",
        ],
    }


def arch_24_geometric_perimeter_fractional_side_svg(rng: random.Random) -> Dict[str, Any]:
    """Solve geometric perimeter problem with fractional side length (SVG)."""
    seed = rng.randint(1, 1_000_000)
    b = rng.choice([2, 3, 4])
    a = rng.choice([1, 2, 5])
    w = rng.choice([3, 4, 5, 6])
    x_val = rng.choice([4, 6, 8, 10])
    # Length = (x + a)/b => ensure x + a is multiple of b for clean geometry
    if (x_val + a) % b != 0:
        a = b - (x_val % b)
    length_val = (x_val + a) // b
    perimeter = 2 * (length_val + w)

    length_label = f"(x + {a})/{b} cm"
    width_label = f"{w} cm"
    perim_label = f"{perimeter} cm"
    svg = draw_fraction_rectangle_perimeter_svg(length_label, width_label, perim_label, seed=seed)

    return {
        "subskill": "24_geometric_perimeter_fractional_side_svg",
        "question_text": (
            f"The rectangle below has length $\\frac{{x + {a}}}{{{b}}}\\text{{ cm}}$, width ${w}\\text{{ cm}}$, "
            f"and a total perimeter of ${perimeter}\\text{{ cm}}$.\n\n"
            f"Calculate the value of $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Set up perimeter formula: 2((x + {a})/{b} + {w}) = {perimeter}", "marks": 1},
            {"step": f"Divide by 2: (x + {a})/{b} + {w} = {perimeter // 2}", "marks": 1},
            {"step": f"Subtract width: (x + {a})/{b} = {length_val}", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Use the perimeter formula $P = 2(\\text{{length}} + \\text{{width}})$: $2\\left(\\frac{{x + {a}}}{{{b}}} + {w}\\right) = {perimeter}$.",
            f"Divide by $2$: $\\frac{{x + {a}}}{{{b}}} + {w} = {perimeter // 2} \\implies \\frac{{x + {a}}}{{{b}}} = {length_val}$.",
            f"Multiply by ${b}$ and subtract ${a}$: $x = {length_val} \\times {b} - {a} = {x_val}$.",
        ],
    }


def arch_25_error_analysis_forgot_lcd_multiplication_on_rhs(rng: random.Random) -> Dict[str, Any]:
    """Error analysis: student cleared LCD on LHS but forgot to multiply RHS integer."""
    d1, d2, lcd = 2, 3, 6
    k = rng.choice([4, 5, 6, 7])
    a = rng.choice([1, 2, 3])
    # Correct: 3(x + a) + 2x = 6k => 5x + 3a = 6k => 5x = 6k - 3a
    # Ensure 6k - 3a is divisible by 5
    # (6k - 3a) % 5 == 0 => k % 5 == 3a % 5
    for test_k in range(k, k + 10):
        if (6 * test_k - 3 * a) % 5 == 0:
            k = test_k
            break
    correct_x = (6 * k - 3 * a) // 5

    return {
        "subskill": "25_error_analysis_forgot_lcd_multiplication_on_rhs",
        "question_text": (
            f"A learner solved the equation:\n"
            f"$$\\frac{{x + {a}}}{{2}} + \\frac{{x}}{{3}} = {k}$$\n\n"
            f"**Learner's Working:**\n"
            f"Step 1: $3(x + {a}) + 2(x) = {k}$\n"
            f"Step 2: $3x + {3 * a} + 2x = {k}$\n"
            f"Step 3: $5x = {k} - {3 * a}$\n\n"
            f"Identify the mathematical error made in Step 1, and determine the correct value of $x$."
        ),
        "correct_answer": str(correct_x),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify error: RHS was not multiplied by the LCD ({lcd}) in Step 1", "marks": 1},
            {"step": f"Multiply RHS correctly: 5x + {3 * a} = {lcd * k}", "marks": 1},
            {"step": f"Calculate accurate solution: x = {correct_x}", "marks": 1},
        ],
        "hints": [
            f"When multiplying both sides of an equation by the LCD ${lcd}$, every single term including the right-hand side ${k}$ must be multiplied by ${lcd}$.",
            f"Step 1 should be $3(x + {a}) + 2x = {lcd} \\times {k} = {lcd * k}$.",
            f"$5x + {3 * a} = {lcd * k} \\implies 5x = {lcd * k - 3 * a} \\implies x = {correct_x}$.",
        ],
    }
