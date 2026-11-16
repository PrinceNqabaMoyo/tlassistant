"""Grade 10 Physical Sciences — Waves, Sound & Light: Archetypes 01–25.
========================================================================
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/PhysicalSciences_Gr10/Term 1/:
- 07. Transverse pulses.md
- 08. Transverse waves.md

Covers:
- 01–05: Transverse pulses (definition, medium, amplitude, pulse length, pulse speed v = d/t).
- 06–10: Superposition of pulses (constructive interference, destructive interference, equal amplitudes, post-interference propagation).
- 11–18: Transverse waves fundamentals (crests, troughs, amplitude, wavelength, points in phase vs opposite phase, period T, frequency f = 1/T).
- 19–25: Wave equation and graph analysis (v = f * lambda, displacement-position and displacement-time graphs, ripple tank applications).
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

TERM = 1
CAPS_WEIGHT = 20
SUGGESTED_DURATION = 6
TOPIC_ID = "grade10_waves_sound_light"
LEARNING_OBJECTIVE = "ps10_waves_pulses"


def _fmt_sa(val: float | int, places: int = 2) -> str:
    """Format number with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _fmt_katex(val: float | int, places: int = 2) -> str:
    """Format number with KaTeX comma decimal notation {x{,}y}."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


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

def _svg_pulse(
    amp_cm: float,
    length_cm: float,
    seed: int,
    show_labels: bool = True,
) -> str:
    """Generate inline SVG for a single transverse pulse on a string."""
    w, h = 420, 200
    base_y = 130
    scale_y = 12.0
    scale_x = 16.0
    
    peak_y = base_y - (amp_cm * scale_y)
    pulse_half_px = (length_cm * scale_x) / 2.0
    cx = 210
    x_start = cx - pulse_half_px
    x_end = cx + pulse_half_px

    # Smooth bell-like pulse curve using bezier
    ctrl_y = peak_y - 10
    d = (
        f"M 30 {base_y} L {x_start:.1f} {base_y} "
        f"C {x_start + pulse_half_px*0.5:.1f} {base_y}, {cx - pulse_half_px*0.25:.1f} {peak_y:.1f}, {cx:.1f} {peak_y:.1f} "
        f"C {cx + pulse_half_px*0.25:.1f} {peak_y:.1f}, {x_end - pulse_half_px*0.5:.1f} {base_y}, {x_end:.1f} {base_y} "
        f"L 390 {base_y}"
    )

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .string { stroke: #0284c7; stroke-width: 3; fill: none; stroke-linecap: round; }',
        '    .base { stroke: #94a3b8; stroke-width: 1.5; stroke-dasharray: 4,4; }',
        '    .dim { stroke: #dc2626; stroke-width: 1.5; }',
        '    .txt { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; fill: #0f172a; font-weight: bold; }',
        '  </style>',
        f'  <line x1="20" y1="{base_y}" x2="400" y2="{base_y}" class="base" />',
        f'  <path d="{d}" class="string" />',
    ]
    if show_labels:
        # Amplitude dimension line
        svg.append(f'  <line x1="{cx}" y1="{base_y}" x2="{cx}" y2="{peak_y:.1f}" class="dim" />')
        svg.append(f'  <circle cx="{cx}" cy="{peak_y:.1f}" r="3.5" fill="#dc2626" />')
        svg.append(f'  <text x="{cx + 10}" y="{(base_y + peak_y)/2:.1f}" class="txt" fill="#dc2626">A = {_fmt_sa(amp_cm)} cm</text>')
        # Pulse length dimension line
        dim_y = base_y + 35
        svg.append(f'  <line x1="{x_start:.1f}" y1="{dim_y}" x2="{x_end:.1f}" y2="{dim_y}" class="dim" />')
        svg.append(f'  <line x1="{x_start:.1f}" y1="{base_y + 10}" x2="{x_start:.1f}" y2="{dim_y + 5}" stroke="#dc2626" stroke-width="1" />')
        svg.append(f'  <line x1="{x_end:.1f}" y1="{base_y + 10}" x2="{x_end:.1f}" y2="{dim_y + 5}" stroke="#dc2626" stroke-width="1" />')
        svg.append(f'  <text x="{cx}" y="{dim_y + 18}" class="txt" text-anchor="middle" fill="#dc2626">Pulse length = {_fmt_sa(length_cm)} cm</text>')
    svg.append('</svg>')
    return "\n".join(svg)


def _svg_two_pulses(
    a1_cm: float,
    a2_cm: float,
    side1: str = "crest",
    side2: str = "crest",
) -> str:
    """Generate inline SVG for two pulses approaching each other."""
    w, h = 440, 220
    base_y = 110
    scale = 10.0

    # Pulse 1 at left
    cx1 = 120
    dy1 = -a1_cm * scale if side1 == "crest" else a1_cm * scale
    p1 = f"M 30 {base_y} L 70 {base_y} Q {cx1} {base_y + 2*dy1} 170 {base_y} L 220 {base_y}"
    
    # Pulse 2 at right
    cx2 = 320
    dy2 = -a2_cm * scale if side2 == "crest" else a2_cm * scale
    p2 = f"M 220 {base_y} L 270 {base_y} Q {cx2} {base_y + 2*dy2} 370 {base_y} L 410 {base_y}"

    arrow1_y = base_y - 35 if side1 == "crest" else base_y + 35
    arrow1_poly = f"190,{base_y - 39} 198,{base_y - 35} 190,{base_y - 31}" if side1 == "crest" else f"190,{base_y + 31} 198,{base_y + 35} 190,{base_y + 39}"
    arrow2_y = base_y - 35 if side2 == "crest" else base_y + 35
    arrow2_poly = f"250,{base_y - 39} 242,{base_y - 35} 250,{base_y - 31}" if side2 == "crest" else f"250,{base_y + 31} 242,{base_y + 35} 250,{base_y + 39}"
    label1_y = base_y + dy1 - 8 if side1 == "crest" else base_y + dy1 + 18
    sign1 = "+" if side1 == "crest" else "-"
    label2_y = base_y + dy2 - 8 if side2 == "crest" else base_y + dy2 + 18
    sign2 = "+" if side2 == "crest" else "-"

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .string { stroke: #0284c7; stroke-width: 2.8; fill: none; stroke-linecap: round; }',
        '    .base { stroke: #94a3b8; stroke-width: 1.2; stroke-dasharray: 4,4; }',
        '    .arrow { stroke: #16a34a; stroke-width: 2; fill: #16a34a; }',
        '    .txt { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; fill: #0f172a; font-weight: bold; }',
        '  </style>',
        f'  <line x1="20" y1="{base_y}" x2="420" y2="{base_y}" class="base" />',
        f'  <path d="{p1} {p2}" class="string" />',
        # Velocity arrows
        f'  <line x1="140" y1="{arrow1_y}" x2="190" y2="{arrow1_y}" class="arrow" />',
        f'  <polygon points="{arrow1_poly}" fill="#16a34a" />',
        f'  <line x1="300" y1="{arrow2_y}" x2="250" y2="{arrow2_y}" class="arrow" />',
        f'  <polygon points="{arrow2_poly}" fill="#16a34a" />',
        # Labels
        f'  <text x="{cx1}" y="{label1_y}" class="txt" text-anchor="middle" fill="#0284c7">A_1 = {sign1}{_fmt_sa(a1_cm)} cm</text>',
        f'  <text x="{cx2}" y="{label2_y}" class="txt" text-anchor="middle" fill="#0284c7">A_2 = {sign2}{_fmt_sa(a2_cm)} cm</text>',
        '</svg>',
    ]
    return "\n".join(svg)


def _svg_transverse_wave(
    amp: float,
    wavelength: float,
    cycles: float = 2.0,
    x_axis_label: str = "Position x (m)",
    y_axis_label: str = "Displacement y (cm)",
    unit_x: str = "m",
    unit_y: str = "cm",
) -> str:
    """Generate inline SVG for a sinusoidal transverse wave graph."""
    w, h = 480, 240
    ox, oy = 50, 120
    scale_y = 60.0 / max(amp, 0.1)
    plot_width = 380.0
    dx_per_wave = plot_width / cycles

    pts = []
    steps = 100
    for i in range(steps + 1):
        frac = i / steps
        x_val = frac * cycles * wavelength
        px = ox + frac * plot_width
        py = oy - (amp * math.sin(2 * math.pi * frac * cycles)) * scale_y
        pts.append(f"{px:.1f},{py:.1f}")

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="230" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .axis { stroke: #0f172a; stroke-width: 1.5; }',
        '    .wave { stroke: #2563eb; stroke-width: 2.5; fill: none; }',
        '    .grid { stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 3,3; }',
        '    .dim { stroke: #dc2626; stroke-width: 1.5; stroke-dasharray: 4,3; }',
        '    .txt { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #1e293b; font-weight: 600; }',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; fill: #0f172a; font-weight: bold; }',
        '  </style>',
        # Axes
        f'  <line x1="{ox}" y1="20" x2="{ox}" y2="{h - 25}" class="axis" />',
        f'  <line x1="{ox - 10}" y1="{oy}" x2="{ox + plot_width + 20}" y2="{oy}" class="axis" />',
        # Labels on axes
        f'  <text x="{ox + plot_width + 10}" y="{oy + 18}" class="lbl">{x_axis_label}</text>',
        f'  <text x="{ox - 45}" y="25" class="lbl">{y_axis_label}</text>',
        # Horizontal amplitude guides
        f'  <line x1="{ox}" y1="{oy - amp*scale_y:.1f}" x2="{ox + plot_width}" y2="{oy - amp*scale_y:.1f}" class="grid" />',
        f'  <line x1="{ox}" y1="{oy + amp*scale_y:.1f}" x2="{ox + plot_width}" y2="{oy + amp*scale_y:.1f}" class="grid" />',
        f'  <text x="{ox - 30}" y="{oy - amp*scale_y + 4:.1f}" class="txt">+{_fmt_sa(amp)}</text>',
        f'  <text x="{ox - 30}" y="{oy + amp*scale_y + 4:.1f}" class="txt">-{_fmt_sa(amp)}</text>',
        f'  <text x="{ox - 15}" y="{oy + 14}" class="txt">0</text>',
        # Wavelength markers
        f'  <text x="{ox + dx_per_wave:.1f}" y="{oy + 16}" class="txt" text-anchor="middle">{_fmt_sa(wavelength)}</text>',
        f'  <text x="{ox + 2*dx_per_wave:.1f}" y="{oy + 16}" class="txt" text-anchor="middle">{_fmt_sa(2*wavelength)}</text>',
        # Wave path
        f'  <polyline points="{" ".join(pts)}" class="wave" />',
        # Crest marker
        f'  <circle cx="{ox + dx_per_wave*0.25:.1f}" cy="{oy - amp*scale_y:.1f}" r="4" fill="#dc2626" />',
        f'  <text x="{ox + dx_per_wave*0.25:.1f}" y="{oy - amp*scale_y - 8:.1f}" class="txt" fill="#dc2626" text-anchor="middle">Crest</text>',
        # Trough marker
        f'  <circle cx="{ox + dx_per_wave*0.75:.1f}" cy="{oy + amp*scale_y:.1f}" r="4" fill="#dc2626" />',
        f'  <text x="{ox + dx_per_wave*0.75:.1f}" y="{oy + amp*scale_y + 18:.1f}" class="txt" fill="#dc2626" text-anchor="middle">Trough</text>',
        '</svg>',
    ]
    return "\n".join(svg)


# =========================================================================== #
# Archetypes 01 to 25
# =========================================================================== #

def _build_01(rng: random.Random) -> Dict[str, Any]:
    sub = "01_transverse_pulse_definition_and_medium"
    medium = rng.choice(["a stretched nylon rope", "a horizontal slinky spring", "a taut elastic cord", "a long rubber tube"])
    prompt = (
        f"A learner flicks {medium} once vertically to create a single disturbance.\n"
        "Which of the following statements correctly defines a **transverse pulse** and the role of the medium?\n\n"
        "A. A single disturbance where particles of the medium vibrate perpendicular to the direction of pulse motion.\n"
        "B. A continuous succession of waves where particles vibrate parallel to the direction of motion.\n"
        "C. The physical transport of matter from one location to another across empty space.\n"
        "D. A single disturbance where particles move permanently along the direction of wave travel."
    )
    ans = "A. A single disturbance where particles of the medium vibrate perpendicular to the direction of pulse motion."
    opts = [
        ans,
        "B. A continuous succession of waves where particles vibrate parallel to the direction of motion.",
        "C. The physical transport of matter from one location to another across empty space.",
        "D. A single disturbance where particles move permanently along the direction of wave travel.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Recall definition of pulse", "op": "\\text{Pulse = single disturbance}", "to": "\\text{Single disturbance}"},
        {"rule": "Define transverse direction", "op": "\\text{Particle motion } \\perp \\text{ pulse motion}", "to": "\\text{Perpendicular vibration}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A pulse is a single disturbance in a medium.",
        t2="In a transverse pulse, particles move perpendicular to the direction in which the pulse travels.",
        t3="Option A correctly states both the single disturbance nature and the perpendicular vibration.",
        misconceptions=["confusing_pulse_with_periodic_wave", "confusing_transverse_with_longitudinal"],
        marks=2,
    )


def _build_02(rng: random.Random) -> Dict[str, Any]:
    sub = "02_pulse_amplitude_and_pulse_length_identification"
    amp = rng.choice([2.5, 3.0, 3.5, 4.0, 5.0])
    length = rng.choice([8.0, 10.0, 12.0, 14.0, 16.0])

    svg = _svg_pulse(amp, length, rng.randint(100, 999), show_labels=True)
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "alt_text": "Transverse pulse on a string"}

    prompt = (
        f"Refer to the accompanying diagram showing a single transverse pulse moving along a stretched cord.\n"
        f"Determine the **amplitude** ($A$) and the **pulse length** of this disturbance."
    )
    ans = f"$A = {_fmt_sa(amp)}\\text{{ cm}},\\; \\text{{Pulse length}} = {_fmt_sa(length)}\\text{{ cm}}$"
    d1 = f"$A = {_fmt_sa(amp * 2)}\\text{{ cm}},\\; \\text{{Pulse length}} = {_fmt_sa(length)}\\text{{ cm}}$"
    d2 = f"$A = {_fmt_sa(amp)}\\text{{ cm}},\\; \\text{{Pulse length}} = {_fmt_sa(length / 2)}\\text{{ cm}}$"
    d3 = f"$A = {_fmt_sa(length)}\\text{{ cm}},\\; \\text{{Pulse length}} = {_fmt_sa(amp)}\\text{{ cm}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Identify amplitude A", "op": f"A = \\text{{maximum displacement from rest}}", "to": f"{_fmt_sa(amp)}\\text{{ cm}}"},
        {"rule": "Identify pulse length", "op": f"L = \\text{{horizontal extent of pulse}}", "to": f"{_fmt_sa(length)}\\text{{ cm}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Amplitude is the maximum displacement of a particle from its position of rest.",
        t2="Pulse length is the distance from the leading edge to the trailing edge of the disturbance.",
        t3=f"A = {_fmt_sa(amp)} cm and length = {_fmt_sa(length)} cm.",
        misconceptions=["doubling_amplitude_from_peak_to_trough", "swapping_amplitude_and_pulse_length"],
        marks=2,
        diagram_spec=diag,
    )


def _build_03(rng: random.Random) -> Dict[str, Any]:
    sub = "03_pulse_speed_calculation"
    d = rng.choice([4.0, 6.0, 8.0, 10.0, 12.0, 15.0])
    t = rng.choice([0.5, 0.8, 1.2, 1.5, 2.0, 2.5])
    v = round(d / t, 2)

    prompt = (
        f"A transverse pulse generated at one end of a heavy spring travels a distance of "
        f"$\\Delta x = {_fmt_sa(d)}\\text{{ m}}$ in a time interval of $\\Delta t = {_fmt_sa(t)}\\text{{ s}}$.\n"
        f"Calculate the speed ($v$) of the pulse along the spring."
    )
    ans = f"$v = {_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d1 = f"$v = {_fmt_sa(round(d * t, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d2 = f"$v = {_fmt_sa(round(t / d, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d3 = f"$v = {_fmt_sa(round(v * 2, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "State pulse speed formula", "op": "v = \\frac{\\Delta x}{\\Delta t}", "to": f"v = \\frac{{{_fmt_sa(d)}}}{{{_fmt_sa(t)}}}"},
        {"rule": "Compute numerical speed", "op": f"\\frac{{{_fmt_sa(d)}}}{{{_fmt_sa(t)}}}", "to": f"{_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Speed is defined as distance traveled per unit time: v = Delta x / Delta t.",
        t2=f"Substitute distance {_fmt_sa(d)} m and time {_fmt_sa(t)} s into v = d/t.",
        t3=f"v = {_fmt_sa(d)} / {_fmt_sa(t)} = {_fmt_sa(v)} m/s.",
        misconceptions=["multiplying_distance_by_time", "inverting_time_and_distance"],
        marks=3,
    )


def _build_04(rng: random.Random) -> Dict[str, Any]:
    sub = "04_pulse_travel_time_and_distance"
    v = rng.choice([2.5, 4.0, 5.0, 6.0, 8.0])
    L = rng.choice([15.0, 20.0, 24.0, 30.0, 40.0])
    t = round(L / v, 2)

    prompt = (
        f"A transverse pulse travels with a constant speed of $v = {_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"along a horizontal wire of length $L = {_fmt_sa(L)}\\text{{ m}}$.\n"
        f"Calculate the time taken ($\\Delta t$) for the pulse to travel from one end of the wire to the other."
    )
    ans = f"$\\Delta t = {_fmt_sa(t)}\\text{{ s}}$"
    d1 = f"$\\Delta t = {_fmt_sa(round(L * v, 2))}\\text{{ s}}$"
    d2 = f"$\\Delta t = {_fmt_sa(round(v / L, 3))}\\text{{ s}}$"
    d3 = f"$\\Delta t = {_fmt_sa(round(t / 2, 2))}\\text{{ s}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Rearrange speed formula for time", "op": "\\Delta t = \\frac{\\Delta x}{v}", "to": f"\\Delta t = \\frac{{{_fmt_sa(L)}}}{{{_fmt_sa(v)}}}"},
        {"rule": "Evaluate travel time", "op": f"\\frac{{{_fmt_sa(L)}}}{{{_fmt_sa(v)}}}", "to": f"{_fmt_sa(t)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Time is distance divided by speed: Delta t = Delta x / v.",
        t2=f"Divide the length {_fmt_sa(L)} m by the speed {_fmt_sa(v)} m/s.",
        t3=f"Delta t = {_fmt_sa(L)} / {_fmt_sa(v)} = {_fmt_sa(t)} s.",
        misconceptions=["multiplying_speed_by_distance", "inverting_fraction"],
        marks=3,
    )


def _build_05(rng: random.Random) -> Dict[str, Any]:
    sub = "05_particle_motion_during_pulse_passage"
    direction = rng.choice(["right", "left"])
    particle = rng.choice(["P", "Q", "R"])
    
    prompt = (
        f"A single transverse crest travels to the **{direction}** along a horizontal rope. "
        f"Consider a point {particle} on the rope that is currently at its resting equilibrium position.\n"
        f"As the crest passes point {particle}, what is the exact motion of particle {particle}?\n\n"
        "A. Particle moves upwards to maximum displacement, then downwards back to equilibrium.\n"
        f"B. Particle moves horizontally to the {direction} with the speed of the pulse.\n"
        "C. Particle moves downwards into a trough, then upwards to the crest.\n"
        "D. Particle remains stationary while only energy moves."
    )
    ans = "A. Particle moves upwards to maximum displacement, then downwards back to equilibrium."
    opts = [
        ans,
        f"B. Particle moves horizontally to the {direction} with the speed of the pulse.",
        "C. Particle moves downwards into a trough, then upwards to the crest.",
        "D. Particle remains stationary while only energy moves.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Understand particle motion in transverse pulse", "op": "\\text{Particles vibrate } \\perp \\text{ to wave travel}", "to": "\\text{Vertical oscillation only}"},
        {"rule": "Trace passage of a crest", "op": "\\text{Rest } \\to \\text{ Upward peak } \\to \\text{ Rest}", "to": "\\text{Upwards then downwards}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="In a transverse pulse, particles vibrate perpendicular to the direction of propagation.",
        t2="Particles do NOT travel along with the pulse; they oscillate vertically and return to equilibrium.",
        t3="For a crest, the particle first rises to the peak displacement and then returns down to rest.",
        misconceptions=["believing_particles_travel_horizontally_with_pulse", "confusing_crest_with_trough_sequence"],
        marks=2,
    )


def _build_06(rng: random.Random) -> Dict[str, Any]:
    sub = "06_superposition_principle_definition"
    medium = rng.choice(["a stretched rope", "a water ripple tank", "a long coiled spring", "an elastic string"])
    prompt = (
        f"Two pulses travel towards each other in {medium} and overlap.\n"
        "State the **Principle of Superposition** for waves and pulses:\n\n"
        "A. When two pulses meet, the resultant displacement is the algebraic sum of the displacements of the individual pulses.\n"
        "B. When two pulses meet, they reflect off each other and reverse their velocities.\n"
        "C. The speed of a pulse is equal to the product of its frequency and wavelength.\n"
        "D. Two pulses in the same medium always annihilate each other permanently."
    )
    ans = "A. When two pulses meet, the resultant displacement is the algebraic sum of the displacements of the individual pulses."
    opts = [
        ans,
        "B. When two pulses meet, they reflect off each other and reverse their velocities.",
        "C. The speed of a pulse is equal to the product of its frequency and wavelength.",
        "D. Two pulses in the same medium always annihilate each other permanently.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "State definition of principle of superposition", "op": "\\text{Resultant displacement} = \\sum \\text{individual displacements}", "to": "\\text{Algebraic sum of displacements}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The principle of superposition deals with what happens when two pulses occupy the same medium simultaneously.",
        t2="Displacements are vectors (or signed scalars): they add algebraically taking signs into account.",
        t3="Option A provides the exact standard definition.",
        misconceptions=["thinking_pulses_bounce_off_each_other", "confusing_superposition_with_reflection"],
        marks=2,
    )


def _build_07(rng: random.Random) -> Dict[str, Any]:
    sub = "07_constructive_interference_two_crests"
    a1 = rng.choice([2.0, 3.0, 3.5, 4.0])
    a2 = rng.choice([1.5, 2.5, 3.0, 4.5])
    a_res = round(a1 + a2, 1)

    svg = _svg_two_pulses(a1, a2, side1="crest", side2="crest")
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "alt_text": "Two crest pulses approaching"}

    prompt = (
        f"Refer to the accompanying diagram showing two transverse pulses moving towards each other on the same side of a string. "
        f"Pulse 1 has amplitude $A_1 = +{_fmt_sa(a1)}\\text{{ cm}}$ and Pulse 2 has amplitude $A_2 = +{_fmt_sa(a2)}\\text{{ cm}}$.\n"
        f"Name the type of interference that occurs when they overlap, and calculate the maximum resultant amplitude ($A_{{res}}$)."
    )
    ans = f"Constructive interference; $A_{{res}} = +{_fmt_sa(a_res)}\\text{{ cm}}$"
    d1 = f"Destructive interference; $A_{{res}} = +{_fmt_sa(abs(a1 - a2))}\\text{{ cm}}$"
    d2 = f"Constructive interference; $A_{{res}} = +{_fmt_sa(max(a1, a2))}\\text{{ cm}}$"
    d3 = f"Destructive interference; $A_{{res}} = 0\\text{{ cm}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Identify type of interference", "op": "\\text{Both pulses on same side} \\implies \\text{Constructive interference}", "to": "\\text{Constructive}"},
        {"rule": "Calculate resultant amplitude", "op": f"A_{{res}} = A_1 + A_2 = {_fmt_sa(a1)} + {_fmt_sa(a2)}", "to": f"+{_fmt_sa(a_res)}\\text{{ cm}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="When two crests meet on the same side of the resting position, constructive interference occurs.",
        t2=f"The amplitudes add together: A_res = A_1 + A_2 = {_fmt_sa(a1)} + {_fmt_sa(a2)}.",
        t3=f"A_res = +{_fmt_sa(a_res)} cm.",
        misconceptions=["subtracting_amplitudes_for_same_side_pulses", "assuming_amplitude_equals_the_larger_pulse"],
        marks=3,
        diagram_spec=diag,
    )


def _build_08(rng: random.Random) -> Dict[str, Any]:
    sub = "08_destructive_interference_crest_and_trough"
    a1 = rng.choice([4.0, 5.0, 6.0, 7.0])
    a2 = rng.choice([1.5, 2.0, 2.5, 3.0])
    a_res = round(a1 - a2, 1)

    svg = _svg_two_pulses(a1, a2, side1="crest", side2="trough")
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "alt_text": "Crest and trough pulses approaching"}

    prompt = (
        f"Refer to the accompanying diagram showing two transverse pulses on opposite sides of a string moving towards each other. "
        f"Pulse 1 is a crest of amplitude $A_1 = +{_fmt_sa(a1)}\\text{{ cm}}$ and Pulse 2 is a trough of amplitude $A_2 = -{_fmt_sa(a2)}\\text{{ cm}}$.\n"
        f"Name the type of interference that occurs at the point of overlap, and calculate the resultant displacement ($A_{{res}}$)."
    )
    ans = f"Destructive interference; $A_{{res}} = +{_fmt_sa(a_res)}\\text{{ cm}}$"
    d1 = f"Constructive interference; $A_{{res}} = +{_fmt_sa(round(a1 + a2, 1))}\\text{{ cm}}$"
    d2 = f"Destructive interference; $A_{{res}} = -{_fmt_sa(a_res)}\\text{{ cm}}$"
    d3 = f"Destructive interference; $A_{{res}} = 0\\text{{ cm}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Identify type of interference", "op": "\\text{Pulses on opposite sides} \\implies \\text{Destructive interference}", "to": "\\text{Destructive}"},
        {"rule": "Apply algebraic sum of displacements", "op": f"A_{{res}} = A_1 + A_2 = (+{_fmt_sa(a1)}) + (-{_fmt_sa(a2)})", "to": f"+{_fmt_sa(a_res)}\\text{{ cm}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="When a crest and a trough meet, destructive interference occurs.",
        t2=f"Add displacements algebraically: A_res = (+{_fmt_sa(a1)}) + (-{_fmt_sa(a2)}) = +{_fmt_sa(a_res)} cm.",
        t3=f"Resultant displacement is +{_fmt_sa(a_res)} cm (a smaller crest).",
        misconceptions=["adding_magnitudes_instead_of_algebraic_sum", "assuming_complete_cancellation_when_amplitudes_differ"],
        marks=3,
        diagram_spec=diag,
    )


def _build_09(rng: random.Random) -> Dict[str, Any]:
    sub = "09_total_destructive_interference_equal_pulses"
    amp = rng.choice([3.0, 4.0, 5.0, 6.0])

    svg = _svg_two_pulses(amp, amp, side1="crest", side2="trough")
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "alt_text": "Equal and opposite pulses"}

    prompt = (
        f"Refer to the accompanying diagram. Two pulses of equal magnitude but opposite displacement "
        f"($A_1 = +{_fmt_sa(amp)}\\text{{ cm}}$ and $A_2 = -{_fmt_sa(amp)}\\text{{ cm}}$) travel towards each other on a string.\n"
        f"What is the resultant displacement of the string at the exact instant they completely overlap?"
    )
    ans = "$0\\text{ cm}$ (Complete destructive cancellation)"
    d1 = f"$+{_fmt_sa(round(amp * 2, 1))}\\text{{ cm}}$"
    d2 = f"$+{_fmt_sa(amp)}\\text{{ cm}}$"
    d3 = f"$-{_fmt_sa(amp)}\\text{{ cm}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Apply superposition principle", "op": f"A_{{res}} = (+{_fmt_sa(amp)}) + (-{_fmt_sa(amp)})", "to": "0\\text{ cm}"},
        {"rule": "State physical effect", "op": "\\text{Complete destructive interference}", "to": "\\text{String is momentarily flat}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="When two identical pulses on opposite sides overlap completely, they cancel each other out.",
        t2=f"A_res = (+{_fmt_sa(amp)}) + (-{_fmt_sa(amp)}) = 0 cm.",
        t3="The string is momentarily completely straight and undisturbed.",
        misconceptions=["believing_pulses_reflect_back", "adding_absolute_values"],
        marks=2,
        diagram_spec=diag,
    )


def _build_10(rng: random.Random) -> Dict[str, Any]:
    sub = "10_superposition_post_interference_propagation"
    a_val = rng.choice([3, 4, 5, 6])
    prompt = (
        f"Two pulses (Pulse A of amplitude ${a_val}\\text{{ cm}}$ and Pulse B) interfere destructively in a rope. "
        "What happens to the two pulses **after** they have passed through each other?\n\n"
        "A. Both pulses continue moving in their original directions with their original shapes, amplitudes, and speeds unaltered.\n"
        "B. Both pulses are permanently destroyed and no further wave motion occurs.\n"
        "C. The pulses bounce off each other and travel backwards with reduced amplitudes.\n"
        "D. They combine permanently into a single stationary standing wave."
    )
    ans = "A. Both pulses continue moving in their original directions with their original shapes, amplitudes, and speeds unaltered."
    opts = [
        ans,
        "B. Both pulses are permanently destroyed and no further wave motion occurs.",
        "C. The pulses bounce off each other and travel backwards with reduced amplitudes.",
        "D. They combine permanently into a single stationary standing wave.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Understand independence of wave propagation", "op": "\\text{Superposition is temporary}", "to": "\\text{Pulses pass through unchanged}"},
        {"rule": "Determine post-overlap state", "op": "\\text{Retain original speed, shape, direction}", "to": "\\text{Unaltered propagation}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Superposition only occurs during the period of overlap.",
        t2="Once the pulses pass past each other, they continue along their original path as if the collision never occurred.",
        t3="Option A correctly describes this fundamental wave behavior.",
        misconceptions=["thinking_interference_causes_permanent_destruction", "believing_pulses_bounce_like_billiard_balls"],
        marks=2,
    )


def _build_11(rng: random.Random) -> Dict[str, Any]:
    sub = "11_transverse_wave_definition_and_direction"
    ex_medium = rng.choice(["a vibrating guitar string", "water ripples on a pond", "a shaken skipping rope", "an oscillating slinky"])
    prompt = (
        f"A periodic wave is generated along {ex_medium}.\n"
        "Which of the following is the correct definition of a **transverse wave**?\n\n"
        "A. A wave in which the particles of the medium vibrate perpendicular to the direction of propagation of the wave.\n"
        "B. A wave in which particles vibrate parallel to the direction of wave travel.\n"
        "C. A wave consisting exclusively of compressions and rarefactions in a gas.\n"
        "D. A disturbance that transfers matter rather than energy across space."
    )
    ans = "A. A wave in which the particles of the medium vibrate perpendicular to the direction of propagation of the wave."
    opts = [
        ans,
        "B. A wave in which particles vibrate parallel to the direction of wave travel.",
        "C. A wave consisting exclusively of compressions and rarefactions in a gas.",
        "D. A disturbance that transfers matter rather than energy across space.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Define transverse wave", "op": "\\text{Particle motion } \\perp \\text{ wave direction}", "to": "\\text{Perpendicular vibration}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Transverse means 'at right angles to' or 'perpendicular'.",
        t2="Particles oscillate at 90 degrees to the direction in which wave energy propagates.",
        t3="Option A is the correct definition.",
        misconceptions=["confusing_transverse_with_longitudinal_definition", "believing_waves_transfer_matter"],
        marks=2,
    )


def _build_12(rng: random.Random) -> Dict[str, Any]:
    sub = "12_crest_trough_and_amplitude_from_wave_graph"
    amp = rng.choice([2.0, 3.0, 4.0, 5.0, 6.0])
    wlen = rng.choice([2.0, 4.0, 5.0, 6.0])

    svg = _svg_transverse_wave(amp, wlen, cycles=2.0)
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "alt_text": "Transverse wave graph"}

    prompt = (
        f"Refer to the accompanying diagram representing a transverse wave.\n"
        f"1. Identify the maximum displacement above the equilibrium line (crest displacement).\n"
        f"2. Determine the **amplitude** ($A$) of the wave."
    )
    ans = f"Crest displacement = $+{_fmt_sa(amp)}\\text{{ cm}},\\; \\text{{Amplitude }} A = {_fmt_sa(amp)}\\text{{ cm}}$"
    d1 = f"Crest displacement = $+{_fmt_sa(amp * 2)}\\text{{ cm}},\\; \\text{{Amplitude }} A = {_fmt_sa(amp * 2)}\\text{{ cm}}$"
    d2 = f"Crest displacement = $+{_fmt_sa(amp)}\\text{{ cm}},\\; \\text{{Amplitude }} A = {_fmt_sa(amp * 2)}\\text{{ cm}}$"
    d3 = f"Crest displacement = $+{_fmt_sa(wlen)}\\text{{ cm}},\\; \\text{{Amplitude }} A = {_fmt_sa(wlen)}\\text{{ cm}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Read crest displacement from graph", "op": f"y_{{crest}} = +{_fmt_sa(amp)}\\text{{ cm}}", "to": f"+{_fmt_sa(amp)}\\text{{ cm}}"},
        {"rule": "Define amplitude", "op": f"A = |y_{{crest}}| = {_fmt_sa(amp)}\\text{{ cm}}", "to": f"{_fmt_sa(amp)}\\text{{ cm}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="A crest is the highest point of a wave above the resting baseline.",
        t2="Amplitude is the distance from the resting position to a crest (or to a trough), NOT from crest to trough.",
        t3=f"The amplitude is {_fmt_sa(amp)} cm.",
        misconceptions=["measuring_amplitude_from_crest_to_trough", "confusing_amplitude_with_wavelength"],
        marks=2,
        diagram_spec=diag,
    )


def _build_13(rng: random.Random) -> Dict[str, Any]:
    sub = "13_wavelength_definition_and_measurement"
    amp = rng.choice([2.0, 3.0, 4.0])
    wlen = rng.choice([2.5, 4.0, 5.0, 6.0, 8.0])

    svg = _svg_transverse_wave(amp, wlen, cycles=2.0, x_axis_label="Distance x (m)")
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "alt_text": "Displacement vs distance wave"}

    prompt = (
        f"Refer to the accompanying diagram of a snapshot of a wave.\n"
        f"1. Define **wavelength** ($\\lambda$).\n"
        f"2. Read the value of the wavelength from the graph."
    )
    ans = f"Distance between two consecutive points in phase; $\\lambda = {_fmt_sa(wlen)}\\text{{ m}}$"
    d1 = f"Distance between two consecutive points in phase; $\\lambda = {_fmt_sa(wlen * 2)}\\text{{ m}}$"
    d2 = f"Distance from crest to trough; $\\lambda = {_fmt_sa(wlen / 2)}\\text{{ m}}$"
    d3 = f"Height of a wave crest; $\\lambda = {_fmt_sa(amp)}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Define wavelength", "op": "\\text{Wavelength = distance between consecutive in-phase points}", "to": "\\text{Distance between consecutive crests}"},
        {"rule": "Read wavelength from scale", "op": f"\\lambda = {_fmt_sa(wlen)}\\text{{ m}}", "to": f"{_fmt_sa(wlen)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Wavelength is the distance between two consecutive points in phase.",
        t2="On a displacement-position graph, one full wave cycle corresponds to one wavelength.",
        t3=f"The wavelength is lambda = {_fmt_sa(wlen)} m.",
        misconceptions=["reading_half_wavelength_crest_to_trough", "confusing_position_axis_with_time_axis"],
        marks=3,
        diagram_spec=diag,
    )


def _build_14(rng: random.Random) -> Dict[str, Any]:
    sub = "14_points_in_phase_identification"
    pts_pair = rng.choice([("P and Q", "two consecutive crests"), ("A and E", "two consecutive troughs"), ("X and Y", "separated by 1 wavelength"), ("M and N", "separated by 2 wavelengths")])
    prompt = (
        f"Consider two points {pts_pair[0]} ({pts_pair[1]}) on a periodic transverse wave. "
        "Two points on a periodic transverse wave are said to be **in phase** when they:\n\n"
        "A. Are moving in the same direction and have the same displacement from equilibrium at the same time.\n"
        "B. Are moving in opposite directions with the same displacement.\n"
        "C. Are separated by exactly half a wavelength ($0{,}5\\lambda$).\n"
        "D. Lie on opposite sides of the resting baseline."
    )
    ans = "A. Are moving in the same direction and have the same displacement from equilibrium at the same time."
    opts = [
        ans,
        "B. Are moving in opposite directions with the same displacement.",
        "C. Are separated by exactly half a wavelength ($0{,}5\\lambda$).",
        "D. Lie on opposite sides of the resting baseline.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "State condition for points in phase", "op": "\\text{Same displacement AND same direction of motion}", "to": "\\text{In phase condition}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Points in phase must have both the same displacement and be moving in the exact same direction.",
        t2="They are separated by whole-number multiples of the wavelength: lambda, 2*lambda, etc.",
        t3="Option A correctly gives both criteria.",
        misconceptions=["ignoring_direction_of_motion", "confusing_in_phase_with_opposite_phase"],
        marks=2,
    )


def _build_15(rng: random.Random) -> Dict[str, Any]:
    sub = "15_points_out_of_phase_opposite_phase"
    pts_pair = rng.choice([("a crest K and an adjacent trough L", "0,5"), ("point A and point B separated by 1,5 wavelengths", "1,5"), ("point R and point S separated by 2,5 wavelengths", "2,5")])
    prompt = (
        f"Consider {pts_pair[0]} on a transverse wave. "
        "Two points on a transverse wave are in **complete opposite phase** (out of phase by $180^\\circ$) if they:\n\n"
        "A. Have equal magnitude of displacement on opposite sides of rest and are moving in opposite directions (separated by an odd multiple of $0{,}5\\lambda$).\n"
        "B. Are separated by exactly one full wavelength ($1\\lambda$).\n"
        "C. Are both crests located on adjacent cycles.\n"
        "D. Both have zero displacement and are moving in the same direction."
    )
    ans = "A. Have equal magnitude of displacement on opposite sides of rest and are moving in opposite directions (separated by an odd multiple of $0{,}5\\lambda$)."
    opts = [
        ans,
        "B. Are separated by exactly one full wavelength ($1\\lambda$).",
        "C. Are both crests located on adjacent cycles.",
        "D. Both have zero displacement and are moving in the same direction.",
    ]
    rng.shuffle(opts)
    steps = [
        {"rule": "Define opposite phase", "op": "\\text{Separated by } (n + 0{,}5)\\lambda \\text{ with opposite directions}", "to": "\\text{Opposite phase}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Points in opposite phase are separated by an odd number of half wavelengths (lambda/2, 3*lambda/2).",
        t2="A crest and a trough on the same cycle are in opposite phase.",
        t3="Option A correctly specifies opposite displacement and direction.",
        misconceptions=["confusing_half_wavelength_with_full_wavelength", "thinking_opposite_phase_means_random_phase"],
        marks=2,
    )


def _build_16(rng: random.Random) -> Dict[str, Any]:
    sub = "16_wave_period_definition_and_calculation"
    num_waves = rng.choice([10, 15, 20, 25, 40, 50])
    total_time = rng.choice([2.0, 4.0, 5.0, 8.0, 10.0])
    T = round(total_time / num_waves, 3)

    prompt = (
        f"A wave generator in a ripple tank produces **{num_waves} complete waves** in a time of "
        f"$\\Delta t = {_fmt_sa(total_time)}\\text{{ s}}$.\n"
        f"Calculate the **period** ($T$) of the waves."
    )
    ans = f"$T = {_fmt_sa(T)}\\text{{ s}}$"
    d1 = f"$T = {_fmt_sa(round(num_waves / total_time, 2))}\\text{{ s}}$"
    d2 = f"$T = {_fmt_sa(round(num_waves * total_time, 1))}\\text{{ s}}$"
    d3 = f"$T = {_fmt_sa(round(T * 2, 3))}\\text{{ s}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "State period definition formula", "op": "T = \\frac{\\text{total time}}{\\text{number of waves}}", "to": f"T = \\frac{{{_fmt_sa(total_time)}}}{{{num_waves}}}"},
        {"rule": "Calculate period T", "op": f"\\frac{{{_fmt_sa(total_time)}}}{{{num_waves}}}", "to": f"{_fmt_sa(T)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Period is the time required for one complete wave to pass: T = time / number of waves.",
        t2=f"Divide the total time {_fmt_sa(total_time)} s by {num_waves} waves.",
        t3=f"T = {_fmt_sa(total_time)} / {num_waves} = {_fmt_sa(T)} s.",
        misconceptions=["inverting_period_to_get_frequency", "multiplying_waves_by_time"],
        marks=3,
    )


def _build_17(rng: random.Random) -> Dict[str, Any]:
    sub = "17_wave_frequency_definition_and_calculation"
    num_waves = rng.choice([30, 45, 60, 90, 120])
    total_time = rng.choice([2.0, 3.0, 4.0, 5.0, 6.0])
    f_val = round(num_waves / total_time, 2)

    prompt = (
        f"A surfer observes that **{num_waves} wave crests** pass a fixed marker buoy in a time of "
        f"$\\Delta t = {_fmt_sa(total_time)}\\text{{ s}}$.\n"
        f"Calculate the **frequency** ($f$) of the water waves in Hertz ($\\text{{Hz}}$)."
    )
    ans = f"$f = {_fmt_sa(f_val)}\\text{{ Hz}}$"
    d1 = f"$f = {_fmt_sa(round(total_time / num_waves, 3))}\\text{{ Hz}}$"
    d2 = f"$f = {_fmt_sa(round(num_waves * total_time, 1))}\\text{{ Hz}}$"
    d3 = f"$f = {_fmt_sa(round(f_val / 2, 2))}\\text{{ Hz}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "State frequency formula", "op": "f = \\frac{\\text{number of waves}}{\\Delta t}", "to": f"f = \\frac{{{num_waves}}}{{{_fmt_sa(total_time)}}}"},
        {"rule": "Calculate numerical frequency", "op": f"\\frac{{{num_waves}}}{{{_fmt_sa(total_time)}}}", "to": f"{_fmt_sa(f_val)}\\text{{ Hz}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Frequency is the number of complete waves passing a point per second: f = N / Delta t.",
        t2=f"Divide the number of waves ({num_waves}) by the time ({_fmt_sa(total_time)} s).",
        t3=f"f = {num_waves} / {_fmt_sa(total_time)} = {_fmt_sa(f_val)} Hz.",
        misconceptions=["dividing_time_by_waves_frequency_period_swap", "unit_confusion_using_seconds_for_frequency"],
        marks=3,
    )


def _build_18(rng: random.Random) -> Dict[str, Any]:
    sub = "18_frequency_and_period_reciprocal_relation"
    f_val = rng.choice([2.0, 4.0, 5.0, 8.0, 10.0, 20.0, 50.0])
    T = round(1.0 / f_val, 4)

    prompt = (
        f"A tuning fork vibrates with a frequency of $f = {_fmt_sa(f_val)}\\text{{ Hz}}$.\n"
        f"Calculate the **period** ($T$) of vibration of the tuning fork."
    )
    ans = f"$T = {_fmt_sa(T)}\\text{{ s}}$"
    d1 = f"$T = {_fmt_sa(f_val)}\\text{{ s}}$"
    d2 = f"$T = {_fmt_sa(round(f_val * 2, 1))}\\text{{ s}}$"
    d3 = f"$T = {_fmt_sa(round(T * 10, 3))}\\text{{ s}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "State period-frequency relation", "op": "T = \\frac{1}{f}", "to": f"T = \\frac{{1}}{{{_fmt_sa(f_val)}}}"},
        {"rule": "Evaluate period", "op": f"\\frac{{1}}{{{_fmt_sa(f_val)}}}", "to": f"{_fmt_sa(T)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Period and frequency are reciprocals of each other: T = 1/f.",
        t2=f"Divide 1 by the frequency {_fmt_sa(f_val)} Hz.",
        t3=f"T = 1 / {_fmt_sa(f_val)} = {_fmt_sa(T)} s.",
        misconceptions=["confusing_period_and_frequency_values", "forgetting_reciprocal_formula"],
        marks=2,
    )


def _build_19(rng: random.Random) -> Dict[str, Any]:
    sub = "19_wave_equation_speed_frequency_wavelength"
    f_val = rng.choice([4.0, 5.0, 6.0, 8.0, 10.0, 12.0])
    wlen = rng.choice([0.25, 0.4, 0.5, 0.75, 1.2, 1.5])
    v = round(f_val * wlen, 2)

    prompt = (
        f"A transverse wave has a frequency of $f = {_fmt_sa(f_val)}\\text{{ Hz}}$ and a wavelength of "
        f"$\\lambda = {_fmt_sa(wlen)}\\text{{ m}}$.\n"
        f"Calculate the speed ($v$) of the wave."
    )
    ans = f"$v = {_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d1 = f"$v = {_fmt_sa(round(f_val / wlen, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d2 = f"$v = {_fmt_sa(round(wlen / f_val, 3))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d3 = f"$v = {_fmt_sa(round(v * 2, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "State wave equation", "op": "v = f \\lambda", "to": f"v = ({_fmt_sa(f_val)})({_fmt_sa(wlen)})"},
        {"rule": "Calculate wave speed", "op": f"({_fmt_sa(f_val)})({_fmt_sa(wlen)})", "to": f"{_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="The wave equation relates speed, frequency, and wavelength: v = f * lambda.",
        t2=f"Multiply frequency ({_fmt_sa(f_val)} Hz) by wavelength ({_fmt_sa(wlen)} m).",
        t3=f"v = {_fmt_sa(f_val)} * {_fmt_sa(wlen)} = {_fmt_sa(v)} m/s.",
        misconceptions=["dividing_frequency_by_wavelength", "dividing_wavelength_by_frequency"],
        marks=3,
    )


def _build_20(rng: random.Random) -> Dict[str, Any]:
    sub = "20_wave_equation_finding_wavelength"
    v = rng.choice([12.0, 15.0, 18.0, 20.0, 24.0, 30.0])
    f_val = rng.choice([3.0, 4.0, 5.0, 6.0, 8.0])
    wlen = round(v / f_val, 2)

    prompt = (
        f"A radio transmitter generates waves that travel through air at a speed of "
        f"$v = {_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ with a frequency of $f = {_fmt_sa(f_val)}\\text{{ Hz}}$.\n"
        f"Calculate the wavelength ($\\lambda$) of these waves."
    )
    ans = f"$\\lambda = {_fmt_sa(wlen)}\\text{{ m}}$"
    d1 = f"$\\lambda = {_fmt_sa(round(v * f_val, 1))}\\text{{ m}}$"
    d2 = f"$\\lambda = {_fmt_sa(round(f_val / v, 3))}\\text{{ m}}$"
    d3 = f"$\\lambda = {_fmt_sa(round(wlen / 2, 2))}\\text{{ m}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Rearrange wave equation for wavelength", "op": "\\lambda = \\frac{v}{f}", "to": f"\\lambda = \\frac{{{_fmt_sa(v)}}}{{{_fmt_sa(f_val)}}}"},
        {"rule": "Calculate numerical wavelength", "op": f"\\frac{{{_fmt_sa(v)}}}{{{_fmt_sa(f_val)}}}", "to": f"{_fmt_sa(wlen)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Rearrange v = f * lambda to solve for wavelength: lambda = v / f.",
        t2=f"Divide wave speed ({_fmt_sa(v)} m/s) by frequency ({_fmt_sa(f_val)} Hz).",
        t3=f"lambda = {_fmt_sa(v)} / {_fmt_sa(f_val)} = {_fmt_sa(wlen)} m.",
        misconceptions=["multiplying_speed_by_frequency", "inverting_wave_equation"],
        marks=3,
    )


def _build_21(rng: random.Random) -> Dict[str, Any]:
    sub = "21_wave_equation_finding_frequency"
    v = rng.choice([20.0, 24.0, 30.0, 36.0, 48.0, 60.0])
    wlen = rng.choice([1.5, 2.0, 3.0, 4.0, 5.0, 6.0])
    f_val = round(v / wlen, 2)

    prompt = (
        f"Water waves travel across a lake with a speed of $v = {_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"The crests are separated by a distance of $\\lambda = {_fmt_sa(wlen)}\\text{{ m}}$.\n"
        f"Calculate the frequency ($f$) of the waves."
    )
    ans = f"$f = {_fmt_sa(f_val)}\\text{{ Hz}}$"
    d1 = f"$f = {_fmt_sa(round(v * wlen, 1))}\\text{{ Hz}}$"
    d2 = f"$f = {_fmt_sa(round(wlen / v, 3))}\\text{{ Hz}}$"
    d3 = f"$f = {_fmt_sa(round(f_val * 2, 2))}\\text{{ Hz}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Rearrange wave equation for frequency", "op": "f = \\frac{v}{\\lambda}", "to": f"f = \\frac{{{_fmt_sa(v)}}}{{{_fmt_sa(wlen)}}}"},
        {"rule": "Calculate numerical frequency", "op": f"\\frac{{{_fmt_sa(v)}}}{{{_fmt_sa(wlen)}}}", "to": f"{_fmt_sa(f_val)}\\text{{ Hz}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Rearrange v = f * lambda to solve for frequency: f = v / lambda.",
        t2=f"Divide speed ({_fmt_sa(v)} m/s) by wavelength ({_fmt_sa(wlen)} m).",
        t3=f"f = {_fmt_sa(v)} / {_fmt_sa(wlen)} = {_fmt_sa(f_val)} Hz.",
        misconceptions=["multiplying_speed_by_wavelength", "inverting_fraction"],
        marks=3,
    )


def _build_22(rng: random.Random) -> Dict[str, Any]:
    sub = "22_displacement_time_graph_interpretation"
    amp = rng.choice([2.0, 3.0, 4.0, 5.0])
    T = rng.choice([0.2, 0.4, 0.5, 0.8, 1.0])
    f_val = round(1.0 / T, 2)

    svg = _svg_transverse_wave(amp, T, cycles=2.0, x_axis_label="Time t (s)", unit_x="s")
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "alt_text": "Displacement-time wave graph"}

    prompt = (
        f"Refer to the accompanying diagram showing a displacement versus time graph for a particle in a medium.\n"
        f"1. Read the **period** ($T$) and **amplitude** ($A$) directly from the graph.\n"
        f"2. Calculate the **frequency** ($f$) of the wave."
    )
    ans = f"$T = {_fmt_sa(T)}\\text{{ s}},\\; A = {_fmt_sa(amp)}\\text{{ cm}},\\; f = {_fmt_sa(f_val)}\\text{{ Hz}}$"
    d1 = f"$T = {_fmt_sa(T * 2)}\\text{{ s}},\\; A = {_fmt_sa(amp)}\\text{{ cm}},\\; f = {_fmt_sa(round(1/(2*T), 2))}\\text{{ Hz}}$"
    d2 = f"$T = {_fmt_sa(T)}\\text{{ s}},\\; A = {_fmt_sa(amp * 2)}\\text{{ cm}},\\; f = {_fmt_sa(f_val)}\\text{{ Hz}}$"
    d3 = f"$T = {_fmt_sa(round(1/T, 2))}\\text{{ s}},\\; A = {_fmt_sa(amp)}\\text{{ cm}},\\; f = {_fmt_sa(T)}\\text{{ Hz}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Read period T from time axis", "op": f"T = {_fmt_sa(T)}\\text{{ s}}", "to": f"{_fmt_sa(T)}\\text{{ s}}"},
        {"rule": "Read amplitude A from y-axis", "op": f"A = {_fmt_sa(amp)}\\text{{ cm}}", "to": f"{_fmt_sa(amp)}\\text{{ cm}}"},
        {"rule": "Calculate frequency f = 1/T", "op": f"f = \\frac{{1}}{{{_fmt_sa(T)}}}", "to": f"{_fmt_sa(f_val)}\\text{{ Hz}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="On a displacement vs time graph, the horizontal length of one complete wave is the period T.",
        t2=f"Read T = {_fmt_sa(T)} s and A = {_fmt_sa(amp)} cm. Then calculate frequency f = 1/T.",
        t3=f"f = 1 / {_fmt_sa(T)} = {_fmt_sa(f_val)} Hz.",
        misconceptions=["reading_wavelength_from_time_axis", "swapping_period_and_frequency"],
        marks=4,
        diagram_spec=diag,
    )


def _build_23(rng: random.Random) -> Dict[str, Any]:
    sub = "23_displacement_position_graph_interpretation"
    amp = rng.choice([2.5, 3.5, 4.5, 6.0])
    wlen = rng.choice([1.2, 1.5, 2.0, 2.4, 3.0])

    svg = _svg_transverse_wave(amp, wlen, cycles=2.0, x_axis_label="Position x (m)", unit_x="m")
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "alt_text": "Displacement-position wave graph"}

    prompt = (
        f"Refer to the accompanying diagram showing a displacement versus position graph of a wave snapshot.\n"
        f"Determine the **wavelength** ($\\lambda$) and the **amplitude** ($A$) of the wave."
    )
    ans = f"$\\lambda = {_fmt_sa(wlen)}\\text{{ m}},\\; A = {_fmt_sa(amp)}\\text{{ cm}}$"
    d1 = f"$\\lambda = {_fmt_sa(round(wlen * 2, 2))}\\text{{ m}},\\; A = {_fmt_sa(amp)}\\text{{ cm}}$"
    d2 = f"$\\lambda = {_fmt_sa(wlen)}\\text{{ m}},\\; A = {_fmt_sa(round(amp * 2, 1))}\\text{{ cm}}$"
    d3 = f"$\\lambda = {_fmt_sa(round(wlen / 2, 2))}\\text{{ m}},\\; A = {_fmt_sa(amp)}\\text{{ cm}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Read wavelength from position axis", "op": f"\\lambda = {_fmt_sa(wlen)}\\text{{ m}}", "to": f"{_fmt_sa(wlen)}\\text{{ m}}"},
        {"rule": "Read amplitude from vertical axis", "op": f"A = {_fmt_sa(amp)}\\text{{ cm}}", "to": f"{_fmt_sa(amp)}\\text{{ cm}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="On a displacement-position graph, one full cycle represents the wavelength lambda.",
        t2=f"Read lambda = {_fmt_sa(wlen)} m directly from the horizontal axis for one full cycle.",
        t3=f"Wavelength = {_fmt_sa(wlen)} m and Amplitude = {_fmt_sa(amp)} cm.",
        misconceptions=["confusing_position_axis_with_time_axis", "measuring_half_wavelength"],
        marks=3,
        diagram_spec=diag,
    )


def _build_24(rng: random.Random) -> Dict[str, Any]:
    sub = "24_combined_wave_graph_speed_derivation"
    amp = rng.choice([3.0, 4.0, 5.0])
    wlen = rng.choice([1.5, 2.0, 2.5, 3.0])
    T = rng.choice([0.25, 0.5, 0.75, 1.0])
    v = round(wlen / T, 2)
    f_val = round(1.0 / T, 2)

    svg = _svg_transverse_wave(amp, wlen, cycles=2.0, x_axis_label="Position x (m)", unit_x="m")
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "alt_text": "Wave snapshot with known period"}

    prompt = (
        f"Refer to the accompanying diagram showing a snapshot of a wave with wavelength $\\lambda = {_fmt_sa(wlen)}\\text{{ m}}$. "
        f"A timing sensor at a fixed position indicates that each wave takes $T = {_fmt_sa(T)}\\text{{ s}}$ to pass.\n"
        f"Calculate the speed ($v$) of the wave."
    )
    ans = f"$v = {_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d1 = f"$v = {_fmt_sa(round(wlen * T, 3))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d2 = f"$v = {_fmt_sa(round(T / wlen, 3))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d3 = f"$v = {_fmt_sa(round(v * 2, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Use wave equation v = lambda / T", "op": f"v = \\frac{{\\lambda}}{{T}} = \\frac{{{_fmt_sa(wlen)}}}{{{_fmt_sa(T)}}}", "to": f"{_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Wave speed can be found using v = lambda / T or v = f * lambda where f = 1/T.",
        t2=f"Divide wavelength ({_fmt_sa(wlen)} m) by period ({_fmt_sa(T)} s).",
        t3=f"v = {_fmt_sa(wlen)} / {_fmt_sa(T)} = {_fmt_sa(v)} m/s.",
        misconceptions=["multiplying_wavelength_by_period", "inverting_formula"],
        marks=3,
        diagram_spec=diag,
    )


def _build_25(rng: random.Random) -> Dict[str, Any]:
    sub = "25_water_waves_in_ripple_tank_calculations"
    num_waves = rng.choice([12, 15, 20, 24])
    dist_cm = rng.choice([60.0, 75.0, 90.0, 120.0])
    wlen_cm = round(dist_cm / num_waves, 2)
    wlen_m = round(wlen_cm / 100.0, 4)
    t_sec = rng.choice([2.0, 3.0, 4.0, 5.0])
    f_val = round(num_waves / t_sec, 2)
    v = round(f_val * wlen_m, 3)

    prompt = (
        f"In a laboratory ripple tank investigation, a vibrating bar produces **{num_waves} complete waves** "
        f"spanning a total distance of ${dist_cm:.0f}\\text{{ cm}}$ in a time of $t = {_fmt_sa(t_sec)}\\text{{ s}}$.\n"
        f"1. Calculate the wavelength ($\\lambda$) in meters.\n"
        f"2. Calculate the frequency ($f$) in $\\text{{Hz}}$.\n"
        f"3. Calculate the wave speed ($v$) in $\\text{{m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    ans = f"$\\lambda = {_fmt_sa(wlen_m)}\\text{{ m}},\\; f = {_fmt_sa(f_val)}\\text{{ Hz}},\\; v = {_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d1 = f"$\\lambda = {_fmt_sa(wlen_cm)}\\text{{ m}},\\; f = {_fmt_sa(f_val)}\\text{{ Hz}},\\; v = {_fmt_sa(round(f_val * wlen_cm, 2))}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d2 = f"$\\lambda = {_fmt_sa(wlen_m)}\\text{{ m}},\\; f = {_fmt_sa(round(t_sec / num_waves, 3))}\\text{{ Hz}},\\; v = {_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    d3 = f"$\\lambda = {_fmt_sa(wlen_m * 2)}\\text{{ m}},\\; f = {_fmt_sa(f_val)}\\text{{ Hz}},\\; v = {_fmt_sa(v * 2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    opts = [ans, d1, d2, d3]
    rng.shuffle(opts)

    steps = [
        {"rule": "Calculate wavelength in meters", "op": f"\\lambda = \\frac{{{dist_cm}\\text{{ cm}}}}{{{num_waves}}} = {_fmt_sa(wlen_cm)}\\text{{ cm}} = {_fmt_sa(wlen_m)}\\text{{ m}}", "to": f"{_fmt_sa(wlen_m)}\\text{{ m}}"},
        {"rule": "Calculate frequency f", "op": f"f = \\frac{{{num_waves}}}{{{_fmt_sa(t_sec)}}}", "to": f"{_fmt_sa(f_val)}\\text{{ Hz}}"},
        {"rule": "Calculate wave speed v = f * lambda", "op": f"v = ({_fmt_sa(f_val)})({_fmt_sa(wlen_m)})", "to": f"{_fmt_sa(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=opts,
        sol_steps=steps,
        t1="Wavelength = total distance / number of waves. Frequency = number of waves / time.",
        t2="Remember to convert distance from cm to meters before calculating speed v = f * lambda.",
        t3=f"lambda = {_fmt_sa(wlen_m)} m, f = {_fmt_sa(f_val)} Hz, v = {_fmt_sa(v)} m/s.",
        misconceptions=["forgetting_to_convert_cm_to_meters", "inverting_frequency_formula"],
        marks=4,
    )


# Export dictionary of builders 01 to 25
BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_transverse_pulse_definition_and_medium": _build_01,
    "02_pulse_amplitude_and_pulse_length_identification": _build_02,
    "03_pulse_speed_calculation": _build_03,
    "04_pulse_travel_time_and_distance": _build_04,
    "05_particle_motion_during_pulse_passage": _build_05,
    "06_superposition_principle_definition": _build_06,
    "07_constructive_interference_two_crests": _build_07,
    "08_destructive_interference_crest_and_trough": _build_08,
    "09_total_destructive_interference_equal_pulses": _build_09,
    "10_superposition_post_interference_propagation": _build_10,
    "11_transverse_wave_definition_and_direction": _build_11,
    "12_crest_trough_and_amplitude_from_wave_graph": _build_12,
    "13_wavelength_definition_and_measurement": _build_13,
    "14_points_in_phase_identification": _build_14,
    "15_points_out_of_phase_opposite_phase": _build_15,
    "16_wave_period_definition_and_calculation": _build_16,
    "17_wave_frequency_definition_and_calculation": _build_17,
    "18_frequency_and_period_reciprocal_relation": _build_18,
    "19_wave_equation_speed_frequency_wavelength": _build_19,
    "20_wave_equation_finding_wavelength": _build_20,
    "21_wave_equation_finding_frequency": _build_21,
    "22_displacement_time_graph_interpretation": _build_22,
    "23_displacement_position_graph_interpretation": _build_23,
    "24_combined_wave_graph_speed_derivation": _build_24,
    "25_water_waves_in_ripple_tank_calculations": _build_25,
}

SUBSKILLS_01_25: List[str] = list(BUILDERS_01_25.keys())
