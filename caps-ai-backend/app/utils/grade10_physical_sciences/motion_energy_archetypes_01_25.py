"""Grade 10 Physical Sciences — 1D Motion & Mechanical Energy (Archetypes 01–25).
Deterministic 6-pillar question generators covering Paper 1 (Physics Term 3):
- Subskills 01–07: Reference frames, position, distance, displacement, speed, velocity, acceleration.
- Subskills 08–14: The 4 kinematic equations of motion and solving for all parameters.
- Subskills 15–17: Stopping distances (reaction time + braking) and multi-stage motion.
- Subskills 18–25: Position-time, velocity-time, and acceleration-time graphs (gradient, area, reversals, conversions).

All questions adhere strictly to the 6-pillar contract and the South African National Curriculum Standards.
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
# 01. Frame of reference and 1D position
# ============================================================================ #
def build_01_frame_of_reference_and_1d_position(r: random.Random) -> Dict[str, Any]:
    pos_a = r.choice([-15, -12, -10, -8])
    pos_b = r.choice([6, 8, 12, 15, 20])
    unit = "m"
    dir_ref = r.choice(["east", "to the right"])

    svg = f"""<svg viewBox="0 0 500 120" width="100%" height="120" xmlns="http://www.w3.org/2000/svg">
  <line x1="30" y1="60" x2="470" y2="60" stroke="#0F172A" stroke-width="2" marker-end="url(#arrow)" />
  <defs><marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#0F172A"/></marker></defs>
  <line x1="250" y1="50" x2="250" y2="70" stroke="#DC2626" stroke-width="3" />
  <text x="250" y="88" font-size="12" fill="#DC2626" text-anchor="middle" font-weight="bold">Origin (0 m)</text>
  <circle cx="{250 + pos_a * 8}" cy="60" r="5" fill="#2563EB" />
  <text x="{250 + pos_a * 8}" y="45" font-size="12" fill="#2563EB" text-anchor="middle">A ({pos_a} m)</text>
  <circle cx="{250 + pos_b * 8}" cy="60" r="5" fill="#059669" />
  <text x="{250 + pos_b * 8}" y="45" font-size="12" fill="#059669" text-anchor="middle">B (+{pos_b} m)</text>
  <text x="470" y="85" font-size="11" fill="#475569" text-anchor="end">+ direction ({dir_ref})</text>
</svg>"""

    prompt = (
        f"Refer to the one-dimensional position coordinate axis shown in the figure, where the positive direction is chosen as {dir_ref}.\n\n"
        f"1. Define the term *frame of reference*.\n"
        f"2. Write down the position of point $A$ and point $B$ relative to the origin, including magnitude and direction.\n"
        f"3. A learner walks from point $A$ to point $B$. Calculate the learner's displacement $\\Delta x$."
    )
    dx = pos_b - pos_a
    ans = f"Delta x = +{dx} m ({dir_ref})"
    sol = (
        f"1. A frame of reference is a coordinate system or set of axes within which observers measure the position and motion of objects.\n"
        f"2. Position of $A$: ${abs(pos_a)}\\text{{ m}}$ in the negative direction (opposite to {dir_ref}).\n"
        f"   Position of $B$: ${pos_b}\\text{{ m}}$ in the positive direction ({dir_ref}).\n"
        f"3. $\\Delta x = x_f - x_i = {pos_b} - ({pos_a}) = {pos_b} + {abs(pos_a)} = {dx}\\text{{ m}}$ {dir_ref}."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of frame of reference", "marks": 1},
        {"step": 2, "criterion": "Correct positions with signs/directions", "marks": 2},
        {"step": 3, "criterion": f"Displacement formula and answer Delta x = {dx} m", "marks": 2},
    ]
    hints = {
        "tier_1": "Displacement is change in position: Delta x = x_final - x_initial.",
        "tier_2": f"Substitute x_final = {pos_b} and x_initial = {pos_a}.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "01_frame_of_reference_and_1d_position", 1, prompt, ans, sol, 5, ["confused_position_with_distance"], rubric, hints, spec)


# ============================================================================ #
# 02. Distance vs displacement in 1D
# ============================================================================ #
def build_02_distance_vs_displacement_1d(r: random.Random) -> Dict[str, Any]:
    d1 = r.choice([30, 40, 50, 60, 80])
    d2 = r.choice([15, 20, 25, 35])
    dir_init = r.choice(["east", "north"])
    dir_rev = "west" if dir_init == "east" else "south"

    total_dist = d1 + d2
    net_disp = d1 - d2

    prompt = (
        f"A cyclist travels along a straight road for ${d1}\\text{{ m}}$ due {dir_init}, turns around, and rides "
        f"${d2}\\text{{ m}}$ due {dir_rev}.\n\n"
        f"1. Differentiate between *distance* and *displacement*.\n"
        f"2. Calculate the total distance covered by the cyclist.\n"
        f"3. Calculate the resultant displacement of the cyclist relative to the starting point."
    )
    ans = f"Distance = {total_dist} m; Displacement = {net_disp} m {dir_init}"
    sol = (
        f"1. **Distance** is the total path length travelled by an object (a scalar quantity). "
        f"**Displacement** is the change in position of an object, which is the shortest straight line from start to finish with direction (a vector quantity).\n"
        f"2. $\\text{{Total distance}} = d_1 + d_2 = {d1} + {d2} = {total_dist}\\text{{ m}}$.\n"
        f"3. Taking {dir_init} as the positive direction:\n"
        f"   $\\Delta x = (+{d1}) + (-{d2}) = {net_disp}\\text{{ m}}$ due {dir_init}."
    )
    rubric = [
        {"step": 1, "criterion": "Distinction: scalar path length vs vector position change", "marks": 2},
        {"step": 2, "criterion": f"Distance = {total_dist} m", "marks": 1},
        {"step": 3, "criterion": f"Displacement = {net_disp} m {dir_init}", "marks": 2},
    ]
    hints = {
        "tier_1": "Distance adds all magnitudes; displacement takes directions into account.",
        "tier_2": f"Distance = {d1} + {d2}. Displacement = {d1} - {d2} in the initial direction.",
        "tier_3": ans,
    }
    return _make_q(r, "02_distance_vs_displacement_1d", 2, prompt, ans, sol, 5, ["confused_distance_and_displacement"], rubric, hints)


# ============================================================================ #
# 03. Average speed calculation
# ============================================================================ #
def build_03_average_speed_calculation(r: random.Random) -> Dict[str, Any]:
    lap_length_m = r.choice([400, 800, 1200, 1500])
    time_s = r.choice([50, 60, 80, 100, 125])
    speed = round(lap_length_m / time_s, 2)

    prompt = (
        f"An athlete completes a running track circuit of length ${lap_length_m}\\text{{ m}}$ in a time of "
        f"${time_s}\\text{{ seconds}}$.\n\n"
        f"1. Define the term *average speed*.\n"
        f"2. Calculate the athlete's average speed in metres per second ($\\text{{m}}\\cdot\\text{{s}}^{{-1}}$).\n"
        f"3. State whether average speed is a scalar or vector quantity."
    )
    ans = f"{_fmt_tex(speed)} m*s^-1"
    sol = (
        f"1. **Average speed** is the total distance travelled per unit time ($\\text{{average speed}} = \\frac{{\\text{{total distance}}}}{{\\Delta t}}$).\n"
        f"2. $\\text{{Average speed}} = \\frac{{{lap_length_m}}}{{{time_s}}} = {_fmt_tex(speed)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"3. Average speed is a **scalar** quantity because it has magnitude only (no direction)."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of average speed", "marks": 1},
        {"step": 2, "criterion": "Formula and substitution", "marks": 1},
        {"step": 3, "criterion": f"Average speed = {_fmt_tex(speed)} m/s", "marks": 1},
        {"step": 4, "criterion": "Identified as scalar", "marks": 1},
    ]
    hints = {
        "tier_1": "Average speed = total distance / total time.",
        "tier_2": f"Divide {lap_length_m} by {time_s}.",
        "tier_3": ans,
    }
    return _make_q(r, "03_average_speed_calculation", 3, prompt, ans, sol, 4, ["confused_speed_and_velocity"], rubric, hints)


# ============================================================================ #
# 04. Average velocity calculation
# ============================================================================ #
def build_04_average_velocity_calculation(r: random.Random) -> Dict[str, Any]:
    dx = r.choice([120, 150, 180, 240, 300])
    dt = r.choice([15, 20, 25, 30, 40])
    direction = r.choice(["west", "forward", "north"])
    v_avg = round(dx / dt, 2)

    prompt = (
        f"A delivery drone flies with a straight-line displacement of ${dx}\\text{{ m}}$ due {direction} in "
        f"${dt}\\text{{ s}}$.\n\n"
        f"1. Define the term *average velocity*.\n"
        f"2. Calculate the average velocity ($\\vec{{v}}_{{\\text{{avg}}}}$) of the drone."
    )
    ans = f"{_fmt_tex(v_avg)} m*s^-1 {direction}"
    sol = (
        f"1. **Average velocity** is the rate of change of position or total displacement per unit time "
        f"($\\vec{{v}}_{{\\text{{avg}}}} = \\frac{{\\Delta \\vec{{x}}}}{{\\Delta t}}$).\n"
        f"2. $\\vec{{v}}_{{\\text{{avg}}}} = \\frac{{\\Delta \\vec{{x}}}}{{\\Delta t}} = \\frac{{{dx}}}{{{dt}}} = "
        f"{_fmt_tex(v_avg)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ due {direction}."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of average velocity", "marks": 1},
        {"step": 2, "criterion": "Formula v = Delta x / Delta t", "marks": 1},
        {"step": 3, "criterion": f"Calculated magnitude {_fmt_tex(v_avg)} with correct direction {direction}", "marks": 2},
    ]
    hints = {
        "tier_1": "Velocity is a vector: magnitude and direction must be stated.",
        "tier_2": f"v_avg = {dx} / {dt} with direction {direction}.",
        "tier_3": ans,
    }
    return _make_q(r, "04_average_velocity_calculation", 4, prompt, ans, sol, 4, ["omitted_direction_in_velocity"], rubric, hints)


# ============================================================================ #
# 05. Instantaneous speed and velocity
# ============================================================================ #
def build_05_instantaneous_speed_vs_velocity(r: random.Random) -> Dict[str, Any]:
    speed_kmh = r.choice([60, 72, 90, 108, 120])
    speed_ms = round(speed_kmh / 3.6, 2)
    dir_heading = r.choice(["south", "east", "towards Cape Town"])

    prompt = (
        f"A driver glances at her car speedometer while travelling along a straight highway heading {dir_heading}. "
        f"The speedometer needle points exactly to ${speed_kmh}\\text{{ km}}\\cdot\\text{{h}}^{{-1}}$.\n\n"
        f"1. Define *instantaneous velocity*.\n"
        f"2. Convert the speedometer reading to metres per second ($\\text{{m}}\\cdot\\text{{s}}^{{-1}}$).\n"
        f"3. Write down the driver's instantaneous velocity in SI units."
    )
    ans = f"{_fmt_tex(speed_ms)} m*s^-1 {dir_heading}"
    sol = (
        f"1. **Instantaneous velocity** is the rate of change of position at a specific moment in time ($v = \\lim_{{\\Delta t \\to 0}} \\frac{{\\Delta x}}{{\\Delta t}}$).\n"
        f"2. To convert from $\\text{{km/h}}$ to $\\text{{m/s}}$, divide by $3{{,}}6$:\n"
        f"   $\\text{{Speed}} = \\frac{{{speed_kmh}}}{{3{{,}}6}} = {_fmt_tex(speed_ms)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"3. Instantaneous velocity = **${_fmt_tex(speed_ms)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ {dir_heading}**."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of instantaneous velocity", "marks": 1},
        {"step": 2, "criterion": f"Conversion to m/s = {_fmt_tex(speed_ms)}", "marks": 1},
        {"step": 3, "criterion": f"Stated magnitude and direction {dir_heading}", "marks": 1},
    ]
    hints = {
        "tier_1": "Divide km/h by 3.6 to get m/s.",
        "tier_2": f"{speed_kmh} / 3.6 = {_fmt(speed_ms)} m/s.",
        "tier_3": ans,
    }
    return _make_q(r, "05_instantaneous_speed_vs_velocity", 5, prompt, ans, sol, 3, ["multiplied_by_3_point_6_instead_of_dividing"], rubric, hints)


# ============================================================================ #
# 06. Acceleration definition and calculation
# ============================================================================ #
def build_06_acceleration_definition_and_calculation(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([0, 5, 10, 12])
    vf = vi + r.choice([15, 20, 25, 30])
    dt = r.choice([4, 5, 6, 8, 10])
    a = round((vf - vi) / dt, 2)
    direction = r.choice(["east", "forward"])

    prompt = (
        f"A motorcycle accelerates uniformly from an initial velocity of ${vi}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"to a final velocity of ${vf}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ due {direction} in ${dt}\\text{{ seconds}}$.\n\n"
        f"1. Define the term *acceleration*.\n"
        f"2. Calculate the acceleration of the motorcycle."
    )
    ans = f"{_fmt_tex(a)} m*s^-2 {direction}"
    sol = (
        f"1. **Acceleration** is defined as the rate of change of velocity ($a = \\frac{{\\Delta v}}{{\\Delta t}}$).\n"
        f"2. $a = \\frac{{v_f - v_i}}{{\\Delta t}} = \\frac{{{vf} - {vi}}}{{{dt}}} = \\frac{{{vf - vi}}}{{{dt}}} = "
        f"{_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ due {direction}."
    )
    rubric = [
        {"step": 1, "criterion": "Definition: rate of change of velocity", "marks": 1},
        {"step": 2, "criterion": "Formula a = (vf - vi) / dt", "marks": 1},
        {"step": 3, "criterion": f"Answer a = {_fmt_tex(a)} m*s^-2 with direction {direction}", "marks": 2},
    ]
    hints = {
        "tier_1": "a = (vf - vi) / Delta t.",
        "tier_2": f"a = ({vf} - {vi}) / {dt}.",
        "tier_3": ans,
    }
    return _make_q(r, "06_acceleration_definition_and_calculation", 6, prompt, ans, sol, 4, ["inverted_initial_and_final_velocities"], rubric, hints)


# ============================================================================ #
# 07. Positive, negative acceleration and deceleration
# ============================================================================ #
def build_07_positive_negative_acceleration_and_deceleration(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([25, 30, 35, 40])
    dt = r.choice([5, 6, 8, 10])
    vf = 0
    a = round((vf - vi) / dt, 2)
    dir_forward = "east"

    prompt = (
        f"A truck travels at ${vi}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ due {dir_forward}. The driver applies the brakes "
        f"and the truck comes to a complete standstill in ${dt}\\text{{ s}}$.\n\n"
        f"1. Taking {dir_forward} as the positive direction, calculate the acceleration ($a$) of the truck.\n"
        f"2. Explain the physical meaning of the negative sign in your calculated acceleration value.\n"
        f"3. Differentiate between *negative acceleration* and *deceleration*."
    )
    ans = f"{_fmt_tex(a)} m*s^-2 ({_fmt_tex(abs(a))} m*s^-2 west)"
    sol = (
        f"1. Taking {dir_forward} as positive ($+$):\n"
        f"   $a = \\frac{{v_f - v_i}}{{\\Delta t}} = \\frac{{0 - {vi}}}{{{dt}}} = {_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ "
        f"(or ${_fmt_tex(abs(a))}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ west).\n"
        f"2. The negative sign indicates that the acceleration vector points opposite to the chosen positive direction (west).\n"
        f"3. **Deceleration** means that the object's speed is decreasing (velocity and acceleration have opposite signs). "
        f"**Negative acceleration** simply means the acceleration vector points in the negative coordinate direction."
    )
    rubric = [
        {"step": 1, "criterion": f"Calculated a = {_fmt_tex(a)} m*s^-2", "marks": 2},
        {"step": 2, "criterion": "Explanation of negative sign indicating westward direction", "marks": 1},
        {"step": 3, "criterion": "Difference between deceleration (slowing down) and negative acceleration", "marks": 2},
    ]
    hints = {
        "tier_1": "vf = 0 m/s when coming to rest.",
        "tier_2": f"a = (0 - {vi}) / {dt} = {_fmt(a)} m/s^2.",
        "tier_3": ans,
    }
    return _make_q(r, "07_positive_negative_acceleration_and_deceleration", 7, prompt, ans, sol, 5, ["confused_negative_acceleration_with_deceleration"], rubric, hints)


# ============================================================================ #
# 08. Equation of motion: vf from vi, a, t
# ============================================================================ #
def build_08_equation_motion_vf_from_vi_a_t(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([4.0, 6.0, 8.0, 12.0])
    a = r.choice([1.5, 2.0, 2.5, 3.2])
    t = r.choice([4.0, 5.0, 6.0, 7.5])
    vf = round(vi + a * t, 2)

    prompt = (
        f"A sports car travelling at an initial velocity of ${vi}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ accelerates "
        f"at a constant rate of ${_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ forward for ${_fmt_tex(t)}\\text{{ s}}$.\n\n"
        f"Calculate the final velocity ($v_f$) of the car at the end of this time interval."
    )
    ans = f"{_fmt_tex(vf)} m*s^-1 forward"
    sol = (
        f"$v_f = v_i + a \\Delta t$\n"
        f"$v_f = {vi} + ({_fmt_tex(a)})({_fmt_tex(t)}) = {vi} + {round(a*t, 2)} = {_fmt_tex(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ forward."
    )
    rubric = [
        {"step": 1, "criterion": "Formula vf = vi + a * dt", "marks": 1},
        {"step": 2, "criterion": "Correct substitution", "marks": 1},
        {"step": 3, "criterion": f"Final velocity vf = {_fmt_tex(vf)} m*s^-1 with direction", "marks": 1},
    ]
    hints = {
        "tier_1": "Use vf = vi + a*Delta t.",
        "tier_2": f"vf = {vi} + ({_fmt(a)} * {_fmt(t)}).",
        "tier_3": ans,
    }
    return _make_q(r, "08_equation_motion_vf_from_vi_a_t", 8, prompt, ans, sol, 3, ["forgot_initial_velocity"], rubric, hints)


# ============================================================================ #
# 09. Equation of motion: Delta x from vi, a, t
# ============================================================================ #
def build_09_equation_motion_deltax_from_vi_a_t(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([0.0, 5.0, 10.0, 15.0])
    a = r.choice([1.2, 1.8, 2.0, 2.5, 3.0])
    t = r.choice([4.0, 5.0, 6.0, 8.0])
    term1 = vi * t
    term2 = 0.5 * a * (t**2)
    dx = round(term1 + term2, 2)

    prompt = (
        f"A passenger train travelling at ${vi}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ accelerates uniformly forward at "
        f"${_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ for ${_fmt_tex(t)}\\text{{ s}}$.\n\n"
        f"Calculate the displacement ($\\Delta x$) covered by the train during the acceleration phase."
    )
    ans = f"{_fmt_tex(dx)} m forward"
    sol = (
        f"$\\Delta x = v_i \\Delta t + \\frac{{1}}{{2}} a (\\Delta t)^2$\n"
        f"$\\Delta x = ({vi})({_fmt_tex(t)}) + \\frac{{1}}{{2}}({_fmt_tex(a)})({_fmt_tex(t)})^2$\n"
        f"$\\Delta x = {_fmt_tex(term1)} + {_fmt_tex(term2)} = {_fmt_tex(dx)}\\text{{ m}}$ forward."
    )
    rubric = [
        {"step": 1, "criterion": "Formula Delta x = vi*dt + 0.5*a*dt^2", "marks": 1},
        {"step": 2, "criterion": "Substitution of given values", "marks": 1},
        {"step": 3, "criterion": f"Answer Delta x = {_fmt_tex(dx)} m", "marks": 1},
    ]
    hints = {
        "tier_1": "Delta x = vi*Delta t + 0.5*a*(Delta t)^2.",
        "tier_2": f"Remember to square the time: ({_fmt(t)})^2 = {_fmt(t**2)}.",
        "tier_3": ans,
    }
    return _make_q(r, "09_equation_motion_deltax_from_vi_a_t", 9, prompt, ans, sol, 3, ["forgot_squaring_time_in_kinematics"], rubric, hints)


# ============================================================================ #
# 10. Equation of motion: vf^2 from vi, a, Delta x
# ============================================================================ #
def build_10_equation_motion_vf2_from_vi_a_deltax(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([0.0, 4.0, 8.0, 10.0])
    a = r.choice([1.5, 2.0, 3.0, 4.0])
    dx = r.choice([25.0, 50.0, 75.0, 100.0])
    vf_sq = vi**2 + 2 * a * dx
    vf = round(math.sqrt(vf_sq), 2)

    prompt = (
        f"A go-kart starts from an initial speed of ${vi}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ and accelerates forward "
        f"at ${_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ along a straight track of length ${_fmt_tex(dx)}\\text{{ m}}$.\n\n"
        f"Calculate the speed ($v_f$) of the go-kart at the end of the track."
    )
    ans = f"{_fmt_tex(vf)} m*s^-1"
    sol = (
        f"$v_f^2 = v_i^2 + 2 a \\Delta x$\n"
        f"$v_f^2 = ({vi})^2 + 2({_fmt_tex(a)})({_fmt_tex(dx)})$\n"
        f"$v_f^2 = {vi**2} + {round(2*a*dx, 2)} = {_fmt_tex(vf_sq)}\\text{{ m}}^2\\cdot\\text{{s}}^{{-2}}$\n"
        f"$v_f = \\sqrt{{{_fmt_tex(vf_sq)}}} = {_fmt_tex(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula vf^2 = vi^2 + 2*a*Delta x", "marks": 1},
        {"step": 2, "criterion": "Substitution of values", "marks": 1},
        {"step": 3, "criterion": f"Calculated vf = {_fmt_tex(vf)} m/s", "marks": 1},
    ]
    hints = {
        "tier_1": "Use vf^2 = vi^2 + 2*a*Delta x when time is not given.",
        "tier_2": f"vf = sqrt({vi**2} + 2*{_fmt(a)}*{_fmt(dx)}).",
        "tier_3": ans,
    }
    return _make_q(r, "10_equation_motion_vf2_from_vi_a_deltax", 10, prompt, ans, sol, 3, ["forgot_square_root_vf"], rubric, hints)


# ============================================================================ #
# 11. Equation of motion: Delta x from average velocity and t
# ============================================================================ #
def build_11_equation_motion_deltax_from_average_velocity_t(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([10.0, 12.0, 16.0, 20.0])
    vf = vi + r.choice([10.0, 14.0, 18.0, 24.0])
    t = r.choice([5.0, 6.0, 8.0, 10.0])
    v_avg = (vi + vf) / 2.0
    dx = round(v_avg * t, 2)

    prompt = (
        f"A racing car enters a straight section at an initial velocity of ${vi}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"and reaches ${vf}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ forward after ${_fmt_tex(t)}\\text{{ s}}$ under uniform acceleration.\n\n"
        f"Calculate the displacement ($\\Delta x$) of the car using the average velocity equation of motion."
    )
    ans = f"{_fmt_tex(dx)} m forward"
    sol = (
        f"$\\Delta x = \\left(\\frac{{v_i + v_f}}{{2}}\\right) \\Delta t$\n"
        f"$\\Delta x = \\left(\\frac{{{vi} + {vf}}}{{2}}\\right)({_fmt_tex(t)}) = ({_fmt_tex(v_avg)})({_fmt_tex(t)}) = {_fmt_tex(dx)}\\text{{ m}}$ forward."
    )
    rubric = [
        {"step": 1, "criterion": "Formula Delta x = ((vi + vf) / 2) * dt", "marks": 1},
        {"step": 2, "criterion": "Substitution of vi, vf, dt", "marks": 1},
        {"step": 3, "criterion": f"Answer Delta x = {_fmt_tex(dx)} m forward", "marks": 1},
    ]
    hints = {
        "tier_1": "Delta x = ((vi + vf) / 2) * Delta t.",
        "tier_2": f"Average velocity = ({vi} + {vf}) / 2 = {_fmt(v_avg)} m/s.",
        "tier_3": ans,
    }
    return _make_q(r, "11_equation_motion_deltax_from_average_velocity_t", 11, prompt, ans, sol, 3, ["forgot_halving_in_average_velocity"], rubric, hints)


# ============================================================================ #
# 12. Kinematics solve for time interval
# ============================================================================ #
def build_12_kinematics_solve_for_time_interval(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([20.0, 24.0, 28.0, 32.0])
    vf = r.choice([4.0, 6.0, 8.0, 10.0])
    a_mag = r.choice([2.0, 2.5, 3.0, 4.0])
    a = -a_mag
    t = round((vf - vi) / a, 2)

    prompt = (
        f"A car travelling at ${vi}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ slows down to ${vf}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"at a constant deceleration of ${_fmt_tex(a_mag)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$.\n\n"
        f"Calculate the time taken ($\\Delta t$) for this speed reduction."
    )
    ans = f"{_fmt_tex(t)} s"
    sol = (
        f"Taking forward as positive: $v_i = {vi}\\text{{ m/s}}$, $v_f = {vf}\\text{{ m/s}}$, $a = -{_fmt_tex(a_mag)}\\text{{ m/s}}^2$.\n"
        f"$v_f = v_i + a \\Delta t$\n"
        f"${vf} = {vi} + (-{_fmt_tex(a_mag)}) \\Delta t$\n"
        f"${vf} - {vi} = -{_fmt_tex(a_mag)} \\Delta t$\n"
        f"${vf - vi} = -{_fmt_tex(a_mag)} \\Delta t$\n"
        f"$\\Delta t = \\frac{{{vf - vi}}}{{-{_fmt_tex(a_mag)}}} = {_fmt_tex(t)}\\text{{ s}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula vf = vi + a*dt with negative acceleration for deceleration", "marks": 1},
        {"step": 2, "criterion": "Correct algebraic rearrangement", "marks": 1},
        {"step": 3, "criterion": f"Answer dt = {_fmt_tex(t)} s", "marks": 1},
    ]
    hints = {
        "tier_1": "Because the car is slowing down, acceleration is negative: a = -a_mag.",
        "tier_2": f"Delta t = (vf - vi) / a = ({vf} - {vi}) / (-{_fmt(a_mag)}).",
        "tier_3": ans,
    }
    return _make_q(r, "12_kinematics_solve_for_time_interval", 12, prompt, ans, sol, 3, ["negative_time_due_to_sign_error"], rubric, hints)


# ============================================================================ #
# 13. Kinematics solve for uniform acceleration
# ============================================================================ #
def build_13_kinematics_solve_for_uniform_acceleration(r: random.Random) -> Dict[str, Any]:
    vi = 0.0
    dx = r.choice([60.0, 90.0, 120.0, 150.0])
    t = r.choice([5.0, 6.0, 8.0, 10.0])
    # dx = 0.5 * a * t^2 => a = 2*dx / t^2
    a = round((2 * dx) / (t**2), 2)

    prompt = (
        f"An electric vehicle accelerates uniformly from rest along a test strip, covering a distance of "
        f"${_fmt_tex(dx)}\\text{{ m}}$ in ${_fmt_tex(t)}\\text{{ s}}$.\n\n"
        f"Calculate the acceleration ($a$) of the vehicle."
    )
    ans = f"{_fmt_tex(a)} m*s^-2"
    sol = (
        f"$\\Delta x = v_i \\Delta t + \\frac{{1}}{{2}} a (\\Delta t)^2$\n"
        f"Since $v_i = 0$:\n"
        f"${_fmt_tex(dx)} = 0 + \\frac{{1}}{{2}} a ({_fmt_tex(t)})^2\n"
        f"${_fmt_tex(dx)} = {round(0.5*(t**2), 2)} a\n"
        f"$a = \\frac{{{_fmt_tex(dx)}}}{{{round(0.5*(t**2), 2)}}} = {_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula Delta x = 0.5*a*dt^2 (vi = 0)", "marks": 1},
        {"step": 2, "criterion": f"Substitution: {_fmt_tex(dx)} = 0.5 * a * ({_fmt_tex(t)})^2", "marks": 1},
        {"step": 3, "criterion": f"Answer a = {_fmt_tex(a)} m*s^-2", "marks": 1},
    ]
    hints = {
        "tier_1": "From rest means vi = 0. So Delta x = 0.5 * a * t^2.",
        "tier_2": f"a = 2 * Delta x / t^2 = 2 * {_fmt(dx)} / ({_fmt(t)})^2.",
        "tier_3": ans,
    }
    return _make_q(r, "13_kinematics_solve_for_uniform_acceleration", 13, prompt, ans, sol, 3, ["forgot_factor_of_half"], rubric, hints)


# ============================================================================ #
# 14. Kinematics solve for initial velocity
# ============================================================================ #
def build_14_kinematics_solve_for_initial_velocity(r: random.Random) -> Dict[str, Any]:
    vf = r.choice([25.0, 30.0, 35.0, 40.0])
    a = r.choice([2.0, 2.5, 3.0])
    t = r.choice([4.0, 5.0, 6.0])
    vi = round(vf - a * t, 2)

    prompt = (
        f"An airplane touches down on a runway and accelerates forwards at ${_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ "
        f"for ${_fmt_tex(t)}\\text{{ s}}$, reaching a speed of ${_fmt_tex(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n\n"
        f"Calculate the initial speed ($v_i$) of the airplane at the start of this ${_fmt_tex(t)}\\text{{ s}}$ interval."
    )
    ans = f"{_fmt_tex(vi)} m*s^-1"
    sol = (
        f"$v_f = v_i + a \\Delta t$\n"
        f"${_fmt_tex(vf)} = v_i + ({_fmt_tex(a)})({_fmt_tex(t)})$\n"
        f"${_fmt_tex(vf)} = v_i + {round(a*t, 2)}$\n"
        f"$v_i = {_fmt_tex(vf)} - {round(a*t, 2)} = {_fmt_tex(vi)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula vf = vi + a*dt", "marks": 1},
        {"step": 2, "criterion": f"Substitution: {_fmt_tex(vf)} = vi + {_fmt_tex(a)} * {_fmt_tex(t)}", "marks": 1},
        {"step": 3, "criterion": f"Answer vi = {_fmt_tex(vi)} m*s^-1", "marks": 1},
    ]
    hints = {
        "tier_1": "vi = vf - a*Delta t.",
        "tier_2": f"vi = {_fmt(vf)} - ({_fmt(a)} * {_fmt(t)}).",
        "tier_3": ans,
    }
    return _make_q(r, "14_kinematics_solve_for_initial_velocity", 14, prompt, ans, sol, 3, ["added_a_t_instead_of_subtracting"], rubric, hints)


# ============================================================================ #
# 15. Stopping distance: reaction time and braking
# ============================================================================ #
def build_15_stopping_distance_reaction_time_and_braking(r: random.Random) -> Dict[str, Any]:
    speed_kmh = r.choice([72, 90, 108])
    speed_ms = round(speed_kmh / 3.6, 2)
    t_react = r.choice([0.6, 0.75, 0.8, 1.0])
    a_brake = r.choice([4.0, 5.0, 6.0])

    d_think = round(speed_ms * t_react, 2)
    d_brake = round((speed_ms**2) / (2 * a_brake), 2)
    d_total = round(d_think + d_brake, 2)

    prompt = (
        f"A motorist drives at ${speed_kmh}\\text{{ km}}\\cdot\\text{{h}}^{{-1}}$ along a straight road when a hazard "
        f"suddenly appears. The driver's reaction time is ${_fmt_tex(t_react)}\\text{{ s}}$, after which the brakes are "
        f"applied, producing a constant deceleration of ${_fmt_tex(a_brake)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ until "
        f"the vehicle stops.\n\n"
        f"1. Convert ${speed_kmh}\\text{{ km}}\\cdot\\text{{h}}^{{-1}}$ to $\\text{{m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"2. Calculate the 'thinking distance' (distance covered during the driver's reaction time).\n"
        f"3. Calculate the braking distance of the car.\n"
        f"4. Calculate the total stopping distance."
    )
    ans = f"Stopping distance = {d_total} m"
    sol = (
        f"1. $v = \\frac{{{speed_kmh}}}{{3{{,}}6}} = {_fmt_tex(speed_ms)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"2. During reaction time, speed is constant ($a = 0$):\n"
        f"   $d_{{\\text{{think}}}} = v \\times t_{{\\text{{react}}}} = {_fmt_tex(speed_ms)} \\times {_fmt_tex(t_react)} = {_fmt_tex(d_think)}\\text{{ m}}$.\n"
        f"3. During braking: $v_i = {_fmt_tex(speed_ms)}\\text{{ m/s}}$, $v_f = 0$, $a = -{_fmt_tex(a_brake)}\\text{{ m/s}}^2$:\n"
        f"   $v_f^2 = v_i^2 + 2 a d_{{\\text{{brake}}}}$\n"
        f"   $0 = ({_fmt_tex(speed_ms)})^2 + 2(-{_fmt_tex(a_brake)}) d_{{\\text{{brake}}}}$\n"
        f"   $2({_fmt_tex(a_brake)}) d_{{\\text{{brake}}}} = {round(speed_ms**2, 2)}$\n"
        f"   $d_{{\\text{{brake}}}} = \\frac{{{round(speed_ms**2, 2)}}}{{{2*a_brake}}} = {_fmt_tex(d_brake)}\\text{{ m}}$.\n"
        f"4. Total stopping distance $= d_{{\\text{{think}}}} + d_{{\\text{{brake}}}} = {_fmt_tex(d_think)} + {_fmt_tex(d_brake)} = {_fmt_tex(d_total)}\\text{{ m}}$."
    )
    rubric = [
        {"step": 1, "criterion": f"Speed conversion to {_fmt_tex(speed_ms)} m/s", "marks": 1},
        {"step": 2, "criterion": f"Thinking distance = {_fmt_tex(d_think)} m", "marks": 1},
        {"step": 3, "criterion": f"Braking distance = {_fmt_tex(d_brake)} m", "marks": 2},
        {"step": 4, "criterion": f"Total stopping distance = {_fmt_tex(d_total)} m", "marks": 1},
    ]
    hints = {
        "tier_1": "Total stopping distance = thinking distance + braking distance.",
        "tier_2": "Thinking distance = v * t_react; Braking distance from vf^2 = vi^2 + 2*a*dx.",
        "tier_3": ans,
    }
    return _make_q(r, "15_stopping_distance_reaction_time_and_braking", 15, prompt, ans, sol, 5, ["ignored_reaction_time"], rubric, hints)


# ============================================================================ #
# 16. Two-stage motion: acceleration then constant velocity
# ============================================================================ #
def build_16_two_stage_motion_acceleration_then_constant_velocity(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2.0, 2.5, 3.0])
    t1 = r.choice([4.0, 5.0, 6.0])
    t2 = r.choice([8.0, 10.0, 12.0])

    v_const = round(a * t1, 2)
    dx1 = round(0.5 * a * (t1**2), 2)
    dx2 = round(v_const * t2, 2)
    dx_total = round(dx1 + dx2, 2)

    prompt = (
        f"A cyclist starts from rest ($v_i = 0$) and accelerates uniformly at ${_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ "
        f"for ${_fmt_tex(t1)}\\text{{ s}}$. She then continues riding at this achieved speed for a further ${_fmt_tex(t2)}\\text{{ s}}$.\n\n"
        f"1. Calculate the speed achieved by the cyclist at the end of the first ${_fmt_tex(t1)}\\text{{ s}}$.\n"
        f"2. Calculate the distance covered during Stage 1.\n"
        f"3. Calculate the distance covered during Stage 2.\n"
        f"4. Calculate the total distance covered over the entire motion."
    )
    ans = f"Total distance = {dx_total} m"
    sol = (
        f"1. **Stage 1 (Acceleration):**\n"
        f"   $v_f = v_i + a \\Delta t_1 = 0 + ({_fmt_tex(a)})({_fmt_tex(t1)}) = {_fmt_tex(v_const)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"2. $\\Delta x_1 = v_i \\Delta t_1 + \\frac{{1}}{{2}} a (\\Delta t_1)^2 = 0 + \\frac{{1}}{{2}}({_fmt_tex(a)})({_fmt_tex(t1)})^2 = {_fmt_tex(dx1)}\\text{{ m}}$.\n"
        f"3. **Stage 2 (Constant speed):**\n"
        f"   $\\Delta x_2 = v \\times \\Delta t_2 = {_fmt_tex(v_const)} \\times {_fmt_tex(t2)} = {_fmt_tex(dx2)}\\text{{ m}}$.\n"
        f"4. $\\text{{Total distance}} = \\Delta x_1 + \\Delta x_2 = {_fmt_tex(dx1)} + {_fmt_tex(dx2)} = {_fmt_tex(dx_total)}\\text{{ m}}$."
    )
    rubric = [
        {"step": 1, "criterion": f"Calculated max speed = {_fmt_tex(v_const)} m/s", "marks": 1},
        {"step": 2, "criterion": f"Distance stage 1 = {_fmt_tex(dx1)} m", "marks": 1},
        {"step": 3, "criterion": f"Distance stage 2 = {_fmt_tex(dx2)} m", "marks": 1},
        {"step": 4, "criterion": f"Total distance = {_fmt_tex(dx_total)} m", "marks": 1},
    ]
    hints = {
        "tier_1": "Calculate each stage separately: Stage 1 has a = const; Stage 2 has a = 0.",
        "tier_2": f"v1 = a*t1 = {_fmt(v_const)} m/s. dx1 = 0.5*a*t1^2. dx2 = v1*t2.",
        "tier_3": ans,
    }
    return _make_q(r, "16_two_stage_motion_acceleration_then_constant_velocity", 16, prompt, ans, sol, 4, ["applied_acceleration_formula_to_stage_2"], rubric, hints)


# ============================================================================ #
# 17. Two-stage motion: constant velocity then braking
# ============================================================================ #
def build_17_two_stage_motion_constant_velocity_then_braking(r: random.Random) -> Dict[str, Any]:
    v_init = r.choice([15.0, 18.0, 20.0, 24.0])
    t1 = r.choice([4.0, 5.0, 6.0])
    a_brake = r.choice([2.5, 3.0, 4.0])

    dx1 = round(v_init * t1, 2)
    # v_f = 0 => dx2 = v_init^2 / (2 * a_brake)
    dx2 = round((v_init**2) / (2 * a_brake), 2)
    t_brake = round(v_init / a_brake, 2)
    dx_total = round(dx1 + dx2, 2)

    prompt = (
        f"A car cruises at a steady ${_fmt_tex(v_init)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ for ${_fmt_tex(t1)}\\text{{ s}}$. "
        f"The brakes are then engaged, causing the car to decelerate uniformly at ${_fmt_tex(a_brake)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$ "
        f"until it stops.\n\n"
        f"1. Calculate the distance covered while cruising at constant velocity.\n"
        f"2. Calculate the distance covered while braking to a halt.\n"
        f"3. Calculate the total time taken from the beginning of cruising until the car stops."
    )
    ans = f"Total distance = {dx_total} m, Total time = {round(t1 + t_brake, 2)} s"
    sol = (
        f"1. **Stage 1 (Cruising):** $\\Delta x_1 = v \\Delta t_1 = {_fmt_tex(v_init)} \\times {_fmt_tex(t1)} = {_fmt_tex(dx1)}\\text{{ m}}$.\n"
        f"2. **Stage 2 (Braking):** $v_f^2 = v_i^2 + 2 a \\Delta x_2$\n"
        f"   $0 = ({_fmt_tex(v_init)})^2 + 2(-{_fmt_tex(a_brake)}) \\Delta x_2 \\implies "
        f"\\Delta x_2 = \\frac{{{round(v_init**2, 2)}}}{{{2*a_brake}}} = {_fmt_tex(dx2)}\\text{{ m}}$.\n"
        f"3. Braking time: $v_f = v_i + a \\Delta t_2 \\implies 0 = {_fmt_tex(v_init)} - {_fmt_tex(a_brake)} \\Delta t_2 "
        f"\\implies \\Delta t_2 = \\frac{{{_fmt_tex(v_init)}}}{{{_fmt_tex(a_brake)}}} = {_fmt_tex(t_brake)}\\text{{ s}}$.\n"
        f"   $\\text{{Total time}} = \\Delta t_1 + \\Delta t_2 = {_fmt_tex(t1)} + {_fmt_tex(t_brake)} = {_fmt_tex(round(t1 + t_brake, 2))}\\text{{ s}}$."
    )
    rubric = [
        {"step": 1, "criterion": f"Cruising distance = {_fmt_tex(dx1)} m", "marks": 1},
        {"step": 2, "criterion": f"Braking distance = {_fmt_tex(dx2)} m", "marks": 2},
        {"step": 3, "criterion": f"Total time = {_fmt_tex(round(t1 + t_brake, 2))} s", "marks": 2},
    ]
    hints = {
        "tier_1": "Braking distance is found from vf^2 = vi^2 + 2*a*dx.",
        "tier_2": f"dx1 = {dx1} m; dx2 = {v_init}^2 / (2 * {a_brake}) = {dx2} m.",
        "tier_3": ans,
    }
    return _make_q(r, "17_two_stage_motion_constant_velocity_then_braking", 17, prompt, ans, sol, 5, ["confused_two_different_time_stages"], rubric, hints)


# ============================================================================ #
# 18. Position-time graph interpretation: constant velocity
# ============================================================================ #
def build_18_position_time_graph_constant_velocity_interpretation(r: random.Random) -> Dict[str, Any]:
    v = r.choice([3.0, 4.0, 5.0, 6.0])
    t1 = r.choice([4, 5, 6])
    t2 = t1 + r.choice([3, 4, 5])
    t3 = t2 + r.choice([4, 5])
    x1 = round(v * t1, 1)

    svg = f"""<svg viewBox="0 0 500 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="280" fill="#F8FAFC" />
  <line x1="60" y1="230" x2="460" y2="230" stroke="#0F172A" stroke-width="2" />
  <line x1="60" y1="230" x2="60" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="460" y="255" font-size="12" fill="#0F172A" text-anchor="end">Time t (s)</text>
  <text x="45" y="35" font-size="12" fill="#0F172A" text-anchor="middle">x (m)</text>
  <line x1="60" y1="230" x2="{60 + t1 * 20}" y2="{230 - int(x1 * 4)}" stroke="#2563EB" stroke-width="3" />
  <line x1="{60 + t1 * 20}" y1="{230 - int(x1 * 4)}" x2="{60 + t2 * 20}" y2="{230 - int(x1 * 4)}" stroke="#2563EB" stroke-width="3" />
  <line x1="{60 + t2 * 20}" y1="{230 - int(x1 * 4)}" x2="{60 + t3 * 20}" y2="230" stroke="#2563EB" stroke-width="3" />
  <text x="{60 + t1 * 20}" y="248" font-size="11" fill="#475569" text-anchor="middle">{t1}</text>
  <text x="{60 + t2 * 20}" y="248" font-size="11" fill="#475569" text-anchor="middle">{t2}</text>
  <text x="{60 + t3 * 20}" y="248" font-size="11" fill="#475569" text-anchor="middle">{t3}</text>
  <text x="45" y="{235 - int(x1 * 4)}" font-size="11" fill="#475569" text-anchor="end">{_fmt(x1)}</text>
  <line x1="60" y1="{230 - int(x1 * 4)}" x2="{60 + t2 * 20}" y2="{230 - int(x1 * 4)}" stroke="#CBD5E1" stroke-dasharray="4,4" />
</svg>"""

    v_return = round(-x1 / (t3 - t2), 2)

    prompt = (
        f"Refer to the position-time ($x-t$) graph shown in the figure for a toy car moving along a straight track.\n\n"
        f"1. What physical quantity is represented by the gradient (slope) of a position-time graph?\n"
        f"2. Describe the motion of the car during the interval from $t = {t1}\\text{{ s}}$ to $t = {t2}\\text{{ s}}$.\n"
        f"3. Calculate the velocity of the car during the first ${t1}\\text{{ s}}$ ($t = 0$ to $t = {t1}\\text{{ s}}$).\n"
        f"4. Calculate the velocity of the car during the final interval from $t = {t2}\\text{{ s}}$ to $t = {t3}\\text{{ s}}$."
    )
    ans = f"1. Velocity; 2. Stationary; 3. +{_fmt_tex(v)} m*s^-1; 4. {_fmt_tex(v_return)} m*s^-1"
    sol = (
        f"1. The gradient of an $x-t$ graph represents **velocity** ($v = \\frac{{\\Delta x}}{{\\Delta t}}$).\n"
        f"2. From $t = {t1}\\text{{ s}}$ to $t = {t2}\\text{{ s}}$, the graph is a horizontal line (gradient $= 0$), "
        f"meaning the car is **stationary** (at rest at position $x = {_fmt_tex(x1)}\\text{{ m}}$).\n"
        f"3. Interval $0$ to ${t1}\\text{{ s}}$:\n"
        f"   $v = \\frac{{\\Delta x}}{{\\Delta t}} = \\frac{{{_fmt_tex(x1)} - 0}}{{{t1} - 0}} = {_fmt_tex(v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"4. Interval ${t2}\\text{{ s}}$ to ${t3}\\text{{ s}}$:\n"
        f"   $v = \\frac{{0 - {_fmt_tex(x1)}}}{{{t3} - {t2}}} = \\frac{{-{_fmt_tex(x1)}}}{{{t3 - t2}}} = {_fmt_tex(v_return)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ "
        f"(moving in the negative direction back to the origin)."
    )
    rubric = [
        {"step": 1, "criterion": "Identified gradient as velocity", "marks": 1},
        {"step": 2, "criterion": "Described motion as stationary / at rest", "marks": 1},
        {"step": 3, "criterion": f"Calculated forward velocity = +{_fmt_tex(v)} m/s", "marks": 1},
        {"step": 4, "criterion": f"Calculated return velocity = {_fmt_tex(v_return)} m/s", "marks": 2},
    ]
    hints = {
        "tier_1": "Gradient = Delta x / Delta t = velocity. Horizontal line means object is not moving.",
        "tier_2": f"v1 = {x1} / {t1} = {_fmt(v)} m/s. Return v = (0 - {x1}) / ({t3} - {t2}).",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "18_position_time_graph_constant_velocity_interpretation", 18, prompt, ans, sol, 5, ["confused_position_time_with_velocity_time"], rubric, hints, spec)


# ============================================================================ #
# 19. Position-time graph: accelerating motion
# ============================================================================ #
def build_19_position_time_graph_accelerating_motion(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1.0, 1.5, 2.0])
    t_end = r.choice([4, 6, 8])
    x_end = round(0.5 * a * (t_end**2), 1)

    svg = f"""<svg viewBox="0 0 500 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="280" fill="#F8FAFC" />
  <line x1="60" y1="230" x2="460" y2="230" stroke="#0F172A" stroke-width="2" />
  <line x1="60" y1="230" x2="60" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="460" y="255" font-size="12" fill="#0F172A" text-anchor="end">Time t (s)</text>
  <text x="45" y="35" font-size="12" fill="#0F172A" text-anchor="middle">x (m)</text>
  <path d="M 60 230 Q 220 220 400 60" fill="none" stroke="#DC2626" stroke-width="3" />
  <circle cx="400" cy="60" r="4" fill="#DC2626" />
  <text x="400" y="248" font-size="11" fill="#475569" text-anchor="middle">{t_end}</text>
  <text x="45" y="65" font-size="11" fill="#475569" text-anchor="end">{_fmt(x_end)}</text>
  <line x1="60" y1="60" x2="400" y2="60" stroke="#CBD5E1" stroke-dasharray="4,4" />
  <line x1="400" y1="60" x2="400" y2="230" stroke="#CBD5E1" stroke-dasharray="4,4" />
</svg>"""

    v_final = round(a * t_end, 2)

    prompt = (
        f"Refer to the position-time graph shown in the figure for an object starting from rest at $t = 0$.\n\n"
        f"1. Explain why the curved shape of this graph indicates that the object is accelerating.\n"
        f"2. Given that the acceleration is constant and the object reaches $x = {_fmt_tex(x_end)}\\text{{ m}}$ "
        f"at $t = {t_end}\\text{{ s}}$, calculate the uniform acceleration ($a$).\n"
        f"3. Calculate the instantaneous velocity at $t = {t_end}\\text{{ s}}$."
    )
    ans = f"a = {_fmt_tex(a)} m*s^-2, vf = {_fmt_tex(v_final)} m*s^-1"
    sol = (
        f"1. The gradient of the tangent to a position-time graph represents instantaneous velocity. "
        f"Because the slope gets steeper as time increases, the velocity is continuously increasing, which demonstrates acceleration.\n"
        f"2. $\\Delta x = v_i \\Delta t + \\frac{{1}}{{2}} a (\\Delta t)^2$\n"
        f"   Since $v_i = 0$:\n"
        f"   ${_fmt_tex(x_end)} = \\frac{{1}}{{2}} a ({t_end})^2 = \\frac{{1}}{{2}} a ({t_end**2}) = {round(0.5*(t_end**2), 1)} a$\n"
        f"   $a = \\frac{{{_fmt_tex(x_end)}}}{{{round(0.5*(t_end**2), 1)}}} = {_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$.\n"
        f"3. $v_f = v_i + a \\Delta t = 0 + ({_fmt_tex(a)})({t_end}) = {_fmt_tex(v_final)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Explanation: increasing slope indicates increasing velocity", "marks": 1},
        {"step": 2, "criterion": f"Calculated a = {_fmt_tex(a)} m*s^-2", "marks": 2},
        {"step": 3, "criterion": f"Calculated vf = {_fmt_tex(v_final)} m*s^-1", "marks": 1},
    ]
    hints = {
        "tier_1": "Parabolic x-t curve means constant acceleration.",
        "tier_2": f"dx = 0.5 * a * t^2. So a = 2 * {x_end} / {t_end}^2.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "19_position_time_graph_accelerating_motion", 19, prompt, ans, sol, 4, ["thought_curved_graph_means_curved_path"], rubric, hints, spec)


# ============================================================================ #
# 20. Velocity-time graph gradient as acceleration
# ============================================================================ #
def build_20_velocity_time_graph_gradient_as_acceleration(r: random.Random) -> Dict[str, Any]:
    vi = r.choice([0, 4, 8])
    vf = vi + r.choice([12, 16, 20])
    dt = r.choice([4, 5, 8])
    a = round((vf - vi) / dt, 2)

    svg = f"""<svg viewBox="0 0 500 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="280" fill="#F8FAFC" />
  <line x1="60" y1="230" x2="460" y2="230" stroke="#0F172A" stroke-width="2" />
  <line x1="60" y1="230" x2="60" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="460" y="255" font-size="12" fill="#0F172A" text-anchor="end">Time t (s)</text>
  <text x="45" y="35" font-size="12" fill="#0F172A" text-anchor="middle">v (m/s)</text>
  <line x1="60" y1="{230 - vi * 7}" x2="{60 + dt * 40}" y2="{230 - vf * 7}" stroke="#059669" stroke-width="3" />
  <circle cx="60" cy="{230 - vi * 7}" r="4" fill="#059669" />
  <circle cx="{60 + dt * 40}" cy="{230 - vf * 7}" r="4" fill="#059669" />
  <text x="45" y="{235 - vi * 7}" font-size="11" fill="#475569" text-anchor="end">{vi}</text>
  <text x="45" y="{235 - vf * 7}" font-size="11" fill="#475569" text-anchor="end">{vf}</text>
  <text x="{60 + dt * 40}" y="248" font-size="11" fill="#475569" text-anchor="middle">{dt}</text>
  <line x1="60" y1="{230 - vf * 7}" x2="{60 + dt * 40}" y2="{230 - vf * 7}" stroke="#CBD5E1" stroke-dasharray="4,4" />
  <line x1="{60 + dt * 40}" y1="{230 - vf * 7}" x2="{60 + dt * 40}" y2="230" stroke="#CBD5E1" stroke-dasharray="4,4" />
</svg>"""

    prompt = (
        f"Refer to the velocity-time ($v-t$) graph shown in the figure for a moving vehicle.\n\n"
        f"1. State what physical quantity is represented by the gradient of a velocity-time graph.\n"
        f"2. Use coordinates from the graph to calculate the acceleration ($a$) of the vehicle.\n"
        f"3. State whether this motion represents uniform or non-uniform acceleration, giving a reason."
    )
    ans = f"Gradient = {_fmt_tex(a)} m*s^-2; Uniform acceleration (straight line)"
    sol = (
        f"1. The gradient of a velocity-time graph represents **acceleration** ($a = \\frac{{\\Delta v}}{{\\Delta t}}$).\n"
        f"2. Taking points $(0; {vi})$ and $({dt}; {vf})$:\n"
        f"   $\\text{{Gradient}} = \\frac{{{vf} - {vi}}}{{{dt} - 0}} = \\frac{{{vf - vi}}}{{{dt}}} = {_fmt_tex(a)}\\text{{ m}}\\cdot\\text{{s}}^{{-2}}$.\n"
        f"3. It represents **uniform acceleration** because the graph is a straight line with a constant gradient."
    )
    rubric = [
        {"step": 1, "criterion": "Identified gradient as acceleration", "marks": 1},
        {"step": 2, "criterion": f"Calculated gradient a = {_fmt_tex(a)} m*s^-2", "marks": 2},
        {"step": 3, "criterion": "Stated uniform acceleration due to straight line", "marks": 1},
    ]
    hints = {
        "tier_1": "Gradient = (y2 - y1) / (x2 - x1) = (vf - vi) / (t2 - t1).",
        "tier_2": f"Gradient = ({vf} - {vi}) / {dt} = {_fmt(a)} m/s^2.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "20_velocity_time_graph_gradient_as_acceleration", 20, prompt, ans, sol, 4, ["used_area_instead_of_gradient_for_acceleration"], rubric, hints, spec)


# ============================================================================ #
# 21. Velocity-time graph area as displacement (triangle)
# ============================================================================ #
def build_21_velocity_time_graph_area_as_displacement_triangle(r: random.Random) -> Dict[str, Any]:
    vf = r.choice([12, 16, 20, 24])
    dt = r.choice([5, 6, 8, 10])
    area = round(0.5 * dt * vf, 1)

    svg = f"""<svg viewBox="0 0 500 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="280" fill="#F8FAFC" />
  <line x1="60" y1="230" x2="460" y2="230" stroke="#0F172A" stroke-width="2" />
  <line x1="60" y1="230" x2="60" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="460" y="255" font-size="12" fill="#0F172A" text-anchor="end">Time t (s)</text>
  <text x="45" y="35" font-size="12" fill="#0F172A" text-anchor="middle">v (m/s)</text>
  <polygon points="60,230 {60 + dt * 35},230 {60 + dt * 35},{230 - vf * 7}" fill="#E0F2FE" />
  <line x1="60" y1="230" x2="{60 + dt * 35}" y2="{230 - vf * 7}" stroke="#0284C7" stroke-width="3" />
  <text x="{60 + dt * 35}" y="248" font-size="11" fill="#475569" text-anchor="middle">{dt}</text>
  <text x="45" y="{235 - vf * 7}" font-size="11" fill="#475569" text-anchor="end">{vf}</text>
  <line x1="60" y1="{230 - vf * 7}" x2="{60 + dt * 35}" y2="{230 - vf * 7}" stroke="#CBD5E1" stroke-dasharray="4,4" />
  <line x1="{60 + dt * 35}" y1="{230 - vf * 7}" x2="{60 + dt * 35}" y2="230" stroke="#CBD5E1" stroke-dasharray="4,4" />
</svg>"""

    prompt = (
        f"Refer to the velocity-time graph shown in the figure for a sprint runner accelerating uniformly from rest.\n\n"
        f"1. What physical quantity is represented by the area under a velocity-time graph?\n"
        f"2. Calculate the displacement ($\\Delta x$) covered by the runner in the first ${dt}\\text{{ s}}$ by finding the area under the graph."
    )
    ans = f"Area = {_fmt_tex(area)} m"
    sol = (
        f"1. The area under a velocity-time graph represents the **displacement** ($\\Delta x$) of the object.\n"
        f"2. The area under the graph forms a right-angled triangle with base $= {dt}\\text{{ s}}$ and height $= {vf}\\text{{ m/s}}$:\n"
        f"   $\\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} = \\frac{{1}}{{2}} \\times {dt} \\times {vf} = {_fmt_tex(area)}\\text{{ m}}$.\n"
        f"   Therefore, the displacement is **${_fmt_tex(area)}\\text{{ m}}$** forward."
    )
    rubric = [
        {"step": 1, "criterion": "Identified area as displacement", "marks": 1},
        {"step": 2, "criterion": "Triangle area formula 0.5 * base * height", "marks": 1},
        {"step": 3, "criterion": f"Calculated displacement = {_fmt_tex(area)} m", "marks": 1},
    ]
    hints = {
        "tier_1": "Area of triangle = 0.5 * base * height.",
        "tier_2": f"Area = 0.5 * {dt} * {vf} = {_fmt(area)} m.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "21_velocity_time_graph_area_as_displacement_triangle", 21, prompt, ans, sol, 3, ["forgot_half_in_triangle_area"], rubric, hints, spec)


# ============================================================================ #
# 22. Velocity-time graph area as displacement (trapezoid)
# ============================================================================ #
def build_22_velocity_time_graph_area_as_displacement_trapezoid(r: random.Random) -> Dict[str, Any]:
    t1 = r.choice([3, 4, 5])
    t2 = t1 + r.choice([4, 6, 8])
    t3 = t2 + r.choice([3, 4, 5])
    v_top = r.choice([10, 15, 20])

    area_tri1 = 0.5 * t1 * v_top
    area_rect = (t2 - t1) * v_top
    area_tri2 = 0.5 * (t3 - t2) * v_top
    total_area = round(area_tri1 + area_rect + area_tri2, 1)

    svg = f"""<svg viewBox="0 0 500 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="280" fill="#F8FAFC" />
  <line x1="60" y1="230" x2="460" y2="230" stroke="#0F172A" stroke-width="2" />
  <line x1="60" y1="230" x2="60" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="460" y="255" font-size="12" fill="#0F172A" text-anchor="end">Time t (s)</text>
  <text x="45" y="35" font-size="12" fill="#0F172A" text-anchor="middle">v (m/s)</text>
  <polygon points="60,230 {60 + t1 * 18},{230 - v_top * 8} {60 + t2 * 18},{230 - v_top * 8} {60 + t3 * 18},230" fill="#FEF3C7" />
  <line x1="60" y1="230" x2="{60 + t1 * 18}" y2="{230 - v_top * 8}" stroke="#D97706" stroke-width="3" />
  <line x1="{60 + t1 * 18}" y1="{230 - v_top * 8}" x2="{60 + t2 * 18}" y2="{230 - v_top * 8}" stroke="#D97706" stroke-width="3" />
  <line x1="{60 + t2 * 18}" y1="{230 - v_top * 8}" x2="{60 + t3 * 18}" y2="230" stroke="#D97706" stroke-width="3" />
  <text x="{60 + t1 * 18}" y="248" font-size="11" fill="#475569" text-anchor="middle">{t1}</text>
  <text x="{60 + t2 * 18}" y="248" font-size="11" fill="#475569" text-anchor="middle">{t2}</text>
  <text x="{60 + t3 * 18}" y="248" font-size="11" fill="#475569" text-anchor="middle">{t3}</text>
  <text x="45" y="{235 - v_top * 8}" font-size="11" fill="#475569" text-anchor="end">{v_top}</text>
</svg>"""

    prompt = (
        f"Refer to the trapezoidal velocity-time graph shown in the figure for a passenger lift ascending a shaft.\n\n"
        f"1. Calculate the total displacement ($\\Delta y$) of the lift from $t = 0$ to $t = {t3}\\text{{ s}}$ by determining the area of the trapezoid.\n"
        f"2. Calculate the average velocity of the lift over the entire ${t3}\\text{{ s}}$ trip."
    )
    v_avg = round(total_area / t3, 2)
    ans = f"Displacement = {_fmt_tex(total_area)} m, v_avg = {_fmt_tex(v_avg)} m*s^-1"
    sol = (
        f"1. Area of trapezoid = $\\frac{{1}}{{2}} \\times (\\text{{sum of parallel sides}}) \\times \\text{{height}}$\n"
        f"   Parallel sides: bottom base $= {t3}\\text{{ s}}$, top base $= {t2} - {t1} = {t2 - t1}\\text{{ s}}$. Height $= {v_top}\\text{{ m/s}}$.\n"
        f"   $\\Delta y = \\frac{{1}}{{2}} \\times ({t3} + {t2 - t1}) \\times {v_top} = \\frac{{1}}{{2}} \\times {t3 + t2 - t1} \\times {v_top} = {_fmt_tex(total_area)}\\text{{ m}}$.\n"
        f"   (Alternatively, Triangle 1 $= {_fmt_tex(area_tri1)} +$ Rectangle $= {_fmt_tex(area_rect)} +$ Triangle 2 $= {_fmt_tex(area_tri2)} = {_fmt_tex(total_area)}\\text{{ m}}$).\n"
        f"2. $v_{{\\text{{avg}}}} = \\frac{{\\Delta y}}{{\\Delta t}} = \\frac{{{_fmt_tex(total_area)}}}{{{t3}}} = {_fmt_tex(v_avg)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Trapezoid area formula or sum of geometric parts", "marks": 1},
        {"step": 2, "criterion": f"Calculated displacement = {_fmt_tex(total_area)} m", "marks": 2},
        {"step": 3, "criterion": f"Calculated v_avg = {_fmt_tex(v_avg)} m*s^-1", "marks": 1},
    ]
    hints = {
        "tier_1": "Area of trapezoid = 0.5 * (a + b) * h.",
        "tier_2": f"a = {t3}, b = {t2 - t1}, h = {v_top}.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "22_velocity_time_graph_area_as_displacement_trapezoid", 22, prompt, ans, sol, 4, ["used_wrong_parallel_side_length"], rubric, hints, spec)


# ============================================================================ #
# 23. Velocity-time graph: motion reversal and negative area
# ============================================================================ #
def build_23_velocity_time_graph_direction_reversal_negative_area(r: random.Random) -> Dict[str, Any]:
    v_fwd = r.choice([10, 12, 16])
    t_zero = r.choice([4, 5, 6])
    v_rev = -r.choice([6, 8, 10])
    t_end = t_zero + r.choice([3, 4])

    area_pos = round(0.5 * t_zero * v_fwd, 1)
    area_neg = round(0.5 * (t_end - t_zero) * abs(v_rev), 1)
    net_disp = round(area_pos - area_neg, 1)
    total_dist = round(area_pos + area_neg, 1)

    svg = f"""<svg viewBox="0 0 500 280" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="280" fill="#F8FAFC" />
  <line x1="60" y1="150" x2="460" y2="150" stroke="#0F172A" stroke-width="2" />
  <line x1="60" y1="260" x2="60" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="460" y="175" font-size="12" fill="#0F172A" text-anchor="end">Time t (s)</text>
  <text x="45" y="35" font-size="12" fill="#0F172A" text-anchor="middle">v (m/s)</text>
  <polygon points="60,150 60,{150 - v_fwd * 6} {60 + t_zero * 35},150" fill="#DCFCE7" />
  <polygon points="{60 + t_zero * 35},150 {60 + t_end * 35},{150 - v_rev * 6} {60 + t_end * 35},150" fill="#FEE2E2" />
  <line x1="60" y1="{150 - v_fwd * 6}" x2="{60 + t_end * 35}" y2="{150 - v_rev * 6}" stroke="#7C3AED" stroke-width="3" />
  <text x="45" y="{155 - v_fwd * 6}" font-size="11" fill="#475569" text-anchor="end">+{v_fwd}</text>
  <text x="45" y="{155 - v_rev * 6}" font-size="11" fill="#475569" text-anchor="end">{v_rev}</text>
  <text x="{60 + t_zero * 35}" y="170" font-size="11" fill="#475569" text-anchor="middle">{t_zero}</text>
  <text x="{60 + t_end * 35}" y="170" font-size="11" fill="#475569" text-anchor="middle">{t_end}</text>
</svg>"""

    prompt = (
        f"Refer to the velocity-time graph shown in the figure for a cart moving along a straight rail.\n\n"
        f"1. At what time ($t$) does the cart momentarily come to rest and reverse its direction of motion?\n"
        f"2. Calculate the net displacement ($\\Delta x$) of the cart between $t = 0$ and $t = {t_end}\\text{{ s}}$.\n"
        f"3. Calculate the total distance covered by the cart over the ${t_end}\\text{{ s}}$ interval."
    )
    ans = f"Reverses at t = {t_zero} s; Displacement = {_fmt_tex(net_disp)} m; Distance = {_fmt_tex(total_dist)} m"
    sol = (
        f"1. The cart reverses direction when $v = 0\\text{{ m/s}}$ and crosses the time axis, which occurs at **$t = {t_zero}\\text{{ s}}$**.\n"
        f"2. $\\text{{Positive area}} = \\frac{{1}}{{2}} \\times {t_zero} \\times {v_fwd} = +{_fmt_tex(area_pos)}\\text{{ m}}$.\n"
        f"   $\\text{{Negative area}} = \\frac{{1}}{{2}} \\times ({t_end} - {t_zero}) \\times ({v_rev}) = -{_fmt_tex(area_neg)}\\text{{ m}}$.\n"
        f"   $\\Delta x = \\text{{Area}}_1 + \\text{{Area}}_2 = {_fmt_tex(area_pos)} - {_fmt_tex(area_neg)} = {_fmt_tex(net_disp)}\\text{{ m}}$ forward.\n"
        f"3. $\\text{{Total distance}} = |\\text{{Area}}_1| + |\\text{{Area}}_2| = {_fmt_tex(area_pos)} + {_fmt_tex(area_neg)} = {_fmt_tex(total_dist)}\\text{{ m}}$."
    )
    rubric = [
        {"step": 1, "criterion": f"Identified direction reversal time t = {t_zero} s", "marks": 1},
        {"step": 2, "criterion": f"Calculated net displacement = {_fmt_tex(net_disp)} m", "marks": 2},
        {"step": 3, "criterion": f"Calculated total distance = {_fmt_tex(total_dist)} m", "marks": 1},
    ]
    hints = {
        "tier_1": "Displacement subtracts the area below the time axis; distance adds both absolute areas.",
        "tier_2": f"Area above = {area_pos} m; Area below = {area_neg} m.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "23_velocity_time_graph_direction_reversal_negative_area", 23, prompt, ans, sol, 4, ["added_negative_area_to_displacement"], rubric, hints, spec)


# ============================================================================ #
# 24. Acceleration-time graph: area as change in velocity
# ============================================================================ #
def build_24_acceleration_time_graph_area_as_change_in_velocity(r: random.Random) -> Dict[str, Any]:
    a_val = r.choice([2.0, 3.0, 4.0, 5.0])
    dt = r.choice([4, 5, 6, 8])
    vi = r.choice([0, 5, 10])
    delta_v = round(a_val * dt, 1)
    vf = round(vi + delta_v, 1)

    svg = f"""<svg viewBox="0 0 500 240" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#F8FAFC" />
  <line x1="60" y1="190" x2="460" y2="190" stroke="#0F172A" stroke-width="2" />
  <line x1="60" y1="190" x2="60" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="460" y="215" font-size="12" fill="#0F172A" text-anchor="end">Time t (s)</text>
  <text x="45" y="35" font-size="12" fill="#0F172A" text-anchor="middle">a (m/s²)</text>
  <rect x="60" y="{190 - int(a_val * 25)}" width="{dt * 40}" height="{int(a_val * 25)}" fill="#E0E7FF" />
  <line x1="60" y1="{190 - int(a_val * 25)}" x2="{60 + dt * 40}" y2="{190 - int(a_val * 25)}" stroke="#4F46E5" stroke-width="3" />
  <text x="45" y="{195 - int(a_val * 25)}" font-size="11" fill="#475569" text-anchor="end">{_fmt(a_val)}</text>
  <text x="{60 + dt * 40}" y="208" font-size="11" fill="#475569" text-anchor="middle">{dt}</text>
</svg>"""

    prompt = (
        f"Refer to the acceleration-time ($a-t$) graph shown in the figure for a particle with an initial velocity "
        f"of ${vi}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$ at $t = 0$.\n\n"
        f"1. What physical quantity is represented by the area under an acceleration-time graph?\n"
        f"2. Calculate the change in velocity ($\\Delta v$) over the ${dt}\\text{{ s}}$ interval.\n"
        f"3. Calculate the final velocity ($v_f$) of the particle at $t = {dt}\\text{{ s}}$."
    )
    ans = f"Delta v = {_fmt_tex(delta_v)} m*s^-1, vf = {_fmt_tex(vf)} m*s^-1"
    sol = (
        f"1. The area under an $a-t$ graph represents the **change in velocity** ($\\Delta v = a \\Delta t$).\n"
        f"2. $\\Delta v = \\text{{Area of rectangle}} = {_fmt_tex(a_val)} \\times {dt} = {_fmt_tex(delta_v)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"3. $v_f = v_i + \\Delta v = {vi} + {_fmt_tex(delta_v)} = {_fmt_tex(vf)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Identified area as change in velocity", "marks": 1},
        {"step": 2, "criterion": f"Calculated Delta v = {_fmt_tex(delta_v)} m*s^-1", "marks": 1},
        {"step": 3, "criterion": f"Calculated vf = {_fmt_tex(vf)} m*s^-1", "marks": 1},
    ]
    hints = {
        "tier_1": "Area under an a-t graph gives Delta v, not displacement.",
        "tier_2": f"Delta v = a * dt = {_fmt(a_val)} * {dt} = {_fmt(delta_v)} m/s.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "24_acceleration_time_graph_area_as_change_in_velocity", 24, prompt, ans, sol, 3, ["confused_area_of_a_t_with_displacement"], rubric, hints, spec)


# ============================================================================ #
# 25. Converting position-time to velocity-time graph
# ============================================================================ #
def build_25_converting_position_time_to_velocity_time_graph(r: random.Random) -> Dict[str, Any]:
    t1 = r.choice([3, 4])
    t2 = t1 + r.choice([3, 4])
    v1 = r.choice([2.0, 3.0, 4.0])
    x1 = round(v1 * t1, 1)

    svg = f"""<svg viewBox="0 0 500 240" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#F8FAFC" />
  <line x1="60" y1="200" x2="460" y2="200" stroke="#0F172A" stroke-width="2" />
  <line x1="60" y1="200" x2="60" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="460" y="225" font-size="12" fill="#0F172A" text-anchor="end">Time t (s)</text>
  <text x="45" y="35" font-size="12" fill="#0F172A" text-anchor="middle">x (m)</text>
  <line x1="60" y1="200" x2="{60 + t1 * 35}" y2="{200 - int(x1 * 8)}" stroke="#2563EB" stroke-width="3" />
  <line x1="{60 + t1 * 35}" y1="{200 - int(x1 * 8)}" x2="{60 + t2 * 35}" y2="{200 - int(x1 * 8)}" stroke="#2563EB" stroke-width="3" />
  <text x="{60 + t1 * 35}" y="218" font-size="11" fill="#475569" text-anchor="middle">{t1}</text>
  <text x="{60 + t2 * 35}" y="218" font-size="11" fill="#475569" text-anchor="middle">{t2}</text>
  <text x="45" y="{205 - int(x1 * 8)}" font-size="11" fill="#475569" text-anchor="end">{_fmt(x1)}</text>
</svg>"""

    prompt = (
        f"Refer to the position-time graph shown in the figure for a runner moving along a straight line.\n\n"
        f"1. Calculate the gradient for the interval $0$ to ${t1}\\text{{ s}}$ and state the velocity value.\n"
        f"2. Calculate the gradient for the interval ${t1}\\text{{ s}}$ to ${t2}\\text{{ s}}$ and state the velocity value.\n"
        f"3. Describe the shape of the corresponding velocity-time graph across both intervals."
    )
    ans = f"v1 = {_fmt_tex(v1)} m*s^-1; v2 = 0 m*s^-1"
    sol = (
        f"1. Interval $0$ to ${t1}\\text{{ s}}$:\n"
        f"   $\\text{{Gradient}} = \\frac{{{_fmt_tex(x1)} - 0}}{{{t1} - 0}} = {_fmt_tex(v1)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"   The velocity is constant at **${_fmt_tex(v1)}\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$**.\n"
        f"2. Interval ${t1}\\text{{ s}}$ to ${t2}\\text{{ s}}$:\n"
        f"   $\\text{{Gradient}} = \\frac{{{_fmt_tex(x1)} - {_fmt_tex(x1)}}}{{{t2} - {t1}}} = 0\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$.\n"
        f"   The velocity is **$0\\text{{ m}}\\cdot\\text{{s}}^{{-1}}$**.\n"
        f"3. On a $v-t$ graph, the motion is represented by a horizontal line at $v = {_fmt_tex(v1)}\\text{{ m/s}}$ "
        f"from $t = 0$ to $t = {t1}\\text{{ s}}$, followed by a vertical drop to a horizontal line along the time axis ($v = 0$) "
        f"from $t = {t1}\\text{{ s}}$ to $t = {t2}\\text{{ s}}$."
    )
    rubric = [
        {"step": 1, "criterion": f"Calculated v1 = {_fmt_tex(v1)} m*s^-1", "marks": 1},
        {"step": 2, "criterion": "Calculated v2 = 0 m*s^-1", "marks": 1},
        {"step": 3, "criterion": "Described horizontal line segments at v1 and 0", "marks": 2},
    ]
    hints = {
        "tier_1": "Velocity is the slope of position-time. Flat x-t means v = 0.",
        "tier_2": f"From 0 to {t1}s, v = {x1} / {t1} = {_fmt(v1)} m/s. From {t1}s to {t2}s, v = 0.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "25_converting_position_time_to_velocity_time_graph", 25, prompt, ans, sol, 4, ["thought_velocity_increases_because_position_increases"], rubric, hints, spec)


# ============================================================================ #
# BUILDERS EXPORT DICTIONARY 01–25
# ============================================================================ #
BUILDERS_01_25: Dict[str, Any] = {
    "01_frame_of_reference_and_1d_position": build_01_frame_of_reference_and_1d_position,
    "02_distance_vs_displacement_1d": build_02_distance_vs_displacement_1d,
    "03_average_speed_calculation": build_03_average_speed_calculation,
    "04_average_velocity_calculation": build_04_average_velocity_calculation,
    "05_instantaneous_speed_vs_velocity": build_05_instantaneous_speed_vs_velocity,
    "06_acceleration_definition_and_calculation": build_06_acceleration_definition_and_calculation,
    "07_positive_negative_acceleration_and_deceleration": build_07_positive_negative_acceleration_and_deceleration,
    "08_equation_motion_vf_from_vi_a_t": build_08_equation_motion_vf_from_vi_a_t,
    "09_equation_motion_deltax_from_vi_a_t": build_09_equation_motion_deltax_from_vi_a_t,
    "10_equation_motion_vf2_from_vi_a_deltax": build_10_equation_motion_vf2_from_vi_a_deltax,
    "11_equation_motion_deltax_from_average_velocity_t": build_11_equation_motion_deltax_from_average_velocity_t,
    "12_kinematics_solve_for_time_interval": build_12_kinematics_solve_for_time_interval,
    "13_kinematics_solve_for_uniform_acceleration": build_13_kinematics_solve_for_uniform_acceleration,
    "14_kinematics_solve_for_initial_velocity": build_14_kinematics_solve_for_initial_velocity,
    "15_stopping_distance_reaction_time_and_braking": build_15_stopping_distance_reaction_time_and_braking,
    "16_two_stage_motion_acceleration_then_constant_velocity": build_16_two_stage_motion_acceleration_then_constant_velocity,
    "17_two_stage_motion_constant_velocity_then_braking": build_17_two_stage_motion_constant_velocity_then_braking,
    "18_position_time_graph_constant_velocity_interpretation": build_18_position_time_graph_constant_velocity_interpretation,
    "19_position_time_graph_accelerating_motion": build_19_position_time_graph_accelerating_motion,
    "20_velocity_time_graph_gradient_as_acceleration": build_20_velocity_time_graph_gradient_as_acceleration,
    "21_velocity_time_graph_area_as_displacement_triangle": build_21_velocity_time_graph_area_as_displacement_triangle,
    "22_velocity_time_graph_area_as_displacement_trapezoid": build_22_velocity_time_graph_area_as_displacement_trapezoid,
    "23_velocity_time_graph_direction_reversal_negative_area": build_23_velocity_time_graph_direction_reversal_negative_area,
    "24_acceleration_time_graph_area_as_change_in_velocity": build_24_acceleration_time_graph_area_as_change_in_velocity,
    "25_converting_position_time_to_velocity_time_graph": build_25_converting_position_time_to_velocity_time_graph,
}
