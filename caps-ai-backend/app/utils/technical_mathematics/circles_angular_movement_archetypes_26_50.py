"""Grade 10–12 Technical Mathematics — Circles, Angles & Angular Movement (Archetypes 26 to 50).
Aligned with South African National Curriculum Standards.
Reference:
- curriculum_docs_auto/TechnicalMathematics_Gr10/Term 3/01. Circles  angles and angular Movement.md
- curriculum_docs_auto/TechnicalMathematics_Gr11/Term 3/01. Circles angles and angular movement.md

Covers:
- Rotational frequency conversions (rpm to r/s, r/s to rad/s, angular velocity omega = 2*pi*n, theta = omega*t) (26..30)
- Circumferential / linear velocity (v = pi*D*n = omega*r, saw blades, clock hands, centripetal accel) (31..35)
- Belt and pulley drives (v1 = v2 => omega1*r1 = omega2*r2, stepped cones, crossed belts) (36..40)
- Meshed gears and gear trains (N1*T1 = N2*T2, compound trains, rack & pinion) (41..44)
- Winch drum cable winding, vehicle road wheel travel velocity, conveyor rollers (45..48)
- Technical engineering transmission synthesis & diagnostic autopsy (49..50)
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple


def _fmt(val: float, decimals: int = 2) -> str:
    """Format float using South African comma decimal convention."""
    rounded = round(val, decimals)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _svg_rotating_wheel(diameter_m: float, rpm: int, show_tangent: bool = True) -> str:
    """Dynamic SVG of a rotating circular wheel / blade with radius, rotation sense, and tangential velocity."""
    r_val = _fmt(diameter_m / 2.0, 2)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%" style="max-width:360px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="180" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Rotating Wheel ({rpm} r/min)</text>'
        f'<circle cx="160" cy="135" r="75" fill="#f8fafc" stroke="#2563eb" stroke-width="2.5"/>'
        f'<circle cx="160" cy="135" r="4.5" fill="#1e3a8a"/>'
        f'<line x1="160" y1="135" x2="235" y2="135" stroke="#1d4ed8" stroke-width="2" stroke-dasharray="4,3"/>'
        f'<text x="195" y="128" font-size="10" font-weight="bold" fill="#1d4ed8">r = {r_val} m</text>'
        f'<path d="M 160 85 A 50 50 0 0 1 210 135" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrow)"/>'
        f'<text x="195" y="95" font-size="11" font-weight="bold" fill="#c2410c">ω</text>'
        + (
            f'<line x1="235" y1="135" x2="235" y2="65" stroke="#dc2626" stroke-width="2.5"/>'
            f'<polygon points="235,58 230,70 240,70" fill="#dc2626"/>'
            f'<text x="242" y="75" font-size="11" font-weight="bold" fill="#dc2626">v = ωr</text>'
            if show_tangent else ""
        ) +
        f'<text x="160" y="152" text-anchor="middle" font-size="10" fill="#475569">O (Center)</text>'
        f'</svg>'
    )


def _svg_belt_pulley_drive(d1: float, d2: float, crossed: bool = False) -> str:
    """Dynamic SVG of two belt-connected pulleys with pitch diameters d1 and d2."""
    r1_px = max(24, min(50, int(d1 * 40)))
    r2_px = max(20, min(55, int(d2 * 40)))
    c1_x, c1_y = 90, 130
    c2_x, c2_y = 265, 130

    belt_path = (
        f'<line x1="{c1_x}" y1="{c1_y - r1_px}" x2="{c2_x}" y2="{c2_y + r2_px}" stroke="#334155" stroke-width="2.5"/>'
        f'<line x1="{c1_x}" y1="{c1_y + r1_px}" x2="{c2_x}" y2="{c2_y - r2_px}" stroke="#334155" stroke-width="2.5"/>'
        if crossed else
        f'<line x1="{c1_x}" y1="{c1_y - r1_px}" x2="{c2_x}" y2="{c2_y - r2_px}" stroke="#334155" stroke-width="2.5"/>'
        f'<line x1="{c1_x}" y1="{c1_y + r1_px}" x2="{c2_x}" y2="{c2_y + r2_px}" stroke="#334155" stroke-width="2.5"/>'
    )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%" style="max-width:360px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="180" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Belt and Pulley Drive</text>'
        f'{belt_path}'
        f'<circle cx="{c1_x}" cy="{c1_y}" r="{r1_px}" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>'
        f'<circle cx="{c1_x}" cy="{c1_y}" r="4" fill="#0369a1"/>'
        f'<text x="{c1_x}" y="{c1_y + r1_px + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#0369a1">Driver D₁={_fmt(d1)} m</text>'
        f'<circle cx="{c2_x}" cy="{c2_y}" r="{r2_px}" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>'
        f'<circle cx="{c2_x}" cy="{c2_y}" r="4" fill="#b45309"/>'
        f'<text x="{c2_x}" y="{c2_y + r2_px + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#b45309">Driven D₂={_fmt(d2)} m</text>'
        f'<text x="180" y="105" text-anchor="middle" font-size="10" fill="#64748b">Belt velocity v₁ = v₂</text>'
        f'</svg>'
    )


def _svg_meshed_gears(t1: int, t2: int) -> str:
    """Dynamic SVG of two meshed spur gears with tooth counts T1 and T2."""
    r1 = 40
    r2 = max(30, min(65, int(40 * (t2 / max(t1, 1)))))
    c1_x = 100
    c2_x = c1_x + r1 + r2
    cy = 130
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%" style="max-width:360px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="180" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Meshed Gear Transmission</text>'
        f'<circle cx="{c1_x}" cy="{cy}" r="{r1}" fill="#f1f5f9" stroke="#475569" stroke-width="2.5" stroke-dasharray="6,3"/>'
        f'<circle cx="{c1_x}" cy="{cy}" r="4" fill="#0f172a"/>'
        f'<text x="{c1_x}" y="{cy + r1 + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">Gear 1 (T₁ = {t1})</text>'
        f'<circle cx="{c2_x}" cy="{cy}" r="{r2}" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="6,3"/>'
        f'<circle cx="{c2_x}" cy="{cy}" r="4" fill="#991b1b"/>'
        f'<text x="{c2_x}" y="{cy + r2 + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#991b1b">Gear 2 (T₂ = {t2})</text>'
        f'<circle cx="{c1_x + r1}" cy="{cy}" r="3" fill="#ea580c"/>'
        f'<text x="{c1_x + r1}" y="{cy - 12}" text-anchor="middle" font-size="9" fill="#ea580c">Mesh Point</text>'
        f'</svg>'
    )


def _svg_rack_and_pinion(diam_mm: int, rpm: int) -> str:
    """Dynamic SVG of a rack and pinion mechanism with diameter and linear traverse vector."""
    r_px = max(25, min(55, diam_mm // 2))
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%" style="max-width:360px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="180" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Rack and Pinion Feed Drive</text>'
        f'<circle cx="150" cy="110" r="{r_px}" fill="#f1f5f9" stroke="#0f172a" stroke-width="2.5" stroke-dasharray="6,3"/>'
        f'<circle cx="150" cy="110" r="4.5" fill="#0f172a"/>'
        f'<text x="150" y="114" text-anchor="middle" font-size="9" fill="#0f172a">D = {diam_mm} mm</text>'
        f'<line x1="40" y1="{110 + r_px}" x2="300" y2="{110 + r_px}" stroke="#334155" stroke-width="6"/>'
        f'<text x="60" y="{110 + r_px + 18}" font-size="10" font-weight="bold" fill="#334155">Traverse Rack ({rpm} r/min)</text>'
        f'<line x1="220" y1="{110 + r_px}" x2="270" y2="{110 + r_px}" stroke="#dc2626" stroke-width="2.5"/>'
        f'<polygon points="275,{110 + r_px} 265,{110 + r_px - 4} 265,{110 + r_px + 4}" fill="#dc2626"/>'
        f'<text x="250" y="{110 + r_px - 8}" font-size="10" font-weight="bold" fill="#dc2626">v</text>'
        f'</svg>'
    )


def _svg_winch_drum(radius_m: float, turns: float) -> str:
    """Dynamic SVG of a winch / hoist drum with wound cable."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%" style="max-width:360px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="180" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Winch Drum Cable Hoist</text>'
        f'<circle cx="140" cy="115" r="50" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5"/>'
        f'<circle cx="140" cy="115" r="5" fill="#0f172a"/>'
        f'<line x1="140" y1="115" x2="190" y2="115" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,3"/>'
        f'<text x="165" y="108" font-size="10" font-weight="bold" fill="#2563eb">r = {_fmt(radius_m)} m</text>'
        f'<line x1="190" y1="115" x2="190" y2="210" stroke="#475569" stroke-width="3"/>'
        f'<rect x="175" y="210" width="30" height="25" rx="3" fill="#ea580c"/>'
        f'<text x="190" y="227" text-anchor="middle" font-size="10" font-weight="bold" fill="#ffffff">Load</text>'
        f'<text x="210" y="165" font-size="10" fill="#475569">Lift h = rθ</text>'
        f'</svg>'
    )


def _make_q(
    r: random.Random,
    subskill: str,
    idx: int,
    prompt: str,
    correct_answer: str,
    solution_text: str,
    marks: int,
    tags: List[str],
    rubric: List[Dict[str, Any]],
    hints: Dict[str, str],
    svg: Optional[str] = None,
) -> Dict[str, Any]:
    q_id = f"tech_math_ang_{idx:02d}_{r.randint(100000, 999999)}"
    marking_points = [
        {
            "id": f"mp_{i + 1}",
            "desc": item.get("criterion", f"Step {i + 1}"),
            "marks": item.get("marks", 1),
            "editable": True,
        }
        for i, item in enumerate(rubric)
    ]
    out: Dict[str, Any] = {
        "id": q_id,
        "topic": "Circles, angles and angular movement",
        "subskill": subskill,
        "archetype_id": subskill,
        "question_type": "numeric_input",
        "modality": "math_steps",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": correct_answer,
        "sample_answer": solution_text,
        "solution": solution_text,
        "explanation": solution_text,
        "marks": marks,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "learning_objective_id": f"tech_math_{subskill}",
        "mode": subskill,
        "misconception_tags": tags,
        "Rubric": rubric,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
    }
    if svg:
        out["diagram_spec"] = {
            "kind": "inline_svg",
            "svg": svg,
            "width": 360,
            "height": 250,
        }
    return out


# 26. Rotational frequency rpm to rev/s conversion
def build_26_rotational_frequency_rpm_to_rps_conversion(r: random.Random) -> Dict[str, Any]:
    rpm = r.choice([360, 480, 720, 900, 1200, 1500, 1800, 2400, 3000, 3600])
    rps = rpm / 60.0
    prompt = (
        f"An electric lathe spindle rotates at a constant rotational frequency of ${rpm}\\text{{ r/min}}$ (revolutions per minute).\n\n"
        f"Convert this rotational frequency to revolutions per second ($\\text{{r/s}}$ or $\\text{{s}}^{{-1}}$)."
    )
    ans = f"{_fmt(rps)}\\text{{ r/s}}"
    sol = f"$n = \\frac{{\\text{{rpm}}}}{{60}} = \\frac{{{rpm}}}{{60}} = {_fmt(rps)}\\text{{ r/s}}$."
    return _make_q(
        r, "26_rotational_frequency_rpm_to_rps_conversion", 26, prompt, ans, sol, 2,
        ["multiplied_by_60_instead_of_dividing_for_rps"],
        [{"step": 1, "criterion": "Formula n = rpm / 60", "marks": 1}, {"step": 2, "criterion": f"n = {_fmt(rps)} r/s", "marks": 1}],
        {"tier_1": "Divide revolutions per minute by 60 to obtain revolutions per second.", "tier_2": f"{rpm} / 60.", "tier_3": ans},
    )


# 27. Angular velocity from rotational frequency in rad/s
def build_27_angular_velocity_from_rotational_frequency_rad_per_sec(r: random.Random) -> Dict[str, Any]:
    rpm = r.choice([150, 300, 450, 600, 750, 900, 1200, 1800])
    rps = rpm / 60.0
    omega = 2.0 * math.pi * rps
    omega_s = _fmt(omega, 2)
    prompt = (
        f"A circular grinding disc rotates at a constant frequency of ${rpm}\\text{{ r/min}}$.\n\n"
        f"Calculate the **angular velocity** ($\\omega$) of the disc in radians per second ($\\text{{rad}}\\cdot\\text{{s}}^{{-1}}$). "
        f"Round your answer to two decimal places."
    )
    ans = f"{omega_s}\\text{{ rad/s}}"
    sol = (
        f"$n = \\frac{{{rpm}}}{{60}} = {_fmt(rps)}\\text{{ r/s}}$.\n"
        f"$\\omega = 2\\pi n = 2\\pi({_fmt(rps)}) = {2 * rps}\\pi \\approx {omega_s}\\text{{ rad/s}}$."
    )
    return _make_q(
        r, "27_angular_velocity_from_rotational_frequency_rad_per_sec", 27, prompt, ans, sol, 3,
        ["forgot_to_convert_rpm_to_rps_before_omega_formula", "used_pi_instead_of_2_pi_in_omega"],
        [{"step": 1, "criterion": f"n = {rpm}/60 = {_fmt(rps)} r/s", "marks": 1}, {"step": 2, "criterion": "Formula omega = 2*pi*n", "marks": 1}, {"step": 3, "criterion": f"omega = {omega_s} rad/s", "marks": 1}],
        {"tier_1": "First divide rpm by 60 to find n in r/s, then use omega = 2*pi*n.", "tier_2": f"n = {_fmt(rps)} r/s; omega = 2*pi*{_fmt(rps)}.", "tier_3": ans},
    )


# 28. Rotational frequency and rpm from angular velocity
def build_28_rotational_frequency_and_rpm_from_angular_velocity(r: random.Random) -> Dict[str, Any]:
    rps = r.choice([5, 8, 10, 12, 15, 20, 25])
    omega = round(2.0 * math.pi * rps, 2)
    rpm = int(rps * 60)
    prompt = (
        f"The rotor of an induction motor has an angular velocity of $\\omega = {_fmt(omega)}\\text{{ rad}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Calculate the rotational frequency ($n$) in $\\text{{r/s}}$.\n"
        f"2. Calculate the speed of the motor in revolutions per minute ($\\text{{r/min}}$)."
    )
    ans = f"n = {rps}\\text{{ r/s}},\\ \\text{{speed}} = {rpm}\\text{{ r/min}}"
    sol = (
        f"1. $n = \\frac{{\\omega}}{{2\\pi}} = \\frac{{{_fmt(omega)}}}{{2\\pi}} \\approx {rps}\\text{{ r/s}}$.\n"
        f"2. $\\text{{Speed in r/min}} = n \\times 60 = {rps} \\times 60 = {rpm}\\text{{ r/min}}$."
    )
    return _make_q(
        r, "28_rotational_frequency_and_rpm_from_angular_velocity", 28, prompt, ans, sol, 3,
        ["divided_by_pi_instead_of_two_pi_when_solving_for_n"],
        [{"step": 1, "criterion": f"n = omega / (2*pi) = {rps} r/s", "marks": 2}, {"step": 2, "criterion": f"rpm = n * 60 = {rpm} r/min", "marks": 1}],
        {"tier_1": "Isolate n: n = omega / (2*pi). Then multiply by 60 for rpm.", "tier_2": f"{_fmt(omega)} / (2*pi) = {rps} r/s.", "tier_3": ans},
    )


# 29. Angular displacement from angular velocity and time
def build_29_angular_displacement_from_angular_velocity_and_time(r: random.Random) -> Dict[str, Any]:
    rps = r.choice([2, 4, 5, 8, 10])
    omega = round(2.0 * math.pi * rps, 2)
    t_sec = r.randint(3, 12)
    theta = round(omega * t_sec, 2)
    revs = round(rps * t_sec, 1)
    prompt = (
        f"A flywheel rotates at a constant angular velocity of $\\omega = {_fmt(omega)}\\text{{ rad}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Calculate the total angular displacement ($\\theta$) in radians rotated in ${t_sec}\\text{{ seconds}}$.\n"
        f"2. How many complete revolutions does the flywheel make in this time?"
    )
    ans = f"\\theta = {_fmt(theta)}\\text{{ rad}},\\ N = {_fmt(revs)}\\text{{ revs}}"
    sol = (
        f"1. $\\theta = \\omega t = {_fmt(omega)} \\times {t_sec} = {_fmt(theta)}\\text{{ rad}}$.\n"
        f"2. $N = \\frac{{\\theta}}{{2\\pi}} = \\frac{{{_fmt(theta)}}}{{2\\pi}} = {_fmt(revs)}\\text{{ revolutions}}$."
    )
    return _make_q(
        r, "29_angular_displacement_from_angular_velocity_and_time", 29, prompt, ans, sol, 3,
        ["divided_by_time_instead_of_multiplying_for_angular_displacement"],
        [{"step": 1, "criterion": f"theta = omega * t = {_fmt(theta)} rad", "marks": 2}, {"step": 2, "criterion": f"Revolutions N = theta / (2*pi) = {_fmt(revs)}", "marks": 1}],
        {"tier_1": "Angular displacement is theta = omega * t in radians.", "tier_2": "Divide theta by 2*pi to find the number of revolutions.", "tier_3": ans},
    )


# 30. Time taken for specified number of revolutions
def build_30_time_taken_for_specified_number_of_revolutions(r: random.Random) -> Dict[str, Any]:
    rpm = r.choice([120, 240, 360, 480, 600])
    rps = rpm // 60
    n_revs = r.choice([20, 40, 60, 100, 150])
    t_sec = round(n_revs / rps, 2)
    prompt = (
        f"A centrifuge runs at a steady speed of ${rpm}\\text{{ r/min}}$.\n\n"
        f"Calculate the time in seconds taken for the centrifuge drum to complete ${n_revs}$ revolutions."
    )
    ans = f"{_fmt(t_sec)}\\text{{ s}}"
    sol = (
        f"Rotational frequency $n = \\frac{{{rpm}}}{{60}} = {rps}\\text{{ r/s}}$.\n"
        f"Time $t = \\frac{{N}}{{n}} = \\frac{{{n_revs}}}{{{rps}}} = {_fmt(t_sec)}\\text{{ seconds}}$."
    )
    return _make_q(
        r, "30_time_taken_for_specified_number_of_revolutions", 30, prompt, ans, sol, 2,
        ["multiplied_frequency_by_revolutions_instead_of_dividing"],
        [{"step": 1, "criterion": f"n = {rpm} / 60 = {rps} r/s", "marks": 1}, {"step": 2, "criterion": f"t = {n_revs} / {rps} = {_fmt(t_sec)} s", "marks": 1}],
        {"tier_1": "Convert rpm to rps, then time t = number of revolutions / rps.", "tier_2": f"t = {n_revs} / {rps}.", "tier_3": ans},
    )


# 31. Circumferential linear velocity from radius and omega (with SVG)
def build_31_circumferential_linear_velocity_from_radius_and_omega_svg(r: random.Random) -> Dict[str, Any]:
    diam = r.choice([0.6, 0.8, 1.0, 1.2, 1.5, 2.0])
    radius = diam / 2.0
    rpm = r.choice([120, 180, 240, 300, 420, 600])
    omega = round(2.0 * math.pi * (rpm / 60.0), 2)
    v_lin = round(radius * omega, 2)
    svg = _svg_rotating_wheel(diam, rpm, show_tangent=True)
    prompt = (
        f"Refer to the rotating wheel shown in the diagram, which has a diameter of $D = {_fmt(diam)}\\text{{ m}}$ "
        f"and rotates at ${rpm}\\text{{ r/min}}$ (angular velocity $\\omega = {_fmt(omega)}\\text{{ rad/s}}$).\n\n"
        f"Calculate the **circumferential (linear) velocity** ($v = \\omega r$) of a point on the outer rim of the wheel in $\\text{{m/s}}$."
    )
    ans = f"{_fmt(v_lin)}\\text{{ m/s}}"
    sol = (
        f"Radius $r = \\frac{{D}}{{2}} = \\frac{{{_fmt(diam)}}}{{2}} = {_fmt(radius)}\\text{{ m}}$.\n"
        f"Linear velocity $v = \\omega r = {_fmt(omega)} \\times {_fmt(radius)} = {_fmt(v_lin)}\\text{{ m/s}}$."
    )
    return _make_q(
        r, "31_circumferential_linear_velocity_from_radius_and_omega_svg", 31, prompt, ans, sol, 3,
        ["used_diameter_instead_of_radius_in_v_equals_omega_r"],
        [{"step": 1, "criterion": f"Radius r = {diam}/2 = {_fmt(radius)} m", "marks": 1}, {"step": 2, "criterion": "Formula v = omega * r", "marks": 1}, {"step": 3, "criterion": f"v = {_fmt(v_lin)} m/s", "marks": 1}],
        {"tier_1": "Divide the diameter by 2 to get the radius, then use v = omega * r.", "tier_2": f"v = {_fmt(omega)} * {_fmt(radius)}.", "tier_3": ans},
        svg=svg,
    )


# 32. Circumferential linear velocity from diameter and rpm (with SVG)
def build_32_circumferential_linear_velocity_from_diameter_and_rpm_svg(r: random.Random) -> Dict[str, Any]:
    diam_mm = r.choice([250, 300, 350, 400, 450, 500])
    diam_m = diam_mm / 1000.0
    rpm = r.choice([1200, 1500, 1800, 2400, 3000])
    rps = rpm / 60.0
    v_lin = round(math.pi * diam_m * rps, 2)
    svg = _svg_rotating_wheel(diam_m, rpm, show_tangent=True)
    prompt = (
        f"A circular tungsten-carbide saw blade (shown in the diagram) has a diameter of ${diam_mm}\\text{{ mm}}$ "
        f"and spins at an operating speed of ${rpm}\\text{{ r/min}}$.\n\n"
        f"1. Express the blade diameter in metres ($D$).\n"
        f"2. Calculate the rotational frequency $n$ in $\\text{{r/s}}$.\n"
        f"3. Calculate the cutting speed (circumferential linear velocity $v = \\pi D n$) of the blade teeth in $\\text{{m/s}}$."
    )
    ans = f"{_fmt(v_lin)}\\text{{ m/s}}"
    sol = (
        f"1. $D = \\frac{{{diam_mm}}}{{1000}} = {_fmt(diam_m)}\\text{{ m}}$.\n"
        f"2. $n = \\frac{{{rpm}}}{{60}} = {_fmt(rps)}\\text{{ r/s}}$.\n"
        f"3. $v = \\pi D n = \\pi \\times {_fmt(diam_m)} \\times {_fmt(rps)} \\approx {_fmt(v_lin)}\\text{{ m/s}}$."
    )
    return _make_q(
        r, "32_circumferential_linear_velocity_from_diameter_and_rpm_svg", 32, prompt, ans, sol, 3,
        ["forgot_to_convert_millimetres_to_metres_in_linear_velocity"],
        [{"step": 1, "criterion": f"Diameter D = {_fmt(diam_m)} m", "marks": 1}, {"step": 2, "criterion": f"n = {_fmt(rps)} r/s", "marks": 1}, {"step": 3, "criterion": f"v = pi*D*n = {_fmt(v_lin)} m/s", "marks": 1}],
        {"tier_1": "Convert mm to m by dividing by 1000, and rpm to r/s by dividing by 60.", "tier_2": f"v = pi * {diam_m} * {rps}.", "tier_3": ans},
        svg=svg,
    )


# 33. Find radius or diameter from linear and angular velocity (with SVG)
def build_33_find_radius_or_diameter_from_linear_and_angular_velocity_svg(r: random.Random) -> Dict[str, Any]:
    v_lin = r.choice([15, 20, 25, 30, 35, 40])
    rpm = r.choice([300, 450, 600, 900, 1200])
    rps = rpm / 60.0
    omega = 2.0 * math.pi * rps
    radius = round(v_lin / omega, 3)
    diam = round(2.0 * radius, 3)
    svg = _svg_rotating_wheel(diam, rpm, show_tangent=True)
    prompt = (
        f"A high-speed industrial turbine wheel (illustrated in the diagram) spins at ${rpm}\\text{{ r/min}}$. "
        f"The maximum allowable tangential speed on the outer rim is $v = {v_lin}\\text{{ m/s}}$.\n\n"
        f"Calculate the **maximum permissible diameter** ($D$) of the wheel in metres, correct to two decimal places."
    )
    ans = f"{_fmt(diam, 2)}\\text{{ m}}"
    sol = (
        f"$\\omega = 2\\pi n = 2\\pi\\left(\\frac{{{rpm}}}{{60}}\\right) = {_fmt(omega, 2)}\\text{{ rad/s}}$.\n"
        f"Radius $r = \\frac{{v}}{{\\omega}} = \\frac{{{v_lin}}}{{{_fmt(omega, 2)}}} \\approx {_fmt(radius, 3)}\\text{{ m}}$.\n"
        f"Diameter $D = 2r = 2 \\times {_fmt(radius, 3)} \\approx {_fmt(diam, 2)}\\text{{ m}}$."
    )
    return _make_q(
        r, "33_find_radius_or_diameter_from_linear_and_angular_velocity_svg", 33, prompt, ans, sol, 3,
        ["confused_radius_with_diameter_when_solving_from_v"],
        [{"step": 1, "criterion": f"omega = 2*pi*n = {_fmt(omega, 2)} rad/s", "marks": 1}, {"step": 2, "criterion": f"r = v / omega = {_fmt(radius, 3)} m", "marks": 1}, {"step": 3, "criterion": f"D = 2r = {_fmt(diam, 2)} m", "marks": 1}],
        {"tier_1": "Find omega first, then r = v / omega, then double r to find diameter D.", "tier_2": f"r = {v_lin} / {_fmt(omega, 2)}.", "tier_3": ans},
        svg=svg,
    )


# 34. Linear speed of clock hand tip (with SVG)
def build_34_linear_speed_of_clock_hand_tip_svg(r: random.Random) -> Dict[str, Any]:
    hand_type = r.choice(["second", "minute"])
    length_cm = r.randint(8, 25)
    length_m = length_cm / 100.0

    if hand_type == "second":
        t_period = 60  # seconds
        name = "second hand"
    else:
        t_period = 3600  # seconds
        name = "minute hand"

    omega = (2.0 * math.pi) / t_period
    v_lin_mm_s = round(length_m * omega * 1000.0, 2)
    svg = _svg_rotating_wheel(length_m * 2.0, 1, show_tangent=True)

    prompt = (
        f"The {name} of an ornamental town hall clock (represented by the rotating pointer in the diagram) "
        f"has a length of ${length_cm}\\text{{ cm}}$ from the pivot to the tip.\n\n"
        f"1. State the period of one complete revolution in seconds.\n"
        f"2. Calculate the angular velocity $\\omega$ of the {name} in $\\text{{rad/s}}$.\n"
        f"3. Calculate the linear speed of the tip in millimetres per second ($\\text{{mm/s}}$)."
    )
    ans = f"{_fmt(v_lin_mm_s)}\\text{{ mm/s}}"
    sol = (
        f"1. Period $T = {t_period}\\text{{ s}}$.\n"
        f"2. $\\omega = \\frac{{2\\pi}}{{T}} = \\frac{{2\\pi}}{{{t_period}}}\\text{{ rad/s}}$.\n"
        f"3. Linear speed $v = \\omega r = \\frac{{2\\pi}}{{{t_period}}} \\times {length_cm * 10}\\text{{ mm}} \\approx {_fmt(v_lin_mm_s)}\\text{{ mm/s}}$."
    )
    return _make_q(
        r, "34_linear_speed_of_clock_hand_tip_svg", 34, prompt, ans, sol, 3,
        ["incorrect_time_period_for_clock_hand_revolution"],
        [{"step": 1, "criterion": f"Period T = {t_period} s", "marks": 1}, {"step": 2, "criterion": f"omega = 2*pi / {t_period}", "marks": 1}, {"step": 3, "criterion": f"v = {_fmt(v_lin_mm_s)} mm/s", "marks": 1}],
        {"tier_1": f"A {name} takes {t_period} seconds to complete 2*pi radians.", "tier_2": f"v = omega * r = (2*pi / {t_period}) * {length_cm * 10} mm/s.", "tier_3": ans},
        svg=svg,
    )


# 35. Centripetal acceleration on rotating rim (with SVG)
def build_35_centripetal_acceleration_on_rotating_rim_svg(r: random.Random) -> Dict[str, Any]:
    diam_m = r.choice([0.4, 0.5, 0.6, 0.8, 1.0])
    radius = diam_m / 2.0
    rpm = r.choice([300, 600, 900, 1200])
    omega = round(2.0 * math.pi * (rpm / 60.0), 2)
    accel = round((omega ** 2) * radius, 1)
    svg = _svg_rotating_wheel(diam_m, rpm, show_tangent=True)
    prompt = (
        f"A centrifuge rotor of diameter $D = {_fmt(diam_m)}\\text{{ m}}$ (shown in the diagram) spins at ${rpm}\\text{{ r/min}}$ "
        f"(angular velocity $\\omega = {_fmt(omega)}\\text{{ rad/s}}$).\n\n"
        f"Calculate the **centripetal acceleration** ($a = \\omega^2 r$) experienced by a test sample located at the outer rim. "
        f"Express your answer in $\\text{{m}}\\cdot\\text{{s}}^{{-2}}$."
    )
    ans = f"{_fmt(accel, 1)}\\text{{ m/s}}^2"
    sol = (
        f"Radius $r = \\frac{{{_fmt(diam_m)}}}{{2}} = {_fmt(radius)}\\text{{ m}}$.\n"
        f"Centripetal acceleration $a = \\omega^2 r = ({_fmt(omega)})^2 \\times {_fmt(radius)} \\approx {_fmt(accel, 1)}\\text{{ m/s}}^2$."
    )
    return _make_q(
        r, "35_centripetal_acceleration_on_rotating_rim_svg", 35, prompt, ans, sol, 3,
        ["forgot_to_square_angular_velocity_in_acceleration_formula"],
        [{"step": 1, "criterion": f"Radius r = {_fmt(radius)} m", "marks": 1}, {"step": 2, "criterion": "Formula a = omega^2 * r", "marks": 1}, {"step": 3, "criterion": f"a = {_fmt(accel, 1)} m/s^2", "marks": 1}],
        {"tier_1": "Square the angular velocity and multiply by the radius: a = omega^2 * r.", "tier_2": f"({_fmt(omega)})^2 * {_fmt(radius)}.", "tier_3": ans},
        svg=svg,
    )


# 36. Belt and pulley drive equal linear speed (with SVG)
def build_36_belt_and_pulley_drive_equal_linear_speed_svg(r: random.Random) -> Dict[str, Any]:
    d1 = r.choice([0.15, 0.20, 0.25, 0.30])
    ratio = r.choice([1.5, 2.0, 2.5, 3.0])
    d2 = round(d1 * ratio, 2)
    rpm1 = r.choice([600, 900, 1200, 1500, 1800])
    rpm2 = round(rpm1 / ratio, 1)
    svg = _svg_belt_pulley_drive(d1, d2, crossed=False)
    prompt = (
        f"In the belt and pulley drive shown in the diagram, driver pulley 1 has diameter $D_1 = {_fmt(d1)}\\text{{ m}}$ "
        f"and rotates at $n_1 = {rpm1}\\text{{ r/min}}$.\n"
        f"The driven pulley 2 has diameter $D_2 = {_fmt(d2)}\\text{{ m}}$. The belt does not slip ($v_1 = v_2$).\n\n"
        f"Calculate the rotational frequency ($n_2$) of the driven pulley in $\\text{{r/min}}$."
    )
    ans = f"{_fmt(rpm2)}\\text{{ r/min}}"
    sol = (
        f"Since the belt linear velocity is equal on both pulleys ($v_1 = v_2$):\n"
        f"$$\\pi D_1 n_1 = \\pi D_2 n_2 \\implies D_1 n_1 = D_2 n_2$$\n"
        f"$$n_2 = \\frac{{D_1 \\times n_1}}{{D_2}} = \\frac{{{_fmt(d1)} \\times {rpm1}}}{{{_fmt(d2)}}} = {_fmt(rpm2)}\\text{{ r/min}}$."
    )
    return _make_q(
        r, "36_belt_and_pulley_drive_equal_linear_speed_svg", 36, prompt, ans, sol, 3,
        ["inverted_pulley_diameter_ratio"],
        [{"step": 1, "criterion": "Equate D1*n1 = D2*n2", "marks": 1}, {"step": 2, "criterion": "Substitute given values", "marks": 1}, {"step": 3, "criterion": f"n2 = {_fmt(rpm2)} r/min", "marks": 1}],
        {"tier_1": "For a belt drive, D1 * n1 = D2 * n2.", "tier_2": f"n2 = ({_fmt(d1)} * {rpm1}) / {_fmt(d2)}.", "tier_3": ans},
        svg=svg,
    )


# 37. Belt drive calculate required driver pulley diameter (with SVG)
def build_37_belt_drive_calculate_required_driver_pulley_diameter_svg(r: random.Random) -> Dict[str, Any]:
    d2 = r.choice([0.30, 0.40, 0.50, 0.60])
    rpm_motor = 1440  # standard 4-pole motor rpm
    rpm_driven = r.choice([360, 480, 720])
    d1 = round((d2 * rpm_driven) / rpm_motor, 3)
    d1_mm = int(round(d1 * 1000))
    svg = _svg_belt_pulley_drive(d1, d2, crossed=False)
    prompt = (
        f"An electric motor running at $n_1 = {rpm_motor}\\text{{ r/min}}$ drives an air compressor pulley (diameter $D_2 = {_fmt(d2)}\\text{{ m}}$) "
        f"via a flat belt (illustrated in the diagram).\n"
        f"The compressor must operate at $n_2 = {rpm_driven}\\text{{ r/min}}$.\n\n"
        f"Calculate the **required pitch diameter of the motor pulley** ($D_1$) in millimetres."
    )
    ans = f"{d1_mm}\\text{{ mm}}"
    sol = (
        f"$D_1 n_1 = D_2 n_2 \\implies D_1 = \\frac{{D_2 \\times n_2}}{{n_1}} = \\frac{{{_fmt(d2)} \\times {rpm_driven}}}{{{rpm_motor}}} = {_fmt(d1, 3)}\\text{{ m}}$.\n"
        f"In millimetres: $D_1 = {_fmt(d1, 3)} \\times 1000 = {d1_mm}\\text{{ mm}}$."
    )
    return _make_q(
        r, "37_belt_drive_calculate_required_driver_pulley_diameter_svg", 37, prompt, ans, sol, 3,
        ["inverted_motor_and_driven_speed_ratio"],
        [{"step": 1, "criterion": "Formula D1 = (D2 * n2) / n1", "marks": 1}, {"step": 2, "criterion": f"D1 = {_fmt(d1, 3)} m", "marks": 1}, {"step": 3, "criterion": f"D1 = {d1_mm} mm", "marks": 1}],
        {"tier_1": "Since the motor runs faster than the compressor, the motor pulley must be smaller: D1 = (D2 * n2) / n1.", "tier_2": f"D1 = ({_fmt(d2)} * {rpm_driven}) / {rpm_motor}.", "tier_3": ans},
        svg=svg,
    )


# 38. Stepped cone pulley transmission speed ratios (with SVG)
def build_38_stepped_cone_pulley_transmission_speed_ratios_svg(r: random.Random) -> Dict[str, Any]:
    n_in = r.choice([600, 900, 1200])
    pair1 = (0.10, 0.30)  # low step (1:3)
    pair2 = (0.20, 0.20)  # mid step (1:1)
    pair3 = (0.30, 0.10)  # high step (3:1)
    step = r.choice([1, 2, 3])
    d1, d2 = [pair1, pair2, pair3][step - 1]
    n_out = round(n_in * (d1 / d2))
    svg = _svg_belt_pulley_drive(d1, d2, crossed=False)
    prompt = (
        f"A workshop drill press uses a stepped cone pulley drive (shown schematically in the diagram) driven by a motor at $n = {n_in}\\text{{ r/min}}$.\n"
        f"On step {step}, the active driver pulley diameter is $D_1 = {_fmt(d1)}\\text{{ m}}$ and the driven pulley diameter is $D_2 = {_fmt(d2)}\\text{{ m}}$.\n\n"
        f"Calculate the spindle speed ($n_2$) in $\\text{{r/min}}$ on this step."
    )
    ans = f"{n_out}\\text{{ r/min}}"
    sol = f"$n_2 = \\frac{{D_1}}{{D_2}} \\times n_1 = \\frac{{{_fmt(d1)}}}{{{_fmt(d2)}}} \\times {n_in} = {n_out}\\text{{ r/min}}$."
    return _make_q(
        r, "38_stepped_cone_pulley_transmission_speed_ratios_svg", 38, prompt, ans, sol, 3,
        ["swapped_driver_and_driven_cone_step_diameters"],
        [{"step": 1, "criterion": "Formula n2 = (D1 / D2) * n1", "marks": 1}, {"step": 2, "criterion": f"Ratio = {_fmt(d1 / d2, 2)}", "marks": 1}, {"step": 3, "criterion": f"n2 = {n_out} r/min", "marks": 1}],
        {"tier_1": "Multiply input rpm by the ratio of driver diameter to driven diameter (D1 / D2).", "tier_2": f"n2 = ({_fmt(d1)} / {_fmt(d2)}) * {n_in}.", "tier_3": ans},
        svg=svg,
    )


# 39. Crossed belt drive direction and angular speed (with SVG)
def build_39_crossed_belt_drive_direction_and_angular_speed_svg(r: random.Random) -> Dict[str, Any]:
    d1 = r.choice([0.2, 0.3, 0.4])
    d2 = round(d1 * r.choice([1.5, 2.0]), 2)
    rpm1 = r.choice([400, 600, 800])
    rpm2 = round(rpm1 * (d1 / d2), 1)
    svg = _svg_belt_pulley_drive(d1, d2, crossed=True)
    prompt = (
        f"Refer to the crossed belt drive shown in the diagram, where driver pulley 1 has diameter $D_1 = {_fmt(d1)}\\text{{ m}}$ "
        f"and turns **clockwise** at ${rpm1}\\text{{ r/min}}$. Driven pulley 2 has diameter $D_2 = {_fmt(d2)}\\text{{ m}}$.\n\n"
        f"1. State the **direction of rotation** of driven pulley 2 (clockwise or anticlockwise).\n"
        f"2. Calculate the rotational speed ($n_2$) of driven pulley 2 in $\\text{{r/min}}$."
    )
    ans = f"\\text{{Anticlockwise}},\\ n_2 = {_fmt(rpm2)}\\text{{ r/min}}"
    sol = (
        f"1. Because the belt is **crossed**, the driven pulley rotates in the **opposite (anticlockwise)** direction.\n"
        f"2. $n_2 = \\frac{{D_1}}{{D_2}} \\times n_1 = \\frac{{{_fmt(d1)}}}{{{_fmt(d2)}}} \\times {rpm1} = {_fmt(rpm2)}\\text{{ r/min}}$."
    )
    return _make_q(
        r, "39_crossed_belt_drive_direction_and_angular_speed_svg", 39, prompt, ans, sol, 3,
        ["stated_same_direction_for_crossed_belt_drive"],
        [{"step": 1, "criterion": "Direction is anticlockwise (reversed by crossed belt)", "marks": 1}, {"step": 2, "criterion": f"n2 = {_fmt(rpm2)} r/min", "marks": 2}],
        {"tier_1": "A crossed belt reverses the rotational direction of the driven shaft.", "tier_2": f"Speed calculation is identical to open belt: n2 = (D1 / D2) * n1.", "tier_3": ans},
        svg=svg,
    )


# 40. Belt linear speed and travel distance (with SVG)
def build_40_belt_linear_speed_and_travel_distance_svg(r: random.Random) -> Dict[str, Any]:
    d1 = r.choice([0.25, 0.30, 0.40, 0.50])
    rpm1 = r.choice([300, 480, 600, 900])
    rps1 = rpm1 / 60.0
    v_belt = round(math.pi * d1 * rps1, 2)
    t_min = r.choice([2, 3, 5])
    t_sec = t_min * 60
    dist_m = round(v_belt * t_sec, 1)
    svg = _svg_belt_pulley_drive(d1, d1 * 1.5, crossed=False)
    prompt = (
        f"A heavy conveyor belt runs around a drive pulley of diameter $D = {_fmt(d1)}\\text{{ m}}$ (shown in the diagram) rotating at ${rpm1}\\text{{ r/min}}$.\n\n"
        f"1. Calculate the linear speed of the belt ($v$) in metres per second ($\\text{{m/s}}$).\n"
        f"2. Calculate the distance moved by a point on the belt in ${t_min}\\text{{ minutes}}$."
    )
    ans = f"v = {_fmt(v_belt)}\\text{{ m/s}},\\ s = {_fmt(dist_m)}\\text{{ m}}"
    sol = (
        f"1. $v = \\pi D n = \\pi \\times {_fmt(d1)} \\times \\left(\\frac{{{rpm1}}}{{60}}\\right) \\approx {_fmt(v_belt)}\\text{{ m/s}}$.\n"
        f"2. In ${t_min}\\text{{ min}} = {t_sec}\\text{{ s}}$, distance $s = v \\times t = {_fmt(v_belt)} \\times {t_sec} = {_fmt(dist_m)}\\text{{ m}}$."
    )
    return _make_q(
        r, "40_belt_linear_speed_and_travel_distance_svg", 40, prompt, ans, sol, 3,
        ["forgot_to_convert_minutes_to_seconds_when_multiplying_speed"],
        [{"step": 1, "criterion": f"Linear speed v = {_fmt(v_belt)} m/s", "marks": 2}, {"step": 2, "criterion": f"Distance s = {_fmt(dist_m)} m", "marks": 1}],
        {"tier_1": "v = pi * D * (rpm / 60). Then multiply v by time in seconds.", "tier_2": f"s = {_fmt(v_belt)} * ({t_min} * 60).", "tier_3": ans},
        svg=svg,
    )


# 41. Meshed spur gears velocity ratio and teeth count (with SVG)
def build_41_meshed_spur_gears_velocity_ratio_and_teeth_count_svg(r: random.Random) -> Dict[str, Any]:
    t1 = r.choice([18, 20, 24, 28, 30])
    ratio = r.choice([2, 3, 4])
    t2 = t1 * ratio
    n1 = r.choice([300, 600, 900, 1200])
    n2 = n1 // ratio
    svg = _svg_meshed_gears(t1, t2)
    prompt = (
        f"In the spur gear pair shown in the diagram, pinion 1 has $T_1 = {t1}\\text{{ teeth}}$ and rotates **clockwise** at $n_1 = {n1}\\text{{ r/min}}$.\n"
        f"Driven gear 2 has $T_2 = {t2}\\text{{ teeth}}$.\n\n"
        f"1. State the direction of rotation of Gear 2.\n"
        f"2. Calculate the gear ratio (velocity ratio) $\\frac{{n_1}}{{n_2}}$.\n"
        f"3. Calculate the rotational speed ($n_2$) of Gear 2 in $\\text{{r/min}}$."
    )
    ans = f"\\text{{Anticlockwise}},\\ \\text{{Ratio}} = {ratio} : 1,\\ n_2 = {n2}\\text{{ r/min}}"
    sol = (
        f"1. Directly meshed external gears rotate in **opposite (anticlockwise)** directions.\n"
        f"2. $\\frac{{n_1}}{{n_2}} = \\frac{{T_2}}{{T_1}} = \\frac{{{t2}}}{{{t1}}} = {ratio} : 1$.\n"
        f"3. $n_2 = n_1 \\times \\frac{{T_1}}{{T_2}} = {n1} \\times \\frac{{{t1}}}{{{t2}}} = {n2}\\text{{ r/min}}$."
    )
    return _make_q(
        r, "41_meshed_spur_gears_velocity_ratio_and_teeth_count_svg", 41, prompt, ans, sol, 3,
        ["inverted_gear_ratio_formula_T1_over_T2"],
        [{"step": 1, "criterion": "Anticlockwise direction", "marks": 1}, {"step": 2, "criterion": f"Gear ratio {ratio}:1", "marks": 1}, {"step": 3, "criterion": f"n2 = {n2} r/min", "marks": 1}],
        {"tier_1": "Directly meshed gears turn in opposite directions. The larger gear turns slower: n2 = n1 * (T1 / T2).", "tier_2": f"n2 = {n1} * ({t1} / {t2}).", "tier_3": ans},
        svg=svg,
    )


# 42. Compound gear train overall velocity ratio (with SVG)
def build_42_compound_gear_train_overall_velocity_ratio_svg(r: random.Random) -> Dict[str, Any]:
    t1 = r.choice([20, 24])
    t2 = r.choice([60, 72])  # stage 1: 3:1
    t3 = r.choice([25, 30])
    t4 = r.choice([75, 90])  # stage 2: 3:1
    r1 = t2 // t1
    r2 = t4 // t3
    total_ratio = r1 * r2
    n_in = r.choice([900, 1440, 1800])
    n_out = n_in // total_ratio
    svg = _svg_meshed_gears(t1, t4)
    prompt = (
        f"A two-stage compound reduction gear train consists of:\n"
        f"• Stage 1: Driver Gear 1 ($T_1 = {t1}$) meshes with Gear 2 ($T_2 = {t2}$).\n"
        f"• Stage 2: Gear 3 ($T_3 = {t3}$, keyed to the same shaft as Gear 2) meshes with driven Gear 4 ($T_4 = {t4}$).\n"
        f"The input speed at Gear 1 is $n_1 = {n_in}\\text{{ r/min}}$.\n\n"
        f"1. Calculate the overall gear ratio of the compound train.\n"
        f"2. Calculate the output speed ($n_4$) of Gear 4 in $\\text{{r/min}}$."
    )
    ans = f"\\text{{Gear Ratio}} = {total_ratio} : 1,\\ n_4 = {n_out}\\text{{ r/min}}"
    sol = (
        f"1. Overall ratio $= \\frac{{T_2 \\times T_4}}{{T_1 \\times T_3}} = \\frac{{{t2} \\times {t4}}}{{{t1} \\times {t3}}} = {r1} \\times {r2} = {total_ratio} : 1$.\n"
        f"2. $n_4 = \\frac{{n_1}}{{\\text{{Overall ratio}}}} = \\frac{{{n_in}}}{{{total_ratio}}} = {n_out}\\text{{ r/min}}$."
    )
    return _make_q(
        r, "42_compound_gear_train_overall_velocity_ratio_svg", 42, prompt, ans, sol, 3,
        ["added_stage_ratios_instead_of_multiplying_in_compound_gear_train"],
        [{"step": 1, "criterion": f"Overall ratio = {total_ratio}:1", "marks": 2}, {"step": 2, "criterion": f"n4 = {n_out} r/min", "marks": 1}],
        {"tier_1": "Multiply the velocity ratios of the individual stages: (T2/T1) * (T4/T3).", "tier_2": f"Overall ratio = {r1} * {r2} = {total_ratio}.", "tier_3": ans},
        svg=svg,
    )


# 43. Internal annular gear and pinion speed ratio (with SVG)
def build_43_internal_annular_gear_and_pinion_speed_ratio_svg(r: random.Random) -> Dict[str, Any]:
    t_pinion = r.choice([16, 20, 24])
    ratio = r.choice([3, 4, 5])
    t_ring = t_pinion * ratio
    rpm_pinion = r.choice([600, 900, 1200])
    rpm_ring = rpm_pinion // ratio
    svg = _svg_meshed_gears(t_pinion, t_ring)
    prompt = (
        f"An internal ring gear (annular gear) has $T_2 = {t_ring}\\text{{ teeth}}$ and meshes with an internal pinion of $T_1 = {t_pinion}\\text{{ teeth}}$.\n"
        f"The pinion rotates **clockwise** at $n_1 = {rpm_pinion}\\text{{ r/min}}$.\n\n"
        f"1. State the rotational direction of the internal ring gear.\n"
        f"2. Calculate the rotational speed ($n_2$) of the ring gear in $\\text{{r/min}}$."
    )
    ans = f"\\text{{Clockwise (same direction)}},\\ n_2 = {rpm_ring}\\text{{ r/min}}"
    sol = (
        f"1. Unlike external gears, an internal gear meshes on the inner circumference and rotates in the **same (clockwise)** direction as the pinion.\n"
        f"2. $n_2 = n_1 \\times \\frac{{T_1}}{{T_2}} = {rpm_pinion} \\times \\frac{{{t_pinion}}}{{{t_ring}}} = {rpm_ring}\\text{{ r/min}}$."
    )
    return _make_q(
        r, "43_internal_annular_gear_and_pinion_speed_ratio_svg", 43, prompt, ans, sol, 3,
        ["assumed_internal_gear_reverses_direction_like_external_gears"],
        [{"step": 1, "criterion": "Same direction (clockwise)", "marks": 1}, {"step": 2, "criterion": f"n2 = {rpm_ring} r/min", "marks": 2}],
        {"tier_1": "Internal mesh maintains the same rotational direction as the driver pinion.", "tier_2": f"n2 = {rpm_pinion} * ({t_pinion} / {t_ring}).", "tier_3": ans},
        svg=svg,
    )


# 44. Rack and pinion linear traverse velocity (with SVG)
def build_44_rack_and_pinion_linear_traverse_velocity_svg(r: random.Random) -> Dict[str, Any]:
    pitch_diam_mm = r.choice([60, 80, 100, 120])
    pitch_diam_m = pitch_diam_mm / 1000.0
    rpm = r.choice([60, 90, 120, 150, 180])
    rps = rpm / 60.0
    v_linear = round(math.pi * pitch_diam_m * rps, 3)
    v_mm_s = int(round(v_linear * 1000))
    svg = _svg_rack_and_pinion(pitch_diam_mm, rpm)
    prompt = (
        f"A CNC milling machine traverse table is driven by a rack-and-pinion mechanism.\n"
        f"The driving pinion gear has a pitch circle diameter of $D = {pitch_diam_mm}\\text{{ mm}}$ and turns at ${rpm}\\text{{ r/min}}$.\n\n"
        f"Calculate the **linear feed rate** (traverse velocity $v = \\pi D n$) of the machine table in millimetres per second ($\\text{{mm/s}}$)."
    )
    ans = f"{v_mm_s}\\text{{ mm/s}}"
    sol = (
        f"Rotational frequency $n = \\frac{{{rpm}}}{{60}} = {_fmt(rps, 2)}\\text{{ r/s}}$.\n"
        f"Linear traverse velocity $v = \\pi D n = \\pi \\times {pitch_diam_mm} \\times {_fmt(rps, 2)} \\approx {v_mm_s}\\text{{ mm/s}}$."
    )
    return _make_q(
        r, "44_rack_and_pinion_linear_traverse_velocity_svg", 44, prompt, ans, sol, 3,
        ["confused_linear_rack_feed_with_angular_velocity"],
        [{"step": 1, "criterion": f"n = {rpm} / 60 = {_fmt(rps, 2)} r/s", "marks": 1}, {"step": 2, "criterion": "Formula v = pi * D * n", "marks": 1}, {"step": 3, "criterion": f"v = {v_mm_s} mm/s", "marks": 1}],
        {"tier_1": "The linear speed of the rack equals the circumferential speed of the pinion: v = pi * D * n.", "tier_2": f"v = pi * {pitch_diam_mm} * ({rpm} / 60).", "tier_3": ans},
        svg=svg,
    )


# 45. Winch hoist drum cable winding linear speed (with SVG)
def build_45_winch_hoist_drum_cable_winding_linear_speed_svg(r: random.Random) -> Dict[str, Any]:
    radius_m = r.choice([0.15, 0.20, 0.25, 0.30, 0.40])
    rpm = r.choice([30, 45, 60, 90])
    omega = round(2.0 * math.pi * (rpm / 60.0), 2)
    v_hoist = round(radius_m * omega, 2)
    t_sec = r.choice([10, 15, 20, 30])
    h_lift = round(v_hoist * t_sec, 2)
    svg = _svg_winch_drum(radius_m, 3.5)
    prompt = (
        f"A construction mine hoist uses a cylindrical winch drum of radius $r = {_fmt(radius_m)}\\text{{ m}}$ (shown in the diagram).\n"
        f"The drum winds up steel cable at a constant rotational speed of ${rpm}\\text{{ r/min}}$ ($\\omega = {_fmt(omega)}\\text{{ rad/s}}$).\n\n"
        f"1. Calculate the hoisting velocity ($v = \\omega r$) of the suspended load in $\\text{{m/s}}$.\n"
        f"2. Calculate the vertical height ($h$) the load is raised in ${t_sec}\\text{{ seconds}}$."
    )
    ans = f"v = {_fmt(v_hoist)}\\text{{ m/s}},\\ h = {_fmt(h_lift)}\\text{{ m}}"
    sol = (
        f"1. Hoisting speed $v = \\omega r = {_fmt(omega)} \\times {_fmt(radius_m)} = {_fmt(v_hoist)}\\text{{ m/s}}$.\n"
        f"2. Height raised $h = v \\times t = {_fmt(v_hoist)} \\times {t_sec} = {_fmt(h_lift)}\\text{{ m}}$."
    )
    return _make_q(
        r, "45_winch_hoist_drum_cable_winding_linear_speed_svg", 45, prompt, ans, sol, 3,
        ["used_diameter_instead_of_radius_in_winch_cable_speed"],
        [{"step": 1, "criterion": f"Hoisting speed v = {_fmt(v_hoist)} m/s", "marks": 2}, {"step": 2, "criterion": f"Lift height h = {_fmt(h_lift)} m", "marks": 1}],
        {"tier_1": "Cable winding speed is v = omega * r. Then vertical lift h = v * t.", "tier_2": f"v = {_fmt(omega)} * {_fmt(radius_m)}; h = {_fmt(v_hoist)} * {t_sec}.", "tier_3": ans},
        svg=svg,
    )


# 46. Vehicle speed from wheel diameter and rpm
def build_46_vehicle_speed_from_wheel_diameter_and_rpm(r: random.Random) -> Dict[str, Any]:
    diam_cm = r.choice([55, 60, 65, 70, 75])
    diam_m = diam_cm / 100.0
    rpm = r.choice([500, 600, 700, 800, 900, 1000])
    rps = rpm / 60.0
    v_m_s = math.pi * diam_m * rps
    v_km_h = round(v_m_s * 3.6, 1)
    prompt = (
        f"A motor car has road wheels with an outer tyre diameter of ${diam_cm}\\text{{ cm}}$.\n"
        f"When travelling in top gear, the road wheels rotate at ${rpm}\\text{{ r/min}}$.\n\n"
        f"1. Calculate the linear speed of the car in metres per second ($\\text{{m/s}}$).\n"
        f"2. Convert this speed to kilometres per hour ($\\text{{km/h}}$), rounded to one decimal place."
    )
    ans = f"{_fmt(v_km_h, 1)}\\text{{ km/h}}"
    sol = (
        f"1. $D = {_fmt(diam_m)}\\text{{ m}}$ and $n = \\frac{{{rpm}}}{{60}} = {_fmt(rps, 2)}\\text{{ r/s}}$.\n"
        f"   $v = \\pi D n = \\pi \\times {_fmt(diam_m)} \\times {_fmt(rps, 2)} \\approx {_fmt(v_m_s, 2)}\\text{{ m/s}}$.\n"
        f"2. $v_{{\\text{{km/h}}}} = v_{{\\text{{m/s}}}} \\times 3{{,}}6 = {_fmt(v_m_s, 2)} \\times 3{{,}}6 = {_fmt(v_km_h, 1)}\\text{{ km/h}}$."
    )
    return _make_q(
        r, "46_vehicle_speed_from_wheel_diameter_and_rpm", 46, prompt, ans, sol, 3,
        ["divided_by_3_point_6_instead_of_multiplying_to_get_km_per_h"],
        [{"step": 1, "criterion": f"Speed v = {_fmt(v_m_s, 2)} m/s", "marks": 2}, {"step": 2, "criterion": f"Speed in km/h = {_fmt(v_km_h, 1)}", "marks": 1}],
        {"tier_1": "v = pi * D * (rpm / 60) in m/s. Multiply by 3.6 to convert m/s to km/h.", "tier_2": f"v = {_fmt(v_m_s, 2)} * 3.6.", "tier_3": ans},
    )


# 47. Wheel rpm required for prescribed vehicle road speed
def build_47_wheel_rpm_required_for_prescribed_vehicle_road_speed(r: random.Random) -> Dict[str, Any]:
    speed_kmh = r.choice([60, 80, 100, 120])
    diam_cm = r.choice([60, 65, 70])
    diam_m = diam_cm / 100.0
    v_ms = speed_kmh / 3.6
    # v = pi * D * n => n = v / (pi * D) in r/s => rpm = n * 60
    rps = v_ms / (math.pi * diam_m)
    rpm = int(round(rps * 60))
    prompt = (
        f"A truck travels along a straight highway at a steady speed of ${speed_kmh}\\text{{ km/h}}$.\n"
        f"The truck's tyres have an outside diameter of ${diam_cm}\\text{{ cm}}$.\n\n"
        f"Calculate the **rotational frequency** of the tyres in revolutions per minute ($\\text{{r/min}}$), "
        f"rounded to the nearest whole revolution."
    )
    ans = f"{rpm}\\text{{ r/min}}"
    sol = (
        f"$v = \\frac{{{speed_kmh}}}{{3{{,}}6}} = {_fmt(v_ms, 2)}\\text{{ m/s}}$.\n"
        f"Rotational frequency $n = \\frac{{v}}{{\\pi D}} = \\frac{{{_fmt(v_ms, 2)}}}{{\\pi \\times {_fmt(diam_m)}}} \\approx {_fmt(rps, 2)}\\text{{ r/s}}$.\n"
        f"$\\text{{Speed in r/min}} = {_fmt(rps, 2)} \\times 60 \\approx {rpm}\\text{{ r/min}}$."
    )
    return _make_q(
        r, "47_wheel_rpm_required_for_prescribed_vehicle_road_speed", 47, prompt, ans, sol, 3,
        ["forgot_to_convert_km_per_hour_to_m_per_second"],
        [{"step": 1, "criterion": f"v = {speed_kmh} / 3.6 = {_fmt(v_ms, 2)} m/s", "marks": 1}, {"step": 2, "criterion": f"n = v / (pi*D) = {_fmt(rps, 2)} r/s", "marks": 1}, {"step": 3, "criterion": f"rpm = {rpm} r/min", "marks": 1}],
        {"tier_1": "Divide km/h by 3.6 to get m/s, then use n = v / (pi * D). Multiply by 60 for rpm.", "tier_2": f"n = ({speed_kmh} / 3.6) / (pi * {diam_m}).", "tier_3": ans},
    )


# 48. Roller conveyor system material transport rate (with SVG)
def build_48_roller_conveyor_system_material_transport_rate_svg(r: random.Random) -> Dict[str, Any]:
    roller_diam_cm = r.choice([10, 12, 15, 20])
    roller_diam_m = roller_diam_cm / 100.0
    rpm = r.choice([60, 90, 120, 180])
    rps = rpm / 60.0
    v_lin = round(math.pi * roller_diam_m * rps, 2)
    len_conveyor = r.choice([15, 20, 25, 30])
    t_pass = round(len_conveyor / v_lin, 1)
    svg = _svg_rotating_wheel(roller_diam_m, rpm, show_tangent=True)
    prompt = (
        f"An automated assembly line parcel conveyor is powered by driving rollers of diameter $D = {roller_diam_cm}\\text{{ cm}}$ (shown schematically).\n"
        f"The rollers rotate at ${rpm}\\text{{ r/min}}$.\n\n"
        f"1. Calculate the linear transport speed ($v = \\pi D n$) of parcels on the conveyor in $\\text{{m/s}}$.\n"
        f"2. Calculate the time in seconds taken for a box to travel the entire ${len_conveyor}\\text{{ m}}$ length of the conveyor."
    )
    ans = f"v = {_fmt(v_lin)}\\text{{ m/s}},\\ t = {_fmt(t_pass, 1)}\\text{{ s}}"
    sol = (
        f"1. $v = \\pi D n = \\pi \\times {_fmt(roller_diam_m)} \\times \\left(\\frac{{{rpm}}}{{60}}\\right) \\approx {_fmt(v_lin)}\\text{{ m/s}}$.\n"
        f"2. Time $t = \\frac{{L}}{{v}} = \\frac{{{len_conveyor}}}{{{_fmt(v_lin)}}} = {_fmt(t_pass, 1)}\\text{{ seconds}}$."
    )
    return _make_q(
        r, "48_roller_conveyor_system_material_transport_rate_svg", 48, prompt, ans, sol, 3,
        ["multiplied_distance_by_speed_instead_of_dividing_for_time"],
        [{"step": 1, "criterion": f"v = {_fmt(v_lin)} m/s", "marks": 2}, {"step": 2, "criterion": f"t = {len_conveyor} / {_fmt(v_lin)} = {_fmt(t_pass, 1)} s", "marks": 1}],
        {"tier_1": "Calculate linear speed v = pi * D * n. Then time = distance / speed.", "tier_2": f"t = {len_conveyor} / {_fmt(v_lin)}.", "tier_3": ans},
        svg=svg,
    )


# 49. Motor to machine spindle belt reduction drive (with SVG)
def build_49_motor_to_machine_spindle_belt_reduction_drive_svg(r: random.Random) -> Dict[str, Any]:
    motor_rpm = 1440
    d_motor = 0.10  # 100 mm
    ratio = r.choice([2.0, 3.0, 4.0])
    d_spindle = round(d_motor * ratio, 2)
    spindle_rpm = round(motor_rpm / ratio)
    omega_spindle = round(2.0 * math.pi * (spindle_rpm / 60.0), 2)
    cutter_diam = r.choice([0.15, 0.20, 0.25])
    v_cutter = round((cutter_diam / 2.0) * omega_spindle, 2)
    svg = _svg_belt_pulley_drive(d_motor, d_spindle, crossed=False)
    prompt = (
        f"An electric motor running at ${motor_rpm}\\text{{ r/min}}$ has a drive pulley of diameter $D_1 = {_fmt(d_motor)}\\text{{ m}}$.\n"
        f"It drives a milling machine spindle pulley of diameter $D_2 = {_fmt(d_spindle)}\\text{{ m}}$ via a flat belt (illustrated in the diagram).\n"
        f"Mounted on the spindle shaft is a rotary milling cutter with an outside diameter of $D_{{\\text{{cutter}}}} = {_fmt(cutter_diam)}\\text{{ m}}$.\n\n"
        f"1. Calculate the rotational speed of the spindle ($n_2$) in $\\text{{r/min}}$.\n"
        f"2. Calculate the angular velocity $\\omega_2$ of the milling cutter in $\\text{{rad/s}}$.\n"
        f"3. Calculate the cutting speed ($v$) at the tip of the cutter teeth in $\\text{{m/s}}$."
    )
    ans = f"n_2 = {spindle_rpm}\\text{{ r/min}},\\ \\omega_2 = {_fmt(omega_spindle)}\\text{{ rad/s}},\\ v = {_fmt(v_cutter)}\\text{{ m/s}}"
    sol = (
        f"1. $n_2 = n_1 \\times \\frac{{D_1}}{{D_2}} = {motor_rpm} \\times \\frac{{{_fmt(d_motor)}}}{{{_fmt(d_spindle)}}} = {spindle_rpm}\\text{{ r/min}}$.\n"
        f"2. $\\omega_2 = 2\\pi \\left(\\frac{{{spindle_rpm}}}{{60}}\\right) = {_fmt(omega_spindle)}\\text{{ rad/s}}$.\n"
        f"3. $v = \\omega_2 \\times r_{{\\text{{cutter}}}} = {_fmt(omega_spindle)} \\times {_fmt(cutter_diam / 2.0)} = {_fmt(v_cutter)}\\text{{ m/s}}$."
    )
    return _make_q(
        r, "49_motor_to_machine_spindle_belt_reduction_drive_svg", 49, prompt, ans, sol, 4,
        ["applied_belt_pulley_ratio_to_cutter_diameter_incorrectly"],
        [{"step": 1, "criterion": f"Spindle speed n2 = {spindle_rpm} r/min", "marks": 1}, {"step": 2, "criterion": f"omega2 = {_fmt(omega_spindle)} rad/s", "marks": 1}, {"step": 3, "criterion": f"Cutting speed v = {_fmt(v_cutter)} m/s", "marks": 2}],
        {"tier_1": "First find spindle rpm using D1*n1 = D2*n2. Then find omega2 and finally v = omega2 * (D_cutter / 2).", "tier_2": f"n2 = {motor_rpm} * ({_fmt(d_motor)} / {_fmt(d_spindle)}).", "tier_3": ans},
        svg=svg,
    )


# 50. Angular movement diagnostic autopsy and misconception repair
def build_50_angular_movement_diagnostic_autopsy_and_misconception_repair(r: random.Random) -> Dict[str, Any]:
    rpm = r.choice([600, 900, 1200, 1800])
    diam_m = r.choice([0.4, 0.5, 0.6, 0.8])
    rps = rpm / 60.0
    true_omega = round(2.0 * math.pi * rps, 2)
    radius_m = diam_m / 2.0
    true_v = round(true_omega * radius_m, 2)
    wrong_omega = round(2.0 * math.pi * rpm, 2)
    wrong_v = round(wrong_omega * diam_m, 2)
    prompt = (
        f"A learner is given a rotating flywheel of diameter $D = {_fmt(diam_m)}\\text{{ m}}$ rotating at ${rpm}\\text{{ r/min}}$:\n"
        f"• **Learner's Step 1:** Calculates $\\omega = 2\\pi \\times {rpm} = {_fmt(wrong_omega)}\\text{{ rad/s}}$ (omitted dividing rpm by 60).\n"
        f"• **Learner's Step 2:** Calculates linear velocity $v = \\omega \\times D = {_fmt(wrong_omega)} \\times {_fmt(diam_m)} = {_fmt(wrong_v)}\\text{{ m/s}}$ (used diameter instead of radius).\n\n"
        f"1. Identify the conceptual error in Step 1 and calculate the **correct angular velocity** $\\omega$ in $\\text{{rad/s}}$.\n"
        f"2. Identify the conceptual error in Step 2 and calculate the **correct circumferential linear velocity** $v$ in $\\text{{m/s}}$."
    )
    ans = f"\\omega = {_fmt(true_omega)}\\text{{ rad/s}},\\ v = {_fmt(true_v)}\\text{{ m/s}}"
    sol = (
        f"1. In Step 1, rotational frequency must be in revolutions per second ($n = \\frac{{{rpm}}}{{60}} = {_fmt(rps)}\\text{{ r/s}}$). "
        f"Correct angular velocity: $\\omega = 2\\pi n = 2\\pi({_fmt(rps)}) = {_fmt(true_omega)}\\text{{ rad/s}}$.\n"
        f"2. In Step 2, $v = \\omega r$, where $r = \\frac{{D}}{{2}} = {_fmt(radius_m)}\\text{{ m}}$ (not $D$). "
        f"Correct linear velocity: $v = {_fmt(true_omega)} \\times {_fmt(radius_m)} = {_fmt(true_v)}\\text{{ m/s}}$."
    )
    return _make_q(
        r, "50_angular_movement_diagnostic_autopsy_and_misconception_repair", 50, prompt, ans, sol, 4,
        ["rpm_to_rps_conversion_error", "used_diameter_instead_of_radius_in_v_equals_omega_r"],
        [{"step": 1, "criterion": "Identified rpm/60 error", "marks": 1}, {"step": 2, "criterion": f"Correct omega = {_fmt(true_omega)} rad/s", "marks": 1}, {"step": 3, "criterion": "Identified radius vs diameter error", "marks": 1}, {"step": 4, "criterion": f"Correct v = {_fmt(true_v)} m/s", "marks": 1}],
        {"tier_1": "Divide rpm by 60 before calculating omega = 2*pi*n, and halve diameter to find radius in v = omega*r.", "tier_2": f"omega = 2*pi*({rpm}/60); v = omega * ({diam_m}/2).", "tier_3": ans},
    )


ARCHETYPES_26_50 = {
    "26_rotational_frequency_rpm_to_rps_conversion": build_26_rotational_frequency_rpm_to_rps_conversion,
    "27_angular_velocity_from_rotational_frequency_rad_per_sec": build_27_angular_velocity_from_rotational_frequency_rad_per_sec,
    "28_rotational_frequency_and_rpm_from_angular_velocity": build_28_rotational_frequency_and_rpm_from_angular_velocity,
    "29_angular_displacement_from_angular_velocity_and_time": build_29_angular_displacement_from_angular_velocity_and_time,
    "30_time_taken_for_specified_number_of_revolutions": build_30_time_taken_for_specified_number_of_revolutions,
    "31_circumferential_linear_velocity_from_radius_and_omega_svg": build_31_circumferential_linear_velocity_from_radius_and_omega_svg,
    "32_circumferential_linear_velocity_from_diameter_and_rpm_svg": build_32_circumferential_linear_velocity_from_diameter_and_rpm_svg,
    "33_find_radius_or_diameter_from_linear_and_angular_velocity_svg": build_33_find_radius_or_diameter_from_linear_and_angular_velocity_svg,
    "34_linear_speed_of_clock_hand_tip_svg": build_34_linear_speed_of_clock_hand_tip_svg,
    "35_centripetal_acceleration_on_rotating_rim_svg": build_35_centripetal_acceleration_on_rotating_rim_svg,
    "36_belt_and_pulley_drive_equal_linear_speed_svg": build_36_belt_and_pulley_drive_equal_linear_speed_svg,
    "37_belt_drive_calculate_required_driver_pulley_diameter_svg": build_37_belt_drive_calculate_required_driver_pulley_diameter_svg,
    "38_stepped_cone_pulley_transmission_speed_ratios_svg": build_38_stepped_cone_pulley_transmission_speed_ratios_svg,
    "39_crossed_belt_drive_direction_and_angular_speed_svg": build_39_crossed_belt_drive_direction_and_angular_speed_svg,
    "40_belt_linear_speed_and_travel_distance_svg": build_40_belt_linear_speed_and_travel_distance_svg,
    "41_meshed_spur_gears_velocity_ratio_and_teeth_count_svg": build_41_meshed_spur_gears_velocity_ratio_and_teeth_count_svg,
    "42_compound_gear_train_overall_velocity_ratio_svg": build_42_compound_gear_train_overall_velocity_ratio_svg,
    "43_internal_annular_gear_and_pinion_speed_ratio_svg": build_43_internal_annular_gear_and_pinion_speed_ratio_svg,
    "44_rack_and_pinion_linear_traverse_velocity_svg": build_44_rack_and_pinion_linear_traverse_velocity_svg,
    "45_winch_hoist_drum_cable_winding_linear_speed_svg": build_45_winch_hoist_drum_cable_winding_linear_speed_svg,
    "46_vehicle_speed_from_wheel_diameter_and_rpm": build_46_vehicle_speed_from_wheel_diameter_and_rpm,
    "47_wheel_rpm_required_for_prescribed_vehicle_road_speed": build_47_wheel_rpm_required_for_prescribed_vehicle_road_speed,
    "48_roller_conveyor_system_material_transport_rate_svg": build_48_roller_conveyor_system_material_transport_rate_svg,
    "49_motor_to_machine_spindle_belt_reduction_drive_svg": build_49_motor_to_machine_spindle_belt_reduction_drive_svg,
    "50_angular_movement_diagnostic_autopsy_and_misconception_repair": build_50_angular_movement_diagnostic_autopsy_and_misconception_repair,
}
