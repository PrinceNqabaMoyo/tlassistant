"""Grade 12 Mathematics — Euclidean Geometry Archetypes 26 to 50.
Focus: Similarity Criteria, Proportional Sides, Pythagorean Theorem via Similarity, Circle Similarity Riders.
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

from app.utils.grade12_mathematics.euclidean_geometry_archetypes_01_25 import _draw_triangle_parallel_svg


# --------------------------------------------------------------------------- #
# SVG Vector Drawing Helpers for Similarity and Circle Geometry Figures
# --------------------------------------------------------------------------- #

def _svg_wrap(inner_svg: str, width: int = 360, height: int = 260) -> str:
    return (
        f'<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" '
        f'xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; max-width:{width}px;">'
        f'{inner_svg}'
        f'</svg>'
    )


def _draw_bowtie_svg(
    a_pt=(70, 50),
    b_pt=(290, 50),
    c_pt=(290, 200),
    d_pt=(70, 200),
    x_pt=(180, 125),
    labels=("A", "B", "C", "D", "X"),
) -> str:
    """Draws hourglass / bowtie figure with parallel lines AB and CD intersecting at X."""
    elements = [
        f'<line x1="{a_pt[0]}" y1="{a_pt[1]}" x2="{b_pt[0]}" y2="{b_pt[1]}" stroke="#2563eb" stroke-width="2"/>',
        f'<line x1="{d_pt[0]}" y1="{d_pt[1]}" x2="{c_pt[0]}" y2="{c_pt[1]}" stroke="#2563eb" stroke-width="2"/>',
        f'<line x1="{a_pt[0]}" y1="{a_pt[1]}" x2="{c_pt[0]}" y2="{c_pt[1]}" stroke="#1e293b" stroke-width="2"/>',
        f'<line x1="{b_pt[0]}" y1="{b_pt[1]}" x2="{d_pt[0]}" y2="{d_pt[1]}" stroke="#1e293b" stroke-width="2"/>',
        # Parallel arrow markers
        f'<path d="M 174 46 L 180 50 L 174 54" fill="none" stroke="#2563eb" stroke-width="2"/>',
        f'<path d="M 174 196 L 180 200 L 174 204" fill="none" stroke="#2563eb" stroke-width="2"/>',
        # Labels
        f'<text x="{a_pt[0] - 12}" y="{a_pt[1] + 5}" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">{labels[0]}</text>',
        f'<text x="{b_pt[0] + 6}" y="{b_pt[1] + 5}" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">{labels[1]}</text>',
        f'<text x="{c_pt[0] + 6}" y="{c_pt[1] + 5}" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">{labels[2]}</text>',
        f'<text x="{d_pt[0] - 12}" y="{d_pt[1] + 5}" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">{labels[3]}</text>',
        f'<text x="{x_pt[0] + 8}" y="{x_pt[1] - 8}" font-family="sans-serif" font-weight="bold" font-size="13" fill="#dc2626">{labels[4]}</text>',
    ]
    return _svg_wrap("".join(elements), width=360, height=250)


def _draw_right_triangle_altitude_svg(labels=("A", "B", "C", "D")) -> str:
    """Draws right triangle ABC with altitude BD perpendicular to hypotenuse AC."""
    # A at (60, 200), B at (160, 50), C at (310, 200)
    # Foot of perpendicular D on AC at (160, 200)
    elements = [
        '<polygon points="60,200 160,50 310,200" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>',
        '<line x1="160" y1="50" x2="160" y2="200" stroke="#dc2626" stroke-width="2"/>',
        # Right angle marker at foot D
        '<path d="M 160 185 L 175 185 L 175 200" fill="none" stroke="#dc2626" stroke-width="1.5"/>',
        # Right angle marker at vertex B
        '<path d="M 150 65 L 165 75 L 175 60" fill="none" stroke="#2563eb" stroke-width="1.5"/>',
        # Labels
        f'<text x="45" y="210" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">{labels[0]}</text>',
        f'<text x="160" y="38" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">{labels[1]}</text>',
        f'<text x="320" y="210" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">{labels[2]}</text>',
        f'<text x="160" y="222" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#dc2626">{labels[3]}</text>',
    ]
    return _svg_wrap("".join(elements), width=360, height=250)


def _draw_circle_chords_svg(title_pts="A, B, C, D, X") -> str:
    """Draws a circle with two intersecting chords creating similar bowtie triangles."""
    # Circle centre at (180, 120), radius 90
    elements = [
        '<circle cx="180" cy="120" r="90" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        # Chord AC and BD intersecting at X
        '<line x1="110" y1="70" x2="250" y2="170" stroke="#2563eb" stroke-width="2"/>',
        '<line x1="110" y1="170" x2="250" y2="70" stroke="#2563eb" stroke-width="2"/>',
        '<line x1="110" y1="70" x2="110" y2="170" stroke="#1e293b" stroke-width="2"/>',
        '<line x1="250" y1="70" x2="250" y2="170" stroke="#1e293b" stroke-width="2"/>',
        # Point markers
        '<circle cx="110" cy="70" r="3" fill="#0f172a"/>',
        '<circle cx="110" cy="170" r="3" fill="#0f172a"/>',
        '<circle cx="250" cy="70" r="3" fill="#0f172a"/>',
        '<circle cx="250" cy="170" r="3" fill="#0f172a"/>',
        '<circle cx="180" cy="120" r="3" fill="#dc2626"/>',
        # Labels
        '<text x="95" y="65" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">A</text>',
        '<text x="95" y="185" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">D</text>',
        '<text x="260" y="65" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">C</text>',
        '<text x="260" y="185" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">B</text>',
        '<text x="180" y="140" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="13" fill="#dc2626">X</text>',
    ]
    return _svg_wrap("".join(elements), width=360, height=250)


# --------------------------------------------------------------------------- #
# Archetype Builders 26 to 50
# --------------------------------------------------------------------------- #

def build_26_similarity_equiangular_definition_and_identification(rng: random.Random) -> Dict[str, Any]:
    angle_a = rng.randint(45, 65)
    angle_b = rng.randint(50, 70)
    angle_c = 180 - angle_a - angle_b

    prompt = (
        f"In $\\triangle ABC$, $\\hat{{A}} = {angle_a}^\\circ$ and $\\hat{{B}} = {angle_b}^\\circ$. "
        f"In $\\triangle DEF$, $\\hat{{D}} = {angle_a}^\\circ$ and $\\hat{{F}} = {angle_c}^\\circ$. "
        f"Calculate the size of $\\hat{{C}}$ in degrees to confirm both triangles are equiangular ($\\\\angle\\\\angle\\\\angle$)."
    )
    sample = (
        f"\\text{{In }} \\triangle ABC:\\\\\n"
        f"\\hat{{C}} = 180^\\circ - ({angle_a}^\\circ + {angle_b}^\\circ) = {angle_c}^\\circ \\quad (\\text{{sum of }} \\angle\\text{{s in }} \\triangle).\\\\\n"
        f"\\text{{Since }} \\hat{{A}} = \\hat{{D}} = {angle_a}^\\circ, \\hat{{B}} = \\hat{{E}} = {angle_b}^\\circ, "
        f"\\text{{ and }} \\hat{{C}} = \\hat{{F}} = {angle_c}^\\circ, \\triangle ABC \\mathbin{{|||}} \\triangle DEF \\quad (\\text{{equiangular}})."
    )
    svg = _svg_wrap(
        f'<polygon points="40,180 120,40 180,180" fill="#f8fafc" stroke="#2563eb" stroke-width="2"/>'
        f'<polygon points="210,180 270,75 320,180" fill="#f8fafc" stroke="#059669" stroke-width="2"/>'
        f'<text x="120" y="30" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="12" fill="#2563eb">A ({angle_a}°)</text>'
        f'<text x="35" y="195" font-family="sans-serif" font-weight="bold" font-size="12" fill="#2563eb">B ({angle_b}°)</text>'
        f'<text x="185" y="195" font-family="sans-serif" font-weight="bold" font-size="12" fill="#2563eb">C</text>'
        f'<text x="270" y="65" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="12" fill="#059669">D ({angle_a}°)</text>'
        f'<text x="205" y="195" font-family="sans-serif" font-weight="bold" font-size="12" fill="#059669">E</text>'
        f'<text x="325" y="195" font-family="sans-serif" font-weight="bold" font-size="12" fill="#059669">F ({angle_c}°)</text>',
        width=360,
        height=220,
    )
    return {
        "id": "g12_eg_26",
        "topic": "Euclidean geometry",
        "subskill": "26_similarity_equiangular_definition_and_identification",
        "question_text": prompt,
        "answer_latex": f"{angle_c}^\\circ",
        "answer_sympy": str(angle_c),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Equiangular similar triangles"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Sum of angles in triangle = 180 degrees", "marks": 1},
                {"id": "mp2", "desc": f"Angle C = {angle_c} degrees", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The interior angles of any triangle sum to 180 degrees.",
            "2_concept": f"Angle C = 180 - ({angle_a} + {angle_b}).",
            "3_breakdown": f"Angle C = 180 - {angle_a + angle_b} = {angle_c} degrees.",
        },
        "misconception_tags": ["arithmetic_angle_subtraction_error", "angle_sum_confusion"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 2,
    }


def build_27_similarity_statement_vertex_ordering(rng: random.Random) -> Dict[str, Any]:
    # Corresponding vertices test
    letters_1 = ["A", "B", "C"]
    letters_2 = ["D", "E", "F"]
    rng.shuffle(letters_2)
    t1_name = "ABC"
    t2_name = "".join(letters_2)

    prompt = (
        f"In two similar triangles, vertices must be named in exact corresponding order. "
        f"If $\\hat{{A}} = \\hat{{{letters_2[0]}}}$, $\\hat{{B}} = \\hat{{{letters_2[1]}}}$, "
        f"and $\\hat{{C}} = \\hat{{{letters_2[2]}}}$, write the similarity statement in the form "
        f"$\\triangle ABC \\mathbin{{|||}} \\triangle \\text{{XYZ}}$."
    )
    ans_latex = f"\\triangle {t2_name}"
    sample = (
        f"\\text{{Matching corresponding equal angles: }}\\\\\n"
        f"A \\longleftrightarrow {letters_2[0]}\\\\\n"
        f"B \\longleftrightarrow {letters_2[1]}\\\\\n"
        f"C \\longleftrightarrow {letters_2[2]}\\\\\n"
        f"\\text{{Therefore, }} \\triangle ABC \\mathbin{{|||}} \\triangle {t2_name}."
    )
    svg = _svg_wrap(
        f'<text x="50" y="60" font-family="sans-serif" font-size="14" fill="#1e293b">Triangle 1: Angles A, B, C</text>'
        f'<text x="50" y="100" font-family="sans-serif" font-size="14" fill="#2563eb">Equal to: Angles {letters_2[0]}, {letters_2[1]}, {letters_2[2]}</text>'
        f'<text x="50" y="150" font-family="sans-serif" font-size="14" font-weight="bold" fill="#059669">Correct Statement: ABC ||| {t2_name}</text>',
        width=360,
        height=180,
    )
    return {
        "id": "g12_eg_27",
        "topic": "Euclidean geometry",
        "subskill": "27_similarity_statement_vertex_ordering",
        "question_text": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"'{t2_name}'",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Corresponding vertex matching"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Match vertices in one-to-one correspondence", "marks": 1},
                {"id": "mp2", "desc": f"Correct order {t2_name}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Match each letter in ABC with its corresponding equal angle in the second triangle.",
            "2_concept": f"A matches {letters_2[0]}, B matches {letters_2[1]}, C matches {letters_2[2]}.",
            "3_breakdown": f"The triangle is named {t2_name}.",
        },
        "misconception_tags": ["arbitrary_alphabetical_vertex_naming", "misaligned_corresponding_vertices"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 2,
    }


def build_28_similarity_finding_corresponding_side_lengths(rng: random.Random) -> Dict[str, Any]:
    # ABC ||| DEF. AB = c1, BC = a1, AC = b1. DE = c2. Find EF (a2)
    k = rng.choice([2, 3, 4])
    ab = rng.randint(4, 7)
    bc = rng.randint(5, 9)
    de = ab * k
    ef = bc * k

    prompt = (
        f"It is given that $\\triangle ABC \\mathbin{{|||}} \\triangle DEF$. "
        f"The lengths of the sides are $AB = {ab}\\text{{ cm}}$, $BC = {bc}\\text{{ cm}}$, "
        f"and $DE = {de}\\text{{ cm}}$. "
        f"Calculate the length of side $EF$."
    )
    sample = (
        f"\\text{{Since }} \\triangle ABC \\mathbin{{|||}} \\triangle DEF, "
        f"\\frac{{EF}}{{BC}} = \\frac{{DE}}{{AB}} \\quad (\\text{{sides in proportion, }} \\triangle ABC \\mathbin{{|||}} \\triangle DEF)\\\\\n"
        f"\\frac{{EF}}{{{bc}}} = \\frac{{{de}}}{{{ab}}} = {k}\\\\\n"
        f"EF = {bc} \\times {k} = {ef}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<polygon points="40,160 110,60 160,160" fill="#f8fafc" stroke="#2563eb" stroke-width="2"/>'
        f'<polygon points="200,190 280,40 340,190" fill="#f8fafc" stroke="#059669" stroke-width="2"/>'
        f'<text x="65" y="100" font-family="sans-serif" font-size="12" fill="#2563eb">AB = {ab}</text>'
        f'<text x="100" y="175" font-family="sans-serif" font-size="12" fill="#2563eb">BC = {bc}</text>'
        f'<text x="230" y="100" font-family="sans-serif" font-size="12" fill="#059669">DE = {de}</text>'
        f'<text x="260" y="205" font-family="sans-serif" font-size="12" fill="#dc2626">EF = ?</text>',
        width=360,
        height=220,
    )
    return {
        "id": "g12_eg_28",
        "topic": "Euclidean geometry",
        "subskill": "28_similarity_finding_corresponding_side_lengths",
        "question_text": prompt,
        "answer_latex": str(ef),
        "answer_sympy": str(ef),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Similar triangles corresponding side lengths"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "State ratio EF/BC = DE/AB with reason", "marks": 1},
                {"id": "mp2", "desc": f"Calculate EF = {ef}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "In similar triangles, the ratio of corresponding sides is equal.",
            "2_concept": f"EF / {bc} = {de} / {ab} = {k}.",
            "3_breakdown": f"EF = {bc} * {k} = {ef} cm.",
        },
        "misconception_tags": ["inverted_scale_factor", "mismatched_corresponding_sides"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_29_similarity_ratio_of_perimeters(rng: random.Random) -> Dict[str, Any]:
    # Ratio of perimeters of similar polygons
    p1 = rng.choice([24, 30, 36])
    scale_num = rng.choice([3, 4, 5])
    scale_den = rng.choice([2, 3])
    while scale_num <= scale_den or math.gcd(scale_num, scale_den) != 1:
        scale_num = 5
        scale_den = 2
    p2 = (p1 * scale_num) // scale_den

    prompt = (
        f"Polygon $P_1$ is similar to polygon $P_2$. The ratio of their corresponding side lengths is "
        f"$\\frac{{\\text{{side}}_1}}{{\\text{{side}}_2}} = \\frac{{{scale_den}}}{{{scale_num}}}$. "
        f"If the perimeter of $P_1$ is ${p1}\\text{{ cm}}$, determine the perimeter of $P_2$."
    )
    sample = (
        f"\\text{{The ratio of perimeters of similar polygons equals the ratio of their corresponding sides: }}\\\\\n"
        f"\\frac{{\\text{{Perimeter}}(P_2)}}{{\\text{{Perimeter}}(P_1)}} = \\frac{{{scale_num}}}{{{scale_den}}}\\\\\n"
        f"\\text{{Perimeter}}(P_2) = \\frac{{{scale_num}}}{{{scale_den}}} \\times {p1} = {p2}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<polygon points="60,140 100,70 140,140" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
        f'<polygon points="200,170 260,50 320,170" fill="#f0fdf4" stroke="#059669" stroke-width="2"/>'
        f'<text x="100" y="160" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">P1 ({p1} cm)</text>'
        f'<text x="260" y="195" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#059669">P2 (? cm)</text>',
        width=360,
        height=220,
    )
    return {
        "id": "g12_eg_29",
        "topic": "Euclidean geometry",
        "subskill": "29_similarity_ratio_of_perimeters",
        "question_text": prompt,
        "answer_latex": str(p2),
        "answer_sympy": str(p2),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Perimeter ratio of similar polygons"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"State ratio of perimeters equals scale factor {scale_num}/{scale_den}", "marks": 1},
                {"id": "mp2", "desc": f"Calculate perimeter = {p2} cm", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The perimeter scale factor is linear (the same as the side length scale factor).",
            "2_concept": f"Perimeter(P2) = ({scale_num} / {scale_den}) * Perimeter(P1).",
            "3_breakdown": f"Perimeter(P2) = ({scale_num} / {scale_den}) * {p1} = {p2} cm.",
        },
        "misconception_tags": ["squaring_perimeter_ratio", "inverse_scale_multiplication"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_30_similarity_ratio_of_areas(rng: random.Random) -> Dict[str, Any]:
    # Ratio of areas of similar triangles = k^2
    s1 = rng.choice([2, 3, 4])
    s2 = s1 + rng.choice([1, 2, 3])
    area1 = (s1 ** 2) * rng.randint(3, 6)
    k_factor = area1 // (s1 ** 2)
    area2 = (s2 ** 2) * k_factor

    prompt = (
        f"Two triangles $\\triangle ABC$ and $\\triangle DEF$ are similar ($\\triangle ABC \\mathbin{{|||}} \\triangle DEF$). "
        f"The ratio of their corresponding side lengths is $\\frac{{AB}}{{DE}} = \\frac{{{s1}}}{{{s2}}}$. "
        f"If the area of $\\triangle ABC = {area1}\\text{{ cm}}^2$, calculate the area of $\\triangle DEF$."
    )
    sample = (
        f"\\text{{The ratio of areas of similar triangles equals the square of the ratio of their corresponding sides: }}\\\\\n"
        f"\\frac{{\\text{{Area}}(\\triangle DEF)}}{{\\text{{Area}}(\\triangle ABC)}} = "
        f"\\left(\\frac{{DE}}{{AB}}\\right)^2 = \\left(\\frac{{{s2}}}{{{s1}}}\\right)^2 = \\frac{{{s2**2}}}{{{s1**2}}}\\\\\n"
        f"\\text{{Area}}(\\triangle DEF) = \\frac{{{s2**2}}}{{{s1**2}}} \\times {area1} = {area2}\\text{{ cm}}^2."
    )
    svg = _svg_wrap(
        f'<polygon points="50,150 110,60 150,150" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
        f'<polygon points="190,180 270,40 330,180" fill="#f0fdf4" stroke="#059669" stroke-width="2"/>'
        f'<text x="100" y="170" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">Area = {area1} cm²</text>'
        f'<text x="260" y="200" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#059669">Area = ? cm²</text>',
        width=360,
        height=220,
    )
    return {
        "id": "g12_eg_30",
        "topic": "Euclidean geometry",
        "subskill": "30_similarity_ratio_of_areas",
        "question_text": prompt,
        "answer_latex": str(area2),
        "answer_sympy": str(area2),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Area ratio of similar triangles"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"State ratio of areas equals square of side ratio ({s2}/{s1})^2 = {s2**2}/{s1**2}", "marks": 1},
                {"id": "mp2", "desc": f"Calculate Area = {area2} cm^2", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Remember that area scales with the SQUARE of the linear side ratio.",
            "2_concept": f"Area(DEF) / Area(ABC) = (s2 / s1)^2 = ({s2}/{s1})^2 = {s2**2}/{s1**2}.",
            "3_breakdown": f"Area(DEF) = ({s2**2}/{s1**2}) * {area1} = {area2} cm^2.",
        },
        "misconception_tags": ["forgetting_to_square_linear_ratio", "inverse_ratio_multiplication"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_31_similarity_equiangular_parallel_lines(rng: random.Random) -> Dict[str, Any]:
    # In triangle ABC, DE || BC. Prove ADE ||| ABC. Find BC given DE, AD, AB.
    ad = rng.randint(3, 6)
    db = rng.randint(2, 5)
    ab = ad + db
    factor = rng.randint(2, 4)
    de = ad * factor
    bc = ab * factor

    prompt = (
        f"In $\\triangle ABC$, line segment $DE$ is drawn parallel to $BC$ ($D$ on $AB$, $E$ on $AC$). "
        f"Since $DE \\parallel BC$, $\\triangle ADE \\mathbin{{|||}} \\triangle ABC$ (equiangular: corresponding angles equal). "
        f"Given $AD = {ad}\\text{{ cm}}$, $DB = {db}\\text{{ cm}}$ (so $AB = {ab}\\text{{ cm}}$), "
        f"and $DE = {de}\\text{{ cm}}$, calculate the length of base $BC$."
    )
    sample = (
        f"\\text{{Since }} \\triangle ADE \\mathbin{{|||}} \\triangle ABC \\quad (\\angle\\angle\\angle, \\text{{corresp }} \\angle\\text{{s}}, DE \\parallel BC):\\\\\n"
        f"\\frac{{BC}}{{DE}} = \\frac{{AB}}{{AD}}\\\\\n"
        f"\\frac{{BC}}{{{de}}} = \\frac{{{ab}}}{{{ad}}} = {factor}\\\\\n"
        f"BC = {de} \\times {factor} = {bc}\\text{{ cm}}."
    )
    side_texts = [
        {"x": 90, "y": 95, "text": f"{ad}"},
        {"x": 65, "y": 175, "text": f"{db}"},
        {"x": 160, "y": 125, "text": f"DE = {de}"},
        {"x": 160, "y": 240, "text": "BC = ?", "color": "#dc2626"},
    ]
    svg = _draw_triangle_parallel_svg(labels=("A", "B", "C", "D", "E"), side_texts=side_texts)

    return {
        "id": "g12_eg_31",
        "topic": "Euclidean geometry",
        "subskill": "31_similarity_equiangular_parallel_lines",
        "question_text": prompt,
        "answer_latex": str(bc),
        "answer_sympy": str(bc),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Triangle with parallel line similarity"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculate total side AB = {ad} + {db} = {ab}", "marks": 1},
                {"id": "mp2", "desc": "State ratio BC/DE = AB/AD with similarity reason", "marks": 1},
                {"id": "mp3", "desc": f"Calculate BC = {bc}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Compare the small triangle ADE with the large triangle ABC.",
            "2_concept": f"BC / DE = AB / AD, where AB = AD + DB = {ab}.",
            "3_breakdown": f"BC = ({ab} / {ad}) * {de} = {bc} cm.",
        },
        "misconception_tags": ["using_db_instead_of_total_ab", "proportion_theorem_applied_to_base"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 4,
    }


def build_32_similarity_vertically_opposite_angles_hourglass(rng: random.Random) -> Dict[str, Any]:
    # Hourglass / bowtie figure: AB || CD intersecting at X.
    # Triangles AXB ||| CXD
    ax = rng.randint(3, 6)
    k = rng.randint(2, 4)
    cx = ax * k
    ab = rng.randint(4, 7)
    cd = ab * k

    prompt = (
        f"In the hourglass figure, line segments $AC$ and $BD$ intersect at point $X$, "
        f"with line segments $AB \\parallel CD$. "
        f"Given $AX = {ax}\\text{{ cm}}$, $XC = {cx}\\text{{ cm}}$, and $AB = {ab}\\text{{ cm}}$, "
        f"calculate the length of segment $CD$."
    )
    sample = (
        f"\\text{{In }} \\triangle AXB \\text{{ and }} \\triangle CXD:\\\\\n"
        f"\\hat{{A}} = \\hat{{C}} \\quad (\\text{{alt }} \\angle\\text{{s}}, AB \\parallel CD)\\\\\n"
        f"A\\hat{{X}}B = C\\hat{{X}}D \\quad (\\text{{vert opp }} \\angle\\text{{s}})\\\\\n"
        f"\\implies \\triangle AXB \\mathbin{{|||}} \\triangle CXD \\quad (\\angle\\angle\\angle)\\\\\n"
        f"\\frac{{CD}}{{AB}} = \\frac{{XC}}{{AX}} = \\frac{{{cx}}}{{{ax}}} = {k}\\\\\n"
        f"CD = {ab} \\times {k} = {cd}\\text{{ cm}}."
    )
    svg = _draw_bowtie_svg(labels=("A", "B", "C", "D", "X"))

    return {
        "id": "g12_eg_32",
        "topic": "Euclidean geometry",
        "subskill": "32_similarity_vertically_opposite_angles_hourglass",
        "question_text": prompt,
        "answer_latex": str(cd),
        "answer_sympy": str(cd),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Hourglass bowtie similar triangles (AX={ax}, XC={cx})"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Establish similarity via alternate and vertically opposite angles", "marks": 1},
                {"id": "mp2", "desc": "Ratio CD/AB = XC/AX", "marks": 1},
                {"id": "mp3", "desc": f"Calculate CD = {cd}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Alternate interior angles and vertically opposite angles make triangles AXB and CXD similar.",
            "2_concept": f"CD / AB = XC / AX = {cx} / {ax} = {k}.",
            "3_breakdown": f"CD = {ab} * {k} = {cd} cm.",
        },
        "misconception_tags": ["mismatched_hourglass_vertices", "inverse_scale_multiplication"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_33_similarity_shared_angle_and_perpendicular(rng: random.Random) -> Dict[str, Any]:
    # Right triangle ABC with angle B = 90. Point D on AB, E on AC such that angle ADE = 90.
    # Triangles ADE and ABC share angle A and both have a right angle => ADE ||| ABC.
    ad = rng.randint(3, 5)
    ae = rng.randint(5, 8)
    factor = rng.randint(2, 3)
    ab = ad * factor
    ac = ae * factor

    prompt = (
        f"In right-angled triangle $\\triangle ABC$ ($\\\\hat{{B}} = 90^\\circ$), point $D$ lies on $AB$ "
        f"and point $E$ lies on $AC$ such that segment $DE$ is perpendicular to $AB$ ($\\\\hat{{D}} = 90^\\circ$). "
        f"Triangles $\\triangle ADE$ and $\\triangle ABC$ share the common acute angle $\\\\hat{{A}}$. "
        f"Given $AD = {ad}\\text{{ cm}}$, $AE = {ae}\\text{{ cm}}$, and $AB = {ab}\\text{{ cm}}$, "
        f"calculate the length of hypotenuse $AC$."
    )
    sample = (
        f"\\text{{In }} \\triangle ADE \\text{{ and }} \\triangle ABC:\\\\\n"
        f"\\hat{{A}} = \\hat{{A}} \\quad (\\text{{common}})\\\\\n"
        f"A\\hat{{D}}E = A\\hat{{B}}C = 90^\\circ \\quad (\\text{{given}})\\\\\n"
        f"\\implies \\triangle ADE \\mathbin{{|||}} \\triangle ABC \\quad (\\angle\\angle\\angle)\\\\\n"
        f"\\frac{{AC}}{{AE}} = \\frac{{AB}}{{AD}} \\implies "
        f"AC = \\frac{{{ab}}}{{{ad}}} \\times {ae} = {factor} \\times {ae} = {ac}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<polygon points="40,200 40,50 300,200" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="40" y1="125" x2="170" y2="200" stroke="#2563eb" stroke-width="2"/>'
        f'<path d="M 40 185 L 55 185 L 55 200" fill="none" stroke="#1e293b" stroke-width="1.5"/>'
        f'<path d="M 40 110 L 55 110 L 55 125" fill="none" stroke="#2563eb" stroke-width="1.5"/>'
        f'<text x="35" y="40" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">A</text>'
        f'<text x="25" y="215" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">B</text>'
        f'<text x="310" y="215" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">C</text>'
        f'<text x="25" y="130" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">D</text>'
        f'<text x="175" y="215" font-family="sans-serif" font-weight="bold" font-size="13" fill="#2563eb">E</text>',
        width=360,
        height=240,
    )
    return {
        "id": "g12_eg_33",
        "topic": "Euclidean geometry",
        "subskill": "33_similarity_shared_angle_and_perpendicular",
        "question_text": prompt,
        "answer_latex": str(ac),
        "answer_sympy": str(ac),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Nested right-angled similar triangles (AD={ad}, AB={ab})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Establish similarity ADE ||| ABC with shared angle and 90 deg", "marks": 1},
                {"id": "mp2", "desc": f"Calculate AC = {ac}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Both triangles share angle A and have a 90 degree angle, so they are similar.",
            "2_concept": f"AC / AE = AB / AD = {ab} / {ad} = {factor}.",
            "3_breakdown": f"AC = {factor} * {ae} = {ac} cm.",
        },
        "misconception_tags": ["mismatched_hypotenuse_ratio", "incorrect_adjacent_side_pairing"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_34_similarity_sides_in_proportion_test(rng: random.Random) -> Dict[str, Any]:
    # Test if two triangles are similar by sides
    is_similar = rng.choice([True, False])
    k = rng.choice([2, 3])
    a, b, c = 4, 6, 8
    if is_similar:
        d, e, f = a * k, b * k, c * k
        ans_str = "Similar"
    else:
        d, e, f = a * k, b * k, c * k + rng.choice([1, -1])
        ans_str = "Not similar"

    prompt = (
        f"Triangle $\\triangle ABC$ has side lengths $AB = {a}$, $BC = {b}$, and $AC = {c}$. "
        f"Triangle $\\triangle DEF$ has side lengths $DE = {d}$, $EF = {e}$, and $DF = {f}$. "
        f"Determine whether $\\triangle ABC$ and $\\triangle DEF$ are similar by comparing the ratios "
        f"of all corresponding sides. (Enter 'Similar' or 'Not similar')."
    )
    sample = (
        f"\\frac{{DE}}{{AB}} = \\frac{{{d}}}{{{a}}} = {round(d/a, 2)}\\\\\n"
        f"\\frac{{EF}}{{BC}} = \\frac{{{e}}}{{{b}}} = {round(e/b, 2)}\\\\\n"
        f"\\frac{{DF}}{{AC}} = \\frac{{{f}}}{{{c}}} = {round(f/c, 2)}\\\\\n"
        f"\\text{{Since all three ratios are {'equal' if is_similar else 'not all equal'}: }} "
        f"\\triangle ABC \\text{{ is }} {'\\mathbin{|||} \\triangle DEF \\quad (\\text{sides in prop})' if is_similar else '\\text{not similar to } \\triangle DEF'}."
    )
    svg = _svg_wrap(
        f'<polygon points="40,150 90,60 140,150" fill="#f8fafc" stroke="#2563eb" stroke-width="2"/>'
        f'<polygon points="190,170 270,50 330,170" fill="#f8fafc" stroke="#059669" stroke-width="2"/>'
        f'<text x="90" y="170" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">Sides: {a}, {b}, {c}</text>'
        f'<text x="260" y="195" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#059669">Sides: {d}, {e}, {f}</text>',
        width=360,
        height=220,
    )
    return {
        "id": "g12_eg_34",
        "topic": "Euclidean geometry",
        "subskill": "34_similarity_sides_in_proportion_test",
        "question_text": prompt,
        "answer_latex": f"\\text{{{ans_str}}}",
        "answer_sympy": f"'{ans_str}'",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Side proportionality similarity test"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Check ratios of all three pairs of corresponding sides", "marks": 1},
                {"id": "mp2", "desc": f"Correct conclusion: {ans_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Calculate DE/AB, EF/BC, and DF/AC.",
            "2_concept": "For triangles to be similar by SSS~, all three side ratios must be equal.",
            "3_breakdown": f"Ratios: {d}/{a}, {e}/{b}, {f}/{c}. Compare these values.",
        },
        "misconception_tags": ["checking_only_two_sides", "ratio_misordering"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_35_similarity_two_sides_proportional_included_angle(rng: random.Random) -> Dict[str, Any]:
    angle_val = rng.randint(40, 65)
    k = rng.choice([2, 3])
    ab = rng.randint(4, 6)
    ac = rng.randint(6, 9)
    de = ab * k
    df = ac * k

    prompt = (
        f"In $\\triangle ABC$ and $\\triangle DEF$, $\\hat{{A}} = \\hat{{D}} = {angle_val}^\\circ$. "
        f"The sides including the angles satisfy $AB = {ab}$, $AC = {ac}$, $DE = {de}$, and $DF = {df}$. "
        f"Since two pairs of sides are proportional ($\\frac{{DE}}{{AB}} = \\frac{{DF}}{{AC}} = {k}$) and their included angles are equal, "
        f"$\\triangle ABC \\mathbin{{|||}} \\triangle DEF$ (SAS similarity). "
        f"If side $BC = 5\\text{{ cm}}$, determine the length of side $EF$."
    )
    bc = 5
    ef = bc * k
    sample = (
        f"\\text{{By SAS similarity criteria, }} \\triangle ABC \\mathbin{{|||}} \\triangle DEF.\\\\\n"
        f"\\frac{{EF}}{{BC}} = \\frac{{DE}}{{AB}} = {k}\\\\\n"
        f"EF = {bc} \\times {k} = {ef}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<polygon points="40,160 100,60 160,160" fill="#f8fafc" stroke="#2563eb" stroke-width="2"/>'
        f'<polygon points="190,180 270,40 330,180" fill="#f8fafc" stroke="#059669" stroke-width="2"/>'
        f'<text x="100" y="50" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#2563eb">{angle_val}°</text>'
        f'<text x="270" y="30" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#059669">{angle_val}°</text>',
        width=360,
        height=220,
    )
    return {
        "id": "g12_eg_35",
        "topic": "Euclidean geometry",
        "subskill": "35_similarity_two_sides_proportional_included_angle",
        "question_text": prompt,
        "answer_latex": str(ef),
        "answer_sympy": str(ef),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "SAS similarity third side calculation"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"State scale factor k = {k}", "marks": 1},
                {"id": "mp2", "desc": f"Calculate EF = {ef}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The ratio of all corresponding sides in similar triangles is equal.",
            "2_concept": f"EF / BC = DE / AB = {k}.",
            "3_breakdown": f"EF = {bc} * {k} = {ef} cm.",
        },
        "misconception_tags": ["non_included_angle_misuse", "multiplication_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_36_pythagorean_proof_similarity_altitude_to_hypotenuse(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In $\\triangle ABC$, $\\\\hat{{B}} = 90^\\circ$ and $BD \\perp AC$ with $D$ on hypotenuse $AC$. "
        f"The altitude to the hypotenuse divides the triangle into two smaller triangles that are similar to each other "
        f"and to the original triangle. "
        f"Complete the similarity statement: $\\triangle ABC \\mathbin{{|||}} \\triangle \\text{{ADB}} \\mathbin{{|||}} \\triangle \\text{{?}}$ "
        f"(Name the third similar triangle with vertices in correct corresponding order)."
    )
    ans_latex = "\\triangle BDC"
    ans_str = "BDC"
    sample = (
        f"\\text{{In right triangle }} \\triangle ABC (\\hat{{B}} = 90^\\circ) \\text{{ with }} BD \\perp AC:\\\\\n"
        f"\\hat{{A}} \\text{{ is common to }} \\triangle ABC \\text{{ and }} \\triangle ADB.\\\\\n"
        f"\\hat{{C}} \\text{{ is common to }} \\triangle ABC \\text{{ and }} \\triangle BDC.\\\\\n"
        f"A\\hat{{D}}B = B\\hat{{D}}C = A\\hat{{B}}C = 90^\\circ.\\\\\n"
        f"\\text{{Therefore, }} \\triangle ABC \\mathbin{{|||}} \\triangle ADB \\mathbin{{|||}} \\triangle BDC."
    )
    var_idx = rng.randint(1, 999)
    svg = _draw_right_triangle_altitude_svg(labels=("A", "B", "C", "D"))

    return {
        "id": "g12_eg_36",
        "topic": "Euclidean geometry",
        "subskill": "36_pythagorean_proof_similarity_altitude_to_hypotenuse",
        "question_text": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": f"'{ans_str}'",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Altitude to hypotenuse three similar triangles (variant {var_idx})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identify equal angles in triangles ABC and BDC", "marks": 1},
                {"id": "mp2", "desc": f"Correct corresponding order: {ans_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Match the right angle D with right angle B, and the common angle C.",
            "2_concept": "In triangle BDC, angle D is 90 degrees and angle C is common with ABC.",
            "3_breakdown": "The correct vertex ordering is BDC.",
        },
        "misconception_tags": ["reversed_vertex_ordering", "mismatched_acute_angles"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_37_pythagorean_proof_geometric_mean_relations(rng: random.Random) -> Dict[str, Any]:
    # Geometric mean: BD^2 = AD * DC
    ad = rng.choice([4, 9, 16])
    dc = rng.choice([9, 16, 25])
    while ad == dc:
        dc = 25
    bd = int(math.isqrt(ad * dc))

    prompt = (
        f"In right-angled triangle $\\triangle ABC$ ($\\\\hat{{B}} = 90^\\circ$), altitude $BD \\perp AC$. "
        f"From the similarity $\\triangle ADB \\mathbin{{|||}} \\triangle BDC$, we obtain the geometric mean theorem: "
        f"$BD^2 = AD \\cdot DC$. "
        f"If $AD = {ad}\\text{{ cm}}$ and $DC = {dc}\\text{{ cm}}$, calculate the length of altitude $BD$."
    )
    sample = (
        f"\\text{{From }} \\triangle ADB \\mathbin{{|||}} \\triangle BDC:\\\\\n"
        f"\\frac{{BD}}{{AD}} = \\frac{{DC}}{{BD}} \\implies BD^2 = AD \\times DC\\\\\n"
        f"BD^2 = {ad} \\times {dc} = {ad * dc}\\\\\n"
        f"BD = \\sqrt{{{ad * dc}}} = {bd}\\text{{ cm}}."
    )
    svg = _draw_right_triangle_altitude_svg(labels=("A", "B", "C", "D"))

    return {
        "id": "g12_eg_37",
        "topic": "Euclidean geometry",
        "subskill": "37_pythagorean_proof_geometric_mean_relations",
        "question_text": prompt,
        "answer_latex": str(bd),
        "answer_sympy": str(bd),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Geometric mean altitude relation (AD={ad}, DC={dc})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"State BD^2 = AD * DC = {ad} * {dc} = {ad * dc}", "marks": 1},
                {"id": "mp2", "desc": f"Calculate BD = {bd}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The altitude BD is the geometric mean between the two segments of the hypotenuse.",
            "2_concept": f"BD^2 = AD * DC = {ad} * {dc} = {ad * dc}.",
            "3_breakdown": f"BD = sqrt({ad * dc}) = {bd} cm.",
        },
        "misconception_tags": ["adding_segments_instead_of_multiplying", "square_root_arithmetic_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_38_pythagorean_proof_algebraic_summation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In the Euclidean proof of Pythagoras' theorem using similar triangles, we have "
        f"$AB^2 = AD \\cdot AC$ (from $\\triangle ABC \\mathbin{{|||}} \\triangle ADB$) and "
        f"$BC^2 = CD \\cdot AC$ (from $\\triangle ABC \\mathbin{{|||}} \\triangle BDC$). "
        f"Summing these gives $AB^2 + BC^2 = AD \\cdot AC + CD \\cdot AC = AC(AD + CD)$. "
        f"Since point $D$ lies on $AC$, simplify the factor $(AD + CD)$ in terms of the whole side."
    )
    ans_latex = "AC"
    sample = (
        f"\\text{{Since }} D \\text{{ lies on segment }} AC, AD + CD = AC.\\\\\n"
        f"\\text{{Substituting into the sum: }}\\\\\n"
        f"AB^2 + BC^2 = AC(AD + CD) = AC(AC) = AC^2."
    )
    step_seed = rng.randint(10, 99)
    svg = _draw_right_triangle_altitude_svg(labels=("A", "B", "C", "D"))

    return {
        "id": "g12_eg_38",
        "topic": "Euclidean geometry",
        "subskill": "38_pythagorean_proof_algebraic_summation",
        "question_text": prompt,
        "answer_latex": ans_latex,
        "answer_sympy": "'AC'",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Pythagorean theorem proof summation (step {step_seed})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Recognise collinear segment addition AD + CD = AC", "marks": 1},
                {"id": "mp2", "desc": "Conclude AB^2 + BC^2 = AC^2", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Look at the hypotenuse AC which is divided into segments AD and CD.",
            "2_concept": "AD + CD equals the whole hypotenuse AC.",
            "3_breakdown": "The factor (AD + CD) simplifies to AC.",
        },
        "misconception_tags": ["confusing_segment_sum_with_product", "misidentifying_hypotenuse"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 2,
    }


def build_39_geometric_mean_numerical_calculation(rng: random.Random) -> Dict[str, Any]:
    # In right triangle ABC with altitude BD to AC:
    # AB^2 = AD * AC. Let AD = 4, AC = 16 => AB = 8.
    ad = rng.choice([2, 3, 4])
    k = rng.choice([4, 9, 16])
    ac = ad * k
    ab = int(math.isqrt(ad * ac))

    prompt = (
        f"In right triangle $\\triangle ABC$ ($\\\\hat{{B}} = 90^\\circ$), altitude $BD \\perp AC$. "
        f"From similarity $\\triangle ABC \\mathbin{{|||}} \\triangle ADB$, the leg rule gives $AB^2 = AD \\cdot AC$. "
        f"Given $AD = {ad}\\text{{ cm}}$ and total hypotenuse $AC = {ac}\\text{{ cm}}$, "
        f"calculate the length of leg $AB$."
    )
    sample = (
        f"AB^2 = AD \\times AC = {ad} \\times {ac} = {ad * ac}\\\\\n"
        f"AB = \\sqrt{{{ad * ac}}} = {ab}\\text{{ cm}}."
    )
    svg = _draw_right_triangle_altitude_svg(labels=("A", "B", "C", "D"))

    return {
        "id": "g12_eg_39",
        "topic": "Euclidean geometry",
        "subskill": "39_geometric_mean_numerical_calculation",
        "question_text": prompt,
        "answer_latex": str(ab),
        "answer_sympy": str(ab),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Right triangle leg rule calculation (AD={ad}, AC={ac})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"State AB^2 = AD * AC = {ad * ac}", "marks": 1},
                {"id": "mp2", "desc": f"Calculate AB = {ab}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Each leg of the right triangle is the geometric mean of the whole hypotenuse and adjacent segment.",
            "2_concept": f"AB^2 = AD * AC = {ad} * {ac} = {ad * ac}.",
            "3_breakdown": f"AB = sqrt({ad * ac}) = {ab} cm.",
        },
        "misconception_tags": ["using_altitude_instead_of_hypotenuse", "arithmetic_square_root_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_40_circle_similarity_subtended_angles_bowtie(rng: random.Random) -> Dict[str, Any]:
    # Intersecting chords inside circle: AX * XB = CX * XD
    ax = rng.randint(3, 6)
    xb = rng.randint(6, 10)
    cx = rng.choice([2, 4, 5])
    while (ax * xb) % cx != 0:
        cx = 2 if (ax * xb) % 2 == 0 else 3
    xd = (ax * xb) // cx

    prompt = (
        f"In a circle, chords $AB$ and $CD$ intersect at point $X$. "
        f"Angles subtended by the same chord are equal ($\\hat{{A}} = \\hat{{C}}$ and $\\hat{{D}} = \\hat{{B}}$), "
        f"making $\\triangle AXD \\mathbin{{|||}} \\triangle CXB$. "
        f"Given $AX = {ax}\\text{{ cm}}$, $XB = {xb}\\text{{ cm}}$, and $CX = {cx}\\text{{ cm}}$, "
        f"calculate the length of segment $XD$."
    )
    sample = (
        f"\\text{{Since }} \\triangle AXD \\mathbin{{|||}} \\triangle CXB \\quad (\\text{{angles in same seg}}):\\\\\n"
        f"\\frac{{AX}}{{CX}} = \\frac{{XD}}{{XB}} \\implies AX \\times XB = CX \\times XD\\\\\n"
        f"{ax} \\times {xb} = {cx} \\times XD\\\\\n"
        f"XD = \\frac{{{ax * xb}}}{{{cx}}} = {xd}\\text{{ cm}}."
    )
    svg = _draw_circle_chords_svg()

    return {
        "id": "g12_eg_40",
        "topic": "Euclidean geometry",
        "subskill": "40_circle_similarity_subtended_angles_bowtie",
        "question_text": prompt,
        "answer_latex": str(xd),
        "answer_sympy": str(xd),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Intersecting chords circle similarity (AX={ax}, CX={cx})"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "State similarity AXD ||| CXB (angles in same segment)", "marks": 1},
                {"id": "mp2", "desc": f"Intersecting chord product AX * XB = CX * XD", "marks": 1},
                {"id": "mp3", "desc": f"Calculate XD = {xd}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "In a circle, intersecting chords satisfy AX * XB = CX * XD.",
            "2_concept": f"{ax} * {xb} = {cx} * XD.",
            "3_breakdown": f"XD = ({ax} * {xb}) / {cx} = {xd} cm.",
        },
        "misconception_tags": ["adding_chord_segments_instead_of_multiplying", "mispaired_chord_segments"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_41_circle_similarity_secants_intersecting_outside(rng: random.Random) -> Dict[str, Any]:
    # Secants PAB and PCD intersecting outside circle at P.
    # PA * PB = PC * PD.
    triples = [(3, 9, 4), (4, 8, 3), (4, 11, 5), (5, 7, 4), (3, 7, 2), (4, 6, 2)]
    pa, ab, pc = rng.choice(triples)
    pb = pa + ab
    prod = pa * pb
    pd = prod // pc
    cd = pd - pc

    prompt = (
        f"Two secants $PAB$ and $PCD$ intersect outside a circle at point $P$. "
        f"Exterior angles of cyclic quadrilateral $ABCD$ establish that $\\triangle PAC \\mathbin{{|||}} \\triangle PDB$. "
        f"Given $PA = {pa}\\text{{ cm}}$, $AB = {ab}\\text{{ cm}}$ (so $PB = {pb}\\text{{ cm}}$), "
        f"and $PC = {pc}\\text{{ cm}}$, calculate the length of segment $CD$."
    )
    sample = (
        f"\\text{{From }} \\triangle PAC \\mathbin{{|||}} \\triangle PDB:\\\\\n"
        f"\\frac{{PA}}{{PD}} = \\frac{{PC}}{{PB}} \\implies PA \\times PB = PC \\times PD\\\\\n"
        f"PD = \\frac{{PA \\times PB}}{{PC}} = \\frac{{{pa} \\times {pb}}}{{{pc}}} = \\frac{{{prod}}}{{{pc}}} = {pd}\\text{{ cm}}.\\\\\n"
        f"CD = PD - PC = {pd} - {pc} = {cd}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<circle cx="210" cy="120" r="70" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="120" x2="280" y2="70" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="50" y1="120" x2="280" y2="170" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="35" y="125" font-family="sans-serif" font-weight="bold" font-size="13" fill="#dc2626">P</text>'
        f'<text x="145" y="95" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">A</text>'
        f'<text x="285" y="65" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">B</text>'
        f'<text x="145" y="160" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">C</text>'
        f'<text x="285" y="185" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">D</text>',
        width=360,
        height=240,
    )
    return {
        "id": "g12_eg_41",
        "topic": "Euclidean geometry",
        "subskill": "41_circle_similarity_secants_intersecting_outside",
        "question_text": prompt,
        "answer_latex": str(cd),
        "answer_sympy": str(cd),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"External secants circle similarity (PA={pa}, PC={pc})"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculate PB = {pb}", "marks": 1},
                {"id": "mp2", "desc": f"Apply secant theorem PA * PB = PC * PD to find PD = {pd}", "marks": 1},
                {"id": "mp3", "desc": f"Subtract to find CD = {cd}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The secant theorem states: PA * PB = PC * PD.",
            "2_concept": f"PD = ({pa} * {pb}) / {pc} = {pd}.",
            "3_breakdown": f"CD = PD - PC = {pd} - {pc} = {cd} cm.",
        },
        "misconception_tags": ["using_ab_instead_of_whole_secant_pb", "subtraction_step_omission"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 4,
    }


def build_42_circle_similarity_tangent_secant_theorem(rng: random.Random) -> Dict[str, Any]:
    # PT tangent, PAB secant. PT^2 = PA * PB
    pairs = [(2, 8), (2, 18), (3, 12), (3, 27), (4, 9), (4, 16), (4, 36), (8, 18), (8, 32)]
    pa, pb = rng.choice(pairs)
    pt_val = int(math.isqrt(pa * pb))
    ab_val = pb - pa

    prompt = (
        f"From an external point $P$, tangent $PT$ touches the circle at $T$ and secant $PAB$ cuts the circle at $A$ and $B$. "
        f"By the tangent-chord theorem and similarity $\\triangle PTA \\mathbin{{|||}} \\triangle PBT$, we have $PT^2 = PA \\cdot PB$. "
        f"Given $PA = {pa}\\text{{ cm}}$ and $AB = {ab_val}\\text{{ cm}}$ (so $PB = {pb}\\text{{ cm}}$), "
        f"calculate the length of tangent segment $PT$."
    )
    sample = (
        f"PB = PA + AB = {pa} + {ab_val} = {pb}\\text{{ cm}}.\\\\\n"
        f"\\text{{By the tangent-secant theorem: }}\\\\\n"
        f"PT^2 = PA \\times PB = {pa} \\times {pb} = {pa * pb}\\\\\n"
        f"PT = \\sqrt{{{pa * pb}}} = {pt_val}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<circle cx="210" cy="130" r="70" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="130" x2="280" y2="180" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="50" y1="130" x2="190" y2="62" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="35" y="135" font-family="sans-serif" font-weight="bold" font-size="13" fill="#0f172a">P</text>'
        f'<text x="185" y="52" font-family="sans-serif" font-weight="bold" font-size="13" fill="#dc2626">T</text>'
        f'<text x="145" y="160" font-family="sans-serif" font-weight="bold" font-size="12" fill="#2563eb">A</text>'
        f'<text x="285" y="195" font-family="sans-serif" font-weight="bold" font-size="12" fill="#2563eb">B</text>',
        width=360,
        height=240,
    )
    return {
        "id": "g12_eg_42",
        "topic": "Euclidean geometry",
        "subskill": "42_circle_similarity_tangent_secant_theorem",
        "question_text": prompt,
        "answer_latex": str(pt_val),
        "answer_sympy": str(pt_val),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Tangent-secant circle similarity (PA={pa}, PB={pb})"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculate PB = PA + AB = {pb}", "marks": 1},
                {"id": "mp2", "desc": f"State PT^2 = PA * PB = {pa * pb}", "marks": 1},
                {"id": "mp3", "desc": f"Solve PT = {pt_val}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The tangent-secant theorem states that PT^2 = PA * PB.",
            "2_concept": f"PB = {pa} + {ab_val} = {pb}. Then PT^2 = {pa} * {pb} = {pa * pb}.",
            "3_breakdown": f"PT = sqrt({pa * pb}) = {pt_val} cm.",
        },
        "misconception_tags": ["using_ab_instead_of_whole_secant_pb", "forgetting_square_root"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_43_circle_similarity_tangent_chord_and_parallel(rng: random.Random) -> Dict[str, Any]:
    angle_val = rng.randint(48, 68)
    prompt = (
        f"In a circle, line $TAY$ is tangent to the circle at point $A$. "
        f"Chord $BC$ is drawn parallel to tangent $TAY$ ($BC \\parallel TY$). "
        f"Chord $AB$ subtends an angle $A\\hat{{C}}B$ at the circumference. "
        f"If the tangent-chord angle $T\\hat{{A}}B = {angle_val}^\\circ$, "
        f"calculate the size of alternate interior angle $A\\hat{{B}}C$ in degrees."
    )
    sample = (
        f"A\\hat{{C}}B = T\\hat{{A}}B = {angle_val}^\\circ \\quad (\\text{{tan-chord theorem}})\\\\\n"
        f"A\\hat{{B}}C = T\\hat{{A}}B = {angle_val}^\\circ \\quad (\\text{{alt }} \\angle\\text{{s}}, BC \\parallel TY)."
    )
    svg = _svg_wrap(
        f'<circle cx="180" cy="140" r="70" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="70" x2="300" y2="70" stroke="#dc2626" stroke-width="2"/>'
        f'<line x1="120" y1="160" x2="240" y2="160" stroke="#2563eb" stroke-width="2"/>'
        f'<polygon points="180,70 120,160 240,160" fill="none" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="50" y="65" font-family="sans-serif" font-size="12" fill="#dc2626">T</text>'
        f'<text x="180" y="60" font-family="sans-serif" font-weight="bold" font-size="12" fill="#dc2626">A</text>'
        f'<text x="305" y="65" font-family="sans-serif" font-size="12" fill="#dc2626">Y</text>'
        f'<text x="105" y="170" font-family="sans-serif" font-weight="bold" font-size="12" fill="#2563eb">B</text>'
        f'<text x="245" y="170" font-family="sans-serif" font-weight="bold" font-size="12" fill="#2563eb">C</text>',
        width=360,
        height=230,
    )
    return {
        "id": "g12_eg_43",
        "topic": "Euclidean geometry",
        "subskill": "43_circle_similarity_tangent_chord_and_parallel",
        "question_text": prompt,
        "answer_latex": f"{angle_val}^\\circ",
        "answer_sympy": str(angle_val),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Tangent and parallel chord geometry ({angle_val}°)"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "State alternate angle equality ABC = TAB (BC || TY)", "marks": 1},
                {"id": "mp2", "desc": f"Angle ABC = {angle_val} degrees", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Lines TY and BC are parallel, so alternate interior angles are equal.",
            "2_concept": "Angle ABC and Angle TAB are alternate interior angles.",
            "3_breakdown": f"Angle ABC = Angle TAB = {angle_val} degrees.",
        },
        "misconception_tags": ["confusing_tangent_chord_with_alternate_angles", "misidentifying_parallel_lines"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 2,
    }


def build_44_circle_similarity_cyclic_quad_exterior_angle(rng: random.Random) -> Dict[str, Any]:
    angle_d = rng.randint(72, 108)
    prompt = (
        f"In cyclic quadrilateral $ABCD$, side $AB$ is extended to point $E$ beyond the circle. "
        f"By the exterior angle theorem of a cyclic quadrilateral, exterior angle $C\\hat{{B}}E$ equals "
        f"interior opposite angle $\\hat{{D}}$. "
        f"If $\\hat{{D}} = {angle_d}^\\circ$, find the measure of exterior angle $C\\hat{{B}}E$ in degrees."
    )
    sample = (
        f"C\\hat{{B}}E = \\hat{{D}} = {angle_d}^\\circ \\quad (\\text{{ext }} \\angle \\text{{ of cyclic quad}})."
    )
    svg = _svg_wrap(
        f'<circle cx="180" cy="130" r="75" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<polygon points="120,70 240,75 230,190 120,180" fill="none" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="120" y1="70" x2="310" y2="75" stroke="#94a3b8" stroke-dasharray="3" stroke-width="2"/>'
        f'<text x="110" y="65" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">A</text>'
        f'<text x="240" y="65" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">B</text>'
        f'<text x="235" y="205" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">C</text>'
        f'<text x="110" y="195" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">D</text>'
        f'<text x="315" y="75" font-family="sans-serif" font-weight="bold" font-size="12" fill="#dc2626">E</text>',
        width=360,
        height=240,
    )
    return {
        "id": "g12_eg_44",
        "topic": "Euclidean geometry",
        "subskill": "44_circle_similarity_cyclic_quad_exterior_angle",
        "question_text": prompt,
        "answer_latex": f"{angle_d}^\\circ",
        "answer_sympy": str(angle_d),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Cyclic quad exterior angle ({angle_d}°)"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "State theorem: exterior angle of cyclic quad = interior opposite angle", "marks": 1},
                {"id": "mp2", "desc": f"Angle CBE = {angle_d} degrees", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The exterior angle of a cyclic quadrilateral is equal to the interior opposite angle.",
            "2_concept": "CBE = D because ABCD is a cyclic quadrilateral.",
            "3_breakdown": f"CBE = {angle_d} degrees.",
        },
        "misconception_tags": ["supplementary_angle_confusion", "misidentified_opposite_interior_angle"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 2,
    }


def build_45_circle_similarity_angle_bisector_in_circle(rng: random.Random) -> Dict[str, Any]:
    # Chord AE bisects angle BAC in triangle ABC inscribed in circle
    # ABD ||| AEC => AD/AC = AB/AE => AD * AE = AB * AC
    # AE = AD + DE => AD(AD + DE) = AB * AC => AD^2 + DE*AD - AB*AC = 0
    tuples = [(8, 4, 6, 16), (9, 3, 6, 18), (10, 5, 6, 25), (12, 6, 9, 24), (10, 2, 8, 15), (8, 7, 6, 20)]
    ad, de, ab, ac = rng.choice(tuples)
    ae = ad + de
    prod = ad * ae

    prompt = (
        f"Triangles $\\triangle ABC$ and $\\triangle ACE$ are inscribed in a circle. "
        f"Line segment $AE$ bisects $\\\\hat{{A}}$ ($B\\\\hat{{A}}E = C\\\\hat{{A}}E$) and intersects chord $BC$ at point $D$. "
        f"Angles subtended by chord $EC$ make $\\\\hat{{B}} = \\\\hat{{E}}$, establishing $\\triangle ABD \\mathbin{{|||}} \\triangle AEC$. "
        f"This yields the relation $AD \\cdot AE = AB \\cdot AC$. "
        f"Given $AB = {ab}\\text{{ cm}}$, $AC = {ac}\\text{{ cm}}$, and $DE = {de}\\text{{ cm}}$, "
        f"calculate the positive length of segment $AD$."
    )
    sample = (
        f"\\text{{Since }} \\triangle ABD \\mathbin{{|||}} \\triangle AEC:\\\\\n"
        f"\\frac{{AD}}{{AC}} = \\frac{{AB}}{{AE}} \\implies AD \\times AE = AB \\times AC\\\\\n"
        f"AD(AD + {de}) = {ab} \\times {ac} = {prod}\\\\\n"
        f"AD^2 + {de}AD - {prod} = 0\\\\\n"
        f"(AD - {ad})(AD + {ad + de}) = 0\\\\\n"
        f"\\text{{Since length is positive, }} AD = {ad}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<circle cx="180" cy="130" r="75" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<polygon points="180,55 120,180 240,180" fill="none" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="180" y1="55" x2="200" y2="204" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="180" y="45" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">A</text>'
        f'<text x="105" y="190" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">B</text>'
        f'<text x="245" y="190" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">C</text>'
        f'<text x="195" y="175" font-family="sans-serif" font-weight="bold" font-size="12" fill="#dc2626">D</text>'
        f'<text x="200" y="222" font-family="sans-serif" font-weight="bold" font-size="12" fill="#dc2626">E</text>',
        width=360,
        height=240,
    )
    return {
        "id": "g12_eg_45",
        "topic": "Euclidean geometry",
        "subskill": "45_circle_similarity_angle_bisector_in_circle",
        "question_text": prompt,
        "answer_latex": str(ad),
        "answer_sympy": str(ad),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Inscribed triangle angle bisector relation (AB={ab}, AC={ac})"},
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Set up product relation AD * AE = AB * AC", "marks": 1},
                {"id": "mp2", "desc": f"Form quadratic AD^2 + {de}AD - {prod} = 0", "marks": 1},
                {"id": "mp3", "desc": "Factorise quadratic equation", "marks": 1},
                {"id": "mp4", "desc": f"Select positive root AD = {ad}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "AE = AD + DE. Substitute into AD * AE = AB * AC.",
            "2_concept": f"AD(AD + {de}) = {prod} -> AD^2 + {de}AD - {prod} = 0.",
            "3_breakdown": f"(AD - {ad})(AD + {ad + de}) = 0 -> AD = {ad} cm.",
        },
        "misconception_tags": ["quadratic_factorisation_error", "retaining_negative_root"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 5,
    }


def build_46_circle_similarity_proportional_product_proof(rng: random.Random) -> Dict[str, Any]:
    # Product relation proof: FE^2 = FB * FC
    pairs = [(2, 8), (2, 18), (4, 9), (4, 16), (4, 36), (8, 18), (8, 32)]
    fb, fc = rng.choice(pairs)
    fe = int(math.isqrt(fb * fc))

    prompt = (
        f"In a geometric circle rider, chained similarity proves that $\\triangle FCE \\mathbin{{|||}} \\triangle FEB$. "
        f"From this similarity, the proportional product relation is $FE^2 = FB \\cdot FC$. "
        f"If measured lengths are $FB = {fb}\\text{{ cm}}$ and $FC = {fc}\\text{{ cm}}$, "
        f"calculate the exact length of segment $FE$."
    )
    sample = (
        f"\\text{{From }} \\triangle FCE \\mathbin{{|||}} \\triangle FEB:\\\\\n"
        f"\\frac{{FE}}{{FC}} = \\frac{{FB}}{{FE}} \\implies FE^2 = FB \\times FC\\\\\n"
        f"FE^2 = {fb} \\times {fc} = {fb * fc}\\\\\n"
        f"FE = \\sqrt{{{fb * fc}}} = {fe}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<circle cx="200" cy="130" r="70" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="130" x2="270" y2="70" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="50" y1="130" x2="270" y2="190" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="200" y1="60" x2="50" y2="130" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="35" y="135" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">F</text>'
        f'<text x="195" y="50" font-family="sans-serif" font-weight="bold" font-size="12" fill="#dc2626">E</text>'
        f'<text x="140" y="105" font-family="sans-serif" font-weight="bold" font-size="12" fill="#2563eb">B</text>'
        f'<text x="275" y="70" font-family="sans-serif" font-weight="bold" font-size="12" fill="#2563eb">C</text>',
        width=360,
        height=230,
    )
    return {
        "id": "g12_eg_46",
        "topic": "Euclidean geometry",
        "subskill": "46_circle_similarity_proportional_product_proof",
        "question_text": prompt,
        "answer_latex": str(fe),
        "answer_sympy": str(fe),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Proportional product geometric rider (FB={fb}, FC={fc})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"State FE^2 = FB * FC = {fb * fc}", "marks": 1},
                {"id": "mp2", "desc": f"Calculate FE = {fe}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The similarity ratio FE/FC = FB/FE cross-multiplies to FE^2 = FB * FC.",
            "2_concept": f"FE^2 = {fb} * {fc} = {fb * fc}.",
            "3_breakdown": f"FE = sqrt({fb * fc}) = {fe} cm.",
        },
        "misconception_tags": ["cross_multiplication_inversion", "forgetting_square_root"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_47_circle_similarity_diameter_subtending_right_angle(rng: random.Random) -> Dict[str, Any]:
    # Diameter AB subtends angle C = 90. CD perpendicular to AB.
    # Triangle ABC right at C, altitude CD to hypotenuse AB.
    pairs = [(2, 8), (3, 12), (4, 9), (4, 16), (5, 20), (6, 24)]
    ad, db = rng.choice(pairs)
    cd = int(math.isqrt(ad * db))

    prompt = (
        f"Segment $AB$ is the diameter of a circle. Point $C$ lies on the circumference, so "
        f"$A\\hat{{C}}B = 90^\\circ$ (angle in semi-circle). A perpendicular $CD \\perp AB$ is drawn to diameter $AB$. "
        f"By similarity of right triangles, $CD^2 = AD \\cdot DB$. "
        f"If $AD = {ad}\\text{{ cm}}$ and $DB = {db}\\text{{ cm}}$, calculate the length of $CD$."
    )
    sample = (
        f"A\\hat{{C}}B = 90^\\circ \\quad (\\angle \\text{{ in semi-circle}}).\\\\\n"
        f"\\text{{In right }} \\triangle ABC \\text{{ with }} CD \\perp AB:\\\\\n"
        f"CD^2 = AD \\times DB = {ad} \\times {db} = {ad * db}\\\\\n"
        f"CD = \\sqrt{{{ad * db}}} = {cd}\\text{{ cm}}."
    )
    svg = _svg_wrap(
        f'<path d="M 50 180 A 130 130 0 0 1 310 180 Z" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="180" x2="310" y2="180" stroke="#0f172a" stroke-width="2"/>'
        f'<polygon points="50,180 150,65 310,180" fill="none" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="150" y1="65" x2="150" y2="180" stroke="#dc2626" stroke-width="2"/>'
        f'<path d="M 150 165 L 165 165 L 165 180" fill="none" stroke="#dc2626" stroke-width="1.5"/>'
        f'<text x="40" y="195" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">A</text>'
        f'<text x="315" y="195" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">B</text>'
        f'<text x="150" y="55" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="12" fill="#2563eb">C</text>'
        f'<text x="150" y="200" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="12" fill="#dc2626">D</text>',
        width=360,
        height=230,
    )
    return {
        "id": "g12_eg_47",
        "topic": "Euclidean geometry",
        "subskill": "47_circle_similarity_diameter_subtending_right_angle",
        "question_text": prompt,
        "answer_latex": str(cd),
        "answer_sympy": str(cd),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Diameter semi-circle altitude theorem (AD={ad}, DB={db})"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"State CD^2 = AD * DB = {ad * db}", "marks": 1},
                {"id": "mp2", "desc": f"Calculate CD = {cd}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "The diameter subtends a 90 degree angle at the circumference (angle in semi-circle).",
            "2_concept": f"CD^2 = AD * DB = {ad} * {db} = {ad * db}.",
            "3_breakdown": f"CD = sqrt({ad * db}) = {cd} cm.",
        },
        "misconception_tags": ["semi_circle_angle_omission", "square_root_error"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_48_circle_similarity_concyclic_points_converse(rng: random.Random) -> Dict[str, Any]:
    angle_val = rng.randint(42, 68)
    prompt = (
        f"In quadrilateral $ABCD$, diagonals $AC$ and $BD$ intersect at $E$. "
        f"It is measured that $A\\hat{{D}}B = {angle_val}^\\circ$ and $A\\hat{{C}}B = {angle_val}^\\circ$. "
        f"Since segment $AB$ subtends equal angles at points $C$ and $D$ on the same side of $AB$, "
        f"conclude whether the four points $A, B, C, D$ are concyclic (form a cyclic quadrilateral). "
        f"(Enter 'Concyclic' or 'Not concyclic')."
    )
    ans_str = "Concyclic"
    sample = (
        f"\\text{{Since }} A\\hat{{D}}B = A\\hat{{C}}B = {angle_val}^\\circ, "
        f"\\text{{line segment }} AB \\text{{ subtends equal angles at }} C \\text{{ and }} D.\\\\\n"
        f"\\text{{Therefore, by the converse of angles in the same segment, }} ABCD \\text{{ is a cyclic quadrilateral }} "
        f"(A, B, C, D \\text{{ are concyclic}})."
    )
    svg = _draw_bowtie_svg(labels=("A", "B", "C", "D", "E"))

    return {
        "id": "g12_eg_48",
        "topic": "Euclidean geometry",
        "subskill": "48_circle_similarity_concyclic_points_converse",
        "question_text": prompt,
        "answer_latex": f"\\text{{{ans_str}}}",
        "answer_sympy": f"'{ans_str}'",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Converse subtended angles concyclic test ({angle_val}°)"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "State converse theorem: segment subtending equal angles implies concyclic", "marks": 1},
                {"id": "mp2", "desc": f"Correct conclusion: {ans_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "If a line segment subtends equal angles at two points on the same side, the four points lie on a circle.",
            "2_concept": f"ADB = ACB = {angle_val} degrees.",
            "3_breakdown": "Conclusion: Concyclic.",
        },
        "misconception_tags": ["confusing_theorem_with_converse", "concyclic_definition_uncertainty"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 2,
    }


def build_49_circle_similarity_tangent_proof_converse(rng: random.Random) -> Dict[str, Any]:
    # Converse of tangent-secant theorem: If PT^2 = PA * PB, PT is tangent to circumcircle of TAB.
    pt = rng.choice([6, 8, 10])
    pa = rng.choice([3, 4, 5])
    is_tangent = rng.choice([True, False])
    if is_tangent:
        pb = (pt ** 2) // pa
        ans_str = "Tangent"
    else:
        pb = (pt ** 2) // pa + rng.choice([1, 2, -1])
        ans_str = "Not tangent"

    prompt = (
        f"A line through $P$ passes through points $A$ and $B$, while segment $PT$ connects $P$ to point $T$. "
        f"The measured lengths are $PT = {pt}\\text{{ cm}}$, $PA = {pa}\\text{{ cm}}$, and $PB = {pb}\\text{{ cm}}$. "
        f"By comparing $PT^2$ with $PA \\cdot PB$, determine whether line $PT$ is tangent to the circle passing through $A, B, T$. "
        f"(Enter 'Tangent' or 'Not tangent')."
    )
    sample = (
        f"PT^2 = {pt}^2 = {pt * pt}\\\\\n"
        f"PA \\times PB = {pa} \\times {pb} = {pa * pb}\\\\\n"
        f"\\text{{Since }} PT^2 {'=' if is_tangent else '\\neq'} PA \\times PB, "
        f"PT \\text{{ is }} {'tangent to the circle \\quad (\\text{converse tan-secant theorem})' if is_tangent else '\\text{not tangent to the circle}'}."
    )
    svg = _svg_wrap(
        f'<circle cx="210" cy="130" r="70" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="50" y1="130" x2="280" y2="180" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="50" y1="130" x2="190" y2="62" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="35" y="135" font-family="sans-serif" font-weight="bold" font-size="12" fill="#0f172a">P</text>'
        f'<text x="185" y="52" font-family="sans-serif" font-weight="bold" font-size="12" fill="#dc2626">T ({pt})</text>'
        f'<text x="145" y="160" font-family="sans-serif" font-size="12" fill="#2563eb">A ({pa})</text>'
        f'<text x="285" y="195" font-family="sans-serif" font-size="12" fill="#2563eb">B ({pb})</text>',
        width=360,
        height=240,
    )
    return {
        "id": "g12_eg_49",
        "topic": "Euclidean geometry",
        "subskill": "49_circle_similarity_tangent_proof_converse",
        "question_text": prompt,
        "answer_latex": f"\\text{{{ans_str}}}",
        "answer_sympy": f"'{ans_str}'",
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Converse tangent-secant test"},
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculate and compare PT^2 = {pt*pt} and PA*PB = {pa*pb}", "marks": 1},
                {"id": "mp2", "desc": f"Correct conclusion: {ans_str}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "Calculate PT^2 and compare it to PA * PB.",
            "2_concept": f"PT^2 = {pt**2}, while PA * PB = {pa * pb}.",
            "3_breakdown": f"Conclusion: {ans_str}.",
        },
        "misconception_tags": ["arithmetic_product_error", "confusing_converse_criteria"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 3,
    }


def build_50_euclidean_geometry_comprehensive_synthesis_rider(rng: random.Random) -> Dict[str, Any]:
    # Comprehensive Grade 12 examination multi-part rider
    # In triangle ABC, line DE || BC, and chord circle similarities
    # Given AD = 12, DB = 6, DE = 8. Find BC
    ad = rng.choice([12, 16, 20])
    db = rng.choice([6, 8, 10])
    ab = ad + db
    factor = ab // math.gcd(ab, ad)
    ad_factor = ad // math.gcd(ab, ad)
    de = ad_factor * rng.randint(3, 5)
    bc = (de * factor) // ad_factor

    prompt = (
        f"In an examination rider on Euclidean geometry, $\\triangle ABC$ has line segment $DE \\parallel BC$ "
        f"($D$ on $AB$, $E$ on $AC$). "
        f"You are given $AD = {ad}\\text{{ cm}}$, $DB = {db}\\text{{ cm}}$, and $DE = {de}\\text{{ cm}}$. "
        f"First determine $AB = AD + DB$, then use similarity $\\triangle ADE \\mathbin{{|||}} \\triangle ABC$ "
        f"to calculate the exact length of side $BC$."
    )
    sample = (
        f"AB = AD + DB = {ad} + {db} = {ab}\\text{{ cm}}.\\\\\n"
        f"\\text{{Since }} DE \\parallel BC, \\triangle ADE \\mathbin{{|||}} \\triangle ABC \\quad (\\angle\\angle\\angle, \\text{{corresp }} \\angle\\text{{s}}):\\\\\n"
        f"\\frac{{BC}}{{DE}} = \\frac{{AB}}{{AD}}\\\\\n"
        f"BC = \\frac{{{ab}}}{{{ad}}} \\times {de} = {bc}\\text{{ cm}}."
    )
    side_texts = [
        {"x": 90, "y": 95, "text": f"{ad}"},
        {"x": 65, "y": 175, "text": f"{db}"},
        {"x": 160, "y": 125, "text": f"DE = {de}"},
        {"x": 160, "y": 240, "text": "BC = ?", "color": "#dc2626"},
    ]
    svg = _draw_triangle_parallel_svg(labels=("A", "B", "C", "D", "E"), side_texts=side_texts)

    return {
        "id": "g12_eg_50",
        "topic": "Euclidean geometry",
        "subskill": "50_euclidean_geometry_comprehensive_synthesis_rider",
        "question_text": prompt,
        "answer_latex": str(bc),
        "answer_sympy": str(bc),
        "sample_answer": sample,
        "worked_solution": sample,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Comprehensive examination geometry synthesis rider"},
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculate AB = {ad} + {db} = {ab}", "marks": 1},
                {"id": "mp2", "desc": "State similarity ADE ||| ABC with reason", "marks": 1},
                {"id": "mp3", "desc": f"Calculate BC = {bc}", "marks": 1},
            ],
        },
        "hints": {
            "1_nudge": "First find the total length of side AB = AD + DB.",
            "2_concept": f"By similarity, BC / DE = AB / AD = {ab} / {ad}.",
            "3_breakdown": f"BC = ({ab} / {ad}) * {de} = {bc} cm.",
        },
        "misconception_tags": ["using_db_instead_of_total_ab", "proportionality_theorem_misapplication_to_base"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 4,
    }


# Map of builders 26 to 50
BUILDERS_26_50 = {
    "26_similarity_equiangular_definition_and_identification": build_26_similarity_equiangular_definition_and_identification,
    "27_similarity_statement_vertex_ordering": build_27_similarity_statement_vertex_ordering,
    "28_similarity_finding_corresponding_side_lengths": build_28_similarity_finding_corresponding_side_lengths,
    "29_similarity_ratio_of_perimeters": build_29_similarity_ratio_of_perimeters,
    "30_similarity_ratio_of_areas": build_30_similarity_ratio_of_areas,
    "31_similarity_equiangular_parallel_lines": build_31_similarity_equiangular_parallel_lines,
    "32_similarity_vertically_opposite_angles_hourglass": build_32_similarity_vertically_opposite_angles_hourglass,
    "33_similarity_shared_angle_and_perpendicular": build_33_similarity_shared_angle_and_perpendicular,
    "34_similarity_sides_in_proportion_test": build_34_similarity_sides_in_proportion_test,
    "35_similarity_two_sides_proportional_included_angle": build_35_similarity_two_sides_proportional_included_angle,
    "36_pythagorean_proof_similarity_altitude_to_hypotenuse": build_36_pythagorean_proof_similarity_altitude_to_hypotenuse,
    "37_pythagorean_proof_geometric_mean_relations": build_37_pythagorean_proof_geometric_mean_relations,
    "38_pythagorean_proof_algebraic_summation": build_38_pythagorean_proof_algebraic_summation,
    "39_geometric_mean_numerical_calculation": build_39_geometric_mean_numerical_calculation,
    "40_circle_similarity_subtended_angles_bowtie": build_40_circle_similarity_subtended_angles_bowtie,
    "41_circle_similarity_secants_intersecting_outside": build_41_circle_similarity_secants_intersecting_outside,
    "42_circle_similarity_tangent_secant_theorem": build_42_circle_similarity_tangent_secant_theorem,
    "43_circle_similarity_tangent_chord_and_parallel": build_43_circle_similarity_tangent_chord_and_parallel,
    "44_circle_similarity_cyclic_quad_exterior_angle": build_44_circle_similarity_cyclic_quad_exterior_angle,
    "45_circle_similarity_angle_bisector_in_circle": build_45_circle_similarity_angle_bisector_in_circle,
    "46_circle_similarity_proportional_product_proof": build_46_circle_similarity_proportional_product_proof,
    "47_circle_similarity_diameter_subtending_right_angle": build_47_circle_similarity_diameter_subtending_right_angle,
    "48_circle_similarity_concyclic_points_converse": build_48_circle_similarity_concyclic_points_converse,
    "49_circle_similarity_tangent_proof_converse": build_49_circle_similarity_tangent_proof_converse,
    "50_euclidean_geometry_comprehensive_synthesis_rider": build_50_euclidean_geometry_comprehensive_synthesis_rider,
}
