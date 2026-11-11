"""Grade 8 Mathematics — Pythagoras Archetypes 26 to 50.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 3/03. The theorem of Pythagoras.md

Archetypes covering:
  - 26 to 30: Converse classifying triangles (acute, right, obtuse), error analysis.
  - 31 to 40: Real-world contexts (ladder against wall, walking displacement, rectangle/square diagonals, flagpole wire, ramp, isosceles/equilateral altitudes).
  - 41 to 50: Coordinate geometry distance, right triangle perimeter and area, composite figures, rhombus diagonals, scaling triples, adjacent triangles, broken tree problem.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .pythagoras_svg import (
    draw_pythagoras_triangle_svg,
    draw_pythagoras_ladder_context_svg,
)


def _fmt_dec(v: float, places: int = 1) -> str:
    s = f"{v:.{places}f}"
    return s.replace(".", ",")


# ----------------------------------------------------------------------
# 26. Converse Classify Triangle Acute, Right, Obtuse
# ----------------------------------------------------------------------
def arch_26_converse_classify_triangle_acute_right_obtuse(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["acute", "right", "obtuse"])
    if choice == "acute":
        a, b, c = 7, 8, 10  # 49 + 64 = 113 > 100
        desc = "Acute-angled triangle (a² + b² > c²)"
    elif choice == "right":
        a, b, c = 6, 8, 10  # 36 + 64 = 100 = 100
        desc = "Right-angled triangle (a² + b² = c²)"
    else:
        a, b, c = 4, 5, 8   # 16 + 25 = 41 < 64
        desc = "Obtuse-angled triangle (a² + b² < c²)"

    lhs = a * a + b * b
    rhs = c * c
    comp = ">" if lhs > rhs else ("=" if lhs == rhs else "<")

    prompt = (
        f"A triangle has side lengths of **{a} cm**, **{b} cm**, and **{c} cm** (where {c} cm is the longest side).\n\n"
        f"1. Calculate \\(a^2 + b^2\\) and \\(c^2\\).\n"
        f"2. Compare \\(a^2 + b^2\\) with \\(c^2\\) and classify the triangle as acute-angled, right-angled, or obtuse-angled."
    )
    sol = (
        f"**1. Squares calculation:**\n"
        f"\\[ a^2 + b^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {lhs} \\]\n"
        f"\\[ c^2 = {c}^2 = {rhs} \\]\n\n"
        f"**2. Comparison and Classification:**\n"
        f"Since \\({lhs} {comp} {rhs}\\), \\(a^2 + b^2 {comp} c^2\\).\n"
        f"Classification: **{desc}**."
    )
    ans = f"1. a² + b² = {lhs}, c² = {rhs}; 2. {choice}-angled triangle"
    return {
        "id": f"g8_pyth_class_tri_{rng.randint(100000, 999999)}",
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
        "subskill": "26_converse_classify_triangle_acute_right_obtuse",
        "learning_objective_id": "math_g8_pyth_class_tri",
        "hints": {
            "tier_1": "If a² + b² > c², acute; if =, right; if <, obtuse.",
            "tier_2": f"{lhs} vs {rhs}.",
            "tier_3": f"{choice}-angled triangle.",
        },
        "misconception_tags": ["confusing_acute_and_obtuse_inequalities"],
    }


# ----------------------------------------------------------------------
# 27. Converse Acute-Angled Triangle Test
# ----------------------------------------------------------------------
def arch_27_converse_acute_angled_triangle_test(rng: random.Random) -> Dict[str, Any]:
    a, b, c = rng.choice([(5, 6, 7), (7, 8, 9), (8, 9, 11)])
    lhs = a * a + b * b
    rhs = c * c

    prompt = (
        f"A triangle has side measurements of **{a} cm**, **{b} cm**, and **{c} cm**.\n\n"
        f"1. Show that \\(a^2 + b^2 > c^2\\).\n"
        f"2. Conclude the classification of this triangle based on interior angles."
    )
    sol = (
        f"**1. Calculation:**\n"
        f"\\[ a^2 + b^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {lhs} \\]\n"
        f"\\[ c^2 = {c}^2 = {rhs} \\]\n"
        f"Since \\({lhs} > {rhs}\\), \\(a^2 + b^2 > c^2\\).\n\n"
        f"**2. Conclusion:** Because the sum of the squares on the shorter sides exceeds the square on the longest side, "
        f"all three interior angles are acute, making it an **acute-angled triangle**."
    )
    ans = f"1. {lhs} > {rhs}; 2. acute-angled triangle"
    return {
        "id": f"g8_pyth_acute_test_{rng.randint(100000, 999999)}",
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
        "subskill": "27_converse_acute_angled_triangle_test",
        "learning_objective_id": "math_g8_pyth_acute_test",
        "hints": {
            "tier_1": f"Calculate {a}² + {b}² = {lhs} and {c}² = {rhs}.",
            "tier_2": f"{lhs} > {rhs}.",
            "tier_3": "Acute-angled triangle.",
        },
        "misconception_tags": ["calling_it_right_angled_despite_inequality"],
    }


# ----------------------------------------------------------------------
# 28. Converse Obtuse-Angled Triangle Test
# ----------------------------------------------------------------------
def arch_28_converse_obtuse_angled_triangle_test(rng: random.Random) -> Dict[str, Any]:
    a, b, c = rng.choice([(3, 4, 6), (4, 5, 7), (5, 7, 10)])
    lhs = a * a + b * b
    rhs = c * c

    prompt = (
        f"A triangle has side lengths of **{a} cm**, **{b} cm**, and **{c} cm**.\n\n"
        f"1. Calculate \\(a^2 + b^2\\) and \\(c^2\\).\n"
        f"2. Explain why this triangle must contain an obtuse angle (angle > 90°)."
    )
    sol = (
        f"**1. Calculation:**\n"
        f"\\[ a^2 + b^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {lhs} \\]\n"
        f"\\[ c^2 = {c}^2 = {rhs} \\]\n\n"
        f"**2. Explanation:** Because \\({lhs} < {rhs}\\) (\\(a^2 + b^2 < c^2\\)), the square on the longest side "
        f"is greater than the sum of the squares on the other two sides. This geometric condition occurs only when "
        f"the angle opposite the longest side has expanded beyond 90°, forming an **obtuse-angled triangle**."
    )
    ans = f"1. a² + b² = {lhs}, c² = {rhs}; 2. a² + b² < c² indicates an obtuse-angled triangle"
    return {
        "id": f"g8_pyth_obtuse_test_{rng.randint(100000, 999999)}",
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
        "subskill": "28_converse_obtuse_angled_triangle_test",
        "learning_objective_id": "math_g8_pyth_obtuse_test",
        "hints": {
            "tier_1": f"Compare {lhs} with {rhs}.",
            "tier_2": f"{lhs} < {rhs}.",
            "tier_3": "Obtuse-angled triangle.",
        },
        "misconception_tags": ["treating_obtuse_condition_as_acute"],
    }


# ----------------------------------------------------------------------
# 29. Converse Triangle Classification Synthesis
# ----------------------------------------------------------------------
def arch_29_converse_triangle_table_classification(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Classify each of the following three triangles with given side lengths as either Acute, Right, or Obtuse:\n\n"
        "1. Triangle A: sides 9 cm, 12 cm, 15 cm\n"
        "2. Triangle B: sides 6 cm, 7 cm, 8 cm\n"
        "3. Triangle C: sides 5 cm, 8 cm, 11 cm"
    )
    sol = (
        "**1. Triangle A (9, 12, 15):**\n"
        "\\[ 9^2 + 12^2 = 81 + 144 = 225 = 15^2 \\implies \\mathbf{Right-angled} \\]\n\n"
        "**2. Triangle B (6, 7, 8):**\n"
        "\\[ 6^2 + 7^2 = 36 + 49 = 85 > 8^2 = 64 \\implies \\mathbf{Acute-angled} \\]\n\n"
        "**3. Triangle C (5, 8, 11):**\n"
        "\\[ 5^2 + 8^2 = 25 + 64 = 89 < 11^2 = 121 \\implies \\mathbf{Obtuse-angled} \\]"
    )
    ans = "1. Right-angled; 2. Acute-angled; 3. Obtuse-angled"
    return {
        "id": f"g8_pyth_class_synth_{rng.randint(100000, 999999)}",
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
        "subskill": "29_converse_triangle_table_classification",
        "learning_objective_id": "math_g8_pyth_class_synth",
        "hints": {
            "tier_1": "Test a² + b² vs c² for each triangle.",
            "tier_2": "A: 81+144=225=15²; B: 36+49=85>64; C: 25+64=89<121.",
            "tier_3": ans,
        },
        "misconception_tags": ["mixing_up_comparison_rules_across_multiple_cases"],
    }


# ----------------------------------------------------------------------
# 30. Converse Error Analysis: Comparing Wrong Side to Sum
# ----------------------------------------------------------------------
def arch_30_converse_error_analysis_comparing_wrong_side_to_sum(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner tests whether a triangle with sides **8 cm**, **17 cm**, and **15 cm** is right-angled.\n"
        "The learner calculates \\(8^2 + 17^2 = 64 + 289 = 353\\), compares it to \\(15^2 = 225\\), and concludes "
        "that the triangle is NOT right-angled.\n\n"
        "1. Identify the fatal error made by the learner.\n"
        "2. Provide the correct calculation and determine if the triangle is indeed right-angled."
    )
    sol = (
        "**1. Error Identification:** The learner added the square of the longest side (17 cm) to 8 cm instead of "
        "isolating the longest side as \\(c\\). In the Converse of Pythagoras, \\(c\\) MUST strictly be the longest side (17 cm).\n\n"
        "**2. Correct Calculation:**\n"
        "\\[ 8^2 + 15^2 = 64 + 225 = 289 \\]\n"
        "\\[ 17^2 = 289 \\]\n"
        "Since \\(8^2 + 15^2 = 17^2\\), the triangle **IS right-angled**."
    )
    ans = "1. failed to isolate the longest side (17 cm) as c; 2. 8² + 15² = 64 + 225 = 289 = 17², so it is right-angled"
    return {
        "id": f"g8_pyth_err_conv_{rng.randint(100000, 999999)}",
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
        "subskill": "30_converse_error_analysis_comparing_wrong_side_to_sum",
        "learning_objective_id": "math_g8_pyth_err_conv",
        "hints": {
            "tier_1": "The longest side must always be on its own on the RHS.",
            "tier_2": "Longest side is 17 cm, so test 8² + 15² = 17².",
            "tier_3": ans,
        },
        "misconception_tags": ["not_identifying_the_longest_side_first_when_testing_converse"],
    }


# ----------------------------------------------------------------------
# 31. Context: Ladder Find Hypotenuse Length (WITH SVG)
# ----------------------------------------------------------------------
def arch_31_context_ladder_find_hypotenuse_length(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    dist = 3 * k
    wall = 4 * k
    ladder = 5 * k
    svg = draw_pythagoras_ladder_context_svg(wall, dist, ladder, unknown="ladder", seed=rng.randint(100, 999999))

    prompt = (
        f"A ladder leans against a vertical building wall. The foot of the ladder is placed **{dist} m** "
        f"away from the base of the wall, and the top of the ladder reaches **{wall} m** up the wall.\n\n"
        f"Calculate the length of the ladder in meters, showing formula and working."
    )
    sol = (
        f"**Calculation of Ladder Length:**\n"
        f"The wall, ground, and ladder form a right-angled triangle where the ladder is the hypotenuse \\(c\\):\n"
        f"\\[ c^2 = a^2 + b^2 \\quad [\\text{{Pythagoras / wall }} \\perp \\text{{ ground}}] \\]\n"
        f"\\[ c^2 = {dist}^2 + {wall}^2 = {dist*dist} + {wall*wall} = {ladder*ladder} \\]\n"
        f"\\[ c = \\sqrt{{{ladder*ladder}}} = {ladder}\\text{{ m}} \\]"
    )
    ans = f"{ladder} m"
    return {
        "id": f"g8_pyth_lad_hyp_{rng.randint(100000, 999999)}",
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
        "subskill": "31_context_ladder_find_hypotenuse_length",
        "learning_objective_id": "math_g8_pyth_lad_hyp",
        "hints": {
            "tier_1": f"Ladder² = {dist}² + {wall}².",
            "tier_2": f"Ladder² = {dist*dist} + {wall*wall} = {ladder*ladder}.",
            "tier_3": f"{ladder} m.",
        },
        "misconception_tags": ["subtracting_instead_of_adding_for_ladder_length"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 32. Context: Ladder Find Wall Height Reached (WITH SVG)
# ----------------------------------------------------------------------
def arch_32_context_ladder_find_wall_height_reached(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    dist = 5 * k
    wall = 12 * k
    ladder = 13 * k
    svg = draw_pythagoras_ladder_context_svg(wall, dist, ladder, unknown="wall", seed=rng.randint(100, 999999))

    prompt = (
        f"A **{ladder} m** long ladder leans against a vertical wall. Its foot rests on level ground "
        f"**{dist} m** away from the wall.\n\n"
        f"Calculate the height up the wall reached by the top of the ladder."
    )
    sol = (
        f"**Calculation of Wall Height:**\n"
        f"\\[ h^2 = \\text{{ladder}}^2 - \\text{{ground}}^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ h^2 = {ladder}^2 - {dist}^2 = {ladder*ladder} - {dist*dist} = {wall*wall} \\]\n"
        f"\\[ h = \\sqrt{{{wall*wall}}} = {wall}\\text{{ m}} \\]"
    )
    ans = f"{wall} m"
    return {
        "id": f"g8_pyth_lad_wall_{rng.randint(100000, 999999)}",
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
        "subskill": "32_context_ladder_find_wall_height_reached",
        "learning_objective_id": "math_g8_pyth_lad_wall",
        "hints": {
            "tier_1": f"h² = {ladder}² - {dist}².",
            "tier_2": f"h² = {ladder*ladder} - {dist*dist} = {wall*wall}.",
            "tier_3": f"{wall} m.",
        },
        "misconception_tags": ["adding_ladder_length_and_ground_distance"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 33. Context: Ladder Find Distance from Base (WITH SVG)
# ----------------------------------------------------------------------
def arch_33_context_ladder_find_distance_from_base(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    dist = 6 * k
    wall = 8 * k
    ladder = 10 * k
    svg = draw_pythagoras_ladder_context_svg(wall, dist, ladder, unknown="ground", seed=rng.randint(100, 999999))

    prompt = (
        f"A firefighter extends a **{ladder} m** ladder so that it reaches a window **{wall} m** high on a vertical wall.\n\n"
        f"How far from the base of the wall must the foot of the ladder be placed on the ground?"
    )
    sol = (
        f"**Calculation of Ground Distance:**\n"
        f"\\[ d^2 = \\text{{ladder}}^2 - \\text{{wall}}^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ d^2 = {ladder}^2 - {wall}^2 = {ladder*ladder} - {wall*wall} = {dist*dist} \\]\n"
        f"\\[ d = \\sqrt{{{dist*dist}}} = {dist}\\text{{ m}} \\]"
    )
    ans = f"{dist} m"
    return {
        "id": f"g8_pyth_lad_dist_{rng.randint(100000, 999999)}",
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
        "subskill": "33_context_ladder_find_distance_from_base",
        "learning_objective_id": "math_g8_pyth_lad_dist",
        "hints": {
            "tier_1": f"d² = {ladder}² - {wall}².",
            "tier_2": f"{ladder*ladder} - {wall*wall} = {dist*dist}.",
            "tier_3": f"{dist} m.",
        },
        "misconception_tags": ["adding_instead_of_subtracting_for_ground_distance"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 34. Context: Walking Displacement North and East (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_34_context_walking_displacement_north_east(rng: random.Random) -> Dict[str, Any]:
    east = rng.choice([6, 9, 12])
    north = rng.choice([8, 12, 16])
    # scaled 3-4-5
    k = east // 3
    if north != 4 * k:
        north = 4 * k
    direct = 5 * k

    prompt = (
        f"A hiker walks **{east} km due East** and then turns and walks **{north} km due North**.\n\n"
        f"1. Explain why North and East directions form a right-angled triangle.\n"
        f"2. Calculate the direct straight-line distance from the starting point to the final position."
    )
    sol = (
        f"**1. Geometric Explanation:** North and East are perpendicular cardinal directions that intersect at exactly **90°**.\n\n"
        f"**2. Straight-line distance calculation:**\n"
        f"\\[ d^2 = {east}^2 + {north}^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ d^2 = {east*east} + {north*north} = {direct*direct} \\]\n"
        f"\\[ d = \\sqrt{{{direct*direct}}} = {direct}\\text{{ km}} \\]"
    )
    ans = f"1. cardinal directions North and East meet at 90°; 2. {direct} km"
    return {
        "id": f"g8_pyth_walk_{rng.randint(100000, 999999)}",
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
        "subskill": "34_context_walking_displacement_north_east",
        "learning_objective_id": "math_g8_pyth_walk",
        "hints": {
            "tier_1": f"Direct distance is the hypotenuse: d² = {east}² + {north}².",
            "tier_2": f"d² = {direct*direct}.",
            "tier_3": f"{direct} km.",
        },
        "misconception_tags": ["adding_walked_distances_instead_of_displacement"],
    }


# ----------------------------------------------------------------------
# 35. Context: Diagonal of a Rectangle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_35_context_diagonal_of_rectangle(rng: random.Random) -> Dict[str, Any]:
    l_val, w_val, d_val = rng.choice([(8, 15, 17), (12, 16, 20), (7, 24, 25), (20, 21, 29)])

    prompt = (
        f"A rectangular television screen has a width of **{l_val} cm** and a height of **{w_val} cm**.\n\n"
        f"1. Explain why the diagonal of a rectangle can be calculated using the Theorem of Pythagoras.\n"
        f"2. Calculate the diagonal screen size of the television in cm."
    )
    sol = (
        f"**1. Explanation:** The four interior corner angles of a rectangle are all **90°**. Drawing a diagonal "
        f"divides the rectangle into two congruent right-angled triangles where the diagonal forms the hypotenuse.\n\n"
        f"**2. Calculation:**\n"
        f"\\[ d^2 = {l_val}^2 + {w_val}^2 = {l_val*l_val} + {w_val*w_val} = {d_val*d_val} \\]\n"
        f"\\[ d = \\sqrt{{{d_val*d_val}}} = {d_val}\\text{{ cm}} \\]"
    )
    ans = f"1. corner angles of rectangle are 90°, so diagonal is hypotenuse; 2. {d_val} cm"
    return {
        "id": f"g8_pyth_diag_rect_{rng.randint(100000, 999999)}",
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
        "subskill": "35_context_diagonal_of_rectangle",
        "learning_objective_id": "math_g8_pyth_diag_rect",
        "hints": {
            "tier_1": f"Diagonal d² = {l_val}² + {w_val}².",
            "tier_2": f"d = sqrt({d_val*d_val}).",
            "tier_3": f"{d_val} cm.",
        },
        "misconception_tags": ["multiplying_length_by_width_for_diagonal"],
    }


# ----------------------------------------------------------------------
# 36. Context: Diagonal of a Square (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_36_context_diagonal_of_square(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([5, 6, 8, 10])
    d_sq = 2 * s * s
    d_val = math.sqrt(d_sq)
    d_str = _fmt_dec(d_val, 1)

    prompt = (
        f"A square garden plot has side lengths of **{s} m**.\n\n"
        f"Calculate the diagonal distance from one corner of the garden to the opposite corner (round to 1 decimal place)."
    )
    sol = (
        f"**Calculation of Diagonal:**\n"
        f"\\[ d^2 = s^2 + s^2 = 2s^2 \\quad [\\text{{Pythagoras in square}}] \\]\n"
        f"\\[ d^2 = {s}^2 + {s}^2 = {s*s} + {s*s} = {d_sq} \\]\n"
        f"\\[ d = \\sqrt{{{d_sq}}} = {s}\\sqrt{{2}} \\approx {d_str}\\text{{ m}} \\]"
    )
    ans = f"{d_str} m"
    return {
        "id": f"g8_pyth_diag_sq_{rng.randint(100000, 999999)}",
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
        "subskill": "36_context_diagonal_of_square",
        "learning_objective_id": "math_g8_pyth_diag_sq",
        "hints": {
            "tier_1": f"d² = {s}² + {s}² = {d_sq}.",
            "tier_2": f"d = sqrt({d_sq}).",
            "tier_3": f"{d_str} m.",
        },
        "misconception_tags": ["assuming_diagonal_equals_side_length"],
    }


# ----------------------------------------------------------------------
# 37. Context: Flagpole Guy Wire Support (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_37_context_flagpole_guy_wire_support(rng: random.Random) -> Dict[str, Any]:
    h_pole = rng.choice([8, 12, 15])
    dist_anchor = rng.choice([6, 9, 8])
    if (h_pole, dist_anchor) == (8, 6):
        wire = 10
    elif (h_pole, dist_anchor) == (12, 9):
        wire = 15
    else:
        h_pole, dist_anchor, wire = 15, 8, 17

    prompt = (
        f"A vertical flagpole **{h_pole} m** tall is supported by a straight steel guy wire anchored "
        f"to level ground **{dist_anchor} m** from the base of the pole.\n\n"
        f"Calculate the length of the guy wire in meters."
    )
    sol = (
        f"**Calculation of Wire Length:**\n"
        f"\\[ \\text{{wire}}^2 = \\text{{height}}^2 + \\text{{distance}}^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ \\text{{wire}}^2 = {h_pole}^2 + {dist_anchor}^2 = {h_pole*h_pole} + {dist_anchor*dist_anchor} = {wire*wire} \\]\n"
        f"\\[ \\text{{wire}} = \\sqrt{{{wire*wire}}} = {wire}\\text{{ m}} \\]"
    )
    ans = f"{wire} m"
    return {
        "id": f"g8_pyth_wire_{rng.randint(100000, 999999)}",
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
        "subskill": "37_context_flagpole_guy_wire_support",
        "learning_objective_id": "math_g8_pyth_wire",
        "hints": {
            "tier_1": f"wire² = {h_pole}² + {dist_anchor}².",
            "tier_2": f"wire² = {wire*wire}.",
            "tier_3": f"{wire} m.",
        },
        "misconception_tags": ["subtracting_pole_height_from_anchor_distance"],
    }


# ----------------------------------------------------------------------
# 38. Context: Ramp Slope Distance (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_38_context_ramp_slope_distance(rng: random.Random) -> Dict[str, Any]:
    rise = rng.choice([1.5, 2.0, 2.5])
    run = rng.choice([2.0, 3.0, 4.0])
    slope_sq = rise * rise + run * run
    slope_val = math.sqrt(slope_sq)
    slope_str = _fmt_dec(slope_val, 2)

    prompt = (
        f"A wheelchair access ramp has a horizontal run of **{run:.1f} m** and reaches a vertical rise of **{rise:.1f} m**.\n\n"
        f"Calculate the slanted travel length of the ramp surface in meters (round to 2 decimal places)."
    )
    sol = (
        f"**Calculation of Slanted Ramp Length:**\n"
        f"\\[ \\text{{ramp}}^2 = \\text{{run}}^2 + \\text{{rise}}^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ \\text{{ramp}}^2 = {run:.1f}^2 + {rise:.1f}^2 = {run*run:.2f} + {rise*rise:.2f} = {slope_sq:.2f} \\]\n"
        f"\\[ \\text{{ramp}} = \\sqrt{{{slope_sq:.2f}}} \\approx {slope_str}\\text{{ m}} \\]"
    )
    ans = f"{slope_str} m"
    return {
        "id": f"g8_pyth_ramp_{rng.randint(100000, 999999)}",
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
        "subskill": "38_context_ramp_slope_distance",
        "learning_objective_id": "math_g8_pyth_ramp",
        "hints": {
            "tier_1": f"ramp² = {run}² + {rise}².",
            "tier_2": f"Take square root of {slope_sq:.2f}.",
            "tier_3": f"{slope_str} m.",
        },
        "misconception_tags": ["confusing_ramp_slanted_length_with_horizontal_run"],
    }


# ----------------------------------------------------------------------
# 39. Context: Altitude of Isosceles Triangle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_39_context_altitude_of_isosceles_triangle(rng: random.Random) -> Dict[str, Any]:
    # half base = 6, equal side = 10 -> h = 8
    # or half base = 5, equal side = 13 -> h = 12
    half_b, side, h_val = rng.choice([(6, 10, 8), (5, 13, 12), (8, 17, 15)])
    full_b = half_b * 2

    prompt = (
        f"An isosceles triangle has a base of **{full_b} cm** and two equal sides of **{side} cm** each.\n\n"
        f"1. Explain why the perpendicular altitude bisects the base into two equal segments of {half_b} cm.\n"
        f"2. Calculate the perpendicular height (altitude) of the triangle in cm."
    )
    sol = (
        f"**1. Explanation:** In an isosceles triangle, the perpendicular height dropped from the vertex between "
        f"the equal sides to the base bisects both the vertex angle and the base, forming two congruent right-angled triangles.\n\n"
        f"**2. Height Calculation:**\n"
        f"\\[ h^2 = \\text{{side}}^2 - (\\text{{half base}})^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ h^2 = {side}^2 - {half_b}^2 = {side*side} - {half_b*half_b} = {h_val*h_val} \\]\n"
        f"\\[ h = \\sqrt{{{h_val*h_val}}} = {h_val}\\text{{ cm}} \\]"
    )
    ans = f"1. altitude bisects base due to symmetry / congruent triangles; 2. {h_val} cm"
    return {
        "id": f"g8_pyth_iso_alt_{rng.randint(100000, 999999)}",
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
        "subskill": "39_context_altitude_of_isosceles_triangle",
        "learning_objective_id": "math_g8_pyth_iso_alt",
        "hints": {
            "tier_1": f"Half the base is {half_b} cm.",
            "tier_2": f"h² = {side}² - {half_b}² = {h_val*h_val}.",
            "tier_3": f"{h_val} cm.",
        },
        "misconception_tags": ["using_full_base_length_instead_of_half_base"],
    }


# ----------------------------------------------------------------------
# 40. Context: Altitude of Equilateral Triangle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_40_context_altitude_of_equilateral_triangle(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([6, 8, 10, 12])
    half_s = s // 2
    h_sq = s * s - half_s * half_s
    h_val = math.sqrt(h_sq)
    h_str = _fmt_dec(h_val, 1)

    prompt = (
        f"An equilateral triangle has all three sides equal to **{s} cm**.\n\n"
        f"1. State the length of half the base when the altitude is dropped.\n"
        f"2. Calculate the perpendicular altitude of the triangle (round to 1 decimal place)."
    )
    sol = (
        f"**1. Half the base:** \\({s} \\div 2 = {half_s}\\text{{ cm}}\\).\n\n"
        f"**2. Height Calculation:**\n"
        f"\\[ h^2 = s^2 - (s/2)^2 = {s}^2 - {half_s}^2 = {s*s} - {half_s*half_s} = {h_sq} \\]\n"
        f"\\[ h = \\sqrt{{{h_sq}}} = {half_s}\\sqrt{{3}} \\approx {h_str}\\text{{ cm}} \\]"
    )
    ans = f"1. {half_s} cm; 2. {h_str} cm"
    return {
        "id": f"g8_pyth_equil_alt_{rng.randint(100000, 999999)}",
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
        "subskill": "40_context_altitude_of_equilateral_triangle",
        "learning_objective_id": "math_g8_pyth_equil_alt",
        "hints": {
            "tier_1": f"Base is split into {half_s} cm.",
            "tier_2": f"h² = {s}² - {half_s}² = {h_sq}.",
            "tier_3": f"{h_str} cm.",
        },
        "misconception_tags": ["using_full_side_length_as_base_in_pythagoras"],
    }


# ----------------------------------------------------------------------
# 41. Coordinate Geometry Distance Between Two Points (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_41_coordinate_geometry_distance_between_two_points(rng: random.Random) -> Dict[str, Any]:
    x1, y1 = 1, 2
    dx, dy, d = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13)])
    x2, y2 = x1 + dx, y1 + dy

    prompt = (
        f"Points \\(A({x1}; {y1})\\) and \\(B({x2}; {y2})\\) lie on a Cartesian coordinate plane.\n\n"
        f"1. Explain how the Theorem of Pythagoras is used to find the distance between two points.\n"
        f"2. Calculate the straight-line distance \\(AB\\)."
    )
    sol = (
        f"**1. Explanation:** The horizontal change \\(\\Delta x = x_2 - x_1 = {dx}\\) and vertical change "
        f"\\(\\Delta y = y_2 - y_1 = {dy}\\) form perpendicular legs of a right-angled triangle, where distance \\(AB\\) "
        f"is the hypotenuse.\n\n"
        f"**2. Calculation:**\n"
        f"\\[ AB^2 = (\\Delta x)^2 + (\\Delta y)^2 = {dx}^2 + {dy}^2 = {dx*dx} + {dy*dy} = {d*d} \\]\n"
        f"\\[ AB = \\sqrt{{{d*d}}} = {d}\\text{{ units}} \\]"
    )
    ans = f"1. horizontal dx and vertical dy form legs of right triangle where AB is hypotenuse; 2. {d} units"
    return {
        "id": f"g8_pyth_coord_dist_{rng.randint(100000, 999999)}",
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
        "subskill": "41_coordinate_geometry_distance_between_two_points",
        "learning_objective_id": "math_g8_pyth_coord_dist",
        "hints": {
            "tier_1": f"Δx = {x2} - {x1} = {dx}; Δy = {y2} - {y1} = {dy}.",
            "tier_2": f"AB² = {dx}² + {dy}² = {d*d}.",
            "tier_3": f"{d} units.",
        },
        "misconception_tags": ["subtracting_coordinates_inconsistently"],
    }


# ----------------------------------------------------------------------
# 42. Coordinate Geometry Distance From Origin (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_42_coordinate_geometry_distance_from_origin(rng: random.Random) -> Dict[str, Any]:
    x, y, d = rng.choice([(6, 8, 10), (8, 15, 17), (5, 12, 13)])
    prompt = (
        f"A point \\(P({x}; {y})\\) lies in the Cartesian plane.\n\n"
        f"Calculate the distance from the origin \\((0; 0)\\) to point \\(P\\)."
    )
    sol = (
        f"**Calculation of Distance OP:**\n"
        f"\\[ OP^2 = x^2 + y^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ OP^2 = {x}^2 + {y}^2 = {x*x} + {y*y} = {d*d} \\]\n"
        f"\\[ OP = \\sqrt{{{d*d}}} = {d}\\text{{ units}} \\]"
    )
    ans = f"{d} units"
    return {
        "id": f"g8_pyth_dist_origin_{rng.randint(100000, 999999)}",
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
        "subskill": "42_coordinate_geometry_distance_from_origin",
        "learning_objective_id": "math_g8_pyth_dist_origin",
        "hints": {
            "tier_1": f"OP² = {x}² + {y}².",
            "tier_2": f"OP² = {d*d}.",
            "tier_3": f"{d} units.",
        },
        "misconception_tags": ["adding_x_and_y_without_squaring"],
    }


# ----------------------------------------------------------------------
# 43. Perimeter of Right-Angled Triangle Using Pythagoras (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_43_perimeter_of_right_angled_triangle_using_pythagoras(rng: random.Random) -> Dict[str, Any]:
    a, b, c = rng.choice([(5, 12, 13), (6, 8, 10), (9, 12, 15), (8, 15, 17)])
    perim = a + b + c

    prompt = (
        f"A right-angled triangle has two perpendicular sides measuring **{a} cm** and **{b} cm**.\n\n"
        f"1. Calculate the length of the hypotenuse \\(c\\).\n"
        f"2. Calculate the perimeter of the triangle."
    )
    sol = (
        f"**1. Hypotenuse:**\n"
        f"\\[ c^2 = a^2 + b^2 = {a}^2 + {b}^2 = {a*a + b*b} \\implies c = {c}\\text{{ cm}} \\]\n\n"
        f"**2. Perimeter:**\n"
        f"\\[ P = a + b + c = {a} + {b} + {c} = {perim}\\text{{ cm}} \\]"
    )
    ans = f"1. {c} cm; 2. {perim} cm"
    return {
        "id": f"g8_pyth_perim_{rng.randint(100000, 999999)}",
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
        "subskill": "43_perimeter_of_right_angled_triangle_using_pythagoras",
        "learning_objective_id": "math_g8_pyth_perim",
        "hints": {
            "tier_1": f"Find c first: c = sqrt({a}² + {b}²).",
            "tier_2": f"Add all three sides: {a} + {b} + {c}.",
            "tier_3": f"{perim} cm.",
        },
        "misconception_tags": ["forgetting_to_add_the_hypotenuse_to_perimeter"],
    }


# ----------------------------------------------------------------------
# 44. Area of Right-Angled Triangle Given Hypotenuse and Leg (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_44_area_of_right_angled_triangle_given_hypotenuse_and_leg(rng: random.Random) -> Dict[str, Any]:
    a, b, c = rng.choice([(6, 8, 10), (5, 12, 13), (9, 12, 15)])
    area = (a * b) // 2

    prompt = (
        f"A right-angled triangle has a hypotenuse of **{c} cm** and one perpendicular side of **{b} cm**.\n\n"
        f"1. Calculate the length of the other perpendicular side \\(a\\).\n"
        f"2. Calculate the area of the triangle in cm²."
    )
    sol = (
        f"**1. Perpendicular leg \\(a\\):**\n"
        f"\\[ a^2 = c^2 - b^2 = {c}^2 - {b}^2 = {c*c} - {b*b} = {a*a} \\implies a = {a}\\text{{ cm}} \\]\n\n"
        f"**2. Area of triangle:**\n"
        f"\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} = \\frac{{1}}{{2}} \\times {b} \\times {a} = {area}\\text{{ cm}}^2 \\]"
    )
    ans = f"1. {a} cm; 2. {area} cm²"
    return {
        "id": f"g8_pyth_area_given_hyp_{rng.randint(100000, 999999)}",
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
        "subskill": "44_area_of_right_angled_triangle_given_hypotenuse_and_leg",
        "learning_objective_id": "math_g8_pyth_area_given_hyp",
        "hints": {
            "tier_1": f"Find missing leg first: a = sqrt({c}² - {b}²).",
            "tier_2": f"Area = 1/2 * {b} * {a}.",
            "tier_3": f"{a} cm; {area} cm².",
        },
        "misconception_tags": ["using_hypotenuse_as_height_in_area_formula"],
    }


# ----------------------------------------------------------------------
# 45. Composite Area: Rectangle Plus Right Triangle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_45_composite_area_rectangle_plus_right_triangle(rng: random.Random) -> Dict[str, Any]:
    l_rect = rng.choice([10, 12, 14])
    h_rect = rng.choice([6, 8])
    tri_b = 6
    tri_h = h_rect
    a_rect = l_rect * h_rect
    a_tri = (tri_b * tri_h) // 2
    total_a = a_rect + a_tri

    prompt = (
        f"A composite shape consists of a rectangle measuring **{l_rect} cm by {h_rect} cm** "
        f"with a right-angled triangle attached to its side (base **{tri_b} cm**, height **{h_rect} cm**).\n\n"
        f"1. Calculate the area of the rectangle and the area of the attached triangle.\n"
        f"2. Calculate the total area of the composite shape."
    )
    sol = (
        f"**1. Separate Areas:**\n"
        f"- Rectangle area = \\({l_rect} \\times {h_rect} = {a_rect}\\text{{ cm}}^2\\)\n"
        f"- Triangle area = \\(\\frac{{1}}{{2}} \\times {tri_b} \\times {tri_h} = {a_tri}\\text{{ cm}}^2\\)\n\n"
        f"**2. Total Area:**\n"
        f"\\[ \\text{{Total Area}} = {a_rect} + {a_tri} = {total_a}\\text{{ cm}}^2 \\]"
    )
    ans = f"1. {a_rect} cm², {a_tri} cm²; 2. {total_a} cm²"
    return {
        "id": f"g8_pyth_comp_area_{rng.randint(100000, 999999)}",
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
        "subskill": "45_composite_area_rectangle_plus_right_triangle",
        "learning_objective_id": "math_g8_pyth_comp_area",
        "hints": {
            "tier_1": "Add the rectangle area and the triangle area.",
            "tier_2": f"{a_rect} + {a_tri}.",
            "tier_3": f"{total_a} cm².",
        },
        "misconception_tags": ["forgetting_half_factor_for_triangle_area"],
    }


# ----------------------------------------------------------------------
# 46. Composite Perimeter Shape With Right Triangle Slant (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_46_composite_perimeter_shape_with_right_triangle_slant(rng: random.Random) -> Dict[str, Any]:
    # Trapezoid-like shape: bottom = 14, top = 10, vertical height = 3, slant dx = 4 -> slant c = 5
    top = 10
    h_val = 3
    dx = 4
    bottom = top + dx
    slant = 5
    perim = top + h_val + bottom + slant

    prompt = (
        f"A right-trapezium shape has a top parallel edge of **{top} cm**, a vertical perpendicular edge of **{h_val} cm**, "
        f"and a bottom parallel edge of **{bottom} cm**.\n\n"
        f"1. Use Pythagoras on the right-triangle projection (base = {dx} cm, height = {h_val} cm) to calculate the slanted side length.\n"
        f"2. Calculate the total perimeter of the trapezium."
    )
    sol = (
        f"**1. Slanted side length:**\n"
        f"\\[ c^2 = {dx}^2 + {h_val}^2 = 16 + 9 = 25 \\implies c = 5\\text{{ cm}} \\]\n\n"
        f"**2. Total Perimeter:**\n"
        f"\\[ P = {top} + {h_val} + {bottom} + {slant} = {perim}\\text{{ cm}} \\]"
    )
    ans = f"1. 5 cm; 2. {perim} cm"
    return {
        "id": f"g8_pyth_comp_perim_{rng.randint(100000, 999999)}",
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
        "subskill": "46_composite_perimeter_shape_with_right_triangle_slant",
        "learning_objective_id": "math_g8_pyth_comp_perim",
        "hints": {
            "tier_1": f"Slanted side = sqrt({dx}² + {h_val}²) = 5 cm.",
            "tier_2": f"Add the 4 outer edges: {top} + {h_val} + {bottom} + 5.",
            "tier_3": f"{perim} cm.",
        },
        "misconception_tags": ["adding_internal_height_to_perimeter"],
    }


# ----------------------------------------------------------------------
# 47. Rhombus Diagonals and Side Length (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_47_rhombus_diagonals_and_side_length(rng: random.Random) -> Dict[str, Any]:
    # half diagonals 6 and 8 -> side = 10
    # or half diagonals 5 and 12 -> side = 13
    d1_half, d2_half, s = rng.choice([(6, 8, 10), (5, 12, 13)])
    d1 = d1_half * 2
    d2 = d2_half * 2

    prompt = (
        f"A rhombus has diagonals of lengths **{d1} cm** and **{d2} cm**.\n\n"
        f"1. State the geometric property regarding the intersection angle of the diagonals of a rhombus.\n"
        f"2. Calculate the side length of the rhombus."
    )
    sol = (
        f"**1. Diagonals property:** The diagonals of a rhombus bisect each other perpendicularly at **90°**.\n\n"
        f"**2. Side length calculation:**\n"
        f"The four right-angled triangles created have legs equal to half the diagonals:\n"
        f"\\[ a = {d1}/2 = {d1_half}\\text{{ cm}}, \\quad b = {d2}/2 = {d2_half}\\text{{ cm}} \\]\n"
        f"\\[ s^2 = {d1_half}^2 + {d2_half}^2 = {d1_half*d1_half} + {d2_half*d2_half} = {s*s} \\]\n"
        f"\\[ s = \\sqrt{{{s*s}}} = {s}\\text{{ cm}} \\]"
    )
    ans = f"1. diagonals bisect each other at 90°; 2. {s} cm"
    return {
        "id": f"g8_pyth_rhombus_{rng.randint(100000, 999999)}",
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
        "subskill": "47_rhombus_diagonals_and_side_length",
        "learning_objective_id": "math_g8_pyth_rhombus",
        "hints": {
            "tier_1": f"Half diagonals are {d1_half} cm and {d2_half} cm.",
            "tier_2": f"s² = {d1_half}² + {d2_half}² = {s*s}.",
            "tier_3": f"{s} cm.",
        },
        "misconception_tags": ["using_full_diagonal_lengths_instead_of_half"],
    }


# ----------------------------------------------------------------------
# 48. Pythagorean Triples Scaling Rule (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_48_pythagorean_triples_scaling_rule(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([3, 5, 7, 10])
    a, b, c = 3 * k, 4 * k, 5 * k

    prompt = (
        f"The numbers \\((3; 4; 5)\\) form a primitive Pythagorean triple because \\(3^2 + 4^2 = 5^2\\).\n\n"
        f"1. If each number in a Pythagorean triple \\((a; b; c)\\) is multiplied by a positive integer \\(k = {k}\\), "
        f"explain algebraically why \\((ka; kb; kc)\\) is also a Pythagorean triple.\n"
        f"2. Write down the scaled triple for \\(k = {k}\\)."
    )
    sol = (
        f"**1. Algebraic Proof:**\n"
        f"\\[ (ka)^2 + (kb)^2 = k^2 a^2 + k^2 b^2 = k^2 (a^2 + b^2) \\]\n"
        f"Since \\(a^2 + b^2 = c^2\\):\n"
        f"\\[ k^2 (a^2 + b^2) = k^2 c^2 = (kc)^2 \\]\n"
        f"Thus, \\((ka)^2 + (kb)^2 = (kc)^2\\), proving that any scalar multiple of a triple is also a triple.\n\n"
        f"**2. Scaled Triple:** \\(({a}; {b}; {c})\\)."
    )
    ans = f"1. (ka)² + (kb)² = k²(a² + b²) = k²c² = (kc)²; 2. ({a}; {b}; {c})"
    return {
        "id": f"g8_pyth_triple_scale_{rng.randint(100000, 999999)}",
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
        "subskill": "48_pythagorean_triples_scaling_rule",
        "learning_objective_id": "math_g8_pyth_triple_scale",
        "hints": {
            "tier_1": f"Multiply 3, 4, 5 each by {k}.",
            "tier_2": f"3*{k} = {a}, 4*{k} = {b}, 5*{k} = {c}.",
            "tier_3": f"({a}; {b}; {c}).",
        },
        "misconception_tags": ["scaling_only_the_two_legs_without_scaling_hypotenuse"],
    }


# ----------------------------------------------------------------------
# 49. Two-Step Pythagoras: Adjacent Right Triangles (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_49_two_step_pythagoras_adjacent_right_triangles(rng: random.Random) -> Dict[str, Any]:
    # Triangle 1: legs 3 and 4 -> shared hypotenuse = 5
    # Triangle 2: shared leg = 5, other leg = 12 -> final hypotenuse = 13
    prompt = (
        "Two right-angled triangles share a common side \\(BD\\):\n"
        "- In the first triangle \\(\\triangle ABD\\), perpendicular legs are \\(AB = 3\\text{{ cm}}\\) and \\(AD = 4\\text{{ cm}}\\).\n"
        "- In the second triangle \\(\\triangle BCD\\), \\(BD\\) is a perpendicular leg and \\(BC = 12\\text{{ cm}}\\).\n\n"
        "1. Calculate the length of the shared side \\(BD\\).\n"
        "2. Calculate the length of hypotenuse \\(CD\\) in the second triangle."
    )
    sol = (
        "**1. Step 1: Calculate BD in \\(\\triangle ABD\\):**\n"
        "\\[ BD^2 = AB^2 + AD^2 = 3^2 + 4^2 = 9 + 16 = 25 \\implies BD = 5\\text{{ cm}} \\]\n\n"
        "**2. Step 2: Calculate CD in \\(\\triangle BCD\\):**\n"
        "\\[ CD^2 = BD^2 + BC^2 = 5^2 + 12^2 = 25 + 144 = 169 \\implies CD = 13\\text{{ cm}} \\]"
    )
    ans = "1. BD = 5 cm; 2. CD = 13 cm"
    return {
        "id": f"g8_pyth_adj_tri_{rng.randint(100000, 999999)}",
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
        "subskill": "49_two_step_pythagoras_adjacent_right_triangles",
        "learning_objective_id": "math_g8_pyth_adj_tri",
        "hints": {
            "tier_1": "Find BD first: sqrt(3² + 4²) = 5 cm.",
            "tier_2": "Then find CD: sqrt(5² + 12²).",
            "tier_3": "BD = 5 cm; CD = 13 cm.",
        },
        "misconception_tags": ["adding_all_legs_together_in_single_step"],
    }


# ----------------------------------------------------------------------
# 50. Pythagoras Word Problem: Tree Broken by Wind (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_50_pythagoras_word_problem_tree_broken_by_wind(rng: random.Random) -> Dict[str, Any]:
    # stump = 5, top touches at 12 m from base -> broken fallen part = 13 m -> original tree = 5 + 13 = 18 m
    stump = 5
    dist = 12
    fallen = 13
    orig_h = stump + fallen

    prompt = (
        f"A strong wind storm snaps a vertical tree at a height of **{stump} m** above level ground.\n"
        f"The top of the tree falls over, remaining attached at the fracture point, and touches the ground "
        f"at a point **{dist} m** away from the base of the trunk.\n\n"
        f"1. Calculate the length of the broken fallen upper portion of the tree.\n"
        f"2. Calculate the original total height of the tree before it broke."
    )
    sol = (
        f"**1. Broken Upper Portion (Hypotenuse):**\n"
        f"\\[ c^2 = \\text{{stump}}^2 + \\text{{distance}}^2 \\quad [\\text{{Pythagoras / trunk }} \\perp \\text{{ ground}}] \\]\n"
        f"\\[ c^2 = {stump}^2 + {dist}^2 = 25 + 144 = 169 \\implies c = 13\\text{{ m}} \\]\n\n"
        f"**2. Original Total Height:**\n"
        f"\\[ \\text{{Total Height}} = \\text{{stump}} + \\text{{broken portion}} = {stump} + 13 = {orig_h}\\text{{ m}} \\]"
    )
    ans = f"1. 13 m; 2. {orig_h} m"
    return {
        "id": f"g8_pyth_tree_broken_{rng.randint(100000, 999999)}",
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
        "subskill": "50_pythagoras_word_problem_tree_broken_by_wind",
        "learning_objective_id": "math_g8_pyth_tree_broken",
        "hints": {
            "tier_1": f"Fallen part = sqrt({stump}² + {dist}²) = 13 m.",
            "tier_2": f"Add the {stump} m stump to the 13 m fallen part.",
            "tier_3": f"13 m; {orig_h} m.",
        },
        "misconception_tags": ["forgetting_to_add_the_stump_height_for_original_tree_height"],
    }
