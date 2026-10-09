"""
Grade 7 Mathematics - Transformation Geometry Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Directly grounded in curriculum_docs_auto/Mathematics_Gr7/Term 3/04. Transformation geometry.md.

Archetypes Covered:
1. Lines of Symmetry of 2D Shapes (Square: 4, Rectangle: 2, Equilateral Triangle: 3, Isosceles: 1, Scalene: 0, Regular Hexagon: 6, Parallelogram: 0)
2. Translations (Coordinate translation rules: (x, y) -> (x + a, y + b))
3. Reflections (Reflection across x-axis or y-axis)
4. Enlargements and Reductions (Scale factor k, effect on side lengths and area)
"""

from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


# ============================================================================
# ARCHETYPE 1: Lines of Symmetry
# ============================================================================

def _generate_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    """
    Number of lines of symmetry in geometric shapes.
    """
    shapes_data = [
        ("an equilateral triangle", "3", "An equilateral triangle has 3 lines of symmetry (each passing through a vertex and the midpoint of the opposite side).", "equilateral_symmetry"),
        ("an isosceles triangle", "1", "An isosceles triangle has exactly 1 line of symmetry (passing through the vertex between the equal sides).", "isosceles_symmetry"),
        ("a scalene triangle", "0", "A scalene triangle has no equal sides and no equal angles, so it has 0 lines of symmetry.", "scalene_symmetry"),
        ("a rectangle", "2", "A rectangle has 2 lines of symmetry (the horizontal and vertical lines connecting the midpoints of opposite sides; its diagonals are NOT lines of symmetry).", "rectangle_symmetry"),
        ("a square", "4", "A square has 4 lines of symmetry (2 through opposite side midpoints and 2 along the diagonals).", "square_symmetry"),
        ("a parallelogram (not a rhombus or rectangle)", "0", "A general parallelogram has 0 lines of symmetry (folding along diagonals or midlines does not produce matching halves).", "parallelogram_symmetry"),
        ("a regular hexagon", "6", "A regular hexagon has 6 lines of symmetry (3 passing through opposite vertices and 3 through midpoints of opposite sides).", "hexagon_symmetry")
    ]

    shape_name, count_str, explanation, subskill = rng.choice(shapes_data)

    prompt = (
        f"How many lines of symmetry does **{shape_name}** have?"
    )

    return {
        "id": f"g7_math_trans_sym_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": count_str,
        "answer_latex": count_str,
        "explanation": explanation,
        "canonical_solution": explanation,
        "marks": 1,
        "term": 3,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 2,
        "subskill": subskill,
        "learning_objective_id": "math_g7_trans_lines_symmetry",
        "misconception_tags": [
            "diagonal_of_rectangle_mistaken_for_symmetry_line",
            "parallelogram_symmetry_error"
        ],
        "diagnostic_tags": ["transformation_geometry", "symmetry", "2d_shapes"],
        "minimum_mastery_score": 75,
        "keywords": ["lines of symmetry", "axis of symmetry", "mirror line", "fold in half"],
        "marking_schema": {
            "total_marks": 1,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct number of lines of symmetry ({count_str})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "strict"
        },
        "hints": {
            "tier_1": f"Think about how many ways you can fold the shape so both halves match exactly.",
            "tier_2": f"Be careful with diagonals: folding a rectangle along a diagonal does not match the edges.",
            "tier_3": f"{shape_name.capitalize()} has {count_str} lines of symmetry."
        }
    }


# ============================================================================
# ARCHETYPE 2: Translations
# ============================================================================

def _generate_translation_question(rng: random.Random) -> Dict[str, Any]:
    """
    Translation of a point on the Cartesian grid: (x, y) -> (x + a, y + b).
    """
    orig_x = rng.randint(-5, 5)
    orig_y = rng.randint(-5, 5)

    shift_x = rng.choice([-4, -3, -2, 2, 3, 4])
    shift_y = rng.choice([-4, -3, -2, 2, 3, 4])

    new_x = orig_x + shift_x
    new_y = orig_y + shift_y

    dir_x = f"{abs(shift_x)} units to the {'right' if shift_x > 0 else 'left'}"
    dir_y = f"{abs(shift_y)} units {'up' if shift_y > 0 else 'down'}"

    point_label = rng.choice(["A", "P", "K", "T"])

    prompt = (
        f"Point \\({point_label}({orig_x}; {orig_y})\\) is translated on a coordinate grid "
        f"**{dir_x}** and **{dir_y}**.\n\n"
        f"Determine the coordinates of the image point \\({point_label}'\\).\n"
        f"(Format your answer as '(x; y)', e.g. '({new_x}; {new_y})')."
    )

    sol = (
        f"Step 1: Write down the translation rule:\n"
        f"\\[ (x; y) \\longrightarrow (x {'+' if shift_x > 0 else '-'} {abs(shift_x)}; "
        f"y {'+' if shift_y > 0 else '-'} {abs(shift_y)}) \\]\n\n"
        f"Step 2: Apply to coordinates of {point_label}({orig_x}; {orig_y}):\n"
        f"\\(x' = {orig_x} {'+' if shift_x > 0 else '-'} {abs(shift_x)} = {new_x}\\)\n"
        f"\\(y' = {orig_y} {'+' if shift_y > 0 else '-'} {abs(shift_y)} = {new_y}\\)\n\n"
        f"Therefore, \\({point_label}'({new_x}; {new_y})\\)."
    )

    ans_str = f"({new_x}; {new_y})"

    return {
        "id": f"g7_math_trans_coord_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans_str,
        "answer_latex": f"({new_x}; {new_y})",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "term": 3,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 3,
        "subskill": "point_translation",
        "learning_objective_id": "math_g7_trans_translation_coords",
        "misconception_tags": [
            "translation_direction_sign_inversion",
            "x_y_coordinate_swap"
        ],
        "diagnostic_tags": ["transformation_geometry", "translation", "coordinates"],
        "minimum_mastery_score": 75,
        "keywords": ["translation", "image point", "coordinates", "shift"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct x-coordinate ({new_x})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct y-coordinate ({new_y})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Moving right increases x, moving left decreases x. Moving up increases y, moving down decreases y.",
            "tier_2": f"New x = {orig_x} {'+' if shift_x > 0 else '-'} {abs(shift_x)}. New y = {orig_y} {'+' if shift_y > 0 else '-'} {abs(shift_y)}.",
            "tier_3": f"Coordinates: ({new_x}; {new_y})."
        }
    }


# ============================================================================
# ARCHETYPE 3: Reflections across Axes
# ============================================================================

def _generate_reflection_question(rng: random.Random) -> Dict[str, Any]:
    """
    Reflection of a point across the x-axis or y-axis.
    Across x-axis: (x, y) -> (x, -y).
    Across y-axis: (x, y) -> (-x, y).
    """
    axis = rng.choice(["x-axis", "y-axis"])
    x = rng.choice([-6, -4, -3, 2, 4, 5])
    y = rng.choice([-5, -3, 2, 4, 6])
    pt = rng.choice(["B", "C", "Q", "M"])

    if axis == "x-axis":
        new_x = x
        new_y = -y
        rule = "(x; y) \\longrightarrow (x; -y)"
        rule_desc = "The x-coordinate remains unchanged, and the sign of the y-coordinate is inverted."
    else:
        new_x = -x
        new_y = y
        rule = "(x; y) \\longrightarrow (-x; y)"
        rule_desc = "The sign of the x-coordinate is inverted, and the y-coordinate remains unchanged."

    prompt = (
        f"Point \\({pt}({x}; {y})\\) is reflected across the **{axis}**.\n\n"
        f"Determine the coordinates of the reflected image point \\({pt}'\\).\n"
        f"(Format your answer as '(x; y)', e.g. '({new_x}; {new_y})')."
    )

    sol = (
        f"Step 1: State the reflection rule across the {axis}:\n"
        f"\\[ {rule} \\]\n"
        f"({rule_desc})\n\n"
        f"Step 2: Apply to point \\({pt}({x}; {y})\\):\n"
        f"\\[ {pt}'({new_x}; {new_y}) \\]"
    )

    ans_str = f"({new_x}; {new_y})"

    return {
        "id": f"g7_math_trans_refl_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans_str,
        "answer_latex": f"({new_x}; {new_y})",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "term": 3,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 3,
        "subskill": "point_reflection",
        "learning_objective_id": "math_g7_trans_reflection_axis",
        "misconception_tags": [
            "axis_reflection_sign_swap_confusion",
            "x_y_coordinate_swap"
        ],
        "diagnostic_tags": ["transformation_geometry", "reflection", "axes"],
        "minimum_mastery_score": 75,
        "keywords": ["reflection", "x-axis", "y-axis", "image point", "mirror"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct x-coordinate ({new_x})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct y-coordinate ({new_y})", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"When reflecting across the {axis}, which coordinate changes sign?",
            "tier_2": f"Reflection across the {axis}: {rule_desc}",
            "tier_3": f"{pt}'({new_x}; {new_y})."
        }
    }


# ============================================================================
# ARCHETYPE 4: Enlargements & Reductions (Scale Factor)
# ============================================================================

def _generate_scale_factor_question(rng: random.Random) -> Dict[str, Any]:
    """
    Enlargements and reductions: side length scaling.
    """
    is_enlarge = rng.choice([True, False])
    orig_l = rng.randint(4, 12)
    orig_w = rng.randint(2, orig_l - 1)
    k = rng.choice([2, 3, 4])

    if is_enlarge:
        new_l = orig_l * k
        new_w = orig_w * k
        prompt = (
            f"A rectangle with dimensions \\({orig_l}\\text{{ cm}}\\) by \\({orig_w}\\text{{ cm}}\\) "
            f"is **enlarged** by a scale factor of \\(k = {k}\\).\n\n"
            f"Calculate the length of the longer side of the enlarged rectangle."
        )
        sol = (
            f"Step 1: To enlarge a shape by scale factor \\(k\\), multiply each side length by \\(k\\):\n"
            f"\\[ \\text{{New length}} = {orig_l} \\times {k} = {new_l}\\text{{ cm}} \\]"
        )
        ans = str(new_l)
        ans_display = f"{new_l} cm"
        t1 = f"Multiply the original length by the scale factor."
        t2 = f"New length = {orig_l} × {k}."
        t3 = f"{orig_l} × {k} = {new_l} cm."
        subskill = "enlargement_scale_factor"
    else:
        new_l = orig_l
        scaled_l = orig_l * k
        prompt = (
            f"A rectangular poster with a length of \\({scaled_l}\\text{{ cm}}\\) "
            f"is **reduced** by a scale factor of \\(k = \\frac{{1}}{{{k}}}\\).\n\n"
            f"Calculate the length of the reduced poster."
        )
        sol = (
            f"Step 1: To reduce a shape by a scale factor \\(\\frac{{1}}{{{k}}}\\), divide the length by \\({k}\\):\n"
            f"\\[ \\text{{New length}} = \\frac{{{scaled_l}}}{{{k}}} = {new_l}\\text{{ cm}} \\]"
        )
        ans = str(new_l)
        ans_display = f"{new_l} cm"
        t1 = f"To reduce, divide the original length by {k}."
        t2 = f"New length = {scaled_l} ÷ {k}."
        t3 = f"{scaled_l} ÷ {k} = {new_l} cm."
        subskill = "reduction_scale_factor"

    return {
        "id": f"g7_math_trans_scale_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans_display,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "term": 3,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 2,
        "subskill": subskill,
        "learning_objective_id": "math_g7_trans_scale_factor",
        "misconception_tags": [
            "add_scale_factor_instead_of_multiplying",
            "arithmetic_calculation_error"
        ],
        "diagnostic_tags": ["transformation_geometry", "scale_factor", "enlargement_reduction"],
        "minimum_mastery_score": 75,
        "keywords": ["scale factor", "enlargement", "reduction", "dimensions"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Application of scale factor multiplication/division", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct calculated dimension ({ans})", "marks": 1, "editable": True}
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
    Main entry point for Grade 7 Transformation Geometry Generator.
    Supports atomic micro-drills:
    - mode="elementary_symmetry": Lines of symmetry in 2D shapes
    - mode="elementary_translation": Point translations on grid
    - mode="elementary_reflection": Reflection across axes
    - mode="elementary_scale": Enlargements and reductions
    - mode="compound": Full authentic exam mix
    """
    rng = _rng(seed)
    questions = []

    for _ in range(count):
        if mode == "elementary_symmetry" or subskill == "symmetry":
            q = _generate_lines_of_symmetry(rng)
        elif mode == "elementary_translation" or subskill == "translation":
            q = _generate_translation_question(rng)
        elif mode == "elementary_reflection" or subskill == "reflection":
            q = _generate_reflection_question(rng)
        elif mode == "elementary_scale" or subskill in ["scale", "enlargement", "reduction"]:
            q = _generate_scale_factor_question(rng)
        else: # compound: pick across all archetypes
            archetype = rng.choice([
                lambda: _generate_lines_of_symmetry(rng),
                lambda: _generate_translation_question(rng),
                lambda: _generate_reflection_question(rng),
                lambda: _generate_scale_factor_question(rng)
            ])
            q = archetype()
        questions.append(q)

    return questions
