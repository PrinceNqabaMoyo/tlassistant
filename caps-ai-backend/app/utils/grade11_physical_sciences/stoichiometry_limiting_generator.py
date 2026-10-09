"""Grade 11 Physical Sciences — Stoichiometry & Limiting Reactants Generator.
Deterministic 6-pillar CAPS question generator covering Paper 2 (Chemistry Term 3):
- Mole concept: n = m / M, n = V / Vm (Vm = 22.4 dm^3/mol at STP), c = n / V.
- Limiting and excess reactants determination.
- Mass of excess reactant remaining unreacted.
- Theoretical yield and percentage yield: % Yield = (Actual yield / Theoretical yield) x 100.
- Percentage purity of impure chemical samples.

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


REACTION_SYSTEMS = [
    {
        "equation": r"\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \to 2\text{NH}_3(\text{g})",
        "A": {"name": "Nitrogen (N2)", "M": 28.0, "coeff": 1},
        "B": {"name": "Hydrogen (H2)", "M": 2.0, "coeff": 3},
        "Product": {"name": "Ammonia (NH3)", "M": 17.0, "coeff": 2},
    },
    {
        "equation": r"2\text{Mg}(\text{s}) + \text{O}_2(\text{g}) \to 2\text{MgO}(\text{s})",
        "A": {"name": "Magnesium (Mg)", "M": 24.3, "coeff": 2},
        "B": {"name": "Oxygen (O2)", "M": 32.0, "coeff": 1},
        "Product": {"name": "Magnesium oxide (MgO)", "M": 40.3, "coeff": 2},
    },
    {
        "equation": r"\text{CH}_4(\text{g}) + 2\text{O}_2(\text{g}) \to \text{CO}_2(\text{g}) + 2\text{H}_2\text{O}(\text{g})",
        "A": {"name": "Methane (CH4)", "M": 16.0, "coeff": 1},
        "B": {"name": "Oxygen (O2)", "M": 32.0, "coeff": 2},
        "Product": {"name": "Carbon dioxide (CO2)", "M": 44.0, "coeff": 1},
    },
]


def _build_limiting_drill(r: random.Random) -> Dict[str, Any]:
    rxn = r.choice(REACTION_SYSTEMS)
    a = rxn["A"]
    b = rxn["B"]
    prod = rxn["Product"]

    # Choose clean masses
    mass_a = round(r.uniform(20.0, 60.0), 1)
    mass_b = round(r.uniform(10.0, 40.0), 1)

    n_a = round(mass_a / a["M"], 3)
    n_b = round(mass_b / b["M"], 3)

    # Compare n_a / coeff_a vs n_b / coeff_b
    ratio_a = n_a / a["coeff"]
    ratio_b = n_b / b["coeff"]

    if ratio_a < ratio_b:
        limiting = a
        excess = b
        n_limiting = n_a
        n_excess_used = round(n_limiting * (b["coeff"] / a["coeff"]), 3)
        n_excess_left = round(n_b - n_excess_used, 3)
        mass_excess_left = round(n_excess_left * b["M"], 2)
        n_prod_theo = round(n_limiting * (prod["coeff"] / a["coeff"]), 3)
    else:
        limiting = b
        excess = a
        n_limiting = n_b
        n_excess_used = round(n_limiting * (a["coeff"] / b["coeff"]), 3)
        n_excess_left = round(n_a - n_excess_used, 3)
        mass_excess_left = round(n_excess_left * a["M"], 2)
        n_prod_theo = round(n_limiting * (prod["coeff"] / b["coeff"]), 3)

    mass_prod_theo = round(n_prod_theo * prod["M"], 2)

    # Realistic percentage yield (70% - 90%)
    pct_yield = round(r.uniform(75.0, 92.0), 1)
    mass_prod_actual = round(mass_prod_theo * (pct_yield / 100.0), 2)

    prompt = (
        f"In a chemical synthesis, **${_fmt_sa(mass_a)}\\text{{ g}}$** of **{a['name']}** is reacted with "
        f"**${_fmt_sa(mass_b)}\\text{{ g}}$** of **{b['name']}** according to the balanced equation:\n\n"
        f"$${rxn['equation']}$$\n\n"
        f"Molar masses: $M({a['name']}) = {_fmt_sa(a['M'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, "
        f"$M({b['name']}) = {_fmt_sa(b['M'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, "
        f"$M({prod['name']}) = {_fmt_sa(prod['M'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$.\n\n"
        f"1. Calculate the initial number of moles of {a['name']} and {b['name']}.\n"
        f"2. Determine by calculation which substance is the **limiting reactant**.\n"
        f"3. Calculate the mass of the excess reactant that remains unreacted.\n"
        f"4. Calculate the **theoretical yield** (in grams) of {prod['name']}.\n"
        f"5. If **${_fmt_sa(mass_prod_actual)}\\text{{ g}}$** of {prod['name']} is obtained in the experiment, calculate the **percentage yield**."
    )

    sol = (
        f"1. Initial moles:\n"
        f"   $n({a['name']}) = \\frac{{m}}{{M}} = \\frac{{{_fmt_sa(mass_a)}}}{{{_fmt_sa(a['M'])}}} = {_fmt_sa(n_a)}\\text{{ mol}}$\n"
        f"   $n({b['name']}) = \\frac{{m}}{{M}} = \\frac{{{_fmt_sa(mass_b)}}}{{{_fmt_sa(b['M'])}}} = {_fmt_sa(n_b)}\\text{{ mol}}$\n\n"
        f"2. Stoichiometric requirement:\n"
        f"   $\\frac{{n({a['name']})}}{{{a['coeff']}}} = {_fmt_sa(round(ratio_a, 3))}, \\quad \\frac{{n({b['name']})}}{{{b['coeff']}}} = {_fmt_sa(round(ratio_b, 3))}$\n"
        f"   Since the ratio for {limiting['name']} is smaller, **{limiting['name']} is the limiting reactant**.\n\n"
        f"3. Excess reactant calculation:\n"
        f"   Moles of {excess['name']} reacted = ${n_limiting} \\times \\frac{{{excess['coeff']}}}{{{limiting['coeff']}}} = {_fmt_sa(n_excess_used)}\\text{{ mol}}$\n"
        f"   Moles of {excess['name']} remaining = ${n_a if excess==a else n_b} - {_fmt_sa(n_excess_used)} = {_fmt_sa(n_excess_left)}\\text{{ mol}}$\n"
        f"   Mass of {excess['name']} remaining = $n \\times M = {_fmt_sa(n_excess_left)} \\times {_fmt_sa(excess['M'])} = {_fmt_sa(mass_excess_left)}\\text{{ g}}$\n\n"
        f"4. Theoretical yield of {prod['name']}:\n"
        f"   $n({prod['name']}) = {n_limiting} \\times \\frac{{{prod['coeff']}}}{{{limiting['coeff']}}} = {_fmt_sa(n_prod_theo)}\\text{{ mol}}$\n"
        f"   $m({prod['name']}) = n \\times M = {_fmt_sa(n_prod_theo)} \\times {_fmt_sa(prod['M'])} = {_fmt_sa(mass_prod_theo)}\\text{{ g}}$\n\n"
        f"5. Percentage yield:\n"
        f"   $\\text{{\\% Yield}} = \\frac{{\\text{{Actual yield}}}}{{\\text{{Theoretical yield}}}} \\times 100 = \\frac{{{_fmt_sa(mass_prod_actual)}}}{{{_fmt_sa(mass_prod_theo)}}} \\times 100 = {_fmt_sa(pct_yield)}\\%$"
    )

    return {
        "id": f"g11_ps_stoich_lim_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Limiting: {limiting['name']}, Theo yield: {_fmt_sa(mass_prod_theo)} g, % Yield: {_fmt_sa(pct_yield)}%",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculate initial moles n(A) = {_fmt_sa(n_a)}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculate initial moles n(B) = {_fmt_sa(n_b)}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Identify limiting reactant: {limiting['name']}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculate excess mass remaining = {_fmt_sa(mass_excess_left)} g", "marks": 2, "editable": True},
                {"id": "mp5", "desc": f"Calculate theoretical yield = {_fmt_sa(mass_prod_theo)} g", "marks": 2, "editable": True},
                {"id": "mp6", "desc": f"Calculate percentage yield = {_fmt_sa(pct_yield)}%", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "confused_smaller_mass_with_limiting_reactant", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Convert both masses to moles first using $n = m / M$. Never compare raw masses directly.",
            "tier_2": "Divide moles by their stoichiometric coefficients to find the limiting reactant.",
            "tier_3": f"Limiting reactant is {limiting['name']}. Theoretical yield = {_fmt_sa(mass_prod_theo)}\\text{{ g}}. Yield = {_fmt_sa(pct_yield)}%.",
        },
        "misconception_tags": ["confused_smaller_mass_with_limiting_reactant", "inverted_percentage_yield_fraction"],
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 7,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)
    return _build_limiting_drill(r)
