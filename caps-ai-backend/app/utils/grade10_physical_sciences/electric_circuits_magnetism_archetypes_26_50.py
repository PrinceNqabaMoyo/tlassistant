"""Grade 10 Physical Sciences — Electric Circuits & Magnetism: Archetypes 26 to 50.
Grounded in curriculum_docs_auto/PhysicalSciences_Gr10/Term 2/06. Electric circuits.md:
- Resistance definition R = V / I, microscopic collision mechanism, factors affecting resistance (L, A, T, material).
- Ohmic vs non-ohmic conductors, graphical determination of resistance from V vs I and I vs V graphs.
- Series circuits: equivalent resistance Rs = R1 + R2 + ..., current conservation, potential division V = V1 + V2.
- Parallel circuits: equivalent resistance 1/Rp = 1/R1 + 1/R2 + ..., potential equality, current branching I = I1 + I2.
- Complex series-parallel resistor networks, multimeter reading predictions.
- Switch toggling dynamics, short circuit hazards, faulty meter connection effects.
- Electrical energy E = V * I * Delta t, power P = V * I, and domestic electricity cost calculation in kWh.
- Capstone diagnostic autopsy resolving common Grade 10 electric circuit misconceptions.

100% Aligned with South African National Curriculum Standards.
Complies strictly with 6-Pillar Generator Contract.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "Electric circuits"
SUBJECT = "Physical Sciences"
GRADE = "10"


def _fmt(val: float | int, decimals: int = 2) -> str:
    """Format decimal numbers using South African comma decimal separator for KaTeX."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    rounded = round(val, decimals)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{{,}}")


def _fmt_plain(val: float | int, decimals: int = 2) -> str:
    """Format decimal numbers using South African comma decimal separator for plain text."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    rounded = round(val, decimals)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_q(
    r: random.Random,
    subskill: str,
    num: int,
    prompt: str,
    correct_ans: str,
    worked_sol: str,
    marks: int,
    misconceptions: List[str],
    criteria: List[Dict[str, Any]],
    hints: Dict[str, str],
    diagram_spec: Optional[Dict[str, Any]] = None,
    weight: int = 15,
    duration: int = 5,
) -> Dict[str, Any]:
    qid = f"phys10_circ_{num:02d}_{r.randint(10000, 99999)}"
    q: Dict[str, Any] = {
        "id": qid,
        "question_id": qid,
        "topic": TOPIC,
        "subject": SUBJECT,
        "grade": GRADE,
        "term": 2,
        "subskill": subskill,
        "mode": f"elementary_{subskill}",
        "question_type": "short_answer",
        "question": prompt,
        "prompt": prompt,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "answer": correct_ans,
        "worked_solution": worked_sol,
        "explanation": worked_sol,
        "marks": marks,
        "caps_weight_percent": weight,
        "suggested_duration_mins": duration,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": criteria,
        },
        "hints": hints,
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = "context"
    return q


# =========================================================================== #
# 26. Resistance: Definition as Ratio V / I & Microscopic Cause
# =========================================================================== #
def _build_26_resistance_definition_ratio_V_I(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    v_val = r.choice([6.0, 9.0, 12.0, 18.0, 24.0])
    i_val = r.choice([0.5, 1.2, 1.5, 2.0, 2.5, 3.0])
    r_val = round(v_val / i_val, 2)

    prompt = (
        f"A potential difference of **${_fmt(v_val)}\\text{{ V}}$** applied across a metallic conductor produces a "
        f"steady current of **${_fmt(i_val)}\\text{{ A}}$**.\n\n"
        f"1. Define the term **electrical resistance**.\n"
        f"2. State the SI unit of resistance and define it in terms of volts and amperes.\n"
        f"3. Calculate the resistance ($R$) of this conductor.\n"
        f"4. Describe on a microscopic level what causes resistance when electrons drift through a metal conductor."
    )
    ans = (
        f"1. A material's opposition to the flow of electric charge (ratio of potential difference to current); "
        f"2. Ohm (\\Omega), 1 \\Omega = 1 V/A (one volt per ampere); "
        f"3. R = {_fmt(r_val)} \\Omega; "
        f"4. Drifting free electrons collide with vibrating positive metal ions in the crystal lattice, transferring kinetic energy to the lattice as heat."
    )
    sol = (
        f"1. **Electrical resistance:** The opposition that a substance offers to the flow of electric charge (defined as $R = \\frac{{V}}{{I}}$) [1M].\n"
        f"2. The SI unit is the **Ohm ($\\Omega$)**. One ohm is defined as one volt per ampere ($1\\ \\Omega = 1\\text{{ V}}\\cdot\\text{{A}}^{{-1}}$) [1M].\n"
        f"3. $R = \\frac{{V}}{{I}} = \\frac{{{_fmt(v_val)}\\text{{ V}}}}{{{_fmt(i_val)}\\text{{ A}}}} = {_fmt(r_val)}\\ \\Omega$ [1A].\n"
        f"4. **Microscopic cause:** As conduction electrons drift under the electric field, they undergo repeated collisions with the vibrating positive metal cations forming the crystal lattice. These collisions impede electron motion and convert electrical kinetic energy into thermal energy (heat) [1M]."
    )
    return _make_q(
        r, "26_resistance_definition_ratio_V_I", 26, prompt, ans, sol, 4,
        ["resistance_is_friction_only_misconception", "formula_inversion_error"],
        [
            {"id": "mp1", "desc": "Definition of electrical resistance", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Unit Ohm = Volt / Ampere", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation R = {_fmt(r_val)} Ohm", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Microscopic collision explanation with lattice ions", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$R = \\frac{V}{I}$. 1 Ohm = 1 Volt per Ampere.",
            "tier_2": f"Divide voltage ({_fmt(v_val)} V) by current ({_fmt(i_val)} A).",
            "tier_3": f"R = {_fmt(r_val)} Ohm. Microscopic collisions cause resistance.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 27. Resistance: Factors Affecting Resistance (L, A, T, Material)
# =========================================================================== #
def _build_27_factors_affecting_conductor_resistance(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r_initial = r.choice([4.0, 6.0, 8.0, 10.0, 12.0])
    factor_l = r.choice([2, 3])
    factor_a = r.choice([2, 4])
    r_longer = round(r_initial * factor_l, 1)
    r_thicker = round(r_initial / factor_a, 2)

    prompt = (
        f"A cylindrical copper conducting wire has an initial resistance of **${_fmt(r_initial)}\\ \\Omega$**.\n\n"
        f"1. State the four physical factors that influence the resistance of a metallic conductor.\n"
        f"2. Calculate the resistance of a second copper wire of the same thickness but **{factor_l} times longer**.\n"
        f"3. Calculate the resistance of a third copper wire of the original length but with **{factor_a} times the cross-sectional area**.\n"
        f"4. Explain what happens to the resistance of a metallic conductor when its temperature is increased."
    )
    ans = (
        f"1. Length, cross-sectional area (thickness), temperature, and type of material (resistivity); "
        f"2. R = {_fmt(r_longer)} \\Omega; 3. R = {_fmt(r_thicker)} \\Omega; "
        f"4. Resistance increases: higher temperature causes metal ions in the lattice to vibrate with greater amplitude, increasing the frequency of collisions with drifting electrons."
    )
    sol = (
        f"1. Four factors affecting resistance [1M]:\n"
        f"   - **Length ($L$):** $R \\propto L$\n"
        f"   - **Cross-sectional area ($A$):** $R \\propto \\frac{{1}}{{A}}$\n"
        f"   - **Temperature ($T$):** In metals, higher $T$ increases $R$\n"
        f"   - **Type of material:** Inherent resistivity (e.g. copper vs nichrome)\n"
        f"2. Length: $R_2 = R_1 \\times {factor_l} = {_fmt(r_initial)} \\times {factor_l} = {_fmt(r_longer)}\\ \\Omega$ [1M].\n"
        f"3. Area: $R_3 = \\frac{{R_1}}{{{factor_a}}} = \\frac{{{_fmt(r_initial)}}}{{{factor_a}}} = {_fmt(r_thicker)}\\ \\Omega$ [1M].\n"
        f"4. When temperature rises, lattice cations gain thermal kinetic energy and vibrate more vigorously, presenting a larger effective collision cross-section that slows down electron drift, thereby **increasing resistance** [1A]."
    )
    return _make_q(
        r, "27_factors_affecting_conductor_resistance", 27, prompt, ans, sol, 4,
        ["thickness_increases_resistance_fallacy", "temperature_decreases_resistance_confusion"],
        [
            {"id": "mp1", "desc": "Four physical factors named correctly", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation for length scaling R = {_fmt(r_longer)} Ohm", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation for area scaling R = {_fmt(r_thicker)} Ohm", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Temperature mechanism explanation (lattice vibrations)", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$R \\propto L$ and $R \\propto \\frac{1}{A}$. Higher temperature increases resistance in metals.",
            "tier_2": f"Longer: multiply by {factor_l}. Thicker: divide by {factor_a}.",
            "tier_3": f"R_longer = {_fmt(r_longer)} Ohm; R_thicker = {_fmt(r_thicker)} Ohm.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 28. Resistance: Ohmic vs Non-Ohmic Conductors (V-I Characteristics)
# =========================================================================== #
def _build_28_ohmic_vs_non_ohmic_conductors(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r_val = r.choice([5, 10, 15, 20])
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">V-I Characteristic Curves: Conductor A vs Conductor B</text>'
        f'<line x1="60" y1="160" x2="400" y2="160" stroke="#334155" stroke-width="2"/>'
        f'<line x1="60" y1="160" x2="60" y2="30" stroke="#334155" stroke-width="2"/>'
        f'<text x="410" y="165" font-size="11" fill="#334155">I (A)</text>'
        f'<text x="50" y="25" text-anchor="middle" font-size="11" fill="#334155">V (V)</text>'
        f'<line x1="60" y1="160" x2="360" y2="50" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="365" y="55" font-size="11" font-weight="bold" fill="#2563eb">Conductor A (Ohmic Resistor, {r_val} Ω)</text>'
        f'<path d="M 60 160 Q 220 150, 360 70" fill="none" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="365" y="85" font-size="11" font-weight="bold" fill="#dc2626">Conductor B (Filament Lamp)</text>'
        f'</svg>'
    )
    prompt = (
        f"Refer to the V-I characteristic graph illustrating potential difference ($V$) versus current ($I$) for two circuit components, **Conductor A** and **Conductor B**.\n\n"
        f"1. State **Ohm's Law** in words.\n"
        f"2. Identify which conductor (A or B) is an **ohmic conductor**, giving a reason based on the graph.\n"
        f"3. Explain why the gradient of Conductor B steepens as current increases (i.e. why a filament lamp is non-ohmic).\n"
        f"4. State the physical condition that must remain constant for a metallic conductor to strictly obey Ohm's Law."
    )
    ans = (
        f"1. Potential difference across a conductor is directly proportional to the current through it, provided temperature remains constant; "
        f"2. Conductor A: straight line graph passing through the origin indicating constant resistance (constant V/I ratio); "
        f"3. As current increases, the filament heats up; higher temperature increases lattice vibrations, increasing resistance, so greater voltage is needed per unit current; "
        f"4. Constant temperature."
    )
    sol = (
        f"1. **Ohm's Law:** The potential difference across a conductor is directly proportional to the current flowing through it, provided its temperature remains constant [1M].\n"
        f"2. **Conductor A** is ohmic because its $V-I$ graph is a **linear straight line passing through the origin**, demonstrating that the ratio $\\frac{{V}}{{I}} = R$ is constant [1M].\n"
        f"3. **Conductor B** represents a filament bulb. As current increases, the tungsten wire heats up drastically. Elevated temperature increases lattice vibrations, thereby increasing the filament's resistance ($R$). Hence the graph curves upward, requiring disproportionately larger voltage to increase current [1M].\n"
        f"4. The physical condition is **constant temperature** [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "28_ohmic_vs_non_ohmic_conductors", 28, prompt, ans, sol, 4,
        ["all_conductors_obey_ohms_law_fallacy", "confuses_ohmic_and_non_ohmic_graphs"],
        [
            {"id": "mp1", "desc": "Statement of Ohm's Law", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Identification of Conductor A with straight line reasoning", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Filament bulb heating mechanism for non-ohmic behavior", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Constant temperature condition specified", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Ohm's law: $V \\propto I$ at constant temperature. Straight line through origin = ohmic.",
            "tier_2": "Conductor A is a straight line $\\rightarrow$ ohmic. Conductor B curves as temperature increases.",
            "tier_3": "1. Conductor A is ohmic. 2. Temperature must remain constant.",
        },
        diagram_spec=diag, weight=14, duration=5,
    )


# =========================================================================== #
# 29. Resistance: Gradient Calculation from V-I Graph
# =========================================================================== #
def _build_29_ohmic_resistor_gradient_calculation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r_val = r.choice([4.0, 5.0, 8.0, 10.0, 12.0, 15.0])
    i1, i2 = 0.5, 2.5
    v1 = round(i1 * r_val, 1)
    v2 = round(i2 * r_val, 1)
    delta_v = round(v2 - v1, 1)
    delta_i = round(i2 - i1, 1)

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">V vs I Graph for an Ohmic Resistor</text>'
        f'<line x1="70" y1="160" x2="400" y2="160" stroke="#334155" stroke-width="2"/>'
        f'<line x1="70" y1="160" x2="70" y2="40" stroke="#334155" stroke-width="2"/>'
        f'<text x="410" y="165" font-size="11" fill="#334155">I (A)</text>'
        f'<text x="50" y="35" text-anchor="middle" font-size="11" fill="#334155">V (V)</text>'
        f'<line x1="70" y1="160" x2="350" y2="50" stroke="#0ea5e9" stroke-width="2.5"/>'
        f'<circle cx="140" cy="132" r="4" fill="#ef4444"/>'
        f'<text x="140" y="150" text-anchor="middle" font-size="10">({_fmt(i1)}, {_fmt(v1)})</text>'
        f'<circle cx="315" cy="64" r="4" fill="#ef4444"/>'
        f'<text x="315" y="52" text-anchor="middle" font-size="10">({_fmt(i2)}, {_fmt(v2)})</text>'
        f'<line x1="140" y1="132" x2="315" y2="132" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<line x1="315" y1="132" x2="315" y2="64" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'</svg>'
    )
    prompt = (
        f"Refer to the V-I characteristic graph illustrating potential difference ($V$) on the vertical axis versus current ($I$) on the horizontal axis for an ohmic resistor. "
        f"Two identified coordinates on the line are **(${_fmt(i1)}\\text{{ A}}, {_fmt(v1)}\\text{{ V}}$)** and "
        f"**(${_fmt(i2)}\\text{{ A}}, {_fmt(v2)}\\text{{ V}}$)**.\n\n"
        f"1. Explain what physical quantity is represented by the gradient (slope) of a $V\\text{{ vs }}I$ graph.\n"
        f"2. Calculate the gradient of the graph, showing the change in potential difference ($\\Delta V$) and change in current ($\\Delta I$).\n"
        f"3. State the resistance of the resistor with correct units.\n"
        f"4. If current was plotted on the vertical axis and potential difference on the horizontal axis ($I\\text{{ vs }}V$), state what the gradient would represent."
    )
    ans = (
        f"1. Resistance (R); 2. Gradient = Delta V / Delta I = {_fmt(delta_v)} / {_fmt(delta_i)} = {_fmt(r_val)}; "
        f"3. R = {_fmt(r_val)} \\Omega; 4. Conductance or the reciprocal of resistance (1/R)."
    )
    sol = (
        f"1. For a $V\\text{{ vs }}I$ graph, $\\text{{Gradient}} = \\frac{{\\Delta V}}{{\\Delta I}} = R$ (Resistance) [1M].\n"
        f"2. $\\Delta V = {_fmt(v2)} - {_fmt(v1)} = {_fmt(delta_v)}\\text{{ V}}$ [1M]\n"
        f"   $\\Delta I = {_fmt(i2)} - {_fmt(i1)} = {_fmt(delta_i)}\\text{{ A}}$\n"
        f"   $\\text{{Gradient}} = \\frac{{{_fmt(delta_v)}}}{{{_fmt(delta_i)}}} = {_fmt(r_val)}$ [1M].\n"
        f"3. Resistance $R = {_fmt(r_val)}\\ \\Omega$ [1A].\n"
        f"4. For an $I\\text{{ vs }}V$ graph, $\\text{{Gradient}} = \\frac{{\\Delta I}}{{\\Delta V}} = \\frac{{1}}{{R}}$ (the reciprocal of resistance) [1M]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "29_ohmic_resistor_gradient_calculation", 29, prompt, ans, sol, 5,
        ["gradient_inverted_for_V_vs_I_graph", "missing_units_in_gradient_calculation"],
        [
            {"id": "mp1", "desc": "Gradient represents resistance R", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Delta V = {_fmt(delta_v)} V and Delta I = {_fmt(delta_i)} A", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Gradient calculation = {_fmt(r_val)}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Resistance with units R = {_fmt(r_val)} Ohm", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Reciprocal 1/R for I vs V graph", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "On a $V\\text{{ vs }}I$ graph, $\\text{{slope}} = \\frac{{\\Delta V}}{{\\Delta I}} = R$.",
            "tier_2": f"$\\Delta V = {_fmt(v2)} - {_fmt(v1)}$; $\\Delta I = {_fmt(i2)} - {_fmt(i1)}$.",
            "tier_3": f"Slope = {_fmt(r_val)}; $R = {_fmt(r_val)}\\ \\Omega$.",
        },
        diagram_spec=diag, weight=15, duration=5,
    )


# =========================================================================== #
# 30. Resistance: Unknown Resistor from Meter Readings
# =========================================================================== #
def _build_30_calculating_unknown_resistor_from_V_and_I(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r_val = r.choice([3, 4, 6, 8, 10, 12, 15])
    i_val = r.choice([0.5, 1.0, 1.5, 2.0])
    v_val = round(i_val * r_val, 1)

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 180" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Determining Unknown Resistance Rx Using Meters</text>'
        f'<rect x="120" y="60" width="220" height="70" fill="none" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(180, 60)"><line x1="0" y1="0" x2="30" y2="0"/><line x1="30" y1="-12" x2="30" y2="12" stroke-width="2.5"/><line x1="38" y1="-7" x2="38" y2="7" stroke-width="4"/><line x1="38" y1="0" x2="70" y2="0"/><text x="35" y="-18" text-anchor="middle" font-size="10" fill="#b91c1c">Battery</text></g>'
        f'<g transform="translate(340, 95)"><circle cx="0" cy="0" r="14" fill="#ffffff" stroke="#2563eb" stroke-width="2"/><text x="0" y="4" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">A</text><text x="22" y="4" font-size="10" fill="#1d4ed8">{_fmt(i_val)} A</text></g>'
        f'<g transform="translate(230, 130)"><line x1="-50" y1="0" x2="-25" y2="0"/><rect x="-25" y="-10" width="50" height="20" fill="#f8fafc" stroke="#334155" stroke-width="2"/><line x1="25" y1="0" x2="50" y2="0"/><text x="0" y="4" text-anchor="middle" font-size="10" font-weight="bold">Rx</text></g>'
        f'<g transform="translate(230, 160)"><line x1="-25" y1="-30" x2="-25" y2="0"/><line x1="-25" y1="0" x2="25" y2="0"/><line x1="25" y1="0" x2="25" y2="-30"/><circle cx="0" cy="0" r="12" fill="#ffffff" stroke="#0ea5e9" stroke-width="2"/><text x="0" y="4" text-anchor="middle" font-size="10" font-weight="bold" fill="#0369a1">V</text><text x="0" y="16" text-anchor="middle" font-size="9" fill="#0284c7">{_fmt(v_val)} V</text></g>'
        f'</svg>'
    )
    prompt = (
        f"In the circuit diagram illustrated, an unknown resistor **$R_x$** is connected to a battery. "
        f"An ammeter connected in series reads **${_fmt(i_val)}\\text{{ A}}$**, while a voltmeter connected in parallel across $R_x$ reads **${_fmt(v_val)}\\text{{ V}}$**.\n\n"
        f"1. State the formula of Ohm's Law used to calculate resistance.\n"
        f"2. Calculate the resistance of the unknown resistor $R_x$.\n"
        f"3. Explain why the ammeter reading is identical before and after resistor $R_x$."
    )
    ans = (
        f"1. R = V / I; 2. Rx = {_fmt(r_val)} \\Omega; "
        f"3. Current is the rate of flow of charge; charge is conserved in a single unbranched circuit loop and is not 'consumed' by resistors."
    )
    sol = (
        f"1. $R = \\frac{{V}}{{I}}$ [1M].\n"
        f"2. $R_x = \\frac{{V}}{{I}} = \\frac{{{_fmt(v_val)}\\text{{ V}}}}{{{_fmt(i_val)}\\text{{ A}}}} = {_fmt(r_val)}\\ \\Omega$ [2M].\n"
        f"3. Resistors do not 'use up' or consume current. Electric charge is conserved; the number of coulombs entering the resistor per second must equal the number exiting per second [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "30_calculating_unknown_resistor_from_V_and_I", 30, prompt, ans, sol, 4,
        ["current_consumed_misconception", "formula_multiplication_error"],
        [
            {"id": "mp1", "desc": "Formula R = V / I", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Substitution and calculation of Rx = {_fmt(r_val)} Ohm", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Current conservation explanation (charge not used up)", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$R = \\frac{V}{I}$. Divide voltmeter reading by ammeter reading.",
            "tier_2": f"Rx = {_fmt(v_val)} V / {_fmt(i_val)} A.",
            "tier_3": f"Rx = {_fmt(r_val)} Ohm. Current is conserved through the resistor.",
        },
        diagram_spec=diag, weight=12, duration=4,
    )


# =========================================================================== #
# 31. Series Resistors: Two Resistors Equivalent Resistance (Rs = R1 + R2)
# =========================================================================== #
def _build_31_series_equivalent_resistance_two_resistors(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r1 = r.choice([3, 4, 5, 6, 8, 12])
    r2 = r.choice([2, 5, 7, 10, 15, 18])
    rs = r1 + r2

    prompt = (
        f"Two resistors with resistances **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$** are connected in series.\n\n"
        f"1. State the formula for the equivalent resistance of resistors connected in series.\n"
        f"2. Calculate the total equivalent resistance ($R_s$) of the combination.\n"
        f"3. Explain why the equivalent resistance of a series combination is always greater than any individual resistor in the series."
    )
    ans = (
        f"1. Rs = R1 + R2; 2. Rs = {rs} \\Omega; "
        f"3. In series, charge must pass consecutively through each resistor, effectively increasing the total length of the resisting path (R proportional to L)."
    )
    sol = (
        f"1. For series resistors: $R_s = R_1 + R_2 + \\dots$ [1M].\n"
        f"2. $R_s = {r1}\\ \\Omega + {r2}\\ \\Omega = {rs}\\ \\Omega$ [1A].\n"
        f"3. Connecting resistors in series forces the electric current to traverse each resistor one after the other. This effectively increases the total length of resisting conductor ($R \\propto L$), so total opposition is the sum of the individual resistances and is therefore greater than any single resistor [1M]."
    )
    return _make_q(
        r, "31_series_equivalent_resistance_two_resistors", 31, prompt, ans, sol, 3,
        ["series_parallel_formula_confusion", "inverts_series_addition"],
        [
            {"id": "mp1", "desc": "Formula Rs = R1 + R2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation of Rs = {rs} Ohm", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Effective length increase explanation", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "In series, simply add the resistances: $R_s = R_1 + R_2$.",
            "tier_2": f"Add {r1} + {r2}.",
            "tier_3": f"Rs = {rs} Ohm.",
        },
        weight=10, duration=3,
    )


# =========================================================================== #
# 32. Series Resistors: Three Resistors with Decimals
# =========================================================================== #
def _build_32_series_equivalent_resistance_three_resistors(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r1 = r.choice([0.5, 1.2, 1.5, 2.4, 3.5])
    r2 = r.choice([4.0, 5.5, 6.2, 7.5, 8.0])
    r3 = r.choice([10.0, 11.5, 12.0, 15.6])
    rs = round(r1 + r2 + r3, 2)

    prompt = (
        f"A series circuit contains three resistors: **$R_1 = {_fmt(r1)}\\ \\Omega$**, "
        f"**$R_2 = {_fmt(r2)}\\ \\Omega$**, and **$R_3 = {_fmt(r3)}\\ \\Omega$**.\n\n"
        f"1. Write down the equation for the total resistance of three series resistors.\n"
        f"2. Calculate the total equivalent resistance ($R_s$) of the circuit.\n"
        f"3. If a fourth resistor of $5\\ \\Omega$ is added in series, predict whether the total current in the circuit will increase, decrease, or remain constant (assuming supply voltage is fixed)."
    )
    ans = (
        f"1. Rs = R1 + R2 + R3; 2. Rs = {_fmt(rs)} \\Omega; 3. Total current will decrease."
    )
    sol = (
        f"1. $R_s = R_1 + R_2 + R_3$ [1M].\n"
        f"2. $R_s = {_fmt(r1)} + {_fmt(r2)} + {_fmt(r3)} = {_fmt(rs)}\\ \\Omega$ [1A].\n"
        f"3. Adding another resistor in series **increases the total circuit resistance** ($R_s$). By Ohm's law ($I = \\frac{{V}}{{R_s}}$), with voltage constant, the total current will **decrease** [1A]."
    )
    return _make_q(
        r, "32_series_equivalent_resistance_three_resistors", 32, prompt, ans, sol, 3,
        ["adding_resistor_increases_current_fallacy", "decimal_arithmetic_error"],
        [
            {"id": "mp1", "desc": "Formula Rs = R1 + R2 + R3", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation of Rs = {_fmt(rs)} Ohm", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Prediction that current decreases when series R increases", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$R_s = R_1 + R_2 + R_3$. Adding resistors in series increases total resistance, reducing current.",
            "tier_2": f"Sum: {_fmt(r1)} + {_fmt(r2)} + {_fmt(r3)}.",
            "tier_3": f"Rs = {_fmt(rs)} Ohm. Current decreases.",
        },
        weight=10, duration=3,
    )


# =========================================================================== #
# 33. Series Circuits: Current Conservation Throughout Single Loop
# =========================================================================== #
def _build_33_series_circuit_current_conservation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    i_tot = r.choice([0.5, 0.8, 1.2, 1.5, 2.0, 2.5, 3.0])
    r1 = r.choice([2, 3, 4, 5, 6])
    r2 = r.choice([3, 4, 5, 6, 8, 10])
    v1 = round(i_tot * r1, 2)
    v2 = round(i_tot * r2, 2)
    v_batt = round(v1 + v2, 2)

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 170" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Current Conservation in a Series Circuit</text>'
        f'<rect x="100" y="55" width="260" height="80" fill="none" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(210, 55)"><line x1="0" y1="0" x2="20" y2="0"/><line x1="20" y1="-10" x2="20" y2="10" stroke-width="2.5"/><line x1="28" y1="-6" x2="28" y2="6" stroke-width="4"/><line x1="28" y1="0" x2="50" y2="0"/><text x="25" y="-16" text-anchor="middle" font-size="10" fill="#b91c1c">{_fmt(v_batt)} V</text></g>'
        f'<g transform="translate(100, 95)"><circle cx="0" cy="0" r="12" fill="#ffffff" stroke="#2563eb" stroke-width="2"/><text x="0" y="4" text-anchor="middle" font-size="10" font-weight="bold" fill="#1d4ed8">A1</text><text x="-25" y="4" text-anchor="end" font-size="9" fill="#1d4ed8">{_fmt(i_tot)} A</text></g>'
        f'<g transform="translate(230, 135)"><circle cx="0" cy="0" r="12" fill="#ffffff" stroke="#2563eb" stroke-width="2"/><text x="0" y="4" text-anchor="middle" font-size="10" font-weight="bold" fill="#1d4ed8">A2</text></g>'
        f'<g transform="translate(360, 95)"><circle cx="0" cy="0" r="12" fill="#ffffff" stroke="#2563eb" stroke-width="2"/><text x="0" y="4" text-anchor="middle" font-size="10" font-weight="bold" fill="#1d4ed8">A3</text></g>'
        f'<g transform="translate(160, 135)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R1 ({r1} Ω)</text></g>'
        f'<g transform="translate(300, 135)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R2 ({r2} Ω)</text></g>'
        f'</svg>'
    )
    prompt = (
        f"In the circuit diagram illustrated, two resistors **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$** are connected in series with a **${_fmt(v_batt)}\\text{{ V}}$** battery. "
        f"Three ammeters, **A1**, **A2**, and **A3**, are positioned at different points along the circuit loop. "
        f"Ammeter A1 registers a reading of **${_fmt(i_tot)}\\text{{ A}}$**.\n\n"
        f"1. State the readings on ammeters **A2** and **A3**.\n"
        f"2. Explain the fundamental physical principle governing current in a series circuit.\n"
        f"3. Calculate the potential difference ($V_1$) across resistor $R_1$.\n"
        f"4. A learner claims that ammeter A3 will read less current than A1 because resistor $R_1$ and $R_2$ 'use up current'. Refute this misconception with scientific reasoning."
    )
    ans = (
        f"1. A2 = {_fmt(i_tot)} A, A3 = {_fmt(i_tot)} A; "
        f"2. Current is the same at all points in a series circuit (I_tot = I1 = I2); "
        f"3. V1 = {_fmt(v1)} V; "
        f"4. Current is the rate of flow of charge, not energy. Resistors consume electrical energy (voltage), but electric charge is conserved and cannot accumulate or disappear in a closed single-loop circuit."
    )
    sol = (
        f"1. Readings: $A_2 = {_fmt(i_tot)}\\text{{ A}}$ and $A_3 = {_fmt(i_tot)}\\text{{ A}}$ [1M].\n"
        f"2. In a series circuit, there is **only one continuous path** for charge carriers to travel. Therefore, the rate of flow of charge (current) is identical at every point in the circuit: $I_{{\\text{{total}}}} = I_1 = I_2 = I_3$ [1M].\n"
        f"3. $V_1 = I \\times R_1 = ({_fmt(i_tot)}\\text{{ A}}) \\times ({r1}\\ \\Omega) = {_fmt(v1)}\\text{{ V}}$ [1A].\n"
        f"4. **Refutation:** Resistors do **not** consume current. They transform **potential energy** into thermal/light energy. Conservation of charge dictates that every coulomb of electrons that enters a resistor must exit it simultaneously: current is strictly conserved [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "i_tot": i_tot, "r1": r1, "r2": r2, "v_batt": v_batt}
    return _make_q(
        r, "33_series_circuit_current_conservation", 33, prompt, ans, sol, 4,
        ["current_consumed_misconception", "attenuation_model_of_current"],
        [
            {"id": "mp1", "desc": f"Meter readings A2 = A3 = {_fmt(i_tot)} A", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Statement that current is same everywhere in series", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of V1 = {_fmt(v1)} V", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Scientific refutation of current consumption misconception", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "There is only one path for current in series: current is identical everywhere! $V_1 = I \\times R_1$.",
            "tier_2": f"A1 = {_fmt(i_tot)} A, so A2 = {_fmt(i_tot)} A and A3 = {_fmt(i_tot)} A. V1 = {_fmt(i_tot)} * {r1}.",
            "tier_3": f"All ammeters read {_fmt(i_tot)} A. V1 = {_fmt(v1)} V. Charges are not consumed.",
        },
        diagram_spec=diag, weight=12, duration=4,
    )


# =========================================================================== #
# 34. Series Circuits: Potential Division (V_tot = V1 + V2 + ...)
# =========================================================================== #
def _build_34_series_circuit_potential_division(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    v_batt = r.choice([12.0, 18.0, 24.0])
    v1 = round(r.choice([3.0, 4.0, 5.0, 6.0, 7.5]), 1)
    v2 = round(v_batt - v1, 1)

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 180" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Voltage Division in a Series Circuit</text>'
        f'<rect x="100" y="55" width="260" height="70" fill="none" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(210, 55)"><line x1="0" y1="0" x2="20" y2="0"/><line x1="20" y1="-10" x2="20" y2="10" stroke-width="2.5"/><line x1="28" y1="-6" x2="28" y2="6" stroke-width="4"/><line x1="28" y1="0" x2="50" y2="0"/><text x="25" y="-16" text-anchor="middle" font-size="10" fill="#b91c1c">Battery ({_fmt(v_batt)} V)</text></g>'
        f'<g transform="translate(160, 125)"><rect x="-20" y="-10" width="40" height="20" fill="#f8fafc" stroke="#334155" stroke-width="1.8"/><text x="0" y="5" text-anchor="middle" font-size="10">R1</text></g>'
        f'<g transform="translate(300, 125)"><rect x="-20" y="-10" width="40" height="20" fill="#f8fafc" stroke="#334155" stroke-width="1.8"/><text x="0" y="5" text-anchor="middle" font-size="10">R2</text></g>'
        f'<g transform="translate(160, 160)"><circle cx="0" cy="0" r="11" fill="#ffffff" stroke="#0ea5e9" stroke-width="2"/><text x="0" y="4" text-anchor="middle" font-size="9" font-weight="bold" fill="#0369a1">V1</text><text x="0" y="-14" text-anchor="middle" font-size="8" fill="#0284c7">{_fmt(v1)} V</text></g>'
        f'<g transform="translate(300, 160)"><circle cx="0" cy="0" r="11" fill="#ffffff" stroke="#0ea5e9" stroke-width="2"/><text x="0" y="4" text-anchor="middle" font-size="9" font-weight="bold" fill="#0369a1">V2</text><text x="0" y="-14" text-anchor="middle" font-size="8" fill="#0284c7">?</text></g>'
        f'</svg>'
    )
    prompt = (
        f"In the circuit diagram illustrated, two resistors $R_1$ and $R_2$ are connected in series with a **${_fmt(v_batt)}\\text{{ V}}$** battery. "
        f"Voltmeter $V_1$ connected across $R_1$ reads **${_fmt(v1)}\\text{{ V}}$**.\n\n"
        f"1. State the principle of potential division for resistors in series.\n"
        f"2. Calculate the reading on voltmeter **$V_2$** connected across resistor $R_2$.\n"
        f"3. If $R_1 < R_2$, explain which resistor dissipates more electrical energy per second."
    )
    ans = (
        f"1. The total potential difference across the battery equals the sum of the potential differences across each individual series resistor (V_tot = V1 + V2); "
        f"2. V2 = {_fmt(v2)} V; "
        f"3. R2: since current is identical in both series resistors (P = I^2 R or P = V*I), the resistor with higher resistance drops more voltage and dissipates more energy per second."
    )
    sol = (
        f"1. In a series circuit, total voltage is divided among the series components: $V_{{\\text{{total}}}} = V_1 + V_2$ [1M].\n"
        f"2. $V_2 = V_{{\\text{{total}}}} - V_1 = {_fmt(v_batt)} - {_fmt(v1)} = {_fmt(v2)}\\text{{ V}}$ [1A].\n"
        f"3. Since current is the same through both resistors ($I_1 = I_2$), power dissipation is $P = I^2 R$. Because $R_2 > R_1$, **resistor $R_2$ drops more potential difference ($V_2 > V_1$) and dissipates more energy per second** [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "34_series_circuit_potential_division", 34, prompt, ans, sol, 3,
        ["equal_voltage_split_assumption_fallacy", "voltage_same_in_series_confusion"],
        [
            {"id": "mp1", "desc": "Statement of voltage division V_tot = V1 + V2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation of V2 = {_fmt(v2)} V", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Energy dissipation comparison (higher R drops more V)", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$V_{\\text{total}} = V_1 + V_2$. Subtract $V_1$ from battery voltage.",
            "tier_2": f"V2 = {_fmt(v_batt)} V - {_fmt(v1)} V.",
            "tier_3": f"V2 = {_fmt(v2)} V. Resistor R2 dissipates more energy.",
        },
        diagram_spec=diag, weight=12, duration=4,
    )


# =========================================================================== #
# 35. Series Circuits: Voltage Divider Ratio Calculation
# =========================================================================== #
def _build_35_series_voltage_divider_ratio(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r1 = r.choice([2, 3, 4, 6])
    r2 = r.choice([6, 8, 12, 14])
    rs = r1 + r2
    v_tot = r.choice([12, 18, 24, 30])
    v1 = round((r1 / rs) * v_tot, 2)
    v2 = round((r2 / rs) * v_tot, 2)

    prompt = (
        f"Two resistors, **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**, are connected in series across a "
        f"**${v_tot}\\text{{ V}}$** power supply.\n\n"
        f"1. State the ratio of potential differences across the two resistors ($V_1 : V_2$) in simplified integer form.\n"
        f"2. Use the voltage divider formula ($V_1 = \\frac{{R_1}}{{R_s}} \\times V_{{\\text{{total}}}}$) to calculate the potential difference across $R_1$.\n"
        f"3. Calculate the potential difference across $R_2$."
    )
    g = math.gcd(r1, r2)
    ratio_str = f"{r1 // g} : {r2 // g}"
    ans = f"1. V1 : V2 = {ratio_str}; 2. V1 = {_fmt(v1)} V; 3. V2 = {_fmt(v2)} V."
    sol = (
        f"1. Voltage divides in direct proportion to resistance: $V_1 : V_2 = R_1 : R_2 = {r1} : {r2} = \\mathbf{{{ratio_str}}}$ [1M].\n"
        f"2. $R_s = R_1 + R_2 = {r1} + {r2} = {rs}\\ \\Omega$ [1M].\n"
        f"   $V_1 = \\frac{{R_1}}{{R_s}} \\times V_{{\\text{{total}}}} = \\frac{{{r1}}}{{{rs}}} \\times {v_tot} = {_fmt(v1)}\\text{{ V}}$ [1A].\n"
        f"3. $V_2 = \\frac{{R_2}}{{R_s}} \\times V_{{\\text{{total}}}} = \\frac{{{r2}}}{{{rs}}} \\times {v_tot} = {_fmt(v2)}\\text{{ V}}$ (or $V_2 = {v_tot} - {_fmt(v1)} = {_fmt(v2)}\\text{{ V}}$) [1A]."
    )
    return _make_q(
        r, "35_series_voltage_divider_ratio", 35, prompt, ans, sol, 4,
        ["inverse_ratio_voltage_division_error", "fractional_voltage_divider_error"],
        [
            {"id": "mp1", "desc": f"Ratio V1 : V2 = {ratio_str}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Rs calculation = {rs} Ohm", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of V1 = {_fmt(v1)} V", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculation of V2 = {_fmt(v2)} V", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$V_1 = \\frac{R_1}{R_1 + R_2} \\times V_{\\text{total}}$.",
            "tier_2": f"Total resistance = {rs} Ohm. $V_1 = ({r1}/{rs}) \\times {v_tot}$.",
            "tier_3": f"V1 = {_fmt(v1)} V, V2 = {_fmt(v2)} V.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 36. Series Circuits: Fault Finding (Open Switch or Blown Bulb)
# =========================================================================== #
def _build_36_series_circuit_fault_finding_open_switch_or_bulb(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    v_batt = r.choice([6.0, 9.0, 12.0, 24.0])
    r1 = r.choice([3, 5, 8])

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 180" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Fault Finding: Open Circuit Break in Series Loop</text>'
        f'<rect x="100" y="55" width="260" height="70" fill="none" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(210, 55)"><line x1="0" y1="0" x2="20" y2="0"/><line x1="20" y1="-10" x2="20" y2="10" stroke-width="2.5"/><line x1="28" y1="-6" x2="28" y2="6" stroke-width="4"/><line x1="28" y1="0" x2="50" y2="0"/><text x="25" y="-16" text-anchor="middle" font-size="10" fill="#b91c1c">{_fmt(v_batt)} V</text></g>'
        f'<g transform="translate(160, 125)"><rect x="-20" y="-10" width="40" height="20" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="10">R1 ({r1} Ω)</text></g>'
        f'<g transform="translate(300, 125)"><circle cx="0" cy="0" r="14" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/><line x1="-8" y1="-8" x2="8" y2="8" stroke="#dc2626" stroke-width="2"/><line x1="-8" y1="8" x2="8" y2="-8" stroke="#dc2626" stroke-width="2"/><text x="0" y="25" text-anchor="middle" font-size="10" fill="#b91c1c">Blown Lamp L2</text></g>'
        f'<g transform="translate(100, 90)"><circle cx="0" cy="0" r="11" fill="#ffffff" stroke="#2563eb" stroke-width="2"/><text x="0" y="4" text-anchor="middle" font-size="9" font-weight="bold" fill="#1d4ed8">A</text></g>'
        f'</svg>'
    )
    prompt = (
        f"In the circuit diagram illustrated, resistor $R_1 = {r1}\\ \\Omega$ and filament lamp $L_2$ are connected in series with a **${_fmt(v_batt)}\\text{{ V}}$** battery. "
        f"During operation, the filament inside lamp $L_2$ suddenly burns out and breaks (creating an open circuit).\n\n"
        f"1. State the reading on the ammeter **A** immediately after the lamp burns out.\n"
        f"2. State the reading on a voltmeter connected across the intact resistor $R_1$.\n"
        f"3. State the reading on a voltmeter connected directly across the terminals of the blown lamp $L_2$, providing scientific reasoning for your answer."
    )
    ans = (
        f"1. Ammeter A = 0 A; 2. Voltmeter across R1 = 0 V; "
        f"3. Voltmeter across L2 = {_fmt(v_batt)} V (full battery EMF) because the break has infinite resistance and no current flows through R1, so there is zero potential drop across R1."
    )
    sol = (
        f"1. The broken filament creates an open circuit: circuit current immediately drops to **$0\\text{{ A}}$** [1M].\n"
        f"2. Voltmeter across $R_1$: by Ohm's Law, $V_1 = I \\times R_1 = 0\\text{{ A}} \\times {r1}\\ \\Omega = \\mathbf{{0\\text{{ V}}}}$ [1M].\n"
        f"3. Voltmeter across broken lamp $L_2$: reads the full battery potential difference of **${_fmt(v_batt)}\\text{{ V}}$** [1A]. "
        f"Because no current flows, there is zero voltage drop across the rest of the circuit; the voltmeter's terminals are connected directly to the positive and negative terminals of the battery via the intact leads and resistor [1M]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "36_series_circuit_fault_finding_open_switch_or_bulb", 36, prompt, ans, sol, 4,
        ["voltmeter_across_open_switch_reads_zero_fallacy", "believes_current_continues_through_break"],
        [
            {"id": "mp1", "desc": "Ammeter reading = 0 A", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Voltmeter across R1 = 0 V", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Voltmeter across break reads full EMF = {_fmt(v_batt)} V", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Scientific reasoning for full EMF across break", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "In an open circuit, current is ZERO everywhere! Voltmeter across intact resistor reads 0 V.",
            "tier_2": "A voltmeter across an open break acts like a meter across the battery: it reads full EMF.",
            "tier_3": f"A = 0 A; V_R1 = 0 V; V_break = {_fmt(v_batt)} V.",
        },
        diagram_spec=diag, weight=14, duration=5,
    )


# =========================================================================== #
# 37. Parallel Resistors: Two Identical Resistors (Rp = R / 2)
# =========================================================================== #
def _build_37_parallel_equivalent_resistance_two_identical(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r_val = r.choice([4, 6, 8, 10, 12, 16, 20])
    rp = r_val / 2

    prompt = (
        f"Two identical resistors, each having a resistance of **${r_val}\\ \\Omega$**, are connected in parallel with each other.\n\n"
        f"1. State the formula for the equivalent resistance ($R_p$) of two resistors connected in parallel.\n"
        f"2. Calculate the equivalent resistance of this parallel combination.\n"
        f"3. State the general rule regarding the equivalent resistance of identical parallel resistors.\n"
        f"4. Explain why adding an identical resistor in parallel reduces the overall resistance of the circuit."
    )
    ans = (
        f"1. 1/Rp = 1/R1 + 1/R2; 2. Rp = {_fmt(rp)} \\Omega; "
        f"3. For n identical resistors R in parallel, Rp = R / n; "
        f"4. Adding parallel branches provides additional alternative pathways for charge carriers, effectively increasing the total cross-sectional area available for flow."
    )
    sol = (
        f"1. Parallel resistance formula: $\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_2}}$ [1M].\n"
        f"2. $\\frac{{1}}{{R_p}} = \\frac{{1}}{{{r_val}}} + \\frac{{1}}{{{r_val}}} = \\frac{{2}}{{{r_val}}} \\implies R_p = \\frac{{{r_val}}}{{2}} = {_fmt(rp)}\\ \\Omega$ [1A].\n"
        f"3. For $N$ identical resistors in parallel: $R_p = \\frac{{R}}{{N}}$ [1M].\n"
        f"4. Each added parallel branch creates an independent route for electrons to travel. This effectively increases the total cross-sectional area of conduction ($R \\propto \\frac{{1}}{{A}}$), allowing more total current to flow for the same voltage [1A]."
    )
    return _make_q(
        r, "37_parallel_equivalent_resistance_two_identical", 37, prompt, ans, sol, 4,
        ["adding_resistors_always_increases_resistance_fallacy", "forgot_to_invert_reciprocal"],
        [
            {"id": "mp1", "desc": "Formula 1/Rp = 1/R1 + 1/R2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation of Rp = {_fmt(rp)} Ohm", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "General rule Rp = R / n", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Effective area increase explanation", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "For two identical resistors in parallel, simply divide by 2: $R_p = \\frac{R}{2}$.",
            "tier_2": f"Rp = {r_val} / 2.",
            "tier_3": f"Rp = {_fmt(rp)} Ohm. Parallel branches add pathways.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 38. Parallel Resistors: Two Different Resistors
# =========================================================================== #
def _build_38_parallel_equivalent_resistance_two_different(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    pairs = [(2, 3), (3, 6), (4, 12), (6, 12), (5, 20), (10, 15), (6, 9), (4, 6)]
    r1, r2 = r.choice(pairs)
    rp = (r1 * r2) / (r1 + r2)

    prompt = (
        f"Two resistors with resistances **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$** are connected in parallel.\n\n"
        f"1. Write down the reciprocal formula for two parallel resistors: $\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_2}}$.\n"
        f"2. Calculate the equivalent resistance ($R_p$) of the combination.\n"
        f"3. Verify that the calculated equivalent resistance is smaller than the resistance of the smallest individual resistor."
    )
    ans = (
        f"1. 1/Rp = 1/R1 + 1/R2; 2. Rp = {_fmt(rp)} \\Omega; "
        f"3. {_fmt(rp)} \\Omega is less than {min(r1, r2)} \\Omega; verified."
    )
    sol = (
        f"1. $\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_2}}$ [1M].\n"
        f"2. $\\frac{{1}}{{R_p}} = \\frac{{1}}{{{r1}}} + \\frac{{1}}{{{r2}}} = \\frac{{{r1 + r2}}}{{{r1 * r2}}}$\n"
        f"   $R_p = \\frac{{{r1} \\times {r2}}}{{{r1} + {r2}}} = \\frac{{{r1 * r2}}}{{{r1 + r2}}} = {_fmt(rp)}\\ \\Omega$ [2M].\n"
        f"3. Comparison: $R_p = {_fmt(rp)}\\ \\Omega < {min(r1, r2)}\\ \\Omega$. "
        f"The equivalent resistance of any parallel network is always strictly less than the smallest individual branch resistance [1A]."
    )
    return _make_q(
        r, "38_parallel_equivalent_resistance_two_different", 38, prompt, ans, sol, 4,
        ["forgot_to_invert_reciprocal_error", "added_resistances_directly"],
        [
            {"id": "mp1", "desc": "Formula statement", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Fractional addition step", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Reciprocal inversion and calculation of Rp = {_fmt(rp)} Ohm", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Verification that Rp < {min(r1, r2)} Ohm", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Remember to flip the fraction at the end! $R_p = \\frac{R_1 R_2}{R_1 + R_2}$.",
            "tier_2": f"Product over sum: ({r1} * {r2}) / ({r1} + {r2}) = {r1 * r2} / {r1 + r2}.",
            "tier_3": f"Rp = {_fmt(rp)} Ohm. Note that {_fmt(rp)} < {min(r1, r2)}.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 39. Parallel Resistors: Three Resistors in Parallel
# =========================================================================== #
def _build_39_parallel_equivalent_resistance_three_resistors(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    triples = [(2, 3, 6), (6, 12, 12), (4, 6, 12), (10, 20, 20), (5, 10, 10), (3, 6, 6)]
    r1, r2, r3 = r.choice(triples)
    inv_sum = (1.0 / r1) + (1.0 / r2) + (1.0 / r3)
    rp = round(1.0 / inv_sum, 2)

    prompt = (
        f"Three resistors with resistances **$R_1 = {r1}\\ \\Omega$**, **$R_2 = {r2}\\ \\Omega$**, and "
        f"**$R_3 = {r3}\\ \\Omega$** are connected in parallel across an electric supply.\n\n"
        f"1. Write down the equation for the equivalent resistance of three parallel resistors.\n"
        f"2. Calculate the equivalent resistance ($R_p$) of this three-resistor combination.\n"
        f"3. If a fourth parallel branch is connected, state what happens to the total resistance of the circuit."
    )
    ans = f"1. 1/Rp = 1/R1 + 1/R2 + 1/R3; 2. Rp = {_fmt(rp)} \\Omega; 3. Total resistance will decrease further."
    sol = (
        f"1. $\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_2}} + \\frac{{1}}{{R_3}}$ [1M].\n"
        f"2. $\\frac{{1}}{{R_p}} = \\frac{{1}}{{{r1}}} + \\frac{{1}}{{{r2}}} + \\frac{{1}}{{{r3}}} = {_fmt(inv_sum, 3)}$\n"
        f"   $R_p = \\frac{{1}}{{{_fmt(inv_sum, 3)}}} = {_fmt(rp)}\\ \\Omega$ [2M].\n"
        f"3. Connecting an additional branch provides yet another parallel pathway for charge, causing total equivalent resistance to **decrease** [1A]."
    )
    return _make_q(
        r, "39_parallel_equivalent_resistance_three_resistors", 39, prompt, ans, sol, 4,
        ["three_resistors_parallel_reciprocal_error", "confuses_parallel_with_series"],
        [
            {"id": "mp1", "desc": "Formula 1/Rp = 1/R1 + 1/R2 + 1/R3", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Substitution and reciprocal summation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation of Rp = {_fmt(rp)} Ohm", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Deduction that extra branch decreases total resistance", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Add reciprocals: $\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}$. Don't forget to invert!",
            "tier_2": f"1/Rp = 1/{r1} + 1/{r2} + 1/{r3}.",
            "tier_3": f"Rp = {_fmt(rp)} Ohm. More parallel branches = lower resistance.",
        },
        weight=14, duration=4,
    )


# =========================================================================== #
# 40. Parallel Circuits: Potential Difference Equality Across Branches
# =========================================================================== #
def _build_40_parallel_circuit_potential_equality(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    v_batt = r.choice([6.0, 9.0, 12.0, 18.0])
    r1 = r.choice([3, 4, 6])
    r2 = r.choice([6, 8, 12])

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Potential Equality Across Parallel Branches</text>'
        f'<line x1="120" y1="50" x2="340" y2="50" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(210, 50)"><line x1="0" y1="0" x2="20" y2="0"/><line x1="20" y1="-10" x2="20" y2="10" stroke-width="2.5"/><line x1="28" y1="-6" x2="28" y2="6" stroke-width="4"/><line x1="28" y1="0" x2="50" y2="0"/><text x="25" y="-15" text-anchor="middle" font-size="10" fill="#b91c1c">{_fmt(v_batt)} V</text></g>'
        f'<line x1="120" y1="50" x2="120" y2="160" stroke="#334155" stroke-width="2"/>'
        f'<line x1="340" y1="50" x2="340" y2="160" stroke="#334155" stroke-width="2"/>'
        f'<line x1="120" y1="105" x2="340" y2="105" stroke="#334155" stroke-width="2"/>'
        f'<line x1="120" y1="160" x2="340" y2="160" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(230, 105)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R1 ({r1} Ω)</text></g>'
        f'<g transform="translate(230, 160)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R2 ({r2} Ω)</text></g>'
        f'<g transform="translate(370, 105)"><circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#0ea5e9" stroke-width="2"/><text x="0" y="3" text-anchor="middle" font-size="8" font-weight="bold" fill="#0369a1">V1</text></g>'
        f'<g transform="translate(370, 160)"><circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#0ea5e9" stroke-width="2"/><text x="0" y="3" text-anchor="middle" font-size="8" font-weight="bold" fill="#0369a1">V2</text></g>'
        f'</svg>'
    )
    prompt = (
        f"In the circuit diagram illustrated, two resistors $R_1 = {r1}\\ \\Omega$ and $R_2 = {r2}\\ \\Omega$ are connected in parallel across a **${_fmt(v_batt)}\\text{{ V}}$** battery. "
        f"Voltmeters $V_1$ and $V_2$ measure the potential difference across $R_1$ and $R_2$ respectively.\n\n"
        f"1. State the reading on voltmeter **$V_1$**.\n"
        f"2. State the reading on voltmeter **$V_2$**.\n"
        f"3. Explain why the potential difference is identical across both parallel branches, even though $R_1 \\neq R_2$.\n"
        f"4. State why household electrical appliances (lights, plugs, kettles) are connected in parallel rather than in series."
    )
    ans = (
        f"1. V1 = {_fmt(v_batt)} V; 2. V2 = {_fmt(v_batt)} V; "
        f"3. Both resistors are connected directly across the same two common nodes (conductors connected to battery terminals); "
        f"4. Each appliance receives full mains voltage (230 V) and operates independently (switching off or unplugging one appliance does not break the circuit for others)."
    )
    sol = (
        f"1. $V_1 = {_fmt(v_batt)}\\text{{ V}}$ [1M].\n"
        f"2. $V_2 = {_fmt(v_batt)}\\text{{ V}}$ [1M].\n"
        f"3. Both branches connect directly to the same common electrical nodes: the left ends connect to the positive terminal and the right ends to the negative terminal. Hence, the potential difference across each parallel component is identical to the source voltage: $V_{{\\text{{parallel}}}} = V_1 = V_2 = V_{{\\text{{battery}}}}$ [1M].\n"
        f"4. Household applications [1A]:\n"
        f"   - **Full operating voltage:** Every appliance operates at standard potential.\n"
        f"   - **Independent operation:** If one device is switched off or fails, other branches continue operating."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "40_parallel_circuit_potential_equality", 40, prompt, ans, sol, 4,
        ["voltage_divides_in_parallel_misconception", "resistance_affects_parallel_voltage_fallacy"],
        [
            {"id": "mp1", "desc": f"V1 reading = {_fmt(v_batt)} V", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"V2 reading = {_fmt(v_batt)} V", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Common nodes potential equality explanation", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Household parallel connection rationale", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "In parallel, potential difference is the SAME across all branches! ($V_p = V_1 = V_2$).",
            "tier_2": f"Both voltmeters read the full battery voltage: {_fmt(v_batt)} V.",
            "tier_3": f"V1 = {_fmt(v_batt)} V, V2 = {_fmt(v_batt)} V.",
        },
        diagram_spec=diag, weight=12, duration=4,
    )


# =========================================================================== #
# 41. Parallel Circuits: Current Branching (I_tot = I1 + I2)
# =========================================================================== #
def _build_41_parallel_circuit_current_branching(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    pair = r.choice([(1.2, 0.4), (1.5, 0.5), (2.0, 0.8), (1.8, 0.6), (2.4, 0.8), (1.6, 0.4), (1.4, 0.7)])
    swap = r.choice([True, False])
    i1, i2 = (pair[1], pair[0]) if swap else (pair[0], pair[1])
    i1 = round(i1, 1)
    i2 = round(i2, 1)
    i_tot = round(i1 + i2, 1)

    larger_i = max(i1, i2)
    smaller_i = min(i1, i2)
    larger_i_branch = "A1" if i1 > i2 else "A2"
    smaller_i_branch = "A2" if i1 > i2 else "A1"
    larger_r_branch = "R2" if i1 > i2 else "R1"
    smaller_r_branch = "R1" if i1 > i2 else "R2"

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Current Branching in a Parallel Circuit</text>'
        f'<line x1="80" y1="50" x2="380" y2="50" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(210, 50)"><line x1="0" y1="0" x2="20" y2="0"/><line x1="20" y1="-10" x2="20" y2="10" stroke-width="2.5"/><line x1="28" y1="-6" x2="28" y2="6" stroke-width="4"/><line x1="28" y1="0" x2="50" y2="0"/><text x="25" y="-15" text-anchor="middle" font-size="10" fill="#b91c1c">Battery</text></g>'
        f'<g transform="translate(80, 80)"><circle cx="0" cy="0" r="12" fill="#ffffff" stroke="#2563eb" stroke-width="2"/><text x="0" y="4" text-anchor="middle" font-size="10" font-weight="bold" fill="#1d4ed8">A_tot</text></g>'
        f'<line x1="80" y1="50" x2="80" y2="160" stroke="#334155" stroke-width="2"/>'
        f'<line x1="380" y1="50" x2="380" y2="160" stroke="#334155" stroke-width="2"/>'
        f'<line x1="80" y1="105" x2="380" y2="105" stroke="#334155" stroke-width="2"/>'
        f'<line x1="80" y1="160" x2="380" y2="160" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(170, 105)"><circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#2563eb" stroke-width="2"/><text x="0" y="3" text-anchor="middle" font-size="8" font-weight="bold" fill="#1d4ed8">A1</text><text x="0" y="-12" text-anchor="middle" font-size="8" fill="#1d4ed8">{_fmt(i1)} A</text></g>'
        f'<g transform="translate(250, 105)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R1</text></g>'
        f'<g transform="translate(170, 160)"><circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#2563eb" stroke-width="2"/><text x="0" y="3" text-anchor="middle" font-size="8" font-weight="bold" fill="#1d4ed8">A2</text><text x="0" y="18" text-anchor="middle" font-size="8" fill="#1d4ed8">{_fmt(i2)} A</text></g>'
        f'<g transform="translate(250, 160)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R2</text></g>'
        f'</svg>'
    )
    prompt = (
        f"In the circuit diagram illustrated, an electric circuit branches into two parallel paths containing resistors $R_1$ and $R_2$. "
        f"Ammeter $A_1$ in branch 1 reads **${_fmt(i1)}\\text{{ A}}$**, and ammeter $A_2$ in branch 2 reads **${_fmt(i2)}\\text{{ A}}$**.\n\n"
        f"1. State the relationship between total circuit current and branch currents in a parallel circuit.\n"
        f"2. Calculate the reading on the main ammeter **$A_{{\\text{{tot}}}}$**.\n"
        f"3. Comparing the two branch readings ({_fmt(i1)} A vs {_fmt(i2)} A), deduce whether resistor **$R_1$** or **$R_2$** has the larger resistance value, providing scientific reasoning based on Ohm's Law."
    )
    ans = (
        f"1. I_tot = I1 + I2; 2. A_tot = {_fmt(i_tot)} A; "
        f"3. Resistor {larger_r_branch} has the larger resistance: since voltage is identical across parallel branches (I = V / R), current is inversely proportional to resistance. The branch with smaller current ({smaller_i_branch} = {_fmt(smaller_i)} A) must have the larger resistance."
    )
    sol = (
        f"1. In a parallel circuit, total current entering a junction equals the sum of currents leaving the junction (conservation of charge): $I_{{\\text{{total}}}} = I_1 + I_2$ [1M].\n"
        f"2. $I_{{\\text{{total}}}} = {_fmt(i1)} + {_fmt(i2)} = {_fmt(i_tot)}\\text{{ A}}$ [1A].\n"
        f"3. Both parallel branches experience identical potential difference ($V_p$). By Ohm's Law, $I = \\frac{{V_p}}{{R}}$, meaning $I \\propto \\frac{{1}}{{R}}$ for constant voltage. "
        f"Because branch {smaller_i_branch} carries less current (${_fmt(smaller_i)}\\text{{ A}} < {_fmt(larger_i)}\\text{{ A}}$), "
        f"**resistor {larger_r_branch} offers greater opposition to current and therefore has the larger resistance (${larger_r_branch} > {smaller_r_branch}$)** [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "i1": i1, "i2": i2, "i_tot": i_tot}
    return _make_q(
        r, "41_parallel_circuit_current_branching", 41, prompt, ans, sol, 3,
        ["current_equal_in_parallel_branches_fallacy", "larger_current_means_larger_resistance_error"],
        [
            {"id": "mp1", "desc": "Formula I_tot = I1 + I2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation of I_tot = {_fmt(i_tot)} A", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Deduction that resistor {larger_r_branch} has larger resistance with inverse current reasoning", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$I_{\\text{total}} = I_1 + I_2$. Add the branch currents. Smaller current = larger resistance.",
            "tier_2": f"Total current = {_fmt(i1)} A + {_fmt(i2)} A = {_fmt(i_tot)} A. Notice {_fmt(smaller_i)} A < {_fmt(larger_i)} A.",
            "tier_3": f"A_tot = {_fmt(i_tot)} A. Resistor {larger_r_branch} has larger resistance because branch {smaller_i_branch} carries less current.",
        },
        diagram_spec=diag, weight=12, duration=4,
    )


# =========================================================================== #
# 42. Parallel Circuits: Current Divider Calculation
# =========================================================================== #
def _build_42_parallel_current_divider_calculation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    v_batt = r.choice([12, 24, 36])
    r1 = r.choice([4, 6, 8])
    r2 = r.choice([12, 18, 24])
    i1 = round(v_batt / r1, 2)
    i2 = round(v_batt / r2, 2)
    i_tot = round(i1 + i2, 2)

    prompt = (
        f"Two resistors, **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**, are connected in parallel across a "
        f"**${v_batt}\\text{{ V}}$** battery of negligible internal resistance.\n\n"
        f"1. Calculate the current ($I_1$) passing through resistor $R_1$.\n"
        f"2. Calculate the current ($I_2$) passing through resistor $R_2$.\n"
        f"3. Calculate the total current ($I_{{\\text{{total}}}}$) supplied by the battery.\n"
        f"4. State the ratio of currents $I_1 : I_2$ in simplified integer form."
    )
    g = math.gcd(r2, r1)
    ratio_str = f"{r2 // g} : {r1 // g}"
    ans = (
        f"1. I1 = {_fmt(i1)} A; 2. I2 = {_fmt(i2)} A; 3. I_tot = {_fmt(i_tot)} A; 4. I1 : I2 = {ratio_str}."
    )
    sol = (
        f"1. Potential difference across $R_1$ is $V_p = {v_batt}\\text{{ V}}$:\n"
        f"   $I_1 = \\frac{{V_p}}{{R_1}} = \\frac{{{v_batt}}}{{{r1}}} = {_fmt(i1)}\\text{{ A}}$ [1A].\n"
        f"2. Potential difference across $R_2$ is $V_p = {v_batt}\\text{{ V}}$:\n"
        f"   $I_2 = \\frac{{V_p}}{{R_2}} = \\frac{{{v_batt}}}{{{r2}}} = {_fmt(i2)}\\text{{ A}}$ [1A].\n"
        f"3. $I_{{\\text{{total}}}} = I_1 + I_2 = {_fmt(i1)} + {_fmt(i2)} = {_fmt(i_tot)}\\text{{ A}}$ [1M].\n"
        f"4. Current ratio: $I_1 : I_2 = \\frac{{V}}{{R_1}} : \\frac{{V}}{{R_2}} = R_2 : R_1 = {r2} : {r1} = \\mathbf{{{ratio_str}}}$ [1A]."
    )
    return _make_q(
        r, "42_parallel_current_divider_calculation", 42, prompt, ans, sol, 4,
        ["current_divider_proportional_to_R_fallacy", "branch_voltage_division_error"],
        [
            {"id": "mp1", "desc": f"Calculation of I1 = {_fmt(i1)} A", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculation of I2 = {_fmt(i2)} A", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Total current I_tot = {_fmt(i_tot)} A", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Current ratio I1 : I2 = {ratio_str}", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Each branch gets the full {v_batt} V! $I_1 = V / R_1$ and $I_2 = V / R_2$.",
            "tier_2": f"I1 = {v_batt} / {r1}; I2 = {v_batt} / {r2}.",
            "tier_3": f"I1 = {_fmt(i1)} A, I2 = {_fmt(i2)} A, I_tot = {_fmt(i_tot)} A.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 43. Combination Circuits: Series Resistor with Parallel Pair
# =========================================================================== #
def _build_43_series_parallel_network(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r1 = r.choice([2, 3, 4, 5])
    pair = r.choice([(6, 12, 4), (4, 12, 3), (10, 15, 6), (6, 3, 2), (8, 24, 6)])
    r2, r3, rp = pair
    r_tot = r1 + rp

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Series-Parallel Combination Network</text>'
        f'<line x1="80" y1="50" x2="380" y2="50" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(210, 50)"><line x1="0" y1="0" x2="20" y2="0"/><line x1="20" y1="-10" x2="20" y2="10" stroke-width="2.5"/><line x1="28" y1="-6" x2="28" y2="6" stroke-width="4"/><line x1="28" y1="0" x2="50" y2="0"/><text x="25" y="-15" text-anchor="middle" font-size="10" fill="#b91c1c">Battery</text></g>'
        f'<line x1="80" y1="50" x2="80" y2="135" stroke="#334155" stroke-width="2"/>'
        f'<line x1="380" y1="50" x2="380" y2="135" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(130, 135)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R1 ({r1} Ω)</text></g>'
        f'<line x1="80" y1="135" x2="110" y2="135" stroke="#334155" stroke-width="2"/>'
        f'<line x1="150" y1="135" x2="200" y2="135" stroke="#334155" stroke-width="2"/>'
        f'<line x1="200" y1="105" x2="200" y2="165" stroke="#334155" stroke-width="2"/>'
        f'<line x1="200" y1="105" x2="330" y2="105" stroke="#334155" stroke-width="2"/>'
        f'<line x1="200" y1="165" x2="330" y2="165" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(265, 105)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R2 ({r2} Ω)</text></g>'
        f'<g transform="translate(265, 165)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R3 ({r3} Ω)</text></g>'
        f'<line x1="330" y1="105" x2="330" y2="165" stroke="#334155" stroke-width="2"/>'
        f'<line x1="330" y1="135" x2="380" y2="135" stroke="#334155" stroke-width="2"/>'
        f'</svg>'
    )
    prompt = (
        f"In the circuit diagram illustrated, resistor **$R_1 = {r1}\\ \\Omega$** is connected in series with a parallel pair "
        f"consisting of **$R_2 = {r2}\\ \\Omega$** and **$R_3 = {r3}\\ \\Omega$**.\n\n"
        f"1. Calculate the equivalent resistance ($R_p$) of the parallel combination ($R_2 \\parallel R_3$).\n"
        f"2. Calculate the total equivalent resistance ($R_{{\\text{{total}}}}$) of the complete circuit.\n"
        f"3. Explain step-by-step the strategy used to simplify a series-parallel network."
    )
    ans = (
        f"1. Rp = {rp} \\Omega; 2. R_total = {r_tot} \\Omega; "
        f"3. First resolve the parallel branch into a single equivalent resistor Rp using 1/Rp = 1/R2 + 1/R3; then add the series resistor R1 (R_total = R1 + Rp)."
    )
    sol = (
        f"1. Parallel combination: $\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_2}} + \\frac{{1}}{{R_3}} = \\frac{{1}}{{{r2}}} + \\frac{{1}}{{{r3}}}$\n"
        f"   $R_p = \\frac{{{r2} \\times {r3}}}{{{r2} + {r3}}} = \\frac{{{r2 * r3}}}{{{r2 + r3}}} = {rp}\\ \\Omega$ [2M].\n"
        f"2. Total resistance: $R_{{\\text{{total}}}} = R_1 + R_p = {r1} + {rp} = {r_tot}\\ \\Omega$ [1A].\n"
        f"3. **Reduction Strategy:** Identify purely parallel sub-circuits and calculate their single equivalent resistance ($R_p$). "
        f"Then treat $R_p$ as a single resistor in series with $R_1$, adding them directly to find $R_{{\\text{{total}}}}$ [1M]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "43_series_parallel_network_resistor_in_series_with_parallel_pair", 43, prompt, ans, sol, 4,
        ["added_all_resistors_in_series_error", "forgot_to_add_series_component_to_Rp"],
        [
            {"id": "mp1", "desc": f"Calculation of parallel pair Rp = {rp} Ohm", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Total resistance R_tot = {r_tot} Ohm", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Step-by-step reduction strategy explanation", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Step 1: calculate parallel equivalent $R_p$. Step 2: add $R_1$ to $R_p$.",
            "tier_2": f"Rp = ({r2} * {r3}) / ({r2} + {r3}) = {rp} Ohm. R_tot = {r1} + {rp}.",
            "tier_3": f"Rp = {rp} Ohm, R_total = {r_tot} Ohm.",
        },
        diagram_spec=diag, weight=14, duration=5,
    )


# =========================================================================== #
# 44. Combination Circuits: Full Multimeter Readings Solution
# =========================================================================== #
def _build_44_series_parallel_multimeter_readings_calculation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r1 = r.choice([2, 4])
    r2, r3, rp = r.choice([(6, 12, 4), (4, 12, 3), (6, 3, 2)])
    r_tot = r1 + rp
    current_a = r.choice([1.0, 1.5, 2.0])
    v_batt = round(current_a * r_tot, 1)

    v1 = round(current_a * r1, 1)
    vp = round(current_a * rp, 1)
    i2 = round(vp / r2, 2)
    i3 = round(vp / r3, 2)

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 210" width="100%" style="max-width:460px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="230" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Series-Parallel Circuit with Multimeters</text>'
        f'<line x1="60" y1="50" x2="400" y2="50" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(210, 50)"><line x1="0" y1="0" x2="20" y2="0"/><line x1="20" y1="-10" x2="20" y2="10" stroke-width="2.5"/><line x1="28" y1="-6" x2="28" y2="6" stroke-width="4"/><line x1="28" y1="0" x2="50" y2="0"/><text x="25" y="-15" text-anchor="middle" font-size="10" fill="#b91c1c">{_fmt(v_batt)} V</text></g>'
        f'<g transform="translate(60, 95)"><circle cx="0" cy="0" r="12" fill="#ffffff" stroke="#2563eb" stroke-width="2"/><text x="0" y="4" text-anchor="middle" font-size="10" font-weight="bold" fill="#1d4ed8">A1</text></g>'
        f'<line x1="60" y1="50" x2="60" y2="140" stroke="#334155" stroke-width="2"/>'
        f'<line x1="400" y1="50" x2="400" y2="140" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(120, 140)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R1 ({r1} Ω)</text></g>'
        f'<line x1="60" y1="140" x2="100" y2="140" stroke="#334155" stroke-width="2"/>'
        f'<line x1="140" y1="140" x2="200" y2="140" stroke="#334155" stroke-width="2"/>'
        f'<line x1="200" y1="110" x2="200" y2="170" stroke="#334155" stroke-width="2"/>'
        f'<line x1="200" y1="110" x2="340" y2="110" stroke="#334155" stroke-width="2"/>'
        f'<line x1="200" y1="170" x2="340" y2="170" stroke="#334155" stroke-width="2"/>'
        f'<g transform="translate(250, 110)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R2 ({r2} Ω)</text></g>'
        f'<g transform="translate(250, 170)"><rect x="-20" y="-8" width="40" height="16" fill="#f8fafc" stroke="#334155"/><text x="0" y="4" text-anchor="middle" font-size="9">R3 ({r3} Ω)</text></g>'
        f'<g transform="translate(310, 110)"><circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#2563eb" stroke-width="2"/><text x="0" y="3" text-anchor="middle" font-size="8" font-weight="bold" fill="#1d4ed8">A2</text></g>'
        f'<line x1="340" y1="110" x2="340" y2="170" stroke="#334155" stroke-width="2"/>'
        f'<line x1="340" y1="140" x2="400" y2="140" stroke="#334155" stroke-width="2"/>'
        f'</svg>'
    )
    prompt = (
        f"In the circuit diagram illustrated, a battery of potential difference **${_fmt(v_batt)}\\text{{ V}}$** is connected to "
        f"resistor **$R_1 = {r1}\\ \\Omega$** in series with a parallel pair **$R_2 = {r2}\\ \\Omega$** and **$R_3 = {r3}\\ \\Omega$**.\n\n"
        f"1. Calculate the total equivalent resistance ($R_{{\\text{{total}}}}$) of the circuit.\n"
        f"2. Calculate the reading on the main ammeter **A1**.\n"
        f"3. Calculate the potential difference ($V_1$) across resistor $R_1$.\n"
        f"4. Calculate the potential difference ($V_p$) across the parallel combination.\n"
        f"5. Calculate the reading on branch ammeter **A2** (connected in branch $R_2$)."
    )
    ans = (
        f"1. R_total = {r_tot} \\Omega; 2. A1 = {_fmt(current_a)} A; 3. V1 = {_fmt(v1)} V; "
        f"4. Vp = {_fmt(vp)} V; 5. A2 = {_fmt(i2)} A."
    )
    sol = (
        f"1. $R_p = \\frac{{{r2} \\times {r3}}}{{{r2} + {r3}}} = {rp}\\ \\Omega$ [1M].\n"
        f"   $R_{{\\text{{total}}}} = R_1 + R_p = {r1} + {rp} = {r_tot}\\ \\Omega$ [1M].\n"
        f"2. Main current: $I = \\frac{{V_{{\\text{{total}}}}}}{{R_{{\\text{{total}}}}}} = \\frac{{{_fmt(v_batt)}}}{{{r_tot}}} = {_fmt(current_a)}\\text{{ A}}$ [1A].\n"
        f"3. Potential difference across $R_1$: $V_1 = I \\times R_1 = {_fmt(current_a)} \\times {r1} = {_fmt(v1)}\\text{{ V}}$ [1A].\n"
        f"4. Potential difference across parallel pair: $V_p = V_{{\\text{{total}}}} - V_1 = {_fmt(v_batt)} - {_fmt(v1)} = {_fmt(vp)}\\text{{ V}}$ "
        f"(or $V_p = I \\times R_p = {_fmt(current_a)} \\times {rp} = {_fmt(vp)}\\text{{ V}}$) [1M].\n"
        f"5. Current through $R_2$: $I_2 = \\frac{{V_p}}{{R_2}} = \\frac{{{_fmt(vp)}}}{{{r2}}} = {_fmt(i2)}\\text{{ A}}$ [1A]."
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    return _make_q(
        r, "44_series_parallel_multimeter_readings_calculation", 44, prompt, ans, sol, 6,
        ["used_battery_voltage_on_parallel_branch_error", "current_divider_arithmetic_error"],
        [
            {"id": "mp1", "desc": f"Total resistance R_tot = {r_tot} Ohm", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Main current A1 = {_fmt(current_a)} A", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Voltage drop V1 = {_fmt(v1)} V", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Parallel voltage drop Vp = {_fmt(vp)} V", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Branch current A2 = {_fmt(i2)} A", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$R_{\\text{tot}} = R_1 + R_p$. Then $I_{\\text{main}} = V / R_{\\text{tot}}$. $V_p = V_{\\text{batt}} - V_1$.",
            "tier_2": f"R_tot = {r_tot} Ohm. A1 = {_fmt(current_a)} A. V1 = {_fmt(v1)} V. Vp = {_fmt(vp)} V.",
            "tier_3": f"A2 = {_fmt(vp)} / {r2} = {_fmt(i2)} A.",
        },
        diagram_spec=diag, weight=18, duration=6,
    )


# =========================================================================== #
# 45. Switch Dynamics: Effect of Closing Switch in Parallel Branch
# =========================================================================== #
def _build_45_switch_open_vs_closed_effect_on_parallel_branch(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r1 = r.choice([2, 4])
    r2 = 6
    r3 = 6
    rp_closed = 3
    r_open = r1 + r2
    r_closed = r1 + rp_closed

    prompt = (
        f"A circuit contains a series resistor $R_1 = {r1}\\ \\Omega$ connected to a parallel network of two identical "
        f"resistors $R_2 = {r2}\\ \\Omega$ and $R_3 = {r3}\\ \\Omega$. A switch **S** is placed in series with resistor $R_3$ only.\n\n"
        f"When switch S is **open**, $R_3$ is disconnected.\n"
        f"When switch S is **closed**, $R_3$ is connected in parallel with $R_2$.\n\n"
        f"Predict and explain the effect of **closing switch S** on:\n"
        f"1. The total equivalent resistance of the circuit (increases / decreases / remains constant).\n"
        f"2. The total current supplied by the battery.\n"
        f"3. The brightness of a lamp acting as resistor $R_1$.\n"
        f"4. The reading on a voltmeter connected across resistor $R_2$."
    )
    ans = (
        f"1. Decreases (from {r_open} \\Omega to {r_closed} \\Omega); "
        f"2. Increases (I = V / R_total); "
        f"3. Increases (burns brighter because higher current passes through R1, P = I^2 R); "
        f"4. Decreases (higher current increases V1 = I * R1, leaving less remaining voltage for the parallel combination, Vp = V_batt - V1)."
    )
    sol = (
        f"1. **Total resistance decreases:** Adding $R_3$ in parallel provides an additional pathway, decreasing parallel resistance from ${r2}\\ \\Omega$ to $R_p = {rp_closed}\\ \\Omega$. "
        f"Total resistance decreases from ${r_open}\\ \\Omega$ to ${r_closed}\\ \\Omega$ [1M].\n"
        f"2. **Total current increases:** With battery EMF constant, $I_{{\\text{{total}}}} = \\frac{{V}}{{R_{{\\text{{total}}}}}}$. A smaller $R_{{\\text{{total}}}}$ causes total current to increase [1M].\n"
        f"3. **Brightness of $R_1$ increases:** Because all total current passes through series resistor $R_1$, the power dissipated in $R_1$ ($P_1 = I^2 R_1$) increases, so it shines brighter [1M].\n"
        f"4. **Voltage across $R_2$ decreases:** Increased current through $R_1$ causes a larger voltage drop across $R_1$ ($V_1 = I R_1$). By potential division ($V_p = V_{{\\text{{battery}}}} - V_1$), the voltage remaining across the parallel combination **decreases** [1A]."
    )
    return _make_q(
        r, "45_switch_open_vs_closed_effect_on_parallel_branch", 45, prompt, ans, sol, 4,
        ["closing_switch_increases_resistance_fallacy", "parallel_voltage_unaffected_by_series_load_error"],
        [
            {"id": "mp1", "desc": "Total resistance decreases deduction", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Total current increases deduction", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Brightness of R1 increases explanation", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Voltage across parallel pair decreases reasoning", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Adding a parallel branch decreases total resistance, which increases total current from battery.",
            "tier_2": "Higher current increases $V_1 = I R_1$, so $V_p = V_{\\text{batt}} - V_1$ decreases.",
            "tier_3": "1. Decreases. 2. Increases. 3. Brighter. 4. Decreases.",
        },
        weight=15, duration=5,
    )


# =========================================================================== #
# 46. Short Circuit: Concept, Mechanism & Hazards
# =========================================================================== #
def _build_46_short_circuit_concept_and_consequences(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    v_batt = r.choice([6.0, 12.0, 24.0])
    prompt = (
        f"A circuit consists of a battery (${_fmt(v_batt)}\\text{{ V}}$) powering two identical light bulbs, $L_1$ and $L_2$, in series. "
        f"A low-resistance copper connecting lead is accidentally placed directly across the terminals of lamp $L_2$, "
        f"creating a **short circuit** across $L_2$.\n\n"
        f"1. Define the term **short circuit**.\n"
        f"2. Explain what happens to the state of lamp $L_2$ (glows brighter, dimmer, or goes out completely).\n"
        f"3. Explain what happens to the brightness of lamp $L_1$.\n"
        f"4. State two significant physical hazards caused by short circuits in domestic and industrial electrical installations."
    )
    ans = (
        f"1. An unintended low-resistance connection between two points in an electric circuit that bypasses the normal load; "
        f"2. Lamp L2 goes out completely because virtually all current bypasses it through the zero-resistance copper wire; "
        f"3. Lamp L1 shines significantly brighter (and may burn out) because total circuit resistance halved, doubling the current through L1; "
        f"4. Electrical fire hazard due to severe overheating (P = I^2 R in leads) and battery damage or thermal explosion."
    )
    sol = (
        f"1. **Short circuit:** An electric circuit of very low resistance made accidentally or intentionally, bypassing the regular load and drawing excessive current [1M].\n"
        f"2. **Lamp $L_2$ goes out completely:** Current follows the path of least resistance. The bypass wire has nearly zero resistance ($R \\approx 0$), diverting all current away from $L_2$ ($I_{{L2}} \\approx 0$) [1M].\n"
        f"3. **Lamp $L_1$ shines brighter:** Removing $L_2$ from the resistive path halves the total resistance ($R_{{\\text{{new}}}} = R_{{L1}}$). Total current doubles ($I = \\frac{{V}}{{R_{{L1}}}}$), so power in $L_1$ quadruples ($P = I^2 R_{{L1}}$) [1M].\n"
        f"4. **Hazards [1A]:**\n"
        f"   - **Electrical fire:** Rapid Joule heating ($I^2 R$) can melt wire insulation and ignite nearby combustible materials.\n"
        f"   - **Equipment / battery damage:** Risk of battery leakage, rupture, or explosion from intense discharge."
    )
    return _make_q(
        r, "46_short_circuit_concept_and_consequences", 46, prompt, ans, sol, 4,
        ["both_bulbs_turn_off_fallacy", "misunderstands_current_bypass_mechanism"],
        [
            {"id": "mp1", "desc": "Definition of short circuit", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "L2 turns off completely explanation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "L1 shines brighter explanation (halved resistance)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Two hazards: fire risk and battery explosion/damage", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Current takes the path of zero resistance. L2 is completely bypassed.",
            "tier_2": "Because L2 is bypassed, total circuit resistance drops, so current through L1 surges.",
            "tier_3": "1. Low resistance bypass. 2. L2 goes out. 3. L1 shines brighter. 4. Fire and battery explosion.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 47. Meter Connections: Swapping Ammeter & Voltmeter Effects
# =========================================================================== #
def _build_47_ammeter_incorrectly_in_parallel_or_voltmeter_in_series(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    scenario = r.choice(["ammeter_in_parallel", "voltmeter_in_series"])
    is_ammeter_par = (scenario == "ammeter_in_parallel")

    prompt = (
        f"In a practical laboratory test, a student mistakenly swaps the positions of the meters:\n\n"
        f"**Scenario:** A student connects {'an ammeter in parallel across a resistor connected to a battery' if is_ammeter_par else 'a voltmeter in series with a resistor and battery in a single closed loop'}.\n\n"
        f"1. State the correct standard connection rule for this meter.\n"
        f"2. Explain what will happen to the circuit and the meter in this incorrect configuration.\n"
        f"3. Relate your explanation to the internal resistance characteristic of the meter."
    )
    ans = (
        f"1. {'Ammeters must be connected in series' if is_ammeter_par else 'Voltmeters must be connected in parallel'}; "
        f"2. {'The ammeter short-circuits the resistor: a massive current surges through the ammeter, potentially blowing its fuse or burning out the meter' if is_ammeter_par else 'The voltmeter blocks current: the circuit current drops to near zero and the load turns off; the voltmeter reads the full battery EMF'}; "
        f"3. {'An ammeter has near zero internal resistance ($R_A \\approx 0$), presenting a short circuit path' if is_ammeter_par else 'A voltmeter has near infinite internal resistance ($R_V \\approx \\infty$), effectively acting as an open break in the series circuit'}."
    )
    sol = (
        f"1. Connection rule: **{'Ammeters must always be connected in series' if is_ammeter_par else 'Voltmeters must always be connected in parallel'}** [1M].\n"
        f"2. Physical consequence: **{'A short circuit occurs across the resistor. A dangerous current surge flows through the ammeter, likely blowing the internal fuse or destroying the meter coil' if is_ammeter_par else 'The high resistance of the voltmeter virtually halts all charge flow. Circuit current drops to zero ($I \\approx 0\\text{{ A}}$), so the resistor receives no current, while the voltmeter reads the entire battery EMF'}** [1M].\n"
        f"3. Resistance explanation: {'An ammeter has extremely low internal resistance ($R_a \\approx 0\\ \\Omega$). When placed in parallel, it bypasses the load entirely.' if is_ammeter_par else 'A voltmeter has extremely high internal resistance ($R_v \\approx 10^6\\ \\Omega$). When placed in series, its enormous resistance dominates the loop, reducing current to microamperes.'} [2M]."
    )
    return _make_q(
        r, "47_ammeter_and_voltmeter_incorrect_connection_effects", 47, prompt, ans, sol, 4,
        ["confuses_voltmeter_and_ammeter_internal_resistance", "meter_damage_mechanics_misconception"],
        [
            {"id": "mp1", "desc": "Correct connection rule stated", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Physical consequence described accurately", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Internal resistance property justification", "marks": 2, "editable": True},
        ],
        {
            "tier_1": "Ammeters have near 0 Ohm resistance. Voltmeters have near infinite resistance.",
            "tier_2": "Ammeter in parallel = short circuit / blown fuse. Voltmeter in series = blocks current.",
            "tier_3": ans,
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 48. Electrical Energy: Transfer Formula E = V * I * Delta t
# =========================================================================== #
def _build_48_electrical_energy_transfer_E_V_I_t(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    v_val = r.choice([12.0, 24.0, 230.0])
    i_val = r.choice([0.5, 1.5, 2.0, 4.0, 5.0])
    time_min = r.choice([2, 5, 10, 15, 30])
    time_s = time_min * 60
    energy_j = round(v_val * i_val * time_s, 1)
    energy_kj = round(energy_j / 1000.0, 2)

    prompt = (
        f"An electrical appliance operates at a potential difference of **${_fmt(v_val)}\\text{{ V}}$**, drawing a "
        f"current of **${_fmt(i_val)}\\text{{ A}}$** for **{time_min} minutes**.\n\n"
        f"1. Convert the operating time into seconds.\n"
        f"2. State the formula for electrical energy ($E$) in terms of potential difference, current, and time.\n"
        f"3. Calculate the total electrical energy transferred in Joules (J).\n"
        f"4. Express this energy in kilojoules (kJ)."
    )
    ans = (
        f"1. Delta t = {time_s} s; 2. E = V * I * Delta t; 3. E = {_fmt(energy_j)} J; 4. E = {_fmt(energy_kj)} kJ."
    )
    sol = (
        f"1. Time conversion: $\\Delta t = {time_min} \\times 60 = {time_s}\\text{{ s}}$ [1M].\n"
        f"2. $E = V \\times I \\times \\Delta t$ [1M].\n"
        f"3. $E = ({_fmt(v_val)}\\text{{ V}}) \\times ({_fmt(i_val)}\\text{{ A}}) \\times ({time_s}\\text{{ s}}) = {_fmt(energy_j)}\\text{{ J}}$ [1A].\n"
        f"4. Energy in kilojoules: $E = \\frac{{{_fmt(energy_j)}}}{{1000}} = {_fmt(energy_kj)}\\text{{ kJ}}$ [1A]."
    )
    return _make_q(
        r, "48_electrical_energy_transfer_E_V_I_t", 48, prompt, ans, sol, 4,
        ["forgot_time_conversion_to_seconds", "kilojoule_prefix_error"],
        [
            {"id": "mp1", "desc": f"Time conversion to seconds = {time_s} s", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Formula E = V * I * Delta t", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Energy calculation in Joules = {_fmt(energy_j)} J", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Energy in kilojoules = {_fmt(energy_kj)} kJ", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$E = V I \\Delta t$. Time must always be converted to seconds!",
            "tier_2": f"Time = {time_s} s. Multiply {_fmt(v_val)} * {_fmt(i_val)} * {time_s}.",
            "tier_3": f"E = {_fmt(energy_j)} J = {_fmt(energy_kj)} kJ.",
        },
        weight=12, duration=4,
    )


# =========================================================================== #
# 49. Power & Energy Cost: P = V * I, kWh and Domestic Electricity Tariffs
# =========================================================================== #
def _build_49_electrical_power_and_cost_of_electricity(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    power_w = r.choice([1000, 1500, 2000, 2500, 3000])
    hours = r.choice([2.0, 3.0, 4.0, 5.0])
    days = r.choice([30, 31])
    tariff_rand = r.choice([2.20, 2.50, 2.85, 3.10])  # Rand per kWh
    power_kw = power_w / 1000.0
    total_hours = hours * days
    energy_kwh = round(power_kw * total_hours, 2)
    total_cost = round(energy_kwh * tariff_rand, 2)

    prompt = (
        f"A domestic electric geyser rated at **{power_w}\\text{{ W}}** (${_fmt(power_kw)}\\text{{ kW}}$) operates for "
        f"**{_fmt_plain(hours)} hours per day** over a billing period of **{days} days**.\n"
        f"Electricity is charged at a municipal tariff rate of **R{_fmt_plain(tariff_rand)} per kilowatt-hour (kWh)**.\n\n"
        f"1. Define the term **electrical power**.\n"
        f"2. Convert the power rating of the geyser from watts (W) to kilowatts (kW).\n"
        f"3. Calculate the total electrical energy consumed by the geyser in kilowatt-hours (kWh) over the {days} days.\n"
        f"4. Calculate the total cost in Rands (R) of operating the geyser for this billing cycle."
    )
    ans = (
        f"1. The rate at which electrical work is done (or rate at which electrical energy is transferred); "
        f"2. P = {_fmt(power_kw)} kW; 3. Energy = {_fmt(energy_kwh)} kWh; 4. Cost = R{_fmt(total_cost)}."
    )
    sol = (
        f"1. **Electrical power:** The rate at which electrical energy is converted into other forms of energy ($P = \\frac{{E}}{{\\Delta t}} = V I$) [1M].\n"
        f"2. $P = \\frac{{{power_w}\\text{{ W}}}}{{1000}} = {_fmt(power_kw)}\\text{{ kW}}$ [1M].\n"
        f"3. Total hours: $t = {_fmt_plain(hours)}\\text{{ h/day}} \\times {days}\\text{{ days}} = {int(total_hours)}\\text{{ hours}}$\n"
        f"   $\\text{{Energy (kWh)}} = P(\\text{{kW}}) \\times t(\\text{{hours}}) = {_fmt(power_kw)} \\times {int(total_hours)} = {_fmt(energy_kwh)}\\text{{ kWh}}$ [1A].\n"
        f"4. $\\text{{Cost}} = \\text{{Energy (kWh)}} \\times \\text{{Tariff}} = {_fmt(energy_kwh)} \\times R{_fmt(tariff_rand)} = \\mathbf{{R{_fmt(total_cost)}}}$ [1A]."
    )
    return _make_q(
        r, "49_electrical_power_and_cost_of_electricity", 49, prompt, ans, sol, 4,
        ["confuses_power_and_energy", "failed_to_convert_watts_to_kilowatts"],
        [
            {"id": "mp1", "desc": "Definition of electrical power", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Power in kW = {_fmt(power_kw)} kW", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Energy in kWh = {_fmt(energy_kwh)} kWh", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Cost calculation = R{_fmt(total_cost)}", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "$\\text{Energy in kWh} = \\frac{\\text{Power (W)}}{1000} \\times \\text{Time (hours)}$. $\\text{Cost} = \\text{kWh} \\times \\text{Tariff}$.",
            "tier_2": f"Power in kW = {_fmt(power_kw)} kW. Total hours = {int(total_hours)} h. Energy = {_fmt(energy_kwh)} kWh.",
            "tier_3": f"Energy = {_fmt(energy_kwh)} kWh; Cost = R{_fmt(total_cost)}.",
        },
        weight=15, duration=5,
    )


# =========================================================================== #
# 50. Comprehensive Capstone: Diagnostic Autopsy & Misconception Repair
# =========================================================================== #
def _build_50_electric_circuits_and_magnetism_diagnostic_autopsy(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    scenarios = [
        {
            "title": "Current Consumed by Circuit Components",
            "claim": "A learner states that in a series circuit containing two identical bulbs, the first bulb is brighter than the second bulb because the first bulb uses up most of the current before it reaches the second bulb.",
            "misconception": "Believes electric current is an energy source that gets 'consumed' or depleted as it travels through circuit components (attenuation model).",
            "correction": "Electric current is the rate of flow of electric charge (I = Q/Delta t). In a series circuit, charge is strictly conserved and there is only one pathway: every electron entering the first bulb must pass through the second bulb. Both bulbs experience the exact same current and glow with equal brightness. Resistors consume potential energy (voltage), not current."
        },
        {
            "title": "Voltage 'Flows' Through Wires",
            "claim": "A learner writes in a test: 'A voltage of 12 V flows through the circuit wires into the resistor.'",
            "misconception": "Confuses current with potential difference, viewing voltage as a substance or fluid that flows along wires.",
            "correction": "Voltage (potential difference) does not flow; it is the work done per unit charge (energy difference) BETWEEN two points in a circuit. What flows is electric current (charge). Voltage is the electrical pressure or 'push' provided by the battery that drives the current."
        },
        {
            "title": "Ammeter Connected Across Battery",
            "claim": "A learner connects an ammeter in parallel across a 12 V battery to measure how much current the battery can produce.",
            "misconception": "Believes an ammeter measures the 'capacity' of a battery and can be connected directly across its terminals like a voltmeter.",
            "correction": "An ideal ammeter has near zero internal resistance. Connecting it in parallel across a voltage source causes a catastrophic short circuit: a huge surge of current flows through the meter, blowing its fuse, burning its internal coil, or destroying the battery. Ammeters must always be connected in series with a load."
        },
        {
            "title": "Cutting a Magnet Produces Isolated Monopoles",
            "claim": "A learner asserts that if a bar magnet is cut in half, one half will be a pure North pole and the other half will be a pure South pole.",
            "misconception": "Believes magnetic poles can exist as isolated monopoles, similar to isolated positive and negative electrostatic charges.",
            "correction": "Magnetic monopoles do not exist in nature. Magnetism arises from microscopic aligned domains containing electron spins. Cutting a magnet creates two separate magnets, each with its own North and South poles."
        }
    ]
    chosen = r.choice(scenarios)

    prompt = (
        f"**Diagnostic Autopsy:** Review the following common learner claim regarding electric circuits and magnetism:\n\n"
        f"**Student Claim ({chosen['title']}):**\n"
        f"\"{chosen['claim']}\"\n\n"
        f"1. Identify and name the fundamental physics misconception demonstrated by the student.\n"
        f"2. Provide a rigorous, scientifically accurate explanation refuting the student's statement.\n"
        f"3. State the correct underlying physical law or principle (e.g. Conservation of Charge, Definition of Potential Difference, Non-existence of Monopoles) that resolves this error."
    )
    ans = (
        f"1. Misconception: {chosen['misconception']}; "
        f"2. Scientific refutation: {chosen['correction']}; "
        f"3. Governed by fundamental conservation principles and definitions in physics."
    )
    sol = (
        f"1. **Identified Misconception:** {chosen['misconception']} [1M].\n"
        f"2. **Scientific Refutation & Correction:** {chosen['correction']} [2M].\n"
        f"3. **Underlying Principle:** Governed by fundamental physical laws: conservation of charge ($I_{{\\text{{in}}}} = I_{{\\text{{out}}}}$), definition of potential difference ($V = \\frac{{W}}{{Q}}$ as energy per unit charge, not a flowing substance), and domain theory of magnetism ($B = \\nabla \\times A$, no isolated monopoles) [1A]."
    )
    return _make_q(
        r, "50_comprehensive_grade10_electric_circuits_synthesis", 50, prompt, ans, sol, 4,
        ["conceptual_diagnostic_autopsy_misconception", "circuit_misconception_repair_error"],
        [
            {"id": "mp1", "desc": "Identification of fundamental misconception", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Scientific refutation and explanation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Underlying physical law / principle cited", "marks": 1, "editable": True},
        ],
        {
            "tier_1": "Carefully identify what the learner confused (e.g. current vs voltage, charge conservation, or magnetic monopoles).",
            "tier_2": "State the correct scientific definition and demonstrate how it corrects the error.",
            "tier_3": chosen["correction"],
        },
        weight=15, duration=5,
    )


# =========================================================================== #
# Export Dictionary for Subskills 26 to 50
# =========================================================================== #
BUILDERS_26_50: Dict[str, Any] = {
    "26_resistance_definition_ratio_V_I": _build_26_resistance_definition_ratio_V_I,
    "27_factors_affecting_conductor_resistance": _build_27_factors_affecting_conductor_resistance,
    "28_ohmic_vs_non_ohmic_conductors": _build_28_ohmic_vs_non_ohmic_conductors,
    "29_ohmic_resistor_gradient_calculation": _build_29_ohmic_resistor_gradient_calculation,
    "30_calculating_unknown_resistor_from_V_and_I": _build_30_calculating_unknown_resistor_from_V_and_I,
    "31_series_equivalent_resistance_two_resistors": _build_31_series_equivalent_resistance_two_resistors,
    "32_series_equivalent_resistance_three_resistors": _build_32_series_equivalent_resistance_three_resistors,
    "33_series_circuit_current_conservation": _build_33_series_circuit_current_conservation,
    "34_series_circuit_potential_division": _build_34_series_circuit_potential_division,
    "35_series_voltage_divider_ratio": _build_35_series_voltage_divider_ratio,
    "36_series_circuit_fault_finding_open_bulb_or_switch": _build_36_series_circuit_fault_finding_open_switch_or_bulb,
    "37_parallel_equivalent_resistance_two_identical": _build_37_parallel_equivalent_resistance_two_identical,
    "38_parallel_equivalent_resistance_two_different": _build_38_parallel_equivalent_resistance_two_different,
    "39_parallel_equivalent_resistance_three_resistors": _build_39_parallel_equivalent_resistance_three_resistors,
    "40_parallel_circuit_potential_equality": _build_40_parallel_circuit_potential_equality,
    "41_parallel_circuit_current_branching": _build_41_parallel_circuit_current_branching,
    "42_parallel_current_divider_calculation": _build_42_parallel_current_divider_calculation,
    "43_series_parallel_network_resistor_in_series_with_parallel_pair": _build_43_series_parallel_network,
    "44_series_parallel_multimeter_readings_calculation": _build_44_series_parallel_multimeter_readings_calculation,
    "45_switch_open_vs_closed_effect_on_parallel_branch": _build_45_switch_open_vs_closed_effect_on_parallel_branch,
    "46_short_circuit_concept_and_consequences": _build_46_short_circuit_concept_and_consequences,
    "47_ammeter_and_voltmeter_incorrect_connection_effects": _build_47_ammeter_incorrectly_in_parallel_or_voltmeter_in_series,
    "48_electrical_energy_transfer_E_V_I_t": _build_48_electrical_energy_transfer_E_V_I_t,
    "49_electrical_power_and_cost_of_electricity": _build_49_electrical_power_and_cost_of_electricity,
    "50_comprehensive_grade10_electric_circuits_synthesis": _build_50_electric_circuits_and_magnetism_diagnostic_autopsy,
}
