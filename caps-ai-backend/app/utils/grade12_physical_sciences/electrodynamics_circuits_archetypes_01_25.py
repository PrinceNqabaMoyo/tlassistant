"""Grade 12 Physical Sciences — Electrodynamics & Electric Circuits (Archetypes 01–25).
Deterministic 6-pillar question generators covering Paper 1 (Physics Term 3):
- Subskills 01–05: Magnetic flux, Faraday's Law, Lenz's Law, Fleming's dynamo rule.
- Subskills 06–10: AC generator (alternator): structure, slip rings, sinusoidal emf, coil position, frequency.
- Subskills 11–13: DC generator: split-ring commutator, pulsating DC, AC vs DC generator structural comparisons.
- Subskills 14–18: DC electric motors: motor effect, Fleming's Left-Hand Rule, commutator role, motor vs generator.
- Subskills 19–25: Alternating current (AC) theory: peak vs rms voltage/current (Vrms = Vmax / sqrt(2), Irms = Imax / sqrt(2)),
  physical definition of rms, oscilloscope waveform analysis.

All questions adhere strictly to the 6-pillar contract and the South African National Curriculum Standards.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


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
    q_id = f"g12_ps_ed_{num:02d}_{r.randint(10000, 99999)}"
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
# 01. Magnetic flux definition and calculation
# ============================================================================ #
def build_01_magnetic_flux_definition_and_calculation(r: random.Random) -> Dict[str, Any]:
    b_val = r.choice([0.15, 0.20, 0.25, 0.40, 0.50])
    area_cm2 = r.choice([40, 50, 60, 80, 100])
    area_m2 = area_cm2 / 10000.0
    flux = round(b_val * area_m2, 5)

    prompt = (
        f"A rectangular coil of cross-sectional area ${area_cm2}\\text{{ cm}}^2$ is placed in a uniform magnetic field "
        f"of strength ${b_val}\\text{{ T}}$ such that the plane of the coil is perpendicular to the magnetic field lines.\n\n"
        f"1. Define the term *magnetic flux* ($\\Phi$).\n"
        f"2. Convert the cross-sectional area to square metres ($\\text{{m}}^2$).\n"
        f"3. Calculate the total magnetic flux linking the coil in webers ($\\text{{Wb}}$)."
    )
    ans = f"Phi = {_fmt_tex(flux)} Wb"
    sol = (
        f"1. **Magnetic flux** is the product of the magnetic field strength ($B$) and the perpendicular area ($A$) "
        f"through which the field lines pass ($\\Phi = B A \\cos\\theta$).\n"
        f"2. $A = \\frac{{{area_cm2}}}{{10\\ 000}} = {_fmt_tex(area_m2)}\\text{{ m}}^2$.\n"
        f"3. When the plane of the coil is perpendicular to the field lines, the normal to the surface is parallel to $B$ ($\\theta = 0^\\circ$):\n"
        f"   $\\Phi = B A \\cos(0^\\circ) = ({b_val})({_fmt_tex(area_m2)})(1) = {_fmt_tex(flux)}\\text{{ Wb}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of magnetic flux", "marks": 1},
        {"step": 2, "criterion": f"Conversion of area to m^2 = {_fmt_tex(area_m2)}", "marks": 1},
        {"step": 3, "criterion": f"Calculated magnetic flux = {_fmt_tex(flux)} Wb", "marks": 2},
    ]
    hints = {
        "tier_1": "Magnetic flux is Phi = B * A * cos(theta). Divide cm^2 by 10 000 to get m^2.",
        "tier_2": f"Phi = {b_val} * {_fmt(area_m2)} * cos(0) = {_fmt(flux)} Wb.",
        "tier_3": ans,
    }
    return _make_q(r, "01_magnetic_flux_definition_and_calculation", 1, prompt, ans, sol, 4, ["used_90_degrees_instead_of_0_degrees_for_normal_angle"], rubric, hints)


# ============================================================================ #
# 02. Faraday's Law induced emf calculation
# ============================================================================ #
def build_02_faradays_law_induced_emf_calculation(r: random.Random) -> Dict[str, Any]:
    n_turns = r.choice([50, 100, 200, 250, 500])
    phi_i = 0.0
    phi_f = r.choice([0.02, 0.04, 0.05, 0.08])
    dt = r.choice([0.05, 0.10, 0.20])
    delta_phi = phi_f - phi_i
    emf = round(n_turns * (delta_phi / dt), 2)

    prompt = (
        f"A solenoid containing ${n_turns}$ turns of copper wire experiences a magnetic flux change from "
        f"${phi_i}\\text{{ Wb}}$ to ${phi_f}\\text{{ Wb}}$ in a time interval of ${_fmt_tex(dt)}\\text{{ s}}$.\n\n"
        f"1. State **Faraday's Law of Electromagnetic Induction** in words.\n"
        f"2. Calculate the magnitude of the induced electromotive force (emf) across the solenoid."
    )
    ans = f"emf = {_fmt_tex(emf)} V"
    sol = (
        f"1. **Faraday's Law:** The magnitude of the induced electromotive force across a circuit is directly proportional "
        f"to the rate of change of magnetic flux linkage ($\\mathcal{{E}} = -N \\frac{{\\Delta \\Phi}}{{\\Delta t}}$).\n"
        f"2. $\\mathcal{{E}} = N \\frac{{\\Delta \\Phi}}{{\\Delta t}} = ({n_turns}) \\frac{{{phi_f} - {phi_i}}}{{{_fmt_tex(dt)}}} = "
        f"({n_turns}) \\frac{{{phi_f}}}{{{_fmt_tex(dt)}}} = {_fmt_tex(emf)}\\text{{ V}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Statement of Faraday's Law in words", "marks": 2},
        {"step": 2, "criterion": "Formula emf = N * Delta Phi / Delta t", "marks": 1},
        {"step": 3, "criterion": f"Calculated induced emf = {_fmt_tex(emf)} V", "marks": 2},
    ]
    hints = {
        "tier_1": "Faraday's law relates induced emf to the rate of change of magnetic flux: emf = N * Delta Phi / dt.",
        "tier_2": f"emf = {n_turns} * ({phi_f} / {_fmt(dt)}) = {_fmt(emf)} V.",
        "tier_3": ans,
    }
    return _make_q(r, "02_faradays_law_induced_emf_calculation", 2, prompt, ans, sol, 5, ["forgot_multiplying_by_number_of_turns_N"], rubric, hints)


# ============================================================================ #
# 03. Lenz's Law: direction of induced current
# ============================================================================ #
def build_03_lenzs_law_direction_of_induced_current(r: random.Random) -> Dict[str, Any]:
    pole = r.choice(["North pole", "South pole"])
    motion = r.choice(["pushed into", "pulled out of"])

    if pole == "North pole" and motion == "pushed into":
        induced_pole = "North pole"
        reason = "oppose the approach of the incoming North pole by repelling it"
    elif pole == "North pole" and motion == "pulled out of":
        induced_pole = "South pole"
        reason = "oppose the departure of the North pole by attracting it"
    elif pole == "South pole" and motion == "pushed into":
        induced_pole = "South pole"
        reason = "oppose the approach of the incoming South pole by repelling it"
    else:
        induced_pole = "North pole"
        reason = "oppose the departure of the South pole by attracting it"

    prompt = (
        f"A permanent bar magnet with its **{pole}** facing a cylindrical copper solenoid is **{motion}** the coil.\n\n"
        f"1. State **Lenz's Law**.\n"
        f"2. State the magnetic polarity (North or South) induced at the near face of the solenoid.\n"
        f"3. Explain how Lenz's law determines this polarity."
    )
    ans = f"Induced pole = {induced_pole}"
    sol = (
        f"1. **Lenz's Law:** The direction of an induced current is always such that its magnetic field opposes the change in magnetic flux that produced it.\n"
        f"2. Induced polarity at near face: **{induced_pole}**.\n"
        f"3. According to Lenz's law, the induced current creates a magnetic field that acts to {reason}."
    )
    rubric = [
        {"step": 1, "criterion": "Statement of Lenz's Law", "marks": 2},
        {"step": 2, "criterion": f"Identified near face polarity as {induced_pole}", "marks": 1},
        {"step": 3, "criterion": f"Explanation based on opposing the magnetic flux change ({reason})", "marks": 1},
    ]
    hints = {
        "tier_1": "Lenz's Law states that the induced magnetic field opposes the original motion.",
        "tier_2": "Approaching poles repel (same polarity); receding poles attract (opposite polarity).",
        "tier_3": ans,
    }
    return _make_q(r, "03_lenzs_law_direction_of_induced_current", 3, prompt, ans, sol, 4, ["confused_lenz_law_with_faraday_law"], rubric, hints)


# ============================================================================ #
# 04. Fleming's Right-Hand dynamo rule for generators
# ============================================================================ #
def build_04_flemings_right_hand_dynamo_rule_generators(r: random.Random) -> Dict[str, Any]:
    arm_motion = r.choice(["upward", "downward"])
    field_dir = "left to right (from North pole to South pole)"

    # Fleming's Right-Hand Rule:
    # Thumb: Motion of conductor (upward or downward)
    # First finger: Magnetic Field (left to right / East)
    # Second finger: Induced Current
    if arm_motion == "upward":
        current_dir = "into the page (away from observer)"
    else:
        current_dir = "out of the page (towards observer)"

    prompt = (
        f"A straight copper wire armature arm is situated between the magnetic poles of an alternator. "
        f"The magnetic field lines point from **{field_dir}**. The wire arm is forced to move **{arm_motion}**.\n\n"
        f"1. Name the rule used to determine the direction of induced current in a generator.\n"
        f"2. Identify what physical quantities are represented by the **Thumb**, **First finger**, and **Second finger** in this rule.\n"
        f"3. Determine the direction of the induced current in the copper wire arm ({current_dir})."
    )
    ans = f"Fleming's Right-Hand Rule; Current flows {current_dir}"
    sol = (
        f"1. **Fleming's Right-Hand Rule** (also called the Generator / Dynamo Rule).\n"
        f"2. - **Thumb:** Direction of Motion / Force on the conductor.\n"
        f"   - **First finger (Forefinger):** Direction of the Magnetic Field (North to South).\n"
        f"   - **Second finger:** Direction of the Induced Current ($+$ to $-$).\n"
        f"3. Pointing the first finger to the right and the thumb {arm_motion}, the second finger points **{current_dir}**."
    )
    rubric = [
        {"step": 1, "criterion": "Named Fleming's Right-Hand Rule", "marks": 1},
        {"step": 2, "criterion": "Identified Thumb (motion), Forefinger (field), Second finger (current)", "marks": 3},
        {"step": 3, "criterion": f"Identified current direction: {current_dir}", "marks": 1},
    ]
    hints = {
        "tier_1": "Right hand for Generators (Dynamo); Left hand for Motors.",
        "tier_2": "Thumb = Motion, Forefinger = Field, Second finger = Current.",
        "tier_3": ans,
    }
    return _make_q(r, "04_flemings_right_hand_dynamo_rule_generators", 4, prompt, ans, sol, 5, ["used_left_hand_rule_for_generator"], rubric, hints)


# ============================================================================ #
# 05. Factors affecting magnitude of induced emf
# ============================================================================ #
def build_05_factors_affecting_magnitude_of_induced_emf(r: random.Random) -> Dict[str, Any]:
    speed_factor = r.choice([2, 3, 4])
    turns_factor = r.choice([2, 3])
    overall_factor = speed_factor * turns_factor

    prompt = (
        f"An AC generator produces a maximum induced electromotive force of $V_{{\\text{{max}}}} = 100\\text{{ V}}$.\n\n"
        f"1. State three structural or operational factors that can increase the maximum induced emf of a generator.\n"
        f"2. If the rotational speed of the armature is multiplied by a factor of ${speed_factor}$ and the number of coil turns "
        f"is multiplied by a factor of ${turns_factor}$, calculate the new maximum induced emf ($V_{{\\text{{max, new}}}}$)."
    )
    new_v = 100 * overall_factor
    ans = f"New Vmax = {new_v} V"
    sol = (
        f"1. Three factors that increase induced emf ($\\mathcal{{E}} = -N \\frac{{\\Delta \\Phi}}{{\\Delta t}} = N B A \\omega$):\n"
        f"   - Increasing the rotational speed / frequency of the coil ($\\omega$).\n"
        f"   - Increasing the number of turns ($N$) in the armature coil.\n"
        f"   - Increasing the magnetic field strength ($B$) by using stronger permanent magnets or electromagnets.\n"
        f"   - (Also acceptable: increasing the cross-sectional area $A$ of the coil, or winding coil around a soft iron core).\n"
        f"2. Since $\\mathcal{{E}}_{{\\text{{max}}}} \\propto N \\cdot \\omega$:\n"
        f"   $V_{{\\text{{max, new}}}} = 100 \\times ({speed_factor}) \\times ({turns_factor}) = 100 \\times {overall_factor} = {new_v}\\text{{ V}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Stated three valid factors affecting induced emf", "marks": 3},
        {"step": 2, "criterion": f"Calculated new peak emf = {new_v} V", "marks": 2},
    ]
    hints = {
        "tier_1": "Peak emf is proportional to: number of turns N, magnetic field B, coil area A, and rotational speed omega.",
        "tier_2": f"New Vmax = 100 * {speed_factor} * {turns_factor} = {new_v} V.",
        "tier_3": ans,
    }
    return _make_q(r, "05_factors_affecting_magnitude_of_induced_emf", 5, prompt, ans, sol, 5, ["omitted_rotational_speed_as_factor"], rubric, hints)


# ============================================================================ #
# 06. AC generator components and functions
# ============================================================================ #
def build_06_ac_generator_components_and_functions(r: random.Random) -> Dict[str, Any]:
    comp = r.choice(["Slip rings", "Carbon brushes", "Armature coil", "Pole pieces / Field magnets"])

    if comp == "Slip rings":
        func = "Maintain continuous electrical contact between the rotating armature coil and the stationary external circuit without twisting the lead wires."
    elif comp == "Carbon brushes":
        func = "Press against the rotating slip rings to provide a low-friction electrical pathway conducting induced current to the external circuit."
    elif comp == "Armature coil":
        func = "Rotate within the magnetic field to cut magnetic flux lines, experiencing a rate of change of flux that induces an electromotive force."
    else:
        func = "Provide a uniform, strong magnetic field across the region through which the armature coil rotates."

    prompt = (
        f"Refer to an alternating current (AC) generator (alternator).\n\n"
        f"1. Name the four essential structural components of an AC generator.\n"
        f"2. State the specific function of the **{comp}** in the generator."
    )
    ans = f"Function of {comp}: {func}"
    sol = (
        f"1. The four essential components of an AC generator are:\n"
        f"   - Armature coil (insulated copper wire wound around a soft iron core)\n"
        f"   - Field magnets / pole pieces (North and South poles)\n"
        f"   - Slip rings (two continuous circular metal rings)\n"
        f"   - Carbon brushes (spring-loaded conductive carbon blocks)\n"
        f"2. Function of **{comp}**: {func}"
    )
    rubric = [
        {"step": 1, "criterion": "Listed 4 core generator components", "marks": 2},
        {"step": 2, "criterion": f"Accurate description of function for {comp}", "marks": 2},
    ]
    hints = {
        "tier_1": "AC generators use smooth SLIP RINGS and carbon brushes.",
        "tier_2": f"{comp}: {func}",
        "tier_3": ans,
    }
    return _make_q(r, "06_ac_generator_components_and_functions", 6, prompt, ans, sol, 4, ["confused_slip_rings_with_split_ring_commutator"], rubric, hints)


# ============================================================================ #
# 07. AC generator slip rings and brushes function
# ============================================================================ #
def build_07_ac_generator_slip_rings_and_brushes_function(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A design engineer evaluates the current collection system of a large-scale power station alternator.\n\n"
        f"1. Why are **slip rings** used in an AC generator rather than a split-ring commutator?\n"
        f"2. Why are the contact brushes made of **carbon (graphite)** rather than hard copper metal?"
    )
    ans = "Slip rings preserve the alternating direction of current; graphite brushes are self-lubricating and conduct electricity with low mechanical wear"
    sol = (
        f"1. **Slip rings** maintain continuous, permanent electrical contact with the same sides of the coil throughout full rotations. "
        f"As the coil rotates through $180^\\circ$, the induced current naturally reverses direction in the coil, and this natural alternating current "
        f"is delivered directly to the external circuit without rectification.\n"
        f"2. **Carbon (graphite) brushes** are used because:\n"
        f"   - Graphite is a good electrical conductor.\n"
        f"   - Graphite is soft and self-lubricating, minimizing friction and mechanical wear on the rotating metal slip rings.\n"
        f"   - Graphite has a high melting point and resists thermal damage from electrical sparking."
    )
    rubric = [
        {"step": 1, "criterion": "Explained slip rings preserve alternating polarity without rectification", "marks": 2},
        {"step": 2, "criterion": "Stated graphite is conductive and soft/self-lubricating to reduce ring wear", "marks": 2},
    ]
    hints = {
        "tier_1": "Slip rings do not reverse connections; split rings reverse connections every half-cycle.",
        "tier_2": "Graphite is conductive, soft, self-lubricating, and prevents ring damage.",
        "tier_3": ans,
    }
    return _make_q(r, "07_ac_generator_slip_rings_and_brushes_function", 7, prompt, ans, sol, 4, ["thought_slip_rings_rectify_current"], rubric, hints)


# ============================================================================ #
# 08. AC generator induced emf sinusoidal waveform
# ============================================================================ #
def build_08_ac_generator_induced_emf_sinusoidal_waveform(r: random.Random) -> Dict[str, Any]:
    v_max = r.choice([150, 200, 311, 325])
    f_hz = r.choice([50, 60])
    period_ms = round(1000.0 / f_hz, 1)

    svg = f"""<svg viewBox="0 0 500 240" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#F8FAFC" />
  <line x1="50" y1="120" x2="450" y2="120" stroke="#0F172A" stroke-width="2" />
  <line x1="50" y1="210" x2="50" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="450" y="145" font-size="12" fill="#0F172A" text-anchor="end">Time t (ms)</text>
  <text x="40" y="35" font-size="12" fill="#0F172A" text-anchor="middle">V (V)</text>
  <path d="M 50 120 Q 125 30 200 120 T 350 120" fill="none" stroke="#2563EB" stroke-width="3" />
  <text x="40" y="45" font-size="11" fill="#475569" text-anchor="end">+{v_max}</text>
  <text x="40" y="205" font-size="11" fill="#475569" text-anchor="end">-{v_max}</text>
  <text x="200" y="140" font-size="11" fill="#475569" text-anchor="middle">{_fmt(period_ms / 2.0)}</text>
  <text x="350" y="140" font-size="11" fill="#475569" text-anchor="middle">{_fmt(period_ms)}</text>
  <line x1="125" y1="40" x2="125" y2="120" stroke="#CBD5E1" stroke-dasharray="3,3" />
  <circle cx="125" cy="40" r="4" fill="#2563EB" />
  <circle cx="275" cy="200" r="4" fill="#2563EB" />
</svg>"""

    prompt = (
        f"Refer to the voltage-time output graph shown in the figure for an alternating current generator.\n\n"
        f"1. Write down the peak (maximum) voltage ($V_{{\\text{{max}}}}$) delivered by the alternator.\n"
        f"2. Write down the period ($T$) of one complete cycle in seconds.\n"
        f"3. Calculate the rotational frequency ($f$) of the generator armature in hertz ($\\text{{Hz}}$)."
    )
    ans = f"Vmax = {v_max} V; T = {_fmt_tex(period_ms / 1000.0)} s; f = {f_hz} Hz"
    sol = (
        f"1. From the crest of the waveform: $V_{{\\text{{max}}}} = **{v_max}\\text{{ V}}**$.\n"
        f"2. The time for one full cycle is ${period_ms}\\text{{ ms}} = \\frac{{{period_ms}}}{{1000}} = **{_fmt_tex(period_ms / 1000.0)}\\text{{ s}}**$.\n"
        f"3. $f = \\frac{{1}}{{T}} = \\frac{{1}}{{{_fmt_tex(period_ms / 1000.0)}}} = **{f_hz}\\text{{ Hz}}**$."
    )
    rubric = [
        {"step": 1, "criterion": f"Identified Vmax = {v_max} V", "marks": 1},
        {"step": 2, "criterion": f"Converted period to seconds = {_fmt_tex(period_ms / 1000.0)} s", "marks": 1},
        {"step": 3, "criterion": f"Calculated frequency f = {f_hz} Hz", "marks": 2},
    ]
    hints = {
        "tier_1": "Peak voltage is the maximum height of the wave. Period is time for one full cycle. f = 1/T.",
        "tier_2": f"T = {period_ms} ms = {_fmt(period_ms/1000.0)} s. f = 1 / T = {f_hz} Hz.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "08_ac_generator_induced_emf_sinusoidal_waveform", 8, prompt, ans, sol, 4, ["confused_peak_to_peak_with_peak_voltage"], rubric, hints, spec)


# ============================================================================ #
# 09. AC generator coil orientation and induced emf
# ============================================================================ #
def build_09_ac_generator_coil_orientation_and_induced_emf(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A rectangular coil rotates at a constant angular speed within a uniform magnetic field.\n\n"
        f"1. When the plane of the coil is **perpendicular** to the magnetic field lines:\n"
        f"   - Is the magnetic flux linking the coil at a maximum, minimum, or zero?\n"
        f"   - What is the value of the induced emf (maximum, minimum, or zero)? Explain your answer using Faraday's Law.\n"
        f"2. When the plane of the coil is **parallel** to the magnetic field lines:\n"
        f"   - Is the magnetic flux linking the coil at a maximum, minimum, or zero?\n"
        f"   - What is the value of the induced emf (maximum, minimum, or zero)?"
    )
    ans = "Perpendicular: Flux is maximum, induced emf is zero; Parallel: Flux is zero, induced emf is maximum"
    sol = (
        f"1. **Perpendicular coil plane:**\n"
        f"   - Magnetic flux $\\Phi = B A \\cos(0^\\circ) = B A$ is at a **maximum**.\n"
        f"   - Induced emf is **zero ($\\mathcal{{E}} = 0$)** because the rate of change of magnetic flux is zero "
        f"($\\frac{{\\Delta \\Phi}}{{\\Delta t}} = 0$ at the stationary turning point of the flux cosine curve; "
        f"the coil arms are moving momentarily parallel to the field lines and cutting no flux).\n"
        f"2. **Parallel coil plane:**\n"
        f"   - Magnetic flux linking the loop is **zero ($\\Phi = 0$)**.\n"
        f"   - Induced emf is at its **maximum ($\\mathcal{{E}} = \\mathcal{{E}}_{{\\text{{max}}}}$)** because the coil arms "
        f"are cutting perpendicularly across the magnetic field lines at the maximum possible rate ($\\frac{{\\Delta \\Phi}}{{\\Delta t}}$ is maximum)."
    )
    rubric = [
        {"step": 1, "criterion": "Perpendicular: Flux is maximum, emf is zero with flux-rate justification", "marks": 2},
        {"step": 2, "criterion": "Parallel: Flux is zero, emf is maximum with cutting rate justification", "marks": 2},
    ]
    hints = {
        "tier_1": "Emf depends on rate of change of flux, not the instantaneous amount of flux.",
        "tier_2": "When flux is maximum (perpendicular), rate of change is zero (emf = 0). When flux is zero (parallel), rate of change is maximum (emf = max).",
        "tier_3": ans,
    }
    return _make_q(r, "09_ac_generator_coil_orientation_and_induced_emf", 9, prompt, ans, sol, 4, ["assumed_maximum_flux_means_maximum_emf"], rubric, hints)


# ============================================================================ #
# 10. AC generator frequency and period of rotation
# ============================================================================ #
def build_10_ac_generator_frequency_and_period_of_rotation(r: random.Random) -> Dict[str, Any]:
    rpm = r.choice([1500, 1800, 3000, 3600])
    rps = rpm / 60.0  # Hz
    period = round(1.0 / rps, 4)

    prompt = (
        f"An alternator in a commercial power turbine turns at a constant rotational frequency of "
        f"${rpm}\\text{{ r/min}}$ (revolutions per minute).\n\n"
        f"1. Calculate the frequency of the generated alternating current in hertz ($\\text{{Hz}}$).\n"
        f"2. Calculate the period ($T$) of the generated AC waveform."
    )
    ans = f"f = {int(rps)} Hz; T = {_fmt_tex(period)} s"
    sol = (
        f"1. $f = \\frac{{\\text{{rpm}}}}{{60}} = \\frac{{{rpm}}}{{60}} = **{int(rps)}\\text{{ Hz}}**$.\n"
        f"2. $T = \\frac{{1}}{{f}} = \\frac{{1}}{{{int(rps)}}} = **{_fmt_tex(period)}\\text{{ s}}**$."
    )
    rubric = [
        {"step": 1, "criterion": f"Calculated frequency f = {int(rps)} Hz", "marks": 2},
        {"step": 2, "criterion": f"Calculated period T = {_fmt_tex(period)} s", "marks": 1},
    ]
    hints = {
        "tier_1": "Frequency f = rpm / 60. Period T = 1 / f.",
        "tier_2": f"f = {rpm} / 60 = {int(rps)} Hz. T = 1 / {int(rps)}.",
        "tier_3": ans,
    }
    return _make_q(r, "10_ac_generator_frequency_and_period_of_rotation", 10, prompt, ans, sol, 3, ["forgot_dividing_rpm_by_60"], rubric, hints)


# ============================================================================ #
# 11. DC generator split-ring commutator function
# ============================================================================ #
def build_11_dc_generator_split_ring_commutator_function(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Consider a direct current (DC) generator.\n\n"
        f"1. Name the component that replaces slip rings in a DC generator.\n"
        f"2. State the essential function of this component.\n"
        f"3. Explain how this component achieves mechanical rectification of the induced current."
    )
    ans = "Split-ring commutator; reverses electrical connections to external circuit every half-rotation to maintain unidirectional current"
    sol = (
        f"1. The component is the **split-ring commutator**.\n"
        f"2. **Function:** To mechanically rectify the induced alternating current inside the coil so that direct current "
        f"(flowing in one direction only) is delivered to the external circuit.\n"
        f"3. **Explanation:** As the coil rotates through the vertical position every half-turn ($180^\\circ$), the induced current "
        f"inside the coil naturally reverses. At this exact moment, each half of the split-ring commutator breaks contact with one carbon brush "
        f"and connects to the opposite brush. This switch inverts the connections, ensuring that current exits through the same positive brush "
        f"during every half-cycle."
    )
    rubric = [
        {"step": 1, "criterion": "Identified split-ring commutator", "marks": 1},
        {"step": 2, "criterion": "Stated function: converts AC to unidirectional DC", "marks": 1},
        {"step": 3, "criterion": "Explained brush contact reversal every half-cycle", "marks": 2},
    ]
    hints = {
        "tier_1": "DC generators use split-ring commutators to reverse connections every 180 degrees.",
        "tier_2": "The split ring ensures the current in the external circuit is always unidirectional.",
        "tier_3": ans,
    }
    return _make_q(r, "11_dc_generator_split_ring_commutator_function", 11, prompt, ans, sol, 4, ["thought_dc_generators_create_unidirectional_current_without_rectification"], rubric, hints)


# ============================================================================ #
# 12. DC generator pulsating direct current waveform
# ============================================================================ #
def build_12_dc_generator_pulsating_direct_current_waveform(r: random.Random) -> Dict[str, Any]:
    v_max = r.choice([12, 24, 48, 120])
    f_hz = 50
    t_pulse_ms = round(1000.0 / (2 * f_hz), 1)  # 10 ms per pulsating hump

    svg = f"""<svg viewBox="0 0 500 240" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#F8FAFC" />
  <line x1="50" y1="200" x2="450" y2="200" stroke="#0F172A" stroke-width="2" />
  <line x1="50" y1="200" x2="50" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="450" y="225" font-size="12" fill="#0F172A" text-anchor="end">Time t (ms)</text>
  <text x="40" y="35" font-size="12" fill="#0F172A" text-anchor="middle">V (V)</text>
  <path d="M 50 200 Q 125 40 200 200 Q 275 40 350 200 Q 425 40 500 200" fill="none" stroke="#D97706" stroke-width="3" />
  <text x="40" y="55" font-size="11" fill="#475569" text-anchor="end">+{v_max}</text>
  <text x="200" y="218" font-size="11" fill="#475569" text-anchor="middle">{_fmt(t_pulse_ms)}</text>
  <text x="350" y="218" font-size="11" fill="#475569" text-anchor="middle">{_fmt(2 * t_pulse_ms)}</text>
  <line x1="50" y1="50" x2="450" y2="50" stroke="#CBD5E1" stroke-dasharray="3,3" />
</svg>"""

    prompt = (
        f"Refer to the output voltage waveform shown in the figure for a single-coil generator.\n\n"
        f"1. Identify whether this waveform represents an **AC generator** or a **DC generator**. Give a reason based on the graph.\n"
        f"2. Explain why this voltage is described as *pulsating direct current* rather than *steady direct current* (such as from a chemical cell).\n"
        f"3. State how a commercial DC generator can be modified to smooth this waveform into nearly constant direct current."
    )
    ans = "DC generator; voltage is always positive (unidirectional); commercial generators use multiple coils at different angles"
    sol = (
        f"1. This is a **DC generator** because the output voltage is always positive ($V \\ge 0$) and never crosses the time axis into negative values.\n"
        f"2. It is called **pulsating DC** because although the current flows in one direction only, its magnitude fluctuates between zero and peak value ($V_{{\\text{{max}}}} = {v_max}\\text{{ V}}$) "
        f"as the rotating coil angle varies.\n"
        f"3. Commercial DC dynamos use **multiple armature coils wound at different angles** connected to a multi-segment commutator. "
        f"The overlapping peaks smooth out the ripple into an almost steady DC output."
    )
    rubric = [
        {"step": 1, "criterion": "Identified DC generator with unidirectional voltage justification", "marks": 2},
        {"step": 2, "criterion": "Explained pulsating nature (magnitude varies while direction remains positive)", "marks": 1},
        {"step": 3, "criterion": "Stated modification: multiple coils / multi-segmented commutator", "marks": 1},
    ]
    hints = {
        "tier_1": "Notice that the graph stays entirely above the zero line: it is direct current, not alternating.",
        "tier_2": "The voltage pulses from 0 to Vmax because a single coil rotates through parallel and perpendicular positions.",
        "tier_3": ans,
    }
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(r, "12_dc_generator_pulsating_direct_current_waveform", 12, prompt, ans, sol, 4, ["confused_pulsating_dc_with_ac"], rubric, hints, spec)


# ============================================================================ #
# 13. Comparison: AC generator versus DC generator
# ============================================================================ #
def build_13_comparison_ac_generator_versus_dc_generator(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Compare an **AC generator** and a **DC generator** across the following design and functional criteria:\n\n"
        f"1. The mechanical component used to connect the rotating coil to the brushes.\n"
        f"2. The nature and direction of the output current delivered to the load resistor.\n"
        f"3. State one major practical advantage of AC generators over DC generators in national electricity grid distribution."
    )
    ans = "AC uses slip rings; DC uses split-ring commutator; AC voltage can be stepped up/down efficiently using transformers"
    sol = (
        f"1. **Component:** AC generators use two continuous **slip rings**; DC generators use a **split-ring commutator**.\n"
        f"2. **Output current:**\n"
        f"   - AC generator: Alternating current that periodically reverses direction in a sinusoidal waveform.\n"
        f"   - DC generator: Unidirectional pulsating direct current that flows in one direction only.\n"
        f"3. **Practical advantage:** AC voltage can be easily and efficiently stepped up to very high voltages (and low currents) "
        f"using **transformers** for long-distance transmission, dramatically reducing thermal energy losses ($P = I^2 R$) in power cables."
    )
    rubric = [
        {"step": 1, "criterion": "Slip rings for AC vs split-ring commutator for DC", "marks": 2},
        {"step": 2, "criterion": "Alternating current vs unidirectional DC", "marks": 2},
        {"step": 3, "criterion": "AC can be stepped up/down with transformers for low transmission loss", "marks": 1},
    ]
    hints = {
        "tier_1": "AC = slip rings; DC = split-ring commutator.",
        "tier_2": "Transformers only work with AC, allowing high voltage / low current distribution.",
        "tier_3": ans,
    }
    return _make_q(r, "13_comparison_ac_generator_versus_dc_generator", 13, prompt, ans, sol, 5, ["asserted_dc_can_be_transformed_directly"], rubric, hints)


# ============================================================================ #
# 14. DC electric motor: operating principle (motor effect)
# ============================================================================ #
def build_14_dc_electric_motor_operating_principle_motor_effect(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A direct current (DC) electric motor is connected to a battery.\n\n"
        f"1. State the fundamental **operating physical principle** of an electric motor.\n"
        f"2. Describe the **energy conversion** that takes place in a motor.\n"
        f"3. Explain how the magnetic field of the permanent magnets interacts with the current in the armature coil to generate motion."
    )
    ans = "Operating principle: The motor effect; Energy conversion: Electrical to mechanical"
    sol = (
        f"1. **Operating principle:** The **motor effect** (the force experienced by a current-carrying conductor when placed in a magnetic field).\n"
        f"2. **Energy conversion:** **Electrical energy** is converted into **mechanical (kinetic) energy**.\n"
        f"3. **Explanation:** When current passes through the armature coil, it generates its own magnetic field around the conductors. "
        f"This current-induced field interacts with the external magnetic field of the permanent magnets (reinforcing the field on one side "
        f"and weakening it on the other). This magnetic imbalance exerts equal and opposite perpendicular forces ($F = I L B \\sin\\theta$) "
        f"on opposite sides of the coil, creating a turning effect (torque) that causes the coil to rotate."
    )
    rubric = [
        {"step": 1, "criterion": "Stated principle: The motor effect", "marks": 1},
        {"step": 2, "criterion": "Energy conversion: electrical to mechanical energy", "marks": 1},
        {"step": 3, "criterion": "Explained interaction of magnetic fields producing torque on opposite arms", "marks": 2},
    ]
    hints = {
        "tier_1": "Motors convert electrical energy into mechanical energy using the motor effect.",
        "tier_2": "Current-carrying wire in an external B-field experiences magnetic force F = ILB.",
        "tier_3": ans,
    }
    return _make_q(r, "14_dc_electric_motor_operating_principle_motor_effect", 14, prompt, ans, sol, 4, ["confused_motor_effect_with_electromagnetic_induction"], rubric, hints)


# ============================================================================ #
# 15. Fleming's Left-Hand motor rule for rotation direction
# ============================================================================ #
def build_15_flemings_left_hand_motor_rule_rotation_direction(r: random.Random) -> Dict[str, Any]:
    current_side_a = r.choice(["into the page", "out of the page"])
    field_dir = "left to right (North to South)"

    if current_side_a == "into the page":
        force_side_a = "downward"
        force_side_b = "upward"
        rotation = "clockwise"
    else:
        force_side_a = "upward"
        force_side_b = "downward"
        rotation = "anticlockwise"

    prompt = (
        f"A rectangular coil in a DC motor is placed horizontally between a North pole on the left and a South pole on the right. "
        f"Arm $A$ of the coil carries conventional current pointing **{current_side_a}**, while opposite Arm $B$ carries current in the reverse direction.\n\n"
        f"1. Name the rule used to deduce the direction of the magnetic force on the coil arms of an electric motor.\n"
        f"2. Determine the direction of the magnetic force on Arm $A$.\n"
        f"3. Determine the direction of the resulting rotation of the armature coil (clockwise or anticlockwise)."
    )
    ans = f"Fleming's Left-Hand Rule; Force on A is {force_side_a}; Rotation is {rotation}"
    sol = (
        f"1. **Fleming's Left-Hand Rule** (the Motor Rule).\n"
        f"2. Using the left hand: Forefinger points to the right (North to South), Second finger points {current_side_a}. "
        f"The thumb points **{force_side_a}** on Arm $A$.\n"
        f"3. Since Arm $B$ carries current in the reverse direction, the force on Arm $B$ is {force_side_b}. "
        f"With Arm $A$ pushed {force_side_a} and Arm $B$ pushed {force_side_b}, the coil rotates **{rotation}**."
    )
    rubric = [
        {"step": 1, "criterion": "Named Fleming's Left-Hand Rule", "marks": 1},
        {"step": 2, "criterion": f"Deduced force on Arm A is {force_side_a}", "marks": 2},
        {"step": 3, "criterion": f"Deduced rotation is {rotation}", "marks": 1},
    ]
    hints = {
        "tier_1": "Left hand for Motors (FBI: Force, B-field, Current).",
        "tier_2": f"Forefinger = East. Current = {current_side_a}. Thumb = {force_side_a}.",
        "tier_3": ans,
    }
    return _make_q(r, "15_flemings_left_hand_motor_rule_rotation_direction", 15, prompt, ans, sol, 4, ["used_right_hand_rule_for_motor"], rubric, hints)


# ============================================================================ #
# 16. DC motor split-ring commutator role in continuous rotation
# ============================================================================ #
def build_16_dc_motor_split_ring_commutator_role_in_rotation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a DC electric motor, a split-ring commutator connects the rotating armature coil to the DC power source.\n\n"
        f"1. State what would happen to the motion of the coil if slip rings were used instead of a split-ring commutator.\n"
        f"2. Explain the exact mechanism by which the split-ring commutator ensures continuous rotation in a single direction."
    )
    ans = "Without split ring, coil oscillates back and forth; split ring reverses current direction every 180 degrees so torque remains unidirectional"
    sol = (
        f"1. If slip rings were used, the coil would rotate through $90^\\circ$ to the vertical position, overshoot slightly, "
        f"and then experience a reversing torque that pulls it backwards. The coil would simply **oscillate back and forth** about the vertical position "
        f"and come to a standstill.\n"
        f"2. **Mechanism:** Every time the coil passes through the vertical neutral plane ($180^\\circ$ rotation), the gap in the split ring passes the brushes, "
        f"momentarily cutting off current. As the coil's momentum carries it past vertical, each commutator segment contacts the opposite brush, "
        f"thereby **reversing the direction of current in the coil**. This reverses the forces on the coil sides, ensuring that the torque continues "
        f"to act in the **same direction of rotation**."
    )
    rubric = [
        {"step": 1, "criterion": "Stated coil would oscillate and stop at vertical position", "marks": 2},
        {"step": 2, "criterion": "Explained current reversal every half-cycle preserves unidirectional torque", "marks": 2},
    ]
    hints = {
        "tier_1": "At the vertical plane, the torque would reverse if the current did not switch.",
        "tier_2": "The split-ring commutator reverses the current every 180 degrees so the coil keeps spinning in the same direction.",
        "tier_3": ans,
    }
    return _make_q(r, "16_dc_motor_split_ring_commutator_role_in_rotation", 16, prompt, ans, sol, 4, ["thought_motor_rotates_continuously_without_commutator"], rubric, hints)


# ============================================================================ #
# 17. Comparison: electric motor versus electric generator
# ============================================================================ #
def build_17_comparison_electric_motor_versus_electric_generator(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Compare an **electric motor** and an **electric generator** in a summary evaluation:\n\n"
        f"1. State the input energy and output energy for each device.\n"
        f"2. State the primary physical law / effect governing each device.\n"
        f"3. State which hand rule (Fleming's Left-Hand Rule or Fleming's Right-Hand Rule) applies to each device."
    )
    ans = "Motor: Electrical to Mechanical, Motor effect, Left-Hand Rule; Generator: Mechanical to Electrical, Electromagnetic induction, Right-Hand Rule"
    sol = (
        f"1. **Energy Conversions:**\n"
        f"   - **Electric Motor:** Converts **electrical energy** into **mechanical (kinetic) energy**.\n"
        f"   - **Electric Generator:** Converts **mechanical (kinetic) energy** into **electrical energy**.\n"
        f"2. **Operating Principles:**\n"
        f"   - **Motor:** The **motor effect**.\n"
        f"   - **Generator:** **Electromagnetic induction** (Faraday's Law).\n"
        f"3. **Hand Rules:**\n"
        f"   - **Motor:** **Fleming's Left-Hand Rule**.\n"
        f"   - **Generator:** **Fleming's Right-Hand Rule**."
    )
    rubric = [
        {"step": 1, "criterion": "Correct energy conversions for motor and generator", "marks": 2},
        {"step": 2, "criterion": "Motor effect vs electromagnetic induction", "marks": 2},
        {"step": 3, "criterion": "Left-Hand rule (motor) vs Right-Hand rule (generator)", "marks": 2},
    ]
    hints = {
        "tier_1": "Motor: Electrical IN -> Mechanical OUT (Left hand). Generator: Mechanical IN -> Electrical OUT (Right hand).",
        "tier_2": "Motor uses motor effect; Generator uses Faraday's electromagnetic induction.",
        "tier_3": ans,
    }
    return _make_q(r, "17_comparison_electric_motor_versus_electric_generator", 17, prompt, ans, sol, 6, ["inverted_left_and_right_hand_rules"], rubric, hints)


# ============================================================================ #
# 18. Methods to increase motor torque and power
# ============================================================================ #
def build_18_methods_to_increase_motor_torque_and_power(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"An electric vehicle design team seeks to maximize the output torque of its DC traction motor.\n\n"
        f"1. State three practical modifications that can be made to increase the torque generated by the motor.\n"
        f"2. Explain why winding the armature coils around a soft iron core significantly increases the motor's power."
    )
    ans = "Increase current, increase magnetic field strength, increase number of coil turns; soft iron core concentrates magnetic flux"
    sol = (
        f"1. Three methods to increase motor torque ($F = n I L B \\sin\\theta$):\n"
        f"   - Increase the current ($I$) flowing through the armature coils (by increasing supply voltage).\n"
        f"   - Increase the strength of the magnetic field ($B$) by using stronger electromagnets.\n"
        f"   - Increase the number of turns ($n$) of wire in the armature coil.\n"
        f"   - (Also acceptable: increase the cross-sectional area of the coil).\n"
        f"2. A **soft iron core** has high magnetic permeability, which concentrates and intensifies the magnetic flux lines "
        f"passing through the coil, substantially increasing the magnetic field strength ($B$) and therefore the magnetic force ($F$) and torque."
    )
    rubric = [
        {"step": 1, "criterion": "Listed three valid methods to increase torque", "marks": 3},
        {"step": 2, "criterion": "Explained soft iron core concentrates magnetic flux / increases B-field", "marks": 1},
    ]
    hints = {
        "tier_1": "Torque is proportional to: Current, B-field strength, number of coil turns, and coil area.",
        "tier_2": "Soft iron is ferromagnetic and concentrates magnetic field lines.",
        "tier_3": ans,
    }
    return _make_q(r, "18_methods_to_increase_motor_torque_and_power", 18, prompt, ans, sol, 4, ["suggested_increasing_resistance_to_increase_torque"], rubric, hints)


# ============================================================================ #
# 19. Alternating current concept and definition
# ============================================================================ #
def build_19_alternating_current_concept_and_definition(r: random.Random) -> Dict[str, Any]:
    f_val = r.choice([50, 60])
    prompt = (
        f"Domestic electricity in South Africa is supplied as alternating current at a frequency of ${f_val}\\text{{ Hz}}$.\n\n"
        f"1. Define the term *alternating current (AC)*.\n"
        f"2. What does a frequency of ${f_val}\\text{{ Hz}}$ mean in terms of the direction of electron flow in a circuit?\n"
        f"3. State how many times per second the current drops to zero."
    )
    ans = f"Current reverses direction periodically; 50 Hz means 50 full cycles per second; drops to zero {2 * f_val} times per second"
    sol = (
        f"1. **Alternating current (AC)** is an electric current that periodically reverses its direction and whose magnitude continuously varies with time.\n"
        f"2. A frequency of ${f_val}\\text{{ Hz}}$ means that the electrons complete ${f_val}$ full cycles of forward-and-backward oscillation every second.\n"
        f"3. In each complete cycle, the current passes through zero twice. Therefore, at ${f_val}\\text{{ Hz}}$, the current drops to zero "
        f"$2 \\times {f_val} = **{2 * f_val}\\text{{ times per second}}**$."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of alternating current", "marks": 1},
        {"step": 2, "criterion": f"Explanation of {f_val} complete cycles per second", "marks": 1},
        {"step": 3, "criterion": f"Calculated zero-crossings = {2 * f_val} times per second", "marks": 1},
    ]
    hints = {
        "tier_1": "Alternating current periodically reverses direction. One cycle has two zero crossings.",
        "tier_2": f"At {f_val} Hz, there are {f_val} cycles/second and 2 * {f_val} zero crossings/second.",
        "tier_3": ans,
    }
    return _make_q(r, "19_alternating_current_concept_and_definition", 19, prompt, ans, sol, 3, ["forgot_current_crosses_zero_twice_per_cycle"], rubric, hints)


# ============================================================================ #
# 20. Root-mean-square (rms) voltage and current definitions
# ============================================================================ #
def build_20_root_mean_square_rms_voltage_and_current_definitions(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In AC circuit analysis, voltages and currents are routinely quoted as root-mean-square (rms) quantities.\n\n"
        f"1. Define the **root-mean-square (rms) value of an alternating voltage ($V_{{\\text{{rms}}}}$)**.\n"
        f"2. Define the **root-mean-square (rms) value of an alternating current ($I_{{\\text{{rms}}}}$)**.\n"
        f"3. Explain why the simple arithmetic mean (average) of an AC sinusoidal voltage over one full cycle cannot be used to determine power dissipation."
    )
    ans = "Vrms is the DC voltage that delivers the same average power; arithmetic average over a full cycle is zero"
    sol = (
        f"1. **$V_{{\\text{{rms}}}}$:** The value of the direct voltage (DC) that dissipates the same average energy (or delivers the same average power) "
        f"in a given resistor as the alternating voltage.\n"
        f"2. **$I_{{\\text{{rms}}}}$:** The value of the direct current (DC) that dissipates the same average power in a given resistor as the alternating current.\n"
        f"3. Over one complete sinusoidal cycle, the positive half-cycle and negative half-cycle are completely symmetrical. "
        f"The simple arithmetic average of the voltage is zero ($\\text{{average}} = 0\\text{{ V}}$), even though energy is continuously dissipated as heat "
        f"in both half-cycles ($P \\propto V^2 > 0$)."
    )
    rubric = [
        {"step": 1, "criterion": "Definition of Vrms in terms of equivalent DC power dissipation", "marks": 2},
        {"step": 2, "criterion": "Definition of Irms in terms of equivalent DC power dissipation", "marks": 2},
        {"step": 3, "criterion": "Explained arithmetic mean of a full sine wave is zero while heating power is positive", "marks": 1},
    ]
    hints = {
        "tier_1": "RMS value is the DC equivalent that dissipates the same average power in a resistor.",
        "tier_2": "The simple average of a sine wave is zero because positive and negative halves cancel.",
        "tier_3": ans,
    }
    return _make_q(r, "20_root_mean_square_rms_voltage_and_current_definitions", 20, prompt, ans, sol, 5, ["defined_rms_as_arithmetic_mean_of_peak_voltage"], rubric, hints)


# ============================================================================ #
# 21. Calculate Vrms from Vmax
# ============================================================================ #
def build_21_calculate_vrms_from_vmax(r: random.Random) -> Dict[str, Any]:
    v_max = r.choice([311, 325, 340, 155, 170])
    v_rms = round(v_max / math.sqrt(2), 1)

    prompt = (
        f"An AC generator produces a sinusoidal output with a peak voltage of $V_{{\\text{{max}}}} = {v_max}\\text{{ V}}$.\n\n"
        f"Calculate the root-mean-square voltage ($V_{{\\text{{rms}}}}$) of this generator."
    )
    ans = f"Vrms = {_fmt_tex(v_rms)} V"
    sol = (
        f"$V_{{\\text{{rms}}}} = \\frac{{V_{{\\text{{max}}}}}}{{\\sqrt{{2}}}}\n"
        f"$V_{{\\text{{rms}}}} = \\frac{{{v_max}}}{{\\sqrt{{2}}}} = \\frac{{{v_max}}}{{1{{,}}4142}} = {_fmt_tex(v_rms)}\\text{{ V}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula Vrms = Vmax / sqrt(2)", "marks": 1},
        {"step": 2, "criterion": f"Substitution: {v_max} / sqrt(2)", "marks": 1},
        {"step": 3, "criterion": f"Answer Vrms = {_fmt_tex(v_rms)} V", "marks": 1},
    ]
    hints = {
        "tier_1": "Vrms = Vmax / sqrt(2).",
        "tier_2": f"Vrms = {v_max} / 1.4142 = {_fmt(v_rms)} V.",
        "tier_3": ans,
    }
    return _make_q(r, "21_calculate_vrms_from_vmax", 21, prompt, ans, sol, 3, ["multiplied_by_sqrt_2_instead_of_dividing"], rubric, hints)


# ============================================================================ #
# 22. Calculate Vmax from Vrms
# ============================================================================ #
def build_22_calculate_vmax_from_vrms(r: random.Random) -> Dict[str, Any]:
    v_rms = r.choice([220, 230, 240, 110, 120])
    v_max = round(v_rms * math.sqrt(2), 1)

    prompt = (
        f"The mains electricity supply in a domestic residence has an rms voltage rating of ${v_rms}\\text{{ V}}$ AC.\n\n"
        f"1. State what is meant by the rated value ${v_rms}\\text{{ V}}$.\n"
        f"2. Calculate the peak (maximum) voltage ($V_{{\\text{{max}}}}$) delivered by this supply."
    )
    ans = f"Vmax = {_fmt_tex(v_max)} V"
    sol = (
        f"1. The rated value of ${v_rms}\\text{{ V}}$ is the **root-mean-square (rms) voltage**, representing the DC equivalent voltage delivering the same average power.\n"
        f"2. $V_{{\\text{{rms}}}} = \\frac{{V_{{\\text{{max}}}}}}{{\\sqrt{{2}}}} \\implies "
        f"V_{{\\text{{max}}}} = V_{{\\text{{rms}}}} \\times \\sqrt{{2}} = {v_rms} \\times \\sqrt{{2}} = {_fmt_tex(v_max)}\\text{{ V}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Identified rating as rms value", "marks": 1},
        {"step": 2, "criterion": "Formula Vmax = Vrms * sqrt(2)", "marks": 1},
        {"step": 3, "criterion": f"Answer Vmax = {_fmt_tex(v_max)} V", "marks": 1},
    ]
    hints = {
        "tier_1": "Peak voltage is always higher than rms voltage: Vmax = Vrms * sqrt(2).",
        "tier_2": f"Vmax = {v_rms} * 1.4142 = {_fmt(v_max)} V.",
        "tier_3": ans,
    }
    return _make_q(r, "22_calculate_vmax_from_vrms", 22, prompt, ans, sol, 3, ["divided_by_sqrt_2_instead_of_multiplying"], rubric, hints)


# ============================================================================ #
# 23. Calculate Irms from Imax
# ============================================================================ #
def build_23_calculate_irms_from_imax(r: random.Random) -> Dict[str, Any]:
    i_max = r.choice([10.0, 14.14, 15.0, 16.0, 20.0])
    i_rms = round(i_max / math.sqrt(2), 2)

    prompt = (
        f"An AC transmission line carries a peak current of $I_{{\\text{{max}}}} = {_fmt_tex(i_max)}\\text{{ A}}$.\n\n"
        f"Calculate the root-mean-square current ($I_{{\\text{{rms}}}}$) in the line."
    )
    ans = f"Irms = {_fmt_tex(i_rms)} A"
    sol = (
        f"$I_{{\\text{{rms}}}} = \\frac{{I_{{\\text{{max}}}}}}{{\\sqrt{{2}}}}\n"
        f"$I_{{\\text{{rms}}}} = \\frac{{{_fmt_tex(i_max)}}}{{\\sqrt{{2}}}} = {_fmt_tex(i_rms)}\\text{{ A}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula Irms = Imax / sqrt(2)", "marks": 1},
        {"step": 2, "criterion": f"Substitution: {_fmt_tex(i_max)} / sqrt(2)", "marks": 1},
        {"step": 3, "criterion": f"Answer Irms = {_fmt_tex(i_rms)} A", "marks": 1},
    ]
    hints = {
        "tier_1": "Irms = Imax / sqrt(2).",
        "tier_2": f"Irms = {_fmt(i_max)} / 1.4142 = {_fmt(i_rms)} A.",
        "tier_3": ans,
    }
    return _make_q(r, "23_calculate_irms_from_imax", 23, prompt, ans, sol, 3, ["confused_irms_and_imax_formula"], rubric, hints)


# ============================================================================ #
# 24. Calculate Imax from Irms
# ============================================================================ #
def build_24_calculate_imax_from_irms(r: random.Random) -> Dict[str, Any]:
    i_rms = r.choice([5.0, 8.0, 10.0, 12.0, 15.0])
    i_max = round(i_rms * math.sqrt(2), 2)

    prompt = (
        f"An electric motor draws an rms current of ${_fmt_tex(i_rms)}\\text{{ A}}$ from an AC power socket.\n\n"
        f"Calculate the peak (maximum) current ($I_{{\\text{{max}}}}$) drawn by the motor."
    )
    ans = f"Imax = {_fmt_tex(i_max)} A"
    sol = (
        f"$I_{{\\text{{rms}}}} = \\frac{{I_{{\\text{{max}}}}}}{{\\sqrt{{2}}}} \\implies "
        f"I_{{\\text{{max}}}} = I_{{\\text{{rms}}}} \\times \\sqrt{{2}} = {_fmt_tex(i_rms)} \\times \\sqrt{{2}} = {_fmt_tex(i_max)}\\text{{ A}}$."
    )
    rubric = [
        {"step": 1, "criterion": "Formula Imax = Irms * sqrt(2)", "marks": 1},
        {"step": 2, "criterion": f"Substitution: {_fmt_tex(i_rms)} * sqrt(2)", "marks": 1},
        {"step": 3, "criterion": f"Answer Imax = {_fmt_tex(i_max)} A", "marks": 1},
    ]
    hints = {
        "tier_1": "Imax = Irms * sqrt(2).",
        "tier_2": f"Imax = {_fmt(i_rms)} * 1.4142 = {_fmt(i_max)} A.",
        "tier_3": ans,
    }
    return _make_q(r, "24_calculate_imax_from_irms", 24, prompt, ans, sol, 3, ["divided_by_sqrt_2_instead_of_multiplying"], rubric, hints)


# ============================================================================ #
# 25. AC sinusoidal waveform oscilloscope reading
# ============================================================================ #
def build_25_ac_sinusoidal_waveform_oscilloscope_reading(r: random.Random) -> Dict[str, Any]:
    y_div = r.choice([2.0, 5.0, 10.0])  # Volts per division
    num_div_peak = r.choice([2.5, 3.0, 3.5, 4.0])
    v_max = round(num_div_peak * y_div, 1)
    v_rms = round(v_max / math.sqrt(2), 1)

    t_div_ms = r.choice([2.0, 5.0])  # ms per division
    num_div_cycle = r.choice([4.0, 5.0])
    t_period_ms = round(num_div_cycle * t_div_ms, 1)
    f_hz = round(1000.0 / t_period_ms, 1)

    prompt = (
        f"An oscilloscope display is used to measure an AC voltage signal. The Y-gain (voltage sensitivity) setting is "
        f"${_fmt_tex(y_div)}\\text{{ V/div}}$, and the time-base setting is ${_fmt_tex(t_div_ms)}\\text{{ ms/div}}$. "
        f"From the screen, the peak of the wave is ${_fmt_tex(num_div_peak)}\\text{{ vertical divisions}}$ above the central baseline, "
        f"and one full cycle occupies ${_fmt_tex(num_div_cycle)}\\text{{ horizontal divisions}}$.\n\n"
        f"1. Calculate the peak voltage ($V_{{\\text{{max}}}}$).\n"
        f"2. Calculate the root-mean-square voltage ($V_{{\\text{{rms}}}}$).\n"
        f"3. Calculate the period ($T$) and frequency ($f$) of the AC voltage signal."
    )
    ans = f"Vmax = {_fmt_tex(v_max)} V; Vrms = {_fmt_tex(v_rms)} V; f = {_fmt_tex(f_hz)} Hz"
    sol = (
        f"1. $V_{{\\text{{max}}}} = \\text{{vertical divisions}} \\times \\text{{Y-gain}} = {_fmt_tex(num_div_peak)} \\times {_fmt_tex(y_div)} = {_fmt_tex(v_max)}\\text{{ V}}$.\n"
        f"2. $V_{{\\text{{rms}}}} = \\frac{{V_{{\\text{{max}}}}}}{{\\sqrt{{2}}}} = \\frac{{{_fmt_tex(v_max)}}}{{\\sqrt{{2}}}} = {_fmt_tex(v_rms)}\\text{{ V}}$.\n"
        f"3. Period: $T = \\text{{horizontal divisions}} \\times \\text{{time-base}} = {_fmt_tex(num_div_cycle)} \\times {_fmt_tex(t_div_ms)} = {_fmt_tex(t_period_ms)}\\text{{ ms}} = {_fmt_tex(t_period_ms / 1000.0)}\\text{{ s}}$.\n"
        f"   Frequency: $f = \\frac{{1}}{{T}} = \\frac{{1}}{{{_fmt_tex(t_period_ms / 1000.0)}}} = {_fmt_tex(f_hz)}\\text{{ Hz}}$."
    )
    rubric = [
        {"step": 1, "criterion": f"Calculated Vmax = {_fmt_tex(v_max)} V", "marks": 1},
        {"step": 2, "criterion": f"Calculated Vrms = {_fmt_tex(v_rms)} V", "marks": 1},
        {"step": 3, "criterion": f"Calculated period T = {_fmt_tex(t_period_ms)} ms", "marks": 1},
        {"step": 4, "criterion": f"Calculated frequency f = {_fmt_tex(f_hz)} Hz", "marks": 1},
    ]
    hints = {
        "tier_1": "Peak voltage = divisions * Y-gain. Period = divisions * time-base. Vrms = Vmax / sqrt(2).",
        "tier_2": f"Vmax = {_fmt(num_div_peak)} * {_fmt(y_div)} = {_fmt(v_max)} V. T = {_fmt(t_period_ms)} ms.",
        "tier_3": ans,
    }
    return _make_q(r, "25_ac_sinusoidal_waveform_oscilloscope_reading", 25, prompt, ans, sol, 4, ["used_peak_to_peak_divisions_instead_of_peak"], rubric, hints)


# ============================================================================ #
# BUILDERS EXPORT DICTIONARY 01–25
# ============================================================================ #
BUILDERS_01_25: Dict[str, Any] = {
    "01_magnetic_flux_definition_and_calculation": build_01_magnetic_flux_definition_and_calculation,
    "02_faradays_law_induced_emf_calculation": build_02_faradays_law_induced_emf_calculation,
    "03_lenzs_law_direction_of_induced_current": build_03_lenzs_law_direction_of_induced_current,
    "04_flemings_right_hand_dynamo_rule_generators": build_04_flemings_right_hand_dynamo_rule_generators,
    "05_factors_affecting_magnitude_of_induced_emf": build_05_factors_affecting_magnitude_of_induced_emf,
    "06_ac_generator_components_and_functions": build_06_ac_generator_components_and_functions,
    "07_ac_generator_slip_rings_and_brushes_function": build_07_ac_generator_slip_rings_and_brushes_function,
    "08_ac_generator_induced_emf_sinusoidal_waveform": build_08_ac_generator_induced_emf_sinusoidal_waveform,
    "09_ac_generator_coil_orientation_and_induced_emf": build_09_ac_generator_coil_orientation_and_induced_emf,
    "10_ac_generator_frequency_and_period_of_rotation": build_10_ac_generator_frequency_and_period_of_rotation,
    "11_dc_generator_split_ring_commutator_function": build_11_dc_generator_split_ring_commutator_function,
    "12_dc_generator_pulsating_direct_current_waveform": build_12_dc_generator_pulsating_direct_current_waveform,
    "13_comparison_ac_generator_versus_dc_generator": build_13_comparison_ac_generator_versus_dc_generator,
    "14_dc_electric_motor_operating_principle_motor_effect": build_14_dc_electric_motor_operating_principle_motor_effect,
    "15_flemings_left_hand_motor_rule_rotation_direction": build_15_flemings_left_hand_motor_rule_rotation_direction,
    "16_dc_motor_split_ring_commutator_role_in_rotation": build_16_dc_motor_split_ring_commutator_role_in_rotation,
    "17_comparison_electric_motor_versus_electric_generator": build_17_comparison_electric_motor_versus_electric_generator,
    "18_methods_to_increase_motor_torque_and_power": build_18_methods_to_increase_motor_torque_and_power,
    "19_alternating_current_concept_and_definition": build_19_alternating_current_concept_and_definition,
    "20_root_mean_square_rms_voltage_and_current_definitions": build_20_root_mean_square_rms_voltage_and_current_definitions,
    "21_calculate_vrms_from_vmax": build_21_calculate_vrms_from_vmax,
    "22_calculate_vmax_from_vrms": build_22_calculate_vmax_from_vrms,
    "23_calculate_irms_from_imax": build_23_calculate_irms_from_imax,
    "24_calculate_imax_from_irms": build_24_calculate_imax_from_irms,
    "25_ac_sinusoidal_waveform_oscilloscope_reading": build_25_ac_sinusoidal_waveform_oscilloscope_reading,
}
