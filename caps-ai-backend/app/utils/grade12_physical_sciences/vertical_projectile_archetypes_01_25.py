"""
vertical_projectile_archetypes_01_25.py
---------------------------------------
Grade 12 Physical Sciences — Vertical Projectile Motion in 1D (Subskills 01–25).
Subskills covered:
  01. 01_free_fall_and_projectile_definition
  02. 02_acceleration_at_maximum_height_apex
  03. 03_sign_convention_upward_vs_downward_positive
  04. 04_dropped_object_velocity_after_time
  05. 05_dropped_object_vertical_displacement
  06. 06_dropped_object_time_to_reach_ground
  07. 07_dropped_object_final_impact_speed
  08. 08_projected_downwards_final_velocity
  09. 09_projected_downwards_displacement_in_time
  10. 10_projected_downwards_time_to_ground
  11. 11_projected_upwards_time_to_maximum_height
  12. 12_projected_upwards_maximum_height_reached
  13. 13_time_symmetry_upward_and_downward_flight
  14. 14_velocity_symmetry_at_equal_heights
  15. 15_projected_upwards_velocity_at_given_time
  16. 16_projected_upwards_height_at_given_time
  17. 17_time_interval_above_given_height
  18. 18_cliff_launch_upwards_maximum_height_above_ground
  19. 19_cliff_launch_upwards_final_impact_velocity
  20. 20_cliff_launch_upwards_total_flight_time
  21. 21_cliff_launch_speed_from_known_flight_time
  22. 22_cliff_height_from_upward_launch_and_time
  23. 23_distance_travelled_in_nth_second_of_free_fall
  24. 24_window_passage_initial_drop_height
  25. 25_two_stage_rocket_powered_ascent_then_free_fall

All generators are 100% deterministic (random.Random(seed)), zero-LLM,
adhering strictly to South African comma decimal convention and 6-pillar contract.
"""

from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional

TERM = 1
CAPS_WEIGHT = 20
SUGGESTED_DURATION = 5
TOPIC_ID = "grade12_vertical_projectile"
LEARNING_OBJECTIVE = "PS12.VPM"
G = 9.8


def _fmt_sa(val: float, decimals: int = 2) -> str:
    """Format float with South African comma decimal notation for LaTeX."""
    if abs(val - round(val)) < 1e-9:
        return str(int(round(val)))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _base_contract(
    subskill: str,
    prompt: str,
    answer: str,
    options: Optional[List[str]],
    sol_steps: List[Dict[str, str]],
    t1: str,
    t2: str,
    t3: str,
    misconceptions: List[str],
    marks: int = 4,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Enforce universal 6-pillar generator contract."""
    worked = "\n".join(
        f"{s.get('rule', '')}: ${s.get('op', '')} \\implies {s.get('to', '')}$"
        for s in sol_steps
    )
    q: Dict[str, Any] = {
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT,
        "suggested_duration_mins": SUGGESTED_DURATION,
        "topic": TOPIC_ID,
        "learning_objective_id": LEARNING_OBJECTIVE,
        "subskill": subskill,
        "prompt": prompt,
        "prompt_latex": prompt,
        "question_text": prompt,
        "question": prompt,
        "worked_solution": worked,
        "explanation": worked,
        "correct_answer": answer,
        "sample_answer": answer,
        "expected_answer": answer,
        "answer_mode": "mcq" if options else "short_answer",
        "total_marks": marks,
        "marks": marks,
        "misconception_tags": misconceptions,
        "hints": [
            {"tier": 1, "title": "Key Concept", "text": t1},
            {"tier": 2, "title": "Formula / Principle", "text": t2},
            {"tier": 3, "title": "Worked Step", "text": t3},
        ],
        "canonical_solution": {
            "steps": sol_steps,
            "final_answer": answer,
        },
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{i+1}", "desc": s.get("rule", f"Step {i+1}"), "marks": 1, "editable": True}
                for i, s in enumerate(sol_steps[:marks])
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }
    if options:
        q["options"] = options
        q["correct_option"] = answer
        q["answer_latex"] = answer
        q["answer_value"] = answer
    else:
        q["answer_latex"] = answer
        q["answer_value"] = answer
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


# =========================================================================== #
# Archetypes 01 to 25
# =========================================================================== #

def _build_01(rng: random.Random) -> Dict[str, Any]:
    sub = "01_free_fall_and_projectile_definition"
    obj = rng.choice(["a cricket ball", "a steel sphere", "a stone", "a tennis ball"])
    v0 = rng.choice([12, 15, 18, 20])
    prompt = (
        f"During a mechanics investigation, {obj} is launched vertically upwards with an initial speed of ${v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        "in the absence of air resistance.\n\n"
        "Which statement correctly defines **free fall** and a **projectile**?\n\n"
        "A. Free fall is motion under the influence of gravitational force only, and a projectile is an object upon which the only force acting is gravity.\n"
        "B. Free fall only occurs when an object moves downwards after being dropped from rest.\n"
        "C. A projectile is an object propelled continuously by an internal engine thrust throughout its flight.\n"
        "D. Free fall is motion where gravitational acceleration decreases to zero at maximum height."
    )
    ans = "A. Free fall is motion under the influence of gravitational force only, and a projectile is an object upon which the only force acting is gravity."
    opts = [
        ans,
        "B. Free fall only occurs when an object moves downwards after being dropped from rest.",
        "C. A projectile is an object propelled continuously by an internal engine thrust throughout its flight.",
        "D. Free fall is motion where gravitational acceleration decreases to zero at maximum height.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Define free fall", "op": "F_{\\text{resultant}} = F_g", "to": "\\text{Motion under gravity alone}"},
        {"rule": "Define projectile", "op": "\\text{Object acted upon only by gravity}", "to": "\\text{Applies to upward and downward motion}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Even while moving upwards, an object in air (ignoring drag) is in free fall.",
        t2="A projectile is any object upon which the only force acting is the gravitational force of the Earth.",
        t3="Option A gives the exact physical definitions.",
        misconceptions=["thinking_free_fall_only_means_moving_downwards", "confusing_propelled_rockets_with_projectiles"],
        marks=2,
    )


def _build_02(rng: random.Random) -> Dict[str, Any]:
    sub = "02_acceleration_at_maximum_height_apex"
    v0 = rng.choice([9.8, 14.7, 19.6, 24.5, 29.4])
    t_apex = round(v0 / G, 2)
    prompt = (
        f"A ball is thrown vertically upwards at $v_i = {_fmt_sa(v0)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ and reaches its highest point (apex) "
        f"at $t = {_fmt_sa(t_apex)}\\text{{ s}}$.\n\n"
        "What are the **velocity** and the **acceleration** of the ball at the exact instant it is at its maximum height?\n\n"
        "A. Velocity is $0\\text{ m}\\cdot\\text{s}^{-1}$; acceleration is $9{,}8\\text{ m}\\cdot\\text{s}^{-2}$ downwards.\n"
        "B. Velocity is $0\\text{ m}\\cdot\\text{s}^{-1}$; acceleration is $0\\text{ m}\\cdot\\text{s}^{-2}$.\n"
        "C. Velocity is $9{,}8\\text{ m}\\cdot\\text{s}^{-1}$ downwards; acceleration is $0\\text{ m}\\cdot\\text{s}^{-2}$.\n"
        "D. Velocity is $9{,}8\\text{ m}\\cdot\\text{s}^{-1}$ upwards; acceleration is $9{,}8\\text{ m}\\cdot\\text{s}^{-2}$ upwards."
    )
    ans = "A. Velocity is $0\\text{ m}\\cdot\\text{s}^{-1}$; acceleration is $9{,}8\\text{ m}\\cdot\\text{s}^{-2}$ downwards."
    opts = [
        ans,
        "B. Velocity is $0\\text{ m}\\cdot\\text{s}^{-1}$; acceleration is $0\\text{ m}\\cdot\\text{s}^{-2}$.",
        "C. Velocity is $9{,}8\\text{ m}\\cdot\\text{s}^{-1}$ downwards; acceleration is $0\\text{ m}\\cdot\\text{s}^{-2}$.",
        "D. Velocity is $9{,}8\\text{ m}\\cdot\\text{s}^{-1}$ upwards; acceleration is $9{,}8\\text{ m}\\cdot\\text{s}^{-2}$ upwards.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Determine velocity at apex", "op": "v_{\\text{apex}} = 0\\text{ m}\\cdot\\text{s}^{-1}", "to": "\\text{Instantaneous rest at turning point}"},
        {"rule": "Determine gravitational acceleration at apex", "op": "\\vec{a} = \\vec{g} = 9{,}8\\text{ m}\\cdot\\text{s}^{-2}\\text{ downwards}", "to": "\\text{Gravity acts continuously}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="At the turning point (maximum height), the ball momentarily stops before reversing direction.",
        t2="However, Earth's gravity never switches off: the gravitational force and acceleration remain 9,8 m/s^2 downwards.",
        t3="Option A correctly states v = 0 m/s and a = 9,8 m/s^2 downwards.",
        misconceptions=["apex_acceleration_zero_misconception", "confusing_velocity_with_acceleration"],
        marks=2,
    )


def _build_03(rng: random.Random) -> Dict[str, Any]:
    sub = "03_sign_convention_upward_vs_downward_positive"
    v0 = rng.choice([15, 20, 25, 30])
    h_cliff = rng.choice([35, 45, 55, 65])
    prompt = (
        f"A stone is projected vertically upwards at ${v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ from the top of a ${h_cliff}\\text{{ m}}$ building "
        "and eventually strikes the ground at the base of the building.\n\n"
        "If the learner chooses **upwards as the positive direction**, which set of signs correctly represents the initial velocity ($v_i$), "
        "gravitational acceleration ($g$), and total vertical displacement ($\\Delta y$) from launch to ground impact?\n\n"
        f"A. $v_i = +{v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; g = -9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}},\\; \\Delta y = -{h_cliff}\\text{{ m}}$\n"
        f"B. $v_i = +{v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; g = +9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}},\\; \\Delta y = +{h_cliff}\\text{{ m}}$\n"
        f"C. $v_i = -{v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; g = -9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}},\\; \\Delta y = +{h_cliff}\\text{{ m}}$\n"
        f"D. $v_i = +{v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; g = -9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}},\\; \\Delta y = +{h_cliff}\\text{{ m}}$"
    )
    ans = f"A. $v_i = +{v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; g = -9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}},\\; \\Delta y = -{h_cliff}\\text{{ m}}$"
    opts = [
        ans,
        f"B. $v_i = +{v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; g = +9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}},\\; \\Delta y = +{h_cliff}\\text{{ m}}$",
        f"C. $v_i = -{v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; g = -9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}},\\; \\Delta y = +{h_cliff}\\text{{ m}}$",
        f"D. $v_i = +{v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; g = -9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}},\\; \\Delta y = +{h_cliff}\\text{{ m}}$",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Assign sign to upward initial velocity", "op": f"v_i = +{v0}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}", "to": "\\text{Positive (upwards)}"},
        {"rule": "Assign sign to downward gravity and downward overall displacement", "op": f"g = -9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}},\\; \\Delta y = -{h_cliff}\\text{{ m}}", "to": "\\text{Both negative (downwards)}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="With upwards chosen as positive, any vector pointing upwards is positive and any vector pointing downwards is negative.",
        t2=f"Initial velocity is upwards (+{v0}), gravity acts downwards (-9,8), and the final position at the ground is {h_cliff} m below the starting point (-{h_cliff}).",
        t3="Option A assigns all three vector signs consistently.",
        misconceptions=["sign_convention_inconsistency", "forgetting_negative_displacement_below_launch_point"],
        marks=3,
    )


def _build_04(rng: random.Random) -> Dict[str, Any]:
    sub = "04_dropped_object_velocity_after_time"
    t_val = rng.choice([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
    vf = round(G * t_val, 2)
    prompt = (
        f"A metal bolt is dropped from rest ($v_i = 0\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$) from a high bridge. "
        f"Ignore air resistance and take $g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ downwards.\n\n"
        f"Calculate the magnitude of the bolt's velocity after $\\Delta t = {_fmt_sa(t_val)}\\text{{ s}}$ of free fall."
    )
    ans = f"$v_f = {_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}$"
    d1 = f"$v_f = {_fmt_sa(round(0.5 * G * t_val**2, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}$"
    d2 = f"$v_f = {_fmt_sa(round(vf / 2, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}$"
    d3 = f"$v_f = {_fmt_sa(round(G / t_val, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Select velocity-time equation of motion (downwards positive)", "op": "v_f = v_i + g \\Delta t", "to": f"v_f = 0 + (9{{,}}8)({_fmt_sa(t_val)})"},
        {"rule": "Compute final velocity", "op": f"9{{,}}8 \\times {_fmt_sa(t_val)}", "to": f"{_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="'Dropped from rest' means the initial velocity is v_i = 0 m/s.",
        t2="Use v_f = v_i + g * delta_t with g = 9,8 m/s^2 downwards.",
        t3=f"v_f = 0 + 9,8 * {_fmt_sa(t_val)} = {_fmt_sa(vf)} m/s downwards.",
        misconceptions=["confusing_velocity_formula_with_displacement_formula", "non_zero_initial_velocity_for_dropped_object"],
        marks=3,
    )


def _build_05(rng: random.Random) -> Dict[str, Any]:
    sub = "05_dropped_object_vertical_displacement"
    t_val = rng.choice([1.0, 1.5, 2.0, 2.5, 3.0, 4.0])
    dy = round(0.5 * G * (t_val ** 2), 2)
    prompt = (
        f"A stone is released from rest from a hovering observation drone. "
        f"Calculate the vertical distance ($\\Delta y$) the stone falls during the first $\\Delta t = {_fmt_sa(t_val)}\\text{{ s}}$ "
        f"of its motion ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$)."
    )
    ans = f"$\\Delta y = {_fmt_sa(dy)}\\text{{ m}}$"
    d1 = f"$\\Delta y = {_fmt_sa(round(G * t_val, 2))}\\text{{ m}}$"
    d2 = f"$\\Delta y = {_fmt_sa(round(G * (t_val ** 2), 2))}\\text{{ m}}$"
    d3 = f"$\\Delta y = {_fmt_sa(round(0.5 * G * t_val, 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "State position-time equation of motion (downwards positive)", "op": "\\Delta y = v_i \\Delta t + \\frac{1}{2} g \\Delta t^2", "to": f"\\Delta y = 0 + \\frac{{1}}{{2}}(9{{,}}8)({_fmt_sa(t_val)})^2"},
        {"rule": "Evaluate vertical distance fallen", "op": f"4{{,}}9 \\times ({_fmt_sa(t_val)})^2", "to": f"{_fmt_sa(dy)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Since the stone is released from rest, v_i = 0 m/s.",
        t2="Use delta_y = v_i * delta_t + 0,5 * g * delta_t^2.",
        t3=f"delta_y = 0,5 * 9,8 * ({_fmt_sa(t_val)})^2 = {_fmt_sa(dy)} m.",
        misconceptions=["forgetting_to_square_time", "omitting_factor_of_half"],
        marks=3,
    )


def _build_06(rng: random.Random) -> Dict[str, Any]:
    sub = "06_dropped_object_time_to_reach_ground"
    t_exact = rng.choice([2.0, 2.5, 3.0, 3.5, 4.0, 5.0])
    h_val = round(0.5 * G * (t_exact ** 2), 2)
    prompt = (
        f"A rescue supply crate is dropped from rest from a stationary helicopter at a height of "
        f"$h = {_fmt_sa(h_val)}\\text{{ m}}$ above the ground. Ignore air resistance ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"Calculate the time ($\\Delta t$) taken for the crate to reach the ground."
    )
    ans = f"$\\Delta t = {_fmt_sa(t_exact)}\\text{{ s}}$"
    d1 = f"$\\Delta t = {_fmt_sa(round(t_exact ** 2, 2))}\\text{{ s}}$"
    d2 = f"$\\Delta t = {_fmt_sa(round(h_val / G, 2))}\\text{{ s}}$"
    d3 = f"$\\Delta t = {_fmt_sa(round(math.sqrt(h_val / G), 2))}\\text{{ s}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Use displacement-time equation with v_i = 0", "op": "\\Delta y = \\frac{1}{2} g \\Delta t^2", "to": f"{_fmt_sa(h_val)} = 4{{,}}9 \\Delta t^2"},
        {"rule": "Solve for time by taking square root", "op": f"\\Delta t = \\sqrt{{\\frac{{{_fmt_sa(h_val)}}}{{4{{,}}9}}}}", "to": f"{_fmt_sa(t_exact)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Substitute v_i = 0 and delta_y = h into delta_y = v_i * t + 0,5 * g * t^2.",
        t2=f"Rearrange to get t^2 = (2 * {_fmt_sa(h_val)}) / 9,8 = {_fmt_sa(t_exact**2)}.",
        t3=f"Take the square root to obtain t = {_fmt_sa(t_exact)} s.",
        misconceptions=["forgetting_square_root_when_solving_for_time", "dividing_height_by_g_directly"],
        marks=3,
    )


def _build_07(rng: random.Random) -> Dict[str, Any]:
    sub = "07_dropped_object_final_impact_speed"
    t_exact = rng.choice([1.5, 2.0, 2.5, 3.0, 4.0])
    h_val = round(0.5 * G * (t_exact ** 2), 2)
    vf = round(G * t_exact, 2)
    prompt = (
        f"A coconut falls from rest from a palm tree of height $h = {_fmt_sa(h_val)}\\text{{ m}}$ above the beach.\n\n"
        f"Calculate the speed ($v_f$) of the coconut just before it hits the sand ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$)."
    )
    ans = f"$v_f = {_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d1 = f"$v_f = {_fmt_sa(round(vf ** 2, 1))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d2 = f"$v_f = {_fmt_sa(round(math.sqrt(G * h_val), 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d3 = f"$v_f = {_fmt_sa(round(vf / 2, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Apply velocity-displacement equation (downwards positive)", "op": "v_f^2 = v_i^2 + 2 g \\Delta y", "to": f"v_f^2 = 0 + 2(9{{,}}8)({_fmt_sa(h_val)})"},
        {"rule": "Take square root for final impact speed", "op": f"v_f = \\sqrt{{{_fmt_sa(round(2 * G * h_val, 2))}}}", "to": f"{_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Since time is not given, use the time-independent equation v_f^2 = v_i^2 + 2 * g * delta_y.",
        t2=f"With v_i = 0, v_f^2 = 2 * 9,8 * {_fmt_sa(h_val)} = {_fmt_sa(round(vf**2, 2))}.",
        t3=f"Take the square root: v_f = {_fmt_sa(vf)} m/s.",
        misconceptions=["forgetting_to_take_square_root_of_vf_squared", "omitting_factor_of_2_in_2gdy"],
        marks=3,
    )


def _build_08(rng: random.Random) -> Dict[str, Any]:
    sub = "08_projected_downwards_final_velocity"
    vi = rng.choice([4.0, 5.0, 6.0, 8.0, 10.0])
    t_val = rng.choice([1.5, 2.0, 2.5, 3.0])
    vf = round(vi + G * t_val, 2)
    prompt = (
        f"A learner throws a pebble **vertically downwards** from a bridge with an initial velocity of "
        f"$v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ downwards.\n\n"
        f"Calculate the velocity ($v_f$) of the pebble after $\\Delta t = {_fmt_sa(t_val)}\\text{{ s}}$ ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ downwards)."
    )
    ans = f"$v_f = {_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}$"
    d1 = f"$v_f = {_fmt_sa(round(abs(vi - G * t_val), 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}$"
    d2 = f"$v_f = {_fmt_sa(round(G * t_val, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}$"
    d3 = f"$v_f = {_fmt_sa(round(vi * t_val, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Take downwards as positive so both v_i and g are positive", "op": "v_f = v_i + g \\Delta t", "to": f"v_f = {_fmt_sa(vi)} + (9{{,}}8)({_fmt_sa(t_val)})"},
        {"rule": "Calculate final downward velocity", "op": f"{_fmt_sa(vi)} + {_fmt_sa(round(G * t_val, 2))}", "to": f"{_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Because the pebble is thrown downwards, its initial velocity is in the same direction as gravitational acceleration.",
        t2="Taking downwards as positive: v_f = v_i + g * delta_t.",
        t3=f"v_f = {_fmt_sa(vi)} + 9,8 * {_fmt_sa(t_val)} = {_fmt_sa(vf)} m/s downwards.",
        misconceptions=["subtracting_g_t_when_thrown_downwards", "setting_vi_to_zero_when_thrown_downwards"],
        marks=3,
    )


def _build_09(rng: random.Random) -> Dict[str, Any]:
    sub = "09_projected_downwards_displacement_in_time"
    vi = rng.choice([3.0, 5.0, 6.0, 7.5, 10.0])
    t_val = rng.choice([1.0, 2.0, 2.5, 3.0])
    dy = round(vi * t_val + 0.5 * G * (t_val ** 2), 2)
    prompt = (
        f"A ball is projected vertically downwards at $v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ from the top of a cliff.\n\n"
        f"Calculate the vertical distance ($\\Delta y$) covered by the ball in $\\Delta t = {_fmt_sa(t_val)}\\text{{ s}}$."
    )
    ans = f"$\\Delta y = {_fmt_sa(dy)}\\text{{ m}}$"
    d1 = f"$\\Delta y = {_fmt_sa(round(abs(vi * t_val - 0.5 * G * (t_val ** 2)), 2))}\\text{{ m}}$"
    d2 = f"$\\Delta y = {_fmt_sa(round(0.5 * G * (t_val ** 2), 2))}\\text{{ m}}$"
    d3 = f"$\\Delta y = {_fmt_sa(round(vi * t_val + G * (t_val ** 2), 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Apply displacement-time equation (downwards positive)", "op": "\\Delta y = v_i \\Delta t + \\frac{1}{2} g \\Delta t^2", "to": f"\\Delta y = ({_fmt_sa(vi)})({_fmt_sa(t_val)}) + 4{{,}}9({_fmt_sa(t_val)})^2"},
        {"rule": "Evaluate total downward distance", "op": f"{_fmt_sa(round(vi * t_val, 2))} + {_fmt_sa(round(0.5 * G * t_val**2, 2))}", "to": f"{_fmt_sa(dy)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Both initial velocity and gravity act downwards, so both terms in delta_y = v_i*t + 0,5*g*t^2 have the same sign.",
        t2=f"Substitute v_i = {_fmt_sa(vi)} m/s, t = {_fmt_sa(t_val)} s, and g = 9,8 m/s^2.",
        t3=f"delta_y = {_fmt_sa(dy)} m.",
        misconceptions=["opposite_signs_for_downward_throw_and_gravity", "omitting_vi_t_term"],
        marks=3,
    )


def _build_10(rng: random.Random) -> Dict[str, Any]:
    sub = "10_projected_downwards_time_to_ground"
    vi = rng.choice([4.9, 9.8, 14.7])
    t_exact = rng.choice([1.0, 1.5, 2.0, 2.5, 3.0])
    h_val = round(vi * t_exact + 0.5 * G * (t_exact ** 2), 2)
    vf = round(vi + G * t_exact, 2)
    prompt = (
        f"A stone is thrown vertically downwards with an initial speed of $v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"from a height of $h = {_fmt_sa(h_val)}\\text{{ m}}$ above the ground.\n\n"
        f"Calculate the time ($\\Delta t$) taken for the stone to strike the ground."
    )
    ans = f"$\\Delta t = {_fmt_sa(t_exact)}\\text{{ s}}$"
    d1 = f"$\\Delta t = {_fmt_sa(round(h_val / vi, 2))}\\text{{ s}}$"
    d2 = f"$\\Delta t = {_fmt_sa(round(math.sqrt(2 * h_val / G), 2))}\\text{{ s}}$"
    d3 = f"$\\Delta t = {_fmt_sa(round(t_exact + 1.2, 2))}\\text{{ s}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Find final velocity using v_f^2 = v_i^2 + 2g*Delta_y", "op": f"v_f = \\sqrt{{({_fmt_sa(vi)})^2 + 2(9{{,}}8)({_fmt_sa(h_val)})}}", "to": f"v_f = {_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Solve for time using v_f = v_i + g*Delta_t", "op": f"\\Delta t = \\frac{{{_fmt_sa(vf)} - {_fmt_sa(vi)}}}{{9{{,}}8}}", "to": f"{_fmt_sa(t_exact)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="First find the impact velocity using v_f^2 = v_i^2 + 2*g*delta_y (taking downwards as positive).",
        t2=f"v_f = {_fmt_sa(vf)} m/s downwards. Then substitute into v_f = v_i + g*t.",
        t3=f"t = ({_fmt_sa(vf)} - {_fmt_sa(vi)}) / 9,8 = {_fmt_sa(t_exact)} s.",
        misconceptions=["using_constant_velocity_formula_d_over_v", "ignoring_initial_downward_speed"],
        marks=4,
    )


def _build_11(rng: random.Random) -> Dict[str, Any]:
    sub = "11_projected_upwards_time_to_maximum_height"
    vi = rng.choice([9.8, 14.7, 19.6, 24.5, 29.4, 34.3, 39.2])
    t_apex = round(vi / G, 2)
    prompt = (
        f"A ball is projected vertically upwards with an initial velocity of $v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the time ($\\Delta t$) it takes for the ball to reach its maximum height ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ downwards)."
    )
    ans = f"$\\Delta t = {_fmt_sa(t_apex)}\\text{{ s}}$"
    d1 = f"$\\Delta t = {_fmt_sa(round(t_apex * 2, 2))}\\text{{ s}}$"
    d2 = f"$\\Delta t = {_fmt_sa(round(vi * G, 1))}\\text{{ s}}$"
    d3 = f"$\\Delta t = {_fmt_sa(round(t_apex / 2, 2))}\\text{{ s}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Set v_f = 0 at maximum height (upwards positive)", "op": "0 = v_i + (-9{,}8)\\Delta t", "to": f"9{{,}}8\\Delta t = {_fmt_sa(vi)}"},
        {"rule": "Solve for time to apex", "op": f"\\Delta t = \\frac{{{_fmt_sa(vi)}}}{{9{{,}}8}}", "to": f"{_fmt_sa(t_apex)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="At maximum height, the vertical velocity of the projectile is momentarily v_f = 0 m/s.",
        t2="Use v_f = v_i + g * delta_t with upwards as positive (g = -9,8 m/s^2).",
        t3=f"delta_t = {_fmt_sa(vi)} / 9,8 = {_fmt_sa(t_apex)} s.",
        misconceptions=["confusing_time_to_apex_with_total_flight_time", "multiplying_vi_by_g"],
        marks=3,
    )


def _build_12(rng: random.Random) -> Dict[str, Any]:
    sub = "12_projected_upwards_maximum_height_reached"
    vi = rng.choice([9.8, 14.7, 19.6, 24.5, 29.4, 34.3])
    h_max = round((vi ** 2) / (2 * G), 2)
    prompt = (
        f"An arrow is shot vertically upwards from the ground with an initial velocity of "
        f"$v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Ignore air resistance.\n\n"
        f"Calculate the **maximum height** ($h_{{\\max}}$) reached by the arrow above the launch point."
    )
    ans = f"$h_{{\\max}} = {_fmt_sa(h_max)}\\text{{ m}}$"
    d1 = f"$h_{{\\max}} = {_fmt_sa(round(h_max * 2, 2))}\\text{{ m}}$"
    d2 = f"$h_{{\\max}} = {_fmt_sa(round(vi / G, 2))}\\text{{ m}}$"
    d3 = f"$h_{{\\max}} = {_fmt_sa(round(h_max / 2, 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Use v_f^2 = v_i^2 + 2g*Delta_y with v_f = 0 at apex", "op": f"0 = ({_fmt_sa(vi)})^2 + 2(-9{{,}}8)h_{{\\max}}", "to": f"19{{,}}6 h_{{\\max}} = {_fmt_sa(round(vi**2, 2))}"},
        {"rule": "Calculate maximum height", "op": f"h_{{\\max}} = \\frac{{({_fmt_sa(vi)})^2}}{{19{{,}}6}}", "to": f"{_fmt_sa(h_max)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="At maximum height, the final upward velocity is v_f = 0 m/s.",
        t2="Use v_f^2 = v_i^2 + 2 * g * delta_y with g = -9,8 m/s^2.",
        t3=f"h_max = ({_fmt_sa(vi)})^2 / (2 * 9,8) = {_fmt_sa(h_max)} m.",
        misconceptions=["omitting_factor_of_2_in_2g", "forgetting_to_square_initial_velocity"],
        marks=3,
    )


def _build_13(rng: random.Random) -> Dict[str, Any]:
    sub = "13_time_symmetry_upward_and_downward_flight"
    vi = rng.choice([14.7, 19.6, 24.5, 29.4, 34.3, 49.0])
    t_up = round(vi / G, 2)
    t_total = round(2 * t_up, 2)
    prompt = (
        f"A tennis ball is hit vertically upwards from ground level at $v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"and lands back on the ground at the same height level.\n\n"
        f"Calculate the **total time** ($\\Delta t_{{\\text{{total}}}}$) the ball spends in the air."
    )
    ans = f"$\\Delta t_{{\\text{{total}}}} = {_fmt_sa(t_total)}\\text{{ s}}$"
    d1 = f"$\\Delta t_{{\\text{{total}}}} = {_fmt_sa(t_up)}\\text{{ s}}$"
    d2 = f"$\\Delta t_{{\\text{{total}}}} = {_fmt_sa(round(t_total * 2, 2))}\\text{{ s}}$"
    d3 = f"$\\Delta t_{{\\text{{total}}}} = {_fmt_sa(round(vi / (2 * G), 2))}\\text{{ s}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Calculate time to reach maximum height", "op": f"t_{{\\text{{up}}}} = \\frac{{v_i}}{{g}} = \\frac{{{_fmt_sa(vi)}}}{{9{{,}}8}}", "to": f"{_fmt_sa(t_up)}\\text{{ s}}"},
        {"rule": "Apply time symmetry for return to launch level", "op": f"\\Delta t_{{\\text{{total}}}} = 2 t_{{\\text{{up}}}} = 2({_fmt_sa(t_up)})", "to": f"{_fmt_sa(t_total)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="By time symmetry in free fall, the time taken to rise from launch to apex equals the time taken to fall from apex back to launch level.",
        t2=f"First find t_up = v_i / g = {_fmt_sa(vi)} / 9,8 = {_fmt_sa(t_up)} s.",
        t3=f"Double t_up to find total time in air: 2 * {_fmt_sa(t_up)} = {_fmt_sa(t_total)} s.",
        misconceptions=["giving_half_flight_time_instead_of_total_time", "forgetting_symmetry_of_free_fall"],
        marks=3,
    )


def _build_14(rng: random.Random) -> Dict[str, Any]:
    sub = "14_velocity_symmetry_at_equal_heights"
    v_pass = rng.choice([8.5, 11.2, 14.0, 16.5, 21.0])
    h_pass = rng.choice([5.0, 8.0, 10.0, 12.0])
    prompt = (
        f"A stone thrown vertically upwards passes a window ledge at height ${h_pass}\\text{{ m}}$ above the ground "
        f"with an upward velocity of $+{_fmt_sa(v_pass)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ on its way up.\n\n"
        f"Ignoring air resistance, what is the **velocity** of the stone when it passes the exact same window ledge on its way down?"
    )
    ans = f"$-{_fmt_sa(v_pass)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ (or ${_fmt_sa(v_pass)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}$)"
    d1 = f"$+{_fmt_sa(v_pass)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ upwards}}$"
    d2 = "$0\\text{ m}\\cdot\\text{s}^{-1}$"
    d3 = f"$-{_fmt_sa(round(v_pass * 2, 1))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Apply symmetry of free-fall motion at equal elevations", "op": "|\\vec{v}_{\\text{down}}| = |\\vec{v}_{\\text{up}}|", "to": f"{_fmt_sa(v_pass)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Specify reversed direction on downward pass", "op": "\\vec{v}_{\\text{down}} = -\\vec{v}_{\\text{up}}", "to": f"-{_fmt_sa(v_pass)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ (downwards)}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="In free fall without air resistance, motion is symmetrical about the apex.",
        t2="At any given height, the speed on the way down equals the speed on the way up, but the direction is opposite.",
        t3=f"The velocity passing the ledge downwards is -{_fmt_sa(v_pass)} m/s ({_fmt_sa(v_pass)} m/s downwards).",
        misconceptions=["omitting_direction_reversal_for_velocity", "assuming_speed_doubles_on_return"],
        marks=2,
    )


def _build_15(rng: random.Random) -> Dict[str, Any]:
    sub = "15_projected_upwards_velocity_at_given_time"
    vi = rng.choice([19.6, 24.5, 29.4])
    t_val = rng.choice([1.0, 1.5, 3.0, 3.5, 4.0])
    vf = round(vi - G * t_val, 2)
    direction = "upwards" if vf >= 0 else "downwards"
    prompt = (
        f"A projectile is launched vertically upwards at $v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Determine the **magnitude and direction** of its velocity at $t = {_fmt_sa(t_val)}\\text{{ s}}$ after launch "
        f"($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ downwards)."
    )
    ans = f"${_fmt_sa(abs(vf))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ {direction}}}$"
    opp_dir = "downwards" if direction == "upwards" else "upwards"
    d1 = f"${_fmt_sa(abs(vf))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ {opp_dir}}}$"
    d2 = f"${_fmt_sa(round(vi + G * t_val, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ upwards}}$"
    d3 = f"${_fmt_sa(round(G * t_val, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Apply v_f = v_i + g*Delta_t (upwards positive)", "op": f"v_f = {_fmt_sa(vi)} + (-9{{,}}8)({_fmt_sa(t_val)})", "to": f"v_f = {_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Interpret sign for direction", "op": f"v_f = {_fmt_sa(vf)}", "to": f"{_fmt_sa(abs(vf))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ {direction}}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Choose upwards as positive so v_i is positive and g = -9,8 m/s^2.",
        t2=f"Calculate v_f = {_fmt_sa(vi)} - 9,8 * {_fmt_sa(t_val)} = {_fmt_sa(vf)} m/s.",
        t3=f"The sign indicates the direction is {direction}, with magnitude {_fmt_sa(abs(vf))} m/s.",
        misconceptions=["ignoring_negative_sign_meaning_downward_motion", "adding_g_t_instead_of_subtracting"],
        marks=3,
    )


def _build_16(rng: random.Random) -> Dict[str, Any]:
    sub = "16_projected_upwards_height_at_given_time"
    vi = rng.choice([20.0, 25.0, 30.0, 35.0])
    t_val = rng.choice([1.0, 2.0, 3.0, 4.0])
    dy = round(vi * t_val - 0.5 * G * (t_val ** 2), 2)
    prompt = (
        f"A flare is fired vertically upwards from the ground with an initial velocity of "
        f"$v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the height ($\\Delta y$) of the flare above the ground at $t = {_fmt_sa(t_val)}\\text{{ s}}$ after launch."
    )
    ans = f"$\\Delta y = {_fmt_sa(dy)}\\text{{ m}}$"
    d1 = f"$\\Delta y = {_fmt_sa(round(vi * t_val + 0.5 * G * (t_val ** 2), 2))}\\text{{ m}}$"
    d2 = f"$\\Delta y = {_fmt_sa(round(vi * t_val - G * (t_val ** 2), 2))}\\text{{ m}}$"
    d3 = f"$\\Delta y = {_fmt_sa(round(0.5 * G * (t_val ** 2), 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Use position-time equation (upwards positive)", "op": "\\Delta y = v_i \\Delta t + \\frac{1}{2} g \\Delta t^2", "to": f"\\Delta y = ({_fmt_sa(vi)})({_fmt_sa(t_val)}) + \\frac{{1}}{{2}}(-9{{,}}8)({_fmt_sa(t_val)})^2"},
        {"rule": "Compute height above ground", "op": f"{_fmt_sa(round(vi * t_val, 2))} - {_fmt_sa(round(0.5 * G * t_val**2, 2))}", "to": f"{_fmt_sa(dy)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Take upwards as positive: v_i = +v_i and g = -9,8 m/s^2.",
        t2=f"Substitute into delta_y = v_i*t - 4,9*t^2: ({_fmt_sa(vi)})({_fmt_sa(t_val)}) - 4,9({_fmt_sa(t_val)})^2.",
        t3=f"The height above ground is {_fmt_sa(dy)} m.",
        misconceptions=["adding_gravity_term_during_upward_launch", "omitting_half_factor"],
        marks=3,
    )


def _build_17(rng: random.Random) -> Dict[str, Any]:
    sub = "17_time_interval_above_given_height"
    # Choose clean roots t1 and t2 where 4.9*(t1+t2) = vi and 4.9*t1*t2 = h
    t1, t2 = rng.choice([(1.0, 3.0), (1.0, 4.0), (2.0, 4.0), (1.0, 5.0), (2.0, 5.0)])
    vi = round(4.9 * (t1 + t2), 2)
    h_level = round(4.9 * t1 * t2, 2)
    dt_above = round(t2 - t1, 2)

    prompt = (
        f"A ball is projected vertically upwards from the ground at $v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"It passes a horizontal marker at height $h = {_fmt_sa(h_level)}\\text{{ m}}$ at $t_1 = {_fmt_sa(t1)}\\text{{ s}}$ on the way up "
        f"and again at $t_2 = {_fmt_sa(t2)}\\text{{ s}}$ on the way down.\n\n"
        f"Calculate the total time interval ($\\Delta t$) during which the ball is **above** the ${_fmt_sa(h_level)}\\text{{ m}}$ marker."
    )
    ans = f"$\\Delta t = {_fmt_sa(dt_above)}\\text{{ s}}$"
    d1 = f"$\\Delta t = {_fmt_sa(round(t1 + t2, 2))}\\text{{ s}}$"
    d2 = f"$\\Delta t = {_fmt_sa(round(dt_above / 2, 2))}\\text{{ s}}$"
    d3 = f"$\\Delta t = {_fmt_sa(t2)}\\text{{ s}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Verify upward and downward passage times at height h", "op": f"t_1 = {_fmt_sa(t1)}\\text{{ s}},\\; t_2 = {_fmt_sa(t2)}\\text{{ s}}", "to": "\\text{Two roots of } \\Delta y = v_i t - 4{,}9 t^2"},
        {"rule": "Subtract upward passage time from downward passage time", "op": f"\\Delta t = t_2 - t_1 = {_fmt_sa(t2)} - {_fmt_sa(t1)}", "to": f"{_fmt_sa(dt_above)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The ball is above height h between the instant it passes h going up (t_1) and the instant it passes h coming down (t_2).",
        t2="Time spent above h is simply delta_t = t_2 - t_1.",
        t3=f"delta_t = {_fmt_sa(t2)} - {_fmt_sa(t1)} = {_fmt_sa(dt_above)} s.",
        misconceptions=["adding_passage_times_instead_of_subtracting", "giving_time_from_h_to_apex_only"],
        marks=3,
    )


def _build_18(rng: random.Random) -> Dict[str, Any]:
    sub = "18_cliff_launch_upwards_maximum_height_above_ground"
    h_cliff = rng.choice([25.0, 30.0, 40.0, 50.0, 60.0])
    vi = rng.choice([9.8, 14.7, 19.6, 24.5])
    dy_up = round((vi ** 2) / (2 * G), 2)
    h_ground = round(h_cliff + dy_up, 2)

    prompt = (
        f"A stone is thrown vertically upwards at $v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ from the roof of a building "
        f"that is ${h_cliff:.0f}\\text{{ m}}$ above the ground.\n\n"
        f"Calculate the **maximum height** ($H_{{\\max}}$) reached by the stone **above the ground** ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$)."
    )
    ans = f"$H_{{\\max}} = {_fmt_sa(h_ground)}\\text{{ m}}$"
    d1 = f"$H_{{\\max}} = {_fmt_sa(dy_up)}\\text{{ m}}$"
    d2 = f"$H_{{\\max}} = {_fmt_sa(round(abs(h_cliff - dy_up), 2))}\\text{{ m}}$"
    d3 = f"$H_{{\\max}} = {_fmt_sa(round(h_cliff + 2 * dy_up, 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Calculate maximum height reached above the roof", "op": f"\\Delta y_{{\\text{{up}}}} = \\frac{{v_i^2}}{{2g}} = \\frac{{({_fmt_sa(vi)})^2}}{{19{{,}}6}}", "to": f"{_fmt_sa(dy_up)}\\text{{ m}}"},
        {"rule": "Add building height to get height above ground", "op": f"H_{{\\max}} = {_fmt_sa(h_cliff)} + {_fmt_sa(dy_up)}", "to": f"{_fmt_sa(h_ground)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="First calculate how high the stone rises above the roof where it was launched.",
        t2=f"delta_y_up = ({_fmt_sa(vi)})^2 / 19,6 = {_fmt_sa(dy_up)} m.",
        t3=f"Add the building height ({_fmt_sa(h_cliff)} m): H_max = {_fmt_sa(h_cliff)} + {_fmt_sa(dy_up)} = {_fmt_sa(h_ground)} m.",
        misconceptions=["omitted_initial_cliff_height", "subtracting_cliff_height_from_apex_rise"],
        marks=4,
    )


def _build_19(rng: random.Random) -> Dict[str, Any]:
    sub = "19_cliff_launch_upwards_final_impact_velocity"
    # Pick vi and t_total so vf is clean
    vi = rng.choice([9.8, 14.7, 19.6])
    t_total = rng.choice([4.0, 5.0, 6.0])
    # dy = vi*t - 4.9*t^2 (will be negative since t_total > 2*vi/g)
    h_cliff = round(4.9 * (t_total ** 2) - vi * t_total, 2)
    vf_mag = round(G * t_total - vi, 2)

    prompt = (
        f"A ball is projected vertically upwards at $v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ from the edge of a cliff "
        f"of height $h = {_fmt_sa(h_cliff)}\\text{{ m}}$ above the valley floor.\n\n"
        f"Calculate the magnitude of the ball's velocity ($v_f$) just before it strikes the valley floor."
    )
    ans = f"$v_f = {_fmt_sa(vf_mag)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d1 = f"$v_f = {_fmt_sa(round(math.sqrt(abs(vi**2 - 2 * G * h_cliff)), 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d2 = f"$v_f = {_fmt_sa(round(math.sqrt(2 * G * h_cliff), 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d3 = f"$v_f = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Take upwards as positive so overall displacement is Delta_y = -h", "op": f"v_f^2 = ({_fmt_sa(vi)})^2 + 2(-9{{,}}8)(-{_fmt_sa(h_cliff)})", "to": f"v_f^2 = {_fmt_sa(round(vf_mag**2, 2))}"},
        {"rule": "Take square root to find impact speed", "op": f"v_f = \\sqrt{{{_fmt_sa(round(vf_mag**2, 2))}}}", "to": f"{_fmt_sa(vf_mag)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="With upwards as positive, v_i is positive (+v_i), g = -9,8 m/s^2, and the displacement from cliff top to valley floor is negative (delta_y = -h).",
        t2=f"Substitute into v_f^2 = v_i^2 + 2*g*delta_y: v_f^2 = ({_fmt_sa(vi)})^2 + 2(-9,8)(-{_fmt_sa(h_cliff)}).",
        t3=f"Take the square root to obtain v_f = {_fmt_sa(vf_mag)} m/s.",
        misconceptions=["sign_convention_inconsistency", "using_positive_dy_with_negative_g"],
        marks=4,
    )


def _build_20(rng: random.Random) -> Dict[str, Any]:
    sub = "20_cliff_launch_upwards_total_flight_time"
    vi = rng.choice([9.8, 14.7, 19.6])
    t_total = rng.choice([4.0, 5.0, 6.0])
    h_cliff = round(4.9 * (t_total ** 2) - vi * t_total, 2)
    vf_mag = round(G * t_total - vi, 2)

    prompt = (
        f"A projectile is launched vertically upwards at $v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ from a platform "
        f"$h = {_fmt_sa(h_cliff)}\\text{{ m}}$ above the ground. It rises to its maximum height and then falls to the ground below.\n\n"
        f"Calculate the **total time of flight** ($\\Delta t$) from launch until the projectile hits the ground."
    )
    ans = f"$\\Delta t = {_fmt_sa(t_total)}\\text{{ s}}$"
    d1 = f"$\\Delta t = {_fmt_sa(round(vi / G, 2))}\\text{{ s}}$"
    d2 = f"$\\Delta t = {_fmt_sa(round(2 * vi / G, 2))}\\text{{ s}}$"
    d3 = f"$\\Delta t = {_fmt_sa(round((vf_mag - vi) / G, 2))}\\text{{ s}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Set up displacement equation with upwards positive (Delta_y = -h)", "op": f"-{_fmt_sa(h_cliff)} = {_fmt_sa(vi)}\\Delta t - 4{{,}}9\\Delta t^2", "to": f"4{{,}}9\\Delta t^2 - {_fmt_sa(vi)}\\Delta t - {_fmt_sa(h_cliff)} = 0"},
        {"rule": "Solve for positive time root (or via v_f = -{_fmt_sa(vf_mag)} m/s)", "op": f"-{_fmt_sa(vf_mag)} = {_fmt_sa(vi)} - 9{{,}}8\\Delta t", "to": f"\\Delta t = {_fmt_sa(t_total)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Taking upwards as positive, the overall vertical displacement from platform to ground is delta_y = -h.",
        t2=f"Use delta_y = v_i*t + 0,5*g*t^2: -{_fmt_sa(h_cliff)} = {_fmt_sa(vi)}*t - 4,9*t^2.",
        t3=f"Solving the quadratic equation gives the positive time root delta_t = {_fmt_sa(t_total)} s.",
        misconceptions=["using_wrong_sign_for_final_velocity_vector", "stopping_at_return_to_launch_platform"],
        marks=4,
    )


def _build_21(rng: random.Random) -> Dict[str, Any]:
    sub = "21_cliff_launch_speed_from_known_flight_time"
    vi = rng.choice([10.0, 12.0, 15.0, 20.0])
    t_total = rng.choice([4.0, 5.0, 6.0])
    h_cliff = round(4.9 * (t_total ** 2) - vi * t_total, 2)

    prompt = (
        f"A stone is thrown vertically upwards with an unknown initial speed $v_i$ from the top of a cliff of height "
        f"$h = {_fmt_sa(h_cliff)}\\text{{ m}}$. The stone strikes the ground at the base of the cliff after $\\Delta t = {_fmt_sa(t_total)}\\text{{ s}}$.\n\n"
        f"Calculate the initial upward speed ($v_i$) of the stone."
    )
    ans = f"$v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d1 = f"$v_i = {_fmt_sa(round(4.9 * t_total, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d2 = f"$v_i = {_fmt_sa(round((4.9 * t_total**2 + h_cliff) / t_total, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d3 = f"$v_i = {_fmt_sa(round(h_cliff / t_total, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Use Delta_y = v_i*Delta_t + 0,5*g*Delta_t^2 (upwards positive)", "op": f"-{_fmt_sa(h_cliff)} = v_i({_fmt_sa(t_total)}) - 4{{,}}9({_fmt_sa(t_total)})^2", "to": f"{_fmt_sa(t_total)} v_i = {_fmt_sa(round(4.9 * t_total**2, 2))} - {_fmt_sa(h_cliff)}"},
        {"rule": "Solve for initial speed v_i", "op": f"v_i = \\frac{{{_fmt_sa(round(vi * t_total, 2))}}}{{{_fmt_sa(t_total)}}}", "to": f"{_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Choose upwards as positive so delta_y = -h and g = -9,8 m/s^2.",
        t2=f"Substitute into -{_fmt_sa(h_cliff)} = v_i * ({_fmt_sa(t_total)}) - 4,9 * ({_fmt_sa(t_total)})^2.",
        t3=f"Solve for v_i to obtain {_fmt_sa(vi)} m/s.",
        misconceptions=["using_positive_h_instead_of_negative_h", "setting_vi_equal_to_gt"],
        marks=4,
    )


def _build_22(rng: random.Random) -> Dict[str, Any]:
    sub = "22_cliff_height_from_upward_launch_and_time"
    vi = rng.choice([8.0, 10.0, 12.0, 15.0])
    t_total = rng.choice([3.5, 4.0, 5.0, 6.0])
    h_cliff = round(4.9 * (t_total ** 2) - vi * t_total, 2)

    prompt = (
        f"A ball is projected vertically upwards at $v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ from the top of a vertical tower. "
        f"It hits the ground at the base of the tower $\\Delta t = {_fmt_sa(t_total)}\\text{{ s}}$ after launch.\n\n"
        f"Calculate the height ($h$) of the tower."
    )
    ans = f"$h = {_fmt_sa(h_cliff)}\\text{{ m}}$"
    d1 = f"$h = {_fmt_sa(round(4.9 * (t_total ** 2) + vi * t_total, 2))}\\text{{ m}}$"
    d2 = f"$h = {_fmt_sa(round(4.9 * (t_total ** 2), 2))}\\text{{ m}}$"
    d3 = f"$h = {_fmt_sa(round(vi * t_total, 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Apply Delta_y = v_i*Delta_t + 0,5*g*Delta_t^2 (upwards positive)", "op": f"\\Delta y = ({_fmt_sa(vi)})({_fmt_sa(t_total)}) + \\frac{{1}}{{2}}(-9{{,}}8)({_fmt_sa(t_total)})^2", "to": f"\\Delta y = -{_fmt_sa(h_cliff)}\\text{{ m}}"},
        {"rule": "Interpret magnitude of displacement as tower height", "op": f"h = |\\Delta y| = {_fmt_sa(h_cliff)}\\text{{ m}}", "to": f"{_fmt_sa(h_cliff)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="With upwards as positive, v_i is positive and g = -9,8 m/s^2.",
        t2=f"Calculate delta_y = ({_fmt_sa(vi)})({_fmt_sa(t_total)}) - 4,9({_fmt_sa(t_total)})^2 = -{_fmt_sa(h_cliff)} m.",
        t3=f"The height of the tower is {_fmt_sa(h_cliff)} m.",
        misconceptions=["adding_upward_vi_t_and_downward_gt2", "confusing_total_distance_with_displacement"],
        marks=3,
    )


def _build_23(rng: random.Random) -> Dict[str, Any]:
    sub = "23_distance_travelled_in_nth_second_of_free_fall"
    n_sec = rng.choice([2, 3, 4, 5])
    # Distance between t = n-1 and t = n for dropped object: 4.9*(n^2 - (n-1)^2) = 4.9*(2n - 1)
    y_n = round(4.9 * (n_sec ** 2), 2)
    y_prev = round(4.9 * ((n_sec - 1) ** 2), 2)
    d_nth = round(y_n - y_prev, 2)

    prompt = (
        f"A lead sphere is dropped from rest from a tall tower ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"Calculate the vertical distance ($\\Delta y$) fallen by the sphere **specifically during the {n_sec}th second** of its fall "
        f"(i.e., between $t = {n_sec - 1}\\text{{ s}}$ and $t = {n_sec}\\text{{ s}}$)."
    )
    ans = f"$\\Delta y = {_fmt_sa(d_nth)}\\text{{ m}}$"
    d1 = f"$\\Delta y = {_fmt_sa(y_n)}\\text{{ m}}$"
    d2 = f"$\\Delta y = {_fmt_sa(y_prev)}\\text{{ m}}$"
    d3 = f"$\\Delta y = {_fmt_sa(round(G * n_sec, 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": f"Calculate total distance fallen after {n_sec} s and after {n_sec-1} s", "op": f"y_{{{n_sec}}} = 4{{,}}9({n_sec})^2 = {_fmt_sa(y_n)}\\text{{ m}},\\; y_{{{n_sec-1}}} = 4{{,}}9({n_sec-1})^2 = {_fmt_sa(y_prev)}\\text{{ m}}", "to": "\\text{Cumulative distances found}"},
        {"rule": "Subtract to find distance covered during the n-th second", "op": f"\\Delta y = {_fmt_sa(y_n)} - {_fmt_sa(y_prev)}", "to": f"{_fmt_sa(d_nth)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1=f"The {n_sec}th second is the 1-second interval from t = {n_sec - 1} s to t = {n_sec} s, NOT the entire {n_sec} seconds from t = 0.",
        t2=f"Calculate distance after {n_sec} s ({_fmt_sa(y_n)} m) minus distance after {n_sec - 1} s ({_fmt_sa(y_prev)} m).",
        t3=f"Distance in the {n_sec}th second = {_fmt_sa(y_n)} - {_fmt_sa(y_prev)} = {_fmt_sa(d_nth)} m.",
        misconceptions=["calculating_cumulative_distance_instead_of_nth_second_interval", "using_velocity_as_distance"],
        marks=4,
    )


def _build_24(rng: random.Random) -> Dict[str, Any]:
    sub = "24_window_passage_initial_drop_height"
    # Dropped from roof; reaches top of window after t_top seconds
    t_top = rng.choice([1.0, 1.5, 2.0])
    dt_win = rng.choice([0.2, 0.4, 0.5])
    v_top = round(G * t_top, 2)
    h_win = round(v_top * dt_win + 0.5 * G * (dt_win ** 2), 3)
    h_above_win = round(0.5 * G * (t_top ** 2), 2)

    prompt = (
        f"A flower pot falls from rest from a roof above a window. The window has a vertical height of "
        f"$h_{{\\text{{win}}}} = {_fmt_sa(h_win, 3)}\\text{{ m}}$, and the pot takes $\\Delta t = {_fmt_sa(dt_win)}\\text{{ s}}$ "
        f"to pass from the top of the window to the bottom of the window.\n\n"
        f"1. Calculate the speed ($v_{{\\text{{top}}}}$) of the pot at the top of the window.\n"
        f"2. Calculate the distance ($d$) from the roof to the top of the window."
    )
    ans = f"$v_{{\\text{{top}}}} = {_fmt_sa(v_top)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; d = {_fmt_sa(h_above_win)}\\text{{ m}}$"
    d1 = f"$v_{{\\text{{top}}}} = {_fmt_sa(round(h_win / dt_win, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; d = {_fmt_sa(h_above_win)}\\text{{ m}}$"
    d2 = f"$v_{{\\text{{top}}}} = {_fmt_sa(v_top)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; d = {_fmt_sa(round(h_above_win * 2, 2))}\\text{{ m}}$"
    d3 = f"$v_{{\\text{{top}}}} = 0\\text{{ m}}\\cdot\\text{{s}}^{{-1}},\\; d = {_fmt_sa(h_win)}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Find speed at top of window using Delta_y = v_top*t + 0,5*g*t^2", "op": f"{_fmt_sa(h_win, 3)} = v_{{\\text{{top}}}}({_fmt_sa(dt_win)}) + 4{{,}}9({_fmt_sa(dt_win)})^2", "to": f"v_{{\\text{{top}}}} = {_fmt_sa(v_top)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Find drop distance above window using v_top^2 = 0 + 2*g*d", "op": f"d = \\frac{{({_fmt_sa(v_top)})^2}}{{19{{,}}6}}", "to": f"{_fmt_sa(h_above_win)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The pot is already moving at v_top when it reaches the top of the window.",
        t2=f"Use h_win = v_top*dt + 4,9*dt^2 to find v_top = {_fmt_sa(v_top)} m/s.",
        t3=f"Then use v_top^2 = 2*g*d to find d = {_fmt_sa(h_above_win)} m above the window.",
        misconceptions=["assuming_velocity_at_top_of_window_is_zero", "using_average_speed_as_initial_speed"],
        marks=4,
    )


def _build_25(rng: random.Random) -> Dict[str, Any]:
    sub = "25_two_stage_rocket_powered_ascent_then_free_fall"
    a_engine = rng.choice([14.7, 19.6])
    t_burn = rng.choice([2.0, 3.0, 4.0])
    # Stage 1: upward acceleration a_engine for t_burn
    h1 = round(0.5 * a_engine * (t_burn ** 2), 2)
    v_burnout = round(a_engine * t_burn, 2)
    # Stage 2: free fall upward from burnout to apex
    h2 = round((v_burnout ** 2) / (2 * G), 2)
    h_total = round(h1 + h2, 2)

    prompt = (
        f"A model rocket is launched vertically upwards from rest on the ground. Its engine provides a constant upward "
        f"resultant acceleration of $a = {_fmt_sa(a_engine)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ for $t_1 = {_fmt_sa(t_burn)}\\text{{ s}}$ "
        f"until the fuel is exhausted at height $h_1 = {_fmt_sa(h1)}\\text{{ m}}$ and upward speed $v_1 = {_fmt_sa(v_burnout)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"After burnout, the rocket continues upwards in free fall ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ downwards).\n\n"
        f"Calculate the **maximum height** ($H_{{\\max}}$) above the ground reached by the rocket."
    )
    ans = f"$H_{{\\max}} = {_fmt_sa(h_total)}\\text{{ m}}$"
    d1 = f"$H_{{\\max}} = {_fmt_sa(h1)}\\text{{ m}}$"
    d2 = f"$H_{{\\max}} = {_fmt_sa(h2)}\\text{{ m}}$"
    d3 = f"$H_{{\\max}} = {_fmt_sa(round(abs(h2 - h1), 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)
    steps = [
        {"rule": "Calculate additional height gained during free-fall coasting phase", "op": f"h_2 = \\frac{{v_1^2}}{{2g}} = \\frac{{({_fmt_sa(v_burnout)})^2}}{{19{{,}}6}}", "to": f"{_fmt_sa(h2)}\\text{{ m}}"},
        {"rule": "Sum powered ascent height and coasting height", "op": f"H_{{\\max}} = h_1 + h_2 = {_fmt_sa(h1)} + {_fmt_sa(h2)}", "to": f"{_fmt_sa(h_total)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The rocket does NOT stop immediately when the fuel runs out; its upward momentum carries it higher under free fall.",
        t2=f"During the coasting phase, v_i = {_fmt_sa(v_burnout)} m/s and v_f = 0 at the apex, so h_2 = v_1^2 / 19,6 = {_fmt_sa(h2)} m.",
        t3=f"Total maximum height H_max = {_fmt_sa(h1)} + {_fmt_sa(h2)} = {_fmt_sa(h_total)} m.",
        misconceptions=["assuming_rocket_stops_instantly_at_fuel_burnout", "applying_free_fall_to_powered_engine_phase"],
        marks=4,
    )


# =========================================================================== #
# Export Mapping
# =========================================================================== #

BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_free_fall_and_projectile_definition": _build_01,
    "02_acceleration_at_maximum_height_apex": _build_02,
    "03_sign_convention_upward_vs_downward_positive": _build_03,
    "04_dropped_object_velocity_after_time": _build_04,
    "05_dropped_object_vertical_displacement": _build_05,
    "06_dropped_object_time_to_reach_ground": _build_06,
    "07_dropped_object_final_impact_speed": _build_07,
    "08_projected_downwards_final_velocity": _build_08,
    "09_projected_downwards_displacement_in_time": _build_09,
    "10_projected_downwards_time_to_ground": _build_10,
    "11_projected_upwards_time_to_maximum_height": _build_11,
    "12_projected_upwards_maximum_height_reached": _build_12,
    "13_time_symmetry_upward_and_downward_flight": _build_13,
    "14_velocity_symmetry_at_equal_heights": _build_14,
    "15_projected_upwards_velocity_at_given_time": _build_15,
    "16_projected_upwards_height_at_given_time": _build_16,
    "17_time_interval_above_given_height": _build_17,
    "18_cliff_launch_upwards_maximum_height_above_ground": _build_18,
    "19_cliff_launch_upwards_final_impact_velocity": _build_19,
    "20_cliff_launch_upwards_total_flight_time": _build_20,
    "21_cliff_launch_speed_from_known_flight_time": _build_21,
    "22_cliff_height_from_upward_launch_and_time": _build_22,
    "23_distance_travelled_in_nth_second_of_free_fall": _build_23,
    "24_window_passage_initial_drop_height": _build_24,
    "25_two_stage_rocket_powered_ascent_then_free_fall": _build_25,
}

SUBSKILLS_01_25: List[str] = list(BUILDERS_01_25.keys())
