"""Grade 8 Mathematics — Transformation Geometry Archetypes 01 to 25.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 3/01. Transformation geometry.md

Archetypes covering:
  - 01 to 03: Lines of symmetry in 2D shapes and polygons.
  - 04 to 10: Reflections across x-axis, y-axis, line y=x, triangle reflections, mirror identification, invariant points.
  - 11 to 20: Translations horizontally, vertically, vector combinations, triangle mapping, inverse translation, congruence.
  - 21 to 25: Rotations 90° clockwise, 90° counter-clockwise, 180° half-turn, triangle rotations about origin.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Tuple

from .transformation_geometry_svg import (
    draw_transformation_grid_svg,
    draw_symmetry_polygon_svg,
)


# ----------------------------------------------------------------------
# 01. Lines of Symmetry in Quadrilaterals (WITH SVG)
# ----------------------------------------------------------------------
def arch_01_identify_lines_of_symmetry_quadrilaterals(rng: random.Random) -> Dict[str, Any]:
    shape = rng.choice(["square", "rectangle"])
    svg = draw_symmetry_polygon_svg(poly_type=shape, seed=rng.randint(100, 999999))
    ans_map = {"square": ("4", "two diagonals, one vertical, and one horizontal line"),
               "rectangle": ("2", "one vertical and one horizontal line through the midpoints of opposite sides")}
    cnt, desc = ans_map[shape]

    prompt = (
        f"Consider a geometric **{shape}**:\n\n"
        f"1. How many axes (lines) of symmetry does a {shape} possess?\n"
        f"2. Explain why the diagonals of a non-square rectangle are not lines of symmetry."
    )
    sol = (
        f"**1. Number of axes:** A {shape} has **{cnt}** lines of symmetry ({desc}).\n\n"
        f"**2. Non-square rectangle diagonals:** Folding a rectangle along its diagonal does not cause opposite vertices "
        f"to match up; the edges do not coincide, so the diagonal is not an axis of symmetry."
    )
    ans = f"1. {cnt}; 2. folding along diagonal does not align edges/vertices"
    return {
        "id": f"g8_trans_sym_quad_{rng.randint(100000, 999999)}",
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
        "subskill": "01_identify_lines_of_symmetry_quadrilaterals",
        "learning_objective_id": "math_g8_trans_sym_quad",
        "hints": {
            "tier_1": f"Think about folding the {shape} so both halves match exactly.",
            "tier_2": f"A square has 4 lines of symmetry; a rectangle has 2.",
            "tier_3": f"{cnt} lines of symmetry.",
        },
        "misconception_tags": ["thinking_diagonals_are_symmetry_lines_for_all_rectangles"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 02. Lines of Symmetry in Triangles (WITH SVG)
# ----------------------------------------------------------------------
def arch_02_identify_lines_of_symmetry_triangles(rng: random.Random) -> Dict[str, Any]:
    tri = rng.choice(["equilateral_triangle", "isosceles_triangle"])
    svg = draw_symmetry_polygon_svg(poly_type=tri, seed=rng.randint(100, 999999))
    name = "equilateral triangle" if tri == "equilateral_triangle" else "isosceles triangle"
    cnt = 3 if tri == "equilateral_triangle" else 1

    prompt = (
        f"A triangle is classified as an **{name}**:\n\n"
        f"1. State the number of lines of symmetry for an {name}.\n"
        f"2. How many lines of symmetry does a scalene triangle possess?"
    )
    sol = (
        f"**1. {name.capitalize()} lines of symmetry:** Exactly **{cnt}**.\n\n"
        f"**2. Scalene triangle:** A scalene triangle has **0** lines of symmetry because all three sides and angles are unequal."
    )
    ans = f"1. {cnt}; 2. 0"
    return {
        "id": f"g8_trans_sym_tri_{rng.randint(100000, 999999)}",
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
        "subskill": "02_identify_lines_of_symmetry_triangles",
        "learning_objective_id": "math_g8_trans_sym_tri",
        "hints": {
            "tier_1": "An equilateral triangle has 3 equal sides; an isosceles triangle has 2.",
            "tier_2": "A regular n-sided polygon has n lines of symmetry.",
            "tier_3": f"{cnt} for {name}, 0 for scalene.",
        },
        "misconception_tags": ["assuming_all_triangles_have_three_axes_of_symmetry"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 03. Lines of Symmetry in Regular Polygons (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_03_identify_lines_of_symmetry_regular_polygons(rng: random.Random) -> Dict[str, Any]:
    n, name = rng.choice([(5, "regular pentagon"), (6, "regular hexagon"), (8, "regular octagon")])
    prompt = (
        f"Consider a **{name}** with \\({n}\\) equal sides and \\({n}\\) equal interior angles:\n\n"
        f"1. How many axes of symmetry does a {name} have?\n"
        f"2. State the general rule relating the number of sides \\(n\\) of any regular polygon to its count of symmetry lines."
    )
    sol = (
        f"**1. Number of axes:** A {name} has **{n}** lines of symmetry.\n\n"
        f"**2. General Rule:** Any regular polygon with \\(n\\) sides has exactly \\(n\\) lines of symmetry."
    )
    ans = f"1. {n}; 2. regular n-gon has n lines of symmetry"
    return {
        "id": f"g8_trans_sym_poly_{rng.randint(100000, 999999)}",
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
        "subskill": "03_identify_lines_of_symmetry_regular_polygons",
        "learning_objective_id": "math_g8_trans_sym_poly",
        "hints": {
            "tier_1": "For regular polygons, the number of lines of symmetry equals the number of sides.",
            "tier_2": f"A {name} has {n} sides.",
            "tier_3": f"{n} lines of symmetry.",
        },
        "misconception_tags": ["confusing_rotational_symmetry_with_line_symmetry"],
    }


# ----------------------------------------------------------------------
# 04. Reflection Across X-Axis Single Point (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_04_reflection_across_x_axis_single_point(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([1, 2, 3, 4])
    py = rng.choice([2, 3, 4, 5])
    rx, ry = px, -py
    svg = draw_transformation_grid_svg([(px, py)], [(rx, ry)], "P", "P'", "x-axis", seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(P({px}; {py})\\) is reflected across the horizontal x-axis to produce image \\(P'\\).\n\n"
        f"1. State the coordinate mapping rule for a reflection across the x-axis: \\((x; y) \\to (\\dots; \\dots)\\).\n"
        f"2. Write down the exact coordinates of image point \\(P'\\)."
    )
    sol = (
        f"**1. Reflection Rule across x-axis:** \\((x; y) \\to (x; -y)\\). The x-coordinate stays unchanged, while the y-coordinate changes sign.\n\n"
        f"**2. Coordinates of P':**\n"
        f"\\[ P({px}; {py}) \\to P'({rx}; {ry}) \\]"
    )
    ans = f"1. (x; -y); 2. ({rx}; {ry})"
    return {
        "id": f"g8_trans_refl_x_{rng.randint(100000, 999999)}",
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
        "subskill": "04_reflection_across_x_axis_single_point",
        "learning_objective_id": "math_g8_trans_refl_x",
        "hints": {
            "tier_1": "Reflection across the x-axis keeps the x-coordinate the same and inverts the sign of y.",
            "tier_2": f"({px}; {py}) becomes ({px}; -({py})).",
            "tier_3": f"P'({rx}; {ry}).",
        },
        "misconception_tags": ["negating_x_instead_of_y_for_x_axis_reflection"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 05. Reflection Across Y-Axis Single Point (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_05_reflection_across_y_axis_single_point(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([2, 3, 4, 5])
    py = rng.choice([1, 2, 3, 4])
    rx, ry = -px, py
    svg = draw_transformation_grid_svg([(px, py)], [(rx, ry)], "Q", "Q'", "y-axis", seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(Q({px}; {py})\\) is reflected across the vertical y-axis to produce image \\(Q'\\).\n\n"
        f"1. State the coordinate mapping rule for a reflection across the y-axis: \\((x; y) \\to (\\dots; \\dots)\\).\n"
        f"2. Write down the exact coordinates of image point \\(Q'\\)."
    )
    sol = (
        f"**1. Reflection Rule across y-axis:** \\((x; y) \\to (-x; y)\\). The y-coordinate stays unchanged, while the x-coordinate changes sign.\n\n"
        f"**2. Coordinates of Q':**\n"
        f"\\[ Q({px}; {py}) \\to Q'({rx}; {ry}) \\]"
    )
    ans = f"1. (-x; y); 2. ({rx}; {ry})"
    return {
        "id": f"g8_trans_refl_y_{rng.randint(100000, 999999)}",
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
        "subskill": "05_reflection_across_y_axis_single_point",
        "learning_objective_id": "math_g8_trans_refl_y",
        "hints": {
            "tier_1": "Reflection across the y-axis keeps y unchanged and negates x.",
            "tier_2": f"({px}; {py}) becomes (-{px}; {py}).",
            "tier_3": f"Q'({rx}; {ry}).",
        },
        "misconception_tags": ["negating_y_instead_of_x_for_y_axis_reflection"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 06. Reflection Across Line Y = X (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_06_reflection_across_line_y_equals_x(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([1, 2, 4])
    py = rng.choice([3, 5])
    rx, ry = py, px
    svg = draw_transformation_grid_svg([(px, py)], [(rx, ry)], "R", "R'", "y=x", seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(R({px}; {py})\\) is reflected across the diagonal line \\(y = x\\) to yield image \\(R'\\).\n\n"
        f"1. State the coordinate mapping rule for reflection in the line \\(y = x\\): \\((x; y) \\to (\\dots; \\dots)\\).\n"
        f"2. Determine the exact coordinates of image \\(R'\\)."
    )
    sol = (
        f"**1. Mapping Rule:** \\((x; y) \\to (y; x)\\). The coordinates swap positions.\n\n"
        f"**2. Coordinates of R':**\n"
        f"\\[ R({px}; {py}) \\to R'({rx}; {ry}) \\]"
    )
    ans = f"1. (y; x); 2. ({rx}; {ry})"
    return {
        "id": f"g8_trans_refl_yx_{rng.randint(100000, 999999)}",
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
        "subskill": "06_reflection_across_line_y_equals_x",
        "learning_objective_id": "math_g8_trans_refl_yx",
        "hints": {
            "tier_1": "In the line y = x, swap the x and y coordinates.",
            "tier_2": f"({px}; {py}) swaps to ({py}; {px}).",
            "tier_3": f"R'({rx}; {ry}).",
        },
        "misconception_tags": ["negating_coordinates_instead_of_swapping_in_y_equals_x"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 07. Reflection of Triangle Across X-Axis (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_07_reflection_triangle_across_x_axis_vertices(rng: random.Random) -> Dict[str, Any]:
    dx = rng.choice([0, 1])
    orig = [(1 + dx, 2), (4 + dx, 2), (2 + dx, 5)]
    trans = [(x, -y) for x, y in orig]
    svg = draw_transformation_grid_svg(orig, trans, line_of_reflection="x-axis", seed=rng.randint(100, 999999))

    prompt = (
        f"Triangle \\(ABC\\) has vertices \\(A({orig[0][0]}; {orig[0][1]})\\), \\(B({orig[1][0]}; {orig[1][1]})\\), "
        f"and \\(C({orig[2][0]}; {orig[2][1]})\\).\n"
        f"The triangle is reflected across the x-axis to form \\(\\triangle A'B'C'\\).\n\n"
        f"Write down the coordinates of vertices \\(A'\\), \\(B'\\), and \\(C'\\)."
    )
    sol = (
        f"**Reflection across x-axis rule:** \\((x; y) \\to (x; -y)\\)\n"
        f"- \\(A({orig[0][0]}; {orig[0][1]}) \\to A'({trans[0][0]}; {trans[0][1]})\\)\n"
        f"- \\(B({orig[1][0]}; {orig[1][1]}) \\to B'({trans[1][0]}; {trans[1][1]})\\)\n"
        f"- \\(C({orig[2][0]}; {orig[2][1]}) \\to C'({trans[2][0]}; {trans[2][1]})\\)"
    )
    ans = f"A'({trans[0][0]}; {trans[0][1]}), B'({trans[1][0]}; {trans[1][1]}), C'({trans[2][0]}; {trans[2][1]})"
    return {
        "id": f"g8_trans_refl_tri_x_{rng.randint(100000, 999999)}",
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
        "subskill": "07_reflection_triangle_across_x_axis_vertices",
        "learning_objective_id": "math_g8_trans_refl_tri_x",
        "hints": {
            "tier_1": "Keep all x-values the same and negate each y-value.",
            "tier_2": f"A' is ({orig[0][0]}; {-orig[0][1]}). Apply same to B and C.",
            "tier_3": ans,
        },
        "misconception_tags": ["negating_x_values_during_x_axis_reflection"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 08. Reflection of Triangle Across Y-Axis (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_08_reflection_triangle_across_y_axis_vertices(rng: random.Random) -> Dict[str, Any]:
    dy = rng.choice([0, 1])
    orig = [(2, 1 + dy), (5, 1 + dy), (3, 4 + dy)]
    trans = [(-x, y) for x, y in orig]
    svg = draw_transformation_grid_svg(orig, trans, line_of_reflection="y-axis", seed=rng.randint(100, 999999))

    prompt = (
        f"Triangle \\(ABC\\) has vertices \\(A({orig[0][0]}; {orig[0][1]})\\), \\(B({orig[1][0]}; {orig[1][1]})\\), "
        f"and \\(C({orig[2][0]}; {orig[2][1]})\\).\n"
        f"The triangle is reflected across the y-axis to create \\(\\triangle A'B'C'\\).\n\n"
        f"Write down the coordinates of image vertices \\(A'\\), \\(B'\\), and \\(C'\\)."
    )
    sol = (
        f"**Reflection across y-axis rule:** \\((x; y) \\to (-x; y)\\)\n"
        f"- \\(A({orig[0][0]}; {orig[0][1]}) \\to A'({trans[0][0]}; {trans[0][1]})\\)\n"
        f"- \\(B({orig[1][0]}; {orig[1][1]}) \\to B'({trans[1][0]}; {trans[1][1]})\\)\n"
        f"- \\(C({orig[2][0]}; {orig[2][1]}) \\to C'({trans[2][0]}; {trans[2][1]})\\)"
    )
    ans = f"A'({trans[0][0]}; {trans[0][1]}), B'({trans[1][0]}; {trans[1][1]}), C'({trans[2][0]}; {trans[2][1]})"
    return {
        "id": f"g8_trans_refl_tri_y_{rng.randint(100000, 999999)}",
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
        "subskill": "08_reflection_triangle_across_y_axis_vertices",
        "learning_objective_id": "math_g8_trans_refl_tri_y",
        "hints": {
            "tier_1": "Negate all x-coordinates while leaving y-coordinates unchanged.",
            "tier_2": f"A({orig[0][0]}; {orig[0][1]}) becomes A'({-orig[0][0]}; {orig[0][1]}).",
            "tier_3": ans,
        },
        "misconception_tags": ["negating_y_coordinates_during_y_axis_reflection"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 09. Identify Mirror Line From Coordinates (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_09_reflection_identify_mirror_line_from_coordinates(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["x-axis", "y-axis", "y=x"])
    x, y = rng.choice([3, 4, 5]), rng.choice([1, 2])
    if choice == "x-axis":
        p, p_prime = (x, y), (x, -y)
        rule = "x-axis (the line y = 0)"
    elif choice == "y-axis":
        p, p_prime = (x, y), (-x, y)
        rule = "y-axis (the line x = 0)"
    else:
        p, p_prime = (x, y), (y, x)
        rule = "line y = x"

    prompt = (
        f"A point \\(M({p[0]}; {p[1]})\\) is reflected to become point \\(M'({p_prime[0]}; {p_prime[1]})\\).\n\n"
        f"1. Identify the line of reflection (mirror line) for this transformation.\n"
        f"2. Justify your answer by comparing the coordinates of \\(M\\) and \\(M'\\)."
    )
    sol = (
        f"**1. Line of Reflection:** The **{rule}**.\n\n"
        f"**2. Justification:**\n"
        f"Comparing \\(M({p[0]}; {p[1]})\\) and \\(M'({p_prime[0]}; {p_prime[1]})\\), we see that "
        f"{'the x-coordinate is unchanged and y is negated' if choice == 'x-axis' else ('the y-coordinate is unchanged and x is negated' if choice == 'y-axis' else 'x and y swapped positions')}, "
        f"which matches the algebraic definition of reflection across the {choice}."
    )
    ans = f"1. {choice}; 2. coordinates match {rule} mapping"
    return {
        "id": f"g8_trans_id_mirror_{rng.randint(100000, 999999)}",
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
        "subskill": "09_reflection_identify_mirror_line_from_coordinates",
        "learning_objective_id": "math_g8_trans_id_mirror",
        "hints": {
            "tier_1": "Look at which coordinate changed its sign or whether they swapped.",
            "tier_2": f"Here, {p} mapped to {p_prime}.",
            "tier_3": f"Mirror line is {choice}.",
        },
        "misconception_tags": ["confusing_x_axis_and_y_axis_mirror_rules"],
    }


# ----------------------------------------------------------------------
# 10. Invariant Points on Mirror Line (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_10_reflection_invariant_points_on_mirror_line(rng: random.Random) -> Dict[str, Any]:
    axis = rng.choice(["x-axis", "y-axis"])
    coord_val = rng.choice([3, -4, 5, -2])

    if axis == "x-axis":
        pt = f"({coord_val}; 0)"
        expl = "Because it lies directly on the horizontal axis (y = 0), reflecting across the x-axis leaves it unchanged: (x; -0) = (x; 0)."
    else:
        pt = f"(0; {coord_val})"
        expl = "Because it lies directly on the vertical axis (x = 0), reflecting across the y-axis leaves it unchanged: (-0; y) = (0; y)."

    prompt = (
        f"An **invariant point** is a point that does not change position under a given transformation.\n\n"
        f"1. Give an example of an invariant point when reflecting across the **{axis}**.\n"
        f"2. Explain in general where all invariant points must lie during a reflection."
    )
    sol = (
        f"**1. Invariant point example:** Point \\({pt}\\).\n\n"
        f"**2. Explanation:** {expl} In general, all invariant points during a reflection lie directly "
        f"on the line of reflection (mirror line)."
    )
    ans = f"1. {pt}; 2. all invariant points lie on the line of reflection"
    return {
        "id": f"g8_trans_invariant_{rng.randint(100000, 999999)}",
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
        "subskill": "10_reflection_invariant_points_on_mirror_line",
        "learning_objective_id": "math_g8_trans_invariant",
        "hints": {
            "tier_1": "Points that lie on the mirror line do not move when reflected.",
            "tier_2": f"On the {axis}, the {'y-coordinate' if axis == 'x-axis' else 'x-coordinate'} is zero.",
            "tier_3": f"{pt}; points on the mirror line.",
        },
        "misconception_tags": ["thinking_invariant_points_only_occur_at_origin"],
    }


# ----------------------------------------------------------------------
# 11. Translation Horizontal Units Rule (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_11_translation_horizontal_units_rule(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([-3, -2, -1, 1])
    py = rng.choice([1, 2, 3])
    units = rng.choice([3, 4, 5])
    direction = rng.choice(["right", "left"])
    shift = units if direction == "right" else -units
    tx, ty = px + shift, py

    svg = draw_transformation_grid_svg([(px, py)], [(tx, ty)], "A", "A'", show_vector=True, seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(A({px}; {py})\\) is translated **{units} units to the {direction}** to form image \\(A'\\).\n\n"
        f"1. Write down the algebraic translation rule: \\((x; y) \\to (\\dots; \\dots)\\).\n"
        f"2. Calculate the coordinates of image \\(A'\\)."
    )
    op = f"+ {units}" if direction == "right" else f"- {units}"
    sol = (
        f"**1. Translation Rule:** Moving {units} units {direction} changes only the x-coordinate:\n"
        f"\\[ (x; y) \\to (x {op}; y) \\]\n\n"
        f"**2. Coordinates of A':**\n"
        f"\\[ A'({px} {op}; {py}) = A'({tx}; {ty}) \\]"
    )
    ans = f"1. (x {op}; y); 2. ({tx}; {ty})"
    return {
        "id": f"g8_trans_horiz_{rng.randint(100000, 999999)}",
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
        "subskill": "11_translation_horizontal_units_rule",
        "learning_objective_id": "math_g8_trans_horiz",
        "hints": {
            "tier_1": f"Horizontal movement affects the x-coordinate: right is +, left is -.",
            "tier_2": f"x' = {px} {op}, y' = {py}.",
            "tier_3": f"A'({tx}; {ty}).",
        },
        "misconception_tags": ["modifying_y_coordinate_for_horizontal_translation"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 12. Translation Vertical Units Rule (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_12_translation_vertical_units_rule(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([-2, 1, 3])
    py = rng.choice([-2, -1, 1])
    units = rng.choice([2, 3, 4])
    direction = rng.choice(["up", "down"])
    shift = units if direction == "up" else -units
    tx, ty = px, py + shift

    svg = draw_transformation_grid_svg([(px, py)], [(tx, ty)], "B", "B'", show_vector=True, seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(B({px}; {py})\\) is translated **{units} units {direction}** to form image \\(B'\\).\n\n"
        f"1. Write down the algebraic translation rule: \\((x; y) \\to (\\dots; \\dots)\\).\n"
        f"2. Determine the coordinates of image \\(B'\\)."
    )
    op = f"+ {units}" if direction == "up" else f"- {units}"
    sol = (
        f"**1. Translation Rule:** Moving {units} units {direction} changes only the y-coordinate:\n"
        f"\\[ (x; y) \\to (x; y {op}) \\]\n\n"
        f"**2. Coordinates of B':**\n"
        f"\\[ B'({px}; {py} {op}) = B'({tx}; {ty}) \\]"
    )
    ans = f"1. (x; y {op}); 2. ({tx}; {ty})"
    return {
        "id": f"g8_trans_vert_{rng.randint(100000, 999999)}",
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
        "subskill": "12_translation_vertical_units_rule",
        "learning_objective_id": "math_g8_trans_vert",
        "hints": {
            "tier_1": f"Vertical movement affects the y-coordinate: up is +, down is -.",
            "tier_2": f"x' = {px}, y' = {py} {op}.",
            "tier_3": f"B'({tx}; {ty}).",
        },
        "misconception_tags": ["modifying_x_coordinate_for_vertical_translation"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 13. Combined Vector Translation Rule (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_13_translation_combined_vector_rule(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([-3, -2, 1, 2])
    py = rng.choice([-2, 1, 2])
    dx = rng.choice([2, 3, 4])
    dy = rng.choice([2, 3])
    tx, ty = px + dx, py - dy

    svg = draw_transformation_grid_svg([(px, py)], [(tx, ty)], "C", "C'", show_vector=True, seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(C({px}; {py})\\) undergoes the transformation rule \\((x; y) \\to (x + {dx}; y - {dy})\\).\n\n"
        f"1. Describe this translation in words (horizontal and vertical directions and units).\n"
        f"2. Calculate the coordinates of image point \\(C'\\)."
    )
    sol = (
        f"**1. Description in words:** Translated **{dx} units to the right** and **{dy} units down**.\n\n"
        f"**2. Image Coordinates:**\n"
        f"\\[ C'({px} + {dx}; {py} - {dy}) = C'({tx}; {ty}) \\]"
    )
    ans = f"1. {dx} units right and {dy} units down; 2. ({tx}; {ty})"
    return {
        "id": f"g8_trans_comb_{rng.randint(100000, 999999)}",
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
        "subskill": "13_translation_combined_vector_rule",
        "learning_objective_id": "math_g8_trans_comb",
        "hints": {
            "tier_1": f"+{dx} on x means {dx} units right; -{dy} on y means {dy} units down.",
            "tier_2": f"Add {dx} to {px}; subtract {dy} from {py}.",
            "tier_3": f"C'({tx}; {ty}).",
        },
        "misconception_tags": ["swapping_horizontal_and_vertical_shifts"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 14. Translation of Triangle Vertices (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_14_translation_apply_rule_to_triangle_vertices(rng: random.Random) -> Dict[str, Any]:
    orig = [(-4, 1), (-1, 1), (-3, 3)]
    dx = rng.choice([3, 4, 5])
    dy = rng.choice([1, 2])
    trans = [(x + dx, y + dy) for x, y in orig]

    svg = draw_transformation_grid_svg(orig, trans, show_vector=True, seed=rng.randint(100, 999999))

    prompt = (
        f"Triangle \\(ABC\\) has vertices \\(A({orig[0][0]}; {orig[0][1]})\\), \\(B({orig[1][0]}; {orig[1][1]})\\), "
        f"and \\(C({orig[2][0]}; {orig[2][1]})\\).\n"
        f"The triangle is translated by the rule \\((x; y) \\to (x + {dx}; y + {dy})\\).\n\n"
        f"Determine the coordinates of image vertices \\(A'\\), \\(B'\\), and \\(C'\\)."
    )
    sol = (
        f"**Apply rule \\((x + {dx}; y + {dy})\\) to each vertex:**\n"
        f"- \\(A'({orig[0][0]} + {dx}; {orig[0][1]} + {dy}) = A'({trans[0][0]}; {trans[0][1]})\\)\n"
        f"- \\(B'({orig[1][0]} + {dx}; {orig[1][1]} + {dy}) = B'({trans[1][0]}; {trans[1][1]})\\)\n"
        f"- \\(C'({orig[2][0]} + {dx}; {orig[2][1]} + {dy}) = C'({trans[2][0]}; {trans[2][1]})\\)"
    )
    ans = f"A'({trans[0][0]}; {trans[0][1]}), B'({trans[1][0]}; {trans[1][1]}), C'({trans[2][0]}; {trans[2][1]})"
    return {
        "id": f"g8_trans_tri_rule_{rng.randint(100000, 999999)}",
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
        "subskill": "14_translation_apply_rule_to_triangle_vertices",
        "learning_objective_id": "math_g8_trans_tri_rule",
        "hints": {
            "tier_1": f"Add {dx} to each x-value; add {dy} to each y-value.",
            "tier_2": f"A' is ({-4 + dx}; {1 + dy}).",
            "tier_3": ans,
        },
        "misconception_tags": ["translating_only_one_vertex_instead_of_all_three"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 15. Determine Rule from Point and Image (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_15_translation_determine_rule_from_point_and_image(rng: random.Random) -> Dict[str, Any]:
    x1, y1 = rng.choice([1, 2, 3]), rng.choice([-1, 2, 4])
    dx = rng.choice([-3, -2, 2, 4])
    dy = rng.choice([-4, -2, 3, 5])
    x2, y2 = x1 + dx, y1 + dy

    sign_x = f"+ {dx}" if dx > 0 else f"- {abs(dx)}"
    sign_y = f"+ {dy}" if dy > 0 else f"- {abs(dy)}"

    prompt = (
        f"A point \\(T({x1}; {y1})\\) is translated to its image position \\(T'({x2}; {y2})\\).\n\n"
        f"1. Determine the algebraic translation rule in the format \\((x; y) \\to (x \\pm a; y \\pm b)\\).\n"
        f"2. Describe the movement in words."
    )
    word_x = f"{abs(dx)} units right" if dx > 0 else f"{abs(dx)} units left"
    word_y = f"{abs(dy)} units up" if dy > 0 else f"{abs(dy)} units down"
    sol = (
        f"**1. Algebraic Rule:**\n"
        f"\\[ a = x_2 - x_1 = {x2} - ({x1}) = {dx} \\]\n"
        f"\\[ b = y_2 - y_1 = {y2} - ({y1}) = {dy} \\]\n"
        f"Rule: \\((x; y) \\to (x {sign_x}; y {sign_y})\\)\n\n"
        f"**2. In words:** Translated {word_x} and {word_y}."
    )
    ans = f"1. (x {sign_x}; y {sign_y}); 2. {word_x} and {word_y}"
    return {
        "id": f"g8_trans_det_rule_{rng.randint(100000, 999999)}",
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
        "subskill": "15_translation_determine_rule_from_point_and_image",
        "learning_objective_id": "math_g8_trans_det_rule",
        "hints": {
            "tier_1": "Subtract original coordinates from image coordinates.",
            "tier_2": f"Horizontal change = {x2} - {x1}; vertical change = {y2} - {y1}.",
            "tier_3": f"(x {sign_x}; y {sign_y}).",
        },
        "misconception_tags": ["subtracting_image_from_original_inverting_vector_sign"],
    }


# ----------------------------------------------------------------------
# 16. Inverse Translation: Find Original from Image (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_16_translation_inverse_find_original_from_image(rng: random.Random) -> Dict[str, Any]:
    orig_x = rng.choice([-2, 1, 3])
    orig_y = rng.choice([-1, 2, 4])
    dx = rng.choice([3, 4, 5])
    dy = rng.choice([-2, -3, 2])
    img_x, img_y = orig_x + dx, orig_y + dy

    sign_x = f"+ {dx}" if dx > 0 else f"- {abs(dx)}"
    sign_y = f"+ {dy}" if dy > 0 else f"- {abs(dy)}"

    prompt = (
        f"Under the translation rule \\((x; y) \\to (x {sign_x}; y {sign_y})\\), the transformed point is \\(K'({img_x}; {img_y})\\).\n\n"
        f"1. Explain how to reverse the translation rule to find original point \\(K\\).\n"
        f"2. Determine the exact coordinates of original point \\(K\\)."
    )
    sol = (
        f"**1. Inverse Rule:** To reverse the translation, perform the inverse operations on coordinates \\(K'\\):\n"
        f"\\[ x = x' - ({dx}), \\quad y = y' - ({dy}) \\]\n\n"
        f"**2. Coordinates of K:**\n"
        f"\\[ x = {img_x} - ({dx}) = {orig_x} \\]\n"
        f"\\[ y = {img_y} - ({dy}) = {orig_y} \\]\n"
        f"Original point: \\(K({orig_x}; {orig_y})\\)."
    )
    ans = f"1. apply opposite operations (x' - dx; y' - dy); 2. K({orig_x}; {orig_y})"
    return {
        "id": f"g8_trans_inverse_{rng.randint(100000, 999999)}",
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
        "subskill": "16_translation_inverse_find_original_from_image",
        "learning_objective_id": "math_g8_trans_inverse",
        "hints": {
            "tier_1": "Reverse the operations: if rule adds 3, subtract 3 from K'.",
            "tier_2": f"x = {img_x} - ({dx}); y = {img_y} - ({dy}).",
            "tier_3": f"K({orig_x}; {orig_y}).",
        },
        "misconception_tags": ["applying_forward_rule_to_image_instead_of_inverse"],
    }


# ----------------------------------------------------------------------
# 17. Translation Preservation of Congruence (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_17_translation_preservation_of_congruence(rng: random.Random) -> Dict[str, Any]:
    shape = rng.choice(["triangle", "quadrilateral"])
    orig_area = rng.choice([12, 18, 24, 30])
    orig_perim = rng.choice([16, 20, 26])

    prompt = (
        f"A {shape} with perimeter **{orig_perim} cm** and area **{orig_area} cm²** is translated on a coordinate plane.\n\n"
        f"1. What is the perimeter and area of the translated {shape}?\n"
        f"2. State the geometric term describing why size and shape are completely preserved under a translation."
    )
    sol = (
        f"**1. Translated Perimeter and Area:**\n"
        f"- Translated Perimeter = **{orig_perim} cm**\n"
        f"- Translated Area = **{orig_area} cm²**\n\n"
        f"**2. Geometric Term:** A translation is an **isometry (rigid transformation)**, meaning the original figure "
        f"and its image are **congruent** (same size and shape; side lengths and interior angles remain identical)."
    )
    ans = f"1. perimeter = {orig_perim} cm, area = {orig_area} cm²; 2. isometry / congruent"
    return {
        "id": f"g8_trans_congruence_{rng.randint(100000, 999999)}",
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
        "subskill": "17_translation_preservation_of_congruence",
        "learning_objective_id": "math_g8_trans_congruence",
        "hints": {
            "tier_1": "Translation only moves the position; it does not stretch or shrink the figure.",
            "tier_2": "Perimeter and area remain exactly equal.",
            "tier_3": f"{orig_perim} cm, {orig_area} cm²; congruent / isometry.",
        },
        "misconception_tags": ["assuming_translation_changes_area_or_perimeter"],
    }


# ----------------------------------------------------------------------
# 18. Translation Word Problem Movement on Grid (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_18_translation_word_problem_movement_on_grid(rng: random.Random) -> Dict[str, Any]:
    x0, y0 = rng.choice([2, 3, 4]), rng.choice([1, 2, 3])
    east = rng.choice([3, 5, 6])
    north = rng.choice([2, 4])
    x_final = x0 + east
    y_final = y0 + north

    prompt = (
        f"A robot starts at coordinate position \\(S({x0}; {y0})\\) on a navigational system where "
        f"East corresponds to the positive x-direction and North corresponds to the positive y-direction.\n"
        f"The robot travels **{east} units East** and then **{north} units North**.\n\n"
        f"1. Write the translation vector rule representing this movement.\n"
        f"2. Calculate the robot's final coordinate position."
    )
    sol = (
        f"**1. Translation Rule:** East means \\(+{east}\\) in x; North means \\(+{north}\\) in y:\n"
        f"\\[ (x; y) \\to (x + {east}; y + {north}) \\]\n\n"
        f"**2. Final Position:**\n"
        f"\\[ ({x0} + {east}; {y0} + {north}) = ({x_final}; {y_final}) \\]"
    )
    ans = f"1. (x + {east}; y + {north}); 2. ({x_final}; {y_final})"
    return {
        "id": f"g8_trans_word_nav_{rng.randint(100000, 999999)}",
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
        "subskill": "18_translation_word_problem_movement_on_grid",
        "learning_objective_id": "math_g8_trans_word_nav",
        "hints": {
            "tier_1": "East increases x; North increases y.",
            "tier_2": f"x' = {x0} + {east}; y' = {y0} + {north}.",
            "tier_3": f"({x_final}; {y_final}).",
        },
        "misconception_tags": ["confusing_cardinal_directions_with_coordinate_axes"],
    }


# ----------------------------------------------------------------------
# 19. Translation Parallelogram Coordinates (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_19_translation_parallelogram_coordinates(rng: random.Random) -> Dict[str, Any]:
    orig = [(-4, -2), (-1, -2), (0, 0), (-3, 0)]
    dx = rng.choice([3, 4])
    dy = rng.choice([3, 4])
    trans = [(x + dx, y + dy) for x, y in orig]

    svg = draw_transformation_grid_svg(orig, trans, show_vector=True, seed=rng.randint(100, 999999))

    prompt = (
        f"Parallelogram \\(ABCD\\) has vertices \\(A(-4; -2)\\), \\(B(-1; -2)\\), \\(C(0; 0)\\), and \\(D(-3; 0)\\).\n"
        f"The parallelogram is translated according to the rule \\((x; y) \\to (x + {dx}; y + {dy})\\).\n\n"
        f"Determine the coordinates of image vertex \\(A'\\) and image vertex \\(C'\\)."
    )
    sol = (
        f"**Apply translation rule \\((x + {dx}; y + {dy})\\):**\n"
        f"- \\(A'(-4 + {dx}; -2 + {dy}) = A'({trans[0][0]}; {trans[0][1]})\\)\n"
        f"- \\(C'(0 + {dx}; 0 + {dy}) = C'({trans[2][0]}; {trans[2][1]})\\)"
    )
    ans = f"A'({trans[0][0]}; {trans[0][1]}), C'({trans[2][0]}; {trans[2][1]})"
    return {
        "id": f"g8_trans_parall_{rng.randint(100000, 999999)}",
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
        "subskill": "19_translation_parallelogram_coordinates",
        "learning_objective_id": "math_g8_trans_parall",
        "hints": {
            "tier_1": f"Add {dx} to x-coordinates and {dy} to y-coordinates.",
            "tier_2": f"A' is ({-4 + dx}; {-2 + dy}); C' is ({dx}; {dy}).",
            "tier_3": ans,
        },
        "misconception_tags": ["adding_translation_vector_to_only_one_coordinate"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 20. Coordinate Mapping Algebraic Notation (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_20_translation_coordinate_mapping_algebraic_notation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 5, 7])
    b = rng.choice([3, 4, 6])
    prompt = (
        f"A transformation is defined algebraically as \\(T: (x; y) \\to (x - {a}; y + {b})\\).\n\n"
        f"1. What type of geometric transformation does this rule represent?\n"
        f"2. If point \\(W(10; -4)\\) is mapped under \\(T\\), calculate the coordinates of \\(W'\\)."
    )
    wx, wy = 10 - a, -4 + b
    sol = (
        f"**1. Transformation Type:** A **translation** (horizontal translation of {a} units left and vertical translation of {b} units up).\n\n"
        f"**2. Coordinates of W':**\n"
        f"\\[ W'(10 - {a}; -4 + {b}) = W'({wx}; {wy}) \\]"
    )
    ans = f"1. translation; 2. ({wx}; {wy})"
    return {
        "id": f"g8_trans_notat_{rng.randint(100000, 999999)}",
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
        "subskill": "20_translation_coordinate_mapping_algebraic_notation",
        "learning_objective_id": "math_g8_trans_notat",
        "hints": {
            "tier_1": "Adding or subtracting constants from coordinates is a translation.",
            "tier_2": f"Substitute x = 10 and y = -4 into (x - {a}; y + {b}).",
            "tier_3": f"Translation; W'({wx}; {wy}).",
        },
        "misconception_tags": ["confusing_translation_notation_with_dilation_multiplication"],
    }


# ----------------------------------------------------------------------
# 21. Rotation 90° Clockwise About Origin (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_21_rotation_90_degrees_clockwise_origin(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([2, 3, 4])
    py = rng.choice([1, 2, 5])
    rx, ry = py, -px  # (x, y) -> (y, -x)
    svg = draw_transformation_grid_svg([(px, py)], [(rx, ry)], "P", "P'", seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(P({px}; {py})\\) is rotated **90° clockwise** about the origin \\((0; 0)\\) to position \\(P'\\).\n\n"
        f"1. State the coordinate mapping rule for a 90° clockwise rotation about the origin: \\((x; y) \\to (\\dots; \\dots)\\).\n"
        f"2. Write down the exact coordinates of image point \\(P'\\)."
    )
    sol = (
        f"**1. Mapping Rule:** A 90° clockwise rotation about the origin maps \\((x; y) \\to (y; -x)\\).\n\n"
        f"**2. Coordinates of P':**\n"
        f"\\[ P({px}; {py}) \\to P'({rx}; {ry}) \\]"
    )
    ans = f"1. (y; -x); 2. ({rx}; {ry})"
    return {
        "id": f"g8_trans_rot90_cw_{rng.randint(100000, 999999)}",
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
        "subskill": "21_rotation_90_degrees_clockwise_origin",
        "learning_objective_id": "math_g8_trans_rot90_cw",
        "hints": {
            "tier_1": "90° clockwise rotation: swap x and y, and negate the new y-coordinate: (y; -x).",
            "tier_2": f"New x is {py}; new y is -({px}).",
            "tier_3": f"P'({rx}; {ry}).",
        },
        "misconception_tags": ["negating_x_instead_of_y_for_clockwise_rotation"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 22. Rotation 90° Counter-Clockwise About Origin (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_22_rotation_90_degrees_counter_clockwise_origin(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([2, 3, 4])
    py = rng.choice([1, 2, 5])
    rx, ry = -py, px  # (x, y) -> (-y, x)
    svg = draw_transformation_grid_svg([(px, py)], [(rx, ry)], "Q", "Q'", seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(Q({px}; {py})\\) is rotated **90° counter-clockwise** (anti-clockwise) about the origin to point \\(Q'\\).\n\n"
        f"1. State the coordinate mapping rule for a 90° counter-clockwise rotation about the origin: \\((x; y) \\to (\\dots; \\dots)\\).\n"
        f"2. Determine the exact coordinates of image point \\(Q'\\)."
    )
    sol = (
        f"**1. Mapping Rule:** A 90° counter-clockwise rotation about the origin maps \\((x; y) \\to (-y; x)\\).\n\n"
        f"**2. Coordinates of Q':**\n"
        f"\\[ Q({px}; {py}) \\to Q'({rx}; {ry}) \\]"
    )
    ans = f"1. (-y; x); 2. ({rx}; {ry})"
    return {
        "id": f"g8_trans_rot90_ccw_{rng.randint(100000, 999999)}",
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
        "subskill": "22_rotation_90_degrees_counter_clockwise_origin",
        "learning_objective_id": "math_g8_trans_rot90_ccw",
        "hints": {
            "tier_1": "90° counter-clockwise rotation: swap x and y, and negate the new x-coordinate: (-y; x).",
            "tier_2": f"New x is -({py}); new y is {px}.",
            "tier_3": f"Q'({rx}; {ry}).",
        },
        "misconception_tags": ["confusing_clockwise_and_counter_clockwise_rotation_rules"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 23. Rotation 180° About Origin Half-Turn (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_23_rotation_180_degrees_origin_half_turn(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([2, 3, 4])
    py = rng.choice([1, 2, 4])
    rx, ry = -px, -py  # (x, y) -> (-x, -y)
    svg = draw_transformation_grid_svg([(px, py)], [(rx, ry)], "R", "R'", seed=rng.randint(100, 999999))

    prompt = (
        f"Point \\(R({px}; {py})\\) is rotated **180°** (half-turn) about the origin to image point \\(R'\\).\n\n"
        f"1. State the coordinate mapping rule for a 180° rotation about the origin: \\((x; y) \\to (\\dots; \\dots)\\).\n"
        f"2. Write down the coordinates of image point \\(R'\\)."
    )
    sol = (
        f"**1. Mapping Rule:** A 180° rotation about the origin maps \\((x; y) \\to (-x; -y)\\). Both coordinates change sign.\n\n"
        f"**2. Coordinates of R':**\n"
        f"\\[ R({px}; {py}) \\to R'({rx}; {ry}) \\]"
    )
    ans = f"1. (-x; -y); 2. ({rx}; {ry})"
    return {
        "id": f"g8_trans_rot180_{rng.randint(100000, 999999)}",
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
        "subskill": "23_rotation_180_degrees_origin_half_turn",
        "learning_objective_id": "math_g8_trans_rot180",
        "hints": {
            "tier_1": "A 180° rotation inverts the sign of both coordinates: (-x; -y).",
            "tier_2": f"Negate {px} and {py}.",
            "tier_3": f"R'({rx}; {ry}).",
        },
        "misconception_tags": ["swapping_coordinates_during_180_degree_rotation"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 24. Rotation of Triangle Vertices 90° Clockwise (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_24_rotation_triangle_vertices_90_clockwise(rng: random.Random) -> Dict[str, Any]:
    dx = rng.choice([0, 1])
    dy = rng.choice([0, 1])
    orig = [(1 + dx, 2 + dy), (4 + dx, 1 + dy), (3 + dx, 4 + dy)]
    trans = [(y, -x) for x, y in orig]
    svg = draw_transformation_grid_svg(orig, trans, seed=rng.randint(100, 999999))

    prompt = (
        f"Triangle \\(ABC\\) has vertices \\(A({orig[0][0]}; {orig[0][1]})\\), \\(B({orig[1][0]}; {orig[1][1]})\\), and \\(C({orig[2][0]}; {orig[2][1]})\\).\n"
        f"The triangle is rotated **90° clockwise** about the origin to form \\(\\triangle A'B'C'\\).\n\n"
        f"Calculate the coordinates of image vertices \\(A'\\), \\(B'\\), and \\(C'\\)."
    )
    sol = (
        f"**Apply 90° clockwise rule \\((x; y) \\to (y; -x)\\):**\n"
        f"- \\(A({orig[0][0]}; {orig[0][1]}) \\to A'({trans[0][0]}; {trans[0][1]})\\)\n"
        f"- \\(B({orig[1][0]}; {orig[1][1]}) \\to B'({trans[1][0]}; {trans[1][1]})\\)\n"
        f"- \\(C({orig[2][0]}; {orig[2][1]}) \\to C'({trans[2][0]}; {trans[2][1]})\\)"
    )
    ans = f"A'({trans[0][0]}; {trans[0][1]}), B'({trans[1][0]}; {trans[1][1]}), C'({trans[2][0]}; {trans[2][1]})"
    return {
        "id": f"g8_trans_rot_tri_90_{rng.randint(100000, 999999)}",
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
        "subskill": "24_rotation_triangle_vertices_90_clockwise",
        "learning_objective_id": "math_g8_trans_rot_tri_90",
        "hints": {
            "tier_1": "For 90° clockwise, (x; y) -> (y; -x).",
            "tier_2": f"A' is ({orig[0][1]}; {-orig[0][0]}). Apply same to B and C.",
            "tier_3": ans,
        },
        "misconception_tags": ["negating_first_coordinate_instead_of_second"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 25. Rotation of Triangle Vertices 180° (WITH SVG GRID)
# ----------------------------------------------------------------------
def arch_25_rotation_triangle_vertices_180_degrees(rng: random.Random) -> Dict[str, Any]:
    dx = rng.choice([0, 1])
    dy = rng.choice([0, 1])
    orig = [(1 + dx, 1 + dy), (3 + dx, 1 + dy), (2 + dx, 4 + dy)]
    trans = [(-x, -y) for x, y in orig]
    svg = draw_transformation_grid_svg(orig, trans, seed=rng.randint(100, 999999))

    prompt = (
        f"Triangle \\(ABC\\) has vertices \\(A({orig[0][0]}; {orig[0][1]})\\), \\(B({orig[1][0]}; {orig[1][1]})\\), and \\(C({orig[2][0]}; {orig[2][1]})\\).\n"
        f"The triangle undergoes a **180° rotation** about the origin \\((0; 0)\\).\n\n"
        f"Write down the coordinates of image vertices \\(A'\\), \\(B'\\), and \\(C'\\)."
    )
    sol = (
        f"**Apply 180° rotation rule \\((x; y) \\to (-x; -y)\\):**\n"
        f"- \\(A({orig[0][0]}; {orig[0][1]}) \\to A'({trans[0][0]}; {trans[0][1]})\\)\n"
        f"- \\(B({orig[1][0]}; {orig[1][1]}) \\to B'({trans[1][0]}; {trans[1][1]})\\)\n"
        f"- \\(C({orig[2][0]}; {orig[2][1]}) \\to C'({trans[2][0]}; {trans[2][1]})\\)"
    )
    ans = f"A'({trans[0][0]}; {trans[0][1]}), B'({trans[1][0]}; {trans[1][1]}), C'({trans[2][0]}; {trans[2][1]})"
    return {
        "id": f"g8_trans_rot_tri_180_{rng.randint(100000, 999999)}",
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
        "subskill": "25_rotation_triangle_vertices_180_degrees",
        "learning_objective_id": "math_g8_trans_rot_tri_180",
        "hints": {
            "tier_1": "A 180° rotation negates both x and y coordinates.",
            "tier_2": f"A'({-orig[0][0]}; {-orig[0][1]}), B'({-orig[1][0]}; {-orig[1][1]}), C'({-orig[2][0]}; {-orig[2][1]}).",
            "tier_3": ans,
        },
        "misconception_tags": ["forgetting_to_negate_one_of_the_coordinates"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }
