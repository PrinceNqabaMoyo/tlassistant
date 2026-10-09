"""Grade 11 Physical Sciences — Energy & Chemical Change Generator.
Deterministic 6-pillar CAPS question generator covering Paper 2 (Chemistry Term 3):
- Exothermic vs endothermic reactions: energy absorption vs energy release.
- Enthalpy change: Delta H = H_products - H_reactants (Delta H < 0 exothermic, Delta H > 0 endothermic).
- Bond energy calculations: Delta H = sum(Bond energies broken) - sum(Bond energies formed).
- Potential energy profiles (reaction coordinate diagrams):
  Activation energy (E_A), activated complex, enthalpy change (Delta H), reverse activation energy.
- Effect of catalysts: lowers activation energy by providing alternative reaction pathway.

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


def _fmt_sa(val: float | int, places: int = 1) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


BOND_ENERGY_REACTIONS = [
    {
        "name": "Synthesis of Hydrogen Chloride",
        "equation": r"\text{H}_2(\text{g}) + \text{Cl}_2(\text{g}) \to 2\text{HCl}(\text{g})",
        "broken": [("H-H", 1, 436), ("Cl-Cl", 1, 242)],
        "formed": [("H-Cl", 2, 431)],
        "type": "Exothermic",
    },
    {
        "name": "Combustion of Methane",
        "equation": r"\text{CH}_4(\text{g}) + 2\text{O}_2(\text{g}) \to \text{CO}_2(\text{g}) + 2\text{H}_2\text{O}(\text{g})",
        "broken": [("C-H", 4, 413), ("O=O", 2, 498)],
        "formed": [("C=O (in CO2)", 2, 799), ("O-H", 4, 463)],
        "type": "Exothermic",
    },
    {
        "name": "Synthesis of Ammonia (Haber process)",
        "equation": r"\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \to 2\text{NH}_3(\text{g})",
        "broken": [("N≡N", 1, 945), ("H-H", 3, 436)],
        "formed": [("N-H", 6, 391)],
        "type": "Exothermic",
    },
]


def _build_bond_energy_drill(r: random.Random) -> Dict[str, Any]:
    rxn = r.choice(BOND_ENERGY_REACTIONS)

    energy_broken = sum(count * be for _, count, be in rxn["broken"])
    energy_formed = sum(count * be for _, count, be in rxn["formed"])
    delta_h = energy_broken - energy_formed

    broken_str = " + ".join([f"{count} \\times {be}\\text{{ (for {name})}}" for name, count, be in rxn["broken"]])
    formed_str = " + ".join([f"{count} \\times {be}\\text{{ (for {name})}}" for name, count, be in rxn["formed"]])

    bond_table_lines = []
    for name, _, be in rxn["broken"] + rxn["formed"]:
        bond_table_lines.append(f"- **{name}:** ${be}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$")
    bonds_text = "\n".join(dict.fromkeys(bond_table_lines))

    prompt = (
        f"Consider the balanced chemical equation below:\n\n"
        f"$${rxn['equation']}$$\n\n"
        f"The following average bond energies are provided:\n"
        f"{bonds_text}\n\n"
        f"1. Define the term *bond energy*.\n"
        f"2. Calculate the total energy absorbed to break all bonds in the reactants.\n"
        f"3. Calculate the total energy released when new bonds are formed in the products.\n"
        f"4. Calculate the enthalpy change ($\\Delta H$) for the reaction.\n"
        f"5. State whether this reaction is **exothermic** or **endothermic**, and justify using the sign of $\\Delta H$."
    )

    sol = (
        f"1. **Bond energy:** The amount of energy required to break one mole of a specific covalent bond in the gaseous phase.\n\n"
        f"2. $\\text{{Energy absorbed (bonds broken)}} = {broken_str} = {energy_broken}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$\n\n"
        f"3. $\\text{{Energy released (bonds formed)}} = {formed_str} = {energy_formed}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$\n\n"
        f"4. $\\Delta H = \\sum \\text{{Bond energy (broken)}} - \\sum \\text{{Bond energy (formed)}}$\n"
        f"   $\\Delta H = {energy_broken} - {energy_formed} = {delta_h}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$\n\n"
        f"5. The reaction is **{rxn['type']}** because $\\Delta H < 0$ (energy released in bond formation exceeds energy absorbed in bond breaking)."
    )

    return {
        "id": f"g11_ps_energy_bond_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Delta H = {delta_h} kJ/mol, {rxn['type']}",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: Energy required to break one mole of a bond", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculate energy absorbed = {energy_broken} kJ/mol", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate energy released = {energy_formed} kJ/mol", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Formula: Delta H = Bonds broken - Bonds formed", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculate Delta H = {delta_h} kJ/mol", "marks": 1, "editable": True},
                {"id": "mp6", "desc": f"Classification: {rxn['type']} with Delta H justification", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "inverted_bond_energy_formula", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Breaking bonds ABSORBS energy (+); forming bonds RELEASES energy (-).",
            "tier_2": "$\\Delta H = \\sum BE(\\text{bonds broken}) - \\sum BE(\\text{bonds formed})$.",
            "tier_3": f"$\\Delta H = {energy_broken} - {energy_formed} = {delta_h}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$.",
        },
        "misconception_tags": ["inverted_bond_energy_formula", "sign_error_delta_h"],
        "term": 3,
        "caps_weight_percent": 14,
        "suggested_duration_mins": 5,
    }


def _build_profile_drill(r: random.Random) -> Dict[str, Any]:
    is_exo = r.choice([True, False])
    h_reactants = r.choice([150, 180, 200, 220])
    ea = r.choice([80, 100, 120, 150])
    h_complex = h_reactants + ea

    if is_exo:
        delta_val = r.choice([40, 60, 80, 100])
        h_products = h_reactants - delta_val
        delta_h = -delta_val
        reaction_type = "Exothermic"
    else:
        delta_val = r.choice([30, 50, 70, 90])
        h_products = h_reactants + delta_val
        delta_h = delta_val
        reaction_type = "Endothermic"

    ea_rev = h_complex - h_products
    catalyst_lowering = r.choice([20, 30, 40])
    ea_cat = ea - catalyst_lowering

    prompt = (
        f"A hypothetical reversible reaction has the following energy values along its reaction pathway:\n\n"
        f"- Potential energy of reactants: **${h_reactants}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$**\n"
        f"- Potential energy of activated complex: **${h_complex}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$**\n"
        f"- Potential energy of products: **${h_products}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$**\n\n"
        f"1. Define the term *activation energy* ($E_A$).\n"
        f"2. Calculate the activation energy ($E_A$) for the forward reaction.\n"
        f"3. Calculate the enthalpy change ($\\Delta H$) for the forward reaction.\n"
        f"4. Calculate the activation energy ($E_{{A,\\text{{rev}}}}$) for the reverse reaction.\n"
        f"5. A catalyst is added that lowers the activation energy by **${catalyst_lowering}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$**. "
        f"What is the new $\\Delta H$ of the catalysed reaction?"
    )

    sol = (
        f"1. **Activation energy:** The minimum amount of energy required to initiate a chemical reaction.\n\n"
        f"2. $E_A = H_{{\\text{{complex}}}} - H_{{\\text{{reactants}}}} = {h_complex} - {h_reactants} = {ea}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$\n\n"
        f"3. $\\Delta H = H_{{\\text{{products}}}} - H_{{\\text{{reactants}}}} = {h_products} - {h_reactants} = {delta_h}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$ ({reaction_type})\n\n"
        f"4. $E_{{A,\\text{{rev}}}} = H_{{\\text{{complex}}}} - H_{{\\text{{products}}}} = {h_complex} - {h_products} = {ea_rev}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$\n\n"
        f"5. **Remains unchanged (${delta_h}\\text{{ kJ}}\\cdot\\text{{mol}}^{{-1}}$).** A catalyst lowers the activation energy of both forward and reverse reactions equally and does not alter the enthalpy change ($\\Delta H$)."
    )

    return {
        "id": f"g11_ps_energy_prof_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"EA={ea} kJ/mol, Delta H={delta_h} kJ/mol, EA_rev={ea_rev} kJ/mol",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Definition of activation energy", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculate EA = {ea} kJ/mol", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculate Delta H = {delta_h} kJ/mol", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculate EA_reverse = {ea_rev} kJ/mol", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "State Delta H unchanged with catalyst", "marks": 1, "editable": True},
                {"id": "mp6", "desc": "Justification: Catalyst does not affect reactant or product enthalpy", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "catalyst_changes_delta_h_fallacy", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "$E_A = H_{\\text{complex}} - H_{\\text{reactants}}$, $\\Delta H = H_{\\text{products}} - H_{\\text{reactants}}$.",
            "tier_2": "For the reverse reaction, the products become the reactants: $E_{A,\\text{rev}} = H_{\\text{complex}} - H_{\\text{products}}$.",
            "tier_3": f"$E_A = {ea}\\text{{ kJ/mol}}$. $\\Delta H = {delta_h}\\text{{ kJ/mol}}$. Catalysts never change $\\Delta H$.",
        },
        "misconception_tags": ["catalyst_changes_delta_h_fallacy", "confused_activation_energy_with_enthalpy"],
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)
    if mode == "elementary_bond_energy":
        return _build_bond_energy_drill(r)
    elif mode == "elementary_potential_energy_diagram":
        return _build_profile_drill(r)
    else:
        choice = r.choice(["bond", "profile"])
        if choice == "bond":
            return _build_bond_energy_drill(r)
        else:
            return _build_profile_drill(r)
