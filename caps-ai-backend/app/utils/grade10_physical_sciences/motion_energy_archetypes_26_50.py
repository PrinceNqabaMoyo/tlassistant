"""Grade 10 Physical Sciences — 1D Motion & Mechanical Energy (Archetypes 26–50).
Deterministic 6-pillar question generators covering Paper 1 (Physics Term 3):
- Subskills 26–28: Graph conversions (v-t to a-t) and ticker-timer tape analysis.
- Subskills 29–31: 1D vertical motion under gravity (free fall, thrown downwards, projected upwards).
- Subskills 32–36: Gravitational potential energy (Ep = mgh) and kinetic energy (Ek = 0.5 mv^2).
- Subskills 37–43: Mechanical energy and Law of Conservation of Mechanical Energy across physical systems
  (free fall, projectiles, inclined slopes, roller coasters, pendulums, intermediate heights).
- Subskills 44–48: Non-conservative systems (friction loss), work by gravity, work-energy theorem, power, efficiency.
- Subskills 49–50: Multi-stage kinematics & energy synthesis, and diagnostic autopsy / misconception repair.

All questions adhere strictly to the 6-pillar contract and South African National Curriculum Standards.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

G_VAL = 9.8


def _fmt(val: float | int, places: int = 2) -> str:
    """Format number with South African comma decimal."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _fmt_tex(val: float | int, places: int = 2) -> str:
    """Format number with South African LaTeX comma separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _make_q(
    r: random.Random,
    subskill: str,
    num: int,
    prompt: str,
    correct_ans: str,
    worked_sol: str,
    marks: int,
    misconceptions: List[str],
    rubric: List[Dict[str, Any]],
    hints: Dict[str, str],
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q_id = f"g10_ps_motion_{num:02d}_{r.randint(10000, 99999)}"
    q: Dict[str, Any] = {
        "id": q_id,
        "type": "compound",
        "subskill": subskill,
        "prompt": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": worked_sol,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": rubric,
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "misconception_tags": misconceptions,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


# ============================================================================ #
# 26. Converting velocity-time to acceleration-time graph
# ============================================================================ #
def build_26_converting_velocity_time_to_acceleration_time_graph(r: random.Random) -> Dict[str, Any]:
    a1 = r.choice([2.0, 2.5, 3.0])
    t1 = r.choice([3, 4])
    t2 = t1 + r.choice([3, 4])
    v_top = round(a1 * t1, 1)

    svg = f"""<svg viewBox="0 0 500 240" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#F8FAFC" />
  <line x1="60" y1="200" x2="460" y2="200" stroke="#0F172A" stroke-width="2" />
  <line x1="60" y1="200" x2="60" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="460" y="225" font-size="12" fill="#0F172A" text-anchor="end">Time t (s)</text>
  <text x="45" y="35" font-size="12" fill="#0F172A" text-anchor="middle">v (m/s)</text>
  <line x1="60" y1="200" x2="{60 + t1 * 35}" y2="{200 - int(v_top * 8)}" stroke="#2563EB" stroke-width="3" />
  <line x1="{60 + t1 * 35}" y1="{200 - int(v_top * 8)}" x2="{60 + t2 * 35}" y2="{200 - int(v_top * 8)}" stroke="#2563EB" stroke-width="3" />
  <text x="{60 + t1 * 35}" y="218" font-size="11" fill="#475569" text-anchor="middle">{t1}</text>
  <text x="{60 + t2 * 35}" y="218" font-size="11" fill="#475569" text-anchor="middle">{t2}</text>
  <text x="45" y="{205 - int(v_top * 8)}" font-size="11" fill="#475569" text-anchor="end">{_fmt(v_top)}</text>
</svg>"""

    prompt = (
        f"Refer to the velocity-time graph shown in the figure for a moving vehicle.\n\n"
        f"1. Calculate the acceleration of the vehicle during the first interval ($0$ to ${t1}\\text{{ s}}$).\n"
        f"2. Calculate the acceleration of the vehicle during the second interval (${t1}\\text{{ s}}$ to ${t2}\\text{{ s}}$).\n"
        f"3. Describe the appearance of the corresponding acceleration-time ($a-t$) graph across both intervals."
    )
    ans = f"a1 = {_fmt_tex(a1)} m*s^-2; a2 = 0 m*s^-2"
    sol = (
        f"1. Interval $0$ to ${t1}\\text{{ s}}$:\n"
        f"   $a_1 = \\frac{{\\Delta v}}{{\\Delta t}} = \\frac{{{_fmt_tex(v_top)} - 0}}{{{t1} - 0}} = {_fmt_tex(a1)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$.\n"
        f"2. Interval ${t1}\\text{{ s}}$ to ${t2}\\text{{ s}}$:\n"
        f"   $a_2 = \\frac{{\\Delta v}}{{\\Delta t}} = \\frac{{{_fmt_tex(v_top)} - {_fmt_tex(v_top)}}}{{{t2} - {t1}}} = 0\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$.\n"
        f"3. On an $a-t$ graph, the motion is represented by a horizontal line segment at $a = {_fmt_tex(a1)}\\text{{ m/s}}^2$ "
        f"from $t = 0$ to $t = {t1}\\text{{ s}}$, followed by a step change down to a horizontal line along the time axis ($a = 0$) "
        f"from $t = {t1}\\text{{ s}}$ to $t = {t2}\\text{{ s}}$."
    )
    rubric = [
        {"step": 1, "criterion": f"Calculated a1 = {_fmt_tex(a1)} m*s^-2", "marks": 1},
        {"step": 2, "criterion": "Calculated a2 = 0 m*s^-2", "marks": 1},
        {"step": 3, "criterion": "Described horizontal line segments at a1 and 0", "marks": 2},
    ]
    hints = {
        "tier_1": "Acceleration is the gradient of the velocity-time graph.",
        "tier_2": f"Slope of segment 1 is {v_top}/{t1} = {_fmt(a1)}. Slope of segment 2 is 0.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "26_converting_velocity_time_to_acceleration_time_graph", 26, prompt, ans, sol, 4, ["confused_velocity_with_acceleration_on_graph"], rubric, hints, spec)


# ============================================================================ #
# 27. Ticker timer tape analysis: constant velocity
# ============================================================================ #
def build_27_ticker_timer_tape_analysis_constant_velocity(r: random.Random) -> Dict[str, Any]:
    f_hz = 50
    period = 1.0 / f_hz  # 0.02 s
    num_spaces = r.choice([4, 5, 6])
    t_interval = round(num_spaces * period, 2)
    dist_cm = r.choice([8.0, 10.0, 12.0, 15.0])
    dist_m = round(dist_cm / 100.0, 3)
    v_ms = round(dist_m / t_interval, 2)

    svg = f"""<svg viewBox="0 0 500 120" width="100%" height="100" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="120" fill="#F8FAFC" />
  <rect x="30" y="45" width="440" height="30" fill="#FEF08A" stroke="#CA8A04" stroke-width="1" />
  <circle cx="50" cy="60" r="3" fill="#0F172A" /><text x="50" y="90" font-size="11" fill="#475569" text-anchor="middle">Dot 0</text>
  <circle cx="120" cy="60" r="3" fill="#0F172A" />
  <circle cx="190" cy="60" r="3" fill="#0F172A" />
  <circle cx="260" cy="60" r="3" fill="#0F172A" />
  <circle cx="330" cy="60" r="3" fill="#0F172A" />
  <circle cx="400" cy="60" r="3" fill="#0F172A" /><text x="400" y="90" font-size="11" fill="#475569" text-anchor="middle">Dot {num_spaces}</text>
  <line x1="50" y1="35" x2="400" y2="35" stroke="#2563EB" stroke-width="1.5" marker-start="url(#dot)" marker-end="url(#dot)" />
  <text x="225" y="30" font-size="12" fill="#2563EB" text-anchor="middle">{_fmt(dist_cm)} cm ({num_spaces} spaces)</text>
</svg>"""

    prompt = (
        f"Refer to the ticker-timer tape shown in the figure, produced by a trolley moving at constant velocity. "
        f"The ticker-timer operates at a standard frequency of ${f_hz}\\text{{ Hz}}$. "
        f"The distance across ${num_spaces}$ dot spaces measures ${_fmt_tex(dist_cm)}\\text{{ cm}}$.\n\n"
        f"1. Calculate the period ($T$) of the ticker-timer (time between two consecutive dots).\n"
        f"2. Calculate the time interval ($\\Delta t$) represented by the ${num_spaces}$ dot spaces.\n"
        f"3. Calculate the average velocity of the trolley in metres per second ($\\text{{m}}\\cdot\\text{{s}}^{{-1}}$)."
    )
    ans = f"T = 0,02 s; dt = {_fmt_tex(t_interval)} s; v = {_fmt_tex(v_ms)} m*s^-1"
    sol = (
        f"1. $T = \\frac{{1}}{{f}} = \\frac{{1}}{{{f_hz}}} = 0{{,}}02\\text{{ s}}$.\n"
        f"2. $\\Delta t = {num_spaces} \\times T = {num_spaces} \\times 0{{,}}02 = {_fmt_tex(t_interval)}\\text{{ s}}$.\n"
        f"3. Distance in metres: $\\Delta x = \\frac{{{_fmt_tex(dist_cm)}}}{{100}} = {_fmt_tex(dist_m)}\\text{{ m}}$.\n"
        f"   $v = \\frac{{\\Delta x}}{{\\Delta t}} = \\frac{{{_fmt_tex(dist_m)}}}{{{_fmt_tex(t_interval)}}} = {_fmt_tex(v_ms)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula and calculation for period T = 0,02 s", "marks": 1},
        {"step": 2, "criterion": f"Time interval dt = {_fmt_tex(t_interval)} s", "marks": 1},
        {"step": 3, "criterion": "Conversion of distance cm to m", "marks": 1},
        {"step": 4, "criterion": f"Calculated velocity = {_fmt_tex(v_ms)} m*s^-1", "marks": 1},
    ]
    hints = {
        "tier_1": "Period T = 1/f = 1/50 = 0.02s per dot space. Convert cm to metres.",
        "tier_2": f"Time = {num_spaces} * 0.02 = {_fmt(t_interval)}s. Distance = {_fmt(dist_m)}m.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "27_ticker_timer_tape_analysis_constant_velocity", 27, prompt, ans, sol, 4, ["counted_dots_instead_of_spaces"], rubric, hints, spec)


# ============================================================================ #
# 28. Ticker timer tape analysis: acceleration
# ============================================================================ #
def build_28_ticker_timer_tape_analysis_acceleration(r: random.Random) -> Dict[str, Any]:
    f_hz = 50
    t_dot = 1.0 / f_hz  # 0.02 s
    n_dot = 4  # 4-dot interval
    dt = n_dot * t_dot  # 0.08 s

    dx1_cm = r.choice([3.2, 4.0, 4.8])
    dx2_cm = dx1_cm + r.choice([2.4, 3.2, 4.0])

    dx1_m = round(dx1_cm / 100.0, 4)
    dx2_m = round(dx2_cm / 100.0, 4)

    v1 = round(dx1_m / dt, 3)
    v2 = round(dx2_m / dt, 3)
    a = round((v2 - v1) / dt, 2)

    prompt = (
        f"A ticker timer operating at ${f_hz}\\text{{ Hz}}$ produces dots on a tape attached to an accelerating trolley. "
        f"Two consecutive intervals of ${n_dot}$ dot spaces each are measured:\n"
        f"- First interval: $\\Delta x_1 = {_fmt_tex(dx1_cm)}\\text{{ cm}}$\n"
        f"- Second interval: $\\Delta x_2 = {_fmt_tex(dx2_cm)}\\text{{ cm}}$\n\n"
        f"1. Calculate the time interval ($\\Delta t$) for ${n_dot}$ dot spaces.\n"
        f"2. Calculate the average velocity ($v_1$) during the first interval.\n"
        f"3. Calculate the average velocity ($v_2$) during the second interval.\n"
        f"4. Calculate the acceleration ($a$) of the trolley."
    )
    ans = f"a = {_fmt_tex(a)} m*s^-2"
    sol = (
        f"1. $\\Delta t = {n_dot} \\times \\frac{{1}}{{{f_hz}}} = {n_dot} \\times 0{{,}}02 = {_fmt_tex(dt)}\\text{{ s}}$.\n"
        f"2. $v_1 = \\frac{{\\Delta x_1}}{{\\Delta t}} = \\frac{{{_fmt_tex(dx1_m)}}}{{{_fmt_tex(dt)}}} = {_fmt_tex(v1)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"3. $v_2 = \\frac{{\\Delta x_2}}{{\\Delta t}} = \\frac{{{_fmt_tex(dx2_m)}}}{{{_fmt_tex(dt)}}} = {_fmt_tex(v2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"4. $a = \\frac{{v_2 - v_1}}{{\\Delta t}} = \\frac{{{_fmt_tex(v2)} - {_fmt_tex(v1)}}}{{{_fmt_tex(dt)}}} = "
        f"\\frac{{{_fmt_tex(round(v2 - v1, 3))}}}{{{_fmt_tex(dt)}}} = {_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$."
    )
    rubric = [
        {"step": 1, "criterion": f"Calculated interval time dt = {_fmt_tex(dt)} s", "marks": 1},
        {"step": 2, "criterion": f"Calculated v1 = {_fmt_tex(v1)} m/s", "marks": 1},
        {"step": 3, "criterion": f"Calculated v2 = {_fmt_tex(v2)} m/s", "marks": 1},
        {"step": 4, "criterion": f"Calculated acceleration a = {_fmt_tex(a)} m*s^-2", "marks": 2},
    ]
    hints = {
        "tier_1": "Find velocities v1 and v2 for each interval, then use a = (v2 - v1) / dt.",
        "tier_2": f"dt = {n_dot} * 0.02s = {_fmt(dt)}s. v1 = {_fmt(dx1_m)}/{_fmt(dt)}; v2 = {_fmt(dx2_m)}/{_fmt(dt)}.",
        "tier_3": ans,
    }
    return _make_q(r, "28_ticker_timer_tape_analysis_acceleration", 28, prompt, ans, sol, 5, ["divided_by_total_time_instead_of_interval_time"], rubric, hints)


# ============================================================================ #
# 29. Vertical motion: free fall dropped from rest
# ============================================================================ #
def build_29_vertical_motion_free_fall_dropped_from_rest(r: random.Random) -> Dict[str, Any]:
    t = r.choice([2.0, 3.0, 4.0, 5.0])
    # vi = 0, a = 9.8 downwards
    vf = round(G_VAL * t, 2)
    dy = round(0.5 * G_VAL * (t**2), 2)

    prompt = (
        f"A small lead sphere is dropped from rest from the top of a tall observation tower. "
        f"Ignore air resistance and take $g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ downwards.\n\n"
        f"1. Define the term *free fall*.\n"
        f"2. Calculate the velocity of the sphere after falling for ${_fmt_tex(t)}\\text{{ s}}$.\n"
        f"3. Calculate the vertical distance fallen by the sphere during these ${_fmt_tex(t)}\\text{{ s}}$."
    )
    ans = f"vf = {_fmt_tex(vf)} m*s^-1 downwards, dy = {_fmt_tex(dy)} m"
    sol = (
        f"1. **Free fall** is motion during which the only force acting upon an object is the gravitational force.\n"
        f"2. Taking downwards as positive: $v_i = 0$, $a = 9{{,}}8\\text{{ m/s}}^2$.\n"
        f"   $v_f = v_i + a \\Delta t = 0 + (9{{,}}8)({_fmt_tex(t)}) = {_fmt_tex(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ downwards.\n"
        f"3. $\\Delta y = v_i \\Delta t + \\frac{{1}}{{2}} a (\\Delta t)^2 = 0 + \\frac{{1}}{{2}}(9{{,}}8)({_fmt_tex(t)})^2 = "
        f"(4{{,}}9)({round(t**2, 2)}) = {_fmt_tex(dy)}\\text{{ m}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of free fall", "marks": 1},
        {"step": 2, "criterion": f"Calculated vf = {_fmt_tex(vf)} m*s^-1 downwards", "marks": 2},
        {"step": 3, "criterion": f"Calculated vertical distance dy = {_fmt_tex(dy)} m", "marks": 2},
    ]
    hints = {
        "tier_1": "Dropped from rest means vi = 0. Use g = 9.8 m/s^2.",
        "tier_2": f"vf = 9.8 * {t}. dy = 0.5 * 9.8 * {t}^2.",
        "tier_3": ans,
    }
    return _make_q(r, "29_vertical_motion_free_fall_dropped_from_rest", 29, prompt, ans, sol, 5, ["confused_mass_with_falling_acceleration"], rubric, hints)


# ============================================================================ #
# 30. Vertical motion: projected downwards from height
# ============================================================================ #
def build_30_vertical_motion_projected_downwards_from_height(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([4.0, 5.0, 8.0, 10.0])
    h = r.choice([20.0, 30.0, 45.0])
    # vf^2 = vi^2 + 2*g*h
    vf_sq = vi**2 + 2 * G_VAL * h
    vf = round(math.sqrt(vf_sq), 2)

    prompt = (
        f"A ball is thrown vertically downwards from the edge of a cliff of height ${_fmt_tex(h)}\\text{{ m}}$ "
        f"with an initial velocity of ${_fmt_tex(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. "
        f"Air resistance is negligible ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ downwards).\n\n"
        f"Calculate the speed ($v_f$) with which the ball strikes the ground at the bottom of the cliff."
    )
    ans = f"{_fmt_tex(vf)} m*s^-1"
    sol = (
        f"Taking downwards as positive: $v_i = +{_fmt_tex(vi)}\\text{{ m/s}}$, $a = +9{{,}}8\\text{{ m/s}}^2$, $\\Delta y = +{_fmt_tex(h)}\\text{{ m}}$.\n"
        f"$v_f^2 = v_i^2 + 2 a \\Delta y$\n"
        f"$v_f^2 = ({_fmt_tex(vi)})^2 + 2(9{{,}}8)({_fmt_tex(h)})$\n"
        f"$v_f^2 = {round(vi**2, 2)} + {round(2 * G_VAL * h, 2)} = {_fmt_tex(vf_sq)}\\text{{ m}}^2\\cdot\\text{{s}}^{{-2}}$\n"
        f"$v_f = \\sqrt{{{_fmt_tex(vf_sq)}}} = {_fmt_tex(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula vf^2 = vi^2 + 2*a*dy", "marks": 1},
        {"step": 2, "criterion": "Correct substitution of vi, g, h", "marks": 1},
        {"step": 3, "criterion": f"Answer vf = {_fmt_tex(vf)} m*s^-1", "marks": 1},
    ]
    hints = {
        "tier_1": "Use vf^2 = vi^2 + 2*g*dy when time is not given.",
        "tier_2": f"vf = sqrt({vi}^2 + 2 * 9.8 * {h}).",
        "tier_3": ans,
    }
    return _make_q(r, "30_vertical_motion_projected_downwards_from_height", 30, prompt, ans, sol, 3, ["assumed_vi_is_zero_when_thrown"], rubric, hints)


# ============================================================================ #
# 31. Vertical motion: projected upwards max height and time
# ============================================================================ #
def build_31_vertical_motion_projected_upwards_max_height_and_time(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([14.7, 19.6, 24.5, 29.4])
    # at top, vf = 0
    t_top = round(vi / G_VAL, 2)
    h_max = round((vi**2) / (2 * G_VAL), 2)

    prompt = (
        f"A tennis ball is projected vertically upwards from ground level with an initial velocity of "
        f"${_fmt_tex(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Ignore air resistance ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ downwards).\n\n"
        f"1. What is the velocity of the ball at its maximum height?\n"
        f"2. Calculate the time taken ($\\Delta t$) to reach the highest point.\n"
        f"3. Calculate the maximum height ($h_{{\\text{{max}}}}$) reached above the ground."
    )
    ans = f"vf = 0 m*s^-1; t = {_fmt_tex(t_top)} s; h_max = {_fmt_tex(h_max)} m"
    sol = (
        f"1. At maximum height, the instantaneous velocity is **$0\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$**.\n"
        f"2. Taking upwards as positive: $v_i = +{_fmt_tex(vi)}\\text{{ m/s}}$, $v_f = 0$, $a = -9{{,}}8\\text{{ m/s}}^2$.\n"
        f"   $v_f = v_i + a \\Delta t \\implies 0 = {_fmt_tex(vi)} - 9{{,}}8 \\Delta t$\n"
        f"   $\\Delta t = \\frac{{{_fmt_tex(vi)}}}{{9{{,}}8}} = {_fmt_tex(t_top)}\\text{{ s}}$.\n"
        f"3. $v_f^2 = v_i^2 + 2 a \\Delta y \\implies 0 = ({_fmt_tex(vi)})^2 + 2(-9{{,}}8) h_{{\\text{{max}}}}$\n"
        f"   $h_{{\\text{{max}}}} = \\frac{{({_fmt_tex(vi)})^2}}{{19{{,}}6}} = {_fmt_tex(h_max)}\\text{{ m}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Stated velocity at top is 0 m/s", "marks": 1},
        {"step": 2, "criterion": f"Calculated time to top = {_fmt_tex(t_top)} s", "marks": 2},
        {"step": 3, "criterion": f"Calculated max height = {_fmt_tex(h_max)} m", "marks": 2},
    ]
    hints = {
        "tier_1": "At the peak, vf = 0 m/s. Acceleration is -9.8 m/s^2 when choosing upwards as positive.",
        "tier_2": f"t = {vi} / 9.8 = {_fmt(t_top)}s; h = {vi}^2 / (2 * 9.8) = {_fmt(h_max)}m.",
        "tier_3": ans,
    }
    return _make_q(r, "31_vertical_motion_projected_upwards_max_height_and_time", 31, prompt, ans, sol, 5, ["used_positive_acceleration_while_rising"], rubric, hints)


# ============================================================================ #
# 32. Gravitational potential energy: direct calculation
# ============================================================================ #
def build_32_gravitational_potential_energy_direct_calculation(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([25, 40, 50, 80, 120])
    height = r.choice([3.0, 4.5, 6.0, 8.0, 12.0])
    ep = round(mass * G_VAL * height, 1)

    prompt = (
        f"A building crane lifts a pallet of bricks of mass ${mass}\\text{{ kg}}$ to a scaffolding platform at "
        f"a vertical height of ${_fmt_tex(height)}\\text{{ m}}$ above the ground ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"1. Define the term *gravitational potential energy*.\n"
        f"2. Calculate the gravitational potential energy ($E_p$) of the pallet of bricks relative to the ground."
    )
    ans = f"{_fmt_tex(ep)} J"
    sol = (
        f"1. **Gravitational potential energy** is the energy an object possesses due to its position relative to a reference level (usually the ground) within a gravitational field.\n"
        f"2. $E_p = m g h = ({mass})(9{{,}}8)({_fmt_tex(height)}) = {_fmt_tex(ep)}\\text{{ J}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of gravitational potential energy", "marks": 1},
        {"step": 2, "criterion": "Formula Ep = m*g*h", "marks": 1},
        {"step": 3, "criterion": f"Answer Ep = {_fmt_tex(ep)} J", "marks": 1},
    ]
    hints = {
        "tier_1": "Ep = m * g * h.",
        "tier_2": f"Ep = {mass} * 9.8 * {_fmt(height)}.",
        "tier_3": ans,
    }
    return _make_q(r, "32_gravitational_potential_energy_direct_calculation", 32, prompt, ans, sol, 3, ["forgot_gravity_constant_in_potential_energy"], rubric, hints)


# ============================================================================ #
# 33. Gravitational potential energy: solve for height or mass
# ============================================================================ #
def build_33_gravitational_potential_energy_solve_for_height_or_mass(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([15.0, 20.0, 30.0, 45.0])
    h = r.choice([4.0, 5.0, 6.0, 8.0])
    ep = round(mass * G_VAL * h, 1)

    prompt = (
        f"A water container of mass ${_fmt_tex(mass)}\\text{{ kg}}$ is positioned on top of a farm stand. "
        f"Its gravitational potential energy relative to the ground is ${_fmt_tex(ep)}\\text{{ J}}$ ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"Calculate the vertical height ($h$) of the stand above the ground."
    )
    ans = f"{_fmt_tex(h)} m"
    sol = (
        f"$E_p = m g h$\n"
        f"${_fmt_tex(ep)} = ({_fmt_tex(mass)})(9{{,}}8) h\n"
        f"${_fmt_tex(ep)} = {round(mass * G_VAL, 2)} h\n"
        f"$h = \\frac{{{_fmt_tex(ep)}}}{{{round(mass * G_VAL, 2)}}} = {_fmt_tex(h)}\\text{{ m}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula Ep = m*g*h", "marks": 1},
        {"step": 2, "criterion": f"Substitution: {_fmt_tex(ep)} = {_fmt_tex(mass)} * 9.8 * h", "marks": 1},
        {"step": 3, "criterion": f"Answer h = {_fmt_tex(h)} m", "marks": 1},
    ]
    hints = {
        "tier_1": "h = Ep / (m * g).",
        "tier_2": f"h = {_fmt(ep)} / ({_fmt(mass)} * 9.8).",
        "tier_3": ans,
    }
    return _make_q(r, "33_gravitational_potential_energy_solve_for_height_or_mass", 33, prompt, ans, sol, 3, ["inverted_formula_for_height"], rubric, hints)


# ============================================================================ #
# 34. Kinetic energy: direct calculation
# ============================================================================ #
def build_34_kinetic_energy_direct_calculation(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([800, 1000, 1200, 1500])
    v = r.choice([15.0, 20.0, 25.0])
    ek = round(0.5 * mass * (v**2), 1)

    prompt = (
        f"A small sedan of mass ${mass}\\text{{ kg}}$ travels along a straight road at a constant speed of "
        f"${_fmt_tex(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. Define the term *kinetic energy*.\n"
        f"2. Calculate the kinetic energy ($E_k$) of the car."
    )
    ans = f"{_fmt_tex(ek)} J"
    sol = (
        f"1. **Kinetic energy** is the energy that an object possesses as a result of its motion.\n"
        f"2. $E_k = \\frac{{1}}{{2}} m v^2 = \\frac{{1}}{{2}} ({mass}) ({_fmt_tex(v)})^2 = "
        f"({round(0.5 * mass)}) ({round(v**2, 1)}) = {_fmt_tex(ek)}\\text{{ J}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of kinetic energy", "marks": 1},
        {"step": 2, "criterion": "Formula Ek = 0.5 * m * v^2", "marks": 1},
        {"step": 3, "criterion": f"Answer Ek = {_fmt_tex(ek)} J", "marks": 1},
    ]
    hints = {
        "tier_1": "Ek = 0.5 * m * v^2. Remember to square the velocity.",
        "tier_2": f"Ek = 0.5 * {mass} * {_fmt(v)}^2 = 0.5 * {mass} * {v**2}.",
        "tier_3": ans,
    }
    return _make_q(r, "34_kinetic_energy_direct_calculation", 34, prompt, ans, sol, 3, ["forgot_squaring_velocity_in_ek"], rubric, hints)


# ============================================================================ #
# 35. Kinetic energy: solve for velocity
# ============================================================================ #
def build_35_kinetic_energy_solve_for_velocity(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([0.15, 0.20, 0.45, 0.50])  # hockey ball, soccer ball
    v = r.choice([16.0, 20.0, 24.0, 28.0])
    ek = round(0.5 * mass * (v**2), 2)

    prompt = (
        f"A sports ball of mass ${_fmt_tex(mass)}\\text{{ kg}}$ is kicked and possesses ${_fmt_tex(ek)}\\text{{ J}}$ "
        f"of kinetic energy.\n\n"
        f"Calculate the speed ($v$) of the ball."
    )
    ans = f"{_fmt_tex(v)} m*s^-1"
    sol = (
        f"$E_k = \\frac{{1}}{{2}} m v^2$\n"
        f"${_fmt_tex(ek)} = \\frac{{1}}{{2}} ({_fmt_tex(mass)}) v^2\n"
        f"${_fmt_tex(ek)} = {round(0.5 * mass, 4)} v^2\n"
        f"$v^2 = \\frac{{{_fmt_tex(ek)}}}{{{round(0.5 * mass, 4)}}} = {round(v**2, 1)}\\text{{ m}}^2\\cdot\\text{{s}}^{{-2}}\n"
        f"$v = \\sqrt{{{round(v**2, 1)}}} = {_fmt_tex(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula Ek = 0.5 * m * v^2", "marks": 1},
        {"step": 2, "criterion": f"Substitution: {_fmt_tex(ek)} = 0.5 * {_fmt_tex(mass)} * v^2", "marks": 1},
        {"step": 3, "criterion": f"Answer v = {_fmt_tex(v)} m*s^-1", "marks": 1},
    ]
    hints = {
        "tier_1": "v = sqrt(2 * Ek / m).",
        "tier_2": f"v^2 = 2 * {_fmt(ek)} / {_fmt(mass)} = {v**2}. Take the square root.",
        "tier_3": ans,
    }
    return _make_q(r, "35_kinetic_energy_solve_for_velocity", 35, prompt, ans, sol, 3, ["forgot_square_root_in_v_from_ek"], rubric, hints)


# ============================================================================ #
# 36. Kinetic energy: solve for mass
# ============================================================================ #
def build_36_kinetic_energy_solve_for_mass(r: random.Random) -> Dict[str, Any]:
    v = r.choice([12.0, 15.0, 18.0, 20.0])
    mass = r.choice([60.0, 75.0, 80.0, 90.0])  # sprinter
    ek = round(0.5 * mass * (v**2), 1)

    prompt = (
        f"An athlete sprints across the finish line with a velocity of ${_fmt_tex(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, "
        f"possessing ${_fmt_tex(ek)}\\text{{ J}}$ of kinetic energy.\n\n"
        f"Calculate the mass ($m$) of the athlete."
    )
    ans = f"{_fmt_tex(mass)} kg"
    sol = (
        f"$E_k = \\frac{{1}}{{2}} m v^2\n"
        f"${_fmt_tex(ek)} = \\frac{{1}}{{2}} m ({_fmt_tex(v)})^2\n"
        f"${_fmt_tex(ek)} = \\frac{{1}}{{2}} m ({round(v**2, 1)}) = {round(0.5 * (v**2), 2)} m\n"
        f"$m = \\frac{{{_fmt_tex(ek)}}}{{{round(0.5 * (v**2), 2)}}} = {_fmt_tex(mass)}\\text{{ kg}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula Ek = 0.5 * m * v^2", "marks": 1},
        {"step": 2, "criterion": f"Substitution: {_fmt_tex(ek)} = 0.5 * m * ({_fmt_tex(v)})^2", "marks": 1},
        {"step": 3, "criterion": f"Answer m = {_fmt_tex(mass)} kg", "marks": 1},
    ]
    hints = {
        "tier_1": "m = 2 * Ek / v^2.",
        "tier_2": f"m = 2 * {_fmt(ek)} / ({_fmt(v)})^2 = {_fmt(mass)} kg.",
        "tier_3": ans,
    }
    return _make_q(r, "36_kinetic_energy_solve_for_mass", 36, prompt, ans, sol, 3, ["forgot_factor_of_two_when_rearranging_for_mass"], rubric, hints)


# ============================================================================ #
# 37. Total mechanical energy: isolated system
# ============================================================================ #
def build_37_total_mechanical_energy_isolated_system(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([2.0, 3.0, 5.0, 10.0])
    h = r.choice([5.0, 8.0, 10.0, 15.0])
    v = r.choice([4.0, 6.0, 8.0])

    ep = round(mass * G_VAL * h, 1)
    ek = round(0.5 * mass * (v**2), 1)
    e_mech = round(ep + ek, 1)

    prompt = (
        f"A drone of mass ${_fmt_tex(mass)}\\text{{ kg}}$ flies horizontally at a speed of ${_fmt_tex(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"at an altitude of ${_fmt_tex(h)}\\text{{ m}}$ above the ground ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"1. Define the term *mechanical energy*.\n"
        f"2. Calculate the gravitational potential energy ($E_p$) of the drone.\n"
        f"3. Calculate the kinetic energy ($E_k$) of the drone.\n"
        f"4. Calculate the total mechanical energy ($E_{{\\text{{mech}}}}$) of the drone."
    )
    ans = f"Ep = {_fmt_tex(ep)} J, Ek = {_fmt_tex(ek)} J, Emech = {_fmt_tex(e_mech)} J"
    sol = (
        f"1. **Mechanical energy** is the sum of the gravitational potential energy and kinetic energy of an object ($E_{{\\text{{mech}}}} = E_k + E_p$).\n"
        f"2. $E_p = m g h = ({_fmt_tex(mass)})(9{{,}}8)({_fmt_tex(h)}) = {_fmt_tex(ep)}\\text{{ J}}$.\n"
        f"3. $E_k = \\frac{{1}}{{2}} m v^2 = \\frac{{1}}{{2}} ({_fmt_tex(mass)}) ({_fmt_tex(v)})^2 = {_fmt_tex(ek)}\\text{{ J}}$.\n"
        f"4. $E_{{\\text{{mech}}}} = E_p + E_k = {_fmt_tex(ep)} + {_fmt_tex(ek)} = {_fmt_tex(e_mech)}\\text{{ J}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of mechanical energy", "marks": 1},
        {"step": 2, "criterion": f"Calculated Ep = {_fmt_tex(ep)} J", "marks": 1},
        {"step": 3, "criterion": f"Calculated Ek = {_fmt_tex(ek)} J", "marks": 1},
        {"step": 4, "criterion": f"Calculated Emech = {_fmt_tex(e_mech)} J", "marks": 1},
    ]
    hints = {
        "tier_1": "Emech = Ep + Ek = mgh + 0.5*m*v^2.",
        "tier_2": f"Ep = {ep} J; Ek = {ek} J. Sum them up.",
        "tier_3": ans,
    }
    return _make_q(r, "37_total_mechanical_energy_isolated_system", 37, prompt, ans, sol, 4, ["confused_total_mechanical_energy_with_kinetic_energy"], rubric, hints)


# ============================================================================ #
# 38. Conservation of mechanical energy: free fall impact speed
# ============================================================================ #
def build_38_conservation_mechanical_energy_free_fall_impact_speed(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([2.5, 4.0, 6.0, 10.0])
    h = r.choice([15.0, 20.0, 25.0, 30.0])
    v_sq = 2 * G_VAL * h
    v_impact = round(math.sqrt(v_sq), 2)
    ep_top = round(mass * G_VAL * h, 1)

    prompt = (
        f"A boulder of mass ${_fmt_tex(mass)}\\text{{ kg}}$ dislodges and falls from rest from a cliff top of height "
        f"${_fmt_tex(h)}\\text{{ m}}$ above the ground. Assume air resistance is negligible ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"1. State the **Law of Conservation of Mechanical Energy**.\n"
        f"2. Use the principle of conservation of mechanical energy to calculate the speed ($v$) with which the boulder strikes the ground.\n"
        f"3. Explain why the boulder's impact speed does not depend on its mass."
    )
    ans = f"{_fmt_tex(v_impact)} m*s^-1"
    sol = (
        f"1. **Law of Conservation of Mechanical Energy:** In an isolated system (where only conservative forces do work), "
        f"the total mechanical energy remains constant ($E_{{\\text{{mech, initial}}}} = E_{{\\text{{mech, final}}}}$).\n"
        f"2. $(E_k + E_p)_{{\\text{{top}}}} = (E_k + E_p)_{{\\text{{bottom}}}}$\n"
        f"   $0 + m g h = \\frac{{1}}{{2}} m v^2 + 0$\n"
        f"   Dividing both sides by mass $m$:\n"
        f"   $g h = \\frac{{1}}{{2}} v^2 \\implies v^2 = 2 g h = 2(9{{,}}8)({_fmt_tex(h)}) = {_fmt_tex(round(v_sq, 2))}\\text{{ m}}^2\\cdot\\text{{s}}^{{-2}}$\n"
        f"   $v = \\sqrt{{{_fmt_tex(round(v_sq, 2))}}} = {_fmt_tex(v_impact)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"3. Mass $m$ cancels from both sides of the equation ($mgh = \\frac{{1}}{{2}}mv^2 \\implies v = \\sqrt{{2gh}}$), "
        f"so all freely falling objects in a vacuum accelerate at the same rate regardless of mass."
    )
    rubric = [
        {"step": 1, "criterion": "Statement of Law of Conservation of Mechanical Energy", "marks": 1},
        {"step": 2, "criterion": "Equated mechanical energies: (Ek + Ep)top = (Ek + Ep)bottom", "marks": 1},
        {"step": 3, "criterion": f"Calculated impact speed v = {_fmt_tex(v_impact)} m*s^-1", "marks": 2},
        {"step": 4, "criterion": "Explanation of mass cancellation (v = sqrt(2gh))", "marks": 1},
    ]
    hints = {
        "tier_1": "At top, Ep = mgh and Ek = 0. At bottom, Ep = 0 and Ek = 0.5*m*v^2.",
        "tier_2": f"v = sqrt(2 * g * h) = sqrt(2 * 9.8 * {h}).",
        "tier_3": ans,
    }
    return _make_q(r, "38_conservation_mechanical_energy_free_fall_impact_speed", 38, prompt, ans, sol, 5, ["thought_heavier_objects_fall_faster"], rubric, hints)


# ============================================================================ #
# 39. Conservation of mechanical energy: vertical projectile peak
# ============================================================================ #
def build_39_conservation_mechanical_energy_vertical_projectile_peak(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([0.2, 0.5, 1.0])
    v_launch = r.choice([14.0, 18.0, 21.0, 28.0])
    h_max = round((v_launch**2) / (2 * G_VAL), 2)
    ek_bottom = round(0.5 * mass * (v_launch**2), 1)

    prompt = (
        f"A rocket model of mass ${_fmt_tex(mass)}\\text{{ kg}}$ is launched vertically upwards from ground level at an initial "
        f"speed of ${_fmt_tex(v_launch)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$. Ignore air resistance ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"1. Calculate the initial kinetic energy ($E_k$) of the rocket at launch.\n"
        f"2. Use conservation of mechanical energy to calculate the maximum vertical height ($h_{{\\text{{max}}}}$) reached by the rocket."
    )
    ans = f"Ek = {_fmt_tex(ek_bottom)} J, h_max = {_fmt_tex(h_max)} m"
    sol = (
        f"1. $E_k = \\frac{{1}}{{2}} m v^2 = \\frac{{1}}{{2}} ({_fmt_tex(mass)}) ({_fmt_tex(v_launch)})^2 = {_fmt_tex(ek_bottom)}\\text{{ J}}$.\n"
        f"2. In the isolated system (no air friction):\n"
        f"   $(E_k + E_p)_{{\\text{{bottom}}}} = (E_k + E_p)_{{\\text{{top}}}}$\n"
        f"   ${_fmt_tex(ek_bottom)} + 0 = 0 + m g h_{{\\text{{max}}}}$\n"
        f"   ${_fmt_tex(ek_bottom)} = ({_fmt_tex(mass)})(9{{,}}8) h_{{\\text{{max}}}}$\n"
        f"   $h_{{\\text{{max}}}} = \\frac{{{_fmt_tex(ek_bottom)}}}{{({_fmt_tex(mass)})(9{{,}}8)}} = {_fmt_tex(h_max)}\\text{{ m}}$."
    )
    rubric = [
        {"step": 1, "criterion": f"Calculated launch Ek = {_fmt_tex(ek_bottom)} J", "marks": 1},
        {"step": 2, "criterion": "Equated mechanical energies at launch and peak", "marks": 1},
        {"step": 3, "criterion": f"Calculated maximum height = {_fmt_tex(h_max)} m", "marks": 2},
    ]
    hints = {
        "tier_1": "All kinetic energy at the bottom converts into potential energy at the peak.",
        "tier_2": f"h = Ek / (m * 9.8) = {ek_bottom} / ({mass} * 9.8).",
        "tier_3": ans,
    }
    return _make_q(r, "39_conservation_mechanical_energy_vertical_projectile_peak", 39, prompt, ans, sol, 4, ["used_kinematics_instead_of_energy_principles"], rubric, hints)


# ============================================================================ #
# 40. Conservation of mechanical energy: frictionless inclined slope
# ============================================================================ #
def build_40_conservation_mechanical_energy_frictionless_inclined_slope(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([20.0, 30.0, 45.0])
    h = r.choice([4.0, 5.0, 6.0, 8.0])
    length_slope = round(h / math.sin(math.radians(30)), 1)
    v_bottom = round(math.sqrt(2 * G_VAL * h), 2)

    svg = f"""<svg viewBox="0 0 500 240" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#F8FAFC" />
  <line x1="50" y1="200" x2="450" y2="200" stroke="#0F172A" stroke-width="2" />
  <polygon points="100,200 400,200 100,{200 - int(h * 15)}" fill="#E2E8F0" stroke="#475569" stroke-width="2" />
  <line x1="100" y1="200" x2="100" y2="{200 - int(h * 15)}" stroke="#DC2626" stroke-width="2" stroke-dasharray="4,4" />
  <text x="80" y="{200 - int(h * 7)}" font-size="12" fill="#DC2626" text-anchor="end">h = {_fmt(h)} m</text>
  <circle cx="120" cy="{200 - int(h * 15) + 10}" r="8" fill="#2563EB" />
  <text x="135" y="{200 - int(h * 15) + 5}" font-size="11" fill="#2563EB">Trolley ({_fmt(mass)} kg)</text>
  <text x="410" y="195" font-size="11" fill="#475569">Bottom (v = ?)</text>
</svg>"""

    prompt = (
        f"Refer to the inclined plane shown in the figure. A trolley of mass ${_fmt_tex(mass)}\\text{{ kg}}$ is released "
        f"from rest at the top of the ramp at a vertical height of ${_fmt_tex(h)}\\text{{ m}}$. "
        f"The track is frictionless ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"1. Explain why the normal force exerted by the ramp does no work on the trolley.\n"
        f"2. Use conservation of mechanical energy to calculate the speed of the trolley when it reaches the bottom of the ramp."
    )
    ans = f"{_fmt_tex(v_bottom)} m*s^-1"
    sol = (
        f"1. The normal force acts perpendicular ($90^\\circ$) to the displacement along the ramp. "
        f"Since $W = F \\Delta x \\cos(90^\\circ) = 0$, the normal force does zero work.\n"
        f"2. Since no friction acts, mechanical energy is conserved:\n"
        f"   $(E_k + E_p)_{{\\text{{top}}}} = (E_k + E_p)_{{\\text{{bottom}}}}$\n"
        f"   $0 + m g h = \\frac{{1}}{{2}} m v^2 + 0$\n"
        f"   $v = \\sqrt{{2 g h}} = \\sqrt{{2(9{{,}}8)({_fmt_tex(h)})}} = \\sqrt{{{round(2 * G_VAL * h, 2)}}} = {_fmt_tex(v_bottom)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Explanation: normal force is perpendicular to displacement (cos 90 = 0)", "marks": 1},
        {"step": 2, "criterion": "Formula (Ek + Ep)top = (Ek + Ep)bottom", "marks": 1},
        {"step": 3, "criterion": f"Calculated speed at bottom = {_fmt_tex(v_bottom)} m*s^-1", "marks": 2},
    ]
    hints = {
        "tier_1": "Only vertical height h matters for gravitational potential energy, not the length of the slope.",
        "tier_2": f"v = sqrt(2 * 9.8 * {h}).",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "40_conservation_mechanical_energy_frictionless_inclined_slope", 40, prompt, ans, sol, 4, ["used_slope_length_instead_of_vertical_height_in_mgh"], rubric, hints, spec)


# ============================================================================ #
# 41. Conservation of mechanical energy: roller coaster track
# ============================================================================ #
def build_41_conservation_mechanical_energy_roller_coaster_track(r: random.Random) -> Dict[str, Any]:
    h1 = r.choice([25.0, 30.0, 35.0])
    h2 = r.choice([10.0, 12.0, 15.0])
    v1 = r.choice([2.0, 4.0, 5.0])

    # 0.5*m*v1^2 + m*g*h1 = 0.5*m*v2^2 + m*g*h2 => v2^2 = v1^2 + 2*g*(h1 - h2)
    delta_h = h1 - h2
    v2_sq = v1**2 + 2 * G_VAL * delta_h
    v2 = round(math.sqrt(v2_sq), 2)

    svg = f"""<svg viewBox="0 0 500 240" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#F8FAFC" />
  <path d="M 50 60 Q 200 240 320 150 T 460 210" fill="none" stroke="#2563EB" stroke-width="4" />
  <circle cx="50" cy="60" r="7" fill="#DC2626" />
  <text x="65" y="55" font-size="11" fill="#DC2626" font-weight="bold">Point A (h1 = {_fmt(h1)} m, v1 = {_fmt(v1)} m/s)</text>
  <circle cx="320" cy="150" r="7" fill="#059669" />
  <text x="335" y="145" font-size="11" fill="#059669" font-weight="bold">Point B (h2 = {_fmt(h2)} m, v2 = ?)</text>
  <line x1="30" y1="215" x2="470" y2="215" stroke="#0F172A" stroke-width="2" />
  <text x="470" y="235" font-size="11" fill="#475569" text-anchor="end">Ground Level</text>
</svg>"""

    prompt = (
        f"Refer to the frictionless roller coaster track profile shown in the figure. A coaster car of mass $600\\text{{ kg}}$ "
        f"passes Point $A$ at a height of ${_fmt_tex(h1)}\\text{{ m}}$ with a speed of ${_fmt_tex(v1)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Assuming friction and air resistance are negligible ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$), calculate the speed "
        f"of the car when it reaches Point $B$ at a height of ${_fmt_tex(h2)}\\text{{ m}}$ above the ground."
    )
    ans = f"{_fmt_tex(v2)} m*s^-1"
    sol = (
        f"$(E_k + E_p)_A = (E_k + E_p)_B$\n"
        f"$\\frac{{1}}{{2}} m v_1^2 + m g h_1 = \\frac{{1}}{{2}} m v_2^2 + m g h_2$\n"
        f"Dividing by mass $m$:\n"
        f"$\\frac{{1}}{{2}} v_1^2 + g h_1 = \\frac{{1}}{{2}} v_2^2 + g h_2\n"
        f"$\\frac{{1}}{{2}} v_2^2 = \\frac{{1}}{{2}} v_1^2 + g (h_1 - h_2)\n"
        f"$v_2^2 = v_1^2 + 2 g (h_1 - h_2) = ({_fmt_tex(v1)})^2 + 2(9{{,}}8)({_fmt_tex(delta_h)})\n"
        f"$v_2^2 = {round(v1**2, 2)} + {round(2 * G_VAL * delta_h, 2)} = {_fmt_tex(round(v2_sq, 2))}\\text{{ m}}^2\\cdot\\text{{s}}^{{-2}}\n"
        f"$v_2 = \\sqrt{{{_fmt_tex(round(v2_sq, 2))}}} = {_fmt_tex(v2)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula (Ek + Ep)A = (Ek + Ep)B", "marks": 1},
        {"step": 2, "criterion": "Correct substitution of initial velocity and heights", "marks": 2},
        {"step": 3, "criterion": f"Answer v2 = {_fmt_tex(v2)} m*s^-1", "marks": 1},
    ]
    hints = {
        "tier_1": "v2^2 = v1^2 + 2*g*(h1 - h2).",
        "tier_2": f"v2 = sqrt({v1}^2 + 2 * 9.8 * ({h1} - {h2})).",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "41_conservation_mechanical_energy_roller_coaster_track", 41, prompt, ans, sol, 4, ["ignored_initial_kinetic_energy_at_point_a"], rubric, hints, spec)


# ============================================================================ #
# 42. Conservation of mechanical energy: pendulum bob lowest point
# ============================================================================ #
def build_42_conservation_mechanical_energy_pendulum_bob_lowest_point(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([0.5, 1.0, 1.5, 2.0])
    h_release = r.choice([0.45, 0.60, 0.80, 1.25])
    v_sq = 2 * G_VAL * h_release
    v_bottom = round(math.sqrt(v_sq), 2)

    svg = f"""<svg viewBox="0 0 500 240" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#F8FAFC" />
  <line x1="200" y1="20" x2="300" y2="20" stroke="#0F172A" stroke-width="4" />
  <line x1="250" y1="20" x2="350" y2="120" stroke="#475569" stroke-width="2" />
  <line x1="250" y1="20" x2="250" y2="200" stroke="#CBD5E1" stroke-dasharray="4,4" />
  <circle cx="350" cy="120" r="10" fill="#DC2626" />
  <circle cx="250" cy="200" r="10" fill="#059669" />
  <text x="370" y="125" font-size="12" fill="#DC2626">Released from rest</text>
  <text x="250" y="225" font-size="12" fill="#059669" text-anchor="middle">Lowest point (v = ?)</text>
  <line x1="220" y1="120" x2="350" y2="120" stroke="#DC2626" stroke-dasharray="2,2" />
  <line x1="220" y1="200" x2="250" y2="200" stroke="#059669" stroke-dasharray="2,2" />
  <text x="200" y="165" font-size="11" fill="#DC2626" text-anchor="end">h = {_fmt(h_release)} m</text>
</svg>"""

    prompt = (
        f"Refer to the pendulum system shown in the figure. A pendulum bob of mass ${_fmt_tex(mass)}\\text{{ kg}}$ is pulled "
        f"aside until it is at a vertical height of ${_fmt_tex(h_release)}\\text{{ m}}$ above its lowest equilibrium position "
        f"and released from rest ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"1. Name the two forces acting on the pendulum bob during its swing.\n"
        f"2. Explain why the tension force in the string does no work on the bob.\n"
        f"3. Calculate the speed ($v$) of the bob as it swings through its lowest position."
    )
    ans = f"{_fmt_tex(v_bottom)} m*s^-1"
    sol = (
        f"1. The two forces acting on the bob are the **gravitational force (weight)** and the **tension force** in the string.\n"
        f"2. The tension force acts radially towards the pivot, which is always perpendicular ($90^\\circ$) to the circular path "
        f"of motion of the bob. Since $W = F \\Delta x \\cos(90^\\circ) = 0$, the tension does no work.\n"
        f"3. Since tension does no work and air resistance is negligible, mechanical energy is conserved:\n"
        f"   $E_{{\\text{{mech, release}}}} = E_{{\\text{{mech, lowest}}}}$\n"
        f"   $m g h = \\frac{{1}}{{2}} m v^2 \\implies v = \\sqrt{{2 g h}} = \\sqrt{{2(9{{,}}8)({_fmt_tex(h_release)})}} = "
        f"\\sqrt{{{round(v_sq, 2)}}} = {_fmt_tex(v_bottom)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Named gravity/weight and string tension", "marks": 1},
        {"step": 2, "criterion": "Explained tension is perpendicular to path of motion (zero work)", "marks": 1},
        {"step": 3, "criterion": f"Calculated speed at lowest point = {_fmt_tex(v_bottom)} m*s^-1", "marks": 2},
    ]
    hints = {
        "tier_1": "All Ep at the release height converts into Ek at the lowest point.",
        "tier_2": f"v = sqrt(2 * 9.8 * {h_release}).",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "42_conservation_mechanical_energy_pendulum_bob_lowest_point", 42, prompt, ans, sol, 4, ["assumed_tension_does_work_on_pendulum"], rubric, hints, spec)


# ============================================================================ #
# 43. Conservation of mechanical energy: speed at intermediate height
# ============================================================================ #
def build_43_conservation_mechanical_energy_speed_at_intermediate_height(r: random.Random) -> Dict[str, Any]:
    h_top = r.choice([20.0, 30.0, 40.0])
    fraction = r.choice([0.25, 0.5, 0.75])
    h_inter = round(h_top * fraction, 1)
    # v = sqrt(2 * g * (h_top - h_inter))
    dh = h_top - h_inter
    v_sq = 2 * G_VAL * dh
    v = round(math.sqrt(v_sq), 2)

    prompt = (
        f"A ball of mass $0{{,}}5\\text{{ kg}}$ is dropped from rest from a rooftop at a height of ${_fmt_tex(h_top)}\\text{{ m}}$ "
        f"above the ground. Take $g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ and ignore air resistance.\n\n"
        f"Using energy principles, calculate the speed ($v$) of the ball when it has fallen to an intermediate height of "
        f"${_fmt_tex(h_inter)}\\text{{ m}}$ above the ground."
    )
    ans = f"{_fmt_tex(v)} m*s^-1"
    sol = (
        f"$(E_k + E_p)_{{\\text{{top}}}} = (E_k + E_p)_{{\\text{{intermediate}}}}$\n"
        f"$0 + m g h_{{\\text{{top}}}} = \\frac{{1}}{{2}} m v^2 + m g h_{{\\text{{inter}}}}$\n"
        f"Dividing by mass $m$:\n"
        f"$g h_{{\\text{{top}}}} - g h_{{\\text{{inter}}}} = \\frac{{1}}{{2}} v^2\n"
        f"$v^2 = 2 g (h_{{\\text{{top}}}} - h_{{\\text{{inter}}}}) = 2(9{{,}}8)({_fmt_tex(dh)}) = {_fmt_tex(round(v_sq, 2))}\\text{{ m}}^2\\cdot\\text{{s}}^{{-2}}\n"
        f"$v = \\sqrt{{{_fmt_tex(round(v_sq, 2))}}} = {_fmt_tex(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula (Ek + Ep)top = (Ek + Ep)inter", "marks": 1},
        {"step": 2, "criterion": f"Identified height drop Delta h = {_fmt_tex(dh)} m", "marks": 1},
        {"step": 3, "criterion": f"Calculated intermediate speed = {_fmt_tex(v)} m*s^-1", "marks": 2},
    ]
    hints = {
        "tier_1": "The lost potential energy mg(h_top - h_inter) converts into kinetic energy 0.5*m*v^2.",
        "tier_2": f"v = sqrt(2 * 9.8 * ({h_top} - {h_inter})).",
        "tier_3": ans,
    }
    return _make_q(r, "43_conservation_mechanical_energy_speed_at_intermediate_height", 43, prompt, ans, sol, 4, ["used_h_inter_instead_of_h_drop"], rubric, hints)


# ============================================================================ #
# 44. Non-conservative system: mechanical energy lost to friction
# ============================================================================ #
def build_44_non_conservative_system_mechanical_energy_lost_to_friction(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([5.0, 10.0, 15.0])
    h = r.choice([4.0, 5.0, 6.0])
    # theoretical v_bottom = sqrt(2*g*h)
    v_ideal = math.sqrt(2 * G_VAL * h)
    v_actual = round(v_ideal * r.choice([0.7, 0.75, 0.8]), 2)

    ep_initial = round(mass * G_VAL * h, 1)
    ek_final = round(0.5 * mass * (v_actual**2), 1)
    e_lost = round(ep_initial - ek_final, 1)

    prompt = (
        f"A crate of mass ${_fmt_tex(mass)}\\text{{ kg}}$ slides from rest down a rough loading ramp of vertical height "
        f"${_fmt_tex(h)}\\text{{ m}}$. When the crate reaches the bottom of the ramp, its speed is measured to be "
        f"${_fmt_tex(v_actual)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"1. State why mechanical energy is **not** conserved during this motion.\n"
        f"2. Calculate the mechanical energy ($E_{{\\text{{mech, initial}}}}$) at the top of the ramp.\n"
        f"3. Calculate the mechanical energy ($E_{{\\text{{mech, final}}}}$) at the bottom of the ramp.\n"
        f"4. Calculate the work done by the frictional force ($W_{{\\text{{friction}}}}$) / energy lost to heat."
    )
    ans = f"Energy lost to friction = {_fmt_tex(e_lost)} J (W_friction = -{_fmt_tex(e_lost)} J)"
    sol = (
        f"1. Mechanical energy is not conserved because friction is a **non-conservative force** that converts mechanical energy into internal thermal energy (heat).\n"
        f"2. $E_{{\\text{{mech, top}}}} = E_p + E_k = m g h + 0 = ({_fmt_tex(mass)})(9{{,}}8)({_fmt_tex(h)}) = {_fmt_tex(ep_initial)}\\text{{ J}}$.\n"
        f"3. $E_{{\\text{{mech, bottom}}}} = E_p + E_k = 0 + \\frac{{1}}{{2}} m v^2 = \\frac{{1}}{{2}} ({_fmt_tex(mass)}) ({_fmt_tex(v_actual)})^2 = {_fmt_tex(ek_final)}\\text{{ J}}$.\n"
        f"4. $W_{{\\text{{nc}}}} = \\Delta E_{{\\text{{mech}}}} = E_{{\\text{{mech, final}}}} - E_{{\\text{{mech, initial}}}} = "
        f"{_fmt_tex(ek_final)} - {_fmt_tex(ep_initial)} = -{_fmt_tex(e_lost)}\\text{{ J}}$.\n"
        f"   Therefore, **${_fmt_tex(e_lost)}\\text{{ J}}$** of mechanical energy was dissipated as heat."
    )
    rubric = [
        {"step": 1, "criterion": "Stated friction is a non-conservative force", "marks": 1},
        {"step": 2, "criterion": f"Calculated E_initial = {_fmt_tex(ep_initial)} J", "marks": 1},
        {"step": 3, "criterion": f"Calculated E_final = {_fmt_tex(ek_final)} J", "marks": 1},
        {"step": 4, "criterion": f"Calculated W_nc = -{_fmt_tex(e_lost)} J (energy lost)", "marks": 2},
    ]
    hints = {
        "tier_1": "W_nc = E_mech_final - E_mech_initial.",
        "tier_2": f"Initial E = {ep_initial} J; Final E = {ek_final} J.",
        "tier_3": ans,
    }
    return _make_q(r, "44_non_conservative_system_mechanical_energy_lost_to_friction", 44, prompt, ans, sol, 5, ["assumed_mechanical_energy_is_always_conserved"], rubric, hints)


# ============================================================================ #
# 45. Work done by gravitational force as change in Ep
# ============================================================================ #
def build_45_work_done_by_gravitational_force_as_change_in_ep(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([12.0, 15.0, 20.0, 25.0])
    dy = r.choice([2.0, 3.0, 4.0, 5.0])
    w_grav = round(mass * G_VAL * dy, 1)

    prompt = (
        f"A construction worker lowers a bucket of concrete of mass ${_fmt_tex(mass)}\\text{{ kg}}$ vertically downwards "
        f"through a distance of ${_fmt_tex(dy)}\\text{{ m}}$ ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"1. Calculate the work done by the gravitational force ($W_g$) on the bucket.\n"
        f"2. State whether gravity does positive or negative work on the bucket during its descent, giving a reason.\n"
        f"3. State how the gravitational potential energy of the bucket changed."
    )
    ans = f"Wg = +{_fmt_tex(w_grav)} J; Positive work; Ep decreased by {_fmt_tex(w_grav)} J"
    sol = (
        f"1. $W_g = F_g \\Delta y \\cos\\theta = (m g) \\Delta y \\cos(0^\\circ) = ({_fmt_tex(mass)})(9{{,}}8)({_fmt_tex(dy)})(1) = +{_fmt_tex(w_grav)}\\text{{ J}}$.\n"
        f"2. Gravity does **positive work** because the force of gravity points in the same direction (downwards) as the displacement vector.\n"
        f"3. Since $W_g = -\\Delta E_p$, the gravitational potential energy of the bucket **decreased by ${_fmt_tex(w_grav)}\\text{{ J}}$**."
    )
    rubric = [
        {"step": 1, "criterion": f"Calculated Wg = +{_fmt_tex(w_grav)} J", "marks": 2},
        {"step": 2, "criterion": "Stated positive work (force and displacement in same direction)", "marks": 1},
        {"step": 3, "criterion": f"Stated Ep decreased by {_fmt_tex(w_grav)} J", "marks": 1},
    ]
    hints = {
        "tier_1": "W = F * Delta x * cos(theta). For downward motion, theta = 0 deg.",
        "tier_2": f"Wg = {mass} * 9.8 * {dy} = {w_grav} J.",
        "tier_3": ans,
    }
    return _make_q(r, "45_work_done_by_gravitational_force_as_change_in_ep", 45, prompt, ans, sol, 4, ["wrong_sign_for_gravitational_work"], rubric, hints)


# ============================================================================ #
# 46. Work-energy theorem: introductory net work and delta Ek
# ============================================================================ #
def build_46_work_energy_theorem_introductory_net_work_delta_ek(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([400, 500, 600])
    vi = r.choice([10.0, 12.0, 15.0])
    vf = vi + r.choice([6.0, 8.0, 10.0])
    ek_i = 0.5 * mass * (vi**2)
    ek_f = 0.5 * mass * (vf**2)
    w_net = round(ek_f - ek_i, 1)

    prompt = (
        f"A bobsled of mass ${mass}\\text{{ kg}}$ accelerates horizontally from an initial velocity of "
        f"${_fmt_tex(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ to a final velocity of ${_fmt_tex(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"1. State the **Work-Energy Theorem**.\n"
        f"2. Calculate the initial kinetic energy ($E_{{k, i}}$) of the bobsled.\n"
        f"3. Calculate the final kinetic energy ($E_{{k, f}}$) of the bobsled.\n"
        f"4. Calculate the net work ($W_{{\\text{{net}}}}$) done on the bobsled."
    )
    ans = f"W_net = {_fmt_tex(w_net)} J"
    sol = (
        f"1. **Work-Energy Theorem:** The net work done on an object is equal to the change in the object's kinetic energy "
        f"($W_{{\\text{{net}}}} = \\Delta E_k = E_{{k, f}} - E_{{k, i}}$).\n"
        f"2. $E_{{k, i}} = \\frac{{1}}{{2}} m v_i^2 = \\frac{{1}}{{2}} ({mass}) ({_fmt_tex(vi)})^2 = {_fmt_tex(ek_i)}\\text{{ J}}$.\n"
        f"3. $E_{{k, f}} = \\frac{{1}}{{2}} m v_f^2 = \\frac{{1}}{{2}} ({mass}) ({_fmt_tex(vf)})^2 = {_fmt_tex(ek_f)}\\text{{ J}}$.\n"
        f"4. $W_{{\\text{{net}}}} = \\Delta E_k = E_{{k, f}} - E_{{k, i}} = {_fmt_tex(ek_f)} - {_fmt_tex(ek_i)} = {_fmt_tex(w_net)}\\text{{ J}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Statement of Work-Energy Theorem", "marks": 1},
        {"step": 2, "criterion": f"Calculated Ek_i = {_fmt_tex(ek_i)} J", "marks": 1},
        {"step": 3, "criterion": f"Calculated Ek_f = {_fmt_tex(ek_f)} J", "marks": 1},
        {"step": 4, "criterion": f"Calculated W_net = {_fmt_tex(w_net)} J", "marks": 1},
    ]
    hints = {
        "tier_1": "W_net = Delta Ek = 0.5*m*(vf^2 - vi^2).",
        "tier_2": f"W_net = 0.5 * {mass} * ({vf}^2 - {vi}^2).",
        "tier_3": ans,
    }
    return _make_q(r, "46_work_energy_theorem_introductory_net_work_delta_ek", 46, prompt, ans, sol, 4, ["used_difference_of_velocities_squared_incorrectly"], rubric, hints)


# ============================================================================ #
# 47. Mechanical power: rate of energy transfer
# ============================================================================ #
def build_47_mechanical_power_rate_of_energy_transfer(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([300, 450, 600, 800])
    h = r.choice([6.0, 9.0, 12.0, 15.0])
    dt = r.choice([10.0, 15.0, 20.0])

    work = round(mass * G_VAL * h, 1)
    power_w = round(work / dt, 1)
    power_kw = round(power_w / 1000.0, 3)

    prompt = (
        f"An electric hoist lifts a motor vehicle engine of mass ${mass}\\text{{ kg}}$ vertically through a height of "
        f"${_fmt_tex(h)}\\text{{ m}}$ in ${_fmt_tex(dt)}\\text{{ seconds}}$ at constant velocity ($g = 9{{,}}8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$).\n\n"
        f"1. Define the term *power*.\n"
        f"2. Calculate the work done by the hoist in lifting the engine.\n"
        f"3. Calculate the power output of the hoist in watts ($\\text{{W}}$) and kilowatts ($\\text{{kW}}$)."
    )
    ans = f"P = {_fmt_tex(power_w)} W ({_fmt_tex(power_kw)} kW)"
    sol = (
        f"1. **Power** is the rate at which work is done or the rate at which energy is transferred ($P = \\frac{{W}}{{\\Delta t}}$).\n"
        f"2. $W = \\Delta E_p = m g h = ({mass})(9{{,}}8)({_fmt_tex(h)}) = {_fmt_tex(work)}\\text{{ J}}$.\n"
        f"3. $P = \\frac{{W}}{{\\Delta t}} = \\frac{{{_fmt_tex(work)}}}{{{_fmt_tex(dt)}}} = {_fmt_tex(power_w)}\\text{{ W}}$.\n"
        f"   In kilowatts: $P = \\frac{{{_fmt_tex(power_w)}}}{{1000}} = {_fmt_tex(power_kw)}\\text{{ kW}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of power as rate of doing work", "marks": 1},
        {"step": 2, "criterion": f"Calculated work done W = {_fmt_tex(work)} J", "marks": 1},
        {"step": 3, "criterion": f"Calculated power in W = {_fmt_tex(power_w)} W", "marks": 1},
        {"step": 4, "criterion": f"Converted power to kW = {_fmt_tex(power_kw)} kW", "marks": 1},
    ]
    hints = {
        "tier_1": "Power = Work / time = mgh / Delta t.",
        "tier_2": f"P = ({mass} * 9.8 * {h}) / {dt}.",
        "tier_3": ans,
    }
    return _make_q(r, "47_mechanical_power_rate_of_energy_transfer", 47, prompt, ans, sol, 4, ["multiplied_by_time_instead_of_dividing_for_power"], rubric, hints)


# ============================================================================ #
# 48. Energy efficiency: useful energy percentage
# ============================================================================ #
def build_48_energy_efficiency_useful_energy_percentage(r: random.Random) -> Dict[str, Any]:
    e_input = r.choice([2000, 3000, 4000, 5000])
    eff_pct = r.choice([60, 65, 70, 75, 80])
    e_useful = round(e_input * (eff_pct / 100.0), 1)
    e_wasted = round(e_input - e_useful, 1)

    prompt = (
        f"An electric winch draws ${e_input}\\text{{ J}}$ of electrical energy from a supply while hauling a load. "
        f"The useful mechanical work performed on the load is ${_fmt_tex(e_useful)}\\text{{ J}}$.\n\n"
        f"1. State the **Law of Conservation of Energy**.\n"
        f"2. Calculate the percentage efficiency of the winch.\n"
        f"3. Calculate the quantity of energy wasted (dissipated as thermal energy and sound)."
    )
    ans = f"Efficiency = {eff_pct}%, Wasted = {_fmt_tex(e_wasted)} J"
    sol = (
        f"1. **Law of Conservation of Energy:** Energy cannot be created or destroyed; it can only be transformed from one form into another.\n"
        f"2. $\\text{{Percentage efficiency}} = \\frac{{E_{{\\text{{useful}}}}}}{{E_{{\\text{{input}}}}}} \\times 100\\% = "
        f"\\frac{{{_fmt_tex(e_useful)}}}{{{e_input}}} \\times 100\\% = {eff_pct}\\%$.\n"
        f"3. $E_{{\\text{{wasted}}}} = E_{{\\text{{input}}}} - E_{{\\text{{useful}}}} = {e_input} - {_fmt_tex(e_useful)} = {_fmt_tex(e_wasted)}\\text{{ J}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Statement of Law of Conservation of Energy", "marks": 1},
        {"step": 2, "criterion": f"Efficiency calculation = {eff_pct}%", "marks": 2},
        {"step": 3, "criterion": f"Wasted energy calculation = {_fmt_tex(e_wasted)} J", "marks": 1},
    ]
    hints = {
        "tier_1": "Efficiency = (Useful energy / Total input energy) * 100%.",
        "tier_2": f"Efficiency = ({e_useful} / {e_input}) * 100% = {eff_pct}%.",
        "tier_3": ans,
    }
    return _make_q(r, "48_energy_efficiency_useful_energy_percentage", 48, prompt, ans, sol, 4, ["inverted_efficiency_ratio"], rubric, hints)


# ============================================================================ #
# 49. Multistage kinematics and energy conservation synthesis
# ============================================================================ #
def build_49_multistage_kinematics_and_energy_conservation_synthesis(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([2.0, 4.0, 5.0])
    h = r.choice([5.0, 7.2, 10.0])
    v_bottom = round(math.sqrt(2 * G_VAL * h), 2)
    a_brake = r.choice([2.0, 2.5, 4.0])
    # dx_stop = v_bottom^2 / (2 * a_brake) = 2*g*h / (2*a_brake) = g*h / a_brake
    dx_stop = round((G_VAL * h) / a_brake, 2)

    svg = f"""<svg viewBox="0 0 500 240" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#F8FAFC" />
  <path d="M 60 40 Q 60 180 200 180 L 450 180" fill="none" stroke="#2563EB" stroke-width="3" />
  <circle cx="60" cy="40" r="7" fill="#DC2626" />
  <text x="75" y="45" font-size="11" fill="#DC2626">Point A (h = {_fmt(h)} m)</text>
  <circle cx="200" cy="180" r="7" fill="#059669" />
  <text x="200" y="170" font-size="11" fill="#059669" text-anchor="middle">Point B (bottom)</text>
  <line x1="200" y1="180" x2="450" y2="180" stroke="#D97706" stroke-width="4" stroke-dasharray="6,4" />
  <text x="325" y="205" font-size="11" fill="#D97706" text-anchor="middle">Rough Flat Section (a = -{_fmt(a_brake)} m/s²)</text>
  <circle cx="{200 + int(dx_stop * 8)}" cy="180" r="7" fill="#475569" />
  <text x="{200 + int(dx_stop * 8)}" y="170" font-size="11" fill="#475569" text-anchor="middle">Point C (Rest)</text>
</svg>"""

    prompt = (
        f"Refer to the composite track shown in the figure. A block of mass ${_fmt_tex(mass)}\\text{{ kg}}$ is released "
        f"from rest at Point $A$ at a vertical height of ${_fmt_tex(h)}\\text{{ m}}$. The curved section from $A$ to $B$ is "
        f"completely frictionless. At Point $B$, the block enters a rough horizontal section where friction brings it to rest "
        f"with a constant deceleration of ${_fmt_tex(a_brake)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ at Point $C$.\n\n"
        f"1. Use conservation of mechanical energy along the frictionless section to calculate the speed of the block at Point $B$.\n"
        f"2. Use equations of motion to calculate the stopping distance ($\\Delta x$) between Point $B$ and Point $C$."
    )
    ans = f"v_B = {_fmt_tex(v_bottom)} m*s^-1, Delta x = {_fmt_tex(dx_stop)} m"
    sol = (
        f"1. **Section A to B (Conservation of Mechanical Energy):**\n"
        f"   $(E_k + E_p)_A = (E_k + E_p)_B$\n"
        f"   $0 + m g h = \\frac{{1}}{{2}} m v_B^2 + 0$\n"
        f"   $v_B = \\sqrt{{2 g h}} = \\sqrt{{2(9{{,}}8)({_fmt_tex(h)})}} = {_fmt_tex(v_bottom)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"2. **Section B to C (Kinematics on rough horizontal surface):**\n"
        f"   $v_i = {_fmt_tex(v_bottom)}\\text{{ m/s}}$, $v_f = 0$, $a = -{_fmt_tex(a_brake)}\\text{{ m/s}}^2$.\n"
        f"   $v_f^2 = v_i^2 + 2 a \\Delta x$\n"
        f"   $0 = ({_fmt_tex(v_bottom)})^2 + 2(-{_fmt_tex(a_brake)}) \\Delta x$\n"
        f"   $2({_fmt_tex(a_brake)}) \\Delta x = {round(v_bottom**2, 2)}$\n"
        f"   $\\Delta x = \\frac{{{round(v_bottom**2, 2)}}}{{{2*a_brake}}} = {_fmt_tex(dx_stop)}\\text{{ m}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Equated mechanical energies at A and B", "marks": 1},
        {"step": 2, "criterion": f"Calculated v_B = {_fmt_tex(v_bottom)} m*s^-1", "marks": 2},
        {"step": 3, "criterion": "Formula vf^2 = vi^2 + 2*a*dx", "marks": 1},
        {"step": 4, "criterion": f"Calculated stopping distance Delta x = {_fmt_tex(dx_stop)} m", "marks": 2},
    ]
    hints = {
        "tier_1": "Find v at B using energy conservation (v = sqrt(2gh)), then find stopping distance using vf^2 = vi^2 + 2*a*dx.",
        "tier_2": f"v_B = sqrt(2 * 9.8 * {h}) = {_fmt(v_bottom)} m/s. Then dx = v_B^2 / (2 * {a_brake}).",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "49_multistage_kinematics_and_energy_conservation_synthesis", 49, prompt, ans, sol, 6, ["applied_energy_conservation_to_rough_horizontal_section"], rubric, hints, spec)


# ============================================================================ #
# 50. Motion and energy diagnostic autopsy and misconception repair
# ============================================================================ #
def build_50_motion_and_energy_diagnostic_autopsy_and_misconception_repair(r: random.Random) -> Dict[str, Any]:
    mass = r.choice([2.0, 5.0, 10.0])
    h = r.choice([10.0, 15.0, 20.0])
    correct_ep = round(mass * G_VAL * h, 1)
    correct_v = round(math.sqrt(2 * G_VAL * h), 2)

    prompt = (
        f"A learner attempts the following physics problem:\n"
        f"'A ball of mass ${mass}\\text{{ kg}}$ is dropped from a height of ${_fmt_tex(h)}\\text{{ m}}$ in the presence of air resistance. "
        f"Calculate its impact speed.'\n\n"
        f"The learner's memorandum working shows:\n"
        f"   $\\text{{Step 1: }} E_p = mgh = ({mass})(9{{,}}8)({_fmt_tex(h)}) = {_fmt_tex(correct_ep)}\\text{{ J}}$\n"
        f"   $\\text{{Step 2: }} E_k = \\frac{{1}}{{2}} m v^2 \\implies {_fmt_tex(correct_ep)} = \\frac{{1}}{{2}} ({mass}) v^2$\n"
        f"   $\\text{{Step 3: }} v = \\sqrt{{{round(2 * G_VAL * h, 2)}}} = {_fmt_tex(correct_v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$\n\n"
        f"1. Identify the fundamental conceptual error in the learner's reasoning.\n"
        f"2. Explain under what strict condition the relation $E_{{\\text{{mech, top}}}} = E_{{\\text{{mech, bottom}}}}$ holds true.\n"
        f"3. State whether the actual impact speed in the real world will be greater than, equal to, or less than "
        f"${_fmt_tex(correct_v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$, giving an energy-based explanation."
    )
    ans = f"Conceptual error: applied mechanical energy conservation in non-isolated system; actual speed will be less than {_fmt_tex(correct_v)} m*s^-1"
    sol = (
        f"1. **Conceptual error:** The learner applied the Law of Conservation of Mechanical Energy directly, "
        f"ignoring the presence of air resistance. Air resistance is a non-conservative force that removes mechanical energy from the system.\n"
        f"2. Conservation of mechanical energy holds strictly only in an **isolated system**, where no external or non-conservative forces "
        f"(such as air resistance or friction) do work ($W_{{\\text{{nc}}}} = 0$).\n"
        f"3. The actual impact speed will be **less than ${_fmt_tex(correct_v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$**. "
        f"Because air resistance does negative work ($W_{{\\text{{air}}}} < 0$), part of the initial gravitational potential energy "
        f"is converted into thermal energy, leaving less kinetic energy available at ground level ($E_k < mgh \\implies v < \\sqrt{{2gh}}$)."
    )
    rubric = [
        {"step": 1, "criterion": "Identified incorrect application of energy conservation in presence of air resistance", "marks": 2},
        {"step": 2, "criterion": "Stated strict condition: isolated system / zero non-conservative forces", "marks": 1},
        {"step": 3, "criterion": f"Stated actual speed is less than {_fmt_tex(correct_v)} m*s^-1 with energy loss justification", "marks": 2},
    ]
    hints = {
        "tier_1": "Air resistance is a non-conservative force that dissipates mechanical energy as heat.",
        "tier_2": "In the presence of air resistance, E_mech is not conserved: final Ek is strictly less than initial Ep.",
        "tier_3": ans,
    }
    return _make_q(r, "50_motion_and_energy_diagnostic_autopsy_and_misconception_repair", 50, prompt, ans, sol, 5, ["assumed_conservation_holds_with_air_resistance"], rubric, hints)


# ============================================================================ #
# BUILDERS EXPORT DICTIONARY 26–50
# ============================================================================ #
BUILDERS_26_50: Dict[str, Any] = {
    "26_converting_velocity_time_to_acceleration_time_graph": build_26_converting_velocity_time_to_acceleration_time_graph,
    "27_ticker_timer_tape_analysis_constant_velocity": build_27_ticker_timer_tape_analysis_constant_velocity,
    "28_ticker_timer_tape_analysis_acceleration": build_28_ticker_timer_tape_analysis_acceleration,
    "29_vertical_motion_free_fall_dropped_from_rest": build_29_vertical_motion_free_fall_dropped_from_rest,
    "30_vertical_motion_projected_downwards_from_height": build_30_vertical_motion_projected_downwards_from_height,
    "31_vertical_motion_projected_upwards_max_height_and_time": build_31_vertical_motion_projected_upwards_max_height_and_time,
    "32_gravitational_potential_energy_direct_calculation": build_32_gravitational_potential_energy_direct_calculation,
    "33_gravitational_potential_energy_solve_for_height_or_mass": build_33_gravitational_potential_energy_solve_for_height_or_mass,
    "34_kinetic_energy_direct_calculation": build_34_kinetic_energy_direct_calculation,
    "35_kinetic_energy_solve_for_velocity": build_35_kinetic_energy_solve_for_velocity,
    "36_kinetic_energy_solve_for_mass": build_36_kinetic_energy_solve_for_mass,
    "37_total_mechanical_energy_isolated_system": build_37_total_mechanical_energy_isolated_system,
    "38_conservation_mechanical_energy_free_fall_impact_speed": build_38_conservation_mechanical_energy_free_fall_impact_speed,
    "39_conservation_mechanical_energy_vertical_projectile_peak": build_39_conservation_mechanical_energy_vertical_projectile_peak,
    "40_conservation_mechanical_energy_frictionless_inclined_slope": build_40_conservation_mechanical_energy_frictionless_inclined_slope,
    "41_conservation_mechanical_energy_roller_coaster_track": build_41_conservation_mechanical_energy_roller_coaster_track,
    "42_conservation_mechanical_energy_pendulum_bob_lowest_point": build_42_conservation_mechanical_energy_pendulum_bob_lowest_point,
    "43_conservation_mechanical_energy_speed_at_intermediate_height": build_43_conservation_mechanical_energy_speed_at_intermediate_height,
    "44_non_conservative_system_mechanical_energy_lost_to_friction": build_44_non_conservative_system_mechanical_energy_lost_to_friction,
    "45_work_done_by_gravitational_force_as_change_in_ep": build_45_work_done_by_gravitational_force_as_change_in_ep,
    "46_work_energy_theorem_introductory_net_work_delta_ek": build_46_work_energy_theorem_introductory_net_work_delta_ek,
    "47_mechanical_power_rate_of_energy_transfer": build_47_mechanical_power_rate_of_energy_transfer,
    "48_energy_efficiency_useful_energy_percentage": build_48_energy_efficiency_useful_energy_percentage,
    "49_multistage_kinematics_and_energy_conservation_synthesis": build_49_multistage_kinematics_and_energy_conservation_synthesis,
    "50_motion_and_energy_diagnostic_autopsy_and_misconception_repair": build_50_motion_and_energy_diagnostic_autopsy_and_misconception_repair,
}
