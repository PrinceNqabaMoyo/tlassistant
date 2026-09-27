"""Physical Sciences & Senior Phase Natural Sciences — Thermal Physics & Ideal Gases.
Covers kinetic molecular theory, Boyle's, Charles's, Gay-Lussac's laws, and the Ideal Gas Equation (PV = nRT).
Strictly complies with the 6-Pillar Generator Contract:
- Multi-grade vertical strand (Gr8 NS, Gr10 PS, Gr11 PS)
- Procedural seeded PRNG determinism (random.Random(seed))
- Atomic elementary sub-drills (mode="compound" | "elementary_*")
- Standardized misconception taxonomy
- Teacher-editable marking schema with [M] and [A] marks
- Deterministic 3-tier pre-baked hints
- South African comma decimal convention (",")
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

R_GAS = 8.31  # J / (mol * K)
STP_TEMP_K = 273.15  # K
STP_PRESSURE_KPA = 101.3  # kPa
VM_STP = 22.4  # dm^3 / mol


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_gr8_10_kinetic_theory(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 8/10: Particle model of matter and kinetic molecular theory assumptions."""
    qid = _make_id("ps10_kinetic_theory", seed, idx)

    prompt = (
        "The kinetic molecular theory explains the macroscopic properties of gases based on the behavior of microscopic particles.\n\n"
        "1. State two basic assumptions of the kinetic theory regarding ideal gas particles.\n"
        "2. Explain, in terms of the kinetic molecular theory, why the pressure exerted by a gas on the walls of its "
        "rigid container increases when the gas is heated at constant volume."
    )
    ans_str = (
        "1. Particles in constant random motion; volume of particles negligible compared to container; collisions perfectly elastic; no intermolecular forces. "
        "2. Higher temperature increases average kinetic energy and particle speed, causing more frequent and forceful collisions against walls."
    )
    memo = (
        "1. Assumptions (any 2) [2]:\n"
        "   - Gas particles are in continuous, rapid, random motion in straight lines.\n"
        "   - The volume of individual gas particles is negligible compared to the total volume of the container.\n"
        "   - Collisions between particles and the container walls are perfectly elastic (no kinetic energy is lost).\n"
        "   - There are no intermolecular forces of attraction or repulsion between gas particles.\n"
        "2. Pressure increase explanation [3]: Heating increases the temperature, which directly increases the average kinetic energy and speed of the gas particles [1]. "
        "The particles collide with the container walls more frequently [1] and with greater force per collision [1], thereby increasing the pressure ($P = F/A$)."
    )
    hints = {
        "tier_1": "Think about particle motion, particle size, and what happens to particle speed when temperature rises.",
        "tier_2": "Temperature is a measure of average kinetic energy. Faster particles hit the container walls harder and more often.",
        "tier_3": "1. Negligible volume / elastic collisions / constant motion. 2. Higher temp -> faster particles -> more frequent, harder collisions -> higher pressure.",
    }
    marks = 5

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["particle_expansion_misconception", "elastic_collision_misunderstood", "pressure_force_area_confusion"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Kinetic theory assumptions", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Kinetic energy increase with temperature", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Collision frequency and force on walls", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr11_ideal_gas_calculations(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11 Physical Sciences: PV = nRT, Boyle's Law, and Combined Gas Law."""
    qid = _make_id("ps11_ideal_gas", seed, idx)

    if mode == "elementary_celsius_to_kelvin":
        t_celsius = r.choice([0, 20, 25, 27, 37, 50, 100, -20])
        t_kelvin = t_celsius + 273
        prompt = (
            f"In all gas law calculations, temperature must be expressed in the absolute thermodynamic unit, Kelvin (K).\n\n"
            f"Convert a temperature of ${t_celsius}^\\circ\\text{{C}}$ to Kelvin."
        )
        ans_str = f"T = {_fmt_sa(t_kelvin)} K"
        memo = f"T(K) = T(°C) + 273 = {t_celsius} + 273 = {_fmt_sa(t_kelvin)} K [2]"
        hints = {
            "tier_1": "Formula: T(K) = T(°C) + 273.",
            "tier_2": "Add 273 to the Celsius temperature.",
            "tier_3": f"{t_celsius} + 273 = {t_kelvin} K.",
        }
        return {
            "id": qid,
            "question_id": qid,
            "term": 1,
            "caps_weight_percent": 8,
            "suggested_duration_mins": 3,
            "mode": mode,
            "question_type": "short_answer",
            "question": prompt,
            "correct_answer": ans_str,
            "sample_answer": ans_str,
            "worked_solution": memo,
            "explanation": memo,
            "marks": 2,
            "hints": hints,
            "misconception_tags": ["forgot_kelvin_conversion"],
            "marking_schema": {"total_marks": 2, "marking_points": [{"id": "mp_1", "desc": "Kelvin conversion", "marks": 2, "editable": True}], "deductions": [], "carry_forward_rule": "consequential_accuracy"},
        }

    elif mode == "elementary_boyle_law":
        p1 = r.choice([100, 120, 150, 200])  # kPa
        v1 = r.choice([2.0, 3.0, 4.0, 5.0])  # dm^3
        p2 = r.choice([250, 300, 400, 500])  # kPa
        # P1 * V1 = P2 * V2 -> V2 = (P1 * V1) / P2
        v2 = round((p1 * v1) / p2, 2)

        prompt = (
            f"A sample of gas occupies a volume of ${_fmt_sa(v1)}\\text{{ dm}}^3$ at an initial pressure of ${_fmt_sa(p1)}\\text{{ kPa}}$.\n"
            f"The pressure is increased to ${_fmt_sa(p2)}\\text{{ kPa}}$ while maintaining a constant temperature.\n\n"
            f"1. State Boyle's Law in words.\n"
            f"2. Calculate the new volume ($V_2$) of the gas in $\\text{{dm}}^3$."
        )
        ans_str = f"1. Pressure is inversely proportional to volume at constant temperature; 2. V_2 = {_fmt_sa(v2)} dm^3"
        memo = (
            "1. Boyle's Law: The pressure of an enclosed gas is inversely proportional to its volume, provided the temperature remains constant [2].\n"
            f"2. $P_1 V_1 = P_2 V_2 \\implies ({_fmt_sa(p1)})({_fmt_sa(v1)}) = ({_fmt_sa(p2)}) V_2$ [M]\n"
            f"   $$V_2 = \\frac{{{_fmt_sa(p1)} \\times {_fmt_sa(v1)}}}{{{_fmt_sa(p2)}}} = {_fmt_sa(v2)}\\text{{ dm}}^3$$ [A]"
        )
        hints = {
            "tier_1": "Apply Boyle's Law: P1 * V1 = P2 * V2.",
            "tier_2": "Substitute: V2 = (P1 * V1) / P2.",
            "tier_3": f"V2 = ({p1} * {v1}) / {p2} = {_fmt_sa(v2)} dm^3.",
        }
        return {
            "id": qid,
            "question_id": qid,
            "term": 1,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 6,
            "mode": mode,
            "question_type": "short_answer",
            "question": prompt,
            "correct_answer": ans_str,
            "sample_answer": ans_str,
            "worked_solution": memo,
            "explanation": memo,
            "marks": 5,
            "hints": hints,
            "misconception_tags": ["boyles_law_proportionality_inversion", "pressure_kpa_pa_unit_error"],
            "marking_schema": {"total_marks": 5, "marking_points": [{"id": "mp_1", "desc": "Boyle's Law statement", "marks": 2, "editable": True}, {"id": "mp_2", "desc": "Calculated volume", "marks": 3, "editable": True}], "deductions": [], "carry_forward_rule": "consequential_accuracy"},
        }

    else:
        # Full compound Gr11 question: Ideal Gas Equation (PV = nRT)
        gas_name = r.choice(["oxygen (O2)", "carbon dioxide (CO2)", "nitrogen (N2)", "methane (CH4)"])
        molar_mass = 32 if "oxygen" in gas_name else (44 if "carbon dioxide" in gas_name else (28 if "nitrogen" in gas_name else 16))
        mass_g = r.choice([16.0, 32.0, 44.0, 64.0, 88.0])
        n_mol = round(mass_g / molar_mass, 2)

        vol_dm3 = r.choice([10.0, 15.0, 20.0, 25.0, 30.0])
        vol_m3 = vol_dm3 / 1000.0

        temp_c = r.choice([20, 25, 27, 30, 40, 50])
        temp_k = temp_c + 273

        # P * V = n * R * T -> P = (n * R * T) / V
        p_pa = (n_mol * R_GAS * temp_k) / vol_m3
        p_kpa = round(p_pa / 1000.0, 1)

        prompt = (
            f"A rigid cylinder with a volume of ${_fmt_sa(vol_dm3)}\\text{{ dm}}^3$ contains "
            f"${_fmt_sa(mass_g)}\\text{{ g}}$ of {gas_name} gas at a temperature of ${temp_c}^\\circ\\text{{C}}$.\n"
            f"(Molar gas constant $R = 8{{,}}31\\text{{ J}}\\cdot\\text{{K}}^{{-1}}\\cdot\\text{{mol}}^{{-1}}$, "
            f"Molar mass of {gas_name.split()[0]} $M = {molar_mass}\\text{{ g/mol}}$).\n\n"
            f"1. Convert the temperature to Kelvin and volume to cubic metres ($\\text{{m}}^3$).\n"
            f"2. Calculate the number of moles ($n$) of {gas_name} gas in the cylinder.\n"
            f"3. Calculate the pressure ($P$) of the gas in kilopascals ($\\text{{kPa}}$) using the ideal gas equation ($PV = nRT$).\n"
            f"4. Under what temperature and pressure conditions do real gases deviate significantly from ideal gas behavior?"
        )
        ans_str = (
            f"1. T = {_fmt_sa(temp_k)} K, V = {vol_m3:.3f} m^3; "
            f"2. n = {_fmt_sa(n_mol)} mol; "
            f"3. P = {_fmt_sa(p_kpa)} kPa; "
            f"4. High pressure and low temperature."
        )
        memo = (
            f"1. Unit conversions [2]:\n"
            f"   - $T = {temp_c} + 273 = {_fmt_sa(temp_k)}\\text{{ K}}$ [1]\n"
            f"   - $V = \\frac{{{_fmt_sa(vol_dm3)}}}{{1000}} = {vol_m3:.3f}\\text{{ m}}^3$ [1]\n"
            f"2. Moles [2]: $n = \\frac{{m}}{{M}} = \\frac{{{_fmt_sa(mass_g)}}}{{{molar_mass}}} = {_fmt_sa(n_mol)}\\text{{ mol}}$ [M+A]\n"
            f"3. Pressure calculation [3]:\n"
            f"   $$PV = nRT \\implies P({vol_m3:.3f}) = ({_fmt_sa(n_mol)})(8{{,}}31)({_fmt_sa(temp_k)})$$\n"
            f"   $$P = \\frac{{{_fmt_sa(n_mol)} \\times 8{{,}}31 \\times {_fmt_sa(temp_k)}}}{{{vol_m3:.3f}}} = {_fmt_sa(round(p_pa, 0))}\\text{{ Pa}} = {_fmt_sa(p_kpa)}\\text{{ kPa}}$$ [A]\n"
            f"4. Real gas deviations [2]: High pressure (particle volume becomes significant compared to container volume) [1] "
            f"and Low temperature (particles move slowly, allowing weak intermolecular forces of attraction to become significant) [1]."
        )
        hints = {
            "tier_1": "Convert: T to Kelvin (+273), V to m^3 (/1000). Find n = m/M, then apply PV = nRT.",
            "tier_2": "Formula: P = (n * R * T) / V. Divide by 1000 to express pressure in kPa.",
            "tier_3": f"1. T = {temp_k} K, V = {vol_m3} m^3. 2. n = {n_mol} mol. 3. P = {p_kpa} kPa. 4. High pressure and low temperature.",
        }
        marks = 9

        return {
            "id": qid,
            "question_id": qid,
            "term": 1,
            "caps_weight_percent": 18,
            "suggested_duration_mins": 10,
            "mode": mode,
            "question_type": "short_answer",
            "question": prompt,
            "correct_answer": ans_str,
            "sample_answer": ans_str,
            "worked_solution": memo,
            "explanation": memo,
            "marks": marks,
            "hints": hints,
            "misconception_tags": ["forgot_kelvin_conversion", "volume_dm3_m3_conversion_error", "pressure_kpa_pa_unit_error", "real_gas_deviation_condition_inversion"],
            "marking_schema": {
                "total_marks": marks,
                "marking_points": [
                    {"id": "mp_1", "desc": "Temperature and volume conversions", "marks": 2, "editable": True},
                    {"id": "mp_2", "desc": "Mole calculation", "marks": 2, "editable": True},
                    {"id": "mp_3", "desc": "Ideal gas equation substitution and pressure in kPa", "marks": 3, "editable": True},
                    {"id": "mp_4", "desc": "Conditions for real gas deviation", "marks": 2, "editable": True},
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
    grade: str = "11",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Thermal Physics & Ideal Gases."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    grade_num = "".join(ch for ch in str(grade) if ch.isdigit()) or "11"

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if grade_num in ("8", "10") or subskill in ("kinetic_theory", "states_of_matter", "particle_model"):
            q = _generate_gr8_10_kinetic_theory(sub_r, sub_seed, i, mode)
        else:
            q = _generate_gr11_ideal_gas_calculations(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
