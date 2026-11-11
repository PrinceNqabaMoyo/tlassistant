"""Grade 9 Mathematics - Theorem of Pythagoras Archetypes 26 to 50.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 3/02. Pythagoras Theorem.md

Covers:
- Ladder problems: wall height, base distance, slipping ladder two-stage movement
- 2D Quadrilaterals: rectangle diagonal & breadth, square diagonal & area
- Rhombus side length and perimeter from perpendicular bisecting diagonals
- Isosceles and equilateral triangles: altitudes and areas
- Kite and trapezium side/height/area via Pythagoras
- Cartesian plane: distance between two points (integer, surd, decimal)
- Multi-step composite right triangles sharing common sides
- Spiral of Theodorus stages
- Real-world contexts: flagpoles/guy wires, ship displacement
- 3D space diagonals: rectangular prisms and cubes
- Error analysis: diagnosing geometric misconceptions
- Compound multi-step geometry synthesis

100% AST pure, zero LLM calls, zero network imports.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from .pythagoras_svg import (
    draw_composite_right_triangles_svg,
    draw_ladder_wall_svg,
    draw_right_triangle_svg,
)


# ----------------------------------------------------------------------
# 26. Ladder Against Wall: Calculate Height Up Wall
# ----------------------------------------------------------------------
def arch_26_ladder_against_wall_calculate_height(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (5.0, 3.0, 4.0),
        (13.0, 5.0, 12.0),
        (10.0, 6.0, 8.0),
        (15.0, 9.0, 12.0),
        (17.0, 8.0, 15.0),
        (25.0, 7.0, 24.0),
    ]
    ladder, ground, wall = rng.choice(configs)
    seed_val = rng.randint(1000, 999999)
    svg = draw_ladder_wall_svg(
        wall_height=wall,
        ground_dist=ground,
        ladder_len=ladder,
        unknown="wall",
        seed=seed_val,
    )

    prompt = (
        f"A ladder of length \\({ladder:g}\\text{{ m}}\\) leans against a vertical wall. "
        f"The foot of the ladder is placed on level ground \\({ground:g}\\text{{ m}}\\) away from the base of the wall. "
        f"Calculate the vertical height \\(h\\) that the ladder reaches up the wall."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"The vertical wall and horizontal ground meet at a \\(90^\\circ\\) right angle.\n"
        f"\\[ h^2 + ({ground:g})^2 = ({ladder:g})^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ h^2 = ({ladder:g})^2 - ({ground:g})^2 \\]\n"
        f"\\[ h^2 = {ladder**2:g} - {ground**2:g} = {wall**2:g} \\]\n"
        f"\\[ h = \\sqrt{{{wall**2:g}}} = {wall:g}\\text{{ m}} \\]"
    )
    return {
        "id": f"g9_pyth_ladder_ht_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{wall:g} m",
        "expected_answer": f"{wall:g} m",
        "sample_answer": f"h = {wall:g} m [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras: h² = L² - d²", "marks": 1},
            {"desc": f"Substitute: {ladder**2:g} - {ground**2:g} = {wall**2:g}", "marks": 1},
            {"desc": f"Calculate height h = {wall:g} m", "marks": 1},
        ],
        "hints": [
            "The ladder forms the hypotenuse of a right-angled triangle.",
            f"Subtract: h² = {ladder}² - {ground}².",
            f"h = √{wall*wall} = {wall:g} m.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 27. Ladder Against Wall: Calculate Base Distance
# ----------------------------------------------------------------------
def arch_27_ladder_against_wall_calculate_base_distance(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (5.0, 4.0, 3.0),
        (13.0, 12.0, 5.0),
        (10.0, 8.0, 6.0),
        (15.0, 12.0, 9.0),
        (17.0, 15.0, 8.0),
        (25.0, 24.0, 7.0),
    ]
    ladder, wall, ground = rng.choice(configs)
    seed_val = rng.randint(1000, 999999)
    svg = draw_ladder_wall_svg(
        wall_height=wall,
        ground_dist=ground,
        ladder_len=ladder,
        unknown="ground",
        seed=seed_val,
    )

    prompt = (
        f"A painter places a \\({ladder:g}\\text{{ m}}\\) ladder against a wall so that the top reaches a window "
        f"\\({wall:g}\\text{{ m}}\\) above the ground. "
        f"Assuming the wall is perpendicular to the ground, how far from the base of the wall is the foot of the ladder placed?"
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ d^2 + ({wall:g})^2 = ({ladder:g})^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ d^2 = ({ladder:g})^2 - ({wall:g})^2 \\]\n"
        f"\\[ d^2 = {ladder**2:g} - {wall**2:g} = {ground**2:g} \\]\n"
        f"\\[ d = \\sqrt{{{ground**2:g}}} = {ground:g}\\text{{ m}} \\]"
    )
    return {
        "id": f"g9_pyth_ladder_dist_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ground:g} m",
        "expected_answer": f"{ground:g} m",
        "sample_answer": f"d = {ground:g} m [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras subtraction: d² = L² - h²", "marks": 1},
            {"desc": f"Substitute: {ladder**2:g} - {wall**2:g} = {ground**2:g}", "marks": 1},
            {"desc": f"Calculate distance d = {ground:g} m", "marks": 1},
        ],
        "hints": [
            "Use Pythagoras with the ladder as the hypotenuse.",
            f"Subtract: d² = {ladder}² - {wall}² = {ground*ground}.",
            f"Take the square root: d = {ground:g} m.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 28. Ladder Slipping: Two-Stage Movement
# ----------------------------------------------------------------------
def arch_28_ladder_slipping_two_stage_movement(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (10, 8, 6, 2, 6, 8, 2),
        (13, 12, 5, 7, 5, 12, 7),
        (25, 24, 7, 9, 15, 20, 13),
        (25, 20, 15, 5, 15, 20, 5),
        (15, 12, 9, 3, 9, 12, 3),
    ]
    ladder, h1, d1, slip_down, h2, d2, slip_out = rng.choice(configs)

    prompt = (
        f"A \\({ladder}\\text{{ m}}\\) ladder rests against a vertical wall with its foot \\({d1}\\text{{ m}}\\) from the wall, "
        f"reaching a height of \\({h1}\\text{{ m}}\\) up the wall. "
        f"If the top of the ladder slips down by \\({slip_down}\\text{{ m}}\\), "
        f"calculate how far the bottom of the ladder will slide outward away from the wall."
    )
    sol = (
        f"**Step 1: Calculate the new vertical height of the ladder.**\n"
        f"\\[ h_2 = {h1} - {slip_down} = {h2}\\text{{ m}} \\]\n\n"
        f"**Step 2: Calculate the new distance from the wall.**\n"
        f"The length of the ladder remains constant at \\({ladder}\\text{{ m}}\\):\n"
        f"\\[ d_2^2 + h_2^2 = {ladder}^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ d_2^2 + ({h2})^2 = ({ladder})^2 \\]\n"
        f"\\[ d_2^2 = {ladder*ladder} - {h2*h2} = {d2*d2} \\]\n"
        f"\\[ d_2 = \\sqrt{{{d2*d2}}} = {d2}\\text{{ m}} \\]\n\n"
        f"**Step 3: Calculate the outward slip distance.**\n"
        f"\\[ \\text{{Outward slip}} = d_2 - d_1 = {d2} - {d1} = {slip_out}\\text{{ m}} \\]"
    )
    return {
        "id": f"g9_pyth_ladder_slip_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{slip_out} m",
        "expected_answer": f"{slip_out} m",
        "sample_answer": f"{slip_out} m (new distance = {d2} m, outward slide = {slip_out} m)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": f"Determine new vertical height: {h2} m", "marks": 1},
            {"desc": f"Apply Pythagoras to find new ground distance d₂ = {d2} m", "marks": 2},
            {"desc": f"Subtract to find outward slide: {d2} - {d1} = {slip_out} m", "marks": 1},
        ],
        "hints": [
            f"The new height of the ladder is {h1} - {slip_down} = {h2} m.",
            f"Find the new ground distance: d₂² = {ladder}² - {h2}².",
            f"Subtract the original distance {d1} m from {d2} m.",
        ],
    }


# ----------------------------------------------------------------------
# 29. Rectangle Diagonal Calculation
# ----------------------------------------------------------------------
def arch_29_rectangle_diagonal_calculation(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25)]
    w, l, d = rng.choice(triples)
    unit = rng.choice(["cm", "m"])
    if rng.random() > 0.5:
        w, l = l, w

    prompt = (
        f"A rectangle has length \\({l}\\text{{ {unit}}}\\) and breadth \\({w}\\text{{ {unit}}}\\). "
        f"Calculate the length of the diagonal of the rectangle."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"The adjacent sides of a rectangle meet at \\(90^\\circ\\). "
        f"The diagonal splits the rectangle into two right-angled triangles.\n"
        f"\\[ d^2 = l^2 + w^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ d^2 = ({l})^2 + ({w})^2 \\]\n"
        f"\\[ d^2 = {l*l} + {w*w} = {d*d} \\]\n"
        f"\\[ d = \\sqrt{{{d*d}}} = {d}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_rect_diag_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{d} {unit}",
        "expected_answer": f"{d} {unit}",
        "sample_answer": f"d = {d} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras to rectangle diagonal d² = l² + w²", "marks": 1},
            {"desc": f"Substitute: {l*l} + {w*w} = {d*d}", "marks": 1},
            {"desc": f"Calculate diagonal d = {d} {unit}", "marks": 1},
        ],
        "hints": [
            "The diagonal and two adjacent sides of a rectangle form a right triangle.",
            f"Add {l}² ({l*l}) and {w}² ({w*w}).",
            f"Take the square root: d = {d} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 30. Rectangle Breadth from Diagonal and Length
# ----------------------------------------------------------------------
def arch_30_rectangle_breadth_from_diagonal_and_length(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
    w, l, d = rng.choice(triples)
    unit = rng.choice(["cm", "m"])

    prompt = (
        f"The diagonal of a rectangle is \\({d}\\text{{ {unit}}}\\) and its length is \\({l}\\text{{ {unit}}}\\). "
        f"Calculate the breadth of the rectangle."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ d^2 = l^2 + w^2 \\quad [\\text{{Pythagoras in rectangle}}] \\]\n"
        f"\\[ w^2 = d^2 - l^2 \\]\n"
        f"\\[ w^2 = ({d})^2 - ({l})^2 \\]\n"
        f"\\[ w^2 = {d*d} - {l*l} = {w*w} \\]\n"
        f"\\[ w = \\sqrt{{{w*w}}} = {w}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_rect_breadth_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{w} {unit}",
        "expected_answer": f"{w} {unit}",
        "sample_answer": f"Breadth = {w} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras subtraction: w² = d² - l²", "marks": 1},
            {"desc": f"Substitute: {d*d} - {l*l} = {w*w}", "marks": 1},
            {"desc": f"Calculate breadth w = {w} {unit}", "marks": 1},
        ],
        "hints": [
            "Subtract the square of the length from the square of the diagonal.",
            f"w² = {d}² - {l}² = {d*d} - {l*l} = {w*w}.",
            f"w = √{w*w} = {w} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 31. Square Diagonal: Exact Surd and Decimal
# ----------------------------------------------------------------------
def arch_31_square_diagonal_exact_surd_and_decimal(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([4, 5, 6, 7, 8, 9, 10, 12])
    unit = rng.choice(["cm", "m"])
    sum_sq = 2 * s * s
    d_exact = math.sqrt(sum_sq)
    d_round = round(d_exact, 2)
    d_sa = f"{d_round:.2f}".replace(".", ",")

    prompt = (
        f"A square has side lengths of \\({s}\\text{{ {unit}}}\\). "
        f"Calculate the length of the diagonal of the square. "
        f"State your answer in exact surd form and as a decimal rounded to two decimal places."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"All four angles of a square are \\(90^\\circ\\).\n"
        f"\\[ d^2 = s^2 + s^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ d^2 = ({s})^2 + ({s})^2 = {s*s} + {s*s} = {sum_sq} \\]\n"
        f"\\[ d = \\sqrt{{{sum_sq}}} = {s}\\sqrt{{2}}\\text{{ {unit}}} \\approx {d_sa}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_sq_diag_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{s}√2 {unit} (or {d_sa} {unit})",
        "expected_answer": f"{d_sa} {unit}",
        "sample_answer": f"d = {s}√2 {unit} ≈ {d_sa} {unit}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Apply Pythagoras: d² = {s}² + {s}² = {sum_sq}", "marks": 1},
            {"desc": f"State surd form: {s}√2 {unit}", "marks": 1},
            {"desc": f"Evaluate decimal rounded to 2 places: {d_sa} {unit}", "marks": 1},
        ],
        "hints": [
            f"The diagonal of a square of side s is s√2.",
            f"Calculate d² = 2 × {s}² = {sum_sq}.",
            f"d = {s}√2 ≈ {d_sa} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 32. Square Side and Area from Diagonal
# ----------------------------------------------------------------------
def arch_32_square_side_and_area_from_diagonal(rng: random.Random) -> Dict[str, Any]:
    # d^2 = 2s^2 => Area = s^2 = d^2 / 2
    d = rng.choice([6, 8, 10, 12, 14, 16])
    unit = "cm"
    area = (d * d) // 2

    prompt = (
        f"The diagonal of a square is \\({d}\\text{{ {unit}}}\\). "
        f"Using Pythagoras' Theorem (\\(d^2 = s^2 + s^2\\)), calculate the exact area of the square."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"Let \\(s\\) be the side length of the square.\n"
        f"\\[ s^2 + s^2 = d^2 \\quad [\\text{{Pythagoras in square}}] \\]\n"
        f"\\[ 2s^2 = ({d})^2 \\]\n"
        f"\\[ 2s^2 = {d*d} \\]\n"
        f"\\[ s^2 = \\frac{{{d*d}}}{{2}} = {area}\\text{{ {unit}}}^2 \\]\n\n"
        f"Since the area of a square is \\(\\text{{Area}} = s^2\\):\n"
        f"\\[ \\text{{Area}} = {area}\\text{{ {unit}}}^2 \\]"
    )
    return {
        "id": f"g9_pyth_sq_area_diag_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{area} cm²",
        "expected_answer": f"{area} cm²",
        "sample_answer": f"Area = {area} cm²",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Set up Pythagoras: 2s² = {d}²", "marks": 1},
            {"desc": f"Evaluate 2s² = {d*d}", "marks": 1},
            {"desc": f"Solve Area = s² = {area} cm²", "marks": 1},
        ],
        "hints": [
            "In a square with diagonal d, d² = 2s².",
            f"The area of the square is s² = d² / 2.",
            f"Area = {d*d} / 2 = {area} cm².",
        ],
    }


# ----------------------------------------------------------------------
# 33. Rhombus Side Length from Diagonals
# ----------------------------------------------------------------------
def arch_33_rhombus_side_length_from_diagonals(rng: random.Random) -> Dict[str, Any]:
    # Diagonals bisect at 90 deg: half diagonals form right triangle
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)]
    h1, h2, side = rng.choice(triples)
    d1 = 2 * h1
    d2 = 2 * h2
    unit = "cm"

    prompt = (
        f"The diagonals of a rhombus have lengths of \\({d1}\\text{{ {unit}}}\\) and \\({d2}\\text{{ {unit}}}\\). "
        f"Recall that the diagonals of a rhombus bisect each other perpendicularly at \\(90^\\circ\\). "
        f"Calculate the side length of the rhombus."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"The diagonals bisect each other at right angles:\n"
        f"\\[ \\text{{Half diagonal 1}} = \\frac{{{d1}}}{{2}} = {h1}\\text{{ {unit}}} \\]\n"
        f"\\[ \\text{{Half diagonal 2}} = \\frac{{{d2}}}{{2}} = {h2}\\text{{ {unit}}} \\]\n\n"
        f"Each quarter triangle is a right-angled triangle where the side \\(s\\) is the hypotenuse:\n"
        f"\\[ s^2 = ({h1})^2 + ({h2})^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ s^2 = {h1*h1} + {h2*h2} = {side*side} \\]\n"
        f"\\[ s = \\sqrt{{{side*side}}} = {side}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_rhomb_side_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{side} {unit}",
        "expected_answer": f"{side} {unit}",
        "sample_answer": f"Side = {side} {unit} [diags bisect ⊥, Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Halve both diagonals: {h1} {unit} and {h2} {unit}", "marks": 1},
            {"desc": f"Apply Pythagoras: s² = {h1}² + {h2}² = {side*side}", "marks": 1},
            {"desc": f"Calculate side = {side} {unit}", "marks": 1},
        ],
        "hints": [
            f"Halve the diagonals: {d1}/2 = {h1} and {d2}/2 = {h2}.",
            "The side of the rhombus is the hypotenuse of the right triangle formed by the half-diagonals.",
            f"s = √({h1}² + {h2}²) = {side} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 34. Rhombus Perimeter from Diagonals
# ----------------------------------------------------------------------
def arch_34_rhombus_perimeter_from_diagonals(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25), (10, 24, 26)]
    h1, h2, side = rng.choice(triples)
    d1 = 2 * h1
    d2 = 2 * h2
    perim = 4 * side
    unit = "cm"

    prompt = (
        f"A rhombus has diagonals of lengths \\({d1}\\text{{ {unit}}}\\) and \\({d2}\\text{{ {unit}}}\\). "
        f"Calculate the **perimeter** of the rhombus."
    )
    sol = (
        f"**Step 1: Find the side length of the rhombus.**\n"
        f"Diagonals bisect at \\(90^\\circ\\):\n"
        f"\\[ s^2 = \\left(\\frac{{{d1}}}{{2}}\\right)^2 + \\left(\\frac{{{d2}}}{{2}}\\right)^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ s^2 = ({h1})^2 + ({h2})^2 = {h1*h1} + {h2*h2} = {side*side} \\]\n"
        f"\\[ s = {side}\\text{{ {unit}}} \\]\n\n"
        f"**Step 2: Calculate perimeter.**\n"
        f"All four sides of a rhombus are equal:\n"
        f"\\[ \\text{{Perimeter}} = 4 \\times s = 4 \\times {side}\\text{{ {unit}}} = {perim}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_rhomb_perim_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{perim} {unit}",
        "expected_answer": f"{perim} {unit}",
        "sample_answer": f"Perimeter = {perim} {unit}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Apply Pythagoras to find side = {side} {unit}", "marks": 2},
            {"desc": f"Multiply by 4 to find perimeter = {perim} {unit}", "marks": 1},
        ],
        "hints": [
            f"Find side length using half-diagonals {h1} and {h2}.",
            f"Side s = {side} {unit}.",
            f"Perimeter is 4 × {side} = {perim} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 35. Isosceles Triangle Altitude Calculation
# ----------------------------------------------------------------------
def arch_35_isosceles_triangle_altitude_calculation(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)]
    half_b, h, s = rng.choice(triples)
    base = 2 * half_b
    unit = "cm"

    prompt = (
        f"An isosceles triangle \\(\\triangle ABC\\) has equal sides \\(AB = AC = {s}\\text{{ {unit}}}\\) "
        f"and a base \\(BC = {base}\\text{{ {unit}}}\\). "
        f"An altitude \\(AD\\) is drawn perpendicular to \\(BC\\), bisecting the base at \\(D\\). "
        f"Calculate the length of altitude \\(AD\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"The altitude to the base of an isosceles triangle bisects the base:\n"
        f"\\[ BD = \\frac{{{base}}}{{2}} = {half_b}\\text{{ {unit}}} \\]\n\n"
        f"In right-angled \\(\\triangle ABD\\) (\\(\\hat{{D}} = 90^\\circ\\)):\n"
        f"\\[ AD^2 + BD^2 = AB^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ AD^2 = AB^2 - BD^2 \\]\n"
        f"\\[ AD^2 = ({s})^2 - ({half_b})^2 \\]\n"
        f"\\[ AD^2 = {s*s} - {half_b*half_b} = {h*h} \\]\n"
        f"\\[ AD = \\sqrt{{{h*h}}} = {h}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_iso_alt_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{h} {unit}",
        "expected_answer": f"{h} {unit}",
        "sample_answer": f"AD = {h} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Bisect base BC to get BD = {half_b} {unit}", "marks": 1},
            {"desc": f"Apply Pythagoras AD² = {s}² - {half_b}² = {h*h}", "marks": 1},
            {"desc": f"Calculate altitude AD = {h} {unit}", "marks": 1},
        ],
        "hints": [
            f"The altitude divides the base into two equal halves of {half_b} {unit} each.",
            f"Apply Pythagoras: AD² = {s}² - {half_b}².",
            f"AD = √{h*h} = {h} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 36. Isosceles Triangle Area Calculation via Pythagoras
# ----------------------------------------------------------------------
def arch_36_isosceles_triangle_area_calculation_via_pythagoras(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25)]
    half_b, h, s = rng.choice(triples)
    base = 2 * half_b
    unit = "cm"
    area = (base * h) // 2

    prompt = (
        f"An isosceles triangle has two equal sides of length \\({s}\\text{{ {unit}}}\\) each, "
        f"and a base of \\({base}\\text{{ {unit}}}\\).\n\n"
        f"1. Calculate the perpendicular height (altitude) of the triangle.\n"
        f"2. Hence, calculate the area of the isosceles triangle."
    )
    sol = (
        f"**Step 1: Calculate perpendicular height using Pythagoras.**\n"
        f"Half base \\(BD = {base} \\div 2 = {half_b}\\text{{ {unit}}}\\).\n"
        f"\\[ h^2 = ({s})^2 - ({half_b})^2 = {s*s} - {half_b*half_b} = {h*h} \\]\n"
        f"\\[ h = {h}\\text{{ {unit}}} \\]\n\n"
        f"**Step 2: Calculate the area of the triangle.**\n"
        f"\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} \\]\n"
        f"\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times {base} \\times {h} = {area}\\text{{ {unit}}}^2 \\]"
    )
    return {
        "id": f"g9_pyth_iso_area_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{area} cm²",
        "expected_answer": f"{area} cm²",
        "sample_answer": f"Height = {h} {unit}, Area = {area} cm²",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": f"Find half-base = {half_b} {unit}", "marks": 1},
            {"desc": f"Apply Pythagoras to find height h = {h} {unit}", "marks": 1},
            {"desc": "Apply area formula 1/2 × base × height", "marks": 1},
            {"desc": f"Calculate Area = {area} cm²", "marks": 1},
        ],
        "hints": [
            f"The altitude cuts the base {base} cm into two segments of {half_b} cm.",
            f"Height h = √({s}² - {half_b}²) = {h} cm.",
            f"Area = 1/2 × {base} × {h} = {area} cm².",
        ],
    }


# ----------------------------------------------------------------------
# 37. Equilateral Triangle Altitude and Area
# ----------------------------------------------------------------------
def arch_37_equilateral_triangle_altitude_and_area(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([4, 6, 8, 10, 12])
    unit = "cm"
    half_s = s // 2
    h_sq = s * s - half_s * half_s
    h_exact = math.sqrt(h_sq)
    h_round = round(h_exact, 2)
    h_sa = f"{h_round:.2f}".replace(".", ",")
    area_exact = 0.5 * s * h_exact
    area_round = round(area_exact, 2)
    area_sa = f"{area_round:.2f}".replace(".", ",")

    prompt = (
        f"An equilateral triangle has sides of length \\({s}\\text{{ {unit}}}\\). "
        f"An altitude is dropped from a vertex to the opposite side, bisecting it into two equal segments of \\({half_s}\\text{{ {unit}}}\\).\n\n"
        f"Calculate the altitude \\(h\\) of the triangle, rounded to two decimal places."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"In the right-angled half-triangle:\n"
        f"\\[ h^2 + ({half_s})^2 = ({s})^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ h^2 = {s*s} - {half_s*half_s} = {h_sq} \\]\n"
        f"\\[ h = \\sqrt{{{h_sq}}} = {half_s}\\sqrt{{3}} \\approx {h_sa}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_equilat_alt_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{h_sa} {unit}",
        "expected_answer": f"{h_sa} {unit}",
        "sample_answer": f"h = {half_s}√3 ≈ {h_sa} {unit}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Apply Pythagoras: h² = {s}² - {half_s}² = {h_sq}", "marks": 1},
            {"desc": f"State exact surd: {half_s}√3 {unit}", "marks": 1},
            {"desc": f"Evaluate rounded decimal: {h_sa} {unit}", "marks": 1},
        ],
        "hints": [
            f"The half-base is {half_s} cm.",
            f"h² = {s}² - {half_s}² = {s*s} - {half_s*half_s} = {h_sq}.",
            f"h = √{h_sq} ≈ {h_sa} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 38. Kite Side Length from Perpendicular Diagonals
# ----------------------------------------------------------------------
def arch_38_kite_side_length_from_perpendicular_diagonals(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (3, 4, 5, 8, 15, 17),
        (6, 8, 10, 8, 15, 17),
        (5, 12, 13, 12, 16, 20),
        (8, 15, 17, 15, 20, 25),
        (7, 24, 25, 24, 32, 40),
        (9, 12, 15, 12, 35, 37),
    ]
    x, y1, s1, x2, y2, s2 = rng.choice(configs)
    unit = "cm"

    prompt = (
        f"In kite \\(ABCD\\), diagonals \\(AC\\) and \\(BD\\) intersect perpendicularly at point \\(M\\) (\\(\\hat{{M}} = 90^\\circ\\)). "
        f"The diagonal of symmetry \\(AC\\) bisects diagonal \\(BD\\), so \\(BM = MD = {x}\\text{{ {unit}}}\\). "
        f"The segments of the main diagonal are \\(AM = {y1}\\text{{ {unit}}}\\) and \\(MC = {y2}\\text{{ {unit}}}\\).\n\n"
        f"Calculate the length of the shorter side \\(AB\\) of the kite."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"The diagonals of a kite intersect perpendicularly at \\(90^\\circ\\).\n"
        f"In right-angled \\(\\triangle AMB\\):\n"
        f"\\[ AB^2 = AM^2 + BM^2 \\quad [\\text{{Pythagoras, }}\\hat{{M}} = 90^\\circ] \\]\n"
        f"\\[ AB^2 = ({y1})^2 + ({x})^2 = {y1*y1} + {x*x} = {s1*s1} \\]\n"
        f"\\[ AB = \\sqrt{{{s1*s1}}} = {s1}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_kite_side_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{s1} {unit}",
        "expected_answer": f"{s1} {unit}",
        "sample_answer": f"AB = {s1} {unit} [Pythagoras in △AMB]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Identify △AMB as a right-angled triangle (diags of kite ⊥)", "marks": 1},
            {"desc": f"Apply Pythagoras: AB² = {y1}² + {x}² = {s1*s1}", "marks": 1},
            {"desc": f"Calculate AB = {s1} {unit}", "marks": 1},
        ],
        "hints": [
            "The diagonals of a kite cross at right angles.",
            f"Use △AMB: AB² = AM² + BM² = {y1}² + {x}².",
            f"AB = √{s1*s1} = {s1} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 39. Trapezium Unknown Slanted Side via Altitude
# ----------------------------------------------------------------------
def arch_39_trapezium_unknown_slanted_side_via_altitude(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
    dx, h, slant = rng.choice(triples)
    top_base = rng.choice([6, 8, 10])
    bot_base = top_base + dx
    unit = "cm"

    prompt = (
        f"Right-angled trapezium \\(ABCD\\) has parallel sides \\(AB \\parallel DC\\). "
        f"Side \\(AD\\) is perpendicular to both parallel sides (\\(\\hat{{A}} = \\hat{{D}} = 90^\\circ\\)). "
        f"Given \\(AB = {top_base}\\text{{ {unit}}}\\), \\(DC = {bot_base}\\text{{ {unit}}}\\), "
        f"and perpendicular height \\(AD = {h}\\text{{ {unit}}}\\), "
        f"calculate the length of the slanted side \\(BC\\)."
    )
    sol = (
        f"**Step 1: Construct perpendicular height from B to DC.**\n"
        f"Drop a perpendicular \\(BE \\perp DC\\). Then \\(ABED\\) is a rectangle, so \\(DE = AB = {top_base}\\text{{ {unit}}}\\) "
        f"and \\(BE = AD = {h}\\text{{ {unit}}}\\).\n\n"
        f"**Step 2: Find base EC of the right-angled triangle.**\n"
        f"\\[ EC = DC - DE = {bot_base} - {top_base} = {dx}\\text{{ {unit}}} \\]\n\n"
        f"**Step 3: Apply Pythagoras in \\(\\triangle BEC\\).**\n"
        f"\\[ BC^2 = BE^2 + EC^2 \\quad [\\text{{Pythagoras, }}\\hat{{E}} = 90^\\circ] \\]\n"
        f"\\[ BC^2 = ({h})^2 + ({dx})^2 = {h*h} + {dx*dx} = {slant*slant} \\]\n"
        f"\\[ BC = \\sqrt{{{slant*slant}}} = {slant}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_trap_slant_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{slant} {unit}",
        "expected_answer": f"{slant} {unit}",
        "sample_answer": f"BC = {slant} {unit} [Pythagoras in △BEC]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Find base of right triangle: EC = {bot_base} - {top_base} = {dx} {unit}", "marks": 1},
            {"desc": f"Apply Pythagoras: BC² = {h}² + {dx}² = {slant*slant}", "marks": 1},
            {"desc": f"Calculate slanted side BC = {slant} {unit}", "marks": 1},
        ],
        "hints": [
            f"The horizontal difference between the parallel sides is {bot_base} - {top_base} = {dx} cm.",
            f"The vertical height is {h} cm.",
            f"Use Pythagoras: BC² = {h}² + {dx}² = {slant*slant}, so BC = {slant} cm.",
        ],
    }


# ----------------------------------------------------------------------
# 40. Trapezium Area via Pythagoras Height
# ----------------------------------------------------------------------
def arch_40_trapezium_area_via_pythagoras_height(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
    dx, h, slant = rng.choice(triples)
    top_base = rng.choice([7, 9, 11])
    bot_base = top_base + dx
    unit = "cm"
    area = (top_base + bot_base) * h // 2

    prompt = (
        f"In right-angled trapezium \\(ABCD\\), \\(AB \\parallel DC\\) and \\(\\hat{{A}} = \\hat{{D}} = 90^\\circ\\). "
        f"The parallel sides are \\(AB = {top_base}\\text{{ {unit}}}\\) and \\(DC = {bot_base}\\text{{ {unit}}}\\). "
        f"The slanted side is \\(BC = {slant}\\text{{ {unit}}}\\).\n\n"
        f"1. Use Pythagoras' Theorem to calculate the perpendicular height \\(AD\\).\n"
        f"2. Hence, calculate the area of the trapezium."
    )
    sol = (
        f"**Step 1: Calculate the perpendicular height AD.**\n"
        f"Let \\(BE \\perp DC\\). Then \\(EC = {bot_base} - {top_base} = {dx}\\text{{ {unit}}}\\).\n"
        f"\\[ AD^2 = BC^2 - EC^2 \\quad [\\text{{Pythagoras in }}\\triangle BEC] \\]\n"
        f"\\[ AD^2 = ({slant})^2 - ({dx})^2 = {slant*slant} - {dx*dx} = {h*h} \\]\n"
        f"\\[ AD = {h}\\text{{ {unit}}} \\]\n\n"
        f"**Step 2: Calculate the area of the trapezium.**\n"
        f"\\[ \\text{{Area}} = \\frac{{1}}{{2}} (a + b) \\times h \\]\n"
        f"\\[ \\text{{Area}} = \\frac{{1}}{{2}} ({top_base} + {bot_base}) \\times {h} \\]\n"
        f"\\[ \\text{{Area}} = \\frac{{1}}{{2}} ({top_base + bot_base}) \\times {h} = {area}\\text{{ {unit}}}^2 \\]"
    )
    return {
        "id": f"g9_pyth_trap_area_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{area} cm²",
        "expected_answer": f"{area} cm²",
        "sample_answer": f"Height = {h} {unit}, Area = {area} cm²",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": f"Calculate EC = {dx} {unit}", "marks": 1},
            {"desc": f"Apply Pythagoras to find height = {h} {unit}", "marks": 1},
            {"desc": "Apply trapezium area formula 1/2(a + b)h", "marks": 1},
            {"desc": f"Calculate Area = {area} cm²", "marks": 1},
        ],
        "hints": [
            f"The horizontal base of the right triangle is {bot_base} - {top_base} = {dx} cm.",
            f"Height h = √({slant}² - {dx}²) = {h} cm.",
            f"Area = 1/2({top_base} + {bot_base}) × {h} = {area} cm².",
        ],
    }


# ----------------------------------------------------------------------
# 41. Distance Between Two Points Cartesian Plane: Integer
# ----------------------------------------------------------------------
def arch_41_distance_between_two_points_cartesian_plane_integer(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
    dx, dy, dist = rng.choice(triples)
    x1 = rng.randint(1, 5)
    y1 = rng.randint(1, 5)
    x2 = x1 + dx
    y2 = y1 + dy

    prompt = (
        f"Calculate the distance between points \\(A({x1}; {y1})\\) and \\(B({x2}; {y2})\\) "
        f"on the Cartesian coordinate plane using Pythagoras' Theorem."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"By constructing horizontal and vertical line segments between \\(A\\) and \\(B\\):\n"
        f"\\[ \\Delta x = x_2 - x_1 = {x2} - {x1} = {dx} \\]\n"
        f"\\[ \\Delta y = y_2 - y_1 = {y2} - {y1} = {dy} \\]\n\n"
        f"By the Theorem of Pythagoras:\n"
        f"\\[ AB^2 = (\\Delta x)^2 + (\\Delta y)^2 \\]\n"
        f"\\[ AB^2 = ({dx})^2 + ({dy})^2 = {dx*dx} + {dy*dy} = {dist*dist} \\]\n"
        f"\\[ AB = \\sqrt{{{dist*dist}}} = {dist}\\text{{ units}} \\]"
    )
    return {
        "id": f"g9_pyth_dist_int_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{dist} units",
        "expected_answer": f"{dist} units",
        "sample_answer": f"AB = {dist} units [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate Δx = {dx} and Δy = {dy}", "marks": 1},
            {"desc": f"Apply Pythagoras AB² = {dx}² + {dy}² = {dist*dist}", "marks": 1},
            {"desc": f"Solve distance AB = {dist} units", "marks": 1},
        ],
        "hints": [
            f"Find horizontal change: {x2} - {x1} = {dx}.",
            f"Find vertical change: {y2} - {y1} = {dy}.",
            f"Distance = √({dx}² + {dy}²) = {dist} units.",
        ],
    }


# ----------------------------------------------------------------------
# 42. Distance Between Two Points Cartesian Plane: Surd / Decimal
# ----------------------------------------------------------------------
def arch_42_distance_between_two_points_cartesian_plane_surd_decimal(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (2, 4, 20), (3, 5, 34), (4, 6, 52), (1, 6, 37), (2, 7, 53)
    ]
    dx, dy, sum_sq = rng.choice(configs)
    x1 = rng.randint(0, 4)
    y1 = rng.randint(0, 4)
    x2 = x1 + dx
    y2 = y1 + dy
    d_exact = math.sqrt(sum_sq)
    d_round = round(d_exact, 2)
    d_sa = f"{d_round:.2f}".replace(".", ",")

    prompt = (
        f"Points \\(P({x1}; {y1})\\) and \\(Q({x2}; {y2})\\) are plotted on a Cartesian plane. "
        f"Calculate the distance \\(PQ\\), giving your answer in **simplest surd form** and rounded to **two decimal places**."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ \\Delta x = {x2} - {x1} = {dx} \\]\n"
        f"\\[ \\Delta y = {y2} - {y1} = {dy} \\]\n\n"
        f"By Pythagoras' Theorem:\n"
        f"\\[ PQ^2 = (\\Delta x)^2 + (\\Delta y)^2 = ({dx})^2 + ({dy})^2 = {dx*dx} + {dy*dy} = {sum_sq} \\]\n"
        f"\\[ PQ = \\sqrt{{{sum_sq}}} \\approx {d_sa}\\text{{ units}} \\]"
    )
    return {
        "id": f"g9_pyth_dist_surd_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"√{sum_sq} units (or {d_sa} units)",
        "expected_answer": f"{d_sa} units",
        "sample_answer": f"PQ = √{sum_sq} units ≈ {d_sa} units",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate Δx = {dx}, Δy = {dy}, and sum of squares = {sum_sq}", "marks": 1},
            {"desc": f"State exact surd: √{sum_sq} units", "marks": 1},
            {"desc": f"Evaluate rounded decimal: {d_sa} units", "marks": 1},
        ],
        "hints": [
            f"Δx = {dx}, Δy = {dy}.",
            f"Distance² = {dx}² + {dy}² = {sum_sq}.",
            f"PQ = √{sum_sq} ≈ {d_sa} units.",
        ],
    }


# ----------------------------------------------------------------------
# 43. Two Connected Right Triangles Shared Hypotenuse / Leg
# ----------------------------------------------------------------------
def arch_43_two_connected_right_triangles_shared_hypotenuse(rng: random.Random) -> Dict[str, Any]:
    # Triangle 1: legs 3, 4 -> hyp 5
    # Triangle 2: leg 5, leg 12 -> hyp 13
    triples_pair = [
        ((3, 4, 5), 12, 13),
        ((6, 8, 10), 24, 26),
        ((8, 15, 17), 17, round(math.sqrt(17*17 + 17*17))),  # surd case
    ]
    (a1, b1, c1), leg2, hyp2 = triples_pair[0] if rng.random() > 0.4 else triples_pair[1]
    unit = "cm"

    seed_val = rng.randint(1000, 999999)
    svg = draw_composite_right_triangles_svg(t1_legs=(a1, b1), t2_leg=leg2, seed=seed_val)

    prompt = (
        f"In the composite geometric figure shown below, \\(\\triangle ABC\\) has \\(\\hat{{B}} = 90^\\circ\\), "
        f"\\(AB = {b1}\\text{{ {unit}}}\\), and \\(BC = {a1}\\text{{ {unit}}}\\). "
        f"A second right-angled triangle \\(\\triangle ACD\\) has \\(\\hat{{C}} = 90^\\circ\\) "
        f"and side \\(CD = {leg2}\\text{{ {unit}}}\\).\n\n"
        f"Calculate the length of side \\(AD\\)."
    )
    sol = (
        f"**Step 1: Calculate the shared side AC in \\(\\triangle ABC\\).**\n"
        f"\\[ AC^2 = AB^2 + BC^2 \\quad [\\text{{Pythagoras, }}\\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ AC^2 = ({b1})^2 + ({a1})^2 = {b1*b1} + {a1*a1} = {c1*c1} \\]\n"
        f"\\[ AC = {c1}\\text{{ {unit}}} \\]\n\n"
        f"**Step 2: Calculate hypotenuse AD in \\(\\triangle ACD\\).**\n"
        f"\\[ AD^2 = AC^2 + CD^2 \\quad [\\text{{Pythagoras, }}\\hat{{C}} = 90^\\circ] \\]\n"
        f"\\[ AD^2 = {c1*c1} + ({leg2})^2 = {c1*c1} + {leg2*leg2} = {hyp2*hyp2} \\]\n"
        f"\\[ AD = \\sqrt{{{hyp2*hyp2}}} = {hyp2}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_comp_two_tri_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{hyp2} {unit}",
        "expected_answer": f"{hyp2} {unit}",
        "sample_answer": f"AC = {c1} {unit}, AD = {hyp2} {unit}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": f"Apply Pythagoras in △ABC to find AC = {c1} {unit}", "marks": 2},
            {"desc": f"Apply Pythagoras in △ACD to find AD² = {hyp2*hyp2}", "marks": 1},
            {"desc": f"Calculate AD = {hyp2} {unit}", "marks": 1},
        ],
        "hints": [
            f"First find the shared side AC in the first triangle: AC² = {b1}² + {a1}².",
            f"Then use AC = {c1} cm to find AD in the second triangle.",
            f"AD = √({c1}² + {leg2}²) = {hyp2} {unit}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 44. Stepped Spiral of Theodorus: Two Stages
# ----------------------------------------------------------------------
def arch_44_stepped_spiral_of_theodorus_two_stages(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (1, 1, 2, "√2", 1, 3, "√3"),
        (2, 2, 8, "√8", 2, 12, "√12"),
        (1, 1, 2, "√2", 2, 6, "√6"),
        (3, 3, 18, "√18", 3, 27, "√27"),
        (2, 2, 8, "√8", 1, 9, "3"),
        (1, 2, 5, "√5", 2, 9, "3"),
    ]
    u1, u2, sq1, s1_str, u3, sq2, s2_str = rng.choice(configs)

    prompt = (
        f"In the Spiral of Theodorus, right triangles are constructed sequentially:\n"
        f"1. Triangle 1 is an isosceles right triangle with legs of \\({u1}\\text{{ cm}}\\) each and hypotenuse \\(h_1\\).\n"
        f"2. Triangle 2 has base \\(h_1\\), perpendicular leg of \\({u3}\\text{{ cm}}\\), and hypotenuse \\(h_2\\).\n\n"
        f"Calculate the exact length of hypotenuse \\(h_2\\) in surd form."
    )
    sol = (
        f"**Step 1: Calculate \\(h_1\\).**\n"
        f"\\[ h_1^2 = {u1}^2 + {u2}^2 = {u1*u1} + {u2*u2} = {sq1} \\]\n"
        f"\\[ h_1 = \\sqrt{{{sq1}}}\\text{{ cm}} \\]\n\n"
        f"**Step 2: Calculate \\(h_2\\).**\n"
        f"\\[ h_2^2 = (h_1)^2 + ({u3})^2 \\]\n"
        f"\\[ h_2^2 = {sq1} + {u3*u3} = {sq2} \\]\n"
        f"\\[ h_2 = \\sqrt{{{sq2}}}\\text{{ cm}} \\]"
    )
    return {
        "id": f"g9_pyth_theodorus_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"√{sq2} cm",
        "expected_answer": f"√{sq2} cm",
        "sample_answer": f"h₂ = √{sq2} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate h₁² = {sq1}", "marks": 1},
            {"desc": f"Calculate h₂² = {sq1} + {u3*u3} = {sq2}", "marks": 1},
            {"desc": f"State exact surd: h₂ = √{sq2} cm", "marks": 1},
        ],
        "hints": [
            f"First find h₁² = {u1}² + {u2}² = {sq1}.",
            f"Then h₂² = (h₁)² + {u3}² = {sq1} + {u3*u3} = {sq2}.",
            f"h₂ = √{sq2} cm.",
        ],
    }


# ----------------------------------------------------------------------
# 45. Flagpole and Guy Wire Length
# ----------------------------------------------------------------------
def arch_45_flagpole_and_guy_wire_length(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)]
    dist, height, wire = rng.choice(triples)

    prompt = (
        f"A vertical flagpole is \\({height}\\text{{ m}}\\) tall. "
        f"A straight guy wire is fastened from the very top of the flagpole to an anchor peg "
        f"driven into the level ground \\({dist}\\text{{ m}}\\) from the base of the pole. "
        f"Calculate the length of the guy wire."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"The flagpole meets the level ground at \\(90^\\circ\\).\n"
        f"\\[ \\text{{Wire}}^2 = \\text{{Height}}^2 + \\text{{Distance}}^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ \\text{{Wire}}^2 = ({height})^2 + ({dist})^2 \\]\n"
        f"\\[ \\text{{Wire}}^2 = {height*height} + {dist*dist} = {wire*wire} \\]\n"
        f"\\[ \\text{{Wire}} = \\sqrt{{{wire*wire}}} = {wire}\\text{{ m}} \\]"
    )
    return {
        "id": f"g9_pyth_guy_wire_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{wire} m",
        "expected_answer": f"{wire} m",
        "sample_answer": f"Wire length = {wire} m [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras formula W² = H² + D²", "marks": 1},
            {"desc": f"Substitute: {height*height} + {dist*dist} = {wire*wire}", "marks": 1},
            {"desc": f"Calculate wire length = {wire} m", "marks": 1},
        ],
        "hints": [
            "The flagpole, ground, and wire form a right-angled triangle.",
            f"Add {height}² = {height*height} and {dist}² = {dist*dist}.",
            f"Square root of {wire*wire} is {wire} m.",
        ],
    }


# ----------------------------------------------------------------------
# 46. Ship Navigation: North-East Displacement
# ----------------------------------------------------------------------
def arch_46_ship_navigation_north_east_displacement(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (7, 24, 25)]
    east, north, direct = rng.choice(triples)
    scale = rng.choice([1, 10])
    east *= scale
    north *= scale
    direct *= scale

    prompt = (
        f"A cargo ship leaves Cape Town harbour and sails due North for \\({north}\\text{{ km}}\\), "
        f"then turns due East and sails for \\({east}\\text{{ km}}\\). "
        f"Calculate the direct straight-line distance of the ship from the harbour."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"North and East compass directions are perpendicular (\\(90^\\circ\\)).\n"
        f"\\[ d^2 = (\\text{{North}})^2 + (\\text{{East}})^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ d^2 = ({north})^2 + ({east})^2 \\]\n"
        f"\\[ d^2 = {north*north} + {east*east} = {direct*direct} \\]\n"
        f"\\[ d = \\sqrt{{{direct*direct}}} = {direct}\\text{{ km}} \\]"
    )
    return {
        "id": f"g9_pyth_ship_disp_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{direct} km",
        "expected_answer": f"{direct} km",
        "sample_answer": f"Distance = {direct} km [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Recognize North and East meet at 90°", "marks": 1},
            {"desc": f"Apply Pythagoras: {north*north} + {east*east} = {direct*direct}", "marks": 1},
            {"desc": f"Calculate direct distance = {direct} km", "marks": 1},
        ],
        "hints": [
            "North and East form a 90° right angle.",
            f"Calculate {north}² + {east}².",
            f"The direct distance is √{direct*direct} = {direct} km.",
        ],
    }


# ----------------------------------------------------------------------
# 47. Space Diagonal of Rectangular Prism Box
# ----------------------------------------------------------------------
def arch_47_space_diagonal_of_rectangular_prism_box(rng: random.Random) -> Dict[str, Any]:
    # d^2 = l^2 + w^2 + h^2
    # e.g. (2, 3, 6) -> 4 + 9 + 36 = 49 -> 7
    # (1, 4, 8) -> 1 + 16 + 64 = 81 -> 9
    # (2, 6, 9) -> 4 + 36 + 81 = 121 -> 11
    # (3, 4, 12) -> 9 + 16 + 144 = 169 -> 13
    # (4, 12, 3) -> 13
    configs = [
        (2, 3, 6, 7),
        (1, 4, 8, 9),
        (2, 6, 9, 11),
        (3, 4, 12, 13),
        (4, 7, 4, 9),
        (6, 6, 7, 11),
    ]
    l, w, h, diag = rng.choice(configs)
    unit = "cm"

    prompt = (
        f"A rectangular prism (box) has dimensions: length \\(l = {l}\\text{{ {unit}}}\\), "
        f"width \\(w = {w}\\text{{ {unit}}}\\), and height \\(h = {h}\\text{{ {unit}}}\\).\n\n"
        f"Using the 3D Theorem of Pythagoras (\\(d^2 = l^2 + w^2 + h^2\\)), "
        f"calculate the length of the internal **space diagonal** connecting two opposite corners."
    )
    sol = (
        f"**Step 1: Calculate the face diagonal on the base.**\n"
        f"\\[ d_{{\\text{{base}}}}^2 = l^2 + w^2 = {l}^2 + {w}^2 = {l*l} + {w*w} = {l*l + w*w} \\]\n\n"
        f"**Step 2: Calculate the 3D space diagonal.**\n"
        f"\\[ d^2 = d_{{\\text{{base}}}}^2 + h^2 \\quad [\\text{{Pythagoras in 3D}}] \\]\n"
        f"\\[ d^2 = ({l*l + w*w}) + ({h})^2 = {l*l + w*w} + {h*h} = {diag*diag} \\]\n"
        f"\\[ d = \\sqrt{{{diag*diag}}} = {diag}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_space_diag_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{diag} {unit}",
        "expected_answer": f"{diag} {unit}",
        "sample_answer": f"d = {diag} {unit} [d² = l² + w² + h²]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply 3D Pythagoras formula d² = l² + w² + h²", "marks": 1},
            {"desc": f"Substitute: {l*l} + {w*w} + {h*h} = {diag*diag}", "marks": 1},
            {"desc": f"Calculate space diagonal d = {diag} {unit}", "marks": 1},
        ],
        "hints": [
            "In 3D, the space diagonal formula is d² = l² + w² + h².",
            f"Calculate {l}² ({l*l}) + {w}² ({w*w}) + {h}² ({h*h}) = {diag*diag}.",
            f"Take the square root: d = {diag} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 48. Cube Space Diagonal: Exact and Rounded
# ----------------------------------------------------------------------
def arch_48_cube_space_diagonal_exact_and_rounded(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([3, 4, 5, 6, 7, 8, 10])
    unit = "cm"
    sum_sq = 3 * s * s
    d_exact = math.sqrt(sum_sq)
    d_round = round(d_exact, 2)
    d_sa = f"{d_round:.2f}".replace(".", ",")

    prompt = (
        f"A cube has edge lengths of \\({s}\\text{{ {unit}}}\\). "
        f"Calculate the length of the space diagonal connecting opposite corners of the cube. "
        f"Express your answer in exact surd form and rounded to two decimal places."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"For a cube of side \\(s\\), \\(l = w = h = s\\).\n"
        f"\\[ d^2 = s^2 + s^2 + s^2 = 3s^2 \\quad [\\text{{Pythagoras in 3D}}] \\]\n"
        f"\\[ d^2 = 3({s})^2 = 3({s*s}) = {sum_sq} \\]\n"
        f"\\[ d = \\sqrt{{{sum_sq}}} = {s}\\sqrt{{3}}\\text{{ {unit}}} \\approx {d_sa}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_cube_diag_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{s}√3 {unit} (or {d_sa} {unit})",
        "expected_answer": f"{d_sa} {unit}",
        "sample_answer": f"d = {s}√3 {unit} ≈ {d_sa} {unit}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Apply 3D Pythagoras for cube: d² = 3s² = {sum_sq}", "marks": 1},
            {"desc": f"State surd form: {s}√3 {unit}", "marks": 1},
            {"desc": f"Evaluate rounded decimal: {d_sa} {unit}", "marks": 1},
        ],
        "hints": [
            f"The space diagonal of a cube with edge s is s√3.",
            f"d² = 3 × {s}² = {sum_sq}.",
            f"d = {s}√3 ≈ {d_sa} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 49. Error Analysis: Diagnose Pythagoras Misconception
# ----------------------------------------------------------------------
def arch_49_error_analysis_diagnose_pythagoras_misconception(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(["Thabo", "Sipho", "Zola", "Buhle", "Lerato", "Kagiso", "Nomsa", "Andile"])
    scenarios = [
        (
            f"{name} attempted to calculate the hypotenuse \\(c\\) of a right triangle with legs "
            f"\\(3\\text{{ cm}}\\) and \\(4\\text{{ cm}}\\) by writing:\n"
            f"\\[ c = 3 + 4 = 7\\text{{ cm}} \\]\n"
            f"Identify {name}'s misconception and write down the correct calculation.",
            f"**Misconception Analysis:**\n"
            f"{name} added the side lengths directly without squaring them first.\n"
            f"Pythagoras' Theorem states that the square on the hypotenuse is equal to the sum of the squares of the other two sides:\n"
            f"\\[ c^2 = a^2 + b^2 = 3^2 + 4^2 = 9 + 16 = 25 \\]\n"
            f"\\[ c = \\sqrt{{25}} = 5\\text{{ cm}} \\]\n"
            f"Side lengths cannot be added directly (triangle inequality: \\(c < a + b\\)).",
            "Must square side lengths first (c² = a² + b²); c = √(3² + 4²) = 5 cm, not 7 cm.",
            "Sides must be squared before adding: c = 5 cm.",
            [
                {"desc": "Identify that sides cannot be added linearly without squaring", "marks": 1},
                {"desc": "Provide correct calculation yielding c = 5 cm", "marks": 1},
            ],
            [
                "Does a² + b² = c² mean a + b = c?",
                "Square both numbers first, then add and take the square root.",
                "Correct answer is 5 cm.",
            ],
        ),
        (
            f"{name} was given a right triangle with hypotenuse \\(13\\text{{ cm}}\\) and one leg \\(5\\text{{ cm}}\\). "
            f"{name} solved for the unknown leg \\(b\\) by writing:\n"
            f"\\[ b^2 = 13^2 + 5^2 = 169 + 25 = 194 \\implies b = \\sqrt{{194}} \\approx 13{{,}}93\\text{{ cm}} \\]\n"
            f"Explain why {name}'s answer is impossible, and provide the correct calculation.",
            f"**Misconception Analysis:**\n"
            f"{name} added the squares instead of subtracting.\n"
            f"The hypotenuse is always the longest side of a right triangle; a leg cannot be \\(13{{,}}93\\text{{ cm}}\\) "
            f"when the hypotenuse is only \\(13\\text{{ cm}}\\).\n\n"
            f"**Correct Calculation:**\n"
            f"\\[ b^2 = c^2 - a^2 = 13^2 - 5^2 = 169 - 25 = 144 \\]\n"
            f"\\[ b = \\sqrt{{144}} = 12\\text{{ cm}} \\]",
            "Must subtract when finding a shorter side (b² = c² - a²); b = √(169 - 25) = 12 cm.",
            "Added squares instead of subtracting; leg cannot exceed hypotenuse. b = 12 cm.",
            [
                {"desc": "Identify that squares must be subtracted to find a leg", "marks": 1},
                {"desc": "Calculate correct leg length b = 12 cm", "marks": 1},
            ],
            [
                "The hypotenuse is the longest side, so the leg must be less than 13 cm.",
                "To find a shorter side, subtract: b² = 13² - 5².",
                "b = √144 = 12 cm.",
            ],
        ),
        (
            f"{name} tried to apply the formula \\(a^2 + b^2 = c^2\\) to an acute triangle with angles "
            f"\\(50^\\circ\\), \\(60^\\circ\\), and \\(70^\\circ\\).\n"
            f"Explain why the Theorem of Pythagoras cannot be applied to this triangle.",
            f"**Misconception Analysis:**\n"
            f"The Theorem of Pythagoras applies **strictly to right-angled triangles** (triangles containing exactly one \\(90^\\circ\\) angle).\n"
            f"Since all angles of this triangle are less than \\(90^\\circ\\) (acute), no side is a hypotenuse, "
            f"and the relationship \\(a^2 + b^2 = c^2\\) does not hold.",
            "Pythagoras' Theorem applies strictly to right-angled triangles (containing a 90° angle).",
            "Cannot be applied because the triangle does not have a 90° right angle.",
            [
                {"desc": "State that Pythagoras applies only to right-angled triangles", "marks": 1},
                {"desc": "Note that this triangle has no 90° angle (all angles < 90°)", "marks": 1},
            ],
            [
                "What kind of triangle does Pythagoras require?",
                "The triangle must have a 90° angle.",
                "This triangle is acute (all angles < 90°), so Pythagoras does not apply.",
            ],
        ),
    ]
    prompt, sol, cor_ans, exp_ans, schema, hints = rng.choice(scenarios)

    return {
        "id": f"g9_pyth_err_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": cor_ans,
        "expected_answer": exp_ans,
        "sample_answer": cor_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": schema,
        "hints": hints,
    }


# ----------------------------------------------------------------------
# 50. Compound Multi-Step Pythagoras Synthesis
# ----------------------------------------------------------------------
def arch_50_compound_multi_step_pythagoras_synthesis(rng: random.Random) -> Dict[str, Any]:
    # A park path problem:
    # A rectangular park has length L and width W.
    # Walking around the edge takes L + W.
    # Walking directly along the diagonal saves distance: (L + W) - d.
    triples = [
        (60, 80, 100),
        (90, 120, 150),
        (50, 120, 130),
        (80, 150, 170),
        (70, 240, 250),
    ]
    w, l, d = rng.choice(triples)
    walk_around = l + w
    distance_saved = walk_around - d

    prompt = (
        f"A rectangular sports field in Soweto is \\({l}\\text{{ m}}\\) long and \\({w}\\text{{ m}}\\) wide. "
        f"Lerato wants to travel from one corner of the field to the diagonally opposite corner.\n\n"
        f"1. Calculate the length of the diagonal path across the field.\n"
        f"2. How much walking distance does Lerato save by taking the diagonal path directly across the field "
        f"instead of walking along the two outside edges?"
    )
    sol = (
        f"**Step 1: Calculate the diagonal distance across the field.**\n"
        f"The edges of the field meet at a \\(90^\\circ\\) right angle:\n"
        f"\\[ d^2 = l^2 + w^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ d^2 = ({l})^2 + ({w})^2 = {l*l} + {w*w} = {d*d} \\]\n"
        f"\\[ d = \\sqrt{{{d*d}}} = {d}\\text{{ m}} \\]\n\n"
        f"**Step 2: Calculate walking distance saved.**\n"
        f"Walking along the edges:\n"
        f"\\[ \\text{{Edge distance}} = {l} + {w} = {walk_around}\\text{{ m}} \\]\n\n"
        f"Distance saved by taking the diagonal path:\n"
        f"\\[ \\text{{Distance saved}} = {walk_around} - {d} = {distance_saved}\\text{{ m}} \\]"
    )
    return {
        "id": f"g9_pyth_synth_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Diagonal = {d} m, Distance saved = {distance_saved} m",
        "expected_answer": f"{distance_saved} m",
        "sample_answer": f"Diagonal = {d} m, Distance saved = {distance_saved} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": f"Apply Pythagoras to find diagonal d = {d} m", "marks": 2},
            {"desc": f"Calculate perimeter edge path = {walk_around} m", "marks": 1},
            {"desc": f"Calculate distance saved: {walk_around} - {d} = {distance_saved} m", "marks": 1},
        ],
        "hints": [
            f"Use Pythagoras: d² = {l}² + {w}².",
            f"The diagonal path is {d} m.",
            f"Compare {l + w} m with {d} m to find the distance saved ({distance_saved} m).",
        ],
    }
