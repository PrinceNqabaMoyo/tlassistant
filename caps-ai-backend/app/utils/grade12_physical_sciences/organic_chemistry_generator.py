"""Grade 12 Physical Sciences — Organic Chemistry Generator.
Deterministic 6-pillar CAPS question generator covering Paper 2 (Chemistry Term 1):
- Homologous series & functional groups: Alkanes, Alkenes, Alkynes, Haloalkanes, Alcohols,
  Aldehydes, Ketones, Carboxylic acids, Esters.
- IUPAC nomenclature & structural formulas.
- Structural isomers: Chain, Positional, Functional isomers.
- Physical properties (boiling point, vapour pressure, melting point) vs intermolecular forces.
- Organic reactions: Addition, Substitution, Elimination, Esterification.

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


IUPAC_COMPOUNDS = [
    {
        "name": "2-methylbutane",
        "formula": r"\text{CH}_3\text{CH}(\text{CH}_3)\text{CH}_2\text{CH}_3",
        "condensed": "CH3-CH(CH3)-CH2-CH3",
        "series": "Alkane",
        "functional_group": "Carbon-carbon single bonds (C-C)",
        "chain_length": 4,
        "substituents": "methyl on carbon-2",
        "intermolecular": "London forces (induced dipole forces)",
    },
    {
        "name": "butan-2-ol",
        "formula": r"\text{CH}_3\text{CH}_2\text{CH(OH)}\text{CH}_3",
        "condensed": "CH3-CH2-CH(OH)-CH3",
        "series": "Alcohol",
        "functional_group": "Hydroxyl group (-OH)",
        "chain_length": 4,
        "substituents": "hydroxyl on carbon-2",
        "intermolecular": "Hydrogen bonding (one site per molecule) and London forces",
    },
    {
        "name": "ethyl propanoate",
        "formula": r"\text{CH}_3\text{CH}_2\text{COO}\text{CH}_2\text{CH}_3",
        "condensed": "CH3-CH2-COO-CH2-CH3",
        "series": "Ester",
        "functional_group": "Ester group (-COO-)",
        "chain_length": 3,
        "alcohol_part": "ethanol",
        "acid_part": "propanoic acid",
        "intermolecular": "Dipole-dipole forces and London forces",
    },
    {
        "name": "2-bromopropane",
        "formula": r"\text{CH}_3\text{CH(Br)}\text{CH}_3",
        "condensed": "CH3-CH(Br)-CH3",
        "series": "Haloalkane",
        "functional_group": "Halogen atom (-Br bonded to sp3 C)",
        "chain_length": 3,
        "substituents": "bromo on carbon-2",
        "intermolecular": "Dipole-dipole forces and London forces",
    },
    {
        "name": "pentan-2-one",
        "formula": r"\text{CH}_3\text{COCH}_2\text{CH}_2\text{CH}_3",
        "condensed": "CH3-CO-CH2-CH2-CH3",
        "series": "Ketone",
        "functional_group": "Carbonyl group (C=O) on secondary carbon",
        "chain_length": 5,
        "substituents": "carbonyl on carbon-2",
        "intermolecular": "Dipole-dipole forces and London forces",
    },
    {
        "name": "butanoic acid",
        "formula": r"\text{CH}_3\text{CH}_2\text{CH}_2\text{COOH}",
        "condensed": "CH3-CH2-CH2-COOH",
        "series": "Carboxylic acid",
        "functional_group": "Carboxyl group (-COOH)",
        "chain_length": 4,
        "substituents": "terminal carboxyl group",
        "intermolecular": "Extensive hydrogen bonding (two hydrogen bonds per molecule / dimer formation) and London forces",
    },
    {
        "name": "pentanal",
        "formula": r"\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_2\text{CHO}",
        "condensed": "CH3-CH2-CH2-CH2-CHO",
        "series": "Aldehyde",
        "functional_group": "Carbonyl group (-CHO) on terminal carbon",
        "chain_length": 5,
        "substituents": "terminal carbonyl group",
        "intermolecular": "Dipole-dipole forces and London forces",
    },
]

ISOMER_PAIRS = [
    {
        "type": "Chain isomers",
        "compound_A": "Pentane (CH3-CH2-CH2-CH2-CH3)",
        "compound_B": "2-methylbutane (CH3-CH(CH3)-CH2-CH3)",
        "molecular_formula": "C5H12",
        "difference": "Different carbon skeleton arrangements (straight chain vs branched chain)",
    },
    {
        "type": "Positional isomers",
        "compound_A": "Butan-1-ol (CH3-CH2-CH2-CH2OH)",
        "compound_B": "Butan-2-ol (CH3-CH2-CH(OH)-CH3)",
        "molecular_formula": "C4H10O",
        "difference": "Different position of the hydroxyl (-OH) functional group on the parent carbon chain",
    },
    {
        "type": "Functional isomers",
        "compound_A": "Propanoic acid (CH3-CH2-COOH)",
        "compound_B": "Ethyl methanoate (HCOOCH2-CH3)",
        "molecular_formula": "C3H6O2",
        "difference": "Different functional groups (carboxylic acid vs ester) sharing the same molecular formula",
    },
    {
        "type": "Functional isomers",
        "compound_A": "Pentan-2-one (CH3-CO-CH2-CH2-CH3)",
        "compound_B": "Pentanal (CH3-CH2-CH2-CH2-CHO)",
        "molecular_formula": "C5H10O",
        "difference": "Different functional groups (ketone vs aldehyde) sharing the same molecular formula",
    },
]

ORGANIC_REACTIONS = [
    {
        "name": "Esterification (Condensation)",
        "reactants": "Ethanol and ethanoic acid",
        "catalyst": "Concentrated sulphuric acid (conc. H2SO4) and gentle heating",
        "product": "Ethyl ethanoate and water (H2O)",
        "equation": r"\text{CH}_3\text{COOH} + \text{CH}_3\text{CH}_2\text{OH} \xrightarrow{\text{conc. } \text{H}_2\text{SO}_4, \Delta} \text{CH}_3\text{COOCH}_2\text{CH}_3 + \text{H}_2\text{O}",
        "observation": "Sweet, fruity aroma formed",
    },
    {
        "name": "Halogenation (Addition)",
        "reactants": "Ethene and bromine (Br2)",
        "catalyst": "Room temperature (no catalyst required)",
        "product": "1,2-dibromoethane",
        "equation": r"\text{CH}_2=\text{CH}_2 + \text{Br}_2 \to \text{CH}_2\text{Br}-\text{CH}_2\text{Br}",
        "observation": "Rapid decolourisation of reddish-brown bromine water",
    },
    {
        "name": "Hydrolysis (Substitution)",
        "reactants": "2-bromobutane and dilute sodium hydroxide (NaOH(aq))",
        "catalyst": "Mild heating in aqueous solution",
        "product": "Butan-2-ol and sodium bromide (NaBr)",
        "equation": r"\text{CH}_3\text{CH(Br)}\text{CH}_2\text{CH}_3 + \text{NaOH(aq)} \xrightarrow{\Delta} \text{CH}_3\text{CH(OH)}\text{CH}_2\text{CH}_3 + \text{NaBr}",
        "observation": "Haloalkane converted to secondary alcohol",
    },
    {
        "name": "Dehydrohalogenation (Elimination)",
        "reactants": "2-bromobutane heated strongly with concentrated potassium hydroxide in ethanol (conc. KOH in ethanol)",
        "catalyst": "Reflux with concentrated strong base in ethanol",
        "product": "But-2-ene (major product by Zaitsev's rule) + HBr (or KBr + H2O)",
        "equation": r"\text{CH}_3\text{CH(Br)}\text{CH}_2\text{CH}_3 \xrightarrow[\Delta]{\text{conc. KOH / ethanol}} \text{CH}_3\text{CH}=\text{CH}\text{CH}_3 + \text{KBr} + \text{H}_2\text{O}",
        "observation": "Alkene formed from haloalkane (elimination of H and Br)",
    },
]


def _build_iupac_drill(r: random.Random) -> Dict[str, Any]:
    comp = r.choice(IUPAC_COMPOUNDS)

    prompt = (
        f"Consider the condensed organic structural formula:\n\n"
        f"$$\\mathbf{{{comp['formula']}}}$$\n\n"
        f"1. Identify the **homologous series** to which this compound belongs.\n"
        f"2. Write down the IUPAC name of the compound.\n"
        f"3. Name or draw the **functional group** of this homologous series."
    )

    sol = (
        f"1. Homologous series: **{comp['series']}**\n"
        f"2. IUPAC name: **{comp['name']}**\n"
        f"3. Functional group: **{comp['functional_group']}**"
    )

    return {
        "id": f"g12_ps_org_iupac_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": comp["name"],
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct homologous series ({comp['series']})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct parent chain length ({comp['chain_length']} carbons)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct substituent/suffix numbering ({comp['name']})", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"State functional group: {comp['functional_group']}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_hyphen_or_comma_iupac", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Find the longest continuous carbon chain containing the principal functional group.",
            "tier_2": "Number the carbon chain from the end closest to the functional group to assign the lowest possible locants.",
            "tier_3": f"Parent chain: {comp['chain_length']} carbons. Substituted group: {comp['substituents']}. IUPAC name: {comp['name']}.",
        },
        "misconception_tags": ["wrong_iupac_numbering_direction", "omitted_hyphen_or_comma_iupac"],
        "term": 1,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


def _build_isomers_drill(r: random.Random) -> Dict[str, Any]:
    pair = r.choice(ISOMER_PAIRS)

    prompt = (
        f"Compounds **A** and **B** have the same molecular formula $\\mathbf{{{pair['molecular_formula']}}}$:\n\n"
        f"- Compound A: {pair['compound_A']}\n"
        f"- Compound B: {pair['compound_B']}\n\n"
        f"1. Define the term *structural isomer*.\n"
        f"2. Identify the specific type of structural isomerism shown by compounds A and B.\n"
        f"3. Explain the structural difference between these two molecules."
    )

    sol = (
        f"1. **Structural isomer:** Organic molecules with the same molecular formula but different structural formulas.\n"
        f"2. Type of isomerism: **{pair['type']}**\n"
        f"3. Structural difference: **{pair['difference']}**"
    )

    return {
        "id": f"g12_ps_org_isomers_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": pair["type"],
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: Same molecular formula, different structural formula", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Identify isomer type: {pair['type']}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Explain difference: {pair['difference']}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Recall the three types of structural isomers: chain isomers, positional isomers, and functional isomers.",
            "tier_2": "Examine whether the carbon skeleton, the location of the functional group, or the functional group itself differs.",
            "tier_3": f"They are {pair['type']} because {pair['difference']}.",
        },
        "misconception_tags": ["confused_chain_and_positional_isomers"],
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 4,
    }


def _build_physical_properties_drill(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        {
            "A": ("Butan-1-ol", 117.7, "Hydrogen bonding (one -OH per molecule)"),
            "B": ("Butanoic acid", 163.5, "Stronger hydrogen bonding (forms dimers with two H-bonds per pair)"),
            "question": "Explain why butanoic acid has a significantly higher boiling point than butan-1-ol, despite similar molar masses.",
            "reasoning": (
                "1. Both molecules have similar molecular mass and surface area, so London forces are comparable.\n"
                "2. Butan-1-ol has one site for hydrogen bonding per molecule.\n"
                "3. Butanoic acid molecules form stable dimers through two hydrogen bonds between carboxyl groups.\n"
                "4. More energy is required to overcome the stronger intermolecular hydrogen bonds in butanoic acid, resulting in a higher boiling point."
            ),
        },
        {
            "A": ("Pentane", 36.1, "Straight chain alkane (larger surface area)"),
            "B": ("2,2-dimethylpropane", 9.5, "Highly branched spherical molecule (smaller surface area)"),
            "question": "Explain why pentane has a higher boiling point than 2,2-dimethylpropane (both are C5H12 isomers).",
            "reasoning": (
                "1. Both compounds have the same molecular formula (C5H12) and London forces.\n"
                "2. Pentane has an unbranched straight-chain structure with a larger molecular surface area.\n"
                "3. 2,2-dimethylpropane is more compact and spherical, reducing the contact surface area between molecules.\n"
                "4. Stronger/more extensive London forces exist between pentane molecules, requiring more thermal energy to overcome."
            ),
        },
    ]
    scen = r.choice(scenarios)

    prompt = (
        f"The boiling points of two organic compounds are given below:\n\n"
        f"- **Compound A:** {scen['A'][0]} (Boiling point: ${scen['A'][1]}^\\circ\\text{{C}}$)\n"
        f"- **Compound B:** {scen['B'][0]} (Boiling point: ${scen['B'][1]}^\\circ\\text{{C}}$)\n\n"
        f"{scen['question']}"
    )

    sol = scen["reasoning"]

    return {
        "id": f"g12_ps_org_phys_prop_{r.randint(10000, 99999)}",
        "type": "essay_reasoning",
        "prompt": prompt,
        "correct_answer": "Higher boiling point due to stronger intermolecular forces requiring more energy to overcome",
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Identify and compare the types of intermolecular forces present", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Compare molecular surface area or number of hydrogen bonding sites", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "State which substance has stronger overall intermolecular forces", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Relate stronger intermolecular forces to higher energy required to separate molecules", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "stated_breaking_covalent_bonds", "penalty": -2}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Boiling point involves overcoming INTERMOLECULAR forces between molecules, never breaking covalent bonds inside molecules.",
            "tier_2": "Structure your answer: 1. Identify IMF in both. 2. Compare strength/extent. 3. Conclude on energy required.",
            "tier_3": f"{scen['reasoning']}",
        },
        "misconception_tags": ["intermolecular_vs_intramolecular_confusion"],
        "term": 1,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
    }


def _build_reactions_drill(r: random.Random) -> Dict[str, Any]:
    rxn = r.choice(ORGANIC_REACTIONS)

    prompt = (
        f"Consider the organic transformation:\n\n"
        f"**Reactants:** {rxn['reactants']}\n\n"
        f"1. Identify the **type of organic reaction** taking place (Addition, Substitution, Elimination, or Esterification).\n"
        f"2. State the essential **reaction condition or catalyst** required for this reaction.\n"
        f"3. Write down the name of the major organic product formed.\n"
        f"4. Write a balanced chemical equation using structural or condensed formulas."
    )

    sol = (
        f"1. Reaction type: **{rxn['name']}**\n"
        f"2. Reaction condition: **{rxn['catalyst']}**\n"
        f"3. Major product: **{rxn['product']}**\n"
        f"4. Balanced equation:\n"
        f"$${rxn['equation']}$$"
    )

    return {
        "id": f"g12_ps_org_rxn_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": rxn["name"],
        "worked_solution": sol,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct reaction type ({rxn['name']})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Essential condition/catalyst ({rxn['catalyst']})", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Name major product ({rxn['product']})", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Balanced equation with correct formulas", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "omitted_catalyst", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Addition: unsaturated to saturated (adds across double bond). Substitution: atom replaced. Elimination: saturated to unsaturated (forms double bond).",
            "tier_2": f"Here, {rxn['reactants']} undergo {rxn['name']}.",
            "tier_3": f"Reaction: {rxn['name']}. Condition: {rxn['catalyst']}. Equation: {rxn['equation']}.",
        },
        "misconception_tags": ["omitted_catalyst_h2so4", "confused_addition_and_substitution"],
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    r = _rng(seed)

    if mode == "elementary_iupac":
        return _build_iupac_drill(r)
    elif mode == "elementary_isomers":
        return _build_isomers_drill(r)
    elif mode == "elementary_physical_properties":
        return _build_physical_properties_drill(r)
    elif mode == "elementary_reactions":
        return _build_reactions_drill(r)
    else:
        choice = r.choice(["iupac", "isomers", "phys_prop", "reactions"])
        if choice == "iupac":
            return _build_iupac_drill(r)
        elif choice == "isomers":
            return _build_isomers_drill(r)
        elif choice == "phys_prop":
            return _build_physical_properties_drill(r)
        else:
            return _build_reactions_drill(r)
