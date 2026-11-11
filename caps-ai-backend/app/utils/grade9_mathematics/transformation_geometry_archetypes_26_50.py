"""Grade 9 Mathematics — Transformation Geometry Archetypes 26 to 50 (CAPS Term 3).
Rotations, Enlargements/Reductions, Area/Perimeter Scaling Factors, Composite Transformations, and Invariance.
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
# Archetype 26: Rotate Triangle 180° About Origin
# -----------------------------------------------------------------------------
def arch_26_rotation_triangle_origin_180(rng: random.Random, seed: int) -> Dict[str, Any]:
    x1, y1 = rng.randint(1, 3), rng.randint(1, 3)
    x2, y2 = x1 + rng.randint(2, 3), y1
    x3, y3 = x1, y1 + rng.randint(2, 3)

    pre_pts = [(x1, y1), (x2, y2), (x3, y3)]
    img_pts = [(-x1, -y1), (-x2, -y2), (-x3, -y3)]

    svg = draw_transformation_grid_svg(
        pre_image=pre_pts,
        image=img_pts,
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="rotation",
        rotation_center=(0, 0),
        rotation_angle_deg=180,
        seed=seed,
        title="Triangle 180° Rotation About Origin",
    )

    ans_str = f"A'{_fmt_pt(-x1, -y1)}, B'{_fmt_pt(-x2, -y2)}, C'{_fmt_pt(-x3, -y3)}"
    prompt = (
        f"Triangle $\\triangle ABC$ with vertices $A{_fmt_pt(x1, y1)}$, $B{_fmt_pt(x2, y2)}$, and $C{_fmt_pt(x3, y3)}$ "
        f"is rotated $180^\\circ$ about the origin $O(0; 0)$. "
        f"Determine the coordinates of the image vertices $A', B', C'$."
    )
    sol = (
        f"The coordinate rule for a $180^\\circ$ rotation about the origin is $(x; y) \\to (-x; -y)$:\n"
        f"$A{_fmt_pt(x1, y1)} \\to A'{_fmt_pt(-x1, -y1)}$\n"
        f"$B{_fmt_pt(x2, y2)} \\to B'{_fmt_pt(-x2, -y2)}$\n"
        f"$C{_fmt_pt(x3, y3)} \\to C'{_fmt_pt(-x3, -y3)}$\n"
        f"Therefore, the image vertices are {ans_str}."
    )

    return {
        "subskill": "26_rotation_triangle_origin_180",
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
            {"desc": f"Correct coordinates for A': {_fmt_pt(-x1, -y1)}", "marks": 1},
            {"desc": f"Correct coordinates for B': {_fmt_pt(-x2, -y2)}", "marks": 1},
            {"desc": f"Correct coordinates for C': {_fmt_pt(-x3, -y3)}", "marks": 1},
        ],
        "hints": [
            "A 180° rotation about the origin negates both coordinates: (x; y) -> (-x; -y).",
            f"A' = (-{x1}; -{y1}).",
            f"Full answer: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 27: Identify Angle and Direction of Rotation from Origin
# -----------------------------------------------------------------------------
def arch_27_rotation_identify_angle_direction(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-4, -3, -2, 2, 3, 4])
    y = rng.choice([-4, -3, -2, 2, 3, 4])
    while abs(x) == abs(y):
        y = rng.choice([-4, -3, -2, 2, 3, 4])

    rot_type = rng.choice(["90_cw", "90_ccw", "180"])
    if rot_type == "90_cw":
        xp, yp = y, -x
        desc = "90° clockwise"
        angle_deg = 90
    elif rot_type == "90_ccw":
        xp, yp = -y, x
        desc = "90° anti-clockwise"
        angle_deg = -90
    else:
        xp, yp = -x, -y
        desc = "180°"
        angle_deg = 180

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="rotation",
        rotation_center=(0, 0),
        rotation_angle_deg=angle_deg,
        seed=seed,
        title="Identify Rotation",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ was rotated about the origin $O(0; 0)$ "
        f"to arrive at $P'{_fmt_pt(xp, yp)}$. "
        f"Determine the angle and direction of this rotation (e.g. '90° clockwise', '90° anti-clockwise', or '180°')."
    )
    sol = (
        f"Analyzing the coordinates from $P({x}; {y})$ to $P'({xp}; {yp})$:\n"
        f"Rule matches $(x; y) \\to ({xp}; {yp})$, which corresponds to a rotation of {desc} about the origin.\n"
        f"Therefore, the rotation is {desc}."
    )

    return {
        "subskill": "27_rotation_identify_angle_direction",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": desc,
        "expected_answer": desc,
        "sample_answer": desc,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Analyze coordinate transformations to test standard rotation rules", "marks": 1},
            {"desc": f"State correct rotation: {desc}", "marks": 1},
        ],
        "hints": [
            "Check the coordinate patterns: (y; -x) is 90° CW; (-y; x) is 90° CCW; (-x; -y) is 180°.",
            f"Here, original ({x}; {y}) became ({xp}; {yp}).",
            f"The rotation is {desc}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 28: Rotation About a Point Not at the Origin
# -----------------------------------------------------------------------------
def arch_28_rotation_about_point_not_origin(rng: random.Random, seed: int) -> Dict[str, Any]:
    cx = rng.choice([-2, -1, 1, 2])
    cy = rng.choice([-2, -1, 1, 2])
    dx = rng.choice([-3, -2, 2, 3])
    dy = rng.choice([-3, -2, 2, 3])
    px = cx + dx
    py = cy + dy

    rot_angle = rng.choice(["180", "90_cw"])
    if rot_angle == "180":
        # 180 deg about (cx, cy): (cx - dx, cy - dy) = (2cx - px, 2cy - py)
        xp = cx - dx
        yp = cy - dy
        rot_name = "180°"
    else:
        # 90 deg clockwise about (cx, cy): relative (dx, dy) -> (dy, -dx)
        xp = cx + dy
        yp = cy - dx
        rot_name = "90° clockwise"

    ans_str = _fmt_pt(xp, yp)
    svg = draw_transformation_grid_svg(
        pre_image=[(px, py)],
        image=[(xp, yp)],
        pre_labels=[f"P({px}; {py})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="rotation",
        rotation_center=(cx, cy),
        seed=seed,
        title=f"Rotation {rot_name} About C{_fmt_pt(cx, cy)}",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(px, py)}$ is rotated {rot_name} "
        f"about the center of rotation $C{_fmt_pt(cx, cy)}$ (not the origin). "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"To rotate about center $C({cx}; {cy})$:\n"
        f"1. Shift coordinates relative to $C$: $(\\Delta x; \\Delta y) = ({px} - ({cx}); {py} - ({cy})) = ({dx}; {dy})$.\n"
        f"2. Apply {rot_name} rotation to relative vector:\n"
        + (f"   $(\\Delta x; \\Delta y) \\to (-\\Delta x; -\\Delta y) = ({-dx}; {-dy})$.\n" if rot_angle == "180" else f"   $(\\Delta x; \\Delta y) \\to (\\Delta y; -\\Delta x) = ({dy}; {-dx})$.\n")
        + f"3. Translate back to center $C$:\n"
        f"   $x' = {cx} + ({xp - cx}) = {xp}$\n"
        f"   $y' = {cy} + ({yp - cy}) = {yp}$\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "28_rotation_about_point_not_origin",
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
            {"desc": f"Calculate relative vector from center C: ({dx}; {dy})", "marks": 1},
            {"desc": f"Rotate relative vector by {rot_name}", "marks": 1},
            {"desc": f"Shift back to center to obtain {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Subtract center coordinates C({cx}; {cy}) from P to find relative position.",
            f"Apply the rotation rule to the relative vector, then add C({cx}; {cy}) back.",
            f"Image coordinates: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 29: Enlargement of a Point from the Origin (Integer Scale Factor)
# -----------------------------------------------------------------------------
def arch_29_enlargement_point_origin(rng: random.Random, seed: int) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4])
    x = rng.choice([-3, -2, -1, 1, 2, 3])
    y = rng.choice([-3, -2, -1, 1, 2, 3])
    xp, yp = k * x, k * y
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="enlargement",
        dilation_center=(0, 0),
        scale_factor=k,
        seed=seed,
        title=f"Enlargement by Scale Factor k = {k}",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ is enlarged with respect to the origin $O(0; 0)$ "
        f"by a scale factor of $k = {k}$. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"The coordinate rule for dilation (enlargement) from the origin by scale factor $k$ is $(x; y) \\to (kx; ky)$:\n"
        f"$x' = k \\times x = {k} \\times ({x}) = {xp}$\n"
        f"$y' = k \\times y = {k} \\times ({y}) = {yp}$\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "29_enlargement_point_origin",
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
            {"desc": f"Multiply each coordinate by scale factor k = {k}", "marks": 1},
            {"desc": f"State correct image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Multiply both the x-coordinate and the y-coordinate by {k}.",
            f"x' = {k} * ({x}) = {xp}, y' = {k} * ({y}) = {yp}.",
            f"Image coordinates: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 30: Reduction of a Point from Origin (Fractional Scale Factor)
# -----------------------------------------------------------------------------
def arch_30_reduction_point_origin(rng: random.Random, seed: int) -> Dict[str, Any]:
    denom = rng.choice([2, 3, 4])
    mult_x = rng.choice([-3, -2, -1, 1, 2, 3])
    mult_y = rng.choice([-3, -2, -1, 1, 2, 3])
    x = mult_x * denom
    y = mult_y * denom
    xp = mult_x
    yp = mult_y
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P'({xp}; {yp})"],
        transformation_type="enlargement",
        dilation_center=(0, 0),
        scale_factor=1.0 / denom,
        seed=seed,
        title=f"Reduction by Scale Factor k = 1/{denom}",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $P{_fmt_pt(x, y)}$ undergoes a reduction with respect to the origin $O(0; 0)$ "
        f"by a scale factor of $k = \\frac{{1}}{{{denom}}}$. "
        f"Determine the coordinates of the image point $P'$."
    )
    sol = (
        f"The coordinate rule for a reduction from the origin by scale factor $k = \\frac{{1}}{{{denom}}}$ is "
        f"$(x; y) \\to \\left(\\frac{{x}}{{{denom}}}; \\frac{{y}}{{{denom}}}\\right)$:\n"
        f"$x' = \\frac{{{x}}}{{{denom}}} = {xp}$\n"
        f"$y' = \\frac{{{y}}}{{{denom}}} = {yp}$\n"
        f"Therefore, the image point is $P'{ans_str}$."
    )

    return {
        "subskill": "30_reduction_point_origin",
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
            {"desc": f"Divide each coordinate by {denom} (multiply by 1/{denom})", "marks": 1},
            {"desc": f"State correct image coordinates {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Divide both coordinates by {denom}.",
            f"x' = {x}/{denom} = {xp}, y' = {y}/{denom} = {yp}.",
            f"Image coordinates: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 31: Find Scale Factor from Coordinates
# -----------------------------------------------------------------------------
def arch_31_enlargement_find_scale_factor(rng: random.Random, seed: int) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4, 5])
    x1 = rng.choice([-3, -2, -1, 1, 2, 3])
    y1 = rng.choice([-3, -2, -1, 1, 2, 3])
    x2, y2 = k * x1, k * y1

    svg = draw_transformation_grid_svg(
        pre_image=[(x1, y1)],
        image=[(x2, y2)],
        pre_labels=[f"A({x1}; {y1})"],
        image_labels=[f"A'({x2}; {y2})"],
        transformation_type="enlargement",
        dilation_center=(0, 0),
        scale_factor=k,
        seed=seed,
        title="Find Scale Factor k",
    )

    prompt = (
        f"In the Cartesian plane diagram, point $A{_fmt_pt(x1, y1)}$ is mapped to $A'{_fmt_pt(x2, y2)}$ "
        f"under an enlargement centered at the origin. "
        f"Calculate the scale factor $k$ of the enlargement."
    )
    sol = (
        f"For a dilation centered at the origin, $(x'; y') = (kx; ky)$.\n"
        f"We can find $k$ using either coordinate ratio:\n"
        f"$k = \\frac{{x'}}{{x}} = \\frac{{{x2}}}{{{x1}}} = {k}$ (or $k = \\frac{{y'}}{{y}} = \\frac{{{y2}}}{{{y1}}} = {k}$).\n"
        f"Therefore, the scale factor is $k = {k}$."
    )

    return {
        "subskill": "31_enlargement_find_scale_factor",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(k),
        "expected_answer": str(k),
        "sample_answer": f"k = {k}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Set up ratio of image coordinate to original coordinate", "marks": 1},
            {"desc": f"Calculate scale factor k = {k}", "marks": 1},
        ],
        "hints": [
            "The scale factor is the ratio: image coordinate / original coordinate.",
            f"k = {x2} / ({x1}) = {k}.",
            f"The scale factor is {k}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 32: Enlarge Triangle Vertices from Origin
# -----------------------------------------------------------------------------
def arch_32_enlargement_triangle_vertices(rng: random.Random, seed: int) -> Dict[str, Any]:
    k = rng.choice([2, 3])
    x1, y1 = rng.randint(1, 2), rng.randint(1, 2)
    x2, y2 = x1 + rng.randint(1, 2), y1
    x3, y3 = x1, y1 + rng.randint(1, 2)

    pre_pts = [(x1, y1), (x2, y2), (x3, y3)]
    img_pts = [(k * x1, k * y1), (k * x2, k * y2), (k * x3, k * y3)]

    svg = draw_transformation_grid_svg(
        pre_image=pre_pts,
        image=img_pts,
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="enlargement",
        dilation_center=(0, 0),
        scale_factor=k,
        seed=seed,
        title=f"Triangle Enlargement by Scale Factor k = {k}",
    )

    ans_str = f"A'{_fmt_pt(k*x1, k*y1)}, B'{_fmt_pt(k*x2, k*y2)}, C'{_fmt_pt(k*x3, k*y3)}"
    prompt = (
        f"Triangle $\\triangle ABC$ has vertices $A{_fmt_pt(x1, y1)}$, $B{_fmt_pt(x2, y2)}$, and $C{_fmt_pt(x3, y3)}$. "
        f"The triangle is enlarged by a scale factor of $k = {k}$ with the center of enlargement at the origin. "
        f"Determine the coordinates of the image vertices $A', B', C'$."
    )
    sol = (
        f"Multiply each coordinate of every vertex by $k = {k}$:\n"
        f"$A{_fmt_pt(x1, y1)} \\to A'({k}\\times {x1}; {k}\\times {y1}) = A'{_fmt_pt(k*x1, k*y1)}$\n"
        f"$B{_fmt_pt(x2, y2)} \\to B'({k}\\times {x2}; {k}\\times {y2}) = B'{_fmt_pt(k*x2, k*y2)}$\n"
        f"$C{_fmt_pt(x3, y3)} \\to C'({k}\\times {x3}; {k}\\times {y3}) = C'{_fmt_pt(k*x3, k*y3)}$\n"
        f"Therefore, the image vertices are {ans_str}."
    )

    return {
        "subskill": "32_enlargement_triangle_vertices",
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
            {"desc": f"Correct coordinates for A': {_fmt_pt(k*x1, k*y1)}", "marks": 1},
            {"desc": f"Correct coordinates for B': {_fmt_pt(k*x2, k*y2)}", "marks": 1},
            {"desc": f"Correct coordinates for C': {_fmt_pt(k*x3, k*y3)}", "marks": 1},
        ],
        "hints": [
            f"Multiply every coordinate by {k}.",
            f"A': ({k} * {x1}; {k} * {y1}) = {_fmt_pt(k*x1, k*y1)}.",
            f"Full answer: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 33: Reduce Triangle Vertices from Origin
# -----------------------------------------------------------------------------
def arch_33_reduction_triangle_vertices(rng: random.Random, seed: int) -> Dict[str, Any]:
    denom = 2
    x1, y1 = 2 * rng.randint(1, 2), 2 * rng.randint(1, 2)
    x2, y2 = x1 + 2 * rng.randint(1, 2), y1
    x3, y3 = x1, y1 + 2 * rng.randint(1, 2)

    pre_pts = [(x1, y1), (x2, y2), (x3, y3)]
    img_pts = [(x1 // denom, y1 // denom), (x2 // denom, y2 // denom), (x3 // denom, y3 // denom)]

    svg = draw_transformation_grid_svg(
        pre_image=pre_pts,
        image=img_pts,
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="enlargement",
        dilation_center=(0, 0),
        scale_factor=0.5,
        seed=seed,
        title="Triangle Reduction by Scale Factor k = 1/2",
    )

    ans_str = f"A'{_fmt_pt(x1//2, y1//2)}, B'{_fmt_pt(x2//2, y2//2)}, C'{_fmt_pt(x3//2, y3//2)}"
    prompt = (
        f"Triangle $\\triangle ABC$ has vertices $A{_fmt_pt(x1, y1)}$, $B{_fmt_pt(x2, y2)}$, and $C{_fmt_pt(x3, y3)}$. "
        f"It undergoes a reduction by a scale factor of $k = \\frac{{1}}{{2}}$ about the origin. "
        f"Determine the coordinates of the image vertices $A', B', C'$."
    )
    sol = (
        f"Divide every coordinate by $2$ (multiply by $\\frac{{1}}{{2}}$):\n"
        f"$A{_fmt_pt(x1, y1)} \\to A'({x1//2}; {y1//2})$\n"
        f"$B{_fmt_pt(x2, y2)} \\to B'({x2//2}; {y2//2})$\n"
        f"$C{_fmt_pt(x3, y3)} \\to C'({x3//2}; {y3//2})$\n"
        f"Therefore, the image vertices are {ans_str}."
    )

    return {
        "subskill": "33_reduction_triangle_vertices",
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
            {"desc": f"Correct coordinates for A': {_fmt_pt(x1//2, y1//2)}", "marks": 1},
            {"desc": f"Correct coordinates for B': {_fmt_pt(x2//2, y2//2)}", "marks": 1},
            {"desc": f"Correct coordinates for C': {_fmt_pt(x3//2, y3//2)}", "marks": 1},
        ],
        "hints": [
            "Halve each coordinate of the vertices.",
            f"A': ({x1}/2; {y1}/2) = {_fmt_pt(x1//2, y1//2)}.",
            f"Full answer: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 34: Side Length Relationship Under Enlargement/Reduction
# -----------------------------------------------------------------------------
def arch_34_enlargement_side_lengths(rng: random.Random, seed: int) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4, 5])
    orig_len = rng.randint(4, 12)
    img_len = k * orig_len

    svg = draw_transformation_grid_svg(
        pre_image=[(1, 1), (1 + orig_len // 2, 1)],
        image=[(2, 3), (2 + img_len // 2, 3)],
        pre_labels=["A", f"B ({orig_len} cm)"],
        image_labels=["A'", f"B' ({img_len} cm)"],
        transformation_type="none",
        seed=seed,
        title=f"Side Length Scaling (k = {k})",
    )

    prompt = (
        f"A line segment $AB$ has length $AB = {orig_len}\\text{{ cm}}$. "
        f"If the segment is enlarged by a scale factor of $k = {k}$, "
        f"calculate the length of the image segment $A'B'$ in cm."
    )
    sol = (
        f"Under an enlargement with scale factor $k$, the length of any segment is scaled directly by $k$:\n"
        f"$A'B' = k \\times AB = {k} \\times {orig_len} = {img_len}\\text{{ cm}}$.\n"
        f"Therefore, the length of the image segment is ${img_len}$ cm."
    )

    return {
        "subskill": "34_enlargement_side_lengths",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(img_len),
        "expected_answer": str(img_len),
        "sample_answer": f"{img_len} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State linear scaling formula: A'B' = k * AB", "marks": 1},
            {"desc": f"Calculate image length: {img_len} cm", "marks": 1},
        ],
        "hints": [
            "Side lengths scale linearly by the factor k.",
            f"Multiply the original side length ({orig_len}) by k ({k}).",
            f"Image length = {img_len} cm.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 35: Effect of Scale Factor on Perimeter
# -----------------------------------------------------------------------------
def arch_35_enlargement_perimeter_effect(rng: random.Random, seed: int) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4, 5])
    p_orig = rng.randint(14, 30)
    p_img = k * p_orig

    svg = draw_transformation_grid_svg(
        pre_image=[(1, 1), (3, 1), (3, 2), (1, 2)],
        image=[(2, 3), (2 + 2*k, 3), (2 + 2*k, 3 + k), (2, 3 + k)],
        pre_labels=["A", "B", "C", "D"],
        image_labels=["A'", "B'", "C'", "D'"],
        transformation_type="none",
        seed=seed,
        title=f"Perimeter Scaling: P' = k * P (k = {k})",
    )

    prompt = (
        f"A 2D polygon has a perimeter of ${p_orig}\\text{{ cm}}$. "
        f"If the figure is enlarged by a scale factor of $k = {k}$, "
        f"determine the perimeter of the enlarged figure in cm."
    )
    sol = (
        f"Perimeter is a one-dimensional (linear) measurement, so it scales by factor $k$:\n"
        f"$\\text{{Perimeter}}' = k \\times \\text{{Perimeter}} = {k} \\times {p_orig} = {p_img}\\text{{ cm}}$.\n"
        f"Therefore, the perimeter of the enlarged figure is ${p_img}$ cm."
    )

    return {
        "subskill": "35_enlargement_perimeter_effect",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(p_img),
        "expected_answer": str(p_img),
        "sample_answer": f"{p_img} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Apply linear scaling formula: P' = k * P", "marks": 1},
            {"desc": f"Compute image perimeter: {p_img} cm", "marks": 1},
        ],
        "hints": [
            "Perimeter scales by k (not k squared!).",
            f"Multiply {p_orig} by {k}.",
            f"Image perimeter = {p_img} cm.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 36: Effect of Scale Factor on Area (k^2 Factor)
# -----------------------------------------------------------------------------
def arch_36_enlargement_area_factor_k_squared(rng: random.Random, seed: int) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4, 5])
    k_sq = k * k

    svg = draw_transformation_grid_svg(
        pre_image=[(1, 1), (2, 1), (2, 2), (1, 2)],
        image=[(2, 3), (2 + k, 3), (2 + k, 3 + k), (2, 3 + k)],
        pre_labels=["", "", "", ""],
        image_labels=["", "", "", ""],
        transformation_type="none",
        seed=seed,
        title=f"Area Scaling: Area' = k² * Area (k = {k})",
    )

    prompt = (
        f"When a two-dimensional geometric figure is enlarged by a linear scale factor of $k = {k}$, "
        f"by what factor does its area increase?"
    )
    sol = (
        f"Area is a two-dimensional measurement involving length $\\times$ breadth.\n"
        f"When all linear dimensions are multiplied by $k = {k}$, the area is multiplied by $k^2$:\n"
        f"$\\text{{Area Factor}} = k^2 = ({k})^2 = {k_sq}$.\n"
        f"Therefore, the area increases by a factor of ${k_sq}$."
    )

    return {
        "subskill": "36_enlargement_area_factor_k_squared",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(k_sq),
        "expected_answer": str(k_sq),
        "sample_answer": f"Increases by a factor of {k_sq} (or k²)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "State area scale factor formula k^2", "marks": 1},
            {"desc": f"Calculate factor: {k_sq}", "marks": 1},
        ],
        "hints": [
            "Linear dimensions scale by k; two-dimensional areas scale by k².",
            f"Compute ({k})².",
            f"The area increases by a factor of {k_sq}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 37: Find Area of Image Given Original Area and k
# -----------------------------------------------------------------------------
def arch_37_enlargement_find_area_given_original(rng: random.Random, seed: int) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4])
    a_orig = rng.choice([6, 8, 10, 12, 15, 20])
    a_img = (k * k) * a_orig

    svg = draw_transformation_grid_svg(
        pre_image=[(1, 1), (3, 1), (2, 3)],
        image=[(2, 2), (2 + 2*k, 2), (2 + k, 2 + 2*k)],
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="none",
        seed=seed,
        title=f"Enlargement: Area' = k² * Area",
    )

    prompt = (
        f"A triangle has an area of ${a_orig}\\text{{ cm}}^2$. "
        f"If the triangle is enlarged by a scale factor of $k = {k}$, "
        f"calculate the area of the enlarged triangle in $\\text{{cm}}^2$."
    )
    sol = (
        f"The formula for the area of an enlarged figure is $\\text{{Area}}' = k^2 \\times \\text{{Area}}$:\n"
        f"$\\text{{Area}}' = ({k})^2 \\times {a_orig} = {k*k} \\times {a_orig} = {a_img}\\text{{ cm}}^2$.\n"
        f"Therefore, the area of the enlarged triangle is ${a_img}\\text{{ cm}}^2$."
    )

    return {
        "subskill": "37_enlargement_find_area_given_original",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(a_img),
        "expected_answer": str(a_img),
        "sample_answer": f"{a_img} cm²",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Apply k^2 = {k*k} to area calculation", "marks": 1},
            {"desc": f"Calculate final area: {a_img} cm²", "marks": 1},
        ],
        "hints": [
            "Multiply the original area by k².",
            f"k² = ({k})² = {k*k}.",
            f"Area' = {k*k} * {a_orig} = {a_img} cm².",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 38: Find Original Area Given Enlarged Area and k
# -----------------------------------------------------------------------------
def arch_38_enlargement_find_original_area(rng: random.Random, seed: int) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4])
    a_orig = rng.choice([5, 8, 10, 12, 16])
    a_img = (k * k) * a_orig

    svg = draw_transformation_grid_svg(
        pre_image=[(1, 1), (3, 1), (3, 2), (1, 2)],
        image=[(2, 2), (2 + 2*k, 2), (2 + 2*k, 2 + k), (2, 2 + k)],
        pre_labels=["", "", "", ""],
        image_labels=["", "", "", ""],
        transformation_type="none",
        seed=seed,
        title=f"Find Original Area: Area = Area' / k²",
    )

    prompt = (
        f"After an enlargement by a scale factor of $k = {k}$, the area of a shape is ${a_img}\\text{{ cm}}^2$. "
        f"Determine the area of the original shape in $\\text{{cm}}^2$."
    )
    sol = (
        f"Since $\\text{{Area}}' = k^2 \\times \\text{{Area}}$, we have:\n"
        f"$\\text{{Area}} = \\frac{{\\text{{Area}}'}}{{k^2}} = \\frac{{{a_img}}}{{({k})^2}} = \\frac{{{a_img}}}{{{k*k}}} = {a_orig}\\text{{ cm}}^2$.\n"
        f"Therefore, the original area was ${a_orig}\\text{{ cm}}^2$."
    )

    return {
        "subskill": "38_enlargement_find_original_area",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(a_orig),
        "expected_answer": str(a_orig),
        "sample_answer": f"{a_orig} cm²",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Divide image area by k^2 = {k*k}", "marks": 1},
            {"desc": f"Calculate original area: {a_orig} cm²", "marks": 1},
        ],
        "hints": [
            "Divide the enlarged area by k².",
            f"k² = ({k})² = {k*k}.",
            f"Original Area = {a_img} / {k*k} = {a_orig} cm².",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 39: Determine Scale Factor k from Areas
# -----------------------------------------------------------------------------
def arch_39_enlargement_find_k_from_areas(rng: random.Random, seed: int) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4, 5])
    a_orig = rng.choice([4, 6, 8, 10, 12])
    a_img = (k * k) * a_orig

    svg = draw_transformation_grid_svg(
        pre_image=[(1, 1), (3, 1), (2, 3)],
        image=[(2, 2), (2 + 2*k, 2), (2 + k, 2 + 2*k)],
        pre_labels=["", "", ""],
        image_labels=["", "", ""],
        transformation_type="none",
        seed=seed,
        title=f"Find k from Areas: k = sqrt(Area' / Area)",
    )

    prompt = (
        f"The area of a 2D figure is ${a_orig}\\text{{ cm}}^2$, and the area of its enlarged image is ${a_img}\\text{{ cm}}^2$. "
        f"Calculate the linear scale factor $k$ of the enlargement."
    )
    sol = (
        f"The relationship between the areas is $\\frac{{\\text{{Area}}'}}{{\\text{{Area}}}} = k^2$.\n"
        f"$k^2 = \\frac{{{a_img}}}{{{a_orig}}} = {k*k}$.\n"
        f"Taking the square root (since scale factor $k > 0$):\n"
        f"$k = \\sqrt{{{k*k}}} = {k}$.\n"
        f"Therefore, the linear scale factor is $k = {k}$."
    )

    return {
        "subskill": "39_enlargement_find_k_from_areas",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(k),
        "expected_answer": str(k),
        "sample_answer": f"k = {k}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Compute area ratio: {a_img}/{a_orig} = {k*k}", "marks": 1},
            {"desc": f"Take square root to find k = {k}", "marks": 1},
        ],
        "hints": [
            "The area ratio equals k².",
            f"k² = {a_img} / {a_orig} = {k*k}.",
            f"k = sqrt({k*k}) = {k}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 40: Ratio of Areas Under Enlargement
# -----------------------------------------------------------------------------
def arch_40_enlargement_ratio_of_areas(rng: random.Random, seed: int) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4, 5])
    k_sq = k * k
    order = rng.choice(["orig_to_img", "img_to_orig"])

    if order == "orig_to_img":
        ratio_str = f"1 : {k_sq}"
        q_order = "original figure to the enlarged figure"
    else:
        ratio_str = f"{k_sq} : 1"
        q_order = "enlarged figure to the original figure"

    svg = draw_transformation_grid_svg(
        pre_image=[(1, 1), (3, 1), (2, 3)],
        image=[(2, 2), (2 + 2*k, 2), (2 + k, 2 + 2*k)],
        pre_labels=["", "", ""],
        image_labels=["", "", ""],
        transformation_type="none",
        seed=seed,
        title=f"Ratio of Areas (k = {k})",
    )

    prompt = (
        f"A polygon is enlarged by a scale factor of $k = {k}$. "
        f"Determine the ratio of the area of the {q_order} in the simplest form $A : B$."
    )
    sol = (
        f"Under an enlargement with scale factor $k$, the ratio of the sides is $1 : k = 1 : {k}$.\n"
        f"The ratio of the areas is the square of the ratio of the sides: $1^2 : k^2 = 1 : ({k})^2 = 1 : {k_sq}$.\n"
        f"For the ratio of {q_order}, the ratio is ${ratio_str}$."
    )

    return {
        "subskill": "40_enlargement_ratio_of_areas",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ratio_str,
        "expected_answer": ratio_str,
        "sample_answer": ratio_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Square the linear scale factor to obtain area ratio", "marks": 1},
            {"desc": f"State ratio in correct order: {ratio_str}", "marks": 1},
        ],
        "hints": [
            "The area ratio is the square of the linear scale factor.",
            f"k² = ({k})² = {k_sq}.",
            f"Ratio: {ratio_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 41: Angle Invariance Under Enlargement/Reduction
# -----------------------------------------------------------------------------
def arch_41_enlargement_angle_invariance(rng: random.Random, seed: int) -> Dict[str, Any]:
    angle_val = rng.choice([35, 40, 50, 60, 75, 90])
    k = rng.choice([2, 3, 4])

    svg = draw_transformation_grid_svg(
        pre_image=[(1, 1), (3, 1), (2, 3)],
        image=[(2, 2), (2 + 2*k, 2), (2 + k, 2 + 2*k)],
        pre_labels=["A", "B", "C"],
        image_labels=["A'", "B'", "C'"],
        transformation_type="enlargement",
        dilation_center=(0, 0),
        scale_factor=k,
        seed=seed,
        title=f"Angle Invariance Under Dilation (k = {k})",
    )

    prompt = (
        f"In $\\triangle ABC$, interior angle $\\hat{{A}} = {angle_val}^\\circ$. "
        f"The triangle is enlarged by a scale factor of $k = {k}$ to form $\\triangle A'B'C'$. "
        f"Determine the size of the corresponding interior angle $\\hat{{A}}'$ in the enlarged triangle (in degrees)."
    )
    sol = (
        f"A dilation (enlargement or reduction) preserves angle sizes.\n"
        f"The enlarged figure is similar to the original figure, which means all corresponding angles are equal:\n"
        f"$\\hat{{A}}' = \\hat{{A}} = {angle_val}^\\circ$.\n"
        f"Therefore, the size of $\\hat{{A}}'$ is ${angle_val}^\\circ$."
    )

    return {
        "subskill": "41_enlargement_angle_invariance",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(angle_val),
        "expected_answer": str(angle_val),
        "sample_answer": f"{angle_val}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "State that enlargement preserves angle sizes (similarity)", "marks": 1},
            {"desc": f"State angle size: {angle_val}°", "marks": 1},
        ],
        "hints": [
            "Enlargements change side lengths and area, but interior angles NEVER change!",
            f"The image triangle is similar to the original, so angle A' = angle A.",
            f"Answer: {angle_val}°.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 42: Composite Transformation — Reflection Then Translation
# -----------------------------------------------------------------------------
def arch_42_composite_reflection_then_translation(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    axis = rng.choice(["x_axis", "y_axis"])
    dx = rng.choice([-3, -2, 2, 3])
    dy = rng.choice([-3, -2, 2, 3])

    if axis == "x_axis":
        x_mid, y_mid = x, -y
        axis_name = "x-axis"
    else:
        x_mid, y_mid = -x, y
        axis_name = "y-axis"

    xp = x_mid + dx
    yp = y_mid + dy
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P''({xp}; {yp})"],
        transformation_type="none",
        seed=seed,
        title=f"Reflect in {axis_name}, then Translate",
    )

    prompt = (
        f"Point $P{_fmt_pt(x, y)}$ undergoes two successive transformations:\n"
        f"1. First, reflection across the {axis_name}.\n"
        f"2. Second, translation by the rule $(x; y) \\to (x {dx:+d}; y {dy:+d})$.\n"
        f"Determine the final coordinates of the image point $P''$."
    )
    sol = (
        f"Step 1: Reflect $P({x}; {y})$ across the {axis_name}:\n"
        f"   $P{_fmt_pt(x, y)} \\to P'{_fmt_pt(x_mid, y_mid)}$.\n"
        f"Step 2: Translate $P'$ by $(x {dx:+d}; y {dy:+d})$:\n"
        f"   $x'' = {x_mid} {dx:+d} = {xp}$\n"
        f"   $y'' = {y_mid} {dy:+d} = {yp}$\n"
        f"Therefore, the final image point is $P''{ans_str}$."
    )

    return {
        "subskill": "42_composite_reflection_then_translation",
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
            {"desc": f"Correct intermediate coordinates P': {_fmt_pt(x_mid, y_mid)}", "marks": 1},
            {"desc": f"Apply translation shifts to P'", "marks": 1},
            {"desc": f"Final coordinates P'': {ans_str}", "marks": 1},
        ],
        "hints": [
            f"First apply reflection in {axis_name}: P' = ({x_mid}; {y_mid}).",
            f"Next add {dx} to x and {dy} to y.",
            f"Final image P'' is {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 43: Composite Transformation — Translation Then Reflection
# -----------------------------------------------------------------------------
def arch_43_composite_translation_then_reflection(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    dx = rng.choice([-3, -2, 2, 3])
    dy = rng.choice([-3, -2, 2, 3])
    axis = rng.choice(["x_axis", "y_axis"])

    x_mid = x + dx
    y_mid = y + dy

    if axis == "x_axis":
        xp = x_mid
        yp = -y_mid
        axis_name = "x-axis"
    else:
        xp = -x_mid
        yp = y_mid
        axis_name = "y-axis"

    ans_str = _fmt_pt(xp, yp)
    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P''({xp}; {yp})"],
        transformation_type="none",
        seed=seed,
        title=f"Translate, then Reflect in {axis_name}",
    )

    prompt = (
        f"Point $P{_fmt_pt(x, y)}$ undergoes two successive transformations:\n"
        f"1. First, translation by the rule $(x; y) \\to (x {dx:+d}; y {dy:+d})$.\n"
        f"2. Second, reflection across the {axis_name}.\n"
        f"Determine the final coordinates of the image point $P''$."
    )
    sol = (
        f"Step 1: Translate $P({x}; {y})$ by $(x {dx:+d}; y {dy:+d})$:\n"
        f"   $P'({x} {dx:+d}; {y} {dy:+d}) = P'{_fmt_pt(x_mid, y_mid)}$.\n"
        f"Step 2: Reflect $P'$ across the {axis_name}:\n"
        f"   $P'{_fmt_pt(x_mid, y_mid)} \\to P''{ans_str}$.\n"
        f"Therefore, the final coordinates are $P''{ans_str}$."
    )

    return {
        "subskill": "43_composite_translation_then_reflection",
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
            {"desc": f"Correct intermediate coordinates after translation: {_fmt_pt(x_mid, y_mid)}", "marks": 1},
            {"desc": f"Apply {axis_name} reflection to intermediate point", "marks": 1},
            {"desc": f"Final coordinates P'': {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Step 1: P' = ({x + dx}; {y + dy}) = {_fmt_pt(x_mid, y_mid)}.",
            f"Step 2: Reflect P' across {axis_name}.",
            f"Final image P'' is {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 44: Double Reflection in Parallel Axes
# -----------------------------------------------------------------------------
def arch_44_composite_double_reflection_parallel_axes(rng: random.Random, seed: int) -> Dict[str, Any]:
    c = rng.choice([1, 2, 3])
    x = rng.randint(-4, 0)
    y = rng.randint(-3, 3)

    # First reflection in y-axis (x = 0): (-x; y)
    # Second reflection in line x = c: (2c - (-x); y) = (x + 2c; y)
    # Equivalent to a translation by 2c to the right!
    shift = 2 * c
    xp = x + shift
    yp = y
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P''({xp}; {yp})"],
        transformation_type="none",
        seed=seed,
        title=f"Double Reflection in x = 0 and x = {c}",
    )

    prompt = (
        f"Point $P{_fmt_pt(x, y)}$ is reflected across the $y$-axis (the line $x = 0$) to point $P'$, "
        f"and $P'$ is then reflected across the vertical line $x = {c}$ to point $P''$.\n"
        f"Determine the final coordinates of $P''$."
    )
    sol = (
        f"Step 1: Reflect across the $y$-axis ($x = 0$):\n"
        f"   $P({x}; {y}) \\to P'(-({x}); {y}) = P'({-x}; {y})$.\n"
        f"Step 2: Reflect $P'$ across the line $x = {c}$:\n"
        f"   $x'' = 2({c}) - ({-x}) = {2*c} + {x} = {xp}$.\n"
        f"   $y'' = {y}$.\n"
        f"Note: Reflecting across two parallel lines separated by distance $d = {c}$ is equivalent to a translation by $2d = {shift}$ units.\n"
        f"Therefore, the final coordinates are $P''{ans_str}$."
    )

    return {
        "subskill": "44_composite_double_reflection_parallel_axes",
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
            {"desc": f"Correct first reflection across y-axis: P'({-x}; {y})", "marks": 1},
            {"desc": f"Correct second reflection across x = {c}", "marks": 1},
            {"desc": f"Final coordinates P'': {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Step 1: P' is ({-x}; {y}).",
            f"Step 2: x'' = 2*{c} - ({-x}) = {xp}.",
            f"P'' is {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 45: Double Reflection in Perpendicular Axes (180° Rotation)
# -----------------------------------------------------------------------------
def arch_45_composite_double_reflection_perpendicular_axes(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    y = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    xp, yp = -x, -y
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P''({xp}; {yp})"],
        transformation_type="rotation",
        rotation_center=(0, 0),
        rotation_angle_deg=180,
        seed=seed,
        title="Double Reflection in Both Axes = 180° Rotation",
    )

    prompt = (
        f"Point $P{_fmt_pt(x, y)}$ is first reflected across the $x$-axis, "
        f"and the resulting point is then reflected across the $y$-axis.\n"
        f"(a) Determine the final coordinates of image point $P''$.\n"
        f"(b) What single transformation is geometrically equivalent to this double reflection?"
    )
    sol = (
        f"1. Reflect across the $x$-axis: $P({x}; {y}) \\to P'({x}; {-y})$.\n"
        f"2. Reflect $P'$ across the $y$-axis: $P'({x}; {-y}) \\to P''({-x}; {-y}) = P''{ans_str}$.\n"
        f"Notice that $(x; y) \\to (-x; -y)$ is mathematically identical to a rotation of $180^\\circ$ about the origin $O(0; 0)$.\n"
        f"Therefore, the final coordinates are {ans_str} and the single transformation is a rotation of 180° about the origin."
    )

    return {
        "subskill": "45_composite_double_reflection_perpendicular_axes",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans_str,
        "expected_answer": ans_str,
        "sample_answer": f"{ans_str} (Equivalent to 180° rotation about origin)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Correct image coordinates {ans_str}", "marks": 2},
            {"desc": "Identify equivalence to 180° rotation about origin", "marks": 1},
        ],
        "hints": [
            "Reflecting in the x-axis negates y; reflecting in the y-axis negates x.",
            f"Both signs flip: ({x}; {y}) -> ({-x}; {-y}).",
            f"Answer: {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 46: Composite Transformation — Rotation Then Translation
# -----------------------------------------------------------------------------
def arch_46_composite_rotation_then_translation(rng: random.Random, seed: int) -> Dict[str, Any]:
    x = rng.choice([-3, -2, -1, 1, 2, 3])
    y = rng.choice([-3, -2, -1, 1, 2, 3])
    dx = rng.choice([-3, -2, 2, 3])
    dy = rng.choice([-3, -2, 2, 3])

    # 90 deg clockwise rotation about origin: (y; -x)
    x_rot, y_rot = y, -x
    xp, yp = x_rot + dx, y_rot + dy
    ans_str = _fmt_pt(xp, yp)

    svg = draw_transformation_grid_svg(
        pre_image=[(x, y)],
        image=[(xp, yp)],
        pre_labels=[f"P({x}; {y})"],
        image_labels=[f"P''({xp}; {yp})"],
        transformation_type="none",
        seed=seed,
        title="Rotate 90° CW then Translate",
    )

    prompt = (
        f"Point $P{_fmt_pt(x, y)}$ undergoes two successive transformations:\n"
        f"1. A $90^\\circ$ clockwise rotation about the origin $O(0; 0)$.\n"
        f"2. A translation by $(x {dx:+d}; y {dy:+d})$.\n"
        f"Determine the final coordinates of $P''$."
    )
    sol = (
        f"Step 1: Rotate $90^\\circ$ clockwise about the origin: $(x; y) \\to (y; -x)$.\n"
        f"   $P{_fmt_pt(x, y)} \\to P'{_fmt_pt(x_rot, y_rot)}$.\n"
        f"Step 2: Translate $P'$ by $(x {dx:+d}; y {dy:+d})$:\n"
        f"   $x'' = {x_rot} {dx:+d} = {xp}$\n"
        f"   $y'' = {y_rot} {dy:+d} = {yp}$\n"
        f"Therefore, the final coordinates are $P''{ans_str}$."
    )

    return {
        "subskill": "46_composite_rotation_then_translation",
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
            {"desc": f"Correct 90° clockwise rotation to P': {_fmt_pt(x_rot, y_rot)}", "marks": 1},
            {"desc": f"Apply translation shifts to P'", "marks": 1},
            {"desc": f"Final coordinates P'': {ans_str}", "marks": 1},
        ],
        "hints": [
            f"Step 1: 90° CW rotation gives P'({y}; -{x}) = {_fmt_pt(x_rot, y_rot)}.",
            f"Step 2: Add {dx} to x and {dy} to y.",
            f"Final point P'' is {ans_str}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 47: Identify Single Transformation Type from Coordinates
# -----------------------------------------------------------------------------
def arch_47_identify_transformation_type(rng: random.Random, seed: int) -> Dict[str, Any]:
    types = [
        ("translation", "Translation", (2, 3), (5, 1), "both coordinates shifted by constant values without flipping or rotating"),
        ("reflection", "Reflection", (3, -2), (3, 2), "the y-coordinate changed sign while the x-coordinate remained unchanged (reflection across x-axis)"),
        ("rotation", "Rotation", (2, 4), (-4, 2), "coordinates swapped and one changed sign: (x; y) -> (-y; x), representing 90° anti-clockwise rotation"),
        ("enlargement", "Enlargement", (2, 3), (6, 9), "both coordinates are multiplied by the same scale factor k = 3"),
    ]
    t_key, t_name, p1, p2, reason = rng.choice(types)

    svg = draw_transformation_grid_svg(
        pre_image=[p1],
        image=[p2],
        pre_labels=[f"P{_fmt_pt(*p1)}"],
        image_labels=[f"P'{_fmt_pt(*p2)}"],
        transformation_type="none",
        seed=seed,
        title=f"Identify Transformation",
    )

    prompt = (
        f"In the Cartesian plane diagram, pre-image $P{_fmt_pt(*p1)}$ is transformed to image $P'{_fmt_pt(*p2)}$. "
        f"Identify the single transformation type that occurred (choose from: 'Translation', 'Reflection', 'Rotation', or 'Enlargement')."
    )
    sol = (
        f"Comparing the coordinates $P{_fmt_pt(*p1)}$ and $P'{_fmt_pt(*p2)}$:\n"
        f"Reason: {reason}.\n"
        f"Therefore, the transformation is a {t_name}."
    )

    return {
        "subskill": "47_identify_transformation_type",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": t_name,
        "expected_answer": t_name,
        "sample_answer": f"{t_name} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Analyze coordinate relationship between pre-image and image", "marks": 1},
            {"desc": f"Correctly identify transformation: {t_name}", "marks": 1},
        ],
        "hints": [
            "Check if points are shifted by addition, negated by reflection, turned by rotation, or scaled by multiplication.",
            f"Here, {reason}.",
            f"The transformation is {t_name}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 48: Invariant (Fixed) Points Under Transformations
# -----------------------------------------------------------------------------
def arch_48_invariant_points_lines(rng: random.Random, seed: int) -> Dict[str, Any]:
    scenarios = [
        ("reflection in the x-axis", "y = 0", "Any point lying on the x-axis (where y = 0) has coordinates (x; 0). Under reflection (x; -0) = (x; 0), so the point does not move."),
        ("reflection in the y-axis", "x = 0", "Any point lying on the y-axis (where x = 0) has coordinates (0; y). Under reflection (-0; y) = (0; y), so it remains fixed."),
        ("reflection in the line y = x", "y = x", "Any point lying on the line y = x has coordinates (a; a). Swapping coordinates gives (a; a), which is identical."),
        ("rotation of 90° about the origin", "(0; 0)", "The only invariant point under a rotation about the origin is the center of rotation itself, the origin (0; 0)."),
        ("enlargement by scale factor k = 2 about the origin", "(0; 0)", "The center of enlargement (0; 0) is the only fixed point, since (k*0; k*0) = (0; 0)."),
    ]
    trans_name, invariant_desc, reason = rng.choice(scenarios)

    svg = draw_transformation_grid_svg(
        pre_image=[(0, 0)],
        pre_labels=["O(0; 0)"],
        transformation_type="none",
        seed=seed,
        title="Invariant (Fixed) Points",
    )

    prompt = (
        f"An invariant point is a point that does not change position under a geometric transformation.\n"
        f"Identify all invariant points under a {trans_name}."
    )
    sol = (
        f"For a {trans_name}:\n"
        f"{reason}\n"
        f"Therefore, the invariant condition is: {invariant_desc}."
    )

    return {
        "subskill": "48_invariant_points_lines",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": invariant_desc,
        "expected_answer": invariant_desc,
        "sample_answer": f"{invariant_desc} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify condition where pre-image equals image", "marks": 1},
            {"desc": f"State invariant point(s) or line: {invariant_desc}", "marks": 1},
        ],
        "hints": [
            "An invariant point satisfies: Image = Pre-image.",
            "For reflections, all points ON the mirror line are invariant. For rotations, the center of rotation is invariant.",
            f"The answer is {invariant_desc}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 49: Isometry (Congruence) vs Similarity Classification
# -----------------------------------------------------------------------------
def arch_49_isometry_congruence_vs_similarity(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("Translation", "Congruent (Isometry)", "Translations preserve both side lengths and angle sizes without changing the size or shape of the figure."),
        ("Reflection", "Congruent (Isometry)", "Reflections preserve side lengths and angle sizes (though orientation/handedness is reversed), producing congruent figures."),
        ("Rotation", "Congruent (Isometry)", "Rotations preserve distances and angle measures, producing congruent figures."),
        ("Enlargement with scale factor k = 3", "Similar (Not congruent)", "Enlargements preserve angle sizes but multiply side lengths by k = 3, producing figures of the same shape but different sizes."),
        ("Reduction with scale factor k = 1/2", "Similar (Not congruent)", "Reductions preserve angle sizes but halve side lengths, producing similar figures of different sizes."),
    ]
    t_name, classification, reason = rng.choice(choices)

    svg = draw_transformation_grid_svg(
        pre_image=[(-2, -2), (2, -2), (0, 2)],
        pre_labels=["A", "B", "C"],
        transformation_type="none",
        seed=seed,
        title=f"{t_name}: Congruence vs Similarity",
    )

    prompt = (
        f"Consider the transformation: **{t_name}**.\n"
        f"Does this transformation produce an image that is 'Congruent (Isometry)' or 'Similar (Not congruent)' to the original figure?"
    )
    sol = (
        f"For **{t_name}**:\n"
        f"{reason}\n"
        f"Therefore, the image is **{classification}**."
    )

    return {
        "subskill": "49_isometry_congruence_vs_similarity",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": classification,
        "expected_answer": classification,
        "sample_answer": f"{classification} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Classify transformation into rigid motion (isometry) or dilation", "marks": 1},
            {"desc": f"State correct classification: {classification}", "marks": 1},
        ],
        "hints": [
            "Translations, reflections, and rotations are isometries (rigid motions) that preserve size and shape (congruent).",
            "Enlargements and reductions with scale factor k ≠ 1 change the size but preserve angles (similar).",
            f"The answer is {classification}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 50: Coordinate Mapping Notation and Algebraic Rule Synthesis
# -----------------------------------------------------------------------------
def arch_50_coordinate_mapping_notation_algebraic_rule(rng: random.Random, seed: int) -> Dict[str, Any]:
    rules = [
        ("reflection in the x-axis", "(x; -y)"),
        ("reflection in the y-axis", "(-x; y)"),
        ("reflection in the line y = x", "(y; x)"),
        ("reflection in the line y = -x", "(-y; -x)"),
        ("90° clockwise rotation about the origin", "(y; -x)"),
        ("90° anti-clockwise rotation about the origin", "(-y; x)"),
        ("180° rotation about the origin", "(-x; -y)"),
        ("enlargement by scale factor k = 2 about the origin", "(2x; 2y)"),
        ("enlargement by scale factor k = 3 about the origin", "(3x; 3y)"),
    ]
    name, rule_rhs = rng.choice(rules)
    full_rule = f"(x; y) -> {rule_rhs}"

    svg = draw_transformation_grid_svg(
        pre_image=[(2, 3)],
        pre_labels=["(x; y)"],
        transformation_type="none",
        seed=seed,
        title=f"Algebraic Rule for {name}",
    )

    prompt = (
        f"Write down the general algebraic coordinate mapping rule for a **{name}** "
        f"in the notation $(x; y) \\to (\\dots; \\dots)$."
    )
    sol = (
        f"Under a {name}, any point $(x; y)$ maps according to:\n"
        f"$(x; y) \\to {rule_rhs}$.\n"
        f"Therefore, the coordinate rule is ${full_rule}$."
    )

    return {
        "subskill": "50_coordinate_mapping_notation_algebraic_rule",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": rule_rhs,
        "expected_answer": rule_rhs,
        "sample_answer": full_rule,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify standard transformation formula", "marks": 1},
            {"desc": f"State correct image coordinate formula: {rule_rhs}", "marks": 1},
        ],
        "hints": [
            f"Recall the general coordinate formula for a {name}.",
            f"The image coordinates in terms of x and y are {rule_rhs}.",
            f"The rule is (x; y) -> {rule_rhs}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }
