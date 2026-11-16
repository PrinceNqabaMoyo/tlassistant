"""Grade 11 Physical Sciences — Energy and Chemical Change (Subskills 01–25).
Grounded strictly in:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 3/02. Energy and chemical change.md

Covers:
- Enthalpy (H), chemical system vs surroundings, heat of reaction ΔH = E_prod - E_react
- Bond breaking (endothermic) vs bond formation (exothermic), potential energy vs internuclear distance curves
- Exothermic vs endothermic reactions, thermochemical equation notations, stoichiometric scaling & reversibility
- Physical phase changes, photosynthesis, respiration, combustion, limestone kiln decomposition
- Lab investigations (citric acid + NaHCO3, steel wool + O2, salt dissolutions, neutralisation) and calorimetry (q = mcΔT)
- Bond dissociation energy enthalpy calculations and unknown bond energy solving.

Zero-LLM: 100% deterministic Python with seed-varied parameters, South African comma decimals, and inline SVG diagrams.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


TOPIC = "physical_sciences_electrochemistry"
LO = "phys11_energy_chemical_change"


def _fmt_sa(val: float, decimals: int = 1) -> str:
    """Format a float with South African comma decimal separator."""
    rounded = round(val, decimals)
    if decimals == 0 or abs(rounded - round(rounded)) < 1e-6:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _svg_wrap(inner: str, width: int = 380, height: int = 230) -> str:
    """Wrap SVG markup on a clean, high-contrast scientific canvas."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" '
        f'style="background:#ffffff;border:1px solid #cbd5e1;border-radius:6px;">'
        f"{inner}</svg>"
    )


def _pillars(
    qid: str,
    subskill: str,
    prompt: str,
    answer: str,
    sample: str,
    marking_points: List[Dict[str, Any]],
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 3,
    duration: int = 4,
    diagram_spec: Optional[Dict[str, Any]] = None,
    question_type: str = "typed",
    options: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Assemble standardized 6-pillar Grade 11 Energy & Chemical Change payload."""
    total_marks = sum(int(mp.get("marks", 1)) for mp in marking_points) if marking_points else marks
    payload: Dict[str, Any] = {
        "id": qid,
        "question_id": qid,
        "topic": "Energy and chemical change",
        "subskill": subskill,
        "learning_objective_id": LO,
        "subject": "Physical Sciences",
        "grade": 11,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": duration,
        "mode": f"elementary_{subskill}",
        "question_type": question_type,
        "prompt": prompt,
        "question_text": prompt,
        "correct_answer": answer,
        "expected_answer": answer,
        "answer_latex": answer,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": total_marks,
        "marking_schema": {
            "total_marks": total_marks,
            "marking_points": marking_points,
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "hint_sections": hints,
        "misconception_tags": misconception_tags,
    }
    if options:
        payload["options"] = options
    if diagram_spec is not None:
        payload["diagram_spec"] = diagram_spec
    return payload


# =========================================================================== #
# 01: Chemical System, Enthalpy & Heat of Reaction
# =========================================================================== #
def build_01_chemical_system_and_enthalpy_definition(rng: random.Random) -> Dict[str, Any]:
    e_react = rng.choice([80, 110, 140, 180])
    e_prod = rng.choice([45, 60, 210, 250])
    dh = e_prod - e_react
    kind = "exothermic" if dh < 0 else "endothermic"
    prompt = (
        f"In a closed chemical system at constant pressure, the total chemical potential energy (enthalpy) of the reactants "
        f"is ${e_react}\\text{{ kJ·mol}}^{{-1}}$ and that of the products is ${e_prod}\\text{{ kJ·mol}}^{{-1}}$.\n\n"
        f"1. Define **enthalpy ($H$)** and **heat of reaction ($\\Delta H$)**.\n"
        f"2. Calculate $\\Delta H$ for this reaction and classify it as exothermic or endothermic."
    )
    ans = f"ΔH = {dh} kJ/mol ({kind})"
    sample = (
        f"1. **Enthalpy ($H$)** is a measure of the total energy of a chemical system at a given pressure. "
        f"**Heat of reaction ($\\Delta H$)** is the net energy absorbed or released per mole during a chemical reaction ($\Delta H = E_{{\\text{{prod}}}} - E_{{\\text{{react}}}}$).\n"
        f"2. $\\Delta H = {e_prod} - {e_react} = {'+' if dh > 0 else ''}{dh}\\text{{ kJ·mol}}^{{-1}}$. Since $\\Delta H {'<' if dh < 0 else '>'} 0$, the reaction is **{kind}**."
    )
    return _pillars(
        qid=f"ps11_e01_{rng.randint(10000, 99999)}",
        subskill="01_chemical_system_and_enthalpy_definition",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Accurate definitions of enthalpy and heat of reaction", "marks": 2},
            {"id": "mp2", "desc": f"ΔH = {e_prod} - {e_react} = {dh} kJ/mol", "marks": 1},
            {"id": "mp3", "desc": f"Classify as {kind}", "marks": 1},
        ],
        hints={
            "1_nudge": "Remember the formula: ΔH = E(products) - E(reactants).",
            "2_concept": "Negative ΔH indicates energy was released (exothermic); positive ΔH indicates energy was absorbed (endothermic).",
            "3_breakdown": sample,
        },
        misconception_tags=["subtracting_reactants_minus_products"],
        marks=4,
        duration=4,
    )


# =========================================================================== #
# 02: Bond Breaking is Endothermic
# =========================================================================== #
def build_02_bond_breaking_endothermic_energy_absorbed(rng: random.Random) -> Dict[str, Any]:
    bonds = [
        ("HCl(g) → H(g) + Cl(g)", "H–Cl", 431),
        ("N₂(g) → 2N(g)", "N≡N", 945),
        ("CO(g) → C(g) + O(g)", "C≡O", 1072),
        ("Cl₂(g) → 2Cl(g)", "Cl–Cl", 243),
        ("O₂(g) → 2O(g)", "O=O", 498),
    ]
    eq, b_name, energy = rng.choice(bonds)
    moles = rng.choice([1, 2, 3])
    total_e = moles * energy
    prompt = (
        f"Consider the bond dissociation process: $${eq}$$\n"
        f"The bond energy of the **{b_name}** bond is ${energy}\\text{{ kJ·mol}}^{{-1}}$.\n\n"
        f"1. State whether energy is **absorbed** or **released** when {b_name} bonds break, and explain why.\n"
        f"2. Calculate the energy change when ${moles}\\text{{ mol}}$ of {b_name} bonds break completely."
    )
    ans = f"Absorbed (endothermic); +{total_e} kJ"
    sample = (
        f"1. Energy is **absorbed** (endothermic process) because work must be done to overcome the electrostatic attraction holding the bonded atoms together.\n"
        f"2. Energy absorbed = ${moles} \\times {energy} = +{total_e}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e02_{rng.randint(10000, 99999)}",
        subskill="02_bond_breaking_endothermic_energy_absorbed",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "State energy is absorbed (endothermic)", "marks": 1},
            {"id": "mp2", "desc": "Explain overcoming attractive force between nuclei and shared electrons", "marks": 1},
            {"id": "mp3", "desc": f"Calculate +{total_e} kJ", "marks": 1},
        ],
        hints={
            "1_nudge": "Breaking any stable chemical bond always requires pulling attracted atoms apart.",
            "2_concept": "Bond breaking is ALWAYS endothermic (energy absorbed > 0).",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_breaking_bonds_releases_energy"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 03: Bond Forming is Exothermic
# =========================================================================== #
def build_03_bond_forming_exothermic_energy_released(rng: random.Random) -> Dict[str, Any]:
    bonds = [
        ("H(g) + F(g) → HF(g)", "H–F", 565),
        ("2N(g) → N₂(g)", "N≡N", 945),
        ("H(g) + H(g) → H₂(g)", "H–H", 436),
        ("2Br(g) → Br₂(g)", "Br–Br", 193),
    ]
    eq, b_name, energy = rng.choice(bonds)
    moles = rng.choice([2, 3, 4])
    total_e = moles * energy
    prompt = (
        f"Consider the bond formation process: $${eq}$$\n"
        f"The bond dissociation energy of **{b_name}** is ${energy}\\text{{ kJ·mol}}^{{-1}}$.\n\n"
        f"1. State whether energy is **absorbed** or **released** when new {b_name} bonds form.\n"
        f"2. Calculate $\\Delta H$ when ${moles}\\text{{ mol}}$ of {b_name} bonds form from isolated gaseous atoms."
    )
    ans = f"Released (exothermic); ΔH = -{total_e} kJ"
    sample = (
        f"1. Energy is **released** (exothermic process) because atoms move into a lower, more stable potential energy state.\n"
        f"2. $\\Delta H = -{moles} \\times {energy} = -{total_e}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e03_{rng.randint(10000, 99999)}",
        subskill="03_bond_forming_exothermic_energy_released",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "State energy is released (exothermic)", "marks": 1},
            {"id": "mp2", "desc": f"Calculate ΔH = -{total_e} kJ (correct negative sign)", "marks": 2},
        ],
        hints={
            "1_nudge": "Forming a chemical bond lowers the system's potential energy.",
            "2_concept": "Bond formation is ALWAYS exothermic (energy released, ΔH < 0).",
            "3_breakdown": sample,
        },
        misconception_tags=["writing_positive_ΔH_for_bond_formation"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 04: Potential Energy vs Internuclear Distance Curve (Inline SVG)
# =========================================================================== #
def build_04_potential_energy_vs_internuclear_distance_bond(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {"dir": "from X to A", "process": "bond breaking", "energy_change": "increases (energy absorbed)", "r0": 74, "eb": 436},
        {"dir": "from A to X", "process": "bond formation", "energy_change": "decreases (energy released)", "r0": 127, "eb": 431},
    ]
    c = rng.choice(cases)
    svg = _svg_wrap(
        f'<line x1="55" y1="20" x2="55" y2="195" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="45" y1="95" x2="340" y2="95" stroke="#64748b" stroke-dasharray="4,3"/>'
        f'<text x="15" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">E</text>'
        f'<text x="240" y="110" font-family="sans-serif" font-size="11" fill="#0f172a">Internuclear distance</text>'
        f'<path d="M 80 25 Q 105 185, 145 170 Q 190 150, 260 100 L 325 96" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<circle cx="145" cy="170" r="4.5" fill="#dc2626"/>'
        f'<circle cx="295" cy="96" r="4.5" fill="#16a34a"/>'
        f'<text x="145" y="188" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">X ({c["r0"]} pm, -{c["eb"]})</text>'
        f'<text x="295" y="84" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#16a34a">A (separated)</text>',
        width=360,
        height=210,
    )
    prompt = (
        f"Refer to the potential energy curve against internuclear distance for a diatomic covalent bond.\n\n"
        f"Suppose the two atoms move **{c['dir']}** along the curve:\n"
        f"1. Identify whether this shift represents **bond breaking** or **bond formation**.\n"
        f"2. State how the potential energy of the system changes and whether energy is absorbed or released."
    )
    ans = f"{c['process']}; potential energy {c['energy_change']}"
    sample = (
        f"1. Moving {c['dir']} corresponds to **{c['process']}**.\n"
        f"2. Along this path, the system's potential energy **{c['energy_change']}**."
    )
    return _pillars(
        qid=f"ps11_e04_{rng.randint(10000, 99999)}",
        subskill="04_potential_energy_vs_internuclear_distance_bond",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Identify {c['process']}", "marks": 1},
            {"id": "mp2", "desc": f"Potential energy {c['energy_change']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Point X is the bonded state at minimum potential energy; point A represents separated atoms at E ≈ 0.",
            "2_concept": "Moving away from X breaks the bond (energy increases); moving into X forms the bond (energy decreases).",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_distance_increase_with_energy_release"],
        marks=3,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Internuclear PE curve ({c['dir']}, r0={c['r0']} pm)"},
    )


# =========================================================================== #
# 05: Exothermic Energy Balance Criteria
# =========================================================================== #
def build_05_exothermic_energy_balance_criteria(rng: random.Random) -> Dict[str, Any]:
    e_broken = rng.choice([550, 680, 720])
    e_formed = e_broken + rng.choice([180, 240, 320])
    dh = e_broken - e_formed
    prompt = (
        f"During a chemical reaction, ${e_broken}\\text{{ kJ}}$ of energy is absorbed to break the bonds in the reactants, "
        f"and ${e_formed}\\text{{ kJ}}$ of energy is released when new product bonds form.\n\n"
        f"1. Calculate the overall heat of reaction ($\\Delta H$).\n"
        f"2. State whether the reaction is exothermic or endothermic and compare $E_{{\\text{{products}}}}$ to $E_{{\\text{{reactants}}}}$."
    )
    ans = f"ΔH = {dh} kJ; exothermic (E_products < E_reactants)"
    sample = (
        f"1. $\\Delta H = E_{{\\text{{broken}}}} - E_{{\\text{{formed}}}} = {e_broken} - {e_formed} = {dh}\\text{{ kJ}}$.\n"
        f"2. Because more energy is released forming product bonds than absorbed breaking reactant bonds ($\\Delta H < 0$), "
        f"the reaction is **exothermic**, and $E_{{\\text{{products}}}} < E_{{\\text{{reactants}}}}$."
    )
    return _pillars(
        qid=f"ps11_e05_{rng.randint(10000, 99999)}",
        subskill="05_exothermic_energy_balance_criteria",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Calculate ΔH = {dh} kJ", "marks": 1},
            {"id": "mp2", "desc": "Classify as exothermic with E_products < E_reactants", "marks": 2},
        ],
        hints={
            "1_nudge": "Compare energy absorbed (bonds broken) vs energy released (bonds formed).",
            "2_concept": "Exothermic: energy released > energy absorbed, so net energy leaves to the surroundings.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_products_have_higher_energy_in_exothermic"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 06: Endothermic Energy Balance Criteria
# =========================================================================== #
def build_06_endothermic_energy_balance_criteria(rng: random.Random) -> Dict[str, Any]:
    e_broken = rng.choice([850, 920, 1050])
    e_formed = e_broken - rng.choice([150, 220, 310])
    dh = e_broken - e_formed
    prompt = (
        f"In a synthesis reaction, ${e_broken}\\text{{ kJ}}$ of energy is required to break reactant bonds, "
        f"while only ${e_formed}\\text{{ kJ}}$ is released when new product bonds form.\n\n"
        f"1. Calculate $\\Delta H$ for the reaction.\n"
        f"2. Classify the reaction and state how the temperature of the surrounding container changes if unheated."
    )
    ans = f"ΔH = +{dh} kJ; endothermic; surrounding temperature decreases"
    sample = (
        f"1. $\\Delta H = {e_broken} - {e_formed} = +{dh}\\text{{ kJ}}$.\n"
        f"2. Since energy absorbed exceeds energy released ($\\Delta H > 0$), the reaction is **endothermic**. "
        f"Heat is absorbed from the surroundings, causing the container temperature to **decrease**."
    )
    return _pillars(
        qid=f"ps11_e06_{rng.randint(10000, 99999)}",
        subskill="06_endothermic_energy_balance_criteria",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Calculate ΔH = +{dh} kJ", "marks": 1},
            {"id": "mp2", "desc": "Endothermic classification and surrounding temperature decreases", "marks": 2},
        ],
        hints={
            "1_nudge": "If energy absorbed > energy released, the system takes net energy FROM the surroundings.",
            "2_concept": "When a system absorbs heat from the surroundings, the thermometer in the surroundings drops.",
            "3_breakdown": sample,
        },
        misconception_tags=["thinking_endothermic_reaction_makes_thermometer_rise"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 07: Thermochemical Equation with Heat on Right
# =========================================================================== #
def build_07_thermochemical_equation_heat_term_right(rng: random.Random) -> Dict[str, Any]:
    rxns = [
        ("C(s) + O₂(g) → CO₂(g) + 393 kJ·mol⁻¹", 393),
        ("H₂(g) + I₂(g) → 2HI(g) + 21 kJ·mol⁻¹", 21),
        ("N₂(g) + 3H₂(g) → 2NH₃(g) + 92 kJ·mol⁻¹", 92),
    ]
    eq, q_val = rng.choice(rxns)
    prompt = (
        f"Given the thermochemical equation:\n$${eq}$$\n\n"
        f"1. State whether this reaction is exothermic or endothermic and give a reason.\n"
        f"2. Rewrite the reaction using $\\Delta H$ notation."
    )
    ans = f"Exothermic (energy appears on product side); ΔH = -{q_val} kJ/mol"
    sample = (
        f"1. **Exothermic**, because energy ($+{q_val}\\text{{ kJ·mol}}^{{-1}}$) is written on the right-hand (product) side, indicating energy is released.\n"
        f"2. {eq.split(' + ' + str(q_val))[0]}   $\\Delta H = -{q_val}\\text{{ kJ·mol}}^{{-1}}$."
    )
    return _pillars(
        qid=f"ps11_e07_{rng.randint(10000, 99999)}",
        subskill="07_thermochemical_equation_heat_term_right",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Classify as exothermic (heat released as product)", "marks": 2},
            {"id": "mp2", "desc": f"Write ΔH = -{q_val} kJ/mol", "marks": 1},
        ],
        hints={
            "1_nudge": "Reactants -> Products + Energy means energy is produced/released.",
            "2_concept": "Exothermic equations have negative ΔH.",
            "3_breakdown": sample,
        },
        misconception_tags=["writing_positive_ΔH_when_energy_is_on_RHS"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 08: Thermochemical Equation with Heat on Left
# =========================================================================== #
def build_08_thermochemical_equation_heat_term_left(rng: random.Random) -> Dict[str, Any]:
    rxns = [
        ("C(s) + H₂O(g) + 131 kJ·mol⁻¹ → CO(g) + H₂(g)", 131),
        ("CaCO₃(s) + 178 kJ·mol⁻¹ → CaO(s) + CO₂(g)", 178),
        ("2NH₃(g) + 92 kJ·mol⁻¹ → N₂(g) + 3H₂(g)", 92),
    ]
    eq, q_val = rng.choice(rxns)
    prompt = (
        f"Given the thermochemical equation:\n$${eq}$$\n\n"
        f"1. State whether this reaction is exothermic or endothermic and give a reason.\n"
        f"2. Write down the numerical value and sign of $\\Delta H$."
    )
    ans = f"Endothermic (energy absorbed as reactant); ΔH = +{q_val} kJ/mol"
    sample = (
        f"1. **Endothermic**, because ${q_val}\\text{{ kJ·mol}}^{{-1}}$ is written on the left-hand (reactant) side, showing heat must be absorbed.\n"
        f"2. $\\Delta H = +{q_val}\\text{{ kJ·mol}}^{{-1}}$."
    )
    return _pillars(
        qid=f"ps11_e08_{rng.randint(10000, 99999)}",
        subskill="08_thermochemical_equation_heat_term_left",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Classify as endothermic (heat absorbed on LHS)", "marks": 2},
            {"id": "mp2", "desc": f"State ΔH = +{q_val} kJ/mol", "marks": 1},
        ],
        hints={
            "1_nudge": "Reactants + Energy -> Products represents an endothermic process.",
            "2_concept": "Endothermic reactions always have ΔH > 0.",
            "3_breakdown": sample,
        },
        misconception_tags=["writing_negative_ΔH_when_energy_is_on_LHS"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 09: Thermochemical Equation ΔH Notation Conversion
# =========================================================================== #
def build_09_thermochemical_equation_delta_H_notation(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(g)", -802, "exothermic", "CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(g) + 802 kJ·mol⁻¹"),
        ("2Na(s) + Cl₂(g) → 2NaCl(s)", -822, "exothermic", "2Na(s) + Cl₂(g) → 2NaCl(s) + 822 kJ·mol⁻¹"),
        ("N₂(g) + O₂(g) → 2NO(g)", 181, "endothermic", "N₂(g) + O₂(g) + 181 kJ·mol⁻¹ → 2NO(g)"),
    ]
    eq, dh, kind, rewritten = rng.choice(cases)
    sign_dh = f"+{dh}" if dh > 0 else str(dh)
    prompt = (
        f"Consider the equation: $${eq} \\quad \\Delta H = {sign_dh}\\text{{ kJ·mol}}^{{-1}}$$\n\n"
        f"1. State whether the reaction is exothermic or endothermic.\n"
        f"2. Rewrite the thermochemical equation with the numerical heat term placed directly on the appropriate side of the arrow."
    )
    ans = f"{kind}; {rewritten}"
    sample = f"1. **{kind.capitalize()}** since $\\Delta H {'<' if dh < 0 else '>'} 0$.\n2. $${rewritten}$$"
    return _pillars(
        qid=f"ps11_e09_{rng.randint(10000, 99999)}",
        subskill="09_thermochemical_equation_delta_H_notation",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Classify as {kind}", "marks": 1},
            {"id": "mp2", "desc": f"Place +{abs(dh)} kJ/mol on {'product' if dh < 0 else 'reactant'} side", "marks": 2},
        ],
        hints={
            "1_nudge": "Never write a minus sign for energy placed directly in an equation; put it on the product side if exothermic.",
            "2_concept": "Exothermic -> +Energy on RHS; Endothermic -> +Energy on LHS.",
            "3_breakdown": sample,
        },
        misconception_tags=["putting_negative_heat_on_product_side"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 10: Molar Enthalpy Stoichiometric Scaling
# =========================================================================== #
def build_10_molar_enthalpy_stoichiometric_scaling(rng: random.Random) -> Dict[str, Any]:
    fuels = [
        {"name": "methane (CH₄)", "M": 16.0, "eq": "CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(g)", "dh": -802, "coeff": 1},
        {"name": "carbon (C)", "M": 12.0, "eq": "C(s) + O₂(g) → CO₂(g)", "dh": -393, "coeff": 1},
        {"name": "hydrogen (H₂)", "M": 2.0, "eq": "2H₂(g) + O₂(g) → 2H₂O(g)", "dh": -484, "coeff": 2},
    ]
    f = rng.choice(fuels)
    n_mol = rng.choice([0.5, 1.5, 2.5, 3.0])
    mass_g = round(n_mol * f["M"], 1)
    q_rel = round((n_mol / f["coeff"]) * abs(f["dh"]), 1)
    prompt = (
        f"The combustion of **{f['name']}** ($M = {_fmt_sa(f['M'], 1)}\\text{{ g·mol}}^{{-1}}$) follows:\n"
        f"$${f['eq']} \\quad \\Delta H = {f['dh']}\\text{{ kJ}}$$\n\n"
        f"Calculate the total thermal energy released (in kJ) when ${_fmt_sa(mass_g, 1)}\\text{{ g}}$ of {f['name']} burns completely in excess oxygen."
    )
    ans = f"{_fmt_sa(q_rel, 1)} kJ"
    sample = (
        f"1. $n = \\frac{{m}}{{M}} = \\frac{{{_fmt_sa(mass_g, 1)}}}{{{_fmt_sa(f['M'], 1)}}} = {_fmt_sa(n_mol, 1)}\\text{{ mol}}$.\n"
        f"2. From stoichiometry, {f['coeff']} mol releases {abs(f['dh'])} kJ.\n"
        f"   Energy released = $\\frac{{{_fmt_sa(n_mol, 1)}}}{{{f['coeff']}}} \\times {abs(f['dh'])} = {_fmt_sa(q_rel, 1)}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e10_{rng.randint(10000, 99999)}",
        subskill="10_molar_enthalpy_stoichiometric_scaling",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Calculate n = {_fmt_sa(n_mol, 1)} mol", "marks": 1},
            {"id": "mp2", "desc": f"Scale by stoichiometric coefficient {f['coeff']}", "marks": 1},
            {"id": "mp3", "desc": f"Energy released = {_fmt_sa(q_rel, 1)} kJ", "marks": 1},
        ],
        hints={
            "1_nudge": "Convert mass in grams to moles using n = m / M.",
            "2_concept": "Multiply (n / equation coefficient) by |ΔH|.",
            "3_breakdown": sample,
        },
        misconception_tags=["ignoring_stoichiometric_coefficient_2_in_2H2"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 11: Reversing Reaction Enthalpy Sign Flip
# =========================================================================== #
def build_11_reversing_reaction_enthalpy_sign_flip(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("N₂(g) + 3H₂(g) → 2NH₃(g)", -92, "2NH₃(g) → N₂(g) + 3H₂(g)"),
        ("CaCO₃(s) → CaO(s) + CO₂(g)", 178, "CaO(s) + CO₂(g) → CaCO₃(s)"),
        ("2H₂(g) + O₂(g) → 2H₂O(l)", -572, "2H₂O(l) → 2H₂(g) + O₂(g)"),
    ]
    fwd, dh, rev = rng.choice(pairs)
    rev_dh = -dh
    sign_f = f"+{dh}" if dh > 0 else str(dh)
    sign_r = f"+{rev_dh}" if rev_dh > 0 else str(rev_dh)
    rev_type = "endothermic" if rev_dh > 0 else "exothermic"
    prompt = (
        f"For the forward reaction:\n$${fwd} \\quad \\Delta H = {sign_f}\\text{{ kJ·mol}}^{{-1}}$$\n\n"
        f"Determine $\\Delta H$ for the reverse reaction:\n$${rev}$$\n"
        f"and state whether the reverse reaction is exothermic or endothermic."
    )
    ans = f"ΔH = {sign_r} kJ/mol ({rev_type})"
    sample = (
        f"Reversing a chemical reaction preserves the magnitude of $\\Delta H$ while inverting its sign:\n"
        f"$\\Delta H_{{\\text{{reverse}}}} = {sign_r}\\text{{ kJ·mol}}^{{-1}}$ (**{rev_type}**)."
    )
    return _pillars(
        qid=f"ps11_e11_{rng.randint(10000, 99999)}",
        subskill="11_reversing_reaction_enthalpy_sign_flip",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Invert sign: ΔH = {sign_r} kJ/mol", "marks": 2},
            {"id": "mp2", "desc": f"Classify reverse reaction as {rev_type}", "marks": 1},
        ],
        hints={
            "1_nudge": "By conservation of energy, reversing reactants and products reverses energy flow.",
            "2_concept": "ΔH(reverse) = -ΔH(forward).",
            "3_breakdown": sample,
        },
        misconception_tags=["inverting_1_over_ΔH_instead_of_negating"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 12: Physical Phase Changes (Endothermic vs Exothermic Processes)
# =========================================================================== #
def build_12_physical_phase_changes_endo_vs_exo(rng: random.Random) -> Dict[str, Any]:
    processes = [
        ("Evaporation of liquid water", "endothermic", "energy must be absorbed to overcome intermolecular hydrogen bonds so liquid particles escape into gas"),
        ("Melting of ice cubes", "endothermic", "energy is absorbed to overcome rigid lattice intermolecular forces as solid turns into liquid"),
        ("Condensation of steam on a cold window", "exothermic", "gas molecules slow down and form intermolecular hydrogen bonds, releasing latent heat"),
        ("Freezing of liquid water into ice", "exothermic", "heat energy is released to the surroundings as molecules lock into a crystal lattice"),
    ]
    proc, kind, why = rng.choice(processes)
    prompt = (
        f"Classify the physical phase change **{proc}** as an **endothermic** or **exothermic** process.\n\n"
        f"Explain your answer in terms of intermolecular forces and energy transfer."
    )
    ans = f"{kind.capitalize()} process because {why}"
    sample = f"Classification: **{kind.capitalize()} process**.\nExplanation: {why.capitalize()}."
    return _pillars(
        qid=f"ps11_e12_{rng.randint(10000, 99999)}",
        subskill="12_physical_phase_changes_endo_vs_exo",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Classify as {kind}", "marks": 1},
            {"id": "mp2", "desc": f"Explain via intermolecular forces: {why}", "marks": 2},
        ],
        hints={
            "1_nudge": "Ask whether particles move farther apart (requires overcoming IMF) or closer together (forms stronger IMF).",
            "2_concept": "Solid -> Liquid -> Gas requires energy input (endothermic); Gas -> Liquid -> Solid releases energy (exothermic).",
            "3_breakdown": sample,
        },
        misconception_tags=["thinking_freezing_is_endothermic_because_temperature_is_cold"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 13: Photosynthesis as Endothermic Solar Energy Conversion
# =========================================================================== #
def build_13_photosynthesis_endothermic_solar_energy(rng: random.Random) -> Dict[str, Any]:
    moles_gluc = rng.choice([1, 2, 3])
    dh_photo = 2803
    total_e = moles_gluc * dh_photo
    prompt = (
        f"Green plants synthesise glucose via **photosynthesis**:\n"
        f"$$6\\text{{CO}}_2(g) + 6\\text{{H}}_2\\text{{O}}(l) \\rightarrow \\text{{C}}_6\\text{{H}}_{{12}}\\text{{O}}_6(s) + 6\\text{{O}}_2(g) \\quad \\Delta H = +2\\,803\\text{{ kJ·mol}}^{{-1}}$$\n\n"
        f"1. State whether photosynthesis is exothermic or endothermic and identify the source of energy.\n"
        f"2. Calculate how much solar energy (in kJ) is stored when ${moles_gluc}\\text{{ mol}}$ of glucose forms."
    )
    ans = f"Endothermic (solar/radiant energy from sunlight); +{total_e} kJ"
    sample = (
        f"1. **Endothermic** ($\\Delta H > 0$); energy is absorbed from **sunlight (radiant energy)** and stored as chemical potential energy.\n"
        f"2. Energy absorbed = ${moles_gluc} \\times 2\\,803 = +{total_e}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e13_{rng.randint(10000, 99999)}",
        subskill="13_photosynthesis_endothermic_solar_energy",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Endothermic reaction using radiant solar energy", "marks": 2},
            {"id": "mp2", "desc": f"Calculate +{total_e} kJ", "marks": 1},
        ],
        hints={
            "1_nudge": "Notice the positive sign on ΔH (+2 803 kJ/mol).",
            "2_concept": "Sunlight supplies the activation and enthalpy energy stored in glucose.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_photosynthesis_with_exothermic_respiration"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 14: Cellular Respiration & Combustion Exothermic Reactions
# =========================================================================== #
def build_14_cellular_respiration_and_combustion_exothermic(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Cellular respiration", "C₆H₁₂O₆(s) + 6O₂(g) → 6CO₂(g) + 6H₂O(l) + energy", "cells break down glucose with oxygen to release energy for biological work"),
        ("Combustion of octane (petrol)", "2C₈H₁₈(l) + 25O₂(g) → 16CO₂(g) + 18H₂O(g) + heat", "car engines release large thermal energy while producing CO₂ emissions"),
    ]
    name, eq, desc = rng.choice(cases)
    prompt = (
        f"Consider the reaction representing **{name}**:\n$${eq}$$\n\n"
        f"1. Classify the reaction as exothermic or endothermic and state the sign of $\\Delta H$.\n"
        f"2. Explain the energy conversion taking place and identify one gaseous product formed."
    )
    ans = f"Exothermic (ΔH < 0); chemical potential energy converts to thermal/usable energy; produces CO₂"
    sample = (
        f"1. **Exothermic** reaction ($\\Delta H < 0$) because energy is released on the product side.\n"
        f"2. Chemical potential energy is released as thermal/kinetic energy as {desc}; carbon dioxide ($\\text{{CO}}_2$) is produced."
    )
    return _pillars(
        qid=f"ps11_e14_{rng.randint(10000, 99999)}",
        subskill="14_cellular_respiration_and_combustion_exothermic",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Exothermic with ΔH < 0", "marks": 1},
            {"id": "mp2", "desc": "Chemical potential energy -> heat/usable energy; CO2 produced", "marks": 2},
        ],
        hints={
            "1_nudge": "Both respiration and fuel combustion react carbon compounds with O₂ to release energy.",
            "2_concept": "Exothermic reactions release energy (ΔH < 0).",
            "3_breakdown": sample,
        },
        misconception_tags=["saying_respiration_is_endothermic"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 15: Thermal Decomposition of Limestone in Industrial Kiln
# =========================================================================== #
def build_15_thermal_decomposition_of_limestone_kiln(rng: random.Random) -> Dict[str, Any]:
    mass_kg = rng.choice([50, 100, 200])
    # CaCO3 M = 100 g/mol; ΔH = +178 kJ/mol -> 1 kg = 10 mol -> 1780 kJ/kg
    energy_kj = int((mass_kg * 1000 / 100) * 178)
    prompt = (
        f"In industry, limestone ($\\text{{CaCO}}_3$, $M = 100\\text{{ g·mol}}^{{-1}}$) is heated above $900^\\circ\\text{{C}}$ in a lime kiln "
        f"to produce quicklime ($\\text{{CaO}}$) for steelmaking and soil neutralisation:\n"
        f"$$\\text{{CaCO}}_3(s) \\rightarrow \\text{{CaO}}(s) + \\text{{CO}}_2(g) \\quad \\Delta H = +178\\text{{ kJ·mol}}^{{-1}}$$\n\n"
        f"1. State why continuous heating above $900^\\circ\\text{{C}}$ is necessary.\n"
        f"2. Calculate the heat energy (in kJ) absorbed to decompose ${mass_kg}\\text{{ kg}}$ of pure $\\text{{CaCO}}_3$."
    )
    ans = f"Endothermic reaction (ΔH > 0); {energy_kj} kJ absorbed"
    sample = (
        f"1. Thermal decomposition is **endothermic** ($\\Delta H > 0$), so continuous heat input is required to break bonds.\n"
        f"2. $n(\\text{{CaCO}}_3) = \\frac{{{mass_kg * 1000}}}{{100}} = {mass_kg * 10}\\text{{ mol}}$.\n"
        f"   Heat absorbed = ${mass_kg * 10} \\times 178 = {energy_kj}\\text{{ kJ}}$."
    )
    return _pillars(
        qid=f"ps11_e15_{rng.randint(10000, 99999)}",
        subskill="15_thermal_decomposition_of_limestone_kiln",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Endothermic decomposition requires continuous energy supply", "marks": 1},
            {"id": "mp2", "desc": f"Calculate n = {mass_kg * 10} mol", "marks": 1},
            {"id": "mp3", "desc": f"Energy = {energy_kj} kJ", "marks": 1},
        ],
        hints={
            "1_nudge": "Convert kg to grams (× 1 000) before calculating moles n = m / M.",
            "2_concept": "Multiply moles by ΔH = +178 kJ/mol.",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_kg_to_g_conversion"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 16: Endothermic Salt Dissolutions & Cold Reactions
# =========================================================================== #
def build_16_salt_dissolution_endothermic_cold_packs(rng: random.Random) -> Dict[str, Any]:
    exps = [
        {"sys": "citric acid solution + solid sodium bicarbonate (NaHCO₃)", "dt": -6, "t_init": 22},
        {"sys": "solid ammonium nitrate (NH₄NO₃) dissolving in water (instant cold pack)", "dt": -9, "t_init": 24},
        {"sys": "solid potassium nitrate (KNO₃) dissolving in water", "dt": -5, "t_init": 21},
        {"sys": "Ba(OH)₂·8H₂O(s) reacting with 2NH₄NO₃(s)", "dt": -20, "t_init": 23},
    ]
    e = rng.choice(exps)
    t_final = e["t_init"] + e["dt"]
    prompt = (
        f"In a laboratory investigation inside an insulated polystyrene cup, a learner mixes **{e['sys']}**. "
        f"The thermometer reading drops from ${e['t_init']}^\\circ\\text{{C}}$ to ${t_final}^\\circ\\text{{C}}$.\n\n"
        f"1. State whether this process is exothermic or endothermic.\n"
        f"2. Explain why the thermometer reading decreased."
    )
    ans = "Endothermic; the chemical system absorbs heat from the water/thermometer, lowering surrounding temperature"
    sample = (
        f"1. **Endothermic** ($\Delta H > 0$).\n"
        f"2. The chemical process absorbs thermal energy from the surrounding water and thermometer, reducing the kinetic energy of the solution and causing the temperature to drop by {abs(e['dt'])} °C."
    )
    return _pillars(
        qid=f"ps11_e16_{rng.randint(10000, 99999)}",
        subskill="16_salt_dissolution_endothermic_cold_packs",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Classify as endothermic", "marks": 1},
            {"id": "mp2", "desc": "System absorbs thermal energy from surrounding solution/thermometer", "marks": 2},
        ],
        hints={
            "1_nudge": "The thermometer measures the temperature of the surrounding water, not inside the chemical bonds.",
            "2_concept": "Endothermic reactions absorb energy FROM the surroundings, making the cup feel cold.",
            "3_breakdown": sample,
        },
        misconception_tags=["thinking_temperature_drop_means_exothermic"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 17: Exothermic Salt Dissolutions, Neutralisation & Steel Wool Oxidation
# =========================================================================== #
def build_17_salt_dissolution_neutralisation_exothermic(rng: random.Random) -> Dict[str, Any]:
    exps = [
        ("vinegar-washed steel wool reacting with oxygen in a sealed cup", 8, 22),
        ("solid calcium chloride (CaCl₂) dissolving in water", 12, 21),
        ("solid sodium hydroxide (NaOH) dissolving in water", 10, 20),
        ("dilute H₂SO₄(aq) neutralising NaOH(aq)", 14, 22),
    ]
    sys_name, dt, t_init = rng.choice(exps)
    t_final = t_init + dt
    prompt = (
        f"When **{sys_name}** occurs in an insulated cup, the temperature rises from ${t_init}^\\circ\\text{{C}}$ to ${t_final}^\\circ\\text{{C}}$.\n\n"
        f"1. State whether the process is exothermic or endothermic and indicate the sign of $\\Delta H$.\n"
        f"2. Explain the energy transfer responsible for the temperature increase."
    )
    ans = f"Exothermic (ΔH < 0); chemical energy is released into the surrounding water/air"
    sample = (
        f"1. **Exothermic** ($\\Delta H < 0$).\n"
        f"2. Chemical potential energy is released as heat into the surrounding solution/thermometer, increasing particle kinetic energy and raising the temperature by {dt} °C."
    )
    return _pillars(
        qid=f"ps11_e17_{rng.randint(10000, 99999)}",
        subskill="17_salt_dissolution_neutralisation_exothermic",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Classify as exothermic with ΔH < 0", "marks": 1},
            {"id": "mp2", "desc": "Heat released by chemical system warms the surroundings", "marks": 2},
        ],
        hints={
            "1_nudge": "A thermometer rise means heat flowed OUT of the reacting chemicals into the water.",
            "2_concept": "Exothermic reactions release energy (ΔH < 0).",
            "3_breakdown": sample,
        },
        misconception_tags=["thinking_temperature_rise_means_heat_was_absorbed_by_system"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 18: Polystyrene Cup Calorimetry Design (Inline SVG)
# =========================================================================== #
def build_18_polystyrene_cup_calorimetry_experimental_design(rng: random.Random) -> Dict[str, Any]:
    features = [
        ("Polystyrene cup", "acts as a poor thermal conductor (insulator) to minimise heat loss or gain to the room"),
        ("Plastic lid with small thermometer hole", "prevents heat loss via convection and evaporation of water"),
        ("Stirring rod", "ensures uniform mixing and homogeneous temperature distribution throughout the solution"),
    ]
    feat, purpose = rng.choice(features)
    svg = _svg_wrap(
        f'<polygon points="115,65 245,65 225,180 135,180" fill="#f1f5f9" stroke="#334155" stroke-width="2.5"/>'
        f'<rect x="110" y="55" width="140" height="10" rx="3" fill="#cbd5e1" stroke="#475569"/>'
        f'<rect x="176" y="20" width="8" height="135" fill="#fee2e2" stroke="#dc2626"/>'
        f'<line x1="130" y1="115" x2="230" y2="115" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="180" y="148" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#1e3a8a">Reaction mixture</text>'
        f'<text x="180" y="203" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Component: {feat}</text>',
        width=360,
        height=215,
    )
    prompt = (
        f"Refer to the coffee-cup calorimeter apparatus used to investigate exothermic and endothermic reactions.\n\n"
        f"1. State the specific scientific purpose of using the **{feat}**.\n"
        f"2. Identify one practical safety rule when diluting concentrated sulfuric acid during such calorimetry investigations."
    )
    ans = f"{feat}: {purpose}; always add concentrated acid slowly to water (never water to acid)"
    sample = (
        f"1. **{feat}**: {purpose}.\n"
        f"2. Safety rule: Always add acid slowly to water (with stirring), never water to concentrated acid, to prevent violent exothermic splashing."
    )
    return _pillars(
        qid=f"ps11_e18_{rng.randint(10000, 99999)}",
        subskill="18_polystyrene_cup_calorimetry_experimental_design",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Purpose of {feat}: {purpose}", "marks": 2},
            {"id": "mp2", "desc": "Always add acid to water safely", "marks": 1},
        ],
        hints={
            "1_nudge": "Think about controlling heat exchange with the room and keeping concentrations/temperatures uniform.",
            "2_concept": "Insulators reduce conduction; lids reduce convection/evaporation.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_polystyrene_absorbs_reaction_heat"],
        marks=3,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Calorimeter apparatus ({feat})"},
    )


# =========================================================================== #
# 19: Calorimetry Heat Calculation q = mcΔT
# =========================================================================== #
def build_19_calorimetry_heat_calculation_q_mc_deltaT(rng: random.Random) -> Dict[str, Any]:
    vol_ml = rng.choice([100, 150, 200])
    mass_g = vol_ml
    dt = rng.choice([5.0, 7.5, 10.0, 12.0])
    sign = rng.choice([1, -1])
    t1 = 22.0
    t2 = t1 + sign * dt
    # c = 4.18 J/(g*K)
    q_j = round(mass_g * 4.18 * dt, 1)
    q_kj = round(q_j / 1000, 2)
    kind = "exothermic" if sign > 0 else "endothermic"
    prompt = (
        f"In a calorimetry experiment, a reaction occurs inside ${vol_ml}\\text{{ cm}}^3$ of aqueous solution "
        f"(assume mass $= {mass_g}\\text{{ g}}$ and $c = 4{{,}}18\\text{{ J·g}}^{{-1}}\\text{{·K}}^{{-1}}$). "
        f"The temperature changes from ${_fmt_sa(t1, 1)}^\\circ\\text{{C}}$ to ${_fmt_sa(t2, 1)}^\\circ\\text{{C}}$.\n\n"
        f"1. Calculate the thermal energy $q$ (in kJ) exchanged with the solution ($q = mc\\Delta T$).\n"
        f"2. Deduce whether the chemical reaction is exothermic or endothermic."
    )
    ans = f"q = {_fmt_sa(q_kj, 2)} kJ; {kind}"
    sample = (
        f"1. $|\\Delta T| = |{_fmt_sa(t2, 1)} - {_fmt_sa(t1, 1)}| = {_fmt_sa(dt, 1)}\\text{{ K}}$.\n"
        f"   $q = mc\\Delta T = ({mass_g})(4{{,}}18)({_fmt_sa(dt, 1)}) = {_fmt_sa(q_j, 1)}\\text{{ J}} = {_fmt_sa(q_kj, 2)}\\text{{ kJ}}$.\n"
        f"2. Because the solution temperature {'rose' if sign > 0 else 'dropped'}, the reaction is **{kind}**."
    )
    return _pillars(
        qid=f"ps11_e19_{rng.randint(10000, 99999)}",
        subskill="19_calorimetry_heat_calculation_q_mc_deltaT",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"ΔT = {_fmt_sa(dt, 1)} K", "marks": 1},
            {"id": "mp2", "desc": f"q = {_fmt_sa(q_kj, 2)} kJ", "marks": 2},
            {"id": "mp3", "desc": f"Classify as {kind}", "marks": 1},
        ],
        hints={
            "1_nudge": "Use q = m × c × ΔT with m in grams and c = 4,18 J/(g·K), then divide by 1 000 for kJ.",
            "2_concept": "Temperature increase -> exothermic; temperature decrease -> endothermic.",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_to_divide_by_1000_for_kJ"],
        marks=4,
        duration=5,
    )


# =========================================================================== #
# 20: Molar Enthalpy from Calorimetry Data
# =========================================================================== #
def build_20_molar_enthalpy_from_calorimetry_data(rng: random.Random) -> Dict[str, Any]:
    n_mol = rng.choice([0.05, 0.10, 0.20])
    dh_mag = rng.choice([25.0, 30.0, 56.0])
    q_kj = round(n_mol * dh_mag, 2)
    is_exo = rng.choice([True, False])
    signed_dh = -dh_mag if is_exo else dh_mag
    obs = "rises" if is_exo else "drops"
    prompt = (
        f"When ${_fmt_sa(n_mol, 2)}\\text{{ mol}}$ of reactant reacts completely in an insulated calorimeter, "
        f"the water temperature **{obs}** and ${_fmt_sa(q_kj, 2)}\\text{{ kJ}}$ of heat is transferred between the reaction and the water.\n\n"
        f"Calculate the molar enthalpy change $\\Delta H$ (with correct sign) in $\\text{{kJ·mol}}^{{-1}}$."
    )
    sign_str = f"+{_fmt_sa(signed_dh, 1)}" if signed_dh > 0 else _fmt_sa(signed_dh, 1)
    ans = f"ΔH = {sign_str} kJ/mol"
    sample = (
        f"1. Magnitude $|\\Delta H| = \\frac{{q}}{{n}} = \\frac{{{_fmt_sa(q_kj, 2)}}}{{{_fmt_sa(n_mol, 2)}}} = {_fmt_sa(dh_mag, 1)}\\text{{ kJ·mol}}^{{-1}}$.\n"
        f"2. Since the water temperature {obs}, the reaction is {'exothermic (ΔH < 0)' if is_exo else 'endothermic (ΔH > 0)'}: "
        f"$\\Delta H = {sign_str}\\text{{ kJ·mol}}^{{-1}}$."
    )
    return _pillars(
        qid=f"ps11_e20_{rng.randint(10000, 99999)}",
        subskill="20_molar_enthalpy_from_calorimetry_data",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Divide q / n = {_fmt_sa(dh_mag, 1)} kJ/mol", "marks": 2},
            {"id": "mp2", "desc": f"Assign correct sign ({'+' if signed_dh > 0 else '-'})", "marks": 1},
        ],
        hints={
            "1_nudge": "Molar enthalpy ΔH = ± q / n.",
            "2_concept": "Water temperature rises -> exothermic (-); water temperature drops -> endothermic (+).",
            "3_breakdown": sample,
        },
        misconception_tags=["omitting_sign_on_molar_enthalpy"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 21: Bond Energy Enthalpy — Hydrogen + Halogen/Oxygen
# =========================================================================== #
def build_21_bond_energy_enthalpy_combustion_hydrogen(rng: random.Random) -> Dict[str, Any]:
    rxns = [
        {"eq": "H₂(g) + F₂(g) → 2HF(g)", "eb": 436 + 159, "ef": 2 * 565, "desc": "E(H–H)=436, E(F–F)=159, E(H–F)=565 kJ/mol"},
        {"eq": "H₂(g) + Br₂(g) → 2HBr(g)", "eb": 436 + 193, "ef": 2 * 366, "desc": "E(H–H)=436, E(Br–Br)=193, E(H–Br)=366 kJ/mol"},
        {"eq": "2H₂(g) + O₂(g) → 2H₂O(g)", "eb": 2 * 436 + 498, "ef": 4 * 464, "desc": "E(H–H)=436, E(O=O)=498, E(O–H)=464 kJ/mol"},
    ]
    r = rng.choice(rxns)
    dh = r["eb"] - r["ef"]
    prompt = (
        f"Calculate $\\Delta H$ for the gas-phase reaction:\n$${r['eq']}$$\n"
        f"given average bond energies ({r['desc']}).\n"
        f"State whether the reaction is exothermic or endothermic."
    )
    ans = f"ΔH = {dh} kJ (exothermic)"
    sample = (
        f"$\\sum E_{{\\text{{broken}}}} = {r['eb']}\\text{{ kJ}}$; $\\sum E_{{\\text{{formed}}}} = {r['ef']}\\text{{ kJ}}$.\n"
        f"$\\Delta H = {r['eb']} - {r['ef']} = {dh}\\text{{ kJ}}$ (**exothermic**)."
    )
    return _pillars(
        qid=f"ps11_e21_{rng.randint(10000, 99999)}",
        subskill="21_bond_energy_enthalpy_combustion_hydrogen",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Bonds broken = {r['eb']} kJ", "marks": 1},
            {"id": "mp2", "desc": f"Bonds formed = {r['ef']} kJ", "marks": 1},
            {"id": "mp3", "desc": f"ΔH = {dh} kJ (exothermic)", "marks": 2},
        ],
        hints={
            "1_nudge": "Count the exact number of bonds broken in reactants and formed in products.",
            "2_concept": "ΔH = ΣE(bonds broken) - ΣE(bonds formed).",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_coefficient_2_for_2HF_or_4_OH_bonds"],
        marks=4,
        duration=5,
    )


# =========================================================================== #
# 22: Bond Energy Enthalpy — Hydrocarbon Combustion
# =========================================================================== #
def build_22_bond_energy_enthalpy_combustion_hydrocarbons(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {
            "eq": "CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(g)",
            "broken": "4(C–H) + 2(O=O) = 4(413) + 2(498) = 2 648 kJ",
            "eb": 4 * 413 + 2 * 498,
            "formed": "2(C=O) + 4(O–H) = 2(799) + 4(464) = 3 454 kJ",
            "ef": 2 * 799 + 4 * 464,
        },
        {
            "eq": "CH₃OH(g) + 1,5 O₂(g) → CO₂(g) + 2H₂O(g)",
            "broken": "3(C–H) + 1(C–O) + 1(O–H) + 1,5(O=O) = 1239 + 358 + 464 + 747 = 2 808 kJ",
            "eb": 3 * 413 + 358 + 464 + 747,
            "formed": "2(C=O) + 4(O–H) = 2(799) + 4(464) = 3 454 kJ",
            "ef": 2 * 799 + 4 * 464,
        },
    ]
    c = rng.choice(cases)
    dh = c["eb"] - c["ef"]
    prompt = (
        f"Estimate $\\Delta H$ for the complete combustion reaction:\n$${c['eq']}$$\n"
        f"using average bond energies: $E(\\text{{C–H}})=413$, $E(\\text{{C–O}})=358$, $E(\\text{{O=O}})=498$, "
        f"$E(\\text{{C=O}})=799$, $E(\\text{{O–H}})=464\\text{{ kJ·mol}}^{{-1}}$."
    )
    ans = f"ΔH = {dh} kJ/mol (exothermic)"
    sample = (
        f"1. Bonds broken: {c['broken']}.\n"
        f"2. Bonds formed: {c['formed']}.\n"
        f"3. $\\Delta H = {c['eb']} - {c['ef']} = {dh}\\text{{ kJ·mol}}^{{-1}}$ (exothermic)."
    )
    return _pillars(
        qid=f"ps11_e22_{rng.randint(10000, 99999)}",
        subskill="22_bond_energy_enthalpy_combustion_hydrocarbons",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Total reactant bonds broken = {c['eb']} kJ", "marks": 2},
            {"id": "mp2", "desc": f"Total product bonds formed = {c['ef']} kJ", "marks": 2},
            {"id": "mp3", "desc": f"ΔH = {dh} kJ/mol", "marks": 1},
        ],
        hints={
            "1_nudge": "Remember CO₂ contains TWO C=O double bonds and each H₂O contains TWO O–H bonds.",
            "2_concept": "ΔH = ΣE(broken) - ΣE(formed).",
            "3_breakdown": sample,
        },
        misconception_tags=["counting_only_one_CO_double_bond_in_CO2"],
        marks=5,
        duration=6,
    )


# =========================================================================== #
# 23: Bond Energy Enthalpy — Ammonia Synthesis / Decomposition
# =========================================================================== #
def build_23_bond_energy_enthalpy_synthesis_ammonia_haber(rng: random.Random) -> Dict[str, Any]:
    forward = rng.choice([True, False])
    eb_fwd = 945 + 3 * 436  # 2253
    ef_fwd = 6 * 391        # 2346
    if forward:
        eq = "N₂(g) + 3H₂(g) → 2NH₃(g)"
        eb, ef = eb_fwd, ef_fwd
    else:
        eq = "2NH₃(g) → N₂(g) + 3H₂(g)"
        eb, ef = ef_fwd, eb_fwd
    dh = eb - ef
    kind = "exothermic" if dh < 0 else "endothermic"
    prompt = (
        f"For the industrial reaction:\n$${eq}$$\n"
        f"Calculate $\\Delta H$ using $E(\\text{{N≡N}}) = 945$, $E(\\text{{H–H}}) = 436$, and $E(\\text{{N–H}}) = 391\\text{{ kJ·mol}}^{{-1}}$, "
        f"and classify the reaction."
    )
    ans = f"ΔH = {'+' if dh > 0 else ''}{dh} kJ ({kind})"
    sample = (
        f"Bonds broken = {eb} kJ; Bonds formed = {ef} kJ.\n"
        f"$\\Delta H = {eb} - {ef} = {'+' if dh > 0 else ''}{dh}\\text{{ kJ}}$ (**{kind}**)."
    )
    return _pillars(
        qid=f"ps11_e23_{rng.randint(10000, 99999)}",
        subskill="23_bond_energy_enthalpy_synthesis_ammonia_haber",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Bonds broken = {eb} kJ", "marks": 1},
            {"id": "mp2", "desc": f"Bonds formed = {ef} kJ", "marks": 1},
            {"id": "mp3", "desc": f"ΔH = {'+' if dh > 0 else ''}{dh} kJ ({kind})", "marks": 2},
        ],
        hints={
            "1_nudge": "Each NH₃ molecule has 3 N–H bonds, so 2NH₃ has 6 N–H bonds in total.",
            "2_concept": "ΔH = ΣE(broken) - ΣE(formed).",
            "3_breakdown": sample,
        },
        misconception_tags=["counting_3_NH_bonds_instead_of_6"],
        marks=4,
        duration=5,
    )


# =========================================================================== #
# 24: Unknown Bond Energy from Given ΔH
# =========================================================================== #
def build_24_unknown_bond_energy_from_reaction_deltaH(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {"eq": "H₂(g) + I₂(g) → 2HI(g)", "known_br": "E(H–H)=436, E(I–I)=151", "eb": 436 + 151, "dh": -9, "n_x": 2, "x_name": "H–I"},
        {"eq": "H₂(g) + Cl₂(g) → 2HCl(g)", "known_br": "E(H–H)=436, E(Cl–Cl)=243", "eb": 436 + 243, "dh": -185, "n_x": 2, "x_name": "H–Cl"},
    ]
    c = rng.choice(cases)
    x_val = (c["eb"] - c["dh"]) // c["n_x"]
    prompt = (
        f"For the reaction $${c['eq']} \\quad \\Delta H = {c['dh']}\\text{{ kJ}}$$\n"
        f"Given {c['known_br']} kJ·mol⁻¹, calculate the average bond energy of the **{c['x_name']}** bond."
    )
    ans = f"{x_val} kJ/mol"
    sample = (
        f"$\\Delta H = \\sum E_{{\\text{{broken}}}} - \\sum E_{{\\text{{formed}}}}$\n"
        f"${c['dh']} = {c['eb']} - {c['n_x']} \\cdot E(\\text{{{c['x_name']}}})$\n"
        f"${c['n_x']} \\cdot E(\\text{{{c['x_name']}}}) = {c['eb']} - ({c['dh']}) = {c['eb'] - c['dh']}$\n"
        f"$E(\\text{{{c['x_name']}}}) = {x_val}\\text{{ kJ·mol}}^{{-1}}$."
    )
    return _pillars(
        qid=f"ps11_e24_{rng.randint(10000, 99999)}",
        subskill="24_unknown_bond_energy_from_reaction_deltaH",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Substitute into ΔH = ΣE(broken) - ΣE(formed)", "marks": 2},
            {"id": "mp2", "desc": f"Solve E({c['x_name']}) = {x_val} kJ/mol", "marks": 2},
        ],
        hints={
            "1_nudge": "Set up ΔH = E(broken) - 2·E(product bond) and solve algebraically.",
            "2_concept": "Pay close attention to negative signs: -(-ΔH) adds.",
            "3_breakdown": sample,
        },
        misconception_tags=["forgetting_factor_2_when_solving_for_product_bond"],
        marks=4,
        duration=5,
    )


# =========================================================================== #
# 25: Chemiluminescence & Thermite Energy Conversions
# =========================================================================== #
def build_25_chemiluminescence_and_thermite_energy_transfers(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {
            "name": "a diver's chemical lightstick",
            "eq": "Phenyl oxalate ester + H₂O₂ + dye → products + visible light",
            "form": "chemical potential energy converts primarily into **light (radiant) energy** (chemiluminescence) with minimal heat",
            "kind": "exothermic",
        },
        {
            "name": "the thermite welding reaction",
            "eq": "Fe₂O₃(s) + 2Al(s) → 2Fe(l) + Al₂O₃(s) + heat",
            "form": "chemical potential energy converts into intense **thermal (heat) and light energy**, melting the iron formed",
            "kind": "exothermic",
        },
    ]
    c = rng.choice(cases)
    prompt = (
        f"Consider the energy changes occurring in **{c['name']}**:\n$${c['eq']}$$\n\n"
        f"1. State whether this reaction is exothermic or endothermic.\n"
        f"2. Describe the primary energy transformation taking place."
    )
    ans = f"{c['kind'].capitalize()}; {c['form']}"
    sample = f"1. **{c['kind'].capitalize()}** ($\\Delta H < 0$).\n2. {c['form'].capitalize()}."
    return _pillars(
        qid=f"ps11_e25_{rng.randint(10000, 99999)}",
        subskill="25_chemiluminescence_and_thermite_energy_transfers",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Classify as exothermic", "marks": 1},
            {"id": "mp2", "desc": f"Energy transformation: {c['form']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Exothermic reactions can release energy as heat, light, or both.",
            "2_concept": "Lightsticks release energy as visible light (chemiluminescence).",
            "3_breakdown": sample,
        },
        misconception_tags=["assuming_exothermic_reactions_only_emit_heat_never_light"],
        marks=3,
        duration=3,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_chemical_system_and_enthalpy_definition": build_01_chemical_system_and_enthalpy_definition,
    "02_bond_breaking_endothermic_energy_absorbed": build_02_bond_breaking_endothermic_energy_absorbed,
    "03_bond_forming_exothermic_energy_released": build_03_bond_forming_exothermic_energy_released,
    "04_potential_energy_vs_internuclear_distance_bond": build_04_potential_energy_vs_internuclear_distance_bond,
    "05_exothermic_energy_balance_criteria": build_05_exothermic_energy_balance_criteria,
    "06_endothermic_energy_balance_criteria": build_06_endothermic_energy_balance_criteria,
    "07_thermochemical_equation_heat_term_right": build_07_thermochemical_equation_heat_term_right,
    "08_thermochemical_equation_heat_term_left": build_08_thermochemical_equation_heat_term_left,
    "09_thermochemical_equation_delta_H_notation": build_09_thermochemical_equation_delta_H_notation,
    "10_molar_enthalpy_stoichiometric_scaling": build_10_molar_enthalpy_stoichiometric_scaling,
    "11_reversing_reaction_enthalpy_sign_flip": build_11_reversing_reaction_enthalpy_sign_flip,
    "12_physical_phase_changes_endo_vs_exo": build_12_physical_phase_changes_endo_vs_exo,
    "13_photosynthesis_endothermic_solar_energy": build_13_photosynthesis_endothermic_solar_energy,
    "14_cellular_respiration_and_combustion_exothermic": build_14_cellular_respiration_and_combustion_exothermic,
    "15_thermal_decomposition_of_limestone_kiln": build_15_thermal_decomposition_of_limestone_kiln,
    "16_salt_dissolution_endothermic_cold_packs": build_16_salt_dissolution_endothermic_cold_packs,
    "17_salt_dissolution_neutralisation_exothermic": build_17_salt_dissolution_neutralisation_exothermic,
    "18_polystyrene_cup_calorimetry_experimental_design": build_18_polystyrene_cup_calorimetry_experimental_design,
    "19_calorimetry_heat_calculation_q_mc_deltaT": build_19_calorimetry_heat_calculation_q_mc_deltaT,
    "20_molar_enthalpy_from_calorimetry_data": build_20_molar_enthalpy_from_calorimetry_data,
    "21_bond_energy_enthalpy_combustion_hydrogen": build_21_bond_energy_enthalpy_combustion_hydrogen,
    "22_bond_energy_enthalpy_combustion_hydrocarbons": build_22_bond_energy_enthalpy_combustion_hydrocarbons,
    "23_bond_energy_enthalpy_synthesis_ammonia_haber": build_23_bond_energy_enthalpy_synthesis_ammonia_haber,
    "24_unknown_bond_energy_from_reaction_deltaH": build_24_unknown_bond_energy_from_reaction_deltaH,
    "25_chemiluminescence_and_thermite_energy_transfers": build_25_chemiluminescence_and_thermite_energy_transfers,
}
