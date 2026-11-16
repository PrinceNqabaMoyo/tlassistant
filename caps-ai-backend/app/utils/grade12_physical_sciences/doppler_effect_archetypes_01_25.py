"""Grade 12 Physical Sciences - The Doppler Effect Archetypes 01 to 25.
Grounded in curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/04. The Doppler effect.md.

Covers:
  - Definition and physical basis of the Doppler Effect.
  - Stationary vs moving source wavefronts (compression ahead, rarefaction behind).
  - Observed wavelength: lambda' = (v - v_S) / f_S and (v + v_S) / f_S.
  - Doppler formula for moving source: f_L = (v / (v +- v_S)) * f_S.
  - Pitch drops when passing a stationary listener: Delta f = f_L(approach) - f_L(recede).
  - Solving for source speed v_S, source frequency f_S, or speed of sound v.
  - Ratio and percentage change in observed frequencies.
  - Moving listener with stationary source: f_L = ((v +- v_L) / v) * f_S.
  - General Doppler equation with both source and listener in motion.
  - Distinguishing loudness (amplitude) from pitch (frequency).
  - Seed-varied inline vector SVG wavefront diagram analysis.

Complies with 6-Pillar Generator Contract, 100% deterministic, zero LLM calls.
All numbers formatted with South African comma decimal convention.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple


def _fmt(val: float | int, decimals: int = 2) -> str:
    """Format float using South African comma decimal convention."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _make_q(
    r: random.Random,
    subskill_id: str,
    subskill_num: int,
    prompt: str,
    ans: str,
    sol: str,
    marks: int,
    misconceptions: List[str],
    marking_points: List[Dict[str, Any]],
    hints: Dict[str, str],
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    qid = f"gr12_doppler_{subskill_num:02d}_{r.randint(1000, 9999)}"
    q: Dict[str, Any] = {
        "id": qid,
        "question_id": qid,
        "subskill_id": subskill_id,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 9,
        "mode": "compound",
        "topic": "The Doppler effect",
        "question_type": "short_answer",
        "question": prompt,
        "prompt": prompt,
        "question_text": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [{"rule": "omitted_hz_or_ms_units", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


def _build_wavefront_svg(v_s: float, v: float, dir_str: str, seed: int) -> Dict[str, Any]:
    """Generates a seed-varied inline vector SVG showing Doppler wavefront compression."""
    # Scale center offset based on source speed ratio vs/v
    ratio = min(max(v_s / v, 0.05), 0.35)
    offset_step = 22 * ratio * (1 if dir_str == "right" else -1)
    cx, cy = 250, 150

    circles = []
    radii = [30, 60, 90, 120]
    for i, r_val in enumerate(radii):
        # Earlier wavefronts emitted further back
        c_x = cx - (len(radii) - 1 - i) * offset_step
        circles.append(
            f'<circle cx="{c_x:.1f}" cy="{cy}" r="{r_val}" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="none" />'
        )

    # Source dot and arrow
    source_x = cx
    arrow_end = source_x + (30 if dir_str == "right" else -30)
    obs_a_x = 420
    obs_b_x = 80

    svg_content = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 300" width="100%" height="auto" style="background:#f8fafc; border-radius:8px;">'
        f'<!-- seed:{seed} -->'
        f'<rect width="500" height="300" fill="#f8fafc" />'
        f'{"".join(circles)}'
        f'<circle cx="{source_x}" cy="{cy}" r="6" fill="#dc2626" />'
        f'<text x="{source_x}" y="{cy - 12}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">Source S (vs = {_fmt(v_s)} m·s⁻¹)</text>'
        f'<line x1="{source_x}" y1="{cy}" x2="{arrow_end}" y2="{cy}" stroke="#dc2626" stroke-width="3" marker-end="url(#arrow)" />'
        f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="#dc2626" />'
        f'</marker></defs>'
        f'<circle cx="{obs_a_x}" cy="{cy}" r="7" fill="#059669" />'
        f'<text x="{obs_a_x}" y="{cy - 12}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#059669" text-anchor="middle">Listener A</text>'
        f'<circle cx="{obs_b_x}" cy="{cy}" r="7" fill="#7c3aed" />'
        f'<text x="{obs_b_x}" y="{cy - 12}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#7c3aed" text-anchor="middle">Listener B</text>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "diagram_role": "context",
        "svg": svg_content,
        "width": 500,
        "height": 300,
    }


# =============================================================================
# Subskills 01–25 Builders
# =============================================================================

# 01. Definition and nature of Doppler effect
def build_01_definition_and_nature_of_doppler_effect(r: random.Random) -> Dict[str, Any]:
    ctx = r.choice(["an ambulance siren", "a commuter train horn", "a highway police patrol car"])
    prompt = (
        f"A learner investigating wave phenomena observes the pitch changes produced by {ctx}.\n\n"
        f"1. State the **Doppler Effect** in words.\n"
        f"2. Identify the fundamental condition necessary for the Doppler effect to occur.\n"
        f"3. State whether the actual frequency emitted by the source changes during relative motion."
    )
    ans = "1. Apparent change in frequency (or pitch) of a wave detected by an observer because the source and observer have different velocities relative to the medium; 2. Relative motion between source and observer; 3. No, the source frequency remains constant."
    sol = (
        "1. **Doppler Effect:** The apparent change in frequency (or pitch) of a wave detected by an observer "
        "because the source and the observer have different velocities relative to the medium of propagation.\n"
        "2. The essential condition is **relative motion** along the line connecting the source and the observer.\n"
        "3. The **actual source frequency ($f_S$) remains constant**; only the observed/detected frequency ($f_L$) changes."
    )
    return _make_q(
        r, "01_definition_and_nature_of_doppler_effect", 1, prompt, ans, sol, 4,
        ["thought_source_alters_its_vibration_rate_when_moving"],
        [{"step": 1, "criterion": "Definition of Doppler effect (apparent change in frequency)", "marks": 2}, {"step": 2, "criterion": "Relative motion between source and observer", "marks": 1}, {"step": 3, "criterion": "Actual frequency emitted is unchanged", "marks": 1}],
        {"tier_1": "The Doppler effect is an apparent change in frequency.", "tier_2": "Relative motion changes the detected rate of wavefronts, not the source's physical oscillation.", "tier_3": ans},
    )


# 02. Stationary source wavefronts wavelength and frequency
def build_02_stationary_source_wavefronts_wavelength_frequency(r: random.Random) -> Dict[str, Any]:
    fs = r.choice([250, 440, 500, 680, 850])
    v = r.choice([330.0, 340.0, 343.0])
    lam = round(v / fs, 3)
    prompt = (
        f"A stationary loudspeaker emits sound waves of frequency ${fs}\\text{{ Hz}}$ into still air "
        f"where the speed of sound is ${_fmt(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Describe the spatial shape and spacing of the wavefronts produced around the stationary loudspeaker.\n"
        f"2. Calculate the wavelength ($\\lambda$) of the sound waves in meters."
    )
    ans = f"Concentric spheres/circles with uniform spacing; lambda = {_fmt(lam)} m"
    sol = (
        f"1. The wavefronts form **concentric circles** (or spheres in 3D) centred on the loudspeaker, "
        f"with identical, uniform spacing in all directions.\n"
        f"2. Using the wave equation $v = f\\lambda$:\n"
        f"   $$\\lambda = \\frac{{v}}{{f_S}} = \\frac{{{_fmt(v)}}}{{{fs}}} = {_fmt(lam)}\\text{{ m}}$$"
    )
    return _make_q(
        r, "02_stationary_source_wavefronts_wavelength_frequency", 2, prompt, ans, sol, 3,
        ["inverted_wave_equation_wavelength_frequency"],
        [{"step": 1, "criterion": "Concentric circles with uniform radial spacing", "marks": 1}, {"step": 2, "criterion": "Formula v = f * lambda", "marks": 1}, {"step": 3, "criterion": f"Wavelength = {_fmt(lam)} m", "marks": 1}],
        {"tier_1": "Recall the wave speed equation: v = f * lambda.", "tier_2": f"lambda = {_fmt(v)} / {fs}.", "tier_3": ans},
    )


# 03. Wavefront compression approaching source mechanism
def build_03_wavefront_compression_approaching_source_mechanism(r: random.Random) -> Dict[str, Any]:
    veh = r.choice(["A police cruiser", "An emergency medical vehicle", "A diesel locomotive"])
    prompt = (
        f"{veh} sounding its siren approaches a stationary pedestrian standing on a pavement.\n\n"
        f"Explain in terms of **wavefronts, wavelength, and wave speed** why the pedestrian hears a sound of **higher pitch** than that emitted by the siren."
    )
    ans = "As the source moves forward, each successive wavefront is emitted closer to the previous wavefront in the direction of motion. This compresses the wavefronts, decreasing the observed wavelength. Since wave speed in air is constant, the decreased wavelength causes a higher frequency (pitch) according to v = f*lambda."
    sol = (
        "1. As the source moves towards the observer, each successive crest is emitted from a position closer "
        "to the previous crest in the forward direction.\n"
        "2. This **compresses the wavefronts** ahead of the source, resulting in a **shorter observed wavelength** ($\\lambda_L < \\lambda_S$).\n"
        "3. Since the **speed of sound ($v$) in the medium is constant**, the shorter wavelength causes the observer "
        "to intercept more wave crests per second, resulting in a **higher observed frequency** ($f_L > f_S$) and therefore higher pitch ($v = f_L \\lambda_L$)."
    )
    return _make_q(
        r, "03_wavefront_compression_approaching_source_mechanism", 3, prompt, ans, sol, 4,
        ["claimed_wave_speed_in_air_increases_due_to_vehicle_motion"],
        [{"step": 1, "criterion": "Successive crests emitted closer together in forward direction", "marks": 1}, {"step": 2, "criterion": "Wavefronts compressed / wavelength decreases ahead", "marks": 1}, {"step": 3, "criterion": "Speed of sound in air remains constant", "marks": 1}, {"step": 4, "criterion": "Higher frequency (pitch) according to v = f * lambda", "marks": 1}],
        {"tier_1": "Think about where each crest is emitted relative to the previous one.", "tier_2": "Wavelength ahead decreases while wave speed in air stays constant.", "tier_3": ans},
    )


# 04. Wavefront stretching receding source mechanism
def build_04_wavefront_stretching_receding_source_mechanism(r: random.Random) -> Dict[str, Any]:
    veh = r.choice(["A fire engine", "A commuter train", "A rapid response vehicle"])
    prompt = (
        f"{veh} sounding its siren drives directly away from a stationary observer at a steady speed.\n\n"
        f"Explain in terms of **wavefronts and wavelength** why the observer detects a sound of **lower pitch** than that emitted by the source."
    )
    ans = "As the source moves away, each successive wavefront is emitted further behind the previous one. This stretches the wavefronts, increasing the observed wavelength. Since sound speed in air is constant, the longer wavelength results in a lower observed frequency and lower pitch."
    sol = (
        "1. As the source travels away from the observer, each successive crest is emitted from a location "
        "further away from the observer than the preceding crest.\n"
        "2. This **stretches the wavefronts** behind the source, producing a **longer observed wavelength** ($\\lambda_L > \\lambda_S$).\n"
        "3. Because sound speed $v$ in air is constant, the longer wavelength means fewer crests reach the observer per second, "
        "giving a **lower observed frequency** ($f_L < f_S$) and lower pitch ($f = v / \\lambda$)."
    )
    return _make_q(
        r, "04_wavefront_stretching_receding_source_mechanism", 4, prompt, ans, sol, 3,
        ["assumed_amplitude_decrease_is_the_cause_of_lower_pitch"],
        [{"step": 1, "criterion": "Successive crests emitted further apart behind source", "marks": 1}, {"step": 2, "criterion": "Observed wavelength increases (wavefronts stretched)", "marks": 1}, {"step": 3, "criterion": "Constant wave speed leads to lower frequency / lower pitch", "marks": 1}],
        {"tier_1": "Behind the moving source, crests are spaced further apart.", "tier_2": "Wavelength increases, so frequency must decrease because wave speed is constant.", "tier_3": ans},
    )


# 05. Apparent wavelength ahead of approaching source
def build_05_apparent_wavelength_ahead_of_approaching_source(r: random.Random) -> Dict[str, Any]:
    fs = r.choice([400, 500, 600, 800])
    vs = r.choice([20.0, 25.0, 30.0, 34.0])
    v = 340.0
    lam_ahead = round((v - vs) / fs, 4)
    lam_orig = round(v / fs, 4)

    prompt = (
        f"A sound source emits a tone of frequency ${fs}\\text{{ Hz}}$ while travelling east at "
        f"${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ towards a stationary observer. "
        f"Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Calculate the wavelength ($\\lambda_S$) of the sound when the source is at rest.\n"
        f"2. Calculate the compressed apparent wavelength ($\\lambda_L$) detected ahead of the moving source."
    )
    ans = f"lambda_S = {_fmt(lam_orig)} m; lambda_L = {_fmt(lam_ahead)} m"
    sol = (
        f"1. At rest: $$\\lambda_S = \\frac{{v}}{{f_S}} = \\frac{{{v}}}{{{fs}}} = {_fmt(lam_orig)}\\text{{ m}}$$\n"
        f"2. Ahead of the approaching source, the source travels a distance $v_S T = v_S / f_S$ between crests:\n"
        f"   $$\\lambda_L = \\frac{{v - v_S}}{{f_S}} = \\frac{{{v} - {_fmt(vs)}}}{{{fs}}} = \\frac{{{_fmt(v - vs)}}}{{{fs}}} = {_fmt(lam_ahead)}\\text{{ m}}$$"
    )
    return _make_q(
        r, "05_apparent_wavelength_ahead_of_approaching_source", 5, prompt, ans, sol, 4,
        ["added_source_speed_instead_of_subtracting_for_approaching_wavelength"],
        [{"step": 1, "criterion": f"Rest wavelength = {_fmt(lam_orig)} m", "marks": 1}, {"step": 2, "criterion": "Formula lambda_L = (v - v_S) / f_S", "marks": 1}, {"step": 3, "criterion": "Substitution", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(lam_ahead)} m", "marks": 1}],
        {"tier_1": "Ahead of the source, wavelength is shortened: lambda' = (v - vs) / f.", "tier_2": f"Subtract source speed from sound speed: ({v} - {vs}) / {fs}.", "tier_3": ans},
    )


# 06. Apparent wavelength behind receding source
def build_06_apparent_wavelength_behind_receding_source(r: random.Random) -> Dict[str, Any]:
    fs = r.choice([350, 450, 550, 700])
    vs = r.choice([22.0, 26.0, 30.0, 35.0])
    v = 340.0
    lam_behind = round((v + vs) / fs, 4)

    prompt = (
        f"A siren of frequency ${fs}\\text{{ Hz}}$ moves away from a stationary observer at "
        f"${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the stretched apparent wavelength ($\\lambda_L$) of the sound waves behind the receding siren in meters."
    )
    ans = f"{_fmt(lam_behind)} m"
    sol = (
        f"Behind a receding source, the distance between crests is stretched by the source's motion:\n"
        f"$$\\lambda_L = \\frac{{v + v_S}}{{f_S}} = \\frac{{{v} + {_fmt(vs)}}}{{{fs}}} = \\frac{{{_fmt(v + vs)}}}{{{fs}}} = {_fmt(lam_behind)}\\text{{ m}}$$"
    )
    return _make_q(
        r, "06_apparent_wavelength_behind_receding_source", 6, prompt, ans, sol, 3,
        ["used_subtraction_for_receding_wavelength"],
        [{"step": 1, "criterion": "Formula lambda_L = (v + v_S) / f_S", "marks": 1}, {"step": 2, "criterion": f"Substitution ({v} + {_fmt(vs)}) / {fs}", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(lam_behind)} m", "marks": 1}],
        {"tier_1": "Behind the source, wavefronts are further apart: lambda' = (v + vs) / f.", "tier_2": f"Add source speed to sound speed: ({v} + {vs}) / {fs}.", "tier_3": ans},
    )


# 07. Doppler formula moving source approaching stationary listener
def build_07_doppler_formula_moving_source_approaching_stationary_listener(r: random.Random) -> Dict[str, Any]:
    veh = r.choice(["an ambulance", "a traffic patrol car", "a fire truck"])
    vs = r.choice([20.0, 25.0, 28.0, 32.0, 35.0])
    fs = r.choice([600, 750, 800, 900])
    v = 340.0
    fl = round((v / (v - vs)) * fs, 2)

    prompt = (
        f"{veh.capitalize()} moves along a straight level road at a constant speed of ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"towards a stationary listener. The siren emits sound waves with a frequency of ${fs}\\text{{ Hz}}$. "
        f"Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Write down the Doppler formula applicable when a source moves towards a stationary listener ($v_L = 0$).\n"
        f"2. Calculate the frequency ($f_L$) detected by the stationary listener."
    )
    ans = f"fL = {_fmt(fl)} Hz"
    sol = (
        f"1. General formula: $f_L = \\left(\\frac{{v \\pm v_L}}{{v \\mp v_S}}\\right) f_S$\n"
        f"   For moving source approaching stationary listener ($v_L = 0$ and denominator $- v_S$):\n"
        f"   $$f_L = \\left(\\frac{{v}}{{v - v_S}}\\right) f_S$$\n"
        f"2. Calculation:\n"
        f"   $$f_L = \\left(\\frac{{{v}}}{{{v} - {_fmt(vs)}}}\\right) ({fs}) = \\left(\\frac{{{v}}}{{{_fmt(v - vs)}}}\\right) ({fs}) = {_fmt(fl)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "07_doppler_formula_moving_source_approaching_stationary_listener", 7, prompt, ans, sol, 4,
        ["used_plus_sign_in_denominator_for_approaching_source"],
        [{"step": 1, "criterion": "Formula fL = (v / (v - vS)) * fS", "marks": 1}, {"step": 2, "criterion": f"Substitution ({v} / ({v} - {_fmt(vs)})) * {fs}", "marks": 2}, {"step": 3, "criterion": f"Answer {_fmt(fl)} Hz", "marks": 1}],
        {"tier_1": "Approaching source means higher observed frequency, so use (v - vs) in denominator.", "tier_2": f"fL = ({v} / ({v} - {vs})) * {fs}.", "tier_3": ans},
    )


# 08. Doppler formula moving source receding from stationary listener
def build_08_doppler_formula_moving_source_receding_from_stationary_listener(r: random.Random) -> Dict[str, Any]:
    veh = r.choice(["A high-speed train", "A police cruiser", "A rescue helicopter"])
    vs = r.choice([24.0, 30.0, 36.0, 40.0])
    fs = r.choice([500, 650, 720, 850])
    v = 340.0
    fl = round((v / (v + vs)) * fs, 2)

    prompt = (
        f"{veh} sounding a horn at ${fs}\\text{{ Hz}}$ moves directly away from a stationary observer at "
        f"${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the frequency detected by the stationary observer as the source recedes."
    )
    ans = f"{_fmt(fl)} Hz"
    sol = (
        f"$$f_L = \\left(\\frac{{v}}{{v + v_S}}\\right) f_S$$\n"
        f"$$f_L = \\left(\\frac{{{v}}}{{{v} + {_fmt(vs)}}}\\right) ({fs}) = \\left(\\frac{{{v}}}{{{_fmt(v + vs)}}}\\right) ({fs}) = {_fmt(fl)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "08_doppler_formula_moving_source_receding_from_stationary_listener", 8, prompt, ans, sol, 3,
        ["used_minus_sign_in_denominator_for_receding_source"],
        [{"step": 1, "criterion": "Formula fL = (v / (v + vS)) * fS", "marks": 1}, {"step": 2, "criterion": f"Substitution ({v} / ({v} + {_fmt(vs)})) * {fs}", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(fl)} Hz", "marks": 1}],
        {"tier_1": "Receding source means lower frequency, so denominator is (v + vs).", "tier_2": f"fL = ({v} / ({v} + {vs})) * {fs}.", "tier_3": ans},
    )


# 09. Approaching and then receding pitch drop
def build_09_approaching_and_then_receding_pitch_drop(r: random.Random) -> Dict[str, Any]:
    vs = r.choice([25.0, 30.0, 35.0])
    fs = r.choice([500, 600, 800])
    v = 340.0
    fl_app = round((v / (v - vs)) * fs, 2)
    fl_rec = round((v / (v + vs)) * fs, 2)
    delta_f = round(fl_app - fl_rec, 2)

    prompt = (
        f"A patrol car emits a siren frequency of ${fs}\\text{{ Hz}}$ while travelling past a stationary bystander "
        f"at a constant speed of ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Take the speed of sound as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Calculate the frequency heard by the bystander as the patrol car approaches.\n"
        f"2. Calculate the frequency heard by the bystander after the car has passed and recedes.\n"
        f"3. Calculate the total sudden drop in pitch ($\\Delta f = f_{{L,\\text{{approach}}}} - f_{{L,\\text{{recede}}}}$) perceived by the bystander."
    )
    ans = f"fL_app = {_fmt(fl_app)} Hz; fL_rec = {_fmt(fl_rec)} Hz; Delta f = {_fmt(delta_f)} Hz"
    sol = (
        f"1. Approaching: $$f_{{L,\\text{{app}}}} = \\left(\\frac{{{v}}}{{{v} - {_fmt(vs)}}}\\right) ({fs}) = {_fmt(fl_app)}\\text{{ Hz}}$$\n"
        f"2. Receding: $$f_{{L,\\text{{rec}}}} = \\left(\\frac{{{v}}}{{{v} + {_fmt(vs)}}}\\right) ({fs}) = {_fmt(fl_rec)}\\text{{ Hz}}$$\n"
        f"3. Drop in pitch: $$\\Delta f = {_fmt(fl_app)} - {_fmt(fl_rec)} = {_fmt(delta_f)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "09_approaching_and_then_receding_pitch_drop", 9, prompt, ans, sol, 5,
        ["forgot_to_compute_difference_delta_f"],
        [{"step": 1, "criterion": f"Approach frequency = {_fmt(fl_app)} Hz", "marks": 2}, {"step": 2, "criterion": f"Recede frequency = {_fmt(fl_rec)} Hz", "marks": 2}, {"step": 3, "criterion": f"Pitch drop = {_fmt(delta_f)} Hz", "marks": 1}],
        {"tier_1": "Calculate approaching frequency with (v - vs) and receding frequency with (v + vs).", "tier_2": "Subtract the receding frequency from the approaching frequency.", "tier_3": ans},
    )


# 10. Solving for source speed from detected frequency approaching
def build_10_solving_for_source_speed_from_detected_frequency_approaching(r: random.Random) -> Dict[str, Any]:
    fs = r.choice([400, 500, 600, 800])
    vs_exact = r.choice([20.0, 25.0, 30.0, 32.0, 35.0])
    v = 340.0
    fl = round((v / (v - vs_exact)) * fs, 2)

    prompt = (
        f"A train sounds its whistle of frequency ${fs}\\text{{ Hz}}$ as it approaches a level crossing. "
        f"A stationary monitor at the crossing records a frequency of ${_fmt(fl)}\\text{{ Hz}}$. "
        f"Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the speed ($v_S$) of the approaching train."
    )
    ans = f"{_fmt(vs_exact)} m·s⁻¹"
    sol = (
        f"$$f_L = \\left(\\frac{{v}}{{v - v_S}}\\right) f_S$$\n"
        f"$${_fmt(fl)} = \\left(\\frac{{{v}}}{{{v} - v_S}}\\right) ({fs})$$\n"
        f"$${_fmt(fl)} ({v} - v_S) = {v} \\times {fs}$$\n"
        f"$${v} - v_S = \\frac{{{v} \\times {fs}}}{{{_fmt(fl)}}} = {_fmt((v * fs) / fl, 2)}$$\n"
        f"$$v_S = {v} - {_fmt((v * fs) / fl, 2)} = {_fmt(vs_exact)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "10_solving_for_source_speed_from_detected_frequency_approaching", 10, prompt, ans, sol, 4,
        ["algebraic_inversion_error_when_solving_for_vS"],
        [{"step": 1, "criterion": "Formula fL = (v / (v - vS)) * fS", "marks": 1}, {"step": 2, "criterion": "Substitution of known values", "marks": 1}, {"step": 3, "criterion": "Algebraic rearrangement isolating vS", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(vs_exact)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Rearrange fL = [v / (v - vS)] * fS to isolate vS.", "tier_2": "v - vS = (v * fS) / fL, then vS = v - (v * fS) / fL.", "tier_3": ans},
    )


# 11. Solving for source speed from detected frequency receding
def build_11_solving_for_source_speed_from_detected_frequency_receding(r: random.Random) -> Dict[str, Any]:
    fs = r.choice([550, 700, 850])
    vs_exact = r.choice([20.0, 24.0, 28.0, 32.0])
    v = 340.0
    fl = round((v / (v + vs_exact)) * fs, 2)

    prompt = (
        f"An emergency vehicle moves away from a stationary microphone. The vehicle's siren has a known frequency "
        f"of ${fs}\\text{{ Hz}}$, but the microphone records a frequency of ${_fmt(fl)}\\text{{ Hz}}$. "
        f"Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the speed ($v_S$) at which the emergency vehicle is receding."
    )
    ans = f"{_fmt(vs_exact)} m·s⁻¹"
    sol = (
        f"$$f_L = \\left(\\frac{{v}}{{v + v_S}}\\right) f_S$$\n"
        f"$${_fmt(fl)} = \\left(\\frac{{{v}}}{{{v} + v_S}}\\right) ({fs})$$\n"
        f"$${v} + v_S = \\frac{{{v} \\times {fs}}}{{{_fmt(fl)}}} = {_fmt((v * fs) / fl, 2)}$$\n"
        f"$$v_S = {_fmt((v * fs) / fl, 2)} - {v} = {_fmt(vs_exact)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "11_solving_for_source_speed_from_detected_frequency_receding", 11, prompt, ans, sol, 4,
        ["sign_error_solving_receding_source_velocity"],
        [{"step": 1, "criterion": "Formula fL = (v / (v + vS)) * fS", "marks": 1}, {"step": 2, "criterion": "Correct substitution", "marks": 1}, {"step": 3, "criterion": "Correct algebraic rearrangement", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(vs_exact)} m·s⁻¹", "marks": 1}],
        {"tier_1": "For receding source: fL = [v / (v + vS)] * fS.", "tier_2": "v + vS = (v * fS) / fL, then vS = (v * fS) / fL - v.", "tier_3": ans},
    )


# 12. Solving for source frequency from detected frequency
def build_12_solving_for_source_frequency_from_detected_frequency(r: random.Random) -> Dict[str, Any]:
    fs_exact = r.choice([380, 480, 560, 640, 750])
    vs = r.choice([18.0, 22.0, 26.0, 30.0])
    v = 340.0
    fl = round((v / (v - vs)) * fs_exact, 2)

    prompt = (
        f"A motorcycle travelling at ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ towards a stationary observer "
        f"emits a steady tone. The observer detects a frequency of ${_fmt(fl)}\\text{{ Hz}}$. "
        f"Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the actual frequency ($f_S$) emitted by the motorcycle's horn."
    )
    ans = f"{fs_exact} Hz"
    sol = (
        f"$$f_L = \\left(\\frac{{v}}{{v - v_S}}\\right) f_S$$\n"
        f"$$f_S = f_L \\left(\\frac{{v - v_S}}{{v}}\\right)$$\n"
        f"$$f_S = {_fmt(fl)} \\left(\\frac{{{v} - {_fmt(vs)}}}{{{v}}}\\right) = {_fmt(fl)} \\left(\\frac{{{_fmt(v - vs)}}}{{{v}}}\\right) = {fs_exact}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "12_solving_for_source_frequency_from_detected_frequency", 12, prompt, ans, sol, 3,
        ["inverted_formula_when_solving_for_source_frequency"],
        [{"step": 1, "criterion": "Formula fL = (v / (v - vS)) * fS", "marks": 1}, {"step": 2, "criterion": "Substitution of fL, v, vS", "marks": 1}, {"step": 3, "criterion": f"Answer {fs_exact} Hz", "marks": 1}],
        {"tier_1": "Isolate fS: fS = fL * (v - vS) / v.", "tier_2": f"Multiply {fl} by ({v} - {vs}) / {v}.", "tier_3": ans},
    )


# 13. Solving for speed of sound in gas or air
def build_13_solving_for_speed_of_sound_in_gas_or_air(r: random.Random) -> Dict[str, Any]:
    v_exact = r.choice([320.0, 330.0, 340.0, 350.0])
    vs = r.choice([25.0, 30.0, 35.0])
    fs = 400
    fl = round((v_exact / (v_exact - vs)) * fs, 2)

    prompt = (
        f"In an acoustics experiment in a gas chamber, a sound source of frequency ${fs}\\text{{ Hz}}$ moves towards a stationary detector "
        f"at a velocity of ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. The detector measures a frequency of ${_fmt(fl)}\\text{{ Hz}}$.\n\n"
        f"Calculate the speed of sound ($v$) in the gas."
    )
    ans = f"{_fmt(v_exact)} m·s⁻¹"
    sol = (
        f"$$f_L = \\left(\\frac{{v}}{{v - v_S}}\\right) f_S$$\n"
        f"$${_fmt(fl)} (v - {_fmt(vs)}) = v \\times {fs}$$\n"
        f"$${_fmt(fl)} v - {_fmt(fl * vs, 2)} = {fs} v$$\n"
        f"$$({_fmt(fl)} - {fs}) v = {_fmt(fl * vs, 2)}$$\n"
        f"$$v = \\frac{{{_fmt(fl * vs, 2)}}}{{{_fmt(fl - fs, 2)}}} = {_fmt(v_exact)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "13_solving_for_speed_of_sound_in_gas_or_air", 13, prompt, ans, sol, 4,
        ["failed_to_collect_like_terms_when_solving_for_wave_speed"],
        [{"step": 1, "criterion": "Doppler equation stated", "marks": 1}, {"step": 2, "criterion": "Correct substitution", "marks": 1}, {"step": 3, "criterion": "Expanding and grouping v terms", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(v_exact)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Substitute into fL * (v - vS) = v * fS and solve for v.", "tier_2": "Group terms: v * (fL - fS) = fL * vS.", "tier_3": ans},
    )


# 14. Ratio of observed frequencies approach to recede
def build_14_ratio_of_observed_frequencies_approach_to_recede(r: random.Random) -> Dict[str, Any]:
    vs = r.choice([20.0, 25.0, 30.0, 34.0])
    v = 340.0
    ratio = round((v + vs) / (v - vs), 3)

    prompt = (
        f"A race car sounding its engine at constant frequency approaches and then recedes from a trackside spectator.\n"
        f"The speed of sound in air is ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, and the ratio of the frequency heard during approach "
        f"to that heard during recession is $R = \\frac{{f_{{L,\\text{{approach}}}}}}{{f_{{L,\\text{{recede}}}}}} = {_fmt(ratio)}$.\n\n"
        f"1. Show that the frequency ratio is given by $R = \\frac{{v + v_S}}{{v - v_S}}$.\n"
        f"2. Calculate the speed ($v_S$) of the race car."
    )
    ans = f"R = (v + vS) / (v - vS); vS = {_fmt(vs)} m·s⁻¹"
    sol = (
        f"1. Approach: $f_{{L1}} = \\frac{{v}}{{v - v_S}} f_S$\n"
        f"   Recede: $f_{{L2}} = \\frac{{v}}{{v + v_S}} f_S$\n"
        f"   Ratio: $R = \\frac{{f_{{L1}}}}{{f_{{L2}}}} = \\frac{{v / (v - v_S)}}{{v / (v + v_S)}} = \\frac{{v + v_S}}{{v - v_S}}$\n"
        f"2. Solve for $v_S$:\n"
        f"   $$R(v - v_S) = v + v_S \\implies R v - R v_S = v + v_S \\implies (R + 1) v_S = (R - 1) v$$\n"
        f"   $$v_S = v \\left(\\frac{{R - 1}}{{R + 1}}\\right) = {v} \\left(\\frac{{{_fmt(ratio)} - 1}}{{{_fmt(ratio)} + 1}}\\right) = {_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "14_ratio_of_observed_frequencies_approach_to_recede", 14, prompt, ans, sol, 5,
        ["inverted_the_frequency_ratio_terms"],
        [{"step": 1, "criterion": "Derivation of R = (v + vS)/(v - vS)", "marks": 2}, {"step": 2, "criterion": "Formula vS = v * (R - 1)/(R + 1)", "marks": 1}, {"step": 3, "criterion": "Substitution of R and v", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(vs)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Divide the two Doppler equations to eliminate source frequency fS.", "tier_2": "Solve for vS = v * (R - 1) / (R + 1).", "tier_3": ans},
    )


# 15. Percentage change in observed frequency approach
def build_15_percentage_change_in_observed_frequency_approach(r: random.Random) -> Dict[str, Any]:
    fs = 500
    vs = r.choice([17.0, 20.0, 25.0, 30.0, 34.0])
    v = 340.0
    fl = round((v / (v - vs)) * fs, 2)
    pct = round(((fl - fs) / fs) * 100.0, 2)

    prompt = (
        f"A vehicle sounding its horn of frequency ${fs}\\text{{ Hz}}$ approaches a stationary listener at "
        f"${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Take the speed of sound as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Calculate the frequency ($f_L$) detected by the listener.\n"
        f"2. Calculate the percentage increase in the detected frequency relative to the emitted frequency."
    )
    ans = f"fL = {_fmt(fl)} Hz; Increase = {_fmt(pct)}%"
    sol = (
        f"1. $$f_L = \\left(\\frac{{{v}}}{{{v} - {_fmt(vs)}}}\\right) ({fs}) = {_fmt(fl)}\\text{{ Hz}}$$\n"
        f"2. $$\\text{{Percentage Increase}} = \\frac{{f_L - f_S}}{{f_S}} \\times 100\\% = \\frac{{{_fmt(fl)} - {fs}}}{{{fs}}} \\times 100\\% = {_fmt(pct)}\\%$$"
    )
    return _make_q(
        r, "15_percentage_change_in_observed_frequency_approach", 15, prompt, ans, sol, 4,
        ["divided_by_fL_instead_of_fS_for_percentage_change"],
        [{"step": 1, "criterion": f"Observed frequency = {_fmt(fl)} Hz", "marks": 2}, {"step": 2, "criterion": "Formula (fL - fS) / fS * 100%", "marks": 1}, {"step": 3, "criterion": f"Percentage increase = {_fmt(pct)}%", "marks": 1}],
        {"tier_1": "Find fL first, then calculate (fL - fS) / fS * 100.", "tier_2": "Always divide by the original emitted frequency fS.", "tier_3": ans},
    )


# 16. Percentage change in observed frequency receding
def build_16_percentage_change_in_observed_frequency_receding(r: random.Random) -> Dict[str, Any]:
    fs = 600
    vs = r.choice([20.0, 25.0, 30.0, 34.0])
    v = 340.0
    fl = round((v / (v + vs)) * fs, 2)
    pct = round(((fs - fl) / fs) * 100.0, 2)

    prompt = (
        f"An emergency siren of frequency ${fs}\\text{{ Hz}}$ travels away from a stationary monitor at "
        f"${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Take the speed of sound as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the percentage decrease in the frequency detected by the monitor relative to the emitted frequency."
    )
    ans = f"{_fmt(pct)}%"
    sol = (
        f"$$f_L = \\left(\\frac{{{v}}}{{{v} + {_fmt(vs)}}}\\right) ({fs}) = {_fmt(fl)}\\text{{ Hz}}$$\n"
        f"$$\\text{{Percentage Decrease}} = \\frac{{f_S - f_L}}{{f_S}} \\times 100\\% = \\frac{{{fs} - {_fmt(fl)}}}{{{fs}}} \\times 100\\% = {_fmt(pct)}\\%$$"
    )
    return _make_q(
        r, "16_percentage_change_in_observed_frequency_receding", 16, prompt, ans, sol, 3,
        ["treated_decrease_as_negative_without_stating_decrease"],
        [{"step": 1, "criterion": f"Receding frequency = {_fmt(fl)} Hz", "marks": 1}, {"step": 2, "criterion": "Percentage decrease calculation", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(pct)}%", "marks": 1}],
        {"tier_1": "Calculate fL for receding source with (v + vs).", "tier_2": "Percentage decrease is (fS - fL) / fS * 100.", "tier_3": ans},
    )


# 17. Stationary source moving listener approaching
def build_17_stationary_source_moving_listener_approaching(r: random.Random) -> Dict[str, Any]:
    fs = r.choice([440, 500, 680, 800])
    vl = r.choice([10.0, 15.0, 20.0, 25.0])
    v = 340.0
    fl = round(((v + vl) / v) * fs, 2)

    prompt = (
        f"A stationary factory siren sounds at ${fs}\\text{{ Hz}}$. A cyclist pedals towards the factory at "
        f"a steady speed of ${_fmt(vl)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. State whether the wavelength of the sound waves in the air is altered by the cyclist's motion.\n"
        f"2. Calculate the frequency ($f_L$) heard by the cyclist."
    )
    ans = f"Wavelength in air is unchanged; fL = {_fmt(fl)} Hz"
    sol = (
        f"1. The **wavelength in air is not changed** (it depends only on the stationary source: $\\lambda = v / f_S$). "
        f"The cyclist hears a higher frequency because they intercept more wavefronts per second due to their own motion.\n"
        f"2. Using the Doppler formula for a moving listener approaching a stationary source ($v_S = 0$):\n"
        f"   $$f_L = \\left(\\frac{{v + v_L}}{{v}}\\right) f_S = \\left(\\frac{{{v} + {_fmt(vl)}}}{{{v}}}\\right) ({fs}) = \\left(\\frac{{{_fmt(v + vl)}}}{{{v}}}\\right) ({fs}) = {_fmt(fl)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "17_stationary_source_moving_listener_approaching", 17, prompt, ans, sol, 4,
        ["assumed_wavelength_in_medium_changes_when_observer_moves"],
        [{"step": 1, "criterion": "Wavelength in air is unchanged", "marks": 1}, {"step": 2, "criterion": "Formula fL = ((v + vL) / v) * fS", "marks": 1}, {"step": 3, "criterion": "Substitution", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(fl)} Hz", "marks": 1}],
        {"tier_1": "For a moving listener, vL is in the numerator: fL = [(v + vL) / v] * fS.", "tier_2": "The source is stationary, so the wavelength in the air remains constant.", "tier_3": ans},
    )


# 18. Stationary source moving listener receding
def build_18_stationary_source_moving_listener_receding(r: random.Random) -> Dict[str, Any]:
    fs = r.choice([520, 600, 750, 900])
    vl = r.choice([12.0, 16.0, 20.0, 24.0])
    v = 340.0
    fl = round(((v - vl) / v) * fs, 2)

    prompt = (
        f"A motorist drives away from a stationary church bell ringing at ${fs}\\text{{ Hz}}$ at a speed of "
        f"${_fmt(vl)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the frequency detected by the motorist."
    )
    ans = f"{_fmt(fl)} Hz"
    sol = (
        f"$$f_L = \\left(\\frac{{v - v_L}}{{v}}\\right) f_S = \\left(\\frac{{{v} - {_fmt(vl)}}}{{{v}}}\\right) ({fs}) = \\left(\\frac{{{_fmt(v - vl)}}}{{{v}}}\\right) ({fs}) = {_fmt(fl)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "18_stationary_source_moving_listener_receding", 18, prompt, ans, sol, 3,
        ["used_plus_sign_in_numerator_for_receding_listener"],
        [{"step": 1, "criterion": "Formula fL = ((v - vL) / v) * fS", "marks": 1}, {"step": 2, "criterion": "Substitution", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(fl)} Hz", "marks": 1}],
        {"tier_1": "Listener moving away hears lower pitch: fL = [(v - vL) / v] * fS.", "tier_2": f"Subtract listener speed in numerator: ({v} - {vl}) / {v} * {fs}.", "tier_3": ans},
    )


# 19. Solving for listener speed approaching or receding
def build_19_solving_for_listener_speed_approaching_or_receding(r: random.Random) -> Dict[str, Any]:
    fs = 450
    vl_exact = r.choice([15.0, 20.0, 25.0, 30.0])
    v = 340.0
    fl = round(((v + vl_exact) / v) * fs, 2)

    prompt = (
        f"A car drives towards a stationary acoustic beacon emitting sound at ${fs}\\text{{ Hz}}$. "
        f"The driver detects a frequency of ${_fmt(fl)}\\text{{ Hz}}$. Take the speed of sound as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the speed ($v_L$) of the car."
    )
    ans = f"{_fmt(vl_exact)} m·s⁻¹"
    sol = (
        f"$$f_L = \\left(\\frac{{v + v_L}}{{v}}\\right) f_S$$\n"
        f"$${_fmt(fl)} = \\left(\\frac{{{v} + v_L}}{{{v}}}\\right) ({fs})$$\n"
        f"$${v} + v_L = \\frac{{{_fmt(fl)} \\times {v}}}{{{fs}}} = {_fmt((fl * v) / fs, 2)}$$\n"
        f"$$v_L = {_fmt((fl * v) / fs, 2)} - {v} = {_fmt(vl_exact)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "19_solving_for_listener_speed_approaching_or_receding", 19, prompt, ans, sol, 3,
        ["confused_numerator_vL_with_denominator_vS"],
        [{"step": 1, "criterion": "Formula fL = ((v + vL) / v) * fS", "marks": 1}, {"step": 2, "criterion": "Substitution and rearrangement", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(vl_exact)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Remember listener speed vL is in the numerator.", "tier_2": "vL = (fL / fS) * v - v.", "tier_3": ans},
    )


# 20. Comparison between moving source vs moving listener
def build_20_comparison_between_moving_source_vs_moving_listener(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Compare the physical mechanism of the Doppler effect in the following two cases:\n"
        "**Case A:** A sound source moves at speed $u$ towards a stationary listener.\n"
        "**Case B:** A listener moves at the same speed $u$ towards a stationary sound source.\n\n"
        "1. For each case, state whether the wavelength of the sound waves in the air is changed or unchanged.\n"
        "2. Explain why the two cases produce slightly different observed frequencies even when $u$ is identical."
    )
    ans = "Case A: wavelength in air is compressed/shortened. Case B: wavelength in air is unchanged. The frequencies differ because Case A changes the physical wavelength in the medium (fL = v/(v - u) * fS), while Case B changes the rate at which wavefronts are intercepted by the listener (fL = (v + u)/v * fS)."
    sol = (
        "1. **Wavelength comparison:**\n"
        "   - **Case A (Moving source):** The wavelength in the air is **compressed / shortened** ($\\lambda_L = (v - u)/f_S$).\n"
        "   - **Case B (Moving listener):** The wavelength in the air is **unchanged** ($\\lambda_L = v/f_S$).\n"
        "2. **Frequency difference explanation:**\n"
        "   - In Case A, $f_L = \\frac{v}{v - u} f_S$.\n"
        "   - In Case B, $f_L = \\frac{v + u}{v} f_S = \\left(1 + \\frac{u}{v}\\right) f_S$.\n"
        "   - Since $\\frac{1}{1 - u/v} > 1 + u/v$ for any $u > 0$, the moving source produces a slightly higher frequency shift "
        "than the moving listener at the same speed."
    )
    return _make_q(
        r, "20_comparison_between_moving_source_vs_moving_listener", 20, prompt, ans, sol, 4,
        ["assumed_moving_source_and_moving_listener_are_mechanically_identical"],
        [{"step": 1, "criterion": "Case A wavelength is compressed", "marks": 1}, {"step": 2, "criterion": "Case B wavelength is unchanged", "marks": 1}, {"step": 3, "criterion": "Formulas compared fL = v/(v - u) vs (v + u)/v", "marks": 1}, {"step": 4, "criterion": "Moving source produces slightly greater shift", "marks": 1}],
        {"tier_1": "Moving source changes wavelength; moving listener changes relative encounter rate.", "tier_2": "Compare 1/(1 - u/v) with (1 + u/v).", "tier_3": ans},
    )


# 21. General Doppler equation both moving same direction
def build_21_general_doppler_equation_both_moving_same_direction(r: random.Random) -> Dict[str, Any]:
    fs = 700
    vs = r.choice([30.0, 35.0, 40.0])  # Police car chasing
    vl = r.choice([18.0, 20.0, 25.0])  # Suspect fleeing ahead in same direction
    v = 340.0
    # Both moving east. Source behind listener: listener moves away from source (+ in vL receding?),
    # Source moves towards listener (- in vS).
    # fL = ((v - vL) / (v - vS)) * fS
    fl = round(((v - vl) / (v - vs)) * fs, 2)

    prompt = (
        f"A police car with a siren of frequency ${fs}\\text{{ Hz}}$ chases a getaway car along a straight highway.\n"
        f"Both vehicles travel east. The police car moves at ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ and "
        f"the getaway car moves ahead at ${_fmt(vl)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the frequency detected by the driver of the getaway car."
    )
    ans = f"{_fmt(fl)} Hz"
    sol = (
        f"General formula: $$f_L = \\left(\\frac{{v \\pm v_L}}{{v \\mp v_S}}\\right) f_S$$\n"
        f"- The police car (source) moves towards the getaway car $\\implies$ denominator is $(v - v_S)$.\n"
        f"- The getaway car (listener) moves away from the police car $\\implies$ numerator is $(v - v_L)$.\n"
        f"$$f_L = \\left(\\frac{{{v} - {_fmt(vl)}}}{{{v} - {_fmt(vs)}}}\\right) ({fs}) = \\left(\\frac{{{_fmt(v - vl)}}}{{{_fmt(v - vs)}}}\\right) ({fs}) = {_fmt(fl)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "21_general_doppler_equation_both_moving_same_direction", 21, prompt, ans, sol, 4,
        ["sign_errors_when_both_source_and_listener_move"],
        [{"step": 1, "criterion": "Formula fL = ((v - vL) / (v - vS)) * fS", "marks": 1}, {"step": 2, "criterion": f"Numerator (340 - {_fmt(vl)})", "marks": 1}, {"step": 3, "criterion": f"Denominator (340 - {_fmt(vs)})", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(fl)} Hz", "marks": 1}],
        {"tier_1": "Source approaches listener: denominator is (v - vs).", "tier_2": "Listener flees from source: numerator is (v - vl).", "tier_3": ans},
    )


# 22. General Doppler equation both moving towards each other
def build_22_general_doppler_equation_both_moving_towards_each_other(r: random.Random) -> Dict[str, Any]:
    fs = 650
    vs = r.choice([20.0, 25.0])
    vl = r.choice([15.0, 20.0])
    v = 340.0
    # Both moving towards each other: numerator is (v + vL), denominator is (v - vS)
    fl = round(((v + vl) / (v - vs)) * fs, 2)

    prompt = (
        f"Two ambulances travel towards each other on a straight road. Ambulance $A$ sounds its siren at ${fs}\\text{{ Hz}}$ "
        f"and travels east at ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Ambulance $B$ travels west at ${_fmt(vl)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the frequency of Ambulance $A$'s siren heard by paramedics in Ambulance $B$."
    )
    ans = f"{_fmt(fl)} Hz"
    sol = (
        f"Both source and listener move towards each other:\n"
        f"- Listener moves towards source $\\implies$ numerator is $(v + v_L)$.\n"
        f"- Source moves towards listener $\\implies$ denominator is $(v - v_S)$.\n"
        f"$$f_L = \\left(\\frac{{v + v_L}}{{v - v_S}}\\right) f_S = \\left(\\frac{{{v} + {_fmt(vl)}}}{{{v} - {_fmt(vs)}}}\\right) ({fs}) = \\left(\\frac{{{_fmt(v + vl)}}}{{{_fmt(v - vs)}}}\\right) ({fs}) = {_fmt(fl)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "22_general_doppler_equation_both_moving_towards_each_other", 22, prompt, ans, sol, 4,
        ["mixed_up_signs_for_mutual_approach"],
        [{"step": 1, "criterion": "Formula fL = ((v + vL) / (v - vS)) * fS", "marks": 1}, {"step": 2, "criterion": "Numerator (v + vL)", "marks": 1}, {"step": 3, "criterion": "Denominator (v - vS)", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(fl)} Hz", "marks": 1}],
        {"tier_1": "Both move towards: numerator gets (+), denominator gets (-).", "tier_2": f"fL = [({v} + {vl}) / ({v} - {vs})] * {fs}.", "tier_3": ans},
    )


# 23. General Doppler equation both moving away from each other
def build_23_general_doppler_equation_both_moving_away_from_each_other(r: random.Random) -> Dict[str, Any]:
    fs = 800
    vs = r.choice([22.0, 28.0])
    vl = r.choice([16.0, 20.0])
    v = 340.0
    # Both moving away: numerator (v - vL), denominator (v + vS)
    fl = round(((v - vl) / (v + vs)) * fs, 2)

    prompt = (
        f"After passing each other at an intersection, two vehicles travel away from each other in opposite directions. "
        f"Vehicle $A$ emits a horn frequency of ${fs}\\text{{ Hz}}$ travelling east at ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, "
        f"while Vehicle $B$ travels west at ${_fmt(vl)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Speed of sound is ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the frequency detected by a passenger in Vehicle $B$."
    )
    ans = f"{_fmt(fl)} Hz"
    sol = (
        f"Both source and listener move away from each other:\n"
        f"- Listener moves away $\\implies$ numerator is $(v - v_L)$.\n"
        f"- Source moves away $\\implies$ denominator is $(v + v_S)$.\n"
        f"$$f_L = \\left(\\frac{{v - v_L}}{{v + v_S}}\\right) f_S = \\left(\\frac{{{v} - {_fmt(vl)}}}{{{v} + {_fmt(vs)}}}\\right) ({fs}) = \\left(\\frac{{{_fmt(v - vl)}}}{{{_fmt(v + vs)}}}\\right) ({fs}) = {_fmt(fl)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "23_general_doppler_equation_both_moving_away_from_each_other", 23, prompt, ans, sol, 4,
        ["mixed_up_signs_for_mutual_recession"],
        [{"step": 1, "criterion": "Formula fL = ((v - vL) / (v + vS)) * fS", "marks": 1}, {"step": 2, "criterion": "Numerator (v - vL)", "marks": 1}, {"step": 3, "criterion": "Denominator (v + vS)", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(fl)} Hz", "marks": 1}],
        {"tier_1": "Both move away: numerator gets (-), denominator gets (+).", "tier_2": f"fL = [({v} - {vl}) / ({v} + {vs})] * {fs}.", "tier_3": ans},
    )


# 24. Sound intensity vs frequency misconception separation
def build_24_sound_intensity_vs_frequency_misconception_separation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner listening to a passing ambulance remarks: *\"The siren gets louder as it approaches and softer as it moves away, "
        "and that is what the Doppler effect describes.\"*\n\n"
        "1. Identify the conceptual error in the learner's statement.\n"
        "2. Explain clearly the difference between what causes the change in **loudness** and what causes the change in **pitch**."
    )
    ans = "The Doppler effect describes the change in observed frequency (pitch), NOT loudness (volume). Loudness changes because sound intensity decreases with distance (inverse-square law), whereas pitch changes because relative motion alters the rate at which wavefronts reach the ear."
    sol = (
        "1. **Conceptual error:** The Doppler effect refers strictly to the change in **observed frequency (pitch)**, "
        "not the change in **loudness (amplitude/volume)**.\n"
        "2. **Distinction:**\n"
        "   - **Loudness (Amplitude / Intensity):** Depends on the amplitude of the wave and distance from the source. "
        "Sound spreads out over a larger area as it travels, decreasing in intensity according to the inverse-square law ($I \\propto 1/r^2$).\n"
        "   - **Pitch (Frequency):** Depends on the frequency (number of wave cycles intercepted per second). "
        "The Doppler effect changes the detected frequency due to relative motion compressing or stretching wavefronts."
    )
    return _make_q(
        r, "24_sound_intensity_vs_frequency_misconception_separation", 24, prompt, ans, sol, 4,
        ["confused_pitch_frequency_with_loudness_amplitude"],
        [{"step": 1, "criterion": "Identified that Doppler effect is about pitch/frequency, not loudness", "marks": 1}, {"step": 2, "criterion": "Loudness depends on amplitude and distance (inverse square law)", "marks": 2}, {"step": 3, "criterion": "Pitch depends on relative motion altering intercepted frequency", "marks": 1}],
        {"tier_1": "Loudness relates to amplitude/distance; pitch relates to frequency/relative motion.", "tier_2": "The Doppler effect governs frequency/pitch only.", "tier_3": ans},
    )


# 25. Doppler wavefront diagram analysis
def build_25_doppler_wavefront_diagram_analysis(r: random.Random) -> Dict[str, Any]:
    vs = r.choice([25.0, 30.0, 35.0])
    v = 340.0
    fs = 400
    fl_app = round((v / (v - vs)) * fs, 1)
    fl_rec = round((v / (v + vs)) * fs, 1)

    diagram_spec = _build_wavefront_svg(vs, v, "right", r.randint(100, 999))
    prompt = (
        f"Inspect the acoustic wavefront diagram provided for a source $S$ emitting sound waves of frequency ${fs}\\text{{ Hz}}$ "
        f"while moving along a horizontal line. Two stationary listeners, $A$ and $B$, are located on either side of the source. "
        f"Take the speed of sound as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. State the direction in which source $S$ is moving (towards Listener $A$ or towards Listener $B$). Give a reason based on the diagram.\n"
        f"2. Which listener detects sound of shorter wavelength? Justify your choice.\n"
        f"3. Calculate the frequency ($f_L$) detected by Listener $A$ if the source moves at ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    ans = f"Towards Listener A (wavefronts compressed on right); Listener A (shorter wavelength); fL = {_fmt(fl_app)} Hz"
    sol = (
        f"1. Source $S$ is moving **towards Listener $A$** (to the right). "
        f"Reason: The circular wavefronts are compressed and crowded closer together on the right side.\n"
        f"2. **Listener $A$** detects sound of shorter wavelength because the forward motion of the source compresses the distance between crests ($\\lambda_A < \\lambda_B$).\n"
        f"3. Since source approaches Listener $A$:\n"
        f"   $$f_{{L,A}} = \\left(\\frac{{v}}{{v - v_S}}\\right) f_S = \\left(\\frac{{{v}}}{{{v} - {_fmt(vs)}}}\\right) ({fs}) = {_fmt(fl_app)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "25_doppler_wavefront_diagram_analysis", 25, prompt, ans, sol, 5,
        ["reversed_direction_of_source_motion_from_wavefront_crowding"],
        [{"step": 1, "criterion": "Direction: towards Listener A with valid reason (compressed wavefronts)", "marks": 2}, {"step": 2, "criterion": "Listener A detects shorter wavelength with justification", "marks": 1}, {"step": 3, "criterion": "Formula fL = (v / (v - vS)) * fS", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(fl_app)} Hz", "marks": 1}],
        {"tier_1": "Wavefronts are compressed in the direction of source motion.", "tier_2": "Listener A is in the compressed region, so fL is higher.", "tier_3": ans},
        diagram_spec=diagram_spec,
    )


# Roster of Subskills 01–25
SUBSKILLS_01_25: Dict[str, Any] = {
    "01_definition_and_nature_of_doppler_effect": build_01_definition_and_nature_of_doppler_effect,
    "02_stationary_source_wavefronts_wavelength_frequency": build_02_stationary_source_wavefronts_wavelength_frequency,
    "03_wavefront_compression_approaching_source_mechanism": build_03_wavefront_compression_approaching_source_mechanism,
    "04_wavefront_stretching_receding_source_mechanism": build_04_wavefront_stretching_receding_source_mechanism,
    "05_apparent_wavelength_ahead_of_approaching_source": build_05_apparent_wavelength_ahead_of_approaching_source,
    "06_apparent_wavelength_behind_receding_source": build_06_apparent_wavelength_behind_receding_source,
    "07_doppler_formula_moving_source_approaching_stationary_listener": build_07_doppler_formula_moving_source_approaching_stationary_listener,
    "08_doppler_formula_moving_source_receding_from_stationary_listener": build_08_doppler_formula_moving_source_receding_from_stationary_listener,
    "09_approaching_and_then_receding_pitch_drop": build_09_approaching_and_then_receding_pitch_drop,
    "10_solving_for_source_speed_from_detected_frequency_approaching": build_10_solving_for_source_speed_from_detected_frequency_approaching,
    "11_solving_for_source_speed_from_detected_frequency_receding": build_11_solving_for_source_speed_from_detected_frequency_receding,
    "12_solving_for_source_frequency_from_detected_frequency": build_12_solving_for_source_frequency_from_detected_frequency,
    "13_solving_for_speed_of_sound_in_gas_or_air": build_13_solving_for_speed_of_sound_in_gas_or_air,
    "14_ratio_of_observed_frequencies_approach_to_recede": build_14_ratio_of_observed_frequencies_approach_to_recede,
    "15_percentage_change_in_observed_frequency_approach": build_15_percentage_change_in_observed_frequency_approach,
    "16_percentage_change_in_observed_frequency_receding": build_16_percentage_change_in_observed_frequency_receding,
    "17_stationary_source_moving_listener_approaching": build_17_stationary_source_moving_listener_approaching,
    "18_stationary_source_moving_listener_receding": build_18_stationary_source_moving_listener_receding,
    "19_solving_for_listener_speed_approaching_or_receding": build_19_solving_for_listener_speed_approaching_or_receding,
    "20_comparison_between_moving_source_vs_moving_listener": build_20_comparison_between_moving_source_vs_moving_listener,
    "21_general_doppler_equation_both_moving_same_direction": build_21_general_doppler_equation_both_moving_same_direction,
    "22_general_doppler_equation_both_moving_towards_each_other": build_22_general_doppler_equation_both_moving_towards_each_other,
    "23_general_doppler_equation_both_moving_away_from_each_other": build_23_general_doppler_equation_both_moving_away_from_each_other,
    "24_sound_intensity_vs_frequency_misconception_separation": build_24_sound_intensity_vs_frequency_misconception_separation,
    "25_doppler_wavefront_diagram_analysis": build_25_doppler_wavefront_diagram_analysis,
}
