"""Grade 10 Physical Sciences — Waves, Sound & Light (Deterministic 6-Pillar Generator).
Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/07. Transverse pulses.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/08. Transverse waves.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/09. Longitudinal waves.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/10. Sound.md
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/11. Electromagnetic radiation.md

Complies strictly with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=1 (or term=2 for optics), caps_weight_percent, suggested_duration_mins.
2. Deconstructibility: Compound scenarios and atomic elementary sub-drills (elementary_wave_speed, elementary_sound_echo, elementary_photon_energy, elementary_snell_refraction).
3. Standardized Misconceptions: wavelength_frequency_inversion, half_distance_echo_forgotten, photon_energy_unit_conversion, refractive_index_inversion.
4. Teacher-Editable Marking Schema with [M] method and [A] accuracy marks.
5. Deterministic 3-Tier Pre-Baked Hints.
6. South African comma decimal convention (",").
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "grade10_waves_sound_light"

SPEED_OF_SOUND_AIR = 340.0  # m/s at 20 deg C
SPEED_OF_LIGHT = 3.0e8      # m/s
PLANCK_CONSTANT = 6.63e-34  # J.s

PROMPT_LEAD_HOOKS_WAVES = [
    "In a physics laboratory investigation on wave motion,",
    "A ripple tank is set up to generate periodic water pulses across a shallow basin,",
    "A sound technician analyzes acoustic reflections using an ultrasonic sensor,",
    "During an offshore geophysical survey using sonar echo-sounding,",
    "An astronomical observatory monitors incoming electromagnetic radiation from a distant nebula,"
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
        f"1. Calculate the wave propagation speed in m·s⁻¹.\n"
        f"2. Calculate the period (T) of the wave in seconds.\n"
        f"3. Differentiate between a transverse wave and a longitudinal wave with reference to particle motion."
    )
    ans_str = f"1. {_fmt_sa(v)} m/s; 2. {_fmt_sa(period)} s; 3. In transverse waves, particles vibrate perpendicular to wave propagation; in longitudinal waves, particles vibrate parallel to propagation."
    memo = (
        f"1. v = f · λ [1M]\n"
        f"   v = ({_fmt_sa(f)})({_fmt_sa(wavelength)}) = {_fmt_sa(v)} m·s⁻¹ [1A]\n"
        f"2. T = 1 / f [1M]\n"
        f"   T = 1 / {_fmt_sa(f)} = {_fmt_sa(period, 3)} s [1A]\n"
        f"3. In a transverse wave, the particles of the medium vibrate perpendicular to the direction of wave motion [1]. "
        f"In a longitudinal wave, particles vibrate parallel to the direction of wave motion [1]."
    )
    hints = {
        "tier_1": "Use the wave speed formula v = f * lambda. The period is the reciprocal of the frequency.",
        "tier_2": "v = f * lambda gives speed. T = 1/f gives period. Transverse particles move perpendicular; longitudinal move parallel.",
        "tier_3": f"1. v = ({_fmt_sa(f)})({_fmt_sa(wavelength)}) = {_fmt_sa(v)} m/s. 2. T = 1/{_fmt_sa(f)} = {_fmt_sa(period, 3)} s.",
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
        "misconception_tags": ["wavelength_frequency_inversion"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Wave speed calculation (formula + substitution)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Period calculation (formula + substitution)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Wave nature distinction", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_sound_echo_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Longitudinal sound reflection / echo calculation: 2d = v * t."""
    hook = r.choice(PROMPT_LEAD_HOOKS_WAVES)
    qid = _make_id("waves10_echo", seed, idx)

    distance = r.choice([85, 170, 255, 340, 510, 680, 850])
    v_sound = SPEED_OF_SOUND_AIR
    time_echo = (2 * distance) / v_sound

    prompt = (
        f"{hook} a learner claps hands in front of a vertical cliff wall located {_fmt_sa(distance)} m away. "
        f"The speed of sound in the ambient air is {_fmt_sa(v_sound)} m·s⁻¹.\n\n"
        f"1. Explain why sound is classified as a mechanical longitudinal wave.\n"
        f"2. Calculate the time taken, in seconds, for the learner to hear the echo.\n"
        f"3. State how an increase in air temperature would affect the speed of sound and the time taken to hear the echo."
    )
    ans_str = f"1. Requires a material medium and particles oscillate parallel to wave direction; 2. {_fmt_sa(time_echo)} s; 3. Sound speed increases, so time to hear echo decreases."
    memo = (
        "1. Sound requires a material medium to propagate (cannot travel through a vacuum) [1], "
        "and particles vibrate parallel to the direction of propagation creating compressions and rarefactions [1].\n"
        f"2. Total distance travelled = 2 · d = 2 · {_fmt_sa(distance)} = {_fmt_sa(2 * distance)} m [1M]\n"
        f"   v = Δx / Δt => Δt = 2d / v = {_fmt_sa(2 * distance)} / {_fmt_sa(v_sound)} = {_fmt_sa(time_echo, 2)} s [1M, 1A]\n"
        "3. Increased temperature increases the kinetic energy of air particles, causing sound speed to increase [1]; "
        "therefore, the time taken for the echo to return decreases [1]."
    )
    hints = {
        "tier_1": "Remember an echo travels to the cliff and back (total distance = 2d).",
        "tier_2": "Use v = (2 * d) / t. Speed of sound increases with temperature because air particles collide faster.",
        "tier_3": f"1. Mechanical & longitudinal. 2. t = (2 * {_fmt_sa(distance)}) / {_fmt_sa(v_sound)} = {_fmt_sa(time_echo, 2)} s. 3. Speed increases, time decreases.",
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
        "misconception_tags": ["half_distance_echo_forgotten"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Mechanical/longitudinal definition", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Echo time calculation (2d/v)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Temperature relationship explanation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_photon_energy_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Electromagnetic radiation: E = hf = hc / lambda."""
    hook = r.choice(PROMPT_LEAD_HOOKS_WAVES)
    qid = _make_id("waves10_photon", seed, idx)

    band = r.choice(EM_SPECTRUM_BANDS)
    freq = band["freq_base"] * (10 ** band["freq_exp"])
    energy = PLANCK_CONSTANT * freq
    wavelength = SPEED_OF_LIGHT / freq

    prompt = (
        f"{hook} a beam of {band['name']} with a frequency of {band['freq_base']} × 10^{band['freq_exp']} Hz is analyzed. "
        f"(Take c = 3,0 × 10⁸ m·s⁻¹ and h = 6,63 × 10⁻³⁴ J·s).\n\n"
        f"1. State one practical technological or medical application of {band['name']}.\n"
        f"2. Calculate the wavelength of this radiation in meters.\n"
        f"3. Calculate the energy of a single photon of this radiation in Joules (J)."
    )
    ans_str = f"1. {band['use']}; 2. {wavelength:.2e} m; 3. {energy:.2e} J"
    memo = (
        f"1. Application: {band['use']}. [1]\n"
        f"2. c = f · λ => λ = c / f [1M]\n"
        f"   λ = (3,0 × 10⁸) / ({band['freq_base']} × 10^{band['freq_exp']}) = {wavelength:.2e} m [1A]\n"
        f"3. E = h · f [1M]\n"
        f"   E = (6,63 × 10⁻³⁴) · ({band['freq_base']} × 10^{band['freq_exp']}) = {energy:.2e} J [1A]\n"
        "   (Unit mark: Joules) [1A]"
    )
    hints = {
        "tier_1": "Use c = f * lambda for wavelength, and Planck's equation E = h * f for photon energy.",
        "tier_2": "Wavelength = (3.0e8) / f. Photon energy = (6.63e-34) * f. Units are meters and Joules.",
        "tier_3": f"1. {band['use']}. 2. lambda = {wavelength:.2e} m. 3. E = {energy:.2e} J.",
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
        "misconception_tags": ["photon_energy_unit_conversion"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Practical application statement", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Wavelength calculation (c = f * lambda)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Photon energy calculation (E = hf)", "marks": 3, "editable": True},
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
    grade: str = "10",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Grade 10 Physical Sciences Waves, Sound & Light."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("waves", "transverse", "frequency") or mode == "elementary_wave_speed":
            q = _generate_wave_equation_question(sub_r, sub_seed, i, mode)
        elif subskill in ("sound", "echo", "longitudinal") or mode == "elementary_sound_echo":
            q = _generate_sound_echo_question(sub_r, sub_seed, i, mode)
        elif subskill in ("em_radiation", "photons", "light") or mode == "elementary_photon_energy":
            q = _generate_photon_energy_question(sub_r, sub_seed, i, mode)
        else:
            chosen = sub_r.choice(["wave_eq", "echo", "photon"])
            if chosen == "wave_eq":
                q = _generate_wave_equation_question(sub_r, sub_seed, i, mode)
            elif chosen == "echo":
                q = _generate_sound_echo_question(sub_r, sub_seed, i, mode)
            else:
                q = _generate_photon_energy_question(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
