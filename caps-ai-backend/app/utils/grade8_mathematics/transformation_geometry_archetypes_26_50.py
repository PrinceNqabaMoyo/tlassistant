"""Grade 8 Mathematics — Transformation Geometry Archetypes 26 to 50.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 3/01. Transformation geometry.md

Archetypes covering:
  - 26 to 30: Rotation angle/direction identification, invariant center, quadrants, order and angle of rotational symmetry.
  - 31 to 40: Enlargements and reductions (dilations), scale factor k, triangle dilation, perimeter ratio (k), area ratio (k²), similarity.
  - 41 to 50: Composite transformations, rule identification, congruence vs similarity, isometries, error analysis, tessellations, applications.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Tuple

from .transformation_geometry_svg import (
    draw_transformation_grid_svg,
)


# ----------------------------------------------------------------------
# 26. Identify Rotation Angle and Direction From Coordinates (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_26_rotation_identify_angle_and_direction_from_coordinates(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["90_cw", "90_ccw", "180"])
    x, y = rng.choice([2, 3]), rng.choice([4, 5])
    if choice == "90_cw":
        img = (y, -x)
        desc = "90° clockwise about the origin"
    elif choice == "90_ccw":
        img = (-y, x)
        desc = "90° counter-clockwise about the origin"
    else:
        img = (-x, -y)
        desc = "180° rotation (half-turn) about the origin"

    prompt = (
        f"Point \\(P({x}; {y})\\) is rotated about the origin \\((0; 0)\\) to position \\(P'({img[0]}; {img[1]})\\).\n\n"
        f"1. Identify the angle and direction of this rotation.\n"
        f"2. State the general coordinate rule that verifies your choice."
    )
    rule = "(x; y) -> (y; -x)" if choice == "90_cw" else ("(x; y) -> (-y; x)" if choice == "90_ccw" else "(x; y) -> (-x; -y)")
    sol = (
        f"**1. Rotation angle and direction:** **{desc}**.\n\n"
        f"**2. Coordinate Rule:** \\({rule}\\). Substituting \\(({x}; {y})\\) results in \\(({img[0]}; {img[1]})\\)."
    )
    ans = f"1. {desc}; 2. {rule}"
    return {
        "id": f"g8_trans_id_rot_{rng.randint(100000, 999999)}",
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
        "subskill": "26_rotation_identify_angle_and_direction_from_coordinates",
        "learning_objective_id": "math_g8_trans_id_rot",
        "hints": {
            "tier_1": "Compare the coordinates of P and P': did they swap? which signs changed?",
            "tier_2": f"Here ({x}; {y}) became ({img[0]}; {img[1]}).",
            "tier_3": f"{desc}; rule: {rule}.",
        },
        "misconception_tags": ["confusing_clockwise_and_counter_clockwise_signs"],
    }


# ----------------------------------------------------------------------
# 27. Rotation Invariant Center Point (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_27_rotation_invariant_center_point(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([90, 180, 270])
    prompt = (
        f"A coordinate plane is rotated by **{angle}°** about the origin \\((0; 0)\\).\n\n"
        f"1. What are the coordinates of the invariant point that remains stationary under this rotation?\n"
        f"2. Explain why this point does not change position."
    )
    sol = (
        f"**1. Invariant point:** The origin **\\((0; 0)\\)**.\n\n"
        f"**2. Explanation:** The origin is the center of rotation. The distance from the center of rotation "
        f"to itself is zero, so rotating about this pivot leaves \\((0; 0)\\) strictly invariant (stationary)."
    )
    ans = "1. (0; 0); 2. the center of rotation has distance 0 from pivot and remains fixed"
    return {
        "id": f"g8_trans_rot_pivot_{rng.randint(100000, 999999)}",
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
        "subskill": "27_rotation_invariant_center_point",
        "learning_objective_id": "math_g8_trans_rot_pivot",
        "hints": {
            "tier_1": "The pivot point of a rotation never changes position.",
            "tier_2": "The center of rotation is the origin (0; 0).",
            "tier_3": "(0; 0); it is the center of rotation.",
        },
        "misconception_tags": ["thinking_no_points_are_invariant_under_rotation"],
    }


# ----------------------------------------------------------------------
# 28. Rotation Quadrant Location After Turn (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_28_rotation_quadrant_location_after_turn(rng: random.Random) -> Dict[str, Any]:
    q_start = 1
    px, py = rng.choice([2, 3]), rng.choice([4, 5])  # Quadrant I: (+, +)
    rotation_type = rng.choice(["90_cw", "90_ccw", "180"])

    if rotation_type == "90_cw":
        # (x, y) -> (y, -x) = (+, -) => Quadrant IV
        target_q = "Quadrant IV"
        deg_str = "90° clockwise"
    elif rotation_type == "90_ccw":
        # (x, y) -> (-y, x) = (-, +) => Quadrant II
        target_q = "Quadrant II"
        deg_str = "90° counter-clockwise"
    else:
        # (x, y) -> (-x, -y) = (-, -) => Quadrant III
        target_q = "Quadrant III"
        deg_str = "180°"

    prompt = (
        f"Point \\(A({px}; {py})\\) starts in Quadrant I.\n"
        f"The point is rotated **{deg_str}** about the origin \\((0; 0)\\).\n\n"
        f"1. In which quadrant does point \\(A'\\) lie?\n"
        f"2. State the signs (positive or negative) of the x-coordinate and y-coordinate in this destination quadrant."
    )
    signs = "(+, -)" if target_q == "Quadrant IV" else ("(-, +)" if target_q == "Quadrant II" else "(-, -)")
    sol = (
        f"**1. Destination Quadrant:** **{target_q}**.\n\n"
        f"**2. Coordinate Signs:** In {target_q}, coordinates have signs **{signs}** "
        f"({'x is positive, y is negative' if target_q == 'Quadrant IV' else ('x is negative, y is positive' if target_q == 'Quadrant II' else 'both x and y are negative')})."
    )
    ans = f"1. {target_q}; 2. {signs}"
    return {
        "id": f"g8_trans_rot_quad_{rng.randint(100000, 999999)}",
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
        "subskill": "28_rotation_quadrant_location_after_turn",
        "learning_objective_id": "math_g8_trans_rot_quad",
        "hints": {
            "tier_1": "Moving 90° clockwise turns from Quadrant I into Quadrant IV.",
            "tier_2": "Recall signs: Quad I (+, +), Quad II (-, +), Quad III (-, -), Quad IV (+, -).",
            "tier_3": f"{target_q}; {signs}.",
        },
        "misconception_tags": ["reversing_quadrant_numbering_direction"],
    }


# ----------------------------------------------------------------------
# 29. Order of Rotational Symmetry in 2D Shapes (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_29_rotation_order_of_rotational_symmetry_2d_shapes(rng: random.Random) -> Dict[str, Any]:
    shape, order = rng.choice([
        ("square", 4),
        ("rectangle", 2),
        ("equilateral triangle", 3),
        ("regular hexagon", 6),
        ("parallelogram", 2),
    ])

    prompt = (
        f"Consider a standard **{shape}**:\n\n"
        f"1. Define the term **order of rotational symmetry**.\n"
        f"2. What is the order of rotational symmetry of a {shape} during a complete 360° turn about its center?"
    )
    sol = (
        f"**1. Definition:** The order of rotational symmetry is the number of times a shape fits exactly onto itself "
        f"during one complete rotation of \\(360^\\circ\\) about its center.\n\n"
        f"**2. Order for {shape}:** Exactly **{order}**."
    )
    ans = f"1. number of times shape fits onto itself in 360° rotation; 2. {order}"
    return {
        "id": f"g8_trans_rot_order_{rng.randint(100000, 999999)}",
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
        "subskill": "29_rotation_order_of_rotational_symmetry_2d_shapes",
        "learning_objective_id": "math_g8_trans_rot_order",
        "hints": {
            "tier_1": "Count how many times the shape looks identical within a full 360° turn.",
            "tier_2": f"For a regular polygon with n sides, order is n. For a rectangle/parallelogram, order is 2.",
            "tier_3": f"Order is {order}.",
        },
        "misconception_tags": ["confusing_order_of_rotational_symmetry_with_lines_of_symmetry"],
    }


# ----------------------------------------------------------------------
# 30. Angle of Rotational Symmetry Calculation (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_30_rotation_angle_of_rotational_symmetry_calculation(rng: random.Random) -> Dict[str, Any]:
    n, name = rng.choice([(3, "equilateral triangle"), (4, "square"), (5, "regular pentagon"), (6, "regular hexagon"), (8, "regular octagon")])
    angle = 360 // n

    prompt = (
        f"A **{name}** has an order of rotational symmetry equal to \\({n}\\).\n\n"
        f"1. State the formula for calculating the minimum angle of rotational symmetry.\n"
        f"2. Calculate the smallest angle in degrees through which a {name} must be rotated to coincide with its original position."
    )
    sol = (
        f"**1. Formula:**\n"
        f"\\[ \\text{{Angle of rotational symmetry}} = \\frac{{360^\\circ}}{{\\text{{Order of rotational symmetry}}}} = \\frac{{360^\\circ}}{{n}} \\]\n\n"
        f"**2. Calculation for {name}:**\n"
        f"\\[ \\frac{{360^\\circ}}{{{n}}} = {angle}^\\circ \\]"
    )
    ans = f"1. 360° / order; 2. {angle}°"
    return {
        "id": f"g8_trans_rot_angle_{rng.randint(100000, 999999)}",
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
        "subskill": "30_rotation_angle_of_rotational_symmetry_calculation",
        "learning_objective_id": "math_g8_trans_rot_angle",
        "hints": {
            "tier_1": "Divide 360° by the order of rotational symmetry.",
            "tier_2": f"360° ÷ {n}.",
            "tier_3": f"{angle}°.",
        },
        "misconception_tags": ["dividing_180_instead_of_360_for_rotational_angle"],
    }


# ----------------------------------------------------------------------
# 31. Enlargement Scale Factor Coordinates Origin (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_31_enlargement_scale_factor_coordinates_origin(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([1, 2])
    py = rng.choice([1, 2])
    k = rng.choice([2, 3])
    ex, ey = px * k, py * k

    svg = draw_transformation_grid_svg([(px, py)], [(ex, ey)], "P", "P'", seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(P({px}; {py})\\) undergoes an enlargement with a scale factor of **\\(k = {k}\\)** centered at the origin \\((0; 0)\\).\n\n"
        f"1. Write down the algebraic coordinate rule for an enlargement by scale factor \\(k\\): \\((x; y) \\to (\\dots; \\dots)\\).\n"
        f"2. Calculate the coordinates of image point \\(P'\\)."
    )
    sol = (
        f"**1. Enlargement Rule:** \\((x; y) \\to (kx; ky)\\). Both coordinates are multiplied by the scale factor \\(k\\).\n\n"
        f"**2. Coordinates of P':**\n"
        f"\\[ P({px}; {py}) \\to P'({k} \\times {px}; {k} \\times {py}) = P'({ex}; {ey}) \\]"
    )
    ans = f"1. (kx; ky); 2. ({ex}; {ey})"
    return {
        "id": f"g8_trans_enl_coord_{rng.randint(100000, 999999)}",
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
        "subskill": "31_enlargement_scale_factor_coordinates_origin",
        "learning_objective_id": "math_g8_trans_enl_coord",
        "hints": {
            "tier_1": f"Multiply both the x-coordinate and the y-coordinate by {k}.",
            "tier_2": f"x' = {k} * {px}, y' = {k} * {py}.",
            "tier_3": f"P'({ex}; {ey}).",
        },
        "misconception_tags": ["adding_scale_factor_instead_of_multiplying"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 32. Reduction Scale Factor Coordinates Origin (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_32_reduction_scale_factor_coordinates_origin(rng: random.Random) -> Dict[str, Any]:
    ex = rng.choice([2, 4, 6])
    ey = rng.choice([2, 4])
    rx, ry = ex // 2, ey // 2

    svg = draw_transformation_grid_svg([(ex, ey)], [(rx, ry)], "Q", "Q'", seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(Q({ex}; {ey})\\) undergoes a reduction with scale factor **\\(k = \\frac{{1}}{{2}}\\) (or 0.5)** "
        f"with the center of reduction at origin \\((0; 0)\\).\n\n"
        f"1. Explain what happens to the distance from the origin when \\(k < 1\\).\n"
        f"2. Calculate the coordinates of image point \\(Q'\\)."
    )
    sol = (
        f"**1. Distance reduction:** When \\(0 < k < 1\\), the distance from the origin to the image is reduced "
        f"to half its original length, bringing the point closer to the origin.\n\n"
        f"**2. Coordinates of Q':**\n"
        f"\\[ Q'\\left(\\frac{{1}}{{2}} \\times {ex}; \\frac{{1}}{{2}} \\times {ey}\\right) = Q'({rx}; {ry}) \\]"
    )
    ans = f"1. distance from origin is halved / point moves closer; 2. ({rx}; {ry})"
    return {
        "id": f"g8_trans_red_coord_{rng.randint(100000, 999999)}",
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
        "subskill": "32_reduction_scale_factor_coordinates_origin",
        "learning_objective_id": "math_g8_trans_red_coord",
        "hints": {
            "tier_1": "Multiply each coordinate by 1/2 (divide each by 2).",
            "tier_2": f"{ex} / 2 = {rx}; {ey} / 2 = {ry}.",
            "tier_3": f"Q'({rx}; {ry}).",
        },
        "misconception_tags": ["subtracting_half_instead_of_multiplying_by_half"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 33. Enlargement Triangle Vertices Scale Factor 2 (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_33_enlargement_triangle_vertices_scale_factor_2(rng: random.Random) -> Dict[str, Any]:
    dx = rng.choice([0, 1])
    orig = [(1 + dx, 1), (2 + dx, 1), (1 + dx, 3)]
    trans = [(2 * x, 2 * y) for x, y in orig]
    svg = draw_transformation_grid_svg(orig, trans, seed=rng.randint(100, 999999))

    prompt = (
        f"Triangle \\(ABC\\) has vertices \\(A({orig[0][0]}; {orig[0][1]})\\), \\(B({orig[1][0]}; {orig[1][1]})\\), and \\(C({orig[2][0]}; {orig[2][1]})\\).\n"
        f"The triangle is enlarged by a scale factor of **\\(k = 2\\)** with the center of enlargement at the origin.\n\n"
        f"Determine the coordinates of image vertices \\(A'\\), \\(B'\\), and \\(C'\\)."
    )
    sol = (
        f"**Multiply each vertex coordinate by \\(k = 2\\):**\n"
        f"- \\(A'(2 \\times {orig[0][0]}; 2 \\times {orig[0][1]}) = A'({trans[0][0]}; {trans[0][1]})\\)\n"
        f"- \\(B'(2 \\times {orig[1][0]}; 2 \\times {orig[1][1]}) = B'({trans[1][0]}; {trans[1][1]})\\)\n"
        f"- \\(C'(2 \\times {orig[2][0]}; 2 \\times {orig[2][1]}) = C'({trans[2][0]}; {trans[2][1]})\\)"
    )
    ans = f"A'({trans[0][0]}; {trans[0][1]}), B'({trans[1][0]}; {trans[1][1]}), C'({trans[2][0]}; {trans[2][1]})"
    return {
        "id": f"g8_trans_enl_tri_k2_{rng.randint(100000, 999999)}",
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
        "subskill": "33_enlargement_triangle_vertices_scale_factor_2",
        "learning_objective_id": "math_g8_trans_enl_tri_k2",
        "hints": {
            "tier_1": "Multiply both x and y of each vertex by 2.",
            "tier_2": f"A' is ({trans[0][0]}; {trans[0][1]}).",
            "tier_3": ans,
        },
        "misconception_tags": ["multiplying_only_one_coordinate_by_scale_factor"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 34. Reduction Triangle Vertices Fractional Scale Factor (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_34_reduction_triangle_vertices_fractional_scale_factor(rng: random.Random) -> Dict[str, Any]:
    shift = rng.choice([0, 2])
    orig = [(2, 2 + shift), (6, 2 + shift), (2, 6 + shift)]
    trans = [(x // 2, y // 2) for x, y in orig]
    svg = draw_transformation_grid_svg(orig, trans, seed=rng.randint(100, 999999))

    prompt = (
        f"Triangle \\(ABC\\) has vertices \\(A({orig[0][0]}; {orig[0][1]})\\), \\(B({orig[1][0]}; {orig[1][1]})\\), and \\(C({orig[2][0]}; {orig[2][1]})\\).\n"
        f"The triangle undergoes a reduction with scale factor **\\(k = \\frac{{1}}{{2}}\\)** about the origin.\n\n"
        f"Calculate the coordinates of image vertices \\(A'\\), \\(B'\\), and \\(C'\\)."
    )
    sol = (
        f"**Multiply each coordinate by \\(\\frac{{1}}{{2}}\\):**\n"
        f"- \\(A'({orig[0][0]} \\times \\frac{{1}}{{2}}; {orig[0][1]} \\times \\frac{{1}}{{2}}) = A'({trans[0][0]}; {trans[0][1]})\\)\n"
        f"- \\(B'({orig[1][0]} \\times \\frac{{1}}{{2}}; {orig[1][1]} \\times \\frac{{1}}{{2}}) = B'({trans[1][0]}; {trans[1][1]})\\)\n"
        f"- \\(C'({orig[2][0]} \\times \\frac{{1}}{{2}}; {orig[2][1]} \\times \\frac{{1}}{{2}}) = C'({trans[2][0]}; {trans[2][1]})\\)"
    )
    ans = f"A'({trans[0][0]}; {trans[0][1]}), B'({trans[1][0]}; {trans[1][1]}), C'({trans[2][0]}; {trans[2][1]})"
    return {
        "id": f"g8_trans_red_tri_half_{rng.randint(100000, 999999)}",
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
        "subskill": "34_reduction_triangle_vertices_fractional_scale_factor",
        "learning_objective_id": "math_g8_trans_red_tri_half",
        "hints": {
            "tier_1": "Halve each coordinate of all three vertices.",
            "tier_2": f"A' is ({trans[0][0]}; {trans[0][1]}).",
            "tier_3": ans,
        },
        "misconception_tags": ["dividing_by_2_incorrectly_with_negative_or_fractional_values"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 35. Determine Scale Factor From Original and Image Lengths (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_35_determine_scale_factor_from_original_and_image_lengths(rng: random.Random) -> Dict[str, Any]:
    orig_len = rng.choice([4, 5, 6, 8])
    k = rng.choice([2, 3, 4])
    img_len = orig_len * k

    prompt = (
        f"A line segment on an original polygon has length **{orig_len} cm**.\n"
        f"The corresponding line segment on the enlarged polygon has length **{img_len} cm**.\n\n"
        f"1. State the formula for determining the scale factor \\(k\\).\n"
        f"2. Calculate the exact scale factor \\(k\\) of this enlargement."
    )
    sol = (
        f"**1. Scale Factor Formula:**\n"
        f"\\[ k = \\frac{{\\text{{Length of enlarged dimension}}}}{{\\text{{Length of original dimension}}}} \\]\n\n"
        f"**2. Calculation:**\n"
        f"\\[ k = \\frac{{{img_len}}}{{{orig_len}}} = {k} \\]"
    )
    ans = f"1. enlarged length / original length; 2. k = {k}"
    return {
        "id": f"g8_trans_calc_k_{rng.randint(100000, 999999)}",
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
        "subskill": "35_determine_scale_factor_from_original_and_image_lengths",
        "learning_objective_id": "math_g8_trans_calc_k",
        "hints": {
            "tier_1": "Divide the enlarged length by the original length.",
            "tier_2": f"{img_len} ÷ {orig_len}.",
            "tier_3": f"k = {k}.",
        },
        "misconception_tags": ["dividing_original_by_image_inverting_scale_factor"],
    }


# ----------------------------------------------------------------------
# 36. Determine Scale Factor From Coordinates (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_36_determine_scale_factor_from_coordinates(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([2, 3, 4])
    py = rng.choice([3, 5])
    k = rng.choice([2, 3, 5])
    px_prime, py_prime = px * k, py * k

    prompt = (
        f"An enlargement centered at the origin maps point \\(A({px}; {py})\\) to image point \\(A'({px_prime}; {py_prime})\\).\n\n"
        f"1. Determine the scale factor \\(k\\).\n"
        f"2. Verify your answer using both the x-coordinates and the y-coordinates."
    )
    sol = (
        f"**1. Scale factor \\(k\\):**\n"
        f"\\[ k = \\frac{{x'}}{{x}} = \\frac{{{px_prime}}}{{{px}}} = {k} \\]\n\n"
        f"**2. Verification:**\n"
        f"Using y-coordinates: \\(\\frac{{y'}}{{y}} = \\frac{{{py_prime}}}{{{py}}} = {k}\\).\n"
        f"Both coordinates confirm \\(k = {k}\\)."
    )
    ans = f"1. k = {k}; 2. x'/x = {px_prime}/{px} = {k} and y'/y = {py_prime}/{py} = {k}"
    return {
        "id": f"g8_trans_k_coords_{rng.randint(100000, 999999)}",
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
        "subskill": "36_determine_scale_factor_from_coordinates",
        "learning_objective_id": "math_g8_trans_k_coords",
        "hints": {
            "tier_1": "Divide any image coordinate by its corresponding original coordinate.",
            "tier_2": f"{px_prime} ÷ {px}.",
            "tier_3": f"k = {k}.",
        },
        "misconception_tags": ["subtracting_coordinates_instead_of_dividing_for_scale_factor"],
    }


# ----------------------------------------------------------------------
# 37. Enlargement Perimeter Relationship k (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_37_enlargement_perimeter_relationship_k(rng: random.Random) -> Dict[str, Any]:
    orig_p = rng.choice([14, 18, 22, 25])
    k = rng.choice([2, 3, 4])
    new_p = orig_p * k

    prompt = (
        f"A polygon has a perimeter of **{orig_p} cm**.\n"
        f"The polygon is enlarged by a scale factor of **\\(k = {k}\\)**.\n\n"
        f"1. State the relationship between the original perimeter \\(P\\), the scale factor \\(k\\), and the new perimeter \\(P'\\).\n"
        f"2. Calculate the perimeter of the enlarged polygon."
    )
    sol = (
        f"**1. Relationship:** Perimeter is a one-dimensional linear measure, so the image perimeter is scaled by factor \\(k\\):\n"
        f"\\[ P' = k \\times P \\]\n\n"
        f"**2. Calculation:**\n"
        f"\\[ P' = {k} \\times {orig_p} = {new_p} \\text{{ cm}} \\]"
    )
    ans = f"1. P' = k * P; 2. {new_p} cm"
    return {
        "id": f"g8_trans_perim_k_{rng.randint(100000, 999999)}",
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
        "subskill": "37_enlargement_perimeter_relationship_k",
        "learning_objective_id": "math_g8_trans_perim_k",
        "hints": {
            "tier_1": "Perimeter is multiplied directly by k.",
            "tier_2": f"Multiply {orig_p} by {k}.",
            "tier_3": f"{new_p} cm.",
        },
        "misconception_tags": ["multiplying_perimeter_by_k_squared_instead_of_k"],
    }


# ----------------------------------------------------------------------
# 38. Enlargement Area Relationship k Squared (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_38_enlargement_area_relationship_k_squared(rng: random.Random) -> Dict[str, Any]:
    orig_a = rng.choice([6, 10, 15, 20])
    k = rng.choice([2, 3, 4])
    k_sq = k * k
    new_a = orig_a * k_sq

    prompt = (
        f"A triangle has an area of **{orig_a} cm²**.\n"
        f"It is enlarged by a scale factor of **\\(k = {k}\\)**.\n\n"
        f"1. Explain why the area of the enlarged triangle is not simply \\({k} \\times {orig_a}\\).\n"
        f"2. Calculate the area of the enlarged triangle in cm²."
    )
    sol = (
        f"**1. Explanation:** Area is a two-dimensional quantity (length \\(\\times\\) breadth). Since both the base "
        f"and perpendicular height are multiplied by \\(k\\), the area is multiplied by \\(k \\times k = k^2\\).\n\n"
        f"**2. Calculation:**\n"
        f"\\[ \\text{{New Area}} = k^2 \\times \\text{{Original Area}} = {k}^2 \\times {orig_a} = {k_sq} \\times {orig_a} = {new_a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. both dimensions are multiplied by k so area scales by k²; 2. {new_a} cm²"
    return {
        "id": f"g8_trans_area_k2_{rng.randint(100000, 999999)}",
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
        "subskill": "38_enlargement_area_relationship_k_squared",
        "learning_objective_id": "math_g8_trans_area_k2",
        "hints": {
            "tier_1": "Area scales by k² (scale factor squared).",
            "tier_2": f"Calculate {k}² = {k_sq}, then multiply by {orig_a}.",
            "tier_3": f"{new_a} cm².",
        },
        "misconception_tags": ["multiplying_area_by_k_instead_of_k_squared"],
    }


# ----------------------------------------------------------------------
# 39. Reduction Area Relationship k Squared (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_39_reduction_area_relationship_k_squared(rng: random.Random) -> Dict[str, Any]:
    k_inv = rng.choice([2, 3])
    k_sq = k_inv * k_inv
    new_a = rng.choice([5, 8, 12])
    orig_a = new_a * k_sq

    prompt = (
        f"A rectangle with an original area of **{orig_a} cm²** is reduced by a scale factor of **\\(k = \\frac{{1}}{{{k_inv}}}\\)**.\n\n"
        f"1. State the scale factor for the area (in fraction form).\n"
        f"2. Calculate the area of the reduced rectangle."
    )
    sol = (
        f"**1. Area scale factor:**\n"
        f"\\[ k^2 = \\left(\\frac{{1}}{{{k_inv}}}\\right)^2 = \\frac{{1}}{{{k_sq}}} \\]\n\n"
        f"**2. Reduced Area:**\n"
        f"\\[ \\text{{New Area}} = \\frac{{1}}{{{k_sq}}} \\times {orig_a} = {new_a} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. 1/{k_sq}; 2. {new_a} cm²"
    return {
        "id": f"g8_trans_red_area_{rng.randint(100000, 999999)}",
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
        "subskill": "39_reduction_area_relationship_k_squared",
        "learning_objective_id": "math_g8_trans_red_area",
        "hints": {
            "tier_1": f"Square the fractional scale factor: (1/{k_inv})² = 1/{k_sq}.",
            "tier_2": f"Divide {orig_a} by {k_sq}.",
            "tier_3": f"{new_a} cm².",
        },
        "misconception_tags": ["dividing_area_by_k_instead_of_k_squared"],
    }


# ----------------------------------------------------------------------
# 40. Similar Figures Properties: Angles Equal, Sides Proportional (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_40_similar_figures_properties_angles_equal_sides_proportional(rng: random.Random) -> Dict[str, Any]:
    angle_a = rng.choice([40, 50, 65])
    angle_b = rng.choice([60, 70])
    angle_c = 180 - (angle_a + angle_b)
    k = rng.choice([2, 3])

    prompt = (
        f"Triangle \\(ABC\\) has interior angles \\(A = {angle_a}^\\circ\\), \\(B = {angle_b}^\\circ\\), and \\(C = {angle_c}^\\circ\\).\n"
        f"The triangle is enlarged by scale factor \\(k = {k}\\) to create similar triangle \\(\\triangle A'B'C'\\).\n\n"
        f"1. What is the size of interior angle \\(A'\\) in the enlarged triangle?\n"
        f"2. Complete the fundamental geometric statement: For similar figures, corresponding angles are \\(\\dots\\) "
        f"and corresponding sides are \\(\\dots\\)."
    )
    sol = (
        f"**1. Size of angle A':** Exactly **{angle_a}°**. Under an enlargement, angle sizes remain invariant (unchanged).\n\n"
        f"**2. Fundamental Statement:** For similar figures, corresponding angles are **equal** and "
        f"corresponding sides are **proportional (in the same ratio)**."
    )
    ans = f"1. {angle_a}°; 2. equal, proportional"
    return {
        "id": f"g8_trans_sim_prop_{rng.randint(100000, 999999)}",
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
        "subskill": "40_similar_figures_properties_angles_equal_sides_proportional",
        "learning_objective_id": "math_g8_trans_sim_prop",
        "hints": {
            "tier_1": "Enlargements do not change angles; they only change side lengths.",
            "tier_2": f"Angle A' = Angle A = {angle_a}°.",
            "tier_3": f"{angle_a}°; equal, proportional.",
        },
        "misconception_tags": ["multiplying_interior_angles_by_scale_factor"],
    }


# ----------------------------------------------------------------------
# 41. Composite Translation Then Reflection Across X-Axis (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_41_composite_translation_then_reflection_across_x_axis(rng: random.Random) -> Dict[str, Any]:
    px, py = rng.choice([1, 2]), rng.choice([2, 3])
    dx = rng.choice([2, 3])
    # Step 1: translate (x+dx, y)
    t1 = (px + dx, py)
    # Step 2: reflect x-axis (x, -y)
    t2 = (t1[0], -t1[1])

    svg = draw_transformation_grid_svg([(px, py)], [t2], "P", "P''", line_of_reflection="x-axis", seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(P({px}; {py})\\) undergoes a two-step composite transformation:\n"
        f"Step 1: Translated **{dx} units to the right**.\n"
        f"Step 2: Reflected across the **x-axis**.\n\n"
        f"Determine the final coordinates of point \\(P''\\) after both transformations are completed."
    )
    sol = (
        f"**Step 1 (Translation):**\n"
        f"\\[ P({px}; {py}) \\to P'({px} + {dx}; {py}) = P'({t1[0]}; {t1[1]}) \\]\n\n"
        f"**Step 2 (Reflection across x-axis):**\n"
        f"\\[ P'({t1[0]}; {t1[1]}) \\to P''({t2[0]}; -({t1[1]})) = P''({t2[0]}; {t2[1]}) \\]"
    )
    ans = f"P''({t2[0]}; {t2[1]})"
    return {
        "id": f"g8_trans_comp_trans_refl_{rng.randint(100000, 999999)}",
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
        "subskill": "41_composite_translation_then_reflection_across_x_axis",
        "learning_objective_id": "math_g8_trans_comp_trans_refl",
        "hints": {
            "tier_1": f"First add {dx} to x: ({px + dx}; {py}). Then negate y.",
            "tier_2": f"P'({t1[0]}; {t1[1]}) becomes P''({t2[0]}; {-t1[1]}).",
            "tier_3": f"P''({t2[0]}; {t2[1]}).",
        },
        "misconception_tags": ["performing_composite_transformations_in_wrong_sequence"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 42. Composite Reflection Then Translation (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_42_composite_reflection_then_translation(rng: random.Random) -> Dict[str, Any]:
    px, py = rng.choice([3, 4]), rng.choice([1, 2])
    dy = rng.choice([3, 4])
    # Step 1: reflect y-axis (-x, y)
    t1 = (-px, py)
    # Step 2: translate dy up (-x, y + dy)
    t2 = (t1[0], t1[1] + dy)

    prompt = (
        f"Point \\(Q({px}; {py})\\) is first reflected across the **y-axis** and then translated **{dy} units up**.\n\n"
        f"1. Write down the intermediate coordinates after the reflection.\n"
        f"2. Write down the final coordinates after the upward translation."
    )
    sol = (
        f"**1. After reflection across y-axis:**\n"
        f"\\[ Q({px}; {py}) \\to Q'(-{px}; {py}) = Q'({t1[0]}; {t1[1]}) \\]\n\n"
        f"**2. After upward translation:**\n"
        f"\\[ Q'({t1[0]}; {t1[1]}) \\to Q''({t1[0]}; {t1[1]} + {dy}) = Q''({t2[0]}; {t2[1]}) \\]"
    )
    ans = f"1. Q'({t1[0]}; {t1[1]}); 2. Q''({t2[0]}; {t2[1]})"
    return {
        "id": f"g8_trans_comp_refl_trans_{rng.randint(100000, 999999)}",
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
        "subskill": "42_composite_reflection_then_translation",
        "learning_objective_id": "math_g8_trans_comp_refl_trans",
        "hints": {
            "tier_1": f"Reflecting across y-axis negates x: ({ -px }; { py }).",
            "tier_2": f"Adding {dy} to y gives ({ -px }; { py + dy }).",
            "tier_3": f"Q'({t1[0]}; {t1[1]}); Q''({t2[0]}; {t2[1]}).",
        },
        "misconception_tags": ["negating_y_instead_of_x_during_composite_step"],
    }


# ----------------------------------------------------------------------
# 43. Composite Rotation 180° Then Translation (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_43_composite_rotation_180_then_translation(rng: random.Random) -> Dict[str, Any]:
    px, py = rng.choice([2, 3]), rng.choice([1, 4])
    dx = rng.choice([2, 5])
    # Step 1: 180 rot (-x, -y)
    t1 = (-px, -py)
    # Step 2: translate dx right
    t2 = (t1[0] + dx, t1[1])

    prompt = (
        f"Point \\(R({px}; {py})\\) is rotated **180° about the origin** and then translated **{dx} units to the right**.\n\n"
        f"Calculate the coordinates of final point \\(R''\\)."
    )
    sol = (
        f"**Step 1 (180° rotation about origin):**\n"
        f"\\[ R({px}; {py}) \\to R'(-{px}; -{py}) = R'({t1[0]}; {t1[1]}) \\]\n\n"
        f"**Step 2 (Translation {dx} units right):**\n"
        f"\\[ R'({t1[0]}; {t1[1]}) \\to R''({t1[0]} + {dx}; {t1[1]}) = R''({t2[0]}; {t2[1]}) \\]"
    )
    ans = f"R''({t2[0]}; {t2[1]})"
    return {
        "id": f"g8_trans_comp_rot_trans_{rng.randint(100000, 999999)}",
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
        "subskill": "43_composite_rotation_180_then_translation",
        "learning_objective_id": "math_g8_trans_comp_rot_trans",
        "hints": {
            "tier_1": "180° rotation negates both x and y.",
            "tier_2": f"R'({-px}; {-py}), then add {dx} to the x-coordinate.",
            "tier_3": f"R''({t2[0]}; {t2[1]}).",
        },
        "misconception_tags": ["adding_translation_to_y_instead_of_x"],
    }


# ----------------------------------------------------------------------
# 44. Identify Transformation Type From Coordinate Rule (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_44_identify_transformation_type_from_coordinate_rule(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["refl_x", "refl_y", "trans", "enlarge", "rot180"])
    if choice == "refl_x":
        rule = "(x; y) \\to (x; -y)"
        name = "Reflection across the x-axis"
    elif choice == "refl_y":
        rule = "(x; y) \\to (-x; y)"
        name = "Reflection across the y-axis"
    elif choice == "trans":
        rule = "(x; y) \\to (x - 3; y + 4)"
        name = "Translation (3 units left, 4 units up)"
    elif choice == "enlarge":
        rule = "(x; y) \\to (3x; 3y)"
        name = "Enlargement by scale factor 3 centered at the origin"
    else:
        rule = "(x; y) \\to (-x; -y)"
        name = "Rotation of 180° about the origin"

    prompt = (
        f"Consider the algebraic transformation rule \\({rule}\\).\n\n"
        f"1. Name the exact geometric transformation described by this rule.\n"
        f"2. Does this transformation preserve the size (congruence) of the original shape? Answer Yes or No and explain."
    )
    is_cong = "No" if choice == "enlarge" else "Yes"
    sol = (
        f"**1. Transformation Name:** **{name}**.\n\n"
        f"**2. Size preservation:** **{is_cong}**. "
        f"{'An enlargement alters the dimensions and area of the shape by the scale factor' if is_cong == 'No' else 'Reflections, translations, and rotations are isometries (rigid motions) that preserve side lengths and angle sizes' }."
    )
    ans = f"1. {name}; 2. {is_cong}"
    return {
        "id": f"g8_trans_rule_id_{rng.randint(100000, 999999)}",
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
        "subskill": "44_identify_transformation_type_from_coordinate_rule",
        "learning_objective_id": "math_g8_trans_rule_id",
        "hints": {
            "tier_1": "Recall: (x; -y) is x-reflection; (-x; y) is y-reflection; (kx; ky) is dilation.",
            "tier_2": f"Here the rule is {rule}.",
            "tier_3": f"{name}; {is_cong}.",
        },
        "misconception_tags": ["confusing_dilation_with_translation_rules"],
    }


# ----------------------------------------------------------------------
# 45. Congruence vs Similarity Classification Table (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_45_congruence_vs_similarity_classification_table(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Geometric transformations can produce congruent images or similar images.\n\n"
        f"1. Which three geometric transformations always produce **congruent** figures (identical size and shape)?\n"
        f"2. Which transformations produce **similar** figures where angle sizes match but side lengths are scaled?"
    )
    sol = (
        f"**1. Congruent Transformations (Rigid Motions / Isometries):**\n"
        f"- **Translations** (sliding)\n"
        f"- **Reflections** (flipping)\n"
        f"- **Rotations** (turning)\n\n"
        f"**2. Similar Transformations:**\n"
        f"- **Enlargements** and **reductions** (dilations with scale factor \\(k \\neq 1\\))."
    )
    ans = "1. translations, reflections, rotations; 2. enlargements and reductions"
    return {
        "id": f"g8_trans_cong_sim_class_{rng.randint(100000, 999999)}",
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
        "subskill": "45_congruence_vs_similarity_classification_table",
        "learning_objective_id": "math_g8_trans_cong_sim_class",
        "hints": {
            "tier_1": "Congruent figures have identical size and shape; similar figures have proportional sides.",
            "tier_2": "Translation, reflection, and rotation do not alter dimensions.",
            "tier_3": "1. Translations, reflections, rotations; 2. Enlargements and reductions.",
        },
        "misconception_tags": ["thinking_reflections_alter_shape_size"],
    }


# ----------------------------------------------------------------------
# 46. Isometry Definition and Properties (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_46_isometry_definition_and_properties(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In advanced transformation geometry, certain mappings are termed **isometries**.\n\n"
        f"1. Define the mathematical term **isometry**.\n"
        f"2. Name two geometric properties that remain strictly invariant under an isometry."
    )
    sol = (
        f"**1. Definition:** An isometry (rigid transformation) is a geometric transformation that preserves "
        f"distances between all pairs of points (distance-preserving mapping).\n\n"
        f"**2. Invariant Properties:**\n"
        f"- Lengths of line segments (distances).\n"
        f"- Measures of interior angles.\n"
        f"- Parallelism of lines and total perimeter/area."
    )
    ans = "1. distance-preserving transformation; 2. side lengths and angle measures"
    return {
        "id": f"g8_trans_isometry_{rng.randint(100000, 999999)}",
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
        "subskill": "46_isometry_definition_and_properties",
        "learning_objective_id": "math_g8_trans_isometry",
        "hints": {
            "tier_1": "'Iso' means equal and 'metry' means measure.",
            "tier_2": "An isometry preserves distance and angle measures.",
            "tier_3": "Distance-preserving transformation; side lengths and angles.",
        },
        "misconception_tags": ["believing_dilations_are_isometries"],
    }


# ----------------------------------------------------------------------
# 47. Coordinate Geometry Distance After Translation (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_47_coordinate_geometry_distance_after_translation(rng: random.Random) -> Dict[str, Any]:
    seg_len = rng.choice([5, 8, 10, 12])
    dx = rng.choice([3, 7])
    dy = rng.choice([-4, 5])

    prompt = (
        f"Line segment \\(AB\\) has a length of **{seg_len} units**.\n"
        f"It is translated according to the rule \\((x; y) \\to (x + {dx}; y {dy:+d})\\) to form segment \\(A'B'\\).\n\n"
        f"1. What is the length of transformed segment \\(A'B'\\)?\n"
        f"2. Explain why the length of the segment is unchanged."
    )
    sol = (
        f"**1. Length of A'B':** Exactly **{seg_len} units**.\n\n"
        f"**2. Explanation:** Translation is a rigid motion (isometry). Every point on the segment is shifted "
        f"by the exact same vector distance and direction, preserving the length of the segment."
    )
    ans = f"1. {seg_len} units; 2. translation is an isometry that preserves distance"
    return {
        "id": f"g8_trans_dist_inv_{rng.randint(100000, 999999)}",
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
        "subskill": "47_coordinate_geometry_distance_after_translation",
        "learning_objective_id": "math_g8_trans_dist_inv",
        "hints": {
            "tier_1": "Translating a line segment does not stretch or shrink it.",
            "tier_2": f"Length of A'B' equals length of AB = {seg_len}.",
            "tier_3": f"{seg_len} units; translation preserves distances.",
        },
        "misconception_tags": ["adding_translation_shift_to_segment_length"],
    }


# ----------------------------------------------------------------------
# 48. Transformation Error Analysis: Reflection Sign (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_48_transformation_error_analysis_incorrect_reflection_sign(rng: random.Random) -> Dict[str, Any]:
    px, py = rng.choice([3, 5]), rng.choice([2, 4])
    prompt = (
        f"A learner is asked to reflect point \\(P({px}; {py})\\) across the line \\(y = 0\\).\n"
        f"The learner writes down the answer as \\(P'(-{px}; {py})\\).\n\n"
        f"1. Identify the conceptual error made by the learner.\n"
        f"2. State the correct coordinates of point \\(P'\\)."
    )
    sol = (
        f"**1. Error Analysis:** The learner incorrectly reflected across the vertical axis \\(x = 0\\) instead of the horizontal line \\(y = 0\\). "
        f"Reflection across the line \\(y = 0\\) requires keeping the x-coordinate unchanged and negating the y-coordinate: \\((x; -y)\\).\n\n"
        f"**2. Correct Answer:** \\(P'({px}; -{py})\\)."
    )
    ans = f"1. reflected across vertical axis instead of horizontal line y = 0 (negated x instead of y); 2. P'({px}; -{py})"
    return {
        "id": f"g8_trans_err_anal_{rng.randint(100000, 999999)}",
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
        "subskill": "48_transformation_error_analysis_incorrect_reflection_sign",
        "learning_objective_id": "math_g8_trans_err_anal",
        "hints": {
            "tier_1": "Reflection across the line y = 0 keeps x the same and inverts y.",
            "tier_2": f"Correct rule is (x; -y).",
            "tier_3": f"Learner negated x instead of y; correct is ({px}; {-py}).",
        },
        "misconception_tags": ["confusing_x_and_y_reflection_coordinate_signs"],
    }


# ----------------------------------------------------------------------
# 49. Tessellation Basic Patterns Using Translations (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_49_tessellation_basic_patterns_using_translations(rng: random.Random) -> Dict[str, Any]:
    poly = rng.choice(["regular hexagon", "equilateral triangle", "square"])
    interior_angle = {"regular hexagon": 120, "equilateral triangle": 60, "square": 90}[poly]

    prompt = (
        f"A repeating geometric pattern is created to cover a flat surface using identical **{poly}s**.\n\n"
        f"1. What is the mathematical term for a tiled pattern that covers a surface without any gaps or overlaps?\n"
        f"2. Explain using interior angles ({interior_angle}°) why {poly}s can form this pattern around a single vertex."
    )
    count = 360 // interior_angle
    sol = (
        f"**1. Mathematical Term:** A **tessellation** (or tiling).\n\n"
        f"**2. Explanation:** The interior angle of a {poly} is **{interior_angle}°**. Around a single vertex, "
        f"the angles must sum to exactly **360°**:\n"
        f"\\[ {count} \\times {interior_angle}^\\circ = 360^\\circ \\]\n"
        f"Because {interior_angle}° divides 360° evenly into {count} whole shapes, they fit perfectly without gaps or overlaps."
    )
    ans = f"1. tessellation; 2. {count} x {interior_angle}° = 360°, fitting completely around a vertex"
    return {
        "id": f"g8_trans_tessell_{rng.randint(100000, 999999)}",
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
        "subskill": "49_tessellation_basic_patterns_using_translations",
        "learning_objective_id": "math_g8_trans_tessell",
        "hints": {
            "tier_1": "Covering a plane without gaps or overlaps is called tessellation.",
            "tier_2": f"Check if {interior_angle}° divides 360° evenly.",
            "tier_3": f"Tessellation; {count} * {interior_angle}° = 360°.",
        },
        "misconception_tags": ["assuming_any_polygon_can_tessellate_without_checking_angles"],
    }


# ----------------------------------------------------------------------
# 50. Transformation Word Problem Computer Graphics Scaling (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_50_transformation_word_problem_computer_graphics_scaling(rng: random.Random) -> Dict[str, Any]:
    w0 = rng.choice([16, 32, 64])
    h0 = rng.choice([16, 32, 48])
    zoom = rng.choice([2, 3, 4])
    w_final = w0 * zoom
    h_final = h0 * zoom

    prompt = (
        f"A video game developer scales a 2D character sprite with initial dimensions **{w0} pixels wide** by "
        f"**{h0} pixels high** using an enlargement factor of **\\(k = {zoom}\\)**.\n\n"
        f"1. What are the new pixel dimensions (width and height) of the enlarged sprite?\n"
        f"2. By what factor has the total screen area occupied by the sprite increased?"
    )
    zoom_sq = zoom * zoom
    sol = (
        f"**1. New pixel dimensions:**\n"
        f"- Width = \\({w0} \\times {zoom} = {w_final}\\) pixels\n"
        f"- Height = \\({h0} \\times {zoom} = {h_final}\\) pixels\n\n"
        f"**2. Area increase factor:**\n"
        f"Since both width and height are multiplied by \\(k = {zoom}\\), the screen area increases by:\n"
        f"\\[ k^2 = {zoom}^2 = {zoom_sq} \\text{{ times}} \\]"
    )
    ans = f"1. {w_final} x {h_final} pixels; 2. {zoom_sq} times (k²)"
    return {
        "id": f"g8_trans_cg_scaling_{rng.randint(100000, 999999)}",
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
        "subskill": "50_transformation_word_problem_computer_graphics_scaling",
        "learning_objective_id": "math_g8_trans_cg_scaling",
        "hints": {
            "tier_1": f"Multiply width and height by {zoom}.",
            "tier_2": f"Area scale factor is k² = {zoom}² = {zoom_sq}.",
            "tier_3": f"{w_final} x {h_final} pixels; {zoom_sq} times.",
        },
        "misconception_tags": ["scaling_area_by_k_instead_of_k_squared_in_applications"],
    }
