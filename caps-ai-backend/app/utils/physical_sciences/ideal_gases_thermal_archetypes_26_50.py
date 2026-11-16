"""Grade 11 Physical Sciences — Term 1 Chapter 7: Ideal Gases & Thermal Physics
Archetypes 26–50:
- 26–32: Combined / General Gas Equation (P1*V1/T1 = P2*V2/T2), STP Conversions, Subsea Bubbles, Connected Bulbs
- 33–41: Ideal Gas Equation (PV = nRT), Mass & Molar Mass (PV = (m/M)RT), Gas Density, Dalton's Partial Pressures
- 42–45: Avogadro's Hypothesis, Molar Volume at STP (Vm = 22,4 dm^3/mol), Gas Stoichiometry
- 46–50: Real vs Ideal Gas Deviations (High Pressure, Low Temperature, PV/nRT Graph) & Capstone Synthesis

All 25 builders strictly comply with:
- 6-Pillar Generator Contract
- Procedural determinism via rng: random.Random
- South African comma decimal separator ({,}) in KaTeX
- Valid inline vector SVGs in diagram_spec (never raw in question_text)
- Zero diagram description leaks
"""
from __future__ import annotations

import random
from typing import Any, Dict

R_GAS = 8.31  # J / (mol * K)
NA_CONST = 6.02e23


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
# 26–32: General Gas Equation (P1*V1/T1 = P2*V2/T2)
# ---------------------------------------------------------------------------


def build_26_general_gas_equation_derivation(rng: random.Random) -> Dict[str, Any]:
    gas_sample = rng.choice(["nitrogen (N2)", "oxygen (O2)", "helium (He)", "carbon dioxide (CO2)", "argon (Ar)"])
    n_moles = rng.choice([0.5, 1.0, 2.0, 2.5, 3.0])
    qid = f"ps11_gas_26_{rng.randint(100000, 999999)}"

    prompt = (
        f"Boyle's Law, Charles's Law, and Gay-Lussac's Law can be combined into a single General Gas Equation "
        f"for a fixed sample of {_fmt(n_moles)}\\text{{ mol}}$ of {gas_sample}.\n\n"
        f"1. Write down the General Gas Equation relating initial state $(P_1, V_1, T_1)$ and final state $(P_2, V_2, T_2)$.\n"
        f"2. Show how Boyle's Law, Charles's Law, and Gay-Lussac's Law are each obtained as special cases of this equation.\n"
        f"3. State the single condition that must remain constant for the General Gas Equation to hold."
    )
    ans = (
        "1. (P1*V1)/T1 = (P2*V2)/T2. "
        "2. At constant T (T1=T2), P1*V1 = P2*V2 (Boyle's Law); at constant P (P1=P2), V1/T1 = V2/T2 (Charles's Law); "
        "at constant V (V1=V2), P1/T1 = P2/T2 (Gay-Lussac's Law). "
        "3. The amount (mass or number of moles) of enclosed gas must remain constant."
    )
    memo = (
        "1. General Gas Equation [1]:\n"
        "   $$\\frac{P_1 V_1}{T_1} = \\frac{P_2 V_2}{T_2}$$ [1]\n"
        "2. Special cases [3]:\n"
        "   - Constant temperature ($T_1 = T_2$): cancels $T$ to give $P_1 V_1 = P_2 V_2$ (Boyle's Law) [1].\n"
        "   - Constant pressure ($P_1 = P_2$): cancels $P$ to give $\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$ (Charles's Law) [1].\n"
        "   - Constant volume ($V_1 = V_2$): cancels $V$ to give $\\frac{P_1}{T_1} = \\frac{P_2}{T_2}$ (Gay-Lussac's Law) [1].\n"
        "3. Constant condition [1]: Fixed mass / number of moles ($n$) of enclosed gas [1]."
    )
    hints = {
        "tier_1": "Combine P ∝ 1/V, V ∝ T, and P ∝ T into one equation.",
        "tier_2": "(P1 * V1) / T1 = (P2 * V2) / T2. Cancel whichever variable is held constant.",
        "tier_3": "General Gas Equation: P1V1/T1 = P2V2/T2 for a fixed amount (moles/mass) of gas.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "26_general_gas_equation_derivation",
        "learning_objective_id": "ps11_general_gas_eq_def",
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
        "misconception_tags": ["general_gas_equation_inversion", "failed_to_state_constant_variables"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "General Gas Equation formula", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Derivation of Boyle's, Charles's, Gay-Lussac's laws", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Constant mass/moles condition", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_27_general_gas_equation_solve_v2(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice([100.0, 120.0, 150.0, 180.0])  # kPa
    v1 = rng.choice([4.0, 5.0, 6.0, 8.0])  # dm^3
    t1_c = rng.choice([20, 25, 27])
    p2 = rng.choice([200.0, 240.0, 250.0, 300.0])  # kPa
    t2_c = rng.choice([77, 100, 127, 150])
    t1_k = t1_c + 273
    t2_k = t2_c + 273
    # V2 = (P1 * V1 * T2_K) / (P2 * T1_K)
    v2 = round((p1 * v1 * t2_k) / (p2 * t1_k), 2)
    qid = f"ps11_gas_27_{rng.randint(100000, 999999)}"

    prompt = (
        f"A sealed sample of gas occupies a volume of ${_fmt(v1)}\\text{{ dm}}^3$ at a pressure of ${_fmt(p1)}\\text{{ kPa}}$ "
        f"and a temperature of ${t1_c}^\\circ\\text{{C}}$.\n"
        f"The gas is simultaneously compressed to a pressure of ${_fmt(p2)}\\text{{ kPa}}$ and heated to ${t2_c}^\\circ\\text{{C}}$.\n\n"
        f"1. Convert both temperatures to Kelvin.\n"
        f"2. Calculate the final volume ($V_2$) of the gas in $\\text{{dm}}^3$."
    )
    ans = f"1. T_1 = {_fmt(t1_k)} K, T_2 = {_fmt(t2_k)} K; 2. V_2 = {_fmt(v2)} dm^3"
    memo = (
        f"1. Temperature conversions [2]:\n"
        f"   - $T_1 = {t1_c} + 273 = {_fmt(t1_k)}\\text{{ K}}$ [1]\n"
        f"   - $T_2 = {t2_c} + 273 = {_fmt(t2_k)}\\text{{ K}}$ [1]\n"
        f"2. General Gas Equation [3]:\n"
        f"   $$\\frac{{P_1 V_1}}{{T_1}} = \\frac{{P_2 V_2}}{{T_2}}$$ [M]\n"
        f"   $$\\frac{{({_fmt(p1)})({_fmt(v1)})}}{{{_fmt(t1_k)}}} = \\frac{{({_fmt(p2)}) V_2}}{{{_fmt(t2_k)}}}$$\n"
        f"   $$V_2 = \\frac{{{_fmt(p1)} \\times {_fmt(v1)} \\times {_fmt(t2_k)}}}{{{_fmt(p2)} \\times {_fmt(t1_k)}}} = {_fmt(v2)}\\text{{ dm}}^3$$ [A]"
    )
    hints = {
        "tier_1": "Use (P1 * V1) / T1 = (P2 * V2) / T2 with temperatures in Kelvin.",
        "tier_2": f"T1 = {t1_k} K, T2 = {t2_k} K. Solve V2 = (P1 * V1 * T2) / (P2 * T1).",
        "tier_3": f"V2 = ({p1} * {v1} * {t2_k}) / ({p2} * {t1_k}) = {_fmt(v2)} dm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "27_general_gas_equation_solve_v2",
        "learning_objective_id": "ps11_general_gas_v2",
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
        "misconception_tags": ["forgot_kelvin_conversion", "general_gas_equation_cross_multiplication_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert T1 and T2 to Kelvin", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "General gas equation substitution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct final volume with units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_28_general_gas_equation_solve_p2(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice([100.0, 101.3])  # kPa at ground level
    v1 = rng.choice([120.0, 150.0, 200.0])  # dm^3
    t1_c = rng.choice([20, 25, 27])
    v2 = rng.choice([300.0, 400.0, 500.0])  # dm^3 high altitude
    t2_c = rng.choice([-33, -23, -13, -3])  # upper atmosphere cold
    t1_k = t1_c + 273
    t2_k = t2_c + 273
    # P2 = (P1 * V1 * T2_K) / (V2 * T1_K)
    p2 = round((p1 * v1 * t2_k) / (v2 * t1_k), 2)
    qid = f"ps11_gas_28_{rng.randint(100000, 999999)}"

    prompt = (
        f"A meteorological weather balloon is filled with ${_fmt(v1)}\\text{{ dm}}^3$ of helium at ground level, "
        f"where the atmospheric pressure is ${_fmt(p1)}\\text{{ kPa}}$ and the temperature is ${t1_c}^\\circ\\text{{C}}$.\n"
        f"As the balloon ascends into the stratosphere, the temperature drops to ${t2_c}^\\circ\\text{{C}}$ "
        f"and the balloon expands to a volume of ${_fmt(v2)}\\text{{ dm}}^3$.\n\n"
        f"Calculate the atmospheric pressure ($P_2$) in $\\text{{kPa}}$ at this altitude."
    )
    ans = f"P_2 = {_fmt(p2)} kPa"
    memo = (
        f"1. Convert temperatures to Kelvin [2]:\n"
        f"   - $T_1 = {t1_c} + 273 = {_fmt(t1_k)}\\text{{ K}}$ [1]\n"
        f"   - $T_2 = {t2_c} + 273 = {_fmt(t2_k)}\\text{{ K}}$ [1]\n"
        f"2. Apply the General Gas Equation [3]:\n"
        f"   $$\\frac{{P_1 V_1}}{{T_1}} = \\frac{{P_2 V_2}}{{T_2}}$$ [M]\n"
        f"   $$\\frac{{({_fmt(p1)})({_fmt(v1)})}}{{{_fmt(t1_k)}}} = \\frac{{P_2 ({_fmt(v2)})}}{{{_fmt(t2_k)}}}$$\n"
        f"   $$P_2 = \\frac{{{_fmt(p1)} \\times {_fmt(v1)} \\times {_fmt(t2_k)}}}{{{_fmt(v2)} \\times {_fmt(t1_k)}}} = {_fmt(p2)}\\text{{ kPa}}$$ [A]"
    )
    hints = {
        "tier_1": "Convert both temperatures (including negative Celsius!) to Kelvin (+273).",
        "tier_2": f"T1 = {t1_k} K, T2 = {t2_k} K. Solve P2 = (P1 * V1 * T2) / (V2 * T1).",
        "tier_3": f"P2 = ({p1} * {v1} * {t2_k}) / ({v2} * {t1_k}) = {_fmt(p2)} kPa.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "28_general_gas_equation_solve_p2",
        "learning_objective_id": "ps11_general_gas_p2",
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
        "misconception_tags": ["forgot_kelvin_conversion", "negative_celsius_kelvin_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert T1 and T2 to Kelvin", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "General gas equation substitution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct final pressure with units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_29_general_gas_equation_solve_t2(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice([100.0, 120.0, 150.0])  # kPa
    v1 = rng.choice([2.0, 3.0, 4.0])  # dm^3
    t1_c = rng.choice([20, 27])
    p2 = rng.choice([200.0, 250.0, 300.0])  # kPa
    v2 = rng.choice([3.0, 4.5, 6.0])  # dm^3
    t1_k = t1_c + 273
    # T2_K = (P2 * V2 * T1_K) / (P1 * V1)
    t2_k = round((p2 * v2 * t1_k) / (p1 * v1), 1)
    t2_c = round(t2_k - 273, 1)
    qid = f"ps11_gas_29_{rng.randint(100000, 999999)}"

    prompt = (
        f"An enclosed mass of gas occupies ${_fmt(v1)}\\text{{ dm}}^3$ at ${_fmt(p1)}\\text{{ kPa}}$ and ${t1_c}^\\circ\\text{{C}}$.\n"
        f"The conditions are changed until the volume is ${_fmt(v2)}\\text{{ dm}}^3$ at a pressure of ${_fmt(p2)}\\text{{ kPa}}$.\n\n"
        f"Calculate the final temperature ($T_2$) of the gas in both Kelvin ($\\text{{K}}$) and degrees Celsius ($^\\circ\\text{{C}}$)."
    )
    ans = f"T_2 = {_fmt(t2_k)} K = {_fmt(t2_c)} °C"
    memo = (
        f"1. Initial temperature in Kelvin [1]:\n"
        f"   $$T_1 = {t1_c} + 273 = {_fmt(t1_k)}\\text{{ K}}$$ [1]\n"
        f"2. General Gas Equation [3]:\n"
        f"   $$\\frac{{P_1 V_1}}{{T_1}} = \\frac{{P_2 V_2}}{{T_2}}$$ [M]\n"
        f"   $$\\frac{{({_fmt(p1)})({_fmt(v1)})}}{{{_fmt(t1_k)}}} = \\frac{{({_fmt(p2)})({_fmt(v2)})}}{{T_2}}$$\n"
        f"   $$T_2 = \\frac{{{_fmt(p2)} \\times {_fmt(v2)} \\times {_fmt(t1_k)}}}{{{_fmt(p1)} \\times {_fmt(v1)}}} = {_fmt(t2_k)}\\text{{ K}}$$ [2]\n"
        f"3. Convert to Celsius [1]:\n"
        f"   $$T_2(^\\circ\\text{{C}}) = {_fmt(t2_k)} - 273 = {_fmt(t2_c)}^\\circ\\text{{C}}$$ [A]"
    )
    hints = {
        "tier_1": "Use (P1 * V1) / T1 = (P2 * V2) / T2.",
        "tier_2": f"T1 = {t1_k} K. Solve T2 = (P2 * V2 * T1) / (P1 * V1).",
        "tier_3": f"T2 = {_fmt(t2_k)} K = {_fmt(t2_c)} °C.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "29_general_gas_equation_solve_t2",
        "learning_objective_id": "ps11_general_gas_t2",
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
        "misconception_tags": ["forgot_kelvin_conversion", "celsius_to_kelvin_inversion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert T1 to Kelvin", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "General gas equation substitution and T2 in K", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Convert T2 to Celsius", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_30_gas_volume_converted_to_stp(rng: random.Random) -> Dict[str, Any]:
    v1_cm3 = rng.choice([250.0, 400.0, 500.0, 600.0, 800.0])
    p1_kpa = rng.choice([95.0, 98.0, 105.0, 110.0, 120.0])
    t1_c = rng.choice([20, 25, 30, 35])
    t1_k = t1_c + 273
    p_stp = 101.3
    t_stp = 273
    # V_stp = (P1 * V1 * T_stp) / (P_stp * T1_K)
    v_stp_cm3 = round((p1_kpa * v1_cm3 * t_stp) / (p_stp * t1_k), 1)
    qid = f"ps11_gas_30_{rng.randint(100000, 999999)}"

    prompt = (
        f"During a laboratory reaction, ${_fmt(v1_cm3)}\\text{{ cm}}^3$ of oxygen gas is collected at a laboratory pressure "
        f"of ${_fmt(p1_kpa)}\\text{{ kPa}}$ and temperature of ${t1_c}^\\circ\\text{{C}}$.\n\n"
        f"1. State the standard values of temperature (in $\\text{{K}}$) and pressure (in $\\text{{kPa}}$) at STP.\n"
        f"2. Calculate the volume that this gas sample would occupy at STP in $\\text{{cm}}^3$."
    )
    ans = f"1. T_STP = 273 K (0 °C), P_STP = 101,3 kPa; 2. V_STP = {_fmt(v_stp_cm3)} cm^3"
    memo = (
        f"1. STP values [2]: Standard temperature $T_2 = 273\\text{{ K}}$ ($0^\\circ\\text{{C}}$) [1]; "
        f"Standard pressure $P_2 = 101{{,}}3\\text{{ kPa}}$ ($1{{,}}013 \\times 10^5\\text{{ Pa}}$) [1].\n"
        f"2. Volume at STP [3]:\n"
        f"   $$T_1 = {t1_c} + 273 = {_fmt(t1_k)}\\text{{ K}}$$\n"
        f"   $$\\frac{{P_1 V_1}}{{T_1}} = \\frac{{P_2 V_2}}{{T_2}} \\implies \\frac{{({_fmt(p1_kpa)})({_fmt(v1_cm3)})}}{{{_fmt(t1_k)}}} = \\frac{{(101{{,}}3) V_2}}{{273}}$$ [M]\n"
        f"   $$V_2 = \\frac{{{_fmt(p1_kpa)} \\times {_fmt(v1_cm3)} \\times 273}}{{101{{,}}3 \\times {_fmt(t1_k)}}} = {_fmt(v_stp_cm3)}\\text{{ cm}}^3$$ [A]"
    )
    hints = {
        "tier_1": "STP means T2 = 273 K and P2 = 101,3 kPa.",
        "tier_2": f"Convert T1 = {t1_k} K. Apply (P1 * V1) / T1 = (101,3 * V2) / 273.",
        "tier_3": f"V2 = {_fmt(v_stp_cm3)} cm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "30_gas_volume_converted_to_stp",
        "learning_objective_id": "ps11_general_gas_stp_conv",
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
        "misconception_tags": ["stp_values_confused_with_room_temp", "forgot_kelvin_conversion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "State standard temperature and pressure at STP", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "General gas equation substitution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct STP volume", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_31_underwater_diver_bubble_expansion(rng: random.Random) -> Dict[str, Any]:
    p1_kpa = rng.choice([300.0, 400.0, 500.0])  # deep water pressure
    v1_cm3 = rng.choice([2.0, 3.0, 4.0, 5.0])
    t1_c = rng.choice([7, 10, 12])  # cold deep water
    p2_kpa = 101.3  # surface
    t2_c = rng.choice([22, 25, 27])  # warm surface water
    t1_k = t1_c + 273
    t2_k = t2_c + 273
    v2_cm3 = round((p1_kpa * v1_cm3 * t2_k) / (p2_kpa * t1_k), 2)
    qid = f"ps11_gas_31_{rng.randint(100000, 999999)}"

    prompt = (
        f"A scuba diver at the bottom of a deep lake releases an air bubble of volume ${_fmt(v1_cm3)}\\text{{ cm}}^3$, "
        f"where the total hydrostatic pressure is ${_fmt(p1_kpa)}\\text{{ kPa}}$ and the water temperature is ${t1_c}^\\circ\\text{{C}}$.\n"
        f"The bubble rises to the surface, where atmospheric pressure is $101{{,}}3\\text{{ kPa}}$ and the surface water temperature is ${t2_c}^\\circ\\text{{C}}$.\n\n"
        f"1. State TWO physical reasons why the air bubble expands as it rises to the surface.\n"
        f"2. Calculate the volume ($V_2$) of the air bubble just as it reaches the surface in $\\text{{cm}}^3$."
    )
    ans = f"1. Hydrostatic pressure decreases as depth decreases, and water temperature increases near the surface. 2. V_2 = {_fmt(v2_cm3)} cm^3"
    memo = (
        f"1. Two reasons for expansion [2]:\n"
        f"   - External water pressure decreases as the bubble rises ($V \\propto \\frac{{1}}{{P}}$) [1].\n"
        f"   - Water temperature increases from ${t1_c}^\\circ\\text{{C}}$ to ${t2_c}^\\circ\\text{{C}}$ ($V \\propto T$) [1].\n"
        f"2. Calculation [3]:\n"
        f"   $$T_1 = {t1_c} + 273 = {_fmt(t1_k)}\\text{{ K}}, \\quad T_2 = {t2_c} + 273 = {_fmt(t2_k)}\\text{{ K}}$$ [1]\n"
        f"   $$\\frac{{P_1 V_1}}{{T_1}} = \\frac{{P_2 V_2}}{{T_2}} \\implies V_2 = \\frac{{{_fmt(p1_kpa)} \\times {_fmt(v1_cm3)} \\times {_fmt(t2_k)}}}{{101{{,}}3 \\times {_fmt(t1_k)}}} = {_fmt(v2_cm3)}\\text{{ cm}}^3$$ [2]"
    )
    hints = {
        "tier_1": "Both pressure and temperature change as the bubble rises: use P1V1/T1 = P2V2/T2.",
        "tier_2": f"T1 = {t1_k} K, T2 = {t2_k} K. Solve for V2.",
        "tier_3": f"V2 = ({p1_kpa} * {v1_cm3} * {t2_k}) / (101,3 * {t1_k}) = {_fmt(v2_cm3)} cm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "31_underwater_diver_bubble_expansion",
        "learning_objective_id": "ps11_diver_bubble_expansion",
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
        "misconception_tags": ["forgot_kelvin_conversion", "hydrostatic_pressure_depth_confusion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Two reasons for bubble expansion (lower P, higher T)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Kelvin conversions", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Calculate final bubble volume", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_32_two_connected_bulbs_isothermal(rng: random.Random) -> Dict[str, Any]:
    v_a = rng.choice([2.0, 3.0, 4.0])  # dm^3
    p_a = rng.choice([150.0, 200.0, 300.0])  # kPa
    v_b = rng.choice([1.0, 2.0, 4.0, 6.0])  # dm^3 (evacuated or with gas)
    # Assume Bulb B is initially evacuated (P_B = 0)
    v_tot = v_a + v_b
    p_final = round((p_a * v_a) / v_tot, 1)
    qid = f"ps11_gas_32_{rng.randint(100000, 999999)}"

    svg_inner = (
        f'<circle cx="110" cy="120" r="55" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5"/>'
        f'<circle cx="270" cy="120" r="45" fill="#f8fafc" stroke="#64748b" stroke-width="2.5"/>'
        f'<rect x="165" y="114" width="60" height="12" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>'
        f'<line x1="195" y1="100" x2="195" y2="140" stroke="#dc2626" stroke-width="3"/>'
        f'<text x="195" y="92" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Tap T</text>'
        f'<text x="110" y="110" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e40af">Bulb A</text>'
        f'<text x="110" y="128" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#1e40af">V = {_fmt(v_a)} dm³</text>'
        f'<text x="110" y="144" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#1e40af">P = {_fmt(p_a)} kPa</text>'
        f'<text x="270" y="115" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#334155">Bulb B</text>'
        f'<text x="270" y="132" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#334155">V = {_fmt(v_b)} dm³</text>'
        f'<text x="270" y="148" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#64748b">(Vacuum)</text>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying apparatus consisting of two rigid glass bulbs, A and B, connected by a narrow tube "
        f"of negligible volume with a closed tap T.\n"
        f"Bulb A has a volume of ${_fmt(v_a)}\\text{{ dm}}^3$ and contains an ideal gas at a pressure of ${_fmt(p_a)}\\text{{ kPa}}$.\n"
        f"Bulb B has a volume of ${_fmt(v_b)}\\text{{ dm}}^3$ and is completely evacuated (vacuum).\n\n"
        f"Tap T is opened while the temperature of the entire apparatus is maintained constant.\n"
        f"1. State the total final volume ($V_2$) occupied by the gas after the tap is opened.\n"
        f"2. Calculate the final equilibrium pressure ($P_2$) inside the connected bulbs in $\\text{{kPa}}$."
    )
    ans = f"1. V_2 = {_fmt(v_tot)} dm^3; 2. P_2 = {_fmt(p_final)} kPa"
    memo = (
        f"1. Total final volume [1]:\n"
        f"   $$V_2 = V_A + V_B = {_fmt(v_a)} + {_fmt(v_b)} = {_fmt(v_tot)}\\text{{ dm}}^3$$ [1]\n"
        f"2. Boyle's Law calculation [3]:\n"
        f"   $$P_1 V_1 = P_2 V_2$$ [M]\n"
        f"   $$({_fmt(p_a)})({_fmt(v_a)}) = P_2 ({_fmt(v_tot)})$$\n"
        f"   $$P_2 = \\frac{{{_fmt(p_a)} \\times {_fmt(v_a)}}}{{{_fmt(v_tot)}}} = {_fmt(p_final)}\\text{{ kPa}}$$ [A]"
    )
    hints = {
        "tier_1": "When the tap opens, the gas expands to fill both Bulb A and Bulb B: V2 = VA + VB.",
        "tier_2": f"V2 = {_fmt(v_tot)} dm^3. Apply Boyle's Law P1*V1 = P2*V2.",
        "tier_3": f"P2 = ({p_a} * {v_a}) / {_fmt(v_tot)} = {_fmt(p_final)} kPa.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "32_two_connected_bulbs_isothermal",
        "learning_objective_id": "ps11_connected_bulbs_boyle",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Connected Gas Bulbs A ({_fmt(v_a)} dm³) & B ({_fmt(v_b)} dm³)"},
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["forgot_to_add_bulb_volumes", "boyles_law_proportionality_inversion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Total volume V2 = VA + VB", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Boyle's Law substitution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct final pressure", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ---------------------------------------------------------------------------
# 33–41: Ideal Gas Equation (PV = nRT) & Density / Partial Pressures
# ---------------------------------------------------------------------------


def build_33_ideal_gas_law_solve_pressure(rng: random.Random) -> Dict[str, Any]:
    n_mol = rng.choice([0.5, 1.2, 2.0, 2.5, 3.5, 4.0])
    v_dm3 = rng.choice([10.0, 15.0, 20.0, 25.0, 50.0])
    v_m3 = v_dm3 / 1000.0
    t_c = rng.choice([20, 25, 27, 37, 50])
    t_k = t_c + 273
    # P = (n * R * T) / V
    p_pa = (n_mol * R_GAS * t_k) / v_m3
    p_kpa = round(p_pa / 1000.0, 1)
    qid = f"ps11_gas_33_{rng.randint(100000, 999999)}"

    prompt = (
        f"A rigid gas cylinder of volume ${_fmt(v_dm3)}\\text{{ dm}}^3$ contains ${_fmt(n_mol)}\\text{{ mol}}$ of an ideal gas "
        f"at a temperature of ${t_c}^\\circ\\text{{C}}$.\n"
        f"(Universal gas constant $R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"1. Convert the volume to SI units ($\\text{{m}}^3$) and temperature to Kelvin ($\\text{{K}}$).\n"
        f"2. Calculate the pressure ($P$) exerted by the gas in kilopascals ($\\text{{kPa}}$)."
    )
    ans = f"1. V = {v_m3:.3f} m^3, T = {_fmt(t_k)} K; 2. P = {_fmt(p_kpa)} kPa"
    memo = (
        f"1. SI conversions [2]:\n"
        f"   - $V = \\frac{{{_fmt(v_dm3)}}}{{1000}} = {v_m3:.3f}\\text{{ m}}^3$ [1]\n"
        f"   - $T = {t_c} + 273 = {_fmt(t_k)}\\text{{ K}}$ [1]\n"
        f"2. Ideal Gas Equation [3]:\n"
        f"   $$PV = nRT$$ [M]\n"
        f"   $$P({v_m3:.3f}) = ({_fmt(n_mol)})(8{{,}}31)({_fmt(t_k)})$$\n"
        f"   $$P = \\frac{{{_fmt(n_mol)} \\times 8{{,}}31 \\times {_fmt(t_k)}}}{{{v_m3:.3f}}} = {_fmt(round(p_pa))}\\text{{ Pa}} = {_fmt(p_kpa)}\\text{{ kPa}}$$ [A]"
    )
    hints = {
        "tier_1": "In PV = nRT, V must be in m^3 and T in K.",
        "tier_2": f"V = {v_m3:.3f} m^3, T = {t_k} K. Solve P = (n * R * T) / V in Pa, then divide by 1000 for kPa.",
        "tier_3": f"P = {_fmt(p_kpa)} kPa.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "33_ideal_gas_law_solve_pressure",
        "learning_objective_id": "ps11_ideal_gas_solve_p",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["volume_dm3_m3_conversion_error", "forgot_kelvin_conversion", "pressure_kpa_pa_unit_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert V to m^3 and T to K", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "PV = nRT substitution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct pressure in kPa", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_34_ideal_gas_law_solve_volume(rng: random.Random) -> Dict[str, Any]:
    n_mol = rng.choice([0.8, 1.5, 2.0, 3.0, 5.0])
    p_kpa = rng.choice([100.0, 120.0, 150.0, 200.0])
    p_pa = p_kpa * 1000.0
    t_c = rng.choice([25, 27, 40, 60])
    t_k = t_c + 273
    # V_m3 = (n * R * T) / P_pa
    v_m3 = (n_mol * R_GAS * t_k) / p_pa
    v_dm3 = round(v_m3 * 1000.0, 2)
    qid = f"ps11_gas_34_{rng.randint(100000, 999999)}"

    prompt = (
        f"Calculate the volume (in $\\text{{dm}}^3$) occupied by ${_fmt(n_mol)}\\text{{ mol}}$ of an ideal gas "
        f"at a pressure of ${_fmt(p_kpa)}\\text{{ kPa}}$ and a temperature of ${t_c}^\\circ\\text{{C}}$.\n"
        f"($R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$)."
    )
    ans = f"V = {_fmt(v_dm3)} dm^3 (or {_fmt(v_m3, 4)} m^3)"
    memo = (
        f"1. SI conversions [2]:\n"
        f"   - $P = {_fmt(p_kpa)} \\times 10^3 = {_fmt(int(p_pa))}\\text{{ Pa}}$ [1]\n"
        f"   - $T = {t_c} + 273 = {_fmt(t_k)}\\text{{ K}}$ [1]\n"
        f"2. Ideal Gas Equation [3]:\n"
        f"   $$PV = nRT \\implies ({_fmt(int(p_pa))}) V = ({_fmt(n_mol)})(8{{,}}31)({_fmt(t_k)})$$ [M]\n"
        f"   $$V = \\frac{{{_fmt(n_mol)} \\times 8{{,}}31 \\times {_fmt(t_k)}}}{{{_fmt(int(p_pa))}}} = {_fmt(v_m3, 4)}\\text{{ m}}^3 = {_fmt(v_dm3)}\\text{{ dm}}^3$$ [A]"
    )
    hints = {
        "tier_1": "Convert P to Pa (*1000) and T to K (+273).",
        "tier_2": f"V(m^3) = (n * R * T) / P. Multiply by 1000 to convert m^3 to dm^3.",
        "tier_3": f"V = {_fmt(v_dm3)} dm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "34_ideal_gas_law_solve_volume",
        "learning_objective_id": "ps11_ideal_gas_solve_v",
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
        "misconception_tags": ["pressure_kpa_pa_unit_error", "volume_dm3_m3_conversion_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert P to Pa and T to K", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "PV = nRT substitution and V in m^3", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Convert V to dm^3", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_35_ideal_gas_law_solve_moles(rng: random.Random) -> Dict[str, Any]:
    p_kpa = rng.choice([101.3, 150.0, 200.0, 250.0])
    p_pa = p_kpa * 1000.0
    v_dm3 = rng.choice([12.0, 24.0, 30.0, 45.0])
    v_m3 = v_dm3 / 1000.0
    t_c = rng.choice([20, 25, 27])
    t_k = t_c + 273
    n_mol = round((p_pa * v_m3) / (R_GAS * t_k), 3)
    n_particles_coeff = round(n_mol * 6.02, 2)
    qid = f"ps11_gas_35_{rng.randint(100000, 999999)}"

    prompt = (
        f"A sealed vessel of volume ${_fmt(v_dm3)}\\text{{ dm}}^3$ holds helium gas at a pressure of ${_fmt(p_kpa)}\\text{{ kPa}}$ "
        f"and temperature of ${t_c}^\\circ\\text{{C}}$.\n"
        f"($R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$, $N_A = 6{{,}}02 \\times 10^{{23}}\\text{{ mol}}^{{-1}}$).\n\n"
        f"1. Calculate the number of moles ($n$) of helium in the vessel.\n"
        f"2. Calculate the number of helium atoms ($N$) inside the vessel."
    )
    ans = f"1. n = {_fmt(n_mol, 3)} mol; 2. N = {_fmt(n_particles_coeff)} x 10^23 atoms"
    memo = (
        f"1. Number of moles [4]:\n"
        f"   - $P = {_fmt(p_kpa)} \\times 10^3 = {_fmt(int(p_pa))}\\text{{ Pa}}$, $V = \\frac{{{_fmt(v_dm3)}}}{{1000}} = {v_m3:.3f}\\text{{ m}}^3$, $T = {t_c} + 273 = {_fmt(t_k)}\\text{{ K}}$ [2]\n"
        f"   - $PV = nRT \\implies n = \\frac{{PV}}{{RT}} = \\frac{{({_fmt(int(p_pa))})({v_m3:.3f})}}{{(8{{,}}31)({_fmt(t_k)})}} = {_fmt(n_mol, 3)}\\text{{ mol}}$ [2]\n"
        f"2. Number of atoms [2]:\n"
        f"   $$N = n \\times N_A = {_fmt(n_mol, 3)} \\times 6{{,}}02 \\times 10^{{23}} = {_fmt(n_particles_coeff)} \\times 10^{{23}}\\text{{ atoms}}$$ [2]"
    )
    hints = {
        "tier_1": "Use n = PV / (RT) with P in Pa, V in m^3, T in K. Then N = n * NA.",
        "tier_2": f"P*V = {_fmt(p_kpa * v_dm3)} J. Divide by (8,31 * {t_k}).",
        "tier_3": f"n = {_fmt(n_mol, 3)} mol. N = {_fmt(n_particles_coeff)} x 10^23 atoms.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "35_ideal_gas_law_solve_moles",
        "learning_objective_id": "ps11_ideal_gas_solve_n",
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
        "misconception_tags": ["volume_dm3_m3_conversion_error", "avogadro_number_multiplication_error"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "SI conversions for P, V, T", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Calculate moles n = PV/RT", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Calculate number of atoms N = n * NA", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_36_ideal_gas_law_solve_temperature(rng: random.Random) -> Dict[str, Any]:
    n_mol = rng.choice([0.5, 1.0, 1.5, 2.0])
    v_dm3 = rng.choice([10.0, 15.0, 20.0])
    v_m3 = v_dm3 / 1000.0
    p_kpa = rng.choice([125.0, 150.0, 200.0, 250.0])
    p_pa = p_kpa * 1000.0
    # T_K = (P * V) / (n * R)
    t_k = round((p_pa * v_m3) / (n_mol * R_GAS), 1)
    t_c = round(t_k - 273, 1)
    qid = f"ps11_gas_36_{rng.randint(100000, 999999)}"

    prompt = (
        f"A container of volume ${_fmt(v_dm3)}\\text{{ dm}}^3$ holds ${_fmt(n_mol)}\\text{{ mol}}$ of argon gas at a pressure of ${_fmt(p_kpa)}\\text{{ kPa}}$.\n"
        f"($R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"Calculate the temperature of the gas in Kelvin ($\\text{{K}}$) and in degrees Celsius ($^\\circ\\text{{C}}$)."
    )
    ans = f"T = {_fmt(t_k)} K = {_fmt(t_c)} °C"
    memo = (
        f"1. SI conversions [2]:\n"
        f"   - $P = {_fmt(p_kpa)} \\times 10^3 = {_fmt(int(p_pa))}\\text{{ Pa}}$ [1]\n"
        f"   - $V = \\frac{{{_fmt(v_dm3)}}}{{1000}} = {v_m3:.3f}\\text{{ m}}^3$ [1]\n"
        f"2. Ideal Gas Equation [3]:\n"
        f"   $$PV = nRT \\implies T = \\frac{{PV}}{{nR}} = \\frac{{({_fmt(int(p_pa))})({v_m3:.3f})}}{{({_fmt(n_mol)})(8{{,}}31)}} = {_fmt(t_k)}\\text{{ K}}$$ [2]\n"
        f"   $$T(^\\circ\\text{{C}}) = {_fmt(t_k)} - 273 = {_fmt(t_c)}^\\circ\\text{{C}}$$ [1]"
    )
    hints = {
        "tier_1": "Use T = PV / (nR) with P in Pa and V in m^3.",
        "tier_2": f"T(K) = ({int(p_pa)} * {v_m3:.3f}) / ({n_mol} * 8,31). Subtract 273 for °C.",
        "tier_3": f"T = {_fmt(t_k)} K = {_fmt(t_c)} °C.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "36_ideal_gas_law_solve_temperature",
        "learning_objective_id": "ps11_ideal_gas_solve_t",
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
        "misconception_tags": ["pressure_kpa_pa_unit_error", "volume_dm3_m3_conversion_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "SI conversions for P and V", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Solve T in Kelvin", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Convert T to Celsius", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_37_ideal_gas_law_from_mass(rng: random.Random) -> Dict[str, Any]:
    gas_name, m_molar = rng.choice([
        ("oxygen (O2)", 32.0),
        ("nitrogen (N2)", 28.0),
        ("carbon dioxide (CO2)", 44.0),
        ("methane (CH4)", 16.0),
    ])
    mass_g = rng.choice([16.0, 28.0, 32.0, 44.0, 56.0, 64.0, 88.0])
    n_mol = round(mass_g / m_molar, 3)
    v_dm3 = rng.choice([10.0, 20.0, 25.0])
    v_m3 = v_dm3 / 1000.0
    t_c = rng.choice([25, 27, 30])
    t_k = t_c + 273
    p_pa = (n_mol * R_GAS * t_k) / v_m3
    p_kpa = round(p_pa / 1000.0, 1)
    qid = f"ps11_gas_37_{rng.randint(100000, 999999)}"

    prompt = (
        f"A sealed tank of volume ${_fmt(v_dm3)}\\text{{ dm}}^3$ contains ${_fmt(mass_g)}\\text{{ g}}$ of {gas_name} "
        f"at ${t_c}^\\circ\\text{{C}}$.\n"
        f"(Molar mass $M = {_fmt(m_molar)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, $R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"1. Calculate the number of moles ($n$) of {gas_name}.\n"
        f"2. Calculate the pressure ($P$) inside the tank in $\\text{{kPa}}$."
    )
    ans = f"1. n = {_fmt(n_mol, 3)} mol; 2. P = {_fmt(p_kpa)} kPa"
    memo = (
        f"1. Moles calculation [2]:\n"
        f"   $$n = \\frac{{m}}{{M}} = \\frac{{{_fmt(mass_g)}}}{{{_fmt(m_molar)}}} = {_fmt(n_mol, 3)}\\text{{ mol}}$$ [2]\n"
        f"2. Ideal Gas Equation [4]:\n"
        f"   - $V = {v_m3:.3f}\\text{{ m}}^3$, $T = {t_c} + 273 = {_fmt(t_k)}\\text{{ K}}$ [1]\n"
        f"   - $PV = nRT \\implies P = \\frac{{nRT}}{{V}} = \\frac{{({_fmt(n_mol, 3)})(8{{,}}31)({_fmt(t_k)})}}{{{v_m3:.3f}}} = {_fmt(round(p_pa))}\\text{{ Pa}} = {_fmt(p_kpa)}\\text{{ kPa}}$ [3]"
    )
    hints = {
        "tier_1": "First find n = m / M. Then apply PV = nRT.",
        "tier_2": f"n = {mass_g} / {m_molar} = {_fmt(n_mol, 3)} mol. Convert V to m^3 and T to K.",
        "tier_3": f"P = {_fmt(p_kpa)} kPa.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "37_ideal_gas_law_from_mass",
        "learning_objective_id": "ps11_ideal_gas_from_mass",
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
        "misconception_tags": ["diatomic_molar_mass_halved", "volume_dm3_m3_conversion_error"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Calculate moles n = m/M", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "SI conversions for V and T", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "PV = nRT substitution and final pressure in kPa", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_38_ideal_gas_law_molar_mass_determination(rng: random.Random) -> Dict[str, Any]:
    gas_formula, true_m = rng.choice([
        ("CH4 (methane)", 16.0),
        ("N2 (nitrogen)", 28.0),
        ("O2 (oxygen)", 32.0),
        ("CO2 (carbon dioxide)", 44.0),
        ("SO2 (sulfur dioxide)", 64.0),
    ])
    n_mol = rng.choice([0.25, 0.50, 0.75])
    mass_g = round(n_mol * true_m, 2)
    v_dm3 = rng.choice([5.0, 10.0, 12.0])
    v_m3 = v_dm3 / 1000.0
    t_c = rng.choice([25, 27])
    t_k = t_c + 273
    p_pa = (n_mol * R_GAS * t_k) / v_m3
    p_kpa = round(p_pa / 1000.0, 2)
    qid = f"ps11_gas_38_{rng.randint(100000, 999999)}"

    prompt = (
        f"An unknown pure gas of mass ${_fmt(mass_g)}\\text{{ g}}$ occupies a volume of ${_fmt(v_dm3)}\\text{{ dm}}^3$ "
        f"at a pressure of ${_fmt(p_kpa)}\\text{{ kPa}}$ and temperature of ${t_c}^\\circ\\text{{C}}$.\n"
        f"($R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"1. Calculate the number of moles ($n$) of the gas sample.\n"
        f"2. Calculate the molar mass ($M$) of the unknown gas in $\\text{{g}}\\cdot\\text{{mol}}^{{-1}}$.\n"
        f"3. Identify the unknown gas from the following candidates: $\\text{{CH}}_4\\ (16)$, $\\text{{N}}_2\\ (28)$, "
        f"$\\text{{O}}_2\\ (32)$, $\\text{{CO}}_2\\ (44)$, $\\text{{SO}}_2\\ (64)$."
    )
    ans = f"1. n = {_fmt(n_mol)} mol; 2. M = {_fmt(true_m)} g/mol; 3. {gas_formula}"
    memo = (
        f"1. Number of moles [3]:\n"
        f"   $$n = \\frac{{PV}}{{RT}} = \\frac{{({_fmt(p_kpa)} \\times 10^3)({v_m3:.3f})}}{{(8{{,}}31)({t_k})}} = {_fmt(n_mol)}\\text{{ mol}}$$ [3]\n"
        f"2. Molar mass [2]:\n"
        f"   $$M = \\frac{{m}}{{n}} = \\frac{{{_fmt(mass_g)}}}{{{_fmt(n_mol)}}} = {_fmt(true_m)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$$ [2]\n"
        f"3. Identification [1]: The gas is {gas_formula} [1]."
    )
    hints = {
        "tier_1": "Find n = PV / (RT), then calculate M = m / n.",
        "tier_2": f"n = {_fmt(n_mol)} mol. M = {mass_g} / {n_mol}.",
        "tier_3": f"M = {_fmt(true_m)} g/mol -> {gas_formula}.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "38_ideal_gas_law_molar_mass_determination",
        "learning_objective_id": "ps11_ideal_gas_molar_mass",
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
        "misconception_tags": ["molar_mass_inversion_n_over_m", "volume_dm3_m3_conversion_error"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Calculate moles n = PV/RT", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Calculate molar mass M = m/n", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Identify unknown gas formula", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_39_gas_density_calculation(rng: random.Random) -> Dict[str, Any]:
    gas_name, m_molar = rng.choice([
        ("oxygen (O2)", 32.0),
        ("carbon dioxide (CO2)", 44.0),
        ("nitrogen (N2)", 28.0),
        ("chlorine (Cl2)", 71.0),
    ])
    p_kpa = rng.choice([101.3, 150.0, 200.0])
    t_c = rng.choice([0, 20, 25, 27])
    t_k = t_c + 273
    # rho (g/dm^3) = (P_kPa * M) / (R * T_K)
    rho_g_dm3 = round((p_kpa * m_molar) / (R_GAS * t_k), 2)
    qid = f"ps11_gas_39_{rng.randint(100000, 999999)}"

    prompt = (
        f"Starting from the ideal gas equation $PV = nRT$ and the mole relation $n = \\frac{{m}}{{M}}$, "
        f"the density ($\\rho = \\frac{{m}}{{V}}$) of an ideal gas can be determined.\n\n"
        f"Calculate the density (in $\\text{{g}}\\cdot\\text{{dm}}^{{-3}}$) of {gas_name} ($M = {_fmt(m_molar)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$) "
        f"at a pressure of ${_fmt(p_kpa)}\\text{{ kPa}}$ and temperature of ${t_c}^\\circ\\text{{C}}$.\n"
        f"($R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$)."
    )
    ans = f"Density = {_fmt(rho_g_dm3)} g/dm^3"
    memo = (
        f"1. Consider a volume $V = 1\\text{{ dm}}^3 = 0{{,}}001\\text{{ m}}^3$ at $T = {t_c} + 273 = {_fmt(t_k)}\\text{{ K}}$ [1].\n"
        f"2. From $PV = \\frac{{m}}{{M}}RT$, density in $\\text{{g}}\\cdot\\text{{dm}}^{{-3}}$ is given by:\n"
        f"   $$\\rho = \\frac{{m}}{{V}} = \\frac{{P(\\text{{kPa}}) \\cdot M}}{{R \\cdot T}}$$ [2]\n"
        f"   $$\\rho = \\frac{{{_fmt(p_kpa)} \\times {_fmt(m_molar)}}}{{8{{,}}31 \\times {_fmt(t_k)}}} = {_fmt(rho_g_dm3)}\\text{{ g}}\\cdot\\text{{dm}}^{{-3}}$$ [2]"
    )
    hints = {
        "tier_1": "Substitute n = m/M into PV = nRT -> PV = (m/M)RT -> m/V = PM / (RT).",
        "tier_2": f"T = {t_k} K. Using P in kPa and M in g/mol gives density directly in g/dm^3.",
        "tier_3": f"rho = ({p_kpa} * {m_molar}) / (8,31 * {t_k}) = {_fmt(rho_g_dm3)} g/dm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "39_gas_density_calculation",
        "learning_objective_id": "ps11_ideal_gas_density",
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
        "misconception_tags": ["density_formula_inversion", "forgot_kelvin_conversion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert T to Kelvin", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Relate PV = (m/M)RT to density m/V", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Calculate correct density in g/dm^3", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_40_gas_molar_mass_from_density(rng: random.Random) -> Dict[str, Any]:
    gas_name, m_molar = rng.choice([
        ("neon (Ne)", 20.2),
        ("argon (Ar)", 39.9),
        ("ethane (C2H6)", 30.0),
        ("propane (C3H8)", 44.0),
    ])
    p_kpa = rng.choice([100.0, 101.3, 120.0])
    t_c = rng.choice([20, 25, 27])
    t_k = t_c + 273
    rho = round((p_kpa * m_molar) / (R_GAS * t_k), 3)
    m_calc = round((rho * R_GAS * t_k) / p_kpa, 1)
    qid = f"ps11_gas_40_{rng.randint(100000, 999999)}"

    prompt = (
        f"An unknown gaseous hydrocarbon or noble gas has a measured density of ${_fmt(rho, 3)}\\text{{ g}}\\cdot\\text{{dm}}^{{-3}}$ "
        f"at a pressure of ${_fmt(p_kpa)}\\text{{ kPa}}$ and temperature of ${t_c}^\\circ\\text{{C}}$.\n"
        f"($R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"Calculate the molar mass ($M$) of the gas in $\\text{{g}}\\cdot\\text{{mol}}^{{-1}}$."
    )
    ans = f"M = {_fmt(m_calc)} g/mol"
    memo = (
        f"1. Temperature in Kelvin [1]: $T = {t_c} + 273 = {_fmt(t_k)}\\text{{ K}}$ [1].\n"
        f"2. Molar mass from density [3]:\n"
        f"   $$M = \\frac{{\\rho R T}}{{P}} = \\frac{{{_fmt(rho, 3)} \\times 8{{,}}31 \\times {_fmt(t_k)}}}{{{_fmt(p_kpa)}}} = {_fmt(m_calc)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$$ [3]"
    )
    hints = {
        "tier_1": "Use M = (rho * R * T) / P where rho is in g/dm^3 and P is in kPa.",
        "tier_2": f"T = {t_k} K. Substitute rho = {rho}, R = 8,31, P = {p_kpa}.",
        "tier_3": f"M = {_fmt(m_calc)} g/mol.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "40_gas_molar_mass_from_density",
        "learning_objective_id": "ps11_molar_mass_from_density",
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
        "misconception_tags": ["density_formula_inversion", "forgot_kelvin_conversion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert T to Kelvin", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Formula M = rho*R*T/P and substitution", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct molar mass", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_41_gas_mixture_dalton_partial_pressures(rng: random.Random) -> Dict[str, Any]:
    n_n2 = rng.choice([0.4, 0.6, 0.8, 1.2])
    n_o2 = rng.choice([0.2, 0.4, 0.6])
    n_tot = round(n_n2 + n_o2, 2)
    v_dm3 = rng.choice([10.0, 15.0, 20.0])
    v_m3 = v_dm3 / 1000.0
    t_c = rng.choice([25, 27])
    t_k = t_c + 273
    p_tot_kpa = round(((n_tot * R_GAS * t_k) / v_m3) / 1000.0, 1)
    p_n2_kpa = round(p_tot_kpa * (n_n2 / n_tot), 1)
    qid = f"ps11_gas_41_{rng.randint(100000, 999999)}"

    prompt = (
        f"A gas cylinder of volume ${_fmt(v_dm3)}\\text{{ dm}}^3$ contains a non-reacting mixture of "
        f"${_fmt(n_n2)}\\text{{ mol}}$ of nitrogen ($\\text{{N}}_2$) and ${_fmt(n_o2)}\\text{{ mol}}$ of oxygen ($\\text{{O}}_2$) "
        f"at a temperature of ${t_c}^\\circ\\text{{C}}$.\n"
        f"($R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"1. Calculate the total number of moles ($n_{{\\text{{total}}}}$) of gas in the cylinder.\n"
        f"2. Calculate the total pressure ($P_{{\\text{{total}}}}$) in $\\text{{kPa}}$ exerted by the gas mixture.\n"
        f"3. Calculate the partial pressure exerted by the nitrogen gas alone."
    )
    ans = f"1. n_total = {_fmt(n_tot)} mol; 2. P_total = {_fmt(p_tot_kpa)} kPa; 3. P_N2 = {_fmt(p_n2_kpa)} kPa"
    memo = (
        f"1. Total moles [1]: $n_{{\\text{{total}}}} = {_fmt(n_n2)} + {_fmt(n_o2)} = {_fmt(n_tot)}\\text{{ mol}}$ [1].\n"
        f"2. Total pressure [3]:\n"
        f"   $$T = {t_c} + 273 = {_fmt(t_k)}\\text{{ K}}, \\quad V = {v_m3:.3f}\\text{{ m}}^3$$\n"
        f"   $$P_{{\\text{{total}}}} = \\frac{{n_{{\\text{{total}}}} R T}}{{V}} = \\frac{{({_fmt(n_tot)})(8{{,}}31)({t_k})}}{{{v_m3:.3f}}} \\div 1000 = {_fmt(p_tot_kpa)}\\text{{ kPa}}$$ [3]\n"
        f"3. Partial pressure of $\\text{{N}}_2$ [2]:\n"
        f"   $$P_{{\\text{{N}}_2}} = \\frac{{n_{{\\text{{N}}_2}}}}{{n_{{\\text{{total}}}}}} \\times P_{{\\text{{total}}}} = \\frac{{{_fmt(n_n2)}}}{{{_fmt(n_tot)}}} \\times {_fmt(p_tot_kpa)} = {_fmt(p_n2_kpa)}\\text{{ kPa}}$$ [2]"
    )
    hints = {
        "tier_1": "Add moles: n_total = n_N2 + n_O2. Then P_total = (n_total * R * T) / V.",
        "tier_2": "Partial pressure of N2 = (n_N2 / n_total) * P_total.",
        "tier_3": f"n_total = {_fmt(n_tot)} mol, P_total = {_fmt(p_tot_kpa)} kPa, P_N2 = {_fmt(p_n2_kpa)} kPa.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "41_gas_mixture_dalton_partial_pressures",
        "learning_objective_id": "ps11_dalton_partial_pressures",
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
        "misconception_tags": ["partial_pressure_mole_fraction_error", "volume_dm3_m3_conversion_error"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Total moles n_total", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Total pressure calculation", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Partial pressure of N2", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ---------------------------------------------------------------------------
# 42–45: Avogadro's Hypothesis, Molar Volume at STP & Gas Stoichiometry
# ---------------------------------------------------------------------------


def build_42_avogadro_hypothesis_and_molar_volume_stp(rng: random.Random) -> Dict[str, Any]:
    n_mol = rng.choice([0.25, 0.5, 1.5, 2.0, 2.5, 3.0])
    v_stp = round(n_mol * 22.4, 2)
    qid = f"ps11_gas_42_{rng.randint(100000, 999999)}"

    prompt = (
        f"Avogadro's Law states that equal volumes of all ideal gases at the same temperature and pressure "
        f"contain the same number of molecules.\n\n"
        f"1. State the value of the standard molar volume ($V_m$) of an ideal gas at STP.\n"
        f"2. Calculate the volume (in $\\text{{dm}}^3$) occupied by ${_fmt(n_mol)}\\text{{ mol}}$ of ammonia gas ($\\text{{NH}}_3$) at STP."
    )
    ans = f"1. V_m = 22,4 dm^3/mol; 2. V = {_fmt(v_stp)} dm^3"
    memo = (
        f"1. Standard molar volume at STP [1]: $V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$ [1].\n"
        f"2. Volume calculation [2]:\n"
        f"   $$V = n \\times V_m = {_fmt(n_mol)} \\times 22{{,}}4 = {_fmt(v_stp)}\\text{{ dm}}^3$$ [2]"
    )
    hints = {
        "tier_1": "At STP, 1 mole of any ideal gas occupies 22,4 dm^3.",
        "tier_2": f"Multiply n = {_fmt(n_mol)} mol by 22,4 dm^3/mol.",
        "tier_3": f"V = {_fmt(v_stp)} dm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "42_avogadro_hypothesis_and_molar_volume_stp",
        "learning_objective_id": "ps11_avogadro_molar_vol_stp",
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
        "misconception_tags": ["molar_volume_used_at_non_stp", "molar_mass_used_instead_of_molar_volume"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "State Vm = 22,4 dm^3/mol", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Calculate V = n * Vm", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_43_gas_moles_from_stp_volume(rng: random.Random) -> Dict[str, Any]:
    gas_name, m_molar = rng.choice([
        ("carbon dioxide (CO2)", 44.0),
        ("oxygen (O2)", 32.0),
        ("nitrogen (N2)", 28.0),
        ("sulfur dioxide (SO2)", 64.0),
    ])
    n_mol = rng.choice([0.2, 0.5, 0.75, 1.25, 1.5])
    v_dm3 = round(n_mol * 22.4, 2)
    mass_g = round(n_mol * m_molar, 2)
    qid = f"ps11_gas_43_{rng.randint(100000, 999999)}"

    prompt = (
        f"A gas jar contains ${_fmt(v_dm3)}\\text{{ dm}}^3$ of {gas_name} ($M = {_fmt(m_molar)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$) measured at STP.\n"
        f"($V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"1. Calculate the number of moles ($n$) of {gas_name} in the jar.\n"
        f"2. Calculate the mass ($m$) of the gas sample in grams."
    )
    ans = f"1. n = {_fmt(n_mol)} mol; 2. m = {_fmt(mass_g)} g"
    memo = (
        f"1. Moles at STP [2]:\n"
        f"   $$n = \\frac{{V}}{{V_m}} = \\frac{{{_fmt(v_dm3)}}}{{22{{,}}4}} = {_fmt(n_mol)}\\text{{ mol}}$$ [2]\n"
        f"2. Mass of gas [2]:\n"
        f"   $$m = n \\times M = {_fmt(n_mol)} \\times {_fmt(m_molar)} = {_fmt(mass_g)}\\text{{ g}}$$ [2]"
    )
    hints = {
        "tier_1": "First find n = V / 22,4. Then find m = n * M.",
        "tier_2": f"n = {_fmt(v_dm3)} / 22,4 = {_fmt(n_mol)} mol.",
        "tier_3": f"m = {_fmt(n_mol)} * {_fmt(m_molar)} = {_fmt(mass_g)} g.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "43_gas_moles_from_stp_volume",
        "learning_objective_id": "ps11_moles_from_stp_vol",
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
        "misconception_tags": ["molar_volume_division_inversion", "molar_mass_calculation_error"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Calculate moles n = V / 22,4", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Calculate mass m = n * M", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_44_gas_stoichiometry_combustion_volume(rng: random.Random) -> Dict[str, Any]:
    v_ch4 = rng.choice([2.0, 3.5, 5.0, 6.0, 8.0])  # dm^3
    v_o2 = round(2 * v_ch4, 1)
    v_co2 = v_ch4
    qid = f"ps11_gas_44_{rng.randint(100000, 999999)}"

    prompt = (
        f"Methane gas burns completely in excess oxygen according to the balanced chemical equation:\n"
        f"$$\\text{{CH}}_4(\\text{{g}}) + 2\\text{{O}}_2(\\text{{g}}) \\rightarrow \\text{{CO}}_2(\\text{{g}}) + 2\\text{{H}}_2\\text{{O}}(\\text{{g}})$$\n\n"
        f"All gas volumes are measured at the same temperature and pressure, where ${_fmt(v_ch4)}\\text{{ dm}}^3$ of $\\text{{CH}}_4$ reacts completely.\n"
        f"1. Calculate the volume of $\\text{{O}}_2(\\text{{g}})$ required for complete combustion.\n"
        f"2. Calculate the volume of $\\text{{CO}}_2(\\text{{g}})$ produced."
    )
    ans = f"1. V(O2) = {_fmt(v_o2)} dm^3; 2. V(CO2) = {_fmt(v_co2)} dm^3"
    memo = (
        f"By Avogadro's Law, at constant temperature and pressure, gas volumes react in the same simple ratio as their stoichiometric mole coefficients:\n"
        f"1. Volume of $\\text{{O}}_2$ [2]:\n"
        f"   Mole ratio $\\text{{CH}}_4 : \\text{{O}}_2 = 1 : 2$\n"
        f"   $$V(\\text{{O}}_2) = 2 \\times {_fmt(v_ch4)} = {_fmt(v_o2)}\\text{{ dm}}^3$$ [2]\n"
        f"2. Volume of $\\text{{CO}}_2$ [2]:\n"
        f"   Mole ratio $\\text{{CH}}_4 : \\text{{CO}}_2 = 1 : 1$\n"
        f"   $$V(\\text{{CO}}_2) = 1 \\times {_fmt(v_ch4)} = {_fmt(v_co2)}\\text{{ dm}}^3$$ [2]"
    )
    hints = {
        "tier_1": "At constant T and P, volume ratios equal stoichiometric mole ratios.",
        "tier_2": "Ratio CH4 : O2 = 1 : 2. Ratio CH4 : CO2 = 1 : 1.",
        "tier_3": f"V(O2) = {_fmt(v_o2)} dm^3, V(CO2) = {_fmt(v_co2)} dm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "44_gas_stoichiometry_combustion_volume",
        "learning_objective_id": "ps11_gas_stoich_volume_ratios",
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
        "misconception_tags": ["stoichiometric_ratio_inversion", "unnecessary_molar_mass_conversion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Volume of O2 using 1:2 ratio", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Volume of CO2 using 1:1 ratio", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_45_gas_stoichiometry_mass_to_gas_volume(rng: random.Random) -> Dict[str, Any]:
    mass_caco3 = rng.choice([5.0, 10.0, 20.0, 25.0, 50.0])  # g (M = 100 g/mol)
    n_caco3 = round(mass_caco3 / 100.0, 3)
    n_co2 = n_caco3
    v_co2_stp = round(n_co2 * 22.4, 2)
    qid = f"ps11_gas_45_{rng.randint(100000, 999999)}"

    prompt = (
        f"Calcium carbonate reacts completely with excess dilute hydrochloric acid according to the balanced equation:\n"
        f"$$\\text{{CaCO}}_3(\\text{{s}}) + 2\\text{{HCl}}(\\text{{aq}}) \\rightarrow \\text{{CaCl}}_2(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\text{{l}}) + \\text{{CO}}_2(\\text{{g}})$$\n\n"
        f"In an experiment, ${_fmt(mass_caco3)}\\text{{ g}}$ of pure $\\text{{CaCO}}_3$ ($M = 100\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$) reacts completely.\n"
        f"1. Calculate the number of moles of $\\text{{CaCO}}_3$ that reacted.\n"
        f"2. Calculate the volume of $\\text{{CO}}_2(\\text{{g}})$ produced at STP ($V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$)."
    )
    ans = f"1. n(CaCO3) = {_fmt(n_caco3, 3)} mol; 2. V(CO2) = {_fmt(v_co2_stp)} dm^3"
    memo = (
        f"1. Moles of $\\text{{CaCO}}_3$ [2]:\n"
        f"   $$n = \\frac{{m}}{{M}} = \\frac{{{_fmt(mass_caco3)}}}{{100}} = {_fmt(n_caco3, 3)}\\text{{ mol}}$$ [2]\n"
        f"2. Volume of $\\text{{CO}}_2$ at STP [3]:\n"
        f"   - Stoichiometric ratio $\\text{{CaCO}}_3 : \\text{{CO}}_2 = 1 : 1 \\implies n(\\text{{CO}}_2) = {_fmt(n_co2, 3)}\\text{{ mol}}$ [1]\n"
        f"   - $V = n \\times V_m = {_fmt(n_co2, 3)} \\times 22{{,}}4 = {_fmt(v_co2_stp)}\\text{{ dm}}^3$ [2]"
    )
    hints = {
        "tier_1": "Find n(CaCO3) = m / 100. Use 1:1 mole ratio to find n(CO2), then multiply by 22,4 dm^3/mol.",
        "tier_2": f"n = {mass_caco3} / 100 = {_fmt(n_caco3, 3)} mol.",
        "tier_3": f"V(CO2) = {_fmt(n_co2, 3)} * 22,4 = {_fmt(v_co2_stp)} dm^3.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "45_gas_stoichiometry_mass_to_gas_volume",
        "learning_objective_id": "ps11_gas_stoich_mass_to_vol",
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
        "misconception_tags": ["stoichiometric_ratio_error", "molar_volume_calculation_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Moles of CaCO3", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "1:1 mole ratio for CO2", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Volume of CO2 at STP", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ---------------------------------------------------------------------------
# 46–50: Real vs Ideal Gas Deviations & Capstone Synthesis
# ---------------------------------------------------------------------------


def build_46_ideal_vs_real_gas_definitions_comparison(rng: random.Random) -> Dict[str, Any]:
    gas_pair = rng.choice([
        ("helium (He)", "ammonia (NH3)"),
        ("hydrogen (H2)", "water vapour (H2O)"),
        ("neon (Ne)", "sulfur dioxide (SO2)"),
    ])
    qid = f"ps11_gas_46_{rng.randint(100000, 999999)}"

    prompt = (
        f"In physical sciences, we distinguish between a theoretical ideal gas and real gases such as {gas_pair[0]} and {gas_pair[1]}.\n\n"
        f"1. Define an 'ideal gas' in terms of particle volume and intermolecular forces.\n"
        f"2. State under which conditions of temperature and pressure a real gas behaves most like an ideal gas.\n"
        f"3. Between {gas_pair[0]} and {gas_pair[1]}, identify which gas behaves more closely to an ideal gas at room temperature, and give a reason."
    )
    ans = (
        f"1. An ideal gas is a theoretical gas composed of identical particles of zero volume with no intermolecular forces between them, obeying PV=nRT under all conditions. "
        f"2. High temperature and low pressure. "
        f"3. {gas_pair[0]}, because it consists of very small non-polar particles with extremely weak London dispersion forces compared to the stronger intermolecular forces and larger molecular size of {gas_pair[1]}."
    )
    memo = (
        f"1. Ideal gas definition [2]: A hypothetical gas whose molecules occupy negligible (zero) volume [1] and experience zero intermolecular forces of attraction or repulsion [1].\n"
        f"2. Ideal behaviour conditions [2]: High temperature [1] and low pressure [1].\n"
        f"3. Comparison [2]: {gas_pair[0]} behaves more ideally [1] because its atoms/molecules have very small particle volume and very weak intermolecular (London) forces compared to {gas_pair[1]} [1]."
    )
    hints = {
        "tier_1": "Ideal gases have zero particle volume and zero intermolecular attractions.",
        "tier_2": "Real gases act ideally when particles are far apart (low P) and moving fast (high T).",
        "tier_3": f"Ideal gas: zero volume, no IMF. Ideal conditions: high T, low P. More ideal: {gas_pair[0]}.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "46_ideal_vs_real_gas_definitions_comparison",
        "learning_objective_id": "ps11_ideal_vs_real_def",
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
        "misconception_tags": ["real_gas_deviation_condition_inversion", "imf_ideal_deviation_confusion"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of ideal gas (zero volume, no IMF)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Conditions for ideal behaviour (high T, low P)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Identify more ideal gas with molecular reason", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_47_real_gas_deviation_high_pressure(rng: random.Random) -> Dict[str, Any]:
    p_high = rng.choice([500, 800, 1000, 1500])  # atm
    qid = f"ps11_gas_47_{rng.randint(100000, 999999)}"

    svg_inner = (
        f'<line x1="50" y1="200" x2="350" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<text x="310" y="220" font-family="sans-serif" font-size="12" fill="#334155">P (atm)</text>'
        f'<text x="15" y="30" font-family="sans-serif" font-size="12" fill="#334155">V (dm³)</text>'
        # Ideal gas curve (solid blue)
        f'<path d="M 65 35 Q 90 150 330 190" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        # Real gas curve (dashed red - stays higher volume at high P)
        f'<path d="M 65 35 Q 95 135 330 165" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="5,4"/>'
        f'<text x="240" y="150" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Real gas ({p_high} atm)</text>'
        f'<text x="240" y="185" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">Ideal gas</text>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying graph comparing the volume-pressure curves of an ideal gas (solid line) "
        f"and a real gas (dashed line) up to a high pressure of ${p_high}\\text{{ atm}}$.\n\n"
        f"1. State how the measured volume of the real gas compares to the predicted ideal gas volume at very high pressures.\n"
        f"2. Explain this deviation at high pressure in terms of the kinetic molecular theory."
    )
    ans = (
        "1. At very high pressure, the volume of a real gas is greater than that predicted for an ideal gas. "
        "2. At high pressures, molecules are forced very close together, so the actual volume of the gas molecules themselves is no longer negligible compared to the container volume."
    )
    memo = (
        "1. Volume comparison [1]: At high pressure, the volume of the real gas is larger than the volume predicted for an ideal gas [1].\n"
        "2. Molecular explanation [3]:\n"
        "   - Ideal gas theory assumes particles have zero volume [1].\n"
        "   - At very high pressures, gas molecules are compressed close together so their own finite molecular volume becomes a significant fraction of the total container volume [1].\n"
        "   - Repulsive forces at very short distances and the volume occupied by the particles prevent the gas from compressing as much as an ideal gas [1]."
    )
    hints = {
        "tier_1": "Look at the right side of the graph (high P): which curve is higher in V?",
        "tier_2": "At high pressure, particles are crowded together. Do real molecules have zero volume?",
        "tier_3": "1. Real gas volume > ideal gas volume. 2. Particle volume is no longer negligible compared to container volume.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "47_real_gas_deviation_high_pressure",
        "learning_objective_id": "ps11_real_gas_high_p",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Real vs Ideal Gas V vs P up to {p_high} atm"},
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["high_pressure_imf_vs_volume_confusion", "real_gas_deviation_condition_inversion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "State real gas volume is larger than ideal at high P", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Explain finite molecular volume becoming significant", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_48_real_gas_deviation_low_temperature(rng: random.Random) -> Dict[str, Any]:
    t_low_k = rng.choice([50, 80, 100, 120])  # K
    qid = f"ps11_gas_48_{rng.randint(100000, 999999)}"

    svg_inner = (
        f'<line x1="50" y1="200" x2="350" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<text x="310" y="220" font-family="sans-serif" font-size="12" fill="#334155">T (K)</text>'
        f'<text x="15" y="30" font-family="sans-serif" font-size="12" fill="#334155">P (kPa)</text>'
        # Ideal gas straight dashed line
        f'<line x1="50" y1="200" x2="320" y2="40" stroke="#2563eb" stroke-width="2" stroke-dasharray="5,4"/>'
        # Real gas curve dipping below ideal at low T
        f'<path d="M 110 185 Q 150 155 210 105 L 320 40" fill="none" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="160" y="75" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">Ideal gas</text>'
        f'<text x="135" y="175" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Real gas (near {t_low_k} K)</text>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying graph of pressure ($P$) versus absolute temperature ($T$) comparing an ideal gas "
        f"and a real gas cooled toward ${t_low_k}\\text{{ K}}$.\n\n"
        f"1. State how the measured pressure of the real gas compares to the ideal gas prediction at low temperatures.\n"
        f"2. Explain this deviation at low temperature in terms of intermolecular forces and wall collisions.\n"
        f"3. State what physical phase change eventually occurs if the real gas is cooled further."
    )
    ans = (
        "1. At low temperature, the pressure of a real gas is lower than predicted for an ideal gas. "
        "2. At low temperatures, particles have low average kinetic energy and move slowly, allowing intermolecular attractive forces to pull particles together. "
        "This reduces the force and frequency of collisions with the container walls. "
        "3. Condensation / liquefaction (gas turns into a liquid)."
    )
    memo = (
        "1. Pressure comparison [1]: Real gas pressure is lower than ideal gas pressure at low temperatures [1].\n"
        "2. Explanation [3]:\n"
        "   - At low temperatures, gas molecules have low average kinetic energy and move slowly [1].\n"
        "   - Intermolecular forces of attraction between molecules become significant [1].\n"
        "   - Molecules are pulled inward away from the walls, colliding with the container walls with less force and frequency, lowering pressure [1].\n"
        "3. Phase change [1]: Liquefaction / condensation into a liquid [1]."
    )
    hints = {
        "tier_1": "At low T, particles move slowly and intermolecular attractions take effect.",
        "tier_2": "Attractive forces pull molecules together, reducing collision impact on walls -> lower pressure.",
        "tier_3": "1. Real P < Ideal P. 2. Low KE allows intermolecular attractions to reduce wall collisions. 3. Liquefaction.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "48_real_gas_deviation_low_temperature",
        "learning_objective_id": "ps11_real_gas_low_t",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Real vs Ideal Gas P vs T near {t_low_k} K"},
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["low_temp_imf_deviation_misunderstood", "real_gas_deviation_condition_inversion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "State real gas pressure is lower at low T", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Explain role of low KE and intermolecular attractions", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Identify liquefaction / condensation", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_49_compressibility_factor_z_graph(rng: random.Random) -> Dict[str, Any]:
    gas_a, gas_b = rng.choice([
        ("H2", "NH3"),
        ("He", "CO2"),
        ("N2", "SO2"),
    ])
    qid = f"ps11_gas_49_{rng.randint(100000, 999999)}"

    svg_inner = (
        f'<line x1="50" y1="200" x2="350" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>'
        f'<text x="310" y="220" font-family="sans-serif" font-size="12" fill="#334155">P (atm)</text>'
        f'<text x="10" y="30" font-family="sans-serif" font-size="11" fill="#334155">PV / nRT</text>'
        # Ideal gas horizontal line at Z = 1
        f'<line x1="50" y1="130" x2="340" y2="130" stroke="#64748b" stroke-width="2" stroke-dasharray="4"/>'
        f'<text x="30" y="134" font-family="sans-serif" font-size="11" font-weight="bold" fill="#334155">1,0</text>'
        f'<text x="275" y="124" font-family="sans-serif" font-size="10" fill="#64748b">Ideal Gas</text>'
        # Gas A (slight dip or steady rise)
        f'<path d="M 50 130 Q 140 120 320 55" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<text x="290" y="50" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">Gas X ({gas_a})</text>'
        # Gas B (deep dip below 1 then rise)
        f'<path d="M 50 130 Q 140 195 330 75" fill="none" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="145" y="185" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Gas Y ({gas_b})</text>'
    )
    svg = _svg_wrap(svg_inner, 380, 240)

    prompt = (
        f"Refer to the accompanying graph of the compressibility ratio $\\frac{{PV}}{{nRT}}$ plotted against pressure ($P$) "
        f"at constant temperature for an ideal gas, Gas X ({gas_a}), and Gas Y ({gas_b}).\n\n"
        f"1. State the value of $\\frac{{PV}}{{nRT}}$ for $1\\text{{ mol}}$ of an ideal gas at all pressures.\n"
        f"2. Explain why Curve Y ({gas_b}) dips significantly below $1{{,}}0$ at moderate pressures.\n"
        f"3. Explain why both curves rise above $1{{,}}0$ at very high pressures."
    )
    ans = (
        f"1. PV/(nRT) = 1,0. "
        f"2. {gas_b} has strong intermolecular forces of attraction which pull molecules closer together at moderate pressures, making PV smaller than nRT (Z < 1). "
        f"3. At very high pressures, the finite molecular volume of the gas particles themselves becomes significant compared to the container volume, making V (and PV/nRT) greater than 1,0."
    )
    memo = (
        f"1. Ideal value [1]: $\\frac{{PV}}{{nRT}} = 1{{,}}0$ [1].\n"
        f"2. Dip below $1{{,}}0$ for {gas_b} [2]:\n"
        f"   - {gas_b} experiences strong intermolecular attractive forces (dipole-dipole / hydrogen bonding / larger van der Waals forces) [1].\n"
        f"   - At moderate pressures, these attractions pull molecules closer together, reducing volume/pressure below ideal predictions ($PV < nRT$) [1].\n"
        f"3. Rise above $1{{,}}0$ at very high pressures [2]:\n"
        f"   - At extreme pressures, molecules are packed very tightly and their own molecular volume is no longer negligible [1].\n"
        f"   - The actual volume occupied exceeds the ideal prediction, causing $\\frac{{PV}}{{nRT}} > 1{{,}}0$ [1]."
    )
    hints = {
        "tier_1": "For an ideal gas, PV = nRT so PV/(nRT) = 1.",
        "tier_2": "A dip below 1 is caused by intermolecular attractions. A rise above 1 is caused by finite molecular volume.",
        "tier_3": f"1. 1,0. 2. Strong intermolecular attractions in {gas_b} cause Z < 1. 3. Finite particle volume at high P causes Z > 1.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "49_compressibility_factor_z_graph",
        "learning_objective_id": "ps11_compressibility_z_graph",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"PV/nRT vs P for {gas_a} and {gas_b}"},
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["compressibility_factor_dip_vs_rise_inversion", "imf_ideal_deviation_confusion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Value PV/nRT = 1,0 for ideal gas", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Explain dip below 1 due to intermolecular attractions", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Explain rise above 1 due to finite molecular volume", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def build_50_ideal_gas_thermal_capstone_synthesis(rng: random.Random) -> Dict[str, Any]:
    gas_name, m_molar = rng.choice([
        ("oxygen (O2)", 32.0),
        ("nitrogen (N2)", 28.0),
        ("carbon dioxide (CO2)", 44.0),
    ])
    mass_g = rng.choice([32.0, 56.0, 64.0, 88.0])
    n_mol = round(mass_g / m_molar, 2)
    v1_dm3 = rng.choice([15.0, 20.0, 25.0])
    v1_m3 = v1_dm3 / 1000.0
    t1_c = rng.choice([25, 27])
    t1_k = t1_c + 273
    p1_pa = (n_mol * R_GAS * t1_k) / v1_m3
    p1_kpa = round(p1_pa / 1000.0, 1)

    t2_c = rng.choice([100, 127, 150])
    t2_k = t2_c + 273
    p2_kpa = round(p1_kpa * (t2_k / t1_k), 1)
    qid = f"ps11_gas_50_{rng.randint(100000, 999999)}"

    prompt = (
        f"A rigid steel cylinder of volume ${_fmt(v1_dm3)}\\text{{ dm}}^3$ is filled with ${_fmt(mass_g)}\\text{{ g}}$ of {gas_name} "
        f"($M = {_fmt(m_molar)}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$) at an initial temperature of ${t1_c}^\\circ\\text{{C}}$.\n"
        f"($R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$).\n\n"
        f"1. Calculate the number of moles ($n$) of {gas_name} in the cylinder.\n"
        f"2. Calculate the initial pressure ($P_1$) inside the cylinder in $\\text{{kPa}}$.\n"
        f"3. The cylinder is subsequently heated to ${t2_c}^\\circ\\text{{C}}$. Calculate the new pressure ($P_2$) in $\\text{{kPa}}$.\n"
        f"4. Explain why the real pressure measured at very high pressures would differ from the ideal gas calculation."
    )
    ans = (
        f"1. n = {_fmt(n_mol)} mol; "
        f"2. P_1 = {_fmt(p1_kpa)} kPa; "
        f"3. P_2 = {_fmt(p2_kpa)} kPa; "
        f"4. At very high pressures, the volume of the gas molecules themselves becomes significant compared to the container volume, reducing free space and increasing collision frequency so real pressure exceeds ideal pressure."
    )
    memo = (
        f"1. Moles [2]: $n = \\frac{{m}}{{M}} = \\frac{{{_fmt(mass_g)}}}{{{_fmt(m_molar)}}} = {_fmt(n_mol)}\\text{{ mol}}$ [2].\n"
        f"2. Initial pressure [3]:\n"
        f"   $$V_1 = {v1_m3:.3f}\\text{{ m}}^3, \\quad T_1 = {t1_c} + 273 = {_fmt(t1_k)}\\text{{ K}}$$\n"
        f"   $$P_1 = \\frac{{nRT_1}}{{V_1}} = \\frac{{({_fmt(n_mol)})(8{{,}}31)({t1_k})}}{{{v1_m3:.3f}}} \\div 1000 = {_fmt(p1_kpa)}\\text{{ kPa}}$$ [3]\n"
        f"3. New pressure via Gay-Lussac's Law [2]:\n"
        f"   $$T_2 = {t2_c} + 273 = {_fmt(t2_k)}\\text{{ K}}$$\n"
        f"   $$P_2 = P_1 \\times \\frac{{T_2}}{{T_1}} = {_fmt(p1_kpa)} \\times \\frac{{{_fmt(t2_k)}}}{{{_fmt(t1_k)}}} = {_fmt(p2_kpa)}\\text{{ kPa}}$$ [2]\n"
        f"4. High-pressure deviation [2]: Molecules occupy finite volume [1], reducing the effective free volume available for movement and increasing wall collision frequency [1]."
    )
    hints = {
        "tier_1": "Step 1: n = m/M. Step 2: P1 = nRT1/V1. Step 3: P2/T2 = P1/T1.",
        "tier_2": f"n = {_fmt(n_mol)} mol, T1 = {t1_k} K, T2 = {t2_k} K.",
        "tier_3": f"P1 = {_fmt(p1_kpa)} kPa, P2 = {_fmt(p2_kpa)} kPa.",
    }
    return {
        "id": qid,
        "question_id": qid,
        "topic": "physical_sciences_ideal_gases_thermal",
        "subskill": "50_ideal_gas_thermal_capstone_synthesis",
        "learning_objective_id": "ps11_ideal_gas_capstone",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "expected_answer": ans,
        "worked_solution": memo,
        "marks": 9,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 9,
        "mode": "compound",
        "hints": hints,
        "misconception_tags": ["forgot_kelvin_conversion", "volume_dm3_m3_conversion_error", "high_pressure_imf_vs_volume_confusion"],
        "marking_schema": {
            "total_marks": 9,
            "marking_points": [
                {"id": "mp_1", "desc": "Calculate moles n = m/M", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Calculate initial pressure P1 via PV = nRT", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Calculate final pressure P2 via Gay-Lussac's Law", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Explain molecular volume effect at high pressure", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


BUILDERS_26_50 = {
    "26_general_gas_equation_derivation": build_26_general_gas_equation_derivation,
    "27_general_gas_equation_solve_v2": build_27_general_gas_equation_solve_v2,
    "28_general_gas_equation_solve_p2": build_28_general_gas_equation_solve_p2,
    "29_general_gas_equation_solve_t2": build_29_general_gas_equation_solve_t2,
    "30_gas_volume_converted_to_stp": build_30_gas_volume_converted_to_stp,
    "31_underwater_diver_bubble_expansion": build_31_underwater_diver_bubble_expansion,
    "32_two_connected_bulbs_isothermal": build_32_two_connected_bulbs_isothermal,
    "33_ideal_gas_law_solve_pressure": build_33_ideal_gas_law_solve_pressure,
    "34_ideal_gas_law_solve_volume": build_34_ideal_gas_law_solve_volume,
    "35_ideal_gas_law_solve_moles": build_35_ideal_gas_law_solve_moles,
    "36_ideal_gas_law_solve_temperature": build_36_ideal_gas_law_solve_temperature,
    "37_ideal_gas_law_from_mass": build_37_ideal_gas_law_from_mass,
    "38_ideal_gas_law_molar_mass_determination": build_38_ideal_gas_law_molar_mass_determination,
    "39_gas_density_calculation": build_39_gas_density_calculation,
    "40_gas_molar_mass_from_density": build_40_gas_molar_mass_from_density,
    "41_gas_mixture_dalton_partial_pressures": build_41_gas_mixture_dalton_partial_pressures,
    "42_avogadro_hypothesis_and_molar_volume_stp": build_42_avogadro_hypothesis_and_molar_volume_stp,
    "43_gas_moles_from_stp_volume": build_43_gas_moles_from_stp_volume,
    "44_gas_stoichiometry_combustion_volume": build_44_gas_stoichiometry_combustion_volume,
    "45_gas_stoichiometry_mass_to_gas_volume": build_45_gas_stoichiometry_mass_to_gas_volume,
    "46_ideal_vs_real_gas_definitions_comparison": build_46_ideal_vs_real_gas_definitions_comparison,
    "47_real_gas_deviation_high_pressure": build_47_real_gas_deviation_high_pressure,
    "48_real_gas_deviation_low_temperature": build_48_real_gas_deviation_low_temperature,
    "49_compressibility_factor_z_graph": build_49_compressibility_factor_z_graph,
    "50_ideal_gas_thermal_capstone_synthesis": build_50_ideal_gas_thermal_capstone_synthesis,
}
