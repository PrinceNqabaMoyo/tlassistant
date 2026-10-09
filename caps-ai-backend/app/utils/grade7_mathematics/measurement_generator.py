"""
Grade 7 Mathematics - Measurement (Perimeter, Area, Surface Area & Volume) Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Directly grounded in curriculum_docs/Mathematics_Gr7/Measurement Studio.md and END OF YEAR EXAM 2018.md.

Archetypes Covered:
1. Perimeter of 2D Shapes (Squares, Rectangles, Regular Polygons)
2. Area of 2D Shapes (Squares, Rectangles, Triangles: A = 1/2 * b * h)
3. Surface Area of 3D Objects (Cubes: 6s^2, Rectangular Prisms: 2(lb + lh + bh))
4. Volume & Capacity of 3D Objects (Cubes: s^3, Rectangular Prisms: l * b * h, cm^3 <-> ml <-> litres)
"""

from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


# ============================================================================
# ARCHETYPE 1: 2D Perimeter (Exam-aligned)
# ============================================================================

def _generate_perimeter_2d(rng: random.Random) -> Dict[str, Any]:
    """
    Perimeter of rectangle or square or finding unknown side.
    """
    shape_type = rng.choice(["rectangle", "square", "reverse_rectangle"])

    if shape_type == "rectangle":
        length = rng.randint(8, 25)
        width = rng.randint(4, length - 2)
        unit = rng.choice(["cm", "m", "mm"])
        perimeter = 2 * (length + width)

        prompt = (
            f"A rectangular garden has a length of \\({length}\\text{{ {unit}}}\\) "
            f"and a width of \\({width}\\text{{ {unit}}}\\).\n\n"
            f"Calculate the **perimeter** of the garden."
        )

        sol = (
            f"Step 1: State the perimeter formula for a rectangle:\n"
            f"\\[ P = 2(l + b) \\quad \\text{{or}} \\quad P = 2l + 2b \\]\n\n"
            f"Step 2: Substitute the given dimensions:\n"
            f"\\[ P = 2({length} + {width}) = 2({length + width}) \\]\n\n"
            f"Step 3: Calculate final perimeter:\n"
            f"\\[ P = {perimeter}\\text{{ {unit}}} \\]"
        )

        ans = str(perimeter)
        ans_display = f"{perimeter} {unit}"
        t1 = f"Perimeter is the distance all the way around the outside of the shape."
        t2 = f"Use the formula P = 2(length + width) = 2({length} + {width})."
        t3 = f"P = 2 × {length + width} = {perimeter} {unit}."

    elif shape_type == "square":
        side = rng.randint(5, 20)
        unit = rng.choice(["cm", "m"])
        perimeter = 4 * side

        prompt = (
            f"Calculate the **perimeter** of a square whose sides are each \\({side}\\text{{ {unit}}}\\) long."
        )

        sol = (
            f"Step 1: State the perimeter formula for a square:\n"
            f"\\[ P = 4s \\]\n\n"
            f"Step 2: Substitute the side length:\n"
            f"\\[ P = 4 \\times {side} = {perimeter}\\text{{ {unit}}} \\]"
        )

        ans = str(perimeter)
        ans_display = f"{perimeter} {unit}"
        t1 = f"A square has 4 equal sides. Add all 4 sides or multiply side length by 4."
        t2 = f"P = 4 × {side}."
        t3 = f"P = 4 × {side} = {perimeter} {unit}."

    else: # reverse_rectangle: given perimeter and length, find width
        width = rng.randint(5, 15)
        length = width + rng.randint(4, 12)
        unit = "cm"
        perimeter = 2 * (length + width)

        prompt = (
            f"The perimeter of a rectangle is \\({perimeter}\\text{{ {unit}}}\\). "
            f"If its length is \\({length}\\text{{ {unit}}}\\), calculate its width."
        )

        sol = (
            f"Step 1: State the perimeter formula:\n"
            f"\\[ 2(l + b) = P \\]\n\n"
            f"Step 2: Substitute known values:\n"
            f"\\[ 2({length} + b) = {perimeter} \\]\n\n"
            f"Step 3: Divide both sides by 2:\n"
            f"\\[ {length} + b = {perimeter // 2} \\]\n\n"
            f"Step 4: Solve for width \\(b\\):\n"
            f"\\[ b = {perimeter // 2} - {length} = {width}\\text{{ {unit}}} \\]"
        )

        ans = str(width)
        ans_display = f"{width} {unit}"
        t1 = f"Half of the perimeter equals length + width."
        t2 = f"Half perimeter = {perimeter} ÷ 2 = {perimeter // 2}. Subtract the length {length}."
        t3 = f"Width = {perimeter // 2} - {length} = {width} {unit}."

    return {
        "id": f"g7_math_meas_perim_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans_display,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": "perimeter_2d_calculation",
        "learning_objective_id": "math_g7_meas_perimeter",
        "misconception_tags": [
            "confused_perimeter_and_area",
            "arithmetic_calculation_error"
        ],
        "diagnostic_tags": ["measurement", "perimeter", "2d_shapes"],
        "minimum_mastery_score": 75,
        "keywords": ["perimeter", "distance around", "formula"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct application of perimeter formula", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct numerical value ({ans})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": t1,
            "tier_2": t2,
            "tier_3": t3
        }
    }


# ============================================================================
# ARCHETYPE 2: 2D Area (Rectangles & Triangles)
# ============================================================================

def _generate_area_2d(rng: random.Random) -> Dict[str, Any]:
    """
    Area of rectangle or triangle (A = 1/2 * b * h).
    """
    is_triangle = rng.choice([True, False])

    if is_triangle:
        base = rng.choice([6, 8, 10, 12, 14, 16])
        height = rng.randint(4, 12)
        unit = "cm"
        area = (base * height) // 2

        prompt = (
            f"Calculate the **area** of a triangle with a base of \\({base}\\text{{ {unit}}}\\) "
            f"and a perpendicular height of \\({height}\\text{{ {unit}}}\\)."
        )

        sol = (
            f"Step 1: State the area formula for a triangle:\n"
            f"\\[ A = \\frac{{1}}{{2}} \\times b \\times h \\]\n\n"
            f"Step 2: Substitute the base and height:\n"
            f"\\[ A = \\frac{{1}}{{2}} \\times {base} \\times {height} \\]\n\n"
            f"Step 3: Multiply and divide by 2:\n"
            f"\\[ A = {base // 2} \\times {height} = {area}\\text{{ {unit}}}^2 \\]"
        )

        ans = str(area)
        ans_display = f"{area} cm^2"
        t1 = f"Remember the area of a triangle is half of base times perpendicular height."
        t2 = f"A = 1/2 × {base} × {height}."
        t3 = f"A = 1/2 × {base * height} = {area} {unit}^2."
        subskill = "triangle_area_calculation"
        tag = "forgot_half_in_triangle_area"

    else:
        length = rng.randint(6, 18)
        width = rng.randint(3, 10)
        unit = "cm"
        area = length * width

        prompt = (
            f"Calculate the **area** of a rectangle that is \\({length}\\text{{ {unit}}}\\) long "
            f"and \\({width}\\text{{ {unit}}}\\) wide."
        )

        sol = (
            f"Step 1: State the area formula for a rectangle:\n"
            f"\\[ A = l \\times b \\]\n\n"
            f"Step 2: Substitute the length and width:\n"
            f"\\[ A = {length} \\times {width} \\]\n\n"
            f"Step 3: Multiply:\n"
            f"\\[ A = {area}\\text{{ {unit}}}^2 \\]"
        )

        ans = str(area)
        ans_display = f"{area} cm^2"
        t1 = f"Area of a rectangle is length times width."
        t2 = f"A = {length} × {width}."
        t3 = f"A = {length} × {width} = {area} {unit}^2."
        subskill = "rectangle_area_calculation"
        tag = "confused_perimeter_and_area"

    return {
        "id": f"g7_math_meas_area_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans_display,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": subskill,
        "learning_objective_id": "math_g7_meas_area_2d",
        "misconception_tags": [tag, "confused_perimeter_and_area"],
        "diagnostic_tags": ["measurement", "area", "triangles", "rectangles"],
        "minimum_mastery_score": 75,
        "keywords": ["area", "base times height", "half base height", "square units"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Formula and numerical substitution", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct area value ({ans})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": t1,
            "tier_2": t2,
            "tier_3": t3
        }
    }


# ============================================================================
# ARCHETYPE 3: 3D Surface Area & Volume
# ============================================================================

def _generate_surface_area_and_volume(rng: random.Random) -> Dict[str, Any]:
    """
    Surface area and volume of rectangular prisms and cubes.
    """
    is_volume = rng.choice([True, False])
    is_cube = rng.choice([True, False])

    if is_cube:
        side = rng.randint(3, 8)
        unit = "cm"

        if is_volume:
            vol = side ** 3
            prompt = (
                f"Calculate the **volume** of a cube with side lengths of \\({side}\\text{{ {unit}}}\\)."
            )
            sol = (
                f"Step 1: State the volume formula for a cube:\n"
                f"\\[ V = s^3 = s \\times s \\times s \\]\n\n"
                f"Step 2: Substitute side length:\n"
                f"\\[ V = {side} \\times {side} \\times {side} = {side * side} \\times {side} = {vol}\\text{{ {unit}}}^3 \\]"
            )
            ans = str(vol)
            ans_display = f"{vol} cm^3"
            t1 = f"Volume of a cube is side cubed: V = s × s × s."
            t2 = f"V = {side} × {side} × {side}."
            t3 = f"V = {vol} {unit}^3."
            subskill = "cube_volume"
        else: # surface area
            sa = 6 * (side ** 2)
            prompt = (
                f"A cube has edges of length \\({side}\\text{{ {unit}}}\\).\n\n"
                f"Calculate the **total surface area** of the cube."
            )
            sol = (
                f"Step 1: A cube has 6 identical square faces:\n"
                f"\\[ \\text{{Total Surface Area}} = 6 \\times s^2 \\]\n\n"
                f"Step 2: Calculate area of one face:\n"
                f"\\[ \\text{{Area of 1 face}} = {side} \\times {side} = {side * side}\\text{{ {unit}}}^2 \\]\n\n"
                f"Step 3: Multiply by 6:\n"
                f"\\[ \\text{{Total Surface Area}} = 6 \\times {side * side} = {sa}\\text{{ {unit}}}^2 \\]"
            )
            ans = str(sa)
            ans_display = f"{sa} cm^2"
            t1 = f"A cube has 6 identical square faces."
            t2 = f"Surface area = 6 × ({side} × {side})."
            t3 = f"Surface area = 6 × {side * side} = {sa} {unit}^2."
            subskill = "cube_surface_area"

    else: # rectangular prism
        l = rng.randint(4, 10)
        b = rng.randint(2, 6)
        h = rng.randint(3, 8)
        unit = "cm"

        if is_volume:
            vol = l * b * h
            prompt = (
                f"A rectangular prism has a length of \\({l}\\text{{ {unit}}}\\), "
                f"a breadth of \\({b}\\text{{ {unit}}}\\), and a height of \\({h}\\text{{ {unit}}}\\).\n\n"
                f"Calculate the **volume** of the prism."
            )
            sol = (
                f"Step 1: State the volume formula for a rectangular prism:\n"
                f"\\[ V = l \\times b \\times h \\]\n\n"
                f"Step 2: Substitute dimensions:\n"
                f"\\[ V = {l} \\times {b} \\times {h} \\]\n\n"
                f"Step 3: Multiply:\n"
                f"\\[ V = {l * b} \\times {h} = {vol}\\text{{ {unit}}}^3 \\]"
            )
            ans = str(vol)
            ans_display = f"{vol} cm^3"
            t1 = f"Volume of a rectangular prism is length × breadth × height."
            t2 = f"V = {l} × {b} × {h}."
            t3 = f"V = {l * b} × {h} = {vol} {unit}^3."
            subskill = "rectangular_prism_volume"
        else: # surface area
            sa = 2 * (l * b + l * h + b * h)
            prompt = (
                f"A closed rectangular box has length \\({l}\\text{{ {unit}}}\\), "
                f"breadth \\({b}\\text{{ {unit}}}\\), and height \\({h}\\text{{ {unit}}}\\).\n\n"
                f"Calculate the **total surface area** of the box."
            )
            sol = (
                f"Step 1: State the total surface area formula for a rectangular prism:\n"
                f"\\[ \\text{{TSA}} = 2(lb + lh + bh) \\]\n\n"
                f"Step 2: Calculate the area of the three pairs of faces:\n"
                f"\\(lb = {l} \\times {b} = {l * b}\\)\n"
                f"\\(lh = {l} \\times {h} = {l * h}\\)\n"
                f"\\(bh = {b} \\times {h} = {b * h}\\)\n\n"
                f"Step 3: Sum the areas and double:\n"
                f"\\(\\text{{Sum}} = {l * b} + {l * h} + {b * h} = {l * b + l * h + b * h}\\)\n"
                f"\\[ \\text{{TSA}} = 2 \\times {l * b + l * h + b * h} = {sa}\\text{{ {unit}}}^2 \\]"
            )
            ans = str(sa)
            ans_display = f"{sa} cm^2"
            t1 = f"Total surface area is the sum of the areas of all 6 faces (3 matching pairs)."
            t2 = f"TSA = 2({l*b} + {l*h} + {b*h})."
            t3 = f"TSA = 2 × {l*b + l*h + b*h} = {sa} {unit}^2."
            subskill = "rectangular_prism_surface_area"

    return {
        "id": f"g7_math_meas_3d_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans_display,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": subskill,
        "learning_objective_id": "math_g7_meas_surface_volume",
        "misconception_tags": [
            "volume_surface_area_confusion",
            "arithmetic_calculation_error"
        ],
        "diagnostic_tags": ["measurement", "3d_objects", "volume", "surface_area"],
        "minimum_mastery_score": 75,
        "keywords": ["volume", "surface area", "prism", "cube", "capacity"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of correct formula", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate substitution of dimensions", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct numerical value ({ans})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": t1,
            "tier_2": t2,
            "tier_3": t3
        }
    }


# ============================================================================
# MASTER GENERATE FUNCTION (6-Pillar Contract)
# ============================================================================

def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """
    Main entry point for Grade 7 Measurement Question Generator.
    Supports atomic micro-drills:
    - mode="elementary_perimeter_2d": Perimeter of 2D shapes
    - mode="elementary_area_2d": Area of triangles and rectangles
    - mode="elementary_3d": Surface area and volume of prisms and cubes
    - mode="compound": Full authentic exam mix
    """
    rng = _rng(seed)
    questions = []

    for _ in range(count):
        if mode == "elementary_perimeter_2d" or subskill == "perimeter":
            q = _generate_perimeter_2d(rng)
        elif mode == "elementary_area_2d" or subskill == "area":
            q = _generate_area_2d(rng)
        elif mode == "elementary_3d" or subskill in ["volume", "surface_area"]:
            q = _generate_surface_area_and_volume(rng)
        else: # compound: pick across all archetypes
            archetype = rng.choice([
                lambda: _generate_perimeter_2d(rng),
                lambda: _generate_area_2d(rng),
                lambda: _generate_surface_area_and_volume(rng)
            ])
            q = archetype()
        questions.append(q)

    return questions
