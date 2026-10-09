"""Grade 12 Physical Sciences — Electrodynamics & Electric Circuits Generator.
Deterministic 6-pillar CAPS question generator covering Paper 1 (Physics Term 3):
- Electrical machines: AC and DC generators (alternators) vs electric motors.
- Slip rings vs split-ring commutators, Fleming's rules, energy conversions.
- Alternating current (AC) theory: Peak vs rms values (I_rms = I_max / sqrt(2), V_rms = V_max / sqrt(2)).
- Average power dissipation: P_ave = V_rms * I_rms = I_rms^2 * R = V_rms^2 / R.
- Internal resistance of batteries: emf = V_load + V_internal = I(R_ext + r), lost volts.

Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _build_ac_rms_drill(r: random.Random) -> Dict[str, Any]:
    v_rms = r.choice([220, 230, 240, 110, 120])
    p_ave = r.choice([1000, 1200, 1500, 1800, 2000, 2200, 2500])

    v_max = round(v_rms * math.sqrt(2), 1)
    i_rms = round(p_ave / v_rms, 2)
    i_max = round(i_rms * math.sqrt(2), 2)
    r_val = round((v_rms**2) / p_ave, 2)

    prompt = (
        f"An electric kettle is marked with the power rating **${p_ave}\\text{{ W}}, {v_rms}\\text{{ V}}$**.\n"
        f"It is connected to a standard alternating current (AC) domestic wall socket.\n\n"
        f"1. Calculate the peak (maximum) voltage ($V_{{max}}$) supplied to the kettle.\n"
        f"2. Calculate the rms current ($I_{{rms}}$) flowing through the heating element.\n"
        f"3. Calculate the resistance ($R$) of the heating element.\n"
        f"4. Calculate the maximum (peak) current ($I_{{max}}$)."
    )

    sol = (
        f"1. $V_{{rms}} = \\frac{{V_{{max}}}}{{\\sqrt{{2}}}}$\n"
        f"   $V_{{max}} = V_{{rms}} \\times \\sqrt{{2}} = {v_rms} \\times \\sqrt{{2}} = {_fmt_sa(v_max)}\\text{{ V}}$\n\n"
        f"2. $P_{{ave}} = V_{{rms}} I_{{rms}}$\n"
        f"   $I_{{rms}} = \\frac{{{p_ave}}}{{{v_rms}}} = {_fmt_sa(i_rms)}\\text{{ A}}$\n\n"
        f"3. $R = \\frac{{V_{{rms}}^2}}{{P_{{ave}}}} = \\frac{{{v_rms}^2}}{{{p_ave}}} = {_fmt_sa(r_val)}\\ \\Omega$\n\n"
        f"4. $I_{{max}} = I_{{rms}} \\times \\sqrt{{2}} = {_fmt_sa(i_rms)} \\times \\sqrt{{2}} = {_fmt_sa(i_max)}\\text{{ A}}$"
    )

    return {
        "id": f"g12_ps_ac_rms_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Vmax={_fmt_sa(v_max)} V, Irms={_fmt_sa(i_rms)} A, R={_fmt_sa(r_val)} Ohm",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Formula: Vrms = Vmax / sqrt(2)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculate Vmax = {_fmt_sa(v_max)} V", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Formula: Pave = Vrms * Irms", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculate Irms = {_fmt_sa(i_rms)} A", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculate R = {_fmt_sa(r_val)} Ohm", "marks": 1, "editable": True},
                {"id": "mp6", "desc": f"Calculate Imax = {_fmt_sa(i_max)} A", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "confused_rms_and_peak_values", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Recall: $V_{rms} = \\frac{V_{max}}{\\sqrt{2}}$ and $P_{ave} = V_{rms} I_{rms}$.",
            "tier_2": "Household rated values are always root-mean-square (rms) values, not peak values.",
            "tier_3": f"$V_{{max}} = {v_rms} \\times \\sqrt{{2}} = {_fmt_sa(v_max)}\\text{{ V}}$. $I_{{rms}} = {p_ave} / {v_rms} = {_fmt_sa(i_rms)}\\text{{ A}}$.",
        },
        "misconception_tags": ["confused_rms_and_peak_values"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def _build_machines_drill(r: random.Random) -> Dict[str, Any]:
    machine_type = r.choice(["AC Generator", "DC Generator", "Electric Motor"])

    if machine_type == "AC Generator":
        principle = "Electromagnetic induction (Faraday's Law)"
        component = "Slip rings"
        energy_conv = "Mechanical energy to electrical energy"
        function_comp = "Allow continuous electrical contact with rotating coil without tangling wires, delivering alternating current to the external circuit."
    elif machine_type == "DC Generator":
        principle = "Electromagnetic induction (Faraday's Law)"
        component = "Split-ring commutator"
        energy_conv = "Mechanical energy to electrical energy"
        function_comp = "Reverses the external circuit connections every half-cycle to ensure direct current flows in one direction only."
    else:
        principle = "The motor effect (force experienced by a current-carrying conductor in a magnetic field)"
        component = "Split-ring commutator"
        energy_conv = "Electrical energy to mechanical energy"
        function_comp = "Reverses current direction in the armature coil every half-cycle so that the torque continues in a constant direction of rotation."

    prompt = (
        f"Consider an electrical machine: **{machine_type}**.\n\n"
        f"1. State the fundamental **operating physical principle** of this machine.\n"
        f"2. State the essential **energy conversion** that takes place.\n"
        f"3. Name the component used to connect the rotating coil to the external circuit (**slip rings** or **split-ring commutator**).\n"
        f"4. State the function of this component in the {machine_type}."
    )

    sol = (
        f"1. Physical principle: **{principle}**\n"
        f"2. Energy conversion: **{energy_conv}**\n"
        f"3. Component: **{component}**\n"
        f"4. Function: {function_comp}"
    )

    return {
        "id": f"g12_ps_mach_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Principle: {principle}, Component: {component}",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"State physical principle: {principle}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"State energy conversion: {energy_conv}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Identify component: {component}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"State component function: {function_comp}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "split_ring_vs_slip_ring_confusion", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Generators convert mechanical to electrical energy via electromagnetic induction. Motors do the opposite via the motor effect.",
            "tier_2": "AC generators use smooth SLIP RINGS. DC generators and DC motors use SPLIT-RING COMMUTATORS.",
            "tier_3": f"{machine_type}: Principle is {principle}, uses {component}.",
        },
        "misconception_tags": ["split_ring_vs_slip_ring_confusion", "motor_effect_vs_electromagnetic_induction"],
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


def _build_internal_resistance_drill(r: random.Random) -> Dict[str, Any]:
    emf = r.choice([9.0, 12.0, 15.0, 18.0, 24.0])
    r_int = round(r.uniform(0.5, 2.5), 2)
    r_ext = round(r.choice([4.0, 5.0, 6.0, 8.0, 10.0]), 2)

    i_current = round(emf / (r_ext + r_int), 2)
    v_load = round(i_current * r_ext, 2)
    v_lost = round(i_current * r_int, 2)

    prompt = (
        f"A battery with an electromotive force (emf) of **${_fmt_sa(emf)}\\text{{ V}}$** and internal resistance **$r$** "
        f"is connected in series with a resistor of resistance **$R = {_fmt_sa(r_ext)}\\ \\Omega$** and an open switch.\n"
        f"When the switch is closed, a current of **${_fmt_sa(i_current)}\\text{{ A}}$** is measured by an ammeter.\n\n"
        f"1. Define the term *electromotive force (emf)*.\n"
        f"2. Calculate the terminal potential difference across the battery ($V_{{load}}$).\n"
        f"3. Calculate the 'lost volts' across the internal resistance of the battery ($V_{{lost}}$).\n"
        f"4. Calculate the internal resistance ($r$) of the battery."
    )

    sol = (
        f"1. **Electromotive force (emf):** The maximum energy provided by a battery per unit charge passing through it.\n"
        f"2. $V_{{load}} = I R_{{ext}} = {_fmt_sa(i_current)} \\times {_fmt_sa(r_ext)} = {_fmt_sa(v_load)}\\text{{ V}}$\n"
        f"3. $V_{{lost}} = \\text{{emf}} - V_{{load}} = {_fmt_sa(emf)} - {_fmt_sa(v_load)} = {_fmt_sa(v_lost)}\\text{{ V}}$\n"
        f"4. $\\text{{emf}} = I(R_{{ext}} + r)$\n"
        f"   ${_fmt_sa(emf)} = {_fmt_sa(i_current)}({_fmt_sa(r_ext)} + r)$\n"
        f"   ${_fmt_sa(r_ext)} + r = \\frac{{{_fmt_sa(emf)}}}{{{_fmt_sa(i_current)}}} = {_fmt_sa(round(emf / i_current, 2))}$\n"
        f"   $r = {_fmt_sa(round(emf / i_current, 2))} - {_fmt_sa(r_ext)} = {_fmt_sa(r_int)}\\ \\Omega$"
    )

    return {
        "id": f"g12_ps_circ_int_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Vload={_fmt_sa(v_load)} V, r={_fmt_sa(r_int)} Ohm",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: Total energy transferred per unit charge", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula: Vload = I * Rext", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate Vload = {_fmt_sa(v_load)} V", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Formula: emf = I(R + r)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculate r = {_fmt_sa(r_int)} Ohm", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "forgot_internal_resistance_drop", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Recall: $\\text{emf} = V_{load} + V_{lost} = I(R + r)$.",
            "tier_2": "Terminal potential difference is $V_{ext} = IR_{ext}$. Lost volts is $V_{lost} = Ir$.",
            "tier_3": f"$V_{{load}} = {_fmt_sa(i_current)} \\times {_fmt_sa(r_ext)} = {_fmt_sa(v_load)}\\text{{ V}}$. $r = ({_fmt_sa(emf)} - {_fmt_sa(v_load)}) / {_fmt_sa(i_current)} = {_fmt_sa(r_int)}\\ \\Omega$.",
        },
        "misconception_tags": ["forgot_internal_resistance_drop"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)

    if mode == "elementary_ac_rms":
        return _build_ac_rms_drill(r)
    elif mode == "elementary_generators_motors":
        return _build_machines_drill(r)
    elif mode == "elementary_internal_resistance":
        return _build_internal_resistance_drill(r)
    else:
        choice = r.choice(["ac_rms", "machines", "internal_res"])
        if choice == "ac_rms":
            return _build_ac_rms_drill(r)
        elif choice == "machines":
            return _build_machines_drill(r)
        else:
            return _build_internal_resistance_drill(r)
