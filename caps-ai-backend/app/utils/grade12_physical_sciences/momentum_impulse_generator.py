"""Grade 12 Physical Sciences — Momentum and Impulse (Paper 1 Physics).
100% Deterministic & Zero-LLM AST Pure. Satisfies the 6-Pillar Generator Contract.
Covers authentic CAPS Grade 12 Physical Sciences examination standards:
- Compound 6-mark question: 1D linear momentum conservation in collisions
  (Sigma p_i = Sigma p_f => m1*v1i + m2*v2i = (m1 + m2)*vf or m1*v1f + m2*v2f),
  with explicit direction declarations, vector signs, and kinetic energy test for elasticity
  (Sigma Ek(i) vs Sigma Ek(f)).
- Compound 5-mark question: Impulse and Newton's Second Law in terms of momentum
  (F_net * delta_t = delta_p = m*(vf - vi)) with safety/fatality force threshold analysis.
- Elementary sub-drills for adaptive scaffolding:
  - elementary_momentum (p = m*v)
  - elementary_change_momentum (delta_p = m*delta_v = m*(vf - vi))
  - elementary_impulse (Impulse = F_net * delta_t)
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    """Format decimal number using South African comma decimal convention."""
    if isinstance(val, (int, float)) and float(val).is_integer():
        return str(int(val))
    s = f"{float(val):.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


# ============================================================================ #
# 1. ELEMENTARY SUB-DRILL: p = mv (3 MARKS)
# ============================================================================ #

def _build_elementary_momentum(r: random.Random) -> Dict[str, Any]:
    """Elementary Drill: Linear Momentum calculation (p = mv)."""
    scenarios = [
        {"item": "Springbok rugby player", "mass_kg": r.choice([92, 98, 105, 112]), "v": r.choice([6.0, 7.5, 8.0, 8.5]), "unit_conv": False},
        {"item": "delivery motorcycle", "mass_kg": r.choice([160, 180, 210, 240]), "v": r.choice([15.0, 20.0, 22.5, 25.0]), "unit_conv": False},
        {"item": "cricket ball", "mass_g": r.choice([150, 156, 160]), "v": r.choice([25.0, 30.0, 35.0, 38.0]), "unit_conv": True},
        {"item": "patrol car", "mass_kg": r.choice([1200, 1400, 1500, 1650]), "v": r.choice([18.0, 20.0, 24.0, 28.0]), "unit_conv": False},
        {"item": "soccer ball", "mass_g": r.choice([420, 440, 450]), "v": r.choice([18.0, 22.0, 24.0, 26.0]), "unit_conv": True},
    ]
    scen = r.choice(scenarios)
    direction = r.choice(["east", "north", "to the right", "forward"])
    
    if scen["unit_conv"]:
        mass_g = scen["mass_g"]
        mass_kg = mass_g / 1000.0
        mass_desc = f"{mass_g} g"
        conv_step = rf"m = \frac{{{mass_g}}}{{1000}} = {_fmt_sa(mass_kg)}\text{{ kg}}\\"
    else:
        mass_kg = float(scen["mass_kg"])
        mass_desc = f"{_fmt_sa(mass_kg)} kg"
        conv_step = ""

    velocity = scen["v"]
    p_val = round(mass_kg * velocity, 2)
    
    prompt = (
        f"A {scen['item']} of mass {mass_desc} travels at a constant velocity of "
        f"{_fmt_sa(velocity)} m·s⁻¹ {direction}.\n\n"
        f"Calculate the linear momentum of the {scen['item']}."
    )
    
    sample_answer = (
        rf"{conv_step}"
        rf"p = m v\\"
        rf"p = ({_fmt_sa(mass_kg)})({_fmt_sa(velocity)}) = {_fmt_sa(p_val)}\text{{ kg}}\cdot\text{{m}}\cdot\text{{s}}^{{-1}}\text{{ {direction}}}"
    )

    return {
        "id": f"phys_mom_elem_{r.randint(100000, 999999)}",
        "topic": "Momentum and Impulse",
        "subskill": "elementary_momentum",
        "mode": "elementary_momentum",
        "difficulty": "easy",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "marks": 3,
        "prompt": prompt,
        "ideal_answer": f"{_fmt_sa(p_val)} kg·m·s⁻¹ {direction}",
        "sample_answer": sample_answer,
        "misconception_tags": [
            "forgot_to_convert_grams_to_kg",
            "omitted_vector_direction",
            "inverted_momentum_formula"
        ],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_formula", "desc": "[M] Formula p = mv from CAPS Data Sheet", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": f"[M] Substitution of mass ({_fmt_sa(mass_kg)} kg) and velocity ({_fmt_sa(velocity)} m·s⁻¹)", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"[A] Final answer with correct magnitude, unit and direction: {_fmt_sa(p_val)} kg·m·s⁻¹ {direction}", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "omitted_or_wrong_unit", "penalty": -1},
                {"rule": "omitted_vector_direction", "penalty": -1}
            ],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Recall that linear momentum is the product of an object's mass and its velocity. Check if the mass needs to be in kilograms.",
            "tier_2": f"Use the official CAPS formula $p = mv$. Ensure mass is in kg: divide grams by 1 000 if applicable. Remember momentum is a vector quantity having the same direction as velocity.",
            "tier_3": f"Mass = {_fmt_sa(mass_kg)} kg, velocity = {_fmt_sa(velocity)} m·s⁻¹ {direction}. $p = ({_fmt_sa(mass_kg)})({_fmt_sa(velocity)}) = {_fmt_sa(p_val)}$ kg·m·s⁻¹ {direction}."
        }
    }


# ============================================================================ #
# 2. ELEMENTARY SUB-DRILL: delta_p = m(vf - vi) (3 MARKS)
# ============================================================================ #

def _build_elementary_change_momentum(r: random.Random) -> Dict[str, Any]:
    """Elementary Drill: Change in momentum with vector sign reversal."""
    ball_types = [
        {"name": "tennis ball", "mass_kg": 0.06, "vi": r.choice([16.0, 18.0, 20.0, 22.0]), "vf": r.choice([12.0, 14.0, 15.0])},
        {"name": "cricket ball", "mass_kg": 0.16, "vi": r.choice([24.0, 28.0, 30.0, 32.0]), "vf": r.choice([18.0, 20.0, 22.0])},
        {"name": "squash ball", "mass_kg": 0.024, "vi": r.choice([25.0, 30.0, 35.0]), "vf": r.choice([15.0, 20.0, 22.0])},
        {"name": "soccer ball", "mass_kg": 0.45, "vi": r.choice([15.0, 18.0, 20.0]), "vf": r.choice([10.0, 12.0, 14.0])},
    ]
    b = r.choice(ball_types)
    m = b["mass_kg"]
    vi = b["vi"]
    vf = b["vf"] # magnitude of rebound

    pos_dir = r.choice(["right", "east"])
    neg_dir = "left" if pos_dir == "right" else "west"

    # Initial motion is in positive direction, rebounds in negative direction
    # vi_vec = +vi, vf_vec = -vf
    delta_p = round(m * ((-vf) - (+vi)), 3)
    mag_delta_p = abs(delta_p)

    prompt = (
        f"A {b['name']} of mass {_fmt_sa(m)} kg moves horizontally to the {pos_dir} at "
        f"{_fmt_sa(vi)} m·s⁻¹. It strikes a vertical wall and rebounds horizontally to the {neg_dir} at "
        f"{_fmt_sa(vf)} m·s⁻¹.\n\n"
        f"Taking motion to the {pos_dir} as positive, calculate the change in momentum (Δp) of the {b['name']}."
    )

    sample_answer = (
        rf"\text{{Taking {pos_dir} as positive:}}\\"
        rf"\Delta p = m(v_f - v_i)\\"
        rf"\Delta p = ({_fmt_sa(m)})((- {_fmt_sa(vf)}) - (+ {_fmt_sa(vi)}))\\"
        rf"\Delta p = ({_fmt_sa(m)})(- {_fmt_sa(vf + vi)}) = - {_fmt_sa(mag_delta_p)}\text{{ kg}}\cdot\text{{m}}\cdot\text{{s}}^{{-1}}\\"
        rf"\therefore \Delta p = {_fmt_sa(mag_delta_p)}\text{{ kg}}\cdot\text{{m}}\cdot\text{{s}}^{{-1}}\text{{ to the {neg_dir}}}"
    )

    return {
        "id": f"phys_mom_chgp_{r.randint(100000, 999999)}",
        "topic": "Momentum and Impulse",
        "subskill": "elementary_change_momentum",
        "mode": "elementary_change_momentum",
        "difficulty": "medium",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "marks": 3,
        "prompt": prompt,
        "ideal_answer": f"{_fmt_sa(mag_delta_p)} kg·m·s⁻¹ to the {neg_dir}",
        "sample_answer": sample_answer,
        "misconception_tags": [
            "scalar_subtraction_ignored_direction_change",
            "confused_initial_and_final_velocities",
            "omitted_vector_direction"
        ],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_formula", "desc": "[M] Formula Δp = m(vf - vi) or Δp = pf - pi", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": f"[M] Correct substitution with opposite vector signs: ({_fmt_sa(m)})(-{_fmt_sa(vf)} - (+{_fmt_sa(vi)}))", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"[A] Final answer with magnitude, unit and direction: {_fmt_sa(mag_delta_p)} kg·m·s⁻¹ to the {neg_dir}", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "omitted_or_wrong_unit", "penalty": -1},
                {"rule": "omitted_vector_direction", "penalty": -1}
            ],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Velocity is a vector quantity. Because the ball rebounds in the opposite direction, its final velocity has a negative sign.",
            "tier_2": f"Use $\\Delta p = m(v_f - v_i)$. If {pos_dir} is positive, then $v_i = +{_fmt_sa(vi)}$ m·s⁻¹ and $v_f = -{_fmt_sa(vf)}$ m·s⁻¹.",
            "tier_3": f"$\\Delta p = ({_fmt_sa(m)})(-{_fmt_sa(vf)} - (+{_fmt_sa(vi)})) = ({_fmt_sa(m)})(-{_fmt_sa(vf + vi)}) = -{_fmt_sa(mag_delta_p)}$ kg·m·s⁻¹, which means {_fmt_sa(mag_delta_p)} kg·m·s⁻¹ to the {neg_dir}."
        }
    }


# ============================================================================ #
# 3. ELEMENTARY SUB-DRILL: Impulse = F_net * delta_t (3 MARKS)
# ============================================================================ #

def _build_elementary_impulse(r: random.Random) -> Dict[str, Any]:
    """Elementary Drill: Impulse of a constant net force (Impulse = F_net * delta_t)."""
    scenarios = [
        {"context": "trolley on a horizontal air track", "f_net": r.choice([120, 180, 250, 360, 450]), "dt": r.choice([0.15, 0.20, 0.25, 0.35, 0.40])},
        {"context": "ice hockey puck struck by a stick", "f_net": r.choice([200, 300, 400, 500]), "dt": r.choice([0.05, 0.08, 0.10, 0.12])},
        {"context": "toy rocket during launch thruster phase", "f_net": r.choice([80, 140, 220, 320]), "dt": r.choice([0.30, 0.45, 0.50, 0.60])},
        {"context": "rugby ball during a place kick", "f_net": r.choice([350, 480, 600, 720]), "dt": r.choice([0.04, 0.05, 0.06, 0.08])},
    ]
    scen = r.choice(scenarios)
    direction = r.choice(["east", "west", "to the right", "forward"])
    f_net = scen["f_net"]
    dt = scen["dt"]
    impulse = round(f_net * dt, 2)

    prompt = (
        f"A constant net horizontal force of {_fmt_sa(f_net)} N acts {direction} on a {scen['context']} "
        f"for a time interval of {_fmt_sa(dt)} s.\n\n"
        f"Calculate the impulse of the net force acting on the object."
    )

    sample_answer = (
        rf"\text{{Impulse}} = F_{{\text{{net}}}} \Delta t\\"
        rf"\text{{Impulse}} = ({_fmt_sa(f_net)})({_fmt_sa(dt)}) = {_fmt_sa(impulse)}\text{{ N}}\cdot\text{{s}}\text{{ {direction}}} "
        rf"\quad (\text{{or }}{_fmt_sa(impulse)}\text{{ kg}}\cdot\text{{m}}\cdot\text{{s}}^{{-1}}\text{{ {direction}}})"
    )

    return {
        "id": f"phys_mom_elem_imp_{r.randint(100000, 999999)}",
        "topic": "Momentum and Impulse",
        "subskill": "elementary_impulse",
        "mode": "elementary_impulse",
        "difficulty": "easy",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "marks": 3,
        "prompt": prompt,
        "ideal_answer": f"{_fmt_sa(impulse)} N·s {direction}",
        "sample_answer": sample_answer,
        "misconception_tags": [
            "divided_force_by_time",
            "omitted_direction_in_impulse",
            "confused_impulse_with_force"
        ],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_formula", "desc": "[M] Formula Impulse = F_net * Δt", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": f"[M] Substitution of F_net ({_fmt_sa(f_net)} N) and Δt ({_fmt_sa(dt)} s)", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"[A] Final answer with unit (N·s or kg·m·s⁻¹) and direction: {_fmt_sa(impulse)} N·s {direction}", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "omitted_or_wrong_unit", "penalty": -1},
                {"rule": "omitted_vector_direction", "penalty": -1}
            ],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Impulse is defined as the product of the net force and the time interval during which it acts.",
            "tier_2": f"Use the formula $\\text{{Impulse}} = F_{{\\text{{net}}}} \\Delta t$. Impulse is a vector quantity that has the same direction as the net force.",
            "tier_3": f"$\\text{{Impulse}} = ({_fmt_sa(f_net)})({_fmt_sa(dt)}) = {_fmt_sa(impulse)}$ N·s {direction}."
        }
    }


# ============================================================================ #
# 4. COMPOUND 5-MARK QUESTION: IMPULSE & NEWTON'S 2ND LAW
# ============================================================================ #

def _build_compound_impulse(r: random.Random) -> Dict[str, Any]:
    """Compound 5-mark Question: Impulse and Newton's Second Law in terms of momentum.
    Includes vehicle crash safety / fatality force threshold calculation.
    """
    variant = r.choice(["vehicle_barrier_crash", "cricket_batsman_strike"])
    
    if variant == "vehicle_barrier_crash":
        vehicles = [
            {"type": "passenger car", "mass": r.choice([1000, 1100, 1200, 1250]), "vi": r.choice([20.0, 25.0, 30.0]), "vf_rebound": r.choice([2.0, 3.0, 4.0])},
            {"type": "minibus taxi", "mass": r.choice([1800, 2000, 2200]), "vi": r.choice([18.0, 20.0, 22.0]), "vf_rebound": r.choice([2.0, 2.5, 3.0])},
            {"type": "delivery bakkie", "mass": r.choice([1400, 1500, 1600]), "vi": r.choice([22.0, 24.0, 26.0]), "vf_rebound": r.choice([3.0, 4.0])},
        ]
        veh = r.choice(vehicles)
        mass = veh["mass"]
        vi = veh["vi"]
        vf_rebound = veh["vf_rebound"]
        dt = r.choice([0.15, 0.20, 0.25])
        
        pos_dir = "east"
        neg_dir = "west"

        # vi is east (+), vf is rebound west (-)
        # F_net * dt = m*(vf - vi)
        delta_p = mass * ((-vf_rebound) - (+vi))
        f_net = round(delta_p / dt, 1)
        f_net_mag = abs(f_net)
        
        # Fatality threshold (typically ~85 000 N to 120 000 N in biomechanical research)
        f_threshold = r.choice([80000, 85000, 90000, 100000])
        is_fatal = f_net_mag > f_threshold

        prompt = (
            f"A {veh['type']} of mass {_fmt_sa(mass)} kg is travelling {pos_dir} on a straight horizontal road at "
            f"{_fmt_sa(vi)} m·s⁻¹. It collides head-on with a solid concrete barrier and rebounds at "
            f"{_fmt_sa(vf_rebound)} m·s⁻¹ {neg_dir}. The collision lasts for a contact duration of {_fmt_sa(dt)} s.\n\n"
            f"1. Taking {pos_dir} as positive, calculate the magnitude and direction of the average net force (F_net) "
            f"exerted on the {veh['type']} during the collision. (4 marks)\n\n"
            f"2. Biomechanical research indicates that collision forces exceeding {_fmt_sa(f_threshold)} N can result in "
            f"fatal injuries to vehicle occupants. Determine, by comparing your answer to Question 1 with this threshold, "
            f"whether this collision could be fatal. (1 mark)"
        )

        fatal_verdict = (
            f"Yes, the collision could be fatal because the magnitude of the net force ({_fmt_sa(f_net_mag)} N) "
            f"is greater than the safety threshold of {_fmt_sa(f_threshold)} N."
            if is_fatal else
            f"No, the collision is non-fatal because the magnitude of the net force ({_fmt_sa(f_net_mag)} N) "
            f"does not exceed the safety threshold of {_fmt_sa(f_threshold)} N."
        )

        sample_answer = (
            rf"\textbf{{1. Net force on the vehicle:}}\\"
            rf"\text{{Taking {pos_dir} as positive:}}\\"
            rf"F_{{\text{{net}}}} \Delta t = \Delta p = m(v_f - v_i)\\"
            rf"F_{{\text{{net}}}} ({_fmt_sa(dt)}) = ({_fmt_sa(mass)})((- {_fmt_sa(vf_rebound)}) - (+ {_fmt_sa(vi)}))\\"
            rf"F_{{\text{{net}}}} ({_fmt_sa(dt)}) = ({_fmt_sa(mass)})(- {_fmt_sa(vf_rebound + vi)}) = {_fmt_sa(delta_p)}\text{{ kg}}\cdot\text{{m}}\cdot\text{{s}}^{{-1}}\\"
            rf"F_{{\text{{net}}}} = \frac{{{_fmt_sa(delta_p)}}}{{{_fmt_sa(dt)}}} = - {_fmt_sa(f_net_mag)}\text{{ N}}\\"
            rf"\therefore F_{{\text{{net}}}} = {_fmt_sa(f_net_mag)}\text{{ N {neg_dir}}}\\\\"
            rf"\textbf{{2. Safety assessment:}}\\"
            rf"|F_{{\text{{net}}}}| = {_fmt_sa(f_net_mag)}\text{{ N}} "
            rf"{' > ' if is_fatal else ' \\le '} {_fmt_sa(f_threshold)}\text{{ N}}\\"
            rf"\therefore \text{{{fatal_verdict}}}"
        )

        marking_schema = {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_fnet_formula", "desc": "[M] Formula F_net * Δt = Δp = m(vf - vi) from CAPS Data Sheet", "marks": 1, "editable": True},
                {"id": "mp_fnet_sub_signs", "desc": f"[M] Substitution with correct vector signs: ({_fmt_sa(mass)})(-{_fmt_sa(vf_rebound)} - (+{_fmt_sa(vi)}))", "marks": 1, "editable": True},
                {"id": "mp_fnet_sub_dt", "desc": f"[M] Substitution of contact time Δt = {_fmt_sa(dt)} s", "marks": 1, "editable": True},
                {"id": "mp_fnet_ans", "desc": f"[A] Final force magnitude, unit and direction: {_fmt_sa(f_net_mag)} N {neg_dir}", "marks": 1, "editable": True},
                {"id": "mp_fatal_deduction", "desc": f"[A] Correct deduction comparing {_fmt_sa(f_net_mag)} N to {_fmt_sa(f_threshold)} N: {'Fatal' if is_fatal else 'Non-fatal'}", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "omitted_or_wrong_unit", "penalty": -1},
                {"rule": "omitted_vector_direction", "penalty": -1}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }

        hints = {
            "tier_1": f"Use Newton's Second Law expressed in terms of momentum: $F_{{\\text{{net}}}} \\Delta t = \\Delta p = m(v_f - v_i)$. Pay careful attention to the signs when the vehicle rebounds.",
            "tier_2": f"Taking {pos_dir} as positive: $v_i = +{_fmt_sa(vi)}$ m·s⁻¹ and $v_f = -{_fmt_sa(vf_rebound)}$ m·s⁻¹. Substitute into $F_{{\\text{{net}}}}(\\Delta t) = m(v_f - v_i)$ and solve for $F_{{\\text{{net}}}}$. Then compare $|F_{{\\text{{net}}}}|$ with the threshold {_fmt_sa(f_threshold)} N.",
            "tier_3": f"$F_{{\\text{{net}}}}({_fmt_sa(dt)}) = ({_fmt_sa(mass)})(-{_fmt_sa(vf_rebound)} - (+{_fmt_sa(vi)})) = {_fmt_sa(delta_p)}$. $F_{{\\text{{net}}}} = {_fmt_sa(delta_p)} / {_fmt_sa(dt)} = -{_fmt_sa(f_net_mag)}$ N ({_fmt_sa(f_net_mag)} N {neg_dir}). Since {_fmt_sa(f_net_mag)} N {' > ' if is_fatal else ' <= '} {_fmt_sa(f_threshold)} N, the collision {'could be fatal' if is_fatal else 'is non-fatal'}."
        }

    else:
        # variant == "cricket_batsman_strike"
        mass_g = r.choice([156, 160])
        mass = mass_g / 1000.0
        vi = r.choice([30.0, 32.0, 35.0, 40.0]) # towards batsman (south)
        vf = r.choice([20.0, 24.0, 25.0, 28.0]) # back to bowler (north)
        dt = r.choice([0.02, 0.025, 0.03])
        
        pos_dir = "north"
        neg_dir = "south"
        
        # vi is south (-), vf is north (+)
        delta_p = round(mass * ((+vf) - (-vi)), 3)
        f_net = round(delta_p / dt, 1)
        
        prompt = (
            f"A cricket ball of mass {mass_g} g is bowled towards a batsman at a speed of {_fmt_sa(vi)} m·s⁻¹ {neg_dir}. "
            f"The batsman hits the ball straight back towards the bowler at a speed of {_fmt_sa(vf)} m·s⁻¹ {pos_dir}. "
            f"The cricket bat remains in contact with the ball for {_fmt_sa(dt)} s.\n\n"
            f"1. Taking {pos_dir} as positive, calculate the change in momentum (Δp) of the cricket ball. (3 marks)\n\n"
            f"2. Calculate the magnitude and direction of the average net force (F_net) exerted by the bat on the ball. (2 marks)"
        )

        sample_answer = (
            rf"\textbf{{1. Change in momentum:}}\\"
            rf"\text{{Convert mass to kg: }} m = \frac{{{mass_g}}}{{1000}} = {_fmt_sa(mass)}\text{{ kg}}\\"
            rf"\text{{Taking {pos_dir} as positive:}}\\"
            rf"\Delta p = m(v_f - v_i)\\"
            rf"\Delta p = ({_fmt_sa(mass)})((+ {_fmt_sa(vf)}) - (- {_fmt_sa(vi)}))\\"
            rf"\Delta p = ({_fmt_sa(mass)})({_fmt_sa(vf + vi)}) = + {_fmt_sa(delta_p)}\text{{ kg}}\cdot\text{{m}}\cdot\text{{s}}^{{-1}}\\"
            rf"\therefore \Delta p = {_fmt_sa(delta_p)}\text{{ kg}}\cdot\text{{m}}\cdot\text{{s}}^{{-1}}\text{{ {pos_dir}}}\\\\"
            rf"\textbf{{2. Average net force:}}\\"
            rf"F_{{\text{{net}}}} \Delta t = \Delta p \implies F_{{\text{{net}}}} = \frac{{\Delta p}}{{\Delta t}}\\"
            rf"F_{{\text{{net}}}} = \frac{{{_fmt_sa(delta_p)}}}{{{_fmt_sa(dt)}}} = {_fmt_sa(f_net)}\text{{ N {pos_dir}}}"
        )

        marking_schema = {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_dp_formula", "desc": "[M] Formula Δp = m(vf - vi) with mass converted to kg", "marks": 1, "editable": True},
                {"id": "mp_dp_sub", "desc": f"[M] Substitution with correct opposite vector signs: ({_fmt_sa(mass)})({_fmt_sa(vf)} - (-{_fmt_sa(vi)}))", "marks": 1, "editable": True},
                {"id": "mp_dp_ans", "desc": f"[A] Change in momentum with unit and direction: {_fmt_sa(delta_p)} kg·m·s⁻¹ {pos_dir}", "marks": 1, "editable": True},
                {"id": "mp_fnet_formula", "desc": "[M] Formula F_net * Δt = Δp or F_net = Δp / Δt", "marks": 1, "editable": True},
                {"id": "mp_fnet_ans", "desc": f"[A] Net force with unit and direction: {_fmt_sa(f_net)} N {pos_dir}", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "omitted_or_wrong_unit", "penalty": -1},
                {"rule": "omitted_vector_direction", "penalty": -1}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }

        hints = {
            "tier_1": f"First convert mass from grams to kilograms ({mass_g} g = {_fmt_sa(mass)} kg). Remember that the ball rebounds in the opposite direction.",
            "tier_2": f"Taking {pos_dir} as positive: $v_i = -{_fmt_sa(vi)}$ m·s⁻¹ and $v_f = +{_fmt_sa(vf)}$ m·s⁻¹. Use $\\Delta p = m(v_f - v_i)$. Then use $F_{{\\text{{net}}}} = \\frac{{\\Delta p}}{{\\Delta t}}$.",
            "tier_3": f"$\\Delta p = ({_fmt_sa(mass)})(+{_fmt_sa(vf)} - (-{_fmt_sa(vi)})) = {_fmt_sa(delta_p)}$ kg·m·s⁻¹ {pos_dir}. $F_{{\\text{{net}}}} = {_fmt_sa(delta_p)} / {_fmt_sa(dt)} = {_fmt_sa(f_net)}$ N {pos_dir}."
        }

    return {
        "id": f"phys_mom_cmpd_imp_{r.randint(100000, 999999)}",
        "topic": "Momentum and Impulse",
        "subskill": "impulse_newton_second_law",
        "mode": "compound",
        "difficulty": "hard",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 7,
        "marks": 5,
        "prompt": prompt,
        "ideal_answer": f"F_net = {_fmt_sa(f_net if variant == 'cricket_batsman_strike' else f_net_mag)} N",
        "sample_answer": sample_answer,
        "misconception_tags": [
            "ignored_vector_sign_in_rebound",
            "confused_impulse_with_force",
            "omitted_vector_direction"
        ],
        "marking_schema": marking_schema,
        "hints": hints
    }


# ============================================================================ #
# 5. COMPOUND 6-MARK QUESTION: 1D COLLISION & ELASTICITY TEST
# ============================================================================ #

def _build_compound_collision(r: random.Random) -> Dict[str, Any]:
    """Compound 6-mark Question: 1D Linear Momentum Conservation & Kinetic Energy Elasticity Test.
    Sigma p_i = Sigma p_f => m1*v1i + m2*v2i = (m1 + m2)*vf (inelastic) or m1*v1f + m2*v2f (elastic).
    Sub-question 1 (4 marks): Post-collision velocity with direction.
    Sub-question 2 (2 marks): Kinetic energy calculation and elasticity classification.
    """
    collision_type = r.choice(["inelastic_coalescing", "elastic_billiard"])

    if collision_type == "inelastic_coalescing":
        # Two vehicles collide and stick together
        scenarios = [
            {
                "obj1": "minibus taxi", "m1": 2000, "v1i": 25.0,
                "obj2": "passenger car", "m2": 1000, "v2i": -20.0,
                "dir_pos": "east", "dir_neg": "west"
            },
            {
                "obj1": "delivery truck", "m1": 4500, "v1i": 20.0,
                "obj2": "sedan", "m2": 1500, "v2i": -10.0,
                "dir_pos": "east", "dir_neg": "west"
            },
            {
                "obj1": "heavy bakkie", "m1": 1800, "v1i": 30.0,
                "obj2": "hatchback", "m2": 1200, "v2i": -15.0,
                "dir_pos": "east", "dir_neg": "west"
            },
            {
                "obj1": "freight truck A", "m1": 5000, "v1i": 18.0,
                "obj2": "freight truck B", "m2": 3000, "v2i": -10.0,
                "dir_pos": "right", "dir_neg": "left"
            },
            {
                "obj1": "patrol vehicle", "m1": 1600, "v1i": 28.0,
                "obj2": "suspect vehicle", "m2": 1400, "v2i": -14.0,
                "dir_pos": "east", "dir_neg": "west"
            },
        ]
        scen = r.choice(scenarios)
        m1 = scen["m1"]
        v1i = scen["v1i"]
        m2 = scen["m2"]
        v2i = scen["v2i"] # negative in positive frame
        pos_dir = scen["dir_pos"]
        neg_dir = scen["dir_neg"]

        # Total initial momentum: p_total_i = m1*v1i + m2*v2i
        p_total_i = round(m1 * v1i + m2 * v2i, 1)
        m_total = m1 + m2
        vf = round(p_total_i / m_total, 2)
        vf_mag = abs(vf)
        final_dir = pos_dir if vf >= 0 else neg_dir

        # Kinetic energy calculations
        # Ek_initial = 0.5 * m1 * v1i^2 + 0.5 * m2 * v2i^2
        ek_1i = round(0.5 * m1 * (v1i ** 2), 2)
        ek_2i = round(0.5 * m2 * (abs(v2i) ** 2), 2)
        ek_total_i = round(ek_1i + ek_2i, 2)

        # Ek_final = 0.5 * (m1 + m2) * vf^2
        ek_total_f = round(0.5 * m_total * (vf ** 2), 2)
        delta_ek = round(ek_total_f - ek_total_i, 2)

        prompt = (
            f"A {scen['obj1']} of mass {_fmt_sa(m1)} kg is travelling {pos_dir} at a constant velocity of "
            f"{_fmt_sa(v1i)} m·s⁻¹. It collides head-on on a straight horizontal road with a {scen['obj2']} of mass "
            f"{_fmt_sa(m2)} kg travelling {neg_dir} at a velocity of {_fmt_sa(abs(v2i))} m·s⁻¹.\n\n"
            f"During the collision, the two vehicles lock together and move off as a single combined unit.\n\n"
            f"1. Taking motion to the {pos_dir} as positive, calculate the velocity of the combined vehicle wreckage "
            f"immediately after the collision. (4 marks)\n\n"
            f"2. Determine, by means of calculations of the total kinetic energy of the system before and after the collision, "
            f"whether this collision is ELASTIC or INELASTIC. (2 marks)"
        )

        sample_answer = (
            rf"\textbf{{1. Velocity of wreckage after collision:}}\\"
            rf"\text{{Taking {pos_dir} as positive:}}\\"
            rf"\sum p_i = \sum p_f\\"
            rf"m_1 v_{{1i}} + m_2 v_{{2i}} = (m_1 + m_2) v_f\\"
            rf"({_fmt_sa(m1)})({_fmt_sa(v1i)}) + ({_fmt_sa(m2)})(- {_fmt_sa(abs(v2i))}) = ({_fmt_sa(m1)} + {_fmt_sa(m2)}) v_f\\"
            rf"{_fmt_sa(round(m1 * v1i, 1))} + ({_fmt_sa(round(m2 * v2i, 1))}) = ({_fmt_sa(m_total)}) v_f\\"
            rf"{_fmt_sa(p_total_i)} = {_fmt_sa(m_total)} v_f\\"
            rf"v_f = \frac{{{_fmt_sa(p_total_i)}}}{{{_fmt_sa(m_total)}}} = {_fmt_sa(vf)}\text{{ m}}\cdot\text{{s}}^{{-1}}\\"
            rf"\therefore v_f = {_fmt_sa(vf_mag)}\text{{ m}}\cdot\text{{s}}^{{-1}}\text{{ {final_dir}}}\\\\"
            rf"\textbf{{2. Elasticity determination:}}\\"
            rf"\sum E_{{ki}} = \frac{{1}}{{2}} m_1 v_{{1i}}^2 + \frac{{1}}{{2}} m_2 v_{{2i}}^2\\"
            rf"\sum E_{{ki}} = \frac{{1}}{{2}}({_fmt_sa(m1)})({_fmt_sa(v1i)})^2 + \frac{{1}}{{2}}({_fmt_sa(m2)})({_fmt_sa(abs(v2i))})^2\\"
            rf"\sum E_{{ki}} = {_fmt_sa(ek_1i)} + {_fmt_sa(ek_2i)} = {_fmt_sa(ek_total_i)}\text{{ J}}\\"
            rf"\sum E_{{kf}} = \frac{{1}}{{2}} (m_1 + m_2) v_f^2 = \frac{{1}}{{2}} ({_fmt_sa(m_total)}) ({_fmt_sa(vf)})^2 = {_fmt_sa(ek_total_f)}\text{{ J}}\\"
            rf"\text{{Since }}\sum E_{{ki}} \neq \sum E_{{kf}} \text{{ (}}\sum E_{{kf}} < \sum E_{{ki}}\text{{), the collision is }}\textbf{{INELASTIC}}."
        )

        marking_schema = {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_p_formula", "desc": "[M] Formula Σp_i = Σp_f or m1*v1i + m2*v2i = (m1 + m2)*vf", "marks": 1, "editable": True},
                {"id": "mp_p_sub_init", "desc": f"[M] Substitution of initial values with vector signs: ({_fmt_sa(m1)})({_fmt_sa(v1i)}) + ({_fmt_sa(m2)})(-{_fmt_sa(abs(v2i))})", "marks": 1, "editable": True},
                {"id": "mp_p_sub_fin", "desc": f"[M] Substitution of combined mass ({_fmt_sa(m_total)}) * vf", "marks": 1, "editable": True},
                {"id": "mp_p_ans", "desc": f"[A] Final velocity magnitude, unit and direction: {_fmt_sa(vf_mag)} m·s⁻¹ {final_dir}", "marks": 1, "editable": True},
                {"id": "mp_ek_calc", "desc": f"[M] Correct calculation of ΣEk(i) = {_fmt_sa(ek_total_i)} J and ΣEk(f) = {_fmt_sa(ek_total_f)} J", "marks": 1, "editable": True},
                {"id": "mp_ek_deduction", "desc": "[A] Correct conclusion with valid justification: ΣEk(i) != ΣEk(f) hence collision is INELASTIC", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "omitted_or_wrong_unit", "penalty": -1},
                {"rule": "omitted_vector_direction", "penalty": -1}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }

        hints = {
            "tier_1": f"Apply the Principle of Conservation of Linear Momentum: total momentum before equals total momentum after in an isolated system. Remember to assign signs according to the chosen positive direction.",
            "tier_2": f"Taking {pos_dir} as positive: $m_1 v_{{1i}} + m_2 v_{{2i}} = (m_1 + m_2) v_f$. Substitute $v_{{2i}} = -{_fmt_sa(abs(v2i))}$ m·s⁻¹. For Question 2, calculate total initial $E_k = \\frac{{1}}{{2}}m_1 v_{{1i}}^2 + \\frac{{1}}{{2}}m_2 v_{{2i}}^2$ and final $E_k = \\frac{{1}}{{2}}(m_1+m_2)v_f^2$. If they are not equal, it is inelastic.",
            "tier_3": f"Initial momentum = $({_fmt_sa(m1)})({_fmt_sa(v1i)}) + ({_fmt_sa(m2)})(-{_fmt_sa(abs(v2i))}) = {_fmt_sa(p_total_i)}$ kg·m·s⁻¹. $v_f = {_fmt_sa(p_total_i)} / {_fmt_sa(m_total)} = {_fmt_sa(vf)}$ m·s⁻¹ {final_dir}. Total $E_{{ki}} = {_fmt_sa(ek_total_i)}$ J, $E_{{kf}} = {_fmt_sa(ek_total_f)}$ J. Since $E_{{kf}} \\neq E_{{ki}}$, the collision is INELASTIC."
        }

        ideal_ans = f"vf = {_fmt_sa(vf_mag)} m·s⁻¹ {final_dir}; INELASTIC"

    else:
        # collision_type == "elastic_billiard"
        # Two laboratory trolleys or steel spheres collide elastically
        scenarios = [
            {"obj1": "Trolley A", "m1": 2.0, "v1i": 5.0, "obj2": "Trolley B", "m2": 3.0, "v2i": 0.0, "v1f": -1.0, "v2f": 4.0},
            {"obj1": "Steel Sphere A", "m1": 0.5, "v1i": 6.0, "obj2": "Steel Sphere B", "m2": 1.0, "v2i": 0.0, "v1f": -2.0, "v2f": 4.0},
            {"obj1": "Billiard Ball 1", "m1": 0.3, "v1i": 4.0, "obj2": "Billiard Ball 2", "m2": 0.3, "v2i": -2.0, "v1f": -2.0, "v2f": 4.0},
            {"obj1": "Dynamic Cart 1", "m1": 1.0, "v1i": 3.0, "obj2": "Dynamic Cart 2", "m2": 2.0, "v2i": 0.0, "v1f": -1.0, "v2f": 2.0},
        ]
        scen = r.choice(scenarios)
        m1 = scen["m1"]
        v1i = scen["v1i"]
        m2 = scen["m2"]
        v2i = scen["v2i"]
        v1f = scen["v1f"]
        v2f = scen["v2f"]
        
        pos_dir = "right"
        neg_dir = "left"

        v1f_dir = pos_dir if v1f >= 0 else neg_dir
        v2f_dir = pos_dir if v2f >= 0 else neg_dir
        
        ek_total_i = round(0.5 * m1 * (v1i ** 2) + 0.5 * m2 * (v2i ** 2), 2)
        ek_total_f = round(0.5 * m1 * (v1f ** 2) + 0.5 * m2 * (v2f ** 2), 2)

        prompt = (
            f"In a physics laboratory experiment on a frictionless horizontal air track, {scen['obj1']} of mass "
            f"{_fmt_sa(m1)} kg travels to the {pos_dir} at {_fmt_sa(v1i)} m·s⁻¹. It collides head-on with "
            f"{scen['obj2']} of mass {_fmt_sa(m2)} kg "
            f"{f'which is initially at rest' if v2i == 0.0 else f'travelling to the {neg_dir} at {_fmt_sa(abs(v2i))} m·s⁻¹'}.\n\n"
            f"After the collision, {scen['obj1']} rebounds to the {v1f_dir} at {_fmt_sa(abs(v1f))} m·s⁻¹.\n\n"
            f"1. Taking motion to the {pos_dir} as positive, calculate the velocity of {scen['obj2']} immediately "
            f"after the collision. (4 marks)\n\n"
            f"2. Determine, by calculating the total kinetic energy of the system before and after the collision, "
            f"whether this collision is ELASTIC or INELASTIC. (2 marks)"
        )

        sample_answer = (
            rf"\textbf{{1. Velocity of {scen['obj2']} after collision:}}\\"
            rf"\text{{Taking {pos_dir} as positive:}}\\"
            rf"\sum p_i = \sum p_f\\"
            rf"m_1 v_{{1i}} + m_2 v_{{2i}} = m_1 v_{{1f}} + m_2 v_{{2f}}\\"
            rf"({_fmt_sa(m1)})({_fmt_sa(v1i)}) + ({_fmt_sa(m2)})({_fmt_sa(v2i)}) = ({_fmt_sa(m1)})({_fmt_sa(v1f)}) + ({_fmt_sa(m2)}) v_{{2f}}\\"
            rf"{_fmt_sa(round(m1 * v1i + m2 * v2i, 2))} = {_fmt_sa(round(m1 * v1f, 2))} + ({_fmt_sa(m2)}) v_{{2f}}\\"
            rf"({_fmt_sa(m2)}) v_{{2f}} = {_fmt_sa(round((m1 * v1i + m2 * v2i) - (m1 * v1f), 2))}\\"
            rf"v_{{2f}} = {_fmt_sa(v2f)}\text{{ m}}\cdot\text{{s}}^{{-1}}\\"
            rf"\therefore v_{{2f}} = {_fmt_sa(abs(v2f))}\text{{ m}}\cdot\text{{s}}^{{-1}}\text{{ to the {v2f_dir}}}\\\\"
            rf"\textbf{{2. Elasticity determination:}}\\"
            rf"\sum E_{{ki}} = \frac{{1}}{{2}} m_1 v_{{1i}}^2 + \frac{{1}}{{2}} m_2 v_{{2i}}^2 = "
            rf"\frac{{1}}{{2}}({_fmt_sa(m1)})({_fmt_sa(v1i)})^2 + \frac{{1}}{{2}}({_fmt_sa(m2)})({_fmt_sa(abs(v2i))})^2 = {_fmt_sa(ek_total_i)}\text{{ J}}\\"
            rf"\sum E_{{kf}} = \frac{{1}}{{2}} m_1 v_{{1f}}^2 + \frac{{1}}{{2}} m_2 v_{{2f}}^2 = "
            rf"\frac{{1}}{{2}}({_fmt_sa(m1)})({_fmt_sa(abs(v1f))})^2 + \frac{{1}}{{2}}({_fmt_sa(m2)})({_fmt_sa(v2f)})^2 = {_fmt_sa(ek_total_f)}\text{{ J}}\\"
            rf"\text{{Since }}\sum E_{{ki}} = \sum E_{{kf}} = {_fmt_sa(ek_total_i)}\text{{ J}}, \text{{the collision is }}\textbf{{ELASTIC}}."
        )

        marking_schema = {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_p_formula", "desc": "[M] Formula Σp_i = Σp_f or m1*v1i + m2*v2i = m1*v1f + m2*v2f", "marks": 1, "editable": True},
                {"id": "mp_p_sub_init", "desc": f"[M] Substitution of initial values: ({_fmt_sa(m1)})({_fmt_sa(v1i)}) + ({_fmt_sa(m2)})({_fmt_sa(v2i)})", "marks": 1, "editable": True},
                {"id": "mp_p_sub_fin", "desc": f"[M] Substitution of final values with rebound sign: ({_fmt_sa(m1)})({_fmt_sa(v1f)}) + ({_fmt_sa(m2)})*v2f", "marks": 1, "editable": True},
                {"id": "mp_p_ans", "desc": f"[A] Final velocity magnitude, unit and direction: {_fmt_sa(abs(v2f))} m·s⁻¹ to the {v2f_dir}", "marks": 1, "editable": True},
                {"id": "mp_ek_calc", "desc": f"[M] Calculation of ΣEk(i) = {_fmt_sa(ek_total_i)} J and ΣEk(f) = {_fmt_sa(ek_total_f)} J", "marks": 1, "editable": True},
                {"id": "mp_ek_deduction", "desc": "[A] Conclusion with valid justification: ΣEk(i) = ΣEk(f) hence collision is ELASTIC", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "omitted_or_wrong_unit", "penalty": -1},
                {"rule": "omitted_vector_direction", "penalty": -1}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }

        hints = {
            "tier_1": f"Apply the Principle of Conservation of Linear Momentum: $\\sum p_i = \\sum p_f$. Note that {scen['obj1']} rebounds to the {v1f_dir}, so its final velocity is negative.",
            "tier_2": f"Taking {pos_dir} as positive: $m_1 v_{{1i}} + m_2 v_{{2i}} = m_1 v_{{1f}} + m_2 v_{{2f}}$. Substitute $v_{{1f}} = {_fmt_sa(v1f)}$ m·s⁻¹ and solve for $v_{{2f}}$. For Question 2, calculate total kinetic energy before and after.",
            "tier_3": f"Initial momentum = $({_fmt_sa(m1)})({_fmt_sa(v1i)}) + ({_fmt_sa(m2)})({_fmt_sa(v2i)}) = {_fmt_sa(round(m1 * v1i + m2 * v2i, 2))}$ kg·m·s⁻¹. Final momentum = $({_fmt_sa(m1)})({_fmt_sa(v1f)}) + ({_fmt_sa(m2)})v_{{2f}}$. $v_{{2f}} = {_fmt_sa(v2f)}$ m·s⁻¹ to the {v2f_dir}. Total $E_{{ki}} = {_fmt_sa(ek_total_i)}$ J, $E_{{kf}} = {_fmt_sa(ek_total_f)}$ J. Since $E_{{ki}} = E_{{kf}}$, the collision is ELASTIC."
        }

        ideal_ans = f"v2f = {_fmt_sa(abs(v2f))} m·s⁻¹ to the {v2f_dir}; ELASTIC"

    return {
        "id": f"phys_mom_cmpd_coll_{r.randint(100000, 999999)}",
        "topic": "Momentum and Impulse",
        "subskill": "conservation_of_momentum_1d",
        "mode": "compound",
        "difficulty": "hard",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 9,
        "marks": 6,
        "prompt": prompt,
        "ideal_answer": ideal_ans,
        "sample_answer": sample_answer,
        "misconception_tags": [
            "ignored_vector_sign_in_momentum_sum",
            "confused_elastic_and_inelastic_kinetic_energy",
            "omitted_vector_direction"
        ],
        "marking_schema": marking_schema,
        "hints": hints
    }


# ============================================================================ #
# BUILDER REGISTRY & PUBLIC GENERATOR API
# ============================================================================ #

BUILDERS = {
    "compound": _build_compound_collision,
    "compound_collision": _build_compound_collision,
    "compound_impulse": _build_compound_impulse,
    "conservation_of_momentum": _build_compound_collision,
    "conservation_of_momentum_1d": _build_compound_collision,
    "collisions": _build_compound_collision,
    "1d_collisions": _build_compound_collision,
    "impulse": _build_compound_impulse,
    "impulse_newton_second_law": _build_compound_impulse,
    "newtons_second_law_momentum": _build_compound_impulse,
    "elementary_momentum": _build_elementary_momentum,
    "elementary_change_momentum": _build_elementary_change_momentum,
    "elementary_impulse": _build_elementary_impulse,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generates authentic CAPS Grade 12 Physical Sciences Momentum & Impulse questions.
    Returns a list of 6-pillar compliant question dictionaries.
    """
    base_seed = 42 if seed is None else int(seed)
    
    # Priority:
    # 1. If explicit recognized subskill is provided, prioritize it
    # 2. Else if explicit non-default mode is provided, use mode
    # 3. Else fallback to "compound"
    chosen_key = "compound"
    if subskill and subskill in BUILDERS and subskill != "compound":
        chosen_key = subskill
    elif mode and mode in BUILDERS and mode != "compound":
        chosen_key = mode
    elif subskill and subskill in BUILDERS:
        chosen_key = subskill

    questions: List[Dict[str, Any]] = []
    for i in range(max(1, count)):
        current_seed = base_seed * 1000 + i
        r = _rng(current_seed)
        
        # When in generic compound mode (no specific subskill),
        # alternate between collision (6 marks) and impulse (5 marks)
        if chosen_key == "compound":
            builder = _build_compound_collision if (i % 2 == 0) else _build_compound_impulse
        else:
            builder = BUILDERS.get(chosen_key, _build_compound_collision)

        q = builder(r)
        q["seed"] = current_seed
        questions.append(q)

    return questions
