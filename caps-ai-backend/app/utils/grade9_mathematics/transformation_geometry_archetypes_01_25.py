"""Grade 9 Mathematics — Transformation Geometry Archetypes 01 to 25 (CAPS Term 3).
Symmetry, Translations, Reflections, and Rotations on the Cartesian Plane.
100% AST Pure: SymPy / Python math only, zero LLM authority.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.grade9_mathematics.transformation_geometry_svg import (
    draw_transformation_grid_svg,
    draw_symmetry_polygon_svg,
)


def _fmt_pt(x: float | int, y: float | int) -> str:
    """Format point as (x; y) with South African semicolon notation."""
    def _c(v: float | int) -> str:
        if isinstance(v, float) and v.is_integer():
            v = int(v)
        return str(v).replace(".", ",")
    return f"({_c(x)}; {_c(y)})"


# -----------------------------------------------------------------------------
# Archetype 01: Lines of Symmetry of Regular Polygons
# -----------------------------------------------------------------------------
def arch_01_symmetry_lines_regular_polygons(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("equilateral_triangle", "equilateral triangle", 3),
        ("square", "square", 4),
        ("regular_pentagon", "regular pentagon", 5),
        ("regular_hexagon", "regular hexagon", 6),
    ]
    poly_type, name, n_lines = rng.choice(choices)
    svg = draw_symmetry_polygon_svg(poly_type, show_lines=True, seed=seed)

    prompt = (
        f"Consider the regular 2D polygon shown in the diagram ({name}). "
        f"Determine the total number of lines (axes) of symmetry that this regular polygon possesses."
    )
    sol = (
        f"A regular polygon with $n$ equal sides and $n$ equal interior angles has exactly $n$ lines of symmetry.\n"
        f"An {name} has $n = {n_lines}$ equal sides, each line of symmetry passing through vertices and/or midpoints of opposite sides.\n"
        f"Therefore, the total number of lines of symmetry is ${n_lines}$."
    )

    return {
        "subskill": "01_symmetry_lines_regular_polygons",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(n_lines),
        "expected_answer": str(n_lines),
        "sample_answer": str(n_lines),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State formula or property for regular polygon with {n_lines} sides", "marks": 1},
            {"desc": f"Correct number of lines of symmetry: {n_lines}", "marks": 1},
        ],
        "hints": [
            "A line of symmetry folds a figure into two congruent halves that match exactly.",
            f"A regular polygon with $n$ sides has $n$ lines of symmetry.",
            f"For an {name}, the number of lines of symmetry is {n_lines}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 02: Lines of Symmetry of Special Quadrilaterals
# -----------------------------------------------------------------------------
def arch_02_symmetry_lines_quadrilaterals(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("rectangle", "rectangle (non-square)", 2, "2 lines connecting the midpoints of opposite sides (diagonals are not lines of symmetry)."),
        ("rhombus", "rhombus (non-square)", 2, "2 lines along its diagonals (which intersect perpendicularly)."),
        ("kite", "kite", 1, "1 line along the main diagonal connecting the vertices between the equal sides."),
        ("parallelogram", "general parallelogram (non-rhombus, non-rectangle)", 0, "0 lines of symmetry (it possesses rotational symmetry of order 2, but no reflection symmetry)."),
    ]
    poly_type, name, n_lines, reason = rng.choice(choices)
    svg = draw_symmetry_polygon_svg(poly_type, show_lines=(n_lines > 0), seed=seed)

    prompt = (
        f"Examine the geometric quadrilateral shown in the diagram ({name}). "
        f"How many lines of symmetry does this quadrilateral have?"
    )
    sol = (
        f"For a {name}:\n"
        f"It has {n_lines} line(s) of symmetry: {reason}\n"
        f"Therefore, the number of lines of symmetry is ${n_lines}$."
    )

    return {
        "subskill": "02_symmetry_lines_quadrilaterals",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(n_lines),
        "expected_answer": str(n_lines),
        "sample_answer": str(n_lines),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify geometric symmetry properties of quadrilateral", "marks": 1},
            {"desc": f"State correct number of lines of symmetry: {n_lines}", "marks": 1},
        ],
        "hints": [
            "Consider folding the shape along lines joining midpoints of sides or along its diagonals.",
            f"Recall the symmetry classification for a {name}.",
            f"The answer is {n_lines}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 03: Order of Rotational Symmetry
# -----------------------------------------------------------------------------
def arch_03_rotational_symmetry_order(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("equilateral_triangle", "equilateral triangle", 3, 120),
        ("square", "square", 4, 90),
        ("regular_pentagon", "regular pentagon", 5, 72),
        ("regular_hexagon", "regular hexagon", 6, 60),
        ("rectangle", "rectangle", 2, 180),
        ("rhombus", "rhombus", 2, 180),
        ("parallelogram", "parallelogram", 2, 180),
    ]
    poly_type, name, order, angle = rng.choice(choices)
    svg = draw_symmetry_polygon_svg(poly_type, show_lines=False, seed=seed)

    prompt = (
        f"Refer to the 2D figure shown in the diagram ({name}). "
        f"State its order of rotational symmetry during a complete $360^\\circ$ revolution about its center."
    )
    sol = (
        f"The order of rotational symmetry is the number of times a shape fits onto itself during one full rotation ($360^\\circ$).\n"
        f"A {name} rotates onto itself every ${angle}^\\circ$.\n"
        f"$\\text{{Order}} = \\frac{{360^\\circ}}{{{angle}^\\circ}} = {order}$.\n"
        f"Therefore, the order of rotational symmetry is ${order}$."
    )

    return {
        "subskill": "03_rotational_symmetry_order",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(order),
        "expected_answer": str(order),
        "sample_answer": str(order),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "State definition or formula for rotational symmetry order", "marks": 1},
            {"desc": f"Correct order of rotational symmetry: {order}", "marks": 1},
        ],
        "hints": [
            "How many times does the shape look identical to its initial position in a 360° turn?",
            f"The minimum angle of rotation is {angle}°.",
            f"Order = 360° / {angle}° = {order}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 04: Translation of a Point Along a Single Axis
# -----------------------------------------------------------------------------
def arch_04_translation_point_single_axis(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.randint(-4, 4)
    y = rng.randint(-4, 4)
    axis = rng.choice(["horizontal", "vertical"])

    if axis == "horizontal":
        shift = rng.choice([-4, -3, -2, 2, 3, 4])
        xp, yp = x + shift, y
        direction = f"{abs(shift)} units to the {'right' if shift > 0 else 'left'}"
        rule_str = f"(x {shift:+d}; y)"
    else:
        shift = rng.choice([-4, -3, -2, 2, 3, 4])
        xp, yp = x, y + shift
        direction = f"{abs(shift)} units {'upwards' if shift > 0 else 'downwards'}"
        rule_str = f"(x; y {shift:+d})"

    ans_str = _fmt_pt(xp, yp)
    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="translation",
        seed=seed,
        title=f"Translation: {direction}",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is translated {direction} "
        f"according to the rule $(x; y) \\to {rule_str}$. "
        f"Determine the coordinates of the image point $P'$ in the format $(x; y)$."
    )
    sol = (
        f"Applying the translation rule $(x; y) \\to {rule_str}$:\n"
        f"$x' = {x} {'+ ' + str(shift) if shift > 0 and axis == 'horizontal' else ('- ' + str(abs(shift)) if axis == 'horizontal' else '')} = {xp}$\n"
        f"$y' = {y} {'+ ' + str(shift) if shift > 0 and axis == 'vertical' else ('- ' + str(abs(shift)) if axis == 'vertical' else '')} = {yp}$\n"
        f"Thus, the coordinates of the image point are $P'{ans_str}$."
    )

    return {
        "subskill": "04_translation_point_single_axis",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply translation shift to target coordinate", "marks": 1},
            {"desc": f"State final image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Translating {direction} changes only the {'x' if axis == 'horizontal' else 'y'}-coordinate.",
            f"Add {shift} to the {'x' if axis == 'horizontal' else 'y'}-coordinate of ({x}; {y}).",
            f"Image point P' is {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 05: Translation of a Point Along Both Axes
# -----------------------------------------------------------------------------
def arch_05_translation_point_both_axes(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.randint(-4, 3)
    y = rng.randint(-4, 3)
    dx = rng.choice([-3, -2, -1, 1, 2, 3])
    dy = rng.choice([-3, -2, -1, 1, 2, 3])
    xp, yp = x + dx, y + dy
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="translation",
        seed=seed,
        title=f"Translation: (x; y) -> (x {dx:+d}; y {dy:+d})",
    )

    prompt = (
        f"Point $P{_fmt_pt(x, y)}$ is translated according to the rule "
        f"$(x; y) \\to (x {dx:+d}; y {dy:+d})$. "
        f"Determine the coordinates of the image point $P'$ in the format $(x; y)$."
    )
    sol = (
        f"Given translation rule: $(x; y) \\to (x {dx:+d}; y {dy:+d})$:\n"
        f"$x' = x {dx:+d} = {x} {dx:+d} = {xp}$\n"
        f"$y' = y {dy:+d} = {y} {dy:+d} = {yp}$\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "05_translation_point_both_axes",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Substitute x and y into algebraic translation rule", "marks": 1},
            {"desc": f"Correct coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Add {dx} to the x-coordinate: {x} + ({dx}) = {xp}.",
            f"Add {dy} to the y-coordinate: {y} + ({dy}) = {yp}.",
            f"The image coordinates are {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 06: Determine Translation Vector from Coordinates
# -----------------------------------------------------------------------------
def arch_06_translation_find_vector(rng: random.Random, seed: int) -> Dict[str, Any]:
    x1 = rng.randint(-4, 3)
    y1 = rng.randint(-4, 3)
    dx = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    dy = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    x2, y2 = x1 + dx, y1 + dy

    svg = draw_transformation_grid_svg(
        pre_image=[(x1, y1)],
        image=[(x2, y2)],
        pre_labels=[f"A({x1}; {y1})"],
        image_labels=[f"A'({x2}; {y2})"],
        transformation_type="translation",
        seed=seed,
        title="Find Translation Rule",
    )

    rule_str = f"(x {dx:+d}; y {dy:+d})"
    prompt = (
        f"In the Cartesian plane diagram, point $A{_fmt_pt(x1, y1)}$ is translated to its image $A'{_fmt_pt(x2, y2)}$. "
        f"State the algebraic translation rule in the format $(x; y) \\to (x \\pm a; y \\pm b)$."
    )
    sol = (
        f"To find the horizontal shift $a$ and vertical shift $b$:\n"
        f"$a = x' - x = {x2} - ({x1}) = {dx}$\n"
        f"$b = y' - y = {y2} - ({y1}) = {dy}$\n"
        f"Therefore, the translation rule is $(x; y) \\to {rule_str}$."
    )

    return {
        "subskill": "06_translation_find_vector",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": rule_str,
        "expected_answer": rule_str,
        "sample_answer": rule_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Calculate horizontal shift dx and vertical shift dy", "marks": 1},
            {"desc": f"State full mapping rule {rule_str}", "marks": 1},
        ],
        "hints": [
            "Find the difference in x-coordinates: x_image - x_original.",
            "Find the difference in y-coordinates: y_image - y_original.",
            f"Rule: (x; y) -> {rule_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 07: Find Pre-Image Under Translation (Inverse Translation)
# -----------------------------------------------------------------------------
def arch_07_translation_find_preimage(rng: random.Random, seed: int) -> Dict[str, Any]:
    x_orig = rng.randint(-3, 3)
    y_orig = rng.randint(-3, 3)
    dx = rng.choice([-3, -2, -1, 1, 2, 3])
    dy = rng.choice([-3, -2, -1, 1, 2, 3])
    xp, yp = x_orig + dx, y_orig + dy
    ans_str = _fmt_pt(x_orig, y_orig)

    svg = draw_transformation_grid_svg(
        pre_image=[(x_orig, y_orig)],
        image=[(xp, yp)],
        pre_labels=[f"P({x_orig}; {y_orig})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="translation",
        seed=seed,
        title="Inverse Translation: Find P",
    )

    prompt = (
        f"A point $P(x; y)$ was translated according to the rule $(x; y) \\to (x {dx:+d}; y {dy:+d})$ "
        f"to arrive at the image point $P'{_fmt_pt(xp, yp)}$. "
        f"Determine the coordinates of the original point $P$."
    )
    sol = (
        f"The translation rule is $x' = x {dx:+d}$ and $y' = y {dy:+d}$.\n"
        f"To find the original coordinates $(x; y)$, reverse the translation:\n"
        f"$x = x' - ({dx}) = {xp} - ({dx}) = {x_orig}$\n"
        f"$y = y' - ({dy}) = {yp} - ({dy}) = {y_orig}$\n"
        f"Therefore, the original pre-image coordinates are $P{ans_str}$."
    )

    return {
        "subskill": "07_translation_find_preimage",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Invert the translation equations to solve for x and y", "marks": 1},
            {"desc": f"Correct original coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "To reverse a translation, subtract the shifts from the image coordinates.",
            f"x = {xp} - ({dx}) and y = {yp} - ({dy}).",
            f"The original point is P{ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 08: Translate Triangle Vertices
# -----------------------------------------------------------------------------
def arch_08_translation_triangle_vertices(rng: random.Random, seed: int) -> Dict[str, Any]:
    # Triangle ABC
    x1, y1 = rng.randint(-4, 1), rng.randint(-4, 1)
    x2, y2 = x1 + rng.randint(2, 4), y1
    x3, y3 = x1 + rng.randint(1, 3), y1 + rng.randint(2, 4)

    dx = rng.choice([-3, -2, 2, 3])
    dy = rng.choice([-3, -2, 2, 3])

    axp, ayp = x1 + dx, y1 + dy
    bxp, byp = x2 + dx, y2 + dy
    cxp, cyp = x3 + dx, y3 + dy

    pre_pts = [(x1, y1), (x2, y2), (x3, y3)]
    img_pts = [(axp, ayp), (bxp, byp), (cxp, cyp)]

    svg = draw_transformation_grid_svg(
        pre_image=pre_pts,
        image=img_pts,
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="translation",
        seed=seed,
        title=f"Translate Triangle ABC: (x {dx:+d}; y {dy:+d})",
    )

    ans_str = f"A'{_fmt_pt(axp, ayp)}, B'{_fmt_pt(bxp, byp)}, C'{_fmt_pt(cxp, cyp)}"
    prompt = (
        f"In the Cartesian plane diagram, triangle $\\triangle ABC$ with vertices "
        f"$A{_fmt_pt(x1, y1)}$, $B{_fmt_pt(x2, y2)}$, and $C{_fmt_pt(x3, y3)}$ is translated by the rule "
        f"$(x; y) \\to (x {dx:+d}; y {dy:+d})$. "
        f"State the coordinates of the image vertices $A', B', C'$."
    )
    sol = (
        f"Applying the translation $(x; y) \\to (x {dx:+d}; y {dy:+d})$ to each vertex:\n"
        f"$A{_fmt_pt(x1, y1)} \\to A'({x1}{dx:+d}; {y1}{dy:+d}) = A'{_fmt_pt(axp, ayp)}$\n"
        f"$B{_fmt_pt(x2, y2)} \\to B'({x2}{dx:+d}; {y2}{dy:+d}) = B'{_fmt_pt(bxp, byp)}$\n"
        f"$C{_fmt_pt(x3, y3)} \\to C'({x3}{dx:+d}; {y3}{dy:+d}) = C'{_fmt_pt(cxp, cyp)}$\n"
        f"Therefore, the image vertices are {ans_str}."
    )

    return {
        "subskill": "08_translation_triangle_vertices",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Correct coordinates for A': {_fmt_pt(axp, ayp)}", "marks": 1},
            {"desc": f"Correct coordinates for B': {_fmt_pt(bxp, byp)}", "marks": 1},
            {"desc": f"Correct coordinates for C': {_fmt_pt(cxp, cyp)}", "marks": 1},
        ],
        "hints": [
            f"Add {dx} to every x-coordinate and {dy} to every y-coordinate.",
            f"A': ({x1} + {dx}; {y1} + {dy}) = {_fmt_pt(axp, ayp)}.",
            f"Full answer: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 09: Translation Isometry & Invariance Properties
# -----------------------------------------------------------------------------
def arch_09_translation_properties_isometry(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("Are the corresponding side lengths of the original figure and its image equal after a translation?", "Yes", "Translation is an isometry (rigid transformation) that preserves distance; hence side lengths remain equal."),
        ("Does a translation change the size of the interior angles of a polygon?", "No", "Translations preserve angle measures; corresponding angles in pre-image and image are strictly equal."),
        ("Are the line segments connecting corresponding vertices (e.g. AA' and BB') parallel and equal in length?", "Yes", "All points of the figure move in the same direction by the exact same distance along parallel vectors."),
        ("Is the image figure congruent to the original figure under a translation?", "Yes", "Because both side lengths and angle sizes are preserved, the image is congruent to the original figure."),
    ]
    q_text, ans, reason = rng.choice(choices)

    # Illustrative triangle translation
    svg = draw_transformation_grid_svg(
        pre_image=[(-3, -2), (-1, -2), (-2, 1)],
        image=[(1, 1), (3, 1), (2, 4)],
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="translation",
        seed=seed,
        title="Translation Properties (Isometry)",
    )

    prompt = f"Refer to the translation of the polygon shown in the diagram. {q_text} (Answer 'Yes' or 'No')."
    sol = f"{ans}.\nReason: {reason}"

    return {
        "subskill": "09_translation_properties_isometry",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": f"{ans} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct binary response: {ans}", "marks": 1},
            {"desc": "Provide geometric property justification", "marks": 1},
        ],
        "hints": [
            "A translation slides a figure without rotating, flipping, or resizing it.",
            "Translations preserve both side lengths and interior angle measures (rigid motion).",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 10: Reflection of a Point in the x-axis
# -----------------------------------------------------------------------------
def arch_10_reflection_point_x_axis(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    y = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    xp, yp = x, -y
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="reflection",
        mirror_line="x_axis",
        seed=seed,
        title="Reflection across the x-axis",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is reflected across the $x$-axis. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"The reflection rule for reflection across the $x$-axis is $(x; y) \\to (x; -y)$.\n"
        f"Here, $x = {x}$ and $y = {y}$.\n"
        f"$x' = {x}$\n"
        f"$y' = -({y}) = {yp}$\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "10_reflection_point_x_axis",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply x-axis reflection rule (x; -y)", "marks": 1},
            {"desc": f"State correct image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "In an x-axis reflection, the x-coordinate stays the same and the y-coordinate changes sign.",
            f"x' = {x}, y' = -({y}).",
            f"Image coordinates: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 11: Reflection of a Point in the y-axis
# -----------------------------------------------------------------------------
def arch_11_reflection_point_y_axis(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    y = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    xp, yp = -x, y
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="reflection",
        mirror_line="y_axis",
        seed=seed,
        title="Reflection across the y-axis",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is reflected across the $y$-axis. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"The reflection rule for reflection across the $y$-axis is $(x; y) \\to (-x; y)$.\n"
        f"Here, $x = {x}$ and $y = {y}$.\n"
        f"$x' = -({x}) = {xp}$\n"
        f"$y' = {y}$\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "11_reflection_point_y_axis",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply y-axis reflection rule (-x; y)", "marks": 1},
            {"desc": f"State correct image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "In a y-axis reflection, the y-coordinate stays the same and the x-coordinate changes sign.",
            f"x' = -({x}), y' = {y}.",
            f"Image coordinates: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 12: Reflection in the Line y = x
# -----------------------------------------------------------------------------
def arch_12_reflection_point_line_y_equals_x(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    y = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    while y == x:
        y = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

    xp, yp = y, x
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="reflection",
        mirror_line="y=x",
        seed=seed,
        title="Reflection in the line y = x",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is reflected across the line $y = x$. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"The reflection rule across the diagonal line $y = x$ swaps the coordinates: $(x; y) \\to (y; x)$.\n"
        f"Original point $P({x}; {y}) \\implies x' = {y}$ and $y' = {x}$.\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "12_reflection_point_line_y_equals_x",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply diagonal line reflection rule (x; y) -> (y; x)", "marks": 1},
            {"desc": f"State swapped coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "Reflecting across the line y = x interchanges the x and y coordinates.",
            f"The old y-coordinate ({y}) becomes the new x-coordinate.",
            f"Image coordinates: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 13: Reflection in the Line y = -x
# -----------------------------------------------------------------------------
def arch_13_reflection_point_line_y_equals_neg_x(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    while y == -x:
        y = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])

    xp, yp = -y, -x
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="reflection",
        mirror_line="y=-x",
        seed=seed,
        title="Reflection in the line y = -x",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is reflected across the line $y = -x$. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"The reflection rule across the line $y = -x$ is $(x; y) \\to (-y; -x)$.\n"
        f"Original coordinates: $x = {x}$ and $y = {y}$.\n"
        f"$x' = -y = -({y}) = {xp}$\n"
        f"$y' = -x = -({x}) = {yp}$\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "13_reflection_point_line_y_equals_neg_x",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply coordinate reflection rule (x; y) -> (-y; -x)", "marks": 1},
            {"desc": f"State correct image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "Reflecting across y = -x swaps coordinates and negates both.",
            f"x' = -({y}) = {xp}, y' = -({x}) = {yp}.",
            f"The image point is {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 14: Reflection Across a Horizontal Line y = c
# -----------------------------------------------------------------------------
def arch_14_reflection_point_horizontal_line(rng: random.Random, seed: int) -> Dict[str, Any]:
    c = rng.choice([-2, -1, 1, 2])
    x = rng.randint(-4, 4)
    dy = rng.choice([-3, -2, 2, 3])
    y = c + dy
    yp = c - dy  # 2c - y
    xp = x
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="reflection",
        mirror_line="y=c",
        mirror_c=c,
        seed=seed,
        title=f"Reflection in horizontal line y = {c}",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is reflected across the horizontal line $y = {c}$. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"For a reflection across the horizontal line $y = c$:\n"
        f"The $x$-coordinate remains unchanged: $x' = {x}$.\n"
        f"The distance from $P$ to the line is $|{y} - ({c})| = {abs(dy)}$ units.\n"
        f"The image $P'$ lies the same distance on the opposite side of the line:\n"
        f"$y' = 2c - y = 2({c}) - ({y}) = {2*c - y} = {yp}$.\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "14_reflection_point_horizontal_line",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Keep x = {x} unchanged and compute distance from y = {c}", "marks": 1},
            {"desc": f"Correct image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "A horizontal mirror line keeps the x-coordinate unchanged.",
            f"Distance to mirror line y = {c}: |{y} - {c}| = {abs(dy)}.",
            f"Image point: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 15: Reflection Across a Vertical Line x = c
# -----------------------------------------------------------------------------
def arch_15_reflection_point_vertical_line(rng: random.Random, seed: int) -> Dict[str, Any]:
    c = rng.choice([-2, -1, 1, 2])
    y = rng.randint(-4, 4)
    dx = rng.choice([-3, -2, 2, 3])
    x = c + dx
    xp = c - dx  # 2c - x
    yp = y
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="reflection",
        mirror_line="x=c",
        mirror_c=c,
        seed=seed,
        title=f"Reflection in vertical line x = {c}",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is reflected across the vertical line $x = {c}$. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"For a reflection across the vertical line $x = c$:\n"
        f"The $y$-coordinate remains unchanged: $y' = {y}$.\n"
        f"The distance from $P$ to the vertical mirror line is $|{x} - ({c})| = {abs(dx)}$ units.\n"
        f"The image $P'$ is placed at the same distance on the opposite side:\n"
        f"$x' = 2c - x = 2({c}) - ({x}) = {2*c - x} = {xp}$.\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "15_reflection_point_vertical_line",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Keep y = {y} unchanged and apply 2c - x", "marks": 1},
            {"desc": f"Correct image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "A vertical mirror line keeps the y-coordinate unchanged.",
            f"Distance to mirror line x = {c}: |{x} - {c}| = {abs(dx)}.",
            f"Image point: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 16: Reflection of a Triangle Across the x-axis
# -----------------------------------------------------------------------------
def arch_16_reflection_triangle_x_axis(rng: random.Random, seed: int) -> Dict[str, Any]:
    x1, y1 = rng.randint(-4, 1), rng.randint(1, 4)
    x2, y2 = x1 + rng.randint(2, 4), y1
    x3, y3 = x1 + rng.randint(1, 3), y1 + rng.randint(1, 3)

    pre_pts = [(x1, y1), (x2, y2), (x3, y3)]
    img_pts = [(x1, -y1), (x2, -y2), (x3, -y3)]

    svg = draw_transformation_grid_svg(
        pre_image=pre_pts,
        image=img_pts,
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="reflection",
        mirror_line="x_axis",
        seed=seed,
        title="Triangle Reflection in x-axis",
    )

    ans_str = f"A'{_fmt_pt(x1, -y1)}, B'{_fmt_pt(x2, -y2)}, C'{_fmt_pt(x3, -y3)}"
    prompt = (
        f"Triangle $\\triangle ABC$ has vertices $A{_fmt_pt(x1, y1)}$, $B{_fmt_pt(x2, y2)}$, and $C{_fmt_pt(x3, y3)}$. "
        f"The triangle is reflected across the $x$-axis. "
        f"Determine the coordinates of the image vertices $A', B', C'$."
    )
    sol = (
        f"Under reflection across the $x$-axis, the rule is $(x; y) \\to (x; -y)$:\n"
        f"$A{_fmt_pt(x1, y1)} \\to A'{_fmt_pt(x1, -y1)}$\n"
        f"$B{_fmt_pt(x2, y2)} \\to B'{_fmt_pt(x2, -y2)}$\n"
        f"$C{_fmt_pt(x3, y3)} \\to C'{_fmt_pt(x3, -y3)}$\n"
        f"Therefore, the image vertices are {ans_str}."
    )

    return {
        "subskill": "16_reflection_triangle_x_axis",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Correct coordinates for A': {_fmt_pt(x1, -y1)}", "marks": 1},
            {"desc": f"Correct coordinates for B': {_fmt_pt(x2, -y2)}", "marks": 1},
            {"desc": f"Correct coordinates for C': {_fmt_pt(x3, -y3)}", "marks": 1},
        ],
        "hints": [
            "In an x-axis reflection, keep the x-coordinate identical and negate the y-coordinate.",
            f"A' = ({x1}; -{y1}).",
            f"Full answer: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 17: Reflection of a Triangle Across the y-axis
# -----------------------------------------------------------------------------
def arch_17_reflection_triangle_y_axis(rng: random.Random, seed: int) -> Dict[str, Any]:
    x1, y1 = rng.randint(1, 4), rng.randint(-3, 2)
    x2, y2 = x1 + rng.randint(1, 3), y1
    x3, y3 = x1, y1 + rng.randint(2, 4)

    pre_pts = [(x1, y1), (x2, y2), (x3, y3)]
    img_pts = [(-x1, y1), (-x2, y2), (-x3, y3)]

    svg = draw_transformation_grid_svg(
        pre_image=pre_pts,
        image=img_pts,
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="reflection",
        mirror_line="y_axis",
        seed=seed,
        title="Triangle Reflection in y-axis",
    )

    ans_str = f"A'{_fmt_pt(-x1, y1)}, B'{_fmt_pt(-x2, y2)}, C'{_fmt_pt(-x3, y3)}"
    prompt = (
        f"Triangle $\\triangle ABC$ with vertices $A{_fmt_pt(x1, y1)}$, $B{_fmt_pt(x2, y2)}$, and $C{_fmt_pt(x3, y3)}$ "
        f"is reflected across the $y$-axis. "
        f"Determine the coordinates of the image vertices $A', B', C'$."
    )
    sol = (
        f"The reflection rule across the $y$-axis is $(x; y) \\to (-x; y)$:\n"
        f"$A{_fmt_pt(x1, y1)} \\to A'{_fmt_pt(-x1, y1)}$\n"
        f"$B{_fmt_pt(x2, y2)} \\to B'{_fmt_pt(-x2, y2)}$\n"
        f"$C{_fmt_pt(x3, y3)} \\to C'{_fmt_pt(-x3, y3)}$\n"
        f"Therefore, the image vertices are {ans_str}."
    )

    return {
        "subskill": "17_reflection_triangle_y_axis",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Correct coordinates for A': {_fmt_pt(-x1, y1)}", "marks": 1},
            {"desc": f"Correct coordinates for B': {_fmt_pt(-x2, y2)}", "marks": 1},
            {"desc": f"Correct coordinates for C': {_fmt_pt(-x3, y3)}", "marks": 1},
        ],
        "hints": [
            "In a y-axis reflection, negate the x-coordinate and keep the y-coordinate identical.",
            f"A' = (-{x1}; {y1}).",
            f"Full answer: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 18: Reflection of a Triangle in the Line y = x
# -----------------------------------------------------------------------------
def arch_18_reflection_triangle_line_y_equals_x(rng: random.Random, seed: int) -> Dict[str, Any]:
    x1, y1 = rng.randint(1, 3), rng.randint(3, 5)
    x2, y2 = x1 + rng.randint(1, 2), y1
    x3, y3 = x1, y1 - rng.randint(2, 3)

    pre_pts = [(x1, y1), (x2, y2), (x3, y3)]
    img_pts = [(y1, x1), (y2, x2), (y3, x3)]

    svg = draw_transformation_grid_svg(
        pre_image=pre_pts,
        image=img_pts,
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="reflection",
        mirror_line="y=x",
        seed=seed,
        title="Triangle Reflection in line y = x",
    )

    ans_str = f"A'{_fmt_pt(y1, x1)}, B'{_fmt_pt(y2, x2)}, C'{_fmt_pt(y3, x3)}"
    prompt = (
        f"Triangle $\\triangle ABC$ with vertices $A{_fmt_pt(x1, y1)}$, $B{_fmt_pt(x2, y2)}$, and $C{_fmt_pt(x3, y3)}$ "
        f"is reflected across the line $y = x$. "
        f"Determine the coordinates of the image vertices $A', B', C'$."
    )
    sol = (
        f"The reflection rule across $y = x$ interchanges the coordinates: $(x; y) \\to (y; x)$:\n"
        f"$A{_fmt_pt(x1, y1)} \\to A'{_fmt_pt(y1, x1)}$\n"
        f"$B{_fmt_pt(x2, y2)} \\to B'{_fmt_pt(y2, x2)}$\n"
        f"$C{_fmt_pt(x3, y3)} \\to C'{_fmt_pt(y3, x3)}$\n"
        f"Therefore, the image vertices are {ans_str}."
    )

    return {
        "subskill": "18_reflection_triangle_line_y_equals_x",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Correct coordinates for A': {_fmt_pt(y1, x1)}", "marks": 1},
            {"desc": f"Correct coordinates for B': {_fmt_pt(y2, x2)}", "marks": 1},
            {"desc": f"Correct coordinates for C': {_fmt_pt(y3, x3)}", "marks": 1},
        ],
        "hints": [
            "When reflecting across the line y = x, swap x and y for each vertex.",
            f"A' = ({y1}; {x1}).",
            f"Full answer: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 19: Identify the Line of Reflection from Coordinates
# -----------------------------------------------------------------------------
def arch_19_reflection_identify_mirror_line(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-4, -3, -2, 2, 3, 4])
    y = rng.choice([-4, -3, -2, 2, 3, 4])
    while abs(x) == abs(y):
        y = rng.choice([-4, -3, -2, 2, 3, 4])

    choice = rng.choice(["x_axis", "y_axis", "y=x"])
    if choice == "x_axis":
        xp, yp = x, -y
        line_desc = "x-axis"
        line_eq = "y = 0"
    elif choice == "y_axis":
        xp, yp = -x, y
        line_desc = "y-axis"
        line_eq = "x = 0"
    else:
        xp, yp = y, x
        line_desc = "line y = x"
        line_eq = "y = x"

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="reflection",
        mirror_line=choice,
        seed=seed,
        title="Identify Line of Reflection",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is reflected to produce image $P'{_fmt_pt(xp, yp)}$. "
        f"Identify the line of reflection across which $P$ was reflected."
    )
    sol = (
        f"Compare the coordinates of $P({x}; {y})$ and $P'({xp}; {yp})$:\n"
        f"Notice that the transformation corresponds to {line_desc} ({line_eq}).\n"
        f"Therefore, the line of reflection is the {line_desc}."
    )

    return {
        "subskill": "19_reflection_identify_mirror_line",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": line_desc,
        "expected_answer": line_desc,
        "sample_answer": f"Reflection in the {line_desc}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Compare coordinate signs and positions", "marks": 1},
            {"desc": f"Identify correct line of reflection: {line_desc}", "marks": 1},
        ],
        "hints": [
            "Check which coordinate changed sign or if the coordinates swapped positions.",
            f"If y changed sign, it is the x-axis. If x changed sign, it is the y-axis. If swapped, it is y = x.",
            f"The answer is {line_desc}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 20: Reflection Perpendicular Bisector Property
# -----------------------------------------------------------------------------
def arch_20_reflection_perpendicular_bisector(rng: random.Random, seed: int) -> Dict[str, Any]:
    # Point reflected in x-axis or y-axis, asks for the midpoint of PP' which lies on the mirror line
    axis = rng.choice(["x_axis", "y_axis"])
    x = rng.choice([-4, -2, 2, 4])
    y = rng.choice([-4, -2, 2, 4])

    if axis == "x_axis":
        xp, yp = x, -y
        mx, my = x, 0
        mirror_name = "x-axis"
    else:
        xp, yp = -x, y
        mx, my = 0, y
        mirror_name = "y-axis"

    ans_str = _fmt_pt(mx, my)
    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="reflection",
        mirror_line=axis,
        seed=seed,
        title=f"Perpendicular Bisector on {mirror_name}",
    )

    prompt = (
        f"A fundamental property of reflection is that the line of reflection is the perpendicular bisector "
        f"of the line segment $PP'$ connecting pre-image $P{_fmt_pt(x, y)}$ and image $P'{_fmt_pt(xp, yp)}$. "
        f"Calculate the coordinates of the midpoint $M$ of segment $PP'$, which lies directly on the mirror line."
    )
    sol = (
        f"The midpoint formula for segment $PP'$ is $M\\left(\\frac{{x_1 + x_2}}{{2}}; \\frac{{y_1 + y_2}}{{2}}\\right)$:\n"
        f"$x_M = \\frac{{{x} + ({xp})}}{{2}} = \\frac{{{x + xp}}}{{2}} = {mx}$\n"
        f"$y_M = \\frac{{{y} + ({yp})}}{{2}} = \\frac{{{y + yp}}}{{2}} = {my}$\n"
        f"Therefore, the midpoint is $M{ans_str}$, confirming it lies on the {mirror_name}."
    )

    return {
        "subskill": "20_reflection_perpendicular_bisector",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply midpoint formula to coordinates of P and P'", "marks": 1},
            {"desc": f"Correct midpoint coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "The midpoint formula is ((x1 + x2)/2; (y1 + y2)/2).",
            f"Add coordinates and divide by 2: ({x} + {xp})/2 and ({y} + {yp})/2.",
            f"Midpoint M is {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 21: Rotate Point 90° Clockwise About Origin
# -----------------------------------------------------------------------------
def arch_21_rotation_point_origin_90_clockwise(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    y = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    xp, yp = y, -x
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="rotation",
        rotation_center=(0, 0),
        rotation_angle_deg=90,
        seed=seed,
        title="Rotation: 90° Clockwise About Origin",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is rotated $90^\\circ$ clockwise about the origin $O(0; 0)$. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"The coordinate rule for a $90^\\circ$ clockwise rotation about the origin is $(x; y) \\to (y; -x)$.\n"
        f"Here, $x = {x}$ and $y = {y}$.\n"
        f"$x' = y = {y}$\n"
        f"$y' = -x = -({x}) = {yp}$\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "21_rotation_point_origin_90_clockwise",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply 90° clockwise rotation rule (x; y) -> (y; -x)", "marks": 1},
            {"desc": f"State correct image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "For a 90° clockwise rotation about the origin: (x; y) -> (y; -x).",
            f"The new x is {y}, the new y is -({x}) = {yp}.",
            f"Image coordinates: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 22: Rotate Point 90° Anti-Clockwise About Origin
# -----------------------------------------------------------------------------
def arch_22_rotation_point_origin_90_anticlockwise(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    y = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    xp, yp = -y, x
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="rotation",
        rotation_center=(0, 0),
        rotation_angle_deg=-90,
        seed=seed,
        title="Rotation: 90° Anti-Clockwise About Origin",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is rotated $90^\\circ$ anti-clockwise (counter-clockwise) "
        f"about the origin $O(0; 0)$. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"The coordinate rule for a $90^\\circ$ anti-clockwise rotation about the origin is $(x; y) \\to (-y; x)$.\n"
        f"Here, $x = {x}$ and $y = {y}$.\n"
        f"$x' = -y = -({y}) = {xp}$\n"
        f"$y' = x = {x}$\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "22_rotation_point_origin_90_anticlockwise",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply 90° anti-clockwise rotation rule (x; y) -> (-y; x)", "marks": 1},
            {"desc": f"State correct image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "For a 90° anti-clockwise rotation about the origin: (x; y) -> (-y; x).",
            f"The new x is -({y}) = {xp}, the new y is {x}.",
            f"Image coordinates: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 23: Rotate Point 180° About Origin
# -----------------------------------------------------------------------------
def arch_23_rotation_point_origin_180(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    y = rng.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    xp, yp = -x, -y
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="rotation",
        rotation_center=(0, 0),
        rotation_angle_deg=180,
        seed=seed,
        title="Rotation: 180° About Origin",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is rotated $180^\\circ$ about the origin $O(0; 0)$. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"The coordinate rule for a $180^\\circ$ rotation (half-turn) about the origin is $(x; y) \\to (-x; -y)$.\n"
        f"Here, $x = {x}$ and $y = {y}$.\n"
        f"$x' = -({x}) = {xp}$\n"
        f"$y' = -({y}) = {yp}$\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "23_rotation_point_origin_180",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply 180° rotation rule (x; y) -> (-x; -y)", "marks": 1},
            {"desc": f"State correct image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            "A 180° rotation about the origin changes the signs of both coordinates.",
            f"x' = -({x}) = {xp}, y' = -({y}) = {yp}.",
            f"Image coordinates: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 24: Rotate Triangle 90° Clockwise About Origin
# -----------------------------------------------------------------------------
def arch_24_rotation_triangle_origin_90_cw(rng: random.Random, seed: int) -> Dict[str, Any]:
    x1, y1 = rng.randint(1, 3), rng.randint(1, 3)
    x2, y2 = x1 + rng.randint(2, 3), y1
    x3, y3 = x1, y1 + rng.randint(2, 3)

    pre_pts = [(x1, y1), (x2, y2), (x3, y3)]
    img_pts = [(y1, -x1), (y2, -x2), (y3, -x3)]

    svg = draw_transformation_grid_svg(
        pre_image=pre_pts,
        image=img_pts,
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="rotation",
        rotation_center=(0, 0),
        rotation_angle_deg=90,
        seed=seed,
        title="Triangle 90° Clockwise Rotation About Origin",
    )

    ans_str = f"A'{_fmt_pt(y1, -x1)}, B'{_fmt_pt(y2, -x2)}, C'{_fmt_pt(y3, -x3)}"
    prompt = (
        f"Triangle $\\triangle ABC$ with vertices $A{_fmt_pt(x1, y1)}$, $B{_fmt_pt(x2, y2)}$, and $C{_fmt_pt(x3, y3)}$ "
        f"is rotated $90^\\circ$ clockwise about the origin $O(0; 0)$. "
        f"Determine the coordinates of the image vertices $A', B', C'$."
    )
    sol = (
        f"The coordinate rule for a $90^\\circ$ clockwise rotation about the origin is $(x; y) \\to (y; -x)$:\n"
        f"$A{_fmt_pt(x1, y1)} \\to A'{_fmt_pt(y1, -x1)}$\n"
        f"$B{_fmt_pt(x2, y2)} \\to B'{_fmt_pt(y2, -x2)}$\n"
        f"$C{_fmt_pt(x3, y3)} \\to C'{_fmt_pt(y3, -x3)}$\n"
        f"Therefore, the image vertices are {ans_str}."
    )

    return {
        "subskill": "24_rotation_triangle_origin_90_cw",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Correct coordinates for A': {_fmt_pt(y1, -x1)}", "marks": 1},
            {"desc": f"Correct coordinates for B': {_fmt_pt(y2, -x2)}", "marks": 1},
            {"desc": f"Correct coordinates for C': {_fmt_pt(y3, -x3)}", "marks": 1},
        ],
        "hints": [
            "Apply the rule (x; y) -> (y; -x) to each vertex.",
            f"A({x1}; {y1}) becomes A'({y1}; -{x1}).",
            f"Full answer: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 25: Rotate Triangle 90° Anti-Clockwise About Origin
# -----------------------------------------------------------------------------
def arch_25_rotation_triangle_origin_90_ccw(rng: random.Random, seed: int) -> Dict[str, Any]:
    x1, y1 = rng.randint(1, 3), rng.randint(1, 3)
    x2, y2 = x1 + rng.randint(2, 3), y1
    x3, y3 = x1, y1 + rng.randint(2, 3)

    pre_pts = [(x1, y1), (x2, y2), (x3, y3)]
    img_pts = [(-y1, x1), (-y2, x2), (-y3, x3)]

    svg = draw_transformation_grid_svg(
        pre_image=pre_pts,
        image=img_pts,
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="rotation",
        rotation_center=(0, 0),
        rotation_angle_deg=-90,
        seed=seed,
        title="Triangle 90° Anti-Clockwise Rotation About Origin",
    )

    ans_str = f"A'{_fmt_pt(-y1, x1)}, B'{_fmt_pt(-y2, x2)}, C'{_fmt_pt(-y3, x3)}"
    prompt = (
        f"Triangle $\\triangle ABC$ with vertices $A{_fmt_pt(x1, y1)}$, $B{_fmt_pt(x2, y2)}$, and $C{_fmt_pt(x3, y3)}$ "
        f"is rotated $90^\\circ$ anti-clockwise about the origin $O(0; 0)$. "
        f"Determine the coordinates of the image vertices $A', B', C'$."
    )
    sol = (
        f"The coordinate rule for a $90^\\circ$ anti-clockwise rotation about the origin is $(x; y) \\to (-y; x)$:\n"
        f"$A{_fmt_pt(x1, y1)} \\to A'{_fmt_pt(-y1, x1)}$\n"
        f"$B{_fmt_pt(x2, y2)} \\to B'{_fmt_pt(-y2, x2)}$\n"
        f"$C{_fmt_pt(x3, y3)} \\to C'{_fmt_pt(-y3, x3)}$\n"
        f"Therefore, the image vertices are {ans_str}."
    )

    return {
        "subskill": "25_rotation_triangle_origin_90_ccw",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Correct coordinates for A': {_fmt_pt(-y1, x1)}", "marks": 1},
            {"desc": f"Correct coordinates for B': {_fmt_pt(-y2, x2)}", "marks": 1},
            {"desc": f"Correct coordinates for C': {_fmt_pt(-y3, x3)}", "marks": 1},
        ],
        "hints": [
            "Apply the rule (x; y) -> (-y; x) to each vertex.",
            f"A({x1}; {y1}) becomes A'(-{y1}; {x1}).",
            f"Full answer: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }
