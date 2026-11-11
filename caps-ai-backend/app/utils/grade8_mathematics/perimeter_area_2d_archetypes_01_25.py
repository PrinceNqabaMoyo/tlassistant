"""Grade 8 Mathematics - Perimeter and Area of 2D Shapes Archetypes (01 to 25).
Covers:
  - Perimeter: Square, rectangle, triangles (equilateral, isosceles, scalene), regular polygons,
    parallelogram, rhombus, trapezium, kite, circle circumference, semicircle, quadrant,
    composite L-shapes, and realistic practical fencing/track word problems.
  - Area: Square, rectangle, right-angled triangles.
Strictly zero-LLM, deterministic execution parameterized by random.Random.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .perimeter_area_2d_svg import (
    draw_l_shaped_polygon_svg,
    draw_labeled_rect_svg,
    draw_parallelogram_with_height_svg,
    draw_trapezium_with_height_svg,
    draw_triangle_with_height_svg,
)


# ----------------------------------------------------------------------
# 01. Perimeter Square Formula And Calculation (WITH SVG)
# ----------------------------------------------------------------------
def arch_01_perimeter_square_formula_and_calculation(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([6, 9, 12, 15, 18, 24])
    p = 4 * s
    svg = draw_labeled_rect_svg(f"{s} cm", f"{s} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"A square has sides of length \\(s = {s}\\) cm.\n\n"
        f"1. State the formula for the perimeter \\(P\\) of a square.\n"
        f"2. Calculate the perimeter of this square in cm."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ P = 4s \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ P = 4 \\times {s} = {p} \\text{{ cm}} \\]"
    )
    ans = f"1. P = 4s; 2. {p} cm"
    return {
        "id": f"g8_perim_sq_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "01_perimeter_square_formula_and_calculation",
        "learning_objective_id": "math_g8_perim_sq",
        "hints": {
            "tier_1": "Perimeter of a square is the distance around all four equal sides: P = 4s.",
            "tier_2": f"Multiply 4 by {s}.",
            "tier_3": f"P = {p} cm.",
        },
        "misconception_tags": ["calculating_area_instead_of_perimeter_for_square"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 02. Perimeter Rectangle Formula And Calculation (WITH SVG)
# ----------------------------------------------------------------------
def arch_02_perimeter_rectangle_formula_and_calculation(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([14, 18, 22, 26, 30])
    b = rng.choice([6, 8, 10, 12])
    p = 2 * (l + b)
    svg = draw_labeled_rect_svg(f"{l} m", f"{b} m", seed=rng.randint(100, 999999))

    prompt = (
        f"A rectangular courtyard has length \\(l = {l}\\) m and breadth \\(b = {b}\\) m.\n\n"
        f"1. Write down the formula for the perimeter \\(P\\) of a rectangle.\n"
        f"2. Calculate the perimeter of the courtyard in meters."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ P = 2(l + b) \\quad \\text{{or}} \\quad P = 2l + 2b \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ P = 2({l} + {b}) = 2({l + b}) = {p} \\text{{ m}} \\]"
    )
    ans = f"1. P = 2(l + b); 2. {p} m"
    return {
        "id": f"g8_perim_rect_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "02_perimeter_rectangle_formula_and_calculation",
        "learning_objective_id": "math_g8_perim_rect",
        "hints": {
            "tier_1": "Perimeter is twice the sum of length and breadth: P = 2(l + b).",
            "tier_2": f"2 × ({l} + {b}) = 2 × {l + b}.",
            "tier_3": f"P = {p} m.",
        },
        "misconception_tags": ["adding_length_and_breadth_only_once"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 03. Perimeter Square Inverse Find Side Length (WITH SVG)
# ----------------------------------------------------------------------
def arch_03_perimeter_square_inverse_find_side_length(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([7, 11, 13, 16, 21])
    p = 4 * s
    svg = draw_labeled_rect_svg("s", "s", seed=rng.randint(100, 999999))

    prompt = (
        f"The total perimeter of a square wooden picture frame is **{p} cm**.\n\n"
        f"1. Set up an equation using the perimeter formula \\(P = 4s\\).\n"
        f"2. Solve for the side length \\(s\\) of the square in cm."
    )
    sol = (
        f"**Step 1: Equation**\n"
        f"\\[ 4s = {p} \\]\n\n"
        f"**Step 2: Solve for s**\n"
        f"\\[ s = \\frac{{{p}}}{{4}} = {s} \\text{{ cm}} \\]"
    )
    ans = f"1. 4s = {p}; 2. s = {s} cm"
    return {
        "id": f"g8_perim_sq_inv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "03_perimeter_square_inverse_find_side_length",
        "learning_objective_id": "math_g8_perim_sq_inv",
        "hints": {
            "tier_1": "Divide the total perimeter by 4.",
            "tier_2": f"{p} ÷ 4.",
            "tier_3": f"s = {s} cm.",
        },
        "misconception_tags": ["taking_square_root_of_perimeter"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 04. Perimeter Rectangle Inverse Find Breadth Or Length (WITH SVG)
# ----------------------------------------------------------------------
def arch_04_perimeter_rectangle_inverse_find_breadth_or_length(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([15, 20, 25, 30])
    b = rng.choice([7, 9, 12, 14])
    p = 2 * (l + b)
    svg = draw_labeled_rect_svg(f"{l} m", "b = ?", seed=rng.randint(100, 999999))

    prompt = (
        f"A rectangular fence has a total perimeter of **{p} m** and a length of \\(l = {l}\\) m.\n\n"
        f"1. Find the semi-perimeter (half-perimeter) \\(l + b\\).\n"
        f"2. Calculate the breadth \\(b\\) of the rectangle in meters."
    )
    semi = p // 2
    sol = (
        f"**Step 1: Semi-perimeter**\n"
        f"\\[ l + b = \\frac{{P}}{{2}} = \\frac{{{p}}}{{2}} = {semi} \\text{{ m}} \\]\n\n"
        f"**Step 2: Breadth b**\n"
        f"\\[ b = {semi} - {l} = {b} \\text{{ m}} \\]"
    )
    ans = f"1. {semi} m; 2. b = {b} m"
    return {
        "id": f"g8_perim_rect_inv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "04_perimeter_rectangle_inverse_find_breadth_or_length",
        "learning_objective_id": "math_g8_perim_rect_inv",
        "hints": {
            "tier_1": "Divide perimeter by 2, then subtract the given length.",
            "tier_2": f"{p} ÷ 2 = {semi} m, then {semi} - {l}.",
            "tier_3": f"b = {b} m.",
        },
        "misconception_tags": ["subtracting_length_directly_from_total_perimeter"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 05. Perimeter Equilateral Triangle (WITH SVG)
# ----------------------------------------------------------------------
def arch_05_perimeter_equilateral_triangle(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([8, 11, 14, 17, 20])
    p = 3 * s
    svg = draw_triangle_with_height_svg(f"{s} cm", "h", side_lbl=f"{s} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"An equilateral triangle has side lengths of **{s} cm**.\n\n"
        f"1. State the formula for the perimeter \\(P\\) of an equilateral triangle.\n"
        f"2. Calculate its perimeter in cm."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ P = 3s \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ P = 3 \\times {s} = {p} \\text{{ cm}} \\]"
    )
    ans = f"1. P = 3s; 2. {p} cm"
    return {
        "id": f"g8_perim_equi_tri_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "05_perimeter_equilateral_triangle",
        "learning_objective_id": "math_g8_perim_equi_tri",
        "hints": {
            "tier_1": "All 3 sides are equal in length.",
            "tier_2": f"3 × {s}.",
            "tier_3": f"P = {p} cm.",
        },
        "misconception_tags": ["multiplying_by_4_instead_of_3_for_triangle"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 06. Perimeter Isosceles Triangle (WITH SVG)
# ----------------------------------------------------------------------
def arch_06_perimeter_isosceles_triangle(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([10, 13, 15, 18])  # equal sides
    b = rng.choice([6, 8, 12, 14])    # base
    p = 2 * a + b
    svg = draw_triangle_with_height_svg(f"{b} cm", "h", side_lbl=f"{a} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"An isosceles triangle has two equal sides of length **{a} cm** each and a base of **{b} cm**.\n\n"
        f"1. State the formula for the perimeter \\(P\\) of an isosceles triangle.\n"
        f"2. Calculate its perimeter in cm."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ P = 2a + b \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ P = 2({a}) + {b} = {2 * a} + {b} = {p} \\text{{ cm}} \\]"
    )
    ans = f"1. P = 2a + b; 2. {p} cm"
    return {
        "id": f"g8_perim_iso_tri_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "06_perimeter_isosceles_triangle",
        "learning_objective_id": "math_g8_perim_iso_tri",
        "hints": {
            "tier_1": "Add the two equal sides and the base: P = 2a + b.",
            "tier_2": f"2 × {a} + {b}.",
            "tier_3": f"P = {p} cm.",
        },
        "misconception_tags": ["adding_equal_side_only_once"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 07. Perimeter Scalene Triangle (WITH SVG)
# ----------------------------------------------------------------------
def arch_07_perimeter_scalene_triangle(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([7, 8, 9])
    b = rng.choice([10, 11, 12])
    c = rng.choice([13, 14, 15])
    p = a + b + c
    svg = draw_triangle_with_height_svg(f"{b} cm", "h", side_lbl=f"{a} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"A scalene triangular plot has three unequal side lengths: **{a} m**, **{b} m**, and **{c} m**.\n\n"
        f"Calculate the total perimeter of the plot in meters."
    )
    sol = (
        f"**Calculation:**\n"
        f"\\[ P = a + b + c = {a} + {b} + {c} = {p} \\text{{ m}} \\]"
    )
    ans = f"{p} m"
    return {
        "id": f"g8_perim_scal_tri_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "07_perimeter_scalene_triangle",
        "learning_objective_id": "math_g8_perim_scal_tri",
        "hints": {
            "tier_1": "Perimeter is the sum of all 3 sides.",
            "tier_2": f"{a} + {b} + {c}.",
            "tier_3": f"P = {p} m.",
        },
        "misconception_tags": ["forgetting_one_side"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 08. Perimeter Regular Pentagon And Hexagon (WITH SVG)
# ----------------------------------------------------------------------
def arch_08_perimeter_regular_pentagon_and_hexagon(rng: random.Random) -> Dict[str, Any]:
    n, name = rng.choice([(5, "pentagon"), (6, "hexagon")])
    s = rng.choice([4, 6, 8, 10, 12])
    p = n * s

    prompt = (
        f"A regular **{name}** has sides each measuring **{s} cm**.\n\n"
        f"1. How many equal sides does a regular {name} have?\n"
        f"2. Calculate the perimeter of this regular {name} in cm."
    )
    sol = (
        f"**1. Number of sides:** Exactly **{n}** equal sides.\n\n"
        f"**2. Perimeter calculation:**\n"
        f"\\[ P = {n} \\times s = {n} \\times {s} = {p} \\text{{ cm}} \\]"
    )
    ans = f"1. {n}; 2. {p} cm"
    return {
        "id": f"g8_perim_reg_poly_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "08_perimeter_regular_pentagon_and_hexagon",
        "learning_objective_id": "math_g8_perim_reg_poly",
        "hints": {
            "tier_1": f"A regular {name} has {n} equal sides.",
            "tier_2": f"{n} × {s}.",
            "tier_3": f"P = {p} cm.",
        },
        "misconception_tags": ["using_wrong_number_of_sides_for_polygon"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 09. Perimeter Parallelogram And Rhombus (WITH SVG)
# ----------------------------------------------------------------------
def arch_09_perimeter_parallelogram_and_rhombus(rng: random.Random) -> Dict[str, Any]:
    is_rhombus = rng.choice([True, False])
    if is_rhombus:
        s = rng.choice([8, 12, 15, 20])
        p = 4 * s
        prompt = (
            f"A rhombus has sides of length \\(s = {s}\\) cm.\n\n"
            f"Calculate the perimeter of the rhombus in cm."
        )
        sol = (
            f"**Calculation:**\n"
            f"All four sides of a rhombus are equal in length:\n"
            f"\\[ P = 4s = 4 \\times {s} = {p} \\text{{ cm}} \\]"
        )
        ans = f"{p} cm"
        svg = draw_parallelogram_with_height_svg(f"{s} cm", "h", slant_lbl=f"{s} cm", seed=rng.randint(100, 999999))
    else:
        a = rng.choice([14, 18, 22])
        b = rng.choice([6, 9, 11])
        p = 2 * (a + b)
        prompt = (
            f"A parallelogram has adjacent sides of lengths \\(a = {a}\\) cm and \\(b = {b}\\) cm.\n\n"
            f"Calculate the perimeter of the parallelogram in cm."
        )
        sol = (
            f"**Calculation:**\n"
            f"Opposite sides of a parallelogram are equal:\n"
            f"\\[ P = 2(a + b) = 2({a} + {b}) = 2({a + b}) = {p} \\text{{ cm}} \\]"
        )
        ans = f"{p} cm"
        svg = draw_parallelogram_with_height_svg(f"{a} cm", "h", slant_lbl=f"{b} cm", seed=rng.randint(100, 999999))

    return {
        "id": f"g8_perim_parm_rhomb_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "09_perimeter_parallelogram_and_rhombus",
        "learning_objective_id": "math_g8_perim_parm_rhomb",
        "hints": {
            "tier_1": "Rhombus: P = 4s. Parallelogram: P = 2(a + b).",
            "tier_2": "Add all 4 boundary sides.",
            "tier_3": f"P = {ans}.",
        },
        "misconception_tags": ["using_perpendicular_height_instead_of_slant_side_for_perimeter"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 10. Perimeter Trapezium Sum All Sides (WITH SVG)
# ----------------------------------------------------------------------
def arch_10_perimeter_trapezium_sum_all_sides(rng: random.Random) -> Dict[str, Any]:
    top = rng.choice([8, 10, 12])
    bot = rng.choice([16, 20, 24])
    s1 = rng.choice([7, 9])
    s2 = rng.choice([8, 10])
    p = top + bot + s1 + s2

    svg = draw_trapezium_with_height_svg(f"{top} cm", f"{bot} cm", "h", seed=rng.randint(100, 999999))

    prompt = (
        f"A trapezium has parallel sides \\(a = {top}\\) cm and \\(b = {bot}\\) cm, "
        f"and non-parallel sides measuring **{s1} cm** and **{s2} cm**.\n\n"
        f"Calculate the perimeter of the trapezium in cm."
    )
    sol = (
        f"**Calculation:**\n"
        f"\\[ P = \\text{{sum of all 4 sides}} = {top} + {bot} + {s1} + {s2} = {p} \\text{{ cm}} \\]"
    )
    ans = f"{p} cm"
    return {
        "id": f"g8_perim_trap_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "10_perimeter_trapezium_sum_all_sides",
        "learning_objective_id": "math_g8_perim_trap",
        "hints": {
            "tier_1": "Perimeter is the sum of all four outer sides.",
            "tier_2": f"{top} + {bot} + {s1} + {s2}.",
            "tier_3": f"P = {p} cm.",
        },
        "misconception_tags": ["including_height_in_perimeter"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 11. Perimeter Kite Adjacent Pairs (WITH SVG)
# ----------------------------------------------------------------------
def arch_11_perimeter_kite_adjacent_pairs(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([6, 9, 12])
    b = rng.choice([14, 18, 20])
    p = 2 * (a + b)

    prompt = (
        f"A kite has two pairs of equal adjacent sides measuring \\(a = {a}\\) cm and \\(b = {b}\\) cm.\n\n"
        f"1. Write down the perimeter formula for a kite.\n"
        f"2. Calculate the perimeter of the kite in cm."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ P = 2(a + b) \\quad \\text{{or}} \\quad P = 2a + 2b \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ P = 2({a} + {b}) = 2({a + b}) = {p} \\text{{ cm}} \\]"
    )
    ans = f"1. P = 2(a + b); 2. {p} cm"
    return {
        "id": f"g8_perim_kite_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "11_perimeter_kite_adjacent_pairs",
        "learning_objective_id": "math_g8_perim_kite",
        "hints": {
            "tier_1": "Kite has two sides of length a and two sides of length b.",
            "tier_2": f"2 × ({a} + {b}).",
            "tier_3": f"P = {p} cm.",
        },
        "misconception_tags": ["adding_a_and_b_without_doubling"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 12. Circumference Circle Given Radius (WITH SVG)
# ----------------------------------------------------------------------
def arch_12_circumference_circle_given_radius(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([7, 14, 21, 28, 35])
    # using pi = 22/7 for exact clean integer arithmetic
    c_val = 2 * (22 * r // 7)

    prompt = (
        f"A circular pond has a radius of \\(r = {r}\\) m. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. State the formula for the circumference \\(C\\) of a circle in terms of radius \\(r\\).\n"
        f"2. Calculate the circumference of the pond in meters."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ C = 2\\pi r \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ C = 2 \\times \\frac{{22}}{{7}} \\times {r} = 2 \\times 22 \\times {r // 7} = {c_val} \\text{{ m}} \\]"
    )
    ans = f"1. C = 2pi*r; 2. {c_val} m"
    return {
        "id": f"g8_circ_pond_rad_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "12_circumference_circle_given_radius",
        "learning_objective_id": "math_g8_circ_pond_rad",
        "hints": {
            "tier_1": "Circumference formula is C = 2πr.",
            "tier_2": f"2 × (22/7) × {r}.",
            "tier_3": f"C = {c_val} m.",
        },
        "misconception_tags": ["using_area_formula_pi_r_squared_for_circumference"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 13. Circumference Circle Given Diameter (WITH SVG)
# ----------------------------------------------------------------------
def arch_13_circumference_circle_given_diameter(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([14, 28, 42, 56, 70])
    c_val = 22 * d // 7

    prompt = (
        f"A bicycle wheel has a diameter of \\(d = {d}\\) cm. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. State the formula for circumference in terms of diameter \\(d\\).\n"
        f"2. Calculate the circumference of the wheel in cm."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ C = \\pi d \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ C = \\frac{{22}}{{7}} \\times {d} = 22 \\times {d // 7} = {c_val} \\text{{ cm}} \\]"
    )
    ans = f"1. C = pi*d; 2. {c_val} cm"
    return {
        "id": f"g8_circ_wheel_dia_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "13_circumference_circle_given_diameter",
        "learning_objective_id": "math_g8_circ_wheel_dia",
        "hints": {
            "tier_1": "Circumference from diameter is C = πd.",
            "tier_2": f"(22/7) × {d}.",
            "tier_3": f"C = {c_val} cm.",
        },
        "misconception_tags": ["multiplying_by_2_when_already_given_diameter"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 14. Circumference Circle Inverse Find Radius (WITH SVG)
# ----------------------------------------------------------------------
def arch_14_circumference_circle_inverse_find_radius(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([7, 14, 21, 35])
    c_val = 2 * (22 * r // 7)

    prompt = (
        f"The circumference of a circular running track is **{c_val} m**. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"Calculate the radius \\(r\\) of the track in meters."
    )
    sol = (
        f"**Calculation:**\n"
        f"\\[ C = 2\\pi r \\implies {c_val} = 2 \\times \\frac{{22}}{{7}} \\times r \\]\n"
        f"\\[ {c_val} = \\frac{{44}}{{7}} r \\]\n"
        f"\\[ r = \\frac{{{c_val} \\times 7}}{{44}} = {r} \\text{{ m}} \\]"
    )
    ans = f"{r} m"
    return {
        "id": f"g8_circ_inv_rad_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "14_circumference_circle_inverse_find_radius",
        "learning_objective_id": "math_g8_circ_inv_rad",
        "hints": {
            "tier_1": "Use r = C / (2π).",
            "tier_2": f"r = ({c_val} × 7) / 44.",
            "tier_3": f"r = {r} m.",
        },
        "misconception_tags": ["dividing_by_pi_only_and_forgetting_to_divide_by_2"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 15. Circumference Circle Inverse Find Diameter (WITH SVG)
# ----------------------------------------------------------------------
def arch_15_circumference_circle_inverse_find_diameter(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([14, 28, 42, 63])
    c_val = 22 * d // 7

    prompt = (
        f"A tree trunk has a circumference of **{c_val} cm**. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"Calculate the diameter \\(d\\) of the trunk in cm."
    )
    sol = (
        f"**Calculation:**\n"
        f"\\[ C = \\pi d \\implies {c_val} = \\frac{{22}}{{7}} d \\]\n"
        f"\\[ d = \\frac{{{c_val} \\times 7}}{{22}} = {d} \\text{{ cm}} \\]"
    )
    ans = f"{d} cm"
    return {
        "id": f"g8_circ_inv_dia_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "15_circumference_circle_inverse_find_diameter",
        "learning_objective_id": "math_g8_circ_inv_dia",
        "hints": {
            "tier_1": "d = C / π.",
            "tier_2": f"d = ({c_val} × 7) / 22.",
            "tier_3": f"d = {d} cm.",
        },
        "misconception_tags": ["dividing_by_2_unnecessarily"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 16. Perimeter Semicircle Curved Plus Diameter (WITH SVG)
# ----------------------------------------------------------------------
def arch_16_perimeter_semicircle_curved_plus_diameter(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([14, 28, 42])
    r = d // 2
    curved = 22 * r // 7
    tot_p = curved + d

    prompt = (
        f"A closed semicircular garden bed has a diameter of \\(d = {d}\\) m. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. Calculate the length of the curved arc boundary.\n"
        f"2. Calculate the total perimeter of the closed semicircle in meters."
    )
    sol = (
        f"**Step 1: Curved boundary**\n"
        f"\\[ \\text{{Curved arc}} = \\frac{{1}}{{2}} \\pi d = \\frac{{1}}{{2}} \\times \\frac{{22}}{{7}} \\times {d} = {curved} \\text{{ m}} \\]\n\n"
        f"**Step 2: Total perimeter**\n"
        f"\\[ P = \\text{{Curved arc}} + d = {curved} + {d} = {tot_p} \\text{{ m}} \\]"
    )
    ans = f"1. {curved} m; 2. {tot_p} m"
    return {
        "id": f"g8_perim_semicirc_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "16_perimeter_semicircle_curved_plus_diameter",
        "learning_objective_id": "math_g8_perim_semicirc",
        "hints": {
            "tier_1": "Perimeter includes the curved half-circumference PLUS the straight diameter.",
            "tier_2": f"Curved = {curved} m. Add diameter {d} m.",
            "tier_3": f"Total perimeter = {tot_p} m.",
        },
        "misconception_tags": ["forgetting_to_add_the_diameter_boundary_to_semicircle"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 17. Perimeter Quadrant Quarter Circle Plus Two Radii (WITH SVG)
# ----------------------------------------------------------------------
def arch_17_perimeter_quadrant_quarter_circle_plus_two_radii(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([7, 14, 21, 28])
    curved = (2 * 22 * r // 7) // 4
    tot_p = curved + 2 * r

    prompt = (
        f"A quadrant (one-quarter of a circle) has a radius of \\(r = {r}\\) cm. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. Calculate the curved arc length \\(\\frac{{1}}{{4}}(2\\pi r)\\).\n"
        f"2. Calculate the total perimeter of the closed quadrant in cm."
    )
    sol = (
        f"**Step 1: Curved arc**\n"
        f"\\[ \\text{{Arc}} = \\frac{{1}}{{4}} \\times 2 \\times \\frac{{22}}{{7}} \\times {r} = {curved} \\text{{ cm}} \\]\n\n"
        f"**Step 2: Total perimeter**\n"
        f"\\[ P = \\text{{Arc}} + 2r = {curved} + 2({r}) = {curved} + {2 * r} = {tot_p} \\text{{ cm}} \\]"
    )
    ans = f"1. {curved} cm; 2. {tot_p} cm"
    return {
        "id": f"g8_perim_quadrant_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "17_perimeter_quadrant_quarter_circle_plus_two_radii",
        "learning_objective_id": "math_g8_perim_quadrant",
        "hints": {
            "tier_1": "Perimeter = (1/4 of circumference) + 2 radii.",
            "tier_2": f"Arc = {curved} cm. Add 2 × {r} = {2 * r} cm.",
            "tier_3": f"P = {tot_p} cm.",
        },
        "misconception_tags": ["forgetting_the_two_straight_radii_in_quadrant"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 18. Perimeter Composite L-Shaped Polygon (WITH SVG)
# ----------------------------------------------------------------------
def arch_18_perimeter_composite_l_shaped_polygon(rng: random.Random) -> Dict[str, Any]:
    w_tot = rng.choice([16, 20, 24])
    h_tot = rng.choice([12, 15, 18])
    w_cut = rng.choice([6, 8, 10])
    h_cut = rng.choice([5, 6, 8])

    # In any orthogonal polygon (like L-shape), the perimeter is simply 2*(W + H)
    p = 2 * (w_tot + h_tot)

    svg = draw_l_shaped_polygon_svg(
        f"{w_tot} m",
        f"{h_tot} m",
        f"{w_cut} m",
        f"{h_cut} m",
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In the given L-shaped floor plan, total width is **{w_tot} m** and total height is **{h_tot} m**.\n"
        f"The upper horizontal edge is **{w_cut} m** and the rightmost vertical edge is **{h_cut} m**.\n\n"
        f"1. Explain why the sum of all horizontal edges equals \\(2 \\times {w_tot}\\) m.\n"
        f"2. Calculate the total perimeter of the floor in meters."
    )
    sol = (
        f"**Step 1: Horizontal edges**\n"
        f"The stepped top horizontal edges project directly to match the total bottom edge: "
        f"\\({w_cut} + ({w_tot} - {w_cut}) = {w_tot}\\) m. Thus total horizontal = \\(2 \\times {w_tot}\\) m.\n\n"
        f"**Step 2: Total perimeter**\n"
        f"\\[ P = 2({w_tot} + {h_tot}) = 2({w_tot + h_tot}) = {p} \\text{{ m}} \\]"
    )
    ans = f"1. stepped edges project to total width; 2. {p} m"
    return {
        "id": f"g8_perim_l_shape_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "18_perimeter_composite_l_shaped_polygon",
        "learning_objective_id": "math_g8_perim_l_shape",
        "hints": {
            "tier_1": "The perimeter of an L-shape is the same as the enclosing rectangle: 2(W + H).",
            "tier_2": f"2 × ({w_tot} + {h_tot}).",
            "tier_3": f"P = {p} m.",
        },
        "misconception_tags": ["subtracting_the_cutout_corner_from_perimeter"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 19. Perimeter Word Problem Fencing Garden With Gate (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_19_perimeter_word_problem_fencing_garden_with_gate(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([25, 30, 35])
    b = rng.choice([15, 20, 22])
    gate = rng.choice([2, 3, 4])
    rate = rng.choice([85, 95, 120])  # Rand per meter

    p_tot = 2 * (l + b)
    fence_len = p_tot - gate
    cost = fence_len * rate

    prompt = (
        f"A rectangular vegetable garden measures **{l} m** by **{b} m**.\n"
        f"The owner wants to erect wire fencing around the entire boundary, leaving a **{gate} m** opening for a gate.\n\n"
        f"1. Calculate the total perimeter of the garden boundary in meters.\n"
        f"2. How many meters of wire fencing are required after deducting the gate?\n"
        f"3. If fencing costs **R{rate} per meter**, calculate the total cost in Rands."
    )
    sol = (
        f"**Step 1: Total perimeter**\n"
        f"\\[ P = 2({l} + {b}) = 2({l + b}) = {p_tot} \\text{{ m}} \\]\n\n"
        f"**Step 2: Fencing needed**\n"
        f"\\[ \\text{{Fence length}} = {p_tot} - {gate} = {fence_len} \\text{{ m}} \\]\n\n"
        f"**Step 3: Total cost**\n"
        f"\\[ \\text{{Cost}} = {fence_len} \\times {rate} = \\text{{R}}{cost} \\]"
    )
    ans = f"1. {p_tot} m; 2. {fence_len} m; 3. R{cost}"
    return {
        "id": f"g8_perim_fence_cost_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "19_perimeter_word_problem_fencing_garden_with_gate",
        "learning_objective_id": "math_g8_perim_fence_cost",
        "hints": {
            "tier_1": "Find full perimeter first, then subtract the gate width.",
            "tier_2": f"Perimeter = {p_tot} m, fence = {fence_len} m.",
            "tier_3": f"Cost = {fence_len} × R{rate} = R{cost}.",
        },
        "misconception_tags": ["forgetting_to_deduct_gate_opening"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 20. Perimeter Word Problem Athletic Track Straight And Semicircles (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_20_perimeter_word_problem_athletic_track_straight_and_semicircles(rng: random.Random) -> Dict[str, Any]:
    straight = rng.choice([80, 100, 110])
    dia = rng.choice([56, 70, 84])
    # Two semicircles combine to 1 full circle circumference = pi * dia
    circ = 22 * dia // 7
    total_lap = 2 * straight + circ

    prompt = (
        f"An athletics running track consists of two parallel straight sections of **{straight} m** each, "
        f"connected at the ends by two identical semicircular bends with diameter \\(d = {dia}\\) m. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. What is the combined distance of the two straight sections?\n"
        f"2. What is the combined distance of the two semicircular bends (one full circumference)?\n"
        f"3. Calculate the total distance of one complete lap around the track in meters."
    )
    sol = (
        f"**Step 1: Two straights**\n"
        f"\\[ 2 \\times {straight} = {2 * straight} \\text{{ m}} \\]\n\n"
        f"**Step 2: Two semicircles**\n"
        f"\\[ \\text{{Circumference}} = \\pi d = \\frac{{22}}{{7}} \\times {dia} = {circ} \\text{{ m}} \\]\n\n"
        f"**Step 3: Total lap distance**\n"
        f"\\[ \\text{{Total}} = {2 * straight} + {circ} = {total_lap} \\text{{ m}} \\]"
    )
    ans = f"1. {2 * straight} m; 2. {circ} m; 3. {total_lap} m"
    return {
        "id": f"g8_perim_track_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "20_perimeter_word_problem_athletic_track_straight_and_semicircles",
        "learning_objective_id": "math_g8_perim_track",
        "hints": {
            "tier_1": "Two semicircles form one full circle of diameter d.",
            "tier_2": f"2 × {straight} = {2 * straight} m; πd = {circ} m.",
            "tier_3": f"Total = {total_lap} m.",
        },
        "misconception_tags": ["adding_diameter_to_the_track_perimeter"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 21. Area Square Direct Formula (WITH SVG)
# ----------------------------------------------------------------------
def arch_21_area_square_direct_formula(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([7, 9, 12, 14, 16, 20])
    a = s * s
    svg = draw_labeled_rect_svg(f"{s} cm", f"{s} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"A square ceramic tile has side lengths of \\(s = {s}\\) cm.\n\n"
        f"1. State the formula for the area \\(A\\) of a square.\n"
        f"2. Calculate the area of the tile in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = s^2 \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A = {s}^2 = {s} \\times {s} = {a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. A = s^2; 2. {a} cm²"
    return {
        "id": f"g8_area_sq_direct_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "21_area_square_direct_formula",
        "learning_objective_id": "math_g8_area_sq_direct",
        "hints": {
            "tier_1": "Area of a square is side squared: A = s².",
            "tier_2": f"{s} × {s}.",
            "tier_3": f"A = {a} cm².",
        },
        "misconception_tags": ["multiplying_by_4_instead_of_squaring"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 22. Area Square Inverse Square Root Side (WITH SVG)
# ----------------------------------------------------------------------
def arch_22_area_square_inverse_square_root_side(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([8, 11, 13, 15, 17, 25])
    a = s * s
    svg = draw_labeled_rect_svg("s = ?", "s = ?", seed=rng.randint(100, 999999))

    prompt = (
        f"The area of a square hall floor is **{a} \\(\\text{{m}}^2\\)**.\n\n"
        f"1. Set up an equation using the area formula \\(A = s^2\\).\n"
        f"2. Calculate the length of one side \\(s\\) of the hall in meters."
    )
    sol = (
        f"**Step 1: Equation**\n"
        f"\\[ s^2 = {a} \\]\n\n"
        f"**Step 2: Solve for s**\n"
        f"\\[ s = \\sqrt{{{a}}} = {s} \\text{{ m}} \\]"
    )
    ans = f"1. s^2 = {a}; 2. s = {s} m"
    return {
        "id": f"g8_area_sq_inv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "22_area_square_inverse_square_root_side",
        "learning_objective_id": "math_g8_area_sq_inv",
        "hints": {
            "tier_1": "Take the square root of the area: s = √A.",
            "tier_2": f"√{a}.",
            "tier_3": f"s = {s} m.",
        },
        "misconception_tags": ["dividing_area_by_4_instead_of_taking_square_root"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 23. Area Rectangle Direct Formula (WITH SVG)
# ----------------------------------------------------------------------
def arch_23_area_rectangle_direct_formula(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([12, 16, 20, 25, 30])
    b = rng.choice([5, 8, 10, 14])
    a = l * b
    svg = draw_labeled_rect_svg(f"{l} m", f"{b} m", seed=rng.randint(100, 999999))

    prompt = (
        f"A rectangular soccer pitch has length \\(l = {l}\\) m and breadth \\(b = {b}\\) m.\n\n"
        f"1. Write down the formula for the area \\(A\\) of a rectangle.\n"
        f"2. Calculate the area of the pitch in \\(\\text{{m}}^2\\)."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = l \\times b \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A = {l} \\times {b} = {a} \\text{{ m}}^2 \\]"
    )
    ans = f"1. A = l * b; 2. {a} m²"
    return {
        "id": f"g8_area_rect_direct_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "23_area_rectangle_direct_formula",
        "learning_objective_id": "math_g8_area_rect_direct",
        "hints": {
            "tier_1": "Area of rectangle = length × breadth.",
            "tier_2": f"{l} × {b}.",
            "tier_3": f"A = {a} m².",
        },
        "misconception_tags": ["calculating_perimeter_instead_of_area"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 24. Area Rectangle Inverse Find Length Or Breadth (WITH SVG)
# ----------------------------------------------------------------------
def arch_24_area_rectangle_inverse_find_length_or_breadth(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([15, 18, 24, 30])
    b = rng.choice([6, 8, 12])
    a = l * b
    svg = draw_labeled_rect_svg("l = ?", f"{b} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"The area of a rectangular painting is **{a} \\(\\text{{cm}}^2\\)** and its breadth is **{b} cm**.\n\n"
        f"1. Write down the equation relating area, length, and breadth.\n"
        f"2. Calculate the length \\(l\\) of the painting in cm."
    )
    sol = (
        f"**Step 1: Equation**\n"
        f"\\[ A = l \\times b \\implies {a} = l \\times {b} \\]\n\n"
        f"**Step 2: Solve for l**\n"
        f"\\[ l = \\frac{{{a}}}{{{b}}} = {l} \\text{{ cm}} \\]"
    )
    ans = f"1. A = l * b; 2. l = {l} cm"
    return {
        "id": f"g8_area_rect_inv_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "24_area_rectangle_inverse_find_length_or_breadth",
        "learning_objective_id": "math_g8_area_rect_inv",
        "hints": {
            "tier_1": "Length = Area ÷ Breadth.",
            "tier_2": f"{a} ÷ {b}.",
            "tier_3": f"l = {l} cm.",
        },
        "misconception_tags": ["subtracting_breadth_from_area"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 25. Area Right Angled Triangle (WITH SVG)
# ----------------------------------------------------------------------
def arch_25_area_right_angled_triangle(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([6, 8, 10, 12, 14])
    h = rng.choice([5, 7, 9, 11, 15])
    a = (b * h) // 2

    svg = draw_triangle_with_height_svg(f"{b} cm", f"{h} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"A right-angled triangle has perpendicular legs of base \\(b = {b}\\) cm and height \\(h = {h}\\) cm.\n\n"
        f"1. State the formula for the area \\(A\\) of a triangle.\n"
        f"2. Calculate its area in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = \\frac{{1}}{{2}} b \\times h \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A = \\frac{{1}}{{2}} \\times {b} \\times {h} = {b // 2} \\times {h} = {a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. A = 1/2 * b * h; 2. {a} cm²"
    return {
        "id": f"g8_area_rt_tri_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "25_area_right_angled_triangle",
        "learning_objective_id": "math_g8_area_rt_tri",
        "hints": {
            "tier_1": "Area = 1/2 × base × perpendicular height.",
            "tier_2": f"(1/2) × {b} × {h}.",
            "tier_3": f"A = {a} cm².",
        },
        "misconception_tags": ["forgetting_to_halve_the_product_of_base_and_height"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }
