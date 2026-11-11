"""Grade 9 Mathematics — Transformation Geometry Generator (Deterministic 6-Pillar Contract).

Curriculum Alignment:
- Grade 9 Term 3: Transformation geometry
- South African National Curriculum Standards (Senior Phase Mathematics)
- Transformations on the Cartesian coordinate plane:
  * Translations: (x, y) -> (x + a, y + b)
  * Reflections: across the x-axis (x, -y), y-axis (-x, y), and the line y = x (y, x)
  * Rotations: 90° clockwise (y, -x), 90° anti-clockwise (-y, x), and 180° (-x, -y) about the origin
  * Enlargements and Reductions: scale factor k, (x, y) -> (kx, ky), effect on area: Area' = k^2 * Area

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with coordinate rule, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs (kind: 'function_graph' with coordinate landmarks)
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng

TOPIC = "grade9_math_transformation_geometry"
LO = "math9_transformation_geometry"


def generate_grade9_transformation_geometry_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "translation_coordinates",
        "reflection_axes",
        "reflection_line_y_equals_x",
        "rotation_origin",
        "enlargement_area_factor",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_trans_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "translation_coordinates":
        # Point P(x, y) translated by (a units horizontally, b units vertically)
        px = r.randint(-5, 5)
        py = r.randint(-5, 5)
        dx = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
        dy = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
        
        dir_x = "units to the right" if dx > 0 else "units to the left"
        dir_y = "units up" if dy > 0 else "units down"
        
        im_x = px + dx
        im_y = py + dy

        question_text = (
            f"Point $P({px}; {py})$ is plotted on a Cartesian plane.\n\n"
            f"1. Write down the coordinate mapping rule for a translation of "
            f"${abs(dx)}$ {dir_x} and ${abs(dy)}$ {dir_y}.\n"
            f"2. Determine the coordinates of the image point $P'$."
        )

        steps = [
            {"id": "S1", "statement": f"Mapping rule: $(x; y) \\to (x {'+' if dx > 0 else '-'} {abs(dx)}; y {'+' if dy > 0 else '-'} {abs(dy)})$", "reason": "translation vector rule", "deps": []},
            {"id": "S2", "statement": f"Calculate x': ${px} {'+' if dx > 0 else '-'} {abs(dx)} = {im_x}$", "reason": "horizontal translation", "deps": ["S1"]},
            {"id": "S3", "statement": f"Calculate y': ${py} {'+' if dy > 0 else '-'} {abs(dy)} = {im_y}$", "reason": "vertical translation", "deps": ["S1"]},
            {"id": "S4", "statement": f"Image coordinates: $P'({im_x}; {im_y})$", "reason": "final image point", "deps": ["S2", "S3"]},
        ]

        hints = [
            "A horizontal shift to the right adds to the x-coordinate; to the left subtracts from x. A vertical shift upwards adds to y; downwards subtracts from y.",
            f"Rule: $(x; y) \\to (x + ({dx}); y + ({dy}))$.",
            f"Substitute the coordinates of $P({px}; {py})$: $x' = {px} + ({dx}) = {im_x}$ and $y' = {py} + ({dy}) = {im_y}$. Thus $P'({im_x}; {im_y})$.",
        ]

        error_tax = [
            {
                "id": "err_swapped_axes",
                "tag": "misconception_xy_swap",
                "condition": "Applied horizontal shift to y and vertical shift to x",
                "feedback": "Horizontal translation affects the x-coordinate (first value), vertical translation affects the y-coordinate (second value).",
            },
        ]

        sample_answer = (
            f"1. $(x; y) \\to (x {'+' if dx > 0 else '-'} {abs(dx)}; y {'+' if dy > 0 else '-'} {abs(dy)})$\n"
            f"2. $x' = {px} + ({dx}) = {im_x}$\n"
            f"   $y' = {py} + ({dy}) = {im_y}$\n"
            f"   $P'({im_x}; {im_y})$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "function_graph",
            "domain": [-8, 8],
            "range": [-8, 8],
            "landmarks": [
                {"x": px, "y": py, "label": f"P({px}; {py})"},
                {"x": im_x, "y": im_y, "label": f"P'({im_x}; {im_y})"},
            ],
        }

        correct_ans = f"({im_x}; {im_y})"
        subskill_id = "translation_coordinates"
        reason_code = "translation mapping (x + a; y + b)"
        marks = 3

    elif archetype == "reflection_axes":
        # Reflect in x-axis or y-axis
        axis = r.choice(["x-axis", "y-axis"])
        px = r.randint(-6, 6)
        py = r.randint(-6, 6)
        if px == 0:
            px = 3
        if py == 0:
            py = 4

        if axis == "x-axis":
            rule_str = "$(x; y) \\to (x; -y)$"
            im_x = px
            im_y = -py
            explanation = "Reflection in the x-axis leaves the x-coordinate unchanged and negates the y-coordinate."
        else:
            rule_str = "$(x; y) \\to (-x; y)$"
            im_x = -px
            im_y = py
            explanation = "Reflection in the y-axis negates the x-coordinate and leaves the y-coordinate unchanged."

        question_text = (
            f"Point $A({px}; {py})$ is reflected across the ${axis}$.\n\n"
            f"1. State the general algebraic transformation rule for reflection in the ${axis}$.\n"
            f"2. Write down the coordinates of the image point $A'$."
        )

        steps = [
            {"id": "S1", "statement": f"General rule for reflection in {axis}: {rule_str}", "reason": "reflection definition", "deps": []},
            {"id": "S2", "statement": f"Apply rule to $A({px}; {py}) \\implies A'({im_x}; {im_y})$", "reason": "sign negation", "deps": ["S1"]},
        ]

        hints = [
            f"Think about flipping a point across the {axis}. The distance to the mirror line is preserved, but it flips to the opposite side.",
            f"For reflection in the {axis}: {rule_str}.",
            f"Applying the rule to $A({px}; {py})$ gives $A'({im_x}; {im_y})$.",
        ]

        error_tax = [
            {
                "id": "err_negated_wrong_coord",
                "tag": "misconception_axis_negation_inversion",
                "condition": "Negated the coordinate matching the axis name (e.g. negated x for x-axis)",
                "feedback": f"When reflecting across the {axis}, the {'x' if axis == 'x-axis' else 'y'} coordinate stays the same because the axis itself doesn't move. The other coordinate changes sign.",
            },
        ]

        sample_answer = (
            f"1. {rule_str}\n"
            f"2. $A'({im_x}; {im_y})$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "function_graph",
            "domain": [-8, 8],
            "range": [-8, 8],
            "landmarks": [
                {"x": px, "y": py, "label": f"A({px}; {py})"},
                {"x": im_x, "y": im_y, "label": f"A'({im_x}; {im_y})"},
            ],
        }

        correct_ans = f"({im_x}; {im_y})"
        subskill_id = "reflection_axes"
        reason_code = f"reflection across {axis}"
        marks = 2

    elif archetype == "reflection_line_y_equals_x":
        # Reflection in the line y = x: (x; y) -> (y; x)
        px = r.randint(-5, 6)
        py = r.randint(-5, 6)
        if px == py:
            py = px + 3

        im_x = py
        im_y = px

        question_text = (
            f"Triangle vertex $B({px}; {py})$ is reflected in the line $y = x$.\n\n"
            f"1. State the general transformation rule for reflection in the line $y = x$.\n"
            f"2. Determine the coordinates of the image vertex $B'$."
        )

        steps = [
            {"id": "S1", "statement": "General rule for reflection in $y = x$: $(x; y) \\to (y; x)$", "reason": "diagonal reflection property", "deps": []},
            {"id": "S2", "statement": f"Swap coordinates: $x' = {py}$, $y' = {px}$", "reason": "direct transposition", "deps": ["S1"]},
            {"id": "S3", "statement": f"Image coordinates: $B'({im_x}; {im_y})$", "reason": "final image point", "deps": ["S2"]},
        ]

        hints = [
            "Reflecting in the diagonal line y = x interchanges the roles of x and y.",
            "The coordinate rule is $(x; y) \\to (y; x)$.",
            f"Swap the values of $B({px}; {py})$: the new x-coordinate is {py} and the new y-coordinate is {px}, so $B'({im_x}; {im_y})$.",
        ]

        error_tax = [
            {
                "id": "err_negated_and_swapped",
                "tag": "misconception_line_y_minus_x",
                "condition": "Wrote (-y; -x) which is reflection across y = -x",
                "feedback": "For the line y = x, simply swap the coordinates: (x; y) → (y; x). Do not change their signs.",
            },
        ]

        sample_answer = (
            f"1. $(x; y) \\to (y; x)$\n"
            f"2. $B'({im_x}; {im_y})$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "function_graph",
            "domain": [-8, 8],
            "range": [-8, 8],
            "curves": [{"formula": "x", "label": "y = x"}],
            "landmarks": [
                {"x": px, "y": py, "label": f"B({px}; {py})"},
                {"x": im_x, "y": im_y, "label": f"B'({im_x}; {im_y})"},
            ],
        }

        correct_ans = f"({im_x}; {im_y})"
        subskill_id = "reflection_line_y_equals_x"
        reason_code = "reflection in line y = x: (y; x)"
        marks = 2

    elif archetype == "rotation_origin":
        # Rotation of 90° clockwise, 90° anti-clockwise, or 180° about the origin
        rot_type = r.choice(["90_cw", "90_ccw", "180"])
        px = r.randint(-5, 5)
        py = r.randint(-5, 5)
        if px == 0 and py == 0:
            px, py = 3, 4

        if rot_type == "90_cw":
            name = "90° clockwise about the origin"
            rule_str = "$(x; y) \\to (y; -x)$"
            im_x = py
            im_y = -px
        elif rot_type == "90_ccw":
            name = "90° anti-clockwise about the origin"
            rule_str = "$(x; y) \\to (-y; x)$"
            im_x = -py
            im_y = px
        else:
            name = "180° about the origin"
            rule_str = "$(x; y) \\to (-x; -y)$"
            im_x = -px
            im_y = -py

        question_text = (
            f"Point $C({px}; {py})$ is rotated by ${name}$.\n\n"
            f"1. State the algebraic rule for this rotation.\n"
            f"2. Determine the coordinates of the image point $C'$."
        )

        steps = [
            {"id": "S1", "statement": f"Rotation rule for {name}: {rule_str}", "reason": "rotation coordinate mapping", "deps": []},
            {"id": "S2", "statement": f"Apply rule to $C({px}; {py}) \\implies C'({im_x}; {im_y})$", "reason": "coordinate calculation", "deps": ["S1"]},
        ]

        hints = [
            f"Recall the rotation rules about the origin:\n- 90° clockwise: (x; y) → (y; -x)\n- 90° anti-clockwise: (x; y) → (-y; x)\n- 180°: (x; y) → (-x; -y).",
            f"For {name}, apply the rule: {rule_str}.",
            f"Substituting $x = {px}$ and $y = {py}$ gives $C'({im_x}; {im_y})$.",
        ]

        error_tax = [
            {
                "id": "err_swapped_direction",
                "tag": "misconception_rotation_direction",
                "condition": "Confused clockwise and anti-clockwise rules",
                "feedback": "Remember: 90° clockwise turns toward the positive x-axis, so (x; y) → (y; -x). 90° anti-clockwise turns toward positive y, so (x; y) → (-y; x).",
            },
        ]

        sample_answer = (
            f"1. {rule_str}\n"
            f"2. $C'({im_x}; {im_y})$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "function_graph",
            "domain": [-8, 8],
            "range": [-8, 8],
            "landmarks": [
                {"x": px, "y": py, "label": f"C({px}; {py})"},
                {"x": im_x, "y": im_y, "label": f"C'({im_x}; {im_y})"},
            ],
        }

        correct_ans = f"({im_x}; {im_y})"
        subskill_id = "rotation_origin"
        reason_code = f"rotation {name}"
        marks = 2

    else:
        # enlargement_area_factor: Scale factor k and effect on area (k^2)
        # Classic Grade 9 examination question:
        # A rectangle has dimensions l and b, area = l*b.
        # It is enlarged by scale factor k.
        # What is the area of the enlarged rectangle? Area' = k^2 * Area.
        k = r.choice([2, 3, 4, 5])
        orig_area = r.randint(12, 40)
        new_area = orig_area * (k ** 2)

        question_text = (
            f"A geometric polygon $P$ has an area of ${orig_area}\\text{{ cm}}^2$.\n\n"
            f"The polygon is enlarged by a constant scale factor of $k = {k}$ "
            f"to form image polygon $P'$.\n\n"
            f"1. State the relationship between the scale factor $k$ and the ratio of the areas "
            f"$\\frac{{\\text{{Area of }} P'}}{{\\text{{Area of }} P}}$.\n"
            f"2. Calculate the area of the enlarged polygon $P'$."
        )

        steps = [
            {"id": "S1", "statement": "$\\text{{Area of image}} = k^2 \\times \\text{{Area of original}}$", "reason": "area enlargement theorem", "deps": []},
            {"id": "S2", "statement": f"Calculate scale factor squared: $k^2 = {k}^2 = {k**2}$", "reason": "arithmetic", "deps": ["S1"]},
            {"id": "S3", "statement": f"$\\text{{Area of }} P' = {k**2} \\times {orig_area} = {new_area}\\text{{ cm}}^2$", "reason": "multiply by original area", "deps": ["S2"]},
        ]

        hints = [
            "When a 2D shape is enlarged by a linear scale factor k, its perimeter increases by k, but its area increases by k² (the square of the scale factor).",
            f"Use the area enlargement formula: $\\text{{Area}}' = k^2 \\times \\text{{Area}} = ({k})^2 \\times {orig_area}$.",
            f"Calculate: ${k}^2 = {k**2}$. Multiply ${k**2} \\times {orig_area} = {new_area}\\text{{ cm}}^2$.",
        ]

        error_tax = [
            {
                "id": "err_multiplied_by_k_not_ksquared",
                "tag": "misconception_linear_vs_area_scaling",
                "condition": f"Calculated {k} * {orig_area} = {k * orig_area}",
                "feedback": "Area has two dimensions (length × breadth), so enlarging each dimension by k enlarges the area by k × k = k². Do not multiply by k only.",
            },
        ]

        sample_answer = (
            f"1. $\\frac{{\\text{{Area of }} P'}}{{\\text{{Area of }} P}} = k^2$\n"
            f"2. $\\text{{Area of }} P' = k^2 \\times \\text{{Area of }} P$\n"
            f"   $\\text{{Area of }} P' = ({k})^2 \\times {orig_area}\\text{{ cm}}^2$\n"
            f"   $\\text{{Area of }} P' = {k**2} \\times {orig_area} = {new_area}\\text{{ cm}}^2$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "function_graph",
            "domain": [0, 10],
            "range": [0, 10],
            "caption": f"Enlargement by scale factor k = {k} (Area multiplies by {k**2})",
        }

        correct_ans = f"{new_area} cm²"
        subskill_id = "enlargement_area_factor"
        reason_code = "area scale factor k^2"
        marks = 3

    q = {
        "id": qid,
        "subject": "Mathematics",
        "grade": 9,
        "topic": TOPIC,
        "subskill": subskill_id,
        "learning_objective_id": LO,
        "mode": mode,
        "difficulty": difficulty,
        "question_type": "free_response",
        "answer_mode": "free_response",
        "prompt": question_text,
        "question": question_text,
        "prompt_latex": question_text,
        "answer_latex": correct_ans,
        "correct_answer": correct_ans,
        "sample_answer": sample_answer,
        "worked_solution": sample_answer,
        "canonical_solution": sample_answer,
        "marking_schema": [
            {"criterion": f"Correct transformation rule [{reason_code}]", "marks": 1},
            {"criterion": f"Correct calculation and coordinates/value {correct_ans}", "marks": marks - 1},
        ],
        "marks": marks,
        "hints": hints,
        "hint_sections": {
            "concept": hints[0],
            "rules": hints[1],
            "step_by_step": hints[2],
        },
        "misconception_tags": [m["tag"] for m in error_tax],
        "diagnostic_tags": [f"diag_{subskill_id}"],
        "keywords": ["transformation", "translation", "reflection", "rotation", "enlargement", "scale factor", "Cartesian plane"],
        "term": 3,
        "caps_weight_percent": 10.0,
        "suggested_duration_mins": 5,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Solve Cartesian transformation problem",
            "steps": steps,
        },
        "metadata": {
            "diagram_spec": diagram_spec,
            "answer_value": correct_ans,
            "reason_code": reason_code,
        },
    }
    return q


def generate(seed: Optional[int] = None, count: int = 1, **kwargs: Any) -> Dict[str, Any]:
    r = rng(seed)
    questions = []
    for _ in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        questions.append(generate_grade9_transformation_geometry_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
