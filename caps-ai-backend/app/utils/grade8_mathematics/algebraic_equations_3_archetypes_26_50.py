"""
Grade 8 Mathematics - Algebraic Equations 3 Archetypes (26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/02. Algebraic equations 3.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional

from .svg_diagrams import (
    draw_algebraic_shape_perimeter_svg,
    draw_angles_on_line_svg,
    draw_triangle_angles_svg,
)


# ----------------------------------------------------------------------
# 26. Geometry Vertically Opposite Angles Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_26_geometry_vertically_opposite_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5])
    c = rng.choice([1, 2])
    ans_x = rng.choice([15, 20, 25])
    b = rng.choice([10, 15, 20])
    # a*x - b = c*x + d => (a - c)*ans_x - b = d
    d = (a - c) * ans_x - b
    ang_val = a * ans_x - b

    lbl1 = f"{a}x - {b}°"
    lbl2 = f"{c}x + {d}°"
    svg = draw_angles_on_line_svg(ang_val, lbl1, lbl2)

    prompt = (
        f"Two intersecting straight lines form vertically opposite angles:\n\n"
        f"\\[ \\angle P = ({a}x - {b})^\\circ \\quad \\text{{and}} \\quad \\angle Q = ({c}x + {d})^\\circ \\]\n\n"
        f"1. State the theorem relating vertically opposite angles.\n"
        f"2. Set up an equation and solve for \\(x\\).\n"
        f"3. Calculate the actual size in degrees of both angles."
    )
    sol = (
        f"**Step 1: Geometric Theorem**\n"
        f"Vertically opposite angles are equal (\\(\\text{{vert. opp. }} \\angle\\text{{s are equal}}\\)).\n\n"
        f"**Step 2: Set up equation and solve**\n"
        f"\\[ {a}x - {b} = {c}x + {d} \\]\n"
        f"\\[ {a}x - {c}x = {d} + {b} \\]\n"
        f"\\[ {a - c}x = {d + b} \\]\n"
        f"\\[ x = \\frac{{{d + b}}}{{{a - c}}} = {ans_x} \\]\n\n"
        f"**Step 3: Actual angle size**\n"
        f"\\(\\angle P = {a}({ans_x}) - {b} = {ang_val}^\\circ\\)\n"
        f"\\(\\angle Q = {c}({ans_x}) + {d} = {ang_val}^\\circ\\)."
    )
    ans = f"1. vert opp angles are equal; 2. x = {ans_x}; 3. {ang_val}°"
    return {
        "id": f"g8_eq3_vert_opp_{rng.randint(100000, 999999)}",
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
        "subskill": "26_geometry_vertically_opposite_angles_algebraic",
        "learning_objective_id": "math_g8_eq3_vert_opp_angles",
        "hints": {
            "tier_1": f"Vertically opposite angles are equal in magnitude.",
            "tier_2": f"{a}x - {b} = {c}x + {d}.",
            "tier_3": f"{a - c}x = {d + b}, so x = {ans_x}.",
        },
        "misconception_tags": ["adding_angles_to_180_instead_of_equating"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 27. Geometry Triangle Interior Angles Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_27_geometry_triangle_interior_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    ans_x = rng.choice([15, 20, 25])
    a = rng.choice([2, 3])
    b = rng.choice([1, 2])
    c = 1
    # a*x + b*x + c*x + k = 180 => (a+b+c)*ans_x + k = 180
    total_coeff = a + b + c
    k = 180 - total_coeff * ans_x
    if k < 10 or k > 60:
        ans_x = 20
        a, b, c = 2, 3, 1  # sum = 6 => 6*20 = 120 => k = 60
        k = 60

    ang_a = a * ans_x
    ang_b = b * ans_x
    ang_c = c * ans_x + k

    lbl_a = f"{a}x°"
    lbl_b = f"{b}x°"
    lbl_c = f"(x + {k})°"
    svg = draw_triangle_angles_svg(ang_a, ang_b, ang_c, lbl_a, lbl_b, lbl_c)

    prompt = (
        f"In a triangle, the interior angles are given algebraically as:\n\n"
        f"\\[ \\hat{{A}} = {a}x^\\circ, \\quad \\hat{{B}} = {b}x^\\circ, \\quad \\hat{{C}} = (x + {k})^\\circ \\]\n\n"
        f"1. Set up an equation using the sum of interior angles of a triangle.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Find the measure in degrees of angle \\(\\hat{{C}}\\)."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"The sum of interior angles of a triangle equals \\(180^\\circ\\):\n"
        f"\\[ {a}x + {b}x + (x + {k}) = 180 \\]\n"
        f"\\[ {total_coeff}x + {k} = 180 \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {total_coeff}x = 180 - {k} = {180 - k} \\]\n"
        f"\\[ x = \\frac{{{180 - k}}}{{{total_coeff}}} = {ans_x} \\]\n\n"
        f"**Step 3: Measure of angle C**\n"
        f"\\[ \\hat{{C}} = {ans_x} + {k} = {ang_c}^\\circ \\]"
    )
    ans = f"1. {total_coeff}x + {k} = 180; 2. x = {ans_x}; 3. C = {ang_c}°"
    return {
        "id": f"g8_eq3_tri_int_{rng.randint(100000, 999999)}",
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
        "subskill": "27_geometry_triangle_interior_angles_algebraic",
        "learning_objective_id": "math_g8_eq3_triangle_interior_sum",
        "hints": {
            "tier_1": f"Sum of angles in a triangle = 180°.",
            "tier_2": f"({a} + {b} + 1)x + {k} = 180.",
            "tier_3": f"x = {ans_x}, C = {ang_c}°.",
        },
        "misconception_tags": ["setting_triangle_sum_to_360"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 28. Geometry Isosceles Triangle Base Angles Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_28_geometry_isosceles_triangle_base_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4])
    c = rng.choice([1, 2])
    ans_x = rng.choice([15, 20, 25])
    b = rng.choice([5, 10])
    # a*x - b = c*x + d => d = (a-c)*ans_x - b
    d = (a - c) * ans_x - b
    base_ang = a * ans_x - b
    apex_ang = 180 - 2 * base_ang
    if apex_ang <= 20 or apex_ang >= 120:
        ans_x = 20
        a, c, b = 3, 1, 10
        d = 30
        base_ang = 50
        apex_ang = 80

    lbl_b = f"{a}x - {b}°"
    lbl_c = f"{c}x + {d}°"
    lbl_a = f"{apex_ang}°"
    svg = draw_triangle_angles_svg(apex_ang, base_ang, base_ang, lbl_a, lbl_b, lbl_c)

    prompt = (
        f"In an isosceles triangle \\(\\Delta ABC\\) with \\(AB = AC\\), the equal base angles are given as:\n\n"
        f"\\[ \\hat{{B}} = ({a}x - {b})^\\circ \\quad \\text{{and}} \\quad \\hat{{C}} = ({c}x + {d})^\\circ \\]\n\n"
        f"1. State the geometric property of base angles in an isosceles triangle.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Calculate the size of the apex angle \\(\\hat{{A}}\\)."
    )
    sol = (
        f"**Step 1: Isosceles Triangle Property**\n"
        f"Angles opposite equal sides are equal (\\(\\angle\\text{{s opp. equal sides}}\\)).\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {a}x - {b} = {c}x + {d} \\]\n"
        f"\\[ {a - c}x = {d + b} \\]\n"
        f"\\[ x = \\frac{{{d + b}}}{{{a - c}}} = {ans_x} \\]\n\n"
        f"**Step 3: Base angle and apex angle**\n"
        f"Base angle \\(= {a}({ans_x}) - {b} = {base_ang}^\\circ\\).\n"
        f"\\[ \\hat{{A}} = 180^\\circ - 2({base_ang}^\\circ) = {apex_ang}^\\circ \\]"
    )
    ans = f"1. angles opp equal sides are equal; 2. x = {ans_x}; 3. A = {apex_ang}°"
    return {
        "id": f"g8_eq3_iso_tri_{rng.randint(100000, 999999)}",
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
        "subskill": "28_geometry_isosceles_triangle_base_angles_algebraic",
        "learning_objective_id": "math_g8_eq3_isosceles_angles",
        "hints": {
            "tier_1": f"Base angles are equal: {a}x - {b} = {c}x + {d}.",
            "tier_2": f"{a - c}x = {d + b}, giving x = {ans_x}.",
            "tier_3": f"Apex angle A = 180° - 2({base_ang}°) = {apex_ang}°.",
        },
        "misconception_tags": ["forgetting_to_double_base_angle_for_apex"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 29. Geometry Exterior Angle Of Triangle Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_29_geometry_exterior_angle_of_triangle_algebraic(rng: random.Random) -> Dict[str, Any]:
    ans_x = rng.choice([15, 20, 25])
    a = 4
    c, e = 2, 1
    # Ext = a*x + b; Int1 = c*x + d; Int2 = e*x + f
    # Ext = Int1 + Int2 => a*x + b = (c+e)*x + (d+f)
    # 4x + b = 3x + (d+f) => x = (d+f) - b
    d = rng.choice([10, 15])
    f = rng.choice([10, 20])
    b = (d + f) - ans_x

    ang_int1 = c * ans_x + d
    ang_int2 = e * ans_x + f
    ang_ext = a * ans_x + b
    ang_int3 = 180 - ang_ext

    lbl_a = f"({c}x + {d})°"
    lbl_b = f"({e}x + {f})°"
    lbl_c = f"{ang_int3}°"
    ext_lbl = f"({a}x + {b})°"
    svg = draw_triangle_angles_svg(ang_int1, ang_int2, ang_int3, lbl_a, lbl_b, lbl_c, ext_lbl)

    prompt = (
        f"In a triangle with an extended exterior angle, the two opposite interior angles and the exterior angle are:\n\n"
        f"\\[ \\hat{{A}} = ({c}x + {d})^\\circ, \\quad \\hat{{B}} = ({e}x + {f})^\\circ, \\quad \\text{{Exterior }} \\angle = ({a}x + {b})^\\circ \\]\n\n"
        f"1. State the exterior angle of a triangle theorem.\n"
        f"2. Set up an equation and solve for \\(x\\).\n"
        f"3. Find the size of the exterior angle."
    )
    sol = (
        f"**Step 1: Exterior Angle Theorem**\n"
        f"The exterior angle of a triangle equals the sum of the two opposite interior angles (\\(\\text{{ext. }} \\angle \\text{{ of }} \\Delta\\)).\n\n"
        f"**Step 2: Set up equation and solve**\n"
        f"\\[ ({a}x + {b}) = ({c}x + {d}) + ({e}x + {f}) \\]\n"
        f"\\[ {a}x + {b} = {c + e}x + {d + f} \\]\n"
        f"\\[ {a - (c + e)}x = {d + f - b} \\]\n"
        f"\\[ x = {ans_x} \\]\n\n"
        f"**Step 3: Exterior angle**\n"
        f"\\[ \\text{{Exterior }} \\angle = {a}({ans_x}) + {b} = {ang_ext}^\\circ \\]"
    )
    ans = f"1. ext angle of triangle = sum of opp interior angles; 2. x = {ans_x}; 3. ext angle = {ang_ext}°"
    return {
        "id": f"g8_eq3_ext_tri_{rng.randint(100000, 999999)}",
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
        "subskill": "29_geometry_exterior_angle_of_triangle_algebraic",
        "learning_objective_id": "math_g8_eq3_exterior_angle_triangle",
        "hints": {
            "tier_1": f"Exterior angle = sum of two opposite interior angles.",
            "tier_2": f"{a}x + {b} = ({c + e})x + ({d + f}).",
            "tier_3": f"x = {ans_x}, exterior angle = {ang_ext}°.",
        },
        "misconception_tags": ["adding_all_three_angles_to_180_including_exterior"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 30. Consecutive Integers Algebraic Sum Product Puzzle
# ----------------------------------------------------------------------
def arch_30_consecutive_integers_algebraic_sum_product_puzzle(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([15, 21, 24, 30, 35])
    s = 3 * n + 3  # n + (n+1) + (n+2) = 3n + 3

    prompt = (
        f"The sum of three consecutive integers is **{s}**.\n\n"
        f"1. Let the smallest integer be \\(n\\). Write an algebraic equation for the sum.\n"
        f"2. Solve your equation to determine the three integers."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"The integers are \\(n\\), \\(n + 1\\), and \\(n + 2\\).\n"
        f"\\[ n + (n + 1) + (n + 2) = {s} \\]\n"
        f"\\[ 3n + 3 = {s} \\]\n\n"
        f"**Step 2: Solve for n**\n"
        f"\\[ 3n = {s} - 3 = {s - 3} \\]\n"
        f"\\[ n = \\frac{{{s - 3}}}{{3}} = {n} \\]\n\n"
        f"The three integers are **{n}**, **{n + 1}**, and **{n + 2}**."
    )
    ans = f"1. 3n + 3 = {s}; 2. {n}, {n + 1}, {n + 2}"
    return {
        "id": f"g8_eq3_cons_int_{rng.randint(100000, 999999)}",
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
        "subskill": "30_consecutive_integers_algebraic_sum_product_puzzle",
        "learning_objective_id": "math_g8_eq3_consecutive_integers",
        "hints": {
            "tier_1": f"Consecutive integers: n, n+1, n+2.",
            "tier_2": f"3n + 3 = {s}.",
            "tier_3": f"n = {n}, integers are {n}, {n + 1}, {n + 2}.",
        },
        "misconception_tags": ["using_n_plus_2_and_n_plus_4_for_regular_consecutive"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 31. Consecutive Even Integers With Multiplier
# ----------------------------------------------------------------------
def arch_31_consecutive_even_integers_with_multiplier(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([10, 12, 14, 16, 18])  # smallest even
    # 2*(n) + 3*(n + 2) = s => 2n + 3n + 6 = 5n + 6
    s = 5 * n + 6

    prompt = (
        f"Two consecutive even numbers are such that twice the smaller number added to three times the larger number equals **{s}**.\n\n"
        f"1. Let the smaller even number be \\(x\\). Write an algebraic equation for this condition.\n"
        f"2. Solve for \\(x\\) and state both even numbers."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"Smaller even number = \\(x\\); larger even number = \\(x + 2\\).\n"
        f"\\[ 2x + 3(x + 2) = {s} \\]\n\n"
        f"**Step 2: Expand and solve**\n"
        f"\\[ 2x + 3x + 6 = {s} \\]\n"
        f"\\[ 5x + 6 = {s} \\]\n"
        f"\\[ 5x = {s - 6} \\]\n"
        f"\\[ x = \\frac{{{s - 6}}}{{5}} = {n} \\]\n\n"
        f"The smaller number is **{n}** and the larger is **{n + 2}**."
    )
    ans = f"1. 2x + 3(x + 2) = {s}; 2. {n} and {n + 2}"
    return {
        "id": f"g8_eq3_even_mult_{rng.randint(100000, 999999)}",
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
        "subskill": "31_consecutive_even_integers_with_multiplier",
        "learning_objective_id": "math_g8_eq3_even_integers_mult",
        "hints": {
            "tier_1": f"Consecutive even numbers differ by 2: x and x + 2.",
            "tier_2": f"2x + 3(x + 2) = {s}.",
            "tier_3": f"5x + 6 = {s}, so x = {n}.",
        },
        "misconception_tags": ["using_x_plus_1_for_even_numbers"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 32. Speed Distance Time Opposing Directions
# ----------------------------------------------------------------------
def arch_32_speed_distance_time_opposing_directions(rng: random.Random) -> Dict[str, Any]:
    v1 = rng.choice([60, 70, 80])
    v2 = rng.choice([80, 90, 100])
    t = rng.choice([2, 3, 4])
    dist = (v1 + v2) * t

    prompt = (
        f"Two cars leave towns that are **{dist} km** apart at the same time, traveling towards each other on the same highway. "
        f"Car A travels at **{v1} km/h** and Car B travels at **{v2} km/h**.\n\n"
        f"1. Set up an algebraic equation for the time \\(t\\) in hours until the two cars meet.\n"
        f"2. Solve for \\(t\\) and determine the distance Car A has traveled when they meet."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"Distance traveled by A + Distance traveled by B = Total distance:\n"
        f"\\[ {v1}t + {v2}t = {dist} \\]\n\n"
        f"**Step 2: Solve for t**\n"
        f"\\[ {v1 + v2}t = {dist} \\]\n"
        f"\\[ t = \\frac{{{dist}}}{{{v1 + v2}}} = {t} \\text{{ hours}} \\]\n\n"
        f"**Distance Car A traveled:**\n"
        f"\\[ \\text{{Distance}} = {v1} \\times {t} = {v1 * t} \\text{{ km}} \\]"
    )
    ans = f"1. {v1}t + {v2}t = {dist}; 2. t = {t} hours, Car A distance = {v1 * t} km"
    return {
        "id": f"g8_eq3_sdt_opp_{rng.randint(100000, 999999)}",
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
        "subskill": "32_speed_distance_time_opposing_directions",
        "learning_objective_id": "math_g8_eq3_sdt_opposing",
        "hints": {
            "tier_1": f"Distance = Speed × Time. Total distance = {dist} km.",
            "tier_2": f"({v1} + {v2})t = {dist}.",
            "tier_3": f"t = {t} hours; Car A distance = {v1 * t} km.",
        },
        "misconception_tags": ["subtracting_speeds_when_approaching"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 33. Speed Distance Time Same Direction Catch Up
# ----------------------------------------------------------------------
def arch_33_speed_distance_time_same_direction_catch_up(rng: random.Random) -> Dict[str, Any]:
    v_slow = rng.choice([60, 75])
    head_start_hours = rng.choice([1, 2])
    v_fast = v_slow + rng.choice([25, 30])
    # v_fast * t = v_slow * (t + head_start_hours)
    # (v_fast - v_slow) * t = v_slow * head_start_hours
    # Choose clean integer t
    lead_dist = v_slow * head_start_hours
    diff_speed = v_fast - v_slow
    # Adjust to integer
    t = math.ceil(lead_dist / diff_speed)
    lead_dist = diff_speed * t
    head_start_hours = lead_dist // v_slow
    if head_start_hours == 0:
        head_start_hours = 1
        v_slow = 60
        v_fast = 90
        t = 2

    prompt = (
        f"A truck departs a depot traveling at **{v_slow} km/h**. "
        f"**{head_start_hours} hour(s)** later, a courier car leaves the same depot traveling in the same direction at **{v_fast} km/h**.\n\n"
        f"1. Let \\(t\\) be the time in hours that the courier car has been driving. Set up an equation representing when the courier overtakes the truck.\n"
        f"2. Solve for \\(t\\)."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"Truck travel time = \\(t + {head_start_hours}\\) hours.\n"
        f"Distance truck = Distance courier:\n"
        f"\\[ {v_fast}t = {v_slow}(t + {head_start_hours}) \\]\n\n"
        f"**Step 2: Solve for t**\n"
        f"\\[ {v_fast}t = {v_slow}t + {v_slow * head_start_hours} \\]\n"
        f"\\[ {v_fast - v_slow}t = {v_slow * head_start_hours} \\]\n"
        f"\\[ t = \\frac{{{v_slow * head_start_hours}}}{{{v_fast - v_slow}}} = {t} \\text{{ hours}} \\]"
    )
    ans = f"1. {v_fast}t = {v_slow}(t + {head_start_hours}); 2. t = {t} hours"
    return {
        "id": f"g8_eq3_catchup_{rng.randint(100000, 999999)}",
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
        "subskill": "33_speed_distance_time_same_direction_catch_up",
        "learning_objective_id": "math_g8_eq3_sdt_catchup",
        "hints": {
            "tier_1": f"Courier distance = Truck distance.",
            "tier_2": f"{v_fast}t = {v_slow}(t + {head_start_hours}).",
            "tier_3": f"t = {t} hours.",
        },
        "misconception_tags": ["adding_headstart_to_faster_vehicle"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 34. Money Saving Target Weekly Deposit
# ----------------------------------------------------------------------
def arch_34_money_saving_target_weekly_deposit(rng: random.Random) -> Dict[str, Any]:
    s0 = rng.choice([250, 400, 500, 650])
    deposit = rng.choice([75, 120, 150, 200])
    weeks = rng.choice([8, 10, 12, 16])
    target = s0 + deposit * weeks

    prompt = (
        f"Sipho has **R{s0}** saved in his account and decides to save an additional **R{deposit}** each week.\n\n"
        f"1. Write an algebraic equation for the number of weeks \\(w\\) needed to save a total of **R{target}**.\n"
        f"2. Solve your equation for \\(w\\)."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {s0} + {deposit}w = {target} \\]\n\n"
        f"**Step 2: Solve for w**\n"
        f"\\[ {deposit}w = {target} - {s0} = {target - s0} \\]\n"
        f"\\[ w = \\frac{{{target - s0}}}{{{deposit}}} = {weeks} \\text{{ weeks}} \\]"
    )
    ans = f"1. {s0} + {deposit}w = {target}; 2. w = {weeks} weeks"
    return {
        "id": f"g8_eq3_savings_{rng.randint(100000, 999999)}",
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
        "subskill": "34_money_saving_target_weekly_deposit",
        "learning_objective_id": "math_g8_eq3_saving_milestone",
        "hints": {
            "tier_1": f"Initial savings + (Weekly deposit × weeks) = Target.",
            "tier_2": f"{deposit}w = {target - s0}.",
            "tier_3": f"w = {weeks} weeks.",
        },
        "misconception_tags": ["dividing_target_directly_without_subtracting_initial"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 35. Commercial Discount And Vat Equation
# ----------------------------------------------------------------------
def arch_35_commercial_discount_and_vat_equation(rng: random.Random) -> Dict[str, Any]:
    disc_percent = rng.choice([10, 20, 25, 30])
    orig_price = rng.choice([200, 350, 400, 500, 600])
    multiplier = (100 - disc_percent) / 100
    sale_price = int(orig_price * multiplier)

    prompt = (
        f"An item was discounted by **{disc_percent}%** during a seasonal sale and sold for **R{sale_price}**.\n\n"
        f"1. Let the original marked price be \\(P\\). Set up an algebraic equation relating \\(P\\) and the sale price.\n"
        f"2. Solve for \\(P\\) to determine the original marked price."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"Paying \\({100 - disc_percent}\\%\\) of original price \\(P\\):\n"
        f"\\[ {multiplier}P = {sale_price} \\quad \\text{{or}} \\quad \\frac{{{100 - disc_percent}}}{{100}}P = {sale_price} \\]\n\n"
        f"**Step 2: Solve for P**\n"
        f"\\[ P = \\frac{{{sale_price}}}{{{multiplier}}} = R{orig_price} \\]"
    )
    ans = f"1. {multiplier}P = {sale_price}; 2. P = R{orig_price}"
    return {
        "id": f"g8_eq3_discount_{rng.randint(100000, 999999)}",
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
        "subskill": "35_commercial_discount_and_vat_equation",
        "learning_objective_id": "math_g8_eq3_commercial_discount",
        "hints": {
            "tier_1": f"If discount is {disc_percent}%, the customer pays {100 - disc_percent}%.",
            "tier_2": f"{multiplier} × P = {sale_price}.",
            "tier_3": f"P = {sale_price} ÷ {multiplier} = R{orig_price}.",
        },
        "misconception_tags": ["adding_discount_percentage_to_sale_price"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 36. Water Reservoir Inflow Outflow Balance
# ----------------------------------------------------------------------
def arch_36_water_reservoir_inflow_outflow_balance(rng: random.Random) -> Dict[str, Any]:
    v0 = rng.choice([1200, 1500, 2000, 2400])
    inflow = rng.choice([80, 100, 120])
    outflow = rng.choice([30, 40, 50])
    net_inflow = inflow - outflow
    hours = rng.choice([5, 8, 10, 12])
    target = v0 + net_inflow * hours

    prompt = (
        f"A municipal water reservoir initially holds **{v0} liters** of water. "
        f"Water flows into the reservoir at **{inflow} L/h** while being pumped out at **{outflow} L/h**.\n\n"
        f"1. Write an algebraic formula for the water volume \\(V\\) after \\(t\\) hours.\n"
        f"2. Solve an equation to find how many hours it will take for the reservoir to contain **{target} liters**."
    )
    sol = (
        f"**Step 1: Net inflow rate and formula**\n"
        f"Net rate = \\({inflow} - {outflow} = {net_inflow} \\text{{ L/h}}\\).\n"
        f"\\[ V = {v0} + {net_inflow}t \\]\n\n"
        f"**Step 2: Solve equation**\n"
        f"\\[ {v0} + {net_inflow}t = {target} \\]\n"
        f"\\[ {net_inflow}t = {target - v0} \\]\n"
        f"\\[ t = \\frac{{{target - v0}}}{{{net_inflow}}} = {hours} \\text{{ hours}} \\]"
    )
    ans = f"1. V = {v0} + {net_inflow}t; 2. t = {hours} hours"
    return {
        "id": f"g8_eq3_reservoir_{rng.randint(100000, 999999)}",
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
        "subskill": "36_water_reservoir_inflow_outflow_balance",
        "learning_objective_id": "math_g8_eq3_reservoir_balance",
        "hints": {
            "tier_1": f"Net rate = Inflow - Outflow = {inflow} - {outflow} = {net_inflow} L/h.",
            "tier_2": f"{v0} + {net_inflow}t = {target}.",
            "tier_3": f"t = {hours} hours.",
        },
        "misconception_tags": ["adding_outflow_to_inflow"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 37. Perimeter Composite Shape Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_37_perimeter_composite_shape_algebraic(rng: random.Random) -> Dict[str, Any]:
    ans_x = rng.choice([4, 5, 6, 8])
    a_len = rng.choice([2, 3])
    b_len = rng.choice([1, 3, 5])
    d_wid = rng.choice([2, 4])
    # Length = a_len*x + b_len, Width = x + d_wid
    # Perimeter = 2*(a_len*x + b_len) + 2*(x + d_wid) = (2*a_len + 2)x + (2*b_len + 2*d_wid)
    coeff_x = 2 * a_len + 2
    const_p = 2 * b_len + 2 * d_wid
    p = coeff_x * ans_x + const_p

    length_lbl = f"{a_len}x + {b_len}"
    width_lbl = f"x + {d_wid}"
    seed_val = rng.randint(100, 999999)
    svg = draw_algebraic_shape_perimeter_svg(
        "rectangle",
        [length_lbl, width_lbl, length_lbl, width_lbl],
        title=f"Perimeter Model (P = {p} m)",
        seed=seed_val,
    )

    prompt = (
        f"A rectangular garden plot has side lengths expressed algebraically as \\({length_lbl}\\) meters and \\({width_lbl}\\) meters.\n\n"
        f"The total perimeter of the garden is **{p} meters**.\n\n"
        f"1. Write an algebraic equation for the perimeter \\(P\\) in terms of \\(x\\).\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Calculate the actual numerical dimensions (length and width) of the plot."
    )
    l_val = a_len * ans_x + b_len
    w_val = ans_x + d_wid
    sol = (
        f"**Step 1: Set up perimeter equation**\n"
        f"\\[ P = 2(\\text{{length}}) + 2(\\text{{width}}) \\]\n"
        f"\\[ 2({length_lbl}) + 2({width_lbl}) = {p} \\]\n"
        f"\\[ {2 * a_len}x + {2 * b_len} + 2x + {2 * d_wid} = {p} \\]\n"
        f"\\[ {coeff_x}x + {const_p} = {p} \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {coeff_x}x = {p} - {const_p} = {p - const_p} \\]\n"
        f"\\[ x = \\frac{{{p - const_p}}}{{{coeff_x}}} = {ans_x} \\]\n\n"
        f"**Step 3: Actual dimensions**\n"
        f"Length \\(= {a_len}({ans_x}) + {b_len} = {l_val} \\text{{ m}}\\)\n"
        f"Width \\(= {ans_x} + {d_wid} = {w_val} \\text{{ m}}\\)\n"
        f"Check: \\(2({l_val}) + 2({w_val}) = {2 * l_val + 2 * w_val} = {p}\\)."
    )
    ans = f"1. {coeff_x}x + {const_p} = {p}; 2. x = {ans_x}; 3. Length = {l_val} m, Width = {w_val} m"
    return {
        "id": f"g8_eq3_perim_rect_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "subskill": "37_perimeter_composite_shape_algebraic",
        "learning_objective_id": "math_g8_eq3_perimeter_algebraic",
        "hints": {
            "tier_1": f"Perimeter = 2(length + width).",
            "tier_2": f"2(2x + 1) + 2(x + 3) = 6x + 8 = {p}.",
            "tier_3": f"x = {ans_x}; Length = {l_val} m, Width = {w_val} m.",
        },
        "misconception_tags": ["adding_length_and_width_only_once_for_perimeter"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 38. Area Rectangle Algebraic Dimensions
# ----------------------------------------------------------------------
def arch_38_area_rectangle_algebraic_dimensions(rng: random.Random) -> Dict[str, Any]:
    w = rng.choice([5, 6, 8, 10])
    extra = rng.choice([3, 4, 5])
    # Length is w + extra. Perimeter = 2*(w + w + extra) = 4w + 2*extra
    p = 4 * w + 2 * extra
    area = w * (w + extra)

    prompt = (
        f"The length of a rectangle is **{extra} cm** longer than its width \\(w\\). "
        f"The perimeter of the rectangle is **{p} cm**.\n\n"
        f"1. Set up an equation in terms of \\(w\\) and solve for the width.\n"
        f"2. Calculate the area of the rectangle in \\(\\text{{cm}}^2\\)."
    )
    sol = (
        f"**Step 1: Set up and solve equation**\n"
        f"Width = \\(w\\), Length = \\(w + {extra}\\).\n"
        f"\\[ 2(w + w + {extra}) = {p} \\]\n"
        f"\\[ 2(2w + {extra}) = {p} \\]\n"
        f"\\[ 4w + {2 * extra} = {p} \\]\n"
        f"\\[ 4w = {p - 2 * extra} \\]\n"
        f"\\[ w = \\frac{{{p - 2 * extra}}}{{4}} = {w} \\text{{ cm}} \\]\n\n"
        f"**Step 2: Area**\n"
        f"Length \\(= {w} + {extra} = {w + extra} \\text{{ cm}}\\).\n"
        f"\\[ \\text{{Area}} = \\text{{length}} \\times \\text{{width}} = {w + extra} \\times {w} = {area} \\text{{ cm}}^2 \\]"
    )
    ans = f"1. w = {w} cm (length = {w + extra} cm); 2. Area = {area} cm²"
    return {
        "id": f"g8_eq3_area_dim_{rng.randint(100000, 999999)}",
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
        "subskill": "38_area_rectangle_algebraic_dimensions",
        "learning_objective_id": "math_g8_eq3_area_dimensions",
        "hints": {
            "tier_1": f"Perimeter = 2(w + w + {extra}) = 4w + {2 * extra}.",
            "tier_2": f"4w = {p - 2 * extra}, so w = {w} cm.",
            "tier_3": f"Area = {w} × {w + extra} = {area} cm².",
        },
        "misconception_tags": ["confusing_perimeter_formula_with_area_formula"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 39. Fraction Equation Bracket In Numerator
# ----------------------------------------------------------------------
def arch_39_fraction_equation_bracket_in_numerator(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    c = rng.choice([3, 5, 7])
    ans_x = rng.choice([2, 4, 5, 6])
    b = rng.choice([1, 2, 3])
    # a*(ans_x + b) must be divisible by c, or let d be integer
    # d = a*(ans_x + b) // c
    # Let d be chosen first
    d = rng.choice([2, 4, 6])
    # a*(ans_x + b) = c * d => ans_x = (c*d - a*b)/a
    # To make ans_x an integer, c*d must be divisible by a
    cd = c * d
    while (cd - a * b) % a != 0 or (cd - a * b) // a <= 0:
        d += 1
        cd = c * d
    ans_x = (cd - a * b) // a

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\frac{{{a}(x + {b})}}{{{c}}} = {d} \\]"
    )
    sol = (
        f"**Step 1:** Multiply both sides by {c} to clear the denominator:\n"
        f"\\[ {a}(x + {b}) = {d} \\times {c} = {c * d} \\]\n\n"
        f"**Step 2:** Expand the bracket or divide by {a}:\n"
        f"Dividing both sides by {a}:\n"
        f"\\[ x + {b} = \\frac{{{c * d}}}{{{a}}} = {c * d // a} \\]\n\n"
        f"**Step 3:** Subtract {b} from both sides:\n"
        f"\\[ x = {c * d // a} - {b} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_frac_brk_{rng.randint(100000, 999999)}",
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
        "subskill": "39_fraction_equation_bracket_in_numerator",
        "learning_objective_id": "math_g8_eq3_fraction_bracket_num",
        "hints": {
            "tier_1": f"Multiply both sides by {c}.",
            "tier_2": f"{a}(x + {b}) = {c * d}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["expanding_before_clearing_denominator"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 40. Fraction Equation Variable In Denominator Simple
# ----------------------------------------------------------------------
def arch_40_fraction_equation_variable_in_denominator_simple(rng: random.Random) -> Dict[str, Any]:
    ans_x = rng.choice([2, 3, 4, 5, 6])
    c = rng.choice([3, 4, 7, 8])
    k = ans_x * c

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\frac{{{k}}}{{x}} = {c} \\]"
    )
    sol = (
        f"**Step 1:** Multiply both sides by \\(x\\) (where \\(x \\neq 0\\)):\n"
        f"\\[ {k} = {c}x \\]\n\n"
        f"**Step 2:** Divide both sides by {c}:\n"
        f"\\[ x = \\frac{{{k}}}{{{c}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_denom_var_{rng.randint(100000, 999999)}",
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
        "subskill": "40_fraction_equation_variable_in_denominator_simple",
        "learning_objective_id": "math_g8_eq3_var_denominator",
        "hints": {
            "tier_1": f"Multiply both sides by x to get x out of the denominator.",
            "tier_2": f"{k} = {c}x.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["multiplying_k_by_c"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 41. Fraction Equation Variable In Denominator Two Step
# ----------------------------------------------------------------------
def arch_41_fraction_equation_variable_in_denominator_two_step(rng: random.Random) -> Dict[str, Any]:
    ans_x = rng.choice([2, 3, 5, 7])
    a = rng.choice([1, 2, 3])
    c = rng.choice([2, 4, 5])
    k = c * (ans_x + a)

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\frac{{{k}}}{{x + {a}}} = {c} \\]"
    )
    sol = (
        f"**Step 1:** Multiply both sides by \\((x + {a})\\):\n"
        f"\\[ {k} = {c}(x + {a}) \\]\n\n"
        f"**Step 2:** Divide both sides by {c}:\n"
        f"\\[ \\frac{{{k}}}{{{c}}} = x + {a} \\]\n"
        f"\\[ {k // c} = x + {a} \\]\n\n"
        f"**Step 3:** Subtract {a} from both sides:\n"
        f"\\[ x = {k // c} - {a} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_denom_2step_{rng.randint(100000, 999999)}",
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
        "subskill": "41_fraction_equation_variable_in_denominator_two_step",
        "learning_objective_id": "math_g8_eq3_denom_binomial",
        "hints": {
            "tier_1": f"Multiply both sides by (x + {a}).",
            "tier_2": f"{k} = {c}(x + {a}), so x + {a} = {k // c}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["splitting_denominator_into_separate_fractions"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 42. Identity Equation Infinite Solutions Proof
# ----------------------------------------------------------------------
def arch_42_identity_equation_infinite_solutions_proof(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.choice([3, 5, 7])
    c = rng.choice([4, 6, 8])
    const = a * b + c

    prompt = (
        f"Solve the following equation and interpret the result:\n"
        f"\\[ {a}(x + {b}) + {c} = {a}x + {const} \\]"
    )
    sol = (
        f"**Step 1:** Expand the LHS bracket:\n"
        f"\\[ {a}x + {a * b} + {c} = {a}x + {const} \\]\n"
        f"\\[ {a}x + {const} = {a}x + {const} \\]\n\n"
        f"**Step 2:** Subtract \\({a}x\\) from both sides:\n"
        f"\\[ {const} = {const} \\quad \\text{{or}} \\quad 0x = 0 \\]\n\n"
        f"**Interpretation:**\n"
        f"Since this statement is true for **any** value of \\(x\\), the equation is an **identity**.\n"
        f"Solution: **All real numbers** (infinitely many solutions, \\(x \\in \\mathbb{{R}}\\))."
    )
    ans = "All real numbers (identity, infinitely many solutions)"
    return {
        "id": f"g8_eq3_identity_{rng.randint(100000, 999999)}",
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
        "subskill": "42_identity_equation_infinite_solutions_proof",
        "learning_objective_id": "math_g8_eq3_identity_solutions",
        "hints": {
            "tier_1": f"Expand LHS: {a}x + {a * b} + {c}.",
            "tier_2": f"Both sides are identical: {a}x + {const} = {a}x + {const}.",
            "tier_3": f"0 = 0 is always true, so x can be any real number.",
        },
        "misconception_tags": ["concluding_x_equals_0_when_0x_equals_0"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 43. Contradiction Equation No Solution Proof
# ----------------------------------------------------------------------
def arch_43_contradiction_equation_no_solution_proof(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    b = rng.choice([2, 4, 6])
    c = a * b + rng.choice([3, 5, 7])  # differs from a*b

    prompt = (
        f"Solve the following equation and interpret the result:\n"
        f"\\[ {a}(x + {b}) = {a}x + {c} \\]"
    )
    sol = (
        f"**Step 1:** Expand the LHS bracket:\n"
        f"\\[ {a}x + {a * b} = {a}x + {c} \\]\n\n"
        f"**Step 2:** Subtract \\({a}x\\) from both sides:\n"
        f"\\[ {a * b} = {c} \\quad \\text{{or}} \\quad 0x = {c - a * b} \\]\n\n"
        f"**Interpretation:**\n"
        f"Since \\({a * b} \\neq {c}\\), this is a mathematical contradiction (false statement).\n"
        f"There is no value of \\(x\\) that can make this statement true.\n"
        f"Solution: **No solution** (empty set, \\(\\emptyset\\))."
    )
    ans = "No solution (contradiction, empty set)"
    return {
        "id": f"g8_eq3_contra_{rng.randint(100000, 999999)}",
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
        "subskill": "43_contradiction_equation_no_solution_proof",
        "learning_objective_id": "math_g8_eq3_contradiction_no_sol",
        "hints": {
            "tier_1": f"Expand LHS: {a}x + {a * b}.",
            "tier_2": f"Subtract {a}x from both sides: {a * b} = {c}.",
            "tier_3": f"{a * b} does not equal {c}, so there is no solution.",
        },
        "misconception_tags": ["concluding_x_equals_0_when_contradiction_arises"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 44. Diagnosing Distributive Sign Error
# ----------------------------------------------------------------------
def arch_44_diagnosing_distributive_sign_error(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([3, 4, 5])
    c = rng.choice([12, 15, 20])

    prompt = (
        f"A learner solved the equation \\(10 - (x - {b}) = {c}\\) through the following working:\n\n"
        f"**Step 1:** \\(10 - x - {b} = {c}\\)\n"
        f"**Step 2:** \\({10 - b} - x = {c}\\)\n"
        f"**Step 3:** \\(-x = {c} - {10 - b}\\)\n"
        f"**Step 4:** \\(x = -({c - (10 - b)})\\)\n\n"
        f"1. Identify which step contains the fatal algebraic error.\n"
        f"2. Explain what the learner did wrong.\n"
        f"3. Provide the correct solution for \\(x\\)."
    )
    correct_step1 = f"10 - x + {b} = {c}"
    correct_ans_x = 10 + b - c
    sol = (
        f"**Step 1: Error Identification**\n"
        f"The error occurred in **Step 1**.\n\n"
        f"**Step 2: Explanation**\n"
        f"The learner failed to distribute the negative sign to the second term inside the bracket:\n"
        f"\\[ - (x - {b}) = -x + {b} \\]\n"
        f"The learner wrote \\(-{b}\\) instead of \\(+{b}\\).\n\n"
        f"**Step 3: Correct Solution**\n"
        f"\\[ 10 - x + {b} = {c} \\]\n"
        f"\\[ {10 + b} - x = {c} \\]\n"
        f"\\[ -x = {c} - {10 + b} = {c - (10 + b)} \\]\n"
        f"\\[ x = {correct_ans_x} \\]"
    )
    ans = f"1. Step 1; 2. -(-{b}) should be +{b}; 3. x = {correct_ans_x}"
    return {
        "id": f"g8_eq3_diag_sign_{rng.randint(100000, 999999)}",
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
        "subskill": "44_diagnosing_distributive_sign_error",
        "learning_objective_id": "math_g8_eq3_diag_distributive_sign",
        "hints": {
            "tier_1": f"Check the signs when removing the bracket preceded by a minus.",
            "tier_2": f"-(x - {b}) = -x + {b}.",
            "tier_3": f"Error in Step 1. Correct x = {correct_ans_x}.",
        },
        "misconception_tags": ["failing_to_distribute_negative_over_subtraction"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 45. Diagnosing Fraction Clearing Common Error
# ----------------------------------------------------------------------
def arch_45_diagnosing_fraction_clearing_common_error(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5])
    a = rng.choice([2, 5])
    b = rng.choice([6, 8, 10])

    prompt = (
        f"A learner attempted to solve \\(\\frac{{x}}{{{d}}} + {a} = {b}\\) as follows:\n\n"
        f"**Step 1:** \\(x + {a} = {b * d}\\)\n"
        f"**Step 2:** \\(x = {b * d} - {a} = {b * d - a}\\)\n\n"
        f"1. In which step did the learner make a conceptual error?\n"
        f"2. Explain what fundamental rule of equations was violated.\n"
        f"3. Calculate the correct solution."
    )
    correct_ans_x = d * (b - a)
    sol = (
        f"**Step 1: Error Identification**\n"
        f"The error occurred in **Step 1**.\n\n"
        f"**Step 2: Explanation**\n"
        f"When multiplying both sides of an equation by a denominator (here {d}), **every term** on both sides must be multiplied by {d}.\n"
        f"The learner multiplied \\(\\frac{{x}}{{{d}}}\\) and \\({b}\\) by {d}, but forgot to multiply \\({a}\\) by {d}.\n"
        f"The correct expanded line is: \\(x + {a * d} = {b * d}\\).\n\n"
        f"**Step 3: Correct Solution**\n"
        f"\\[ \\frac{{x}}{{{d}}} = {b} - {a} = {b - a} \\]\n"
        f"\\[ x = ({b - a}) \\times {d} = {correct_ans_x} \\]"
    )
    ans = f"1. Step 1; 2. Forgot to multiply the term {a} by {d}; 3. x = {correct_ans_x}"
    return {
        "id": f"g8_eq3_diag_frac_{rng.randint(100000, 999999)}",
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
        "subskill": "45_diagnosing_fraction_clearing_common_error",
        "learning_objective_id": "math_g8_eq3_diag_fraction_clearing",
        "hints": {
            "tier_1": f"Every term on both sides must be multiplied by {d}.",
            "tier_2": f"The term {a} was not multiplied by {d}.",
            "tier_3": f"Correct solution: x = {correct_ans_x}.",
        },
        "misconception_tags": ["multiplying_only_some_terms_by_lcd"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 46. Equation With Mixed Decimals And Brackets
# ----------------------------------------------------------------------
def arch_46_equation_with_mixed_decimals_and_brackets(rng: random.Random) -> Dict[str, Any]:
    ans_x = rng.choice([4, 6, 8, 10])
    # 0,5(x + 4) = 0,2x + k => 0,5x + 2 = 0,2x + k => 0,3x = k - 2 => k = 0,3*ans_x + 2
    b = 4
    k = round(0.3 * ans_x + 2.0, 1)

    k_sa = str(k).replace(".", ",")

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ 0,5(x + {b}) = 0,2x + {k_sa} \\]"
    )
    sol = (
        f"**Step 1:** Expand the LHS bracket:\n"
        f"\\[ 0,5x + 0,5({b}) = 0,2x + {k_sa} \\]\n"
        f"\\[ 0,5x + 2 = 0,2x + {k_sa} \\]\n\n"
        f"**Step 2:** Group like terms:\n"
        f"\\[ 0,5x - 0,2x = {k_sa} - 2 \\]\n"
        f"\\[ 0,3x = {round(k - 2, 1):.1f}\\text{{ (or }}{round(k - 2, 1)}\\text{{)}} \\]\n\n"
        f"**Step 3:** Divide by 0,3:\n"
        f"\\[ x = \\frac{{{round(k - 2, 1)}}}{{0,3}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_dec_brk_{rng.randint(100000, 999999)}",
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
        "subskill": "46_equation_with_mixed_decimals_and_brackets",
        "learning_objective_id": "math_g8_eq3_decimal_brackets",
        "hints": {
            "tier_1": f"0,5(x + {b}) = 0,5x + 2.",
            "tier_2": f"0,3x = {round(k - 2, 1)}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["decimal_point_misplacement_in_division"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 47. Exponential Equation Fractional Base
# ----------------------------------------------------------------------
def arch_47_exponential_equation_fractional_base(rng: random.Random) -> Dict[str, Any]:
    base_denom = rng.choice([2, 3, 4])
    exp_val = rng.choice([2, 3, 4])
    denom_target = base_denom ** exp_val

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\left(\\frac{{1}}{{{base_denom}}}\\right)^x = \\frac{{1}}{{{denom_target}}} \\]"
    )
    sol = (
        f"**Step 1:** Express the RHS fraction as a power of \\(\\frac{{1}}{{{base_denom}}}\\):\n"
        f"\\[ \\frac{{1}}{{{denom_target}}} = \\left(\\frac{{1}}{{{base_denom}}}\\right)^{{{exp_val}}} \\]\n\n"
        f"**Step 2:** Equate exponents:\n"
        f"\\[ \\left(\\frac{{1}}{{{base_denom}}}\\right)^x = \\left(\\frac{{1}}{{{base_denom}}}\\right)^{{{exp_val}}} \\implies x = {exp_val} \\]"
    )
    ans = str(exp_val)
    return {
        "id": f"g8_eq3_exp_frac_{rng.randint(100000, 999999)}",
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
        "subskill": "47_exponential_equation_fractional_base",
        "learning_objective_id": "math_g8_eq3_exp_fraction_base",
        "hints": {
            "tier_1": f"Write 1/{denom_target} as (1/{base_denom})^n.",
            "tier_2": f"(1/{base_denom})^{exp_val} = 1/{denom_target}.",
            "tier_3": f"x = {exp_val}.",
        },
        "misconception_tags": ["inverting_fraction_without_negating_exponent"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 48. Exponential Equation With Root Powers
# ----------------------------------------------------------------------
def arch_48_exponential_equation_with_root_powers(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3])
    exp_val = rng.choice([2, 3, 4])
    val = base ** exp_val
    sq_val = val ** 2

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {base}^x = \\sqrt{{{sq_val}}} \\]"
    )
    sol = (
        f"**Step 1:** Evaluate the square root on the RHS:\n"
        f"\\[ \\sqrt{{{sq_val}}} = {val} \\]\n\n"
        f"**Step 2:** Express {val} as a power of base {base}:\n"
        f"\\[ {val} = {base}^{exp_val} \\]\n\n"
        f"**Step 3:** Equate exponents:\n"
        f"\\[ {base}^x = {base}^{exp_val} \\implies x = {exp_val} \\]"
    )
    ans = str(exp_val)
    return {
        "id": f"g8_eq3_exp_sqrt_{rng.randint(100000, 999999)}",
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
        "subskill": "48_exponential_equation_with_root_powers",
        "learning_objective_id": "math_g8_eq3_exp_square_root",
        "hints": {
            "tier_1": f"First calculate the square root of {sq_val}.",
            "tier_2": f"{base}^x = {val} = {base}^{exp_val}.",
            "tier_3": f"x = {exp_val}.",
        },
        "misconception_tags": ["dividing_by_2_instead_of_taking_square_root"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 49. Two Container Liquid Transfer Equation
# ----------------------------------------------------------------------
def arch_49_two_container_liquid_transfer_equation(rng: random.Random) -> Dict[str, Any]:
    # Tank A has va, Tank B has vb. Transfer x liters from A to B so Tank B has twice Tank A:
    # vb + x = 2*(va - x) => vb + x = 2*va - 2*x => 3*x = 2*va - vb => x = (2*va - vb)/3
    x = rng.choice([10, 15, 20, 25])
    va = rng.choice([60, 80, 100])
    vb = 2 * va - 3 * x

    prompt = (
        f"Tank A contains **{va} liters** of water and Tank B contains **{vb} liters** of water. "
        f"Water is poured from Tank A into Tank B until Tank B contains exactly **twice** as much water as Tank A.\n\n"
        f"1. Let \\(x\\) be the number of liters transferred. Write an algebraic equation modeling this situation.\n"
        f"2. Solve for \\(x\\) and state the final volume of water in Tank A."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"After transfer: Tank A = \\({va} - x\\); Tank B = \\({vb} + x\\).\n"
        f"Condition: Tank B = \\(2 \\times \\text{{Tank A}}\\):\n"
        f"\\[ {vb} + x = 2({va} - x) \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {vb} + x = {2 * va} - 2x \\]\n"
        f"\\[ x + 2x = {2 * va} - {vb} \\]\n"
        f"\\[ 3x = {2 * va - vb} \\]\n"
        f"\\[ x = \\frac{{{2 * va - vb}}}{{3}} = {x} \\text{{ liters}} \\]\n\n"
        f"**Final volume in Tank A:** \\({va} - {x} = {va - x} \\text{{ liters}}\\)."
    )
    ans = f"1. {vb} + x = 2({va} - x); 2. x = {x} liters (Tank A final = {va - x} L)"
    return {
        "id": f"g8_eq3_transfer_{rng.randint(100000, 999999)}",
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
        "subskill": "49_two_container_liquid_transfer_equation",
        "learning_objective_id": "math_g8_eq3_liquid_transfer",
        "hints": {
            "tier_1": f"After transfer, Tank A has {va} - x and Tank B has {vb} + x.",
            "tier_2": f"{vb} + x = 2({va} - x).",
            "tier_3": f"3x = {2 * va - vb}, so x = {x} L.",
        },
        "misconception_tags": ["subtracting_transfer_from_both_tanks"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 50. Algebraic Equations 3 Capstone Synthesis
# ----------------------------------------------------------------------
def arch_50_algebraic_equations_3_capstone_synthesis(rng: random.Random) -> Dict[str, Any]:
    c_trees = rng.choice([150, 200, 250])
    rate = rng.choice([20, 25, 30])
    target = c_trees + rate * rng.choice([10, 15, 20])
    days = (target - c_trees) // rate

    prompt = (
        f"**Comprehensive Synthesis: Agricultural Development Planning**\n\n"
        f"A commercial citrus farm has **{c_trees}** mature trees planted across its north block. "
        f"The nursery planting team plants **{rate}** new trees each working day.\n\n"
        f"1. Formulate a linear equation to find after how many working days \\(d\\) the north block will contain exactly **{target}** trees.\n"
        f"2. Solve your equation showing all inverse operations.\n"
        f"3. A second south block starts with **{c_trees + 200}** trees and expands by **{rate - 10}** trees per day. "
        f"Determine after how many days both blocks will have equal tree counts."
    )
    # c_trees + rate*d2 = (c_trees + 200) + (rate - 10)*d2
    # rate*d2 - (rate - 10)*d2 = 200 => 10*d2 = 200 => d2 = 20 days
    d2 = 20
    trees_equal = c_trees + rate * d2
    sol = (
        f"**Part 1 & 2: Milestone Equation**\n"
        f"\\[ {c_trees} + {rate}d = {target} \\]\n"
        f"\\[ {rate}d = {target} - {c_trees} = {target - c_trees} \\]\n"
        f"\\[ d = \\frac{{{target - c_trees}}}{{{rate}}} = {days} \\text{{ working days}} \\]\n\n"
        f"**Part 3: Break-Even Between North and South Blocks**\n"
        f"\\[ {c_trees} + {rate}d = {c_trees + 200} + {rate - 10}d \\]\n"
        f"\\[ {rate}d - {rate - 10}d = {c_trees + 200} - {c_trees} \\]\n"
        f"\\[ 10d = 200 \\implies d = 20 \\text{{ working days}} \\]\n"
        f"At 20 days, each block will hold **{trees_equal} trees**."
    )
    ans = f"1. {c_trees} + {rate}d = {target}; 2. d = {days} days; 3. d = 20 days ({trees_equal} trees)"
    return {
        "id": f"g8_eq3_capstone_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 6,
        "subskill": "50_algebraic_equations_3_capstone_synthesis",
        "learning_objective_id": "math_g8_eq3_capstone",
        "hints": {
            "tier_1": f"For Part 1: {c_trees} + {rate}d = {target}.",
            "tier_2": f"For Part 3: Equate north and south: {c_trees} + {rate}d = {c_trees + 200} + {rate - 10}d.",
            "tier_3": f"Part 2: {days} days; Part 3: 20 days.",
        },
        "misconception_tags": ["combining_unlike_terms", "sign_error_transposition"],
        "diagram_spec": None,
    }


BUILDERS_26_50: List[Callable[[random.Random], Dict[str, Any]]] = [
    arch_26_geometry_vertically_opposite_angles_algebraic,
    arch_27_geometry_triangle_interior_angles_algebraic,
    arch_28_geometry_isosceles_triangle_base_angles_algebraic,
    arch_29_geometry_exterior_angle_of_triangle_algebraic,
    arch_30_consecutive_integers_algebraic_sum_product_puzzle,
    arch_31_consecutive_even_integers_with_multiplier,
    arch_32_speed_distance_time_opposing_directions,
    arch_33_speed_distance_time_same_direction_catch_up,
    arch_34_money_saving_target_weekly_deposit,
    arch_35_commercial_discount_and_vat_equation,
    arch_36_water_reservoir_inflow_outflow_balance,
    arch_37_perimeter_composite_shape_algebraic,
    arch_38_area_rectangle_algebraic_dimensions,
    arch_39_fraction_equation_bracket_in_numerator,
    arch_40_fraction_equation_variable_in_denominator_simple,
    arch_41_fraction_equation_variable_in_denominator_two_step,
    arch_42_identity_equation_infinite_solutions_proof,
    arch_43_contradiction_equation_no_solution_proof,
    arch_44_diagnosing_distributive_sign_error,
    arch_45_diagnosing_fraction_clearing_common_error,
    arch_46_equation_with_mixed_decimals_and_brackets,
    arch_47_exponential_equation_fractional_base,
    arch_48_exponential_equation_with_root_powers,
    arch_49_two_container_liquid_transfer_equation,
    arch_50_algebraic_equations_3_capstone_synthesis,
]
