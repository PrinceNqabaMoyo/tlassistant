"""Grade 10–12 Technical Mathematics — Circles, Angles & Angular Movement Generator.
Deterministic 6-pillar CAPS question generator covering Paper 2 (Term 3):
- Radian and degree angle conversions: theta_rad = theta_deg * (pi / 180).
- Arc length: s = r * theta (theta in radians).
- Area of circular sector: Area = 1/2 * r^2 * theta (theta in radians).
- Area of segment: Area = 1/2 * r^2 * (theta - sin(theta)).
- Angular velocity: omega = theta / t = 2 * pi * n (where n is frequency in rev/s).
- Circumferential / linear velocity: v = r * omega.

Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _build_arc_sector_drill(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([5.0, 6.0, 8.0, 10.0, 12.0, 14.0, 15.0])
    deg_angle = r.choice([30, 45, 60, 90, 120, 135, 150])

    rad_angle = round(deg_angle * (math.pi / 180.0), 3)
    arc_length = round(radius * (deg_angle * (math.pi / 180.0)), 2)
    sector_area = round(0.5 * (radius**2) * (deg_angle * (math.pi / 180.0)), 2)

    prompt = (
        f"A circular disc has a radius of **${_fmt_sa(radius)}\\text{{ cm}}$**. "
        f"A sector of the circle subtends a central angle of **${deg_angle}^\\circ$**.\n\n"
        f"1. Convert the central angle of ${deg_angle}^\\circ$ to radians (leave your answer in terms of $\\pi$ and as a decimal rounded to two decimal places).\n"
        f"2. Calculate the arc length ($s$) bounding the sector.\n"
        f"3. Calculate the area ($A$) of the circular sector."
    )

    sol = (
        f"1. $\\theta = {deg_angle}^\\circ \\times \\frac{{\\pi}}{{180^\\circ}} = \\frac{{{deg_angle}}}{{180}}\\pi = {_fmt_sa(round(deg_angle * math.pi / 180.0, 2))}\\text{{ rad}}$\n\n"
        f"2. $s = r \\theta = {_fmt_sa(radius)} \\times ({deg_angle} \\times \\frac{{\\pi}}{{180}}) = {_fmt_sa(arc_length)}\\text{{ cm}}$\n\n"
        f"3. $\\text{{Area}} = \\frac{{1}}{{2}} r^2 \\theta = \\frac{{1}}{{2}} ({_fmt_sa(radius)})^2 \\times ({deg_angle} \\times \\frac{{\\pi}}{{180}}) = {_fmt_sa(sector_area)}\\text{{ cm}}^2$"
    )

    return {
        "id": f"tech_math_arc_sec_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"theta={_fmt_sa(round(deg_angle * math.pi / 180.0, 2))} rad, s={_fmt_sa(arc_length)} cm, Area={_fmt_sa(sector_area)} cm2",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Convert degrees to radians: theta = deg * pi / 180", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Angle in radians: {_fmt_sa(round(deg_angle * math.pi / 180.0, 2))} rad", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate arc length s = {_fmt_sa(arc_length)} cm", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Formula: Area = 0.5 * r^2 * theta", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculate sector area = {_fmt_sa(sector_area)} cm2", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "used_degrees_in_arc_length_formula", "penalty": -2}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Angles MUST be converted to radians before calculating arc length ($s = r\\theta$) and sector area ($A = \\frac{1}{2}r^2\\theta$).",
            "tier_2": "$\\theta = \\text{degrees} \\times \\frac{\\pi}{180}$.",
            "tier_3": f"$\\theta = {_fmt_sa(round(deg_angle * math.pi / 180.0, 2))}\\text{{ rad}}$. $s = {_fmt_sa(arc_length)}\\text{{ cm}}$. Area = {_fmt_sa(sector_area)}\\text{{ cm}}^2.",
        },
        "misconception_tags": ["used_degrees_in_arc_length_formula", "forgot_half_in_sector_area"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def _build_angular_velocity_drill(r: random.Random) -> Dict[str, Any]:
    diameter = r.choice([0.4, 0.5, 0.6, 0.8, 1.0, 1.2])  # in meters
    radius = diameter / 2.0
    rpm = r.choice([300, 600, 900, 1200, 1500, 1800])  # rev / min

    rps = rpm / 60.0  # rev / s
    omega = round(2.0 * math.pi * rps, 2)  # rad / s
    v_linear = round(radius * omega, 2)  # m / s

    prompt = (
        f"A circular milling machine blade has a diameter of **${_fmt_sa(diameter)}\\text{{ m}}$**.\n"
        f"The blade rotates at a constant rotational frequency of **${rpm}\\text{{ r/min}}$** (revolutions per minute).\n\n"
        f"1. Calculate the rotational frequency ($n$) in revolutions per second ($\\text{{r/s}}$).\n"
        f"2. Calculate the angular velocity ($\\omega$) of the blade in radians per second ($\\text{{rad}}\\cdot\\text{{s}}^{{-1}}$).\n"
        f"3. Calculate the linear circumferential speed ($v$) of a cutting tooth on the outer rim of the blade."
    )

    sol = (
        f"1. $n = \\frac{{{rpm}}}{{60}} = {_fmt_sa(rps)}\\text{{ r/s}}$\n\n"
        f"2. $\\omega = 2\\pi n = 2 \\times \\pi \\times {_fmt_sa(rps)} = {_fmt_sa(omega)}\\text{{ rad}}\\cdot\\text{{s}}^{{-1}}$\n\n"
        f"3. Radius $r = \\frac{{{_fmt_sa(diameter)}}}{{2}} = {_fmt_sa(radius)}\\text{{ m}}$\n"
        f"   $v = r \\omega = {_fmt_sa(radius)} \\times {_fmt_sa(omega)} = {_fmt_sa(v_linear)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    )

    return {
        "id": f"tech_math_ang_vel_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"n={_fmt_sa(rps)} r/s, omega={_fmt_sa(omega)} rad/s, v={_fmt_sa(v_linear)} m/s",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Convert r/min to r/s: n = {rpm}/60 = {_fmt_sa(rps)} r/s", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula: omega = 2 * pi * n", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate omega = {_fmt_sa(omega)} rad/s", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculate radius r = d/2 = {_fmt_sa(radius)} m", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculate linear speed v = r * omega = {_fmt_sa(v_linear)} m/s", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "rpm_to_rps_conversion_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Convert r/min to r/s by dividing by 60. Then $\\omega = 2\\pi n$ and $v = r\\omega$.",
            "tier_2": "Ensure diameter is halved to obtain radius before calculating linear speed.",
            "tier_3": f"$n = {_fmt_sa(rps)}\\text{{ r/s}}$. $\\omega = {_fmt_sa(omega)}\\text{{ rad/s}}$. $v = {_fmt_sa(v_linear)}\\text{{ m/s}}$.",
        },
        "misconception_tags": ["rpm_to_rps_conversion_error", "confused_angular_and_linear_velocity"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)
    if mode == "elementary_arc_sector":
        return _build_arc_sector_drill(r)
    elif mode == "elementary_angular_velocity":
        return _build_angular_velocity_drill(r)
    else:
        choice = r.choice(["arc_sec", "ang_vel"])
        if choice == "arc_sec":
            return _build_arc_sector_drill(r)
        else:
            return _build_angular_velocity_drill(r)
