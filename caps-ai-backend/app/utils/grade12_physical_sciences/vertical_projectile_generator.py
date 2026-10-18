"""Grade 12 Physical Sciences — Vertical Projectile Motion in 1D (Deterministic 6-Pillar Generator).
Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 1/02. Vertical projectile motion in one dimension.md

Complies strictly with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=1, caps_weight_percent=20, suggested_duration_mins=12.
2. Deconstructibility: Compound multi-stage projectile scenarios and atomic elementary sub-drills (elementary_projectile_apex_time, elementary_projectile_max_height, elementary_projectile_impact_velocity, elementary_cliff_trajectory).
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
    "A ball is thrown vertically upwards from the edge of a flat school building roof,",
    "From the top of a cliff overlooking the ocean, a stone is projected vertically,",
    "A distress flare is fired vertically upwards from a rescue boat,"
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
        f"{hook} with an initial speed of {_fmt_sa(vi)} m·s⁻¹. Ignore air resistance and take g = 9,8 m·s⁻².\n\n"
        f"1. Define the term 'projectile'.\n"
        f"2. State the magnitude and direction of the ball's acceleration at its highest point (apex).\n"
        f"3. Calculate the time taken, in seconds, for the ball to reach its maximum height.\n"
        f"4. Calculate the maximum height reached above the ground in meters.\n"
        f"5. What is the ball's velocity upon returning to the ground?"
    )
    ans_str = f"1. An object upon which the only force acting is gravity; 2. 9,8 m/s^2 downwards; 3. {_fmt_sa(t_apex)} s; 4. {_fmt_sa(h_max)} m; 5. {_fmt_sa(vi)} m/s downwards"
    memo = (
        "1. A projectile is an object which has been given an initial velocity and on which the only acting force is gravity. [2]\n"
        "2. Acceleration at apex: 9,8 m·s⁻² downwards (gravity is constant throughout free-fall). [2]\n"
        f"3. Taking upwards as positive:\n"
        f"   vf = vi + g·Δt => 0 = {_fmt_sa(vi)} + (-9,8)·Δt [1M]\n"
        f"   Δt = {_fmt_sa(vi)} / 9,8 = {_fmt_sa(t_apex, 2)} s [1A]\n"
        f"4. vf² = vi² + 2g·Δy => 0 = ({_fmt_sa(vi)})² + 2(-9,8)·Δy [1M]\n"
        f"   Δy = ({_fmt_sa(vi)})² / (19,6) = {_fmt_sa(h_max, 2)} m [1A]\n"
        f"5. Velocity on return = {_fmt_sa(vi)} m·s⁻¹ downwards (by symmetry of motion in a vacuum). [1A]"
    )
    hints = {
        "tier_1": "At apex, vertical velocity is zero, but acceleration is still 9.8 m/s^2 downwards.",
        "tier_2": "Use vf = vi + a*t with vf = 0. Use vf^2 = vi^2 + 2*a*dy for maximum height.",
        "tier_3": f"1. Free fall object. 2. 9,8 m/s^2 down. 3. t = {_fmt_sa(vi)} / 9,8 = {_fmt_sa(t_apex, 2)} s. 4. h = {_fmt_sa(h_max, 2)} m. 5. {_fmt_sa(vi)} m/s down.",
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
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 8,
        "hints": hints,
        "misconception_tags": ["apex_acceleration_zero_misconception", "sign_convention_inconsistency"],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_1", "desc": "Projectile definition", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Acceleration at apex identification", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Time to apex calculation", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Maximum height calculation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_cliff_launch_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Vertical projectile launched upwards from a cliff/building edge."""
    hook = r.choice(PROMPT_LEAD_HOOKS_PROJECTILE)
    qid = _make_id("proj12_cliff", seed, idx)

    cliff_height = r.choice([25.0, 30.0, 40.0, 50.0, 60.0, 80.0])
    vi = r.choice([10.0, 15.0, 20.0, 25.0])

    # vf^2 = vi^2 + 2 * g * cliff_height (when falling down to ground, delta_y = -cliff_height)
    vf_squared = (vi ** 2) + (2 * G_ACCEL * cliff_height)
    vf_ground = math.sqrt(vf_squared)
    # Total flight time: vf = vi + a*t => -vf_ground = vi - g*t => t = (vi + vf_ground) / g
    t_flight = (vi + vf_ground) / G_ACCEL

    prompt = (
        f"{hook} from the top edge of a building of height {_fmt_sa(cliff_height)} m above the ground. "
        f"The projectile is thrown vertically upwards with an initial speed of {_fmt_sa(vi)} m·s⁻¹. "
        f"It rises to its highest point and then falls past the roofline straight to the ground below. "
        f"(Take g = 9,8 m·s⁻²).\n\n"
        f"1. Calculate the magnitude of the projectile's velocity just before it hits the ground in m·s⁻¹.\n"
        f"2. Calculate the total time of flight, from launch until striking the ground, in seconds.\n"
        f"3. Sketch or describe the shape of the position-versus-time graph for this motion."
    )
    ans_str = f"1. {_fmt_sa(vf_ground)} m/s; 2. {_fmt_sa(t_flight)} s; 3. Inverted parabolic curve starting at {_fmt_sa(cliff_height)} m, rising to apex, and dropping to 0 m."
    memo = (
        f"1. Taking upwards as positive (displacement to ground Δy = -{_fmt_sa(cliff_height)} m):\n"
        f"   vf² = vi² + 2g·Δy [1M]\n"
        f"   vf² = ({_fmt_sa(vi)})² + 2(-9,8)(-{_fmt_sa(cliff_height)}) = {_fmt_sa(vi**2)} + {_fmt_sa(19.6 * cliff_height)} = {_fmt_sa(vf_squared, 2)} [1M]\n"
        f"   vf = -√({_fmt_sa(vf_squared, 2)}) = -{_fmt_sa(vf_ground, 2)} m·s⁻¹\n"
        f"   Magnitude = {_fmt_sa(vf_ground, 2)} m·s⁻¹ [1A]\n"
        f"2. vf = vi + g·Δt [1M]\n"
        f"   -{_fmt_sa(vf_ground, 2)} = {_fmt_sa(vi)} + (-9,8)·Δt\n"
        f"   -9,8·Δt = -({_fmt_sa(vi)} + {_fmt_sa(vf_ground, 2)}) => Δt = {_fmt_sa(t_flight, 2)} s [1A]\n"
        "3. Position-time graph: Inverted parabola starting at positive initial position y0 > 0, curving upwards to a peak, then curving downwards through y = 0. [2]"
    )
    hints = {
        "tier_1": "Watch your signs: if up is positive, displacement to the ground below is negative (-h).",
        "tier_2": "vf^2 = vi^2 + 2*g*dy with dy = -cliff_height gives ground impact speed. Then use vf = vi + g*t.",
        "tier_3": f"1. vf^2 = {_fmt_sa(vi)}^2 + 2(9.8)({_fmt_sa(cliff_height)}) => vf = {_fmt_sa(vf_ground, 2)} m/s. 2. t = ({_fmt_sa(vi)} + {_fmt_sa(vf_ground, 2)}) / 9.8 = {_fmt_sa(t_flight, 2)} s.",
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
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 7,
        "hints": hints,
        "misconception_tags": ["omitted_initial_cliff_height", "sign_convention_inconsistency"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Ground velocity calculation (formula + substitution)", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Total flight time calculation (vf = vi + gt)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Position-time graph description", "marks": 2, "editable": True},
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
