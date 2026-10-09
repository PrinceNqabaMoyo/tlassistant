"""Grade 10 Physical Sciences — Chemical Change & Quantitative Chemistry Generator.
Deterministic 6-pillar CAPS question generator covering Paper 2 (Chemistry Term 2 & 3):
- Conservation of atoms and mass in balanced equations.
- The mole concept: n = m / M, n = N / NA (NA = 6.02 x 10^23 mol^-1).
- Molar gas volume at STP: n = V / Vm (Vm = 22.4 dm^3/mol).
- Concentration of solutions: c = n / V = m / (M * V).
- Percentage composition of elements by mass in compounds.
- Empirical formula and molecular formula calculations.

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
    return s.replace(".", "{{,}}")


NA = 6.02e23
VM_STP = 22.4


EMPIRICAL_COMPOUNDS = [
    {
        "name": "Sulfur trioxide",
        "elements": [("Sulfur (S)", 32.1, 40.05), ("Oxygen (O)", 16.0, 59.95)],
        "ratio": "1 : 3",
        "empirical": r"\text{SO}_3",
        "molar_mass": 80.1,
    },
    {
        "name": "Ethene derivative",
        "elements": [("Carbon (C)", 12.0, 85.71), ("Hydrogen (H)", 1.0, 14.29)],
        "ratio": "1 : 2",
        "empirical": r"\text{CH}_2",
        "molar_mass": 14.0,
    },
    {
        "name": "Water / Hydrogen peroxide precursor",
        "elements": [("Hydrogen (H)", 1.0, 5.88), ("Oxygen (O)", 16.0, 94.12)],
        "ratio": "1 : 1",
        "empirical": r"\text{HO}",
        "molar_mass": 17.0,
    },
    {
        "name": "Phosphorus pentoxide precursor",
        "elements": [("Phosphorus (P)", 31.0, 43.66), ("Oxygen (O)", 16.0, 56.34)],
        "ratio": "2 : 5",
        "empirical": r"\text{P}_2\text{O}_5",
        "molar_mass": 142.0,
    },
]


def _build_empirical_drill(r: random.Random) -> Dict[str, Any]:
    comp = r.choice(EMPIRICAL_COMPOUNDS)

    el_desc = ", ".join([f"**{pct}% {name.split()[0]}**" for name, _, pct in comp["elements"]])

    calc_steps = []
    ratio_parts = []
    for name, ar, pct in comp["elements"]:
        n = round(pct / ar, 3)
        calc_steps.append(f"$n({name.split()[0]}) = \\frac{{{pct}\\text{{ g}}}}{{{ar}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}}} = {n}\\text{{ mol}}$")
        ratio_parts.append(n)

    min_n = min(ratio_parts)
    norm_ratio = [round(n / min_n, 1) for n in ratio_parts]

    prompt = (
        f"A chemical compound was analysed in a laboratory and found to contain {el_desc} by mass.\n\n"
        f"1. Define the term *empirical formula*.\n"
        f"2. Determine the empirical formula of the compound through step-by-step mole calculation."
    )

    sol = (
        f"1. **Empirical formula:** The simplest whole-number ratio of the atoms of each element in a compound.\n\n"
        f"2. Assume a $100\\text{{ g}}$ sample of the compound:\n"
        + "\n".join([f"   - {step}" for step in calc_steps])
        + f"\n   Divide by the smallest value ({min_n} mol):\n"
        + f"   Mole ratio: **{comp['ratio']}**\n\n"
        + f"   Therefore, the empirical formula is **${comp['empirical']}$**."
    )

    return {
        "id": f"g10_ps_emp_form_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": comp["empirical"],
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: Simplest whole-number ratio of atoms", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Convert percentages to moles (n = m/M)", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Divide by smallest to get whole-number ratio: {comp['ratio']}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"State final empirical formula: {comp['empirical']}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "empirical_formula_ratio_rounding_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Assume a 100 g sample, so % by mass equals grams of each element.",
            "tier_2": "Calculate moles for each element using $n = m / M$, then divide each by the smallest mole value.",
            "tier_3": f"Mole ratio is {comp['ratio']}. Empirical formula: ${comp['empirical']}$.",
        },
        "misconception_tags": ["empirical_formula_ratio_rounding_error", "confused_moles_and_mass"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def _build_stoich_stp_drill(r: random.Random) -> Dict[str, Any]:
    # CaCO3 + 2HCl -> CaCl2 + H2O + CO2(g)
    mass_caco3 = r.choice([5.0, 10.0, 15.0, 20.0, 25.0])
    m_caco3 = 100.1  # g/mol

    n_caco3 = round(mass_caco3 / m_caco3, 3)
    # 1 mol CaCO3 produces 1 mol CO2
    n_co2 = n_caco3
    v_co2_dm3 = round(n_co2 * VM_STP, 2)
    m_co2 = round(n_co2 * 44.0, 2)

    prompt = (
        f"A student heats **${_fmt_sa(mass_caco3)}\\text{{ g}}$** of calcium carbonate, $\\text{{CaCO}}_3$, "
        f"which decomposes completely according to the balanced equation:\n\n"
        f"$$\\text{{CaCO}}_3(\\text{{s}}) \\xrightarrow{{\\Delta}} \\text{{CaO}}(\\text{{s}}) + \\text{{CO}}_2(\\text{{g}})$$\n\n"
        f"Molar masses: $M(\\text{{CaCO}}_3) = 100{{,}}1\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, "
        f"$M(\\text{{CO}}_2) = 44{{,}}0\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$.\n"
        f"Molar volume of a gas at STP: $V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$.\n\n"
        f"1. Calculate the number of moles of $\\text{{CaCO}}_3$ reacted.\n"
        f"2. Determine the number of moles of $\\text{{CO}}_2(\\text{{g}})$ gas produced.\n"
        f"3. Calculate the volume (in $\\text{{dm}}^3$) of $\\text{{CO}}_2(\\text{{g}})$ collected at standard temperature and pressure (STP).\n"
        f"4. Calculate the mass of $\\text{{CO}}_2(\\text{{g}})$ produced."
    )

    sol = (
        f"1. $n(\\text{{CaCO}}_3) = \\frac{{m}}{{M}} = \\frac{{{_fmt_sa(mass_caco3)}}}{{100{{,}}1}} = {_fmt_sa(n_caco3)}\\text{{ mol}}$\n\n"
        f"2. From the balanced equation, $n(\\text{{CO}}_2) : n(\\text{{CaCO}}_3) = 1 : 1$.\n"
        f"   Therefore, $n(\\text{{CO}}_2) = {_fmt_sa(n_co2)}\\text{{ mol}}$.\n\n"
        f"3. $V(\\text{{CO}}_2) = n \\times V_m = {_fmt_sa(n_co2)} \\times 22{{,}}4 = {_fmt_sa(v_co2_dm3)}\\text{{ dm}}^3$\n\n"
        f"4. $m(\\text{{CO}}_2) = n \\times M = {_fmt_sa(n_co2)} \\times 44{{,}}0 = {_fmt_sa(m_co2)}\\text{{ g}}$"
    )

    return {
        "id": f"g10_ps_stoich_stp_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"n={_fmt_sa(n_caco3)} mol, V={_fmt_sa(v_co2_dm3)} dm3, m={_fmt_sa(m_co2)} g",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Formula: n = m / M", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculate n(CaCO3) = {_fmt_sa(n_caco3)} mol", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Mole ratio 1:1 statement", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculate V(CO2) at STP = {_fmt_sa(v_co2_dm3)} dm3", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculate m(CO2) = {_fmt_sa(m_co2)} g", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "forgot_stp_molar_volume_22_4", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "$n = \\frac{m}{M}$ and at STP $V = n \\times V_m$ where $V_m = 22{{,}}4\\text{ dm}^3\\cdot\\text{mol}^{-1}$.",
            "tier_2": "The balanced chemical equation shows a 1:1 mole ratio between calcium carbonate and carbon dioxide.",
            "tier_3": f"$n = {_fmt_sa(n_caco3)}\\text{{ mol}}$. $V = {_fmt_sa(v_co2_dm3)}\\text{{ dm}}^3$. Mass = {_fmt_sa(m_co2)}\\text{{ g}}.",
        },
        "misconception_tags": ["forgot_stp_molar_volume_22_4", "confused_moles_and_mass"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)
    if mode == "elementary_empirical":
        return _build_empirical_drill(r)
    elif mode == "elementary_stoich":
        return _build_stoich_stp_drill(r)
    else:
        choice = r.choice(["empirical", "stoich"])
        if choice == "empirical":
            return _build_empirical_drill(r)
        else:
            return _build_stoich_stp_drill(r)
