"""Grade 9 Mathematics - Geometry of 2D Shapes Archetypes 01 to 25.
Grounded strictly in curriculum_docs_auto/Mathematics_Gr9/Term 2/04. Geometry of 2D shapes.md:
Classifying triangles, interior angle sum of triangles (180°), exterior angle theorem,
isosceles and equilateral triangle properties, right-angled triangles, triangle inequality,
4 congruency conditions (SSS, SAS, AAS, RHS), 2-column formal proofs [Statement | Reason],
and deducing unknown sides/angles from corresponding congruent parts.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from .geometry_2d_shapes_svg import (
    draw_congruent_triangles_pair_svg,
    draw_triangle_angles_svg,
    draw_triangle_exterior_angle_svg,
)


# ----------------------------------------------------------------------
# 01. Classify Triangle by Sides and Angles
# ----------------------------------------------------------------------
def arch_01_classify_triangle_by_sides_and_angles(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("scalene acute-angled", [45, 65, 70], [6, 8, 9], "All sides are unequal, and all three angles are acute (< 90°)."),
        ("isosceles acute-angled", [50, 65, 65], [7, 8, 8], "Two sides are equal in length, and all angles are acute."),
        ("equilateral", [60, 60, 60], [6, 6, 6], "All three sides are equal, and all three angles equal 60°."),
        ("right-angled scalene", [90, 35, 55], [6, 8, 10], "One angle is 90° and all three side lengths are unequal."),
        ("isosceles right-angled", [90, 45, 45], [5, 5, 7], "One angle is 90° and two sides are equal in length."),
        ("obtuse-angled scalene", [110, 30, 40], [5, 7, 10], "One angle is obtuse (> 90°) and all sides are unequal."),
        ("isosceles obtuse-angled", [120, 30, 30], [6, 6, 10], "One angle is obtuse (> 90°) and two sides are equal in length."),
    ]
    t_name, angs, sides, reason = rng.choice(types)
    rng.shuffle(angs)

    prompt = (
        f"A triangle has interior angles measuring \\({angs[0]}^\\circ\\), \\({angs[1]}^\\circ\\), and \\({angs[2]}^\\circ\\), "
        f"and side lengths of {sides[0]} cm, {sides[1]} cm, and {sides[2]} cm. "
        f"Classify this triangle according to both its side lengths and its angles."
    )
    sol = (
        f"**Step 1: Classify by sides.**\n"
        f"Side lengths: {sides[0]} cm, {sides[1]} cm, {sides[2]} cm.\n\n"
        f"**Step 2: Classify by angles.**\n"
        f"Angles: \\({angs[0]}^\\circ\\), \\({angs[1]}^\\circ\\), \\({angs[2]}^\\circ\\).\n\n"
        f"**Conclusion:**\n"
        f"The triangle is an **{t_name} triangle**. Reason: {reason}"
    )
    return {
        "id": f"g9_geom_class_tri_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": t_name,
        "expected_answer": t_name,
        "sample_answer": t_name,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Classify side type (scalene/isosceles/equilateral)", "marks": 1},
            {"desc": "Classify angle type (acute/right/obtuse)", "marks": 1},
        ],
        "hints": [
            "Check how many sides are equal: 3 equal = equilateral, 2 equal = isosceles, 0 equal = scalene.",
            "Check the largest angle: 90° = right-angled, > 90° = obtuse-angled, all < 90° = acute-angled.",
            f"Classification: {t_name}.",
        ],
    }


# ----------------------------------------------------------------------
# 02. Triangle Interior Angle Sum Basic (with SVG diagram)
# ----------------------------------------------------------------------
def arch_02_triangle_interior_angle_sum_basic(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(35, 75)
    b = rng.randint(35, 180 - a - 25)
    c = 180 - (a + b)

    seed_val = rng.randint(1000, 999999)
    svg = draw_triangle_angles_svg(
        angles=(c, a, b),
        labels=("A", "B", "C"),
        angle_texts=(f"{a}^\\circ", f"{b}^\\circ", "x"),
        seed=seed_val,
    )

    prompt = (
        f"In \\(\\triangle ABC\\) shown in the diagram below, \\(\\hat{{A}} = {a}^\\circ\\) and \\(\\hat{{B}} = {b}^\\circ\\). "
        f"Calculate the size of \\(\\hat{{C}}\\) (marked as \\(x\\)). Provide the geometric theorem reason."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ \\hat{{A}} + \\hat{{B}} + \\hat{{C}} = 180^\\circ \\quad [\\text{{sum of }}\\angle\\text{{s in }}\\triangle] \\]\n"
        f"\\[ {a}^\\circ + {b}^\\circ + x = 180^\\circ \\]\n"
        f"\\[ {a + b}^\\circ + x = 180^\\circ \\]\n"
        f"\\[ x = 180^\\circ - {a + b}^\\circ = {c}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_tri_sum_bas_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{c}°",
        "expected_answer": f"{c}°",
        "sample_answer": f"{c}° [sum of ∠s in △]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State theorem: sum of ∠s in △ = 180°", "marks": 1},
            {"desc": f"Calculate x = {c}°", "marks": 1},
        ],
        "hints": [
            "The sum of interior angles in any triangle is always 180°.",
            f"Add the two known angles: {a}° + {b}° = {a + b}°.",
            f"Subtract from 180° to find x: 180° - {a + b}° = {c}°.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 03. Triangle Interior Angles: Algebraic Linear
# ----------------------------------------------------------------------
def arch_03_triangle_interior_angles_algebraic_linear(rng: random.Random) -> Dict[str, Any]:
    # Angles: k1 x, k2 x, k3 x where sum of k_i = 9, 10, 12, 15, 18, 20
    k_combos = [
        (2, 3, 4),   # sum = 9 -> x = 20
        (1, 2, 3),   # sum = 6 -> x = 30
        (2, 3, 5),   # sum = 10 -> x = 18
        (3, 4, 5),   # sum = 12 -> x = 15
        (4, 5, 9),   # sum = 18 -> x = 10
        (1, 4, 5),   # sum = 10 -> x = 18
    ]
    k1, k2, k3 = rng.choice(k_combos)
    k_sum = k1 + k2 + k3
    x_val = 180 // k_sum

    ang1 = k1 * x_val
    ang2 = k2 * x_val
    ang3 = k3 * x_val
    target = rng.choice(["smallest", "largest"])
    target_val = min(ang1, ang2, ang3) if target == "smallest" else max(ang1, ang2, ang3)

    prompt = (
        f"The interior angles of a triangle are represented algebraically as "
        f"\\({k1}x\\), \\({k2}x\\), and \\({k3}x\\). "
        f"Solve for \\(x\\) and hence calculate the size of the **{target}** angle in degrees."
    )
    sol = (
        f"**Step 1: Apply the sum of interior angles theorem.**\n"
        f"\\[ {k1}x + {k2}x + {k3}x = 180^\\circ \\quad [\\text{{sum of }}\\angle\\text{{s in }}\\triangle] \\]\n"
        f"\\[ {k_sum}x = 180^\\circ \\]\n"
        f"\\[ x = 180^\\circ \\div {k_sum} = {x_val}^\\circ \\]\n\n"
        f"**Step 2: Calculate the {target} angle.**\n"
        f"Angles are \\({ang1}^\\circ\\), \\({ang2}^\\circ\\), and \\({ang3}^\\circ\\).\n"
        f"The {target} angle is **{target_val}°**."
    )
    return {
        "id": f"g9_geom_tri_alg_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{target_val}°",
        "expected_answer": f"{target_val}°",
        "sample_answer": f"x = {x_val}°, {target} angle = {target_val}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Set up equation {k_sum}x = 180° with reason [sum of ∠s in △]", "marks": 1},
            {"desc": f"Solve x = {x_val}°", "marks": 1},
            {"desc": f"Calculate {target} angle = {target_val}°", "marks": 1},
        ],
        "hints": [
            f"Add all three algebraic angle terms: {k1}x + {k2}x + {k3}x = 180°.",
            f"Solve for x: {k_sum}x = 180°.",
            f"Substitute x to find the {target} angle ({target_val}°).",
        ],
    }


# ----------------------------------------------------------------------
# 04. Triangle Exterior Angle Theorem Numeric (with SVG diagram)
# ----------------------------------------------------------------------
def arch_04_triangle_exterior_angle_theorem_numeric(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(40, 75)
    b = rng.randint(35, 75)
    ext_angle = a + b

    seed_val = rng.randint(1000, 999999)
    svg = draw_triangle_exterior_angle_svg(
        int_a=f"{a}^\\circ",
        int_b=f"{b}^\\circ",
        ext_c="x",
        seed=seed_val,
    )

    prompt = (
        f"In \\(\\triangle ABC\\) shown in the diagram below, side \\(BC\\) is extended to \\(D\\). "
        f"Given that \\(\\hat{{A}} = {a}^\\circ\\) and \\(\\hat{{B}} = {b}^\\circ\\), "
        f"determine the size of the exterior angle \\(A\\hat{{C}}D\\) (marked as \\(x\\)). "
        f"State the full geometric theorem reason."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ A\\hat{{C}}D = \\hat{{A}} + \\hat{{B}} \\quad [\\text{{ext }}\\angle\\text{{ of }}\\triangle = \\text{{sum of opp int }}\\angle\\text{{s}}] \\]\n"
        f"\\[ x = {a}^\\circ + {b}^\\circ \\]\n"
        f"\\[ x = {ext_angle}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_ext_num_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ext_angle}°",
        "expected_answer": f"{ext_angle}°",
        "sample_answer": f"{ext_angle}° [ext ∠ of △]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "State theorem [ext ∠ of △]", "marks": 1},
            {"desc": f"Calculate x = {ext_angle}°", "marks": 1},
        ],
        "hints": [
            "The exterior angle of a triangle equals the sum of the two opposite interior angles.",
            f"Add angle A ({a}°) and angle B ({b}°).",
            f"Exterior angle x = {ext_angle}°.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 05. Triangle Exterior Angle Theorem: Algebraic
# ----------------------------------------------------------------------
def arch_05_triangle_exterior_angle_theorem_algebraic(rng: random.Random) -> Dict[str, Any]:
    # ext_angle = ax + b, opp_int1 = cx, opp_int2 = d
    # ax + b = cx + d => (a - c) x = d - b
    c = rng.randint(2, 4)
    x_val = rng.randint(12, 25)
    b_val = rng.randint(10, 30)
    a = c + rng.choice([1, 2])
    d_val = (a - c) * x_val + b_val

    ext_ang = a * x_val + b_val
    int1 = c * x_val

    prompt = (
        f"In \\(\\triangle ABC\\), side \\(BC\\) is produced to \\(D\\). "
        f"The exterior angle \\(A\\hat{{C}}D = ({a}x + {b_val})^\\circ\\), and the two opposite interior "
        f"angles are \\(\\hat{{A}} = {c}x^\\circ\\) and \\(\\hat{{B}} = {d_val}^\\circ\\). "
        f"Solve for \\(x\\) and hence calculate the size of the exterior angle \\(A\\hat{{C}}D\\)."
    )
    sol = (
        f"**Step 1: Set up the exterior angle equation.**\n"
        f"\\[ A\\hat{{C}}D = \\hat{{A}} + \\hat{{B}} \\quad [\\text{{ext }}\\angle\\text{{ of }}\\triangle] \\]\n"
        f"\\[ {a}x + {b_val} = {c}x + {d_val} \\]\n\n"
        f"**Step 2: Solve for x.**\n"
        f"\\[ {a}x - {c}x = {d_val} - {b_val} \\]\n"
        f"\\[ {a - c}x = {d_val - b_val} \\]\n"
        f"\\[ x = {x_val} \\]\n\n"
        f"**Step 3: Calculate exterior angle size.**\n"
        f"\\[ A\\hat{{C}}D = {a}({x_val}) + {b_val} = {ext_ang}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_ext_alg_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{ext_ang}°",
        "expected_answer": f"{ext_ang}°",
        "sample_answer": f"x = {x_val}, A^CD = {ext_ang}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Equate exterior angle to sum of interior angles [ext ∠ of △]", "marks": 1},
            {"desc": f"Solve linear equation for x = {x_val}", "marks": 1},
            {"desc": f"Evaluate exterior angle = {ext_ang}°", "marks": 1},
        ],
        "hints": [
            f"Use the theorem: exterior angle = sum of opposite interior angles ({a}x + {b_val} = {c}x + {d_val}).",
            f"Group like terms to solve for x ({a - c}x = {d_val - b_val}).",
            f"Substitute x = {x_val} into {a}x + {b_val} to get {ext_ang}°.",
        ],
    }


# ----------------------------------------------------------------------
# 06. Isosceles Triangle Base Angles Calculation (with SVG diagram)
# ----------------------------------------------------------------------
def arch_06_isosceles_triangle_base_angles_calculation(rng: random.Random) -> Dict[str, Any]:
    vert = rng.choice([36, 40, 48, 50, 52, 64, 70, 80, 96, 100])
    base = (180 - vert) // 2

    seed_val = rng.randint(1000, 999999)
    svg = draw_triangle_angles_svg(
        angles=(vert, base, base),
        labels=("A", "B", "C"),
        angle_texts=(f"{vert}^\\circ", "x", "x"),
        side_ticks=(True, False, True),
        seed=seed_val,
    )

    prompt = (
        f"In \\(\\triangle ABC\\) shown in the diagram below, \\(AB = AC\\) and vertex angle \\(\\hat{{A}} = {vert}^\\circ\\). "
        f"Calculate the size of base angle \\(\\hat{{B}}\\) (marked as \\(x\\)). State all geometric reasons."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ \\hat{{B}} = \\hat{{C}} = x \\quad [\\angle\\text{{s opp equal sides, }} AB = AC] \\]\n"
        f"\\[ \\hat{{A}} + \\hat{{B}} + \\hat{{C}} = 180^\\circ \\quad [\\text{{sum of }}\\angle\\text{{s in }}\\triangle] \\]\n"
        f"\\[ {vert}^\\circ + 2x = 180^\\circ \\]\n"
        f"\\[ 2x = 180^\\circ - {vert}^\\circ = {180 - vert}^\\circ \\]\n"
        f"\\[ x = {base}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_iso_base_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{base}°",
        "expected_answer": f"{base}°",
        "sample_answer": f"{base}° [∠s opp equal sides; sum of ∠s in △]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "State ∠B = ∠C [∠s opp equal sides]", "marks": 1},
            {"desc": "Apply sum of angles in triangle = 180°", "marks": 1},
            {"desc": f"Calculate x = {base}°", "marks": 1},
        ],
        "hints": [
            "Angles opposite equal sides in an isosceles triangle are equal.",
            f"Subtract vertex angle {vert}° from 180°.",
            f"Divide remainder by 2: {180 - vert}° ÷ 2 = {base}°.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 07. Isosceles Triangle Vertex Angle from Base
# ----------------------------------------------------------------------
def arch_07_isosceles_triangle_vertex_angle_from_base(rng: random.Random) -> Dict[str, Any]:
    base = rng.randint(35, 78)
    vert = 180 - 2 * base

    prompt = (
        f"In \\(\\triangle PQR\\), \\(PQ = PR\\) and base angle \\(\\hat{{Q}} = {base}^\\circ\\). "
        f"Calculate the size of the vertex angle \\(\\hat{{P}}\\). State the geometric reasons."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ \\hat{{R}} = \\hat{{Q}} = {base}^\\circ \\quad [\\angle\\text{{s opp equal sides, }} PQ = PR] \\]\n"
        f"\\[ \\hat{{P}} + \\hat{{Q}} + \\hat{{R}} = 180^\\circ \\quad [\\text{{sum of }}\\angle\\text{{s in }}\\triangle] \\]\n"
        f"\\[ \\hat{{P}} = 180^\\circ - ({base}^\\circ + {base}^\\circ) = 180^\\circ - {2 * base}^\\circ = {vert}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_iso_vert_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{vert}°",
        "expected_answer": f"{vert}°",
        "sample_answer": f"{vert}° [∠s opp equal sides; sum of ∠s in △]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State ∠R = {base}° [∠s opp equal sides]", "marks": 1},
            {"desc": f"Calculate vertex angle = {vert}°", "marks": 1},
        ],
        "hints": [
            f"The two base angles are equal: angle Q = angle R = {base}°.",
            f"Multiply base angle by 2: {2 * base}°.",
            f"Subtract from 180° to find vertex angle: {vert}°.",
        ],
    }


# ----------------------------------------------------------------------
# 08. Isosceles Triangle with Exterior Angle
# ----------------------------------------------------------------------
def arch_08_isosceles_triangle_with_exterior_angle(rng: random.Random) -> Dict[str, Any]:
    # Ext angle at base C is 180 - base
    base = rng.randint(40, 75)
    ext_c = 180 - base
    vert = 180 - 2 * base

    prompt = (
        f"In \\(\\triangle ABC\\), \\(AB = AC\\). Side \\(BC\\) is extended past \\(C\\) to point \\(D\\). "
        f"If the exterior angle \\(A\\hat{{C}}D = {ext_c}^\\circ\\), "
        f"calculate the size of the vertex angle \\(\\hat{{A}}\\)."
    )
    sol = (
        f"**Step 1: Find base angle \\(A\\hat{{C}}B\\).**\n"
        f"\\[ A\\hat{{C}}B = 180^\\circ - {ext_c}^\\circ = {base}^\\circ \\quad [\\angle\\text{{s on a straight line}}] \\]\n\n"
        f"**Step 2: Find base angle \\(\\hat{{B}}\\).**\n"
        f"\\[ \\hat{{B}} = A\\hat{{C}}B = {base}^\\circ \\quad [\\angle\\text{{s opp equal sides, }} AB = AC] \\]\n\n"
        f"**Step 3: Calculate vertex angle \\(\\hat{{A}}\\).**\n"
        f"\\[ \\hat{{A}} = 180^\\circ - ({base}^\\circ + {base}^\\circ) = {vert}^\\circ \\quad [\\text{{sum of }}\\angle\\text{{s in }}\\triangle] \\]"
    )
    return {
        "id": f"g9_geom_iso_ext_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{vert}°",
        "expected_answer": f"{vert}°",
        "sample_answer": f"{vert}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate base angle ACB = 180° - {ext_c}° = {base}° [∠s on straight line]", "marks": 1},
            {"desc": f"Recognize ∠B = {base}° [∠s opp equal sides]", "marks": 1},
            {"desc": f"Calculate vertex angle A = {vert}° [sum of ∠s in △]", "marks": 1},
        ],
        "hints": [
            f"Angles on a straight line add to 180°, so interior base angle = 180° - {ext_c}° = {base}°.",
            f"Because AB = AC, both base angles are {base}°.",
            f"Calculate vertex angle = 180° - 2({base}°) = {vert}°.",
        ],
    }


# ----------------------------------------------------------------------
# 09. Equilateral Triangle Properties and Algebra
# ----------------------------------------------------------------------
def arch_09_equilateral_triangle_properties_and_algebra(rng: random.Random) -> Dict[str, Any]:
    # Side 1 = 3x - a, Side 2 = x + b => 2x = a + b
    x_val = rng.randint(4, 12)
    a_val = rng.randint(2, 8)
    b_val = 2 * x_val - a_val

    side_len = x_val + b_val

    prompt = (
        f"\\(\\triangle ABC\\) is an equilateral triangle. Side \\(AB = 3x - {a_val}\\text{{ cm}}\\) "
        f"and side \\(BC = x + {b_val}\\text{{ cm}}\\). "
        f"Solve for \\(x\\) and hence determine the perimeter of \\(\\triangle ABC\\)."
    )
    sol = (
        f"**Step 1: Apply equilateral triangle side equality.**\n"
        f"\\[ AB = BC \\quad [\\text{{all sides equal in equilat }}\\triangle] \\]\n"
        f"\\[ 3x - {a_val} = x + {b_val} \\]\n"
        f"\\[ 2x = {a_val + b_val} \\]\n"
        f"\\[ x = {x_val} \\]\n\n"
        f"**Step 2: Calculate side length.**\n"
        f"\\[ \\text{{Side length}} = {x_val} + {b_val} = {side_len}\\text{{ cm}} \\]\n\n"
        f"**Step 3: Calculate perimeter.**\n"
        f"\\[ \\text{{Perimeter}} = 3 \\times {side_len}\\text{{ cm}} = {3 * side_len}\\text{{ cm}} \\]"
    )
    return {
        "id": f"g9_geom_equilat_alg_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{3 * side_len} cm",
        "expected_answer": f"{3 * side_len} cm",
        "sample_answer": f"x = {x_val}, Perimeter = {3 * side_len} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Equate 3x - {a_val} = x + {b_val} [equilat △]", "marks": 1},
            {"desc": f"Solve for x = {x_val}", "marks": 1},
            {"desc": f"Calculate perimeter = {3 * side_len} cm", "marks": 1},
        ],
        "hints": [
            "All three sides of an equilateral triangle have equal length.",
            f"Solve 3x - {a_val} = x + {b_val} to find x.",
            f"Perimeter is 3 times the side length ({3 * side_len} cm).",
        ],
    }


# ----------------------------------------------------------------------
# 10. Right-Angled Triangle Acute Angles Complementary
# ----------------------------------------------------------------------
def arch_10_right_angled_triangle_acute_angles_complementary(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (1, 2, 30),
        (1, 4, 18),
        (2, 3, 18),
        (1, 5, 15),
        (1, 8, 10),
        (3, 7, 9),
        (4, 5, 10),
    ]
    m1, m2, x_val = rng.choice(configs)
    a1 = m1 * x_val
    a2 = m2 * x_val

    prompt = (
        f"In a right-angled triangle, one acute angle is \\({m1}x^\\circ\\) and the second acute angle "
        f"is \\({m2}x^\\circ\\). "
        f"Solve for \\(x\\) and determine the measure of the larger acute angle."
    )
    sol = (
        f"**Step 1: Set up equation using complementary acute angles.**\n"
        f"In a right-angled triangle, the acute angles sum to \\(90^\\circ\\):\n"
        f"\\[ {m1}x + {m2}x = 90^\\circ \\]\n"
        f"\\[ {m1 + m2}x = 90^\\circ \\]\n"
        f"\\[ x = 90^\\circ \\div {m1 + m2} = {x_val}^\\circ \\]\n\n"
        f"**Step 2: Calculate the larger acute angle.**\n"
        f"\\[ \\text{{Larger acute angle}} = {m2}({x_val}^\\circ) = {a2}^\\circ \\]"
    )
    return {
        "id": f"g9_geom_rt_comp_{rng.randint(100000, 999999)}",
        "question_type": "geometry_angle",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{a2}°",
        "expected_answer": f"{a2}°",
        "sample_answer": f"x = {x_val}°, larger angle = {a2}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Solve {m1+m2}x = 90° for x = {x_val}°", "marks": 1},
            {"desc": f"Calculate larger angle = {a2}°", "marks": 1},
        ],
        "hints": [
            "In any right-angled triangle, the two acute angles sum to 90°.",
            f"Add {m1}x + {m2}x = 90°.",
            f"Substitute x = {x_val}° to find the larger angle ({a2}°).",
        ],
    }


# ----------------------------------------------------------------------
# 11. Triangle Inequality Theorem
# ----------------------------------------------------------------------
def arch_11_triangle_inequality_theorem(rng: random.Random) -> Dict[str, Any]:
    valid = rng.choice([True, False])
    if valid:
        a = rng.randint(4, 9)
        b = rng.randint(5, 10)
        c = rng.randint(max(a, b) - min(a, b) + 1, a + b - 1)
        ans = "Yes"
        sol_text = f"Since {min(a,b)} + {sorted([a,b,c])[1]} = {min(a,b)+sorted([a,b,c])[1]} > {max(a,b,c)}, a triangle can be formed."
    else:
        a = rng.randint(3, 6)
        b = rng.randint(3, 6)
        c = a + b + rng.randint(0, 4)
        ans = "No"
        sol_text = f"Since {a} + {b} = {a + b} \\le {c}, the two shorter sides cannot meet, so no triangle can be formed."

    prompt = (
        f"Determine whether a triangle can be constructed with side lengths measuring "
        f"{a} cm, {b} cm, and {c} cm. Answer 'Yes' or 'No' and provide the mathematical reason based on the Triangle Inequality Theorem."
    )
    sol = (
        f"**Triangle Inequality Theorem:**\n"
        f"The sum of the lengths of any two sides of a triangle must be strictly greater than the third side:\n"
        f"\\[ a + b > c \\]\n\n"
        f"**Evaluation:**\n"
        f"{sol_text}\n"
        f"**Answer:** **{ans}**"
    )
    return {
        "id": f"g9_geom_tri_ineq_{rng.randint(100000, 999999)}",
        "question_type": "boolean_choice",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": f"{ans}. {sol_text}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State correct decision ({ans})", "marks": 1},
            {"desc": "Justify with Triangle Inequality sum of two shorter sides vs longest side", "marks": 1},
        ],
        "hints": [
            "Check if the sum of the two shorter sides is strictly greater than the longest side.",
            f"Add {min(a, b)} and {sorted([a,b,c])[1]} and compare to {max(a,b,c)}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 12. Congruence: Identify Condition SSS (with SVG diagram)
# ----------------------------------------------------------------------
def arch_12_congruence_identify_condition_sss(rng: random.Random) -> Dict[str, Any]:
    t1_labels, t2_labels = rng.choice([
        (("A", "B", "C"), ("D", "E", "F")),
        (("P", "Q", "R"), ("S", "T", "U")),
        (("K", "L", "M"), ("X", "Y", "Z")),
        (("G", "H", "I"), ("J", "K", "L")),
    ])
    t1_name = "".join(t1_labels)
    t2_name = "".join(t2_labels)
    seed_val = rng.randint(1000, 999999)
    svg = draw_congruent_triangles_pair_svg(
        t1_labels=t1_labels,
        t2_labels=t2_labels,
        condition="SSS",
        seed=seed_val,
    )

    prompt = (
        f"Examine the two triangles \\(\\triangle {t1_name}\\) and \\(\\triangle {t2_name}\\) shown in the diagram below. "
        f"Identify which of the four conditions of congruency proves that \\(\\triangle {t1_name} \\equiv \\triangle {t2_name}\\). "
        f"(Choose from: SSS, SAS, AAS, or RHS)."
    )
    sol = (
        f"**Analysis of Markings:**\n"
        f"1. \\({t1_labels[0]}{t1_labels[1]} = {t2_labels[0]}{t2_labels[1]}\\) (single tick mark)\n"
        f"2. \\({t1_labels[1]}{t1_labels[2]} = {t2_labels[1]}{t2_labels[2]}\\) (double tick mark)\n"
        f"3. \\({t1_labels[0]}{t1_labels[2]} = {t2_labels[0]}{t2_labels[2]}\\) (triple tick mark)\n\n"
        f"All three pairs of corresponding sides are equal.\n"
        f"Therefore, \\(\\triangle {t1_name} \\equiv \\triangle {t2_name}\\) **[SSS]** (Side-Side-Side)."
    )
    return {
        "id": f"g9_geom_cong_sss_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "SSS",
        "expected_answer": "SSS",
        "sample_answer": "SSS (Side-Side-Side)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify 3 pairs of equal sides", "marks": 1},
            {"desc": "State condition as SSS", "marks": 1},
        ],
        "hints": [
            "Look at the tick marks on the sides of both triangles.",
            "All three pairs of sides have matching equality ticks.",
            "The correct condition is SSS.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 13. Congruence: Identify Condition SAS (with SVG diagram)
# ----------------------------------------------------------------------
def arch_13_congruence_identify_condition_sas(rng: random.Random) -> Dict[str, Any]:
    t1_labels, t2_labels = rng.choice([
        (("A", "B", "C"), ("D", "E", "F")),
        (("P", "Q", "R"), ("S", "T", "U")),
        (("K", "L", "M"), ("X", "Y", "Z")),
        (("G", "H", "I"), ("J", "K", "L")),
    ])
    t1_name = "".join(t1_labels)
    t2_name = "".join(t2_labels)
    seed_val = rng.randint(1000, 999999)
    svg = draw_congruent_triangles_pair_svg(
        t1_labels=t1_labels,
        t2_labels=t2_labels,
        condition="SAS",
        seed=seed_val,
    )

    prompt = (
        f"Examine \\(\\triangle {t1_name}\\) and \\(\\triangle {t2_name}\\) in the diagram below. "
        f"Which of the four conditions of congruency proves that \\(\\triangle {t1_name} \\equiv \\triangle {t2_name}\\)? "
        f"(Choose from: SSS, SAS, AAS, or RHS)."
    )
    sol = (
        f"**Analysis of Markings:**\n"
        f"1. \\({t1_labels[0]}{t1_labels[1]} = {t2_labels[0]}{t2_labels[1]}\\) (side)\n"
        f"2. \\(\\hat{{{t1_labels[1]}}} = \\hat{{{t2_labels[1]}}}\\) (included angle)\n"
        f"3. \\({t1_labels[1]}{t1_labels[2]} = {t2_labels[1]}{t2_labels[2]}\\) (side)\n\n"
        f"Two pairs of sides and the **included angle** (the angle between the two sides) are equal.\n"
        f"Therefore, \\(\\triangle {t1_name} \\equiv \\triangle {t2_name}\\) **[SAS]** (Side-Angle-Side)."
    )
    return {
        "id": f"g9_geom_cong_sas_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "SAS",
        "expected_answer": "SAS",
        "sample_answer": "SAS (Side-Angle-Side)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify two sides and the included angle", "marks": 1},
            {"desc": "State condition as SAS", "marks": 1},
        ],
        "hints": [
            "Check which angle is marked: it is directly between the two marked sides.",
            "Two sides and the included angle prove congruency.",
            "The condition is SAS.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 14. Congruence: Identify Condition AAS (with SVG diagram)
# ----------------------------------------------------------------------
def arch_14_congruence_identify_condition_aas(rng: random.Random) -> Dict[str, Any]:
    t1_labels, t2_labels = rng.choice([
        (("A", "B", "C"), ("D", "E", "F")),
        (("P", "Q", "R"), ("S", "T", "U")),
        (("K", "L", "M"), ("X", "Y", "Z")),
        (("G", "H", "I"), ("J", "K", "L")),
    ])
    t1_name = "".join(t1_labels)
    t2_name = "".join(t2_labels)
    seed_val = rng.randint(1000, 999999)
    svg = draw_congruent_triangles_pair_svg(
        t1_labels=t1_labels,
        t2_labels=t2_labels,
        condition="AAS",
        seed=seed_val,
    )

    prompt = (
        f"Examine \\(\\triangle {t1_name}\\) and \\(\\triangle {t2_name}\\) in the diagram below. "
        f"State the condition of congruency that proves \\(\\triangle {t1_name} \\equiv \\triangle {t2_name}\\). "
        f"(Choose from: SSS, SAS, AAS, or RHS)."
    )
    sol = (
        f"**Analysis of Markings:**\n"
        f"1. \\(\\hat{{{t1_labels[1]}}} = \\hat{{{t2_labels[1]}}}\\) (angle)\n"
        f"2. \\(\\hat{{{t1_labels[2]}}} = \\hat{{{t2_labels[2]}}}\\) (angle)\n"
        f"3. \\({t1_labels[0]}{t1_labels[1]} = {t2_labels[0]}{t2_labels[1]}\\) (corresponding side)\n\n"
        f"Two pairs of angles and a corresponding pair of sides are equal.\n"
        f"Therefore, \\(\\triangle {t1_name} \\equiv \\triangle {t2_name}\\) **[AAS]** (Angle-Angle-Side / SAA)."
    )
    return {
        "id": f"g9_geom_cong_aas_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "AAS",
        "expected_answer": "AAS",
        "sample_answer": "AAS (Angle-Angle-Side)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify two pairs of equal angles and a corresponding side", "marks": 1},
            {"desc": "State condition as AAS (or SAA)", "marks": 1},
        ],
        "hints": [
            "Two angles and one side are marked as equal.",
            "Since the side is not between the two angles, this is AAS.",
            "Condition is AAS.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 15. Congruence: Identify Condition RHS (with SVG diagram)
# ----------------------------------------------------------------------
def arch_15_congruence_identify_condition_rhs(rng: random.Random) -> Dict[str, Any]:
    t1_labels, t2_labels = rng.choice([
        (("A", "B", "C"), ("D", "E", "F")),
        (("P", "Q", "R"), ("S", "T", "U")),
        (("K", "L", "M"), ("X", "Y", "Z")),
        (("G", "H", "I"), ("J", "K", "L")),
    ])
    t1_name = "".join(t1_labels)
    t2_name = "".join(t2_labels)
    seed_val = rng.randint(1000, 999999)
    svg = draw_congruent_triangles_pair_svg(
        t1_labels=t1_labels,
        t2_labels=t2_labels,
        condition="RHS",
        seed=seed_val,
    )

    prompt = (
        f"Examine the two right-angled triangles in the diagram below. "
        f"Identify the specific condition of congruency that proves \\(\\triangle {t1_name} \\equiv \\triangle {t2_name}\\). "
        f"(Choose from: SSS, SAS, AAS, or RHS)."
    )
    sol = (
        f"**Analysis of Markings:**\n"
        f"1. \\(\\hat{{{t1_labels[1]}}} = \\hat{{{t2_labels[1]}}} = 90^\\circ\\) (Right angle)\n"
        f"2. \\({t1_labels[0]}{t1_labels[2]} = {t2_labels[0]}{t2_labels[2]}\\) (Hypotenuse, opposite the 90° angle)\n"
        f"3. \\({t1_labels[0]}{t1_labels[1]} = {t2_labels[0]}{t2_labels[1]}\\) (Side)\n\n"
        f"Right angle, hypotenuse, and one corresponding side are equal.\n"
        f"Therefore, \\(\\triangle {t1_name} \\equiv \\triangle {t2_name}\\) **[RHS]** (Right angle-Hypotenuse-Side)."
    )
    return {
        "id": f"g9_geom_cong_rhs_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "RHS",
        "expected_answer": "RHS",
        "sample_answer": "RHS (Right angle-Hypotenuse-Side)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify 90° angle, equal hypotenuses, and one pair of equal sides", "marks": 1},
            {"desc": "State condition as RHS", "marks": 1},
        ],
        "hints": [
            "Check for a 90° right angle in both triangles.",
            "Check whether the hypotenuses (sides opposite the 90° angles) are equal.",
            "Condition is RHS.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 16. Congruence: Non-Condition SSA Counterexample
# ----------------------------------------------------------------------
def arch_16_congruence_non_condition_ssa_counterexample(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(["Thabo", "Sipho", "Zola", "Buhle", "Lerato", "Kagiso", "Nomsa", "Andile"])
    s1 = rng.choice([6, 7, 8, 9, 10])
    s2 = rng.choice([4, 5])
    ang = rng.choice([30, 35, 40, 45])
    prompt = (
        f"{name} attempts to prove two triangles are congruent by showing that two pairs of sides "
        f"({s1} cm and {s2} cm) and one pair of non-included angles ({ang}°) are equal (SSA). "
        f"Explain why 'SSA' is not accepted as a general condition of congruency in Euclidean geometry."
    )
    sol = (
        f"**Geometric Explanation:**\n"
        f"The SSA (Side-Side-Angle) configuration does not guarantee congruency because it is ambiguous (the 'ambiguous case'). "
        f"Given two side lengths and a non-included angle ({ang}°), the second side ({s2} cm) can swing into two distinct positions, "
        f"forming either an acute-angled triangle or an obtuse-angled triangle with the exact same given dimensions. "
        f"The only exception is when the angle is a right angle, which is the RHS condition."
    )
    return {
        "id": f"g9_geom_ssa_counter_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "Ambiguous case: two different triangles can be formed with the same measurements unless the angle is 90° (RHS).",
        "expected_answer": "Ambiguous case: allows two different non-congruent triangles to be formed.",
        "sample_answer": "SSA allows two non-congruent triangles (ambiguous case).",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify ambiguous case (two different triangles can be constructed)", "marks": 1},
            {"desc": "Note angle must be included (SAS) or right angle (RHS) to guarantee unique triangle", "marks": 1},
        ],
        "hints": [
            "Think about whether the non-included side can swing in two different directions.",
            "This creates an acute or an obtuse triangle with the identical measurements.",
            "The configuration is known as the ambiguous case.",
        ],
    }


# ----------------------------------------------------------------------
# 17. Congruence Statement: Correct Vertex Correspondence
# ----------------------------------------------------------------------
def arch_17_congruence_statement_correct_vertex_correspondence(rng: random.Random) -> Dict[str, Any]:
    # Triangle ABC with matching vertices in DEF
    perms = [
        ("ABC", "DEF", "A corresponds to D, B to E, C to F"),
        ("ABC", "DFE", "A corresponds to D, B to F, C to E"),
        ("ABC", "EFD", "A corresponds to E, B to F, C to D"),
        ("ABC", "FDE", "A corresponds to F, B to D, C to E"),
    ]
    t1, t2, desc = rng.choice(perms)

    prompt = (
        f"In two congruent triangles, vertex \\({t1[0]}\\) corresponds to vertex \\({t2[0]}\\), "
        f"vertex \\({t1[1]}\\) corresponds to vertex \\({t2[1]}\\), and "
        f"vertex \\({t1[2]}\\) corresponds to vertex \\({t2[2]}\\). "
        f"Complete the formal congruency statement with vertices in the exact corresponding order:\n"
        f"\\[ \\triangle {t1} \\equiv \\triangle \\text{{???}} \\]"
    )
    sol = (
        f"**Vertex Matching:**\n"
        f"\\({t1[0]} \\leftrightarrow {t2[0]}\\)\n"
        f"\\({t1[1]} \\leftrightarrow {t2[1]}\\)\n"
        f"\\({t1[2]} \\leftrightarrow {t2[2]}\\)\n\n"
        f"**Congruency Statement:**\n"
        f"\\[ \\triangle {t1} \\equiv \\triangle {t2} \\]"
    )
    return {
        "id": f"g9_geom_cong_order_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": t2,
        "expected_answer": t2,
        "sample_answer": f"\\triangle {t2}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Match vertices in correct corresponding order", "marks": 1},
            {"desc": f"State triangle name as {t2}", "marks": 1},
        ],
        "hints": [
            "Order of vertices in a congruency statement must match corresponding equal angles.",
            f"First letter matches {t2[0]}, second matches {t2[1]}, third matches {t2[2]}.",
            f"The triangle name is {t2}.",
        ],
    }


# ----------------------------------------------------------------------
# 18. Congruence: Formal Proof SSS
# ----------------------------------------------------------------------
def arch_18_congruence_formal_proof_sss(rng: random.Random) -> Dict[str, Any]:
    s1 = rng.randint(5, 8)
    s2 = rng.randint(9, 12)
    s3 = rng.randint(13, 16)

    prompt = (
        f"In \\(\\triangle ABC\\) and \\(\\triangle DEF\\), "
        f"\\(AB = DE = {s1}\\text{{ cm}}\\), "
        f"\\(BC = EF = {s2}\\text{{ cm}}\\), and "
        f"\\(AC = DF = {s3}\\text{{ cm}}\\). "
        f"Write down the formal 2-column proof to prove that \\(\\triangle ABC \\equiv \\triangle DEF\\)."
    )
    sol = (
        f"**In \\(\\triangle ABC\\) and \\(\\triangle DEF\\):**\n"
        f"1. \\(AB = DE = {s1}\\text{{ cm}}\\) \\quad [given]\n"
        f"2. \\(BC = EF = {s2}\\text{{ cm}}\\) \\quad [given]\n"
        f"3. \\(AC = DF = {s3}\\text{{ cm}}\\) \\quad [given]\n"
        f"\\[ \\therefore \\triangle ABC \\equiv \\triangle DEF \\quad [\\text{{SSS}}] \\]"
    )
    return {
        "id": f"g9_geom_proof_sss_{rng.randint(100000, 999999)}",
        "question_type": "formal_proof",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "SSS",
        "expected_answer": "SSS",
        "sample_answer": sol,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": "State AB = DE [given]", "marks": 1},
            {"desc": "State BC = EF [given]", "marks": 1},
            {"desc": "State AC = DF [given]", "marks": 1},
            {"desc": "Conclusion: △ABC ≡ △DEF [SSS]", "marks": 1},
        ],
        "hints": [
            "List all three given pairs of equal sides with the reason [given].",
            "Conclude with the congruency symbol ≡ and the reason [SSS].",
            "Reason: SSS (Side-Side-Side).",
        ],
    }


# ----------------------------------------------------------------------
# 19. Congruence: Formal Proof SAS
# ----------------------------------------------------------------------
def arch_19_congruence_formal_proof_sas(rng: random.Random) -> Dict[str, Any]:
    ang = rng.randint(45, 80)
    s1 = rng.randint(5, 9)
    s2 = rng.randint(10, 15)

    prompt = (
        f"In \\(\\triangle KLM\\) and \\(\\triangle NPQ\\), "
        f"\\(KL = NP = {s1}\\text{{ cm}}\\), "
        f"\\(\\hat{{L}} = \\hat{{P}} = {ang}^\\circ\\), and "
        f"\\(LM = PQ = {s2}\\text{{ cm}}\\). "
        f"Set out the 3 statements and conclusion proving that \\(\\triangle KLM \\equiv \\triangle NPQ\\)."
    )
    sol = (
        f"**In \\(\\triangle KLM\\) and \\(\\triangle NPQ\\):**\n"
        f"1. \\(KL = NP = {s1}\\text{{ cm}}\\) \\quad [given]\n"
        f"2. \\(\\hat{{L}} = \\hat{{P}} = {ang}^\\circ\\) \\quad [given, included angle]\n"
        f"3. \\(LM = PQ = {s2}\\text{{ cm}}\\) \\quad [given]\n"
        f"\\[ \\therefore \\triangle KLM \\equiv \\triangle NPQ \\quad [\\text{{SAS}}] \\]"
    )
    return {
        "id": f"g9_geom_proof_sas_{rng.randint(100000, 999999)}",
        "question_type": "formal_proof",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "SAS",
        "expected_answer": "SAS",
        "sample_answer": sol,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": f"State KL = NP [given]", "marks": 1},
            {"desc": f"State ∠L = ∠P = {ang}° [given]", "marks": 1},
            {"desc": f"State LM = PQ [given]", "marks": 1},
            {"desc": "Conclusion: △KLM ≡ △NPQ [SAS]", "marks": 1},
        ],
        "hints": [
            "Two sides and the included angle are given.",
            "Write the three statements with reason [given].",
            "Conclude with reason [SAS].",
        ],
    }


# ----------------------------------------------------------------------
# 20. Congruence: Formal Proof AAS
# ----------------------------------------------------------------------
def arch_20_congruence_formal_proof_aas(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.randint(40, 65)
    a2 = rng.randint(45, 70)
    side_val = rng.randint(6, 12)

    prompt = (
        f"In \\(\\triangle ABC\\) and \\(\\triangle DEF\\), "
        f"\\(\\hat{{A}} = \\hat{{D}} = {a1}^\\circ\\), "
        f"\\(\\hat{{B}} = \\hat{{E}} = {a2}^\\circ\\), and "
        f"\\(BC = EF = {side_val}\\text{{ cm}}\\). "
        f"Provide the formal proof showing \\(\\triangle ABC \\equiv \\triangle DEF\\)."
    )
    sol = (
        f"**In \\(\\triangle ABC\\) and \\(\\triangle DEF\\):**\n"
        f"1. \\(\\hat{{A}} = \\hat{{D}} = {a1}^\\circ\\) \\quad [given]\n"
        f"2. \\(\\hat{{B}} = \\hat{{E}} = {a2}^\\circ\\) \\quad [given]\n"
        f"3. \\(BC = EF = {side_val}\\text{{ cm}}\\) \\quad [given]\n"
        f"\\[ \\therefore \\triangle ABC \\equiv \\triangle DEF \\quad [\\text{{AAS}}] \\]"
    )
    return {
        "id": f"g9_geom_proof_aas_{rng.randint(100000, 999999)}",
        "question_type": "formal_proof",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "AAS",
        "expected_answer": "AAS",
        "sample_answer": sol,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": f"State ∠A = ∠D [given]", "marks": 1},
            {"desc": f"State ∠B = ∠E [given]", "marks": 1},
            {"desc": f"State BC = EF [given]", "marks": 1},
            {"desc": "Conclusion: △ABC ≡ △DEF [AAS]", "marks": 1},
        ],
        "hints": [
            "List the two angle conditions and the side condition.",
            "Verify that the side corresponds in both triangles.",
            "Reason: AAS (Angle-Angle-Side).",
        ],
    }


# ----------------------------------------------------------------------
# 21. Congruence: Formal Proof RHS
# ----------------------------------------------------------------------
def arch_21_congruence_formal_proof_rhs(rng: random.Random) -> Dict[str, Any]:
    hyp = rng.choice([10, 13, 15, 17, 20])
    leg = rng.choice([6, 8, 12])
    while leg >= hyp:
        hyp = leg + 5

    prompt = (
        f"In \\(\\triangle ABC\\) and \\(\\triangle DEF\\), "
        f"\\(\\hat{{B}} = \\hat{{E}} = 90^\\circ\\), "
        f"\\(AC = DF = {hyp}\\text{{ cm}}\\) (hypotenuses), and "
        f"\\(AB = DE = {leg}\\text{{ cm}}\\). "
        f"Write down the formal 2-column proof to prove \\(\\triangle ABC \\equiv \\triangle DEF\\)."
    )
    sol = (
        f"**In \\(\\triangle ABC\\) and \\(\\triangle DEF\\):**\n"
        f"1. \\(\\hat{{B}} = \\hat{{E}} = 90^\\circ\\) \\quad [given, right angle]\n"
        f"2. \\(AC = DF = {hyp}\\text{{ cm}}\\) \\quad [given, hypotenuse]\n"
        f"3. \\(AB = DE = {leg}\\text{{ cm}}\\) \\quad [given, side]\n"
        f"\\[ \\therefore \\triangle ABC \\equiv \\triangle DEF \\quad [\\text{{RHS}}] \\]"
    )
    return {
        "id": f"g9_geom_proof_rhs_{rng.randint(100000, 999999)}",
        "question_type": "formal_proof",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "RHS",
        "expected_answer": "RHS",
        "sample_answer": sol,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": "State ∠B = ∠E = 90° [given]", "marks": 1},
            {"desc": f"State hypotenuse AC = DF = {hyp} cm [given]", "marks": 1},
            {"desc": f"State side AB = DE = {leg} cm [given]", "marks": 1},
            {"desc": "Conclusion: △ABC ≡ △DEF [RHS]", "marks": 1},
        ],
        "hints": [
            "State the right angle condition (R).",
            "State the equal hypotenuses (H).",
            "State the pair of equal sides (S) and conclude RHS.",
        ],
    }


# ----------------------------------------------------------------------
# 22. Congruence: Deduce Unknown Side after Proof
# ----------------------------------------------------------------------
def arch_22_congruence_deduce_unknown_side_after_proof(rng: random.Random) -> Dict[str, Any]:
    known_side = rng.randint(7, 18)
    a_coef = rng.choice([2, 3])
    b_const = rng.randint(2, 6)
    # a * x - b = known_side => x = (known_side + b) / a
    x_val = rng.randint(4, 10)
    known_side = a_coef * x_val - b_const

    prompt = (
        f"It is given that \\(\\triangle ABC \\equiv \\triangle DEF\\). "
        f"If \\(BC = {known_side}\\text{{ cm}}\\) and corresponding side \\(EF = {a_coef}x - {b_const}\\text{{ cm}}\\), "
        f"calculate the value of \\(x\\). State the geometric reason."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ EF = BC \\quad [\\text{{corr sides of congruent }}\\triangle\\text{{s, }} \\triangle ABC \\equiv \\triangle DEF] \\]\n"
        f"\\[ {a_coef}x - {b_const} = {known_side} \\]\n"
        f"\\[ {a_coef}x = {known_side + b_const} \\]\n"
        f"\\[ x = {x_val} \\]"
    )
    return {
        "id": f"g9_geom_deduce_side_{rng.randint(100000, 999999)}",
        "question_type": "numeric",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(x_val),
        "expected_answer": str(x_val),
        "sample_answer": f"x = {x_val} [corr sides of △ ≡ △]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Equate corresponding sides with reason [corr sides of ≡ △s]", "marks": 1},
            {"desc": f"Solve for x = {x_val}", "marks": 1},
        ],
        "hints": [
            "Corresponding sides of congruent triangles are equal in length.",
            f"Set up equation: {a_coef}x - {b_const} = {known_side}.",
            f"Solve for x: x = {x_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 23. Congruence: Deduce Unknown Angle after Proof
# ----------------------------------------------------------------------
def arch_23_congruence_deduce_unknown_angle_after_proof(rng: random.Random) -> Dict[str, Any]:
    ang_val = rng.randint(40, 75)
    coef = rng.choice([2, 3])
    const = rng.randint(5, 20)
    # coef * y + const = ang_val
    y_val = rng.randint(10, 25)
    ang_val = coef * y_val + const

    prompt = (
        f"It is established that \\(\\triangle PQR \\equiv \\triangle STU\\). "
        f"If \\(\\hat{{P}} = {ang_val}^\\circ\\) and corresponding angle \\(\\hat{{S}} = ({coef}y + {const})^\\circ\\), "
        f"calculate the numerical value of \\(y\\). State the geometric reason."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ \\hat{{S}} = \\hat{{P}} \\quad [\\text{{corr }}\\angle\\text{{s of congruent }}\\triangle\\text{{s, }} \\triangle PQR \\equiv \\triangle STU] \\]\n"
        f"\\[ {coef}y + {const} = {ang_val} \\]\n"
        f"\\[ {coef}y = {ang_val - const} \\]\n"
        f"\\[ y = {y_val} \\]"
    )
    return {
        "id": f"g9_geom_deduce_ang_{rng.randint(100000, 999999)}",
        "question_type": "numeric",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(y_val),
        "expected_answer": str(y_val),
        "sample_answer": f"y = {y_val} [corr ∠s of ≡ △s]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "Equate corresponding angles [corr ∠s of ≡ △s]", "marks": 1},
            {"desc": f"Solve for y = {y_val}", "marks": 1},
        ],
        "hints": [
            "Corresponding angles of congruent triangles are equal.",
            f"Set up: {coef}y + {const} = {ang_val}.",
            f"Solve for y = {y_val}.",
        ],
    }


# ----------------------------------------------------------------------
# 24. Overlapping Triangles: Common Side Congruence
# ----------------------------------------------------------------------
def arch_24_overlapping_triangles_common_side_congruence(rng: random.Random) -> Dict[str, Any]:
    quad_name, diag, s1, s2, s3, s4, t1, t2 = rng.choice([
        ("ABCD", "AC", "AB", "AD", "BC", "DC", "ABC", "ADC"),
        ("PQRS", "PR", "PQ", "PS", "QR", "SR", "PQR", "PSR"),
        ("KLMN", "KM", "KL", "KN", "LM", "NM", "KLM", "KNM"),
        ("WXYZ", "WY", "WX", "WZ", "XY", "ZY", "WXY", "WZY"),
    ])
    prompt = (
        f"Quadrilateral \\({quad_name}\\) has diagonal \\({diag}\\) drawn. "
        f"Given that \\({s1} = {s2}\\) and \\({s3} = {s4}\\), "
        f"identify the third pair of equal sides required to prove \\(\\triangle {t1} \\equiv \\triangle {t2}\\), "
        f"and state its geometric reason."
    )
    sol = (
        f"**Third Side Identification:**\n"
        f"\\[ {diag} = {diag} \\quad [\\text{{common side}}] \\]\n\n"
        f"**Congruency Conclusion:**\n"
        f"With \\({s1} = {s2}\\) [given], \\({s3} = {s4}\\) [given], and \\({diag} = {diag}\\) [common side],\n"
        f"\\[ \\triangle {t1} \\equiv \\triangle {t2} \\quad [\\text{{SSS}}] \\]"
    )
    return {
        "id": f"g9_geom_common_side_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{diag} = {diag} [common side]",
        "expected_answer": f"{diag} = {diag} [common side]",
        "sample_answer": f"{diag} is a common side; condition is SSS.",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify {diag} as the shared/common side ({diag} = {diag})", "marks": 1},
            {"desc": "State reason as 'common side'", "marks": 1},
        ],
        "hints": [
            "Notice which side is shared by both triangles.",
            f"The diagonal {diag} belongs to both triangle {t1} and triangle {t2}.",
            "The reason is 'common side' (reflexive property).",
        ],
    }


# ----------------------------------------------------------------------
# 25. Triangles with Vertically Opposite Angles Congruence
# ----------------------------------------------------------------------
def arch_25_triangles_with_vertically_opposite_angles_congruence(rng: random.Random) -> Dict[str, Any]:
    l1, l2, m, p1, p2, p3, p4 = rng.choice([
        ("AB", "CD", "M", "AM", "MB", "CM", "MD"),
        ("PQ", "RS", "O", "PO", "OQ", "RO", "OS"),
        ("EF", "GH", "K", "EK", "KF", "GK", "KH"),
        ("UV", "WX", "T", "UT", "TV", "WT", "TX"),
    ])
    t1 = f"{l1[0]}{m}{l2[0]}"
    t2 = f"{l1[1]}{m}{l2[1]}"
    ang1 = f"{l1[0]}\\hat{{{m}}}{l2[0]}"
    ang2 = f"{l1[1]}\\hat{{{m}}}{l2[1]}"

    prompt = (
        f"Line segments \\({l1}\\) and \\({l2}\\) intersect at point \\({m}\\), which is the midpoint of both segments "
        f"(so \\({p1} = {p2}\\) and \\({p3} = {p4}\\)). "
        f"Name the equal angle relationship at vertex \\({m}\\) that allows proving \\(\\triangle {t1} \\equiv \\triangle {t2}\\), "
        f"and state the resulting congruency condition."
    )
    sol = (
        f"**Angle Relationship:**\n"
        f"\\[ {ang1} = {ang2} \\quad [\\text{{vertically opposite }}\\angle\\text{{s}}] \\]\n\n"
        f"**Congruency Proof:**\n"
        f"1. \\({p1} = {p2}\\) [given, {m} is midpoint of {l1}]\n"
        f"2. \\({ang1} = {ang2}\\) [vert opp \\angle\\text{{s}}]\n"
        f"3. \\({p3} = {p4}\\) [given, {m} is midpoint of {l2}]\n"
        f"\\[ \\therefore \\triangle {t1} \\equiv \\triangle {t2} \\quad [\\text{{SAS}}] \\]"
    )
    return {
        "id": f"g9_geom_vert_opp_cong_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "SAS",
        "expected_answer": "SAS",
        "sample_answer": f"Vertically opposite angles at {m}; condition is SAS.",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify vertically opposite angles at {m}", "marks": 1},
            {"desc": "State congruency condition as SAS", "marks": 1},
        ],
        "hints": [
            "When two straight lines cross, vertically opposite angles are equal.",
            "The equal angle is included between the two pairs of equal segments.",
            "The condition is SAS.",
        ],
    }
