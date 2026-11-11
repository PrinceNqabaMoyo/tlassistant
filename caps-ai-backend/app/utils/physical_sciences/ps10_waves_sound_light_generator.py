"""Physical Sciences Grade 10 — Waves, Sound & Light Dedicated Generator.

Curriculum Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/07. Transverse pulses.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/08. Transverse waves.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/09. Longitudinal waves.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/10. Sound.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/11. Electromagnetic radiation.md

Complies with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=1, caps_weight_percent=20, suggested_duration_mins=8.
2. Deconstructible compound questions & atomic sub-drills.
3. Standardized Misconceptions.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Hints.
6. South African comma decimal convention (",").
"""

from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.physical_sciences.physical_sciences_builders import build_transverse_wave_question

TOPIC = "grade10_waves_sound_light"
SPEED_OF_SOUND_AIR = 340.0  # m/s at 20 °C
SPEED_OF_LIGHT = 3.0e8      # m/s
PLANCK_CONSTANT = 6.63e-34  # J·s

PROMPT_LEAD_HOOKS_WAVES = [
    "In a physics laboratory investigation on wave motion,",
    "A ripple tank is set up to generate periodic water pulses across a shallow basin,",
    "A sound technician analyzes acoustic reflections using an ultrasonic sensor,",
    "During an offshore geophysical survey using sonar echo-sounding,",
    "An astronomical observatory monitors incoming electromagnetic radiation from a distant nebula,",
]

EM_SPECTRUM_BANDS = [
    {"name": "Radio waves", "freq_exp": 7, "freq_base": 3.0, "use": "broadcasting and telecommunication"},
    {"name": "Microwaves", "freq_exp": 10, "freq_base": 2.5, "use": "radar and satellite transmissions"},
    {"name": "Infrared radiation", "freq_exp": 13, "freq_base": 4.0, "use": "thermal imaging and remote controls"},
    {"name": "Visible light", "freq_exp": 14, "freq_base": 5.5, "use": "human optical vision and photosynthesis"},
    {"name": "Ultraviolet light", "freq_exp": 15, "freq_base": 1.5, "use": "sterilization and vitamin D synthesis"},
    {"name": "X-rays", "freq_exp": 17, "freq_base": 3.0, "use": "medical diagnostic radiography"},
    {"name": "Gamma rays", "freq_exp": 19, "freq_base": 5.0, "use": "radiotherapy and food irradiation"},
]


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_wave_equation_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Transverse wave equation v = f * lambda and period T = 1/f."""
    hook = r.choice(PROMPT_LEAD_HOOKS_WAVES)
    qid = _make_id("waves10_equation", seed, idx)

    f = r.choice([2.5, 4.0, 5.0, 8.0, 10.0, 12.5, 20.0, 25.0])
    wavelength = r.choice([0.2, 0.4, 0.5, 0.8, 1.2, 1.5, 2.0, 2.5])
    v = f * wavelength
    period = 1.0 / f

    prompt = (
        f"{hook} a periodic transverse wave propagates through a medium with a frequency of {_fmt_sa(f)} Hz "
        f"and a wavelength of {_fmt_sa(wavelength)} m.\n\n"
        f"1. Define the term *transverse wave*.\n"
        f"2. Calculate the wave propagation speed in m·s⁻¹.\n"
        f"3. Calculate the period (T) of the wave in seconds.\n"
        f"4. Differentiate between a transverse wave and a longitudinal wave with reference to particle motion."
    )
    ans_str = (
        f"1. A wave where particles vibrate perpendicular to the direction of propagation; "
        f"2. {_fmt_sa(v)} m/s; 3. {_fmt_sa(period)} s; "
        f"4. Transverse: particles move perpendicular to wave motion; Longitudinal: particles move parallel to wave motion."
    )
    memo = (
        f"1. Definition [2]: A wave where the particles of the medium oscillate perpendicular (at right angles) to the direction of wave propagation. [2]\n"
        f"2. Wave speed [2]:\n"
        f"   $$v = f \\cdot \\lambda = ({_fmt_sa(f)})({_fmt_sa(wavelength)}) = {_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$ [1M + 1A]\n"
        f"3. Period calculation [2]:\n"
        f"   $$T = \\frac{{1}}{{f}} = \\frac{{1}}{{{_fmt_sa(f)}}} = {_fmt_sa(period)}\\text{{ s}}$$ [1M + 1A]\n"
        f"4. Motion comparison [2]:\n"
        f"   - Transverse: particles oscillate perpendicular to wave travel. [1]\n"
        f"   - Longitudinal: particles oscillate parallel to wave travel. [1]"
    )
    hints = {
        "tier_1": "Use the wave speed formula v = f * lambda and period T = 1 / f.",
        "tier_2": f"v = {_fmt_sa(f)} * {_fmt_sa(wavelength)} = {_fmt_sa(v)} m/s. Period T = 1 / {_fmt_sa(f)} s.",
        "tier_3": f"Wave speed = {_fmt_sa(v)} m·s⁻¹. Period = {_fmt_sa(period)} s.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 8,
        "hints": hints,
        "misconception_tags": ["wavelength_frequency_inversion", "transverse_longitudinal_confusion"],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of transverse wave", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Wave speed calculation formula and answer", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Period calculation formula and answer", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Comparison of particle motion", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_sound_echo_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Sound echoes and sonar reflection: 2d = v * t."""
    qid = _make_id("waves10_echo", seed, idx)
    distance = r.choice([85.0, 170.0, 340.0, 510.0, 680.0])
    v = SPEED_OF_SOUND_AIR
    t = (2.0 * distance) / v

    prompt = (
        f"A learner stands a distance of {_fmt_sa(distance)} m from a tall vertical cliff face and claps two wooden blocks together. "
        f"The speed of sound in air at the time of the experiment is {_fmt_sa(v)} m·s⁻¹.\n\n"
        f"1. Define an *echo*.\n"
        f"2. Explain why the sound travels a total distance of 2d before the echo is heard.\n"
        f"3. Calculate the time elapsed, in seconds, before the learner hears the reflected echo."
    )
    ans_str = f"1. A reflected sound wave; 2. Sound must travel from the learner to the cliff and back; 3. {_fmt_sa(t)} s"
    memo = (
        f"1. Echo definition [1]: An echo is a reflected sound wave from a barrier. [1]\n"
        f"2. Two-way path [1]: Sound wave travels to the obstacle (distance d) and reflects back to the observer (distance d), total distance = 2d. [1]\n"
        f"3. Time calculation [3]:\n"
        f"   $$v = \\frac{{2d}}{{\\Delta t}} \\implies \\Delta t = \\frac{{2d}}{{v}} = \\frac{{2 \\times {_fmt_sa(distance)}}}{{{_fmt_sa(v)}}} = \\frac{{{_fmt_sa(2 * distance)}}}{{{_fmt_sa(v)}}} = {_fmt_sa(t)}\\text{{ s}}$$ [1M + 1M + 1A]"
    )
    hints = {
        "tier_1": "Remember that an echo travels to the cliff AND bounces back: total distance is 2 * d.",
        "tier_2": f"Formula: t = (2 * d) / v = (2 * {_fmt_sa(distance)}) / {_fmt_sa(v)}.",
        "tier_3": f"Time = {_fmt_sa(t)} s.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 5,
        "hints": hints,
        "misconception_tags": ["half_distance_echo_forgotten"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of echo", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Explanation of two-way distance 2d", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Calculation of echo time delay", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_photon_energy_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Electromagnetic radiation: E = h * f and c = f * lambda."""
    qid = _make_id("waves10_em", seed, idx)
    band = r.choice(EM_SPECTRUM_BANDS)
    f_val = band["freq_base"] * (10 ** band["freq_exp"])
    energy = PLANCK_CONSTANT * f_val
    wavelength = SPEED_OF_LIGHT / f_val

    prompt = (
        f"A source of electromagnetic radiation emits {band['name']} with a frequency of "
        f"${_fmt_sa(band['freq_base'])}\\times 10^{{{band['freq_exp']}}}\\text{{ Hz}}$.\n\n"
        f"1. State Planck's constant ($h$) with its appropriate SI unit.\n"
        f"2. Calculate the energy ($E$) of a single photon of this radiation in Joules.\n"
        f"3. Calculate the wavelength ($\\lambda$) of this radiation in air ($c = 3,0\\times 10^8\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$).\n"
        f"4. State one practical application of {band['name']} in everyday technology or medicine."
    )
    ans_str = (
        f"1. 6,63 x 10^-34 J·s; "
        f"2. E = {energy:.2e} J; "
        f"3. lambda = {wavelength:.2e} m; "
        f"4. {band['use']}."
    )
    memo = (
        f"1. Planck's constant [1]: $$h = 6,63\\times 10^{{-34}}\\text{{ J}}\\cdot\\text{{s}}$$ [1]\n"
        f"2. Photon energy [3]:\n"
        f"   $$E = h \\cdot f = (6,63\\times 10^{{-34}})({_fmt_sa(band['freq_base'])}\\times 10^{{{band['freq_exp']}}}) = {energy:.2e}\\text{{ J}}$$ [1M + 1M + 1A]\n"
        f"3. Wavelength calculation [2]:\n"
        f"   $$\\lambda = \\frac{{c}}{{f}} = \\frac{{3,0\\times 10^8}}{{{_fmt_sa(band['freq_base'])}\\times 10^{{{band['freq_exp']}}}}} = {wavelength:.2e}\\text{{ m}}$$ [1M + 1A]\n"
        f"4. Application [1]: {band['use']}. [1]"
    )
    hints = {
        "tier_1": "Recall the photon energy equation E = h * f and c = f * lambda.",
        "tier_2": f"Multiply Planck's constant by the frequency: E = (6.63e-34) * ({band['freq_base']}e{band['freq_exp']}).",
        "tier_3": f"Energy = {energy:.2e} J. Wavelength = {wavelength:.2e} m.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 7,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": 7,
        "hints": hints,
        "misconception_tags": ["photon_energy_unit_conversion", "wavelength_frequency_inversion"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Planck's constant and SI unit", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Photon energy equation and calculation", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Wavelength calculation", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Practical technology application", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "concepts",
    difficulty: str = "medium",
    count: int = 1,
    grade: str = "10",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Grade 10 Physical Sciences Waves, Sound & Light."""
    r = random.Random(seed)
    questions = []

    for i in range(count):
        sub_seed = (seed + i * 37) if seed is not None else random.randint(1000, 99999)

        if mode == "scaffold" or subskill == "transverse_wave_diagram":
            q = build_transverse_wave_question(seed=sub_seed, grade=10, mode=mode)
        elif mode == "elementary_wave_speed":
            q = _generate_wave_equation_question(r, sub_seed, i, mode)
        elif mode == "elementary_sound_echo":
            q = _generate_sound_echo_question(r, sub_seed, i, mode)
        elif mode == "elementary_photon_energy":
            q = _generate_photon_energy_question(r, sub_seed, i, mode)
        else:
            # Compound progression: diagram visual scaffold followed by quantitative derivations
            picker = i % 4
            if picker == 0:
                q = build_transverse_wave_question(seed=sub_seed, grade=10, mode=mode)
            elif picker == 1:
                q = _generate_wave_equation_question(r, sub_seed, i, mode)
            elif picker == 2:
                q = _generate_sound_echo_question(r, sub_seed, i, mode)
            else:
                q = _generate_photon_energy_question(r, sub_seed, i, mode)

        questions.append(q)

    return questions
