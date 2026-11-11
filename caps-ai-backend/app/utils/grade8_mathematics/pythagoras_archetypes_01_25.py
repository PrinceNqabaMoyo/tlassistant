"""Grade 8 Mathematics — Pythagoras Archetypes 01 to 25.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr8/Term 3/03. The theorem of Pythagoras.md

Archetypes covering:
  - 01 to 05: Hypotenuse definition, Pythagoras theorem statement, area square proof, 3-4-5 and 5-12-13 triples.
  - 06 to 12: Hypotenuse calculation for scaled triples (8-15-17, 7-24-25, 9-40-41), decimal rounding, surd form, isosceles right triangle.
  - 13 to 20: Calculating shorter leg (a² = c² - b²), triples, decimal rounding, and surds.
  - 21 to 25: Leg in surd form, hypotenuse inequality checks, converse theorem statement, converse verification, right-angle vertex identification.

Strictly zero-LLM, deterministic execution, 100% CAPS compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .pythagoras_svg import (
    draw_pythagoras_triangle_svg,
    draw_pythagoras_squares_proof_svg,
)


def _fmt_dec(v: float, places: int = 1) -> str:
    s = f"{v:.{places}f}"
    return s.replace(".", ",")


# ----------------------------------------------------------------------
# 01. Identify Hypotenuse and Right Angle Relationship
# ----------------------------------------------------------------------
def arch_01_identify_hypotenuse_and_right_angle_relationship(rng: random.Random) -> Dict[str, Any]:
    tri = rng.choice(["ABC", "PQR", "XYZ"])
    right_v = tri[1]
    hyp = f"{tri[0]}{tri[2]}"

    prompt = (
        f"In right-angled \\(\\triangle {tri}\\), the interior angle \\(\\hat{{{right_v}}} = 90^\\circ\\).\n\n"
        f"1. What is the mathematical name for the side opposite the 90° angle?\n"
        f"2. Name the specific hypotenuse side for \\(\\triangle {tri}\\).\n"
        f"3. State how the length of the hypotenuse compares to the other two sides."
    )
    sol = (
        f"**1. Mathematical Name:** The **hypotenuse**.\n\n"
        f"**2. Hypotenuse in \\(\\triangle {tri}\\):** Side **\\({hyp}\\)** (the side directly opposite vertex \\(\\hat{{{right_v}}}\\)).\n\n"
        f"**3. Length Comparison:** The hypotenuse is strictly the **longest side** in any right-angled triangle."
    )
    ans = f"1. hypotenuse; 2. {hyp}; 3. longest side"
    return {
        "id": f"g8_pyth_id_hyp_{rng.randint(100000, 999999)}",
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
        "subskill": "01_identify_hypotenuse_and_right_angle_relationship",
        "learning_objective_id": "math_g8_pyth_id_hyp",
        "hints": {
            "tier_1": "The side opposite the 90° angle is the hypotenuse.",
            "tier_2": f"Opposite vertex {right_v} is side {hyp}.",
            "tier_3": f"Hypotenuse; {hyp}; longest side.",
        },
        "misconception_tags": ["identifying_an_adjacent_leg_as_hypotenuse"],
    }


# ----------------------------------------------------------------------
# 02. State Theorem of Pythagoras Formula and Reasons
# ----------------------------------------------------------------------
def arch_02_state_theorem_of_pythagoras_formula_and_reasons(rng: random.Random) -> Dict[str, Any]:
    tri = rng.choice(["DEF", "KLM", "ABC"])
    v90 = tri[1]
    s_hyp = f"{tri[0]}{tri[2]}"
    s1 = f"{tri[0]}{tri[1]}"
    s2 = f"{tri[1]}{tri[2]}"

    prompt = (
        f"In \\(\\triangle {tri}\\), the angle \\(\\hat{{{v90}}} = 90^\\circ\\).\n\n"
        f"1. State the Theorem of Pythagoras in terms of the side names of \\(\\triangle {tri}\\).\n"
        f"2. Write down the formal geometric reason required in CAPS examination marking."
    )
    sol = (
        f"**1. Theorem Formula:**\n"
        f"\\[ {s_hyp}^2 = {s1}^2 + {s2}^2 \\]\n\n"
        f"**2. Formal Exam Reason:**\n"
        f"\\([\\text{{Pythagoras}} / \\hat{{{v90}}} = 90^\\circ]\\)"
    )
    ans = f"1. {s_hyp}² = {s1}² + {s2}²; 2. [Pythagoras / {v90} = 90°]"
    return {
        "id": f"g8_pyth_state_thm_{rng.randint(100000, 999999)}",
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
        "subskill": "02_state_theorem_of_pythagoras_formula_and_reasons",
        "learning_objective_id": "math_g8_pyth_state_thm",
        "hints": {
            "tier_1": f"The square on the hypotenuse {s_hyp} equals sum of squares on other two sides.",
            "tier_2": f"{s_hyp}² = {s1}² + {s2}².",
            "tier_3": f"{s_hyp}² = {s1}² + {s2}²; [Pythagoras / {v90} = 90°].",
        },
        "misconception_tags": ["forgetting_to_write_geometric_reasons_in_pythagoras"],
    }


# ----------------------------------------------------------------------
# 03. Pythagoras Area Proof: Squares on Sides (WITH SVG)
# ----------------------------------------------------------------------
def arch_03_pythagoras_area_proof_squares_on_sides(rng: random.Random) -> Dict[str, Any]:
    scale = rng.choice([1, 2])
    a, b, c = 3 * scale, 4 * scale, 5 * scale
    a2, b2, c2 = a * a, b * b, c * c
    svg = draw_pythagoras_squares_proof_svg(a, b, c, seed=rng.randint(100, 999999))

    prompt = (
        f"Geometric squares are constructed on each side of a right-angled triangle with perpendicular legs "
        f"**\\(a = {a}\\text{{ cm}}\\)** and **\\(b = {b}\\text{{ cm}}\\)**:\n\n"
        f"1. Calculate the area of the square on leg \\(a\\) and on leg \\(b\\).\n"
        f"2. Use the area relationship \\(c^2 = a^2 + b^2\\) to state the area of the square on the hypotenuse \\(c\\).\n"
        f"3. Determine the length of the hypotenuse \\(c\\)."
    )
    sol = (
        f"**1. Areas of squares on legs:**\n"
        f"- Area on leg \\(a\\): \\(a^2 = {a}^2 = {a2}\\text{{ cm}}^2\\)\n"
        f"- Area on leg \\(b\\): \\(b^2 = {b}^2 = {b2}\\text{{ cm}}^2\\)\n\n"
        f"**2. Area of square on hypotenuse:**\n"
        f"\\[ c^2 = a^2 + b^2 = {a2} + {b2} = {c2}\\text{{ cm}}^2 \\]\n\n"
        f"**3. Length of hypotenuse:**\n"
        f"\\[ c = \\sqrt{{{c2}}} = {c}\\text{{ cm}} \\]"
    )
    ans = f"1. {a2} cm², {b2} cm²; 2. {c2} cm²; 3. {c} cm"
    return {
        "id": f"g8_pyth_area_proof_{rng.randint(100000, 999999)}",
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
        "subskill": "03_pythagoras_area_proof_squares_on_sides",
        "learning_objective_id": "math_g8_pyth_area_proof",
        "hints": {
            "tier_1": "Square each side length to find the areas.",
            "tier_2": f"{a}² + {b}² = {a2} + {b2} = {c2}.",
            "tier_3": f"c = sqrt({c2}) = {c} cm.",
        },
        "misconception_tags": ["adding_lengths_directly_without_squaring"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 04. Calculate Hypotenuse Triple 3-4-5 Scaled (WITH SVG)
# ----------------------------------------------------------------------
def arch_04_calculate_hypotenuse_triple_3_4_5_scaled(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2, 3, 4])
    a, b, c = 3 * k, 4 * k, 5 * k
    svg = draw_pythagoras_triangle_svg(a, b, c, "B", "C", "A", unknown="c", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\), side \\(AB = {a}\\text{{ cm}}\\), "
        f"and side \\(BC = {b}\\text{{ cm}}\\).\n\n"
        f"Calculate the length of the hypotenuse \\(AC\\), showing full working and reasons."
    )
    sol = (
        f"**Calculation of Hypotenuse AC:**\n"
        f"\\[ AC^2 = AB^2 + BC^2 \\quad [\\text{{Pythagoras / }} \\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ AC^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {c*c} \\]\n"
        f"\\[ AC = \\sqrt{{{c*c}}} = {c}\\text{{ cm}} \\]"
    )
    ans = f"{c} cm"
    return {
        "id": f"g8_pyth_hyp_345_{rng.randint(100000, 999999)}",
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
        "subskill": "04_calculate_hypotenuse_triple_3_4_5_scaled",
        "learning_objective_id": "math_g8_pyth_hyp_345",
        "hints": {
            "tier_1": f"AC² = {a}² + {b}².",
            "tier_2": f"AC² = {a*a} + {b*b} = {c*c}.",
            "tier_3": f"AC = {c} cm.",
        },
        "misconception_tags": ["forgetting_square_root_at_final_step"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 05. Calculate Hypotenuse Triple 5-12-13 Scaled (WITH SVG)
# ----------------------------------------------------------------------
def arch_05_calculate_hypotenuse_triple_5_12_13_scaled(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    a, b, c = 5 * k, 12 * k, 13 * k
    svg = draw_pythagoras_triangle_svg(a, b, c, "Q", "R", "P", unknown="c", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle PQR\\), \\(\\hat{{Q}} = 90^\\circ\\), \\(PQ = {a}\\text{{ cm}}\\), "
        f"and \\(QR = {b}\\text{{ cm}}\\).\n\n"
        f"Determine the length of hypotenuse \\(PR\\) with geometric reasons."
    )
    sol = (
        f"**Calculation of Hypotenuse PR:**\n"
        f"\\[ PR^2 = PQ^2 + QR^2 \\quad [\\text{{Pythagoras / }} \\hat{{Q}} = 90^\\circ] \\]\n"
        f"\\[ PR^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {c*c} \\]\n"
        f"\\[ PR = \\sqrt{{{c*c}}} = {c}\\text{{ cm}} \\]"
    )
    ans = f"{c} cm"
    return {
        "id": f"g8_pyth_hyp_51213_{rng.randint(100000, 999999)}",
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
        "subskill": "05_calculate_hypotenuse_triple_5_12_13_scaled",
        "learning_objective_id": "math_g8_pyth_hyp_51213",
        "hints": {
            "tier_1": f"PR² = {a}² + {b}².",
            "tier_2": f"PR² = {a*a} + {b*b} = {c*c}.",
            "tier_3": f"PR = {c} cm.",
        },
        "misconception_tags": ["adding_without_squaring"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 06. Calculate Hypotenuse Triple 8-15-17 Scaled (WITH SVG)
# ----------------------------------------------------------------------
def arch_06_calculate_hypotenuse_triple_8_15_17_scaled(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    a, b, c = 8 * k, 15 * k, 17 * k
    svg = draw_pythagoras_triangle_svg(a, b, c, "Y", "Z", "X", unknown="c", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle XYZ\\), \\(\\hat{{Y}} = 90^\\circ\\), \\(XY = {a}\\text{{ mm}}\\), "
        f"and \\(YZ = {b}\\text{{ mm}}\\).\n\n"
        f"Calculate the length of the hypotenuse \\(XZ\\)."
    )
    sol = (
        f"**Calculation of Hypotenuse XZ:**\n"
        f"\\[ XZ^2 = XY^2 + YZ^2 \\quad [\\text{{Pythagoras / }} \\hat{{Y}} = 90^\\circ] \\]\n"
        f"\\[ XZ^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {c*c} \\]\n"
        f"\\[ XZ = \\sqrt{{{c*c}}} = {c}\\text{{ mm}} \\]"
    )
    ans = f"{c} mm"
    return {
        "id": f"g8_pyth_hyp_81517_{rng.randint(100000, 999999)}",
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
        "subskill": "06_calculate_hypotenuse_triple_8_15_17_scaled",
        "learning_objective_id": "math_g8_pyth_hyp_81517",
        "hints": {
            "tier_1": f"XZ² = {a}² + {b}².",
            "tier_2": f"XZ² = {a*a} + {b*b} = {c*c}.",
            "tier_3": f"XZ = {c} mm.",
        },
        "misconception_tags": ["forgetting_units_mm"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 07. Calculate Hypotenuse Triple 7-24-25 Scaled (WITH SVG)
# ----------------------------------------------------------------------
def arch_07_calculate_hypotenuse_triple_7_24_25_scaled(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    a, b, c = 7 * k, 24 * k, 25 * k
    svg = draw_pythagoras_triangle_svg(a, b, c, "B", "C", "A", unknown="c", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\), side \\(AB = {a}\\text{{ cm}}\\), "
        f"and side \\(BC = {b}\\text{{ cm}}\\).\n\n"
        f"Calculate the length of hypotenuse \\(AC\\)."
    )
    sol = (
        f"**Calculation of AC:**\n"
        f"\\[ AC^2 = AB^2 + BC^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ AC^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {c*c} \\]\n"
        f"\\[ AC = \\sqrt{{{c*c}}} = {c}\\text{{ cm}} \\]"
    )
    ans = f"{c} cm"
    return {
        "id": f"g8_pyth_hyp_72425_{rng.randint(100000, 999999)}",
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
        "subskill": "07_calculate_hypotenuse_triple_7_24_25_scaled",
        "learning_objective_id": "math_g8_pyth_hyp_72425",
        "hints": {
            "tier_1": f"AC² = {a}² + {b}².",
            "tier_2": f"{a*a} + {b*b} = {c*c}.",
            "tier_3": f"AC = {c} cm.",
        },
        "misconception_tags": ["arithmetic_error_in_squaring_24"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 08. Calculate Hypotenuse Triple 9-40-41 Scaled (WITH SVG)
# ----------------------------------------------------------------------
def arch_08_calculate_hypotenuse_triple_9_40_41_scaled(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    a, b, c = 9 * k, 40 * k, 41 * k
    svg = draw_pythagoras_triangle_svg(a, b, c, "E", "F", "D", unknown="c", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle DEF\\), \\(\\hat{{E}} = 90^\\circ\\), \\(DE = {a}\\text{{ m}}\\), "
        f"and \\(EF = {b}\\text{{ m}}\\).\n\n"
        f"Determine the length of hypotenuse \\(DF\\)."
    )
    sol = (
        f"**Calculation of DF:**\n"
        f"\\[ DF^2 = DE^2 + EF^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ DF^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {c*c} \\]\n"
        f"\\[ DF = \\sqrt{{{c*c}}} = {c}\\text{{ m}} \\]"
    )
    ans = f"{c} m"
    return {
        "id": f"g8_pyth_hyp_94041_{rng.randint(100000, 999999)}",
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
        "subskill": "08_calculate_hypotenuse_triple_9_40_41_scaled",
        "learning_objective_id": "math_g8_pyth_hyp_94041",
        "hints": {
            "tier_1": "DF² = 9² + 40².",
            "tier_2": "81 + 1600 = 1681.",
            "tier_3": "DF = 41 m.",
        },
        "misconception_tags": ["arithmetic_error_in_squaring_40"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 09. Calculate Hypotenuse Non-Integer Round 1 Decimal (WITH SVG)
# ----------------------------------------------------------------------
def arch_09_calculate_hypotenuse_non_integer_round_1_decimal(rng: random.Random) -> Dict[str, Any]:
    a, b = rng.choice([(5, 7), (4, 6), (6, 9), (5, 8)])
    c_val = math.sqrt(a * a + b * b)
    c_str = _fmt_dec(c_val, 1)
    svg = draw_pythagoras_triangle_svg(a, b, round(c_val, 1), "B", "C", "A", unknown="c", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\), side \\(AB = {a}\\text{{ cm}}\\), "
        f"and side \\(BC = {b}\\text{{ cm}}\\).\n\n"
        f"Calculate the length of the hypotenuse \\(AC\\), rounded off to **1 decimal place**."
    )
    sol = (
        f"**Calculation of AC:**\n"
        f"\\[ AC^2 = AB^2 + BC^2 \\quad [\\text{{Pythagoras / }} \\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ AC^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {a*a + b*b} \\]\n"
        f"\\[ AC = \\sqrt{{{a*a + b*b}}} \\approx {c_str}\\text{{ cm}} \\]"
    )
    ans = f"{c_str} cm"
    return {
        "id": f"g8_pyth_hyp_dec1_{rng.randint(100000, 999999)}",
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
        "subskill": "09_calculate_hypotenuse_non_integer_round_1_decimal",
        "learning_objective_id": "math_g8_pyth_hyp_dec1",
        "hints": {
            "tier_1": f"AC² = {a}² + {b}² = {a*a + b*b}.",
            "tier_2": f"Take the square root of {a*a + b*b}.",
            "tier_3": f"AC ≈ {c_str} cm.",
        },
        "misconception_tags": ["rounding_off_prematurely_before_square_root"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 10. Calculate Hypotenuse Non-Integer Round 2 Decimals (WITH SVG)
# ----------------------------------------------------------------------
def arch_10_calculate_hypotenuse_non_integer_round_2_decimals(rng: random.Random) -> Dict[str, Any]:
    a, b = rng.choice([(3, 7), (5, 9), (7, 11), (6, 10)])
    c_val = math.sqrt(a * a + b * b)
    c_str = _fmt_dec(c_val, 2)
    svg = draw_pythagoras_triangle_svg(a, b, round(c_val, 2), "Q", "R", "P", unknown="c", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle PQR\\), \\(\\hat{{Q}} = 90^\\circ\\), side \\(PQ = {a}\\text{{ cm}}\\), "
        f"and side \\(QR = {b}\\text{{ cm}}\\).\n\n"
        f"Calculate the length of hypotenuse \\(PR\\) correct to **2 decimal places**."
    )
    sol = (
        f"**Calculation of PR:**\n"
        f"\\[ PR^2 = PQ^2 + QR^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ PR^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {a*a + b*b} \\]\n"
        f"\\[ PR = \\sqrt{{{a*a + b*b}}} \\approx {c_str}\\text{{ cm}} \\]"
    )
    ans = f"{c_str} cm"
    return {
        "id": f"g8_pyth_hyp_dec2_{rng.randint(100000, 999999)}",
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
        "subskill": "10_calculate_hypotenuse_non_integer_round_2_decimals",
        "learning_objective_id": "math_g8_pyth_hyp_dec2",
        "hints": {
            "tier_1": f"PR² = {a*a} + {b*b} = {a*a + b*b}.",
            "tier_2": f"Find sqrt({a*a + b*b}) to two decimal places.",
            "tier_3": f"PR ≈ {c_str} cm.",
        },
        "misconception_tags": ["incorrect_decimal_rounding"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 11. Calculate Hypotenuse Surd Exact Form (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_11_calculate_hypotenuse_surd_exact_form(rng: random.Random) -> Dict[str, Any]:
    a, b = rng.choice([(2, 3), (3, 5), (4, 7), (2, 5)])
    sum_sq = a * a + b * b

    prompt = (
        f"In a right-angled triangle, the lengths of the two perpendicular sides are **{a} cm** and **{b} cm**.\n\n"
        f"1. Calculate the exact length of the hypotenuse, leaving your answer in **surd form** (square root form).\n"
        f"2. Explain why writing an answer in surd form is more mathematically exact than a rounded decimal."
    )
    sol = (
        f"**1. Hypotenuse in surd form:**\n"
        f"\\[ c^2 = a^2 + b^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {sum_sq} \\]\n"
        f"\\[ c = \\sqrt{{{sum_sq}}}\\text{{ cm}} \\]\n\n"
        f"**2. Mathematical Exactness:** A surd representation \\(\\sqrt{{{sum_sq}}}\\) contains the exact true value "
        f"without any rounding error, whereas decimals for non-square numbers are non-terminating and non-recurring."
    )
    ans = f"1. sqrt({sum_sq}) cm; 2. surd represents exact value without rounding error"
    return {
        "id": f"g8_pyth_hyp_surd_{rng.randint(100000, 999999)}",
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
        "subskill": "11_calculate_hypotenuse_surd_exact_form",
        "learning_objective_id": "math_g8_pyth_hyp_surd",
        "hints": {
            "tier_1": f"c² = {a}² + {b}² = {sum_sq}.",
            "tier_2": f"Leave as sqrt({sum_sq}).",
            "tier_3": f"sqrt({sum_sq}) cm.",
        },
        "misconception_tags": ["approximating_to_decimal_when_surd_is_requested"],
    }


# ----------------------------------------------------------------------
# 12. Calculate Hypotenuse Isosceles Right-Angled Triangle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_12_calculate_hypotenuse_isosceles_right_angled_triangle(rng: random.Random) -> Dict[str, Any]:
    leg = rng.choice([4, 6, 8, 10])
    c_sq = 2 * leg * leg
    c_val = math.sqrt(c_sq)
    c_str = _fmt_dec(c_val, 2)

    prompt = (
        f"An isosceles right-angled triangle has two equal perpendicular sides, each of length **{leg} cm**.\n\n"
        f"1. Write an algebraic formula for the hypotenuse \\(c\\) in terms of leg length \\(x\\).\n"
        f"2. Calculate the length of the hypotenuse in cm (round to 2 decimal places)."
    )
    sol = (
        f"**1. Algebraic formula:**\n"
        f"\\[ c^2 = x^2 + x^2 = 2x^2 \\implies c = x\\sqrt{{2}} \\]\n\n"
        f"**2. Calculation for \\(x = {leg}\\):**\n"
        f"\\[ c^2 = {leg}^2 + {leg}^2 = {leg*leg} + {leg*leg} = {c_sq} \\]\n"
        f"\\[ c = \\sqrt{{{c_sq}}} = {leg}\\sqrt{{2}} \\approx {c_str}\\text{{ cm}} \\]"
    )
    ans = f"1. c = x*sqrt(2); 2. {c_str} cm"
    return {
        "id": f"g8_pyth_hyp_iso_{rng.randint(100000, 999999)}",
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
        "subskill": "12_calculate_hypotenuse_isosceles_right_angled_triangle",
        "learning_objective_id": "math_g8_pyth_hyp_iso",
        "hints": {
            "tier_1": f"c² = {leg}² + {leg}² = 2 * {leg*leg} = {c_sq}.",
            "tier_2": f"Take the square root of {c_sq}.",
            "tier_3": f"{c_str} cm.",
        },
        "misconception_tags": ["doubling_leg_length_instead_of_multiplying_by_sqrt2"],
    }


# ----------------------------------------------------------------------
# 13. Calculate Leg Rearrangement Formula (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_13_calculate_leg_rearrangement_formula(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a right-angled triangle with hypotenuse \\(c\\) and perpendicular legs \\(a\\) and \\(b\\):\n\n"
        "1. Starting from \\(c^2 = a^2 + b^2\\), make \\(a^2\\) the subject of the formula.\n"
        "2. Explain why calculating a shorter leg involves subtraction rather than addition."
    )
    sol = (
        "**1. Subject formula:**\n"
        "\\[ a^2 = c^2 - b^2 \\implies a = \\sqrt{c^2 - b^2} \\]\n\n"
        "**2. Explanation:** The hypotenuse \\(c\\) is the longest side whose square equals the sum of the squares "
        "of the other two sides. To find a shorter leg, we must subtract the square of the known leg from the square of the hypotenuse."
    )
    ans = "1. a² = c² - b²; 2. hypotenuse is the longest side so we subtract from c²"
    return {
        "id": f"g8_pyth_leg_rearr_{rng.randint(100000, 999999)}",
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
        "subskill": "13_calculate_leg_rearrangement_formula",
        "learning_objective_id": "math_g8_pyth_leg_rearr",
        "hints": {
            "tier_1": "Subtract b² from both sides of c² = a² + b².",
            "tier_2": "a² = c² - b².",
            "tier_3": ans,
        },
        "misconception_tags": ["adding_hypotenuse_squared_and_leg_squared_to_find_shorter_side"],
    }


# ----------------------------------------------------------------------
# 14. Calculate Leg Triple 3-4-5 Scaled (WITH SVG)
# ----------------------------------------------------------------------
def arch_14_calculate_leg_triple_3_4_5_scaled(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2, 3])
    a, b, c = 3 * k, 4 * k, 5 * k
    svg = draw_pythagoras_triangle_svg(a, b, c, "B", "C", "A", unknown="a", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\), hypotenuse \\(AC = {c}\\text{{ cm}}\\), "
        f"and leg \\(BC = {b}\\text{{ cm}}\\).\n\n"
        f"Calculate the length of perpendicular leg \\(AB\\), stating the geometric reason."
    )
    sol = (
        f"**Calculation of Leg AB:**\n"
        f"\\[ AB^2 = AC^2 - BC^2 \\quad [\\text{{Pythagoras / }} \\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ AB^2 = {c}^2 - {b}^2 = {c*c} - {b*b} = {a*a} \\]\n"
        f"\\[ AB = \\sqrt{{{a*a}}} = {a}\\text{{ cm}} \\]"
    )
    ans = f"{a} cm"
    return {
        "id": f"g8_pyth_leg_345_{rng.randint(100000, 999999)}",
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
        "subskill": "14_calculate_leg_triple_3_4_5_scaled",
        "learning_objective_id": "math_g8_pyth_leg_345",
        "hints": {
            "tier_1": f"AB² = AC² - BC² = {c}² - {b}².",
            "tier_2": f"AB² = {c*c} - {b*b} = {a*a}.",
            "tier_3": f"AB = {a} cm.",
        },
        "misconception_tags": ["adding_instead_of_subtracting_when_finding_leg"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 15. Calculate Leg Triple 5-12-13 Scaled (WITH SVG)
# ----------------------------------------------------------------------
def arch_15_calculate_leg_triple_5_12_13_scaled(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    a, b, c = 5 * k, 12 * k, 13 * k
    svg = draw_pythagoras_triangle_svg(a, b, c, "Q", "R", "P", unknown="b", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle PQR\\), \\(\\hat{{Q}} = 90^\\circ\\), hypotenuse \\(PR = {c}\\text{{ cm}}\\), "
        f"and leg \\(PQ = {a}\\text{{ cm}}\\).\n\n"
        f"Determine the length of leg \\(QR\\)."
    )
    sol = (
        f"**Calculation of Leg QR:**\n"
        f"\\[ QR^2 = PR^2 - PQ^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ QR^2 = {c}^2 - {a}^2 = {c*c} - {a*a} = {b*b} \\]\n"
        f"\\[ QR = \\sqrt{{{b*b}}} = {b}\\text{{ cm}} \\]"
    )
    ans = f"{b} cm"
    return {
        "id": f"g8_pyth_leg_51213_{rng.randint(100000, 999999)}",
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
        "subskill": "15_calculate_leg_triple_5_12_13_scaled",
        "learning_objective_id": "math_g8_pyth_leg_51213",
        "hints": {
            "tier_1": f"QR² = {c}² - {a}².",
            "tier_2": f"QR² = {c*c} - {a*a} = {b*b}.",
            "tier_3": f"QR = {b} cm.",
        },
        "misconception_tags": ["subtracting_in_wrong_order_causing_negative_square"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 16. Calculate Leg Triple 8-15-17 Scaled (WITH SVG)
# ----------------------------------------------------------------------
def arch_16_calculate_leg_triple_8_15_17_scaled(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    a, b, c = 8 * k, 15 * k, 17 * k
    svg = draw_pythagoras_triangle_svg(a, b, c, "Y", "Z", "X", unknown="a", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle XYZ\\), \\(\\hat{{Y}} = 90^\\circ\\), hypotenuse \\(XZ = {c}\\text{{ cm}}\\), "
        f"and leg \\(YZ = {b}\\text{{ cm}}\\).\n\n"
        f"Calculate the length of perpendicular side \\(XY\\)."
    )
    sol = (
        f"**Calculation of XY:**\n"
        f"\\[ XY^2 = XZ^2 - YZ^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ XY^2 = {c}^2 - {b}^2 = {c*c} - {b*b} = {a*a} \\]\n"
        f"\\[ XY = \\sqrt{{{a*a}}} = {a}\\text{{ cm}} \\]"
    )
    ans = f"{a} cm"
    return {
        "id": f"g8_pyth_leg_81517_{rng.randint(100000, 999999)}",
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
        "subskill": "16_calculate_leg_triple_8_15_17_scaled",
        "learning_objective_id": "math_g8_pyth_leg_81517",
        "hints": {
            "tier_1": f"XY² = {c}² - {b}².",
            "tier_2": f"{c*c} - {b*b} = {a*a}.",
            "tier_3": f"XY = {a} cm.",
        },
        "misconception_tags": ["arithmetic_error_in_289_minus_225"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 17. Calculate Leg Triple 7-24-25 Scaled (WITH SVG)
# ----------------------------------------------------------------------
def arch_17_calculate_leg_triple_7_24_25_scaled(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([1, 2])
    a, b, c = 7 * k, 24 * k, 25 * k
    svg = draw_pythagoras_triangle_svg(a, b, c, "B", "C", "A", unknown="b", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\), hypotenuse \\(AC = {c}\\text{{ cm}}\\), "
        f"and leg \\(AB = {a}\\text{{ cm}}\\).\n\n"
        f"Determine the length of leg \\(BC\\)."
    )
    sol = (
        f"**Calculation of BC:**\n"
        f"\\[ BC^2 = AC^2 - AB^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ BC^2 = {c}^2 - {a}^2 = {c*c} - {a*a} = {b*b} \\]\n"
        f"\\[ BC = \\sqrt{{{b*b}}} = {b}\\text{{ cm}} \\]"
    )
    ans = f"{b} cm"
    return {
        "id": f"g8_pyth_leg_72425_{rng.randint(100000, 999999)}",
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
        "subskill": "17_calculate_leg_triple_7_24_25_scaled",
        "learning_objective_id": "math_g8_pyth_leg_72425",
        "hints": {
            "tier_1": f"BC² = {c}² - {a}².",
            "tier_2": f"{c*c} - {a*a} = {b*b}.",
            "tier_3": f"BC = {b} cm.",
        },
        "misconception_tags": ["arithmetic_error_in_subtracting_49"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 18. Calculate Leg Triple 6-8-10 Scaled (WITH SVG)
# ----------------------------------------------------------------------
def arch_18_calculate_leg_triple_6_8_10_scaled(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([2, 3])
    a, b, c = 3 * k, 4 * k, 5 * k
    svg = draw_pythagoras_triangle_svg(a, b, c, "E", "F", "D", unknown="a", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle DEF\\), \\(\\hat{{E}} = 90^\\circ\\), hypotenuse \\(DF = {c}\\text{{ cm}}\\), "
        f"and leg \\(EF = {b}\\text{{ cm}}\\).\n\n"
        f"Calculate the length of perpendicular leg \\(DE\\)."
    )
    sol = (
        f"**Calculation of DE:**\n"
        f"\\[ DE^2 = DF^2 - EF^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ DE^2 = {c}^2 - {b}^2 = {c*c} - {b*b} = {a*a} \\]\n"
        f"\\[ DE = \\sqrt{{{a*a}}} = {a}\\text{{ cm}} \\]"
    )
    ans = f"{a} cm"
    return {
        "id": f"g8_pyth_leg_6810_{rng.randint(100000, 999999)}",
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
        "subskill": "18_calculate_leg_triple_6_8_10_scaled",
        "learning_objective_id": "math_g8_pyth_leg_6810",
        "hints": {
            "tier_1": f"DE² = {c}² - {b}².",
            "tier_2": f"DE² = {c*c} - {b*b} = {a*a}.",
            "tier_3": f"DE = {a} cm.",
        },
        "misconception_tags": ["adding_instead_of_subtracting_legs"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 19. Calculate Leg Non-Integer Round 1 Decimal (WITH SVG)
# ----------------------------------------------------------------------
def arch_19_calculate_leg_non_integer_round_1_decimal(rng: random.Random) -> Dict[str, Any]:
    c, b = rng.choice([(10, 6), (12, 7), (15, 9), (14, 8)])
    a_sq = c * c - b * b
    a_val = math.sqrt(a_sq)
    a_str = _fmt_dec(a_val, 1)
    svg = draw_pythagoras_triangle_svg(round(a_val, 1), b, c, "B", "C", "A", unknown="a", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\), hypotenuse \\(AC = {c}\\text{{ cm}}\\), "
        f"and leg \\(BC = {b}\\text{{ cm}}\\).\n\n"
        f"Calculate the length of perpendicular leg \\(AB\\), rounded to **1 decimal place**."
    )
    sol = (
        f"**Calculation of AB:**\n"
        f"\\[ AB^2 = AC^2 - BC^2 \\quad [\\text{{Pythagoras / }} \\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ AB^2 = {c}^2 - {b}^2 = {c*c} - {b*b} = {a_sq} \\]\n"
        f"\\[ AB = \\sqrt{{{a_sq}}} \\approx {a_str}\\text{{ cm}} \\]"
    )
    ans = f"{a_str} cm"
    return {
        "id": f"g8_pyth_leg_dec1_{rng.randint(100000, 999999)}",
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
        "subskill": "19_calculate_leg_non_integer_round_1_decimal",
        "learning_objective_id": "math_g8_pyth_leg_dec1",
        "hints": {
            "tier_1": f"AB² = {c}² - {b}² = {a_sq}.",
            "tier_2": f"Find sqrt({a_sq}) to 1 decimal place.",
            "tier_3": f"AB ≈ {a_str} cm.",
        },
        "misconception_tags": ["adding_hypotenuse_and_leg_squares"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 20. Calculate Leg Non-Integer Round 2 Decimals (WITH SVG)
# ----------------------------------------------------------------------
def arch_20_calculate_leg_non_integer_round_2_decimals(rng: random.Random) -> Dict[str, Any]:
    c, a = rng.choice([(11, 4), (13, 6), (16, 7), (9, 5)])
    b_sq = c * c - a * a
    b_val = math.sqrt(b_sq)
    b_str = _fmt_dec(b_val, 2)
    svg = draw_pythagoras_triangle_svg(a, round(b_val, 2), c, "Q", "R", "P", unknown="b", seed=rng.randint(100, 999999))

    prompt = (
        f"In right-angled \\(\\triangle PQR\\), \\(\\hat{{Q}} = 90^\\circ\\), hypotenuse \\(PR = {c}\\text{{ cm}}\\), "
        f"and leg \\(PQ = {a}\\text{{ cm}}\\).\n\n"
        f"Calculate the length of leg \\(QR\\) correct to **2 decimal places**."
    )
    sol = (
        f"**Calculation of QR:**\n"
        f"\\[ QR^2 = PR^2 - PQ^2 \\quad [\\text{{Pythagoras}}] \\]\n"
        f"\\[ QR^2 = {c}^2 - {a}^2 = {c*c} - {a*a} = {b_sq} \\]\n"
        f"\\[ QR = \\sqrt{{{b_sq}}} \\approx {b_str}\\text{{ cm}} \\]"
    )
    ans = f"{b_str} cm"
    return {
        "id": f"g8_pyth_leg_dec2_{rng.randint(100000, 999999)}",
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
        "subskill": "20_calculate_leg_non_integer_round_2_decimals",
        "learning_objective_id": "math_g8_pyth_leg_dec2",
        "hints": {
            "tier_1": f"QR² = {c}² - {a}² = {b_sq}.",
            "tier_2": f"Find sqrt({b_sq}) to two decimal places.",
            "tier_3": f"QR ≈ {b_str} cm.",
        },
        "misconception_tags": ["rounding_error_in_second_decimal_place"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 21. Calculate Leg Exact Surd Form (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_21_calculate_leg_exact_surd_form(rng: random.Random) -> Dict[str, Any]:
    c, b = rng.choice([(6, 2), (8, 3), (7, 4), (10, 5)])
    diff_sq = c * c - b * b

    prompt = (
        f"A right-angled triangle has a hypotenuse of **{c} cm** and one leg of **{b} cm**.\n\n"
        f"Calculate the exact length of the other leg in **surd form** (simplest radical form)."
    )
    sol = (
        f"**Calculation:**\n"
        f"\\[ a^2 = c^2 - b^2 = {c}^2 - {b}^2 = {c*c} - {b*b} = {diff_sq} \\]\n"
        f"\\[ a = \\sqrt{{{diff_sq}}}\\text{{ cm}} \\]"
    )
    ans = f"sqrt({diff_sq}) cm"
    return {
        "id": f"g8_pyth_leg_surd_{rng.randint(100000, 999999)}",
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
        "subskill": "21_calculate_leg_exact_surd_form",
        "learning_objective_id": "math_g8_pyth_leg_surd",
        "hints": {
            "tier_1": f"a² = {c}² - {b}² = {diff_sq}.",
            "tier_2": f"Leave as sqrt({diff_sq}).",
            "tier_3": f"sqrt({diff_sq}) cm.",
        },
        "misconception_tags": ["evaluating_to_decimal_instead_of_surd"],
    }


# ----------------------------------------------------------------------
# 22. Identify Longest Side Rule in Right Triangle (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_22_identify_longest_side_rule_in_right_triangle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In Euclidean geometry, the relationship between side lengths and opposite angles is fundamental:\n\n"
        "1. In any triangle, which side is opposite the largest interior angle?\n"
        "2. Explain why the hypotenuse must strictly be the longest side in a right-angled triangle."
    )
    sol = (
        "**1. General Triangle Rule:** The side opposite the largest interior angle is always the longest side of the triangle.\n\n"
        "**2. In a right-angled triangle:** The sum of angles in a triangle is 180°. Since the right angle is 90°, "
        "the remaining two acute angles must sum to 90°, meaning each must be strictly less than 90°. "
        "Therefore, the 90° angle is the largest angle, and its opposite side (the hypotenuse) is strictly the longest side."
    )
    ans = "1. longest side is opposite largest angle; 2. 90° is the largest angle so hypotenuse is strictly the longest side"
    return {
        "id": f"g8_pyth_longest_rule_{rng.randint(100000, 999999)}",
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
        "subskill": "22_identify_longest_side_rule_in_right_triangle",
        "learning_objective_id": "math_g8_pyth_longest_rule",
        "hints": {
            "tier_1": "The largest angle is always opposite the longest side.",
            "tier_2": "In a right triangle, the other two angles must each be < 90°.",
            "tier_3": ans,
        },
        "misconception_tags": ["believing_a_leg_can_be_equal_to_or_longer_than_hypotenuse"],
    }


# ----------------------------------------------------------------------
# 23. Converse Theorem Statement and Meaning (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_23_converse_theorem_statement_and_meaning(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **Converse of the Theorem of Pythagoras** is used to test whether a triangle contains a right angle:\n\n"
        "1. State the Converse of the Theorem of Pythagoras in words.\n"
        "2. Contrast the starting condition of the Theorem of Pythagoras with that of its Converse."
    )
    sol = (
        "**1. Statement of Converse:** If in a triangle with sides \\(a\\), \\(b\\), and \\(c\\) (where \\(c\\) is the longest side), "
        "the square of the longest side equals the sum of the squares of the other two sides (\\(c^2 = a^2 + b^2\\)), "
        "then the triangle is a **right-angled triangle** with the 90° angle opposite side \\(c\\).\n\n"
        "**2. Difference:**\n"
        "- The **Theorem** starts with a known right-angled triangle and concludes \\(c^2 = a^2 + b^2\\).\n"
        "- The **Converse** starts with known side lengths satisfying \\(c^2 = a^2 + b^2\\) and concludes that the triangle contains a right angle (90°)."
    )
    ans = "1. if c² = a² + b² then the triangle is right-angled; 2. theorem assumes 90° to find lengths; converse uses lengths to prove 90°"
    return {
        "id": f"g8_pyth_converse_stmt_{rng.randint(100000, 999999)}",
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
        "subskill": "23_converse_theorem_statement_and_meaning",
        "learning_objective_id": "math_g8_pyth_converse_stmt",
        "hints": {
            "tier_1": "The converse works in reverse: lengths prove 90°.",
            "tier_2": "If c² = a² + b², then the triangle is right-angled.",
            "tier_3": ans,
        },
        "misconception_tags": ["confusing_theorem_of_pythagoras_with_its_converse"],
    }


# ----------------------------------------------------------------------
# 24. Converse Verify Right-Angled Triangle Triple (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_24_converse_verify_right_angled_triangle_triple(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["yes", "no"])
    if choice == "yes":
        a, b, c = rng.choice([(6, 8, 10), (9, 12, 15), (5, 12, 13), (8, 15, 17)])
        is_right = "Yes"
    else:
        a, b, c = rng.choice([(5, 6, 8), (4, 7, 9), (7, 9, 12), (6, 9, 11)])
        is_right = "No"

    lhs = a * a + b * b
    rhs = c * c
    comp = "=" if lhs == rhs else ("<" if lhs < rhs else ">")

    prompt = (
        f"A triangle has side lengths of **{a} cm**, **{b} cm**, and **{c} cm**.\n\n"
        f"1. Calculate \\(a^2 + b^2\\) and calculate \\(c^2\\).\n"
        f"2. Use the Converse of the Theorem of Pythagoras to determine whether this is a right-angled triangle."
    )
    sol = (
        f"**1. Squares calculation:**\n"
        f"\\[ a^2 + b^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {lhs} \\]\n"
        f"\\[ c^2 = {c}^2 = {rhs} \\]\n\n"
        f"**2. Conclusion:**\n"
        f"Since \\({lhs} {comp} {rhs}\\), \\(a^2 + b^2 {comp} c^2\\). "
        f"{'Therefore, by the Converse of Pythagoras, this IS a right-angled triangle.' if choice == 'yes' else 'Therefore, this is NOT a right-angled triangle.'}"
    )
    ans = f"1. a² + b² = {lhs}, c² = {rhs}; 2. {is_right}"
    return {
        "id": f"g8_pyth_conv_verify_{rng.randint(100000, 999999)}",
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
        "subskill": "24_converse_verify_right_angled_triangle_triple",
        "learning_objective_id": "math_g8_pyth_conv_verify",
        "hints": {
            "tier_1": f"Compare {a}² + {b}² with {c}².",
            "tier_2": f"{lhs} vs {rhs}.",
            "tier_3": f"{is_right}.",
        },
        "misconception_tags": ["assuming_any_triangle_with_whole_numbers_is_right_angled"],
    }


# ----------------------------------------------------------------------
# 25. Converse Identify Which Vertex is 90 Degrees (ZERO LEAK TRIGGERS)
# ----------------------------------------------------------------------
def arch_25_converse_identify_which_vertex_is_90_degrees(rng: random.Random) -> Dict[str, Any]:
    tri = rng.choice(["ABC", "PQR", "XYZ"])
    v_right = tri[1]
    hyp = f"{tri[0]}{tri[2]}"
    leg1 = f"{tri[0]}{tri[1]}"
    leg2 = f"{tri[1]}{tri[2]}"
    a, b, c = 9, 12, 15

    prompt = (
        f"In \\(\\triangle {tri}\\), the side lengths are \\({leg1} = {a}\\text{{ cm}}\\), "
        f"\\({leg2} = {b}\\text{{ cm}}\\), and \\({hyp} = {c}\\text{{ cm}}\\).\n\n"
        f"1. Verify that \\(\\triangle {tri}\\) is a right-angled triangle.\n"
        f"2. Identify exactly which vertex has the 90° right angle."
    )
    sol = (
        f"**1. Verification:**\n"
        f"\\[ {leg1}^2 + {leg2}^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {a*a + b*b} \\]\n"
        f"\\[ {hyp}^2 = {c}^2 = {c*c} \\]\n"
        f"Since \\({leg1}^2 + {leg2}^2 = {hyp}^2\\), \\(\\triangle {tri}\\) is a right-angled triangle.\n\n"
        f"**2. 90° Vertex:** The right angle is opposite the longest side \\({hyp}\\), which is vertex **\\(\\hat{{{v_right}}}\\)**."
    )
    ans = f"1. {a}² + {b}² = {c}² (81 + 144 = 225); 2. vertex {v_right}"
    return {
        "id": f"g8_pyth_conv_vertex_{rng.randint(100000, 999999)}",
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
        "subskill": "25_converse_identify_which_vertex_is_90_degrees",
        "learning_objective_id": "math_g8_pyth_conv_vertex",
        "hints": {
            "tier_1": "The 90° angle is opposite the longest side.",
            "tier_2": f"Opposite side {hyp} is vertex {v_right}.",
            "tier_3": f"Vertex {v_right}.",
        },
        "misconception_tags": ["picking_an_endpoint_of_hypotenuse_as_the_right_angle"],
    }
