"""Grade 11 Mathematics — Euclidean Geometry (Circle Geometry): Archetypes 01 to 25.

Grounded strictly in:
- curriculum_docs/Mathematics_Gr11/Term_3/Euclidean geometry.md
- curriculum_docs_auto/Mathematics_Gr11/Term 3/03. Euclidean geometry.md
- Official South African National Curriculum Standards for Grade 11 Mathematics Paper 2.

Zero-LLM, 100% deterministic Python & SymPy calculations with South African comma decimals ({,})
and dynamic seed-varied inline SVG circle geometry figures.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from app.utils.grade11_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    num,
    rng,
    solution_graph,
    step,
    to_latex,
)

TOPIC_NAME = "Euclidean geometry"
TOPIC_ID = "grade11_math_circle_geometry"
LEARNING_OBJECTIVE_ID = "math11_circle_geometry"

# --------------------------------------------------------------------------- #
# Dynamic 2D Circle Geometry SVG Renderer (Surface 1)
# --------------------------------------------------------------------------- #
def _pt_on_circle(deg: float, cx: float = 210.0, cy: float = 155.0, r: float = 92.0) -> Tuple[float, float]:
    rad = math.radians(deg)
    return (round(cx + r * math.cos(rad), 1), round(cy + r * math.sin(rad), 1))

def circle_geo_svg(
    title: str,
    points: Dict[str, Tuple[float, float]],
    segments: List[Tuple[str, str]],
    labels: Optional[Dict[str, str]] = None,
    callouts: Optional[List[Tuple[float, float, str, str]]] = None,
    right_angle_at: Optional[Tuple[float, float]] = None,
    dashed_segments: Optional[List[Tuple[str, str]]] = None,
    show_center: bool = True,
) -> Dict[str, Any]:
    """Build a crisp, seed-varied inline SVG diagram_spec for Circle Geometry."""
    cx, cy, rad = 210.0, 155.0, 92.0
    parts: List[str] = [
        '<svg viewBox="0 0 420 310" xmlns="http://www.w3.org/2000/svg" '
        'style="width:100%;max-width:440px;height:auto;font-family:system-ui,-apple-system,sans-serif;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">',
        f'<text x="210" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#1e293b">{title}</text>',
        f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>',
    ]

    if dashed_segments:
        for p1, p2 in dashed_segments:
            if p1 in points and p2 in points:
                x1, y1 = points[p1]
                x2, y2 = points[p2]
                parts.append(
                    f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#64748b" stroke-width="1.6" stroke-dasharray="5,4"/>'
                )

    for p1, p2 in segments:
        if p1 in points and p2 in points:
            x1, y1 = points[p1]
            x2, y2 = points[p2]
            parts.append(
                f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0f172a" stroke-width="2"/>'
            )

    if right_angle_at is not None:
        rx, ry = right_angle_at
        parts.append(
            f'<rect x="{round(rx, 1)}" y="{round(ry - 9, 1)}" width="9" height="9" fill="none" stroke="#dc2626" stroke-width="1.5"/>'
        )

    if show_center and "O" in points:
        ox, oy = points["O"]
        parts.append(f'<circle cx="{ox}" cy="{oy}" r="3.5" fill="#dc2626"/>')

    lbl_map = labels or {k: k for k in points}
    for name, (px, py) in points.items():
        parts.append(f'<circle cx="{px}" cy="{py}" r="3" fill="#0f172a"/>')
        dx = px - cx
        dy = py - cy
        dist = math.hypot(dx, dy)
        if dist < 8:
            lx, ly = px - 12, py - 8
        else:
            lx = round(px + (dx / dist) * 16, 1)
            ly = round(py + (dy / dist) * 16 + 4, 1)
        txt = lbl_map.get(name, name)
        parts.append(
            f'<text x="{lx}" y="{ly}" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">{txt}</text>'
        )

    if callouts:
        for tx, ty, text_val, color in callouts:
            parts.append(
                f'<text x="{round(tx, 1)}" y="{round(ty, 1)}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{color}">{text_val}</text>'
            )

    parts.append("</svg>")
    return {
        "kind": "inline_svg",
        "svg": "".join(parts),
        "title": title,
        "diagram_role": "context",
    }

# 01. Perpendicular from Centre to Chord Bisects Chord
def arch_01_chord_perp_from_centre_bisects_chord(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    half_len = r.randint(6, 24)
    full_len = 2 * half_len
    ask_half = r.choice([True, False])

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(40),
    }
    pts["M"] = (round((pts["A"][0] + pts["B"][0]) / 2, 1), round((pts["A"][1] + pts["B"][1]) / 2, 1))

    if ask_half:
        prompt = (
            f"In the circle with centre $O$, $OM \\perp AB$ at point $M$ on chord $AB$. "
            f"If the total length of chord $AB = {full_len}\\text{{ cm}}$, determine the length of $AM$ "
            f"and state the geometric reason."
        )
        ans_val = half_len
        ans_latex = rf"{half_len}\text{{ cm}}"
        step_str = rf"AM = \frac{{1}}{{2}} AB = \frac{{1}}{{2}}({full_len}) = {half_len}\text{{ cm}}"
        callout_txt = f"AB = {full_len} cm, AM = ?"
    else:
        prompt = (
            f"In the circle with centre $O$, line segment $OM$ is drawn from the centre perpendicular to chord $AB$ at $M$. "
            f"If $AM = {half_len}\\text{{ cm}}$, calculate the total length of chord $AB$ and state the geometric reason."
        )
        ans_val = full_len
        ans_latex = rf"{full_len}\text{{ cm}}"
        step_str = rf"AB = 2 \times AM = 2({half_len}) = {full_len}\text{{ cm}}"
        callout_txt = f"AM = {half_len} cm, AB = ?"

    diag = circle_geo_svg(
        title=f"Circle Centre O with OM ⊥ Chord AB ({callout_txt})",
        points=pts,
        segments=[("O", "M"), ("A", "B")],
        dashed_segments=[("O", "A"), ("O", "B")],
        right_angle_at=pts["M"],
        callouts=[(210, 288, callout_txt, "#1d4ed8")],
    )

    steps = [
        step(from_latex=r"OM \perp AB", to_latex_str=r"AM = MB \quad (\text{line from centre } \perp \text{ to chord})", op="apply perpendicular from centre to chord theorem", rule="line from centre perpendicular to chord bisects chord",),
        step(from_latex=r"AM = MB", to_latex_str=step_str, op="calculate chord length", rule="arithmetic",),
    ]
    canonical = solution_graph(goal="determine chord segment using Theorem 1", steps=steps, final_latex=ans_latex)

    return make_math_question(
        prefix="g11_cg_01",
        topic=TOPIC_NAME,
        subskill="01_chord_perp_from_centre_bisects_chord",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_01",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        answer_sympy=str(ans_val),
        sample_answer=rf"{step_str} \quad (\text{{line from centre }} \perp \text{{ to chord}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct length {ans_val} cm", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct reason: line from centre perp to chord", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Recall what a line drawn from the centre of a circle perpendicular to a chord does to the chord.",
            "2_concept": "A perpendicular drawn from the centre of a circle to a chord bisects the chord ($AM = MB$).",
            "3_breakdown": f"${step_str}$ (line from centre $\\perp$ to chord).",
        },
        misconception_tags=["omitted_geometric_reason", "chord_bisector_halving_vs_doubling"],
        keywords=["circle geometry", "chord", "perpendicular from centre"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_01_chord_perp_from_centre_bisects_chord",
        difficulty=difficulty,
    )

# 02. Chord & Pythagoras — Find Radius OA
def arch_02_chord_pythagoras_find_radius(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20), (7, 24, 25)]
    op_len, ap_len, oa_radius = r.choice(triples)
    scale = r.choice([1, 2])
    op_len *= scale
    ap_len *= scale
    oa_radius *= scale
    ab_len = 2 * ap_len

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(142),
        "B": _pt_on_circle(38),
    }
    pts["P"] = (round((pts["A"][0] + pts["B"][0]) / 2, 1), round((pts["A"][1] + pts["B"][1]) / 2, 1))

    prompt = (
        f"In the circle with centre $O$, $OP \\perp AB$ at point $P$ on chord $AB$. "
        f"It is given that chord $AB = {ab_len}\\text{{ mm}}$ and $OP = {op_len}\\text{{ mm}}$. "
        f"Calculate the length of the radius $OA$, stating all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Chord AB = {ab_len} mm, OP = {op_len} mm — Find Radius OA",
        points=pts,
        segments=[("O", "P"), ("A", "B"), ("O", "A")],
        right_angle_at=pts["P"],
        callouts=[(168, 185, f"OP={op_len}", "#1d4ed8"), (210, 290, f"AB = {ab_len} mm, OA = r = ?", "#0f172a")],
    )

    steps = [
        step(from_latex=rf"AB = {ab_len}\text{{ mm}}, \; OP \perp AB", to_latex_str=rf"AP = \frac{{1}}{{2}}({ab_len}) = {ap_len}\text{{ mm}} \quad (\text{{line from centre }} \perp \text{{ to chord}})", op="halve the chord", rule="line from centre perpendicular to chord",),
        step(from_latex=r"OA^2 = OP^2 + AP^2", to_latex_str=rf"OA^2 = {op_len}^2 + {ap_len}^2 = {op_len**2 + ap_len**2} \quad (\text{{Pythagoras}})", op="apply Theorem of Pythagoras in right-angled triangle OAP", rule="Pythagoras",),
        step(from_latex=rf"OA = \sqrt{{{op_len**2 + ap_len**2}}}", to_latex_str=rf"OA = {oa_radius}\text{{ mm}}", op="take positive square root", rule="square root",),
    ]
    canonical = solution_graph(goal="calculate radius OA using chord bisector and Pythagoras", steps=steps, final_latex=rf"{oa_radius}\text{{ mm}}")

    return make_math_question(
        prefix="g11_cg_02",
        topic=TOPIC_NAME,
        subskill="02_chord_pythagoras_find_radius",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_02",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{oa_radius}\text{{ mm}}",
        answer_sympy=str(oa_radius),
        sample_answer=rf"AP = {ap_len}\text{{ mm (line from centre }}\perp\text{{ to chord)}}; \; OA = \sqrt{{{op_len}^2 + {ap_len}^2}} = {oa_radius}\text{{ mm (Pythagoras)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"AP = {ap_len} mm with reason (line from centre perp to chord)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Pythagoras substitution OA^2 = {op_len}^2 + {ap_len}^2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Radius OA = {oa_radius} mm", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "First find the half-chord $AP$ using the perpendicular from centre theorem, then use Pythagoras in $\\triangle OAP$.",
            "2_concept": "$AP = \\frac{1}{2}AB$ (line from centre $\\perp$ to chord) and $OA^2 = OP^2 + AP^2$ (Pythagoras).",
            "3_breakdown": f"$AP = {ap_len}\\text{{ mm}}$, so $OA = \\sqrt{{{op_len}^2 + {ap_len}^2}} = {oa_radius}\\text{{ mm}}$.",
        },
        misconception_tags=["used_full_chord_in_pythagoras", "omitted_geometric_reason"],
        keywords=["circle geometry", "chord", "Pythagoras", "radius"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_02_chord_pythagoras_find_radius",
        difficulty=difficulty,
    )

# 03. Chord & Pythagoras — Find Full Chord Length AB
def arch_03_chord_pythagoras_find_chord_length(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20), (15, 20, 25)]
    op_len, ap_len, oa_radius = r.choice(triples)
    scale = r.choice([1, 2, 3])
    op_len *= scale
    ap_len *= scale
    oa_radius *= scale
    ab_len = 2 * ap_len

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(35),
    }
    pts["P"] = (round((pts["A"][0] + pts["B"][0]) / 2, 1), round((pts["A"][1] + pts["B"][1]) / 2, 1))

    prompt = (
        f"A circle with centre $O$ has a radius $OA = {oa_radius}\\text{{ cm}}$. "
        f"A perpendicular $OP$ of length ${op_len}\\text{{ cm}}$ is drawn from $O$ to chord $AB$ at $P$. "
        f"Calculate the full length of chord $AB$. Provide complete geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Radius OA = {oa_radius} cm, OP = {op_len} cm — Find Chord AB",
        points=pts,
        segments=[("O", "P"), ("A", "B"), ("O", "A")],
        right_angle_at=pts["P"],
        callouts=[(160, 175, f"r={oa_radius}", "#dc2626"), (232, 185, f"OP={op_len}", "#1d4ed8"), (210, 290, "Find AB", "#0f172a")],
    )

    steps = [
        step(from_latex=r"AP^2 = OA^2 - OP^2", to_latex_str=rf"AP^2 = {oa_radius}^2 - {op_len}^2 = {ap_len**2} \implies AP = {ap_len}\text{{ cm}} \quad (\text{{Pythagoras}})", op="find half-chord AP by Pythagoras", rule="Pythagoras",),
        step(from_latex=r"AB = 2 \times AP", to_latex_str=rf"AB = 2({ap_len}) = {ab_len}\text{{ cm}} \quad (\text{{line from centre }} \perp \text{{ to chord}})", op="double AP to find full chord AB", rule="line from centre perpendicular to chord",),
    ]
    canonical = solution_graph(goal="find full chord length AB", steps=steps, final_latex=rf"{ab_len}\text{{ cm}}")

    return make_math_question(
        prefix="g11_cg_03",
        topic=TOPIC_NAME,
        subskill="03_chord_pythagoras_find_chord_length",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_03",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ab_len}\text{{ cm}}",
        answer_sympy=str(ab_len),
        sample_answer=rf"AP = \sqrt{{{oa_radius}^2 - {op_len}^2}} = {ap_len}\text{{ cm (Pythagoras)}}; \; AB = 2({ap_len}) = {ab_len}\text{{ cm (line from centre }}\perp\text{{ to chord)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"AP = {ap_len} cm using Pythagoras", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: line from centre perp to chord bisects chord", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Full chord AB = {ab_len} cm", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Use Pythagoras in right-angled $\\triangle OAP$ to find $AP$, then double your answer for $AB$.",
            "2_concept": "$AP = \\sqrt{OA^2 - OP^2}$ and $AB = 2 \\cdot AP$ (line from centre $\\perp$ to chord).",
            "3_breakdown": f"$AP = {ap_len}\\text{{ cm}}$, so $AB = 2 \\times {ap_len} = {ab_len}\\text{{ cm}}$.",
        },
        misconception_tags=["forgot_to_double_half_chord", "added_hypotenuse_squared"],
        keywords=["circle geometry", "chord length", "Pythagoras"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_03_chord_pythagoras_find_chord_length",
        difficulty=difficulty,
    )

# 04. Chord & Pythagoras — Find Perpendicular Distance OP
def arch_04_chord_pythagoras_find_perp_distance(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (7, 24, 25)]
    op_len, ap_len, oa_radius = r.choice(triples)
    scale = r.choice([1, 2, 3])
    op_len *= scale
    ap_len *= scale
    oa_radius *= scale
    ab_len = 2 * ap_len

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(40),
    }
    pts["P"] = (round((pts["A"][0] + pts["B"][0]) / 2, 1), round((pts["A"][1] + pts["B"][1]) / 2, 1))

    prompt = (
        f"In the circle with centre $O$ and radius $r = {oa_radius}\\text{{ units}}$, "
        f"chord $AB$ has a length of ${ab_len}\\text{{ units}}$. "
        f"If $OP \\perp AB$, calculate the perpendicular distance $OP$ from the centre $O$ to the chord $AB$."
    )

    diag = circle_geo_svg(
        title=f"Radius = {oa_radius}, Chord AB = {ab_len} — Find OP",
        points=pts,
        segments=[("O", "P"), ("A", "B"), ("O", "A")],
        right_angle_at=pts["P"],
        callouts=[(160, 175, f"OA={oa_radius}", "#dc2626"), (210, 290, f"AB = {ab_len}, OP = ?", "#1d4ed8")],
    )

    steps = [
        step(from_latex=rf"AB = {ab_len}", to_latex_str=rf"AP = \frac{{1}}{{2}}({ab_len}) = {ap_len} \quad (\text{{line from centre }} \perp \text{{ to chord}})", op="bisect chord AB", rule="line from centre perpendicular to chord",),
        step(from_latex=r"OP^2 = OA^2 - AP^2", to_latex_str=rf"OP = \sqrt{{{oa_radius}^2 - {ap_len}^2}} = {op_len}\text{{ units}} \quad (\text{{Pythagoras}})", op="calculate perpendicular distance OP", rule="Pythagoras",),
    ]
    canonical = solution_graph(goal="find perpendicular distance OP", steps=steps, final_latex=str(op_len))

    return make_math_question(
        prefix="g11_cg_04",
        topic=TOPIC_NAME,
        subskill="04_chord_pythagoras_find_perp_distance",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_04",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=str(op_len),
        answer_sympy=str(op_len),
        sample_answer=rf"AP = {ap_len}\text{{ (line from centre }}\perp\text{{ to chord)}}; \; OP = \sqrt{{{oa_radius}^2 - {ap_len}^2}} = {op_len}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"AP = {ap_len} with reason", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Pythagoras OP^2 = {oa_radius}^2 - {ap_len}^2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"OP = {op_len}", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Halve the chord $AB$ first to find $AP$, then apply the Theorem of Pythagoras in $\\triangle OAP$.",
            "2_concept": "$AP = \\frac{1}{2}AB$ and $OP = \\sqrt{OA^2 - AP^2}$.",
            "3_breakdown": f"$AP = {ap_len}$, so $OP = \\sqrt{{{oa_radius}^2 - {ap_len}^2}} = {op_len}$.",
        },
        misconception_tags=["used_full_chord_in_pythagoras", "omitted_geometric_reason"],
        keywords=["circle geometry", "perpendicular distance", "chord"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_04_chord_pythagoras_find_perp_distance",
        difficulty=difficulty,
    )

# 05. Chord & Sagitta (Arrow Height PC where Radius OC ⊥ AB at P)
def arch_05_chord_arrow_height_sagitta(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (7, 24, 25)]
    op_len, ap_len, rad = r.choice(triples)
    scale = r.choice([1, 2, 3])
    op_len *= scale
    ap_len *= scale
    rad *= scale
    ab_len = 2 * ap_len
    pc_sagitta = rad - op_len

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(40),
        "C": _pt_on_circle(90),
    }
    pts["P"] = (210.0, round(pts["A"][1], 1))

    prompt = (
        f"In the circle with centre $O$ and radius $r = {rad}\\text{{ cm}}$, radius $OC$ intersects chord $AB$ "
        f"perpendicularly at $P$. If the length of chord $AB = {ab_len}\\text{{ cm}}$, calculate the length of segment $PC$ "
        f"(between the chord and the circumference). State all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Radius OC = {rad} cm ⊥ Chord AB = {ab_len} cm at P — Find PC",
        points=pts,
        segments=[("O", "C"), ("A", "B"), ("O", "A")],
        right_angle_at=pts["P"],
        callouts=[(162, 175, f"OA={rad}", "#dc2626"), (210, 292, f"AB = {ab_len} cm, PC = ?", "#1d4ed8")],
    )

    steps = [
        step(from_latex=rf"AB = {ab_len}\text{{ cm}}", to_latex_str=rf"AP = {ap_len}\text{{ cm}} \quad (\text{{line from centre }} \perp \text{{ to chord}})", op="find half-chord AP", rule="line from centre perpendicular to chord",),
        step(from_latex=rf"OP = \sqrt{{OA^2 - AP^2}}", to_latex_str=rf"OP = \sqrt{{{rad}^2 - {ap_len}^2}} = {op_len}\text{{ cm}} \quad (\text{{Pythagoras}})", op="calculate OP using Pythagoras", rule="Pythagoras",),
        step(from_latex=rf"OC = OA = {rad}\text{{ cm}} \quad (\text{{radii}})", to_latex_str=rf"PC = OC - OP = {rad} - {op_len} = {pc_sagitta}\text{{ cm}}", op="subtract OP from radius OC", rule="equal radii",),
    ]
    canonical = solution_graph(goal="calculate arrow height PC", steps=steps, final_latex=rf"{pc_sagitta}\text{{ cm}}")

    return make_math_question(
        prefix="g11_cg_05",
        topic=TOPIC_NAME,
        subskill="05_chord_arrow_height_sagitta",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_05",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{pc_sagitta}\text{{ cm}}",
        answer_sympy=str(pc_sagitta),
        sample_answer=rf"AP = {ap_len}\text{{ cm}}; \; OP = {op_len}\text{{ cm}}; \; PC = OC - OP = {rad} - {op_len} = {pc_sagitta}\text{{ cm (radii)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"AP = {ap_len} cm (line from centre perp to chord)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"OP = {op_len} cm (Pythagoras)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"OC = OA = {rad} cm (radii)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"PC = {pc_sagitta} cm", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Notice that $OC$ is a radius, so $OC = OA = {rad}\\text{ cm}$. First find $OP$ in right-angled $\\triangle OAP$.",
            "2_concept": "$AP = \\frac{1}{2}AB$, $OP = \\sqrt{OA^2 - AP^2}$, and $PC = OC - OP$ since $OC = OA$ (radii).",
            "3_breakdown": f"$OP = {op_len}\\text{{ cm}}$, therefore $PC = {rad} - {op_len} = {pc_sagitta}\\text{{ cm}}$.",
        },
        misconception_tags=["stopped_at_op_instead_of_pc", "failed_to_identify_equal_radii"],
        keywords=["circle geometry", "chord", "radii", "sagitta"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="elementary_05_chord_arrow_height_sagitta",
        difficulty=difficulty,
    )

# 06. Converse Theorem 1: Line from Centre to Midpoint of Chord is ⊥
def arch_06_converse_midpoint_chord_perp_angle(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_o = r.randint(28, 66)
    ang_a = 90 - ang_o

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(40),
    }
    pts["M"] = (round((pts["A"][0] + pts["B"][0]) / 2, 1), round((pts["A"][1] + pts["B"][1]) / 2, 1))

    prompt = (
        f"In the circle with centre $O$, $M$ is the midpoint of chord $AB$ ($AM = MB$). "
        f"Radius $OA$ and segment $OM$ are drawn. If $A\\hat{{O}}M = {ang_o}^\\circ$, "
        f"calculate the size of $O\\hat{{A}}M$ and state the geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Midpoint M of Chord AB (AM = MB), ∠AOM = {ang_o}°",
        points=pts,
        segments=[("O", "M"), ("A", "B"), ("O", "A")],
        callouts=[(192, 185, f"∠O={ang_o}°", "#dc2626"), (210, 290, "AM = MB, find ∠OAM", "#1d4ed8")],
    )

    steps = [
        step(from_latex=r"AM = MB", to_latex_str=r"O\hat{M}A = 90^\circ \quad (\text{line from centre to midpt of chord})", op="apply midpoint of chord converse theorem", rule="line from centre to midpoint of chord is perpendicular to chord",),
        step(from_latex=rf"O\hat{{A}}M + {ang_o}^\circ + 90^\circ = 180^\circ", to_latex_str=rf"O\hat{{A}}M = 90^\circ - {ang_o}^\circ = {ang_a}^\circ \quad (\text{{sum of }}\angle\text{{s in }}\triangle)", op="use angle sum in triangle OAM", rule="sum of angles in triangle",),
    ]
    canonical = solution_graph(goal="find angle OAM using midpoint of chord converse", steps=steps, final_latex=rf"{ang_a}^\circ")

    return make_math_question(
        prefix="g11_cg_06",
        topic=TOPIC_NAME,
        subskill="06_converse_midpoint_chord_perp_angle",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_06",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_a}^\circ",
        answer_sympy=str(ang_a),
        sample_answer=rf"O\hat{{M}}A = 90^\circ \text{{ (line from centre to midpt of chord)}}; \; O\hat{{A}}M = 90^\circ - {ang_o}^\circ = {ang_a}^\circ",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Angle OMA = 90 deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: line from centre to midpt of chord", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle OAM = {ang_a} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Since $M$ is the midpoint of chord $AB$, what angle does $OM$ make with $AB$?",
            "2_concept": "$O\\hat{M}A = 90^\\circ$ (line from centre to midpt of chord). Then use the sum of angles in $\\triangle OAM$.",
            "3_breakdown": f"$O\\hat{{A}}M = 180^\\circ - 90^\\circ - {ang_o}^\\circ = {ang_a}^\\circ$.",
        },
        misconception_tags=["omitted_geometric_reason", "midpoint_converse_reason_confused"],
        keywords=["circle geometry", "midpoint of chord", "converse theorem"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_06_converse_midpoint_chord_perp_angle",
        difficulty=difficulty,
    )

# 07. Algebraic Chord & Pythagoras Problem
def arch_07_chord_algebraic_pythagoras_variable(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    # Pick a Pythagorean triple (x, x+d, hyp) e.g. (3k, 4k, 5k) or (5k, 12k, 13k) or (8k, 15k, 17k)
    base_triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
    a0, b0, c0 = r.choice(base_triples)
    k = r.choice([1, 2, 3])
    x_val = a0 * k
    ap_val = b0 * k
    diff = ap_val - x_val
    rad_val = c0 * k
    ab_val = 2 * ap_val

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(40),
    }
    pts["P"] = (round((pts["A"][0] + pts["B"][0]) / 2, 1), round((pts["A"][1] + pts["B"][1]) / 2, 1))

    prompt = (
        f"In the circle with centre $O$, $OP \\perp AB$ at $P$. "
        f"The distance $OP = x\\text{{ units}}$, the chord $AB = {ab_val}\\text{{ units}}$ (or $AP = x + {diff}$), "
        f"and the radius $OA = {rad_val}\\text{{ units}}$. "
        f"Form an equation and solve for $x$."
    )

    diag = circle_geo_svg(
        title=f"Algebraic Chord Rider: OP = x, AP = x + {diff}, OA = {rad_val}",
        points=pts,
        segments=[("O", "P"), ("A", "B"), ("O", "A")],
        right_angle_at=pts["P"],
        callouts=[(162, 175, f"OA={rad_val}", "#dc2626"), (210, 290, f"OP = x, AP = x + {diff}", "#1d4ed8")],
    )

    steps = [
        step(from_latex=r"OP^2 + AP^2 = OA^2", to_latex_str=rf"x^2 + (x + {diff})^2 = {rad_val}^2 \quad (\text{{Pythagoras}})", op="set up Pythagoras equation in triangle OAP", rule="Pythagoras",),
        step(from_latex=rf"2x^2 + {2*diff}x + {diff**2 - rad_val**2} = 0", to_latex_str=rf"x^2 + {diff}x - {(rad_val**2 - diff**2)//2} = 0", op="expand and simplify quadratic equation", rule="quadratic standard form",),
        step(from_latex=rf"(x - {x_val})(x + {x_val + diff}) = 0", to_latex_str=rf"x = {x_val} \quad (x > 0)", op="solve for positive length x", rule="zero product property",),
    ]
    canonical = solution_graph(goal="solve for x using Pythagoras in circle chord", steps=steps, final_latex=str(x_val))

    return make_math_question(
        prefix="g11_cg_07",
        topic=TOPIC_NAME,
        subskill="07_chord_algebraic_pythagoras_variable",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_07",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=str(x_val),
        answer_sympy=str(x_val),
        sample_answer=rf"x^2 + (x + {diff})^2 = {rad_val}^2 \implies x = {x_val}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Pythagoras equation x^2 + (x + {diff})^2 = {rad_val}^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Standard quadratic form", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Factorisation", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Valid positive solution x = {x_val}", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Apply the Theorem of Pythagoras in right-angled $\\triangle OAP$: $OP^2 + AP^2 = OA^2$.",
            "2_concept": f"Substitute $OP = x$, $AP = x + {diff}$, and $OA = {rad_val}$ into $OP^2 + AP^2 = OA^2$.",
            "3_breakdown": f"$x^2 + (x + {diff})^2 = {rad_val}^2 \\implies x = {x_val}$ (since $x > 0$).",
        },
        misconception_tags=["binomial_squaring_error", "kept_negative_length_root"],
        keywords=["circle geometry", "chord", "quadratic Pythagoras"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="elementary_07_chord_algebraic_pythagoras_variable",
        difficulty=difficulty,
    )

# 08. Distance Between Two Parallel Chords on Opposite Sides of Centre
def arch_08_two_parallel_chords_distance(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    # Radius r = 5k or 13k or 10k or 17k or 25k where we have two pairs (d1, h1) and (d2, h2)
    configs = [
        (5, 3, 4, 4, 3),
        (10, 6, 8, 8, 6),
        (15, 9, 12, 12, 9),
        (20, 12, 16, 16, 12),
        (25, 7, 24, 15, 20),
        (25, 15, 20, 20, 15),
        (13, 5, 12, 12, 5),
        (26, 10, 24, 24, 10),
    ]
    base_r, d1, h1, d2, h2 = r.choice(configs)
    scale = r.choice([1, 2])
    rad = base_r * scale
    op = d1 * scale
    oq = d2 * scale
    ab_len = 2 * h1 * scale
    cd_len = 2 * h2 * scale
    pq_dist = op + oq

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(35),
        "C": _pt_on_circle(215),
        "D": _pt_on_circle(325),
    }
    pts["P"] = (210.0, round(pts["A"][1], 1))
    pts["Q"] = (210.0, round(pts["C"][1], 1))

    prompt = (
        f"In a circle with centre $O$ and radius $r = {rad}\\text{{ cm}}$, two parallel chords $AB = {ab_len}\\text{{ cm}}$ "
        f"and $CD = {cd_len}\\text{{ cm}}$ lie on opposite sides of the centre $O$. "
        f"Calculate the perpendicular distance $PQ$ between the two parallel chords."
    )

    diag = circle_geo_svg(
        title=f"Parallel Chords AB = {ab_len} cm & CD = {cd_len} cm (r = {rad} cm)",
        points=pts,
        segments=[("A", "B"), ("C", "D"), ("P", "Q"), ("O", "A"), ("O", "C")],
        right_angle_at=pts["P"],
        callouts=[(210, 292, f"r = {rad} cm, AB = {ab_len} cm, CD = {cd_len} cm — Find PQ", "#1d4ed8")],
    )

    steps = [
        step(from_latex=rf"AP = \frac{{1}}{{2}}({ab_len}) = {h1*scale}\text{{ cm}}, \; CQ = \frac{{1}}{{2}}({cd_len}) = {h2*scale}\text{{ cm}}", to_latex_str=rf"OP = \sqrt{{{rad}^2 - {h1*scale}^2}} = {op}\text{{ cm}} \quad (\text{{Pythagoras}})", op="find perpendicular distance OP to chord AB", rule="line from centre perpendicular to chord and Pythagoras",),
        step(from_latex=rf"OQ = \sqrt{{{rad}^2 - {h2*scale}^2}}", to_latex_str=rf"OQ = {oq}\text{{ cm}} \quad (\text{{Pythagoras}})", op="find perpendicular distance OQ to chord CD", rule="Pythagoras",),
        step(from_latex=r"PQ = OP + OQ", to_latex_str=rf"PQ = {op} + {oq} = {pq_dist}\text{{ cm}}", op="sum distances on opposite sides of centre", rule="collinear perpendicular segments",),
    ]
    canonical = solution_graph(goal="calculate distance PQ between parallel chords", steps=steps, final_latex=rf"{pq_dist}\text{{ cm}}")

    return make_math_question(
        prefix="g11_cg_08",
        topic=TOPIC_NAME,
        subskill="08_two_parallel_chords_distance",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_08",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{pq_dist}\text{{ cm}}",
        answer_sympy=str(pq_dist),
        sample_answer=rf"OP = {op}\text{{ cm}}, \; OQ = {oq}\text{{ cm}}; \; PQ = {op} + {oq} = {pq_dist}\text{{ cm}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Half-chords AP = {h1*scale} cm and CQ = {h2*scale} cm", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"OP = {op} cm", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"OQ = {oq} cm", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Total distance PQ = {pq_dist} cm", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Find the perpendicular distance from $O$ to each chord separately using Pythagoras, then add them.",
            "2_concept": "$OP = \\sqrt{r^2 - (AB/2)^2}$ and $OQ = \\sqrt{r^2 - (CD/2)^2}$, so $PQ = OP + OQ$.",
            "3_breakdown": f"$OP = {op}\\text{{ cm}}$ and $OQ = {oq}\\text{{ cm}}$, so $PQ = {op} + {oq} = {pq_dist}\\text{{ cm}}$.",
        },
        misconception_tags=["subtracted_distances_instead_of_adding", "used_full_chord_in_pythagoras"],
        keywords=["circle geometry", "parallel chords", "Pythagoras"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=5,
        mode="elementary_08_two_parallel_chords_distance",
        difficulty=difficulty,
    )

# 09. Angle at Centre = 2 × Angle at Circumference (Find Centre Angle)
def arch_09_angle_at_centre_find_centre_angle(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_c = r.randint(26, 68)
    ang_o = 2 * ang_c

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(135),
        "B": _pt_on_circle(45),
        "C": _pt_on_circle(270),
    }

    prompt = (
        f"In the circle with centre $O$, arc $AB$ subtends $A\\hat{{C}}B = {ang_c}^\\circ$ at the circumference "
        f"and $A\\hat{{O}}B$ at the centre. Calculate the size of $A\\hat{{O}}B$ and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Angle at Centre Theorem: ∠ACB = {ang_c}°, Find ∠AOB",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("C", "A"), ("C", "B")],
        callouts=[(210, 95, f"∠C = {ang_c}°", "#1d4ed8"), (210, 182, "∠AOB = ?", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"A\hat{{C}}B = {ang_c}^\circ", to_latex_str=rf"A\hat{{O}}B = 2 \times {ang_c}^\circ = {ang_o}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})", op="multiply circumference angle by 2", rule="angle at centre = 2 x angle at circumference",),
    ]
    canonical = solution_graph(goal="find angle AOB at centre", steps=steps, final_latex=rf"{ang_o}^\circ")

    return make_math_question(
        prefix="g11_cg_09",
        topic=TOPIC_NAME,
        subskill="09_angle_at_centre_find_centre_angle",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_09",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_o}^\circ",
        answer_sympy=str(ang_o),
        sample_answer=rf"A\hat{{O}}B = 2 \times {ang_c}^\circ = {ang_o}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct angle AOB = {ang_o} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: angle at centre = 2 x angle at circ", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Compare the angle at the centre $A\\hat{O}B$ with the angle at the circumference $A\\hat{C}B$ subtended by the same arc $AB$.",
            "2_concept": "$A\\hat{O}B = 2 \\times A\\hat{C}B$ ($\\angle$ at centre $= 2 \\times \\angle$ at circ).",
            "3_breakdown": f"$A\\hat{{O}}B = 2 \\times {ang_c}^\\circ = {ang_o}^\\circ$.",
        },
        misconception_tags=["halved_instead_of_doubling", "omitted_geometric_reason"],
        keywords=["circle geometry", "angle at centre", "circumference"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="elementary_09_angle_at_centre_find_centre_angle",
        difficulty=difficulty,
    )

# 10. Angle at Centre Theorem — Find Circumference Angle
def arch_10_angle_at_centre_find_circumference_angle(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_c = r.randint(25, 72)
    ang_o = 2 * ang_c

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(135),
        "B": _pt_on_circle(45),
        "C": _pt_on_circle(270),
    }

    prompt = (
        f"In the circle with centre $O$, arc $AB$ subtends $A\\hat{{O}}B = {ang_o}^\\circ$ at the centre. "
        f"Point $C$ lies on the major arc $AB$. Calculate the size of $A\\hat{{C}}B$ and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Angle at Centre ∠AOB = {ang_o}° — Find Inscribed ∠ACB",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("C", "A"), ("C", "B")],
        callouts=[(210, 182, f"∠O = {ang_o}°", "#dc2626"), (210, 95, "∠C = ?", "#1d4ed8")],
    )

    steps = [
        step(from_latex=rf"A\hat{{O}}B = {ang_o}^\circ", to_latex_str=rf"A\hat{{C}}B = \frac{{1}}{{2}}({ang_o}^\circ) = {ang_c}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})", op="halve the angle at the centre", rule="angle at centre = 2 x angle at circumference",),
    ]
    canonical = solution_graph(goal="find angle ACB at circumference", steps=steps, final_latex=rf"{ang_c}^\circ")

    return make_math_question(
        prefix="g11_cg_10",
        topic=TOPIC_NAME,
        subskill="10_angle_at_centre_find_circumference_angle",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_10",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_c}^\circ",
        answer_sympy=str(ang_c),
        sample_answer=rf"A\hat{{C}}B = \frac{{1}}{{2}}({ang_o}^\circ) = {ang_c}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct angle ACB = {ang_c} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: angle at centre = 2 x angle at circ", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "The angle at the circumference is half the angle at the centre subtended by the same arc.",
            "2_concept": "$A\\hat{C}B = \\frac{1}{2}A\\hat{O}B$ ($\\angle$ at centre $= 2 \\times \\angle$ at circ).",
            "3_breakdown": f"$A\\hat{{C}}B = \\frac{{{ang_o}^\\circ}}{{2}} = {ang_c}^\\circ$.",
        },
        misconception_tags=["doubled_instead_of_halving", "omitted_geometric_reason"],
        keywords=["circle geometry", "angle at centre", "inscribed angle"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="elementary_10_angle_at_centre_find_circumference_angle",
        difficulty=difficulty,
    )

# 11. Reflex Angle at Centre & Obtuse Angle at Circumference
def arch_11_angle_at_centre_reflex_obtuse_inscribed(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_c_obtuse = r.randint(98, 138)
    reflex_o = 2 * ang_c_obtuse
    obtuse_o = 360 - reflex_o

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(150),
        "B": _pt_on_circle(30),
        "C": _pt_on_circle(90),
    }

    prompt = (
        f"In the circle with centre $O$, points $A$, $C$, and $B$ lie on the minor arc such that "
        f"the obtuse inscribed angle $A\\hat{{C}}B = {ang_c_obtuse}^\\circ$. "
        f"Calculate the size of the interior obtuse angle $A\\hat{{O}}B$ inside quadrilateral $OACB$, "
        f"giving complete geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Reflex Angle at Centre & Obtuse ∠ACB = {ang_c_obtuse}°",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("C", "A"), ("C", "B")],
        callouts=[(210, 225, f"∠ACB = {ang_c_obtuse}°", "#1d4ed8"), (210, 135, "∠AOB = ?", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"A\hat{{C}}B = {ang_c_obtuse}^\circ", to_latex_str=rf"\text{{reflex }} A\hat{{O}}B = 2 \times {ang_c_obtuse}^\circ = {reflex_o}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})", op="calculate reflex angle at centre O", rule="angle at centre = 2 x angle at circumference",),
        step(from_latex=rf"\text{{reflex }} A\hat{{O}}B = {reflex_o}^\circ", to_latex_str=rf"A\hat{{O}}B = 360^\circ - {reflex_o}^\circ = {obtuse_o}^\circ \quad (\angle\text{{s round a pt}})", op="subtract from 360 degrees around point O", rule="angles around a point",),
    ]
    canonical = solution_graph(goal="find interior angle AOB using reflex angle at centre", steps=steps, final_latex=rf"{obtuse_o}^\circ")

    return make_math_question(
        prefix="g11_cg_11",
        topic=TOPIC_NAME,
        subskill="11_angle_at_centre_reflex_obtuse_inscribed",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_11",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{obtuse_o}^\circ",
        answer_sympy=str(obtuse_o),
        sample_answer=rf"\text{{reflex }} A\hat{{O}}B = {reflex_o}^\circ \text{{ (}}\angle\text{{ at centre }} = 2\angle\text{{ at circ)}}; \; A\hat{{O}}B = 360^\circ - {reflex_o}^\circ = {obtuse_o}^\circ \text{{ (}}\angle\text{{s round a pt)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Reflex angle AOB = {reflex_o} deg (angle at centre = 2 x angle at circ)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Angles around a point sum to 360 deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Interior angle AOB = {obtuse_o} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "An obtuse angle $A\\hat{C}B$ at the circumference is subtended by the major arc, so it corresponds to the **reflex** angle at $O$.",
            "2_concept": "First find $\\text{reflex } A\\hat{O}B = 2 \\times A\\hat{C}B$, then use angles around a point ($360^\\circ$).",
            "3_breakdown": f"$\\text{{reflex }} A\\hat{{O}}B = {reflex_o}^\\circ \\implies A\\hat{{O}}B = 360^\\circ - {reflex_o}^\\circ = {obtuse_o}^\\circ$.",
        },
        misconception_tags=["treated_oacb_as_cyclic_quad", "forgot_reflex_angle_at_centre"],
        keywords=["circle geometry", "reflex angle at centre", "angles round a point"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_11_angle_at_centre_reflex_obtuse_inscribed",
        difficulty=difficulty,
    )

# 12. Angle at Centre Combined with Isosceles Triangle of Radii (OA = OB)
def arch_12_angle_at_centre_with_isosceles_radii(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_c = r.randint(25, 65)
    ang_o = 2 * ang_c
    ang_oab = 90 - ang_c

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(40),
        "C": _pt_on_circle(270),
    }

    prompt = (
        f"In the circle with centre $O$, points $A$, $B$, and $C$ lie on the circumference and chord $AB$ is drawn. "
        f"If $A\\hat{{C}}B = {ang_c}^\\circ$, calculate the size of base angle $O\\hat{{A}}B$. "
        f"Provide all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Angle at Centre & Isosceles △OAB (∠C = {ang_c}°)",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("A", "B"), ("C", "A"), ("C", "B")],
        callouts=[(210, 95, f"∠C = {ang_c}°", "#1d4ed8"), (210, 290, "Find ∠OAB", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"A\hat{{C}}B = {ang_c}^\circ", to_latex_str=rf"A\hat{{O}}B = 2 \times {ang_c}^\circ = {ang_o}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})", op="calculate angle at centre AOB", rule="angle at centre = 2 x angle at circumference",),
        step(from_latex=r"OA = OB \quad (\text{radii})", to_latex_str=rf"O\hat{{A}}B = O\hat{{B}}A = \frac{{180^\circ - {ang_o}^\circ}}{{2}} = {ang_oab}^\circ \quad (\angle\text{{s opp equal radii}})", op="use isosceles triangle OAB to find base angle OAB", rule="angles opposite equal sides / radii",),
    ]
    canonical = solution_graph(goal="find base angle OAB", steps=steps, final_latex=rf"{ang_oab}^\circ")

    return make_math_question(
        prefix="g11_cg_12",
        topic=TOPIC_NAME,
        subskill="12_angle_at_centre_with_isosceles_radii",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_12",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_oab}^\circ",
        answer_sympy=str(ang_oab),
        sample_answer=rf"A\hat{{O}}B = {ang_o}^\circ \text{{ (}}\angle\text{{ at centre}} = 2\angle\text{{ at circ)}}; \; O\hat{{A}}B = \frac{{180^\circ - {ang_o}^\circ}}{{2}} = {ang_oab}^\circ \text{{ (}}\angle\text{{s opp equal radii)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle AOB = {ang_o} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: angle at centre = 2 x angle at circ", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "OA = OB (radii) / angles opp equal sides", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Angle OAB = {ang_oab} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "First find $A\\hat{O}B$ at the centre, then notice that $\\triangle OAB$ is isosceles because $OA = OB$ (radii).",
            "2_concept": "$A\\hat{O}B = 2\\hat{C}$ and $O\\hat{A}B = \\frac{180^\\circ - A\\hat{O}B}{2}$ ($\\angle$s opp equal radii).",
            "3_breakdown": f"$A\\hat{{O}}B = {ang_o}^\\circ \\implies O\\hat{{A}}B = \\frac{{180^\\circ - {ang_o}^\\circ}}{{2}} = {ang_oab}^\\circ$.",
        },
        misconception_tags=["failed_to_identify_equal_radii", "omitted_geometric_reason"],
        keywords=["circle geometry", "equal radii", "angle at centre"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_12_angle_at_centre_with_isosceles_radii",
        difficulty=difficulty,
    )

# 13. Reverse from Radii Base Angle to Circumference Angle
def arch_13_angle_at_centre_reverse_from_radii_base_angle(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_oab = r.randint(22, 64)
    ang_o = 180 - 2 * ang_oab
    ang_c = 90 - ang_oab

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(40),
        "C": _pt_on_circle(270),
    }

    prompt = (
        f"In the circle with centre $O$, chord $AB$ is drawn such that $O\\hat{{A}}B = {ang_oab}^\\circ$. "
        f"Point $C$ lies on the major arc $AB$. Calculate the size of $A\\hat{{C}}B$, stating all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Given Base Angle ∠OAB = {ang_oab}° — Find Inscribed ∠ACB",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("A", "B"), ("C", "A"), ("C", "B")],
        callouts=[(210, 290, f"∠OAB = {ang_oab}°, Find ∠ACB", "#1d4ed8")],
    )

    steps = [
        step(from_latex=rf"OA = OB \implies O\hat{{B}}A = O\hat{{A}}B = {ang_oab}^\circ \quad (\angle\text{{s opp equal radii}})", to_latex_str=rf"A\hat{{O}}B = 180^\circ - 2({ang_oab}^\circ) = {ang_o}^\circ \quad (\text{{sum of }}\angle\text{{s in }}\triangle)", op="find angle AOB at the centre", rule="angles opposite equal radii and triangle sum",),
        step(from_latex=rf"A\hat{{O}}B = {ang_o}^\circ", to_latex_str=rf"A\hat{{C}}B = \frac{{1}}{{2}}({ang_o}^\circ) = {ang_c}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})", op="halve angle at centre to find ACB", rule="angle at centre = 2 x angle at circumference",),
    ]
    canonical = solution_graph(goal="find angle ACB from base angle OAB", steps=steps, final_latex=rf"{ang_c}^\circ")

    return make_math_question(
        prefix="g11_cg_13",
        topic=TOPIC_NAME,
        subskill="13_angle_at_centre_reverse_from_radii_base_angle",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_13",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_c}^\circ",
        answer_sympy=str(ang_c),
        sample_answer=rf"A\hat{{O}}B = 180^\circ - 2({ang_oab}^\circ) = {ang_o}^\circ; \; A\hat{{C}}B = \frac{{1}}{{2}}({ang_o}^\circ) = {ang_c}^\circ",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle OBA = {ang_oab} deg (angles opp equal radii)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Angle AOB = {ang_o} deg (sum of angles in triangle)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Reason: angle at centre = 2 x angle at circ", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Angle ACB = {ang_c} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Use $OA = OB$ (radii) in $\\triangle OAB$ to find $A\\hat{O}B$ first.",
            "2_concept": "$O\\hat{B}A = O\\hat{A}B = {ang_oab}^\\circ$, so $A\\hat{O}B = 180^\\circ - 2({ang_oab}^\\circ)$ and $A\\hat{C}B = \\frac{1}{2}A\\hat{O}B$.",
            "3_breakdown": f"$A\\hat{{O}}B = {ang_o}^\\circ \\implies A\\hat{{C}}B = {ang_c}^\\circ$.",
        },
        misconception_tags=["equated_base_angle_to_circumference_angle", "omitted_geometric_reason"],
        keywords=["circle geometry", "radii", "angle at centre"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_13_angle_at_centre_reverse_from_radii_base_angle",
        difficulty=difficulty,
    )

# 14. Algebraic Angle at Centre Equation
def arch_14_angle_at_centre_algebraic_x(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    x_val = r.randint(18, 42)
    b_offset = r.randint(5, 18)
    ang_c = x_val + b_offset
    ang_o = 2 * ang_c
    # Express ang_o as 3x - a_offset => a_offset = 3*x_val - ang_o = x_val - 2*b_offset
    # Ensure a_offset is positive by picking x_val > 2*b_offset + 2
    x_val = r.randint(2 * b_offset + 4, 2 * b_offset + 25)
    ang_c = x_val + b_offset
    ang_o = 2 * ang_c
    a_offset = 3 * x_val - ang_o

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(135),
        "B": _pt_on_circle(45),
        "C": _pt_on_circle(270),
    }

    prompt = (
        f"In the circle with centre $O$, arc $AB$ subtends $A\\hat{{O}}B = (3x - {a_offset}^\\circ)$ at the centre "
        f"and $A\\hat{{C}}B = (x + {b_offset}^\\circ)$ at the circumference. "
        f"Determine the value of $x$, stating the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Algebraic Angle at Centre: ∠O = 3x - {a_offset}°, ∠C = x + {b_offset}°",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("C", "A"), ("C", "B")],
        callouts=[(210, 95, f"∠C = x+{b_offset}°", "#1d4ed8"), (210, 182, f"∠O = 3x-{a_offset}°", "#dc2626")],
    )

    steps = [
        step(from_latex=r"A\hat{O}B = 2 \times A\hat{C}B", to_latex_str=rf"3x - {a_offset}^\circ = 2(x + {b_offset}^\circ) \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})", op="set up equation using angle at centre theorem", rule="angle at centre = 2 x angle at circumference",),
        step(from_latex=rf"3x - {a_offset}^\circ = 2x + {2*b_offset}^\circ", to_latex_str=rf"x = {x_val}^\circ", op="solve linear equation for x", rule="linear equation",),
    ]
    canonical = solution_graph(goal="solve for x using angle at centre theorem", steps=steps, final_latex=rf"{x_val}^\circ")

    return make_math_question(
        prefix="g11_cg_14",
        topic=TOPIC_NAME,
        subskill="14_angle_at_centre_algebraic_x",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_14",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{x_val}^\circ",
        answer_sympy=str(x_val),
        sample_answer=rf"3x - {a_offset}^\circ = 2(x + {b_offset}^\circ) \implies x = {x_val}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Equation 3x - {a_offset} = 2(x + {b_offset})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: angle at centre = 2 x angle at circ", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"x = {x_val} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Set the centre angle equal to twice the circumference angle.",
            "2_concept": "$3x - {a_offset}^\\circ = 2(x + {b_offset}^\\circ)$ ($\\angle$ at centre $= 2 \\times \\angle$ at circ).",
            "3_breakdown": f"$3x - {a_offset}^\\circ = 2x + {2*b_offset}^\\circ \\implies x = {x_val}^\\circ$.",
        },
        misconception_tags=["equated_centre_and_circumference_angles", "distribution_error"],
        keywords=["circle geometry", "algebraic rider", "angle at centre"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_14_angle_at_centre_algebraic_x",
        difficulty=difficulty,
    )

# 15. Angle in a Semi-Circle Theorem (Thales' Theorem)
def arch_15_angle_in_semicircle_basic(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_a = r.randint(24, 68)
    ang_b = 90 - ang_a

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(180),
        "B": _pt_on_circle(0),
        "C": _pt_on_circle(250),
    }

    prompt = (
        f"In the circle with centre $O$, $AB$ is a diameter and point $C$ lies on the circumference. "
        f"If $\\hat{{A}} = {ang_a}^\\circ$, calculate the size of $\\hat{{B}}$ and state all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Angle in a Semi-Circle: Diameter AB, ∠A = {ang_a}°, Find ∠B",
        points=pts,
        segments=[("A", "B"), ("A", "C"), ("B", "C")],
        callouts=[(145, 148, f"∠A={ang_a}°", "#1d4ed8"), (265, 148, "∠B=?", "#dc2626")],
    )

    steps = [
        step(from_latex=r"\text{Diameter } AB", to_latex_str=r"A\hat{C}B = 90^\circ \quad (\angle \text{ in semi-circle})", op="identify right angle subtended by diameter", rule="angle in semi-circle",),
        step(from_latex=rf"\hat{{B}} + {ang_a}^\circ + 90^\circ = 180^\circ", to_latex_str=rf"\hat{{B}} = 90^\circ - {ang_a}^\circ = {ang_b}^\circ \quad (\text{{sum of }}\angle\text{{s in }}\triangle)", op="use triangle angle sum", rule="sum of angles in triangle",),
    ]
    canonical = solution_graph(goal="find angle B using angle in semi-circle theorem", steps=steps, final_latex=rf"{ang_b}^\circ")

    return make_math_question(
        prefix="g11_cg_15",
        topic=TOPIC_NAME,
        subskill="15_angle_in_semicircle_basic",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_15",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_b}^\circ",
        answer_sympy=str(ang_b),
        sample_answer=rf"\hat{{C}} = 90^\circ \text{{ (}}\angle\text{{ in semi-circle)}}; \; \hat{{B}} = 90^\circ - {ang_a}^\circ = {ang_b}^\circ \text{{ (sum of }}\angle\text{{s in }}\triangle\text{{)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Angle C = 90 deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: angle in semi-circle", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle B = {ang_b} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "What angle does a diameter subtend at the circumference of a circle?",
            "2_concept": "$\\hat{C} = 90^\\circ$ ($\\angle$ in semi-circle), and the angles of $\\triangle ABC$ sum to $180^\\circ$.",
            "3_breakdown": f"$\\hat{{B}} = 180^\\circ - 90^\\circ - {ang_a}^\\circ = {ang_b}^\\circ$.",
        },
        misconception_tags=["missed_angle_in_semicircle", "omitted_geometric_reason"],
        keywords=["circle geometry", "semi-circle", "diameter"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_15_angle_in_semicircle_basic",
        difficulty=difficulty,
    )

# 16. Angle in a Semi-Circle + Pythagoras Chord Length
def arch_16_angle_in_semicircle_pythagoras_chord(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    triples = [(6, 8, 10), (10, 24, 26), (12, 16, 20), (16, 30, 34), (18, 24, 30), (14, 48, 50)]
    ac_len, bc_len, ab_diam = r.choice(triples)
    rad = ab_diam // 2

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(180),
        "B": _pt_on_circle(0),
        "C": _pt_on_circle(245),
    }

    prompt = (
        f"In the circle with centre $O$ and radius $r = {rad}\\text{{ cm}}$, $AB$ is a diameter and $C$ is a point "
        f"on the circumference. If chord $AC = {ac_len}\\text{{ cm}}$, calculate the length of chord $BC$, "
        f"giving complete geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Semi-Circle Pythagoras: Radius = {rad} cm, AC = {ac_len} cm — Find BC",
        points=pts,
        segments=[("A", "B"), ("A", "C"), ("B", "C")],
        callouts=[(145, 110, f"AC={ac_len}", "#1d4ed8"), (210, 175, f"AB={ab_diam}", "#dc2626"), (255, 110, "BC=?", "#0f172a")],
    )

    steps = [
        step(from_latex=rf"\text{{Radius }} r = {rad}\text{{ cm}}", to_latex_str=rf"AB = 2({rad}) = {ab_diam}\text{{ cm}} \quad \text{{and}} \quad A\hat{{C}}B = 90^\circ \quad (\angle \text{{ in semi-circle}})", op="identify diameter length and right angle at C", rule="angle in semi-circle",),
        step(from_latex=r"BC^2 = AB^2 - AC^2", to_latex_str=rf"BC = \sqrt{{{ab_diam}^2 - {ac_len}^2}} = {bc_len}\text{{ cm}} \quad (\text{{Pythagoras}})", op="apply Pythagoras in right-angled triangle ABC", rule="Pythagoras",),
    ]
    canonical = solution_graph(goal="find chord BC using angle in semi-circle and Pythagoras", steps=steps, final_latex=rf"{bc_len}\text{{ cm}}")

    return make_math_question(
        prefix="g11_cg_16",
        topic=TOPIC_NAME,
        subskill="16_angle_in_semicircle_pythagoras_chord",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_16",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{bc_len}\text{{ cm}}",
        answer_sympy=str(bc_len),
        sample_answer=rf"A\hat{{C}}B = 90^\circ \text{{ (}}\angle\text{{ in semi-circle)}}; \; BC = \sqrt{{{ab_diam}^2 - {ac_len}^2}} = {bc_len}\text{{ cm (Pythagoras)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Angle ACB = 90 deg (angle in semi-circle)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Diameter AB = {ab_diam} cm and Pythagoras substitution", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"BC = {bc_len} cm", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Since $AB$ is a diameter, $\\hat{C} = 90^\\circ$ ($\\angle$ in semi-circle), making $AB = 2r$ the hypotenuse of $\\triangle ABC$.",
            "2_concept": "$AB = 2({rad}) = {ab_diam}\\text{ cm}$ and $BC = \\sqrt{AB^2 - AC^2}$ (Pythagoras).",
            "3_breakdown": f"$BC = \\sqrt{{{ab_diam}^2 - {ac_len}^2}} = {bc_len}\\text{{ cm}}$.",
        },
        misconception_tags=["used_radius_instead_of_diameter", "omitted_geometric_reason"],
        keywords=["circle geometry", "semi-circle", "Pythagoras"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_16_angle_in_semicircle_pythagoras_chord",
        difficulty=difficulty,
    )

# 17. Angle in Semi-Circle with Radius Forming Isosceles Triangle
def arch_17_angle_in_semicircle_with_isosceles_chord(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_a = r.randint(25, 65)
    ang_b = 90 - ang_a
    ang_bco = ang_b

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(180),
        "B": _pt_on_circle(0),
        "C": _pt_on_circle(240),
    }

    prompt = (
        f"In the circle with centre $O$, $AB$ is a diameter and $C$ is a point on the circumference. "
        f"Radius $OC$ is drawn. If $C\\hat{{A}}B = {ang_a}^\\circ$, calculate the size of $O\\hat{{C}}B$, "
        f"stating all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Diameter AB & Radius OC: ∠CAB = {ang_a}° — Find ∠OCB",
        points=pts,
        segments=[("A", "B"), ("A", "C"), ("B", "C"), ("O", "C")],
        callouts=[(145, 145, f"∠A={ang_a}°", "#1d4ed8"), (235, 115, "∠OCB=?", "#dc2626")],
    )

    steps = [
        step(from_latex=r"\text{Diameter } AB", to_latex_str=r"A\hat{C}B = 90^\circ \quad (\angle \text{ in semi-circle})", op="identify angle in semi-circle", rule="angle in semi-circle",),
        step(from_latex=rf"OA = OC \implies A\hat{{C}}O = C\hat{{A}}O = {ang_a}^\circ \quad (\angle\text{{s opp equal radii}})", to_latex_str=rf"O\hat{{C}}B = 90^\circ - {ang_a}^\circ = {ang_bco}^\circ", op="subtract ACO from 90 degrees", rule="complementary angles in right angle ACB",),
    ]
    canonical = solution_graph(goal="find angle OCB", steps=steps, final_latex=rf"{ang_bco}^\circ")

    return make_math_question(
        prefix="g11_cg_17",
        topic=TOPIC_NAME,
        subskill="17_angle_in_semicircle_with_isosceles_chord",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_17",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_bco}^\circ",
        answer_sympy=str(ang_bco),
        sample_answer=rf"A\hat{{C}}B = 90^\circ \text{{ (}}\angle\text{{ in semi-circle)}}; \; A\hat{{C}}O = {ang_a}^\circ \text{{ (}}\angle\text{{s opp equal radii)}}; \; O\hat{{C}}B = 90^\circ - {ang_a}^\circ = {ang_bco}^\circ",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Angle ACB = 90 deg (angle in semi-circle)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Angle ACO = {ang_a} deg or Angle B = {ang_bco} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle OCB = {ang_bco} deg with reasons", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Notice that $A\\hat{C}B = 90^\\circ$ ($\\angle$ in semi-circle) and $OA = OC = OB$ (radii).",
            "2_concept": "$A\\hat{C}O = \\hat{A} = {ang_a}^\\circ$ ($\\angle$s opp equal radii), and $O\\hat{C}B = A\\hat{C}B - A\\hat{C}O$.",
            "3_breakdown": f"$O\\hat{{C}}B = 90^\\circ - {ang_a}^\\circ = {ang_bco}^\\circ$.",
        },
        misconception_tags=["assumed_oc_perp_ab", "omitted_geometric_reason"],
        keywords=["circle geometry", "semi-circle", "radii"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_17_angle_in_semicircle_with_isosceles_chord",
        difficulty=difficulty,
    )

# 18. Converse of Angle in Semi-Circle — Prove Chord is a Diameter
def arch_18_converse_angle_in_semicircle_prove_diameter(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_a = r.randint(28, 62)
    ang_b = 90 - ang_a
    ang_c = 90

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(180),
        "B": _pt_on_circle(0),
        "C": _pt_on_circle(250),
    }

    prompt = (
        f"Points $A$, $B$, and $C$ lie on a circle. In $\\triangle ABC$, $\\hat{{A}} = {ang_a}^\\circ$ "
        f"and $\\hat{{B}} = {ang_b}^\\circ$. Calculate $\\hat{{C}}$ and hence explain why chord $AB$ must pass "
        f"through the centre $O$ of the circle."
    )

    diag = circle_geo_svg(
        title=f"Converse of Semi-Circle Theorem: ∠A = {ang_a}°, ∠B = {ang_b}°",
        points=pts,
        segments=[("A", "B"), ("A", "C"), ("B", "C")],
        show_center=False,
        callouts=[(145, 148, f"∠A={ang_a}°", "#1d4ed8"), (265, 148, f"∠B={ang_b}°", "#1d4ed8"), (210, 290, "Find ∠C & prove AB is diameter", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"\hat{{A}} = {ang_a}^\circ, \; \hat{{B}} = {ang_b}^\circ", to_latex_str=rf"\hat{{C}} = 180^\circ - ({ang_a}^\circ + {ang_b}^\circ) = 90^\circ \quad (\text{{sum of }}\angle\text{{s in }}\triangle)", op="calculate angle C in triangle ABC", rule="sum of angles in triangle",),
        step(from_latex=r"\hat{C} = 90^\circ", to_latex_str=r"AB \text{ is a diameter} \quad (\text{chord subtends } 90^\circ)", op="conclude AB is a diameter by converse of angle in semi-circle", rule="converse angle in semi-circle (chord subtends 90 degrees)",),
    ]
    canonical = solution_graph(goal="prove AB is a diameter", steps=steps, final_latex=r"90^\circ")

    return make_math_question(
        prefix="g11_cg_18",
        topic=TOPIC_NAME,
        subskill="18_converse_angle_in_semicircle_prove_diameter",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_18",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=r"90^\circ",
        answer_sympy=str(ang_c),
        sample_answer=rf"\hat{{C}} = 180^\circ - ({ang_a}^\circ + {ang_b}^\circ) = 90^\circ \text{{ (sum of }}\angle\text{{s in }}\triangle\text{{)}} \implies AB \text{{ is a diameter (chord subtends }} 90^\circ\text{{)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Angle C = 90 deg (sum of angles in triangle)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Conclusion that AB is a diameter", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Correct converse reason: chord subtends 90 deg / converse angle in semi-circle", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "First calculate $\\hat{C}$ using the sum of angles in $\\triangle ABC$.",
            "2_concept": "If a chord subtends an angle of $90^\\circ$ at the circumference, that chord is a diameter (chord subtends $90^\\circ$).",
            "3_breakdown": f"$\\hat{{C}} = 180^\\circ - ({ang_a}^\\circ + {ang_b}^\\circ) = 90^\\circ$, so $AB$ is a diameter (chord subtends $90^\\circ$).",
        },
        misconception_tags=["used_forward_reason_instead_of_converse", "omitted_geometric_reason"],
        keywords=["circle geometry", "converse semi-circle", "chord subtends 90"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_18_converse_angle_in_semicircle_prove_diameter",
        difficulty=difficulty,
    )

# 19. Angles in the Same Segment (Bow-Tie / Butterfly Configuration)
def arch_19_angles_in_same_segment_basic(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_c = r.randint(28, 74)

    pts = {
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(35),
        "C": _pt_on_circle(235),
        "D": _pt_on_circle(305),
    }

    prompt = (
        f"In the circle, chords $AD$ and $BC$ intersect, and chords $AC$ and $BD$ are drawn. "
        f"Arc $AB$ subtends $\\hat{{C}} = {ang_c}^\\circ$ and $\\hat{{D}}$ in the same segment. "
        f"Determine the size of $\\hat{{D}}$ and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Angles in the Same Segment: ∠C = {ang_c}° — Find ∠D",
        points=pts,
        segments=[("A", "C"), ("B", "C"), ("A", "D"), ("B", "D"), ("A", "B")],
        show_center=False,
        callouts=[(165, 110, f"∠C={ang_c}°", "#1d4ed8"), (255, 110, "∠D=?", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"\hat{{C}} = {ang_c}^\circ", to_latex_str=rf"\hat{{D}} = \hat{{C}} = {ang_c}^\circ \quad (\angle\text{{s in same seg}})", op="apply angles in the same segment theorem", rule="angles in the same segment",),
    ]
    canonical = solution_graph(goal="find angle D using angles in same segment", steps=steps, final_latex=rf"{ang_c}^\circ")

    return make_math_question(
        prefix="g11_cg_19",
        topic=TOPIC_NAME,
        subskill="19_angles_in_same_segment_basic",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_19",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_c}^\circ",
        answer_sympy=str(ang_c),
        sample_answer=rf"\hat{{D}} = \hat{{C}} = {ang_c}^\circ \quad (\angle\text{{s in same seg}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle D = {ang_c} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: angles in same seg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Trace the arc/chord that subtends both $\\hat{C}$ and $\\hat{D}$ at the circumference.",
            "2_concept": "Angles subtended by the same chord/arc in the same segment of a circle are equal ($\\angle$s in same seg).",
            "3_breakdown": f"$\\hat{{D}} = \\hat{{C}} = {ang_c}^\\circ$ ($\\angle$s in same seg).",
        },
        misconception_tags=["subtended_arc_confusion", "omitted_geometric_reason"],
        keywords=["circle geometry", "angles in same segment", "butterfly"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="elementary_19_angles_in_same_segment_basic",
        difficulty=difficulty,
    )

# 20. Angles in Same Segment + Triangle Angle Sum in Intersecting Chords
def arch_20_angles_in_same_segment_triangle_sum(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_c = r.randint(30, 58)
    ang_b = r.randint(35, 62)
    ang_deb = 180 - (ang_c + ang_b)

    pts = {
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(35),
        "C": _pt_on_circle(235),
        "D": _pt_on_circle(305),
        "E": (210.0, 155.0),
    }

    prompt = (
        f"In the circle, chords $AD$ and $BC$ intersect at point $E$. Chords $AC$ and $BD$ are drawn. "
        f"It is given that $A\\hat{{C}}B = {ang_c}^\\circ$ and $C\\hat{{B}}D = {ang_b}^\\circ$. "
        f"Calculate the size of $D\\hat{{E}}B$, giving complete geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Intersecting Chords at E: ∠ACB = {ang_c}°, ∠CBD = {ang_b}°",
        points=pts,
        segments=[("A", "D"), ("B", "C"), ("A", "C"), ("B", "D")],
        show_center=False,
        callouts=[(165, 108, f"∠C={ang_c}°", "#1d4ed8"), (265, 200, f"∠B={ang_b}°", "#1d4ed8"), (210, 290, "Find ∠DEB", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"A\hat{{C}}B = {ang_c}^\circ", to_latex_str=rf"A\hat{{D}}B = A\hat{{C}}B = {ang_c}^\circ \quad (\angle\text{{s in same seg}})", op="find angle ADB using angles in same segment", rule="angles in the same segment",),
        step(from_latex=rf"\text{{In }}\triangle DEB: \; D\hat{{E}}B + {ang_c}^\circ + {ang_b}^\circ = 180^\circ", to_latex_str=rf"D\hat{{E}}B = 180^\circ - ({ang_c}^\circ + {ang_b}^\circ) = {ang_deb}^\circ \quad (\text{{sum of }}\angle\text{{s in }}\triangle)", op="calculate angle DEB in triangle DEB", rule="sum of angles in triangle",),
    ]
    canonical = solution_graph(goal="find angle DEB", steps=steps, final_latex=rf"{ang_deb}^\circ")

    return make_math_question(
        prefix="g11_cg_20",
        topic=TOPIC_NAME,
        subskill="20_angles_in_same_segment_triangle_sum",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_20",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_deb}^\circ",
        answer_sympy=str(ang_deb),
        sample_answer=rf"\hat{{D}} = {ang_c}^\circ \text{{ (}}\angle\text{{s in same seg)}}; \; D\hat{{E}}B = 180^\circ - ({ang_c}^\circ + {ang_b}^\circ) = {ang_deb}^\circ \text{{ (sum of }}\angle\text{{s in }}\triangle\text{{)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle ADB = {ang_c} deg (angles in same seg)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Sum of angles in triangle DEB = 180 deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle DEB = {ang_deb} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Transfer $A\\hat{C}B$ to $A\\hat{D}B$ using angles in the same segment, then work inside $\\triangle DEB$.",
            "2_concept": "$A\\hat{D}B = A\\hat{C}B = {ang_c}^\\circ$ ($\\angle$s in same seg), then use the sum of angles in $\\triangle DEB$.",
            "3_breakdown": f"$D\\hat{{E}}B = 180^\\circ - ({ang_c}^\\circ + {ang_b}^\\circ) = {ang_deb}^\\circ$.",
        },
        misconception_tags=["treated_e_as_circle_centre", "omitted_geometric_reason"],
        keywords=["circle geometry", "angles in same segment", "triangle sum"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_20_angles_in_same_segment_triangle_sum",
        difficulty=difficulty,
    )

# 21. Angles in Same Segment with Parallel Lines (Alt ∠s + ∠s in Same Seg)
def arch_21_angles_in_same_segment_parallel_chords(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_cab = r.randint(26, 64)

    pts = {
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(35),
        "C": _pt_on_circle(215),
        "D": _pt_on_circle(325),
    }

    prompt = (
        f"In the circle, chord $AB$ is parallel to chord $CD$ ($AB \\parallel CD$), and diagonals $AC$, $BC$, "
        f"and $BD$ are drawn. If $B\\hat{{A}}C = {ang_cab}^\\circ$, determine the size of $C\\hat{{B}}D$, "
        f"giving all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Parallel Chords AB ∥ CD: ∠BAC = {ang_cab}° — Find ∠CBD",
        points=pts,
        segments=[("A", "B"), ("C", "D"), ("A", "C"), ("B", "C"), ("B", "D")],
        show_center=False,
        callouts=[(165, 205, f"∠BAC={ang_cab}°", "#1d4ed8"), (210, 290, "AB ∥ CD, Find ∠CBD", "#dc2626")],
    )

    steps = [
        step(from_latex=rf"B\hat{{A}}C = {ang_cab}^\circ", to_latex_str=rf"B\hat{{D}}C = B\hat{{A}}C = {ang_cab}^\circ \quad (\angle\text{{s in same seg}})", op="apply angles in the same segment subtended by chord BC", rule="angles in the same segment",),
        step(from_latex=rf"AB \parallel CD \quad \text{{or}} \quad A\hat{{C}}D = B\hat{{A}}C = {ang_cab}^\circ", to_latex_str=rf"C\hat{{B}}D = B\hat{{A}}C = {ang_cab}^\circ \quad (\text{{alt }}\angle\text{{s, }} AB \parallel CD \text{{ and }} \angle\text{{s in same seg}})", op="combine alternate angles and angles in same segment", rule="alternate angles and angles in the same segment",),
    ]
    canonical = solution_graph(goal="find angle CBD using parallel chords and same segment", steps=steps, final_latex=rf"{ang_cab}^\circ")

    return make_math_question(
        prefix="g11_cg_21",
        topic=TOPIC_NAME,
        subskill="21_angles_in_same_segment_parallel_chords",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_21",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_cab}^\circ",
        answer_sympy=str(ang_cab),
        sample_answer=rf"A\hat{{C}}D = B\hat{{A}}C = {ang_cab}^\circ \text{{ (alt }}\angle\text{{s, }} AB \parallel CD\text{{)}}; \; C\hat{{B}}D = A\hat{{C}}D = {ang_cab}^\circ \text{{ (}}\angle\text{{s in same seg)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle ACD = {ang_cab} deg (alt angles, AB || CD)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Angle CBD = {ang_cab} deg (angles in same seg)", "marks": 2, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Use alternate angles between parallel chords $AB \\parallel CD$ to find $A\\hat{C}D$, then look at the chord $AD$.",
            "2_concept": "$A\\hat{C}D = B\\hat{A}C$ (alt $\\angle$s, $AB \\parallel CD$) and $C\\hat{B}D = A\\hat{C}D$ ($\\angle$s in same seg).",
            "3_breakdown": f"$A\\hat{{C}}D = {ang_cab}^\\circ \\implies C\\hat{{B}}D = {ang_cab}^\\circ$.",
        },
        misconception_tags=["omitted_parallel_line_reason", "subtended_arc_confusion"],
        keywords=["circle geometry", "parallel chords", "alternate angles", "same segment"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=4,
        mode="elementary_21_angles_in_same_segment_parallel_chords",
        difficulty=difficulty,
    )

# 22. Algebraic Angles in Same Segment Equation
def arch_22_angles_in_same_segment_algebraic_x(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    x_val = r.randint(15, 34)
    a_val = r.randint(4, 16)
    ang_total = 2 * x_val + a_val
    b_val = ang_total - x_val

    pts = {
        "A": _pt_on_circle(145),
        "B": _pt_on_circle(35),
        "C": _pt_on_circle(235),
        "D": _pt_on_circle(305),
    }

    prompt = (
        f"In the circle, chord $AB$ subtends $\\hat{{C}} = (2x + {a_val}^\\circ)$ and $\\hat{{D}} = (x + {b_val}^\\circ)$ "
        f"in the same segment. Calculate the value of $x$ and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Same Segment Algebraic: ∠C = 2x + {a_val}°, ∠D = x + {b_val}°",
        points=pts,
        segments=[("A", "C"), ("B", "C"), ("A", "D"), ("B", "D"), ("A", "B")],
        show_center=False,
        callouts=[(160, 108, f"2x+{a_val}°", "#1d4ed8"), (260, 108, f"x+{b_val}°", "#dc2626")],
    )

    steps = [
        step(from_latex=r"\hat{C} = \hat{D}", to_latex_str=rf"2x + {a_val}^\circ = x + {b_val}^\circ \quad (\angle\text{{s in same seg}})", op="equate angles in the same segment", rule="angles in the same segment",),
        step(from_latex=rf"2x - x = {b_val}^\circ - {a_val}^\circ", to_latex_str=rf"x = {x_val}^\circ", op="solve for x", rule="linear equation",),
    ]
    canonical = solution_graph(goal="solve for x using angles in same segment", steps=steps, final_latex=rf"{x_val}^\circ")

    return make_math_question(
        prefix="g11_cg_22",
        topic=TOPIC_NAME,
        subskill="22_angles_in_same_segment_algebraic_x",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_22",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{x_val}^\circ",
        answer_sympy=str(x_val),
        sample_answer=rf"2x + {a_val}^\circ = x + {b_val}^\circ \implies x = {x_val}^\circ \quad (\angle\text{{s in same seg}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Equate 2x + {a_val} = x + {b_val}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: angles in same seg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"x = {x_val} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Angles subtended by the same chord $AB$ in the same segment are equal.",
            "2_concept": "$2x + {a_val}^\\circ = x + {b_val}^\\circ$ ($\\angle$s in same seg).",
            "3_breakdown": f"$x = {b_val}^\\circ - {a_val}^\\circ = {x_val}^\\circ$.",
        },
        misconception_tags=["added_to_180_instead_of_equating", "omitted_geometric_reason"],
        keywords=["circle geometry", "angles in same segment", "algebraic"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_22_angles_in_same_segment_algebraic_x",
        difficulty=difficulty,
    )

# 23. Equal Chords Subtend Equal Angles at the Circumference
def arch_23_equal_chords_subtend_equal_angles_circumference(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_val = r.randint(24, 58)
    chord_len = r.randint(7, 19)

    pts = {
        "A": _pt_on_circle(160),
        "B": _pt_on_circle(110),
        "C": _pt_on_circle(70),
        "D": _pt_on_circle(20),
        "P": _pt_on_circle(270),
    }

    prompt = (
        f"In the circle, chords $AB$ and $CD$ are equal in length ($AB = CD = {chord_len}\\text{{ cm}}$). "
        f"Point $P$ lies on the circumference such that $A\\hat{{P}}B = {ang_val}^\\circ$. "
        f"Determine the size of $C\\hat{{P}}D$ and state the geometric reason."
    )

    diag = circle_geo_svg(
        title=f"Equal Chords AB = CD = {chord_len} cm, ∠APB = {ang_val}°",
        points=pts,
        segments=[("A", "B"), ("C", "D"), ("P", "A"), ("P", "B"), ("P", "C"), ("P", "D")],
        show_center=False,
        callouts=[(210, 290, f"AB = CD = {chord_len} cm, ∠APB = {ang_val}°, Find ∠CPD", "#1d4ed8")],
    )

    steps = [
        step(from_latex=rf"AB = CD, \; A\hat{{P}}B = {ang_val}^\circ", to_latex_str=rf"C\hat{{P}}D = A\hat{{P}}B = {ang_val}^\circ \quad (\text{{equal chords; equal }}\angle\text{{s}})", op="apply equal chords corollary", rule="equal chords subtend equal angles at the circumference",),
    ]
    canonical = solution_graph(goal="find angle CPD subtended by equal chord", steps=steps, final_latex=rf"{ang_val}^\circ")

    return make_math_question(
        prefix="g11_cg_23",
        topic=TOPIC_NAME,
        subskill="23_equal_chords_subtend_equal_angles_circumference",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_23",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{ang_val}^\circ",
        answer_sympy=str(ang_val),
        sample_answer=rf"C\hat{{P}}D = {ang_val}^\circ \quad (\text{{equal chords; equal }}\angle\text{{s}})",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle CPD = {ang_val} deg", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Reason: equal chords; equal angles", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Compare the lengths of chords $AB$ and $CD$ that subtend $A\\hat{P}B$ and $C\\hat{P}D$.",
            "2_concept": "Equal chords subtend equal angles at the circumference (equal chords; equal $\\angle$s).",
            "3_breakdown": f"$C\\hat{{P}}D = A\\hat{{P}}B = {ang_val}^\\circ$ (equal chords; equal $\\angle$s).",
        },
        misconception_tags=["omitted_geometric_reason", "confused_equal_chords_with_same_segment"],
        keywords=["circle geometry", "equal chords", "circumference angles"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=2,
        mode="elementary_23_equal_chords_subtend_equal_angles_circumference",
        difficulty=difficulty,
    )

# 24. Equal Chords Subtend Equal Angles at the Centre
def arch_24_equal_chords_subtend_equal_angles_centre(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    ang_centre = r.randint(42, 86)
    base_ang = (180 - ang_centre) // 2 if (180 - ang_centre) % 2 == 0 else (181 - ang_centre) // 2
    ang_centre = 180 - 2 * base_ang

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(165),
        "B": _pt_on_circle(115),
        "C": _pt_on_circle(65),
        "D": _pt_on_circle(15),
    }

    prompt = (
        f"In the circle with centre $O$, chord $AB =$ chord $CD$. "
        f"If $A\\hat{{O}}B = {ang_centre}^\\circ$, calculate the size of $O\\hat{{C}}D$, "
        f"stating all geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Equal Chords at Centre: AB = CD, ∠AOB = {ang_centre}° — Find ∠OCD",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("A", "B"), ("O", "C"), ("O", "D"), ("C", "D")],
        callouts=[(210, 290, f"AB = CD, ∠AOB = {ang_centre}°, Find ∠OCD", "#1d4ed8")],
    )

    steps = [
        step(from_latex=rf"AB = CD, \; A\hat{{O}}B = {ang_centre}^\circ", to_latex_str=rf"C\hat{{O}}D = A\hat{{O}}B = {ang_centre}^\circ \quad (\text{{equal chords; equal }}\angle\text{{s}})", op="find angle COD at the centre", rule="equal chords subtend equal angles at the centre",),
        step(from_latex=r"OC = OD \quad (\text{radii})", to_latex_str=rf"O\hat{{C}}D = \frac{{180^\circ - {ang_centre}^\circ}}{{2}} = {base_ang}^\circ \quad (\angle\text{{s opp equal radii}})", op="calculate base angle OCD in isosceles triangle OCD", rule="angles opposite equal radii",),
    ]
    canonical = solution_graph(goal="find angle OCD", steps=steps, final_latex=rf"{base_ang}^\circ")

    return make_math_question(
        prefix="g11_cg_24",
        topic=TOPIC_NAME,
        subskill="24_equal_chords_subtend_equal_angles_centre",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_24",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{base_ang}^\circ",
        answer_sympy=str(base_ang),
        sample_answer=rf"C\hat{{O}}D = {ang_centre}^\circ \text{{ (equal chords; equal }}\angle\text{{s)}}; \; O\hat{{C}}D = \frac{{180^\circ - {ang_centre}^\circ}}{{2}} = {base_ang}^\circ \text{{ (}}\angle\text{{s opp equal radii)}}",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle COD = {ang_centre} deg (equal chords; equal angles)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "OC = OD (radii) / angles opp equal sides", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle OCD = {base_ang} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "First find $C\\hat{O}D$ using equal chords, then use isosceles $\\triangle OCD$ ($OC = OD$ radii).",
            "2_concept": "$C\\hat{O}D = A\\hat{O}B = {ang_centre}^\\circ$ (equal chords; equal $\\angle$s) and $O\\hat{C}D = \\frac{180^\\circ - C\\hat{O}D}{2}$.",
            "3_breakdown": f"$O\\hat{{C}}D = \\frac{{180^\\circ - {ang_centre}^\\circ}}{{2}} = {base_ang}^\\circ$.",
        },
        misconception_tags=["omitted_geometric_reason", "failed_to_identify_equal_radii"],
        keywords=["circle geometry", "equal chords", "centre angle", "radii"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_24_equal_chords_subtend_equal_angles_centre",
        difficulty=difficulty,
    )

# 25. Combined Angle at Centre & Angles in Same Segment Rider
def arch_25_centre_and_same_segment_combined(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    ang_c = r.randint(26, 62)
    ang_o = 2 * ang_c
    ang_d = ang_c
    sum_cd = ang_c + ang_d

    pts = {
        "O": (210.0, 155.0),
        "A": _pt_on_circle(140),
        "B": _pt_on_circle(40),
        "C": _pt_on_circle(235),
        "D": _pt_on_circle(305),
    }

    prompt = (
        f"In the circle with centre $O$, arc $AB$ subtends $A\\hat{{O}}B = {ang_o}^\\circ$ at the centre, "
        f"and subtends $A\\hat{{C}}B$ and $A\\hat{{D}}B$ at the circumference in the same segment. "
        f"Calculate the value of $A\\hat{{C}}B + A\\hat{{D}}B$, stating your geometric reasons."
    )

    diag = circle_geo_svg(
        title=f"Centre & Same Segment: ∠AOB = {ang_o}° — Find ∠ACB + ∠ADB",
        points=pts,
        segments=[("O", "A"), ("O", "B"), ("C", "A"), ("C", "B"), ("D", "A"), ("D", "B")],
        callouts=[(210, 185, f"∠AOB={ang_o}°", "#dc2626"), (210, 290, "Find ∠ACB + ∠ADB", "#1d4ed8")],
    )

    steps = [
        step(from_latex=rf"A\hat{{O}}B = {ang_o}^\circ", to_latex_str=rf"A\hat{{C}}B = \frac{{1}}{{2}}({ang_o}^\circ) = {ang_c}^\circ \quad (\angle \text{{ at centre }} = 2\times\angle \text{{ at circ}})", op="calculate angle ACB from angle at centre", rule="angle at centre = 2 x angle at circumference",),
        step(from_latex=rf"A\hat{{D}}B = A\hat{{C}}B = {ang_d}^\circ \quad (\angle\text{{s in same seg}})", to_latex_str=rf"A\hat{{C}}B + A\hat{{D}}B = {ang_c}^\circ + {ang_d}^\circ = {sum_cd}^\circ", op="find angle ADB and sum both circumference angles", rule="angles in the same segment",),
    ]
    canonical = solution_graph(goal="calculate ACB + ADB", steps=steps, final_latex=rf"{sum_cd}^\circ")

    return make_math_question(
        prefix="g11_cg_25",
        topic=TOPIC_NAME,
        subskill="25_centre_and_same_segment_combined",
        learning_objective_id=f"{LEARNING_OBJECTIVE_ID}_25",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"{sum_cd}^\circ",
        answer_sympy=str(sum_cd),
        sample_answer=rf"A\hat{{C}}B = {ang_c}^\circ \text{{ (}}\angle\text{{ at centre }} = 2\angle\text{{ at circ)}}; \; A\hat{{D}}B = {ang_d}^\circ \text{{ (}}\angle\text{{s in same seg)}}; \; \text{{Sum}} = {sum_cd}^\circ",
        canonical_solution=canonical,
        diagram_spec=diag,
        marking_schema={
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Angle ACB = {ang_c} deg (angle at centre = 2 x angle at circ)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Angle ADB = {ang_d} deg (angles in same seg)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Sum ACB + ADB = {sum_cd} deg", "marks": 1, "editable": True},
            ],
        },
        hints={
            "1_nudge": "Find $A\\hat{C}B$ using the angle at centre theorem, then find $A\\hat{D}B$ using angles in the same segment.",
            "2_concept": "$A\\hat{C}B = A\\hat{D}B = \\frac{1}{2}A\\hat{O}B$, so $A\\hat{C}B + A\\hat{D}B = A\\hat{O}B$.",
            "3_breakdown": f"$A\\hat{{C}}B = {ang_c}^\\circ$ and $A\\hat{{D}}B = {ang_d}^\\circ$, so their sum is ${sum_cd}^\\circ$.",
        },
        misconception_tags=["omitted_geometric_reason", "halved_sum_instead_of_single_angle"],
        keywords=["circle geometry", "angle at centre", "angles in same segment"],
        term=3,
        caps_weight_percent=35,
        suggested_duration_mins=3,
        mode="elementary_25_centre_and_same_segment_combined",
        difficulty=difficulty,
    )

ARCHETYPE_BUILDERS_01_25: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "01_chord_perp_from_centre_bisects_chord": arch_01_chord_perp_from_centre_bisects_chord,
    "02_chord_pythagoras_find_radius": arch_02_chord_pythagoras_find_radius,
    "03_chord_pythagoras_find_chord_length": arch_03_chord_pythagoras_find_chord_length,
    "04_chord_pythagoras_find_perp_distance": arch_04_chord_pythagoras_find_perp_distance,
    "05_chord_arrow_height_sagitta": arch_05_chord_arrow_height_sagitta,
    "06_converse_midpoint_chord_perp_angle": arch_06_converse_midpoint_chord_perp_angle,
    "07_chord_algebraic_pythagoras_variable": arch_07_chord_algebraic_pythagoras_variable,
    "08_two_parallel_chords_distance": arch_08_two_parallel_chords_distance,
    "09_angle_at_centre_find_centre_angle": arch_09_angle_at_centre_find_centre_angle,
    "10_angle_at_centre_find_circumference_angle": arch_10_angle_at_centre_find_circumference_angle,
    "11_angle_at_centre_reflex_obtuse_inscribed": arch_11_angle_at_centre_reflex_obtuse_inscribed,
    "12_angle_at_centre_with_isosceles_radii": arch_12_angle_at_centre_with_isosceles_radii,
    "13_angle_at_centre_reverse_from_radii_base_angle": arch_13_angle_at_centre_reverse_from_radii_base_angle,
    "14_angle_at_centre_algebraic_x": arch_14_angle_at_centre_algebraic_x,
    "15_angle_in_semicircle_basic": arch_15_angle_in_semicircle_basic,
    "16_angle_in_semicircle_pythagoras_chord": arch_16_angle_in_semicircle_pythagoras_chord,
    "17_angle_in_semicircle_with_isosceles_chord": arch_17_angle_in_semicircle_with_isosceles_chord,
    "18_converse_angle_in_semicircle_prove_diameter": arch_18_converse_angle_in_semicircle_prove_diameter,
    "19_angles_in_same_segment_basic": arch_19_angles_in_same_segment_basic,
    "20_angles_in_same_segment_triangle_sum": arch_20_angles_in_same_segment_triangle_sum,
    "21_angles_in_same_segment_parallel_chords": arch_21_angles_in_same_segment_parallel_chords,
    "22_angles_in_same_segment_algebraic_x": arch_22_angles_in_same_segment_algebraic_x,
    "23_equal_chords_subtend_equal_angles_circumference": arch_23_equal_chords_subtend_equal_angles_circumference,
    "24_equal_chords_subtend_equal_angles_centre": arch_24_equal_chords_subtend_equal_angles_centre,
    "25_centre_and_same_segment_combined": arch_25_centre_and_same_segment_combined,
}
