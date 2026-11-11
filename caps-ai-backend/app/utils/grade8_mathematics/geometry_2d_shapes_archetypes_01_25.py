"""Grade 8 Mathematics - Geometry of 2D Shapes Archetypes (01 to 25).
Covers:
  - Triangles: Interior angle sum (180 deg), exterior angle theorem, isosceles and equilateral triangles, right-angled triangles.
  - Quadrilaterals: Interior angle sum (360 deg), parallelogram, rectangle, rhombus, square, trapezium, kite properties.
Strictly zero-LLM, deterministic execution parameterized by random.Random.
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .geometry_2d_shapes_svg import draw_quadrilateral_svg, draw_triangle_svg


# ----------------------------------------------------------------------
# 01. Triangle Interior Angle Sum Numerical (WITH SVG)
# ----------------------------------------------------------------------
def arch_01_triangle_interior_angle_sum_numerical(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([35, 42, 48, 55, 62, 70])
    ang2 = rng.choice([44, 52, 58, 65, 73])
    ang3 = 180 - (ang1 + ang2)

    labels = {"A": f"{ang1}°", "B": f"{ang2}°", "C": "x"}
    svg = draw_triangle_svg(ang1, ang2, ang3, angle_labels=labels, seed=rng.randint(100, 999999))

    prompt = (
        f"In the given triangle \\(ABC\\), \\(\\hat{{A}} = {ang1}^\\circ\\) and \\(\\hat{{B}} = {ang2}^\\circ\\).\n\n"
        f"1. State the fundamental geometric theorem regarding the interior angles of a triangle.\n"
        f"2. Calculate the value of \\(x\\) (the size of \\(\\hat{{C}}\\)) with reasons."
    )
    sol = (
        f"**Step 1: Geometric Theorem**\n"
        f"The sum of the interior angles of a triangle is \\(180^\\circ\\) (\\(\\text{{sum of }}\\angle\\text{{s in }}\\triangle ABC\\)).\n\n"
        f"**Step 2: Calculate x**\n"
        f"\\[ \\hat{{A}} + \\hat{{B}} + \\hat{{C}} = 180^\\circ \\]\n"
        f"\\[ {ang1}^\\circ + {ang2}^\\circ + x = 180^\\circ \\]\n"
        f"\\[ {ang1 + ang2}^\\circ + x = 180^\\circ \\]\n"
        f"\\[ x = 180^\\circ - {ang1 + ang2}^\\circ = {ang3}^\\circ \\]"
    )
    ans = f"1. sum of angles in triangle = 180°; 2. x = {ang3}°"
    return {
        "id": f"g8_tri_sum_num_{rng.randint(100000, 999999)}",
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
        "subskill": "01_triangle_interior_angle_sum_numerical",
        "learning_objective_id": "math_g8_tri_sum_num",
        "hints": {
            "tier_1": "The three interior angles of any triangle always add up to 180°.",
            "tier_2": f"Add {ang1}° and {ang2}°, then subtract from 180°.",
            "tier_3": f"x = 180° - {ang1 + ang2}° = {ang3}°.",
        },
        "misconception_tags": ["subtracting_from_360_instead_of_180"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 02. Triangle Exterior Angle Theorem Numerical (WITH SVG)
# ----------------------------------------------------------------------
def arch_02_triangle_exterior_angle_theorem_numerical(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([32, 45, 54, 60, 68])
    ang2 = rng.choice([36, 48, 55, 62, 70])
    ext_ang = ang1 + ang2

    labels = {"A": f"{ang1}°", "B": f"{ang2}°"}
    svg = draw_triangle_svg(
        ang1,
        ang2,
        180 - ext_ang,
        angle_labels=labels,
        ext_angle=("C", "d"),
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In the given triangle \\(ABC\\), the side \\(BC\\) is extended to point \\(D\\) to form exterior angle \\(d = \\angle ACD\\).\n"
        f"The two opposite interior angles measure \\(\\hat{{A}} = {ang1}^\\circ\\) and \\(\\hat{{B}} = {ang2}^\\circ\\).\n\n"
        f"1. State the exterior angle theorem of a triangle.\n"
        f"2. Calculate the size of exterior angle \\(d\\) with reason."
    )
    sol = (
        f"**Step 1: Geometric Theorem**\n"
        f"The exterior angle of a triangle equals the sum of the two interior opposite angles "
        f"(\\(\\text{{ext. }}\\angle\\text{{ of }}\\triangle\\)).\n\n"
        f"**Step 2: Calculate d**\n"
        f"\\[ d = \\hat{{A}} + \\hat{{B}} \\quad (\\text{{ext. }}\\angle\\text{{ of }}\\triangle ABC) \\]\n"
        f"\\[ d = {ang1}^\\circ + {ang2}^\\circ = {ext_ang}^\\circ \\]"
    )
    ans = f"1. ext. angle equals sum of two opposite interior angles; 2. d = {ext_ang}°"
    return {
        "id": f"g8_tri_ext_num_{rng.randint(100000, 999999)}",
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
        "subskill": "02_triangle_exterior_angle_theorem_numerical",
        "learning_objective_id": "math_g8_tri_ext_num",
        "hints": {
            "tier_1": "Recall: Exterior angle of triangle = sum of interior opposite angles.",
            "tier_2": f"Add the two given opposite interior angles: {ang1}° + {ang2}°.",
            "tier_3": f"d = {ext_ang}°.",
        },
        "misconception_tags": ["subtracting_interior_from_180_instead_of_adding"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 03. Triangle Interior Angle Sum Algebraic Linear (WITH SVG)
# ----------------------------------------------------------------------
def arch_03_triangle_interior_angle_sum_algebraic_linear(rng: random.Random) -> Dict[str, Any]:
    c1, c2, c3 = rng.choice([(1, 2, 3), (2, 3, 4), (1, 3, 5), (2, 2, 5)])
    ans_x = 180 // (c1 + c2 + c3)
    k1 = c1 * ans_x
    k2 = c2 * ans_x
    k3 = 180 - (k1 + k2)

    labels = {"A": f"{c1}x", "B": f"{c2}x", "C": f"{c3}x"}
    svg = draw_triangle_svg(k1, k2, k3, angle_labels=labels, seed=rng.randint(100, 999999))

    prompt = (
        f"In the given triangle, the three interior angles are represented algebraically as "
        f"\\({c1}x\\), \\({c2}x\\), and \\({c3}x\\).\n\n"
        f"1. Set up an equation using the triangle angle sum theorem.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Calculate the size of the largest interior angle."
    )
    tot_c = c1 + c2 + c3
    max_c = max(c1, c2, c3)
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {c1}x + {c2}x + {c3}x = 180^\\circ \\quad (\\text{{sum of }}\\angle\\text{{s in }}\\triangle) \\]\n"
        f"\\[ {tot_c}x = 180 \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ x = \\frac{{180}}{{{tot_c}}} = {ans_x} \\]\n\n"
        f"**Step 3: Largest angle**\n"
        f"\\[ \\text{{Largest}} = {max_c} \\times {ans_x} = {max_c * ans_x}^\\circ \\]"
    )
    ans = f"1. {tot_c}x = 180; 2. x = {ans_x}; 3. {max_c * ans_x}°"
    return {
        "id": f"g8_tri_sum_alg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "03_triangle_interior_angle_sum_algebraic_linear",
        "learning_objective_id": "math_g8_tri_sum_alg",
        "hints": {
            "tier_1": "Add all three algebraic expressions and equate to 180°.",
            "tier_2": f"{tot_c}x = 180°.",
            "tier_3": f"x = {ans_x}, and the largest angle is {max_c * ans_x}°.",
        },
        "misconception_tags": ["forgetting_to_find_largest_angle"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 04. Triangle Exterior Angle Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_04_triangle_exterior_angle_algebraic(rng: random.Random) -> Dict[str, Any]:
    # ext = (a + b)x + (c + d)
    x_val = rng.choice([15, 20, 25, 30])
    a_coef, b_coef = rng.choice([(2, 1), (3, 2), (2, 2)])
    ext_coef = a_coef + b_coef
    k1 = rng.choice([5, 10, 15])
    k2 = rng.choice([5, 10, 15])
    ext_const = k1 + k2

    # Angles for SVG
    ang_a = a_coef * x_val + k1
    ang_b = b_coef * x_val + k2
    ext_ang = ang_a + ang_b

    labels = {"A": f"({a_coef}x + {k1}°)", "B": f"({b_coef}x + {k2}°)"}
    svg = draw_triangle_svg(
        ang_a,
        ang_b,
        180 - ext_ang,
        angle_labels=labels,
        ext_angle=("C", f"({ext_coef}x + {ext_const}°)"),
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In the given triangle, side \\(BC\\) is extended to \\(D\\).\n"
        f"The two interior opposite angles are \\(\\hat{{A}} = {a_coef}x + {k1}^\\circ\\) and \\(\\hat{{B}} = {b_coef}x + {k2}^\\circ\\).\n"
        f"The exterior angle \\(\\angle ACD = {ext_coef}x + {ext_const}^\\circ\\).\n\n"
        f"1. Write down an equation using the exterior angle theorem.\n"
        f"2. Verify that the equation is consistent and state the size of the exterior angle if \\(x = {x_val}\\)."
    )
    sol = (
        f"**Step 1: Equation**\n"
        f"\\[ ({a_coef}x + {k1}^\\circ) + ({b_coef}x + {k2}^\\circ) = {ext_coef}x + {ext_const}^\\circ \\quad (\\text{{ext. }}\\angle\\text{{ of }}\\triangle) \\]\n\n"
        f"**Step 2: Calculate size for x = {x_val}**\n"
        f"\\[ \\text{{Exterior angle}} = {ext_coef}({x_val}) + {ext_const} = {ext_coef * x_val + ext_const}^\\circ \\]"
    )
    ans = f"1. ({a_coef}x + {k1}) + ({b_coef}x + {k2}) = {ext_coef}x + {ext_const}; 2. {ext_ang}°"
    return {
        "id": f"g8_tri_ext_alg_{rng.randint(100000, 999999)}",
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
        "subskill": "04_triangle_exterior_angle_algebraic",
        "learning_objective_id": "math_g8_tri_ext_alg",
        "hints": {
            "tier_1": "Sum of two interior opposite angles equals the exterior angle.",
            "tier_2": f"Substitute x = {x_val} into {ext_coef}x + {ext_const}.",
            "tier_3": f"Exterior angle = {ext_ang}°.",
        },
        "misconception_tags": ["adding_adjacent_interior_instead_of_opposite"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 05. Isosceles Triangle Base Angles Given Apex (WITH SVG)
# ----------------------------------------------------------------------
def arch_05_isosceles_triangle_base_angles_given_apex(rng: random.Random) -> Dict[str, Any]:
    apex = rng.choice([36, 40, 50, 70, 80, 100])
    base = (180 - apex) // 2

    labels = {"A": f"{apex}°", "B": "x", "C": "x"}
    side_lbls = {"AB": "equal", "AC": "equal"}
    svg = draw_triangle_svg(
        apex,
        base,
        base,
        angle_labels=labels,
        side_labels=side_lbls,
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In the given isosceles triangle \\(ABC\\), \\(AB = AC\\) and the apex angle \\(\\hat{{A}} = {apex}^\\circ\\).\n\n"
        f"1. State the theorem relating sides and angles in an isosceles triangle.\n"
        f"2. Calculate the size of base angle \\(x = \\hat{{B}} = \\hat{{C}}\\) with reasons."
    )
    sol = (
        f"**Step 1: Geometric Reason**\n"
        f"Angles opposite equal sides are equal (\\(\\angle\\text{{s opp. equal sides}}\\)). Therefore, \\(\\hat{{B}} = \\hat{{C}} = x\\).\n\n"
        f"**Step 2: Calculate x**\n"
        f"\\[ \\hat{{A}} + 2x = 180^\\circ \\quad (\\text{{sum of }}\\angle\\text{{s in }}\\triangle ABC) \\]\n"
        f"\\[ {apex}^\\circ + 2x = 180^\\circ \\]\n"
        f"\\[ 2x = 180^\\circ - {apex}^\\circ = {180 - apex}^\\circ \\]\n"
        f"\\[ x = \\frac{{{180 - apex}^\\circ}}{{2}} = {base}^\\circ \\]"
    )
    ans = f"1. angles opp. equal sides are equal; 2. x = {base}°"
    return {
        "id": f"g8_iso_base_from_apex_{rng.randint(100000, 999999)}",
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
        "subskill": "05_isosceles_triangle_base_angles_given_apex",
        "learning_objective_id": "math_g8_iso_base_from_apex",
        "hints": {
            "tier_1": "In an isosceles triangle, the two angles opposite the equal sides are equal.",
            "tier_2": f"Subtract apex angle {apex}° from 180°, then divide by 2.",
            "tier_3": f"(180° - {apex}°) / 2 = {base}°.",
        },
        "misconception_tags": ["forgetting_to_divide_remainder_by_2"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 06. Isosceles Triangle Apex Given Base Angle (WITH SVG)
# ----------------------------------------------------------------------
def arch_06_isosceles_triangle_apex_given_base_angle(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([35, 42, 55, 65, 72])
    apex = 180 - 2 * base

    labels = {"A": "y", "B": f"{base}°", "C": f"{base}°"}
    side_lbls = {"AB": "equal", "AC": "equal"}
    svg = draw_triangle_svg(
        apex,
        base,
        base,
        angle_labels=labels,
        side_labels=side_lbls,
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In the given isosceles triangle \\(ABC\\), \\(AB = AC\\) and base angle \\(\\hat{{B}} = {base}^\\circ\\).\n\n"
        f"1. What is the size of the other base angle \\(\\hat{{C}}\\)? State the reason.\n"
        f"2. Calculate the size of apex angle \\(y = \\hat{{A}}\\) with reason."
    )
    sol = (
        f"**Step 1: Base angle C**\n"
        f"\\(\\hat{{C}} = {base}^\\circ\\) (\\(\\angle\\text{{s opp. equal sides, }} AB = AC\\)).\n\n"
        f"**Step 2: Apex angle y**\n"
        f"\\[ y = 180^\\circ - ({base}^\\circ + {base}^\\circ) \\quad (\\text{{sum of }}\\angle\\text{{s in }}\\triangle) \\]\n"
        f"\\[ y = 180^\\circ - {2 * base}^\\circ = {apex}^\\circ \\]"
    )
    ans = f"1. C = {base}° (angles opp equal sides); 2. y = {apex}° (sum of angles in triangle)"
    return {
        "id": f"g8_iso_apex_from_base_{rng.randint(100000, 999999)}",
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
        "subskill": "06_isosceles_triangle_apex_given_base_angle",
        "learning_objective_id": "math_g8_iso_apex_from_base",
        "hints": {
            "tier_1": "Both base angles are identical in size.",
            "tier_2": f"Sum of two base angles is 2 × {base}° = {2 * base}°.",
            "tier_3": f"y = 180° - {2 * base}° = {apex}°.",
        },
        "misconception_tags": ["subtracting_single_base_angle_from_180"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 07. Isosceles Triangle Algebraic Base Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_07_isosceles_triangle_algebraic_base_angles(rng: random.Random) -> Dict[str, Any]:
    ans_x = rng.choice([12, 15, 18, 20])
    c1 = rng.choice([2, 3])
    k1 = rng.choice([10, 15, 20])
    base_deg = c1 * ans_x + k1
    apex_deg = 180 - 2 * base_deg

    labels = {"A": f"{apex_deg}°", "B": f"({c1}x + {k1}°)", "C": "base"}
    svg = draw_triangle_svg(
        apex_deg,
        base_deg,
        base_deg,
        angle_labels=labels,
        side_labels={"AB": "equal", "AC": "equal"},
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In the given isosceles triangle \\(ABC\\), \\(AB = AC\\). The apex angle is \\(\\hat{{A}} = {apex_deg}^\\circ\\), "
        f"and one base angle is \\(\\hat{{B}} = {c1}x + {k1}^\\circ\\).\n\n"
        f"1. Determine the numerical value of base angle \\(\\hat{{B}}\\).\n"
        f"2. Solve the linear equation for \\(x\\)."
    )
    sol = (
        f"**Step 1: Numerical value of base angle**\n"
        f"\\[ \\hat{{B}} = \\frac{{180^\\circ - {apex_deg}^\\circ}}{{2}} = \\frac{{{180 - apex_deg}^\\circ}}{{2}} = {base_deg}^\\circ \\quad (\\angle\\text{{s opp. equal sides}}) \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {c1}x + {k1} = {base_deg} \\]\n"
        f"\\[ {c1}x = {base_deg - k1} \\]\n"
        f"\\[ x = \\frac{{{base_deg - k1}}}{{{c1}}} = {ans_x} \\]"
    )
    ans = f"1. B = {base_deg}°; 2. x = {ans_x}"
    return {
        "id": f"g8_iso_alg_base_{rng.randint(100000, 999999)}",
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
        "subskill": "07_isosceles_triangle_algebraic_base_angles",
        "learning_objective_id": "math_g8_iso_alg_base",
        "hints": {
            "tier_1": f"Calculate the numerical size of base angle B first: (180° - {apex_deg}°) / 2.",
            "tier_2": f"Set {c1}x + {k1} = {base_deg}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["equating_base_angle_directly_to_apex"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 08. Equilateral Triangle All Angles And Sides (WITH SVG)
# ----------------------------------------------------------------------
def arch_08_equilateral_triangle_all_angles_and_sides(rng: random.Random) -> Dict[str, Any]:
    ans_x = rng.choice([4, 6, 8, 10])
    c1, c2 = 3, 1
    k1 = rng.choice([2, 5, 8])
    k2 = (c1 - c2) * ans_x - k1
    side_len = c1 * ans_x - k1

    side_lbls = {"AB": f"{c1}x - {k1}", "BC": f"{c2}x + {k2}", "AC": f"{side_len} cm"}
    svg = draw_triangle_svg(
        60,
        60,
        60,
        angle_labels={"A": "60°", "B": "60°", "C": "60°"},
        side_labels=side_lbls,
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In equilateral triangle \\(ABC\\), all three sides are equal in length: "
        f"\\(AB = {c1}x - {k1}\\) cm and \\(BC = {c2}x + {k2}\\) cm.\n\n"
        f"1. State the size of each interior angle of an equilateral triangle.\n"
        f"2. Solve for \\(x\\) using the property of equal sides.\n"
        f"3. Calculate the perimeter of \\(\\triangle ABC\\) in cm."
    )
    sol = (
        f"**Step 1: Interior angles**\n"
        f"Each interior angle is \\(60^\\circ\\) (\\(\\text{{equilateral }}\\triangle\\)).\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {c1}x - {k1} = {c2}x + {k2} \\quad (\\text{{sides of equilateral }}\\triangle) \\]\n"
        f"\\[ {c1 - c2}x = {k2 + k1} \\]\n"
        f"\\[ x = {ans_x} \\]\n\n"
        f"**Step 3: Perimeter**\n"
        f"\\[ \\text{{Side length}} = {c1}({ans_x}) - {k1} = {side_len} \\text{{ cm}} \\]\n"
        f"\\[ \\text{{Perimeter}} = 3 \\times {side_len} = {3 * side_len} \\text{{ cm}} \\]"
    )
    ans = f"1. 60°; 2. x = {ans_x}; 3. {3 * side_len} cm"
    return {
        "id": f"g8_equi_tri_all_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "08_equilateral_triangle_all_angles_and_sides",
        "learning_objective_id": "math_g8_equi_tri_all",
        "hints": {
            "tier_1": "All 3 sides are equal and all 3 angles are 60°.",
            "tier_2": f"Set {c1}x - {k1} = {c2}x + {k2}.",
            "tier_3": f"x = {ans_x}, side = {side_len} cm, perimeter = {3 * side_len} cm.",
        },
        "misconception_tags": ["thinking_equilateral_angles_are_different"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 09. Right Angled Triangle Complementary Acute Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_09_right_angled_triangle_complementary_acute_angles(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([25, 32, 38, 45, 53, 64])
    ang2 = 90 - ang1

    labels = {"A": f"{ang1}°", "B": "90°", "C": "y"}
    svg = draw_triangle_svg(ang1, 90, ang2, angle_labels=labels, seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled triangle \\(ABC\\), \\(\\hat{{B}} = 90^\\circ\\) and \\(\\hat{{A}} = {ang1}^\\circ\\).\n\n"
        f"1. Explain why the two acute angles in a right-angled triangle are complementary.\n"
        f"2. Calculate the value of \\(y = \\hat{{C}}\\)."
    )
    sol = (
        f"**Step 1: Complementary explanation**\n"
        f"Since the total interior angle sum is \\(180^\\circ\\) and one angle is \\(90^\\circ\\), the other two angles "
        f"must add up to \\(180^\\circ - 90^\\circ = 90^\\circ\\). Two angles that add to \\(90^\\circ\\) are complementary.\n\n"
        f"**Step 2: Calculate y**\n"
        f"\\[ y = 90^\\circ - {ang1}^\\circ = {ang2}^\\circ \\]"
    )
    ans = f"1. sum to 90° because 180° - 90° = 90°; 2. y = {ang2}°"
    return {
        "id": f"g8_rt_tri_comp_{rng.randint(100000, 999999)}",
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
        "subskill": "09_right_angled_triangle_complementary_acute_angles",
        "learning_objective_id": "math_g8_rt_tri_comp",
        "hints": {
            "tier_1": "In a right-angled triangle, the acute angles sum to 90°.",
            "tier_2": f"Subtract {ang1}° from 90°.",
            "tier_3": f"y = {ang2}°.",
        },
        "misconception_tags": ["subtracting_from_180_instead_of_90"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 10. Classify Triangle By Angles And Sides (WITH SVG)
# ----------------------------------------------------------------------
def arch_10_classify_triangle_by_angles_and_sides(rng: random.Random) -> Dict[str, Any]:
    t_type = rng.choice(["obtuse_isosceles", "acute_scalene", "right_isosceles", "acute_equilateral"])
    if t_type == "obtuse_isosceles":
        a, b, c = 120, 30, 30
        desc_angle = "obtuse-angled"
        desc_side = "isosceles"
    elif t_type == "acute_scalene":
        a, b, c = 70, 60, 50
        desc_angle = "acute-angled"
        desc_side = "scalene"
    elif t_type == "right_isosceles":
        a, b, c = 90, 45, 45
        desc_angle = "right-angled"
        desc_side = "isosceles"
    else:
        a, b, c = 60, 60, 60
        desc_angle = "acute-angled (equiangular)"
        desc_side = "equilateral"

    svg = draw_triangle_svg(
        a,
        b,
        c,
        angle_labels={"A": f"{a}°", "B": f"{b}°", "C": f"{c}°"},
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"A triangle has interior angles measuring **{a}^\\circ**, **{b}^\\circ**, and **{c}^\\circ**.\n\n"
        f"1. Classify the triangle according to its **angles** (acute-angled, right-angled, or obtuse-angled).\n"
        f"2. Classify the triangle according to its **sides** (scalene, isosceles, or equilateral).\n"
        f"3. State your reason for each classification."
    )
    sol = (
        f"**1. Classification by angles:** {desc_angle}.\n"
        f"Reason: The largest angle is {max(a, b, c)}°.\n\n"
        f"**2. Classification by sides:** {desc_side}.\n"
        f"Reason: The angles determine equal/different sides (number of equal angles)."
    )
    ans = f"1. {desc_angle}; 2. {desc_side}"
    return {
        "id": f"g8_tri_classify_{rng.randint(100000, 999999)}",
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
        "subskill": "10_classify_triangle_by_angles_and_sides",
        "learning_objective_id": "math_g8_tri_classify",
        "hints": {
            "tier_1": "Angles: right (90°), obtuse (>90°), acute (all <90°).",
            "tier_2": "Sides: equilateral (all equal), isosceles (2 equal), scalene (all different).",
            "tier_3": f"Classification: {desc_angle} and {desc_side}.",
        },
        "misconception_tags": ["confusing_angle_classification_with_side_classification"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 11. Triangle Exterior Angle With Adjacent Supplementary (WITH SVG)
# ----------------------------------------------------------------------
def arch_11_triangle_exterior_angle_with_adjacent_supplementary(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([40, 50, 60])
    ang2 = rng.choice([45, 55, 65])
    ext_c = ang1 + ang2
    int_c = 180 - ext_c

    svg = draw_triangle_svg(
        ang1,
        ang2,
        int_c,
        angle_labels={"A": f"{ang1}°", "B": f"{ang2}°", "C": "z"},
        ext_angle=("C", f"{ext_c}°"),
        seed=rng.randint(100, 999999),
    )

    prompt = (
        f"In the given triangle \\(ABC\\), the exterior angle at vertex \\(C\\) is \\({ext_c}^\\circ\\).\n\n"
        f"1. Calculate the adjacent interior angle \\(z = \\angle ACB\\) using straight line angles.\n"
        f"2. Confirm that the sum \\(\\hat{{A}} + \\hat{{B}} + z = 180^\\circ\\) if \\(\\hat{{A}} = {ang1}^\\circ\\) and \\(\\hat{{B}} = {ang2}^\\circ\\)."
    )
    sol = (
        f"**Step 1: Calculate z**\n"
        f"\\[ z = 180^\\circ - {ext_c}^\\circ = {int_c}^\\circ \\quad (\\angle\\text{{s on a straight line}}) \\]\n\n"
        f"**Step 2: Confirm triangle sum**\n"
        f"\\[ {ang1}^\\circ + {ang2}^\\circ + {int_c}^\\circ = {ang1 + ang2 + int_c}^\\circ = 180^\\circ \\]"
    )
    ans = f"1. z = {int_c}° (angles on str line); 2. {ang1}° + {ang2}° + {int_c}° = 180°"
    return {
        "id": f"g8_tri_ext_supp_{rng.randint(100000, 999999)}",
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
        "subskill": "11_triangle_exterior_angle_with_adjacent_supplementary",
        "learning_objective_id": "math_g8_tri_ext_supp",
        "hints": {
            "tier_1": "Angles on a straight line add to 180°.",
            "tier_2": f"z = 180° - {ext_c}°.",
            "tier_3": f"z = {int_c}°.",
        },
        "misconception_tags": ["confusing_interior_and_exterior_supplement"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 12. Quadrilateral Interior Angle Sum Numerical (WITH SVG)
# ----------------------------------------------------------------------
def arch_12_quadrilateral_interior_angle_sum_numerical(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([75, 85, 95])
    b = rng.choice([100, 110, 115])
    c = rng.choice([60, 70, 80])
    d = 360 - (a + b + c)

    angles = {"A": f"{a}°", "B": f"{b}°", "C": f"{c}°", "D": "x"}
    svg = draw_quadrilateral_svg(kind="general", angles=angles, seed=rng.randint(100, 999999))

    prompt = (
        f"In the given quadrilateral \\(ABCD\\), three interior angles measure "
        f"\\(\\hat{{A}} = {a}^\\circ\\), \\(\\hat{{B}} = {b}^\\circ\\), and \\(\\hat{{C}} = {c}^\\circ\\).\n\n"
        f"1. State the theorem for the sum of the interior angles of a quadrilateral.\n"
        f"2. Calculate the value of \\(x = \\hat{{D}}\\) with geometric reason."
    )
    sol = (
        f"**Step 1: Geometric Theorem**\n"
        f"The sum of interior angles of a quadrilateral is \\(360^\\circ\\) (\\(\\text{{sum of }}\\angle\\text{{s in quad}}\\).\n\n"
        f"**Step 2: Calculate x**\n"
        f"\\[ {a}^\\circ + {b}^\\circ + {c}^\\circ + x = 360^\\circ \\]\n"
        f"\\[ {a + b + c}^\\circ + x = 360^\\circ \\]\n"
        f"\\[ x = 360^\\circ - {a + b + c}^\\circ = {d}^\\circ \\]"
    )
    ans = f"1. sum of angles in quadrilateral = 360°; 2. x = {d}°"
    return {
        "id": f"g8_quad_sum_num_{rng.randint(100000, 999999)}",
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
        "subskill": "12_quadrilateral_interior_angle_sum_numerical",
        "learning_objective_id": "math_g8_quad_sum_num",
        "hints": {
            "tier_1": "Four angles of any quadrilateral add up to 360°.",
            "tier_2": f"Add {a} + {b} + {c} = {a + b + c}°, then subtract from 360°.",
            "tier_3": f"x = {d}°.",
        },
        "misconception_tags": ["using_180_instead_of_360_for_quadrilateral"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 13. Quadrilateral Interior Angle Sum Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_13_quadrilateral_interior_angle_sum_algebraic(rng: random.Random) -> Dict[str, Any]:
    c1, c2, c3, c4 = rng.choice([(1, 2, 3, 4), (2, 3, 3, 4), (2, 2, 3, 5)])
    tot = c1 + c2 + c3 + c4
    ans_x = 360 // tot

    angles = {"A": f"{c1}x", "B": f"{c2}x", "C": f"{c3}x", "D": f"{c4}x"}
    svg = draw_quadrilateral_svg(kind="general", angles=angles, seed=rng.randint(100, 999999))

    prompt = (
        f"In quadrilateral \\(ABCD\\), the four interior angles are given algebraically as "
        f"\\({c1}x\\), \\({c2}x\\), \\({c3}x\\), and \\({c4}x\\).\n\n"
        f"1. Formulate an algebraic equation using the quadrilateral angle sum theorem.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Find the measure in degrees of the smallest interior angle."
    )
    min_c = min(c1, c2, c3, c4)
    sol = (
        f"**Step 1: Formulate equation**\n"
        f"\\[ {c1}x + {c2}x + {c3}x + {c4}x = 360^\\circ \\quad (\\text{{sum of }}\\angle\\text{{s in quad}}) \\]\n"
        f"\\[ {tot}x = 360 \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ x = \\frac{{360}}{{{tot}}} = {ans_x} \\]\n\n"
        f"**Step 3: Smallest angle**\n"
        f"\\[ {min_c} \\times {ans_x} = {min_c * ans_x}^\\circ \\]"
    )
    ans = f"1. {tot}x = 360; 2. x = {ans_x}; 3. {min_c * ans_x}°"
    return {
        "id": f"g8_quad_sum_alg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "13_quadrilateral_interior_angle_sum_algebraic",
        "learning_objective_id": "math_g8_quad_sum_alg",
        "hints": {
            "tier_1": "Sum of all four angles equals 360°.",
            "tier_2": f"{tot}x = 360°.",
            "tier_3": f"x = {ans_x}, smallest angle = {min_c * ans_x}°.",
        },
        "misconception_tags": ["equating_quadrilateral_sum_to_180"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 14. Parallelogram Opposite Angles Equal (WITH SVG)
# ----------------------------------------------------------------------
def arch_14_parallelogram_opposite_angles_equal(rng: random.Random) -> Dict[str, Any]:
    ang_acute = rng.choice([55, 65, 70, 75])
    ang_obtuse = 180 - ang_acute

    angles = {"A": f"{ang_acute}°", "B": "y", "C": "x", "D": f"{ang_obtuse}°"}
    svg = draw_quadrilateral_svg(kind="parallelogram", angles=angles, seed=rng.randint(100, 999999))

    prompt = (
        f"In the given parallelogram \\(ABCD\\) (\\(AB \\parallel DC\\) and \\(AD \\parallel BC\\)), "
        f"\\(\\hat{{A}} = {ang_acute}^\\circ\\) and \\(\\hat{{D}} = {ang_obtuse}^\\circ\\).\n\n"
        f"1. State the value of \\(x = \\hat{{C}}\\) with reason.\n"
        f"2. State the value of \\(y = \\hat{{B}}\\) with reason."
    )
    sol = (
        f"**1. Value of x:**\n"
        f"\\(x = {ang_acute}^\\circ\\) (\\(\\text{{opp. }}\\angle\\text{{s of }} \\parallel\\text{{m are equal}}\\)).\n\n"
        f"**2. Value of y:**\n"
        f"\\(y = {ang_obtuse}^\\circ\\) (\\(\\text{{opp. }}\\angle\\text{{s of }} \\parallel\\text{{m are equal}}\\))."
    )
    ans = f"1. x = {ang_acute}° (opp. angles of ||m); 2. y = {ang_obtuse}° (opp. angles of ||m)"
    return {
        "id": f"g8_parm_opp_ang_{rng.randint(100000, 999999)}",
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
        "subskill": "14_parallelogram_opposite_angles_equal",
        "learning_objective_id": "math_g8_parm_opp_ang",
        "hints": {
            "tier_1": "Opposite angles of a parallelogram are equal.",
            "tier_2": f"Angle C is opposite to Angle A ({ang_acute}°).",
            "tier_3": f"x = {ang_acute}°, y = {ang_obtuse}°.",
        },
        "misconception_tags": ["confusing_opposite_and_adjacent_angles_in_parallelogram"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 15. Parallelogram Co-Interior Adjacent Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_15_parallelogram_co_interior_adjacent_angles(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([62, 68, 74, 80])
    ang2 = 180 - ang1

    angles = {"A": f"{ang1}°", "B": "p"}
    svg = draw_quadrilateral_svg(kind="parallelogram", angles=angles, seed=rng.randint(100, 999999))

    prompt = (
        f"In the given parallelogram \\(ABCD\\), \\(AB \\parallel DC\\) and \\(\\hat{{A}} = {ang1}^\\circ\\).\n\n"
        f"1. Explain why adjacent angles \\(\\hat{{A}}\\) and \\(\\hat{{B}}\\) sum to \\(180^\\circ\\).\n"
        f"2. Calculate the value of \\(p = \\hat{{B}}\\) with reason."
    )
    sol = (
        f"**Step 1: Reason**\n"
        f"Adjacent angles between parallel lines are co-interior angles, which are supplementary "
        f"(\\(\\text{{co-int. }}\\angle\\text{{s, }} AD \\parallel BC\\)).\n\n"
        f"**Step 2: Calculate p**\n"
        f"\\[ p = 180^\\circ - {ang1}^\\circ = {ang2}^\\circ \\]"
    )
    ans = f"1. co-interior angles on parallel lines sum to 180°; 2. p = {ang2}°"
    return {
        "id": f"g8_parm_adj_ang_{rng.randint(100000, 999999)}",
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
        "subskill": "15_parallelogram_co_interior_adjacent_angles",
        "learning_objective_id": "math_g8_parm_adj_ang",
        "hints": {
            "tier_1": "Adjacent angles of a parallelogram are co-interior and sum to 180°.",
            "tier_2": f"Subtract {ang1}° from 180°.",
            "tier_3": f"p = {ang2}°.",
        },
        "misconception_tags": ["assuming_adjacent_angles_are_equal"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 16. Parallelogram Opposite Sides Equal Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_16_parallelogram_opposite_sides_equal_algebraic(rng: random.Random) -> Dict[str, Any]:
    ans_x = rng.choice([5, 7, 9, 11])
    ans_y = rng.choice([3, 4, 6, 8])

    c_x = 2
    k_x = rng.choice([3, 5, 7])
    top_len = c_x * ans_x + k_x

    c_y = 3
    k_y = rng.choice([2, 4, 6])
    side_len = c_y * ans_y - k_y

    side_lbls = {
        "top": f"{c_x}x + {k_x}",
        "bottom": f"{top_len} cm",
        "left": f"{c_y}y - {k_y}",
        "right": f"{side_len} cm",
    }
    svg = draw_quadrilateral_svg(kind="parallelogram", labels=side_lbls, seed=rng.randint(100, 999999))

    prompt = (
        f"In parallelogram \\(ABCD\\), opposite sides are equal in length:\n"
        f"\\(AB = {c_x}x + {k_x}\\) cm, \\(DC = {top_len}\\) cm, "
        f"\\(AD = {c_y}y - {k_y}\\) cm, and \\(BC = {side_len}\\) cm.\n\n"
        f"1. Solve for \\(x\\).\n"
        f"2. Solve for \\(y\\).\n"
        f"3. State the geometric reason justifying both equations."
    )
    sol = (
        f"**Step 1: Solve for x**\n"
        f"\\[ {c_x}x + {k_x} = {top_len} \\quad (\\text{{opp. sides of }} \\parallel\\text{{m are equal}}) \\]\n"
        f"\\[ {c_x}x = {top_len - k_x} \\implies x = {ans_x} \\]\n\n"
        f"**Step 2: Solve for y**\n"
        f"\\[ {c_y}y - {k_y} = {side_len} \\quad (\\text{{opp. sides of }} \\parallel\\text{{m are equal}}) \\]\n"
        f"\\[ {c_y}y = {side_len + k_y} \\implies y = {ans_y} \\]\n\n"
        f"**Step 3: Reason**\n"
        f"Opposite sides of a parallelogram are equal in length (\\(\\text{{opp. sides of }} \\parallel\\text{{m}}\\))."
    )
    ans = f"1. x = {ans_x}; 2. y = {ans_y}; 3. opp. sides of ||m are equal"
    return {
        "id": f"g8_parm_opp_sides_alg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "16_parallelogram_opposite_sides_equal_algebraic",
        "learning_objective_id": "math_g8_parm_opp_sides_alg",
        "hints": {
            "tier_1": "Opposite sides of a parallelogram are equal.",
            "tier_2": f"Set {c_x}x + {k_x} = {top_len} and {c_y}y - {k_y} = {side_len}.",
            "tier_3": f"x = {ans_x}, y = {ans_y}.",
        },
        "misconception_tags": ["equating_adjacent_sides_instead_of_opposite"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 17. Parallelogram Diagonals Bisect Each Other (WITH SVG)
# ----------------------------------------------------------------------
def arch_17_parallelogram_diagonals_bisect_each_other(rng: random.Random) -> Dict[str, Any]:
    ao = rng.choice([4, 6, 8, 10])
    bo = rng.choice([5, 7, 9, 11])

    svg = draw_quadrilateral_svg(kind="parallelogram", draw_diagonals=True, seed=rng.randint(100, 999999))

    prompt = (
        f"The diagonals of parallelogram \\(ABCD\\) intersect at point \\(O\\).\n"
        f"Segment \\(AO = {ao}\\) cm and segment \\(BO = {bo}\\) cm.\n\n"
        f"1. State the theorem concerning the diagonals of a parallelogram.\n"
        f"2. Calculate the length of diagonal \\(AC\\).\n"
        f"3. Calculate the length of diagonal \\(BD\\)."
    )
    sol = (
        f"**Step 1: Theorem**\n"
        f"The diagonals of a parallelogram bisect each other (\\(\\text{{diag. of }} \\parallel\\text{{m bisect}}\\)).\n\n"
        f"**Step 2: Diagonal AC**\n"
        f"\\[ AC = 2 \\times AO = 2 \\times {ao} = {2 * ao} \\text{{ cm}} \\]\n\n"
        f"**Step 3: Diagonal BD**\n"
        f"\\[ BD = 2 \\times BO = 2 \\times {bo} = {2 * bo} \\text{{ cm}} \\]"
    )
    ans = f"1. diagonals bisect each other; 2. AC = {2 * ao} cm; 3. BD = {2 * bo} cm"
    return {
        "id": f"g8_parm_diag_bisect_{rng.randint(100000, 999999)}",
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
        "subskill": "17_parallelogram_diagonals_bisect_each_other",
        "learning_objective_id": "math_g8_parm_diag_bisect",
        "hints": {
            "tier_1": "Diagonals cut each other into two equal halves.",
            "tier_2": f"Double the half-segments: 2 × {ao} and 2 × {bo}.",
            "tier_3": f"AC = {2 * ao} cm, BD = {2 * bo} cm.",
        },
        "misconception_tags": ["assuming_diagonals_are_equal_in_all_parallelograms"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 18. Rectangle Properties Right Angles And Equal Diagonals (WITH SVG)
# ----------------------------------------------------------------------
def arch_18_rectangle_properties_right_angles_and_equal_diagonals(rng: random.Random) -> Dict[str, Any]:
    diag_len = rng.choice([10, 13, 15, 20])

    svg = draw_quadrilateral_svg(kind="rectangle", draw_diagonals=True, seed=rng.randint(100, 999999))

    prompt = (
        f"Consider rectangle \\(ABCD\\) with diagonals \\(AC\\) and \\(BD\\) intersecting at point \\(O\\).\n"
        f"The diagonal \\(AC = {diag_len}\\) cm.\n\n"
        f"1. What is the size of each of the four interior angles?\n"
        f"2. What is the length of diagonal \\(BD\\)? State the reason.\n"
        f"3. Find the length of segment \\(AO\\)."
    )
    half_diag = diag_len / 2
    half_str = f"{int(half_diag)}" if half_diag.is_integer() else f"{half_diag:.1f}"
    sol = (
        f"**1. Interior angles:** Each angle is \\(90^\\circ\\) (\\(\\text{{angles of rectangle}}\\)).\n\n"
        f"**2. Diagonal BD:** \\(BD = {diag_len}\\) cm (\\(\\text{{diagonals of rectangle are equal}}\\)).\n\n"
        f"**3. Segment AO:**\n"
        f"\\[ AO = \\frac{{{diag_len}}}{{2}} = {half_str} \\text{{ cm}} \\quad (\\text{{diagonals bisect each other}}) \\]"
    )
    ans = f"1. 90°; 2. BD = {diag_len} cm (diagonals equal); 3. AO = {half_str} cm"
    return {
        "id": f"g8_rect_props_{rng.randint(100000, 999999)}",
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
        "subskill": "18_rectangle_properties_right_angles_and_equal_diagonals",
        "learning_objective_id": "math_g8_rect_props",
        "hints": {
            "tier_1": "In a rectangle, all angles are 90° and diagonals are equal in length.",
            "tier_2": f"BD = AC = {diag_len} cm.",
            "tier_3": f"AO = {diag_len} / 2 = {half_str} cm.",
        },
        "misconception_tags": ["thinking_rectangle_diagonals_are_perpendicular"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 19. Rhombus Properties All Sides Equal And Opposite Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_19_rhombus_properties_all_sides_equal_and_opposite_angles(rng: random.Random) -> Dict[str, Any]:
    side_len = rng.choice([6, 8, 10, 12])
    ang1 = rng.choice([60, 70, 80])
    ang2 = 180 - ang1

    angles = {"A": f"{ang1}°", "B": "x"}
    side_lbls = {"top": f"{side_len} cm"}
    svg = draw_quadrilateral_svg(kind="rhombus", angles=angles, labels=side_lbls, seed=rng.randint(100, 999999))

    prompt = (
        f"In rhombus \\(ABCD\\), side \\(AB = {side_len}\\) cm and \\(\\hat{{A}} = {ang1}^\\circ\\).\n\n"
        f"1. What is the total perimeter of the rhombus?\n"
        f"2. Calculate the size of adjacent interior angle \\(x = \\hat{{B}}\\) with reason."
    )
    sol = (
        f"**Step 1: Perimeter**\n"
        f"All four sides of a rhombus are equal in length:\n"
        f"\\[ \\text{{Perimeter}} = 4 \\times {side_len} = {4 * side_len} \\text{{ cm}} \\]\n\n"
        f"**Step 2: Angle x**\n"
        f"\\[ x = 180^\\circ - {ang1}^\\circ = {ang2}^\\circ \\quad (\\text{{co-int. }}\\angle\\text{{s, }} AD \\parallel BC) \\]"
    )
    ans = f"1. {4 * side_len} cm; 2. x = {ang2}° (co-int. angles, AD || BC)"
    return {
        "id": f"g8_rhomb_props_{rng.randint(100000, 999999)}",
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
        "subskill": "19_rhombus_properties_all_sides_equal_and_opposite_angles",
        "learning_objective_id": "math_g8_rhomb_props",
        "hints": {
            "tier_1": "All four sides of a rhombus are equal. Adjacent angles sum to 180°.",
            "tier_2": f"Perimeter = 4 × {side_len} cm.",
            "tier_3": f"Angle B = 180° - {ang1}° = {ang2}°.",
        },
        "misconception_tags": ["assuming_all_angles_of_rhombus_are_90"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 20. Rhombus Diagonals Perpendicular Bisectors (WITH SVG)
# ----------------------------------------------------------------------
def arch_20_rhombus_diagonals_perpendicular_bisectors(rng: random.Random) -> Dict[str, Any]:
    svg = draw_quadrilateral_svg(kind="rhombus", draw_diagonals=True, seed=rng.randint(100, 999999))

    prompt = (
        f"The diagonals of rhombus \\(ABCD\\) intersect at point \\(O\\).\n\n"
        f"1. State the angle at which the diagonals of a rhombus intersect (\\(\\angle AOB\\)).\n"
        f"2. State the two key theorems regarding the diagonals of a rhombus."
    )
    sol = (
        f"**1. Angle of intersection:**\n"
        f"\\(\\angle AOB = 90^\\circ\\) (\\(\\text{{diagonals of rhombus bisect at right angles}}\\)).\n\n"
        f"**2. Two key theorems:**\n"
        f"1. The diagonals bisect each other perpendicularly at \\(90^\\circ\\) (\\(\\text{{diag. of rhombus }}\\perp\\)).\n"
        f"2. The diagonals bisect the vertex interior angles of the rhombus."
    )
    ans = "1. 90°; 2. diagonals bisect perpendicularly at 90°, and bisect vertex angles"
    return {
        "id": f"g8_rhomb_diag_perp_{rng.randint(100000, 999999)}",
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
        "subskill": "20_rhombus_diagonals_perpendicular_bisectors",
        "learning_objective_id": "math_g8_rhomb_diag_perp",
        "hints": {
            "tier_1": "Rhombus diagonals are perpendicular bisectors.",
            "tier_2": "The angle between perpendicular lines is 90°.",
            "tier_3": "Angle AOB = 90°; diagonals bisect perpendicularly and bisect vertex angles.",
        },
        "misconception_tags": ["thinking_rhombus_diagonals_are_equal_in_length"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 21. Square Properties Regular Quadrilateral (WITH SVG)
# ----------------------------------------------------------------------
def arch_21_square_properties_regular_quadrilateral(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([5, 8, 12, 15])
    side_lbls = {"top": f"{s} cm"}
    svg = draw_quadrilateral_svg(kind="square", labels=side_lbls, draw_diagonals=True, seed=rng.randint(100, 999999))

    prompt = (
        f"A square \\(ABCD\\) has side length **{s} cm**.\n\n"
        f"1. Why is a square classified as both a rectangle and a rhombus?\n"
        f"2. What is the measure of the angle between its diagonals at their intersection?\n"
        f"3. Calculate the area of the square in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**1. Classification:**\n"
        f"- It is a rectangle because all 4 interior angles are \\(90^\\circ\\).\n"
        f"- It is a rhombus because all 4 sides are equal in length.\n\n"
        f"**2. Angle between diagonals:**\n"
        f"\\(90^\\circ\\) (\\(\\text{{diagonals of square bisect perpendicularly}}\\)).\n\n"
        f"**3. Area:**\n"
        f"\\[ \\text{{Area}} = s^2 = {s}^2 = {s * s} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. all angles 90° (rectangle) and all sides equal (rhombus); 2. 90°; 3. {s * s} cm²"
    return {
        "id": f"g8_sq_props_{rng.randint(100000, 999999)}",
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
        "subskill": "21_square_properties_regular_quadrilateral",
        "learning_objective_id": "math_g8_sq_props",
        "hints": {
            "tier_1": "A square is a regular quadrilateral: equal sides and equal angles.",
            "tier_2": "Diagonals of a square are equal and cross at 90°.",
            "tier_3": f"Area = {s} × {s} = {s * s} cm².",
        },
        "misconception_tags": ["confusing_area_with_perimeter"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 22. Trapezium Co-Interior Angles Between Parallel Sides (WITH SVG)
# ----------------------------------------------------------------------
def arch_22_trapezium_co_interior_angles_between_parallel_sides(rng: random.Random) -> Dict[str, Any]:
    ang_a = rng.choice([105, 110, 115, 120])
    ang_d = 180 - ang_a
    ang_b = rng.choice([95, 100, 125])
    ang_c = 180 - ang_b

    angles = {"A": f"{ang_a}°", "B": f"{ang_b}°", "C": "y", "D": "x"}
    svg = draw_quadrilateral_svg(kind="trapezium", angles=angles, seed=rng.randint(100, 999999))

    prompt = (
        f"In trapezium \\(ABCD\\), \\(AB \\parallel DC\\).\n"
        f"Interior angles \\(\\hat{{A}} = {ang_a}^\\circ\\) and \\(\\hat{{B}} = {ang_b}^\\circ\\).\n\n"
        f"1. Calculate the value of \\(x = \\hat{{D}}\\) with reason.\n"
        f"2. Calculate the value of \\(y = \\hat{{C}}\\) with reason."
    )
    sol = (
        f"**Step 1: Calculate x**\n"
        f"\\[ x = 180^\\circ - {ang_a}^\\circ = {ang_d}^\\circ \\quad (\\text{{co-int. }}\\angle\\text{{s, }} AB \\parallel DC) \\]\n\n"
        f"**Step 2: Calculate y**\n"
        f"\\[ y = 180^\\circ - {ang_b}^\\circ = {ang_c}^\\circ \\quad (\\text{{co-int. }}\\angle\\text{{s, }} AB \\parallel DC) \\]"
    )
    ans = f"1. x = {ang_d}° (co-int. angles, AB || DC); 2. y = {ang_c}° (co-int. angles, AB || DC)"
    return {
        "id": f"g8_trap_coint_{rng.randint(100000, 999999)}",
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
        "subskill": "22_trapezium_co_interior_angles_between_parallel_sides",
        "learning_objective_id": "math_g8_trap_coint",
        "hints": {
            "tier_1": "Angles on each non-parallel side are co-interior between parallel bases.",
            "tier_2": f"x = 180° - {ang_a}° and y = 180° - {ang_b}°.",
            "tier_3": f"x = {ang_d}°, y = {ang_c}°.",
        },
        "misconception_tags": ["adding_angles_on_same_base_to_180"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 23. Isosceles Trapezium Base Angles And Diagonals (WITH SVG)
# ----------------------------------------------------------------------
def arch_23_isosceles_trapezium_base_angles_and_diagonals(rng: random.Random) -> Dict[str, Any]:
    base_ang = rng.choice([65, 70, 75])
    top_ang = 180 - base_ang
    diag_len = rng.choice([12, 14, 16])

    angles = {"A": f"{top_ang}°", "D": f"{base_ang}°"}
    svg = draw_quadrilateral_svg(kind="trapezium", angles=angles, draw_diagonals=True, seed=rng.randint(100, 999999))

    prompt = (
        f"In isosceles trapezium \\(ABCD\\), \\(AB \\parallel DC\\) and the non-parallel sides are equal (\\(AD = BC\\)).\n"
        f"Base angle \\(\\hat{{D}} = {base_ang}^\\circ\\) and diagonal \\(AC = {diag_len}\\) cm.\n\n"
        f"1. What is the size of the other base angle \\(\\hat{{C}}\\) along \\(DC\\)?\n"
        f"2. What is the size of top angle \\(\\hat{{A}}\\) with reason?\n"
        f"3. What is the length of diagonal \\(BD\\)?"
    )
    sol = (
        f"**1. Base angle C:**\n"
        f"\\(\\hat{{C}} = {base_ang}^\\circ\\) (\\(\\text{{base }}\\angle\\text{{s of isosceles trapezium are equal}}\\)).\n\n"
        f"**2. Top angle A:**\n"
        f"\\(\\hat{{A}} = 180^\\circ - {base_ang}^\\circ = {top_ang}^\\circ\\) (\\(\\text{{co-int. }}\\angle\\text{{s, }} AB \\parallel DC\\)).\n\n"
        f"**3. Diagonal BD:**\n"
        f"\\(BD = {diag_len}\\) cm (\\(\\text{{diagonals of isosceles trapezium are equal}}\\))."
    )
    ans = f"1. C = {base_ang}°; 2. A = {top_ang}° (co-int. angles, AB || DC); 3. BD = {diag_len} cm"
    return {
        "id": f"g8_iso_trap_{rng.randint(100000, 999999)}",
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
        "subskill": "23_isosceles_trapezium_base_angles_and_diagonals",
        "learning_objective_id": "math_g8_iso_trap",
        "hints": {
            "tier_1": "In an isosceles trapezium, base angles are equal and diagonals are equal.",
            "tier_2": f"Angle C = Angle D = {base_ang}°, BD = AC = {diag_len} cm.",
            "tier_3": f"Angle A = 180° - {base_ang}° = {top_ang}°.",
        },
        "misconception_tags": ["assuming_all_trapeziums_have_equal_diagonals"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 24. Kite Properties Two Pairs Adjacent Sides Equal (WITH SVG)
# ----------------------------------------------------------------------
def arch_24_kite_properties_two_pairs_adjacent_sides_equal(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([5, 7, 9])
    b = rng.choice([10, 12, 14])
    ang_b = rng.choice([100, 105, 110])

    angles = {"B": f"{ang_b}°", "D": "x"}
    side_lbls = {"top": f"{a} cm", "bottom": f"{b} cm"}
    svg = draw_quadrilateral_svg(kind="kite", angles=angles, labels=side_lbls, seed=rng.randint(100, 999999))

    prompt = (
        f"In kite \\(ABCD\\), \\(AB = AD = {a}\\) cm and \\(BC = DC = {b}\\) cm.\n"
        f"The angle \\(\\hat{{B}} = {ang_b}^\\circ\\).\n\n"
        f"1. What is the total perimeter of the kite in cm?\n"
        f"2. State the size of opposite angle \\(x = \\hat{{D}}\\) with geometric reason."
    )
    perim = 2 * (a + b)
    sol = (
        f"**Step 1: Perimeter**\n"
        f"\\[ \\text{{Perimeter}} = 2({a}) + 2({b}) = {perim} \\text{{ cm}} \\]\n\n"
        f"**Step 2: Angle D**\n"
        f"\\(x = {ang_b}^\\circ\\) (\\(\\text{{one pair of opp. }}\\angle\\text{{s of kite are equal, between unequal sides}}\\))."
    )
    ans = f"1. {perim} cm; 2. x = {ang_b}° (one pair opp. angles of kite equal)"
    return {
        "id": f"g8_kite_props_{rng.randint(100000, 999999)}",
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
        "subskill": "24_kite_properties_two_pairs_adjacent_sides_equal",
        "learning_objective_id": "math_g8_kite_props",
        "hints": {
            "tier_1": "Kite has two pairs of adjacent equal sides and one pair of equal opposite angles.",
            "tier_2": f"Perimeter = 2 × ({a} + {b}) cm.",
            "tier_3": f"x = {ang_b}°.",
        },
        "misconception_tags": ["thinking_both_pairs_of_opposite_angles_are_equal_in_kite"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 25. Kite Diagonals Perpendicular And Axis Of Symmetry (WITH SVG)
# ----------------------------------------------------------------------
def arch_25_kite_diagonals_perpendicular_and_axis_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    svg = draw_quadrilateral_svg(kind="kite", draw_diagonals=True, seed=rng.randint(100, 999999))

    prompt = (
        f"The diagonals \\(AC\\) and \\(BD\\) of kite \\(ABCD\\) intersect at point \\(O\\).\n"
        f"Diagonal \\(AC\\) is the line of symmetry.\n\n"
        f"1. What is the size of \\(\\angle AOB\\) at the intersection of the diagonals?\n"
        f"2. Which diagonal bisects the other into two equal segments?\n"
        f"3. State how many lines of reflective symmetry a kite has."
    )
    sol = (
        f"**1. Angle AOB:** \\(90^\\circ\\) (\\(\\text{{diagonals of kite intersect at right angles}}\\)).\n\n"
        f"**2. Bisecting diagonal:** Diagonal \\(AC\\) (the main diagonal / line of symmetry) bisects diagonal \\(BD\\) (\\(BO = OD\\)).\n\n"
        f"**3. Lines of symmetry:** Exactly **1** line of symmetry (along the main diagonal \\(AC\\))."
    )
    ans = "1. 90°; 2. AC bisects BD (BO = OD); 3. 1 line of symmetry"
    return {
        "id": f"g8_kite_diag_{rng.randint(100000, 999999)}",
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
        "subskill": "25_kite_diagonals_perpendicular_and_axis_of_symmetry",
        "learning_objective_id": "math_g8_kite_diag",
        "hints": {
            "tier_1": "Diagonals of a kite intersect at 90°.",
            "tier_2": "The main diagonal bisects the cross diagonal.",
            "tier_3": "Angle is 90°; AC bisects BD; 1 line of symmetry.",
        },
        "misconception_tags": ["assuming_both_diagonals_bisect_each_other_in_a_kite"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }
