"""Physical Sciences (Grade 12 Term 1) — Work, Energy and Power Archetypes 26 to 50.

Grounded strictly in the South African National Physical Sciences Curriculum:
- Conservative and non-conservative forces, path dependence.
- Work done by non-conservative forces theorem: W_nc = Delta E_k + Delta E_p.
- Applications on horizontal, inclined, and curved tracks with friction.
- Conservation of mechanical energy in isolated systems.
- Power: P = W / Delta t, P_ave = F * v_ave.
- Pumps, hoists, vehicles, efficiency, and kilowatt-hours (kWh).
- Multi-stage capstone synthesis and diagnostic autopsy.

100% deterministic, math backed, zero-LLM, compliant with 6-pillar contract.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict

G_ACCEL = 9.8  # m/s^2


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    """Format number with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and abs(val - round(val)) < 1e-6):
        return str(int(round(val)))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _clean_svg(svg: str) -> str:
    return svg.strip()


# Archetype 26: Conservative forces and path independence
def _b26_conservative_forces_and_path_independence(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([3.0, 5.0, 8.0, 10.0, 12.0])
    h_m = r.choice([2.5, 3.0, 4.0, 5.0, 6.0])
    w_g = mass_kg * G_ACCEL * h_m

    prompt = (
        f"A laboratory cart of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is raised from vertical position $y = 0\\text{{ m}}$ "
        f"to height $h = {_fmt_sa(h_m)}\\text{{ m}}$ above the floor ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"In trial 1, the cart is lifted vertically straight upward.\n"
        f"In trial 2, the cart is pushed up a frictionless ramp of length $L = {_fmt_sa(h_m * 2)}\\text{{ m}}$ to the same height $h$.\n\n"
        f"1. Define a **conservative force** in words.\n"
        f"2. Calculate the work done by the gravitational force on the cart during trial 1 and trial 2.\n"
        f"3. State what conclusion can be drawn regarding the work done by gravity around any closed path."
    )

    ans_latex = (
        rf"1.\; \text{{A force is conservative if the work done by the force on an object moving between two points is independent of the path taken.}}\n"
        rf"2.\; \text{{Trial 1 (vertical upward): }} W_g = m g \Delta y \cos(180^\circ) = ({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(h_m)})(-1) = -{_fmt_sa(w_g, 2)}\text{{ J}}.\n"
        rf"\quad \text{{Trial 2 (ramp upward): }} W_g = m g L \cos(90^\circ + \theta) = -m g h = -{_fmt_sa(w_g, 2)}\text{{ J}}.\n"
        rf"3.\; \text{{The work done by a conservative force on an object moving along any closed path is zero (0 J).}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of conservative force (path independence)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Work by gravity trial 1: -{_fmt_sa(w_g, 2)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Work by gravity trial 2: -{_fmt_sa(w_g, 2)} J (same value)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Closed path statement: zero work around closed path", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_negative_sign_upward_gravity", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "A conservative force depends only on initial and final positions, not on path length.",
        "tier_2": "Because displacement is upward and gravity acts downward, work done by gravity is negative: $W_g = -mgh$.",
        "tier_3": f"Work in both paths is $-{_fmt_sa(w_g, 2)}\\text{{ J}}$. Around a closed path, $\\oint F_g \\cdot dr = 0\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_26_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_26_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "26_conservative_forces_and_path_independence",
        "learning_objective_id": "ps_wep_26_conservative_definition",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_conservative_with_constant_force", "believed_ramp_requires_more_gravity_work"],
        "keywords": ["conservative force", "path independence", "closed path", "gravity"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 27: Non-conservative forces and path dependence
def _b27_non_conservative_forces_and_path_dependence(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([4.0, 6.0, 10.0, 15.0])
    mu_k = r.choice([0.20, 0.25, 0.30, 0.35])
    f_k = mu_k * mass_kg * G_ACCEL
    dist_1 = r.choice([3.0, 4.0, 5.0])
    dist_2 = dist_1 * r.choice([1.5, 2.0, 2.5])

    w_f1 = -f_k * dist_1
    w_f2 = -f_k * dist_2

    prompt = (
        f"A heavy crate of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is pushed across a rough horizontal floor where "
        f"the coefficient of kinetic friction is $\\mu_k = {_fmt_sa(mu_k)}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"The crate is moved from point A to point B:\n"
        f"- Path 1 is a direct straight path of length $d_1 = {_fmt_sa(dist_1)}\\text{{ m}}$.\n"
        f"- Path 2 is a curved, detour route of total length $d_2 = {_fmt_sa(dist_2)}\\text{{ m}}$.\n\n"
        f"1. Define a **non-conservative force** in words.\n"
        f"2. Calculate the magnitude of the kinetic friction force $f_k$ acting on the crate.\n"
        f"3. Calculate the work done by friction along Path 1 and along Path 2.\n"
        f"4. State why kinetic friction is classified as a non-conservative force based on your answers."
    )

    ans_latex = (
        rf"1.\; \text{{A force for which the work done in moving an object between two points depends on the path taken.}}\n"
        rf"2.\; f_k = \mu_k N = \mu_k m g = ({_fmt_sa(mu_k)})({_fmt_sa(mass_kg)})(9{{,}}8) = {_fmt_sa(f_k, 2)}\text{{ N}}.\n"
        rf"3.\; W_{{f,1}} = f_k d_1 \cos(180^\circ) = ({_fmt_sa(f_k, 2)})({_fmt_sa(dist_1)})(-1) = {_fmt_sa(w_f1, 2)}\text{{ J}}.\n"
        rf"\quad W_{{f,2}} = f_k d_2 \cos(180^\circ) = ({_fmt_sa(f_k, 2)})({_fmt_sa(dist_2)})(-1) = {_fmt_sa(w_f2, 2)}\text{{ J}}.\n"
        rf"4.\; \text{{The work done by friction depends on the length of the path taken (more work is done on the longer path), so friction is non-conservative.}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of non-conservative force", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculation of friction force: {_fmt_sa(f_k, 2)} N", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Work along Path 1: {_fmt_sa(w_f1, 2)} J", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Work along Path 2: {_fmt_sa(w_f2, 2)} J", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Path dependence conclusion", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_negative_sign_friction_work", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Work done by friction always opposes displacement: $W_f = f_k d \\cos(180^\\circ) = -f_k d$.",
        "tier_2": f"Find $f_k = \\mu_k m g = {_fmt_sa(f_k, 2)}\\text{{ N}}$. Then multiply by each distance with a negative sign.",
        "tier_3": f"$W_{{f,1}} = {_fmt_sa(w_f1, 2)}\\text{{ J}}$ and $W_{{f,2}} = {_fmt_sa(w_f2, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_27_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_27_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "27_non_conservative_forces_and_path_dependence",
        "learning_objective_id": "ps_wep_27_non_conservative_path",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_friction_work_independent_of_path", "omitted_negative_sign_friction_work"],
        "keywords": ["non-conservative force", "friction", "path dependence"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 28: Work done by non-conservative forces theorem
def _b28_work_done_by_non_conservative_forces_theorem(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([2.0, 4.0, 5.0, 8.0])
    vi = r.choice([2.0, 3.0, 4.0])
    vf = r.choice([6.0, 7.0, 8.0])
    hi = r.choice([3.0, 4.0, 5.0])
    hf = r.choice([0.0, 1.0])

    delta_ek = 0.5 * mass_kg * (vf ** 2 - vi ** 2)
    delta_ep = mass_kg * G_ACCEL * (hf - hi)
    wnc = delta_ek + delta_ep

    prompt = (
        f"A sled of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ moves down a track from an initial height $h_i = {_fmt_sa(hi)}\\text{{ m}}$ "
        f"with an initial speed of $v_i = {_fmt_sa(vi)}\\text{{ m/s}}$. It reaches a lower position $h_f = {_fmt_sa(hf)}\\text{{ m}}$ "
        f"with a final speed of $v_f = {_fmt_sa(vf)}\\text{{ m/s}}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. State the relationship between the work done by non-conservative forces ($W_{{\\text{{nc}}}}$) "
        f"and the mechanical energy of the system.\n"
        f"2. Calculate the change in kinetic energy ($\\Delta E_k$) of the sled.\n"
        f"3. Calculate the change in gravitational potential energy ($\\Delta E_p$) of the sled.\n"
        f"4. Determine the total work done by non-conservative forces ($W_{{\\text{{nc}}}}$) acting on the sled."
    )

    ans_latex = (
        rf"1.\; W_{{\text{{nc}}}} = \Delta E_k + \Delta E_p = (E_{{kf}} - E_{{ki}}) + (E_{{pf}} - E_{{pi}})\n"
        rf"2.\; \Delta E_k = \frac{{1}}{{2}} m (v_f^2 - v_i^2) = \frac{{1}}{{2}}({_fmt_sa(mass_kg)})({_fmt_sa(vf)}^2 - {_fmt_sa(vi)}^2) = {_fmt_sa(delta_ek, 2)}\text{{ J}}\n"
        rf"3.\; \Delta E_p = m g (h_f - h_i) = ({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(hf)} - {_fmt_sa(hi)}) = {_fmt_sa(delta_ep, 2)}\text{{ J}}\n"
        rf"4.\; W_{{\text{{nc}}}} = \Delta E_k + \Delta E_p = {_fmt_sa(delta_ek, 2)} + ({_fmt_sa(delta_ep, 2)}) = {_fmt_sa(wnc, 2)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Statement: W_nc = Delta E_k + Delta E_p", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Delta E_k calculation: {_fmt_sa(delta_ek, 2)} J", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Delta E_p calculation: {_fmt_sa(delta_ep, 2)} J", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Evaluation of W_nc: {_fmt_sa(wnc, 2)} J", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "sign_error_in_delta_ep", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall that $W_{\\text{nc}} = \\Delta E_k + \\Delta E_p$.",
        "tier_2": "Calculate $\\Delta E_k = \\frac{1}{2}m(v_f^2 - v_i^2)$ and $\\Delta E_p = mg(h_f - h_i)$.",
        "tier_3": f"$\\Delta E_k = {_fmt_sa(delta_ek, 2)}\\text{{ J}}$, $\\Delta E_p = {_fmt_sa(delta_ep, 2)}\\text{{ J}}$, $W_{{\\text{{nc}}}} = {_fmt_sa(wnc, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_28_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_28_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "28_work_done_by_non_conservative_forces_theorem",
        "learning_objective_id": "ps_wep_28_wnc_theorem",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_wnc_with_wnet", "inverted_initial_and_final_in_deltas"],
        "keywords": ["W_nc theorem", "mechanical energy", "Delta Ek", "Delta Ep"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 29: W_nc on horizontal surface with friction
def _b29_wnc_on_horizontal_surface_with_friction(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([5.0, 8.0, 10.0, 12.0, 20.0])
    vi = r.choice([6.0, 8.0, 10.0, 12.0])
    mu_k = r.choice([0.15, 0.20, 0.25, 0.30])
    f_k = mu_k * mass_kg * G_ACCEL
    # delta_ek = 0 - 0.5 * m * vi^2 = -0.5 * m * vi^2
    # W_nc = W_f = -f_k * dx -> dx = 0.5 * m * vi^2 / f_k = vi^2 / (2 * mu_k * g)
    stop_dist = (vi ** 2) / (2 * mu_k * G_ACCEL)
    w_f = -0.5 * mass_kg * (vi ** 2)

    prompt = (
        f"A box of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ slides across a rough horizontal concrete floor. "
        f"It passes point A with a speed of $v_i = {_fmt_sa(vi)}\\text{{ m/s}}$. "
        f"The coefficient of kinetic friction between the box and the floor is $\\mu_k = {_fmt_sa(mu_k)}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. State why $\\Delta E_p = 0\\text{{ J}}$ along this horizontal surface.\n"
        f"2. Use the **work done by non-conservative forces theorem** ($W_{{\\text{{nc}}}} = \\Delta E_k + \\Delta E_p$) "
        f"to calculate the work done by friction as the box comes to rest.\n"
        f"3. Calculate the distance $\\Delta x$ the box slides before stopping."
    )

    ans_latex = (
        rf"1.\; \text{{The height does not change on a horizontal surface (}}\Delta h = 0\text{{ m), hence }}\Delta E_p = m g \Delta h = 0\text{{ J}}.\n"
        rf"2.\; W_{{\text{{nc}}}} = \Delta E_k + \Delta E_p = (0 - \frac{{1}}{{2}} m v_i^2) + 0 = -\frac{{1}}{{2}}({_fmt_sa(mass_kg)})({_fmt_sa(vi)})^2 = {_fmt_sa(w_f, 2)}\text{{ J}}.\n"
        rf"3.\; W_f = f_k \Delta x \cos(180^\circ) = -(\mu_k m g)\Delta x\n"
        rf"\quad {_fmt_sa(w_f, 2)} = -({_fmt_sa(mu_k)})({_fmt_sa(mass_kg)})(9{{,}}8)\Delta x = -{_fmt_sa(f_k, 2)}\Delta x\n"
        rf"\quad \Delta x = \frac{{{_fmt_sa(abs(w_f), 2)}}}{{{_fmt_sa(f_k, 2)}}} = {_fmt_sa(stop_dist, 2)}\text{{ m}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Explanation of zero Delta Ep", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Work done by non-conservative forces: {_fmt_sa(w_f, 2)} J", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Stopping distance calculation: {_fmt_sa(stop_dist, 2)} m", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_negative_sign_in_friction_work", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Since $\\Delta h = 0$, $W_{\\text{nc}} = W_f = \\Delta E_k = 0 - \\frac{1}{2}mv_i^2$.",
        "tier_2": "Friction force is $f_k = \\mu_k m g$. Equate $W_f = -f_k \\Delta x$ to $\\Delta E_k$.",
        "tier_3": f"$W_f = {_fmt_sa(w_f, 2)}\\text{{ J}}$, and $\\Delta x = {_fmt_sa(stop_dist, 2)}\\text{{ m}}$.",
    }

    return {
        "id": f"ps_wep_29_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_29_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "29_wnc_on_horizontal_surface_with_friction",
        "learning_objective_id": "ps_wep_29_wnc_horizontal",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_delta_ep_is_zero_on_flat_surface", "used_positive_work_for_friction"],
        "keywords": ["W_nc", "friction", "stopping distance", "horizontal surface"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 30: W_nc sliding down rough incline
def _b30_wnc_sliding_down_rough_incline(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([3.0, 4.0, 5.0, 6.0])
    theta_deg = r.choice([25.0, 30.0, 35.0])
    theta_rad = math.radians(theta_deg)
    length_m = r.choice([4.0, 5.0, 6.0])
    height_m = length_m * math.sin(theta_rad)
    f_k = r.choice([5.0, 8.0, 10.0, 12.0])

    w_nc = -f_k * length_m
    delta_ep = -mass_kg * G_ACCEL * height_m
    # W_nc = Delta Ek + Delta Ep -> Delta Ek = W_nc - Delta Ep = -f_k*L + mgh
    ek_f = w_nc - delta_ep
    vf = math.sqrt(2 * ek_f / mass_kg)

    svg = _clean_svg(f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 220" width="100%" height="200" style="background:#f8fafc;">
      <polygon points="50,180 370,180 370,50" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
      <line x1="50" y1="180" x2="370" y2="180" stroke="#1e293b" stroke-width="2"/>
      <line x1="370" y1="180" x2="370" y2="50" stroke="#1e293b" stroke-width="2" stroke-dasharray="4"/>
      <path d="M 100,180 A 50,50 0 0,0 95,162" fill="none" stroke="#2563eb" stroke-width="2"/>
      <text x="108" y="174" font-size="13" font-family="sans-serif" fill="#2563eb">{_fmt_sa(theta_deg)}°</text>
      <rect x="230" y="85" width="36" height="24" transform="rotate({_fmt_sa(-theta_deg)} 248 97)" fill="#3b82f6" stroke="#1e3a8a" stroke-width="1.5"/>
      <text x="248" y="102" font-size="11" font-family="sans-serif" fill="#ffffff" text-anchor="middle">{_fmt_sa(mass_kg)} kg</text>
      <text x="378" y="120" font-size="12" font-family="sans-serif" fill="#64748b">h = {_fmt_sa(height_m, 2)} m</text>
      <text x="190" y="70" font-size="12" font-family="sans-serif" fill="#64748b">L = {_fmt_sa(length_m)} m</text>
    </svg>
    """)

    prompt = (
        f"In the accompanying diagram, a block of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ slides from rest at the top of a rough inclined plane "
        f"of length $L = {_fmt_sa(length_m)}\\text{{ m}}$ inclined at an angle of $\\theta = {_fmt_sa(theta_deg)}^\\circ$ to the horizontal. "
        f"The vertical height of the incline is $h = {_fmt_sa(height_m, 2)}\\text{{ m}}$. "
        f"A constant frictional force of $f_k = {_fmt_sa(f_k)}\\text{{ N}}$ acts on the block as it slides down ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the work done by the non-conservative frictional force ($W_{{\\text{{nc}}}}$) along the incline.\n"
        f"2. Use the work-energy theorem involving non-conservative forces ($W_{{\\text{{nc}}}} = \\Delta E_k + \\Delta E_p$) "
        f"to calculate the speed of the block when it reaches the bottom of the incline."
    )

    ans_latex = (
        rf"1.\; W_{{\text{{nc}}}} = W_f = f_k L \cos(180^\circ) = ({_fmt_sa(f_k)})({_fmt_sa(length_m)})(-1) = {_fmt_sa(w_nc, 2)}\text{{ J}}\n"
        rf"2.\; W_{{\text{{nc}}}} = \Delta E_k + \Delta E_p\n"
        rf"\quad {_fmt_sa(w_nc, 2)} = (\frac{{1}}{{2}} m v_f^2 - 0) + (0 - m g h)\n"
        rf"\quad {_fmt_sa(w_nc, 2)} = \frac{{1}}{{2}}({_fmt_sa(mass_kg)})v_f^2 - ({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(height_m, 2)})\n"
        rf"\quad {_fmt_sa(w_nc, 2)} = {_fmt_sa(0.5 * mass_kg)} v_f^2 - {_fmt_sa(-delta_ep, 2)}\n"
        rf"\quad {_fmt_sa(0.5 * mass_kg)} v_f^2 = {_fmt_sa(ek_f, 2)}\implies v_f = \sqrt{{\frac{{{_fmt_sa(ek_f, 2)}}}{{{_fmt_sa(0.5 * mass_kg)}}}}} = {_fmt_sa(vf, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculation of W_nc: {_fmt_sa(w_nc, 2)} J", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Statement: W_nc = Delta Ek + Delta Ep", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Substitution of values into formula", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Final speed: {_fmt_sa(vf, 2)} m/s", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_speed", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "$W_{\\text{nc}}$ is just the work done by friction along the surface: $W_{\\text{nc}} = -f_k L$.",
        "tier_2": "Substitute into $W_{\\text{nc}} = (E_{kf} - 0) + (0 - mgh)$. Solve for $E_{kf} = \\frac{1}{2}mv_f^2$.",
        "tier_3": f"$W_{{\\text{{nc}}}} = {_fmt_sa(w_nc, 2)}\\text{{ J}}$ and $v_f = {_fmt_sa(vf, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_30_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_30_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "30_wnc_sliding_down_rough_incline",
        "learning_objective_id": "ps_wep_30_wnc_rough_incline",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["added_potential_energy_to_wnc_twice", "used_vertical_height_for_friction_distance"],
        "keywords": ["rough incline", "W_nc", "friction", "kinetic energy"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 31: W_nc pushed up rough incline
def _b31_wnc_pushed_up_rough_incline(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([4.0, 5.0, 8.0, 10.0])
    theta_deg = r.choice([20.0, 25.0, 30.0])
    theta_rad = math.radians(theta_deg)
    length_m = r.choice([5.0, 6.0, 8.0])
    height_m = length_m * math.sin(theta_rad)
    f_k = r.choice([8.0, 10.0, 12.0, 15.0])
    f_applied = r.choice([60.0, 80.0, 100.0, 120.0])

    w_applied = f_applied * length_m
    w_friction = -f_k * length_m
    w_nc = w_applied + w_friction
    delta_ep = mass_kg * G_ACCEL * height_m
    ek_f = w_nc - delta_ep
    vf = math.sqrt(2 * max(0.1, ek_f) / mass_kg)

    prompt = (
        f"A crate of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is pushed from rest at the bottom of a rough inclined plane "
        f"by a constant applied force of $F_A = {_fmt_sa(f_applied)}\\text{{ N}}$ directed parallel to and up the incline. "
        f"The incline makes an angle of $\\theta = {_fmt_sa(theta_deg)}^\\circ$ with the horizontal and has length $L = {_fmt_sa(length_m)}\\text{{ m}}$. "
        f"A constant frictional force of $f_k = {_fmt_sa(f_k)}\\text{{ N}}$ opposes the motion ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Identify the two non-conservative forces acting on the crate.\n"
        f"2. Calculate the net work done by all non-conservative forces ($W_{{\\text{{nc}}}}$) over the length of the incline.\n"
        f"3. Using $W_{{\\text{{nc}}}} = \\Delta E_k + \\Delta E_p$, determine the speed of the crate as it reaches the top."
    )

    ans_latex = (
        rf"1.\; \text{{The applied force }} F_A \text{{ and the kinetic frictional force }} f_k.\n"
        rf"2.\; W_{{\text{{nc}}}} = W_{{F_A}} + W_f = F_A L \cos(0^\circ) + f_k L \cos(180^\circ)\n"
        rf"\quad = ({_fmt_sa(f_applied)})({_fmt_sa(length_m)})(1) - ({_fmt_sa(f_k)})({_fmt_sa(length_m)}) = {_fmt_sa(w_applied, 2)} - {_fmt_sa(abs(w_friction), 2)} = {_fmt_sa(w_nc, 2)}\text{{ J}}\n"
        rf"3.\; W_{{\text{{nc}}}} = \Delta E_k + \Delta E_p\n"
        rf"\quad \Delta E_p = m g h = ({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(length_m)}\sin({_fmt_sa(theta_deg)}^\circ)) = {_fmt_sa(delta_ep, 2)}\text{{ J}}\n"
        rf"\quad {_fmt_sa(w_nc, 2)} = \frac{{1}}{{2}}({_fmt_sa(mass_kg)})v_f^2 + {_fmt_sa(delta_ep, 2)}\n"
        rf"\quad \frac{{1}}{{2}}({_fmt_sa(mass_kg)})v_f^2 = {_fmt_sa(ek_f, 2)}\implies v_f = {_fmt_sa(vf, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Identification of non-conservative forces (applied force and friction)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation of W_nc: {_fmt_sa(w_nc, 2)} J", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Delta Ep calculation: {_fmt_sa(delta_ep, 2)} J", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Final speed calculation: {_fmt_sa(vf, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_applied_force_from_wnc", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "$W_{\\text{nc}}$ includes both the applied push and friction: $W_{\\text{nc}} = W_A + W_f$.",
        "tier_2": "Calculate $h = L\\sin\\theta$, find $\\Delta E_p = mgh$, and substitute into $W_{\\text{nc}} = \\frac{1}{2}mv_f^2 + \\Delta E_p$.",
        "tier_3": f"$W_{{\\text{{nc}}}} = {_fmt_sa(w_nc, 2)}\\text{{ J}}$, $\\Delta E_p = {_fmt_sa(delta_ep, 2)}\\text{{ J}}$, $v_f = {_fmt_sa(vf, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_31_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_31_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "31_wnc_pushed_up_rough_incline",
        "learning_objective_id": "ps_wep_31_pushed_incline_wnc",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_applied_force_in_wnc", "omitted_vertical_height_component"],
        "keywords": ["applied force", "rough incline", "W_nc", "work-energy theorem"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 32: W_nc falling with air resistance
def _b32_wnc_falling_with_air_resistance(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([0.5, 1.0, 2.0, 5.0])
    h_m = r.choice([15.0, 20.0, 25.0, 30.0])
    # speed without air resistance = sqrt(2gh)
    v_ideal = math.sqrt(2 * G_ACCEL * h_m)
    # actual vf is 75% to 85% of v_ideal
    vf = round(v_ideal * r.choice([0.75, 0.80, 0.85]), 1)

    delta_ek = 0.5 * mass_kg * (vf ** 2)
    delta_ep = -mass_kg * G_ACCEL * h_m
    w_air = delta_ek + delta_ep
    f_drag_ave = abs(w_air) / h_m

    prompt = (
        f"A parachutist drops a package of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ from rest from a helicopter hovering "
        f"at a height of $h = {_fmt_sa(h_m)}\\text{{ m}}$ above flat ground ($g = 9{{,}}8\\text{{ m/s}}^2$). "
        f"Because of air resistance, the package strikes the ground with a speed of $v_f = {_fmt_sa(vf)}\\text{{ m/s}}$.\n\n"
        f"1. State whether mechanical energy is conserved during the fall. Give a reason for your answer.\n"
        f"2. Use the work done by non-conservative forces theorem ($W_{{\\text{{nc}}}} = \\Delta E_k + \\Delta E_p$) "
        f"to calculate the work done by air resistance ($W_{{\\text{{air}}}}$) on the package.\n"
        f"3. Calculate the magnitude of the average upward drag force exerted by the air on the package."
    )

    ans_latex = (
        rf"1.\; \text{{No, mechanical energy is not conserved because air resistance is a non-conservative force doing negative work.}}\n"
        rf"2.\; W_{{\text{{nc}}}} = W_{{\text{{air}}}} = \Delta E_k + \Delta E_p\n"
        rf"\quad \Delta E_k = \frac{{1}}{{2}} m v_f^2 - 0 = \frac{{1}}{{2}}({_fmt_sa(mass_kg)})({_fmt_sa(vf)})^2 = {_fmt_sa(delta_ek, 2)}\text{{ J}}\n"
        rf"\quad \Delta E_p = m g (0 - h) = -({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(h_m)}) = {_fmt_sa(delta_ep, 2)}\text{{ J}}\n"
        rf"\quad W_{{\text{{air}}}} = {_fmt_sa(delta_ek, 2)} + ({_fmt_sa(delta_ep, 2)}) = {_fmt_sa(w_air, 2)}\text{{ J}}\n"
        rf"3.\; W_{{\text{{air}}}} = F_{{\text{{drag}}}} h \cos(180^\circ) = -F_{{\text{{drag}}}} h\n"
        rf"\quad F_{{\text{{drag}}}} = \frac{{|W_{{\text{{air}}}}|}}{{h}} = \frac{{{_fmt_sa(abs(w_air), 2)}}}{{{_fmt_sa(h_m)}}} = {_fmt_sa(f_drag_ave, 2)}\text{{ N}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Conservation of energy judgement with valid reason", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "W_nc theorem formula", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of W_air: {_fmt_sa(w_air, 2)} J", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Average drag force magnitude: {_fmt_sa(f_drag_ave, 2)} N", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_negative_sign_in_work_air", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Air resistance takes away mechanical energy, so $W_{\\text{air}} = \\Delta E_k + \\Delta E_p < 0$.",
        "tier_2": "Calculate $\\Delta E_k = \\frac{1}{2}mv_f^2$ and $\\Delta E_p = -mgh$. Then $F_{\\text{drag}} = |W_{\\text{air}}| / h$.",
        "tier_3": f"$W_{{\\text{{air}}}} = {_fmt_sa(w_air, 2)}\\text{{ J}}$ and $F_{{\\text{{drag}}}} = {_fmt_sa(f_drag_ave, 2)}\\text{{ N}}$.",
    }

    return {
        "id": f"ps_wep_32_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_32_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "32_wnc_falling_with_air_resistance",
        "learning_objective_id": "ps_wep_32_falling_air_drag",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["treated_air_resistance_as_conservative", "used_ideal_free_fall_speed"],
        "keywords": ["air resistance", "drag force", "W_nc", "falling object"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 33: W_nc curved roller coaster track with friction
def _b33_wnc_curved_roller_coaster_track_with_friction(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([250, 300, 400, 500])
    h_top = r.choice([18.0, 20.0, 25.0])
    v_top = r.choice([2.0, 3.0, 4.0])
    v_bottom = r.choice([14.0, 15.0, 16.0])

    ek_i = 0.5 * mass_kg * (v_top ** 2)
    ep_i = mass_kg * G_ACCEL * h_top
    e_mech_i = ek_i + ep_i

    ek_f = 0.5 * mass_kg * (v_bottom ** 2)
    ep_f = 0.0
    e_mech_f = ek_f + ep_f

    w_nc = e_mech_f - e_mech_i

    prompt = (
        f"A roller-coaster cart with passengers has a total mass of $m = {mass_kg}\\text{{ kg}}$. "
        f"The cart enters the top of a curved descent at height $h = {_fmt_sa(h_top)}\\text{{ m}}$ with a speed of $v_i = {_fmt_sa(v_top)}\\text{{ m/s}}$. "
        f"As it reaches the lowest level of the track ($h = 0\\text{{ m}}$), its speed is measured as $v_f = {_fmt_sa(v_bottom)}\\text{{ m/s}}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the initial mechanical energy ($E_{{\\text{{mech,i}}}}$) of the cart at the top.\n"
        f"2. Calculate the final mechanical energy ($E_{{\\text{{mech,f}}}}$) of the cart at the bottom.\n"
        f"3. Use the work done by non-conservative forces theorem to calculate the work done by friction and air drag ($W_{{\\text{{nc}}}}$) during the descent.\n"
        f"4. State what happened to the energy that was lost by the mechanical system."
    )

    ans_latex = (
        rf"1.\; E_{{\text{{mech,i}}}} = E_{{ki}} + E_{{pi}} = \frac{{1}}{{2}} m v_i^2 + m g h\n"
        rf"\quad = \frac{{1}}{{2}}({mass_kg})({_fmt_sa(v_top)})^2 + ({mass_kg})(9{{,}}8)({_fmt_sa(h_top)}) = {_fmt_sa(ek_i, 2)} + {_fmt_sa(ep_i, 2)} = {_fmt_sa(e_mech_i, 2)}\text{{ J}}\n"
        rf"2.\; E_{{\text{{mech,f}}}} = E_{{kf}} + E_{{pf}} = \frac{{1}}{{2}}({mass_kg})({_fmt_sa(v_bottom)})^2 + 0 = {_fmt_sa(e_mech_f, 2)}\text{{ J}}\n"
        rf"3.\; W_{{\text{{nc}}}} = E_{{\text{{mech,f}}}} - E_{{\text{{mech,i}}}} = {_fmt_sa(e_mech_f, 2)} - {_fmt_sa(e_mech_i, 2)} = {_fmt_sa(w_nc, 2)}\text{{ J}}\n"
        rf"4.\; \text{{The mechanical energy was converted into internal thermal energy (heat) and sound energy due to friction.}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Initial mechanical energy: {_fmt_sa(e_mech_i, 2)} J", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Final mechanical energy: {_fmt_sa(e_mech_f, 2)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of W_nc: {_fmt_sa(w_nc, 2)} J", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Thermal energy dissipation statement", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_negative_sign_in_loss", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "$W_{\\text{nc}} = E_{\\text{mech,f}} - E_{\\text{mech,i}}$.",
        "tier_2": "Calculate total initial energy ($E_{ki} + E_{pi}$) and final energy ($E_{kf}$).",
        "tier_3": f"$E_{{\\text{{mech,i}}}} = {_fmt_sa(e_mech_i, 2)}\\text{{ J}}$, $E_{{\\text{{mech,f}}}} = {_fmt_sa(e_mech_f, 2)}\\text{{ J}}$, $W_{{\\text{{nc}}}} = {_fmt_sa(w_nc, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_33_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_33_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "33_wnc_curved_roller_coaster_track_with_friction",
        "learning_objective_id": "ps_wep_33_roller_coaster_wnc",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["subtracted_energies_backwards", "assumed_energy_was_destroyed"],
        "keywords": ["curved track", "roller coaster", "W_nc", "thermal dissipation"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 34: W_nc ski jumper slope and friction
def _b34_wnc_ski_jumper_slope_and_friction(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([65.0, 70.0, 75.0, 80.0])
    h1 = r.choice([40.0, 45.0, 50.0])
    h2 = r.choice([10.0, 12.0, 15.0])
    w_friction = -r.choice([3500.0, 4000.0, 4500.0, 5000.0])

    delta_ep = mass_kg * G_ACCEL * (h2 - h1)
    # W_nc = Delta Ek + Delta Ep -> Delta Ek = W_nc - Delta Ep
    ek2 = w_friction - delta_ep
    v_launch = math.sqrt(2 * ek2 / mass_kg)

    prompt = (
        f"A ski jumper with equipment has a mass of $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$. "
        f"The skier starts from rest at the top of an in-run at height $h_1 = {_fmt_sa(h1)}\\text{{ m}}$ above the ground. "
        f"During the descent to the takeoff lip at height $h_2 = {_fmt_sa(h2)}\\text{{ m}}$, friction and air resistance "
        f"do a total of $W_{{\\text{{nc}}}} = {_fmt_sa(w_friction)}\\text{{ J}}$ of work ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the change in gravitational potential energy ($\\Delta E_p$) of the skier between the top and the takeoff lip.\n"
        f"2. Use the work done by non-conservative forces theorem ($W_{{\\text{{nc}}}} = \\Delta E_k + \\Delta E_p$) "
        f"to determine the takeoff launch speed ($v_2$) of the ski jumper."
    )

    ans_latex = (
        rf"1.\; \Delta E_p = m g (h_2 - h_1) = ({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(h2)} - {_fmt_sa(h1)}) = {_fmt_sa(delta_ep, 2)}\text{{ J}}\n"
        rf"2.\; W_{{\text{{nc}}}} = \Delta E_k + \Delta E_p\n"
        rf"\quad {_fmt_sa(w_friction)} = (\frac{{1}}{{2}} m v_2^2 - 0) + ({_fmt_sa(delta_ep, 2)})\n"
        rf"\quad \frac{{1}}{{2}}({_fmt_sa(mass_kg)})v_2^2 = {_fmt_sa(w_friction)} - ({_fmt_sa(delta_ep, 2)}) = {_fmt_sa(ek2, 2)}\text{{ J}}\n"
        rf"\quad v_2 = \sqrt{{\frac{{2 \\times {_fmt_sa(ek2, 2)}}}{{{_fmt_sa(mass_kg)}}}}} = {_fmt_sa(v_launch, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Delta Ep calculation: {_fmt_sa(delta_ep, 2)} J", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Formula: W_nc = Delta Ek + Delta Ep", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Takeoff launch speed: {_fmt_sa(v_launch, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_speed", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Notice that $\\Delta E_p = mg(h_2 - h_1)$ is negative because the skier loses height.",
        "tier_2": "Solve for $\\Delta E_k = W_{\\text{nc}} - \\Delta E_p$, then use $\\Delta E_k = \\frac{1}{2}mv_2^2$.",
        "tier_3": f"$\\Delta E_p = {_fmt_sa(delta_ep, 2)}\\text{{ J}}$, $E_{{k2}} = {_fmt_sa(ek2, 2)}\\text{{ J}}$, $v_2 = {_fmt_sa(v_launch, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_34_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_34_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "34_wnc_ski_jumper_slope_and_friction",
        "learning_objective_id": "ps_wep_34_ski_jump_wnc",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["subtracted_heights_backwards", "treated_wnc_as_positive"],
        "keywords": ["ski jumper", "takeoff speed", "W_nc", "gravitational potential energy"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 35: Conservation of mechanical energy isolated system
def _b35_conservation_of_mechanical_energy_isolated_system(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([2.5, 4.0, 5.0, 10.0])
    h1 = r.choice([6.0, 8.0, 10.0, 12.0])
    v1 = r.choice([0.0, 2.0, 4.0])
    h2 = r.choice([1.0, 2.0, 3.0])

    e_mech = 0.5 * mass_kg * (v1 ** 2) + mass_kg * G_ACCEL * h1
    ek2 = e_mech - mass_kg * G_ACCEL * h2
    v2 = math.sqrt(2 * ek2 / mass_kg)

    prompt = (
        f"A frictionless skate ramp has an elevation profile where a skater of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ "
        f"passes point A at height $h_A = {_fmt_sa(h1)}\\text{{ m}}$ with speed $v_A = {_fmt_sa(v1)}\\text{{ m/s}}$. "
        f"The skater continues along the smooth track to point B at height $h_B = {_fmt_sa(h2)}\\text{{ m}}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. State the **principle of conservation of mechanical energy** in words.\n"
        f"2. Explain what is meant by an **isolated system** in physics.\n"
        f"3. Calculate the speed $v_B$ of the skater at point B using energy principles."
    )

    ans_latex = (
        rf"1.\; \text{{The total mechanical energy in an isolated system remains constant.}}\n"
        rf"2.\; \text{{An isolated system is one in which the net external force acting on the system is zero (no external non-conservative forces act).}}\n"
        rf"3.\; E_{{\text{{mech,A}}}} = E_{{\text{{mech,B}}}}\n"
        rf"\quad \frac{{1}}{{2}} m v_A^2 + m g h_A = \frac{{1}}{{2}} m v_B^2 + m g h_B\n"
        rf"\quad \frac{{1}}{{2}}({_fmt_sa(mass_kg)})({_fmt_sa(v1)})^2 + ({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(h1)}) = \frac{{1}}{{2}}({_fmt_sa(mass_kg)})v_B^2 + ({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(h2)})\n"
        rf"\quad {_fmt_sa(e_mech, 2)} = {_fmt_sa(0.5 * mass_kg)} v_B^2 + {_fmt_sa(mass_kg * G_ACCEL * h2, 2)}\n"
        rf"\quad {_fmt_sa(0.5 * mass_kg)} v_B^2 = {_fmt_sa(ek2, 2)}\implies v_B = {_fmt_sa(v2, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Statement: Conservation of mechanical energy", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Definition of isolated system", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Energy conservation equation: E_mech,A = E_mech,B", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Evaluation of final speed: {_fmt_sa(v2, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_speed", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "In an isolated system without friction, mechanical energy is conserved: $E_{kA} + E_{pA} = E_{kB} + E_{pB}$.",
        "tier_2": "Calculate total energy at A: $E_{\\text{mech}} = \\frac{1}{2}mv_A^2 + mgh_A$. Equate to $\\frac{1}{2}mv_B^2 + mgh_B$.",
        "tier_3": f"$E_{{\\text{{mech}}}} = {_fmt_sa(e_mech, 2)}\\text{{ J}}$ and $v_B = {_fmt_sa(v2, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_35_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_35_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "35_conservation_of_mechanical_energy_isolated_system",
        "learning_objective_id": "ps_wep_35_mech_energy_conservation",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_closed_system_with_isolated_system", "forgot_initial_kinetic_energy"],
        "keywords": ["conservation of mechanical energy", "isolated system", "frictionless track"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 36: Conservation of mechanical energy loop-the-loop
def _b36_conservation_of_mechanical_energy_loop_the_loop(r: random.Random) -> Dict[str, Any]:
    radius_m = r.choice([2.0, 3.0, 4.0, 5.0])
    mass_kg = r.choice([0.5, 1.0, 2.0])
    # Min speed at top: v_top = sqrt(g * r)
    v_top = math.sqrt(G_ACCEL * radius_m)
    # Height of top is 2*r. E_top = 0.5 * m * (g*r) + m * g * (2*r) = 2.5 * m * g * r
    h_min = 2.5 * radius_m
    v_bottom = math.sqrt(2 * G_ACCEL * h_min)  # sqrt(5 * g * r)

    svg = _clean_svg(f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 260" width="100%" height="220" style="background:#f8fafc;">
      <path d="M 40,30 L 120,200 L 180,200 A 60,60 0 1,0 180,80 A 60,60 0 0,0 180,200 L 340,200" fill="none" stroke="#334155" stroke-width="3"/>
      <line x1="30" y1="200" x2="350" y2="200" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4"/>
      <circle cx="180" cy="80" r="8" fill="#ef4444"/>
      <text x="180" y="70" font-size="12" font-family="sans-serif" fill="#ef4444" text-anchor="middle">Top (C)</text>
      <circle cx="180" cy="200" r="8" fill="#3b82f6"/>
      <text x="180" y="222" font-size="12" font-family="sans-serif" fill="#3b82f6" text-anchor="middle">Bottom (B)</text>
      <circle cx="40" cy="30" r="8" fill="#10b981"/>
      <text x="40" y="20" font-size="12" font-family="sans-serif" fill="#10b981" text-anchor="middle">Release (A)</text>
      <line x1="180" y1="140" x2="180" y2="80" stroke="#64748b" stroke-width="1.5"/>
      <text x="190" y="115" font-size="11" font-family="sans-serif" fill="#64748b">r = {_fmt_sa(radius_m)} m</text>
    </svg>
    """)

    prompt = (
        f"In the accompanying diagram, a roller-coaster model car of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is released from rest at point A "
        f"at height $h$ on a frictionless track. The track includes a vertical circular loop of radius $r = {_fmt_sa(radius_m)}\\text{{ m}}$. "
        f"The top of the loop is designated point C ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. State the condition for the minimum speed required at the top of the loop (point C) to just maintain contact with the track.\n"
        f"2. Calculate the minimum speed $v_{{\\text{{top}}}}$ of the car at point C.\n"
        f"3. Using the principle of conservation of mechanical energy, determine the minimum release height $h_{{\\text{{min}}}}$ at point A "
        f"above the lowest level of the track."
    )

    ans_latex = (
        rf"1.\; \text{{At the minimum speed, normal force }} N = 0\text{{ N, so gravity alone provides the centripetal force: }} m g = \frac{{m v^2}}{{r}} \implies v_{{\text{{top}}}} = \sqrt{{g r}}.\n"
        rf"2.\; v_{{\text{{top}}}} = \sqrt{{g r}} = \sqrt{{(9{{,}}8)({_fmt_sa(radius_m)})}} = {_fmt_sa(v_top, 2)}\text{{ m/s}}\n"
        rf"3.\; E_{{\text{{mech,A}}}} = E_{{\text{{mech,C}}}}\n"
        rf"\quad m g h_{{\text{{min}}}} + 0 = \frac{{1}}{{2}} m v_{{\text{{top}}}}^2 + m g (2 r)\n"
        rf"\quad g h_{{\text{{min}}}} = \frac{{1}}{{2}}(g r) + 2 g r = 2{{,}}5 g r\n"
        rf"\quad h_{{\text{{min}}}} = 2{{,}}5 r = 2{{,}}5({_fmt_sa(radius_m)}) = {_fmt_sa(h_min, 2)}\text{{ m}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Condition for minimum speed (N = 0, gravity as centripetal force)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Minimum speed at top: {_fmt_sa(v_top, 2)} m/s", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Conservation of energy and release height: {_fmt_sa(h_min, 2)} m", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_vertical_height_diameter", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "At the top of the loop, centripetal force equals gravity when normal force is zero: $v = \\sqrt{gr}$.",
        "tier_2": "The height of the top of the loop is $2r$. Conserve mechanical energy between release point and top.",
        "tier_3": f"$v_{{\\text{{top}}}} = {_fmt_sa(v_top, 2)}\\text{{ m/s}}$ and $h_{{\\text{{min}}}} = 2{{,}}5 r = {_fmt_sa(h_min, 2)}\\text{{ m}}$.",
    }

    return {
        "id": f"ps_wep_36_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_36_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "36_conservation_of_mechanical_energy_loop_the_loop",
        "learning_objective_id": "ps_wep_36_loop_the_loop",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_height_equals_r_instead_of_2r", "forgot_kinetic_energy_at_top_of_loop"],
        "keywords": ["loop-the-loop", "centripetal force", "minimum speed", "conservation of mechanical energy"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 37: Average power definition and formula
def _b37_average_power_definition_and_formula(r: random.Random) -> Dict[str, Any]:
    work_j = r.choice([12000, 18000, 24000, 36000, 48000])
    dt_s = r.choice([15.0, 20.0, 25.0, 30.0, 40.0])
    power_w = work_j / dt_s
    power_kw = power_w / 1000.0

    prompt = (
        f"An electric winch performs $W = {work_j}\\text{{ J}}$ of work in lifting a load through a vertical shaft "
        f"in a time interval of $\\Delta t = {_fmt_sa(dt_s)}\\text{{ s}}$.\n\n"
        f"1. Define **power** in words.\n"
        f"2. State the SI unit of power and its equivalent in fundamental base units (or Joules and seconds).\n"
        f"3. Calculate the average power output of the winch in watts ($\\text{{W}}$) and in kilowatts ($\\text{{kW}}$)."
    )

    ans_latex = (
        rf"1.\; \text{{Power is the rate at which work is done (or the rate at which energy is transferred/expended).}}\n"
        rf"2.\; \text{{The SI unit is the watt (W), where }} 1\text{{ W}} = 1\text{{ J/s}} = 1\text{{ kg}}\cdot\text{{m}}^2\cdot\text{{s}}^{{-3}}.\n"
        rf"3.\; P = \frac{{W}}{{\Delta t}} = \frac{{{work_j}}}{{{_fmt_sa(dt_s)}}} = {_fmt_sa(power_w, 2)}\text{{ W}} = {_fmt_sa(power_kw, 3)}\text{{ kW}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of power (rate of doing work)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "SI unit and equivalence: 1 W = 1 J/s", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Power calculation: {_fmt_sa(power_w, 2)} W ({_fmt_sa(power_kw, 3)} kW)", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_power", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Power is defined as the rate of doing work: $P = \\frac{W}{\\Delta t}$.",
        "tier_2": f"Divide work by time: $P = \\frac{{{work_j}}}{{{dt_s}}}$. Convert to kW by dividing by 1000.",
        "tier_3": f"$P = {_fmt_sa(power_w, 2)}\\text{{ W}} = {_fmt_sa(power_kw, 3)}\\text{{ kW}}$.",
    }

    return {
        "id": f"ps_wep_37_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_37_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "37_average_power_definition_and_formula",
        "learning_objective_id": "ps_wep_37_power_definition",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_power_with_energy", "incorrect_prefix_conversion_kw"],
        "keywords": ["power", "rate of doing work", "watt", "kilowatt"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 38: Power lifting mass at constant speed
def _b38_power_lifting_mass_at_constant_speed(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([200, 400, 500, 750, 1000])
    height_m = r.choice([12.0, 15.0, 20.0, 24.0])
    dt_s = r.choice([8.0, 10.0, 12.0, 16.0])
    v_const = height_m / dt_s
    f_up = mass_kg * G_ACCEL
    power_w = f_up * v_const
    power_kw = power_w / 1000.0

    prompt = (
        f"A construction hoist motor lifts a pallet of bricks with total mass $m = {mass_kg}\\text{{ kg}}$ "
        f"vertically upward through a height of $h = {_fmt_sa(height_m)}\\text{{ m}}$ in a time interval of $\\Delta t = {_fmt_sa(dt_s)}\\text{{ s}}$ "
        f"at constant velocity ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Explain why the upward tension force exerted by the hoist cable equals the weight of the pallet.\n"
        f"2. Calculate the constant upward velocity ($v$) of the pallet.\n"
        f"3. Calculate the power developed by the motor using:\n"
        f"   - (a) $P = \\frac{{W}}{{\\Delta t}}$\n"
        f"   - (b) $P = F v$\n"
        f"4. State the motor's power in kilowatts ($\\text{{kW}}$)."
    )

    ans_latex = (
        rf"1.\; \text{{At constant velocity, acceleration }} a = 0\text{{ m/s}}^2 \text{{, so the resultant vertical force is zero: }} F_{{\text{{net}}}} = T - mg = 0 \implies T = mg.\n"
        rf"2.\; v = \frac{{h}}{{\Delta t}} = \frac{{{_fmt_sa(height_m)}}}{{{_fmt_sa(dt_s)}}} = {_fmt_sa(v_const, 2)}\text{{ m/s}}\n"
        rf"3.\; \text{{(a) }} W = F h = ({mass_kg} \times 9{{,}}8)({_fmt_sa(height_m)}) = {_fmt_sa(f_up * height_m, 2)}\text{{ J}}\n"
        rf"\quad P = \frac{{W}}{{\Delta t}} = \frac{{{_fmt_sa(f_up * height_m, 2)}}}{{{_fmt_sa(dt_s)}}} = {_fmt_sa(power_w, 2)}\text{{ W}}\n"
        rf"\quad \text{{(b) }} P = F v = ({mass_kg} \times 9{{,}}8)({_fmt_sa(v_const, 2)}) = {_fmt_sa(power_w, 2)}\text{{ W}}\n"
        rf"4.\; P = {_fmt_sa(power_kw, 2)}\text{{ kW}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Newton's first law explanation (a = 0 implies T = mg)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Constant velocity calculation: {_fmt_sa(v_const, 2)} m/s", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Power calculation using P = W / Delta t", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Power calculation using P = F * v", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Conversion to kW: {_fmt_sa(power_kw, 2)} kW", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_power", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "At constant velocity, $F_{\\text{cable}} = mg = ({mass_kg})(9{{,}}8)\\text{{ N}}$.",
        "tier_2": "Calculate $v = h / \\Delta t$. Power is either $W/\\Delta t$ or $F v$. Both yield the same result.",
        "tier_3": f"$v = {_fmt_sa(v_const, 2)}\\text{{ m/s}}$ and $P = {_fmt_sa(power_w, 2)}\\text{{ W}} = {_fmt_sa(power_kw, 2)}\\text{{ kW}}$.",
    }

    return {
        "id": f"ps_wep_38_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_38_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "38_power_lifting_mass_at_constant_speed",
        "learning_objective_id": "ps_wep_38_hoist_power_constant_v",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_mass_instead_of_weight_in_force", "multiplied_by_time_instead_of_dividing"],
        "keywords": ["hoist", "constant speed", "P = Fv", "lifting work"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 39: Power accelerating vehicle from rest
def _b39_power_accelerating_vehicle_from_rest(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([800, 1000, 1200, 1500])
    vf_kmh = r.choice([72, 90, 108])
    vf_ms = vf_kmh / 3.6
    dt_s = r.choice([5.0, 6.0, 8.0, 10.0])

    delta_ek = 0.5 * mass_kg * (vf_ms ** 2)
    p_ave_w = delta_ek / dt_s
    p_ave_kw = p_ave_w / 1000.0

    prompt = (
        f"An electric vehicle of mass $m = {mass_kg}\\text{{ kg}}$ accelerates uniformly from rest along a level road "
        f"to reach a speed of ${vf_kmh}\\text{{ km/h}}$ in a time of $\\Delta t = {_fmt_sa(dt_s)}\\text{{ s}}$. "
        f"Assume all resistive forces are negligible during this initial sprint.\n\n"
        f"1. Convert the final speed of ${vf_kmh}\\text{{ km/h}}$ to metres per second ($\\text{{m/s}}$).\n"
        f"2. Calculate the change in kinetic energy ($\\Delta E_k$) of the vehicle.\n"
        f"3. Calculate the average power output ($P_{{\\text{{ave}}}}$) delivered to accelerate the vehicle, in kilowatts ($\\text{{kW}}$)."
    )

    ans_latex = (
        rf"1.\; v_f = \frac{{{vf_kmh}}}{{3{{,}}6}} = {_fmt_sa(vf_ms, 2)}\text{{ m/s}}\n"
        rf"2.\; \Delta E_k = \frac{{1}}{{2}} m v_f^2 - 0 = \frac{{1}}{{2}}({mass_kg})({_fmt_sa(vf_ms, 2)})^2 = {_fmt_sa(delta_ek, 2)}\text{{ J}}\n"
        rf"3.\; P_{{\text{{ave}}}} = \frac{{\Delta E_k}}{{\Delta t}} = \frac{{{_fmt_sa(delta_ek, 2)}}}{{{_fmt_sa(dt_s)}}} = {_fmt_sa(p_ave_w, 2)}\text{{ W}} = {_fmt_sa(p_ave_kw, 2)}\text{{ kW}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Conversion km/h to m/s: {_fmt_sa(vf_ms, 2)} m/s", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Kinetic energy calculation: {_fmt_sa(delta_ek, 2)} J", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Average power in kW: {_fmt_sa(p_ave_kw, 2)} kW", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_speed_conversion_kmh_to_ms", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Divide speed in km/h by 3.6 to convert to m/s.",
        "tier_2": "Work done equals the gain in kinetic energy: $W = \\Delta E_k = \\frac{1}{2}mv_f^2$.",
        "tier_3": f"$\\Delta E_k = {_fmt_sa(delta_ek, 2)}\\text{{ J}}$ and $P_{{\\text{{ave}}}} = {_fmt_sa(p_ave_kw, 2)}\\text{{ kW}}$.",
    }

    return {
        "id": f"ps_wep_39_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_39_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "39_power_accelerating_vehicle_from_rest",
        "learning_objective_id": "ps_wep_39_vehicle_acceleration_power",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_kmh_directly_in_kinetic_energy", "confused_peak_power_with_average_power"],
        "keywords": ["vehicle acceleration", "average power", "kinetic energy", "speed conversion"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 40: Power formula P = F * v at constant speed
def _b40_power_formula_p_equals_f_v_constant_speed(r: random.Random) -> Dict[str, Any]:
    speed_ms = r.choice([20.0, 25.0, 30.0, 35.0])
    res_force_n = r.choice([400, 500, 600, 800, 1000])
    power_w = res_force_n * speed_ms
    power_kw = power_w / 1000.0

    prompt = (
        f"A motor vehicle cruises at a steady speed of $v = {_fmt_sa(speed_ms)}\\text{{ m/s}}$ along a straight level highway. "
        f"The total resistive forces (air drag and rolling friction) opposing the vehicle have a combined magnitude of $F_R = {res_force_n}\\text{{ N}}$.\n\n"
        f"1. State Newton's First Law of Motion and deduce the magnitude of the forward driving force $F_D$ exerted by the engine.\n"
        f"2. Write down the equation that directly relates power, force, and velocity at constant speed.\n"
        f"3. Calculate the power developed by the vehicle engine in kilowatts ($\\text{{kW}}$)."
    )

    ans_latex = (
        rf"1.\; \text{{A body continues in its state of rest or uniform motion in a straight line unless acted upon by a non-zero net force.}}\n"
        rf"\quad \text{{At constant speed, }} a = 0\text{{ m/s}}^2 \implies F_{{\text{{net}}}} = F_D - F_R = 0 \implies F_D = F_R = {res_force_n}\text{{ N}}.\n"
        rf"2.\; P = F v\n"
        rf"3.\; P = F_D v = ({res_force_n})({_fmt_sa(speed_ms)}) = {_fmt_sa(power_w, 2)}\text{{ W}} = {_fmt_sa(power_kw, 2)}\text{{ kW}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Newton's First Law statement", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Deduction of driving force: {res_force_n} N", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Formula: P = F * v", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Power in kW: {_fmt_sa(power_kw, 2)} kW", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_power", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "At constant velocity, forward driving force equals backward resistive force.",
        "tier_2": "Use the formula $P = F v$. Convert watts to kilowatts by dividing by 1000.",
        "tier_3": f"$F_D = {res_force_n}\\text{{ N}}$ and $P = {_fmt_sa(power_kw, 2)}\\text{{ kW}}$.",
    }

    return {
        "id": f"ps_wep_40_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_40_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "40_power_formula_p_equals_f_v_constant_speed",
        "learning_objective_id": "ps_wep_40_p_equals_fv",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_net_force_is_used_in_p_equals_fv", "forgot_forward_force_balances_resistance"],
        "keywords": ["constant velocity", "P = Fv", "driving force", "resistance"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 5,
    }


# Archetype 41: Power car cruising against air resistance
def _b41_power_car_cruising_against_air_resistance(r: random.Random) -> Dict[str, Any]:
    v1 = r.choice([20.0, 22.0, 25.0])
    v2 = v1 * 1.5  # 50% increase
    # Drag force proportional to v^2: F_drag = k * v^2 -> Power = F_drag * v = k * v^3
    k_drag = r.choice([0.6, 0.8, 1.0])
    f_drag_1 = k_drag * (v1 ** 2)
    p1 = f_drag_1 * v1
    f_drag_2 = k_drag * (v2 ** 2)
    p2 = f_drag_2 * v2
    ratio = p2 / p1  # should be (1.5)^3 = 3.375

    prompt = (
        f"The aerodynamic drag force opposing a streamlined sports car traveling at high speed is given by "
        f"$F_{{\\text{{drag}}}} = k v^2$, where $k = {_fmt_sa(k_drag)}\\text{{ kg/m}}$.\n\n"
        f"1. At a steady cruising speed of $v_1 = {_fmt_sa(v1)}\\text{{ m/s}}$, calculate:\n"
        f"   - (a) The aerodynamic drag force $F_{{\\text{{drag,1}}}}$.\n"
        f"   - (b) The power $P_1$ needed to overcome this drag force, in kilowatts ($\\text{{kW}}$).\n"
        f"2. The driver accelerates to a higher steady cruising speed of $v_2 = {_fmt_sa(v2, 2)}\\text{{ m/s}}$ (a 50% increase in speed).\n"
        f"   - (a) Calculate the new power $P_2$ in kilowatts.\n"
        f"   - (b) Determine the ratio $\\frac{{P_2}}{{P_1}}$ and explain why fuel consumption increases drastically at higher highway speeds."
    )

    ans_latex = (
        rf"1.\; \text{{(a) }} F_{{\text{{drag,1}}}} = k v_1^2 = ({_fmt_sa(k_drag)})({_fmt_sa(v1)})^2 = {_fmt_sa(f_drag_1, 2)}\text{{ N}}\n"
        rf"\quad \text{{(b) }} P_1 = F_{{\text{{drag,1}}}} v_1 = ({_fmt_sa(f_drag_1, 2)})({_fmt_sa(v1)}) = {_fmt_sa(p1, 2)}\text{{ W}} = {_fmt_sa(p1 / 1000.0, 2)}\text{{ kW}}\n"
        rf"2.\; \text{{(a) }} F_{{\text{{drag,2}}}} = k v_2^2 = ({_fmt_sa(k_drag)})({_fmt_sa(v2, 2)})^2 = {_fmt_sa(f_drag_2, 2)}\text{{ N}}\n"
        rf"\quad P_2 = F_{{\text{{drag,2}}}} v_2 = ({_fmt_sa(f_drag_2, 2)})({_fmt_sa(v2, 2)}) = {_fmt_sa(p2, 2)}\text{{ W}} = {_fmt_sa(p2 / 1000.0, 2)}\text{{ kW}}\n"
        rf"\quad \text{{(b) }} \frac{{P_2}}{{P_1}} = \frac{{{_fmt_sa(p2, 2)}}}{{{_fmt_sa(p1, 2)}}} = {_fmt_sa(ratio, 2)} = (1{{,}}5)^3\n"
        rf"\quad \text{{Because power depends on the cube of the speed (}}P \propto v^3\text{{), doubling or increasing speed requires substantially more engine power and fuel.}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculation of F_drag,1: {_fmt_sa(f_drag_1, 2)} N", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation of P_1: {_fmt_sa(p1 / 1000.0, 2)} kW", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of F_drag,2: {_fmt_sa(f_drag_2, 2)} N", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculation of P_2: {_fmt_sa(p2 / 1000.0, 2)} kW", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Ratio P2 / P1 = {_fmt_sa(ratio, 2)} with cubic relationship explanation", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_cubic_dependency_justification", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Since $F_{\\text{drag}} = kv^2$, power is $P = F v = kv^3$.",
        "tier_2": "Calculate $P_1 = k v_1^3$ and $P_2 = k v_2^3$. Divide by 1000 for kW.",
        "tier_3": f"$P_1 = {_fmt_sa(p1 / 1000.0, 2)}\\text{{ kW}}$, $P_2 = {_fmt_sa(p2 / 1000.0, 2)}\\text{{ kW}}$, ratio = {_fmt_sa(ratio, 2)}.",
    }

    return {
        "id": f"ps_wep_41_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_41_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "41_power_car_cruising_against_air_resistance",
        "learning_objective_id": "ps_wep_41_drag_power_scaling",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_power_is_proportional_to_v_squared_instead_of_cubed"],
        "keywords": ["aerodynamic drag", "cubic power law", "fuel consumption", "speed scaling"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 42: Power vehicle climbing rough incline
def _b42_power_vehicle_climbing_rough_incline(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([1200, 1500, 2000, 2500])
    theta_deg = r.choice([5.0, 6.0, 8.0, 10.0])
    theta_rad = math.radians(theta_deg)
    v_ms = r.choice([15.0, 20.0, 22.0, 25.0])
    f_k = r.choice([300, 400, 500, 600])

    # F_parallel = m * g * sin(theta)
    f_parallel = mass_kg * G_ACCEL * math.sin(theta_rad)
    f_engine = f_parallel + f_k
    power_w = f_engine * v_ms
    power_kw = power_w / 1000.0

    prompt = (
        f"A bakkie of mass $m = {mass_kg}\\text{{ kg}}$ climbs an incline that makes an angle of $\\theta = {_fmt_sa(theta_deg)}^\\circ$ "
        f"with the horizontal at a constant speed of $v = {_fmt_sa(v_ms)}\\text{{ m/s}}$. "
        f"A total frictional force of $f_k = {f_k}\\text{{ N}}$ opposes the motion ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Draw a labeled free-body diagram of all forces acting on the bakkie as it climbs.\n"
        f"2. Calculate the component of gravitational force acting parallel to the incline ($F_{{g\\parallel}}$).\n"
        f"3. Calculate the forward driving force $F_D$ exerted by the wheels on the road.\n"
        f"4. Determine the power output of the engine in kilowatts ($\\text{{kW}}$)."
    )

    ans_latex = (
        rf"1.\; \text{{Free-body diagram: Normal force }} N \text{{ perpendicular to slope, Gravity }} F_g \text{{ vertically down, Friction }} f_k \text{{ down the slope, Driving force }} F_D \text{{ up the slope.}}\n"
        rf"2.\; F_{{g\\parallel}} = m g \sin\theta = ({mass_kg})(9{{,}}8)\sin({_fmt_sa(theta_deg)}^\circ) = {_fmt_sa(f_parallel, 2)}\text{{ N}}\n"
        rf"3.\; \text{{At constant speed, }} a = 0 \implies F_D = F_{{g\\parallel}} + f_k = {_fmt_sa(f_parallel, 2)} + {f_k} = {_fmt_sa(f_engine, 2)}\text{{ N}}\n"
        rf"4.\; P = F_D v = ({_fmt_sa(f_engine, 2)})({_fmt_sa(v_ms)}) = {_fmt_sa(power_w, 2)}\text{{ W}} = {_fmt_sa(power_kw, 2)}\text{{ kW}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Free-body diagram: 4 forces correctly directed", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Parallel gravitational force: {_fmt_sa(f_parallel, 2)} N", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Total driving force: {_fmt_sa(f_engine, 2)} N", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Engine power output: {_fmt_sa(power_kw, 2)} kW", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_parallel_gravity_component", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The engine must overcome both the parallel component of gravity ($mg\\sin\\theta$) and friction ($f_k$).",
        "tier_2": "Calculate $F_D = mg\\sin\\theta + f_k$. Then multiply by speed $v$ to find power.",
        "tier_3": f"$F_D = {_fmt_sa(f_engine, 2)}\\text{{ N}}$ and $P = {_fmt_sa(power_kw, 2)}\\text{{ kW}}$.",
    }

    return {
        "id": f"ps_wep_42_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_42_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "42_power_vehicle_climbing_rough_incline",
        "learning_objective_id": "ps_wep_42_incline_power",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_cos_instead_of_sin_for_parallel_gravity", "forgot_friction_in_driving_force"],
        "keywords": ["vehicle climbing", "inclined road", "power", "driving force"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 43: Borehole submersible pump power
def _b43_borehole_submersible_pump_power(r: random.Random) -> Dict[str, Any]:
    vol_litres = r.choice([1200, 1800, 2400, 3000, 3600])  # per hour
    depth_m = r.choice([40.0, 50.0, 60.0, 80.0])
    eff_percent = r.choice([60, 70, 75, 80])
    eff = eff_percent / 100.0

    # 1 L of water = 1 kg -> mass in 1 hour (3600 s)
    mass_kg = vol_litres * 1.0
    dt_s = 3600.0  # 1 hour
    work_out = mass_kg * G_ACCEL * depth_m
    p_out = work_out / dt_s
    p_in = p_out / eff

    prompt = (
        f"A submersible borehole pump on a Karoo farm delivers ${vol_litres}\\text{{ litres}}$ of water per hour "
        f"from a deep underground water table located $h = {_fmt_sa(depth_m)}\\text{{ m}}$ below the surface.\n"
        f"Density of water = $1000\\text{{ kg/m}}^3$ ($1\\text{{ litre}} = 1\\text{{ kg}}$), and $g = 9{{,}}8\\text{{ m/s}}^2$.\n\n"
        f"1. Calculate the total mass $m$ of water pumped in one hour.\n"
        f"2. Calculate the minimum work done by the pump to lift this volume of water to ground level in one hour.\n"
        f"3. Calculate the useful power output ($P_{{\\text{{out}}}}$) of the pump.\n"
        f"4. If the overall mechanical efficiency of the pump system is ${eff_percent}\\%$, calculate the electrical power input ($P_{{\\text{{in}}}}$) required to operate the pump in watts ($\\text{{W}}$)."
    )

    ans_latex = (
        rf"1.\; m = {vol_litres}\text{{ L}} \times 1\text{{ kg/L}} = {vol_litres}\text{{ kg}}\n"
        rf"2.\; W = m g h = ({vol_litres})(9{{,}}8)({_fmt_sa(depth_m)}) = {_fmt_sa(work_out, 2)}\text{{ J}}\n"
        rf"3.\; P_{{\text{{out}}}} = \frac{{W}}{{\Delta t}} = \frac{{{_fmt_sa(work_out, 2)}}}{{3600\text{{ s}}}} = {_fmt_sa(p_out, 2)}\text{{ W}}\n"
        rf"4.\; \text{{Efficiency }} \eta = \frac{{P_{{\text{{out}}}}}}{{P_{{\text{{in}}}}}} \times 100\% \implies P_{{\text{{in}}}} = \frac{{P_{{\text{{out}}}}}}{{\eta}} = \frac{{{_fmt_sa(p_out, 2)}}}{{{_fmt_sa(eff)}}} = {_fmt_sa(p_in, 2)}\text{{ W}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Mass calculation: {vol_litres} kg", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Work to lift water: {_fmt_sa(work_out, 2)} J", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Useful power output: {_fmt_sa(p_out, 2)} W", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Electrical power input: {_fmt_sa(p_in, 2)} W", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_time_conversion_hours_to_seconds", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "1 litre of water has a mass of 1 kg. Convert 1 hour to 3600 seconds.",
        "tier_2": "Work done is $W = mgh$. Power output is $P_{\\text{out}} = W / 3600$.",
        "tier_3": f"$P_{{\\text{{out}}}} = {_fmt_sa(p_out, 2)}\\text{{ W}}$ and $P_{{\\text{{in}}}} = {_fmt_sa(p_in, 2)}\\text{{ W}}$.",
    }

    return {
        "id": f"ps_wep_43_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_43_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "43_borehole_submersible_pump_power",
        "learning_objective_id": "ps_wep_43_borehole_pump",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["multiplied_by_efficiency_instead_of_dividing_for_pin", "used_60s_instead_of_3600s_for_1_hour"],
        "keywords": ["borehole pump", "efficiency", "power input", "lifting water"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 6,
    }


# Archetype 44: Hydroelectric pumped storage generation power
def _b44_hydroelectric_pump_storage_generation_power(r: random.Random) -> Dict[str, Any]:
    flow_rate_m3_s = r.choice([25.0, 30.0, 40.0, 50.0])
    head_height_m = r.choice([250.0, 300.0, 350.0, 400.0])
    eff_percent = r.choice([85, 88, 90])
    eff = eff_percent / 100.0

    # 1 m^3 of water = 1000 kg
    mass_per_sec = flow_rate_m3_s * 1000.0
    p_hydro_ideal = mass_per_sec * G_ACCEL * head_height_m  # Watts
    p_elec_actual = p_hydro_ideal * eff
    p_elec_mw = p_elec_actual / 1e6

    prompt = (
        f"At a South African pumped-storage hydroelectric power station (such as Drakensberg or Ingula), "
        f"water falls through penstock pipes from an upper reservoir through an effective vertical head of $h = {_fmt_sa(head_height_m)}\\text{{ m}}$. "
        f"Water flows through the turbines at a volumetric rate of $Q = {_fmt_sa(flow_rate_m3_s)}\\text{{ m}}^3\\text{{/s}}$.\n"
        f"Density of water = $1000\\text{{ kg/m}}^3$, and $g = 9{{,}}8\\text{{ m/s}}^2$.\n\n"
        f"1. Calculate the mass of water flowing through the turbines per second.\n"
        f"2. Calculate the rate of gravitational potential energy released by the water ($P_{{\\text{{hydro}}}}$) in megawatts ($\\text{{MW}}$).\n"
        f"3. If the combined turbine-generator system has an efficiency of ${eff_percent}\\%$, calculate the electrical power generated in megawatts ($\\text{{MW}}$)."
    )

    ans_latex = (
        rf"1.\; \frac{{m}}{{\Delta t}} = \rho Q = (1000\\text{{ kg/m}}^3)({_fmt_sa(flow_rate_m3_s)}\\text{{ m}}^3\\text{{/s}}) = {_fmt_sa(mass_per_sec)}\\text{{ kg/s}}\n"
        rf"2.\; P_{{\text{{hydro}}}} = \frac{{\Delta E_p}}{{\Delta t}} = \left(\frac{{m}}{{\Delta t}}\right) g h = ({_fmt_sa(mass_per_sec)})(9{{,}}8)({_fmt_sa(head_height_m)}) = {_fmt_sa(p_hydro_ideal, 2)}\text{{ W}} = {_fmt_sa(p_hydro_ideal / 1e6, 2)}\text{{ MW}}\n"
        rf"3.\; P_{{\text{{elec}}}} = \eta P_{{\text{{hydro}}}} = ({_fmt_sa(eff)})({_fmt_sa(p_hydro_ideal / 1e6, 2)}\text{{ MW}}) = {_fmt_sa(p_elec_mw, 2)}\text{{ MW}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Mass flow rate: {_fmt_sa(mass_per_sec)} kg/s", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Ideal hydraulic power: {_fmt_sa(p_hydro_ideal / 1e6, 2)} MW", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Generated electrical power: {_fmt_sa(p_elec_mw, 2)} MW", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "incorrect_megawatt_conversion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Mass flow rate is $\\rho Q$. In 1 second, mass is $1000 \\times Q$ kg.",
        "tier_2": "Power is rate of potential energy release: $P = \\frac{m}{\\Delta t} g h$. $1\\text{ MW} = 10^6\\text{ W}$.",
        "tier_3": f"$P_{{\\text{{hydro}}}} = {_fmt_sa(p_hydro_ideal / 1e6, 2)}\\text{{ MW}}$ and $P_{{\\text{{elec}}}} = {_fmt_sa(p_elec_mw, 2)}\\text{{ MW}}$.",
    }

    return {
        "id": f"ps_wep_44_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_44_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "44_hydroelectric_pump_storage_generation_power",
        "learning_objective_id": "ps_wep_44_hydro_power",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_water_density_factor", "confused_megawatts_with_kilowatts"],
        "keywords": ["hydroelectric", "pumped storage", "efficiency", "megawatts"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 45: Escalator human passenger transport power
def _b45_escalator_human_passenger_transport_power(r: random.Random) -> Dict[str, Any]:
    n_passengers = r.choice([40, 50, 60, 75])  # per minute
    avg_mass_kg = r.choice([65.0, 70.0, 75.0])
    h_vert_m = r.choice([6.0, 8.0, 10.0])
    dt_s = 60.0

    total_mass = n_passengers * avg_mass_kg
    work_useful = total_mass * G_ACCEL * h_vert_m
    power_useful_w = work_useful / dt_s
    power_useful_kw = power_useful_w / 1000.0

    prompt = (
        f"An escalator in a shopping mall transports passengers between two floors separated by a vertical height "
        f"of $h = {_fmt_sa(h_vert_m)}\\text{{ m}}$. During peak shopping hours, the escalator moves ${n_passengers}\\text{{ passengers}}$ per minute "
        f"at constant speed. The average mass per passenger is $m_{{\\text{{ave}}}} = {_fmt_sa(avg_mass_kg)}\\text{{ kg}}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the total mass $M$ of passengers elevated per minute.\n"
        f"2. Calculate the minimum work done by the escalator motor in one minute just to elevate these passengers.\n"
        f"3. Determine the minimum average power developed by the motor to carry the passenger load, in kilowatts ($\\text{{kW}}$)."
    )

    ans_latex = (
        rf"1.\; M = {n_passengers} \times {_fmt_sa(avg_mass_kg)} = {_fmt_sa(total_mass)}\text{{ kg}}\n"
        rf"2.\; W = M g h = ({_fmt_sa(total_mass)})(9{{,}}8)({_fmt_sa(h_vert_m)}) = {_fmt_sa(work_useful, 2)}\text{{ J}}\n"
        rf"3.\; P = \frac{{W}}{{\Delta t}} = \frac{{{_fmt_sa(work_useful, 2)}}}{{60\text{{ s}}}} = {_fmt_sa(power_useful_w, 2)}\text{{ W}} = {_fmt_sa(power_useful_kw, 2)}\text{{ kW}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Total passenger mass: {_fmt_sa(total_mass)} kg", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Work done in one minute: {_fmt_sa(work_useful, 2)} J", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Power in kW: {_fmt_sa(power_useful_kw, 2)} kW", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_time_seconds_conversion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Multiply number of passengers by average mass to find total mass elevated.",
        "tier_2": "Calculate work $W = Mgh$, then divide by 60 seconds to find power in watts.",
        "tier_3": f"$W = {_fmt_sa(work_useful, 2)}\\text{{ J}}$ and $P = {_fmt_sa(power_useful_kw, 2)}\\text{{ kW}}$.",
    }

    return {
        "id": f"ps_wep_45_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_45_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "45_escalator_human_passenger_transport_power",
        "learning_objective_id": "ps_wep_45_escalator_power",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_incline_length_instead_of_vertical_height_for_mgh", "forgot_to_divide_by_60_seconds"],
        "keywords": ["escalator", "passenger transport", "average power", "lifting work"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 46: Mechanical efficiency of machines
def _b46_mechanical_efficiency_of_machines(r: random.Random) -> Dict[str, Any]:
    p_in_kw = r.choice([5.0, 7.5, 10.0, 15.0])
    p_in_w = p_in_kw * 1000.0
    mass_kg = r.choice([300, 400, 500, 600])
    v_const = r.choice([1.0, 1.2, 1.5])  # m/s

    f_up = mass_kg * G_ACCEL
    p_out_w = f_up * v_const
    eff_percent = (p_out_w / p_in_w) * 100.0
    p_lost_kw = (p_in_w - p_out_w) / 1000.0

    prompt = (
        f"An electric crane motor draws $P_{{\\text{{in}}}} = {_fmt_sa(p_in_kw)}\\text{{ kW}}$ of electrical power while lifting "
        f"a crate of mass $m = {mass_kg}\\text{{ kg}}$ vertically upward at a constant speed of $v = {_fmt_sa(v_const)}\\text{{ m/s}}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Define the **mechanical efficiency** of a machine in words.\n"
        f"2. Calculate the mechanical power output ($P_{{\\text{{out}}}}$) developed by the crane.\n"
        f"3. Calculate the percentage efficiency of the crane system.\n"
        f"4. Determine the rate at which electrical energy is converted into heat and sound in the motor and gears (in $\\text{{kW}}$)."
    )

    ans_latex = (
        rf"1.\; \text{{The ratio of useful work/power output to total work/power input, usually expressed as a percentage.}}\n"
        rf"2.\; P_{{\text{{out}}}} = F v = (m g) v = ({mass_kg} \times 9{{,}}8)({_fmt_sa(v_const)}) = {_fmt_sa(p_out_w, 2)}\text{{ W}}\n"
        rf"3.\; \text{{Efficiency }} \eta = \frac{{P_{{\text{{out}}}}}}{{P_{{\text{{in}}}}}} \times 100\% = \frac{{{_fmt_sa(p_out_w, 2)}}}{{{_fmt_sa(p_in_w)}}} \times 100\% = {_fmt_sa(eff_percent, 2)}\%\n"
        rf"4.\; P_{{\text{{lost}}}} = P_{{\text{{in}}}} - P_{{\text{{out}}}} = {_fmt_sa(p_in_kw)} - {_fmt_sa(p_out_w / 1000.0, 2)} = {_fmt_sa(p_lost_kw, 2)}\text{{ kW}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of efficiency", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Useful power output: {_fmt_sa(p_out_w, 2)} W", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Percentage efficiency: {_fmt_sa(eff_percent, 2)}%", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Power lost as heat: {_fmt_sa(p_lost_kw, 2)} kW", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "inverted_efficiency_ratio", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Efficiency is given by $\\eta = \\frac{P_{\\text{out}}}{P_{\\text{in}}} \\times 100\\%$.",
        "tier_2": "Useful output power is $P_{\\text{out}} = mgv$. Power input is given in kW (multiply by 1000 for W).",
        "tier_3": f"$P_{{\\text{{out}}}} = {_fmt_sa(p_out_w, 2)}\\text{{ W}}$, efficiency = {_fmt_sa(eff_percent, 2)}%, lost power = {_fmt_sa(p_lost_kw, 2)} kW.",
    }

    return {
        "id": f"ps_wep_46_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_46_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "46_mechanical_efficiency_of_machines",
        "learning_objective_id": "ps_wep_46_machine_efficiency",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["inverted_efficiency_fraction", "assumed_efficiency_can_exceed_100_percent"],
        "keywords": ["mechanical efficiency", "power output", "power input", "energy losses"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 47: Kilowatt-hour and electrical energy cost
def _b47_kilowatt_hour_and_electrical_energy_cost(r: random.Random) -> Dict[str, Any]:
    power_w = r.choice([1500, 2000, 2500, 3000])  # e.g. geyser or heater
    hours_per_day = r.choice([3.0, 4.0, 5.0])
    days = 30
    tariff_rands = r.choice([2.50, 2.80, 3.20, 3.50])

    power_kw = power_w / 1000.0
    energy_kwh_per_day = power_kw * hours_per_day
    total_kwh = energy_kwh_per_day * days
    total_cost = total_kwh * tariff_rands
    energy_joules_1kwh = 3.6e6
    total_joules = total_kwh * energy_joules_1kwh

    prompt = (
        f"A domestic water heater (geyser) is rated at $P = {power_w}\\text{{ W}}$. "
        f"The geyser elements operate for an average of ${_fmt_sa(hours_per_day)}\\text{{ hours}}$ per day over a $30\\text{{-day}}$ month. "
        f"The municipal tariff for electricity is $\\text{{R}}{_fmt_sa(tariff_rands)}\\text{{ per kilowatt-hour (kWh)}}$.\n\n"
        f"1. Define the unit **kilowatt-hour (kWh)** in terms of power and time.\n"
        f"2. Show by calculation that $1\\text{{ kWh}} = 3{{,}}6 \\times 10^6\\text{{ J}}$.\n"
        f"3. Calculate the total electrical energy consumed by the geyser in one month in kilowatt-hours ($\\text{{kWh}}$).\n"
        f"4. Calculate the cost to operate the geyser for the month, in rands ($\\text{{R}}$)."
    )

    ans_latex = (
        rf"1.\; \text{{A kilowatt-hour is the amount of electrical energy consumed by a }} 1\text{{ kW}} \text{{ appliance operating continuously for }} 1\text{{ hour}}.\n"
        rf"2.\; 1\text{{ kWh}} = 1000\text{{ W}} \times 3600\text{{ s}} = 3{{,}}6 \\times 10^6\text{{ J}}\n"
        rf"3.\; E = P \times t = ({_fmt_sa(power_kw)}\\text{{ kW}}) \times ({_fmt_sa(hours_per_day)}\\text{{ h/day}} \times 30\\text{{ days}}) = {_fmt_sa(total_kwh, 2)}\\text{{ kWh}}\n"
        rf"4.\; \text{{Cost}} = {_fmt_sa(total_kwh, 2)}\\text{{ kWh}} \times \\text{{R}}{_fmt_sa(tariff_rands)} = \\text{{R}}{_fmt_sa(total_cost, 2)}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of kilowatt-hour", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Conversion: 1 kWh = 3.6 * 10^6 J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Monthly kWh calculation: {_fmt_sa(total_kwh, 2)} kWh", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Total cost in rands: R{_fmt_sa(total_cost, 2)}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_currency_or_kwh_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "$1\\text{ kWh} = 1000\\text{ W} \\times 3600\\text{ s} = 3.6 \\times 10^6\\text{ J}$.",
        "tier_2": "Convert power to kW: $P = {power_w}/1000 = {power_kw}\\text{ kW}$. Multiply by total hours.",
        "tier_3": f"Total energy = {_fmt_sa(total_kwh, 2)}\\text{{ kWh}}, and cost = R{_fmt_sa(total_cost, 2)}.",
    }

    return {
        "id": f"ps_wep_47_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_47_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "47_kilowatt_hour_and_electrical_energy_cost",
        "learning_objective_id": "ps_wep_47_kwh_cost",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["treated_kwh_as_unit_of_power_instead_of_energy", "forgot_to_convert_watts_to_kilowatts"],
        "keywords": ["kilowatt-hour", "electrical energy", "tariff cost", "joules conversion"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 5,
    }


# Archetype 48: Work energy power composite multistage rider
def _b48_work_energy_power_composite_multistage_rider(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([4.0, 5.0, 8.0, 10.0])
    h_start = r.choice([3.0, 4.0, 5.0])
    # Section 1: frictionless curve from height h_start to ground level
    v_ground = math.sqrt(2 * G_ACCEL * h_start)

    # Section 2: rough horizontal surface of length L with friction mu_k
    l_rough = r.choice([4.0, 5.0, 6.0])
    mu_k = r.choice([0.15, 0.20, 0.25])
    f_k = mu_k * mass_kg * G_ACCEL
    w_f = -f_k * l_rough
    ek_ground = 0.5 * mass_kg * (v_ground ** 2)
    ek_after_rough = ek_ground + w_f
    v_after_rough = math.sqrt(max(0.1, 2 * ek_after_rough / mass_kg))

    # Section 3: smooth slope to max height h_final
    h_final = ek_after_rough / (mass_kg * G_ACCEL)

    prompt = (
        f"A laboratory test car of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is released from rest at point A "
        f"at height $h_A = {_fmt_sa(h_start)}\\text{{ m}}$ on a frictionless curved ramp ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"- **Stage 1**: The car glides down the frictionless ramp to point B at ground level ($h_B = 0\\text{{ m}}$).\n"
        f"- **Stage 2**: From point B, it travels across a rough horizontal track BC of length $L = {_fmt_sa(l_rough)}\\text{{ m}}$ "
        f"where the coefficient of kinetic friction is $\\mu_k = {_fmt_sa(mu_k)}$.\n"
        f"- **Stage 3**: Past point C, the track becomes frictionless again and curves upward to point D.\n\n"
        f"1. Use conservation of mechanical energy to determine the speed of the car at point B.\n"
        f"2. Calculate the work done by friction along track BC.\n"
        f"3. Use the work-energy theorem ($W_{{\\text{{net}}}} = \\Delta E_k$) to find the speed of the car as it reaches point C.\n"
        f"4. Determine the maximum vertical height $h_D$ reached by the car on the final smooth incline."
    )

    ans_latex = (
        rf"1.\; E_{{\text{{mech,A}}}} = E_{{\text{{mech,B}}}} \implies m g h_A = \frac{{1}}{{2}} m v_B^2\n"
        rf"\quad v_B = \sqrt{{2 g h_A}} = \sqrt{{2(9{{,}}8)({_fmt_sa(h_start)})}} = {_fmt_sa(v_ground, 2)}\text{{ m/s}}\n"
        rf"2.\; W_f = f_k L \cos(180^\circ) = -(\mu_k m g) L = -({_fmt_sa(mu_k)})({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(l_rough)}) = {_fmt_sa(w_f, 2)}\text{{ J}}\n"
        rf"3.\; W_{{\text{{net}}}} = W_f = \frac{{1}}{{2}} m v_C^2 - \frac{{1}}{{2}} m v_B^2\n"
        rf"\quad {_fmt_sa(w_f, 2)} = \frac{{1}}{{2}}({_fmt_sa(mass_kg)})v_C^2 - {_fmt_sa(ek_ground, 2)}\n"
        rf"\quad \frac{{1}}{{2}}({_fmt_sa(mass_kg)})v_C^2 = {_fmt_sa(ek_after_rough, 2)}\implies v_C = {_fmt_sa(v_after_rough, 2)}\text{{ m/s}}\n"
        rf"4.\; E_{{\text{{mech,C}}}} = E_{{\text{{mech,D}}}} \implies \frac{{1}}{{2}} m v_C^2 = m g h_D\n"
        rf"\quad h_D = \frac{{{_fmt_sa(ek_after_rough, 2)}}}{{({_fmt_sa(mass_kg)})(9{{,}}8)}} = {_fmt_sa(h_final, 2)}\text{{ m}}"
    )

    marking_schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": f"Speed at B: {_fmt_sa(v_ground, 2)} m/s", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Work by friction BC: {_fmt_sa(w_f, 2)} J", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Speed at C: {_fmt_sa(v_after_rough, 2)} m/s", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Maximum final height at D: {_fmt_sa(h_final, 2)} m", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_height_speed", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Break the motion into stages: Stage 1 is energy conservation, Stage 2 has friction work, Stage 3 is energy conservation.",
        "tier_2": "At B, $v_B = \\sqrt{2gh_A}$. On BC, $W_f = -\\mu_k mg L$. At D, $mgh_D = E_{kC}$.",
        "tier_3": f"$v_B = {_fmt_sa(v_ground, 2)}\\text{{ m/s}}$, $W_f = {_fmt_sa(w_f, 2)}\\text{{ J}}$, $v_C = {_fmt_sa(v_after_rough, 2)}\\text{{ m/s}}$, $h_D = {_fmt_sa(h_final, 2)}\\text{{ m}}$.",
    }

    return {
        "id": f"ps_wep_48_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_48_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "48_work_energy_power_composite_multistage_rider",
        "learning_objective_id": "ps_wep_48_multistage_composite",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["treated_entire_track_as_frictionless", "forgot_to_carry_forward_kinetic_energy_at_c"],
        "keywords": ["multistage track", "friction work", "energy conservation", "maximum height"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 7,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 8,
    }


# Archetype 49: Work energy power capstone synthesis
def _b49_work_energy_power_capstone_synthesis(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([500, 600, 800, 1000])
    h_winch = r.choice([15.0, 20.0, 25.0])
    dt_winch = r.choice([20.0, 25.0, 30.0])
    v_top = h_winch / dt_winch
    f_lift = mass_kg * G_ACCEL
    p_winch = f_lift * v_top

    # then package slides down rough chute of angle 30 deg, length 10 m, friction 200 N
    l_chute = 10.0
    theta_chute = 30.0
    h_chute = l_chute * math.sin(math.radians(theta_chute))  # 5.0 m
    f_k_chute = r.choice([150.0, 200.0, 250.0])
    w_nc_chute = -f_k_chute * l_chute
    delta_ep_chute = -mass_kg * G_ACCEL * h_chute
    ek_bottom = w_nc_chute - delta_ep_chute
    vf_chute = math.sqrt(2 * ek_bottom / mass_kg)

    prompt = (
        f"A mining conveyance cage of mass $m = {mass_kg}\\text{{ kg}}$ is hoisted vertically from the bottom of a shaft "
        f"through a vertical height of $h_1 = {_fmt_sa(h_winch)}\\text{{ m}}$ at a steady speed in $\\Delta t = {_fmt_sa(dt_winch)}\\text{{ s}}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. State the Work-Energy Theorem in words.\n"
        f"2. Calculate the power developed by the hoist winch motor during the vertical lift, in kilowatts ($\\text{{kW}}$).\n"
        f"3. At the surface, the ore is loaded into a bin that slides from rest down a rough discharge chute of length $L = {_fmt_sa(l_chute)}\\text{{ m}}$ "
        f"inclined at $30^\\circ$ to the horizontal. A constant kinetic friction force of $f_k = {_fmt_sa(f_k_chute)}\\text{{ N}}$ acts on the bin.\n"
        f"   - (a) Calculate the work done by non-conservative forces ($W_{{\\text{{nc}}}}$) along the chute.\n"
        f"   - (b) Use $W_{{\\text{{nc}}}} = \\Delta E_k + \\Delta E_p$ to calculate the speed of the bin at the bottom of the chute."
    )

    ans_latex = (
        rf"1.\; \text{{The work done on an object by the net force is equal to the change in the object's kinetic energy.}}\n"
        rf"2.\; \text{{Lifting force }} F = mg = ({mass_kg})(9{{,}}8) = {_fmt_sa(f_lift, 2)}\text{{ N}}\n"
        rf"\quad P = \frac{{W}}{{\Delta t}} = \frac{{F h_1}}{{\Delta t}} = \frac{{({_fmt_sa(f_lift, 2)})({_fmt_sa(h_winch)})}}{{{_fmt_sa(dt_winch)}}} = {_fmt_sa(p_winch, 2)}\text{{ W}} = {_fmt_sa(p_winch / 1000.0, 2)}\text{{ kW}}\n"
        rf"3.\; \text{{(a) }} W_{{\text{{nc}}}} = f_k L \cos(180^\circ) = ({_fmt_sa(f_k_chute)})({_fmt_sa(l_chute)})(-1) = {_fmt_sa(w_nc_chute, 2)}\text{{ J}}\n"
        rf"\quad \text{{(b) }} W_{{\text{{nc}}}} = \Delta E_k + \Delta E_p\n"
        rf"\quad \Delta E_p = -m g (L\sin 30^\circ) = -({mass_kg})(9{{,}}8)({_fmt_sa(h_chute)}) = {_fmt_sa(delta_ep_chute, 2)}\text{{ J}}\n"
        rf"\quad {_fmt_sa(w_nc_chute, 2)} = \frac{{1}}{{2}}({mass_kg})v_f^2 + ({_fmt_sa(delta_ep_chute, 2)})\n"
        rf"\quad \frac{{1}}{{2}}({mass_kg})v_f^2 = {_fmt_sa(ek_bottom, 2)}\implies v_f = {_fmt_sa(vf_chute, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Statement of Work-Energy Theorem", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Hoist power calculation: {_fmt_sa(p_winch / 1000.0, 2)} kW", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"W_nc along chute: {_fmt_sa(w_nc_chute, 2)} J", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Speed at bottom of chute: {_fmt_sa(vf_chute, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Recall: Work-Energy theorem states that $W_{\\text{net}} = \\Delta E_k$. Power is $W/\\Delta t$.",
        "tier_2": "For the chute, $h = 10\\sin(30^\\circ) = 5\\text{ m}$. Use $W_{\\text{nc}} = \\Delta E_k + \\Delta E_p$.",
        "tier_3": f"Power = {_fmt_sa(p_winch / 1000.0, 2)}\\text{{ kW}}$, $W_{{\\text{{nc}}}} = {_fmt_sa(w_nc_chute, 2)}\\text{{ J}}$, $v_f = {_fmt_sa(vf_chute, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_49_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_49_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "49_work_energy_power_capstone_synthesis",
        "learning_objective_id": "ps_wep_49_capstone_synthesis",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_work_energy_theorem_with_wnc_theorem", "omitted_gravitational_potential_energy_on_incline"],
        "keywords": ["capstone synthesis", "hoist power", "rough chute", "W_nc theorem"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 7,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 8,
    }


# Archetype 50: Work energy power diagnostic autopsy
def _b50_work_energy_power_diagnostic_autopsy(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([2.0, 3.0, 4.0, 5.0])
    h_m = r.choice([3.0, 4.0, 5.0])
    vi = 0.0
    w_g = mass_kg * G_ACCEL * h_m
    v_actual = math.sqrt(2 * G_ACCEL * h_m)

    prompt = (
        f"A learner is analyzing a falling ball of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ released from rest "
        f"from height $h = {_fmt_sa(h_m)}\\text{{ m}}$ above the floor (free fall in a vacuum, $g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"The learner presents the following written argument:\n"
        f'> *"In this problem, gravity does positive work $W_g = +mgh$. At the same time, gravitational potential energy is converted '
        f'to kinetic energy, so $W_{{\\text{{net}}}} = W_g + \\Delta E_p = mgh + mgh = 2mgh$. Therefore, $\\frac{{1}}{{2}}mv^2 = 2mgh$, '
        f'which gives $v = \\sqrt{{4gh}}$."*\n\n'
        f"1. Identify the fundamental conceptual error in the learner's reasoning (the 'double-counting' error).\n"
        f"2. Explain clearly whether gravity should be included as work done ($W_{{\\text{{net}}}}$) OR as potential energy ($\\Delta E_p$), and why both cannot be added together.\n"
        f"3. Calculate the correct final speed $v$ using:\n"
        f"   - (a) The Work-Energy Theorem: $W_{{\\text{{net}}}} = \\Delta E_k$\n"
        f"   - (b) The Conservation of Mechanical Energy: $E_{{\\text{{mech,i}}}} = E_{{\\text{{mech,f}}}}$\n"
        f"4. Confirm that both valid methods yield the identical numerical speed."
    )

    ans_latex = (
        rf"1.\; \text{{The learner double-counted gravity by including it both as work done }} W_g \text{{ and as change in potential energy }} \Delta E_p.\n"
        rf"2.\; \text{{Gravitational potential energy is defined such that }} W_g = -\Delta E_p. \text{{ Therefore, in }} W_{{\text{{net}}}} = \Delta E_k\text{{, gravity is already counted in }} W_{{\text{{net}}}}. \text{{ In }} W_{{\text{{nc}}}} = \Delta E_k + \Delta E_p\text{{, gravity is accounted for inside }} \Delta E_p\text{{ and }} W_{{\text{{nc}}}} = 0.\n"
        rf"3.\; \text{{(a) Work-Energy Theorem: }} W_{{\text{{net}}}} = W_g = mgh = \frac{{1}}{{2}} m v^2 \implies v = \sqrt{{2gh}} = \sqrt{{2(9{{,}}8)({_fmt_sa(h_m)})}} = {_fmt_sa(v_actual, 2)}\text{{ m/s}}.\n"
        rf"\quad \text{{(b) Conservation of Mechanical Energy: }} mgh + 0 = 0 + \frac{{1}}{{2}} m v^2 \implies v = \sqrt{{2gh}} = {_fmt_sa(v_actual, 2)}\text{{ m/s}}.\n"
        rf"4.\; \text{{Both methods give }} v = {_fmt_sa(v_actual, 2)}\text{{ m/s}}, \text{{ confirming that }} W_g \text{{ and }} -\Delta E_p \text{{ are the exact same physical quantity.}}"
    )

    marking_schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Identification of double-counting misconception", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Explanation of relationship W_g = -Delta Ep", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Correct speed via Work-Energy theorem: {_fmt_sa(v_actual, 2)} m/s", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct speed via Conservation of Energy: {_fmt_sa(v_actual, 2)} m/s", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Equivalence verification statement", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "unjustified_assertion_without_w_equals_minus_delta_ep", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Gravitational potential energy is the negative of the work done by gravity: $\\Delta E_p = -W_g$.",
        "tier_2": "If you use $W_{\\text{net}} = \\Delta E_k$, include $W_g$. If you use $W_{\\text{nc}} = \\Delta E_k + \\Delta E_p$, gravity is inside $\\Delta E_p$ and $W_{\\text{nc}} = 0$.",
        "tier_3": f"Correct speed is $v = \\sqrt{{2gh}} = {_fmt_sa(v_actual, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_50_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_50_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "50_work_energy_power_diagnostic_autopsy",
        "learning_objective_id": "ps_wep_50_diagnostic_autopsy",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["double_counted_gravity_as_work_and_potential_energy", "confused_wg_with_wnc"],
        "keywords": ["diagnostic autopsy", "double counting", "Work-Energy Theorem", "potential energy equivalence"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 7,
    }


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_conservative_forces_and_path_independence": _b26_conservative_forces_and_path_independence,
    "27_non_conservative_forces_and_path_dependence": _b27_non_conservative_forces_and_path_dependence,
    "28_work_done_by_non_conservative_forces_theorem": _b28_work_done_by_non_conservative_forces_theorem,
    "29_wnc_on_horizontal_surface_with_friction": _b29_wnc_on_horizontal_surface_with_friction,
    "30_wnc_sliding_down_rough_incline": _b30_wnc_sliding_down_rough_incline,
    "31_wnc_pushed_up_rough_incline": _b31_wnc_pushed_up_rough_incline,
    "32_wnc_falling_with_air_resistance": _b32_wnc_falling_with_air_resistance,
    "33_wnc_curved_roller_coaster_track_with_friction": _b33_wnc_curved_roller_coaster_track_with_friction,
    "34_wnc_ski_jumper_slope_and_friction": _b34_wnc_ski_jumper_slope_and_friction,
    "35_conservation_of_mechanical_energy_isolated_system": _b35_conservation_of_mechanical_energy_isolated_system,
    "36_conservation_of_mechanical_energy_loop_the_loop": _b36_conservation_of_mechanical_energy_loop_the_loop,
    "37_average_power_definition_and_formula": _b37_average_power_definition_and_formula,
    "38_power_lifting_mass_at_constant_speed": _b38_power_lifting_mass_at_constant_speed,
    "39_power_accelerating_vehicle_from_rest": _b39_power_accelerating_vehicle_from_rest,
    "40_power_formula_p_equals_f_v_constant_speed": _b40_power_formula_p_equals_f_v_constant_speed,
    "41_power_car_cruising_against_air_resistance": _b41_power_car_cruising_against_air_resistance,
    "42_power_vehicle_climbing_rough_incline": _b42_power_vehicle_climbing_rough_incline,
    "43_borehole_submersible_pump_power": _b43_borehole_submersible_pump_power,
    "44_hydroelectric_pump_storage_generation_power": _b44_hydroelectric_pump_storage_generation_power,
    "45_escalator_human_passenger_transport_power": _b45_escalator_human_passenger_transport_power,
    "46_mechanical_efficiency_of_machines": _b46_mechanical_efficiency_of_machines,
    "47_kilowatt_hour_and_electrical_energy_cost": _b47_kilowatt_hour_and_electrical_energy_cost,
    "48_work_energy_power_composite_multistage_rider": _b48_work_energy_power_composite_multistage_rider,
    "49_work_energy_power_capstone_synthesis": _b49_work_energy_power_capstone_synthesis,
    "50_work_energy_power_diagnostic_autopsy": _b50_work_energy_power_diagnostic_autopsy,
}
