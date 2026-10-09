"""Grade 10 Physical Sciences — 1D Motion & Mechanical Energy Generator.
Deterministic 6-pillar CAPS question generator covering Paper 1 (Physics Term 3):
- Vectors vs scalars: displacement vs distance, velocity vs speed.
- Equations of motion in one dimension:
  vf = vi + a * Delta t
  Delta x = vi * Delta t + 1/2 a (Delta t)^2
  vf^2 = vi^2 + 2 a Delta x
  Delta x = ((vi + vf) / 2) * Delta t
- Velocity-time graphs: gradient = acceleration, area under graph = displacement.
- Gravitational potential energy: Ep = m * g * h (g = 9.8 m/s^2).
- Kinetic energy: Ek = 1/2 m v^2.
- Conservation of mechanical energy: (Ek + Ep)_top = (Ek + Ep)_bottom (isolated system).

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
    return s.replace(".", "{{,}}")


G_VAL = 9.8


def _build_kinematics_drill(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([0.0, 5.0, 10.0, 15.0])
    a = r.choice([1.5, 2.0, 2.5, 3.0, 4.0])
    t = r.choice([4.0, 5.0, 6.0, 8.0])

    vf = round(vi + a * t, 2)
    dx = round(vi * t + 0.5 * a * (t**2), 2)

    prompt = (
        f"A car accelerates uniformly along a straight horizontal road from an initial velocity of "
        f"**${_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$** at a constant acceleration of "
        f"**${_fmt_sa(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$** for **${_fmt_sa(t)}\\text{{ seconds}}$**.\n\n"
        f"1. Define the term *acceleration*.\n"
        f"2. Calculate the final velocity ($v_f$) of the car at $t = {_fmt_sa(t)}\\text{{ s}}$.\n"
        f"3. Calculate the total displacement ($\\Delta x$) of the car during this time interval."
    )

    sol = (
        f"1. **Acceleration:** The rate of change of velocity ($a = \\frac{{\\Delta v}}{{\\Delta t}}$).\n\n"
        f"2. $v_f = v_i + a \\Delta t$\n"
        f"   $v_f = {_fmt_sa(vi)} + ({_fmt_sa(a)})({_fmt_sa(t)}) = {_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n\n"
        f"3. $\\Delta x = v_i \\Delta t + \\frac{{1}}{{2}} a (\\Delta t)^2$\n"
        f"   $\\Delta x = ({_fmt_sa(vi)})({_fmt_sa(t)}) + \\frac{{1}}{{2}}({_fmt_sa(a)})({_fmt_sa(t)})^2$\n"
        f"   $\\Delta x = {round(vi * t, 2)} + {round(0.5 * a * (t**2), 2)} = {_fmt_sa(dx)}\\text{{ m}}$"
    )

    return {
        "id": f"g10_ps_mot_kin_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"vf={_fmt_sa(vf)} m/s, dx={_fmt_sa(dx)} m",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: Rate of change of velocity", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula: vf = vi + a * dt", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate vf = {_fmt_sa(vf)} m/s", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Formula: dx = vi * dt + 0.5 * a * dt^2", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculate dx = {_fmt_sa(dx)} m", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_braking_acceleration", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Use the standard equations of motion: $v_f = v_i + a\\Delta t$ and $\\Delta x = v_i\\Delta t + \\frac{1}{2}a(\\Delta t)^2$.",
            "tier_2": "Substitute given values directly: $v_i = {_fmt_sa(vi)}$, $a = {_fmt_sa(a)}$, and $\\Delta t = {_fmt_sa(t)}$.",
            "tier_3": f"$v_f = {_fmt_sa(vf)}\\text{{ m/s}}$. $\\Delta x = {_fmt_sa(dx)}\\text{{ m}}$.",
        },
        "misconception_tags": ["sign_error_braking_acceleration", "confused_distance_and_displacement"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def _build_mechanical_energy_drill(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([2.0, 5.0, 10.0, 20.0, 50.0])
    h_initial = r.choice([5.0, 10.0, 15.0, 20.0])

    ep_top = round(mass * G_VAL * h_initial, 1)
    # Released from rest at top: Ek_top = 0 => E_mech = Ep_top
    # At ground: Ep_bottom = 0 => Ek_bottom = Ep_top => 0.5 * m * v^2 = Ep_top
    v_bottom = round(math.sqrt(2 * G_VAL * h_initial), 2)
    ek_bottom = ep_top

    prompt = (
        f"A frictionless trolley of mass **${_fmt_sa(mass)}\\text{{ kg}}$** is released from rest at the top of an inclined "
        f"track at a vertical height of **${_fmt_sa(h_initial)}\\text{{ m}}$** above the ground.\n"
        f"Assume air resistance and friction are negligible ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"1. State the **Law of Conservation of Mechanical Energy**.\n"
        f"2. Calculate the gravitational potential energy ($E_p$) of the trolley at the top of the track.\n"
        f"3. State the kinetic energy ($E_k$) of the trolley at the moment of release.\n"
        f"4. Use energy principles to calculate the speed ($v$) of the trolley when it reaches the bottom of the track."
    )

    sol = (
        f"1. **Law of Conservation of Mechanical Energy:** In an isolated system (where only conservative forces act), the total mechanical energy remains constant ($E_{{\\text{{mech}}}} = E_k + E_p = \\text{{constant}}$).\n\n"
        f"2. $E_p = m g h = ({_fmt_sa(mass)})(9{{,}}8)({_fmt_sa(h_initial)}) = {_fmt_sa(ep_top)}\\text{{ J}}$\n\n"
        f"3. Since the trolley is released from rest ($v = 0$), $E_k = 0\\text{{ J}}$.\n\n"
        f"4. $(E_k + E_p)_{{\\text{{top}}}} = (E_k + E_p)_{{\\text{{bottom}}}}$\n"
        f"   $0 + {_fmt_sa(ep_top)} = \\frac{{1}}{{2}} m v^2 + 0$\n"
        f"   ${_fmt_sa(ep_top)} = \\frac{{1}}{{2}} ({_fmt_sa(mass)}) v^2$\n"
        f"   $v^2 = \\frac{{2 \\times {_fmt_sa(ep_top)}}}{{{_fmt_sa(mass)}}} = {round(2 * G_VAL * h_initial, 2)}$\n"
        f"   $v = \\sqrt{{{round(2 * G_VAL * h_initial, 2)}}} = {_fmt_sa(v_bottom)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    )

    return {
        "id": f"g10_ps_energy_mech_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Ep={_fmt_sa(ep_top)} J, v={_fmt_sa(v_bottom)} m/s",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Statement of Conservation of Mechanical Energy", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula: Ep = m * g * h", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate Ep = {_fmt_sa(ep_top)} J", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Identify Ek_top = 0 J", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Equate mechanical energy: (Ek + Ep)top = (Ek + Ep)bottom", "marks": 1, "editable": True},
                {"id": "mp6", "desc": f"Calculate v = {_fmt_sa(v_bottom)} m/s", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "forgot_squaring_velocity_ek", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "$E_p = mgh$ and $E_k = \\frac{1}{2}mv^2$.",
            "tier_2": "In the absence of friction, all potential energy at the top converts into kinetic energy at the bottom: $mgh = \\frac{1}{2}mv^2$.",
            "tier_3": f"$E_p = {_fmt_sa(ep_top)}\\text{{ J}}$. Speed at bottom: $v = \\sqrt{{2gh}} = {_fmt_sa(v_bottom)}\\text{{ m/s}}$.",
        },
        "misconception_tags": ["forgot_squaring_velocity_ek", "gravity_g_omitted_or_wrong_sign"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)
    if mode == "elementary_kinematics":
        return _build_kinematics_drill(r)
    elif mode == "elementary_energy":
        return _build_mechanical_energy_drill(r)
    else:
        choice = r.choice(["kinematics", "energy"])
        if choice == "kinematics":
            return _build_kinematics_drill(r)
        else:
            return _build_mechanical_energy_drill(r)
