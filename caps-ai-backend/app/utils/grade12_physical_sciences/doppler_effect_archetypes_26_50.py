"""Grade 12 Physical Sciences - The Doppler Effect Archetypes 26 to 50.
Grounded in curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/04. The Doppler effect.md.

Covers:
  - Frequency vs time step-down graph analysis with seed-varied inline vector SVGs.
  - Graphical relationships (f_L vs v_S, lambda vs v_S).
  - Doppler echo and reflection from stationary and moving targets (radar speed trap).
  - Doppler effect with light: redshift and blueshift of stellar absorption spectra.
  - Spectral line displacement (Delta lambda / lambda_0 = v / c) and radial velocity.
  - Cosmological redshift, Hubble's Law, and expanding universe evidence.
  - Binary star orbital Doppler shifts with inline vector SVGs.
  - Medical applications: Doppler ultrasound blood flowmeter and fetal heart monitor.
  - Technological applications: Weather radar, ocean current profiling, satellite tracking.
  - Physical boundary conditions: Sonic boom, Mach number, temperature and wind effects.
  - Whirling buzzer laboratory demonstration and angled observer geometries.
  - Capstone comprehensive exam riders and diagnostic autopsy / misconception repair.

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
            "deductions": [{"rule": "omitted_units", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


def _build_freq_time_graph_svg(fl_app: float, fl_rec: float, fs: float, seed: int) -> Dict[str, Any]:
    """Generates an inline vector SVG of observed frequency vs time as vehicle passes."""
    w, h = 480, 260
    ox, oy = 70, 210

    # Points for the step-down curve
    y_app = oy - int(fl_app / 6.0)
    y_rec = oy - int(fl_rec / 6.0)
    y_fs = oy - int(fs / 6.0)

    # Ensure in bounds
    y_app = max(40, min(oy - 50, y_app))
    y_rec = max(y_app + 25, min(oy - 10, y_rec))
    y_fs = (y_app + y_rec) // 2

    path_d = f"M {ox} {y_app} L {ox + 140} {y_app} L {ox + 180} {y_rec} L {ox + 340} {y_rec}"

    svg_content = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" style="background:#f8fafc; border-radius:8px;">'
        f'<!-- seed:{seed} -->'
        f'<rect width="{w}" height="{h}" fill="#f8fafc" />'
        # Grid lines
        f'<line x1="{ox}" y1="{oy}" x2="{ox + 360}" y2="{oy}" stroke="#334155" stroke-width="2" />'
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="20" stroke="#334155" stroke-width="2" />'
        # Labels
        f'<text x="{ox + 360}" y="{oy + 25}" font-family="sans-serif" font-size="12" fill="#334155" text-anchor="end">Time t (s)</text>'
        f'<text x="20" y="30" font-family="sans-serif" font-size="12" fill="#334155">fL (Hz)</text>'
        # Frequency plateau lines & labels
        f'<line x1="{ox}" y1="{y_app}" x2="{ox + 340}" y2="{y_app}" stroke="#cbd5e1" stroke-dasharray="4,4" />'
        f'<text x="{ox - 8}" y="{y_app + 4}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#059669" text-anchor="end">{_fmt(fl_app)}</text>'
        f'<line x1="{ox}" y1="{y_rec}" x2="{ox + 340}" y2="{y_rec}" stroke="#cbd5e1" stroke-dasharray="4,4" />'
        f'<text x="{ox - 8}" y="{y_rec + 4}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="end">{_fmt(fl_rec)}</text>'
        # Emitted frequency guide
        f'<line x1="{ox}" y1="{y_fs}" x2="{ox + 340}" y2="{y_fs}" stroke="#94a3b8" stroke-dasharray="2,2" />'
        f'<text x="{ox + 345}" y="{y_fs + 4}" font-family="sans-serif" font-size="10" fill="#64748b">fs = {_fmt(fs)}</text>'
        # Curve
        f'<path d="{path_d}" fill="none" stroke="#2563eb" stroke-width="3" />'
        # Annotations
        f'<text x="{ox + 70}" y="{y_app - 8}" font-family="sans-serif" font-size="11" fill="#059669" font-weight="bold">Approaching</text>'
        f'<text x="{ox + 250}" y="{y_rec - 8}" font-family="sans-serif" font-size="11" fill="#dc2626" font-weight="bold">Receding</text>'
        f'<circle cx="{ox + 160}" cy="{y_fs}" r="4" fill="#d97706" />'
        f'<text x="{ox + 160}" y="{oy + 18}" font-family="sans-serif" font-size="10" fill="#d97706" text-anchor="middle">Passing observer</text>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "diagram_role": "context",
        "svg": svg_content,
        "width": w,
        "height": h,
    }


def _build_freq_vs_speed_svg(fs: float, v: float, seed: int) -> Dict[str, Any]:
    """Generates an inline vector SVG showing linear graph of fL vs vS for approaching source."""
    w, h = 460, 240
    ox, oy = 70, 190
    y_int = oy - 60
    y_top = y_int - 80
    x_end = ox + 320

    svg_content = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" style="background:#f8fafc; border-radius:8px;">'
        f'<!-- seed:{seed} -->'
        f'<rect width="{w}" height="{h}" fill="#f8fafc" />'
        f'<line x1="{ox}" y1="{oy}" x2="{ox + 350}" y2="{oy}" stroke="#334155" stroke-width="2" />'
        f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="20" stroke="#334155" stroke-width="2" />'
        f'<text x="{ox + 350}" y="{oy + 25}" font-family="sans-serif" font-size="12" fill="#334155" text-anchor="end">Source speed vS (m·s⁻¹)</text>'
        f'<text x="20" y="30" font-family="sans-serif" font-size="12" fill="#334155">fL (Hz)</text>'
        f'<line x1="{ox}" y1="{y_int}" x2="{x_end}" y2="{y_top}" stroke="#2563eb" stroke-width="3" />'
        f'<circle cx="{ox}" cy="{y_int}" r="5" fill="#dc2626" />'
        f'<text x="{ox - 8}" y="{y_int + 4}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="end">fs = {_fmt(fs)}</text>'
        f'<line x1="{x_end}" y1="{oy}" x2="{x_end}" y2="{y_top}" stroke="#94a3b8" stroke-dasharray="3,3" />'
        f'<circle cx="{x_end}" cy="{y_top}" r="4" fill="#2563eb" />'
        f'<text x="{x_end}" y="{oy + 18}" font-family="sans-serif" font-size="11" fill="#334155" text-anchor="middle">vS</text>'
        f'<text x="{ox + 160}" y="{y_int - 50}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">fL ≈ fs + (fs/v)·vS</text>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "diagram_role": "context",
        "svg": svg_content,
        "width": w,
        "height": h,
    }


def _build_binary_star_svg(shift_px: int, seed: int) -> Dict[str, Any]:
    """Generates an inline vector SVG comparing reference vs binary star spectral absorption lines."""
    w, h = 480, 200
    svg_content = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" style="background:#ffffff; border-radius:8px;">'
        f'<!-- seed:{seed} -->'
        f'<rect width="{w}" height="{h}" fill="#f8fafc" />'
        # Spectrum Bar 1: Laboratory Reference
        f'<text x="20" y="32" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">1. Laboratory Reference (At Rest):</text>'
        f'<rect x="20" y="40" width="440" height="30" rx="4" fill="url(#spec_grad)" stroke="#64748b" />'
        # Reference lines (e.g. 100, 180, 280, 360)
        f'<line x1="120" y1="40" x2="120" y2="70" stroke="#000000" stroke-width="2.5" />'
        f'<line x1="220" y1="40" x2="220" y2="70" stroke="#000000" stroke-width="2.5" />'
        f'<line x1="320" y1="40" x2="320" y2="70" stroke="#000000" stroke-width="2.5" />'
        # Spectrum Bar 2: Star A (Redshifted)
        f'<text x="20" y="98" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">2. Star A (Receding from Earth - Redshift):</text>'
        f'<rect x="20" y="106" width="440" height="30" rx="4" fill="url(#spec_grad)" stroke="#64748b" />'
        f'<line x1="{120 + shift_px}" y1="106" x2="{120 + shift_px}" y2="136" stroke="#000000" stroke-width="2.5" />'
        f'<line x1="{220 + shift_px}" y1="106" x2="{220 + shift_px}" y2="136" stroke="#000000" stroke-width="2.5" />'
        f'<line x1="{320 + shift_px}" y1="106" x2="{320 + shift_px}" y2="136" stroke="#000000" stroke-width="2.5" />'
        # Labels Blue vs Red end
        f'<text x="25" y="160" font-family="sans-serif" font-size="10" font-weight="bold" fill="#2563eb">← Shorter wavelength (Blue)</text>'
        f'<text x="455" y="160" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="end">Longer wavelength (Red) →</text>'
        f'<defs>'
        f'<linearGradient id="spec_grad" x1="0%" y1="0%" x2="100%" y2="0%">'
        f'<stop offset="0%" stop-color="#3b82f6" />'
        f'<stop offset="30%" stop-color="#06b6d4" />'
        f'<stop offset="60%" stop-color="#eab308" />'
        f'<stop offset="100%" stop-color="#ef4444" />'
        f'</linearGradient>'
        f'</defs>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "diagram_role": "context",
        "svg": svg_content,
        "width": w,
        "height": h,
    }


def _build_ultrasound_flow_svg(angle_deg: int, v_flow: float, seed: int) -> Dict[str, Any]:
    """Generates an inline vector SVG of Doppler ultrasound transducer over a blood vessel."""
    w, h = 480, 240
    svg_content = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" style="background:#ffffff; border-radius:8px;">'
        f'<!-- seed:{seed} -->'
        f'<rect width="{w}" height="{h}" fill="#f8fafc" />'
        # Skin surface
        f'<line x1="20" y1="70" x2="460" y2="70" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4" />'
        f'<text x="30" y="62" font-family="sans-serif" font-size="10" fill="#64748b">Skin surface</text>'
        # Blood vessel walls
        f'<rect x="20" y="130" width="440" height="60" fill="#fee2e2" stroke="#dc2626" stroke-width="2" rx="4" />'
        f'<text x="30" y="122" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Blood vessel (Artery)</text>'
        # Flow arrow & Red Blood Cells
        f'<line x1="80" y1="160" x2="380" y2="160" stroke="#b91c1c" stroke-width="2" marker-end="url(#red_arrow)" />'
        f'<circle cx="140" cy="155" r="5" fill="#dc2626" />'
        f'<circle cx="200" cy="165" r="5" fill="#dc2626" />'
        f'<circle cx="280" cy="158" r="5" fill="#dc2626" />'
        f'<text x="390" y="164" font-family="sans-serif" font-size="11" font-weight="bold" fill="#b91c1c">v = {_fmt(v_flow)} m·s⁻¹</text>'
        # Transducer probe
        f'<polygon points="210,15 270,15 250,70 190,70" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2" />'
        f'<text x="230" y="42" font-family="sans-serif" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Probe</text>'
        # Ultrasound beam line
        f'<line x1="220" y1="70" x2="270" y2="155" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="3,3" />'
        f'<text x="275" y="105" font-family="sans-serif" font-size="11" font-weight="bold" fill="#d97706">θ = {angle_deg}°</text>'
        f'<defs>'
        f'<marker id="red_arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="#b91c1c" />'
        f'</marker>'
        f'</defs>'
        f'</svg>'
    )
    return {
        "kind": "inline_svg",
        "diagram_role": "context",
        "svg": svg_content,
        "width": w,
        "height": h,
    }


# =============================================================================
# Subskills 26–50 Builders
# =============================================================================

# 26. Frequency vs time graph approaching passing receding
def build_26_frequency_vs_time_graph_approaching_passing_receding(r: random.Random) -> Dict[str, Any]:
    fs = r.choice([480, 540, 600, 720])
    vs = r.choice([20.0, 25.0, 30.0])
    v = 340.0
    fl_app = round((v / (v - vs)) * fs, 1)
    fl_rec = round((v / (v + vs)) * fs, 1)

    diagram_spec = _build_freq_time_graph_svg(fl_app, fl_rec, fs, r.randint(100, 999))
    prompt = (
        f"A vehicle sounding its horn passes a roadside audio detector. The detector records the observed frequency "
        f"over time, as displayed in the accompanying frequency-time graph. "
        f"The speed of sound in air is ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Read off the detected frequency during approach ($f_{{L,\\text{{approach}}}}$) and during recession ($f_{{L,\\text{{recede}}}}$).\n"
        f"2. Explain why the detected frequency remains roughly constant while the vehicle is far away and approaching, then drops rapidly as it passes.\n"
        f"3. Using the Doppler equations for approach and recession, calculate the speed ($v_S$) of the vehicle."
    )
    ans = f"fL_app = {_fmt(fl_app)} Hz; fL_rec = {_fmt(fl_rec)} Hz; vS = {_fmt(vs)} m·s⁻¹"
    sol = (
        f"1. From graph: $f_{{L,\\text{{approach}}}} = {_fmt(fl_app)}\\text{{ Hz}}$ and $f_{{L,\\text{{recede}}}} = {_fmt(fl_rec)}\\text{{ Hz}}$.\n"
        f"2. While far away on a straight road, the component of velocity directly along the line of sight is constant ($v_S$), "
        f"yielding a constant frequency. As the vehicle passes directly alongside the observer, the line-of-sight velocity "
        f"rapidly swings from $+v_S$ to $-v_S$, creating the sudden downward pitch shift.\n"
        f"3. Using the ratio $R = \\frac{{f_{{L,\\text{{app}}}}}}{{f_{{L,\\text{{rec}}}}}} = \\frac{{v + v_S}}{{v - v_S}}$:\n"
        f"   $$R = \\frac{{{_fmt(fl_app)}}}{{{_fmt(fl_rec)}}} = {_fmt(fl_app / fl_rec, 3)}$$\n"
        f"   $$v_S = v \\left(\\frac{{R - 1}}{{R + 1}}\\right) = {v} \\left(\\frac{{{_fmt(fl_app / fl_rec, 3)} - 1}}{{{_fmt(fl_app / fl_rec, 3)} + 1}}\\right) = {_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "26_frequency_vs_time_graph_approaching_passing_receding", 26, prompt, ans, sol, 6,
        ["misread_graph_plateau_values"],
        [{"step": 1, "criterion": f"fL_approach = {_fmt(fl_app)} Hz and fL_recede = {_fmt(fl_rec)} Hz", "marks": 2}, {"step": 2, "criterion": "Explanation of line-of-sight component velocity", "marks": 2}, {"step": 3, "criterion": "Formula and substitution for vehicle speed", "marks": 1}, {"step": 4, "criterion": f"Answer vS = {_fmt(vs)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Read the top horizontal plateau for approach and bottom for recede.", "tier_2": "Use the frequency ratio R = (v + vs) / (v - vs) to find vs.", "tier_3": ans},
        diagram_spec=diagram_spec,
    )


# 27. Frequency vs source velocity linear approximation
def build_27_frequency_vs_source_velocity_linear_approximation(r: random.Random) -> Dict[str, Any]:
    fs = 500
    v = 340.0
    # For small vs/v, fL approx fs * (1 + vs/v) = fs + (fs/v) * vs
    slope = round(fs / v, 2)
    diagram_spec = _build_freq_vs_speed_svg(fs, v, r.randint(100, 999))
    prompt = (
        f"An acoustic laboratory plots observed frequency ($f_L$) against source velocity ($v_S$) for an approaching vehicle "
        f"emitting a sound of frequency ${fs}\\text{{ Hz}}$ in air where $v = {v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, "
        f"as shown in the accompanying linear graph.\n"
        f"For speeds much smaller than sound ($v_S \\ll v$), the relationship approximates a straight line: "
        f"$f_L \\approx f_S + \\left(\\frac{{f_S}}{{v}}\\right) v_S$.\n\n"
        f"1. Identify the $y$-intercept of this graph.\n"
        f"2. Calculate the gradient (slope) of this linear approximation in $\\text{{Hz}}\\cdot\\text{{s}}\\cdot\\text{{m}}^{{-1}}$."
    )
    ans = f"y-intercept = {fs} Hz; Gradient = {_fmt(slope)} Hz·s·m⁻¹"
    sol = (
        f"1. The $y$-intercept corresponds to $v_S = 0$, which is the actual emitted frequency: **{fs} Hz**.\n"
        f"2. The gradient of the linear approximation is:\n"
        f"   $$\\text{{Gradient}} = \\frac{{f_S}}{{v}} = \\frac{{{fs}}}{{{v}}} = {_fmt(slope)}\\text{{ Hz}}\\cdot\\text{{s}}\\cdot\\text{{m}}^{{-1}}$$"
    )
    return _make_q(
        r, "27_frequency_vs_source_velocity_linear_approximation", 27, prompt, ans, sol, 3,
        ["confused_y_intercept_with_zero"],
        [{"step": 1, "criterion": f"y-intercept = {fs} Hz (source frequency)", "marks": 1}, {"step": 2, "criterion": "Gradient formula fs / v", "marks": 1}, {"step": 3, "criterion": f"Gradient = {_fmt(slope)} Hz·s·m⁻¹", "marks": 1}],
        {"tier_1": "When velocity is zero, detected frequency equals source frequency.", "tier_2": "The slope of f vs v is fS / v.", "tier_3": ans},
        diagram_spec=diagram_spec,
    )


# 28. Wavelength vs source velocity linear relationship
def build_28_wavelength_vs_source_velocity_linear_relationship(r: random.Random) -> Dict[str, Any]:
    fs = 400
    v = 340.0
    lam_0 = round(v / fs, 3)
    slope = round(-1.0 / fs, 4)

    prompt = (
        f"A sound source of frequency ${fs}\\text{{ Hz}}$ moves towards an observer at speed $v_S$. "
        f"The wavelength ahead of the source obeys the equation $\\lambda' = \\frac{{v - v_S}}{{f_S}} = \\lambda_0 - \\left(\\frac{{1}}{{f_S}}\\right) v_S$.\n\n"
        f"1. Calculate the initial wavelength $\\lambda_0$ when the source is stationary ($v = {v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$).\n"
        f"2. State whether a graph of $\\lambda'$ versus $v_S$ has a positive or negative slope, and state the physical quantity represented by the slope magnitude ($1/f_S$)."
    )
    ans = f"lambda_0 = {_fmt(lam_0)} m; Negative slope; Slope magnitude is period T = 1/fS"
    sol = (
        f"1. $$\\lambda_0 = \\frac{{v}}{{f_S}} = \\frac{{{v}}}{{{fs}}} = {_fmt(lam_0)}\\text{{ m}}$$\n"
        f"2. The slope is **negative** ($-1/f_S$) because wavelength decreases as source speed increases. "
        f"The magnitude of the slope is $\\frac{{1}}{{f_S}} = T$, which represents the **wave period** ($T = {_fmt(1.0 / fs, 4)}\\text{{ s}}$)."
    )
    return _make_q(
        r, "28_wavelength_vs_source_velocity_linear_relationship", 28, prompt, ans, sol, 3,
        ["stated_slope_is_positive_for_wavelength_vs_speed"],
        [{"step": 1, "criterion": f"Rest wavelength = {_fmt(lam_0)} m", "marks": 1}, {"step": 2, "criterion": "Negative slope identified", "marks": 1}, {"step": 3, "criterion": "Slope magnitude represents wave period T = 1/fS", "marks": 1}],
        {"tier_1": "Wavelength decreases as speed increases, so slope is negative.", "tier_2": "1 / fS is the period T.", "tier_3": ans},
    )


# 29. Doppler echo reflection stationary target
def build_29_doppler_echo_reflection_stationary_target(r: random.Random) -> Dict[str, Any]:
    fs = 800
    vs = r.choice([15.0, 20.0, 25.0])
    v = 340.0
    # Step 1: Wall receives f_wall = (v / (v - vs)) * fs
    f_wall = (v / (v - vs)) * fs
    # Step 2: Wall re-emits f_wall. Car receives f_echo = ((v + vs) / v) * f_wall = ((v + vs) / (v - vs)) * fs
    f_echo = round(((v + vs) / (v - vs)) * fs, 1)

    prompt = (
        f"A bat flies at ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ directly towards a flat vertical rock face "
        f"while emitting an ultrasonic chirp of frequency ${fs}\\text{{ Hz}}$. Take the speed of sound as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Calculate the frequency of the sound waves hitting the rock wall.\n"
        f"2. Calculate the echo frequency detected by the bat upon receiving the reflected sound waves."
    )
    ans = f"f_wall = {_fmt(round(f_wall, 1))} Hz; f_echo = {_fmt(f_echo)} Hz"
    sol = (
        f"1. The moving bat acts as a source approaching a stationary observer (the wall):\n"
        f"   $$f_{{\\text{{wall}}}} = \\left(\\frac{{v}}{{v - v_S}}\\right) f_S = \\left(\\frac{{{v}}}{{{v} - {_fmt(vs)}}}\\right) ({fs}) = {_fmt(round(f_wall, 1))}\\text{{ Hz}}$$\n"
        f"2. The wall reflects this frequency and acts as a stationary source emitting $f_{{\\text{{wall}}}}$. "
        f"The bat is now an observer moving towards the stationary source:\n"
        f"   $$f_{{\\text{{echo}}}} = \\left(\\frac{{v + v_S}}{{v}}\\right) f_{{\\text{{wall}}}} = \\left(\\frac{{v + v_S}}{{v}}\\right) \\left(\\frac{{v}}{{v - v_S}}\\right) f_S = \\left(\\frac{{v + v_S}}{{v - v_S}}\\right) f_S$$\n"
        f"   $$f_{{\\text{{echo}}}} = \\left(\\frac{{{v} + {_fmt(vs)}}}{{{v} - {_fmt(vs)}}}\\right) ({fs}) = \\left(\\frac{{{_fmt(v + vs)}}}{{{_fmt(v - vs)}}}\\right) ({fs}) = {_fmt(f_echo)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "29_doppler_echo_reflection_stationary_target", 29, prompt, ans, sol, 5,
        ["only_applied_doppler_shift_once_for_echo"],
        [{"step": 1, "criterion": f"Wall incident frequency = {_fmt(round(f_wall, 1))} Hz", "marks": 2}, {"step": 2, "criterion": "Two-stage Doppler shift application", "marks": 2}, {"step": 3, "criterion": f"Final echo frequency = {_fmt(f_echo)} Hz", "marks": 1}],
        {"tier_1": "An echo involves a two-stage Doppler shift: bat to wall, then wall back to bat.", "tier_2": "f_echo = [(v + vs) / (v - vs)] * fS.", "tier_3": ans},
    )


# 30. Doppler echo reflection moving target
def build_30_doppler_echo_reflection_moving_target(r: random.Random) -> Dict[str, Any]:
    f0 = 24000  # 24 kHz sonar
    vt = r.choice([6.0, 8.0, 10.0])  # Submarine target speed approaching
    v = 1500.0  # Speed of sound in seawater
    # Target receives f_t = ((v + vt)/v) * f0
    # Target re-emits f_t. Station receives f_echo = (v / (v - vt)) * f_t = ((v + vt)/(v - vt)) * f0
    f_echo = round(((v + vt) / (v - vt)) * f0, 1)
    df = round(f_echo - f0, 1)

    prompt = (
        f"A stationary naval sonar station emits an acoustic pulse of frequency ${f0}\\text{{ Hz}}$ in seawater "
        f"where sound travels at ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"An approaching submarine moves directly towards the station at ${_fmt(vt)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Calculate the frequency received by the submarine.\n"
        f"2. Calculate the beat frequency (frequency shift $\\Delta f = f_{{\\text{{echo}}}} - f_0$) detected back at the sonar station."
    )
    ans = f"f_received = {_fmt(round(((v + vt)/v)*f0, 1))} Hz; Delta f = {_fmt(df)} Hz"
    sol = (
        f"1. Submarine moves towards stationary source: $$f_{{\\text{{sub}}}} = \\left(\\frac{{{v} + {_fmt(vt)}}}{{{v}}}\\right) ({f0}) = {_fmt(round(((v + vt)/v)*f0, 1))}\\text{{ Hz}}$$\n"
        f"2. Submarine reflects sound as a moving source approaching the stationary station:\n"
        f"   $$f_{{\\text{{echo}}}} = \\left(\\frac{{{v}}}{{{v} - {_fmt(vt)}}}\\right) f_{{\\text{{sub}}}} = \\left(\\frac{{{v} + {_fmt(vt)}}}{{{v} - {_fmt(vt)}}}\\right) ({f0}) = {_fmt(f_echo)}\\text{{ Hz}}$$\n"
        f"   $$\\Delta f = {_fmt(f_echo)} - {f0} = {_fmt(df)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "30_doppler_echo_reflection_moving_target", 30, prompt, ans, sol, 5,
        ["failed_to_apply_reflection_as_secondary_source"],
        [{"step": 1, "criterion": "Submarine received frequency calculation", "marks": 2}, {"step": 2, "criterion": "Echo frequency calculation", "marks": 2}, {"step": 3, "criterion": f"Frequency shift Delta f = {_fmt(df)} Hz", "marks": 1}],
        {"tier_1": "First treat target as moving observer, then as moving source.", "tier_2": "Delta f = f_echo - f0.", "tier_3": ans},
    )


# 31. Radar speed gun beat frequency calculation
def build_31_radar_speed_gun_beat_frequency_calculation(r: random.Random) -> Dict[str, Any]:
    f0 = 10.5e9  # 10.5 GHz X-band radar
    v_kmh = r.choice([72, 90, 108, 126])
    v_car = v_kmh / 3.6  # 20, 25, 30, 35 m/s
    c = 3.0e8
    # Delta f = 2 * v_car * f0 / c
    delta_f = round((2.0 * v_car * f0) / c, 1)

    prompt = (
        f"A traffic officer operates a Doppler radar speed trap emitting electromagnetic waves at $f_0 = 10{{,}}5\\text{{ GHz}}$ "
        f"($10{{,}}5 \\times 10^9\\text{{ Hz}}$). The radar reflects off an approaching car and produces a beat frequency "
        f"shift of $\\Delta f = {_fmt(delta_f)}\\text{{ Hz}}$. Take the speed of light as $c = 3{{,}}0 \\times 10^8\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Explain how the beat frequency is formed between transmitted and reflected waves.\n"
        f"2. Using $\\Delta f = \\frac{{2 v_{{\\text{{car}}}}}}{{c}} f_0$, calculate the speed of the car in $\\text{{m}}\\cdot\\text{{s}}^{{-1}}$ and $\\text{{km}}\\cdot\\text{{h}}^{{-1}}$."
    )
    ans = f"v = {_fmt(v_car)} m·s⁻¹ ({v_kmh} km·h⁻¹)"
    sol = (
        "1. The radar receiver superimposes the transmitted wave and the Doppler-shifted reflected wave. "
        "Interference between the two slightly different frequencies produces periodic variations in amplitude called **beats**, "
        "whose frequency equals the difference $\\Delta f = |f_{\\text{reflected}} - f_0|$.\n"
        f"2. Rearrange for $v_{{\\text{{car}}}}$:\n"
        f"   $$v_{{\\text{{car}}}} = \\frac{{c \\Delta f}}{{2 f_0}} = \\frac{{(3{{,}}0 \\times 10^8)({_fmt(delta_f)})}}{{2(10{{,}}5 \\times 10^9)}} = {_fmt(v_car)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"   $$\\text{{Speed in km/h}} = {_fmt(v_car)} \\times 3{{,}}6 = {v_kmh}\\text{{ km}}\\cdot\\text{{h}}^{{-1}}$$"
    )
    return _make_q(
        r, "31_radar_speed_gun_beat_frequency_calculation", 31, prompt, ans, sol, 5,
        ["omitted_factor_of_two_for_round_trip_radar_echo"],
        [{"step": 1, "criterion": "Beat formation explanation via wave interference", "marks": 2}, {"step": 2, "criterion": "Formula rearrangement for v_car", "marks": 1}, {"step": 3, "criterion": f"Speed in m/s = {_fmt(v_car)} m·s⁻¹", "marks": 1}, {"step": 4, "criterion": f"Speed in km/h = {v_kmh} km·h⁻¹", "marks": 1}],
        {"tier_1": "Radar echo has a factor of 2 because of two-way travel.", "tier_2": "Multiply m/s by 3,6 to obtain km/h.", "tier_3": ans},
    )


# 32. Doppler effect with light intro
def build_32_doppler_effect_with_light_intro(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Doppler effect applies to both sound waves and light waves.\n\n"
        "1. State TWO differences between sound waves and light waves regarding their wave type and medium requirement.\n"
        "2. What observable property of light corresponds to pitch in sound?\n"
        "3. State what happens to the detected color (frequency) of light when a light source moves rapidly towards an observer."
    )
    ans = "1. Sound is a longitudinal mechanical wave requiring a medium; light is a transverse electromagnetic wave that can propagate through vacuum; 2. Color (or wavelength/frequency); 3. Shifted to higher frequency (blueshift)."
    sol = (
        "1. **Differences:**\n"
        "   - **Wave type:** Sound is a longitudinal wave (particle oscillations parallel to propagation); light is a transverse electromagnetic wave.\n"
        "   - **Medium:** Sound requires a material medium to propagate; light does not require a medium and travels through a vacuum.\n"
        "2. The **color** of visible light corresponds to its frequency/wavelength, just as pitch corresponds to sound frequency.\n"
        "3. When moving towards an observer, light is shifted to a **higher frequency / shorter wavelength**, known as **blueshift**."
    )
    return _make_q(
        r, "32_doppler_effect_with_light_intro", 32, prompt, ans, sol, 4,
        ["classified_light_as_longitudinal"],
        [{"step": 1, "criterion": "Sound longitudinal vs light transverse", "marks": 1}, {"step": 2, "criterion": "Sound requires medium vs light in vacuum", "marks": 1}, {"step": 3, "criterion": "Pitch corresponds to color/frequency", "marks": 1}, {"step": 4, "criterion": "Towards observer causes shift to higher frequency (blueshift)", "marks": 1}],
        {"tier_1": "Sound is mechanical; light is electromagnetic.", "tier_2": "Higher frequency in visible light shifts towards the blue/violet end.", "tier_3": ans},
    )


# 33. Redshift definition and spectral line displacement
def build_33_redshift_definition_and_spectral_line_displacement(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Astronomers observe the line absorption spectra of distant stars and galaxies.\n\n"
        "1. Define the term **redshift** in the context of astronomical observations.\n"
        "2. Explain what a redshift indicates about the motion of a distant galaxy relative to Earth.\n"
        "3. Does redshift mean that all stars and galaxies appear red to the naked eye? Explain."
    )
    ans = "1. Redshift is the shift of spectral lines to longer wavelengths (lower frequencies) towards the red end of the spectrum; 2. It indicates the galaxy is moving away from Earth (receding); 3. No, it refers to the displacement of specific spectral absorption lines, not the overall perceived color of the star."
    sol = (
        "1. **Redshift:** The shift in the positions of spectral lines towards the longer wavelength (lower frequency) "
        "or red end of the electromagnetic spectrum.\n"
        "2. A redshift indicates that the celestial object is **moving away from (receding from) the observer on Earth**.\n"
        "3. **No**, redshift does not mean the object physically looks red. It means that identifiable absorption lines "
        "(such as hydrogen or helium spectral lines) are displaced to slightly longer wavelengths compared to laboratory reference values."
    )
    return _make_q(
        r, "33_redshift_definition_and_spectral_line_displacement", 33, prompt, ans, sol, 4,
        ["thought_redshift_turns_stars_red_in_color"],
        [{"step": 1, "criterion": "Definition of redshift (spectral lines shifted to longer wavelengths)", "marks": 2}, {"step": 2, "criterion": "Indicates motion away from Earth (recession)", "marks": 1}, {"step": 3, "criterion": "Does not mean star looks red; refers to line displacement", "marks": 1}],
        {"tier_1": "Redshift means wavelengths are stretched to longer values.", "tier_2": "Longer wavelengths correspond to the red end of visible light.", "tier_3": ans},
    )


# 34. Blueshift definition and approaching celestial objects
def build_34_blueshift_definition_and_approaching_celestial_objects(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Spectral analysis of the Andromeda Galaxy reveals that its spectral absorption lines are shifted towards shorter wavelengths.\n\n"
        "1. Name this phenomenon.\n"
        "2. State what this observation reveals about the motion of the Andromeda Galaxy relative to the Milky Way.\n"
        "3. Contrast the wavelength and frequency changes associated with a blueshift versus a redshift."
    )
    ans = "1. Blueshift; 2. Andromeda is moving towards the Milky Way; 3. Blueshift: shorter wavelength and higher frequency; Redshift: longer wavelength and lower frequency."
    sol = (
        "1. The phenomenon is called **blueshift**.\n"
        "2. It indicates that the Andromeda Galaxy is **moving towards our Milky Way Galaxy** (approaching Earth).\n"
        "3. **Comparison:**\n"
        "   - **Blueshift:** $\\lambda$ decreases (shorter wavelength), $f$ increases (higher frequency).\n"
        "   - **Redshift:** $\\lambda$ increases (longer wavelength), $f$ decreases (lower frequency)."
    )
    return _make_q(
        r, "34_blueshift_definition_and_approaching_celestial_objects", 34, prompt, ans, sol, 3,
        ["reversed_blueshift_wavelength_direction"],
        [{"step": 1, "criterion": "Identification as blueshift", "marks": 1}, {"step": 2, "criterion": "Approaching the Milky Way / Earth", "marks": 1}, {"step": 3, "criterion": "Comparison of wavelength and frequency changes", "marks": 1}],
        {"tier_1": "Blue light has shorter wavelength than red light.", "tier_2": "Approaching objects produce shorter wavelengths (blueshift).", "tier_3": ans},
    )


# 35. Stellar radial velocity from wavelength shift
def build_35_stellar_radial_velocity_from_wavelength_shift(r: random.Random) -> Dict[str, Any]:
    lam0 = 656.3  # Hydrogen-alpha line in nm
    v_star = r.choice([150000.0, 300000.0, 450000.0, 600000.0])  # m/s
    c = 3.0e8
    # Delta lambda = (v / c) * lam0
    delta_lam = round((v_star / c) * lam0, 3)
    lam_obs = round(lam0 + delta_lam, 3)

    prompt = (
        f"A hydrogen absorption line measured in a terrestrial laboratory has a rest wavelength of $\\lambda_0 = {_fmt(lam0)}\\text{{ nm}}$. "
        f"In the light emitted by a distant star, this same line is observed at $\\lambda = {_fmt(lam_obs)}\\text{{ nm}}$. "
        f"Take the speed of light as $c = 3{{,}}0 \\times 10^8\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. State whether the star is moving towards or away from Earth.\n"
        f"2. Calculate the change in wavelength ($\\Delta\\lambda = \\lambda - \\lambda_0$).\n"
        f"3. Using $\\frac{{\\Delta\\lambda}}{{\\lambda_0}} = \\frac{{v}}{{c}}$, calculate the radial speed ($v$) of the star in $\\text{{km}}\\cdot\\text{{s}}^{{-1}}$."
    )
    ans = f"Away from Earth; Delta lambda = {_fmt(delta_lam)} nm; v = {_fmt(v_star / 1000.0)} km·s⁻¹"
    sol = (
        f"1. Since $\\lambda > \\lambda_0$ (${_fmt(lam_obs)}\\text{{ nm}} > {_fmt(lam0)}\\text{{ nm}}$), the wavelength is lengthened (redshift), "
        f"meaning the star is **moving away from Earth**.\n"
        f"2. $$\\Delta\\lambda = {_fmt(lam_obs)} - {_fmt(lam0)} = {_fmt(delta_lam)}\\text{{ nm}}$$\n"
        f"3. Using the Doppler shift formula for light:\n"
        f"   $$v = c \\left(\\frac{{\\Delta\\lambda}}{{\\lambda_0}}\\right) = (3{{,}}0 \\times 10^8) \\left(\\frac{{{_fmt(delta_lam)}}}{{{_fmt(lam0)}}}\\right) = {_fmt(v_star)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}} = {_fmt(v_star / 1000.0)}\\text{{ km}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "35_stellar_radial_velocity_from_wavelength_shift", 35, prompt, ans, sol, 5,
        ["forgot_to_convert_speed_to_km_per_s"],
        [{"step": 1, "criterion": "Moving away from Earth deduced from lambda > lambda_0", "marks": 1}, {"step": 2, "criterion": f"Delta lambda = {_fmt(delta_lam)} nm", "marks": 1}, {"step": 3, "criterion": "Formula v = c * Delta lambda / lambda_0", "marks": 1}, {"step": 4, "criterion": f"Speed in m/s = {_fmt(v_star)} m·s⁻¹", "marks": 1}, {"step": 5, "criterion": f"Speed in km/s = {_fmt(v_star / 1000.0)} km·s⁻¹", "marks": 1}],
        {"tier_1": "Delta lambda / lambda_0 = v / c gives radial speed.", "tier_2": "Divide m/s by 1000 to get km/s.", "tier_3": ans},
    )


# 36. Cosmological redshift and expanding universe
def build_36_cosmological_redshift_and_expanding_universe(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the 1920s, Edwin Hubble analyzed the spectra of distant galaxies.\n\n"
        "1. What did Hubble discover about the spectra of almost all distant galaxies?\n"
        "2. What relationship did he establish between a galaxy's distance from Earth and its redshift?\n"
        "3. State the major cosmological theory supported by this observation."
    )
    ans = "1. Their spectral lines are redshifted; 2. The further away a galaxy is from Earth, the greater its redshift (and recessional velocity); 3. The Big Bang theory / Expanding Universe theory."
    sol = (
        "1. Hubble observed that light from almost all distant galaxies exhibited **redshift**, proving that galaxies are moving away from Earth.\n"
        "2. He found that the **redshift is directly proportional to distance**: more distant galaxies are receding faster than nearer ones ($v = H_0 d$).\n"
        "3. This discovery provides direct observational evidence that the **universe is expanding**, supporting the **Big Bang Theory**."
    )
    return _make_q(
        r, "36_cosmological_redshift_and_expanding_universe", 36, prompt, ans, sol, 4,
        ["claimed_galaxies_move_towards_earth_in_expanding_universe"],
        [{"step": 1, "criterion": "Distant galaxies are redshifted", "marks": 1}, {"step": 2, "criterion": "Further galaxies have larger redshift / faster recession", "marks": 2}, {"step": 3, "criterion": "Supports expanding universe / Big Bang theory", "marks": 1}],
        {"tier_1": "Hubble observed redshifts proportional to distance.", "tier_2": "This proves the universe is expanding uniformly.", "tier_3": ans},
    )


# 37. Hubble law velocity distance relationship
def build_37_hubble_law_velocity_distance_relationship(r: random.Random) -> Dict[str, Any]:
    h0 = 70.0  # km/s per Mpc
    d_mpc = r.choice([50, 80, 120, 150])
    v_rec = round(h0 * d_mpc, 1)

    prompt = (
        f"A distant galaxy is located at a distance of ${d_mpc}\\text{{ Mpc}}$ (megaparsecs) from Earth. "
        f"Take the Hubble constant as $H_0 = 70\\text{{ km}}\\cdot\\text{{s}}^{{-1}}\\cdot\\text{{Mpc}}^{{-1}}$.\n\n"
        f"1. State Hubble's Law in words.\n"
        f"2. Using Hubble's Law ($v = H_0 d$), calculate the recessional velocity of this galaxy in $\\text{{km}}\\cdot\\text{{s}}^{{-1}}$."
    )
    ans = f"v = {_fmt(v_rec)} km·s⁻¹"
    sol = (
        "1. **Hubble's Law:** The recessional velocity of a distant galaxy is directly proportional to its distance from Earth.\n"
        f"2. Calculation:\n"
        f"   $$v = H_0 d = (70)({d_mpc}) = {_fmt(v_rec)}\\text{{ km}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "37_hubble_law_velocity_distance_relationship", 37, prompt, ans, sol, 3,
        ["inverted_hubbles_law_multiplication"],
        [{"step": 1, "criterion": "Statement of Hubble's Law", "marks": 1}, {"step": 2, "criterion": "Formula v = H0 * d", "marks": 1}, {"step": 3, "criterion": f"Answer {_fmt(v_rec)} km·s⁻¹", "marks": 1}],
        {"tier_1": "Hubble's Law is v = H0 * d.", "tier_2": f"Multiply {h0} by {d_mpc}.", "tier_3": ans},
    )


# 38. Binary star system periodic Doppler shifts
def build_38_binary_star_system_periodic_doppler_shifts(r: random.Random) -> Dict[str, Any]:
    shift = r.choice([15, 20, 25])
    diagram_spec = _build_binary_star_svg(shift, r.randint(100, 999))
    prompt = (
        "Refer to the accompanying spectral comparison showing laboratory reference absorption lines "
        "alongside the shifted lines observed from Star A in a spectroscopic binary star system.\n\n"
        "1. Based on the diagram, determine whether Star A is currently orbiting towards or away from Earth.\n"
        "2. Predict the spectral line displacement observed half an orbital period later when Star A reaches the opposite side of its orbit.\n"
        "3. Explain why binary stars produce periodic alternating shifts in their spectral lines."
    )
    ans = "1. Away from Earth (redshifted towards longer wavelengths); 2. Shifted towards shorter wavelengths (blueshifted); 3. As the star orbits around the common centre of mass, it alternates between moving towards Earth (blueshift) and away from Earth (redshift)."
    sol = (
        "1. The absorption lines are displaced to the right (towards the longer wavelength / red end), "
        "indicating that Star A is currently **receding / moving away from Earth** (redshift).\n"
        "2. Half an orbit later, Star A will be moving towards Earth, so its lines will be displaced to the left, "
        "exhibiting a **blueshift** (shorter wavelength).\n"
        "3. In a binary system, stars orbit a common centre of mass. During each full orbit, each star moves alternately "
        "towards Earth (producing blueshift) and away from Earth (producing redshift) in a **periodic cycle**."
    )
    return _make_q(
        r, "38_binary_star_system_periodic_doppler_shifts", 38, prompt, ans, sol, 4,
        ["failed_to_recognize_periodic_nature_of_orbital_motion"],
        [{"step": 1, "criterion": "Star A moving away from Earth (redshift)", "marks": 1}, {"step": 2, "criterion": "Opposite side shows blueshift (towards shorter wavelength)", "marks": 1}, {"step": 3, "criterion": "Orbital motion alternates velocity along line of sight", "marks": 2}],
        {"tier_1": "Rightward shift is towards longer wavelength (redshift).", "tier_2": "Circular orbit alternates direction relative to the observer.", "tier_3": ans},
        diagram_spec=diagram_spec,
    )


# 39. Doppler flow meter medical blood flow velocity
def build_39_doppler_flow_meter_medical_blood_flow_velocity(r: random.Random) -> Dict[str, Any]:
    angle = r.choice([30, 45, 60])
    v_blood = r.choice([0.20, 0.35, 0.50])  # m/s
    c_tissue = 1540.0  # m/s in human soft tissue
    f0 = 5.0e6  # 5 MHz ultrasound
    rad = math.radians(angle)
    # Delta f = 2 * f0 * v * cos(theta) / c
    delta_f = round((2.0 * f0 * v_blood * math.cos(rad)) / c_tissue, 1)

    diagram_spec = _build_ultrasound_flow_svg(angle, v_blood, r.randint(100, 999))
    prompt = (
        f"A medical Doppler flowmeter transmits ultrasound of frequency $f_0 = 5{{,}}0\\text{{ MHz}}$ into a patient's artery "
        f"at an angle $\\theta = {angle}^\\circ$ to the direction of blood flow, as illustrated in the schematic diagram.\n"
        f"The speed of ultrasound in human soft tissue is ${c_tissue}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"The reflected signal from moving red blood cells undergoes a frequency shift of $\\Delta f = {_fmt(delta_f)}\\text{{ Hz}}$.\n\n"
        f"1. Identify the moving 'source' or reflector that causes the Doppler shift in this medical diagnostic technique.\n"
        f"2. Using $\\Delta f = \\frac{{2 f_0 v_{{\\text{{blood}}}} \\cos\\theta}}{{c}}$, calculate the speed of blood flow ($v_{{\\text{{blood}}}}$) in $\\text{{m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    ans = f"Red blood cells; v_blood = {_fmt(v_blood)} m·s⁻¹"
    sol = (
        "1. The moving reflectors causing the Doppler shift are **red blood cells (erythrocytes)** flowing within the vessel.\n"
        f"2. Rearrange for $v_{{\\text{{blood}}}}$:\n"
        f"   $$v_{{\\text{{blood}}}} = \\frac{{c \\Delta f}}{{2 f_0 \\cos\\theta}} = \\frac{{({c_tissue})({_fmt(delta_f)})}}{{2(5{{,}}0 \\times 10^6) \\cos({angle}^\\circ)}} = {_fmt(v_blood)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$"
    )
    return _make_q(
        r, "39_doppler_flow_meter_medical_blood_flow_velocity", 39, prompt, ans, sol, 4,
        ["forgot_cosine_factor_in_doppler_flowmeter"],
        [{"step": 1, "criterion": "Identification of red blood cells as reflectors", "marks": 1}, {"step": 2, "criterion": "Formula rearrangement isolating v_blood", "marks": 1}, {"step": 3, "criterion": "Substitution including angle cosine", "marks": 1}, {"step": 4, "criterion": f"Answer v_blood = {_fmt(v_blood)} m·s⁻¹", "marks": 1}],
        {"tier_1": "Ultrasound reflects off flowing red blood cells.", "tier_2": "Remember to include cos(theta) in the denominator.", "tier_3": ans},
        diagram_spec=diagram_spec,
    )


# 40. Fetal heartbeat ultrasound monitor
def build_40_fetal_heartbeat_ultrasound_monitor(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A pregnant woman undergoes a non-invasive prenatal ultrasound examination to monitor the fetal heartbeat.\n\n"
        "1. Explain how the Doppler effect is utilized to detect and measure the fetal heart rate.\n"
        "2. State TWO advantages of using ultrasound rather than X-rays for prenatal diagnostics."
    )
    ans = "1. High-frequency ultrasound waves directed at the fetal heart reflect off the moving heart walls and valve leaflets. The motion shifts the reflected frequency via the Doppler effect, allowing the heart rate and wall velocity to be monitored; 2. Ultrasound uses non-ionizing mechanical sound waves (safe for fetus), whereas X-rays are ionizing radiation that can cause cell damage and fetal mutations."
    sol = (
        "1. **Doppler mechanism:** The ultrasound transducer transmits high-frequency sound waves into the womb. "
        "When these waves strike the **moving muscular walls and valves of the fetal heart**, the reflected sound undergoes "
        "a periodic **Doppler frequency shift** proportional to heart velocity. The electronic system converts these frequency "
        "shifts into an audible heartbeat and heart-rate display.\n"
        "2. **Advantages over X-rays:**\n"
        "   - Ultrasound is **non-ionizing radiation**, presenting no danger of radiation damage or genetic mutations to the fetus.\n"
        "   - Ultrasound provides **real-time dynamic imaging** of moving soft tissues, which X-rays cannot do safely."
    )
    return _make_q(
        r, "40_fetal_heartbeat_ultrasound_monitor", 40, prompt, ans, sol, 4,
        ["believed_ultrasound_emits_ionizing_radiation"],
        [{"step": 1, "criterion": "Explanation of reflection from moving fetal heart walls", "marks": 2}, {"step": 2, "criterion": "Advantage 1: non-ionizing / safe for fetus", "marks": 1}, {"step": 3, "criterion": "Advantage 2: real-time soft tissue monitoring", "marks": 1}],
        {"tier_1": "Moving heart walls reflect ultrasound with a frequency shift.", "tier_2": "Sound waves are non-ionizing, unlike X-rays.", "tier_3": ans},
    )


# 41. Acoustic Doppler current profiler oceanography
def build_41_acoustic_doppler_current_profiler_oceanography(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Oceanographers and marine engineers utilize an Acoustic Doppler Current Profiler (ADCP) mounted beneath a research vessel.\n\n"
        "1. Explain how an ADCP measures water current velocities at various depths.\n"
        "2. Name the physical entities suspended in water that act as sound scatterers/reflectors."
    )
    ans = "1. The ADCP transmits acoustic pings into the water column. The pings reflect off moving suspended particles, and the Doppler frequency shift of the returned echo reveals the velocity of the water current; 2. Suspended sediment particles and zooplankton/plankton."
    sol = (
        "1. The instrument emits ultrasonic pulses into the water column. As sound travels downward, it scatters off "
        "suspended particles drifting with the current. By measuring the **Doppler shift in the frequency of the scattered echo**, "
        "the computer calculates the current velocity at different water depths based on return transit times.\n"
        "2. Sound scatters off **suspended microscopic sediment particles**, organic debris, and **zooplankton/plankton** drifting in the water."
    )
    return _make_q(
        r, "41_acoustic_doppler_current_profiler_oceanography", 41, prompt, ans, sol, 3,
        ["assumed_water_molecules_themselves_reflect_sound_directly"],
        [{"step": 1, "criterion": "Explanation of Doppler shift from moving suspended scatterers", "marks": 2}, {"step": 2, "criterion": "Identification of plankton or sediment particles as reflectors", "marks": 1}],
        {"tier_1": "Sound bounces off drifting particles in the water.", "tier_2": "The frequency shift of the echo is proportional to current speed.", "tier_3": ans},
    )


# 42. Weather Doppler radar precipitation tracking
def build_42_weather_doppler_radar_precipitation_tracking(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Meteorologists use pulse-Doppler weather radar to monitor storms and severe weather systems.\n\n"
        "1. Explain how Doppler radar detects the wind speed and direction of rotating storms (such as tornadoes).\n"
        "2. What property of the returned radar echo indicates the **rate of precipitation (rain intensity)** versus the **speed of wind**?"
    )
    ans = "1. Radar pulses bounce off raindrops and hail. If precipitation moves towards the radar, the echo is blueshifted; if moving away, it is redshifted. Rotating storms show adjacent areas of approaching and receding winds (couplets); 2. Intensity/amplitude of the echo indicates rainfall rate; frequency shift indicates wind speed."
    sol = (
        "1. The radar antenna transmits radio wave pulses that reflect off **falling raindrops, snowflakes, and hail**. "
        "Precipitation carried towards the radar reflects waves at a **higher frequency**; precipitation moving away reflects "
        "at a **lower frequency**. A rotating vortex (mesocyclone) produces a distinct side-by-side pattern of approaching and "
        "receding winds (a Doppler velocity couplet).\n"
        "2. **Distinction:**\n"
        "   - **Echo Intensity (Reflectivity / Amplitude):** Proportional to the size and concentration of raindrops (rain rate).\n"
        "   - **Doppler Frequency Shift ($\\Delta f$):** Directly proportional to the radial velocity of the raindrops (wind speed)."
    )
    return _make_q(
        r, "42_weather_doppler_radar_precipitation_tracking", 42, prompt, ans, sol, 4,
        ["confused_radar_reflectivity_with_doppler_frequency_shift"],
        [{"step": 1, "criterion": "Reflection from precipitation with Doppler frequency shift", "marks": 2}, {"step": 2, "criterion": "Echo amplitude gives rain intensity", "marks": 1}, {"step": 3, "criterion": "Frequency shift gives wind velocity", "marks": 1}],
        {"tier_1": "Frequency shift measures wind speed.", "tier_2": "Echo brightness/amplitude measures rainfall rate.", "tier_3": ans},
    )


# 43. Satellite Doppler tracking and GPS
def build_43_satellite_doppler_tracking_and_gps(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A low-Earth-orbit satellite orbiting at $7{{,}}5\\text{{ km}}\\cdot\\text{{s}}^{{-1}}$ transmits radio telemetry at $400\\text{{ MHz}}$.\n\n"
        "1. Describe the change in received telemetry frequency as the satellite passes from horizon to horizon over a ground tracking station.\n"
        "2. Why must modern GPS receivers compensate for the Doppler effect when locking onto satellite signals?"
    )
    ans = "1. Highest frequency as it rises and approaches, drops to true frequency at zenith, and drops to lowest frequency as it recedes towards the opposite horizon; 2. High satellite orbital speeds cause Doppler shifts that would otherwise prevent the receiver from matching the signal carrier frequency and code timing."
    sol = (
        "1. As the satellite rises above the horizon and approaches the ground station, the received frequency is **higher than 400 MHz**. "
        "At the zenith (closest approach), the line-of-sight velocity is zero, so the frequency momentarily equals **400 MHz**. "
        "As it recedes towards the opposite horizon, the frequency drops **below 400 MHz**.\n"
        "2. GPS satellites travel at high orbital velocities (~$3{{,}}9\\text{{ km/s}}$). The resulting Doppler frequency shifts "
        "(up to $\\pm 5\\text{{ kHz}}$ on the $L_1$ frequency) would prevent the receiver's tracking loop from acquiring and decoding "
        "the pseudo-random timing codes unless the Doppler shift is calculated and compensated."
    )
    return _make_q(
        r, "43_satellite_doppler_tracking_and_gps", 43, prompt, ans, sol, 4,
        ["assumed_satellite_signals_do_not_experience_doppler_shift"],
        [{"step": 1, "criterion": "Approach (higher), zenith (true), recede (lower)", "marks": 2}, {"step": 2, "criterion": "GPS orbital velocity causes frequency shifts that require receiver frequency compensation", "marks": 2}],
        {"tier_1": "Satellite orbits create line-of-sight velocity shifts.", "tier_2": "GPS receivers must scan Doppler frequency offsets to lock signals.", "tier_3": ans},
    )


# 44. Sonic boom and Mach number threshold
def build_44_sonic_boom_and_mach_number_threshold(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A supersonic jet accelerates from subsonic speed ($v_S < v$) through the sound barrier ($v_S = v$) "
        "to supersonic flight ($v_S > v$) in air where $v = 340\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        "1. Describe what happens to the circular wavefronts ahead of the aircraft as $v_S \\to v$.\n"
        "2. Explain the physical origin of a **sonic boom** heard on the ground when $v_S > v$."
    )
    ans = "1. Wavefronts pile up directly on top of each other at the nose of the aircraft, creating a high-pressure barrier; 2. Overlapping spherical wavefronts form a conical shock wave (Mach cone) of intense high pressure. When this pressure discontinuity sweeps over an observer on the ground, a loud explosive sonic boom is heard."
    sol = (
        "1. As $v_S \\to v$, the aircraft travels as fast as the sound waves it creates. The wavefronts cannot escape ahead "
        "and **pile up directly on top of each other**, producing an extreme constructive interference pressure ridge (the sound barrier).\n"
        "2. When $v_S > v$, the aircraft outruns its own sound. The spherical wavefronts overlap constructively along a V-shaped cone "
        "(the **Mach cone**). This cone forms a steep **shock wave** of sudden high pressure followed by sudden low pressure. "
        "When this shock wave passes over an observer on the ground, the sudden pressure jump is heard as a loud **sonic boom**."
    )
    return _make_q(
        r, "44_sonic_boom_and_mach_number_threshold", 44, prompt, ans, sol, 4,
        ["thought_sonic_boom_only_happens_at_the_exact_moment_breaking_sound_barrier"],
        [{"step": 1, "criterion": "Wavefronts pile up at sound barrier as vs -> v", "marks": 2}, {"step": 2, "criterion": "Mach cone shock wave constructive interference", "marks": 1}, {"step": 3, "criterion": "Sudden pressure discontinuity creates sonic boom on ground", "marks": 1}],
        {"tier_1": "Supersonic aircraft drag a continuous Mach shock cone behind them.", "tier_2": "The sonic boom is heard whenever the cone edge sweeps over an observer.", "tier_3": ans},
    )


# 45. Temperature effect on sound speed and Doppler frequency
def build_45_temperature_effect_on_sound_speed_and_doppler_frequency(r: random.Random) -> Dict[str, Any]:
    fs = 500
    vs = 30.0
    # On cold day (T = 5 C): v = 334 m/s
    # On hot day (T = 35 C): v = 352 m/s
    v_cold = 334.0
    v_hot = 352.0
    fl_cold = round((v_cold / (v_cold - vs)) * fs, 2)
    fl_hot = round((v_hot / (v_hot - vs)) * fs, 2)

    prompt = (
        f"A police siren of frequency ${fs}\\text{{ Hz}}$ approaches a stationary listener at ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"The speed of sound in air depends on temperature: $v = {_fmt(v_cold)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ on a cold winter morning "
        f"and $v = {_fmt(v_hot)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ on a hot summer afternoon.\n\n"
        f"1. Calculate the detected frequency on the cold winter morning.\n"
        f"2. Calculate the detected frequency on the hot summer afternoon.\n"
        f"3. State on which day the Doppler frequency shift ($\\Delta f = f_L - f_S$) is greater, and provide a mathematical reason."
    )
    ans = f"Cold: {_fmt(fl_cold)} Hz; Hot: {_fmt(fl_hot)} Hz; Greater shift on cold day (lower sound speed increases vs/v ratio)"
    sol = (
        f"1. Cold day: $$f_{{L,\\text{{cold}}}} = \\left(\\frac{{{_fmt(v_cold)}}}{{{_fmt(v_cold)} - {_fmt(vs)}}}\\right) ({fs}) = {_fmt(fl_cold)}\\text{{ Hz}}$$\n"
        f"2. Hot day: $$f_{{L,\\text{{hot}}}} = \\left(\\frac{{{_fmt(v_hot)}}}{{{_fmt(v_hot)} - {_fmt(vs)}}}\\right) ({fs}) = {_fmt(fl_hot)}\\text{{ Hz}}$$\n"
        f"3. The Doppler frequency shift is **greater on the cold winter day** "
        f"($\\Delta f_{{\\text{{cold}}}} = {_fmt(round(fl_cold - fs, 2))}\\text{{ Hz}} > \\Delta f_{{\\text{{hot}}}} = {_fmt(round(fl_hot - fs, 2))}\\text{{ Hz}}$). "
        f"Reason: Since $v$ is smaller on the cold day, the ratio $\\frac{{v_S}}{{v}}$ is larger, producing a greater fractional frequency shift."
    )
    return _make_q(
        r, "45_temperature_effect_on_sound_speed_and_doppler_frequency", 45, prompt, ans, sol, 5,
        ["thought_higher_sound_speed_produces_larger_doppler_shift"],
        [{"step": 1, "criterion": f"Cold day frequency = {_fmt(fl_cold)} Hz", "marks": 2}, {"step": 2, "criterion": f"Hot day frequency = {_fmt(fl_hot)} Hz", "marks": 2}, {"step": 3, "criterion": "Cold day has greater shift because vs/v ratio is larger", "marks": 1}],
        {"tier_1": "Calculate fL for both temperatures using the corresponding wave speeds.", "tier_2": "A smaller sound speed v increases the relative speed ratio vs / v.", "tier_3": ans},
    )


# 46. Wind effect on Doppler frequency
def build_46_wind_effect_on_doppler_frequency(r: random.Random) -> Dict[str, Any]:
    fs = 400
    vs = 20.0
    v_still = 340.0
    v_wind = 15.0  # Wind blowing from source to listener
    # Medium is moving with speed v_wind towards listener: v_eff = v_still + v_wind = 355 m/s
    v_eff = v_still + v_wind
    fl_wind = round((v_eff / (v_eff - vs)) * fs, 2)
    fl_no_wind = round((v_still / (v_still - vs)) * fs, 2)

    prompt = (
        f"A sound source of frequency ${fs}\\text{{ Hz}}$ travels at ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ towards a stationary observer. "
        f"The speed of sound in still air is ${v_still}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"A strong tailwind blows at ${_fmt(v_wind)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ from the source directly towards the observer.\n\n"
        f"1. Explain how the wind alters the effective speed of sound relative to the observer.\n"
        f"2. Calculate the frequency detected by the observer with the wind blowing ($v_{{\\text{{eff}}}} = {v_still} + {_fmt(v_wind)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$)."
    )
    ans = f"v_eff = {_fmt(v_eff)} m·s⁻¹; fL = {_fmt(fl_wind)} Hz"
    sol = (
        f"1. Because sound propagates through the air medium, a wind blowing in the direction of sound propagation "
        f"adds to the speed of sound relative to the ground observer: $v_{{\\text{{eff}}}} = v + v_{{\\text{{wind}}}} = {v_still} + {_fmt(v_wind)} = {_fmt(v_eff)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"2. Using the effective sound speed in the Doppler formula:\n"
        f"   $$f_L = \\left(\\frac{{v_{{\\text{{eff}}}}}}{{v_{{\\text{{eff}}}} - v_S}}\\right) f_S = \\left(\\frac{{{_fmt(v_eff)}}}{{{_fmt(v_eff)} - {_fmt(vs)}}}\\right) ({fs}) = \\left(\\frac{{{_fmt(v_eff)}}}{{{_fmt(v_eff - vs)}}}\\right) ({fs}) = {_fmt(fl_wind)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "46_wind_effect_on_doppler_frequency", 46, prompt, ans, sol, 4,
        ["subtracted_wind_speed_instead_of_adding_for_tailwind"],
        [{"step": 1, "criterion": "Wind speed adds to sound speed relative to ground observer", "marks": 1}, {"step": 2, "criterion": f"Effective speed v_eff = {_fmt(v_eff)} m·s⁻¹", "marks": 1}, {"step": 3, "criterion": "Substitution into Doppler formula", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(fl_wind)} Hz", "marks": 1}],
        {"tier_1": "Wind carries the sound waves: add wind speed for tailwind.", "tier_2": "Replace v with (v + v_wind) in the Doppler formula.", "tier_3": ans},
    )


# 47. Angled approach non head on Doppler shift
def build_47_angled_approach_non_head_on_doppler_shift(r: random.Random) -> Dict[str, Any]:
    fs = 600
    vs = 30.0
    angle = r.choice([30, 45, 60])
    v = 340.0
    rad = math.radians(angle)
    v_radial = round(vs * math.cos(rad), 2)
    fl = round((v / (v - v_radial)) * fs, 2)

    prompt = (
        f"A car travelling at ${_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ on a straight highway sounds its horn of frequency ${fs}\\text{{ Hz}}$. "
        f"A stationary observer stands in a field at an angle $\\theta = {angle}^\\circ$ off the line of travel of the car. "
        f"Take the speed of sound as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Explain why the Doppler shift depends only on the component of velocity directed towards the observer.\n"
        f"2. Calculate the radial velocity component ($v_{{\\text{{radial}}}} = v_S \\cos\\theta$) of the car towards the observer.\n"
        f"3. Calculate the frequency heard by the observer at this instant."
    )
    ans = f"v_radial = {_fmt(v_radial)} m·s⁻¹; fL = {_fmt(fl)} Hz"
    sol = (
        "1. The Doppler effect occurs strictly due to relative motion along the line of sight connecting source and observer. "
        "Motion perpendicular to the line of sight does not compress wavefronts in the observer's direction.\n"
        f"2. Component along line of sight:\n"
        f"   $$v_{{\\text{{radial}}}} = v_S \\cos({angle}^\\circ) = ({_fmt(vs)}) \\cos({angle}^\\circ) = {_fmt(v_radial)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"3. Using $v_{{\\text{{radial}}}}$ in the Doppler formula:\n"
        f"   $$f_L = \\left(\\frac{{v}}{{v - v_{{\\text{{radial}}}}}}\\right) f_S = \\left(\\frac{{{v}}}{{{v} - {_fmt(v_radial)}}}\\right) ({fs}) = {_fmt(fl)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "47_angled_approach_non_head_on_doppler_shift", 47, prompt, ans, sol, 5,
        ["used_total_velocity_instead_of_radial_component_for_angled_observer"],
        [{"step": 1, "criterion": "Explanation of line-of-sight component velocity", "marks": 1}, {"step": 2, "criterion": f"Radial component = {_fmt(v_radial)} m·s⁻¹", "marks": 2}, {"step": 3, "criterion": "Substitution into Doppler formula", "marks": 1}, {"step": 4, "criterion": f"Answer {_fmt(fl)} Hz", "marks": 1}],
        {"tier_1": "Only the component of velocity along the line of sight matters.", "tier_2": "v_radial = vs * cos(theta).", "tier_3": ans},
    )


# 48. Laboratory whirling buzzer or tuning fork experiment
def build_48_laboratory_whirling_buzzer_or_tuning_fork_experiment(r: random.Random) -> Dict[str, Any]:
    fs = 440
    # Whirling in horizontal circle of radius r_circ with angular velocity omega
    # tangential speed v_tan = 12 m/s
    v_tan = r.choice([10.0, 12.0, 15.0])
    v = 340.0
    fl_max = round((v / (v - v_tan)) * fs, 1)
    fl_min = round((v / (v + v_tan)) * fs, 1)

    prompt = (
        f"In a classroom demonstration of the Doppler effect, an educator attaches an electronic buzzer emitting a constant frequency "
        f"of ${fs}\\text{{ Hz}}$ to a sturdy string and whirls it in a horizontal circle at a tangential speed of ${_fmt(v_tan)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"A learner stands several meters away in the plane of the circle. Take the speed of sound as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Describe how the pitch heard by the learner varies during one complete revolution of the buzzer.\n"
        f"2. Calculate the maximum frequency ($f_{{\\max}}$) heard by the learner.\n"
        f"3. Calculate the minimum frequency ($f_{{\\min}}$) heard by the learner."
    )
    ans = f"Pitch fluctuates periodically; f_max = {_fmt(fl_max)} Hz; f_min = {_fmt(fl_min)} Hz"
    sol = (
        "1. The pitch fluctuates periodically between a maximum and a minimum once per revolution. "
        "The pitch is highest when the buzzer moves directly towards the learner, equals 440 Hz when moving perpendicular "
        "to the line of sight, and reaches a minimum when moving directly away.\n"
        f"2. Maximum frequency (tangential velocity directed towards learner):\n"
        f"   $$f_{{\\max}} = \\left(\\frac{{v}}{{v - v_{{\\text{{tan}}}}}}\\right) f_S = \\left(\\frac{{{v}}}{{{v} - {_fmt(v_tan)}}}\\right) ({fs}) = {_fmt(fl_max)}\\text{{ Hz}}$$\n"
        f"3. Minimum frequency (tangential velocity directed away from learner):\n"
        f"   $$f_{{\\min}} = \\left(\\frac{{v}}{{v + v_{{\\text{{tan}}}}}}\\right) f_S = \\left(\\frac{{{v}}}{{{v} + {_fmt(v_tan)}}}\\right) ({fs}) = {_fmt(fl_min)}\\text{{ Hz}}$$"
    )
    return _make_q(
        r, "48_laboratory_whirling_buzzer_or_tuning_fork_experiment", 48, prompt, ans, sol, 5,
        ["assumed_pitch_stays_constant_in_circular_motion"],
        [{"step": 1, "criterion": "Periodic pitch fluctuation described across revolution", "marks": 2}, {"step": 2, "criterion": f"f_max calculation = {_fmt(fl_max)} Hz", "marks": 2}, {"step": 3, "criterion": f"f_min calculation = {_fmt(fl_min)} Hz", "marks": 1}],
        {"tier_1": "Tangential velocity points towards the observer on one side and away on the other.", "tier_2": "Use (v - v_tan) for max and (v + v_tan) for min.", "tier_3": ans},
    )


# 49. Capstone comprehensive Doppler exam rider
def build_49_capstone_comprehensive_doppler_exam_rider(r: random.Random) -> Dict[str, Any]:
    fs = 650
    vs = r.choice([25.0, 30.0])
    v = 340.0
    fl_app = round((v / (v - vs)) * fs, 2)
    fl_rec = round((v / (v + vs)) * fs, 2)

    prompt = (
        f"An emergency response vehicle sounding its siren at ${fs}\\text{{ Hz}}$ travels along a straight road at a constant speed.\n"
        f"A stationary recording device at the roadside records a frequency of ${_fmt(fl_app)}\\text{{ Hz}}$ as the vehicle approaches. "
        f"Take the speed of sound in air as ${v}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. State the **Doppler Effect** in words.\n"
        f"2. Calculate the speed ($v_S$) of the emergency response vehicle.\n"
        f"3. Calculate the frequency recorded by the device after the vehicle passes and moves away.\n"
        f"4. Name ONE application of the Doppler effect in medicine and ONE in astrophysics."
    )
    ans = f"1. Apparent change in frequency of a wave detected by an observer when source and observer move relative to medium; 2. vS = {_fmt(vs)} m·s⁻¹; 3. fL_rec = {_fmt(fl_rec)} Hz; 4. Medicine: Doppler ultrasound (blood flow/fetal heart); Astrophysics: Redshift (expanding universe)."
    sol = (
        "1. **Doppler Effect:** The apparent change in frequency (or pitch) of a wave detected by an observer "
        "because the source and observer have different velocities relative to the medium of propagation. [2]\n"
        f"2. Speed of vehicle ($v_S$):\n"
        f"   $$f_L = \\left(\\frac{{v}}{{v - v_S}}\\right) f_S \\implies {_fmt(fl_app)} = \\left(\\frac{{{v}}}{{{v} - v_S}}\\right) ({fs})$$\n"
        f"   $${v} - v_S = \\frac{{{v} \\times {fs}}}{{{_fmt(fl_app)}}} = {_fmt((v * fs) / fl_app, 2)}$$\n"
        f"   $$v_S = {v} - {_fmt((v * fs) / fl_app, 2)} = {_fmt(vs)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$$\n"
        f"3. Receding frequency:\n"
        f"   $$f_{{L,\\text{{rec}}}} = \\left(\\frac{{v}}{{v + v_S}}\\right) f_S = \\left(\\frac{{{v}}}{{{v} + {_fmt(vs)}}}\\right) ({fs}) = {_fmt(fl_rec)}\\text{{ Hz}}$$\n"
        "4. Applications:\n"
        "   - **Medicine:** Doppler ultrasound flowmeter (measuring blood flow velocity or monitoring fetal heartbeat).\n"
        "   - **Astrophysics:** Redshift of distant galaxies providing observational evidence for an expanding universe."
    )
    return _make_q(
        r, "49_capstone_comprehensive_doppler_exam_rider", 49, prompt, ans, sol, 8,
        ["sign_errors_in_exam_rider_doppler_formula"],
        [{"step": 1, "criterion": "Definition of Doppler effect", "marks": 2}, {"step": 2, "criterion": "Formula and substitution for vehicle speed", "marks": 2}, {"step": 3, "criterion": f"Speed vS = {_fmt(vs)} m·s⁻¹", "marks": 1}, {"step": 4, "criterion": f"Receding frequency = {_fmt(fl_rec)} Hz", "marks": 2}, {"step": 5, "criterion": "Two valid applications stated", "marks": 1}],
        {"tier_1": "Use fL = [v / (v - vs)] * fS to find vs first.", "tier_2": "Then use vs in fL = [v / (v + vs)] * fS for receding frequency.", "tier_3": ans},
    )


# 50. Diagnostic autopsy and misconception remediation
def build_50_diagnostic_autopsy_and_misconception_remediation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Evaluate the following four statements made by learners about the Doppler effect and classify each as **CORRECT** or **INCORRECT**. "
        "For each incorrect statement, provide the correct scientific explanation:\n\n"
        "**Statement A:** *\"When an ambulance approaches a stationary listener, the sound waves travel through the air at a faster speed than 340 m/s.\"*\n"
        "**Statement B:** *\"A redshift observed in light from a distant star proves that the speed of light from that star has decreased.\"*\n"
        "**Statement C:** *\"When a sound source moves towards an observer, the observed wavelength is shorter than the source wavelength.\"*\n"
        "**Statement D:** *\"The Doppler effect explains why an ambulance siren sounds louder when it is closer to you.\"*"
    )
    ans = "Statement A: INCORRECT (sound speed depends only on the medium, not source motion); Statement B: INCORRECT (light speed in vacuum is constant c; redshift is caused by wave stretching / relative motion); Statement C: CORRECT (wavefronts are compressed ahead); Statement D: INCORRECT (loudness changes due to intensity/distance; Doppler effect changes frequency/pitch)."
    sol = (
        "1. **Statement A is INCORRECT.** Sound speed in air depends solely on the physical properties of the transmitting medium "
        "(temperature, pressure, medium density), NOT on the velocity of the emitting source. The wave speed remains constant at 340 m/s.\n"
        "2. **Statement B is INCORRECT.** According to the postulates of physics, the speed of light in a vacuum is universally constant ($c$). "
        "Redshift is caused by the elongation of the observed wavelength due to relative motion (or cosmological space expansion), not a change in light speed.\n"
        "3. **Statement C is CORRECT.** Ahead of the moving source, successive crests are emitted closer together, compressing the wavelength in the medium ($\\lambda_L < \\lambda_S$).\n"
        "4. **Statement D is INCORRECT.** Loudness depends on wave amplitude and the inverse-square decrease of intensity with distance. "
        "The Doppler effect explains the change in **pitch (frequency)**, not volume."
    )
    return _make_q(
        r, "50_diagnostic_autopsy_and_misconception_remediation", 50, prompt, ans, sol, 6,
        ["failed_diagnostic_autopsy_misconceptions"],
        [{"step": 1, "criterion": "Statement A incorrect: sound speed is medium-dependent", "marks": 1}, {"step": 2, "criterion": "Statement B incorrect: light speed c is constant", "marks": 2}, {"step": 3, "criterion": "Statement C correct: wavelength is compressed ahead", "marks": 1}, {"step": 4, "criterion": "Statement D incorrect: loudness vs pitch distinction", "marks": 2}],
        {"tier_1": "Sound and light speeds do not depend on the motion of the source.", "tier_2": "Doppler effect explains frequency/pitch, not loudness.", "tier_3": ans},
    )


# Roster of Subskills 26–50
SUBSKILLS_26_50: Dict[str, Any] = {
    "26_frequency_vs_time_graph_approaching_passing_receding": build_26_frequency_vs_time_graph_approaching_passing_receding,
    "27_frequency_vs_source_velocity_linear_approximation": build_27_frequency_vs_source_velocity_linear_approximation,
    "28_wavelength_vs_source_velocity_linear_relationship": build_28_wavelength_vs_source_velocity_linear_relationship,
    "29_doppler_echo_reflection_stationary_target": build_29_doppler_echo_reflection_stationary_target,
    "30_doppler_echo_reflection_moving_target": build_30_doppler_echo_reflection_moving_target,
    "31_radar_speed_gun_beat_frequency_calculation": build_31_radar_speed_gun_beat_frequency_calculation,
    "32_doppler_effect_with_light_intro": build_32_doppler_effect_with_light_intro,
    "33_redshift_definition_and_spectral_line_displacement": build_33_redshift_definition_and_spectral_line_displacement,
    "34_blueshift_definition_and_approaching_celestial_objects": build_34_blueshift_definition_and_approaching_celestial_objects,
    "35_stellar_radial_velocity_from_wavelength_shift": build_35_stellar_radial_velocity_from_wavelength_shift,
    "36_cosmological_redshift_and_expanding_universe": build_36_cosmological_redshift_and_expanding_universe,
    "37_hubble_law_velocity_distance_relationship": build_37_hubble_law_velocity_distance_relationship,
    "38_binary_star_system_periodic_doppler_shifts": build_38_binary_star_system_periodic_doppler_shifts,
    "39_doppler_flow_meter_medical_blood_flow_velocity": build_39_doppler_flow_meter_medical_blood_flow_velocity,
    "40_fetal_heartbeat_ultrasound_monitor": build_40_fetal_heartbeat_ultrasound_monitor,
    "41_acoustic_doppler_current_profiler_oceanography": build_41_acoustic_doppler_current_profiler_oceanography,
    "42_weather_doppler_radar_precipitation_tracking": build_42_weather_doppler_radar_precipitation_tracking,
    "43_satellite_doppler_tracking_and_gps": build_43_satellite_doppler_tracking_and_gps,
    "44_sonic_boom_and_mach_number_threshold": build_44_sonic_boom_and_mach_number_threshold,
    "45_temperature_effect_on_sound_speed_and_doppler_frequency": build_45_temperature_effect_on_sound_speed_and_doppler_frequency,
    "46_wind_effect_on_doppler_frequency": build_46_wind_effect_on_doppler_frequency,
    "47_angled_approach_non_head_on_doppler_shift": build_47_angled_approach_non_head_on_doppler_shift,
    "48_laboratory_whirling_buzzer_or_tuning_fork_experiment": build_48_laboratory_whirling_buzzer_or_tuning_fork_experiment,
    "49_capstone_comprehensive_doppler_exam_rider": build_49_capstone_comprehensive_doppler_exam_rider,
    "50_diagnostic_autopsy_and_misconception_remediation": build_50_diagnostic_autopsy_and_misconception_remediation,
}
