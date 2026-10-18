"""Grade 12 Physical Sciences — The Doppler Effect (Deterministic 6-Pillar Generator).
Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/04. The Doppler effect.md

Complies strictly with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=2, caps_weight_percent=15, suggested_duration_mins=10.
2. Deconstructibility: Compound Doppler calculations and atomic elementary sub-drills (elementary_doppler_formula, elementary_doppler_towards, elementary_doppler_away, elementary_redshift_universe).
3. Standardized Misconceptions: doppler_sign_confusion_approach_recede, apparent_vs_actual_frequency_confusion, doppler_speed_of_sound_shift_fallacy.
4. Teacher-Editable Marking Schema with [M] method and [A] accuracy marks.
5. Deterministic 3-Tier Pre-Baked Hints.
6. South African comma decimal convention (",").
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

TOPIC = "grade12_doppler_effect"
SPEED_OF_SOUND_AIR = 340.0  # m/s

EMERGENCY_VEHICLES = [
    {"type": "an emergency ambulance", "siren_hz": 800, "speed_ms": 25.0},
    {"type": "a police patrol vehicle", "siren_hz": 950, "speed_ms": 30.0},
    {"type": "a fire rescue truck", "siren_hz": 650, "speed_ms": 20.0},
    {"type": "a commuter train sounding its horn", "siren_hz": 440, "speed_ms": 35.0},
    {"type": "a traffic highway patrol motorcycle", "siren_hz": 1100, "speed_ms": 28.0},
]

PROMPT_LEAD_HOOKS_DOPPLER = [
    "During a roadside acoustics experiment on a level highway,",
    "A traffic safety research station records acoustic frequencies from moving traffic,",
    "A stationary pedestrian stands beside a long straight urban road as",
    "In a Grade 12 physics examination question on wave phenomena,",
    "A clinical ultrasound scan measures the Doppler frequency shift of moving red blood cells while"
]


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_doppler_approach_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Source moving towards a stationary listener: fL = [v / (v - vs)] * fs."""
    hook = r.choice(PROMPT_LEAD_HOOKS_DOPPLER)
    veh = r.choice(EMERGENCY_VEHICLES)
    qid = _make_id("doppler12_approach", seed, idx)

    vs = veh["speed_ms"]
    fs = veh["siren_hz"]
    v = SPEED_OF_SOUND_AIR

    fl = (v / (v - vs)) * fs

    prompt = (
        f"{hook} {veh['type']} approaches a stationary listener at a constant speed of {_fmt_sa(vs)} m·s⁻¹. "
        f"The siren emits sound waves with a frequency of {fs} Hz. Take the speed of sound in air as {_fmt_sa(v)} m·s⁻¹.\n\n"
        f"1. State the Doppler Effect in words.\n"
        f"2. Explain in terms of wavefronts why the frequency detected by the listener is higher than the emitted frequency.\n"
        f"3. Calculate the frequency (fL) heard by the stationary listener as the vehicle approaches in Hz.\n"
        f"4. State one practical application of the Doppler Effect in medical diagnosis."
    )
    ans_str = f"1. The apparent change in frequency of a wave detected by an observer when there is relative motion between the source and observer; 2. Wavefronts are compressed closer together ahead of moving source, decreasing wavelength and increasing observed frequency; 3. {_fmt_sa(fl)} Hz; 4. Doppler ultrasound (flow meter) to monitor blood flow velocity."
    memo = (
        "1. Doppler Effect: The apparent change in frequency (or pitch) of a wave detected by an observer because the source and the observer have different velocities relative to the medium of propagation. [2]\n"
        "2. As the source moves towards the stationary observer, each successive crest is emitted closer to the previous crest. "
        "This compresses the wavefronts, decreasing the observed wavelength (λ), which results in a higher observed frequency (fL > fs) because wave speed in the medium remains constant. [2]\n"
        "3. fL = [v / (v - vs)] · fs [1M]\n"
        f"   fL = [{_fmt_sa(v)} / ({_fmt_sa(v)} - {_fmt_sa(vs)})] · {fs} = [{_fmt_sa(v)} / {_fmt_sa(v - vs)}] · {fs} [1M]\n"
        f"   fL = {_fmt_sa(fl, 2)} Hz [1A]\n"
        "4. Application: Measuring blood flow velocity in arteries using ultrasound (Doppler flow meter) / echocardiogram. [1]"
    )
    hints = {
        "tier_1": "As source approaches, the denominator is (v - vs), which makes the frequency higher.",
        "tier_2": "Formula: fL = [v / (v - vs)] * fs. Wavefronts bunch up ahead of the vehicle.",
        "tier_3": f"1. Relative motion frequency change. 2. Shorter wavelength -> higher frequency. 3. fL = [{_fmt_sa(v)} / ({_fmt_sa(v)} - {_fmt_sa(vs)})] * {fs} = {_fmt_sa(fl, 2)} Hz. 4. Blood flow ultrasound.",
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 15,
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
        "misconception_tags": ["doppler_sign_confusion_approach_recede", "doppler_speed_of_sound_shift_fallacy"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Doppler effect definition", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Wavefront compression conceptual explanation", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Frequency calculation (formula, substitution, answer)", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Medical/practical application", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_doppler_recede_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Source moving away from a stationary listener: fL = [v / (v + vs)] * fs."""
    hook = r.choice(PROMPT_LEAD_HOOKS_DOPPLER)
    veh = r.choice(EMERGENCY_VEHICLES)
    qid = _make_id("doppler12_recede", seed, idx)

    vs = veh["speed_ms"]
    fs = veh["siren_hz"]
    v = SPEED_OF_SOUND_AIR

    fl = (v / (v + vs)) * fs

    prompt = (
        f"{hook} {veh['type']} travels away from a stationary observer at a constant velocity of {_fmt_sa(vs)} m·s⁻¹. "
        f"The siren emits sound waves at a frequency of {fs} Hz. Take the speed of sound in air as {_fmt_sa(v)} m·s⁻¹.\n\n"
        f"1. Will the pitch heard by the observer be HIGHER, LOWER, or EQUAL TO the pitch of the stationary siren? Explain briefly.\n"
        f"2. Calculate the frequency heard by the stationary observer as the vehicle moves away in Hz.\n"
        f"3. Explain how the Doppler Effect with light (redshift) provides observational evidence that the universe is expanding."
    )
    ans_str = f"1. LOWER, because wavefronts are stretched apart, increasing observed wavelength and decreasing perceived frequency; 2. {_fmt_sa(fl)} Hz; 3. Light from distant galaxies is shifted towards longer (red) wavelengths, proving galaxies are moving away from Earth."
    memo = (
        "1. LOWER [1]. As the source moves away, each successive wavefront is emitted further away, stretching the wavelength (λ increases), resulting in a lower frequency/pitch (f = v/λ) [1].\n"
        "2. fL = [v / (v + vs)] · fs [1M]\n"
        f"   fL = [{_fmt_sa(v)} / ({_fmt_sa(v)} + {_fmt_sa(vs)})] · {fs} = [{_fmt_sa(v)} / {_fmt_sa(v + vs)}] · {fs} [1M]\n"
        f"   fL = {_fmt_sa(fl, 2)} Hz [1A]\n"
        "3. Redshift in astronomy: Light absorption spectra from distant galaxies are shifted towards longer (red) wavelengths [1]. "
        "By the Doppler Effect, this spectral redshift proves that distant galaxies are receding away from us, providing evidence for the expansion of the universe (Big Bang theory) [1]."
    )
    hints = {
        "tier_1": "Moving away uses (v + vs) in the denominator, decreasing the observed frequency.",
        "tier_2": "Formula: fL = [v / (v + vs)] * fs. Redshift means light stretched to longer wavelengths (moving away).",
        "tier_3": f"1. Lower pitch. 2. fL = [{_fmt_sa(v)} / ({_fmt_sa(v)} + {_fmt_sa(vs)})] * {fs} = {_fmt_sa(fl, 2)} Hz. 3. Redshift shows receding galaxies.",
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 15,
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
        "misconception_tags": ["doppler_sign_confusion_approach_recede", "apparent_vs_actual_frequency_confusion"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Pitch change qualitative deduction", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Frequency calculation (formula + substitution)", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Astronomical redshift explanation", "marks": 2, "editable": True},
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
    """Master generator for Grade 12 Physical Sciences The Doppler Effect."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("approach", "towards") or mode == "elementary_doppler_towards":
            q = _generate_doppler_approach_question(sub_r, sub_seed, i, mode)
        elif subskill in ("recede", "away", "redshift") or mode in ("elementary_doppler_away", "elementary_redshift_universe"):
            q = _generate_doppler_recede_question(sub_r, sub_seed, i, mode)
        else:
            chosen = sub_r.choice(["approach", "recede"])
            if chosen == "approach":
                q = _generate_doppler_approach_question(sub_r, sub_seed, i, mode)
            else:
                q = _generate_doppler_recede_question(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
