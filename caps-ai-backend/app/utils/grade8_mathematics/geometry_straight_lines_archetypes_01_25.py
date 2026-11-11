"""
Grade 8 Mathematics - Geometry of Straight Lines Archetypes (01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/03. Geometry of straight lines.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional

from .svg_diagrams import (
    draw_angles_on_line_svg,
    draw_parallel_lines_transversal_svg,
)


# ----------------------------------------------------------------------
# 01. Angles On Straight Line Numerical Two Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_01_angles_on_straight_line_numerical_two_angles(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([35, 45, 55, 65, 75, 115, 125, 135])
    ang2 = 180 - ang1
    var = rng.choice(["a", "x", "y", "m"])

    svg = draw_angles_on_line_svg(ang1, f"{ang1}°", f"{var}")

    prompt = (
        f"In the straight-line configuration shown below, line \\(AB\\) is a straight line intersected by ray \\(OC\\):\n\n"
        f"One of the adjacent angles measures **{ang1}^\\circ** and the adjacent angle is labeled \\({var}\\).\n\n"
        f"1. State the geometric reason connecting the two adjacent angles.\n"
        f"2. Set up an equation and calculate the size of \\({var}\\) in degrees."
    )
    sol = (
        f"**Step 1: Geometric Reason**\n"
        f"Adjacent angles on a straight line add up to \\(180^\\circ\\) (\\(\\text{{adj }} \\angle\\text{{s on a straight line}}\\)).\n\n"
        f"**Step 2: Set up equation and solve**\n"
        f"\\[ {var} + {ang1}^\\circ = 180^\\circ \\]\n"
        f"\\[ {var} = 180^\\circ - {ang1}^\\circ = {ang2}^\\circ \\]"
    )
    ans = f"1. adj angles on straight line = 180°; 2. {var} = {ang2}°"
    return {
        "id": f"g8_line_num2_{rng.randint(100000, 999999)}",
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
        "subskill": "01_angles_on_straight_line_numerical_two_angles",
        "learning_objective_id": "math_g8_lines_adj_angles_num",
        "hints": {
            "tier_1": f"Angles on a straight line add up to 180°.",
            "tier_2": f"{var} = 180° - {ang1}°.",
            "tier_3": f"{var} = {ang2}°.",
        },
        "misconception_tags": ["subtracting_from_90_instead_of_180", "omitting_geometric_reason"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 02. Angles On Straight Line Three Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_02_angles_on_straight_line_three_angles(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([40, 50, 60])
    ang2 = rng.choice([35, 45, 55])
    ang3 = 180 - (ang1 + ang2)
    var = "k"

    # SVG: show first angle and remainder
    svg = draw_angles_on_line_svg(ang1, f"{ang1}°", f"{ang2}° + {var}")

    prompt = (
        f"Three adjacent angles meet at point \\(O\\) along straight line \\(AB\\):\n\n"
        f"\\[ \\angle 1 = {ang1}^\\circ, \\quad \\angle 2 = {ang2}^\\circ, \\quad \\angle 3 = {var} \\]\n\n"
        f"1. Write down an equation connecting all three angles, with geometric reason.\n"
        f"2. Calculate the value of \\({var}\\) in degrees."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"Adjacent angles on a straight line sum to \\(180^\\circ\\) (\\(\\angle\\text{{s on a straight line}}\\):\n"
        f"\\[ {ang1}^\\circ + {ang2}^\\circ + {var} = 180^\\circ \\]\n"
        f"\\[ {ang1 + ang2}^\\circ + {var} = 180^\\circ \\]\n\n"
        f"**Step 2: Solve for k**\n"
        f"\\[ {var} = 180^\\circ - {ang1 + ang2}^\\circ = {ang3}^\\circ \\]"
    )
    ans = f"1. {ang1}° + {ang2}° + {var} = 180° (adj angles on straight line); 2. {var} = {ang3}°"
    return {
        "id": f"g8_line_num3_{rng.randint(100000, 999999)}",
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
        "subskill": "02_angles_on_straight_line_three_angles",
        "learning_objective_id": "math_g8_lines_three_angles_num",
        "hints": {
            "tier_1": f"All three angles on line AB add up to 180°.",
            "tier_2": f"{ang1 + ang2}° + {var} = 180°.",
            "tier_3": f"{var} = {ang3}°.",
        },
        "misconception_tags": ["adding_angles_to_360_for_straight_line"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 03. Perpendicular Lines Adjacent Supplementary (WITH SVG)
# ----------------------------------------------------------------------
def arch_03_perpendicular_lines_adjacent_supplementary(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([24, 32, 41, 56, 68])
    ang2 = 90 - ang1
    var = "x"

    svg = draw_angles_on_line_svg(90, "90°", f"{ang1}° + {var}")

    prompt = (
        f"A ray stands perpendicular to straight line \\(AB\\), dividing the right angle into two adjacent angles:\n\n"
        f"One acute angle is **{ang1}^\\circ** and the adjacent acute angle is labeled \\({var}\\).\n\n"
        f"1. State the relationship between complementary angles.\n"
        f"2. Solve for \\({var}\\) in degrees."
    )
    sol = (
        f"**Step 1: Complementary Angle Definition**\n"
        f"Complementary angles add up to \\(90^\\circ\\) (\\(\\text{{adj complementary }} \\angle\\text{{s}}\\)).\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {var} + {ang1}^\\circ = 90^\\circ \\]\n"
        f"\\[ {var} = 90^\\circ - {ang1}^\\circ = {ang2}^\\circ \\]"
    )
    ans = f"1. complementary angles add to 90°; 2. {var} = {ang2}°"
    return {
        "id": f"g8_line_perp_{rng.randint(100000, 999999)}",
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
        "subskill": "03_perpendicular_lines_adjacent_supplementary",
        "learning_objective_id": "math_g8_lines_perpendicular_adj",
        "hints": {
            "tier_1": f"The perpendicular symbol indicates a 90° angle.",
            "tier_2": f"{var} + {ang1}° = 90°.",
            "tier_3": f"{var} = {ang2}°.",
        },
        "misconception_tags": ["subtracting_from_180_instead_of_90_for_complementary"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 04. Angles On Straight Line Algebraic Linear (WITH SVG)
# ----------------------------------------------------------------------
def arch_04_angles_on_straight_line_algebraic_linear(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([20, 30, 40, 50, 60])
    # x + (x + k) = 180 => 2x = 180 - k
    ans_x = (180 - k) // 2
    ang1 = ans_x
    ang2 = ans_x + k

    svg = draw_angles_on_line_svg(ang1, "x", f"x + {k}°")

    prompt = (
        f"Two adjacent angles lie on a straight line: \\(\\angle 1 = x\\) and \\(\\angle 2 = x + {k}^\\circ\\).\n\n"
        f"1. Formulate an algebraic equation using the straight line theorem.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Calculate the actual size in degrees of both angles."
    )
    sol = (
        f"**Step 1: Formulate equation**\n"
        f"Adjacent angles on a straight line add up to \\(180^\\circ\\):\n"
        f"\\[ x + (x + {k}) = 180 \\]\n"
        f"\\[ 2x + {k} = 180 \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ 2x = 180 - {k} = {180 - k} \\]\n"
        f"\\[ x = \\frac{{{180 - k}}}{{2}} = {ans_x} \\]\n\n"
        f"**Step 3: Actual angle sizes**\n"
        f"\\(\\angle 1 = {ans_x}^\\circ\\) and \\(\\angle 2 = {ans_x} + {k} = {ang2}^\\circ\\).\n"
        f"Check: \\({ans_x}^\\circ + {ang2}^\\circ = 180^\\circ\\)."
    )
    ans = f"1. 2x + {k} = 180; 2. x = {ans_x}; 3. {ans_x}°, {ang2}°"
    return {
        "id": f"g8_line_alg_lin_{rng.randint(100000, 999999)}",
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
        "subskill": "04_angles_on_straight_line_algebraic_linear",
        "learning_objective_id": "math_g8_lines_alg_linear",
        "hints": {
            "tier_1": f"x + (x + {k}) = 180°.",
            "tier_2": f"2x = {180 - k}.",
            "tier_3": f"x = {ans_x}°, angles are {ans_x}° and {ang2}°.",
        },
        "misconception_tags": ["forgetting_to_combine_like_terms_2x"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 05. Angles On Straight Line Multipliers (WITH SVG)
# ----------------------------------------------------------------------
def arch_05_angles_on_straight_line_multipliers(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    c = rng.choice([1, 2, 3])
    total_coeff = a + c
    # total_coeff * x = 180
    while 180 % total_coeff != 0:
        c += 1
        total_coeff = a + c
    ans_x = 180 // total_coeff
    ang1 = a * ans_x
    ang2 = c * ans_x

    svg = draw_angles_on_line_svg(ang1, f"{a}x", f"{c}x")

    prompt = (
        f"Two adjacent angles on a straight line are given as \\({a}x\\) and \\({c}x\\):\n\n"
        f"1. Set up an equation and solve for \\(x\\).\n"
        f"2. Determine the measure of both angles."
    )
    sol = (
        f"**Step 1: Set up equation and solve**\n"
        f"\\[ {a}x + {c}x = 180 \\quad (\\text{{adj }} \\angle\\text{{s on straight line}}) \\]\n"
        f"\\[ {total_coeff}x = 180 \\]\n"
        f"\\[ x = \\frac{{180}}{{{total_coeff}}} = {ans_x} \\]\n\n"
        f"**Step 2: Angles**\n"
        f"First angle \\(= {a}({ans_x}) = {ang1}^\\circ\\)\n"
        f"Second angle \\(= {c}({ans_x}) = {ang2}^\\circ\\)"
    )
    ans = f"1. x = {ans_x}; 2. {ang1}°, {ang2}°"
    return {
        "id": f"g8_line_alg_mult_{rng.randint(100000, 999999)}",
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
        "subskill": "05_angles_on_straight_line_multipliers",
        "learning_objective_id": "math_g8_lines_alg_multipliers",
        "hints": {
            "tier_1": f"({a} + {c})x = 180°.",
            "tier_2": f"{total_coeff}x = 180°.",
            "tier_3": f"x = {ans_x}°; {ang1}° and {ang2}°.",
        },
        "misconception_tags": ["dividing_180_by_single_coefficient"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 06. Angles On Straight Line Binomial Expressions (WITH SVG)
# ----------------------------------------------------------------------
def arch_06_angles_on_straight_line_binomial_expressions(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    c = rng.choice([1, 2])
    ans_x = rng.choice([15, 20, 25, 30])
    b = rng.choice([10, 15, 20])
    d = 180 - (a + c) * ans_x - b
    if d < 5 or d > 50:
        ans_x = 20
        a, c, b = 2, 3, 15
        d = 180 - 5 * 20 - 15  # 65

    ang1 = a * ans_x + b
    ang2 = c * ans_x + d

    svg = draw_angles_on_line_svg(ang1, f"{a}x + {b}°", f"{c}x + {d}°")

    prompt = (
        f"Two adjacent angles on straight line \\(MN\\) are expressed as \\(({a}x + {b})^\\circ\\) and \\(({c}x + {d})^\\circ\\):\n\n"
        f"1. Set up an equation with geometric reason.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Calculate the size of the larger angle."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ ({a}x + {b}) + ({c}x + {d}) = 180 \\quad (\\text{{adj }} \\angle\\text{{s on str line}}) \\]\n"
        f"\\[ {a + c}x + {b + d} = 180 \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {a + c}x = 180 - {b + d} = {180 - (b + d)} \\]\n"
        f"\\[ x = \\frac{{{180 - (b + d)}}}{{{a + c}}} = {ans_x} \\]\n\n"
        f"**Step 3: Larger angle**\n"
        f"\\(\\angle 1 = {ang1}^\\circ\\); \\(\\angle 2 = {ang2}^\\circ\\).\n"
        f"The larger angle is **{max(ang1, ang2)}^\\circ**."
    )
    ans = f"1. {a + c}x + {b + d} = 180 (adj angles on straight line); 2. x = {ans_x}; 3. Larger angle = {max(ang1, ang2)}°"
    return {
        "id": f"g8_line_binom_{rng.randint(100000, 999999)}",
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
        "subskill": "06_angles_on_straight_line_binomial_expressions",
        "learning_objective_id": "math_g8_lines_binomial",
        "hints": {
            "tier_1": f"Combine like terms: ({a} + {c})x + ({b} + {d}) = 180°.",
            "tier_2": f"{a + c}x = {180 - (b + d)}.",
            "tier_3": f"x = {ans_x}, larger angle = {max(ang1, ang2)}°.",
        },
        "misconception_tags": ["sign_error_transposing_constants"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 07. Angles On Straight Line Three Algebraic Terms (WITH SVG)
# ----------------------------------------------------------------------
def arch_07_angles_on_straight_line_three_algebraic_terms(rng: random.Random) -> Dict[str, Any]:
    # a x + b x + c x = 180 => total * x = 180
    a, b, c = rng.choice([(1, 2, 3), (2, 3, 4), (1, 3, 5), (1, 2, 6)])
    total = a + b + c
    ans_x = 180 // total
    ang1 = a * ans_x
    ang2 = b * ans_x
    ang3 = c * ans_x

    svg = draw_angles_on_line_svg(ang1, f"{a}x", f"{b}x + {c}x")

    prompt = (
        f"Three angles lie adjacent along a straight line: \\({a}x\\), \\({b}x\\), and \\({c}x\\):\n\n"
        f"1. Formulate the equation and calculate \\(x\\).\n"
        f"2. Find the size in degrees of all three angles."
    )
    sol = (
        f"**Step 1: Formulate and solve**\n"
        f"\\[ {a}x + {b}x + {c}x = 180 \\quad (\\text{{adj }} \\angle\\text{{s on str line}}) \\]\n"
        f"\\[ {total}x = 180 \\implies x = {ans_x} \\]\n\n"
        f"**Step 2: Angles**\n"
        f"\\({a}({ans_x}) = {ang1}^\\circ\\), \\({b}({ans_x}) = {ang2}^\\circ\\), and \\({c}({ans_x}) = {ang3}^\\circ\\)."
    )
    ans = f"1. x = {ans_x}; 2. {ang1}°, {ang2}°, {ang3}°"
    return {
        "id": f"g8_line_3alg_{rng.randint(100000, 999999)}",
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
        "subskill": "07_angles_on_straight_line_three_algebraic_terms",
        "learning_objective_id": "math_g8_lines_three_algebraic",
        "hints": {
            "tier_1": f"Sum = ({a} + {b} + {c})x = 180°.",
            "tier_2": f"{total}x = 180°.",
            "tier_3": f"x = {ans_x}°; {ang1}°, {ang2}°, {ang3}°.",
        },
        "misconception_tags": ["omitting_one_of_the_angles_from_sum"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 08. Angles On Straight Line Mixed Terms And Constant (WITH SVG)
# ----------------------------------------------------------------------
def arch_08_angles_on_straight_line_mixed_terms_and_constant(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    b = rng.choice([1, 2])
    const = rng.choice([30, 40, 50])
    total_coeff = a + b
    ans_x = (180 - const) // total_coeff
    const = 180 - total_coeff * ans_x  # ensure exact integer

    ang1 = a * ans_x
    ang2 = b * ans_x + const

    svg = draw_angles_on_line_svg(ang1, f"{a}x", f"{b}x + {const}°")

    prompt = (
        f"Two adjacent angles on straight line \\(EF\\) are given as \\({a}x\\) and \\(({b}x + {const}^\\circ)\\):\n\n"
        f"1. Write an equation relating the angles.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Calculate the actual size of the angle \\(({b}x + {const}^\\circ)\\)."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {a}x + ({b}x + {const}) = 180 \\quad (\\text{{adj }} \\angle\\text{{s on str line}}) \\]\n"
        f"\\[ {total_coeff}x + {const} = 180 \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {total_coeff}x = 180 - {const} = {180 - const} \\]\n"
        f"\\[ x = \\frac{{{180 - const}}}{{{total_coeff}}} = {ans_x} \\]\n\n"
        f"**Step 3: Angle size**\n"
        f"\\[ {b}({ans_x}) + {const} = {ang2}^\\circ \\]"
    )
    ans = f"1. {total_coeff}x + {const} = 180; 2. x = {ans_x}; 3. {ang2}°"
    return {
        "id": f"g8_line_mixed_c_{rng.randint(100000, 999999)}",
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
        "subskill": "08_angles_on_straight_line_mixed_terms_and_constant",
        "learning_objective_id": "math_g8_lines_mixed_constant",
        "hints": {
            "tier_1": f"{a}x + {b}x + {const} = 180°.",
            "tier_2": f"{total_coeff}x = {180 - const}.",
            "tier_3": f"x = {ans_x}, angle = {ang2}°.",
        },
        "misconception_tags": ["adding_constant_to_180_instead_of_subtracting"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 09. Vertically Opposite Angles Numerical (WITH SVG)
# ----------------------------------------------------------------------
def arch_09_vertically_opposite_angles_numerical(rng: random.Random) -> Dict[str, Any]:
    known_ang = rng.choice([48, 62, 74, 85, 112, 126, 138])
    var = "y"

    svg = draw_angles_on_line_svg(known_ang, f"{known_ang}°", f"180° - {known_ang}°")

    prompt = (
        f"Two straight lines intersect at point \\(O\\). One of the angles formed is **{known_ang}^\\circ**, "
        f"and the angle directly vertically opposite to it is labeled \\({var}\\).\n\n"
        f"1. State the theorem relating vertically opposite angles.\n"
        f"2. Write down the value of \\({var}\\) with reason."
    )
    sol = (
        f"**Step 1: Geometric Theorem**\n"
        f"Vertically opposite angles are equal (\\(\\text{{vert. opp. }} \\angle\\text{{s are equal}}\\)).\n\n"
        f"**Step 2: Value of y**\n"
        f"\\[ {var} = {known_ang}^\\circ \\quad (\\text{{vert. opp. }} \\angle\\text{{s}}) \\]"
    )
    ans = f"1. vert opp angles are equal; 2. {var} = {known_ang}°"
    return {
        "id": f"g8_line_vert_num_{rng.randint(100000, 999999)}",
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
        "subskill": "09_vertically_opposite_angles_numerical",
        "learning_objective_id": "math_g8_lines_vert_opp_num",
        "hints": {
            "tier_1": f"Vertically opposite angles are always equal.",
            "tier_2": f"{var} = {known_ang}°.",
            "tier_3": f"{var} = {known_ang}° (vert opp angles).",
        },
        "misconception_tags": ["subtracting_from_180_for_vertically_opposite"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 10. Vertically Opposite Angles Full Revolution (WITH SVG)
# ----------------------------------------------------------------------
def arch_10_vertically_opposite_angles_full_revolution(rng: random.Random) -> Dict[str, Any]:
    known = rng.choice([65, 75, 80, 105, 115, 125])
    supp = 180 - known

    svg = draw_angles_on_line_svg(known, f"{known}°", f"{supp}°")

    prompt = (
        f"Two straight lines intersect at vertex \\(O\\), creating four angles: a known angle of **{known}^\\circ** "
        f"and three unknown angles labeled \\(a\\), \\(b\\), and \\(c\\) (where \\(b\\) is vertically opposite to {known}^\\circ).\n\n"
        f"Calculate the values of \\(a\\), \\(b\\), and \\(c\\), providing geometric reasons for each statement."
    )
    sol = (
        f"**Step 1: Find b (vertically opposite)**\n"
        f"\\[ b = {known}^\\circ \\quad (\\text{{vert. opp. }} \\angle\\text{{s}}) \\]\n\n"
        f"**Step 2: Find a (adjacent supplementary on straight line)**\n"
        f"\\[ a = 180^\\circ - {known}^\\circ = {supp}^\\circ \\quad (\\angle\\text{{s on a straight line}}) \\]\n\n"
        f"**Step 3: Find c (vertically opposite to a)**\n"
        f"\\[ c = a = {supp}^\\circ \\quad (\\text{{vert. opp. }} \\angle\\text{{s}}) \\]"
    )
    ans = f"a = {supp}°, b = {known}°, c = {supp}°"
    return {
        "id": f"g8_line_vert_rev_{rng.randint(100000, 999999)}",
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
        "subskill": "10_vertically_opposite_angles_full_revolution",
        "learning_objective_id": "math_g8_lines_full_intersection",
        "hints": {
            "tier_1": f"b is vertically opposite {known}°.",
            "tier_2": f"a and {known}° lie on a straight line: a = 180° - {known}°.",
            "tier_3": f"a = {supp}°, b = {known}°, c = {supp}°.",
        },
        "misconception_tags": ["confusing_adjacent_and_opposite_angles"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 11. Vertically Opposite Angles Algebraic One Step (WITH SVG)
# ----------------------------------------------------------------------
def arch_11_vertically_opposite_angles_algebraic_one_step(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    ans_x = rng.choice([16, 22, 24, 28, 32])
    target = a * ans_x

    svg = draw_angles_on_line_svg(target, f"{a}x", f"180° - {target}°")

    prompt = (
        f"Two intersecting lines form vertically opposite angles labeled \\({a}x\\) and **{target}^\\circ**:\n\n"
        f"1. Set up an equation with reason.\n"
        f"2. Solve for \\(x\\)."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {a}x = {target} \\quad (\\text{{vert. opp. }} \\angle\\text{{s}}) \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ x = \\frac{{{target}}}{{{a}}} = {ans_x} \\]"
    )
    ans = f"1. {a}x = {target} (vert opp angles); 2. x = {ans_x}"
    return {
        "id": f"g8_line_vert_1step_{rng.randint(100000, 999999)}",
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
        "subskill": "11_vertically_opposite_angles_algebraic_one_step",
        "learning_objective_id": "math_g8_lines_vert_alg_1step",
        "hints": {
            "tier_1": f"Equate: {a}x = {target}°.",
            "tier_2": f"Divide by {a}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["adding_angles_to_180_instead_of_equating"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 12. Vertically Opposite Angles Algebraic Two Step (WITH SVG)
# ----------------------------------------------------------------------
def arch_12_vertically_opposite_angles_algebraic_two_step(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.choice([12, 18, 24, 30])
    ans_x = rng.choice([15, 20, 25])
    target = a * ans_x + b

    svg = draw_angles_on_line_svg(target, f"{a}x + {b}°", f"180° - {target}°")

    prompt = (
        f"Two intersecting straight lines form vertically opposite angles given as \\(({a}x + {b})^\\circ\\) and **{target}^\\circ**:\n\n"
        f"1. Set up an equation with reason.\n"
        f"2. Solve for \\(x\\)."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {a}x + {b} = {target} \\quad (\\text{{vert. opp. }} \\angle\\text{{s}}) \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {a}x = {target} - {b} = {target - b} \\]\n"
        f"\\[ x = \\frac{{{target - b}}}{{{a}}} = {ans_x} \\]"
    )
    ans = f"1. {a}x + {b} = {target} (vert opp angles); 2. x = {ans_x}"
    return {
        "id": f"g8_line_vert_2step_{rng.randint(100000, 999999)}",
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
        "subskill": "12_vertically_opposite_angles_algebraic_two_step",
        "learning_objective_id": "math_g8_lines_vert_alg_2step",
        "hints": {
            "tier_1": f"{a}x + {b} = {target}°.",
            "tier_2": f"{a}x = {target - b}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["adding_constants_instead_of_subtracting"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 13. Vertically Opposite Angles Variables Both Sides (WITH SVG)
# ----------------------------------------------------------------------
def arch_13_vertically_opposite_angles_variables_both_sides(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([4, 5])
    c = rng.choice([2, 3])
    ans_x = rng.choice([15, 20, 25])
    b = rng.choice([10, 15])
    # a*ans_x - b = c*ans_x + d => d = (a - c)*ans_x - b
    d = (a - c) * ans_x - b
    ang_val = a * ans_x - b

    svg = draw_angles_on_line_svg(ang_val, f"{a}x - {b}°", f"{c}x + {d}°")

    prompt = (
        f"Two intersecting lines form vertically opposite angles: \\(({a}x - {b})^\\circ\\) and \\(({c}x + {d})^\\circ\\):\n\n"
        f"1. Set up an equation with reason.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Calculate the actual size in degrees of both angles."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {a}x - {b} = {c}x + {d} \\quad (\\text{{vert. opp. }} \\angle\\text{{s}}) \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {a}x - {c}x = {d} + {b} \\]\n"
        f"\\[ {a - c}x = {d + b} \\]\n"
        f"\\[ x = \\frac{{{d + b}}}{{{a - c}}} = {ans_x} \\]\n\n"
        f"**Step 3: Actual angle size**\n"
        f"\\[ {a}({ans_x}) - {b} = {ang_val}^\\circ \\]"
    )
    ans = f"1. {a}x - {b} = {c}x + {d} (vert opp angles); 2. x = {ans_x}; 3. {ang_val}°"
    return {
        "id": f"g8_line_vert_both_{rng.randint(100000, 999999)}",
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
        "subskill": "13_vertically_opposite_angles_variables_both_sides",
        "learning_objective_id": "math_g8_lines_vert_variables_both",
        "hints": {
            "tier_1": f"Equate: {a}x - {b} = {c}x + {d}.",
            "tier_2": f"({a} - {c})x = {d + b}.",
            "tier_3": f"x = {ans_x}, angle = {ang_val}°.",
        },
        "misconception_tags": ["adding_angles_to_180_instead_of_equating"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 14. Intersecting Lines Perpendicular And Opposite (WITH SVG)
# ----------------------------------------------------------------------
def arch_14_intersecting_lines_perpendicular_and_opposite(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([25, 35, 45])
    comp = 90 - ang1

    svg = draw_angles_on_line_svg(90, "90°", f"{ang1}° + {comp}°")

    prompt = (
        f"Two straight lines \\(AB\\) and \\(CD\\) intersect at \\(O\\). A ray \\(OE\\) is drawn such that \\(OE \\perp AB\\).\n"
        f"If \\(\\angle AOE = 90^\\circ\\) and one adjacent angle to the ray is **{ang1}^\\circ**:\n\n"
        f"1. Calculate the complement angle \\(x\\) within the right angle.\n"
        f"2. Calculate the vertically opposite angle to \\(x\\)."
    )
    sol = (
        f"**Step 1: Complement angle**\n"
        f"\\[ x = 90^\\circ - {ang1}^\\circ = {comp}^\\circ \\quad (\\angle\\text{{s in right angle}}) \\]\n\n"
        f"**Step 2: Vertically opposite angle**\n"
        f"\\[ \\text{{Vert. opp. angle}} = x = {comp}^\\circ \\quad (\\text{{vert. opp. }} \\angle\\text{{s}}) \\]"
    )
    ans = f"1. x = {comp}°; 2. {comp}°"
    return {
        "id": f"g8_line_perp_opp_{rng.randint(100000, 999999)}",
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
        "subskill": "14_intersecting_lines_perpendicular_and_opposite",
        "learning_objective_id": "math_g8_lines_perp_and_opposite",
        "hints": {
            "tier_1": f"Within the right angle, x + {ang1}° = 90°.",
            "tier_2": f"x = {comp}°.",
            "tier_3": f"Vertically opposite angle is also {comp}°.",
        },
        "misconception_tags": ["confusing_perpendicular_with_straight_line_sum"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 15. Identifying Transversal And Angle Pairs (WITH SVG)
# ----------------------------------------------------------------------
def arch_15_identifying_transversal_and_angle_pairs(rng: random.Random) -> Dict[str, Any]:
    angle_deg = rng.choice([60, 65, 70])
    lbls = {
        "top_acute_left": "a",
        "top_obtuse_right": "b",
        "top_obtuse_left": "c",
        "top_acute_right": "d",
        "bot_acute_left": "e",
        "bot_obtuse_right": "f",
        "bot_obtuse_left": "g",
        "bot_acute_right": "h",
    }
    svg = draw_parallel_lines_transversal_svg(angle_deg, lbls)

    prompt = (
        f"In the parallel lines and transversal configuration below (where \\(AB \\parallel CD\\)):\n\n"
        f"1. Identify the letter of the angle that is **corresponding** to angle \\(a\\).\n"
        f"2. Identify the angle that is **alternate interior** to angle \\(d\\).\n"
        f"3. Identify the angle that is **co-interior** with angle \\(d\\)."
    )
    sol = (
        f"**1. Corresponding angle to a:**\n"
        f"Angle \\(a\\) is top-left of line 1; the matching position on line 2 is **\\(e\\)**.\n\n"
        f"**2. Alternate interior angle to d:**\n"
        f"Angle \\(d\\) is interior right; the alternate interior angle on the opposite side is **\\(c\\)** (or \\(g\\) depending on labeling: \\(c\\) and \\(d\\) alternate with \\(f\\) and \\(e\\)). Specifically, \\(d\\) and **\\(g\\)** are alternate interior.\n\n"
        f"**3. Co-interior angle to d:**\n"
        f"Co-interior angles lie on the same side between parallel lines: \\(d\\) and **\\(f\\)**."
    )
    ans = "1. e; 2. g; 3. f"
    return {
        "id": f"g8_line_trans_id_{rng.randint(100000, 999999)}",
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
        "subskill": "15_identifying_transversal_and_angle_pairs",
        "learning_objective_id": "math_g8_lines_transversal_classify",
        "hints": {
            "tier_1": f"Corresponding = F-shape; Alternate = Z-shape; Co-interior = U-shape.",
            "tier_2": f"Corresponding to a is e.",
            "tier_3": f"1. e; 2. g; 3. f.",
        },
        "misconception_tags": ["confusing_alternate_and_corresponding_positions"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 16. Parallel Lines Corresponding Angles Numerical (WITH SVG)
# ----------------------------------------------------------------------
def arch_16_parallel_lines_corresponding_angles_numerical(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([55, 65, 75, 80, 110, 120])
    lbls = {
        "top_acute_left": f"{ang}°",
        "bot_acute_left": "x",
    }
    svg = draw_parallel_lines_transversal_svg(ang if ang < 90 else 180 - ang, lbls)

    prompt = (
        f"Two parallel lines \\(AB \\parallel CD\\) are intersected by transversal \\(EF\\). "
        f"One acute angle is **{ang}^\\circ** and its corresponding angle is labeled \\(x\\).\n\n"
        f"State the value of \\(x\\) and give the correct formal geometric reason."
    )
    sol = (
        f"**Step 1: Value and reason**\n"
        f"\\[ x = {ang}^\\circ \\quad (\\text{{corresp. }} \\angle\\text{{s, }} AB \\parallel CD) \\]"
    )
    ans = f"x = {ang}° (corresp. angles, AB || CD)"
    return {
        "id": f"g8_line_corresp_num_{rng.randint(100000, 999999)}",
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
        "subskill": "16_parallel_lines_corresponding_angles_numerical",
        "learning_objective_id": "math_g8_lines_corresp_num",
        "hints": {
            "tier_1": f"Corresponding angles on parallel lines are equal.",
            "tier_2": f"Always state the parallel lines in your reason: corresp ∠s, AB || CD.",
            "tier_3": f"x = {ang}°.",
        },
        "misconception_tags": ["omitting_parallel_line_names_in_reason"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 17. Parallel Lines Alternate Interior Angles Numerical (WITH SVG)
# ----------------------------------------------------------------------
def arch_17_parallel_lines_alternate_interior_angles_numerical(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([52, 64, 72, 84])
    lbls = {
        "top_acute_right": f"{ang}°",
        "bot_acute_left": "m",
    }
    svg = draw_parallel_lines_transversal_svg(ang, lbls)

    prompt = (
        f"Given \\(AB \\parallel CD\\) intersected by transversal \\(PQ\\), where alternate interior angles are **{ang}^\\circ** and \\(m\\):\n\n"
        f"Write down the value of \\(m\\) and state the complete geometric reason."
    )
    sol = (
        f"**Step 1: Value and reason**\n"
        f"\\[ m = {ang}^\\circ \\quad (\\text{{alt. }} \\angle\\text{{s, }} AB \\parallel CD) \\]"
    )
    ans = f"m = {ang}° (alt. angles, AB || CD)"
    return {
        "id": f"g8_line_alt_num_{rng.randint(100000, 999999)}",
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
        "subskill": "17_parallel_lines_alternate_interior_angles_numerical",
        "learning_objective_id": "math_g8_lines_alt_num",
        "hints": {
            "tier_1": f"Alternate interior angles (Z-angles) are equal when lines are parallel.",
            "tier_2": f"m = {ang}°.",
            "tier_3": f"m = {ang}° (alt ∠s, AB || CD).",
        },
        "misconception_tags": ["omitting_parallel_line_names_in_reason"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 18. Parallel Lines Cointerior Angles Numerical (WITH SVG)
# ----------------------------------------------------------------------
def arch_18_parallel_lines_cointerior_angles_numerical(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([65, 75, 80, 110, 120])
    supp = 180 - ang
    lbls = {
        "top_acute_right": f"{ang}°",
        "bot_obtuse_right": "y",
    }
    svg = draw_parallel_lines_transversal_svg(ang if ang < 90 else 180 - ang, lbls)

    prompt = (
        f"Lines \\(AB\\) and \\(CD\\) are parallel (\\(AB \\parallel CD\\)). "
        f"Two co-interior angles on the right side of the transversal measure **{ang}^\\circ** and \\(y\\).\n\n"
        f"1. State the relationship between co-interior angles on parallel lines.\n"
        f"2. Calculate \\(y\\) giving the geometric reason."
    )
    sol = (
        f"**Step 1: Co-interior angle theorem**\n"
        f"Co-interior angles add up to \\(180^\\circ\\) (\\(\\text{{co-int. }} \\angle\\text{{s, }} AB \\parallel CD\\)).\n\n"
        f"**Step 2: Calculate y**\n"
        f"\\[ y + {ang}^\\circ = 180^\\circ \\]\n"
        f"\\[ y = 180^\\circ - {ang}^\\circ = {supp}^\\circ \\quad (\\text{{co-int. }} \\angle\\text{{s, }} AB \\parallel CD) \\]"
    )
    ans = f"1. co-interior angles sum to 180°; 2. y = {supp}° (co-int. angles, AB || CD)"
    return {
        "id": f"g8_line_coint_num_{rng.randint(100000, 999999)}",
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
        "subskill": "18_parallel_lines_cointerior_angles_numerical",
        "learning_objective_id": "math_g8_lines_coint_num",
        "hints": {
            "tier_1": f"Co-interior angles on parallel lines are supplementary (sum to 180°).",
            "tier_2": f"y = 180° - {ang}°.",
            "tier_3": f"y = {supp}° (co-int ∠s, AB || CD).",
        },
        "misconception_tags": ["equating_cointerior_angles_instead_of_summing_to_180"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 19. Parallel Lines Alternate Exterior Angles Numerical (WITH SVG)
# ----------------------------------------------------------------------
def arch_19_parallel_lines_alternate_exterior_angles_numerical(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([58, 68, 76, 82])
    lbls = {
        "top_acute_left": f"{ang}°",
        "bot_acute_right": "z",
    }
    svg = draw_parallel_lines_transversal_svg(ang, lbls)

    prompt = (
        f"In the figure where \\(AB \\parallel CD\\), angles measuring **{ang}^\\circ** and \\(z\\) are alternate exterior angles.\n\n"
        f"State the value of \\(z\\) with reason."
    )
    sol = (
        f"**Step 1: Value and reason**\n"
        f"\\[ z = {ang}^\\circ \\quad (\\text{{alt. ext. }} \\angle\\text{{s, }} AB \\parallel CD) \\]"
    )
    ans = f"z = {ang}° (alt. ext. angles, AB || CD)"
    return {
        "id": f"g8_line_altext_num_{rng.randint(100000, 999999)}",
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
        "subskill": "19_parallel_lines_alternate_exterior_angles_numerical",
        "learning_objective_id": "math_g8_lines_altext_num",
        "hints": {
            "tier_1": f"Alternate exterior angles on parallel lines are equal.",
            "tier_2": f"z = {ang}°.",
            "tier_3": f"z = {ang}° (alt ext ∠s, AB || CD).",
        },
        "misconception_tags": ["confusing_exterior_with_interior"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 20. Parallel Lines Corresponding Angles Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_20_parallel_lines_corresponding_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4])
    c = rng.choice([1, 2])
    ans_x = rng.choice([15, 20, 25])
    b = rng.choice([5, 10])
    # a*ans_x - b = c*ans_x + d => d = (a - c)*ans_x - b
    d = (a - c) * ans_x - b
    ang_val = a * ans_x - b

    lbls = {
        "top_acute_left": f"{a}x - {b}°",
        "bot_acute_left": f"{c}x + {d}°",
    }
    svg = draw_parallel_lines_transversal_svg(ang_val if ang_val < 90 else 180 - ang_val, lbls)

    prompt = (
        f"Two parallel lines \\(AB \\parallel CD\\) are cut by a transversal. "
        f"Two corresponding angles are labeled \\(({a}x - {b})^\\circ\\) and \\(({c}x + {d})^\\circ\\):\n\n"
        f"1. Set up an equation with reason.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Calculate the actual size in degrees of both angles."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {a}x - {b} = {c}x + {d} \\quad (\\text{{corresp. }} \\angle\\text{{s, }} AB \\parallel CD) \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {a}x - {c}x = {d} + {b} \\]\n"
        f"\\[ {a - c}x = {d + b} \\]\n"
        f"\\[ x = \\frac{{{d + b}}}{{{a - c}}} = {ans_x} \\]\n\n"
        f"**Step 3: Actual angle size**\n"
        f"\\[ {a}({ans_x}) - {b} = {ang_val}^\\circ \\]"
    )
    ans = f"1. {a}x - {b} = {c}x + {d} (corresp angles, AB || CD); 2. x = {ans_x}; 3. {ang_val}°"
    return {
        "id": f"g8_line_corresp_alg_{rng.randint(100000, 999999)}",
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
        "subskill": "20_parallel_lines_corresponding_angles_algebraic",
        "learning_objective_id": "math_g8_lines_corresp_algebraic",
        "hints": {
            "tier_1": f"Corresponding angles are equal: {a}x - {b} = {c}x + {d}.",
            "tier_2": f"({a} - {c})x = {d + b}.",
            "tier_3": f"x = {ans_x}, angle = {ang_val}°.",
        },
        "misconception_tags": ["adding_angles_to_180_for_corresponding"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 21. Parallel Lines Alternate Angles Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_21_parallel_lines_alternate_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5])
    c = rng.choice([1, 2])
    ans_x = rng.choice([15, 20, 25])
    b = rng.choice([10, 20])
    d = (a - c) * ans_x - b
    ang_val = a * ans_x - b

    lbls = {
        "top_acute_right": f"{a}x - {b}°",
        "bot_acute_left": f"{c}x + {d}°",
    }
    svg = draw_parallel_lines_transversal_svg(ang_val, lbls)

    prompt = (
        f"Lines \\(AB\\) and \\(CD\\) are parallel (\\(AB \\parallel CD\\)). "
        f"Alternate interior angles are given as \\(({a}x - {b})^\\circ\\) and \\(({c}x + {d})^\\circ\\):\n\n"
        f"1. Set up an equation with reason.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Find the angle size in degrees."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {a}x - {b} = {c}x + {d} \\quad (\\text{{alt. }} \\angle\\text{{s, }} AB \\parallel CD) \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ {a - c}x = {d + b} \\]\n"
        f"\\[ x = \\frac{{{d + b}}}{{{a - c}}} = {ans_x} \\]\n\n"
        f"**Step 3: Angle size**\n"
        f"\\[ {a}({ans_x}) - {b} = {ang_val}^\\circ \\]"
    )
    ans = f"1. {a}x - {b} = {c}x + {d} (alt angles, AB || CD); 2. x = {ans_x}; 3. {ang_val}°"
    return {
        "id": f"g8_line_alt_alg_{rng.randint(100000, 999999)}",
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
        "subskill": "21_parallel_lines_alternate_angles_algebraic",
        "learning_objective_id": "math_g8_lines_alt_algebraic",
        "hints": {
            "tier_1": f"Alternate angles are equal: {a}x - {b} = {c}x + {d}.",
            "tier_2": f"({a} - {c})x = {d + b}.",
            "tier_3": f"x = {ans_x}, angle = {ang_val}°.",
        },
        "misconception_tags": ["setting_sum_to_180_for_alternate_angles"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 22. Parallel Lines Cointerior Angles Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_22_parallel_lines_cointerior_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    c = rng.choice([1, 2])
    ans_x = rng.choice([20, 25, 30])
    b = rng.choice([10, 15])
    d = 180 - (a + c) * ans_x - b
    if d < 5 or d > 60:
        ans_x = 25
        a, c, b = 2, 2, 10
        d = 70

    ang1 = a * ans_x + b
    ang2 = c * ans_x + d

    lbls = {
        "top_acute_right": f"{a}x + {b}°",
        "bot_obtuse_right": f"{c}x + {d}°",
    }
    svg = draw_parallel_lines_transversal_svg(ang1, lbls)

    prompt = (
        f"In the diagram, line \\(AB \\parallel CD\\). Two co-interior angles are labeled \\(({a}x + {b})^\\circ\\) and \\(({c}x + {d})^\\circ\\):\n\n"
        f"1. State the theorem for co-interior angles between parallel lines.\n"
        f"2. Formulate and solve an equation for \\(x\\).\n"
        f"3. Calculate the size of the obtuse angle."
    )
    sol = (
        f"**Step 1: Co-interior angle theorem**\n"
        f"Co-interior angles add up to \\(180^\\circ\\) (\\(\\text{{co-int. }} \\angle\\text{{s, }} AB \\parallel CD\\)).\n\n"
        f"**Step 2: Formulate and solve**\n"
        f"\\[ ({a}x + {b}) + ({c}x + {d}) = 180 \\]\n"
        f"\\[ {a + c}x + {b + d} = 180 \\]\n"
        f"\\[ {a + c}x = 180 - {b + d} = {180 - (b + d)} \\]\n"
        f"\\[ x = \\frac{{{180 - (b + d)}}}{{{a + c}}} = {ans_x} \\]\n\n"
        f"**Step 3: Obtuse angle**\n"
        f"\\(\\angle 1 = {ang1}^\\circ\\), \\(\\angle 2 = {ang2}^\\circ\\).\n"
        f"The obtuse angle is **{max(ang1, ang2)}^\\circ**."
    )
    ans = f"1. co-interior angles sum to 180°; 2. x = {ans_x}; 3. {max(ang1, ang2)}°"
    return {
        "id": f"g8_line_coint_alg_{rng.randint(100000, 999999)}",
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
        "subskill": "22_parallel_lines_cointerior_angles_algebraic",
        "learning_objective_id": "math_g8_lines_coint_algebraic",
        "hints": {
            "tier_1": f"Co-interior angles add up to 180°.",
            "tier_2": f"{a + c}x + {b + d} = 180°.",
            "tier_3": f"x = {ans_x}, obtuse angle = {max(ang1, ang2)}°.",
        },
        "misconception_tags": ["equating_cointerior_angles"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 23. Parallel Lines Cointerior Multipliers (WITH SVG)
# ----------------------------------------------------------------------
def arch_23_parallel_lines_cointerior_multipliers(rng: random.Random) -> Dict[str, Any]:
    a, c = rng.choice([(2, 3), (1, 4), (1, 5), (3, 7)])
    total = a + c
    ans_x = 180 // total
    ang1 = a * ans_x
    ang2 = c * ans_x

    lbls = {
        "top_acute_right": f"{a}x",
        "bot_obtuse_right": f"{c}x",
    }
    svg = draw_parallel_lines_transversal_svg(ang1, lbls)

    prompt = (
        f"Given \\(AB \\parallel CD\\), two co-interior angles on the right side of the transversal are \\({a}x\\) and \\({c}x\\):\n\n"
        f"1. Set up an equation with reason.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. State the size in degrees of both angles."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {a}x + {c}x = 180 \\quad (\\text{{co-int. }} \\angle\\text{{s, }} AB \\parallel CD) \\]\n"
        f"\\[ {total}x = 180 \\implies x = {ans_x} \\]\n\n"
        f"**Step 2: Calculate angles**\n"
        f"\\({a}({ans_x}) = {ang1}^\\circ\\) and \\({c}({ans_x}) = {ang2}^\\circ\\)."
    )
    ans = f"1. {total}x = 180 (co-int angles, AB || CD); 2. x = {ans_x}; 3. {ang1}°, {ang2}°"
    return {
        "id": f"g8_line_coint_mult_{rng.randint(100000, 999999)}",
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
        "subskill": "23_parallel_lines_cointerior_multipliers",
        "learning_objective_id": "math_g8_lines_coint_multipliers",
        "hints": {
            "tier_1": f"{a}x + {c}x = 180°.",
            "tier_2": f"{total}x = 180°.",
            "tier_3": f"x = {ans_x}°; {ang1}°, {ang2}°.",
        },
        "misconception_tags": ["equating_cointerior_multipliers"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 24. Parallel Lines Two Step Deduction Corresp And Straight (WITH SVG)
# ----------------------------------------------------------------------
def arch_24_parallel_lines_two_step_deduction_corresp_and_straight(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([60, 70, 75, 80])
    supp = 180 - ang

    lbls = {
        "top_acute_left": f"{ang}°",
        "bot_acute_left": "x",
        "bot_obtuse_right": "y",
    }
    svg = draw_parallel_lines_transversal_svg(ang, lbls)

    prompt = (
        f"In the figure with \\(AB \\parallel CD\\), an angle of **{ang}^\\circ** is given on line \\(AB\\). "
        f"Angle \\(x\\) is corresponding on line \\(CD\\), and angle \\(y\\) is adjacent to \\(x\\) on line \\(CD\\):\n\n"
        f"1. Find \\(x\\) with geometric reason.\n"
        f"2. Find \\(y\\) with geometric reason."
    )
    sol = (
        f"**Step 1: Find x**\n"
        f"\\[ x = {ang}^\\circ \\quad (\\text{{corresp. }} \\angle\\text{{s, }} AB \\parallel CD) \\]\n\n"
        f"**Step 2: Find y**\n"
        f"Angles \\(x\\) and \\(y\\) lie on straight line \\(CD\\):\n"
        f"\\[ y = 180^\\circ - x = 180^\\circ - {ang}^\\circ = {supp}^\\circ \\quad (\\angle\\text{{s on str line}}) \\]"
    )
    ans = f"1. x = {ang}° (corresp angles, AB || CD); 2. y = {supp}° (angles on straight line)"
    return {
        "id": f"g8_line_2step_corresp_{rng.randint(100000, 999999)}",
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
        "subskill": "24_parallel_lines_two_step_deduction_corresp_and_straight",
        "learning_objective_id": "math_g8_lines_2step_corresp_str",
        "hints": {
            "tier_1": f"x is corresponding to {ang}°.",
            "tier_2": f"y + x = 180° on straight line CD.",
            "tier_3": f"x = {ang}°, y = {supp}°.",
        },
        "misconception_tags": ["omitting_reasons_for_intermediate_steps"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 25. Parallel Lines Two Step Deduction Alt And Opposite (WITH SVG)
# ----------------------------------------------------------------------
def arch_25_parallel_lines_two_step_deduction_alt_and_opposite(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([55, 65, 70, 85])
    supp = 180 - ang

    lbls = {
        "top_acute_right": f"{ang}°",
        "bot_acute_left": "p",
        "bot_obtuse_right": "q",
    }
    svg = draw_parallel_lines_transversal_svg(ang, lbls)

    prompt = (
        f"In the parallel lines diagram with \\(AB \\parallel CD\\), an angle of **{ang}^\\circ** is marked. "
        f"Angle \\(p\\) is alternate interior to it on line \\(CD\\), and angle \\(q\\) is vertically opposite to the adjacent supplementary angle:\n\n"
        f"1. Calculate \\(p\\) with reason.\n"
        f"2. Calculate \\(q\\) with reason."
    )
    sol = (
        f"**Step 1: Find p**\n"
        f"\\[ p = {ang}^\\circ \\quad (\\text{{alt. }} \\angle\\text{{s, }} AB \\parallel CD) \\]\n\n"
        f"**Step 2: Find q**\n"
        f"Angle \\(q\\) is co-interior with {ang}^\\circ (or supplementary to \\(p\\)):\n"
        f"\\[ q = 180^\\circ - {ang}^\\circ = {supp}^\\circ \\quad (\\text{{co-int. }} \\angle\\text{{s, }} AB \\parallel CD \\text{{ or }} \\angle\\text{{s on str line}}) \\]"
    )
    ans = f"1. p = {ang}° (alt angles, AB || CD); 2. q = {supp}° (co-int angles or straight line)"
    return {
        "id": f"g8_line_2step_alt_{rng.randint(100000, 999999)}",
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
        "subskill": "25_parallel_lines_two_step_deduction_alt_and_opposite",
        "learning_objective_id": "math_g8_lines_2step_alt_opp",
        "hints": {
            "tier_1": f"p alternates with {ang}°.",
            "tier_2": f"q = 180° - {ang}°.",
            "tier_3": f"p = {ang}°, q = {supp}°.",
        },
        "misconception_tags": ["confusing_alternate_and_cointerior"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


BUILDERS_01_25: List[Callable[[random.Random], Dict[str, Any]]] = [
    arch_01_angles_on_straight_line_numerical_two_angles,
    arch_02_angles_on_straight_line_three_angles,
    arch_03_perpendicular_lines_adjacent_supplementary,
    arch_04_angles_on_straight_line_algebraic_linear,
    arch_05_angles_on_straight_line_multipliers,
    arch_06_angles_on_straight_line_binomial_expressions,
    arch_07_angles_on_straight_line_three_algebraic_terms,
    arch_08_angles_on_straight_line_mixed_terms_and_constant,
    arch_09_vertically_opposite_angles_numerical,
    arch_10_vertically_opposite_angles_full_revolution,
    arch_11_vertically_opposite_angles_algebraic_one_step,
    arch_12_vertically_opposite_angles_algebraic_two_step,
    arch_13_vertically_opposite_angles_variables_both_sides,
    arch_14_intersecting_lines_perpendicular_and_opposite,
    arch_15_identifying_transversal_and_angle_pairs,
    arch_16_parallel_lines_corresponding_angles_numerical,
    arch_17_parallel_lines_alternate_interior_angles_numerical,
    arch_18_parallel_lines_cointerior_angles_numerical,
    arch_19_parallel_lines_alternate_exterior_angles_numerical,
    arch_20_parallel_lines_corresponding_angles_algebraic,
    arch_21_parallel_lines_alternate_angles_algebraic,
    arch_22_parallel_lines_cointerior_angles_algebraic,
    arch_23_parallel_lines_cointerior_multipliers,
    arch_24_parallel_lines_two_step_deduction_corresp_and_straight,
    arch_25_parallel_lines_two_step_deduction_alt_and_opposite,
]
