"""Grade 12 Mathematics - Trigonometry: Compound and Double Angles (Archetypes 26-50).
100% Aligned with South African National Curriculum Standards (CAPS Grade 12 Paper 2).
Grounded strictly in curriculum_docs_auto/Mathematics_Gr12/Term 1/05. Trigonometry.md and Syllabus.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from .trigonometry_compound_angles_archetypes_01_25 import (
    _mcq,
    _svg_triangle_2d,
    _typed,
)


def _svg_3d_tower(h_val: float, d_val: float, alpha: int, beta: int) -> Dict[str, Any]:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 280" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">'
        '<polygon points="70,220 300,240 450,190 220,170" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>'
        '<line x1="300" y1="240" x2="300" y2="60" stroke="#0f172a" stroke-width="3"/>'
        '<text x="310" y="55" font-size="14" font-weight="bold" fill="#0f172a">D (Apex)</text>'
        '<text x="310" y="255" font-size="13" font-weight="bold" fill="#0f172a">C (Base)</text>'
        '<line x1="70" y1="220" x2="300" y2="60" stroke="#2563eb" stroke-width="2"/>'
        '<text x="50" y="235" font-size="13" font-weight="bold" fill="#0f172a">A</text>'
        '<line x1="450" y1="190" x2="300" y2="60" stroke="#16a34a" stroke-width="2"/>'
        '<text x="460" y="200" font-size="13" font-weight="bold" fill="#0f172a">B</text>'
        '<line x1="70" y1="220" x2="450" y2="190" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4"/>'
        f'<text x="250" y="220" font-size="11" font-weight="bold" fill="#dc2626">c = {d_val} m</text>'
        f'<text x="110" y="205" font-size="11" font-weight="bold" fill="#2563eb">\u2220CAD = {alpha}\u00b0</text>'
        f'<text x="390" y="180" font-size="11" font-weight="bold" fill="#16a34a">\u2220CBD = {beta}\u00b0</text>'
        '</svg>'
    )
    return {
        "kind": "inline_svg",
        "title": "3D Vertical Tower on Horizontal Plane",
        "svg": svg,
        "diagram_role": "context",
    }


def _svg_3d_prism(ba: float, bc: float, ang_b: int) -> Dict[str, Any]:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 280" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">'
        '<polygon points="120,220 280,240 220,120" fill="#eff6ff" stroke="#1e293b" stroke-width="2"/>'
        '<polygon points="260,150 420,170 360,50" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>'
        '<line x1="120" y1="220" x2="260" y2="150" stroke="#334155" stroke-width="1.5"/>'
        '<line x1="280" y1="240" x2="420" y2="170" stroke="#334155" stroke-width="1.5"/>'
        '<line x1="220" y1="120" x2="360" y2="50" stroke="#334155" stroke-width="1.5"/>'
        '<text x="105" y="235" font-size="13" font-weight="bold" fill="#0f172a">A</text>'
        '<text x="280" y="258" font-size="13" font-weight="bold" fill="#0f172a">B</text>'
        '<text x="210" y="110" font-size="13" font-weight="bold" fill="#0f172a">C</text>'
        '<text x="250" y="145" font-size="13" font-weight="bold" fill="#0f172a">D</text>'
        '<text x="430" y="175" font-size="13" font-weight="bold" fill="#0f172a">E</text>'
        '<text x="365" y="45" font-size="13" font-weight="bold" fill="#0f172a">F</text>'
        f'<text x="175" y="245" font-size="11" font-weight="bold" fill="#2563eb">BA = {ba}</text>'
        f'<text x="260" y="180" font-size="11" font-weight="bold" fill="#16a34a">BC = {bc}</text>'
        f'<text x="235" y="215" font-size="11" font-weight="bold" fill="#dc2626">\u2220B = {ang_b}\u00b0</text>'
        '</svg>'
    )
    return {
        "kind": "inline_svg",
        "title": "3D Triangular Prism Setup",
        "svg": svg,
        "diagram_role": "context",
    }


def _svg_two_buildings(dist: int, ang_elev: int, ang_dep: int, h_p: float, h_q: float) -> Dict[str, Any]:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 280" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">'
        '<line x1="40" y1="240" x2="480" y2="240" stroke="#334155" stroke-width="2"/>'
        '<rect x="80" y="120" width="70" height="120" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>'
        '<text x="95" y="180" font-size="12" font-weight="bold" fill="#0f172a">P</text>'
        '<rect x="350" y="40" width="90" height="200" fill="#cbd5e1" stroke="#0f172a" stroke-width="2"/>'
        '<text x="385" y="140" font-size="12" font-weight="bold" fill="#0f172a">Q</text>'
        '<line x1="150" y1="120" x2="350" y2="120" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>'
        '<line x1="150" y1="120" x2="350" y2="40" stroke="#2563eb" stroke-width="1.5"/>'
        '<line x1="150" y1="120" x2="350" y2="240" stroke="#dc2626" stroke-width="1.5"/>'
        f'<text x="230" y="110" font-size="11" font-weight="bold" fill="#2563eb">\u2191 {ang_elev}\u00b0</text>'
        f'<text x="230" y="145" font-size="11" font-weight="bold" fill="#dc2626">\u2193 {ang_dep}\u00b0</text>'
        f'<text x="230" y="258" font-size="12" font-weight="bold" fill="#0f172a">{dist} m</text>'
        '</svg>'
    )
    return {
        "kind": "inline_svg",
        "title": "Two Buildings: Angles of Elevation and Depression",
        "svg": svg,
        "diagram_role": "context",
    }


def _svg_surveyor_theodolite(d: int, ang: int, h_inst: float, h_tot: float) -> Dict[str, Any]:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 260" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">'
        '<line x1="40" y1="220" x2="480" y2="220" stroke="#334155" stroke-width="2"/>'
        '<line x1="100" y1="220" x2="100" y2="170" stroke="#0f172a" stroke-width="3"/>'
        '<circle cx="100" cy="165" r="5" fill="#2563eb"/>'
        f'<text x="60" y="195" font-size="11" font-weight="bold" fill="#0f172a">{h_inst} m</text>'
        '<rect x="380" y="40" width="30" height="180" fill="#94a3b8" stroke="#0f172a" stroke-width="2"/>'
        '<text x="420" y="130" font-size="13" font-weight="bold" fill="#0f172a">Tower</text>'
        '<line x1="100" y1="165" x2="380" y2="165" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>'
        '<line x1="100" y1="165" x2="380" y2="40" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="140" y="155" font-size="11" font-weight="bold" fill="#2563eb">{ang}\u00b0</text>'
        f'<text x="230" y="240" font-size="12" font-weight="bold" fill="#0f172a">d = {d} m</text>'
        '</svg>'
    )
    return {
        "kind": "inline_svg",
        "title": "Surveyor with Theodolite Angle of Elevation",
        "svg": svg,
        "diagram_role": "context",
    }


def _svg_pole_observer(h_bd: float, ang_p: int, bp: float) -> Dict[str, Any]:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 260" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">'
        '<line x1="50" y1="220" x2="470" y2="220" stroke="#334155" stroke-width="2"/>'
        '<line x1="380" y1="220" x2="380" y2="60" stroke="#0f172a" stroke-width="3"/>'
        '<text x="390" y="60" font-size="13" font-weight="bold" fill="#0f172a">B</text>'
        '<text x="390" y="235" font-size="13" font-weight="bold" fill="#0f172a">D</text>'
        f'<text x="400" y="140" font-size="11" font-weight="bold" fill="#2563eb">h = {int(h_bd)} m</text>'
        '<circle cx="120" cy="220" r="5" fill="#dc2626"/>'
        '<text x="110" y="240" font-size="13" font-weight="bold" fill="#0f172a">P</text>'
        '<line x1="120" y1="220" x2="380" y2="60" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="160" y="210" font-size="11" font-weight="bold" fill="#2563eb">{ang_p}\u00b0</text>'
        f'<text x="230" y="130" font-size="11" font-weight="bold" fill="#0f172a">PB = ?</text>'
        '</svg>'
    )
    return {
        "kind": "inline_svg",
        "title": "Observer and Vertical Pole BD",
        "svg": svg,
        "diagram_role": "context",
    }


def _svg_3d_tower_formula(d_name: str, apex_label: str) -> Dict[str, Any]:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 280" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">'
        '<polygon points="70,220 300,240 450,190 220,170" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>'
        '<line x1="300" y1="240" x2="300" y2="60" stroke="#0f172a" stroke-width="3"/>'
        f'<text x="310" y="55" font-size="14" font-weight="bold" fill="#0f172a">{apex_label}</text>'
        '<text x="310" y="255" font-size="13" font-weight="bold" fill="#0f172a">C</text>'
        '<line x1="70" y1="220" x2="300" y2="60" stroke="#2563eb" stroke-width="2"/>'
        '<text x="50" y="235" font-size="13" font-weight="bold" fill="#0f172a">A</text>'
        '<line x1="450" y1="190" x2="300" y2="60" stroke="#16a34a" stroke-width="2"/>'
        '<text x="460" y="200" font-size="13" font-weight="bold" fill="#0f172a">B</text>'
        '<line x1="70" y1="220" x2="450" y2="190" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="250" y="220" font-size="12" font-weight="bold" fill="#dc2626">AB = {d_name}</text>'
        '<text x="110" y="205" font-size="11" font-weight="bold" fill="#2563eb">\u03b1</text>'
        '<text x="390" y="180" font-size="11" font-weight="bold" fill="#16a34a">\u03b2</text>'
        '</svg>'
    )
    return {
        "kind": "inline_svg",
        "title": "3D Mast Formula Derivation Setup",
        "svg": svg,
        "diagram_role": "context",
    }


def _svg_3d_mast_cosine(theta_sym: str, h_sym: str) -> Dict[str, Any]:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 280" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">'
        '<polygon points="120,230 380,240 260,170" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>'
        '<line x1="260" y1="170" x2="260" y2="50" stroke="#0f172a" stroke-width="3"/>'
        f'<text x="270" y="55" font-size="13" font-weight="bold" fill="#0f172a">D (height {h_sym})</text>'
        '<text x="270" y="175" font-size="13" font-weight="bold" fill="#0f172a">A (base)</text>'
        '<line x1="120" y1="230" x2="260" y2="50" stroke="#2563eb" stroke-width="2"/>'
        '<text x="100" y="240" font-size="13" font-weight="bold" fill="#0f172a">B</text>'
        '<line x1="380" y1="240" x2="260" y2="50" stroke="#16a34a" stroke-width="2"/>'
        '<text x="395" y="245" font-size="13" font-weight="bold" fill="#0f172a">C</text>'
        '<line x1="120" y1="230" x2="380" y2="240" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4"/>'
        f'<text x="250" y="210" font-size="12" font-weight="bold" fill="#0f172a">\u2220BAC = {theta_sym}</text>'
        '<text x="140" y="215" font-size="11" font-weight="bold" fill="#2563eb">\u03b2</text>'
        '<text x="350" y="225" font-size="11" font-weight="bold" fill="#16a34a">\u03b1</text>'
        '</svg>'
    )
    return {
        "kind": "inline_svg",
        "title": "3D Cosine Rule Formula Derivation Setup",
        "svg": svg,
        "diagram_role": "context",
    }


# ---------------------------------------------------------------------------
# Archetypes 26 - 36 (2D Sine/Cosine/Area Rules & Elevation)
# ---------------------------------------------------------------------------

def _b26_sine_rule_solve_side_2d(rng: random.Random) -> Dict[str, Any]:
    ang_a = rng.choice([42, 46, 50, 54])
    ang_b = rng.choice([58, 62, 66, 70])
    side_a = rng.choice([6, 8, 10, 12])
    # a / sin A = b / sin B => b = a * sin B / sin A
    rad_a = math.radians(ang_a)
    rad_b = math.radians(ang_b)
    side_b = round(side_a * math.sin(rad_b) / math.sin(rad_a), 1)
    side_b_str = f"{side_b}".replace(".", "{,}")

    svg = _svg_triangle_2d(
        (220, 50), (80, 230), (360, 230),
        ("C", "A", "B"),
        [
            {"x": 130, "y": 210, "text": f"{ang_a}\u00b0", "color": "#2563eb"},
            {"x": 310, "y": 210, "text": f"{ang_b}\u00b0", "color": "#16a34a"},
            {"x": 310, "y": 130, "text": f"BC = {side_a} cm", "color": "#0f172a"},
            {"x": 130, "y": 130, "text": "AC = ?", "color": "#dc2626"},
        ]
    )
    prompt = (
        f"Refer to the triangle below. In $\\Delta ABC$, $BC = {side_a}\\text{{ cm}}$, "
        f"$\\angle CAB = {ang_a}^\\circ$ and $\\angle CBA = {ang_b}^\\circ$.\n"
        f"Use the Sine Rule to calculate the length of $AC$, correct to 1 decimal place."
    )
    ans = f"{side_b}"
    accepted = [ans, f"{side_b_str}", f"{side_b} cm", f"{side_b_str} cm"]
    sol = (
        f"1. State the Sine Rule:\n"
        f"$$\\frac{{AC}}{{\\sin B}} = \\frac{{BC}}{{\\sin A}}$$\n"
        f"2. Substitute known values:\n"
        f"$$\\frac{{AC}}{{\\sin {ang_b}^\\circ}} = \\frac{{{side_a}}}{{\\sin {ang_a}^\\circ}}$$\n"
        f"3. Solve for $AC$:\n"
        f"$$AC = \\frac{{{side_a} \\times \\sin {ang_b}^\\circ}}{{\\sin {ang_a}^\\circ}} \\approx {side_b_str}\\text{{ cm}}$$"
    )
    return _typed(
        subskill="26_sine_rule_solve_side_2d",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-26",
        concept_id="sine_rule_side_calculation",
        misconception_tags=["inverted_sine_rule_ratio"],
        hints=[
            r"Match opposite sides with their opposite angles: AC is opposite \hat{B} and BC is opposite \hat{A}.",
            rf"Use the formula AC = BC \cdot \frac{{\sin B}}{{\sin A}}.",
            f"Calculate: {side_a} * sin({ang_b}°) / sin({ang_a}°) = {side_b}.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b27_sine_rule_solve_angle_2d(rng: random.Random) -> Dict[str, Any]:
    side_p = rng.choice([12, 14, 16])
    side_q = rng.choice([7, 8, 9])
    ang_p = rng.choice([28, 32, 35])
    # sin Q / q = sin P / p => sin Q = q * sin P / p
    rad_p = math.radians(ang_p)
    sin_q = side_q * math.sin(rad_p) / side_p
    ang_q = round(math.degrees(math.asin(sin_q)), 1)
    ang_q_str = f"{ang_q}".replace(".", "{,}")

    svg = _svg_triangle_2d(
        (220, 60), (70, 220), (370, 220),
        ("R", "P", "Q"),
        [
            {"x": 120, "y": 200, "text": f"{ang_p}\u00b0", "color": "#2563eb"},
            {"x": 130, "y": 130, "text": f"PR = {side_q} m", "color": "#0f172a"},
            {"x": 310, "y": 130, "text": f"QR = {side_p} m", "color": "#0f172a"},
        ]
    )
    prompt = (
        f"Refer to the triangle below. In $\\Delta PQR$, $QR = {side_p}\\text{{ m}}$, "
        f"$PR = {side_q}\\text{{ m}}$, and $\\angle P = {ang_p}^\\circ$.\n"
        f"Calculate the size of acute angle $Q$, correct to 1 decimal place."
    )
    ans = rf"{ang_q}^\circ"
    accepted = [f"{ang_q}", f"{ang_q_str}", rf"{ang_q}^\circ", rf"{ang_q_str}^\circ"]
    sol = (
        f"1. Apply the Sine Rule for angle $Q$:\n"
        f"$$\\frac{{\\sin Q}}{{PR}} = \\frac{{\\sin P}}{{QR}}$$\n"
        f"$$\\sin Q = \\frac{{{side_q} \\times \\sin {ang_p}^\\circ}}{{{side_p}}} \\approx {round(sin_q, 4)}$$\n"
        f"2. Take the inverse sine:\n"
        f"$$Q = \\arcsin({round(sin_q, 4)}) \\approx {ang_q_str}^\\circ$$"
    )
    return _typed(
        subskill="27_sine_rule_solve_angle_2d",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-27",
        concept_id="sine_rule_angle_calculation",
        misconception_tags=["used_degree_mode_instead_of_arcsin"],
        hints=[
            r"Set up: \frac{\sin Q}{q} = \frac{\sin P}{p}.",
            f"Multiply both sides by {side_q} to isolate sin Q.",
            f"Take arcsin to find Q: {ang_q}°.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b28_sine_rule_ambiguous_case(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"In $\Delta ABC$, $a = 7\text{ cm}$, $b = 9\text{ cm}$, and $\angle A = 40^\circ$." + "\n"
        r"Why does this information give rise to the **ambiguous case** (two possible triangles)?"
    )
    correct = r"Because $b\sin A < a < b$ ($5{,}78 < 7 < 9$), allowing angle $B$ to be acute ($55{,}7^\circ$) or obtuse ($124{,}3^\circ$) with $\angle A + \angle B < 180^\circ$."
    dist = [
        r"Because $\sin B > 1$, which produces two imaginary solutions.",
        r"Because $a > b$, which automatically creates two symmetric triangles.",
        r"Because angle $A$ is an obtuse angle.",
    ]
    sol = (
        r"1. Calculate the altitude: $h = b\sin A = 9\sin 40^\circ \approx 5{,}78\text{ cm}$." + "\n"
        r"2. Since $h < a < b$ ($5{,}78 < 7 < 9$), side $a$ can pivot into two distinct valid triangle positions." + "\n"
        r"3. $\sin B = \frac{9\sin 40^\circ}{7} \approx 0{,}8265 \implies B \approx 55{,}7^\circ$ or $B \approx 124{,}3^\circ$." + "\n"
        r"4. Since $40^\circ + 124{,}3^\circ = 164{,}3^\circ < 180^\circ$, both triangles are valid."
    )
    return _mcq(
        rng,
        subskill="28_sine_rule_ambiguous_case",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-28",
        concept_id="ambiguous_case_sine_rule",
        misconception_tags=["ignored_obtuse_triangle_possibility"],
        hints=[
            r"Check the height h = b\sin A compared to side a.",
            r"When b\sin A < a < b, two triangles can be constructed.",
            "Verify that 180° - B produces a valid triangle where the sum of angles is less than 180°.",
        ],
        worked_solution=sol,
    )


def _b29_cosine_rule_solve_side_2d(rng: random.Random) -> Dict[str, Any]:
    b_val = rng.choice([10, 12, 14])
    c_val = rng.choice([8, 9, 11])
    ang_a = rng.choice([55, 60, 102, 110])
    # a^2 = b^2 + c^2 - 2bc cos A
    rad = math.radians(ang_a)
    a_sq = b_val**2 + c_val**2 - 2 * b_val * c_val * math.cos(rad)
    a_val = round(math.sqrt(a_sq), 1)
    a_str = f"{a_val}".replace(".", "{,}")

    svg = _svg_triangle_2d(
        (220, 60), (70, 220), (370, 220),
        ("A", "B", "C"),
        [
            {"x": 220, "y": 90, "text": f"{ang_a}\u00b0", "color": "#2563eb"},
            {"x": 130, "y": 140, "text": f"c = {c_val} cm", "color": "#0f172a"},
            {"x": 310, "y": 140, "text": f"b = {b_val} cm", "color": "#0f172a"},
            {"x": 220, "y": 240, "text": "a = ?", "color": "#dc2626"},
        ]
    )
    prompt = (
        f"Refer to the triangle below. In $\\Delta ABC$, $b = {b_val}\\text{{ cm}}$, "
        f"$c = {c_val}\\text{{ cm}}$, and $\\angle A = {ang_a}^\\circ$.\n"
        f"Calculate the length of side $a$, correct to 1 decimal place."
    )
    ans = f"{a_val}"
    accepted = [ans, a_str, f"{a_val} cm", f"{a_str} cm"]
    sol = (
        f"1. Apply the Cosine Rule for side $a$:\n"
        f"$$a^2 = b^2 + c^2 - 2bc\\cos A$$\n"
        f"2. Substitute values:\n"
        f"$$a^2 = {b_val}^2 + {c_val}^2 - 2({b_val})({c_val})\\cos {ang_a}^\\circ$$\n"
        f"$$a^2 = {b_val**2 + c_val**2} - {2*b_val*c_val}\\cos {ang_a}^\\circ \\approx {round(a_sq, 2)}$$\n"
        f"3. Take square root: $a \\approx {a_str}\\text{{ cm}}$."
    )
    return _typed(
        subskill="29_cosine_rule_solve_side_2d",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-29",
        concept_id="cosine_rule_side_calculation",
        misconception_tags=["sign_error_with_obtuse_cosine"],
        hints=[
            r"Use a^2 = b^2 + c^2 - 2bc\cos A.",
            rf"Substitute b = {b_val}, c = {c_val}, and \hat{{A}} = {ang_a}^\circ.",
            f"Square root the result to find a: {a_val} cm.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b30_cosine_rule_solve_angle_2d(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([7, 8, 9])
    b = rng.choice([10, 11, 12])
    c = rng.choice([13, 14, 15])
    # Find largest angle C opposite largest side c:
    # cos C = (a^2 + b^2 - c^2) / (2ab)
    cos_c = (a**2 + b**2 - c**2) / (2 * a * b)
    ang_c = round(math.degrees(math.acos(cos_c)), 1)
    ang_str = f"{ang_c}".replace(".", "{,}")

    svg = _svg_triangle_2d(
        (180, 60), (60, 220), (400, 220),
        ("C", "A", "B"),
        [
            {"x": 100, "y": 140, "text": f"b = {b} cm", "color": "#0f172a"},
            {"x": 300, "y": 130, "text": f"a = {a} cm", "color": "#0f172a"},
            {"x": 230, "y": 240, "text": f"c = {c} cm", "color": "#0f172a"},
        ]
    )
    prompt = (
        f"Refer to the triangle below. The sides of $\\Delta ABC$ are $a = {a}\\text{{ cm}}$, "
        f"$b = {b}\\text{{ cm}}$, and $c = {c}\\text{{ cm}}$.\n"
        f"Calculate the size of the largest angle $\\angle C$, correct to 1 decimal place."
    )
    ans = rf"{ang_c}^\circ"
    accepted = [f"{ang_c}", ang_str, ans, rf"{ang_str}^\circ"]
    sol = (
        f"1. The largest angle lies opposite the longest side ($c = {c}\\text{{ cm}}$).\n"
        f"2. Rearrange the Cosine Rule for $\\cos C$:\n"
        f"$$\\cos C = \\frac{{a^2 + b^2 - c^2}}{{2ab}} = \\frac{{{a}^2 + {b}^2 - {c}^2}}{{2({a})({b})}} = \\frac{{{a**2 + b**2 - c**2}}}{{{2*a*b}}}$$\n"
        f"3. Calculate angle $C$:\n"
        f"$$C = \\arccos({round(cos_c, 4)}) \\approx {ang_str}^\\circ$$"
    )
    return _typed(
        subskill="30_cosine_rule_solve_angle_2d",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-30",
        concept_id="cosine_rule_angle_calculation",
        misconception_tags=["wrong_side_subtraction_in_cosine_rule"],
        hints=[
            r"The largest angle is opposite the longest side.",
            r"Formula: \cos C = \frac{a^2 + b^2 - c^2}{2ab}.",
            f"Evaluate arccos to get {ang_c}°.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b31_area_rule_triangle_calculation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([6, 8, 10])
    b = rng.choice([9, 12, 14])
    ang = rng.choice([48, 52, 60, 115])
    # Area = 0.5 * a * b * sin(ang)
    rad = math.radians(ang)
    area = round(0.5 * a * b * math.sin(rad), 1)
    area_str = f"{area}".replace(".", "{,}")

    svg = _svg_triangle_2d(
        (220, 60), (70, 220), (370, 220),
        ("C", "A", "B"),
        [
            {"x": 220, "y": 90, "text": f"{ang}\u00b0", "color": "#2563eb"},
            {"x": 130, "y": 140, "text": f"b = {b} cm", "color": "#0f172a"},
            {"x": 310, "y": 140, "text": f"a = {a} cm", "color": "#0f172a"},
        ]
    )
    prompt = (
        f"Refer to the triangle below. In $\\Delta ABC$, $a = {a}\\text{{ cm}}$, "
        f"$b = {b}\\text{{ cm}}$, and $\\angle C = {ang}^\\circ$.\n"
        f"Calculate the area of $\\Delta ABC$, correct to 1 decimal place."
    )
    ans = f"{area}"
    accepted = [ans, area_str, f"{area} cm^2", f"{area_str} cm^2"]
    sol = (
        f"1. Apply the Area Rule:\n"
        f"$$\\text{{Area}} = \\frac{{1}}{{2}}ab\\sin C$$\n"
        f"2. Substitute values:\n"
        f"$$\\text{{Area}} = \\frac{{1}}{{2}}({a})({b})\\sin {ang}^\\circ = {0.5*a*b} \\times \\sin {ang}^\\circ \\approx {area_str}\\text{{ cm}}^2$$"
    )
    return _typed(
        subskill="31_area_rule_triangle_calculation",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-31",
        concept_id="area_rule_triangle",
        misconception_tags=["forgot_half_factor_in_area_rule"],
        hints=[
            r"Use \text{Area} = \frac{1}{2}ab\sin C.",
            rf"Substitute: 0.5 * {a} * {b} * \sin({ang}^\circ).",
            f"The computed area is {area} cm².",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b32_area_rule_quadrilateral_decomposition(rng: random.Random) -> Dict[str, Any]:
    # Two triangles: T1 with sides a1, b1, angle1 and T2 with a2, b2, angle2
    a1, b1, ang1 = 4, 5, 60
    a2, b2, ang2 = 3, 6, 45
    area1 = 0.5 * a1 * b1 * math.sin(math.radians(ang1))
    area2 = 0.5 * a2 * b2 * math.sin(math.radians(ang2))
    tot_area = round(area1 + area2, 1)
    tot_str = f"{tot_area}".replace(".", "{,}")

    prompt = (
        f"A plot of land in the shape of a quadrilateral $ABCD$ is divided by diagonal $BD$ into two triangles:\n"
        f"- In $\\Delta ABD$: $AB = {a1}\\text{{ m}}$, $AD = {b1}\\text{{ m}}$, and $\\angle BAD = {ang1}^\\circ$.\n"
        f"- In $\\Delta BCD$: $BC = {a2}\\text{{ m}}$, $CD = {b2}\\text{{ m}}$, and $\\angle BCD = {ang2}^\\circ$.\n"
        f"Calculate the total area of quadrilateral $ABCD$, correct to 1 decimal place."
    )
    ans = f"{tot_area}"
    accepted = [ans, tot_str, f"{tot_area} m^2", f"{tot_str} m^2"]
    sol = (
        f"1. Area of $\\Delta ABD = \\frac{{1}}{{2}}({a1})({b1})\\sin {ang1}^\\circ = {0.5*a1*b1}\\sin {ang1}^\\circ \\approx {round(area1, 2)}\\text{{ m}}^2$.\n"
        f"2. Area of $\\Delta BCD = \\frac{{1}}{{2}}({a2})({b2})\\sin {ang2}^\\circ = {0.5*a2*b2}\\sin {ang2}^\\circ \\approx {round(area2, 2)}\\text{{ m}}^2$.\n"
        f"3. Total Area $= \\text{{Area}}(\\Delta ABD) + \\text{{Area}}(\\Delta BCD) \\approx {tot_str}\\text{{ m}}^2$."
    )
    return _typed(
        subskill="32_area_rule_quadrilateral_decomposition",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-32",
        concept_id="area_rule_quadrilateral_composite",
        misconception_tags=["added_angles_instead_of_areas"],
        hints=[
            "Compute the area of each triangle separately using Area = 0.5 * a * b * sin(theta).",
            "Sum the areas of the two triangles.",
            f"Total area is {tot_area} m².",
        ],
        worked_solution=sol,
    )


def _b33_angle_elevation_single_triangle(rng: random.Random) -> Dict[str, Any]:
    h = rng.choice([45, 60, 75, 80])
    ang = rng.choice([12, 15, 18, 22])
    # tan ang = h / d => d = h / tan ang
    rad = math.radians(ang)
    d = round(h / math.tan(rad), 1)
    d_str = f"{d}".replace(".", "{,}")

    prompt = (
        f"An observer standing on top of a vertical cliff of height ${h}\\text{{ m}}$ spots a boat in the sea at an "
        f"angle of depression of ${ang}^\\circ$.\n"
        f"Calculate the distance from the boat to the base of the cliff on the water surface, correct to 1 decimal place."
    )
    ans = f"{d}"
    accepted = [ans, d_str, f"{d} m", f"{d_str} m"]
    sol = (
        f"1. The angle of depression from the cliff top equals the angle of elevation from the boat to the top (${ang}^\\circ$).\n"
        f"2. In the right-angled triangle formed by cliff height and ground distance:\n"
        f"$$\\tan {ang}^\\circ = \\frac{{\\text{{Opposite}}}}{{\\text{{Adjacent}}}} = \\frac{{{h}}}{{d}}$$\n"
        f"3. Solve for $d$:\n"
        f"$$d = \\frac{{{h}}}{{\\tan {ang}^\\circ}} \\approx {d_str}\\text{{ m}}$$"
    )
    return _typed(
        subskill="33_angle_elevation_single_triangle",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-33",
        concept_id="angle_of_depression_right_triangle",
        misconception_tags=["confused_depression_angle_with_zenith_angle"],
        hints=[
            r"Angle of depression = angle of elevation from the ground: \theta = " + f"{ang}°.",
            rf"Use \tan({ang}^\circ) = \frac{{{h}}}{{d}}.",
            f"Calculate d = {h} / tan({ang}°) = {d} m.",
        ],
        worked_solution=sol,
    )


def _b34_angle_elevation_depression_two_buildings(rng: random.Random) -> Dict[str, Any]:
    dist = rng.choice([30, 35, 40])
    ang_elev = rng.choice([20, 24, 28])
    ang_dep = rng.choice([30, 34, 38])
    # h_P = dist * tan(ang_dep)
    # h_above = dist * tan(ang_elev)
    # h_Q = h_P + h_above
    rad_dep = math.radians(ang_dep)
    rad_elev = math.radians(ang_elev)
    h_p = round(dist * math.tan(rad_dep), 1)
    h_q = round(h_p + dist * math.tan(rad_elev), 1)
    h_p_str = f"{h_p}".replace(".", "{,}")
    h_q_str = f"{h_q}".replace(".", "{,}")
    svg = _svg_two_buildings(dist, ang_elev, ang_dep, h_p, h_q)

    prompt = (
        f"Refer to the diagram below. Two buildings $P$ and $Q$ stand across a street ${dist}\\text{{ m}}$ apart on horizontal ground.\n"
        f"From a point on the roof of Building $P$, the angle of elevation of the top of Building $Q$ is ${ang_elev}^\\circ$, "
        f"and the angle of depression of the base of Building $Q$ is ${ang_dep}^\\circ$.\n"
        f"Calculate the height of Building $Q$, correct to 1 decimal place."
    )
    ans = f"{h_q}"
    accepted = [ans, h_q_str, f"{h_q} m", f"{h_q_str} m"]
    sol = (
        f"1. Let the horizontal line from roof of $P$ to building $Q$ have length ${dist}\\text{{ m}}$.\n"
        f"2. Height of Building $P$ equals the lower segment of $Q$:\n"
        f"$$h_P = {dist} \\times \\tan {ang_dep}^\\circ \\approx {h_p_str}\\text{{ m}}$$\n"
        f"3. Height of $Q$ above the roof of $P$:\n"
        f"$$h_{{\\text{{upper}}}} = {dist} \\times \\tan {ang_elev}^\\circ \\approx {round(dist * math.tan(rad_elev), 1)}\\text{{ m}}$$\n"
        f"4. Total height of Building $Q = h_P + h_{{\\text{{upper}}}} \\approx {h_q_str}\\text{{ m}}$."
    )
    return _typed(
        subskill="34_angle_elevation_depression_two_buildings",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-34",
        concept_id="elevation_depression_composite",
        misconception_tags=["forgot_to_add_lower_and_upper_segments"],
        hints=[
            rf"Lower segment = {dist} * \tan({ang_dep}^\circ).",
            rf"Upper segment = {dist} * \tan({ang_elev}^\circ).",
            "Sum both segments to find the total height of Building Q.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b35_angle_elevation_surveyor_theodolite(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([50, 60, 80])
    ang = rng.choice([30, 35, 40])
    h_inst = rng.choice([1.5, 1.6, 1.8])
    h_tot = round(h_inst + d * math.tan(math.radians(ang)), 1)
    h_tot_str = f"{h_tot}".replace(".", "{,}")
    svg = _svg_surveyor_theodolite(d, ang, h_inst, h_tot)

    prompt = (
        f"Refer to the diagram below. A surveyor stands ${d}\\text{{ metres}}$ from the base of a vertical tower and uses a "
        f"${h_inst}\\text{{ metre}}$ tall theodolite to measure the angle of elevation to the top of the tower as ${ang}^\\circ$.\n"
        f"Calculate the total height of the tower, correct to 1 decimal place."
    )
    ans = f"{h_tot}"
    accepted = [ans, h_tot_str, f"{h_tot} m", f"{h_tot_str} m"]
    sol = (
        f"1. Let $h_{{\\text{{triangle}}}}$ be the height of the tower above the theodolite:\n"
        f"$$\\tan {ang}^\\circ = \\frac{{h_{{\\text{{triangle}}}}}}{{{d}}} \\implies h_{{\\text{{triangle}}}} = {d} \\times \\tan {ang}^\\circ \\approx {round(d * math.tan(math.radians(ang)), 1)}\\text{{ m}}$$\n"
        f"2. Add the height of the theodolite instrument:\n"
        f"$$\\text{{Total Height}} = {h_inst} + h_{{\\text{{triangle}}}} \\approx {h_tot_str}\\text{{ m}}$$"
    )
    return _typed(
        subskill="35_angle_elevation_surveyor_theodolite",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-35",
        concept_id="surveyor_elevation_with_instrument_height",
        misconception_tags=["forgot_to_add_instrument_height"],
        hints=[
            r"Find the vertical height above eye-level using d * \tan(\theta).",
            f"Add the theodolite height ({h_inst} m) to get the total tower height.",
            f"Total height = {h_tot} m.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b36_2d_trig_bearings_and_navigation(rng: random.Random) -> Dict[str, Any]:
    d1 = rng.choice([12, 15, 20])
    d2 = rng.choice([8, 10, 14])
    # Ship sails due East (090), then on bearing 150 (turns 60 deg right)
    # Interior angle = 180 - 60 = 120 deg
    interior_ang = 120
    d3_sq = d1**2 + d2**2 - 2 * d1 * d2 * math.cos(math.radians(interior_ang))
    d3 = round(math.sqrt(d3_sq), 1)
    d3_str = f"{d3}".replace(".", "{,}")

    prompt = (
        f"A boat departs port $A$ and sails ${d1}\\text{{ km}}$ on a bearing of $090^\\circ$ to point $B$.\n"
        f"At point $B$, it alters course to a bearing of $150^\\circ$ and sails for ${d2}\\text{{ km}}$ to point $C$.\n"
        f"Calculate the direct distance from point $C$ back to port $A$, correct to 1 decimal place."
    )
    ans = f"{d3}"
    accepted = [ans, d3_str, f"{d3} km", f"{d3_str} km"]
    sol = (
        f"1. Determine the interior angle $\\angle ABC$:\n"
        f"$$\\angle ABC = 180^\\circ - (150^\\circ - 90^\\circ) = 180^\\circ - 60^\\circ = {interior_ang}^\\circ$$\n"
        f"2. Apply the Cosine Rule in $\\Delta ABC$:\n"
        f"$$AC^2 = AB^2 + BC^2 - 2(AB)(BC)\\cos {interior_ang}^\\circ$$\n"
        f"$$AC^2 = {d1}^2 + {d2}^2 - 2({d1})({d2})\\cos 120^\\circ = {d1**2 + d2**2} - ({2*d1*d2})(-0{{,}}5) = {d3_sq}$$\n"
        f"3. $AC = \\sqrt{{{d3_sq}}} \\approx {d3_str}\\text{{ km}}$."
    )
    return _typed(
        subskill="36_2d_trig_bearings_and_navigation",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-36",
        concept_id="bearings_cosine_rule",
        misconception_tags=["interior_bearing_angle_miscalculation"],
        hints=[
            "Draw the north lines at A and B to find the interior angle B.",
            rf"The interior angle is 180° - 60° = {interior_ang}°.",
            f"Use the Cosine Rule to find the direct distance AC: {d3} km.",
        ],
        worked_solution=sol,
    )


# ---------------------------------------------------------------------------
# Archetypes 37 - 50 (3D Trigonometry & Advanced Synthesis)
# ---------------------------------------------------------------------------

def _b37_3d_vertical_tower_horizontal_ground(rng: random.Random) -> Dict[str, Any]:
    alpha = rng.choice([20, 25, 28, 30])
    beta = rng.choice([35, 38, 42, 45])
    theta = rng.choice([40, 45, 50, 55])
    c = rng.choice([120, 140, 160, 180])
    # AC = h / tan alpha, BC = h / tan beta
    # In horizontal triangle ABC: c^2 = AC^2 + BC^2 - 2(AC)(BC) cos theta
    # c^2 = h^2 [ (1/tan a)^2 + (1/tan b)^2 - 2 cos theta / (tan a tan b) ]
    t_a = math.tan(math.radians(alpha))
    t_b = math.tan(math.radians(beta))
    term = (1 / t_a**2) + (1 / t_b**2) - (2 * math.cos(math.radians(theta)) / (t_a * t_b))
    h = round(math.sqrt(c**2 / term), 1)
    h_str = f"{h}".replace(".", "{,}")

    svg = _svg_3d_tower(h, c, alpha, beta)
    prompt = (
        f"Refer to the 3D diagram below. A vertical cellphone mast $CD$ of height $h$ stands on horizontal ground with base $C$.\n"
        f"Two points $A$ and $B$ are on the ground such that $AB = {c}\\text{{ m}}$, $\\angle CAD = {alpha}^\\circ$, "
        f"$\\angle CBD = {beta}^\\circ$, and $\\angle ACB = {theta}^\\circ$.\n"
        f"Calculate the height $h$ of the mast, correct to 1 decimal place."
    )
    ans = f"{h}"
    accepted = [ans, h_str, f"{h} m", f"{h_str} m"]
    sol = (
        f"1. In vertical right-angled $\\Delta ACD$:\n"
        f"$$\\tan {alpha}^\\circ = \\frac{{h}}{{AC}} \\implies AC = \\frac{{h}}{{\\tan {alpha}^\\circ}}$$\n"
        f"2. In vertical right-angled $\\Delta BCD$:\n"
        f"$$\\tan {beta}^\\circ = \\frac{{h}}{{BC}} \\implies BC = \\frac{{h}}{{\\tan {beta}^\\circ}}$$\n"
        f"3. In horizontal $\\Delta ABC$, apply the Cosine Rule:\n"
        f"$$AB^2 = AC^2 + BC^2 - 2(AC)(BC)\\cos {theta}^\\circ$$\n"
        f"$${c}^2 = h^2 \\left[\\frac{{1}}{{\\tan^2 {alpha}^\\circ}} + \\frac{{1}}{{\\tan^2 {beta}^\\circ}} - \\frac{{2\\cos {theta}^\\circ}}{{\\tan {alpha}^\\circ\\tan {beta}^\\circ}}\\right]$$\n"
        f"4. Solving yields $h \\approx {h_str}\\text{{ m}}$."
    )
    return _typed(
        subskill="37_3d_vertical_tower_horizontal_ground_distance",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-37",
        concept_id="3d_trig_tower_horizontal_base",
        misconception_tags=["confused_horizontal_and_vertical_planes"],
        hints=[
            r"Express the ground distances AC and BC in terms of h using \tan\alpha and \tan\beta.",
            r"Apply the Cosine Rule in the horizontal triangle ABC: AB^2 = AC^2 + BC^2 - 2 AC BC \cos\theta.",
            f"Substitute known values and solve for h: {h} m.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b38_3d_pyramid_apex_edge_calculation(rng: random.Random) -> Dict[str, Any]:
    lh = rng.choice([3.0, 4.0, 5.0, 6.0])
    ang_hbl = rng.choice([35, 40, 45, 50])
    # LH is perpendicular to LB (angle HLB = 90)
    # tan 40 = LH / LB => LB = LH / tan 40
    lb = round(lh / math.tan(math.radians(ang_hbl)), 1)
    lb_str = f"{lb}".replace(".", "{,}")

    lh_display = int(lh) if lh.is_integer() else lh
    prompt = (
        f"In a triangular pyramid $HABCD$, vertical line $LH$ connects apex $H$ to base point $L$, with $LH = {lh_display}\\text{{ m}}$ and $LH \\perp LB$.\n"
        f"Given that $\\angle HBL = {ang_hbl}^\\circ$ and $\\angle HLB = 90^\\circ$:\n"
        f"Calculate the length of base segment $LB$, correct to 1 decimal place."
    )
    ans = f"{lb}"
    accepted = [ans, lb_str, f"{lb} m", f"{lb_str} m"]
    sol = (
        f"1. In right-angled $\\Delta HLB$, $LH = {lh_display}\\text{{ m}}$ and $\\angle HBL = {ang_hbl}^\\circ$.\n"
        f"2. $\\tan {ang_hbl}^\\circ = \\frac{{LH}}{{LB}} = \\frac{{{lh_display}}}{{LB}}$.\n"
        f"3. $LB = \\frac{{{lh_display}}}{{\\tan {ang_hbl}^\\circ}} = \\frac{{{lh_display}}}{{{round(math.tan(math.radians(ang_hbl)), 4)}}} \\approx {lb_str}\\text{{ m}}$."
    )
    return _typed(
        subskill="38_3d_pyramid_apex_edge_calculation",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-38",
        concept_id="3d_pyramid_vertical_height",
        misconception_tags=["inverted_trig_ratio_in_vertical_triangle"],
        hints=[
            r"Identify that \Delta HLB is a right-angled triangle with \angle HLB = 90^\circ.",
            rf"Use \tan({ang_hbl}^\circ) = \frac{{LH}}{{LB}}.",
            f"Calculate LB = {lh_display} / tan({ang_hbl}°) = {lb} m.",
        ],
        worked_solution=sol,
    )


def _b39_3d_triangular_prism_measurements(rng: random.Random) -> Dict[str, Any]:
    ba = rng.choice([4.0, 5.0, 6.0, 8.0])
    bc = rng.choice([5.0, 6.0, 7.0, 9.0])
    ang_b = rng.choice([45, 50, 55, 60])
    # In triangle ABC: AC^2 = BA^2 + BC^2 - 2 BA BC cos B
    ac_sq = ba**2 + bc**2 - 2 * ba * bc * math.cos(math.radians(ang_b))
    ac = round(math.sqrt(ac_sq), 1)
    ac_str = f"{ac}".replace(".", "{,}")

    ba_disp = int(ba) if ba.is_integer() else ba
    bc_disp = int(bc) if bc.is_integer() else bc
    svg = _svg_3d_prism(ba_disp, bc_disp, ang_b)
    prompt = (
        f"Refer to the triangular prism $ABC.DEF$ shown below. In $\\Delta ABC$, $BA = {ba_disp}\\text{{ units}}$, "
        f"$BC = {bc_disp}\\text{{ units}}$, and $\\angle ABC = {ang_b}^\\circ$.\n"
        f"Calculate the length of diagonal $AC$ on the triangular face, correct to 1 decimal place."
    )
    ans = f"{ac}"
    accepted = [ans, ac_str, f"{ac} units"]
    sol = (
        f"1. Apply the Cosine Rule in $\\Delta ABC$:\n"
        f"$$AC^2 = BA^2 + BC^2 - 2(BA)(BC)\\cos {ang_b}^\\circ$$\n"
        f"$$AC^2 = {ba}^2 + {bc}^2 - 2({ba})({bc})\\cos {ang_b}^\\circ = {ba**2 + bc**2} - {2*ba*bc}\\cos {ang_b}^\\circ \\approx {round(ac_sq, 2)}$$\n"
        f"2. $AC = \\sqrt{{{round(ac_sq, 2)}}} \\approx {ac_str}\\text{{ units}}$."
    )
    return _typed(
        subskill="39_3d_triangular_prism_measurements",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-39",
        concept_id="3d_prism_face_cosine_rule",
        misconception_tags=["treated_isosceles_face_as_right_angled"],
        hints=[
            rf"Use the Cosine Rule on face \Delta ABC with sides BA = {ba_disp}, BC = {bc_disp} and included angle {ang_b}°.",
            rf"AC^2 = {ba_disp}^2 + {bc_disp}^2 - 2({ba_disp})({bc_disp})\cos {ang_b}^\circ.",
            f"AC = {ac} units.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b40_3d_two_vertical_poles_distance(rng: random.Random) -> Dict[str, Any]:
    h_bd = rng.choice([6.0, 7.0, 8.0, 10.0])
    ang_p = rng.choice([18, 22, 25, 30])
    # In triangle BPD, pole BD is vertical, angle BPD = ang_p deg
    # sin ang_p = BD / BP => BP = BD / sin ang_p
    bp = round(h_bd / math.sin(math.radians(ang_p)), 2)
    bp_str = f"{bp}".replace(".", "{,}")
    svg = _svg_pole_observer(h_bd, ang_p, bp)

    prompt = (
        f"Refer to the diagram below. An observer stands at point $P$ on horizontal ground and looks at vertical pole $BD$ of height ${int(h_bd)}\\text{{ m}}$.\n"
        f"The angle of elevation to the top of pole $B$ from point $P$ is ${ang_p}^\\circ$.\n"
        f"Calculate the line-of-sight distance from point $P$ to the top of the pole $B$ (length $PB$), correct to 2 decimal places."
    )
    ans = f"{bp}"
    accepted = [ans, bp_str, f"{bp} m", f"{bp_str} m"]
    sol = (
        f"1. In right-angled $\\Delta BDP$ where $\\angle BDP = 90^\\circ$:\n"
        f"$$\\sin {ang_p}^\\circ = \\frac{{\\text{{Opposite}}}}{{\\text{{Hypotenuse}}}} = \\frac{{BD}}{{PB}}$$\n"
        f"2. Solve for $PB$:\n"
        f"$$PB = \\frac{{{int(h_bd)}}}{{\\sin {ang_p}^\\circ}} = \\frac{{{int(h_bd)}}}{{{round(math.sin(math.radians(ang_p)), 4)}}} \\approx {bp_str}\\text{{ m}}$$"
    )
    return _typed(
        subskill="40_3d_two_vertical_poles_distance_between_tops",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-40",
        concept_id="3d_pole_hypotenuse_calculation",
        misconception_tags=["used_tangent_instead_of_sine_for_hypotenuse"],
        hints=[
            "PB is the hypotenuse of right-angled triangle BDP.",
            rf"Use \sin({ang_p}^\circ) = \frac{{BD}}{{PB}}.",
            f"PB = {int(h_bd)} / sin({ang_p}°) = {bp} m.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b41_3d_formula_derivation_single_variable(rng: random.Random) -> Dict[str, Any]:
    apex_letter = rng.choice(["D", "T"])
    svg = _svg_3d_tower_formula("d", f"{apex_letter} (Apex)")
    prompt = (
        f"Refer to the 3D diagram below. Vertical tower $C{apex_letter} = h$ has base $C$. Points $A$ and $B$ are in the horizontal plane such that $AB = d$.\n"
        f"The angles of elevation of ${apex_letter}$ from $A$ and $B$ are $\\alpha$ and $\\beta$ respectively. In $\\Delta ABC$, $\\angle CAB = \\alpha$ and $\\angle CBA = \\beta$.\n"
        r"Which expression correctly gives the height $h$ in terms of $d$, $\alpha$, and $\beta$?"
    )
    correct = r"h = \frac{d\sin\beta\tan\alpha}{\sin(\alpha + \beta)}"
    dist = [
        r"h = \frac{d\cos\beta\tan\alpha}{\sin(\alpha + \beta)}",
        r"h = \frac{d\sin\alpha\sin\beta}{\cos(\alpha + \beta)}",
        r"h = d\tan\alpha\tan\beta",
    ]
    sol = (
        r"1. In $\Delta ABC$, $\angle ACB = 180^\circ - (\alpha + \beta)$, so $\sin\angle ACB = \sin(\alpha + \beta)$." + "\n"
        r"2. By Sine Rule in $\Delta ABC$: $\frac{AC}{\sin\beta} = \frac{AB}{\sin(\alpha + \beta)} \implies AC = \frac{d\sin\beta}{\sin(\alpha + \beta)}$." + "\n"
        rf"3. In right-angled $\Delta AC{apex_letter}$: $\tan\alpha = \frac{{h}}{{AC}} \implies h = AC\tan\alpha = \frac{{d\sin\beta\tan\alpha}}{{\sin(\alpha + \beta)}}$."
    )
    return _mcq(
        rng,
        subskill="41_3d_formula_derivation_single_variable",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-41",
        concept_id="algebraic_3d_height_derivation",
        misconception_tags=["sine_rule_derivation_error"],
        hints=[
            r"Find \angle ACB in the horizontal plane: 180^\circ - (\alpha + \beta).",
            r"Use the Sine Rule to express AC in terms of d, \alpha, \beta.",
            r"Multiply by \tan\alpha to obtain h.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b42_3d_formula_cosine_rule_derivation(rng: random.Random) -> Dict[str, Any]:
    h_sym = rng.choice(["h", "H"])
    svg = _svg_3d_mast_cosine(r"\theta", h_sym)
    prompt = (
        f"Refer to the 3D diagram below. A vertical mast $AD = {h_sym}$ stands at point $A$ on horizontal ground. Points $B$ and $C$ lie on the ground such that $\\angle BAC = \\theta$.\n"
        f"The angles of elevation of $D$ from $B$ and $C$ are $\\beta$ and $\\alpha$ respectively.\n"
        r"Which equation correctly expresses the distance squared $BC^2$ across the ground?"
    )
    correct = rf"BC^2 = {h_sym}^2\left(\frac{{1}}{{\tan^2\beta}} + \frac{{1}}{{\tan^2\alpha}} - \frac{{2\cos\theta}}{{\tan\beta\tan\alpha}}\right)"
    dist = [
        rf"BC^2 = {h_sym}^2\left(\tan^2\beta + \tan^2\alpha - 2\tan\beta\tan\alpha\cos\theta\right)",
        rf"BC^2 = {h_sym}^2\left(\frac{{1}}{{\sin^2\beta}} + \frac{{1}}{{\sin^2\alpha}} - \frac{{2\cos\theta}}{{\sin\beta\sin\alpha}}\right)",
        rf"BC^2 = \frac{{{h_sym}^2}}{{\tan^2\theta}}",
    ]
    sol = (
        rf"1. In $\Delta ABD$, $AB = \frac{{{h_sym}}}{{\tan\beta}}$. In $\Delta ACD$, $AC = \frac{{{h_sym}}}{{\tan\alpha}}$." + "\n"
        r"2. In $\Delta ABC$, applying the Cosine Rule: $BC^2 = AB^2 + AC^2 - 2(AB)(AC)\cos\theta$." + "\n"
        rf"3. Factor out ${h_sym}^2$: $BC^2 = {h_sym}^2\left(\frac{{1}}{{\tan^2\beta}} + \frac{{1}}{{\tan^2\alpha}} - \frac{{2\cos\theta}}{{\tan\beta\tan\alpha}}\right)$."
    )
    return _mcq(
        rng,
        subskill="42_3d_formula_cosine_rule_derivation",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-42",
        concept_id="3d_cosine_rule_symbolic_proof",
        misconception_tags=["inverted_tangent_ratios"],
        hints=[
            rf"Express AB and AC in terms of {h_sym} and tangents.",
            r"Substitute into the Cosine Rule: BC^2 = AB^2 + AC^2 - 2 AB AC \cos\theta.",
            rf"Factorise {h_sym}^2 out of all terms.",
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


def _b43_compound_angle_in_right_triangle_geometry(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"In right-angled $\Delta ABC$ ($\angle C = 90^\circ$), point $D$ lies on $AC$ such that $\angle DBC = \beta$ and $\angle ABD = \alpha$." + "\n"
        r"If $BC = 4$, $CD = 3$, and $DA = 5$, what is the exact value of $\tan(\alpha + \beta)$?"
    )
    ans = "2"
    dist = ["1", r"\frac{3}{4}", r"\frac{5}{4}"]
    sol = (
        r"1. In $\Delta ABC$, $\angle B = \alpha + \beta$." + "\n"
        r"2. Total side $AC = CD + DA = 3 + 5 = 8$." + "\n"
        r"3. Since $\Delta ABC$ is right-angled at $C$:" + "\n"
        r"$$\tan(\alpha + \beta) = \frac{AC}{BC} = \frac{8}{4} = 2$$"
    )
    return _mcq(
        rng,
        subskill="43_compound_angle_in_right_triangle_geometry",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-43",
        concept_id="geometry_trig_compound_ratio",
        misconception_tags=["treated_alpha_as_angle_in_right_triangle"],
        hints=[
            r"Notice that \angle B of the whole right triangle ABC is \alpha + \beta.",
            r"The opposite side is AC = CD + DA.",
            r"\tan(\alpha + \beta) = \frac{AC}{BC} = \frac{8}{4} = 2.",
        ],
        worked_solution=sol,
    )


def _b44_trig_expression_simplification_without_calculator(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Simplify the following numerical expression without using a calculator:" + "\n"
        r"$$\frac{\sin 140^\circ \cos 20^\circ - \cos 140^\circ \sin 20^\circ}{\cos 40^\circ \cos 20^\circ - \sin 40^\circ \sin 20^\circ}$$"
    )
    ans = r"\sqrt{3}"
    dist = [r"\frac{\sqrt{3}}{2}", r"1", r"\frac{1}{\sqrt{3}}"]
    sol = (
        r"1. The numerator is a compound sine expansion:" + "\n"
        r"$$\sin 140^\circ \cos 20^\circ - \cos 140^\circ \sin 20^\circ = \sin(140^\circ - 20^\circ) = \sin 120^\circ = \sin 60^\circ = \frac{\sqrt{3}}{2}$$" + "\n"
        r"2. The denominator is a compound cosine expansion:" + "\n"
        r"$$\cos 40^\circ \cos 20^\circ - \sin 40^\circ \sin 20^\circ = \cos(40^\circ + 20^\circ) = \cos 60^\circ = \frac{1}{2}$$" + "\n"
        r"3. Dividing gives: $\frac{\sqrt{3}/2}{1/2} = \sqrt{3}$."
    )
    return _mcq(
        rng,
        subskill="44_trig_expression_simplification_without_calculator",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-44",
        concept_id="compound_angle_numerical_quotient",
        misconception_tags=["sign_error_in_denominator_expansion"],
        hints=[
            r"Numerator condenses to \sin(140^\circ - 20^\circ) = \sin 120^\circ.",
            r"Denominator condenses to \cos(40^\circ + 20^\circ) = \cos 60^\circ.",
            r"Evaluate \sin 120^\circ / \cos 60^\circ = \sqrt{3}.",
        ],
        worked_solution=sol,
    )


def _b45_trig_substitutions_given_cos_p(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"If $\cos 20^\circ = p$, express $\cos 40^\circ$ in terms of $p$."
    )
    ans = r"2p^2 - 1"
    dist = [r"p^2 - 1", r"1 - 2p^2", r"2p"]
    sol = (
        r"1. Notice that $40^\circ = 2(20^\circ)$." + "\n"
        r"2. Apply the double angle identity for cosine:" + "\n"
        r"$$\cos 40^\circ = \cos 2(20^\circ) = 2\cos^2 20^\circ - 1 = 2p^2 - 1$$"
    )
    return _mcq(
        rng,
        subskill="45_trig_substitutions_given_cos_p",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-45",
        concept_id="substitution_in_terms_of_p",
        misconception_tags=["linear_scaling_of_angles"],
        hints=[
            r"Write 40^\circ as 2 \times 20^\circ.",
            r"Use the identity \cos 2\theta = 2\cos^2\theta - 1.",
            r"Substitute \cos 20^\circ = p to get 2p^2 - 1.",
        ],
        worked_solution=sol,
    )


def _b46_trig_substitutions_given_sin_and_cos_m_n(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"If $\sin 10^\circ = m$ and $\cos 25^\circ = n$, express $\sin 35^\circ$ in terms of $m$ and $n$."
    )
    correct = r"m\sqrt{1-n^2} + n\sqrt{1-m^2}"
    dist = [
        r"mn + \sqrt{(1-m^2)(1-n^2)}",
        r"m + n",
        r"2mn",
    ]
    sol = (
        r"1. Write $35^\circ = 10^\circ + 25^\circ$." + "\n"
        r"2. $\sin 35^\circ = \sin(10^\circ + 25^\circ) = \sin 10^\circ\cos 25^\circ + \cos 10^\circ\sin 25^\circ$." + "\n"
        r"3. Since $\sin 10^\circ = m$, $\cos 10^\circ = \sqrt{1 - m^2}$." + "\n"
        r"4. Since $\cos 25^\circ = n$, $\sin 25^\circ = \sqrt{1 - n^2}$." + "\n"
        r"5. Substitute: $\sin 35^\circ = m\cdot n + \sqrt{1-m^2}\sqrt{1-n^2}$, but wait:" + "\n"
        r"$$\sin 10^\circ\cos 25^\circ + \cos 10^\circ\sin 25^\circ = mn + \sqrt{1-m^2}\sqrt{1-n^2}$$"
    )
    # Correct formula: sin 10 cos 25 + cos 10 sin 25 = m * n + sqrt(1 - m^2)*sqrt(1 - n^2)
    correct_expr = r"mn + \sqrt{1-m^2}\sqrt{1-n^2}"
    dist_fixed = [
        r"m\sqrt{1-n^2} + n\sqrt{1-m^2}",
        r"m + n",
        r"2mn",
    ]
    return _mcq(
        rng,
        subskill="46_trig_substitutions_given_sin_and_cos_m_n",
        prompt=prompt,
        correct=correct_expr,
        distractors=dist_fixed,
        learning_objective_id="G12-MATH-TRIG-46",
        concept_id="compound_angle_substitution_variables",
        misconception_tags=["assumed_sin_a_plus_b_is_sin_a_plus_sin_b"],
        hints=[
            r"Express 35^\circ as 10^\circ + 25^\circ.",
            r"Expand using \sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta.",
            r"Use Pythagoras to find \cos 10^\circ = \sqrt{1-m^2} and \sin 25^\circ = \sqrt{1-n^2}.",
        ],
        worked_solution=sol,
    )


def _b47_trig_quadratic_identity_factorisation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Simplify the expression to a single term:" + "\n"
        r"$$\frac{(\sin x + \cos x)^2 - 1}{\sin 2x}$$"
    )
    ans = "1"
    dist = ["2", r"\tan x", r"\sin x\cos x"]
    sol = (
        r"1. Expand $(\sin x + \cos x)^2$:" + "\n"
        r"$$(\sin x + \cos x)^2 = \sin^2 x + 2\sin x\cos x + \cos^2 x = (\sin^2 x + \cos^2 x) + \sin 2x = 1 + \sin 2x$$" + "\n"
        r"2. Subtract 1: $$(1 + \sin 2x) - 1 = \sin 2x$$" + "\n"
        r"3. Divide by the denominator: $$\frac{\sin 2x}{\sin 2x} = 1$$"
    )
    return _mcq(
        rng,
        subskill="47_trig_quadratic_identity_factorisation",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-47",
        concept_id="binomial_expansion_trig_identity",
        misconception_tags=["forgot_cross_term_in_binomial_square"],
        hints=[
            r"Expand (\sin x + \cos x)^2 into \sin^2 x + 2\sin x\cos x + \cos^2 x.",
            r"Use \sin^2 x + \cos^2 x = 1 and 2\sin x\cos x = \sin 2x.",
            r"The numerator simplifies to \sin 2x, yielding 1.",
        ],
        worked_solution=sol,
    )


def _b48_3d_crane_or_truss_application(rng: random.Random) -> Dict[str, Any]:
    pq = 4.0
    pr = 10.0
    ang_pqr = 120
    # In triangle PQR: sin R / 4 = sin 120 / 10 => sin R = 4 * sin 120 / 10 = 0.4 * sqrt(3)/2 = 0.3464
    sin_r = pq * math.sin(math.radians(ang_pqr)) / pr
    ang_r = math.degrees(math.asin(sin_r))
    ang_qpr = round(180 - ang_pqr - ang_r, 1)
    ang_qpr_str = f"{ang_qpr}".replace(".", "{,}")

    prompt = (
        f"A construction crane is modeled by $\\Delta PQR$ where $PQ = {int(pq)}\\text{{ m}}$, "
        f"$PR = {int(pr)}\\text{{ m}}$, and $\\angle PQR = {ang_pqr}^\\circ$.\n"
        f"Calculate the size of angle $\\angle QPR$, correct to 1 decimal place."
    )
    ans = rf"{ang_qpr}^\circ"
    accepted = [f"{ang_qpr}", ang_qpr_str, ans, rf"{ang_qpr_str}^\circ"]
    sol = (
        f"1. Apply the Sine Rule to find angle $R$:\n"
        f"$$\\frac{{\\sin R}}{{PQ}} = \\frac{{\\sin {ang_pqr}^\\circ}}{{PR}} \\implies \\sin R = \\frac{{{int(pq)} \\times \\sin 120^\\circ}}{{{int(pr)}}} \\approx {round(sin_r, 4)}$$\n"
        f"$$R = \\arcsin({round(sin_r, 4)}) \\approx {round(ang_r, 1)}^\\circ$$\n"
        f"2. Sum of angles in $\\Delta PQR$ is $180^\\circ$:\n"
        f"$$\\angle QPR = 180^\\circ - {ang_pqr}^\\circ - {round(ang_r, 1)}^\\circ \\approx {ang_qpr_str}^\\circ$$"
    )
    return _typed(
        subskill="48_3d_crane_or_truss_engineering_application",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-48",
        concept_id="crane_geometry_sine_rule",
        misconception_tags=["stopped_after_finding_angle_R"],
        hints=[
            r"Find angle R first using the Sine Rule: \frac{\sin R}{PQ} = \frac{\sin 120^\circ}{PR}.",
            r"Subtract angle R and 120° from 180° to find angle QPR.",
            f"Angle QPR is {ang_qpr}°.",
        ],
        worked_solution=sol,
    )


def _b49_complex_general_solution_quadratic_in_cos(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Solve for $x$ in the general solution:" + "\n"
        r"$$2\cos^2 x - 5\cos x + 2 = 0$$"
    )
    correct = r"x = \pm 60^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}"
    dist = [
        r"x = \pm 60^\circ + k \cdot 360^\circ \quad \text{or} \quad x = k \cdot 360^\circ, \quad k \in \mathbb{Z}",
        r"x = 30^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}",
        r"x = \pm 45^\circ + k \cdot 180^\circ, \quad k \in \mathbb{Z}",
    ]
    sol = (
        r"1. Factorise the quadratic in $\cos x$:" + "\n"
        r"$$(2\cos x - 1)(\cos x - 2) = 0$$" + "\n"
        r"2. Factor 1: $\cos x = 2$ has no real solution since $-1 \le \cos x \le 1$." + "\n"
        r"3. Factor 2: $\cos x = \frac{1}{2} \implies x = \pm 60^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}$."
    )
    return _mcq(
        rng,
        subskill="49_complex_general_solution_quadratic_in_cos",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-49",
        concept_id="quadratic_trig_extraneous_roots",
        misconception_tags=["attempted_to_solve_cos_x_equals_2"],
        hints=[
            r"Factorise the quadratic: (2\cos x - 1)(\cos x - 2) = 0.",
            r"Reject \cos x = 2 because cosine cannot exceed 1.",
            r"Solve \cos x = 1/2: x = \pm 60^\circ + k\cdot 360^\circ.",
        ],
        worked_solution=sol,
    )


def _b50_integrated_grade12_trigonometry_synthesis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Given the expression $f(x) = \frac{\sin 2x}{1 - \cos 2x}$:" + "\n"
        r"1. Simplify $f(x)$ to a single trigonometric ratio." + "\n"
        r"2. Hence, determine the general solution of $f(x) = \sqrt{3}$."
    )
    correct = r"f(x) = \frac{1}{\tan x}; \quad x = 30^\circ + k \cdot 180^\circ, \quad k \in \mathbb{Z}"
    dist = [
        r"f(x) = \tan x; \quad x = 60^\circ + k \cdot 180^\circ, \quad k \in \mathbb{Z}",
        r"f(x) = \sin x; \quad x = 30^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}",
        r"f(x) = \cos x; \quad x = \pm 30^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}",
    ]
    sol = (
        r"1. Simplify using double-angle identities:" + "\n"
        r"$$\frac{\sin 2x}{1 - \cos 2x} = \frac{2\sin x\cos x}{1 - (1 - 2\sin^2 x)} = \frac{2\sin x\cos x}{2\sin^2 x} = \frac{\cos x}{\sin x} = \frac{1}{\tan x}$$\n"
        r"2. Solve $\frac{1}{\tan x} = \sqrt{3} \implies \tan x = \frac{1}{\sqrt{3}}$." + "\n"
        r"3. General solution: $x = 30^\circ + k \cdot 180^\circ, \quad k \in \mathbb{Z}$."
    )
    return _mcq(
        rng,
        subskill="50_integrated_grade12_trigonometry_synthesis",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-50",
        concept_id="trigonometry_synthesis_simplification_and_equation",
        misconception_tags=["inverted_cotangent_ratio"],
        hints=[
            r"Use \cos 2x = 1 - 2\sin^2 x to simplify the denominator to 2\sin^2 x.",
            r"The fraction reduces to \frac{\cos x}{\sin x} = \frac{1}{\tan x}.",
            r"Set \tan x = \frac{1}{\sqrt{3}} and solve for x.",
        ],
        worked_solution=sol,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_sine_rule_solve_side_2d": _b26_sine_rule_solve_side_2d,
    "27_sine_rule_solve_angle_2d": _b27_sine_rule_solve_angle_2d,
    "28_sine_rule_ambiguous_case": _b28_sine_rule_ambiguous_case,
    "29_cosine_rule_solve_side_2d": _b29_cosine_rule_solve_side_2d,
    "30_cosine_rule_solve_angle_2d": _b30_cosine_rule_solve_angle_2d,
    "31_area_rule_triangle_calculation": _b31_area_rule_triangle_calculation,
    "32_area_rule_quadrilateral_decomposition": _b32_area_rule_quadrilateral_decomposition,
    "33_angle_elevation_single_triangle": _b33_angle_elevation_single_triangle,
    "34_angle_elevation_depression_two_buildings": _b34_angle_elevation_depression_two_buildings,
    "35_angle_elevation_surveyor_theodolite": _b35_angle_elevation_surveyor_theodolite,
    "36_2d_trig_bearings_and_navigation": _b36_2d_trig_bearings_and_navigation,
    "37_3d_vertical_tower_horizontal_ground_distance": _b37_3d_vertical_tower_horizontal_ground,
    "38_3d_pyramid_apex_edge_calculation": _b38_3d_pyramid_apex_edge_calculation,
    "39_3d_triangular_prism_measurements": _b39_3d_triangular_prism_measurements,
    "40_3d_two_vertical_poles_distance_between_tops": _b40_3d_two_vertical_poles_distance,
    "41_3d_formula_derivation_single_variable": _b41_3d_formula_derivation_single_variable,
    "42_3d_formula_cosine_rule_derivation": _b42_3d_formula_cosine_rule_derivation,
    "43_compound_angle_in_right_triangle_geometry": _b43_compound_angle_in_right_triangle_geometry,
    "44_trig_expression_simplification_without_calculator": _b44_trig_expression_simplification_without_calculator,
    "45_trig_substitutions_given_cos_p": _b45_trig_substitutions_given_cos_p,
    "46_trig_substitutions_given_sin_and_cos_m_n": _b46_trig_substitutions_given_sin_and_cos_m_n,
    "47_trig_quadratic_identity_factorisation": _b47_trig_quadratic_identity_factorisation,
    "48_3d_crane_or_truss_engineering_application": _b48_3d_crane_or_truss_application,
    "49_complex_general_solution_quadratic_in_cos": _b49_complex_general_solution_quadratic_in_cos,
    "50_integrated_grade12_trigonometry_synthesis": _b50_integrated_grade12_trigonometry_synthesis,
}
