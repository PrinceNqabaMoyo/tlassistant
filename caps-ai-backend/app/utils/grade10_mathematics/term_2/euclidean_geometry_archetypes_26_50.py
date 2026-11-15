"""Grade 10 Mathematics — Term 2/3 — Euclidean Geometry: Archetypes 26 to 50.

Grounded in curriculum_docs_auto/Mathematics_Gr10/Term 3/04. Euclidean geometry 1.md
and 04. Euclidean geometry 2.md.
Covers:
  26-29: Similarity (equiangular AAA, proportional sides, calculate missing side, shadow application)
  30-39: Quadrilaterals (trapezium, parallelogram opp sides/angles/diagonals, rectangle, rhombus, square, kite, hierarchy)
  40-42: Proving special quadrilaterals (prove parallelogram, rhombus, rectangle)
  43-47: Mid-point Theorem (midpoint parallel & half, calculate length, converse, Varignon quadrilateral, multi-step rider)
  48-50: Formal deductions, polygon angle sum, comprehensive composite exam-level rider

100% deterministic, zero LLM, publication-grade inline SVG specs, South African comma decimals {{,}} in KaTeX.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "grade10_math_euclidean_geometry"
LO = "math10_euclidean_geometry"


def _add_pillars(
    q: Dict[str, Any],
    subskill_name: str,
    duration: int = 4,
    weight: int = 30,
) -> Dict[str, Any]:
    marks = int(q.get("marks", 2))
    schema = [
        {"criterion": "Correct geometric statement and valid theorem reason", "marks": max(1, marks - 1)},
        {"criterion": "Accurate algebraic calculation and correct final numerical value", "marks": 1},
    ]
    q.update({
        "topic": TOPIC,
        "topic_id": TOPIC,
        "subtopic_id": "euclidean_geometry",
        "grade": "10",
        "subject": "Mathematics",
        "difficulty": q.get("difficulty", "medium"),
        "mode": f"elementary_{subskill_name}",
        "term": 2,
        "caps_weight_percent": weight,
        "suggested_duration_mins": duration,
        "marking_schema": schema,
    })
    return q


def _svg_wrapper(inner_elements: str, width: int = 360, height: int = 240, view_box: str = "0 0 360 240") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" width="{width}" height="{height}" '
        f'style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">\n'
        f'{inner_elements}\n'
        f'</svg>'
    )


# --------------------------------------------------------------------------- #
# 26_similarity_equiangular_triangles_aaa
# --------------------------------------------------------------------------- #
def _build_26_similarity_equiangular_triangles_aaa(r: random.Random) -> Dict[str, Any]:
    a = r.randint(40, 60)
    b = r.randint(55, 75)
    c = 180 - (a + b)

    svg = _svg_wrapper(
        f'<polygon points="40,160 130,160 75,70" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="75" y="55" font-size="12" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="30" y="175" font-size="12" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="135" y="175" font-size="12" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="75" y="85" font-size="11" font-weight="bold" fill="#2563eb" text-anchor="middle">{a}°</text>\n'
        f'<text x="55" y="150" font-size="11" font-weight="bold" fill="#059669">{b}°</text>\n'
        f'<text x="105" y="150" font-size="11" font-weight="bold" fill="#d97706">{c}°</text>\n'
        f'<polygon points="180,180 320,180 235,40" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="235" y="28" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="170" y="195" font-size="13" font-weight="bold" fill="#0f172a">E</text>\n'
        f'<text x="325" y="195" font-size="13" font-weight="bold" fill="#0f172a">F</text>\n'
        f'<text x="235" y="60" font-size="12" font-weight="bold" fill="#2563eb" text-anchor="middle">{a}°</text>\n'
        f'<text x="205" y="170" font-size="12" font-weight="bold" fill="#059669">{b}°</text>\n'
        f'<text x="285" y="170" font-size="12" font-weight="bold" fill="#d97706">{c}°</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "a": a, "b": b, "c": c, "condition": "AAA"}

    prompt = f"In the diagram below, $\\triangle ABC$ and $\\triangle DEF$ have interior angles measuring {a}$^\\circ$, {b}$^\\circ$, and {c}$^\\circ$ respectively. What is the mathematical relationship between the two triangles?"
    corr = "\\triangle ABC \\;|||\\; \\triangle DEF \\text{ (similar, equiangular / AAA)}"
    opts = [
        "\\triangle ABC \\;|||\\; \\triangle DEF \\text{ (similar, equiangular / AAA)}",
        "\\triangle ABC \\equiv \\triangle DEF \\text{ (congruent by AAA)}",
        "\\triangle ABC \\text{ and } \\triangle DEF \\text{ are neither similar nor congruent}",
        "\\triangle ABC \\equiv \\triangle DEF \\text{ (congruent by SSS)}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_26_{r.randint(1000, 9999)}",
        "subskill": "26_similarity_equiangular_triangles_aaa",
        "question_type": "mcq",
        "title": "Similarity: Equiangular Triangles (AAA)",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{Since all three pairs of corresponding angles are equal:}}\\\\\\hat{{A}} = \\hat{{D}} = {a}^\\circ, \\; \\hat{{B}} = \\hat{{E}} = {b}^\\circ, \\; \\hat{{C}} = \\hat{{F}} = {c}^\\circ.\\\\\n\\therefore \\triangle ABC \\;|||\\; \\triangle DEF \\quad \\text{{(equiangular / AAA)}}.",
        "explanation": f"Triangles with corresponding angles equal are similar (same shape, different size), denoted ||| (AAA). They are not necessarily congruent.",
        "marks": 2,
        "hints": {
            "tier_1": "Notice that all corresponding angles are equal, but side lengths are different.",
            "tier_2": "Equal angles guarantee the same shape (similarity), not congruence.",
            "tier_3": "Correct statement: $\\triangle ABC \\;|||\\; \\triangle DEF$ (AAA).",
        },
        "misconception_tags": ["confuses_similarity_with_congruence"],
        "diagram_spec": diag,
    }, "26_similarity_equiangular_triangles_aaa")


# --------------------------------------------------------------------------- #
# 27_similarity_proportional_sides_ratio
# --------------------------------------------------------------------------- #
def _build_27_similarity_proportional_sides_ratio(r: random.Random) -> Dict[str, Any]:
    scale = r.choice([2, 3, 4])
    s1, s2, s3 = 3, 4, 5
    d1, d2, d3 = s1 * scale, s2 * scale, s3 * scale

    svg = _svg_wrapper(
        f'<polygon points="40,160 120,160 40,80" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="25" y="80" font-size="12" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="25" y="175" font-size="12" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="125" y="175" font-size="12" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="20" y="125" font-size="11" font-weight="bold" fill="#2563eb">{s1}</text>\n'
        f'<text x="75" y="175" font-size="11" font-weight="bold" fill="#059669">{s2}</text>\n'
        f'<text x="85" y="115" font-size="11" font-weight="bold" fill="#dc2626">{s3}</text>\n'
        f'<polygon points="170,180 320,180 170,30" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="155" y="30" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="155" y="195" font-size="13" font-weight="bold" fill="#0f172a">E</text>\n'
        f'<text x="325" y="195" font-size="13" font-weight="bold" fill="#0f172a">F</text>\n'
        f'<text x="145" y="110" font-size="12" font-weight="bold" fill="#2563eb">{d1}</text>\n'
        f'<text x="240" y="195" font-size="12" font-weight="bold" fill="#059669">{d2}</text>\n'
        f'<text x="250" y="100" font-size="12" font-weight="bold" fill="#dc2626">{d3}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "scale": scale, "s": [s1, s2, s3], "d": [d1, d2, d3]}

    prompt = f"In the diagram below, $\\triangle ABC \\;|||\\; \\triangle DEF$. The sides are $AB = {s1}, BC = {s2}, AC = {s3}$ and $DE = {d1}, EF = {d2}, DF = {d3}$. Determine the scale factor $k = \\frac{{DE}}{{AB}}$."
    corr = f"k = {scale}"
    opts = [f"k = {scale}", f"k = {scale + 1}", f"k = \\frac{{1}}{{{scale}}}", f"k = {scale * 2}"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_27_{r.randint(1000, 9999)}",
        "subskill": "27_similarity_proportional_sides_ratio",
        "question_type": "mcq",
        "title": "Similarity: Scale Factor and Proportional Sides",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"k = \\frac{{DE}}{{AB}} = \\frac{{{d1}}}{{{s1}}} = {scale}. \\quad \\text{{Check: }} \\frac{{EF}}{{BC}} = \\frac{{{d2}}}{{{s2}}} = {scale}, \\; \\frac{{DF}}{{AC}} = \\frac{{{d3}}}{{{s3}}} = {scale}.",
        "explanation": f"In similar triangles, corresponding sides are in constant proportion: $\\frac{{{d1}}}{{{s1}}} = \\frac{{{d2}}}{{{s2}}} = \\frac{{{d3}}}{{{s3}}} = {scale}$.",
        "marks": 2,
        "hints": {
            "tier_1": "Divide any side of the larger triangle by its corresponding side in the smaller triangle.",
            "tier_2": f"Compare $DE$ and $AB$: $\\frac{{{d1}}}{{{s1}}} = {scale}$.",
            "tier_3": f"Scale factor is $k = {scale}$.",
        },
        "misconception_tags": ["inverts_ratio_smaller_over_larger"],
        "diagram_spec": diag,
    }, "27_similarity_proportional_sides_ratio")


# --------------------------------------------------------------------------- #
# 28_similarity_calculate_missing_side
# --------------------------------------------------------------------------- #
def _build_28_similarity_calculate_missing_side(r: random.Random) -> Dict[str, Any]:
    scale = r.choice([2, 3, 5])
    ab = r.randint(4, 8)
    de = ab * scale
    bc = r.randint(3, 7)
    ef = bc * scale

    svg = _svg_wrapper(
        f'<polygon points="40,160 130,160 85,70" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="80" y="55" font-size="12" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="30" y="175" font-size="12" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="135" y="175" font-size="12" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="50" y="110" font-size="11" font-weight="bold" fill="#2563eb">{ab}</text>\n'
        f'<text x="80" y="175" font-size="11" font-weight="bold" fill="#059669">{bc}</text>\n'
        f'<polygon points="170,180 320,180 245,30" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="240" y="20" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="155" y="195" font-size="13" font-weight="bold" fill="#0f172a">E</text>\n'
        f'<text x="325" y="195" font-size="13" font-weight="bold" fill="#0f172a">F</text>\n'
        f'<text x="190" y="100" font-size="12" font-weight="bold" fill="#2563eb">{de}</text>\n'
        f'<text x="240" y="195" font-size="12" font-weight="bold" fill="#dc2626">x</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "ab": ab, "de": de, "bc": bc, "ef": ef}

    prompt = f"Given that $\\triangle ABC \\;|||\\; \\triangle DEF$, with $AB = {ab}$, $DE = {de}$, and $BC = {bc}$. Calculate the length of side $EF = x$."
    corr = f"{ef}"
    opts = [f"{ef}", f"{ef + scale}", f"{ef - 1}", f"{bc + de}"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_28_{r.randint(1000, 9999)}",
        "subskill": "28_similarity_calculate_missing_side",
        "question_type": "mcq",
        "title": "Calculate Missing Side Using Similarity Ratio",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\frac{{EF}}{{BC}} = \\frac{{DE}}{{AB}} \\quad \\text{{(sides in proportion, }} \\triangle ABC \\;|||\\; \\triangle DEF\\text{{)}}\\\\\\frac{{x}}{{{bc}}} = \\frac{{{de}}}{{{ab}}} = {scale} \\implies x = {bc} \\times {scale} = {ef}.",
        "explanation": f"Using the similarity proportion: $\\frac{{x}}{{{bc}}} = \\frac{{{de}}}{{{ab}}} \\implies x = {ef}$.",
        "marks": 2,
        "hints": {
            "tier_1": "Set up a proportion between corresponding sides: $\\frac{EF}{BC} = \\frac{DE}{AB}$.",
            "tier_2": f"Find scale factor: $\\frac{{{de}}}{{{ab}}} = {scale}$.",
            "tier_3": f"Multiply $BC$ by {scale}: ${bc} \\times {scale} = {ef}$.",
        },
        "misconception_tags": ["adds_difference_instead_of_multiplying_ratio"],
        "diagram_spec": diag,
    }, "28_similarity_calculate_missing_side")


# --------------------------------------------------------------------------- #
# 29_similarity_shadow_and_height_application
# --------------------------------------------------------------------------- #
def _build_29_similarity_shadow_and_height_application(r: random.Random) -> Dict[str, Any]:
    pole_h = r.choice([2, 3])
    pole_s = r.choice([3, 4])
    tree_s = pole_s * r.choice([4, 5, 6])
    tree_h = (pole_h * tree_s) // pole_s

    svg = _svg_wrapper(
        f'<line x1="30" y1="200" x2="330" y2="200" stroke="#64748b" stroke-width="3"/>\n'
        f'<line x1="60" y1="200" x2="60" y2="120" stroke="#334155" stroke-width="3"/>\n'
        f'<line x1="60" y1="120" x2="140" y2="200" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'<text x="45" y="160" font-size="12" font-weight="bold" fill="#2563eb">{pole_h} m</text>\n'
        f'<text x="90" y="215" font-size="12" font-weight="bold" fill="#0f172a">{pole_s} m</text>\n'
        f'<line x1="180" y1="200" x2="180" y2="40" stroke="#16a34a" stroke-width="4"/>\n'
        f'<line x1="180" y1="40" x2="330" y2="200" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="4,4"/>\n'
        f'<text x="160" y="110" font-size="12" font-weight="bold" fill="#dc2626">H = ?</text>\n'
        f'<text x="240" y="215" font-size="12" font-weight="bold" fill="#0f172a">{tree_s} m</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "pole_h": pole_h, "pole_s": pole_s, "tree_s": tree_s, "tree_h": tree_h}

    prompt = f"At the same time of day, a vertical pole of height {pole_h} m casts a shadow of {pole_s} m on level ground, while a nearby building casts a shadow of {tree_s} m. Calculate the height of the building ($H$)."
    corr = f"{tree_h}\\text{{ m}}"
    opts = [f"{tree_h}\\text{{ m}}", f"{tree_h + 2}\\text{{ m}}", f"{tree_h - 2}\\text{{ m}}", f"{tree_s - pole_s}\\text{{ m}}"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_29_{r.randint(1000, 9999)}",
        "subskill": "29_similarity_shadow_and_height_application",
        "question_type": "mcq",
        "title": "Similarity Application: Indirect Measurement",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{The sun's rays strike at the same angle, creating similar right-angled triangles:}}\\\\\\frac{{H}}{{{pole_h}}} = \\frac{{{tree_s}}}{{{pole_s}}} \\implies H = {pole_h} \\times \\frac{{{tree_s}}}{{{pole_s}}} = {tree_h}\\text{{ m}}.",
        "explanation": f"Using similar triangles formed by the sun's rays: $\\frac{{H}}{{{pole_h}}} = \\frac{{{tree_s}}}{{{pole_s}}} \\implies H = {tree_h}$ m.",
        "marks": 2,
        "hints": {
            "tier_1": "The pole and building form similar right-angled triangles with their shadows.",
            "tier_2": f"Set up the proportion: $\\frac{{H}}{{{pole_h}}} = \\frac{{{tree_s}}}{{{pole_s}}}$.",
            "tier_3": f"Cross-multiply to get $H = {tree_h}$ m.",
        },
        "misconception_tags": ["subtracts_shadows_instead_of_scaling"],
        "diagram_spec": diag,
    }, "29_similarity_shadow_and_height_application")


# --------------------------------------------------------------------------- #
# 30_trapezium_properties_and_angles
# --------------------------------------------------------------------------- #
def _build_30_trapezium_properties_and_angles(r: random.Random) -> Dict[str, Any]:
    angle_a = r.randint(65, 115)
    angle_d = 180 - angle_a

    svg = _svg_wrapper(
        f'<polygon points="90,60 210,60 280,180 50,180" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<path d="M 145 55 L 155 60 L 145 65" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<path d="M 160 175 L 170 180 L 160 185" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<text x="80" y="50" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="215" y="50" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="290" y="195" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="35" y="195" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="95" y="85" font-size="13" font-weight="bold" fill="#2563eb">{angle_a}°</text>\n'
        f'<text x="75" y="170" font-size="13" font-weight="bold" fill="#059669">x</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angle_a": angle_a, "angle_d": angle_d, "parallel": ["AB", "DC"]}

    prompt = f"In the quadrilateral $ABCD$ below, $AB \\parallel DC$ (trapezium). Given $\\hat{{A}} = {angle_a}^\\circ$, calculate the value of co-interior angle $x = \\hat{{D}}$."
    corr = f"{angle_d}^\\circ"
    opts = [f"{angle_d}^\\circ", f"{angle_a}^\\circ", f"{angle_d + 10}^\\circ", f"{90}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_30_{r.randint(1000, 9999)}",
        "subskill": "30_trapezium_properties_and_angles",
        "question_type": "mcq",
        "title": "Trapezium: Co-interior Angles Between Parallel Sides",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\hat{{A}} + \\hat{{D}} = 180^\\circ \\quad \\text{{(co-int angles, }} AB \\parallel DC\\text{{)}}\\\\{angle_a}^\\circ + x = 180^\\circ \\implies x = 180^\\circ - {angle_a}^\\circ = {angle_d}^\\circ.",
        "explanation": f"In a trapezium, angles between parallel sides on the same transversal are co-interior and sum to 180°: $180° - {angle_a}° = {angle_d}°$.",
        "marks": 2,
        "hints": {
            "tier_1": "A trapezium has one pair of parallel sides.",
            "tier_2": f"Angles $\\hat{{A}}$ and $\\hat{{D}}$ are co-interior between parallel lines $AB$ and $DC$, summing to 180°.",
            "tier_3": f"Calculate $180^\\circ - {angle_a}^\\circ = {angle_d}^\\circ$.",
        },
        "misconception_tags": ["assumes_opposite_angles_equal_in_trapezium"],
        "diagram_spec": diag,
    }, "30_trapezium_properties_and_angles")


# --------------------------------------------------------------------------- #
# 31_parallelogram_opposite_sides_equal
# --------------------------------------------------------------------------- #
def _build_31_parallelogram_opposite_sides_equal(r: random.Random) -> Dict[str, Any]:
    ab = r.randint(8, 20)
    ad = r.randint(5, 14)

    svg = _svg_wrapper(
        f'<polygon points="90,60 270,60 220,180 40,180" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<text x="80" y="50" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="280" y="50" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="230" y="195" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="30" y="195" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="175" y="50" font-size="13" font-weight="bold" fill="#2563eb">{ab} cm</text>\n'
        f'<text x="50" y="120" font-size="13" font-weight="bold" fill="#059669">{ad} cm</text>\n'
        f'<text x="130" y="195" font-size="13" font-weight="bold" fill="#dc2626">DC = ?</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "ab": ab, "ad": ad, "shape": "parallelogram"}

    prompt = f"In parallelogram $ABCD$ below, side $AB = {ab}\\text{{ cm}}$ and side $AD = {ad}\\text{{ cm}}$. State the length of opposite side $DC$ and give the official geometric reason."
    corr = f"DC = {ab}\\text{{ cm (opp sides of }} \\parallel\\text{{m)}}"
    opts = [
        f"DC = {ab}\\text{{ cm (opp sides of }} \\parallel\\text{{m)}}",
        f"DC = {ad}\\text{{ cm (opp sides of }} \\parallel\\text{{m)}}",
        f"DC = {ab + ad}\\text{{ cm (sum of sides)}}",
        f"DC = {ab}\\text{{ cm (diagonals bisect)}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_31_{r.randint(1000, 9999)}",
        "subskill": "31_parallelogram_opposite_sides_equal",
        "question_type": "mcq",
        "title": "Parallelogram: Opposite Sides are Equal",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"DC = AB = {ab}\\text{{ cm}} \\quad \\text{{(opp sides of }} \\parallel\\text{{m)}}.",
        "explanation": f"A fundamental property of any parallelogram is that opposite sides are equal in length.",
        "marks": 2,
        "hints": {
            "tier_1": "Recall the properties of a parallelogram: opposite sides are parallel AND equal.",
            "tier_2": f"Side $DC$ is directly opposite side $AB$.",
            "tier_3": f"Therefore $DC = {ab}$ cm with reason (opp sides of $\\parallel$m).",
        },
        "misconception_tags": ["mismatches_adjacent_for_opposite_sides"],
        "diagram_spec": diag,
    }, "31_parallelogram_opposite_sides_equal")


# --------------------------------------------------------------------------- #
# 32_parallelogram_opposite_angles_equal
# --------------------------------------------------------------------------- #
def _build_32_parallelogram_opposite_angles_equal(r: random.Random) -> Dict[str, Any]:
    angle_a = r.randint(55, 80)
    angle_b = 180 - angle_a

    svg = _svg_wrapper(
        f'<polygon points="90,60 270,60 220,180 40,180" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<text x="80" y="50" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="280" y="50" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="230" y="195" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="30" y="195" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="95" y="85" font-size="13" font-weight="bold" fill="#2563eb">{angle_a}°</text>\n'
        f'<text x="205" y="165" font-size="13" font-weight="bold" fill="#059669">\\hat{{C}} = ?</text>\n'
        f'<text x="240" y="85" font-size="13" font-weight="bold" fill="#dc2626">\\hat{{B}} = ?</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angle_a": angle_a, "angle_b": angle_b, "shape": "parallelogram"}

    prompt = f"In parallelogram $ABCD$ below, $\\hat{{A}} = {angle_a}^\\circ$. Determine the size of opposite angle $\\hat{{C}}$ and adjacent angle $\\hat{{B}}$."
    corr = f"\\hat{{C}} = {angle_a}^\\circ, \\; \\hat{{B}} = {angle_b}^\\circ"
    opts = [
        f"\\hat{{C}} = {angle_a}^\\circ, \\; \\hat{{B}} = {angle_b}^\\circ",
        f"\\hat{{C}} = {angle_b}^\\circ, \\; \\hat{{B}} = {angle_a}^\\circ",
        f"\\hat{{C}} = {angle_a}^\\circ, \\; \\hat{{B}} = {angle_a}^\\circ",
        f"\\hat{{C}} = 90^\\circ, \\; \\hat{{B}} = 90^\\circ",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_32_{r.randint(1000, 9999)}",
        "subskill": "32_parallelogram_opposite_angles_equal",
        "question_type": "mcq",
        "title": "Parallelogram: Opposite Angles are Equal",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\hat{{C}} = \\hat{{A}} = {angle_a}^\\circ \\quad \\text{{(opp angles of }} \\parallel\\text{{m)}}\\\\\\hat{{B}} = 180^\\circ - {angle_a}^\\circ = {angle_b}^\\circ \\quad \\text{{(co-int angles, }} AB \\parallel DC\\text{{)}}.",
        "explanation": f"Opposite angles of a parallelogram are equal ($\\hat{{C}} = \\hat{{A}} = {angle_a}°$), and consecutive angles are supplementary ($\\hat{{B}} = 180° - {angle_a}° = {angle_b}°$).",
        "marks": 2,
        "hints": {
            "tier_1": "In a parallelogram, opposite angles are equal, and adjacent angles sum to 180°.",
            "tier_2": f"$\\hat{{C}}$ is opposite $\\hat{{A}}$, so $\\hat{{C}} = {angle_a}^\\circ$.",
            "tier_3": f"$\\hat{{B}} = 180^\\circ - {angle_a}^\\circ = {angle_b}^\\circ$.",
        },
        "misconception_tags": ["confuses_consecutive_and_opposite_angles"],
        "diagram_spec": diag,
    }, "32_parallelogram_opposite_angles_equal")


# --------------------------------------------------------------------------- #
# 33_parallelogram_diagonals_bisect
# --------------------------------------------------------------------------- #
def _build_33_parallelogram_diagonals_bisect(r: random.Random) -> Dict[str, Any]:
    half_ac = r.randint(4, 9)
    full_ac = 2 * half_ac
    half_bd = r.randint(5, 11)
    full_bd = 2 * half_bd

    svg = _svg_wrapper(
        f'<polygon points="80,50 260,50 220,180 40,180" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="80" y1="50" x2="220" y2="180" stroke="#2563eb" stroke-width="1.8"/>\n'
        f'<line x1="260" y1="50" x2="40" y2="180" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<circle cx="150" cy="115" r="3.5" fill="#0f172a"/>\n'
        f'<text x="70" y="45" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="270" y="45" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="230" y="195" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="30" y="195" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="155" y="130" font-size="13" font-weight="bold" fill="#0f172a">M</text>\n'
        f'<text x="100" y="80" font-size="12" font-weight="bold" fill="#2563eb">AM = {half_ac}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "half_ac": half_ac, "full_ac": full_ac, "center": "M"}

    prompt = f"In parallelogram $ABCD$ below, the diagonals intersect at $M$. If $AM = {half_ac}\\text{{ cm}}$, calculate the full length of diagonal $AC$ and state the reason."
    corr = f"AC = {full_ac}\\text{{ cm (diagonals of }} \\parallel\\text{{m bisect each other)}}"
    opts = [
        f"AC = {full_ac}\\text{{ cm (diagonals of }} \\parallel\\text{{m bisect each other)}}",
        f"AC = {half_ac}\\text{{ cm (diagonals equal)}}",
        f"AC = {half_ac + 4}\\text{{ cm (opp sides of }} \\parallel\\text{{m)}}",
        f"AC = {full_ac + 2}\\text{{ cm (diagonals perp)}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_33_{r.randint(1000, 9999)}",
        "subskill": "33_parallelogram_diagonals_bisect",
        "question_type": "mcq",
        "title": "Parallelogram: Diagonals Bisect Each Other",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"AC = 2 \\times AM = 2 \\times {half_ac} = {full_ac}\\text{{ cm}} \\quad \\text{{(diagonals of }} \\parallel\\text{{m bisect each other)}}.",
        "explanation": f"The diagonals of a parallelogram bisect each other at their midpoint $M$. Therefore, $AC = 2 \\times AM = {full_ac}$ cm.",
        "marks": 2,
        "hints": {
            "tier_1": "The diagonals of a parallelogram cut each other in half (bisect).",
            "tier_2": f"If $AM = {half_ac}$, then $MC = {half_ac}$.",
            "tier_3": f"Full length $AC = 2 \\times {half_ac} = {full_ac}$ cm.",
        },
        "misconception_tags": ["thinks_diagonals_of_all_parallelograms_are_equal"],
        "diagram_spec": diag,
    }, "33_parallelogram_diagonals_bisect")


# --------------------------------------------------------------------------- #
# 34_parallelogram_algebraic_side_and_angle
# --------------------------------------------------------------------------- #
def _build_34_parallelogram_algebraic_side_and_angle(r: random.Random) -> Dict[str, Any]:
    x_val = r.randint(4, 9)
    # AB = 3x - 2, DC = x + 10  => 3x - x = 12 => 2x = 12 => x = 6
    diff = 2 * x_val
    k_add = r.randint(2, 6)
    k_sub = diff - k_add
    side_len = 3 * x_val - k_sub

    svg = _svg_wrapper(
        f'<polygon points="80,50 260,50 220,170 40,170" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<text x="70" y="45" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="270" y="45" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="230" y="185" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="30" y="185" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="150" y="45" font-size="12" font-weight="bold" fill="#2563eb">3x - {k_sub}</text>\n'
        f'<text x="110" y="185" font-size="12" font-weight="bold" fill="#059669">x + {k_add}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "x_val": x_val, "side_len": side_len}

    prompt = f"In parallelogram $ABCD$ below, opposite sides are given algebraically as $AB = 3x - {k_sub}$ and $DC = x + {k_add}$. Solve for $x$ and determine the length of $AB$."
    corr = f"x = {x_val}, \\; AB = {side_len}"
    opts = [
        f"x = {x_val}, \\; AB = {side_len}",
        f"x = {x_val + 2}, \\; AB = {side_len + 4}",
        f"x = {x_val}, \\; AB = {side_len - 2}",
        f"x = {k_add}, \\; AB = {side_len}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_34_{r.randint(1000, 9999)}",
        "subskill": "34_parallelogram_algebraic_side_and_angle",
        "question_type": "mcq",
        "title": "Algebraic Equation on Parallelogram Sides",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"3x - {k_sub} = x + {k_add} \\quad \\text{{(opp sides of }} \\parallel\\text{{m equal)}}\\\\2x = {k_add + k_sub} \\implies x = {x_val}.\\\\AB = 3({x_val}) - {k_sub} = {side_len}.",
        "explanation": f"Equate opposite sides: $3x - {k_sub} = x + {k_add} \\implies 2x = {k_add + k_sub} \\implies x = {x_val}$. Then $AB = {side_len}$.",
        "marks": 3,
        "hints": {
            "tier_1": "Opposite sides of a parallelogram are equal in length.",
            "tier_2": f"Set up the equation: $3x - {k_sub} = x + {k_add}$.",
            "tier_3": f"Solve for $x$: $x = {x_val}$, then substitute to find $AB = {side_len}$.",
        },
        "misconception_tags": ["algebraic_subtraction_error", "confuses_adjacent_with_opposite_sides"],
        "diagram_spec": diag,
    }, "34_parallelogram_algebraic_side_and_angle")


# --------------------------------------------------------------------------- #
# 35_rectangle_properties_right_angles_diagonals
# --------------------------------------------------------------------------- #
def _build_35_rectangle_properties_right_angles_diagonals(r: random.Random) -> Dict[str, Any]:
    w = r.randint(6, 12)
    h = r.randint(4, 9)
    v1, v2, v3, v4 = r.choice([("A", "B", "C", "D"), ("P", "Q", "R", "S"), ("K", "L", "M", "N")])
    d1 = f"{v1}{v3}"
    d2 = f"{v2}{v4}"

    svg = _svg_wrapper(
        f'<polygon points="60,60 280,60 280,180 60,180" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="60" y1="60" x2="280" y2="180" stroke="#2563eb" stroke-width="1.8"/>\n'
        f'<line x1="280" y1="60" x2="60" y2="180" stroke="#2563eb" stroke-width="1.8"/>\n'
        f'<rect x="60" y="162" width="18" height="18" fill="none" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<text x="50" y="55" font-size="13" font-weight="bold" fill="#0f172a">{v1}</text>\n'
        f'<text x="290" y="55" font-size="13" font-weight="bold" fill="#0f172a">{v2}</text>\n'
        f'<text x="290" y="195" font-size="13" font-weight="bold" fill="#0f172a">{v3}</text>\n'
        f'<text x="50" y="195" font-size="13" font-weight="bold" fill="#0f172a">{v4}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "w": w, "h": h, "shape": "rectangle"}

    prompt = f"In rectangle ${v1}{v2}{v3}{v4}$ shown below (with width ${w}\\text{{ cm}}$ and height ${h}\\text{{ cm}}$), which of the following statements is TRUE regarding its diagonals ${d1}$ and ${d2}$?"
    corr = f"Diagonals are equal in length and bisect each other ({d1} = {d2})"
    opts = [
        f"Diagonals are equal in length and bisect each other ({d1} = {d2})",
        f"Diagonals bisect at right angles ({d1} \\perp {d2})",
        "Diagonals bisect the corner vertex angles into 45° each",
        "Diagonals are perpendicular and have unequal lengths",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_35_{r.randint(1000, 9999)}",
        "subskill": "35_rectangle_properties_right_angles_diagonals",
        "question_type": "mcq",
        "title": "Rectangle Properties: Equal Diagonals",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{A rectangle is a parallelogram with four right angles. Its diagonals are equal in length ({d1} = {d2}) and bisect each other, but they do NOT bisect perpendicularly (unless it is a square).}}",
        "explanation": f"In a rectangle, diagonals are equal in length (${d1} = {d2}$) and bisect each other.",
        "marks": 2,
        "hints": {
            "tier_1": "Recall the defining properties that distinguish a rectangle from a general parallelogram.",
            "tier_2": f"A rectangle has equal diagonals (${d1} = {d2}$).",
            "tier_3": "The correct option is: Diagonals are equal in length and bisect each other.",
        },
        "misconception_tags": ["assumes_rectangle_diagonals_are_perpendicular"],
        "diagram_spec": diag,
    }, "35_rectangle_properties_right_angles_diagonals")


# --------------------------------------------------------------------------- #
# 36_rhombus_properties_perpendicular_diagonals
# --------------------------------------------------------------------------- #
def _build_36_rhombus_properties_perpendicular_diagonals(r: random.Random) -> Dict[str, Any]:
    side = r.randint(5, 15)
    v1, v2, v3, v4 = r.choice([("A", "B", "C", "D"), ("P", "Q", "R", "S"), ("K", "L", "M", "N")])

    svg = _svg_wrapper(
        f'<polygon points="180,40 280,120 180,200 80,120" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="180" y1="40" x2="180" y2="200" stroke="#2563eb" stroke-width="1.8"/>\n'
        f'<line x1="80" y1="120" x2="280" y2="120" stroke="#2563eb" stroke-width="1.8"/>\n'
        f'<rect x="180" y="102" width="18" height="18" fill="none" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<text x="180" y="28" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{v1}</text>\n'
        f'<text x="295" y="125" font-size="13" font-weight="bold" fill="#0f172a">{v2}</text>\n'
        f'<text x="180" y="215" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{v3}</text>\n'
        f'<text x="65" y="125" font-size="13" font-weight="bold" fill="#0f172a">{v4}</text>\n'
        f'<text x="190" y="115" font-size="12" font-weight="bold" fill="#0f172a">X</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "side": side, "shape": "rhombus"}

    prompt = f"In rhombus ${v1}{v2}{v3}{v4}$ below with side length ${side}\\text{{ cm}}$, diagonals ${v1}{v3}$ and ${v2}{v4}$ intersect at $X$. What is the size of angle ${v1}\\hat{{X}}{v2}$ and what special property do the diagonals have regarding vertex angles?"
    corr = f"{v1}\\hat{{X}}{v2} = 90^\\circ \\text{{ and diagonals bisect the vertex angles}}"
    opts = [
        f"{v1}\\hat{{X}}{v2} = 90^\\circ \\text{{ and diagonals bisect the vertex angles}}",
        f"{v1}\\hat{{X}}{v2} = 60^\\circ \\text{{ and diagonals are equal in length}}",
        f"{v1}\\hat{{X}}{v2} = 90^\\circ \\text{{ and diagonals are equal in length}}",
        f"{v1}\\hat{{X}}{v2} = 180^\\circ \\text{{ and diagonals are parallel}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_36_{r.randint(1000, 9999)}",
        "subskill": "36_rhombus_properties_perpendicular_diagonals",
        "question_type": "mcq",
        "title": "Rhombus Properties: Perpendicular Diagonals",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{In a rhombus, all four sides are equal, diagonals bisect perpendicularly at }} 90^\\circ \\text{{ (}} {v1}{v3} \\perp {v2}{v4} \\text{{), and the diagonals bisect the interior vertex angles.}}",
        "explanation": f"A rhombus has perpendicular diagonals that bisect each other and bisect the vertex angles: ${v1}\\hat{{X}}{v2} = 90^\\circ$.",
        "marks": 2,
        "hints": {
            "tier_1": "Recall that a rhombus is an equilateral parallelogram.",
            "tier_2": "The diagonals cross at right angles (90°).",
            "tier_3": f"${v1}\\hat{{X}}{v2} = 90^\\circ$ and diagonals bisect the vertex angles.",
        },
        "misconception_tags": ["confuses_rhombus_with_general_parallelogram"],
        "diagram_spec": diag,
    }, "36_rhombus_properties_perpendicular_diagonals")


# --------------------------------------------------------------------------- #
# 37_square_properties_regular_quadrilateral
# --------------------------------------------------------------------------- #
def _build_37_square_properties_regular_quadrilateral(r: random.Random) -> Dict[str, Any]:
    side = r.randint(4, 12)
    v1, v2, v3, v4 = r.choice([("A", "B", "C", "D"), ("P", "Q", "R", "S"), ("W", "X", "Y", "Z")])

    svg = _svg_wrapper(
        f'<rect x="80" y="40" width="160" height="160" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="80" y1="40" x2="240" y2="200" stroke="#2563eb" stroke-width="1.8"/>\n'
        f'<line x1="240" y1="40" x2="80" y2="200" stroke="#2563eb" stroke-width="1.8"/>\n'
        f'<rect x="80" y="182" width="18" height="18" fill="none" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<rect x="151" y="111" width="18" height="18" fill="none" stroke="#2563eb" stroke-width="1.5" transform="rotate(45 160 120)"/>\n'
        f'<text x="70" y="35" font-size="13" font-weight="bold" fill="#0f172a">{v1}</text>\n'
        f'<text x="245" y="35" font-size="13" font-weight="bold" fill="#0f172a">{v2}</text>\n'
        f'<text x="245" y="215" font-size="13" font-weight="bold" fill="#0f172a">{v3}</text>\n'
        f'<text x="70" y="215" font-size="13" font-weight="bold" fill="#0f172a">{v4}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "side": side, "shape": "square"}

    prompt = f"A square ${v1}{v2}{v3}{v4}$ with side length ${side}\\text{{ cm}}$ inherits all properties from both the rectangle and the rhombus. Which statement uniquely describes the diagonals of a square?"
    corr = "Diagonals are equal in length AND intersect perpendicularly at 90°"
    opts = [
        "Diagonals are equal in length AND intersect perpendicularly at 90°",
        "Diagonals are unequal in length and intersect at 90°",
        "Diagonals are equal in length but intersect at 60°",
        "Diagonals are parallel to opposite sides",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_37_{r.randint(1000, 9999)}",
        "subskill": "37_square_properties_regular_quadrilateral",
        "question_type": "mcq",
        "title": "Square: The Regular Quadrilateral",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": "\\text{A square has 4 equal sides and 4 right angles. It combines rectangle properties (equal diagonals) and rhombus properties (perpendicular diagonals bisecting vertex angles).}",
        "explanation": f"A square has diagonals that are both equal in length (${v1}{v3} = {v2}{v4}$) and perpendicular to each other (${v1}{v3} \\perp {v2}{v4}$).",
        "marks": 2,
        "hints": {
            "tier_1": "Think about what features a square shares with a rectangle and with a rhombus.",
            "tier_2": "Rectangle gives equal diagonals; rhombus gives perpendicular diagonals.",
            "tier_3": "Correct answer: Diagonals are equal in length AND intersect perpendicularly at 90°.",
        },
        "misconception_tags": ["confuses_rhombus_and_square_properties"],
        "diagram_spec": diag,
    }, "37_square_properties_regular_quadrilateral")


# --------------------------------------------------------------------------- #
# 38_kite_properties_adjacent_sides_diagonals
# --------------------------------------------------------------------------- #
def _build_38_kite_properties_adjacent_sides_diagonals(r: random.Random) -> Dict[str, Any]:
    top_side = r.randint(4, 8)
    bot_side = r.randint(9, 15)
    v1, v2, v3, v4 = r.choice([("A", "B", "C", "D"), ("P", "Q", "R", "S"), ("K", "L", "M", "N")])

    svg = _svg_wrapper(
        f'<polygon points="180,30 260,90 180,210 100,90" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="180" y1="30" x2="180" y2="210" stroke="#2563eb" stroke-width="2"/>\n'
        f'<line x1="100" y1="90" x2="260" y2="90" stroke="#dc2626" stroke-width="2"/>\n'
        f'<rect x="180" y="72" width="18" height="18" fill="none" stroke="#2563eb" stroke-width="1.8"/>\n'
        f'<text x="180" y="20" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{v1}</text>\n'
        f'<text x="270" y="95" font-size="13" font-weight="bold" fill="#0f172a">{v2}</text>\n'
        f'<text x="180" y="225" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{v3}</text>\n'
        f'<text x="85" y="95" font-size="13" font-weight="bold" fill="#0f172a">{v4}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "top": top_side, "bot": bot_side, "shape": "kite"}

    prompt = f"In kite ${v1}{v2}{v3}{v4}$ below with ${v1}{v2} = {v1}{v4} = {top_side}\\text{{ cm}}$ and ${v3}{v2} = {v3}{v4} = {bot_side}\\text{{ cm}}$, which diagonal is the main axis of symmetry that bisects the other diagonal at $90^\\circ$?"
    corr = f"Diagonal {v1}{v3} bisects {v2}{v4} at 90° and bisects vertex angles {v1} and {v3}"
    opts = [
        f"Diagonal {v1}{v3} bisects {v2}{v4} at 90° and bisects vertex angles {v1} and {v3}",
        f"Both diagonals bisect each other equally at 90°",
        f"Diagonal {v2}{v4} is longer and bisects {v1}{v3}",
        "Neither diagonal is perpendicular",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_38_{r.randint(1000, 9999)}",
        "subskill": "38_kite_properties_adjacent_sides_diagonals",
        "question_type": "mcq",
        "title": "Kite: Symmetry and Diagonal Properties",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{In a kite, the main diagonal (connecting the vertices between equal adjacent sides) is the axis of symmetry: it perpendicularly bisects the other diagonal and bisects the vertex angles.}}",
        "explanation": f"Diagonal ${v1}{v3}$ connects the vertices between equal sides; it is the line of symmetry that perpendicularly bisects ${v2}{v4}$.",
        "marks": 2,
        "hints": {
            "tier_1": "A kite has two pairs of equal adjacent sides.",
            "tier_2": "The main diagonal between the apexes acts as a mirror line.",
            "tier_3": f"Diagonal ${v1}{v3}$ perpendicularly bisects ${v2}{v4}$ and bisects vertex angles $\\hat{{{v1}}}$ and $\\hat{{{v3}}}$.",
        },
        "misconception_tags": ["assumes_both_diagonals_bisect_each_other_in_kite"],
        "diagram_spec": diag,
    }, "38_kite_properties_adjacent_sides_diagonals")


# --------------------------------------------------------------------------- #
# 39_quadrilateral_hierarchy_and_classification
# --------------------------------------------------------------------------- #
def _build_39_quadrilateral_hierarchy_and_classification(r: random.Random) -> Dict[str, Any]:
    statements = [
        ("Every rhombus is a parallelogram.", True, "a rhombus has two pairs of parallel opposite sides"),
        ("Every rectangle is a square.", False, "a rectangle does not necessarily have all four sides equal"),
        ("Every square is a rectangle.", True, "a square has four right angles and opposite sides parallel"),
        ("Every parallelogram is a trapezium.", True, "a parallelogram has at least one pair of parallel sides"),
        ("Every kite is a parallelogram.", False, "opposite sides of a kite are not generally parallel"),
    ]
    stmt, is_true, reason = r.choice(statements)

    prompt = f"Evaluate the geometric statement: \"{stmt}\" Is this statement true or false? Select the correct classification reasoning."
    if is_true:
        corr = f"True: Because {reason}"
        wrong = f"False: Because {reason}"
    else:
        corr = f"False: Because {reason}"
        wrong = f"True: Because {reason}"

    opts = [
        corr,
        wrong,
        "True: Because all quadrilaterals have equal diagonals",
        "False: Because only triangles have hierarchical classifications",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_39_{r.randint(1000, 9999)}",
        "subskill": "39_quadrilateral_hierarchy_and_classification",
        "question_type": "mcq",
        "title": "Quadrilateral Hierarchy and Classification",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{Classification: }} {corr}.",
        "explanation": f"According to the hierarchical definition of quadrilaterals: {corr}.",
        "marks": 2,
        "hints": {
            "tier_1": "Recall the quadrilateral tree: Trapezium -> Parallelogram -> (Rectangle & Rhombus) -> Square.",
            "tier_2": f"Test if every property required is guaranteed: {reason}.",
            "tier_3": f"Conclusion: {corr}.",
        },
        "misconception_tags": ["reverses_subset_inclusion_in_quadrilaterals"],
    }, "39_quadrilateral_hierarchy_and_classification")


# --------------------------------------------------------------------------- #
# 40_prove_quadrilateral_is_parallelogram
# --------------------------------------------------------------------------- #
def _build_40_prove_quadrilateral_is_parallelogram(r: random.Random) -> Dict[str, Any]:
    v1, v2, v3, v4 = r.choice([("A", "B", "C", "D"), ("P", "Q", "R", "S"), ("K", "L", "M", "N")])
    methods = [
        ("both pairs of opposite sides are parallel", f"{v1}{v2} || {v4}{v3} and {v1}{v4} || {v2}{v3}"),
        ("both pairs of opposite sides are equal in length", f"{v1}{v2} = {v4}{v3} and {v1}{v4} = {v2}{v3}"),
        ("both pairs of opposite interior angles are equal", f"angle {v1} = angle {v3} and angle {v2} = angle {v4}"),
        ("the diagonals bisect each other", f"{v1}X = X{v3} and {v2}X = X{v4}"),
        ("one pair of opposite sides is both equal and parallel", f"{v1}{v2} = {v4}{v3} and {v1}{v2} || {v4}{v3}"),
    ]
    valid_cond, notation = r.choice(methods)

    prompt = f"To formally prove that a given quadrilateral ${v1}{v2}{v3}{v4}$ is a parallelogram, which of the following is an official, sufficient test condition in Euclidean geometry?"
    corr = f"Prove that {valid_cond} ({notation})"
    opts = [
        f"Prove that {valid_cond} ({notation})",
        "Prove that all four interior angles sum to 360°",
        "Prove that the diagonals are perpendicular to each other",
        "Prove that one pair of adjacent sides is equal",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_40_{r.randint(1000, 9999)}",
        "subskill": "40_prove_quadrilateral_is_parallelogram",
        "question_type": "mcq",
        "title": "Proving a Quadrilateral is a Parallelogram",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{To prove a quad is a parallelogram, prove any 1 of the 5 standard conditions:}}\\\\1.\\; \\text{{Both pairs opp sides }} \\parallel.\\\\2.\\; \\text{{Both pairs opp sides }}=.\\\\3.\\; \\text{{Both pairs opp angles }}=.\\\\4.\\; \\text{{Diagonals bisect each other}}.\\\\5.\\; \\text{{One pair of opp sides is equal AND parallel}}.",
        "explanation": f"Sufficient condition: {valid_cond}.",
        "marks": 2,
        "hints": {
            "tier_1": "Review the five definitive tests to prove a quadrilateral is a parallelogram.",
            "tier_2": "Angles summing to 360° is true for ANY quadrilateral and does not prove it is a parallelogram.",
            "tier_3": f"Correct test: {valid_cond}.",
        },
        "misconception_tags": ["uses_360_angle_sum_as_proof_of_parallelogram"],
    }, "40_prove_quadrilateral_is_parallelogram")


# --------------------------------------------------------------------------- #
# 41_prove_quadrilateral_is_rhombus
# --------------------------------------------------------------------------- #
def _build_41_prove_quadrilateral_is_rhombus(r: random.Random) -> Dict[str, Any]:
    v1, v2, v3, v4 = r.choice([("A", "B", "C", "D"), ("P", "Q", "R", "S"), ("K", "L", "M", "N")])
    tests = [
        f"A parallelogram with a pair of adjacent sides equal ({v1}{v2} = {v1}{v4})",
        f"A parallelogram whose diagonals intersect perpendicularly at 90° ({v1}{v3} perpendicular to {v2}{v4})",
        "A parallelogram whose diagonals bisect the interior vertex angles",
        "A quadrilateral with all four sides equal in length",
    ]
    correct_test = r.choice(tests)
    distractors = [
        f"A parallelogram with equal diagonals ({v1}{v3} = {v2}{v4})",
        "A quadrilateral with four right angles",
        "A parallelogram with one angle measuring 90°",
    ]
    opts = [correct_test] + r.sample(distractors, 3)
    r.shuffle(opts)

    prompt = f"Which of the following conditions is sufficient to prove that a given parallelogram ${v1}{v2}{v3}{v4}$ is specifically a RHOMBUS?"

    return _add_pillars({
        "id": f"g10_euclid_41_{r.randint(1000, 9999)}",
        "subskill": "41_prove_quadrilateral_is_rhombus",
        "question_type": "mcq",
        "title": "Proving a Parallelogram is a Rhombus",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${correct_test}$",
        "expected_answer": f"${correct_test}$",
        "sample_answer": f"${correct_test}$",
        "worked_solution": "\\text{To prove a parallelogram is a rhombus, show that: (1) adjacent sides are equal, (2) diagonals are perpendicular, or (3) diagonals bisect the vertex angles.}",
        "explanation": f"{correct_test} is a sufficient condition to establish a rhombus.",
        "marks": 2,
        "hints": {
            "tier_1": "A rhombus is an equilateral parallelogram.",
            "tier_2": "Look for properties relating to equal adjacent sides or perpendicular diagonals.",
            "tier_3": f"Correct test: {correct_test}.",
        },
        "misconception_tags": ["confuses_rhombus_proof_with_rectangle_proof"],
    }, "41_prove_quadrilateral_is_rhombus")


# --------------------------------------------------------------------------- #
# 42_prove_quadrilateral_is_rectangle
# --------------------------------------------------------------------------- #
def _build_42_prove_quadrilateral_is_rectangle(r: random.Random) -> Dict[str, Any]:
    v1, v2, v3, v4 = r.choice([("A", "B", "C", "D"), ("P", "Q", "R", "S"), ("K", "L", "M", "N")])
    tests = [
        f"A parallelogram with at least one interior angle equal to 90° (\\hat{{{v1}}} = 90^\\circ)",
        f"A parallelogram whose diagonals are equal in length ({v1}{v3} = {v2}{v4})",
    ]
    correct_test = r.choice(tests)
    distractors = [
        f"A parallelogram whose diagonals intersect perpendicularly at 90° ({v1}{v3} \\perp {v2}{v4})",
        "A parallelogram with all four sides equal",
        "A quadrilateral whose opposite angles sum to 180°",
    ]
    opts = [correct_test] + distractors
    r.shuffle(opts)

    prompt = f"Which of the following conditions is sufficient to prove that a parallelogram ${v1}{v2}{v3}{v4}$ is specifically a RECTANGLE?"

    return _add_pillars({
        "id": f"g10_euclid_42_{r.randint(1000, 9999)}",
        "subskill": "42_prove_quadrilateral_is_rectangle",
        "question_type": "mcq",
        "title": "Proving a Parallelogram is a Rectangle",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${correct_test}$",
        "expected_answer": f"${correct_test}$",
        "sample_answer": f"${correct_test}$",
        "worked_solution": "\\text{To prove a parallelogram is a rectangle, prove either: (1) one angle is } 90^\\circ \\text{ or (2) the diagonals are equal in length (} AC = BD \\text{)}.",
        "explanation": f"Proving {correct_test} proves the parallelogram is a rectangle.",
        "marks": 2,
        "hints": {
            "tier_1": "A rectangle is an equiangular parallelogram.",
            "tier_2": "If one angle of a parallelogram is 90°, all four must be 90°.",
            "tier_3": f"Correct condition: {correct_test}.",
        },
        "misconception_tags": ["confuses_perpendicular_diagonals_with_equal_diagonals"],
    }, "42_prove_quadrilateral_is_rectangle")


# --------------------------------------------------------------------------- #
# 43_midpoint_theorem_segment_parallel_and_half
# --------------------------------------------------------------------------- #
def _build_43_midpoint_theorem_segment_parallel_and_half(r: random.Random) -> Dict[str, Any]:
    bc_len = r.randint(12, 28)
    de_len = bc_len / 2
    bc_str = f"{bc_len}"
    de_str = f"{de_len:g}"

    svg = _svg_wrapper(
        f'<polygon points="180,40 60,190 300,190" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="120" y1="115" x2="240" y2="115" stroke="#2563eb" stroke-width="2.5"/>\n'
        f'<circle cx="120" cy="115" r="3.5" fill="#2563eb"/>\n'
        f'<circle cx="240" cy="115" r="3.5" fill="#2563eb"/>\n'
        f'<text x="180" y="28" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>\n'
        f'<text x="45" y="205" font-size="14" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="310" y="205" font-size="14" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="100" y="115" font-size="13" font-weight="bold" fill="#2563eb">D</text>\n'
        f'<text x="255" y="115" font-size="13" font-weight="bold" fill="#2563eb">E</text>\n'
        f'<text x="180" y="215" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">BC = {bc_str} cm</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "bc": bc_len, "de": de_len}

    prompt = f"In $\\triangle ABC$ below, $D$ is the midpoint of $AB$ ($AD = DB$) and $E$ is the midpoint of $AC$ ($AE = EC$). If base $BC = {bc_str}\\text{{ cm}}$, determine the relationship between segment $DE$ and base $BC$."
    corr = f"DE \\parallel BC \\text{{ and }} DE = {de_str}\\text{{ cm (Midpoint Theorem)}}"
    opts = [
        f"DE \\parallel BC \\text{{ and }} DE = {de_str}\\text{{ cm (Midpoint Theorem)}}",
        f"DE \\parallel BC \\text{{ and }} DE = {bc_str}\\text{{ cm (Midpoint Theorem)}}",
        f"DE \\perp BC \\text{{ and }} DE = {de_str}\\text{{ cm (Pythagoras)}}",
        f"DE \\text{{ is not parallel to }} BC",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_43_{r.randint(1000, 9999)}",
        "subskill": "43_midpoint_theorem_segment_parallel_and_half",
        "question_type": "mcq",
        "title": "The Mid-point Theorem: Properties and Length",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{By the Mid-point Theorem:}}\\\\DE \\parallel BC \\quad \\text{{and}} \\quad DE = \\frac{{1}}{{2}} BC = \\frac{{1}}{{2}}({bc_str}) = {de_str}\\text{{ cm}}.",
        "explanation": f"The line segment joining the midpoints of two sides of a triangle is parallel to the third side and equal to half its length: $DE = \\frac{{1}}{{2}}({bc_str}) = {de_str}$ cm.",
        "marks": 2,
        "hints": {
            "tier_1": "Recall the Midpoint Theorem for triangles.",
            "tier_2": "The segment connecting the two midpoints is parallel to the base and exactly half its length.",
            "tier_3": f"Divide {bc_str} by 2: {de_str} cm, and $DE \\parallel BC$.",
        },
        "misconception_tags": ["forgets_factor_of_half_in_midpoint_theorem"],
        "diagram_spec": diag,
    }, "43_midpoint_theorem_segment_parallel_and_half")


# --------------------------------------------------------------------------- #
# 44_midpoint_theorem_calculate_length
# --------------------------------------------------------------------------- #
def _build_44_midpoint_theorem_calculate_length(r: random.Random) -> Dict[str, Any]:
    de_len = r.randint(6, 15)
    bc_len = 2 * de_len

    svg = _svg_wrapper(
        f'<polygon points="180,40 60,190 300,190" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="120" y1="115" x2="240" y2="115" stroke="#2563eb" stroke-width="2.5"/>\n'
        f'<text x="180" y="28" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">P</text>\n'
        f'<text x="45" y="205" font-size="14" font-weight="bold" fill="#0f172a">Q</text>\n'
        f'<text x="310" y="205" font-size="14" font-weight="bold" fill="#0f172a">R</text>\n'
        f'<text x="100" y="115" font-size="13" font-weight="bold" fill="#2563eb">M</text>\n'
        f'<text x="255" y="115" font-size="13" font-weight="bold" fill="#2563eb">N</text>\n'
        f'<text x="180" y="105" font-size="13" font-weight="bold" fill="#2563eb" text-anchor="middle">MN = {de_len} cm</text>\n'
        f'<text x="180" y="215" font-size="13" font-weight="bold" fill="#dc2626" text-anchor="middle">QR = ?</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "mn": de_len, "qr": bc_len}

    prompt = f"In $\\triangle PQR$ below, $M$ is the midpoint of $PQ$ and $N$ is the midpoint of $PR$. If segment $MN = {de_len}\\text{{ cm}}$, calculate the length of the base $QR$."
    corr = f"QR = {bc_len}\\text{{ cm (Midpoint Theorem)}}"
    opts = [
        f"QR = {bc_len}\\text{{ cm (Midpoint Theorem)}}",
        f"QR = {de_len}\\text{{ cm}}",
        f"QR = {de_len + 4}\\text{{ cm}}",
        f"QR = {bc_len + 2}\\text{{ cm}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_44_{r.randint(1000, 9999)}",
        "subskill": "44_midpoint_theorem_calculate_length",
        "question_type": "mcq",
        "title": "Midpoint Theorem: Calculate Base Length",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"QR = 2 \\times MN = 2 \\times {de_len} = {bc_len}\\text{{ cm}} \\quad \\text{{(Midpoint Theorem)}}.",
        "explanation": f"By the Midpoint Theorem, the base is twice the length of the midpoint line segment: $QR = 2 \\times {de_len} = {bc_len}$ cm.",
        "marks": 2,
        "hints": {
            "tier_1": "The base of the triangle is twice as long as the midpoint line segment.",
            "tier_2": f"Multiply $MN$ by 2: $2 \\times {de_len}$.",
            "tier_3": f"Therefore $QR = {bc_len}$ cm.",
        },
        "misconception_tags": ["divides_by_two_instead_of_multiplying"],
        "diagram_spec": diag,
    }, "44_midpoint_theorem_calculate_length")


# --------------------------------------------------------------------------- #
# 45_converse_midpoint_theorem_bisects_side
# --------------------------------------------------------------------------- #
def _build_45_converse_midpoint_theorem_bisects_side(r: random.Random) -> Dict[str, Any]:
    ac_len = r.randint(14, 30)
    ae_len = ac_len // 2

    svg = _svg_wrapper(
        f'<polygon points="180,40 60,190 300,190" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="120" y1="115" x2="240" y2="115" stroke="#2563eb" stroke-width="2.5"/>\n'
        f'<path d="M 175 110 L 185 115 L 175 120" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<path d="M 175 185 L 185 190 L 175 195" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<text x="180" y="28" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>\n'
        f'<text x="45" y="205" font-size="14" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="310" y="205" font-size="14" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="100" y="115" font-size="13" font-weight="bold" fill="#2563eb">D</text>\n'
        f'<text x="255" y="115" font-size="13" font-weight="bold" fill="#2563eb">E</text>\n'
        f'<text x="280" y="115" font-size="12" font-weight="bold" fill="#0f172a">AC = {ac_len} cm</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "ac": ac_len, "ae": ae_len}

    prompt = f"In $\\triangle ABC$ below, $D$ is the midpoint of $AB$, and line $DE \\parallel BC$ with $E$ on $AC$. If the total length $AC = {ac_len}\\text{{ cm}}$, what can be deduced about point $E$ and length $AE$?"
    corr = f"E \\text{{ is the midpoint of }} AC, \\; AE = {ae_len}\\text{{ cm (converse Midpoint Theorem)}}"
    opts = [
        f"E \\text{{ is the midpoint of }} AC, \\; AE = {ae_len}\\text{{ cm (converse Midpoint Theorem)}}",
        f"E \\text{{ is not a midpoint}}, \\; AE = {ac_len - 3}\\text{{ cm}}",
        f"AE = {ac_len}\\text{{ cm (sides equal)}}",
        f"E \\text{{ is the centroid of }} \\triangle ABC",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_45_{r.randint(1000, 9999)}",
        "subskill": "45_converse_midpoint_theorem_bisects_side",
        "question_type": "mcq",
        "title": "Converse of the Mid-point Theorem",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{By the converse of the Mid-point Theorem, a line drawn through the midpoint of one side of a triangle parallel to a second side bisects the third side:}}\\\\E \\text{{ is the midpoint of }} AC \\implies AE = EC = \\frac{{{ac_len}}}{{2}} = {ae_len}\\text{{ cm}}.",
        "explanation": f"Converse Midpoint Theorem states that line $DE$ through midpoint $D$ parallel to $BC$ must bisect side $AC$. Therefore $AE = {ae_len}$ cm.",
        "marks": 2,
        "hints": {
            "tier_1": "Recall the converse of the Midpoint Theorem.",
            "tier_2": "A line through the midpoint of one side parallel to another side bisects the third side.",
            "tier_3": f"$E$ bisects $AC$, so $AE = {ac_len} / 2 = {ae_len}$ cm.",
        },
        "misconception_tags": ["confuses_midpoint_theorem_with_converse"],
        "diagram_spec": diag,
    }, "45_converse_midpoint_theorem_bisects_side")


# --------------------------------------------------------------------------- #
# 46_midpoint_theorem_in_quadrilateral
# --------------------------------------------------------------------------- #
def _build_46_midpoint_theorem_in_quadrilateral(r: random.Random) -> Dict[str, Any]:
    v1, v2, v3, v4 = r.choice([("A", "B", "C", "D"), ("E", "F", "G", "H"), ("K", "L", "M", "N")])
    p1, p2, p3, p4 = r.choice([("P", "Q", "R", "S"), ("W", "X", "Y", "Z"), ("U", "V", "W", "X")])

    svg = _svg_wrapper(
        f'<polygon points="70,50 280,30 290,190 40,170" fill="none" stroke="#64748b" stroke-width="2"/>\n'
        f'<polygon points="175,40 285,110 165,180 55,110" fill="#e0e7ff" stroke="#2563eb" stroke-width="2.5"/>\n'
        f'<text x="60" y="45" font-size="12" font-weight="bold" fill="#0f172a">{v1}</text>\n'
        f'<text x="290" y="30" font-size="12" font-weight="bold" fill="#0f172a">{v2}</text>\n'
        f'<text x="300" y="200" font-size="12" font-weight="bold" fill="#0f172a">{v3}</text>\n'
        f'<text x="25" y="180" font-size="12" font-weight="bold" fill="#0f172a">{v4}</text>\n'
        f'<text x="175" y="30" font-size="12" font-weight="bold" fill="#2563eb">{p1}</text>\n'
        f'<text x="295" y="115" font-size="12" font-weight="bold" fill="#2563eb">{p2}</text>\n'
        f'<text x="165" y="200" font-size="12" font-weight="bold" fill="#2563eb">{p3}</text>\n'
        f'<text x="40" y="115" font-size="12" font-weight="bold" fill="#2563eb">{p4}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "outer": f"{v1}{v2}{v3}{v4}", "inner": f"{p1}{p2}{p3}{p4}"}

    prompt = f"In quadrilateral ${v1}{v2}{v3}{v4}$ (Varignon's Theorem), the midpoints of the four sides are joined consecutively to form inner quadrilateral ${p1}{p2}{p3}{p4}$. What type of quadrilateral is ${p1}{p2}{p3}{p4}$ always guaranteed to be?"
    corr = "A parallelogram (Varignon's Parallelogram)"
    opts = [
        "A parallelogram (Varignon's Parallelogram)",
        "A rectangle",
        "A rhombus",
        "A trapezium with no parallel sides",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_46_{r.randint(1000, 9999)}",
        "subskill": "46_midpoint_theorem_in_quadrilateral",
        "question_type": "mcq",
        "title": "Varignon's Theorem: Midpoints of a Quadrilateral",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": "\\text{Draw diagonal } AC. \\text{ In } \\triangle ABC, PQ \\parallel AC \\text{ and } PQ = \\frac{1}{2} AC \\text{ (Midpoint Thm). In } \\triangle ADC, SR \\parallel AC \\text{ and } SR = \\frac{1}{2} AC. \\text{ Thus } PQ = SR \\text{ and } PQ \\parallel SR, \\text{ proving } PQRS \\text{ is a parallelogram.}",
        "explanation": "Joining the midpoints of any quadrilateral always forms a parallelogram because both pairs of opposite segments are parallel to and half the diagonals.",
        "marks": 2,
        "hints": {
            "tier_1": "Apply the Midpoint Theorem using diagonal $AC$.",
            "tier_2": "Both $PQ$ and $SR$ are parallel to diagonal $AC$ and equal to half $AC$.",
            "tier_3": "One pair of opposite sides is equal and parallel, so $PQRS$ is a parallelogram.",
        },
        "misconception_tags": ["assumes_inner_shape_must_be_rectangle"],
        "diagram_spec": diag,
    }, "46_midpoint_theorem_in_quadrilateral")


# --------------------------------------------------------------------------- #
# 47_midpoint_theorem_multi_step_rider
# --------------------------------------------------------------------------- #
def _build_47_midpoint_theorem_multi_step_rider(r: random.Random) -> Dict[str, Any]:
    base = r.randint(16, 28)
    half = base // 2
    quarter = half // 2

    prompt = f"In $\\triangle ABC$, $D$ and $E$ are midpoints of $AB$ and $AC$ respectively, so $DE = {half}\\text{{ cm}}$ and $BC = {base}\\text{{ cm}}$. If $F$ is further the midpoint of $AD$ and $G$ is the midpoint of $AE$, calculate the length of segment $FG$."
    corr = f"FG = {quarter}\\text{{ cm}}"
    opts = [
        f"FG = {quarter}\\text{{ cm}}",
        f"FG = {half}\\text{{ cm}}",
        f"FG = {base}\\text{{ cm}}",
        f"FG = {quarter + 2}\\text{{ cm}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_47_{r.randint(1000, 9999)}",
        "subskill": "47_midpoint_theorem_multi_step_rider",
        "question_type": "mcq",
        "title": "Multi-Step Midpoint Theorem Rider",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{In }} \\triangle ADE, \\; F \\text{{ is midpoint of }} AD \\text{{ and }} G \\text{{ is midpoint of }} AE.\\\\\nFG = \\frac{{1}}{{2}} DE = \\frac{{1}}{{2}}({half}) = {quarter}\\text{{ cm}} \\quad \\text{{(Midpoint Theorem)}}.",
        "explanation": f"Applying the Midpoint Theorem repeatedly: $DE = \\frac{{1}}{{2}}BC = {half}$ cm, then $FG = \\frac{{1}}{{2}}DE = {quarter}$ cm.",
        "marks": 2,
        "hints": {
            "tier_1": "Apply the Midpoint Theorem inside the smaller triangle $\\triangle ADE$.",
            "tier_2": f"$FG$ joins the midpoints of $\\triangle ADE$, so $FG = \\frac{{1}}{{2}} DE$.",
            "tier_3": f"$FG = \\frac{{1}}{{2}} \\times {half} = {quarter}$ cm.",
        },
        "misconception_tags": ["applies_half_only_once"],
    }, "47_midpoint_theorem_multi_step_rider")


# --------------------------------------------------------------------------- #
# 48_geometric_rider_statement_and_reasons
# --------------------------------------------------------------------------- #
def _build_48_geometric_rider_statement_and_reasons(r: random.Random) -> Dict[str, Any]:
    items = [
        ("Adjacent angles on a straight line add to 180°", "(\\angle s on a straight line)"),
        ("Opposite angles of a parallelogram are equal", "(opp \\angle s of ||m)"),
        ("Angles subtended by equal sides in an isosceles triangle are equal", "(\\angle s opp equal sides)"),
        ("The line segment joining midpoints of two sides of a triangle is parallel and half of the third side", "(Midpoint Theorem)"),
        ("Angles on opposite sides of a transversal between parallel lines in a Z-pattern are equal", "(alt \\angle s, AB || CD)"),
    ]
    stmt, reason = r.choice(items)

    prompt = f"In formal Euclidean geometry proofs, what is the official examination reason code for the statement: \"{stmt}\"?"
    corr = f"{reason}"
    other_reasons = [r[1] for r in items if r[1] != reason]
    opts = [reason] + r.sample(other_reasons, 3)
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_48_{r.randint(1000, 9999)}",
        "subskill": "48_geometric_rider_statement_and_reasons",
        "question_type": "mcq",
        "title": "Formal Geometric Statements and Examination Reasons",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{The standard accepted curriculum reason is: }} {reason}.",
        "explanation": f"In South African geometry examinations, every geometric deduction requires an exact official reason: {reason}.",
        "marks": 2,
        "hints": {
            "tier_1": "Recall the standard abbreviated reason codes used in Grade 10 geometry.",
            "tier_2": f"The statement describes {stmt}.",
            "tier_3": f"Correct reason: {reason}.",
        },
        "misconception_tags": ["omits_parallel_lines_identifier_in_reasons"],
    }, "48_geometric_rider_statement_and_reasons")


# --------------------------------------------------------------------------- #
# 49_polygon_interior_and_exterior_angle_formula
# --------------------------------------------------------------------------- #
def _build_49_polygon_interior_and_exterior_angle_formula(r: random.Random) -> Dict[str, Any]:
    polygons = [
        ("pentagon", 5, 540, 108),
        ("hexagon", 6, 720, 120),
        ("heptagon", 7, 900, None),
        ("octagon", 8, 1080, 135),
        ("nonagon", 9, 1260, 140),
        ("decagon", 10, 1440, 144),
    ]
    name, n_sides, int_sum, each_reg = r.choice(polygons)

    prompt = f"Using the polygon interior angle formula $S = (n - 2) \\times 180^\\circ$, calculate the sum of the interior angles of a {name} ($n = {n_sides}$)."
    corr = f"{int_sum}^\\circ"
    opts = [f"{int_sum}^\\circ", f"{int_sum + 180}^\\circ", f"{int_sum - 180}^\\circ", f"{n_sides * 180}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_49_{r.randint(1000, 9999)}",
        "subskill": "49_polygon_interior_and_exterior_angle_formula",
        "question_type": "mcq",
        "title": "Sum of Interior Angles of an n-sided Polygon",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"S = (n - 2) \\times 180^\\circ = ({n_sides} - 2) \\times 180^\\circ = {n_sides - 2} \\times 180^\\circ = {int_sum}^\\circ.",
        "explanation": f"The sum of interior angles of an $n$-sided polygon is $(n - 2) \\times 180° = ({n_sides} - 2) \\times 180° = {int_sum}°$.",
        "marks": 2,
        "hints": {
            "tier_1": "Apply the formula $S = (n - 2) \\times 180^\\circ$.",
            "tier_2": f"Substitute $n = {n_sides}$: $S = ({n_sides} - 2) \\times 180^\\circ = {n_sides - 2} \\times 180^\\circ$.",
            "tier_3": f"Multiply: {n_sides - 2} * 180° = {int_sum}°.",
        },
        "misconception_tags": ["multiplies_n_by_180_without_subtracting_two"],
    }, "49_polygon_interior_and_exterior_angle_formula")


# --------------------------------------------------------------------------- #
# 50_composite_geometric_figure_comprehensive
# --------------------------------------------------------------------------- #
def _build_50_composite_geometric_figure_comprehensive(r: random.Random) -> Dict[str, Any]:
    angle_c = r.randint(48, 72)
    angle_b = 180 - 2 * angle_c

    svg = _svg_wrapper(
        f'<polygon points="60,60 260,60 210,180 50,180" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="210" y1="180" x2="260" y2="60" stroke="#2563eb" stroke-width="2"/>\n'
        f'<line x1="130" y1="120" x2="140" y2="120" stroke="#dc2626" stroke-width="2"/>\n'
        f'<line x1="230" y1="120" x2="240" y2="120" stroke="#dc2626" stroke-width="2"/>\n'
        f'<text x="50" y="50" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="270" y="50" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="220" y="195" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="40" y="195" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="190" y="165" font-size="12" font-weight="bold" fill="#2563eb">{angle_c}°</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angle_c": angle_c, "angle_b": angle_b}

    prompt = f"In the composite diagram below, $ABCD$ is a parallelogram with $AB \\parallel DC$ and $AD \\parallel BC$. A line segment inside $\\triangle BCD$ creates an isosceles triangle where base angle is {angle_c}$^\\circ$. Calculate the vertex angle $\\hat{{B}} = {angle_b}^\\circ$ and explain how it relates to $\\hat{{D}}$."
    corr = f"\\hat{{B}} = {angle_b}^\\circ, \\; \\hat{{D}} = {angle_b}^\\circ \\text{{ (opp angles of }} \\parallel\\text{{m equal)}}"
    opts = [
        f"\\hat{{B}} = {angle_b}^\\circ, \\; \\hat{{D}} = {angle_b}^\\circ \\text{{ (opp angles of }} \\parallel\\text{{m equal)}}",
        f"\\hat{{B}} = {angle_c}^\\circ, \\; \\hat{{D}} = {angle_c}^\\circ",
        f"\\hat{{B}} = {180 - angle_b}^\\circ, \\; \\hat{{D}} = {angle_b}^\\circ",
        f"\\hat{{B}} = 90^\\circ, \\; \\hat{{D}} = 90^\\circ",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_50_{r.randint(1000, 9999)}",
        "subskill": "50_composite_geometric_figure_comprehensive",
        "question_type": "mcq",
        "title": "Composite Exam-Level Geometric Rider",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{In the isosceles triangle, the two base angles are }} {angle_c}^\\circ.\\\\\n\\text{{Vertex angle }} \\hat{{B}} = 180^\\circ - 2({angle_c}^\\circ) = {angle_b}^\\circ.\\\\\n\\text{{Since }} ABCD \\text{{ is a parallelogram, }} \\hat{{D}} = \\hat{{B}} = {angle_b}^\\circ \\quad \\text{{(opp angles of }} \\parallel\\text{{m)}}.",
        "explanation": f"Combining the angle sum of an isosceles triangle ($180° - 2({angle_c}°) = {angle_b}°$) with opposite angles of a parallelogram being equal gives $\\hat{{D}} = \\hat{{B}} = {angle_b}°$.",
        "marks": 3,
        "hints": {
            "tier_1": "Calculate the unknown angle in the isosceles triangle first.",
            "tier_2": f"Vertex angle $= 180^\\circ - 2({angle_c}^\\circ) = {angle_b}^\\circ$.",
            "tier_3": f"Opposite angles of a parallelogram are equal, so $\\hat{{D}} = \\hat{{B}} = {angle_b}^\\circ$.",
        },
        "misconception_tags": ["fails_to_chain_intermediate_angle_reasons"],
        "diagram_spec": diag,
    }, "50_composite_geometric_figure_comprehensive")


# --------------------------------------------------------------------------- #
# EXPORTED BUILDERS DICT (26 to 50)
# --------------------------------------------------------------------------- #
BUILDERS_26_50: Dict[str, Any] = {
    "26_similarity_equiangular_triangles_aaa": _build_26_similarity_equiangular_triangles_aaa,
    "27_similarity_proportional_sides_ratio": _build_27_similarity_proportional_sides_ratio,
    "28_similarity_calculate_missing_side": _build_28_similarity_calculate_missing_side,
    "29_similarity_shadow_and_height_application": _build_29_similarity_shadow_and_height_application,
    "30_trapezium_properties_and_angles": _build_30_trapezium_properties_and_angles,
    "31_parallelogram_opposite_sides_equal": _build_31_parallelogram_opposite_sides_equal,
    "32_parallelogram_opposite_angles_equal": _build_32_parallelogram_opposite_angles_equal,
    "33_parallelogram_diagonals_bisect": _build_33_parallelogram_diagonals_bisect,
    "34_parallelogram_algebraic_side_and_angle": _build_34_parallelogram_algebraic_side_and_angle,
    "35_rectangle_properties_right_angles_diagonals": _build_35_rectangle_properties_right_angles_diagonals,
    "36_rhombus_properties_perpendicular_diagonals": _build_36_rhombus_properties_perpendicular_diagonals,
    "37_square_properties_regular_quadrilateral": _build_37_square_properties_regular_quadrilateral,
    "38_kite_properties_adjacent_sides_diagonals": _build_38_kite_properties_adjacent_sides_diagonals,
    "39_quadrilateral_hierarchy_and_classification": _build_39_quadrilateral_hierarchy_and_classification,
    "40_prove_quadrilateral_is_parallelogram": _build_40_prove_quadrilateral_is_parallelogram,
    "41_prove_quadrilateral_is_rhombus": _build_41_prove_quadrilateral_is_rhombus,
    "42_prove_quadrilateral_is_rectangle": _build_42_prove_quadrilateral_is_rectangle,
    "43_midpoint_theorem_segment_parallel_and_half": _build_43_midpoint_theorem_segment_parallel_and_half,
    "44_midpoint_theorem_calculate_length": _build_44_midpoint_theorem_calculate_length,
    "45_converse_midpoint_theorem_bisects_side": _build_45_converse_midpoint_theorem_bisects_side,
    "46_midpoint_theorem_in_quadrilateral": _build_46_midpoint_theorem_in_quadrilateral,
    "47_midpoint_theorem_multi_step_rider": _build_47_midpoint_theorem_multi_step_rider,
    "48_geometric_rider_statement_and_reasons": _build_48_geometric_rider_statement_and_reasons,
    "49_polygon_interior_and_exterior_angle_formula": _build_49_polygon_interior_and_exterior_angle_formula,
    "50_composite_geometric_figure_comprehensive": _build_50_composite_geometric_figure_comprehensive,
}
