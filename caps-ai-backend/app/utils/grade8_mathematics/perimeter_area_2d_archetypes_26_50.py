"""Grade 8 Mathematics - Perimeter and Area of 2D Shapes Archetypes (26 to 50).
Covers:
  - Area: Acute/obtuse triangles, inverse triangle dimensions, parallelogram, rhombus, kite,
    trapezium, circle area, semicircle, quadrant, unit conversions (length and area),
    composite figures (L-shape, rectangle+triangle, Norman window), shaded areas (square-circle,
    annulus ring), and tiling/flooring cost calculations.
Strictly zero-LLM, deterministic execution parameterized by random.Random.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .perimeter_area_2d_svg import (
    draw_annulus_ring_svg,
    draw_l_shaped_polygon_svg,
    draw_labeled_rect_svg,
    draw_parallelogram_with_height_svg,
    draw_shaded_square_circle_svg,
    draw_trapezium_with_height_svg,
    draw_triangle_with_height_svg,
)


# ----------------------------------------------------------------------
# 26. Area Acute Triangle Interior Perpendicular Height (WITH SVG)
# ----------------------------------------------------------------------
def arch_26_area_acute_triangle_interior_perpendicular_height(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([12, 16, 20, 24])
    h = rng.choice([7, 9, 11, 13, 15])
    a = (b * h) // 2

    svg = draw_triangle_with_height_svg(f"{b} cm", f"{h} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"In the given acute-angled triangle, the base is \\(b = {b}\\) cm and the interior "
        f"perpendicular height is \\(h = {h}\\) cm.\n\n"
        f"1. State the formula for the area of a triangle.\n"
        f"2. Calculate the area of the triangle in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = \\frac{{1}}{{2}} b \\times h \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A = \\frac{{1}}{{2}} \\times {b} \\times {h} = {b // 2} \\times {h} = {a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. A = 1/2 * b * h; 2. {a} cm²"
    return {
        "id": f"g8_area_acute_tri_{rng.randint(100000, 999999)}",
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
        "subskill": "26_area_acute_triangle_interior_perpendicular_height",
        "learning_objective_id": "math_g8_area_acute_tri",
        "hints": {
            "tier_1": "Area is 1/2 × base × height.",
            "tier_2": f"(1/2) × {b} × {h}.",
            "tier_3": f"A = {a} cm².",
        },
        "misconception_tags": ["using_slant_height_instead_of_perpendicular_height"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 27. Area Obtuse Triangle Exterior Perpendicular Height (WITH SVG)
# ----------------------------------------------------------------------
def arch_27_area_obtuse_triangle_exterior_perpendicular_height(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([8, 10, 14, 18])
    h = rng.choice([6, 8, 12, 14])
    a = (b * h) // 2

    svg = draw_triangle_with_height_svg(f"{b} m", f"{h} m", seed=rng.randint(100, 999999))

    prompt = (
        f"In the illustration below, obtuse \\(\\triangle PQR\\) has perpendicular altitude \\(h = {h}\\) m "
        f"dropped externally to baseline \\(PQ = {b}\\) m.\n\n"
        f"1. Confirm whether the standard triangular region formula applies for an external altitude.\n"
        f"2. Determine the area enclosed by \\(\\triangle PQR\\) in square meters."
    )
    sol = (
        f"**1. Yes:** The formula \\(A = \\frac{{1}}{{2}} b \\times h\\) applies to all triangles regardless of whether the altitude falls inside or outside.\n\n"
        f"**2. Calculation:**\n"
        f"\\[ A = \\frac{{1}}{{2}} \\times {b} \\times {h} = {a} \\text{{ m}}^2 \\]"
    )
    ans = f"1. Yes; 2. {a} m²"
    return {
        "id": f"g8_area_obtuse_tri_{rng.randint(100000, 999999)}",
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
        "subskill": "27_area_obtuse_triangle_exterior_perpendicular_height",
        "learning_objective_id": "math_g8_area_obtuse_tri",
        "hints": {
            "tier_1": "Only use the base of the triangle, not the extended distance.",
            "tier_2": f"(1/2) × {b} × {h}.",
            "tier_3": f"A = {a} m².",
        },
        "misconception_tags": ["adding_extension_length_to_triangle_base"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 28. Area Triangle Inverse Find Height (WITH SVG)
# ----------------------------------------------------------------------
def arch_28_area_triangle_inverse_find_height(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([10, 12, 16, 20])
    h = rng.choice([6, 9, 14, 18])
    a = (b * h) // 2

    svg = draw_triangle_with_height_svg(f"{b} cm", "h = ?", seed=rng.randint(100, 999999))

    prompt = (
        f"A triangle has an area of **{a} \\(\\text{{cm}}^2\\)** and a base of \\(b = {b}\\) cm.\n\n"
        f"1. Set up an equation using the triangle area formula.\n"
        f"2. Solve for the perpendicular height \\(h\\) in cm."
    )
    sol = (
        f"**Step 1: Equation**\n"
        f"\\[ \\frac{{1}}{{2}} \\times {b} \\times h = {a} \\]\n"
        f"\\[ {b // 2} h = {a} \\]\n\n"
        f"**Step 2: Solve for h**\n"
        f"\\[ h = \\frac{{{a}}}{{{b // 2}}} = {h} \\text{{ cm}} \\]"
    )
    ans = f"1. (1/2)*{b}*h = {a}; 2. h = {h} cm"
    return {
        "id": f"g8_area_tri_inv_h_{rng.randint(100000, 999999)}",
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
        "subskill": "28_area_triangle_inverse_find_height",
        "learning_objective_id": "math_g8_area_tri_inv_h",
        "hints": {
            "tier_1": "Double the area first, then divide by the base: h = 2A / b.",
            "tier_2": f"2 × {a} = {2 * a}. Divide by {b}.",
            "tier_3": f"h = {h} cm.",
        },
        "misconception_tags": ["forgetting_to_double_the_area_before_dividing"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 29. Area Triangle Inverse Find Base (WITH SVG)
# ----------------------------------------------------------------------
def arch_29_area_triangle_inverse_find_base(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([14, 18, 22, 26])
    h = rng.choice([8, 10, 12, 16])
    a = (b * h) // 2

    svg = draw_triangle_with_height_svg("b = ?", f"{h} m", seed=rng.randint(100, 999999))

    prompt = (
        f"A triangle has an area of **{a} \\(\\text{{m}}^2\\)** and perpendicular height \\(h = {h}\\) m.\n\n"
        f"Calculate the length of the base \\(b\\) in meters."
    )
    sol = (
        f"**Calculation:**\n"
        f"\\[ A = \\frac{{1}}{{2}} b \\times h \\implies {a} = \\frac{{1}}{{2}} b \\times {h} \\]\n"
        f"\\[ {h // 2} b = {a} \\implies b = \\frac{{{a}}}{{{h // 2}}} = {b} \\text{{ m}} \\]"
    )
    ans = f"{b} m"
    return {
        "id": f"g8_area_tri_inv_b_{rng.randint(100000, 999999)}",
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
        "subskill": "29_area_triangle_inverse_find_base",
        "learning_objective_id": "math_g8_area_tri_inv_b",
        "hints": {
            "tier_1": "b = 2A / h.",
            "tier_2": f"2 × {a} = {2 * a}. Divide by {h}.",
            "tier_3": f"b = {b} m.",
        },
        "misconception_tags": ["dividing_area_directly_by_height"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 30. Area Parallelogram Base Times Perpendicular Height (WITH SVG)
# ----------------------------------------------------------------------
def arch_30_area_parallelogram_base_times_perpendicular_height(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([12, 15, 18, 24])
    h = rng.choice([6, 8, 10, 14])
    slant = h + rng.choice([2, 4, 5])
    a = b * h

    svg = draw_parallelogram_with_height_svg(f"{b} cm", f"{h} cm", slant_lbl=f"{slant} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"In the given parallelogram, the base is \\(b = {b}\\) cm, the perpendicular height is \\(h = {h}\\) cm, "
        f"and the slant side is **{slant} cm**.\n\n"
        f"1. State the formula for the area of a parallelogram.\n"
        f"2. Calculate its area in \\(\\text{{cm}}^2\\), explicitly identifying which side is NOT used."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = b \\times h_\\perp \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A = {b} \\times {h} = {a} \\text{{ cm}}^2 \\]\n"
        f"(The slant side of {slant} cm is not used in the area calculation.)"
    )
    ans = f"1. A = b * h; 2. {a} cm² (slant side {slant} cm is not used)"
    return {
        "id": f"g8_area_parm_direct_{rng.randint(100000, 999999)}",
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
        "subskill": "30_area_parallelogram_base_times_perpendicular_height",
        "learning_objective_id": "math_g8_area_parm_direct",
        "hints": {
            "tier_1": "Area is base × perpendicular height. Do NOT use the slant side.",
            "tier_2": f"{b} × {h}.",
            "tier_3": f"A = {a} cm².",
        },
        "misconception_tags": ["multiplying_base_by_slant_height"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 31. Area Parallelogram Inverse Find Base Or Height (WITH SVG)
# ----------------------------------------------------------------------
def arch_31_area_parallelogram_inverse_find_base_or_height(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([15, 20, 25, 30])
    h = rng.choice([8, 12, 16])
    a = b * h

    svg = draw_parallelogram_with_height_svg(f"{b} m", "h = ?", seed=rng.randint(100, 999999))

    prompt = (
        f"A parallelogram has an area of **{a} \\(\\text{{m}}^2\\)** and a base of \\(b = {b}\\) m.\n\n"
        f"Calculate its perpendicular height \\(h\\) in meters."
    )
    sol = (
        f"**Calculation:**\n"
        f"\\[ A = b \\times h \\implies {a} = {b} \\times h \\]\n"
        f"\\[ h = \\frac{{{a}}}{{{b}}} = {h} \\text{{ m}} \\]"
    )
    ans = f"{h} m"
    return {
        "id": f"g8_area_parm_inv_{rng.randint(100000, 999999)}",
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
        "subskill": "31_area_parallelogram_inverse_find_base_or_height",
        "learning_objective_id": "math_g8_area_parm_inv",
        "hints": {
            "tier_1": "h = Area ÷ Base.",
            "tier_2": f"{a} ÷ {b}.",
            "tier_3": f"h = {h} m.",
        },
        "misconception_tags": ["halving_parallelogram_area_as_if_it_were_a_triangle"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 32. Area Rhombus Using Diagonals (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_32_area_rhombus_using_diagonals(rng: random.Random) -> Dict[str, Any]:
    d1 = rng.choice([10, 12, 16, 20])
    d2 = rng.choice([8, 14, 18, 22])
    a = (d1 * d2) // 2

    prompt = (
        f"A rhombus has perpendicular diagonals of lengths \\(d_1 = {d1}\\) cm and \\(d_2 = {d2}\\) cm.\n\n"
        f"1. State the formula for the area of a rhombus in terms of its diagonals.\n"
        f"2. Calculate the area of the rhombus in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = \\frac{{1}}{{2}} d_1 \\times d_2 \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A = \\frac{{1}}{{2}} \\times {d1} \\times {d2} = {d1 // 2} \\times {d2} = {a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. A = 1/2 * d1 * d2; 2. {a} cm²"
    return {
        "id": f"g8_area_rhomb_diag_{rng.randint(100000, 999999)}",
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
        "subskill": "32_area_rhombus_using_diagonals",
        "learning_objective_id": "math_g8_area_rhomb_diag",
        "hints": {
            "tier_1": "Area is half the product of the diagonals.",
            "tier_2": f"(1/2) × {d1} × {d2}.",
            "tier_3": f"A = {a} cm².",
        },
        "misconception_tags": ["forgetting_to_halve_the_product_of_diagonals"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 33. Area Kite Using Diagonals (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_33_area_kite_using_diagonals(rng: random.Random) -> Dict[str, Any]:
    d1 = rng.choice([12, 14, 18, 24])
    d2 = rng.choice([6, 10, 16])
    a = (d1 * d2) // 2

    prompt = (
        f"A decorative kite has intersecting perpendicular diagonals measuring \\(d_1 = {d1}\\) cm and \\(d_2 = {d2}\\) cm.\n\n"
        f"1. State the formula for the area of a kite.\n"
        f"2. Calculate the area of the kite in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = \\frac{{1}}{{2}} d_1 \\times d_2 \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A = \\frac{{1}}{{2}} \\times {d1} \\times {d2} = {a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. A = 1/2 * d1 * d2; 2. {a} cm²"
    return {
        "id": f"g8_area_kite_diag_{rng.randint(100000, 999999)}",
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
        "subskill": "33_area_kite_using_diagonals",
        "learning_objective_id": "math_g8_area_kite_diag",
        "hints": {
            "tier_1": "Like a rhombus, kite area is 1/2 × d1 × d2.",
            "tier_2": f"(1/2) × {d1} × {d2}.",
            "tier_3": f"A = {a} cm².",
        },
        "misconception_tags": ["multiplying_adjacent_sides_instead_of_diagonals"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 34. Area Trapezium Half Sum Parallel Sides Times Height (WITH SVG)
# ----------------------------------------------------------------------
def arch_34_area_trapezium_half_sum_parallel_sides_times_height(rng: random.Random) -> Dict[str, Any]:
    top = rng.choice([8, 10, 12, 14])
    bot = top + rng.choice([6, 8, 10, 12])
    h = rng.choice([6, 8, 10, 12])
    a = ((top + bot) * h) // 2

    svg = draw_trapezium_with_height_svg(f"{top} cm", f"{bot} cm", f"{h} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"In the given trapezium, parallel sides are \\(a = {top}\\) cm and \\(b = {bot}\\) cm, "
        f"and the perpendicular height is \\(h = {h}\\) cm.\n\n"
        f"1. State the formula for the area of a trapezium.\n"
        f"2. Calculate its area in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = \\frac{{1}}{{2}}(a + b) \\times h \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A = \\frac{{1}}{{2}}({top} + {bot}) \\times {h} = \\frac{{1}}{{2}}({top + bot}) \\times {h} = {(top + bot) // 2} \\times {h} = {a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. A = 1/2(a + b)h; 2. {a} cm²"
    return {
        "id": f"g8_area_trap_direct_{rng.randint(100000, 999999)}",
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
        "subskill": "34_area_trapezium_half_sum_parallel_sides_times_height",
        "learning_objective_id": "math_g8_area_trap_direct",
        "hints": {
            "tier_1": "Add parallel sides first: (a + b), divide by 2, then multiply by height.",
            "tier_2": f"({top} + {bot}) / 2 = {(top + bot)/2}. Multiply by {h}.",
            "tier_3": f"A = {a} cm².",
        },
        "misconception_tags": ["multiplying_parallel_sides_instead_of_adding"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 35. Area Trapezium Inverse Find Height (WITH SVG)
# ----------------------------------------------------------------------
def arch_35_area_trapezium_inverse_find_height(rng: random.Random) -> Dict[str, Any]:
    top = rng.choice([6, 10, 12])
    bot = top + rng.choice([8, 10, 14])
    h = rng.choice([5, 7, 9, 11])
    a = ((top + bot) * h) // 2

    svg = draw_trapezium_with_height_svg(f"{top} m", f"{bot} m", "h = ?", seed=rng.randint(100, 999999))

    prompt = (
        f"A trapezium has an area of **{a} \\(\\text{{m}}^2\\)**. "
        f"Its parallel sides measure \\(a = {top}\\) m and \\(b = {bot}\\) m.\n\n"
        f"Calculate the perpendicular height \\(h\\) in meters."
    )
    sum_ab = top + bot
    sol = (
        f"**Calculation:**\n"
        f"\\[ A = \\frac{{1}}{{2}}(a + b)h \\implies {a} = \\frac{{1}}{{2}}({top} + {bot})h \\]\n"
        f"\\[ {a} = {sum_ab // 2} h \\implies h = \\frac{{{a}}}{{{sum_ab // 2}}} = {h} \\text{{ m}} \\]"
    )
    ans = f"{h} m"
    return {
        "id": f"g8_area_trap_inv_h_{rng.randint(100000, 999999)}",
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
        "subskill": "35_area_trapezium_inverse_find_height",
        "learning_objective_id": "math_g8_area_trap_inv_h",
        "hints": {
            "tier_1": "h = 2A / (a + b).",
            "tier_2": f"2 × {a} = {2 * a}. Divide by ({top} + {bot}) = {sum_ab}.",
            "tier_3": f"h = {h} m.",
        },
        "misconception_tags": ["dividing_area_by_sum_of_bases_without_doubling"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 36. Area Circle Given Radius (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_36_area_circle_given_radius(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([7, 14, 21, 28])
    a = 22 * r * r // 7

    prompt = (
        f"A circular grass lawn has a radius of \\(r = {r}\\) m. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. State the formula for the area \\(A\\) of a circle.\n"
        f"2. Calculate the area of the lawn in \\(\\text{{m}}^2\\)."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = \\pi r^2 \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A = \\frac{{22}}{{7}} \\times {r}^2 = \\frac{{22}}{{7}} \\times {r * r} = 22 \\times {r} \\times {r // 7} = {a} \\text{{ m}}^2 \\]"
    )
    ans = f"1. A = pi*r^2; 2. {a} m²"
    return {
        "id": f"g8_area_circ_rad_{rng.randint(100000, 999999)}",
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
        "subskill": "36_area_circle_given_radius",
        "learning_objective_id": "math_g8_area_circ_rad",
        "hints": {
            "tier_1": "Formula is A = πr².",
            "tier_2": f"(22/7) × {r}² = (22/7) × {r * r}.",
            "tier_3": f"A = {a} m².",
        },
        "misconception_tags": ["using_circumference_formula_2_pi_r_instead_of_pi_r_squared"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 37. Area Circle Given Diameter (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_37_area_circle_given_diameter(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([14, 28, 42])
    r = d // 2
    a = 22 * r * r // 7

    prompt = (
        f"A round dining table top has a diameter of \\(d = {d}\\) cm. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. Find the radius \\(r\\) of the tabletop.\n"
        f"2. Calculate the surface area of the tabletop in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Radius**\n"
        f"\\[ r = \\frac{{d}}{{2}} = \\frac{{{d}}}{{2}} = {r} \\text{{ cm}} \\]\n\n"
        f"**Step 2: Area**\n"
        f"\\[ A = \\pi r^2 = \\frac{{22}}{{7}} \\times {r}^2 = {a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. r = {r} cm; 2. {a} cm²"
    return {
        "id": f"g8_area_circ_dia_{rng.randint(100000, 999999)}",
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
        "subskill": "37_area_circle_given_diameter",
        "learning_objective_id": "math_g8_area_circ_dia",
        "hints": {
            "tier_1": "Divide diameter by 2 first to get the radius.",
            "tier_2": f"r = {r} cm, then A = (22/7) × {r}².",
            "tier_3": f"A = {a} cm².",
        },
        "misconception_tags": ["squaring_the_diameter_directly"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 38. Area Circle Inverse Find Radius (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_38_area_circle_inverse_find_radius(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([7, 14, 21])
    a = 22 * r * r // 7

    prompt = (
        f"A circular carpet covers an area of **{a} \\(\\text{{m}}^2\\)**. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. Set up an equation using \\(A = \\pi r^2\\).\n"
        f"2. Calculate the radius \\(r\\) of the carpet in meters."
    )
    sol = (
        f"**Step 1: Equation**\n"
        f"\\[ \\frac{{22}}{{7}} r^2 = {a} \\]\n\n"
        f"**Step 2: Solve for r**\n"
        f"\\[ r^2 = \\frac{{{a} \\times 7}}{{22}} = {r * r} \\]\n"
        f"\\[ r = \\sqrt{{{r * r}}} = {r} \\text{{ m}} \\]"
    )
    ans = f"1. (22/7)*r^2 = {a}; 2. r = {r} m"
    return {
        "id": f"g8_area_circ_inv_{rng.randint(100000, 999999)}",
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
        "subskill": "38_area_circle_inverse_find_radius",
        "learning_objective_id": "math_g8_area_circ_inv",
        "hints": {
            "tier_1": "r² = A ÷ π, then take square root.",
            "tier_2": f"r² = ({a} × 7) / 22 = {r * r}.",
            "tier_3": f"r = {r} m.",
        },
        "misconception_tags": ["forgetting_to_take_square_root_after_dividing_by_pi"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 39. Area Semicircle Half Pi R Squared (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_39_area_semicircle_half_pi_r_squared(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([7, 14, 21])
    full_a = 22 * r * r // 7
    semi_a = full_a // 2

    prompt = (
        f"A semicircular window pane has a radius of \\(r = {r}\\) cm. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. State the formula for the area of a semicircle.\n"
        f"2. Calculate its area in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = \\frac{{1}}{{2}} \\pi r^2 \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A = \\frac{{1}}{{2}} \\times \\frac{{22}}{{7}} \\times {r}^2 = \\frac{{1}}{{2}} \\times {full_a} = {semi_a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. A = 1/2 * pi * r^2; 2. {semi_a} cm²"
    return {
        "id": f"g8_area_semicirc_{rng.randint(100000, 999999)}",
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
        "subskill": "39_area_semicircle_half_pi_r_squared",
        "learning_objective_id": "math_g8_area_semicirc",
        "hints": {
            "tier_1": "Calculate the full circle area, then divide by 2.",
            "tier_2": f"Full area = {full_a} cm². Divide by 2.",
            "tier_3": f"A = {semi_a} cm².",
        },
        "misconception_tags": ["dividing_radius_by_2_instead_of_halving_area"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 40. Area Quadrant Quarter Pi R Squared (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_40_area_quadrant_quarter_pi_r_squared(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([14, 28])
    full_a = 22 * r * r // 7
    quad_a = full_a // 4

    prompt = (
        f"A quadrant (one quarter of a circle) has a radius of \\(r = {r}\\) m. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"Calculate the area of the quadrant in \\(\\text{{m}}^2\\)."
    )
    sol = (
        f"**Calculation:**\n"
        f"\\[ A = \\frac{{1}}{{4}} \\pi r^2 = \\frac{{1}}{{4}} \\times \\frac{{22}}{{7}} \\times {r}^2 = \\frac{{{full_a}}}{{4}} = {quad_a} \\text{{ m}}^2 \\]"
    )
    ans = f"{quad_a} m²"
    return {
        "id": f"g8_area_quadrant_{rng.randint(100000, 999999)}",
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
        "subskill": "40_area_quadrant_quarter_pi_r_squared",
        "learning_objective_id": "math_g8_area_quadrant",
        "hints": {
            "tier_1": "Divide full circle area by 4.",
            "tier_2": f"{full_a} ÷ 4.",
            "tier_3": f"A = {quad_a} m².",
        },
        "misconception_tags": ["multiplying_by_4_instead_of_dividing"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 41. Unit Conversion Length Mm Cm M Km (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_41_unit_conversion_length_mm_cm_m_km(rng: random.Random) -> Dict[str, Any]:
    val_m = rng.choice([2.5, 4.2, 7.5, 12.0])
    val_cm = int(val_m * 100)
    val_mm = val_cm * 10

    prompt = (
        f"A straight metal rod has a length of **{val_m} m**.\n\n"
        f"1. Convert this length to centimeters (cm).\n"
        f"2. Convert this length to millimeters (mm)."
    )
    sol = (
        f"**1. Meters to cm:** Multiply by 100:\n"
        f"\\[ {val_m} \\times 100 = {val_cm} \\text{{ cm}} \\]\n\n"
        f"**2. Meters to mm:** Multiply by 1 000 (or cm by 10):\n"
        f"\\[ {val_cm} \\times 10 = {val_mm} \\text{{ mm}} \\]"
    )
    ans = f"1. {val_cm} cm; 2. {val_mm} mm"
    return {
        "id": f"g8_conv_length_{rng.randint(100000, 999999)}",
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
        "subskill": "41_unit_conversion_length_mm_cm_m_km",
        "learning_objective_id": "math_g8_conv_length",
        "hints": {
            "tier_1": "1 m = 100 cm = 1 000 mm.",
            "tier_2": f"{val_m} × 100 = {val_cm} cm.",
            "tier_3": f"{val_cm} cm and {val_mm} mm.",
        },
        "misconception_tags": ["multiplying_by_10_instead_of_100_for_meters_to_cm"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 42. Unit Conversion Area Cm2 To Mm2 (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_42_unit_conversion_area_cm2_to_mm2(rng: random.Random) -> Dict[str, Any]:
    cm2 = rng.choice([3, 5, 8, 12, 15])
    mm2 = cm2 * 100

    prompt = (
        f"Recall that \\(1\\text{{ cm}} = 10\\text{{ mm}}\\).\n\n"
        f"1. Explain why \\(1\\text{{ cm}}^2 = 100\\text{{ mm}}^2\\).\n"
        f"2. Convert **{cm2} \\(\\text{{cm}}^2\\)** into \\(\\text{{mm}}^2\\)."
    )
    sol = (
        f"**1. Explanation:** A square of side \\(1\\text{{ cm}}\\) has side length \\(10\\text{{ mm}}\\). "
        f"Its area is \\(10\\text{{ mm}} \\times 10\\text{{ mm}} = 100\\text{{ mm}}^2\\).\n\n"
        f"**2. Conversion:**\n"
        f"\\[ {cm2} \\times 100 = {mm2} \\text{{ mm}}^2 \\]"
    )
    ans = f"1. 10 mm * 10 mm = 100 mm²; 2. {mm2} mm²"
    return {
        "id": f"g8_conv_cm2_mm2_{rng.randint(100000, 999999)}",
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
        "subskill": "42_unit_conversion_area_cm2_to_mm2",
        "learning_objective_id": "math_g8_conv_cm2_mm2",
        "hints": {
            "tier_1": "Multiply by 10² = 100.",
            "tier_2": f"{cm2} × 100.",
            "tier_3": f"{mm2} mm².",
        },
        "misconception_tags": ["multiplying_by_10_instead_of_100_for_area"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 43. Unit Conversion Area M2 To Cm2 (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_43_unit_conversion_area_m2_to_cm2(rng: random.Random) -> Dict[str, Any]:
    m2 = rng.choice([2, 4, 6, 8])
    cm2 = m2 * 10000

    prompt = (
        f"Recall that \\(1\\text{{ m}} = 100\\text{{ cm}}\\).\n\n"
        f"1. Explain why \\(1\\text{{ m}}^2 = 10\\,000\\text{{ cm}}^2\\).\n"
        f"2. Convert **{m2} \\(\\text{{m}}^2\\)** into \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**1. Explanation:** \\(1\\text{{ m}}^2 = 100\\text{{ cm}} \\times 100\\text{{ cm}} = 10\\,000\\text{{ cm}}^2\\).\n\n"
        f"**2. Conversion:**\n"
        f"\\[ {m2} \\times 10\\,000 = {cm2} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. 100 cm * 100 cm = 10 000 cm²; 2. {cm2} cm²"
    return {
        "id": f"g8_conv_m2_cm2_{rng.randint(100000, 999999)}",
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
        "subskill": "43_unit_conversion_area_m2_to_cm2",
        "learning_objective_id": "math_g8_conv_m2_cm2",
        "hints": {
            "tier_1": "Multiply by 100² = 10 000.",
            "tier_2": f"{m2} × 10 000.",
            "tier_3": f"{cm2} cm².",
        },
        "misconception_tags": ["multiplying_by_100_instead_of_10000"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 44. Unit Conversion Area Hectares To M2 (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_44_unit_conversion_area_hectares_to_m2(rng: random.Random) -> Dict[str, Any]:
    ha = rng.choice([1.5, 2.0, 3.5, 5.0])
    m2 = int(ha * 10000)

    prompt = (
        f"In South African agriculture and land measurement, \\(1\\text{{ hectare (ha)}} = 10\\,000\\text{{ m}}^2\\).\n\n"
        f"A commercial farm plot has an area of **{ha} hectares**.\n\n"
        f"Calculate the area of the plot in \\(\\text{{m}}^2\\)."
    )
    sol = (
        f"**Calculation:**\n"
        f"\\[ \\text{{Area}} = {ha} \\times 10\\,000 = {m2} \\text{{ m}}^2 \\]"
    )
    ans = f"{m2} m²"
    return {
        "id": f"g8_conv_ha_m2_{rng.randint(100000, 999999)}",
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
        "subskill": "44_unit_conversion_area_hectares_to_m2",
        "learning_objective_id": "math_g8_conv_ha_m2",
        "hints": {
            "tier_1": "1 hectare = 10 000 m².",
            "tier_2": f"{ha} × 10 000.",
            "tier_3": f"{m2} m².",
        },
        "misconception_tags": ["using_1000_instead_of_10000_for_hectares"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 45. Composite Area L-Shaped Partition Two Rectangles (WITH SVG)
# ----------------------------------------------------------------------
def arch_45_composite_area_l_shaped_partition_two_rectangles(rng: random.Random) -> Dict[str, Any]:
    w_tot = rng.choice([12, 16, 20])
    h_tot = rng.choice([10, 14, 18])
    w_top = rng.choice([4, 6, 8])
    h_top = rng.choice([4, 5, 6])

    # Decompose into vertical left rectangle + right bottom rectangle
    # Left rect: w_top x h_tot
    # Right rect: (w_tot - w_top) x (h_tot - h_top)
    a1 = w_top * h_tot
    a2 = (w_tot - w_top) * (h_tot - h_top)
    tot_a = a1 + a2

    svg = draw_l_shaped_polygon_svg(
        f"{w_tot} m",
        f"{h_tot} m",
        f"{w_top} m",
        f"{h_tot - h_top} m",
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In the given L-shaped floor plan, total width is **{w_tot} m** and total height is **{h_tot} m**.\n"
        f"The top narrower section has width **{w_top} m** and height **{h_top} m**.\n\n"
        f"1. Explain how to split this composite shape into two simpler non-overlapping rectangles.\n"
        f"2. Calculate the total area of the floor in \\(\\text{{m}}^2\\)."
    )
    sol = (
        f"**Step 1: Partitioning**\n"
        f"Split vertically into Rectangle 1 (left) measuring \\({w_top} \\times {h_tot}\\) m, "
        f"and Rectangle 2 (right) measuring \\({w_tot - w_top} \\times {h_tot - h_top}\\) m.\n\n"
        f"**Step 2: Total area**\n"
        f"\\[ A_1 = {w_top} \\times {h_tot} = {a1} \\text{{ m}}^2 \\]\n"
        f"\\[ A_2 = {w_tot - w_top} \\times {h_tot - h_top} = {a2} \\text{{ m}}^2 \\]\n"
        f"\\[ A_{{\\text{{total}}}} = {a1} + {a2} = {tot_a} \\text{{ m}}^2 \\]"
    )
    ans = f"1. split into two rectangles; 2. {tot_a} m²"
    return {
        "id": f"g8_area_l_shape_{rng.randint(100000, 999999)}",
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
        "subskill": "45_composite_area_l_shaped_partition_two_rectangles",
        "learning_objective_id": "math_g8_area_l_shape",
        "hints": {
            "tier_1": "Divide into two rectangles, find each area, and add them together.",
            "tier_2": f"Area 1 = {a1} m², Area 2 = {a2} m².",
            "tier_3": f"Total area = {tot_a} m².",
        },
        "misconception_tags": ["multiplying_outer_dimensions_directly"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 46. Composite Area Rectangle Plus Triangle Gable End (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_46_composite_area_rectangle_plus_triangle_gable_end(rng: random.Random) -> Dict[str, Any]:
    w = rng.choice([8, 10, 12])
    h_wall = rng.choice([4, 5, 6])
    h_roof = rng.choice([3, 4, 5])

    a_rect = w * h_wall
    a_tri = (w * h_roof) // 2
    tot_a = a_rect + a_tri

    prompt = (
        f"A gable end wall of a building consists of a rectangular wall surmounted by a triangular roof section:\n"
        f"- The rectangular wall has width **{w} m** and height **{h_wall} m**.\n"
        f"- The triangular section shares the base of **{w} m** and has perpendicular height **{h_roof} m**.\n\n"
        f"1. Calculate the area of the rectangular wall.\n"
        f"2. Calculate the area of the triangular roof section.\n"
        f"3. Calculate the total wall area in \\(\\text{{m}}^2\\)."
    )
    sol = (
        f"**Step 1: Rectangle area**\n"
        f"\\[ A_{{\\text{{rect}}}} = {w} \\times {h_wall} = {a_rect} \\text{{ m}}^2 \\]\n\n"
        f"**Step 2: Triangle area**\n"
        f"\\[ A_{{\\text{{tri}}}} = \\frac{{1}}{{2}} \\times {w} \\times {h_roof} = {a_tri} \\text{{ m}}^2 \\]\n\n"
        f"**Step 3: Total area**\n"
        f"\\[ A_{{\\text{{total}}}} = {a_rect} + {a_tri} = {tot_a} \\text{{ m}}^2 \\]"
    )
    ans = f"1. {a_rect} m²; 2. {a_tri} m²; 3. {tot_a} m²"
    return {
        "id": f"g8_area_gable_{rng.randint(100000, 999999)}",
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
        "subskill": "46_composite_area_rectangle_plus_triangle_gable_end",
        "learning_objective_id": "math_g8_area_gable",
        "hints": {
            "tier_1": "Add area of rectangle (w × h_wall) to area of triangle (1/2 × w × h_roof).",
            "tier_2": f"{a_rect} + {a_tri}.",
            "tier_3": f"Total area = {tot_a} m².",
        },
        "misconception_tags": ["forgetting_to_halve_the_triangular_section_area"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 47. Composite Area Rectangle With Semicircle Attached (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_47_composite_area_rectangle_with_semicircle_attached(rng: random.Random) -> Dict[str, Any]:
    w = rng.choice([14, 28])
    h = rng.choice([10, 15, 20])
    r = w // 2

    a_rect = w * h
    a_semi = (22 * r * r // 7) // 2
    tot_a = a_rect + a_semi

    prompt = (
        f"A window consists of a rectangular pane topped by a semicircular arch. (Take \\(\\pi = \\frac{{22}}{{7}}\\))\n"
        f"- The rectangle has width **{w} cm** and height **{h} cm**.\n"
        f"- The semicircle has diameter \\(d = {w}\\) cm.\n\n"
        f"1. Calculate the area of the rectangular portion.\n"
        f"2. Calculate the area of the semicircular arch.\n"
        f"3. Calculate the total area of the window in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Rectangle area**\n"
        f"\\[ A_{{\\text{{rect}}}} = {w} \\times {h} = {a_rect} \\text{{ cm}}^2 \\]\n\n"
        f"**Step 2: Semicircle area**\n"
        f"Radius \\(r = {w} / 2 = {r}\\) cm.\n"
        f"\\[ A_{{\\text{{semi}}}} = \\frac{{1}}{{2}} \\times \\frac{{22}}{{7}} \\times {r}^2 = {a_semi} \\text{{ cm}}^2 \\]\n\n"
        f"**Step 3: Total area**\n"
        f"\\[ A_{{\\text{{total}}}} = {a_rect} + {a_semi} = {tot_a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. {a_rect} cm²; 2. {a_semi} cm²; 3. {tot_a} cm²"
    return {
        "id": f"g8_area_norman_win_{rng.randint(100000, 999999)}",
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
        "subskill": "47_composite_area_rectangle_with_semicircle_attached",
        "learning_objective_id": "math_g8_area_norman_win",
        "hints": {
            "tier_1": "Add the rectangle area to the half-circle area.",
            "tier_2": f"Radius = {r} cm. Semicircle area = {a_semi} cm².",
            "tier_3": f"Total area = {tot_a} cm².",
        },
        "misconception_tags": ["using_full_circle_area_instead_of_semicircle"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 48. Shaded Area Square With Inscribed Circle (WITH SVG)
# ----------------------------------------------------------------------
def arch_48_shaded_area_square_with_inscribed_circle(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([7, 14, 21])
    s = 2 * r
    a_sq = s * s
    a_circ = 22 * r * r // 7
    shaded = a_sq - a_circ

    svg = draw_shaded_square_circle_svg(f"{s} cm", f"{r} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"In the given figure, a circle of radius \\(r = {r}\\) cm is inscribed inside a square of side \\(s = {s}\\) cm. "
        f"(Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. Calculate the area of the outer square.\n"
        f"2. Calculate the area of the unshaded inner circle.\n"
        f"3. Calculate the shaded area between the square and the circle in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Square area**\n"
        f"\\[ A_{{\\text{{square}}}} = {s}^2 = {a_sq} \\text{{ cm}}^2 \\]\n\n"
        f"**Step 2: Circle area**\n"
        f"\\[ A_{{\\text{{circle}}}} = \\frac{{22}}{{7}} \\times {r}^2 = {a_circ} \\text{{ cm}}^2 \\]\n\n"
        f"**Step 3: Shaded area**\n"
        f"\\[ A_{{\\text{{shaded}}}} = {a_sq} - {a_circ} = {shaded} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. {a_sq} cm²; 2. {a_circ} cm²; 3. {shaded} cm²"
    return {
        "id": f"g8_shaded_sq_circ_{rng.randint(100000, 999999)}",
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
        "subskill": "48_shaded_area_square_with_inscribed_circle",
        "learning_objective_id": "math_g8_shaded_sq_circ",
        "hints": {
            "tier_1": "Shaded area = Outer Area - Inner Area.",
            "tier_2": f"Square = {a_sq} cm², Circle = {a_circ} cm².",
            "tier_3": f"Shaded = {shaded} cm².",
        },
        "misconception_tags": ["adding_areas_instead_of_subtracting_for_shaded_region"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 49. Shaded Area Annulus Ring Between Concentric Circles (WITH SVG)
# ----------------------------------------------------------------------
def arch_49_shaded_area_annulus_ring_between_concentric_circles(rng: random.Random) -> Dict[str, Any]:
    R = rng.choice([14, 21, 28])
    r = R - 7
    a_big = 22 * R * R // 7
    a_small = 22 * r * r // 7
    ring_a = a_big - a_small

    svg = draw_annulus_ring_svg(f"{R} cm", f"{r} cm", seed=rng.randint(100, 999999))

    prompt = (
        f"In the given figure, two concentric circles have radii \\(R = {R}\\) cm and \\(r = {r}\\) cm. "
        f"(Take \\(\\pi = \\frac{{22}}{{7}}\\))\n\n"
        f"1. State the formula for the area of the shaded ring (annulus) between them.\n"
        f"2. Calculate the area of the shaded ring in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ A = \\pi R^2 - \\pi r^2 = \\pi(R^2 - r^2) \\]\n\n"
        f"**Step 2: Calculation**\n"
        f"\\[ A_{{\\text{{outer}}}} = \\frac{{22}}{{7}} \\times {R}^2 = {a_big} \\text{{ cm}}^2 \\]\n"
        f"\\[ A_{{\\text{{inner}}}} = \\frac{{22}}{{7}} \\times {r}^2 = {a_small} \\text{{ cm}}^2 \\]\n"
        f"\\[ A_{{\\text{{ring}}}} = {a_big} - {a_small} = {ring_a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. A = pi(R^2 - r^2); 2. {ring_a} cm²"
    return {
        "id": f"g8_shaded_annulus_{rng.randint(100000, 999999)}",
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
        "subskill": "49_shaded_area_annulus_ring_between_concentric_circles",
        "learning_objective_id": "math_g8_shaded_annulus",
        "hints": {
            "tier_1": "Subtract inner circle area from outer circle area.",
            "tier_2": f"Outer = {a_big} cm², Inner = {a_small} cm².",
            "tier_3": f"Ring area = {ring_a} cm².",
        },
        "misconception_tags": ["subtracting_radii_first_and_then_squaring"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 50. Area Word Problem Flooring Tiling Cost Calculation (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_50_area_word_problem_flooring_tiling_cost_calculation(rng: random.Random) -> Dict[str, Any]:
    l = rng.choice([6, 8, 10])
    b = rng.choice([4, 5, 6])
    floor_a = l * b
    rate = rng.choice([150, 180, 220, 250])  # Rands per m^2
    tot_cost = floor_a * rate

    prompt = (
        f"A homeowner wants to retile a rectangular living room floor measuring **{l} m** by **{b} m**.\n\n"
        f"1. Calculate the total floor area to be tiled in \\(\\text{{m}}^2\\).\n"
        f"2. If tiling and labour costs **R{rate} per square meter**, calculate the total cost in Rands."
    )
    sol = (
        f"**Step 1: Floor area**\n"
        f"\\[ A = l \\times b = {l} \\times {b} = {floor_a} \\text{{ m}}^2 \\]\n\n"
        f"**Step 2: Total cost**\n"
        f"\\[ \\text{{Total Cost}} = {floor_a} \\times {rate} = \\text{{R}}{tot_cost} \\]"
    )
    ans = f"1. {floor_a} m²; 2. R{tot_cost}"
    return {
        "id": f"g8_area_tiling_cost_{rng.randint(100000, 999999)}",
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
        "subskill": "50_area_word_problem_flooring_tiling_cost_calculation",
        "learning_objective_id": "math_g8_area_tiling_cost",
        "hints": {
            "tier_1": "Find the floor area first: l × b.",
            "tier_2": f"Area = {floor_a} m².",
            "tier_3": f"Cost = {floor_a} × R{rate} = R{tot_cost}.",
        },
        "misconception_tags": ["using_perimeter_instead_of_area_for_tiling_cost"],
        "diagram_spec": None,
    }
