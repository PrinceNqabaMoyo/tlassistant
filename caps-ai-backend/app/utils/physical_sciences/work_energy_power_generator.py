"""Work, Energy, and Power Generator (Grades 10 & 12 Physical Sciences).

Complies with the 6-pillar South African CAPS contract:
- Term & calendar metadata
- Deconstructible compound and elementary sub-drills
- Standardized misconception taxonomy
- Teacher-editable marking schema with [M] and [A] marks
- Deterministic 3-tier pre-baked hints
- South African comma decimal convention
"""

import math
import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float, decimals: int = 2) -> str:
    """Formats a float using South African comma decimal convention."""
    if abs(val - round(val)) < 1e-6:
        return str(int(round(val)))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    return f"{prefix}_{seed or 'rnd'}_{idx}"


def _generate_gr10_mechanical_energy(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 10: Mechanical energy conservation (Ep + Ek)."""
    mass = r.choice([2, 5, 10, 15, 20])
    height = r.choice([5, 8, 10, 12, 15, 20])
    g = 9.8

    # Ep = m * g * h
    ep_top = mass * g * height
    # At ground, Ek = Ep_top -> 0.5 * m * v^2 = Ep_top -> v = sqrt(2 * g * h)
    v_bottom = math.sqrt(2 * g * height)

    qid = _make_id("ps10_work_mech", seed, idx)

    if mode == "elementary_kinetic_energy":
        v_test = r.choice([4, 6, 8, 10, 12])
        ek = 0.5 * mass * (v_test ** 2)
        prompt = (
            f"An object of mass ${_fmt_sa(mass)}\\text{{ kg}}$ travels across a smooth horizontal surface at a speed of ${_fmt_sa(v_test)}\\text{{ m/s}}$.\n\n"
            f"Calculate the kinetic energy ($E_k$) of the object."
        )
        ans_str = f"Ek = {_fmt_sa(ek)} J"
        memo = (
            f"Kinetic energy formula [2]:\n"
            f"$$E_k = \\frac{{1}}{{2}} m v^2 = \\frac{{1}}{{2}}({_fmt_sa(mass)})({_fmt_sa(v_test)})^2 = {_fmt_sa(ek)}\\text{{ J}}$$ [M+A]"
        )
        hints = {
            "tier_1": "Recall the formula for kinetic energy: Ek = 0.5 * m * v^2.",
            "tier_2": f"Substitute m = {mass} kg and v = {v_test} m/s into Ek = 0.5 * m * v^2.",
            "tier_3": f"Ek = 0.5 * {mass} * {v_test}^2 = {ek} J.",
        }
        marks = 2
    else:
        # Compound
        prompt = (
            f"A roller-coaster cart with a mass of ${_fmt_sa(mass)}\\text{{ kg}}$ is released from rest at point A, "
            f"which is at a vertical height of ${_fmt_sa(height)}\\text{{ m}}$ above the ground. "
            f"Assume that friction and air resistance are negligible ($g = 9{{,}}8\\text{{ m/s}}^2$).\n\n"
            f"1. State the principle of conservation of mechanical energy in words.\n"
            f"2. Calculate the gravitational potential energy ($E_p$) of the cart at point A.\n"
            f"3. Using energy principles, determine the speed of the cart as it reaches the ground (point B)."
        )
        ans_str = (
            f"1. Total mechanical energy in an isolated system remains constant; "
            f"2. Ep = {_fmt_sa(ep_top)} J; "
            f"3. v = {_fmt_sa(v_bottom, 2)} m/s"
        )
        memo = (
            f"1. Principle of conservation of mechanical energy [2]: "
            f"The total mechanical energy in an isolated/closed system remains constant (or is conserved). [2]\n"
            f"2. Gravitational potential energy [2]:\n"
            f"   $$E_p = mgh = ({_fmt_sa(mass)})(9{{,}}8)({_fmt_sa(height)}) = {_fmt_sa(ep_top)}\\text{{ J}}$$ [M+A]\n"
            f"3. Speed at ground [3]:\n"
            f"   $$(E_p + E_k)_A = (E_p + E_k)_B$$\n"
            f"   $${_fmt_sa(ep_top)} + 0 = 0 + \\frac{{1}}{{2}}({_fmt_sa(mass)})v^2$$\n"
            f"   $$v^2 = \\frac{{2 \\times {_fmt_sa(ep_top)}}}{{{_fmt_sa(mass)}}} = {_fmt_sa(2 * g * height)}$$\n"
            f"   $$v = \\sqrt{{{_fmt_sa(2 * g * height)}}} = {_fmt_sa(v_bottom, 2)}\\text{{ m/s}}$$ [M+A]"
        )
        hints = {
            "tier_1": "At the top, Ep = mgh and Ek = 0. At the bottom, all potential energy is converted to kinetic energy (Ek = 0.5 * m * v^2).",
            "tier_2": f"Find Ep = {mass} * 9.8 * {height}. Set 0.5 * {mass} * v^2 equal to this Ep to solve for v.",
            "tier_3": f"Ep = {ep_top} J. v = sqrt(2 * 9.8 * {height}) = {v_bottom:.2f} m/s.",
        }
        marks = 7

    return {
        "id": qid,
        "question_id": qid,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["kinetic_energy_velocity_not_squared", "confused_potential_and_kinetic_energy", "forgot_isolated_system_condition"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of conservation of mechanical energy", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Gravitational potential energy calculation", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Mechanical energy conservation equation and final speed", "marks": 3, "editable": True},
            ],
            "deductions": [{"rule": "missing_or_incorrect_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr12_work_energy_theorem(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 12: Work-energy theorem and non-conservative work."""
    mass = r.choice([4, 6, 8, 10, 12])
    dist = r.choice([5, 8, 10, 15, 20])
    applied_force = r.choice([40, 50, 60, 80, 100])
    angle_deg = r.choice([0, 20, 30])
    friction_force = r.choice([10, 15, 20, 25])
    vi = r.choice([0, 2, 4])

    rad = math.radians(angle_deg)
    w_applied = applied_force * dist * math.cos(rad)
    w_friction = -friction_force * dist  # cos(180) = -1
    w_net = w_applied + w_friction

    # W_net = Delta Ek = 0.5 * m * (vf^2 - vi^2)
    # vf^2 = vi^2 + 2 * W_net / m
    vf_sq = (vi ** 2) + (2 * w_net / mass)
    if vf_sq < 0:
        vf_sq = 16.0
    vf = math.sqrt(vf_sq)

    qid = _make_id("ps12_work_theorem", seed, idx)

    if mode == "elementary_work_cos_theta":
        prompt = (
            f"A force of ${_fmt_sa(applied_force)}\\text{{ N}}$ is applied to a crate, pulling it across a horizontal floor for a distance of ${_fmt_sa(dist)}\\text{{ m}}$. "
            f"The force is applied at an angle of ${angle_deg}^\\circ$ to the horizontal.\n\n"
            f"Calculate the work done by the applied force on the crate."
        )
        ans_str = f"W = {_fmt_sa(w_applied, 2)} J"
        memo = (
            f"Work formula [3]:\n"
            f"$$W = F \\Delta x \\cos \\theta = ({_fmt_sa(applied_force)})({_fmt_sa(dist)})\\cos({angle_deg}^\\circ) = {_fmt_sa(w_applied, 2)}\\text{{ J}}$$ [M+A]"
        )
        hints = {
            "tier_1": "Use the work formula: W = F * delta_x * cos(theta).",
            "tier_2": f"Substitute F = {applied_force} N, delta_x = {dist} m, theta = {angle_deg} degrees.",
            "tier_3": f"W = {applied_force} * {dist} * cos({angle_deg}) = {w_applied:.2f} J.",
        }
        marks = 3
    elif mode == "elementary_power_watt":
        time_sec = r.choice([5, 8, 10, 12])
        work_val = r.choice([1200, 2400, 3600, 4800])
        p_watt = work_val / time_sec
        prompt = (
            f"An electric crane motor lifts a container, doing ${_fmt_sa(work_val)}\\text{{ J}}$ of work in ${_fmt_sa(time_sec)}\\text{{ s}}$.\n\n"
            f"1. Define the term *power* in physics.\n"
            f"2. Calculate the average power exerted by the crane motor in watts ($\\text{{W}}$)."
        )
        ans_str = f"1. Power is the rate at which work is done (or energy is transferred); 2. P = {_fmt_sa(p_watt, 1)} W"
        memo = (
            f"1. Definition [2]: Power is the rate at which work is done (or rate of energy transfer). [2]\n"
            f"2. Power calculation [2]:\n"
            f"   $$P = \\frac{{W}}{{\\Delta t}} = \\frac{{{_fmt_sa(work_val)}}}{{{_fmt_sa(time_sec)}}} = {_fmt_sa(p_watt, 1)}\\text{{ W}}$$ [M+A]"
        )
        hints = {
            "tier_1": "Power is work divided by elapsed time: P = W / delta_t.",
            "tier_2": f"Divide {work_val} J by {time_sec} s.",
            "tier_3": f"P = {work_val} / {time_sec} = {p_watt:.1f} W.",
        }
        marks = 4
    else:
        # Compound Grade 12 Work-Energy Question
        prompt = (
            f"A crate of mass ${_fmt_sa(mass)}\\text{{ kg}}$ moves horizontally along a rough surface. A constant pulling force of "
            f"${_fmt_sa(applied_force)}\\text{{ N}}$ acts on the crate at an angle of ${angle_deg}^\\circ$ to the horizontal over a displacement of ${_fmt_sa(dist)}\\text{{ m}}$. "
            f"A constant frictional force of ${_fmt_sa(friction_force)}\\text{{ N}}$ opposes the motion. The initial velocity of the crate is ${_fmt_sa(vi)}\\text{{ m/s}}$.\n\n"
            f"1. State the work-energy theorem in words.\n"
            f"2. Draw a labeled free-body diagram of all forces acting on the crate.\n"
            f"3. Calculate the net work done ($W_{{\\text{{net}}}}$) on the crate over the ${_fmt_sa(dist)}\\text{{ m}}$ displacement.\n"
            f"4. Use the work-energy theorem to calculate the final velocity ($v_f$) of the crate."
        )
        ans_str = (
            f"1. The net work done on an object is equal to the change in the object's kinetic energy; "
            f"2. 4 forces: Normal force (up), Gravity (down), Applied force (at angle), Friction (left); "
            f"3. W_net = {_fmt_sa(w_net, 2)} J; "
            f"4. vf = {_fmt_sa(vf, 2)} m/s"
        )
        memo = (
            f"1. Work-energy theorem [2]: The net work done on an object is equal to the change in the object's kinetic energy. [2]\n"
            f"2. Free-body diagram [4]:\n"
            f"   - Normal force $F_N$ acting perpendicular upwards [1]\n"
            f"   - Gravitational force $F_g$ / $w$ acting vertically downwards [1]\n"
            f"   - Applied force $F_A$ directed at ${angle_deg}^\\circ$ above horizontal [1]\n"
            f"   - Kinetic friction $f_k$ directed opposite to motion [1]\n"
            f"3. Net work [4]:\n"
            f"   $$W_{{F_A}} = F_A \\Delta x \\cos({angle_deg}^\\circ) = ({_fmt_sa(applied_force)})({_fmt_sa(dist)})\\cos({angle_deg}^\\circ) = {_fmt_sa(w_applied, 2)}\\text{{ J}}$$ [1]\n"
            f"   $$W_{{f_k}} = f_k \\Delta x \\cos(180^\\circ) = ({_fmt_sa(friction_force)})({_fmt_sa(dist)})(-1) = {_fmt_sa(w_friction, 2)}\\text{{ J}}$$ [1]\n"
            f"   $$W_{{\\text{{net}}}} = W_{{F_A}} + W_{{f_k}} = {_fmt_sa(w_applied, 2)} + ({_fmt_sa(w_friction, 2)}) = {_fmt_sa(w_net, 2)}\\text{{ J}}$$ [2]\n"
            f"4. Final velocity calculation [3]:\n"
            f"   $$W_{{\\text{{net}}}} = \\Delta E_k = \\frac{{1}}{{2}} m v_f^2 - \\frac{{1}}{{2}} m v_i^2$$\n"
            f"   $${_fmt_sa(w_net, 2)} = \\frac{{1}}{{2}}({_fmt_sa(mass)}) v_f^2 - \\frac{{1}}{{2}}({_fmt_sa(mass)})({_fmt_sa(vi)})^2$$\n"
            f"   $${_fmt_sa(w_net, 2)} = {_fmt_sa(0.5 * mass)} v_f^2 - {_fmt_sa(0.5 * mass * (vi**2))}$$\n"
            f"   $$v_f^2 = {_fmt_sa(vf_sq, 2)} \\implies v_f = {_fmt_sa(vf, 2)}\\text{{ m/s}}$$ [M+A]"
        )
        hints = {
            "tier_1": "Calculate work for each force: W = F * delta_x * cos(theta). Sum them to find W_net.",
            "tier_2": "Friction acts at 180 degrees, doing negative work. Normal and gravitational forces do zero work because cos(90) = 0.",
            "tier_3": f"W_net = {w_applied:.2f} + ({w_friction:.2f}) = {w_net:.2f} J. Then solve W_net = 0.5 * m * (vf^2 - vi^2) -> vf = {vf:.2f} m/s.",
        }
        marks = 13

    return {
        "id": qid,
        "question_id": qid,
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 14,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": [
            "work_angle_theta_misidentified",
            "sign_of_friction_work_positive",
            "forgot_work_energy_theorem_definition",
            "normal_force_does_work_error",
        ],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of work-energy theorem", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Free-body diagram vector arrows", "marks": 4, "editable": True},
                {"id": "mp_3", "desc": "Net work calculation with directional signs", "marks": 4, "editable": True},
                {"id": "mp_4", "desc": "Final velocity via work-energy theorem", "marks": 3, "editable": True},
            ],
            "deductions": [{"rule": "sign_error_friction_work", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "concepts",
    difficulty: str = "medium",
    count: int = 1,
    grade: str = "12",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Work, Energy, and Power."""
    r = random.Random(seed)
    questions = []

    for i in range(count):
        gr_str = str(grade).strip()
        if gr_str == "10":
            q = _generate_gr10_mechanical_energy(r, seed, i, mode)
        else:
            q = _generate_gr12_work_energy_theorem(r, seed, i, mode)
        questions.append(q)

    return questions
