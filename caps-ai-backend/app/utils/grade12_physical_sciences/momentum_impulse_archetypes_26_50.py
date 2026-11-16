"""Grade 12 Physical Sciences — Momentum and Impulse: Archetypes 26 to 50.
Ground truth curriculum:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 1/01. Momentum and Impulse.md

Covers:
- 26–27: Isolated systems, external forces, formal principle of conservation of linear momentum.
- 28–32: 1D collisions (stick together, head-on rebound, stationary target, shunting/rear-end).
- 33–34: Elastic vs inelastic collisions (kinetic energy test: sum Ek_i vs sum Ek_f, mechanical energy lost to heat/sound/deformation).
- 35–38: Explosions and separations (stationary recoil, rocket staging in flight, ballistic bullet embeds vs passes through).
- 39–40: Ballistic pendulum and spring-loaded glider release with seed-varied inline SVGs.
- 41–44: Physics in action & safety (crumple zones, airbags, seatbelts, arrestor beds, sports follow-through & catching).
- 45–48: Cascades, post-collision friction stopping distances, ramp conversions, Newton's 3rd Law internal force cancellation.
- 49–50: Comprehensive exam synthesis rider and post-exam diagnostic autopsy / misconception triage.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _fmt(val: float | int, decimals: int = 2) -> str:
    """Format numeric values with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    rounded = round(float(val), decimals)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _svg_ballistic_pendulum(h_cm: float, m_b_g: float, m_w_kg: float) -> str:
    """Dynamic SVG of a ballistic pendulum before collision and after swing to height h."""
    swing_x = 260 + min(40, int(h_cm * 2.5))
    swing_y = 170 - min(45, int(h_cm * 3.0))
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="20" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Ballistic Pendulum Apparatus</text>'
        f'<line x1="80" y1="35" x2="300" y2="35" stroke="#334155" stroke-width="3"/>'
        f'<circle cx="160" cy="35" r="3" fill="#0f172a"/>'
        f'<circle cx="240" cy="35" r="3" fill="#0f172a"/>'
        f'<line x1="160" y1="35" x2="160" y2="155" stroke="#64748b" stroke-width="1.5"/>'
        f'<rect x="140" y="155" width="40" height="30" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>'
        f'<text x="160" y="174" text-anchor="middle" font-size="9" font-weight="bold" fill="#0f172a">{_fmt(m_w_kg)} kg</text>'
        f'<rect x="40" y="167" width="18" height="6" rx="2" fill="#d97706"/>'
        f'<line x1="62" y1="170" x2="110" y2="170" stroke="#d97706" stroke-width="2"/>'
        f'<polygon points="118,170 108,166 108,174" fill="#d97706"/>'
        f'<text x="75" y="162" text-anchor="middle" font-size="9" fill="#b45309">bullet ({_fmt(m_b_g)} g)</text>'
        f'<line x1="240" y1="35" x2="{swing_x}" y2="{swing_y}" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<rect x="{swing_x - 18}" y="{swing_y}" width="36" height="26" fill="#e2e8f0" stroke="#94a3b8" stroke-dasharray="2,2"/>'
        f'<line x1="185" y1="170" x2="{swing_x + 35}" y2="170" stroke="#94a3b8" stroke-dasharray="2,2"/>'
        f'<line x1="{swing_x + 25}" y1="170" x2="{swing_x + 25}" y2="{swing_y + 13}" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="{swing_x + 32}" y="{int((170 + swing_y + 13)/2)}" font-size="10" font-weight="bold" fill="#2563eb">h = {_fmt(h_cm)} cm</text>'
        f'</svg>'
    )


def _svg_gliders_spring(m1: float, m2: float, v1: float, v2: float) -> str:
    """Dynamic SVG of two compressed gliders on a linear air track released from rest."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 200" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Linear Air Track: Spring Release</text>'
        f'<line x1="25" y1="140" x2="355" y2="140" stroke="#334155" stroke-width="3"/>'
        f'<rect x="80" y="90" width="70" height="48" rx="4" fill="#93c5fd" stroke="#1d4ed8" stroke-width="2"/>'
        f'<text x="115" y="112" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e3a8a">Glider A</text>'
        f'<text x="115" y="128" text-anchor="middle" font-size="9" fill="#1e3a8a">{_fmt(m1)} kg</text>'
        f'<line x1="95" y1="75" x2="45" y2="75" stroke="#2563eb" stroke-width="2.5"/>'
        f'<polygon points="38,75 50,70 50,80" fill="#2563eb"/>'
        f'<text x="70" y="68" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">v_A = {_fmt(v1)} m·s⁻¹</text>'
        f'<rect x="230" y="90" width="75" height="48" rx="4" fill="#fecaca" stroke="#b91c1c" stroke-width="2"/>'
        f'<text x="267" y="112" text-anchor="middle" font-size="10" font-weight="bold" fill="#7f1d1d">Glider B</text>'
        f'<text x="267" y="128" text-anchor="middle" font-size="9" fill="#7f1d1d">{_fmt(m2)} kg</text>'
        f'<line x1="285" y1="75" x2="335" y2="75" stroke="#dc2626" stroke-width="2.5"/>'
        f'<polygon points="342,75 330,70 330,80" fill="#dc2626"/>'
        f'<text x="310" y="68" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">v_B = {_fmt(v2)} m·s⁻¹</text>'
        f'<path d="M 152 114 Q 165 105 178 114 T 204 114 T 228 114" fill="none" stroke="#64748b" stroke-width="2.5"/>'
        f'<text x="190" y="170" text-anchor="middle" font-size="9" fill="#475569">Initial state: at rest (Total p_i = 0)</text>'
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
    q_id = f"g12_mom_{idx:02d}_{r.randint(100000, 999999)}"
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
        "topic": "Momentum and Impulse",
        "subskill": subskill,
        "archetype_id": subskill,
        "question_type": "numeric_input",
        "modality": "physics_calculation",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": correct_answer,
        "ideal_answer": correct_answer,
        "sample_answer": solution_text,
        "solution": solution_text,
        "explanation": solution_text,
        "marks": marks,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "learning_objective_id": f"g12_mom_{subskill}",
        "mode": subskill,
        "misconception_tags": tags,
        "rubric": rubric,
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
            "width": 380,
            "height": 220,
        }
    return out


# 26. Isolated system and external forces definition
def build_26_isolated_system_and_external_forces_definition(r: random.Random) -> Dict[str, Any]:
    examples = [
        ("Two colliding trolleys on a smooth horizontal track with negligible friction", "Isolated system", "The resultant external force acting on the two trolleys is zero."),
        ("A skydiver falling through the air experiencing significant air resistance", "Non-isolated system", "Air resistance is an external force acting on the system, so the net external force is not zero."),
        ("A bullet embedding into a wooden block on a frictionless table", "Isolated system", "Horizontal friction is negligible, so the net external horizontal force on the bullet-block system is zero."),
        ("A car skidding to a halt on a rough tar road due to tyre-road friction", "Non-isolated system", "Friction between tyres and road is an unbalanced external force acting on the car."),
    ]
    ex = r.choice(examples)
    prompt = (
        f"Consider the following scenario: **{ex[0]}**\n\n"
        f"1. Define the term **isolated system** (or closed system) as used in physics.\n"
        f"2. Distinguish between an **internal force** and an **external force** within a system of bodies.\n"
        f"3. Classify the scenario above as an isolated system or non-isolated system, and give a reason."
    )
    ans = f"Isolated system: net external force is zero; {ex[1]}: {ex[2]}"
    sol = (
        f"1. An **isolated system** is a system on which the resultant (net) external force is zero.\n"
        f"2. **Internal forces** are forces that objects within the system exert on one another (they cancel out in pairs by Newton's Third Law). "
        f"**External forces** originate from outside the system (such as friction with the surface or air resistance).\n"
        f"3. **{ex[1]}**: {ex[2]}."
    )
    return _make_q(
        r, "26_isolated_system_and_external_forces_definition", 26, prompt, ans, sol, 4,
        ["confused_closed_matter_system_with_isolated_force_system"],
        [{"step": 1, "criterion": "Definition: net external force is zero", "marks": 2}, {"step": 2, "criterion": "Distinction between internal and external forces", "marks": 1}, {"step": 3, "criterion": f"Classification as {ex[1]} with reason", "marks": 1}],
        {"tier_1": "In physics mechanics, an isolated system means zero net external force.", "tier_2": "Internal forces cancel in action-reaction pairs.", "tier_3": ans},
    )


# 27. Principle of conservation of linear momentum statement
def build_27_principle_of_conservation_of_linear_momentum_statement(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"1. State the **Principle of Conservation of Linear Momentum** in words.\n"
        f"2. Write the general mathematical equation representing this principle for a collision between two objects $A$ and $B$.\n"
        f"3. State the crucial condition required for this principle to hold true."
    )
    ans = "Total linear momentum of an isolated system remains constant; m1*v1i + m2*v2i = m1*v1f + m2*v2f; System must be isolated (net external force = 0)"
    sol = (
        f"1. **Principle of Conservation of Linear Momentum:** The total linear momentum of an isolated system remains constant (is conserved) in magnitude and direction.\n"
        f"2. $$\\sum \\vec{{p}}_i = \\sum \\vec{{p}}_f \\implies m_A\\vec{{v}}_{{Ai}} + m_B\\vec{{v}}_{{Bi}} = m_A\\vec{{v}}_{{Af}} + m_B\\vec{{v}}_{{Bf}}$$\n"
        f"3. The essential condition is that the system must be **isolated** (the resultant external force on the system must be zero, $\\vec{{F}}_{{\\text{{net, ext}}}} = 0$)."
    )
    return _make_q(
        r, "27_principle_of_conservation_of_linear_momentum_statement", 27, prompt, ans, sol, 4,
        ["omitted_isolated_system_condition_in_momentum_conservation"],
        [{"step": 1, "criterion": "Complete law statement including 'total linear momentum of an isolated system is conserved'", "marks": 2}, {"step": 2, "criterion": "Formula m1v1i + m2v2i = m1v1f + m2v2f", "marks": 1}, {"step": 3, "criterion": "Condition: net external force is zero", "marks": 1}],
        {"tier_1": "The definition must explicitly mention that the system is isolated.", "tier_2": "Total initial momentum equals total final momentum.", "tier_3": ans},
    )


# 28. Conservation of momentum trolleys colliding stick together
def build_28_conservation_of_momentum_trolleys_colliding_stick_together(r: random.Random) -> Dict[str, Any]:
    m1 = r.choice([2.0, 3.0, 4.0, 5.0])
    v1i = r.choice([4.0, 6.0, 8.0])
    m2 = r.choice([1.0, 2.0, 3.0])
    v2i = 0.0
    vf = round((m1 * v1i) / (m1 + m2), 2)
    d = r.choice(["east", "to the right", "forward"])

    prompt = (
        f"A trolley $A$ of mass ${_fmt(m1)}\\text{{ kg}}$ moves along a frictionless horizontal track at ${_fmt(v1i)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ {d}.\n"
        f"It collides with a stationary trolley $B$ of mass ${_fmt(m2)}\\text{{ kg}}$.\n"
        f"On impact, the trolleys couple together and move as a single combined unit.\n\n"
        f"1. State the principle of conservation of linear momentum.\n"
        f"2. Calculate the velocity of the combined trolleys immediately after the collision."
    )
    ans = f"{_fmt(vf)} m·s⁻¹ {d}"
    sol = (
        f"1. The total linear momentum of an isolated system remains constant in magnitude and direction.\n"
        f"2. Take {d} as positive ($+$):\n"
        f"   $$\\sum p_i = \\sum p_f$$\n"
        f"   $$m_1 v_{{1i}} + m_2 v_{{2i}} = (m_1 + m_2) v_f$$\n"
        f"   $$({_fmt(m1)})({_fmt(v1i)}) + ({_fmt(m2)})(0) = ({_fmt(m1)} + {_fmt(m2)}) v_f$$\n"
        f"   $${_fmt(m1 * v1i)} = {_fmt(m1 + m2)} v_f \\implies v_f = \\frac{{{_fmt(m1 * v1i)}}}{{{_fmt(m1 + m2)}}} = {_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ {d}}}$$"
    )
    return _make_q(
        r, "28_conservation_of_momentum_trolleys_colliding_stick_together", 28, prompt, ans, sol, 5,
        ["forgot_to_add_masses_for_coupled_collision"],
        [{"step": 1, "criterion": "Statement of conservation of linear momentum", "marks": 2}, {"step": 2, "criterion": "Formula m1v1i + m2v2i = (m1+m2)vf", "marks": 1}, {"step": 3, "criterion": "Correct substitution", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(vf)} m·s⁻¹ {d}", "marks": 1}],
        {"tier_1": "When two objects stick together, their combined mass is m1 + m2.", "tier_2": f"vf = ({m1} * {v1i}) / ({m1} + {m2}).", "tier_3": ans},
    )


# 29. Conservation of momentum opposite direction head on stick
def build_29_conservation_of_momentum_opposite_direction_head_on_stick(r: random.Random) -> Dict[str, Any]:
    m1 = r.choice([1200, 1500, 1800])
    v1i = r.choice([15.0, 20.0, 25.0])
    m2 = r.choice([800, 1000, 1200])
    v2i_mag = r.choice([10.0, 15.0, 20.0])
    # p_net = m1*v1i - m2*v2i_mag
    p_net = m1 * v1i - m2 * v2i_mag
    total_m = m1 + m2
    vf = round(p_net / total_m, 2)
    res_dir = "east" if vf >= 0 else "west"

    prompt = (
        f"Car $A$ of mass ${m1}\\text{{ kg}}$ travelling east at ${_fmt(v1i)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ collides head-on "
        f"with Car $B$ of mass ${m2}\\text{{ kg}}$ travelling west at ${_fmt(v2i_mag)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"The wreckage of the two vehicles locks together on impact.\n\n"
        f"Taking east as positive, calculate the velocity (magnitude and direction) of the wreckage immediately after the impact."
    )
    ans = f"{_fmt(abs(vf))} m·s⁻¹ {res_dir}"
    sol = (
        f"Take east as positive ($+$):\n"
        f"- $v_{{Ai}} = +{_fmt(v1i)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n"
        f"- $v_{{Bi}} = -{_fmt(v2i_mag)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n"
        f"$$\\sum p_i = \\sum p_f$$\n"
        f"$$m_A v_{{Ai}} + m_B v_{{Bi}} = (m_A + m_B) v_f$$\n"
        f"$$({m1})({_fmt(v1i)}) + ({m2})(-{_fmt(v2i_mag)}) = ({m1} + {m2}) v_f$$\n"
        f"$${_fmt(m1 * v1i)} - {_fmt(m2 * v2i_mag)} = {total_m} v_f$$\n"
        f"$$v_f = \\frac{{{_fmt(p_net)}}}{{{total_m}}} = {_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"Therefore, velocity is **{_fmt(abs(vf))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}} {res_dir}**."
    )
    return _make_q(
        r, "29_conservation_of_momentum_opposite_direction_head_on_stick", 29, prompt, ans, sol, 5,
        ["added_head_on_momenta_instead_of_subtracting_vector_direction"],
        [{"step": 1, "criterion": "Formula mAvAi + mBvBi = (mA + mB)vf", "marks": 1}, {"step": 2, "criterion": f"Negative sign for westbound car (-{_fmt(v2i_mag)})", "marks": 1}, {"step": 3, "criterion": f"Total initial momentum = {_fmt(p_net)} kg·m·s⁻¹", "marks": 1}, {"step": 4, "criterion": f"Magnitude {_fmt(abs(vf))} m·s⁻¹", "marks": 1}, {"step": 5, "criterion": f"Direction {res_dir}", "marks": 1}],
        {"tier_1": "In a head-on collision, one velocity must be given a negative sign.", "tier_2": "Substitute: m1*v1 - m2*v2 = (m1 + m2)*vf.", "tier_3": ans},
    )


# 30. Conservation of momentum one stationary rebound apart
def build_30_conservation_of_momentum_one_stationary_rebound_apart(r: random.Random) -> Dict[str, Any]:
    m1 = r.choice([0.5, 1.0, 2.0])
    v1i = r.choice([6.0, 8.0, 10.0])
    m2 = r.choice([0.5, 1.0, 2.0])
    v1f = r.choice([1.0, 2.0, 3.0])
    # m1*v1i = m1*v1f + m2*v2f => v2f = (m1*v1i - m1*v1f) / m2
    v2f = round((m1 * (v1i - v1f)) / m2, 2)
    d = "east"

    prompt = (
        f"Trolley $X$ of mass ${_fmt(m1)}\\text{{ kg}}$ moves east at ${_fmt(v1i)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ and collides with "
        f"a stationary trolley $Y$ of mass ${_fmt(m2)}\\text{{ kg}}$ on a horizontal frictionless track.\n"
        f"After the collision, trolley $X$ continues moving east at ${_fmt(v1f)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the velocity of trolley $Y$ immediately after the collision."
    )
    ans = f"{_fmt(v2f)} m·s⁻¹ east"
    sol = (
        f"Take east as positive ($+$):\n"
        f"$$\\sum p_i = \\sum p_f$$\n"
        f"$$m_X v_{{Xi}} + m_Y v_{{Yi}} = m_X v_{{Xf}} + m_Y v_{{Yf}}$$\n"
        f"$$({_fmt(m1)})({_fmt(v1i)}) + 0 = ({_fmt(m1)})({_fmt(v1f)}) + ({_fmt(m2)}) v_{{Yf}}$$\n"
        f"$${_fmt(m1 * v1i)} = {_fmt(m1 * v1f)} + {_fmt(m2)} v_{{Yf}}$$\n"
        f"$$v_{{Yf}} = \\frac{{{_fmt(m1 * (v1i - v1f))}}}{{{_fmt(m2)}}} = {_fmt(v2f)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ east}}$$"
    )
    return _make_q(
        r, "30_conservation_of_momentum_one_stationary_rebound_apart", 30, prompt, ans, sol, 4,
        ["algebraic_rearrangement_error_in_momentum_conservation"],
        [{"step": 1, "criterion": "Formula m1v1i + m2v2i = m1v1f + m2v2f", "marks": 1}, {"step": 2, "criterion": "Substitution of known values", "marks": 1}, {"step": 3, "criterion": "Correct algebraic rearrangement", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(v2f)} m·s⁻¹ east", "marks": 1}],
        {"tier_1": "Initial momentum is only carried by trolley X.", "tier_2": "Subtract trolley X's final momentum from initial momentum, then divide by mY.", "tier_3": ans},
    )


# 31. Conservation of momentum both moving rebound apart
def build_31_conservation_of_momentum_both_moving_rebound_apart(r: random.Random) -> Dict[str, Any]:
    m1 = 3.0
    v1i = 5.0
    m2 = 2.0
    v2i = -4.0  # moving west
    v1f = -2.0  # rebounds west
    # 3(5) + 2(-4) = 15 - 8 = +7 kg*m/s
    # 3(-2) + 2*v2f = -6 + 2*v2f => 2*v2f = 13 => v2f = +6.5 m/s
    p_init = m1 * v1i + m2 * v2i
    v2f = round((p_init - m1 * v1f) / m2, 2)

    prompt = (
        f"Block $A$ of mass $3\\text{{ kg}}$ moves east at $5\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ and Block $B$ of mass $2\\text{{ kg}}$ "
        f"moves west at $4\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ on a frictionless surface.\n"
        f"They collide head-on. After the collision, Block $A$ rebounds west at $2\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Taking east as positive, calculate the velocity (magnitude and direction) of Block $B$ after the collision."
    )
    ans = f"{_fmt(v2f)} m·s⁻¹ east"
    sol = (
        f"Take east as positive ($+$):\n"
        f"- $v_{{Ai}} = +5\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, $v_{{Bi}} = -4\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n"
        f"- $v_{{Af}} = -2\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n"
        f"$$\\sum p_i = \\sum p_f$$\n"
        f"$$m_A v_{{Ai}} + m_B v_{{Bi}} = m_A v_{{Af}} + m_B v_{{Bf}}$$\n"
        f"$$(3)(5) + (2)(-4) = (3)(-2) + (2)v_{{Bf}}$$\n"
        f"$$15 - 8 = -6 + 2v_{{Bf}}$$\n"
        f"$$7 = -6 + 2v_{{Bf}} \\implies 2v_{{Bf}} = 13 \\implies v_{{Bf}} = +{_fmt(v2f)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"Block $B$ moves at **{_fmt(v2f)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}} east**."
    )
    return _make_q(
        r, "31_conservation_of_momentum_both_moving_rebound_apart", 31, prompt, ans, sol, 5,
        ["omitted_negative_sign_for_rebound_velocity_in_both_moving_collision"],
        [{"step": 1, "criterion": "Formula mAvAi + mBvBi = mAvAf + mBvBf", "marks": 1}, {"step": 2, "criterion": "Substitution with correct signs (+5, -4, -2)", "marks": 2}, {"step": 3, "criterion": f"Magnitude {_fmt(v2f)} m·s⁻¹", "marks": 1}, {"step": 4, "criterion": "Direction: east", "marks": 1}],
        {"tier_1": "Carefully assign +/- signs to every vector based on East (+).", "tier_2": "Block B before collision is -4, Block A after collision is -2.", "tier_3": ans},
    )


# 32. Conservation of momentum rear end collision shunting
def build_32_conservation_of_momentum_rear_end_collision_shunting(r: random.Random) -> Dict[str, Any]:
    m_suv = r.choice([2000, 2200, 2500])
    v_suv_i = r.choice([25.0, 30.0])
    m_hatch = r.choice([1000, 1100, 1200])
    v_hatch_i = r.choice([12.0, 15.0])
    v_suv_f = r.choice([18.0, 20.0])
    # p_tot = m1*v1i + m2*v2i
    p_tot = m_suv * v_suv_i + m_hatch * v_hatch_i
    v_hatch_f = round((p_tot - m_suv * v_suv_f) / m_hatch, 2)

    prompt = (
        f"An SUV of mass ${m_suv}\\text{{ kg}}$ travelling north at ${_fmt(v_suv_i)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ rear-ends "
        f"a hatchback of mass ${m_hatch}\\text{{ kg}}$ moving in the same lane at ${_fmt(v_hatch_i)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ north.\n"
        f"Immediately after the impact, the SUV's speed drops to ${_fmt(v_suv_f)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ north.\n\n"
        f"Calculate the speed and direction of the hatchback immediately after the rear-end shunting collision."
    )
    ans = f"{_fmt(v_hatch_f)} m·s⁻¹ north"
    sol = (
        f"Take north as positive ($+$):\n"
        f"$$\\sum p_i = \\sum p_f$$\n"
        f"$$m_1 v_{{1i}} + m_2 v_{{2i}} = m_1 v_{{1f}} + m_2 v_{{2f}}$$\n"
        f"$$({m_suv})({_fmt(v_suv_i)}) + ({m_hatch})({_fmt(v_hatch_i)}) = ({m_suv})({_fmt(v_suv_f)}) + ({m_hatch})v_{{2f}}$$\n"
        f"$${_fmt(p_tot)} = {_fmt(m_suv * v_suv_f)} + {m_hatch} v_{{2f}}$$\n"
        f"$$v_{{2f}} = \\frac{{{_fmt(p_tot - m_suv * v_suv_f)}}}{{{m_hatch}}} = {_fmt(v_hatch_f)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ north}}$$"
    )
    return _make_q(
        r, "32_conservation_of_momentum_rear_end_collision_shunting", 32, prompt, ans, sol, 4,
        ["treated_same_direction_vehicles_as_opposing_signs"],
        [{"step": 1, "criterion": "Formula m1v1i + m2v2i = m1v1f + m2v2f", "marks": 1}, {"step": 2, "criterion": "All initial and final velocities treated as positive (north)", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(v_hatch_f)} m·s⁻¹", "marks": 1}, {"step": 4, "criterion": "Direction: north", "marks": 1}],
        {"tier_1": "Both vehicles travel in the same direction initially, so both are positive.", "tier_2": "Calculate total initial momentum, subtract SUV final momentum, divide by hatchback mass.", "tier_3": ans},
    )


# 33. Elastic vs inelastic collisions kinetic energy test
def build_33_elastic_vs_inelastic_collisions_kinetic_energy_test(r: random.Random) -> Dict[str, Any]:
    # Inelastic collision test
    m1, v1i = 2.0, 6.0
    m2, v2i = 3.0, 0.0
    vf = round((m1 * v1i) / (m1 + m2), 2)  # 2.4 m/s
    ek_i = 0.5 * m1 * (v1i ** 2)  # 36 J
    ek_f = round(0.5 * (m1 + m2) * (vf ** 2), 2)  # 14.4 J

    prompt = (
        f"Trolley $A$ of mass $2\\text{{ kg}}$ gliding at $6\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ impacts a stationary trolley $B$ of mass $3\\text{{ kg}}$.\n"
        f"Both carts couple together with a common velocity of $2{{,}}4\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. State the distinction between an elastic impact and an inelastic impact.\n"
        f"2. Calculate the combined mechanical kinetic energy before ($E_{{ki}}$) and after ($E_{{kf}}$) the impact.\n"
        f"3. Classify with a reason whether this impact is elastic or inelastic."
    )
    ans = f"Inelastic; Total initial Ek ({_fmt(ek_i)} J) > Total final Ek ({_fmt(ek_f)} J)"
    sol = (
        f"1. In an **elastic collision**, total kinetic energy is conserved ($\\sum E_{{ki}} = \\sum E_{{kf}}$). "
        f"In an **inelastic collision**, total kinetic energy is not conserved ($\\sum E_{{kf}} < \\sum E_{{ki}}$).\n"
        f"2. Calculation:\n"
        f"   - $\\sum E_{{ki}} = \\frac{{1}}{{2}}(2)(6)^2 + 0 = {_fmt(ek_i)}\\text{{ J}}$\n"
        f"   - $\\sum E_{{kf}} = \\frac{{1}}{{2}}(2 + 3)(2{{,}}4)^2 = {_fmt(ek_f)}\\text{{ J}}$\n"
        f"3. Since $\\sum E_{{ki}} \\neq \\sum E_{{kf}}$ (${_fmt(ek_i)}\\text{{ J}} > {_fmt(ek_f)}\\text{{ J}}$), the collision is **inelastic**."
    )
    return _make_q(
        r, "33_elastic_vs_inelastic_collisions_kinetic_energy_test", 33, prompt, ans, sol, 5,
        ["assumed_all_collisions_conserve_kinetic_energy"],
        [{"step": 1, "criterion": "Definitions of elastic and inelastic collisions", "marks": 2}, {"step": 2, "criterion": f"Total initial Ek = {_fmt(ek_i)} J", "marks": 1}, {"step": 3, "criterion": f"Total final Ek = {_fmt(ek_f)} J", "marks": 1}, {"step": 4, "criterion": "Conclusion: inelastic because Ek is not conserved", "marks": 1}],
        {"tier_1": "Calculate Ek = 0,5 * m * v^2 for each object before and after the collision.", "tier_2": "Compare sum(Ek_i) with sum(Ek_f).", "tier_3": ans},
    )


# 34. Loss of kinetic energy and deformation work
def build_34_loss_of_kinetic_energy_and_deformation_work(r: random.Random) -> Dict[str, Any]:
    m1 = r.choice([1000, 1200, 1500])
    v1i = r.choice([20.0, 25.0])
    m2 = r.choice([800, 1000])
    v2i = 0.0
    vf = round((m1 * v1i) / (m1 + m2), 2)
    ek_i = 0.5 * m1 * (v1i ** 2)
    ek_f = round(0.5 * (m1 + m2) * (vf ** 2), 2)
    loss = round(ek_i - ek_f, 2)

    prompt = (
        f"A motor vehicle of mass ${m1}\\text{{ kg}}$ traveling at ${_fmt(v1i)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ strikes a parked vehicle of mass ${m2}\\text{{ kg}}$.\n"
        f"The bumpers interlock and both vehicles proceed at ${_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Determine the amount of mechanical energy transformed ($\\Delta E_k = E_{{ki}} - E_{{kf}}$) during impact.\n"
        f"2. Explain what happened to this dissipated energy (state two physical forms)."
    )
    ans = f"Loss = {_fmt(loss)} J; Converted to internal heat/thermal energy, sound, and work done deforming metal"
    sol = (
        f"1. $$E_{{ki}} = \\frac{{1}}{{2}}({m1})({_fmt(v1i)})^2 = {_fmt(ek_i)}\\text{{ J}}$$\n"
        f"   $$E_{{kf}} = \\frac{{1}}{{2}}({m1 + m2})({_fmt(vf)})^2 = {_fmt(ek_f)}\\text{{ J}}$$\n"
        f"   $$\\text{{Loss}} = E_{{ki}} - E_{{kf}} = {_fmt(ek_i)} - {_fmt(ek_f)} = {_fmt(loss)}\\text{{ J}}$$\n"
        f"2. The lost kinetic energy was converted into **heat (thermal energy)**, **sound energy**, and **work done deforming/crumpling the metal** structure."
    )
    return _make_q(
        r, "34_loss_of_kinetic_energy_and_deformation_work", 34, prompt, ans, sol, 4,
        ["thought_lost_kinetic_energy_disappeared_from_universe"],
        [{"step": 1, "criterion": f"Calculate initial Ek = {_fmt(ek_i)} J", "marks": 1}, {"step": 2, "criterion": f"Calculate final Ek = {_fmt(ek_f)} J", "marks": 1}, {"step": 3, "criterion": f"Kinetic energy loss = {_fmt(loss)} J", "marks": 1}, {"step": 4, "criterion": "Two valid forms: heat, sound, or deformation work", "marks": 1}],
        {"tier_1": "Calculate initial and final kinetic energies, then subtract.", "tier_2": "Energy cannot be destroyed; it converts to heat, sound, and metal deformation.", "tier_3": ans},
    )


# 35. Explosion stationary object separating two fragments
def build_35_explosion_stationary_object_separating_two_fragments(r: random.Random) -> Dict[str, Any]:
    # Cannon and cannonball or astronaut and tool
    m_cannon = r.choice([400, 500, 600, 800])
    m_ball = r.choice([4.0, 5.0, 8.0, 10.0])
    v_ball = r.choice([120.0, 150.0, 200.0])
    v_recoil = round((m_ball * v_ball) / m_cannon, 2)

    prompt = (
        f"A cannon of mass ${m_cannon}\\text{{ kg}}$ loaded with a cannonball of mass ${_fmt(m_ball)}\\text{{ kg}}$ is initially at rest.\n"
        f"When fired, the cannonball leaves the muzzle horizontally at ${_fmt(v_ball)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ forward.\n\n"
        f"1. Explain why the total initial momentum of the system is zero.\n"
        f"2. Calculate the recoil velocity of the cannon."
    )
    ans = f"{_fmt(v_recoil)} m·s⁻¹ backward"
    sol = (
        f"1. The cannon and cannonball are initially stationary ($v_i = 0$), so $p_i = (m_1 + m_2)(0) = 0$.\n"
        f"2. Take forward as positive ($+$):\n"
        f"   $$\\sum p_i = \\sum p_f$$\n"
        f"   $$0 = m_{{\\text{{cannon}}}} v_{{\\text{{recoil}}}} + m_{{\\text{{ball}}}} v_{{\\text{{ball}}}}$$\n"
        f"   $$0 = ({m_cannon})v_{{\\text{{recoil}}}} + ({_fmt(m_ball)})({_fmt(v_ball)})$$\n"
        f"   $$v_{{\\text{{recoil}}}} = -\\frac{{{_fmt(m_ball * v_ball)}}}{{{m_cannon}}} = -{_fmt(v_recoil)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"   The recoil velocity is **{_fmt(v_recoil)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}} backward**."
    )
    return _make_q(
        r, "35_explosion_stationary_object_separating_two_fragments", 35, prompt, ans, sol, 4,
        ["omitted_negative_sign_for_recoil_velocity"],
        [{"step": 1, "criterion": "Initial momentum is zero because system was at rest", "marks": 1}, {"step": 2, "criterion": "Formula 0 = m1v1 + m2v2", "marks": 1}, {"step": 3, "criterion": f"Magnitude {_fmt(v_recoil)} m·s⁻¹", "marks": 1}, {"step": 4, "criterion": "Direction: backward", "marks": 1}],
        {"tier_1": "Total initial momentum is zero.", "tier_2": "The cannon must have equal and opposite momentum to the cannonball: m1*v1 = -m2*v2.", "tier_3": ans},
    )


# 36. Explosion moving object separating in flight
def build_36_explosion_moving_object_separating_in_flight(r: random.Random) -> Dict[str, Any]:
    # Rocket in flight: (m1+m2)*vi = m1*v1f + m2*v2f
    m_body = 4000
    m_capsule = 1000
    vi = 1200.0
    v_body_f = 1100.0
    # (5000)(1200) = 4000(1100) + 1000(v_cap)
    # 6 000 000 = 4 400 000 + 1000*v_cap => 1000*v_cap = 1 600 000 => v_cap = 1600 m/s
    p_tot = (m_body + m_capsule) * vi
    v_cap_f = round((p_tot - m_body * v_body_f) / m_capsule, 1)

    prompt = (
        f"A space rocket of total mass $5000\\text{{ kg}}$ travels in outer space at $1200\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ forward.\n"
        f"An explosive bolt staging separates the rocket into a main body ($4000\\text{{ kg}}$) and a capsule ($1000\\text{{ kg}}$).\n"
        f"After staging, the main body continues forward at $1100\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the velocity of the capsule immediately after staging."
    )
    ans = f"{_fmt(v_cap_f)} m·s⁻¹ forward"
    sol = (
        f"Take forward as positive ($+$):\n"
        f"$$\\sum p_i = \\sum p_f$$\n"
        f"$$(m_{{\\text{{body}}}} + m_{{\\text{{capsule}}}}) v_i = m_{{\\text{{body}}}} v_{{\\text{{body, f}}}} + m_{{\\text{{capsule}}}} v_{{\\text{{capsule, f}}}}$$\n"
        f"$$(5000)(1200) = (4000)(1100) + (1000)v_{{\\text{{capsule, f}}}}$$\n"
        f"$$6{{,}}000{{,}}000 = 4{{,}}400{{,}}000 + 1000 v_{{\\text{{capsule, f}}}}$$\n"
        f"$$v_{{\\text{{capsule, f}}}} = \\frac{{1{{,}}600{{,}}000}}{{1000}} = {_fmt(v_cap_f)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ forward}}$$"
    )
    return _make_q(
        r, "36_explosion_moving_object_separating_in_flight", 36, prompt, ans, sol, 4,
        ["treated_initial_momentum_as_zero_for_moving_rocket_staging"],
        [{"step": 1, "criterion": "Formula (m1 + m2)vi = m1v1f + m2v2f", "marks": 1}, {"step": 2, "criterion": "Total initial momentum = 6 000 000 kg·m·s⁻¹", "marks": 1}, {"step": 3, "criterion": "Substitution of main body values", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(v_cap_f)} m·s⁻¹ forward", "marks": 1}],
        {"tier_1": "The rocket is already moving, so initial momentum is NOT zero.", "tier_2": "Calculate total initial momentum, subtract main body final momentum, divide by capsule mass.", "tier_3": ans},
    )


# 37. Bullet fired into stationary wooden block
def build_37_bullet_fired_into_stationary_wooden_block(r: random.Random) -> Dict[str, Any]:
    m_b_g = r.choice([15.0, 20.0, 25.0])
    m_b = m_b_g / 1000.0
    v_b = r.choice([300.0, 400.0, 500.0])
    m_w = r.choice([1.98, 2.98, 4.98])
    total_m = round(m_b + m_w, 3)
    vf = round((m_b * v_b) / total_m, 2)

    prompt = (
        f"A bullet of mass ${m_b_g}\\text{{ g}}$ is fired horizontally at ${_fmt(v_b)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ into a stationary "
        f"wooden block of mass ${_fmt(m_w)}\\text{{ kg}}$ resting on a smooth frictionless table.\n"
        f"The bullet embeds itself deeply inside the block.\n\n"
        f"Calculate the speed of the block and embedded bullet immediately after the collision."
    )
    ans = f"{_fmt(vf)} m·s⁻¹"
    sol = (
        f"1. Convert bullet mass: $m_b = \\frac{{{m_b_g}}}{{1000}} = {_fmt(m_b, 3)}\\text{{ kg}}$.\n"
        f"2. Apply conservation of linear momentum:\n"
        f"   $$m_b v_b + m_w v_w = (m_b + m_w) v_f$$\n"
        f"   $$({_fmt(m_b, 3)})({_fmt(v_b)}) + 0 = ({_fmt(m_b, 3)} + {_fmt(m_w)}) v_f$$\n"
        f"   $${_fmt(m_b * v_b)} = {_fmt(total_m, 3)} v_f \\implies v_f = \\frac{{{_fmt(m_b * v_b)}}}{{{_fmt(total_m, 3)}}} = {_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "37_bullet_fired_into_stationary_wooden_block", 37, prompt, ans, sol, 4,
        ["forgot_to_convert_bullet_grams_to_kg"],
        [{"step": 1, "criterion": f"Convert bullet mass to {_fmt(m_b, 3)} kg", "marks": 1}, {"step": 2, "criterion": "Formula mb*vb = (mb + mw)*vf", "marks": 1}, {"step": 3, "criterion": "Correct substitution", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(vf)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Divide grams by 1000 to convert to kg.", "tier_2": "Apply mb*vb = (mb + mw)*vf.", "tier_3": ans},
    )


# 38. Bullet passing through wooden block with reduced speed
def build_38_bullet_passing_through_wooden_block_with_reduced_speed(r: random.Random) -> Dict[str, Any]:
    m_b_g = 10.0
    m_b = 0.010
    v_bi = 400.0
    v_bf = 150.0
    m_w = 2.0
    # 0.010 * 400 = 0.010 * 150 + 2.0 * v_wf
    # 4.0 = 1.5 + 2.0*v_wf => 2.5 = 2.0*v_wf => v_wf = 1.25 m/s
    v_wf = round((m_b * (v_bi - v_bf)) / m_w, 2)

    prompt = (
        f"A bullet of mass $10\\text{{ g}}$ is fired horizontally at $400\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ towards a wooden block "
        f"of mass $2\\text{{ kg}}$ resting on a smooth horizontal table.\n"
        f"The bullet passes completely through the block and emerges horizontally with a reduced speed of $150\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the speed with which the wooden block moves after the bullet exits."
    )
    ans = f"{_fmt(v_wf)} m·s⁻¹"
    sol = (
        f"1. $m_b = \\frac{{10}}{{1000}} = 0{{,}}010\\text{{ kg}}$.\n"
        f"2. $$\\sum p_i = \\sum p_f$$\n"
        f"   $$m_b v_{{bi}} + 0 = m_b v_{{bf}} + m_w v_{{wf}}$$\n"
        f"   $$(0{{,}}010)(400) = (0{{,}}010)(150) + (2{{,}}0) v_{{wf}}$$\n"
        f"   $$4{{,}}0 = 1{{,}}5 + 2{{,}}0 v_{{wf}}$$\n"
        f"   $$2{{,}}0 v_{{wf}} = 2{{,}}5 \\implies v_{{wf}} = {_fmt(v_wf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "38_bullet_passing_through_wooden_block_with_reduced_speed", 38, prompt, ans, sol, 4,
        ["treated_bullet_as_embedded_instead_of_passing_through"],
        [{"step": 1, "criterion": "Convert bullet mass to 0,010 kg", "marks": 1}, {"step": 2, "criterion": "Formula mb*vbi = mb*vbf + mw*vwf", "marks": 1}, {"step": 3, "criterion": "Substitution of velocities", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(v_wf)} m·s⁻¹", "marks": 1}],
        {"tier_1": "The bullet does not remain inside; each object has its own separate final velocity.", "tier_2": "Calculate momentum transferred: 0,010*(400 - 150) = 2,5 N·s; divide by block mass.", "tier_3": ans},
    )


# 39. Ballistic pendulum conservation of momentum and energy (with SVG)
def build_39_ballistic_pendulum_conservation_of_momentum_and_energy_svg(r: random.Random) -> Dict[str, Any]:
    m_b_g = r.choice([10.0, 20.0, 25.0])
    m_b = m_b_g / 1000.0
    m_w = r.choice([1.99, 2.98, 4.975])
    total_m = round(m_b + m_w, 3)
    h_cm = r.choice([5.0, 8.0, 10.0, 12.0, 15.0])
    h_m = h_cm / 100.0
    g = 9.8
    # Swing: 0.5 * M * vf^2 = M * g * h => vf = sqrt(2 * g * h)
    vf = round(math.sqrt(2.0 * g * h_m), 3)
    # Collision: m_b * v_b = total_m * vf => v_b = (total_m * vf) / m_b
    vb = round((total_m * vf) / m_b, 1)
    svg = _svg_ballistic_pendulum(h_cm, m_b_g, m_w)

    prompt = (
        f"Refer to the ballistic pendulum apparatus where a bullet of mass ${m_b_g}\\text{{ g}}$ is fired horizontally into a suspended "
        f"block of mass ${_fmt(m_w)}\\text{{ kg}}$. The bullet embeds in the block, and the combination swings upwards to a maximum "
        f"height of $h = {_fmt(h_cm)}\\text{{ cm}}$ above its resting position.\n\n"
        f"1. State which conservation principle applies during the **collision**, and which applies during the subsequent **swing**.\n"
        f"2. Calculate the speed of the block and bullet combination immediately after the impact.\n"
        f"3. Calculate the initial firing speed ($v_b$) of the bullet."
    )
    ans = f"v_comb = {_fmt(vf, 3)} m·s⁻¹; v_bullet = {_fmt(vb)} m·s⁻¹"
    sol = (
        f"1. During the **collision**: **Conservation of linear momentum** (inelastic collision; kinetic energy is lost to deformation).\n"
        f"   During the **swing**: **Conservation of mechanical energy** (gravitational potential energy conversion, no friction).\n"
        f"2. For the swing from lowest point to maximum height $h = {_fmt(h_m)}\\text{{ m}}$:\n"
        f"   $$E_{{k, \\text{{bottom}}}} = E_{{p, \\text{{top}}}}$$\n"
        f"   $$\\frac{{1}}{{2}} M v_f^2 = M g h \\implies v_f = \\sqrt{{2 g h}} = \\sqrt{{2(9{{,}}8)({_fmt(h_m)})}} = {_fmt(vf, 3)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"3. For the collision:\n"
        f"   $$m_b v_b = (m_b + m_w) v_f$$\n"
        f"   $$({_fmt(m_b, 3)}) v_b = ({_fmt(total_m, 3)})({_fmt(vf, 3)})$$\n"
        f"   $$v_b = \\frac{{{_fmt(total_m * vf)}}}{{{_fmt(m_b, 3)}}} = {_fmt(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "39_ballistic_pendulum_conservation_of_momentum_and_energy_svg", 39, prompt, ans, sol, 6,
        ["applied_conservation_of_kinetic_energy_to_bullet_impact"],
        [{"step": 1, "criterion": "Distinction between collision (momentum) and swing (energy)", "marks": 2}, {"step": 2, "criterion": "Conservation of mechanical energy for swing vf = sqrt(2gh)", "marks": 1}, {"step": 3, "criterion": f"Combined speed = {_fmt(vf, 3)} m·s⁻¹", "marks": 1}, {"step": 4, "criterion": "Conservation of linear momentum substitution", "marks": 1}, {"step": 5, "criterion": f"Bullet speed = {_fmt(vb)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Work backwards: use Ep = mgh at top to find combined speed at bottom.", "tier_2": "Then use mb*vb = (mb + mw)*vf to find the bullet's firing speed.", "tier_3": ans},
        svg=svg,
    )


# 40. Two gliders compressed spring release (with SVG)
def build_40_two_gliders_compressed_spring_release_svg(r: random.Random) -> Dict[str, Any]:
    m1 = r.choice([0.4, 0.5, 0.8])
    m2 = r.choice([0.6, 1.0, 1.2])
    v1 = r.choice([1.5, 2.0, 3.0])
    v2 = round((m1 * v1) / m2, 2)
    svg = _svg_gliders_spring(m1, m2, v1, v2)

    prompt = (
        f"Refer to the linear air track showing two gliders, $A$ of mass ${_fmt(m1)}\\text{{ kg}}$ and $B$ of mass ${_fmt(m2)}\\text{{ kg}}$, "
        f"held together with a light compressed spring between them. The gliders are initially at rest.\n"
        f"When the spring mechanism is triggered, Glider $A$ moves off to the left at ${_fmt(v1)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Taking to the right as positive, calculate the velocity of Glider $B$."
    )
    ans = f"{_fmt(v2)} m·s⁻¹ to the right"
    sol = (
        f"Take to the right as positive ($+$):\n"
        f"- $v_{{Ai}} = 0$, $v_{{Bi}} = 0$\n"
        f"- $v_{{Af}} = -{_fmt(v1)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ (to the left)\n"
        f"$$\\sum p_i = \\sum p_f$$\n"
        f"$$0 = m_A v_{{Af}} + m_B v_{{Bf}}$$\n"
        f"$$0 = ({_fmt(m1)})(-{_fmt(v1)}) + ({_fmt(m2)}) v_{{Bf}}$$\n"
        f"$$0 = -{_fmt(m1 * v1)} + {_fmt(m2)} v_{{Bf}} \\implies v_{{Bf}} = +\\frac{{{_fmt(m1 * v1)}}}{{{_fmt(m2)}}} = +{_fmt(v2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"Glider $B$ moves at **{_fmt(v2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}} to the right**."
    )
    return _make_q(
        r, "40_two_gliders_compressed_spring_release_svg", 40, prompt, ans, sol, 4,
        ["omitted_negative_sign_for_leftward_glider"],
        [{"step": 1, "criterion": "Formula 0 = mAvAf + mBvBf", "marks": 1}, {"step": 2, "criterion": f"Negative sign for leftward velocity (-{_fmt(v1)})", "marks": 1}, {"step": 3, "criterion": f"Magnitude {_fmt(v2)} m·s⁻¹", "marks": 1}, {"step": 4, "criterion": "Direction: to the right", "marks": 1}],
        {"tier_1": "Initial momentum is zero.", "tier_2": "Glider A to the left is negative, so Glider B must move to the right (positive).", "tier_3": ans},
        svg=svg,
    )


# 41. Physics in action car crumple zones and safety
def build_41_physics_in_action_car_crumple_zones_and_safety(r: random.Random) -> Dict[str, Any]:
    m = 1200
    vi = 20.0  # 72 km/h
    # delta_p is fixed: m*(0 - vi) = -24 000 kg*m/s
    dp = m * vi
    dt_rigid = 0.05
    dt_crumple = 0.25
    f_rigid = dp / dt_rigid
    f_crumple = dp / dt_crumple

    prompt = (
        f"A motorcar of mass ${m}\\text{{ kg}}$ travelling at $20\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ strikes a solid barrier and comes to rest.\n\n"
        f"1. Calculate the magnitude of the change in momentum ($\\Delta p$) of the car.\n"
        f"2. If the car had a rigid chassis that stopped it in $\\Delta t = 0{{,}}05\\text{{ s}}$, calculate the average net force exerted on the vehicle.\n"
        f"3. Modern vehicles incorporate engineered **crumple zones** that increase the collision stopping duration to $\\Delta t = 0{{,}}25\\text{{ s}}$. "
        f"Calculate the average net force in this case.\n"
        f"4. With reference to $F_{{\\text{{net}}}} = \\frac{{\\Delta p}}{{\\Delta t}}$, explain the life-saving benefit of crumple zones for vehicle occupants."
    )
    ans = f"Δp = {dp} kg·m·s⁻¹; F_rigid = {_fmt(f_rigid)} N; F_crumple = {_fmt(f_crumple)} N; Crumple zones prolong contact time Δt so that for the same Δp, F_net is significantly reduced"
    sol = (
        f"1. $$\\Delta p = m(v_f - v_i) = {m}(0 - 20) = -{dp}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"   Magnitude is **{dp}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}**.\n"
        f"2. $$F_{{\\text{{rigid}}}} = \\frac{{\\Delta p}}{{\\Delta t}} = \\frac{{{dp}}}{{0{{,}}05}} = {_fmt(f_rigid)}\\text{{ N}}$$\n"
        f"3. $$F_{{\\text{{crumple}}}} = \\frac{{\\Delta p}}{{\\Delta t}} = \\frac{{{dp}}}{{0{{,}}25}} = {_fmt(f_crumple)}\\text{{ N}}$$\n"
        f"4. For a car coming to rest, the **change in momentum $\\Delta p$ is fixed**. "
        f"By extending the deformation time $\\Delta t$, the rate of change of momentum is reduced, which **dramatically decreases the average net force $F_{{\\text{{net}}}}$** "
        f"transmitted to the occupants, preventing fatal injuries."
    )
    return _make_q(
        r, "41_physics_in_action_car_crumple_zones_and_safety", 41, prompt, ans, sol, 5,
        ["thought_crumple_zones_reduce_the_total_momentum_change"],
        [{"step": 1, "criterion": f"Calculate Δp = {dp} kg·m·s⁻¹", "marks": 1}, {"step": 2, "criterion": f"F_rigid = {_fmt(f_rigid)} N", "marks": 1}, {"step": 3, "criterion": f"F_crumple = {_fmt(f_crumple)} N", "marks": 1}, {"step": 4, "criterion": "Statement that Δp remains constant for coming to rest", "marks": 1}, {"step": 5, "criterion": "Explanation that increasing Δt decreases F_net", "marks": 1}],
        {"tier_1": "Change in momentum is fixed because initial and final velocities are identical in both cases.", "tier_2": "Because F_net = Δp / Δt, increasing Δt reduces the force F_net.", "tier_3": ans},
    )


# 42. Physics in action airbags seatbelts and padded dashboards
def build_42_physics_in_action_airbags_seatbelts_and_padded_dashboards(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Modern road passenger vehicles are equipped with safety features including seatbelts, airbags, and padded dashboards.\n\n"
        f"1. Explain how **airbags** and **seatbelts** work in conjunction to reduce the risk of severe head and chest injuries during a frontal collision.\n"
        f"2. Frame your explanation explicitly using the concepts of **impulse**, **contact time ($\\Delta t$)**, and **resultant force ($\\vec{{F}}_{{\\text{{net}}}}$)**."
    )
    ans = "Airbags and seatbelts extend the contact time Δt over which the passenger's momentum changes to zero. Since F_net = Δp / Δt and Δp is constant, the larger Δt significantly reduces the average net force experienced by the body, preventing fatal trauma."
    sol = (
        f"1. In a frontal collision, the vehicle stops rapidly, but the occupant continues moving forward due to inertia.\n"
        f"2. To bring the occupant to rest, their momentum must change from $p_i = mv$ to $0$ (a fixed change in momentum $\\Delta p$).\n"
        f"3. **Airbags and stretching seatbelts** deform and yield, **increasing the duration of the impact (contact time $\\Delta t$)**.\n"
        f"4. According to Newton's Second Law in terms of momentum:\n"
        f"   $$\\vec{{F}}_{{\\text{{net}}}} = \\frac{{\\Delta\\vec{{p}}}}{{\\Delta t}}$$\n"
        f"   Because $\\Delta p$ is constant, increasing $\\Delta t$ **substantially reduces the average resultant force $\\vec{{F}}_{{\\text{{net}}}}$** acting on the occupant's head and torso, "
        f"preventing collision with rigid steering columns or windshields."
    )
    return _make_q(
        r, "42_physics_in_action_airbags_seatbelts_and_padded_dashboards", 42, prompt, ans, sol, 4,
        ["thought_airbags_reduce_the_impulse_delivered_to_passenger"],
        [{"step": 1, "criterion": "Identify fixed change in momentum Δp to bring occupant to rest", "marks": 1}, {"step": 2, "criterion": "Airbag/seatbelt increases contact time Δt", "marks": 1}, {"step": 3, "criterion": "Reference to formula F_net = Δp / Δt (or Impulse = F_net * Δt)", "marks": 1}, {"step": 4, "criterion": "Conclude that force F_net is reduced, preventing severe injury", "marks": 1}],
        {"tier_1": "Impulse (Δp) is determined by the occupant's mass and speed.", "tier_2": "The cushion effect increases the time Δt to come to a stop, which lowers F_net.", "tier_3": ans},
    )


# 43. Physics in action arrestor beds for runaway trucks
def build_43_physics_in_action_arrestor_beds_for_runaway_trucks(r: random.Random) -> Dict[str, Any]:
    m_truck = r.choice([15000, 20000, 25000])
    v_init = r.choice([25.0, 30.0])  # ~90-108 km/h
    dt = r.choice([4.0, 5.0, 6.0])
    dp = m_truck * v_init
    f_arrest = round(dp / dt, 1)

    prompt = (
        f"A runaway heavy transport truck of mass ${m_truck}\\text{{ kg}}$ descending a steep mountain pass suffers total brake failure "
        f"at ${_fmt(v_init)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ and steers into an emergency **arrestor bed** filled with deep gravel.\n"
        f"The truck sinks into the gravel and is brought smoothly to a complete standstill in ${_fmt(dt)}\\text{{ s}}$.\n\n"
        f"1. Calculate the magnitude of the impulse delivered to the truck by the arrestor bed.\n"
        f"2. Calculate the average decelerating net force exerted by the gravel bed on the truck.\n"
        f"3. Explain why driving into an arrestor bed is far safer than colliding with a rigid concrete safety barrier."
    )
    ans = f"Impulse = {dp} N·s; F_net = {_fmt(f_arrest)} N; The deep gravel allows the truck to sink and stop gradually over a long time (Δt), greatly reducing the decelerating force"
    sol = (
        f"1. $$\\text{{Impulse}} = \\Delta p = m(v_f - v_i) = {m_truck}(0 - {_fmt(v_init)}) = -{dp}\\text{{ N}}\\cdot\\text{{s}}$$\n"
        f"   Magnitude is **{dp}\\text{{ N}}\\cdot\\text{{s}}**.\n"
        f"2. $$F_{{\\text{{net}}}} = \\frac{{\\Delta p}}{{\\Delta t}} = \\frac{{{dp}}}{{{_fmt(dt)}}} = {_fmt(f_arrest)}\\text{{ N}}$$\n"
        f"3. A rigid concrete barrier stops the truck almost instantaneously ($\\Delta t \\approx 0{{,}}1\\text{{ s}}$), causing extreme deceleration forces "
        f"that crush the vehicle cabin. The loose gravel arrestor bed allows the truck to sink and stop gradually over several seconds ($\\Delta t = {_fmt(dt)}\\text{{ s}}$), "
        f"greatly **reducing the net force $F_{{\\text{{net}}}}$** to survivable levels."
    )
    return _make_q(
        r, "43_physics_in_action_arrestor_beds_for_runaway_trucks", 43, prompt, ans, sol, 4,
        ["confused_arrestor_bed_mechanism_with_gravity_alone"],
        [{"step": 1, "criterion": f"Calculate impulse = {dp} N·s", "marks": 1}, {"step": 2, "criterion": f"Calculate F_net = {_fmt(f_arrest)} N", "marks": 1}, {"step": 3, "criterion": "Concrete barrier has very small Δt resulting in catastrophic force", "marks": 1}, {"step": 4, "criterion": "Gravel increases Δt, dramatically reducing F_net", "marks": 1}],
        {"tier_1": "Calculate impulse = m * v_init.", "tier_2": "Divide by the stopping time to find average force.", "tier_3": ans},
    )


# 44. Physics in action sports follow through and catching
def build_44_physics_in_action_sports_follow_through_and_catching(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In sports science, the concept of impulse is fundamental to performance and injury prevention:\n\n"
        f"1. When catching a hard-hit cricket ball, a fielder always pulls their hands backwards in the direction of the ball's motion. "
        f"Explain why this reduces pain and injury to the hands.\n"
        f"2. In tennis, golf, and baseball, coaches insist on a full **follow-through** when striking the ball. "
        f"Explain how following through increases the final speed of the ball, referring to the impulse formula."
    )
    ans = "Catching: pulling hands back increases contact time Δt, which reduces F_net = Δp/Δt on hands; Follow-through: prolongs contact duration Δt with the ball while exerting force F, increasing Impulse = F*Δt = Δp, resulting in a higher exit speed vf."
    sol = (
        f"1. **Catching a ball:** To stop the ball, a fixed change in momentum $\\Delta p = m(0 - v_i)$ must be achieved. "
        f"By pulling the hands backward, the fielder **increases the contact time $\\Delta t$** of the catch. "
        f"Because $F_{{\\text{{net}}}} = \\frac{{\\Delta p}}{{\\Delta t}}$, increasing $\\Delta t$ **reduces the average force** exerted on the fielder's hands, preventing injury.\n\n"
        f"2. **Follow-through:** During a swing, a full follow-through **increases the contact duration $\\Delta t$** over which the racket/club exerts force $F$ on the ball. "
        f"Since $\\text{{Impulse}} = F_{{\\text{{net}}}}\\Delta t = m(v_f - v_i)$, increasing the contact time increases the impulse delivered to the ball, "
        f"producing a **larger change in momentum and thus a higher final launch velocity $v_f$**."
    )
    return _make_q(
        r, "44_physics_in_action_sports_follow_through_and_catching", 44, prompt, ans, sol, 4,
        ["confused_force_reduction_in_catching_with_momentum_change_increase_in_hitting"],
        [{"step": 1, "criterion": "Catching: increased Δt reduces F_net on hands", "marks": 2}, {"step": 2, "criterion": "Hitting: increased Δt increases Impulse = F*Δt", "marks": 1}, {"step": 3, "criterion": "Conclude that larger impulse produces greater exit velocity", "marks": 1}],
        {"tier_1": "In catching, Δp is fixed and we want to minimize F_net by maximizing Δt.", "tier_2": "In hitting, F is maximum and increasing Δt maximizes Δp (and therefore vf).", "tier_3": ans},
    )


# 45. Multi body three object linear cascade collision
def build_45_multi_body_three_object_linear_cascade_collision(r: random.Random) -> Dict[str, Any]:
    # A hits B, then B hits C
    # All masses equal e.g. 1 kg or different
    mA = 2.0
    mB = 2.0
    mC = 2.0
    vAi = 6.0
    # In first collision, A stops and B takes off at 6.0 m/s (elastic identical masses)
    # Then B collides with C and they stick together: (mB+mC)*vf = mB*vB => 4*vf = 12 => vf = 3.0 m/s
    v_final = 3.0

    prompt = (
        f"Three identical dynamics carts, $A$, $B$, and $C$, each of mass $2\\text{{ kg}}$, are aligned in a straight line on a horizontal frictionless track.\n"
        f"Carts $B$ and $C$ are initially stationary. Cart $A$ moves east at $6\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ and strikes Cart $B$.\n"
        f"In the first collision, Cart $A$ comes to a complete standstill and transfers all its momentum to Cart $B$.\n"
        f"Cart $B$ then collides with Cart $C$, and carts $B$ and $C$ couple together and move as one.\n\n"
        f"1. State the velocity of Cart $B$ immediately after being struck by Cart $A$.\n"
        f"2. Calculate the final velocity of the coupled carts $B$ and $C$."
    )
    ans = f"v_B = 6 m·s⁻¹ east; v_final(B+C) = {_fmt(v_final)} m·s⁻¹ east"
    sol = (
        f"1. First collision ($A$ and $B$):\n"
        f"   $$m_A v_{{Ai}} + 0 = m_A(0) + m_B v_{{Bf1}}$$\n"
        f"   $$(2)(6) = (2)v_{{Bf1}} \\implies v_{{Bf1}} = 6\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ east}}$$\n\n"
        f"2. Second collision ($B$ and $C$):\n"
        f"   $$m_B v_{{Bi2}} + 0 = (m_B + m_C) v_{{f2}}$$\n"
        f"   $$(2)(6) = (2 + 2)v_{{f2}}$$\n"
        f"   $$12 = 4 v_{{f2}} \\implies v_{{f2}} = {_fmt(v_final)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ east}}$$"
    )
    return _make_q(
        r, "45_multi_body_three_object_linear_cascade_collision", 45, prompt, ans, sol, 4,
        ["treated_cascade_collision_as_single_step"],
        [{"step": 1, "criterion": "First collision momentum conservation", "marks": 1}, {"step": 2, "criterion": "Cart B velocity = 6 m·s⁻¹ east", "marks": 1}, {"step": 3, "criterion": "Second collision momentum conservation mB*vB = (mB + mC)*vf", "marks": 1}, {"step": 4, "criterion": f"Final coupled velocity = {_fmt(v_final)} m·s⁻¹ east", "marks": 1}],
        {"tier_1": "Solve the cascade step-by-step: first collision A->B, then second collision B->C.", "tier_2": "In the second collision, B and C stick together.", "tier_3": ans},
    )


# 46. Collision with frictional stopping distance kinematics
def build_46_collision_with_frictional_stopping_distance_kinematics(r: random.Random) -> Dict[str, Any]:
    m1 = 1200
    v1i = 20.0
    m2 = 800
    # Combined mass after sticking together: 2000 kg
    # vf = (1200*20) / 2000 = 12.0 m/s
    vf_coll = 12.0
    # Friction on road: mu_k = 0.6 => a = -mu_k * g = -0.6 * 9.8 = -5.88 m/s^2
    mu_k = 0.6
    g = 9.8
    a_fric = mu_k * g  # 5.88 m/s^2
    # v^2 = u^2 + 2as => 0 = (12)^2 - 2(5.88)*s => s = 144 / 11.76 = 12.24 m
    dist = round((vf_coll ** 2) / (2.0 * a_fric), 2)

    prompt = (
        f"Car $A$ of mass $1200\\text{{ kg}}$ travelling east at $20\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ collides with stationary Car $B$ of mass $800\\text{{ kg}}$.\n"
        f"The two cars lock together immediately upon impact.\n"
        f"After the collision, the wreckage skids across a rough road surface with a coefficient of kinetic friction $\\mu_k = 0{{,}}6$.\n\n"
        f"1. Calculate the velocity of the locked wreckage immediately after the impact.\n"
        f"2. Calculate the magnitude of the frictional deceleration of the wreckage ($a = \\mu_k g$, where $g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n"
        f"3. Calculate the skid distance ($\\Delta x$) until the wreckage comes to rest."
    )
    ans = f"v_post = {_fmt(vf_coll)} m·s⁻¹ east; a = {_fmt(a_fric)} m·s⁻²; Skid distance = {_fmt(dist)} m"
    sol = (
        f"1. Conservation of linear momentum:\n"
        f"   $$m_A v_{{Ai}} + 0 = (m_A + m_B) v_f$$\n"
        f"   $$(1200)(20) = (1200 + 800) v_f \\implies 24{{,}}000 = 2000 v_f \\implies v_f = {_fmt(vf_coll)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ east}}$$\n\n"
        f"2. Deceleration from kinetic friction:\n"
        f"   $$f_k = \\mu_k N = \\mu_k m g \\implies a = \\frac{{f_k}}{{m}} = \\mu_k g = (0{{,}}6)(9{{,}}8) = {_fmt(a_fric)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$$\n\n"
        f"3. Stopping distance using equation of motion ($v_f^2 = v_i^2 + 2a\\Delta x$ with $v_f = 0$ and $a = -{_fmt(a_fric)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$):\n"
        f"   $$0 = ({_fmt(vf_coll)})^2 - 2({_fmt(a_fric)})\\Delta x$$\n"
        f"   $$\\Delta x = \\frac{{{_fmt(vf_coll ** 2)}}}{{2({_fmt(a_fric)})}} = {_fmt(dist)}\\text{{ m}}$$"
    )
    return _make_q(
        r, "46_collision_with_frictional_stopping_distance_kinematics", 46, prompt, ans, sol, 5,
        ["used_pre_collision_speed_for_skid_mark_calculation"],
        [{"step": 1, "criterion": f"Post-collision speed = {_fmt(vf_coll)} m·s⁻¹", "marks": 2}, {"step": 2, "criterion": f"Deceleration a = μk * g = {_fmt(a_fric)} m·s⁻²", "marks": 1}, {"step": 3, "criterion": "Equation of motion vf^2 = vi^2 + 2aΔx", "marks": 1}, {"step": 4, "criterion": f"Skid distance = {_fmt(dist)} m", "marks": 1}],
        {"tier_1": "Find the post-collision speed using momentum conservation first.", "tier_2": "Then use kinematics with a = -mu*g to find the skid distance.", "tier_3": ans},
    )


# 47. Collision on inclined ramp or drop
def build_47_collision_on_inclined_ramp_or_drop(r: random.Random) -> Dict[str, Any]:
    m1 = 2.0
    m2 = 3.0
    h = r.choice([1.25, 1.80, 2.45, 3.20])
    g = 9.8
    # v1_bottom = sqrt(2*g*h)
    v1_bottom = round(math.sqrt(2.0 * g * h), 2)
    # Inelastic collision: (m1+m2)*vf = m1*v1_bottom => vf = (2 / 5) * v1_bottom
    vf = round((m1 * v1_bottom) / (m1 + m2), 2)

    prompt = (
        f"Cart $A$ of mass $2\\text{{ kg}}$ is released from rest at the top of a smooth curved ramp of height $h = {_fmt(h)}\\text{{ m}}$.\n"
        f"At the bottom of the ramp, Cart $A$ moves horizontally on a frictionless track and collides with stationary Cart $B$ of mass $3\\text{{ kg}}$.\n"
        f"The carts lock together upon impact.\n\n"
        f"1. Calculate the speed of Cart $A$ at the bottom of the ramp just before the collision ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n"
        f"2. Calculate the speed of the combined carts after the collision."
    )
    ans = f"v_bottom = {_fmt(v1_bottom)} m·s⁻¹; v_final = {_fmt(vf)} m·s⁻¹"
    sol = (
        f"1. Conservation of mechanical energy on the ramp:\n"
        f"   $$E_{{mech, \\text{{top}}}} = E_{{mech, \\text{{bottom}}}}$$\n"
        f"   $$m_A g h = \\frac{{1}}{{2}} m_A v_A^2 \\implies v_A = \\sqrt{{2 g h}} = \\sqrt{{2(9{{,}}8)({_fmt(h)})}} = {_fmt(v1_bottom)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$\n\n"
        f"2. Conservation of linear momentum during the horizontal collision:\n"
        f"   $$m_A v_A + 0 = (m_A + m_B) v_f$$\n"
        f"   $$(2)({_fmt(v1_bottom)}) = (2 + 3) v_f$$\n"
        f"   $$v_f = \\frac{{2({_fmt(v1_bottom)})}}{{5}} = {_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "47_collision_on_inclined_ramp_or_drop", 47, prompt, ans, sol, 4,
        ["applied_momentum_conservation_to_curved_ramp_fall"],
        [{"step": 1, "criterion": "Energy conservation on ramp mgh = 0,5mv^2", "marks": 1}, {"step": 2, "criterion": f"Speed at bottom = {_fmt(v1_bottom)} m·s⁻¹", "marks": 1}, {"step": 3, "criterion": "Momentum conservation for collision", "marks": 1}, {"step": 4, "criterion": f"Final coupled speed = {_fmt(vf)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Gravity does work on the ramp: use v = sqrt(2gh).", "tier_2": "Then apply linear momentum conservation: m1*v1 = (m1 + m2)*vf.", "tier_3": ans},
    )


# 48. Internal vs external forces system momentum conservation
def build_48_internal_vs_external_forces_system_momentum_conservation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Consider an isolated head-on contact interaction between two carts $A$ and $B$, where interaction forces are exerted.\n\n"
        f"1. State **Newton's Third Law of Motion** in words.\n"
        f"2. Using Newton's Third Law ($\\vec{{F}}_{{A\\text{{ on }}B}} = -\\vec{{F}}_{{B\\text{{ on }}A}}$) and Newton's Second Law expressed with rate of change of momentum, "
        f"demonstrate that the combined momentum of the two-cart assembly remains constant during the contact."
    )
    ans = "Action-reaction pairs are equal in magnitude and opposite in direction. Since F_A on B = -F_B on A and contact time Δt is identical, F_A on B * Δt = -F_B on A * Δt => Δp_B = -Δp_A => Δp_A + Δp_B = 0, so total momentum is conserved."
    sol = (
        f"1. **Newton's Third Law of Motion:** When object $A$ exerts a force on object $B$, object $B$ simultaneously exerts an equal in magnitude and oppositely directed force on object $A$.\n\n"
        f"2. **Proof of Conservation of Linear Momentum:**\n"
        f"   - During the contact time $\\Delta t$, the force exerted by $A$ on $B$ and by $B$ on $A$ satisfy:\n"
        f"     $$\\vec{{F}}_{{A\\text{{ on }}B}} = -\\vec{{F}}_{{B\\text{{ on }}A}}$$\n"
        f"   - Multiplying both sides by the interaction duration $\\Delta t$:\n"
        f"     $$\\vec{{F}}_{{A\\text{{ on }}B}} \\Delta t = -\\vec{{F}}_{{B\\text{{ on }}A}} \\Delta t$$\n"
        f"   - By the impulse-momentum theorem ($\\text{{Impulse}} = \\Delta\\vec{{p}}$):\n"
        f"     $$\\Delta\\vec{{p}}_B = -\\Delta\\vec{{p}}_A$$\n"
        f"   - Rearranging:\n"
        f"     $$\\Delta\\vec{{p}}_A + \\Delta\\vec{{p}}_B = 0 \\implies \\Delta\\vec{{p}}_{{\\text{{total}}}} = 0$$\n"
        f"   - Since the net change in momentum is zero, the total linear momentum before the collision equals the total linear momentum after the collision: "
        f"     $$\\sum\\vec{{p}}_i = \\sum\\vec{{p}}_f$$"
    )
    return _make_q(
        r, "48_internal_vs_external_forces_system_momentum_conservation", 48, prompt, ans, sol, 4,
        ["failed_to_link_newtons_third_law_to_momentum_conservation"],
        [{"step": 1, "criterion": "Statement of Newton's Third Law", "marks": 1}, {"step": 2, "criterion": "Statement FA on B = -FB on A", "marks": 1}, {"step": 3, "criterion": "Multiply by Δt to show ΔpB = -ΔpA", "marks": 1}, {"step": 4, "criterion": "Conclude Δp_total = 0, hence momentum is conserved", "marks": 1}],
        {"tier_1": "Newton's 3rd Law states forces are equal and opposite.", "tier_2": "Because contact times are identical, impulses are equal and opposite, so ΔpA + ΔpB = 0.", "tier_3": ans},
    )


# 49. Capstone momentum and impulse exam rider
def build_49_capstone_momentum_and_impulse_exam_rider(r: random.Random) -> Dict[str, Any]:
    m1 = 1500
    v1i = 20.0  # 72 km/h east
    m2 = 1000
    v2i = 0.0
    vf = round((m1 * v1i) / (m1 + m2), 2)  # 12.0 m/s east
    dt = 0.15
    dp1 = round(m1 * (vf - v1i), 1)  # -12000 N*s
    f_net = round(abs(dp1) / dt, 1)  # 80000 N

    prompt = (
        f"**Comprehensive Examination Question:**\n"
        f"A patrol car of mass ${m1}\\text{{ kg}}$ travelling east at ${_fmt(v1i)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ collides with a stationary "
        f"van of mass ${m2}\\text{{ kg}}$ on a level frictionless road. Immediately after the collision, the two vehicles interlock and move together.\n"
        f"The collision interaction lasts for ${_fmt(dt)}\\text{{ s}}$.\n\n"
        f"1. State the principle of conservation of linear momentum.\n"
        f"2. Calculate the velocity of the locked vehicles immediately after impact.\n"
        f"3. Calculate the magnitude and direction of the average resultant force exerted by the van on the patrol car during the ${_fmt(dt)}\\text{{ s}}$ impact.\n"
        f"4. State the magnitude and direction of the force exerted by the patrol car on the van (name the scientific law supporting your answer)."
    )
    ans = f"v_f = {_fmt(vf)} m·s⁻¹ east; F_van_on_car = {_fmt(f_net)} N west; F_car_on_van = {_fmt(f_net)} N east (Newton's Third Law)"
    sol = (
        f"1. **Conservation of Linear Momentum:** The total linear momentum of an isolated system remains constant in magnitude and direction.\n"
        f"2. Take east as positive ($+$):\n"
        f"   $$m_1 v_{{1i}} + m_2 v_{{2i}} = (m_1 + m_2) v_f$$\n"
        f"   $$({m1})({_fmt(v1i)}) + 0 = ({m1 + m2}) v_f \\implies v_f = \\frac{{{m1 * v1i}}}{{{m1 + m2}}} = {_fmt(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ east}}$$\n"
        f"3. Force on patrol car:\n"
        f"   $$\\Delta p_1 = m_1(v_f - v_{{1i}}) = {m1}({_fmt(vf)} - {_fmt(v1i)}) = {_fmt(dp1)}\\text{{ kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"   $$F_{{\\text{{net}}}} = \\frac{{\\Delta p_1}}{{\\Delta t}} = \\frac{{{_fmt(dp1)}}}{{{_fmt(dt)}}} = -{_fmt(f_net)}\\text{{ N}}$$\n"
        f"   Force is **{_fmt(f_net)}\\text{{ N}} west**.\n"
        f"4. By **Newton's Third Law of Motion**, the force exerted by the patrol car on the van is equal in magnitude and opposite in direction: "
        f"**{_fmt(f_net)}\\text{{ N}} east**."
    )
    return _make_q(
        r, "49_capstone_momentum_and_impulse_exam_rider", 49, prompt, ans, sol, 6,
        ["failed_to_apply_newtons_third_law_for_paired_reaction_force"],
        [{"step": 1, "criterion": "Statement of conservation of linear momentum", "marks": 1}, {"step": 2, "criterion": f"Coupled velocity = {_fmt(vf)} m·s⁻¹ east", "marks": 2}, {"step": 3, "criterion": f"Force on car = {_fmt(f_net)} N west", "marks": 2}, {"step": 4, "criterion": f"Force on van = {_fmt(f_net)} N east (Newton's 3rd Law)", "marks": 1}],
        {"tier_1": "Find combined velocity using momentum conservation.", "tier_2": "Calculate F_net = m*(vf - vi) / Δt for the patrol car.", "tier_3": ans},
    )


# 50. Momentum and impulse diagnostic autopsy and misconception triage
def build_50_momentum_and_impulse_diagnostic_autopsy_and_misconception_triage(r: random.Random) -> Dict[str, Any]:
    cases = [
        (
            "Assuming kinetic energy is always conserved in collisions",
            "A learner is asked whether a car crash where vehicles lock together is elastic. The learner calculates total momentum before and after, finds they are equal, and writes: 'Because momentum is conserved, kinetic energy is also conserved, so the collision is elastic.'",
            "Linear momentum is conserved in all collisions in an isolated system, but kinetic energy is ONLY conserved in elastic collisions. When objects stick together, maximum kinetic energy is transformed into heat, sound, and permanent deformation (an inelastic collision)."
        ),
        (
            "Confusing force with impulse",
            "In an exam question, a learner states: 'An impulse of 500 N was applied to the ball.'",
            "Impulse is force multiplied by time (J = F * Δt), measured in N·s (or kg·m·s⁻¹), NOT in Newtons (N). Newtons is the unit of force, whereas impulse is the change in momentum."
        ),
        (
            "Treating momentum as a scalar in head-on collisions",
            "Two 1000 kg cars approach each other head-on, both at 20 m·s⁻¹. A learner calculates the initial total momentum as: p_total = (1000)(20) + (1000)(20) = 40 000 kg·m·s⁻¹.",
            "Momentum is a vector quantity and directions must be accounted for using signs. If east is positive (+20 m·s⁻¹), the westbound car has velocity -20 m·s⁻¹. The correct total momentum is: p_total = (1000)(20) + (1000)(-20) = 0 kg·m·s⁻¹."
        ),
    ]
    title, err_desc, correction = r.choice(cases)
    prompt = (
        f"**Diagnostic Autopsy:** Review the following common Grade 12 Physical Sciences misconception in Momentum & Impulse:\n\n"
        f"**Learner Error:** {err_desc}\n\n"
        f"1. Identify the fundamental misconception committed by the learner.\n"
        f"2. Provide the scientific correction and state the exact law or rule that was violated."
    )
    ans = correction
    sol = f"1. **Misconception:** {title}.\n2. **Scientific Correction:** {correction}"
    return _make_q(
        r, "50_momentum_and_impulse_diagnostic_autopsy_and_misconception_triage", 50, prompt, ans, sol, 3,
        ["confused_elastic_collision_with_momentum_conservation", "treated_momentum_as_scalar"],
        [{"step": 1, "criterion": f"Identified error: {title}", "marks": 1}, {"step": 2, "criterion": "Underlying physical rule explained", "marks": 1}, {"step": 3, "criterion": "Scientific correction provided", "marks": 1}],
        {"tier_1": "Examine whether vector direction, unit definitions, or energy vs momentum rules were confused.", "tier_2": f"Focus on: {title}.", "tier_3": ans},
    )


ARCHETYPES_26_50 = {
    "26_isolated_system_and_external_forces_definition": build_26_isolated_system_and_external_forces_definition,
    "27_principle_of_conservation_of_linear_momentum_statement": build_27_principle_of_conservation_of_linear_momentum_statement,
    "28_conservation_of_momentum_trolleys_colliding_stick_together": build_28_conservation_of_momentum_trolleys_colliding_stick_together,
    "29_conservation_of_momentum_opposite_direction_head_on_stick": build_29_conservation_of_momentum_opposite_direction_head_on_stick,
    "30_conservation_of_momentum_one_stationary_rebound_apart": build_30_conservation_of_momentum_one_stationary_rebound_apart,
    "31_conservation_of_momentum_both_moving_rebound_apart": build_31_conservation_of_momentum_both_moving_rebound_apart,
    "32_conservation_of_momentum_rear_end_collision_shunting": build_32_conservation_of_momentum_rear_end_collision_shunting,
    "33_elastic_vs_inelastic_collisions_kinetic_energy_test": build_33_elastic_vs_inelastic_collisions_kinetic_energy_test,
    "34_loss_of_kinetic_energy_and_deformation_work": build_34_loss_of_kinetic_energy_and_deformation_work,
    "35_explosion_stationary_object_separating_two_fragments": build_35_explosion_stationary_object_separating_two_fragments,
    "36_explosion_moving_object_separating_in_flight": build_36_explosion_moving_object_separating_in_flight,
    "37_bullet_fired_into_stationary_wooden_block": build_37_bullet_fired_into_stationary_wooden_block,
    "38_bullet_passing_through_wooden_block_with_reduced_speed": build_38_bullet_passing_through_wooden_block_with_reduced_speed,
    "39_ballistic_pendulum_conservation_of_momentum_and_energy_svg": build_39_ballistic_pendulum_conservation_of_momentum_and_energy_svg,
    "40_two_gliders_compressed_spring_release_svg": build_40_two_gliders_compressed_spring_release_svg,
    "41_physics_in_action_car_crumple_zones_and_safety": build_41_physics_in_action_car_crumple_zones_and_safety,
    "42_physics_in_action_airbags_seatbelts_and_padded_dashboards": build_42_physics_in_action_airbags_seatbelts_and_padded_dashboards,
    "43_physics_in_action_arrestor_beds_for_runaway_trucks": build_43_physics_in_action_arrestor_beds_for_runaway_trucks,
    "44_physics_in_action_sports_follow_through_and_catching": build_44_physics_in_action_sports_follow_through_and_catching,
    "45_multi_body_three_object_linear_cascade_collision": build_45_multi_body_three_object_linear_cascade_collision,
    "46_collision_with_frictional_stopping_distance_kinematics": build_46_collision_with_frictional_stopping_distance_kinematics,
    "47_collision_on_inclined_ramp_or_drop": build_47_collision_on_inclined_ramp_or_drop,
    "48_internal_vs_external_forces_system_momentum_conservation": build_48_internal_vs_external_forces_system_momentum_conservation,
    "49_capstone_momentum_and_impulse_exam_rider": build_49_capstone_momentum_and_impulse_exam_rider,
    "50_momentum_and_impulse_diagnostic_autopsy_and_misconception_triage": build_50_momentum_and_impulse_diagnostic_autopsy_and_misconception_triage,
}

BUILDERS_26_50 = ARCHETYPES_26_50
