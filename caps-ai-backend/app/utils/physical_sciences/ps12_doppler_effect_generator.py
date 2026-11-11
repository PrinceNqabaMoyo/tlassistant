"""Physical Sciences Grade 12 — The Doppler Effect Dedicated Generator.

Curriculum Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/04. The Doppler effect.md

Complies with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=2, caps_weight_percent=15, suggested_duration_mins=8.
2. Deconstructible compound questions & atomic sub-drills.
3. Standardized Misconceptions.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Hints.
6. South African comma decimal convention (",").
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.physical_sciences.physical_sciences_builders import build_doppler_effect_question

TOPIC = "grade12_doppler_effect"
SPEED_OF_SOUND_AIR = 340.0  # m/s

EMERGENCY_VEHICLES = [
    {"type": "an emergency ambulance", "siren_hz": 800, "speed_ms": 25.0},
    {"type": "a police patrol vehicle", "siren_hz": 950, "speed_ms": 30.0},
    {"type": "a fire rescue truck", "siren_hz": 650, "speed_ms": 20.0},
    {"type": "a commuter train sounding its horn", "siren_hz": 440, "speed_ms": 35.0},
    {"type": "a traffic highway patrol motorcycle", "siren_hz": 1100, "speed_ms": 28.0},
]


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_doppler_calculation_question(
    r: random.Random, seed: Optional[int], idx: int, mode: str
) -> Dict[str, Any]:
    """Source moving towards and then away from a stationary observer."""
    veh = r.choice(EMERGENCY_VEHICLES)
    qid = _make_id("doppler12_calc", seed, idx)

    vs = veh["speed_ms"]
    fs = veh["siren_hz"]
    v = SPEED_OF_SOUND_AIR

    fl_approach = (v / (v - vs)) * fs
    fl_recede = (v / (v + vs)) * fs

    prompt = (
        f"{veh['type'].capitalize()} travels along a straight level road at a constant speed of {_fmt_sa(vs)} m·s⁻¹. "
        f"The siren emits sound waves with a frequency of {fs} Hz. Take the speed of sound in air as {_fmt_sa(v)} m·s⁻¹.\n\n"
        f"1. State the Doppler Effect in words.\n"
        f"2. Explain in terms of wavefronts why the pitch heard by a stationary observer increases as the vehicle approaches.\n"
        f"3. Calculate the frequency ($f_L$) detected by a stationary observer as the vehicle approaches in Hz.\n"
        f"4. Calculate the frequency ($f_L$) detected by the observer after the vehicle passes and recedes into the distance in Hz.\n"
        f"5. Name ONE application of the Doppler Effect in medicine and ONE in astrophysics."
    )

    ans_str = (
        f"1. Apparent change in frequency of a wave detected by an observer when source and observer move relative to each other; "
        f"2. Wavefronts compressed ahead, decreasing wavelength, increasing frequency; "
        f"3. fL_approach = {_fmt_sa(fl_approach)} Hz; "
        f"4. fL_recede = {_fmt_sa(fl_recede)} Hz; "
        f"5. Medicine: Doppler ultrasound (blood flow); Astrophysics: Redshift (expanding universe)."
    )

    memo = (
        f"1. Doppler Effect definition [2]: The apparent change in frequency (or pitch) of a wave detected by an observer "
        f"because the source and observer have different velocities relative to the medium of propagation. [2]\n"
        f"2. Wavefront explanation [2]: As the source moves towards the observer, each successive crest is emitted closer "
        f"to the previous crest, compressing the wavefronts ahead of the source. This decreases the observed wavelength ($\\lambda$), "
        f"resulting in a higher observed frequency ($f_L > f_s$) because wave speed $v$ in air is constant. [2]\n"
        f"3. Approaching frequency [3]:\n"
        f"   $$f_L = \\left(\\frac{{v}}{{v - v_s}}\\right) f_s = \\left(\\frac{{{_fmt_sa(v)}}}{{{_fmt_sa(v)} - {_fmt_sa(vs)}}}\\right) ({fs}) = \\left(\\frac{{{_fmt_sa(v)}}}{{{_fmt_sa(v - vs)}}}\\right) ({fs}) = {_fmt_sa(fl_approach)}\\text{{ Hz}}$$ [1M + 1M + 1A]\n"
        f"4. Receding frequency [3]:\n"
        f"   $$f_L = \\left(\\frac{{v}}{{v + v_s}}\\right) f_s = \\left(\\frac{{{_fmt_sa(v)}}}{{{_fmt_sa(v)} + {_fmt_sa(vs)}}}\\right) ({fs}) = \\left(\\frac{{{_fmt_sa(v)}}}{{{_fmt_sa(v + vs)}}}\\right) ({fs}) = {_fmt_sa(fl_recede)}\\text{{ Hz}}$$ [1M + 1M + 1A]\n"
        f"5. Applications [2]:\n"
        f"   - Medicine: Doppler ultrasound flowmeter to detect heartbeat/blood flow velocity. [1]\n"
        f"   - Astrophysics: Redshift of distant galaxies providing evidence that the universe is expanding. [1]"
    )

    hints = {
        "tier_1": "Formula: fL = [v / (v - vs)] * fs when approaching, and fL = [v / (v + vs)] * fs when receding.",
        "tier_2": f"Approaching: fL = [{_fmt_sa(v)} / ({_fmt_sa(v)} - {_fmt_sa(vs)})] * {fs}. Receding: fL = [{_fmt_sa(v)} / ({_fmt_sa(v)} + {_fmt_sa(vs)})] * {fs}.",
        "tier_3": f"fL (approach) = {_fmt_sa(fl_approach)} Hz. fL (recede) = {_fmt_sa(fl_recede)} Hz.",
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 9,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 12,
        "hints": hints,
        "misconception_tags": [
            "doppler_sign_confusion_approach_recede",
            "apparent_vs_actual_frequency_confusion",
            "doppler_speed_of_sound_shift_fallacy",
        ],
        "marking_schema": {
            "total_marks": 12,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of Doppler Effect", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Wavefront compression explanation", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Approaching frequency calculation", "marks": 3, "editable": True},
                {"id": "mp_4", "desc": "Receding frequency calculation", "marks": 3, "editable": True},
                {"id": "mp_5", "desc": "Applications in medicine and astrophysics", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "omitted_hz_unit", "penalty": -1}],
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
    """Master generation endpoint for Grade 12 Doppler Effect."""
    r = random.Random(seed)
    questions = []

    for i in range(count):
        sub_seed = (seed + i * 47) if seed is not None else random.randint(1000, 99999)

        if mode == "scaffold" or subskill == "doppler_wavefront_diagram":
            q = build_doppler_effect_question(seed=sub_seed, grade=12, mode=mode)
        elif mode == "elementary_doppler_calc":
            q = _generate_doppler_calculation_question(r, sub_seed, i, mode)
        else:
            # Alternating progression between visual wavefront inspection and Doppler equations
            if i % 2 == 0:
                q = build_doppler_effect_question(seed=sub_seed, grade=12, mode=mode)
            else:
                q = _generate_doppler_calculation_question(r, sub_seed, i, mode)

        questions.append(q)

    return questions
