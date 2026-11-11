"""
Grade 8 Mathematics - Geometry of Straight Lines Archetypes (26 to 50).
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
    draw_triangle_angles_svg,
)


# ----------------------------------------------------------------------
# 26. Parallel Lines Three Parallel Lines (WITH SVG)
# ----------------------------------------------------------------------
def arch_26_parallel_lines_three_parallel_lines(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([60, 68, 72, 80])
    supp = 180 - ang

    lbls = {
        "top_acute_left": f"{ang}°",
        "bot_acute_left": "x",
        "bot_obtuse_right": "y",
    }
    svg = draw_parallel_lines_transversal_svg(ang, lbls)

    prompt = (
        f"Three horizontal lines \\(L_1 \\parallel L_2 \\parallel L_3\\) are intersected by a transversal line. "
        f"An angle of **{ang}^\\circ** is measured at the intersection with \\(L_1\\).\n\n"
        f"1. Determine angle \\(x\\) at \\(L_2\\) corresponding to the {ang}^\\circ angle.\n"
        f"2. Determine angle \\(y\\) at \\(L_3\\) that is co-interior with \\(x\\)."
    )
    sol = (
        f"**Step 1: Angle x**\n"
        f"\\[ x = {ang}^\\circ \\quad (\\text{{corresp. }} \\angle\\text{{s, }} L_1 \\parallel L_2) \\]\n\n"
        f"**Step 2: Angle y**\n"
        f"\\[ y = 180^\\circ - x = 180^\\circ - {ang}^\\circ = {supp}^\\circ \\quad (\\text{{co-int. }} \\angle\\text{{s, }} L_2 \\parallel L_3) \\]"
    )
    ans = f"1. x = {ang}° (corresp angles, L1 || L2); 2. y = {supp}° (co-int angles, L2 || L3)"
    return {
        "id": f"g8_line_3par_{rng.randint(100000, 999999)}",
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
        "subskill": "26_parallel_lines_three_parallel_lines",
        "learning_objective_id": "math_g8_lines_three_parallel",
        "hints": {
            "tier_1": f"Corresponding angles across all parallel lines are equal.",
            "tier_2": f"x = {ang}° (corresp ∠s).",
            "tier_3": f"y = 180° - {ang}° = {supp}° (co-int ∠s).",
        },
        "misconception_tags": ["assuming_non_adjacent_parallel_lines_lose_congruence"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 27. Parallel Lines Two Transversals (WITH SVG)
# ----------------------------------------------------------------------
def arch_27_parallel_lines_two_transversals(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([50, 60, 70])
    ang2 = rng.choice([40, 55, 65])
    supp1 = 180 - ang1
    supp2 = 180 - ang2

    lbls = {
        "top_acute_left": f"{ang1}°",
        "bot_acute_left": "x",
        "top_obtuse_right": f"{supp2}°",
        "bot_acute_right": "y",
    }
    svg = draw_parallel_lines_transversal_svg(ang1, lbls)

    prompt = (
        f"Two parallel lines \\(AB \\parallel CD\\) are crossed by two separate transversals \\(T_1\\) and \\(T_2\\). "
        f"Along \\(T_1\\), an angle of **{ang1}^\\circ** corresponds to \\(x\\). "
        f"Along \\(T_2\\), an alternate angle to \\(y\\) measures **{ang2}^\\circ**.\n\n"
        f"Find the values of \\(x\\) and \\(y\\), stating geometric reasons."
    )
    sol = (
        f"**Step 1: Calculate x**\n"
        f"\\[ x = {ang1}^\\circ \\quad (\\text{{corresp. }} \\angle\\text{{s, }} AB \\parallel CD) \\]\n\n"
        f"**Step 2: Calculate y**\n"
        f"\\[ y = {ang2}^\\circ \\quad (\\text{{alt. }} \\angle\\text{{s, }} AB \\parallel CD) \\]"
    )
    ans = f"x = {ang1}° (corresp angles, AB || CD), y = {ang2}° (alt angles, AB || CD)"
    return {
        "id": f"g8_line_2trans_{rng.randint(100000, 999999)}",
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
        "subskill": "27_parallel_lines_two_transversals",
        "learning_objective_id": "math_g8_lines_two_transversals",
        "hints": {
            "tier_1": f"Treat each transversal independently with parallel lines AB and CD.",
            "tier_2": f"x = {ang1}° (corresp ∠s).",
            "tier_3": f"y = {ang2}° (alt ∠s).",
        },
        "misconception_tags": ["mixing_angles_from_different_transversals"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 28. Proving Lines Parallel Via Corresponding Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_28_proving_lines_parallel_via_corresponding_angles(rng: random.Random) -> Dict[str, Any]:
    is_par = rng.choice([True, False])
    ang1 = rng.choice([64, 75, 82])
    ang2 = ang1 if is_par else ang1 + rng.choice([-5, 5, 8])

    lbls = {
        "top_acute_left": f"{ang1}°",
        "bot_acute_left": f"{ang2}°",
    }
    svg = draw_parallel_lines_transversal_svg(ang1, lbls)

    prompt = (
        f"Two straight lines \\(PQ\\) and \\(RS\\) are cut by transversal \\(TU\\). "
        f"Two corresponding angles measure **{ang1}^\\circ** and **{ang2}^\\circ**.\n\n"
        f"1. Are lines \\(PQ\\) and \\(RS\\) parallel? (Answer 'Yes' or 'No')\n"
        f"2. State the geometric condition (converse theorem) supporting your conclusion."
    )
    if is_par:
        sol = (
            f"**1. Answer:** Yes, \\(PQ \\parallel RS\\).\n\n"
            f"**2. Geometric Reason:**\n"
            f"Since the corresponding angles are equal (both measure \\({ang1}^\\circ\\)), the lines must be parallel "
            f"(\\(\\text{{corresp. }} \\angle\\text{{s are equal}}\\))."
        )
        ans = "1. Yes; 2. corresp. angles are equal"
    else:
        sol = (
            f"**1. Answer:** No, \\(PQ\\) is not parallel to \\(RS\\).\n\n"
            f"**2. Geometric Reason:**\n"
            f"The corresponding angles are not equal (\\({ang1}^\\circ \\neq {ang2}^\\circ\\)), so the lines cannot be parallel."
        )
        ans = "1. No; 2. corresp. angles are not equal"
    return {
        "id": f"g8_line_conv_corresp_{rng.randint(100000, 999999)}",
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
        "subskill": "28_proving_lines_parallel_via_corresponding_angles",
        "learning_objective_id": "math_g8_lines_prove_parallel_corresp",
        "hints": {
            "tier_1": f"Lines are parallel if and only if corresponding angles are equal.",
            "tier_2": f"Compare {ang1}° with {ang2}°.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["assuming_lines_look_parallel_without_checking_angles"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 29. Proving Lines Parallel Via Alternate Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_29_proving_lines_parallel_via_alternate_angles(rng: random.Random) -> Dict[str, Any]:
    is_par = rng.choice([True, False])
    ang1 = rng.choice([56, 68, 74])
    ang2 = ang1 if is_par else ang1 + rng.choice([-6, 6, 10])

    lbls = {
        "top_acute_right": f"{ang1}°",
        "bot_acute_left": f"{ang2}°",
    }
    svg = draw_parallel_lines_transversal_svg(ang1, lbls)

    prompt = (
        f"In a diagram with two lines cut by a transversal, alternate interior angles measure **{ang1}^\\circ** and **{ang2}^\\circ**.\n\n"
        f"Determine whether the two lines are parallel and justify your deduction with the converse alternate angle theorem."
    )
    if is_par:
        sol = (
            f"**Conclusion:** The lines are parallel (\\(\\text{{alt. }} \\angle\\text{{s are equal}}\\)).\n"
            f"Both alternate interior angles measure \\({ang1}^\\circ\\)."
        )
        ans = "Lines are parallel (alt. angles are equal)"
    else:
        sol = (
            f"**Conclusion:** The lines are NOT parallel.\n"
            f"Alternate interior angles are not equal (\\({ang1}^\\circ \\neq {ang2}^\\circ\\))."
        )
        ans = "Lines are not parallel (alt. angles are not equal)"
    return {
        "id": f"g8_line_conv_alt_{rng.randint(100000, 999999)}",
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
        "subskill": "29_proving_lines_parallel_via_alternate_angles",
        "learning_objective_id": "math_g8_lines_prove_parallel_alt",
        "hints": {
            "tier_1": f"Check if the alternate angles are equal.",
            "tier_2": f"{ang1}° versus {ang2}°.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["assuming_parallelism_without_angle_equality"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 30. Proving Lines Parallel Via Cointerior Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_30_proving_lines_parallel_via_cointerior_angles(rng: random.Random) -> Dict[str, Any]:
    is_par = rng.choice([True, False])
    ang1 = rng.choice([65, 75, 85])
    ang2 = (180 - ang1) if is_par else (180 - ang1 + rng.choice([-8, 8, 12]))
    total = ang1 + ang2

    lbls = {
        "top_acute_right": f"{ang1}°",
        "bot_obtuse_right": f"{ang2}°",
    }
    svg = draw_parallel_lines_transversal_svg(ang1, lbls)

    prompt = (
        f"Two co-interior angles between two lines cut by a transversal measure **{ang1}^\\circ** and **{ang2}^\\circ**.\n\n"
        f"1. Calculate the sum of the two co-interior angles.\n"
        f"2. Conclude whether the two lines are parallel, stating the geometric reason."
    )
    if is_par:
        sol = (
            f"**Step 1:** \\({ang1}^\\circ + {ang2}^\\circ = 180^\\circ\\).\n\n"
            f"**Step 2:** Yes, the lines are parallel because co-interior angles are supplementary "
            f"(\\(\\text{{co-int. }} \\angle\\text{{s sum to }} 180^\\circ\\))."
        )
        ans = "1. 180°; 2. Yes, lines are parallel (co-int angles are supplementary)"
    else:
        sol = (
            f"**Step 1:** \\({ang1}^\\circ + {ang2}^\\circ = {total}^\\circ\\).\n\n"
            f"**Step 2:** No, the lines are not parallel because \\({total}^\\circ \\neq 180^\\circ\\) "
            f"(\\(\\text{{co-int. }} \\angle\\text{{s are not supplementary}}\\))."
        )
        ans = f"1. {total}°; 2. No, lines are not parallel (co-int angles do not sum to 180°)"
    return {
        "id": f"g8_line_conv_coint_{rng.randint(100000, 999999)}",
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
        "subskill": "30_proving_lines_parallel_via_cointerior_angles",
        "learning_objective_id": "math_g8_lines_prove_parallel_coint",
        "hints": {
            "tier_1": f"Add the two co-interior angles: {ang1}° + {ang2}°.",
            "tier_2": f"Sum = {total}°.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["checking_if_cointerior_angles_are_equal_instead_of_supplementary"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 31. Angles Around A Point Revolution (WITH SVG)
# ----------------------------------------------------------------------
def arch_31_angles_around_a_point_revolution(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([80, 90, 100])
    a2 = rng.choice([70, 85, 95])
    a3 = rng.choice([60, 75, 80])
    a4 = 360 - (a1 + a2 + a3)

    svg = draw_angles_on_line_svg(a1, f"{a1}° + {a2}°", f"{a3}° + x")

    prompt = (
        f"Four angles meet at a common point \\(P\\) to form a complete revolution:\n\n"
        f"\\[ \\angle 1 = {a1}^\\circ, \\quad \\angle 2 = {a2}^\\circ, \\quad \\angle 3 = {a3}^\\circ, \\quad \\angle 4 = x \\]\n\n"
        f"1. State the theorem for angles around a common point.\n"
        f"2. Calculate the value of \\(x\\) in degrees."
    )
    sol = (
        f"**Step 1: Geometric Theorem**\n"
        f"Angles around a point add up to \\(360^\\circ\\) (\\(\\angle\\text{{s around a point}}\\)).\n\n"
        f"**Step 2: Calculate x**\n"
        f"\\[ {a1}^\\circ + {a2}^\\circ + {a3}^\\circ + x = 360^\\circ \\]\n"
        f"\\[ {a1 + a2 + a3}^\\circ + x = 360^\\circ \\]\n"
        f"\\[ x = 360^\\circ - {a1 + a2 + a3}^\\circ = {a4}^\\circ \\]"
    )
    ans = f"1. angles around a point = 360°; 2. x = {a4}°"
    return {
        "id": f"g8_line_rev_num_{rng.randint(100000, 999999)}",
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
        "subskill": "31_angles_around_a_point_revolution",
        "learning_objective_id": "math_g8_lines_around_point",
        "hints": {
            "tier_1": f"Angles around a point add up to 360°.",
            "tier_2": f"{a1 + a2 + a3}° + x = 360°.",
            "tier_3": f"x = {a4}°.",
        },
        "misconception_tags": ["adding_angles_around_point_to_180"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 32. Angles Around A Point Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_32_angles_around_a_point_algebraic(rng: random.Random) -> Dict[str, Any]:
    c1, c2, c3, c4 = rng.choice([(1, 2, 3, 4), (2, 3, 4, 3), (1, 3, 4, 4)])
    tot = c1 + c2 + c3 + c4
    ans_x = 360 // tot

    svg = draw_angles_on_line_svg(120, f"{c1}x + {c2}x", f"{c3}x + {c4}x")

    prompt = (
        f"Four angles around a point are expressed algebraically as \\({c1}x\\), \\({c2}x\\), \\({c3}x\\), and \\({c4}x\\):\n\n"
        f"1. Set up an equation using the revolution theorem.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Find the measure in degrees of the largest angle."
    )
    max_c = max(c1, c2, c3, c4)
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {c1}x + {c2}x + {c3}x + {c4}x = 360 \\quad (\\angle\\text{{s around a point}}) \\]\n"
        f"\\[ {tot}x = 360 \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ x = \\frac{{360}}{{{tot}}} = {ans_x} \\]\n\n"
        f"**Step 3: Largest angle**\n"
        f"\\[ {max_c} \\times {ans_x} = {max_c * ans_x}^\\circ \\]"
    )
    ans = f"1. {tot}x = 360; 2. x = {ans_x}; 3. {max_c * ans_x}°"
    return {
        "id": f"g8_line_rev_alg_{rng.randint(100000, 999999)}",
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
        "subskill": "32_angles_around_a_point_algebraic",
        "learning_objective_id": "math_g8_lines_around_point_alg",
        "hints": {
            "tier_1": f"Sum all four expressions and set equal to 360°.",
            "tier_2": f"{tot}x = 360°.",
            "tier_3": f"x = {ans_x}, largest angle = {max_c * ans_x}°.",
        },
        "misconception_tags": ["setting_revolution_sum_to_180"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 33. Triangle Angle Sum Straight Line Proof (WITH SVG)
# ----------------------------------------------------------------------
def arch_33_triangle_angle_sum_straight_line_proof(rng: random.Random) -> Dict[str, Any]:
    ang_a = rng.choice([40, 50, 60, 70])
    ang_b = rng.choice([45, 55, 65])
    ang_c = 180 - (ang_a + ang_b)
    svg = draw_triangle_angles_svg(ang_a, ang_b, ang_c, "A", "B", "C")

    prompt = (
        f"Consider \\(\\Delta ABC\\). A line \\(DE\\) is constructed through vertex \\(A\\) parallel to base \\(BC\\) (\\(DE \\parallel BC\\)):\n\n"
        f"1. Name the angle at \\(A\\) that is alternate to \\(\\hat{{B}}\\).\n"
        f"2. Name the angle at \\(A\\) that is alternate to \\(\\hat{{C}}\\).\n"
        f"3. Explain why \\(\\hat{{A}} + \\hat{{B}} + \\hat{{C}} = 180^\\circ\\) using angles on a straight line."
    )
    sol = (
        f"**1.** \\(\\angle DAB = \\hat{{B}}\\) (\\(\\text{{alt. }} \\angle\\text{{s, }} DE \\parallel BC\\)).\n\n"
        f"**2.** \\(\\angle EAC = \\hat{{C}}\\) (\\(\\text{{alt. }} \\angle\\text{{s, }} DE \\parallel BC\\)).\n\n"
        f"**3.** Since \\(DAE\\) is a straight line, the three adjacent angles at vertex \\(A\\) sum to \\(180^\\circ\\):\n"
        f"\\[ \\angle DAB + \\angle BAC + \\angle EAC = 180^\\circ \\quad (\\angle\\text{{s on str line}}) \\]\n"
        f"Substituting \\(\\hat{{B}}\\) and \\(\\hat{{C}}\\) into this equation:\n"
        f"\\[ \\hat{{B}} + \\hat{{A}} + \\hat{{C}} = 180^\\circ \\]"
    )
    ans = "1. DAB; 2. EAC; 3. DAB + BAC + EAC = 180° on straight line, substituting alternate angles"
    return {
        "id": f"g8_line_tri_proof_{rng.randint(100000, 999999)}",
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
        "subskill": "33_triangle_angle_sum_straight_line_proof",
        "learning_objective_id": "math_g8_lines_tri_sum_proof",
        "hints": {
            "tier_1": f"Use alternate interior angles between line DE and base BC.",
            "tier_2": f"Angles on straight line DAE add up to 180°.",
            "tier_3": f"Substitute the equal alternate angles into the straight line equation.",
        },
        "misconception_tags": ["confusing_alternate_and_corresponding_in_proof"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 34. Zig Zag Parallel Lines Auxiliary Line (WITH SVG)
# ----------------------------------------------------------------------
def arch_34_zig_zag_parallel_lines_auxiliary_line(rng: random.Random) -> Dict[str, Any]:
    # Parallel lines AB || CD with a reflex or acute vertex E between them
    # Angle at top = a1, angle at bottom = a2. Reflex angle = a1 + a2
    a1 = rng.choice([35, 42, 50])
    a2 = rng.choice([28, 36, 45])
    mid_angle = a1 + a2

    lbls = {
        "top_acute_right": f"{a1}°",
        "bot_acute_left": f"{a2}°",
    }
    svg = draw_parallel_lines_transversal_svg(a1, lbls)

    prompt = (
        f"Two parallel lines \\(AB \\parallel CD\\) enclose a zig-zag line \\(A-E-C\\).\n"
        f"If \\(\\angle BAE = {a1}^\\circ\\) and \\(\\angle DCE = {a2}^\\circ\\):\n\n"
        f"1. Describe the auxiliary construction line needed through vertex \\(E\\).\n"
        f"2. Calculate the size of reflex angle \\(\\angle AEC\\)."
    )
    sol = (
        f"**Step 1: Construction Line**\n"
        f"Construct an auxiliary line through vertex \\(E\\) parallel to both lines \\(AB\\) and \\(CD\\) (line \\(EF \\parallel AB \\parallel CD\\)).\n\n"
        f"**Step 2: Calculate angle AEC**\n"
        f"Upper half \\(\\angle AEF = \\angle BAE = {a1}^\\circ\\) (\\(\\text{{alt. }} \\angle\\text{{s, }} AB \\parallel EF\\)).\n"
        f"Lower half \\(\\angle FEC = \\angle DCE = {a2}^\\circ\\) (\\(\\text{{alt. }} \\angle\\text{{s, }} EF \\parallel CD\\)).\n"
        f"\\[ \\angle AEC = {a1}^\\circ + {a2}^\\circ = {mid_angle}^\\circ \\]"
    )
    ans = f"1. Draw auxiliary line through E parallel to AB and CD; 2. {mid_angle}°"
    return {
        "id": f"g8_line_zigzag_{rng.randint(100000, 999999)}",
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
        "subskill": "34_zig_zag_parallel_lines_auxiliary_line",
        "learning_objective_id": "math_g8_lines_zigzag_auxiliary",
        "hints": {
            "tier_1": f"Draw a horizontal parallel line through point E.",
            "tier_2": f"The angle at E splits into two alternate angles.",
            "tier_3": f"{a1}° + {a2}° = {mid_angle}°.",
        },
        "misconception_tags": ["subtracting_angles_instead_of_adding"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 35. Parallel Lines With Bisector Ray (WITH SVG)
# ----------------------------------------------------------------------
def arch_35_parallel_lines_with_bisector_ray(rng: random.Random) -> Dict[str, Any]:
    tot_ang = rng.choice([70, 80, 90, 100, 110])
    half = tot_ang // 2

    lbls = {
        "top_acute_left": f"{tot_ang}°",
        "bot_acute_left": "x",
    }
    svg = draw_parallel_lines_transversal_svg(tot_ang if tot_ang < 90 else 180 - tot_ang, lbls)

    prompt = (
        f"In a diagram with \\(AB \\parallel CD\\), an angle of **{tot_ang}^\\circ** at line \\(AB\\) is bisected by a ray into two equal angles.\n"
        f"The corresponding angle at line \\(CD\\) is labeled \\(x\\).\n\n"
        f"1. What is the size of each bisected half?\n"
        f"2. Determine the value of \\(x\\) with reason."
    )
    sol = (
        f"**Step 1: Bisected angle**\n"
        f"\\[ \\text{{Each half}} = \\frac{{{tot_ang}^\\circ}}{{2}} = {half}^\\circ \\]\n\n"
        f"**Step 2: Angle x**\n"
        f"\\[ x = {tot_ang}^\\circ \\quad (\\text{{corresp. }} \\angle\\text{{s, }} AB \\parallel CD) \\]"
    )
    ans = f"1. {half}°; 2. x = {tot_ang}° (corresp. angles, AB || CD)"
    return {
        "id": f"g8_line_bisect_{rng.randint(100000, 999999)}",
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
        "subskill": "35_parallel_lines_with_bisector_ray",
        "learning_objective_id": "math_g8_lines_bisector_ray",
        "hints": {
            "tier_1": f"Bisect means divide into two equal angles.",
            "tier_2": f"{tot_ang}° ÷ 2 = {half}°.",
            "tier_3": f"Corresponding angle x = {tot_ang}°.",
        },
        "misconception_tags": ["assuming_x_is_halved_too"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 36. Perpendicular Transversal All Right Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_36_perpendicular_transversal_all_right_angles(rng: random.Random) -> Dict[str, Any]:
    salt = f"<!-- s:{rng.randint(1000, 999999)} -->\n"
    svg = salt + draw_parallel_lines_transversal_svg(90, {"top_acute_left": "90°", "bot_acute_left": "90°"})

    prompt = (
        f"A transversal line intersects parallel lines \\(AB \\parallel CD\\) at a right angle (\\(90^\\circ\\)):\n\n"
        f"1. Explain why all eight angles formed at the two intersections must measure \\(90^\\circ\\).\n"
        f"2. State the co-interior angle sum for this configuration."
    )
    sol = (
        f"**Step 1: Why all angles are 90°**\n"
        f"- Adjacent angles on straight lines are supplementary: \\(180^\\circ - 90^\\circ = 90^\\circ\\).\n"
        f"- Vertically opposite angles are equal: \\(90^\\circ\\).\n"
        f"- Corresponding and alternate angles on parallel lines are equal: \\(90^\\circ\\).\n\n"
        f"**Step 2: Co-interior sum**\n"
        f"\\[ 90^\\circ + 90^\\circ = 180^\\circ \\]"
    )
    ans = "1. Adjacent supplementary, vertically opposite, and corresponding angles are all 90°; 2. 180°"
    return {
        "id": f"g8_line_perp_trans_{rng.randint(100000, 999999)}",
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
        "subskill": "36_perpendicular_transversal_all_right_angles",
        "learning_objective_id": "math_g8_lines_perp_transversal",
        "hints": {
            "tier_1": f"Apply straight line, vertically opposite, and parallel theorems.",
            "tier_2": f"180° - 90° = 90°.",
            "tier_3": f"All 8 angles equal 90°; co-interior sum is 180°.",
        },
        "misconception_tags": ["assuming_only_some_angles_are_perpendicular"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 37. Parallel Lines With Isosceles Triangle (WITH SVG)
# ----------------------------------------------------------------------
def arch_37_parallel_lines_with_isosceles_triangle(rng: random.Random) -> Dict[str, Any]:
    apex = rng.choice([40, 50, 70, 80])
    base_ang = (180 - apex) // 2

    svg = draw_triangle_angles_svg(apex, base_ang, base_ang, f"{apex}°", "x", "y")

    prompt = (
        f"An isosceles triangle \\(\\Delta ABC\\) with \\(AB = AC\\) is situated between two parallel lines \\(L_1 \\parallel L_2\\). "
        f"The apex angle measures **{apex}^\\circ**.\n\n"
        f"1. Calculate the equal base angles \\(x\\) and \\(y\\).\n"
        f"2. If base \\(BC\\) lies on \\(L_2\\), determine the alternate angle formed with a transversal along \\(AB\\)."
    )
    sol = (
        f"**Step 1: Base angles**\n"
        f"\\[ x = y = \\frac{{180^\\circ - {apex}^\\circ}}{{2}} = \\frac{{{180 - apex}^\\circ}}{{2}} = {base_ang}^\\circ \\quad (\\angle\\text{{s opp. equal sides in }} \\Delta) \\]\n\n"
        f"**Step 2: Alternate angle**\n"
        f"Alternate angle to base angle \\(x\\) is **{base_ang}^\\circ** (\\(\\text{{alt. }} \\angle\\text{{s, }} L_1 \\parallel L_2\\))."
    )
    ans = f"1. x = y = {base_ang}°; 2. {base_ang}°"
    return {
        "id": f"g8_line_iso_tri_{rng.randint(100000, 999999)}",
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
        "subskill": "37_parallel_lines_with_isosceles_triangle",
        "learning_objective_id": "math_g8_lines_isosceles_par",
        "hints": {
            "tier_1": f"Base angles = (180° - {apex}°) ÷ 2.",
            "tier_2": f"Base angles are {base_ang}°.",
            "tier_3": f"Alternate angle is also {base_ang}°.",
        },
        "misconception_tags": ["dividing_apex_angle_by_2_instead_of_remainder"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 38. Parallel Lines With Right Angled Triangle (WITH SVG)
# ----------------------------------------------------------------------
def arch_38_parallel_lines_with_right_angled_triangle(rng: random.Random) -> Dict[str, Any]:
    acute1 = rng.choice([25, 35, 40, 55])
    acute2 = 90 - acute1

    svg = draw_triangle_angles_svg(90, acute1, acute2, "90°", f"{acute1}°", "x")

    prompt = (
        f"A right-angled triangle \\(\\Delta ABC\\) has \\(\\hat{{A}} = 90^\\circ\\) and \\(\\hat{{B}} = {acute1}^\\circ\\). "
        f"Hypotenuse \\(BC\\) is parallel to an overhead line \\(DE\\):\n\n"
        f"1. Calculate the third angle \\(\\hat{{C}}\\).\n"
        f"2. State the size of the angle alternate to \\(\\hat{{B}}\\) along the transversal \\(AB\\)."
    )
    sol = (
        f"**Step 1: Calculate angle C**\n"
        f"\\[ \\hat{{C}} = 90^\\circ - {acute1}^\\circ = {acute2}^\\circ \\quad (\\angle\\text{{ sum of }} \\Delta) \\]\n\n"
        f"**Step 2: Alternate angle**\n"
        f"\\[ \\text{{Alternate }} \\angle = \\hat{{B}} = {acute1}^\\circ \\quad (\\text{{alt. }} \\angle\\text{{s, }} DE \\parallel BC) \\]"
    )
    ans = f"1. C = {acute2}°; 2. {acute1}°"
    return {
        "id": f"g8_line_right_tri_{rng.randint(100000, 999999)}",
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
        "subskill": "38_parallel_lines_with_right_angled_triangle",
        "learning_objective_id": "math_g8_lines_right_tri_par",
        "hints": {
            "tier_1": f"Sum of acute angles in right-angled triangle = 90°.",
            "tier_2": f"C = 90° - {acute1}° = {acute2}°.",
            "tier_3": f"Alternate angle = {acute1}°.",
        },
        "misconception_tags": ["subtracting_from_180_instead_of_90"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 39. Clock Hands Straight Line Angle
# ----------------------------------------------------------------------
def arch_39_clock_hands_straight_line_angle(rng: random.Random) -> Dict[str, Any]:
    hour = rng.choice([6, 12])
    if hour == 6:
        prompt = (
            f"At exactly **6:00**, the hour hand and minute hand of an analogue clock point in opposite directions.\n\n"
            f"1. What is the angle in degrees between the two hands?\n"
            f"2. What geometric term describes this angle?"
        )
        sol = (
            f"**1.** The two hands form a straight line, which measures **180°**.\n\n"
            f"**2.** This is called a **straight angle** (or straight line angle)."
        )
        ans = "1. 180°; 2. straight angle"
    else:
        prompt = (
            f"At exactly **12:00**, the hour hand and minute hand of an analogue clock point in the exact same direction.\n\n"
            f"1. What is the angle between the two hands?\n"
            f"2. How many degrees must the minute hand rotate to form a straight line with the hour hand?"
        )
        sol = (
            f"**1.** The angle is **0°**.\n\n"
            f"**2.** The minute hand must rotate **180°** (half a circle) to point directly opposite the hour hand."
        )
        ans = "1. 0°; 2. 180°"
    return {
        "id": f"g8_line_clock_{rng.randint(100000, 999999)}",
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
        "subskill": "39_clock_hands_straight_line_angle",
        "learning_objective_id": "math_g8_lines_clock_angle",
        "hints": {
            "tier_1": f"Opposite directions form a straight line.",
            "tier_2": f"A straight line measures 180°.",
            "tier_3": f"{ans}.",
        },
        "misconception_tags": ["assuming_full_circle_360_for_straight_line"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 40. Rhombus Or Parallelogram Cointerior Relationship (WITH SVG)
# ----------------------------------------------------------------------
def arch_40_rhombus_or_parallelogram_cointerior_relationship(rng: random.Random) -> Dict[str, Any]:
    acute_ang = rng.choice([60, 65, 70, 75, 80])
    obtuse_ang = 180 - acute_ang

    svg = draw_parallel_lines_transversal_svg(acute_ang, {"top_acute_left": f"{acute_ang}°", "bot_obtuse_left": "x"})

    prompt = (
        f"In a parallelogram \\(ABCD\\), side \\(AB \\parallel DC\\) and side \\(AD \\parallel BC\\). "
        f"One acute interior angle \\(\\hat{{A}} = {acute_ang}^\\circ\\):\n\n"
        f"1. Use the co-interior angle theorem to calculate consecutive angle \\(\\hat{{B}}\\).\n"
        f"2. What is the relationship between opposite angles in a parallelogram?"
    )
    sol = (
        f"**Step 1: Calculate angle B**\n"
        f"Consecutive angles between parallel sides \\(AD \\parallel BC\\) are co-interior:\n"
        f"\\[ \\hat{{B}} = 180^\\circ - {acute_ang}^\\circ = {obtuse_ang}^\\circ \\quad (\\text{{co-int. }} \\angle\\text{{s, }} AD \\parallel BC) \\]\n\n"
        f"**Step 2: Opposite angles**\n"
        f"Opposite angles in a parallelogram are **equal** (\\(\\hat{{C}} = \\hat{{A}} = {acute_ang}^\\circ\\) and \\(\\hat{{D}} = \\hat{{B}} = {obtuse_ang}^\\circ\\))."
    )
    ans = f"1. B = {obtuse_ang}° (co-int angles, AD || BC); 2. opposite angles are equal"
    return {
        "id": f"g8_line_parm_coint_{rng.randint(100000, 999999)}",
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
        "subskill": "40_rhombus_or_parallelogram_cointerior_relationship",
        "learning_objective_id": "math_g8_lines_parm_cointerior",
        "hints": {
            "tier_1": f"Consecutive angles in a parallelogram are co-interior: sum to 180°.",
            "tier_2": f"B = 180° - {acute_ang}° = {obtuse_ang}°.",
            "tier_3": f"Opposite angles are equal.",
        },
        "misconception_tags": ["assuming_all_angles_in_parallelogram_are_equal"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 41. Trapezium Parallel Sides Cointerior Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_41_trapezium_parallel_sides_cointerior_angles(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([65, 70, 75])
    supp1 = 180 - ang1

    svg = draw_parallel_lines_transversal_svg(ang1, {"top_acute_left": f"{ang1}°", "bot_obtuse_left": "p"})

    prompt = (
        f"In a trapezium \\(PQRS\\) with \\(PQ \\parallel SR\\), the interior angle \\(\\hat{{S}} = {ang1}^\\circ\\):\n\n"
        f"Calculate the adjacent interior angle \\(\\hat{{P}}\\) along transversal leg \\(PS\\), stating the geometric reason."
    )
    sol = (
        f"**Step 1: Calculate angle P**\n"
        f"Since \\(PQ \\parallel SR\\), angles \\(\\hat{{P}}\\) and \\(\\hat{{S}}\\) are co-interior angles:\n"
        f"\\[ \\hat{{P}} + \\hat{{S}} = 180^\\circ \\quad (\\text{{co-int. }} \\angle\\text{{s, }} PQ \\parallel SR) \\]\n"
        f"\\[ \\hat{{P}} = 180^\\circ - {ang1}^\\circ = {supp1}^\\circ \\]"
    )
    ans = f"P = {supp1}° (co-int. angles, PQ || SR)"
    return {
        "id": f"g8_line_trap_coint_{rng.randint(100000, 999999)}",
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
        "subskill": "41_trapezium_parallel_sides_cointerior_angles",
        "learning_objective_id": "math_g8_lines_trap_cointerior",
        "hints": {
            "tier_1": f"The parallel sides PQ and SR form co-interior angles with transversal PS.",
            "tier_2": f"P = 180° - {ang1}°.",
            "tier_3": f"P = {supp1}° (co-int ∠s, PQ || SR).",
        },
        "misconception_tags": ["applying_cointerior_to_non_parallel_legs"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 42. Diagnosing Geometric Reason Abbreviation
# ----------------------------------------------------------------------
def arch_42_diagnosing_geometric_reason_abbreviation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner wrote the following line in a formal Euclidean geometry proof:\n"
        f"\\[ \\hat{{B}}_1 = \\hat{{D}}_2 = 65^\\circ \\quad [\\text{{alt. }} \\angle\\text{{s}}] \\]\n\n"
        f"1. Why did the teacher award 0 marks for this geometric reason?\n"
        f"2. How should the reason be written correctly?"
    )
    sol = (
        f"**1. Error Explanation:**\n"
        f"Alternate angles are only equal when the lines they lie on are **parallel**.\n"
        f"Writing just '[alt. ∠s]' without specifying **which** pair of lines is parallel (e.g., \\(AB \\parallel CD\\)) is incomplete and invalid in CAPS exam marking.\n\n"
        f"**2. Correct Reason:**\n"
        f"\\[ [\\text{{alt. }} \\angle\\text{{s, }} AB \\parallel CD] \\]"
    )
    ans = "1. Failed to state which lines are parallel; 2. [alt. angles, AB || CD]"
    return {
        "id": f"g8_line_diag_abbr_{rng.randint(100000, 999999)}",
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
        "subskill": "42_diagnosing_geometric_reason_abbreviation",
        "learning_objective_id": "math_g8_lines_diag_reason_abbr",
        "hints": {
            "tier_1": f"Reasons for parallel line angle pairs MUST always include the names of the parallel lines.",
            "tier_2": f"Write: [alt. ∠s, line1 || line2].",
            "tier_3": f"Must name parallel lines.",
        },
        "misconception_tags": ["omitting_parallel_line_names_in_reason"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 43. Diagnosing Cointerior Angle Fallacy
# ----------------------------------------------------------------------
def arch_43_diagnosing_cointerior_angle_fallacy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner was asked to find angle \\(y\\) between parallel lines \\(AB \\parallel CD\\) where the co-interior angle is 70°.\n"
        f"The learner wrote: \\(y = 70^\\circ \\quad [\\text{{co-int. }} \\angle\\text{{s, }} AB \\parallel CD]\\).\n\n"
        f"1. Explain the learner's misconception.\n"
        f"2. Give the correct value of \\(y\\)."
    )
    sol = (
        f"**1. Misconception:**\n"
        f"The learner incorrectly assumed that co-interior angles are equal, confusing them with alternate or corresponding angles.\n"
        f"Co-interior angles are **supplementary** (they add up to 180°).\n\n"
        f"**2. Correct Value:**\n"
        f"\\[ y = 180^\\circ - 70^\\circ = 110^\\circ \\]"
    )
    ans = "1. Co-interior angles are supplementary (sum to 180°), not equal; 2. y = 110°"
    return {
        "id": f"g8_line_diag_coint_{rng.randint(100000, 999999)}",
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
        "subskill": "43_diagnosing_cointerior_angle_fallacy",
        "learning_objective_id": "math_g8_lines_diag_cointerior_fallacy",
        "hints": {
            "tier_1": f"Co-interior angles are U-shaped: they add to 180°.",
            "tier_2": f"y = 180° - 70°.",
            "tier_3": f"y = 110°.",
        },
        "misconception_tags": ["equating_cointerior_angles"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 44. Diagnosing Non Parallel Transversal Fallacy
# ----------------------------------------------------------------------
def arch_44_diagnosing_non_parallel_transversal_fallacy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner looked at two lines intersected by a transversal where no parallel line arrows were marked, and wrote:\n"
        f"\\[ \\hat{{A}} = \\hat{{B}} = 50^\\circ \\quad [\\text{{alt. }} \\angle\\text{{s}}] \\]\n\n"
        f"1. Under what strict condition are alternate angles equal?\n"
        f"2. Was the learner justified in concluding the angles were equal without parallel markings?"
    )
    sol = (
        f"**1. Strict Condition:**\n"
        f"Alternate angles are **only** equal if the two lines cut by the transversal are **parallel**.\n\n"
        f"**2. Conclusion:**\n"
        f"No. Without given parallel markings (arrows) or a given statement that the lines are parallel, alternate angles are generally not equal."
    )
    ans = "1. Lines must be parallel; 2. No, not justified without parallel markings"
    return {
        "id": f"g8_line_diag_nonpar_{rng.randint(100000, 999999)}",
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
        "subskill": "44_diagnosing_non_parallel_transversal_fallacy",
        "learning_objective_id": "math_g8_lines_diag_non_parallel",
        "hints": {
            "tier_1": f"Angle pair relationships only produce equal angles when lines are parallel.",
            "tier_2": f"Arrows on lines indicate parallelism.",
            "tier_3": f"Lines must be parallel.",
        },
        "misconception_tags": ["assuming_transversal_angles_equal_without_parallel_lines"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 45. Complex Two Parallel Pairs Rhomboid Grid (WITH SVG)
# ----------------------------------------------------------------------
def arch_45_complex_two_parallel_pairs_rhomboid_grid(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([65, 75, 80])
    supp = 180 - ang

    svg = draw_parallel_lines_transversal_svg(ang, {"top_acute_left": f"{ang}°", "bot_obtuse_right": "x"})

    prompt = (
        f"Two pairs of parallel lines intersect to form a grid: \\(AB \\parallel CD\\) and \\(EF \\parallel GH\\).\n"
        f"One acute angle in the grid is **{ang}^\\circ**.\n\n"
        f"1. Find the obtuse angle \\(x\\) adjacent to it.\n"
        f"2. Explain why all acute angles in the entire grid measure {ang}^\\circ."
    )
    sol = (
        f"**Step 1: Obtuse angle**\n"
        f"\\[ x = 180^\\circ - {ang}^\\circ = {supp}^\\circ \\quad (\\angle\\text{{s on str line or co-int. }} \\angle\\text{{s}}) \\]\n\n"
        f"**Step 2: Grid symmetry**\n"
        f"Because both pairs of lines are parallel, all corresponding, alternate, and vertically opposite angles propagate throughout the intersections, making every acute angle **{ang}^\\circ** and every obtuse angle **{supp}^\\circ**."
    )
    ans = f"1. x = {supp}°; 2. Repeated application of corresponding, alternate, and vertically opposite angles across both parallel pairs"
    return {
        "id": f"g8_line_grid_{rng.randint(100000, 999999)}",
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
        "subskill": "45_complex_two_parallel_pairs_rhomboid_grid",
        "learning_objective_id": "math_g8_lines_two_parallel_pairs",
        "hints": {
            "tier_1": f"Adjacent angles on straight lines are supplementary.",
            "tier_2": f"180° - {ang}° = {supp}°.",
            "tier_3": f"x = {supp}°.",
        },
        "misconception_tags": ["confusing_intersecting_pairs"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 46. Straight Line Algebraic Fractional Angles (WITH SVG)
# ----------------------------------------------------------------------
def arch_46_straight_line_algebraic_fractional_angles(rng: random.Random) -> Dict[str, Any]:
    # x/2 + x/3 + k = 180 => (5/6)x + k = 180 => (5/6)x = 180 - k => x must be multiple of 6
    ans_x = rng.choice([60, 72, 84, 96])
    fractional_sum = (5 * ans_x) // 6
    k = 180 - fractional_sum

    svg = draw_angles_on_line_svg(fractional_sum, f"5x/6", f"{k}°")

    prompt = (
        f"Three angles on a straight line are expressed as \\(\\frac{{x}}{{2}}\\), \\(\\frac{{x}}{{3}}\\), and **{k}^\\circ**:\n\n"
        f"1. Set up an equation using the LCD of the fractions.\n"
        f"2. Solve for \\(x\\)."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ \\frac{{x}}{{2}} + \\frac{{x}}{{3}} + {k} = 180 \\quad (\\text{{adj }} \\angle\\text{{s on str line}}) \\]\n"
        f"The LCD of 2 and 3 is 6:\n"
        f"\\[ \\frac{{3x + 2x}}{{6}} + {k} = 180 \\]\n"
        f"\\[ \\frac{{5x}}{{6}} = 180 - {k} = {180 - k} \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ 5x = ({180 - k}) \\times 6 = {(180 - k) * 6} \\]\n"
        f"\\[ x = \\frac{{{(180 - k) * 6}}}{{5}} = {ans_x} \\]"
    )
    ans = f"1. 5x/6 + {k} = 180; 2. x = {ans_x}"
    return {
        "id": f"g8_line_frac_ang_{rng.randint(100000, 999999)}",
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
        "subskill": "46_straight_line_algebraic_fractional_angles",
        "learning_objective_id": "math_g8_lines_fractional_angles",
        "hints": {
            "tier_1": f"x/2 + x/3 = 5x/6.",
            "tier_2": f"5x/6 = {180 - k}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["adding_denominators_for_fractions"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 47. Straight Line With Decimal Angle Measures (WITH SVG)
# ----------------------------------------------------------------------
def arch_47_straight_line_with_decimal_angle_measures(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([42.5, 54.5, 68.5, 73.5, 115.5])
    ang2 = round(180.0 - ang1, 1)

    ang1_sa = str(ang1).replace(".", ",")
    ang2_sa = str(ang2).replace(".", ",")

    svg = draw_angles_on_line_svg(int(ang1), f"{ang1_sa}°", "y")

    prompt = (
        f"Line \\(AB\\) is a straight line. An adjacent ray creates an angle of **{ang1_sa}^\\circ** and an unknown angle \\(y\\):\n\n"
        f"1. Set up an equation with reason.\n"
        f"2. Calculate \\(y\\) in degrees using South African decimal notation."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ y + {ang1_sa}^\\circ = 180^\\circ \\quad (\\text{{adj }} \\angle\\text{{s on str line}}) \\]\n\n"
        f"**Step 2: Solve for y**\n"
        f"\\[ y = 180^\\circ - {ang1_sa}^\\circ = {ang2_sa}^\\circ \\]"
    )
    ans = f"1. y + {ang1_sa}° = 180° (adj angles on straight line); 2. y = {ang2_sa}°"
    return {
        "id": f"g8_line_dec_ang_{rng.randint(100000, 999999)}",
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
        "subskill": "47_straight_line_with_decimal_angle_measures",
        "learning_objective_id": "math_g8_lines_decimal_angles",
        "hints": {
            "tier_1": f"Subtract {ang1_sa}° from 180°.",
            "tier_2": f"180 - {ang1_sa} = {ang2_sa}.",
            "tier_3": f"y = {ang2_sa}°.",
        },
        "misconception_tags": ["decimal_subtraction_borrowing_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 48. Reflection Of Light Ray Straight Line (WITH SVG)
# ----------------------------------------------------------------------
def arch_48_reflection_of_light_ray_straight_line(rng: random.Random) -> Dict[str, Any]:
    # Flat mirror on straight line. Light ray strikes surface. Angle of incidence = Angle of reflection = i
    # Angle between incident and reflected ray = 2*i. Grazing angles = 90 - i
    i = rng.choice([30, 40, 45, 50, 60])
    grazing = 90 - i
    between = 2 * i

    svg = draw_angles_on_line_svg(90 - i, f"{grazing}°", f"{between}° + {grazing}°")

    prompt = (
        f"A ray of light reflects off a flat horizontal mirror lying along straight line \\(MN\\). "
        f"The angle between the incoming light ray and the surface of the mirror is **{grazing}^\\circ**.\n\n"
        f"By the Law of Reflection, the angle between the reflected ray and the mirror surface is also **{grazing}^\\circ**.\n\n"
        f"Calculate the angle \\(\\theta\\) between the incoming ray and the reflected ray, using the straight-line theorem."
    )
    sol = (
        f"**Step 1: Identify all angles on straight line MN**\n"
        f"The angles lying on the straight mirror surface are \\({grazing}^\\circ\\), \\(\\theta\\), and \\({grazing}^\\circ\\).\n\n"
        f"**Step 2: Set up equation and solve**\n"
        f"\\[ {grazing}^\\circ + \\theta + {grazing}^\\circ = 180^\\circ \\quad (\\angle\\text{{s on str line}}) \\]\n"
        f"\\[ \\theta + {2 * grazing}^\\circ = 180^\\circ \\]\n"
        f"\\[ \\theta = 180^\\circ - {2 * grazing}^\\circ = {between}^\\circ \\]"
    )
    ans = f"θ = {between}° (angles on straight line)"
    return {
        "id": f"g8_line_optic_{rng.randint(100000, 999999)}",
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
        "subskill": "48_reflection_of_light_ray_straight_line",
        "learning_objective_id": "math_g8_lines_reflection_straight",
        "hints": {
            "tier_1": f"Sum of angles along the mirror = 180°.",
            "tier_2": f"θ = 180° - 2({grazing}°).",
            "tier_3": f"θ = {between}°.",
        },
        "misconception_tags": ["subtracting_single_grazing_angle_only"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 49. Surveying Compass Bearing Straight Line
# ----------------------------------------------------------------------
def arch_49_surveying_compass_bearing_straight_line(rng: random.Random) -> Dict[str, Any]:
    forward_bearing = rng.choice([40, 65, 80, 115, 130])
    back_bearing = forward_bearing + 180

    prompt = (
        f"In surveying and navigation, a surveyor sights a landmark on a forward bearing of **{forward_bearing:03d}^\\circ**.\n\n"
        f"1. Explain why the back-bearing (direction pointing directly back along the same line) is found by adding \\(180^\\circ\\).\n"
        f"2. Calculate the exact back-bearing in degrees."
    )
    sol = (
        f"**1. Geometric Explanation:**\n"
        f"A straight line forms a straight angle of \\(180^\\circ\\). Reversing direction along the same straight line corresponds to rotating through \\(180^\\circ\\).\n\n"
        f"**2. Calculation:**\n"
        f"\\[ \\text{{Back-bearing}} = {forward_bearing}^\\circ + 180^\\circ = {back_bearing:03d}^\\circ \\]"
    )
    ans = f"1. Reversing direction along a straight line is a 180° rotation; 2. {back_bearing:03d}°"
    return {
        "id": f"g8_line_bearing_{rng.randint(100000, 999999)}",
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
        "subskill": "49_surveying_compass_bearing_straight_line",
        "learning_objective_id": "math_g8_lines_surveying_bearing",
        "hints": {
            "tier_1": f"Back-bearing is in the directly opposite direction (180° away).",
            "tier_2": f"Add 180° to {forward_bearing:03d}°.",
            "tier_3": f"{back_bearing:03d}°.",
        },
        "misconception_tags": ["subtracting_from_360_instead_of_adding_180"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 50. Geometry Of Straight Lines Capstone Synthesis (WITH SVG)
# ----------------------------------------------------------------------
def arch_50_geometry_of_straight_lines_capstone_synthesis(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([65, 70, 75, 80])
    supp = 180 - ang

    lbls = {
        "top_acute_left": f"{ang}°",
        "top_obtuse_right": "w",
        "bot_acute_left": "x",
        "bot_obtuse_right": "y",
    }
    svg = draw_parallel_lines_transversal_svg(ang, lbls)

    prompt = (
        f"**Comprehensive Deductive Geometry Proof**\n\n"
        f"In the configuration shown below, two horizontal lines are parallel (\\(AB \\parallel CD\\)) "
        f"and intersected by transversal line \\(EF\\). An acute angle at \\(AB\\) measures **{ang}^\\circ**.\n\n"
        f"Calculate the values of \\(w\\), \\(x\\), and \\(y\\), stating the exact formal geometric reason for each deduction."
    )
    sol = (
        f"**Deduction 1: Angle w**\n"
        f"\\[ w = 180^\\circ - {ang}^\\circ = {supp}^\\circ \\quad (\\angle\\text{{s on a straight line}}) \\]\n\n"
        f"**Deduction 2: Angle x**\n"
        f"\\[ x = {ang}^\\circ \\quad (\\text{{corresp. }} \\angle\\text{{s, }} AB \\parallel CD) \\]\n\n"
        f"**Deduction 3: Angle y**\n"
        f"\\[ y = {supp}^\\circ \\quad (\\text{{co-int. }} \\angle\\text{{s, }} AB \\parallel CD \\text{{ or }} \\text{{vert. opp. }} \\angle\\text{{s to }} w) \\]"
    )
    ans = f"w = {supp}° (angles on straight line); x = {ang}° (corresp angles, AB || CD); y = {supp}° (co-int angles, AB || CD)"
    return {
        "id": f"g8_line_capstone_{rng.randint(100000, 999999)}",
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
        "subskill": "50_geometry_of_straight_lines_capstone_synthesis",
        "learning_objective_id": "math_g8_lines_capstone",
        "hints": {
            "tier_1": f"w and {ang}° form a straight line: w = 180° - {ang}°.",
            "tier_2": f"x corresponds to {ang}°: x = {ang}° (corresp ∠s, AB || CD).",
            "tier_3": f"y = {supp}° (co-int ∠s, AB || CD).",
        },
        "misconception_tags": ["omitting_parallel_line_names_in_reasons"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


BUILDERS_26_50: List[Callable[[random.Random], Dict[str, Any]]] = [
    arch_26_parallel_lines_three_parallel_lines,
    arch_27_parallel_lines_two_transversals,
    arch_28_proving_lines_parallel_via_corresponding_angles,
    arch_29_proving_lines_parallel_via_alternate_angles,
    arch_30_proving_lines_parallel_via_cointerior_angles,
    arch_31_angles_around_a_point_revolution,
    arch_32_angles_around_a_point_algebraic,
    arch_33_triangle_angle_sum_straight_line_proof,
    arch_34_zig_zag_parallel_lines_auxiliary_line,
    arch_35_parallel_lines_with_bisector_ray,
    arch_36_perpendicular_transversal_all_right_angles,
    arch_37_parallel_lines_with_isosceles_triangle,
    arch_38_parallel_lines_with_right_angled_triangle,
    arch_39_clock_hands_straight_line_angle,
    arch_40_rhombus_or_parallelogram_cointerior_relationship,
    arch_41_trapezium_parallel_sides_cointerior_angles,
    arch_42_diagnosing_geometric_reason_abbreviation,
    arch_43_diagnosing_cointerior_angle_fallacy,
    arch_44_diagnosing_non_parallel_transversal_fallacy,
    arch_45_complex_two_parallel_pairs_rhomboid_grid,
    arch_46_straight_line_algebraic_fractional_angles,
    arch_47_straight_line_with_decimal_angle_measures,
    arch_48_reflection_of_light_ray_straight_line,
    arch_49_surveying_compass_bearing_straight_line,
    arch_50_geometry_of_straight_lines_capstone_synthesis,
]
