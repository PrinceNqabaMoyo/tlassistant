"""Grade 9 Mathematics - Geometry of Straight Lines Archetypes (01 to 25).
Grounded strictly in:
  - curriculum_docs_auto/Mathematics_Gr9/Term 2/03. Geometry of straight lines.md

Covers:
  - Vertically opposite angles (numeric and algebraic equations)
  - Adjacent angles on a straight line (two and three angles, numeric and algebraic)
  - Perpendicular lines and complementary adjacent angles
  - Angles around a point (revolution)
  - Intersecting lines complete 4-angle systems
  - Parallel lines cut by a transversal:
    - Corresponding angles (numeric, algebraic, calculating angle size)
    - Alternate interior angles (numeric, algebraic, calculating angle size)
    - Co-interior angles summing to 180 degrees (numeric, algebraic, calculating angle size)
    - Full 8-angle deduction networks
    - Formal Euclidean [Statement | Reason] geometry proofs
    - Error analysis: confusing alternate and co-interior angles
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .geometry_straight_lines_svg import (
    draw_angles_around_point_svg,
    draw_intersecting_lines_svg,
    draw_parallel_transversal_svg,
    draw_straight_line_adjacent_angles_svg,
)


def arch_01_vertically_opposite_angles_numeric(rng: random.Random) -> Dict[str, Any]:
    """Calculate vertically opposite angle with reason [vert opp angles]."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([42, 54, 63, 71, 78, 115, 126, 134])
    svg = draw_intersecting_lines_svg({"top": f"{theta}°", "bottom": "x"}, seed=seed)

    return {
        "subskill": "01_vertically_opposite_angles_numeric",
        "question_text": (
            f"Straight lines $AB$ and $CD$ intersect at point $O$ as shown in the diagram below.\n\n"
            f"If $\\hat{{O}}_1 = {theta}^\\circ$, calculate the size of angle $x$ (in degrees) "
            f"and provide the standard geometric reason:"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State equation: x = {theta}°", "marks": 1},
            {"step": "State correct reason: [vert opp ∠s]", "marks": 1},
        ],
        "hints": [
            "When two straight lines cross, the angles opposite each other at the intersection vertex are called vertically opposite angles.",
            "Vertically opposite angles are always equal to each other [vert opp $\\angle$s].",
            f"$x = {theta}^\\circ$.",
        ],
    }


def arch_02_vertically_opposite_angles_algebraic_linear(rng: random.Random) -> Dict[str, Any]:
    """Solve linear equation for x from vertically opposite angles."""
    seed = rng.randint(1, 1_000_000)
    a = 3
    c = 1
    x_val = rng.choice([15, 20, 25, 30])
    b = rng.choice([10, 15, 20])
    d = (a - c) * x_val + b

    svg = draw_intersecting_lines_svg({"top": f"{a}x + {b}°", "bottom": f"x + {d}°"}, seed=seed)

    return {
        "subskill": "02_vertically_opposite_angles_algebraic_linear",
        "question_text": (
            f"In the diagram below, lines $AB$ and $CD$ intersect at point $O$.\n\n"
            f"Given that $\\hat{{O}}_1 = ({a}x + {b})^\\circ$ and $\\hat{{O}}_3 = (x + {d})^\\circ$ are vertically opposite angles, "
            f"calculate the value of $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Equate angles with reason: {a}x + {b} = x + {d} [vert opp ∠s]", "marks": 1},
            {"step": f"Transpose terms: 2x = {d - b}", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Since the angles are vertically opposite, set them equal: ${a}x + {b} = x + {d}$.",
            f"Subtract $x$ and subtract ${b}$: $2x = {d - b}$.",
            f"Divide by $2$: $x = {x_val}$.",
        ],
    }


def arch_03_vertically_opposite_angles_calculate_angle_size(rng: random.Random) -> Dict[str, Any]:
    """Solve for x, then calculate the numerical size of the angle in degrees."""
    seed = rng.randint(1, 1_000_000)
    a, c = 4, 1
    x_val = rng.choice([12, 14, 16, 18])
    b = rng.choice([8, 12, 16])
    d = (a - c) * x_val + b
    angle_size = a * x_val + b

    svg = draw_intersecting_lines_svg({"top": f"{a}x + {b}°", "bottom": f"x + {d}°"}, seed=seed)

    return {
        "subskill": "03_vertically_opposite_angles_calculate_angle_size",
        "question_text": (
            f"Straight lines $AB$ and $CD$ intersect at $O$ as shown below.\n\n"
            f"If $\\hat{{O}}_1 = ({a}x + {b})^\\circ$ and $\\hat{{O}}_3 = (x + {d})^\\circ$:\n"
            f"Solve for $x$, and hence calculate the size of $\\hat{{O}}_1$ in degrees:"
        ),
        "correct_answer": str(angle_size),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Equate: {a}x + {b} = x + {d} [vert opp ∠s] => x = {x_val}", "marks": 1},
            {"step": f"Substitute x into angle expression: {a}({x_val}) + {b} = {angle_size}°", "marks": 1},
        ],
        "hints": [
            f"Equate vertically opposite angles: ${a}x + {b} = x + {d} \\implies 3x = {d - b} \\implies x = {x_val}$.",
            f"Now substitute $x = {x_val}$ into ${a}x + {b}$: ${a}({x_val}) + {b}$.",
            f"The angle size is ${angle_size}^\\circ$.",
        ],
    }


def arch_04_adjacent_angles_straight_line_numeric_two_angles(rng: random.Random) -> Dict[str, Any]:
    """Calculate unknown angle on a straight line: theta + x = 180."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([48, 55, 64, 72, 85, 112, 125, 138])
    ans = 180 - theta
    svg = draw_straight_line_adjacent_angles_svg(f"{theta}°", "x", seed=seed)

    return {
        "subskill": "04_adjacent_angles_straight_line_numeric_two_angles",
        "question_text": (
            f"In the diagram below, $AB$ is a straight line and ray $MC$ originates from point $M$.\n\n"
            f"Given that $A\\hat{{M}}C = {theta}^\\circ$, calculate the size of angle $x$ in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State supplementary equation: {theta}° + x = 180° [∠s on a str line]", "marks": 1},
            {"step": f"Calculate x: x = {ans}°", "marks": 1},
        ],
        "hints": [
            "Adjacent angles on a straight line are supplementary, meaning they add up to $180^\\circ$ [$\\angle$s on a str line].",
            f"Set up equation: ${theta}^\\circ + x = 180^\\circ$.",
            f"$x = 180^\\circ - {theta}^\\circ = {ans}^\\circ$.",
        ],
    }


def arch_05_adjacent_angles_straight_line_numeric_three_angles(rng: random.Random) -> Dict[str, Any]:
    """Three angles on straight line: theta1 + theta2 + x = 180."""
    seed = rng.randint(1, 1_000_000)
    theta1 = rng.choice([35, 42, 50])
    theta2 = rng.choice([55, 63, 70])
    ans = 180 - (theta1 + theta2)
    svg = draw_straight_line_adjacent_angles_svg(f"{theta1}°", f"{theta2}°", "x", seed=seed)

    return {
        "subskill": "05_adjacent_angles_straight_line_numeric_three_angles",
        "question_text": (
            f"Line $AB$ is a straight line. Three adjacent angles lie along the line: "
            f"${theta1}^\\circ$, ${theta2}^\\circ$, and $x$, as shown below.\n\n"
            f"Calculate the value of $x$ in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Set up equation: {theta1}° + {theta2}° + x = 180° [∠s on a str line]", "marks": 1},
            {"step": f"Solve for x: x = {ans}°", "marks": 1},
        ],
        "hints": [
            "All angles along a straight line sum to $180^\\circ$ [$\\angle$s on a str line].",
            f"${theta1}^\\circ + {theta2}^\\circ + x = 180^\\circ \\implies {theta1 + theta2}^\\circ + x = 180^\\circ$.",
            f"$x = 180^\\circ - {theta1 + theta2}^\\circ = {ans}^\\circ$.",
        ],
    }


def arch_06_adjacent_angles_straight_line_algebraic_linear(rng: random.Random) -> Dict[str, Any]:
    """Solve (2x + b) + (3x + d) = 180 for x."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([20, 22, 24, 26, 28])
    # 5x + b + d = 180 => b + d = 180 - 5x
    rem = 180 - 5 * x_val
    b = rng.choice([10, 15, 20])
    d = rem - b
    svg = draw_straight_line_adjacent_angles_svg(f"2x + {b}°", f"3x + {d}°", seed=seed)

    return {
        "subskill": "06_adjacent_angles_straight_line_algebraic_linear",
        "question_text": (
            f"In the diagram below, $AB$ is a straight line.\n\n"
            f"If the two adjacent angles are $(2x + {b})^\\circ$ and $(3x + {d})^\\circ$, "
            f"calculate the value of $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Write equation: (2x + {b}) + (3x + {d}) = 180 [∠s on a str line]", "marks": 1},
            {"step": f"Collect like terms: 5x + {b + d} = 180", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            "Adjacent angles on a straight line add up to $180^\\circ$: $(2x + {b}) + (3x + {d}) = 180$.",
            f"Combine like terms: $5x + {b + d} = 180 \\implies 5x = {180 - (b + d)}$.",
            f"Divide by $5$: $x = {x_val}$.",
        ],
    }


def arch_07_adjacent_angles_straight_line_algebraic_three_angles(rng: random.Random) -> Dict[str, Any]:
    """Solve ax + bx + cx = 180."""
    seed = rng.randint(1, 1_000_000)
    a, b, c = 2, 3, 4
    # 9x = 180 => x = 20
    x_val = 20
    svg = draw_straight_line_adjacent_angles_svg(f"{a}x", f"{b}x", f"{c}x", seed=seed)

    return {
        "subskill": "07_adjacent_angles_straight_line_algebraic_three_angles",
        "question_text": (
            f"Along straight line $AB$, three adjacent angles are given algebraically as "
            f"${a}x$, ${b}x$, and ${c}x$, as shown below.\n\n"
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
            {"step": f"Set up equation: {a}x + {b}x + {c}x = 180 [∠s on a str line]", "marks": 1},
            {"step": f"Combine terms: {a + b + c}x = 180", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Sum of angles on a straight line is $180^\\circ$: ${a}x + ${b}x + ${c}x = 180$.",
            f"${a + b + c}x = 180$.",
            f"$x = 180 \\div {a + b + c} = {x_val}$.",
        ],
    }


def arch_08_perpendicular_adjacent_angles_numeric(rng: random.Random) -> Dict[str, Any]:
    """Perpendicular ray forming complementary angles: theta + x = 90."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([25, 34, 42, 51, 63, 72])
    ans = 90 - theta
    svg = draw_straight_line_adjacent_angles_svg(f"{theta}°", "x", ray_angle_deg=90.0, seed=seed)

    return {
        "subskill": "08_perpendicular_adjacent_angles_numeric",
        "question_text": (
            f"In the diagram below, ray $MC$ is perpendicular to line $AB$ ($MC \\perp AB$), forming a right angle.\n\n"
            f"If one adjacent angle is ${theta}^\\circ$, calculate the size of angle $x$ in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State complementary equation: {theta}° + x = 90° [MC ⊥ AB]", "marks": 1},
            {"step": f"Calculate x: x = {ans}°", "marks": 1},
        ],
        "hints": [
            "Perpendicular lines form a right angle ($90^\\circ$).",
            f"${theta}^\\circ + x = 90^\\circ$.",
            f"$x = 90^\\circ - {theta}^\\circ = {ans}^\\circ$.",
        ],
    }


def arch_09_perpendicular_adjacent_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    """Solve (2x + b) + (x + d) = 90."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([15, 18, 20, 22])
    # 3x + b + d = 90 => b + d = 90 - 3x
    rem = 90 - 3 * x_val
    b = rng.choice([4, 6, 8])
    d = rem - b
    svg = draw_straight_line_adjacent_angles_svg(f"2x + {b}°", f"x + {d}°", ray_angle_deg=90.0, seed=seed)

    return {
        "subskill": "09_perpendicular_adjacent_angles_algebraic",
        "question_text": (
            f"Ray $MC$ is perpendicular to line $AB$ ($MC \\perp AB$), so the total angle is $90^\\circ$.\n\n"
            f"Given the two complementary angles $(2x + {b})^\\circ$ and $(x + {d})^\\circ$ in the diagram below:\n"
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
            {"step": f"Set up equation: (2x + {b}) + (x + {d}) = 90 [given MC ⊥ AB]", "marks": 1},
            {"step": f"Collect like terms: 3x + {b + d} = 90", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"The two angles sum to $90^\\circ$: $(2x + {b}) + (x + {d}) = 90$.",
            f"$3x + {b + d} = 90 \\implies 3x = {90 - (b + d)}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_10_angles_around_a_point_revolution_numeric(rng: random.Random) -> Dict[str, Any]:
    """Three angles around a point sum to 360 degrees."""
    seed = rng.randint(1, 1_000_000)
    theta1 = rng.choice([105, 115, 125])
    theta2 = rng.choice([120, 130, 140])
    ans = 360 - theta1 - theta2
    svg = draw_angles_around_point_svg([f"{theta1}°", f"{theta2}°", "x"], seed=seed)

    return {
        "subskill": "10_angles_around_a_point_revolution_numeric",
        "question_text": (
            f"Three angles meet around vertex point $O$ as shown below.\n\n"
            f"Given angles of ${theta1}^\\circ$ and ${theta2}^\\circ$, calculate the size of angle $x$ in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State revolution equation: {theta1}° + {theta2}° + x = 360° [∠s around a pt]", "marks": 1},
            {"step": f"Solve for x: x = {ans}°", "marks": 1},
        ],
        "hints": [
            "Angles meeting around a single point form a complete revolution and sum to $360^\\circ$ [$\\angle$s around a pt].",
            f"${theta1}^\\circ + {theta2}^\\circ + x = 360^\\circ \\implies {theta1 + theta2}^\\circ + x = 360^\\circ$.",
            f"$x = 360^\\circ - {theta1 + theta2}^\\circ = {ans}^\\circ$.",
        ],
    }


def arch_11_angles_around_a_point_revolution_algebraic(rng: random.Random) -> Dict[str, Any]:
    """Four angles around a point: 2x + 3x + 4x + 3x = 360."""
    seed = rng.randint(1, 1_000_000)
    a, b, c, d = 2, 3, 4, 3
    # 12x = 360 => x = 30
    x_val = 30
    svg = draw_angles_around_point_svg([f"{a}x", f"{b}x", f"{c}x", f"{d}x"], seed=seed)

    return {
        "subskill": "11_angles_around_a_point_revolution_algebraic",
        "question_text": (
            f"Four angles are arranged around a single vertex $O$: "
            f"${a}x$, ${b}x$, ${c}x$, and ${d}x$, as shown in the diagram below.\n\n"
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
            {"step": f"Sum angles to 360: {a}x + {b}x + {c}x + {d}x = 360 [∠s around a pt]", "marks": 1},
            {"step": f"Collect like terms: {a + b + c + d}x = 360", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"The sum of angles around a point is $360^\\circ$: ${a}x + ${b}x + ${c}x + ${d}x = 360$.",
            f"${a + b + c + d}x = 360$.",
            f"$x = 360 \\div {a + b + c + d} = {x_val}$.",
        ],
    }


def arch_12_intersecting_lines_four_angles_complete_set(rng: random.Random) -> Dict[str, Any]:
    """Given acute angle theta at intersection, calculate adjacent obtuse angle y."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([40, 50, 65, 75, 80])
    ans = 180 - theta
    svg = draw_intersecting_lines_svg({"top": f"{theta}°", "right": "y", "bottom": f"{theta}°"}, seed=seed)

    return {
        "subskill": "12_intersecting_lines_four_angles_complete_set",
        "question_text": (
            f"Two straight lines cross at vertex $O$ as shown below.\n\n"
            f"If $\\hat{{O}}_1 = {theta}^\\circ$, calculate the size of adjacent angle $y$ in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State supplementary angle relation: {theta}° + y = 180° [∠s on a str line]", "marks": 1},
            {"step": f"Solve for y: y = {ans}°", "marks": 1},
        ],
        "hints": [
            "Adjacent angles on a straight line add up to $180^\\circ$ [$\\angle$s on a str line].",
            f"${theta}^\\circ + y = 180^\\circ$.",
            f"$y = 180^\\circ - {theta}^\\circ = {ans}^\\circ$.",
        ],
    }


def arch_13_parallel_lines_corresponding_angles_numeric(rng: random.Random) -> Dict[str, Any]:
    """Parallel lines cut by transversal: corresponding angles are equal."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([45, 58, 67, 74, 82, 115, 128])
    svg = draw_parallel_transversal_svg({"G2": f"{theta}°", "H2": "x"}, seed=seed)

    return {
        "subskill": "13_parallel_lines_corresponding_angles_numeric",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$), cut by transversal $EF$ as shown below.\n\n"
            f"If $\\hat{{G}}_2 = {theta}^\\circ$, calculate the size of corresponding angle $x$ in degrees:"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State angle equality: x = {theta}°", "marks": 1},
            {"step": "State reason: [corresp ∠s, AB || CD]", "marks": 1},
        ],
        "hints": [
            "Corresponding angles occupy matching positions (F-shape) at each intersection along parallel lines.",
            "Corresponding angles are equal when lines are parallel [corresp $\\angle$s, $AB \\parallel CD$].",
            f"$x = {theta}^\\circ$.",
        ],
    }


def arch_14_parallel_lines_corresponding_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    """Solve linear equation from corresponding angles: 3x + b = x + d."""
    seed = rng.randint(1, 1_000_000)
    a, c = 3, 1
    x_val = rng.choice([15, 20, 25, 30])
    b = rng.choice([10, 15, 20])
    d = (a - c) * x_val + b
    svg = draw_parallel_transversal_svg({"G2": f"{a}x + {b}°", "H2": f"x + {d}°"}, seed=seed)

    return {
        "subskill": "14_parallel_lines_corresponding_angles_algebraic",
        "question_text": (
            f"In the diagram below, $AB \\parallel CD$.\n\n"
            f"Corresponding angles are $\\hat{{G}}_2 = ({a}x + {b})^\\circ$ and $\\hat{{H}}_2 = (x + {d})^\\circ$.\n"
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
            {"step": f"Equate: {a}x + {b} = x + {d} [corresp ∠s, AB || CD]", "marks": 1},
            {"step": f"Subtract x and {b}: 2x = {d - b}", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Corresponding angles on parallel lines are equal: ${a}x + {b} = x + {d}$.",
            f"$2x = {d - b}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_15_parallel_lines_corresponding_angles_calculate_angle(rng: random.Random) -> Dict[str, Any]:
    """Calculate x, then calculate size of corresponding angle."""
    seed = rng.randint(1, 1_000_000)
    a, c = 3, 1
    x_val = rng.choice([15, 20, 25])
    b = rng.choice([10, 15])
    d = (a - c) * x_val + b
    angle_size = a * x_val + b
    svg = draw_parallel_transversal_svg({"G2": f"{a}x + {b}°", "H2": f"x + {d}°"}, seed=seed)

    return {
        "subskill": "15_parallel_lines_corresponding_angles_calculate_angle",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"Given corresponding angles $\\hat{{G}}_2 = ({a}x + {b})^\\circ$ and $\\hat{{H}}_2 = (x + {d})^\\circ$:\n"
            f"Solve for $x$, and calculate the size of $\\hat{{G}}_2$ in degrees:"
        ),
        "correct_answer": str(angle_size),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Solve for x: {a}x + {b} = x + {d} => x = {x_val}", "marks": 1},
            {"step": f"Calculate angle: {a}({x_val}) + {b} = {angle_size}°", "marks": 1},
        ],
        "hints": [
            f"Equate: ${a}x + {b} = x + {d} \\implies 2x = {d - b} \\implies x = {x_val}$.",
            f"Substitute $x = {x_val}$: ${a}({x_val}) + {b} = {angle_size}^\\circ$.",
            f"The angle size is ${angle_size}^\\circ$.",
        ],
    }


def arch_16_parallel_lines_alternate_angles_numeric(rng: random.Random) -> Dict[str, Any]:
    """Alternate interior angles (Z-shape) are equal."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([48, 56, 65, 73, 82])
    svg = draw_parallel_transversal_svg({"G4": f"{theta}°", "H1": "x"}, seed=seed)

    return {
        "subskill": "16_parallel_lines_alternate_angles_numeric",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$) as shown below.\n\n"
            f"If $\\hat{{G}}_4 = {theta}^\\circ$, calculate the size of alternate interior angle $x$ in degrees:"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State x = {theta}°", "marks": 1},
            {"step": "State reason: [alt ∠s, AB || CD]", "marks": 1},
        ],
        "hints": [
            "Alternate interior angles lie on opposite sides of the transversal between parallel lines (Z-shape).",
            "Alternate angles are equal when lines are parallel [alt $\\angle$s, $AB \\parallel CD$].",
            f"$x = {theta}^\\circ$.",
        ],
    }


def arch_17_parallel_lines_alternate_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    """Solve linear equation from alternate interior angles."""
    seed = rng.randint(1, 1_000_000)
    a, c = 4, 2
    x_val = rng.choice([15, 20, 25])
    b = rng.choice([10, 15])
    d = (a - c) * x_val - b
    svg = draw_parallel_transversal_svg({"G4": f"{a}x - {b}°", "H1": f"{c}x + {d}°"}, seed=seed)

    return {
        "subskill": "17_parallel_lines_alternate_angles_algebraic",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"Alternate interior angles are $\\hat{{G}}_4 = ({a}x - {b})^\\circ$ and $\\hat{{H}}_1 = ({c}x + {d})^\\circ$.\n"
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
            {"step": f"Equate: {a}x - {b} = {c}x + {d} [alt ∠s, AB || CD]", "marks": 1},
            {"step": f"Transpose terms: 2x = {d + b}", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Alternate angles are equal: ${a}x - {b} = {c}x + {d}$.",
            f"${a - c}x = {d + b}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_18_parallel_lines_alternate_angles_calculate_angle(rng: random.Random) -> Dict[str, Any]:
    """Calculate x, then determine size of alternate interior angle."""
    seed = rng.randint(1, 1_000_000)
    a, c = 4, 2
    x_val = rng.choice([15, 18, 22])
    b = rng.choice([10, 14])
    d = (a - c) * x_val - b
    angle_size = a * x_val - b
    svg = draw_parallel_transversal_svg({"G4": f"{a}x - {b}°", "H1": f"{c}x + {d}°"}, seed=seed)

    return {
        "subskill": "18_parallel_lines_alternate_angles_calculate_angle",
        "question_text": (
            f"In the diagram below, $AB \\parallel CD$.\n\n"
            f"Given $\\hat{{G}}_4 = ({a}x - {b})^\\circ$ and $\\hat{{H}}_1 = ({c}x + {d})^\\circ$:\n"
            f"Solve for $x$, and calculate the size of angle $\\hat{{G}}_4$ in degrees:"
        ),
        "correct_answer": str(angle_size),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Solve for x: {a}x - {b} = {c}x + {d} => x = {x_val}", "marks": 1},
            {"step": f"Calculate angle: {a}({x_val}) - {b} = {angle_size}°", "marks": 1},
        ],
        "hints": [
            f"Equate: ${a}x - {b} = {c}x + {d} \\implies 2x = {d + b} \\implies x = {x_val}$.",
            f"Substitute $x = {x_val}$: ${a}({x_val}) - {b} = {angle_size}^\\circ$.",
            f"The angle size is ${angle_size}^\\circ$.",
        ],
    }


def arch_19_parallel_lines_cointerior_angles_numeric(rng: random.Random) -> Dict[str, Any]:
    """Co-interior angles (C-shape) sum to 180 degrees."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([65, 75, 80, 105, 115, 125])
    ans = 180 - theta
    svg = draw_parallel_transversal_svg({"G4": f"{theta}°", "H2": "x"}, seed=seed)

    return {
        "subskill": "19_parallel_lines_cointerior_angles_numeric",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$) as shown below.\n\n"
            f"If $\\hat{{G}}_4 = {theta}^\\circ$, calculate the size of co-interior angle $x$ in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"State supplementary equation: {theta}° + x = 180° [co-int ∠s, AB || CD]", "marks": 1},
            {"step": f"Calculate x: x = {ans}°", "marks": 1},
        ],
        "hints": [
            "Co-interior angles lie on the same side of the transversal between the parallel lines (C-shape).",
            "Co-interior angles are supplementary (add to $180^\\circ$) when lines are parallel [co-int $\\angle$s, $AB \\parallel CD$].",
            f"$x = 180^\\circ - {theta}^\\circ = {ans}^\\circ$.",
        ],
    }


def arch_20_parallel_lines_cointerior_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    """Solve (2x + b) + (3x + d) = 180 from co-interior angles."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([20, 22, 24, 26])
    rem = 180 - 5 * x_val
    b = rng.choice([10, 15, 20])
    d = rem - b
    svg = draw_parallel_transversal_svg({"G4": f"2x + {b}°", "H2": f"3x + {d}°"}, seed=seed)

    return {
        "subskill": "20_parallel_lines_cointerior_angles_algebraic",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"Co-interior angles are $\\hat{{G}}_4 = (2x + {b})^\\circ$ and $\\hat{{H}}_2 = (3x + {d})^\\circ$.\n"
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
            {"step": f"Write equation: (2x + {b}) + (3x + {d}) = 180 [co-int ∠s, AB || CD]", "marks": 1},
            {"step": f"Simplify: 5x + {b + d} = 180", "marks": 1},
            {"step": f"Solve for x: x = {x_val}", "marks": 1},
        ],
        "hints": [
            f"Co-interior angles add to $180^\\circ$: $(2x + {b}) + (3x + {d}) = 180$.",
            f"$5x + {b + d} = 180 \\implies 5x = {180 - (b + d)}$.",
            f"$x = {x_val}$.",
        ],
    }


def arch_21_parallel_lines_cointerior_angles_calculate_angle(rng: random.Random) -> Dict[str, Any]:
    """Calculate x, then determine size of obtuse co-interior angle."""
    seed = rng.randint(1, 1_000_000)
    x_val = rng.choice([20, 22, 24])
    rem = 180 - 5 * x_val
    b = 10
    d = rem - b
    obtuse_angle = 3 * x_val + d
    svg = draw_parallel_transversal_svg({"G4": f"2x + {b}°", "H2": f"3x + {d}°"}, seed=seed)

    return {
        "subskill": "21_parallel_lines_cointerior_angles_calculate_angle",
        "question_text": (
            f"In the diagram below, $AB \\parallel CD$.\n\n"
            f"Given co-interior angles $\\hat{{G}}_4 = (2x + {b})^\\circ$ and $\\hat{{H}}_2 = (3x + {d})^\\circ$:\n"
            f"Solve for $x$, and calculate the size of obtuse angle $\\hat{{H}}_2$ in degrees:"
        ),
        "correct_answer": str(obtuse_angle),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Solve for x: 5x + {b + d} = 180 => x = {x_val}", "marks": 1},
            {"step": f"Calculate angle: 3({x_val}) + {d} = {obtuse_angle}°", "marks": 1},
        ],
        "hints": [
            f"Sum to $180^\\circ$: $(2x + {b}) + (3x + {d}) = 180 \\implies 5x = {180 - (b + d)} \\implies x = {x_val}$.",
            f"Substitute into $\\hat{{H}}_2$: $3({x_val}) + {d} = {obtuse_angle}^\\circ$.",
            f"The angle size is ${obtuse_angle}^\\circ$.",
        ],
    }


def arch_22_parallel_transversal_full_eight_angles_deduction(rng: random.Random) -> Dict[str, Any]:
    """Deduce angle in 8-angle network from exterior angle."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([55, 65, 75, 80])
    ans = 180 - theta
    svg = draw_parallel_transversal_svg({"G1": f"{theta}°", "H2": "x"}, seed=seed)

    return {
        "subskill": "22_parallel_transversal_full_eight_angles_deduction",
        "question_text": (
            f"Lines $AB$ and $CD$ are parallel ($AB \\parallel CD$).\n\n"
            f"If $\\hat{{G}}_1 = {theta}^\\circ$ as shown in the diagram below, "
            f"calculate the size of interior angle $x$ in degrees:"
        ),
        "correct_answer": str(ans),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Find corresponding angle H1 = {theta}° [corresp ∠s, AB || CD]", "marks": 1},
            {"step": f"Calculate supplementary adjacent angle x = 180° - {theta}° = {ans}° [∠s on a str line]", "marks": 1},
        ],
        "hints": [
            f"Notice that $\\hat{{H}}_1 = \\hat{{G}}_1 = {theta}^\\circ$ [corresp $\\angle$s, $AB \\parallel CD$].",
            f"Angles $\\hat{{H}}_1$ and $x$ lie on straight line $CD$: $\\hat{{H}}_1 + x = 180^\\circ$.",
            f"$x = 180^\\circ - {theta}^\\circ = {ans}^\\circ$.",
        ],
    }


def arch_23_statement_reason_fill_transversal_angle(rng: random.Random) -> Dict[str, Any]:
    """Euclidean deduction: identify whether angle pair is corresp, alt, or co-int."""
    seed = rng.randint(1, 1_000_000)
    kind = rng.choice(["alternate", "corresponding", "cointerior"])
    if kind == "alternate":
        labels = {"G4": "50°", "H1": "50°"}
        ans = "alternate"
        rel_str = "\\hat{G}_4 = \\hat{H}_1"
    elif kind == "corresponding":
        labels = {"G2": "60°", "H2": "60°"}
        ans = "corresponding"
        rel_str = "\\hat{G}_2 = \\hat{H}_2"
    else:
        labels = {"G4": "110°", "H2": "70°"}
        ans = "cointerior"
        rel_str = "\\hat{G}_4 + \\hat{H}_2 = 180^\\circ"

    svg = draw_parallel_transversal_svg(labels, seed=seed)

    return {
        "subskill": "23_statement_reason_fill_transversal_angle",
        "question_text": (
            f"In the parallel line diagram below ($AB \\parallel CD$):\n"
            f"Consider the geometric relation: $${rel_str}$$\n\n"
            f"Identify whether this angle relationship is **alternate**, **corresponding**, or **cointerior**:"
        ),
        "correct_answer": ans,
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Correctly identify angle relationship as '{ans}'", "marks": 1},
        ],
        "hints": [
            "F-shape indicates corresponding angles, Z-shape indicates alternate angles, C/U-shape indicates co-interior angles.",
            f"Inspect the positions of the two highlighted angles.",
            f"The correct relationship is '{ans}'.",
        ],
    }


def arch_24_statement_reason_fill_transversal_statement(rng: random.Random) -> Dict[str, Any]:
    """Euclidean deduction: given reason [alt angles, AB || CD], find equal angle."""
    seed = rng.randint(1, 1_000_000)
    theta = rng.choice([44, 52, 63, 75])
    svg = draw_parallel_transversal_svg({"G3": f"{theta}°", "H2": "x"}, seed=seed)

    return {
        "subskill": "24_statement_reason_fill_transversal_statement",
        "question_text": (
            f"In the diagram below, $AB \\parallel CD$.\n\n"
            f"Given that $\\hat{{G}}_3 = {theta}^\\circ$ and $\\hat{{G}}_3 = x$ [alt $\\angle$s, $AB \\parallel CD$]:\n"
            f"State the value of angle $x$ in degrees:"
        ),
        "correct_answer": str(theta),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": f"Apply alternate interior angle equality: x = {theta}°", "marks": 1},
        ],
        "hints": [
            "Alternate angles are equal when lines are parallel.",
            f"$x = \\hat{{G}}_3 = {theta}^\\circ$.",
            f"The value is ${theta}$.",
        ],
    }


def arch_25_error_analysis_confusing_alternate_and_cointerior(rng: random.Random) -> Dict[str, Any]:
    """Error analysis: student set co-interior angles equal instead of supplementary."""
    seed = rng.randint(1, 1_000_000)
    # Correct: (2x + 10) + (3x + 20) = 180 => 5x + 30 = 180 => 5x = 150 => x = 30
    x_val = 30
    svg = draw_parallel_transversal_svg({"G4": "2x + 10°", "H2": "3x + 20°"}, seed=seed)

    return {
        "subskill": "25_error_analysis_confusing_alternate_and_cointerior",
        "question_text": (
            f"A learner was asked to find $x$ from the parallel lines ($AB \\parallel CD$) below.\n\n"
            f"**Learner's Working:**\n"
            f"Step 1: $2x + 10 = 3x + 20$ [alt $\\angle$s, $AB \\parallel CD$]\n"
            f"Step 2: $x = -10$\n\n"
            f"Explain the geometric misconception in Step 1, and determine the correct value of $x$:"
        ),
        "correct_answer": str(x_val),
        "tolerance": 0.0,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": [
            {"step": "Identify error: The angles are co-interior (supplementary), not alternate (equal)", "marks": 1},
            {"step": f"Correct equation: (2x + 10) + (3x + 20) = 180", "marks": 1},
            {"step": f"Accurate solution: x = {x_val}", "marks": 1},
        ],
        "hints": [
            "The two angles are on the same side of the transversal between the parallel lines, making them co-interior angles, not alternate angles.",
            "Co-interior angles sum to $180^\\circ$: $(2x + 10) + (3x + 20) = 180$.",
            f"$5x + 30 = 180 \\implies 5x = 150 \\implies x = {x_val}$.",
        ],
    }
