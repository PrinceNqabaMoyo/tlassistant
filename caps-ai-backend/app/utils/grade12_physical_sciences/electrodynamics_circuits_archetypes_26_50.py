"""Grade 12 Physical Sciences — Electrodynamics & Electric Circuits (Archetypes 26–50).
Deterministic 6-pillar question generators covering Paper 1 (Physics Term 3):
- Subskills 26–30: AC power dissipation (P_ave = Vrms * Irms = Irms^2 * R = Vrms^2 / R), peak vs average power, domestic energy cost.
- Subskills 31–36: Internal resistance and emf: definition, lost volts, terminal pd, calculating r and emf from simultaneous states, short-circuit current.
- Subskills 37–38: Graphical analysis of V vs I: intercept = emf, gradient = -r, experimental determination.
- Subskills 39–45: Resistor networks with internal resistance: series, parallel, combined series-parallel, voltmeter/ammeter readings across switches, power dissipation.
- Subskills 46–48: Circuit dynamics: switch closing/opening effects, bulb brightness changes, battery aging/flat battery syndrome.
- Subskills 49–50: Capstone synthesis: AC generation to transmission lines to internal resistance, diagnostic autopsy and misconception repair.

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
    q_id = f"g12_ps_circuits_{num:02d}_{r.randint(10000, 99999)}"
    q: Dict[str, Any] = {
        "id": q_id,
        "type": "compound",
        "modality": "electric_circuits",
        "subskill": subskill,
        "archetype_id": num,
        "prompt": prompt,
        "correct_answer": correct_ans,
        "worked_solution": worked_sol,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp{i+1}", "desc": item["criterion"], "marks": item.get("marks", 1), "editable": True}
                for i, item in enumerate(rubric)
            ],
            "deductions": [{"rule": "incorrect_units_or_rounding", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "misconception_tags": misconceptions,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
    return q


# ============================================================================ #
# SUBSKILLS 26–30: AC POWER DISSIPATION & DOMESTIC ELECTRICITY
# ============================================================================ #

def build_26_ac_average_power_from_vrms_and_irms(r: random.Random) -> Dict[str, Any]:
    v_rms = r.choice([220, 230, 240])
    i_rms = round(r.uniform(3.5, 9.5), 1)
    p_ave = round(v_rms * i_rms, 1)

    prompt = (
        f"A commercial alternating current (AC) fan motor is connected to a standard domestic wall outlet with a root-mean-square voltage of "
        f"${v_rms}\\text{{ V}}$. The rms current drawn by the motor during steady operation is ${i_rms}\\text{{ A}}$.\n\n"
        f"1. State the formula relating average electrical power ($P_{{\\text{{ave}}}}$) to $V_{{\\text{{rms}}}}$ and $I_{{\\text{{rms}}}}$.\n"
        f"2. Calculate the average power dissipated by the motor."
    )
    ans = f"P_ave = {_fmt_tex(p_ave)} W"
    sol = (
        f"1. $P_{{\\text{{ave}}}} = V_{{\\text{{rms}}}} I_{{\\text{{rms}}}}$\n"
        f"2. $P_{{\\text{{ave}}}} = ({v_rms})({_fmt_tex(i_rms)}) = {_fmt_tex(p_ave)}\\text{{ W}}$."
    )
    rubric = [
        {"criterion": "Formula: P_ave = V_rms * I_rms", "marks": 1},
        {"criterion": f"Substitution: ({v_rms})({_fmt_tex(i_rms)})", "marks": 1},
        {"criterion": f"Calculated average power: {_fmt_tex(p_ave)} W with unit", "marks": 1},
    ]
    hints = {
        "tier_1": "Recall: P_ave = V_rms * I_rms.",
        "tier_2": f"Substitute V_rms = {v_rms} V and I_rms = {_fmt(i_rms)} A.",
        "tier_3": ans,
    }
    return _make_q(r, "26_ac_average_power_from_vrms_and_irms", 26, prompt, ans, sol, 3, ["used_peak_instead_of_rms_current"], rubric, hints)


def build_27_ac_power_dissipation_in_heating_resistor(r: random.Random) -> Dict[str, Any]:
    r_val = r.choice([15, 20, 25, 30, 40, 50])
    i_rms = round(r.uniform(4.0, 8.0), 1)
    p_ave = round((i_rms ** 2) * r_val, 1)

    prompt = (
        f"An electric heating element inside an electric toaster has a resistance of ${r_val}\\ \\Omega$. When connected to an AC power supply, "
        f"an alternating current with an rms value of ${i_rms}\\text{{ A}}$ passes through the heating element.\n\n"
        f"1. Calculate the average electrical power dissipated as heat in the resistor.\n"
        f"2. Calculate the peak (maximum) instantaneous power dissipated by this heating element."
    )
    p_max = round(2 * p_ave, 1)
    ans = f"P_ave = {_fmt_tex(p_ave)} W; P_max = {_fmt_tex(p_max)} W"
    sol = (
        f"1. $P_{{\\text{{ave}}}} = I_{{\\text{{rms}}}}^2 R = ({_fmt_tex(i_rms)})^2 ({r_val}) = {_fmt_tex(p_ave)}\\text{{ W}}$.\n"
        f"2. For a sinusoidal alternating current, peak power is twice the average power:\n"
        f"   $P_{{\\text{{max}}}} = 2 P_{{\\text{{ave}}}} = 2 \\times {_fmt_tex(p_ave)} = {_fmt_tex(p_max)}\\text{{ W}}$\n"
        f"   (or $P_{{\\text{{max}}}} = I_{{\\text{{max}}}}^2 R = (\\sqrt{{2}} I_{{\\text{{rms}}}})^2 R = 2 I_{{\\text{{rms}}}}^2 R$)."
    )
    rubric = [
        {"criterion": "Formula: P_ave = I_rms^2 * R", "marks": 1},
        {"criterion": f"Substitution: ({_fmt_tex(i_rms)})^2 * {r_val}", "marks": 1},
        {"criterion": f"Calculated P_ave = {_fmt_tex(p_ave)} W", "marks": 1},
        {"criterion": f"Calculated peak power P_max = 2 * P_ave = {_fmt_tex(p_max)} W", "marks": 1},
    ]
    hints = {
        "tier_1": "Use P_ave = I_rms^2 * R. Peak power is 2 * P_ave.",
        "tier_2": f"P_ave = ({_fmt(i_rms)})^2 * {r_val} = {_fmt(p_ave)} W.",
        "tier_3": ans,
    }
    return _make_q(r, "27_ac_power_dissipation_in_heating_resistor", 27, prompt, ans, sol, 4, ["confused_peak_and_average_power"], rubric, hints)


def build_28_ac_power_dissipation_from_voltage_and_resistance(r: random.Random) -> Dict[str, Any]:
    v_rms = r.choice([220, 230, 240])
    p_kw = r.choice([1.2, 1.5, 2.0, 2.4, 3.0])
    p_ave = round(p_kw * 1000.0)
    r_val = round((v_rms ** 2) / p_ave, 2)

    prompt = (
        f"An electric geyser heating element is rated to operate on an AC root-mean-square voltage of ${v_rms}\\text{{ V}}$. "
        f"The label indicates that its average power rating is ${p_kw}\\text{{ kW}}$.\n\n"
        f"1. Convert the power rating to watts (W).\n"
        f"2. Calculate the electrical resistance of the geyser heating element under operating conditions.\n"
        f"3. Calculate the rms current drawn by the geyser."
    )
    i_rms = round(p_ave / v_rms, 2)
    ans = f"R = {_fmt_tex(r_val)} Ohm; I_rms = {_fmt_tex(i_rms)} A"
    sol = (
        f"1. $P_{{\\text{{ave}}}} = {_fmt_tex(p_kw)}\\text{{ kW}} = {_fmt_tex(p_ave)}\\text{{ W}}$.\n"
        f"2. $P_{{\\text{{ave}}}} = \\frac{{V_{{\\text{{rms}}}}^2}}{{R}} \\implies R = \\frac{{V_{{\\text{{rms}}}}^2}}{{P_{{\\text{{ave}}}}}} = \\frac{{{v_rms}^2}}{{{_fmt_tex(p_ave)}}} = {_fmt_tex(r_val)}\\ \\Omega$.\n"
        f"3. $I_{{\\text{{rms}}}} = \\frac{{P_{{\\text{{ave}}}}}}{{V_{{\\text{{rms}}}}}} = \\frac{{{_fmt_tex(p_ave)}}}{{{v_rms}}} = {_fmt_tex(i_rms)}\\text{{ A}}$."
    )
    rubric = [
        {"criterion": "Converted kW to W: P_ave = {_fmt_tex(p_ave)} W", "marks": 1},
        {"criterion": "Formula: P_ave = V_rms^2 / R", "marks": 1},
        {"criterion": f"Calculated resistance R = {_fmt_tex(r_val)} Ohm", "marks": 1},
        {"criterion": f"Calculated rms current I_rms = {_fmt_tex(i_rms)} A", "marks": 1},
    ]
    hints = {
        "tier_1": "1 kW = 1000 W. Use P_ave = V_rms^2 / R and P_ave = V_rms * I_rms.",
        "tier_2": f"R = ({v_rms}^2) / {p_ave} = {_fmt(r_val)} Ohm.",
        "tier_3": ans,
    }
    return _make_q(r, "28_ac_power_dissipation_from_voltage_and_resistance", 28, prompt, ans, sol, 4, ["failed_to_convert_kilowatts_to_watts"], rubric, hints)


def build_29_ac_peak_power_versus_average_power(r: random.Random) -> Dict[str, Any]:
    p_ave = r.choice([800, 1000, 1200, 1500, 1800, 2200])
    p_max = 2 * p_ave

    prompt = (
        f"An AC microwave oven operates at an average power of ${p_ave}\\text{{ W}}$.\n\n"
        f"1. Explain why the average power dissipated in an AC circuit with purely resistive load is given by "
        f"$P_{{\\text{{ave}}}} = \\frac{{1}}{{2}} V_{{\\text{{max}}}} I_{{\\text{{max}}}}$ rather than $V_{{\\text{{max}}}} I_{{\\text{{max}}}}$.\n"
        f"2. Calculate the peak instantaneous power ($P_{{\\text{{max}}}}$) delivered to the oven.\n"
        f"3. Explain why electrical appliance ratings in South Africa specify rms values rather than peak values."
    )
    ans = f"P_max = {_fmt_tex(p_max)} W"
    sol = (
        f"1. In a sinusoidal AC waveform, both voltage and current vary continuously from zero to maximum values. "
        f"The instantaneous power $p(t) = v(t)i(t) = V_{{\\text{{max}}}}I_{{\\text{{max}}}}\\sin^2(\\omega t)$. "
        f"The mathematical average of $\\sin^2(\\omega t)$ over a complete cycle is $\\frac{{1}}{{2}}$. "
        f"Therefore, $P_{{\\text{{ave}}}} = \\frac{{1}}{{2}} V_{{\\text{{max}}}} I_{{\\text{{max}}}} = V_{{\\text{{rms}}}} I_{{\\text{{rms}}}}$.\n"
        f"2. $P_{{\\text{{max}}}} = 2 \\times P_{{\\text{{ave}}}} = 2 \\times {p_ave} = {_fmt_tex(p_max)}\\text{{ W}}$.\n"
        f"3. Rms values are specified because they represent the equivalent direct current (DC) value that delivers the exact same heating effect or average power in a resistor."
    )
    rubric = [
        {"criterion": "Explained average of sin^2(wt) is 1/2 over full cycle", "marks": 1},
        {"criterion": f"Calculated peak power P_max = 2 * P_ave = {_fmt_tex(p_max)} W", "marks": 1},
        {"criterion": "Stated rms is the equivalent DC value providing same thermal power", "marks": 1},
    ]
    hints = {
        "tier_1": "Peak power is exactly double average power: P_max = 2 * P_ave.",
        "tier_2": f"P_max = 2 * {p_ave} = {p_max} W.",
        "tier_3": ans,
    }
    return _make_q(r, "29_ac_peak_power_versus_average_power", 29, prompt, ans, sol, 3, ["assumed_average_power_equals_peak_power"], rubric, hints)


def build_30_domestic_ac_appliance_energy_consumption_and_cost(r: random.Random) -> Dict[str, Any]:
    p_w = r.choice([1500, 1800, 2000, 2200, 2500])
    p_kw = p_w / 1000.0
    hours_per_day = r.choice([2, 3, 4, 5])
    days = 30
    total_hours = hours_per_day * days
    energy_kwh = round(p_kw * total_hours, 1)
    tariff_rand = r.choice([2.45, 2.65, 2.85, 3.10, 3.25])
    total_cost = round(energy_kwh * tariff_rand, 2)

    prompt = (
        f"A domestic space heater with a power rating of ${p_w}\\text{{ W}}$ is operated for ${hours_per_day}\\text{{ hours}}$ "
        f"per day during a ${days}\\text{{-day}}$ winter month.\n"
        f"The local municipality charges electricity at a tariff of $\\text{{R }}{_fmt_tex(tariff_rand)}\\text{{ per kWh}}$.\n\n"
        f"1. Calculate the total energy consumed by the heater in kilowatt-hours (kWh) over the ${days}\\text{{-day}}$ period.\n"
        f"2. Calculate the total cost (in Rands) of operating this space heater for the month."
    )
    ans = f"Energy = {_fmt_tex(energy_kwh)} kWh; Cost = R {_fmt_tex(total_cost)}"
    sol = (
        f"1. Power in kilowatts: $P = \\frac{{{p_w}}}{{1000}} = {_fmt_tex(p_kw)}\\text{{ kW}}$.\n"
        f"   Total operating hours: $\\Delta t = {hours_per_day} \\times {days} = {total_hours}\\text{{ hours}}$.\n"
        f"   Energy consumed: $E = P \\times \\Delta t = {_fmt_tex(p_kw)} \\times {total_hours} = {_fmt_tex(energy_kwh)}\\text{{ kWh}}$.\n"
        f"2. Total cost: $\\text{{Cost}} = E \\times \\text{{tariff}} = {_fmt_tex(energy_kwh)} \\times {_fmt_tex(tariff_rand)} = \\text{{R }}{_fmt_tex(total_cost)}$."
    )
    rubric = [
        {"criterion": f"Converted power to kW: {_fmt_tex(p_kw)} kW", "marks": 1},
        {"criterion": f"Calculated energy E = {_fmt_tex(energy_kwh)} kWh", "marks": 1},
        {"criterion": f"Calculated total cost = R {_fmt_tex(total_cost)}", "marks": 1},
    ]
    hints = {
        "tier_1": "Energy (kWh) = Power (kW) * time (hours). Cost = Energy * tariff.",
        "tier_2": f"E = {_fmt(p_kw)} kW * {total_hours} h = {_fmt(energy_kwh)} kWh.",
        "tier_3": ans,
    }
    return _make_q(r, "30_domestic_ac_appliance_energy_consumption_and_cost", 30, prompt, ans, sol, 3, ["used_watts_instead_of_kilowatts_for_kwh"], rubric, hints)


# ============================================================================ #
# SUBSKILLS 31–36: EMF, INTERNAL RESISTANCE & LOST VOLTS
# ============================================================================ #

def build_31_electromotive_force_emf_definition_and_measurement(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([6, 9, 12, 18, 24])

    prompt = (
        f"A lead-acid storage battery has a label stating that its electromotive force (emf) is ${emf_val}\\text{{ V}}$.\n\n"
        f"1. Define the term *electromotive force (emf)* of a battery.\n"
        f"2. Describe how the emf of this battery can be measured experimentally using a voltmeter.\n"
        f"3. Explain why the voltmeter reading will decrease as soon as a light bulb is connected across the terminals."
    )
    ans = f"emf = {emf_val} V; terminal pd drops due to internal resistance (lost volts = Ir)"
    sol = (
        f"1. **Electromotive force (emf)** is defined as the maximum energy provided by a battery per unit charge passing through it "
        f"(or the maximum work done per unit electric charge by the source).\n"
        f"2. Connect a high-resistance voltmeter directly across the battery terminals when the external circuit is open (switch open, so no current flows).\n"
        f"3. Real batteries have an internal resistance ($r$). When current ($I$) flows through the closed circuit, some electrical potential energy is dissipated "
        f"internally inside the battery as heat ($V_{{\\text{{lost}}}} = Ir$). The terminal potential difference is $V_{{\\text{{terminal}}}} = \\mathcal{{E}} - Ir$, which is less than the emf."
    )
    rubric = [
        {"criterion": "Defined emf as max energy provided per unit charge / work per coulomb", "marks": 1},
        {"criterion": "Stated voltmeter connected across terminals in open circuit (zero current)", "marks": 1},
        {"criterion": "Explained lost volts inside internal resistance: V_term = emf - Ir", "marks": 1},
    ]
    hints = {
        "tier_1": "Emf is work done per unit charge when no current flows.",
        "tier_2": "When current flows, V_terminal = emf - I*r.",
        "tier_3": ans,
    }
    return _make_q(r, "31_electromotive_force_emf_definition_and_measurement", 31, prompt, ans, sol, 3, ["confused_emf_with_terminal_potential_difference"], rubric, hints)


def build_32_internal_resistance_and_lost_volts_concept(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])
    r_int = round(r.choice([0.5, 0.8, 1.0, 1.2, 1.5]), 1)
    i_val = round(r.choice([2.0, 2.5, 3.0, 4.0]), 1)
    v_lost = round(i_val * r_int, 2)
    v_term = round(emf_val - v_lost, 2)

    prompt = (
        f"A battery with an emf of ${emf_val}\\text{{ V}}$ and an internal resistance of ${r_int}\\ \\Omega$ is connected to an external circuit. "
        f"An ammeter measures a steady current of ${i_val}\\text{{ A}}$ delivering charge through the circuit.\n\n"
        f"1. Calculate the 'lost volts' ($V_{{\\text{{lost}}}}$) dissipated across the internal resistance of the battery.\n"
        f"2. Calculate the terminal potential difference ($V_{{\\text{{load}}}}$) available to the external circuit."
    )
    ans = f"V_lost = {_fmt_tex(v_lost)} V; V_load = {_fmt_tex(v_term)} V"
    sol = (
        f"1. $V_{{\\text{{lost}}}} = I r = ({_fmt_tex(i_val)})({_fmt_tex(r_int)}) = {_fmt_tex(v_lost)}\\text{{ V}}$.\n"
        f"2. $V_{{\\text{{load}}}} = \\mathcal{{E}} - V_{{\\text{{lost}}}} = {emf_val} - {_fmt_tex(v_lost)} = {_fmt_tex(v_term)}\\text{{ V}}$."
    )
    rubric = [
        {"criterion": "Formula: V_lost = I * r", "marks": 1},
        {"criterion": f"Calculated V_lost = {_fmt_tex(v_lost)} V", "marks": 1},
        {"criterion": "Formula: V_load = emf - V_lost", "marks": 1},
        {"criterion": f"Calculated V_load = {_fmt_tex(v_term)} V", "marks": 1},
    ]
    hints = {
        "tier_1": "Lost volts = I * r. Terminal pd = emf - lost volts.",
        "tier_2": f"V_lost = {_fmt(i_val)} * {_fmt(r_int)} = {_fmt(v_lost)} V.",
        "tier_3": ans,
    }
    return _make_q(r, "32_internal_resistance_and_lost_volts_concept", 32, prompt, ans, sol, 4, ["treated_battery_as_ideal_with_zero_internal_resistance"], rubric, hints)


def build_33_terminal_potential_difference_calculation(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([9, 12, 15, 24])
    r_ext = r.choice([5, 8, 10, 15, 20])
    r_int = round(r.choice([0.5, 1.0, 1.5, 2.0]), 1)
    r_tot = r_ext + r_int
    i_curr = round(emf_val / r_tot, 2)
    v_term = round(i_curr * r_ext, 2)

    prompt = (
        f"A battery with an electromotive force of ${emf_val}\\text{{ V}}$ and internal resistance of ${r_int}\\ \\Omega$ is connected across a "
        f"resistor of resistance ${r_ext}\\ \\Omega$.\n\n"
        f"1. Calculate the total resistance of the entire circuit.\n"
        f"2. Calculate the current flowing in the circuit.\n"
        f"3. Calculate the terminal potential difference across the battery."
    )
    ans = f"R_tot = {_fmt_tex(r_tot)} Ohm; I = {_fmt_tex(i_curr)} A; V_term = {_fmt_tex(v_term)} V"
    sol = (
        f"1. $R_{{\\text{{total}}}} = R_{{\\text{{ext}}}} + r = {r_ext} + {_fmt_tex(r_int)} = {_fmt_tex(r_tot)}\\ \\Omega$.\n"
        f"2. $I = \\frac{{\\mathcal{{E}}}}{{R_{{\\text{{total}}}}}} = \\frac{{{emf_val}}}{{{_fmt_tex(r_tot)}}} = {_fmt_tex(i_curr)}\\text{{ A}}$.\n"
        f"3. $V_{{\\text{{terminal}}}} = I R_{{\\text{{ext}}}} = ({_fmt_tex(i_curr)})({r_ext}) = {_fmt_tex(v_term)}\\text{{ V}}$\n"
        f"   (or $V_{{\\text{{terminal}}}} = \\mathcal{{E}} - Ir = {emf_val} - ({_fmt_tex(i_curr)})({_fmt_tex(r_int)}) = {_fmt_tex(v_term)}\\text{{ V}}$)."
    )
    rubric = [
        {"criterion": f"Calculated R_total = {_fmt_tex(r_tot)} Ohm", "marks": 1},
        {"criterion": f"Calculated current I = {_fmt_tex(i_curr)} A", "marks": 1},
        {"criterion": f"Calculated V_terminal = {_fmt_tex(v_term)} V", "marks": 1},
    ]
    hints = {
        "tier_1": "R_total = R_ext + r. I = emf / R_total. V_term = I * R_ext.",
        "tier_2": f"I = {emf_val} / {_fmt(r_tot)} = {_fmt(i_curr)} A.",
        "tier_3": ans,
    }
    return _make_q(r, "33_terminal_potential_difference_calculation", 33, prompt, ans, sol, 3, ["forgot_internal_resistance_in_total_resistance"], rubric, hints)


def build_34_calculate_internal_resistance_given_emf_current_rload(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 15, 24])
    r_int_exact = round(r.choice([0.6, 0.8, 1.2, 1.5, 2.0]), 1)
    i_curr = round(r.choice([2.0, 2.5, 3.0, 4.0]), 1)
    v_lost = round(i_curr * r_int_exact, 2)
    v_load = round(emf_val - v_lost, 2)

    prompt = (
        f"When an external resistor is connected to a battery of emf ${emf_val}\\text{{ V}}$, a voltmeter placed across the battery terminals reads "
        f"${_fmt_tex(v_load)}\\text{{ V}}$ while an ammeter measures a current of ${_fmt_tex(i_curr)}\\text{{ A}}$.\n\n"
        f"1. Calculate the 'lost volts' across the internal resistance.\n"
        f"2. Calculate the internal resistance ($r$) of the battery."
    )
    ans = f"V_lost = {_fmt_tex(v_lost)} V; r = {_fmt_tex(r_int_exact)} Ohm"
    sol = (
        f"1. $V_{{\\text{{lost}}}} = \\mathcal{{E}} - V_{{\\text{{load}}}} = {emf_val} - {_fmt_tex(v_load)} = {_fmt_tex(v_lost)}\\text{{ V}}$.\n"
        f"2. $V_{{\\text{{lost}}}} = I r \\implies r = \\frac{{V_{{\\text{{lost}}}}}}{{I}} = \\frac{{{_fmt_tex(v_lost)}}}{{{_fmt_tex(i_curr)}}} = {_fmt_tex(r_int_exact)}\\ \\Omega$."
    )
    rubric = [
        {"criterion": f"Calculated V_lost = {_fmt_tex(v_lost)} V", "marks": 1},
        {"criterion": "Formula: r = V_lost / I", "marks": 1},
        {"criterion": f"Calculated r = {_fmt_tex(r_int_exact)} Ohm", "marks": 1},
    ]
    hints = {
        "tier_1": "Lost volts = emf - V_load. Then r = V_lost / I.",
        "tier_2": f"V_lost = {emf_val} - {_fmt(v_load)} = {_fmt(v_lost)} V. r = {_fmt(v_lost)} / {_fmt(i_curr)}.",
        "tier_3": ans,
    }
    return _make_q(r, "34_calculate_internal_resistance_given_emf_current_rload", 34, prompt, ans, sol, 3, ["divided_emf_by_current_directly"], rubric, hints)


def build_35_calculate_emf_given_load_resistance_and_two_currents(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])
    r_int = round(r.choice([1.0, 1.5, 2.0]), 1)
    r1 = r.choice([4, 5, 6])
    r2 = r.choice([8, 10, 12])
    i1 = round(emf_val / (r1 + r_int), 2)
    i2 = round(emf_val / (r2 + r_int), 2)

    prompt = (
        f"An unknown direct-current battery of electromotive force $\\mathcal{{E}}$ and internal resistance $r$ is connected to two different external loads in turn:\n"
        f"- When connected to a resistor of resistance ${r1}\\ \\Omega$, the ammeter reads ${_fmt_tex(i1)}\\text{{ A}}$.\n"
        f"- When connected to a resistor of resistance ${r2}\\ \\Omega$, the ammeter reads ${_fmt_tex(i2)}\\text{{ A}}$.\n\n"
        f"1. Write down an equation expressing $\\mathcal{{E}}$ in terms of $r$ for the first resistor (${r1}\\ \\Omega$).\n"
        f"2. Write down an equation expressing $\\mathcal{{E}}$ in terms of $r$ for the second resistor (${r2}\\ \\Omega$).\n"
        f"3. Solve the equations simultaneously to determine the internal resistance $r$ and the electromotive force $\\mathcal{{E}}$."
    )
    ans = f"r = {_fmt_tex(r_int)} Ohm; emf = {emf_val} V"
    sol = (
        f"1. Equation 1: $\\mathcal{{E}} = I_1 (R_1 + r) = {_fmt_tex(i1)}({r1} + r) = {_fmt_tex(i1 * r1)} + {_fmt_tex(i1)}r$.\n"
        f"2. Equation 2: $\\mathcal{{E}} = I_2 (R_2 + r) = {_fmt_tex(i2)}({r2} + r) = {_fmt_tex(i2 * r2)} + {_fmt_tex(i2)}r$.\n"
        f"3. Equating both expressions:\n"
        f"   ${_fmt_tex(i1 * r1)} + {_fmt_tex(i1)}r = {_fmt_tex(i2 * r2)} + {_fmt_tex(i2)}r$\n"
        f"   $({_fmt_tex(i1)} - {_fmt_tex(i2)})r = {_fmt_tex(i2 * r2)} - {_fmt_tex(i1 * r1)}$\n"
        f"   $r = {_fmt_tex(r_int)}\\ \\Omega$.\n"
        f"   Substitute $r = {_fmt_tex(r_int)}\\ \\Omega$ into Equation 1:\n"
        f"   $\\mathcal{{E}} = {_fmt_tex(i1)}({r1} + {_fmt_tex(r_int)}) = {emf_val}\\text{{ V}}$."
    )
    rubric = [
        {"criterion": "Set up equation 1: emf = I1*(R1 + r)", "marks": 1},
        {"criterion": "Set up equation 2: emf = I2*(R2 + r)", "marks": 1},
        {"criterion": f"Solved for internal resistance r = {_fmt_tex(r_int)} Ohm", "marks": 1},
        {"criterion": f"Calculated electromotive force emf = {emf_val} V", "marks": 1},
    ]
    hints = {
        "tier_1": "Recall: emf = I*(R + r) for each state. Equate the two expressions.",
        "tier_2": f"({_fmt(i1)})({r1} + r) = ({_fmt(i2)})({r2} + r). Solve for r.",
        "tier_3": ans,
    }
    return _make_q(r, "35_calculate_emf_given_load_resistance_and_two_currents", 35, prompt, ans, sol, 4, ["incorrect_simultaneous_equation_substitution"], rubric, hints)


def build_36_maximum_current_from_short_circuited_battery(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 24, 36])
    r_int = round(r.choice([0.2, 0.4, 0.5, 0.8]), 1)
    i_sc = round(emf_val / r_int, 1)
    p_sc = round((i_sc ** 2) * r_int, 1)

    prompt = (
        f"A lead-acid car battery has an electromotive force of ${emf_val}\\text{{ V}}$ and an internal resistance of ${r_int}\\ \\Omega$. "
        f"A technician accidentally drops a steel wrench directly across the two battery terminals, causing a direct short circuit ($R_{{\\text{{ext}}}} \\approx 0\\ \\Omega$).\n\n"
        f"1. Calculate the maximum theoretical short-circuit current ($I_{{\\text{{sc}}}}$) flowing through the battery.\n"
        f"2. Calculate the rate at which electrical energy is converted into heat inside the battery during the short circuit.\n"
        f"3. State two safety hazards associated with short-circuiting a chemical battery."
    )
    ans = f"I_sc = {_fmt_tex(i_sc)} A; P_lost = {_fmt_tex(p_sc)} W"
    sol = (
        f"1. At short circuit, $R_{{\\text{{ext}}}} = 0$: $I_{{\\text{{sc}}}} = \\frac{{\\mathcal{{E}}}}{{r}} = \\frac{{{emf_val}}}{{{_fmt_tex(r_int)}}} = {_fmt_tex(i_sc)}\\text{{ A}}$.\n"
        f"2. Internal thermal power dissipation: $P = I_{{\\text{{sc}}}}^2 r = ({_fmt_tex(i_sc)})^2 ({_fmt_tex(r_int)}) = {_fmt_tex(p_sc)}\\text{{ W}}$.\n"
        f"3. Hazards: (a) Rapid overheating and boiling/vaporization of acid electrolyte leading to battery explosion, "
        f"(b) Fire hazard from red-hot shorting conductor, or release of toxic hydrogen gas."
    )
    rubric = [
        {"criterion": f"Calculated short-circuit current I_sc = {_fmt_tex(i_sc)} A", "marks": 1},
        {"criterion": f"Calculated internal thermal power dissipation P = {_fmt_tex(p_sc)} W", "marks": 1},
        {"criterion": "Stated explosion/fire/acid boil hazard", "marks": 1},
    ]
    hints = {
        "tier_1": "For short circuit, external resistance R = 0, so I = emf / r.",
        "tier_2": f"I_sc = {emf_val} / {_fmt(r_int)} = {_fmt(i_sc)} A. P = I^2 * r.",
        "tier_3": ans,
    }
    return _make_q(r, "36_maximum_current_from_short_circuited_battery", 36, prompt, ans, sol, 3, ["assumed_short_circuit_current_is_infinite"], rubric, hints)


# ============================================================================ #
# SUBSKILLS 37–38: GRAPHICAL ANALYSIS OF TERMINAL VOLTAGE VS CURRENT
# ============================================================================ #

def build_37_graphical_analysis_terminal_voltage_vs_current_intercept_and_slope(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([6, 9, 12, 18])
    r_int = round(r.choice([1.0, 1.5, 2.0]), 1)
    i1 = round(r.choice([1.0, 1.5, 2.0]), 1)
    v1 = round(emf_val - i1 * r_int, 1)

    # Inline vector SVG graph of V vs I
    # Axes: horizontal (Current I in A) 0..6 A, vertical (Voltage V in V) 0..20 V
    x_max = 5.0
    y_max = emf_val * 1.25
    x_origin, y_origin = 60, 260
    plot_w, plot_h = 360, 200

    def to_svg(i_c: float, v_c: float) -> tuple[float, float]:
        sx = x_origin + (i_c / x_max) * plot_w
        sy = y_origin - (v_c / y_max) * plot_h
        return sx, sy

    x_int_c = emf_val / r_int
    x_end_val = min(x_int_c, 4.0)
    y_end_val = emf_val - x_end_val * r_int

    p0_x, p0_y = to_svg(0.0, float(emf_val))
    p1_x, p1_y = to_svg(i1, v1)
    pe_x, pe_y = to_svg(x_end_val, y_end_val)

    svg = (
        f'<svg viewBox="0 0 480 300" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">\n'
        f'  <rect width="480" height="300" fill="#ffffff" />\n'
        f'  <!-- Axes -->\n'
        f'  <line x1="{x_origin}" y1="{y_origin}" x2="{x_origin + plot_w + 30}" y2="{y_origin}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />\n'
        f'  <line x1="{x_origin}" y1="{y_origin}" x2="{x_origin}" y2="{y_origin - plot_h - 30}" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />\n'
        f'  <!-- Labels -->\n'
        f'  <text x="{x_origin + plot_w + 35}" y="{y_origin + 5}" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">I (A)</text>\n'
        f'  <text x="{x_origin - 15}" y="{y_origin - plot_h - 35}" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">V (V)</text>\n'
        f'  <!-- Intercept marker -->\n'
        f'  <circle cx="{p0_x:.1f}" cy="{p0_y:.1f}" r="4" fill="#2563eb" />\n'
        f'  <text x="{p0_x - 30:.1f}" y="{p0_y + 4:.1f}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#2563eb">{emf_val}</text>\n'
        f'  <!-- Data point 1 -->\n'
        f'  <line x1="{p1_x:.1f}" y1="{y_origin}" x2="{p1_x:.1f}" y2="{p1_y:.1f}" stroke="#94a3b8" stroke-dasharray="4,4" />\n'
        f'  <line x1="{x_origin}" y1="{p1_y:.1f}" x2="{p1_x:.1f}" y2="{p1_y:.1f}" stroke="#94a3b8" stroke-dasharray="4,4" />\n'
        f'  <circle cx="{p1_x:.1f}" cy="{p1_y:.1f}" r="4" fill="#dc2626" />\n'
        f'  <text x="{p1_x - 10:.1f}" y="{y_origin + 18}" font-family="sans-serif" font-size="11" fill="#475569">{_fmt(i1)}</text>\n'
        f'  <text x="{x_origin - 35:.1f}" y="{p1_y + 4:.1f}" font-family="sans-serif" font-size="11" fill="#475569">{_fmt(v1)}</text>\n'
        f'  <!-- Best fit line -->\n'
        f'  <line x1="{p0_x:.1f}" y1="{p0_y:.1f}" x2="{pe_x:.1f}" y2="{pe_y:.1f}" stroke="#2563eb" stroke-width="2.5" />\n'
        f'</svg>'
    )
    diagram = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}

    prompt = (
        f"Refer to the terminal potential difference versus current graph below obtained experimentally for a direct-current cell.\n\n"
        f"1. Write down the mathematical relationship between terminal potential difference ($V$), electromotive force ($\\mathcal{{E}}$), "
        f"current ($I$), and internal resistance ($r$).\n"
        f"2. From the graph, deduce the electromotive force ($\\mathcal{{E}}$) of the cell.\n"
        f"3. Calculate the gradient (slope) of the line.\n"
        f"4. Hence, determine the internal resistance ($r$) of the cell."
    )
    slope = -r_int
    ans = f"emf = {emf_val} V; gradient = {_fmt_tex(slope)} V/A; r = {_fmt_tex(r_int)} Ohm"
    sol = (
        f"1. $V = \\mathcal{{E}} - Ir = -rI + \\mathcal{{E}}$ (form of linear equation $y = mx + c$).\n"
        f"2. The vertical intercept ($y$-intercept where $I = 0$) represents the electromotive force: $\\mathcal{{E}} = {emf_val}\\text{{ V}}$.\n"
        f"3. $\\text{{Gradient}} = \\frac{{y_2 - y_1}}{{x_2 - x_1}} = \\frac{{{_fmt_tex(v1)} - {emf_val}}}{{{_fmt_tex(i1)} - 0}} = \\frac{{{_fmt_tex(v1 - emf_val)}}}{{{_fmt_tex(i1)}}} = {_fmt_tex(slope)}\\text{{ V}}\\cdot\\text{{A}}^{{-1}}$.\n"
        f"4. Since $\\text{{gradient}} = -r$, internal resistance $r = -(\\text{{gradient}}) = {_fmt_tex(r_int)}\\ \\Omega$."
    )
    rubric = [
        {"criterion": "Stated V = emf - Ir", "marks": 1},
        {"criterion": f"Read vertical intercept: emf = {emf_val} V", "marks": 1},
        {"criterion": f"Calculated slope = {_fmt_tex(slope)}", "marks": 1},
        {"criterion": f"Duly concluded r = {_fmt_tex(r_int)} Ohm", "marks": 1},
    ]
    hints = {
        "tier_1": "The y-intercept gives the emf. The gradient of V vs I equals -r.",
        "tier_2": f"y-intercept is {emf_val} V. Gradient = ({_fmt(v1)} - {emf_val}) / ({_fmt(i1)} - 0).",
        "tier_3": ans,
    }
    return _make_q(r, "37_graphical_analysis_terminal_voltage_vs_current_intercept_and_slope", 37, prompt, ans, sol, 4, ["used_positive_gradient_for_internal_resistance"], rubric, hints, diagram_spec=diagram)


def build_38_graphical_determination_of_internal_resistance_from_experimental_data(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])
    r_int = round(r.choice([0.8, 1.2, 1.5, 2.0]), 1)
    i1 = round(r.choice([1.0, 1.5]), 1)
    i2 = round(i1 + r.choice([2.0, 2.5, 3.0]), 1)
    v1 = round(emf_val - i1 * r_int, 2)
    v2 = round(emf_val - i2 * r_int, 2)

    prompt = (
        f"A learner conducts an experiment to determine the emf and internal resistance of a battery. "
        f"The learner records the following terminal potential difference ($V$) readings for two operating currents ($I$):\n\n"
        f"| Reading | Current $I$ (A) | Terminal pd $V$ (V) |\n"
        f"| :--- | :---: | :---: |\n"
        f"| 1 | ${_fmt_tex(i1)}$ | ${_fmt_tex(v1)}$ |\n"
        f"| 2 | ${_fmt_tex(i2)}$ | ${_fmt_tex(v2)}$ |\n\n"
        f"1. Calculate the rate of change of terminal potential difference with current ($\\frac{{\\Delta V}}{{\\Delta I}}$).\n"
        f"2. State the physical quantity represented by the absolute value of $\\frac{{\\Delta V}}{{\\Delta I}}$.\n"
        f"3. Calculate the internal resistance ($r$) of the battery.\n"
        f"4. Calculate the electromotive force ($\\mathcal{{E}}$) of the battery."
    )
    delta_v = round(v2 - v1, 2)
    delta_i = round(i2 - i1, 2)
    gradient = round(delta_v / delta_i, 2)
    ans = f"gradient = {_fmt_tex(gradient)} V/A; r = {_fmt_tex(r_int)} Ohm; emf = {emf_val} V"
    sol = (
        f"1. $\\frac{{\\Delta V}}{{\\Delta I}} = \\frac{{{_fmt_tex(v2)} - {_fmt_tex(v1)}}}{{{_fmt_tex(i2)} - {_fmt_tex(i1)}}} = \\frac{{{_fmt_tex(delta_v)}}}{{{_fmt_tex(delta_i)}}} = {_fmt_tex(gradient)}\\text{{ V}}\\cdot\\text{{A}}^{{-1}}$.\n"
        f"2. The absolute value of $\\frac{{\\Delta V}}{{\\Delta I}}$ represents the **internal resistance** ($r$) of the cell.\n"
        f"3. $r = -\\frac{{\\Delta V}}{{\\Delta I}} = {_fmt_tex(r_int)}\\ \\Omega$.\n"
        f"4. $\\mathcal{{E}} = V_1 + I_1 r = {_fmt_tex(v1)} + ({_fmt_tex(i1)})({_fmt_tex(r_int)}) = {emf_val}\\text{{ V}}$."
    )
    rubric = [
        {"criterion": f"Calculated delta V / delta I = {_fmt_tex(gradient)}", "marks": 1},
        {"criterion": "Identified physical quantity as internal resistance", "marks": 1},
        {"criterion": f"Determined r = {_fmt_tex(r_int)} Ohm", "marks": 1},
        {"criterion": f"Calculated emf = {emf_val} V", "marks": 1},
    ]
    hints = {
        "tier_1": "r = - (V2 - V1) / (I2 - I1). Then emf = V + I*r.",
        "tier_2": f"r = -({_fmt(v2)} - {_fmt(v1)}) / ({_fmt(i2)} - {_fmt(i1)}) = {_fmt(r_int)} Ohm.",
        "tier_3": ans,
    }
    return _make_q(r, "38_graphical_determination_of_internal_resistance_from_experimental_data", 38, prompt, ans, sol, 4, ["confused_delta_v_delta_i_sign"], rubric, hints)


# ============================================================================ #
# SUBSKILLS 39–45: SERIES & PARALLEL RESISTOR CIRCUITS WITH INTERNAL RESISTANCE
# ============================================================================ #

def build_39_series_resistor_circuit_with_internal_resistance(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])
    r1 = r.choice([3, 4, 5])
    r2 = r.choice([5, 6, 8])
    r_int = round(r.choice([0.5, 1.0, 1.5]), 1)
    r_ext = r1 + r2
    r_tot = r_ext + r_int
    i_curr = round(emf_val / r_tot, 2)
    v1 = round(i_curr * r1, 2)
    v2 = round(i_curr * r2, 2)
    v_term = round(i_curr * r_ext, 2)

    prompt = (
        f"A battery with an emf of ${emf_val}\\text{{ V}}$ and internal resistance of ${r_int}\\ \\Omega$ is connected in series with two resistors, "
        f"$R_1 = {r1}\\ \\Omega$ and $R_2 = {r2}\\ \\Omega$.\n\n"
        f"1. Calculate the total resistance ($R_{{\\text{{total}}}}$) of the circuit.\n"
        f"2. Calculate the current ($I$) flowing through the circuit.\n"
        f"3. Calculate the potential difference across resistor $R_1$.\n"
        f"4. Calculate the terminal potential difference across the battery."
    )
    ans = f"R_tot = {_fmt_tex(r_tot)} Ohm; I = {_fmt_tex(i_curr)} A; V1 = {_fmt_tex(v1)} V; V_term = {_fmt_tex(v_term)} V"
    sol = (
        f"1. $R_{{\\text{{total}}}} = R_1 + R_2 + r = {r1} + {r2} + {_fmt_tex(r_int)} = {_fmt_tex(r_tot)}\\ \\Omega$.\n"
        f"2. $I = \\frac{{\\mathcal{{E}}}}{{R_{{\\text{{total}}}}}} = \\frac{{{emf_val}}}{{{_fmt_tex(r_tot)}}} = {_fmt_tex(i_curr)}\\text{{ A}}$.\n"
        f"3. $V_1 = I R_1 = ({_fmt_tex(i_curr)})({r1}) = {_fmt_tex(v1)}\\text{{ V}}$.\n"
        f"4. $V_{{\\text{{terminal}}}} = I (R_1 + R_2) = ({_fmt_tex(i_curr)})({r_ext}) = {_fmt_tex(v_term)}\\text{{ V}}$."
    )
    rubric = [
        {"criterion": f"Calculated R_tot = {_fmt_tex(r_tot)} Ohm", "marks": 1},
        {"criterion": f"Calculated current I = {_fmt_tex(i_curr)} A", "marks": 1},
        {"criterion": f"Calculated V1 = {_fmt_tex(v1)} V", "marks": 1},
        {"criterion": f"Calculated V_terminal = {_fmt_tex(v_term)} V", "marks": 1},
    ]
    hints = {
        "tier_1": "Add all three resistances in series. I = emf / R_total.",
        "tier_2": f"R_total = {r1} + {r2} + {_fmt(r_int)} = {_fmt(r_tot)} Ohm. I = {emf_val} / {_fmt(r_tot)}.",
        "tier_3": ans,
    }
    return _make_q(r, "39_series_resistor_circuit_with_internal_resistance", 39, prompt, ans, sol, 4, ["neglected_internal_resistance_in_series_sum"], rubric, hints)


def build_40_parallel_resistor_circuit_with_internal_resistance(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])
    r1 = r.choice([6, 12, 20])
    r2 = r.choice([6, 12, 20])
    r_p = round((r1 * r2) / (r1 + r2), 2)
    r_int = round(r.choice([0.5, 1.0, 1.5]), 1)
    r_tot = round(r_p + r_int, 2)
    i_tot = round(emf_val / r_tot, 2)
    v_term = round(i_tot * r_p, 2)
    i1 = round(v_term / r1, 2)

    prompt = (
        f"A direct-current battery with an electromotive force of ${emf_val}\\text{{ V}}$ and internal resistance of ${r_int}\\ \\Omega$ is "
        f"connected to two external resistors in parallel: $R_1 = {r1}\\ \\Omega$ and $R_2 = {r2}\\ \\Omega$.\n\n"
        f"1. Calculate the equivalent resistance ($R_p$) of the parallel combination.\n"
        f"2. Calculate the total current ($I_{{\\text{{total}}}}$) leaving the battery.\n"
        f"3. Calculate the terminal potential difference ($V_{{\\text{{terminal}}}}$) of the battery.\n"
        f"4. Calculate the current flowing through resistor $R_1$."
    )
    ans = f"Rp = {_fmt_tex(r_p)} Ohm; I_tot = {_fmt_tex(i_tot)} A; V_term = {_fmt_tex(v_term)} V; I1 = {_fmt_tex(i1)} A"
    sol = (
        f"1. $\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_2}} = \\frac{{1}}{{{r1}}} + \\frac{{1}}{{{r2}}} \\implies R_p = {_fmt_tex(r_p)}\\ \\Omega$.\n"
        f"2. $R_{{\\text{{total}}}} = R_p + r = {_fmt_tex(r_p)} + {_fmt_tex(r_int)} = {_fmt_tex(r_tot)}\\ \\Omega$.\n"
        f"   $I_{{\\text{{total}}}} = \\frac{{\\mathcal{{E}}}}{{R_{{\\text{{total}}}}}} = \\frac{{{emf_val}}}{{{_fmt_tex(r_tot)}}} = {_fmt_tex(i_tot)}\\text{{ A}}$.\n"
        f"3. $V_{{\\text{{terminal}}}} = I_{{\\text{{total}}}} R_p = ({_fmt_tex(i_tot)})({_fmt_tex(r_p)}) = {_fmt_tex(v_term)}\\text{{ V}}$.\n"
        f"4. $I_1 = \\frac{{V_{{\\text{{terminal}}}}}}{{R_1}} = \\frac{{{_fmt_tex(v_term)}}}{{{r1}}} = {_fmt_tex(i1)}\\text{{ A}}$."
    )
    rubric = [
        {"criterion": f"Calculated R_p = {_fmt_tex(r_p)} Ohm", "marks": 1},
        {"criterion": f"Calculated total current I_tot = {_fmt_tex(i_tot)} A", "marks": 1},
        {"criterion": f"Calculated V_terminal = {_fmt_tex(v_term)} V", "marks": 1},
        {"criterion": f"Calculated branch current I1 = {_fmt_tex(i1)} A", "marks": 1},
    ]
    hints = {
        "tier_1": "1/Rp = 1/R1 + 1/R2. Then R_total = Rp + r. Terminal pd is Vp = I_tot * Rp.",
        "tier_2": f"Rp = {_fmt(r_p)} Ohm. I_total = {emf_val} / ({_fmt(r_p)} + {_fmt(r_int)}).",
        "tier_3": ans,
    }
    return _make_q(r, "40_parallel_resistor_circuit_with_internal_resistance", 40, prompt, ans, sol, 4, ["added_parallel_resistors_directly_instead_of_reciprocals"], rubric, hints)


def build_41_series_parallel_combination_circuit_with_internal_resistance(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])
    r_int = round(r.choice([1.0, 1.5, 2.0]), 1)
    r_s = r.choice([3, 4, 5])
    r_p1 = r.choice([6, 12])
    r_p2 = r.choice([6, 12])
    r_p = round((r_p1 * r_p2) / (r_p1 + r_p2), 2)
    r_ext = round(r_s + r_p, 2)
    r_tot = round(r_ext + r_int, 2)
    i_main = round(emf_val / r_tot, 2)
    v_term = round(i_main * r_ext, 2)
    v_p = round(i_main * r_p, 2)

    # Inline vector SVG of series-parallel circuit
    svg = (
        f'<svg viewBox="0 0 520 280" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">\n'
        f'  <rect width="520" height="280" fill="#ffffff" />\n'
        f'  <!-- Circuit wires -->\n'
        f'  <polyline points="70,140 70,60 210,60" fill="none" stroke="#1e293b" stroke-width="2" />\n'
        f'  <polyline points="290,60 340,60" fill="none" stroke="#1e293b" stroke-width="2" />\n'
        f'  <!-- Parallel branches split -->\n'
        f'  <polyline points="340,60 340,30 380,30" fill="none" stroke="#1e293b" stroke-width="2" />\n'
        f'  <polyline points="340,60 340,90 380,90" fill="none" stroke="#1e293b" stroke-width="2" />\n'
        f'  <polyline points="440,30 480,30 480,60" fill="none" stroke="#1e293b" stroke-width="2" />\n'
        f'  <polyline points="440,90 480,90 480,60" fill="none" stroke="#1e293b" stroke-width="2" />\n'
        f'  <!-- Return wire -->\n'
        f'  <polyline points="480,60 480,220 70,220 70,160" fill="none" stroke="#1e293b" stroke-width="2" />\n'
        f'  <!-- Battery box (dashed) -->\n'
        f'  <rect x="40" y="110" width="60" height="80" fill="none" stroke="#94a3b8" stroke-dasharray="3,3" />\n'
        f'  <line x1="60" y1="140" x2="80" y2="140" stroke="#0f172a" stroke-width="3" />\n'
        f'  <line x1="65" y1="150" x2="75" y2="150" stroke="#0f172a" stroke-width="1.5" />\n'
        f'  <text x="15" y="148" font-family="sans-serif" font-size="11" fill="#0f172a">{emf_val}V, {r_int}&#937;</text>\n'
        f'  <!-- Series Resistor Rs -->\n'
        f'  <rect x="210" y="50" width="80" height="20" fill="#f8fafc" stroke="#2563eb" stroke-width="2" />\n'
        f'  <text x="235" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">{r_s}&#937;</text>\n'
        f'  <!-- Parallel Resistor Rp1 -->\n'
        f'  <rect x="380" y="20" width="60" height="20" fill="#f8fafc" stroke="#059669" stroke-width="2" />\n'
        f'  <text x="395" y="35" font-family="sans-serif" font-size="11" fill="#059669">{r_p1}&#937;</text>\n'
        f'  <!-- Parallel Resistor Rp2 -->\n'
        f'  <rect x="380" y="80" width="60" height="20" fill="#f8fafc" stroke="#059669" stroke-width="2" />\n'
        f'  <text x="395" y="95" font-family="sans-serif" font-size="11" fill="#059669">{r_p2}&#937;</text>\n'
        f'  <!-- Voltmeter across battery -->\n'
        f'  <circle cx="70" cy="250" r="14" fill="#ffffff" stroke="#d97706" stroke-width="2" />\n'
        f'  <text x="65" y="254" font-family="sans-serif" font-size="12" font-weight="bold" fill="#d97706">V</text>\n'
        f'  <line x1="70" y1="220" x2="70" y2="236" stroke="#d97706" stroke-width="1.5" />\n'
        f'</svg>'
    )
    diagram = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}

    prompt = (
        f"Refer to the electric circuit schematic below containing a real battery of emf ${emf_val}\\text{{ V}}$ and internal resistance ${r_int}\\ \\Omega$ "
        f"connected to a series resistor $R_s = {r_s}\\ \\Omega$ and a parallel combination of $R_1 = {r_p1}\\ \\Omega$ and $R_2 = {r_p2}\\ \\Omega$.\n\n"
        f"1. Calculate the effective external resistance ($R_{{\\text{{ext}}}}$) of the circuit.\n"
        f"2. Calculate the reading on the main ammeter measuring the total current leaving the battery.\n"
        f"3. Calculate the terminal potential difference across the battery terminals.\n"
        f"4. Calculate the potential difference across the parallel combination."
    )
    ans = f"R_ext = {_fmt_tex(r_ext)} Ohm; I_main = {_fmt_tex(i_main)} A; V_term = {_fmt_tex(v_term)} V; V_p = {_fmt_tex(v_p)} V"
    sol = (
        f"1. Parallel equivalent: $R_p = \\frac{{{r_p1} \\times {r_p2}}}{{{r_p1} + {r_p2}}} = {_fmt_tex(r_p)}\\ \\Omega$.\n"
        f"   External resistance: $R_{{\\text{{ext}}}} = R_s + R_p = {r_s} + {_fmt_tex(r_p)} = {_fmt_tex(r_ext)}\\ \\Omega$.\n"
        f"2. Total circuit resistance: $R_{{\\text{{total}}}} = R_{{\\text{{ext}}}} + r = {_fmt_tex(r_ext)} + {_fmt_tex(r_int)} = {_fmt_tex(r_tot)}\\ \\Omega$.\n"
        f"   $I_{{\\text{{main}}}} = \\frac{{\\mathcal{{E}}}}{{R_{{\\text{{total}}}}}} = \\frac{{{emf_val}}}{{{_fmt_tex(r_tot)}}} = {_fmt_tex(i_main)}\\text{{ A}}$.\n"
        f"3. $V_{{\\text{{terminal}}}} = I_{{\\text{{main}}}} R_{{\\text{{ext}}}} = ({_fmt_tex(i_main)})({_fmt_tex(r_ext)}) = {_fmt_tex(v_term)}\\text{{ V}}$.\n"
        f"4. $V_p = I_{{\\text{{main}}}} R_p = ({_fmt_tex(i_main)})({_fmt_tex(r_p)}) = {_fmt_tex(v_p)}\\text{{ V}}$."
    )
    rubric = [
        {"criterion": f"Calculated R_ext = {_fmt_tex(r_ext)} Ohm", "marks": 1},
        {"criterion": f"Calculated I_main = {_fmt_tex(i_main)} A", "marks": 1},
        {"criterion": f"Calculated V_terminal = {_fmt_tex(v_term)} V", "marks": 1},
        {"criterion": f"Calculated V_parallel = {_fmt_tex(v_p)} V", "marks": 1},
    ]
    hints = {
        "tier_1": "Find Rp first, then add Rs to get R_ext. Total resistance includes r.",
        "tier_2": f"Rp = {_fmt(r_p)} Ohm. R_ext = {r_s} + {_fmt(r_p)} = {_fmt(r_ext)} Ohm. I = {emf_val} / ({_fmt(r_ext)} + {_fmt(r_int)}).",
        "tier_3": ans,
    }
    return _make_q(r, "41_series_parallel_combination_circuit_with_internal_resistance", 41, prompt, ans, sol, 4, ["calculated_parallel_voltage_using_total_emf"], rubric, hints, diagram_spec=diagram)


def build_42_voltmeter_reading_across_battery_open_vs_closed_switch(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])
    r_int = round(r.choice([1.0, 1.5, 2.0]), 1)
    r_load = r.choice([4, 6, 8, 10])
    i_closed = round(emf_val / (r_load + r_int), 2)
    v_closed = round(i_closed * r_load, 2)

    prompt = (
        f"A voltmeter is connected across the terminals of a battery having an emf of ${emf_val}\\text{{ V}}$ and internal resistance of "
        f"${r_int}\\ \\Omega$. The external circuit consists of a switch $S$ and an external resistor of resistance ${r_load}\\ \\Omega$.\n\n"
        f"1. State the reading on the voltmeter when switch $S$ is OPEN.\n"
        f"2. Calculate the reading on the voltmeter when switch $S$ is CLOSED.\n"
        f"3. Explain why the voltmeter reading changes when the switch is closed."
    )
    ans = f"V_open = {emf_val} V; V_closed = {_fmt_tex(v_closed)} V"
    sol = (
        f"1. When switch $S$ is open, no current flows ($I = 0$). The voltmeter reads the full electromotive force: $V = \\mathcal{{E}} = {emf_val}\\text{{ V}}$.\n"
        f"2. When switch $S$ is closed, current flows:\n"
        f"   $I = \\frac{{\\mathcal{{E}}}}{{R + r}} = \\frac{{{emf_val}}}{{{r_load} + {_fmt_tex(r_int)}}} = {_fmt_tex(i_closed)}\\text{{ A}}$.\n"
        f"   $V_{{\\text{{closed}}}} = \\mathcal{{E}} - Ir = {emf_val} - ({_fmt_tex(i_closed)})({_fmt_tex(r_int)}) = {_fmt_tex(v_closed)}\\text{{ V}}$.\n"
        f"3. When the switch is closed, current passes through the battery's internal resistance, resulting in internal energy dissipation "
        f"('lost volts' $V_{{\\text{{lost}}}} = Ir$). The terminal pd equals $\\mathcal{{E}} - Ir$."
    )
    rubric = [
        {"criterion": f"Stated V_open = {emf_val} V", "marks": 1},
        {"criterion": f"Calculated V_closed = {_fmt_tex(v_closed)} V", "marks": 1},
        {"criterion": "Explained lost volts Ir due to current through internal resistance", "marks": 1},
    ]
    hints = {
        "tier_1": "With switch open, I = 0 so V = emf. With switch closed, V = emf - I*r.",
        "tier_2": f"V_open = {emf_val} V. I = {emf_val} / ({r_load} + {_fmt(r_int)}) = {_fmt(i_closed)} A.",
        "tier_3": ans,
    }
    return _make_q(r, "42_voltmeter_reading_across_battery_open_vs_closed_switch", 42, prompt, ans, sol, 3, ["assumed_voltmeter_reading_is_identical_open_and_closed"], rubric, hints)


def build_43_voltmeter_reading_across_parallel_resistor_branches(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])
    r_int = round(r.choice([0.8, 1.2, 1.5]), 1)
    r_s = r.choice([2, 3, 4])
    r_p1 = 6
    r_p2 = 12
    r_p = round((r_p1 * r_p2) / (r_p1 + r_p2), 2)  # 4.0
    r_tot = round(r_s + r_p + r_int, 2)
    i_curr = round(emf_val / r_tot, 2)
    v_parallel = round(i_curr * r_p, 2)

    prompt = (
        f"A battery with an emf of ${emf_val}\\text{{ V}}$ and internal resistance of ${r_int}\\ \\Omega$ is connected to a circuit containing "
        f"a series resistor $R_s = {r_s}\\ \\Omega$ and two resistors in parallel ($R_1 = {r_p1}\\ \\Omega$ and $R_2 = {r_p2}\\ \\Omega$). "
        f"A voltmeter $V_2$ is connected across the parallel combination.\n\n"
        f"1. Calculate the total resistance of the circuit.\n"
        f"2. Calculate the main current in the circuit.\n"
        f"3. Calculate the reading on voltmeter $V_2$."
    )
    ans = f"R_tot = {_fmt_tex(r_tot)} Ohm; I = {_fmt_tex(i_curr)} A; V2 = {_fmt_tex(v_parallel)} V"
    sol = (
        f"1. Equivalent parallel resistance: $R_p = \\frac{{{r_p1} \\times {r_p2}}}{{{r_p1} + {r_p2}}} = \\frac{{72}}{{18}} = {_fmt_tex(r_p)}\\ \\Omega$.\n"
        f"   Total resistance: $R_{{\\text{{total}}}} = R_s + R_p + r = {r_s} + {_fmt_tex(r_p)} + {_fmt_tex(r_int)} = {_fmt_tex(r_tot)}\\ \\Omega$.\n"
        f"2. $I = \\frac{{\\mathcal{{E}}}}{{R_{{\\text{{total}}}}}} = \\frac{{{emf_val}}}{{{_fmt_tex(r_tot)}}} = {_fmt_tex(i_curr)}\\text{{ A}}$.\n"
        f"3. $V_2 = I R_p = ({_fmt_tex(i_curr)})({_fmt_tex(r_p)}) = {_fmt_tex(v_parallel)}\\text{{ V}}$."
    )
    rubric = [
        {"criterion": f"Calculated R_tot = {_fmt_tex(r_tot)} Ohm", "marks": 1},
        {"criterion": f"Calculated current I = {_fmt_tex(i_curr)} A", "marks": 1},
        {"criterion": f"Calculated V2 = {_fmt_tex(v_parallel)} V", "marks": 1},
    ]
    hints = {
        "tier_1": "Rp = (R1 * R2) / (R1 + R2). V2 is the potential difference across Rp.",
        "tier_2": f"Rp = {_fmt(r_p)} Ohm. Total current I = {emf_val} / {_fmt(r_tot)}. V2 = I * Rp.",
        "tier_3": ans,
    }
    return _make_q(r, "43_voltmeter_reading_across_parallel_resistor_branches", 43, prompt, ans, sol, 3, ["calculated_parallel_voltage_without_subtracting_series_drop"], rubric, hints)


def build_44_ammeter_branch_current_and_main_current_division(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])
    r_int = 1.0
    r_p1 = r.choice([6, 10, 15])
    r_p2 = r.choice([6, 10, 15])
    r_p = round((r_p1 * r_p2) / (r_p1 + r_p2), 2)
    i_tot = round(emf_val / (r_p + r_int), 2)
    i1 = round(i_tot * (r_p2 / (r_p1 + r_p2)), 2)
    i2 = round(i_tot - i1, 2)

    prompt = (
        f"A battery with an emf of ${emf_val}\\text{{ V}}$ and internal resistance $r = 1{{,}}0\\ \\Omega$ supplies current to two parallel resistors "
        f"$R_1 = {r_p1}\\ \\Omega$ and $R_2 = {r_p2}\\ \\Omega$. An ammeter $A_1$ is connected in the branch of resistor $R_1$.\n\n"
        f"1. Calculate the total current ($I_{{\\text{{total}}}}$) leaving the battery.\n"
        f"2. Use the current divider principle to calculate the current ($I_1$) measured by ammeter $A_1$."
    )
    ans = f"I_tot = {_fmt_tex(i_tot)} A; I1 = {_fmt_tex(i1)} A"
    sol = (
        f"1. $R_p = \\frac{{{r_p1} \\times {r_p2}}}{{{r_p1} + {r_p2}}} = {_fmt_tex(r_p)}\\ \\Omega$.\n"
        f"   $I_{{\\text{{total}}}} = \\frac{{\\mathcal{{E}}}}{{R_p + r}} = \\frac{{{emf_val}}}{{{_fmt_tex(r_p)} + 1{{,}}0}} = {_fmt_tex(i_tot)}\\text{{ A}}$.\n"
        f"2. By current division: $I_1 = I_{{\\text{{total}}}} \\times \\frac{{R_2}}{{R_1 + R_2}} = {_fmt_tex(i_tot)} \\times \\frac{{{r_p2}}}{{{r_p1 + r_p2}}} = {_fmt_tex(i1)}\\text{{ A}}$."
    )
    rubric = [
        {"criterion": f"Calculated total current I_tot = {_fmt_tex(i_tot)} A", "marks": 1},
        {"criterion": "Applied current divider formula or V_p / R1", "marks": 1},
        {"criterion": f"Calculated branch current I1 = {_fmt_tex(i1)} A", "marks": 1},
    ]
    hints = {
        "tier_1": "Find total current first. Branch current I1 = I_tot * (R2 / (R1 + R2)).",
        "tier_2": f"I_total = {_fmt(i_tot)} A. I1 = {_fmt(i_tot)} * ({r_p2} / {r_p1 + r_p2}).",
        "tier_3": ans,
    }
    return _make_q(r, "44_ammeter_branch_current_and_main_current_division", 44, prompt, ans, sol, 3, ["inverted_current_divider_resistor_ratio"], rubric, hints)


def build_45_power_dissipation_across_internal_resistance_versus_external_load(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])
    r_ext = r.choice([4, 6, 8, 10])
    r_int = round(r.choice([1.0, 1.5, 2.0]), 1)
    i_curr = round(emf_val / (r_ext + r_int), 2)
    p_load = round((i_curr ** 2) * r_ext, 2)
    p_lost = round((i_curr ** 2) * r_int, 2)
    p_total = round(emf_val * i_curr, 2)
    efficiency = round((p_load / p_total) * 100.0, 1)

    prompt = (
        f"A battery with an emf of ${emf_val}\\text{{ V}}$ and internal resistance of ${r_int}\\ \\Omega$ is connected to an external load resistor of resistance ${r_ext}\\ \\Omega$.\n\n"
        f"1. Calculate the rate of electrical energy delivered to the external load ($P_{{\\text{{load}}}}$).\n"
        f"2. Calculate the rate of energy wasted as internal heat inside the battery ($P_{{\\text{{lost}}}}$).\n"
        f"3. Calculate the total power produced by chemical conversion inside the battery ($P_{{\\text{{total}}}}$).\n"
        f"4. Calculate the percentage electrical efficiency ($\\eta$) of this battery circuit."
    )
    ans = f"P_load = {_fmt_tex(p_load)} W; P_lost = {_fmt_tex(p_lost)} W; P_total = {_fmt_tex(p_total)} W; efficiency = {_fmt_tex(efficiency)} %"
    sol = (
        f"1. Current: $I = \\frac{{\\mathcal{{E}}}}{{R_{{\\text{{ext}}}} + r}} = \\frac{{{emf_val}}}{{{r_ext} + {_fmt_tex(r_int)}}} = {_fmt_tex(i_curr)}\\text{{ A}}$.\n"
        f"   $P_{{\\text{{load}}}} = I^2 R_{{\\text{{ext}}}} = ({_fmt_tex(i_curr)})^2 ({r_ext}) = {_fmt_tex(p_load)}\\text{{ W}}$.\n"
        f"2. $P_{{\\text{{lost}}}} = I^2 r = ({_fmt_tex(i_curr)})^2 ({_fmt_tex(r_int)}) = {_fmt_tex(p_lost)}\\text{{ W}}$.\n"
        f"3. $P_{{\\text{{total}}}} = \\mathcal{{E}} I = ({emf_val})({_fmt_tex(i_curr)}) = {_fmt_tex(p_total)}\\text{{ W}}$\n"
        f"   (or $P_{{\\text{{load}}}} + P_{{\\text{{lost}}}} = {_fmt_tex(p_load)} + {_fmt_tex(p_lost)} = {_fmt_tex(p_total)}\\text{{ W}}$).\n"
        f"4. $\\eta = \\frac{{P_{{\\text{{load}}}}}}{{P_{{\\text{{total}}}}}} \\times 100\\% = \\frac{{{_fmt_tex(p_load)}}}{{{_fmt_tex(p_total)}}} \\times 100\\% = {_fmt_tex(efficiency)}\\%$"
        f"   (or $\\frac{{R_{{\\text{{ext}}}}}}{{R_{{\\text{{ext}}}} + r}} \\times 100\\%$)."
    )
    rubric = [
        {"criterion": f"Calculated P_load = {_fmt_tex(p_load)} W", "marks": 1},
        {"criterion": f"Calculated P_lost = {_fmt_tex(p_lost)} W", "marks": 1},
        {"criterion": f"Calculated P_total = {_fmt_tex(p_total)} W", "marks": 1},
        {"criterion": f"Calculated efficiency = {_fmt_tex(efficiency)} %", "marks": 1},
    ]
    hints = {
        "tier_1": "P_load = I^2 * R_ext, P_lost = I^2 * r, P_total = emf * I, efficiency = P_load / P_total * 100.",
        "tier_2": f"I = {_fmt(i_curr)} A. P_load = {_fmt(p_load)} W, P_lost = {_fmt(p_lost)} W.",
        "tier_3": ans,
    }
    return _make_q(r, "45_power_dissipation_across_internal_resistance_versus_external_load", 45, prompt, ans, sol, 4, ["assumed_efficiency_is_always_100_percent"], rubric, hints)


# ============================================================================ #
# SUBSKILLS 46–48: CIRCUIT DYNAMICS & REAL-WORLD DIAGNOSTICS
# ============================================================================ #

def build_46_circuit_dynamics_closing_switch_in_parallel_branch(r: random.Random) -> Dict[str, Any]:
    emf_val = r.choice([12, 18, 24])

    prompt = (
        f"A circuit contains a battery of electromotive force $\\mathcal{{E}} = {emf_val}\\text{{ V}}$ and non-zero internal resistance $r$.\n"
        f"The external circuit contains a resistor $R_1$ connected in series with a parallel branch containing resistor $R_2$ and an open switch $S$.\n"
        f"A voltmeter $V_1$ is connected across the battery terminals, and an ammeter $A$ measures total circuit current.\n\n"
        f"Switch $S$ is now CLOSED.\n"
        f"State and explain the effect of CLOSING the switch on:\n"
        f"1. The total external resistance of the circuit (INCREASES / DECREASES / REMAINS THE SAME).\n"
        f"2. The reading on ammeter $A$ (INCREASES / DECREASES / REMAINS THE SAME).\n"
        f"3. The 'lost volts' across internal resistance $r$ (INCREASES / DECREASES / REMAINS THE SAME).\n"
        f"4. The reading on voltmeter $V_1$ across the battery terminals (INCREASES / DECREASES / REMAINS THE SAME)."
    )
    ans = "1. Decreases; 2. Increases; 3. Increases; 4. Decreases"
    sol = (
        f"1. **Total external resistance DECREASES**: Adding an extra parallel branch ($R_2$) provides an alternate pathway for charge flow, reducing effective parallel resistance.\n"
        f"2. **Ammeter reading INCREASES**: Since total resistance ($R_{{\\text{{ext}}}} + r$) decreases while emf remains constant, total current $I = \\frac{{\\mathcal{{E}}}}{{R_{{\\text{{ext}}}} + r}}$ increases.\n"
        f"3. **Lost volts INCREASES**: $V_{{\\text{{lost}}}} = I r$. Since current $I$ increased and $r$ is constant, $V_{{\\text{{lost}}}}$ increases.\n"
        f"4. **Voltmeter reading DECREASES**: The terminal potential difference $V_1 = \\mathcal{{E}} - I r$. Because lost volts ($I r$) increased, $V_1$ decreases."
    )
    rubric = [
        {"criterion": "Identified total external resistance decreases", "marks": 1},
        {"criterion": "Identified total current increases due to lower resistance", "marks": 1},
        {"criterion": "Identified lost volts Ir increases with higher current", "marks": 1},
        {"criterion": "Concluded terminal pd V1 = emf - Ir decreases", "marks": 1},
    ]
    hints = {
        "tier_1": "Adding parallel branches reduces total resistance. More current causes greater lost volts.",
        "tier_2": "R_ext drops -> I rises -> Ir rises -> V_term = emf - Ir drops.",
        "tier_3": ans,
    }
    return _make_q(r, "46_circuit_dynamics_closing_switch_in_parallel_branch", 46, prompt, ans, sol, 4, ["thought_voltmeter_across_battery_is_independent_of_current"], rubric, hints)


def build_47_circuit_dynamics_opening_switch_effect_on_bulb_brightness(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Three identical incandescent light bulbs ($X$, $Y$, and $Z$) are connected to a real battery with internal resistance $r$.\n"
        f"- Bulb $X$ is connected in series with the battery.\n"
        f"- Bulbs $Y$ and $Z$ are connected in parallel with each other.\n"
        f"- A switch $S$ is placed in series with bulb $Z$ only.\n\n"
        f"Initially switch $S$ is closed and all three bulbs are lit. Switch $S$ is now OPENED.\n\n"
        f"1. What happens to the brightness of bulb $Z$? (EXTINGUISHED / DIMMER / BRIGHTER / UNCHANGED)\n"
        f"2. What happens to the brightness of bulb $X$? Explain your answer step-by-step.\n"
        f"3. What happens to the brightness of bulb $Y$? Explain your answer step-by-step."
    )
    ans = "1. Extinguished; 2. Dimmer (decreased total current); 3. Brighter (increased voltage across Y)"
    sol = (
        f"1. **Bulb $Z$ is EXTINGUISHED** because the open switch breaks the complete conductive loop through bulb $Z$.\n"
        f"2. **Bulb $X$ becomes DIMMER**:\n"
        f"   - Opening switch $S$ removes bulb $Z$ from parallel, increasing parallel resistance from $\\frac{{R}}{{2}}$ to $R$.\n"
        f"   - Total circuit resistance increases, so total current $I$ decreases.\n"
        f"   - Brightness depends on power dissipated: $P_X = I^2 R_X$. Since current $I$ through bulb $X$ decreases, bulb $X$ dims.\n"
        f"3. **Bulb $Y$ becomes BRIGHTER**:\n"
        f"   - Since total current $I$ decreases, the voltage drop across internal resistance ($Ir$) and bulb $X$ ($I R_X$) both decrease.\n"
        f"   - The voltage across bulb $Y$ is $V_Y = \\mathcal{{E}} - I(r + R_X)$. Since $I$ decreased, $V_Y$ increases.\n"
        f"   - Power in bulb $Y$ is $P_Y = \\frac{{V_Y^2}}{{R_Y}}$, so bulb $Y$ glows brighter."
    )
    rubric = [
        {"criterion": "Stated bulb Z goes off / extinguished", "marks": 1},
        {"criterion": "Explained bulb X dims due to decreased total current (P = I^2 * R)", "marks": 1},
        {"criterion": "Explained bulb Y brightens due to increased voltage share V_Y = emf - I(r + R_X)", "marks": 1},
    ]
    hints = {
        "tier_1": "Opening switch increases total resistance, reducing total current. Bulb X gets less current.",
        "tier_2": "Because bulb X and r take less voltage drop, bulb Y receives a larger share of the terminal voltage.",
        "tier_3": ans,
    }
    return _make_q(r, "47_circuit_dynamics_opening_switch_effect_on_bulb_brightness", 47, prompt, ans, sol, 3, ["assumed_all_bulbs_dim_equally"], rubric, hints)


def build_48_internal_resistance_battery_aging_and_flat_battery_syndrome(r: random.Random) -> Dict[str, Any]:
    emf_val = 12
    r_old = round(r.choice([1.8, 2.2, 2.5, 3.0]), 1)
    i_starter = round(r.choice([60, 80, 100]))

    prompt = (
        f"A motorist encounters a car starting problem with an aging 12 V automotive battery:\n"
        f"- When a high-resistance digital voltmeter is connected across the battery terminals with the ignition off, the meter reads exactly **${emf_val}\\text{{ V}}$**.\n"
        f"- However, when the motorist turns the ignition key to engage the starter motor, the dashboard lights go dark and the starter motor fails to crank.\n"
        f"- An automotive technician measures the internal resistance of this aged battery as $r = {r_old}\\ \\Omega$.\n\n"
        f"1. Explain why the voltmeter reads the full ${emf_val}\\text{{ V}}$ when the ignition is switched off.\n"
        f"2. A starter motor requires a current of ${i_starter}\\text{{ A}}$ to crank the engine. Calculate the 'lost volts' that would occur if ${i_starter}\\text{{ A}}$ flowed.\n"
        f"3. Explain why the battery fails completely under load despite showing a 'healthy' ${emf_val}\\text{{ V}}$ on the voltmeter."
    )
    v_lost = round(i_starter * r_old, 1)
    ans = f"V_lost = {_fmt_tex(v_lost)} V; high internal resistance causes terminal pd to collapse to near zero under heavy load"
    sol = (
        f"1. A digital voltmeter has extremely high internal resistance (megaohms). The current drawn is negligible ($I \\approx 0$), "
        f"so the lost volts $V_{{\\text{{lost}}}} = Ir \\approx 0$. Therefore, the voltmeter measures the open-circuit electromotive force (emf) of ${emf_val}\\text{{ V}}$.\n"
        f"2. $V_{{\\text{{lost}}}} = I r = ({i_starter})({_fmt_tex(r_old)}) = {_fmt_tex(v_lost)}\\text{{ V}}$.\n"
        f"3. The calculated lost volts (${_fmt_tex(v_lost)}\\text{{ V}}$) exceeds the total emf of the battery (${emf_val}\\text{{ V}}$). "
        f"In reality, the terminal potential difference collapses to near zero volts ($V_{{\\text{{term}}}} = \\frac{{\\mathcal{{E}} R_{{\\text{{starter}}}}}}{{R_{{\\text{{starter}}}} + r}} \\approx 0\\text{{ V}}$), "
        f"meaning virtually all chemical energy is wasted heating the internal electrolyte and insufficient voltage is available to drive the starter motor."
    )
    rubric = [
        {"criterion": "Explained voltmeter draws near-zero current so Ir = 0 and V = emf", "marks": 1},
        {"criterion": f"Calculated theoretical lost volts V_lost = {_fmt_tex(v_lost)} V", "marks": 1},
        {"criterion": "Explained terminal voltage collapses under high current load due to elevated internal resistance", "marks": 1},
    ]
    hints = {
        "tier_1": "A voltmeter draws no current, so it reads emf. Under heavy starter load, lost volts Ir is huge.",
        "tier_2": f"V_lost = {i_starter} * {_fmt(r_old)} = {_fmt(v_lost)} V, which collapses terminal pd.",
        "tier_3": ans,
    }
    return _make_q(r, "48_internal_resistance_battery_aging_and_flat_battery_syndrome", 48, prompt, ans, sol, 3, ["assumed_battery_with_normal_emf_is_always_functional"], rubric, hints)


# ============================================================================ #
# SUBSKILLS 49–50: CAPSTONE SYNTHESIS & DIAGNOSTIC AUTOPSY
# ============================================================================ #

def build_49_capstone_generator_transmission_line_internal_resistance_synthesis(r: random.Random) -> Dict[str, Any]:
    p_gen_mw = r.choice([10, 20, 25, 50])
    p_gen_w = p_gen_mw * 1000000
    v_trans_kv = r.choice([132, 275, 400])
    v_trans_v = v_trans_kv * 1000
    r_line = r.choice([8, 12, 16, 20])

    i_line = round(p_gen_w / v_trans_v, 2)
    p_lost_w = round((i_line ** 2) * r_line, 1)
    p_lost_kw = round(p_lost_w / 1000.0, 2)
    pct_lost = round((p_lost_w / p_gen_w) * 100.0, 3)

    prompt = (
        f"An AC power station generates an average power of ${p_gen_mw}\\text{{ MW}}$ ($1\\text{{ MW}} = 10^6\\text{{ W}}$). "
        f"A step-up transformer steps up the voltage to ${v_trans_kv}\\text{{ kV}}$ for long-distance transmission over power lines having a "
        f"total loop resistance of ${r_line}\\ \\Omega$.\n\n"
        f"1. Calculate the rms current ($I_{{\\text{{rms}}}}$) in the transmission cables.\n"
        f"2. Calculate the rate of power loss ($P_{{\\text{{loss}}}}$) as thermal dissipation in the transmission cables in kilowatts (kW).\n"
        f"3. Calculate the percentage of generated electrical power lost during transmission.\n"
        f"4. Explain why electrical power is transmitted at extremely high voltages over national grids."
    )
    ans = f"I_rms = {_fmt_tex(i_line)} A; P_lost = {_fmt_tex(p_lost_kw)} kW; pct_lost = {_fmt_tex(pct_lost)} %"
    sol = (
        f"1. $I_{{\\text{{rms}}}} = \\frac{{P_{{\\text{{ave}}}}}}{{V_{{\\text{{rms}}}}}} = \\frac{{{p_gen_w}}}{{{v_trans_v}}} = {_fmt_tex(i_line)}\\text{{ A}}$.\n"
        f"2. $P_{{\\text{{loss}}}} = I_{{\\text{{rms}}}}^2 R_{{\\text{{line}}}} = ({_fmt_tex(i_line)})^2 ({r_line}) = {_fmt_tex(p_lost_w)}\\text{{ W}} = {_fmt_tex(p_lost_kw)}\\text{{ kW}}$.\n"
        f"3. $\\%\\text{{ loss}} = \\frac{{P_{{\\text{{loss}}}}}}{{P_{{\\text{{gen}}}}}} \\times 100\\% = \\frac{{{_fmt_tex(p_lost_w)}}}{{{p_gen_w}}} \\times 100\\% = {_fmt_tex(pct_lost)}\\%$.\n"
        f"4. Transmitting at extremely high voltage dramatically reduces transmission current ($I = P / V$). "
        f"Since thermal line loss is proportional to the square of current ($P_{{\\text{{loss}}}} = I^2 R$), a tenfold increase in voltage reduces power loss by a factor of 100."
    )
    rubric = [
        {"criterion": f"Calculated transmission current I_rms = {_fmt_tex(i_line)} A", "marks": 1},
        {"criterion": f"Calculated thermal line loss = {_fmt_tex(p_lost_kw)} kW", "marks": 1},
        {"criterion": f"Calculated percentage loss = {_fmt_tex(pct_lost)} %", "marks": 1},
        {"criterion": "Explained high voltage minimizes current and thus minimizes I^2*R thermal dissipation", "marks": 1},
    ]
    hints = {
        "tier_1": "I = P / V. Power lost = I^2 * R_line. Percentage = (P_loss / P_gen) * 100.",
        "tier_2": f"I = {p_gen_w} / {v_trans_v} = {_fmt(i_line)} A. P_loss = ({_fmt(i_line)})^2 * {r_line} W.",
        "tier_3": ans,
    }
    return _make_q(r, "49_capstone_generator_transmission_line_internal_resistance_synthesis", 49, prompt, ans, sol, 4, ["used_v_squared_over_r_with_transmission_voltage"], rubric, hints)


def build_50_electrodynamics_and_circuits_diagnostic_autopsy_and_misconception_repair(r: random.Random) -> Dict[str, Any]:
    v_max = r.choice([311, 325, 340])
    v_rms = round(v_max / math.sqrt(2), 1)
    r_element = r.choice([25, 30, 40])
    p_true = round((v_rms ** 2) / r_element, 1)
    p_false = round((v_max ** 2) / r_element, 1)

    prompt = (
        f"A senior Physical Sciences examiner identifies three common misconceptions in candidate exam scripts:\n\n"
        f"**Candidate Error A (AC Theory)**:\n"
        f"A candidate is asked to calculate the power dissipated by a heating resistor of resistance ${r_element}\\ \\Omega$ connected to an AC supply with "
        f"peak voltage $V_{{\\text{{max}}}} = {v_max}\\text{{ V}}$. The candidate writes:\n"
        f"$$P = \\frac{{V_{{\\text{{max}}}}^2}}{{R}} = \\frac{{{v_max}^2}}{{{r_element}}} = {_fmt_tex(p_false)}\\text{{ W}}$$\n"
        f"1. Explain the conceptual error in Candidate Error A and calculate the correct average power ($P_{{\\text{{ave}}}}$).\n\n"
        f"**Candidate Error B (Electrical Machines)**:\n"
        f"A candidate states: *'An AC alternator uses a split-ring commutator to ensure the current in the external circuit flows in alternating directions.'*\n"
        f"2. Identify the scientific mistake in Candidate Error B and state the correct component and its function in an AC alternator.\n\n"
        f"**Candidate Error C (Electric Circuits)**:\n"
        f"A candidate states: *'A 9 V battery always maintains a potential difference of 9 V across its terminals regardless of what components are connected to it.'*\n"
        f"3. Explain why statement C is scientifically false for any real chemical battery."
    )
    ans = f"P_true = {_fmt_tex(p_true)} W; AC alternators use slip rings, not split rings; real batteries have internal resistance so terminal pd drops under load"
    sol = (
        f"1. **Conceptual Repair for Error A**:\n"
        f"   Electrical power ratings for alternating current must use root-mean-square (rms) values, not peak values, because rms represents the effective DC equivalent heating effect.\n"
        f"   $V_{{\\text{{rms}}}} = \\frac{{V_{{\\text{{max}}}}}}{{\\sqrt{{2}}}} = \\frac{{{v_max}}}{{\\sqrt{{2}}}} = {_fmt_tex(v_rms)}\\text{{ V}}$.\n"
        f"   Correct average power: $P_{{\\text{{ave}}}} = \\frac{{V_{{\\text{{rms}}}}^2}}{{R}} = \\frac{{{_fmt_tex(v_rms)}^2}}{{{r_element}}} = {_fmt_tex(p_true)}\\text{{ W}}$ "
        f"   (which is exactly half of the candidate's erroneous value of {_fmt_tex(p_false)} W).\n\n"
        f"2. **Scientific Repair for Error B**:\n"
        f"   An AC alternator uses two continuous **slip rings** with carbon brushes, NOT a split-ring commutator. "
        f"   The slip rings maintain a continuous connection with the rotating coil, allowing the naturally induced alternating emf to pass unchanged into the external circuit. "
        f"   (A split-ring commutator is used in DC machines to reverse coil connections every half-turn).\n\n"
        f"3. **Scientific Repair for Error C**:\n"
        f"   Statement C is false because all real chemical batteries possess internal resistance ($r$). "
        f"   When current ($I$) flows to power external components, an internal potential drop ('lost volts' $V_{{\\text{{lost}}}} = Ir$) occurs inside the electrolyte. "
        f"   The terminal potential difference is $V_{{\\text{{terminal}}}} = \\mathcal{{E}} - Ir = 9 - Ir$, which decreases as the load draws more current."
    )
    rubric = [
        {"criterion": f"Identified must use V_rms and calculated P_ave = {_fmt_tex(p_true)} W", "marks": 2},
        {"criterion": "Identified alternator uses slip rings to maintain AC connection, not split rings", "marks": 2},
        {"criterion": "Explained real batteries have internal resistance causing terminal pd V = emf - Ir to drop under load", "marks": 2},
    ]
    hints = {
        "tier_1": "Error A: P_ave uses V_rms, not V_max. Error B: AC uses slip rings. Error C: Real batteries have internal resistance.",
        "tier_2": f"V_rms = {v_max} / sqrt(2) = {_fmt(v_rms)} V. P_ave = ({_fmt(v_rms)}^2) / {r_element} = {_fmt(p_true)} W.",
        "tier_3": ans,
    }
    return _make_q(r, "50_electrodynamics_and_circuits_diagnostic_autopsy_and_misconception_repair", 50, prompt, ans, sol, 6, ["used_peak_voltage_in_power_formula", "confused_slip_rings_and_split_ring_commutator", "assumed_battery_terminal_pd_is_invariant"], rubric, hints)


# ============================================================================ #
# BUILDERS EXPORT DICTIONARY 26–50
# ============================================================================ #
BUILDERS_26_50: Dict[str, Any] = {
    "26_ac_average_power_from_vrms_and_irms": build_26_ac_average_power_from_vrms_and_irms,
    "27_ac_power_dissipation_in_heating_resistor": build_27_ac_power_dissipation_in_heating_resistor,
    "28_ac_power_dissipation_from_voltage_and_resistance": build_28_ac_power_dissipation_from_voltage_and_resistance,
    "29_ac_peak_power_versus_average_power": build_29_ac_peak_power_versus_average_power,
    "30_domestic_ac_appliance_energy_consumption_and_cost": build_30_domestic_ac_appliance_energy_consumption_and_cost,
    "31_electromotive_force_emf_definition_and_measurement": build_31_electromotive_force_emf_definition_and_measurement,
    "32_internal_resistance_and_lost_volts_concept": build_32_internal_resistance_and_lost_volts_concept,
    "33_terminal_potential_difference_calculation": build_33_terminal_potential_difference_calculation,
    "34_calculate_internal_resistance_given_emf_current_rload": build_34_calculate_internal_resistance_given_emf_current_rload,
    "35_calculate_emf_given_load_resistance_and_two_currents": build_35_calculate_emf_given_load_resistance_and_two_currents,
    "36_maximum_current_from_short_circuited_battery": build_36_maximum_current_from_short_circuited_battery,
    "37_graphical_analysis_terminal_voltage_vs_current_intercept_and_slope": build_37_graphical_analysis_terminal_voltage_vs_current_intercept_and_slope,
    "38_graphical_determination_of_internal_resistance_from_experimental_data": build_38_graphical_determination_of_internal_resistance_from_experimental_data,
    "39_series_resistor_circuit_with_internal_resistance": build_39_series_resistor_circuit_with_internal_resistance,
    "40_parallel_resistor_circuit_with_internal_resistance": build_40_parallel_resistor_circuit_with_internal_resistance,
    "41_series_parallel_combination_circuit_with_internal_resistance": build_41_series_parallel_combination_circuit_with_internal_resistance,
    "42_voltmeter_reading_across_battery_open_vs_closed_switch": build_42_voltmeter_reading_across_battery_open_vs_closed_switch,
    "43_voltmeter_reading_across_parallel_resistor_branches": build_43_voltmeter_reading_across_parallel_resistor_branches,
    "44_ammeter_branch_current_and_main_current_division": build_44_ammeter_branch_current_and_main_current_division,
    "45_power_dissipation_across_internal_resistance_versus_external_load": build_45_power_dissipation_across_internal_resistance_versus_external_load,
    "46_circuit_dynamics_closing_switch_in_parallel_branch": build_46_circuit_dynamics_closing_switch_in_parallel_branch,
    "47_circuit_dynamics_opening_switch_effect_on_bulb_brightness": build_47_circuit_dynamics_opening_switch_effect_on_bulb_brightness,
    "48_internal_resistance_battery_aging_and_flat_battery_syndrome": build_48_internal_resistance_battery_aging_and_flat_battery_syndrome,
    "49_capstone_generator_transmission_line_internal_resistance_synthesis": build_49_capstone_generator_transmission_line_internal_resistance_synthesis,
    "50_electrodynamics_and_circuits_diagnostic_autopsy_and_misconception_repair": build_50_electrodynamics_and_circuits_diagnostic_autopsy_and_misconception_repair,
}
