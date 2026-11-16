"""
optical_phenomena_photoelectric_archetypes_26_50.py
---------------------------------------------------
Grade 12 Physical Sciences — Optical Phenomena & Properties of Matter (Subskills 26–50).
Covering Photoelectric Graphs, Intensity & Photocurrent, Atomic Spectra, & Synthesis:
  26. 26_photon_arrival_rate_from_beam_power
  27. 27_saturation_photocurrent_calculation
  28. 28_quantum_efficiency_calculation
  29. 29_photocurrent_vs_incident_light_intensity
  30. 30_photocurrent_vs_potential_difference_curve
  31. 31_effect_of_doubling_intensity_on_iv_curve
  32. 32_effect_of_increasing_frequency_on_iv_curve
  33. 33_kinetic_energy_vs_frequency_graph_planck_gradient
  34. 34_kinetic_energy_vs_frequency_graph_work_function_intercept
  35. 35_parallel_kmax_vs_frequency_lines_for_different_metals
  36. 36_stopping_potential_vs_frequency_graph
  37. 37_continuous_spectrum_definition_and_origin
  38. 38_line_emission_spectrum_definition_and_origin
  39. 39_line_absorption_spectrum_definition_and_origin
  40. 40_atomic_spectral_fingerprinting
  41. 41_fraunhofer_lines_solar_absorption_spectrum
  42. 42_discrete_energy_levels_in_atoms
  43. 43_bohr_energy_level_transition_photon_emission
  44. 44_bohr_energy_level_transition_wavelength
  45. 45_electron_excitation_energy_absorption
  46. 46_atomic_ionization_energy
  47. 47_hydrogen_emission_series_balmer_lyman_paschen
  48. 48_wave_particle_duality_of_light
  49. 49_skills_for_science_plancks_constant_uncertainty
  50. 50_photoelectric_and_spectra_diagnostic_synthesis

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

# Physical Constants
H = 6.63e-34    # J·s (Planck's constant)
C = 3.0e8       # m·s⁻¹ (Speed of light)
ME = 9.11e-31   # kg (Electron mass)
QE = 1.6e-19    # C (Elementary charge)


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

def _svg_kmax_vs_f(f0_val: float, w0_val: float, metal_name: str = "Sodium") -> str:
    """Generate responsive K_max vs frequency graph."""
    w, h = 500, 240
    ox, oy = 75, 170
    plot_w, plot_h = 390, 130
    x_f0 = ox + 140
    y_top = oy - plot_h
    x_max = ox + plot_w

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .axis { stroke: #475569; stroke-width: 1.5; }',
        '    .grid { stroke: #cbd5e1; stroke-width: 1; stroke-dasharray: 4,4; }',
        '    .trace { stroke: #2563eb; stroke-width: 2.5; fill: none; }',
        '    .ext { stroke: #94a3b8; stroke-width: 1.5; stroke-dasharray: 3,3; }',
        '  </style>',
        f'  <line x1="{ox}" y1="{oy}" x2="{ox + plot_w + 20}" y2="{oy}" class="axis" />',
        f'  <line x1="{ox}" y1="{y_top - 15}" x2="{ox}" y2="{oy + 50}" class="axis" />',
        f'  <text x="{ox + plot_w + 5}" y="{oy - 8}" class="lbl">f (×10¹⁴ Hz)</text>',
        f'  <text x="{ox - 65}" y="{y_top - 5}" class="lbl">K_max (×10⁻¹⁹ J)</text>',
        # Main line above f0
        f'  <line x1="{x_f0}" y1="{oy}" x2="{x_max}" y2="{y_top + 10}" class="trace" />',
        # Dotted extrapolation to y-intercept (-W0)
        f'  <line x1="{ox}" y1="{oy + 40}" x2="{x_f0}" y2="{oy}" class="ext" />',
        # Points and labels
        f'  <circle cx="{x_f0}" cy="{oy}" r="4" fill="#2563eb" />',
        f'  <text x="{x_f0 - 10}" y="{oy + 18}" class="lbl">f₀ = {_fmt_sa(f0_val)}</text>',
        f'  <text x="{ox - 65}" y="{oy + 44}" class="lbl">-W₀ = -{_fmt_sa(w0_val)}</text>',
        f'  <text x="{x_f0 + 50}" y="{oy - 45}" class="lbl" fill="#1e40af">Gradient = h ({metal_name})</text>',
        '</svg>',
    ]
    return "\n".join(svg)


def _svg_iv_curves(v_stop: float, i_sat1: float, i_sat2: float) -> str:
    """Generate responsive photocurrent vs potential difference (I-V) characteristic curve."""
    w, h = 500, 240
    ox, oy = 210, 160
    plot_w, plot_h = 250, 120
    x_stop = ox - 110

    # Path 1: lower intensity I1
    d1 = f"M {x_stop} {oy} C {ox - 30} {oy}, {ox + 30} {oy - 60}, {ox + plot_w} {oy - 60}"
    # Path 2: double intensity I2
    d2 = f"M {x_stop} {oy} C {ox - 30} {oy}, {ox + 30} {oy - 110}, {ox + plot_w} {oy - 110}"

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .axis { stroke: #475569; stroke-width: 1.5; }',
        '    .c1 { stroke: #0284c7; stroke-width: 2.2; fill: none; }',
        '    .c2 { stroke: #dc2626; stroke-width: 2.2; fill: none; }',
        '  </style>',
        f'  <line x1="60" y1="{oy}" x2="{ox + plot_w + 20}" y2="{oy}" class="axis" />',
        f'  <line x1="{ox}" y1="{oy - plot_h - 15}" x2="{ox}" y2="{oy + 25}" class="axis" />',
        f'  <text x="{ox + plot_w + 5}" y="{oy + 18}" class="lbl">V (Volts)</text>',
        f'  <text x="{ox - 50}" y="{oy - plot_h}" class="lbl">I (μA)</text>',
        f'  <path d="{d1}" class="c1" />',
        f'  <path d="{d2}" class="c2" />',
        f'  <circle cx="{x_stop}" cy="{oy}" r="4" fill="#0f172a" />',
        f'  <text x="{x_stop - 25}" y="{oy + 18}" class="lbl">-V_stop (-{_fmt_sa(v_stop)} V)</text>',
        f'  <text x="{ox + plot_w - 70}" y="{oy - 68}" class="lbl" fill="#0284c7">Intensity 1 ({_fmt_sa(i_sat1)} μA)</text>',
        f'  <text x="{ox + plot_w - 70}" y="{oy - 118}" class="lbl" fill="#dc2626">Intensity 2 ({_fmt_sa(i_sat2)} μA)</text>',
        '</svg>',
    ]
    return "\n".join(svg)


def _svg_spectral_strip(lines_nm: List[float], is_emission: bool = True) -> str:
    """Generate responsive atomic spectral strip diagram."""
    w, h = 500, 160
    ox, oy = 50, 45
    strip_w, strip_h = 400, 50

    # Wavelength mapped from 400 nm (violet) to 700 nm (red)
    def _map_x(l_nm: float) -> float:
        return ox + ((l_nm - 400.0) / 300.0) * strip_w

    bg_fill = "#0f172a" if is_emission else "url(#rainbowGrad)"

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="150" xmlns="http://www.w3.org/2000/svg">',
        '  <defs>',
        '    <linearGradient id="rainbowGrad" x1="0%" y1="0%" x2="100%" y2="0%">',
        '      <stop offset="0%" stop-color="#7c3aed" />',
        '      <stop offset="25%" stop-color="#2563eb" />',
        '      <stop offset="50%" stop-color="#16a34a" />',
        '      <stop offset="75%" stop-color="#eab308" />',
        '      <stop offset="100%" stop-color="#dc2626" />',
        '    </linearGradient>',
        '  </defs>',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '  </style>',
        f'  <rect x="{ox}" y="{oy}" width="{strip_w}" height="{strip_h}" fill="{bg_fill}" stroke="#334155" stroke-width="2" rx="4" />',
        f'  <text x="{ox}" y="{oy - 12}" class="lbl">400 nm (Violet)</text>',
        f'  <text x="{ox + strip_w - 75}" y="{oy - 12}" class="lbl">700 nm (Red)</text>',
    ]

    title = "Line Emission Spectrum (Bright lines on dark background)" if is_emission else "Line Absorption Spectrum (Dark lines on continuous spectrum)"
    svg.append(f'  <text x="{ox + 40}" y="{oy + strip_h + 35}" class="lbl" fill="#1e293b">{title}</text>')

    for l_val in lines_nm:
        lx = _map_x(l_val)
        if is_emission:
            # Color depends on wavelength
            line_color = "#38bdf8" if l_val < 480 else ("#4ade80" if l_val < 560 else "#f87171")
            svg.append(f'  <line x1="{lx:.1f}" y1="{oy}" x2="{lx:.1f}" y2="{oy + strip_h}" stroke="{line_color}" stroke-width="2.5" />')
        else:
            # Dark absorption line
            svg.append(f'  <line x1="{lx:.1f}" y1="{oy}" x2="{lx:.1f}" y2="{oy + strip_h}" stroke="#0f172a" stroke-width="3" />')
        svg.append(f'  <text x="{lx - 12:.1f}" y="{oy + strip_h + 16}" class="lbl">{_fmt_sa(l_val)}</text>')

    svg.append('</svg>')
    return "\n".join(svg)


def _svg_bohr_energy_levels(levels_ev: List[float], n_high: int, n_low: int) -> str:
    """Generate responsive Bohr atomic energy levels diagram."""
    w, h = 500, 230
    ox, oy = 90, 40
    plot_w, plot_h = 320, 140

    # Map levels: n=1 at bottom, n=infinity at top
    # level y: top is 0 eV (oy), bottom is -13.6 eV (oy + plot_h)
    e_min = min(levels_ev)
    e_range = abs(e_min)

    def _get_y(ev: float) -> float:
        frac = (0.0 - ev) / e_range
        return oy + frac * plot_h

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .level { stroke: #334155; stroke-width: 2; }',
        '    .trans { stroke: #dc2626; stroke-width: 2.2; marker-end: url(#arrow); }',
        '  </style>',
        '  <defs>',
        '    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">',
        '      <path d="M 0 0 L 10 5 L 0 10 z" fill="#dc2626" />',
        '    </marker>',
        '  </defs>',
        f'  <text x="{ox}" y="25" class="lbl" fill="#0369a1">Discrete Electron Energy Levels (E_n)</text>',
    ]

    # Draw level lines
    for i, ev in enumerate(levels_ev):
        n_num = i + 1
        ly = _get_y(ev)
        svg.append(f'  <line x1="{ox}" y1="{ly:.1f}" x2="{ox + plot_w}" y2="{ly:.1f}" class="level" />')
        svg.append(f'  <text x="{ox - 55}" y="{ly + 4:.1f}" class="lbl">n = {n_num}</text>')
        svg.append(f'  <text x="{ox + plot_w + 10}" y="{ly + 4:.1f}" class="lbl">{_fmt_sa(ev)} eV</text>')

    # Transition arrow
    y1 = _get_y(levels_ev[n_high - 1])
    y2 = _get_y(levels_ev[n_low - 1])
    x_trans = ox + 160
    svg.append(f'  <line x1="{x_trans}" y1="{y1:.1f}" x2="{x_trans}" y2="{y2 - 6:.1f}" class="trans" />')
    delta_ev = round(levels_ev[n_high - 1] - levels_ev[n_low - 1], 2)
    svg.append(f'  <text x="{x_trans + 12}" y="{(y1 + y2)/2:.1f}" class="lbl" fill="#b91c1c">Photon emitted (ΔE = {_fmt_sa(delta_ev)} eV)</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# =========================================================================== #
# Archetypes 26 to 50
# =========================================================================== #

def _build_26(rng: random.Random) -> Dict[str, Any]:
    sub = "26_photon_arrival_rate_from_beam_power"
    power_mw = rng.choice([5.0, 10.0, 15.0, 20.0, 25.0])
    wlen_nm = rng.choice([380, 420, 450, 500])
    power_w = power_mw * 1e-3
    wlen_m = wlen_nm * 1e-9
    e_photon = (H * C) / wlen_m
    n_rate = power_w / e_photon

    prompt = (
        f"A monochromatic laser beam with a wavelength of ${_fmt_sa(wlen_nm)}\\text{{ nm}}$ delivers a radiant power of "
        f"${_fmt_sa(power_mw)}\\text{{ mW}}$ onto a photocell cathode.\n\n"
        "1. Calculate the energy of a single photon in the laser beam.\n"
        "2. Calculate the number of photons striking the photocell cathode per second."
    )
    ans = f"$E_{{\\text{{photon}}}} = {_fmt_sci(e_photon)}\\text{{ J}}$, $N = {_fmt_sci(n_rate)}\\text{{ photons/s}}$"
    steps = [
        {"rule": "Calculate single photon energy from wavelength", "op": f"E = \\frac{{hc}}{{\\lambda}} = \\frac{{(6{{,}}63 \\times 10^{{-34}})(3{{,}}0 \\times 10^8)}}{{{_fmt_sci(wlen_m)}}}", "to": f"{_fmt_sci(e_photon)}\\text{{ J}}"},
        {"rule": "Calculate photon arrival rate from radiant beam power", "op": f"N = \\frac{{P}}{{E_{{\\text{{photon}}}}}} = \\frac{{{_fmt_sci(power_w)}}}{{{_fmt_sci(e_photon)}}}", "to": f"{_fmt_sci(n_rate)}\\text{{ photons}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Power is energy per unit time: P = N * E_photon, so N = P / E_photon.",
        t2=f"Convert power from mW to Watts (x 10^-3) and wavelength from nm to metres (x 10^-9).",
        t3=f"E = {_fmt_sci(e_photon)} J, photon rate = {_fmt_sci(n_rate)} photons/s.",
        misconceptions=["forgetting_to_convert_milliwatts_to_watts"],
        marks=4,
    )


def _build_27(rng: random.Random) -> Dict[str, Any]:
    sub = "27_saturation_photocurrent_calculation"
    n_exp = rng.choice([2.5, 4.0, 5.0, 8.0])
    photons_per_sec = n_exp * 1e14
    # Assume 100% quantum efficiency
    current_a = photons_per_sec * QE
    current_ua = current_a * 1e6

    prompt = (
        f"In a vacuum photocell, light of frequency above the threshold frequency causes ${_fmt_sci(photons_per_sec)}$ "
        "photons to strike the emitter cathode every second. "
        "Assume that every incident photon ejects exactly one photoelectron and that all photoelectrons are collected by the anode.\n\n"
        "1. Calculate the rate at which charge is transferred to the collector anode in Coulombs per second.\n"
        "2. State the saturation photocurrent ($I_{{\\text{{sat}}}}$) in microamperes ($\\mu\\text{{A}}$)."
    )
    ans = f"Charge rate $= {_fmt_sci(current_a)}\\text{{ C}}\\cdot\\text{{s}}^{{-1}}$, $I_{{\\text{{sat}}}} = {_fmt_sa(current_ua)}\\text{{ }}\\mu\\text{{A}}$"
    steps = [
        {"rule": "Calculate total charge emitted per second (current)", "op": f"I = n_e e = ({_fmt_sci(photons_per_sec)})(1{{,}}6 \\times 10^{{-19}})", "to": f"{_fmt_sci(current_a)}\\text{{ A}}"},
        {"rule": "Convert amperes to microamperes", "op": f"I_{{\\mu\\text{{A}}}} = {_fmt_sci(current_a)} \\times 10^6", "to": f"{_fmt_sa(current_ua)}\\text{{ }}\\mu\\text{{A}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Electric current is rate of flow of charge: I = Q / t = n_e * e.",
        t2=f"I = ({_fmt_sci(photons_per_sec)}) * (1,6 x 10^-19 C) = {_fmt_sci(current_a)} A.",
        t3=f"I_sat = {_fmt_sa(current_ua)} μA.",
        misconceptions=["confusing_photons_per_second_directly_with_amperes_without_multiplying_by_e"],
        marks=4,
    )


def _build_28(rng: random.Random) -> Dict[str, Any]:
    sub = "28_quantum_efficiency_calculation"
    p_mw = rng.choice([2.0, 4.0, 5.0])
    wlen_nm = 400
    p_w = p_mw * 1e-3
    e_photon = (H * C) / (wlen_nm * 1e-9)
    n_photons = p_w / e_photon
    # Quantum efficiency 10% to 25%
    eta_pct = rng.choice([10.0, 15.0, 20.0, 25.0])
    n_electrons = n_photons * (eta_pct / 100.0)
    i_sat_ua = round((n_electrons * QE) * 1e6, 2)

    prompt = (
        f"A light beam of wavelength $400\\text{{ nm}}$ and power ${_fmt_sa(p_mw)}\\text{{ mW}}$ is directed at a photocell cathode.\n"
        f"The resulting saturation photocurrent measured in the external circuit is ${_fmt_sa(i_sat_ua)}\\text{{ }}\\mu\\text{{A}}$.\n\n"
        "1. Calculate the number of incident photons striking the cathode per second.\n"
        "2. Calculate the number of photoelectrons emitted per second.\n"
        "3. Calculate the quantum efficiency ($\\eta$) of the photocell (the percentage of photons that eject an electron)."
    )
    ans = f"$N_{{\\text{{photons}}}} = {_fmt_sci(n_photons)}\\text{{ s}}^{{-1}}$, $n_e = {_fmt_sci(n_electrons)}\\text{{ s}}^{{-1}}$, $\\eta = {_fmt_sa(eta_pct)}\\%$"
    steps = [
        {"rule": "Calculate photon arrival rate from power", "op": f"N = \\frac{{P}}{{hc/\\lambda}} = \\frac{{{_fmt_sci(p_w)}}}{{{_fmt_sci(e_photon)}}}", "to": f"{_fmt_sci(n_photons)}\\text{{ photons/s}}"},
        {"rule": "Calculate photoelectron emission rate from saturation current", "op": f"n_e = \\frac{{I}}{{e}} = \\frac{{{_fmt_sa(i_sat_ua)} \\times 10^{{-6}}}}{{1{{,}}6 \\times 10^{{-19}}}}", "to": f"{_fmt_sci(n_electrons)}\\text{{ electrons/s}}"},
        {"rule": "Calculate quantum efficiency percentage", "op": f"\\eta = \\frac{{n_e}}{{N}} \\times 100\\% = \\frac{{{_fmt_sci(n_electrons)}}}{{{_fmt_sci(n_photons)}}} \\times 100\\%", "to": f"{_fmt_sa(eta_pct)}\\%"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Quantum efficiency is the fraction of incident photons that successfully liberate a photoelectron: η = (n_e / N_photons) * 100%.",
        t2=f"n_e = I / e, and N_photons = P / E_photon.",
        t3=f"Quantum efficiency = {_fmt_sa(eta_pct)}%.",
        misconceptions=["assuming_all_photons_eject_electrons_under_real_experimental_conditions"],
        marks=5,
    )


def _build_29(rng: random.Random) -> Dict[str, Any]:
    sub = "29_photocurrent_vs_incident_light_intensity"
    i1 = rng.choice([15.0, 20.0, 25.0])
    factor = rng.choice([2, 3])
    i2 = i1 * factor

    prompt = (
        "In an investigation of the photoelectric effect, monochromatic light of constant frequency $f > f_0$ shines on a photocell.\n"
        f"At an initial intensity $L_1$, the saturation photocurrent is measured as ${_fmt_sa(i1)}\\text{{ }}\\mu\\text{{A}}$.\n\n"
        f"When the intensity is increased to $L_2 = {_fmt_sa(factor)} L_1$:\n"
        "1. State the relationship between saturation photocurrent and light intensity for light of constant frequency.\n"
        f"2. Calculate the new saturation photocurrent in $\\mu\\text{{A}}$."
    )
    ans = f"Directly proportional ($I_{{\\text{{sat}}}} \\propto \\text{{Intensity}}$); New photocurrent $= {_fmt_sa(i2)}\\text{{ }}\\mu\\text{{A}}$"
    steps = [
        {"rule": "State direct proportionality between photocurrent and intensity", "op": "I_{{\\text{{sat}}}} \\propto \\text{{Intensity (for constant }} f)", "to": "\\text{Linear direct proportionality through origin}"},
        {"rule": "Calculate scaled photocurrent", "op": f"I_2 = {_fmt_sa(factor)} \\times I_1 = {_fmt_sa(factor)} \\times {_fmt_sa(i1)}", "to": f"{_fmt_sa(i2)}\\text{{ }}\\mu\\text{{A}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="For radiation of frequency above threshold, doubling the light intensity doubles the photon flux, which doubles the photocurrent.",
        t2=f"I2 = {factor} * I1 = {_fmt_sa(i2)} μA.",
        t3=f"Directly proportional; I = {_fmt_sa(i2)} μA.",
        misconceptions=["believing_current_increases_exponentially_with_intensity"],
        marks=4,
    )


def _build_30(rng: random.Random) -> Dict[str, Any]:
    sub = "30_photocurrent_vs_potential_difference_curve"
    v_stop = rng.choice([1.4, 1.8, 2.2, 2.5])
    i_sat = rng.choice([20.0, 30.0, 40.0])
    svg_str = _svg_iv_curves(v_stop, i_sat, i_sat * 2)

    prompt = (
        "Refer to the accompanying vector graph showing the photocurrent ($I$) versus potential difference ($V$) "
        "characteristic curves for a photocell at two different light intensities (Intensity 1 and Intensity 2).\n\n"
        f"For Intensity 1, the saturation current is ${_fmt_sa(i_sat)}\\text{{ }}\\mu\\text{{A}}$, and the stopping potential is $-{_fmt_sa(v_stop)}\\text{{ V}}$.\n\n"
        "1. Identify the feature of the curve that gives the stopping potential ($V_{{\\text{{stop}}}}$).\n"
        "2. Explain why the photocurrent levels off to a constant value ($I_{{\\text{{sat}}}}$) when the forward potential difference is made large and positive.\n"
        "3. Calculate the maximum kinetic energy of the photoelectrons in electron-volts ($\\text{{eV}}$)."
    )
    ans = f"Stopping potential is the negative voltage where current drops to zero ($-{_fmt_sa(v_stop)}\\text{{ V}}$); Saturation occurs because all emitted electrons are being collected; $K_{{\\max}} = {_fmt_sa(v_stop)}\\text{{ eV}}$"
    steps = [
        {"rule": "Identify stopping potential on horizontal axis", "op": "I(V) = 0 \\implies V = -V_{{\\text{{stop}}}}", "to": f"V_{{\\text{{stop}}}} = {_fmt_sa(v_stop)}\\text{{ V}}"},
        {"rule": "Explain saturation photocurrent physically", "op": "\\text{{Collection rate = emission rate}}", "to": "\\text{{All photoelectrons emitted per second are collected by the anode}}"},
        {"rule": "State maximum kinetic energy in eV", "op": f"K_{{\\max}} = e V_{{\\text{{stop}}}} = {_fmt_sa(v_stop)}\\text{{ eV}}", "to": f"{_fmt_sa(v_stop)}\\text{{ eV}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Photocurrent vs Potential Difference (I-V) Curves"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The point where the I-V curve intercepts the negative voltage axis is the stopping potential -V_stop.",
        t2="Increasing positive anode voltage cannot extract more electrons than are emitted by the photons, producing the flat plateau I_sat.",
        t3=f"V_stop = {_fmt_sa(v_stop)} V, K_max = {_fmt_sa(v_stop)} eV.",
        misconceptions=["thinking_photocurrent_keeps_rising_indefinitely_with_voltage"],
        marks=5,
        diagram_spec=d_spec,
    )


def _build_31(rng: random.Random) -> Dict[str, Any]:
    sub = "31_effect_of_doubling_intensity_on_iv_curve"
    v_stop = rng.choice([1.5, 2.0, 2.4])
    i1 = rng.choice([25.0, 30.0])
    i2 = i1 * 2
    svg_str = _svg_iv_curves(v_stop, i1, i2)

    prompt = (
        "Refer to the accompanying vector graph displaying the $I\\text{–}V$ curves for a photocell illuminated by "
        "monochromatic light of constant frequency at two different intensities ($L_1$ and $L_2 = 2 L_1$).\n\n"
        "1. Explain why both curves cross the voltage axis at the exact same stopping potential ($-V_{{\\text{{stop}}}}$).\n"
        "2. Explain why the saturation photocurrent for Intensity 2 is exactly double that for Intensity 1."
    )
    ans = "1. Stopping potential depends only on frequency and work function ($e V_{\\text{stop}} = hf - W_0$), which are unchanged; 2. Doubling intensity doubles the number of photons per second, doubling the number of photoelectrons emitted per second ($I_{\\text{sat}} \\propto \\text{Intensity}$)."
    steps = [
        {"rule": "Explain common stopping potential", "op": "e V_{{\\text{{stop}}}} = hf - W_0", "to": "\\text{{Frequency and metal are identical, so stopping potential is identical}}"},
        {"rule": "Explain doubled saturation current", "op": "I_{{\\text{{sat}}}} \\propto \\text{{Photon flux}} \\propto \\text{{Intensity}}", "to": "\\text{{Twice as many photons per second liberate twice as many photoelectrons}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Effect of Doubling Intensity on I-V Characteristic"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Changing intensity alters the height of the curve (saturation current) but does NOT shift the stopping potential horizontally.",
        t2="Stopping potential depends strictly on frequency f, which was held constant.",
        t3="Same stopping potential because frequency is constant; doubled current because photon flux doubled.",
        misconceptions=["believing_higher_intensity_shifts_stopping_potential_to_the_left"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_32(rng: random.Random) -> Dict[str, Any]:
    sub = "32_effect_of_increasing_frequency_on_iv_curve"
    prompt = (
        "In a photocell investigation, the frequency of incident radiation is increased from $f_1$ to $f_2$ ($f_2 > f_1$), "
        "while the total beam power (photon arrival rate) is adjusted so that the saturation current remains constant.\n\n"
        "1. State the effect of this frequency increase on the stopping potential ($V_{{\\text{{stop}}}}$). (Choose from *shifts further to the left (more negative)*, *shifts to the right*, or *remains unchanged*).\n"
        "2. Explain your answer using Einstein's photoelectric equation."
    )
    ans = "Shifts further to the left (more negative / greater magnitude); Explanation: Higher frequency photons possess more energy ($E = hf$), producing photoelectrons with greater maximum kinetic energy ($K_{\\max} = hf - W_0$), requiring a larger retarding potential to stop them ($V_{\\text{stop}} = K_{\\max}/e$)."
    steps = [
        {"rule": "State direction of stopping potential shift on I-V graph", "op": "\\text{{Higher frequency effect}}", "to": "\\text{{Shifts further left (more negative)}}"},
        {"rule": "Explain via photoelectric equation", "op": "e V_{{\\text{{stop}}}} = hf - W_0", "to": "\\text{{Higher }} f \\implies \\text{greater } K_{{\\max}} \\implies \\text{larger magnitude of } V_{{\\text{{stop}}}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Higher frequency gives electrons more kinetic energy, so a stronger opposing electric field is required to halt them.",
        t2="V_stop = (hf - W0) / e. As f increases, V_stop increases, so on an I-V graph it intercepts further to the left (more negative).",
        t3="Shifts further to the left (more negative).",
        misconceptions=["confusing_the_graphical_direction_of_stopping_potential_shift"],
        marks=4,
    )


def _build_33(rng: random.Random) -> Dict[str, Any]:
    sub = "33_kinetic_energy_vs_frequency_graph_planck_gradient"
    f0_exp = rng.choice([5.2, 5.5, 6.0])
    w0_j = f0_exp * 1e14 * H
    w0_19 = w0_j * 1e19
    svg_str = _svg_kmax_vs_f(f0_exp, w0_19, "Sodium")

    prompt = (
        "Refer to the accompanying vector graph of maximum kinetic energy ($K_{{\\max}}$) versus incident frequency ($f$) for a metal cathode.\n\n"
        "1. State what physical quantity is represented by the **gradient** (slope) of this graph.\n"
        f"2. Write down the accepted scientific value and unit for this gradient from the physical constants data sheet."
    )
    ans = f"Gradient represents Planck's constant ($h$); Value $= 6{{,}}63 \\times 10^{-34}\\text{{ J}}\\cdot\\text{{s}}$"
    steps = [
        {"rule": "Identify physical meaning of gradient from equation of straight line", "op": "K_{{\\max}} = h f - W_0 \\iff y = m x + c", "to": "\\text{Gradient } m = h \\text{ (Planck's constant)}"},
        {"rule": "State accepted value with correct SI unit", "op": "h = 6{{,}}63 \\times 10^{{-34}}\\text{{ J}}\\cdot\\text{{s}}", "to": "6{,}63 \\times 10^{-34}\\text{ J}\\cdot\\text{s}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "K_max vs Frequency Graph (Planck Gradient)"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Comparing K_max = h*f - W0 with y = mx + c reveals that the slope m is Planck's constant h.",
        t2="Gradient = h = 6,63 x 10^-34 J·s.",
        t3="Gradient = Planck's constant (6,63 x 10^-34 J·s).",
        misconceptions=["stating_the_gradient_is_work_function_instead_of_plancks_constant"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_34(rng: random.Random) -> Dict[str, Any]:
    sub = "34_kinetic_energy_vs_frequency_graph_work_function_intercept"
    f0_exp = rng.choice([5.2, 5.8, 6.5, 7.2])
    w0_j = f0_exp * 1e14 * H
    w0_19 = round(w0_j * 1e19, 2)
    svg_str = _svg_kmax_vs_f(f0_exp, w0_19, "Zinc")

    prompt = (
        "Refer to the accompanying vector graph of maximum kinetic energy ($K_{{\\max}}$) versus frequency ($f$) for a zinc cathode.\n\n"
        "1. State what physical quantity is represented by the horizontal intercept on the frequency axis.\n"
        "2. State what physical quantity is represented by the magnitude of the vertical intercept on the energy axis.\n"
        f"3. Using the values on the graph, state the threshold frequency ($f_0$) and the work function ($W_0$) of the metal."
    )
    ans = f"Horizontal intercept = Threshold frequency ($f_0 = {_fmt_sa(f0_exp)} \\times 10^{{14}}\\text{{ Hz}}$); Vertical intercept magnitude = Work function ($W_0 = {_fmt_sa(w0_19)} \\times 10^{{-19}}\\text{{ J}}$)"
    steps = [
        {"rule": "Identify horizontal intercept as threshold frequency", "op": "K_{{\\max}} = 0 \\implies f = f_0", "to": "\\text{Threshold frequency } f_0"},
        {"rule": "Identify vertical intercept as negative work function", "op": "f = 0 \\implies K_{{\\max}} = -W_0", "to": "\\text{Magnitude of vertical intercept equals work function } W_0"},
        {"rule": "Read values from graph", "op": f"f_0 = {_fmt_sa(f0_exp)} \\times 10^{{14}}\\text{{ Hz}},\\; W_0 = {_fmt_sa(w0_19)} \\times 10^{{-19}}\\text{{ J}}", "to": "Values extracted"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Interpreting Intercepts on K_max vs Frequency Graph"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="When K_max = 0, hf = W0, so the x-intercept is f0. When f = 0, K_max = -W0, so the y-intercept is -W0.",
        t2=f"Threshold frequency = {_fmt_sa(f0_exp)} x 10^14 Hz; Work function = {_fmt_sa(w0_19)} x 10^-19 J.",
        t3=f"f0 = {_fmt_sa(f0_exp)} x 10^14 Hz, W0 = {_fmt_sa(w0_19)} x 10^-19 J.",
        misconceptions=["forgetting_to_read_the_axis_multiplier_powers_of_ten"],
        marks=5,
        diagram_spec=d_spec,
    )


def _build_35(rng: random.Random) -> Dict[str, Any]:
    sub = "35_parallel_kmax_vs_frequency_lines_for_different_metals"
    f0_a = rng.choice([4.8, 5.2, 5.6])
    f0_b = rng.choice([8.0, 8.5, 9.2])
    w0_a = round(f0_a * 1e14 * H * 1e19, 2)
    svg_str = _svg_kmax_vs_f(f0_a, w0_a, "Metal A and Metal B")

    prompt = (
        "Refer to the accompanying vector graph illustrating $K_{{\\max}}$ versus frequency for two different metal cathodes (Metal A and Metal B).\n\n"
        f"The threshold frequency of Metal A is $f_{{0,A}} = {_fmt_sa(f0_a)} \\times 10^{{14}}\\text{{ Hz}}$ and "
        f"for Metal B is $f_{{0,B}} = {_fmt_sa(f0_b)} \\times 10^{{14}}\\text{{ Hz}}$.\n\n"
        "1. Explain why the lines for Metal A and Metal B on this graph are parallel to each other.\n"
        "2. Which metal (A or B) has the larger work function? Give a reason for your answer."
    )
    ans = "1. Both lines have the exact same gradient, which is Planck's constant ($h$), a universal physical constant; 2. Metal B has the larger work function because its threshold frequency is greater ($W_0 = h f_0$ and $f_{0,B} > f_{0,A}$)."
    steps = [
        {"rule": "Explain parallel lines via constant gradient", "op": "\\text{{Gradient of both lines}} = h", "to": "\\text{{Planck's constant is universal, so all metals yield parallel lines}}"},
        {"rule": "Identify metal with larger work function", "op": f"W_0 = h f_0 \\text{{ and }} f_{{0,B}} ({_fmt_sa(f0_b)}) > f_{{0,A}} ({_fmt_sa(f0_a)})", "to": "\\text{{Metal B has the larger work function}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Parallel Lines for Different Metals"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Every metal produces a line with the exact same slope h = 6,63 x 10^-34 J·s, so all lines are parallel.",
        t2="The further to the right the x-intercept f0, the greater the threshold frequency and the larger the work function W0 = h * f0.",
        t3="Parallel because slope is universal Planck's constant h; Metal B has larger work function because f0,B > f0,A.",
        misconceptions=["thinking_different_metals_have_different_slopes"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_36(rng: random.Random) -> Dict[str, Any]:
    sub = "36_stopping_potential_vs_frequency_graph"
    f0_exp = rng.choice([5.0, 5.5, 6.0, 6.8])
    f0_hz = f0_exp * 1e14
    w0_j = f0_hz * H
    slope = H / QE

    prompt = (
        "In a laboratory investigation, a learner plots a graph of stopping potential ($V_{{\\text{{stop}}}}$) on the vertical axis "
        "versus incident frequency ($f$) on the horizontal axis for a photoelectric cell.\n\n"
        "1. State the formula for the gradient of this $V_{{\\text{{stop}}}}$ versus $f$ graph in terms of physical constants.\n"
        f"2. If the horizontal intercept is ${_fmt_sa(f0_exp)} \\times 10^{{14}}\\text{{ Hz}}$, calculate the work function of the cathode in Joules."
    )
    ans = f"Gradient $= \\frac{{h}}{{e}}$; $W_0 = {_fmt_sci(w0_j)}\\text{{ J}}$"
    steps = [
        {"rule": "Derive slope of stopping potential vs frequency graph", "op": "e V_{{\\text{{stop}}}} = hf - W_0 \\implies V_{{\\text{{stop}}}} = \\left(\\frac{{h}}{{e}}\\right) f - \\frac{{W_0}}{{e}}", "to": "\\text{Gradient} = \\frac{h}{e}"},
        {"rule": "Calculate work function from horizontal intercept", "op": f"W_0 = h f_0 = (6{{,}}63 \\times 10^{{-34}})({_fmt_sa(f0_exp)} \\times 10^{{14}})", "to": f"{_fmt_sci(w0_j)}\\text{{ J}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Dividing Einstein's equation by e gives V_stop = (h/e) * f - (W0/e).",
        t2="The gradient of V_stop vs f is h / e. The x-intercept is still the threshold frequency f0.",
        t3=f"Gradient = h / e, W0 = {_fmt_sci(w0_j)} J.",
        misconceptions=["forgetting_to_divide_h_by_e_for_the_stopping_potential_gradient"],
        marks=4,
    )


def _build_37(rng: random.Random) -> Dict[str, Any]:
    sub = "37_continuous_spectrum_definition_and_origin"
    prompt = (
        "Spectroscopy is the study of spectra produced when light interacts with matter.\n\n"
        "1. Define the term **continuous spectrum**.\n"
        "2. Name one light source that produces a continuous spectrum.\n"
        "3. Explain why this light source produces a continuous spectrum rather than discrete lines."
    )
    ans = "1. Continuous spectrum: An emission spectrum that consists of all wavelengths and frequencies of visible light without gaps; 2. An incandescent tungsten bulb filament / hot glowing dense solid; 3. In dense hot solids, atoms are tightly packed together, causing their electron energy levels to overlap into broad continuous energy bands."
    steps = [
        {"rule": "Define continuous spectrum", "op": "\\text{{Definition}}", "to": "\\text{{Spectrum containing all continuous wavelengths of visible light with no dark gaps}}"},
        {"rule": "Identify incandescent source", "op": "\\text{{Hot dense matter}}", "to": "\\text{{Incandescent filament bulb / glowing solid}}"},
        {"rule": "Explain atomic physical origin", "op": "\\text{{Close atomic packing}}", "to": "\\text{{Overlapping energy levels form continuous energy bands}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="A continuous spectrum has no gaps or breaks across the visible range (like a rainbow).",
        t2="Hot, dense glowing solids (like a lightbulb filament) emit continuous spectra because their atoms are tightly packed.",
        t3="Consists of all wavelengths; incandescent bulb; overlapping energy levels.",
        misconceptions=["confusing_a_continuous_spectrum_with_a_line_emission_spectrum"],
        marks=4,
    )


def _build_38(rng: random.Random) -> Dict[str, Any]:
    sub = "38_line_emission_spectrum_definition_and_origin"
    gas_choice = rng.choice([
        ("hydrogen", [434.0, 486.0, 656.0]),
        ("helium", [447.0, 501.0, 587.0, 668.0]),
        ("mercury", [436.0, 546.0, 577.0, 579.0]),
    ])
    gas_name, lines = gas_choice
    svg_str = _svg_spectral_strip(lines, is_emission=True)

    prompt = (
        f"Refer to the accompanying vector diagram illustrating a line emission spectrum for excited {gas_name} gas.\n\n"
        "1. Define the term **line emission spectrum**.\n"
        f"2. Explain how excited low-pressure {gas_name} gas produces a line emission spectrum in terms of electron transitions."
    )
    ans = "1. Line emission spectrum: A spectrum of discrete, separate bright coloured lines on a dark background; 2. When electrons in excited gas atoms drop from higher to lower discrete energy levels, they emit photons of specific, discrete frequencies ($\\Delta E = hf$), producing sharp colored lines."
    steps = [
        {"rule": "State definition of line emission spectrum", "op": "\\text{{Definition}}", "to": "\\text{{Discrete pattern of sharp bright lines on a dark background}}"},
        {"rule": "Explain atomic mechanism of emission", "op": "\\Delta E = E_{{\\text{{high}}}} - E_{{\\text{{low}}}} = hf", "to": "\\text{{Downward electron transitions between discrete energy levels emit photons of specific frequencies}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Line Emission Spectrum"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="A line emission spectrum consists of separate bright colored lines on a dark background.",
        t2="It is produced when excited electrons fall to lower energy levels, releasing energy as photons: ΔE = hf.",
        t3="Bright lines on dark background; emitted when electrons drop to lower energy levels.",
        misconceptions=["thinking_electrons_emit_photons_when_jumping_UP_to_higher_levels"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_39(rng: random.Random) -> Dict[str, Any]:
    sub = "39_line_absorption_spectrum_definition_and_origin"
    gas_choice = rng.choice([
        ("hydrogen", [434.0, 486.0, 656.0]),
        ("sodium", [589.0, 589.6]),
        ("mercury", [436.0, 546.0, 579.0]),
    ])
    gas_name, lines = gas_choice
    svg_str = _svg_spectral_strip(lines, is_emission=False)

    prompt = (
        f"Refer to the accompanying vector diagram illustrating a line absorption spectrum for {gas_name} vapor.\n\n"
        f"White light from an incandescent source is passed through a container of cold, low-pressure {gas_name} gas before entering a spectroscope.\n\n"
        "1. Define the term **line absorption spectrum**.\n"
        "2. Explain how the dark lines in the absorption spectrum are formed."
    )
    ans = "1. Line absorption spectrum: A continuous spectrum crossed by discrete dark lines; 2. Gas atoms absorb specific photon frequencies matching the exact energy differences required to excite electrons to higher energy levels ($\\Delta E = hf$); when these electrons re-emit the photons, they do so in random directions, leaving dark lines in the transmitted beam."
    steps = [
        {"rule": "Define line absorption spectrum", "op": "\\text{{Definition}}", "to": "\\text{{Continuous rainbow spectrum crossed by discrete dark absorption lines}}"},
        {"rule": "Explain atomic absorption mechanism", "op": "\\Delta E = hf", "to": "\\text{{Cool gas atoms absorb specific photon energies to excite electrons; re-emission in all directions creates dark lines}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Line Absorption Spectrum"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="A line absorption spectrum consists of dark lines superimposed on a continuous spectrum.",
        t2="It is formed when cool gas atoms absorb specific photon energies matching electron excitation gaps ΔE = hf.",
        t3="Continuous spectrum with dark lines; formed by absorption of specific frequencies by cool gas atoms.",
        misconceptions=["confusing_absorption_spectra_with_emission_spectra"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_40(rng: random.Random) -> Dict[str, Any]:
    sub = "40_atomic_spectral_fingerprinting"
    prompt = (
        "Astronomers use spectroscopy to identify the chemical composition of distant stars and gas nebulae.\n\n"
        "1. Explain why every chemical element has its own unique, characteristic line emission and absorption spectrum (an \"atomic fingerprint\").\n"
        "2. State whether the wavelengths of the dark absorption lines of a gas correspond exactly to the wavelengths of its bright emission lines."
    )
    ans = "1. Every element has a unique nuclear charge and unique, distinct electron energy level configurations, resulting in a unique set of allowable energy transitions ($\\Delta E$); 2. YES, they correspond exactly, because the energy differences ($\\Delta E$) between the same pair of levels are identical whether absorbing or emitting a photon."
    steps = [
        {"rule": "Explain atomic spectral uniqueness", "op": "\\text{{Unique atomic energy levels}}", "to": "\\text{{Each element has a unique arrangement of discrete electron energy levels}}"},
        {"rule": "Confirm reciprocity of emission and absorption wavelengths", "op": "\\Delta E_{{\\text{{absorb}}}} = \\Delta E_{{\\text{{emit}}}}", "to": "\\text{{Yes, identical wavelengths because identical energy differences are involved}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="No two elements have the same electron energy level spacings, so every element has a unique spectral fingerprint.",
        t2="An atom absorbs and emits the exact same characteristic wavelengths.",
        t3="Unique energy levels; yes, absorption and emission lines occur at identical wavelengths.",
        misconceptions=["believing_absorption_and_emission_occur_at_different_wavelengths_for_the_same_element"],
        marks=4,
    )


def _build_41(rng: random.Random) -> Dict[str, Any]:
    sub = "41_fraunhofer_lines_solar_absorption_spectrum"
    prompt = (
        "When sunlight is dispersed through a high-resolution spectrometer, hundreds of dark lines are observed across the solar spectrum. "
        "These are known as **Fraunhofer lines**.\n\n"
        "1. Identify the type of spectrum formed by Fraunhofer lines. (Continuous, Line Emission, or Line Absorption).\n"
        "2. Explain how Fraunhofer lines are formed in the Sun's atmosphere.\n"
        "3. State how scientists used Fraunhofer lines to discover helium before it was found on Earth."
    )
    ans = "1. Line absorption spectrum; 2. The Sun's dense, hot core emits a continuous spectrum; as this light passes outward through the cooler vaporized gases in the Sun's outer atmosphere (chromosphere), specific wavelengths are absorbed; 3. Spectral lines were observed that did not match any known terrestrial element, proving the existence of a new element (helium, from Greek Helios = Sun)."
    steps = [
        {"rule": "Identify spectrum type", "op": "\\text{{Spectral classification}}", "to": "\\text{{Line absorption spectrum}}"},
        {"rule": "Explain solar mechanism", "op": "\\text{{Hot core continuous emission + cool outer gas absorption}}", "to": "\\text{{Outer atmosphere gases absorb specific frequencies}}"},
        {"rule": "Explain historical discovery of helium", "op": "\\text{{Spectral matching}}", "to": "\\text{{Unmatched spectral absorption lines indicated an unknown element}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Fraunhofer lines are dark absorption lines in the solar spectrum.",
        t2="Cooler gases in the solar atmosphere absorb specific wavelengths from the continuous light emitted by the dense solar interior.",
        t3="Line absorption spectrum; outer gases absorb specific wavelengths; discovered helium.",
        misconceptions=["thinking_fraunhofer_lines_are_caused_by_the_earths_atmosphere_only"],
        marks=5,
    )


def _build_42(rng: random.Random) -> Dict[str, Any]:
    sub = "42_discrete_energy_levels_in_atoms"
    prompt = (
        "Early atomic models viewed electrons as orbiting the nucleus at any continuous distance and energy.\n\n"
        "Explain how the existence of line emission spectra provides conclusive proof that electrons in an atom can only exist in **discrete (quantised) energy levels**."
    )
    ans = "If electrons could have continuous energies, all possible energy changes would occur, producing a continuous rainbow spectrum. Because only discrete, sharp spectral lines are observed, electrons can only transition between fixed, specific energy states, emitting photons of precise frequencies ($\\Delta E = hf$)."
    steps = [
        {"rule": "Contrast continuous vs discrete spectral prediction", "op": "\\text{{Continuous energy levels would predict continuous emission}}", "to": "\\text{{Line spectrum disproves continuous electron energies}}"},
        {"rule": "State quantum inference", "op": "\\Delta E = E_2 - E_1 = hf", "to": "\\text{{Discrete lines prove electrons exist only in quantized energy levels}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="If electron energies were continuous, all frequencies would be emitted, creating a continuous spectrum.",
        t2="The sharp, separate lines prove that electrons can only jump between specific, quantized energy levels.",
        t3="Continuous energy would give a continuous spectrum; discrete lines prove discrete, quantised energy levels.",
        misconceptions=["confusing_discrete_energy_levels_with_continuous_energy_bands"],
        marks=4,
    )


def _build_43(rng: random.Random) -> Dict[str, Any]:
    sub = "43_bohr_energy_level_transition_photon_emission"
    levels = [-13.6, -3.4, -1.51, -0.85]
    transition = rng.choice([(3, 2), (4, 2), (4, 1), (3, 1)])
    n_high, n_low = transition
    e_high = levels[n_high - 1]
    e_low = levels[n_low - 1]
    delta_e_ev = round(e_high - e_low, 2)
    delta_e_j = delta_e_ev * QE
    f_emitted = delta_e_j / H

    svg_str = _svg_bohr_energy_levels(levels, n_high, n_low)

    prompt = (
        "Refer to the accompanying vector diagram displaying discrete electron energy levels for a hydrogen atom.\n\n"
        f"An electron transitions from energy level $n = {n_high}$ ($E_{{{n_high}}} = {_fmt_sa(e_high)}\\text{{ eV}}$) to "
        f"energy level $n = {n_low}$ ($E_{{{n_low}}} = {_fmt_sa(e_low)}\\text{{ eV}}$).\n\n"
        "1. Calculate the energy of the emitted photon in electron-volts ($\\text{{eV}}$).\n"
        "2. Convert this energy to Joules ($\\text{{J}}$).\n"
        "3. Calculate the frequency of the emitted photon in Hertz."
    )
    ans = f"$\\Delta E = {_fmt_sa(delta_e_ev)}\\text{{ eV}}$, $\\Delta E = {_fmt_sci(delta_e_j)}\\text{{ J}}$, $f = {_fmt_sci(f_emitted)}\\text{{ Hz}}$"
    steps = [
        {"rule": "Calculate transition energy difference in eV", "op": f"\\Delta E = E_{n_high} - E_{n_low} = ({_fmt_sa(e_high)}) - ({_fmt_sa(e_low)})", "to": f"{_fmt_sa(delta_e_ev)}\\text{{ eV}}"},
        {"rule": "Convert energy difference to Joules", "op": f"\\Delta E = {_fmt_sa(delta_e_ev)} \\times (1{{,}}6 \\times 10^{{-19}})", "to": f"{_fmt_sci(delta_e_j)}\\text{{ J}}"},
        {"rule": "Calculate frequency of emitted photon", "op": f"f = \\frac{{\\Delta E}}{{h}} = \\frac{{{_fmt_sci(delta_e_j)}}}{{6{{,}}63 \\times 10^{{-34}}}}", "to": f"{_fmt_sci(f_emitted)}\\text{{ Hz}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Bohr Energy Level Transition Diagram"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The energy of the emitted photon equals the difference between the two energy levels: ΔE = E_high - E_low.",
        t2="Convert eV to Joules by multiplying by 1,6 x 10^-19, then use f = ΔE / h.",
        t3=f"ΔE = {_fmt_sa(delta_e_ev)} eV = {_fmt_sci(delta_e_j)} J, f = {_fmt_sci(f_emitted)} Hz.",
        misconceptions=["adding_the_negative_energy_values_incorrectly"],
        marks=5,
        diagram_spec=d_spec,
    )


def _build_44(rng: random.Random) -> Dict[str, Any]:
    sub = "44_bohr_energy_level_transition_wavelength"
    delta_ev = rng.choice([1.89, 2.55, 2.86, 3.03])
    delta_j = delta_ev * QE
    wlen_m = (H * C) / delta_j
    wlen_nm = round(wlen_m * 1e9, 1)

    prompt = (
        f"An electron in an excited atom transitions between two discrete energy levels with an energy difference of "
        f"$\\Delta E = {_fmt_sa(delta_ev)}\\text{{ eV}}$, emitting a single photon.\n\n"
        "1. Calculate the wavelength of the emitted photon in nanometres ($\\text{{nm}}$).\n"
        "2. State whether this radiation lies in the ultraviolet, visible, or infrared region of the electromagnetic spectrum. (Visible light spans $\\approx 400\\text{ nm}$ to $700\\text{ nm}$)."
    )
    region = "visible" if 400 <= wlen_nm <= 700 else ("ultraviolet" if wlen_nm < 400 else "infrared")
    ans = f"$\\lambda = {_fmt_sa(wlen_nm)}\\text{{ nm}}$, Region: {region}"
    steps = [
        {"rule": "Calculate photon wavelength using de Broglie / Planck-Einstein relation", "op": f"\\lambda = \\frac{{hc}}{{\\Delta E}} = \\frac{{(6{{,}}63 \\times 10^{{-34}})(3{{,}}0 \\times 10^8)}}{{{_fmt_sa(delta_ev)} \\times 1{{,}}6 \\times 10^{{-19}}}}", "to": f"{_fmt_sci(wlen_m)}\\text{{ m}} = {_fmt_sa(wlen_nm)}\\text{{ nm}}"},
        {"rule": "Identify electromagnetic spectrum band", "op": f"400\\text{{ nm}} \\le {_fmt_sa(wlen_nm)}\\text{{ nm}} \\le 700\\text{{ nm}}", "to": f"\\text{{{region.capitalize()} spectrum}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="λ = hc / ΔE, where ΔE must be in Joules (multiply eV by 1,6 x 10^-19).",
        t2=f"λ = {_fmt_sa(wlen_nm)} nm.",
        t3=f"λ = {_fmt_sa(wlen_nm)} nm; Region is {region}.",
        misconceptions=["forgetting_to_convert_ev_to_joules_before_calculating_wavelength"],
        marks=4,
    )


def _build_45(rng: random.Random) -> Dict[str, Any]:
    sub = "45_electron_excitation_energy_absorption"
    # Transition from n=1 (-13.6 eV) to n=2 (-3.4 eV) => delta E = 10.2 eV
    e1 = -13.6
    e2 = -3.4
    delta_ev = 10.2
    delta_j = delta_ev * QE
    f_req = delta_j / H

    prompt = (
        f"A hydrogen atom has a ground state energy of $E_1 = {_fmt_sa(e1)}\\text{{ eV}}$ and a first excited state energy of "
        f"$E_2 = {_fmt_sa(e2)}\\text{{ eV}}$.\n\n"
        "1. Calculate the exact photon energy required to excite an electron from the ground state to the first excited state in Joules.\n"
        "2. Explain why a photon with an energy of $11{{,}}0\\text{ eV}$ will NOT be absorbed by this hydrogen atom."
    )
    ans = f"$\\Delta E = {_fmt_sci(delta_j)}\\text{{ J}}$ ($10{{,}}2\\text{{ eV}}$); It will not be absorbed because atomic absorption is an all-or-nothing process: the photon energy must EXACTLY match the difference between discrete levels ($\\Delta E = 10{{,}}2\\text{{ eV}}$); $11{{,}}0\\text{{ eV}}$ does not correspond to any allowed energy transition."
    steps = [
        {"rule": "Calculate excitation energy difference", "op": f"\\Delta E = E_2 - E_1 = ({_fmt_sa(e2)}) - ({_fmt_sa(e1)}) = {_fmt_sa(delta_ev)}\\text{{ eV}}", "to": f"{_fmt_sci(delta_j)}\\text{{ J}}"},
        {"rule": "Explain selective absorption in bound atoms", "op": "\\text{{Quantized all-or-nothing absorption}}", "to": "\\text{{Photon energy must match an exact transition gap}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="An atom cannot absorb 'part' of a photon. The photon energy must match the transition difference ΔE exactly.",
        t2=f"ΔE = 10,2 eV = {_fmt_sci(delta_j)} J. Photons of 11,0 eV cannot be absorbed because 11,0 eV matches no level.",
        t3=f"ΔE = {_fmt_sci(delta_j)} J; not absorbed because it does not match an allowed discrete transition.",
        misconceptions=["thinking_an_atom_can_absorb_an_11_ev_photon_and_keep_10_2_ev_re-emitting_the_rest"],
        marks=4,
    )


def _build_46(rng: random.Random) -> Dict[str, Any]:
    sub = "46_atomic_ionization_energy"
    # Ground state energy e1
    e1_ev = -13.6
    ion_ev = abs(e1_ev)
    ion_j = ion_ev * QE
    f_ion = ion_j / H

    prompt = (
        f"The ground state energy of an electron in a hydrogen atom is $E_1 = {_fmt_sa(e1_ev)}\\text{{ eV}}$, "
        "and the energy at infinity (ionization level) is $E_\\infty = 0\\text{{ eV}}$.\n\n"
        "1. Define the term **ionization energy** of an atom.\n"
        "2. State the ionization energy of hydrogen in electron-volts ($\\text{{eV}}$) and in Joules ($\\text{{J}}$).\n"
        "3. Calculate the minimum frequency of radiation required to ionize a ground-state hydrogen atom."
    )
    ans = f"Ionization energy: The minimum energy needed to remove an electron completely from an atom in its ground state; $E_{{\\text{{ion}}}} = {_fmt_sa(ion_ev)}\\text{{ eV}} = {_fmt_sci(ion_j)}\\text{{ J}}$; $f = {_fmt_sci(f_ion)}\\text{{ Hz}}$"
    steps = [
        {"rule": "State definition of ionization energy", "op": "\\text{{Definition}}", "to": "\\text{{Minimum energy required to completely remove an electron from the ground state}}"},
        {"rule": "State ionization energy in eV and Joules", "op": f"E_{{\\text{{ion}}}} = 0 - ({_fmt_sa(e1_ev)}) = {_fmt_sa(ion_ev)}\\text{{ eV}}", "to": f"{_fmt_sci(ion_j)}\\text{{ J}}"},
        {"rule": "Calculate minimum ionization frequency", "op": f"f = \\frac{{E_{{\\text{{ion}}}}}}{{h}} = \\frac{{{_fmt_sci(ion_j)}}}{{6{{,}}63 \\times 10^{{-34}}}}", "to": f"{_fmt_sci(f_ion)}\\text{{ Hz}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Ionization energy is the energy needed to take an electron from n=1 to n=infinity (E_infinity = 0 eV).",
        t2=f"E_ion = +13,6 eV = 13,6 * 1,6 x 10^-19 J = {_fmt_sci(ion_j)} J.",
        t3=f"E_ion = {_fmt_sa(ion_ev)} eV = {_fmt_sci(ion_j)} J, f = {_fmt_sci(f_ion)} Hz.",
        misconceptions=["stating_ionization_energy_as_a_negative_value"],
        marks=5,
    )


def _build_47(rng: random.Random) -> Dict[str, Any]:
    sub = "47_hydrogen_emission_series_balmer_lyman_paschen"
    prompt = (
        "The spectral lines of atomic hydrogen are grouped into distinct series depending on the lower energy level involved in the transition.\n\n"
        "1. Name the spectral series of hydrogen that produces lines in the **visible** region of the spectrum, and state the principal quantum number ($n$) of the lower level for this series.\n"
        "2. Name the spectral series that corresponds to transitions ending at $n = 1$, and state the region of the electromagnetic spectrum in which these lines appear.\n"
        "3. Name the spectral series that corresponds to transitions ending at $n = 3$."
    )
    ans = "1. Balmer series, lower level $n = 2$; 2. Lyman series, Ultraviolet (UV) region; 3. Paschen series (Infrared region)"
    steps = [
        {"rule": "Identify visible hydrogen spectral series", "op": "\\text{{Visible transitions}}", "to": "\\text{{Balmer series, lower level }} n = 2"},
        {"rule": "Identify ground state transitions", "op": "\\text{{Transitions to }} n = 1", "to": "\\text{{Lyman series, Ultraviolet region}}"},
        {"rule": "Identify infrared transitions", "op": "\\text{{Transitions to }} n = 3", "to": "\\text{{Paschen series, Infrared region}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Transitions ending at n=1 are Lyman (UV); transitions ending at n=2 are Balmer (Visible); transitions ending at n=3 are Paschen (Infrared).",
        t2="Balmer series is the only series in the visible spectrum.",
        t3="Balmer (n=2, visible); Lyman (n=1, UV); Paschen (n=3, IR).",
        misconceptions=["confusing_lyman_and_balmer_series_levels"],
        marks=4,
    )


def _build_48(rng: random.Random) -> Dict[str, Any]:
    sub = "48_wave_particle_duality_of_light"
    prompt = (
        "Light exhibits both wave-like and particle-like properties under different experimental conditions. "
        "This concept is known as the **wave–particle duality of light**.\n\n"
        "1. Name two optical phenomena that provide evidence that light behaves as a **wave**.\n"
        "2. Name two optical phenomena that provide evidence that light behaves as a stream of **particles (photons)**.\n"
        "3. Summarize the modern consensus regarding the dual nature of light."
    )
    ans = "1. Wave evidence: Interference, diffraction, and polarization; 2. Particle evidence: Photoelectric effect and emission/absorption line spectra; 3. Light propagates through space like a wave (producing interference/diffraction), but exchanges energy with matter in discrete, localized particle-like packets called photons."
    steps = [
        {"rule": "State wave phenomena", "op": "\\text{{Wave behavior}}", "to": "\\text{{Interference, diffraction, polarization}}"},
        {"rule": "State particulate phenomena", "op": "\\text{{Particle behavior}}", "to": "\\text{{Photoelectric effect, line spectra, Compton scattering}}"},
        {"rule": "State unified dual description", "op": "\\text{{Duality synthesis}}", "to": "\\text{{Propagates as wave, interacts with matter as particles (photons)}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Wave properties: interference, diffraction, polarization. Particle properties: photoelectric effect, line spectra.",
        t2="Light travels as a wave but interacts with matter as discrete photon packets.",
        t3="Wave: diffraction/interference; Particle: photoelectric effect/line spectra.",
        misconceptions=["believing_light_changes_physically_between_a_wave_and_a_particle_rather_than_exhibiting_dual_properties"],
        marks=5,
    )


def _build_49(rng: random.Random) -> Dict[str, Any]:
    sub = "49_skills_for_science_plancks_constant_uncertainty"
    # Experimental slope of V_stop vs f
    h_accepted = 6.63e-34
    h_exp = rng.choice([6.45e-34, 6.55e-34, 6.75e-34, 6.82e-34])
    slope_exp = h_exp / QE
    pct_err = round((abs(h_exp - h_accepted) / h_accepted) * 100.0, 2)

    prompt = (
        "In a laboratory investigation, learners measure the stopping potential ($V_{{\\text{{stop}}}}$) at different frequencies ($f$) "
        "and determine the gradient of the resulting $V_{{\\text{{stop}}}}$ versus $f$ graph to be "
        f"**${_fmt_sci(slope_exp)}\\text{{ V}}\\cdot\\text{{s}}$**.\n\n"
        "1. Using this gradient and the elementary charge ($e = 1{{,}}6 \\times 10^{-19}\\text{{ C}}$), calculate the experimental value of Planck's constant ($h_{{\\text{{exp}}}}$).\n"
        "2. Calculate the percentage error of this experimental result relative to the accepted value ($6{{,}}63 \\times 10^{-34}\\text{{ J}}\\cdot\\text{{s}}$)."
    )
    ans = f"$h_{{\\text{{exp}}}} = {_fmt_sci(h_exp)}\\text{{ J}}\\cdot\\text{{s}}$, Percentage error $= {_fmt_sa(pct_err)}\\%$"
    steps = [
        {"rule": "Calculate experimental Planck constant from gradient", "op": f"h_{{\\text{{exp}}}} = \\text{{gradient}} \\times e = ({_fmt_sci(slope_exp)})(1{{,}}6 \\times 10^{{-19}})", "to": f"{_fmt_sci(h_exp)}\\text{{ J}}\\cdot\\text{{s}}"},
        {"rule": "Calculate percentage error", "op": f"\\%_{{\\text{{error}}}} = \\frac{{|h_{{\\text{{exp}}}} - h_{{\\text{{accepted}}}}|}}{{h_{{\\text{{accepted}}}}}} \\times 100\\% = \\frac{{|{_fmt_sci(h_exp)} - 6{{,}}63 \\times 10^{{-34}}|}}{{6{{,}}63 \\times 10^{{-34}}}} \\times 100\\%", "to": f"{_fmt_sa(pct_err)}\\%"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Since gradient = h / e, experimental h = gradient * e.",
        t2=f"h_exp = ({_fmt_sci(slope_exp)}) * (1,6 x 10^-19) = {_fmt_sci(h_exp)} J·s.",
        t3=f"h_exp = {_fmt_sci(h_exp)} J·s, percentage error = {_fmt_sa(pct_err)}%.",
        misconceptions=["dividing_gradient_by_e_instead_of_multiplying"],
        marks=4,
    )


def _build_50(rng: random.Random) -> Dict[str, Any]:
    sub = "50_photoelectric_and_spectra_diagnostic_synthesis"
    wlen_nm = rng.choice([240, 260, 280, 300])
    wlen_m = wlen_nm * 1e-9
    w0_j = 3.68e-19  # Potassium
    f0 = w0_j / H
    e_photon = (H * C) / wlen_m
    k_max = e_photon - w0_j
    v_max = math.sqrt((2 * k_max) / ME)
    v_stop = round(k_max / QE, 2)

    prompt = (
        "**Comprehensive Diagnostic Synthesis: Optical Phenomena & Photoelectric Effect**\n\n"
        f"A beam of monochromatic ultraviolet radiation of wavelength ${_fmt_sa(wlen_nm)}\\text{{ nm}}$ is incident on a clean potassium cathode "
        f"($W_0 = 3{{,}}68 \\times 10^{{-19}}\\text{{ J}}$) inside a vacuum photocell connected in a circuit with a variable retarding power supply.\n\n"
        "1. Define the term *work function*.\n"
        "2. Calculate the threshold frequency ($f_0$) of potassium.\n"
        "3. Calculate the maximum kinetic energy ($K_{{\\max}}$) of the emitted photoelectrons in Joules.\n"
        "4. Calculate the maximum speed ($v_{{\\max}}$) of the emitted photoelectrons.\n"
        "5. Calculate the stopping potential ($V_{{\\text{{stop}}}}$) required to reduce the photocurrent to zero.\n"
        "6. State the effect on $K_{{\\max}}$ and on the saturation photocurrent if the intensity of the UV beam is doubled while keeping the wavelength constant."
    )
    ans = (
        f"Work function: Minimum energy required to emit an electron; $f_0 = {_fmt_sci(f0)}\\text{{ Hz}}$, "
        f"$K_{{\\max}} = {_fmt_sci(k_max)}\\text{{ J}}$, $v_{{\\max}} = {_fmt_sci(v_max)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, "
        f"$V_{{\\text{{stop}}}} = {_fmt_sa(v_stop)}\\text{{ V}}$; $K_{{\\max}}$ remains unchanged, saturation photocurrent doubles"
    )
    steps = [
        {"rule": "Define work function", "op": "\\text{{Definition}}", "to": "\\text{{Minimum energy needed to eject an electron from a metal surface}}"},
        {"rule": "Calculate threshold frequency", "op": f"f_0 = \\frac{{W_0}}{{h}} = \\frac{{3{{,}}68 \\times 10^{{-19}}}}{{6{{,}}63 \\times 10^{{-34}}}}", "to": f"{_fmt_sci(f0)}\\text{{ Hz}}"},
        {"rule": "Calculate photon energy and maximum kinetic energy", "op": f"K_{{\\max}} = \\frac{{hc}}{{\\lambda}} - W_0 = {_fmt_sci(e_photon)} - 3{{,}}68 \\times 10^{{-19}}", "to": f"{_fmt_sci(k_max)}\\text{{ J}}"},
        {"rule": "Calculate maximum photoelectron speed", "op": f"v_{{\\max}} = \\sqrt{{\\frac{{2 K_{{\\max}}}}{{m_e}}}} = \\sqrt{{\\frac{{2({_fmt_sci(k_max)})}}{{9{{,}}11 \\times 10^{{-31}}}}}}", "to": f"{_fmt_sci(v_max)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Calculate stopping potential", "op": f"V_{{\\text{{stop}}}} = \\frac{{K_{{\\max}}}}{{e}} = \\frac{{{_fmt_sci(k_max)}}}{{1{{,}}6 \\times 10^{{-19}}}}", "to": f"{_fmt_sa(v_stop)}\\text{{ V}}"},
        {"rule": "State effects of doubling intensity", "op": "\\text{{Effect of intensity}}", "to": "\\text{K_max remains unchanged; saturation photocurrent doubles}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Solve sequentially: (1) f0 = W0/h, (2) E = hc/λ, (3) K_max = E - W0, (4) v_max = sqrt(2 K_max / m_e), (5) V_stop = K_max / e.",
        t2="Intensity changes only the rate of electron emission (current), never individual electron energies.",
        t3=f"f0 = {_fmt_sci(f0)} Hz, K_max = {_fmt_sci(k_max)} J, v_max = {_fmt_sci(v_max)} m/s, V_stop = {_fmt_sa(v_stop)} V.",
        misconceptions=["confusing_intensity_effects_with_frequency_effects"],
        marks=8,
    )


# =========================================================================== #
# Export Mapping
# =========================================================================== #

BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_photon_arrival_rate_from_beam_power": _build_26,
    "27_saturation_photocurrent_calculation": _build_27,
    "28_quantum_efficiency_calculation": _build_28,
    "29_photocurrent_vs_incident_light_intensity": _build_29,
    "30_photocurrent_vs_potential_difference_curve": _build_30,
    "31_effect_of_doubling_intensity_on_iv_curve": _build_31,
    "32_effect_of_increasing_frequency_on_iv_curve": _build_32,
    "33_kinetic_energy_vs_frequency_graph_planck_gradient": _build_33,
    "34_kinetic_energy_vs_frequency_graph_work_function_intercept": _build_34,
    "35_parallel_kmax_vs_frequency_lines_for_different_metals": _build_35,
    "36_stopping_potential_vs_frequency_graph": _build_36,
    "37_continuous_spectrum_definition_and_origin": _build_37,
    "38_line_emission_spectrum_definition_and_origin": _build_38,
    "39_line_absorption_spectrum_definition_and_origin": _build_39,
    "40_atomic_spectral_fingerprinting": _build_40,
    "41_fraunhofer_lines_solar_absorption_spectrum": _build_41,
    "42_discrete_energy_levels_in_atoms": _build_42,
    "43_bohr_energy_level_transition_photon_emission": _build_43,
    "44_bohr_energy_level_transition_wavelength": _build_44,
    "45_electron_excitation_energy_absorption": _build_45,
    "46_atomic_ionization_energy": _build_46,
    "47_hydrogen_emission_series_balmer_lyman_paschen": _build_47,
    "48_wave_particle_duality_of_light": _build_48,
    "49_skills_for_science_plancks_constant_uncertainty": _build_49,
    "50_photoelectric_and_spectra_diagnostic_synthesis": _build_50,
}

SUBSKILLS_26_50: List[str] = list(BUILDERS_26_50.keys())
