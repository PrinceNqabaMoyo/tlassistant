"""Grade 12 Technical Mathematics — Complex Numbers: Archetypes 26–38
===================================================================
100% Aligned with South African National Curriculum Standards (CAPS Technical Mathematics Grade 12).
Grounded strictly in curriculum_docs_auto/TechnicalMathematics_Gr12/Term 1/01. Complex numbers.md.

Covers subskills 26–38:
- 26_polar_multiplication_moduli_and_arguments
- 27_polar_multiplication_angle_reduction
- 28_polar_division_moduli_and_arguments
- 29_polar_division_negative_angle_adjustment
- 30_polar_combined_multiplication_and_division
- 31_de_moivre_theorem_small_positive_power
- 32_de_moivre_theorem_higher_power_with_angle_reduction
- 33_de_moivre_theorem_convert_to_rectangular
- 34_de_moivre_theorem_negative_integer_power
- 35_complex_square_roots_polar_form
- 36_complex_cube_roots_polar_form
- 37_argand_roots_regular_polygon_geometry
- 38_rectangular_to_polar_then_de_moivre
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Tuple


def _fmt_sa(val: float | int, places: int = 1) -> str:
    """Format numeric values with South African decimal comma."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_argand_svg(
    vectors: List[Tuple[float, float, str, str]],  # (r, theta_deg, label, stroke_color)
    polygon_points: List[Tuple[float, float]] | None = None,
    circle_radius: float | None = None,
    seed: int = 42,
    max_r: float = 10.0,
) -> str:
    """Generate dynamic seed-varied inline SVG for Argand plane representations."""
    width, height = 400, 400
    cx, cy = 200, 200
    scale = 160.0 / max(max_r, 1.0)

    elements: List[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" data-seed="{seed}" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px;">',
        '<defs>',
        '  <marker id="arrow-blue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2563eb"/></marker>',
        '  <marker id="arrow-red" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#dc2626"/></marker>',
        '  <marker id="arrow-green" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#16a34a"/></marker>',
        '  <marker id="arrow-purple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#9333ea"/></marker>',
        '</defs>',
    ]

    # Grid lines
    for step in [-120, -60, 60, 120]:
        elements.append(f'<line x1="{cx + step}" y1="20" x2="{cx + step}" y2="380" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3"/>')
        elements.append(f'<line x1="20" y1="{cy + step}" x2="380" y2="{cy + step}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3"/>')

    # Axes
    elements.append(f'<line x1="20" y1="{cy}" x2="380" y2="{cy}" stroke="#475569" stroke-width="2"/>')
    elements.append(f'<line x1="{cx}" y1="380" x2="{cx}" y2="20" stroke="#475569" stroke-width="2"/>')

    # Axis Labels
    elements.append(f'<text x="375" y="{cy - 8}" font-size="12" font-family="sans-serif" font-weight="bold" fill="#334155" text-anchor="end">Re</text>')
    elements.append(f'<text x="{cx + 8}" y="32" font-size="12" font-family="sans-serif" font-weight="bold" fill="#334155">Im</text>')
    elements.append(f'<text x="{cx - 12}" y="{cy + 16}" font-size="11" font-family="sans-serif" fill="#64748b">O</text>')

    # Circle (if requested)
    if circle_radius is not None and circle_radius > 0:
        cr_px = circle_radius * scale
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="{cr_px:.1f}" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>')

    # Inscribed polygon (for roots)
    if polygon_points and len(polygon_points) > 2:
        pts_str = " ".join([f"{cx + x * scale:.1f},{cy - y * scale:.1f}" for x, y in polygon_points])
        elements.append(f'<polygon points="{pts_str}" fill="rgba(147, 51, 234, 0.08)" stroke="#9333ea" stroke-width="1.5" stroke-dasharray="2,2"/>')

    # Vectors
    marker_map = {
        "#2563eb": "arrow-blue",
        "#dc2626": "arrow-red",
        "#16a34a": "arrow-green",
        "#9333ea": "arrow-purple",
    }
    for r, deg, label, color in vectors:
        rad = math.radians(deg)
        vx = r * math.cos(rad)
        vy = r * math.sin(rad)
        x_px = cx + vx * scale
        y_px = cy - vy * scale
        mid_x = cx + (vx * 0.55) * scale
        mid_y = cy - (vy * 0.55) * scale
        marker_id = marker_map.get(color, "arrow-blue")

        # Vector line
        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x_px:.1f}" y2="{y_px:.1f}" stroke="{color}" stroke-width="2.5" marker-end="url(#{marker_id})"/>')

        # Angle arc (small)
        arc_r = min(35.0, r * scale * 0.4)
        if deg > 0 and arc_r > 8:
            large_arc = 1 if deg > 180 else 0
            end_arc_x = cx + arc_r * math.cos(rad)
            end_arc_y = cy - arc_r * math.sin(rad)
            elements.append(f'<path d="M {cx + arc_r} {cy} A {arc_r} {arc_r} 0 {large_arc} 0 {end_arc_x:.1f} {end_arc_y:.1f}" fill="none" stroke="{color}" stroke-width="1" stroke-dasharray="2,1"/>')

        # Label offset
        offset_x = 12 * math.cos(rad)
        offset_y = -12 * math.sin(rad)
        elements.append(f'<circle cx="{x_px:.1f}" cy="{y_px:.1f}" r="3.5" fill="{color}"/>')
        elements.append(f'<text x="{x_px + offset_x:.1f}" y="{y_px + offset_y:.1f}" font-size="11" font-family="sans-serif" font-weight="600" fill="{color}" text-anchor="middle">{label}</text>')

    elements.append('</svg>')
    return "".join(elements)


# --------------------------------------------------------------------------- #
# Subskill 26: Polar Multiplication Direct
# --------------------------------------------------------------------------- #
def build_26_polar_multiplication_moduli_and_arguments(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.choice([2, 3, 4, 5])
    r2 = rng.choice([2, 3, 4, 5])
    theta1 = rng.choice([20, 25, 30, 35, 40, 45, 50, 60])
    theta2 = rng.choice([15, 20, 30, 40, 45, 50, 60, 70])

    r_prod = r1 * r2
    theta_prod = theta1 + theta2

    prompt = (
        f"Two complex numbers are given in polar form:\n"
        f"$$z_1 = {r1}\\operatorname{{cis}}({theta1}^\\circ) \\quad \\text{{and}} \\quad z_2 = {r2}\\operatorname{{cis}}({theta2}^\\circ)$$\n\n"
        f"The vectors representing $z_1$, $z_2$, and their product are plotted on the Argand plane shown.\n\n"
        f"Calculate the product $z_1 \\cdot z_2$ in polar form $r\\operatorname{{cis}}\\theta$, "
        f"where $r > 0$ and $0^\\circ \\le \\theta < 360^\\circ$."
    )

    ans_latex = rf"z_1 \cdot z_2 = {r_prod}\operatorname{{cis}}({theta_prod}^\circ)"
    worked_solution = (
        f"1. State the polar multiplication theorem: $z_1 \\cdot z_2 = r_1 r_2 \\operatorname{{cis}}(\\theta_1 + \\theta_2)$.\n"
        f"2. Multiply moduli: $r = {r1} \\times {r2} = {r_prod}$.\n"
        f"3. Add arguments: $\\theta = {theta1}^\\circ + {theta2}^\\circ = {theta_prod}^\\circ$.\n"
        f"4. Result: $z_1 \\cdot z_2 = {r_prod}\\operatorname{{cis}}({theta_prod}^\\circ)$."
    )

    vectors = [
        (float(r1), float(theta1), f"z1({r1},{theta1}deg)", "#2563eb"),
        (float(r2), float(theta2), f"z2({r2},{theta2}deg)", "#dc2626"),
        (float(r_prod), float(theta_prod), f"z1.z2({r_prod},{theta_prod}deg)", "#16a34a"),
    ]
    svg = _make_argand_svg(vectors, max_r=float(r_prod) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "26_polar_multiplication_moduli_and_arguments",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_polar_multiplication",
        "difficulty": "easy",
        "marks": 3,
        "misconception_tags": ["multiplied_arguments_instead_of_adding", "added_moduli_instead_of_multiplying"],
        "hints": {
            "tier_1": "In polar form, multiply the moduli ($r = r_1 \\times r_2$) and add the arguments ($\\theta = \\theta_1 + \\theta_2$).",
            "tier_2": f"Modulus: $r = {r1} \\times {r2} = {r_prod}$. Argument: $\\theta = {theta1}^\\circ + {theta2}^\\circ$.",
            "tier_3": f"Final answer: ${r_prod}\\operatorname{{cis}}({theta_prod}^\\circ)$.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Multiplication of moduli: {r1} * {r2} = {r_prod}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Addition of arguments: {theta1} + {theta2} = {theta_prod}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct polar statement: {r_prod} cis({theta_prod} deg)", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 27: Polar Multiplication with Angle Reduction (>= 360)
# --------------------------------------------------------------------------- #
def build_27_polar_multiplication_angle_reduction(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.choice([2, 3, 4, 6])
    r2 = rng.choice([2, 3, 5])
    theta1 = rng.choice([200, 210, 225, 240, 250])
    theta2 = rng.choice([160, 180, 190, 200, 210])

    r_prod = r1 * r2
    raw_theta = theta1 + theta2
    reduced_theta = raw_theta - 360

    prompt = (
        f"Given two complex numbers in polar form:\n"
        f"$$z_1 = {r1}\\operatorname{{cis}}({theta1}^\\circ) \\quad \\text{{and}} \\quad z_2 = {r2}\\operatorname{{cis}}({theta2}^\\circ)$$\n\n"
        f"The vectors are depicted on the Argand diagram shown.\n\n"
        f"Determine the product $z_1 \\cdot z_2$ in standard polar form $r\\operatorname{{cis}}\\theta$, "
        f"ensuring that the argument satisfies $0^\\circ \\le \\theta < 360^\\circ$."
    )

    ans_latex = rf"z_1 \cdot z_2 = {r_prod}\operatorname{{cis}}({reduced_theta}^\circ)"
    worked_solution = (
        f"1. Multiply moduli: $r = {r1} \\times {r2} = {r_prod}$.\n"
        f"2. Add arguments: $\\theta_{{\\text{{raw}}}} = {theta1}^\\circ + {theta2}^\\circ = {raw_theta}^\\circ$.\n"
        f"3. Since ${raw_theta}^\\circ \\ge 360^\\circ$, subtract $360^\\circ$ to find the coterminal argument:\n"
        f"   $\\theta = {raw_theta}^\\circ - 360^\\circ = {reduced_theta}^\\circ$.\n"
        f"4. Result: $z_1 \\cdot z_2 = {r_prod}\\operatorname{{cis}}({reduced_theta}^\\circ)$."
    )

    vectors = [
        (float(r1), float(theta1), f"z1({r1},{theta1}deg)", "#2563eb"),
        (float(r2), float(theta2), f"z2({r2},{theta2}deg)", "#dc2626"),
        (float(r_prod), float(reduced_theta), f"prod({r_prod},{reduced_theta}deg)", "#16a34a"),
    ]
    svg = _make_argand_svg(vectors, max_r=float(r_prod) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "27_polar_multiplication_angle_reduction",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_polar_angle_reduction",
        "difficulty": "medium",
        "marks": 4,
        "misconception_tags": ["forgot_angle_reduction_mod_360", "multiplied_arguments_instead_of_adding"],
        "hints": {
            "tier_1": "Multiply the moduli and add the arguments. If the sum is $360^\\circ$ or more, subtract $360^\\circ$.",
            "tier_2": f"Raw argument: ${theta1}^\\circ + {theta2}^\\circ = {raw_theta}^\\circ$. Reduced: ${raw_theta}^\\circ - 360^\\circ = {reduced_theta}^\\circ$.",
            "tier_3": f"Final answer: ${r_prod}\\operatorname{{cis}}({reduced_theta}^\\circ)$.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Modulus product r = {r_prod}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Argument addition theta_raw = {raw_theta} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle reduction to [0, 360): {reduced_theta} deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final polar expression: {r_prod} cis({reduced_theta} deg)", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 28: Polar Division Direct
# --------------------------------------------------------------------------- #
def build_28_polar_division_moduli_and_arguments(rng: random.Random) -> Dict[str, Any]:
    r2 = rng.choice([2, 3, 4])
    mult = rng.choice([2, 3, 4, 5])
    r1 = r2 * mult

    theta2 = rng.choice([15, 25, 30, 45, 50])
    diff = rng.choice([30, 45, 60, 75, 90, 120])
    theta1 = theta2 + diff

    r_quot = mult
    theta_quot = diff

    prompt = (
        f"Two complex numbers in polar form are represented on the Argand plane shown:\n"
        f"$$z_1 = {r1}\\operatorname{{cis}}({theta1}^\\circ) \\quad \\text{{and}} \\quad z_2 = {r2}\\operatorname{{cis}}({theta2}^\\circ)$$\n\n"
        f"Calculate the quotient $\\frac{{z_1}}{{z_2}}$ in polar form $r\\operatorname{{cis}}\\theta$, "
        f"where $0^\\circ \\le \\theta < 360^\\circ$."
    )

    ans_latex = rf"\frac{{z_1}}{{z_2}} = {r_quot}\operatorname{{cis}}({theta_quot}^\circ)"
    worked_solution = (
        f"1. Apply polar division formula: $\\frac{{z_1}}{{z_2}} = \\frac{{r_1}}{{r_2}}\\operatorname{{cis}}(\\theta_1 - \\theta_2)$.\n"
        f"2. Divide moduli: $r = \\frac{{{r1}}}{{{r2}}} = {r_quot}$.\n"
        f"3. Subtract arguments: $\\theta = {theta1}^\\circ - {theta2}^\\circ = {theta_quot}^\\circ$.\n"
        f"4. Result: $\\frac{{z_1}}{{z_2}} = {r_quot}\\operatorname{{cis}}({theta_quot}^\\circ)$."
    )

    vectors = [
        (float(r1), float(theta1), f"z1({r1},{theta1}deg)", "#2563eb"),
        (float(r2), float(theta2), f"z2({r2},{theta2}deg)", "#dc2626"),
        (float(r_quot), float(theta_quot), f"quot({r_quot},{theta_quot}deg)", "#16a34a"),
    ]
    svg = _make_argand_svg(vectors, max_r=float(r1) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "28_polar_division_moduli_and_arguments",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_polar_division",
        "difficulty": "easy",
        "marks": 3,
        "misconception_tags": ["divided_arguments_instead_of_subtracting", "subtracted_moduli_instead_of_dividing"],
        "hints": {
            "tier_1": "Divide the moduli ($r = r_1 / r_2$) and subtract the arguments ($\\theta = \\theta_1 - \\theta_2$).",
            "tier_2": f"Modulus: ${r1} / {r2} = {r_quot}$. Argument: ${theta1}^\\circ - {theta2}^\\circ = {theta_quot}^\\circ$.",
            "tier_3": f"Final answer: ${r_quot}\\operatorname{{cis}}({theta_quot}^\\circ)$.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Modulus quotient: {r1} / {r2} = {r_quot}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Argument subtraction: {theta1} - {theta2} = {theta_quot}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Polar result: {r_quot} cis({theta_quot} deg)", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 29: Polar Division Negative Angle Adjustment
# --------------------------------------------------------------------------- #
def build_29_polar_division_negative_angle_adjustment(rng: random.Random) -> Dict[str, Any]:
    r2 = rng.choice([2, 3, 4])
    mult = rng.choice([2, 3, 4])
    r1 = r2 * mult

    theta1 = rng.choice([30, 45, 60, 75])
    diff = rng.choice([90, 120, 135, 150, 180])
    theta2 = theta1 + diff  # theta1 < theta2

    r_quot = mult
    raw_diff = theta1 - theta2  # negative
    pos_angle = 360 + raw_diff

    prompt = (
        f"Consider the complex numbers $z_1$ and $z_2$ shown on the Argand diagram:\n"
        f"$$z_1 = {r1}\\operatorname{{cis}}({theta1}^\\circ) \\quad \\text{{and}} \\quad z_2 = {r2}\\operatorname{{cis}}({theta2}^\\circ)$$\n\n"
        f"Calculate $\\frac{{z_1}}{{z_2}}$ in standard polar form $r\\operatorname{{cis}}\\theta$, "
        f"where $0^\\circ \\le \\theta < 360^\\circ$."
    )

    ans_latex = rf"\frac{{z_1}}{{z_2}} = {r_quot}\operatorname{{cis}}({pos_angle}^\circ)"
    worked_solution = (
        f"1. Divide moduli: $r = \\frac{{{r1}}}{{{r2}}} = {r_quot}$.\n"
        f"2. Subtract arguments: $\\theta_{{\\text{{raw}}}} = {theta1}^\\circ - {theta2}^\\circ = {raw_diff}^\\circ$.\n"
        f"3. Since ${raw_diff}^\\circ < 0^\\circ$, add $360^\\circ$ to express as a standard positive argument:\n"
        f"   $\\theta = 360^\\circ + ({raw_diff}^\\circ) = {pos_angle}^\\circ$.\n"
        f"4. Result: $\\frac{{z_1}}{{z_2}} = {r_quot}\\operatorname{{cis}}({pos_angle}^\\circ)$."
    )

    vectors = [
        (float(r1), float(theta1), f"z1({r1},{theta1}deg)", "#2563eb"),
        (float(r2), float(theta2), f"z2({r2},{theta2}deg)", "#dc2626"),
        (float(r_quot), float(pos_angle), f"quot({r_quot},{pos_angle}deg)", "#16a34a"),
    ]
    svg = _make_argand_svg(vectors, max_r=float(r1) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "29_polar_division_negative_angle_adjustment",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_polar_negative_angle",
        "difficulty": "medium",
        "marks": 4,
        "misconception_tags": ["left_negative_argument_unconverted", "subtracted_angles_in_wrong_order"],
        "hints": {
            "tier_1": "Divide moduli and subtract arguments. If the resulting angle is negative, add $360^\\circ$.",
            "tier_2": f"Raw argument: ${theta1}^\\circ - {theta2}^\\circ = {raw_diff}^\\circ$. Positive argument: $360^\\circ + ({raw_diff}^\\circ) = {pos_angle}^\\circ$.",
            "tier_3": f"Final answer: ${r_quot}\\operatorname{{cis}}({pos_angle}^\\circ)$.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Quotient modulus: {r1} / {r2} = {r_quot}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Argument subtraction: {theta1} - {theta2} = {raw_diff} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Conversion to positive coterminal angle: {pos_angle} deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final polar answer: {r_quot} cis({pos_angle} deg)", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 30: Combined Polar Multiplication and Division
# --------------------------------------------------------------------------- #
def build_30_polar_combined_multiplication_and_division(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.choice([2, 3, 4, 6])
    r2 = rng.choice([3, 4, 6, 8])
    r3 = rng.choice([2, 3, 4])
    # Ensure (r1 * r2) is divisible by r3
    r1 = r3 * rng.choice([2, 3])

    theta1 = rng.choice([35, 45, 60, 75])
    theta2 = rng.choice([55, 65, 80, 90])
    theta3 = rng.choice([20, 30, 40, 50])

    r_res = (r1 * r2) // r3
    theta_res = (theta1 + theta2 - theta3) % 360

    prompt = (
        f"Evaluate the complex expression in polar form:\n"
        f"$$W = \\frac{{{r1}\\operatorname{{cis}}({theta1}^\\circ) \\times {r2}\\operatorname{{cis}}({theta2}^\\circ)}}{{{r3}\\operatorname{{cis}}({theta3}^\\circ)}}$$\n\n"
        f"The components and result vector are visualised on the Argand plane shown.\n\n"
        f"Express $W$ in standard polar form $r\\operatorname{{cis}}\\theta$, with $r > 0$ and $0^\\circ \\le \\theta < 360^\\circ$."
    )

    ans_latex = rf"W = {r_res}\operatorname{{cis}}({theta_res}^\circ)"
    worked_solution = (
        f"1. Apply polar operations theorem:\n"
        f"   Modulus: $r = \\frac{{r_1 \\times r_2}}{{r_3}} = \\frac{{{r1} \\times {r2}}}{{{r3}}} = {r_res}$.\n"
        f"2. Argument: $\\theta = \\theta_1 + \\theta_2 - \\theta_3 = {theta1}^\\circ + {theta2}^\\circ - {theta3}^\\circ = {theta_res}^\\circ$.\n"
        f"3. Result: $W = {r_res}\\operatorname{{cis}}({theta_res}^\\circ)$."
    )

    vectors = [
        (float(r1), float(theta1), f"z1({r1})", "#2563eb"),
        (float(r2), float(theta2), f"z2({r2})", "#dc2626"),
        (float(r3), float(theta3), f"z3({r3})", "#9333ea"),
        (float(r_res), float(theta_res), f"W({r_res},{theta_res}deg)", "#16a34a"),
    ]
    svg = _make_argand_svg(vectors, max_r=float(max(r1, r2, r_res)) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "30_polar_combined_multiplication_and_division",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "elementary_combined_polar_ops",
        "difficulty": "medium",
        "marks": 5,
        "misconception_tags": ["multiplied_divisor_argument_instead_of_subtracting", "arithmetic_error_in_modulus_chain"],
        "hints": {
            "tier_1": "Multiply the numerator moduli and divide by the denominator modulus. For arguments: add the numerator angles and subtract the denominator angle.",
            "tier_2": f"Modulus: $({r1} \\times {r2}) / {r3} = {r_res}$. Argument: ${theta1}^\\circ + {theta2}^\\circ - {theta3}^\\circ = {theta_res}^\\circ$.",
            "tier_3": f"Final answer: ${r_res}\\operatorname{{cis}}({theta_res}^\\circ)$.",
        },
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Numerator product modulus: {r1 * r2}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Overall modulus r = {r_res}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Numerator angle addition: {theta1 + theta2} deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Denominator angle subtraction: {theta_res} deg", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Complete polar expression: {r_res} cis({theta_res} deg)", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 31: de Moivre's Theorem for Small Positive Integer Powers
# --------------------------------------------------------------------------- #
def build_31_de_moivre_theorem_small_positive_power(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([2, 3])
    theta = rng.choice([20, 25, 30, 35, 40, 45])
    n = rng.choice([2, 3])

    r_pow = r**n
    theta_pow = theta * n

    prompt = (
        f"A complex number $z = {r}\\operatorname{{cis}}({theta}^\\circ)$ is represented by a vector on the Argand diagram shown.\n\n"
        f"Apply de Moivre's Theorem to evaluate $z^{{{n}}}$ in polar form $r\\operatorname{{cis}}\\theta$, "
        f"where $0^\\circ \\le \\theta < 360^\\circ$."
    )

    ans_latex = rf"z^{{{n}}} = {r_pow}\operatorname{{cis}}({theta_pow}^\circ)"
    worked_solution = (
        f"1. State de Moivre's Theorem: $[r\\operatorname{{cis}}\\theta]^n = r^n \\operatorname{{cis}}(n\\theta)$.\n"
        f"2. Calculate the modulus: $r^{{{n}}} = {r}^{{{n}}} = {r_pow}$.\n"
        f"3. Calculate the argument: $\\theta = {n} \\times {theta}^\\circ = {theta_pow}^\\circ$.\n"
        f"4. Result: $z^{{{n}}} = {r_pow}\\operatorname{{cis}}({theta_pow}^\\circ)$."
    )

    vectors = [
        (float(r), float(theta), f"z({r},{theta}deg)", "#2563eb"),
        (float(r_pow), float(theta_pow), f"z^{n}({r_pow},{theta_pow}deg)", "#16a34a"),
    ]
    svg = _make_argand_svg(vectors, max_r=float(r_pow) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "31_de_moivre_theorem_small_positive_power",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 3,
        "mode": "elementary_de_moivre_powers",
        "difficulty": "easy",
        "marks": 3,
        "misconception_tags": ["multiplied_modulus_by_n_instead_of_power", "raised_argument_to_power_instead_of_multiplying"],
        "hints": {
            "tier_1": "By de Moivre's Theorem, raise the modulus to power $n$ ($r^n$) and multiply the argument by $n$ ($n\\theta$).",
            "tier_2": f"Modulus: ${r}^{{{n}}} = {r_pow}$. Argument: ${n} \\times {theta}^\\circ = {theta_pow}^\\circ$.",
            "tier_3": f"Final answer: ${r_pow}\\operatorname{{cis}}({theta_pow}^\\circ)$.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Modulus calculation {r}^{n} = {r_pow}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Argument multiplication {n} * {theta} = {theta_pow} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Final expression {r_pow} cis({theta_pow} deg)", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 32: de Moivre's Theorem with Higher Powers and Angle Reduction
# --------------------------------------------------------------------------- #
def build_32_de_moivre_theorem_higher_power_with_angle_reduction(rng: random.Random) -> Dict[str, Any]:
    r = 2
    n = rng.choice([4, 5, 6])
    theta = rng.choice([70, 75, 80, 85, 95, 100])

    r_pow = r**n
    raw_theta = theta * n
    reduced_theta = raw_theta % 360

    prompt = (
        f"Given the complex number $z = {r}\\operatorname{{cis}}({theta}^\\circ)$ plotted on the Argand plane shown.\n\n"
        f"Use de Moivre's Theorem to calculate $z^{{{n}}}$ in polar form $r\\operatorname{{cis}}\\theta$, "
        f"where $r > 0$ and $0^\\circ \\le \\theta < 360^\\circ$."
    )

    ans_latex = rf"z^{{{n}}} = {r_pow}\operatorname{{cis}}({reduced_theta}^\circ)"
    worked_solution = (
        f"1. Apply de Moivre's Theorem: $z^{{{n}}} = {r}^{{{n}}}\\operatorname{{cis}}({n} \\times {theta}^\\circ)$.\n"
        f"2. Modulus: $r = {r}^{{{n}}} = {r_pow}$.\n"
        f"3. Raw argument: $\\theta_{{\\text{{raw}}}} = {n} \\times {theta}^\\circ = {raw_theta}^\\circ$.\n"
        f"4. Reduce modulo $360^\\circ$:\n"
        f"   ${raw_theta}^\\circ = {raw_theta // 360} \\times 360^\\circ + {reduced_theta}^\\circ \\implies \\theta = {reduced_theta}^\\circ$.\n"
        f"5. Result: $z^{{{n}}} = {r_pow}\\operatorname{{cis}}({reduced_theta}^\\circ)$."
    )

    vectors = [
        (float(r), float(theta), f"z({r},{theta}deg)", "#2563eb"),
        (float(r_pow), float(reduced_theta), f"z^{n}({r_pow},{reduced_theta}deg)", "#16a34a"),
    ]
    svg = _make_argand_svg(vectors, max_r=float(r_pow) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "32_de_moivre_theorem_higher_power_with_angle_reduction",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "mode": "elementary_de_moivre_reduction",
        "difficulty": "medium",
        "marks": 4,
        "misconception_tags": ["forgot_angle_reduction_mod_360", "multiplied_modulus_instead_of_power"],
        "hints": {
            "tier_1": "Calculate $r^n$ and $n\\theta$. Then subtract multiples of $360^\\circ$ until the argument is between $0^\\circ$ and $360^\\circ$.",
            "tier_2": f"Modulus: ${r}^{{{n}}} = {r_pow}$. Raw argument: ${raw_theta}^\\circ$. Coterminal argument: ${reduced_theta}^\\circ$.",
            "tier_3": f"Final answer: ${r_pow}\\operatorname{{cis}}({reduced_theta}^\\circ)$.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Modulus calculation {r}^{n} = {r_pow}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Raw argument calculation {n} * {theta} = {raw_theta} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Coterminal angle reduction to {reduced_theta} deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final statement {r_pow} cis({reduced_theta} deg)", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 33: de Moivre's Theorem Convert to Rectangular Form
# --------------------------------------------------------------------------- #
def build_33_de_moivre_theorem_convert_to_rectangular(rng: random.Random) -> Dict[str, Any]:
    # Select nice combinations where n * theta lands on special angles
    choices = [
        (2, 15, 6, 90, 64, 0, 64, "64i"),
        (2, 30, 3, 90, 8, 0, 8, "8i"),
        (2, 45, 4, 180, 16, -16, 0, "-16"),
        (2, 45, 2, 90, 4, 0, 4, "4i"),
        (2, 60, 3, 180, 8, -8, 0, "-8"),
        (2, 30, 6, 180, 64, -64, 0, "-64"),
        (2, 45, 6, 270, 64, 0, -64, "-64i"),
        (2, 90, 3, 270, 8, 0, -8, "-8i"),
    ]
    r, theta, n, target_deg, r_pow, a_val, b_val, rect_str = rng.choice(choices)

    prompt = (
        f"A complex number $z = {r}\\operatorname{{cis}}({theta}^\\circ)$ is given in polar form.\n\n"
        f"The vector representing $z$ is plotted on the Argand plane shown.\n\n"
        f"1. Apply de Moivre's Theorem to write $z^{{{n}}}$ in polar form $r\\operatorname{{cis}}\\theta$.\n"
        f"2. Hence, convert $z^{{{n}}}$ to rectangular form $a + bi$ without using a calculator."
    )

    ans_latex = rf"z^{{{n}}} = {r_pow}\operatorname{{cis}}({target_deg}^\circ) = {rect_str}"
    worked_solution = (
        f"1. By de Moivre's Theorem: $z^{{{n}}} = {r}^{{{n}}}\\operatorname{{cis}}({n} \\times {theta}^\\circ) = {r_pow}\\operatorname{{cis}}({target_deg}^\\circ)$.\n"
        f"2. Convert to rectangular form $a + bi = r(\\cos\\theta + i\\sin\\theta)$:\n"
        f"   $\\cos({target_deg}^\\circ) = {_fmt_sa(math.cos(math.radians(target_deg)))}$, "
        f"   $\\sin({target_deg}^\\circ) = {_fmt_sa(math.sin(math.radians(target_deg)))}$.\n"
        f"3. $z^{{{n}}} = {r_pow}(\\cos({target_deg}^\\circ) + i\\sin({target_deg}^\\circ)) = {rect_str}$."
    )

    vectors = [
        (float(r), float(theta), f"z({r},{theta}deg)", "#2563eb"),
        (float(r_pow), float(target_deg), f"z^{n}={rect_str}", "#16a34a"),
    ]
    svg = _make_argand_svg(vectors, max_r=float(r_pow) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "33_de_moivre_theorem_convert_to_rectangular",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "elementary_de_moivre_to_rectangular",
        "difficulty": "medium",
        "marks": 5,
        "misconception_tags": ["confused_sin_cos_special_values", "sign_error_in_quadrant_values"],
        "hints": {
            "tier_1": "First apply de Moivre's Theorem to get $r^n \\operatorname{cis}(n\\theta)$. Then evaluate $\\cos(n\\theta)$ and $\\sin(n\\theta)$ using special angles.",
            "tier_2": f"Polar form: ${r_pow}\\operatorname{{cis}}({target_deg}^\\circ)$. Recall $\\cos({target_deg}^\\circ)$ and $\\sin({target_deg}^\\circ)$.",
            "tier_3": f"Final rectangular form: ${rect_str}$.",
        },
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Modulus r^{n} = {r_pow}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Argument n*theta = {target_deg} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Polar form {r_pow} cis({target_deg} deg)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Trigonometric expansion {r_pow}(cos({target_deg}) + i sin({target_deg}))", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Final rectangular answer: {rect_str}", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 34: de Moivre's Theorem for Negative Integer Powers
# --------------------------------------------------------------------------- #
def build_34_de_moivre_theorem_negative_integer_power(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([2, 3, 4])
    theta = rng.choice([30, 45, 60, 90, 120])
    n = rng.choice([1, 2])

    neg_n = -n
    r_pow_denom = r**n
    raw_theta = -n * theta
    reduced_theta = (360 + (raw_theta % 360)) % 360

    prompt = (
        f"A complex number $z = {r}\\operatorname{{cis}}({theta}^\\circ)$ is represented on the Argand plane shown.\n\n"
        f"Use de Moivre's Theorem to evaluate $z^{{{neg_n}}}$ in standard polar form $r\\operatorname{{cis}}\\theta$, "
        f"with $r > 0$ and $0^\\circ \\le \\theta < 360^\\circ$."
    )

    ans_latex = rf"z^{{{neg_n}}} = \frac{{1}}{{{r_pow_denom}}}\operatorname{{cis}}({reduced_theta}^\circ)"
    worked_solution = (
        f"1. Apply de Moivre's Theorem for negative integer exponents:\n"
        f"   $z^{{{neg_n}}} = {r}^{{{neg_n}}}\\operatorname{{cis}}({neg_n} \\times {theta}^\\circ)$.\n"
        f"2. Modulus: $r^{{{neg_n}}} = \\frac{{1}}{{{r}^{{{n}}}}} = \\frac{{1}}{{{r_pow_denom}}}$.\n"
        f"3. Argument: $\\theta_{{\\text{{raw}}}} = {raw_theta}^\\circ$.\n"
        f"4. Convert to standard positive angle $0^\\circ \\le \\theta < 360^\\circ$:\n"
        f"   $\\theta = {raw_theta}^\\circ + 360^\\circ = {reduced_theta}^\\circ$.\n"
        f"5. Result: $z^{{{neg_n}}} = \\frac{{1}}{{{r_pow_denom}}}\\operatorname{{cis}}({reduced_theta}^\\circ)$."
    )

    vectors = [
        (float(r), float(theta), f"z({r},{theta}deg)", "#2563eb"),
        (float(1.0 / r_pow_denom), float(reduced_theta), f"z^{neg_n}", "#16a34a"),
    ]
    svg = _make_argand_svg(vectors, max_r=float(r) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "34_de_moivre_theorem_negative_integer_power",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "mode": "elementary_de_moivre_negative_power",
        "difficulty": "medium",
        "marks": 4,
        "misconception_tags": ["negated_modulus_instead_of_reciprocal", "left_negative_argument_in_polar_form"],
        "hints": {
            "tier_1": "For a negative power $z^{-n} = r^{-n} \\operatorname{cis}(-n\\theta) = \\frac{1}{r^n} \\operatorname{cis}(-n\\theta)$.",
            "tier_2": f"Modulus: $1 / {r}^{{{n}}} = 1 / {r_pow_denom}$. Add $360^\\circ$ to the negative angle ${raw_theta}^\\circ$ to get ${reduced_theta}^\\circ$.",
            "tier_3": f"Final answer: $\\frac{{1}}{{{r_pow_denom}}}\\operatorname{{cis}}({reduced_theta}^\\circ)$.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Reciprocal modulus 1 / {r_pow_denom}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Negative argument calculation {neg_n} * {theta} = {raw_theta} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Positive angle conversion to {reduced_theta} deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Correct polar expression (1/{r_pow_denom}) cis({reduced_theta} deg)", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 35: Complex Square Roots in Polar Form
# --------------------------------------------------------------------------- #
def build_35_complex_square_roots_polar_form(rng: random.Random) -> Dict[str, Any]:
    r_root = rng.choice([2, 3, 4, 5])
    r = r_root**2

    theta = rng.choice([40, 60, 80, 100, 120, 140])

    theta_0 = theta // 2
    theta_1 = theta_0 + 180

    prompt = (
        f"A complex number $z = {r}\\operatorname{{cis}}({theta}^\\circ)$ is represented on the Argand plane shown.\n\n"
        f"Determine the two distinct complex square roots of $z$ in polar form $r\\operatorname{{cis}}\\theta$, "
        f"where $0^\\circ \\le \\theta < 360^\\circ$."
    )

    ans_latex = (
        rf"w_0 = {r_root}\operatorname{{cis}}({theta_0}^\circ), \quad "
        rf"w_1 = {r_root}\operatorname{{cis}}({theta_1}^\circ)"
    )
    worked_solution = (
        f"1. Apply the $n$-th root formula for complex numbers: $w_k = \\sqrt[n]{{r}}\\operatorname{{cis}}\\left(\\frac{{\\theta + 360^\\circ k}}{{n}}\\right)$ for $k = 0, 1$.\n"
        f"2. Modulus of each root: $\\sqrt{{{r}}} = {r_root}$.\n"
        f"3. First root ($k = 0$): $\\theta_0 = \\frac{{{theta}^\\circ}}{{2}} = {theta_0}^\\circ \\implies w_0 = {r_root}\\operatorname{{cis}}({theta_0}^\\circ)$.\n"
        f"4. Second root ($k = 1$): $\\theta_1 = \\frac{{{theta}^\\circ + 360^\\circ}}{{2}} = {theta_0}^\\circ + 180^\\circ = {theta_1}^\\circ \\implies w_1 = {r_root}\\operatorname{{cis}}({theta_1}^\\circ)$.\n"
        f"5. The two roots lie on a circle of radius ${r_root}$ diametrically opposite each other."
    )

    vectors = [
        (float(r), float(theta), f"z({r},{theta}deg)", "#2563eb"),
        (float(r_root), float(theta_0), f"w0({r_root},{theta_0}deg)", "#16a34a"),
        (float(r_root), float(theta_1), f"w1({r_root},{theta_1}deg)", "#dc2626"),
    ]
    svg = _make_argand_svg(vectors, circle_radius=float(r_root), max_r=float(max(r, r_root * 2)) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "35_complex_square_roots_polar_form",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "elementary_complex_square_roots",
        "difficulty": "medium",
        "marks": 5,
        "misconception_tags": ["forgot_second_root_separated_by_180", "divided_modulus_instead_of_taking_square_root"],
        "hints": {
            "tier_1": "Take the square root of the modulus ($\\sqrt{r}$) and divide the argument by 2 for the first root. Add $180^\\circ$ for the second root.",
            "tier_2": f"Modulus: $\\sqrt{{{r}}} = {r_root}$. Angles: ${theta}^\\circ / 2 = {theta_0}^\\circ$ and ${theta_0}^\\circ + 180^\\circ = {theta_1}^\\circ$.",
            "tier_3": f"Final roots: $w_0 = {r_root}\\operatorname{{cis}}({theta_0}^\\circ)$ and $w_1 = {r_root}\\operatorname{{cis}}({theta_1}^\\circ)$.",
        },
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Root modulus sqrt({r}) = {r_root}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"First argument theta / 2 = {theta_0} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"First root w0 = {r_root} cis({theta_0} deg)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Second argument separation +180 deg = {theta_1} deg", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Second root w1 = {r_root} cis({theta_1} deg)", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 36: Complex Cube Roots in Polar Form
# --------------------------------------------------------------------------- #
def build_36_complex_cube_roots_polar_form(rng: random.Random) -> Dict[str, Any]:
    r_root = rng.choice([2, 3])
    r = r_root**3

    theta = rng.choice([30, 45, 60, 90, 120, 150])

    theta_0 = theta // 3
    theta_1 = theta_0 + 120
    theta_2 = theta_0 + 240

    prompt = (
        f"A complex number $z = {r}\\operatorname{{cis}}({theta}^\\circ)$ is given.\n\n"
        f"The root vectors are depicted on the Argand plane shown.\n\n"
        f"Calculate all three distinct complex cube roots of $z$ in polar form $r\\operatorname{{cis}}\\theta$, "
        f"where $0^\\circ \\le \\theta < 360^\\circ$."
    )

    ans_latex = (
        rf"w_0 = {r_root}\operatorname{{cis}}({theta_0}^\circ), \quad "
        rf"w_1 = {r_root}\operatorname{{cis}}({theta_1}^\circ), \quad "
        rf"w_2 = {r_root}\operatorname{{cis}}({theta_2}^\circ)"
    )
    worked_solution = (
        f"1. Apply complex root formula: $w_k = \\sqrt[3]{{r}}\\operatorname{{cis}}\\left(\\frac{{\\theta + 360^\\circ k}}{{3}}\\right)$ for $k = 0, 1, 2$.\n"
        f"2. Modulus: $\\sqrt[3]{{{r}}} = {r_root}$.\n"
        f"3. First root ($k = 0$): $\\theta_0 = \\frac{{{theta}^\\circ}}{{3}} = {theta_0}^\\circ \\implies w_0 = {r_root}\\operatorname{{cis}}({theta_0}^\\circ)$.\n"
        f"4. Second root ($k = 1$): $\\theta_1 = {theta_0}^\\circ + 120^\\circ = {theta_1}^\\circ \\implies w_1 = {r_root}\\operatorname{{cis}}({theta_1}^\\circ)$.\n"
        f"5. Third root ($k = 2$): $\\theta_2 = {theta_0}^\\circ + 240^\\circ = {theta_2}^\\circ \\implies w_2 = {r_root}\\operatorname{{cis}}({theta_2}^\\circ)$.\n"
        f"6. The three roots form an equilateral triangle on a circle of radius ${r_root}$."
    )

    vectors = [
        (float(r_root), float(theta_0), f"w0({r_root},{theta_0}deg)", "#16a34a"),
        (float(r_root), float(theta_1), f"w1({r_root},{theta_1}deg)", "#2563eb"),
        (float(r_root), float(theta_2), f"w2({r_root},{theta_2}deg)", "#dc2626"),
    ]
    pts = [
        (r_root * math.cos(math.radians(theta_0)), r_root * math.sin(math.radians(theta_0))),
        (r_root * math.cos(math.radians(theta_1)), r_root * math.sin(math.radians(theta_1))),
        (r_root * math.cos(math.radians(theta_2)), r_root * math.sin(math.radians(theta_2))),
    ]
    svg = _make_argand_svg(vectors, polygon_points=pts, circle_radius=float(r_root), max_r=float(r_root) * 1.35, seed=rng.randint(1000, 999999))

    return {
        "subskill": "36_complex_cube_roots_polar_form",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "elementary_complex_cube_roots",
        "difficulty": "hard",
        "marks": 6,
        "misconception_tags": ["incorrect_angular_separation_for_cube_roots", "divided_modulus_instead_of_taking_cube_root"],
        "hints": {
            "tier_1": "Modulus of each root is $\\sqrt[3]{r}$. The first argument is $\\theta/3$, and successive roots are separated by $360^\\circ / 3 = 120^\\circ$.",
            "tier_2": f"Modulus: $\\sqrt[3]{{{r}}} = {r_root}$. Arguments: ${theta_0}^\\circ$, ${theta_0}^\\circ + 120^\\circ = {theta_1}^\\circ$, and ${theta_0}^\\circ + 240^\\circ = {theta_2}^\\circ$.",
            "tier_3": f"Final roots: $w_0 = {r_root}\\operatorname{{cis}}({theta_0}^\\circ)$, $w_1 = {r_root}\\operatorname{{cis}}({theta_1}^\\circ)$, $w_2 = {r_root}\\operatorname{{cis}}({theta_2}^\\circ)$.",
        },
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Modulus cube root {r_root}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"First argument theta / 3 = {theta_0} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"First root w0 = {r_root} cis({theta_0} deg)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Second root w1 = {r_root} cis({theta_1} deg)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Third root w2 = {r_root} cis({theta_2} deg)", "marks": 1, "editable": True},
                {"id": "mp6", "desc": "120 degree regular angular separation verified", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 37: Argand Roots Regular Polygon Geometry
# --------------------------------------------------------------------------- #
def build_37_argand_roots_regular_polygon_geometry(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([3, 4])
    r_root = rng.choice([2, 3, 4])
    r_orig = r_root**n
    theta_orig = rng.choice([0, 30, 45, 60])

    theta_0 = theta_orig // n
    ang_sep = 360 // n
    shape_name = "an equilateral triangle" if n == 3 else "a square"

    if n == 3:
        side_len_formula = rf"{r_root}\sqrt{{3}}"
        side_len_approx = round(r_root * math.sqrt(3), 2)
    else:
        side_len_formula = rf"{r_root}\sqrt{{2}}"
        side_len_approx = round(r_root * math.sqrt(2), 2)

    prompt = (
        f"The equation $w^{{{n}}} = {r_orig}\\operatorname{{cis}}({theta_orig}^\\circ)$ has ${n}$ complex roots.\n\n"
        f"The root vectors are plotted on the Argand plane shown, forming the vertices of a regular polygon.\n\n"
        f"1. State the radius $R$ of the circle on which all ${n}$ roots lie.\n"
        f"2. Calculate the angular separation $\\Delta\\theta$ between adjacent roots.\n"
        f"3. Confirm that the roots form {shape_name} and determine the exact distance between adjacent vertices."
    )

    ans_latex = (
        rf"R = {r_root}, \quad \Delta\theta = {ang_sep}^\circ, \quad "
        rf"\text{{Distance}} = {side_len_formula} \approx {_fmt_sa(side_len_approx)}"
    )
    worked_solution = (
        f"1. Circle radius: $R = \\sqrt[{{{n}}}]{{{r_orig}}} = {r_root}$.\n"
        f"2. Angular separation: $\\Delta\\theta = \\frac{{360^\\circ}}{{{n}}} = {ang_sep}^\\circ$.\n"
        f"3. Distance between adjacent roots (using cosine rule with $R = {r_root}$ and $\\Delta\\theta = {ang_sep}^\\circ$):\n"
        f"   $d^2 = R^2 + R^2 - 2R^2\\cos({ang_sep}^\\circ) = 2({r_root})^2(1 - \\cos({ang_sep}^\\circ))$.\n"
        f"   For $n = {n}$, this gives $d = {side_len_formula} \\approx {_fmt_sa(side_len_approx)}$."
    )

    vectors = []
    pts = []
    for k in range(n):
        deg = (theta_0 + k * ang_sep) % 360
        vectors.append((float(r_root), float(deg), f"w{k}", "#9333ea"))
        pts.append((r_root * math.cos(math.radians(deg)), r_root * math.sin(math.radians(deg))))

    svg = _make_argand_svg(vectors, polygon_points=pts, circle_radius=float(r_root), max_r=float(r_root) * 1.35, seed=rng.randint(1000, 999999))

    return {
        "subskill": "37_argand_roots_regular_polygon_geometry",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "elementary_argand_roots_polygon",
        "difficulty": "hard",
        "marks": 6,
        "misconception_tags": ["confused_root_radius_with_original_modulus", "incorrect_polygon_side_calculation"],
        "hints": {
            "tier_1": "The roots of $w^n = z$ lie evenly spaced on a circle of radius $R = \\sqrt[n]{r}$.",
            "tier_2": f"Radius $R = {r_root}$. Angular spacing is $360^\\circ / {n} = {ang_sep}^\\circ$.",
            "tier_3": f"Exact vertex distance: ${side_len_formula}$.",
        },
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Circle radius R = {r_root}", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Angular separation Delta theta = {ang_sep} deg", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Adjacent vertex distance {side_len_formula}", "marks": 2, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 38: Rectangular to Polar then Apply de Moivre's Theorem
# --------------------------------------------------------------------------- #
def build_38_rectangular_to_polar_then_de_moivre(rng: random.Random) -> Dict[str, Any]:
    # Select nice rectangular base that converts to special angles
    configs = [
        ("1 + i", 1, 1, 45, 4, 180, "-4"),
        ("1 - i", 1, -1, 315, 4, 180, "-4"),
        ("-1 + i", -1, 1, 135, 4, 180, "-4"),
        (r"\sqrt{3} + i", math.sqrt(3), 1, 30, 3, 90, "8i"),
        (r"1 + \sqrt{3}i", 1, math.sqrt(3), 60, 3, 180, "-8"),
        (r"\sqrt{3} - i", math.sqrt(3), -1, 330, 3, 270, "-8i"),
    ]
    label_z, a, b, theta, n, final_deg, rect_str = rng.choice(configs)

    if "sqrt{3}" in label_z:
        r_mod = 2
        r_pow = r_mod**n
    else:
        # 1 +/- i has r = sqrt(2), (sqrt(2))^4 = 4
        r_mod = "sqrt(2)"
        r_pow = 4

    prompt = (
        f"Consider the complex number in rectangular form $z = {label_z}$.\n\n"
        f"The vector representing $z$ is plotted on the Argand plane shown.\n\n"
        f"1. Convert $z$ to polar form $r\\operatorname{{cis}}\\theta$, with $0^\\circ \\le \\theta < 360^\\circ$.\n"
        f"2. Hence, apply de Moivre's Theorem to calculate $z^{{{n}}}$ in rectangular form $a + bi$."
    )

    ans_latex = rf"z = \sqrt{{{4 if 'sqrt{3}' in label_z else 2}}}\operatorname{{cis}}({theta}^\circ), \quad z^{{{n}}} = {rect_str}"
    worked_solution = (
        f"1. Calculate modulus: $r = \\sqrt{{a^2 + b^2}} = {2 if 'sqrt{3}' in label_z else '\\sqrt{2}'}$.\n"
        f"2. Argument: $\\theta = {theta}^\\circ$ (from quadrant inspection).\n"
        f"3. Polar form: $z = {2 if 'sqrt{3}' in label_z else '\\sqrt{2}'}\\operatorname{{cis}}({theta}^\\circ)$.\n"
        f"4. Apply de Moivre's Theorem:\n"
        f"   $z^{{{n}}} = ({2 if 'sqrt{3}' in label_z else '\\sqrt{2}'})^{{{n}}}\\operatorname{{cis}}({n} \\times {theta}^\\circ) = {r_pow}\\operatorname{{cis}}({final_deg}^\\circ)$.\n"
        f"5. Convert back to rectangular form:\n"
        f"   ${r_pow}(\\cos({final_deg}^\\circ) + i\\sin({final_deg}^\\circ)) = {rect_str}$."
    )

    vectors = [
        (2.0 if "sqrt{3}" in label_z else 1.414, float(theta), f"z({label_z})", "#2563eb"),
        (float(r_pow), float(final_deg), f"z^{n}={rect_str}", "#16a34a"),
    ]
    svg = _make_argand_svg(vectors, max_r=float(r_pow) * 1.15, seed=rng.randint(1000, 999999))

    return {
        "subskill": "38_rectangular_to_polar_then_de_moivre",
        "topic": "technical_mathematics_complex_numbers",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "elementary_rect_to_polar_de_moivre",
        "difficulty": "hard",
        "marks": 6,
        "misconception_tags": ["expanded_binomial_directly_instead_of_polar", "forgot_quadrant_correction_argument"],
        "hints": {
            "tier_1": "Convert the base complex number to polar form first ($r\\operatorname{cis}\\theta$), then apply $(r\\operatorname{cis}\\theta)^n = r^n \\operatorname{cis}(n\\theta)$.",
            "tier_2": f"Modulus is ${2 if 'sqrt{3}' in label_z else '\\sqrt{2}'}$ and argument is ${theta}^\\circ$. Power: ${r_pow}\\operatorname{{cis}}({final_deg}^\\circ)$.",
            "tier_3": f"Final rectangular answer: ${rect_str}$.",
        },
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Modulus calculation", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Argument determination {theta} deg", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Polar form statement", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"de Moivre application {r_pow} cis({final_deg} deg)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Trig evaluation at {final_deg} deg", "marks": 1, "editable": True},
                {"id": "mp6", "desc": f"Final rectangular answer: {rect_str}", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Export Dictionary
# --------------------------------------------------------------------------- #
BUILDERS_26_38: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_polar_multiplication_moduli_and_arguments": build_26_polar_multiplication_moduli_and_arguments,
    "27_polar_multiplication_angle_reduction": build_27_polar_multiplication_angle_reduction,
    "28_polar_division_moduli_and_arguments": build_28_polar_division_moduli_and_arguments,
    "29_polar_division_negative_angle_adjustment": build_29_polar_division_negative_angle_adjustment,
    "30_polar_combined_multiplication_and_division": build_30_polar_combined_multiplication_and_division,
    "31_de_moivre_theorem_small_positive_power": build_31_de_moivre_theorem_small_positive_power,
    "32_de_moivre_theorem_higher_power_with_angle_reduction": build_32_de_moivre_theorem_higher_power_with_angle_reduction,
    "33_de_moivre_theorem_convert_to_rectangular": build_33_de_moivre_theorem_convert_to_rectangular,
    "34_de_moivre_theorem_negative_integer_power": build_34_de_moivre_theorem_negative_integer_power,
    "35_complex_square_roots_polar_form": build_35_complex_square_roots_polar_form,
    "36_complex_cube_roots_polar_form": build_36_complex_cube_roots_polar_form,
    "37_argand_roots_regular_polygon_geometry": build_37_argand_roots_regular_polygon_geometry,
    "38_rectangular_to_polar_then_de_moivre": build_38_rectangular_to_polar_then_de_moivre,
}
