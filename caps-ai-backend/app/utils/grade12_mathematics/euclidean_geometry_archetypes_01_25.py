"""Grade 12 Mathematics — Euclidean Geometry Archetypes 01 to 25.
Focus: Ratio, Proportion, Proportionality Theorem, Areas of Triangles, Applications.
Complies with official South African curriculum standards:
- 100% deterministic, seed-varied across seeds [101, 102, 103]
- 6-pillar contract: term, caps_weight_percent, duration, hints, marking schema, misconception tags
- Inline SVG diagram specs with diagram_role='context'
- LaTeX formatting with South African comma decimals {{,}}
- Zero trademark acronyms in learner-facing text
"""

from __future__ import annotations

import math
import random
from typing import Any, Dict


# --------------------------------------------------------------------------- #
# SVG Vector Drawing Helpers for Proportionality & Geometry Figures
# --------------------------------------------------------------------------- #

def _svg_wrap(inner_svg: str, width: int = 360, height: int = 260) -> str:
    return (
        f'<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" '
        f'xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; max-width:{width}px;">'
        f'{inner_svg}'
        f'</svg>'
    )


def _draw_triangle_parallel_svg(
    a_pt=(180, 30),
    b_pt=(50, 220),
    c_pt=(310, 220),
    t_ratio=0.55,
    labels=("A", "B", "C", "D", "E"),
    side_texts=None,
) -> str:
    """Draws triangle ABC with segment DE parallel to BC."""
    d_x = int(a_pt[0] + t_ratio * (b_pt[0] - a_pt[0]))
    d_y = int(a_pt[1] + t_ratio * (b_pt[1] - a_pt[1]))
    e_x = int(a_pt[0] + t_ratio * (c_pt[0] - a_pt[0]))
    e_y = int(a_pt[1] + t_ratio * (c_pt[1] - a_pt[1]))

    # Parallel arrow markers (small chevrons) on DE and BC
    de_mid_x = (d_x + e_x) // 2
    de_mid_y = (d_y + e_y) // 2
    bc_mid_x = (b_pt[0] + c_pt[0]) // 2
    bc_mid_y = (b_pt[1] + c_pt[1]) // 2

    elements = [
        f'<polygon points="{a_pt[0]},{a_pt[1]} {b_pt[0]},{b_pt[1]} {c_pt[0]},{c_pt[1]}" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>',
        f'<line x1="{d_x}" y1="{d_y}" x2="{e_x}" y2="{e_y}" stroke="#2563eb" stroke-width="2"/>',
        # Parallel markers >
        f'<path d="M {de_mid_x - 6} {de_mid_y - 4} L {de_mid_x} {de_mid_y} L {de_mid_x - 6} {de_mid_y + 4}" fill="none" stroke="#2563eb" stroke-width="2"/>',
        f'<path d="M {bc_mid_x - 6} {bc_mid_y - 4} L {bc_mid_x} {bc_mid_y} L {bc_mid_x - 6} {bc_mid_y + 4}" fill="none" stroke="#1e293b" stroke-width="2"/>',
        # Vertex labels
        f'<text x="{a_pt[0]}" y="{a_pt[1] - 8}" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">{labels[0]}</text>',
        f'<text x="{b_pt[0] - 12}" y="{b_pt[1] + 14}" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">{labels[1]}</text>',
        f'<text x="{c_pt[0] + 12}" y="{c_pt[1] + 14}" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">{labels[2]}</text>',
        f'<text x="{d_x - 14}" y="{d_y + 4}" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">{labels[3]}</text>',
        f'<text x="{e_x + 14}" y="{e_y + 4}" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">{labels[4]}</text>',
    ]
    if side_texts:
        for st in side_texts:
            elements.append(
                f'<text x="{st["x"]}" y="{st["y"]}" font-family="sans-serif" font-size="12" fill="{st.get("color", "#475569")}">{st["text"]}</text>'
            )
    return _svg_wrap("".join(elements), width=360, height=250)


# --------------------------------------------------------------------------- #
# Archetype Builders 01 to 25
# --------------------------------------------------------------------------- #

def build_01_ratio_simplification_and_fraction(rng: random.Random) -> Dict[str, Any]:
    common = rng.randint(4, 9)
    coprime_pairs = [(3, 4), (3, 5), (3, 7), (5, 6), (5, 8), (7, 8), (7, 9)]
    m, n = rng.choice(coprime_pairs)
    num = m * common
    den = n * common

    prompt = (
        f"In geometric calculations, ratios of side lengths must be expressed in simplest fractional form. "
        f"Simplify the ratio of two line segments measuring ${num}\\text{{ cm}}$ to ${den}\\text{{ cm}}$. "
        f"Give your answer in the form $\\frac{{a}}{{b}}$."
    )
    ans_latex = f"\\frac{{{m}}}{{{n}}}"
    sample = (
        f"\\text{{Ratio}} = \\frac{{{num}}}{{{den}}} "
        f"= \\frac{{{m} \\times {common}}}{{{n} \\times {common}}} "
        f"= \\frac{{{m}}}{{{n}}}."
    )

    svg = _svg_wrap(
        f'<line x1="40" y1="80" x2="{40 + m * 20}" y2="80" stroke="#2563eb" stroke-width="4"/>'
        f'<text x="25" y="85" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">A</text>'
        f'<text x="{45 + m * 20}" y="85" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">B ({num} cm)</text>'
        f'<line x1="40" y1="150" x2="{40 + n * 20}" y2="150" stroke="#059669" stroke-width="4"/>'
        f'<text x="25" y="155" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">C</text>'
        f'<text x="{45 + n * 20}" y="155" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">D ({den} cm)</text>',
        width=360,
        height=220,
    )

    return {
        "id": "g12_eg_01",
        "topic": "Euclidean geometry",
        "subskill": "01_ratio_simplification_and_fraction",
        "question_text": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"{m}/{n}",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Line segments AB and CD"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Divide numerator and denominator by HCF = {common}", "marks": 1},
                {"id": "mp2", "desc": f"Simplest fraction form {m}/{n}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Find the highest common factor of both numbers and divide.",
            "2_concept": f"Both {num} and {den} are divisible by {common}.",
            "3_breakdown": f"{num} / {den} = ({m} * {common}) / ({n} * {common}) = {m}/{n}.",
        },
        "misconception_tags": ["inversion_of_ratio", "unsimplified_fraction"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_02_proportion_extremes_and_means(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(7, 11)
    k = rng.randint(2, 5)
    c = a * k
    d = b * k

    prompt = (
        f"In proportion theory, if four lengths satisfy $\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{x}}$, "
        f"the product of the extremes equals the product of the means ($ad = bc$). "
        f"Solve for $x$ in simplest exact form."
    )
    sample = (
        f"\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{x}} \\implies "
        f"{a}x = {b} \\times {c} \\implies "
        f"{a}x = {b * c} \\implies "
        f"x = \\frac{{{b * c}}}{{{a}}} = {d}."
    )
    svg = _svg_wrap(
        f'<rect x="40" y="40" width="120" height="60" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="100" y="75" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#1e40af">{a} / {b}</text>'
        f'<text x="180" y="75" text-anchor="middle" font-family="sans-serif" font-size="18" fill="#0f172a">=</text>'
        f'<rect x="200" y="40" width="120" height="60" fill="#f0fdf4" stroke="#059669" stroke-width="2"/>'
        f'<text x="260" y="75" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#065f46">{c} / x</text>',
        width=360,
        height=140,
    )
    return {
        "id": "g12_eg_02",
        "topic": "Euclidean geometry",
        "subskill": "02_proportion_extremes_and_means",
        "question_text": prompt,
        "answer_latex": str(d),
        "answer_sympy": str(d),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Proportion equality"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Cross-multiplication {a}*x = {b}*{c}", "marks": 1},
                {"id": "mp2", "desc": f"Solution x = {d}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Cross-multiply: a * x = b * c.",
            "2_concept": f"{a} * x = {b} * {c} = {b * c}.",
            "3_breakdown": f"x = {b * c} / {a} = {d}.",
        },
        "misconception_tags": ["cross_multiplication_error", "algebraic_sign_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_03_proportion_transformations(rng: random.Random) -> Dict[str, Any]:
    p = rng.randint(3, 7)
    q = rng.randint(2, 5)
    sum_val = p + q

    prompt = (
        f"Given the true proportion $\\frac{{a}}{{b}} = \\frac{{{p}}}{{{q}}}$, "
        f"apply the component property $\\frac{{a + b}}{{b}} = \\frac{{c + d}}{{d}}$ "
        f"to find the exact numerical value of the ratio $\\frac{{a + b}}{{b}}$ as a common fraction."
    )
    ans_latex = f"\\frac{{{sum_val}}}{{{q}}}"
    sample = (
        f"\\frac{{a + b}}{{b}} = \\frac{{a}}{{b}} + 1 = \\frac{{{p}}}{{{q}}} + 1 "
        f"= \\frac{{{p} + {q}}}{{{q}}} = \\frac{{{sum_val}}}{{{q}}}."
    )
    svg = _svg_wrap(
        f'<line x1="50" y1="80" x2="290" y2="80" stroke="#1e293b" stroke-width="3"/>'
        f'<circle cx="50" cy="80" r="4" fill="#2563eb"/>'
        f'<circle cx="210" cy="80" r="4" fill="#dc2626"/>'
        f'<circle cx="290" cy="80" r="4" fill="#059669"/>'
        f'<text x="130" y="70" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">a ({p} parts)</text>'
        f'<text x="250" y="70" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#059669">b ({q} parts)</text>'
        f'<text x="170" y="115" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#1e293b">Total a + b = {sum_val} parts</text>',
        width=360,
        height=150,
    )
    return {
        "id": "g12_eg_03",
        "topic": "Euclidean geometry",
        "subskill": "03_proportion_transformations",
        "question_text": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"{sum_val}/{q}",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Segment proportion addition"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Apply transformation (a+b)/b = a/b + 1", "marks": 1},
                {"id": "mp2", "desc": f"Result {sum_val}/{q}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Rewrite (a + b)/b as a/b + b/b.",
            "2_concept": f"Substitute a/b = {p}/{q} and add 1.",
            "3_breakdown": f"({p}/{q}) + 1 = ({p} + {q})/{q} = {sum_val}/{q}.",
        },
        "misconception_tags": ["fraction_addition_error", "misapplied_proportion_rule"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_04_ratio_of_triangle_areas_equal_altitudes(rng: random.Random) -> Dict[str, Any]:
    bd = rng.randint(3, 7)
    dc = rng.randint(4, 9)
    g = math.gcd(bd, dc)
    s_bd = bd // g
    s_dc = dc // g

    prompt = (
        f"In $\\triangle ABC$, point $D$ lies on side $BC$ such that $BD = {bd}\\text{{ cm}}$ and "
        f"$DC = {dc}\\text{{ cm}}$. The two triangles $\\triangle ABD$ and $\\triangle ADC$ share "
        f"the common vertex $A$ and therefore have equal perpendicular heights ($h$). "
        f"Calculate the ratio $\\frac{{\\text{{Area}}(\\triangle ABD)}}{{\\text{{Area}}(\\triangle ADC)}}$ "
        f"in simplest fractional form."
    )
    ans_latex = f"\\frac{{{s_bd}}}{{{s_dc}}}"
    sample = (
        f"\\text{{Triangles }} \\triangle ABD \\text{{ and }} \\triangle ADC \\text{{ have a common vertex }} A "
        f"\\text{{ and share the same perpendicular altitude from }} A \\text{{ to line }} BC.\\\\\n"
        f"\\frac{{\\text{{Area}}(\\triangle ABD)}}{{\\text{{Area}}(\\triangle ADC)}} = \\frac{{BD}}{{DC}} "
        f"= \\frac{{{bd}}}{{{dc}}} = \\frac{{{s_bd}}}{{{s_dc}}} \\quad (\\text{{equal altitudes}})."
    )
    # Draw triangle ABC with line AD
    d_x = int(60 + (bd / (bd + dc)) * 240)
    svg = _svg_wrap(
        f'<polygon points="180,30 60,210 300,210" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="180" y1="30" x2="{d_x}" y2="210" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="180" y="22" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">A</text>'
        f'<text x="50" y="225" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">B</text>'
        f'<text x="310" y="225" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">C</text>'
        f'<text x="{d_x}" y="228" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#dc2626">D</text>'
        f'<text x="{(60 + d_x) // 2}" y="200" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">{bd} cm</text>'
        f'<text x="{(300 + d_x) // 2}" y="200" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#059669">{dc} cm</text>',
        width=360,
        height=250,
    )
    return {
        "id": "g12_eg_04",
        "topic": "Euclidean geometry",
        "subskill": "04_ratio_of_triangle_areas_equal_altitudes",
        "question_text": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"{s_bd}/{s_dc}",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Triangles with equal altitudes"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "State ratio of areas equals ratio of bases (BD/DC)", "marks": 1},
                {"id": "mp2", "desc": f"Simplify fraction to {s_bd}/{s_dc}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Triangles sharing a vertex on a common straight base line have the same height.",
            "2_concept": "Area ratio = base1 / base2 = BD / DC.",
            "3_breakdown": f"Ratio = {bd}/{dc} = {s_bd}/{s_dc}.",
        },
        "misconception_tags": ["squaring_ratio_when_not_similar", "altitude_confusion"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_05_ratio_of_triangle_areas_equal_bases(rng: random.Random) -> Dict[str, Any]:
    area_pqr = rng.randint(24, 60)
    prompt = (
        f"In the geometric configuration, lines $L_1$ and $L_2$ are parallel. "
        f"Triangles $\\triangle PQR$ and $\\triangle SQR$ both lie on the same base $QR$, "
        f"and their third vertices $P$ and $S$ lie on the parallel line $L_1$. "
        f"If the area of $\\triangle PQR = {area_pqr}\\text{{ cm}}^2$, determine the area of $\\triangle SQR$."
    )
    sample = (
        f"\\text{{Triangles }} \\triangle PQR \\text{{ and }} \\triangle SQR \\text{{ are on the same base }} QR "
        f"\\text{{ and between the same parallel lines }} (L_1 \\parallel QR).\\\\\n"
        f"\\text{{Therefore, their perpendicular heights are equal: }} "
        f"\\text{{Area}}(\\triangle SQR) = \\text{{Area}}(\\triangle PQR) = {area_pqr}\\text{{ cm}}^2."
    )
    svg = _svg_wrap(
        f'<line x1="30" y1="50" x2="330" y2="50" stroke="#94a3b8" stroke-dasharray="4" stroke-width="2"/>'
        f'<line x1="30" y1="190" x2="330" y2="190" stroke="#94a3b8" stroke-dasharray="4" stroke-width="2"/>'
        f'<polygon points="90,50 110,190 250,190" fill="rgba(37,99,235,0.15)" stroke="#2563eb" stroke-width="2"/>'
        f'<polygon points="230,50 110,190 250,190" fill="rgba(220,38,38,0.15)" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="90" y="40" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#2563eb">P</text>'
        f'<text x="230" y="40" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#dc2626">S</text>'
        f'<text x="100" y="210" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">Q</text>'
        f'<text x="260" y="210" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">R</text>'
        f'<text x="320" y="45" font-family="sans-serif" font-size="12" fill="#64748b">L1</text>'
        f'<text x="320" y="185" font-family="sans-serif" font-size="12" fill="#64748b">L2</text>'
        f'<text x="180" y="130" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#2563eb">Area(PQR) = {area_pqr} cm²</text>',
        width=360,
        height=230,
    )
    return {
        "id": "g12_eg_05",
        "topic": "Euclidean geometry",
        "subskill": "05_ratio_of_triangle_areas_equal_bases",
        "question_text": prompt,
        "answer_latex": str(area_pqr),
        "answer_sympy": str(area_pqr),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Triangles on same base between parallels (Area = {area_pqr})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "State reason: same base QR and between same parallel lines", "marks": 1},
                {"id": "mp2", "desc": f"Area = {area_pqr}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Check the base and the distance between the parallel lines.",
            "2_concept": "Triangles on the same base between parallel lines have equal area.",
            "3_breakdown": f"Area(SQR) = Area(PQR) = {area_pqr}.",
        },
        "misconception_tags": ["parallel_distance_misunderstanding", "assumed_different_areas"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_06_compound_area_ratios_nested_triangles(rng: random.Random) -> Dict[str, Any]:
    jm = rng.randint(2, 4)
    mk = rng.randint(3, 5)
    jn = rng.randint(2, 4)
    nl = rng.randint(3, 6)

    jk = jm + mk
    jl = jn + nl

    # Area(JMN)/Area(JKL) = (JM/JK) * (JN/JL)
    num = jm * jn
    den = jk * jl
    g = math.gcd(num, den)
    s_num = num // g
    s_den = den // g

    prompt = (
        f"In $\\triangle JKL$, point $M$ lies on $JK$ with $JM = {jm}$ and $MK = {mk}$. "
        f"Point $N$ lies on $JL$ with $JN = {jn}$ and $NL = {nl}$. "
        f"Calculate the ratio of the area of $\\triangle JMN$ to the area of $\\triangle JKL$ "
        f"in simplest fractional form $\\frac{{a}}{{b}}$."
    )
    sample = (
        f"\\frac{{\\text{{Area}}(\\triangle JMN)}}{{\\text{{Area}}(\\triangle JML)}} = \\frac{{JN}}{{JL}} = \\frac{{{jn}}}{{{jl}}}\\\\\n"
        f"\\frac{{\\text{{Area}}(\\triangle JML)}}{{\\text{{Area}}(\\triangle JKL)}} = \\frac{{JM}}{{JK}} = \\frac{{{jm}}}{{{jk}}}\\\\\n"
        f"\\frac{{\\text{{Area}}(\\triangle JMN)}}{{\\text{{Area}}(\\triangle JKL)}} = "
        f"\\left(\\frac{{{jn}}}{{{jl}}}\\right) \\times \\left(\\frac{{{jm}}}{{{jk}}}\\right) "
        f"= \\frac{{{num}}}{{{den}}} = \\frac{{{s_num}}}{{{s_den}}}."
    )
    svg = _svg_wrap(
        f'<polygon points="180,30 50,220 310,220" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<polygon points="180,30 115,125 245,125" fill="rgba(37,99,235,0.2)" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="180" y="22" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">J</text>'
        f'<text x="40" y="235" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">K</text>'
        f'<text x="320" y="235" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">L</text>'
        f'<text x="100" y="125" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">M</text>'
        f'<text x="260" y="125" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">N</text>',
        width=360,
        height=250,
    )
    return {
        "id": "g12_eg_06",
        "topic": "Euclidean geometry",
        "subskill": "06_compound_area_ratios_nested_triangles",
        "question_text": prompt,
        "answer_latex": f"\\frac{{{s_num}}}{{{s_den}}}",
        "answer_sympy": f"{s_num}/{s_den}",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Nested triangle area ratios (JM={jm}, JN={jn})"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Ratio JN/JL = {jn}/{jl}", "marks": 1},
                {"id": "mp2", "desc": f"Ratio JM/JK = {jm}/{jk}", "marks": 1},
                {"id": "mp3", "desc": f"Compound product {s_num}/{s_den}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Express both intermediate area ratios through the common triangle JML.",
            "2_concept": "Area(JMN)/Area(JKL) = (JM/JK) * (JN/JL).",
            "3_breakdown": f"({jm}/{jk}) * ({jn}/{jl}) = {num}/{den} = {s_num}/{s_den}.",
        },
        "misconception_tags": ["linear_sum_instead_of_product", "misidentified_whole_side_length"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 4,
    }


def build_07_proportionality_theorem_single_parallel_side(rng: random.Random) -> Dict[str, Any]:
    ad = rng.randint(3, 8)
    db = rng.randint(4, 9)
    ae = rng.randint(3, 7) * 2
    # ad / db = ae / ec  => ec = (db * ae) / ad
    # choose nice integers
    factor = rng.choice([2, 3, 4])
    ad = factor * rng.randint(2, 4)
    db = factor * rng.randint(3, 5)
    k = rng.randint(2, 5)
    ae = ad * k // factor
    ec = db * k // factor

    prompt = (
        f"In $\\triangle ABC$, point $D$ lies on $AB$ and point $E$ lies on $AC$ such that "
        f"$DE \\parallel BC$. You are given $AD = {ad}\\text{{ cm}}$, $DB = {db}\\text{{ cm}}$, "
        f"and $AE = {ae}\\text{{ cm}}$. "
        f"Apply the proportionality theorem to calculate the length of $EC$."
    )
    sample = (
        f"\\text{{In }} \\triangle ABC, DE \\parallel BC \\implies "
        f"\\frac{{AD}}{{DB}} = \\frac{{AE}}{{EC}} \\quad (\\text{{line }} \\parallel \\text{{ one side of }} \\triangle)\\\\\n"
        f"\\frac{{{ad}}}{{{db}}} = \\frac{{{ae}}}{{EC}}\\\\\n"
        f"EC = \\frac{{{db} \\times {ae}}}{{{ad}}} = {ec}\\text{{ cm}}."
    )
    side_texts = [
        {"x": 90, "y": 95, "text": f"{ad}"},
        {"x": 65, "y": 175, "text": f"{db}"},
        {"x": 235, "y": 95, "text": f"{ae}"},
        {"x": 265, "y": 175, "text": "EC = x", "color": "#dc2626"},
    ]
    svg = _draw_triangle_parallel_svg(labels=("A", "B", "C", "D", "E"), side_texts=side_texts)

    return {
        "id": "g12_eg_07",
        "topic": "Euclidean geometry",
        "subskill": "07_proportionality_theorem_single_parallel_side",
        "question_text": prompt,
        "answer_latex": str(ec),
        "answer_sympy": str(ec),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Triangle with DE || BC"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Correct theorem ratio AD/DB = AE/EC with reason", "marks": 1},
                {"id": "mp2", "desc": f"Correct value EC = {ec}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "A line parallel to one side of a triangle divides the other two sides proportionally.",
            "2_concept": "AD / DB = AE / EC with reason (line || to one side of triangle).",
            "3_breakdown": f"EC = ({db} * {ae}) / {ad} = {ec}.",
        },
        "misconception_tags": ["inverting_proportionality_ratio", "omitted_geometric_reason"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_08_proportionality_theorem_segment_sum_relation(rng: random.Random) -> Dict[str, Any]:
    # In triangle PQR, ST || QR. PQ is given total, PR is given total, QS is given. Find PT.
    # S on PQ, T on PR.
    # PS = PQ - QS.
    # PT / PR = PS / PQ.
    pq = rng.choice([28, 35, 42, 49])
    qs = rng.choice([12, 14, 18, 21])
    while qs >= pq:
        qs = pq // 2
    ps = pq - qs
    pr = rng.choice([20, 25, 30, 35])
    # pt = pr * ps / pq
    g = math.gcd(ps * pr, pq)
    pt_num = (ps * pr) // g
    pt_den = pq // g
    if pt_den == 1:
        ans_sympy = str(pt_num)
        ans_latex = str(pt_num)
    else:
        ans_sympy = f"{pt_num}/{pt_den}"
        ans_latex = f"\\frac{{{pt_num}}}{{{pt_den}}}"

    prompt = (
        f"In $\\triangle PQR$, $ST \\parallel QR$ with point $S$ on $PQ$ and point $T$ on $PR$. "
        f"You are given $PQ = {pq}\\text{{ mm}}$, $PR = {pr}\\text{{ mm}}$, and $QS = {qs}\\text{{ mm}}$. "
        f"Calculate the length of segment $PT$."
    )
    sample = (
        f"PS = PQ - QS = {pq} - {qs} = {ps}\\text{{ mm}}.\\\\\n"
        f"\\text{{In }} \\triangle PQR, ST \\parallel QR \\implies "
        f"\\frac{{PT}}{{PR}} = \\frac{{PS}}{{PQ}} \\quad (\\text{{prop theorem, }} ST \\parallel QR)\\\\\n"
        f"PT = \\frac{{{ps} \\times {pr}}}{{{pq}}} = {ans_latex}\\text{{ mm}}."
    )
    side_texts = [
        {"x": 70, "y": 140, "text": f"PQ = {pq}"},
        {"x": 70, "y": 180, "text": f"QS = {qs}"},
        {"x": 230, "y": 140, "text": f"PR = {pr}"},
        {"x": 230, "y": 100, "text": "PT = ?"},
    ]
    svg = _draw_triangle_parallel_svg(labels=("P", "Q", "R", "S", "T"), side_texts=side_texts)

    return {
        "id": "g12_eg_08",
        "topic": "Euclidean geometry",
        "subskill": "08_proportionality_theorem_segment_sum_relation",
        "question_text": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": ans_sympy,
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Triangle PQR with ST || QR"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculate PS = {ps}", "marks": 1},
                {"id": "mp2", "desc": "State ratio PT/PR = PS/PQ with reason", "marks": 1},
                {"id": "mp3", "desc": f"Answer PT = {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "First find PS by subtracting QS from the whole side PQ.",
            "2_concept": "PT / PR = PS / PQ because ST || QR.",
            "3_breakdown": f"PS = {pq} - {qs} = {ps}. Then PT = ({ps} * {pr}) / {pq} = {ans_latex}.",
        },
        "misconception_tags": ["using_subsegment_instead_of_whole_side", "subtraction_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_09_proportionality_theorem_algebraic_linear(rng: random.Random) -> Dict[str, Any]:
    # AD = x, DB = x + 3
    # AE = 4, EC = 6
    # x / (x+3) = 4 / 6 => 6x = 4x + 12 => 2x = 12 => x = 6
    ae = rng.choice([2, 3, 4])
    ec = ae + rng.choice([1, 2, 3])
    # x / (x + c) = ae / ec => ec * x = ae * x + ae * c => (ec - ae) * x = ae * c
    diff = ec - ae
    c = diff * rng.randint(2, 5)
    x_val = (ae * c) // diff

    prompt = (
        f"In $\\triangle ABC$, line segment $DE$ is drawn parallel to base $BC$ with $D$ on $AB$ and $E$ on $AC$. "
        f"The lengths of the segments are given as $AD = x$, $DB = x + {c}$, $AE = {ae}$, and $EC = {ec}$. "
        f"Solve for the unknown value $x$."
    )
    sample = (
        f"\\text{{Since }} DE \\parallel BC, \\frac{{AD}}{{DB}} = \\frac{{AE}}{{EC}} \\quad (\\text{{prop theorem, }} DE \\parallel BC)\\\\\n"
        f"\\frac{{x}}{{x + {c}}} = \\frac{{{ae}}}{{{ec}}}\\\\\n"
        f"{ec}x = {ae}(x + {c})\\\\\n"
        f"{ec}x = {ae}x + {ae * c}\\\\\n"
        f"{ec - ae}x = {ae * c} \\implies x = {x_val}."
    )
    side_texts = [
        {"x": 90, "y": 95, "text": "x"},
        {"x": 65, "y": 175, "text": f"x + {c}"},
        {"x": 235, "y": 95, "text": f"{ae}"},
        {"x": 265, "y": 175, "text": f"{ec}"},
    ]
    svg = _draw_triangle_parallel_svg(labels=("A", "B", "C", "D", "E"), side_texts=side_texts)

    return {
        "id": "g12_eg_09",
        "topic": "Euclidean geometry",
        "subskill": "09_proportionality_theorem_algebraic_linear",
        "question_text": prompt,
        "answer_latex": str(x_val),
        "answer_sympy": str(x_val),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Algebraic proportionality DE || BC"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Set up equation x / (x + c) = ae / ec", "marks": 1},
                {"id": "mp2", "desc": "Expand and simplify linear equation", "marks": 1},
                {"id": "mp3", "desc": f"Solve x = {x_val}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Set up the ratio AD/DB = AE/EC and cross-multiply.",
            "2_concept": f"{ec} * x = {ae} * (x + {c}).",
            "3_breakdown": f"{ec - ae}x = {ae * c} -> x = {x_val}.",
        },
        "misconception_tags": ["distributive_property_error", "algebraic_cross_multiplication_failure"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 4,
    }


def build_10_proportionality_theorem_algebraic_quadratic(rng: random.Random) -> Dict[str, Any]:
    # x / (x + a) = (x - b) / c or similar
    # Let x = positive integer. E.g. AD = x, DB = x - 2, AE = x + 3, EC = x - 1
    # x(x - 1) = (x + 3)(x - 2) => x^2 - x = x^2 + x - 6 => 2x = 6 => x = 3
    # Let's create quadratic that factors:
    # AD = x, DB = 2, AE = 6, EC = x - 1
    # x / 2 = 6 / (x - 1) => x(x - 1) = 12 => x^2 - x - 12 = 0 => (x - 4)(x + 3) = 0 => x = 4
    x_val = rng.randint(4, 7)
    db = rng.randint(2, 4)
    # x * (x - 1) = db * ae => choose ae = x*(x-1)//db
    diff = rng.choice([1, 2])
    prod = x_val * (x_val - diff)
    db = rng.choice([2, 3])
    while prod % db != 0:
        db = 2 if prod % 2 == 0 else 3
    ae = prod // db

    prompt = (
        f"In $\\triangle PQR$, segment $MN \\parallel QR$ ($M$ on $PQ$, $N$ on $PR$). "
        f"Given $PM = x$, $MQ = {db}$, $PN = {ae}$, and $NR = x - {diff}$, "
        f"solve for the valid geometric side length $x$ ($x > {diff}$)."
    )
    sample = (
        f"\\text{{Since }} MN \\parallel QR, \\frac{{PM}}{{MQ}} = \\frac{{PN}}{{NR}} \\quad (\\text{{prop theorem, }} MN \\parallel QR)\\\\\n"
        f"\\frac{{x}}{{{db}}} = \\frac{{{ae}}}{{x - {diff}}}\\\\\n"
        f"x(x - {diff}) = {db} \\times {ae} = {prod}\\\\\n"
        f"x^2 - {diff}x - {prod} = 0\\\\\n"
        f"(x - {x_val})(x + {x_val - diff}) = 0\\\\\n"
        f"\\text{{Since side length }} x > {diff}, x = {x_val}."
    )
    side_texts = [
        {"x": 90, "y": 95, "text": "x"},
        {"x": 65, "y": 175, "text": f"{db}"},
        {"x": 235, "y": 95, "text": f"{ae}"},
        {"x": 265, "y": 175, "text": f"x - {diff}"},
    ]
    svg = _draw_triangle_parallel_svg(labels=("P", "Q", "R", "M", "N"), side_texts=side_texts)

    return {
        "id": "g12_eg_10",
        "topic": "Euclidean geometry",
        "subskill": "10_proportionality_theorem_algebraic_quadratic",
        "question_text": prompt,
        "answer_latex": str(x_val),
        "answer_sympy": str(x_val),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Quadratic proportionality equation"},
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Equate ratios PM/MQ = PN/NR with geometric reason", "marks": 1},
                {"id": "mp2", "desc": f"Standard quadratic form x^2 - {diff}x - {prod} = 0", "marks": 1},
                {"id": "mp3", "desc": "Factorise quadratic equation", "marks": 1},
                {"id": "mp4", "desc": f"Select positive root x = {x_val}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Cross-multiply PM * NR = MQ * PN to form a quadratic equation.",
            "2_concept": f"x^2 - {diff}x - {prod} = 0. Factorise to find roots.",
            "3_breakdown": f"(x - {x_val})(x + {x_val - diff}) = 0. Length cannot be negative, so x = {x_val}.",
        },
        "misconception_tags": ["keeping_negative_root_for_length", "quadratic_factorisation_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 5,
    }


def build_11_proportionality_theorem_converse_test(rng: random.Random) -> Dict[str, Any]:
    # Determine whether ST || QR
    is_parallel = rng.choice([True, False])
    k = rng.randint(2, 4)
    ps = rng.randint(3, 6)
    sq = rng.randint(4, 8)
    if is_parallel:
        pt = ps * k
        tr = sq * k
        ans_str = "Parallel"
    else:
        pt = ps * k
        tr = sq * k + rng.choice([1, 2, -1])
        ans_str = "Not parallel"

    prompt = (
        f"In $\\triangle PQR$, point $S$ lies on $PQ$ and point $T$ lies on $PR$. "
        f"The measured lengths are $PS = {ps}\\text{{ mm}}$, $SQ = {sq}\\text{{ mm}}$, "
        f"$PT = {pt}\\text{{ mm}}$, and $TR = {tr}\\text{{ mm}}$. "
        f"Determine whether line segment $ST$ is parallel to side $QR$. "
        f"(Enter 'Parallel' or 'Not parallel')."
    )
    r1 = f"{ps}/{sq}"
    r2 = f"{pt}/{tr}"
    sample = (
        f"\\frac{{PS}}{{SQ}} = \\frac{{{ps}}}{{{sq}}}\\\\\n"
        f"\\frac{{PT}}{{TR}} = \\frac{{{pt}}}{{{tr}}}\\\\\n"
        f"\\text{{Since }} \\frac{{PS}}{{SQ}} {'=' if is_parallel else '\\neq'} \\frac{{PT}}{{TR}}, "
        f"ST \\text{{ is }} {'\\parallel QR \\quad (\\text{{converse prop theorem}})' if is_parallel else '\\text{{not parallel to }} QR'}."
    )
    side_texts = [
        {"x": 90, "y": 95, "text": f"{ps}"},
        {"x": 65, "y": 175, "text": f"{sq}"},
        {"x": 235, "y": 95, "text": f"{pt}"},
        {"x": 265, "y": 175, "text": f"{tr}"},
    ]
    svg = _draw_triangle_parallel_svg(labels=("P", "Q", "R", "S", "T"), side_texts=side_texts)

    return {
        "id": "g12_eg_11",
        "topic": "Euclidean geometry",
        "subskill": "11_proportionality_theorem_converse_test",
        "question_text": prompt,
        "answer_latex": f"\\text{{{ans_str}}}",
        "answer_sympy": f"'{ans_str}'",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Converse proportionality test"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculate and compare ratios PS/SQ and PT/TR", "marks": 1},
                {"id": "mp2", "desc": f"Correct conclusion: {ans_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Calculate PS/SQ and PT/TR as simplified fractions.",
            "2_concept": "If PS/SQ = PT/TR, then ST is parallel to QR (converse of proportionality theorem).",
            "3_breakdown": f"PS/SQ = {ps}/{sq} and PT/TR = {pt}/{tr}. Compare these two ratios.",
        },
        "misconception_tags": ["ratio_comparison_failure", "confusing_theorem_with_converse"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_12_proportionality_theorem_multiple_parallels(rng: random.Random) -> Dict[str, Any]:
    # Three parallel lines L1 || L2 || L3 intersecting transversals AB and CD
    # AE / EB = CF / FD
    ae = rng.randint(3, 6)
    eb = rng.randint(4, 8)
    factor = rng.randint(2, 4)
    cf = ae * factor
    fd = eb * factor

    prompt = (
        f"Three parallel lines cut two transversals at points $A, E, B$ and $C, F, D$ respectively. "
        f"Given $AE = {ae}$, $EB = {eb}$, and $CF = {cf}$, calculate the length of segment $FD$."
    )
    sample = (
        f"\\text{{Since parallel lines divide transversals proportionally: }}\\\\\n"
        f"\\frac{{AE}}{{EB}} = \\frac{{CF}}{{FD}}\\\\\n"
        f"\\frac{{{ae}}}{{{eb}}} = \\frac{{{cf}}}{{FD}} \\implies "
        f"FD = \\frac{{{eb} \\times {cf}}}{{{ae}}} = {fd}."
    )
    svg = _svg_wrap(
        f'<line x1="30" y1="50" x2="330" y2="50" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="30" y1="120" x2="330" y2="120" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="30" y1="190" x2="330" y2="190" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="80" y1="30" x2="120" y2="210" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="280" y1="30" x2="240" y2="210" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="75" y="45" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">A</text>'
        f'<text x="95" y="115" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">E</text>'
        f'<text x="125" y="205" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">B</text>'
        f'<text x="285" y="45" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">C</text>'
        f'<text x="265" y="115" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">F</text>'
        f'<text x="235" y="205" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">D</text>'
        f'<text x="70" y="85" font-family="sans-serif" font-size="12" fill="#2563eb">{ae}</text>'
        f'<text x="85" y="160" font-family="sans-serif" font-size="12" fill="#2563eb">{eb}</text>'
        f'<text x="285" y="85" font-family="sans-serif" font-size="12" fill="#059669">{cf}</text>'
        f'<text x="265" y="160" font-family="sans-serif" font-size="12" fill="#dc2626">FD = ?</text>',
        width=360,
        height=230,
    )
    return {
        "id": "g12_eg_12",
        "topic": "Euclidean geometry",
        "subskill": "12_proportionality_theorem_multiple_parallels",
        "question_text": prompt,
        "answer_latex": str(fd),
        "answer_sympy": str(fd),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Three parallel lines cutting transversals"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "State ratio AE/EB = CF/FD", "marks": 1},
                {"id": "mp2", "desc": f"Calculate FD = {fd}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Three parallel lines divide any two transversals in the same proportion.",
            "2_concept": "AE / EB = CF / FD.",
            "3_breakdown": f"FD = ({eb} * {cf}) / {ae} = {fd}.",
        },
        "misconception_tags": ["transversal_ratio_inversion", "unaligned_subsegments"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_13_proportionality_theorem_nested_parallels(rng: random.Random) -> Dict[str, Any]:
    # In triangle PQR: ST || QU, and SQ || TU
    # PT = 30, TR = 20. Find UR if QR is known or find ratio.
    # In triangle PQU: ST || QU => PS/SQ = PT/TU
    # In triangle PQR: SQ || TU or similar
    # Let PT = 30, TR = 20.
    pt = rng.choice([24, 30, 36])
    tr = rng.choice([16, 20, 24])
    # ratio = pt / tr = 3/2
    factor = pt // math.gcd(pt, tr)
    den_f = tr // math.gcd(pt, tr)
    ur = rng.randint(8, 15)
    qu = (ur * factor) // den_f

    prompt = (
        f"In $\\triangle PQR$, point $S$ lies on $PQ$, point $U$ lies on $QR$, and point $T$ lies on $PR$. "
        f"Lines are drawn such that $ST \\parallel QU$. "
        f"Given $PT = {pt}$, $TR = {tr}$, and segment $UR = {ur}$, "
        f"if the same proportion applies across $QR$, calculate $QU$."
    )
    sample = (
        f"\\text{{Applying the proportionality theorem with }} ST \\parallel QU:\\\\\n"
        f"\\frac{{QU}}{{UR}} = \\frac{{PT}}{{TR}} = \\frac{{{pt}}}{{{tr}}} = \\frac{{{factor}}}{{{den_f}}}\\\\\n"
        f"QU = \\frac{{{factor}}}{{{den_f}}} \\times {ur} = {qu}."
    )
    svg = _svg_wrap(
        f'<polygon points="180,30 50,220 310,220" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="110" y1="130" x2="240" y2="130" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="180" y="22" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">P</text>'
        f'<text x="40" y="235" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">Q</text>'
        f'<text x="320" y="235" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">R</text>'
        f'<text x="95" y="130" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">S</text>'
        f'<text x="255" y="130" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">T</text>'
        f'<text x="210" y="235" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#059669">U</text>',
        width=360,
        height=250,
    )
    return {
        "id": "g12_eg_13",
        "topic": "Euclidean geometry",
        "subskill": "13_proportionality_theorem_nested_parallels",
        "question_text": prompt,
        "answer_latex": str(qu),
        "answer_sympy": str(qu),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Triangle with nested parallel segments (PT={pt}, TR={tr})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Ratio QU/UR = PT/TR = {factor}/{den_f}", "marks": 1},
                {"id": "mp2", "desc": f"Calculate QU = {qu}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Relate QU/UR to the known segment ratio PT/TR.",
            "2_concept": f"QU / UR = {pt} / {tr}.",
            "3_breakdown": f"QU = ({factor}/{den_f}) * {ur} = {qu}.",
        },
        "misconception_tags": ["ratio_transitivity_error", "misaligned_transversal_segments"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_14_midpoint_theorem_as_proportionality_special_case(rng: random.Random) -> Dict[str, Any]:
    base_len = rng.choice([16, 24, 32, 40, 48])
    pq_len = base_len // 2
    b_val = rng.randint(2, 6)
    b_expr = pq_len - b_val

    prompt = (
        f"In $\\triangle JOB$, point $P$ is the midpoint of $JO$ and point $Q$ is the midpoint of $OB$. "
        f"By the midpoint theorem (a special case of the proportionality theorem with ratio $1:1$), "
        f"$PQ \\parallel JB$ and $PQ = \\frac{{1}}{{2}}JB$. "
        f"If $JB = {base_len}\\text{{ cm}}$ and $PQ$ is represented by the expression $b + {b_val}$, "
        f"find the numerical value of $b$."
    )
    sample = (
        f"\\text{{By the midpoint theorem, }} PQ = \\frac{{1}}{{2}}JB = \\frac{{1}}{{2}}({base_len}) = {pq_len}\\text{{ cm}}.\\\\\n"
        f"b + {b_val} = {pq_len} \\implies b = {pq_len} - {b_val} = {b_expr}."
    )
    svg = _svg_wrap(
        f'<polygon points="180,30 50,220 310,220" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="115" y1="125" x2="245" y2="125" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="180" y="22" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">O</text>'
        f'<text x="40" y="235" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">J</text>'
        f'<text x="320" y="235" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">B</text>'
        f'<text x="100" y="125" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">P</text>'
        f'<text x="260" y="125" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">Q</text>'
        f'<text x="180" y="115" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">b + {b_val}</text>'
        f'<text x="180" y="240" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#1e293b">JB = {base_len}</text>',
        width=360,
        height=260,
    )
    return {
        "id": "g12_eg_14",
        "topic": "Euclidean geometry",
        "subskill": "14_midpoint_theorem_as_proportionality_special_case",
        "question_text": prompt,
        "answer_latex": str(b_expr),
        "answer_sympy": str(b_expr),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Midpoint theorem segment calculation"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"State PQ = 1/2 * JB = {pq_len}", "marks": 1},
                {"id": "mp2", "desc": f"Solve b = {b_expr}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The segment joining the midpoints of two sides is parallel to the third side and half its length.",
            "2_concept": f"PQ = JB / 2 = {base_len} / 2 = {pq_len}.",
            "3_breakdown": f"b + {b_val} = {pq_len} -> b = {b_expr}.",
        },
        "misconception_tags": ["doubling_instead_of_halving", "linear_equation_subtraction_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_15_proportionality_dividing_segments_ratio_algebra(rng: random.Random) -> Dict[str, Any]:
    # Ratio AP:PB = m:n. Find AP / AB
    m = rng.randint(2, 5)
    n = rng.randint(3, 7)
    tot = m + n

    prompt = (
        f"Point $P$ divides line segment $AB$ internally such that $AP : PB = {m} : {n}$. "
        f"Express the ratio $\\frac{{AP}}{{AB}}$ as a common fraction in simplest form."
    )
    sample = (
        f"\\text{{Let }} AP = {m}k \\text{{ and }} PB = {n}k.\\\\\n"
        f"AB = AP + PB = {m}k + {n}k = {tot}k.\\\\\n"
        f"\\frac{{AP}}{{AB}} = \\frac{{{m}k}}{{{tot}k}} = \\frac{{{m}}}{{{tot}}}."
    )
    svg = _svg_wrap(
        f'<line x1="50" y1="80" x2="310" y2="80" stroke="#1e293b" stroke-width="3"/>'
        f'<circle cx="50" cy="80" r="4" fill="#0f172a"/>'
        f'<circle cx="150" cy="80" r="4" fill="#2563eb"/>'
        f'<circle cx="310" cy="80" r="4" fill="#0f172a"/>'
        f'<text x="50" y="105" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">A</text>'
        f'<text x="150" y="105" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">P</text>'
        f'<text x="310" y="105" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">B</text>'
        f'<text x="100" y="70" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">{m} parts</text>'
        f'<text x="230" y="70" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#475569">{n} parts</text>',
        width=360,
        height=140,
    )
    return {
        "id": "g12_eg_15",
        "topic": "Euclidean geometry",
        "subskill": "15_proportionality_dividing_segments_ratio_algebra",
        "question_text": prompt,
        "answer_latex": f"\\frac{{{m}}}{{{tot}}}",
        "answer_sympy": f"{m}/{tot}",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Segment division ratio"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Total parts AB = {m} + {n} = {tot}", "marks": 1},
                {"id": "mp2", "desc": f"Ratio AP/AB = {m}/{tot}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The whole line segment AB consists of AP + PB.",
            "2_concept": f"Total parts = {m} + {n} = {tot}.",
            "3_breakdown": f"AP / AB = {m} / {tot}.",
        },
        "misconception_tags": ["part_to_part_instead_of_part_to_whole", "addition_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 2,
    }


def build_16_proportionality_shared_side_two_triangles(rng: random.Random) -> Dict[str, Any]:
    # Two triangles ABC and ACD sharing side AC
    # In ABC: DE || BC => AD/DB = AE/EC
    # In ACD: EF || CD => AF/FD = AE/EC
    # Therefore AD/DB = AF/FD
    ad_db_m = rng.randint(2, 4)
    ad_db_n = rng.randint(3, 5)
    af = ad_db_m * rng.randint(2, 4)
    fd = (af * ad_db_n) // ad_db_m

    prompt = (
        f"In quadrilateral $ABCD$, line segment $DE \\parallel BC$ in $\\triangle ABC$ with $E$ on $AC$, "
        f"and $EF \\parallel CD$ in $\\triangle ACD$ with $F$ on $AD$. "
        f"Both triangles share the transversal $AC$. "
        f"If $\\frac{{AE}}{{EC}} = \\frac{{{ad_db_m}}}{{{ad_db_n}}}$ and $AF = {af}\\text{{ cm}}$, "
        f"find the length of segment $FD$."
    )
    sample = (
        f"\\text{{In }} \\triangle ACD, EF \\parallel CD \\implies "
        f"\\frac{{AF}}{{FD}} = \\frac{{AE}}{{EC}} \\quad (\\text{{prop theorem, }} EF \\parallel CD)\\\\\n"
        f"\\frac{{{af}}}{{FD}} = \\frac{{{ad_db_m}}}{{{ad_db_n}}}\\\\\n"
        f"FD = \\frac{{{af} \\times {ad_db_n}}}{{{ad_db_m}}} = {fd}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<polygon points="60,180 180,30 300,180" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="180" y1="30" x2="180" y2="180" stroke="#94a3b8" stroke-dasharray="4" stroke-width="2"/>'
        f'<text x="180" y="20" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">A</text>'
        f'<text x="50" y="195" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">B</text>'
        f'<text x="180" y="200" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">C</text>'
        f'<text x="310" y="195" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">D</text>'
        f'<line x1="100" y1="130" x2="180" y2="130" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="180" y1="130" x2="260" y2="130" stroke="#059669" stroke-width="2"/>'
        f'<text x="195" y="130" font-family="sans-serif" font-size="12" fill="#2563eb">E</text>',
        width=360,
        height=240,
    )
    return {
        "id": "g12_eg_16",
        "topic": "Euclidean geometry",
        "subskill": "16_proportionality_shared_side_two_triangles",
        "question_text": prompt,
        "answer_latex": str(fd),
        "answer_sympy": str(fd),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Shared transversal proportionality (AF={af}, FD={fd})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Equate AF/FD to AE/EC = {ad_db_m}/{ad_db_n}", "marks": 1},
                {"id": "mp2", "desc": f"Calculate FD = {fd}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The ratio AE/EC links both triangles through the common side AC.",
            "2_concept": f"AF / FD = AE / EC = {ad_db_m} / {ad_db_n}.",
            "3_breakdown": f"FD = ({af} * {ad_db_n}) / {ad_db_m} = {fd}.",
        },
        "misconception_tags": ["missing_intermediate_link", "ratio_inversion"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_17_trapezium_parallel_sides_ratio(rng: random.Random) -> Dict[str, Any]:
    # In trapezium ABCD with AB || DC, a line EF is parallel to AB and DC.
    # AE / ED = BF / FC
    ae = rng.randint(4, 8)
    ed = rng.randint(2, 5)
    fc = rng.randint(3, 6)
    # bf = (ae * fc) / ed
    factor = rng.randint(2, 4)
    ed = factor
    ae = factor * rng.randint(2, 3)
    bf = ae * fc // ed

    prompt = (
        f"In trapezium $ABCD$, $AB \\parallel DC$ and line segment $EF$ is drawn parallel to the bases "
        f"with $E$ on $AD$ and $F$ on $BC$. "
        f"Given $AE = {ae}\\text{{ cm}}$, $ED = {ed}\\text{{ cm}}$, and $FC = {fc}\\text{{ cm}}$, "
        f"calculate the length of $BF$."
    )
    sample = (
        f"\\text{{Drawing diagonal }} AC \\text{{ intersecting }} EF \\text{{ at }} G:\\\\\n"
        f"\\text{{In }} \\triangle ADC, EG \\parallel DC \\implies \\frac{{AE}}{{ED}} = \\frac{{AG}}{{GC}}\\\\\n"
        f"\\text{{In }} \\triangle CAB, GF \\parallel AB \\implies \\frac{{AG}}{{GC}} = \\frac{{BF}}{{FC}}\\\\\n"
        f"\\frac{{BF}}{{FC}} = \\frac{{AE}}{{ED}} = \\frac{{{ae}}}{{{ed}}}\\\\\n"
        f"BF = \\frac{{{ae} \\times {fc}}}{{{ed}}} = {bf}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<polygon points="90,40 250,40 310,200 50,200" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="68" y1="120" x2="283" y2="120" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="85" y="32" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">A</text>'
        f'<text x="255" y="32" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">B</text>'
        f'<text x="40" y="215" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">D</text>'
        f'<text x="320" y="215" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">C</text>'
        f'<text x="50" y="125" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">E</text>'
        f'<text x="295" y="125" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">F</text>',
        width=360,
        height=240,
    )
    return {
        "id": "g12_eg_17",
        "topic": "Euclidean geometry",
        "subskill": "17_trapezium_parallel_sides_ratio",
        "question_text": prompt,
        "answer_latex": str(bf),
        "answer_sympy": str(bf),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Trapezium with parallel line EF (AE={ae}, FC={fc})"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Construct diagonal or state parallel transversal property", "marks": 1},
                {"id": "mp2", "desc": "Equate BF/FC = AE/ED", "marks": 1},
                {"id": "mp3", "desc": f"Calculate BF = {bf}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "A line parallel to the parallel sides of a trapezium divides the non-parallel sides in the same proportion.",
            "2_concept": "BF / FC = AE / ED.",
            "3_breakdown": f"BF = ({ae} * {fc}) / {ed} = {bf}.",
        },
        "misconception_tags": ["trapezium_parallel_side_confusion", "cross_division_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 4,
    }


def build_18_ratio_of_areas_with_parallel_transversal(rng: random.Random) -> Dict[str, Any]:
    # In triangle ABC, DE || BC. AD:DB = m:n.
    # Find Area(ADE) : Area(trapezium BCED)
    m = rng.choice([2, 3])
    n = rng.choice([1, 2, 3])
    tot = m + n
    # Area(ADE) / Area(ABC) = (m / tot)^2
    # Area(trapezium) / Area(ABC) = 1 - (m/tot)^2 = (tot^2 - m^2) / tot^2
    # Area(ADE) / Area(trapezium) = m^2 / (tot^2 - m^2)
    m2 = m * m
    trap_parts = tot * tot - m2
    g = math.gcd(m2, trap_parts)
    ans_num = m2 // g
    ans_den = trap_parts // g

    prompt = (
        f"In $\\triangle ABC$, line segment $DE \\parallel BC$ ($D$ on $AB$, $E$ on $AC$) "
        f"such that $AD : DB = {m} : {n}$. "
        f"Find the ratio of the area of $\\triangle ADE$ to the area of the quadrilateral (trapezium) $BCED$ "
        f"in simplest fractional form $\\frac{{a}}{{b}}$."
    )
    sample = (
        f"\\frac{{AD}}{{AB}} = \\frac{{{m}}}{{{m} + {n}}} = \\frac{{{m}}}{{{tot}}}.\\\\\n"
        f"\\text{{Since }} \\triangle ADE \\mathbin{{|||}} \\triangle ABC \\quad (\\text{{equiangular}}):\\\\\n"
        f"\\frac{{\\text{{Area}}(\\triangle ADE)}}{{\\text{{Area}}(\\triangle ABC)}} = "
        f"\\left(\\frac{{AD}}{{AB}}\\right)^2 = \\left(\\frac{{{m}}}{{{tot}}}\\right)^2 = \\frac{{{m2}}}{{{tot * tot}}}.\\\\\n"
        f"\\text{{Area}}(\\text{{trap }} BCED) = {tot * tot} - {m2} = {trap_parts} \\text{{ parts}}.\\\\\n"
        f"\\frac{{\\text{{Area}}(\\triangle ADE)}}{{\\text{{Area}}(\\text{{trap }} BCED)}} = "
        f"\\frac{{{m2}}}{{{trap_parts}}} = \\frac{{{ans_num}}}{{{ans_den}}}."
    )
    svg = _draw_triangle_parallel_svg(labels=("A", "B", "C", "D", "E"))

    return {
        "id": "g12_eg_18",
        "topic": "Euclidean geometry",
        "subskill": "18_ratio_of_areas_with_parallel_transversal",
        "question_text": prompt,
        "answer_latex": f"\\frac{{{ans_num}}}{{{ans_den}}}",
        "answer_sympy": f"{ans_num}/{ans_den}",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Triangle and trapezium area ratio ({m}:{n})"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Ratio AD/AB = {m}/{tot}", "marks": 1},
                {"id": "mp2", "desc": f"Area ratio ADE/ABC = ({m}/{tot})^2 = {m2}/{tot*tot}", "marks": 1},
                {"id": "mp3", "desc": f"Trapezium ratio {ans_num}/{ans_den}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Similar triangles have area ratio equal to the square of their scale factor.",
            "2_concept": f"Area(ADE)/Area(ABC) = (AD/AB)^2 = ({m}/{tot})^2 = {m2}/{tot*tot}.",
            "3_breakdown": f"Area of trapezium = {tot*tot} - {m2} = {trap_parts}. Ratio = {ans_num}/{ans_den}.",
        },
        "misconception_tags": ["forgetting_to_square_scale_factor", "using_subsegment_ratio_directly"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 4,
    }


def build_19_proportionality_median_and_parallel_line(rng: random.Random) -> Dict[str, Any]:
    # In triangle ABC, AD is a median (BD = DC). Line EF || AD cuts BC.
    # Area ratios or segment relations.
    total_area = rng.choice([48, 60, 72, 84])
    median_area = total_area // 2

    prompt = (
        f"In $\\triangle ABC$, line segment $AD$ is a median to side $BC$ ($BD = DC$). "
        f"If the total area of $\\triangle ABC = {total_area}\\text{{ cm}}^2$, "
        f"calculate the area of $\\triangle ABD$."
    )
    sample = (
        f"\\text{{A median of a triangle bisects its area because both resulting triangles }} "
        f"\\triangle ABD \\text{{ and }} \\triangle ACD \\text{{ share the same altitude from }} A "
        f"\\text{{ and have equal bases }} (BD = DC).\\\\\n"
        f"\\text{{Area}}(\\triangle ABD) = \\frac{{1}}{{2}} \\times \\text{{Area}}(\\triangle ABC) "
        f"= \\frac{{1}}{{2}} \\times {total_area} = {median_area}\\text{{ cm}}^2."
    )
    svg = _svg_wrap(
        f'<polygon points="180,30 60,210 300,210" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="180" y1="30" x2="180" y2="210" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="180" y="22" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">A</text>'
        f'<text x="50" y="225" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">B</text>'
        f'<text x="310" y="225" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#0f172a">C</text>'
        f'<text x="180" y="228" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#dc2626">D</text>'
        f'<text x="120" y="200" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">BD = DC</text>',
        width=360,
        height=250,
    )
    return {
        "id": "g12_eg_19",
        "topic": "Euclidean geometry",
        "subskill": "19_proportionality_median_and_parallel_line",
        "question_text": prompt,
        "answer_latex": str(median_area),
        "answer_sympy": str(median_area),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Triangle median area bisection (Area = {total_area})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "State median bisects triangle area (equal bases and equal height)", "marks": 1},
                {"id": "mp2", "desc": f"Area = {median_area}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "A median connects a vertex to the midpoint of the opposite side.",
            "2_concept": "Triangles ABD and ACD have equal bases (BD = DC) and the same height.",
            "3_breakdown": f"Area = {total_area} / 2 = {median_area}.",
        },
        "misconception_tags": ["median_definition_confusion", "area_halving_omission"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 2,
    }


def build_20_proportionality_diagonal_intersection_quadrilateral(rng: random.Random) -> Dict[str, Any]:
    # Diagonals AC and BD intersect at O.
    # If AO/OC = DO/OB, AB || DC
    ao = rng.randint(3, 6)
    k = rng.randint(2, 4)
    oc = ao * k
    bo = rng.randint(4, 7)
    od = bo * k

    prompt = (
        f"In quadrilateral $ABCD$, diagonals $AC$ and $BD$ intersect at point $O$. "
        f"The segment lengths from the intersection are $AO = {ao}\\text{{ cm}}$, $OC = {oc}\\text{{ cm}}$, "
        f"and $OB = {bo}\\text{{ cm}}$. "
        f"If $AB \\parallel DC$, calculate the length of segment $OD$."
    )
    sample = (
        f"\\text{{Since }} AB \\parallel DC, \\triangle OAB \\mathbin{{|||}} \\triangle OCD \\quad (\\text{{equiangular}}):\\\\\n"
        f"\\frac{{OD}}{{OB}} = \\frac{{OC}}{{OA}} \\implies "
        f"\\frac{{OD}}{{{bo}}} = \\frac{{{oc}}}{{{ao}}} = {k}\\\\\n"
        f"OD = {bo} \\times {k} = {od}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<polygon points="70,50 220,50 290,190 40,190" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="70" y1="50" x2="290" y2="190" stroke="#dc2626" stroke-width="2"/>'
        f'<line x1="220" y1="50" x2="40" y2="190" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="65" y="40" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">A</text>'
        f'<text x="225" y="40" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">B</text>'
        f'<text x="35" y="205" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">D</text>'
        f'<text x="295" y="205" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">C</text>'
        f'<text x="145" y="115" font-family="sans-serif" font-weight="bold" font-size="13" fill="#7c3aed">O</text>',
        width=360,
        height=230,
    )
    return {
        "id": "g12_eg_20",
        "topic": "Euclidean geometry",
        "subskill": "20_proportionality_diagonal_intersection_quadrilateral",
        "question_text": prompt,
        "answer_latex": str(od),
        "answer_sympy": str(od),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Quadrilateral diagonal intersection (AO={ao}, OB={bo})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "State ratio OD/OB = OC/OA", "marks": 1},
                {"id": "mp2", "desc": f"Calculate OD = {od}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "With AB || DC, alternate interior angles make triangles OAB and OCD similar.",
            "2_concept": f"OD / OB = OC / OA = {oc} / {ao} = {k}.",
            "3_breakdown": f"OD = {bo} * {k} = {od}.",
        },
        "misconception_tags": ["diagonal_segment_inversion", "similar_triangle_orientation_confusion"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_21_proportionality_external_division(rng: random.Random) -> Dict[str, Any]:
    # Line parallel to side intersecting extensions of sides
    # In triangle ABC, line DE || BC intersects AB produced at D and AC produced at E
    ab = rng.randint(6, 10)
    ad_tot = ab + rng.randint(4, 8)
    bd = ad_tot - ab
    ac = rng.randint(4, 8)
    # AE / AC = AD / AB => AE = AC * AD / AB
    g = math.gcd(ac * ad_tot, ab)
    ae_num = (ac * ad_tot) // g
    ae_den = ab // g
    if ae_den == 1:
        ans_sympy = str(ae_num)
        ans_latex = str(ae_num)
    else:
        ans_sympy = f"{ae_num}/{ae_den}"
        ans_latex = f"\\frac{{{ae_num}}}{{{ae_den}}}"

    prompt = (
        f"In $\\triangle ABC$, the sides $AB$ and $AC$ are extended beyond $B$ and $C$ to points $D$ and $E$ "
        f"respectively such that $DE \\parallel BC$. "
        f"Given $AB = {ab}\\text{{ cm}}$, $BD = {bd}\\text{{ cm}}$ (so $AD = {ad_tot}\\text{{ cm}}$), "
        f"and $AC = {ac}\\text{{ cm}}$, calculate the total length of $AE$."
    )
    sample = (
        f"\\text{{Since }} DE \\parallel BC, \\frac{{AE}}{{AC}} = \\frac{{AD}}{{AB}} \\quad (\\text{{prop theorem, }} DE \\parallel BC)\\\\\n"
        f"\\frac{{AE}}{{{ac}}} = \\frac{{{ad_tot}}}{{{ab}}}\\\\\n"
        f"AE = \\frac{{{ac} \\times {ad_tot}}}{{{ab}}} = {ans_latex}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<polygon points="180,30 110,130 250,130" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="110" y1="130" x2="60" y2="200" stroke="#94a3b8" stroke-dasharray="3" stroke-width="2"/>'
        f'<line x1="250" y1="130" x2="300" y2="200" stroke="#94a3b8" stroke-dasharray="3" stroke-width="2"/>'
        f'<line x1="60" y1="200" x2="300" y2="200" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="180" y="22" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">A</text>'
        f'<text x="100" y="130" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">B</text>'
        f'<text x="255" y="130" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">C</text>'
        f'<text x="50" y="210" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">D</text>'
        f'<text x="310" y="210" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">E</text>',
        width=360,
        height=240,
    )
    return {
        "id": "g12_eg_21",
        "topic": "Euclidean geometry",
        "subskill": "21_proportionality_external_division",
        "question_text": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": ans_sympy,
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"External division by parallel line (AB={ab}, AC={ac})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "State ratio AE/AC = AD/AB with reason", "marks": 1},
                {"id": "mp2", "desc": f"Calculate AE = {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The proportionality theorem applies equally to external extensions of sides.",
            "2_concept": "AE / AC = AD / AB.",
            "3_breakdown": f"AE = ({ac} * {ad_tot}) / {ab} = {ans_latex}.",
        },
        "misconception_tags": ["external_extension_subtraction_error", "ratio_misplacement"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_22_proportionality_coordinate_geometry_verification(rng: random.Random) -> Dict[str, Any]:
    # On coordinate grid: A(2, 6), B(0, 0), C(8, 0)
    # D on AB, E on AC such that y = 3.
    # Verify ratio AD/DB = AE/EC = 1:1 (or other ratio)
    k = rng.choice([2, 3])
    ratio_str = f"1/{k-1}"
    ans_latex = f"\\frac{{1}}{{{k-1}}}"

    prompt = (
        f"In the Cartesian plane, the vertices of $\\triangle ABC$ are $A(0{{,}} {k * 4})$, $B(-{k * 2}{{,}} 0)$, "
        f"and $C({k * 4}{{,}} 0)$. A horizontal line $y = {k * 4 - 4}$ intersects side $AB$ at $D$ and side $AC$ at $E$. "
        f"Since the line is horizontal and $BC$ lies on the x-axis, $DE \\parallel BC$. "
        f"Determine the numerical ratio $\\frac{{AD}}{{DB}}$ in simplest fractional form."
    )
    sample = (
        f"\\text{{The vertical drop from }} A \\text{{ to }} D \\text{{ is }} \\Delta y_1 = {k * 4} - {k * 4 - 4} = 4.\\\\\n"
        f"\\text{{The vertical drop from }} D \\text{{ to }} B \\text{{ is }} \\Delta y_2 = {k * 4 - 4} - 0 = {k * 4 - 4}.\\\\\n"
        f"\\frac{{AD}}{{DB}} = \\frac{{\\Delta y_1}}{{\\Delta y_2}} = \\frac{{4}}{{{k * 4 - 4}}} = \\frac{{1}}{{{k - 1}}}."
    )
    svg = _svg_wrap(
        f'<line x1="30" y1="180" x2="330" y2="180" stroke="#94a3b8" stroke-width="2"/>'
        f'<line x1="160" y1="20" x2="160" y2="210" stroke="#94a3b8" stroke-width="2"/>'
        f'<polygon points="160,40 70,180 270,180" fill="rgba(37,99,235,0.1)" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="100" y1="90" x2="230" y2="90" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="165" y="35" font-family="sans-serif" font-size="12" fill="#0f172a">A</text>'
        f'<text x="60" y="195" font-family="sans-serif" font-size="12" fill="#0f172a">B</text>'
        f'<text x="275" y="195" font-family="sans-serif" font-size="12" fill="#0f172a">C</text>'
        f'<text x="90" y="85" font-family="sans-serif" font-size="12" fill="#2563eb">D</text>'
        f'<text x="235" y="85" font-family="sans-serif" font-size="12" fill="#2563eb">E</text>',
        width=360,
        height=230,
    )
    return {
        "id": "g12_eg_22",
        "topic": "Euclidean geometry",
        "subskill": "22_proportionality_coordinate_geometry_verification",
        "question_text": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"1/{k-1}",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Cartesian proportionality verification (scale={k})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Determine vertical distance ratio delta y1 / delta y2", "marks": 1},
                {"id": "mp2", "desc": f"Simplify to {ans_latex}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Because the line DE is horizontal and parallel to BC, the ratio of segment lengths equals the ratio of vertical drops.",
            "2_concept": f"AD / DB = (y_A - y_D) / (y_D - y_B) = 4 / {k * 4 - 4}.",
            "3_breakdown": f"Ratio = 4 / {k * 4 - 4} = 1 / {k - 1}.",
        },
        "misconception_tags": ["coordinate_distance_formula_unnecessary_complexity", "inverting_y_differences"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_23_proportionality_applied_surveying_river_width(rng: random.Random) -> Dict[str, Any]:
    # River width ST. Markers P, Q, R, S such that QR || ST.
    # TR = 100 m, TP = 600 m => RP = 500 m. QR = 150 m.
    # ST / QR = TP / RP
    tp = rng.choice([600, 650, 700])
    tr = rng.choice([100, 120, 150])
    rp = tp - tr
    qr = rng.choice([120, 150, 180])
    # st = (qr * tp) / rp
    g = math.gcd(qr * tp, rp)
    st_num = (qr * tp) // g
    st_den = rp // g
    if st_den == 1:
        ans_sympy = str(st_num)
        ans_latex = str(st_num)
    else:
        ans_sympy = f"{st_num}/{st_den}"
        ans_latex = f"\\frac{{{st_num}}}{{{st_den}}}"

    prompt = (
        f"A surveyor measures the width of a river $ST$ using marker points $P, Q, R, S, T$. "
        f"Lines $QR$ and $ST$ are parallel ($QR \\parallel ST$). "
        f"The measured distances along the survey baseline are $TR = {tr}\\text{{ m}}$, "
        f"$TP = {tp}\\text{{ m}}$ (so $RP = TP - TR = {rp}\\text{{ m}}$), and $QR = {qr}\\text{{ m}}$. "
        f"Calculate the width of the river $ST$ in metres."
    )
    sample = (
        f"\\text{{Since }} QR \\parallel ST, \\triangle PQR \\mathbin{{|||}} \\triangle PST \\quad (\\text{{equiangular}}):\\\\\n"
        f"\\frac{{ST}}{{QR}} = \\frac{{TP}}{{RP}} \\implies "
        f"ST = \\frac{{{qr} \\times {tp}}}{{{rp}}} = {ans_latex}\\text{{ m}}."
    )
    svg = _svg_wrap(
        f'<rect x="40" y="80" width="280" height="70" fill="rgba(6,182,212,0.2)" stroke="#0891b2" stroke-dasharray="4"/>'
        f'<text x="180" y="120" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#0891b2">River</text>'
        f'<line x1="80" y1="40" x2="280" y2="40" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="80" y1="180" x2="280" y2="180" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="75" y="35" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">Q</text>'
        f'<text x="285" y="35" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">R</text>'
        f'<text x="75" y="195" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">S</text>'
        f'<text x="285" y="195" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">T</text>',
        width=360,
        height=220,
    )
    return {
        "id": "g12_eg_23",
        "topic": "Euclidean geometry",
        "subskill": "23_proportionality_applied_surveying_river_width",
        "question_text": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": ans_sympy,
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"River width surveying measurement (TR={tr}, TP={tp})"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculate RP = TP - TR = {rp} m", "marks": 1},
                {"id": "mp2", "desc": "Set up ratio ST/QR = TP/RP", "marks": 1},
                {"id": "mp3", "desc": f"Answer ST = {ans_latex} m", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "First find the distance RP by subtracting TR from TP.",
            "2_concept": "Because QR || ST, triangle PQR is similar to triangle PST.",
            "3_breakdown": f"ST = ({qr} * {tp}) / {rp} = {ans_latex} m.",
        },
        "misconception_tags": ["using_tr_instead_of_rp", "proportion_setup_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 4,
    }


def build_24_proportionality_applied_shadow_height_projection(rng: random.Random) -> Dict[str, Any]:
    # Person 1.6m tall casts 2m shadow. Pole casts shadow of S m. Find height H.
    person_h = rng.choice([1.5, 1.6, 1.8])
    person_s = rng.choice([2.0, 2.4, 2.5])
    pole_s = person_s * rng.randint(3, 5)
    pole_h = round((person_h * pole_s) / person_s, 2)
    s_pole_h = str(pole_h).replace(".", "{{,}}")
    s_person_h = str(person_h).replace(".", "{{,}}")
    s_person_s = str(person_s).replace(".", "{{,}}")
    s_pole_s = str(pole_s).replace(".", "{{,}}")

    prompt = (
        f"At a particular time of day, sun rays make the same angle with the ground. "
        f"A student of height ${s_person_h}\\text{{ m}}$ casts a horizontal shadow of length ${s_person_s}\\text{{ m}}$. "
        f"At the exact same moment, a vertical lamppost casts a shadow of length ${s_pole_s}\\text{{ m}}$. "
        f"Assuming both the person and the lamppost stand perpendicular to the ground, "
        f"calculate the height of the lamppost in metres."
    )
    sample = (
        f"\\text{{Both triangles are right-angled and share the same angle of elevation of the sun: }}\\\\\n"
        f"\\frac{{H_\\text{{pole}}}}{{H_\\text{{student}}}} = \\frac{{\\text{{Shadow}}_\\text{{pole}}}}{{\\text{{Shadow}}_\\text{{student}}}}\\\\\n"
        f"\\frac{{H_\\text{{pole}}}}{{{s_person_h}}} = \\frac{{{s_pole_s}}}{{{s_person_s}}}\\\\\n"
        f"H_\\text{{pole}} = \\frac{{{s_person_h} \\times {s_pole_s}}}{{{s_person_s}}} = {s_pole_h}\\text{{ m}}."
    )
    svg = _svg_wrap(
        f'<line x1="30" y1="180" x2="330" y2="180" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="80" y1="180" x2="80" y2="110" stroke="#2563eb" stroke-width="4"/>'
        f'<line x1="80" y1="110" x2="160" y2="180" stroke="#f59e0b" stroke-dasharray="3" stroke-width="2"/>'
        f'<line x1="220" y1="180" x2="220" y2="40" stroke="#dc2626" stroke-width="4"/>'
        f'<line x1="220" y1="40" x2="330" y2="180" stroke="#f59e0b" stroke-dasharray="3" stroke-width="2"/>'
        f'<text x="80" y="95" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">Student</text>'
        f'<text x="220" y="25" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#dc2626">Lamppost</text>',
        width=360,
        height=220,
    )
    return {
        "id": "g12_eg_24",
        "topic": "Euclidean geometry",
        "subskill": "24_proportionality_applied_shadow_height_projection",
        "question_text": prompt,
        "answer_latex": s_pole_h,
        "answer_sympy": str(pole_h),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Shadow projection similar triangles (H={s_person_h}, S={s_person_s})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Set up similar triangles height-to-shadow ratio", "marks": 1},
                {"id": "mp2", "desc": f"Calculate height = {s_pole_h} m", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Height of object / Shadow of object is constant for any object at the same moment.",
            "2_concept": "H_pole / H_student = Shadow_pole / Shadow_student.",
            "3_breakdown": f"H_pole = ({person_h} * {pole_s}) / {person_s} = {pole_h} m.",
        },
        "misconception_tags": ["inverting_height_shadow_ratio", "decimal_rounding_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_25_proportionality_applied_vuvuzela_cone_cutoff(rng: random.Random) -> Dict[str, Any]:
    # Cone with diameter D and height H. Small cut-off radius r. Find height of cutoff cone h.
    # By similar cross-sections: r / R = h / H
    big_r = rng.choice([20, 24, 28])
    big_h = rng.choice([40, 50, 60])
    small_r = rng.choice([4, 5, 6])
    small_h = (small_r * big_h) // big_r
    big_d = big_r * 2

    prompt = (
        f"A hollow cone used to make a stadium horn has a base diameter of ${big_d}\\text{{ cm}}$ "
        f"(radius $R = {big_r}\\text{{ cm}}$) and a total perpendicular height of $H = {big_h}\\text{{ cm}}$. "
        f"The small tip of the cone is cut off parallel to the base so that the open mouthpiece has a radius of "
        f"$r = {small_r}\\text{{ cm}}$. "
        f"Using the principle of similar triangles in the cone's axial cross-section, "
        f"calculate the height $h$ of the tip portion that was cut off."
    )
    sample = (
        f"\\text{{The vertical cross-section through the vertex yields similar triangles: }}\\\\\n"
        f"\\frac{{h}}{{H}} = \\frac{{r}}{{R}}\\\\\n"
        f"\\frac{{h}}{{{big_h}}} = \\frac{{{small_r}}}{{{big_r}}}\\\\\n"
        f"h = \\frac{{{small_r} \\times {big_h}}}{{{big_r}}} = {small_h}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<polygon points="180,30 80,210 280,210" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="140" y1="100" x2="220" y2="100" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="180" y1="30" x2="180" y2="210" stroke="#dc2626" stroke-dasharray="3" stroke-width="2"/>'
        f'<text x="180" y="20" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#0f172a">V</text>'
        f'<text x="195" y="95" font-family="sans-serif" font-size="12" fill="#2563eb">r = {small_r}</text>'
        f'<text x="230" y="205" font-family="sans-serif" font-size="12" fill="#0f172a">R = {big_r}</text>'
        f'<text x="160" y="70" font-family="sans-serif" font-size="12" fill="#dc2626">h</text>',
        width=360,
        height=240,
    )
    return {
        "id": "g12_eg_25",
        "topic": "Euclidean geometry",
        "subskill": "25_proportionality_applied_vuvuzela_cone_cutoff",
        "question_text": prompt,
        "answer_latex": str(small_h),
        "answer_sympy": str(small_h),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Cone cross-section similar triangles"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"State ratio h/H = r/R: h/{big_h} = {small_r}/{big_r}", "marks": 1},
                {"id": "mp2", "desc": f"Calculate cutoff height h = {small_h} cm", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The axial cross-section of a cone forms two similar isosceles triangles.",
            "2_concept": "Ratio of heights = ratio of radii: h / H = r / R.",
            "3_breakdown": f"h = ({small_r} * {big_h}) / {big_r} = {small_h} cm.",
        },
        "misconception_tags": ["using_diameter_instead_of_radius", "inverse_proportion_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


# Map of builders 01 to 25
BUILDERS_01_25 = {
    "01_ratio_simplification_and_fraction": build_01_ratio_simplification_and_fraction,
    "02_proportion_extremes_and_means": build_02_proportion_extremes_and_means,
    "03_proportion_transformations": build_03_proportion_transformations,
    "04_ratio_of_triangle_areas_equal_altitudes": build_04_ratio_of_triangle_areas_equal_altitudes,
    "05_ratio_of_triangle_areas_equal_bases": build_05_ratio_of_triangle_areas_equal_bases,
    "06_compound_area_ratios_nested_triangles": build_06_compound_area_ratios_nested_triangles,
    "07_proportionality_theorem_single_parallel_side": build_07_proportionality_theorem_single_parallel_side,
    "08_proportionality_theorem_segment_sum_relation": build_08_proportionality_theorem_segment_sum_relation,
    "09_proportionality_theorem_algebraic_linear": build_09_proportionality_theorem_algebraic_linear,
    "10_proportionality_theorem_algebraic_quadratic": build_10_proportionality_theorem_algebraic_quadratic,
    "11_proportionality_theorem_converse_test": build_11_proportionality_theorem_converse_test,
    "12_proportionality_theorem_multiple_parallels": build_12_proportionality_theorem_multiple_parallels,
    "13_proportionality_theorem_nested_parallels": build_13_proportionality_theorem_nested_parallels,
    "14_midpoint_theorem_as_proportionality_special_case": build_14_midpoint_theorem_as_proportionality_special_case,
    "15_proportionality_dividing_segments_ratio_algebra": build_15_proportionality_dividing_segments_ratio_algebra,
    "16_proportionality_shared_side_two_triangles": build_16_proportionality_shared_side_two_triangles,
    "17_trapezium_parallel_sides_ratio": build_17_trapezium_parallel_sides_ratio,
    "18_ratio_of_areas_with_parallel_transversal": build_18_ratio_of_areas_with_parallel_transversal,
    "19_proportionality_median_and_parallel_line": build_19_proportionality_median_and_parallel_line,
    "20_proportionality_diagonal_intersection_quadrilateral": build_20_proportionality_diagonal_intersection_quadrilateral,
    "21_proportionality_external_division": build_21_proportionality_external_division,
    "22_proportionality_coordinate_geometry_verification": build_22_proportionality_coordinate_geometry_verification,
    "23_proportionality_applied_surveying_river_width": build_23_proportionality_applied_surveying_river_width,
    "24_proportionality_applied_shadow_height_projection": build_24_proportionality_applied_shadow_height_projection,
    "25_proportionality_applied_vuvuzela_cone_cutoff": build_25_proportionality_applied_vuvuzela_cone_cutoff,
}
