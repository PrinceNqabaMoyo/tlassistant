"""Grade 10 Mathematics — Term 1 — Trigonometry: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr10/Term 1/05. Trigonometry 1.md
Focus: Trigonometric ratios in right triangles (sin, cos, tan), reciprocal ratios (cosec, sec, cot),
Pythagoras with trig ratios, special angles (30, 45, 60, 0, 90), calculator evaluations, and right-triangle solving.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple


# Pythagorean triples (opp, adj, hyp)
TRIPLES: List[Tuple[int, int, int]] = [
    (3, 4, 5), (4, 3, 5),
    (5, 12, 13), (12, 5, 13),
    (8, 15, 17), (15, 8, 17),
    (7, 24, 25), (24, 7, 25),
    (6, 8, 10), (8, 6, 10),
]


def _build_right_triangle_svg(
    adj_len: float,
    opp_len: float,
    hyp_len: float,
    adj_label: str = "",
    opp_label: str = "",
    hyp_label: str = "",
    theta_label: str = "θ",
    vertex_A: str = "A",
    vertex_B: str = "B",
    vertex_C: str = "C",
) -> str:
    """Build a dynamic SVG of a right-angled triangle ABC with right angle at B, angle theta at A."""
    # Scale to fit in 440 x 260 box: A at (60, 220), B at (60 + w, 220), C at (60 + w, 220 - h)
    max_w, max_h = 280, 160
    scale = min(max_w / max(1, adj_len), max_h / max(1, opp_len))
    w = max(80, min(max_w, adj_len * scale))
    h = max(60, min(max_h, opp_len * scale))

    ax, ay = 60, 220
    bx, by = ax + w, ay
    cx, cy = bx, ay - h

    # Right angle square at B (bx, by)
    sq_sz = 16
    ra_path = f"M {bx - sq_sz} {by} L {bx - sq_sz} {by - sq_sz} L {bx} {by - sq_sz}"

    # Angle arc at A (ax, ay)
    arc_r = 30
    arc_path = f"M {ax + arc_r} {ay} A {arc_r} {arc_r} 0 0 0 {ax + arc_r * math.cos(math.atan2(h, w))} {ay - arc_r * math.sin(math.atan2(h, w))}"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 260" width="100%" height="240">
  <polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#F8FAFC" stroke="#1E293B" stroke-width="2.5"/>
  <path d="{ra_path}" fill="none" stroke="#1E293B" stroke-width="1.8"/>
  <path d="{arc_path}" fill="none" stroke="#2563EB" stroke-width="2"/>
  <text x="{ax + 36}" y="{ay - 8}" font-size="14" font-weight="bold" fill="#2563EB">{theta_label}</text>
  <!-- Vertices -->
  <text x="{ax - 18}" y="{ay + 6}" font-size="15" font-weight="bold" fill="#0F172A">{vertex_A}</text>
  <text x="{bx + 8}" y="{by + 6}" font-size="15" font-weight="bold" fill="#0F172A">{vertex_B}</text>
  <text x="{cx + 8}" y="{cy - 4}" font-size="15" font-weight="bold" fill="#0F172A">{vertex_C}</text>
  <!-- Side Labels -->
  <text x="{(ax + bx) / 2}" y="{ay + 24}" font-size="14" text-anchor="middle" font-weight="bold" fill="#0F172A">{adj_label}</text>
  <text x="{bx + 26}" y="{(by + cy) / 2 + 5}" font-size="14" text-anchor="middle" font-weight="bold" fill="#0F172A">{opp_label}</text>
  <text x="{(ax + cx) / 2 - 20}" y="{(ay + cy) / 2 - 10}" font-size="14" text-anchor="middle" font-weight="bold" fill="#0F172A">{hyp_label}</text>
</svg>'''


# 01. Identify hypotenuse opposite adjacent
def arch_01_identify_hypotenuse_opposite_adjacent_svg(rng: random.Random) -> Dict[str, Any]:
    target_role = rng.choice(["hypotenuse", "opposite", "adjacent"])
    vA, vB, vC = rng.choice([("A", "B", "C"), ("P", "Q", "R"), ("X", "Y", "Z"), ("K", "L", "M"), ("D", "E", "F")])
    opp, adj, hyp = rng.choice(TRIPLES)
    adj_side = f"{vA}{vB}"
    opp_side = f"{vB}{vC}"
    hyp_side = f"{vA}{vC}"
    # Angle at vA is theta: opposite is vB vC, adjacent is vA vB, hypotenuse is vA vC
    role_to_side = {"opposite": opp_side, "adjacent": adj_side, "hypotenuse": hyp_side}
    correct_side = role_to_side[target_role]

    svg_str = _build_right_triangle_svg(
        adj, opp, hyp,
        adj_label=f"{adj_side} ({adj})", opp_label=f"{opp_side} ({opp})", hyp_label=f"{hyp_side} ({hyp})",
        theta_label="θ", vertex_A=vA, vertex_B=vB, vertex_C=vC
    )
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Right-angled triangle {vA}{vB}{vC} with right angle at {vB} and angle θ at vertex {vA}",
    }

    prompt = (
        f"In the right-angled triangle \\({vA}{vB}{vC}\\) shown, angle \\(\\angle {vB} = 90^\\circ\\) and angle \\(\\angle {vA} = \\theta\\).\n\n"
        f"Identify which side is the **{target_role}** side relative to angle \\(\\theta\\)."
    )
    ans = f"Side {correct_side}"
    sol = (
        f"**Step 1:** Define the roles of sides relative to angle \\(\\theta\\) at vertex \\({vA}\\):\n"
        f"- The **hypotenuse** is always opposite the 90° right angle: side \\({hyp_side}\\).\n"
        f"- The **opposite** side faces directly across from angle \\(\\theta\\): side \\({opp_side}\\).\n"
        f"- The **adjacent** side lies between angle \\(\\theta\\) and the right angle: side \\({adj_side}\\).\n\n"
        f"**Conclusion:** The {target_role} side is **Side {correct_side}**."
    )
    return {
        "id": f"g10_trig_01_{rng.randint(100000, 999999)}",
        "subskill": "01_identify_hypotenuse_opposite_adjacent_svg",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": [f"Side {adj_side}", f"Side {opp_side}", f"Side {hyp_side}"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_01",
        "misconception_tags": ["confusing_opposite_and_adjacent", "confusing_hypotenuse_with_adjacent"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": f"Correctly identify {target_role} side relative to angle theta", "marks": 2},
        ],
        "hints": {
            "tier_1": "The hypotenuse is opposite the 90° angle. The opposite side faces angle θ.",
            "tier_2": f"Here angle θ is at {vA}, so the side facing it is {opp_side}.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_01_identify_hypotenuse_opposite_adjacent_svg",
    }


# 02. Sin ratio definition from triangle
def arch_02_sin_ratio_definition_from_triangle_svg(rng: random.Random) -> Dict[str, Any]:
    opp, adj, hyp = rng.choice(TRIPLES)
    svg_str = _build_right_triangle_svg(
        adj, opp, hyp,
        adj_label=str(adj), opp_label=str(opp), hyp_label=str(hyp),
        theta_label="θ", vertex_A="A", vertex_B="B", vertex_C="C"
    )
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Right triangle ABC with sides {opp}, {adj}, {hyp}",
    }

    prompt = (
        f"In the right-angled triangle \\(ABC\\), the side lengths are \\(AB = {adj}\\), "
        f"\\(BC = {opp}\\), and \\(AC = {hyp}\\).\n\n"
        f"Write down the exact value of \\(\\sin \\theta\\) as a simplified fraction."
    )
    ans = f"{opp}/{hyp}"
    sol = (
        f"**Step 1:** Recall the definition of the sine ratio:\n"
        f"\\[ \\sin \\theta = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}} \\]\n\n"
        f"**Step 2:** Identify the relevant side lengths relative to \\(\\theta\\):\n"
        f"- Opposite side = \\(BC = {opp}\\)\n"
        f"- Hypotenuse = \\(AC = {hyp}\\)\n\n"
        f"**Step 3:** Calculate \\(\\sin \\theta\\):\n"
        f"\\[ \\sin \\theta = \\frac{{{opp}}}{{{hyp}}} \\]"
    )
    return {
        "id": f"g10_trig_02_{rng.randint(100000, 999999)}",
        "subskill": "02_sin_ratio_definition_from_triangle_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"sin θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_02",
        "misconception_tags": ["ratio_definition_inversion", "adjacent_substituted_for_opposite"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "State ratio formula opposite/hypotenuse", "marks": 1},
            {"step": 2, "criterion": "Correct fraction value", "marks": 1},
        ],
        "hints": {
            "tier_1": "sin θ = opposite / hypotenuse.",
            "tier_2": f"Opposite = {opp}, Hypotenuse = {hyp}.",
            "tier_3": f"sin θ = {ans}",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_02_sin_ratio_definition_from_triangle_svg",
    }


# 03. Cos ratio definition from triangle
def arch_03_cos_ratio_definition_from_triangle_svg(rng: random.Random) -> Dict[str, Any]:
    opp, adj, hyp = rng.choice(TRIPLES)
    svg_str = _build_right_triangle_svg(
        adj, opp, hyp,
        adj_label=str(adj), opp_label=str(opp), hyp_label=str(hyp),
        theta_label="θ", vertex_A="A", vertex_B="B", vertex_C="C"
    )
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Right triangle ABC with sides {opp}, {adj}, {hyp}",
    }

    prompt = (
        f"In the right-angled triangle \\(ABC\\), the side lengths are \\(AB = {adj}\\), "
        f"\\(BC = {opp}\\), and \\(AC = {hyp}\\).\n\n"
        f"Write down the exact value of \\(\\cos \\theta\\) as a simplified fraction."
    )
    ans = f"{adj}/{hyp}"
    sol = (
        f"**Step 1:** Recall the definition of the cosine ratio:\n"
        f"\\[ \\cos \\theta = \\frac{{\\text{{adjacent}}}}{{\\text{{hypotenuse}}}} \\]\n\n"
        f"**Step 2:** Identify the relevant side lengths:\n"
        f"- Adjacent side = \\(AB = {adj}\\)\n"
        f"- Hypotenuse = \\(AC = {hyp}\\)\n\n"
        f"**Step 3:** Calculate \\(\\cos \\theta\\):\n"
        f"\\[ \\cos \\theta = \\frac{{{adj}}}{{{hyp}}} \\]"
    )
    return {
        "id": f"g10_trig_03_{rng.randint(100000, 999999)}",
        "subskill": "03_cos_ratio_definition_from_triangle_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"cos θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_03",
        "misconception_tags": ["confusing_sin_and_cos", "ratio_definition_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Formula adjacent/hypotenuse", "marks": 1},
            {"step": 2, "criterion": "Correct numerical ratio", "marks": 1},
        ],
        "hints": {
            "tier_1": "cos θ = adjacent / hypotenuse.",
            "tier_2": f"Adjacent = {adj}, Hypotenuse = {hyp}.",
            "tier_3": f"cos θ = {ans}",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_03_cos_ratio_definition_from_triangle_svg",
    }


# 04. Tan ratio definition from triangle
def arch_04_tan_ratio_definition_from_triangle_svg(rng: random.Random) -> Dict[str, Any]:
    opp, adj, hyp = rng.choice(TRIPLES)
    svg_str = _build_right_triangle_svg(
        adj, opp, hyp,
        adj_label=str(adj), opp_label=str(opp), hyp_label=str(hyp),
        theta_label="θ", vertex_A="A", vertex_B="B", vertex_C="C"
    )
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Right triangle ABC with sides {opp}, {adj}, {hyp}",
    }

    prompt = (
        f"In the right-angled triangle \\(ABC\\), the side lengths are \\(AB = {adj}\\), "
        f"\\(BC = {opp}\\), and \\(AC = {hyp}\\).\n\n"
        f"Write down the exact value of \\(\\tan \\theta\\) as a simplified fraction."
    )
    ans = f"{opp}/{adj}"
    sol = (
        f"**Step 1:** Recall the definition of the tangent ratio:\n"
        f"\\[ \\tan \\theta = \\frac{{\\text{{opposite}}}}{{\\text{{adjacent}}}} \\]\n\n"
        f"**Step 2:** Identify the sides:\n"
        f"- Opposite side = \\(BC = {opp}\\)\n"
        f"- Adjacent side = \\(AB = {adj}\\)\n\n"
        f"**Step 3:** Calculate \\(\\tan \\theta\\):\n"
        f"\\[ \\tan \\theta = \\frac{{{opp}}}{{{adj}}} \\]"
    )
    return {
        "id": f"g10_trig_04_{rng.randint(100000, 999999)}",
        "subskill": "04_tan_ratio_definition_from_triangle_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"tan θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_04",
        "misconception_tags": ["tan_ratio_inversion", "using_hypotenuse_in_tan"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Formula opposite/adjacent", "marks": 1},
            {"step": 2, "criterion": "Correct ratio value", "marks": 1},
        ],
        "hints": {
            "tier_1": "tan θ = opposite / adjacent.",
            "tier_2": f"Opposite = {opp}, Adjacent = {adj}.",
            "tier_3": f"tan θ = {ans}",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_04_tan_ratio_definition_from_triangle_svg",
    }


# 05. Reciprocal cosec ratio definition: cosec θ = 1 / sin θ = hyp / opp
def arch_05_reciprocal_cosec_ratio_definition(rng: random.Random) -> Dict[str, Any]:
    opp, adj, hyp = rng.choice(TRIPLES)
    prompt = (
        f"Given a right-angled triangle where \\(\\sin \\theta = \\frac{{{opp}}}{{{hyp}}}\\), "
        f"determine the value of \\(\\csc \\theta\\) (cosec \\(\\theta\\))."
    )
    ans = f"{hyp}/{opp}"
    sol = (
        f"**Step 1:** Recall the definition of the cosecant ratio as the reciprocal of sine:\n"
        f"\\[ \\csc \\theta = \\frac{{1}}{{\\sin \\theta}} = \\frac{{\\text{{hypotenuse}}}}{{\\text{{opposite}}}} \\]\n\n"
        f"**Step 2:** Invert the sine ratio:\n"
        f"\\[ \\csc \\theta = \\frac{{{hyp}}}{{{opp}}} \\]"
    )
    return {
        "id": f"g10_trig_05_{rng.randint(100000, 999999)}",
        "subskill": "05_reciprocal_cosec_ratio_definition",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"cosec θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_05",
        "misconception_tags": ["confusing_cosec_with_cos", "reciprocal_definition_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Identify cosec as reciprocal of sine", "marks": 1},
            {"step": 2, "criterion": "Correct inverted fraction", "marks": 1},
        ],
        "hints": {
            "tier_1": "cosec θ = 1 / sin θ.",
            "tier_2": f"If sin θ = {opp}/{hyp}, then cosec θ = {hyp}/{opp}.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_05_reciprocal_cosec_ratio_definition",
    }


# 06. Reciprocal sec ratio definition: sec θ = 1 / cos θ = hyp / adj
def arch_06_reciprocal_sec_ratio_definition(rng: random.Random) -> Dict[str, Any]:
    opp, adj, hyp = rng.choice(TRIPLES)
    prompt = (
        f"Given that \\(\\cos \\theta = \\frac{{{adj}}}{{{hyp}}}\\), "
        f"determine the value of \\(\\sec \\theta\\)."
    )
    ans = f"{hyp}/{adj}"
    sol = (
        f"**Step 1:** Recall the definition of the secant ratio as the reciprocal of cosine:\n"
        f"\\[ \\sec \\theta = \\frac{{1}}{{\\cos \\theta}} = \\frac{{\\text{{hypotenuse}}}}{{\\text{{adjacent}}}} \\]\n\n"
        f"**Step 2:** Invert the cosine ratio:\n"
        f"\\[ \\sec \\theta = \\frac{{{hyp}}}{{{adj}}} \\]"
    )
    return {
        "id": f"g10_trig_06_{rng.randint(100000, 999999)}",
        "subskill": "06_reciprocal_sec_ratio_definition",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"sec θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_06",
        "misconception_tags": ["confusing_sec_with_sin", "reciprocal_definition_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Identify sec as reciprocal of cosine", "marks": 1},
            {"step": 2, "criterion": "Correct fraction value", "marks": 1},
        ],
        "hints": {
            "tier_1": "sec θ = 1 / cos θ.",
            "tier_2": f"If cos θ = {adj}/{hyp}, then sec θ = {hyp}/{adj}.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_06_reciprocal_sec_ratio_definition",
    }


# 07. Reciprocal cot ratio definition: cot θ = 1 / tan θ = adj / opp
def arch_07_reciprocal_cot_ratio_definition(rng: random.Random) -> Dict[str, Any]:
    opp, adj, hyp = rng.choice(TRIPLES)
    prompt = (
        f"Given that \\(\\tan \\theta = \\frac{{{opp}}}{{{adj}}}\\), "
        f"determine the exact value of \\(\\cot \\theta\\)."
    )
    ans = f"{adj}/{opp}"
    sol = (
        f"**Step 1:** Recall the definition of cotangent as the reciprocal of tangent:\n"
        f"\\[ \\cot \\theta = \\frac{{1}}{{\\tan \\theta}} = \\frac{{\\text{{adjacent}}}}{{\\text{{opposite}}}} \\]\n\n"
        f"**Step 2:** Invert the tangent ratio:\n"
        f"\\[ \\cot \\theta = \\frac{{{adj}}}{{{opp}}} \\]"
    )
    return {
        "id": f"g10_trig_07_{rng.randint(100000, 999999)}",
        "subskill": "07_reciprocal_cot_ratio_definition",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"cot θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_07",
        "misconception_tags": ["cot_definition_inversion", "reciprocal_confusion"],
        "marking_schema": [
            {"step": 1, "criterion": "Formula cot = 1 / tan", "marks": 1},
            {"step": 2, "criterion": "Inverted fraction answer", "marks": 1},
        ],
        "hints": {
            "tier_1": "cot θ = 1 / tan θ.",
            "tier_2": f"If tan θ = {opp}/{adj}, then cot θ = {adj}/{opp}.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_07_reciprocal_cot_ratio_definition",
    }


# 08. Pythagoras find missing side then sin cos
def arch_08_pythagoras_find_missing_side_then_sin_cos(rng: random.Random) -> Dict[str, Any]:
    opp, adj, hyp = rng.choice(TRIPLES)
    # Give adj and opp, ask for hyp and sin theta
    svg_str = _build_right_triangle_svg(
        adj, opp, hyp,
        adj_label=str(adj), opp_label=str(opp), hyp_label="x",
        theta_label="θ", vertex_A="A", vertex_B="B", vertex_C="C"
    )
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Right triangle ABC with adjacent side {adj} and opposite side {opp}",
    }

    prompt = (
        f"In right-angled triangle \\(ABC\\) shown, \\(AB = {adj}\\) and \\(BC = {opp}\\).\n\n"
        f"1. Use the Theorem of Pythagoras to calculate the length of hypotenuse \\(AC\\).\n"
        f"2. Write down the exact value of \\(\\sin \\theta\\)."
    )
    ans = f"AC = {hyp}, sin θ = {opp}/{hyp}"
    sol = (
        f"**Step 1:** Calculate hypotenuse \\(AC\\) using Pythagoras:\n"
        f"\\[ AC^2 = AB^2 + BC^2 = {adj}^2 + {opp}^2 = {adj**2} + {opp**2} = {hyp**2} \\]\n"
        f"\\[ AC = \\sqrt{{{hyp**2}}} = {hyp} \\]\n\n"
        f"**Step 2:** State the sine ratio:\n"
        f"\\[ \\sin \\theta = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}} = \\frac{{{opp}}}{{{hyp}}} \\]"
    )
    return {
        "id": f"g10_trig_08_{rng.randint(100000, 999999)}",
        "subskill": "08_pythagoras_find_missing_side_then_sin_cos",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{hyp} and {opp}/{hyp}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_08",
        "misconception_tags": ["pythagoras_addition_vs_subtraction_error", "sin_ratio_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Apply Pythagoras to find AC = hyp", "marks": 2},
            {"step": 2, "criterion": "Determine sin theta = opp / hyp", "marks": 1},
        ],
        "hints": {
            "tier_1": f"AC^2 = {adj}^2 + {opp}^2.",
            "tier_2": f"AC = {hyp}. Then sin θ = {opp}/{hyp}.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_08_pythagoras_find_missing_side_then_sin_cos",
    }


# 09. Special angle 30 exact values
def arch_09_special_angle_30_exact_values(rng: random.Random) -> Dict[str, Any]:
    fn = rng.choice(["sin", "cos", "tan"])
    values = {
        "sin": ("1/2", "\\frac{1}{2}"),
        "cos": ("sqrt(3)/2", "\\frac{\\sqrt{3}}{2}"),
        "tan": ("1/sqrt(3)", "\\frac{1}{\\sqrt{3}} = \\frac{\\sqrt{3}}{3}"),
    }
    ans, ans_latex = values[fn]

    prompt = (
        f"Without using a calculator, write down the exact surd value of \\(\\{fn} 30^\\circ\\)."
    )
    sol = (
        f"**Special Angle 30°:**\n"
        f"Derived from an equilateral triangle of side length 2 cut in half:\n"
        f"- Opposite = 1\n"
        f"- Adjacent = \\(\\sqrt{{3}}\\)\n"
        f"- Hypotenuse = 2\n\n"
        f"Therefore, \\(\\{fn} 30^\\circ = {ans_latex}\\)."
    )
    return {
        "id": f"g10_trig_09_{rng.randint(100000, 999999)}",
        "subskill": "09_special_angle_30_exact_values",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"{fn}(30°) = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_09",
        "misconception_tags": ["special_angle_confusing_30_and_60", "decimal_instead_of_surd"],
        "marking_schema": [
            {"step": 1, "criterion": f"State exact surd value for {fn}(30°)", "marks": 2},
        ],
        "hints": {
            "tier_1": "Recall the 30°-60°-90° special triangle with sides 1, sqrt(3), 2.",
            "tier_2": f"Opposite 30° is 1, adjacent is sqrt(3), hypotenuse is 2.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_09_special_angle_30_exact_values",
    }


# 10. Special angle 45 exact values
def arch_10_special_angle_45_exact_values(rng: random.Random) -> Dict[str, Any]:
    fn = rng.choice(["sin", "cos", "tan"])
    values = {
        "sin": ("1/sqrt(2)", "\\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}"),
        "cos": ("1/sqrt(2)", "\\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}"),
        "tan": ("1", "1"),
    }
    ans, ans_latex = values[fn]

    prompt = (
        f"Without using a calculator, write down the exact value of \\(\\{fn} 45^\\circ\\)."
    )
    sol = (
        f"**Special Angle 45°:**\n"
        f"Derived from an isosceles right-angled triangle with legs of length 1:\n"
        f"- Opposite = 1\n"
        f"- Adjacent = 1\n"
        f"- Hypotenuse = \\(\\sqrt{{1^2 + 1^2}} = \\sqrt{{2}}\\)\n\n"
        f"Therefore, \\(\\{fn} 45^\\circ = {ans_latex}\\)."
    )
    return {
        "id": f"g10_trig_10_{rng.randint(100000, 999999)}",
        "subskill": "10_special_angle_45_exact_values",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"{fn}(45°) = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_10",
        "misconception_tags": ["special_angle_45_surd_error", "rationalisation_confusion"],
        "marking_schema": [
            {"step": 1, "criterion": f"State exact value for {fn}(45°)", "marks": 2},
        ],
        "hints": {
            "tier_1": "In a 45°-45°-90° triangle, opposite = 1, adjacent = 1, hypotenuse = sqrt(2).",
            "tier_2": f"{fn}(45°) = {ans_latex}.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_10_special_angle_45_exact_values",
    }


# 11. Special angle 60 exact values
def arch_11_special_angle_60_exact_values(rng: random.Random) -> Dict[str, Any]:
    fn = rng.choice(["sin", "cos", "tan"])
    values = {
        "sin": ("sqrt(3)/2", "\\frac{\\sqrt{3}}{2}"),
        "cos": ("1/2", "\\frac{1}{2}"),
        "tan": ("sqrt(3)", "\\sqrt{3}"),
    }
    ans, ans_latex = values[fn]

    prompt = (
        f"Without using a calculator, write down the exact surd value of \\(\\{fn} 60^\\circ\\)."
    )
    sol = (
        f"**Special Angle 60°:**\n"
        f"In a 30°-60°-90° right triangle:\n"
        f"- Opposite 60° = \\(\\sqrt{{3}}\\)\n"
        f"- Adjacent to 60° = 1\n"
        f"- Hypotenuse = 2\n\n"
        f"Therefore, \\(\\{fn} 60^\\circ = {ans_latex}\\)."
    )
    return {
        "id": f"g10_trig_11_{rng.randint(100000, 999999)}",
        "subskill": "11_special_angle_60_exact_values",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"{fn}(60°) = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_11",
        "misconception_tags": ["special_angle_60_inversion", "sin_cos_60_confusion"],
        "marking_schema": [
            {"step": 1, "criterion": f"State exact value of {fn}(60°)", "marks": 2},
        ],
        "hints": {
            "tier_1": "For 60°, the opposite side is sqrt(3), adjacent is 1, and hypotenuse is 2.",
            "tier_2": f"{fn}(60°) = {ans_latex}.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_11_special_angle_60_exact_values",
    }


# 12. Special angles 0 and 90 boundary values
def arch_12_special_angles_0_and_90_boundary_values(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([0, 90])
    fn = rng.choice(["sin", "cos", "tan"])
    if angle == 0:
        vals = {"sin": ("0", "0"), "cos": ("1", "1"), "tan": ("0", "0")}
    else:
        vals = {"sin": ("1", "1"), "cos": ("0", "0"), "tan": ("undefined", "\\text{undefined}")}

    ans, ans_latex = vals[fn]

    prompt = (
        f"Determine the value of \\(\\{fn} {angle}^\\circ\\) without using a calculator."
    )
    sol = (
        f"**Boundary Angle {angle}° on the Unit Circle:**\n"
        f"- At {angle}°, the coordinates \\((x; y)\\) are {('(1; 0)' if angle == 0 else '(0; 1)')}.\n"
        f"- Since \\(\\sin = y/r\\), \\(\\cos = x/r\\), and \\(\\tan = y/x\\):\n"
        f"\\[ \\{fn} {angle}^\\circ = {ans_latex} \\]"
    )
    return {
        "id": f"g10_trig_12_{rng.randint(100000, 999999)}",
        "subskill": "12_special_angles_0_and_90_boundary_values",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"{fn}({angle}°) = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_12",
        "misconception_tags": ["tan_90_undefined_misconception", "sin_0_cos_0_confusion"],
        "marking_schema": [
            {"step": 1, "criterion": f"State correct boundary value for {fn}({angle}°)", "marks": 2},
        ],
        "hints": {
            "tier_1": f"Think of the Cartesian coordinates at {angle}° on the unit circle.",
            "tier_2": f"{fn}({angle}°) = {ans}.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_12_special_angles_0_and_90_boundary_values",
    }


# 13. Special angles simplify sum and difference: sin 30 + cos 60 = 1/2 + 1/2 = 1
def arch_13_special_angles_simplify_sum_and_difference(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice(["sin30_cos60", "tan45_sin30", "cos60_tan45"])
    if case == "sin30_cos60":
        prompt = "Without a calculator, evaluate:\n\\[ \\sin 30^\\circ + \\cos 60^\\circ \\]"
        ans = "1"
        sol = (
            f"**Step 1:** Substitute special angle values:\n"
            f"- \\(\\sin 30^\\circ = \\frac{{1}}{{2}}\\)\n"
            f"- \\(\\cos 60^\\circ = \\frac{{1}}{{2}}\\)\n\n"
            f"**Step 2:** Add:\n"
            f"\\[ \\frac{{1}}{{2}} + \\frac{{1}}{{2}} = 1 \\]"
        )
    elif case == "tan45_sin30":
        prompt = "Without a calculator, evaluate:\n\\[ \\tan 45^\\circ + \\sin 30^\\circ \\]"
        ans = "3/2"
        sol = (
            f"**Step 1:** Substitute special angle values:\n"
            f"- \\(\\tan 45^\\circ = 1\\)\n"
            f"- \\(\\sin 30^\\circ = \\frac{{1}}{{2}}\\)\n\n"
            f"**Step 2:** Add:\n"
            f"\\[ 1 + \\frac{{1}}{{2}} = \\frac{{3}}{{2}} \\]"
        )
    else:
        prompt = "Without a calculator, evaluate:\n\\[ \\tan 45^\\circ - \\cos 60^\\circ \\]"
        ans = "1/2"
        sol = (
            f"**Step 1:** Substitute special angle values:\n"
            f"- \\(\\tan 45^\\circ = 1\\)\n"
            f"- \\(\\cos 60^\\circ = \\frac{{1}}{{2}}\\)\n\n"
            f"**Step 2:** Subtract:\n"
            f"\\[ 1 - \\frac{{1}}{{2}} = \\frac{{1}}{{2}} \\]"
        )

    return {
        "id": f"g10_trig_13_{rng.randint(100000, 999999)}",
        "subskill": "13_special_angles_simplify_sum_and_difference",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_13",
        "misconception_tags": ["special_angle_substitution_error", "fraction_addition_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Substitute exact values for both ratios", "marks": 1},
            {"step": 2, "criterion": "Simplify to single number/fraction", "marks": 1},
        ],
        "hints": {
            "tier_1": "Replace each trig ratio with its exact special angle value.",
            "tier_2": "Perform the fraction arithmetic.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_13_special_angles_simplify_sum_and_difference",
    }


# 14. Special angles simplify product and quotient: tan 60 * cos 30
def arch_14_special_angles_simplify_product_and_quotient(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice(["tan60_cos30", "tan60_tan30", "sin60_cos30"])
    if case == "tan60_cos30":
        prompt = "Without using a calculator, simplify:\n\\[ \\tan 60^\\circ \\times \\cos 30^\\circ \\]"
        ans = "3/2"
        sol = (
            f"**Step 1:** Substitute exact surd values:\n"
            f"- \\(\\tan 60^\\circ = \\sqrt{{3}}\\)\n"
            f"- \\(\\cos 30^\\circ = \\frac{{\\sqrt{{3}}}}{{2}}\\)\n\n"
            f"**Step 2:** Multiply:\n"
            f"\\[ \\sqrt{{3}} \\times \\frac{{\\sqrt{{3}}}}{{2}} = \\frac{{(\\sqrt{{3}})^2}}{{2}} = \\frac{{3}}{{2}} \\]"
        )
    elif case == "tan60_tan30":
        prompt = "Without using a calculator, simplify:\n\\[ \\tan 60^\\circ \\times \\tan 30^\\circ \\]"
        ans = "1"
        sol = (
            f"**Step 1:** Substitute exact values:\n"
            f"- \\(\\tan 60^\\circ = \\sqrt{{3}}\\)\n"
            f"- \\(\\tan 30^\\circ = \\frac{{1}}{{\\sqrt{{3}}}}\\)\n\n"
            f"**Step 2:** Multiply:\n"
            f"\\[ \\sqrt{{3}} \\times \\frac{{1}}{{\\sqrt{{3}}}} = 1 \\]"
        )
    else:
        prompt = "Without using a calculator, simplify:\n\\[ \\sin 60^\\circ \\times \\cos 30^\\circ \\]"
        ans = "3/4"
        sol = (
            f"**Step 1:** Substitute exact values:\n"
            f"- \\(\\sin 60^\\circ = \\frac{{\\sqrt{{3}}}}{{2}}\\)\n"
            f"- \\(\\cos 30^\\circ = \\frac{{\\sqrt{{3}}}}{{2}}\\)\n\n"
            f"**Step 2:** Multiply:\n"
            f"\\[ \\frac{{\\sqrt{{3}}}}{{2}} \\times \\frac{{\\sqrt{{3}}}}{{2}} = \\frac{{3}}{{4}} \\]"
        )

    return {
        "id": f"g10_trig_14_{rng.randint(100000, 999999)}",
        "subskill": "14_special_angles_simplify_product_and_quotient",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_14",
        "misconception_tags": ["surd_multiplication_error", "special_angle_product_confusion"],
        "marking_schema": [
            {"step": 1, "criterion": "Substitute exact surd values", "marks": 1},
            {"step": 2, "criterion": "Multiply surds accurately", "marks": 1},
        ],
        "hints": {
            "tier_1": "Recall: sqrt(3) * sqrt(3) = 3.",
            "tier_2": "Substitute the exact values and simplify the fraction.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_14_special_angles_simplify_product_and_quotient",
    }


# 15. Special angles pythagorean identity numeric proof: sin^2 θ + cos^2 θ = 1
def arch_15_special_angles_pythagorean_identity_numeric_proof(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([30, 45, 60])
    prompt = (
        f"Verify numerically that \\(\\sin^2 {angle}^\\circ + \\cos^2 {angle}^\\circ = 1\\) "
        f"by substituting exact special angle values."
    )
    ans = "1"
    if angle == 30:
        sol = (
            f"**Step 1:** Substitute values for 30°:\n"
            f"- \\(\\sin 30^\\circ = \\frac{{1}}{{2}} \\implies \\sin^2 30^\\circ = \\left(\\frac{{1}}{{2}}\\right)^2 = \\frac{{1}}{{4}}\\)\n"
            f"- \\(\\cos 30^\\circ = \\frac{{\\sqrt{{3}}}}{{2}} \\implies \\cos^2 30^\\circ = \\left(\\frac{{\\sqrt{{3}}}}{{2}}\\right)^2 = \\frac{{3}}{{4}}\\)\n\n"
            f"**Step 2:** Add:\n"
            f"\\[ \\frac{{1}}{{4}} + \\frac{{3}}{{4}} = \\frac{{4}}{{4}} = 1 \\]"
        )
    elif angle == 45:
        sol = (
            f"**Step 1:** Substitute values for 45°:\n"
            f"- \\(\\sin 45^\\circ = \\frac{{1}}{{\\sqrt{{2}}}} \\implies \\sin^2 45^\\circ = \\frac{{1}}{{2}}\\)\n"
            f"- \\(\\cos 45^\\circ = \\frac{{1}}{{\\sqrt{{2}}}} \\implies \\cos^2 45^\\circ = \\frac{{1}}{{2}}\\)\n\n"
            f"**Step 2:** Add:\n"
            f"\\[ \\frac{{1}}{{2}} + \\frac{{1}}{{2}} = 1 \\]"
        )
    else:  # 60
        sol = (
            f"**Step 1:** Substitute values for 60°:\n"
            f"- \\(\\sin 60^\\circ = \\frac{{\\sqrt{{3}}}}{{2}} \\implies \\sin^2 60^\\circ = \\frac{{3}}{{4}}\\)\n"
            f"- \\(\\cos 60^\\circ = \\frac{{1}}{{2}} \\implies \\cos^2 60^\\circ = \\frac{{1}}{{4}}\\)\n\n"
            f"**Step 2:** Add:\n"
            f"\\[ \\frac{{3}}{{4}} + \\frac{{1}}{{4}} = 1 \\]"
        )

    return {
        "id": f"g10_trig_15_{rng.randint(100000, 999999)}",
        "subskill": "15_special_angles_pythagorean_identity_numeric_proof",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": "1",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_15",
        "misconception_tags": ["squaring_trig_ratios_notation_confusion", "identity_numerical_verification"],
        "marking_schema": [
            {"step": 1, "criterion": "Square each special angle value correctly", "marks": 1},
            {"step": 2, "criterion": "Show sum equals 1", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Find sin({angle}°) and cos({angle}°), square each one, then add.",
            "tier_2": "The squares sum to 1.",
            "tier_3": "1",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_15_special_angles_pythagorean_identity_numeric_proof",
    }


# 16. Calculator evaluate direct sin cos tan to 2 d.p.
def arch_16_calculator_evaluate_direct_sin_cos_tan(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([18, 27, 34, 41, 52, 68, 73, 81])
    fn = rng.choice(["sin", "cos", "tan"])
    rad = math.radians(angle)
    val = {"sin": math.sin(rad), "cos": math.cos(rad), "tan": math.tan(rad)}[fn]
    rounded = round(val, 2)
    ans_str = f"{rounded:.2f}".replace(".", ",")

    prompt = (
        f"Use a scientific calculator to evaluate \\(\\{fn} {angle}^\\circ\\).\n\n"
        f"Round your answer to two decimal places (use South African comma decimal notation)."
    )
    sol = (
        f"**Step 1:** Ensure your calculator is set to **DEG** (degrees) mode.\n\n"
        f"**Step 2:** Key in \\(\\{fn}({angle})\\):\n"
        f"\\[ \\{fn} {angle}^\\circ \\approx {val:.4f} \\]\n\n"
        f"**Step 3:** Round to two decimal places:\n"
        f"\\[ \\{fn} {angle}^\\circ = {ans_str} \\]"
    )
    return {
        "id": f"g10_trig_16_{rng.randint(100000, 999999)}",
        "subskill": "16_calculator_evaluate_direct_sin_cos_tan",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_16",
        "misconception_tags": ["calculator_in_radian_mode", "rounding_to_two_decimal_places"],
        "marking_schema": [
            {"step": 1, "criterion": "Correct raw value in degree mode", "marks": 1},
            {"step": 2, "criterion": "Correct rounding to 2 decimal places with decimal comma", "marks": 1},
        ],
        "hints": {
            "tier_1": "Ensure calculator is in DEG mode, not RAD.",
            "tier_2": f"Raw value is approximately {val:.4f}.",
            "tier_3": ans_str,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_16_calculator_evaluate_direct_sin_cos_tan",
    }


# 17. Calculator evaluate reciprocal sec cosec cot: sec 42 = 1 / cos 42
def arch_17_calculator_evaluate_reciprocal_sec_cosec_cot(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([25, 38, 42, 55, 64, 71])
    recip = rng.choice(["sec", "csc", "cot"])
    rad = math.radians(angle)
    if recip == "sec":
        val = 1.0 / math.cos(rad)
        base = f"\\frac{{1}}{{\\cos {angle}^\\circ}}"
    elif recip == "csc":
        val = 1.0 / math.sin(rad)
        base = f"\\frac{{1}}{{\\sin {angle}^\\circ}}"
    else:
        val = 1.0 / math.tan(rad)
        base = f"\\frac{{1}}{{\\tan {angle}^\\circ}}"

    rounded = round(val, 2)
    ans_str = f"{rounded:.2f}".replace(".", ",")

    prompt = (
        f"Use a scientific calculator to evaluate \\(\\{recip} {angle}^\\circ\\).\n\n"
        f"Round your answer to two decimal places."
    )
    sol = (
        f"**Step 1:** Express \\(\\{recip}\\) in terms of its reciprocal primary ratio:\n"
        f"\\[ \\{recip} {angle}^\\circ = {base} \\]\n\n"
        f"**Step 2:** Evaluate on calculator:\n"
        f"\\[ {base} \\approx {val:.4f} \\]\n\n"
        f"**Step 3:** Round to two decimal places:\n"
        f"\\[ {ans_str} \\]"
    )
    return {
        "id": f"g10_trig_17_{rng.randint(100000, 999999)}",
        "subskill": "17_calculator_evaluate_reciprocal_sec_cosec_cot",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_17",
        "misconception_tags": ["confusing_reciprocal_with_inverse_trig", "calculator_reciprocal_entry_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Rewrite in terms of primary trig ratio (1/cos, 1/sin, 1/tan)", "marks": 1},
            {"step": 2, "criterion": "Evaluate and round to 2 decimal places", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Recall: {recip} is 1 / (primary ratio). Scientific calculators do not have a dedicated {recip} key.",
            "tier_2": f"Calculate {base}.",
            "tier_3": ans_str,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_17_calculator_evaluate_reciprocal_sec_cosec_cot",
    }


# 18. Calculator evaluate bracketed angle expression: 3 sin(2 * theta) or 2 cos(theta) + 1
def arch_18_calculator_evaluate_bracketed_angle_expression(rng: random.Random) -> Dict[str, Any]:
    coeff = rng.choice([2, 3, 4])
    angle = rng.choice([20, 25, 35, 40])
    rad = math.radians(angle)
    val = coeff * math.sin(rad) + 1.5
    rounded = round(val, 2)
    ans_str = f"{rounded:.2f}".replace(".", ",")

    prompt = (
        f"Use a scientific calculator to evaluate the expression:\n"
        f"\\[ {coeff}\\sin({angle}^\\circ) + 1{{,}}5 \\]\n\n"
        f"Round your answer to two decimal places."
    )
    sol = (
        f"**Step 1:** Evaluate \\(\\sin({angle}^\\circ)\\):\n"
        f"\\[ \\sin({angle}^\\circ) \\approx {math.sin(rad):.4f} \\]\n\n"
        f"**Step 2:** Multiply by {coeff} and add 1,5:\n"
        f"\\[ {coeff}({math.sin(rad):.4f}) + 1{{,}}5 = {coeff * math.sin(rad):.4f} + 1{{,}}5 = {val:.4f} \\]\n\n"
        f"**Step 3:** Round to two decimal places:\n"
        f"\\[ {ans_str} \\]"
    )
    return {
        "id": f"g10_trig_18_{rng.randint(100000, 999999)}",
        "subskill": "18_calculator_evaluate_bracketed_angle_expression",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_18",
        "misconception_tags": ["order_of_operations_calculator_entry", "multiplying_angle_instead_of_ratio"],
        "marking_schema": [
            {"step": 1, "criterion": "Correct calculation order", "marks": 1},
            {"step": 2, "criterion": "Correct rounding to 2 decimal places", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Compute sin({angle}°) first, multiply by {coeff}, then add 1,5.",
            "tier_2": f"Intermediate: {coeff * math.sin(rad):.4f} + 1,5.",
            "tier_3": ans_str,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_18_calculator_evaluate_bracketed_angle_expression",
    }


# 19. Calculator solve acute angle inverse sin: sin theta = k
def arch_19_calculator_solve_acute_angle_inverse_sin(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([24, 33, 42, 51, 63, 72])
    k_val = round(math.sin(math.radians(angle)), 4)
    k_str = f"{k_val:.4f}".replace(".", ",")

    prompt = (
        f"Solve for acute angle \\(\\theta\\) (where \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\)):\n"
        f"\\[ \\sin \\theta = {k_str} \\]\n\n"
        f"Round your answer to one decimal place."
    )
    ans = f"{angle:.1f}".replace(".", ",")
    sol = (
        f"**Step 1:** Apply the inverse sine function (\\(\\sin^{{-1}}\\)) on your calculator:\n"
        f"\\[ \\theta = \\sin^{{-1}}({k_str}) \\]\n\n"
        f"**Step 2:** Calculate and round to one decimal place:\n"
        f"\\[ \\theta = {ans}^\\circ \\]"
    )
    return {
        "id": f"g10_trig_19_{rng.randint(100000, 999999)}",
        "subskill": "19_calculator_solve_acute_angle_inverse_sin",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"θ = {ans}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_19",
        "misconception_tags": ["dividing_by_sin_instead_of_arcsin", "rounding_error_angles"],
        "marking_schema": [
            {"step": 1, "criterion": "Apply arcsin / sin^-1", "marks": 1},
            {"step": 2, "criterion": "Round to 1 decimal place with degree unit", "marks": 1},
        ],
        "hints": {
            "tier_1": "Use the shift/2nd sin (sin^-1) key on your calculator.",
            "tier_2": f"theta = arcsin({k_str}).",
            "tier_3": f"{ans}°",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_19_calculator_solve_acute_angle_inverse_sin",
    }


# 20. Calculator solve acute angle inverse cos: cos theta = k
def arch_20_calculator_solve_acute_angle_inverse_cos(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([26, 35, 48, 57, 66, 75])
    k_val = round(math.cos(math.radians(angle)), 4)
    k_str = f"{k_val:.4f}".replace(".", ",")

    prompt = (
        f"Solve for acute angle \\(\\theta\\) (where \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\)):\n"
        f"\\[ \\cos \\theta = {k_str} \\]\n\n"
        f"Round your answer to one decimal place."
    )
    ans = f"{angle:.1f}".replace(".", ",")
    sol = (
        f"**Step 1:** Apply the inverse cosine function (\\(\\cos^{{-1}}\\)):\n"
        f"\\[ \\theta = \\cos^{{-1}}({k_str}) \\]\n\n"
        f"**Step 2:** Calculate and round to one decimal place:\n"
        f"\\[ \\theta = {ans}^\\circ \\]"
    )
    return {
        "id": f"g10_trig_20_{rng.randint(100000, 999999)}",
        "subskill": "20_calculator_solve_acute_angle_inverse_cos",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"θ = {ans}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_20",
        "misconception_tags": ["dividing_by_cos_fallacy", "inverse_trig_entry_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Apply arccos / cos^-1", "marks": 1},
            {"step": 2, "criterion": "Correct rounded angle in degrees", "marks": 1},
        ],
        "hints": {
            "tier_1": "Use the shift/2nd cos (cos^-1) key on your calculator.",
            "tier_2": f"theta = arccos({k_str}).",
            "tier_3": f"{ans}°",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_20_calculator_solve_acute_angle_inverse_cos",
    }


# 21. Calculator solve acute angle inverse tan: tan theta = k
def arch_21_calculator_solve_acute_angle_inverse_tan(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([22, 31, 43, 56, 68])
    k_val = round(math.tan(math.radians(angle)), 4)
    k_str = f"{k_val:.4f}".replace(".", ",")

    prompt = (
        f"Solve for acute angle \\(\\theta\\) (where \\(0^\\circ \\leq \\theta < 90^\\circ\\)):\n"
        f"\\[ \\tan \\theta = {k_str} \\]\n\n"
        f"Round your answer to one decimal place."
    )
    ans = f"{angle:.1f}".replace(".", ",")
    sol = (
        f"**Step 1:** Apply the inverse tangent function (\\(\\tan^{{-1}}\\)):\n"
        f"\\[ \\theta = \\tan^{{-1}}({k_str}) \\]\n\n"
        f"**Step 2:** Calculate and round to one decimal place:\n"
        f"\\[ \\theta = {ans}^\\circ \\]"
    )
    return {
        "id": f"g10_trig_21_{rng.randint(100000, 999999)}",
        "subskill": "21_calculator_solve_acute_angle_inverse_tan",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"θ = {ans}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_21",
        "misconception_tags": ["dividing_by_tan_fallacy", "inverse_tan_calculator_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Apply arctan / tan^-1", "marks": 1},
            {"step": 2, "criterion": "State angle rounded to 1 d.p.", "marks": 1},
        ],
        "hints": {
            "tier_1": "Use the shift/2nd tan (tan^-1) key on your calculator.",
            "tier_2": f"theta = arctan({k_str}).",
            "tier_3": f"{ans}°",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_21_calculator_solve_acute_angle_inverse_tan",
    }


# 22. Right triangle calculate opposite side given hypotenuse
def arch_22_right_triangle_calculate_opposite_side_given_hypotenuse_svg(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([25, 35, 40, 50, 55])
    hyp = rng.randint(12, 28)
    rad = math.radians(angle)
    opp = hyp * math.sin(rad)
    adj = hyp * math.cos(rad)
    rounded_opp = round(opp, 2)
    ans_str = f"{rounded_opp:.2f}".replace(".", ",")

    svg_str = _build_right_triangle_svg(
        adj, opp, hyp,
        adj_label="", opp_label="x", hyp_label=str(hyp),
        theta_label=f"{angle}°", vertex_A="A", vertex_B="B", vertex_C="C"
    )
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Right-angled triangle ABC with angle {angle}° at A and hypotenuse {hyp}",
    }

    prompt = (
        f"In right-angled triangle \\(ABC\\) shown, angle \\(\\angle A = {angle}^\\circ\\) and hypotenuse \\(AC = {hyp}\\).\n\n"
        f"Calculate the length of the opposite side \\(x = BC\\), correct to two decimal places."
    )
    sol = (
        f"**Step 1:** Select the trigonometric ratio linking opposite and hypotenuse:\n"
        f"\\[ \\sin({angle}^\\circ) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}} = \\frac{{x}}{{{hyp}}} \\]\n\n"
        f"**Step 2:** Multiply both sides by {hyp} to solve for \\(x\\):\n"
        f"\\[ x = {hyp} \\times \\sin({angle}^\\circ) \\]\n\n"
        f"**Step 3:** Calculate and round to 2 decimal places:\n"
        f"\\[ x \\approx {hyp} \\times {math.sin(rad):.4f} = {ans_str} \\]"
    )
    return {
        "id": f"g10_trig_22_{rng.randint(100000, 999999)}",
        "subskill": "22_right_triangle_calculate_opposite_side_given_hypotenuse_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"x = {ans_str}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_22",
        "misconception_tags": ["choosing_cos_instead_of_sin", "dividing_hypotenuse_by_sin"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Set up equation sin(theta) = x / hyp", "marks": 1},
            {"step": 2, "criterion": "Isolate x = hyp * sin(theta)", "marks": 1},
            {"step": 3, "criterion": "Accurate rounded answer", "marks": 1},
        ],
        "hints": {
            "tier_1": f"sin({angle}°) = opposite / hypotenuse = x / {hyp}.",
            "tier_2": f"x = {hyp} * sin({angle}°).",
            "tier_3": ans_str,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_22_right_triangle_calculate_opposite_side_given_hypotenuse_svg",
    }


# 23. Right triangle calculate adjacent side given hypotenuse
def arch_23_right_triangle_calculate_adjacent_side_given_hypotenuse_svg(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([28, 36, 44, 52, 62])
    hyp = rng.randint(10, 25)
    rad = math.radians(angle)
    adj = hyp * math.cos(rad)
    opp = hyp * math.sin(rad)
    rounded_adj = round(adj, 2)
    ans_str = f"{rounded_adj:.2f}".replace(".", ",")

    svg_str = _build_right_triangle_svg(
        adj, opp, hyp,
        adj_label="y", opp_label="", hyp_label=str(hyp),
        theta_label=f"{angle}°", vertex_A="A", vertex_B="B", vertex_C="C"
    )
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Right-angled triangle ABC with angle {angle}° and hypotenuse {hyp}",
    }

    prompt = (
        f"In the right-angled triangle \\(ABC\\), \\(\\angle A = {angle}^\\circ\\) and hypotenuse \\(AC = {hyp}\\).\n\n"
        f"Calculate the length of the adjacent side \\(y = AB\\), correct to two decimal places."
    )
    sol = (
        f"**Step 1:** Select the cosine ratio:\n"
        f"\\[ \\cos({angle}^\\circ) = \\frac{{\\text{{adjacent}}}}{{\\text{{hypotenuse}}}} = \\frac{{y}}{{{hyp}}} \\]\n\n"
        f"**Step 2:** Multiply both sides by {hyp}:\n"
        f"\\[ y = {hyp} \\times \\cos({angle}^\\circ) \\]\n\n"
        f"**Step 3:** Calculate and round to 2 decimal places:\n"
        f"\\[ y \\approx {hyp} \\times {math.cos(rad):.4f} = {ans_str} \\]"
    )
    return {
        "id": f"g10_trig_23_{rng.randint(100000, 999999)}",
        "subskill": "23_right_triangle_calculate_adjacent_side_given_hypotenuse_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"y = {ans_str}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_23",
        "misconception_tags": ["choosing_sin_instead_of_cos", "adjacent_hypotenuse_ratio_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Set up equation cos(theta) = y / hyp", "marks": 1},
            {"step": 2, "criterion": "Isolate y = hyp * cos(theta)", "marks": 1},
            {"step": 3, "criterion": "Accurate rounded answer", "marks": 1},
        ],
        "hints": {
            "tier_1": f"cos({angle}°) = adjacent / hypotenuse = y / {hyp}.",
            "tier_2": f"y = {hyp} * cos({angle}°).",
            "tier_3": ans_str,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_23_right_triangle_calculate_adjacent_side_given_hypotenuse_svg",
    }


# 24. Right triangle calculate hypotenuse given side and angle
def arch_24_right_triangle_calculate_hypotenuse_given_side_and_angle_svg(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([30, 38, 45, 54, 60])
    opp = rng.randint(8, 20)
    rad = math.radians(angle)
    hyp = opp / math.sin(rad)
    adj = hyp * math.cos(rad)
    rounded_hyp = round(hyp, 2)
    ans_str = f"{rounded_hyp:.2f}".replace(".", ",")

    svg_str = _build_right_triangle_svg(
        adj, opp, hyp,
        adj_label="", opp_label=str(opp), hyp_label="H",
        theta_label=f"{angle}°", vertex_A="A", vertex_B="B", vertex_C="C"
    )
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Right triangle ABC with angle {angle}° and opposite side {opp}",
    }

    prompt = (
        f"In right-angled triangle \\(ABC\\), \\(\\angle A = {angle}^\\circ\\) and the opposite side \\(BC = {opp}\\).\n\n"
        f"Calculate the length of the hypotenuse \\(H = AC\\), correct to two decimal places."
    )
    sol = (
        f"**Step 1:** Select the sine ratio:\n"
        f"\\[ \\sin({angle}^\\circ) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}} = \\frac{{{opp}}}{{H}} \\]\n\n"
        f"**Step 2:** Rearrange to isolate \\(H\\):\n"
        f"\\[ H = \\frac{{{opp}}}{{\\sin({angle}^\\circ)}} \\]\n\n"
        f"**Step 3:** Calculate and round to 2 decimal places:\n"
        f"\\[ H \\approx \\frac{{{opp}}}{{{math.sin(rad):.4f}}} = {ans_str} \\]"
    )
    return {
        "id": f"g10_trig_24_{rng.randint(100000, 999999)}",
        "subskill": "24_right_triangle_calculate_hypotenuse_given_side_and_angle_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"H = {ans_str}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_24",
        "misconception_tags": ["multiplying_instead_of_dividing_for_hypotenuse", "algebraic_transposition_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Set up equation sin(theta) = opp / H", "marks": 1},
            {"step": 2, "criterion": "Rearrange to H = opp / sin(theta)", "marks": 1},
            {"step": 3, "criterion": "Evaluate and round to 2 d.p.", "marks": 1},
        ],
        "hints": {
            "tier_1": f"sin({angle}°) = {opp} / H.",
            "tier_2": f"H = {opp} / sin({angle}°). Notice you divide by sin({angle}°).",
            "tier_3": ans_str,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_24_right_triangle_calculate_hypotenuse_given_side_and_angle_svg",
    }


# 25. Right triangle calculate opposite given adjacent tan
def arch_25_right_triangle_calculate_opposite_given_adjacent_tan_svg(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([25, 32, 48, 55, 62])
    adj = rng.randint(8, 22)
    rad = math.radians(angle)
    opp = adj * math.tan(rad)
    hyp = math.hypot(adj, opp)
    rounded_opp = round(opp, 2)
    ans_str = f"{rounded_opp:.2f}".replace(".", ",")

    svg_str = _build_right_triangle_svg(
        adj, opp, hyp,
        adj_label=str(adj), opp_label="h", hyp_label="",
        theta_label=f"{angle}°", vertex_A="A", vertex_B="B", vertex_C="C"
    )
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Right triangle ABC with adjacent side {adj} and angle {angle}°",
    }

    prompt = (
        f"In right-angled triangle \\(ABC\\), the adjacent side \\(AB = {adj}\\) and \\(\\angle A = {angle}^\\circ\\).\n\n"
        f"Calculate the length of the opposite side \\(h = BC\\), correct to two decimal places."
    )
    sol = (
        f"**Step 1:** Select the tangent ratio:\n"
        f"\\[ \\tan({angle}^\\circ) = \\frac{{\\text{{opposite}}}}{{\\text{{adjacent}}}} = \\frac{{h}}{{{adj}}} \\]\n\n"
        f"**Step 2:** Multiply both sides by {adj}:\n"
        f"\\[ h = {adj} \\times \\tan({angle}^\\circ) \\]\n\n"
        f"**Step 3:** Calculate and round to 2 decimal places:\n"
        f"\\[ h \\approx {adj} \\times {math.tan(rad):.4f} = {ans_str} \\]"
    )
    return {
        "id": f"g10_trig_25_{rng.randint(100000, 999999)}",
        "subskill": "25_right_triangle_calculate_opposite_given_adjacent_tan_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"h = {ans_str}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_25",
        "misconception_tags": ["using_sin_or_cos_when_hypotenuse_is_unknown", "rounding_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Set up equation tan(theta) = h / adj", "marks": 1},
            {"step": 2, "criterion": "Isolate h = adj * tan(theta)", "marks": 1},
            {"step": 3, "criterion": "Accurate rounded answer", "marks": 1},
        ],
        "hints": {
            "tier_1": f"tan({angle}°) = opposite / adjacent = h / {adj}.",
            "tier_2": f"h = {adj} * tan({angle}°).",
            "tier_3": ans_str,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_25_right_triangle_calculate_opposite_given_adjacent_tan_svg",
    }


BUILDERS_01_25 = {
    "01_identify_hypotenuse_opposite_adjacent_svg": arch_01_identify_hypotenuse_opposite_adjacent_svg,
    "02_sin_ratio_definition_from_triangle_svg": arch_02_sin_ratio_definition_from_triangle_svg,
    "03_cos_ratio_definition_from_triangle_svg": arch_03_cos_ratio_definition_from_triangle_svg,
    "04_tan_ratio_definition_from_triangle_svg": arch_04_tan_ratio_definition_from_triangle_svg,
    "05_reciprocal_cosec_ratio_definition": arch_05_reciprocal_cosec_ratio_definition,
    "06_reciprocal_sec_ratio_definition": arch_06_reciprocal_sec_ratio_definition,
    "07_reciprocal_cot_ratio_definition": arch_07_reciprocal_cot_ratio_definition,
    "08_pythagoras_find_missing_side_then_sin_cos": arch_08_pythagoras_find_missing_side_then_sin_cos,
    "09_special_angle_30_exact_values": arch_09_special_angle_30_exact_values,
    "10_special_angle_45_exact_values": arch_10_special_angle_45_exact_values,
    "11_special_angle_60_exact_values": arch_11_special_angle_60_exact_values,
    "12_special_angles_0_and_90_boundary_values": arch_12_special_angles_0_and_90_boundary_values,
    "13_special_angles_simplify_sum_and_difference": arch_13_special_angles_simplify_sum_and_difference,
    "14_special_angles_simplify_product_and_quotient": arch_14_special_angles_simplify_product_and_quotient,
    "15_special_angles_pythagorean_identity_numeric_proof": arch_15_special_angles_pythagorean_identity_numeric_proof,
    "16_calculator_evaluate_direct_sin_cos_tan": arch_16_calculator_evaluate_direct_sin_cos_tan,
    "17_calculator_evaluate_reciprocal_sec_cosec_cot": arch_17_calculator_evaluate_reciprocal_sec_cosec_cot,
    "18_calculator_evaluate_bracketed_angle_expression": arch_18_calculator_evaluate_bracketed_angle_expression,
    "19_calculator_solve_acute_angle_inverse_sin": arch_19_calculator_solve_acute_angle_inverse_sin,
    "20_calculator_solve_acute_angle_inverse_cos": arch_20_calculator_solve_acute_angle_inverse_cos,
    "21_calculator_solve_acute_angle_inverse_tan": arch_21_calculator_solve_acute_angle_inverse_tan,
    "22_right_triangle_calculate_opposite_side_given_hypotenuse_svg": arch_22_right_triangle_calculate_opposite_side_given_hypotenuse_svg,
    "23_right_triangle_calculate_adjacent_side_given_hypotenuse_svg": arch_23_right_triangle_calculate_adjacent_side_given_hypotenuse_svg,
    "24_right_triangle_calculate_hypotenuse_given_side_and_angle_svg": arch_24_right_triangle_calculate_hypotenuse_given_side_and_angle_svg,
    "25_right_triangle_calculate_opposite_given_adjacent_tan_svg": arch_25_right_triangle_calculate_opposite_given_adjacent_tan_svg,
}
