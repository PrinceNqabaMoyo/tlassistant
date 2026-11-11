"""Grade 9 Mathematics - Area and Perimeter of 2D Shapes Archetypes 01 to 25
=============================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 3 Topic: Area and perimeter of 2D shapes
  - curriculum_docs_auto/Mathematics_Gr9/Term 3/03. Area and perimeter of 2D shapes.md
  - Chapter 14: Squares, rectangles, triangles, parallelograms, rhombi, kites, trapezia,
    circles, semicircles, and quadrants.

Covers Archetypes 01 - 25:
  01: Perimeter of rectangles and squares
  02: Area of squares and rectangles
  03: Find missing dimension given area or perimeter
  04: Perimeter of triangles (scalene, isosceles, equilateral)
  05: Area of right-angled triangles
  06: Area of acute triangles given base and perpendicular height
  07: Area of obtuse triangles with external perpendicular altitude
  08: Find base or height of triangle given area
  09: Perimeter of parallelogram and rhombus
  10: Area of parallelogram (base x perpendicular height)
  11: Find perpendicular height of parallelogram given area
  12: Area of rhombus using diagonals (1/2 * d1 * d2)
  13: Area of kite using diagonals (1/2 * d1 * d2)
  14: Find missing diagonal of rhombus or kite given area
  15: Area of trapezium (1/2 * (a + b) * h)
  16: Find height or parallel side of trapezium given area
  17: Circumference of circle given radius or diameter
  18: Find radius or diameter given circumference
  19: Perimeter of semicircle (curved arc + flat diameter boundary)
  20: Perimeter of quarter-circle quadrant (curved arc + 2 radii)
  21: Area of circle given radius
  22: Area of circle given diameter
  23: Find radius of circle given area
  24: Area of semicircle
  25: Area of quarter-circle quadrant
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.area_perimeter_2d_svg import (
    draw_triangle_with_altitude_svg,
    draw_quadrilateral_svg,
    draw_circle_figure_svg,
)


def arch_01_perimeter_of_rectangles_and_squares(rng: random.Random) -> Dict[str, Any]:
    """Calculate perimeter of rectangle or square."""
    is_square = rng.choice([True, False])
    seed_val = rng.randint(1000, 999999)

    if is_square:
        s = rng.randint(4, 18)
        p = 4 * s
        prompt = (
            f"A square has side lengths measuring **${s}\\text{{ cm}}$**.\n\n"
            f"Calculate the **perimeter** of the square in centimetres."
        )
        schema = [
            {"step": f"State perimeter formula: P = 4s", "marks": 1},
            {"step": f"Calculate: P = 4 * {s} = {p} cm", "marks": 1},
        ]
        hints = [
            "A square has four equal sides.",
            f"Perimeter $P = 4 \\times {s}$.",
            f"Perimeter $= {p}\\text{{ cm}}$.",
        ]
        svg = draw_quadrilateral_svg("rectangle", s, s, label_a=f"{s} cm", label_b=f"{s} cm", seed=seed_val)
    else:
        l = rng.randint(8, 20)
        b = rng.randint(3, l - 1)
        p = 2 * (l + b)
        prompt = (
            f"A rectangle has length **${l}\\text{{ cm}}$** and breadth **${b}\\text{{ cm}}$**.\n\n"
            f"Calculate the **perimeter** of the rectangle in centimetres."
        )
        schema = [
            {"step": f"State perimeter formula: P = 2(l + b)", "marks": 1},
            {"step": f"Calculate: P = 2 * ({l} + {b}) = 2 * {l + b} = {p} cm", "marks": 1},
        ]
        hints = [
            "Perimeter of a rectangle is the sum of all four sides: $P = 2(l + b)$.",
            f"Add length and breadth: ${l} + {b} = {l + b}$, then double.",
            f"Perimeter $= {p}\\text{{ cm}}$.",
        ]
        svg = draw_quadrilateral_svg("rectangle", l, b, label_a=f"{l} cm", label_b=f"{b} cm", seed=seed_val)

    return {
        "subskill": "01_perimeter_of_rectangles_and_squares",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(p),
        "sample_answer": f"{p} cm",
        "tolerance": 0.0,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["perimeter_formula_error", "adding_only_two_sides_error"],
    }


def arch_02_area_of_squares_and_rectangles(rng: random.Random) -> Dict[str, Any]:
    """Calculate area of rectangle or square."""
    is_square = rng.choice([True, False])
    seed_val = rng.randint(1000, 999999)

    if is_square:
        s = rng.randint(5, 15)
        area = s * s
        prompt = (
            f"Calculate the **area** of a square with side length **${s}\\text{{ cm}}$** in square centimetres ($\\text{{cm}}^2$)."
        )
        schema = [
            {"step": f"State formula: Area = s^2", "marks": 1},
            {"step": f"Calculate: {s}^2 = {area} cm^2", "marks": 1},
        ]
        hints = [
            "Area of a square is side squared: $A = s^2$.",
            f"Calculate ${s} \\times {s}$.",
            f"Area $= {area}\\text{{ cm}}^2$.",
        ]
        svg = draw_quadrilateral_svg("rectangle", s, s, label_a=f"{s} cm", label_b=f"{s} cm", seed=seed_val)
    else:
        l = rng.randint(7, 18)
        b = rng.randint(3, l - 1)
        area = l * b
        prompt = (
            f"Calculate the **area** of a rectangle with length **${l}\\text{{ cm}}$** and breadth **${b}\\text{{ cm}}$** in square centimetres ($\\text{{cm}}^2$)."
        )
        schema = [
            {"step": f"State formula: Area = l * b", "marks": 1},
            {"step": f"Calculate: {l} * {b} = {area} cm^2", "marks": 1},
        ]
        hints = [
            "Area of a rectangle is length times breadth: $A = l \\times b$.",
            f"Multiply: ${l} \\times {b}$.",
            f"Area $= {area}\\text{{ cm}}^2$.",
        ]
        svg = draw_quadrilateral_svg("rectangle", l, b, label_a=f"{l} cm", label_b=f"{b} cm", seed=seed_val)

    return {
        "subskill": "02_area_of_squares_and_rectangles",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": schema,
        "hints": hints,
        "misconception_tags": ["area_vs_perimeter_confusion", "multiplication_arithmetic_error"],
    }


def arch_03_find_missing_dimension_given_area_or_perimeter(rng: random.Random) -> Dict[str, Any]:
    """Find missing breadth of rectangle given area and length."""
    b = rng.randint(4, 12)
    l = rng.randint(b + 2, 20)
    area = l * b

    prompt = (
        f"A rectangular garden has an area of **${area}\\text{{ m}}^2$** and a length of **${l}\\text{{ m}}$**.\n\n"
        f"Calculate the **breadth** of the garden in metres."
    )

    return {
        "subskill": "03_find_missing_dimension_given_area_or_perimeter",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(b),
        "sample_answer": f"{b} m",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State area formula: Area = l * b => b = Area / l", "marks": 1},
            {"step": f"Calculate: {area} / {l} = {b} metres", "marks": 1},
        ],
        "hints": [
            "Since $\\text{Area} = l \\times b$, rearrange to solve for breadth: $b = \\frac{\\text{Area}}{l}$.",
            f"Divide ${area}$ by ${l}$.",
            f"Breadth $= {b}\\text{{ m}}$.",
        ],
        "misconception_tags": ["inverse_operation_error", "subtraction_instead_of_division"],
    }


def arch_04_perimeter_of_triangles_all_types(rng: random.Random) -> Dict[str, Any]:
    """Calculate perimeter of triangle given 3 side lengths."""
    a = rng.randint(5, 12)
    b = rng.randint(5, 12)
    c = rng.randint(abs(a - b) + 1, a + b - 1)
    perimeter = a + b + c

    prompt = (
        f"A triangular field has sides measuring **${a}\\text{{ m}}$**, **${b}\\text{{ m}}$**, "
        f"and **${c}\\text{{ m}}$**.\n\n"
        f"Calculate the **perimeter** of the field in metres."
    )

    return {
        "subskill": "04_perimeter_of_triangles_all_types",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(perimeter),
        "sample_answer": f"{perimeter} m",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State perimeter formula: P = a + b + c", "marks": 1},
            {"step": f"Calculate: {a} + {b} + {c} = {perimeter} m", "marks": 1},
        ],
        "hints": [
            "The perimeter of any triangle is the sum of its three sides.",
            f"Add: ${a} + {b} + {c}$.",
            f"Perimeter $= {perimeter}\\text{{ m}}$.",
        ],
        "misconception_tags": ["triangle_perimeter_sum_error"],
    }


def arch_05_area_of_right_angled_triangles(rng: random.Random) -> Dict[str, Any]:
    """Area of right-angled triangle using perpendicular legs."""
    b, h, hyp = rng.choice([(6, 8, 10), (8, 6, 10), (5, 12, 13), (12, 5, 13), (9, 12, 15)])
    area = (b * h) // 2
    seed_val = rng.randint(1000, 999999)
    svg = draw_triangle_with_altitude_svg(b, h, triangle_type="right", base_label=f"base = {b} cm", height_label=f"height = {h} cm", seed=seed_val)

    prompt = (
        f"Refer to the right-angled triangle below with perpendicular legs of **${b}\\text{{ cm}}$** and **${h}\\text{{ cm}}$** "
        f"(and hypotenuse ${hyp}\\text{{ cm}}$):\n\n"
        f"Calculate the **area** of the triangle in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "05_area_of_right_angled_triangles",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State area formula: Area = 1/2 * base * height", "marks": 1},
            {"step": f"Calculate: 1/2 * {b} * {h} = {area} cm^2", "marks": 1},
        ],
        "hints": [
            "In a right-angled triangle, the two legs meeting at $90^\\circ$ serve as the base and perpendicular height.",
            f"Area $= \\frac{{1}}{{2}} \\times {b} \\times {h}$.",
            f"Area $= {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["used_hypotenuse_as_height", "forgot_to_halve_triangle_area"],
    }


def arch_06_area_of_acute_triangles_given_base_and_height(rng: random.Random) -> Dict[str, Any]:
    """Area of acute triangle given base and internal perpendicular height."""
    b = rng.choice([8, 10, 12, 14, 16])
    h = rng.randint(5, 11)
    area = (b * h) // 2
    seed_val = rng.randint(1000, 999999)
    svg = draw_triangle_with_altitude_svg(b, h, triangle_type="acute", base_label=f"b = {b} cm", height_label=f"h = {h} cm", seed=seed_val)

    prompt = (
        f"In the triangle below, the base has a length of **${b}\\text{{ cm}}$** and the perpendicular height "
        f"(altitude) is **${h}\\text{{ cm}}$**:\n\n"
        f"Calculate the **area** of the triangle in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "06_area_of_acute_triangles_given_base_and_height",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State area formula: Area = 1/2 * base * height", "marks": 1},
            {"step": f"Calculate: 1/2 * {b} * {h} = {area} cm^2", "marks": 1},
        ],
        "hints": [
            "Formula: $\\text{Area} = \\frac{1}{2} b h$.",
            f"Multiply: $\\frac{{1}}{{2}} \\times {b} \\times {h}$.",
            f"Area $= {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["triangle_area_formula_error", "forgot_to_halve_triangle_area"],
    }


def arch_07_area_of_obtuse_triangles_external_altitude(rng: random.Random) -> Dict[str, Any]:
    """Area of obtuse triangle with external dropped perpendicular altitude."""
    b = rng.choice([6, 8, 10, 12])
    h = rng.randint(4, 9)
    area = (b * h) // 2
    seed_val = rng.randint(1000, 999999)
    svg = draw_triangle_with_altitude_svg(b, h, triangle_type="obtuse", base_label=f"b = {b} cm", height_label=f"h = {h} cm", seed=seed_val)

    prompt = (
        f"Refer to the obtuse-angled triangle below. The base measures **${b}\\text{{ cm}}$** and the external "
        f"perpendicular height dropped to the extended base is **${h}\\text{{ cm}}$**:\n\n"
        f"Calculate the **area** of the obtuse triangle in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "07_area_of_obtuse_triangles_external_altitude",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recognize that external altitude is the true perpendicular height h corresponding to base b", "marks": 1},
            {"step": f"Calculate: Area = 1/2 * {b} * {h} = {area} cm^2", "marks": 1},
        ],
        "hints": [
            "The area of an obtuse triangle still uses $\\text{Area} = \\frac{1}{2} b h$, using the base of the triangle (not the extended base).",
            f"$\\text{{Area}} = \\frac{{1}}{{2}} \\times {b} \\times {h}$.",
            f"Area $= {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["added_extension_to_base_error", "external_altitude_confusion"],
    }


def arch_08_find_base_or_height_of_triangle_given_area(rng: random.Random) -> Dict[str, Any]:
    """Find perpendicular height of triangle given area and base."""
    b = rng.choice([6, 8, 10, 12, 14])
    h = rng.randint(4, 12)
    area = (b * h) // 2

    prompt = (
        f"A triangle has an area of **${area}\\text{{ cm}}^2$** and a base of **${b}\\text{{ cm}}$**.\n\n"
        f"Calculate the **perpendicular height** of the triangle in centimetres."
    )

    return {
        "subskill": "08_find_base_or_height_of_triangle_given_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(h),
        "sample_answer": f"{h} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Rearrange formula: Area = 1/2 * b * h => h = (2 * Area) / b", "marks": 1},
            {"step": f"Calculate: (2 * {area}) / {b} = {2 * area} / {b} = {h} cm", "marks": 1},
        ],
        "hints": [
            "Start with $\\text{Area} = \\frac{1}{2} b h$. Multiply both sides by $2$: $2 \\times \\text{Area} = b \\times h$.",
            f"Then divide by base: $h = \\frac{{2 \\times {area}}}{{{b}}}$.",
            f"Height $= {h}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["forgot_to_multiply_area_by_two", "triangle_height_rearrangement_error"],
    }


def arch_09_perimeter_of_parallelogram_and_rhombus(rng: random.Random) -> Dict[str, Any]:
    """Calculate perimeter of parallelogram given adjacent sides."""
    a = rng.randint(8, 16)
    b = rng.randint(4, a - 2)
    perimeter = 2 * (a + b)

    prompt = (
        f"A parallelogram has adjacent sides of length **${a}\\text{{ cm}}$** and **${b}\\text{{ cm}}$**.\n\n"
        f"Calculate the **perimeter** of the parallelogram in centimetres."
    )

    return {
        "subskill": "09_perimeter_of_parallelogram_and_rhombus",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(perimeter),
        "sample_answer": f"{perimeter} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State perimeter formula for parallelogram: P = 2(a + b)", "marks": 1},
            {"step": f"Calculate: 2 * ({a} + {b}) = 2 * {a + b} = {perimeter} cm", "marks": 1},
        ],
        "hints": [
            "Opposite sides of a parallelogram are equal in length.",
            f"Perimeter $= 2 \\times ({a} + {b})$.",
            f"Perimeter $= {perimeter}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["parallelogram_perimeter_formula_error"],
    }


def arch_10_area_of_parallelogram_base_times_height(rng: random.Random) -> Dict[str, Any]:
    """Calculate area of parallelogram given base, slant side, and perpendicular height."""
    b = rng.randint(8, 16)
    slant = rng.randint(5, 10)
    h = slant - rng.choice([1, 2])
    area = b * h
    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg("parallelogram", b, slant, param_h=h, label_a=f"base = {b} cm", label_h=f"h = {h} cm", seed=seed_val)

    prompt = (
        f"Refer to the parallelogram below with base **${b}\\text{{ cm}}$**, slanted side **${slant}\\text{{ cm}}$**, "
        f"and perpendicular height **${h}\\text{{ cm}}$**:\n\n"
        f"Calculate the **area** of the parallelogram in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "10_area_of_parallelogram_base_times_height",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State area formula: Area = base * perpendicular_height (ignore slanted side)", "marks": 1},
            {"step": f"Calculate: {b} * {h} = {area} cm^2", "marks": 1},
        ],
        "hints": [
            "Area of a parallelogram is $\\text{base} \\times \\text{perpendicular height}$. Never multiply by the slanted side.",
            f"Multiply: ${b} \\times {h}$.",
            f"Area $= {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["used_slant_height_instead_of_perp_height", "halved_parallelogram_area_error"],
    }


def arch_11_find_perpendicular_height_of_parallelogram(rng: random.Random) -> Dict[str, Any]:
    """Find perpendicular height of parallelogram given area and base."""
    b = rng.randint(6, 15)
    h = rng.randint(4, 12)
    area = b * h

    prompt = (
        f"A parallelogram has an area of **${area}\\text{{ m}}^2$** and a base length of **${b}\\text{{ m}}$**.\n\n"
        f"Calculate the **perpendicular height** of the parallelogram in metres."
    )

    return {
        "subskill": "11_find_perpendicular_height_of_parallelogram",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(h),
        "sample_answer": f"{h} m",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State formula: Area = base * height => height = Area / base", "marks": 1},
            {"step": f"Calculate: {area} / {b} = {h} metres", "marks": 1},
        ],
        "hints": [
            "Since $\\text{Area} = b \\times h$, rearrange: $h = \\frac{\\text{Area}}{b}$.",
            f"Divide ${area}$ by ${b}$.",
            f"Height $= {h}\\text{{ m}}$.",
        ],
        "misconception_tags": ["parallelogram_height_inversion_error"],
    }


def arch_12_area_of_rhombus_using_diagonals(rng: random.Random) -> Dict[str, Any]:
    """Area of rhombus using diagonals: A = 1/2 * d1 * d2."""
    d1 = rng.choice([6, 8, 10, 12, 14])
    d2 = rng.choice([8, 10, 12, 16, 20])
    area = (d1 * d2) // 2
    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg("rhombus", d1, d2, label_a=f"d1 = {d1} cm", label_b=f"d2 = {d2} cm", seed=seed_val)

    prompt = (
        f"Refer to the rhombus below. The diagonals intersect at right angles with lengths of "
        f"**${d1}\\text{{ cm}}$** and **${d2}\\text{{ cm}}$**:\n\n"
        f"Calculate the **area** of the rhombus in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "12_area_of_rhombus_using_diagonals",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State area formula: Area = 1/2 * d1 * d2", "marks": 1},
            {"step": f"Calculate: 1/2 * {d1} * {d2} = {area} cm^2", "marks": 1},
        ],
        "hints": [
            "Formula for area of a rhombus using diagonals: $\\text{Area} = \\frac{1}{2} d_1 d_2$.",
            f"Multiply: $\\frac{{1}}{{2}} \\times {d1} \\times {d2}$.",
            f"Area $= {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["rhombus_area_forgot_to_halve", "diagonal_product_error"],
    }


def arch_13_area_of_kite_using_diagonals(rng: random.Random) -> Dict[str, Any]:
    """Area of kite using diagonals: A = 1/2 * d1 * d2."""
    d1 = rng.choice([8, 10, 12, 14])
    d2 = rng.choice([10, 12, 16, 18, 22])
    area = (d1 * d2) // 2
    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg("kite", d1, d2, label_a=f"d1 = {d1} cm", label_b=f"d2 = {d2} cm", seed=seed_val)

    prompt = (
        f"A decorative kite has two perpendicular diagonals measuring **${d1}\\text{{ cm}}$** and **${d2}\\text{{ cm}}$**.\n\n"
        f"Calculate the **area** of the kite in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "13_area_of_kite_using_diagonals",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State area formula: Area = 1/2 * d1 * d2", "marks": 1},
            {"step": f"Calculate: 1/2 * {d1} * {d2} = {area} cm^2", "marks": 1},
        ],
        "hints": [
            "The area of a kite is half the product of its diagonals: $\\text{Area} = \\frac{1}{2} d_1 d_2$.",
            f"Calculate $\\frac{{1}}{{2}} \\times {d1} \\times {d2}$.",
            f"Area $= {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["kite_area_forgot_half_factor"],
    }


def arch_14_find_missing_diagonal_of_rhombus_or_kite(rng: random.Random) -> Dict[str, Any]:
    """Find missing diagonal of kite or rhombus given area and one diagonal."""
    d1 = rng.choice([6, 8, 10, 12])
    d2 = rng.choice([10, 12, 14, 16, 18])
    area = (d1 * d2) // 2

    prompt = (
        f"A kite has an area of **${area}\\text{{ cm}}^2$** and one diagonal measuring **${d1}\\text{{ cm}}$**.\n\n"
        f"Calculate the length of the **second diagonal** in centimetres."
    )

    return {
        "subskill": "14_find_missing_diagonal_of_rhombus_or_kite",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(d2),
        "sample_answer": f"{d2} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State formula: Area = 1/2 * d1 * d2 => d2 = (2 * Area) / d1", "marks": 1},
            {"step": f"Calculate: (2 * {area}) / {d1} = {2 * area} / {d1} = {d2} cm", "marks": 1},
        ],
        "hints": [
            "Start with $\\text{Area} = \\frac{1}{2} d_1 d_2$.",
            f"Multiply Area by $2$: $2 \\times {area} = {2 * area}$.",
            f"Divide by $d_1$: $d_2 = \\frac{{{2 * area}}}{{{d1}}} = {d2}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["forgot_to_multiply_by_two_in_diagonal_calc"],
    }


def arch_15_area_of_trapezium_parallel_sides_and_height(rng: random.Random) -> Dict[str, Any]:
    """Area of trapezium: A = 1/2 * (a + b) * h."""
    a = rng.randint(4, 10)
    b = rng.randint(a + 4, 18)
    h = rng.choice([4, 6, 8, 10])
    area = ((a + b) * h) // 2
    seed_val = rng.randint(1000, 999999)
    svg = draw_quadrilateral_svg("trapezium", a, b, param_h=h, label_a=f"a = {a} cm", label_b=f"b = {b} cm", label_h=f"h = {h} cm", seed=seed_val)

    prompt = (
        f"Refer to the trapezium below with parallel sides of length **${a}\\text{{ cm}}$** and **${b}\\text{{ cm}}$**, "
        f"and perpendicular height **${h}\\text{{ cm}}$**:\n\n"
        f"Calculate the **area** of the trapezium in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "15_area_of_trapezium_parallel_sides_and_height",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State area formula: Area = 1/2 * (a + b) * h", "marks": 1},
            {"step": f"Add parallel sides: {a} + {b} = {a + b}", "marks": 1},
            {"step": f"Calculate: 1/2 * {a + b} * {h} = {area} cm^2", "marks": 1},
        ],
        "hints": [
            "Formula for area of a trapezium: $\\text{Area} = \\frac{1}{2}(a + b)h$.",
            f"Sum parallel sides: ${a} + {b} = {a + b}\\text{{ cm}}$.",
            f"Multiply: $\\frac{{1}}{{2}} \\times {a + b} \\times {h} = {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["trapezium_area_formula_error", "forgot_to_halve_trapezium_sum"],
    }


def arch_16_find_height_or_parallel_side_of_trapezium(rng: random.Random) -> Dict[str, Any]:
    """Find height of trapezium given area and parallel sides."""
    a = rng.randint(5, 9)
    b = rng.randint(11, 17)
    h = rng.choice([4, 6, 8, 10])
    area = ((a + b) * h) // 2

    prompt = (
        f"A trapezium has an area of **${area}\\text{{ cm}}^2$** and parallel sides of length "
        f"**${a}\\text{{ cm}}$** and **${b}\\text{{ cm}}$**.\n\n"
        f"Calculate the **perpendicular height** of the trapezium in centimetres."
    )

    return {
        "subskill": "16_find_height_or_parallel_side_of_trapezium",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(h),
        "sample_answer": f"{h} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State formula: Area = 1/2 * (a + b) * h => h = (2 * Area) / (a + b)", "marks": 1},
            {"step": f"Calculate: (2 * {area}) / ({a} + {b}) = {2 * area} / {a + b} = {h} cm", "marks": 1},
        ],
        "hints": [
            "Formula: $h = \\frac{2 \\times \\text{Area}}{a + b}$.",
            f"Double the area: $2 \\times {area} = {2 * area}$.",
            f"Divide by the sum of parallel sides (${a + b}$): $\\frac{{{2 * area}}}{{{a + b}}} = {h}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["trapezium_height_rearrangement_error"],
    }


def arch_17_circumference_of_circle_given_radius_or_diameter(rng: random.Random) -> Dict[str, Any]:
    """Calculate circumference of circle using pi = 22/7."""
    k = rng.choice([1, 2, 3, 4])
    r = 7 * k
    c = 2 * 22 * k  # C = 2 * (22/7) * (7k) = 44k
    seed_val = rng.randint(1000, 999999)
    svg = draw_circle_figure_svg(r, kind="circle", label_r=f"r = {r} cm", seed=seed_val)

    prompt = (
        f"A circular pond has a radius of **${r}\\text{{ cm}}$**.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **circumference** of the pond in centimetres."
    )

    return {
        "subskill": "17_circumference_of_circle_given_radius_or_diameter",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(c),
        "sample_answer": f"{c} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State circumference formula: C = 2 * pi * r", "marks": 1},
            {"step": f"Substitute: 2 * (22/7) * {r} = {c} cm", "marks": 1},
        ],
        "hints": [
            "Formula for circumference: $C = 2\\pi r$.",
            f"Substitute $r = {r}$ and $\\pi = \\frac{{22}}{{7}}$: $C = 2 \\times \\frac{{22}}{{7}} \\times {r}$.",
            f"Circumference $= {c}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["circumference_formula_diameter_confusion", "circle_circumference_arithmetic_error"],
    }


def arch_18_find_radius_or_diameter_given_circumference(rng: random.Random) -> Dict[str, Any]:
    """Find radius given circumference using pi = 22/7."""
    k = rng.choice([1, 2, 3, 5])
    r = 7 * k
    c = 44 * k

    prompt = (
        f"The circumference of a bicycle wheel is **${c}\\text{{ cm}}$**.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **radius** of the wheel in centimetres."
    )

    return {
        "subskill": "18_find_radius_or_diameter_given_circumference",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(r),
        "sample_answer": f"{r} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State formula: C = 2 * pi * r => r = C / (2 * pi)", "marks": 1},
            {"step": f"Calculate: {c} / (2 * 22/7) = {c} * 7 / 44 = {r} cm", "marks": 1},
        ],
        "hints": [
            "Since $C = 2\\pi r$, rearrange: $r = \\frac{C}{2\\pi}$.",
            f"$r = \\frac{{{c}}}{{2 \\times \\frac{{22}}{{7}}}} = \\frac{{{c} \\times 7}}{{44}}$.",
            f"Radius $= {r}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["radius_from_circumference_inversion_error"],
    }


def arch_19_perimeter_of_semicircle_curved_plus_diameter(rng: random.Random) -> Dict[str, Any]:
    """Perimeter of semicircle = curved half-circumference + flat diameter."""
    k = rng.choice([1, 2, 3])
    r = 7 * k
    d = 2 * r
    arc = 22 * k  # pi * r = (22/7) * 7k = 22k
    perimeter = arc + d  # 22k + 14k = 36k
    seed_val = rng.randint(1000, 999999)
    svg = draw_circle_figure_svg(r, kind="semicircle", label_r=f"r = {r} cm", seed=seed_val)

    prompt = (
        f"Refer to the closed semicircular region below with radius **${r}\\text{{ cm}}$** (and diameter ${d}\\text{{ cm}}$):\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **total perimeter** of the closed semicircle in centimetres."
    )

    return {
        "subskill": "19_perimeter_of_semicircle_curved_plus_diameter",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(perimeter),
        "sample_answer": f"{perimeter} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate curved arc: pi * r = (22/7) * {r} = {arc} cm", "marks": 1},
            {"step": f"Add diameter: Perimeter = {arc} + {d} = {perimeter} cm", "marks": 1},
        ],
        "hints": [
            "The boundary of a closed semicircle consists of two parts: the curved arc ($\\pi r$) AND the straight diameter ($2r$).",
            f"Curved arc $= \\frac{{22}}{{7}} \\times {r} = {arc}\\text{{ cm}}$. Diameter $= 2 \\times {r} = {d}\\text{{ cm}}$.",
            f"Total perimeter $= {arc} + {d} = {perimeter}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["forgot_diameter_in_semicircle_perimeter", "semicircle_perimeter_error"],
    }


def arch_20_perimeter_of_quarter_circle_quadrant(rng: random.Random) -> Dict[str, Any]:
    """Perimeter of quadrant = curved arc + 2 radii."""
    # arc = (1/4) * 2 * pi * r = (1/2) * (22/7) * r = 11k when r = 7k
    k = rng.choice([1, 2, 4])
    r = 7 * k
    arc = 11 * k
    perimeter = arc + 2 * r  # 11k + 14k = 25k
    seed_val = rng.randint(1000, 999999)
    svg = draw_circle_figure_svg(r, kind="quadrant", label_r=f"r = {r} cm", seed=seed_val)

    prompt = (
        f"Refer to the closed quadrant (quarter-circle) below with radius **${r}\\text{{ cm}}$**:\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **total perimeter** of the closed quadrant in centimetres."
    )

    return {
        "subskill": "20_perimeter_of_quarter_circle_quadrant",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(perimeter),
        "sample_answer": f"{perimeter} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate curved arc: (1/4) * 2 * pi * r = (1/2) * (22/7) * {r} = {arc} cm", "marks": 1},
            {"step": f"Add the two straight radii: Perimeter = {arc} + 2({r}) = {perimeter} cm", "marks": 1},
        ],
        "hints": [
            "The boundary of a quadrant consists of the curved arc plus the two straight edges (radii): $P = \\frac{1}{2}\\pi r + 2r$.",
            f"Curved arc $= {arc}\\text{{ cm}}$. Two radii $= 2 \\times {r} = {2 * r}\\text{{ cm}}$.",
            f"Total perimeter $= {arc} + {2 * r} = {perimeter}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["forgot_radii_in_quadrant_perimeter", "quadrant_arc_length_error"],
    }


def arch_21_area_of_circle_given_radius(rng: random.Random) -> Dict[str, Any]:
    """Area of circle given radius: A = pi * r^2."""
    k = rng.choice([1, 2, 3])
    r = 7 * k
    area = 22 * k * 7 * k  # (22/7) * 49k^2 = 154k^2
    seed_val = rng.randint(1000, 999999)
    svg = draw_circle_figure_svg(r, kind="circle", label_r=f"r = {r} cm", seed=seed_val)

    prompt = (
        f"A circular garden has a radius of **${r}\\text{{ m}}$**.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **area** of the garden in square metres ($\\text{{m}}^2$)."
    )

    return {
        "subskill": "21_area_of_circle_given_radius",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(area),
        "sample_answer": f"{area} m²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State area formula: Area = pi * r^2", "marks": 1},
            {"step": f"Calculate: (22/7) * {r}^2 = {area} m^2", "marks": 1},
        ],
        "hints": [
            "Formula for area of a circle: $A = \\pi r^2$.",
            f"Square the radius: ${r}^2 = {r**2}$.",
            f"Multiply by $\\frac{{22}}{{7}}$: $\\text{{Area}} = {area}\\text{{ m}}^2$.",
        ],
        "misconception_tags": ["circle_area_doubled_radius_instead_of_squared", "circle_circumference_used_for_area"],
    }


def arch_22_area_of_circle_given_diameter(rng: random.Random) -> Dict[str, Any]:
    """Area of circle given diameter: d -> r = d/2 -> A = pi * r^2."""
    k = rng.choice([1, 2])
    d = 14 * k
    r = 7 * k
    area = 154 * (k**2)

    prompt = (
        f"A circular pizza has a diameter of **${d}\\text{{ cm}}$**.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **area** of the pizza in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "22_area_of_circle_given_diameter",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(area),
        "sample_answer": f"{area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Halve diameter to find radius: r = {d} / 2 = {r} cm", "marks": 1},
            {"step": f"Calculate: Area = (22/7) * {r}^2 = {area} cm^2", "marks": 1},
        ],
        "hints": [
            f"First find the radius by dividing diameter by $2$: $r = \\frac{{{d}}}{{2}} = {r}\\text{{ cm}}$.",
            f"Then use $A = \\pi r^2$: $\\frac{{22}}{{7}} \\times {r}^2$.",
            f"Area $= {area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["used_diameter_in_area_formula_directly", "radius_diameter_confusion"],
    }


def arch_23_find_radius_of_circle_given_area(rng: random.Random) -> Dict[str, Any]:
    """Find radius given area using pi = 22/7."""
    k = rng.choice([1, 2, 3])
    r = 7 * k
    area = 154 * (k**2)

    prompt = (
        f"The area of a circle is **${area}\\text{{ cm}}^2$**.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **radius** of the circle in centimetres."
    )

    return {
        "subskill": "23_find_radius_of_circle_given_area",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(r),
        "sample_answer": f"{r} cm",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State formula: Area = pi * r^2 => r^2 = Area / pi", "marks": 1},
            {"step": f"Calculate: r^2 = {area} / (22/7) = {r**2} => r = {r} cm", "marks": 1},
        ],
        "hints": [
            "Since $A = \\pi r^2$, divide area by $\\pi$: $r^2 = \\frac{\\text{Area}}{\\pi}$.",
            f"$r^2 = \\frac{{{area} \\times 7}}{{22}} = {r**2}$.",
            f"Take the square root: $r = \\sqrt{{{r**2}}} = {r}\\text{{ cm}}$.",
        ],
        "misconception_tags": ["forgot_square_root_in_radius_calc"],
    }


def arch_24_area_of_semicircle(rng: random.Random) -> Dict[str, Any]:
    """Area of semicircle: A = 1/2 * pi * r^2."""
    k = rng.choice([1, 2])
    r = 7 * k
    full_area = 154 * (k**2)
    semi_area = full_area // 2

    prompt = (
        f"A semicircular window has a radius of **${r}\\text{{ cm}}$**.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **area** of the window in square centimetres ($\\text{{cm}}^2$)."
    )

    return {
        "subskill": "24_area_of_semicircle",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(semi_area),
        "sample_answer": f"{semi_area} cm²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State formula: Area = 1/2 * pi * r^2", "marks": 1},
            {"step": f"Calculate: 1/2 * (22/7) * {r}^2 = {semi_area} cm^2", "marks": 1},
        ],
        "hints": [
            "A semicircle is exactly half of a full circle: $\\text{Area} = \\frac{1}{2} \\pi r^2$.",
            f"Full circle area $= {full_area}\\text{{ cm}}^2$.",
            f"Divide by $2$: $\\text{{Area}} = {semi_area}\\text{{ cm}}^2$.",
        ],
        "misconception_tags": ["semicircle_area_forgot_to_halve"],
    }


def arch_25_area_of_quarter_circle_quadrant(rng: random.Random) -> Dict[str, Any]:
    """Area of quadrant: A = 1/4 * pi * r^2."""
    k = rng.choice([2, 4])  # Ensure divisible by 4
    r = 7 * k
    full_area = 154 * (k**2)
    quad_area = full_area // 4

    prompt = (
        f"A corner garden is shaped as a quarter-circle (quadrant) with radius **${r}\\text{{ m}}$**.\n\n"
        f"Using $\\pi = \\frac{{22}}{{7}}$, calculate the **area** of the quadrant in square metres ($\\text{{m}}^2$)."
    )

    return {
        "subskill": "25_area_of_quarter_circle_quadrant",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(quad_area),
        "sample_answer": f"{quad_area} m²",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State formula: Area = 1/4 * pi * r^2", "marks": 1},
            {"step": f"Calculate: 1/4 * (22/7) * {r}^2 = {quad_area} m^2", "marks": 1},
        ],
        "hints": [
            "A quadrant is one quarter of a circle: $\\text{Area} = \\frac{1}{4} \\pi r^2$.",
            f"Full circle area $= {full_area}\\text{{ m}}^2$.",
            f"Divide by $4$: $\\text{{Area}} = {quad_area}\\text{{ m}}^2$.",
        ],
        "misconception_tags": ["quadrant_area_formula_error"],
    }
