"""Grade 12 Physical Sciences — Vertical Projectile Motion in 1D (Deterministic 6-Pillar Generator).
Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 1/02. Vertical projectile motion in one dimension.md

Complies strictly with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=1, caps_weight_percent=20, suggested_duration_mins=12.
2. Deconstructibility: Compound multi-stage projectile scenarios and atomic elementary sub-drills.
3. Standardized Misconceptions: apex_acceleration_zero_misconception, sign_convention_inconsistency, omitted_initial_cliff_height.
4. Teacher-Editable Marking Schema with [M] method and [A] accuracy marks.
5. Deterministic 3-Tier Pre-Baked Hints.
6. South African comma decimal convention (",").
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "grade12_vertical_projectile"
G_ACCEL = 9.8  # m/s^2 downwards

PROMPT_LEAD_HOOKS_PROJECTILE = [
    "During an athletics high-jump training session, a tennis ball is launched straight upwards,",
    "In a Grade 12 physics experiment measuring gravitational free-fall using a photogate timer,",
    "A ball is thrown vertically upwards from a horizontal launch pad,",
    "During a kinematics investigation, a projectile is launched vertically upwards,",
    "A distress flare is fired vertically upwards from a stationary platform,",
]


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_ground_launch_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Vertical projectile launched from ground upwards."""
    hook = r.choice(PROMPT_LEAD_HOOKS_PROJECTILE)
    qid = _make_id("proj12_ground", seed, idx)

    vi = r.choice([14.7, 19.6, 24.5, 29.4, 34.3, 39.2, 44.1])
    t_apex = vi / G_ACCEL
    h_max = (vi ** 2) / (2 * G_ACCEL)
    t_total = 2 * t_apex

    prompt = (
        f"Refer to the velocity–time (\\(v\\text{{–}}t\\)) motion graph for a projectile. "
        f"{hook} with an initial upward speed of \\(v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\). Ignore air resistance and take \\(g = 9,8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}\\) downwards.\n\n"
        f"1. Define the term projectile. (2)\n"
        f"2. State the magnitude and direction of the projectile's acceleration at its highest point (apex at \\(t = {_fmt_sa(t_apex)}\\text{{ s}}\\)), and explain how this is represented by the gradient of the \\(v\\text{{–}}t\\) graph. (2)\n"
        f"3. Verify by calculation that the time taken to reach maximum height is \\({_fmt_sa(t_apex)}\\text{{ s}}\\). (2)\n"
        f"4. Calculate the maximum vertical height (\\(\\Delta y_{{\\max}}\\)) reached above the launch point, represented by the shaded area under the \\(v\\text{{–}}t\\) graph from \\(t = 0\\text{{ s}}\\) to \\(t = {_fmt_sa(t_apex)}\\text{{ s}}\\). (2)"
    )
    memo = (
        "Step 1: Definition of a projectile:\n"
        "A projectile is an object upon which the only force acting is the gravitational force (weight).\n\n"
        "Step 2: Acceleration at the apex:\n"
        "9,8 m·s⁻² downwards; the v–t graph has a constant negative gradient equal to g = -9,8 m·s⁻² throughout the entire motion.\n\n"
        f"Step 3: Time to reach maximum height (taking upwards as positive, v_f = 0 m·s⁻¹):\n"
        f"v_f = v_i + g Δt\n"
        f"0 = {_fmt_sa(vi)} + (-9,8) Δt => Δt = {_fmt_sa(vi)} ÷ 9,8 = {_fmt_sa(t_apex, 2)} s\n\n"
        f"Step 4: Maximum height above the ground (Area of triangle = 0,5 × base × height or v_f² = v_i² + 2g Δy):\n"
        f"Δy_max = 0,5 × {_fmt_sa(t_apex, 2)} × {_fmt_sa(vi)} = {_fmt_sa(h_max, 2)} m"
    )
    hints = {
        "tier_1": "At the apex, vertical velocity is zero, but the gradient of the v–t graph (acceleration) remains constant at 9,8 m·s⁻² downwards.",
        "tier_2": "Use v_f = v_i + g Δt with v_f = 0, and find maximum height from the area under the v–t graph: Δy_max = 0,5 × t_apex × v_i.",
        "tier_3": memo,
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 12,
        "mode": mode,
        "topic": TOPIC,
        "question_type": "short_answer",
        "modality": "motion_graph",
        "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin_letter") or locals().get("target_pin") else "context",
            "kind": "motion_graph",
            "type": "motion_graph",
            "v0": round(float(vi), 2),
            "t_apex": round(float(t_apex), 2),
            "t_total": round(float(t_total), 2),
            "h_max": round(float(h_max), 2),
            "graph_type": "velocity_time",
        },
        "question": prompt,
        "prompt": prompt,
        "correct_answer": memo,
        "sample_answer": memo,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 8,
        "hints": hints,
        "misconception_tags": ["apex_acceleration_zero_misconception", "sign_convention_inconsistency"],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_1", "desc": "1. Projectile definition: object upon which the only force acting is gravity", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "2. Acceleration at apex = 9,8 m·s⁻² downwards (constant gradient of v-t graph)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": f"3. Time to apex calculation: 0 = {_fmt_sa(vi)} - 9,8 Δt => Δt = {_fmt_sa(t_apex, 2)} s", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": f"4. Maximum height calculation: Δy_max = {_fmt_sa(h_max, 2)} m", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_cliff_launch_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Vertical projectile launched upwards from a cliff/building edge."""
    hook = r.choice(PROMPT_LEAD_HOOKS_PROJECTILE)
    qid = _make_id("proj12_cliff", seed, idx)

    cliff_height = r.choice([25.0, 30.0, 40.0, 50.0, 60.0])
    vi = r.choice([14.7, 19.6, 24.5])
    t_apex = vi / G_ACCEL
    h_above_cliff = (vi ** 2) / (2 * G_ACCEL)

    vf_squared = (vi ** 2) + (2 * G_ACCEL * cliff_height)
    vf_ground = math.sqrt(vf_squared)
    t_flight = (vi + vf_ground) / G_ACCEL

    prompt = (
        f"Refer to the velocity–time (\\(v\\text{{–}}t\\)) motion graph for a vertical projectile.\n"
        f"{hook} from a platform of height \\({_fmt_sa(cliff_height)}\\text{{ m}}\\) above the ground with an initial upward velocity of \\(v_i = {_fmt_sa(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\). "
        f"It reaches its apex at \\(t = {_fmt_sa(t_apex)}\\text{{ s}}\\) and then falls past the launch level to strike the ground below. (Take \\(g = 9,8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}\\) downwards.)\n\n"
        f"1. Calculate the maximum height above the launch platform reached at \\(t = {_fmt_sa(t_apex)}\\text{{ s}}\\) using the upward area of the \\(v\\text{{–}}t\\) graph. (2)\n"
        f"2. Calculate the magnitude of the projectile's velocity just before it hits the ground in \\(\\text{{m}}\\cdot\\text{{s}}^{{-1}}\\). (3)\n"
        f"3. Calculate the total time of flight from launch until striking the ground. (2)"
    )
    memo = (
        f"Step 1: Maximum height above launch platform at t = {_fmt_sa(t_apex, 2)} s:\n"
        f"Δy_up = 0,5 × base × height = 0,5 × {_fmt_sa(t_apex, 2)} × {_fmt_sa(vi)} = {_fmt_sa(h_above_cliff, 2)} m\n\n"
        f"Step 2: Velocity just before striking the ground (taking upwards as positive, net displacement Δy = -{_fmt_sa(cliff_height)} m):\n"
        f"v_f² = v_i² + 2g Δy\n"
        f"v_f² = ({_fmt_sa(vi)})² + 2(-9,8)(-{_fmt_sa(cliff_height)}) = {_fmt_sa(round(vf_squared, 2))}\n"
        f"Magnitude of impact velocity v_f = {_fmt_sa(vf_ground, 2)} m·s⁻¹ downwards.\n\n"
        f"Step 3: Total time of flight from launch to ground:\n"
        f"v_f = v_i + g Δt\n"
        f"-{_fmt_sa(vf_ground, 2)} = {_fmt_sa(vi)} + (-9,8) Δt => Δt = {_fmt_sa(t_flight, 2)} s"
    )
    hints = {
        "tier_1": "Watch your sign convention: taking upwards as positive, the net displacement from the cliff top to the ground below is Δy = -h.",
        "tier_2": "Use v_f² = v_i² + 2g Δy with Δy = -cliff_height to find impact speed, then use v_f = v_i + g Δt for total flight time.",
        "tier_3": memo,
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 12,
        "mode": mode,
        "topic": TOPIC,
        "question_type": "short_answer",
        "modality": "motion_graph",
        "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin_letter") or locals().get("target_pin") else "context",
            "kind": "motion_graph",
            "type": "motion_graph",
            "v0": round(float(vi), 2),
            "t_apex": round(float(t_apex), 2),
            "t_total": round(float(t_flight), 2),
            "h_cliff": round(float(cliff_height), 2),
            "graph_type": "velocity_time",
        },
        "question": prompt,
        "prompt": prompt,
        "correct_answer": memo,
        "sample_answer": memo,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 7,
        "hints": hints,
        "misconception_tags": ["omitted_initial_cliff_height", "sign_convention_inconsistency"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": f"1. Height above launch platform: Δy_up = 0,5 × {_fmt_sa(t_apex, 2)} × {_fmt_sa(vi)} = {_fmt_sa(h_above_cliff, 2)} m", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"2. Ground impact velocity: v_f = {_fmt_sa(vf_ground, 2)} m·s⁻¹ downwards", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": f"3. Total flight time: Δt = {_fmt_sa(t_flight, 2)} s", "marks": 2, "editable": True},
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
    grade: str = "12",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Grade 12 Physical Sciences Vertical Projectile Motion."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("ground", "max_height", "apex") or mode in ("elementary_projectile_apex_time", "elementary_projectile_max_height"):
            q = _generate_ground_launch_question(sub_r, sub_seed, i, mode)
        elif subskill in ("cliff", "building", "flight_time") or mode in ("elementary_projectile_impact_velocity", "elementary_cliff_trajectory"):
            q = _generate_cliff_launch_question(sub_r, sub_seed, i, mode)
        else:
            chosen = sub_r.choice(["ground", "cliff"])
            if chosen == "ground":
                q = _generate_ground_launch_question(sub_r, sub_seed, i, mode)
            else:
                q = _generate_cliff_launch_question(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
