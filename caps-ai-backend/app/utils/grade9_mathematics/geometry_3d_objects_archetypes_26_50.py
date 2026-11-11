"""Grade 9 Mathematics — Geometry of 3D Objects Archetypes 26 to 50 (CAPS Term 4).
3D Nets, Cross-Sections, Right vs Oblique Solids, Truncated/Composite Solids, and Spatial Synthesis.
100% AST Pure: Python math and random only, zero LLM authority.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.grade9_mathematics.geometry_3d_objects_svg import (
    draw_polyhedron_3d_svg,
    draw_3d_net_svg,
    draw_cross_section_svg,
)


# -----------------------------------------------------------------------------
# Archetype 26: Cube Net Validity (Hexomino Configurations)
# -----------------------------------------------------------------------------
def arch_26_cube_net_validity_hexomino(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("cube_cross_net", "T-cross net (1-4-1 arrangement)", "Valid", "It has 6 square faces that fold along the edges without overlapping to enclose a complete cube."),
        ("cube_t_net", "Latin cross net", "Valid", "The 6 squares fold up neatly around the base square, forming all 6 faces of a cube with zero overlaps."),
        ("cube_cross_net", "Arrangement with 5 squares in a straight row and 1 attached", "Invalid", "A straight row of 5 squares cannot fold into a cube because opposite faces overlap, leaving one side open."),
        ("cube_cross_net", "Arrangement with 4 squares meeting at a single corner (2×2 block)", "Invalid", "A 2×2 square cluster will always overlap faces when folded; it cannot form a valid cube net."),
    ]
    net_key, desc, validity, reason = rng.choice(choices)
    svg = draw_3d_net_svg(net_key, seed=seed, title=desc)

    prompt = (
        f"Consider the 2D arrangement of 6 squares (hexomino net) shown in the diagram: **{desc}**.\n"
        f"State whether this net is a 'Valid' or 'Invalid' net of a cube."
    )
    sol = (
        f"For a net of 6 squares to form a cube:\n"
        f"• Exactly 6 congruent square faces.\n"
        f"• There are exactly 11 distinct valid hexomino nets of a cube.\n"
        f"For this {desc}:\n"
        f"{reason}\n"
        f"Therefore, the net is **{validity}**."
    )

    return {
        "subskill": "26_cube_net_validity_hexomino",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": validity,
        "expected_answer": validity,
        "sample_answer": f"{validity} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct validity determination: {validity}", "marks": 1},
            {"desc": "Provide geometric reasoning regarding face folding and overlaps", "marks": 1},
        ],
        "hints": [
            "Imagine folding the squares up into a 3D box.",
            "If any faces overlap or leave a hole, the net is invalid.",
            f"The answer is {validity}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 27: Opposite Faces on a Cube Net
# -----------------------------------------------------------------------------
def arch_27_cube_net_opposite_faces(rng: random.Random, seed: int) -> Dict[str, Any]:
    # In standard cross net:
    #       [T] (top)
    #    [L][B][R][Bk] (left, base, right, back)
    #       [F] (front)
    # Opposite pairs:
    # (Top, Front)
    # (Left, Right)
    # (Base, Back)
    pairs = [
        ("Base", "Back"),
        ("Back", "Base"),
        ("Left", "Right"),
        ("Right", "Left"),
        ("Top", "Front"),
        ("Front", "Top"),
    ]
    face_q, face_opp = rng.choice(pairs)

    labels = ["Top", "Left", "Base", "Right", "Back", "Front"]
    svg = draw_3d_net_svg("cube_cross_net", labels=labels, seed=seed, title="Cube Net: Identify Opposite Faces")

    prompt = (
        f"An unfolded net of a cube is depicted with faces labeled: Top, Left, Base, Right, Back, and Front.\n"
        f"When the net is folded to form a 3D cube, which face will be opposite the **{face_q}** face?"
    )
    sol = (
        f"When folding the standard cross net of a cube:\n"
        f"• The horizontal strip of 4 faces wraps around: 'Left' is opposite 'Right', and 'Base' is opposite 'Back'.\n"
        f"• The two vertical flaps fold up to become opposite each other: 'Top' is opposite 'Front'.\n"
        f"Therefore, the face opposite **{face_q}** is **{face_opp}**."
    )

    return {
        "subskill": "27_cube_net_opposite_faces",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": face_opp,
        "expected_answer": face_opp,
        "sample_answer": face_opp,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct opposite face: {face_opp}", "marks": 2},
        ],
        "hints": [
            "Faces that are separated by exactly one square along a straight row fold to become opposite.",
            "Left and Right are separated by Base; Top and Front fold over opposite ends.",
            f"The face opposite {face_q} is {face_opp}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 28: Standard Die Numbers on a Cube Net (Opposite Faces Sum to 7)
# -----------------------------------------------------------------------------
def arch_28_cube_net_standard_die_dots(rng: random.Random, seed: int) -> Dict[str, Any]:
    die_pairs = [(1, 6), (2, 5), (3, 4)]
    given_num, opp_num = rng.choice([(1, 6), (6, 1), (2, 5), (5, 2), (3, 4), (4, 3)])

    labels = ["1", "2", "3", "5", "4", "?"]
    svg = draw_3d_net_svg("cube_cross_net", labels=labels, seed=seed, title="Standard Die Net: Opposite Faces Sum to 7")

    prompt = (
        f"On a standard six-sided die, the dots on any two opposite faces always add up to $7$.\n"
        f"If a cube net has the number ${given_num}$ on a face, determine the number on the face directly opposite to it."
    )
    sol = (
        f"On any standard die, opposite faces sum to $7$:\n"
        f"$\\text{{Opposite Face}} = 7 - \\text{{Given Face}} = 7 - {given_num} = {opp_num}$.\n"
        f"Therefore, the number on the opposite face is ${opp_num}$."
    )

    return {
        "subskill": "28_cube_net_standard_die_dots",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(opp_num),
        "expected_answer": str(opp_num),
        "sample_answer": str(opp_num),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Apply opposite faces sum to 7 rule: 7 - {given_num}", "marks": 1},
            {"desc": f"Calculate opposite face value: {opp_num}", "marks": 1},
        ],
        "hints": [
            "The sum of numbers on opposite faces of a standard die is always 7.",
            f"Subtract {given_num} from 7.",
            f"The answer is {opp_num}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 29: Net of a Rectangular Prism (Cuboid)
# -----------------------------------------------------------------------------
def arch_29_rectangular_prism_net(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("How many total rectangular faces are in the net of a rectangular prism?", "6", "A rectangular prism has 6 rectangular faces."),
        ("How many pairs of congruent opposite rectangular faces make up the net of a cuboid?", "3", "A cuboid has 3 pairs of matching congruent rectangular faces (top/bottom, front/back, left/right)."),
    ]
    q_text, ans, reason = rng.choice(choices)
    svg = draw_3d_net_svg("rectangular_prism_net", seed=seed, title="Net of a Rectangular Prism")

    prompt = f"Refer to the 2D unfolded net of a rectangular prism shown in the diagram. {q_text}"
    sol = f"{ans}.\nExplanation: {reason}"

    return {
        "subskill": "29_rectangular_prism_net",
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
            {"desc": f"Correct count: {ans}", "marks": 2},
        ],
        "hints": [
            "A rectangular prism is bounded by 6 rectangles.",
            "Opposite faces are congruent, forming 3 matching pairs.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 30: Net of a Triangular Prism
# -----------------------------------------------------------------------------
def arch_30_triangular_prism_net(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("triangles", "2", "2 congruent triangular bases at the opposite ends"),
        ("rectangles", "3", "3 rectangular lateral faces connecting the corresponding sides"),
    ]
    shape_part, count_ans, reason = rng.choice(choices)
    svg = draw_3d_net_svg("triangular_prism_net", seed=seed, title="Net of a Triangular Prism")

    prompt = (
        f"Examine the 2D unfolded net of a triangular prism shown in the diagram. "
        f"How many **{shape_part}** are in the net of this triangular prism?"
    )
    sol = (
        f"The net of a triangular prism consists of:\n"
        f"• 2 congruent triangular bases.\n"
        f"• 3 rectangular lateral faces.\n"
        f"Therefore, the number of {shape_part} is **{count_ans}** ({reason})."
    )

    return {
        "subskill": "30_triangular_prism_net",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": count_ans,
        "expected_answer": count_ans,
        "sample_answer": count_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct count of {shape_part}: {count_ans}", "marks": 2},
        ],
        "hints": [
            "Count the shapes in the unfolded net of the triangular prism.",
            f"There are {count_ans} {shape_part}.",
            f"Answer: {count_ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 31: Net of a Square-based Pyramid
# -----------------------------------------------------------------------------
def arch_31_square_pyramid_net(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("squares", "1", "1 square base in the center"),
        ("triangles", "4", "4 triangular faces attached to the 4 edges of the square base"),
    ]
    shape_part, count_ans, reason = rng.choice(choices)
    svg = draw_3d_net_svg("square_pyramid_net", seed=seed, title="Net of a Square-Based Pyramid")

    prompt = (
        f"Refer to the 2D unfolded net of a square-based pyramid shown in the diagram. "
        f"How many **{shape_part}** are in this net?"
    )
    sol = (
        f"The net of a square-based pyramid comprises:\n"
        f"• 1 central square base.\n"
        f"• 4 surrounding triangular faces that fold up to meet at the apex.\n"
        f"Therefore, the number of {shape_part} is **{count_ans}**."
    )

    return {
        "subskill": "31_square_pyramid_net",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": count_ans,
        "expected_answer": count_ans,
        "sample_answer": count_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct count: {count_ans}", "marks": 2},
        ],
        "hints": [
            "Look at the center and the flaps of the pyramid net.",
            "There is 1 square base and 4 triangular sides.",
            f"The answer is {count_ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 32: Net of a Regular Tetrahedron
# -----------------------------------------------------------------------------
def arch_32_tetrahedron_net(rng: random.Random, seed: int) -> Dict[str, Any]:
    svg = draw_polyhedron_3d_svg("tetrahedron", seed=seed, title="Tetrahedron and Its Net")

    prompt = (
        f"A regular tetrahedron (triangular-based pyramid) is unfolded to form a 2D net.\n"
        f"What 2D polygon forms all the faces of this net, and how many are there in total?"
    )
    ans = "4 equilateral triangles"
    sol = (
        f"A regular tetrahedron consists of 4 congruent equilateral triangular faces.\n"
        f"When unfolded, its net contains exactly 4 equilateral triangles.\n"
        f"Therefore, the net consists of **{ans}**."
    )

    return {
        "subskill": "32_tetrahedron_net",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify equilateral triangles as face shape", "marks": 1},
            {"desc": "State total face count of 4", "marks": 1},
        ],
        "hints": [
            "A tetrahedron has 4 faces.",
            "Each face is an equilateral triangle.",
            f"The net consists of {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 33: Components of a Cylinder's Net
# -----------------------------------------------------------------------------
def arch_33_cylinder_net_components(rng: random.Random, seed: int) -> Dict[str, Any]:
    svg = draw_3d_net_svg("cylinder_net", seed=seed, title="Net of a Closed Cylinder")

    prompt = (
        f"Examine the 2D unfolded net of a closed cylinder shown in the diagram. "
        f"Name the geometric shapes that make up this net, specifying the quantity of each."
    )
    ans = "2 circles and 1 rectangle"
    sol = (
        f"The unfolded net of a closed cylinder consists of:\n"
        f"• 2 congruent circles representing the top and bottom circular bases (lids).\n"
        f"• 1 rectangle representing the unrolled curved lateral surface.\n"
        f"Therefore, the net is made of **{ans}**."
    )

    return {
        "subskill": "33_cylinder_net_components",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify 2 circular bases", "marks": 1},
            {"desc": "Identify 1 rectangular curved surface", "marks": 1},
        ],
        "hints": [
            "When you unroll the curved surface of a cylinder, it flattens into a rectangle.",
            "The top and bottom are circles.",
            f"The net consists of {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 34: Rectangle Dimensions in a Cylinder's Net
# -----------------------------------------------------------------------------
def arch_34_cylinder_net_rectangle_dimensions(rng: random.Random, seed: int) -> Dict[str, Any]:
    r = rng.choice([7, 14, 21])
    h = rng.randint(10, 30)
    # Circumference C = 2 * pi * r with pi = 22/7
    c_val = 2 * 22 * (r // 7)

    svg = draw_3d_net_svg("cylinder_net", seed=seed, title="Cylinder Net Dimensions")

    prompt = (
        f"A closed cylinder has a circular base with radius $r = {r}\\text{{ cm}}$ and a height of $h = {h}\\text{{ cm}}$. "
        f"When its curved surface is unrolled into a flat rectangle in its net, "
        f"calculate the length of this rectangle using $\\pi = \\frac{{22}}{{7}}$ (in cm)."
    )
    sol = (
        f"The length of the unrolled rectangle wraps completely around the circular base, "
        f"so it equals the circumference of the circle:\n"
        f"$\\text{{Length}} = 2\\pi r = 2 \\times \\frac{{22}}{{7}} \\times {r} = 2 \\times 22 \\times {r // 7} = {c_val}\\text{{ cm}}$.\n"
        f"Therefore, the length of the rectangle is ${c_val}$ cm."
    )

    return {
        "subskill": "34_cylinder_net_rectangle_dimensions",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(c_val),
        "expected_answer": str(c_val),
        "sample_answer": f"{c_val} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "State that length equals circumference 2*pi*r", "marks": 1},
            {"desc": f"Calculate length: {c_val} cm", "marks": 1},
        ],
        "hints": [
            "The length of the rectangular curved face equals the circumference of the circular base.",
            f"Circumference = 2 * (22/7) * {r}.",
            f"Length = {c_val} cm.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 35: Components of a Cone's Net
# -----------------------------------------------------------------------------
def arch_35_cone_net_components(rng: random.Random, seed: int) -> Dict[str, Any]:
    svg = draw_polyhedron_3d_svg("cone", seed=seed, title="Cone and Its Unfolded Net")

    prompt = (
        f"When a right circular cone is unfolded to form a 2D geometric net, "
        f"what two 2D geometric figures make up this net?"
    )
    ans = "1 circle and 1 sector of a circle"
    sol = (
        f"The net of a cone consists of:\n"
        f"• 1 complete circle (the flat circular base).\n"
        f"• 1 sector of a larger circle (the unrolled lateral curved surface, whose arc length equals the circumference of the base circle).\n"
        f"Therefore, the net consists of **{ans}**."
    )

    return {
        "subskill": "35_cone_net_components",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify circular base", "marks": 1},
            {"desc": "Identify circle sector for lateral surface", "marks": 1},
        ],
        "hints": [
            "The base of the cone is a circle.",
            "The curved side of the cone flattens into a slice (sector) of a circle.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 36: Cross-section of a Cube Parallel to a Face
# -----------------------------------------------------------------------------
def arch_36_cross_section_cube_horizontal_vertical(rng: random.Random, seed: int) -> Dict[str, Any]:
    cut_type = rng.choice(["horizontal", "vertical"])
    svg = draw_cross_section_svg("cube", cut_type, "square", seed=seed)

    prompt = (
        f"A geometric cube is sliced by a flat cutting plane that is {cut_type} and parallel to one of its faces "
        f"(as illustrated in the diagram).\n"
        f"What 2D geometric shape is formed by the cross-section?"
    )
    ans = "Square"
    sol = (
        f"Any planar cut through a cube that is parallel to any of its faces creates a cross-section "
        f"that is congruent to the faces of the cube.\n"
        f"Since all faces of a cube are squares, the cross-section is a **{ans}**."
    )

    return {
        "subskill": "36_cross_section_cube_horizontal_vertical",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct cross-section shape: {ans}", "marks": 2},
        ],
        "hints": [
            "A slice parallel to any face produces the exact shape of that face.",
            "The faces of a cube are squares.",
            f"The cross-section is a {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 37: Diagonal Cross-sections of a Cube
# -----------------------------------------------------------------------------
def arch_37_cross_section_cube_diagonal(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("cutting through opposite vertical edges of the cube", "Rectangle", "The diagonal cut through opposite vertical edges forms a rectangle of dimensions s × s√2."),
        ("slicing off one corner vertex of the cube through three adjacent edges equidistant from the vertex", "Equilateral triangle", "The three cut edges are equal in length, forming an equilateral triangle."),
    ]
    desc, shape_ans, reason = rng.choice(choices)
    svg = draw_cross_section_svg("cube", "diagonal", "rectangle", seed=seed)

    prompt = (
        f"A cube is sliced by a diagonal cutting plane: {desc} (shown in the diagram).\n"
        f"What 2D shape is the resulting cross-section? (Choose from: 'Rectangle', 'Equilateral triangle', or 'Circle')."
    )
    sol = (
        f"Analyzing the diagonal slice:\n"
        f"{reason}.\n"
        f"Therefore, the cross-sectional shape is a **{shape_ans}**."
    )

    return {
        "subskill": "37_cross_section_cube_diagonal",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": shape_ans,
        "expected_answer": shape_ans,
        "sample_answer": f"{shape_ans} ({reason})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct shape: {shape_ans}", "marks": 2},
        ],
        "hints": [
            f"Consider the cut: {desc}.",
            f"{reason}",
            f"The answer is {shape_ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 38: Cross-sections of a Cylinder
# -----------------------------------------------------------------------------
def arch_38_cross_section_cylinder(rng: random.Random, seed: int) -> Dict[str, Any]:
    cut_choice = rng.choice(["horizontal", "vertical"])
    if cut_choice == "horizontal":
        ans = "Circle"
        cut_desc = "horizontal and parallel to its circular bases"
        reason = "A cut parallel to the base of a cylinder produces a circle identical in radius to the base."
    else:
        ans = "Rectangle"
        cut_desc = "vertical and perpendicular to its circular bases (passing through the center)"
        reason = "A vertical cut through the cylinder's height produces a rectangle of dimensions 2r × h."

    svg = draw_cross_section_svg("cylinder", cut_choice, ans.lower(), seed=seed)

    prompt = (
        f"A solid cylinder is sliced by a flat cutting plane that is {cut_desc} "
        f"(as shown in the diagram).\n"
        f"What 2D geometric shape is the cross-section?"
    )
    sol = (
        f"For a cylinder:\n"
        f"{reason}\n"
        f"Therefore, the cross-section is a **{ans}**."
    )

    return {
        "subskill": "38_cross_section_cylinder",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct shape: {ans}", "marks": 2},
        ],
        "hints": [
            "A horizontal cut through a cylinder gives a circle.",
            "A vertical cut perpendicular to the bases gives a rectangle.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 39: Cross-sections of a Cone
# -----------------------------------------------------------------------------
def arch_39_cross_section_cone(rng: random.Random, seed: int) -> Dict[str, Any]:
    cut_choice = rng.choice(["horizontal", "vertical"])
    if cut_choice == "horizontal":
        ans = "Circle"
        cut_desc = "horizontal and parallel to its circular base"
        reason = "A cut parallel to the base of a cone creates a circle of smaller radius."
    else:
        ans = "Isosceles triangle"
        cut_desc = "vertical, passing directly through the apex and center of the base"
        reason = "A vertical slice through the apex creates a triangle with two equal slant edges (an isosceles triangle)."

    svg = draw_cross_section_svg("cone", cut_choice, ans.lower(), seed=seed)

    prompt = (
        f"A solid right cone is cut by a flat plane that is {cut_desc} "
        f"(as shown in the diagram).\n"
        f"Determine the 2D geometric shape formed by the cross-section."
    )
    sol = (
        f"For a cone:\n"
        f"{reason}\n"
        f"Therefore, the cross-section is an **{ans}**."
    )

    return {
        "subskill": "39_cross_section_cone",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct shape: {ans}", "marks": 2},
        ],
        "hints": [
            "Horizontal cut parallel to base -> circle.",
            "Vertical cut through apex -> isosceles triangle.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 40: Cross-sections of a Square-based Pyramid
# -----------------------------------------------------------------------------
def arch_40_cross_section_square_pyramid(rng: random.Random, seed: int) -> Dict[str, Any]:
    cut_choice = rng.choice(["horizontal", "vertical"])
    if cut_choice == "horizontal":
        ans = "Square"
        cut_desc = "horizontal and parallel to the square base"
        reason = "A horizontal cut parallel to the base produces a smaller square similar to the base."
    else:
        ans = "Isosceles triangle"
        cut_desc = "vertical, passing through the apex and bisecting opposite edges of the base"
        reason = "A vertical cut through the apex produces an isosceles triangle."

    svg = draw_polyhedron_3d_svg("square_pyramid", seed=seed, title="Cross-section of a Pyramid")

    prompt = (
        f"A square-based pyramid is sliced by a flat cutting plane that is {cut_desc}.\n"
        f"What 2D shape is the resulting cross-section?"
    )
    sol = (
        f"For a square-based pyramid:\n"
        f"{reason}\n"
        f"Therefore, the cross-section is a **{ans}**."
    )

    return {
        "subskill": "40_cross_section_square_pyramid",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct shape: {ans}", "marks": 2},
        ],
        "hints": [
            "Slicing parallel to the base gives a smaller version of the base (square).",
            "Slicing vertically through the apex gives an isosceles triangle.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 41: Cross-sections of a Sphere
# -----------------------------------------------------------------------------
def arch_41_cross_section_sphere(rng: random.Random, seed: int) -> Dict[str, Any]:
    svg = draw_polyhedron_3d_svg("cylinder", seed=seed, title="Cross-sections of a Sphere")

    prompt = (
        f"If a solid 3D sphere is sliced by any flat planar surface at any angle, "
        f"what 2D shape is always formed by the cross-section?"
    )
    ans = "Circle"
    sol = (
        f"A sphere is completely symmetric in three dimensions.\n"
        f"Any plane that intersects a sphere creates a cross-section that is strictly a **{ans}**.\n"
        f"(When the cutting plane passes through the center of the sphere, it is called a great circle).\n"
        f"Therefore, the cross-section is always a **{ans}**."
    )

    return {
        "subskill": "41_cross_section_sphere",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct shape: {ans}", "marks": 2},
        ],
        "hints": [
            "Think about slicing an orange or ball in any direction.",
            "The cut surface is always circular.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 42: Right vs Oblique Prisms
# -----------------------------------------------------------------------------
def arch_42_right_vs_oblique_prisms(rng: random.Random, seed: int) -> Dict[str, Any]:
    svg = draw_polyhedron_3d_svg("triangular_prism", seed=seed, title="Right vs Oblique Prisms")

    prompt = (
        f"In 3D geometry, prisms are categorized as either 'Right prisms' or 'Oblique prisms'.\n"
        f"What angle do the lateral edges make with the bases in a **Right prism** (in degrees)?"
    )
    ans = "90"
    sol = (
        f"In a **Right prism**, all lateral edges and lateral faces are perpendicular ($90^\\circ$) to the planes of the bases.\n"
        f"In an oblique prism, the lateral edges are slanted at an angle other than $90^\\circ$.\n"
        f"Therefore, the angle is ${ans}^\\circ$."
    )

    return {
        "subskill": "42_right_vs_oblique_prisms",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": f"{ans}° (perpendicular)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State angle: {ans}° (or perpendicular)", "marks": 2},
        ],
        "hints": [
            "'Right' in geometry means perpendicular or right-angled.",
            "The lateral edges meet the base at 90°.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 43: Right vs Oblique Pyramids
# -----------------------------------------------------------------------------
def arch_43_right_vs_oblique_pyramids(rng: random.Random, seed: int) -> Dict[str, Any]:
    svg = draw_polyhedron_3d_svg("square_pyramid", seed=seed, title="Right Pyramid Alignment")

    prompt = (
        f"In a **Right pyramid**, where does the perpendicular line dropped from the apex intersect the base?\n"
        f"(Choose from: 'Center of the base', 'Corner vertex of the base', or 'Outside the base')."
    )
    ans = "Center of the base"
    sol = (
        f"In a **Right pyramid**, the apex lies directly above the geometric center (centroid) of the base.\n"
        f"Therefore, the altitude intersects the base at the **{ans}**.\n"
        f"(In an oblique pyramid, the apex is shifted off-center)."
    )

    return {
        "subskill": "43_right_vs_oblique_pyramids",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct alignment description: {ans}", "marks": 2},
        ],
        "hints": [
            "In a right pyramid, the apex is aligned centrally above the base.",
            f"The altitude hits the {ans}.",
            f"Answer: {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 44: Truncated Pyramid (Frustum)
# -----------------------------------------------------------------------------
def arch_44_truncated_pyramid_frustum(rng: random.Random, seed: int) -> Dict[str, Any]:
    svg = draw_polyhedron_3d_svg("square_pyramid", seed=seed, title="Frustum of a Pyramid")

    prompt = (
        f"When a pyramid is cut by a plane parallel to its base and the top portion (containing the apex) is removed, "
        f"the remaining bottom portion is called a **frustum** (truncated pyramid).\n"
        f"What 2D geometric shape are the lateral faces of a frustum of a square-based pyramid?"
    )
    ans = "Trapezium"
    sol = (
        f"A frustum of a pyramid has two parallel square bases of different sizes.\n"
        f"The 4 lateral faces connecting the corresponding parallel sides of the top and bottom squares "
        f"are **trapezia** (trapezoids).\n"
        f"Therefore, each lateral face is a **{ans}**."
    )

    return {
        "subskill": "44_truncated_pyramid_frustum",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct lateral face shape: {ans}", "marks": 2},
        ],
        "hints": [
            "The top and bottom edges of the lateral face are parallel but unequal in length.",
            "A quadrilateral with one pair of parallel sides is a trapezium.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 45: Truncated Cube Faces, Vertices, Edges
# -----------------------------------------------------------------------------
def arch_45_truncated_cube_faces_vertices_edges(rng: random.Random, seed: int) -> Dict[str, Any]:
    target = rng.choice(["faces", "vertices", "edges"])
    if target == "faces":
        ans = "14"
        q_target = "total number of faces (F)"
        details = "6 octagonal faces + 8 triangular faces (created at the 8 truncated corners) = 14 faces"
    elif target == "vertices":
        ans = "24"
        q_target = "total number of vertices (V)"
        details = "Each of the original 8 vertices is replaced by a triangle with 3 vertices: 8 × 3 = 24 vertices"
    else:
        ans = "36"
        q_target = "total number of edges (E)"
        details = "12 original edges (shortened) + 8 × 3 corner edges = 12 + 24 = 36 edges"

    svg = draw_polyhedron_3d_svg("cube", seed=seed, title="Truncated Cube")

    prompt = (
        f"A cube has all $8$ of its corners sliced off uniformly to create a **truncated cube**.\n"
        f"Calculate the {q_target} of the resulting Archimedean solid."
    )
    sol = (
        f"For a truncated cube:\n"
        f"• {details}.\n"
        f"Euler's Formula check: $V - E + F = 24 - 36 + 14 = 2$.\n"
        f"Therefore, the {q_target} is **{ans}**."
    )

    return {
        "subskill": "45_truncated_cube_faces_vertices_edges",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct count: {ans}", "marks": 2},
        ],
        "hints": [
            "Each corner slice replaces 1 vertex with a triangle (3 vertices).",
            f"{details}.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 46: Composite 3D Solid — Grain Silo Components
# -----------------------------------------------------------------------------
def arch_46_composite_solid_silo_components(rng: random.Random, seed: int) -> Dict[str, Any]:
    svg = draw_polyhedron_3d_svg("cylinder", seed=seed, title="Grain Silo Structure")

    prompt = (
        f"A farm grain silo is an example of a composite 3D object constructed by joining standard geometric solids.\n"
        f"Typically, a silo consists of a cylindrical main body topped with which 3D solid roof?\n"
        f"(Choose from: 'Cone (or Hemisphere)', 'Cube', or 'Triangular prism')."
    )
    ans = "Cone (or Hemisphere)"
    sol = (
        f"A standard agricultural grain silo is a composite solid made of:\n"
        f"• A cylindrical tower for bulk storage.\n"
        f"• A conical roof (or hemispherical dome) on top to shed rainwater and debris.\n"
        f"Therefore, the roof solid is a **{ans}**."
    )

    return {
        "subskill": "46_composite_solid_silo_components",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct roof solid: {ans}", "marks": 2},
        ],
        "hints": [
            "A silo has a round circular base to match the cylinder.",
            "A cone or dome sits on top.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 47: Composite 3D Solid — Barn / House Components
# -----------------------------------------------------------------------------
def arch_47_composite_solid_tent_house_components(rng: random.Random, seed: int) -> Dict[str, Any]:
    svg = draw_polyhedron_3d_svg("rectangular_prism", seed=seed, title="House / Barn Structure")

    prompt = (
        f"A standard house or barn building model is formed by placing a triangular prism roof "
        f"on top of what 3D geometric solid?"
    )
    ans = "Rectangular prism"
    sol = (
        f"A house model consists of two joined components:\n"
        f"• Bottom walls: A rectangular prism (cuboid).\n"
        f"• Pitched roof: A right triangular prism.\n"
        f"Therefore, the base structure is a **{ans}**."
    )

    return {
        "subskill": "47_composite_solid_tent_house_components",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correct base solid: {ans}", "marks": 2},
        ],
        "hints": [
            "The walls of the building form a box.",
            "A box shape is a rectangular prism.",
            f"The answer is {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 48: Count Visible Faces of Joined Composite Solids
# -----------------------------------------------------------------------------
def arch_48_count_faces_composite_joined_solids(rng: random.Random, seed: int) -> Dict[str, Any]:
    svg = draw_polyhedron_3d_svg("square_pyramid", seed=seed, title="Pyramid Mounted on Cube")

    prompt = (
        f"A solid composite toy is created by gluing the square base of a square-based pyramid "
        f"directly onto one of the square faces of a cube (matching exactly in size).\n"
        f"How many total visible exterior faces does this composite solid have?"
    )
    ans = "9"
    sol = (
        f"Counting visible exterior faces:\n"
        f"• The cube originally has 6 square faces. Since one face is glued and covered, 5 square faces remain visible.\n"
        f"• The square pyramid has 5 faces (1 square base + 4 triangular sides). The square base is glued inside, leaving 4 triangular faces visible.\n"
        f"• Total visible faces = 5 (from cube) + 4 (from pyramid) = 9 faces.\n"
        f"Therefore, the composite solid has **{ans}** visible faces."
    )

    return {
        "subskill": "48_count_faces_composite_joined_solids",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": f"{ans} (5 cube faces + 4 pyramid faces)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Deduct internal glued faces from both solids", "marks": 1},
            {"desc": f"Calculate visible total: {ans}", "marks": 1},
        ],
        "hints": [
            "The two joined faces become internal and are no longer exterior faces.",
            "Cube has 6 - 1 = 5 exterior faces.",
            "Pyramid has 4 exterior faces.",
            f"Total = 5 + 4 = {ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 49: Orthographic Views to Solid Identification
# -----------------------------------------------------------------------------
def arch_49_spatial_reasoning_identify_solid_from_views(rng: random.Random, seed: int) -> Dict[str, Any]:
    choices = [
        ("Top view: circle; Front view: triangle; Side view: triangle", "Cone"),
        ("Top view: circle; Front view: rectangle; Side view: rectangle", "Cylinder"),
        ("Top view: square; Front view: triangle; Side view: triangle", "Square-based pyramid"),
        ("Top view: rectangle; Front view: triangle; Side view: rectangle", "Triangular prism"),
        ("Top view: circle; Front view: circle; Side view: circle", "Sphere"),
    ]
    views_desc, solid_ans = rng.choice(choices)
    svg = draw_polyhedron_3d_svg("cylinder" if "Cylinder" in solid_ans else ("cone" if "Cone" in solid_ans else "square_pyramid"), seed=seed, title="Orthographic Views")

    prompt = (
        f"An observer views a 3D solid from different angles and records the following orthographic projections:\n"
        f"• **{views_desc}**.\n"
        f"Identify the 3D solid."
    )
    sol = (
        f"Analyzing the projections:\n"
        f"{views_desc} corresponds exclusively to a **{solid_ans}**.\n"
        f"Therefore, the solid is a **{solid_ans}**."
    )

    return {
        "subskill": "49_spatial_reasoning_identify_solid_from_views",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": solid_ans,
        "expected_answer": solid_ans,
        "sample_answer": solid_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correctly deduce 3D solid: {solid_ans}", "marks": 2},
        ],
        "hints": [
            "Combine the 2D shapes seen from the top, front, and side.",
            f"{views_desc}.",
            f"The 3D solid is a {solid_ans}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


# -----------------------------------------------------------------------------
# Archetype 50: 3D Geometry Capstone Synthesis
# -----------------------------------------------------------------------------
def arch_50_3d_geometry_capstone_synthesis(rng: random.Random, seed: int) -> Dict[str, Any]:
    solids = [
        ("Rectangular prism", 6, 8, 12, "2 rectangular bases and 4 rectangular lateral faces", "rectangular_prism"),
        ("Triangular prism", 5, 6, 9, "2 parallel triangular bases and 3 rectangular lateral faces", "triangular_prism"),
        ("Square-based pyramid", 5, 5, 8, "1 square base and 4 triangular lateral faces meeting at an apex", "square_pyramid"),
        ("Regular Octahedron", 8, 6, 12, "8 equilateral triangular faces meeting 4 at each vertex", "octahedron"),
    ]
    name, f_val, v_val, e_val, desc, s_key = rng.choice(solids)
    svg = draw_polyhedron_3d_svg(s_key, seed=seed, title="Capstone 3D Synthesis")

    prompt = (
        f"A polyhedron has $F = {f_val}$ faces, $V = {v_val}$ vertices, and $E = {e_val}$ edges, "
        f"and is characterized by {desc}.\n"
        f"Identify the name of this polyhedron."
    )
    sol = (
        f"1. Checking Euler's formula: $V - E + F = {v_val} - {e_val} + {f_val} = 2$ (verified).\n"
        f"2. The description '{desc}' with $F = {f_val}, V = {v_val}, E = {e_val}$ uniquely defines the **{name}**.\n"
        f"Therefore, the polyhedron is the **{name}**."
    )

    return {
        "subskill": "50_3d_geometry_capstone_synthesis",
        "question_text": prompt,
        "prompt_latex": prompt,
        "correct_answer": name,
        "expected_answer": name,
        "sample_answer": name,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correctly identify polyhedron: {name}", "marks": 2},
        ],
        "hints": [
            f"F = {f_val}, V = {v_val}, E = {e_val}.",
            f"Feature: {desc}.",
            f"The polyhedron is {name}.",
        ],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }
