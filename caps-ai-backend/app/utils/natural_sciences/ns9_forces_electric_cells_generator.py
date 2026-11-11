"""Natural Sciences Grade 9 Term 3: Electric Cells, Resistance, and Energy Cost Generator.

Covers:
- Quantitative Ohm's law calculations: V = I * R, I = V / R, R = V / I.
- Factors affecting conductor resistance: Length, thickness (cross-sectional area), material type (copper vs nichrome), and temperature.
- Electric cells as energy systems: Cells connected in series (voltage additive) vs parallel (extended battery lifespan).
- Electrical power and energy consumption: E (kWh) = Power (kW) * Time (hours).
- Domestic electricity cost calculations: Cost = Energy (kWh) * Tariff rate (R/kWh).
- Circuit diagram integration via 3-layer anti-leak plate.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences.natural_sciences_builders import build_electric_circuit_ns_question


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_ohms_law_and_energy_cost(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Quantitative Ohm's law, resistance factors, and electricity billing."""
    # Clean procedural numbers for Ohm's law: V = I * R
    r_val = r.choice([3, 4, 5, 6, 8, 10, 12])
    i_val = r.choice([0.5, 1.0, 1.5, 2.0, 2.5])
    v_val = round(i_val * r_val, 1)

    # Appliance energy and tariff
    appliance = r.choice([
        {"name": "electric geyser", "power_w": 3000, "hours": 4},
        {"name": "electric heater", "power_w": 2000, "hours": 5},
        {"name": "kettle", "power_w": 2200, "hours": 1},
        {"name": "microwave oven", "power_w": 1000, "hours": 2},
    ])
    tariff_r_per_kwh = r.choice([2.50, 2.80, 3.00, 3.20])
    power_kw = appliance["power_w"] / 1000
    energy_kwh = power_kw * appliance["hours"]
    cost_rand = round(energy_kwh * tariff_r_per_kwh, 2)

    qid = _make_id("ns9_circuits_quant", seed, idx)

    if mode == "elementary_ohms_law":
        prompt = (
            f"A circuit resistor is connected to a ${_fmt_sa(v_val, 1)}\\text{{ V}}$ potential difference and draws an "
            f"electric current of ${_fmt_sa(i_val, 1)}\\text{{ A}}$.\n\n"
            f"Use Ohm's law ($R = \\frac{{V}}{{I}}$) to calculate the resistance ($R$) of this resistor in Ohms ($\\Omega$)."
        )
        ans_str = f"R = {_fmt_sa(r_val, 1)} Ω"
        memo = (
            f"1. Formula: $R = \\frac{{V}}{{I}}$ [M]\n"
            f"2. Substitution: $R = \\frac{{{v_val}\\text{{ V}}}}{{{i_val}\\text{{ A}}}} = {_fmt_sa(r_val, 1)}\\ \\Omega$ [A]"
        )
        hints = {
            "tier_1": "Apply Ohm's law: Resistance = Voltage / Current.",
            "tier_2": f"Calculate: {v_val} / {i_val} = {r_val} Ω.",
            "tier_3": f"R = {_fmt_sa(r_val, 1)} Ω.",
        }
        marks = 3
        misconceptions = ["ohms_law_formula_inversion", "omitted_omega_units"]
    else:
        # Full compound question: Ohm's law + Resistance factors + Energy cost
        prompt = (
            f"A Grade 9 learner investigates electrical resistance and domestic energy usage.\n\n"
            f"1. A resistor in an experimental circuit has a potential difference of ${_fmt_sa(v_val, 1)}\\text{{ V}}$ across it "
            f"and a current of ${_fmt_sa(i_val, 1)}\\text{{ A}}$ passing through it. Calculate its resistance.\n"
            f"2. State THREE physical factors that determine the electrical resistance of a conducting wire.\n"
            f"3. A {appliance['name']} rated at ${appliance['power_w']}\\text{{ W}}$ is operated for ${appliance['hours']}\\text{{ hours}}$ per day.\n"
            f"   The local municipal electricity tariff is $\\text{{R }}{_fmt_sa(tariff_r_per_kwh, 2)}\\text{{ per kWh}}$.\n"
            f"   Calculate:\n"
            f"   a) The electrical energy consumed by the appliance in kilowatt-hours ($\\text{{kWh}}$).\n"
            f"   b) The cost to operate this appliance for the day (in Rands)."
        )
        ans_str = (
            f"1. R = {_fmt_sa(r_val, 1)} Ω; "
            f"2. Length of wire, thickness / cross-sectional area, material type, temperature; "
            f"3. a) {_fmt_sa(energy_kwh, 1)} kWh; b) R {_fmt_sa(cost_rand, 2)}"
        )
        memo = (
            f"1. Ohm's law calculation [3]:\n"
            f"   $$R = \\frac{{V}}{{I}} = \\frac{{{v_val}\\text{{ V}}}}{{{i_val}\\text{{ A}}}} = {_fmt_sa(r_val, 1)}\\ \\Omega$$ [3]\n"
            f"2. Factors determining resistance (any 3) [3]:\n"
            f"   - **Length**: Longer wires present greater resistance [1].\n"
            f"   - **Thickness (cross-sectional area)**: Thicker wires present lower resistance [1].\n"
            f"   - **Material type**: Copper has low resistance; nichrome has high resistance [1].\n"
            f"   - **Temperature**: Hotter metals have higher resistance [1].\n"
            f"3. Energy consumption and cost [3]:\n"
            f"   a) $$\\text{{Energy (kWh)}} = \\frac{{{appliance['power_w']}\\text{{ W}}}}{{1000}} \\times {appliance['hours']}\\text{{ h}} = {_fmt_sa(power_kw, 1)}\\text{{ kW}} \\times {appliance['hours']}\\text{{ h}} = {_fmt_sa(energy_kwh, 1)}\\text{{ kWh}}$$ [2]\n"
            f"   b) $$\\text{{Cost}} = {_fmt_sa(energy_kwh, 1)}\\text{{ kWh}} \\times \\text{{R }}{_fmt_sa(tariff_r_per_kwh, 2)} = \\text{{R }}{_fmt_sa(cost_rand, 2)}$$ [1]"
        )
        hints = {
            "tier_1": "Ohm's law: R = V / I. Convert Watts to kW by dividing by 1000. Cost = kWh * tariff.",
            "tier_2": f"R = {v_val} / {i_val} = {r_val} Ω. Energy = ({appliance['power_w']}/1000) * {appliance['hours']} = {energy_kwh} kWh. Cost = {energy_kwh} * {tariff_r_per_kwh} = R{cost_rand:.2f}.",
            "tier_3": f"1. {_fmt_sa(r_val, 1)} Ω. 2. Length, thickness, material, temperature. 3. a) {_fmt_sa(energy_kwh, 1)} kWh, b) R {_fmt_sa(cost_rand, 2)}.",
        }
        marks = 9
        misconceptions = ["watts_to_kilowatts_conversion_omitted", "cost_calculation_multiplication_error", "confused_series_parallel_resistance"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "question_text": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Ohm's law calculation with units", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Factors affecting resistance in conductors", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Energy consumption calculation in kWh", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Electricity cost calculation in Rand", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_units", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master entry point for Grade 9 Electric Cells & Resistance."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("circuit_schematic", "meter_measurement"):
            q = build_electric_circuit_ns_question(sub_seed, grade=9, mode=mode)
        elif subskill in ("ohms_law", "energy_cost", "resistance_factors") or mode == "elementary_ohms_law":
            q = _generate_ohms_law_and_energy_cost(sub_r, sub_seed, i, mode)
        else:
            # Alternating between circuit diagram schematic and Ohm's law/energy cost calculations
            if i % 2 == 0:
                q = build_electric_circuit_ns_question(sub_seed, grade=9, mode=mode)
            else:
                q = _generate_ohms_law_and_energy_cost(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
