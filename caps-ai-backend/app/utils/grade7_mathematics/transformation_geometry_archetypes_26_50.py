"""Grade 7 Mathematics - Transformation Geometry: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/04. Transformation geometry.md
Focus: Reflections (axes, lines, properties), Rotations (90°, 180°, center of rotation), Enlargements/Reductions (scale factor k, area effect k²), Similar vs Congruent, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_reflection_diagram(ox: int, oy: int, rx: int, ry: int, axis: str = "y-axis") -> str:
    """Renders a coordinate plane showing reflection across an axis."""
    w, h = 320, 240
    cx, cy = 160, 120
    scale = 16

    ax_svg = cx + ox * scale
    ay_svg = cy - oy * scale
    rx_svg = cx + rx * scale
    ry_svg = cy - ry * scale

    grid = [
        f'<line x1="20" y1="{cy}" x2="300" y2="{cy}" stroke="#94a3b8" stroke-width="1.5"/>',
        f'<line x1="{cx}" y1="20" x2="{cx}" y2="220" stroke="#94a3b8" stroke-width="1.5"/>',
        f'<text x="295" y="{cy-6}" font-size="11" fill="#64748b">x</text>',
        f'<text x="{cx+6}" y="30" font-size="11" fill="#64748b">y</text>'
    ]

    mirror_highlight = (
        f'<line x1="{cx}" y1="20" x2="{cx}" y2="220" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5,3"/>'
        if axis == "y-axis" else
        f'<line x1="20" y1="{cy}" x2="300" y2="{cy}" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5,3"/>'
    )

    connect = f'<line x1="{ax_svg}" y1="{ay_svg}" x2="{rx_svg}" y2="{ry_svg}" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3,3"/>'
    p1 = f'<circle cx="{ax_svg}" cy="{ay_svg}" r="5" fill="#2563eb"/><text x="{ax_svg+6}" y="{ay_svg-6}" font-size="11" font-weight="bold" fill="#1e3a8a">P({ox};{oy})</text>'
    p2 = f'<circle cx="{rx_svg}" cy="{ry_svg}" r="5" fill="#16a34a"/><text x="{rx_svg+6}" y="{ry_svg-6}" font-size="11" font-weight="bold" fill="#14532d">P\'({rx};{ry})</text>'

    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'{"".join(grid)}'
        f'{mirror_highlight}{connect}{p1}{p2}'
        f'</svg>'
    )


def _svg_scale_factor_diagram(k: int = 2) -> str:
    """Renders two similar rectangles illustrating scale factor k."""
    w, h = 340, 180
    rect1 = '<rect x="30" y="70" width="60" height="40" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
    label1 = '<text x="60" y="95" text-anchor="middle" font-size="11" fill="#0369a1">A</text>'
    dim1 = '<text x="60" y="62" text-anchor="middle" font-size="10" fill="#64748b">3 cm</text><text x="20" y="95" font-size="10" fill="#64748b">2 cm</text>'

    w2 = 60 * k
    h2 = 40 * k
    rect2 = f'<rect x="140" y="{110 - h2}" width="{w2}" height="{h2}" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
    label2 = f'<text x="{140 + w2/2}" y="{110 - h2/2}" text-anchor="middle" font-size="11" fill="#15803d">A\'</text>'
    dim2 = f'<text x="{140 + w2/2}" y="{102 - h2}" text-anchor="middle" font-size="10" fill="#64748b">{3*k} cm</text><text x="{145 + w2}" y="{110 - h2/2}" font-size="10" fill="#64748b">{2*k} cm</text>'

    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'{rect1}{label1}{dim1}{rect2}{label2}{dim2}'
        f'<text x="170" y="165" text-anchor="middle" font-size="11" fill="#334155">Scale Factor k = {k}</text>'
        f'</svg>'
    )


# 26. Reflection definition and mirror line concept
def arch_26_reflection_definition_and_mirror_concept(rng: random.Random) -> Dict[str, Any]:
    ans = "A transformation that flips a figure across a mirror line so each point and its image are equidistant from the line"
    prompt = (
        "In transformation geometry, define what a **reflection** is, and state the relationship between "
        "the line of reflection and the line segment connecting an original point $P$ to its image $P'$."
    )
    sol = (
        "**Definition:**\n"
        "A reflection is a transformation that flips a figure over a line of reflection (mirror line).\n\n"
        "**Perpendicular Bisector Property:**\n"
        "The line of reflection is the **perpendicular bisector** of the segment $PP'$ connecting each original point to its image:\n"
        "1. The segment $PP'$ is perpendicular ($90^\\circ$) to the line of reflection.\n"
        "2. The line of reflection bisects $PP'$, meaning $P$ and $P'$ are equidistant from the mirror line."
    )
    return {
        "id": f"g7_tg_26_{rng.randint(100000, 999999)}",
        "subskill": "26_reflection_definition_and_mirror_concept",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Flips a figure across a line; the line of reflection is the perpendicular bisector of PP'",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_26",
        "hints": {
            "tier_1": "Think of a flat mirror. How does an object line up with its reflection?",
            "tier_2": "The distance from object to mirror equals distance from image to mirror, at a 90° angle.",
            "tier_3": "Line of reflection is the perpendicular bisector of segment connecting point to its image."
        },
        "misconception_tags": ["confusing_reflection_with_translation"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Defines reflection as flipping across mirror line", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States perpendicular bisector / equidistant property", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 27. Reflection across vertical line x = c
def arch_27_reflection_across_vertical_line(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 4, 5])
    dist = rng.choice([1, 2, 3])
    x_val = c - dist
    y_val = rng.randint(2, 7)
    rx = c + dist
    ans = f"({rx}; {y_val})"
    prompt = (
        f"Point $A({x_val}; {y_val})$ is reflected across the vertical line $x = {c}$.\n\n"
        f"Calculate the coordinates of the reflected position point $A'$."
    )
    sol = (
        f"**Step 1: Find perpendicular distance to mirror line:**\n"
        f"The mirror line is $x = {c}$.\n"
        f"Distance from $A$ to line: ${c} - ({x_val}) = {dist}$ units to the left.\n\n"
        f"**Step 2: Place image at equal distance to the right:**\n"
        f"$$x' = {c} + {dist} = {rx}$$\n"
        f"The vertical position does not change during a reflection across a vertical line:\n"
        f"$$y' = {y_val}$$\n\n"
        f"$$\\therefore A'({rx}; {y_val})$$"
    )
    return {
        "id": f"g7_tg_27_{rng.randint(100000, 999999)}",
        "subskill": "27_reflection_across_vertical_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"A'({rx}; {y_val})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_27",
        "hints": {
            "tier_1": f"Point A is {dist} units left of x = {c}.",
            "tier_2": f"Image A' must be {dist} units right of x = {c}, so x' = {c} + {dist}.",
            "tier_3": f"Coordinates are ({rx}; {y_val})."
        },
        "misconception_tags": ["inverting_y_in_vertical_reflection"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates x' = {rx}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Keeps y' = {y_val}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 28. Reflection across horizontal line y = d
def arch_28_reflection_across_horizontal_line(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5])
    dist = rng.choice([1, 2, 3])
    x_val = rng.randint(2, 6)
    y_val = d + dist
    ry = d - dist
    ans = f"({x_val}; {ry})"
    prompt = (
        f"Point $B({x_val}; {y_val})$ is reflected across the horizontal line $y = {d}$.\n\n"
        f"Determine the coordinates of the reflected position point $B'$."
    )
    sol = (
        f"**Step 1: Distance to the horizontal mirror line:**\n"
        f"The mirror line is $y = {d}$.\n"
        f"Distance from $B$ to line: ${y_val} - {d} = {dist}$ units above.\n\n"
        f"**Step 2: Place image at equal distance below:**\n"
        f"$$y' = {d} - {dist} = {ry}$$\n"
        f"The horizontal position is unchanged:\n"
        f"$$x' = {x_val}$$\n\n"
        f"$$\\therefore B'({x_val}; {ry})$$"
    )
    return {
        "id": f"g7_tg_28_{rng.randint(100000, 999999)}",
        "subskill": "28_reflection_across_horizontal_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"B'({x_val}; {ry})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_28",
        "hints": {
            "tier_1": f"Point B is {dist} units above y = {d}.",
            "tier_2": f"Image B' is {dist} units below: y' = {d} - {dist}.",
            "tier_3": f"Coordinates are ({x_val}; {ry})."
        },
        "misconception_tags": ["inverting_x_in_horizontal_reflection"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Keeps x' = {x_val}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates y' = {ry}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 29. Reflection across y-axis: (x, y) -> (-x, y)
def arch_29_reflection_across_y_axis(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(2, 7)
    y_val = rng.randint(2, 8)
    ans = f"(-{x_val}; {y_val})"
    svg = _svg_reflection_diagram(x_val, y_val, -x_val, y_val, "y-axis")
    prompt = (
        f"The Cartesian diagram illustrates point $P({x_val}; {y_val})$ and the $y$-axis (shown as a dashed red line):\n\n"
        f"1. Write down the algebraic coordinate rule for a reflection across the $y$-axis: $(x; y) \\to (\\dots; \\dots)$.\n"
        f"2. Apply this rule to find the transformed point coordinates of point $P({x_val}; {y_val})$."
    )
    sol = (
        f"**1. Algebraic Rule for $y$-axis reflection:**\n"
        f"When reflecting across the $y$-axis, the $x$-coordinate changes sign, while the $y$-coordinate remains the same:\n"
        f"$$(x; y) \\to (-x; y)$$\n\n"
        f"**2. Apply to $P({x_val}; {y_val})$:**\n"
        f"$$P'(-{x_val}; {y_val})$$"
    )
    return {
        "id": f"g7_tg_29_{rng.randint(100000, 999999)}",
        "subskill": "29_reflection_across_y_axis",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"1. (x; y) -> (-x; y); 2. (-{x_val}; {y_val})",
        "sample_answer": f"(x; y) -> (-x; y) and P'(-{x_val}; {y_val})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_29",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Across the vertical y-axis, right becomes left.",
            "tier_2": f"Change sign of x: x becomes -{x_val}. y stays {y_val}.",
            "tier_3": f"P'(-{x_val}; {y_val})."
        },
        "misconception_tags": ["negating_wrong_coordinate_in_y_axis_reflection"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States rule (x; y) -> (-x; y)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates P'(-{x_val}; {y_val})", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 30. Reflection across x-axis: (x, y) -> (x, -y)
def arch_30_reflection_across_x_axis(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(2, 8)
    y_val = rng.randint(2, 6)
    ans = f"({x_val}; -{y_val})"
    svg = _svg_reflection_diagram(x_val, y_val, x_val, -y_val, "x-axis")
    prompt = (
        f"Point $Q({x_val}; {y_val})$ is reflected across the $x$-axis on a Cartesian plane:\n\n"
        f"1. Write down the algebraic coordinate rule for a reflection across the $x$-axis: $(x; y) \\to (\\dots; \\dots)$.\n"
        f"2. State the transformed point coordinates $Q'$."
    )
    sol = (
        f"**1. Algebraic Rule for $x$-axis reflection:**\n"
        f"When reflecting across the horizontal $x$-axis, the $x$-coordinate remains unchanged and the $y$-coordinate changes sign:\n"
        f"$$(x; y) \\to (x; -y)$$\n\n"
        f"**2. Apply to $Q({x_val}; {y_val})$:**\n"
        f"$$Q'({x_val}; -{y_val})$$"
    )
    return {
        "id": f"g7_tg_30_{rng.randint(100000, 999999)}",
        "subskill": "30_reflection_across_x_axis",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"1. (x; y) -> (x; -y); 2. ({x_val}; -{y_val})",
        "sample_answer": f"(x; y) -> (x; -y) and Q'({x_val}; -{y_val})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_30",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Across the horizontal x-axis, top flips to bottom.",
            "tier_2": f"x stays {x_val}; y changes sign to -{y_val}.",
            "tier_3": f"Q'({x_val}; -{y_val})."
        },
        "misconception_tags": ["negating_wrong_coordinate_in_x_axis_reflection"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States rule (x; y) -> (x; -y)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates Q'({x_val}; -{y_val})", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 31. Reflection across diagonal line y = x
def arch_31_reflection_across_line_y_equals_x(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(2, 5)
    y_val = rng.randint(6, 9)
    ans = f"({y_val}; {x_val})"
    prompt = (
        f"Point $R({x_val}; {y_val})$ is reflected across the $45^\\circ$ diagonal line $y = x$.\n\n"
        f"1. State the algebraic coordinate rule for reflection in the line $y = x$.\n"
        f"2. Determine the transformed point coordinates $R'$."
    )
    sol = (
        f"**1. Algebraic Rule for reflection in $y = x$:**\n"
        f"Reflecting across the line $y = x$ interchanges the $x$ and $y$ coordinates:\n"
        f"$$(x; y) \\to (y; x)$$\n\n"
        f"**2. Apply to $R({x_val}; {y_val})$:**\n"
        f"$$R'({y_val}; {x_val})$$"
    )
    return {
        "id": f"g7_tg_31_{rng.randint(100000, 999999)}",
        "subskill": "31_reflection_across_line_y_equals_x",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"1. (x; y) -> (y; x); 2. ({y_val}; {x_val})",
        "sample_answer": f"(x; y) -> (y; x) and R'({y_val}; {x_val})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_31",
        "hints": {
            "tier_1": "In line y = x, the x-value becomes the y-value, and the y-value becomes the x-value.",
            "tier_2": f"Swap coordinates: ({x_val}; {y_val}) becomes ({y_val}; {x_val}).",
            "tier_3": f"R'({y_val}; {x_val})."
        },
        "misconception_tags": ["negating_instead_of_swapping_in_y_equals_x"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States rule (x; y) -> (y; x)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Determines coordinates ({y_val}; {x_val})", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 32. Perpendicular distance property
def arch_32_perpendicular_distance_property(rng: random.Random) -> Dict[str, Any]:
    ans = "Equidistant; perpendicular (90 degrees)"
    prompt = (
        "In any reflection across a mirror line $m$:\n\n"
        "1. What is the relationship between the distance from original point $A$ to line $m$ and the distance from reflected point $A'$ to line $m$?\n"
        "2. At what angle does the line segment $AA'$ intersect the mirror line $m$?"
    )
    sol = (
        "**Properties of Reflection:**\n"
        "1. **Distance:** The original point $A$ and its reflected position $A'$ are **equidistant** (the exact same perpendicular distance) from the mirror line $m$.\n"
        "2. **Angle:** The segment $AA'$ intersects the mirror line $m$ at a right angle (**$90^\\circ$ / perpendicular**).\n\n"
        "Hence, line $m$ is the perpendicular bisector of segment $AA'$."
    )
    return {
        "id": f"g7_tg_32_{rng.randint(100000, 999999)}",
        "subskill": "32_perpendicular_distance_property",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1. Equal distance (equidistant); 2. 90 degrees (perpendicular)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_32",
        "hints": {
            "tier_1": "Think of looking straight into a mirror.",
            "tier_2": "The distance in front equals the distance behind, and the line of sight is perpendicular.",
            "tier_3": "Equidistant and 90 degrees (perpendicular)."
        },
        "misconception_tags": ["slanted_reflection_misconception"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States equal distance / equidistant", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States perpendicular / 90 degrees", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 33. Orientation reversal in reflection (lateral inversion)
def arch_33_orientation_reversal_lateral_inversion(rng: random.Random) -> Dict[str, Any]:
    ans = "Orientation is reversed (laterally inverted); clockwise vertices become anticlockwise"
    prompt = (
        "Consider triangle $ABC$ with vertices labeled in clockwise order.\n"
        "When triangle $ABC$ is reflected across a line of reflection to produce image $A'B'C'$:\n\n"
        "1. Does the **orientation** (order of vertices) stay the same or reverse?\n"
        "2. Explain what lateral inversion means in the context of reflections."
    )
    sol = (
        "**1. Orientation:**\n"
        "The orientation is **reversed** (clockwise becomes anticlockwise).\n\n"
        "**2. Lateral Inversion:**\n"
        "Lateral inversion means that left and right are swapped relative to the mirror line. "
        "Unlike translation and rotation, reflection creates a mirror image that cannot be superimposed on the original shape simply by sliding or turning."
    )
    return {
        "id": f"g7_tg_33_{rng.randint(100000, 999999)}",
        "subskill": "33_orientation_reversal_lateral_inversion",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Reversed (clockwise becomes anticlockwise); left and right are swapped",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_33",
        "hints": {
            "tier_1": "If you raise your right hand in front of a mirror, which hand does your reflection raise?",
            "tier_2": "The reflection raises its left hand. The orientation is flipped.",
            "tier_3": "Orientation is reversed (laterally inverted)."
        },
        "misconception_tags": ["assuming_reflection_preserves_orientation"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States orientation is reversed", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains clockwise becomes anticlockwise / lateral inversion", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 34. Finding the mirror line given object and image
def arch_34_finding_mirror_line_from_points(rng: random.Random) -> Dict[str, Any]:
    mid_x = rng.choice([3, 4, 5, 6])
    dist = rng.choice([2, 3])
    x1 = mid_x - dist
    x2 = mid_x + dist
    y_val = rng.randint(2, 7)
    ans = f"x = {mid_x}"
    prompt = (
        f"Original point $P({x1}; {y_val})$ is reflected to image point $P'({x2}; {y_val})$.\n\n"
        f"Find the equation of the line of reflection."
    )
    sol = (
        f"**Step 1: Inspect coordinates:**\n"
        f"Both points have the same $y$-coordinate ($y = {y_val}$).\n"
        f"Therefore, the segment $PP'$ is horizontal, which means the line of reflection must be **vertical** ($x = c$).\n\n"
        f"**Step 2: Find the midpoint:**\n"
        f"The line of reflection passes through the midpoint of the segment $PP'$:\n"
        f"$$x = \\frac{{{x1} + {x2}}}{{2}} = \\frac{{{x1 + x2}}}{{2}} = {mid_x}$$\n\n"
        f"$$\\therefore \\text{{Line of reflection: }} x = {mid_x}$$"
    )
    return {
        "id": f"g7_tg_34_{rng.randint(100000, 999999)}",
        "subskill": "34_finding_mirror_line_from_points",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"x = {mid_x}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_34",
        "hints": {
            "tier_1": "Find the halfway point between the two x-coordinates.",
            "tier_2": f"Midpoint = ({x1} + {x2}) / 2 = {mid_x}.",
            "tier_3": f"Line of reflection is x = {mid_x}."
        },
        "misconception_tags": ["confusing_vertical_horizontal_line_equations"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates midpoint coordinate correctly", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"States line equation x = {mid_x}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 35. Reflection SVG visual representation
def arch_35_reflection_svg_visual_grid(rng: random.Random) -> Dict[str, Any]:
    ox, oy = rng.randint(2, 6), rng.randint(2, 6)
    rx, ry = -ox, oy
    svg = _svg_reflection_diagram(ox, oy, rx, ry, "y-axis")
    ans = f"Reflected across the y-axis; P'({rx}; {ry})"
    prompt = (
        "Examine the reflection diagram below:\n\n"
        f"1. Identify the line of reflection shown by the dashed red line.\n"
        f"2. Read the coordinates of the transformed point $P'$."
    )
    sol = (
        "**1. Line of Reflection:**\n"
        "The dashed line is the vertical axis, which is the **$y$-axis** ($x = 0$).\n\n"
        "**2. Reflected Coordinates:**\n"
        "The reflected point $P'$ is located at:\n"
        f"$$P'({rx}; {ry})$$"
    )
    return {
        "id": f"g7_tg_35_{rng.randint(100000, 999999)}",
        "subskill": "35_reflection_svg_visual_grid",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"y-axis; P'({rx}; {ry})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_35",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "The vertical axis with x=0 is the y-axis.",
            "tier_2": f"Point P'({rx}; {ry}) is {ox} units left of the y-axis at y = {ry}.",
            "tier_3": f"{ans}"
        },
        "misconception_tags": ["confusing_x_and_y_axes"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies y-axis as mirror line", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"States coordinates P'({rx}; {ry})", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 36. Double reflection across parallel lines
def arch_36_double_reflection_across_parallel_lines(rng: random.Random) -> Dict[str, Any]:
    ans = "A translation (slide) by twice the distance between the two parallel lines"
    prompt = (
        "A figure undergoes two successive reflections across two parallel lines that are $4\\text{ cm}$ apart.\n\n"
        "1. What single transformation is equivalent to two successive reflections across parallel lines?\n"
        "2. What is the total distance the shape is displaced?"
    )
    sol = (
        "**1. Equivalent Transformation:**\n"
        "Two successive reflections across parallel lines result in a **translation** (slide).\n\n"
        "**2. Displacement Distance:**\n"
        "The translation distance is **twice** the distance between the two parallel mirror lines:\n"
        "$$\\text{Distance} = 2 \\times 4\\text{ cm} = 8\\text{ cm}$$"
    )
    return {
        "id": f"g7_tg_36_{rng.randint(100000, 999999)}",
        "subskill": "36_double_reflection_across_parallel_lines",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": "1. Translation; 2. 8 cm",
        "sample_answer": "Translation of 8 cm (twice the distance between the parallel lines)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_36",
        "hints": {
            "tier_1": "The first reflection flips the shape, and the second reflection flips it back facing forward.",
            "tier_2": "Flipping twice preserves orientation, which is a translation.",
            "tier_3": "It is a translation of 2 × 4 = 8 cm."
        },
        "misconception_tags": ["thinking_double_reflection_is_rotation"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies translation as equivalent transformation", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates distance = 8 cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 37. Rotation definition and key elements
def arch_37_rotation_definition_and_elements(rng: random.Random) -> Dict[str, Any]:
    ans = "Centre of rotation, angle of rotation, and direction (clockwise or anticlockwise)"
    prompt = (
        "In transformation geometry, define what a **rotation** is, and state the **three key pieces of information** "
        "required to fully specify a rotation."
    )
    sol = (
        "**Definition:**\n"
        "A rotation is a transformation that turns a figure around a fixed point.\n\n"
        "**Three Key Specifications:**\n"
        "1. **Centre of rotation:** The fixed point around which the shape turns.\n"
        "2. **Angle of rotation:** The amount of turn measured in degrees (e.g. $90^\\circ, 180^\\circ, 270^\\circ$).\n"
        "3. **Direction of turn:** Either **clockwise** or **anticlockwise**."
    )
    return {
        "id": f"g7_tg_37_{rng.randint(100000, 999999)}",
        "subskill": "37_rotation_definition_and_elements",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Centre of rotation, angle of rotation, direction (clockwise or anticlockwise)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_37",
        "hints": {
            "tier_1": "Think about spinning the hands of a clock or turning a wheel.",
            "tier_2": "Where is the pivot? How far do you turn? Which way?",
            "tier_3": "Centre of rotation, angle, and direction (clockwise / anticlockwise)."
        },
        "misconception_tags": ["omitting_direction_in_rotation"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies centre of rotation", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identifies angle of rotation", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Identifies direction of rotation", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 38. Rotation 90 degrees clockwise about origin
def arch_38_rotation_90_degrees_clockwise(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(2, 6)
    y_val = rng.randint(2, 6)
    ans = f"({y_val}; -{x_val})"
    prompt = (
        f"Point $A({x_val}; {y_val})$ is rotated $90^\\circ$ **clockwise** about the origin $(0; 0)$.\n\n"
        f"1. State the coordinate mapping rule for a $90^\\circ$ clockwise rotation about the origin: $(x; y) \\to (\\dots; \\dots)$.\n"
        f"2. Determine the transformed point coordinates $A'$."
    )
    sol = (
        f"**1. Algebraic Rule for $90^\\circ$ clockwise rotation:**\n"
        f"$$(x; y) \\to (y; -x)$$\n\n"
        f"**2. Apply to $A({x_val}; {y_val})$:**\n"
        f"$$A'({y_val}; -{x_val})$$"
    )
    return {
        "id": f"g7_tg_38_{rng.randint(100000, 999999)}",
        "subskill": "38_rotation_90_degrees_clockwise",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"1. (x; y) -> (y; -x); 2. ({y_val}; -{x_val})",
        "sample_answer": f"(x; y) -> (y; -x) and A'({y_val}; -{x_val})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_38",
        "hints": {
            "tier_1": "Clockwise rotation by 90° moves point from Quadrant 1 to Quadrant 4.",
            "tier_2": "Swap the coordinates and negate the new second coordinate: (y; -x).",
            "tier_3": f"A'({y_val}; -{x_val})."
        },
        "misconception_tags": ["clockwise_anticlockwise_rule_confusion"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States rule (x; y) -> (y; -x)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates coordinates ({y_val}; -{x_val})", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 39. Rotation 90 degrees anticlockwise about origin
def arch_39_rotation_90_degrees_anticlockwise(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(2, 6)
    y_val = rng.randint(2, 6)
    ans = f"(-{y_val}; {x_val})"
    prompt = (
        f"Point $B({x_val}; {y_val})$ is rotated $90^\\circ$ **anticlockwise** about the origin $(0; 0)$.\n\n"
        f"1. State the coordinate mapping rule for a $90^\\circ$ anticlockwise rotation about the origin.\n"
        f"2. Determine the transformed point coordinates $B'$."
    )
    sol = (
        f"**1. Algebraic Rule for $90^\\circ$ anticlockwise rotation:**\n"
        f"$$(x; y) \\to (-y; x)$$\n\n"
        f"**2. Apply to $B({x_val}; {y_val})$:**\n"
        f"$$B'(-{y_val}; {x_val})$$"
    )
    return {
        "id": f"g7_tg_39_{rng.randint(100000, 999999)}",
        "subskill": "39_rotation_90_degrees_anticlockwise",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"1. (x; y) -> (-y; x); 2. (-{y_val}; {x_val})",
        "sample_answer": f"(x; y) -> (-y; x) and B'(-{y_val}; {x_val})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_39",
        "hints": {
            "tier_1": "Anticlockwise by 90° moves point from Quadrant 1 to Quadrant 2.",
            "tier_2": "Swap the coordinates and negate the new first coordinate: (-y; x).",
            "tier_3": f"B'(-{y_val}; {x_val})."
        },
        "misconception_tags": ["clockwise_anticlockwise_rule_confusion"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States rule (x; y) -> (-y; x)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates coordinates (-{y_val}; {x_val})", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 40. Rotation 180 degrees about origin
def arch_40_rotation_180_degrees_about_origin(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(2, 7)
    y_val = rng.randint(2, 7)
    ans = f"(-{x_val}; -{y_val})"
    prompt = (
        f"Point $C({x_val}; {y_val})$ is rotated $180^\\circ$ about the origin $(0; 0)$.\n\n"
        f"1. State the coordinate mapping rule for a $180^\\circ$ rotation: $(x; y) \\to (\\dots; \\dots)$.\n"
        f"2. Does the direction (clockwise vs anticlockwise) make any difference for a $180^\\circ$ turn? Explain.\n"
        f"3. Find the transformed point coordinates $C'$."
    )
    sol = (
        f"**1. Algebraic Rule for $180^\\circ$ rotation:**\n"
        f"$$(x; y) \\to (-x; -y)$$\n\n"
        f"**2. Direction Independence:**\n"
        f"No, direction does not matter. Turning $180^\\circ$ clockwise lands on the exact same position as turning $180^\\circ$ anticlockwise (a half turn).\n\n"
        f"**3. Image Coordinates:**\n"
        f"$$C'(-{x_val}; -{y_val})$$"
    )
    return {
        "id": f"g7_tg_40_{rng.randint(100000, 999999)}",
        "subskill": "40_rotation_180_degrees_about_origin",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"1. (x; y) -> (-x; -y); 2. No difference (half turn); 3. (-{x_val}; -{y_val})",
        "sample_answer": f"(x; y) -> (-x; -y); direction does not matter; C'(-{x_val}; -{y_val})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_40",
        "hints": {
            "tier_1": "A 180° rotation is a straight line through the origin into the opposite quadrant.",
            "tier_2": "Both coordinates simply change signs: (-x; -y).",
            "tier_3": f"C'(-{x_val}; -{y_val})."
        },
        "misconception_tags": ["swapping_coordinates_in_180_rotation"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "States rule (x; y) -> (-x; -y)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains direction does not matter for half turn", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculates coordinates (-{x_val}; -{y_val})", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 41. Rotation about a vertex of the shape
def arch_41_rotation_about_vertex(rng: random.Random) -> Dict[str, Any]:
    ans = "The pivot vertex does not move (its coordinates remain identical)"
    prompt = (
        "Triangle $PQR$ is rotated $90^\\circ$ clockwise about its own vertex $P$.\n\n"
        "1. What happens to the coordinates of vertex $P$ under this rotation?\n"
        "2. How do vertices $Q$ and $R$ move relative to vertex $P$?"
    )
    sol = (
        "**1. Pivot Vertex $P$:**\n"
        "Vertex $P$ is the centre of rotation, so it **does not move**. Its coordinates remain unchanged: $P' = P$.\n\n"
        "**2. Other Vertices $Q$ and $R$:**\n"
        "Vertices $Q$ and $R$ travel along circular arcs centered at $P$, each turning $90^\\circ$ clockwise. "
        "The distances $PQ$ and $PR$ are preserved: $P'Q' = PQ$ and $P'R' = PR$."
    )
    return {
        "id": f"g7_tg_41_{rng.randint(100000, 999999)}",
        "subskill": "41_rotation_about_vertex",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Vertex P stays fixed; Q and R rotate along arcs maintaining equal distances from P",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_41",
        "hints": {
            "tier_1": "If you hold one corner of a triangle down with a pin and spin it, does that pinned corner move?",
            "tier_2": "The pinned corner stays in place. The other corners turn around it.",
            "tier_3": "The pivot vertex remains fixed (invariant)."
        },
        "misconception_tags": ["assuming_all_vertices_change_coordinates"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States pivot vertex P remains fixed / unchanged", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains Q and R rotate along arcs maintaining distances from P", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 42. Direction of rotation conventions
def arch_42_direction_of_rotation_conventions(rng: random.Random) -> Dict[str, Any]:
    ans = "270 degrees clockwise"
    prompt = (
        "In transformation geometry:\n\n"
        "1. What rotation in the clockwise direction is equivalent to a rotation of $90^\\circ$ anticlockwise about the same centre?\n"
        "2. Explain why this equivalence holds."
    )
    sol = (
        "**1. Equivalent Clockwise Rotation:**\n"
        "A rotation of **$270^\\circ$ clockwise** is equivalent to $90^\\circ$ anticlockwise.\n\n"
        "**2. Explanation:**\n"
        "A complete full turn is $360^\\circ$.\n"
        "$$360^\\circ - 90^\\circ = 270^\\circ$$\n"
        "Turning $90^\\circ$ anticlockwise leaves $270^\\circ$ to complete the circle in the clockwise direction to reach the exact same orientation."
    )
    return {
        "id": f"g7_tg_42_{rng.randint(100000, 999999)}",
        "subskill": "42_direction_of_rotation_conventions",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "270 degrees clockwise (since 360 - 90 = 270)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_42",
        "hints": {
            "tier_1": "How many degrees are in a full turn?",
            "tier_2": "Subtract 90° from 360°.",
            "tier_3": "270 degrees clockwise."
        },
        "misconception_tags": ["full_turn_degree_complement_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States 270 degrees clockwise", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Justifies using 360 - 90 = 270", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 43. Preserved properties under rotation
def arch_43_preserved_properties_under_rotation(rng: random.Random) -> Dict[str, Any]:
    ans = "Side lengths, interior angles, area, perimeter, and orientation (congruent)"
    prompt = (
        "When a 2D shape is rotated through an angle of $90^\\circ$ about the origin:\n\n"
        "1. List three properties of the shape that remain unchanged.\n"
        "2. Does the orientation (clockwise order of vertices) reverse, as in a reflection? Explain."
    )
    sol = (
        "**1. Unchanged Properties:**\n"
        "- Side lengths\n"
        "- Interior angle sizes\n"
        "- Area and perimeter\n\n"
        "**2. Orientation:**\n"
        "No, the orientation does **not** reverse. The order of vertices (e.g. clockwise) remains clockwise. "
        "Unlike reflection, rotation does not flip the shape over, so it preserves orientation."
    )
    return {
        "id": f"g7_tg_43_{rng.randint(100000, 999999)}",
        "subskill": "43_preserved_properties_under_rotation",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Side lengths, angles, area; orientation does not reverse (it stays clockwise)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_43",
        "hints": {
            "tier_1": "Does rotating a cutout shape on a table change its size or flip it upside down?",
            "tier_2": "The cutout stays face up and its dimensions remain identical.",
            "tier_3": "Side lengths, angles, and area are preserved; orientation does not flip."
        },
        "misconception_tags": ["confusing_rotation_with_reflection_flip"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Lists side lengths, angles, area preserved", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains orientation is not reversed / stays clockwise", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 44. Rotational symmetry order and angle of rotation for regular polygons
def arch_44_rotational_symmetry_order_and_angle(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([3, 4, 5, 6, 8])
    name = {3: "equilateral triangle", 4: "square", 5: "regular pentagon", 6: "regular hexagon", 8: "regular octagon"}[n]
    angle = 360 // n
    ans = f"Order: {n}; Angle of rotation: {angle} degrees"
    prompt = (
        f"For a **{name}** ($n = {n}$ sides):\n\n"
        f"1. What is the **order of rotational symmetry**?\n"
        f"2. What is the smallest positive **angle of rotation** that maps the shape onto itself?"
    )
    sol = (
        f"**1. Order of Rotational Symmetry:**\n"
        f"For any regular $n$-sided polygon, the order of rotational symmetry equals $n$.\n"
        f"$$\\therefore \\text{{Order}} = {n}$$\n\n"
        f"**2. Angle of Rotation:**\n"
        f"$$\\text{{Angle}} = \\frac{{360^\\circ}}{{n}} = \\frac{{360^\\circ}}{{{n}}} = {angle}^\\circ$$"
    )
    return {
        "id": f"g7_tg_44_{rng.randint(100000, 999999)}",
        "subskill": "44_rotational_symmetry_order_and_angle",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Order {n}; angle {angle} degrees",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_44",
        "hints": {
            "tier_1": f"A regular polygon with {n} sides maps onto itself {n} times in a full circle.",
            "tier_2": f"Divide 360° by {n}.",
            "tier_3": f"Order is {n}; angle is {angle}°."
        },
        "misconception_tags": ["dividing_180_instead_of_360_for_rotational_symmetry"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Identifies order of rotational symmetry = {n}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates smallest angle = {angle} degrees", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 45. Scale factor k definition
def arch_45_scale_factor_definition_and_formula(rng: random.Random) -> Dict[str, Any]:
    ans = "k = Image side length / Original corresponding side length"
    prompt = (
        "Define the **scale factor** $k$ in transformation geometry, write down its calculation formula, "
        "and state what $k > 1$ versus $0 < k < 1$ represents."
    )
    sol = (
        "**Definition & Formula:**\n"
        "The scale factor $k$ is the constant ratio of any side length in the transformed point to the corresponding side length in the original shape:\n"
        "$$k = \\frac{\\text{Length of image side}}{\\text{Length of original corresponding side}}$$\n\n"
        "**Classification:**\n"
        "- If $k > 1$: The transformation is an **enlargement** (the transformed point is larger than the original).\n"
        "- If $0 < k < 1$: The transformation is a **reduction** (the transformed point is smaller than the original).\n"
        "- If $k = 1$: The size is unchanged (congruent figures)."
    )
    return {
        "id": f"g7_tg_45_{rng.randint(100000, 999999)}",
        "subskill": "45_scale_factor_definition_and_formula",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "k = Image length / Original length; k > 1 is enlargement, 0 < k < 1 is reduction",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_45",
        "hints": {
            "tier_1": "Is scale factor new divided by old or old divided by new?",
            "tier_2": "Scale factor = Image length / Original length.",
            "tier_3": "k > 1 enlargement, k < 1 reduction."
        },
        "misconception_tags": ["inverted_scale_factor_ratio"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "States formula k = Image length / Original length", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States k > 1 is enlargement", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "States 0 < k < 1 is reduction", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 46. Enlargement when k > 1
def arch_46_enlargement_side_lengths(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4])
    s1, s2, s3 = 3, 4, 5
    svg = _svg_scale_factor_diagram(k)
    new_s1, new_s2, new_s3 = s1 * k, s2 * k, s3 * k
    ans = f"{new_s1} cm, {new_s2} cm, {new_s3} cm"
    prompt = (
        f"A triangle with side lengths $3\\text{{ cm}}$, $4\\text{{ cm}}$, and $5\\text{{ cm}}$ "
        f"is enlarged by a scale factor of $k = {k}$.\n\n"
        f"1. What are the side lengths of the enlarged triangle?\n"
        f"2. Do the interior angle sizes change under this enlargement? Explain."
    )
    sol = (
        f"**Step 1: Calculate new side lengths:**\n"
        f"Multiply each side length by the scale factor $k = {k}$:\n"
        f"- Side 1: $3 \\times {k} = {new_s1}\\text{{ cm}}$\n"
        f"- Side 2: $4 \\times {k} = {new_s2}\\text{{ cm}}$\n"
        f"- Side 3: $5 \\times {k} = {new_s3}\\text{{ cm}}$\n\n"
        f"**Step 2: Interior angles:**\n"
        f"No, the interior angle sizes **do not change**. In similar figures, corresponding angles remain strictly equal."
    )
    return {
        "id": f"g7_tg_46_{rng.randint(100000, 999999)}",
        "subskill": "46_enlargement_side_lengths",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"1. {new_s1} cm, {new_s2} cm, {new_s3} cm; 2. No, angles remain unchanged",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_46",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": f"Multiply every side length by {k}.",
            "tier_2": "Do angles get bigger when you magnify a picture? No.",
            "tier_3": f"Sides are {new_s1} cm, {new_s2} cm, {new_s3} cm; angles are unchanged."
        },
        "misconception_tags": ["multiplying_angles_by_scale_factor"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates new side lengths: {new_s1}, {new_s2}, {new_s3} cm", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "States angles remain strictly unchanged", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 47. Reduction when 0 < k < 1
def arch_47_reduction_side_lengths(rng: random.Random) -> Dict[str, Any]:
    orig_l = rng.choice([12, 16, 20, 24])
    orig_w = rng.choice([8, 12, 16])
    ans_l = orig_l // 2
    ans_w = orig_w // 2
    ans = f"Length: {ans_l} cm, Width: {ans_w} cm"
    prompt = (
        f"A rectangle measuring ${orig_l}\\text{{ cm}}$ by ${orig_w}\\text{{ cm}}$ is reduced "
        f"using a scale factor of $k = \\frac{{1}}{{2}}$ (or $0{{,}}5$).\n\n"
        f"1. Calculate the dimensions of the reduced rectangle.\n"
        f"2. Calculate the perimeter of both the original rectangle and the reduced rectangle."
    )
    p_orig = 2 * (orig_l + orig_w)
    p_red = 2 * (ans_l + ans_w)
    sol = (
        f"**Step 1: Calculate reduced dimensions:**\n"
        f"- Length: ${orig_l} \\times \\frac{{1}}{{2}} = {ans_l}\\text{{ cm}}$\n"
        f"- Width: ${orig_w} \\times \\frac{{1}}{{2}} = {ans_w}\\text{{ cm}}$\n\n"
        f"**Step 2: Calculate perimeters:**\n"
        f"- Original Perimeter: $2({orig_l} + {orig_w}) = 2({orig_l + orig_w}) = {p_orig}\\text{{ cm}}$\n"
        f"- Reduced Perimeter: $2({ans_l} + {ans_w}) = 2({ans_l + ans_w}) = {p_red}\\text{{ cm}}$\n\n"
        f"Notice that the perimeter is also multiplied by $k = \\frac{{1}}{{2}}$: ${p_orig} \\times \\frac{{1}}{{2}} = {p_red}\\text{{ cm}}$."
    )
    return {
        "id": f"g7_tg_47_{rng.randint(100000, 999999)}",
        "subskill": "47_reduction_side_lengths",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Dimensions: {ans_l} cm by {ans_w} cm; Perimeters: {p_orig} cm and {p_red} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_47",
        "hints": {
            "tier_1": "Multiply each dimension by 1/2 (divide by 2).",
            "tier_2": f"New length = {orig_l} / 2 = {ans_l}; new width = {orig_w} / 2 = {ans_w}.",
            "tier_3": f"{ans_l} cm by {ans_w} cm."
        },
        "misconception_tags": ["subtracting_instead_of_multiplying_by_scale_factor"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates dimensions {ans_l} cm by {ans_w} cm", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Calculates perimeters {p_orig} cm and {p_red} cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 48. Effect of scale factor k on area
def arch_48_effect_of_scale_factor_on_area(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4])
    l, w = 4, 3
    orig_area = l * w
    new_area = orig_area * (k ** 2)
    ans = f"{new_area} cm^2; multiplied by k^2 = {k**2}"
    prompt = (
        f"A rectangular photo has dimensions $4\\text{{ cm}}$ by $3\\text{{ cm}}$ with an area of ${orig_area}\\text{{ cm}}^2$.\n"
        f"The photo is enlarged using a scale factor of $k = {k}$.\n\n"
        f"1. Calculate the area of the enlarged photo.\n"
        f"2. By what factor did the area increase? Express this in terms of $k$."
    )
    sol = (
        f"**Step 1: Calculate enlarged dimensions:**\n"
        f"- Length: $4 \\times {k} = {4 * k}\\text{{ cm}}$\n"
        f"- Width: $3 \\times {k} = {3 * k}\\text{{ cm}}$\n"
        f"$$\\text{{Area}}_{{\\text{{enlarged}}}} = {4 * k} \\times {3 * k} = {new_area}\\text{{ cm}}^2$$\n\n"
        f"**Step 2: Area multiplier factor:**\n"
        f"$$\\frac{{\\text{{Area}}_{{\\text{{enlarged}}}}}}{{\\text{{Area}}_{{\\text{{original}}}}}} = \\frac{{{new_area}}}{{{orig_area}}} = {k**2}$$\n\n"
        f"When linear dimensions are scaled by factor $k$, the **area is multiplied by $k^2$**:\n"
        f"$$k^2 = {k}^2 = {k**2}$$\n"
        f"$$\\therefore \\text{{Area}} = {new_area}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_tg_48_{rng.randint(100000, 999999)}",
        "subskill": "48_effect_of_scale_factor_on_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Area = {new_area} cm^2; increased by k^2 = {k**2}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_48",
        "hints": {
            "tier_1": "Both the length and width are multiplied by k.",
            "tier_2": f"Area is multiplied by k × k = k². Here {k}² = {k**2}.",
            "tier_3": f"New area = {orig_area} × {k**2} = {new_area} cm²."
        },
        "misconception_tags": ["assuming_area_scales_by_k_instead_of_k_squared"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates new area = {new_area} cm^2", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Explains area increases by factor k^2 = {k**2}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 49. Similar figures vs congruent figures distinction
def arch_49_similar_vs_congruent_distinction(rng: random.Random) -> Dict[str, Any]:
    ans = "Congruent: identical size and shape (k = 1); Similar: identical shape, different size (proportional sides, equal angles)"
    prompt = (
        "In transformation geometry, clearly distinguish between **congruent figures** and **similar figures**.\n\n"
        "1. What conditions define congruent figures?\n"
        "2. What conditions define similar figures?\n"
        "3. Which transformations produce congruent images, and which produce similar (non-congruent) images?"
    )
    sol = (
        "**1. Congruent Figures:**\n"
        "Two figures are congruent if they have the exact same shape and the exact same size ($k = 1$). "
        "Corresponding sides are equal, and corresponding angles are equal.\n\n"
        "**2. Similar Figures:**\n"
        "Two figures are similar if they have the same shape, but can have different sizes. "
        "Corresponding angles are equal, and corresponding side lengths are proportional (in the constant ratio $k$).\n\n"
        "**3. Transformation Classification:**\n"
        "- **Congruent:** Translation, Reflection, and Rotation (isometries).\n"
        "- **Similar (non-congruent):** Enlargements and Reductions where $k \\neq 1$."
    )
    return {
        "id": f"g7_tg_49_{rng.randint(100000, 999999)}",
        "subskill": "49_similar_vs_congruent_distinction",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Congruent: same size and shape (rigid transformations); Similar: same shape, proportional sides (enlargements/reductions)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_49",
        "hints": {
            "tier_1": "Think about a photocopy at 100% vs 200%.",
            "tier_2": "100% is congruent (same size and shape). 200% is similar (same shape, enlarged size).",
            "tier_3": "Congruent has k=1; similar has proportional sides and equal angles."
        },
        "misconception_tags": ["confusing_similarity_with_congruence"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Defines congruent as equal sides and angles / same size and shape", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Defines similar as equal angles and proportional sides", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Classifies translations/reflections/rotations vs enlargements/reductions", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 50. Comprehensive diagnostic autopsy / common misconception traps
def arch_50_transformation_geometry_comprehensive_autopsy(rng: random.Random) -> Dict[str, Any]:
    ans = "Diagonal of rectangle does not fold to matching vertices; scale factor multiplies area by k^2 not k; translation preserves shape"
    prompt = (
        "A learner completed a transformation geometry test and made three common errors:\n\n"
        "1. **Statement 1:** 'A non-square rectangle has 4 lines of symmetry because both diagonals are lines of symmetry.'\n"
        "2. **Statement 2:** 'If a triangle is enlarged by scale factor $k = 3$, its area becomes 3 times larger.'\n"
        "3. **Statement 3:** 'When you reflect point $(4; 5)$ across the $x$-axis, the new coordinates are $(-4; 5)$.'\n\n"
        "For each statement, diagnose the misconception and state the correct mathematical fact."
    )
    sol = (
        "**Diagnostic Autopsy:**\n\n"
        "**1. Statement 1 Correction:**\n"
        "- **Misconception:** Assuming that because a diagonal divides a rectangle into two congruent triangles, it must be a line of symmetry.\n"
        "- **Fact:** Folding along the diagonal does not cause the vertices to coincide. A non-square rectangle has only **2** lines of symmetry (horizontal and vertical).\n\n"
        "**2. Statement 2 Correction:**\n"
        "- **Misconception:** Confusing linear scale factor with area scale factor.\n"
        "- **Fact:** Area is two-dimensional ($k^2$). The area becomes $3^2 = 9$ times larger.\n\n"
        "**3. Statement 3 Correction:**\n"
        "- **Misconception:** Negating the $x$-coordinate instead of the $y$-coordinate during an $x$-axis reflection.\n"
        "- **Fact:** Reflection across the $x$-axis preserves $x$ and inverts $y$: $(4; 5) \\to (4; -5)$."
    )
    return {
        "id": f"g7_tg_50_{rng.randint(100000, 999999)}",
        "subskill": "50_transformation_geometry_comprehensive_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1. Diagonals not lines of symmetry (only 2 lines); 2. Area multiplies by 3^2 = 9; 3. Correct point is (4; -5)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_50",
        "hints": {
            "tier_1": "Test each statement against the fundamental laws of symmetry, area scaling, and reflections.",
            "tier_2": "Statement 1: 2 lines; Statement 2: k²=9; Statement 3: (4; -5).",
            "tier_3": "Correct facts: 2 lines of symmetry; area grows by factor 9; coordinates are (4; -5)."
        },
        "misconception_tags": ["rectangle_diagonal_symmetry_trap", "assuming_area_scales_by_k_instead_of_k_squared", "negating_wrong_coordinate_in_x_axis_reflection"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Corrects rectangle diagonal error (only 2 lines of symmetry)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Corrects area scale factor (k^2 = 9 times)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Corrects x-axis reflection coordinates to (4; -5)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }
