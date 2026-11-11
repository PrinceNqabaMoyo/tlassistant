"""Grade 9 Mathematics - Theorem of Pythagoras Archetypes 01 to 25.
Grounded strictly in:
  curriculum_docs_auto/Mathematics_Gr9/Term 3/02. Pythagoras Theorem.md

Covers:
- Identifying hypotenuse and right angle
- Formal Pythagoras theorem statement and algebraic equations
- Pythagorean squares area investigation
- Calculating hypotenuse with canonical and primitive triples (3-4-5, 5-12-13, 8-15-17, 7-24-25, 9-40-41)
- Calculating hypotenuse in exact surd form and rounded decimal form
- Calculating shorter sides (legs) with integer, surd, and decimal results
- Converse of Pythagoras: proving right-angled vs not right-angled
- Classifying acute (c^2 < a^2 + b^2) vs obtuse (c^2 > a^2 + b^2) triangles
- Deducing the 90° vertex from converse relationship
- Pythagorean triple membership tests and Euclid's generation formula
- Algebraic Pythagoras linear unknown sides

100% AST pure, zero LLM calls, zero network imports.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from .pythagoras_svg import (
    draw_pythagorean_squares_svg,
    draw_right_triangle_svg,
)


# ----------------------------------------------------------------------
# 01. Identify Hypotenuse and Right Angle Position
# ----------------------------------------------------------------------
def arch_01_identify_hypotenuse_and_right_angle_position(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (("A", "B", "C"), "B", "AC", (4, 3)),
        (("P", "Q", "R"), "Q", "PR", (5, 12)),
        (("D", "E", "F"), "E", "DF", (8, 15)),
        (("X", "Y", "Z"), "Y", "XZ", (7, 24)),
        (("K", "L", "M"), "L", "KM", (9, 12)),
        (("M", "N", "P"), "N", "MP", (6, 8)),
    ]
    verts, rt_v, hyp, legs = rng.choice(configs)
    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=legs,
        labels=verts,
        right_angle_vertex=rt_v,
        seed=seed_val,
    )

    t_name = "".join(verts)
    prompt = (
        f"In right-angled triangle \\(\\triangle {t_name}\\) shown below, "
        f"the right angle is at vertex \\({rt_v}\\) (\\(\\hat{{{rt_v}}} = 90^\\circ\\)).\n\n"
        f"Identify the **hypotenuse** of \\(\\triangle {t_name}\\) and state the geometric reason for your choice."
    )
    sol = (
        f"**Hypotenuse Identification:**\n"
        f"The hypotenuse of \\(\\triangle {t_name}\\) is side **\\({hyp}\\)**.\n\n"
        f"**Geometric Reason:**\n"
        f"In any right-angled triangle, the hypotenuse is defined as the side opposite the \\(90^\\circ\\) right angle, "
        f"and it is always the longest side of the triangle."
    )
    return {
        "id": f"g9_pyth_hyp_id_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": hyp,
        "expected_answer": hyp,
        "sample_answer": f"Side {hyp} (side opposite the 90° right angle)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify {hyp} as the hypotenuse", "marks": 1},
            {"desc": f"State reason: side opposite the 90° angle ({rt_v})", "marks": 1},
        ],
        "hints": [
            f"Locate the 90° right-angle marker at vertex {rt_v}.",
            f"The hypotenuse is the side directly opposite vertex {rt_v}.",
            f"The hypotenuse is {hyp}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 02. Pythagoras Statement: Formal Algebraic Equation
# ----------------------------------------------------------------------
def arch_02_pythagoras_statement_formal_algebraic_equation(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (("A", "B", "C"), "B", "AC", "AB", "BC"),
        (("P", "Q", "R"), "Q", "PR", "PQ", "QR"),
        (("D", "E", "F"), "E", "DF", "DE", "EF"),
        (("K", "L", "M"), "L", "KM", "KL", "LM"),
        (("X", "Y", "Z"), "Y", "XZ", "XY", "YZ"),
        (("S", "T", "U"), "T", "SU", "ST", "TU"),
    ]
    verts, rt_v, hyp, l1, l2 = rng.choice(configs)
    t_name = "".join(verts)

    prompt = (
        f"In \\(\\triangle {t_name}\\), \\(\\hat{{{rt_v}}} = 90^\\circ\\). "
        f"Write down the formal algebraic statement of the Theorem of Pythagoras for this triangle "
        f"expressing the square on the hypotenuse in terms of the other two sides."
    )
    sol = (
        f"**Pythagoras Theorem Statement:**\n"
        f"\\[ {hyp}^2 = {l1}^2 + {l2}^2 \\quad [\\text{{Theorem of Pythagoras}}] \\]\n\n"
        f"In words: In right-angled \\(\\triangle {t_name}\\), the square on the hypotenuse (\\({hyp}^2\\)) "
        f"equals the sum of the squares on the other two legs (\\({l1}^2 + {l2}^2\\))."
    )
    return {
        "id": f"g9_pyth_stat_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{hyp}^2 = {l1}^2 + {l2}^2",
        "expected_answer": f"{hyp}^2 = {l1}^2 + {l2}^2",
        "sample_answer": f"{hyp}^2 = {l1}^2 + {l2}^2 [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Correctly identify hypotenuse {hyp}^2 on one side", "marks": 1},
            {"desc": f"Correct sum of squares of legs {l1}^2 + {l2}^2", "marks": 1},
        ],
        "hints": [
            f"The hypotenuse is opposite the 90° angle at {rt_v}, which is side {hyp}.",
            f"Apply (hypotenuse)² = (side 1)² + (side 2)².",
            f"The equation is {hyp}^2 = {l1}^2 + {l2}^2.",
        ],
    }


# ----------------------------------------------------------------------
# 03. Pythagorean Squares Area Investigation
# ----------------------------------------------------------------------
def arch_03_pythagorean_squares_area_investigation(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)]
    a, b, c = rng.choice(triples)
    area_a = a * a
    area_b = b * b
    area_c = c * c

    seed_val = rng.randint(1000, 999999)
    svg = draw_pythagorean_squares_svg(legs=(a, b), seed=seed_val)

    prompt = (
        f"A right-angled triangle has squares constructed along each of its three sides. "
        f"The area of the square on the first leg is \\({area_a}\\text{{ cm}}^2\\) and the area of the square "
        f"on the second leg is \\({area_b}\\text{{ cm}}^2\\).\n\n"
        f"1. Calculate the area of the square constructed on the hypotenuse.\n"
        f"2. Hence, determine the length of the hypotenuse of the triangle."
    )
    sol = (
        f"**Step 1: Calculate the area of the square on the hypotenuse.**\n"
        f"By Pythagoras' Theorem, the area of the square on the hypotenuse equals the sum of the areas of the squares on the other two sides:\n"
        f"\\[ \\text{{Area of square on hypotenuse}} = {area_a} + {area_b} = {area_c}\\text{{ cm}}^2 \\]\n\n"
        f"**Step 2: Determine the length of the hypotenuse.**\n"
        f"\\[ \\text{{Hypotenuse}} = \\sqrt{{{area_c}}} = {c}\\text{{ cm}} \\]"
    )
    return {
        "id": f"g9_pyth_sq_area_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Area = {area_c} cm², Hypotenuse = {c} cm",
        "expected_answer": f"{c} cm",
        "sample_answer": f"Area = {area_c} cm², Hypotenuse = {c} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Add square areas {area_a} + {area_b} = {area_c} cm²", "marks": 1},
            {"desc": f"State Area of square on hypotenuse = {area_c} cm²", "marks": 1},
            {"desc": f"Take square root to find hypotenuse = {c} cm", "marks": 1},
        ],
        "hints": [
            "The area of the square on the hypotenuse equals the sum of the areas on the legs.",
            f"Add {area_a} + {area_b} to find the area of the square.",
            f"The square root of {area_c} gives the hypotenuse ({c} cm).",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 04. Calculate Hypotenuse: Integer Triple Basic (3, 4, 5)
# ----------------------------------------------------------------------
def arch_04_calculate_hypotenuse_integer_triple_basic(rng: random.Random) -> Dict[str, Any]:
    unit = rng.choice(["cm", "mm", "m"])
    a, b, c = 3, 4, 5
    if rng.random() > 0.5:
        a, b = b, a

    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=(a, b),
        labels=("A", "B", "C"),
        side_labels={"AB": f"{b} {unit}", "BC": f"{a} {unit}", "AC": "x"},
        seed=seed_val,
    )

    prompt = (
        f"In right-angled \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\). "
        f"The two perpendicular sides are \\(AB = {b}\\text{{ {unit}}}\\) and \\(BC = {a}\\text{{ {unit}}}\\). "
        f"Calculate the length of the hypotenuse \\(AC\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ AC^2 = AB^2 + BC^2 \\quad [\\text{{Pythagoras with }}\\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ AC^2 = {b}^2 + {a}^2 \\]\n"
        f"\\[ AC^2 = {b*b} + {a*a} = {c*c} \\]\n"
        f"\\[ AC = \\sqrt{{{c*c}}} = {c}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_hyp_345_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{c} {unit}",
        "expected_answer": f"{c} {unit}",
        "sample_answer": f"{c} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras formula AC² = AB² + BC²", "marks": 1},
            {"desc": f"Substitute values: {b}² + {a}² = {c*c}", "marks": 1},
            {"desc": f"Calculate AC = {c} {unit}", "marks": 1},
        ],
        "hints": [
            "Use Pythagoras' Theorem: c² = a² + b².",
            f"Square both legs: {a}² = {a*a} and {b}² = {b*b}.",
            f"Add them: {a*a + b*b}, then take the square root ({c} {unit}).",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 05. Calculate Hypotenuse: Integer Triple Scaled (e.g. 6-8-10, 9-12-15)
# ----------------------------------------------------------------------
def arch_05_calculate_hypotenuse_integer_triple_scaled(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([2, 3, 4, 5, 6, 7])
    a, b, c = 3 * mult, 4 * mult, 5 * mult
    unit = rng.choice(["cm", "m", "mm"])
    if rng.random() > 0.5:
        a, b = b, a

    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=(a, b),
        labels=("P", "Q", "R"),
        side_labels={"AB": f"{b} {unit}", "BC": f"{a} {unit}", "AC": "PR = ?"},
        seed=seed_val,
    )

    prompt = (
        f"In \\(\\triangle PQR\\), \\(\\hat{{Q}} = 90^\\circ\\). "
        f"Given that \\(PQ = {b}\\text{{ {unit}}}\\) and \\(QR = {a}\\text{{ {unit}}}\\), "
        f"calculate the length of \\(PR\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ PR^2 = PQ^2 + QR^2 \\quad [\\text{{Pythagoras, }}\\hat{{Q}} = 90^\\circ] \\]\n"
        f"\\[ PR^2 = {b}^2 + {a}^2 \\]\n"
        f"\\[ PR^2 = {b*b} + {a*a} = {c*c} \\]\n"
        f"\\[ PR = \\sqrt{{{c*c}}} = {c}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_hyp_scaled_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{c} {unit}",
        "expected_answer": f"{c} {unit}",
        "sample_answer": f"{c} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras PR² = PQ² + QR²", "marks": 1},
            {"desc": f"Substitute: {b}² + {a}² = {c*c}", "marks": 1},
            {"desc": f"Calculate PR = {c} {unit}", "marks": 1},
        ],
        "hints": [
            "Use the Theorem of Pythagoras: PR² = PQ² + QR².",
            f"Calculate {b}² = {b*b} and {a}² = {a*a}.",
            f"Add to get {c*c}, then square root: PR = {c} {unit}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 06. Calculate Hypotenuse: Primitive Triple 5-12-13
# ----------------------------------------------------------------------
def arch_06_calculate_hypotenuse_primitive_triple_5_12_13(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([1, 2, 3])
    a, b, c = 5 * mult, 12 * mult, 13 * mult
    unit = rng.choice(["cm", "m"])
    if rng.random() > 0.5:
        a, b = b, a

    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=(a, b),
        labels=("D", "E", "F"),
        side_labels={"AB": f"{b} {unit}", "BC": f"{a} {unit}", "AC": "DF = ?"},
        seed=seed_val,
    )

    prompt = (
        f"In right-angled triangle \\(\\triangle DEF\\), \\(\\hat{{E}} = 90^\\circ\\). "
        f"The two perpendicular legs are \\(DE = {b}\\text{{ {unit}}}\\) and \\(EF = {a}\\text{{ {unit}}}\\). "
        f"Calculate the length of the hypotenuse \\(DF\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ DF^2 = DE^2 + EF^2 \\quad [\\text{{Pythagoras, }}\\hat{{E}} = 90^\\circ] \\]\n"
        f"\\[ DF^2 = {b}^2 + {a}^2 \\]\n"
        f"\\[ DF^2 = {b*b} + {a*a} = {c*c} \\]\n"
        f"\\[ DF = \\sqrt{{{c*c}}} = {c}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_hyp_51213_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{c} {unit}",
        "expected_answer": f"{c} {unit}",
        "sample_answer": f"{c} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras formula DF² = DE² + EF²", "marks": 1},
            {"desc": f"Evaluate sum of squares: {b*b} + {a*a} = {c*c}", "marks": 1},
            {"desc": f"Solve DF = {c} {unit}", "marks": 1},
        ],
        "hints": [
            "Apply Pythagoras' Theorem for hypotenuse DF.",
            f"Calculate {b}² + {a}² = {c*c}.",
            f"Take the square root: DF = {c} {unit}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 07. Calculate Hypotenuse: Primitive Triple 8-15-17
# ----------------------------------------------------------------------
def arch_07_calculate_hypotenuse_primitive_triple_8_15_17(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([1, 2])
    a, b, c = 8 * mult, 15 * mult, 17 * mult
    unit = rng.choice(["cm", "m"])
    if rng.random() > 0.5:
        a, b = b, a

    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=(a, b),
        labels=("K", "L", "M"),
        side_labels={"AB": f"{b} {unit}", "BC": f"{a} {unit}", "AC": "x"},
        seed=seed_val,
    )

    prompt = (
        f"In \\(\\triangle KLM\\), \\(\\hat{{L}} = 90^\\circ\\). "
        f"The sides enclosing the right angle are \\(KL = {b}\\text{{ {unit}}}\\) and \\(LM = {a}\\text{{ {unit}}}\\). "
        f"Find the length of hypotenuse \\(KM\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ KM^2 = KL^2 + LM^2 \\quad [\\text{{Pythagoras, }}\\hat{{L}} = 90^\\circ] \\]\n"
        f"\\[ KM^2 = {b}^2 + {a}^2 \\]\n"
        f"\\[ KM^2 = {b*b} + {a*a} = {c*c} \\]\n"
        f"\\[ KM = \\sqrt{{{c*c}}} = {c}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_hyp_81517_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{c} {unit}",
        "expected_answer": f"{c} {unit}",
        "sample_answer": f"{c} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras KM² = KL² + LM²", "marks": 1},
            {"desc": f"Substitute: {b*b} + {a*a} = {c*c}", "marks": 1},
            {"desc": f"Calculate KM = {c} {unit}", "marks": 1},
        ],
        "hints": [
            "Use the theorem: hypotenuse² = leg₁² + leg₂².",
            f"Add {b}² ({b*b}) and {a}² ({a*a}) to get {c*c}.",
            f"Take the square root of {c*c} ({c} {unit}).",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 08. Calculate Hypotenuse: Primitive Triple 7-24-25
# ----------------------------------------------------------------------
def arch_08_calculate_hypotenuse_primitive_triple_7_24_25(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([1, 2])
    a, b, c = 7 * mult, 24 * mult, 25 * mult
    unit = rng.choice(["cm", "m"])
    if rng.random() > 0.5:
        a, b = b, a

    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=(a, b),
        labels=("X", "Y", "Z"),
        side_labels={"AB": f"{b} {unit}", "BC": f"{a} {unit}", "AC": "XZ = ?"},
        seed=seed_val,
    )

    prompt = (
        f"In right-angled triangle \\(\\triangle XYZ\\), \\(\\hat{{Y}} = 90^\\circ\\). "
        f"Given \\(XY = {b}\\text{{ {unit}}}\\) and \\(YZ = {a}\\text{{ {unit}}}\\), "
        f"calculate the length of \\(XZ\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ XZ^2 = XY^2 + YZ^2 \\quad [\\text{{Pythagoras, }}\\hat{{Y}} = 90^\\circ] \\]\n"
        f"\\[ XZ^2 = {b}^2 + {a}^2 \\]\n"
        f"\\[ XZ^2 = {b*b} + {a*a} = {c*c} \\]\n"
        f"\\[ XZ = \\sqrt{{{c*c}}} = {c}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_hyp_72425_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{c} {unit}",
        "expected_answer": f"{c} {unit}",
        "sample_answer": f"{c} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras XZ² = XY² + YZ²", "marks": 1},
            {"desc": f"Substitute: {b*b} + {a*a} = {c*c}", "marks": 1},
            {"desc": f"Calculate XZ = {c} {unit}", "marks": 1},
        ],
        "hints": [
            "Use Pythagoras' Theorem: XZ² = XY² + YZ².",
            f"Square both sides: {b}² = {b*b}, {a}² = {a*a}.",
            f"Sum is {c*c}, so XZ = {c} {unit}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 09. Calculate Hypotenuse: Primitive Triple 9-40-41
# ----------------------------------------------------------------------
def arch_09_calculate_hypotenuse_primitive_triple_9_40_41(rng: random.Random) -> Dict[str, Any]:
    a, b, c = 9, 40, 41
    unit = rng.choice(["cm", "m"])
    if rng.random() > 0.5:
        a, b = b, a

    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=(a, b),
        labels=("A", "B", "C"),
        side_labels={"AB": f"{b} {unit}", "BC": f"{a} {unit}", "AC": "x"},
        seed=seed_val,
    )

    prompt = (
        f"In \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\). "
        f"If \\(AB = {b}\\text{{ {unit}}}\\) and \\(BC = {a}\\text{{ {unit}}}\\), "
        f"determine the exact length of hypotenuse \\(AC\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ AC^2 = AB^2 + BC^2 \\quad [\\text{{Pythagoras, }}\\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ AC^2 = {b}^2 + {a}^2 = {b*b} + {a*a} = {c*c} \\]\n"
        f"\\[ AC = \\sqrt{{{c*c}}} = {c}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_hyp_94041_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{c} {unit}",
        "expected_answer": f"{c} {unit}",
        "sample_answer": f"{c} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras formula AC² = AB² + BC²", "marks": 1},
            {"desc": f"Substitute: {b*b} + {a*a} = {c*c}", "marks": 1},
            {"desc": f"Calculate AC = {c} {unit}", "marks": 1},
        ],
        "hints": [
            "Use the Theorem of Pythagoras.",
            f"Add {b}² = {b*b} and {a}² = {a*a} to get {c*c}.",
            f"Take the square root: {c} {unit}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 10. Calculate Hypotenuse: Irrational Surd Form
# ----------------------------------------------------------------------
def arch_10_calculate_hypotenuse_irrational_surd_form(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (2, 3, 13),
        (3, 5, 34),
        (4, 5, 41),
        (2, 5, 29),
        (3, 6, 45),  # 3*sqrt(5)
        (4, 6, 52),  # 2*sqrt(13)
        (5, 7, 74),
        (6, 7, 85),
    ]
    a, b, sum_sq = rng.choice(configs)
    unit = rng.choice(["cm", "m"])
    if rng.random() > 0.5:
        a, b = b, a

    prompt = (
        f"In right-angled triangle \\(\\triangle PQR\\), \\(\\hat{{Q}} = 90^\\circ\\). "
        f"Side \\(PQ = {b}\\text{{ {unit}}}\\) and side \\(QR = {a}\\text{{ {unit}}}\\). "
        f"Calculate the length of the hypotenuse \\(PR\\), leaving your answer in **simplest surd form**."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ PR^2 = PQ^2 + QR^2 \\quad [\\text{{Pythagoras, }}\\hat{{Q}} = 90^\\circ] \\]\n"
        f"\\[ PR^2 = {b}^2 + {a}^2 \\]\n"
        f"\\[ PR^2 = {b*b} + {a*a} = {sum_sq} \\]\n"
        f"\\[ PR = \\sqrt{{{sum_sq}}}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_hyp_surd_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"√{sum_sq} {unit}",
        "expected_answer": f"√{sum_sq} {unit}",
        "sample_answer": f"√{sum_sq} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras formula PR² = PQ² + QR²", "marks": 1},
            {"desc": f"Substitute values: {b*b} + {a*a} = {sum_sq}", "marks": 1},
            {"desc": f"State exact surd form: PR = √{sum_sq} {unit}", "marks": 1},
        ],
        "hints": [
            "Use Pythagoras: PR² = PQ² + QR².",
            f"Add {b*b} and {a*a} to obtain {sum_sq}.",
            f"Leave the answer under the square root symbol: √{sum_sq} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 11. Calculate Hypotenuse: Decimal Rounding Two Places
# ----------------------------------------------------------------------
def arch_11_calculate_hypotenuse_decimal_rounding_two_places(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (4, 7), (5, 8), (6, 9), (7, 10), (8, 11), (5, 9), (6, 11)
    ]
    a, b = rng.choice(configs)
    unit = rng.choice(["cm", "m"])
    sum_sq = a * a + b * b
    hyp_exact = math.sqrt(sum_sq)
    hyp_rounded = round(hyp_exact, 2)
    # Format with South African comma
    hyp_sa = f"{hyp_rounded:.2f}".replace(".", ",")

    prompt = (
        f"In right-angled triangle \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\). "
        f"Given \\(AB = {b}\\text{{ {unit}}}\\) and \\(BC = {a}\\text{{ {unit}}}\\), "
        f"calculate the length of hypotenuse \\(AC\\). "
        f"Round your final answer to **two decimal places**."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ AC^2 = AB^2 + BC^2 \\quad [\\text{{Pythagoras, }}\\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ AC^2 = {b}^2 + {a}^2 = {b*b} + {a*a} = {sum_sq} \\]\n"
        f"\\[ AC = \\sqrt{{{sum_sq}}} \\approx {hyp_sa}\\text{{ {unit}}} \\quad [\\text{{rounded to 2 dec pl}}] \\]"
    )
    return {
        "id": f"g9_pyth_hyp_dec_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{hyp_sa} {unit}",
        "expected_answer": f"{hyp_sa} {unit}",
        "sample_answer": f"{hyp_sa} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras formula AC² = AB² + BC²", "marks": 1},
            {"desc": f"Calculate AC² = {sum_sq}", "marks": 1},
            {"desc": f"Calculate and round AC = {hyp_sa} {unit}", "marks": 1},
        ],
        "hints": [
            "Use Pythagoras: AC² = AB² + BC².",
            f"Add {b*b} + {a*a} = {sum_sq}.",
            f"Take the square root of {sum_sq} and round to 2 decimal places ({hyp_sa} {unit}).",
        ],
    }


# ----------------------------------------------------------------------
# 12. Calculate Shorter Side: Integer Subtraction (3-4-5 scaled)
# ----------------------------------------------------------------------
def arch_12_calculate_shorter_side_integer_subtraction(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([1, 2, 3, 4, 5])
    a, b, c = 3 * mult, 4 * mult, 5 * mult
    unit = rng.choice(["cm", "m"])
    # Unknown is a
    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=(a, b),
        labels=("A", "B", "C"),
        side_labels={"AB": f"{b} {unit}", "BC": "x = ?", "AC": f"{c} {unit}"},
        seed=seed_val,
    )

    prompt = (
        f"In right-angled triangle \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\). "
        f"The hypotenuse is \\(AC = {c}\\text{{ {unit}}}\\) and one leg is \\(AB = {b}\\text{{ {unit}}}\\). "
        f"Calculate the length of the unknown side \\(BC\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ AC^2 = AB^2 + BC^2 \\quad [\\text{{Pythagoras, }}\\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ BC^2 = AC^2 - AB^2 \\]\n"
        f"\\[ BC^2 = {c}^2 - {b}^2 \\]\n"
        f"\\[ BC^2 = {c*c} - {b*b} = {a*a} \\]\n"
        f"\\[ BC = \\sqrt{{{a*a}}} = {a}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_leg_int_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{a} {unit}",
        "expected_answer": f"{a} {unit}",
        "sample_answer": f"{a} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Rearrange Pythagoras to subtract: BC² = AC² - AB²", "marks": 1},
            {"desc": f"Substitute: {c*c} - {b*b} = {a*a}", "marks": 1},
            {"desc": f"Solve BC = {a} {unit}", "marks": 1},
        ],
        "hints": [
            "To find a shorter side, subtract the square of the known leg from the square of the hypotenuse.",
            f"Set up: BC² = {c}² - {b}² = {c*c} - {b*b}.",
            f"BC = √{a*a} = {a} {unit}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 13. Calculate Shorter Side: Primitive Triple 12 from 13 and 5
# ----------------------------------------------------------------------
def arch_13_calculate_shorter_side_primitive_triple_12_from_13_and_5(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([1, 2])
    a, b, c = 5 * mult, 12 * mult, 13 * mult
    unit = rng.choice(["cm", "m"])

    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=(a, b),
        labels=("P", "Q", "R"),
        side_labels={"AB": "PQ = ?", "BC": f"{a} {unit}", "AC": f"{c} {unit}"},
        seed=seed_val,
    )

    prompt = (
        f"In right-angled triangle \\(\\triangle PQR\\), \\(\\hat{{Q}} = 90^\\circ\\). "
        f"The hypotenuse is \\(PR = {c}\\text{{ {unit}}}\\) and side \\(QR = {a}\\text{{ {unit}}}\\). "
        f"Calculate the length of side \\(PQ\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ PQ^2 + QR^2 = PR^2 \\quad [\\text{{Pythagoras, }}\\hat{{Q}} = 90^\\circ] \\]\n"
        f"\\[ PQ^2 = PR^2 - QR^2 \\]\n"
        f"\\[ PQ^2 = {c}^2 - {a}^2 \\]\n"
        f"\\[ PQ^2 = {c*c} - {a*a} = {b*b} \\]\n"
        f"\\[ PQ = \\sqrt{{{b*b}}} = {b}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_leg_12_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{b} {unit}",
        "expected_answer": f"{b} {unit}",
        "sample_answer": f"{b} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply subtraction formula PQ² = PR² - QR²", "marks": 1},
            {"desc": f"Evaluate: {c*c} - {a*a} = {b*b}", "marks": 1},
            {"desc": f"Calculate PQ = {b} {unit}", "marks": 1},
        ],
        "hints": [
            "Subtract the square of the given leg from the square of the hypotenuse.",
            f"Calculate {c}² - {a}² = {c*c} - {a*a} = {b*b}.",
            f"Take the square root: PQ = {b} {unit}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 14. Calculate Shorter Side: Primitive Triple 15 from 17 and 8
# ----------------------------------------------------------------------
def arch_14_calculate_shorter_side_primitive_triple_15_from_17_and_8(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([1, 2])
    a, b, c = 8 * mult, 15 * mult, 17 * mult
    unit = rng.choice(["cm", "m"])

    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=(a, b),
        labels=("D", "E", "F"),
        side_labels={"AB": f"{b} {unit}", "BC": "EF = ?", "AC": f"{c} {unit}"},
        seed=seed_val,
    )

    prompt = (
        f"In \\(\\triangle DEF\\), \\(\\hat{{E}} = 90^\\circ\\). "
        f"The hypotenuse \\(DF = {c}\\text{{ {unit}}}\\) and leg \\(DE = {b}\\text{{ {unit}}}\\). "
        f"Calculate the length of the base \\(EF\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ EF^2 = DF^2 - DE^2 \\quad [\\text{{Pythagoras, }}\\hat{{E}} = 90^\\circ] \\]\n"
        f"\\[ EF^2 = {c}^2 - {b}^2 \\]\n"
        f"\\[ EF^2 = {c*c} - {b*b} = {a*a} \\]\n"
        f"\\[ EF = \\sqrt{{{a*a}}} = {a}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_leg_15_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{a} {unit}",
        "expected_answer": f"{a} {unit}",
        "sample_answer": f"{a} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras subtraction: EF² = DF² - DE²", "marks": 1},
            {"desc": f"Evaluate {c*c} - {b*b} = {a*a}", "marks": 1},
            {"desc": f"Calculate EF = {a} {unit}", "marks": 1},
        ],
        "hints": [
            "Use EF² = DF² - DE².",
            f"Subtract {b*b} from {c*c} to get {a*a}.",
            f"Square root of {a*a} is {a} {unit}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 15. Calculate Shorter Side: Primitive Triple 24 from 25 and 7
# ----------------------------------------------------------------------
def arch_15_calculate_shorter_side_primitive_triple_24_from_25_and_7(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([1, 2, 3])
    a, b, c = 7 * mult, 24 * mult, 25 * mult
    unit = rng.choice(["cm", "m"])

    seed_val = rng.randint(1000, 999999)
    svg = draw_right_triangle_svg(
        legs=(a, b),
        labels=("K", "L", "M"),
        side_labels={"AB": "KL = ?", "BC": f"{a} {unit}", "AC": f"{c} {unit}"},
        seed=seed_val,
    )

    prompt = (
        f"In right-angled triangle \\(\\triangle KLM\\), \\(\\hat{{L}} = 90^\\circ\\). "
        f"Given that hypotenuse \\(KM = {c}\\text{{ {unit}}}\\) and \\(LM = {a}\\text{{ {unit}}}\\), "
        f"determine the length of side \\(KL\\)."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ KL^2 = KM^2 - LM^2 \\quad [\\text{{Pythagoras, }}\\hat{{L}} = 90^\\circ] \\]\n"
        f"\\[ KL^2 = {c}^2 - {a}^2 = {c*c} - {a*a} = {b*b} \\]\n"
        f"\\[ KL = \\sqrt{{{b*b}}} = {b}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_leg_24_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{b} {unit}",
        "expected_answer": f"{b} {unit}",
        "sample_answer": f"{b} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply Pythagoras formula KL² = KM² - LM²", "marks": 1},
            {"desc": f"Substitute: {c*c} - {a*a} = {b*b}", "marks": 1},
            {"desc": f"Calculate KL = {b} {unit}", "marks": 1},
        ],
        "hints": [
            "Use KL² = KM² - LM².",
            f"Calculate {c*c} - {a*a} = {b*b}.",
            f"KL = √{b*b} = {b} {unit}.",
        ],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 16. Calculate Shorter Side: Surd Simplification
# ----------------------------------------------------------------------
def arch_16_calculate_shorter_side_surd_simplification(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (6, 4, 20),   # 6^2 - 4^2 = 20
        (7, 3, 40),   # 7^2 - 3^2 = 40
        (8, 5, 39),   # 8^2 - 5^2 = 39
        (9, 6, 45),   # 9^2 - 6^2 = 45
        (10, 7, 51),  # 10^2 - 7^2 = 51
        (8, 4, 48),   # 8^2 - 4^2 = 48
    ]
    hyp, leg, diff = rng.choice(configs)
    unit = rng.choice(["cm", "m"])

    prompt = (
        f"In right-angled triangle \\(\\triangle ABC\\), \\(\\hat{{B}} = 90^\\circ\\). "
        f"The hypotenuse is \\(AC = {hyp}\\text{{ {unit}}}\\) and leg \\(BC = {leg}\\text{{ {unit}}}\\). "
        f"Calculate the exact length of side \\(AB\\) in **simplest surd form**."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ AB^2 = AC^2 - BC^2 \\quad [\\text{{Pythagoras, }}\\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ AB^2 = {hyp}^2 - {leg}^2 \\]\n"
        f"\\[ AB^2 = {hyp*hyp} - {leg*leg} = {diff} \\]\n"
        f"\\[ AB = \\sqrt{{{diff}}}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_leg_surd_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"√{diff} {unit}",
        "expected_answer": f"√{diff} {unit}",
        "sample_answer": f"√{diff} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply subtraction AB² = AC² - BC²", "marks": 1},
            {"desc": f"Evaluate {hyp*hyp} - {leg*leg} = {diff}", "marks": 1},
            {"desc": f"State exact surd form: AB = √{diff} {unit}", "marks": 1},
        ],
        "hints": [
            "Subtract the square of the known leg from the square of the hypotenuse.",
            f"Subtract {leg*leg} from {hyp*hyp} to get {diff}.",
            f"Leave the answer in surd form: √{diff} {unit}.",
        ],
    }


# ----------------------------------------------------------------------
# 17. Calculate Shorter Side: Decimal Rounding
# ----------------------------------------------------------------------
def arch_17_calculate_shorter_side_decimal_rounding(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (10, 6), (11, 7), (12, 8), (14, 9), (15, 10), (16, 11)
    ]
    hyp, leg = rng.choice(configs)
    unit = rng.choice(["cm", "m"])
    diff = hyp * hyp - leg * leg
    side_exact = math.sqrt(diff)
    side_rounded = round(side_exact, 2)
    side_sa = f"{side_rounded:.2f}".replace(".", ",")

    prompt = (
        f"In right-angled triangle \\(\\triangle PQR\\), \\(\\hat{{Q}} = 90^\\circ\\). "
        f"Hypotenuse \\(PR = {hyp}\\text{{ {unit}}}\\) and leg \\(QR = {leg}\\text{{ {unit}}}\\). "
        f"Calculate the length of side \\(PQ\\), rounded to **two decimal places**."
    )
    sol = (
        f"**Statement | Reason:**\n"
        f"\\[ PQ^2 = PR^2 - QR^2 \\quad [\\text{{Pythagoras, }}\\hat{{Q}} = 90^\\circ] \\]\n"
        f"\\[ PQ^2 = {hyp}^2 - {leg}^2 = {hyp*hyp} - {leg*leg} = {diff} \\]\n"
        f"\\[ PQ = \\sqrt{{{diff}}} \\approx {side_sa}\\text{{ {unit}}} \\quad [\\text{{rounded to 2 dec pl}}] \\]"
    )
    return {
        "id": f"g9_pyth_leg_dec_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{side_sa} {unit}",
        "expected_answer": f"{side_sa} {unit}",
        "sample_answer": f"{side_sa} {unit} [Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": "Apply subtraction PQ² = PR² - QR²", "marks": 1},
            {"desc": f"Calculate PQ² = {diff}", "marks": 1},
            {"desc": f"Calculate and round PQ = {side_sa} {unit}", "marks": 1},
        ],
        "hints": [
            "Use PQ² = PR² - QR².",
            f"Calculate {hyp*hyp} - {leg*leg} = {diff}.",
            f"Take the square root of {diff} and round to 2 decimal places ({side_sa} {unit}).",
        ],
    }


# ----------------------------------------------------------------------
# 18. Converse Pythagoras: Verify Right-Angled (YES)
# ----------------------------------------------------------------------
def arch_18_converse_pythagoras_verify_right_angled_yes(rng: random.Random) -> Dict[str, Any]:
    triples = [
        (3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15),
        (8, 15, 17), (7, 24, 25), (10, 24, 26), (15, 20, 25)
    ]
    a, b, c = rng.choice(triples)
    unit = rng.choice(["cm", "mm", "m"])

    prompt = (
        f"A triangle has side lengths of \\({a}\\text{{ {unit}}}\\), \\({b}\\text{{ {unit}}}\\), "
        f"and \\({c}\\text{{ {unit}}}\\).\n\n"
        f"Use the **Converse of the Theorem of Pythagoras** to show whether this triangle is right-angled. "
        f"Show all calculations clearly."
    )
    sol = (
        f"**Converse of Pythagoras Test:**\n"
        f"Identify the longest side: \\(c = {c}\\text{{ {unit}}}\\).\n\n"
        f"1. Square of the longest side:\n"
        f"\\[ ({c})^2 = {c*c} \\]\n\n"
        f"2. Sum of the squares of the two shorter sides:\n"
        f"\\[ ({a})^2 + ({b})^2 = {a*a} + {b*b} = {a*a + b*b} \\]\n\n"
        f"**Conclusion:**\n"
        f"Since \\({a}^2 + {b}^2 = {c}^2\\) (both equal \\({c*c}\\)), the triangle **is a right-angled triangle** "
        f"[Converse of Pythagoras]."
    )
    return {
        "id": f"g9_pyth_conv_yes_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "Yes, it is right-angled (a² + b² = c²)",
        "expected_answer": "Yes, it is right-angled",
        "sample_answer": f"Yes; {a}² + {b}² = {c}² ({c*c}) [Converse Pythagoras]",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate square of longest side: {c}² = {c*c}", "marks": 1},
            {"desc": f"Calculate sum of squares of legs: {a}² + {b}² = {c*c}", "marks": 1},
            {"desc": "Conclude triangle is right-angled [Converse of Pythagoras]", "marks": 1},
        ],
        "hints": [
            f"The longest side is {c}.",
            f"Compare {c}² with {a}² + {b}².",
            "If they are equal, the triangle is right-angled.",
        ],
    }


# ----------------------------------------------------------------------
# 19. Converse Pythagoras: Verify Right-Angled (NO)
# ----------------------------------------------------------------------
def arch_19_converse_pythagoras_verify_right_angled_no(rng: random.Random) -> Dict[str, Any]:
    non_triples = [
        (4, 5, 7), (5, 6, 8), (6, 7, 10), (7, 8, 11),
        (5, 11, 13), (8, 14, 17), (6, 9, 11), (7, 10, 13)
    ]
    a, b, c = rng.choice(non_triples)
    unit = rng.choice(["cm", "mm", "m"])
    sum_legs = a * a + b * b
    c_sq = c * c

    prompt = (
        f"A triangle has side lengths of \\({a}\\text{{ {unit}}}\\), \\({b}\\text{{ {unit}}}\\), "
        f"and \\({c}\\text{{ {unit}}}\\).\n\n"
        f"Determine whether this triangle is a right-angled triangle. "
        f"Justify your conclusion using the Converse of Pythagoras."
    )
    sol = (
        f"**Converse of Pythagoras Test:**\n"
        f"Identify the longest side: \\(c = {c}\\text{{ {unit}}}\\).\n\n"
        f"1. Square of the longest side:\n"
        f"\\[ ({c})^2 = {c_sq} \\]\n\n"
        f"2. Sum of the squares of the two shorter sides:\n"
        f"\\[ ({a})^2 + ({b})^2 = {a*a} + {b*b} = {sum_legs} \\]\n\n"
        f"**Conclusion:**\n"
        f"Since \\({a}^2 + {b}^2 \\neq {c}^2\\) (\\({sum_legs} \\neq {c_sq}\\)), "
        f"the triangle **is not a right-angled triangle**."
    )
    return {
        "id": f"g9_pyth_conv_no_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "No, it is not right-angled (a² + b² ≠ c²)",
        "expected_answer": "No, it is not right-angled",
        "sample_answer": f"No; {a}² + {b}² ({sum_legs}) ≠ {c}² ({c_sq})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate square of longest side: {c}² = {c_sq}", "marks": 1},
            {"desc": f"Calculate sum of squares of other sides: {a}² + {b}² = {sum_legs}", "marks": 1},
            {"desc": f"Conclude NOT right-angled because {sum_legs} ≠ {c_sq}", "marks": 1},
        ],
        "hints": [
            f"Square the longest side: {c}² = {c_sq}.",
            f"Add the squares of the other two sides: {a}² + {b}² = {sum_legs}.",
            f"Since {sum_legs} ≠ {c_sq}, it is not right-angled.",
        ],
    }


# ----------------------------------------------------------------------
# 20. Classify Triangle: Acute (c^2 < a^2 + b^2)
# ----------------------------------------------------------------------
def arch_20_classify_triangle_acute_pythagoras_inequality(rng: random.Random) -> Dict[str, Any]:
    acute_triples = [
        (5, 6, 7),   # 49 < 25 + 36 = 61
        (6, 7, 8),   # 64 < 36 + 49 = 85
        (7, 8, 9),   # 81 < 49 + 64 = 113
        (8, 9, 10),  # 100 < 64 + 81 = 145
        (7, 9, 11),  # 121 < 49 + 81 = 130
        (9, 10, 12), # 144 < 81 + 100 = 181
    ]
    a, b, c = rng.choice(acute_triples)
    unit = "cm"
    sum_legs = a * a + b * b
    c_sq = c * c

    prompt = (
        f"A triangle has side lengths \\({a}\\text{{ {unit}}}\\), \\({b}\\text{{ {unit}}}\\), and \\({c}\\text{{ {unit}}}\\). "
        f"By comparing \\(c^2\\) (where \\(c\\) is the longest side) with \\(a^2 + b^2\\), "
        f"classify whether the triangle is **acute-angled, right-angled, or obtuse-angled**."
    )
    sol = (
        f"**Pythagorean Inequality Test:**\n"
        f"Longest side: \\(c = {c}\\).\n"
        f"\\[ c^2 = {c}^2 = {c_sq} \\]\n"
        f"\\[ a^2 + b^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {sum_legs} \\]\n\n"
        f"**Comparison:**\n"
        f"\\[ c^2 < a^2 + b^2 \\quad ({c_sq} < {sum_legs}) \\]\n\n"
        f"Therefore, the triangle is an **acute-angled triangle**."
    )
    return {
        "id": f"g9_pyth_acute_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "Acute-angled (c² < a² + b²)",
        "expected_answer": "Acute-angled",
        "sample_answer": f"Acute-angled ({c_sq} < {sum_legs})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate c² = {c_sq} and a² + b² = {sum_legs}", "marks": 1},
            {"desc": f"Compare: c² < a² + b² ({c_sq} < {sum_legs})", "marks": 1},
            {"desc": "Classify correctly as acute-angled", "marks": 1},
        ],
        "hints": [
            "If c² = a² + b², it is right-angled. If c² < a² + b², it is acute. If c² > a² + b², it is obtuse.",
            f"Compare {c_sq} with {sum_legs}.",
            f"Since {c_sq} < {sum_legs}, the triangle is acute.",
        ],
    }


# ----------------------------------------------------------------------
# 21. Classify Triangle: Obtuse (c^2 > a^2 + b^2)
# ----------------------------------------------------------------------
def arch_21_classify_triangle_obtuse_pythagoras_inequality(rng: random.Random) -> Dict[str, Any]:
    obtuse_triples = [
        (3, 4, 6),   # 36 > 9 + 16 = 25
        (4, 5, 8),   # 64 > 16 + 25 = 41
        (5, 6, 9),   # 81 > 25 + 36 = 61
        (6, 8, 12),  # 144 > 36 + 64 = 100
        (7, 9, 13),  # 169 > 49 + 81 = 130
        (5, 7, 10),  # 100 > 25 + 49 = 74
    ]
    a, b, c = rng.choice(obtuse_triples)
    unit = "cm"
    sum_legs = a * a + b * b
    c_sq = c * c

    prompt = (
        f"A triangle has side lengths \\({a}\\text{{ {unit}}}\\), \\({b}\\text{{ {unit}}}\\), and \\({c}\\text{{ {unit}}}\\). "
        f"Using Pythagorean side comparisons, classify whether the triangle is **acute-angled, right-angled, or obtuse-angled**."
    )
    sol = (
        f"**Pythagorean Inequality Test:**\n"
        f"Longest side: \\(c = {c}\\).\n"
        f"\\[ c^2 = {c}^2 = {c_sq} \\]\n"
        f"\\[ a^2 + b^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {sum_legs} \\]\n\n"
        f"**Comparison:**\n"
        f"\\[ c^2 > a^2 + b^2 \\quad ({c_sq} > {sum_legs}) \\]\n\n"
        f"Therefore, the triangle is an **obtuse-angled triangle**."
    )
    return {
        "id": f"g9_pyth_obtuse_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": "Obtuse-angled (c² > a² + b²)",
        "expected_answer": "Obtuse-angled",
        "sample_answer": f"Obtuse-angled ({c_sq} > {sum_legs})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate c² = {c_sq} and a² + b² = {sum_legs}", "marks": 1},
            {"desc": f"Compare: c² > a² + b² ({c_sq} > {sum_legs})", "marks": 1},
            {"desc": "Classify correctly as obtuse-angled", "marks": 1},
        ],
        "hints": [
            "Check the relation between the square of the longest side and the sum of the squares of the other two sides.",
            f"{c}² = {c_sq} is greater than {sum_legs}.",
            "When c² > a² + b², the triangle is obtuse-angled.",
        ],
    }


# ----------------------------------------------------------------------
# 22. Identify Which Angle is Right Angle from Converse
# ----------------------------------------------------------------------
def arch_22_identify_which_angle_is_right_angle_from_converse(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (("A", "B", "C"), "B", "AC", "AB", "BC"),
        (("P", "Q", "R"), "Q", "PR", "PQ", "QR"),
        (("D", "E", "F"), "E", "DF", "DE", "EF"),
        (("K", "L", "M"), "L", "KM", "KL", "LM"),
        (("X", "Y", "Z"), "Y", "XZ", "XY", "YZ"),
        (("M", "N", "P"), "N", "MP", "MN", "NP"),
    ]
    verts, rt_v, hyp, s1, s2 = rng.choice(configs)
    t_name = "".join(verts)

    prompt = (
        f"In \\(\\triangle {t_name}\\), it is verified that \\({s1}^2 + {s2}^2 = {hyp}^2\\). "
        f"According to the Converse of Pythagoras Theorem, which vertex of \\(\\triangle {t_name}\\) "
        f"is the \\(90^\\circ\\) right angle?"
    )
    sol = (
        f"**Converse of Pythagoras Deduction:**\n"
        f"In the equation \\({s1}^2 + {s2}^2 = {hyp}^2\\), the side \\({hyp}\\) is the hypotenuse.\n"
        f"The \\(90^\\circ\\) right angle is always the angle **opposite the hypotenuse**.\n\n"
        f"The vertex opposite side \\({hyp}\\) is vertex **\\({rt_v}\\)** (or \\(\\hat{{{rt_v}}}\\)).\n"
        f"\\[ \\therefore \\hat{{{rt_v}}} = 90^\\circ \\]"
    )
    return {
        "id": f"g9_pyth_which_angle_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Angle {rt_v} (or {rt_v}^)",
        "expected_answer": f"Angle {rt_v}",
        "sample_answer": f"Angle {rt_v} (opposite hypotenuse {hyp})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify {hyp} as the hypotenuse", "marks": 1},
            {"desc": f"State angle opposite {hyp} is angle {rt_v} = 90°", "marks": 1},
        ],
        "hints": [
            f"The single side on the right of the equality ({hyp}) is the hypotenuse.",
            f"The 90° angle is opposite the hypotenuse {hyp}.",
            f"The opposite vertex is {rt_v}.",
        ],
    }


# ----------------------------------------------------------------------
# 23. Pythagorean Triple Membership Test
# ----------------------------------------------------------------------
def arch_23_pythagorean_triple_membership_test(rng: random.Random) -> Dict[str, Any]:
    choices = [
        ((3, 4, 5), True),
        ((5, 12, 13), True),
        ((7, 24, 25), True),
        ((8, 15, 17), True),
        ((9, 40, 41), True),
        ((6, 8, 10), True),
        ((4, 7, 8), False),
        ((5, 10, 12), False),
        ((7, 12, 15), False),
        ((8, 13, 16), False),
        ((6, 10, 13), False),
    ]
    (a, b, c), is_triple = rng.choice(choices)
    sum_legs = a * a + b * b
    c_sq = c * c

    prompt = (
        f"A set of three positive integers \\((a, b, c)\\) is called a **Pythagorean triple** if \\(a^2 + b^2 = c^2\\).\n\n"
        f"Determine whether \\(({a}, {b}, {c})\\) forms a Pythagorean triple. Show your mathematical proof."
    )
    if is_triple:
        sol = (
            f"**Proof:**\n"
            f"\\[ a^2 + b^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {sum_legs} \\]\n"
            f"\\[ c^2 = {c}^2 = {c_sq} \\]\n\n"
            f"Since \\({a}^2 + {b}^2 = c^2\\) (\\({sum_legs} = {c_sq}\\)), "
            f"the set **\\(({a}, {b}, {c})\\) is a Pythagorean triple**."
        )
        ans = "Yes, it is a Pythagorean triple"
    else:
        sol = (
            f"**Proof:**\n"
            f"\\[ a^2 + b^2 = {a}^2 + {b}^2 = {a*a} + {b*b} = {sum_legs} \\]\n"
            f"\\[ c^2 = {c}^2 = {c_sq} \\]\n\n"
            f"Since \\({a}^2 + {b}^2 \\neq c^2\\) (\\({sum_legs} \\neq {c_sq}\\)), "
            f"the set **\\(({a}, {b}, {c})\\) is NOT a Pythagorean triple**."
        )
        ans = "No, it is not a Pythagorean triple"

    return {
        "id": f"g9_pyth_triple_test_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": sol,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate a² + b² = {sum_legs} and c² = {c_sq}", "marks": 1},
            {"desc": f"State conclusion ({ans})", "marks": 1},
        ],
        "hints": [
            f"Calculate {a}² + {b}².",
            f"Calculate {c}².",
            "Compare the two values to see if they are equal.",
        ],
    }


# ----------------------------------------------------------------------
# 24. Generate Pythagorean Triple from Formula (Euclid's Formula)
# ----------------------------------------------------------------------
def arch_24_generate_pythagorean_triple_from_formula(rng: random.Random) -> Dict[str, Any]:
    configs = [
        (2, 1),  # a = 3, b = 4, c = 5
        (3, 2),  # a = 5, b = 12, c = 13
        (4, 1),  # a = 15, b = 8, c = 17
        (3, 1),  # a = 8, b = 6, c = 10
        (4, 3),  # a = 7, b = 24, c = 25
        (5, 2),  # a = 21, b = 20, c = 29
    ]
    m, n = rng.choice(configs)
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n * n
    # Standardize a < b
    if a > b:
        a, b = b, a

    prompt = (
        f"Euclid's formula generates a Pythagorean triple \\((a, b, c)\\) from two integers \\(m\\) and \\(n\\) (where \\(m > n\\)) using:\n"
        f"\\[ a = m^2 - n^2, \\quad b = 2mn, \\quad c = m^2 + n^2 \\]\n\n"
        f"Given \\(m = {m}\\) and \\(n = {n}\\), calculate the generated Pythagorean triple \\((a, b, c)\\)."
    )
    sol = (
        f"**Step 1: Calculate each side.**\n"
        f"\\[ m^2 - n^2 = {m}^2 - {n}^2 = {m*m} - {n*n} = {m*m - n*n} \\]\n"
        f"\\[ 2mn = 2({m})({n}) = {2 * m * n} \\]\n"
        f"\\[ m^2 + n^2 = {m}^2 + {n}^2 = {m*m} + {n*n} = {m*m + n*n} \\]\n\n"
        f"**Step 2: State the triple.**\n"
        f"The generated Pythagorean triple is **({a}, {b}, {c})**.\n"
        f"Check: \\({a}^2 + {b}^2 = {a*a} + {b*b} = {c*c} = {c}^2\\)."
    )
    return {
        "id": f"g9_pyth_euclid_{rng.randint(100000, 999999)}",
        "question_type": "text",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"({a}, {b}, {c})",
        "expected_answer": f"({a}, {b}, {c})",
        "sample_answer": f"({a}, {b}, {c})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Calculate m² - n² = {m*m - n*n}", "marks": 1},
            {"desc": f"Calculate 2mn = {2*m*n}", "marks": 1},
            {"desc": f"Calculate m² + n² = {m*m + n*n} and state triple", "marks": 1},
        ],
        "hints": [
            f"Substitute m = {m} and n = {n} into each formula.",
            f"Calculate {m}² - {n}², 2({m})({n}), and {m}² + {n}².",
            f"The triple is ({a}, {b}, {c}).",
        ],
    }


# ----------------------------------------------------------------------
# 25. Algebraic Pythagoras: Linear Unknown Side
# ----------------------------------------------------------------------
def arch_25_algebraic_pythagoras_linear_unknown_side(rng: random.Random) -> Dict[str, Any]:
    # Canonical 3x, 4x, 5x or x, x+1, hypotenuse given
    configs = [
        (3, 4, 5, 2, 6, 8, 10),
        (3, 4, 5, 3, 9, 12, 15),
        (3, 4, 5, 4, 12, 16, 20),
        (5, 12, 13, 2, 10, 24, 26),
        (3, 4, 5, 5, 15, 20, 25),
    ]
    c1, c2, c3, k, s1, s2, hyp = rng.choice(configs)
    unit = "cm"

    prompt = (
        f"In right-angled \\(\\triangle ABC\\) with \\(\\hat{{B}} = 90^\\circ\\), "
        f"the sides are given in terms of \\(x\\) as \\(AB = {c2}x\\text{{ {unit}}}\\) "
        f"and \\(BC = {c1}x\\text{{ {unit}}}\\). "
        f"If the hypotenuse \\(AC = {hyp}\\text{{ {unit}}}\\), solve for \\(x\\) and calculate the length of side \\(AB\\)."
    )
    sol = (
        f"**Step 1: Set up the Pythagoras equation.**\n"
        f"\\[ AB^2 + BC^2 = AC^2 \\quad [\\text{{Pythagoras, }}\\hat{{B}} = 90^\\circ] \\]\n"
        f"\\[ ({c2}x)^2 + ({c1}x)^2 = {hyp}^2 \\]\n"
        f"\\[ {c2*c2}x^2 + {c1*c1}x^2 = {hyp*hyp} \\]\n"
        f"\\[ {c2*c2 + c1*c1}x^2 = {hyp*hyp} \\]\n\n"
        f"**Step 2: Solve for x.**\n"
        f"\\[ x^2 = \\frac{{{hyp*hyp}}}{{{c2*c2 + c1*c1}}} = {k*k} \\]\n"
        f"\\[ x = \\sqrt{{{k*k}}} = {k} \\]\n\n"
        f"**Step 3: Calculate AB.**\n"
        f"\\[ AB = {c2}({k}) = {s2}\\text{{ {unit}}} \\]"
    )
    return {
        "id": f"g9_pyth_alg_x_{rng.randint(100000, 999999)}",
        "question_type": "measurement",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"x = {k}, AB = {s2} {unit}",
        "expected_answer": f"{s2} {unit}",
        "sample_answer": f"x = {k}, AB = {s2} {unit}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": [
            {"desc": f"Set up ({c2}x)² + ({c1}x)² = {hyp}²", "marks": 1},
            {"desc": f"Simplify to {c2*c2+c1*c1}x² = {hyp*hyp}", "marks": 1},
            {"desc": f"Solve for x = {k}", "marks": 1},
            {"desc": f"Calculate AB = {s2} {unit}", "marks": 1},
        ],
        "hints": [
            f"Square both expressions: ({c2}x)² = {c2*c2}x² and ({c1}x)² = {c1*c1}x².",
            f"Add like terms: {c2*c2 + c1*c1}x² = {hyp*hyp}.",
            f"Divide to find x² = {k*k}, so x = {k}. Then AB = {s2} {unit}.",
        ],
    }
