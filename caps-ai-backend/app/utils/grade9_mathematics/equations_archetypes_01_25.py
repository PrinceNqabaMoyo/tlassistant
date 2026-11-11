"""Grade 9 Mathematics - Algebraic Equations 1 Archetypes (01 to 25).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/01. Equations 1.md
  - curriculum_docs/Mathematics_Gr9/Equations Studio.md

Covers:
  - Inspection and table of values
  - Balance scale visual models (SVG)
  - One-step and two-step linear equations (additive & multiplicative inverses)
  - Equations with negative coefficients and negative solutions
  - Variables on both sides (integer and fractional solutions)
  - Distributive law in equations: single brackets, both sides brackets, negative multipliers
  - Geometric equations (supplementary angles, triangle angle sums, perimeters)
  - Substitution verification and consecutive integer word problems
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .equations_svg import (
    draw_balance_scale_svg,
    draw_geometric_equation_straight_line_angles_svg,
)


def arch_01_inspection_number_sentence_additive(rng: random.Random) -> Dict[str, Any]:
    """Solve additive open sentence by inspection: x + a = b."""
    x_val = rng.choice([7, 9, 12, 14, 18, 23])
    a = rng.choice([5, 8, 11, 15, 20])
    b = x_val + a

    return {
        "subskill": "01_inspection_number_sentence_additive",
        "question_text": (
            f"Solve the equation by inspection (mental calculation):\n"
            f"$$x + {a} = {b}$$\n\n"
            f"State the value of $x$."
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Determine value of x that makes equation true: {b} - {a} = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Ask yourself: 'What number added to {a} gives {b}?'",
            f"Use the inverse operation: ${b} - {a}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_02_inspection_number_sentence_multiplicative(rng: random.Random) -> Dict[str, Any]:
    """Solve multiplicative open sentence by inspection: a * x = b."""
    a = rng.choice([4, 6, 7, 8, 9])
    x_val = rng.choice([5, 6, 7, 8, 12])
    b = a * x_val

    return {
        "subskill": "02_inspection_number_sentence_multiplicative",
        "question_text": (
            f"Solve for $x$ by inspection:\n$${a}x = {b}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Divide {b} by {a} to find x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Ask yourself: '{a} multiplied by what number equals {b}?'",
            f"Calculate ${b} \\div {a}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_03_inspection_table_of_values_solution(rng: random.Random) -> Dict[str, Any]:
    """Solve an equation by finding intersection in a table of values."""
    x_sol = rng.choice([2, 3, 4, 5])
    m1, c1 = 3, rng.choice([1, 2, 4])
    m2, c2 = 1, m1 * x_sol + c1 - x_sol

    xs = list(range(x_sol - 2, x_sol + 3))
    lhs_vals = [m1 * x + c1 for x in xs]
    rhs_vals = [m2 * x + c2 for x in xs]

    header = "| $x$ | " + " | ".join(str(x) for x in xs) + " |"
    sep = "| :---: | " + " | ".join([":---:"] * len(xs)) + " |"
    lhs_row = f"| ${m1}x + {c1}$ | " + " | ".join(str(v) for v in lhs_vals) + " |"
    rhs_row = f"| $x + {c2}$ | " + " | ".join(str(v) for v in rhs_vals) + " |"
    table_md = f"{header}\n{sep}\n{lhs_row}\n{rhs_row}"

    return {
        "subskill": "03_inspection_table_of_values_solution",
        "question_text": (
            f"Use the inspection table below to determine the value of $x$ for which the left-hand side "
            f"equals the right-hand side in the equation:\n"
            f"$${m1}x + {c1} = x + {c2}$$\n\n"
            f"{table_md}"
        ),
        "correct_answer": str(x_sol),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Locate column where LHS value equals RHS value ({m1 * x_sol + c1})", "marks": 1},
            {"step": f"Read corresponding x-value: x = {x_sol}", "marks": 1},
        ],
        "hints": [
            "Look through the columns of the table and find the column where the row for LHS and RHS have identical outputs.",
            f"Notice that when $x = {x_sol}$, both expressions evaluate to ${m1 * x_sol + c1}$.",
            f"The solution is $x = {x_sol}$.",
        ],
    }


def arch_04_balance_scale_model_two_step_equation(rng: random.Random) -> Dict[str, Any]:
    """Balance scale visual model (SVG) representing ax + b = c."""
    seed = rng.randint(1, 1_000_000)
    a = rng.choice([2, 3, 4])
    x_val = rng.choice([3, 4, 5])
    b = rng.choice([2, 5, 7])
    c = a * x_val + b

    left_label = f"{a}x + {b}"
    right_label = str(c)
    svg = draw_balance_scale_svg(left_label, right_label, seed=seed)

    return {
        "subskill": "04_balance_scale_model_two_step_equation",
        "question_text": (
            f"The beam scale below is in perfect balance, representing the equation $${a}x + {b} = {c}$$.\n\n"
            f"Find the value of the unknown block $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Subtract {b} from both sides: {a}x = {c - b}", "marks": 1},
            {"step": f"Divide by {a}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"To keep the scale balanced, remove ${b}$ from both pans: ${a}x = {c} - {b} = {c - b}$.",
            f"Now divide by ${a}$: $x = {c - b} \\div {a} = {x_val}$.",
            f"The value is $x = {x_val}$.",
        ],
    }


def arch_05_linear_one_step_additive_inverse(rng: random.Random) -> Dict[str, Any]:
    """Solve x - a = b using additive inverse."""
    a = rng.choice([14, 19, 23, 27, 35])
    b = rng.choice([15, 22, 28, 41])
    ans = a + b

    return {
        "subskill": "05_linear_one_step_additive_inverse",
        "question_text": (
            f"Solve the linear equation using the additive inverse:\n"
            f"$$x - {a} = {b}$$\n\n"
            f"Find $x$."
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Add {a} to both sides: x = {b} + {a}", "marks": 1},
            {"step": f"State solution x = {ans}", "marks": 1},
        ],
        "hints": [
            f"The additive inverse of $-{a}$ is $+{a}$. Add ${a}$ to both sides.",
            f"$x = {b} + {a}$.",
            f"$x = {ans}$.",
        ],
    }


def arch_06_linear_one_step_multiplicative_inverse(rng: random.Random) -> Dict[str, Any]:
    """Solve x / a = b using multiplicative inverse."""
    a = rng.choice([4, 5, 6, 7, 8])
    b = rng.choice([6, 7, 9, 12, 15])
    ans = a * b

    return {
        "subskill": "06_linear_one_step_multiplicative_inverse",
        "question_text": (
            f"Solve for $x$:\n$$\\frac{{x}}{{{a}}} = {b}$$"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply both sides by {a}: x = {b} * {a} = {ans}", "marks": 1},
        ],
        "hints": [
            f"The inverse of dividing by ${a}$ is multiplying by ${a}$.",
            f"Multiply both sides by ${a}$: $x = {b} \\times {a}$.",
            f"$x = {ans}$.",
        ],
    }


def arch_07_linear_two_step_positive_integers(rng: random.Random) -> Dict[str, Any]:
    """Solve ax + b = c with positive integer solution."""
    a = rng.choice([3, 4, 5, 6, 7])
    x_val = rng.choice([4, 5, 6, 7, 8])
    b = rng.choice([5, 8, 11, 14])
    c = a * x_val + b

    return {
        "subskill": "07_linear_two_step_positive_integers",
        "question_text": (
            f"Solve for $x$:\n$${a}x + {b} = {c}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Subtract {b} from both sides: {a}x = {c - b}", "marks": 1},
            {"step": f"Divide by {a}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"First isolate the variable term by subtracting ${b}$ from both sides: ${a}x = {c} - {b} = {c - b}$.",
            f"Then divide both sides by ${a}$: $x = \\frac{{{c - b}}}{{{a}}}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_08_linear_two_step_with_subtraction(rng: random.Random) -> Dict[str, Any]:
    """Solve ax - b = c."""
    a = rng.choice([3, 4, 5, 8])
    x_val = rng.choice([4, 6, 7, 9])
    b = rng.choice([7, 9, 13, 17])
    c = a * x_val - b

    return {
        "subskill": "08_linear_two_step_with_subtraction",
        "question_text": (
            f"Solve the linear equation:\n$${a}x - {b} = {c}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Add {b} to both sides: {a}x = {c + b}", "marks": 1},
            {"step": f"Divide by {a}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Add ${b}$ to both sides to cancel $-{b}$: ${a}x = {c} + {b} = {c + b}$.",
            f"Divide by ${a}$: $x = {c + b} \\div {a}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_09_linear_two_step_negative_coefficient(rng: random.Random) -> Dict[str, Any]:
    """Solve -ax + b = c with positive x."""
    a = rng.choice([2, 3, 4, 5])
    x_val = rng.choice([3, 4, 5, 6])
    c = rng.choice([2, 4, 7])
    b = c + a * x_val

    return {
        "subskill": "09_linear_two_step_negative_coefficient",
        "question_text": (
            f"Solve for $x$:\n$${b} - {a}x = {c}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Subtract {b} from both sides: -{a}x = {c - b}", "marks": 1},
            {"step": f"Divide by -{a}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Subtract ${b}$ from both sides: $-{a}x = {c} - {b} = {c - b}$.",
            f"Divide by $-{a}$: negative divided by negative gives positive: $x = \\frac{{{c - b}}}{{-{a}}}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_10_linear_two_step_negative_solution(rng: random.Random) -> Dict[str, Any]:
    """Solve ax + b = c where x < 0."""
    a = rng.choice([3, 4, 5])
    x_val = rng.choice([-6, -5, -4, -3, -2])
    c = rng.choice([4, 7, 10])
    b = c - a * x_val  # so ax + b = a*x_val + c - a*x_val = c

    return {
        "subskill": "10_linear_two_step_negative_solution",
        "question_text": (
            f"Solve the equation:\n$${a}x + {b} = {c}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Subtract {b} from both sides: {a}x = {c - b}", "marks": 1},
            {"step": f"Divide by {a}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Subtract ${b}$ from both sides: ${a}x = {c} - {b} = {c - b}$.",
            f"Divide by ${a}$: $x = \\frac{{{c - b}}}{{{a}}} = {x_val}$.",
            f"Result is $x = {x_val}$.",
        ],
    }


def arch_11_variables_both_sides_positive_integers(rng: random.Random) -> Dict[str, Any]:
    """Solve ax + b = cx + d where a > c and x > 0."""
    a = rng.choice([5, 6, 7])
    c = rng.choice([2, 3])
    x_val = rng.choice([3, 4, 5, 6])
    b = rng.choice([2, 4, 7])
    d = (a - c) * x_val + b

    return {
        "subskill": "11_variables_both_sides_positive_integers",
        "question_text": (
            f"Solve for $x$:\n$${a}x + {b} = {c}x + {d}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Group variable terms on LHS: ({a} - {c})x = {a - c}x", "marks": 1},
            {"step": f"Group constants on RHS: {d} - {b} = {d - b}", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Subtract ${c}x$ from both sides: $({a} - {c})x + {b} = {d} \\implies {a - c}x + {b} = {d}$.",
            f"Subtract ${b}$ from both sides: ${a - c}x = {d - b}$.",
            f"Divide by ${a - c}$: $x = {x_val}$.",
        ],
    }


def arch_12_variables_both_sides_negative_solution(rng: random.Random) -> Dict[str, Any]:
    """Solve ax + b = cx + d where x is negative."""
    a = 5
    c = 2
    x_val = rng.choice([-5, -4, -3, -2])
    d = rng.choice([4, 6, 10])
    b = d - (a - c) * x_val

    return {
        "subskill": "12_variables_both_sides_negative_solution",
        "question_text": (
            f"Solve for $x$:\n$${a}x + {b} = {c}x + {d}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Collect like terms: {a - c}x = {d - b}", "marks": 1},
            {"step": f"Divide to find negative solution: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Subtract ${c}x$ from both sides: ${a - c}x + {b} = {d}$.",
            f"Subtract ${b}$ from both sides: ${a - c}x = {d - b}$.",
            f"Divide by ${a - c}$: $x = {x_val}$.",
        ],
    }


def arch_13_variables_both_sides_fractional_solution(rng: random.Random) -> Dict[str, Any]:
    """Solve 4x + 3 = x + 8 yielding fraction 5/3."""
    ans = "5/3"

    return {
        "subskill": "13_variables_both_sides_fractional_solution",
        "question_text": (
            f"Solve for $x$ and leave your answer as a simplified fraction (e.g. 5/3):\n"
            f"$$4x + 3 = x + 8$$"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Subtract x from both sides: 3x + 3 = 8", "marks": 1},
            {"step": "Subtract 3 from both sides: 3x = 5", "marks": 1},
            {"step": "Divide by 3: x = 5/3", "marks": 1},
        ],
        "hints": [
            "Collect variable terms on the left: $4x - x = 3x$.",
            "Collect constants on the right: $8 - 3 = 5$.",
            f"Divide by 3: $x = {ans}$.",
        ],
    }


def arch_14_brackets_single_expansion(rng: random.Random) -> Dict[str, Any]:
    """Solve a(x + b) = c."""
    a = rng.choice([2, 3, 4, 5])
    b = rng.choice([2, 3, 4])
    x_val = rng.choice([3, 4, 5, 7])
    c = a * (x_val + b)

    return {
        "subskill": "14_brackets_single_expansion",
        "question_text": (
            f"Solve for $x$ by first expanding the brackets:\n"
            f"$${a}(x + {b}) = {c}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Expand brackets: {a}x + {a * b} = {c}", "marks": 1},
            {"step": f"Subtract {a * b} and divide by {a}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Expand using distributive property: ${a}x + {a * b} = {c}$.",
            f"Subtract ${a * b}$: ${a}x = {c - a * b}$.",
            f"Divide by ${a}$: $x = {x_val}$.",
        ],
    }


def arch_15_brackets_with_subtraction(rng: random.Random) -> Dict[str, Any]:
    """Solve a(x - b) = c."""
    a = rng.choice([3, 4, 6])
    b = rng.choice([2, 3, 5])
    x_val = rng.choice([6, 7, 8])
    c = a * (x_val - b)

    return {
        "subskill": "15_brackets_with_subtraction",
        "question_text": (
            f"Solve for $x$:\n$${a}(x - {b}) = {c}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Expand brackets: {a}x - {a * b} = {c}", "marks": 1},
            {"step": f"Add {a * b} and divide by {a}: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Distribute ${a}$: ${a}x - {a * b} = {c}$.",
            f"Add ${a * b}$ to both sides: ${a}x = {c + a * b}$.",
            f"Divide by ${a}$: $x = {x_val}$.",
        ],
    }


def arch_16_brackets_one_side_variable_other(rng: random.Random) -> Dict[str, Any]:
    """Solve a(x + b) = cx + d."""
    a = rng.choice([4, 5])
    c = 2
    b = rng.choice([1, 2])
    x_val = rng.choice([3, 4, 5])
    d = a * (x_val + b) - c * x_val

    return {
        "subskill": "16_brackets_one_side_variable_other",
        "question_text": (
            f"Solve the equation:\n$${a}(x + {b}) = {c}x + {d}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Expand LHS: {a}x + {a * b} = {c}x + {d}", "marks": 1},
            {"step": f"Rearrange to {a - c}x = {d - a * b}", "marks": 1},
            {"step": f"State solution x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Expand the LHS: ${a}x + {a * b} = {c}x + {d}$.",
            f"Subtract ${c}x$ from both sides: ${a - c}x + {a * b} = {d}$.",
            f"Subtract ${a * b}$ and divide by ${a - c}$: $x = {x_val}$.",
        ],
    }


def arch_17_brackets_both_sides(rng: random.Random) -> Dict[str, Any]:
    """Solve a(x + b) = c(x + d)."""
    a = 3
    c = 2
    b = rng.choice([2, 4])
    x_val = rng.choice([3, 5, 7])
    # a(x+b) = 3x + 3b; c(x+d) = 2x + 2d => x + 3b = 2d => 2d = x + 3b
    d_val = (x_val + a * b) // c
    x_val = c * d_val - a * b

    return {
        "subskill": "17_brackets_both_sides",
        "question_text": (
            f"Solve for $x$:\n$${a}(x + {b}) = {c}(x + {d_val})$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Expand both brackets: {a}x + {a * b} = {c}x + {c * d_val}", "marks": 1},
            {"step": f"Collect like terms: ({a} - {c})x = {c * d_val} - {a * b}", "marks": 1},
            {"step": f"State solution x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Expand left and right sides: ${a}x + {a * b} = {c}x + {c * d_val}$.",
            f"Subtract ${c}x$ from both sides: $x + {a * b} = {c * d_val}$.",
            f"Subtract ${a * b}$: $x = {x_val}$.",
        ],
    }


def arch_18_brackets_negative_multiplier(rng: random.Random) -> Dict[str, Any]:
    """Solve k - a(x - b) = c."""
    k = rng.choice([20, 25, 30])
    a = rng.choice([2, 3])
    b = 2
    x_val = rng.choice([4, 5, 6])
    c = k - a * (x_val - b)

    return {
        "subskill": "18_brackets_negative_multiplier",
        "question_text": (
            f"Solve for $x$:\n$${k} - {a}(x - {b}) = {c}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Distribute negative multiplier: {k} - {a}x + {a * b} = {c}", "marks": 1},
            {"step": f"Combine constants and solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Be careful with signs: $-{a} \\times (-{b}) = +{a * b}$.",
            f"LHS becomes: ${k} - {a}x + {a * b} = {k + a * b} - {a}x$.",
            f"Set equal to ${c}$ and solve: $x = {x_val}$.",
        ],
    }


def arch_19_brackets_two_terms_lhs(rng: random.Random) -> Dict[str, Any]:
    """Solve 2(x + 3) + 3(x + 1) = c."""
    x_val = rng.choice([2, 3, 4])
    c = 2 * (x_val + 3) + 3 * (x_val + 1)

    return {
        "subskill": "19_brackets_two_terms_lhs",
        "question_text": (
            f"Expand and solve the equation:\n$$2(x + 3) + 3(x + 1) = {c}$$"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Expand brackets: 2x + 6 + 3x + 3 = {c}", "marks": 1},
            {"step": f"Combine like terms: 5x + 9 = {c}", "marks": 1},
            {"step": f"Solve: 5x = {c - 9} => x = {x_val}", "marks": 1},
        ],
        "hints": [
            "Expand both brackets: $2x + 6 + 3x + 3$.",
            f"Combine like terms: $5x + 9 = {c}$.",
            f"Subtract 9 and divide by 5: $x = {x_val}$.",
        ],
    }


def arch_20_geometric_supplementary_angles_equation(rng: random.Random) -> Dict[str, Any]:
    """Solve equation derived from supplementary angles on a straight line: (2x + 10) + (x + 20) = 180."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([40, 45, 50])
    a = 2
    b = 10
    d = 180 - (a * x_val + b) - x_val
    ang1_str = f"{a}x + {b}°"
    ang2_str = f"x + {d}°"
    svg = draw_geometric_equation_straight_line_angles_svg(ang1_str, ang2_str, seed=seed)

    return {
        "subskill": "20_geometric_supplementary_angles_equation",
        "question_text": (
            f"In the geometric diagram below, $\\angle AMC$ and $\\angle CMB$ lie on a straight line $AB$.\n"
            f"Given that $\\angle AMC = {ang1_str}$ and $\\angle CMB = {ang2_str}$:\n\n"
            f"Set up an equation and solve for $x$ (in degrees):"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Write geometric equation: ({ang1_str}) + ({ang2_str}) = 180° (angles on a straight line)", "marks": 1},
            {"step": f"Combine terms: 3x + {b + d} = 180", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            "Angles on a straight line add up to $180^\\circ$.",
            f"Set up the equation: $({a}x + {b}) + (x + {d}) = 180$.",
            f"Combine like terms: $3x + {b + d} = 180 \\implies 3x = {180 - b - d} \\implies x = {x_val}$.",
        ],
    }


def arch_21_geometric_triangle_angles_sum_equation(rng: random.Random) -> Dict[str, Any]:
    """Solve for x when angles of a triangle sum to 180: x + 2x + 3x = 180."""
    x_val = 30

    return {
        "subskill": "21_geometric_triangle_angles_sum_equation",
        "question_text": (
            f"The three interior angles of a triangle are $x$, $2x$, and $3x$.\n\n"
            f"Calculate the value of $x$ in degrees."
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State angle sum of triangle: x + 2x + 3x = 180°", "marks": 1},
            {"step": f"Solve: 6x = 180° => x = {x_val}", "marks": 1},
        ],
        "hints": [
            "The interior angles of any triangle always sum to $180^\\circ$.",
            "Equation: $x + 2x + 3x = 180^\\circ$.",
            f"$6x = 180^\\circ \\implies x = {x_val}$.",
        ],
    }


def arch_22_geometric_vertically_opposite_angles(rng: random.Random) -> Dict[str, Any]:
    """Solve for x using vertically opposite angles: 3x - 10 = x + 40."""
    x_val = 25

    return {
        "subskill": "22_geometric_vertically_opposite_angles",
        "question_text": (
            f"Two straight lines intersect to form vertically opposite angles measuring "
            f"$(3x - 10)^\\circ$ and $(x + 40)^\\circ$.\n\n"
            f"Solve for $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Set angles equal: 3x - 10 = x + 40 (vertically opposite angles)", "marks": 1},
            {"step": f"Solve 2x = 50 => x = {x_val}", "marks": 1},
        ],
        "hints": [
            "Vertically opposite angles are equal.",
            "Equate the two angles: $3x - 10 = x + 40$.",
            f"Subtract $x$ and add 10: $2x = 50 \\implies x = {x_val}$.",
        ],
    }


def arch_23_geometric_perimeter_rectangle_equation(rng: random.Random) -> Dict[str, Any]:
    """Solve for x using perimeter formula P = 2(l + b)."""
    x_val = rng.choice([4, 5, 6])
    # length = 2x + 3, width = x + 1
    # perimeter = 2(3x + 4) = 6x + 8
    p = 6 * x_val + 8

    return {
        "subskill": "23_geometric_perimeter_rectangle_equation",
        "question_text": (
            f"A rectangle has a length of $(2x + 3)\\text{{ cm}}$ and a breadth of $(x + 1)\\text{{ cm}}$.\n"
            f"Its total perimeter is ${p}\\text{{ cm}}$.\n\n"
            f"Solve for $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up perimeter formula: 2[(2x + 3) + (x + 1)] = {p}", "marks": 1},
            {"step": f"Simplify: 6x + 8 = {p}", "marks": 1},
            {"step": f"Solve: 6x = {p - 8} => x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Perimeter of rectangle $= 2(\\text{{length}} + \\text{{breadth}})$.",
            f"$2[(2x + 3) + (x + 1)] = 2(3x + 4) = 6x + 8 = {p}$.",
            f"$6x = {p - 8} \\implies x = {x_val}$.",
        ],
    }


def arch_24_check_solution_by_substitution(rng: random.Random) -> Dict[str, Any]:
    """Check whether a given candidate value satisfies an equation."""
    a = 4
    b = 7
    c = 27
    # 4x + 7 = 27 => 4x = 20 => x = 5
    candidate = 5

    return {
        "subskill": "24_check_solution_by_substitution",
        "question_text": (
            f"Verify by substitution whether **$x = {candidate}$** is a valid solution to the equation:\n"
            f"$${a}x + {b} = {c}$$\n\n"
            f"Calculate the value of the Left Hand Side (LHS) when $x = {candidate}$:"
        ),
        "correct_answer": str(c),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Substitute x = {candidate} into LHS: {a}({candidate}) + {b} = {a * candidate + b}", "marks": 1},
            {"step": f"Confirm LHS equals RHS ({c})", "marks": 1},
        ],
        "hints": [
            f"Substitute ${candidate}$ into the LHS: ${a}({candidate}) + {b}$.",
            f"${a * candidate} + {b} = {c}$.",
            f"The value of the LHS is ${c}$.",
        ],
    }


def arch_25_word_problem_consecutive_integers(rng: random.Random) -> Dict[str, Any]:
    """Word problem: sum of three consecutive integers is N. Find the smallest integer."""
    first = rng.choice([11, 14, 17, 21, 25])
    total = first + (first + 1) + (first + 2)

    return {
        "subskill": "25_word_problem_consecutive_integers",
        "question_text": (
            f"The sum of three consecutive integers is ${total}$.\n\n"
            f"Find the value of the **smallest** integer."
        ),
        "correct_answer": str(first),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Set up equation: n + (n + 1) + (n + 2) = {total}", "marks": 1},
            {"step": f"Simplify: 3n + 3 = {total} => 3n = {total - 3}", "marks": 1},
            {"step": f"Solve for smallest integer: n = {first}", "marks": 1},
        ],
        "hints": [
            "Let the three consecutive integers be $n$, $n + 1$, and $n + 2$.",
            f"Sum: $3n + 3 = {total}$.",
            f"$3n = {total - 3} \\implies n = {first}$.",
        ],
    }
