"""Physical Sciences (Grade 12 Term 1) — Work, Energy and Power Archetypes 01 to 25.

Grounded strictly in the South African National Physical Sciences Curriculum:
- Work done by a constant force: W = F * Delta x * cos(theta).
- Positive work, zero work (perpendicular forces), and negative work (opposing forces).
- Work done by gravity in vertical motion and along inclined planes.
- Net work (W_net) from sum of works or from resultant force (F_net * Delta x * cos(theta)).
- Force vs displacement graphs (area under F-x graph).
- Work-Energy Theorem: W_net = Delta E_k = 1/2 m v_f^2 - 1/2 m v_i^2.

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


# Archetype 01: Work done by a constant horizontal force
def _b01_work_done_constant_horizontal_force(r: random.Random) -> Dict[str, Any]:
    force_n = r.choice([25, 40, 50, 60, 75, 80, 100, 120, 150])
    dx_m = r.choice([4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 15.0])
    work_j = force_n * dx_m

    prompt = (
        f"A warehouse worker applies a constant horizontal force of magnitude $F = {force_n}\\text{{ N}}$ to push a packing crate "
        f"in a straight line through a displacement of $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ in the direction of the force.\n\n"
        f"1. Define the **work done** on an object by a constant force in words.\n"
        f"2. Calculate the work done $W$ by the applied force on the crate."
    )

    ans_latex = (
        rf"1.\; \text{{The product of the magnitude of the force, the magnitude of the displacement, and the cosine of the angle }} \theta \text{{ between them.}}\n"
        rf"2.\; W = F \Delta x \cos\theta = ({force_n})({_fmt_sa(dx_m)})\cos(0^\circ) = {_fmt_sa(work_j)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of work done by a constant force", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Formula: W = F * Delta x * cos(theta)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Substitute theta = 0 deg and evaluate: {_fmt_sa(work_j)} J", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_units_joules", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Use $W = F \\Delta x \\cos\\theta$, where $\\theta$ is the angle between $\\vec{F}$ and $\\Delta\\vec{x}$.",
        "tier_2": "Since the force acts in the direction of motion, $\\theta = 0^\\circ$ and $\\cos(0^\\circ) = 1$.",
        "tier_3": f"$W = {force_n} \\times {_fmt_sa(dx_m)} \\times 1 = {_fmt_sa(work_j)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_01_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_01_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "01_work_done_constant_horizontal_force",
        "learning_objective_id": "ps_wep_01_horizontal_work",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_90_deg_instead_of_0_deg", "confused_work_with_force"],
        "keywords": ["work done", "constant force", "joules"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 02: Work done by a pulling force at an angle above the horizontal
def _b02_work_done_force_at_angle_above_horizontal(r: random.Random) -> Dict[str, Any]:
    force_n = r.choice([40, 50, 60, 80, 100, 120, 150])
    dx_m = r.choice([5.0, 6.0, 8.0, 10.0, 12.0, 15.0])
    theta_deg = r.choice([20, 25, 30, 35, 40, 45, 60])
    work_j = force_n * dx_m * math.cos(math.radians(theta_deg))

    svg = _clean_svg(f"""
<svg viewBox="0 0 380 160" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="160" fill="#f8fafc" rx="8"/>
  <line x1="30" y1="125" x2="350" y2="125" stroke="#475569" stroke-width="3"/>
  <rect x="80" y="75" width="80" height="50" rx="4" fill="#93c5fd" stroke="#1d4ed8" stroke-width="2"/>
  <line x1="160" y1="100" x2="260" y2="100" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="160" y1="100" x2="250" y2="45" stroke="#dc2626" stroke-width="3"/>
  <polygon points="255,42 244,44 249,52" fill="#dc2626"/>
  <text x="260" y="42" font-size="11" font-weight="bold" fill="#b91c1c">F = {force_n} N</text>
  <text x="195" y="92" font-size="11" font-weight="bold" fill="#0f172a">θ = {theta_deg}°</text>
  <text x="190" y="148" font-size="11" fill="#334155" text-anchor="middle">Horizontal displacement Δx = {_fmt_sa(dx_m)} m</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing a crate pulled across a floor through a displacement "
        f"of $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ by a rope exerting a constant tension force of $F = {force_n}\\text{{ N}}$ "
        f"at an angle of $\\theta = {theta_deg}^\\circ$ above the horizontal.\n\n"
        f"1. State which component of the force $\\vec{{F}}$ does work on the crate during its horizontal motion.\n"
        f"2. Calculate the work done by the force $\\vec{{F}}$ over the displacement $\\Delta x$."
    )

    ans_latex = (
        rf"1.\; \text{{The horizontal component }} F_x = F\cos\theta \text{{ parallel to the displacement.}}\n"
        rf"2.\; W = F \Delta x \cos\theta = ({force_n})({_fmt_sa(dx_m)})\cos({theta_deg}^\circ) = {_fmt_sa(work_j, 2)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Identify horizontal component F cos(theta)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Formula: W = F * Delta x * cos(theta)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Substitution and calculation: W = {_fmt_sa(work_j, 2)} J", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "used_sin_instead_of_cos", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Only the component of force parallel to displacement ($F\\cos\\theta$) does work.",
        "tier_2": f"Substitute $F = {force_n}\\text{{ N}}$, $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$, and $\\theta = {theta_deg}^\\circ$ into $W = F \\Delta x \\cos\\theta$.",
        "tier_3": f"$W = {_fmt_sa(work_j, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_02_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_02_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "02_work_done_force_at_angle_above_horizontal",
        "learning_objective_id": "ps_wep_02_angled_pull",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_sin_instead_of_cos_for_horizontal_work", "omitted_angle_factor"],
        "keywords": ["angled force", "work done", "horizontal component"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 03: Work done by a pushing force at an angle below the horizontal
def _b03_work_done_pushing_force_at_angle_below_horizontal(r: random.Random) -> Dict[str, Any]:
    force_n = r.choice([60, 75, 90, 110, 125, 140, 160])
    dx_m = r.choice([6.0, 8.0, 10.0, 12.0, 15.0, 20.0])
    theta_deg = r.choice([25, 30, 35, 40, 45, 50])
    work_j = force_n * dx_m * math.cos(math.radians(theta_deg))

    prompt = (
        f"A gardener pushes a lawnmower forward through a horizontal distance of $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ "
        f"by applying a constant force of $F = {force_n}\\text{{ N}}$ directed downwards along the handle at an angle of "
        f"$\\theta = {theta_deg}^\\circ$ below the horizontal.\n\n"
        f"1. Calculate the magnitude of the downward vertical component $F_y$ of the pushing force, and state how much work $F_y$ does on the lawnmower.\n"
        f"2. Calculate the work done by the applied force $F$ over the ${_fmt_sa(dx_m)}\\text{{ m}}$ displacement."
    )

    fy = force_n * math.sin(math.radians(theta_deg))
    ans_latex = (
        rf"1.\; F_y = F\sin({theta_deg}^\circ) = {_fmt_sa(fy, 2)}\text{{ N; work done by }} F_y \text{{ is }} 0\text{{ J (perpendicular to horizontal displacement).}}\n"
        rf"2.\; W = F \Delta x \cos({theta_deg}^\circ) = ({force_n})({_fmt_sa(dx_m)})\cos({theta_deg}^\circ) = {_fmt_sa(work_j, 2)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate Fy = {_fmt_sa(fy, 2)} N and state W_y = 0 J", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate work W = F * dx * cos({theta_deg}) = {_fmt_sa(work_j, 2)} J", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The vertical component $F_y = F\\sin\\theta$ acts at $90^\\circ$ to the horizontal motion, so it does zero work.",
        "tier_2": "The horizontal component $F_x = F\\cos\\theta$ acts in the direction of motion ($0^\\circ$).",
        "tier_3": f"$W = {force_n} \\times {_fmt_sa(dx_m)} \\times \\cos({theta_deg}^\\circ) = {_fmt_sa(work_j, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_03_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_03_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "03_work_done_pushing_force_at_angle_below_horizontal",
        "learning_objective_id": "ps_wep_03_angled_push",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_downward_push_does_negative_work", "included_vertical_component_in_work"],
        "keywords": ["pushing at angle", "lawnmower", "work done"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 04: Zero work done by perpendicular forces (Normal and Gravity on flat road)
def _b04_zero_work_done_by_perpendicular_forces(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([10, 15, 20, 25, 30, 40, 50, 60])
    dx_m = r.choice([5.0, 8.0, 10.0, 14.0, 18.0, 25.0])
    fg = mass_kg * G_ACCEL

    prompt = (
        f"A heavy toolbox of mass $m = {mass_kg}\\text{{ kg}}$ slides a distance of $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ "
        f"along a horizontal workshop floor ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the magnitude of the normal force $N$ exerted by the floor on the toolbox.\n"
        f"2. Write down the value of the work done on the toolbox by the normal force $W_N$ and by the gravitational force $W_g$, "
        f"and justify your answer using the work formula."
    )

    ans_latex = (
        rf"1.\; N = F_g = mg = ({mass_kg})(9{{,}}8) = {_fmt_sa(fg, 1)}\text{{ N}}\n"
        rf"2.\; W_N = 0\text{{ J and }} W_g = 0\text{{ J because both forces act perpendicular to the displacement (}}\theta = 90^\circ\text{{, and }}\cos 90^\circ = 0\text{{).}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate N = mg = {_fmt_sa(fg, 1)} N", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "State W_N = 0 J and W_g = 0 J", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Justification: theta = 90 deg and cos(90 deg) = 0", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "On a flat horizontal surface with no vertical applied forces, $N = mg$.",
        "tier_2": "What is the angle $\\theta$ between a vertical force ($\\vec{N}$ or $\\vec{F}_g$) and a horizontal displacement $\\Delta\\vec{x}$?",
        "tier_3": f"$N = {_fmt_sa(fg, 1)}\\text{{ N}}$. Since $\\theta = 90^\\circ$ and $\\cos(90^\\circ) = 0$, $W_N = W_g = 0\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_04_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_04_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "04_zero_work_done_by_perpendicular_forces",
        "learning_objective_id": "ps_wep_04_zero_work",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["multiplied_normal_force_by_horizontal_distance", "forgot_cos_90_is_zero"],
        "keywords": ["zero work", "perpendicular force", "normal force"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 05: Negative work done by kinetic friction
def _b05_negative_work_done_by_kinetic_friction(r: random.Random) -> Dict[str, Any]:
    fk_n = r.choice([12, 15, 18, 22, 25, 30, 35, 45, 60])
    dx_m = r.choice([4.0, 6.0, 8.0, 10.0, 12.0, 15.0, 20.0])
    w_f = -fk_n * dx_m

    prompt = (
        f"A wooden block slides across a rough horizontal table through a displacement of $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ "
        f"while experiencing a constant kinetic frictional force of magnitude $f_k = {fk_n}\\text{{ N}}$.\n\n"
        f"1. State the angle $\\theta$ between the kinetic frictional force $\\vec{{f}}_k$ and the displacement $\\Delta\\vec{{x}}$.\n"
        f"2. Calculate the work done $W_f$ by the frictional force on the block, and state what happens to the mechanical energy removed from the block."
    )

    ans_latex = (
        rf"1.\; \theta = 180^\circ\text{{ (friction acts opposite to the direction of motion).}}\n"
        rf"2.\; W_f = f_k \Delta x \cos(180^\circ) = ({fk_n})({_fmt_sa(dx_m)})(-1) = {_fmt_sa(w_f)}\text{{ J. Mechanical energy is converted into internal/thermal energy (heat).}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Angle theta = 180 deg", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate W_f = {_fmt_sa(w_f)} J (must include negative sign)", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Energy dissipated as thermal energy / heat", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_negative_sign_on_friction_work", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Kinetic friction always opposes relative motion, so the angle between $\\vec{f}_k$ and $\\Delta\\vec{x}$ is $180^\\circ$.",
        "tier_2": "Since $\\cos(180^\\circ) = -1$, work done by kinetic friction is negative: $W_f = -f_k \\Delta x$.",
        "tier_3": f"$W_f = {_fmt_sa(w_f)}\\text{{ J}}$ (dissipated as heat).",
    }

    return {
        "id": f"ps_wep_05_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_05_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "05_negative_work_done_by_kinetic_friction",
        "learning_objective_id": "ps_wep_05_friction_work",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_negative_sign_for_opposing_force", "used_cos_0_for_friction"],
        "keywords": ["negative work", "kinetic friction", "cos 180"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 06: Work done by gravity during vertical downward fall
def _b06_work_done_by_gravity_vertical_free_fall(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 8.0, 10.0])
    h_m = r.choice([5.0, 8.0, 10.0, 12.0, 15.0, 20.0, 25.0])
    w_g = mass_kg * G_ACCEL * h_m
    delta_ep = -w_g

    prompt = (
        f"A steel ball of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ falls vertically downwards through a vertical distance "
        f"of $\\Delta y = {_fmt_sa(h_m)}\\text{{ m}}$ near the Earth's surface ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the work done by the gravitational force $W_g$ on the ball during the fall.\n"
        f"2. State the change in gravitational potential energy $\\Delta E_p$ of the ball and relate $\\Delta E_p$ to $W_g$."
    )

    ans_latex = (
        rf"1.\; W_g = F_g \Delta y \cos(0^\circ) = ({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(h_m)})(1) = +{_fmt_sa(w_g, 2)}\text{{ J}}\n"
        rf"2.\; \Delta E_p = -W_g = -{_fmt_sa(w_g, 2)}\text{{ J (potential energy decreases as gravity does positive work).}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula: W_g = mg * Delta y * cos(0 deg)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate W_g = +{_fmt_sa(w_g, 2)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"State Delta E_p = -W_g = {_fmt_sa(delta_ep, 2)} J", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Both gravity $\\vec{F}_g$ and the downward displacement $\\Delta\\vec{y}$ point downwards, so $\\theta = 0^\\circ$.",
        "tier_2": "Thus $W_g = +mgh$, whereas $\\Delta E_p = mg(h_f - h_i) = -mgh = -W_g$.",
        "tier_3": f"$W_g = +{_fmt_sa(w_g, 2)}\\text{{ J}}$, $\\Delta E_p = {_fmt_sa(delta_ep, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_06_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_06_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "06_work_done_by_gravity_vertical_free_fall",
        "learning_objective_id": "ps_wep_06_gravity_work_down",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assigned_negative_sign_to_gravity_work_when_falling", "equated_W_g_to_plus_delta_Ep"],
        "keywords": ["work done by gravity", "free fall", "potential energy relation"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 07: Work done by gravity during upward vertical motion
def _b07_work_done_by_gravity_upward_projection(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([0.5, 0.8, 1.2, 1.5, 2.0, 3.0, 4.0])
    h_m = r.choice([4.0, 6.0, 8.0, 10.0, 12.0, 15.0, 18.0])
    w_g = -mass_kg * G_ACCEL * h_m

    prompt = (
        f"A stone of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is thrown vertically upwards and rises through a vertical "
        f"displacement of $\\Delta y = {_fmt_sa(h_m)}\\text{{ m}}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. State the angle $\\theta$ between the gravitational force $\\vec{{F}}_g$ and the upward displacement $\\Delta\\vec{{y}}$.\n"
        f"2. Calculate the work done by the gravitational force $W_g$ on the stone as it rises."
    )

    ans_latex = (
        rf"1.\; \theta = 180^\circ\text{{ (gravity acts downwards while displacement is upwards).}}\n"
        rf"2.\; W_g = mg \Delta y \cos(180^\circ) = ({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(h_m)})(-1) = {_fmt_sa(w_g, 2)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Angle theta = 180 deg", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Formula: W_g = mg * Delta y * cos(180 deg)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate W_g = {_fmt_sa(w_g, 2)} J (negative)", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_negative_sign", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Gravity acts vertically downwards while the stone moves vertically upwards ($\\theta = 180^\\circ$).",
        "tier_2": "Use $W_g = mg\\Delta y\\cos(180^\\circ) = -mg\\Delta y$.",
        "tier_3": f"$W_g = {_fmt_sa(w_g, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_07_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_07_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "07_work_done_by_gravity_upward_projection",
        "learning_objective_id": "ps_wep_07_gravity_work_up",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_negative_sign_for_upward_motion_gravity_work", "confused_Delta_Ep_with_W_g"],
        "keywords": ["upward projection", "work by gravity", "negative work"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 08: Work done by gravity sliding down an inclined plane
def _b08_work_done_by_gravity_down_inclined_plane(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 15.0])
    dx_m = r.choice([5.0, 6.0, 8.0, 10.0, 12.0])
    alpha_deg = r.choice([20, 25, 30, 35, 40])
    fg_par = mass_kg * G_ACCEL * math.sin(math.radians(alpha_deg))
    w_g = fg_par * dx_m

    svg = _clean_svg(f"""
<svg viewBox="0 0 380 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="180" fill="#f8fafc" rx="8"/>
  <polygon points="50,150 330,150 50,50" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
  <rect x="120" y="65" width="46" height="28" rx="3" transform="rotate(19.6 143 79)" fill="#f87171" stroke="#b91c1c" stroke-width="2"/>
  <text x="275" y="142" font-size="11" font-weight="bold" fill="#0f172a">α = {alpha_deg}°</text>
  <text x="210" y="75" font-size="11" font-weight="bold" fill="#1e293b">m = {_fmt_sa(mass_kg)} kg, Δx = {_fmt_sa(dx_m)} m down</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing a block of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ sliding down a plane "
        f"inclined at an angle of $\\alpha = {alpha_deg}^\\circ$ to the horizontal through a distance of $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the component of the gravitational force parallel to the incline ($F_{{g\\parallel}} = mg\\sin\\alpha$).\n"
        f"2. Calculate the work done by the gravitational force $W_g$ on the block as it slides $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ down the incline."
    )

    ans_latex = (
        rf"1.\; F_{{g\parallel}} = mg\sin\alpha = ({_fmt_sa(mass_kg)})(9{{,}}8)\sin({alpha_deg}^\circ) = {_fmt_sa(fg_par, 2)}\text{{ N}}\n"
        rf"2.\; W_g = F_{{g\parallel}} \Delta x \cos(0^\circ) = ({_fmt_sa(fg_par, 2)})({_fmt_sa(dx_m)})(1) = {_fmt_sa(w_g, 2)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate Fg_parallel = mg sin({alpha_deg}) = {_fmt_sa(fg_par, 2)} N", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate W_g = +{_fmt_sa(w_g, 2)} J", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "used_cos_instead_of_sin_for_parallel_gravity", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The component of gravity parallel to an incline of angle $\\alpha$ is $F_{g\\parallel} = mg\\sin\\alpha$, pointing down the slope.",
        "tier_2": "Since the block moves down the slope, $F_{g\\parallel}$ is in the same direction as $\\Delta x$ ($\\theta = 0^\\circ$).",
        "tier_3": f"$F_{{g\\parallel}} = {_fmt_sa(fg_par, 2)}\\text{{ N}}$, $W_g = +{_fmt_sa(w_g, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_08_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_08_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "08_work_done_by_gravity_down_inclined_plane",
        "learning_objective_id": "ps_wep_08_gravity_down_incline",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_mg_cos_alpha_for_parallel_component", "negative_sign_when_sliding_down"],
        "keywords": ["inclined plane", "parallel component of weight", "work by gravity"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 09: Work done by gravity moving up an inclined plane
def _b09_work_done_by_gravity_up_inclined_plane(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([5.0, 8.0, 10.0, 12.0, 15.0, 20.0])
    dx_m = r.choice([4.0, 6.0, 8.0, 10.0, 15.0])
    alpha_deg = r.choice([15, 20, 25, 30, 35, 40])
    h_vert = dx_m * math.sin(math.radians(alpha_deg))
    w_g = -mass_kg * G_ACCEL * h_vert

    prompt = (
        f"A crate of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is pulled a distance of $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ "
        f"**up** a ramp inclined at $\\alpha = {alpha_deg}^\\circ$ to the horizontal ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the vertical height $h = \\Delta x \\sin\\alpha$ gained by the crate.\n"
        f"2. Calculate the work done by the gravitational force $W_g$ on the crate during this upward displacement."
    )

    ans_latex = (
        rf"1.\; h = \Delta x \sin\alpha = {_fmt_sa(dx_m)}\sin({alpha_deg}^\circ) = {_fmt_sa(h_vert, 3)}\text{{ m}}\n"
        rf"2.\; W_g = mg\sin\alpha \cdot \Delta x \cos(180^\circ) = -mgh = -({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(h_vert, 3)}) = {_fmt_sa(w_g, 2)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate vertical height h = {_fmt_sa(h_vert, 3)} m", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Use W_g = -mg * dx * sin(alpha) or -mgh", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate W_g = {_fmt_sa(w_g, 2)} J (negative)", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_negative_sign", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "As the crate moves up the incline, $F_{g\\parallel} = mg\\sin\\alpha$ points down the incline ($\\theta = 180^\\circ$).",
        "tier_2": "Thus $W_g = -(mg\\sin\\alpha)\\Delta x = -mgh$.",
        "tier_3": f"$h = {_fmt_sa(h_vert, 3)}\\text{{ m}}$, $W_g = {_fmt_sa(w_g, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_09_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_09_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "09_work_done_by_gravity_up_inclined_plane",
        "learning_objective_id": "ps_wep_09_gravity_up_incline",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["positive_work_by_gravity_going_uphill", "used_cos_alpha_for_height"],
        "keywords": ["upward incline", "work by gravity", "vertical height"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 10: Net work from algebraic sum of individual works
def _b10_total_work_from_sum_of_individual_works(r: random.Random) -> Dict[str, Any]:
    fa = r.choice([50, 60, 80, 90, 100, 120])
    fk = r.choice([15, 20, 25, 30, 35])
    dx = r.choice([4.0, 5.0, 6.0, 8.0, 10.0])
    theta = r.choice([0, 20, 25, 30, 35])

    w_a = fa * dx * math.cos(math.radians(theta))
    w_f = -fk * dx
    w_net = w_a + w_f

    prompt = (
        f"A crate is pulled across a rough horizontal floor through a distance of $\\Delta x = {_fmt_sa(dx)}\\text{{ m}}$ "
        f"by a force $F_A = {fa}\\text{{ N}}$ acting at $\\theta = {theta}^\\circ$ above the horizontal. "
        f"A constant frictional force of $f_k = {fk}\\text{{ N}}$ opposes the motion.\n\n"
        f"1. Calculate the work done on the crate by each of the four forces acting on it ($W_A$, $W_f$, $W_N$, and $W_g$).\n"
        f"2. Calculate the net work $W_{{\\text{{net}}}}$ done on the crate by summing the individual works."
    )

    ans_latex = (
        rf"1.\; W_A = ({fa})({_fmt_sa(dx)})\cos({theta}^\circ) = {_fmt_sa(w_a, 2)}\text{{ J}}, \quad "
        rf"W_f = ({fk})({_fmt_sa(dx)})\cos(180^\circ) = {_fmt_sa(w_f, 2)}\text{{ J}}, \quad W_N = 0\text{{ J}}, \quad W_g = 0\text{{ J}}\n"
        rf"2.\; W_{{\text{{net}}}} = W_A + W_f + W_N + W_g = {_fmt_sa(w_a, 2)} + ({_fmt_sa(w_f, 2)}) + 0 + 0 = {_fmt_sa(w_net, 2)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate W_A = {_fmt_sa(w_a, 2)} J", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate W_f = {_fmt_sa(w_f, 2)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "State W_N = 0 J and W_g = 0 J", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Sum works: W_net = {_fmt_sa(w_net, 2)} J", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Compute the work done by each force using $W = F \\Delta x \\cos\\theta$, then add them algebraically.",
        "tier_2": f"$W_A = +{_fmt_sa(w_a, 2)}\\text{{ J}}$, $W_f = {_fmt_sa(w_f, 2)}\\text{{ J}}$, $W_N = W_g = 0\\text{{ J}}$.",
        "tier_3": f"$W_{{\\text{{net}}}} = {_fmt_sa(w_net, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_10_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_10_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "10_total_work_from_sum_of_individual_works",
        "learning_objective_id": "ps_wep_10_sum_of_works",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["added_friction_work_as_positive", "included_weight_in_horizontal_work"],
        "keywords": ["net work", "algebraic sum", "individual works"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 11: Net work from resultant force method (W_net = F_net * dx * cos(0))
def _b11_total_work_from_resultant_force_method(r: random.Random) -> Dict[str, Any]:
    fa = r.choice([70, 85, 100, 120, 140, 160])
    theta = r.choice([15, 20, 25, 30, 40])
    fk = r.choice([15, 20, 25, 30, 40])
    dx = r.choice([5.0, 8.0, 10.0, 12.0, 15.0])

    f_net = fa * math.cos(math.radians(theta)) - fk
    w_net = f_net * dx

    prompt = (
        f"A sled is pulled horizontally across snow through $\\Delta x = {_fmt_sa(dx)}\\text{{ m}}$ by a rope tension of "
        f"$F_A = {fa}\\text{{ N}}$ at $\\theta = {theta}^\\circ$ above the horizontal against a frictional resistance of $f_k = {fk}\\text{{ N}}$.\n\n"
        f"1. Calculate the horizontal resultant force $F_{{\\text{{net}}}} = F_A\\cos\\theta - f_k$ acting on the sled.\n"
        f"2. Hence calculate the net work $W_{{\\text{{net}}}} = F_{{\\text{{net}}}} \\Delta x \\cos(0^\\circ)$ done on the sled."
    )

    ans_latex = (
        rf"1.\; F_{{\text{{net}}}} = F_A\cos({theta}^\circ) - f_k = {fa}\cos({theta}^\circ) - {fk} = {_fmt_sa(f_net, 2)}\text{{ N}}\n"
        rf"2.\; W_{{\text{{net}}}} = F_{{\text{{net}}}} \Delta x \cos(0^\circ) = ({_fmt_sa(f_net, 2)})({_fmt_sa(dx)})(1) = {_fmt_sa(w_net, 2)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate resultant horizontal force F_net = {_fmt_sa(f_net, 2)} N", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate net work W_net = {_fmt_sa(w_net, 2)} J", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "First resolve the horizontal forces to find $F_{\\text{net}} = F_A\\cos\\theta - f_k$.",
        "tier_2": "Multiply $F_{\\text{net}}$ by the displacement $\\Delta x$.",
        "tier_3": f"$F_{{\\text{{net}}}} = {_fmt_sa(f_net, 2)}\\text{{ N}}$, $W_{{\\text{{net}}}} = {_fmt_sa(w_net, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_11_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_11_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "11_total_work_from_resultant_force_method",
        "learning_objective_id": "ps_wep_11_resultant_force_work",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["subtracted_fk_from_unresolved_FA", "used_theta_again_in_Fnet_dx"],
        "keywords": ["resultant force", "net work", "horizontal resolution"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 12: Zero net work at constant velocity
def _b12_total_work_zero_at_constant_velocity(r: random.Random) -> Dict[str, Any]:
    f_pull = r.choice([30, 45, 60, 75, 90, 110, 130])
    dx = r.choice([5.0, 8.0, 10.0, 12.0, 15.0, 20.0])
    vel = r.choice([1.5, 2.0, 2.5, 3.0, 4.0])
    w_pull = f_pull * dx
    w_fric = -w_pull

    prompt = (
        f"A crate is pulled horizontally by a force of $F = {f_pull}\\text{{ N}}$ at a **constant velocity** of $v = {_fmt_sa(vel)}\\text{{ m/s}}$ "
        f"over a rough horizontal floor for a distance of $\\Delta x = {_fmt_sa(dx)}\\text{{ m}}$.\n\n"
        f"1. State the value of the net work $W_{{\\text{{net}}}}$ done on the crate, giving a reason.\n"
        f"2. Calculate the work done by the pulling force $W_F$ and hence state the work done by the frictional force $W_f$."
    )

    ans_latex = (
        rf"1.\; W_{{\text{{net}}}} = 0\text{{ J because the crate moves at constant velocity (}}a = 0 \implies F_{{\text{{net}}}} = 0\text{{ and }}\Delta E_k = 0\text{{).}}\n"
        rf"2.\; W_F = ({f_pull})({_fmt_sa(dx)})\cos(0^\circ) = +{_fmt_sa(w_pull)}\text{{ J}}, \quad W_f = -W_F = {_fmt_sa(w_fric)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "State W_net = 0 J because constant velocity means F_net = 0 / Delta Ek = 0", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate W_F = +{_fmt_sa(w_pull)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"State W_f = {_fmt_sa(w_fric)} J", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Constant velocity means $\\Delta E_k = 0$ and $F_{\\text{net}} = 0$, so $W_{\\text{net}} = 0\\text{ J}$.",
        "tier_2": "Since $W_{\\text{net}} = W_F + W_f = 0$, the work done by friction is equal and opposite to $W_F$.",
        "tier_3": f"$W_F = +{_fmt_sa(w_pull)}\\text{{ J}}$, $W_f = {_fmt_sa(w_fric)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_12_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_12_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "12_total_work_zero_at_constant_velocity",
        "learning_objective_id": "ps_wep_12_constant_velocity_work",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_nonzero_net_work_at_constant_speed", "equated_W_net_to_W_applied"],
        "keywords": ["constant velocity", "zero net work", "balanced forces"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 13: Work from a Force-Displacement graph (trapezoid / rectangle + triangle)
def _b13_work_from_force_displacement_graph_rectangle_triangle(r: random.Random) -> Dict[str, Any]:
    f_max = r.choice([20, 30, 40, 50, 60, 80, 100])
    x1 = r.choice([4, 5, 6, 8, 10])
    x2 = x1 + r.choice([4, 6, 8, 10])

    w_rect = f_max * x1
    w_tri = 0.5 * f_max * (x2 - x1)
    w_total = w_rect + w_tri

    svg = _clean_svg(f"""
<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="200" fill="#f8fafc" rx="8"/>
  <line x1="55" y1="160" x2="345" y2="160" stroke="#1e293b" stroke-width="2"/>
  <line x1="55" y1="160" x2="55" y2="25" stroke="#1e293b" stroke-width="2"/>
  <polygon points="55,160 55,55 185,55 310,160" fill="#bfdbfe" fill-opacity="0.6" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="185" y1="55" x2="185" y2="160" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="45" y="60" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="end">{f_max}</text>
  <text x="55" y="178" font-size="11" fill="#0f172a" text-anchor="middle">0</text>
  <text x="185" y="178" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{x1}</text>
  <text x="310" y="178" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{x2}</text>
  <text x="200" y="195" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">Position x (m)</text>
  <text x="20" y="95" font-size="11" font-weight="bold" fill="#334155" transform="rotate(-90 20 95)" text-anchor="middle">Force F (N)</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing the Force-Position ($F$ vs $x$) graph for a variable horizontal force "
        f"acting on a trolley from $x = 0\\text{{ m}}$ to $x = {x2}\\text{{ m}}$ (with constant force $F = {f_max}\\text{{ N}}$ from $0$ to ${x1}\\text{{ m}}$).\n\n"
        f"1. State what the area under a Force vs Position graph represents physically.\n"
        f"2. Calculate the total work done by the force from $x = 0\\text{{ m}}$ to $x = {x2}\\text{{ m}}$."
    )

    ans_latex = (
        rf"1.\; \text{{The work done by the force.}}\n"
        rf"2.\; W = \text{{Area}}_{{\text{{rect}}}} + \text{{Area}}_{{\text{{tri}}}} = ({f_max})({x1}) + \frac{{1}}{{2}}({f_max})({x2 - x1}) = {_fmt_sa(w_rect)} + {_fmt_sa(w_tri)} = {_fmt_sa(w_total)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "State area under F-x graph represents work done", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Rectangle area = {_fmt_sa(w_rect)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Triangle area = {_fmt_sa(w_tri)} J", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Total work = {_fmt_sa(w_total)} J", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Work done by a variable force equals the area between the $F$-$x$ graph and the position axis.",
        "tier_2": f"Split the region into a rectangle ($0$ to ${x1}\\text{{ m}}$) and a triangle (${x1}\\text{{ m}}$ to ${x2}\\text{{ m}}$).",
        "tier_3": f"$W = {_fmt_sa(w_rect)} + {_fmt_sa(w_tri)} = {_fmt_sa(w_total)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_13_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_13_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "13_work_from_force_displacement_graph_rectangle_triangle",
        "learning_objective_id": "ps_wep_13_fx_graph_positive",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["calculated_gradient_instead_of_area", "forgot_half_in_triangle_area"],
        "keywords": ["Force-displacement graph", "area under graph", "variable force"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 14: Work from Force-Displacement graph with positive and negative lobes
def _b14_work_from_force_displacement_graph_with_negative_lobe(r: random.Random) -> Dict[str, Any]:
    f_pos = r.choice([30, 40, 50, 60, 80])
    f_neg = r.choice([20, 30, 40])
    x1 = r.choice([4, 6, 8, 10])
    x2 = x1 + r.choice([4, 6, 8])

    w_pos = 0.5 * f_pos * x1
    w_neg = -0.5 * f_neg * (x2 - x1)
    w_total = w_pos + w_neg

    svg = _clean_svg(f"""
<svg viewBox="0 0 380 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="210" fill="#f8fafc" rx="8"/>
  <line x1="55" y1="105" x2="345" y2="105" stroke="#1e293b" stroke-width="2"/>
  <line x1="55" y1="20" x2="55" y2="190" stroke="#1e293b" stroke-width="2"/>
  <polygon points="55,105 125,35 195,105" fill="#bbf7d0" fill-opacity="0.6" stroke="#16a34a" stroke-width="2"/>
  <polygon points="195,105 255,165 315,105" fill="#fecaca" fill-opacity="0.6" stroke="#dc2626" stroke-width="2"/>
  <text x="48" y="40" font-size="11" font-weight="bold" fill="#15803d" text-anchor="end">+{f_pos}</text>
  <text x="48" y="168" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="end">-{f_neg}</text>
  <text x="195" y="122" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{x1}</text>
  <text x="315" y="122" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{x2}</text>
  <text x="335" y="100" font-size="11" font-weight="bold" fill="#334155">x (m)</text>
  <text x="30" y="25" font-size="11" font-weight="bold" fill="#334155">F (N)</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing the Force vs Position graph for a particle moving along the $x$-axis "
        f"from $x = 0\\text{{ m}}$ to $x = {x2}\\text{{ m}}$ (peaking at $+{f_pos}\\text{{ N}}$ between $0$ and ${x1}\\text{{ m}}$, "
        f"and reaching $-{f_neg}\\text{{ N}}$ between ${x1}\\text{{ m}}$ and ${x2}\\text{{ m}}$).\n\n"
        f"1. Calculate the positive work done from $x = 0\\text{{ m}}$ to $x = {x1}\\text{{ m}}$ and the negative work done from $x = {x1}\\text{{ m}}$ to $x = {x2}\\text{{ m}}$.\n"
        f"2. Calculate the net work done on the particle over the entire ${x2}\\text{{ m}}$ displacement."
    )

    ans_latex = (
        rf"1.\; W_{{0\to {x1}}} = +\frac{{1}}{{2}}({x1})({f_pos}) = +{_fmt_sa(w_pos)}\text{{ J}}, \quad "
        rf"W_{{{x1}\to {x2}}} = -\frac{{1}}{{2}}({x2 - x1})({f_neg}) = {_fmt_sa(w_neg)}\text{{ J}}\n"
        rf"2.\; W_{{\text{{net}}}} = {_fmt_sa(w_pos)} + ({_fmt_sa(w_neg)}) = {_fmt_sa(w_total)}\text{{ J}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Positive lobe area = +{_fmt_sa(w_pos)} J", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Negative lobe area = {_fmt_sa(w_neg)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Algebraic sum W_net = {_fmt_sa(w_total)} J", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "added_negative_area_as_positive", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Areas above the $x$-axis represent positive work; areas below the $x$-axis represent negative work.",
        "tier_2": f"First triangle: $+\\frac{{1}}{{2}}({x1})({f_pos}) = {_fmt_sa(w_pos)}\\text{{ J}}$. Second triangle: $-\\frac{{1}}{{2}}({x2-x1})({f_neg}) = {_fmt_sa(w_neg)}\\text{{ J}}$.",
        "tier_3": f"Sum: $W_{{\\text{{net}}}} = {_fmt_sa(w_total)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_14_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_14_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "14_work_from_force_displacement_graph_with_negative_lobe",
        "learning_objective_id": "ps_wep_14_fx_graph_signed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["added_below_axis_area_as_positive", "forgot_triangle_half_factor"],
        "keywords": ["Force-position graph", "signed area", "negative lobe"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 15: Kinetic energy and change in kinetic energy
def _b15_kinetic_energy_and_change_in_kinetic_energy(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([2.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0])
    vi = r.choice([2.0, 3.0, 4.0, 5.0, 6.0])
    vf = r.choice([8.0, 10.0, 12.0, 14.0, 15.0])

    eki = 0.5 * mass_kg * (vi ** 2)
    ekf = 0.5 * mass_kg * (vf ** 2)
    dek = ekf - eki

    prompt = (
        f"A dynamics cart of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ accelerates from an initial speed of "
        f"$v_i = {_fmt_sa(vi)}\\text{{ m/s}}$ to a final speed of $v_f = {_fmt_sa(vf)}\\text{{ m/s}}$.\n\n"
        f"1. Calculate the initial kinetic energy $E_{{k,i}}$ and the final kinetic energy $E_{{k,f}}$ of the cart.\n"
        f"2. Calculate the change in kinetic energy $\\Delta E_k$, and state the net work $W_{{\\text{{net}}}}$ done on the cart."
    )

    ans_latex = (
        rf"1.\; E_{{k,i}} = \frac{{1}}{{2}}mv_i^2 = \frac{{1}}{{2}}({_fmt_sa(mass_kg)})({_fmt_sa(vi)})^2 = {_fmt_sa(eki, 2)}\text{{ J}}, \quad "
        rf"E_{{k,f}} = \frac{{1}}{{2}}mv_f^2 = \frac{{1}}{{2}}({_fmt_sa(mass_kg)})({_fmt_sa(vf)})^2 = {_fmt_sa(ekf, 2)}\text{{ J}}\n"
        rf"2.\; \Delta E_k = E_{{k,f}} - E_{{k,i}} = {_fmt_sa(dek, 2)}\text{{ J}} = W_{{\text{{net}}}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate Ek,i = {_fmt_sa(eki, 2)} J and Ek,f = {_fmt_sa(ekf, 2)} J", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate Delta Ek = {_fmt_sa(dek, 2)} J and equate to W_net", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "used_vf_minus_vi_all_squared", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Note that $\\Delta E_k = \\frac{1}{2}m(v_f^2 - v_i^2) \\neq \\frac{1}{2}m(v_f - v_i)^2$.",
        "tier_2": f"Compute $E_{{k,i}} = {_fmt_sa(eki, 2)}\\text{{ J}}$ and $E_{{k,f}} = {_fmt_sa(ekf, 2)}\\text{{ J}}$.",
        "tier_3": f"$\\Delta E_k = W_{{\\text{{net}}}} = {_fmt_sa(dek, 2)}\\text{{ J}}$.",
    }

    return {
        "id": f"ps_wep_15_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_15_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "15_kinetic_energy_and_change_in_kinetic_energy",
        "learning_objective_id": "ps_wep_15_delta_ek",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["squared_velocity_difference_instead_of_difference_of_squares", "forgot_half_factor"],
        "keywords": ["kinetic energy", "change in kinetic energy", "Work-Energy Theorem"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 16: Work-Energy Theorem horizontal acceleration from rest
def _b16_work_energy_theorem_horizontal_acceleration_from_rest(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([4.0, 5.0, 6.0, 8.0, 10.0])
    fa = r.choice([30, 40, 50, 60, 80])
    fk = r.choice([6, 8, 10, 12, 15])
    dx = r.choice([4.0, 5.0, 6.0, 8.0, 10.0])

    w_net = (fa - fk) * dx
    vf = math.sqrt((2.0 * w_net) / mass_kg)

    prompt = (
        f"A box of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is initially at rest ($v_i = 0\\text{{ m/s}}$) on a rough horizontal floor. "
        f"A horizontal force of $F = {fa}\\text{{ N}}$ pulls the box over a distance of $\\Delta x = {_fmt_sa(dx)}\\text{{ m}}$ against a "
        f"constant frictional force of $f_k = {fk}\\text{{ N}}$.\n\n"
        f"1. State the **Work-Energy Theorem** in words.\n"
        f"2. Use the Work-Energy Theorem to calculate the final speed $v_f$ of the box after moving ${_fmt_sa(dx)}\\text{{ m}}$."
    )

    ans_latex = (
        rf"1.\; \text{{The net work done on an object is equal to the change in the object's kinetic energy (}}W_{{\text{{net}}}} = \Delta E_k\text{{).}}\n"
        rf"2.\; W_{{\text{{net}}}} = ({fa} - {fk})({_fmt_sa(dx)}) = {_fmt_sa(w_net)}\text{{ J}} = \frac{{1}}{{2}}mv_f^2 - 0 \implies "
        rf"v_f = \sqrt{{\frac{{2({_fmt_sa(w_net)})}}{{{_fmt_sa(mass_kg)}}}}} = {_fmt_sa(vf, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Statement of Work-Energy Theorem", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate W_net = {_fmt_sa(w_net)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Equate to 1/2 m vf^2 and solve for vf = {_fmt_sa(vf, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "forgot_square_root", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Work-Energy Theorem: $W_{\\text{net}} = \\Delta E_k = \\frac{1}{2}mv_f^2 - \\frac{1}{2}mv_i^2$.",
        "tier_2": f"Here $W_{{\\text{{net}}}} = ({fa} - {fk}) \\times {_fmt_sa(dx)} = {_fmt_sa(w_net)}\\text{{ J}}$ and $v_i = 0$.",
        "tier_3": f"$v_f = \\sqrt{{2 \\times {_fmt_sa(w_net)} / {_fmt_sa(mass_kg)}}} = {_fmt_sa(vf, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_16_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_16_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "16_work_energy_theorem_horizontal_acceleration_from_rest",
        "learning_objective_id": "ps_wep_16_wet_from_rest",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["forgot_to_take_square_root_for_vf", "omitted_friction_work"],
        "keywords": ["Work-Energy Theorem", "final speed", "horizontal motion"],
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 17: Work-Energy Theorem horizontal motion with non-zero initial velocity
def _b17_work_energy_theorem_horizontal_with_initial_velocity(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([5.0, 6.0, 8.0, 10.0, 12.0])
    vi = r.choice([2.0, 3.0, 4.0, 5.0])
    fa = r.choice([60, 80, 100, 120])
    theta = r.choice([20, 25, 30, 35])
    fk = r.choice([10, 15, 20, 25])
    dx = r.choice([5.0, 6.0, 8.0, 10.0])

    w_a = fa * dx * math.cos(math.radians(theta))
    w_f = -fk * dx
    w_net = w_a + w_f
    vf_sq = (vi ** 2) + (2.0 * w_net) / mass_kg
    vf = math.sqrt(vf_sq)

    prompt = (
        f"A crate of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is moving at an initial velocity of $v_i = {_fmt_sa(vi)}\\text{{ m/s}}$ "
        f"across a horizontal floor when a pulling force of $F_A = {fa}\\text{{ N}}$ at $\\theta = {theta}^\\circ$ above the horizontal "
        f"is applied over a displacement of $\\Delta x = {_fmt_sa(dx)}\\text{{ m}}$. Kinetic friction is $f_k = {fk}\\text{{ N}}$.\n\n"
        f"1. Calculate the net work $W_{{\\text{{net}}}}$ done on the crate over the ${_fmt_sa(dx)}\\text{{ m}}$ displacement.\n"
        f"2. Use the Work-Energy Theorem to calculate the final speed $v_f$ of the crate."
    )

    ans_latex = (
        rf"1.\; W_{{\text{{net}}}} = F_A\Delta x\cos({theta}^\circ) + f_k\Delta x\cos(180^\circ) = {_fmt_sa(w_a, 2)} - {_fmt_sa( abs(w_f), 2)} = {_fmt_sa(w_net, 2)}\text{{ J}}\n"
        rf"2.\; W_{{\text{{net}}}} = \frac{{1}}{{2}}m(v_f^2 - v_i^2) \implies {_fmt_sa(w_net, 2)} = \frac{{1}}{{2}}({_fmt_sa(mass_kg)})(v_f^2 - {_fmt_sa(vi)}^2) \implies v_f = {_fmt_sa(vf, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate W_net = {_fmt_sa(w_net, 2)} J", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Apply W_net = 1/2 m vf^2 - 1/2 m vi^2", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Solve for vf = {_fmt_sa(vf, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_initial_kinetic_energy", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "First compute $W_{\\text{net}} = F_A\\Delta x\\cos\\theta - f_k\\Delta x$.",
        "tier_2": "Do not forget the initial kinetic energy $\\frac{1}{2}mv_i^2$ in $W_{\\text{net}} = \\frac{1}{2}mv_f^2 - \\frac{1}{2}mv_i^2$.",
        "tier_3": f"$W_{{\\text{{net}}}} = {_fmt_sa(w_net, 2)}\\text{{ J}}$, $v_f = {_fmt_sa(vf, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_17_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_17_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "17_work_energy_theorem_horizontal_with_initial_velocity",
        "learning_objective_id": "ps_wep_17_wet_initial_vel",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_initial_kinetic_energy_term", "subtracted_Ekf_from_Eki"],
        "keywords": ["Work-Energy Theorem", "initial velocity", "angled pull"],
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 18: Work-Energy Theorem braking stopping distance
def _b18_work_energy_theorem_braking_stopping_distance(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([900, 1000, 1200, 1400, 1500, 1600])
    vi = r.choice([15.0, 20.0, 22.0, 25.0, 28.0, 30.0])
    f_brake = r.choice([4000, 5000, 6000, 7500, 8000])

    eki = 0.5 * mass_kg * (vi ** 2)
    w_net = -eki
    dx_stop = eki / f_brake

    prompt = (
        f"A car of mass $m = {mass_kg}\\text{{ kg}}$ travelling along a level road at $v_i = {_fmt_sa(vi)}\\text{{ m/s}}$ "
        f"applies its brakes, producing a constant resultant retarding force of $f = {f_brake}\\text{{ N}}$ until it comes to a complete stop ($v_f = 0\\text{{ m/s}}$).\n\n"
        f"1. Determine the net work $W_{{\\text{{net}}}}$ done on the car during braking.\n"
        f"2. Using the Work-Energy Theorem, calculate the stopping distance $\\Delta x$ required to bring the car to rest."
    )

    ans_latex = (
        rf"1.\; W_{{\text{{net}}}} = \Delta E_k = 0 - \frac{{1}}{{2}}({mass_kg})({_fmt_sa(vi)})^2 = {_fmt_sa(w_net)}\text{{ J}}\n"
        rf"2.\; W_{{\text{{net}}}} = f \Delta x \cos(180^\circ) \implies {_fmt_sa(w_net)} = -{f_brake}\Delta x \implies \Delta x = {_fmt_sa(dx_stop, 2)}\text{{ m}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate W_net = Delta Ek = {_fmt_sa(w_net)} J", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Equate to -f * Delta x and solve for Delta x = {_fmt_sa(dx_stop, 2)} m", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Since $v_f = 0$, $W_{\\text{net}} = \\Delta E_k = -\\frac{1}{2}mv_i^2$.",
        "tier_2": "Also $W_{\\text{net}} = -f \\Delta x$, so $\\Delta x = \\frac{\\frac{1}{2}mv_i^2}{f}$.",
        "tier_3": f"$\\Delta x = {_fmt_sa(dx_stop, 2)}\\text{{ m}}$.",
    }

    return {
        "id": f"ps_wep_18_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_18_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "18_work_energy_theorem_braking_stopping_distance",
        "learning_objective_id": "ps_wep_18_stopping_distance",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_velocity_squared_in_stopping_distance", "sign_mismatch_leading_to_negative_distance"],
        "keywords": ["stopping distance", "braking work", "Work-Energy Theorem"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 19: Stopping distance proportionality with initial speed (dx proportional to v^2)
def _b19_work_energy_theorem_stopping_distance_speed_scaling(r: random.Random) -> Dict[str, Any]:
    d_orig = r.choice([12.0, 15.0, 18.0, 20.0, 24.0, 25.0, 30.0])
    v_factor = r.choice([2, 3, 4])
    f_factor = r.choice([1, 2])
    net_factor = (v_factor ** 2) / f_factor
    d_new = d_orig * net_factor

    prompt = (
        f"A vehicle travelling at speed $v$ on a horizontal road requires a minimum braking distance of $d = {_fmt_sa(d_orig)}\\text{{ m}}$ "
        f"to come to rest under a constant braking force $f$.\n\n"
        f"1. Use the Work-Energy Theorem to show that stopping distance $d$ is directly proportional to $v^2$ and inversely proportional to $f$.\n"
        f"2. Calculate the new stopping distance if the initial speed is multiplied by ${v_factor}$ and the braking force is multiplied by ${f_factor}$."
    )

    ans_latex = (
        rf"1.\; -f d = 0 - \frac{{1}}{{2}}mv^2 \implies d = \frac{{mv^2}}{{2f}} \implies d \propto \frac{{v^2}}{{f}}\n"
        rf"2.\; d_{{\text{{new}}}} = d \times \frac{{{v_factor}^2}}{{{f_factor}}} = {_fmt_sa(d_orig)} \times {_fmt_sa(net_factor, 2)} = {_fmt_sa(d_new, 2)}\text{{ m}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Derive d = m*v^2 / (2f) from Work-Energy Theorem", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Apply factor {v_factor}^2 / {f_factor} to obtain d_new = {_fmt_sa(d_new, 2)} m", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "scaled_linearly_with_speed", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "From $f d = \\frac{1}{2}mv^2$, stopping distance scales with the **square** of initial speed ($v^2$).",
        "tier_2": f"Multiplying speed by ${v_factor}$ multiplies kinetic energy by ${v_factor}^2 = {v_factor**2}$.",
        "tier_3": f"$d_{{\\text{{new}}}} = {_fmt_sa(d_orig)} \\times ({v_factor**2} / {f_factor}) = {_fmt_sa(d_new, 2)}\\text{{ m}}$.",
    }

    return {
        "id": f"ps_wep_19_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_19_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "19_work_energy_theorem_stopping_distance_speed_scaling",
        "learning_objective_id": "ps_wep_19_stopping_scaling",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["linear_speed_scaling_for_stopping_distance", "inverted_force_proportionality"],
        "keywords": ["stopping distance scaling", "road safety", "kinetic energy quadratic"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 20: Bullet penetration through a wooden target block
def _b20_work_energy_theorem_bullet_penetration_target(r: random.Random) -> Dict[str, Any]:
    mass_g = r.choice([10.0, 12.0, 15.0, 20.0, 25.0, 30.0])
    mass_kg = mass_g / 1000.0
    vi = r.choice([300, 350, 400, 450, 500])
    vf = r.choice([100, 120, 150, 200])
    thick_cm = r.choice([4.0, 5.0, 6.0, 8.0, 10.0])
    thick_m = thick_cm / 100.0

    dek = 0.5 * mass_kg * (vf**2 - vi**2)
    f_avg = abs(dek) / thick_m

    prompt = (
        f"A bullet of mass $m = {_fmt_sa(mass_g)}\\text{{ g}}$ strikes a stationary wooden block horizontally at speed "
        f"$v_i = {vi}\\text{{ m/s}}$, passes straight through the block of thickness $d = {_fmt_sa(thick_cm)}\\text{{ cm}}$, "
        f"and emerges on the other side with speed $v_f = {vf}\\text{{ m/s}}$.\n\n"
        f"1. Calculate the change in kinetic energy $\\Delta E_k$ of the bullet while passing through the wood.\n"
        f"2. Using the Work-Energy Theorem, calculate the magnitude of the average resistive force $f$ exerted by the wood on the bullet."
    )

    ans_latex = (
        rf"1.\; \Delta E_k = \frac{{1}}{{2}}m(v_f^2 - v_i^2) = \frac{{1}}{{2}}({_fmt_sa(mass_kg, 4)})({vf}^2 - {vi}^2) = {_fmt_sa(dek, 2)}\text{{ J}}\n"
        rf"2.\; W_{{\text{{net}}}} = -f d = \Delta E_k \implies f = \frac{{|\Delta E_k|}}{{d}} = \frac{{{_fmt_sa(abs(dek), 2)}}}{{{_fmt_sa(thick_m, 3)}}} = {_fmt_sa(f_avg, 1)}\text{{ N}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Convert mass from g to kg and thickness from cm to m", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate Delta Ek = {_fmt_sa(dek, 2)} J", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Calculate average resistive force f = {_fmt_sa(f_avg, 1)} N", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "forgot_g_to_kg_or_cm_to_m", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Convert mass to $\\text{kg}$ ($m / 1000$) and thickness to $\\text{m}$ ($d / 100$).",
        "tier_2": "Apply $W_{\\text{net}} = -f d = \\frac{1}{2}m(v_f^2 - v_i^2)$.",
        "tier_3": f"$\\Delta E_k = {_fmt_sa(dek, 2)}\\text{{ J}}$, $f = {_fmt_sa(f_avg, 1)}\\text{{ N}}$.",
    }

    return {
        "id": f"ps_wep_20_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_20_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "20_work_energy_theorem_bullet_penetration_target",
        "learning_objective_id": "ps_wep_20_bullet_penetration",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_grams_to_kg_conversion", "omitted_cm_to_m_conversion"],
        "keywords": ["bullet penetration", "resistive force", "Work-Energy Theorem"],
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 21: Work-Energy Theorem sliding down a frictionless incline
def _b21_work_energy_theorem_sliding_down_frictionless_incline(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([2.0, 4.0, 5.0, 8.0, 10.0, 12.0])
    dx_m = r.choice([4.0, 5.0, 6.0, 8.0, 10.0])
    alpha_deg = r.choice([20, 25, 30, 35, 40])

    w_g = mass_kg * G_ACCEL * dx_m * math.sin(math.radians(alpha_deg))
    vf = math.sqrt((2.0 * w_g) / mass_kg)

    prompt = (
        f"A block of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is released from rest at the top of a **frictionless** ramp "
        f"of length $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ inclined at $\\alpha = {alpha_deg}^\\circ$ to the horizontal ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. State which force(s) do non-zero work on the block as it slides down the frictionless ramp, and calculate the net work $W_{{\\text{{net}}}}$.\n"
        f"2. Calculate the speed $v_f$ of the block at the bottom of the ramp."
    )

    ans_latex = (
        rf"1.\; \text{{Only gravity does work (}}W_N = 0\text{{): }} W_{{\text{{net}}}} = W_g = mg\Delta x\sin({alpha_deg}^\circ) = {_fmt_sa(w_g, 2)}\text{{ J}}\n"
        rf"2.\; W_{{\text{{net}}}} = \frac{{1}}{{2}}mv_f^2 \implies v_f = \sqrt{{2g\Delta x\sin({alpha_deg}^\circ)}} = {_fmt_sa(vf, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Identify only gravity does work and calculate W_net = {_fmt_sa(w_g, 2)} J", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate final speed vf = {_fmt_sa(vf, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "The normal force is perpendicular to the incline ($W_N = 0$), so $W_{\\text{net}} = W_g = mg\\Delta x\\sin\\alpha$.",
        "tier_2": "Equate $W_{\\text{net}} = \\frac{1}{2}mv_f^2$.",
        "tier_3": f"$W_{{\\text{{net}}}} = {_fmt_sa(w_g, 2)}\\text{{ J}}$, $v_f = {_fmt_sa(vf, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_21_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_21_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "21_work_energy_theorem_sliding_down_frictionless_incline",
        "learning_objective_id": "ps_wep_21_wet_smooth_incline",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["included_normal_force_in_work_down_ramp", "used_cos_alpha_instead_of_sin_alpha"],
        "keywords": ["frictionless incline", "Work-Energy Theorem", "speed at bottom"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 22: Work-Energy Theorem sliding down a rough incline
def _b22_work_energy_theorem_sliding_down_rough_incline(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([5.0, 6.0, 8.0, 10.0, 12.0])
    dx_m = r.choice([5.0, 6.0, 8.0, 10.0])
    alpha_deg = r.choice([25, 30, 35, 40])
    fk_n = r.choice([5.0, 8.0, 10.0, 12.0, 15.0])

    w_g = mass_kg * G_ACCEL * dx_m * math.sin(math.radians(alpha_deg))
    w_f = -fk_n * dx_m
    w_net = w_g + w_f
    vf = math.sqrt((2.0 * w_net) / mass_kg)

    svg = _clean_svg(f"""
<svg viewBox="0 0 380 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="180" fill="#f8fafc" rx="8"/>
  <polygon points="50,150 330,150 50,45" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
  <rect x="110" y="58" width="46" height="28" rx="3" transform="rotate(20.5 133 72)" fill="#fbbf24" stroke="#b45309" stroke-width="2"/>
  <text x="275" y="142" font-size="11" font-weight="bold" fill="#0f172a">α = {alpha_deg}°</text>
  <text x="215" y="70" font-size="11" font-weight="bold" fill="#1e293b">m = {_fmt_sa(mass_kg)} kg, fk = {_fmt_sa(fk_n)} N</text>
  <text x="215" y="88" font-size="11" fill="#334155">Rough ramp: Δx = {_fmt_sa(dx_m)} m</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing a crate of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ released from rest "
        f"at the top of a rough incline of angle $\\alpha = {alpha_deg}^\\circ$ and length $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$. "
        f"A constant kinetic frictional force of $f_k = {_fmt_sa(fk_n)}\\text{{ N}}$ acts on the crate ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the work done by gravity $W_g$ and the work done by kinetic friction $W_f$.\n"
        f"2. Use the Work-Energy Theorem to calculate the speed $v_f$ of the crate at the bottom of the incline."
    )

    ans_latex = (
        rf"1.\; W_g = +mg\Delta x\sin({alpha_deg}^\circ) = +{_fmt_sa(w_g, 2)}\text{{ J}}, \quad W_f = -f_k\Delta x = {_fmt_sa(w_f, 2)}\text{{ J}}\n"
        rf"2.\; W_{{\text{{net}}}} = W_g + W_f = {_fmt_sa(w_net, 2)}\text{{ J}} = \frac{{1}}{{2}}mv_f^2 \implies v_f = {_fmt_sa(vf, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate W_g = +{_fmt_sa(w_g, 2)} J", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate W_f = {_fmt_sa(w_f, 2)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate W_net = {_fmt_sa(w_net, 2)} J", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Solve for vf = {_fmt_sa(vf, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Down the ramp, gravity does positive work ($+mg\\Delta x\\sin\\alpha$) while friction does negative work ($-f_k\\Delta x$).",
        "tier_2": f"Find $W_{{\\text{{net}}}} = {_fmt_sa(w_g, 2)} - {_fmt_sa(abs(w_f), 2)} = {_fmt_sa(w_net, 2)}\\text{{ J}}$.",
        "tier_3": f"$v_f = \\sqrt{{2 \\times {_fmt_sa(w_net, 2)} / {_fmt_sa(mass_kg)}}} = {_fmt_sa(vf, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_22_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_22_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "22_work_energy_theorem_sliding_down_rough_incline",
        "learning_objective_id": "ps_wep_22_wet_rough_down",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["added_friction_work_as_positive", "omitted_sin_alpha_in_gravity_work"],
        "keywords": ["rough incline", "Work-Energy Theorem", "sliding down"],
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 23: Work-Energy Theorem pulled up a rough incline
def _b23_work_energy_theorem_pulled_up_rough_incline(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([4.0, 5.0, 6.0, 8.0, 10.0])
    alpha_deg = r.choice([20, 25, 30])
    dx_m = r.choice([4.0, 5.0, 6.0, 8.0])
    fk_n = r.choice([8.0, 10.0, 12.0, 15.0])
    fg_par = mass_kg * G_ACCEL * math.sin(math.radians(alpha_deg))
    f_app = round(fg_par + fk_n + r.choice([20.0, 30.0, 40.0, 50.0]), 1)

    w_app = f_app * dx_m
    w_g = -fg_par * dx_m
    w_f = -fk_n * dx_m
    w_net = w_app + w_g + w_f
    vf = math.sqrt((2.0 * w_net) / mass_kg)

    prompt = (
        f"A crate of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ is pulled from rest a distance of $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ "
        f"**up** a rough incline angled at $\\alpha = {alpha_deg}^\\circ$ to the horizontal by a force $F_A = {_fmt_sa(f_app)}\\text{{ N}}$ "
        f"parallel to the incline. The kinetic frictional force is $f_k = {_fmt_sa(fk_n)}\\text{{ N}}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the work done by the applied force ($W_A$), by gravity ($W_g$), and by friction ($W_f$).\n"
        f"2. Calculate the net work $W_{{\\text{{net}}}}$ and the speed $v_f$ of the crate after moving $\\Delta x = {_fmt_sa(dx_m)}\\text{{ m}}$ up the ramp."
    )

    ans_latex = (
        rf"1.\; W_A = +{_fmt_sa(w_app, 2)}\text{{ J}}, \quad W_g = -mg\Delta x\sin({alpha_deg}^\circ) = {_fmt_sa(w_g, 2)}\text{{ J}}, \quad W_f = -f_k\Delta x = {_fmt_sa(w_f, 2)}\text{{ J}}\n"
        rf"2.\; W_{{\text{{net}}}} = W_A + W_g + W_f = {_fmt_sa(w_net, 2)}\text{{ J}} = \frac{{1}}{{2}}mv_f^2 \implies v_f = {_fmt_sa(vf, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate W_A = +{_fmt_sa(w_app, 2)} J", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate W_g = {_fmt_sa(w_g, 2)} J (negative)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate W_f = {_fmt_sa(w_f, 2)} J (negative)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculate W_net = {_fmt_sa(w_net, 2)} J", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Calculate vf = {_fmt_sa(vf, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "positive_work_for_gravity_uphill", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "When moving **up** the incline, both $F_{g\\parallel}$ and $f_k$ point down the incline ($180^\\circ$), so both $W_g$ and $W_f$ are negative.",
        "tier_2": f"$W_{{\\text{{net}}}} = {_fmt_sa(w_app, 2)} + ({_fmt_sa(w_g, 2)}) + ({_fmt_sa(w_f, 2)}) = {_fmt_sa(w_net, 2)}\\text{{ J}}$.",
        "tier_3": f"$v_f = {_fmt_sa(vf, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_23_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_23_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "23_work_energy_theorem_pulled_up_rough_incline",
        "learning_objective_id": "ps_wep_23_wet_rough_up",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["positive_gravity_work_going_up_incline", "omitted_friction_work"],
        "keywords": ["pulled up incline", "Work-Energy Theorem", "negative work by gravity"],
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 24: Work-Energy Theorem for a vertical hoist / crane cable
def _b24_work_energy_theorem_vertical_hoist_winch(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([50, 80, 100, 120, 150, 200])
    h_m = r.choice([4.0, 5.0, 6.0, 8.0, 10.0])
    fg = mass_kg * G_ACCEL
    tension = round(fg + r.choice([100, 150, 200, 250, 300]), 1)

    w_t = tension * h_m
    w_g = -fg * h_m
    w_net = w_t + w_g
    vf = math.sqrt((2.0 * w_net) / mass_kg)

    prompt = (
        f"A construction winch lifts a concrete block of mass $m = {mass_kg}\\text{{ kg}}$ vertically upwards from rest "
        f"through a height of $\\Delta y = {_fmt_sa(h_m)}\\text{{ m}}$ by exerting a constant upward cable tension of "
        f"$T = {_fmt_sa(tension)}\\text{{ N}}$ ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Calculate the work done by the cable tension $W_T$ and the work done by gravity $W_g$.\n"
        f"2. Use the Work-Energy Theorem to calculate the upward speed $v_f$ of the block at height $\\Delta y = {_fmt_sa(h_m)}\\text{{ m}}$."
    )

    ans_latex = (
        rf"1.\; W_T = T\Delta y\cos(0^\circ) = +{_fmt_sa(w_t, 2)}\text{{ J}}, \quad W_g = mg\Delta y\cos(180^\circ) = {_fmt_sa(w_g, 2)}\text{{ J}}\n"
        rf"2.\; W_{{\text{{net}}}} = W_T + W_g = {_fmt_sa(w_net, 2)}\text{{ J}} = \frac{{1}}{{2}}mv_f^2 \implies v_f = {_fmt_sa(vf, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate W_T = +{_fmt_sa(w_t, 2)} J and W_g = {_fmt_sa(w_g, 2)} J", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate W_net = {_fmt_sa(w_net, 2)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate vf = {_fmt_sa(vf, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Upward tension does positive work ($+T\\Delta y$); downward gravity does negative work ($-mg\\Delta y$).",
        "tier_2": f"$W_{{\\text{{net}}}} = {_fmt_sa(w_t, 2)} - {_fmt_sa(abs(w_g), 2)} = {_fmt_sa(w_net, 2)}\\text{{ J}}$.",
        "tier_3": f"$v_f = \\sqrt{{2 \\times {_fmt_sa(w_net, 2)} / {mass_kg}}} = {_fmt_sa(vf, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_24_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_24_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "24_work_energy_theorem_vertical_hoist_winch",
        "learning_objective_id": "ps_wep_24_vertical_hoist",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["equated_tension_to_mg_during_acceleration", "omitted_gravity_work_in_vertical_lift"],
        "keywords": ["vertical hoist", "cable tension", "Work-Energy Theorem"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 25: Pendulum swing work and speed at lowest point
def _b25_work_energy_theorem_pendulum_swing_speed(r: random.Random) -> Dict[str, Any]:
    mass_kg = r.choice([0.5, 0.8, 1.2, 1.5, 2.0, 2.5, 3.0])
    h_drop = r.choice([0.20, 0.35, 0.45, 0.60, 0.80, 1.00, 1.25])
    w_g = mass_kg * G_ACCEL * h_drop
    vf = math.sqrt(2.0 * G_ACCEL * h_drop)

    prompt = (
        f"A simple pendulum consists of a bob of mass $m = {_fmt_sa(mass_kg)}\\text{{ kg}}$ attached to a light inextensible string. "
        f"The bob is pulled aside to a vertical height of $h = {_fmt_sa(h_drop, 2)}\\text{{ m}}$ above its lowest equilibrium position and released from rest "
        f"(ignore air resistance; $g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
        f"1. Explain why the tension force $\\vec{{T}}$ in the string does **zero work** on the pendulum bob throughout its swing.\n"
        f"2. Calculate the work done by gravity $W_g$ and the speed $v_f$ of the bob as it passes through the lowest point."
    )

    ans_latex = (
        rf"1.\; \text{{At every instant along the circular arc, the string tension }}\vec{{T}}\text{{ is perpendicular to the tangential velocity/displacement (}}\theta = 90^\circ\text{{), so }}W_T = 0\text{{ J.}}\n"
        rf"2.\; W_g = mgh = ({_fmt_sa(mass_kg)})(9{{,}}8)({_fmt_sa(h_drop, 2)}) = {_fmt_sa(w_g, 2)}\text{{ J}}, \quad v_f = \sqrt{{2gh}} = {_fmt_sa(vf, 2)}\text{{ m/s}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Tension acts perpendicular (90 deg) to arc motion at every point, so W_T = 0 J", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate W_g = mgh = {_fmt_sa(w_g, 2)} J", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate vf = sqrt(2gh) = {_fmt_sa(vf, 2)} m/s", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Along a circular arc, the radial string tension is always at $90^\\circ$ to the tangential motion, doing $0\\text{ J}$ of work.",
        "tier_2": "Only gravity does work: $W_{\\text{net}} = W_g = mgh = \\frac{1}{2}mv_f^2$.",
        "tier_3": f"$W_g = {_fmt_sa(w_g, 2)}\\text{{ J}}$, $v_f = {_fmt_sa(vf, 2)}\\text{{ m/s}}$.",
    }

    return {
        "id": f"ps_wep_25_{r.randint(100000, 999999)}",
        "question_id": f"ps_wep_25_{r.randint(100000, 999999)}",
        "topic": "Work energy and power",
        "subskill": "25_work_energy_theorem_pendulum_swing_speed",
        "learning_objective_id": "ps_wep_25_pendulum_swing",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_string_tension_does_work_on_pendulum", "omitted_square_root_in_2gh"],
        "keywords": ["pendulum", "zero work by tension", "Work-Energy Theorem"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_work_done_constant_horizontal_force": _b01_work_done_constant_horizontal_force,
    "02_work_done_force_at_angle_above_horizontal": _b02_work_done_force_at_angle_above_horizontal,
    "03_work_done_pushing_force_at_angle_below_horizontal": _b03_work_done_pushing_force_at_angle_below_horizontal,
    "04_zero_work_done_by_perpendicular_forces": _b04_zero_work_done_by_perpendicular_forces,
    "05_negative_work_done_by_kinetic_friction": _b05_negative_work_done_by_kinetic_friction,
    "06_work_done_by_gravity_vertical_free_fall": _b06_work_done_by_gravity_vertical_free_fall,
    "07_work_done_by_gravity_upward_projection": _b07_work_done_by_gravity_upward_projection,
    "08_work_done_by_gravity_down_inclined_plane": _b08_work_done_by_gravity_down_inclined_plane,
    "09_work_done_by_gravity_up_inclined_plane": _b09_work_done_by_gravity_up_inclined_plane,
    "10_total_work_from_sum_of_individual_works": _b10_total_work_from_sum_of_individual_works,
    "11_total_work_from_resultant_force_method": _b11_total_work_from_resultant_force_method,
    "12_total_work_zero_at_constant_velocity": _b12_total_work_zero_at_constant_velocity,
    "13_work_from_force_displacement_graph_rectangle_triangle": _b13_work_from_force_displacement_graph_rectangle_triangle,
    "14_work_from_force_displacement_graph_with_negative_lobe": _b14_work_from_force_displacement_graph_with_negative_lobe,
    "15_kinetic_energy_and_change_in_kinetic_energy": _b15_kinetic_energy_and_change_in_kinetic_energy,
    "16_work_energy_theorem_horizontal_acceleration_from_rest": _b16_work_energy_theorem_horizontal_acceleration_from_rest,
    "17_work_energy_theorem_horizontal_with_initial_velocity": _b17_work_energy_theorem_horizontal_with_initial_velocity,
    "18_work_energy_theorem_braking_stopping_distance": _b18_work_energy_theorem_braking_stopping_distance,
    "19_work_energy_theorem_stopping_distance_speed_scaling": _b19_work_energy_theorem_stopping_distance_speed_scaling,
    "20_work_energy_theorem_bullet_penetration_target": _b20_work_energy_theorem_bullet_penetration_target,
    "21_work_energy_theorem_sliding_down_frictionless_incline": _b21_work_energy_theorem_sliding_down_frictionless_incline,
    "22_work_energy_theorem_sliding_down_rough_incline": _b22_work_energy_theorem_sliding_down_rough_incline,
    "23_work_energy_theorem_pulled_up_rough_incline": _b23_work_energy_theorem_pulled_up_rough_incline,
    "24_work_energy_theorem_vertical_hoist_winch": _b24_work_energy_theorem_vertical_hoist_winch,
    "25_work_energy_theorem_pendulum_swing_speed": _b25_work_energy_theorem_pendulum_swing_speed,
}
