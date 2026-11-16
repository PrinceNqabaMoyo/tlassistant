"""
ps10_waves_sound_light_archetypes_26_50.py
-----------------------------------------
Grades 10 Physical Sciences - Waves, Sound and Light (Subskills 26–50).
Subskills covered:
  26. 26_longitudinal_wave_definition_and_particle_motion
  27. 27_compressions_and_rarefactions_identification
  28. 28_longitudinal_wavelength_measurement
  29. 29_longitudinal_wave_equation_calculations
  30. 30_transverse_vs_longitudinal_wave_comparison
  31. 31_sound_wave_nature_and_medium_requirement
  32. 32_speed_of_sound_in_different_media
  33. 33_pitch_and_frequency_relationship
  34. 34_loudness_and_amplitude_relationship
  35. 35_sound_quality_timbre_and_waveform
  36. 36_human_audible_frequency_range_and_infrasound
  37. 37_echo_distance_and_reflection_time
  38. 38_speed_of_sound_determination_via_echo
  39. 39_marine_sonar_depth_sounding_calculation
  40. 40_medical_ultrasound_sonography_principles
  41. 41_industrial_ultrasound_flaw_detection
  42. 42_bat_echolocation_obstacle_avoidance
  43. 43_electromagnetic_radiation_wave_model_and_speed
  44. 44_electromagnetic_wave_equation_calculations
  45. 45_electromagnetic_spectrum_frequency_and_wavelength_ordering
  46. 46_electromagnetic_spectrum_applications
  47. 47_penetrating_ability_and_ionising_radiation_hazards
  48. 48_photon_energy_calculation_from_frequency
  49. 49_photon_energy_calculation_from_wavelength
  50. 50_waves_sound_light_diagnostic_synthesis

All generators are 100% deterministic (random.Random(seed)), zero-LLM,
adhering strictly to South African comma decimal convention and 6-pillar contract.
"""

import math
import random
from typing import Any, Callable, Dict, List, Optional


TERM = 1
CAPS_WEIGHT = 15
SUGGESTED_DURATION = 4
TOPIC_ID = "waves_sound_light"
LEARNING_OBJECTIVE = "PS10.WSL"


def _fmt_sa(val: float, decimals: int = 2) -> str:
    """Format float with South African comma decimal notation."""
    if abs(val - round(val)) < 1e-9:
        return str(int(round(val)))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _fmt_sci(val: float, decimals: int = 2) -> str:
    """Format a scientific notation number using SA comma and 10^n notation."""
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
    """Helper to enforce universal 6-pillar generator contract."""
    worked = "\n".join(f"{s.get('rule', '')}: ${s.get('op', '')} \\implies {s.get('to', '')}$" for s in sol_steps)
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
# SVG Diagram Generators
# =========================================================================== #

def _svg_longitudinal_slinky(
    wlen_m: float,
    num_compressions: int = 3,
) -> str:
    """Generate inline SVG showing slinky with compressions and rarefactions."""
    w, h = 480, 200
    y_mid = 95
    coil_h = 32

    # We build coils along x: regions of compression (close coils) and rarefaction (spaced coils)
    coils_svg = []
    x = 40.0
    c_centers = []
    r_centers = []

    for c in range(num_compressions):
        # Compression region (tight loops)
        c_start = x
        for _ in range(7):
            coils_svg.append(f'<path d="M {x:.1f} {y_mid - coil_h} C {x+6:.1f} {y_mid - coil_h - 10}, {x+6:.1f} {y_mid + coil_h + 10}, {x:.1f} {y_mid + coil_h}" stroke="#0284c7" stroke-width="2.2" fill="none"/>')
            x += 6.5
        c_centers.append((c_start + x) / 2.0)

        if c < num_compressions - 1:
            # Rarefaction region (spread loops)
            r_start = x
            for _ in range(5):
                coils_svg.append(f'<path d="M {x:.1f} {y_mid - coil_h} C {x+12:.1f} {y_mid - coil_h - 10}, {x+12:.1f} {y_mid + coil_h + 10}, {x:.1f} {y_mid + coil_h}" stroke="#38bdf8" stroke-width="1.8" fill="none"/>')
                x += 16.0
            r_centers.append((r_start + x) / 2.0)

    # Wavelength dimension line between C1 and C2
    c1_x = c_centers[0]
    c2_x = c_centers[1]
    dim_y = 155

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .dim { stroke: #dc2626; stroke-width: 1.5; }',
        '  </style>',
        "".join(coils_svg),
        # Labels for Compression and Rarefaction
        f'  <text x="{c_centers[0]:.1f}" y="40" class="lbl" fill="#0284c7" text-anchor="middle">Compression</text>',
        f'  <line x1="{c_centers[0]:.1f}" y1="44" x2="{c_centers[0]:.1f}" y2="58" stroke="#0284c7" stroke-width="1.2" />',
        f'  <text x="{r_centers[0]:.1f}" y="40" class="lbl" fill="#0284c7" text-anchor="middle">Rarefaction</text>',
        f'  <line x1="{r_centers[0]:.1f}" y1="44" x2="{r_centers[0]:.1f}" y2="58" stroke="#0284c7" stroke-width="1.2" />',
        # Dimension line for wavelength lambda
        f'  <line x1="{c1_x:.1f}" y1="{dim_y}" x2="{c2_x:.1f}" y2="{dim_y}" class="dim" />',
        f'  <line x1="{c1_x:.1f}" y1="{dim_y - 8}" x2="{c1_x:.1f}" y2="{dim_y + 8}" class="dim" />',
        f'  <line x1="{c2_x:.1f}" y1="{dim_y - 8}" x2="{c2_x:.1f}" y2="{dim_y + 8}" class="dim" />',
        f'  <text x="{(c1_x + c2_x)/2.0:.1f}" y="{dim_y + 18}" class="lbl" fill="#dc2626" text-anchor="middle">λ = {_fmt_sa(wlen_m)} m</text>',
        '</svg>',
    ]
    return "\n".join(svg)


def _svg_sound_waveforms(amp: float, f1: float) -> str:
    """Generate inline SVG showing two waveforms of same frequency/amplitude but different timbre."""
    w, h = 480, 220
    ox = 40
    plot_w = 400.0
    y1_mid = 65
    y2_mid = 160
    scale_y = 20.0 + amp * 5.0

    pts1 = []
    pts2 = []
    steps = 120
    cycles = 3.0
    for i in range(steps + 1):
        frac = i / steps
        px = ox + frac * plot_w
        theta = 2 * math.pi * cycles * frac
        # Waveform 1: pure sine wave (tuning fork / flute)
        val1 = math.sin(theta)
        py1 = y1_mid - val1 * scale_y
        pts1.append(f"{px:.1f},{py1:.1f}")

        # Waveform 2: rich complex wave with 2nd and 3rd harmonics (guitar / violin)
        val2 = 0.7 * math.sin(theta) + 0.35 * math.sin(2 * theta) + 0.15 * math.sin(3 * theta)
        py2 = y2_mid - val2 * scale_y
        pts2.append(f"{px:.1f},{py2:.1f}")

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .axis { stroke: #94a3b8; stroke-width: 1; stroke-dasharray: 4,4; }',
        '    .w1 { stroke: #2563eb; stroke-width: 2.2; fill: none; }',
        '    .w2 { stroke: #7c3aed; stroke-width: 2.2; fill: none; }',
        '  </style>',
        # Graph 1
        f'  <line x1="{ox}" y1="{y1_mid}" x2="{ox + plot_w}" y2="{y1_mid}" class="axis" />',
        f'  <polyline points="{" ".join(pts1)}" class="w1" />',
        f'  <text x="{ox}" y="22" class="lbl" fill="#2563eb">Instrument A (Tuning fork - Pure tone at {_fmt_sa(f1)} Hz)</text>',
        # Graph 2
        f'  <line x1="{ox}" y1="{y2_mid}" x2="{ox + plot_w}" y2="{y2_mid}" class="axis" />',
        f'  <polyline points="{" ".join(pts2)}" class="w2" />',
        f'  <text x="{ox}" y="118" class="lbl" fill="#7c3aed">Instrument B (Guitar - Complex harmonics at {_fmt_sa(f1)} Hz)</text>',
        '</svg>',
    ]
    return "\n".join(svg)


def _svg_echo_reflection(distance_m: float, time_s: float) -> str:
    """Generate inline SVG showing sound pulse emitted, reflected off cliff, and returned."""
    w, h = 480, 200
    cliff_x = 420
    source_x = 70
    ground_y = 160

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .ground { stroke: #334155; stroke-width: 2; }',
        '    .cliff { fill: #64748b; stroke: #334155; stroke-width: 2; }',
        '    .fwd { stroke: #0284c7; stroke-width: 2; fill: none; }',
        '    .ret { stroke: #dc2626; stroke-width: 2; stroke-dasharray: 4,4; fill: none; }',
        '    .dim { stroke: #0f172a; stroke-width: 1.2; }',
        '  </style>',
        # Ground
        f'  <line x1="20" y1="{ground_y}" x2="{w - 20}" y2="{ground_y}" class="ground" />',
        # Cliff / wall
        f'  <rect x="{cliff_x}" y="30" width="40" height="{ground_y - 30}" class="cliff" />',
        f'  <text x="{cliff_x + 20}" y="22" class="lbl" text-anchor="middle">Reflecting Cliff</text>',
        # Sound source / observer
        f'  <circle cx="{source_x}" cy="{ground_y - 35}" r="8" fill="#0284c7" />',
        f'  <line x1="{source_x}" y1="{ground_y - 27}" x2="{source_x}" y2="{ground_y}" stroke="#0284c7" stroke-width="3" />',
        f'  <text x="{source_x}" y="{ground_y - 48}" class="lbl" fill="#0284c7" text-anchor="middle">Observer / Sound Source</text>',
        # Forward sound waves (arcs)
        f'  <path d="M 120 90 A 40 40 0 0 1 120 130" class="fwd" />',
        f'  <path d="M 180 80 A 60 60 0 0 1 180 140" class="fwd" />',
        f'  <path d="M 240 70 A 80 80 0 0 1 240 150" class="fwd" />',
        f'  <text x="210" y="60" class="lbl" fill="#0284c7">Emitted Sound Pulse</text>',
        # Reflected sound waves (arcs going back)
        f'  <path d="M 340 75 A 70 70 0 0 0 340 145" class="ret" />',
        f'  <path d="M 280 85 A 50 50 0 0 0 280 135" class="ret" />',
        f'  <text x="290" y="165" class="lbl" fill="#dc2626">Reflected Echo</text>',
        # Dimension line between observer and cliff
        f'  <line x1="{source_x}" y1="{ground_y + 18}" x2="{cliff_x}" y2="{ground_y + 18}" class="dim" />',
        f'  <line x1="{source_x}" y1="{ground_y + 12}" x2="{source_x}" y2="{ground_y + 24}" class="dim" />',
        f'  <line x1="{cliff_x}" y1="{ground_y + 12}" x2="{cliff_x}" y2="{ground_y + 24}" class="dim" />',
        f'  <text x="{(source_x + cliff_x)/2.0:.1f}" y="{ground_y + 32}" class="lbl" text-anchor="middle">Distance d = {_fmt_sa(distance_m)} m  (Echo time Δt = {_fmt_sa(time_s)} s)</text>',
        '</svg>',
    ]
    return "\n".join(svg)


def _svg_em_spectrum(highlight_band: str = "Visible") -> str:
    """Generate inline SVG showing the Electromagnetic Spectrum with wavelengths and frequencies."""
    w, h = 480, 190
    y_band = 60
    h_band = 40
    ox = 25
    total_w = 430.0

    bands = [
        ("Radio", "#93c5fd"),
        ("Microwave", "#6ee7b7"),
        ("Infrared", "#fde047"),
        ("Visible", "#f97316"),
        ("UV", "#c084fc"),
        ("X-rays", "#f43f5e"),
        ("Gamma", "#be123c"),
    ]
    col_w = total_w / len(bands)

    rects = []
    for i, (name, col) in enumerate(bands):
        bx = ox + i * col_w
        stroke_col = "#0f172a" if name == highlight_band else "#ffffff"
        stroke_w = "2.5" if name == highlight_band else "1.5"
        rects.append(f'<rect x="{bx:.1f}" y="{y_band}" width="{col_w:.1f}" height="{h_band}" fill="{col}" stroke="{stroke_col}" stroke-width="{stroke_w}" />')
        rects.append(f'<text x="{bx + col_w/2.0:.1f}" y="{y_band + 25}" class="lbl" text-anchor="middle" fill="#0f172a">{name}</text>')

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 10px; font-weight: bold; }',
        '    .arrow { stroke: #0f172a; stroke-width: 1.5; }',
        '    .txt { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '  </style>',
        "".join(rects),
        # Arrow: Increasing Frequency and Energy ->
        f'  <line x1="{ox}" y1="35" x2="{ox + total_w}" y2="35" class="arrow" />',
        f'  <polygon points="{ox + total_w},{35} {ox + total_w - 6},{31} {ox + total_w - 6},{39}" fill="#0f172a" />',
        f'  <text x="{ox + total_w/2.0:.1f}" y="25" class="txt" text-anchor="middle">Increasing Frequency (f) and Photon Energy (E) [Focus: {highlight_band}] →</text>',
        # Arrow: Increasing Wavelength <-
        f'  <line x1="{ox + total_w}" y1="{y_band + h_band + 25}" x2="{ox}" y2="{y_band + h_band + 25}" class="arrow" />',
        f'  <polygon points="{ox},{y_band + h_band + 25} {ox + 6},{y_band + h_band + 21} {ox + 6},{y_band + h_band + 29}" fill="#0f172a" />',
        f'  <text x="{ox + total_w/2.0:.1f}" y="{y_band + h_band + 40}" class="txt" text-anchor="middle">← Increasing Wavelength (λ)</text>',
        '</svg>',
    ]
    return "\n".join(svg)


# =========================================================================== #
# Archetypes 26 to 50
# =========================================================================== #

def _build_26(rng: random.Random) -> Dict[str, Any]:
    sub = "26_longitudinal_wave_definition_and_particle_motion"
    medium = rng.choice(["a stretched slinky spring", "an air column inside a pipe", "a metal rod", "water in a long tube"])
    f_hz = rng.choice([25, 50, 100, 150])
    prompt = (
        f"A longitudinal wave of frequency ${f_hz}\\text{{ Hz}}$ propagates through {medium}.\n"
        "Which of the following statements correctly defines a **longitudinal wave** "
        "and describes the motion of the particles in the medium relative to the wave propagation direction?\n\n"
        "A. Particles of the medium vibrate parallel to the direction of wave propagation.\n"
        "B. Particles of the medium vibrate perpendicular to the direction of wave propagation.\n"
        "C. Particles of the medium travel continuously with the wave from source to detector.\n"
        "D. Particles of the medium move in circular orbits with zero net energy transfer."
    )
    ans = "A. Particles of the medium vibrate parallel to the direction of wave propagation."
    opts = [
        ans,
        "B. Particles of the medium vibrate perpendicular to the direction of wave propagation.",
        "C. Particles of the medium travel continuously with the wave from source to detector.",
        "D. Particles of the medium move in circular orbits with zero net energy transfer.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Recall definition of longitudinal wave", "op": "\\text{Longitudinal: particles oscillate } \\parallel \\text{ to propagation}", "to": "\\text{Parallel vibration}"},
        {"rule": "Contrast with transverse wave", "op": "\\text{Transverse oscillates } \\perp", "to": "\\text{Distinction affirmed}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="In a longitudinal wave, disturbances travel through oscillations parallel to the wave path.",
        t2="Sound waves and compressional slinky waves are canonical examples of longitudinal waves.",
        t3="Option A correctly describes parallel particle oscillation.",
        misconceptions=["confusing_transverse_and_longitudinal", "believing_medium_particles_flow_with_wave"],
    )


def _build_27(rng: random.Random) -> Dict[str, Any]:
    sub = "27_compressions_and_rarefactions_identification"
    wlen = round(rng.uniform(0.35, 1.45), 2)
    svg = _svg_longitudinal_slinky(wlen_m=wlen)
    d_spec = {"kind": "inline_svg", "diagram_role": "context", "svg": svg}

    prompt = (
        f"Refer to the accompanying diagram showing a mechanical disturbance with spacing ${_fmt_sa(wlen)}\\text{{ m}}$ travelling along a stretched helical spring.\n\n"
        "Which option accurately characterises the bunched coil zones (**Compression**) and the spread-out coil zones (**Rarefaction**)?\n\n"
        "A. Bunched zones have maximum coil density and elevated pressure; spread-out zones have minimum coil density and reduced pressure.\n"
        "B. Bunched zones have zero pressure; spread-out zones have maximum vertical displacement.\n"
        "C. Bunched zones have reduced pressure; spread-out zones have elevated pressure.\n"
        "D. Bunched zones occur exclusively at fixed boundaries; spread-out zones occur at the centre."
    )
    ans = "A. Bunched zones have maximum coil density and elevated pressure; spread-out zones have minimum coil density and reduced pressure."
    opts = [
        ans,
        "B. Bunched zones have zero pressure; spread-out zones have maximum vertical displacement.",
        "C. Bunched zones have reduced pressure; spread-out zones have elevated pressure.",
        "D. Bunched zones occur exclusively at fixed boundaries; spread-out zones occur at the centre.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Define compression", "op": "\\text{Compression} = \\text{high coil density, high pressure}", "to": "\\text{High density}"},
        {"rule": "Define rarefaction", "op": "\\text{Rarefaction} = \\text{low coil density, low pressure}", "to": "\\text{Low density}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Look at the coils in the slinky diagram: some are pushed tightly together while others are pulled apart.",
        t2="Tightly spaced coils correspond to compressions (high density), and widely spaced coils to rarefactions (low density).",
        t3="Option A correctly characterizes both density and pressure conditions.",
        misconceptions=["inverting_compression_and_rarefaction", "associating_compression_with_low_pressure"],
        diagram_spec=d_spec,
    )


def _build_28(rng: random.Random) -> Dict[str, Any]:
    sub = "28_longitudinal_wavelength_measurement"
    dist_cm = rng.choice([48, 60, 72, 84, 96, 120])
    num_compressions = rng.choice([3, 4, 5])
    # Distance between N consecutive compressions is (N - 1) wavelengths
    num_waves = num_compressions - 1
    wlen_cm = dist_cm / num_waves
    wlen_m = wlen_cm / 100.0

    svg = _svg_longitudinal_slinky(wlen_m=round(wlen_m, 2))
    d_spec = {"kind": "inline_svg", "diagram_role": "context", "svg": svg}

    prompt = (
        f"Refer to the accompanying diagram showing a longitudinal wave in a stretched spring.\n"
        f"A student measures the distance between {num_compressions} consecutive compressions to be exactly ${dist_cm}\\text{{ cm}}$.\n\n"
        "Calculate the **wavelength** ($\\lambda$) of this longitudinal wave in meters ($\\text{m}$)."
    )
    ans = f"$\\lambda = {_fmt_sa(wlen_m)}\\text{{ m}}$"
    d1 = f"$\\lambda = {_fmt_sa(dist_cm / 100.0)}\\text{{ m}}$"
    d2 = f"$\\lambda = {_fmt_sa((dist_cm / num_compressions) / 100.0)}\\text{{ m}}$"
    d3 = f"$\\lambda = {_fmt_sa(round(wlen_m * 2, 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Determine number of wavelengths between compressions", "op": f"n = {num_compressions} - 1 = {num_waves}", "to": f"{num_waves}\\text{{ full wavelengths}}"},
        {"rule": "Calculate wavelength in centimeters", "op": f"\\lambda = \\frac{{{dist_cm}\\text{{ cm}}}}{{{num_waves}}} = {_fmt_sa(wlen_cm)}\\text{{ cm}}", "to": f"{_fmt_sa(wlen_cm)}\\text{{ cm}}"},
        {"rule": "Convert to SI units (meters)", "op": f"\\lambda = \\frac{{{_fmt_sa(wlen_cm)}}}{{100}} = {_fmt_sa(wlen_m)}\\text{{ m}}", "to": f"{_fmt_sa(wlen_m)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The wavelength of a longitudinal wave is the distance between two consecutive compressions or two consecutive rarefactions.",
        t2=f"Between {num_compressions} consecutive compressions, there are {num_compressions} - 1 = {num_waves} complete wavelengths.",
        t3=f"Divide {dist_cm} cm by {num_waves} to find wavelength in cm, then divide by 100 to convert to meters: {_fmt_sa(wlen_m)} m.",
        misconceptions=["dividing_by_n_instead_of_n_minus_1", "forgetting_to_convert_cm_to_m"],
        diagram_spec=d_spec,
    )


def _build_29(rng: random.Random) -> Dict[str, Any]:
    sub = "29_longitudinal_wave_equation_calculations"
    f_val = rng.choice([20, 25, 40, 50, 80, 100])
    wlen = round(rng.uniform(0.25, 0.85), 2)
    v = round(f_val * wlen, 2)

    prompt = (
        f"A longitudinal compression wave generated in a laboratory slinky spring has a frequency of "
        f"$f = {_fmt_sa(f_val)}\\text{{ Hz}}$ and a wavelength of $\\lambda = {_fmt_sa(wlen)}\\text{{ m}}$.\n\n"
        f"Calculate the speed of the wave ($v$) along the spring."
    )
    ans = f"$v = {_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d1 = f"$v = {_fmt_sa(round(f_val / wlen, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d2 = f"$v = {_fmt_sa(round(wlen / f_val, 3))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d3 = f"$v = {_fmt_sa(round(v * 2, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "State wave equation", "op": "v = f \\lambda", "to": f"v = ({_fmt_sa(f_val)})({_fmt_sa(wlen)})"},
        {"rule": "Evaluate speed", "op": f"({_fmt_sa(f_val)})({_fmt_sa(wlen)})", "to": f"{_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The universal wave equation v = f * lambda applies to all waves, both transverse and longitudinal.",
        t2=f"Substitute f = {_fmt_sa(f_val)} Hz and lambda = {_fmt_sa(wlen)} m into v = f * lambda.",
        t3=f"Multiply {_fmt_sa(f_val)} by {_fmt_sa(wlen)} to obtain {_fmt_sa(v)} m/s.",
        misconceptions=["dividing_frequency_by_wavelength", "thinking_wave_equation_only_applies_to_transverse_waves"],
    )


def _build_30(rng: random.Random) -> Dict[str, Any]:
    sub = "30_transverse_vs_longitudinal_wave_comparison"
    ex_pair = rng.choice([
        ("ripples on a water surface", "sound waves in air"),
        ("vibrations on a guitar string", "compression pulses in a slinky"),
        ("light waves in space", "ultrasonic waves in water"),
    ])
    prompt = (
        f"A learner compares {ex_pair[0]} (a transverse wave) with {ex_pair[1]} (a longitudinal wave).\n"
        "Which of the following comparative statements correctly contrasts **transverse waves** and **longitudinal waves**?\n\n"
        "A. Transverse wave particles oscillate perpendicular to the direction of wave travel; longitudinal wave particles oscillate parallel to the direction of wave travel.\n"
        "B. Transverse waves require a material medium to propagate, whereas longitudinal waves can propagate through a complete vacuum.\n"
        "C. Transverse waves consist of compressions and rarefactions, whereas longitudinal waves consist of crests and troughs.\n"
        "D. Transverse waves travel faster than longitudinal waves in every material medium."
    )
    ans = "A. Transverse wave particles oscillate perpendicular to the direction of wave travel; longitudinal wave particles oscillate parallel to the direction of wave travel."
    opts = [
        ans,
        "B. Transverse waves require a material medium to propagate, whereas longitudinal waves can propagate through a complete vacuum.",
        "C. Transverse waves consist of compressions and rarefactions, whereas longitudinal waves consist of crests and troughs.",
        "D. Transverse waves travel faster than longitudinal waves in every material medium.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Contrast particle oscillation directions", "op": "\\text{Transverse } \\perp \\text{ vs Longitudinal } \\parallel", "to": "\\text{Valid comparison established}"},
        {"rule": "Verify medium requirements", "op": "\\text{Sound (longitudinal) cannot propagate in vacuum}", "to": "\\text{Mechanical medium required for sound}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Recall the primary geometric distinction between transverse and longitudinal waves.",
        t2="In transverse waves, vibration is at 90 degrees (perpendicular) to travel. In longitudinal waves, vibration is collinear (parallel) to travel.",
        t3="Option A states this fundamental distinction accurately.",
        misconceptions=["confusing_vibration_axes", "believing_sound_travels_in_vacuum"],
    )


def _build_31(rng: random.Random) -> Dict[str, Any]:
    sub = "31_sound_wave_nature_and_medium_requirement"
    bell_freq = rng.choice([400, 500, 600, 800])
    prompt = (
        f"An electric ringing bell (frequency ${bell_freq}\\text{{ Hz}}$) is placed inside an airtight glass bell jar. As a vacuum pump removes all the air "
        "from the jar, the sound of the bell becomes increasingly faint until it can no longer be heard, even though "
        "the hammer can still be seen striking the gong.\n\n"
        "Which fundamental physical principle does this observation demonstrate?\n\n"
        "A. Sound is a mechanical wave that requires a material medium to propagate.\n"
        "B. Light cannot propagate through a vacuum.\n"
        "C. Sound waves are electromagnetic waves with high frequencies.\n"
        "D. Sound waves travel faster when the pressure inside the jar drops to zero."
    )
    ans = "A. Sound is a mechanical wave that requires a material medium to propagate."
    opts = [
        ans,
        "B. Light cannot propagate through a vacuum.",
        "C. Sound waves are electromagnetic waves with high frequencies.",
        "D. Sound waves travel faster when the pressure inside the jar drops to zero.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Identify wave classification of sound", "op": "\\text{Sound = mechanical longitudinal wave}", "to": "\\text{Requires medium}"},
        {"rule": "Explain vacuum bell jar result", "op": "\\text{Vacuum = no particles to transmit pressure fluctuations}", "to": "\\text{No sound transmitted}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Sound propagates as mechanical pressure pulses through colliding particles in a medium.",
        t2="In a vacuum, there are no particles to transfer energy between compressions and rarefactions.",
        t3="Option A correctly deduces that sound cannot propagate without a material medium.",
        misconceptions=["thinking_sound_is_electromagnetic", "confusing_sound_and_light_propagation"],
    )


def _build_32(rng: random.Random) -> Dict[str, Any]:
    sub = "32_speed_of_sound_in_different_media"
    solid_name, v_solid = rng.choice([("Steel", 5000), ("Aluminium", 5100), ("Glass", 4540), ("Copper", 3900)])

    prompt = (
        "Consider the speed of sound in three different media at room temperature:\n"
        "• Air (gas): approximately $340\\text{ m}\\cdot\\text{s}^{-1}$\n"
        "• Fresh water (liquid): approximately $1\\,500\\text{ m}\\cdot\\text{s}^{-1}$\n"
        f"• {solid_name} (solid): approximately ${v_solid}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n\n"
        "Which statement correctly explains why sound travels significantly faster in solids than in liquids and gases?\n\n"
        "A. Particles in solids are much closer together and tightly bound by strong intermolecular forces, allowing vibrations to be transmitted rapidly from particle to particle.\n"
        "B. Solids have much lower densities than air, allowing sound waves to move with minimal resistance.\n"
        "C. Sound waves in solids are transverse electromagnetic waves that travel at the speed of light.\n"
        "D. Gas particles absorb all sound energy and convert it entirely into chemical energy."
    )
    ans = "A. Particles in solids are much closer together and tightly bound by strong intermolecular forces, allowing vibrations to be transmitted rapidly from particle to particle."
    opts = [
        ans,
        "B. Solids have much lower densities than air, allowing sound waves to move with minimal resistance.",
        "C. Sound waves in solids are transverse electromagnetic waves that travel at the speed of light.",
        "D. Gas particles absorb all sound energy and convert it entirely into chemical energy.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Compare elasticity and particle proximity", "op": "\\text{Solids: tight lattice, high elasticity}", "to": "\\text{Rapid mechanical coupling}"},
        {"rule": "Contrast speed ordering", "op": "v_{\\text{solid}} > v_{\\text{liquid}} > v_{\\text{gas}}", "to": f"{v_solid} > 1500 > 340\\text{{ m/s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Think about how closely packed the atoms are in a solid compared to free-floating gas molecules.",
        t2="Tightly bound particles in solids transfer vibrational kinetic energy to their neighbors much more rapidly.",
        t3="Option A provides the correct microscopic mechanical explanation.",
        misconceptions=["thinking_sound_travels_fastest_in_gases", "confusing_density_alone_with_elastic_modulus"],
    )


def _build_33(rng: random.Random) -> Dict[str, Any]:
    sub = "33_pitch_and_frequency_relationship"
    f_low = rng.choice([128, 256])
    f_high = rng.choice([512, 1024, 2048])

    prompt = (
        f"A learner sounds two tuning forks in a physics laboratory. Tuning fork X vibrates at a frequency of "
        f"$f_X = {_fmt_sa(f_low)}\\text{{ Hz}}$, while tuning fork Y vibrates at $f_Y = {_fmt_sa(f_high)}\\text{{ Hz}}$.\n\n"
        "Which statement correctly compares the **pitch** of the sounds heard from forks X and Y?\n\n"
        "A. Tuning fork Y produces a sound of higher pitch because pitch is directly proportional to frequency.\n"
        "B. Tuning fork X produces a sound of higher pitch because lower frequencies possess greater energy.\n"
        "C. Both forks produce the exact same pitch because sound travels at the same speed in air.\n"
        "D. Tuning fork Y produces a louder sound, but both forks have the same pitch."
    )
    ans = "A. Tuning fork Y produces a sound of higher pitch because pitch is directly proportional to frequency."
    opts = [
        ans,
        "B. Tuning fork X produces a sound of higher pitch because lower frequencies possess greater energy.",
        "C. Both forks produce the exact same pitch because sound travels at the same speed in air.",
        "D. Tuning fork Y produces a louder sound, but both forks have the same pitch.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Relate pitch to wave property", "op": "\\text{Pitch is the auditory sensation of frequency}", "to": "\\text{Pitch } \\propto f"},
        {"rule": "Compare frequencies", "op": f"f_Y = {_fmt_sa(f_high)}\\text{{ Hz}} > f_X = {_fmt_sa(f_low)}\\text{{ Hz}}", "to": "\\text{Y has higher pitch}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Pitch is the physiological perception of the physical frequency of a sound wave.",
        t2="Higher frequency corresponds to higher pitch (a shrill or squeaky sound).",
        t3=f"Since fork Y ({_fmt_sa(f_high)} Hz) has a higher frequency than X ({_fmt_sa(f_low)} Hz), fork Y has a higher pitch.",
        misconceptions=["confusing_pitch_with_loudness", "inverting_pitch_and_frequency"],
    )


def _build_34(rng: random.Random) -> Dict[str, Any]:
    sub = "34_loudness_and_amplitude_relationship"
    a1 = round(rng.uniform(1.0, 2.5), 1)
    a2 = round(a1 * rng.choice([2.0, 3.0]), 1)

    prompt = (
        f"A loudspeaker emits a sound wave. Initially, the vibrating diaphragm has an amplitude of $A_1 = {_fmt_sa(a1)}\\text{{ mm}}$. "
        f"The volume knob is turned up so that the amplitude increases to $A_2 = {_fmt_sa(a2)}\\text{{ mm}}$, while the frequency remains unchanged.\n\n"
        "What change occurs in the sound perceived by a listener, and what wave property is responsible?\n\n"
        "A. The sound becomes louder because loudness increases with increasing wave amplitude (and energy).\n"
        "B. The pitch becomes higher because larger amplitudes cause particles to oscillate with higher frequencies.\n"
        "C. The speed of the sound wave in the air doubles.\n"
        "D. The wavelength of the sound wave increases proportionally."
    )
    ans = "A. The sound becomes louder because loudness increases with increasing wave amplitude (and energy)."
    opts = [
        ans,
        "B. The pitch becomes higher because larger amplitudes cause particles to oscillate with higher frequencies.",
        "C. The speed of the sound wave in the air doubles.",
        "D. The wavelength of the sound wave increases proportionally.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Relate loudness to amplitude", "op": "\\text{Loudness is determined by amplitude and wave energy}", "to": "\\text{Loudness } \\propto A"},
        {"rule": "Verify frequency independence", "op": "\\text{Frequency unchanged } \\implies \\text{ pitch unchanged}", "to": "\\text{Pitch remains constant}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Amplitude represents the maximum displacement of particles from rest and is a measure of wave energy.",
        t2="Greater amplitude means more energy is transferred to the eardrum per second, perceived as greater loudness.",
        t3="Option A is correct: turning up the amplitude makes the sound louder without altering pitch.",
        misconceptions=["confusing_loudness_with_pitch", "believing_amplitude_affects_wave_speed"],
    )


def _build_35(rng: random.Random) -> Dict[str, Any]:
    sub = "35_sound_quality_timbre_and_waveform"
    f_fund = float(rng.choice([256, 320, 440, 512]))
    amp_val = round(rng.uniform(0.8, 1.8), 1)
    svg = _svg_sound_waveforms(amp=amp_val, f1=f_fund)
    d_spec = {"kind": "inline_svg", "diagram_role": "context", "svg": svg}

    prompt = (
        "Refer to the accompanying diagram showing the waveforms of notes played by a tuning fork (Instrument A) "
        f"and an acoustic guitar (Instrument B). Both instruments are sounding a note of frequency ${_fmt_sa(f_fund)}\\text{{ Hz}}$ "
        "with equal loudness.\n\n"
        "Why can a human listener easily distinguish between the two instruments, and which wave property accounts for this difference?\n\n"
        "A. They have different sound quality (timbre) due to the presence of different higher harmonics (overtones) producing distinct waveform shapes.\n"
        "B. They have different speeds of sound in the air around the instruments.\n"
        "C. Instrument A has a higher frequency than Instrument B.\n"
        "D. Instrument B has a larger fundamental wavelength than Instrument A."
    )
    ans = "A. They have different sound quality (timbre) due to the presence of different higher harmonics (overtones) producing distinct waveform shapes."
    opts = [
        ans,
        "B. They have different speeds of sound in the air around the instruments.",
        "C. Instrument A has a higher frequency than Instrument B.",
        "D. Instrument B has a larger fundamental wavelength than Instrument A.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Identify timbre / sound quality", "op": "\\text{Timbre depends on the shape of the waveform}", "to": "\\text{Harmonic composition}"},
        {"rule": "Verify pitch and loudness equality", "op": f"f_A = f_B = {_fmt_sa(f_fund)}\\text{{ Hz}},\\; A_A = A_B", "to": "\\text{Same pitch and loudness, different timbre}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Even when two musical instruments play the same note (same frequency) at the same volume, they sound different.",
        t2="This characteristic tone quality is called timbre, caused by the blend of overtone harmonics that reshape the wave.",
        t3="Option A correctly attributes the distinguishable character to timbre and complex waveforms.",
        misconceptions=["thinking_timbre_is_frequency", "confusing_wave_shape_with_wave_speed"],
        diagram_spec=d_spec,
    )


def _build_36(rng: random.Random) -> Dict[str, Any]:
    sub = "36_human_audible_frequency_range_and_infrasound"
    test_freq = rng.choice([12, 15, 25000, 30000, 45000])
    is_infra = test_freq < 20
    is_ultra = test_freq > 20000

    if is_infra:
        category = "infrasound"
        reason = "its frequency is below the lower threshold of normal human hearing (20 Hz)"
    else:
        category = "ultrasound"
        reason = "its frequency is above the upper threshold of normal human hearing (20 000 Hz)"

    prompt = (
        f"A specialised acoustic transmitter emits sound waves at a frequency of $f = {test_freq}\\text{{ Hz}}$.\n\n"
        "How is this sound wave classified relative to the normal range of human hearing, and is it audible to humans?\n\n"
        f"A. Classified as {category}; inaudible to humans because {reason}.\n"
        "B. Classified as audible sound; clearly heard by humans because the ear hears all frequencies up to $100\\,000\\text{ Hz}$.\n"
        f"C. Classified as electromagnetic radiation; audible only through radio antennas.\n"
        f"D. Classified as {category}; highly audible and damaging to human hearing."
    )
    ans = f"A. Classified as {category}; inaudible to humans because {reason}."
    opts = [
        ans,
        "B. Classified as audible sound; clearly heard by humans because the ear hears all frequencies up to $100\\,000\\text{ Hz}$.",
        "C. Classified as electromagnetic radiation; audible only through radio antennas.",
        f"D. Classified as {category}; highly audible and damaging to human hearing.",
    ]
    rng.shuffle(opts)

    steps = [
        {"rule": "State human hearing limits", "op": "20\\text{ Hz} \\le f_{\\text{audible}} \\le 20\\,000\\text{ Hz}", "to": "\\text{Audible range}"},
        {"rule": "Classify frequency", "op": f"f = {test_freq}\\text{{ Hz}}", "to": f"\\text{{{category.capitalize()}}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Normal human hearing spans the frequency range from 20 Hz to 20 000 Hz (20 kHz).",
        t2="Frequencies below 20 Hz are infrasound; frequencies above 20 kHz are ultrasound.",
        t3=f"Since {test_freq} Hz falls outside 20–20 000 Hz, it is {category} and inaudible to humans.",
        misconceptions=["confusing_infrasound_and_ultrasound", "believing_ultrasound_is_electromagnetic"],
    )


def _build_37(rng: random.Random) -> Dict[str, Any]:
    sub = "37_echo_distance_and_reflection_time"
    v_sound = rng.choice([330, 340, 345])
    t_roundtrip = rng.choice([0.8, 1.2, 1.5, 2.0, 2.4, 3.0])
    # 2d = v * t => d = (v * t) / 2
    d = round((v_sound * t_roundtrip) / 2.0, 1)

    svg = _svg_echo_reflection(distance_m=d, time_s=t_roundtrip)
    d_spec = {"kind": "inline_svg", "diagram_role": "context", "svg": svg}

    prompt = (
        f"Refer to the accompanying diagram showing a person shouting in front of a tall vertical cliff.\n"
        f"The echo of the shout is heard $\\Delta t = {_fmt_sa(t_roundtrip)}\\text{{ s}}$ later. "
        f"Take the speed of sound in air as $v = {_fmt_sa(v_sound)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the distance ($d$) from the person to the reflecting cliff in meters."
    )
    ans = f"$d = {_fmt_sa(d)}\\text{{ m}}$"
    d1 = f"$d = {_fmt_sa(round(v_sound * t_roundtrip, 1))}\\text{{ m}}$"
    d2 = f"$d = {_fmt_sa(round(d / 2, 1))}\\text{{ m}}$"
    d3 = f"$d = {_fmt_sa(round(v_sound / t_roundtrip, 1))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Identify round-trip distance for an echo", "op": "2d = v \\Delta t", "to": f"2d = ({_fmt_sa(v_sound)})({_fmt_sa(t_roundtrip)})"},
        {"rule": "Compute total distance travelled by sound", "op": f"({_fmt_sa(v_sound)})({_fmt_sa(t_roundtrip)}) = {_fmt_sa(v_sound * t_roundtrip)}\\text{{ m}}", "to": f"{_fmt_sa(v_sound * t_roundtrip)}\\text{{ m}}"},
        {"rule": "Divide by 2 to find one-way distance to cliff", "op": f"d = \\frac{{{_fmt_sa(v_sound * t_roundtrip)}}}{{2}} = {_fmt_sa(d)}\\text{{ m}}", "to": f"{_fmt_sa(d)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Remember that an echo travels to the barrier and back again, covering a total distance of 2d.",
        t2="Use the relationship 2d = v * delta_t, so d = (v * delta_t) / 2.",
        t3=f"Multiply {_fmt_sa(v_sound)} by {_fmt_sa(t_roundtrip)} and divide by 2: {_fmt_sa(d)} m.",
        misconceptions=["forgetting_to_divide_by_2_for_echo", "multiplying_by_2_instead_of_dividing"],
        diagram_spec=d_spec,
    )


def _build_38(rng: random.Random) -> Dict[str, Any]:
    sub = "38_speed_of_sound_determination_via_echo"
    dist_m = rng.choice([170, 255, 340, 510, 680])
    # Choose clean speed 340 m/s
    v_target = 340.0
    t_roundtrip = round((2 * dist_m) / v_target, 2)
    v_calc = round((2 * dist_m) / t_roundtrip, 1)

    svg = _svg_echo_reflection(distance_m=dist_m, time_s=t_roundtrip)
    d_spec = {"kind": "inline_svg", "diagram_role": "context", "svg": svg}

    prompt = (
        f"Refer to the accompanying diagram showing an acoustic timing setup at a distance $d = {_fmt_sa(dist_m)}\\text{{ m}}$ from a reflecting barrier. "
        f"One learner claps two wooden blocks together and the group records that the echo returns after a time interval of "
        f"$\\Delta t = {_fmt_sa(t_roundtrip)}\\text{{ s}}$.\n\n"
        f"Determine the experimental speed of sound ($v$) in air from these measurements."
    )
    ans = f"$v = {_fmt_sa(v_calc)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d1 = f"$v = {_fmt_sa(round(dist_m / t_roundtrip, 1))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d2 = f"$v = {_fmt_sa(round((dist_m * t_roundtrip) / 2, 1))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d3 = f"$v = {_fmt_sa(round(v_calc * 2, 1))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "State round-trip echo relation", "op": "v = \\frac{2d}{\\Delta t}", "to": f"v = \\frac{{2({_fmt_sa(dist_m)})}}{{{_fmt_sa(t_roundtrip)}}}"},
        {"rule": "Calculate numerical speed of sound", "op": f"\\frac{{{2 * dist_m}}}{{{_fmt_sa(t_roundtrip)}}}", "to": f"{_fmt_sa(v_calc)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The sound pulse travels to the wall and back, so the total distance is 2 * d.",
        t2=f"Calculate total distance: 2 * {dist_m} = {2 * dist_m} m.",
        t3=f"Divide total distance by time: {2 * dist_m} / {_fmt_sa(t_roundtrip)} = {_fmt_sa(v_calc)} m/s.",
        misconceptions=["dividing_single_distance_by_time", "inverting_time_and_distance"],
        diagram_spec=d_spec,
    )


def _build_39(rng: random.Random) -> Dict[str, Any]:
    sub = "39_marine_sonar_depth_sounding_calculation"
    v_water = rng.choice([1480, 1500, 1520])
    t_pulse = rng.choice([0.4, 0.6, 0.8, 1.2, 1.6, 2.5])
    depth = round((v_water * t_pulse) / 2.0, 1)

    prompt = (
        f"A research ship uses an active SONAR (Sound Navigation and Ranging) system to map the ocean floor. "
        f"An ultrasound pulse sent vertically downward into the seawater returns to the ship's receiver "
        f"$t = {_fmt_sa(t_pulse)}\\text{{ s}}$ after emission.\n"
        f"The speed of sound in seawater is $v = {_fmt_sa(v_water)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the ocean depth ($h$) beneath the ship."
    )
    ans = f"$h = {_fmt_sa(depth)}\\text{{ m}}$"
    d1 = f"$h = {_fmt_sa(round(v_water * t_pulse, 1))}\\text{{ m}}$"
    d2 = f"$h = {_fmt_sa(round(depth / 2, 1))}\\text{{ m}}$"
    d3 = f"$h = {_fmt_sa(round(v_water / t_pulse, 1))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Apply echo formula to SONAR depth sounding", "op": "2h = v t", "to": f"h = \\frac{{v t}}{{2}}"},
        {"rule": "Substitute speed and round-trip time", "op": f"h = \\frac{{({_fmt_sa(v_water)})({_fmt_sa(t_pulse)})}}{{2}}", "to": f"{_fmt_sa(depth)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="SONAR uses the reflection of ultrasound waves to measure depth.",
        t2="The pulse travels down to the seabed and back up to the ship, so 2 * depth = speed * time.",
        t3=f"Multiply {_fmt_sa(v_water)} by {_fmt_sa(t_pulse)} and divide by 2: {_fmt_sa(depth)} m.",
        misconceptions=["omitting_the_factor_of_two_in_sonar", "using_speed_of_sound_in_air_instead_of_water"],
    )


def _build_40(rng: random.Random) -> Dict[str, Any]:
    sub = "40_medical_ultrasound_sonography_principles"
    freq_mhz = rng.choice([2, 3, 5, 7])
    prompt = (
        f"Medical ultrasound scanning (sonography at ${freq_mhz}\\text{{ MHz}}$) is routinely used to monitor the development of an unborn baby (foetus). "
        "Which of the following explains why ultrasound is preferred over X-rays for prenatal scanning, and describes how a sonogram is produced?\n\n"
        "A. Ultrasound consists of non-ionising high-frequency sound waves that do not damage living cells or DNA; scans are created by detecting sound pulses reflected at boundaries between different body tissues.\n"
        "B. Ultrasound uses electromagnetic waves with lower frequencies than radio waves that pass through bone without reflecting.\n"
        "C. Ultrasound provides sharper scans because sound travels faster than light inside human tissue.\n"
        "D. Ultrasound emits radioactive alpha particles that illuminate soft tissues safely."
    )
    ans = "A. Ultrasound consists of non-ionising high-frequency sound waves that do not damage living cells or DNA; scans are created by detecting sound pulses reflected at boundaries between different body tissues."
    opts = [
        ans,
        "B. Ultrasound uses electromagnetic waves with lower frequencies than radio waves that pass through bone without reflecting.",
        "C. Ultrasound provides sharper scans because sound travels faster than light inside human tissue.",
        "D. Ultrasound emits radioactive alpha particles that illuminate soft tissues safely.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Identify safety advantages of ultrasound", "op": "\\text{Non-ionising mechanical wave}", "to": "\\text{Zero cellular / DNA ionization risk}"},
        {"rule": "Explain acoustic impedance reflection", "op": "\\text{Echoes generated at tissue interfaces}", "to": "\\text{Real-time anatomical imaging}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Consider why doctors avoid exposing a developing fetus to ionizing X-ray radiation.",
        t2="Ultrasound is non-ionizing mechanical vibration (> 20 kHz), completely safe for soft body tissues.",
        t3="Option A accurately contrasts non-ionizing safety and partial reflection at tissue boundaries.",
        misconceptions=["confusing_ultrasound_with_ionising_radiation", "believing_ultrasound_is_an_xray_technique"],
    )


def _build_41(rng: random.Random) -> Dict[str, Any]:
    sub = "41_industrial_ultrasound_flaw_detection"
    v_steel = 5000.0
    thickness_mm = rng.choice([80, 100, 120, 150])
    crack_depth_mm = rng.choice([25, 35, 45, 50])
    
    # Time for echo from crack: 2 * (crack_depth) / v_steel
    crack_depth_m = crack_depth_mm / 1000.0
    t_crack_s = (2.0 * crack_depth_m) / v_steel
    t_crack_us = t_crack_s * 1e6

    prompt = (
        f"An industrial non-destructive testing technician uses an ultrasonic probe on a steel rail of total thickness "
        f"${thickness_mm}\\text{{ mm}}$. The speed of sound in the steel is $v = 5\\,000\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"An unexpected flaw echo is detected $\\Delta t = {_fmt_sa(t_crack_us)}\\text{{ }}\\mu\\text{{s}}$ "
        f"(${_fmt_sci(t_crack_s)}\\text{{ s}}$) after pulse transmission, well before the back-wall echo.\n\n"
        f"At what depth ($d$) beneath the surface is the internal flaw located?"
    )
    ans = f"$d = {crack_depth_mm}\\text{{ mm}}$"
    d1 = f"$d = {crack_depth_mm * 2}\\text{{ mm}}$"
    d2 = f"$d = {thickness_mm - crack_depth_mm}\\text{{ mm}}$"
    d3 = f"$d = {round(crack_depth_mm / 2, 1)}\\text{{ mm}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Apply echo distance formula", "op": "d = \\frac{v \\Delta t}{2}", "to": f"d = \\frac{{(5000)({_fmt_sci(t_crack_s)})}}{{2}}"},
        {"rule": "Calculate depth in meters", "op": f"d = {_fmt_sa(crack_depth_m, 3)}\\text{{ m}}", "to": f"{_fmt_sa(crack_depth_m, 3)}\\text{{ m}}"},
        {"rule": "Convert depth to millimeters", "op": f"{_fmt_sa(crack_depth_m, 3)} \\times 1000 = {crack_depth_mm}\\text{{ mm}}", "to": f"{crack_depth_mm}\\text{{ mm}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="An internal flaw or crack creates an acoustic boundary that reflects ultrasound back to the probe.",
        t2="Calculate the depth using d = (v * delta_t) / 2.",
        t3=f"Multiply 5000 m/s by {_fmt_sci(t_crack_s)} s and divide by 2 to get {crack_depth_m} m = {crack_depth_mm} mm.",
        misconceptions=["forgetting_to_divide_roundtrip_time_by_2", "confusing_microseconds_with_seconds"],
    )


def _build_42(rng: random.Random) -> Dict[str, Any]:
    sub = "42_bat_echolocation_obstacle_avoidance"
    v_air = 340.0
    d_m = round(rng.uniform(1.7, 5.1), 1)
    t_return = round((2.0 * d_m) / v_air, 3)

    prompt = (
        f"A microbat flying in complete darkness emits an ultrasonic chirp at $50\\text{{ kHz}}$. "
        f"The bat detects the echo from a flying moth $\\Delta t = {_fmt_sa(t_return)}\\text{{ s}}$ later.\n"
        f"Taking the speed of sound in air as $v = 340\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, calculate the distance "
        f"between the bat and the moth at the moment the chirp was emitted."
    )
    ans = f"$d = {_fmt_sa(d_m)}\\text{{ m}}$"
    d1 = f"$d = {_fmt_sa(round(v_air * t_return, 2))}\\text{{ m}}$"
    d2 = f"$d = {_fmt_sa(round(d_m / 2, 2))}\\text{{ m}}$"
    d3 = f"$d = {_fmt_sa(round(d_m * 2, 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Relate round-trip distance to echo time", "op": "2d = v \\Delta t", "to": f"d = \\frac{{v \\Delta t}}{{2}}"},
        {"rule": "Substitute numerical values", "op": f"d = \\frac{{(340)({_fmt_sa(t_return)})}}{{2}}", "to": f"{_fmt_sa(d_m)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Bats use biological echolocation by emitting high-frequency sound chirps and listening for echoes.",
        t2="Sound travels to the moth and returns, so the round-trip distance is 2d.",
        t3=f"Multiply 340 m/s by {_fmt_sa(t_return)} s and divide by 2: {_fmt_sa(d_m)} m.",
        misconceptions=["omitting_the_factor_of_two", "assuming_frequency_affects_echo_speed"],
    )


def _build_43(rng: random.Random) -> Dict[str, Any]:
    sub = "43_electromagnetic_radiation_wave_model_and_speed"
    c_val = "3{,}0 \\times 10^8\\text{ m}\\cdot\\text{s}^{-1}"
    source_ex = rng.choice(["a distant star", "a solar flare", "an orbiting communication satellite", "a radio broadcast tower"])
    prompt = (
        f"Electromagnetic radiation travels from {source_ex} through the vacuum of space.\n"
        "Which of the following statements correctly describes the **wave model of electromagnetic radiation** "
        "and its speed in a vacuum?\n\n"
        "A. Electromagnetic waves consist of mutually perpendicular, oscillating electric and magnetic fields that propagate through a vacuum at $c = 3{,}0 \\times 10^8\\text{ m}\\cdot\\text{s}^{-1}$ without requiring any material medium.\n"
        "B. Electromagnetic waves are longitudinal pressure waves that require air particles to propagate at $340\\text{ m}\\cdot\\text{s}^{-1}$.\n"
        "C. Electromagnetic waves consist only of stationary magnetic fields that travel at varying speeds depending on the source.\n"
        "D. Electromagnetic waves travel infinitely fast in empty space and only slow down upon entering Earth's atmosphere."
    )
    ans = f"A. Electromagnetic waves consist of mutually perpendicular, oscillating electric and magnetic fields that propagate through a vacuum at $c = {c_val}$ without requiring any material medium."
    opts = [
        ans,
        "B. Electromagnetic waves are longitudinal pressure waves that require air particles to propagate at $340\\text{ m}\\cdot\\text{s}^{-1}$.",
        "C. Electromagnetic waves consist only of stationary magnetic fields that travel at varying speeds depending on the source.",
        "D. Electromagnetic waves travel infinitely fast in empty space and only slow down upon entering Earth's atmosphere.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Recall wave nature of EM radiation", "op": "\\vec{E} \\perp \\vec{B} \\perp \\vec{v}", "to": "\\text{Mutually perpendicular oscillating fields}"},
        {"rule": "State universal speed of light in vacuum", "op": "c = 3{,}0 \\times 10^8\\text{ m}\\cdot\\text{s}^{-1}", "to": "\\text{Constant across entire EM spectrum}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Electromagnetic radiation does not need a material medium; it can travel through the vacuum of outer space.",
        t2="Accelerating charges produce oscillating electric and magnetic fields that are perpendicular to each other and to the direction of propagation.",
        t3=f"All electromagnetic waves travel at the speed of light in vacuum, c = {c_val}.",
        misconceptions=["thinking_light_requires_a_medium", "confusing_em_waves_with_mechanical_waves"],
    )


def _build_44(rng: random.Random) -> Dict[str, Any]:
    sub = "44_electromagnetic_wave_equation_calculations"
    c_speed = 3.0e8
    # Select a standard EM frequency or wavelength
    em_type = rng.choice(["FM Radio", "Microwave", "Visible Light", "X-ray"])
    if em_type == "FM Radio":
        f_val = round(rng.uniform(88.0, 108.0), 1) * 1e6
        desc = f"an FM radio transmission with frequency $f = {_fmt_sci(f_val)}\\text{{ Hz}}$"
    elif em_type == "Microwave":
        f_val = 2.45e9
        desc = "a microwave oven operating at a frequency of $f = 2{,}45 \\times 10^9\\text{ Hz}$"
    elif em_type == "Visible Light":
        f_val = 5.0e14
        desc = "orange visible light with a frequency of $f = 5{,}0 \\times 10^{14}\\text{ Hz}$"
    else:
        f_val = 3.0e17
        desc = "medical diagnostic X-rays with a frequency of $f = 3{,}0 \\times 10^{17}\\text{ Hz}$"

    wlen = c_speed / f_val

    prompt = (
        f"Consider {desc} propagating through a vacuum at $c = 3{{,}}0 \\times 10^8\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the **wavelength** ($\\lambda$) of this electromagnetic wave."
    )
    ans = f"$\\lambda = {_fmt_sci(wlen)}\\text{{ m}}$"
    d1 = f"$\\lambda = {_fmt_sci(f_val / c_speed)}\\text{{ m}}$"
    d2 = f"$\\lambda = {_fmt_sci(c_speed * f_val)}\\text{{ m}}$"
    d3 = f"$\\lambda = {_fmt_sci(wlen * 10)}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "State wave equation for electromagnetic waves", "op": "c = f \\lambda", "to": "\\lambda = \\frac{c}{f}"},
        {"rule": "Substitute vacuum speed of light and frequency", "op": f"\\lambda = \\frac{{3{{,}}0 \\times 10^8}}{{{_fmt_sci(f_val)}}}", "to": f"{_fmt_sci(wlen)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="For all electromagnetic radiation in a vacuum, the wave speed is c = 3,0 x 10^8 m/s.",
        t2="Rearrange the wave equation c = f * lambda to solve for wavelength: lambda = c / f.",
        t3=f"Divide 3,0 x 10^8 by the frequency to find lambda = {_fmt_sci(wlen)} m.",
        misconceptions=["dividing_frequency_by_speed_of_light", "forgetting_speed_of_light_in_vacuum"],
    )


def _build_45(rng: random.Random) -> Dict[str, Any]:
    sub = "45_electromagnetic_spectrum_frequency_and_wavelength_ordering"
    focus_band = rng.choice(["Radio", "Microwave", "Infrared", "Visible", "UV", "X-rays", "Gamma"])
    svg = _svg_em_spectrum(highlight_band=focus_band)
    d_spec = {"kind": "inline_svg", "diagram_role": "context", "svg": svg}

    prompt = (
        f"Refer to the accompanying diagram showing the bands of the electromagnetic spectrum (with **{focus_band}** highlighted).\n\n"
        "Which of the following correctly lists the seven bands of the electromagnetic spectrum in order of "
        "**increasing frequency** (and therefore increasing photon energy)?\n\n"
        "A. Radio waves, Microwaves, Infrared, Visible light, Ultraviolet, X-rays, Gamma rays\n"
        "B. Gamma rays, X-rays, Ultraviolet, Visible light, Infrared, Microwaves, Radio waves\n"
        "C. Visible light, Ultraviolet, Infrared, Radio waves, Microwaves, X-rays, Gamma rays\n"
        "D. Radio waves, Infrared, Microwaves, Visible light, X-rays, Ultraviolet, Gamma rays"
    )
    ans = "A. Radio waves, Microwaves, Infrared, Visible light, Ultraviolet, X-rays, Gamma rays"
    opts = [
        ans,
        "B. Gamma rays, X-rays, Ultraviolet, Visible light, Infrared, Microwaves, Radio waves",
        "C. Visible light, Ultraviolet, Infrared, Radio waves, Microwaves, X-rays, Gamma rays",
        "D. Radio waves, Infrared, Microwaves, Visible light, X-rays, Ultraviolet, Gamma rays",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Recall EM spectrum sequence by frequency", "op": "f_{\\text{Radio}} < f_{\\text{Micro}} < f_{\\text{IR}} < f_{\\text{Vis}} < f_{\\text{UV}} < f_{\\text{X-ray}} < f_{\\text{Gamma}}", "to": "\\text{Order established}"},
        {"rule": "Confirm inverse relationship with wavelength", "op": "\\lambda \\propto \\frac{1}{f}", "to": "\\text{Radio has longest } \\lambda \\text{, Gamma has shortest } \\lambda"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Radio waves have the longest wavelengths and lowest frequencies.",
        t2="Gamma rays have the shortest wavelengths and highest frequencies (and highest photon energies).",
        t3="Option A lists the bands in strict order of increasing frequency from Radio to Gamma.",
        misconceptions=["reversing_frequency_and_wavelength_order", "swapping_infrared_and_ultraviolet"],
        diagram_spec=d_spec,
    )


def _build_46(rng: random.Random) -> Dict[str, Any]:
    sub = "46_electromagnetic_spectrum_applications"
    em_item = rng.choice([
        ("Microwaves", "satellite communications, cellphones, and heating water molecules in food", "Radio waves"),
        ("Infrared radiation", "thermal imaging cameras, TV remote controls, and radiant heaters", "Ultraviolet"),
        ("Ultraviolet radiation", "sterilising surgical instruments, banknote forgery detection, and stimulating vitamin D synthesis in human skin", "Infrared"),
        ("X-rays", "diagnostic medical imaging of dense bones and airport security baggage inspection", "Microwaves"),
        ("Gamma rays", "radiation therapy for destroying malignant cancer cells and sterilising medical equipment", "Visible light"),
    ])
    radiation, application, distractor = em_item

    prompt = (
        f"Which band of the electromagnetic spectrum is primarily utilised for {application}?\n\n"
        f"A. {radiation}\n"
        f"B. {distractor}\n"
        f"C. Sound waves\n"
        f"D. Cathode rays"
    )
    ans = f"A. {radiation}"
    opts = [
        ans,
        f"B. {distractor}",
        "C. Sound waves",
        "D. Cathode rays",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Identify practical technological use of EM wave band", "op": f"\\text{{{application}}} \\to \\text{{{radiation}}}", "to": f"\\text{{{radiation}}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Match the technological application to the specific energy and penetrating properties of the EM band.",
        t2=f"{radiation} possesses the precise penetration/energy characteristics suited for {application}.",
        t3=f"Option A ({radiation}) is the correct technological match.",
        misconceptions=["confusing_infrared_with_ultraviolet", "confusing_sound_waves_with_electromagnetic_waves"],
    )


def _build_47(rng: random.Random) -> Dict[str, Any]:
    sub = "47_penetrating_ability_and_ionising_radiation_hazards"
    example_band = rng.choice(["Ultraviolet (UV-B) radiation", "medical X-rays", "high-energy Gamma rays"])
    prompt = (
        f"High-frequency radiations such as {example_band} are classified as **ionising radiation**, "
        "whereas radio waves and visible light are **non-ionising**.\n\n"
        "What does it mean for electromagnetic radiation to be **ionising**, and what biological hazard does this present to humans?\n\n"
        "A. The photons carry sufficient energy to remove tightly bound electrons from atoms, creating ions that can damage cellular DNA and cause genetic mutations or cancers.\n"
        "B. The waves vibrate so slowly that they freeze living cells upon contact.\n"
        "C. The radiation reflects harmlessly off human skin, converting entirely into audible sound.\n"
        "D. The radiation has such a long wavelength that it physically pushes whole cells out of the human body."
    )
    ans = "A. The photons carry sufficient energy to remove tightly bound electrons from atoms, creating ions that can damage cellular DNA and cause genetic mutations or cancers."
    opts = [
        ans,
        "B. The waves vibrate so slowly that they freeze living cells upon contact.",
        "C. The radiation reflects harmlessly off human skin, converting entirely into audible sound.",
        "D. The radiation has such a long wavelength that it physically pushes whole cells out of the human body.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Define ionisation by radiation", "op": "E_{\\text{photon}} > \\text{Ionisation energy of atom}", "to": "\\text{Ejection of orbital electron}"},
        {"rule": "Relate ionisation to biological damage", "op": "\\text{Ions disrupt molecular bonds in DNA}", "to": "\\text{Mutations / cancer risk}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Ionisation means removing an electron from an atom to create a charged ion.",
        t2="High-frequency photons (UV, X-rays, gamma) have enough energy to break chemical bonds in DNA.",
        t3="Option A accurately explains electron ejection and subsequent biological/DNA mutation risks.",
        misconceptions=["thinking_all_electromagnetic_waves_are_ionising", "believing_radio_waves_cause_dna_mutations"],
    )


def _build_48(rng: random.Random) -> Dict[str, Any]:
    sub = "48_photon_energy_calculation_from_frequency"
    h_const = 6.63e-34
    # Choose frequency for UV or visible photon
    f_exp = rng.choice([14, 15, 16])
    f_base = round(rng.uniform(1.5, 8.5), 1)
    f_val = f_base * (10 ** f_exp)
    energy = h_const * f_val

    prompt = (
        f"A photon of electromagnetic radiation has a frequency of $f = {_fmt_sci(f_val)}\\text{{ Hz}}$.\n"
        f"Planck's constant is $h = 6{{,}}63 \\times 10^{{-34}}\\text{{ J}}\\cdot\\text{{s}}$.\n\n"
        f"Calculate the **energy** ($E$) of this single photon in Joules ($\\text{{J}}$)."
    )
    ans = f"$E = {_fmt_sci(energy)}\\text{{ J}}$"
    d1 = f"$E = {_fmt_sci(f_val / h_const)}\\text{{ J}}$"
    d2 = f"$E = {_fmt_sci(h_const / f_val)}\\text{{ J}}$"
    d3 = f"$E = {_fmt_sci(energy * 10)}\\text{{ J}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "State Planck photon energy equation", "op": "E = h f", "to": f"E = (6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_val)})"},
        {"rule": "Compute photon energy in Joules", "op": f"(6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_val)})", "to": f"{_fmt_sci(energy)}\\text{{ J}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="According to the quantum model, electromagnetic radiation is emitted and absorbed in discrete packets called photons.",
        t2="Use Planck's equation: E = h * f, where h = 6,63 x 10^-34 J*s.",
        t3=f"Multiply h by {_fmt_sci(f_val)} Hz to get E = {_fmt_sci(energy)} J.",
        misconceptions=["dividing_planck_constant_by_frequency", "confusing_frequency_with_wavelength_in_planck_equation"],
    )


def _build_49(rng: random.Random) -> Dict[str, Any]:
    sub = "49_photon_energy_calculation_from_wavelength"
    h_const = 6.63e-34
    c_const = 3.0e8
    # Select a visible or UV wavelength: 200 nm to 750 nm
    wlen_nm = rng.choice([250, 400, 500, 600, 650, 700])
    wlen_m = wlen_nm * 1e-9
    energy = (h_const * c_const) / wlen_m

    prompt = (
        f"A laser emits a beam of monochromatic light with a wavelength of $\\lambda = {wlen_nm}\\text{{ nm}}$ "
        f"(${_fmt_sci(wlen_m)}\\text{{ m}}$) in a vacuum.\n"
        f"Constants: $h = 6{{,}}63 \\times 10^{{-34}}\\text{{ J}}\\cdot\\text{{s}}$, "
        f"$c = 3{{,}}0 \\times 10^8\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the energy ($E$) of a single photon from this laser beam."
    )
    ans = f"$E = {_fmt_sci(energy)}\\text{{ J}}$"
    d1 = f"$E = {_fmt_sci((h_const * wlen_m) / c_const)}\\text{{ J}}$"
    d2 = f"$E = {_fmt_sci(h_const * c_const * wlen_m)}\\text{{ J}}$"
    d3 = f"$E = {_fmt_sci(energy * 1e3)}\\text{{ J}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Combine wave equation and Planck equation", "op": "c = f \\lambda \\implies f = \\frac{c}{\\lambda}", "to": "E = \\frac{h c}{\\lambda}"},
        {"rule": "Substitute constants and wavelength in meters", "op": f"E = \\frac{{(6{{,}}63 \\times 10^{{-34}})(3{{,}}0 \\times 10^8)}}{{{_fmt_sci(wlen_m)}}}", "to": f"{_fmt_sci(energy)}\\text{{ J}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Substitute f = c / lambda into E = h * f to obtain E = (h * c) / lambda.",
        t2=f"Ensure wavelength is in meters: {wlen_nm} nm = {wlen_nm} x 10^-9 m.",
        t3=f"Calculate (6,63 x 10^-34 * 3,0 x 10^8) / ({_fmt_sci(wlen_m)}) = {_fmt_sci(energy)} J.",
        misconceptions=["forgetting_to_convert_nanometers_to_meters", "multiplying_by_wavelength_instead_of_dividing"],
    )


def _build_50(rng: random.Random) -> Dict[str, Any]:
    sub = "50_waves_sound_light_diagnostic_synthesis"
    # Multi-step synthesis: comparing sound wave vs light wave properties and calculating photon energy
    wlen_nm = rng.choice([300, 450, 600])
    wlen_m = wlen_nm * 1e-9
    c_const = 3.0e8
    h_const = 6.63e-34
    f_light = c_const / wlen_m
    e_photon = h_const * f_light

    prompt = (
        f"A learner analyses both sound waves and light waves during a comprehensive waves revision laboratory.\n\n"
        f"Consider a beam of monochromatic light of wavelength $\\lambda = {wlen_nm}\\text{{ nm}}$ (${_fmt_sci(wlen_m)}\\text{{ m}}$).\n"
        f"1. Which wave type represents sound, and which represents light?\n"
        f"2. Calculate the frequency ($f$) of this light wave in vacuum ($c = 3{{,}}0 \\times 10^8\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$).\n"
        f"3. Calculate the photon energy ($E$) using $h = 6{{,}}63 \\times 10^{{-34}}\\text{{ J}}\\cdot\\text{{s}}$."
    )
    ans = (
        f"Sound is longitudinal/mechanical; Light is transverse/electromagnetic; "
        f"$f = {_fmt_sci(f_light)}\\text{{ Hz}},\\; E = {_fmt_sci(e_photon)}\\text{{ J}}$"
    )
    d1 = (
        f"Sound is transverse; Light is longitudinal; "
        f"$f = {_fmt_sci(f_light)}\\text{{ Hz}},\\; E = {_fmt_sci(e_photon)}\\text{{ J}}$"
    )
    d2 = (
        f"Sound is longitudinal/mechanical; Light is transverse/electromagnetic; "
        f"$f = {_fmt_sci(wlen_m / c_const)}\\text{{ Hz}},\\; E = {_fmt_sci(e_photon * 10)}\\text{{ J}}$"
    )
    d3 = (
        f"Both sound and light are transverse electromagnetic waves; "
        f"$f = {_fmt_sci(f_light)}\\text{{ Hz}},\\; E = {_fmt_sci(e_photon)}\\text{{ J}}$"
    )
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Classify sound and light waves", "op": "\\text{Sound: longitudinal mechanical; Light: transverse EM}", "to": "\\text{Classification affirmed}"},
        {"rule": "Calculate light frequency via c = f * lambda", "op": f"f = \\frac{{3{{,}}0 \\times 10^8}}{{{_fmt_sci(wlen_m)}}}", "to": f"{_fmt_sci(f_light)}\\text{{ Hz}}"},
        {"rule": "Calculate photon energy via E = h * f", "op": f"E = (6{{,}}63 \\times 10^{{-34}})({_fmt_sci(f_light)})", "to": f"{_fmt_sci(e_photon)}\\text{{ J}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Sound is a mechanical longitudinal wave requiring a medium. Light is an electromagnetic transverse wave that travels in vacuum.",
        t2="Calculate frequency using f = c / lambda, then use E = h * f to find photon energy.",
        t3=f"f = {_fmt_sci(f_light)} Hz and E = {_fmt_sci(e_photon)} J.",
        misconceptions=["confusing_nature_of_sound_and_light", "inverting_wave_equation_ratios"],
    )


# =========================================================================== #
# Export Mapping
# =========================================================================== #

BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_longitudinal_wave_definition_and_particle_motion": _build_26,
    "27_compressions_and_rarefactions_identification": _build_27,
    "28_longitudinal_wavelength_measurement": _build_28,
    "29_longitudinal_wave_equation_calculations": _build_29,
    "30_transverse_vs_longitudinal_wave_comparison": _build_30,
    "31_sound_wave_nature_and_medium_requirement": _build_31,
    "32_speed_of_sound_in_different_media": _build_32,
    "33_pitch_and_frequency_relationship": _build_33,
    "34_loudness_and_amplitude_relationship": _build_34,
    "35_sound_quality_timbre_and_waveform": _build_35,
    "36_human_audible_frequency_range_and_infrasound": _build_36,
    "37_echo_distance_and_reflection_time": _build_37,
    "38_speed_of_sound_determination_via_echo": _build_38,
    "39_marine_sonar_depth_sounding_calculation": _build_39,
    "40_medical_ultrasound_sonography_principles": _build_40,
    "41_industrial_ultrasound_flaw_detection": _build_41,
    "42_bat_echolocation_obstacle_avoidance": _build_42,
    "43_electromagnetic_radiation_wave_model_and_speed": _build_43,
    "44_electromagnetic_wave_equation_calculations": _build_44,
    "45_electromagnetic_spectrum_frequency_and_wavelength_ordering": _build_45,
    "46_electromagnetic_spectrum_applications": _build_46,
    "47_penetrating_ability_and_ionising_radiation_hazards": _build_47,
    "48_photon_energy_calculation_from_frequency": _build_48,
    "49_photon_energy_calculation_from_wavelength": _build_49,
    "50_waves_sound_light_diagnostic_synthesis": _build_50,
}

SUBSKILLS_26_50: List[str] = list(BUILDERS_26_50.keys())
