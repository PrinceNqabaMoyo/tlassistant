"""Grade 12 Technical Mathematics — Complex Numbers: Archetypes 39–50
===================================================================
100% Aligned with South African National Curriculum Standards (Technical Mathematics Grade 12).
Grounded strictly in curriculum_docs_auto/TechnicalMathematics_Gr12/Term 1/01. Complex numbers.md.

Covers subskills 39–50:
- 39_complex_fourth_roots_de_moivre
- 40_roots_of_unity_polygon
- 41_solve_quadratic_equation_pure_imaginary
- 42_solve_quadratic_equation_complex_roots
- 43_solve_cubic_equation_one_real_two_complex
- 44_ac_impedance_pure_inductive_reactance
- 45_ac_impedance_pure_capacitive_reactance
- 46_ac_impedance_series_rl_circuit
- 47_ac_impedance_series_rc_circuit
- 48_ac_impedance_series_rlc_circuit
- 49_ac_circuit_ohms_law_voltage_current
- 50_technical_complex_ac_synthesis_capstone
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


def _make_phasor_svg(
    title: str,
    vectors: List[Tuple[float, float, str, str]],  # (mag, angle_deg, label, color)
    seed: int = 42,
    max_val: float = 100.0,
) -> Dict[str, Any]:
    """Generate dynamic seed-varied inline SVG for Argand plane and AC Phasor diagrams."""
    width, height = 400, 320
    cx, cy = 190, 160
    scale = 130.0 / max(max_val, 1.0)

    elements: List[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" data-seed="{seed}" style="background-color: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px;">',
        f'<text x="200" y="22" font-size="12" font-family="system-ui,sans-serif" font-weight="bold" fill="#1e293b" text-anchor="middle">{title}</text>',
        '<defs>',
        '  <marker id="arr-blue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2563eb"/></marker>',
        '  <marker id="arr-red" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#dc2626"/></marker>',
        '  <marker id="arr-green" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#16a34a"/></marker>',
        '  <marker id="arr-purple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#9333ea"/></marker>',
        '</defs>',
    ]

    # Grid lines
    for stp in [-100, -50, 50, 100]:
        elements.append(f'<line x1="{cx + stp}" y1="35" x2="{cx + stp}" y2="285" stroke="#f1f5f9" stroke-width="1"/>')
        elements.append(f'<line x1="30" y1="{cy + stp}" x2="350" y2="{cy + stp}" stroke="#f1f5f9" stroke-width="1"/>')

    # Main axes
    elements.append(f'<line x1="25" y1="{cy}" x2="355" y2="{cy}" stroke="#64748b" stroke-width="1.8"/>')
    elements.append(f'<line x1="{cx}" y1="285" x2="{cx}" y2="35" stroke="#64748b" stroke-width="1.8"/>')

    elements.append(f'<text x="360" y="{cy - 6}" font-size="11" font-family="system-ui,sans-serif" font-weight="bold" fill="#334155">Re / R</text>')
    elements.append(f'<text x="{cx + 6}" y="45" font-size="11" font-family="system-ui,sans-serif" font-weight="bold" fill="#334155">+j (Im)</text>')
    elements.append(f'<text x="{cx + 6}" y="280" font-size="11" font-family="system-ui,sans-serif" font-weight="bold" fill="#334155">-j</text>')
    elements.append(f'<text x="{cx - 12}" y="{cy + 15}" font-size="10" font-family="system-ui,sans-serif" fill="#94a3b8">O</text>')

    color_marker = {
        "#2563eb": "arr-blue",
        "#dc2626": "arr-red",
        "#16a34a": "arr-green",
        "#9333ea": "arr-purple",
    }

    for mag, deg, lbl, col in vectors:
        rad = math.radians(deg)
        vx = mag * math.cos(rad)
        vy = mag * math.sin(rad)
        x_px = cx + vx * scale
        y_px = cy - vy * scale
        mid_x = cx + (vx * 0.55) * scale
        mid_y = cy - (vy * 0.55) * scale
        mk = color_marker.get(col, "arr-blue")

        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x_px:.1f}" y2="{y_px:.1f}" stroke="{col}" stroke-width="2.2" marker-end="url(#{mk})"/>')
        elements.append(f'<text x="{mid_x + 6:.1f}" y="{mid_y - 4:.1f}" font-size="11" font-family="system-ui,sans-serif" font-weight="bold" fill="{col}">{lbl}</text>')

    elements.append("</svg>")
    return {
        "kind": "inline_svg",
        "svg": "".join(elements),
        "diagram_role": "context",
        "title": title,
    }


# --------------------------------------------------------------------------- #
# 39. Complex Fourth Roots using de Moivre's Theorem
# --------------------------------------------------------------------------- #
def arch_39_complex_fourth_roots_de_moivre(r: random.Random) -> Dict[str, Any]:
    r_val = r.choice([16, 81, 256, 625])
    theta_deg = r.choice([60, 120, 180, 240])
    root_r = int(round(r_val ** 0.25))
    base_ang = theta_deg // 4
    step_ang = 90
    angles = [(base_ang + step_ang * k) % 360 for k in range(4)]
    seed_val = r.randint(100, 99999)

    vectors = [(root_r, ang, f"w_{k}", "#2563eb") for k, ang in enumerate(angles)]
    diag = _make_phasor_svg(
        f"Fourth Roots of {r_val} cis({theta_deg}°) in Argand Plane",
        vectors,
        seed=seed_val,
        max_val=root_r * 1.3,
    )

    prompt = (
        f"Given the complex number in polar form $z = {r_val}\\operatorname{{cis}}({theta_deg}^\\circ)$.\n\n"
        f"Apply de Moivre's Theorem to calculate all FOUR roots $w_k = z^{{1/4}}$ for $k = 0, 1, 2, 3$. "
        f"State each root in polar form $r\\operatorname{{cis}}\\theta$ where $0^\\circ \\le \\theta < 360^\\circ$."
    )

    sol_roots = [f"{root_r}\\operatorname{{cis}}({ang}^\\circ)" for ang in angles]
    ans_latex = r", \quad ".join([f"w_{k} = {sol_roots[k]}" for k in range(4)])

    sol = (
        f"Step 1: Formula for $n$-th roots via de Moivre's Theorem:\n"
        f"$$w_k = r^{{1/n}} \\operatorname{{cis}}\\left(\\frac{{\\theta + 360^\\circ k}}{{n}}\\right), \\quad k = 0, 1, 2, 3$$\n\n"
        f"Step 2: Modulus of the roots: $r' = ({r_val})^{{1/4}} = {root_r}$.\n\n"
        f"Step 3: Calculate arguments for $k = 0, 1, 2, 3$:\n"
        f"- For $k = 0$: $\\theta_0 = \\frac{{{theta_deg}^\\circ}}{{4}} = {angles[0]}^\\circ \\implies w_0 = {sol_roots[0]}$\n"
        f"- For $k = 1$: $\\theta_1 = \\frac{{{theta_deg}^\\circ + 360^\\circ}}{{4}} = {angles[1]}^\\circ \\implies w_1 = {sol_roots[1]}$\n"
        f"- For $k = 2$: $\\theta_2 = \\frac{{{theta_deg}^\\circ + 720^\\circ}}{{4}} = {angles[2]}^\\circ \\implies w_2 = {sol_roots[2]}$\n"
        f"- For $k = 3$: $\\theta_3 = \\frac{{{theta_deg}^\\circ + 1080^\\circ}}{{4}} = {angles[3]}^\\circ \\implies w_3 = {sol_roots[3]}$"
    )

    return {
        "id": f"tech_cplx_39_{seed_val}",
        "title": "Complex Fourth Roots via de Moivre's Theorem",
        "subskill": "39_complex_fourth_roots_de_moivre",
        "question_family_id": "39_complex_fourth_roots_de_moivre",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"w0={sol_roots[0]}, w1={sol_roots[1]}, w2={sol_roots[2]}, w3={sol_roots[3]}",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Modulus root r = {root_r}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Root w0 = {sol_roots[0]}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Root w1 = {sol_roots[1]}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Root w2 = {sol_roots[2]}", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Root w3 = {sol_roots[3]}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_roots", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "de Moivre's roots formula: $w_k = r^{1/n}\\operatorname{cis}((\\theta + 360^\\circ k)/n)$.",
            "tier_2": f"Modulus is ${r_val}^{{1/4}} = {root_r}$. The angular separation between roots is $360^\\circ / 4 = 90^\\circ$.",
            "tier_3": f"Roots: {ans_latex}.",
        },
        "misconception_tags": ["forgot_to_add_360_multiples_for_roots", "did_not_take_fourth_root_of_modulus"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "difficulty": "hard",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 40. Roots of Unity & Argand Regular Polygon Geometry
# --------------------------------------------------------------------------- #
def arch_40_roots_of_unity_polygon(r: random.Random) -> Dict[str, Any]:
    n = r.choice([3, 4, 5, 6])
    step_ang = 360 // n
    seed_val = r.randint(100, 99999)

    angles = [step_ang * k for k in range(n)]
    vectors = [(1.0, ang, f"w_{k}", "#9333ea") for k, ang in enumerate(angles)]
    polygon_name = {3: "equilateral triangle", 4: "square", 5: "regular pentagon", 6: "regular hexagon"}[n]

    diag = _make_phasor_svg(
        f"{n}-th Roots of Unity on Unit Circle ({polygon_name})",
        vectors,
        seed=seed_val,
        max_val=1.5,
    )

    prompt = (
        f"Consider the equation $z^{{{n}}} = 1$ in the complex numbers.\n\n"
        f"1. Write down the $n$ distinct roots of unity in polar form $r\\operatorname{{cis}}\\theta$ "
        f"where $0^\\circ \\le \\theta < 360^\\circ$.\n"
        f"2. Identify the geometric polygon formed by plotting these roots as vertices on the Argand plane."
    )

    sol_roots = [f"1\\operatorname{{cis}}({ang}^\\circ)" for ang in angles]
    ans_latex = (
        r"\text{Roots: } " + r", \; ".join([f"w_{k} = {sol_roots[k]}" for k in range(n)]) +
        rf", \quad \text{{Polygon: {polygon_name}}}"
    )

    sol = (
        f"Step 1: Write 1 in polar form: $1 = 1\\operatorname{{cis}}(0^\\circ)$.\n\n"
        f"Step 2: Apply de Moivre's theorem for $n$-th roots:\n"
        f"$$w_k = 1^{{1/{n}}} \\operatorname{{cis}}\\left(\\frac{{0^\\circ + 360^\\circ k}}{{{n}}}\\right) = 1\\operatorname{{cis}}({step_ang}^\\circ k)$$\n"
        f"For $k = 0, 1, \\dots, {n-1}$:\n" +
        "\n".join([f"- $w_{k} = {sol_roots[k]}$" for k in range(n)]) +
        f"\n\nStep 3: Geometry: All roots lie on the unit circle $|z| = 1$ separated by {step_ang}°, "
        f"forming the vertices of a **{polygon_name}**."
    )

    return {
        "id": f"tech_cplx_40_{seed_val}",
        "title": "Roots of Unity and Regular Polygon Geometry",
        "subskill": "40_roots_of_unity_polygon",
        "question_family_id": "40_roots_of_unity_polygon",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"polygon={polygon_name}, step={step_ang}",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "1 in polar form: 1 cis(0 deg)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct roots separated by {step_ang} deg", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Geometric identification: {polygon_name}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": f"Express $1$ as $1\\operatorname{{cis}}(0^\\circ)$ and divide $360^\\circ$ by ${n}$.",
            "tier_2": f"The roots are equally spaced by ${step_ang}^\\circ$ around the unit circle $|z| = 1$.",
            "tier_3": f"They form a {polygon_name}: {', '.join(sol_roots)}.",
        },
        "misconception_tags": ["confused_roots_of_unity_with_real_one_only", "wrong_polygon_geometry"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 41. Solving Pure Imaginary Quadratic Equations (z^2 + d = 0)
# --------------------------------------------------------------------------- #
def arch_41_solve_quadratic_equation_pure_imaginary(r: random.Random) -> Dict[str, Any]:
    k = r.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    d = k * k
    seed_val = r.randint(100, 99999)

    vectors = [(k, 90, f"+{k}i", "#dc2626"), (k, 270, f"-{k}i", "#dc2626")]
    diag = _make_phasor_svg(
        f"Roots of z² + {d} = 0 on Imaginary Axis",
        vectors,
        seed=seed_val,
        max_val=k * 1.4,
    )

    prompt = (
        f"Solve the quadratic equation in the complex number field $\\mathbb{{C}}$:\n"
        f"$$z^2 + {d} = 0$$\n\n"
        f"State the solutions in rectangular form $z = a + bi$ and plot them on the Argand plane."
    )

    ans_latex = rf"z = \pm {k}i \quad (z_1 = {k}i, \; z_2 = -{k}i)"

    sol = (
        f"Step 1: Rearrange the equation:\n"
        f"$$z^2 = -{d}$$\n\n"
        f"Step 2: Take square roots of both sides:\n"
        f"$$z = \\pm \\sqrt{{-{d}}} = \\pm \\sqrt{{{d}}} \\cdot \\sqrt{{-1}} = \\pm {k}i$$\n\n"
        f"Step 3: Argand plane location:\n"
        f"Both roots are pure imaginary, lying symmetrically on the vertical imaginary axis at $(0; {k})$ and $(0; -{k})$."
    )

    return {
        "id": f"tech_cplx_41_{seed_val}",
        "title": "Solving Pure Imaginary Quadratic Equation",
        "subskill": "41_solve_quadratic_equation_pure_imaginary",
        "question_family_id": "41_solve_quadratic_equation_pure_imaginary",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"+-{k}i",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"z^2 = -{d}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"z = \\pm \\sqrt{{-{d}}}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Final roots: z = \\pm {k}i", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_plus_minus", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": f"Isolate $z^2 = -{d}$ and recall that $\\sqrt{-1} = i$.",
            "2_concept": f"$\\sqrt{{-{d}}} = \\sqrt{{{d}}} \\cdot i = {k}i$. Don't forget the $\\pm$ sign.",
            "3_breakdown": f"$z = \\pm {k}i$.",
        },
        "misconception_tags": ["lost_plus_minus_in_square_root", "stated_no_solution_for_negative_square"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 42. Solving General Quadratic with Complex Conjugate Roots
# --------------------------------------------------------------------------- #
def arch_42_solve_quadratic_equation_complex_roots(r: random.Random) -> Dict[str, Any]:
    real_p = r.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    imag_q = r.choice([1, 2, 3, 4, 5])
    # Equation: (z - real_p)^2 + imag_q^2 = 0 => z^2 - 2*real_p*z + (real_p^2 + imag_q^2) = 0
    b_coeff = -2 * real_p
    c_coeff = real_p**2 + imag_q**2
    disc = b_coeff**2 - 4 * c_coeff  # = -4 * imag_q^2
    seed_val = r.randint(100, 99999)

    sign_b = f"- {abs(b_coeff)}" if b_coeff < 0 else f"+ {b_coeff}"
    mag_r = math.hypot(real_p, imag_q)
    ang1 = math.degrees(math.atan2(imag_q, real_p)) % 360
    ang2 = math.degrees(math.atan2(-imag_q, real_p)) % 360

    vectors = [(mag_r, ang1, f"z_1", "#2563eb"), (mag_r, ang2, f"z_2", "#dc2626")]
    diag = _make_phasor_svg(
        f"Conjugate Complex Roots of z² {sign_b}z + {c_coeff} = 0",
        vectors,
        seed=seed_val,
        max_val=mag_r * 1.3,
    )

    prompt = (
        f"Solve the quadratic equation in the complex numbers:\n"
        f"$$z^2 {sign_b}z + {c_coeff} = 0$$\n\n"
        f"Express your answers in standard rectangular form $z = a \\pm bi$."
    )

    ans_latex = rf"z = {real_p} \pm {imag_q}i"

    sol = (
        f"Step 1: Identify coefficients:\n"
        f"$$a = 1, \\quad b = {b_coeff}, \\quad c = {c_coeff}$$\n\n"
        f"Step 2: Calculate the discriminant:\n"
        f"$$\\Delta = b^2 - 4ac = ({b_coeff})^2 - 4(1)({c_coeff}) = {b_coeff**2} - {4*c_coeff} = {disc}$$\n"
        f"Since $\\Delta < 0$, the roots are complex conjugates.\n\n"
        f"Step 3: Apply the quadratic formula:\n"
        f"$$z = \\frac{{-b \\pm \\sqrt{{\\Delta}}}}{{2a}} = \\frac{{-({b_coeff}) \\pm \\sqrt{{{disc}}}}}{{2}} = \\frac{{{2*real_p} \\pm {2*imag_q}i}}{{2}} = {real_p} \\pm {imag_q}i$$"
    )

    return {
        "id": f"tech_cplx_42_{seed_val}",
        "title": "Solving Quadratic Equation with Complex Conjugate Roots",
        "subskill": "42_solve_quadratic_equation_complex_roots",
        "question_family_id": "42_solve_quadratic_equation_complex_roots",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"{real_p}+-{imag_q}i",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Quadratic formula substitution", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Discriminant calculation Delta = {disc}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Simplification sqrt({disc}) = {2*imag_q}i", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final conjugate roots: {ans_latex}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "algebraic_sign_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Use the quadratic formula $z = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$.",
            "2_concept": f"The discriminant is negative: $\\Delta = {disc}$, so $\\sqrt{{{disc}}} = {2*imag_q}i$.",
            "3_breakdown": f"$z = \\frac{{{2*real_p} \\pm {2*imag_q}i}}{{2}} = {real_p} \\pm {imag_q}i$.",
        },
        "misconception_tags": ["sign_error_in_quadratic_formula", "failed_to_extract_i_from_negative_discriminant"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 43. Solving Cubic Equation: One Real Root and Two Complex Roots
# --------------------------------------------------------------------------- #
def arch_43_solve_cubic_equation_one_real_two_complex(r: random.Random) -> Dict[str, Any]:
    real_root = r.choice([-3, -2, -1, 1, 2, 3])
    p = r.choice([-2, -1, 1, 2])
    q = r.choice([2, 3, 4])
    # (z - real_root)(z^2 - 2pz + p^2 + q^2) = 0
    # Quad factor: z^2 + b1*z + c1 where b1 = -2p, c1 = p^2 + q^2
    b1 = -2 * p
    c1 = p**2 + q**2
    # Full cubic: z^3 + (b1 - real_root)z^2 + (c1 - b1*real_root)z - real_root*c1
    a_quad = b1 - real_root
    b_quad = c1 - b1 * real_root
    c_quad = -real_root * c1
    seed_val = r.randint(100, 99999)

    sign_a = f"- {abs(a_quad)}" if a_quad < 0 else f"+ {a_quad}"
    sign_b = f"- {abs(b_quad)}" if b_quad < 0 else f"+ {b_quad}"
    sign_c = f"- {abs(c_quad)}" if c_quad < 0 else f"+ {c_quad}"

    vectors = [
        (abs(real_root), 0 if real_root > 0 else 180, f"z_1={real_root}", "#16a34a"),
        (math.hypot(p, q), math.degrees(math.atan2(q, p)) % 360, f"z_2", "#2563eb"),
        (math.hypot(p, -q), math.degrees(math.atan2(-q, p)) % 360, f"z_3", "#dc2626"),
    ]
    diag = _make_phasor_svg(
        f"Three Roots of Cubic in Complex Plane",
        vectors,
        seed=seed_val,
        max_val=max(abs(real_root), math.hypot(p, q)) * 1.3,
    )

    prompt = (
        f"Given that $z = {real_root}$ is a root of the cubic equation:\n"
        f"$$z^3 {sign_a}z^2 {sign_b}z {sign_c} = 0$$\n\n"
        f"1. Factorise the cubic expression into a linear factor and a quadratic factor.\n"
        f"2. Solve for all three roots in $\\mathbb{{C}}$ (state non-real roots in $a \\pm bi$ form)."
    )

    ans_latex = rf"z_1 = {real_root}, \quad z_{{2,3}} = {p} \pm {q}i"

    sol = (
        f"Step 1: Since $z = {real_root}$ is a root, $(z - {real_root})$ is a factor.\n\n"
        f"Step 2: By polynomial division or inspection:\n"
        f"$$z^3 {sign_a}z^2 {sign_b}z {sign_c} = (z - {real_root})(z^2 {f'- {abs(b1)}' if b1 < 0 else f'+ {b1}'}z + {c1}) = 0$$\n\n"
        f"Step 3: Solve the quadratic factor $z^2 {f'- {abs(b1)}' if b1 < 0 else f'+ {b1}'}z + {c1} = 0$:\n"
        f"$$z = \\frac{{-({b1}) \\pm \\sqrt{{({b1})^2 - 4(1)({c1})}}}}{{2}} = \\frac{{{2*p} \\pm \\sqrt{{-{4*q**2}}}}}{{2}} = {p} \\pm {q}i$$\n\n"
        f"All three roots: $z_1 = {real_root}, \\quad z_{{2,3}} = {p} \\pm {q}i$."
    )

    return {
        "id": f"tech_cplx_43_{seed_val}",
        "title": "Solving Cubic Equation with Complex Conjugate Roots",
        "subskill": "43_solve_cubic_equation_one_real_two_complex",
        "question_family_id": "43_solve_cubic_equation_one_real_two_complex",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"z1={real_root}, z2={p}+{q}i, z3={p}-{q}i",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Linear factor (z - {real_root})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Quadratic factor z^2 + {b1}z + {c1}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Quadratic formula application", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Real root z1 = {real_root}", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Complex conjugate roots z = {p} \\pm {q}i", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": f"Divide the cubic polynomial by $(z - {real_root})$ to obtain a quadratic factor.",
            "2_concept": f"Solve the quadratic factor $z^2 + {b1}z + {c1} = 0$ using the quadratic formula.",
            "3_breakdown": f"Roots: $z_1 = {real_root}$, $z_{{2,3}} = {p} \\pm {q}i$.",
        },
        "misconception_tags": ["polynomial_factorisation_error", "missed_complex_conjugate_pair"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "difficulty": "hard",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 44. AC Electrical Impedance: Pure Inductive Reactance (Z_L = jX_L)
# --------------------------------------------------------------------------- #
def arch_44_ac_impedance_pure_inductive_reactance(r: random.Random) -> Dict[str, Any]:
    freq = r.choice([50, 60])  # SA grid 50 Hz
    l_mh = r.choice([20, 50, 100, 150, 200, 250])  # in mH
    l_henry = l_mh / 1000.0
    xl_raw = 2 * math.pi * freq * l_henry
    xl_val = round(xl_raw, 1)
    seed_val = r.randint(100, 99999)

    vectors = [(xl_val, 90, f"Z_L = +j{_fmt_sa(xl_val)} Ω", "#2563eb")]
    diag = _make_phasor_svg(
        f"Pure Inductive Impedance Phasor (f = {freq} Hz, L = {l_mh} mH)",
        vectors,
        seed=seed_val,
        max_val=xl_val * 1.3,
    )

    prompt = (
        f"In an AC electrical circuit connected to a {freq}\\text{{ Hz}} supply, an inductor has an inductance "
        f"of $L = {l_mh}\\text{{ mH}}$.\n\n"
        f"1. Calculate the inductive reactance $X_L = 2\\pi f L$ in Ohms (round to 1 decimal place).\n"
        f"2. State the complex impedance $Z_L$ in rectangular form ($Z_L = jX_L$).\n"
        f"3. State the phase angle $\\theta$ between voltage and current across the inductor."
    )

    ans_latex = rf"X_L = {_fmt_sa(xl_val)}\, \Omega, \quad Z_L = j{_fmt_sa(xl_val)}\, \Omega, \quad \theta = +90^\circ"

    sol = (
        f"Step 1: Inductive reactance formula:\n"
        f"$$X_L = 2\\pi f L = 2\\pi ({freq})({l_henry}) = {_fmt_sa(xl_val)}\\,\\Omega$$\n\n"
        f"Step 2: Complex impedance in rectangular form:\n"
        f"An ideal inductor has zero real resistance ($R = 0$) and a positive imaginary reactance $+jX_L$:\n"
        f"$$Z_L = 0 + jX_L = j{_fmt_sa(xl_val)}\\,\\Omega$$\n\n"
        f"Step 3: Phase relationship:\n"
        f"The voltage across an inductor leads the current by $90^\\circ$, giving a phase angle $\\theta = +90^\\circ$."
    )

    return {
        "id": f"tech_cplx_44_{seed_val}",
        "title": "AC Impedance of Pure Inductor",
        "subskill": "44_ac_impedance_pure_inductive_reactance",
        "question_family_id": "44_ac_impedance_pure_inductive_reactance",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"XL={_fmt_sa(xl_val)}, ZL=j{_fmt_sa(xl_val)}, theta=90",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Formula X_L = 2*pi*f*L substitution", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Accurate X_L value: {_fmt_sa(xl_val)} Ohms", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Rectangular impedance Z_L = j{_fmt_sa(xl_val)} Ohms", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Phase angle theta = +90 deg", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_imaginary_unit_j", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": f"Convert $L = {l_mh}\\text{{ mH}}$ to Henrys ($L = {l_henry}\\text{{ H}}$) before substituting into $X_L = 2\\pi f L$.",
            "2_concept": "Inductive impedance is purely imaginary and positive: $Z_L = jX_L$ with phase angle $+90^\\circ$.",
            "3_breakdown": f"$X_L = {_fmt_sa(xl_val)}\\,\\Omega \\implies Z_L = j{_fmt_sa(xl_val)}\\,\\Omega$.",
        },
        "misconception_tags": ["forgot_to_convert_millihenry_to_henry", "negative_phase_angle_for_inductor"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers in AC Circuits",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 45. AC Electrical Impedance: Pure Capacitive Reactance (Z_C = -jX_C)
# --------------------------------------------------------------------------- #
def arch_45_ac_impedance_pure_capacitive_reactance(r: random.Random) -> Dict[str, Any]:
    freq = r.choice([50, 60])
    c_uf = r.choice([20, 30, 40, 50, 80, 100])  # in uF
    c_farad = c_uf * 1e-6
    xc_raw = 1.0 / (2 * math.pi * freq * c_farad)
    xc_val = round(xc_raw, 1)
    seed_val = r.randint(100, 99999)

    vectors = [(xc_val, 270, f"Z_C = -j{_fmt_sa(xc_val)} Ω", "#dc2626")]
    diag = _make_phasor_svg(
        f"Pure Capacitive Impedance Phasor (f = {freq} Hz, C = {c_uf} µF)",
        vectors,
        seed=seed_val,
        max_val=xc_val * 1.3,
    )

    prompt = (
        f"A capacitor with capacitance $C = {c_uf}\\,\\mu\\text{{F}}$ is connected to a {freq}\\text{{ Hz}} AC power supply.\n\n"
        f"1. Calculate the capacitive reactance $X_C = \\frac{{1}}{{2\\pi f C}}$ in Ohms (round to 1 decimal place).\n"
        f"2. State the complex impedance $Z_C$ in rectangular form ($Z_C = -jX_C$).\n"
        f"3. State the phase angle $\\theta$ between voltage and current across the capacitor."
    )

    ans_latex = rf"X_C = {_fmt_sa(xc_val)}\, \Omega, \quad Z_C = -j{_fmt_sa(xc_val)}\, \Omega, \quad \theta = -90^\circ"

    sol = (
        f"Step 1: Capacitive reactance formula:\n"
        f"$$X_C = \\frac{{1}}{{2\\pi f C}} = \\frac{{1}}{{2\\pi ({freq})({c_uf} \\times 10^{{-6}})}} = {_fmt_sa(xc_val)}\\,\\Omega$$\n\n"
        f"Step 2: Complex impedance in rectangular form:\n"
        f"A capacitor produces negative imaginary reactance $-jX_C$:\n"
        f"$$Z_C = 0 - jX_C = -j{_fmt_sa(xc_val)}\\,\\Omega$$\n\n"
        f"Step 3: Phase relationship:\n"
        f"Voltage lags current by $90^\\circ$ across a capacitor, giving a phase angle $\\theta = -90^\\circ$."
    )

    return {
        "id": f"tech_cplx_45_{seed_val}",
        "title": "AC Impedance of Pure Capacitor",
        "subskill": "45_ac_impedance_pure_capacitive_reactance",
        "question_family_id": "45_ac_impedance_pure_capacitive_reactance",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"XC={_fmt_sa(xc_val)}, ZC=-j{_fmt_sa(xc_val)}, theta=-90",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Formula X_C = 1 / (2*pi*f*C) substitution", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Accurate X_C value: {_fmt_sa(xc_val)} Ohms", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Rectangular impedance Z_C = -j{_fmt_sa(xc_val)} Ohms", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Phase angle theta = -90 deg", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "positive_sign_for_capacitive_reactance", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": f"Convert $C = {c_uf}\\,\\mu\\text{{F}}$ to Farads ($C = {c_uf} \\times 10^{{-6}}\\text{{ F}}$).",
            "2_concept": "Capacitive impedance has a negative imaginary operator: $Z_C = -jX_C$ and phase angle $-90^\\circ$.",
            "3_breakdown": f"$X_C = {_fmt_sa(xc_val)}\\,\\Omega \\implies Z_C = -j{_fmt_sa(xc_val)}\\,\\Omega$.",
        },
        "misconception_tags": ["forgot_micro_conversion_factor", "positive_phase_for_capacitor"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers in AC Circuits",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 46. Series RL Circuit: Total Impedance Z = R + jX_L
# --------------------------------------------------------------------------- #
def arch_46_ac_impedance_series_rl_circuit(r: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)]
    r_base, xl_base, z_base = r.choice(triples)
    scale = r.choice([2, 5, 10])
    r_val = r_base * scale
    xl_val = xl_base * scale
    z_mag = z_base * scale

    phi_deg = round(math.degrees(math.atan(xl_val / r_val)), 1)
    seed_val = r.randint(100, 99999)

    vectors = [
        (r_val, 0, f"R = {r_val} Ω", "#16a34a"),
        (xl_val, 90, f"X_L = {xl_val} Ω", "#2563eb"),
        (z_mag, phi_deg, f"|Z| = {z_mag} Ω", "#dc2626"),
    ]
    diag = _make_phasor_svg(
        f"Series RL Circuit Impedance Triangle (R = {r_val} Ω, XL = {xl_val} Ω)",
        vectors,
        seed=seed_val,
        max_val=z_mag * 1.25,
    )

    prompt = (
        f"A series RL circuit consists of a resistor $R = {r_val}\\,\\Omega$ and an inductor with "
        f"inductive reactance $X_L = {xl_val}\\,\\Omega$.\n\n"
        f"1. Express the total impedance $Z$ in rectangular form ($R + jX_L$).\n"
        f"2. Calculate the total impedance magnitude $|Z| = \\sqrt{{R^2 + X_L^2}}$.\n"
        f"3. Calculate the circuit phase angle $\\phi = \\tan^{{-1}}\\left(\\frac{{X_L}}{{R}}\\right)$ in degrees (1 decimal place).\n"
        f"4. State the impedance in polar form $Z = |Z|\\operatorname{{cis}}\\phi$."
    )

    ans_latex = (
        rf"Z = {r_val} + j{xl_val}\, \Omega, \quad |Z| = {z_mag}\, \Omega, \quad "
        rf"\phi = {_fmt_sa(phi_deg)}^\circ, \quad Z = {z_mag}\operatorname{{cis}}({_fmt_sa(phi_deg)}^\circ)\, \Omega"
    )

    sol = (
        f"Step 1: Total impedance in rectangular form:\n"
        f"$$Z = R + jX_L = {r_val} + j{xl_val}\\,\\Omega$$\n\n"
        f"Step 2: Impedance magnitude via Pythagoras:\n"
        f"$$|Z| = \\sqrt{{R^2 + X_L^2}} = \\sqrt{{{r_val}^2 + {xl_val}^2}} = \\sqrt{{{r_val**2 + xl_val**2}}} = {z_mag}\\,\\Omega$$\n\n"
        f"Step 3: Phase angle calculation:\n"
        f"$$\\phi = \\tan^{{-1}}\\left(\\frac{{X_L}}{{R}}\\right) = \\tan^{{-1}}\\left(\\frac{{{xl_val}}}{{{r_val}}}\\right) = {_fmt_sa(phi_deg)}^\\circ$$\n\n"
        f"Step 4: Polar form representation:\n"
        f"$$Z = |Z|\\operatorname{{cis}}\\phi = {z_mag}\\operatorname{{cis}}({_fmt_sa(phi_deg)}^\\circ)\\,\\Omega$$"
    )

    return {
        "id": f"tech_cplx_46_{seed_val}",
        "title": "Series RL Circuit Complex Impedance",
        "subskill": "46_ac_impedance_series_rl_circuit",
        "question_family_id": "46_ac_impedance_series_rl_circuit",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"Z={r_val}+j{xl_val}, |Z|={z_mag}, phi={_fmt_sa(phi_deg)}",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Rectangular form Z = {r_val} + j{xl_val} Ohms", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Magnitude formula |Z| = sqrt(R^2 + X_L^2)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Magnitude |Z| = {z_mag} Ohms", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Phase angle phi = {_fmt_sa(phi_deg)} deg", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Polar form Z = {z_mag} cis({_fmt_sa(phi_deg)} deg)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "In a series RL circuit, $Z = R + jX_L$. The real axis is $R$ and the positive imaginary axis is $X_L$.",
            "2_concept": "$|Z| = \\sqrt{R^2 + X_L^2}$ and $\\phi = \\tan^{-1}(X_L / R)$.",
            "3_breakdown": f"$|Z| = {z_mag}\\,\\Omega$ and $\\phi = {_fmt_sa(phi_deg)}^\\circ$.",
        },
        "misconception_tags": ["added_r_and_xl_directly_scalar", "inverted_tangent_ratio_for_phase"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers in AC Circuits",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 47. Series RC Circuit: Total Impedance Z = R - jX_C
# --------------------------------------------------------------------------- #
def arch_47_ac_impedance_series_rc_circuit(r: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)]
    r_base, xc_base, z_base = r.choice(triples)
    scale = r.choice([2, 5, 10])
    r_val = r_base * scale
    xc_val = xc_base * scale
    z_mag = z_base * scale

    phi_deg = round(-math.degrees(math.atan(xc_val / r_val)), 1)
    seed_val = r.randint(100, 99999)

    vectors = [
        (r_val, 0, f"R = {r_val} Ω", "#16a34a"),
        (xc_val, 270, f"X_C = {xc_val} Ω", "#dc2626"),
        (z_mag, phi_deg % 360, f"|Z| = {z_mag} Ω", "#9333ea"),
    ]
    diag = _make_phasor_svg(
        f"Series RC Circuit Impedance Triangle (R = {r_val} Ω, XC = {xc_val} Ω)",
        vectors,
        seed=seed_val,
        max_val=z_mag * 1.25,
    )

    prompt = (
        f"A series RC circuit consists of a resistor $R = {r_val}\\,\\Omega$ and a capacitor with "
        f"capacitive reactance $X_C = {xc_val}\\,\\Omega$.\n\n"
        f"1. Express the total impedance $Z$ in rectangular form ($R - jX_C$).\n"
        f"2. Calculate the impedance magnitude $|Z| = \\sqrt{{R^2 + X_C^2}}$.\n"
        f"3. Calculate the circuit phase angle $\\phi = -\\tan^{{-1}}\\left(\\frac{{X_C}}{{R}}\\right)$ in degrees (1 decimal place).\n"
        f"4. State the impedance in polar form $Z = |Z|\\operatorname{{cis}}\\phi$."
    )

    ans_latex = (
        rf"Z = {r_val} - j{xc_val}\, \Omega, \quad |Z| = {z_mag}\, \Omega, \quad "
        rf"\phi = {_fmt_sa(phi_deg)}^\circ, \quad Z = {z_mag}\operatorname{{cis}}({_fmt_sa(phi_deg)}^\circ)\, \Omega"
    )

    sol = (
        f"Step 1: Total impedance in rectangular form:\n"
        f"$$Z = R - jX_C = {r_val} - j{xc_val}\\,\\Omega$$\n\n"
        f"Step 2: Impedance magnitude:\n"
        f"$$|Z| = \\sqrt{{R^2 + (-X_C)^2}} = \\sqrt{{{r_val}^2 + {xc_val}^2}} = {z_mag}\\,\\Omega$$\n\n"
        f"Step 3: Phase angle calculation:\n"
        f"$$\\phi = -\\tan^{{-1}}\\left(\\frac{{X_C}}{{R}}\\right) = -\\tan^{{-1}}\\left(\\frac{{{xc_val}}}{{{r_val}}}\\right) = {_fmt_sa(phi_deg)}^\\circ$$\n"
        f"The phase angle is negative because capacitive current leads voltage.\n\n"
        f"Step 4: Polar form representation:\n"
        f"$$Z = {z_mag}\\operatorname{{cis}}({_fmt_sa(phi_deg)}^\\circ)\\,\\Omega$$"
    )

    return {
        "id": f"tech_cplx_47_{seed_val}",
        "title": "Series RC Circuit Complex Impedance",
        "subskill": "47_ac_impedance_series_rc_circuit",
        "question_family_id": "47_ac_impedance_series_rc_circuit",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"Z={r_val}-j{xc_val}, |Z|={z_mag}, phi={_fmt_sa(phi_deg)}",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Rectangular form Z = {r_val} - j{xc_val} Ohms", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Magnitude formula |Z| = sqrt(R^2 + X_C^2)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Magnitude |Z| = {z_mag} Ohms", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Negative phase angle phi = {_fmt_sa(phi_deg)} deg", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Polar form Z = {z_mag} cis({_fmt_sa(phi_deg)} deg)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_negative_sign_in_rc_reactance", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "In a series RC circuit, the capacitive reactance is subtracted on the imaginary axis: $Z = R - jX_C$.",
            "2_concept": "The phase angle is in Quadrant 4 (negative): $\\phi = -\\tan^{-1}(X_C / R)$.",
            "3_breakdown": f"$Z = {r_val} - j{xc_val}\\,\\Omega$, $|Z| = {z_mag}\\,\\Omega$, $\\phi = {_fmt_sa(phi_deg)}^\\circ$.",
        },
        "misconception_tags": ["used_positive_sign_for_capacitive_impedance", "scalar_addition_of_r_and_xc"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers in AC Circuits",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 48. Series RLC Circuit: Net Reactance, Impedance & Resonance
# --------------------------------------------------------------------------- #
def arch_48_ac_impedance_series_rlc_circuit(r: random.Random) -> Dict[str, Any]:
    r_val = r.choice([20, 30, 40, 50])
    is_inductive = r.choice([True, False])

    if is_inductive:
        x_net = r.choice([15, 20, 25, 30, 40])
        xc_val = r.choice([20, 30, 40])
        xl_val = xc_val + x_net
    else:
        x_net = -r.choice([15, 20, 25, 30, 40])
        xl_val = r.choice([20, 30, 40])
        xc_val = xl_val - x_net

    z_mag = round(math.hypot(r_val, x_net), 1)
    phi_deg = round(math.degrees(math.atan2(x_net, r_val)), 1)
    seed_val = r.randint(100, 99999)

    vectors = [
        (r_val, 0, f"R = {r_val} Ω", "#16a34a"),
        (abs(x_net), 90 if x_net > 0 else 270, f"X_net = {x_net} Ω", "#2563eb" if x_net > 0 else "#dc2626"),
        (z_mag, phi_deg % 360, f"|Z| = {_fmt_sa(z_mag)} Ω", "#9333ea"),
    ]
    diag = _make_phasor_svg(
        f"Series RLC Circuit Phasor (R = {r_val} Ω, XL = {xl_val} Ω, XC = {xc_val} Ω)",
        vectors,
        seed=seed_val,
        max_val=max(z_mag, abs(x_net), r_val) * 1.25,
    )

    prompt = (
        f"A series RLC circuit has a resistance $R = {r_val}\\,\\Omega$, an inductive reactance "
        f"$X_L = {xl_val}\\,\\Omega$, and a capacitive reactance $X_C = {xc_val}\\,\\Omega$.\n\n"
        f"1. Calculate the net reactance $X = X_L - X_C$.\n"
        f"2. Write the total complex impedance $Z$ in rectangular form ($R + j(X_L - X_C)$).\n"
        f"3. Calculate the total impedance magnitude $|Z|$.\n"
        f"4. Calculate the circuit phase angle $\\phi$ in degrees (1 decimal place) and state whether the circuit is predominantly inductive or capacitive."
    )

    nature = "inductive (current lags voltage)" if x_net > 0 else "capacitive (current leads voltage)"
    sign_net = f"+ j{x_net}" if x_net > 0 else f"- j{abs(x_net)}"
    ans_latex = (
        rf"X = {x_net}\, \Omega, \quad Z = {r_val} {sign_net}\, \Omega, \quad "
        rf"|Z| = {_fmt_sa(z_mag)}\, \Omega, \quad \phi = {_fmt_sa(phi_deg)}^\circ \text{{ ({nature})}}"
    )

    sol = (
        f"Step 1: Net reactance:\n"
        f"$$X = X_L - X_C = {xl_val} - {xc_val} = {x_net}\\,\\Omega$$\n\n"
        f"Step 2: Total impedance in rectangular form:\n"
        f"$$Z = R + jX = {r_val} {sign_net}\\,\\Omega$$\n\n"
        f"Step 3: Impedance magnitude:\n"
        f"$$|Z| = \\sqrt{{R^2 + X^2}} = \\sqrt{{{r_val}^2 + ({x_net})^2}} = {_fmt_sa(z_mag)}\\,\\Omega$$\n\n"
        f"Step 4: Phase angle:\n"
        f"$$\\phi = \\tan^{{-1}}\\left(\\frac{{{x_net}}}{{{r_val}}}\\right) = {_fmt_sa(phi_deg)}^\\circ$$\n"
        f"Since $X = {x_net}\\,\\Omega$ is {'positive' if x_net > 0 else 'negative'}, the circuit is **{nature}**."
    )

    return {
        "id": f"tech_cplx_48_{seed_val}",
        "title": "Series RLC Circuit Impedance and Circuit Nature",
        "subskill": "48_ac_impedance_series_rlc_circuit",
        "question_family_id": "48_ac_impedance_series_rlc_circuit",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"X={x_net}, Z={r_val}{sign_net}, |Z|={_fmt_sa(z_mag)}, phi={_fmt_sa(phi_deg)}",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Net reactance X = X_L - X_C = {x_net} Ohms", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Rectangular form Z = {r_val} {sign_net} Ohms", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Magnitude |Z| = {_fmt_sa(z_mag)} Ohms", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Phase angle phi = {_fmt_sa(phi_deg)} deg", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Circuit nature: {nature}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Subtract $X_C$ from $X_L$ to find the net imaginary reactance $X = X_L - X_C$.",
            "2_concept": "Total impedance is $Z = R + j(X_L - X_C)$. If $X > 0$ it is inductive; if $X < 0$ it is capacitive.",
            "3_breakdown": f"$X = {x_net}\\,\\Omega \\implies |Z| = {_fmt_sa(z_mag)}\\,\\Omega$ and $\\phi = {_fmt_sa(phi_deg)}^\\circ$.",
        },
        "misconception_tags": ["added_reactances_instead_of_subtracting", "confused_inductive_and_capacitive_circuit_nature"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers in AC Circuits",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 49. AC Circuit Ohm's Law in Phasor Form: V = I * Z
# --------------------------------------------------------------------------- #
def arch_49_ac_circuit_ohms_law_voltage_current(r: random.Random) -> Dict[str, Any]:
    i_mag = r.choice([2, 3, 4, 5, 8, 10])  # Current in A
    theta_i = r.choice([0, 15, 30, 45])
    z_mag = r.choice([10, 12, 15, 20, 25, 40])
    phi_z = r.choice([30, 45, 60])

    v_mag = i_mag * z_mag
    theta_v = (theta_i + phi_z) % 360
    seed_val = r.randint(100, 99999)

    vectors = [
        (i_mag * 10, theta_i, f"I = {i_mag} A (scaled)", "#16a34a"),
        (v_mag, theta_v, f"V = {v_mag} V", "#dc2626"),
    ]
    diag = _make_phasor_svg(
        f"Phasor Ohm's Law: V = I · Z (|V| = {v_mag} V, θ_V = {theta_v}°)",
        vectors,
        seed=seed_val,
        max_val=v_mag * 1.25,
    )

    prompt = (
        f"In an AC electrical circuit, the current phasor is $I = {i_mag}\\operatorname{{cis}}({theta_i}^\\circ)\\text{{ A}}$, "
        f"and the circuit impedance is $Z = {z_mag}\\operatorname{{cis}}({phi_z}^\\circ)\\,\\Omega$.\n\n"
        f"1. Apply Ohm's Law in polar form ($V = I \\cdot Z$) to determine the supply voltage phasor $V$.\n"
        f"2. State the magnitude of the supply voltage $|V|$.\n"
        f"3. State the phase angle $\\theta_V$ of the voltage in degrees."
    )

    ans_latex = rf"V = {v_mag}\operatorname{{cis}}({theta_v}^\circ)\text{{ V}}, \quad |V| = {v_mag}\text{{ V}}, \quad \theta_V = {theta_v}^\circ"

    sol = (
        f"Step 1: Ohm's Law in polar form:\n"
        f"$$V = I \\cdot Z = [r_1 \\operatorname{{cis}}(\\theta_1)] \\cdot [r_2 \\operatorname{{cis}}(\\theta_2)] = (r_1 r_2) \\operatorname{{cis}}(\\theta_1 + \\theta_2)$$\n\n"
        f"Step 2: Multiply the moduli:\n"
        f"$$|V| = |I| \\cdot |Z| = ({i_mag})({z_mag}) = {v_mag}\\text{{ V}}$$\n\n"
        f"Step 3: Add the phase angles:\n"
        f"$$\\theta_V = \\theta_I + \\phi_Z = {theta_i}^\\circ + {phi_z}^\\circ = {theta_v}^\\circ$$\n\n"
        f"Final voltage phasor:\n"
        f"$$V = {v_mag}\\operatorname{{cis}}({theta_v}^\\circ)\\text{{ V}}$$"
    )

    return {
        "id": f"tech_cplx_49_{seed_val}",
        "title": "AC Ohm's Law in Polar Phasor Form",
        "subskill": "49_ac_circuit_ohms_law_voltage_current",
        "question_family_id": "49_ac_circuit_ohms_law_voltage_current",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"V={v_mag}cis({theta_v}), |V|={v_mag}, theta_V={theta_v}",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Polar multiplication formula V = I * Z", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Voltage magnitude |V| = {v_mag} V", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Voltage phase angle theta_V = {theta_v} deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final phasor V = {v_mag} cis({theta_v} deg) V", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "In polar form, multiply the magnitudes ($|V| = |I| \\times |Z|$) and add the phase angles ($\\theta_V = \\theta_I + \\phi$).",
            "2_concept": "$V = ({i_mag} \\times {z_mag})\\operatorname{cis}({theta_i}^\\circ + {phi_z}^\\circ)$.",
            "3_breakdown": f"$V = {v_mag}\\operatorname{{cis}}({theta_v}^\\circ)\\text{{ V}}$.",
        },
        "misconception_tags": ["multiplied_angles_instead_of_adding", "divided_voltage_by_impedance_for_v"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers in AC Circuits",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# --------------------------------------------------------------------------- #
# 50. Capstone Technical Complex AC Synthesis & Misconception Repair (7 Marks)
# --------------------------------------------------------------------------- #
def arch_50_technical_complex_ac_synthesis_capstone(r: random.Random) -> Dict[str, Any]:
    freq = 50  # SA standard grid frequency 50 Hz
    v_rms = r.choice([220, 230, 240])  # Mains voltage
    r_val = r.choice([15, 20, 24, 30])
    l_mh = r.choice([100, 150, 200])  # in mH
    c_uf = r.choice([50, 80, 100])  # in uF

    # Calculations
    xl_raw = 2 * math.pi * freq * (l_mh * 1e-3)
    xc_raw = 1.0 / (2 * math.pi * freq * (c_uf * 1e-6))
    xl = round(xl_raw, 1)
    xc = round(xc_raw, 1)
    x_net = round(xl - xc, 1)

    z_mag = round(math.hypot(r_val, x_net), 1)
    phi_deg = round(math.degrees(math.atan2(x_net, r_val)), 1)
    i_mag = round(v_rms / z_mag, 2)
    power_factor = round(math.cos(math.radians(phi_deg)), 3)
    seed_val = r.randint(100, 99999)

    vectors = [
        (r_val, 0, f"R = {r_val} Ω", "#16a34a"),
        (abs(x_net), 90 if x_net > 0 else 270, f"X = {_fmt_sa(x_net)} Ω", "#2563eb" if x_net > 0 else "#dc2626"),
        (z_mag, phi_deg % 360, f"|Z| = {_fmt_sa(z_mag)} Ω", "#9333ea"),
    ]
    diag = _make_phasor_svg(
        f"RLC Circuit Synthesis: R = {r_val} Ω, L = {l_mh} mH, C = {c_uf} µF (f = 50 Hz)",
        vectors,
        seed=seed_val,
        max_val=max(z_mag, r_val, abs(x_net)) * 1.3,
    )

    prompt = (
        f"A series RLC circuit is connected to an AC supply of $V = {v_rms}\\text{{ V}}$ at $f = 50\\text{{ Hz}}$.\n"
        f"The circuit components are $R = {r_val}\\,\\Omega$, $L = {l_mh}\\text{{ mH}}$, and $C = {c_uf}\\,\\mu\\text{{F}}$.\n\n"
        f"Determine, with full technical steps:\n"
        f"1. The inductive reactance $X_L$ and capacitive reactance $X_C$ (round to 1 decimal place).\n"
        f"2. The total complex impedance $Z = R + j(X_L - X_C)$ in rectangular form.\n"
        f"3. The total impedance magnitude $|Z|$ and phase angle $\\phi$ in polar form ($|Z|\\operatorname{{cis}}\\phi$).\n"
        f"4. The RMS current drawn by the circuit: $I = \\frac{{V}}{{|Z|}}$ (round to 2 decimal places).\n"
        f"5. The circuit power factor: $\\text{{PF}} = \\cos\\phi$."
    )

    sign_x = f"+ j{_fmt_sa(x_net)}" if x_net >= 0 else f"- j{_fmt_sa(abs(x_net))}"
    ans_latex = (
        rf"X_L = {_fmt_sa(xl)}\, \Omega, \; X_C = {_fmt_sa(xc)}\, \Omega, \quad "
        rf"Z = {_fmt_sa(z_mag)}\operatorname{{cis}}({_fmt_sa(phi_deg)}^\circ)\, \Omega, \quad "
        rf"I = {_fmt_sa(i_mag)}\text{{ A}}, \quad \text{{PF}} = {_fmt_sa(power_factor, 3)}"
    )

    sol = (
        f"Step 1: Calculate reactances:\n"
        f"$$X_L = 2\\pi f L = 2\\pi(50)({l_mh}\\times 10^{{-3}}) = {_fmt_sa(xl)}\\,\\Omega$$\n"
        f"$$X_C = \\frac{{1}}{{2\\pi f C}} = \\frac{{1}}{{2\\pi(50)({c_uf}\\times 10^{{-6}})}} = {_fmt_sa(xc)}\\,\\Omega$$\n"
        f"Net reactance: $X = X_L - X_C = {_fmt_sa(xl)} - {_fmt_sa(xc)} = {_fmt_sa(x_net)}\\,\\Omega$.\n\n"
        f"Step 2: Total impedance in rectangular form:\n"
        f"$$Z = R + jX = {r_val} {sign_x}\\,\\Omega$$\n\n"
        f"Step 3: Total impedance in polar form:\n"
        f"$$|Z| = \\sqrt{{{r_val}^2 + ({_fmt_sa(x_net)})^2}} = {_fmt_sa(z_mag)}\\,\\Omega$$\n"
        f"$$\\phi = \\tan^{{-1}}\\left(\\frac{{{_fmt_sa(x_net)}}}{{{r_val}}}\\right) = {_fmt_sa(phi_deg)}^\\circ$$\n"
        f"$$Z = {_fmt_sa(z_mag)}\\operatorname{{cis}}({_fmt_sa(phi_deg)}^\\circ)\\,\\Omega$$\n\n"
        f"Step 4: Circuit RMS current:\n"
        f"$$I = \\frac{{V}}{{|Z|}} = \\frac{{{v_rms}}}{{{_fmt_sa(z_mag)}}} = {_fmt_sa(i_mag)}\\text{{ A}}$$\n\n"
        f"Step 5: Power factor:\n"
        f"$$\\text{{PF}} = \\cos\\phi = \\cos({_fmt_sa(phi_deg)}^\\circ) = {_fmt_sa(power_factor, 3)}$$"
    )

    return {
        "id": f"tech_cplx_50_{seed_val}",
        "title": "Comprehensive Technical AC Circuit Synthesis",
        "subskill": "50_technical_complex_ac_synthesis_capstone",
        "question_family_id": "50_technical_complex_ac_synthesis_capstone",
        "question_type": "math_short",
        "prompt": prompt,
        "expected_answer": f"XL={_fmt_sa(xl)}, XC={_fmt_sa(xc)}, |Z|={_fmt_sa(z_mag)}, phi={_fmt_sa(phi_deg)}, I={_fmt_sa(i_mag)}, PF={_fmt_sa(power_factor, 3)}",
        "sample_answer": ans_latex,
        "answer_latex": ans_latex,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct XL = {_fmt_sa(xl)} Ohms", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct XC = {_fmt_sa(xc)} Ohms", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Impedance rectangular Z = {r_val} {sign_x} Ohms", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Impedance magnitude |Z| = {_fmt_sa(z_mag)} Ohms", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Phase angle phi = {_fmt_sa(phi_deg)} deg", "marks": 1, "editable": True},
                {"id": "mp6", "desc": f"Current I = {_fmt_sa(i_mag)} A", "marks": 1, "editable": True},
                {"id": "mp7", "desc": f"Power factor PF = cos(phi) = {_fmt_sa(power_factor, 3)}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_power_factor", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": f"Calculate $X_L = 2\\pi(50)L$ and $X_C = \\frac{{1}}{{2\\pi(50)C}}$, then find $X = X_L - X_C$.",
            "2_concept": "$|Z| = \\sqrt{R^2 + X^2}$, $I = V / |Z|$, and $\\text{PF} = \\cos\\phi$.",
            "3_breakdown": f"$X_L = {_fmt_sa(xl)}\\,\\Omega$, $X_C = {_fmt_sa(xc)}\\,\\Omega$, $|Z| = {_fmt_sa(z_mag)}\\,\\Omega$, $I = {_fmt_sa(i_mag)}\\text{{ A}}$, $\\text{{PF}} = {_fmt_sa(power_factor, 3)}$.",
        },
        "misconception_tags": ["added_reactances_without_subtraction", "unit_conversion_error_milli_micro"],
        "curriculum_reference": "Technical Mathematics Grade 12 Term 1 > Complex Numbers in AC Circuits",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "difficulty": "hard",
        "diagram_spec": diag,
        "modality": "diagram",
    }


# ==============================================================================
# Subskills Dictionary and Builders Mapping for 39 - 50
# ==============================================================================

BUILDERS_39_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "39_complex_fourth_roots_de_moivre": arch_39_complex_fourth_roots_de_moivre,
    "40_roots_of_unity_polygon": arch_40_roots_of_unity_polygon,
    "41_solve_quadratic_equation_pure_imaginary": arch_41_solve_quadratic_equation_pure_imaginary,
    "42_solve_quadratic_equation_complex_roots": arch_42_solve_quadratic_equation_complex_roots,
    "43_solve_cubic_equation_one_real_two_complex": arch_43_solve_cubic_equation_one_real_two_complex,
    "44_ac_impedance_pure_inductive_reactance": arch_44_ac_impedance_pure_inductive_reactance,
    "45_ac_impedance_pure_capacitive_reactance": arch_45_ac_impedance_pure_capacitive_reactance,
    "46_ac_impedance_series_rl_circuit": arch_46_ac_impedance_series_rl_circuit,
    "47_ac_impedance_series_rc_circuit": arch_47_ac_impedance_series_rc_circuit,
    "48_ac_impedance_series_rlc_circuit": arch_48_ac_impedance_series_rlc_circuit,
    "49_ac_circuit_ohms_law_voltage_current": arch_49_ac_circuit_ohms_law_voltage_current,
    "50_technical_complex_ac_synthesis_capstone": arch_50_technical_complex_ac_synthesis_capstone,
}

SUBSKILLS_39_50: Dict[str, str] = {
    "39_complex_fourth_roots_de_moivre": "Complex Fourth Roots via de Moivre's Theorem",
    "40_roots_of_unity_polygon": "Roots of Unity and Regular Polygon Geometry",
    "41_solve_quadratic_equation_pure_imaginary": "Solving Pure Imaginary Quadratic Equations",
    "42_solve_quadratic_equation_complex_roots": "Solving Quadratic Equations with Complex Conjugate Roots",
    "43_solve_cubic_equation_one_real_two_complex": "Solving Cubic Equations with Complex Conjugate Roots",
    "44_ac_impedance_pure_inductive_reactance": "AC Electrical Impedance of Pure Inductor",
    "45_ac_impedance_pure_capacitive_reactance": "AC Electrical Impedance of Pure Capacitor",
    "46_ac_impedance_series_rl_circuit": "Complex Impedance and Phasor of Series RL Circuit",
    "47_ac_impedance_series_rc_circuit": "Complex Impedance and Phasor of Series RC Circuit",
    "48_ac_impedance_series_rlc_circuit": "Complex Impedance and Phase Angle of Series RLC Circuit",
    "49_ac_circuit_ohms_law_voltage_current": "AC Ohm's Law in Polar Phasor Form",
    "50_technical_complex_ac_synthesis_capstone": "Capstone Technical AC Circuit Synthesis Problem",
}
