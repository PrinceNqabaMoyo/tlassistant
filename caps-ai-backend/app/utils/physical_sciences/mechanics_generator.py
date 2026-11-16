"""Grade 10 Physical Sciences - Mechanics & Vectors and Scalars Generator
100% Deterministic & SymPy-backed. South African National Curriculum Standards aligned.
Aggregates:
- mechanics_archetypes_01_25.py (Subskills 01 to 25: Foundations of vectors & scalars, collinear addition, perpendicular resultant & Pythagoras)
- mechanics_archetypes_26_50.py (Subskills 26 to 50: Component resolution, multi-vector addition, equilibrium, applied navigation, capstone synthesis)

Also preserves legacy mechanics builders (kinematics, Newton's second law, inclined planes) for backwards compatibility.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional

from app.utils.physical_sciences.mechanics_archetypes_01_25 import (
    BUILDERS_01_25,
    SUBSKILLS_01_25,
    _fmt_sa,
    _rng,
)
from app.utils.physical_sciences.mechanics_archetypes_26_50 import (
    BUILDERS_26_50,
    SUBSKILLS_26_50,
)

# Combine 50 semantic subskill builders
ARCHETYPE_BUILDERS: Dict[str, Callable] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = SUBSKILLS_01_25 + SUBSKILLS_26_50
ORDERED_SUBSKILLS: List[str] = SUBSKILLS
BUILDERS: Dict[str, Callable] = ARCHETYPE_BUILDERS
SUBSKILL_BUILDERS: Dict[str, Callable] = ARCHETYPE_BUILDERS
DISPATCH_TABLE: Dict[str, Callable] = ARCHETYPE_BUILDERS


# ============================================================================
# LEGACY MECHANICS BUILDERS (PRESERVED FOR BACKWARDS COMPATIBILITY)
# ============================================================================

def generate_kinematics_question(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    """Generates 1D kinematic motion calculation (v_f = v_i + a*t or delta_x = v_i*t + 0.5*a*t^2)."""
    vehicles = ["car", "minibus taxi", "goods train", "delivery motorcycle", "racing drone"]
    vehicle = r.choice(vehicles)
    
    vi = r.randint(0, 25) # initial velocity in m/s
    a = r.randint(2, 6)   # acceleration in m/s^2
    t = r.randint(3, 12)  # time in seconds
    vf = vi + a * t       # final velocity in m/s
    dx = vi * t + 0.5 * a * (t ** 2) # displacement in m
    
    solve_for_dx = r.random() < 0.5

    if solve_for_dx:
        prompt = (
            f"A {vehicle} accelerates uniformly from {_fmt_sa(vi)} m·s⁻¹ at a constant rate of "
            f"{_fmt_sa(a)} m·s⁻² for {_fmt_sa(t)} seconds. Calculate the total displacement (Δx) traveled by the {vehicle}."
        )
        answer_val = dx
        unit = "m"
        formula_latex = r"\Delta x = v_i \Delta t + \frac{1}{2} a \Delta t^2"
        calc_latex = rf"\Delta x = ({_fmt_sa(vi)})({_fmt_sa(t)}) + \frac{{1}}{{2}}({_fmt_sa(a)})({_fmt_sa(t)})^2 = {_fmt_sa(dx)}\text{{ m}}"
        misconceptions = ["forgot_half_in_kinematics", "forgot_to_square_time", "confused_initial_with_final_velocity"]
    else:
        prompt = (
            f"A {vehicle} starts from an initial speed of {_fmt_sa(vi)} m·s⁻¹ and accelerates at "
            f"{_fmt_sa(a)} m·s⁻² for {_fmt_sa(t)} seconds. Determine its final velocity (v_f)."
        )
        answer_val = vf
        unit = "m·s⁻¹"
        formula_latex = r"v_f = v_i + a \Delta t"
        calc_latex = rf"v_f = {_fmt_sa(vi)} + ({_fmt_sa(a)})({_fmt_sa(t)}) = {_fmt_sa(vf)}\text{{ m·s}}^{{-1}}"
        misconceptions = ["used_wrong_motion_equation", "sign_error_acceleration"]

    return {
        "id": f"phys_kinematics_{r.randint(100000, 999999)}",
        "topic": "Physical Sciences Mechanics",
        "subskill": "kinematics_1d",
        "term": 1,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 6,
        "prompt": prompt,
        "formula_latex": formula_latex,
        "ideal_answer": f"{_fmt_sa(answer_val)} {unit}",
        "sample_answer": f"{calc_latex}",
        "marks": 4,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_formula", "desc": f"Correct kinematic formula: {formula_latex}", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": "Correct substitution of given values", "marks": 2, "editable": True},
                {"id": "mp_ans", "desc": f"Final answer with correct SI unit: {_fmt_sa(answer_val)} {unit}", "marks": 1, "editable": True}
            ],
            "deductions": [{"rule": "omitted_or_wrong_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "1_nudge": f"Identify your known variables: v_i = {vi} m·s⁻¹, a = {a} m·s⁻², Δt = {t} s.",
            "2_concept": f"Select the standard kinematic formula linking your knowns to the unknown: {formula_latex}.",
            "3_breakdown": f"Substitute values into the equation: {calc_latex}."
        }
    }


def generate_newton_law_question(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    """Generates Newton's 2nd Law problem: F_net = m * a with frictional resistance."""
    mass = r.randint(5, 80) * 10 # 50 kg to 800 kg
    f_applied = r.randint(20, 100) * 50 # applied force in N
    friction = r.randint(5, 25) * 20 # frictional force in N
    f_net = f_applied - friction
    acc = round(f_net / mass, 2)

    prompt = (
        f"A crate of mass {mass} kg is pulled across a rough horizontal concrete floor by an applied force of "
        f"{f_applied} N. A constant frictional force of {friction} N opposes the motion. "
        f"Calculate the acceleration of the crate."
    )

    calc_latex = (
        rf"F_{{\text{{net}}}} = F_{{\text{{applied}}}} - f_{{\text{{friction}}}} = {f_applied} - {friction} = {f_net}\text{{ N}}\\"
        rf"F_{{\text{{net}}}} = m a \implies a = \frac{{{f_net}}}{{{mass}}} = {_fmt_sa(acc)}\text{{ m·s}}^{{-2}}"
    )

    return {
        "id": f"phys_newton_{r.randint(100000, 999999)}",
        "topic": "Physical Sciences Mechanics",
        "subskill": "newtons_second_law",
        "modality": "free_body_diagram",
        "diagram_spec": {
            "diagram_role": "context",
            "kind": "free_body_diagram",
            "mass_kg": mass,
            "angle_deg": 0,
        },
        "fbd_spec": {
            "mass_kg": mass,
            "angle_deg": 0,
            "forces": [
                {"name": "F_N", "label": "Normal Force (FN)", "magnitude": round(mass * 9.8), "dir": "up"},
                {"name": "F_g", "label": "Weight (Fg)", "magnitude": round(mass * 9.8), "dir": "down"},
                {"name": "f_k", "label": "Friction (fk)", "magnitude": friction, "dir": "left"},
                {"name": "F_app", "label": "Applied Force (F)", "magnitude": f_applied, "dir": "right"}
            ]
        },
        "term": 1,
        "caps_weight_percent": 22,
        "suggested_duration_mins": 8,
        "prompt": prompt,
        "ideal_answer": f"{_fmt_sa(acc)} m·s⁻²",
        "sample_answer": calc_latex,
        "marks": 5,
        "misconception_tags": ["omitted_friction_from_fnet", "inverted_mass_acceleration", "confused_weight_with_mass"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_fnet", "desc": "Calculation of Net Force (F_net = F_app - f)", "marks": 2, "editable": True},
                {"id": "mp_formula", "desc": "Formula F_net = ma", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": "Substitution into formula", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"Final answer with unit: {_fmt_sa(acc)} m·s⁻²", "marks": 1, "editable": True}
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "1_nudge": f"First calculate the net force F_net by subtracting friction ({friction} N) from applied force ({f_applied} N).",
            "2_concept": "Apply Newton's Second Law: F_net = m * a.",
            "3_breakdown": f"F_net = {f_net} N. a = F_net / m = {f_net} / {mass} = {_fmt_sa(acc)} m·s⁻²."
        }
    }


def generate_inclined_plane_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    """Generates authentic Grade 11/12 inclined plane problem with kinetic friction."""
    g = 9.8
    mass = r.randint(5, 25)
    theta = r.choice([20, 25, 30, 35, 40, 45])
    theta_rad = math.radians(theta)
    
    fg_par = round(mass * g * math.sin(theta_rad), 2)
    fg_perp = round(mass * g * math.cos(theta_rad), 2)
    normal_force = fg_perp
    
    mu_k = r.choice([0.15, 0.20, 0.25, 0.30])
    fk = round(mu_k * normal_force, 2)
    
    f_app = round(fg_par + fk + mass * r.uniform(1.0, 3.5), 1)
    f_net = round(f_app - fg_par - fk, 2)
    acc = round(f_net / mass, 2)

    prompt = (
        f"A block of mass {_fmt_sa(mass)} kg is pulled UP a rough plane inclined at {_fmt_sa(theta)}° to the horizontal "
        f"by a constant force of {_fmt_sa(f_app)} N applied parallel to the plane. "
        f"The coefficient of kinetic friction between the block and the surface is {_fmt_sa(mu_k)}.\n\n"
        f"1. Draw a labelled free-body diagram showing all the forces acting on the block.\n"
        f"2. Calculate the magnitude of the kinetic frictional force (f_k).\n"
        f"3. Calculate the net force (F_net) acting on the block.\n"
        f"4. Calculate the acceleration of the block up the incline."
    )

    calc_latex = (
        rf"F_N = mg \cos\theta = ({_fmt_sa(mass)})(9{{,}}8)\cos({theta}^\circ) = {_fmt_sa(normal_force)}\text{{ N}}\\"
        rf"f_k = \mu_k F_N = ({_fmt_sa(mu_k)})({_fmt_sa(normal_force)}) = {_fmt_sa(fk)}\text{{ N}}\\"
        rf"F_{{g\parallel}} = mg \sin\theta = ({_fmt_sa(mass)})(9{{,}}8)\sin({theta}^\circ) = {_fmt_sa(fg_par)}\text{{ N}}\\"
        rf"F_{{\text{{net}}}} = F_{{\text{{app}}}} - F_{{g\parallel}} - f_k = {_fmt_sa(f_app)} - {_fmt_sa(fg_par)} - {_fmt_sa(fk)} = {_fmt_sa(f_net)}\text{{ N}}\\"
        rf"a = \frac{{F_{{\text{{net}}}}}}{{m}} = \frac{{{_fmt_sa(f_net)}}}{{{_fmt_sa(mass)}}} = {_fmt_sa(acc)}\text{{ m·s}}^{{-2}}"
    )

    return {
        "id": f"phys_incline_compound_{r.randint(100000, 999999)}",
        "topic": "Physical Sciences Mechanics",
        "subskill": "inclined_plane_newton",
        "mode": "compound",
        "modality": "free_body_diagram",
        "diagram_spec": {
            "diagram_role": "context",
            "kind": "free_body_diagram",
            "mass_kg": mass,
            "angle_deg": theta,
        },
        "fbd_spec": {
            "mass_kg": mass,
            "angle_deg": theta,
            "forces": [
                {"name": "F_N", "label": "Normal Force (FN)", "magnitude": normal_force, "dir": "up"},
                {"name": "F_g", "label": "Weight (Fg)", "magnitude": round(mass * 9.8), "dir": "down"},
                {"name": "f_k", "label": "Friction (fk)", "magnitude": fk, "dir": "left"},
                {"name": "F_app", "label": "Applied Force (F)", "magnitude": f_app, "dir": "right"}
            ]
        },
        "difficulty": "hard",
        "term": 1,
        "caps_weight_percent": 22,
        "suggested_duration_mins": 12,
        "prompt": prompt,
        "ideal_answer": f"a = {_fmt_sa(acc)} m·s⁻² up the incline",
        "sample_answer": calc_latex,
        "marks": 9,
        "misconception_tags": ["omitted_parallel_gravity_component", "confused_sin_cos_on_incline", "inverted_friction_direction"],
        "marking_schema": {
            "total_marks": 9,
            "marking_points": [
                {"id": "mp_fbd", "desc": "Free-body diagram (F_app, F_N, f_k, F_g labelled with arrows)", "marks": 4, "editable": True},
                {"id": "mp_fk", "desc": "Calculation of kinetic friction f_k = mu_k * mg * cos(theta)", "marks": 2, "editable": True},
                {"id": "mp_fnet", "desc": "Net force equation F_net = F_app - F_g|| - f_k", "marks": 2, "editable": True},
                {"id": "mp_acc", "desc": "Final acceleration with direction: a = F_net / m", "marks": 1, "editable": True}
            ],
            "deductions": [{"rule": "omitted_direction_in_vector_answer", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "1_nudge": "Resolve gravity into two perpendicular components: F_g|| down the slope and F_g_perp perpendicular to the slope.",
            "2_concept": "Normal force equals F_g_perp = mg cos(θ). Kinetic friction is f_k = mu_k F_N. Net force along the slope is F_app - F_g|| - f_k.",
            "3_breakdown": f"f_k = {_fmt_sa(fk)} N. F_g|| = {_fmt_sa(fg_par)} N. F_net = {_fmt_sa(f_net)} N. a = {_fmt_sa(acc)} m·s⁻²."
        }
    }


# ============================================================================
# UNIFIED GENERATE DISPATCHER & HELPER APIS
# ============================================================================

def get_subskills() -> List[str]:
    """Returns the ordered list of all 50 semantic subskill IDs."""
    return ORDERED_SUBSKILLS


def generate_question(subskill: Optional[str] = None, seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Generate a single question for a given subskill or random subskill."""
    r = _rng(seed)
    
    if subskill in ARCHETYPE_BUILDERS:
        builder = ARCHETYPE_BUILDERS[subskill]
        return builder(seed=seed, mode=mode)
    elif subskill == "newtons_second_law":
        return generate_newton_law_question(r, mode=mode)
    elif subskill in ("inclined_plane", "inclined_plane_newton"):
        return generate_inclined_plane_question(r, mode=mode)
    elif subskill == "kinematics_1d":
        return generate_kinematics_question(r, mode=mode)
    else:
        # Default: select from 50 semantic subskills
        chosen_id = r.choice(ORDERED_SUBSKILLS)
        return ARCHETYPE_BUILDERS[chosen_id](seed=seed, mode=mode)


def generate(subskill: str = "mixed", count: int = 1, mode: str = "compound", seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    """Entrypoint conforming to the universal generator contract."""
    r = _rng(seed)
    questions = []
    
    for i in range(count):
        sub_seed = (seed + i * 37) if seed is not None else r.randint(1000, 999999)
        
        # Handle legacy or specific subskills
        if subskill in ARCHETYPE_BUILDERS:
            q = ARCHETYPE_BUILDERS[subskill](seed=sub_seed, mode=mode)
        elif subskill in ("pulley_incline_masses_system", "two_body_pulley", "inclined_plane_pulley"):
            from app.utils.physical_sciences.physical_sciences_builders import build_pulley_incline_masses_system_question
            q = build_pulley_incline_masses_system_question(seed=sub_seed, grade=11, mode=mode)
        elif subskill in ("inclined_plane", "inclined_plane_newton"):
            q = generate_inclined_plane_question(r, mode=mode)
        elif subskill == "newtons_second_law":
            q = generate_newton_law_question(r, mode=mode)
        elif subskill == "kinematics_1d":
            q = generate_kinematics_question(r, mode=mode)
        else:
            # Deterministic round-robin / selection across the 50 semantic archetypes
            idx = (sub_seed if seed is not None else i) % len(ORDERED_SUBSKILLS)
            chosen_subskill = ORDERED_SUBSKILLS[idx]
            q = ARCHETYPE_BUILDERS[chosen_subskill](seed=sub_seed, mode=mode)
            
        questions.append(q)
        
    return questions
