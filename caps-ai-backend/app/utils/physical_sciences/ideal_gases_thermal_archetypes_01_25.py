"""Grade 11 Physical Sciences — Term 1 Chapter 7: Ideal Gases & Thermal Physics
Archetypes 01–25:
- 01–05: Kinetic Molecular Theory, Microscopic Pressure, Kelvin & Unit Conversions
- 06–12: Boyle's Law (P1*V1 = P2*V2), Calculations, P vs V, P vs 1/V, PV vs P Graphs
- 13–18: Charles's Law (V1/T1 = V2/T2), Calculations, V vs T(K), V vs T(°C) Graphs, Hot Air Balloon
- 19–25: Gay-Lussac's Law (P1/T1 = P2/T2), Calculations, P vs T(K), P vs T(°C) Graphs, Tyre & Pressure Cooker

All 25 builders strictly comply with:
- 6-Pillar Generator Contract
- Procedural determinism via rng: random.Random
- South African comma decimal separator ({,}) in KaTeX
- Valid inline vector SVGs in diagram_spec (never raw in question_text)
- Zero diagram description leaks
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict


def _fmt(val: float | int, decimals: int = 2) -> str:
    """Format numbers with South African comma decimal separator."""
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _svg_wrap(inner: str, width: int = 380, height: int = 240) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;">'
        f"{inner}</svg>"
    )


# ---------------------------------------------------------------------------
# 01–05: Kinetic Molecular Theory & Units
# ---------------------------------------------------------------------------


def build_01_kinetic_molecular_theory_assumptions(rng: random.Random) -> Dict[str, Any]:
    gas = rng.choice(["helium (He)", "neon (Ne)", "argon (Ar)", "nitrogen (N2)"])
    qid = f"ps11_gas_01_{rng.randint(100000, 999999)}"

    prompt = (
        f"The macroscopic behavior of gases such as {gas} is explained by the kinetic molecular theory.\n\n"
        f"1. State TWO fundamental assumptions of the kinetic molecular theory regarding the particles of an ideal gas.\n"
        f"2. Explain what is meant by an 'elastic collision' between gas particles and the container walls."
    )
    ans = (
        "1. Gas particles have negligible volume compared to container volume; there are no intermolecular forces between particles; "
        "particles are in constant, continuous, random straight-line motion; collisions are perfectly elastic. "
        "2. An elastic collision is one in which total kinetic energy is conserved (no kinetic energy is converted to other forms of energy)."
    )
    memo = (
        "1. Any TWO valid assumptions [2]:\n"
        "   - The volume of individual gas particles is negligible compared to the total volume of the container [1].\n"
        "   - There are no intermolecular forces of attraction or repulsion between particles [1].\n"
        "   - Gas particles are in continuous, rapid, random motion in straight lines [1].\n"
        "   - The average kinetic energy of the particles is directly proportional to the absolute temperature in Kelvin [1].\n"
        "2. Elastic collision [2]: A collision in which the total kinetic energy of the system is conserved / no kinetic energy is lost as heat or sound [2]."
    )
    hints = {
        "tier_1": "Think about particle volume, forces between particles, particle motion, and energy conservation during collisions.",
        "tier_2": "In an ideal gas, particles are point masses with zero volume and no attractions. Collisions conserve kinetic energy.",
        "tier_3": "Assumptions: negligible volume, no intermolecular forces, constant random motion. Elastic collision: total kinetic energy is conserved.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "01_kinetic_molecular_theory_assumptions",
        "learning_objective_id": "ps11_kmt_assumptions",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["particle_expansion_misconception", "elastic_collision_inelastic_confusion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "First kinetic theory assumption", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Second kinetic theory assumption", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Definition of elastic collision", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_02_gas_pressure_microscopic_interpretation(rng: random.Random) -> Dict[str, Any]:
    container_vol = rng.choice([2, 5, 10, 20])
    gas = rng.choice(["argon", "krypton", "oxygen", "methane"])
    qid = f"ps11_gas_02_{rng.randint(100000, 999999)}"

    prompt = (
        f"A sample of {gas} gas is sealed inside a rigid container of volume {_fmt(container_vol)}\\text{{ dm}}^3$.\n\n"
        f"1. Define gas pressure in terms of microscopic particle behavior and macroscopic force.\n"
        f"2. Explain, using kinetic molecular theory, why the pressure increases when more gas particles are injected "
        f"into the rigid container at constant temperature."
    )
    ans = (
        "1. Pressure is the perpendicular force exerted per unit surface area of the container walls, caused by the change in momentum "
        "of colliding gas particles ($P = F/A$). 2. Adding more particles increases particle density/concentration, leading to a greater "
        "frequency of collisions against the container walls, thus increasing the total force and pressure."
    )
    memo = (
        "1. Definition [2]: Macroscopically, pressure is the perpendicular force per unit area ($P = \\frac{F}{A}$) [1]. "
        "Microscopically, it is caused by the collisions of gas particles with the container walls, where each collision imparts an impulse (change in momentum) [1].\n"
        "2. Kinetic theory explanation [3]:\n"
        "   - Adding more particles at constant volume increases the number of particles per unit volume (particle density) [1].\n"
        "   - This increases the frequency of collisions of gas particles with the container walls (more collisions per second) [1].\n"
        "   - Consequently, the total force exerted per unit area increases, resulting in higher pressure [1]."
    )
    hints = {
        "tier_1": "Recall: P = F / A. Think about what causes force on the walls.",
        "tier_2": "Gas particles collide with the walls. More particles in the same space mean more frequent collisions.",
        "tier_3": "Pressure is force per unit area from particle collisions. More particles -> higher collision rate -> higher pressure.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "02_gas_pressure_microscopic_interpretation",
        "learning_objective_id": "ps11_microscopic_pressure",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["pressure_force_area_confusion", "collision_frequency_misunderstood"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of pressure P = F/A", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Particle density increase", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Collision frequency increase", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Total force and pressure increase", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_03_temperature_kelvin_conversion(rng: random.Random) -> Dict[str, Any]:
    c_temp = rng.choice([-196, -78, -40, -15, 0, 15, 20, 25, 27, 37, 85, 100, 150, 250])
    k_val = c_temp + 273
    qid = f"ps11_gas_03_{rng.randint(100000, 999999)}"

    prompt = (
        f"In all gas law calculations, temperature must be expressed on the thermodynamic scale in Kelvin ($\\text{{K}}$).\n\n"
        f"1. Convert a temperature of ${c_temp}^\\circ\\text{{C}}$ to Kelvin.\n"
        f"2. State the value of absolute zero in degrees Celsius ($^\\circ\\text{{C}}$) and describe particle motion at this temperature according to kinetic theory."
    )
    ans = f"1. T = {_fmt(k_val)} K; 2. Absolute zero is -273 °C (0 K); all translational kinetic motion of particles ceases."
    memo = (
        f"1. Kelvin conversion [2]:\n"
        f"   $$T(\\text{{K}}) = T(^\\circ\\text{{C}}) + 273 = {c_temp} + 273 = {_fmt(k_val)}\\text{{ K}}$$ [2]\n"
        f"2. Absolute zero [2]: $-273^\\circ\\text{{C}}$ (or $0\\text{{ K}}$) [1]. At this temperature, the kinetic energy of particles reaches its minimum theoretical value where molecular motion ceases [1]."
    )
    hints = {
        "tier_1": "Formula: T(K) = T(°C) + 273.",
        "tier_2": f"Calculate {c_temp} + 273.",
        "tier_3": f"T = {k_val} K. Absolute zero is -273 °C where molecular kinetic motion ceases.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "03_temperature_kelvin_conversion",
        "learning_objective_id": "ps11_kelvin_conversion",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 6,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["forgot_kelvin_conversion", "absolute_zero_sign_confusion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Kelvin conversion formula and answer", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Value of absolute zero", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "State of particle motion at absolute zero", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_04_pressure_units_conversion(rng: random.Random) -> Dict[str, Any]:
    p_kpa = rng.choice([80.0, 95.5, 101.3, 120.0, 150.0, 202.6, 250.0, 303.9])
    p_pa = p_kpa * 1000.0
    p_atm = round(p_kpa / 101.3, 3)
    p_mmhg = round(p_atm * 760.0, 1)
    qid = f"ps11_gas_04_{rng.randint(100000, 999999)}"

    prompt = (
        f"A gas manometer measures a pressure of ${_fmt(p_kpa)}\\text{{ kPa}}$.\n"
        f"(Given: $1\\text{{ atm}} = 101{{,}}3\\text{{ kPa}} = 101\\,300\\text{{ Pa}} = 760\\text{{ mm Hg}}$).\n\n"
        f"1. Convert this pressure to pascals ($\\text{{Pa}}$).\n"
        f"2. Convert this pressure to atmospheres ($\\text{{atm}}$).\n"
        f"3. Convert this pressure to millimetres of mercury ($\\text{{mm Hg}}$)."
    )
    ans = f"1. {_fmt(int(p_pa))} Pa; 2. {_fmt(p_atm)} atm; 3. {_fmt(p_mmhg)} mm Hg"
    memo = (
        f"1. Pascals [1]:\n"
        f"   $$P = {_fmt(p_kpa)} \\times 10^3 = {_fmt(int(p_pa))}\\text{{ Pa}}$$ [1]\n"
        f"2. Atmospheres [1]:\n"
        f"   $$P = \\frac{{{_fmt(p_kpa)}}}{{101{{,}}3}} = {_fmt(p_atm)}\\text{{ atm}}$$ [1]\n"
        f"3. mm Hg [1]:\n"
        f"   $$P = {_fmt(p_atm)} \\times 760 = {_fmt(p_mmhg)}\\text{{ mm Hg}}$$ [1]"
    )
    hints = {
        "tier_1": "1 kPa = 1000 Pa. 1 atm = 101,3 kPa = 760 mm Hg.",
        "tier_2": "Multiply kPa by 1000 for Pa. Divide kPa by 101,3 for atm.",
        "tier_3": f"Pa = {p_pa}. atm = {p_atm}. mm Hg = {p_mmhg}.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "04_pressure_units_conversion",
        "learning_objective_id": "ps11_pressure_units",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 6,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["pressure_kpa_pa_unit_error", "atm_kpa_conversion_confusion"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Pascals conversion", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Atmospheres conversion", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "mm Hg conversion", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_05_volume_units_conversion(rng: random.Random) -> Dict[str, Any]:
    v_cm3 = rng.choice([250, 500, 750, 1200, 2500, 5000, 15000])
    v_dm3 = v_cm3 / 1000.0
    v_m3 = v_cm3 / 1_000_000.0
    qid = f"ps11_gas_05_{rng.randint(100000, 999999)}"

    prompt = (
        f"In gas law calculations, volume must frequently be converted between laboratory units and the SI unit ($\\text{{m}}^3$).\n\n"
        f"A gas syringe holds a volume of ${v_cm3}\\text{{ cm}}^3$.\n"
        f"1. Convert this volume to cubic decimetres ($\\text{{dm}}^3$).\n"
        f"2. Convert this volume to cubic metres ($\\text{{m}}^3$).\n"
        f"3. State the relationship between $1\\text{{ dm}}^3$ and $1\\text{{ L}}$."
    )
    ans = f"1. {_fmt(v_dm3)} dm^3; 2. {v_m3:.6f} m^3; 3. 1 dm^3 = 1 L"
    memo = (
        f"1. $\\text{{cm}}^3$ to $\\text{{dm}}^3$ [1]:\n"
        f"   $$V = \\frac{{{v_cm3}}}{{1000}} = {_fmt(v_dm3)}\\text{{ dm}}^3$$ [1]\n"
        f"2. $\\text{{dm}}^3$ to $\\text{{m}}^3$ [1]:\n"
        f"   $$V = \\frac{{{_fmt(v_dm3)}}}{{1000}} = {v_m3:.6f}\\text{{ m}}^3$$ [1]\n"
        f"3. Equivalence [1]: $1\\text{{ dm}}^3 = 1\\text{{ L}}$ [1]."
    )
    hints = {
        "tier_1": "1 dm^3 = 1000 cm^3. 1 m^3 = 1000 dm^3 = 1 000 000 cm^3.",
        "tier_2": "Divide cm^3 by 1000 to get dm^3. Divide by another 1000 for m^3.",
        "tier_3": f"V = {_fmt(v_dm3)} dm^3 = {v_m3:.6f} m^3. 1 dm^3 = 1 L.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "05_volume_units_conversion",
        "learning_objective_id": "ps11_volume_units",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 6,
        "suggested_duration_mins": 3,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["volume_dm3_m3_conversion_error", "cm3_to_dm3_confusion"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Conversion to dm^3", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Conversion to m^3", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Equivalence 1 dm^3 = 1 L", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ---------------------------------------------------------------------------
# 06–12: Boyle's Law (P1*V1 = P2*V2) & Graphs
# ---------------------------------------------------------------------------


def build_06_boyles_law_definition_conditions(rng: random.Random) -> Dict[str, Any]:
    gas_sample = rng.choice(["dry air", "helium (He)", "nitrogen (N2)", "argon (Ar)", "oxygen (O2)"])
    temp_val = rng.choice([20, 25, 27, 30])
    qid = f"ps11_gas_06_{rng.randint(100000, 999999)}"

    prompt = (
        f"Robert Boyle formulated the relationship governing gas pressure and volume using a sealed sample of {gas_sample} at ${temp_val}^\\circ\\text{{C}}$.\n\n"
        f"1. State Boyle's Law in words.\n"
        f"2. State the TWO experimental conditions that must be kept constant for Boyle's Law to hold true.\n"
        f"3. Write down the mathematical formula representing Boyle's Law."
    )
    ans = "1. The pressure of an enclosed gas is inversely proportional to its volume, provided the temperature remains constant. 2. Constant temperature and constant amount/mass of gas. 3. P1*V1 = P2*V2 (or P ∝ 1/V)."
    memo = (
        "1. Boyle's Law statement [2]: The pressure of a fixed mass of enclosed gas is inversely proportional to the volume it occupies, "
        "provided the temperature remains constant [2].\n"
        "2. Constant conditions [2]:\n"
        "   - Temperature ($T$) [1]\n"
        "   - Amount of gas / mass / number of moles ($n$) [1]\n"
        "3. Mathematical formula [1]: $P_1 V_1 = P_2 V_2$ or $P \\propto \\frac{1}{V}$ or $PV = k$ [1]."
    )
    hints = {
        "tier_1": "Pressure and volume have an inverse relationship.",
        "tier_2": "State what happens to pressure as volume changes. Two variables must stay constant: T and n.",
        "tier_3": "Boyle's Law: Pressure is inversely proportional to volume at constant temperature for a fixed mass. P1*V1 = P2*V2.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "06_boyles_law_definition_conditions",
        "learning_objective_id": "ps11_boyle_law_def",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["boyles_law_proportionality_inversion", "failed_to_state_constant_variables"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Boyle's Law formal statement", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Constant temperature condition", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Constant mass/amount of gas condition", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Formula P1V1 = P2V2", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_07_boyles_law_calculate_volume(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice([100.0, 101.3, 120.0, 150.0, 180.0])
    v1 = rng.choice([2.5, 4.0, 5.0, 6.0, 8.0])
    p2 = rng.choice([200.0, 240.0, 300.0, 360.0, 400.0])
    # P1 * V1 = P2 * V2 -> V2 = (P1 * V1) / P2
    v2 = round((p1 * v1) / p2, 2)
    qid = f"ps11_gas_07_{rng.randint(100000, 999999)}"

    prompt = (
        f"A fixed mass of enclosed air occupies a volume of ${_fmt(v1)}\\text{{ dm}}^3$ at a pressure of ${_fmt(p1)}\\text{{ kPa}}$.\n"
        f"The gas is compressed at a constant temperature of $25^\\circ\\text{{C}}$ until the pressure reaches ${_fmt(p2)}\\text{{ kPa}}$.\n\n"
        f"1. Name the gas law applied in this situation.\n"
        f"2. Calculate the final volume ($V_2$) of the gas in $\\text{{dm}}^3$."
    )
    ans = f"1. Boyle's Law; 2. V_2 = {_fmt(v2)} dm^3"
    memo = (
        f"1. Name [1]: Boyle's Law [1].\n"
        f"2. Calculation [3]:\n"
        f"   $$P_1 V_1 = P_2 V_2$$ [M]\n"
        f"   $$({_fmt(p1)})({_fmt(v1)}) = ({_fmt(p2)}) V_2$$\n"
        f"   $$V_2 = \\frac{{{_fmt(p1)} \\times {_fmt(v1)}}}{{{_fmt(p2)}}} = {_fmt(v2)}\\text{{ dm}}^3$$ [A]"
    )
    hints = {
        "tier_1": "Constant temperature indicates Boyle's Law: P1 * V1 = P2 * V2.",
        "tier_2": f"Substitute: ({p1}) * ({v1}) = ({p2}) * V2.",
        "tier_3": f"V2 = ({p1} * {v1}) / {p2} = {_fmt(v2)} dm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "07_boyles_law_calculate_volume",
        "learning_objective_id": "ps11_boyle_calc_vol",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["boyles_law_proportionality_inversion", "incorrect_substitution"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Identify Boyle's Law", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Boyle's Law formula substitution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct final volume with units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_08_boyles_law_calculate_pressure(rng: random.Random) -> Dict[str, Any]:
    v1 = rng.choice([50.0, 60.0, 80.0, 100.0])  # cm^3
    p1 = rng.choice([95.0, 100.0, 101.3, 105.0])  # kPa
    v2 = rng.choice([15.0, 20.0, 25.0, 30.0])  # cm^3
    # P2 = (P1 * V1) / V2
    p2 = round((p1 * v1) / v2, 1)
    qid = f"ps11_gas_08_{rng.randint(100000, 999999)}"

    prompt = (
        f"A gas syringe contains ${_fmt(v1)}\\text{{ cm}}^3$ of gas at a pressure of ${_fmt(p1)}\\text{{ kPa}}$.\n"
        f"The plunger is pushed inwards, reducing the volume to ${_fmt(v2)}\\text{{ cm}}^3$ without any change in temperature.\n\n"
        f"1. Explain why the pressure must increase from a macroscopic and microscopic perspective.\n"
        f"2. Calculate the new pressure ($P_2$) of the gas in $\\text{{kPa}}$."
    )
    ans = f"1. Smaller volume forces particles closer, increasing collision rate per unit area. 2. P_2 = {_fmt(p2)} kPa"
    memo = (
        f"1. Explanation [2]: Reducing volume confines the same number of gas particles into a smaller space [1]. "
        f"This increases the frequency of collisions with the syringe walls, resulting in a greater average force per unit area and higher pressure [1].\n"
        f"2. Calculation [3]:\n"
        f"   $$P_1 V_1 = P_2 V_2$$ [M]\n"
        f"   $$({_fmt(p1)})({_fmt(v1)}) = P_2 ({_fmt(v2)})$$\n"
        f"   $$P_2 = \\frac{{{_fmt(p1)} \\times {_fmt(v1)}}}{{{_fmt(v2)}}} = {_fmt(p2)}\\text{{ kPa}}$$ [A]"
    )
    hints = {
        "tier_1": "Boyle's Law: P1 * V1 = P2 * V2.",
        "tier_2": f"P2 = (P1 * V1) / V2 = ({p1} * {v1}) / {v2}.",
        "tier_3": f"P2 = {_fmt(p2)} kPa.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "08_boyles_law_calculate_pressure",
        "learning_objective_id": "ps11_boyle_calc_pres",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["boyles_law_proportionality_inversion", "pressure_force_area_confusion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Kinetic explanation of pressure rise", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Boyle's Law formula substitution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct pressure with units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_09_boyles_law_percentage_change(rng: random.Random) -> Dict[str, Any]:
    pct_vol_decrease = rng.choice([20, 25, 40, 50, 75])
    # V2 = V1 * (1 - pct/100) -> P2 = P1 / (1 - pct/100)
    ratio_p = 1.0 / (1.0 - pct_vol_decrease / 100.0)
    pct_pres_increase = round((ratio_p - 1.0) * 100.0, 1)
    qid = f"ps11_gas_09_{rng.randint(100000, 999999)}"

    prompt = (
        f"A sample of gas is kept at a constant temperature.\n"
        f"The volume of the container is decreased by ${pct_vol_decrease}\\%$.\n\n"
        f"Calculate the percentage increase in the pressure of the gas."
    )
    ans = f"Pressure increases by {_fmt(pct_pres_increase)}%"
    memo = (
        f"Let initial volume be $V_1$ and initial pressure be $P_1$.\n"
        f"Final volume: $V_2 = V_1 - \\frac{{{pct_vol_decrease}}}{{100}}V_1 = {_fmt(1.0 - pct_vol_decrease/100.0)} V_1$ [1]\n"
        f"From Boyle's Law: $P_1 V_1 = P_2 V_2 \\implies P_1 V_1 = P_2 ({_fmt(1.0 - pct_vol_decrease/100.0)} V_1)$ [1]\n"
        f"$$P_2 = \\frac{{P_1}}{{{_fmt(1.0 - pct_vol_decrease/100.0)}}} = {_fmt(ratio_p, 3)} P_1$$ [1]\n"
        f"Percentage increase in pressure:\n"
        f"$$\\text{{Increase}} = \\frac{{P_2 - P_1}}{{P_1}} \\times 100\\% = ({_fmt(ratio_p, 3)} - 1) \\times 100\\% = {_fmt(pct_pres_increase)}\\%$$ [1]"
    )
    hints = {
        "tier_1": "Express V2 in terms of V1: V2 = (1 - pct/100) * V1. Then apply P1*V1 = P2*V2.",
        "tier_2": f"V2 = {1.0 - pct_vol_decrease/100.0} * V1. So P2 = P1 / {1.0 - pct_vol_decrease/100.0}.",
        "tier_3": f"P2 = {_fmt(ratio_p)} P1. Increase = ({_fmt(ratio_p)} - 1) * 100% = {_fmt(pct_pres_increase)}%.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "09_boyles_law_percentage_change",
        "learning_objective_id": "ps11_boyle_pct_change",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["linear_percentage_misconception", "boyles_law_proportionality_inversion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Express V2 in terms of V1", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Boyle's Law equation", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Ratio P2/P1", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Final percentage increase", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_10_boyles_law_graph_p_vs_v(rng: random.Random) -> Dict[str, Any]:
    t_celsius = rng.choice([20, 25, 30, 40])
    p1, p2, p3 = rng.choice([(100, 200, 400), (80, 160, 320), (120, 240, 480)])
    k = 400  # P * V
    v1 = round(k / p1, 1)
    v2 = round(k / p2, 1)
    v3 = round(k / p3, 1)
    qid = f"ps11_gas_10_{rng.randint(100000, 999999)}"

    # Generate inline SVG isotherm curve
    svg_inner = (
        f'<line x1="50" y1="200" x2="350" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<text x="330" y="220" font-family="sans-serif" font-size="12" fill="#334155">V (dm³)</text>'
        f'<text x="20" y="30" font-family="sans-serif" font-size="12" fill="#334155">P (kPa)</text>'
        # Hyperbolic curve
        f'<path d="M 70 40 Q 90 140 330 185" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<circle cx="85" cy="65" r="4" fill="#dc2626"/>'
        f'<circle cx="150" cy="130" r="4" fill="#dc2626"/>'
        f'<circle cx="280" cy="175" r="4" fill="#dc2626"/>'
        f'<text x="95" y="60" font-family="sans-serif" font-size="11" fill="#dc2626">({_fmt(v3)}; {p3})</text>'
        f'<text x="160" y="125" font-family="sans-serif" font-size="11" fill="#dc2626">({_fmt(v2)}; {p2})</text>'
        f'<text x="280" y="165" font-family="sans-serif" font-size="11" fill="#dc2626">({_fmt(v1)}; {p1})</text>'
        f'<text x="180" y="40" font-family="sans-serif" font-size="11" fill="#1e293b" font-weight="bold">T = {t_celsius}°C (Constant)</text>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying sketch showing the experimental relationship between pressure ($P$) "
        f"and volume ($V$) for an enclosed gas at a constant temperature of ${t_celsius}^\\circ\\text{{C}}$.\n\n"
        f"1. Name the mathematical shape of this curve.\n"
        f"2. State the relationship between pressure and volume demonstrated by the graph.\n"
        f"3. Verify that the three coordinate points obey Boyle's Law by calculating the product $P \\times V$ at each point."
    )
    ans = f"1. Hyperbola (or inverse curve). 2. Pressure is inversely proportional to volume. 3. P*V = {p1}*{_fmt(v1)} = {p2}*{_fmt(v2)} = {p3}*{_fmt(v3)} = {k} kPa*dm^3."
    memo = (
        f"1. Curve shape [1]: Hyperbola (or rectangular hyperbola) [1].\n"
        f"2. Relationship [1]: Pressure is inversely proportional to volume ($P \\propto \\frac{{1}}{{V}}$) [1].\n"
        f"3. Verification [3]:\n"
        f"   - Point 1: $P_1 V_1 = ({p1})({_fmt(v1)}) = {k}\\text{{ kPa}}\\cdot\\text{{dm}}^3$ [1]\n"
        f"   - Point 2: $P_2 V_2 = ({p2})({_fmt(v2)}) = {k}\\text{{ kPa}}\\cdot\\text{{dm}}^3$ [1]\n"
        f"   - Point 3: $P_3 V_3 = ({p3})({_fmt(v3)}) = {k}\\text{{ kPa}}\\cdot\\text{{dm}}^3$ [1]\n"
        f"   Since $P \\times V = \\text{{constant}}$, Boyle's Law is verified."
    )
    hints = {
        "tier_1": "A curve of y versus 1/x is a hyperbola. Calculate P * V for all points.",
        "tier_2": "Calculate P1*V1, P2*V2, and P3*V3. They should all equal the same constant k.",
        "tier_3": f"Shape: Hyperbola. Relationship: Inverse proportionality. k = {k} kPa*dm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "10_boyles_law_graph_p_vs_v",
        "learning_objective_id": "ps11_boyle_graph_pv",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Boyle's Law P vs V Isotherm at {t_celsius}°C"},
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["hyperbola_graph_misinterpretation", "inverse_proportionality_verification_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Identify curve shape as hyperbola", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "State inverse proportionality", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Calculate PV products verifying constant", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_11_boyles_law_graph_p_vs_inv_v(rng: random.Random) -> Dict[str, Any]:
    # Straight line passing through origin: P = k * (1/V)
    grad_k = rng.choice([200, 300, 450, 600])  # kPa * dm^3
    x_val = rng.choice([0.2, 0.4, 0.5, 0.8])
    p_val = round(grad_k * x_val, 1)
    qid = f"ps11_gas_11_{rng.randint(100000, 999999)}"

    svg_inner = (
        f'<line x1="50" y1="200" x2="350" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<text x="310" y="225" font-family="sans-serif" font-size="12" fill="#334155">1/V (dm⁻³)</text>'
        f'<text x="20" y="30" font-family="sans-serif" font-size="12" fill="#334155">P (kPa)</text>'
        # Straight line from origin
        f'<line x1="50" y1="200" x2="320" y2="50" stroke="#16a34a" stroke-width="2.5"/>'
        f'<circle cx="230" cy="100" r="4" fill="#dc2626"/>'
        f'<line x1="230" y1="100" x2="230" y2="200" stroke="#94a3b8" stroke-dasharray="4"/>'
        f'<line x1="50" y1="100" x2="230" y2="100" stroke="#94a3b8" stroke-dasharray="4"/>'
        f'<text x="235" y="95" font-family="sans-serif" font-size="11" fill="#dc2626">({_fmt(x_val)}; {_fmt(p_val)})</text>'
        f'<text x="140" y="60" font-family="sans-serif" font-size="11" fill="#1e293b" font-weight="bold">Straight line through origin</text>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying graph showing gas pressure ($P$) plotted against the reciprocal of volume ($\\frac{{1}}{{V}}$).\n\n"
        f"1. Explain what the straight line passing through the origin proves about the relationship between $P$ and $V$.\n"
        f"2. Using the marked coordinate point $({_fmt(x_val)}\\text{{ dm}}^{{-3}}; {_fmt(p_val)}\\text{{ kPa}})$, calculate the gradient of the graph.\n"
        f"3. State the physical quantity represented by this gradient."
    )
    ans = f"1. Proves P is directly proportional to 1/V, meaning P is inversely proportional to V (Boyle's Law). 2. Gradient = {_fmt(grad_k)} kPa*dm^3. 3. The Boyle's Law proportionality constant k (or nRT)."
    memo = (
        f"1. Relationship [2]: A straight line through the origin proves that pressure is directly proportional to the inverse of volume ($P \\propto \\frac{{1}}{{V}}$) [1], "
        f"which confirms that pressure is inversely proportional to volume (Boyle's Law) [1].\n"
        f"2. Gradient calculation [2]:\n"
        f"   $$\\text{{Gradient}} = \\frac{{\\Delta P}}{{\\Delta (1/V)}} = \\frac{{{_fmt(p_val)} - 0}}{{{_fmt(x_val)} - 0}} = {_fmt(grad_k)}\\text{{ kPa}}\\cdot\\text{{dm}}^3$$ [2]\n"
        f"3. Physical meaning [1]: The gradient represents the constant of proportionality $k$ (where $k = PV = nRT$) [1]."
    )
    hints = {
        "tier_1": "A straight line through origin shows direct proportionality: P ∝ 1/V.",
        "tier_2": "Gradient = ΔP / Δ(1/V). Substitute marked point.",
        "tier_3": f"Gradient = {p_val} / {x_val} = {grad_k} kPa*dm^3. Represents k = nRT.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "11_boyles_law_graph_p_vs_inv_v",
        "learning_objective_id": "ps11_boyle_graph_inv_v",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Boyle's Law P vs 1/V Linear Graph"},
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["gradient_units_error", "reciprocal_volume_misunderstood"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Interpretation of linear graph through origin", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Gradient calculation with working", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Physical quantity of gradient (constant k / nRT)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_12_boyles_law_graph_pv_vs_p(rng: random.Random) -> Dict[str, Any]:
    pv_const = rng.choice([250, 400, 500, 750])  # kPa * dm^3
    qid = f"ps11_gas_12_{rng.randint(100000, 999999)}"

    svg_inner = (
        f'<line x1="50" y1="200" x2="350" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<text x="320" y="225" font-family="sans-serif" font-size="12" fill="#334155">P (kPa)</text>'
        f'<text x="15" y="30" font-family="sans-serif" font-size="12" fill="#334155">PV (kPa·dm³)</text>'
        # Horizontal line
        f'<line x1="50" y1="100" x2="340" y2="100" stroke="#7c3aed" stroke-width="2.5"/>'
        f'<text x="55" y="90" font-family="sans-serif" font-size="11" fill="#7c3aed" font-weight="bold">PV = {pv_const} kPa·dm³</text>'
        f'<circle cx="150" cy="100" r="3" fill="#7c3aed"/>'
        f'<circle cx="270" cy="100" r="3" fill="#7c3aed"/>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying plot of the product $PV = {pv_const}\\text{{ kPa}}\\cdot\\text{{dm}}^3$ against pressure ($P$) for an ideal gas sample at constant temperature.\n\n"
        f"1. Explain why the line is horizontal with a gradient of zero.\n"
        f"2. If the temperature of the gas sample is increased to a higher constant temperature, sketch or describe "
        f"how the new graph line would compare to the original line."
    )
    ans = "1. For an ideal gas at constant temperature, the product PV is constant (PV = k), so changing P does not alter PV (zero slope). 2. The new line would remain horizontal but shift upwards to a higher PV intercept, since PV = nRT and higher T gives a larger constant."
    memo = (
        "1. Horizontal line explanation [2]: Boyle's Law states that $PV = k$ (a constant) at constant temperature [1]. "
        "Therefore, as pressure varies, the product $PV$ remains unchanged, resulting in a horizontal line with zero slope [1].\n"
        "2. Effect of higher temperature [2]: Since $PV = nRT$, an increase in temperature ($T$) increases the constant $k$ [1]. "
        "The new graph will be a horizontal line parallel to the original but shifted vertically upwards to a higher $PV$ value [1]."
    )
    hints = {
        "tier_1": "Boyle's Law states PV = k. What happens to a constant function on a graph?",
        "tier_2": "PV is constant at fixed T, so slope is 0. If T increases, PV = nRT also increases.",
        "tier_3": "1. Slope is 0 because PV is constant. 2. Higher T shifts the horizontal line upwards.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "12_boyles_law_graph_pv_vs_p",
        "learning_objective_id": "ps11_boyle_graph_pv_const",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "PV vs P Horizontal Constancy Graph"},
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["pv_constancy_misunderstood", "temperature_shift_inversion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Explanation of zero slope from Boyle's Law", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Effect of higher temperature shifting line upwards", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ---------------------------------------------------------------------------
# 13–18: Charles's Law (V1/T1 = V2/T2) & Graphs
# ---------------------------------------------------------------------------


def build_13_charles_law_definition_conditions(rng: random.Random) -> Dict[str, Any]:
    gas_sample = rng.choice(["hydrogen (H2)", "helium (He)", "nitrogen (N2)", "oxygen (O2)", "argon (Ar)"])
    p_const = rng.choice([100, 101.3, 120, 150])
    qid = f"ps11_gas_13_{rng.randint(100000, 999999)}"

    prompt = (
        f"Jacques Charles investigated the relationship between the volume and temperature of {gas_sample} at a fixed pressure of ${_fmt(p_const)}\\text{{ kPa}}$.\n\n"
        f"1. State Charles's Law in words.\n"
        f"2. Identify the TWO variables that must remain constant for Charles's Law to apply.\n"
        f"3. Write down the mathematical equation for Charles's Law."
    )
    ans = "1. The volume of a fixed mass of enclosed gas is directly proportional to its absolute temperature in Kelvin, provided the pressure remains constant. 2. Constant pressure and constant amount/mass of gas. 3. V1/T1 = V2/T2."
    memo = (
        "1. Charles's Law statement [2]: The volume of a fixed mass of enclosed gas is directly proportional to its absolute temperature (in Kelvin), "
        "provided the pressure remains constant [2].\n"
        "2. Constant variables [2]: Pressure ($P$) [1] and mass / number of moles ($n$) [1].\n"
        "3. Mathematical equation [1]: $\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$ or $V \\propto T$ [1]."
    )
    hints = {
        "tier_1": "Charles's Law relates volume and absolute temperature.",
        "tier_2": "Temperature must be in Kelvin. Pressure is held constant.",
        "tier_3": "V1/T1 = V2/T2 at constant pressure and mass.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "13_charles_law_definition_conditions",
        "learning_objective_id": "ps11_charles_law_def",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["forgot_kelvin_conversion", "failed_to_state_constant_variables"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Charles's Law formal statement", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Constant pressure condition", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Constant mass condition", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Formula V1/T1 = V2/T2", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_14_charles_law_calculate_volume(rng: random.Random) -> Dict[str, Any]:
    t1_c = rng.choice([15, 20, 25, 27, 30])
    v1 = rng.choice([1.5, 2.0, 3.0, 4.5, 6.0])  # dm^3
    t2_c = rng.choice([60, 75, 80, 100, 120])
    t1_k = t1_c + 273
    t2_k = t2_c + 273
    # V2 = (V1 * T2_K) / T1_K
    v2 = round((v1 * t2_k) / t1_k, 2)
    qid = f"ps11_gas_14_{rng.randint(100000, 999999)}"

    prompt = (
        f"A gas syringe with a frictionless piston contains ${_fmt(v1)}\\text{{ dm}}^3$ of nitrogen at ${t1_c}^\\circ\\text{{C}}$.\n"
        f"The gas is heated at constant pressure until the temperature reaches ${t2_c}^\\circ\\text{{C}}$.\n\n"
        f"1. Convert both temperatures to Kelvin.\n"
        f"2. Calculate the new volume ($V_2$) of the gas in $\\text{{dm}}^3$."
    )
    ans = f"1. T_1 = {_fmt(t1_k)} K, T_2 = {_fmt(t2_k)} K; 2. V_2 = {_fmt(v2)} dm^3"
    memo = (
        f"1. Temperature conversions [2]:\n"
        f"   - $T_1 = {t1_c} + 273 = {_fmt(t1_k)}\\text{{ K}}$ [1]\n"
        f"   - $T_2 = {t2_c} + 273 = {_fmt(t2_k)}\\text{{ K}}$ [1]\n"
        f"2. Charles's Law [3]:\n"
        f"   $$\\frac{{V_1}}{{T_1}} = \\frac{{V_2}}{{T_2}}$$ [M]\n"
        f"   $$\\frac{{{_fmt(v1)}}}{{{_fmt(t1_k)}}} = \\frac{{V_2}}{{{_fmt(t2_k)}}}$$\n"
        f"   $$V_2 = \\frac{{{_fmt(v1)} \\times {_fmt(t2_k)}}}{{{_fmt(t1_k)}}} = {_fmt(v2)}\\text{{ dm}}^3$$ [A]"
    )
    hints = {
        "tier_1": "Always convert Celsius to Kelvin: T(K) = T(°C) + 273.",
        "tier_2": f"T1 = {t1_k} K, T2 = {t2_k} K. Apply V1/T1 = V2/T2.",
        "tier_3": f"V2 = ({v1} * {t2_k}) / {t1_k} = {_fmt(v2)} dm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "14_charles_law_calculate_volume",
        "learning_objective_id": "ps11_charles_calc_vol",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["forgot_kelvin_conversion", "celsius_ratio_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert T1 and T2 to Kelvin", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Charles's Law formula substitution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct final volume with units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_15_charles_law_calculate_temperature(rng: random.Random) -> Dict[str, Any]:
    v1 = rng.choice([2.0, 3.0, 4.0, 5.0])  # dm^3
    t1_c = rng.choice([20, 25, 27])
    t1_k = t1_c + 273
    v2 = rng.choice([4.0, 6.0, 8.0, 10.0])  # dm^3 (expansion)
    # T2_K = (V2 * T1_K) / V1
    t2_k = round((v2 * t1_k) / v1, 1)
    t2_c = round(t2_k - 273, 1)
    qid = f"ps11_gas_15_{rng.randint(100000, 999999)}"

    prompt = (
        f"A weather balloon contains ${_fmt(v1)}\\text{{ dm}}^3$ of helium at ${t1_c}^\\circ\\text{{C}}$ and atmospheric pressure.\n"
        f"Assuming the pressure remains constant, to what temperature (in $^\\circ\\text{{C}}$) must the gas be heated "
        f"so that its volume expands to ${_fmt(v2)}\\text{{ dm}}^3$?"
    )
    ans = f"T_2 = {_fmt(t2_c)} °C (or {_fmt(t2_k)} K)"
    memo = (
        f"1. Convert initial temperature to Kelvin [1]:\n"
        f"   $$T_1 = {t1_c} + 273 = {_fmt(t1_k)}\\text{{ K}}$$ [1]\n"
        f"2. Apply Charles's Law [2]:\n"
        f"   $$\\frac{{V_1}}{{T_1}} = \\frac{{V_2}}{{T_2}} \\implies \\frac{{{_fmt(v1)}}}{{{_fmt(t1_k)}}} = \\frac{{{_fmt(v2)}}}{{T_2}}$$ [M]\n"
        f"   $$T_2 = \\frac{{{_fmt(v2)} \\times {_fmt(t1_k)}}}{{{_fmt(v1)}}} = {_fmt(t2_k)}\\text{{ K}}$$ [1]\n"
        f"3. Convert back to degrees Celsius [1]:\n"
        f"   $$T_2(^\\circ\\text{{C}}) = {_fmt(t2_k)} - 273 = {_fmt(t2_c)}^\\circ\\text{{C}}$$ [A]"
    )
    hints = {
        "tier_1": "Formula: V1/T1 = V2/T2. Remember T must be in Kelvin.",
        "tier_2": f"T1 = {t1_k} K. Solve for T2 in K, then subtract 273 for °C.",
        "tier_3": f"T2(K) = ({v2} * {t1_k}) / {v1} = {t2_k} K -> T2(°C) = {t2_c} °C.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "15_charles_law_calculate_temperature",
        "learning_objective_id": "ps11_charles_calc_temp",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["forgot_kelvin_conversion", "celsius_to_kelvin_inversion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert T1 to Kelvin", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Charles's Law formula substitution", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Solve T2 in Kelvin", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Convert T2 to Celsius with units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_16_charles_law_graph_v_vs_t_kelvin(rng: random.Random) -> Dict[str, Any]:
    p_kpa = rng.choice([100, 101.3, 150, 200])
    qid = f"ps11_gas_16_{rng.randint(100000, 999999)}"

    svg_inner = (
        f'<line x1="50" y1="200" x2="350" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<text x="310" y="225" font-family="sans-serif" font-size="12" fill="#334155">T (K)</text>'
        f'<text x="15" y="30" font-family="sans-serif" font-size="12" fill="#334155">V (dm³)</text>'
        # Straight line passing through origin
        f'<line x1="50" y1="200" x2="320" y2="40" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="50" y="215" font-family="sans-serif" font-size="11" fill="#475569">0</text>'
        f'<circle cx="185" cy="120" r="4" fill="#dc2626"/>'
        f'<text x="195" y="115" font-family="sans-serif" font-size="11" fill="#dc2626">Direct Proportionality</text>'
        f'<text x="140" y="35" font-family="sans-serif" font-size="11" fill="#1e293b" font-weight="bold">P = {p_kpa} kPa (Constant)</text>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying graph showing the relationship between volume ($V$) and temperature ($T$) "
        f"for an enclosed gas kept at a constant pressure of ${p_kpa}\\text{{ kPa}}$.\n\n"
        f"1. State what the straight line passing through the origin demonstrates regarding the relationship between $V$ and $T$.\n"
        f"2. Explain, in terms of the kinetic molecular theory, why heating a gas at constant pressure causes it to expand."
    )
    ans = "1. Volume is directly proportional to absolute temperature in Kelvin (V ∝ T). 2. Heating increases the average kinetic energy and speed of particles. To maintain constant pressure (constant collision rate per unit area), the container must expand so particles have further to travel between wall collisions."
    memo = (
        "1. Mathematical relationship [2]: The straight line passing through the origin demonstrates that volume is directly proportional "
        "to the absolute temperature in Kelvin ($V \\propto T$) [2].\n"
        "2. Kinetic theory explanation [3]:\n"
        "   - Heating increases the temperature, which increases the average kinetic energy and average speed of the gas particles [1].\n"
        "   - Faster-moving particles collide more forcefully and more frequently with the walls of the container [1].\n"
        "   - In order for the pressure (force per unit area) to remain constant, the gas must expand, increasing the volume so that the collision frequency per unit area remains unchanged [1]."
    )
    hints = {
        "tier_1": "A straight line through origin represents direct proportionality: V ∝ T.",
        "tier_2": "Higher temperature means faster particles. For pressure to remain constant, volume must increase.",
        "tier_3": "V is directly proportional to T(K). Faster particles need more volume to keep wall collision rate constant.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "16_charles_law_graph_v_vs_t_kelvin",
        "learning_objective_id": "ps11_charles_graph_kelvin",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Charles's Law V vs T(K) at P={p_kpa} kPa"},
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["direct_proportionality_misinterpreted", "pressure_expansion_kinetic_confusion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of direct proportionality V ∝ T", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Kinetic energy increase with temperature", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "More forceful collisions on container", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Volume expansion to maintain constant pressure", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_17_charles_law_graph_v_vs_t_celsius(rng: random.Random) -> Dict[str, Any]:
    v0_dm3 = rng.choice([2.2, 4.5, 6.7, 11.2, 22.4])
    qid = f"ps11_gas_17_{rng.randint(100000, 999999)}"

    svg_inner = (
        f'<line x1="30" y1="180" x2="350" y2="180" stroke="#475569" stroke-width="2"/>'
        f'<line x1="200" y1="20" x2="200" y2="180" stroke="#475569" stroke-width="2"/>'
        f'<text x="320" y="200" font-family="sans-serif" font-size="12" fill="#334155">T (°C)</text>'
        f'<text x="155" y="30" font-family="sans-serif" font-size="12" fill="#334155">V (dm³)</text>'
        # Solid line for positive Celsius
        f'<line x1="200" y1="120" x2="330" y2="40" stroke="#16a34a" stroke-width="2.5"/>'
        # Extrapolated dashed line to -273 °C
        f'<line x1="60" y1="180" x2="200" y2="120" stroke="#dc2626" stroke-width="2" stroke-dasharray="4"/>'
        f'<circle cx="60" cy="180" r="4" fill="#dc2626"/>'
        f'<circle cx="200" cy="120" r="4" fill="#16a34a"/>'
        f'<text x="40" y="205" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">-273°C</text>'
        f'<text x="205" y="125" font-family="sans-serif" font-size="11" fill="#16a34a">(0°C; {_fmt(v0_dm3)} dm³)</text>'
        f'<text x="70" y="145" font-family="sans-serif" font-size="10" fill="#dc2626">Extrapolation</text>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying graph showing the volume of a gas (which occupies ${_fmt(v0_dm3)}\\text{{ dm}}^3$ at $0^\\circ\\text{{C}}$) "
        f"plotted against temperature in degrees Celsius ($^\\circ\\text{{C}}$).\n\n"
        f"1. State the significance of the $x$-intercept at $-273^\\circ\\text{{C}}$.\n"
        f"2. Explain why the line must be dashed (extrapolated) rather than solid as it approaches $-273^\\circ\\text{{C}}$."
    )
    ans = "1. -273 °C represents absolute zero (0 K), the theoretical temperature at which ideal gas volume would reach zero. 2. Real gases liquefy (and solidify) before reaching absolute zero due to intermolecular forces, so real gas data cannot be measured experimentally in the gaseous state."
    memo = (
        "1. Significance of x-intercept [2]:\n"
        "   - The $x$-intercept is absolute zero ($-273^\\circ\\text{C}$ or $0\\text{ K}$) [1].\n"
        "   - It represents the theoretical lowest possible temperature where the volume of an ideal gas would extrapolate to zero [1].\n"
        "2. Reason for dashed/extrapolated line [2]:\n"
        "   - Real gases do not remain in the gaseous phase at extremely low temperatures [1].\n"
        "   - Intermolecular forces cause real gases to liquefy and then solidify before reaching $-273^\\circ\\text{C}$, making direct experimental gas measurements impossible [1]."
    )
    hints = {
        "tier_1": "-273 °C is absolute zero. What happens to real gases when cooled very low?",
        "tier_2": "At low temperatures, gas particles attract and condense into a liquid. The gas laws no longer apply.",
        "tier_3": "1. -273 °C is absolute zero (0 K). 2. Dashed because real gases liquefy before reaching absolute zero.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "17_charles_law_graph_v_vs_t_celsius",
        "learning_objective_id": "ps11_charles_graph_celsius",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Charles's Law V vs T(°C) Extrapolation to -273°C"},
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["absolute_zero_misunderstood", "real_gas_liquefaction_ignored"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Identify -273 °C as absolute zero / zero volume point", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Explain liquefaction of real gases requiring extrapolation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_18_charles_law_hot_air_balloon_density(rng: random.Random) -> Dict[str, Any]:
    t_ambient_c = rng.choice([15, 20, 25])
    t_inside_c = rng.choice([80, 95, 105, 120])
    rho_ambient = 1.20  # kg / m^3
    t_ambient_k = t_ambient_c + 273
    t_inside_k = t_inside_c + 273
    # At constant pressure, rho = m/V -> rho is inversely proportional to T(K)
    # rho_inside = rho_ambient * (T_ambient_K / T_inside_K)
    rho_inside = round(rho_ambient * (t_ambient_k / t_inside_k), 3)
    qid = f"ps11_gas_18_{rng.randint(100000, 999999)}"

    prompt = (
        f"A hot-air balloon operates at atmospheric pressure.\n"
        f"The surrounding ambient air temperature is ${t_ambient_c}^\\circ\\text{{C}}$ with an air density of "
        f"${_fmt(rho_ambient)}\\text{{ kg}}\\cdot\\text{{m}}^{{-3}}$.\n"
        f"The air inside the balloon envelope is heated to a temperature of ${t_inside_c}^\\circ\\text{{C}}$.\n\n"
        f"1. Explain, using Charles's Law, why the density of the air inside the balloon decreases upon heating.\n"
        f"2. Calculate the density of the heated air inside the envelope in $\\text{{kg}}\\cdot\\text{{m}}^{{-3}}$."
    )
    ans = f"1. Heating at constant pressure causes the air to expand (volume increases). Since mass per unit volume decreases, density decreases. 2. Density = {_fmt(rho_inside)} kg/m^3"
    memo = (
        f"1. Explanation [2]: According to Charles's Law, volume is directly proportional to absolute temperature ($V \\propto T$) at constant pressure [1]. "
        f"When air is heated, it expands and escapes through the open bottom, meaning fewer air molecules occupy the fixed envelope volume, decreasing density ($\\rho = \\frac{{m}}{{V}}$) [1].\n"
        f"2. Calculation [3]:\n"
        f"   $$T_1 = {t_ambient_c} + 273 = {_fmt(t_ambient_k)}\\text{{ K}}, \\quad T_2 = {t_inside_c} + 273 = {_fmt(t_inside_k)}\\text{{ K}}$$ [1]\n"
        f"   Since $\\rho \\propto \\frac{{1}}{{T}}$ at constant pressure:\n"
        f"   $$\\rho_2 = \\rho_1 \\times \\frac{{T_1}}{{T_2}} = {_fmt(rho_ambient)} \\times \\frac{{{_fmt(t_ambient_k)}}}{{{_fmt(t_inside_k)}}} = {_fmt(rho_inside)}\\text{{ kg}}\\cdot\\text{{m}}^{{-3}}$$ [2]"
    )
    hints = {
        "tier_1": "Charles's Law: heating causes expansion. Density = mass / volume.",
        "tier_2": "Convert temperatures to Kelvin. Density is inversely proportional to absolute temperature at constant P.",
        "tier_3": f"T1 = {t_ambient_k} K, T2 = {t_inside_k} K. rho2 = {rho_ambient} * ({t_ambient_k}/{t_inside_k}) = {_fmt(rho_inside)} kg/m^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "18_charles_law_hot_air_balloon_density",
        "learning_objective_id": "ps11_charles_hot_air_balloon",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["density_temperature_relation_error", "forgot_kelvin_conversion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Charles's law expansion explanation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Kelvin temperature conversions", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Density calculation with correct units", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ---------------------------------------------------------------------------
# 19–25: Gay-Lussac's Law (P1/T1 = P2/T2) & Practical Applications
# ---------------------------------------------------------------------------


def build_19_gay_lussacs_law_definition_conditions(rng: random.Random) -> Dict[str, Any]:
    gas_sample = rng.choice(["oxygen (O2)", "carbon dioxide (CO2)", "nitrogen (N2)", "argon (Ar)"])
    v_const = rng.choice([2, 5, 10, 25])
    qid = f"ps11_gas_19_{rng.randint(100000, 999999)}"

    prompt = (
        f"Joseph Louis Gay-Lussac investigated the pressure-temperature relationship of {gas_sample} enclosed in a rigid ${v_const}\\text{{ dm}}^3$ container.\n\n"
        f"1. State Gay-Lussac's Law in words.\n"
        f"2. Identify the TWO variables that must remain constant for Gay-Lussac's Law to apply.\n"
        f"3. Write down the mathematical equation for Gay-Lussac's Law."
    )
    ans = "1. The pressure of a fixed mass of enclosed gas is directly proportional to its absolute temperature in Kelvin, provided the volume remains constant. 2. Constant volume and constant amount/mass of gas. 3. P1/T1 = P2/T2."
    memo = (
        "1. Statement [2]: The pressure of a fixed mass of enclosed gas is directly proportional to its absolute temperature (in Kelvin), "
        "provided the volume of the container remains constant [2].\n"
        "2. Constant variables [2]: Volume ($V$) [1] and amount of gas / mass ($n$) [1].\n"
        "3. Formula [1]: $\\frac{P_1}{T_1} = \\frac{P_2}{T_2}$ or $P \\propto T$ [1]."
    )
    hints = {
        "tier_1": "Gay-Lussac's Law relates pressure and temperature in a rigid container.",
        "tier_2": "Temperature must be in Kelvin. Volume is held constant.",
        "tier_3": "P1/T1 = P2/T2 at constant V and n.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "19_gay_lussacs_law_definition_conditions",
        "learning_objective_id": "ps11_gay_lussac_def",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["forgot_kelvin_conversion", "failed_to_state_constant_variables"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Gay-Lussac's Law statement", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Constant volume condition", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Constant mass condition", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Formula P1/T1 = P2/T2", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_20_gay_lussacs_law_calculate_pressure(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice([120.0, 150.0, 200.0, 250.0])  # kPa
    t1_c = rng.choice([18, 20, 25, 27])
    t2_c = rng.choice([80, 95, 120, 150])
    t1_k = t1_c + 273
    t2_k = t2_c + 273
    # P2 = (P1 * T2_K) / T1_K
    p2 = round((p1 * t2_k) / t1_k, 1)
    qid = f"ps11_gas_20_{rng.randint(100000, 999999)}"

    prompt = (
        f"A rigid steel cylinder contains compressed gas at a pressure of ${_fmt(p1)}\\text{{ kPa}}$ at ${t1_c}^\\circ\\text{{C}}$.\n"
        f"The cylinder is heated until the temperature of the gas reaches ${t2_c}^\\circ\\text{{C}}$.\n\n"
        f"1. Convert both temperatures to Kelvin.\n"
        f"2. Calculate the final pressure ($P_2$) of the gas in $\\text{{kPa}}$."
    )
    ans = f"1. T_1 = {_fmt(t1_k)} K, T_2 = {_fmt(t2_k)} K; 2. P_2 = {_fmt(p2)} kPa"
    memo = (
        f"1. Temperature conversions [2]:\n"
        f"   - $T_1 = {t1_c} + 273 = {_fmt(t1_k)}\\text{{ K}}$ [1]\n"
        f"   - $T_2 = {t2_c} + 273 = {_fmt(t2_k)}\\text{{ K}}$ [1]\n"
        f"2. Gay-Lussac's Law [3]:\n"
        f"   $$\\frac{{P_1}}{{T_1}} = \\frac{{P_2}}{{T_2}}$$ [M]\n"
        f"   $$\\frac{{{_fmt(p1)}}}{{{_fmt(t1_k)}}} = \\frac{{P_2}}{{{_fmt(t2_k)}}}$$\n"
        f"   $$P_2 = \\frac{{{_fmt(p1)} \\times {_fmt(t2_k)}}}{{{_fmt(t1_k)}}} = {_fmt(p2)}\\text{{ kPa}}$$ [A]"
    )
    hints = {
        "tier_1": "Formula: P1/T1 = P2/T2. Temperatures must be in Kelvin.",
        "tier_2": f"T1 = {t1_k} K, T2 = {t2_k} K. Solve P2 = (P1 * T2) / T1.",
        "tier_3": f"P2 = ({p1} * {t2_k}) / {t1_k} = {_fmt(p2)} kPa.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "20_gay_lussacs_law_calculate_pressure",
        "learning_objective_id": "ps11_gay_lussac_calc_pres",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["forgot_kelvin_conversion", "gay_lussac_ratio_inversion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert T1 and T2 to Kelvin", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Gay-Lussac formula substitution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct final pressure with units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_21_gay_lussacs_law_calculate_temperature(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice([150.0, 180.0, 200.0])  # kPa
    t1_c = rng.choice([20, 25])
    t1_k = t1_c + 273
    p_burst = rng.choice([450.0, 500.0, 600.0])  # kPa
    # T2_K = (P_burst * T1_K) / P1
    t2_k = round((p_burst * t1_k) / p1, 1)
    t2_c = round(t2_k - 273, 1)
    qid = f"ps11_gas_21_{rng.randint(100000, 999999)}"

    prompt = (
        f"An aerosol can contains propellant gas at a pressure of ${_fmt(p1)}\\text{{ kPa}}$ and a room temperature of ${t1_c}^\\circ\\text{{C}}$.\n"
        f"The can is marked with a safety warning indicating that it will rupture if the internal pressure reaches ${_fmt(p_burst)}\\text{{ kPa}}$.\n\n"
        f"Assuming the volume of the can remains constant, calculate the maximum temperature (in $^\\circ\\text{{C}}$) "
        f"to which the can can be heated before it bursts."
    )
    ans = f"T_max = {_fmt(t2_c)} °C (or {_fmt(t2_k)} K)"
    memo = (
        f"1. Convert initial temperature to Kelvin [1]:\n"
        f"   $$T_1 = {t1_c} + 273 = {_fmt(t1_k)}\\text{{ K}}$$ [1]\n"
        f"2. Apply Gay-Lussac's Law [2]:\n"
        f"   $$\\frac{{P_1}}{{T_1}} = \\frac{{P_2}}{{T_2}} \\implies \\frac{{{_fmt(p1)}}}{{{_fmt(t1_k)}}} = \\frac{{{_fmt(p_burst)}}}{{T_2}}$$ [M]\n"
        f"   $$T_2 = \\frac{{{_fmt(p_burst)} \\times {_fmt(t1_k)}}}{{{_fmt(p1)}}} = {_fmt(t2_k)}\\text{{ K}}$$ [1]\n"
        f"3. Convert back to degrees Celsius [1]:\n"
        f"   $$T_2(^\\circ\\text{{C}}) = {_fmt(t2_k)} - 273 = {_fmt(t2_c)}^\\circ\\text{{C}}$$ [A]"
    )
    hints = {
        "tier_1": "P1/T1 = P2/T2. Volume is constant.",
        "tier_2": f"T1 = {t1_k} K. Solve for T2 in K, then convert to °C.",
        "tier_3": f"T2 = ({p_burst} * {t1_k}) / {p1} = {t2_k} K -> T2(°C) = {t2_c} °C.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "21_gay_lussacs_law_calculate_temperature",
        "learning_objective_id": "ps11_gay_lussac_calc_temp",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["forgot_kelvin_conversion", "celsius_to_kelvin_inversion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert T1 to Kelvin", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Gay-Lussac formula substitution", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Solve T2 in Kelvin", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Convert T2 to Celsius with units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_22_gay_lussacs_law_graph_p_vs_t_kelvin(rng: random.Random) -> Dict[str, Any]:
    vol_dm3 = rng.choice([2.0, 5.0, 10.0])
    qid = f"ps11_gas_22_{rng.randint(100000, 999999)}"

    svg_inner = (
        f'<line x1="50" y1="200" x2="350" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<text x="310" y="225" font-family="sans-serif" font-size="12" fill="#334155">T (K)</text>'
        f'<text x="15" y="30" font-family="sans-serif" font-size="12" fill="#334155">P (kPa)</text>'
        f'<line x1="50" y1="200" x2="320" y2="40" stroke="#d97706" stroke-width="2.5"/>'
        f'<text x="50" y="215" font-family="sans-serif" font-size="11" fill="#475569">0</text>'
        f'<circle cx="185" cy="120" r="4" fill="#dc2626"/>'
        f'<text x="195" y="115" font-family="sans-serif" font-size="11" fill="#dc2626">Direct Proportionality</text>'
        f'<text x="140" y="35" font-family="sans-serif" font-size="11" fill="#1e293b" font-weight="bold">V = {_fmt(vol_dm3)} dm³ (Constant)</text>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying graph showing the relationship between pressure ($P$) and absolute temperature ($T$) "
        f"for an enclosed gas sample in a rigid container of volume ${_fmt(vol_dm3)}\\text{{ dm}}^3$.\n\n"
        f"1. State the relationship between pressure and temperature demonstrated by the graph.\n"
        f"2. Explain, using kinetic molecular theory, why heating the rigid container increases the pressure exerted on its walls."
    )
    ans = "1. Pressure is directly proportional to absolute temperature in Kelvin (P ∝ T). 2. Heating increases the average kinetic energy and speed of the gas particles. Particles collide with the rigid container walls more frequently and with greater force per collision, increasing the pressure (P = F/A)."
    memo = (
        "1. Relationship [2]: Pressure is directly proportional to absolute temperature in Kelvin ($P \\propto T$) [2].\n"
        "2. Kinetic theory explanation [3]:\n"
        "   - Heating increases the temperature, which increases the average kinetic energy and speed of the particles [1].\n"
        "   - Since the volume is fixed, faster particles collide with the walls more frequently (higher collision rate) [1].\n"
        "   - Each collision also delivers a greater change in momentum (greater impact force), so total force per unit area ($P = \\frac{F}{A}$) increases [1]."
    )
    hints = {
        "tier_1": "Gay-Lussac's Law: P ∝ T(K).",
        "tier_2": "Temperature is average kinetic energy. Faster particles hit the walls harder and more often.",
        "tier_3": "Direct proportionality. Higher T -> faster particles -> more frequent, harder collisions -> higher pressure.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "22_gay_lussacs_law_graph_p_vs_t_kelvin",
        "learning_objective_id": "ps11_gay_lussac_graph_kelvin",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Gay-Lussac P vs T(K) at V={_fmt(vol_dm3)} dm³"},
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["direct_proportionality_misinterpreted", "pressure_force_area_confusion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of direct proportionality P ∝ T", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Kinetic energy and speed increase", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Collision frequency increase", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Force per collision and pressure increase", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_23_gay_lussacs_law_graph_p_vs_t_celsius(rng: random.Random) -> Dict[str, Any]:
    p0_kpa = rng.choice([90, 100, 110, 120, 150])
    qid = f"ps11_gas_23_{rng.randint(100000, 999999)}"

    svg_inner = (
        f'<line x1="30" y1="180" x2="350" y2="180" stroke="#475569" stroke-width="2"/>'
        f'<line x1="200" y1="20" x2="200" y2="180" stroke="#475569" stroke-width="2"/>'
        f'<text x="320" y="200" font-family="sans-serif" font-size="12" fill="#334155">T (°C)</text>'
        f'<text x="155" y="30" font-family="sans-serif" font-size="12" fill="#334155">P (kPa)</text>'
        f'<line x1="200" y1="120" x2="330" y2="40" stroke="#ea580c" stroke-width="2.5"/>'
        f'<line x1="60" y1="180" x2="200" y2="120" stroke="#dc2626" stroke-width="2" stroke-dasharray="4"/>'
        f'<circle cx="60" cy="180" r="4" fill="#dc2626"/>'
        f'<circle cx="200" cy="120" r="4" fill="#ea580c"/>'
        f'<text x="40" y="205" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">-273°C</text>'
        f'<text x="205" y="125" font-family="sans-serif" font-size="11" fill="#ea580c">(0°C; {p0_kpa} kPa)</text>'
        f'<text x="70" y="145" font-family="sans-serif" font-size="10" fill="#dc2626">Extrapolation</text>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying graph showing the pressure of an enclosed gas (which has a pressure of ${p0_kpa}\\text{{ kPa}}$ at $0^\\circ\\text{{C}}$) "
        f"plotted against temperature in degrees Celsius ($^\\circ\\text{{C}}$).\n\n"
        f"1. Identify the temperature corresponding to the $x$-intercept where pressure extrapolates to zero.\n"
        f"2. Explain why gas pressure cannot be negative in the physical world."
    )
    ans = "1. -273 °C (absolute zero or 0 K). 2. Pressure is caused by collisions of moving particles. Since particles come to rest at absolute zero, collision rate reaches zero. There cannot be negative particle collisions, so pressure cannot be negative."
    memo = (
        "1. Temperature at intercept [2]: $-273^\\circ\\text{C}$ (absolute zero or $0\\text{ K}$) [2].\n"
        "2. Explanation [2]:\n"
        "   - Pressure arises from collisions of gas particles with the container walls ($P = \\frac{F}{A}$) [1].\n"
        "   - At absolute zero, all translational motion ceases, meaning collision frequency is zero. Negative collisions are physically impossible, so pressure cannot be less than zero [1]."
    )
    hints = {
        "tier_1": "The intercept is -273 °C.",
        "tier_2": "Pressure is wall collisions. You cannot have negative collisions.",
        "tier_3": "Intercept: -273 °C. Negative pressure is impossible because particles cannot have fewer than zero collisions.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "23_gay_lussacs_law_graph_p_vs_t_celsius",
        "learning_objective_id": "ps11_gay_lussac_graph_celsius",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": "Gay-Lussac P vs T(°C) Extrapolation to -273°C"},
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["absolute_zero_misunderstood", "negative_pressure_misconception"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Identify -273 °C absolute zero intercept", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Explain pressure as non-negative collision rate", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_24_tyre_pressure_highway_driving(rng: random.Random) -> Dict[str, Any]:
    p_cold = rng.choice([200.0, 210.0, 220.0, 230.0])  # kPa
    t_cold_c = rng.choice([15, 18, 20])
    t_hot_c = rng.choice([55, 60, 65, 70])
    t_cold_k = t_cold_c + 273
    t_hot_k = t_hot_c + 273
    # P_hot = (P_cold * T_hot_K) / T_cold_K
    p_hot = round((p_cold * t_hot_k) / t_cold_k, 1)
    diff = round(p_hot - p_cold, 1)
    qid = f"ps11_gas_24_{rng.randint(100000, 999999)}"

    prompt = (
        f"Before embarking on a long highway trip, a driver inflates their car tyres to a pressure of "
        f"${_fmt(p_cold)}\\text{{ kPa}}$ on a cold morning when the air temperature is ${t_cold_c}^\\circ\\text{{C}}$.\n"
        f"After driving at high speed on the highway, friction with the road increases the air temperature inside the tyres to ${t_hot_c}^\\circ\\text{{C}}$.\n"
        f"(Assume the tyre volume remains approximately constant).\n\n"
        f"1. Name the gas law that explains the pressure change inside the tyre.\n"
        f"2. Calculate the tyre pressure ($P_2$) after highway driving in $\\text{{kPa}}$.\n"
        f"3. Advise the driver why they should never deflate hot tyres to reach the recommended 'cold' pressure setting."
    )
    ans = f"1. Gay-Lussac's Law; 2. P_2 = {_fmt(p_hot)} kPa; 3. Deflating hot tyres leaves too little air mass; once the tyre cools, pressure drops dangerously below recommended levels."
    memo = (
        f"1. Gas law [1]: Gay-Lussac's Law (or Pressure Law) [1].\n"
        f"2. Calculation [3]:\n"
        f"   $$T_1 = {t_cold_c} + 273 = {_fmt(t_cold_k)}\\text{{ K}}, \\quad T_2 = {t_hot_c} + 273 = {_fmt(t_hot_k)}\\text{{ K}}$$ [1]\n"
        f"   $$\\frac{{P_1}}{{T_1}} = \\frac{{P_2}}{{T_2}} \\implies P_2 = \\frac{{{_fmt(p_cold)} \\times {_fmt(t_hot_k)}}}{{{_fmt(t_cold_k)}}} = {_fmt(p_hot)}\\text{{ kPa}}$$ [2]\n"
        f"3. Practical advice [2]: If air is bled from a hot tyre, the tyre will become under-inflated once it cools down back to ambient temperature [1], "
        f"which leads to dangerous handling, tyre wear, and increased risk of blowout [1]."
    )
    hints = {
        "tier_1": "Volume is constant: apply Gay-Lussac's Law P1/T1 = P2/T2.",
        "tier_2": f"T1 = {t_cold_k} K, T2 = {t_hot_k} K. Solve for P2.",
        "tier_3": f"P2 = ({p_cold} * {t_hot_k}) / {t_cold_k} = {_fmt(p_hot)} kPa. Never bleed hot tyres as they become under-inflated when cool.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "24_tyre_pressure_highway_driving",
        "learning_objective_id": "ps11_gay_lussac_tyre_app",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "term": 1,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["tyre_bleeding_misconception", "forgot_kelvin_conversion"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Identify Gay-Lussac's Law", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Convert temperatures to Kelvin", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Calculate final pressure", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Safety explanation against bleeding hot tyres", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_25_pressure_cooker_principles(rng: random.Random) -> Dict[str, Any]:
    p_cooker = rng.choice([150, 180, 200, 220])  # kPa
    t_boil = round(100 + (p_cooker - 101.3) * 0.28, 1)  # approx boiling temp
    qid = f"ps11_gas_25_{rng.randint(100000, 999999)}"

    prompt = (
        f"A domestic pressure cooker is a sealed rigid pot used to cook food rapidly.\n"
        f"When water boils inside the sealed cooker, trapped steam raises the internal pressure to ${_fmt(p_cooker)}\\text{{ kPa}}$.\n\n"
        f"1. Explain how the pressure cooker increases the boiling point of water inside the vessel.\n"
        f"2. Explain why food cooks substantially faster at this elevated pressure.\n"
        f"3. State what safety device prevents the pressure cooker from exploding if heated continuously."
    )
    ans = f"1. Boiling occurs when vapor pressure equals external pressure; higher sealed pressure forces the boiling point to rise above 100 °C (approx {_fmt(t_boil)} °C). 2. Food cooks at a higher temperature, transferring thermal energy more rapidly and accelerating chemical cooking reactions. 3. A weighted pressure relief safety valve."
    memo = (
        "1. Elevated boiling point [2]:\n"
        "   - A liquid boils when its saturated vapour pressure equals the external pressure acting upon its surface [1].\n"
        f"   - Since the sealed rigid cooker traps steam, the pressure rises to {_fmt(p_cooker)}\\text{{ kPa}}, which requires water to reach a much higher temperature (approx {_fmt(t_boil)}^\\circ\\text{{C}}) before vapour pressure equals chamber pressure [1].\n"
        "2. Faster cooking explanation [2]:\n"
        "   - Food is cooked at a higher temperature than $100^\\circ\\text{{C}}$ [1].\n"
        "   - Higher temperature increases the rate of heat transfer and significantly accelerates the chemical reactions of cooking [1].\n"
        "3. Safety mechanism [1]: A weighted pressure-release valve (or burst disk) that vents excess steam if pressure exceeds safe limits [1]."
    )
    hints = {
        "tier_1": "Boiling occurs when vapour pressure equals ambient pressure.",
        "tier_2": "Higher pressure forces boiling point higher. Higher temperature cooks food faster.",
        "tier_3": "1. Boiling point rises because vapor pressure must match higher chamber pressure. 2. Higher temp cooks food faster. 3. Pressure relief valve.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "25_pressure_cooker_principles",
        "learning_objective_id": "ps11_gay_lussac_pressure_cooker",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["boiling_point_definition_misunderstood", "pressure_temperature_cooking_confusion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of boiling point in relation to vapour pressure", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Higher cooking temperature accelerating cooking rate", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Pressure relief valve safety device", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


BUILDERS_01_25 = {
    "01_kinetic_molecular_theory_assumptions": build_01_kinetic_molecular_theory_assumptions,
    "02_gas_pressure_microscopic_interpretation": build_02_gas_pressure_microscopic_interpretation,
    "03_temperature_kelvin_conversion": build_03_temperature_kelvin_conversion,
    "04_pressure_units_conversion": build_04_pressure_units_conversion,
    "05_volume_units_conversion": build_05_volume_units_conversion,
    "06_boyles_law_definition_conditions": build_06_boyles_law_definition_conditions,
    "07_boyles_law_calculate_volume": build_07_boyles_law_calculate_volume,
    "08_boyles_law_calculate_pressure": build_08_boyles_law_calculate_pressure,
    "09_boyles_law_percentage_change": build_09_boyles_law_percentage_change,
    "10_boyles_law_graph_p_vs_v": build_10_boyles_law_graph_p_vs_v,
    "11_boyles_law_graph_p_vs_inv_v": build_11_boyles_law_graph_p_vs_inv_v,
    "12_boyles_law_graph_pv_vs_p": build_12_boyles_law_graph_pv_vs_p,
    "13_charles_law_definition_conditions": build_13_charles_law_definition_conditions,
    "14_charles_law_calculate_volume": build_14_charles_law_calculate_volume,
    "15_charles_law_calculate_temperature": build_15_charles_law_calculate_temperature,
    "16_charles_law_graph_v_vs_t_kelvin": build_16_charles_law_graph_v_vs_t_kelvin,
    "17_charles_law_graph_v_vs_t_celsius": build_17_charles_law_graph_v_vs_t_celsius,
    "18_charles_law_hot_air_balloon_density": build_18_charles_law_hot_air_balloon_density,
    "19_gay_lussacs_law_definition_conditions": build_19_gay_lussacs_law_definition_conditions,
    "20_gay_lussacs_law_calculate_pressure": build_20_gay_lussacs_law_calculate_pressure,
    "21_gay_lussacs_law_calculate_temperature": build_21_gay_lussacs_law_calculate_temperature,
    "22_gay_lussacs_law_graph_p_vs_t_kelvin": build_22_gay_lussacs_law_graph_p_vs_t_kelvin,
    "23_gay_lussacs_law_graph_p_vs_t_celsius": build_23_gay_lussacs_law_graph_p_vs_t_celsius,
    "24_tyre_pressure_highway_driving": build_24_tyre_pressure_highway_driving,
    "25_pressure_cooker_principles": build_25_pressure_cooker_principles,
}
