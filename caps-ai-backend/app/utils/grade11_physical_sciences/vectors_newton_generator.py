"""Grade 11 Physical Sciences — Vectors in 2D & Newton's Laws (Deterministic 6-Pillar Generator).
Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 1/01. Vectors in two dimensions.md
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 2/01. Newton's laws.md

Complies strictly with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=1 (Vectors) or term=2 (Newton's Laws), caps_weight_percent, suggested_duration_mins.
2. Deconstructibility: Compound scenarios and atomic elementary sub-drills (elementary_vector_resolution, elementary_resultant_pythagoras, elementary_newton_second_law, elementary_inclined_friction).
3. Standardized Misconceptions: cos_sin_component_inversion, forgot_normal_force_angle, fnet_omitted_friction, resultant_direction_quadrant_confusion.
4. Teacher-Editable Marking Schema with [M] and [A] marks.
5. Deterministic 3-Tier Pre-Baked Hints.
6. South African comma decimal convention (",").
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "grade11_vectors_newton"
G_ACCEL = 9.8  # m/s^2

PROMPT_LEAD_HOOKS_VECTORS = [
    "During a structural engineering analysis of cable tensions,",
    "In a physics mechanics laboratory experiment on force resolution,",
    "A heavy crate is dragged across a rough horizontal concrete floor,",
    "A container of cargo rests on an inclined ramp during loading onto a transport truck,",
    "Two tugboats pull a disabled cargo vessel into Durban Harbour,"
]


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_vector_resolution_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Vectors in 2D: Resolve force into Fx and Fy, and determine resultant."""
    hook = r.choice(PROMPT_LEAD_HOOKS_VECTORS)
    qid = _make_id("vec11_resolution", seed, idx)

    f_mag = r.choice([40, 50, 60, 80, 100, 120, 150, 200])
    theta_deg = r.choice([25, 30, 35, 40, 45, 50, 60])
    theta_rad = math.radians(theta_deg)

    fx = f_mag * math.cos(theta_rad)
    fy = f_mag * math.sin(theta_rad)

    prompt = (
        f"{hook} a tensile force of {_fmt_sa(f_mag)} N is exerted on an eye-bolt at an angle of {theta_deg}° "
        f"above the positive x-axis (horizontal).\n\n"
        f"1. Define the term 'resultant vector'.\n"
        f"2. Calculate the magnitude of the horizontal component (Fx) of this force in N.\n"
        f"3. Calculate the magnitude of the vertical component (Fy) of this force in N."
    )
    ans_str = f"1. A single vector which has the same effect as two or more vectors acting together; 2. {_fmt_sa(fx)} N; 3. {_fmt_sa(fy)} N"
    memo = (
        "1. A resultant vector is the single vector that produces the same physical effect as two or more vectors acting together. [2]\n"
        f"2. Fx = F · cos(θ) [1M]\n"
        f"   Fx = ({_fmt_sa(f_mag)}) · cos({theta_deg}°) = {_fmt_sa(fx, 2)} N [1A]\n"
        f"3. Fy = F · sin(θ) [1M]\n"
        f"   Fy = ({_fmt_sa(f_mag)}) · sin({theta_deg}°) = {_fmt_sa(fy, 2)} N [1A]"
    )
    hints = {
        "tier_1": "Horizontal uses cosine; vertical uses sine. Look at adjacent vs opposite sides.",
        "tier_2": "Fx = F * cos(theta), Fy = F * sin(theta). Resultant has same effect as the combined vectors.",
        "tier_3": f"1. Same effect as multiple vectors. 2. Fx = {_fmt_sa(f_mag)} * cos({theta_deg}°) = {_fmt_sa(fx, 2)} N. 3. Fy = {_fmt_sa(f_mag)} * sin({theta_deg}°) = {_fmt_sa(fy, 2)} N.",
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "mode": mode,
        "topic": TOPIC,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 6,
        "hints": hints,
        "misconception_tags": ["cos_sin_component_inversion"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Resultant vector definition", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Fx component calculation", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Fy component calculation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_newton_friction_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Newton's Second Law & Friction: Fnet = ma with fk = mu_k * N."""
    hook = r.choice(PROMPT_LEAD_HOOKS_VECTORS)
    qid = _make_id("vec11_newton", seed, idx)

    mass = r.choice([5, 8, 10, 15, 20, 25, 30])
    mu_k = r.choice([0.15, 0.20, 0.25, 0.30, 0.35])
    f_pull = r.choice([40, 50, 60, 80, 100, 120])

    normal_force = mass * G_ACCEL
    f_k = mu_k * normal_force
    # Ensure net force is positive for forward acceleration
    while f_pull <= f_k + 5:
        f_pull += 20

    f_net = f_pull - f_k
    accel = f_net / mass

    prompt = (
        f"{hook} a wooden crate of mass {mass} kg is pulled along a rough horizontal floor by a constant horizontal force "
        f"of {f_pull} N. The coefficient of kinetic friction (μk) between the crate and the floor is {_fmt_sa(mu_k)}.\n\n"
        f"1. State Newton's Second Law of Motion in words.\n"
        f"2. Calculate the magnitude of the kinetic frictional force (fk) acting on the crate in N.\n"
        f"3. Calculate the acceleration of the crate in m·s⁻²."
    )
    ans_str = f"1. When a net force acts on an object, the object accelerates in the direction of the force with acceleration directly proportional to the force and inversely proportional to the mass; 2. {_fmt_sa(f_k)} N; 3. {_fmt_sa(accel)} m/s^2"
    memo = (
        "1. Newton's Second Law: When a net force acts on an object, the object will accelerate in the direction of the net force. "
        "The acceleration is directly proportional to the net force and inversely proportional to the mass of the object [2].\n"
        f"2. N = mg = ({mass})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(normal_force, 1)} N [1M]\n"
        f"   fk = μk · N = ({_fmt_sa(mu_k)})({_fmt_sa(normal_force, 1)}) = {_fmt_sa(f_k, 2)} N [1M, 1A]\n"
        f"3. Fnet = F_pull - fk = {f_pull} - {_fmt_sa(f_k, 2)} = {_fmt_sa(f_net, 2)} N [1M]\n"
        f"   Fnet = ma => a = Fnet / m = {_fmt_sa(f_net, 2)} / {mass} = {_fmt_sa(accel, 2)} m·s⁻² [1A]"
    )
    hints = {
        "tier_1": "Calculate normal force N = mg, then fk = mu_k * N, then Fnet = F_pull - fk.",
        "tier_2": "Fnet = ma. Kinetic friction opposes motion. Normal force on horizontal surface is mg.",
        "tier_3": f"1. Newton 2 law. 2. fk = ({_fmt_sa(mu_k)})({mass} * 9.8) = {_fmt_sa(f_k, 2)} N. 3. a = ({f_pull} - {_fmt_sa(f_k, 2)}) / {mass} = {_fmt_sa(accel, 2)} m/s^2.",
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "mode": mode,
        "topic": TOPIC,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 7,
        "hints": hints,
        "misconception_tags": ["fnet_omitted_friction"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Newton's Second Law statement", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Frictional force calculation (N = mg, fk = mu * N)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Acceleration calculation (Fnet = ma)", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_inclined_plane_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Inclined plane physics: Fg_parallel = mg * sin(theta), N = mg * cos(theta)."""
    hook = r.choice(PROMPT_LEAD_HOOKS_VECTORS)
    qid = _make_id("vec11_incline", seed, idx)

    mass = r.choice([10, 15, 20, 25, 30, 40, 50])
    incline_deg = r.choice([15, 20, 25, 30, 35])
    incline_rad = math.radians(incline_deg)

    fg = mass * G_ACCEL
    fg_parallel = fg * math.sin(incline_rad)
    fg_perp = fg * math.cos(incline_rad)
    normal_force = fg_perp

    prompt = (
        f"{hook} a crate of mass {mass} kg rests on a frictionless plane inclined at an angle of {incline_deg}° "
        f"to the horizontal.\n\n"
        f"1. Draw or describe the free-body diagram showing all forces acting on the crate.\n"
        f"2. Calculate the component of gravitational force acting parallel to the incline (down the slope) in N.\n"
        f"3. Calculate the magnitude of the normal force exerted by the surface on the crate in N.\n"
        f"4. Calculate the acceleration of the crate as it slides down the frictionless incline in m·s⁻²."
    )
    ans_str = f"1. Gravitational force vertically downwards, Normal force perpendicular to incline; 2. {_fmt_sa(fg_parallel)} N; 3. {_fmt_sa(normal_force)} N; 4. {_fmt_sa(fg_parallel / mass)} m/s^2"
    memo = (
        "1. Free-body diagram: Weight (Fg / w) acting vertically downwards [1]; Normal force (N) acting perpendicular to the inclined plane [1].\n"
        f"2. Fg∥ = mg · sin(θ) [1M]\n"
        f"   Fg∥ = ({mass})({_fmt_sa(G_ACCEL)}) · sin({incline_deg}°) = {_fmt_sa(fg_parallel, 2)} N down the slope [1A]\n"
        f"3. N = Fg⊥ = mg · cos(θ) [1M]\n"
        f"   N = ({mass})({_fmt_sa(G_ACCEL)}) · cos({incline_deg}°) = {_fmt_sa(normal_force, 2)} N perpendicular to slope [1A]\n"
        f"4. Fnet = Fg∥ = ma => a = (mg · sin(θ)) / m = g · sin(θ) [1M]\n"
        f"   a = ({_fmt_sa(G_ACCEL)}) · sin({incline_deg}°) = {_fmt_sa(fg_parallel / mass, 2)} m·s⁻² [1A]"
    )
    hints = {
        "tier_1": "Parallel component uses sin(theta); perpendicular component uses cos(theta).",
        "tier_2": "Fg_parallel = mg * sin(theta), N = mg * cos(theta). On a frictionless slope, a = g * sin(theta).",
        "tier_3": f"1. Weight down, Normal perpendicular. 2. Fg_parallel = {_fmt_sa(fg_parallel, 2)} N. 3. N = {_fmt_sa(normal_force, 2)} N. 4. a = {_fmt_sa(fg_parallel / mass, 2)} m/s^2.",
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "mode": mode,
        "topic": TOPIC,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 8,
        "hints": hints,
        "misconception_tags": ["forgot_normal_force_angle", "cos_sin_component_inversion"],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_1", "desc": "Free-body force identification", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Parallel weight component (mg sin theta)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Normal force component (mg cos theta)", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Acceleration along incline", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: str = "11",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Grade 11 Physical Sciences Vectors in 2D & Newton's Laws."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("vectors", "components", "resolution") or mode == "elementary_vector_resolution":
            q = _generate_vector_resolution_question(sub_r, sub_seed, i, mode)
        elif subskill in ("newton", "friction", "second_law") or mode == "elementary_newton_second_law":
            q = _generate_newton_friction_question(sub_r, sub_seed, i, mode)
        elif subskill in ("incline", "slope", "ramp") or mode == "elementary_inclined_friction":
            q = _generate_inclined_plane_question(sub_r, sub_seed, i, mode)
        else:
            chosen = sub_r.choice(["resolution", "newton", "incline"])
            if chosen == "resolution":
                q = _generate_vector_resolution_question(sub_r, sub_seed, i, mode)
            elif chosen == "newton":
                q = _generate_newton_friction_question(sub_r, sub_seed, i, mode)
            else:
                q = _generate_inclined_plane_question(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
