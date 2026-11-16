"""Grade 11 Physical Sciences — Newton's Laws Archetypes (Subskills 26–50).
Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 2/01. Newton's laws.md

Covers:
- Newton's First Law: Inertia, balanced forces, constant velocity, vehicle seatbelts.
- Newton's Second Law: Fnet = ma, horizontal motion, angled pull/push, vertical motion, elevators (apparent weight).
- Friction: Maximum static friction, kinetic friction, angle-induced normal force variations.
- Inclined Planes: Weight components, frictionless sliding, rough slope sliding, pulling uphill, impending static slip.
- Connected Masses: Horizontal 2-body systems, horizontal with friction, inclined plane systems, half-Atwood pulley systems.
- Newton's Third Law: Action-reaction pairs, contact vs non-contact interactions, reciprocal acceleration.
- Newton's Universal Gravitation: F = G*m1*m2/r^2, surface gravity g = G*M/R^2, proportionality and scaling ratios.

100% deterministic Python, pure SymPy/math, zero LLM calls, strictly < 2000 lines.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

G_ACCEL = 9.8  # m/s^2
G_CONST = 6.67e-11  # N*m^2/kg^2


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    """Formats numbers with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _svg_spec(svg: str) -> Dict[str, Any]:
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


# ==============================================================================
# 26. Newton's First Law — Inertia and Definition
# ==============================================================================
def builder_26(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_26_inertia", seed, idx)
    mass = rng.choice([2, 5, 12, 25, 50, 1200])
    vel = rng.choice([4, 10, 15, 20, 25])
    obj = rng.choice(["hockey puck", "curling stone", "spacecraft", "glider on an air track", "satellite"])

    prompt = (
        f"A {obj} of mass {mass} kg glides along a frictionless surface at a constant velocity "
        f"of {vel} m·s⁻¹ to the east.\n\n"
        f"1. State Newton's First Law of Motion in words.\n"
        f"2. Define the term 'inertia' and identify the physical quantity that provides a quantitative measure of inertia.\n"
        f"3. State the magnitude of the net horizontal force acting on the {obj} while it moves at constant velocity."
    )
    ans_str = (
        f"1. A body will remain in its state of rest or motion at constant velocity unless a non-zero resultant/net force acts on it; "
        f"2. Inertia is the resistance of an object to any change in its state of motion; mass is its quantitative measure; "
        f"3. 0 N"
    )
    memo = (
        "1. Newton's First Law: A body will remain in its state of rest or uniform motion in a straight line at constant velocity "
        "unless a non-zero resultant (net) force acts on it. [2]\n"
        "2. Inertia is the property of a body that resists any change in its state of rest or uniform motion in a straight line. [1]\n"
        f"   The quantitative measure of inertia is mass (measured in kg). [1]\n"
        f"3. Since velocity is constant (acceleration = 0 m·s⁻²), Fnet = 0 N. [1]"
    )
    hints = {
        "tier_1": "Constant velocity means acceleration is zero. What does Newton's First Law state about net force?",
        "tier_2": "Inertia is directly proportional to mass. When velocity is uniform, F_net must equal zero.",
        "tier_3": "1. Newton 1 definition. 2. Inertia is resistance to change in motion; mass is its measure. 3. F_net = 0 N.",
    }
    svg = (
        f'<svg viewBox="0 0 420 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr26" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>'
        f'<line x1="20" y1="140" x2="400" y2="140" stroke="#94a3b8" stroke-width="3"/><rect x="140" y="80" width="80" height="58" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="180" y="112" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">{mass} kg</text><line x1="220" y1="109" x2="310" y2="109" stroke="#2563eb" stroke-width="3" marker-end="url(#arr26)"/>'
        f'<text x="265" y="98" text-anchor="middle" font-size="12" fill="#1e40af">v = {vel} m/s (const)</text><text x="180" y="165" text-anchor="middle" font-size="12" fill="#64748b">Frictionless horizontal surface</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 6,
        "mode": "26_newtons_first_law_inertia_and_definition", "subskill": "26_newtons_first_law_inertia_and_definition",
        "subskill_id": "26_newtons_first_law_inertia_and_definition", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "vector_cartesian", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 5, "hints": hints,
        "misconception_tags": ["velocity_requires_force", "confusing_inertia_with_force"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Newton's First Law verbatim definition", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Definition of inertia", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Mass identified as measure of inertia", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Net force = 0 N for constant velocity", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 27. Newton's First Law — Balanced Forces and Static Equilibrium
# ==============================================================================
def builder_27(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_27_balanced", seed, idx)
    f_left = rng.choice([24, 35, 48, 60, 75, 90])
    f_right1 = rng.choice([10, 15, 20, 25])
    f_right2 = f_left - f_right1
    mass = rng.choice([5, 8, 12, 16, 20])

    prompt = (
        f"A block of mass {mass} kg rests in static equilibrium on a horizontal surface under the action of three "
        f"horizontal forces. Force F₁ = {f_left} N acts to the west (left). Force F₂ = {f_right1} N and an unknown force F₃ "
        f"act to the east (right).\n\n"
        f"1. Explain what is meant by 'balanced forces' in the context of Newton's First Law.\n"
        f"2. Write down the vector equation expressing the horizontal equilibrium condition.\n"
        f"3. Calculate the magnitude and direction of the unknown force F₃."
    )
    ans_str = f"1. Resultant (net) force is zero; 2. Fnet,x = F2 + F3 - F1 = 0; 3. F3 = {f_right2} N to the east (right)"
    memo = (
        "1. Balanced forces are forces acting on a body whose vector sum (net force) is equal to zero (Fnet = 0 N), "
        "producing zero acceleration. [1]\n"
        "2. Taking east (right) as positive: Fnet,x = F₂ + F₃ - F₁ = 0 [1M]\n"
        f"3. {f_right1} + F₃ - {f_left} = 0 [1M]\n"
        f"   F₃ = {f_left} - {f_right1} = {f_right2} N to the east [1A]"
    )
    hints = {
        "tier_1": "Static equilibrium means the block is at rest and the net force in the horizontal direction is zero.",
        "tier_2": "Sum of rightward forces must equal sum of leftward forces: F2 + F3 = F1.",
        "tier_3": f"F3 = F1 - F2 = {f_left} - {f_right1} = {f_right2} N to the east.",
    }
    svg = (
        f'<svg viewBox="0 0 440 200" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr27l" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#dc2626"/></marker>'
        f'<marker id="arr27r" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>'
        f'<line x1="20" y1="160" x2="420" y2="160" stroke="#94a3b8" stroke-width="3"/><rect x="170" y="100" width="80" height="60" rx="4" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>'
        f'<text x="210" y="135" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{mass} kg</text>'
        f'<line x1="170" y1="130" x2="70" y2="130" stroke="#dc2626" stroke-width="3" marker-end="url(#arr27l)"/><text x="120" y="120" text-anchor="middle" font-size="12" font-weight="bold" fill="#dc2626">F₁ = {f_left} N</text>'
        f'<line x1="250" y1="120" x2="330" y2="120" stroke="#2563eb" stroke-width="3" marker-end="url(#arr27r)"/><text x="290" y="110" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">F₂ = {f_right1} N</text>'
        f'<line x1="250" y1="145" x2="360" y2="145" stroke="#2563eb" stroke-width="3" stroke-dasharray="4,3" marker-end="url(#arr27r)"/><text x="310" y="160" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">F₃ = ?</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 7,
        "mode": "27_newtons_first_law_balanced_forces_equilibrium", "subskill": "27_newtons_first_law_balanced_forces_equilibrium",
        "subskill_id": "27_newtons_first_law_balanced_forces_equilibrium", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "vector_cartesian", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 4, "hints": hints,
        "misconception_tags": ["unbalanced_forces_assumption", "direction_omission_equilibrium"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of balanced forces", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Equilibrium vector equation Fnet = 0", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Substitution into equilibrium formula", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Magnitude and direction of F3", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 28. Newton's First Law — Constant Velocity Motion
# ==============================================================================
def builder_28(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_28_constvel", seed, idx)
    mass_car = rng.choice([1100, 1250, 1400, 1600, 1800])
    speed_kmh = rng.choice([80, 100, 120])
    speed_ms = round(speed_kmh / 3.6, 2)
    f_drag = rng.choice([450, 600, 750, 900, 1100])

    prompt = (
        f"A delivery vehicle of mass {mass_car} kg cruises along a straight, horizontal section of the N1 highway "
        f"at a constant speed of {speed_kmh} km·h⁻¹ ({_fmt_sa(speed_ms)} m·s⁻¹). The total resistive forces opposing motion "
        f"(air resistance and tyre rolling friction) equal {f_drag} N.\n\n"
        f"1. State the magnitude of the net horizontal force acting on the cruising vehicle.\n"
        f"2. Determine the forward driving force provided by the vehicle's engine.\n"
        f"3. Explain why the engine must continue to burn fuel even though the net force acting on the car is zero."
    )
    ans_str = (
        f"1. 0 N; 2. {f_drag} N forward; 3. The engine must exert a forward force equal in magnitude to resistive forces "
        f"to keep net force zero and maintain constant speed."
    )
    memo = (
        f"1. Since the vehicle is moving at constant velocity, acceleration a = 0 m·s⁻². "
        f"By Newton's First Law / Second Law: Fnet = ma = ({mass_car})(0) = 0 N. [1]\n"
        f"2. Fnet = F_engine - F_resistive = 0 => F_engine = F_resistive = {f_drag} N forward. [2]\n"
        f"3. Real surfaces and air exert opposing resistive forces ({f_drag} N). If the engine shut off, the net force "
        f"would become non-zero backwards (-{f_drag} N), causing deceleration. The engine force cancels resistive forces "
        f"so that Fnet = 0 N. [2]"
    )
    hints = {
        "tier_1": "Constant velocity means zero acceleration. What does Fnet = ma evaluate to?",
        "tier_2": "Forward engine force must balance total backward resistive forces so F_engine - F_resist = 0.",
        "tier_3": f"1. Fnet = 0 N. 2. F_engine = {f_drag} N. 3. Fuel is needed to overcome friction and drag.",
    }
    svg = (
        f'<svg viewBox="0 0 450 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr28f" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#16a34a"/></marker>'
        f'<marker id="arr28b" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#dc2626"/></marker></defs>'
        f'<line x1="20" y1="140" x2="430" y2="140" stroke="#94a3b8" stroke-width="3"/><rect x="150" y="80" width="130" height="50" rx="8" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>'
        f'<circle cx="180" cy="135" r="14" fill="#1e293b"/><circle cx="250" cy="135" r="14" fill="#1e293b"/><text x="215" y="110" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">{mass_car} kg</text>'
        f'<line x1="280" y1="105" x2="380" y2="105" stroke="#16a34a" stroke-width="3" marker-end="url(#arr28f)"/><text x="330" y="95" text-anchor="middle" font-size="11" font-weight="bold" fill="#16a34a">F_engine = ?</text>'
        f'<line x1="150" y1="105" x2="50" y2="105" stroke="#dc2626" stroke-width="3" marker-end="url(#arr28b)"/><text x="100" y="95" text-anchor="middle" font-size="11" font-weight="bold" fill="#dc2626">F_resist = {f_drag} N</text>'
        f'<text x="215" y="165" text-anchor="middle" font-size="12" fill="#475569">v = {_fmt_sa(speed_ms)} m/s (constant velocity)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 7,
        "mode": "28_newtons_first_law_constant_velocity_motion", "subskill": "28_newtons_first_law_constant_velocity_motion",
        "subskill_id": "28_newtons_first_law_constant_velocity_motion", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "vector_cartesian", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 5, "hints": hints,
        "misconception_tags": ["net_force_required_for_motion", "engine_force_exceeds_friction_at_const_v"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Fnet = 0 N deduction from constant velocity", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Equating engine force to resistive force", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Value and forward direction of engine force", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Physical explanation of fuel combustion overcoming resistance", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 29. Newton's First Law — Seatbelt Safety and Inertia Application
# ==============================================================================
def builder_29(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_29_seatbelt", seed, idx)
    m_passenger = rng.choice([60, 65, 70, 75, 80, 85])
    v_kmh = rng.choice([54, 72, 90, 108])
    v_ms = round(v_kmh / 3.6, 1)

    prompt = (
        f"A passenger of mass {m_passenger} kg travels in a motorcar at a speed of {v_kmh} km·h⁻¹ "
        f"({_fmt_sa(v_ms)} m·s⁻¹). The car collides head-on with a rigid barrier and comes to an abrupt halt.\n\n"
        f"1. Explain in terms of Newton's First Law and inertia what happens to an unrestrained passenger immediately after collision.\n"
        f"2. Explain the critical function of a seatbelt during this sudden deceleration.\n"
        f"3. State whether the force exerted by the seatbelt on the passenger acts forwards or backwards."
    )
    ans_str = (
        f"1. Due to inertia, the passenger continues moving forward at {_fmt_sa(v_ms)} m·s⁻¹ in a straight line; "
        f"2. The seatbelt provides an external unbalanced backward force that decelerates the passenger safely with the vehicle; "
        f"3. Backwards"
    )
    memo = (
        f"1. According to Newton's First Law, an object in motion tends to maintain its uniform velocity. "
        f"When the car stops abruptly, no horizontal stopping force initially acts on the unrestrained passenger, "
        f"so their inertia causes them to continue travelling forward at {_fmt_sa(v_ms)} m·s⁻¹ until striking the dashboard or windscreen. [2]\n"
        "2. The seatbelt provides the necessary external unbalanced force (directed backwards) on the passenger's torso, "
        "causing them to decelerate simultaneously with the vehicle cabin over a controlled distance. [2]\n"
        "3. The force acts backwards (opposite to the initial direction of motion). [1]"
    )
    hints = {
        "tier_1": "Think about what keeps the passenger moving when the car stops: inertia.",
        "tier_2": "Newton's First Law states an object in motion stays in motion unless an external net force acts.",
        "tier_3": "1. Continues forward at initial speed. 2. Seatbelt exerts backward force to decelerate passenger. 3. Backwards.",
    }
    svg = (
        f'<svg viewBox="0 0 420 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr29" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#dc2626"/></marker></defs>'
        f'<line x1="20" y1="150" x2="400" y2="150" stroke="#94a3b8" stroke-width="3"/><rect x="360" y="50" width="30" height="100" fill="#475569"/><text x="375" y="40" text-anchor="middle" font-size="11" fill="#475569">Barrier</text>'
        f'<rect x="180" y="80" width="120" height="60" rx="6" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><circle cx="230" cy="100" r="12" fill="#3b82f6"/><path d="M230,112 L230,135" stroke="#3b82f6" stroke-width="4"/>'
        f'<line x1="230" y1="95" x2="310" y2="95" stroke="#dc2626" stroke-width="3" marker-end="url(#arr29)"/><text x="270" y="85" text-anchor="middle" font-size="11" font-weight="bold" fill="#dc2626">v = {_fmt_sa(v_ms)} m/s</text>'
        f'<text x="240" y="168" text-anchor="middle" font-size="11" fill="#64748b">Passenger mass = {m_passenger} kg</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 6,
        "mode": "29_newtons_first_law_seatbelt_safety_application", "subskill": "29_newtons_first_law_seatbelt_safety_application",
        "subskill_id": "29_newtons_first_law_seatbelt_safety_application", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "vector_cartesian", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 5, "hints": hints,
        "misconception_tags": ["thrown_forward_force_fallacy", "seatbelt_pulls_forward_confusion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Inertia explanation of forward continuation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Seatbelt providing backward external force", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Direction correctly identified as backwards", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 30. Newton's Second Law — Formula Fnet = ma and Verbal Statement
# ==============================================================================
def builder_30(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_30_fnet_ma", seed, idx)
    mass = rng.choice([4, 6, 8, 12, 15, 20])
    accel = rng.choice([1.5, 2.0, 2.5, 3.2, 4.0, 5.0])
    f_net = round(mass * accel, 2)

    prompt = (
        f"A laboratory cart of mass {mass} kg accelerates horizontally across a low-friction track at {_fmt_sa(accel)} m·s⁻² "
        f"to the east.\n\n"
        f"1. State Newton's Second Law of Motion in words.\n"
        f"2. Write down the mathematical equation for Newton's Second Law.\n"
        f"3. Calculate the magnitude and direction of the net force acting on the cart in N."
    )
    ans_str = (
        f"1. When a resultant/net force acts on an object, the object will accelerate in the direction of the force at an "
        f"acceleration directly proportional to the force and inversely proportional to the mass of the object; "
        f"2. Fnet = ma; 3. {_fmt_sa(f_net)} N to the east"
    )
    memo = (
        "1. Newton's Second Law: When a net (resultant) force acts on an object, the object accelerates in the direction of the "
        "net force. The acceleration is directly proportional to the net force and inversely proportional to the mass of the object. [2]\n"
        "2. Fnet = ma [1]\n"
        f"3. Fnet = ({mass})({_fmt_sa(accel)}) = {_fmt_sa(f_net)} N to the east. [2]"
    )
    hints = {
        "tier_1": "Recall Fnet = ma directly. Force and acceleration are in the same direction.",
        "tier_2": "State the law verbatim: directly proportional to net force, inversely proportional to mass.",
        "tier_3": f"Fnet = {mass} * {_fmt_sa(accel)} = {_fmt_sa(f_net)} N to the east.",
    }
    svg = (
        f'<svg viewBox="0 0 420 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr30" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>'
        f'<line x1="20" y1="140" x2="400" y2="140" stroke="#94a3b8" stroke-width="3"/><rect x="140" y="80" width="80" height="50" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<circle cx="160" cy="135" r="8" fill="#1e3a8a"/><circle cx="200" cy="135" r="8" fill="#1e3a8a"/><text x="180" y="110" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">{mass} kg</text>'
        f'<line x1="220" y1="105" x2="330" y2="105" stroke="#2563eb" stroke-width="3" marker-end="url(#arr30)"/><text x="275" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">a = {_fmt_sa(accel)} m/s²</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 6,
        "mode": "30_newtons_second_law_formula_fnet_equals_ma", "subskill": "30_newtons_second_law_formula_fnet_equals_ma",
        "subskill_id": "30_newtons_second_law_formula_fnet_equals_ma", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "vector_cartesian", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 5, "hints": hints,
        "misconception_tags": ["inversely_proportional_confusion", "direction_omission_force"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Verbatim Newton's Second Law statement", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Fnet = ma equation", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Calculated value and unit", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Direction specified as east", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 31. Newton's Second Law — Horizontal Accelerating Crate with Friction
# ==============================================================================
def builder_31(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_31_horiz_fric", seed, idx)
    mass = rng.choice([10, 15, 20, 25, 30])
    mu_k = rng.choice([0.15, 0.20, 0.25, 0.30])
    n_force = round(mass * G_ACCEL, 1)
    fk = round(mu_k * n_force, 2)
    accel_target = rng.choice([1.2, 1.8, 2.4, 3.0])
    f_net = round(mass * accel_target, 2)
    f_app = round(fk + f_net, 1)
    accel = round((f_app - fk) / mass, 2)

    prompt = (
        f"A wooden crate of mass {mass} kg is pulled across a rough horizontal concrete warehouse floor by a constant "
        f"horizontal pulling force of {_fmt_sa(f_app)} N to the right. The coefficient of kinetic friction between the crate "
        f"and the floor is {_fmt_sa(mu_k)}.\n\n"
        f"1. Draw a labelled free-body diagram showing all forces acting on the crate.\n"
        f"2. Calculate the magnitude of the normal force (FN) exerted by the floor on the crate in N.\n"
        f"3. Calculate the magnitude of the kinetic frictional force (fk) in N.\n"
        f"4. Calculate the horizontal acceleration of the crate in m·s⁻²."
    )
    ans_str = (
        f"1. Free-body diagram with FN, Fg, Fapplied, fk; 2. {_fmt_sa(n_force)} N; "
        f"3. {_fmt_sa(fk)} N; 4. {_fmt_sa(accel)} m/s^2 to the right"
    )
    memo = (
        "1. Free-body diagram: FN (up), Fg/w (down), Fapplied (right), fk (left). [2]\n"
        f"2. Vertical equilibrium: FN = Fg = mg = ({mass})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(n_force)} N [1M, 1A]\n"
        f"3. fk = μk · FN = ({_fmt_sa(mu_k)})({_fmt_sa(n_force)}) = {_fmt_sa(fk)} N [1M, 1A]\n"
        f"4. Fnet = Fapplied - fk = {_fmt_sa(f_app)} - {_fmt_sa(fk)} = {_fmt_sa(f_app - fk, 2)} N [1M]\n"
        f"   Fnet = ma => a = Fnet / m = {_fmt_sa(f_app - fk, 2)} / {mass} = {_fmt_sa(accel)} m·s⁻² to the right [1A]"
    )
    hints = {
        "tier_1": "FN = mg for a horizontal surface with horizontal forces. Then fk = mu_k * FN.",
        "tier_2": "Fnet = F_app - fk. Then use Fnet = ma to solve for a.",
        "tier_3": f"FN = {_fmt_sa(n_force)} N, fk = {_fmt_sa(fk)} N, a = ({_fmt_sa(f_app)} - {_fmt_sa(fk)}) / {mass} = {_fmt_sa(accel)} m/s^2.",
    }
    svg = (
        f'<svg viewBox="0 0 440 220" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr31u" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#16a34a"/></marker>'
        f'<marker id="arr31d" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#64748b"/></marker>'
        f'<marker id="arr31r" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker>'
        f'<marker id="arr31l" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#dc2626"/></marker></defs>'
        f'<circle cx="220" cy="110" r="8" fill="#0f172a"/><line x1="220" y1="110" x2="220" y2="35" stroke="#16a34a" stroke-width="3" marker-end="url(#arr31u)"/><text x="235" y="45" font-size="12" font-weight="bold" fill="#16a34a">FN</text>'
        f'<line x1="220" y1="110" x2="220" y2="185" stroke="#64748b" stroke-width="3" marker-end="url(#arr31d)"/><text x="235" y="180" font-size="12" font-weight="bold" fill="#64748b">Fg = {_fmt_sa(n_force)} N</text>'
        f'<line x1="220" y1="110" x2="330" y2="110" stroke="#2563eb" stroke-width="3" marker-end="url(#arr31r)"/><text x="290" y="95" font-size="12" font-weight="bold" fill="#2563eb">Fapplied = {_fmt_sa(f_app)} N</text>'
        f'<line x1="220" y1="110" x2="130" y2="110" stroke="#dc2626" stroke-width="3" marker-end="url(#arr31l)"/><text x="160" y="95" font-size="12" font-weight="bold" fill="#dc2626">fk = ?</text>'
        f'<text x="220" y="210" text-anchor="middle" font-size="11" fill="#475569">Mass = {mass} kg, μk = {_fmt_sa(mu_k)}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 9,
        "mode": "31_newtons_second_law_horizontal_accelerating_crate", "subskill": "31_newtons_second_law_horizontal_accelerating_crate",
        "subskill_id": "31_newtons_second_law_horizontal_accelerating_crate", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 7, "hints": hints,
        "misconception_tags": ["fnet_omitted_friction", "normal_force_inversion"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Labelled free-body diagram", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Normal force FN = mg", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Kinetic friction fk = mu_k * FN", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Net force Fnet and acceleration a = Fnet/m", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 32. Newton's Second Law — Angled Pulling Force (Normal Force Reduction)
# ==============================================================================
def builder_32(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_32_angled_pull", seed, idx)
    mass = rng.choice([15, 20, 25, 30, 40])
    f_pull = rng.choice([80, 100, 120, 150, 180])
    theta_deg = rng.choice([25, 30, 35, 40])
    mu_k = rng.choice([0.15, 0.20, 0.25])

    theta_rad = math.radians(theta_deg)
    fx = f_pull * math.cos(theta_rad)
    fy = f_pull * math.sin(theta_rad)

    w = mass * G_ACCEL
    fn = w - fy
    fk = mu_k * fn
    f_net = fx - fk
    accel = f_net / mass

    prompt = (
        f"A crate of mass {mass} kg rests on a rough horizontal floor. A worker pulls the crate with a rope exerting "
        f"a force of {f_pull} N at an angle of {theta_deg}° above the horizontal. The coefficient of kinetic friction "
        f"is {_fmt_sa(mu_k)}.\n\n"
        f"1. Calculate the vertical component (Fy) and horizontal component (Fx) of the pulling force in N.\n"
        f"2. Show by calculation that the magnitude of the normal force exerted by the floor on the crate is {_fmt_sa(fn, 2)} N.\n"
        f"3. Calculate the magnitude of the kinetic frictional force (fk) in N.\n"
        f"4. Calculate the horizontal acceleration of the crate in m·s⁻²."
    )
    ans_str = (
        f"1. Fx = {_fmt_sa(fx, 2)} N, Fy = {_fmt_sa(fy, 2)} N; 2. FN = mg - Fy = {_fmt_sa(fn, 2)} N; "
        f"3. fk = {_fmt_sa(fk, 2)} N; 4. a = {_fmt_sa(accel, 2)} m/s^2"
    )
    memo = (
        f"1. Fx = F · cos({theta_deg}°) = ({f_pull}) · cos({theta_deg}°) = {_fmt_sa(fx, 2)} N [1M, 1A]\n"
        f"   Fy = F · sin({theta_deg}°) = ({f_pull}) · sin({theta_deg}°) = {_fmt_sa(fy, 2)} N [1M, 1A]\n"
        f"2. Vertical equilibrium: FN + Fy - Fg = 0 => FN = mg - Fy [1M]\n"
        f"   FN = ({mass})({_fmt_sa(G_ACCEL)}) - {_fmt_sa(fy, 2)} = {_fmt_sa(w, 1)} - {_fmt_sa(fy, 2)} = {_fmt_sa(fn, 2)} N [1A]\n"
        f"3. fk = μk · FN = ({_fmt_sa(mu_k)})({_fmt_sa(fn, 2)}) = {_fmt_sa(fk, 2)} N [1M, 1A]\n"
        f"4. Fnet,x = Fx - fk = {_fmt_sa(fx, 2)} - {_fmt_sa(fk, 2)} = {_fmt_sa(f_net, 2)} N [1M]\n"
        f"   a = Fnet,x / m = {_fmt_sa(f_net, 2)} / {mass} = {_fmt_sa(accel, 2)} m·s⁻² [1A]"
    )
    hints = {
        "tier_1": "Because the pull has an upward vertical component Fy, the normal force is reduced: FN = mg - Fy.",
        "tier_2": "Calculate Fx = F*cos(theta), Fy = F*sin(theta), FN = mg - Fy, fk = mu_k * FN, then Fnet = Fx - fk.",
        "tier_3": f"Fx = {_fmt_sa(fx, 2)} N, Fy = {_fmt_sa(fy, 2)} N, FN = {_fmt_sa(fn, 2)} N, a = {_fmt_sa(accel, 2)} m/s^2.",
    }
    svg = (
        f'<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr32" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>'
        f'<line x1="20" y1="170" x2="430" y2="170" stroke="#94a3b8" stroke-width="3"/><rect x="140" y="110" width="80" height="60" rx="4" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="180" y="145" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">{mass} kg</text><line x1="220" y1="130" x2="330" y2="80" stroke="#2563eb" stroke-width="3" marker-end="url(#arr32)"/>'
        f'<line x1="220" y1="130" x2="310" y2="130" stroke="#94a3b8" stroke-dasharray="3,3"/><path d="M255,130 A35,35 0 0,0 250,116" fill="none" stroke="#2563eb" stroke-width="1.5"/>'
        f'<text x="268" y="125" font-size="11" fill="#1e40af">{theta_deg}°</text><text x="315" y="70" font-size="12" font-weight="bold" fill="#2563eb">F = {f_pull} N</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 10,
        "mode": "32_newtons_second_law_angled_pulling_force", "subskill": "32_newtons_second_law_angled_pulling_force",
        "subskill_id": "32_newtons_second_law_angled_pulling_force", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 9, "hints": hints,
        "misconception_tags": ["forgot_normal_force_angle", "added_instead_of_subtracted_vertical_force"],
        "marking_schema": {
            "total_marks": 9,
            "marking_points": [
                {"id": "mp_1", "desc": "Fx component resolution", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Fy component resolution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Normal force derivation FN = mg - Fy", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Kinetic friction calculation", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Acceleration calculation a = (Fx - fk)/m", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 33. Newton's Second Law — Angled Pushing Force (Normal Force Increase)
# ==============================================================================
def builder_33(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_33_angled_push", seed, idx)
    mass = rng.choice([12, 16, 20, 24, 30])
    f_push = rng.choice([70, 90, 110, 130])
    theta_deg = rng.choice([25, 30, 35])
    mu_k = rng.choice([0.15, 0.20, 0.25])

    theta_rad = math.radians(theta_deg)
    fx = f_push * math.cos(theta_rad)
    fy = f_push * math.sin(theta_rad)

    w = mass * G_ACCEL
    fn = w + fy
    fk = mu_k * fn
    f_net = fx - fk
    accel = f_net / mass

    prompt = (
        f"A gardener pushes a lawn mower of mass {mass} kg across flat turf by applying a force of {f_push} N "
        f"directed along the handle at an angle of {theta_deg}° below the horizontal. The coefficient of kinetic friction "
        f"between the wheels and the turf is {_fmt_sa(mu_k)}.\n\n"
        f"1. Explain why pushing downwards increases the normal force compared to pulling at an upward angle.\n"
        f"2. Calculate the magnitude of the normal force (FN) exerted by the ground on the mower in N.\n"
        f"3. Calculate the magnitude of the kinetic frictional force (fk) in N.\n"
        f"4. Calculate the horizontal acceleration of the mower in m·s⁻²."
    )
    ans_str = (
        f"1. Pushing adds a downward vertical component Fy to the weight, requiring a larger normal force FN = mg + Fy; "
        f"2. FN = {_fmt_sa(fn, 2)} N; 3. fk = {_fmt_sa(fk, 2)} N; 4. a = {_fmt_sa(accel, 2)} m/s^2"
    )
    memo = (
        "1. The applied push has a downward vertical component (Fy = F · sin θ) that presses into the ground along with "
        "the gravitational weight. In vertical equilibrium, FN = mg + Fy, which is greater than mg. [2]\n"
        f"2. Fy = F · sin({theta_deg}°) = ({f_push}) · sin({theta_deg}°) = {_fmt_sa(fy, 2)} N [1M]\n"
        f"   FN = mg + Fy = ({mass})({_fmt_sa(G_ACCEL)}) + {_fmt_sa(fy, 2)} = {_fmt_sa(w, 1)} + {_fmt_sa(fy, 2)} = {_fmt_sa(fn, 2)} N [1A]\n"
        f"3. fk = μk · FN = ({_fmt_sa(mu_k)})({_fmt_sa(fn, 2)}) = {_fmt_sa(fk, 2)} N [1M, 1A]\n"
        f"4. Fx = F · cos({theta_deg}°) = ({f_push}) · cos({theta_deg}°) = {_fmt_sa(fx, 2)} N [1M]\n"
        f"   Fnet,x = Fx - fk = {_fmt_sa(fx, 2)} - {_fmt_sa(fk, 2)} = {_fmt_sa(f_net, 2)} N\n"
        f"   a = Fnet,x / m = {_fmt_sa(f_net, 2)} / {mass} = {_fmt_sa(accel, 2)} m·s⁻² [1A]"
    )
    hints = {
        "tier_1": "A downward push adds to the weight: FN = mg + F*sin(theta).",
        "tier_2": "Calculate Fy = F*sin(theta), FN = mg + Fy, fk = mu_k * FN, Fx = F*cos(theta), and a = (Fx - fk)/m.",
        "tier_3": f"FN = {_fmt_sa(fn, 2)} N, fk = {_fmt_sa(fk, 2)} N, a = {_fmt_sa(accel, 2)} m/s^2.",
    }
    svg = (
        f'<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr33" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#dc2626"/></marker></defs>'
        f'<line x1="20" y1="170" x2="430" y2="170" stroke="#94a3b8" stroke-width="3"/><rect x="180" y="110" width="90" height="60" rx="4" fill="#fee2e2" stroke="#b91c1c" stroke-width="2"/>'
        f'<text x="225" y="145" text-anchor="middle" font-size="12" font-weight="bold" fill="#7f1d1d">{mass} kg</text><line x1="90" y1="50" x2="180" y2="120" stroke="#dc2626" stroke-width="3" marker-end="url(#arr33)"/>'
        f'<line x1="90" y1="50" x2="180" y2="50" stroke="#94a3b8" stroke-dasharray="3,3"/><text x="125" y="42" font-size="11" fill="#b91c1c">{theta_deg}°</text>'
        f'<text x="110" y="90" font-size="12" font-weight="bold" fill="#dc2626">F = {f_push} N</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 10,
        "mode": "33_newtons_second_law_angled_pushing_force", "subskill": "33_newtons_second_law_angled_pushing_force",
        "subskill_id": "33_newtons_second_law_angled_pushing_force", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 8, "hints": hints,
        "misconception_tags": ["subtracted_downward_push_from_normal", "forgot_push_increases_friction"],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_1", "desc": "Physical explanation of normal force increase", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Calculation of normal force FN = mg + Fy", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Kinetic friction calculation", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Horizontal acceleration calculation", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 34. Newton's Second Law — Vertical Motion (Crane Hoist / Rocket)
# ==============================================================================
def builder_34(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_34_vertical_lift", seed, idx)
    mass = rng.choice([250, 400, 500, 750, 1000])
    accel = rng.choice([1.2, 1.5, 2.0, 2.5, 3.0])
    w = mass * G_ACCEL
    f_net = mass * accel
    tension = w + f_net

    prompt = (
        f"A construction crane hoists a steel beam of mass {mass} kg vertically upwards with an acceleration "
        f"of {_fmt_sa(accel)} m·s⁻².\n\n"
        f"1. Draw a labelled free-body diagram of all vertical forces acting on the beam.\n"
        f"2. Calculate the gravitational weight (w / Fg) of the beam in N.\n"
        f"3. Write down the net vertical force equation in terms of tension (T) and weight (Fg).\n"
        f"4. Calculate the tension (T) in the crane's hoisting cable in N."
    )
    ans_str = (
        f"1. Free-body diagram with T (up) and Fg (down); 2. {_fmt_sa(w, 1)} N; "
        f"3. Fnet = T - Fg = ma; 4. {_fmt_sa(tension, 1)} N"
    )
    memo = (
        "1. Free-body diagram: Tension T acting vertically upwards, Weight Fg (w) acting vertically downwards. [2]\n"
        f"2. Fg = mg = ({mass})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(w, 1)} N [1M, 1A]\n"
        "3. Taking upward direction as positive: Fnet = T - Fg = ma [1]\n"
        f"4. T - {_fmt_sa(w, 1)} = ({mass})({_fmt_sa(accel)})\n"
        f"   T = {_fmt_sa(w, 1)} + {_fmt_sa(f_net, 1)} = {_fmt_sa(tension, 1)} N [2]"
    )
    hints = {
        "tier_1": "For upward acceleration, upward cable tension must exceed downward weight: T - mg = ma.",
        "tier_2": "Weight Fg = mg. Then T = m(g + a).",
        "tier_3": f"Fg = {_fmt_sa(w, 1)} N, T = {mass} * (9.8 + {_fmt_sa(accel)}) = {_fmt_sa(tension, 1)} N.",
    }
    svg = (
        f'<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr34u" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker>'
        f'<marker id="arr34d" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#64748b"/></marker></defs>'
        f'<circle cx="200" cy="120" r="8" fill="#0f172a"/><line x1="200" y1="120" x2="200" y2="30" stroke="#2563eb" stroke-width="4" marker-end="url(#arr34u)"/><text x="215" y="45" font-size="12" font-weight="bold" fill="#2563eb">T (Tension)</text>'
        f'<line x1="200" y1="120" x2="200" y2="205" stroke="#64748b" stroke-width="3" marker-end="url(#arr34d)"/><text x="215" y="195" font-size="12" font-weight="bold" fill="#64748b">Fg = mg = {_fmt_sa(w, 1)} N</text>'
        f'<text x="200" y="230" text-anchor="middle" font-size="12" fill="#1e40af">a = {_fmt_sa(accel)} m/s² (upwards)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 8,
        "mode": "34_newtons_second_law_vertical_motion_rocket_elevator", "subskill": "34_newtons_second_law_vertical_motion_rocket_elevator",
        "subskill_id": "34_newtons_second_law_vertical_motion_rocket_elevator", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 7, "hints": hints,
        "misconception_tags": ["tension_equals_weight_during_acceleration", "sign_error_vertical_acceleration"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Labelled free-body diagram", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Weight calculation w = mg", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Net force expression Fnet = T - Fg", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Tension calculation T = m(g + a)", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 35. Newton's Second Law — Apparent Weight and Scale in Elevator
# ==============================================================================
def builder_35(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_35_elevator_scale", seed, idx)
    mass = rng.choice([55, 60, 68, 72, 80, 85])
    accel = rng.choice([1.2, 1.6, 2.0, 2.5])
    direction = rng.choice(["upwards", "downwards"])

    true_weight = round(mass * G_ACCEL, 1)
    if direction == "upwards":
        fn = round(mass * (G_ACCEL + accel), 1)
        scale_kg = round(fn / G_ACCEL, 1)
        comp_word = "greater than"
    else:
        fn = round(mass * (G_ACCEL - accel), 1)
        scale_kg = round(fn / G_ACCEL, 1)
        comp_word = "less than"

    prompt = (
        f"A learner of mass {mass} kg stands on a bathroom scale calibrated in Newtons on the floor of a passenger lift (elevator). "
        f"The lift accelerates {direction} at {_fmt_sa(accel)} m·s⁻².\n\n"
        f"1. State what physical quantity the bathroom scale actually measures (true weight or normal force).\n"
        f"2. Calculate the learner's true gravitational weight (w = mg) in N.\n"
        f"3. Calculate the reading on the bathroom scale (apparent weight) in N.\n"
        f"4. State whether the scale reading is greater than, less than, or equal to the learner's true weight."
    )
    ans_str = (
        f"1. Normal force (FN); 2. {_fmt_sa(true_weight)} N; 3. {_fmt_sa(fn)} N; "
        f"4. {comp_word} the true weight"
    )
    memo = (
        "1. The bathroom scale measures the upward normal force (FN) exerted by the scale on the person's feet. [1]\n"
        f"2. w = mg = ({mass})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(true_weight)} N [1M, 1A]\n"
    )
    if direction == "upwards":
        memo += (
            f"3. Taking upward as positive: Fnet = FN - mg = ma [1M]\n"
            f"   FN = m(g + a) = ({mass})({_fmt_sa(G_ACCEL)} + {_fmt_sa(accel)}) = {_fmt_sa(fn)} N [1A]\n"
            f"4. The scale reading ({_fmt_sa(fn)} N) is greater than the true weight ({_fmt_sa(true_weight)} N). [1]"
        )
    else:
        memo += (
            f"3. Taking downward as positive: Fnet = mg - FN = ma [1M]\n"
            f"   FN = m(g - a) = ({mass})({_fmt_sa(G_ACCEL)} - {_fmt_sa(accel)}) = {_fmt_sa(fn)} N [1A]\n"
            f"4. The scale reading ({_fmt_sa(fn)} N) is less than the true weight ({_fmt_sa(true_weight)} N). [1]"
        )

    hints = {
        "tier_1": f"When accelerating {direction}, net force is directed {direction}. Scale reads FN.",
        "tier_2": f"If upward: FN = m(g + a). If downward: FN = m(g - a).",
        "tier_3": f"True weight = {_fmt_sa(true_weight)} N. Scale reading = {_fmt_sa(fn)} N ({comp_word}).",
    }
    svg = (
        f'<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="130" y="20" width="160" height="180" rx="6" fill="#e2e8f0" stroke="#475569" stroke-width="2"/><rect x="160" y="175" width="100" height="15" rx="3" fill="#cbd5e1" stroke="#334155" stroke-width="1.5"/><text x="210" y="186" text-anchor="middle" font-size="10" fill="#334155">Scale</text>'
        f'<circle cx="210" cy="115" r="14" fill="#3b82f6"/><line x1="210" y1="129" x2="210" y2="165" stroke="#3b82f6" stroke-width="4"/><line x1="210" y1="165" x2="195" y2="175" stroke="#3b82f6" stroke-width="3"/><line x1="210" y1="165" x2="225" y2="175" stroke="#3b82f6" stroke-width="3"/>'
        f'<text x="210" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">a = {_fmt_sa(accel)} m/s² ({direction})</text><text x="210" y="212" text-anchor="middle" font-size="11" fill="#475569">Learner mass = {mass} kg</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 8,
        "mode": "35_newtons_second_law_apparent_weight_scale_in_elevator", "subskill": "35_newtons_second_law_apparent_weight_scale_in_elevator",
        "subskill_id": "35_newtons_second_law_apparent_weight_scale_in_elevator", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 6, "hints": hints,
        "misconception_tags": ["scale_measures_gravity_not_normal", "elevator_acceleration_sign_confusion"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification that scale measures normal force", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "True gravitational weight w = mg", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Scale reading calculation FN = m(g +- a)", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Comparison with true weight", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 36. Static Friction — Maximum Coefficient and Impending Motion
# ==============================================================================
def builder_36(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_36_static_fric", seed, idx)
    mass = rng.choice([8, 12, 16, 20, 25])
    mu_s = rng.choice([0.35, 0.40, 0.45, 0.50, 0.55])
    fn = round(mass * G_ACCEL, 1)
    fs_max = round(mu_s * fn, 2)
    f_test = round(fs_max * rng.choice([0.7, 1.2]), 1)
    will_move = f_test > fs_max

    prompt = (
        f"A heavy steel box of mass {mass} kg rests on a rough horizontal workshop floor. The coefficient of static "
        f"friction (μs) between the box and the floor is {_fmt_sa(mu_s)}.\n\n"
        f"1. Define the term 'static frictional force'.\n"
        f"2. Calculate the maximum static frictional force (fs^max) that can develop before the box begins to slip in N.\n"
        f"3. A worker pushes horizontally on the box with a force of {_fmt_sa(f_test)} N. Determine whether the box "
        f"remains stationary or begins to accelerate, and state the actual frictional force acting on the box."
    )
    if will_move:
        ans_str = (
            f"1. Static friction is the force that opposes the tendency of motion of a stationary object relative to a surface; "
            f"2. fs^max = {_fmt_sa(fs_max)} N; 3. The box begins to accelerate because applied force ({_fmt_sa(f_test)} N) > fs^max ({_fmt_sa(fs_max)} N)"
        )
        memo_part3 = (
            f"3. Applied force F = {_fmt_sa(f_test)} N exceeds fs^max = {_fmt_sa(fs_max)} N. "
            f"Therefore, the box breaks static equilibrium and begins to accelerate. [2]"
        )
    else:
        ans_str = (
            f"1. Static friction is the force that opposes the tendency of motion of a stationary object relative to a surface; "
            f"2. fs^max = {_fmt_sa(fs_max)} N; 3. The box remains stationary; actual static friction fs = {_fmt_sa(f_test)} N"
        )
        memo_part3 = (
            f"3. Applied force F = {_fmt_sa(f_test)} N is less than fs^max = {_fmt_sa(fs_max)} N. "
            f"The box remains stationary. The actual static friction adjusts to match the applied force: "
            f"fs = {_fmt_sa(f_test)} N opposing the push. [2]"
        )

    memo = (
        "1. Static frictional force is the force that opposes the tendency of motion of a stationary object relative to a surface. [1]\n"
        f"2. FN = mg = ({mass})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(fn)} N [1M]\n"
        f"   fs^max = μs · FN = ({_fmt_sa(mu_s)})({_fmt_sa(fn)}) = {_fmt_sa(fs_max)} N [1A]\n"
        f"{memo_part3}"
    )
    hints = {
        "tier_1": "Maximum static friction is fs^max = mu_s * FN. If applied force < fs^max, object does not move.",
        "tier_2": "When stationary, static friction exactly equals the applied force, up to fs^max.",
        "tier_3": f"fs^max = {_fmt_sa(fs_max)} N. Test force = {_fmt_sa(f_test)} N.",
    }
    svg = (
        f'<svg viewBox="0 0 420 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<line x1="20" y1="140" x2="400" y2="140" stroke="#94a3b8" stroke-width="3"/><rect x="150" y="80" width="80" height="60" rx="4" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>'
        f'<text x="190" y="115" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">{mass} kg</text><text x="190" y="165" text-anchor="middle" font-size="11" fill="#64748b">μs = {_fmt_sa(mu_s)}, F_test = {_fmt_sa(f_test)} N</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 8,
        "mode": "36_static_friction_maximum_coefficient", "subskill": "36_static_friction_maximum_coefficient",
        "subskill_id": "36_static_friction_maximum_coefficient", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 5, "hints": hints,
        "misconception_tags": ["static_friction_always_equals_fs_max", "confusing_static_and_kinetic_coefficients"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of static friction", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Calculation of fs^max = mu_s * FN", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "State of motion assessment and actual friction value", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 37. Kinetic Friction — Constant Velocity and μk Determination
# ==============================================================================
def builder_37(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_37_kinetic_fric", seed, idx)
    mass = rng.choice([15, 20, 25, 30, 40, 50])
    mu_k = rng.choice([0.18, 0.22, 0.25, 0.32, 0.38])
    fn = round(mass * G_ACCEL, 1)
    fk = round(mu_k * fn, 2)

    prompt = (
        f"A laboratory sled of mass {mass} kg is pulled across a flat horizontal surface at a constant velocity "
        f"by a horizontal pulling force of {_fmt_sa(fk)} N.\n\n"
        f"1. Define 'kinetic frictional force'.\n"
        f"2. State why the kinetic frictional force acting on the sled must equal {_fmt_sa(fk)} N.\n"
        f"3. Calculate the coefficient of kinetic friction (μk) between the sled and the surface."
    )
    ans_str = (
        f"1. Kinetic friction is the force that opposes the motion of a moving object relative to a surface; "
        f"2. Constant velocity implies Fnet = 0, so applied force balances fk; "
        f"3. μk = {_fmt_sa(mu_k, 2)}"
    )
    memo = (
        "1. Kinetic frictional force is the force that opposes the motion of a moving object relative to a surface. [1]\n"
        f"2. When moving at constant velocity, acceleration a = 0 m·s⁻², which means Fnet = 0 N. "
        f"Therefore, Fpull - fk = 0 => fk = Fpull = {_fmt_sa(fk)} N. [2]\n"
        f"3. FN = mg = ({mass})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(fn)} N [1M]\n"
        f"   fk = μk · FN => μk = fk / FN = {_fmt_sa(fk)} / {_fmt_sa(fn)} = {_fmt_sa(mu_k, 2)} [1A]"
    )
    hints = {
        "tier_1": "Constant velocity means net force is zero, so friction balances the pull.",
        "tier_2": "Calculate FN = mg, then mu_k = fk / FN.",
        "tier_3": f"FN = {_fmt_sa(fn)} N. mu_k = {_fmt_sa(fk)} / {_fmt_sa(fn)} = {_fmt_sa(mu_k, 2)}.",
    }
    svg = (
        f'<svg viewBox="0 0 420 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<line x1="20" y1="140" x2="400" y2="140" stroke="#94a3b8" stroke-width="3"/><rect x="150" y="80" width="80" height="60" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="190" y="115" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">{mass} kg</text><text x="190" y="165" text-anchor="middle" font-size="11" fill="#64748b">Fpull = {_fmt_sa(fk)} N (constant velocity)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 7,
        "mode": "37_kinetic_friction_constant_velocity_or_acceleration", "subskill": "37_kinetic_friction_constant_velocity_or_acceleration",
        "subskill_id": "37_kinetic_friction_constant_velocity_or_acceleration", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 5, "hints": hints,
        "misconception_tags": ["coefficient_of_friction_units_confusion", "fnet_non_zero_at_const_v"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of kinetic friction", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Justification that fk = Fpull at constant velocity", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Normal force FN calculation", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Coefficient of friction calculation mu_k = fk/FN", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 38. Friction — Angled Pull Normal Force Reduction Quantitative Comparison
# ==============================================================================
def builder_38(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_38_fric_pull_red", seed, idx)
    mass = rng.choice([20, 25, 30, 40])
    f_pull = rng.choice([60, 80, 100, 120])
    theta_deg = rng.choice([30, 35, 40])
    mu_k = rng.choice([0.25, 0.30, 0.35])

    theta_rad = math.radians(theta_deg)
    fy = f_pull * math.sin(theta_rad)
    fn_horiz = mass * G_ACCEL
    fk_horiz = mu_k * fn_horiz

    fn_angled = fn_horiz - fy
    fk_angled = mu_k * fn_angled
    delta_fk = fk_horiz - fk_angled

    prompt = (
        f"A trunk of mass {mass} kg rests on a rough horizontal floor with kinetic friction coefficient {_fmt_sa(mu_k)}.\n\n"
        f"Case A: The trunk is pulled horizontally.\n"
        f"Case B: The trunk is pulled with a force of {f_pull} N directed at {theta_deg}° above the horizontal.\n\n"
        f"1. Calculate the normal force in Case A (horizontal pull) in N.\n"
        f"2. Calculate the normal force in Case B (angled pull) in N.\n"
        f"3. Calculate the difference (reduction) in kinetic frictional force between Case A and Case B in N."
    )
    ans_str = (
        f"1. FN,A = {_fmt_sa(fn_horiz, 1)} N; 2. FN,B = {_fmt_sa(fn_angled, 2)} N; "
        f"3. Difference = {_fmt_sa(delta_fk, 2)} N"
    )
    memo = (
        f"1. Case A: FN,A = mg = ({mass})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(fn_horiz, 1)} N [1]\n"
        f"2. Case B: Fy = F · sin({theta_deg}°) = ({f_pull}) · sin({theta_deg}°) = {_fmt_sa(fy, 2)} N\n"
        f"   FN,B = mg - Fy = {_fmt_sa(fn_horiz, 1)} - {_fmt_sa(fy, 2)} = {_fmt_sa(fn_angled, 2)} N [2]\n"
        f"3. fk,A = μk · FN,A = ({_fmt_sa(mu_k)})({_fmt_sa(fn_horiz, 1)}) = {_fmt_sa(fk_horiz, 2)} N\n"
        f"   fk,B = μk · FN,B = ({_fmt_sa(mu_k)})({_fmt_sa(fn_angled, 2)}) = {_fmt_sa(fk_angled, 2)} N\n"
        f"   Reduction Δfk = fk,A - fk,B = {_fmt_sa(delta_fk, 2)} N [2]"
    )
    hints = {
        "tier_1": "Upward vertical component of pull relieves some of the normal force, reducing friction.",
        "tier_2": "Calculate FN for both cases, then fk = mu_k * FN for each, and subtract.",
        "tier_3": f"FN,A = {_fmt_sa(fn_horiz, 1)} N, FN,B = {_fmt_sa(fn_angled, 2)} N, Δfk = {_fmt_sa(delta_fk, 2)} N.",
    }
    svg = (
        f'<svg viewBox="0 0 420 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<line x1="20" y1="140" x2="400" y2="140" stroke="#94a3b8" stroke-width="3"/><rect x="150" y="80" width="80" height="60" rx="4" fill="#e0e7ff" stroke="#3730a3" stroke-width="2"/>'
        f'<text x="190" y="115" text-anchor="middle" font-size="12" font-weight="bold" fill="#312e81">{mass} kg</text><text x="190" y="165" text-anchor="middle" font-size="11" fill="#64748b">Pull = {f_pull} N at {theta_deg}°</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 8,
        "mode": "38_friction_angled_pull_normal_force_reduction", "subskill": "38_friction_angled_pull_normal_force_reduction",
        "subskill_id": "38_friction_angled_pull_normal_force_reduction", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 5, "hints": hints,
        "misconception_tags": ["neglecting_upward_pull_component", "friction_independent_of_angle"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Normal force in horizontal case", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Normal force in angled case FN = mg - Fy", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Frictional reduction calculation", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 39. Friction — Angled Push Normal Force Increase Quantitative Comparison
# ==============================================================================
def builder_39(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_39_fric_push_inc", seed, idx)
    mass = rng.choice([15, 20, 25, 30])
    f_push = rng.choice([50, 70, 90, 110])
    theta_deg = rng.choice([25, 30, 35])
    mu_k = rng.choice([0.20, 0.25, 0.30])

    theta_rad = math.radians(theta_deg)
    fy = f_push * math.sin(theta_rad)
    fn_flat = mass * G_ACCEL
    fn_push = fn_flat + fy

    fk_flat = mu_k * fn_flat
    fk_push = mu_k * fn_push
    extra_fric = fk_push - fk_flat

    prompt = (
        f"A container of mass {mass} kg is pushed across a horizontal concrete floor (μk = {_fmt_sa(mu_k)}).\n\n"
        f"1. Calculate the normal force if the container were pushed strictly horizontally in N.\n"
        f"2. Calculate the normal force when a pushing force of {f_push} N is directed at {theta_deg}° below the horizontal in N.\n"
        f"3. Calculate the increase in kinetic frictional resistance caused by the downward pushing angle in N."
    )
    ans_str = (
        f"1. FN = {_fmt_sa(fn_flat, 1)} N; 2. FN = {_fmt_sa(fn_push, 2)} N; "
        f"3. Extra friction = {_fmt_sa(extra_fric, 2)} N"
    )
    memo = (
        f"1. Horizontal push: FN = mg = ({mass})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(fn_flat, 1)} N [1]\n"
        f"2. Downward push: Fy = F · sin({theta_deg}°) = ({f_push}) · sin({theta_deg}°) = {_fmt_sa(fy, 2)} N\n"
        f"   FN = mg + Fy = {_fmt_sa(fn_flat, 1)} + {_fmt_sa(fy, 2)} = {_fmt_sa(fn_push, 2)} N [2]\n"
        f"3. Δfk = μk · Fy = ({_fmt_sa(mu_k)})({_fmt_sa(fy, 2)}) = {_fmt_sa(extra_fric, 2)} N [2]"
    )
    hints = {
        "tier_1": "Pushing downwards increases the normal force by Fy = F*sin(theta).",
        "tier_2": "Extra friction equals mu_k * Fy.",
        "tier_3": f"FN,flat = {_fmt_sa(fn_flat, 1)} N, FN,push = {_fmt_sa(fn_push, 2)} N, Extra fk = {_fmt_sa(extra_fric, 2)} N.",
    }
    svg = (
        f'<svg viewBox="0 0 420 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<line x1="20" y1="140" x2="400" y2="140" stroke="#94a3b8" stroke-width="3"/><rect x="160" y="80" width="80" height="60" rx="4" fill="#fee2e2" stroke="#b91c1c" stroke-width="2"/>'
        f'<text x="200" y="115" text-anchor="middle" font-size="12" font-weight="bold" fill="#7f1d1d">{mass} kg</text><text x="200" y="165" text-anchor="middle" font-size="11" fill="#64748b">Push = {f_push} N at {theta_deg}° below horiz</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 8,
        "mode": "39_friction_angled_push_normal_force_increase", "subskill": "39_friction_angled_push_normal_force_increase",
        "subskill_id": "39_friction_angled_push_normal_force_increase", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 5, "hints": hints,
        "misconception_tags": ["push_reduces_normal_force_misconception"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Flat push normal force", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Angled push normal force FN = mg + Fy", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Extra friction calculation", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 40. Inclined Plane — Weight Components Parallel and Perpendicular
# ==============================================================================
def builder_40(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_40_incline_comp", seed, idx)
    mass = rng.choice([10, 15, 20, 25, 30, 45])
    theta_deg = rng.choice([20, 25, 30, 35, 40])

    theta_rad = math.radians(theta_deg)
    w = mass * G_ACCEL
    w_par = w * math.sin(theta_rad)
    w_perp = w * math.cos(theta_rad)

    prompt = (
        f"A cargo crate of mass {mass} kg rests on an inclined loading ramp inclined at {theta_deg}° to the horizontal.\n\n"
        f"1. Calculate the gravitational weight (w) of the crate in N.\n"
        f"2. Write down the formulas for the components of weight parallel (w∥) and perpendicular (w⊥) to the incline.\n"
        f"3. Calculate the magnitude of the parallel weight component (w∥) in N.\n"
        f"4. Calculate the magnitude of the perpendicular weight component (w⊥) in N."
    )
    ans_str = (
        f"1. w = {_fmt_sa(w, 1)} N; 2. w∥ = mg sin θ, w⊥ = mg cos θ; "
        f"3. w∥ = {_fmt_sa(w_par, 2)} N; 4. w⊥ = {_fmt_sa(w_perp, 2)} N"
    )
    memo = (
        f"1. w = mg = ({mass})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(w, 1)} N [1]\n"
        "2. w∥ = mg · sin(θ) [parallel / down the slope] [1]\n"
        "   w⊥ = mg · cos(θ) [perpendicular / into the slope] [1]\n"
        f"3. w∥ = ({mass})({_fmt_sa(G_ACCEL)}) · sin({theta_deg}°) = {_fmt_sa(w_par, 2)} N [1]\n"
        f"4. w⊥ = ({mass})({_fmt_sa(G_ACCEL)}) · cos({theta_deg}°) = {_fmt_sa(w_perp, 2)} N [1]"
    )
    hints = {
        "tier_1": "Parallel component uses sin(theta); perpendicular component uses cos(theta).",
        "tier_2": "w∥ = mg*sin(theta), w⊥ = mg*cos(theta).",
        "tier_3": f"w = {_fmt_sa(w, 1)} N, w∥ = {_fmt_sa(w_par, 2)} N, w⊥ = {_fmt_sa(w_perp, 2)} N.",
    }
    svg = (
        f'<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr40" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>'
        f'<polygon points="40,180 380,180 380,60" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>'
        f'<path d="M80,180 A40,40 0 0,0 75,165" fill="none" stroke="#0f172a" stroke-width="1.5"/><text x="95" y="174" font-size="11" fill="#0f172a">{theta_deg}°</text>'
        f'<rect x="180" y="90" width="50" height="35" rx="3" transform="rotate(-{theta_deg} 180 90)" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="220" y="80" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">{mass} kg</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 7,
        "mode": "40_inclined_plane_weight_components_parallel_perpendicular", "subskill": "40_inclined_plane_weight_components_parallel_perpendicular",
        "subskill_id": "40_inclined_plane_weight_components_parallel_perpendicular", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 5, "hints": hints,
        "misconception_tags": ["cos_sin_component_inversion", "normal_force_equals_total_weight_on_incline"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Total gravitational weight", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Component formulas identification", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Parallel component calculation", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Perpendicular component calculation", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 41. Inclined Plane — Sliding Down Frictionless (a = g sin θ)
# ==============================================================================
def builder_41(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_41_incline_fricless", seed, idx)
    mass = rng.choice([5, 8, 12, 18, 25])
    theta_deg = rng.choice([20, 30, 35, 45])
    theta_rad = math.radians(theta_deg)
    accel = round(G_ACCEL * math.sin(theta_rad), 2)

    prompt = (
        f"A block of mass {mass} kg is released from rest at the top of a smooth, frictionless ramp inclined at "
        f"{theta_deg}° to the horizontal.\n\n"
        f"1. Draw a labelled free-body diagram showing all forces acting on the sliding block.\n"
        f"2. Write down the net force equation along the incline.\n"
        f"3. Calculate the acceleration of the block down the frictionless ramp in m·s⁻².\n"
        f"4. State what happens to the acceleration if the block's mass is doubled."
    )
    ans_str = (
        f"1. Free-body diagram with FN (perpendicular to incline) and Fg (vertically downwards); "
        f"2. Fnet = mg sin θ = ma; 3. a = {_fmt_sa(accel)} m/s^2; 4. Acceleration remains unchanged"
    )
    memo = (
        "1. Free-body diagram: Normal force FN perpendicular to ramp; Gravitational force Fg (w) vertically downwards. [2]\n"
        f"2. Along the incline: Fnet = Fg∥ = mg · sin(θ) = ma [1]\n"
        f"3. a = g · sin(θ) = ({_fmt_sa(G_ACCEL)}) · sin({theta_deg}°) = {_fmt_sa(accel)} m·s⁻² [2]\n"
        "4. Mass cancels out in a = g · sin θ. Therefore, doubling the mass has no effect on the acceleration. [1]"
    )
    hints = {
        "tier_1": "On a frictionless incline, only the parallel component of gravity drives acceleration: a = g * sin(theta).",
        "tier_2": "Notice that mass m appears on both sides of mg*sin(theta) = ma and cancels out.",
        "tier_3": f"a = 9.8 * sin({theta_deg}°) = {_fmt_sa(accel)} m/s^2. Mass has no effect.",
    }
    svg = (
        f'<svg viewBox="0 0 440 220" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<polygon points="40,180 380,180 380,60" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>'
        f'<rect x="180" y="90" width="50" height="35" rx="3" transform="rotate(-{theta_deg} 180 90)" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="210" y="205" text-anchor="middle" font-size="11" fill="#475569">Smooth ramp inclined at {theta_deg}°</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 8,
        "mode": "41_inclined_plane_sliding_down_frictionless", "subskill": "41_inclined_plane_sliding_down_frictionless",
        "subskill_id": "41_inclined_plane_sliding_down_frictionless", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 6, "hints": hints,
        "misconception_tags": ["heavier_objects_accelerate_faster_down_slope", "normal_force_cancels_weight_directly"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Free-body diagram on incline", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Net force formula mg sin theta = ma", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Acceleration calculation", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Independence of mass deduction", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 42. Inclined Plane — Sliding Down with Kinetic Friction
# ==============================================================================
def builder_42(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_42_incline_kinetic", seed, idx)
    mass = rng.choice([10, 15, 20, 25, 30])
    theta_deg = rng.choice([25, 30, 35, 40])
    mu_k = rng.choice([0.15, 0.20, 0.25])

    theta_rad = math.radians(theta_deg)
    w = mass * G_ACCEL
    w_par = w * math.sin(theta_rad)
    w_perp = w * math.cos(theta_rad)
    fn = w_perp
    fk = mu_k * fn

    f_net = w_par - fk
    if f_net <= 0:
        mu_k = 0.10
        fk = mu_k * fn
        f_net = w_par - fk
    accel = f_net / mass

    prompt = (
        f"A wooden block of mass {mass} kg slides down a rough ramp inclined at {theta_deg}° to the horizontal. "
        f"The coefficient of kinetic friction between the block and the ramp is {_fmt_sa(mu_k)}.\n\n"
        f"1. Calculate the magnitude of the normal force (FN) exerted by the ramp on the block in N.\n"
        f"2. Calculate the magnitude of the kinetic frictional force (fk) acting on the block in N.\n"
        f"3. Calculate the net force (Fnet) parallel to the ramp in N.\n"
        f"4. Calculate the acceleration of the block down the ramp in m·s⁻²."
    )
    ans_str = (
        f"1. FN = {_fmt_sa(fn, 2)} N; 2. fk = {_fmt_sa(fk, 2)} N; "
        f"3. Fnet = {_fmt_sa(f_net, 2)} N down slope; 4. a = {_fmt_sa(accel, 2)} m/s^2 down slope"
    )
    memo = (
        f"1. Perpendicular balance: FN = Fg⊥ = mg · cos({theta_deg}°) = ({mass})({_fmt_sa(G_ACCEL)}) · cos({theta_deg}°) = {_fmt_sa(fn, 2)} N [1M, 1A]\n"
        f"2. fk = μk · FN = ({_fmt_sa(mu_k)})({_fmt_sa(fn, 2)}) = {_fmt_sa(fk, 2)} N [1M, 1A]\n"
        f"3. Fg∥ = mg · sin({theta_deg}°) = ({mass})({_fmt_sa(G_ACCEL)}) · sin({theta_deg}°) = {_fmt_sa(w_par, 2)} N\n"
        f"   Fnet = Fg∥ - fk = {_fmt_sa(w_par, 2)} - {_fmt_sa(fk, 2)} = {_fmt_sa(f_net, 2)} N down slope [1M, 1A]\n"
        f"4. a = Fnet / m = {_fmt_sa(f_net, 2)} / {mass} = {_fmt_sa(accel, 2)} m·s⁻² down slope [1A]"
    )
    hints = {
        "tier_1": "FN = mg*cos(theta). Kinetic friction fk = mu_k * FN acts up the slope.",
        "tier_2": "Fnet = mg*sin(theta) - fk. Acceleration a = Fnet / m.",
        "tier_3": f"FN = {_fmt_sa(fn, 2)} N, fk = {_fmt_sa(fk, 2)} N, a = {_fmt_sa(accel, 2)} m/s^2.",
    }
    svg = (
        f'<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<polygon points="40,180 380,180 380,60" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>'
        f'<rect x="180" y="90" width="50" height="35" rx="3" transform="rotate(-{theta_deg} 180 90)" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="210" y="205" text-anchor="middle" font-size="11" fill="#475569">Ramp angle = {theta_deg}°, μk = {_fmt_sa(mu_k)}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 9,
        "mode": "42_inclined_plane_sliding_down_with_kinetic_friction", "subskill": "42_inclined_plane_sliding_down_with_kinetic_friction",
        "subskill_id": "42_inclined_plane_sliding_down_with_kinetic_friction", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 7, "hints": hints,
        "misconception_tags": ["friction_direction_confusion_incline", "normal_force_calculation_error"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Normal force calculation FN = mg cos theta", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Kinetic friction calculation fk = mu_k * FN", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Net force Fnet = Fg|| - fk", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Acceleration a = Fnet/m", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 43. Inclined Plane — Pulled Uphill with Applied Force and Friction
# ==============================================================================
def builder_43(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_43_incline_pull_up", seed, idx)
    mass = rng.choice([15, 20, 25, 30, 40])
    theta_deg = rng.choice([20, 25, 30])
    mu_k = rng.choice([0.15, 0.20, 0.25])

    theta_rad = math.radians(theta_deg)
    w = mass * G_ACCEL
    w_par = w * math.sin(theta_rad)
    w_perp = w * math.cos(theta_rad)
    fn = w_perp
    fk = mu_k * fn

    opposing = w_par + fk
    f_app = round(opposing + mass * rng.choice([1.0, 1.5, 2.0]), 1)
    f_net = f_app - opposing
    accel = f_net / mass

    prompt = (
        f"A crate of mass {mass} kg is pulled up a rough inclined plane (incline angle = {theta_deg}°, μk = {_fmt_sa(mu_k)}) "
        f"by a cable applying a constant tension force of {_fmt_sa(f_app)} N parallel to the slope.\n\n"
        f"1. Draw a labelled free-body diagram showing all four forces acting on the crate.\n"
        f"2. Calculate the total downward resistive force acting parallel to the slope (Fg∥ + fk) in N.\n"
        f"3. Calculate the net force acting on the crate parallel to the slope in N.\n"
        f"4. Calculate the uphill acceleration of the crate in m·s⁻²."
    )
    ans_str = (
        f"1. FBD with Fapp (uphill), Fg (down), FN (perpendicular), fk (downhill); "
        f"2. Opposing = {_fmt_sa(opposing, 2)} N; 3. Fnet = {_fmt_sa(f_net, 2)} N; 4. a = {_fmt_sa(accel, 2)} m/s^2"
    )
    memo = (
        "1. Free-body diagram: Fapplied up the slope; fk down the slope; Fg∥ (w∥) down the slope; FN perpendicular to slope. [2]\n"
        f"2. Fg∥ = mg · sin({theta_deg}°) = ({mass})({_fmt_sa(G_ACCEL)}) · sin({theta_deg}°) = {_fmt_sa(w_par, 2)} N\n"
        f"   FN = mg · cos({theta_deg}°) = {_fmt_sa(fn, 2)} N\n"
        f"   fk = μk · FN = ({_fmt_sa(mu_k)})({_fmt_sa(fn, 2)}) = {_fmt_sa(fk, 2)} N\n"
        f"   Total resistive force = Fg∥ + fk = {_fmt_sa(w_par, 2)} + {_fmt_sa(fk, 2)} = {_fmt_sa(opposing, 2)} N [2]\n"
        f"3. Fnet = Fapplied - (Fg∥ + fk) = {_fmt_sa(f_app)} - {_fmt_sa(opposing, 2)} = {_fmt_sa(f_net, 2)} N [1]\n"
        f"4. a = Fnet / m = {_fmt_sa(f_net, 2)} / {mass} = {_fmt_sa(accel, 2)} m·s⁻² uphill [2]"
    )
    hints = {
        "tier_1": "When moving uphill, both gravity parallel component AND friction act DOWNHILL against motion.",
        "tier_2": "Fnet = F_app - (mg*sin(theta) + fk).",
        "tier_3": f"Opposing = {_fmt_sa(opposing, 2)} N, a = ({_fmt_sa(f_app)} - {_fmt_sa(opposing, 2)}) / {mass} = {_fmt_sa(accel, 2)} m/s^2.",
    }
    svg = (
        f'<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr43" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>'
        f'<polygon points="40,180 380,180 380,60" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>'
        f'<rect x="180" y="90" width="50" height="35" rx="3" transform="rotate(-{theta_deg} 180 90)" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/>'
        f'<line x1="220" y1="85" x2="310" y2="40" stroke="#2563eb" stroke-width="3" marker-end="url(#arr43)"/><text x="270" y="45" font-size="11" font-weight="bold" fill="#2563eb">Fapplied = {_fmt_sa(f_app)} N</text>'
        f'<text x="210" y="205" text-anchor="middle" font-size="11" fill="#475569">Incline = {theta_deg}°, Mass = {mass} kg</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 10,
        "mode": "43_inclined_plane_pulled_up_with_applied_force_and_friction", "subskill": "43_inclined_plane_pulled_up_with_applied_force_and_friction",
        "subskill_id": "43_inclined_plane_pulled_up_with_applied_force_and_friction", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 7, "hints": hints,
        "misconception_tags": ["subtracted_friction_from_gravity_instead_of_adding", "fbd_omitted_friction_or_gravity"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Free-body diagram", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Sum of opposing downhill forces (Fg|| + fk)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Net force calculation", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Acceleration calculation", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 44. Inclined Plane — Static Friction and Impending Motion (Slip Angle)
# ==============================================================================
def builder_44(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_44_incline_slip", seed, idx)
    mass = rng.choice([10, 15, 20, 25])
    mu_s = rng.choice([0.40, 0.45, 0.50, 0.55, 0.60])
    theta_c_deg = round(math.degrees(math.atan(mu_s)), 1)
    is_rest = rng.choice([True, False])
    if is_rest:
        test_theta = max(15, round(theta_c_deg - 5))
    else:
        test_theta = min(45, round(theta_c_deg + 5))

    test_rad = math.radians(test_theta)
    w_par = mass * G_ACCEL * math.sin(test_rad)
    fn = mass * G_ACCEL * math.cos(test_rad)
    fs_max = mu_s * fn

    prompt = (
        f"A block of mass {mass} kg rests on an inclined ramp whose angle of inclination can be adjusted. "
        f"The coefficient of static friction between the block and the ramp is {_fmt_sa(mu_s)}.\n\n"
        f"1. Derive the mathematical relationship between the coefficient of static friction (μs) and the critical "
        f"slip angle (θc) at impending motion.\n"
        f"2. Calculate the critical angle (θc) in degrees.\n"
        f"3. If the ramp is set to {test_theta}°, determine whether the block remains at rest or begins to slip."
    )
    if test_theta <= theta_c_deg:
        ans_str = (
            f"1. tan θc = μs; 2. θc = {_fmt_sa(theta_c_deg)}°; "
            f"3. Remains at rest because {test_theta}° <= {_fmt_sa(theta_c_deg)}°"
        )
        verdict = f"Since {test_theta}° <= {_fmt_sa(theta_c_deg)}° (w∥ = {_fmt_sa(w_par, 1)} N <= fs^max = {_fmt_sa(fs_max, 1)} N), the block remains at rest. [2]"
    else:
        ans_str = (
            f"1. tan θc = μs; 2. θc = {_fmt_sa(theta_c_deg)}°; "
            f"3. Begins to slip because {test_theta}° > {_fmt_sa(theta_c_deg)}°"
        )
        verdict = f"Since {test_theta}° > {_fmt_sa(theta_c_deg)}° (w∥ = {_fmt_sa(w_par, 1)} N > fs^max = {_fmt_sa(fs_max, 1)} N), the block begins to slip. [2]"

    memo = (
        "1. At impending motion down the slope: Fg∥ = fs^max => mg · sin θc = μs · mg · cos θc [1]\n"
        "   Dividing by mg · cos θc gives: sin θc / cos θc = tan θc = μs [1]\n"
        f"2. θc = arctan(μs) = arctan({_fmt_sa(mu_s)}) = {_fmt_sa(theta_c_deg)}° [2]\n"
        f"3. {verdict}"
    )
    hints = {
        "tier_1": "At impending motion, parallel gravity component equals maximum static friction.",
        "tier_2": "tan(theta_c) = mu_s. Solve for theta_c = arctan(mu_s).",
        "tier_3": f"theta_c = arctan({_fmt_sa(mu_s)}) = {_fmt_sa(theta_c_deg)}°. Compare {test_theta}° to {_fmt_sa(theta_c_deg)}°.",
    }
    svg = (
        f'<svg viewBox="0 0 450 200" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<polygon points="40,160 380,160 380,50" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>'
        f'<text x="210" y="185" text-anchor="middle" font-size="11" fill="#475569">μs = {_fmt_sa(mu_s)}, critical angle θc = arctan(μs)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 8,
        "mode": "44_inclined_plane_static_friction_impending_motion", "subskill": "44_inclined_plane_static_friction_impending_motion",
        "subskill_id": "44_inclined_plane_static_friction_impending_motion", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 6, "hints": hints,
        "misconception_tags": ["tan_theta_inversion_confusion", "mass_dependence_misconception_incline_slip"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Derivation of tan theta_c = mu_s", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Critical angle calculation", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Motion determination at specified angle", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 45. Connected Masses — Horizontal Frictionless Surface (Tension & Accel)
# ==============================================================================
def builder_45(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_45_conn_fricless", seed, idx)
    m1 = rng.choice([3, 4, 5, 6])
    m2 = rng.choice([6, 8, 10, 12])
    m_tot = m1 + m2
    f_pull = rng.choice([30, 45, 60, 75, 90])

    accel = round(f_pull / m_tot, 2)
    f_pull = round(m_tot * accel, 1)
    tension = round(m1 * accel, 2)

    prompt = (
        f"Two blocks A (mass {m1} kg) and B (mass {m2} kg) are connected by a light, inextensible string on a "
        f"frictionless horizontal tabletop. A constant pulling force of {_fmt_sa(f_pull)} N is applied horizontally to block B to the right.\n\n"
        f"1. Treat the two blocks as a single system to calculate the acceleration of the system in m·s⁻².\n"
        f"2. Draw a free-body diagram for block A alone.\n"
        f"3. Calculate the tension (T) in the connecting string in N."
    )
    ans_str = (
        f"1. a = {_fmt_sa(accel)} m/s^2; 2. FBD for block A with T (right), FN (up), Fg (down); "
        f"3. T = {_fmt_sa(tension)} N"
    )
    memo = (
        f"1. System approach: Fnet = (mA + mB) · a\n"
        f"   {_fmt_sa(f_pull)} = ({m1} + {m2}) · a = {m_tot} · a\n"
        f"   a = {_fmt_sa(f_pull)} / {m_tot} = {_fmt_sa(accel)} m·s⁻² [2]\n"
        "2. Block A alone: Normal force upward, Weight downward, Tension T to the right. [2]\n"
        f"3. For block A: Fnet = T = mA · a = ({m1})({_fmt_sa(accel)}) = {_fmt_sa(tension)} N [2]"
    )
    hints = {
        "tier_1": "Find system acceleration first: a = F_pull / (m1 + m2).",
        "tier_2": "The only horizontal force pulling the rear block m1 is the string tension T = m1 * a.",
        "tier_3": f"a = {_fmt_sa(f_pull)} / {m_tot} = {_fmt_sa(accel)} m/s^2. T = {m1} * {_fmt_sa(accel)} = {_fmt_sa(tension)} N.",
    }
    svg = (
        f'<svg viewBox="0 0 460 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr45" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>'
        f'<line x1="20" y1="140" x2="440" y2="140" stroke="#94a3b8" stroke-width="3"/><rect x="80" y="80" width="70" height="60" rx="4" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="115" y="115" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">A ({m1} kg)</text><line x1="150" y1="110" x2="230" y2="110" stroke="#0f172a" stroke-width="3"/><text x="190" y="100" text-anchor="middle" font-size="11" fill="#0f172a">T</text>'
        f'<rect x="230" y="70" width="80" height="70" rx="4" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/><text x="270" y="110" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">B ({m2} kg)</text>'
        f'<line x1="310" y1="105" x2="410" y2="105" stroke="#2563eb" stroke-width="3" marker-end="url(#arr45)"/><text x="360" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">F = {_fmt_sa(f_pull)} N</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 8,
        "mode": "45_connected_masses_horizontal_surface_tension", "subskill": "45_connected_masses_horizontal_surface_tension",
        "subskill_id": "45_connected_masses_horizontal_surface_tension", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 6, "hints": hints,
        "misconception_tags": ["tension_equals_full_applied_force", "individual_block_mass_error"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "System acceleration calculation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Free-body diagram for block A", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Tension calculation T = mA * a", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 46. Connected Masses — Horizontal Surface with Friction
# ==============================================================================
def builder_46(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_46_conn_fric", seed, idx)
    m1 = rng.choice([4, 5, 6, 8])
    m2 = rng.choice([6, 8, 10, 12])
    mu_k = rng.choice([0.15, 0.20, 0.25])

    fn1 = m1 * G_ACCEL
    fn2 = m2 * G_ACCEL
    fk1 = round(mu_k * fn1, 2)
    fk2 = round(mu_k * fn2, 2)
    fk_tot = round(fk1 + fk2, 2)

    m_tot = m1 + m2
    a_target = rng.choice([1.2, 1.5, 2.0])
    f_pull = round(fk_tot + m_tot * a_target, 1)

    f_net = round(f_pull - fk_tot, 2)
    accel = round(f_net / m_tot, 2)
    tension = round(fk1 + m1 * accel, 2)

    prompt = (
        f"Two crates A (mass {m1} kg) and B (mass {m2} kg) on a rough horizontal warehouse floor (μk = {_fmt_sa(mu_k)}) "
        f"are connected by a light taut cord. A horizontal force of {_fmt_sa(f_pull)} N pulls crate B to the right.\n\n"
        f"1. Calculate the frictional forces fk,A and fk,B acting on each crate in N.\n"
        f"2. Write down Newton's Second Law equations of motion for crate A and crate B separately.\n"
        f"3. Calculate the acceleration of the system in m·s⁻².\n"
        f"4. Calculate the tension (T) in the cord connecting the two crates in N."
    )
    ans_str = (
        f"1. fk,A = {_fmt_sa(fk1)} N, fk,B = {_fmt_sa(fk2)} N; "
        f"2. A: T - fk,A = mA*a; B: Fpull - T - fk,B = mB*a; "
        f"3. a = {_fmt_sa(accel)} m/s^2; 4. T = {_fmt_sa(tension)} N"
    )
    memo = (
        f"1. fk,A = μk · mA · g = ({_fmt_sa(mu_k)})({m1})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(fk1)} N [1]\n"
        f"   fk,B = μk · mB · g = ({_fmt_sa(mu_k)})({m2})({_fmt_sa(G_ACCEL)}) = {_fmt_sa(fk2)} N [1]\n"
        f"2. For crate A: T - fk,A = mA · a => T - {_fmt_sa(fk1)} = {m1}a (Eq 1) [1]\n"
        f"   For crate B: Fpull - T - fk,B = mB · a => {_fmt_sa(f_pull)} - T - {_fmt_sa(fk2)} = {m2}a (Eq 2) [1]\n"
        f"3. Adding Eq 1 and Eq 2: {_fmt_sa(f_pull)} - ({_fmt_sa(fk1)} + {_fmt_sa(fk2)}) = ({m1} + {m2})a\n"
        f"   {_fmt_sa(f_net)} = {m_tot}a => a = {_fmt_sa(f_net)} / {m_tot} = {_fmt_sa(accel)} m·s⁻² [2]\n"
        f"4. From Eq 1: T = {_fmt_sa(fk1)} + ({m1})({_fmt_sa(accel)}) = {_fmt_sa(tension)} N [2]"
    )
    hints = {
        "tier_1": "Calculate friction on each crate first: fk = mu_k * mg.",
        "tier_2": "Add the two equations of motion to eliminate T and solve for a: F_pull - fk1 - fk2 = (m1 + m2)*a.",
        "tier_3": f"a = {_fmt_sa(accel)} m/s^2, T = {_fmt_sa(tension)} N.",
    }
    svg = (
        f'<svg viewBox="0 0 460 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr46" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>'
        f'<line x1="20" y1="140" x2="440" y2="140" stroke="#94a3b8" stroke-width="3"/><rect x="80" y="80" width="70" height="60" rx="4" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="115" y="115" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">A ({m1} kg)</text><line x1="150" y1="110" x2="230" y2="110" stroke="#0f172a" stroke-width="3"/><text x="190" y="100" text-anchor="middle" font-size="11" fill="#0f172a">T</text>'
        f'<rect x="230" y="70" width="80" height="70" rx="4" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/><text x="270" y="110" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">B ({m2} kg)</text>'
        f'<line x1="310" y1="105" x2="410" y2="105" stroke="#2563eb" stroke-width="3" marker-end="url(#arr46)"/><text x="360" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">F = {_fmt_sa(f_pull)} N</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 10,
        "mode": "46_connected_masses_horizontal_with_friction", "subskill": "46_connected_masses_horizontal_with_friction",
        "subskill_id": "46_connected_masses_horizontal_with_friction", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 8, "hints": hints,
        "misconception_tags": ["omitted_friction_on_trailing_mass", "simultaneous_equation_sign_error"],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_1", "desc": "Friction calculations on both crates", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Separate equations of motion", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Acceleration calculation", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Tension calculation", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 47. Connected Masses — Inclined Plane Tension and Acceleration
# ==============================================================================
def builder_47(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_47_conn_incline", seed, idx)
    m1 = rng.choice([4, 5, 6])
    m2 = rng.choice([8, 10, 12])
    theta_deg = rng.choice([20, 25, 30])
    theta_rad = math.radians(theta_deg)

    g_par = G_ACCEL * math.sin(theta_rad)
    m_tot = m1 + m2
    f_pull = round(m_tot * g_par + m_tot * rng.choice([1.0, 1.5, 2.0]), 1)

    f_net = f_pull - m_tot * g_par
    accel = round(f_net / m_tot, 2)
    tension = round(m1 * g_par + m1 * accel, 2)

    prompt = (
        f"Two blocks A (mass {m1} kg) and B (mass {m2} kg) connected by a light string rest on a frictionless "
        f"incline inclined at {theta_deg}° to the horizontal. A pulling force of {_fmt_sa(f_pull)} N parallel to the incline "
        f"pulls block B uphill.\n\n"
        f"1. Calculate the total component of gravitational force acting down the slope for the entire system (mA + mB) in N.\n"
        f"2. Calculate the acceleration of the two blocks up the slope in m·s⁻².\n"
        f"3. Calculate the tension (T) in the string connecting block A and block B in N."
    )
    ans_str = (
        f"1. Fg∥,tot = {_fmt_sa(m_tot * g_par, 2)} N; 2. a = {_fmt_sa(accel)} m/s^2; "
        f"3. T = {_fmt_sa(tension)} N"
    )
    memo = (
        f"1. Total parallel gravity: Fg∥,tot = (mA + mB) · g · sin({theta_deg}°) = ({m_tot})({_fmt_sa(G_ACCEL)}) · sin({theta_deg}°) = {_fmt_sa(m_tot * g_par, 2)} N [2]\n"
        f"2. System equation: Fnet = Fpull - Fg∥,tot = {_fmt_sa(f_pull)} - {_fmt_sa(m_tot * g_par, 2)} = {_fmt_sa(f_net, 2)} N\n"
        f"   a = Fnet / (mA + mB) = {_fmt_sa(f_net, 2)} / {m_tot} = {_fmt_sa(accel)} m·s⁻² uphill [2]\n"
        f"3. For block A: T - mA · g · sin({theta_deg}°) = mA · a\n"
        f"   T = ({m1})({_fmt_sa(G_ACCEL)} · sin({theta_deg}°)) + ({m1})({_fmt_sa(accel)}) = {_fmt_sa(tension)} N [2]"
    )
    hints = {
        "tier_1": "System net force uphill = F_pull - (m1 + m2)*g*sin(theta).",
        "tier_2": "For block A: T - m1*g*sin(theta) = m1*a.",
        "tier_3": f"a = {_fmt_sa(accel)} m/s^2, T = {_fmt_sa(tension)} N.",
    }
    svg = (
        f'<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<polygon points="40,180 380,180 380,60" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>'
        f'<rect x="140" y="110" width="45" height="30" rx="3" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/><text x="162" y="129" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">A ({m1}kg)</text>'
        f'<line x1="185" y1="125" x2="235" y2="105" stroke="#0f172a" stroke-width="2"/><text x="210" y="110" text-anchor="middle" font-size="10" fill="#0f172a">T</text>'
        f'<rect x="235" y="85" width="55" height="35" rx="3" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/><text x="262" y="106" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">B ({m2}kg)</text>'
        f'<line x1="290" y1="100" x2="360" y2="70" stroke="#2563eb" stroke-width="3"/><text x="340" y="65" font-size="11" font-weight="bold" fill="#2563eb">F={_fmt_sa(f_pull)}N</text>'
        f'<text x="210" y="205" text-anchor="middle" font-size="11" fill="#475569">Ramp angle = {theta_deg}°, total mass = {m_tot} kg</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 9,
        "mode": "47_connected_masses_inclined_plane_tension_acceleration", "subskill": "47_connected_masses_inclined_plane_tension_acceleration",
        "subskill_id": "47_connected_masses_inclined_plane_tension_acceleration", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "free_body_diagram", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 6, "hints": hints,
        "misconception_tags": ["incline_connected_mass_parallel_gravity_error"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Total parallel gravity calculation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Acceleration calculation", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Tension calculation for trailing block", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 48. Half-Atwood Pulley System — Horizontal Table and Hanging Mass
# ==============================================================================
def builder_48(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_48_half_atwood", seed, idx)
    m1 = rng.choice([4, 6, 8, 10])  # on table
    m2 = rng.choice([2, 3, 4, 5])   # hanging
    mu_k = rng.choice([0.10, 0.15, 0.20])

    fn1 = m1 * G_ACCEL
    fk1 = round(mu_k * fn1, 2)
    w2 = round(m2 * G_ACCEL, 2)

    if w2 <= fk1:
        m2 = m1
        w2 = round(m2 * G_ACCEL, 2)

    f_net = round(w2 - fk1, 2)
    m_tot = m1 + m2
    accel = round(f_net / m_tot, 2)
    tension = round(w2 - m2 * accel, 2)

    prompt = (
        f"A block A of mass {m1} kg rests on a rough horizontal table (μk = {_fmt_sa(mu_k)}). A light inextensible cord "
        f"attached to block A passes over a light frictionless pulley at the edge of the table and supports a hanging "
        f"mass B of {m2} kg.\n\n"
        f"1. Draw separate labelled free-body diagrams for block A and hanging mass B.\n"
        f"2. Write down Newton's Second Law equations of motion for block A and mass B separately.\n"
        f"3. Calculate the acceleration of the system in m·s⁻².\n"
        f"4. Calculate the tension (T) in the cord in N."
    )
    ans_str = (
        f"1. FBDs for A and B; 2. A: T - fk = mA*a; B: mB*g - T = mB*a; "
        f"3. a = {_fmt_sa(accel)} m/s^2; 4. T = {_fmt_sa(tension)} N"
    )
    memo = (
        "1. Block A: Normal force (up), Weight FgA (down), Tension T (right), Friction fk (left). [2]\n"
        "   Mass B: Tension T (up), Weight FgB (down). [1]\n"
        f"2. Block A: T - fk = mA · a => T - {_fmt_sa(fk1)} = {m1}a (Eq 1) [1]\n"
        f"   Mass B: FgB - T = mB · a => {_fmt_sa(w2)} - T = {m2}a (Eq 2) [1]\n"
        f"3. Adding Eq 1 and Eq 2: {_fmt_sa(w2)} - {_fmt_sa(fk1)} = ({m1} + {m2})a\n"
        f"   {_fmt_sa(f_net)} = {m_tot}a => a = {_fmt_sa(f_net)} / {m_tot} = {_fmt_sa(accel)} m·s⁻² [2]\n"
        f"4. From Eq 2: T = {_fmt_sa(w2)} - ({m2})({_fmt_sa(accel)}) = {_fmt_sa(tension)} N [1]"
    )
    hints = {
        "tier_1": "The driving force is the weight of the hanging mass: F_drive = m2 * g.",
        "tier_2": "System equation: m2*g - fk1 = (m1 + m2)*a.",
        "tier_3": f"a = ({_fmt_sa(w2)} - {_fmt_sa(fk1)}) / {m_tot} = {_fmt_sa(accel)} m/s^2. T = {_fmt_sa(tension)} N.",
    }
    svg = (
        f'<svg viewBox="0 0 440 220" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="80" width="280" height="120" fill="#e2e8f0" stroke="#475569" stroke-width="2"/><circle cx="300" cy="80" r="16" fill="#cbd5e1" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="120" y="40" width="60" height="40" rx="3" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/><text x="150" y="65" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">A ({m1} kg)</text>'
        f'<line x1="180" y1="60" x2="300" y2="60" stroke="#0f172a" stroke-width="2"/><line x1="316" y1="80" x2="316" y2="150" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="296" y="150" width="40" height="40" rx="3" fill="#fee2e2" stroke="#b91c1c" stroke-width="2"/><text x="316" y="175" text-anchor="middle" font-size="10" font-weight="bold" fill="#7f1d1d">B ({m2} kg)</text>'
        f'<text x="150" y="140" text-anchor="middle" font-size="11" fill="#475569">Horizontal Table (μk = {_fmt_sa(mu_k)})</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 10,
        "mode": "48_half_atwood_pulley_system_horizontal_and_hanging_mass", "subskill": "48_half_atwood_pulley_system_horizontal_and_hanging_mass",
        "subskill_id": "48_half_atwood_pulley_system_horizontal_and_hanging_mass", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "pulley_system", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 8, "hints": hints,
        "misconception_tags": ["tension_equals_hanging_weight_in_accelerating_system", "forgot_friction_on_table_mass"],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_1", "desc": "Free-body diagrams for both masses", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Coupled equations of motion", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "System acceleration calculation", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Tension calculation", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 49. Newton's Third Law — Action-Reaction Pairs and Distinctions
# ==============================================================================
def builder_49(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_49_newt3_pairs", seed, idx)
    m_skater1 = rng.choice([40, 50, 60])
    m_skater2 = rng.choice([70, 80, 90])
    f_push = rng.choice([120, 150, 180, 200])

    a1 = round(f_push / m_skater1, 2)
    a2 = round(f_push / m_skater2, 2)

    prompt = (
        f"Two ice skaters, Skater 1 (mass {m_skater1} kg) and Skater 2 (mass {m_skater2} kg), stand facing each other "
        f"on frictionless ice. Skater 1 pushes Skater 2 with a force of {f_push} N to the east.\n\n"
        f"1. State Newton's Third Law of Motion in words.\n"
        f"2. Identify the magnitude and direction of the force exerted by Skater 2 on Skater 1.\n"
        f"3. Calculate the acceleration of Skater 1 and Skater 2 immediately during the push.\n"
        f"4. State three essential properties of an action-reaction pair of forces."
    )
    ans_str = (
        f"1. When object A exerts a force on object B, object B simultaneously exerts an oppositely directed force of equal magnitude on object A; "
        f"2. {f_push} N to the west; 3. a1 = {_fmt_sa(a1)} m/s^2 west, a2 = {_fmt_sa(a2)} m/s^2 east; "
        f"4. Equal magnitude, opposite direction, act on different bodies (same nature/type)"
    )
    memo = (
        "1. Newton's Third Law: When one body exerts a force on a second body, the second body simultaneously exerts a "
        "force equal in magnitude and opposite in direction on the first body. [2]\n"
        f"2. By Newton's Third Law: Force on Skater 1 = {f_push} N to the west (opposite direction). [1]\n"
        f"3. a₁ = F / m₁ = {f_push} / {m_skater1} = {_fmt_sa(a1)} m·s⁻² to the west [1]\n"
        f"   a₂ = F / m₂ = {f_push} / {m_skater2} = {_fmt_sa(a2)} m·s⁻² to the east [1]\n"
        "4. Properties of Newton III pairs: (i) Equal in magnitude, (ii) Opposite in direction, "
        "(iii) Act on two different interacting bodies, (iv) Same type/nature of force. (Any three) [2]"
    )
    hints = {
        "tier_1": "Forces between interacting objects are always equal in magnitude and opposite in direction.",
        "tier_2": "Even though forces are equal, accelerations differ because a = F / m and their masses differ.",
        "tier_3": f"F_on_1 = {f_push} N west. a1 = {_fmt_sa(a1)} m/s^2, a2 = {_fmt_sa(a2)} m/s^2.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr49w" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#dc2626"/></marker>'
        f'<marker id="arr49e" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>'
        f'<line x1="20" y1="140" x2="420" y2="140" stroke="#94a3b8" stroke-width="3"/><circle cx="170" cy="90" r="16" fill="#fca5a5" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="170" y="95" text-anchor="middle" font-size="11" font-weight="bold" fill="#7f1d1d">1</text><circle cx="270" cy="90" r="16" fill="#93c5fd" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="270" y="95" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">2</text><line x1="170" y1="65" x2="70" y2="65" stroke="#dc2626" stroke-width="3" marker-end="url(#arr49w)"/>'
        f'<text x="120" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="#dc2626">F2on1 = {f_push} N</text><line x1="270" y1="65" x2="370" y2="65" stroke="#2563eb" stroke-width="3" marker-end="url(#arr49e)"/>'
        f'<text x="320" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">F1on2 = {f_push} N</text><text x="220" y="165" text-anchor="middle" font-size="11" fill="#475569">m1 = {m_skater1} kg, m2 = {m_skater2} kg on frictionless ice</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 7,
        "mode": "49_newtons_third_law_action_reaction_pairs", "subskill": "49_newtons_third_law_action_reaction_pairs",
        "subskill_id": "49_newtons_third_law_action_reaction_pairs", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "vector_cartesian", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 7, "hints": hints,
        "misconception_tags": ["heavier_object_feels_smaller_force", "action_reaction_pairs_cancel_each_other"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Newton's Third Law verbatim statement", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Reaction force magnitude and direction", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Accelerations of both bodies", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Properties of action-reaction pairs", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 50. Newton's Universal Gravitation — Law and Ratio Scaling
# ==============================================================================
def builder_50(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("newt11_50_gravitation", seed, idx)
    m_factor = rng.choice([2, 3, 4])
    r_factor = rng.choice([2, 3, 4])
    ratio_num = m_factor
    ratio_den = r_factor ** 2
    g_earth = 9.8
    g_new = round(g_earth * ratio_num / ratio_den, 2)

    prompt = (
        f"A hypothetical exoplanet has {m_factor} times the mass of the Earth (M_planet = {m_factor}·M_Earth) "
        f"and {r_factor} times the radius of the Earth (R_planet = {r_factor}·R_Earth).\n\n"
        f"1. State Newton's Law of Universal Gravitation in words.\n"
        f"2. Write down the mathematical formula for the gravitational acceleration (g) at the surface of a spherical planet of mass M and radius R.\n"
        f"3. Use ratio and proportionality reasoning to determine the gravitational acceleration on the surface of the exoplanet in terms of g_Earth.\n"
        f"4. Taking g_Earth = 9,8 m·s⁻², calculate the numerical value of gravitational acceleration on the exoplanet in m·s⁻²."
    )
    ans_str = (
        f"1. Every particle in the universe attracts every other particle with a gravitational force that is directly "
        f"proportional to the product of their masses and inversely proportional to the square of the distance between their centres; "
        f"2. g = G*M / R^2; 3. g_planet = ({ratio_num}/{ratio_den}) g_Earth; 4. {_fmt_sa(g_new)} m/s^2"
    )
    memo = (
        "1. Newton's Law of Universal Gravitation: Each particle in the universe attracts every other particle with a gravitational "
        "force that is directly proportional to the product of their masses and inversely proportional to the square of the distance "
        "between their centres. [2]\n"
        "2. g = G · M / R² [1]\n"
        f"3. g_planet = G · ({m_factor} M_Earth) / ({r_factor} R_Earth)² = G · ({m_factor} M_Earth) / ({ratio_den} R_Earth²)\n"
        f"   g_planet = ({ratio_num}/{ratio_den}) · (G · M_Earth / R_Earth²) = ({ratio_num}/{ratio_den}) · g_Earth [2]\n"
        f"4. g_planet = ({ratio_num}/{ratio_den}) · ({_fmt_sa(g_earth)}) = {_fmt_sa(g_new)} m·s⁻² [2]"
    )
    hints = {
        "tier_1": "Recall g = G*M / R^2. Substitute M' = m_factor*M and R' = r_factor*R.",
        "tier_2": "Remember that the denominator is squared: (r_factor*R)^2 = r_factor^2 * R^2.",
        "tier_3": f"g_planet = ({ratio_num}/{ratio_den}) * 9.8 = {_fmt_sa(g_new)} m/s^2.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<defs><marker id="arr50l" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker>'
        f'<marker id="arr50r" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2563eb"/></marker></defs>'
        f'<circle cx="100" cy="90" r="35" fill="#93c5fd" stroke="#1d4ed8" stroke-width="2"/><text x="100" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">M = {m_factor}·M_E</text>'
        f'<circle cx="340" cy="90" r="25" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/><text x="340" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="#7c2d12">R = {r_factor}·R_E</text>'
        f'<line x1="100" y1="90" x2="340" y2="90" stroke="#94a3b8" stroke-dasharray="4,4"/><line x1="135" y1="90" x2="200" y2="90" stroke="#2563eb" stroke-width="3" marker-end="url(#arr50l)"/>'
        f'<line x1="315" y1="90" x2="250" y2="90" stroke="#2563eb" stroke-width="3" marker-end="url(#arr50r)"/><text x="220" y="125" text-anchor="middle" font-size="12" fill="#0f172a">r (distance between centres)</text>'
        f'<text x="220" y="165" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">g_planet = {_fmt_sa(g_new)} m/s² ({ratio_num}/{ratio_den} g_E)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 2, "caps_weight_percent": 18, "suggested_duration_mins": 8,
        "mode": "50_newtons_universal_gravitation_law_and_ratio_scaling", "subskill": "50_newtons_universal_gravitation_law_and_ratio_scaling",
        "subskill_id": "50_newtons_universal_gravitation_law_and_ratio_scaling", "topic": "grade11_vectors_newton",
        "question_type": "short_answer", "modality": "vector_cartesian", "diagram_spec": _svg_spec(svg),
        "question": prompt, "question_text": prompt, "correct_answer": ans_str, "sample_answer": ans_str,
        "worked_solution": memo, "explanation": memo, "marks": 7, "hints": hints,
        "misconception_tags": ["forgot_to_square_radius_ratio", "confusing_G_constant_with_g_acceleration"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Newton's Law of Universal Gravitation verbatim statement", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Formula g = G*M/R^2", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Ratio derivation with squared radius factor", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Numerical value calculation", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


BUILDERS_26_50: Dict[str, Any] = {
    "26_newtons_first_law_inertia_and_definition": builder_26,
    "27_newtons_first_law_balanced_forces_equilibrium": builder_27,
    "28_newtons_first_law_constant_velocity_motion": builder_28,
    "29_newtons_first_law_seatbelt_safety_application": builder_29,
    "30_newtons_second_law_formula_fnet_equals_ma": builder_30,
    "31_newtons_second_law_horizontal_accelerating_crate": builder_31,
    "32_newtons_second_law_angled_pulling_force": builder_32,
    "33_newtons_second_law_angled_pushing_force": builder_33,
    "34_newtons_second_law_vertical_motion_rocket_elevator": builder_34,
    "35_newtons_second_law_apparent_weight_scale_in_elevator": builder_35,
    "36_static_friction_maximum_coefficient": builder_36,
    "37_kinetic_friction_constant_velocity_or_acceleration": builder_37,
    "38_friction_angled_pull_normal_force_reduction": builder_38,
    "39_friction_angled_push_normal_force_increase": builder_39,
    "40_inclined_plane_weight_components_parallel_perpendicular": builder_40,
    "41_inclined_plane_sliding_down_frictionless": builder_41,
    "42_inclined_plane_sliding_down_with_kinetic_friction": builder_42,
    "43_inclined_plane_pulled_up_with_applied_force_and_friction": builder_43,
    "44_inclined_plane_static_friction_impending_motion": builder_44,
    "45_connected_masses_horizontal_surface_tension": builder_45,
    "46_connected_masses_horizontal_with_friction": builder_46,
    "47_connected_masses_inclined_plane_tension_acceleration": builder_47,
    "48_half_atwood_pulley_system_horizontal_and_hanging_mass": builder_48,
    "49_newtons_third_law_action_reaction_pairs": builder_49,
    "50_newtons_universal_gravitation_law_and_ratio_scaling": builder_50,
}
