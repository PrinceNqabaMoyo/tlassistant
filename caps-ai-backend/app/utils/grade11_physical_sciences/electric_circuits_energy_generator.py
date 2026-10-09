"""Grade 11 Physical Sciences — Electric Circuits & Electrical Energy Generator.
Deterministic 6-pillar CAPS question generator covering Paper 1 (Physics Term 3):
- Ohm's Law: Resistance, potential difference, and current relationships.
- Ohmic vs non-ohmic conductors (resistors at constant temp vs incandescent bulbs).
- Series-parallel resistor network analysis: equivalent resistance, potential dividers, branch currents.
- Electrical energy and power: W = V * I * t = I^2 * R * t = (V^2 / R) * t; P = V * I = I^2 * R = V^2 / R.
- Cost of electrical energy: Cost = Power (in kW) x time (in hours) x tariff (in Rands/kWh).

Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

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


def _build_network_drill(r: random.Random) -> Dict[str, Any]:
    # Select clean numbers for series + parallel combination
    r1 = r.choice([4, 6, 8, 12])
    r2 = r.choice([4, 6, 12])
    # Rp = (r1 * r2) / (r1 + r2)
    rp = (r1 * r2) / (r1 + r2)
    while not rp.is_integer():
        r1 = r.choice([6, 12, 10, 20])
        r2 = r.choice([6, 12, 10, 20])
        rp = (r1 * r2) / (r1 + r2)

    rp = int(rp)
    rs = r.choice([2, 3, 4, 5])
    r_tot = rs + rp

    total_current = r.choice([1.5, 2.0, 2.5, 3.0])
    v_total = round(total_current * r_tot, 1)
    v_series = round(total_current * rs, 1)
    v_parallel = round(total_current * rp, 1)

    i_branch1 = round(v_parallel / r1, 2)
    i_branch2 = round(v_parallel / r2, 2)

    power_rs = round((total_current**2) * rs, 2)

    prompt = (
        f"In the circuit diagram represented below, a battery of negligible internal resistance supplies "
        f"a total potential difference of **${_fmt_sa(v_total)}\\text{{ V}}$**.\n"
        f"A resistor of resistance **$R_s = {rs}\\ \\Omega$** is connected in series with a parallel combination "
        f"consisting of two resistors **$R_1 = {r1}\\ \\Omega$** and **$R_2 = {r2}\\ \\Omega$**.\n\n"
        f"1. Calculate the equivalent resistance ($R_p$) of the parallel combination.\n"
        f"2. Calculate the total equivalent resistance ($R_{{\\text{{tot}}}}$) of the circuit.\n"
        f"3. Calculate the total current ($I_{{\\text{{tot}}}}$) flowing through the circuit (reading on an ammeter in the main branch).\n"
        f"4. Calculate the potential difference ($V_p$) across the parallel combination.\n"
        f"5. Calculate the current ($I_1$) flowing through resistor $R_1$."
    )

    sol = (
        f"1. $\\frac{{1}}{{R_p}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_2}} = \\frac{{1}}{{{r1}}} + \\frac{{1}}{{{r2}}}$\n"
        f"   $R_p = \\frac{{{r1} \\times {r2}}}{{{r1} + {r2}}} = \\frac{{{r1 * r2}}}{{{r1 + r2}}} = {rp}\\ \\Omega$\n\n"
        f"2. $R_{{\\text{{tot}}}} = R_s + R_p = {rs} + {rp} = {r_tot}\\ \\Omega$\n\n"
        f"3. $I_{{\\text{{tot}}}} = \\frac{{V_{{\\text{{total}}}}}}{{R_{{\\text{{tot}}}}}} = \\frac{{{_fmt_sa(v_total)}}}{{{r_tot}}} = {_fmt_sa(total_current)}\\text{{ A}}$\n\n"
        f"4. $V_p = I_{{\\text{{tot}}}} \\times R_p = {_fmt_sa(total_current)} \\times {rp} = {_fmt_sa(v_parallel)}\\text{{ V}}$\n\n"
        f"5. $I_1 = \\frac{{V_p}}{{R_1}} = \\frac{{{_fmt_sa(v_parallel)}}}{{{r1}}} = {_fmt_sa(i_branch1)}\\text{{ A}}$"
    )

    return {
        "id": f"g11_ps_circ_net_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Rp={rp} Ohm, Rtot={r_tot} Ohm, Itot={_fmt_sa(total_current)} A, Vp={_fmt_sa(v_parallel)} V",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp1", "desc": "Formula: 1/Rp = 1/R1 + 1/R2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculate Rp = {rp} Ohm", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate Rtot = {r_tot} Ohm", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculate Itot = {_fmt_sa(total_current)} A", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculate Vp = {_fmt_sa(v_parallel)} V", "marks": 1, "editable": True},
                {"id": "mp6", "desc": "Formula: I1 = Vp / R1", "marks": 1, "editable": True},
                {"id": "mp7", "desc": f"Calculate I1 = {_fmt_sa(i_branch1)} A", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "inverted_parallel_resistance_formula", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Find the parallel equivalent resistance first using $\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2}$, then add the series resistor.",
            "tier_2": "Ohm's Law applies to the entire circuit ($I = V_{\\text{tot}}/R_{\\text{tot}}$) and to individual parallel branches ($I_1 = V_p/R_1$).",
            "tier_3": f"$R_p = {rp}\\ \\Omega$, $R_{{\\text{{tot}}}} = {r_tot}\\ \\Omega$, $I_{{\\text{{tot}}}} = {_fmt_sa(total_current)}\\text{{ A}}$, $V_p = {_fmt_sa(v_parallel)}\\text{{ V}}$.",
        },
        "misconception_tags": ["inverted_parallel_resistance_formula", "confused_series_and_parallel_currents"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
    }


def _build_power_cost_drill(r: random.Random) -> Dict[str, Any]:
    appliances = [
        {"name": "Electric geyser", "power_w": 3000, "hours_per_day": 3.5},
        {"name": "Electric stove oven", "power_w": 2400, "hours_per_day": 2.0},
        {"name": "Air conditioner", "power_w": 1800, "hours_per_day": 5.0},
        {"name": "Space heater", "power_w": 2000, "hours_per_day": 4.0},
    ]
    app = r.choice(appliances)
    days = 30
    tariff_rands = round(r.choice([2.50, 2.75, 3.10, 3.25]), 2)  # R per kWh

    power_kw = app["power_w"] / 1000.0
    total_hours = app["hours_per_day"] * days
    energy_kwh = round(power_kw * total_hours, 1)
    total_cost = round(energy_kwh * tariff_rands, 2)

    prompt = (
        f"A household uses an **{app['name']}** rated at **${app['power_w']}\\text{{ W}}$** for an average of "
        f"**${_fmt_sa(app['hours_per_day'])}\\text{{ hours per day}}$** over a **{days}-day** calendar month.\n"
        f"The local municipality charges electricity at a tariff of **$\\text{{R}}{_fmt_sa(tariff_rands)}\\text{{ per kWh}}$**.\n\n"
        f"1. Convert the power rating of the appliance to kilowatts ($\\text{{kW}}$).\n"
        f"2. Calculate the total electrical energy consumed by the appliance over {days} days, in kilowatt-hours ($\\text{{kWh}}$).\n"
        f"3. Calculate the total cost of operating this appliance for the month."
    )

    sol = (
        f"1. $\\text{{Power (kW)}} = \\frac{{{app['power_w']}}}{{1000}} = {_fmt_sa(power_kw)}\\text{{ kW}}$\n\n"
        f"2. $\\text{{Total time}} = {_fmt_sa(app['hours_per_day'])} \\times {days} = {_fmt_sa(total_hours)}\\text{{ hours}}$\n"
        f"   $\\text{{Energy (kWh)}} = \\text{{Power (kW)}} \\times \\text{{time (h)}} = {_fmt_sa(power_kw)} \\times {_fmt_sa(total_hours)} = {_fmt_sa(energy_kwh)}\\text{{ kWh}}$\n\n"
        f"3. $\\text{{Cost}} = \\text{{Energy (kWh)}} \\times \\text{{tariff}} = {_fmt_sa(energy_kwh)} \\times \\text{{R}}{_fmt_sa(tariff_rands)} = \\text{{R}}{_fmt_sa(total_cost)}$"
    )

    return {
        "id": f"g11_ps_circ_cost_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"R{_fmt_sa(total_cost)}",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Convert to kW: {app['power_w']} W = {_fmt_sa(power_kw)} kW", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculate total operating hours = {_fmt_sa(total_hours)} h", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate energy = {_fmt_sa(energy_kwh)} kWh", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculate total cost = R{_fmt_sa(total_cost)}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "forgot_converting_watts_to_kw", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "1 kilowatt (kW) = 1000 watts (W). Energy in kWh = Power in kW x Time in hours.",
            "tier_2": f"First find total hours: ${app['hours_per_day']} \\times {days}$. Then multiply by {power_kw}\\text{{ kW}}.",
            "tier_3": f"Energy = {power_kw} x {total_hours} = {_fmt_sa(energy_kwh)} kWh. Cost = {_fmt_sa(energy_kwh)} x R{_fmt_sa(tariff_rands)} = R{_fmt_sa(total_cost)}.",
        },
        "misconception_tags": ["forgot_converting_watts_to_kw", "failed_minutes_to_hours_conversion"],
        "term": 3,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 4,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)
    if mode == "elementary_power_cost":
        return _build_power_cost_drill(r)
    elif mode == "elementary_resistor_network":
        return _build_network_drill(r)
    else:
        choice = r.choice(["network", "cost"])
        if choice == "network":
            return _build_network_drill(r)
        else:
            return _build_power_cost_drill(r)
