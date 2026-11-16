"""
optical_phenomena_photoelectric_archetypes_01_25.py
---------------------------------------------------
Grade 12 Physical Sciences — Optical Phenomena & Properties of Matter (Subskills 01–25).
Covering Photoelectric Effect Foundations, Energy Quantisation & Photoelectron Kinematics:
  01. 01_photoelectric_effect_definition_and_significance
  02. 02_failure_of_classical_wave_theory
  03. 03_photon_energy_from_frequency
  04. 04_photon_energy_from_wavelength
  05. 05_electron_volt_and_joule_energy_conversions
  06. 06_work_function_definition
  07. 07_threshold_frequency_calculation
  08. 08_threshold_wavelength_calculation
  09. 09_metal_identification_from_threshold_frequency
  10. 10_emission_condition_frequency_vs_threshold
  11. 11_photoelectric_equation_maximum_kinetic_energy
  12. 12_photoelectric_equation_kinetic_energy_in_ev
  13. 13_maximum_speed_of_photoelectrons
  14. 14_work_function_from_kinetic_energy_and_frequency
  15. 15_incident_frequency_from_work_function_and_kinetic_energy
  16. 16_effect_of_doubling_frequency_on_kinetic_energy
  17. 17_effect_of_light_intensity_on_kinetic_energy_and_speed
  18. 18_effect_of_light_intensity_on_photoelectron_emission_rate
  19. 19_instantaneous_emission_no_time_lag
  20. 20_wavelength_decrease_effect_on_photoelectron_speed
  21. 21_stopping_potential_definition_and_principle
  22. 22_stopping_potential_calculation_from_kinetic_energy
  23. 23_stopping_potential_from_incident_frequency_and_work_function
  24. 24_photocell_retarding_circuit_diagram
  25. 25_gold_leaf_electroscope_photoelectric_investigation

All generators are 100% deterministic (random.Random(seed)), zero-LLM,
adhering strictly to South African comma decimal convention and 6-pillar contract.
"""

from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional

TERM = 3
CAPS_WEIGHT = 15
SUGGESTED_DURATION = 5
TOPIC_ID = "grade12_optical_phenomena"
LEARNING_OBJECTIVE = "PS12.OPP"

# Standard Physics Constants
H = 6.63e-34    # J·s (Planck's constant)
C = 3.0e8       # m·s⁻¹ (Speed of light)
ME = 9.11e-31   # kg (Mass of electron)
QE = 1.6e-19    # C (Elementary charge / 1 eV in Joules)

# Reference Metal Cathodes
METALS_REF = [
    {"name": "Caesium (Cs)", "w0_j": 3.42e-19, "w0_ev": 2.14, "f0": 5.16e14},
    {"name": "Potassium (K)", "w0_j": 3.68e-19, "w0_ev": 2.30, "f0": 5.55e14},
    {"name": "Sodium (Na)", "w0_j": 3.78e-19, "w0_ev": 2.36, "f0": 5.70e14},
    {"name": "Zinc (Zn)", "w0_j": 6.88e-19, "w0_ev": 4.30, "f0": 1.04e15},
    {"name": "Copper (Cu)", "w0_j": 7.52e-19, "w0_ev": 4.70, "f0": 1.13e15},
    {"name": "Platinum (Pt)", "w0_j": 1.01e-18, "w0_ev": 6.35, "f0": 1.52e15},
]


def _fmt_sa(val: float, decimals: int = 2) -> str:
    """Format float with South African comma decimal notation."""
    if abs(val - round(val)) < 1e-9:
        return str(int(round(val)))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _fmt_sci(val: float, decimals: int = 2) -> str:
    """Format scientific notation with South African comma."""
    s = f"{val:.{decimals}e}"
    base, exp = s.split("e")
    base_sa = _fmt_sa(float(base), decimals)
    exp_int = int(exp)
    return f"{base_sa} \\times 10^{{{exp_int}}}"


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
    """Universal 6-pillar question contract."""
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
# Vector SVG Helpers
# =========================================================================== #

def _svg_photocell_circuit(v_applied: float, f_inc_14: float) -> str:
    """Generate responsive photocell retarding circuit vector diagram."""
    w, h = 480, 200
    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .wire { stroke: #334155; stroke-width: 2; fill: none; }',
        '    .glass { stroke: #0284c7; stroke-width: 1.5; stroke-dasharray: 4,3; fill: #f0f9ff; rx: 40; }',
        '    .photon { stroke: #eab308; stroke-width: 1.8; stroke-dasharray: 2,2; }',
        '    .electron { fill: #2563eb; stroke: none; }',
        '  </style>',
        # Photocell glass tube
        f'  <rect x="70" y="30" width="160" height="90" class="glass" />',
        # Cathode plate (curved on left)
        '  <path d="M 95 45 Q 110 75 95 105" stroke="#475569" stroke-width="5" fill="none" />',
        f'  <text x="80" y="122" class="lbl">Cathode</text>',
        # Anode collector rod (vertical on right)
        '  <line x1="200" y1="50" x2="200" y2="100" stroke="#dc2626" stroke-width="3" />',
        f'  <text x="185" y="122" class="lbl">Anode</text>',
        # Incoming photons (wavy rays)
        '  <line x1="30" y1="45" x2="90" y2="65" class="photon" />',
        '  <line x1="30" y1="75" x2="90" y2="75" class="photon" />',
        '  <line x1="30" y1="105" x2="90" y2="85" class="photon" />',
        f'  <text x="25" y="30" class="lbl" fill="#ca8a04">Light (f = {_fmt_sa(f_inc_14)} × 10¹⁴ Hz)</text>',
        # Ejected photoelectrons moving to anode
        '  <circle cx="125" cy="70" r="3" class="electron" />',
        '  <circle cx="150" cy="80" r="3" class="electron" />',
        '  <circle cx="170" cy="65" r="3" class="electron" />',
        # External Circuit wires
        '  <path d="M 95 75 L 50 75 L 50 165 L 200 165 L 200 100" class="wire" />',
        # Microammeter circle
        '  <circle cx="120" cy="165" r="14" fill="#ffffff" stroke="#334155" stroke-width="2" />',
        '  <text x="114" y="169" class="lbl">μA</text>',
        # Variable DC Power Supply
        '  <circle cx="320" cy="100" r="16" fill="#ffffff" stroke="#334155" stroke-width="2" />',
        f'  <text x="312" y="104" class="lbl">V</text>',
        f'  <text x="240" y="180" class="lbl" fill="#0369a1">Retarding Potential V = {_fmt_sa(v_applied)} V</text>',
        '</svg>',
    ]
    return "\n".join(svg)


def _svg_electroscope(leaf_angle_deg: int, has_uv: bool = True) -> str:
    """Generate responsive gold-leaf electroscope vector diagram."""
    w, h = 480, 200
    ox, oy = 240, 40
    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .case { stroke: #475569; stroke-width: 2; fill: #f1f5f9; rx: 6; }',
        '    .stem { stroke: #ca8a04; stroke-width: 3.5; fill: none; }',
        '    .zinc { stroke: #64748b; stroke-width: 1.5; fill: #94a3b8; }',
        '  </style>',
        # Insulated metal case
        '  <rect x="180" y="70" width="120" height="110" class="case" />',
        # Polished Zinc Plate on top
        f'  <ellipse cx="{ox}" cy="{oy}" rx="45" ry="12" class="zinc" />',
        f'  <text x="{ox - 40}" y="{oy - 16}" class="lbl">Zinc Plate (Zn)</text>',
        # Brass central stem
        f'  <line x1="{ox}" y1="{oy}" x2="{ox}" y2="155" class="stem" />',
    ]
    # Gold leaf deflected at angle
    rad = math.radians(leaf_angle_deg)
    leaf_x = ox + 40 * math.sin(rad)
    leaf_y = 120 + 40 * math.cos(rad)
    svg.append(f'  <line x1="{ox}" y1="120" x2="{leaf_x:.1f}" y2="{leaf_y:.1f}" stroke="#eab308" stroke-width="2" />')
    if leaf_angle_deg > 10:
        svg.append(f'  <text x="310" y="140" class="lbl" fill="#b45309">Diverged Leaf ({leaf_angle_deg}°)</text>')
    else:
        svg.append('  <text x="310" y="140" class="lbl" fill="#15803d">Collapsed Leaf (Discharged)</text>')

    if has_uv:
        svg.append('  <line x1="80" y1="15" x2="200" y2="35" stroke="#a855f7" stroke-width="2" stroke-dasharray="3,2" />')
        svg.append('  <text x="60" y="32" class="lbl" fill="#9333ea">UV Radiation</text>')
    svg.append('</svg>')
    return "\n".join(svg)


# =========================================================================== #
# Archetypes 01 to 25
# =========================================================================== #

def _build_01(rng: random.Random) -> Dict[str, Any]:
    sub = "01_photoelectric_effect_definition_and_significance"
    metal = rng.choice(["zinc", "sodium", "caesium", "copper"])
    prompt = (
        f"During a physics investigation into modern quantum mechanics, light is shone onto a clean plate of {metal}.\n\n"
        "1. Define the term **photoelectric effect**.\n"
        "2. State the major significance of the photoelectric effect in the development of modern quantum theory of light."
    )
    ans = "Photoelectric effect: The process whereby electrons are ejected from a metal surface when light of suitable frequency is shone on the metal; Significance: It provides conclusive experimental proof for the particle (quantum/photon) nature of light."
    steps = [
        {"rule": "State definition of photoelectric effect", "op": "\\text{{Ejection of electrons by incident light}}", "to": "\\text{{Process whereby electrons are emitted from a metal surface when EM radiation of suitable frequency shines on it}}"},
        {"rule": "State scientific significance of photoelectric effect", "op": "\\text{{Wave-particle duality}}", "to": "\\text{{Demonstrates the particulate (photon) nature of light, refuting purely classical wave theory}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The photoelectric effect refers to the emission of electrons from a metal surface exposed to light of sufficiently high frequency.",
        t2="Classical wave theory failed to explain why low-frequency light (no matter how bright) cannot emit electrons. The photoelectric effect confirmed Einstein's photon hypothesis.",
        t3="Emission of electrons from metal surface under suitable light; proves particulate nature of light.",
        misconceptions=["defining_photoelectric_effect_without_mentioning_frequency_requirement", "confusing_photoelectric_effect_with_thermionic_emission"],
        marks=4,
    )


def _build_02(rng: random.Random) -> Dict[str, Any]:
    sub = "02_failure_of_classical_wave_theory"
    prompt = (
        "Classical electromagnetic wave theory failed to explain key experimental observations of the photoelectric effect.\n\n"
        "1. State what classical wave theory predicted would happen when very bright (high intensity) red light shines on a zinc plate.\n"
        "2. State the actual experimental observation when red light shines on a zinc plate.\n"
        "3. Explain how Einstein's photon model successfully explains this observation."
    )
    ans = "Classical prediction: High intensity would deliver enough energy over time to eject electrons; Observation: No electrons are ejected regardless of intensity or time; Explanation: Energy is delivered in discrete quanta (photons) where E = hf; if f < f0, individual photons lack sufficient energy to overcome the work function W0."
    steps = [
        {"rule": "State classical wave prediction regarding intensity and emission", "op": "\\text{{Classical wave theory: energy accumulates with intensity}}", "to": "\\text{{Electrons should be ejected if red light intensity is high enough}}"},
        {"rule": "State experimental outcome", "op": "\\text{{Experimental reality: threshold cutoff}}", "to": "\\text{{Zero electron emission occurs regardless of brightness or exposure time}}"},
        {"rule": "Apply Einstein's photon model to explain threshold condition", "op": "E = hf < W_0", "to": "\\text{{Each photon interacts one-to-one with an electron; individual red photons have insufficient energy}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Classical wave theory assumed light energy is continuous and determined solely by intensity (brightness).",
        t2="Einstein showed light consists of packets called photons, where energy E = hf. One photon interacts with one electron.",
        t3="Red light frequency is below threshold frequency f0, so individual photons lack energy to overcome work function W0.",
        misconceptions=["believing_bright_light_can_eventually_build_up_enough_energy_to_emit_electrons"],
        marks=5,
    )


def _build_03(rng: random.Random) -> Dict[str, Any]:
    sub = "03_photon_energy_from_frequency"
    f_exp = rng.choice([5.2, 5.8, 6.4, 7.5, 8.2, 9.5])
    f_hz = f_exp * 1e14
    e_photon = H * f_hz

    prompt = (
        f"A monochromatic light source emits radiation with a frequency of ${_fmt_sci(f_hz)}\\text{{ Hz}}$.\n\n"
        "Calculate the energy of a single photon of this radiation in Joules."
    )
    ans = f"$E = {_fmt_sci(e_photon)}\\text{{ J}}$"
    steps = [
        {"rule": "State Planck's energy equation", "op": "E = h f", "to": f"(6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_hz)})"},
        {"rule": "Calculate single photon energy", "op": f"E = (6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_hz)})", "to": f"{_fmt_sci(e_photon)}\\text{{ J}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Planck's equation relates photon energy directly to frequency: E = h * f.",
        t2="Use h = 6,63 x 10^-34 J·s from the standard data sheet.",
        t3=f"E = (6,63 x 10^-34) * ({_fmt_sci(f_hz)}) = {_fmt_sci(e_photon)} J.",
        misconceptions=["confusing_planck_constant_with_gravitational_constant"],
        marks=3,
    )


def _build_04(rng: random.Random) -> Dict[str, Any]:
    sub = "04_photon_energy_from_wavelength"
    wlen_nm = rng.choice([250, 320, 400, 450, 520, 600])
    wlen_m = wlen_nm * 1e-9
    e_photon = (H * C) / wlen_m

    prompt = (
        f"A laser emits photons of wavelength ${_fmt_sa(wlen_nm)}\\text{{ nm}}$ in a vacuum.\n\n"
        "1. Convert this wavelength to metres.\n"
        "2. Calculate the energy of a single photon emitted by this laser in Joules."
    )
    ans = f"$\\lambda = {_fmt_sci(wlen_m)}\\text{{ m}}$, $E = {_fmt_sci(e_photon)}\\text{{ J}}$"
    steps = [
        {"rule": "Convert nanometres to metres", "op": f"\\lambda = {_fmt_sa(wlen_nm)} \\times 10^{{-9}}\\text{{ m}}", "to": f"{_fmt_sci(wlen_m)}\\text{{ m}}"},
        {"rule": "Apply photon energy formula in terms of wavelength", "op": f"E = \\frac{{hc}}{{\\lambda}} = \\frac{{(6{{,}}63 \\times 10^{{-34}})(3{{,}}0 \\times 10^8)}}{{{_fmt_sci(wlen_m)}}}", "to": f"{_fmt_sci(e_photon)}\\text{{ J}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="1 nm = 1 x 10^-9 m. Since c = f * λ, E = h * f = h * c / λ.",
        t2="Use c = 3,0 x 10^8 m/s and h = 6,63 x 10^-34 J·s.",
        t3=f"E = (6,63 x 10^-34 * 3,0 x 10^8) / ({_fmt_sci(wlen_m)}) = {_fmt_sci(e_photon)} J.",
        misconceptions=["forgetting_to_convert_nanometres_to_metres_leading_to_10_to_the_9_error"],
        marks=4,
    )


def _build_05(rng: random.Random) -> Dict[str, Any]:
    sub = "05_electron_volt_and_joule_energy_conversions"
    ev_val = rng.choice([2.14, 2.45, 3.20, 4.30, 5.12])
    j_val = ev_val * QE

    prompt = (
        f"In atomic physics, energies are often expressed in electron-volts ($\\text{{eV}}$).\n\n"
        f"1. Convert an energy of ${_fmt_sa(ev_val)}\\text{{ eV}}$ into Joules ($\\text{{J}}$).\n"
        f"2. A photon has an energy of ${_fmt_sci(j_val)}\\text{{ J}}$. Convert this energy into electron-volts."
    )
    ans = f"${_fmt_sa(ev_val)}\\text{{ eV}} = {_fmt_sci(j_val)}\\text{{ J}}$, ${_fmt_sci(j_val)}\\text{{ J}} = {_fmt_sa(ev_val)}\\text{{ eV}}$"
    steps = [
        {"rule": "Convert eV to Joules by multiplying by elementary charge e", "op": f"E = {_fmt_sa(ev_val)} \\times (1{{,}}6 \\times 10^{{-19}})", "to": f"{_fmt_sci(j_val)}\\text{{ J}}"},
        {"rule": "Convert Joules to eV by dividing by elementary charge e", "op": f"E_{{\\text{{eV}}}} = \\frac{{{_fmt_sci(j_val)}}}{{1{{,}}6 \\times 10^{{-19}}}}", "to": f"{_fmt_sa(ev_val)}\\text{{ eV}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="1 eV is the kinetic energy gained by an electron accelerating through 1 Volt: 1 eV = 1,6 x 10^-19 J.",
        t2="To convert eV -> J: multiply by 1,6 x 10^-19. To convert J -> eV: divide by 1,6 x 10^-19.",
        t3=f"{_fmt_sa(ev_val)} eV = {_fmt_sci(j_val)} J.",
        misconceptions=["multiplying_instead_of_dividing_when_converting_from_joules_to_ev"],
        marks=4,
    )


def _build_06(rng: random.Random) -> Dict[str, Any]:
    sub = "06_work_function_definition"
    metal = rng.choice(["sodium", "potassium", "platinum", "zinc"])
    prompt = (
        f"A laboratory experiment examines the photoelectric properties of {metal}.\n\n"
        "1. Define the term **work function** ($W_0$) of a metal.\n"
        "2. State whether the work function depends on the intensity of the incident light, the frequency of the incident light, or the type of metal."
    )
    ans = "Work function: The minimum amount of energy needed to emit an electron from the surface of a metal; It depends ONLY on the type of metal."
    steps = [
        {"rule": "State definition of work function", "op": "\\text{{Definition}}", "to": "\\text{{Minimum energy required to eject an electron from the surface of a metal}}"},
        {"rule": "State dependency of work function", "op": "\\text{{Material property}}", "to": "\\text{{Depends only on the type of metal (cathode material), independent of light intensity or frequency}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Work function W0 is the minimum binding energy holding an electron in a metal surface.",
        t2="Work function is a characteristic physical constant of the specific metal (like density or melting point).",
        t3="Minimum energy needed to eject an electron; depends solely on the metal.",
        misconceptions=["thinking_the_work_function_changes_when_the_incident_light_is_made_brighter"],
        marks=3,
    )


def _build_07(rng: random.Random) -> Dict[str, Any]:
    sub = "07_threshold_frequency_calculation"
    metal = rng.choice(METALS_REF)
    w0 = metal["w0_j"]
    f0 = w0 / H

    prompt = (
        f"The work function of a {metal['name']} cathode is ${_fmt_sci(w0)}\\text{{ J}}$.\n\n"
        "1. Define the term **threshold frequency** ($f_0$).\n"
        f"2. Calculate the threshold frequency of {metal['name']}."
    )
    ans = f"Threshold frequency: The minimum frequency of light needed to emit electrons from a certain metal surface; $f_0 = {_fmt_sci(f0)}\\text{{ Hz}}$"
    steps = [
        {"rule": "State definition of threshold frequency", "op": "\\text{{Definition}}", "to": "\\text{{Minimum frequency of incident radiation needed to eject electrons from a metal surface}}"},
        {"rule": "Apply W0 = h f0 to calculate threshold frequency", "op": f"f_0 = \\frac{{W_0}}{{h}} = \\frac{{{_fmt_sci(w0)}}}{{6{{,}}63 \\times 10^{{-34}}}}", "to": f"{_fmt_sci(f0)}\\text{{ Hz}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Threshold frequency f0 is related to work function W0 by: W0 = h * f0.",
        t2=f"f0 = W0 / h = ({_fmt_sci(w0)}) / (6,63 x 10^-34).",
        t3=f"f0 = {_fmt_sci(f0)} Hz.",
        misconceptions=["confusing_threshold_frequency_with_maximum_frequency"],
        marks=4,
    )


def _build_08(rng: random.Random) -> Dict[str, Any]:
    sub = "08_threshold_wavelength_calculation"
    metal = rng.choice(METALS_REF)
    w0 = metal["w0_j"]
    f0 = w0 / H
    lambda0_m = C / f0
    lambda0_nm = lambda0_m * 1e9

    prompt = (
        f"The work function of a {metal['name']} plate is ${_fmt_sci(w0)}\\text{{ J}}$.\n\n"
        "1. Define the term **threshold (cut-off) wavelength** ($\\lambda_0$).\n"
        f"2. Calculate the threshold wavelength of {metal['name']} in nanometres ($\\text{{nm}}$)."
    )
    ans = f"Threshold wavelength: The maximum wavelength of radiation that will emit photoelectrons from a metal surface; $\\lambda_0 = {_fmt_sa(lambda0_nm)}\\text{{ nm}}$"
    steps = [
        {"rule": "State definition of threshold wavelength", "op": "\\text{{Definition}}", "to": "\\text{{Maximum wavelength of incident light capable of ejecting photoelectrons}}"},
        {"rule": "Apply lambda0 = hc / W0", "op": f"\\lambda_0 = \\frac{{hc}}{{W_0}} = \\frac{{(6{{,}}63 \\times 10^{{-34}})(3{{,}}0 \\times 10^8)}}{{{_fmt_sci(w0)}}}", "to": f"{_fmt_sci(lambda0_m)}\\text{{ m}} = {_fmt_sa(lambda0_nm)}\\text{{ nm}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Because c = f * λ, the MINIMUM threshold frequency f0 corresponds to the MAXIMUM threshold wavelength λ0 = c / f0 = hc / W0.",
        t2="Radiation must have λ <= λ0 for photoelectron emission to take place.",
        t3=f"λ0 = {_fmt_sa(lambda0_nm)} nm.",
        misconceptions=["thinking_threshold_wavelength_is_the_minimum_wavelength_rather_than_maximum"],
        marks=4,
    )


def _build_09(rng: random.Random) -> Dict[str, Any]:
    sub = "09_metal_identification_from_threshold_frequency"
    chosen = rng.choice(METALS_REF)
    f0 = chosen["f0"]
    w0 = chosen["w0_j"]

    prompt = (
        "In a laboratory investigation, light of variable frequency is incident on an unknown metal surface. "
        f"Photoelectrons are emitted only when the incident frequency is greater than or equal to ${_fmt_sci(f0)}\\text{{ Hz}}$.\n\n"
        "Reference data for work functions:\n"
        "- Caesium: $3{{,}}42 \\times 10^{-19}\\text{ J}$\n"
        "- Sodium: $3{{,}}78 \\times 10^{-19}\\text{ J}$\n"
        "- Zinc: $6{{,}}88 \\times 10^{-19}\\text{ J}$\n"
        "- Copper: $7{{,}}52 \\times 10^{-19}\\text{ J}$\n"
        "- Platinum: $1{{,}}01 \\times 10^{-18}\\text{ J}$\n\n"
        "1. Calculate the work function $W_0$ of this unknown metal in Joules.\n"
        "2. Identify the metal from the reference table."
    )
    ans = f"$W_0 = {_fmt_sci(w0)}\\text{{ J}}$, Metal is {chosen['name']}"
    steps = [
        {"rule": "Calculate work function from threshold frequency", "op": f"W_0 = h f_0 = (6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f0)})", "to": f"{_fmt_sci(w0)}\\text{{ J}}"},
        {"rule": "Match calculated work function to metal in table", "op": f"W_0 \\approx {_fmt_sci(w0)}\\text{{ J}}", "to": f"\\text{{{chosen['name']}}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Use W0 = h * f0 to determine the work function and match it with the table.",
        t2=f"W0 = (6,63 x 10^-34) * ({_fmt_sci(f0)}) = {_fmt_sci(w0)} J.",
        t3=f"The metal is {chosen['name']}.",
        misconceptions=["selecting_wrong_metal_due_to_power_of_ten_misread"],
        marks=4,
    )


def _build_10(rng: random.Random) -> Dict[str, Any]:
    sub = "10_emission_condition_frequency_vs_threshold"
    metal = rng.choice(METALS_REF)
    f0 = metal["f0"]
    # 50% chance above threshold, 50% below
    is_above = rng.choice([True, False])
    factor = rng.uniform(1.15, 1.35) if is_above else rng.uniform(0.70, 0.90)
    f_test = f0 * factor
    e_photon = H * f_test

    prompt = (
        f"Radiation of frequency ${_fmt_sci(f_test)}\\text{{ Hz}}$ is shone on a clean plate of {metal['name']}. "
        f"The threshold frequency of {metal['name']} is ${_fmt_sci(f0)}\\text{{ Hz}}$.\n\n"
        "1. State with a clear scientific reason whether photoelectrons will be ejected from the surface.\n"
        "2. Calculate the energy of a single photon of the incident radiation."
    )
    eject_str = "YES, photoelectrons will be emitted" if is_above else "NO, photoelectrons will NOT be emitted"
    reason_str = f"Incident frequency ({_fmt_sci(f_test)} Hz) is greater than threshold frequency ({_fmt_sci(f0)} Hz)" if is_above else f"Incident frequency ({_fmt_sci(f_test)} Hz) is less than threshold frequency ({_fmt_sci(f0)} Hz)"
    ans = f"{eject_str} ({reason_str}); $E = {_fmt_sci(e_photon)}\\text{{ J}}$"
    steps = [
        {"rule": "Compare incident frequency with threshold frequency", "op": f"f = {_fmt_sci(f_test)}\\text{{ Hz}} \\text{{ vs }} f_0 = {_fmt_sci(f0)}\\text{{ Hz}}", "to": eject_str},
        {"rule": "Calculate photon energy", "op": f"E = h f = (6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_test)})", "to": f"{_fmt_sci(e_photon)}\\text{{ J}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Photoelectrons are ejected if and only if incident frequency f >= f0 (or photon energy E >= W0).",
        t2=f"Compare f = {_fmt_sci(f_test)} Hz with f0 = {_fmt_sci(f0)} Hz.",
        t3=f"{eject_str}.",
        misconceptions=["assuming_emission_depends_on_radiation_intensity_rather_than_frequency"],
        marks=4,
    )


def _build_11(rng: random.Random) -> Dict[str, Any]:
    sub = "11_photoelectric_equation_maximum_kinetic_energy"
    metal = rng.choice(METALS_REF)
    w0 = metal["w0_j"]
    f0 = metal["f0"]
    mult = rng.choice([1.3, 1.4, 1.5, 1.6, 1.8])
    f_inc = f0 * mult
    e_photon = H * f_inc
    k_max = e_photon - w0

    prompt = (
        f"Ultraviolet radiation of frequency ${_fmt_sci(f_inc)}\\text{{ Hz}}$ is incident on a {metal['name']} cathode "
        f"with a work function of ${_fmt_sci(w0)}\\text{{ J}}$.\n\n"
        "1. Write down Einstein's photoelectric equation in symbols.\n"
        "2. Calculate the maximum kinetic energy ($K_{{\\max}}$) of the emitted photoelectrons in Joules."
    )
    ans = f"$E = W_0 + K_{{\\max}}$ ($hf = W_0 + K_{{\\max}}$); $K_{{\\max}} = {_fmt_sci(k_max)}\\text{{ J}}$"
    steps = [
        {"rule": "State Einstein's photoelectric equation", "op": "E = W_0 + K_{{\\max}} \\implies hf = W_0 + K_{{\\max}}", "to": "\\text{Conservation of energy for photon-electron interaction}"},
        {"rule": "Substitute known values and solve for K_max", "op": f"K_{{\\max}} = hf - W_0 = (6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_inc)}) - {_fmt_sci(w0)}", "to": f"{_fmt_sci(k_max)}\\text{{ J}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Einstein's photoelectric equation expresses conservation of energy: Photon Energy (E) = Work Function (W0) + Max Kinetic Energy (K_max).",
        t2=f"K_max = h*f - W0. Photon energy = {_fmt_sci(e_photon)} J, W0 = {_fmt_sci(w0)} J.",
        t3=f"K_max = {_fmt_sci(k_max)} J.",
        misconceptions=["adding_work_function_to_photon_energy_instead_of_subtracting"],
        marks=4,
    )


def _build_12(rng: random.Random) -> Dict[str, Any]:
    sub = "12_photoelectric_equation_kinetic_energy_in_ev"
    metal = rng.choice(METALS_REF)
    w0_ev = metal["w0_ev"]
    w0_j = metal["w0_j"]
    f0 = metal["f0"]
    mult = rng.choice([1.35, 1.50, 1.75, 2.00])
    f_inc = f0 * mult
    e_photon_j = H * f_inc
    e_photon_ev = e_photon_j / QE
    k_max_j = e_photon_j - w0_j
    k_max_ev = round(k_max_j / QE, 2)

    prompt = (
        f"Monochromatic light of frequency ${_fmt_sci(f_inc)}\\text{{ Hz}}$ shines on a {metal['name']} surface. "
        f"The work function of the metal is ${_fmt_sa(w0_ev)}\\text{{ eV}}$.\n\n"
        "1. Calculate the energy of an incident photon in electron-volts ($\\text{{eV}}$).\n"
        "2. Calculate the maximum kinetic energy ($K_{{\\max}}$) of the emitted photoelectrons in $\\text{{eV}}$."
    )
    ans = f"$E_{{\\text{{photon}}}} = {_fmt_sa(e_photon_ev)}\\text{{ eV}}$, $K_{{\\max}} = {_fmt_sa(k_max_ev)}\\text{{ eV}}$"
    steps = [
        {"rule": "Calculate photon energy in Joules then convert to eV", "op": f"E = \\frac{{hf}}{{e}} = \\frac{{(6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_inc)})}}{{1{{,}}6 \\times 10^{{-19}}}}", "to": f"{_fmt_sa(e_photon_ev)}\\text{{ eV}}"},
        {"rule": "Apply photoelectric equation in eV units", "op": f"K_{{\\max}} = E - W_0 = {_fmt_sa(e_photon_ev)} - {_fmt_sa(w0_ev)}", "to": f"{_fmt_sa(k_max_ev)}\\text{{ eV}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="In eV units, the equation remains E = W0 + K_max.",
        t2=f"E_photon = hf / e = {_fmt_sa(e_photon_ev)} eV. K_max = E_photon - W0.",
        t3=f"K_max = {_fmt_sa(e_photon_ev)} - {_fmt_sa(w0_ev)} = {_fmt_sa(k_max_ev)} eV.",
        misconceptions=["mixing_joules_and_electron_volts_in_the_same_subtraction_equation"],
        marks=4,
    )


def _build_13(rng: random.Random) -> Dict[str, Any]:
    sub = "13_maximum_speed_of_photoelectrons"
    metal = rng.choice(METALS_REF)
    w0 = metal["w0_j"]
    f0 = metal["f0"]
    mult = rng.choice([1.4, 1.6, 1.8, 2.0])
    f_inc = f0 * mult
    k_max = (H * f_inc) - w0
    v_max = math.sqrt((2 * k_max) / ME)

    prompt = (
        f"A beam of light of frequency ${_fmt_sci(f_inc)}\\text{{ Hz}}$ is directed at a {metal['name']} cathode ($W_0 = {_fmt_sci(w0)}\\text{{ J}}$).\n\n"
        "1. Calculate the maximum kinetic energy ($K_{{\\max}}$) of the ejected electrons.\n"
        "2. Calculate the maximum speed ($v_{{\\max}}$) of the emitted photoelectrons. (Take $m_e = 9{{,}}11 \\times 10^{-31}\\text{{ kg}}$.)"
    )
    ans = f"$K_{{\\max}} = {_fmt_sci(k_max)}\\text{{ J}}$, $v_{{\\max}} = {_fmt_sci(v_max)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    steps = [
        {"rule": "Calculate maximum kinetic energy using Einstein's equation", "op": f"K_{{\\max}} = hf - W_0 = (6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_inc)}) - {_fmt_sci(w0)}", "to": f"{_fmt_sci(k_max)}\\text{{ J}}"},
        {"rule": "Calculate maximum photoelectron speed using kinetic energy formula", "op": f"v_{{\\max}} = \\sqrt{{\\frac{{2 K_{{\\max}}}}{{m_e}}}} = \\sqrt{{\\frac{{2({_fmt_sci(k_max)})}}{{9{{,}}11 \\times 10^{{-31}}}}}}", "to": f"{_fmt_sci(v_max)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="K_max = 0,5 * m_e * (v_max)^2, where m_e = 9,11 x 10^-31 kg.",
        t2=f"v_max = sqrt(2 * K_max / m_e).",
        t3=f"K_max = {_fmt_sci(k_max)} J, v_max = {_fmt_sci(v_max)} m/s.",
        misconceptions=["forgetting_the_square_root_when_solving_for_speed"],
        marks=5,
    )


def _build_14(rng: random.Random) -> Dict[str, Any]:
    sub = "14_work_function_from_kinetic_energy_and_frequency"
    metal = rng.choice(METALS_REF)
    w0 = metal["w0_j"]
    f0 = metal["f0"]
    mult = rng.choice([1.4, 1.5, 1.7])
    f_inc = f0 * mult
    k_max = (H * f_inc) - w0

    prompt = (
        f"In a photoelectric experiment, light of frequency ${_fmt_sci(f_inc)}\\text{{ Hz}}$ strikes an unknown metal cathode. "
        f"The maximum kinetic energy of the emitted photoelectrons is measured to be ${_fmt_sci(k_max)}\\text{{ J}}$.\n\n"
        "1. Calculate the energy of an incident photon.\n"
        "2. Calculate the work function ($W_0$) of the metal cathode."
    )
    e_photon = H * f_inc
    ans = f"$E = {_fmt_sci(e_photon)}\\text{{ J}}$, $W_0 = {_fmt_sci(w0)}\\text{{ J}}$"
    steps = [
        {"rule": "Calculate incident photon energy", "op": f"E = hf = (6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_inc)})", "to": f"{_fmt_sci(e_photon)}\\text{{ J}}"},
        {"rule": "Calculate work function by rearranging photoelectric equation", "op": f"W_0 = hf - K_{{\\max}} = {_fmt_sci(e_photon)} - {_fmt_sci(k_max)}", "to": f"{_fmt_sci(w0)}\\text{{ J}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Rearrange Einstein's photoelectric equation: W0 = h * f - K_max.",
        t2=f"W0 = {_fmt_sci(e_photon)} - {_fmt_sci(k_max)} J.",
        t3=f"W0 = {_fmt_sci(w0)} J.",
        misconceptions=["adding_k_max_instead_of_subtracting_it_from_photon_energy"],
        marks=4,
    )


def _build_15(rng: random.Random) -> Dict[str, Any]:
    sub = "15_incident_frequency_from_work_function_and_kinetic_energy"
    metal = rng.choice(METALS_REF)
    w0 = metal["w0_j"]
    k_desired = rng.choice([1.2e-19, 1.6e-19, 2.4e-19, 3.2e-19])
    e_req = w0 + k_desired
    f_req = e_req / H

    prompt = (
        f"A photocell uses a {metal['name']} cathode with a work function of ${_fmt_sci(w0)}\\text{{ J}}$.\n\n"
        f"Calculate the minimum frequency of light required to eject photoelectrons with a maximum kinetic energy of ${_fmt_sci(k_desired)}\\text{{ J}}$."
    )
    ans = f"$f = {_fmt_sci(f_req)}\\text{{ Hz}}$"
    steps = [
        {"rule": "Calculate total photon energy required", "op": f"E = W_0 + K_{{\\max}} = {_fmt_sci(w0)} + {_fmt_sci(k_desired)}", "to": f"{_fmt_sci(e_req)}\\text{{ J}}"},
        {"rule": "Calculate frequency from photon energy", "op": f"f = \\frac{{E}}{{h}} = \\frac{{{_fmt_sci(e_req)}}}{{6{{,}}63 \\times 10^{{-34}}}}", "to": f"{_fmt_sci(f_req)}\\text{{ Hz}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The incident photon must supply both the work function W0 and the desired kinetic energy K_max: h * f = W0 + K_max.",
        t2=f"f = (W0 + K_max) / h.",
        t3=f"f = {_fmt_sci(f_req)} Hz.",
        misconceptions=["dividing_only_k_max_by_plancks_constant_and_ignoring_w0"],
        marks=4,
    )


def _build_16(rng: random.Random) -> Dict[str, Any]:
    sub = "16_effect_of_doubling_frequency_on_kinetic_energy"
    w0 = 3.6e-19
    f0 = w0 / H
    f1 = 1.5 * f0
    k1 = (H * f1) - w0
    f2 = 2.0 * f1
    k2 = (H * f2) - w0
    ratio = round(k2 / k1, 2)

    prompt = (
        "A metal surface is illuminated by radiation of frequency $f_1$, producing photoelectrons with maximum kinetic energy $K_1$.\n\n"
        "If the frequency of the incident radiation is now doubled to $f_2 = 2 f_1$:\n"
        "1. State whether the new maximum kinetic energy $K_2$ will be *equal to $2 K_1$*, *less than $2 K_1$*, or *greater than $2 K_1$*.\n"
        "2. Prove your answer mathematically using Einstein's photoelectric equation."
    )
    ans = f"$K_2$ is greater than $2 K_1$ ($K_2 > 2 K_1$); Proof: $K_2 = 2hf_1 - W_0 = 2(W_0 + K_1) - W_0 = 2K_1 + W_0 > 2K_1$"
    steps = [
        {"rule": "State relationship", "op": "\\text{{Comparison}}", "to": "K_2 > 2 K_1"},
        {"rule": "Formulate algebraic proof using photoelectric equation", "op": "K_2 = h(2f_1) - W_0 = 2hf_1 - W_0 = 2(W_0 + K_1) - W_0 = 2K_1 + W_0", "to": "\\text{Since } W_0 > 0,\\; K_2 > 2K_1"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Kinetic energy is NOT directly proportional to frequency because of the work function offset: K_max = hf - W0.",
        t2="K2 = 2hf1 - W0 = 2(K1 + W0) - W0 = 2 K1 + W0. Because W0 > 0, K2 is strictly greater than 2 K1.",
        t3="Greater than 2 K1.",
        misconceptions=["assuming_kinetic_energy_doubles_when_frequency_doubles"],
        marks=4,
    )


def _build_17(rng: random.Random) -> Dict[str, Any]:
    sub = "17_effect_of_light_intensity_on_kinetic_energy_and_speed"
    metal = rng.choice(["sodium", "potassium", "zinc", "copper"])
    prompt = (
        f"Monochromatic blue light shines on a clean {metal} cathode in a vacuum photocell, causing photoelectrons to be ejected.\n\n"
        "The intensity (brightness) of the blue light is now increased while its frequency remains constant.\n\n"
        "1. State the effect of this change on the maximum kinetic energy ($K_{{\\max}}$) of the emitted photoelectrons. (Choose from *increases*, *decreases*, or *remains unchanged*).\n"
        "2. State the effect of this change on the maximum speed ($v_{{\\max}}$) of the emitted photoelectrons.\n"
        "3. Provide a clear scientific explanation based on the photon model of light."
    )
    ans = "1. Remains unchanged; 2. Remains unchanged; 3. Increasing intensity increases the number of photons per second, but does not alter the energy of individual photons ($E = hf$). Since each electron absorbs only one photon, $K_{\\max}$ and $v_{\\max}$ remain constant."
    steps = [
        {"rule": "State effect on K_max", "op": "K_{{\\max}} = hf - W_0", "to": "\\text{{Remains unchanged}}"},
        {"rule": "State effect on v_max", "op": "v_{{\\max}} = \\sqrt{2 K_{{\\max}}/m_e}", "to": "\\text{{Remains unchanged}}"},
        {"rule": "Explain via photon theory", "op": "\\text{{One-to-one interaction}}", "to": "\\text{{Intensity changes photon arrival rate, not individual photon energy}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Intensity represents the number of photons striking per second (brightness), not the energy of individual photons.",
        t2="Maximum kinetic energy depends ONLY on frequency: K_max = hf - W0.",
        t3="Remains unchanged; photon energy depends only on frequency.",
        misconceptions=["believing_higher_light_intensity_makes_electrons_move_faster"],
        marks=4,
    )


def _build_18(rng: random.Random) -> Dict[str, Any]:
    sub = "18_effect_of_light_intensity_on_photoelectron_emission_rate"
    metal = rng.choice(["sodium", "caesium", "potassium"])
    factor = rng.choice([2, 3, 4])
    prompt = (
        f"A beam of light of frequency $f > f_0$ shines on a {metal} plate, producing a photocurrent $I_1$ in an external circuit.\n\n"
        f"The intensity of the light is now increased by a factor of {_fmt_sa(factor)} without changing its frequency.\n\n"
        "1. State the effect on the number of photoelectrons emitted per second.\n"
        f"2. By what factor does the photocurrent ($I$) in the circuit increase?"
    )
    ans = f"Increases by a factor of {_fmt_sa(factor)}; Photocurrent increases by a factor of {_fmt_sa(factor)}"
    steps = [
        {"rule": "Relate light intensity to photon arrival rate", "op": "\\text{{Intensity}} \\propto \\text{{photons per second}}", "to": f"\\text{{Ejection rate increases by a factor of }} {_fmt_sa(factor)}"},
        {"rule": "Relate emission rate to electric current", "op": f"I = \\frac{{\\Delta q}}{{\\Delta t}} = \\frac{{n_e e}}{{\\Delta t}}", "to": f"\\text{{Photocurrent increases by factor of }} {_fmt_sa(factor)}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Each photon ejects one electron. If intensity increases by factor N, the number of photons per second increases by factor N.",
        t2="Photocurrent I = (number of electrons / time) * e, so photocurrent is directly proportional to intensity.",
        t3=f"Increases by factor of {_fmt_sa(factor)}.",
        misconceptions=["thinking_photocurrent_is_independent_of_light_intensity"],
        marks=3,
    )


def _build_19(rng: random.Random) -> Dict[str, Any]:
    sub = "19_instantaneous_emission_no_time_lag"
    prompt = (
        "One of the major contradictions of classical wave theory was the absence of any measurable time delay in the photoelectric effect.\n\n"
        "1. State how quickly photoelectrons are emitted once light of suitable frequency strikes a metal surface.\n"
        "2. Explain why classical wave theory predicted a significant time delay for very dim light.\n"
        "3. Explain why Einstein's photon hypothesis accounts for instantaneous emission even with dim light."
    )
    ans = "1. Instantaneously (within less than $10^{-9}\\text{ s}$ / no time delay); 2. Classical waves spread energy uniformly across the surface, so an electron would have to wait hours to accumulate enough energy; 3. Photon energy is concentrated in localized packets; a single photon delivers all its energy to an electron in an instantaneous one-to-one collision."
    steps = [
        {"rule": "State observation of instantaneous emission", "op": "\\Delta t < 10^{{-9}}\\text{{ s}}", "to": "\\text{{Instantaneous emission with no time lag}}"},
        {"rule": "Explain classical wave theory prediction of time lag", "op": "\\text{{Continuous wave energy distribution}}", "to": "\\text{{Low intensity waves spread energy thinly, requiring time to accumulate W_0}}"},
        {"rule": "Explain quantum photon mechanism", "op": "\\text{{Localized energy packet}}", "to": "\\text{{Instantaneous all-or-nothing energy transfer in one-to-one collision}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="In the photon model, energy is delivered all at once by a single photon collision, so emission is instantaneous.",
        t2="Classical physics treated light as a continuous spread-out wavefront, requiring time for an electron to absorb enough energy.",
        t3="Instantaneous emission; localized photon collision delivers full energy at once.",
        misconceptions=["believing_dim_light_takes_several_minutes_to_emit_its_first_photoelectron"],
        marks=4,
    )


def _build_20(rng: random.Random) -> Dict[str, Any]:
    sub = "20_wavelength_decrease_effect_on_photoelectron_speed"
    metal = rng.choice(METALS_REF)
    w0 = metal["w0_j"]
    lambda1_nm = rng.choice([380, 420, 450])
    lambda2_nm = rng.choice([250, 280, 300])

    prompt = (
        f"A {metal['name']} cathode ($W_0 = {_fmt_sci(w0)}\\text{{ J}}$) is illuminated by radiation of wavelength $\\lambda_1 = {_fmt_sa(lambda1_nm)}\\text{{ nm}}$.\n\n"
        f"The wavelength of the incident radiation is now decreased to $\\lambda_2 = {_fmt_sa(lambda2_nm)}\\text{{ nm}}$.\n\n"
        "1. Explain what happens to the energy of the incident photons when the wavelength decreases.\n"
        "2. State the effect of this decrease in wavelength on the maximum speed ($v_{{\\max}}$) of the emitted photoelectrons."
    )
    ans = "1. Photon energy increases because $E = \\frac{hc}{\\lambda}$; 2. Maximum speed of photoelectrons increases because $K_{\\max} = E - W_0$ increases, and $v_{\\max} = \\sqrt{2K_{\\max}/m_e}$."
    steps = [
        {"rule": "Relate wavelength to photon energy", "op": "E = \\frac{{hc}}{{\\lambda}}", "to": "\\text{{Decreasing wavelength increases photon energy}}"},
        {"rule": "Relate photon energy to photoelectron speed", "op": "v_{{\\max}} = \\sqrt{{\\frac{{2(E - W_0)}}{{m_e}}}}", "to": "\\text{{Maximum speed increases}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Shorter wavelength means higher frequency and greater photon energy (E = hc / λ).",
        t2="Since photon energy increases while work function W0 stays constant, K_max increases, so v_max increases.",
        t3="Photon energy increases; photoelectron maximum speed increases.",
        misconceptions=["confusing_wavelength_with_frequency_and_predicting_speed_decreases"],
        marks=4,
    )


def _build_21(rng: random.Random) -> Dict[str, Any]:
    sub = "21_stopping_potential_definition_and_principle"
    prompt = (
        "In a photoelectric cell experiment, a variable reverse (retarding) voltage is applied between the anode and cathode.\n\n"
        "1. Define the term **stopping potential** ($V_{{\\text{{stop}}}}$).\n"
        "2. State the equation that connects the stopping potential ($V_{{\\text{{stop}}}}$) to the maximum kinetic energy ($K_{{\\max}}$) of the photoelectrons.\n"
        "3. Explain why the photocurrent drops to zero when the applied reverse potential reaches $V_{{\\text{{stop}}}}$."
    )
    ans = "1. Stopping potential: The minimum retarding potential difference needed to stop the fastest emitted photoelectrons from reaching the collector anode; 2. $e V_{\\text{stop}} = K_{\\max}$; 3. The retarding electric field does negative work on the photoelectrons ($W = -e V_{\\text{stop}}$); when this work equals $K_{\\max}$, even the most energetic electrons are brought to rest before touching the anode."
    steps = [
        {"rule": "Define stopping potential", "op": "\\text{{Definition}}", "to": "\\text{{Minimum reverse potential required to reduce photocurrent to zero}}"},
        {"rule": "State relationship with maximum kinetic energy", "op": "e V_{{\\text{{stop}}}} = K_{{\\max}}", "to": "V_{{\\text{{stop}}}} = \\frac{{K_{{\\max}}}}{{e}}"},
        {"rule": "Explain electrostatic stopping mechanism", "op": "W_{{\\text{{electric}}}} = qV = K_{{\\max}}", "to": "\\text{{Fastest electrons lose all kinetic energy against electric field}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The stopping potential V_stop is the negative voltage that stops even the most energetic photoelectrons from reaching the anode.",
        t2="Electric work = q * V_stop = e * V_stop = K_max.",
        t3="Minimum retarding potential reducing photocurrent to zero; e * V_stop = K_max.",
        misconceptions=["confusing_stopping_potential_with_work_function"],
        marks=4,
    )


def _build_22(rng: random.Random) -> Dict[str, Any]:
    sub = "22_stopping_potential_calculation_from_kinetic_energy"
    k_max_j = rng.choice([1.8e-19, 2.4e-19, 3.2e-19, 4.0e-19, 4.8e-19])
    v_stop = round(k_max_j / QE, 2)

    prompt = (
        f"Photoelectrons emitted from a photocell surface have a maximum kinetic energy of ${_fmt_sci(k_max_j)}\\text{{ J}}$.\n\n"
        "Calculate the stopping potential ($V_{{\\text{{stop}}}}$) required to reduce the photocurrent to zero."
    )
    ans = f"$V_{{\\text{{stop}}}} = {_fmt_sa(v_stop)}\\text{{ V}}$"
    steps = [
        {"rule": "Apply stopping potential equation e * V_stop = K_max", "op": "e V_{{\\text{{stop}}}} = K_{{\\max}} \\implies V_{{\\text{{stop}}}} = \\frac{{K_{{\\max}}}}{{e}}", "to": f"V_{{\\text{{stop}}}} = \\frac{{{_fmt_sci(k_max_j)}}}{{1{{,}}6 \\times 10^{{-19}}}}"},
        {"rule": "Calculate numerical stopping potential", "op": f"V_{{\\text{{stop}}}} = \\frac{{{_fmt_sci(k_max_j)}}}{{1{{,}}6 \\times 10^{{-19}}}}", "to": f"{_fmt_sa(v_stop)}\\text{{ V}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="e * V_stop = K_max, so V_stop = K_max / e.",
        t2=f"V_stop = ({_fmt_sci(k_max_j)}) / (1,6 x 10^-19).",
        t3=f"V_stop = {_fmt_sa(v_stop)} V.",
        misconceptions=["multiplying_by_elementary_charge_instead_of_dividing"],
        marks=3,
    )


def _build_23(rng: random.Random) -> Dict[str, Any]:
    sub = "23_stopping_potential_from_incident_frequency_and_work_function"
    metal = rng.choice(METALS_REF)
    w0 = metal["w0_j"]
    f0 = metal["f0"]
    mult = rng.choice([1.5, 1.7, 1.9, 2.2])
    f_inc = f0 * mult
    k_max = (H * f_inc) - w0
    v_stop = round(k_max / QE, 2)

    prompt = (
        f"Radiation of frequency ${_fmt_sci(f_inc)}\\text{{ Hz}}$ shines on a {metal['name']} photocell cathode "
        f"with a work function of ${_fmt_sci(w0)}\\text{{ J}}$.\n\n"
        "1. Calculate the maximum kinetic energy ($K_{{\\max}}$) of the emitted photoelectrons.\n"
        "2. Calculate the stopping potential ($V_{{\\text{{stop}}}}$) in Volts."
    )
    ans = f"$K_{{\\max}} = {_fmt_sci(k_max)}\\text{{ J}}$, $V_{{\\text{{stop}}}} = {_fmt_sa(v_stop)}\\text{{ V}}$"
    steps = [
        {"rule": "Calculate maximum kinetic energy using photoelectric equation", "op": f"K_{{\\max}} = hf - W_0 = (6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_inc)}) - {_fmt_sci(w0)}", "to": f"{_fmt_sci(k_max)}\\text{{ J}}"},
        {"rule": "Calculate stopping potential from K_max", "op": f"V_{{\\text{{stop}}}} = \\frac{{K_{{\\max}}}}{{e}} = \\frac{{{_fmt_sci(k_max)}}}{{1{{,}}6 \\times 10^{{-19}}}}", "to": f"{_fmt_sa(v_stop)}\\text{{ V}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="First find K_max using K_max = hf - W0. Then find V_stop using V_stop = K_max / e.",
        t2=f"K_max = {_fmt_sci(k_max)} J, V_stop = {_fmt_sa(v_stop)} V.",
        t3=f"V_stop = {_fmt_sa(v_stop)} V.",
        misconceptions=["dividing_incident_frequency_by_e_instead_of_kinetic_energy"],
        marks=5,
    )


def _build_24(rng: random.Random) -> Dict[str, Any]:
    sub = "24_photocell_retarding_circuit_diagram"
    v_ret = rng.choice([1.2, 1.5, 1.8, 2.4])
    f_inc_14 = rng.choice([7.5, 8.2, 9.0, 10.5])
    svg_str = _svg_photocell_circuit(v_ret, f_inc_14)

    prompt = (
        "Refer to the accompanying vector diagram illustrating a vacuum photocell connected in a circuit with a variable retarding potential source and a microammeter.\n\n"
        f"Monochromatic ultraviolet light of frequency ${_fmt_sa(f_inc_14)} \\times 10^{{14}}\\text{{ Hz}}$ strikes the cathode, emitting electrons towards the anode.\n\n"
        "1. Identify the polarity of the anode relative to the cathode in a retarding (stopping potential) circuit.\n"
        "2. Explain what happens to the reading on the microammeter as the retarding voltage is gradually increased from $0\\text{{ V}}$ up to the stopping potential $V_{{\\text{{stop}}}}$.\n"
        f"3. If the microammeter reading reaches exactly zero when the reverse voltage is ${_fmt_sa(v_ret)}\\text{{ V}}$, state the maximum kinetic energy of the photoelectrons in electron-volts ($\\text{{eV}}$)."
    )
    ans = f"Anode is negative relative to cathode; Microammeter reading decreases steadily to zero; $K_{{\\max}} = {_fmt_sa(v_ret)}\\text{{ eV}}$"
    steps = [
        {"rule": "Identify anode polarity in retarding configuration", "op": "\\text{{Retarding configuration}}", "to": "\\text{{Anode is negative, cathode is positive}}"},
        {"rule": "Explain current decrease as retarding potential opposes electrons", "op": "\\text{{Opposing electric force}}", "to": "\\text{{Fewer electrons reach the anode; current drops to zero at }} V_{{\\text{{stop}}}}"},
        {"rule": "Convert stopping potential directly to maximum kinetic energy in eV", "op": f"K_{{\\max}} = e V_{{\\text{{stop}}}} \\implies K_{{\\max}} = {_fmt_sa(v_ret)}\\text{{ eV}}", "to": f"{_fmt_sa(v_ret)}\\text{{ eV}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Photocell Retarding Circuit Diagram"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="In a retarding circuit, the collector anode is made negative so it repels incoming photoelectrons.",
        t2="When V = V_stop, the photocurrent drops to zero. The numerical value of V_stop in Volts equals K_max in eV.",
        t3=f"Anode is negative; current drops to zero; K_max = {_fmt_sa(v_ret)} eV.",
        misconceptions=["believing_the_anode_must_be_positive_to_stop_electrons"],
        marks=5,
        diagram_spec=d_spec,
    )


def _build_25(rng: random.Random) -> Dict[str, Any]:
    sub = "25_gold_leaf_electroscope_photoelectric_investigation"
    angle = rng.choice([35, 40, 45])
    svg_str = _svg_electroscope(angle, has_uv=True)

    prompt = (
        "Refer to the accompanying vector diagram illustrating a gold-leaf electroscope investigation of the photoelectric effect.\n\n"
        "A freshly polished zinc plate is mounted on a gold-leaf electroscope and given an initial **negative charge**, "
        f"causing the gold leaf to diverge to an angle of ${_fmt_sa(angle)}^\\circ$.\n\n"
        "1. Explain what happens to the gold leaf when ultraviolet (UV) radiation is shone on the negatively charged zinc plate.\n"
        "2. State what happens to the leaf if a sheet of ordinary window glass is placed between the UV source and the zinc plate.\n"
        "3. Explain what happens if the experiment is repeated with the zinc plate initially given a **positive charge**."
    )
    ans = "1. The gold leaf collapses rapidly (UV light ejects electrons, discharging the negative electroscope); 2. The leaf remains diverged (glass absorbs UV radiation); 3. The leaf does not collapse (any ejected electrons are immediately attracted back to the positively charged plate)."
    steps = [
        {"rule": "Explain discharge of negative electroscope under UV light", "op": "\\text{{Photoelectric ejection of electrons}}", "to": "\\text{{Negatively charged zinc loses excess electrons; leaf collapses}}"},
        {"rule": "Explain effect of inserting glass plate", "op": "\\text{{UV absorption by glass}}", "to": "\\text{{Glass blocks UV radiation; no electrons ejected; leaf stays diverged}}"},
        {"rule": "Explain behavior with positively charged electroscope", "op": "\\text{{Electrostatic attraction to positive plate}}", "to": "\\text{{Positive plate pulls ejected electrons back; net positive charge remains}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Gold-Leaf Electroscope Photoelectric Investigation"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="UV light on a negatively charged zinc plate ejects excess electrons, discharging the electroscope and causing the leaf to drop.",
        t2="Ordinary glass blocks UV light, preventing emission. A positively charged plate attracts ejected electrons back immediately.",
        t3="Leaf collapses; glass stops collapse; positive plate does not discharge.",
        misconceptions=["thinking_positive_charges_can_be_photoelectrically_ejected_from_the_metal"],
        marks=5,
        diagram_spec=d_spec,
    )


# =========================================================================== #
# Export Mapping
# =========================================================================== #

BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_photoelectric_effect_definition_and_significance": _build_01,
    "02_failure_of_classical_wave_theory": _build_02,
    "03_photon_energy_from_frequency": _build_03,
    "04_photon_energy_from_wavelength": _build_04,
    "05_electron_volt_and_joule_energy_conversions": _build_05,
    "06_work_function_definition": _build_06,
    "07_threshold_frequency_calculation": _build_07,
    "08_threshold_wavelength_calculation": _build_08,
    "09_metal_identification_from_threshold_frequency": _build_09,
    "10_emission_condition_frequency_vs_threshold": _build_10,
    "11_photoelectric_equation_maximum_kinetic_energy": _build_11,
    "12_photoelectric_equation_kinetic_energy_in_ev": _build_12,
    "13_maximum_speed_of_photoelectrons": _build_13,
    "14_work_function_from_kinetic_energy_and_frequency": _build_14,
    "15_incident_frequency_from_work_function_and_kinetic_energy": _build_15,
    "16_effect_of_doubling_frequency_on_kinetic_energy": _build_16,
    "17_effect_of_light_intensity_on_kinetic_energy_and_speed": _build_17,
    "18_effect_of_light_intensity_on_photoelectron_emission_rate": _build_18,
    "19_instantaneous_emission_no_time_lag": _build_19,
    "20_wavelength_decrease_effect_on_photoelectron_speed": _build_20,
    "21_stopping_potential_definition_and_principle": _build_21,
    "22_stopping_potential_calculation_from_kinetic_energy": _build_22,
    "23_stopping_potential_from_incident_frequency_and_work_function": _build_23,
    "24_photocell_retarding_circuit_diagram": _build_24,
    "25_gold_leaf_electroscope_photoelectric_investigation": _build_25,
}

SUBSKILLS_01_25: List[str] = list(BUILDERS_01_25.keys())
