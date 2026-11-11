"""Grade 10–12 Technical Mathematics — Circles, Angles & Angular Movement Generator.
Deterministic 6-pillar question generator covering Paper 2 (Term 3):
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

try:
    from app.utils.physical_sciences.physical_sciences_builders import build_hydraulic_gears_belt_pulley_question
except ImportError:
    from ..physical_sciences.physical_sciences_builders import build_hydraulic_gears_belt_pulley_question


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _build_arc_sector_drill(r: random.Random) -> Dict[str, Any]:
    radius = r.choice([5.0, 6.0, 8.0, 10.0, 12.0, 14.0, 15.0])
    deg_angle = r.choice([30, 45, 60, 90, 120, 135, 150])

    rad_val = round(deg_angle * (math.pi / 180.0), 2)
    arc_length = round(radius * (deg_angle * (math.pi / 180.0)), 2)
    sector_area = round(0.5 * (radius**2) * (deg_angle * (math.pi / 180.0)), 2)

    prompt = (
        f"Refer to the circular sector diagram with centre \\(O\\) and radius \\(r = {_fmt_sa(radius)}\\text{{ cm}}\\), "
        f"subtending a central angle of \\(\\theta = {deg_angle}^\\circ\\).\n\n"
        f"1. Convert the central angle of \\({deg_angle}^\\circ\\) to radians (rounded to two decimal places).\n"
        f"2. Calculate the arc length (\\(s\\)) bounding the sector.\n"
        f"3. Calculate the area (\\(A\\)) of the circular sector \\(OAB\\)."
    )

    sol = (
        f"Step 1: Convert central angle θ from degrees to radians:\n"
        f"θ = {deg_angle}° × (π ÷ 180°) = {_fmt_sa(rad_val)} rad\n\n"
        f"Step 2: Calculate arc length s = r × θ:\n"
        f"s = {_fmt_sa(radius)} × ({deg_angle} × π ÷ 180) = {_fmt_sa(arc_length)} cm\n\n"
        f"Step 3: Calculate sector area A = 0,5 × r² × θ:\n"
        f"Area = 0,5 × ({_fmt_sa(radius)})² × ({deg_angle} × π ÷ 180) = {_fmt_sa(sector_area)} cm²"
    )

    rad_norm = 3.0
    rad_rad = deg_angle * math.pi / 180.0
    bx = round(rad_norm * math.cos(rad_rad), 2)
    by = round(rad_norm * math.sin(rad_rad), 2)
    diagram_spec = {
        "kind": "radian_sector",
        "radius": rad_norm,
        "radius_label": _fmt_sa(radius),
        "deg_angle": deg_angle,
        "rad_label": "θ rad",
        "arc_label": "s",
        "unit": "cm",
        "center": "O",
        "points": {
            "O": [0.0, 0.0],
            "A": [rad_norm, 0.0],
            "B": [bx, by],
        },
        "vertex_labels": {
            "O": "O",
            "A": "A",
            "B": "B",
        },
        "chords": [["O", "A"], ["O", "B"]],
        "angles": [
            {"vertex": "O", "p1": "A", "p2": "B", "label": f"{deg_angle}°", "size": 1.0}
        ],
    }

    return {
        "id": f"tech_math_arc_sec_{r.randint(10000, 99999)}",
        "type": "compound",
        "modality": "diagram",
        "diagram_spec": diagram_spec,
        "prompt": prompt,
        "correct_answer": sol,
        "sample_answer": sol,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "1a. Formula to convert degrees to radians: θ = deg × π ÷ 180", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"1b. Angle in radians: θ = {_fmt_sa(rad_val)} rad", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"2. Arc length s = r × θ = {_fmt_sa(arc_length)} cm", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "3a. Sector area formula: Area = 0,5 × r² × θ", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"3b. Sector area = {_fmt_sa(sector_area)} cm²", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "used_degrees_in_arc_length_formula", "penalty": -2}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Angles must be converted to radians before calculating arc length (s = rθ) and sector area (A = 0,5 r² θ).",
            "tier_2": "θ (rad) = degrees × π ÷ 180.",
            "tier_3": f"θ = {_fmt_sa(rad_val)} rad; s = {_fmt_sa(arc_length)} cm; Area = {_fmt_sa(sector_area)} cm².",
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
        f"A circular milling machine blade has a diameter of \\({_fmt_sa(diameter)}\\text{{ m}}\\).\n"
        f"The blade rotates at a constant rotational frequency of \\({rpm}\\text{{ r/min}}\\) (revolutions per minute).\n\n"
        f"1. Calculate the rotational frequency (\\(n\\)) in revolutions per second (\\(\\text{{r/s}}\\)).\n"
        f"2. Calculate the angular velocity (\\(\\omega\\)) of the blade in radians per second (\\(\\text{{rad}}\\cdot\\text{{s}}^{{-1}}\\)).\n"
        f"3. Calculate the linear circumferential speed (\\(v\\)) of a cutting tooth on the outer rim of the blade."
    )

    sol = (
        f"Step 1: Convert rotational frequency from r/min to r/s:\n"
        f"n = {rpm} ÷ 60 = {_fmt_sa(rps)} r/s\n\n"
        f"Step 2: Calculate angular velocity ω = 2πn:\n"
        f"ω = 2 × π × {_fmt_sa(rps)} = {_fmt_sa(omega)} rad·s⁻¹\n\n"
        f"Step 3: Calculate radius r and linear circumferential speed v = rω:\n"
        f"r = {_fmt_sa(diameter)} ÷ 2 = {_fmt_sa(radius)} m\n"
        f"v = {_fmt_sa(radius)} × {_fmt_sa(omega)} = {_fmt_sa(v_linear)} m·s⁻¹"
    )

    rad_norm = 3.0
    deg_angle = 90
    diagram_spec = {
        "kind": "radian_sector",
        "radius": rad_norm,
        "radius_label": _fmt_sa(radius),
        "deg_angle": deg_angle,
        "rad_label": "θ rad",
        "arc_label": "v = rω",
        "unit": "m",
        "center": "O",
        "points": {
            "O": [0.0, 0.0],
            "P": [rad_norm, 0.0],
            "Q": [0.0, rad_norm],
        },
        "vertex_labels": {
            "O": "O (Center)",
            "P": "P (Rim)",
            "Q": "Q",
        },
        "chords": [["O", "P"]],
        "angles": [
            {"vertex": "O", "p1": "P", "p2": "Q", "label": "90°", "size": 0.8}
        ],
    }

    return {
        "id": f"tech_math_ang_vel_{r.randint(10000, 99999)}",
        "type": "compound",
        "modality": "diagram",
        "diagram_spec": diagram_spec,
        "prompt": prompt,
        "correct_answer": sol,
        "sample_answer": sol,
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"1. Convert r/min to r/s: n = {rpm} ÷ 60 = {_fmt_sa(rps)} r/s", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "2a. Formula: ω = 2 × π × n", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"2b. Calculate ω = {_fmt_sa(omega)} rad·s⁻¹", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"3a. Calculate radius r = d ÷ 2 = {_fmt_sa(radius)} m", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"3b. Calculate linear speed v = r × ω = {_fmt_sa(v_linear)} m·s⁻¹", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "rpm_to_rps_conversion_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Convert r/min to r/s by dividing by 60. Then ω = 2πn and v = rω.",
            "tier_2": "Ensure diameter is halved to obtain radius before calculating linear speed.",
            "tier_3": f"n = {_fmt_sa(rps)} r/s; ω = {_fmt_sa(omega)} rad·s⁻¹; v = {_fmt_sa(v_linear)} m·s⁻¹.",
        },
        "misconception_tags": ["rpm_to_rps_conversion_error", "confused_angular_and_linear_velocity"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)
    if mode == "elementary_arc_sector" or kwargs.get("subskill") in ("radian_sector", "arc_sector", "sector"):
        return _build_arc_sector_drill(r)
    elif mode == "elementary_angular_velocity" or kwargs.get("subskill") in ("angular_velocity", "velocity"):
        return _build_angular_velocity_drill(r)
    elif mode in ("hydraulic_gears_belt_pulley", "gears_pulleys") or kwargs.get("subskill") in ("hydraulic_gears_belt_pulley", "gears_pulleys", "gears", "hydraulics"):
        return build_hydraulic_gears_belt_pulley_question(seed=r.randint(1000, 9999), grade=10)
    else:
        choice = r.choice(["arc_sec", "ang_vel"])
        if choice == "arc_sec":
            return _build_arc_sector_drill(r)
        else:
            return _build_angular_velocity_drill(r)

# diagram_role: context (math / ems declarative context visualization)
