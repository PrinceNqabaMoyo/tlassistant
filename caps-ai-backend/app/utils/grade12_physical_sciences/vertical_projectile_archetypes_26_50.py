"""
vertical_projectile_archetypes_26_50.py
---------------------------------------
Grade 12 Physical Sciences — Vertical Projectile Motion in 1D & Skills for Science (Subskills 26-50).
Subskills covered:
  26. 26_bouncing_ball_rebound_velocity_and_speed_loss
  27. 27_bouncing_ball_second_bounce_apex_height
  28. 28_bouncing_ball_contact_time_average_net_force
  29. 29_hot_air_balloon_ascending_dropped_object
  30. 30_hot_air_balloon_descending_dropped_object
  31. 31_hot_air_balloon_projected_upwards_relative_to_balloon
  32. 32_simultaneous_release_one_dropped_one_projected_up
  33. 33_simultaneous_release_two_projected_opposite_directions
  34. 34_delayed_release_catchup_problem
  35. 35_velocity_time_graph_upward_projection_from_ground
  36. 36_velocity_time_graph_cliff_launch_to_ground
  37. 37_velocity_time_graph_bouncing_ball_single_bounce
  38. 38_velocity_time_graph_bouncing_ball_multiple_bounces
  39. 39_position_time_graph_upward_projection_parabola
  40. 40_position_time_graph_cliff_launch_crossing_zero
  41. 41_position_time_graph_bouncing_ball_parabolic_arcs
  42. 42_acceleration_time_graph_projectile_free_fall
  43. 43_acceleration_time_graph_bouncing_ball_impact_spike
  44. 44_graph_conversion_position_time_to_velocity_time
  45. 45_graph_conversion_velocity_time_to_position_time
  46. 46_experimental_data_ticker_timer_free_fall
  47. 47_experimental_data_photogate_dual_flag_timing
  48. 48_skills_for_science_percentage_error_and_uncertainty
  49. 49_skills_for_science_independent_dependent_controlled_variables
  50. 50_vertical_projectile_diagnostic_synthesis

All generators are 100% deterministic (random.Random(seed)), zero-LLM,
adhering strictly to South African comma decimal convention and 6-pillar contract.
"""

from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional

TERM = 1
CAPS_WEIGHT = 20
SUGGESTED_DURATION = 5
TOPIC_ID = "grade12_vertical_projectile"
LEARNING_OBJECTIVE = "PS12.VPM"
G = 9.8


def _fmt_sa(val: float, decimals: int = 2) -> str:
    """Format float with South African comma decimal notation for LaTeX."""
    if abs(val - round(val)) < 1e-9:
        return str(int(round(val)))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
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
    """Enforce universal 6-pillar generator contract."""
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
# Vector SVG Graph Builders
# =========================================================================== #

def _svg_vt_graph(v0: float, t_apex: float, t_total: float, vf: float) -> str:
    """Generate responsive velocity-time vector graph."""
    w, h = 500, 240
    ox, oy = 70, 130
    plot_w, plot_h = 390, 95

    t_scale = plot_w / max(t_total, 0.1)
    v_max = max(abs(v0), abs(vf), 1.0)
    v_scale = plot_h / v_max

    x_apex = ox + t_apex * t_scale
    x_end = ox + t_total * t_scale
    y_start = oy - v0 * v_scale
    y_end = oy - vf * v_scale

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .axis { stroke: #475569; stroke-width: 1.5; }',
        '    .grid { stroke: #cbd5e1; stroke-width: 1; stroke-dasharray: 4,4; }',
        '    .trace { stroke: #2563eb; stroke-width: 2.5; fill: none; }',
        '  </style>',
        f'  <line x1="{ox}" y1="{oy}" x2="{ox + plot_w + 20}" y2="{oy}" class="axis" />',
        f'  <line x1="{ox}" y1="{oy - plot_h - 10}" x2="{ox}" y2="{oy + plot_h + 10}" class="axis" />',
        f'  <text x="{ox + plot_w + 5}" y="{oy - 8}" class="lbl">t (s)</text>',
        f'  <text x="{ox - 60}" y="{oy - plot_h + 5}" class="lbl">v (m·s⁻¹)</text>',
        f'  <line x1="{ox}" y1="{y_start}" x2="{x_end}" y2="{y_end}" class="trace" />',
        f'  <line x1="{x_apex}" y1="{oy - 5}" x2="{x_apex}" y2="{oy + 5}" stroke="#475569" stroke-width="1.5" />',
        f'  <text x="{x_apex - 8}" y="{oy + 18}" class="lbl">{_fmt_sa(t_apex)}</text>',
        f'  <line x1="{x_end}" y1="{oy}" x2="{x_end}" y2="{y_end}" class="grid" />',
        f'  <line x1="{ox}" y1="{y_end}" x2="{x_end}" y2="{y_end}" class="grid" />',
        f'  <text x="{x_end - 8}" y="{oy + 18}" class="lbl">{_fmt_sa(t_total)}</text>',
        f'  <text x="{ox - 52}" y="{y_start + 4}" class="lbl">{_fmt_sa(v0)}</text>',
        f'  <text x="{ox - 56}" y="{y_end + 4}" class="lbl">{_fmt_sa(vf)}</text>',
        '</svg>',
    ]
    return "\n".join(svg)


def _svg_vt_bouncing(v_impact: float, v_reb: float, t1: float, dt_c: float, t2: float) -> str:
    """Generate velocity-time graph for a bouncing ball with impact and rebound."""
    w, h = 500, 240
    ox, oy = 70, 120
    plot_w, plot_h = 390, 90
    t_end = t1 + dt_c + t2
    t_scale = plot_w / max(t_end, 0.1)
    v_max = max(v_impact, v_reb, 1.0)
    v_scale = plot_h / v_max

    x_imp = ox + t1 * t_scale
    x_reb = ox + (t1 + dt_c) * t_scale
    x_apex = ox + t_end * t_scale
    y_imp = oy + v_impact * v_scale
    y_reb = oy - v_reb * v_scale

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .axis { stroke: #475569; stroke-width: 1.5; }',
        '    .grid { stroke: #cbd5e1; stroke-width: 1; stroke-dasharray: 4,4; }',
        '    .trace { stroke: #0284c7; stroke-width: 2.2; fill: none; }',
        '    .contact { stroke: #dc2626; stroke-width: 2.2; stroke-dasharray: 3,2; }',
        '  </style>',
        f'  <line x1="{ox}" y1="{oy}" x2="{ox + plot_w + 20}" y2="{oy}" class="axis" />',
        f'  <line x1="{ox}" y1="{oy - plot_h - 10}" x2="{ox}" y2="{oy + plot_h + 10}" class="axis" />',
        f'  <text x="{ox + plot_w + 5}" y="{oy - 8}" class="lbl">t (s)</text>',
        f'  <text x="{ox - 60}" y="{oy - plot_h + 5}" class="lbl">v (m·s⁻¹)</text>',
        # Falling phase: v from 0 down to -v_impact
        f'  <line x1="{ox}" y1="{oy}" x2="{x_imp}" y2="{y_imp}" class="trace" />',
        # Contact rebound jump (vertical)
        f'  <line x1="{x_imp}" y1="{y_imp}" x2="{x_reb}" y2="{y_reb}" class="contact" />',
        # Upward ascent phase: v from +v_reb down to 0 at apex
        f'  <line x1="{x_reb}" y1="{y_reb}" x2="{x_apex}" y2="{oy}" class="trace" />',
        f'  <line x1="{x_imp}" y1="{oy}" x2="{x_imp}" y2="{y_imp}" class="grid" />',
        f'  <text x="{x_imp - 8}" y="{oy - 8}" class="lbl">{_fmt_sa(t1)}</text>',
        f'  <text x="{x_apex - 8}" y="{oy + 18}" class="lbl">{_fmt_sa(round(t_end, 2))}</text>',
        f'  <text x="{ox - 56}" y="{y_imp + 4}" class="lbl">-{_fmt_sa(v_impact)}</text>',
        f'  <text x="{ox - 52}" y="{y_reb + 4}" class="lbl">+{_fmt_sa(v_reb)}</text>',
        '</svg>',
    ]
    return "\n".join(svg)


def _svg_yt_parabola(h_max: float, t_apex: float, t_total: float, h_cliff: float = 0.0) -> str:
    """Generate responsive position-time vector graph."""
    w, h = 500, 240
    ox, oy = 70, 200
    plot_w, plot_h = 390, 160
    t_scale = plot_w / max(t_total, 0.1)
    y_scale = plot_h / max(h_max, 1.0)

    pts = []
    steps = 60
    for i in range(steps + 1):
        frac = i / steps
        t = frac * t_total
        # Kinematics: y(t) = h_cliff + v0 t - 0.5 * 9.8 * t^2
        # where v0 = 9.8 * t_apex
        v0 = 9.8 * t_apex
        y_val = h_cliff + v0 * t - 0.5 * 9.8 * (t ** 2)
        if y_val < 0:
            y_val = 0.0
        px = ox + t * t_scale
        py = oy - y_val * y_scale
        pts.append(f"{px:.1f},{py:.1f}")

    x_apex = ox + t_apex * t_scale
    y_apex = oy - h_max * y_scale
    x_end = ox + t_total * t_scale

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .axis { stroke: #475569; stroke-width: 1.5; }',
        '    .grid { stroke: #cbd5e1; stroke-width: 1; stroke-dasharray: 4,4; }',
        '    .trace { stroke: #7c3aed; stroke-width: 2.5; fill: none; }',
        '  </style>',
        f'  <line x1="{ox}" y1="{oy}" x2="{ox + plot_w + 20}" y2="{oy}" class="axis" />',
        f'  <line x1="{ox}" y1="{oy - plot_h - 15}" x2="{ox}" y2="{oy + 10}" class="axis" />',
        f'  <text x="{ox + plot_w + 5}" y="{oy + 18}" class="lbl">t (s)</text>',
        f'  <text x="{ox - 50}" y="{oy - plot_h}" class="lbl">y (m)</text>',
        f'  <polyline points="{" ".join(pts)}" class="trace" />',
        f'  <line x1="{x_apex}" y1="{oy}" x2="{x_apex}" y2="{y_apex}" class="grid" />',
        f'  <line x1="{ox}" y1="{y_apex}" x2="{x_apex}" y2="{y_apex}" class="grid" />',
        f'  <text x="{x_apex - 8}" y="{oy + 18}" class="lbl">{_fmt_sa(t_apex)}</text>',
        f'  <text x="{x_end - 8}" y="{oy + 18}" class="lbl">{_fmt_sa(t_total)}</text>',
        f'  <text x="{ox - 45}" y="{y_apex + 4}" class="lbl">{_fmt_sa(h_max)}</text>',
    ]
    if h_cliff > 0:
        y_cliff = oy - h_cliff * y_scale
        svg.append(f'  <text x="{ox - 45}" y="{y_cliff + 4}" class="lbl">{_fmt_sa(h_cliff)}</text>')
    svg.append('</svg>')
    return "\n".join(svg)


def _svg_at_graph(a_val: float = -9.8, t_max: float = 4.0, has_spike: bool = False, f_spike: float = 180.0) -> str:
    """Generate responsive acceleration-time vector graph."""
    w, h = 500, 240
    ox, oy = 70, 90
    plot_w, plot_h = 390, 110
    t_scale = plot_w / max(t_max, 0.1)

    y_base = oy + 60
    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .axis { stroke: #475569; stroke-width: 1.5; }',
        '    .grid { stroke: #cbd5e1; stroke-width: 1; stroke-dasharray: 4,4; }',
        '    .trace { stroke: #059669; stroke-width: 2.5; fill: none; }',
        '  </style>',
        f'  <line x1="{ox}" y1="{oy}" x2="{ox + plot_w + 20}" y2="{oy}" class="axis" />',
        f'  <line x1="{ox}" y1="{oy - 60}" x2="{ox}" y2="{oy + plot_h}" class="axis" />',
        f'  <text x="{ox + plot_w + 5}" y="{oy - 8}" class="lbl">t (s)</text>',
        f'  <text x="{ox - 65}" y="{oy - 45}" class="lbl">a (m·s⁻²)</text>',
        f'  <text x="{ox - 48}" y="{y_base + 4}" class="lbl">-{_fmt_sa(abs(a_val))}</text>',
    ]
    if not has_spike:
        svg.append(f'  <line x1="{ox}" y1="{y_base}" x2="{ox + plot_w}" y2="{y_base}" class="trace" />')
        svg.append(f'  <line x1="{ox + plot_w}" y1="{oy}" x2="{ox + plot_w}" y2="{y_base}" class="grid" />')
        svg.append(f'  <text x="{ox + plot_w - 8}" y="{oy + 18}" class="lbl">{_fmt_sa(t_max)}</text>')
    else:
        # Rebound spike at midpoint
        t_sp = t_max / 2.0
        x_sp1 = ox + (t_sp - 0.1) * t_scale
        x_sp_peak = ox + t_sp * t_scale
        x_sp2 = ox + (t_sp + 0.1) * t_scale
        y_peak = oy - 45
        path_d = f"M {ox} {y_base} L {x_sp1} {y_base} L {x_sp_peak} {y_peak} L {x_sp2} {y_base} L {ox + plot_w} {y_base}"
        svg.append(f'  <path d="{path_d}" class="trace" />')
        svg.append(f'  <text x="{ox - 55}" y="{y_peak + 4}" class="lbl">+{_fmt_sa(f_spike)} m·s⁻²</text>')
        svg.append(f'  <text x="{x_sp_peak - 14}" y="{oy + 18}" class="lbl">{_fmt_sa(t_sp)}</text>')
    svg.append('</svg>')
    return "\n".join(svg)


def _svg_ticker_tape(dots: List[float], tape_len: float) -> str:
    """Generate responsive ticker-tape diagram for experimental free fall."""
    w, h = 500, 160
    ox, oy = 40, 75
    tape_w = 420
    tape_h = 40
    scale = tape_w / max(tape_len, 0.1)

    svg = [
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="150" xmlns="http://www.w3.org/2000/svg">',
        '  <rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
        '  <style>',
        '    .lbl { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; fill: #0f172a; font-weight: bold; }',
        '    .tape { fill: #fef08a; stroke: #ca8a04; stroke-width: 1.5; rx: 4; }',
        '    .dot { fill: #1e293b; stroke: none; }',
        '  </style>',
        f'  <rect x="{ox}" y="{oy}" width="{tape_w}" height="{tape_h}" class="tape" />',
        f'  <text x="{ox}" y="{oy - 15}" class="lbl">Direction of motion: falling downwards → (Frequency = 50 Hz)</text>',
    ]
    for i, d in enumerate(dots):
        cx = ox + d * scale
        cy = oy + tape_h / 2.0
        svg.append(f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="3.5" class="dot" />')
        svg.append(f'  <text x="{cx - 4:.1f}" y="{oy + tape_h + 18}" class="lbl">D{i}</text>')
        if i > 0:
            prev_cx = ox + dots[i - 1] * scale
            mid_x = (prev_cx + cx) / 2.0
            gap_cm = d - dots[i - 1]
            svg.append(f'  <text x="{mid_x - 10:.1f}" y="{oy - 6}" class="lbl" fill="#0284c7">{_fmt_sa(gap_cm)} cm</text>')
    svg.append('</svg>')
    return "\n".join(svg)


# =========================================================================== #
# Archetypes 26 to 50
# =========================================================================== #

def _build_26(rng: random.Random) -> Dict[str, Any]:
    sub = "26_bouncing_ball_rebound_velocity_and_speed_loss"
    m = rng.choice([0.15, 0.20, 0.25, 0.30])
    h1 = rng.choice([2.5, 3.2, 3.6, 4.0, 4.5])
    loss_pct = rng.choice([25.0, 30.0, 36.0, 40.0])
    # h2 is determined by fractional energy retention
    ret_factor = 1.0 - (loss_pct / 100.0)
    h2 = round(h1 * ret_factor, 2)
    v_imp = round(math.sqrt(2 * G * h1), 2)
    v_reb = round(math.sqrt(2 * G * h2), 2)

    prompt = (
        f"A ball of mass ${_fmt_sa(m)}\\text{{ kg}}$ is dropped from rest from a height of ${_fmt_sa(h1)}\\text{{ m}}$ onto a flat concrete pavement. "
        f"Upon bouncing, the ball reaches a maximum rebound height of ${_fmt_sa(h2)}\\text{{ m}}$. "
        f"Assume air resistance is negligible and take $g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ downwards.\n\n"
        "1. Calculate the magnitude of the velocity with which the ball strikes the pavement.\n"
        "2. Calculate the rebound speed of the ball as it leaves the pavement.\n"
        "3. Determine the percentage of mechanical kinetic energy lost during the collision with the pavement."
    )
    ans = f"$v_{{\\text{{strike}}}} = {_fmt_sa(v_imp)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, $v_{{\\text{{rebound}}}} = {_fmt_sa(v_reb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, $\\Delta E_k = {_fmt_sa(loss_pct)}\\%$"
    steps = [
        {"rule": "Calculate impact velocity using equations of motion", "op": f"v_1^2 = v_i^2 + 2g\\Delta y = 0 + 2(9{{,}}8)({_fmt_sa(h1)}) = {_fmt_sa(round(2 * G * h1, 2))}", "to": f"{_fmt_sa(v_imp)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Calculate rebound velocity from maximum rebound height", "op": f"v_f^2 = v_2^2 + 2(-9{{,}}8)({_fmt_sa(h2)}) \\implies v_2 = \\sqrt{{2(9{{,}}8)({_fmt_sa(h2)})}}", "to": f"{_fmt_sa(v_reb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Calculate percentage kinetic energy lost", "op": f"\\%_{{\\text{{lost}}}} = \\frac{{mgh_1 - mgh_2}}{{mgh_1}} \\times 100\\% = \\frac{{{_fmt_sa(h1)} - {_fmt_sa(h2)}}}{{{_fmt_sa(h1)}}} \\times 100\\%", "to": f"{_fmt_sa(loss_pct)}\\%"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="In an inelastic collision with the ground, some kinetic energy is converted into heat, sound, and internal deformation.",
        t2="Use v_f^2 = v_i^2 + 2gΔy for both downward and upward legs. The fraction of energy lost equals (h1 - h2) / h1.",
        t3=f"Impact speed = {_fmt_sa(v_imp)} m/s, rebound speed = {_fmt_sa(v_reb)} m/s, energy lost = {_fmt_sa(loss_pct)}%.",
        misconceptions=["assuming_rebound_speed_equals_impact_speed", "sign_error_during_rebound_calculation"],
        marks=6,
    )


def _build_27(rng: random.Random) -> Dict[str, Any]:
    sub = "27_bouncing_ball_second_bounce_apex_height"
    h0 = rng.choice([4.5, 5.0, 6.0, 7.2])
    k = rng.choice([0.64, 0.70, 0.75, 0.80])  # fractional height retained per bounce
    h1 = round(h0 * k, 2)
    h2 = round(h1 * k, 2)

    prompt = (
        f"A rubber ball is released from rest at an initial height of $h_0 = {_fmt_sa(h0)}\\text{{ m}}$ above the floor. "
        f"After its first rebound, it rises to a peak height of $h_1 = {_fmt_sa(h1)}\\text{{ m}}$. "
        "Assuming that the ball loses the same fraction of mechanical energy on each subsequent collision with the floor, "
        "calculate the maximum height $h_2$ reached by the ball after its second bounce."
    )
    ans = f"$h_2 = {_fmt_sa(h2)}\\text{{ m}}$"
    steps = [
        {"rule": "Determine the fractional height retention factor per bounce", "op": f"k = \\frac{{h_1}}{{h_0}} = \\frac{{{_fmt_sa(h1)}}}{{{_fmt_sa(h0)}}}", "to": f"{_fmt_sa(k)}"},
        {"rule": "Calculate height after second bounce using constant retention factor", "op": f"h_2 = k \\times h_1 = {_fmt_sa(k)} \\times {_fmt_sa(h1)}", "to": f"{_fmt_sa(h2)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="If the fraction of mechanical energy retained per bounce is constant, the ratio of successive rebound heights h_(n)/h_(n-1) is constant.",
        t2=f"k = h1 / h0 = {_fmt_sa(k)}, so h2 = k * h1.",
        t3=f"h2 = {_fmt_sa(k)} * {_fmt_sa(h1)} = {_fmt_sa(h2)} m.",
        misconceptions=["assuming_height_loss_is_linear_rather_than_geometric"],
        marks=3,
    )


def _build_28(rng: random.Random) -> Dict[str, Any]:
    sub = "28_bouncing_ball_contact_time_average_net_force"
    m = rng.choice([0.20, 0.25, 0.30, 0.40])
    v_imp = rng.choice([8.0, 9.0, 10.0, 12.0])
    v_reb = rng.choice([5.0, 6.0, 7.0, 8.0])
    dt = rng.choice([0.02, 0.025, 0.03, 0.04])
    # F_net = m * (v_f - v_i) / dt taking upwards as positive
    # v_f = +v_reb, v_i = -v_imp
    dv = v_reb - (-v_imp)
    f_net = round((m * dv) / dt, 2)
    f_n = round(f_net + (m * G), 2)

    prompt = (
        f"A ball of mass ${_fmt_sa(m)}\\text{{ kg}}$ strikes the floor vertically downwards with a speed of ${_fmt_sa(v_imp)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"and rebounds vertically upwards with a speed of ${_fmt_sa(v_reb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"The ball remains in contact with the floor for a duration of ${_fmt_sa(dt)}\\text{{ s}}$.\n\n"
        "1. Taking upwards as the positive direction, calculate the average resultant vertical force exerted on the ball during the collision.\n"
        "2. Calculate the magnitude of the upward normal force exerted by the floor on the ball during contact."
    )
    ans = f"$F_{{\\text{{net}}}} = {_fmt_sa(f_net)}\\text{{ N}}$ upwards, $F_N = {_fmt_sa(f_n)}\\text{{ N}}$ upwards"
    steps = [
        {"rule": "Calculate change in velocity with correct signs", "op": f"\\Delta v = v_f - v_i = (+{_fmt_sa(v_reb)}) - (-{_fmt_sa(v_imp)})", "to": f"+{_fmt_sa(dv)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Calculate net average vertical force using Newton's second law", "op": f"F_{{\\text{{net}}}} = \\frac{{m\\Delta v}}{{\\Delta t}} = \\frac{{{_fmt_sa(m)}({_fmt_sa(dv)})}}{{{_fmt_sa(dt)}}}", "to": f"{_fmt_sa(f_net)}\\text{{ N}}\\text{{ upwards}}"},
        {"rule": "Calculate normal force exerted by the floor (F_net = F_N - F_g)", "op": f"F_N = F_{{\\text{{net}}}} + mg = {_fmt_sa(f_net)} + ({_fmt_sa(m)})(9{{,}}8)", "to": f"{_fmt_sa(f_n)}\\text{{ N}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Velocity is a vector: striking downwards means v_i is negative, and rebounding upwards means v_f is positive.",
        t2="Δv = v_f - v_i = v_reb - (-v_imp) = v_reb + v_imp. Net force F_net = m Δv / Δt, and normal force F_N = F_net + mg.",
        t3=f"F_net = {_fmt_sa(f_net)} N upwards, F_N = {_fmt_sa(f_n)} N upwards.",
        misconceptions=["subtracting_magnitudes_without_vector_direction_signs", "confusing_net_force_with_normal_force"],
        marks=5,
    )


def _build_29(rng: random.Random) -> Dict[str, Any]:
    sub = "29_hot_air_balloon_ascending_dropped_object"
    vb = rng.choice([3.5, 4.2, 5.0, 6.0])
    h0 = rng.choice([45.0, 50.0, 60.0, 75.0])
    # 4.9 t^2 - vb t - h0 = 0
    disc = (vb ** 2) + 4 * 4.9 * h0
    t_flight = round((vb + math.sqrt(disc)) / 9.8, 2)
    v_strike = round(math.sqrt((vb ** 2) + 2 * G * h0), 2)

    prompt = (
        f"A hot-air balloon is ascending vertically upwards at a constant velocity of ${_fmt_sa(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"When the balloon is at a height of ${_fmt_sa(h0)}\\text{{ m}}$ above the ground, a small sandbag is released from the basket. "
        "Ignore air resistance and take $g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ downwards.\n\n"
        "1. State the initial velocity (magnitude and direction) of the sandbag at the exact instant of release.\n"
        "2. Calculate the total time taken by the sandbag to reach the ground.\n"
        "3. Calculate the magnitude of the velocity with which the sandbag strikes the ground."
    )
    ans = f"$v_i = {_fmt_sa(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ upwards, $t = {_fmt_sa(t_flight)}\\text{{ s}}$, $v_{{\\text{{strike}}}} = {_fmt_sa(v_strike)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    steps = [
        {"rule": "State initial velocity inherited from the moving balloon", "op": "v_i = v_{{\\text{{balloon}}}}", "to": f"{_fmt_sa(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ upwards}}"},
        {"rule": "Calculate total flight time to ground using quadratic displacement equation", "op": f"\\Delta y = v_i \\Delta t + \\frac{{1}}{{2}}a\\Delta t^2 \\implies -{_fmt_sa(h0)} = ({_fmt_sa(vb)})\\Delta t - 4{{,}}9\\Delta t^2", "to": f"\\Delta t = {_fmt_sa(t_flight)}\\text{{ s}}"},
        {"rule": "Calculate final ground strike speed using third equation of motion", "op": f"v_f^2 = v_i^2 + 2a\\Delta y = ({_fmt_sa(vb)})^2 + 2(-9{{,}}8)(-{_fmt_sa(h0)})", "to": f"{_fmt_sa(v_strike)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="An object released from a moving carrier inherits the carrier's instantaneous velocity at release (inertia).",
        t2=f"The sandbag moves upwards initially with v_i = +{_fmt_sa(vb)} m/s before decelerating under gravity.",
        t3=f"Flight time = {_fmt_sa(t_flight)} s, strike speed = {_fmt_sa(v_strike)} m/s.",
        misconceptions=["assuming_dropped_object_has_zero_initial_velocity_from_moving_carrier", "sign_confusion_in_vertical_displacement"],
        marks=6,
    )


def _build_30(rng: random.Random) -> Dict[str, Any]:
    sub = "30_hot_air_balloon_descending_dropped_object"
    vb = rng.choice([2.5, 3.0, 4.0, 5.0])
    h0 = rng.choice([35.0, 40.0, 50.0, 60.0])
    v_strike = round(math.sqrt((vb ** 2) + 2 * G * h0), 2)
    # Taking downwards positive: 4.9 t^2 + vb t - h0 = 0
    disc = (vb ** 2) + 4 * 4.9 * h0
    t_flight = round((-vb + math.sqrt(disc)) / 9.8, 2)

    prompt = (
        f"A hot-air balloon is descending vertically downwards towards the ground at a steady speed of ${_fmt_sa(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"When the balloon is ${_fmt_sa(h0)}\\text{{ m}}$ above the ground, a crew member drops a beacon. "
        "Neglect air resistance and take downwards as the positive direction.\n\n"
        "1. Write down the initial velocity of the beacon at the moment of release.\n"
        "2. Calculate the time taken for the beacon to hit the ground.\n"
        "3. Calculate the velocity of the beacon immediately before hitting the ground."
    )
    ans = f"$v_i = +{_fmt_sa(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, $t = {_fmt_sa(t_flight)}\\text{{ s}}$, $v_f = +{_fmt_sa(v_strike)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ downwards"
    steps = [
        {"rule": "Identify initial downward velocity inherited from carrier", "op": "v_i = +v_{{\\text{{balloon}}}}", "to": f"+{_fmt_sa(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ downwards}}"},
        {"rule": "Calculate time to ground taking downwards positive", "op": f"{_fmt_sa(h0)} = ({_fmt_sa(vb)})\\Delta t + 4{{,}}9\\Delta t^2", "to": f"\\Delta t = {_fmt_sa(t_flight)}\\text{{ s}}"},
        {"rule": "Calculate final impact velocity", "op": f"v_f = v_i + g\\Delta t = {_fmt_sa(vb)} + (9{{,}}8)({_fmt_sa(t_flight)})", "to": f"{_fmt_sa(v_strike)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Because the balloon is descending, the released object already possesses a downward initial velocity.",
        t2="Taking downwards as positive, both initial velocity and acceleration are positive.",
        t3=f"Time = {_fmt_sa(t_flight)} s, impact velocity = {_fmt_sa(v_strike)} m/s downwards.",
        misconceptions=["setting_initial_velocity_to_zero_for_dropped_object"],
        marks=5,
    )


def _build_31(rng: random.Random) -> Dict[str, Any]:
    sub = "31_hot_air_balloon_projected_upwards_relative_to_balloon"
    vb = rng.choice([3.0, 4.0, 5.0])
    v_rel = rng.choice([7.0, 8.0, 10.0, 12.0])
    v_ground = vb + v_rel
    h_gain = round((v_ground ** 2) / (2 * G), 2)
    t_apex = round(v_ground / G, 2)

    prompt = (
        f"A hot-air balloon is rising vertically at a constant speed of ${_fmt_sa(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"A passenger in the balloon throws a ball vertically upwards with a speed of ${_fmt_sa(v_rel)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        "relative to the basket. Neglect air resistance.\n\n"
        "1. Calculate the initial velocity of the ball relative to a stationary observer on the ground.\n"
        "2. Calculate the maximum height the ball reaches above the point of release."
    )
    ans = f"$v_{{i,\\text{{ground}}}} = {_fmt_sa(v_ground)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ upwards, $H_{{\\max}} = {_fmt_sa(h_gain)}\\text{{ m}}$"
    steps = [
        {"rule": "Calculate resultant initial velocity relative to the ground", "op": f"v_{{i,\\text{{ground}}}} = v_{{\\text{{balloon}}}} + v_{{\\text{{rel}}}} = {_fmt_sa(vb)} + {_fmt_sa(v_rel)}", "to": f"{_fmt_sa(v_ground)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Calculate maximum height reached above the release point", "op": f"v_f^2 = v_i^2 + 2a\\Delta y \\implies 0 = ({_fmt_sa(v_ground)})^2 + 2(-9{{,}}8)\\Delta y", "to": f"{_fmt_sa(h_gain)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Relativity of velocities: the ground speed is the vector sum of the balloon's velocity and the throwing velocity.",
        t2=f"v_ground = {_fmt_sa(vb)} + {_fmt_sa(v_rel)} = {_fmt_sa(v_ground)} m/s. Then use v_f^2 = v_i^2 - 2g Δy.",
        t3=f"v_ground = {_fmt_sa(v_ground)} m/s, max height above release = {_fmt_sa(h_gain)} m.",
        misconceptions=["omitting_the_balloon_velocity_from_the_projectile_launch_speed"],
        marks=4,
    )


def _build_32(rng: random.Random) -> Dict[str, Any]:
    sub = "32_simultaneous_release_one_dropped_one_projected_up"
    h_total = rng.choice([60.0, 75.0, 80.0, 90.0, 100.0])
    v_up = rng.choice([25.0, 30.0, 35.0, 40.0])
    # Ball A dropped: y_A(t) = h_total - 0.5 * g * t^2
    # Ball B projected up: y_B(t) = v_up * t - 0.5 * g * t^2
    # Meeting: y_A = y_B => h_total = v_up * t => t = h_total / v_up
    t_meet = round(h_total / v_up, 2)
    y_meet = round(v_up * t_meet - 0.5 * G * (t_meet ** 2), 2)

    prompt = (
        f"At the same instant, Ball A is dropped from rest from the top of a cliff of height ${_fmt_sa(h_total)}\\text{{ m}}$, "
        f"and Ball B is projected vertically upwards from the base of the cliff with an initial speed of ${_fmt_sa(v_up)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        "along the same vertical line. Ignore air resistance and assume they pass without colliding.\n\n"
        "1. Calculate the time elapsed from launch until both balls are at the same vertical height.\n"
        "2. Calculate the height above the ground at which they pass each other."
    )
    ans = f"$t = {_fmt_sa(t_meet)}\\text{{ s}}$, $y = {_fmt_sa(y_meet)}\\text{{ m}}$ above ground"
    steps = [
        {"rule": "Equate vertical position equations for both objects", "op": f"h_{{\\text{{total}}}} - \\frac{{1}}{{2}}gt^2 = v_{{\\text{{up}}}}t - \\frac{{1}}{{2}}gt^2 \\implies {_fmt_sa(h_total)} = ({_fmt_sa(v_up)})t", "to": f"t = {_fmt_sa(t_meet)}\\text{{ s}}"},
        {"rule": "Calculate vertical meeting height from ground using position of Ball B", "op": f"y = v_{{\\text{{up}}}}t - 4{{,}}9t^2 = ({_fmt_sa(v_up)})({_fmt_sa(t_meet)}) - 4{{,}}9({_fmt_sa(t_meet)})^2", "to": f"{_fmt_sa(y_meet)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Notice that both balls experience identical downward gravitational acceleration (-0.5 g t^2), which cancels when equating positions.",
        t2="The meeting time is simply t = H / v_up.",
        t3=f"Meeting time = {_fmt_sa(t_meet)} s, height above ground = {_fmt_sa(y_meet)} m.",
        misconceptions=["forgetting_that_acceleration_cancels_in_relative_motion_problems"],
        marks=5,
    )


def _build_33(rng: random.Random) -> Dict[str, Any]:
    sub = "33_simultaneous_release_two_projected_opposite_directions"
    h_tower = rng.choice([80.0, 90.0, 100.0, 120.0])
    v_top_down = rng.choice([10.0, 12.0, 15.0])
    v_bot_up = rng.choice([25.0, 30.0, 35.0])
    # Relative velocity approach: v_rel = v_top_down + v_bot_up
    v_rel = v_top_down + v_bot_up
    t_pass = round(h_tower / v_rel, 2)
    y_pass_ground = round(v_bot_up * t_pass - 0.5 * G * (t_pass ** 2), 2)

    prompt = (
        f"Projectile 1 is fired vertically upwards from the ground with an initial speed of ${_fmt_sa(v_bot_up)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"Simultaneously, Projectile 2 is projected vertically downwards from the top of a tower of height ${_fmt_sa(h_tower)}\\text{{ m}}$ "
        f"with an initial speed of ${_fmt_sa(v_top_down)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        "1. Calculate the time taken for the two projectiles to pass each other.\n"
        "2. Calculate the height above the ground at which they pass each other."
    )
    ans = f"$t = {_fmt_sa(t_pass)}\\text{{ s}}$, $y = {_fmt_sa(y_pass_ground)}\\text{{ m}}$ above ground"
    steps = [
        {"rule": "Calculate relative approach speed and passing time", "op": f"v_{{\\text{{rel}}}} = v_1 + v_2 = {_fmt_sa(v_bot_up)} + {_fmt_sa(v_top_down)} \\implies t = \\frac{{{_fmt_sa(h_tower)}}}{{{_fmt_sa(v_rel)}}}", "to": f"{_fmt_sa(t_pass)}\\text{{ s}}"},
        {"rule": "Calculate position of lower projectile at passing time", "op": f"y = v_1 t - \\frac{{1}}{{2}}gt^2 = ({_fmt_sa(v_bot_up)})({_fmt_sa(t_pass)}) - 4{{,}}9({_fmt_sa(t_pass)})^2", "to": f"{_fmt_sa(y_pass_ground)}\\text{{ m}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Since both objects experience the same acceleration due to gravity, their relative acceleration is zero. They approach at constant relative speed (v1 + v2).",
        t2="t = H / (v1 + v2), and substitution into y1(t) gives the passing height.",
        t3=f"t = {_fmt_sa(t_pass)} s, y = {_fmt_sa(y_pass_ground)} m.",
        misconceptions=["applying_gravity_twice_to_relative_approach_speed"],
        marks=5,
    )


def _build_34(rng: random.Random) -> Dict[str, Any]:
    sub = "34_delayed_release_catchup_problem"
    h_drop = rng.choice([60.0, 75.0, 80.0, 90.0])
    dt = rng.choice([1.0, 1.2, 1.5])
    # Ball 1 dropped from rest: t1 = sqrt(2 * h_drop / g)
    t1 = round(math.sqrt(2 * h_drop / G), 2)
    # Ball 2 thrown after delay dt: flight time t2 = t1 - dt
    t2 = round(t1 - dt, 2)
    # h_drop = v2 * t2 + 0.5 * g * t2^2 => v2 = (h_drop - 4.9 * t2^2) / t2
    v2 = round((h_drop - 0.5 * G * (t2 ** 2)) / t2, 2)

    prompt = (
        f"A stone is dropped from rest from the edge of a cliff of height ${_fmt_sa(h_drop)}\\text{{ m}}$. "
        f"Exactly ${_fmt_sa(dt)}\\text{{ s}}$ later, a second stone is thrown vertically downwards from the same position "
        "with an initial speed $v_2$ so that both stones strike the ground below at the exact same instant.\n\n"
        "1. Calculate the total time taken by the first stone to reach the ground.\n"
        "2. Calculate the initial downward speed $v_2$ required for the second stone."
    )
    ans = f"$t_1 = {_fmt_sa(t1)}\\text{{ s}}$, $v_2 = {_fmt_sa(v2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ downwards"
    steps = [
        {"rule": "Calculate flight time of the first dropped stone", "op": f"\\Delta y = \\frac{{1}}{{2}}gt_1^2 \\implies t_1 = \\sqrt{{\\frac{{2({_fmt_sa(h_drop)})}}{{9{{,}}8}}}}", "to": f"{_fmt_sa(t1)}\\text{{ s}}"},
        {"rule": "Calculate flight duration available for the second stone", "op": f"t_2 = t_1 - \\Delta t = {_fmt_sa(t1)} - {_fmt_sa(dt)}", "to": f"{_fmt_sa(t2)}\\text{{ s}}"},
        {"rule": "Solve for initial downward speed of the second stone", "op": f"\\Delta y = v_2 t_2 + 4{{,}}9 t_2^2 \\implies {_fmt_sa(h_drop)} = v_2({_fmt_sa(t2)}) + 4{{,}}9({_fmt_sa(t2)})^2", "to": f"{_fmt_sa(v2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The second stone has a shorter flight time: t2 = t1 - delay.",
        t2="Use Δy = v2 * t2 + 0.5 * g * t2^2 to find v2.",
        t3=f"t1 = {_fmt_sa(t1)} s, required launch speed v2 = {_fmt_sa(v2)} m/s.",
        misconceptions=["adding_the_delay_time_instead_of_subtracting_it_for_the_chasing_object"],
        marks=5,
    )


def _build_35(rng: random.Random) -> Dict[str, Any]:
    sub = "35_velocity_time_graph_upward_projection_from_ground"
    v0 = rng.choice([19.6, 24.5, 29.4, 34.3])
    t_apex = round(v0 / G, 2)
    t_total = round(2 * t_apex, 2)
    h_max = round((v0 ** 2) / (2 * G), 2)
    vf = -v0

    svg_str = _svg_vt_graph(v0, t_apex, t_total, vf)
    prompt = (
        "Refer to the accompanying velocity-time ($v\\text{{-}}t$) graph for a projectile launched vertically upwards from the ground.\n\n"
        f"The object leaves the ground at $t = 0\\text{{ s}}$ with velocity $v_i = +{_fmt_sa(v0)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, "
        f"reaches its apex at $t = {_fmt_sa(t_apex)}\\text{{ s}}$, and returns to the ground at $t = {_fmt_sa(t_total)}\\text{{ s}}$.\n\n"
        "1. State what physical quantity is represented by the gradient of this graph.\n"
        "2. Using the coordinates on the graph, calculate the acceleration of the projectile.\n"
        "3. Using the area under the graph from $t = 0\\text{{ s}}$ to $t = t_{{\\text{{apex}}}}$, calculate the maximum height reached above the ground."
    )
    ans = f"Gradient = acceleration, $a = -9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$, $H_{{\\max}} = {_fmt_sa(h_max)}\\text{{ m}}$"
    steps = [
        {"rule": "Identify physical meaning of gradient of velocity-time graph", "op": "\\text{{gradient}} = \\frac{{\\Delta v}}{{\\Delta t}}", "to": "\\text{{Acceleration}}"},
        {"rule": "Calculate numerical gradient using apex coordinates", "op": f"a = \\frac{{0 - ({_fmt_sa(v0)})}}{{{_fmt_sa(t_apex)} - 0}}", "to": "-9{{,}}\\text{{8 m}}\\cdot\\text{{s}}^{{-2}}\\text{{ (downwards)}}"},
        {"rule": "Calculate maximum vertical displacement using area of triangle", "op": f"\\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} = \\frac{{1}}{{2}}({_fmt_sa(t_apex)})({_fmt_sa(v0)})", "to": f"{_fmt_sa(h_max)}\\text{{ m}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Velocity-Time Graph for Projectile"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The gradient of a v-t graph represents acceleration; the area between the curve and the time axis represents displacement.",
        t2=f"Gradient = Δv / Δt = -{_fmt_sa(v0)} / {_fmt_sa(t_apex)} = -9,8 m/s^2. Area = 0,5 * base * height.",
        t3=f"Acceleration = -9,8 m/s^2, H_max = {_fmt_sa(h_max)} m.",
        misconceptions=["believing_acceleration_is_zero_at_t_apex_where_velocity_is_zero"],
        marks=5,
        diagram_spec=d_spec,
    )


def _build_36(rng: random.Random) -> Dict[str, Any]:
    sub = "36_velocity_time_graph_cliff_launch_to_ground"
    v0 = rng.choice([14.7, 19.6, 24.5])
    h_cliff = rng.choice([25.0, 30.0, 40.0, 50.0])
    t_apex = round(v0 / G, 2)
    vf = round(-math.sqrt((v0 ** 2) + 2 * G * h_cliff), 2)
    t_total = round((v0 - vf) / G, 2)
    h_up = round(0.5 * t_apex * v0, 2)
    h_down = round(0.5 * (t_total - t_apex) * abs(vf), 2)

    svg_str = _svg_vt_graph(v0, t_apex, t_total, vf)
    prompt = (
        "Refer to the accompanying velocity-time ($v\\text{{-}}t$) graph illustrating the motion of a ball projected vertically upwards from the edge of a platform.\n\n"
        f"The projectile is launched upwards with initial velocity $v_i = +{_fmt_sa(v0)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, reaches its apex at $t = {_fmt_sa(t_apex)}\\text{{ s}}$, "
        f"and hits the ground at $t = {_fmt_sa(t_total)}\\text{{ s}}$ with velocity $v_f = {_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        "1. Calculate the maximum height reached above the platform using the positive area under the graph.\n"
        "2. Using the geometric areas between the graph and the time axis, calculate the height of the platform."
    )
    ans = f"$H_{{\\text{{platform}}}} = {_fmt_sa(h_cliff)}\\text{{ m}}$, $H_{{\\text{{above}}}} = {_fmt_sa(h_up)}\\text{{ m}}$"
    steps = [
        {"rule": "Calculate upward displacement above platform from positive area", "op": f"\\Delta y_{{\\text{{up}}}} = \\frac{{1}}{{2}}({_fmt_sa(t_apex)})({_fmt_sa(v0)})", "to": f"{_fmt_sa(h_up)}\\text{{ m}}"},
        {"rule": "Calculate downward displacement from negative area", "op": f"\\Delta y_{{\\text{{down}}}} = \\frac{{1}}{{2}}({_fmt_sa(round(t_total - t_apex, 2))})({_fmt_sa(vf)})", "to": f"-{_fmt_sa(h_down)}\\text{{ m}}"},
        {"rule": "Determine platform height from net vertical displacement", "op": f"H_{{\\text{{platform}}}} = |\\Delta y_{{\\text{{down}}}}| - \\Delta y_{{\\text{{up}}}} = {_fmt_sa(h_down)} - {_fmt_sa(h_up)}", "to": f"{_fmt_sa(h_cliff)}\\text{{ m}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Velocity-Time Graph for Cliff Projectile"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The positive area above the time axis is displacement upwards; the negative area below the time axis is displacement downwards.",
        t2=f"Net displacement Δy = Area_up - Area_down = -platform_height.",
        t3=f"Platform height = {_fmt_sa(h_cliff)} m.",
        misconceptions=["adding_positive_and_negative_areas_to_find_net_displacement_without_accounting_for_sign"],
        marks=5,
        diagram_spec=d_spec,
    )


def _build_37(rng: random.Random) -> Dict[str, Any]:
    sub = "37_velocity_time_graph_bouncing_ball_single_bounce"
    v_imp = rng.choice([9.8, 12.0, 14.0])
    v_reb = round(v_imp * rng.choice([0.7, 0.75, 0.8]), 2)
    t1 = round(v_imp / G, 2)
    dt_c = 0.04
    t2 = round(v_reb / G, 2)
    t_end = round(t1 + dt_c + t2, 2)
    h_reb = round((v_reb ** 2) / (2 * G), 2)

    svg_str = _svg_vt_bouncing(v_imp, v_reb, t1, dt_c, t2)
    prompt = (
        "Refer to the accompanying velocity-time ($v\\text{{-}}t$) graph for a ball dropped from rest that bounces once off the floor.\n\n"
        f"The ball strikes the floor at $t = {_fmt_sa(t1)}\\text{{ s}}$ with velocity $-{_fmt_sa(v_imp)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, "
        f"undergoes a rapid collision lasting ${_fmt_sa(dt_c)}\\text{{ s}}$, rebounds upwards with initial speed $+{_fmt_sa(v_reb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, "
        f"and reaches its rebound apex at $t = {_fmt_sa(t_end)}\\text{{ s}}$.\n\n"
        "1. Explain why the gradient of both downward-sloping linear sections is the same.\n"
        "2. Calculate the maximum rebound height reached by the ball after bouncing."
    )
    ans = f"Gradient $= -9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ (free-fall acceleration $g$), $h_{{\\text{{rebound}}}} = {_fmt_sa(h_reb)}\\text{{ m}}$"
    steps = [
        {"rule": "Explain identical slopes during both airborne phases", "op": "\\text{{Airborne motion under gravity only}}", "to": "a = -9{{,}}\\text{{8 m}}\\cdot\\text{{s}}^{{-2}}\\text{{ throughout}}"},
        {"rule": "Calculate maximum rebound height from area under rebound portion of graph", "op": f"\\Delta y = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} = \\frac{{1}}{{2}}({_fmt_sa(t2)})({_fmt_sa(v_reb)})", "to": f"{_fmt_sa(h_reb)}\\text{{ m}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Bouncing Ball Velocity-Time Graph"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Whenever the ball is in the air, the only force acting is gravity, so the gradient of the v-t graph is always -9,8 m/s^2.",
        t2=f"Rebound height is the area of the upward triangle: 0,5 * {_fmt_sa(t2)} * {_fmt_sa(v_reb)} = {_fmt_sa(h_reb)} m.",
        t3=f"Rebound height = {_fmt_sa(h_reb)} m.",
        misconceptions=["thinking_gravity_changes_direction_after_the_bounce"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_38(rng: random.Random) -> Dict[str, Any]:
    sub = "38_velocity_time_graph_bouncing_ball_multiple_bounces"
    v0 = rng.choice([8.0, 10.0, 12.0])
    e = rng.choice([0.80, 0.85])
    v1 = round(v0 * e, 2)
    v2 = round(v1 * e, 2)
    t_drop = round(v0 / G, 2)
    dt = 0.03
    t_reb1 = round(v1 / G, 2)

    svg_str = _svg_vt_bouncing(v0, v1, t_drop, dt, t_reb1)
    prompt = (
        "Refer to the accompanying velocity-time ($v\\text{{-}}t$) graph illustrating the consecutive bounces of a ball dropped from rest.\n\n"
        f"The first impact occurs with speed $v_1 = {_fmt_sa(v0)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, and the rebound speed is $v_1' = {_fmt_sa(v1)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        "1. Calculate the coefficient of restitution $e = \\frac{v'}{v}$ for the first bounce.\n"
        "2. If this collision efficiency factor remains constant, determine the expected rebound speed $v_2'$ after the second bounce."
    )
    ans = f"$e = {_fmt_sa(e)}$, $v_2' = {_fmt_sa(v2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    steps = [
        {"rule": "Calculate ratio of rebound speed to impact speed", "op": f"e = \\frac{{{_fmt_sa(v1)}}}{{{_fmt_sa(v0)}}}", "to": f"{_fmt_sa(e)}"},
        {"rule": "Calculate second rebound speed", "op": f"v_2' = e \\times v_1' = {_fmt_sa(e)} \\times {_fmt_sa(v1)}", "to": f"{_fmt_sa(v2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Consecutive Bounces Velocity-Time Graph"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="In successive inelastic collisions, the ratio of rebound velocity to impact velocity is the coefficient of restitution.",
        t2=f"v2' = e * v1' = {_fmt_sa(e)} * {_fmt_sa(v1)}.",
        t3=f"e = {_fmt_sa(e)}, v2' = {_fmt_sa(v2)} m/s.",
        misconceptions=["assuming_speed_reduction_is_by_constant_arithmetic_subtraction"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_39(rng: random.Random) -> Dict[str, Any]:
    sub = "39_position_time_graph_upward_projection_parabola"
    v0 = rng.choice([14.7, 19.6, 24.5, 29.4])
    t_apex = round(v0 / G, 2)
    t_total = round(2 * t_apex, 2)
    h_max = round((v0 ** 2) / (2 * G), 2)

    svg_str = _svg_yt_parabola(h_max, t_apex, t_total, 0.0)
    prompt = (
        "Refer to the accompanying position-time ($y\\text{{-}}t$) graph illustrating the vertical motion of a ball projected upwards from ground level.\n\n"
        f"The vertex of the symmetrical parabola occurs at $(t, y) = ({_fmt_sa(t_apex)}\\text{{ s}}, {_fmt_sa(h_max)}\\text{{ m}})$.\n\n"
        "1. What is the value of the gradient of the graph at the vertex ($t = {_fmt_sa(t_apex)}\\text{{ s}}$), and what physical quantity does it represent?\n"
        "2. Using the coordinates of the apex, calculate the initial projection speed $v_i$ of the ball."
    )
    ans = f"Gradient at vertex $= 0\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ (velocity is zero at apex), $v_i = {_fmt_sa(v0)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    steps = [
        {"rule": "Interpret gradient at turning point of position-time graph", "op": "\\frac{dy}{dt} = 0", "to": "v = 0\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ at apex}}"},
        {"rule": "Calculate initial projection velocity using apex height", "op": f"v_f^2 = v_i^2 - 2gH_{{\\max}} \\implies v_i = \\sqrt{{2(9{{,}}8)({_fmt_sa(h_max)})}}", "to": f"{_fmt_sa(v0)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Position-Time Graph for Vertical Projection"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The gradient of a position-time graph is instantaneous velocity. At the highest point (turning point), tangent is horizontal so v = 0.",
        t2=f"Use v_f^2 = v_i^2 - 2g H_max with v_f = 0.",
        t3=f"Gradient at vertex = 0 m/s, launch speed v_i = {_fmt_sa(v0)} m/s.",
        misconceptions=["confusing_zero_velocity_at_apex_with_zero_acceleration"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_40(rng: random.Random) -> Dict[str, Any]:
    sub = "40_position_time_graph_cliff_launch_crossing_zero"
    v0 = rng.choice([14.7, 19.6])
    h_cliff = rng.choice([25.0, 30.0, 40.0])
    t_apex = round(v0 / G, 2)
    h_max = round(h_cliff + (v0 ** 2) / (2 * G), 2)
    vf = round(math.sqrt((v0 ** 2) + 2 * G * h_cliff), 2)
    t_total = round((v0 + vf) / G, 2)

    svg_str = _svg_yt_parabola(h_max, t_apex, t_total, h_cliff)
    prompt = (
        "Refer to the accompanying position-time ($y\\text{{-}}t$) graph for a projectile fired upwards from a launch pad above ground level.\n\n"
        f"The curve shows the projectile at $y = {_fmt_sa(h_cliff)}\\text{{ m}}$ at $t = 0\\text{{ s}}$, reaching a maximum height of "
        f"$y = {_fmt_sa(h_max)}\\text{{ m}}$ at $t = {_fmt_sa(t_apex)}\\text{{ s}}$, and striking the ground level ($y = 0\\text{{ m}}$) at $t = {_fmt_sa(t_total)}\\text{{ s}}$.\n\n"
        "1. Identify the height of the launch pad above the ground.\n"
        "2. Calculate the vertical speed with which the projectile strikes the ground."
    )
    ans = f"Launch pad height $= {_fmt_sa(h_cliff)}\\text{{ m}}$, $v_{{\\text{{strike}}}} = {_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    steps = [
        {"rule": "Read launch pad height from y-intercept at t = 0", "op": "y(0) = H_{{\\text{{launch}}}}", "to": f"{_fmt_sa(h_cliff)}\\text{{ m}}"},
        {"rule": "Calculate ground strike speed from total descent from apex", "op": f"v_f = \\sqrt{{2gH_{{\\max}}}} = \\sqrt{{2(9{{,}}8)({_fmt_sa(h_max)})}}", "to": f"{_fmt_sa(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Position-Time Graph for Cliff Launch"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The y-intercept at t = 0 gives the initial launch height. The total vertical fall from apex to ground is H_max.",
        t2=f"v_strike = sqrt(2 * 9,8 * {_fmt_sa(h_max)}) = {_fmt_sa(vf)} m/s.",
        t3=f"Launch height = {_fmt_sa(h_cliff)} m, strike speed = {_fmt_sa(vf)} m/s.",
        misconceptions=["measuring_maximum_height_only_relative_to_cliff_edge_instead_of_ground"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_41(rng: random.Random) -> Dict[str, Any]:
    sub = "41_position_time_graph_bouncing_ball_parabolic_arcs"
    h0 = rng.choice([3.2, 4.0, 4.5, 5.0])
    ret = rng.choice([0.64, 0.70, 0.75])
    h1 = round(h0 * ret, 2)
    t1 = round(math.sqrt(2 * h0 / G), 2)
    t_reb = round(math.sqrt(2 * h1 / G), 2)
    t_bounce1 = t1
    t_apex1 = round(t1 + t_reb, 2)

    prompt = (
        f"A ball is released from rest from an initial height of $h_0 = {_fmt_sa(h0)}\\text{{ m}}$. "
        f"On its first bounce, it reaches a peak height of $h_1 = {_fmt_sa(h1)}\\text{{ m}}$.\n\n"
        "In a position-time ($y\\text{{-}}t$) graph of this motion with the ground as $y = 0\\text{{ m}}$:\n"
        "1. Describe the shape of the curve while the ball is airborne.\n"
        f"2. Calculate the time $t_1$ at which the ball first strikes the ground.\n"
        f"3. Calculate the time $t_2$ at which the ball reaches its first rebound apex (neglect contact time)."
    )
    ans = f"Inverted parabolic arcs, $t_1 = {_fmt_sa(t1)}\\text{{ s}}$, $t_2 = {_fmt_sa(t_apex1)}\\text{{ s}}$"
    steps = [
        {"rule": "State shape of position-time curve under uniform acceleration", "op": "y(t) = y_0 + v_0 t - 4{{,}}9 t^2", "to": "\\text{{Concave-down parabolic segments}}"},
        {"rule": "Calculate first impact time from free fall", "op": f"t_1 = \\sqrt{{\\frac{{2h_0}}{{g}}}} = \\sqrt{{\\frac{{2({_fmt_sa(h0)})}}{{9{{,}}8}}}}", "to": f"{_fmt_sa(t1)}\\text{{ s}}"},
        {"rule": "Calculate time to reach rebound peak", "op": f"t_2 = t_1 + \\sqrt{{\\frac{{2h_1}}{{g}}}} = {_fmt_sa(t1)} + {_fmt_sa(t_reb)}", "to": f"{_fmt_sa(t_apex1)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Under constant gravitational acceleration, y(t) is quadratic in time, producing parabolic arcs between bounces.",
        t2=f"t1 = sqrt(2 * h0 / g) = {_fmt_sa(t1)} s; time to rebound apex is t1 + sqrt(2 * h1 / g).",
        t3=f"t1 = {_fmt_sa(t1)} s, t2 = {_fmt_sa(t_apex1)} s.",
        misconceptions=["drawing_straight_linear_v-shapes_instead_of_curved_parabolas_for_position_time_graphs"],
        marks=5,
    )


def _build_42(rng: random.Random) -> Dict[str, Any]:
    sub = "42_acceleration_time_graph_projectile_free_fall"
    t_flight = rng.choice([3.0, 4.0, 5.0, 6.0])
    svg_str = _svg_at_graph(-9.8, t_flight, has_spike=False)

    prompt = (
        "Refer to the accompanying acceleration-time ($a\\text{{-}}t$) graph for a ball projected vertically upwards from the ground.\n\n"
        f"The flight lasts for ${_fmt_sa(t_flight)}\\text{{ s}}$ until the ball returns to the ground. "
        "Taking upwards as the positive direction:\n\n"
        "1. Explain why the line on the graph is horizontal and lies at $-9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ throughout the entire flight.\n"
        "2. What physical quantity is represented by the area between the horizontal line and the time axis from $t = 0\\text{{ s}}$ to $t = {_fmt_sa(t_flight)}\\text{{ s}}$?\n"
        f"3. Calculate the numerical value of this area."
    )
    d_v = round(-9.8 * t_flight, 2)
    ans = f"Constant downward gravitational acceleration $g$, Area represents change in velocity $\\Delta v = {_fmt_sa(d_v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    steps = [
        {"rule": "Explain constant acceleration in free fall", "op": "F_{{\\text{{net}}}} = F_g = mg \\implies a = -g", "to": "-9{{,}}\\text{{8 m}}\\cdot\\text{{s}}^{{-2}}\\text{{ constant}}"},
        {"rule": "Identify meaning of area under acceleration-time graph", "op": "\\int a\\, dt = \\Delta v", "to": "\\text{{Change in velocity }} \\Delta v"},
        {"rule": "Calculate numerical area", "op": f"\\text{{Area}} = (-9{{,}}8) \\times {_fmt_sa(t_flight)}", "to": f"{_fmt_sa(d_v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Acceleration-Time Graph in Free Fall"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="In free fall, the acceleration is constant at 9,8 m/s^2 downwards regardless of whether the object is moving upwards, instantaneously at rest at apex, or moving downwards.",
        t2="The area between an a-t graph and the time axis equals the change in velocity (Δv = a * Δt).",
        t3=f"Area = {_fmt_sa(d_v)} m/s.",
        misconceptions=["believing_the_acceleration_drops_to_zero_at_the_highest_point"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_43(rng: random.Random) -> Dict[str, Any]:
    sub = "43_acceleration_time_graph_bouncing_ball_impact_spike"
    t_flight = rng.choice([3.2, 3.6, 4.0, 4.4, 4.8])
    f_spike = rng.choice([120.0, 150.0, 180.0, 210.0, 240.0])
    svg_str = _svg_at_graph(-9.8, t_flight, has_spike=True, f_spike=f_spike)

    prompt = (
        "Refer to the accompanying acceleration-time ($a\\text{{-}}t$) graph for a bouncing rubber ball.\n\n"
        "The graph remains at $-9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ while the ball is airborne, but exhibits an intense, "
        "brief positive peak during its collision with the floor.\n\n"
        "1. Taking upwards as positive, explain why the acceleration during collision with the floor is positive and much larger in magnitude than $9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$.\n"
        "2. State what upward force causes this large positive acceleration during contact with the floor."
    )
    ans = "Upward normal force from floor $F_N > mg$ causes rapid upward change in velocity ($\\Delta v > 0$); Normal force $F_N$"
    steps = [
        {"rule": "Explain positive acceleration spike during contact", "op": "a = \\frac{v_f - v_i}{\\Delta t} = \\frac{(+v_{{\\text{{reb}}}}) - (-v_{{\\text{{imp}}}})}{\\Delta t} > 0", "to": "\\text{{Large positive upward acceleration}}"},
        {"rule": "Identify causative contact force", "op": "F_{{\\text{{net}}}} = F_N - mg = ma", "to": "\\text{{Upward normal force }} F_N"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Acceleration-Time Graph with Impact Spike"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="During contact, the floor exerts an upward normal force F_N that far exceeds the ball's weight, causing a rapid upward deceleration and reversal of velocity.",
        t2="Since Δv = (+v_reb) - (-v_imp) > 0 over a small contact time Δt, the contact acceleration is large and positive.",
        t3="Normal force F_N produces large positive acceleration spike.",
        misconceptions=["believing_the_acceleration_during_floor_contact_is_zero_or_negative"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_44(rng: random.Random) -> Dict[str, Any]:
    sub = "44_graph_conversion_position_time_to_velocity_time"
    v0 = rng.choice([19.6, 24.5, 29.4])
    t_apex = round(v0 / G, 2)
    h_max = round((v0 ** 2) / (2 * G), 2)
    t_total = round(2 * t_apex, 2)
    svg_str = _svg_yt_parabola(h_max, t_apex, t_total, 0.0)

    prompt = (
        "Refer to the accompanying position-time ($y\\text{{-}}t$) graph for a stone projected vertically upwards from ground level ($y = 0\\text{{ m}}$).\n\n"
        f"The parabolic curve has its vertex at $(t, y) = ({_fmt_sa(t_apex)}\\text{{ s}}, {_fmt_sa(h_max)}\\text{{ m}})$ "
        f"and returns to $y = 0\\text{{ m}}$ at $t = {_fmt_sa(t_total)}\\text{{ s}}$.\n\n"
        "If this motion is converted into a corresponding velocity-time ($v\\text{{-}}t$) graph (taking upwards as positive):\n"
        "1. State the shape and sign of the gradient of the $v\\text{{-}}t$ line.\n"
        "2. State the value of the vertical velocity at $t = 0\\text{{ s}}$ and at $t = {_fmt_sa(t_apex)}\\text{{ s}}$."
    )
    ans = f"Straight line with constant negative gradient ($-9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$); $v(0) = +{_fmt_sa(v0)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, $v({_fmt_sa(t_apex)}) = 0\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$"
    steps = [
        {"rule": "Determine shape and slope of converted v-t graph", "op": "v(t) = \\frac{dy}{dt} = v_0 - 9{{,}}8 t", "to": "\\text{{Straight line with slope }} -9{{,}}8"},
        {"rule": "Identify velocity at start and apex", "op": f"v_0 = \\sqrt{{2(9{{,}}8)({_fmt_sa(h_max)})}},\\; v_{{\\text{{apex}}}} = 0", "to": f"+{_fmt_sa(v0)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}\\text{{ and }} 0\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Position-Time Graph for Conversion"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The gradient of y-t is the value of v-t. A parabolic y-t graph converts to a straight line on a v-t graph.",
        t2=f"The slope of v-t is constant at -9,8 m/s^2; at the apex t = {_fmt_sa(t_apex)} s, v = 0.",
        t3=f"Slope = -9,8 m/s^2, v(0) = +{_fmt_sa(v0)} m/s, v({_fmt_sa(t_apex)}) = 0 m/s.",
        misconceptions=["converting_parabolic_curve_into_curved_v_t_graph_instead_of_linear"],
        marks=4,
        diagram_spec=d_spec,
    )


def _build_45(rng: random.Random) -> Dict[str, Any]:
    sub = "45_graph_conversion_velocity_time_to_position_time"
    v0 = rng.choice([14.7, 19.6, 24.5, 34.3])
    t_apex = round(v0 / G, 2)
    h_max = round((v0 ** 2) / (2 * G), 2)

    prompt = (
        f"A velocity-time ($v\\text{{-}}t$) graph for a projectile launched vertically upwards from the ground is a straight line "
        f"starting at $(0\\text{{ s}}, +{_fmt_sa(v0)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}})$ and crossing the time axis at $t = {_fmt_sa(t_apex)}\\text{{ s}}$.\n\n"
        "If this motion is converted into a position-time ($y\\text{{-}}t$) graph:\n"
        "1. State the coordinates $(t, y)$ of the turning point (apex vertex) of the resulting curve.\n"
        "2. Explain how this vertical coordinate was calculated from the original $v\\text{{-}}t$ graph."
    )
    ans = f"Vertex coordinates $= ({_fmt_sa(t_apex)}\\text{{ s}}, {_fmt_sa(h_max)}\\text{{ m}})$; Calculated from triangular area under $v\\text{{-}}t$ graph"
    steps = [
        {"rule": "Calculate apex height using triangular area of v-t graph", "op": f"\\text{{Area}} = \\frac{{1}}{{2}}({_fmt_sa(t_apex)})({_fmt_sa(v0)})", "to": f"{_fmt_sa(h_max)}\\text{{ m}}"},
        {"rule": "State vertex coordinates of position-time graph", "op": f"(t_{{\\text{{apex}}}}, H_{{\\max}})", "to": f"({_fmt_sa(t_apex)}\\text{{ s}}, {_fmt_sa(h_max)}\\text{{ m}})"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Displacement is the integral (area under) the v-t graph. A linear v-t graph integrates to a parabolic y-t graph.",
        t2=f"The area under v-t from t = 0 to t_apex gives H_max = 0,5 * {_fmt_sa(t_apex)} * {_fmt_sa(v0)} = {_fmt_sa(h_max)} m.",
        t3=f"Vertex = ({_fmt_sa(t_apex)} s, {_fmt_sa(h_max)} m).",
        misconceptions=["multiplying_velocity_by_time_without_the_half_factor_for_triangular_area"],
        marks=4,
    )


def _build_46(rng: random.Random) -> Dict[str, Any]:
    sub = "46_experimental_data_ticker_timer_free_fall"
    # 50 Hz timer => dt = 0.02 s between dots
    # Consecutive positions from rest: y_n = 0.5 * g * (n * dt)^2
    g_exp = rng.choice([9.60, 9.70, 9.75, 9.80, 9.85])
    dt = 0.02
    dots_cm = [0.0]
    for n in range(1, 6):
        y_m = 0.5 * g_exp * ((n * dt) ** 2)
        dots_cm.append(round(y_m * 100.0, 2))

    tape_len = dots_cm[-1] + 2.0
    svg_str = _svg_ticker_tape(dots_cm, tape_len)

    dy3 = round(dots_cm[3] - dots_cm[2], 2)
    dy4 = round(dots_cm[4] - dots_cm[3], 2)
    v2 = round((dy3 / 100.0) / dt, 2)
    v3 = round((dy4 / 100.0) / dt, 2)

    prompt = (
        "Refer to the accompanying ticker-tape diagram obtained from an experiment investigating free fall under gravity.\n\n"
        "A ticker timer operating at a frequency of $50\\text{{ Hz}}$ produced dots on a tape attached to a falling mass. "
        f"The recorded cumulative positions from the start are:\n"
        f"- $D_0 = 0\\text{{ cm}}$, $D_1 = {_fmt_sa(dots_cm[1])}\\text{{ cm}}$, $D_2 = {_fmt_sa(dots_cm[2])}\\text{{ cm}}$, "
        f"$D_3 = {_fmt_sa(dots_cm[3])}\\text{{ cm}}$, $D_4 = {_fmt_sa(dots_cm[4])}\\text{{ cm}}$, $D_5 = {_fmt_sa(dots_cm[5])}\\text{{ cm}}$.\n\n"
        "1. Calculate the time interval $\\Delta t$ between two consecutive dots.\n"
        "2. Calculate the average velocity during interval $D_2 \\to D_3$ and interval $D_3 \\to D_4$.\n"
        "3. Using these velocities, calculate the experimental acceleration due to gravity $g_{{\\text{{exp}}}}$."
    )
    ans = f"$\\Delta t = 0{{,}}02\\text{{ s}}$, $g_{{\\text{{exp}}}} = {_fmt_sa(g_exp)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$"
    steps = [
        {"rule": "Calculate period between consecutive timer dots", "op": "T = \\frac{1}{f} = \\frac{1}{50}", "to": "0{,}02\\text{ s}"},
        {"rule": "Calculate interval velocities", "op": f"v_2 = \\frac{{{_fmt_sa(dy3)} \\times 10^{{-2}}}}{{0{{,}}02}} = {_fmt_sa(v2)},\\; v_3 = \\frac{{{_fmt_sa(dy4)} \\times 10^{{-2}}}}{{0{{,}}02}} = {_fmt_sa(v3)}", "to": f"v_2 = {_fmt_sa(v2)}\\text{{ m/s}},\\; v_3 = {_fmt_sa(v3)}\\text{{ m/s}}"},
        {"rule": "Calculate experimental gravitational acceleration", "op": f"g_{{\\text{{exp}}}} = \\frac{{v_3 - v_2}}{{\\Delta t}} = \\frac{{{_fmt_sa(v3)} - {_fmt_sa(v2)}}}{{0{{,}}02}}", "to": f"{_fmt_sa(g_exp)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}"},
    ]
    d_spec = {"kind": "inline_svg", "svg": svg_str, "diagram_role": "context", "title": "Ticker-Tape Experimental Data"}
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="A 50 Hz ticker timer makes one dot every Δt = 1/50 = 0,02 s.",
        t2="Velocity v = Δy / Δt, and acceleration a = Δv / Δt.",
        t3=f"Δt = 0,02 s, g_exp = {_fmt_sa(g_exp)} m/s^2.",
        misconceptions=["forgetting_to_convert_centimetres_to_metres_when_calculating_acceleration"],
        marks=6,
        diagram_spec=d_spec,
    )


def _build_47(rng: random.Random) -> Dict[str, Any]:
    sub = "47_experimental_data_photogate_dual_flag_timing"
    flag_w_cm = rng.choice([2.0, 3.0, 4.0, 5.0])
    flag_w_m = flag_w_cm / 100.0
    d_gates_m = rng.choice([0.40, 0.50, 0.60, 0.80])
    g_exp = rng.choice([9.65, 9.72, 9.80, 9.88])

    # Initial drop height above gate 1
    h1 = 0.25
    v1 = round(math.sqrt(2 * g_exp * h1), 3)
    v2 = round(math.sqrt((v1 ** 2) + 2 * g_exp * d_gates_m), 3)
    dt1 = round(flag_w_m / v1, 4)
    dt2 = round(flag_w_m / v2, 4)

    prompt = (
        f"In an experiment to determine the acceleration due to gravity, a cylinder of card with an opaque flag of width ${_fmt_sa(flag_w_cm)}\\text{{ cm}}$ "
        f"is dropped vertically through two photogates connected to a digital timer. "
        f"The vertical separation distance between the two photogates is $d = {_fmt_sa(d_gates_m)}\\text{{ m}}$.\n\n"
        f"The timer records the flag blocking duration at Photogate 1 as $\\Delta t_1 = {_fmt_sa(dt1, 4)}\\text{{ s}}$, "
        f"and at Photogate 2 as $\\Delta t_2 = {_fmt_sa(dt2, 4)}\\text{{ s}}$.\n\n"
        "1. Calculate the instantaneous speed of the cylinder as it passes Photogate 1 and Photogate 2.\n"
        "2. Using an appropriate equation of motion, calculate the experimental acceleration $g_{{\\text{{exp}}}}$."
    )
    ans = f"$v_1 = {_fmt_sa(v1)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, $v_2 = {_fmt_sa(v2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, $g_{{\\text{{exp}}}} = {_fmt_sa(g_exp)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$"
    steps = [
        {"rule": "Calculate instantaneous velocity through Photogate 1", "op": f"v_1 = \\frac{{w}}{{\\Delta t_1}} = \\frac{{{_fmt_sa(flag_w_m)}}}{{{_fmt_sa(dt1, 4)}}}", "to": f"{_fmt_sa(v1)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Calculate instantaneous velocity through Photogate 2", "op": f"v_2 = \\frac{{w}}{{\\Delta t_2}} = \\frac{{{_fmt_sa(flag_w_m)}}}{{{_fmt_sa(dt2, 4)}}}", "to": f"{_fmt_sa(v2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Calculate experimental acceleration using third equation of motion", "op": f"v_2^2 = v_1^2 + 2g d \\implies g = \\frac{{({_fmt_sa(v2)})^2 - ({_fmt_sa(v1)})^2}}{{2({_fmt_sa(d_gates_m)})}}", "to": f"{_fmt_sa(g_exp)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The photogate flag width divided by the beam interruption time gives the instantaneous speed at that gate: v = w / Δt.",
        t2=f"Then use v2^2 = v1^2 + 2 g d to solve for g.",
        t3=f"v1 = {_fmt_sa(v1)} m/s, v2 = {_fmt_sa(v2)} m/s, g_exp = {_fmt_sa(g_exp)} m/s^2.",
        misconceptions=["dividing_the_gate_separation_distance_by_the_gate_shutter_time"],
        marks=5,
    )


def _build_48(rng: random.Random) -> Dict[str, Any]:
    sub = "48_skills_for_science_percentage_error_and_uncertainty"
    g_exp = rng.choice([9.45, 9.55, 9.60, 10.05, 10.15])
    g_accepted = 9.8
    diff = round(abs(g_exp - g_accepted), 2)
    pct_err = round((diff / g_accepted) * 100.0, 2)

    prompt = (
        f"A group of learners conduct a free-fall experiment using a data logger and obtain an experimental value of "
        f"$g_{{\\text{{exp}}}} = {_fmt_sa(g_exp)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$. "
        f"The accepted theoretical value for the acceleration due to gravity is $g_{{\\text{{accepted}}}} = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$.\n\n"
        "1. Calculate the percentage error in their experimental result.\n"
        "2. State one systematic error and one random error that could arise in such a free-fall laboratory setup."
    )
    ans = f"Percentage error $= {_fmt_sa(pct_err)}\\%$; Systematic: uncalibrated timer/air resistance; Random: parallax reading error/human reaction time"
    steps = [
        {"rule": "Calculate experimental percentage error", "op": f"\\%_{{\\text{{error}}}} = \\frac{{|g_{{\\text{{exp}}}} - g_{{\\text{{accepted}}}}|}}{{g_{{\\text{{accepted}}}}}} \\times 100\\% = \\frac{{|{_fmt_sa(g_exp)} - 9{{,}}8|}}{{9{{,}}8}} \\times 100\\%", "to": f"{_fmt_sa(pct_err)}\\%"},
        {"rule": "Identify experimental error categories", "op": "\\text{{Systematic vs Random}}", "to": "\\text{{Systematic: air resistance / calibration; Random: parallax}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Percentage error = (|Experimental - Theoretical| / Theoretical) * 100%.",
        t2="Systematic errors shift all readings in one direction (e.g. air drag reducing measured g). Random errors produce scatter (e.g. parallax).",
        t3=f"Percentage error = {_fmt_sa(pct_err)}%.",
        misconceptions=["dividing_by_the_experimental_value_instead_of_the_accepted_value"],
        marks=4,
    )


def _build_49(rng: random.Random) -> Dict[str, Any]:
    sub = "49_skills_for_science_independent_dependent_controlled_variables"
    h_drop = rng.choice([2.0, 3.0, 4.0])
    prompt = (
        "A learner designs an investigation to test the following hypothesis:\n"
        f"*\"The acceleration of a freely falling sphere increases as its mass increases when dropped from a fixed height of {_fmt_sa(h_drop)}\\text{{ m}}.\"*\n\n"
        "The learner drops three solid spheres of identical diameter and polished surface finish, but made of different materials "
        "(wood: $0{{,}}1\\text{{ kg}}$, aluminium: $0{{,}}3\\text{{ kg}}$, lead: $1{{,}}2\\text{{ kg}}$), using an electromagnetic release mechanism.\n\n"
        "1. Identify the independent variable in this investigation.\n"
        "2. Identify the dependent variable.\n"
        "3. Name two controlled variables that must be kept constant to ensure a fair test.\n"
        "4. Based on the laws of physics, state whether the learner's hypothesis will be supported or rejected."
    )
    ans = "Independent: Mass of sphere; Dependent: Acceleration / time of fall; Controlled: Drop height, sphere diameter/shape; Hypothesis is REJECTED"
    steps = [
        {"rule": "Identify independent variable (the factor deliberately altered)", "op": "\\text{{Manipulated factor}}", "to": "\\text{{Mass of the sphere}}"},
        {"rule": "Identify dependent variable (the observed response)", "op": "\\text{{Measured outcome}}", "to": "\\text{{Acceleration due to gravity / time of fall}}"},
        {"rule": "Identify controlled variables ensuring valid comparison", "op": "\\text{{Fixed conditions}}", "to": "\\text{{Height of release, sphere diameter/aerodynamic shape}}"},
        {"rule": "Formulate conclusion based on gravitational free fall theory", "op": "a = \\frac{F_g}{m} = \\frac{mg}{m} = g", "to": "\\text{{Rejected: gravitational acceleration is independent of mass}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="The independent variable is what the investigator changes (mass). The dependent variable is what is measured (acceleration/time).",
        t2="Since F_net = F_g = mg, a = F_net / m = mg / m = g. All masses fall with identical acceleration in free fall.",
        t3="Independent: Mass. Dependent: Acceleration. Hypothesis rejected.",
        misconceptions=["believing_heavier_objects_fall_faster_in_the_absence_of_air_resistance"],
        marks=5,
    )


def _build_50(rng: random.Random) -> Dict[str, Any]:
    sub = "50_vertical_projectile_diagnostic_synthesis"
    vb = rng.choice([4.0, 5.0, 6.0])
    h0 = rng.choice([50.0, 60.0, 75.0])
    e_ret = rng.choice([0.75, 0.80])

    # Stage 1: stone dropped from ascending balloon
    # Initial upward velocity = vb
    # Flight to ground: 4.9 t^2 - vb t - h0 = 0
    disc = (vb ** 2) + 4 * 4.9 * h0
    t_flight1 = round((vb + math.sqrt(disc)) / 9.8, 2)
    v_strike = round(math.sqrt((vb ** 2) + 2 * G * h0), 2)
    # Stage 2: bounce
    v_reb = round(v_strike * e_ret, 2)
    h_reb = round((v_reb ** 2) / (2 * G), 2)
    t_reb_apex = round(v_reb / G, 2)
    t_total_apex = round(t_flight1 + t_reb_apex, 2)

    prompt = (
        "**Comprehensive Diagnostic Synthesis: Vertical Projectile Motion & Energy**\n\n"
        f"A hot-air balloon is rising vertically at a constant velocity of ${_fmt_sa(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"When the balloon is ${_fmt_sa(h0)}\\text{{ m}}$ above the ground, a steel sphere of mass $0{{,}}25\\text{{ kg}}$ is released.\n"
        f"Upon hitting the ground, the sphere bounces and rebounds with ${_fmt_sa(round(e_ret * 100, 1))}\\%$ of its impact speed. "
        "Ignore air resistance and take upwards as the positive direction.\n\n"
        "1. Write down the initial velocity of the sphere at the moment of release from the balloon.\n"
        "2. Calculate the time elapsed from the instant of release until the sphere strikes the ground.\n"
        "3. Calculate the speed with which the sphere strikes the ground.\n"
        "4. Calculate the maximum height reached by the sphere on its first rebound.\n"
        "5. Calculate the total time elapsed from initial release until the sphere reaches its rebound apex."
    )
    ans = (
        f"$v_i = +{_fmt_sa(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, $t_1 = {_fmt_sa(t_flight1)}\\text{{ s}}$, "
        f"$v_{{\\text{{strike}}}} = {_fmt_sa(v_strike)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, "
        f"$H_{{\\text{{reb}}}} = {_fmt_sa(h_reb)}\\text{{ m}}$, $t_{{\\text{{total}}}} = {_fmt_sa(t_total_apex)}\\text{{ s}}$"
    )
    steps = [
        {"rule": "Identify upward velocity inherited from balloon", "op": "v_i = +v_{{\\text{{balloon}}}}", "to": f"+{_fmt_sa(vb)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Calculate flight time to ground", "op": f"-{_fmt_sa(h0)} = ({_fmt_sa(vb)})t - 4{{,}}9 t^2", "to": f"t_1 = {_fmt_sa(t_flight1)}\\text{{ s}}"},
        {"rule": "Calculate impact velocity", "op": f"v_f^2 = ({_fmt_sa(vb)})^2 + 2(-9{{,}}8)(-{_fmt_sa(h0)})", "to": f"{_fmt_sa(v_strike)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}"},
        {"rule": "Calculate rebound velocity and maximum rebound height", "op": f"v_{{\\text{{reb}}}} = {_fmt_sa(e_ret)} \\times {_fmt_sa(v_strike)} = {_fmt_sa(v_reb)} \\implies H_{{\\text{{reb}}}} = \\frac{{{_fmt_sa(v_reb)}^2}}{{19{{,}}6}}", "to": f"{_fmt_sa(h_reb)}\\text{{ m}}"},
        {"rule": "Calculate total elapsed time to rebound apex", "op": f"t_{{\\text{{total}}}} = t_1 + \\frac{{{_fmt_sa(v_reb)}}}{{9{{,}}8}} = {_fmt_sa(t_flight1)} + {_fmt_sa(t_reb_apex)}", "to": f"{_fmt_sa(t_total_apex)}\\text{{ s}}"},
    ]
    return _base_contract(
        subskill=sub,
        prompt=prompt,
        answer=ans,
        options=None,
        sol_steps=steps,
        t1="Break the multi-stage scenario into distinct phases: (1) free fall from balloon, (2) inelastic ground collision, and (3) upward rebound flight.",
        t2=f"v_i = +{_fmt_sa(vb)} m/s, strike speed = {_fmt_sa(v_strike)} m/s, rebound speed = {_fmt_sa(v_reb)} m/s.",
        t3=f"t1 = {_fmt_sa(t_flight1)} s, strike speed = {_fmt_sa(v_strike)} m/s, H_reb = {_fmt_sa(h_reb)} m, total time = {_fmt_sa(t_total_apex)} s.",
        misconceptions=["ignoring_inherited_velocity_from_balloon", "forgetting_to_add_the_flight_phases_for_total_time"],
        marks=8,
    )


# =========================================================================== #
# Export Mapping
# =========================================================================== #

BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_bouncing_ball_rebound_velocity_and_speed_loss": _build_26,
    "27_bouncing_ball_second_bounce_apex_height": _build_27,
    "28_bouncing_ball_contact_time_average_net_force": _build_28,
    "29_hot_air_balloon_ascending_dropped_object": _build_29,
    "30_hot_air_balloon_descending_dropped_object": _build_30,
    "31_hot_air_balloon_projected_upwards_relative_to_balloon": _build_31,
    "32_simultaneous_release_one_dropped_one_projected_up": _build_32,
    "33_simultaneous_release_two_projected_opposite_directions": _build_33,
    "34_delayed_release_catchup_problem": _build_34,
    "35_velocity_time_graph_upward_projection_from_ground": _build_35,
    "36_velocity_time_graph_cliff_launch_to_ground": _build_36,
    "37_velocity_time_graph_bouncing_ball_single_bounce": _build_37,
    "38_velocity_time_graph_bouncing_ball_multiple_bounces": _build_38,
    "39_position_time_graph_upward_projection_parabola": _build_39,
    "40_position_time_graph_cliff_launch_crossing_zero": _build_40,
    "41_position_time_graph_bouncing_ball_parabolic_arcs": _build_41,
    "42_acceleration_time_graph_projectile_free_fall": _build_42,
    "43_acceleration_time_graph_bouncing_ball_impact_spike": _build_43,
    "44_graph_conversion_position_time_to_velocity_time": _build_44,
    "45_graph_conversion_velocity_time_to_position_time": _build_45,
    "46_experimental_data_ticker_timer_free_fall": _build_46,
    "47_experimental_data_photogate_dual_flag_timing": _build_47,
    "48_skills_for_science_percentage_error_and_uncertainty": _build_48,
    "49_skills_for_science_independent_dependent_controlled_variables": _build_49,
    "50_vertical_projectile_diagnostic_synthesis": _build_50,
}

SUBSKILLS_26_50: List[str] = list(BUILDERS_26_50.keys())
