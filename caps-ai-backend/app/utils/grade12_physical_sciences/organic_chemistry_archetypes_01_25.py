"""Grade 12 Physical Sciences — Organic Chemistry Archetypes (Subskills 01–25).
Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 1/04. Organic molecules.md

Covers:
- Organic molecular definitions, carbon tetravalency, catenation, exceptions.
- Saturated vs unsaturated hydrocarbons, bromine water test.
- Homologous series, functional groups, general formulae.
- IUPAC naming & structural formulas: alkanes (straight & branched), alkenes, alkynes, haloalkanes (1°, 2°, 3°),
  alcohols (1°, 2°, 3°, diols/triols), aldehydes, ketones, carboxylic acids, esters.
- Structural isomerism: chain isomers, positional isomers, functional isomers (aldehydes/ketones, carboxylic acids/esters).

100% deterministic Python, zero LLM calls, strictly < 2000 lines.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    """Formats numbers with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _svg_spec(svg: str) -> Dict[str, Any]:
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


# ==============================================================================
# 01. Organic Molecular Definitions and Uniqueness of Carbon
# ==============================================================================
def builder_01(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_01_carbon_unique", seed, idx)
    test_compound = rng.choice(["carbon dioxide (CO₂)", "sodium carbonate (Na₂CO₃)", "calcium carbide (CaC₂)", "potassium cyanide (KCN)"])
    organic_example = rng.choice(["methane (CH₄)", "ethanol (C₂H₅OH)", "ethanoic acid (CH₃COOH)", "glucose (C₆H₁₂O₆)"])

    prompt = (
        f"Organic chemistry is the chemistry of carbon-containing molecules.\n\n"
        f"1. Define the term 'organic molecule' according to CAPS curriculum standards.\n"
        f"2. Define the term 'catenation' and explain why carbon can form millions of diverse compounds.\n"
        f"3. Explain why {test_compound} is classified as an inorganic compound even though it contains carbon, "
        f"whereas {organic_example} is classified as an organic molecule."
    )
    ans_str = (
        f"1. A molecule that contains carbon atoms (generally bonded to other carbon and hydrogen atoms); "
        f"2. Catenation is the ability of carbon atoms to form covalent bonds with each other to create long chains or rings; "
        f"3. {test_compound} lacks C-C or C-H covalent backbones and exhibits ionic/mineral properties, while {organic_example} has covalent C-C/C-H bonds."
    )
    memo = (
        "1. An organic molecule is a molecule containing carbon atoms, typically bonded to hydrogen, other carbon atoms, "
        "and heteroatoms like O, N, or halogens. (Carbon oxides, carbonates, carbides, and cyanides are excluded). [2]\n"
        "2. Catenation is the bonding of atoms of the same element into longer chains, rings, or complex networks. "
        "Carbon has 4 valence electrons (tetravalency) and can form strong single, double, or triple covalent bonds with other carbon atoms. [2]\n"
        f"3. {test_compound} is classified as inorganic because it behaves as a mineral salt or simple oxide without typical "
        f"organic carbon-hydrogen or carbon-carbon bonding networks, whereas {organic_example} possesses covalent C-C and/or C-H bonds. [2]"
    )
    hints = {
        "tier_1": "Recall the definition: organic molecules contain carbon bonded to other carbons and hydrogens.",
        "tier_2": "Catenation is chain-forming ability. Carbon has 4 valence electrons and forms 4 covalent bonds.",
        "tier_3": f"1. Organic definition. 2. Catenation = chain formation via tetravalency. 3. {test_compound} is an exception.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="180" height="140" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="110" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">Organic Example</text>'
        f'<text x="110" y="80" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">{organic_example}</text>'
        f'<text x="110" y="115" text-anchor="middle" font-size="11" fill="#475569">Covalent C-C / C-H</text>'
        f'<rect x="240" y="20" width="180" height="140" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="330" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#b91c1c">Inorganic Exception</text>'
        f'<text x="330" y="80" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">{test_compound}</text>'
        f'<text x="330" y="115" text-anchor="middle" font-size="11" fill="#475569">Mineral / Oxide / Salt</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "01_organic_molecular_definitions_and_uniqueness_of_carbon",
        "subskill": "01_organic_molecular_definitions_and_uniqueness_of_carbon",
        "subskill_id": "01_organic_molecular_definitions_and_uniqueness_of_carbon",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["all_carbon_compounds_are_organic", "confusing_catenation_with_hybridization"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of organic molecule", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Definition of catenation and tetravalency", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Distinction between organic and inorganic exception", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 02. Hydrocarbons — Saturated vs Unsaturated & Bromine Water Test
# ==============================================================================
def builder_02(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_02_sat_unsat", seed, idx)
    sat_compound = rng.choice(["hexane", "butane", "pentane", "heptane"])
    unsat_compound = rng.choice(["hex-1-ene", "but-2-ene", "pent-1-ene", "propene"])

    prompt = (
        f"Consider the two hydrocarbons {sat_compound} and {unsat_compound}.\n\n"
        f"1. Define the term 'hydrocarbon'.\n"
        f"2. Distinguish between a 'saturated hydrocarbon' and an 'unsaturated hydrocarbon' in terms of bond types.\n"
        f"3. Describe a simple laboratory chemical test using bromine water (Br₂(aq)) to distinguish between "
        f"{sat_compound} and {unsat_compound} in the dark, including the expected colour change for each."
    )
    ans_str = (
        f"1. A compound containing only carbon and hydrogen atoms; "
        f"2. Saturated has only single C-C bonds; unsaturated has one or more multiple (double/triple) C-C bonds; "
        f"3. In the dark, {unsat_compound} rapidly decolourises bromine water from brown/orange to colourless, while {sat_compound} causes no immediate colour change."
    )
    memo = (
        "1. A hydrocarbon is an organic compound that consists entirely of carbon and hydrogen atoms only. [1]\n"
        "2. A saturated hydrocarbon contains only single covalent bonds between adjacent carbon atoms (maximum hydrogens). [1]\n"
        "   An unsaturated hydrocarbon contains one or more double (C=C) or triple (C≡C) carbon-carbon bonds. [1]\n"
        f"3. Bromine water test (in the dark):\n"
        f"   - Add bromine water (orange-brown) to each sample without UV light. [1]\n"
        f"   - Unsaturated ({unsat_compound}) undergoes rapid addition reaction: orange-brown colour decolourises immediately to colourless. [1]\n"
        f"   - Saturated ({sat_compound}) cannot undergo addition: orange-brown colour remains unchanged in the dark. [1]"
    )
    hints = {
        "tier_1": "Saturated = single bonds only. Unsaturated = double or triple bonds.",
        "tier_2": "Bromine water is orange-brown. Alkenes decolourise it rapidly via addition.",
        "tier_3": f"Unsaturated ({unsat_compound}) decolourises Br2(aq) rapidly; saturated ({sat_compound}) stays brown in dark.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="170" height="130" rx="6" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="115" y="50" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">Saturated: {sat_compound}</text>'
        f'<text x="115" y="85" text-anchor="middle" font-size="11" fill="#0f172a">Single C-C bonds</text>'
        f'<text x="115" y="125" text-anchor="middle" font-size="11" font-weight="bold" fill="#ca8a04">Br₂(aq): Stays Orange</text>'
        f'<rect x="240" y="25" width="170" height="130" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
        f'<text x="325" y="50" text-anchor="middle" font-size="12" font-weight="bold" fill="#0369a1">Unsaturated: {unsat_compound}</text>'
        f'<text x="325" y="85" text-anchor="middle" font-size="11" fill="#0f172a">Double C=C bond</text>'
        f'<text x="325" y="125" text-anchor="middle" font-size="11" font-weight="bold" fill="#0284c7">Br₂(aq): Decolourises</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "02_hydrocarbons_saturated_vs_unsaturated",
        "subskill": "02_hydrocarbons_saturated_vs_unsaturated",
        "subskill_id": "02_hydrocarbons_saturated_vs_unsaturated",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["confusing_saturated_with_polar", "bromine_water_colour_inversion"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of hydrocarbon", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Saturated vs unsaturated bond distinction", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Bromine water test description and colour changes", "marks": 3, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 03. Homologous Series — Characteristics and General Formulae
# ==============================================================================
def builder_03(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_03_homologous", seed, idx)
    series_info = [
        {"name": "Alkanes", "gen": "CnH2n+2", "group": "Carbon-carbon single bonds (C-C)", "n": rng.choice([4, 5, 6, 7])},
        {"name": "Alkenes", "gen": "CnH2n", "group": "Carbon-carbon double bond (C=C)", "n": rng.choice([3, 4, 5, 6])},
        {"name": "Alkynes", "gen": "CnH2n-2", "group": "Carbon-carbon triple bond (C≡C)", "n": rng.choice([3, 4, 5])},
        {"name": "Alcohols", "gen": "CnH2n+1OH", "group": "Hydroxyl group (-OH)", "n": rng.choice([2, 3, 4, 5])},
        {"name": "Carboxylic acids", "gen": "CnH2nO2", "group": "Carboxyl group (-COOH)", "n": rng.choice([2, 3, 4])},
        {"name": "Ketones", "gen": "CnH2nO", "group": "Carbonyl group (C=O) on non-terminal carbon", "n": rng.choice([3, 4, 5])},
    ]
    chosen = rng.choice(series_info)
    n = chosen["n"]

    if chosen["name"] == "Alkanes":
        h_count = 2 * n + 2
        mol_form = f"C{n}H{h_count}"
    elif chosen["name"] == "Alkenes":
        h_count = 2 * n
        mol_form = f"C{n}H{h_count}"
    elif chosen["name"] == "Alkynes":
        h_count = 2 * n - 2
        mol_form = f"C{n}H{h_count}"
    elif chosen["name"] == "Alcohols":
        mol_form = f"C{n}H{2*n+1}OH"
    elif chosen["name"] == "Carboxylic acids":
        mol_form = f"C{n}H{2*n}O2"
    else:
        mol_form = f"C{n}H{2*n}O"

    prompt = (
        f"Consider the homologous series of {chosen['name']}.\n\n"
        f"1. Define the term 'homologous series'.\n"
        f"2. Define the term 'functional group'.\n"
        f"3. State the general formula for {chosen['name']}.\n"
        f"4. Determine the molecular formula for a member of this series containing {n} carbon atoms."
    )
    ans_str = (
        f"1. A series of organic compounds that can be described by the same general formula and where each member "
        f"differs from the next by a -CH2- unit; 2. An atom or group of atoms that forms the centre of chemical activity "
        f"in the molecule; 3. {chosen['gen']}; 4. {mol_form}"
    )
    memo = (
        "1. A homologous series is a series of organic compounds that can be described by the same general formula "
        "and where each member differs from the next by a -CH₂- unit (or have the same functional group). [2]\n"
        "2. A functional group is an atom or group of atoms that forms the centre of chemical activity in the molecule. [1]\n"
        f"3. General formula for {chosen['name']}: {chosen['gen']} [1]\n"
        f"4. For n = {n}: molecular formula is {mol_form}. [1]"
    )
    hints = {
        "tier_1": "A homologous series shares the same general formula and functional group.",
        "tier_2": f"General formula of {chosen['name']} is {chosen['gen']}.",
        "tier_3": f"Substitute n={n} into {chosen['gen']} to get {mol_form}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#312e81">{chosen["name"]}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="12" fill="#1e1b4b">General Formula: {chosen["gen"]}</text>'
        f'<text x="220" y="115" text-anchor="middle" font-size="12" fill="#1e1b4b">Functional Group: {chosen["group"]}</text>'
        f'<text x="220" y="142" text-anchor="middle" font-size="12" font-weight="bold" fill="#4338ca">n = {n} → {mol_form}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "03_homologous_series_characteristics_and_general_formulae",
        "subskill": "03_homologous_series_characteristics_and_general_formulae",
        "subskill_id": "03_homologous_series_characteristics_and_general_formulae",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_homologous_series_with_isomers", "general_formula_hydrogen_calculation_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of homologous series", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Definition of functional group", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "General formula state", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Calculated molecular formula", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 04. Alkanes — Straight Chain IUPAC Naming (C1 to C8)
# ==============================================================================
def builder_04(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_04_alkane_straight", seed, idx)
    alkanes = [
        {"name": "propane", "c": 3, "condensed": "CH3-CH2-CH3", "mol": "C3H8"},
        {"name": "butane", "c": 4, "condensed": "CH3-CH2-CH2-CH3", "mol": "C4H10"},
        {"name": "pentane", "c": 5, "condensed": "CH3-(CH2)3-CH3", "mol": "C5H12"},
        {"name": "hexane", "c": 6, "condensed": "CH3-(CH2)4-CH3", "mol": "C6H14"},
        {"name": "heptane", "c": 7, "condensed": "CH3-(CH2)5-CH3", "mol": "C7H16"},
        {"name": "octane", "c": 8, "condensed": "CH3-(CH2)6-CH3", "mol": "C8H18"},
    ]
    chosen = rng.choice(alkanes)

    prompt = (
        f"Consider an unbranched alkane containing {chosen['c']} carbon atoms.\n\n"
        f"1. Write down the IUPAC name of this straight-chain alkane.\n"
        f"2. Write down its molecular formula.\n"
        f"3. Write down its condensed structural formula.\n"
        f"4. State whether this hydrocarbon is saturated or unsaturated, giving a reason."
    )
    ans_str = (
        f"1. {chosen['name']}; 2. {chosen['mol']}; 3. {chosen['condensed']}; "
        f"4. Saturated, because it contains only single carbon-carbon bonds."
    )
    memo = (
        f"1. IUPAC name for a {chosen['c']}-carbon straight alkane: {chosen['name']} [1]\n"
        f"2. Molecular formula: CnH2n+2 = C{chosen['c']}H{2*chosen['c']+2} = {chosen['mol']} [1]\n"
        f"3. Condensed structural formula: {chosen['condensed']} [1]\n"
        "4. Saturated [1], because there are only single C-C covalent bonds throughout the molecule. [1]"
    )
    hints = {
        "tier_1": f"Root for {chosen['c']} carbons: meth-, eth-, prop-, but-, pent-, hex-, hept-, oct-.",
        "tier_2": f"General formula CnH2n+2 gives {chosen['mol']}.",
        "tier_3": f"Name = {chosen['name']}. Saturated because only single C-C bonds.",
    }
    svg = (
        f'<svg viewBox="0 0 440 160" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="40" y="25" width="360" height="110" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">{chosen["name"].upper()}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" fill="#334155">{chosen["condensed"]}</text>'
        f'<text x="220" y="115" text-anchor="middle" font-size="12" fill="#64748b">Molecular formula: {chosen["mol"]} (Saturated)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 6,
        "mode": "04_alkanes_straight_chain_iupac_naming_c1_c8",
        "subskill": "04_alkanes_straight_chain_iupac_naming_c1_c8",
        "subskill_id": "04_alkanes_straight_chain_iupac_naming_c1_c8",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["carbon_prefix_confusion", "hydrogen_count_arithmetic_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "IUPAC name", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Molecular formula", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Condensed structural formula", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Saturation status with reason", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 05. Alkanes — Branched Chain IUPAC Naming
# ==============================================================================
def builder_05(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_05_alkane_branched", seed, idx)
    branched = [
        {"name": "2-methylbutane", "condensed": "CH3-CH(CH3)-CH2-CH3", "longest": 4, "branch": "methyl on carbon-2", "mol": "C5H12"},
        {"name": "2,2-dimethylpropane", "condensed": "C(CH3)4", "longest": 3, "branch": "two methyls on carbon-2", "mol": "C5H12"},
        {"name": "2-methylpentane", "condensed": "CH3-CH(CH3)-CH2-CH2-CH3", "longest": 5, "branch": "methyl on carbon-2", "mol": "C6H14"},
        {"name": "3-methylhexane", "condensed": "CH3-CH2-CH(CH3)-CH2-CH2-CH3", "longest": 6, "branch": "methyl on carbon-3", "mol": "C7H16"},
        {"name": "2,3-dimethylbutane", "condensed": "CH3-CH(CH3)-CH(CH3)-CH3", "longest": 4, "branch": "methyls on carbons 2 and 3", "mol": "C6H14"},
        {"name": "2,2-dimethylbutane", "condensed": "CH3-C(CH3)2-CH2-CH3", "longest": 4, "branch": "two methyls on carbon-2", "mol": "C6H14"},
    ]
    chosen = rng.choice(branched)

    prompt = (
        f"Consider a branched alkane with condensed structural formula {chosen['condensed']}.\n\n"
        f"1. Identify the number of carbon atoms in the longest continuous carbon chain.\n"
        f"2. Write down the correct IUPAC name for this branched alkane.\n"
        f"3. Write down its molecular formula.\n"
        f"4. State the homologous series to which this compound belongs."
    )
    ans_str = (
        f"1. {chosen['longest']}; 2. {chosen['name']}; 3. {chosen['mol']}; 4. Alkanes"
    )
    memo = (
        f"1. Longest continuous carbon chain has {chosen['longest']} carbon atoms. [1]\n"
        f"2. Number the chain from the end that gives substituents the lowest possible locants: "
        f"{chosen['branch']}. IUPAC name: {chosen['name']}. [2]\n"
        f"3. Molecular formula: {chosen['mol']} [1]\n"
        "4. Homologous series: Alkanes [1]"
    )
    hints = {
        "tier_1": "Find the longest continuous carbon chain first. Number from the end giving lowest branch numbers.",
        "tier_2": f"Longest chain = {chosen['longest']} carbons. Substituent: {chosen['branch']}.",
        "tier_3": f"Name = {chosen['name']}. Molecular formula = {chosen['mol']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#78350f">Condensed: {chosen["condensed"]}</text>'
        f'<text x="220" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#b45309">{chosen["name"]}</text>'
        f'<text x="220" y="125" text-anchor="middle" font-size="12" fill="#92400e">Longest chain: {chosen["longest"]} carbons | {chosen["branch"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "05_alkanes_branched_chain_iupac_naming",
        "subskill": "05_alkanes_branched_chain_iupac_naming",
        "subskill_id": "05_alkanes_branched_chain_iupac_naming",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["numbering_from_wrong_end", "failing_to_find_longest_chain"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Longest carbon chain length", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name (correct stem + locants + hyphenation)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Molecular formula", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Homologous series", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 06. Alkanes — Drawing Structural Formulae from Names
# ==============================================================================
def builder_06(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_06_draw_alkane", seed, idx)
    candidates = [
        {"name": "2-methylpropane", "mol": "C4H10", "c_chain": 3, "condensed": "CH(CH3)3"},
        {"name": "2,2-dimethylbutane", "mol": "C6H14", "c_chain": 4, "condensed": "CH3C(CH3)2CH2CH3"},
        {"name": "3-ethylpentane", "mol": "C7H16", "c_chain": 5, "condensed": "CH3CH2CH(CH2CH3)CH2CH3"},
        {"name": "2,3-dimethylpentane", "mol": "C7H16", "c_chain": 5, "condensed": "CH3CH(CH3)CH(CH3)CH2CH3"},
    ]
    chosen = rng.choice(candidates)

    prompt = (
        f"A chemist synthesises the branched alkane {chosen['name']}.\n\n"
        f"1. Define the term 'structural formula'.\n"
        f"2. Write down the molecular formula for {chosen['name']}.\n"
        f"3. Explain the step-by-step rules to draw the complete structural formula of {chosen['name']}.\n"
        f"4. State the total number of single covalent bonds present in one molecule of {chosen['name']}."
    )
    # Total single bonds in alkane CnH2n+2 = (n - 1) C-C bonds + (2n + 2) C-H bonds = 3n + 1 bonds
    # Parse n from mol
    n_c = int(chosen["mol"].split("H")[0].replace("C", ""))
    total_bonds = 3 * n_c + 1

    ans_str = (
        f"1. A structural formula shows which atoms are attached to which within the molecule with all bonds represented; "
        f"2. {chosen['mol']}; 3. Draw a chain of {chosen['c_chain']} carbons, attach substituents as indicated by locants, "
        f"fill all remaining carbon valencies with H atoms; 4. {total_bonds} single covalent bonds"
    )
    memo = (
        "1. A structural formula is a graphic representation that shows which atoms are bonded to each other within "
        "the molecule, with every covalent bond explicitly represented by a line. [1]\n"
        f"2. Molecular formula: {chosen['mol']} [1]\n"
        f"3. Step-by-step procedure: (i) Draw a continuous horizontal chain of {chosen['c_chain']} carbon atoms, "
        "(ii) Number the carbons 1 to N, (iii) Attach alkyl branches at the specified locant positions, "
        "(iv) Complete 4 bonds around every carbon atom by drawing C-H bonds. [2]\n"
        f"4. Total single bonds = (C-C bonds) + (C-H bonds) = ({n_c} - 1) + (2·{n_c} + 2) = {total_bonds} bonds. [1]"
    )
    hints = {
        "tier_1": "In an alkane, every carbon atom forms exactly 4 single covalent bonds.",
        "tier_2": f"Longest chain has {chosen['c_chain']} carbons. Total bonds = 3n + 1 = {total_bonds}.",
        "tier_3": f"Molecular formula = {chosen['mol']}. Total bonds = {total_bonds}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#14532d">{chosen["name"]}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" fill="#166534">Formula: {chosen["mol"]}</text>'
        f'<text x="220" y="115" text-anchor="middle" font-size="12" fill="#15803d">Main chain: {chosen["c_chain"]} carbons | Total bonds: {total_bonds}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "06_alkanes_drawing_structural_formulae",
        "subskill": "06_alkanes_drawing_structural_formulae",
        "subskill_id": "06_alkanes_drawing_structural_formulae",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["omitting_c_h_bonds_in_structural_formula", "pentavalent_carbon_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Structural formula definition", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Molecular formula", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Drawing rules description", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Total single bonds count", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 07. Alkenes — Straight Chain IUPAC Naming & Double Bond Position
# ==============================================================================
def builder_07(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_07_alkene_straight", seed, idx)
    alkenes = [
        {"name": "but-1-ene", "c": 4, "pos": 1, "condensed": "CH2=CH-CH2-CH3", "mol": "C4H8"},
        {"name": "but-2-ene", "c": 4, "pos": 2, "condensed": "CH3-CH=CH-CH3", "mol": "C4H8"},
        {"name": "pent-1-ene", "c": 5, "pos": 1, "condensed": "CH2=CH-CH2-CH2-CH3", "mol": "C5H10"},
        {"name": "pent-2-ene", "c": 5, "pos": 2, "condensed": "CH3-CH=CH-CH2-CH3", "mol": "C5H10"},
        {"name": "hex-1-ene", "c": 6, "pos": 1, "condensed": "CH2=CH-(CH2)3-CH3", "mol": "C6H12"},
        {"name": "hex-2-ene", "c": 6, "pos": 2, "condensed": "CH3-CH=CH-(CH2)2-CH3", "mol": "C6H12"},
        {"name": "hex-3-ene", "c": 6, "pos": 3, "condensed": "CH3-CH2-CH=CH-CH2-CH3", "mol": "C6H12"},
    ]
    chosen = rng.choice(alkenes)

    prompt = (
        f"Consider an unsaturated straight-chain hydrocarbon with condensed structural formula {chosen['condensed']}.\n\n"
        f"1. Write down the IUPAC name for this alkene.\n"
        f"2. Identify the functional group of this molecule.\n"
        f"3. State the general formula for straight-chain alkenes.\n"
        f"4. Explain why numbering starts from the end nearest the double bond rather than the opposite end."
    )
    ans_str = (
        f"1. {chosen['name']}; 2. Carbon-carbon double bond (C=C); 3. CnH2n; "
        f"4. IUPAC rules assign the lowest possible locant number to the functional group (C=C bond)."
    )
    memo = (
        f"1. IUPAC name: {chosen['name']} [2]\n"
        "2. Functional group: Carbon-carbon double covalent bond (C=C). [1]\n"
        "3. General formula: CnH2n [1]\n"
        "4. According to IUPAC nomenclature rules, the main chain must be numbered from the end that gives "
        "the principal functional group (the double bond) the lowest possible position number (locant). [1]"
    )
    hints = {
        "tier_1": "Alkenes end in -ene, with a number showing where the double bond begins.",
        "tier_2": f"Longest chain = {chosen['c']} carbons. Double bond starts at carbon {chosen['pos']}.",
        "tier_3": f"Name = {chosen['name']}. Functional group = C=C.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#0369a1">{chosen["name"].upper()}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{chosen["condensed"]}</text>'
        f'<text x="220" y="115" text-anchor="middle" font-size="12" fill="#0284c7">Double bond at C{chosen["pos"]} | Formula: {chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "07_alkenes_straight_chain_iupac_naming_position_of_double_bond",
        "subskill": "07_alkenes_straight_chain_iupac_naming_position_of_double_bond",
        "subskill_id": "07_alkenes_straight_chain_iupac_naming_position_of_double_bond",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["numbering_from_end_away_from_double_bond", "alkene_general_formula_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "IUPAC name (correct stem and double bond locant)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Functional group identification", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "General formula CnH2n", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Justification for numbering priority", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 08. Alkenes — Branched Chain IUPAC Naming (Functional Group Priority)
# ==============================================================================
def builder_08(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_08_alkene_branched", seed, idx)
    compounds = [
        {"name": "2-methylbut-1-ene", "condensed": "CH2=C(CH3)-CH2-CH3", "stem": "but-1-ene", "branch": "2-methyl", "mol": "C5H10"},
        {"name": "2-methylbut-2-ene", "condensed": "CH3-C(CH3)=CH-CH3", "stem": "but-2-ene", "branch": "2-methyl", "mol": "C5H10"},
        {"name": "3-methylbut-1-ene", "condensed": "CH2=CH-CH(CH3)-CH3", "stem": "but-1-ene", "branch": "3-methyl", "mol": "C5H10"},
        {"name": "2,3-dimethylbut-2-ene", "condensed": "CH3-C(CH3)=C(CH3)-CH3", "stem": "but-2-ene", "branch": "2,3-dimethyl", "mol": "C6H12"},
        {"name": "4-methylpent-2-ene", "condensed": "CH3-CH=CH-CH(CH3)-CH3", "stem": "pent-2-ene", "branch": "4-methyl", "mol": "C6H12"},
    ]
    chosen = rng.choice(compounds)

    prompt = (
        f"Consider the branched unsaturated compound with condensed formula {chosen['condensed']}.\n\n"
        f"1. State which feature takes priority when numbering the main carbon chain: the double bond or the alkyl substituent.\n"
        f"2. Write down the IUPAC name for this branched alkene.\n"
        f"3. Write down its molecular formula.\n"
        f"4. State the number of hydrogen atoms in one molecule of this compound."
    )
    ans_str = (
        f"1. The double bond (functional group) takes priority over alkyl substituents; "
        f"2. {chosen['name']}; 3. {chosen['mol']}; 4. {chosen['mol'].split('H')[1]} hydrogen atoms"
    )
    memo = (
        "1. The carbon-carbon double bond (functional group) takes priority over alkyl branches when numbering the chain. [1]\n"
        f"2. Parent chain containing the double bond: {chosen['stem']}. Substituent: {chosen['branch']}.\n"
        f"   IUPAC name: {chosen['name']} [2]\n"
        f"3. Molecular formula: {chosen['mol']} [1]\n"
        f"4. Number of hydrogen atoms = {chosen['mol'].split('H')[1]}. [1]"
    )
    hints = {
        "tier_1": "Double bond takes numbering priority over methyl branches every time.",
        "tier_2": f"Parent chain is {chosen['stem']} with {chosen['branch']}.",
        "tier_3": f"Name = {chosen['name']}. Molecular formula = {chosen['mol']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#ecfeff" stroke="#0891b2" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#155e75">{chosen["condensed"]}</text>'
        f'<text x="220" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#0e7490">{chosen["name"]}</text>'
        f'<text x="220" y="125" text-anchor="middle" font-size="12" fill="#164e63">Double bond priority over alkyl branch | {chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "08_alkenes_branched_chain_iupac_naming",
        "subskill": "08_alkenes_branched_chain_iupac_naming",
        "subskill_id": "08_alkenes_branched_chain_iupac_naming",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["alkyl_group_given_priority_over_double_bond", "incorrect_stem_selection_alkene"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Double bond priority statement", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Molecular formula", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Hydrogen count", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 09. Alkynes — IUPAC Naming and Triple Bond Structures
# ==============================================================================
def builder_09(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_09_alkynes", seed, idx)
    alkynes = [
        {"name": "ethyne", "condensed": "CH≡CH", "mol": "C2H2", "common": "acetylene", "pos": 1, "c": 2},
        {"name": "propyne", "condensed": "CH≡C-CH3", "mol": "C3H4", "common": "methylacetylene", "pos": 1, "c": 3},
        {"name": "but-1-yne", "condensed": "CH≡C-CH2-CH3", "mol": "C4H6", "common": "ethylacetylene", "pos": 1, "c": 4},
        {"name": "but-2-yne", "condensed": "CH3-C≡C-CH3", "mol": "C4H6", "common": "dimethylacetylene", "pos": 2, "c": 4},
        {"name": "pent-1-yne", "condensed": "CH≡C-CH2-CH2-CH3", "mol": "C5H8", "common": "propylacetylene", "pos": 1, "c": 5},
        {"name": "pent-2-yne", "condensed": "CH3-C≡C-CH2-CH3", "mol": "C5H8", "common": "ethylmethylacetylene", "pos": 2, "c": 5},
    ]
    chosen = rng.choice(alkynes)

    prompt = (
        f"Consider an alkyne with condensed formula {chosen['condensed']}.\n\n"
        f"1. Write down the IUPAC name for this alkyne.\n"
        f"2. Identify the functional group characterizing the alkyne homologous series.\n"
        f"3. State the general formula for alkynes.\n"
        f"4. State the bond angle around the carbon atoms involved in the triple bond and name their geometry."
    )
    ans_str = (
        f"1. {chosen['name']}; 2. Carbon-carbon triple bond (C≡C); 3. CnH2n-2; "
        f"4. 180°, linear geometry"
    )
    memo = (
        f"1. IUPAC name: {chosen['name']} [1]\n"
        "2. Functional group: Carbon-carbon triple bond (C≡C). [1]\n"
        "3. General formula: CnH2n-2 [1]\n"
        "4. Bond angle: 180° [1]; Geometry: Linear (sp hybridised). [1]"
    )
    hints = {
        "tier_1": "Alkynes contain a triple bond C≡C and end in -yne.",
        "tier_2": "General formula is CnH2n-2. Triple-bonded carbons are linear with 180° bond angles.",
        "tier_3": f"Name = {chosen['name']}. Functional group = C≡C. Bond angle = 180°.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#fdf4ff" stroke="#c026d3" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#86198f">{chosen["name"].upper()}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">{chosen["condensed"]}</text>'
        f'<text x="220" y="115" text-anchor="middle" font-size="12" fill="#701a75">Formula: {chosen["mol"]} | Triple bond (C≡C) | Linear 180°</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "09_alkynes_iupac_naming_and_structures",
        "subskill": "09_alkynes_iupac_naming_and_structures",
        "subskill_id": "09_alkynes_iupac_naming_and_structures",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["alkyne_general_formula_confusion", "triple_bond_geometry_misconception"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "IUPAC name", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Functional group identification", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "General formula CnH2n-2", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Bond angle 180 degrees", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Linear geometry", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 10. Haloalkanes — IUPAC Naming and Halogen Substituents
# ==============================================================================
def builder_10(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_10_haloalkanes_iupac", seed, idx)
    haloalkanes = [
        {"name": "2-chlorobutane", "condensed": "CH3-CH(Cl)-CH2-CH3", "halogen": "chloro", "pos": 2, "mol": "C4H9Cl"},
        {"name": "1-bromopropane", "condensed": "CH2(Br)-CH2-CH3", "halogen": "bromo", "pos": 1, "mol": "C3H7Br"},
        {"name": "2-bromopropane", "condensed": "CH3-CH(Br)-CH3", "halogen": "bromo", "pos": 2, "mol": "C3H7Br"},
        {"name": "2-chloro-2-methylpropane", "condensed": "(CH3)3C-Cl", "halogen": "chloro", "pos": 2, "mol": "C4H9Cl"},
        {"name": "2-iodo-3-methylbutane", "condensed": "CH3-CH(I)-CH(CH3)-CH3", "halogen": "iodo", "pos": 2, "mol": "C5H11I"},
        {"name": "1,2-dichloroethane", "condensed": "CH2(Cl)-CH2(Cl)", "halogen": "dichloro", "pos": "1,2", "mol": "C2H4Cl2"},
    ]
    chosen = rng.choice(haloalkanes)

    prompt = (
        f"Consider the halogenated organic compound with condensed formula {chosen['condensed']}.\n\n"
        f"1. Name the homologous series to which this compound belongs.\n"
        f"2. Write down the IUPAC name for this compound.\n"
        f"3. Write down its molecular formula.\n"
        f"4. State the prefix used in IUPAC nomenclature for the halogen substituent present."
    )
    ans_str = (
        f"1. Haloalkanes (alkyl halides); 2. {chosen['name']}; 3. {chosen['mol']}; 4. {chosen['halogen']}"
    )
    memo = (
        "1. Homologous series: Haloalkanes (or alkyl halides). [1]\n"
        f"2. IUPAC name: {chosen['name']} [2]\n"
        f"3. Molecular formula: {chosen['mol']} [1]\n"
        f"4. Halogen prefix: {chosen['halogen']} [1]"
    )
    hints = {
        "tier_1": "Haloalkanes treat halogens (bromo-, chloro-, fluoro-, iodo-) as prefixes on the alkane chain.",
        "tier_2": f"Number from the end giving lowest substituent number: {chosen['name']}.",
        "tier_3": f"Series = Haloalkanes. Name = {chosen['name']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#f0fdfa" stroke="#0d9488" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#134e4a">{chosen["condensed"]}</text>'
        f'<text x="220" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f766e">{chosen["name"]}</text>'
        f'<text x="220" y="125" text-anchor="middle" font-size="12" fill="#115e59">Series: Haloalkanes | Formula: {chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "10_haloalkanes_iupac_naming_and_halogen_substituents",
        "subskill": "10_haloalkanes_iupac_naming_and_halogen_substituents",
        "subskill_id": "10_haloalkanes_iupac_naming_and_halogen_substituents",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["haloalkane_suffix_fallacy", "alphabetical_ordering_omission_halogens"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Homologous series identification", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Molecular formula", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Halogen prefix", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 11. Haloalkanes — Classification into Primary, Secondary, Tertiary
# ==============================================================================
def builder_11(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_11_haloalkane_class", seed, idx)
    examples = [
        {"name": "1-chlorobutane", "class": "primary (1°)", "bonded_c": 1, "formula": "CH3-CH2-CH2-CH2-Cl"},
        {"name": "2-bromobutane", "class": "secondary (2°)", "bonded_c": 2, "formula": "CH3-CH(Br)-CH2-CH3"},
        {"name": "2-chloro-2-methylpropane", "class": "tertiary (3°)", "bonded_c": 3, "formula": "(CH3)3C-Cl"},
        {"name": "1-bromopropane", "class": "primary (1°)", "bonded_c": 1, "formula": "CH3-CH2-CH2-Br"},
        {"name": "2-chloropropane", "class": "secondary (2°)", "bonded_c": 2, "formula": "CH3-CH(Cl)-CH3"},
        {"name": "2-bromo-2-methylbutane", "class": "tertiary (3°)", "bonded_c": 3, "formula": "CH3-C(CH3)(Br)-CH2-CH3"},
    ]
    chosen = rng.choice(examples)

    prompt = (
        f"Consider the haloalkane {chosen['name']} ({chosen['formula']}).\n\n"
        f"1. Classify this haloalkane as primary (1°), secondary (2°), or tertiary (3°).\n"
        f"2. Give a precise reason for your classification based on the carbon atom bonded to the halogen.\n"
        f"3. Write down the IUPAC name of a structural isomer of {chosen['name']} that belongs to a DIFFERENT classification category (primary, secondary, or tertiary)."
    )
    # Find alternate isomer
    other_examples = [e for e in examples if e["class"] != chosen["class"]]
    alt_name = rng.choice(other_examples)["name"]

    ans_str = (
        f"1. {chosen['class']}; 2. The carbon atom bonded to the halogen atom is directly bonded to {chosen['bonded_c']} other carbon atom(s); "
        f"3. E.g. {alt_name}"
    )
    memo = (
        f"1. Classification: {chosen['class']} haloalkane. [1]\n"
        f"2. Reason: The carbon atom bonded to the halogen is directly bonded to {chosen['bonded_c']} other carbon atom(s). [2]\n"
        f"3. An isomer with a different classification: {alt_name}. [1]"
    )
    hints = {
        "tier_1": "Count how many carbon atoms are attached to the C-X carbon.",
        "tier_2": "1 C attached = primary; 2 C attached = secondary; 3 C attached = tertiary.",
        "tier_3": f"{chosen['name']} is {chosen['class']} because C-X carbon has {chosen['bonded_c']} carbon neighbour(s).",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">{chosen["name"]}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" fill="#334155">{chosen["formula"]}</text>'
        f'<text x="220" y="118" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">Classification: {chosen["class"]} ({chosen["bonded_c"]} attached C)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "11_haloalkanes_classification_primary_secondary_tertiary",
        "subskill": "11_haloalkanes_classification_primary_secondary_tertiary",
        "subskill_id": "11_haloalkanes_classification_primary_secondary_tertiary",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 4, "hints": hints, "misconception_tags": ["counting_total_carbons_instead_of_attached_to_functional_carbon"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Classification stated correctly", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Reason based on attached carbons to C-X", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Valid alternative isomer named", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 12. Alcohols — IUPAC Naming and Hydroxyl Functional Group
# ==============================================================================
def builder_12(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_12_alcohols_iupac", seed, idx)
    alcohols = [
        {"name": "ethanol", "condensed": "CH3-CH2-OH", "c": 2, "pos": 1, "mol": "C2H6O"},
        {"name": "propan-1-ol", "condensed": "CH3-CH2-CH2-OH", "c": 3, "pos": 1, "mol": "C3H8O"},
        {"name": "propan-2-ol", "condensed": "CH3-CH(OH)-CH3", "c": 3, "pos": 2, "mol": "C3H8O"},
        {"name": "butan-1-ol", "condensed": "CH3-(CH2)2-CH2-OH", "c": 4, "pos": 1, "mol": "C4H10O"},
        {"name": "butan-2-ol", "condensed": "CH3-CH(OH)-CH2-CH3", "c": 4, "pos": 2, "mol": "C4H10O"},
        {"name": "2-methylpropan-2-ol", "condensed": "(CH3)3C-OH", "c": 3, "pos": 2, "mol": "C4H10O"},
        {"name": "pentan-3-ol", "condensed": "CH3-CH2-CH(OH)-CH2-CH3", "c": 5, "pos": 3, "mol": "C5H12O"},
    ]
    chosen = rng.choice(alcohols)

    prompt = (
        f"Consider the alcohol with condensed structural formula {chosen['condensed']}.\n\n"
        f"1. Write down the IUPAC name for this alcohol.\n"
        f"2. Identify the functional group of the alcohol homologous series.\n"
        f"3. Write down its molecular formula.\n"
        f"4. State the general formula for the saturated aliphatic monohydric alcohols."
    )
    ans_str = (
        f"1. {chosen['name']}; 2. Hydroxyl group (-OH); 3. {chosen['mol']}; 4. CnH2n+1OH (or CnH2n+2O)"
    )
    memo = (
        f"1. IUPAC name: {chosen['name']} [2]\n"
        "2. Functional group: Hydroxyl group (-OH). [1]\n"
        f"3. Molecular formula: {chosen['mol']} [1]\n"
        "4. General formula: CnH2n+1OH (or CnH2n+2O) [1]"
    )
    hints = {
        "tier_1": "Alcohols replace the -e of alkane with -ol, indicating the locant of the -OH group.",
        "tier_2": f"Longest chain has {chosen['c']} carbons. Hydroxyl on carbon {chosen['pos']}.",
        "tier_3": f"Name = {chosen['name']}. Functional group = Hydroxyl group (-OH).",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e3a8a">{chosen["name"]}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#1d4ed8">{chosen["condensed"]}</text>'
        f'<text x="220" y="118" text-anchor="middle" font-size="12" fill="#2563eb">Functional Group: -OH (Hydroxyl) | Formula: {chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "12_alcohols_iupac_naming_hydroxyl_functional_group",
        "subskill": "12_alcohols_iupac_naming_hydroxyl_functional_group",
        "subskill_id": "12_alcohols_iupac_naming_hydroxyl_functional_group",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_hydroxyl_with_hydroxide_ion", "locant_omission_in_alcohol_name"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "IUPAC name", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Hydroxyl group identification", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Molecular formula", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "General formula CnH2n+1OH", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 13. Alcohols — Classification into Primary, Secondary, Tertiary
# ==============================================================================
def builder_13(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_13_alcohol_class", seed, idx)
    alcohols = [
        {"name": "butan-1-ol", "class": "primary (1°)", "bonded_c": 1, "formula": "CH3-CH2-CH2-CH2-OH"},
        {"name": "butan-2-ol", "class": "secondary (2°)", "bonded_c": 2, "formula": "CH3-CH(OH)-CH2-CH3"},
        {"name": "2-methylpropan-2-ol", "class": "tertiary (3°)", "bonded_c": 3, "formula": "(CH3)3C-OH"},
        {"name": "propan-1-ol", "class": "primary (1°)", "bonded_c": 1, "formula": "CH3-CH2-CH2-OH"},
        {"name": "propan-2-ol", "class": "secondary (2°)", "bonded_c": 2, "formula": "CH3-CH(OH)-CH3"},
        {"name": "2-methylbutan-2-ol", "class": "tertiary (3°)", "bonded_c": 3, "formula": "CH3-C(CH3)(OH)-CH2-CH3"},
    ]
    chosen = rng.choice(alcohols)

    prompt = (
        f"Consider the alcohol {chosen['name']} ({chosen['formula']}).\n\n"
        f"1. Classify this alcohol as primary (1°), secondary (2°), or tertiary (3°).\n"
        f"2. Provide a rigorous chemical justification for your classification based on the carbon atom bearing the hydroxyl group.\n"
        f"3. Write down the IUPAC name of an isomer of {chosen['name']} that belongs to a different classification category."
    )
    other_alcohols = [a for a in alcohols if a["class"] != chosen["class"]]
    alt_name = rng.choice(other_alcohols)["name"]

    ans_str = (
        f"1. {chosen['class']}; 2. The carbon atom bonded to the -OH group is directly attached to {chosen['bonded_c']} other carbon atom(s); "
        f"3. E.g. {alt_name}"
    )
    memo = (
        f"1. Classification: {chosen['class']} alcohol. [1]\n"
        f"2. Justification: The carbon atom bonded to the hydroxyl group (-OH) is bonded directly to {chosen['bonded_c']} other carbon atom(s). [2]\n"
        f"3. An isomer with a different classification: {alt_name}. [1]"
    )
    hints = {
        "tier_1": "Look at the carbon holding the -OH group. How many other carbons are directly attached to it?",
        "tier_2": "1 C = primary; 2 C = secondary; 3 C = tertiary.",
        "tier_3": f"{chosen['name']} is {chosen['class']} because the C-OH carbon is bonded to {chosen['bonded_c']} carbon(s).",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#14532d">{chosen["name"]}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" fill="#166534">{chosen["formula"]}</text>'
        f'<text x="220" y="118" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d">{chosen["class"].upper()} ALCOHOL ({chosen["bonded_c"]} C attached to C-OH)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "13_alcohols_classification_primary_secondary_tertiary",
        "subskill": "13_alcohols_classification_primary_secondary_tertiary",
        "subskill_id": "13_alcohols_classification_primary_secondary_tertiary",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 4, "hints": hints, "misconception_tags": ["confusing_alcohol_classification_with_chain_length"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Classification stated correctly", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Reason based on carbon attached to -OH", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Valid alternative isomer named", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 14. Alcohols — Polyhydric Diols and Triols IUPAC Naming
# ==============================================================================
def builder_14(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_14_polyhydric", seed, idx)
    poly = [
        {"name": "ethane-1,2-diol", "common": "ethylene glycol", "condensed": "CH2(OH)-CH2(OH)", "mol": "C2H6O2", "oh": 2, "c": 2},
        {"name": "propane-1,2-diol", "common": "propylene glycol", "condensed": "CH3-CH(OH)-CH2(OH)", "mol": "C3H8O2", "oh": 2, "c": 3},
        {"name": "propane-1,2,3-triol", "common": "glycerol (glycerin)", "condensed": "CH2(OH)-CH(OH)-CH2(OH)", "mol": "C3H8O3", "oh": 3, "c": 3},
        {"name": "butane-1,4-diol", "common": "1,4-butanediol", "condensed": "HO-(CH2)4-OH", "mol": "C4H10O2", "oh": 2, "c": 4},
    ]
    chosen = rng.choice(poly)

    prompt = (
        f"Consider the polyhydric alcohol commonly known as '{chosen['common']}' with condensed formula {chosen['condensed']}.\n\n"
        f"1. Write down the systematic IUPAC name for this compound.\n"
        f"2. Write down its molecular formula.\n"
        f"3. Explain why this compound has significantly higher water solubility and boiling point than a monohydric alcohol of similar molar mass."
    )
    ans_str = (
        f"1. {chosen['name']}; 2. {chosen['mol']}; "
        f"3. Multiple hydroxyl (-OH) groups allow extensive intermolecular hydrogen bonding (both between molecules and with water)."
    )
    memo = (
        f"1. Systematic IUPAC name: {chosen['name']} [2]\n"
        f"2. Molecular formula: {chosen['mol']} [1]\n"
        f"3. The presence of {chosen['oh']} hydroxyl (-OH) groups allows each molecule to form multiple hydrogen bonds with neighbouring molecules "
        f"(increasing boiling point) and with polar water molecules (enhancing water solubility). [2]"
    )
    hints = {
        "tier_1": "Keep the full alkane name (e.g. ethane-, propane-) and add -diol or -triol with position numbers.",
        "tier_2": f"Has {chosen['oh']} -OH groups on {chosen['c']} carbons: {chosen['name']}.",
        "tier_3": f"Name = {chosen['name']}. Multiple -OH groups enable extensive hydrogen bonding.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#312e81">{chosen["name"].upper()}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#4338ca">Common name: {chosen["common"]}</text>'
        f'<text x="220" y="115" text-anchor="middle" font-size="12" fill="#1e1b4b">{chosen["condensed"]} | Formula: {chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "14_alcohols_polyhydric_diols_and_triols_iupac_naming",
        "subskill": "14_alcohols_polyhydric_diols_and_triols_iupac_naming",
        "subskill_id": "14_alcohols_polyhydric_diols_and_triols_iupac_naming",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["dropping_e_before_diol_in_iupac_name"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "IUPAC name", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Molecular formula", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Hydrogen bonding explanation for physical properties", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 15. Aldehydes — IUPAC Naming and Terminal Carbonyl Group
# ==============================================================================
def builder_15(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_15_aldehydes_iupac", seed, idx)
    aldehydes = [
        {"name": "methanal", "common": "formaldehyde", "condensed": "HCHO", "c": 1, "mol": "CH2O"},
        {"name": "ethanal", "common": "acetaldehyde", "condensed": "CH3CHO", "c": 2, "mol": "C2H4O"},
        {"name": "propanal", "common": "propionaldehyde", "condensed": "CH3CH2CHO", "c": 3, "mol": "C3H6O"},
        {"name": "butanal", "common": "butyraldehyde", "condensed": "CH3(CH2)2CHO", "c": 4, "mol": "C4H8O"},
        {"name": "pentanal", "common": "valeraldehyde", "condensed": "CH3(CH2)3CHO", "c": 5, "mol": "C5H10O"},
        {"name": "2-methylpropanal", "common": "isobutyraldehyde", "condensed": "(CH3)2CHCHO", "c": 3, "mol": "C4H8O"},
    ]
    chosen = rng.choice(aldehydes)

    prompt = (
        f"Consider the organic compound with condensed structural formula {chosen['condensed']}.\n\n"
        f"1. Name the homologous series to which this compound belongs.\n"
        f"2. Write down the IUPAC name for this compound.\n"
        f"3. Identify the functional group characterizing this series and state where in the carbon chain it is always located.\n"
        f"4. State the general formula for aliphatic aldehydes."
    )
    ans_str = (
        f"1. Aldehydes; 2. {chosen['name']}; "
        f"3. Carbonyl group (formyl group, -CHO) located on a terminal carbon (carbon-1); 4. CnH2nO"
    )
    memo = (
        "1. Homologous series: Aldehydes. [1]\n"
        f"2. IUPAC name: {chosen['name']} [2]\n"
        "3. Functional group: Carbonyl group (specifically a terminal formyl group, -CHO), always on carbon-1. [1]\n"
        "4. General formula: CnH2nO [1]"
    )
    hints = {
        "tier_1": "Aldehydes end in -al and always have the C=O group at the end of the carbon chain.",
        "tier_2": f"Longest chain has {chosen['c']} carbons. Name = {chosen['name']}.",
        "tier_3": f"Series = Aldehydes. Name = {chosen['name']}. Formula = CnH2nO.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#fdf2f8" stroke="#db2777" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#9d174d">{chosen["name"].upper()}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{chosen["condensed"]}</text>'
        f'<text x="220" y="115" text-anchor="middle" font-size="12" fill="#be185d">Terminal Carbonyl (-CHO) at C1 | Formula: {chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "15_aldehydes_iupac_naming_terminal_carbonyl_group",
        "subskill": "15_aldehydes_iupac_naming_terminal_carbonyl_group",
        "subskill_id": "15_aldehydes_iupac_naming_terminal_carbonyl_group",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_aldehydes_with_alcohols_suffix", "giving_locant_1_for_aldehyde_redundantly"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Homologous series: Aldehydes", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Terminal carbonyl identification", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "General formula CnH2nO", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 16. Ketones — IUPAC Naming and Non-Terminal Carbonyl Group
# ==============================================================================
def builder_16(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_16_ketones_iupac", seed, idx)
    ketones = [
        {"name": "propanone", "common": "acetone", "condensed": "CH3-CO-CH3", "c": 3, "pos": 2, "mol": "C3H6O"},
        {"name": "butan-2-one", "common": "ethyl methyl ketone", "condensed": "CH3-CO-CH2-CH3", "c": 4, "pos": 2, "mol": "C4H8O"},
        {"name": "pentan-2-one", "common": "methyl propyl ketone", "condensed": "CH3-CO-CH2-CH2-CH3", "c": 5, "pos": 2, "mol": "C5H10O"},
        {"name": "pentan-3-one", "common": "diethyl ketone", "condensed": "CH3-CH2-CO-CH2-CH3", "c": 5, "pos": 3, "mol": "C5H10O"},
        {"name": "hexan-2-one", "common": "butyl methyl ketone", "condensed": "CH3-CO-(CH2)3-CH3", "c": 6, "pos": 2, "mol": "C6H12O"},
        {"name": "hexan-3-one", "common": "ethyl propyl ketone", "condensed": "CH3-CH2-CO-(CH2)2-CH3", "c": 6, "pos": 3, "mol": "C6H12O"},
    ]
    chosen = rng.choice(ketones)

    prompt = (
        f"Consider the organic compound with condensed structural formula {chosen['condensed']}.\n\n"
        f"1. Name the homologous series to which this compound belongs.\n"
        f"2. Write down the IUPAC name for this compound.\n"
        f"3. Explain the essential structural difference between the functional group of a ketone and that of an aldehyde.\n"
        f"4. State the minimum number of carbon atoms required for a ketone to exist."
    )
    ans_str = (
        f"1. Ketones; 2. {chosen['name']}; "
        f"3. In a ketone, the carbonyl group (C=O) is bonded to two other carbon atoms (non-terminal); in an aldehyde, it is bonded to at least one hydrogen atom (terminal); "
        f"4. 3 carbon atoms (propanone)"
    )
    memo = (
        "1. Homologous series: Ketones. [1]\n"
        f"2. IUPAC name: {chosen['name']} [2]\n"
        "3. A ketone has its carbonyl group (C=O) flanked by two carbon atoms (internal/non-terminal), "
        "whereas an aldehyde has its carbonyl group at the end of the carbon chain bonded to at least one hydrogen atom (-CHO). [1]\n"
        "4. Minimum carbon atoms: 3 carbons (the simplest ketone is propanone). [1]"
    )
    hints = {
        "tier_1": "Ketones end in -one and have a C=O group between two carbon atoms.",
        "tier_2": f"Longest chain has {chosen['c']} carbons. Carbonyl at carbon {chosen['pos']}.",
        "tier_3": f"Series = Ketones. Name = {chosen['name']}. Minimum carbons = 3.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#9a3412">{chosen["name"].upper()}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{chosen["condensed"]}</text>'
        f'<text x="220" y="115" text-anchor="middle" font-size="12" fill="#c2410c">Internal Carbonyl (C=O) at C{chosen["pos"]} | Formula: {chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "16_ketones_iupac_naming_non_terminal_carbonyl_group",
        "subskill": "16_ketones_iupac_naming_non_terminal_carbonyl_group",
        "subskill_id": "16_ketones_iupac_naming_non_terminal_carbonyl_group",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_aldehydes_and_ketones", "locant_omission_for_pentanone_and_higher"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Homologous series: Ketones", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Structural distinction from aldehyde", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Minimum carbon count = 3", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 17. Carboxylic Acids — IUPAC Naming and Carboxyl Group
# ==============================================================================
def builder_17(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_17_carb_acids_iupac", seed, idx)
    acids = [
        {"name": "methanoic acid", "common": "formic acid", "condensed": "HCOOH", "c": 1, "mol": "CH2O2"},
        {"name": "ethanoic acid", "common": "acetic acid (vinegar)", "condensed": "CH3COOH", "c": 2, "mol": "C2H4O2"},
        {"name": "propanoic acid", "common": "propionic acid", "condensed": "CH3CH2COOH", "c": 3, "mol": "C3H6O2"},
        {"name": "butanoic acid", "common": "butyric acid", "condensed": "CH3(CH2)2COOH", "c": 4, "mol": "C4H8O2"},
        {"name": "pentanoic acid", "common": "valeric acid", "condensed": "CH3(CH2)3COOH", "c": 5, "mol": "C5H10O2"},
        {"name": "2-methylpropanoic acid", "common": "isobutyric acid", "condensed": "(CH3)2CHCOOH", "c": 3, "mol": "C4H8O2"},
    ]
    chosen = rng.choice(acids)

    prompt = (
        f"Consider the organic acid with condensed structural formula {chosen['condensed']}.\n\n"
        f"1. Name the homologous series to which this compound belongs.\n"
        f"2. Write down the IUPAC name for this compound.\n"
        f"3. Name the functional group of this homologous series and write down its structural representation.\n"
        f"4. State the general formula for the aliphatic carboxylic acids."
    )
    ans_str = (
        f"1. Carboxylic acids; 2. {chosen['name']}; "
        f"3. Carboxyl group (-COOH); 4. CnH2nO2 (or CnH2n+1COOH)"
    )
    memo = (
        "1. Homologous series: Carboxylic acids. [1]\n"
        f"2. IUPAC name: {chosen['name']} [2]\n"
        "3. Functional group: Carboxyl group (-COOH), consisting of a carbonyl group (C=O) bonded to a hydroxyl group (-OH) on the same carbon. [1]\n"
        "4. General formula: CnH2nO2 (or CnH2n+1COOH) [1]"
    )
    hints = {
        "tier_1": "Carboxylic acids end in -oic acid and have the -COOH functional group.",
        "tier_2": f"Longest chain has {chosen['c']} carbons. Name = {chosen['name']}.",
        "tier_3": f"Series = Carboxylic acids. Name = {chosen['name']}. Functional group = -COOH.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#991b1b">{chosen["name"].upper()}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{chosen["condensed"]}</text>'
        f'<text x="220" y="115" text-anchor="middle" font-size="12" fill="#b91c1c">Carboxyl Group (-COOH) | Formula: {chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "17_carboxylic_acids_iupac_naming_carboxyl_group",
        "subskill": "17_carboxylic_acids_iupac_naming_carboxyl_group",
        "subskill_id": "17_carboxylic_acids_iupac_naming_carboxyl_group",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_carboxyl_with_carbonyl_only", "omitting_acid_word_in_iupac_name"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Homologous series: Carboxylic acids", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Carboxyl group definition", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "General formula CnH2nO2", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 18. Esters — IUPAC Naming and Esterification Derivation
# ==============================================================================
def builder_18(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_18_esters_iupac", seed, idx)
    esters = [
        {"name": "ethyl ethanoate", "alcohol": "ethanol", "acid": "ethanoic acid", "condensed": "CH3COOCH2CH3", "mol": "C4H8O2", "scent": "sweet pear/glue"},
        {"name": "methyl propanoate", "alcohol": "methanol", "acid": "propanoic acid", "condensed": "CH3CH2COOCH3", "mol": "C4H8O2", "scent": "fruity rum"},
        {"name": "propyl ethanoate", "alcohol": "propan-1-ol", "acid": "ethanoic acid", "condensed": "CH3COOCH2CH2CH3", "mol": "C5H10O2", "scent": "pear"},
        {"name": "ethyl methanoate", "alcohol": "ethanol", "acid": "methanoic acid", "condensed": "HCOOCH2CH3", "mol": "C3H6O2", "scent": "rum"},
        {"name": "methyl butanoate", "alcohol": "methanol", "acid": "butanoic acid", "condensed": "CH3(CH2)2COOCH3", "mol": "C5H10O2", "scent": "apple"},
        {"name": "pentyl ethanoate", "alcohol": "pentan-1-ol", "acid": "ethanoic acid", "condensed": "CH3COO(CH2)4CH3", "mol": "C7H14O2", "scent": "banana"},
    ]
    chosen = rng.choice(esters)

    prompt = (
        f"A sweet-smelling organic compound with condensed structural formula {chosen['condensed']} is prepared in the lab.\n\n"
        f"1. Name the homologous series to which this compound belongs.\n"
        f"2. Write down the IUPAC name for this ester.\n"
        f"3. Write down the IUPAC names of the alcohol and the carboxylic acid reactants used to synthesise this ester.\n"
        f"4. Identify the catalyst used in this esterification reaction."
    )
    ans_str = (
        f"1. Esters; 2. {chosen['name']}; 3. Alcohol: {chosen['alcohol']}, Carboxylic acid: {chosen['acid']}; "
        f"4. Concentrated sulfuric acid (H2SO4)"
    )
    memo = (
        "1. Homologous series: Esters. [1]\n"
        f"2. IUPAC name: {chosen['name']} [2]\n"
        f"   (The alkyl part '{chosen['name'].split()[0]}' comes from {chosen['alcohol']}; the alkanoate part '{chosen['name'].split()[1]}' comes from {chosen['acid']}).\n"
        f"3. Reactants: Alcohol = {chosen['alcohol']} [1]; Carboxylic acid = {chosen['acid']} [1]\n"
        "4. Catalyst: Concentrated sulfuric acid (conc. H₂SO₄). [1]"
    )
    hints = {
        "tier_1": "Esters have two words: alkyl (from alcohol) + alkanoate (from acid).",
        "tier_2": f"Alcohol reactant: {chosen['alcohol']}. Carboxylic acid reactant: {chosen['acid']}.",
        "tier_3": f"Name = {chosen['name']}. Catalyst = conc. H2SO4.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="30" y="25" width="380" height="130" rx="8" fill="#fdf4ff" stroke="#a855f7" stroke-width="2"/>'
        f'<text x="220" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#6b21a8">{chosen["name"].upper()}</text>'
        f'<text x="220" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{chosen["condensed"]}</text>'
        f'<text x="220" y="115" text-anchor="middle" font-size="12" fill="#7e22ce">From: {chosen["alcohol"]} + {chosen["acid"]} (conc. H₂SO₄ catalyst)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "18_esters_iupac_naming_esterification_derivation",
        "subskill": "18_esters_iupac_naming_esterification_derivation",
        "subskill_id": "18_esters_iupac_naming_esterification_derivation",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["inverting_alcohol_and_acid_parts_in_ester_name", "confusing_ester_with_ether"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Homologous series: Esters", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Alcohol precursor named correctly", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Carboxylic acid precursor named correctly", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Concentrated H2SO4 catalyst", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 19. Structural Isomers — Definition and Three Types
# ==============================================================================
def builder_19(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_19_isomers_def", seed, idx)
    mol = rng.choice(["C4H10", "C4H8", "C3H8O", "C3H6O2", "C4H8O"])

    prompt = (
        f"Organic molecules frequently exhibit structural isomerism.\n\n"
        f"1. Define the term 'structural isomer' according to CAPS curriculum standards.\n"
        f"2. Name and briefly define the three distinct types of structural isomerism studied in Grade 12.\n"
        f"3. State whether two compounds with the same molecular formula but different IUPAC names are necessarily structural isomers."
    )
    ans_str = (
        f"1. Organic molecules with the same molecular formula, but different structural formulae; "
        f"2. Chain isomers (different carbon skeleton branching), Positional isomers (same functional group at different positions), "
        f"Functional isomers (same molecular formula but different functional groups); 3. Yes."
    )
    memo = (
        "1. Structural isomers are organic compounds that have the same molecular formula, but different structural formulae. [2]\n"
        "2. The three types of structural isomers are:\n"
        "   - Chain isomers: Compounds with the same molecular formula but different arrangements/branching of the carbon skeleton. [1]\n"
        "   - Positional isomers: Compounds with the same molecular formula and same functional group, but the functional group is in different positions on the carbon chain. [1]\n"
        "   - Functional isomers: Compounds with the same molecular formula, but different functional groups (belonging to different homologous series). [1]\n"
        "3. Yes [1], if two compounds possess the identical molecular formula but different IUPAC names, their atoms are connected differently, making them structural isomers."
    )
    hints = {
        "tier_1": "Same molecular formula, different structural formulae.",
        "tier_2": "Three types: Chain (branching), Positional (group location), Functional (different series).",
        "tier_3": "1. Verbatim definition. 2. Chain, positional, functional. 3. Yes.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="400" height="140" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="2"/>'
        f'<text x="220" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">STRUCTURAL ISOMERS ({mol})</text>'
        f'<text x="220" y="70" text-anchor="middle" font-size="12" fill="#334155">Same Molecular Formula — Different Structural Formulae</text>'
        f'<rect x="35" y="90" width="115" height="55" rx="4" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="92" y="112" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">1. Chain</text>'
        f'<text x="92" y="130" text-anchor="middle" font-size="9" fill="#1e40af">Different branching</text>'
        f'<rect x="162" y="90" width="115" height="55" rx="4" fill="#fef08a" stroke="#ca8a04"/>'
        f'<text x="219" y="112" text-anchor="middle" font-size="11" font-weight="bold" fill="#854d0e">2. Positional</text>'
        f'<text x="219" y="130" text-anchor="middle" font-size="9" fill="#a16207">Different locants</text>'
        f'<rect x="290" y="90" width="115" height="55" rx="4" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="347" y="112" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">3. Functional</text>'
        f'<text x="347" y="130" text-anchor="middle" font-size="9" fill="#b91c1c">Different series</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "19_structural_isomers_definition_and_three_types",
        "subskill": "19_structural_isomers_definition_and_three_types",
        "subskill_id": "19_structural_isomers_definition_and_three_types",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["confusing_structural_isomers_with_allotropes", "confusing_positional_and_functional_isomers"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Structural isomer definition", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Chain isomer definition", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Positional isomer definition", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Functional isomer definition", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Different IUPAC name relationship", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 20. Chain Isomers — Alkanes and Alkenes
# ==============================================================================
def builder_20(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_20_chain_isomers", seed, idx)
    pairs = [
        {"formula": "C4H10", "straight": "butane", "branched": "2-methylpropane", "series": "Alkanes"},
        {"formula": "C5H12", "straight": "pentane", "branched": "2-methylbutane", "series": "Alkanes"},
        {"formula": "C5H10", "straight": "pent-1-ene", "branched": "2-methylbut-1-ene", "series": "Alkenes"},
        {"formula": "C6H14", "straight": "hexane", "branched": "2-methylpentane", "series": "Alkanes"},
    ]
    chosen = rng.choice(pairs)

    prompt = (
        f"Consider the molecular formula {chosen['formula']}.\n\n"
        f"1. Define 'chain isomers'.\n"
        f"2. Write down the IUPAC names of two chain isomers having the molecular formula {chosen['formula']}.\n"
        f"3. Write down the condensed structural formula for both isomers.\n"
        f"4. State whether these two isomers have identical or different chemical and physical properties."
    )
    ans_str = (
        f"1. Compounds with the same molecular formula but different carbon skeleton branching; "
        f"2. {chosen['straight']} and {chosen['branched']}; 3. E.g. straight chain vs branched; "
        f"4. Similar chemical properties but different physical properties (e.g. boiling point)."
    )
    memo = (
        "1. Chain isomers are compounds with the same molecular formula, but different arrangements/branching "
        "of the carbon skeleton. [2]\n"
        f"2. Two chain isomers of {chosen['formula']}: {chosen['straight']} [1] and {chosen['branched']} [1].\n"
        f"3. Straight: {chosen['straight']}; Branched: {chosen['branched']}. [1]\n"
        "4. They have similar chemical properties (belonging to same series) but different physical properties "
        "(branched isomer has lower boiling point due to smaller contact surface area). [1]"
    )
    hints = {
        "tier_1": "Chain isomers differ in how the carbon backbone is branched.",
        "tier_2": f"For {chosen['formula']}: {chosen['straight']} and {chosen['branched']}.",
        "tier_3": f"Names: {chosen['straight']} and {chosen['branched']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="190" height="140" rx="6" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>'
        f'<text x="115" y="50" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{chosen["straight"]}</text>'
        f'<text x="115" y="85" text-anchor="middle" font-size="11" fill="#334155">Straight Chain</text>'
        f'<text x="115" y="125" text-anchor="middle" font-size="11" fill="#64748b">Formula: {chosen["formula"]}</text>'
        f'<rect x="230" y="20" width="190" height="140" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="325" y="50" text-anchor="middle" font-size="13" font-weight="bold" fill="#78350f">{chosen["branched"]}</text>'
        f'<text x="325" y="85" text-anchor="middle" font-size="11" fill="#92400e">Branched Chain</text>'
        f'<text x="325" y="125" text-anchor="middle" font-size="11" fill="#b45309">Formula: {chosen["formula"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "20_chain_isomers_alkanes_and_alkenes",
        "subskill": "20_chain_isomers_alkanes_and_alkenes",
        "subskill_id": "20_chain_isomers_alkanes_and_alkenes",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["confusing_chain_isomers_with_positional_isomers"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of chain isomers", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Straight chain isomer name", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Branched chain isomer name", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Condensed structural formulas", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Physical property comparison", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 21. Positional Isomers — Alkenes and Haloalkanes
# ==============================================================================
def builder_21(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_21_pos_isomers_alkene_halo", seed, idx)
    pairs = [
        {"mol": "C4H8", "iso1": "but-1-ene", "iso2": "but-2-ene", "group": "double bond (C=C)", "series": "Alkenes"},
        {"mol": "C5H10", "iso1": "pent-1-ene", "iso2": "pent-2-ene", "group": "double bond (C=C)", "series": "Alkenes"},
        {"mol": "C3H7Cl", "iso1": "1-chloropropane", "iso2": "2-chloropropane", "group": "chloro group (-Cl)", "series": "Haloalkanes"},
        {"mol": "C4H9Br", "iso1": "1-bromobutane", "iso2": "2-bromobutane", "group": "bromo group (-Br)", "series": "Haloalkanes"},
    ]
    chosen = rng.choice(pairs)

    prompt = (
        f"Consider the two organic compounds {chosen['iso1']} and {chosen['iso2']}.\n\n"
        f"1. Define 'positional isomers'.\n"
        f"2. Write down the molecular formula shared by both compounds.\n"
        f"3. Explain why {chosen['iso1']} and {chosen['iso2']} are classified as positional isomers rather than chain isomers.\n"
        f"4. State the homologous series to which both compounds belong."
    )
    ans_str = (
        f"1. Compounds with the same molecular formula and same functional group, but the functional group is in different positions on the carbon chain; "
        f"2. {chosen['mol']}; 3. Both share the exact same unbranched carbon skeleton, differing only in the position locant of the {chosen['group']}; "
        f"4. {chosen['series']}"
    )
    memo = (
        "1. Positional isomers are compounds with the same molecular formula, but different positions of the "
        "functional group, substituent, or multiple bond on the same carbon chain. [2]\n"
        f"2. Shared molecular formula: {chosen['mol']} [1]\n"
        f"3. Both compounds possess an identical unbranched carbon chain skeleton (no change in branching), "
        f"differing solely in the locant position of the {chosen['group']} (carbon-1 vs carbon-2). [2]\n"
        f"4. Homologous series: {chosen['series']} [1]"
    )
    hints = {
        "tier_1": "Positional isomers have the same carbon skeleton, but the group moves along the chain.",
        "tier_2": f"Both have formula {chosen['mol']}. Position moves from C1 to C2.",
        "tier_3": f"Series = {chosen['series']}. Formula = {chosen['mol']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="190" height="140" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="115" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">{chosen["iso1"]}</text>'
        f'<text x="115" y="90" text-anchor="middle" font-size="11" fill="#1d4ed8">Group at Position 1</text>'
        f'<text x="115" y="125" text-anchor="middle" font-size="11" fill="#64748b">Formula: {chosen["mol"]}</text>'
        f'<rect x="230" y="20" width="190" height="140" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="325" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">{chosen["iso2"]}</text>'
        f'<text x="325" y="90" text-anchor="middle" font-size="11" fill="#1d4ed8">Group at Position 2</text>'
        f'<text x="325" y="125" text-anchor="middle" font-size="11" fill="#64748b">Formula: {chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "21_positional_isomers_alkenes_and_haloalkanes",
        "subskill": "21_positional_isomers_alkenes_and_haloalkanes",
        "subskill_id": "21_positional_isomers_alkenes_and_haloalkanes",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["confusing_positional_with_chain_isomers"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of positional isomers", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Shared molecular formula", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Explanation contrasting with chain isomers", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Homologous series identification", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 22. Positional Isomers — Alcohols and Ketones
# ==============================================================================
def builder_22(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_22_pos_alcohols_ketones", seed, idx)
    pairs = [
        {"mol": "C3H8O", "iso1": "propan-1-ol", "iso2": "propan-2-ol", "group": "-OH", "series": "Alcohols"},
        {"mol": "C4H10O", "iso1": "butan-1-ol", "iso2": "butan-2-ol", "group": "-OH", "series": "Alcohols"},
        {"mol": "C5H10O", "iso1": "pentan-2-one", "iso2": "pentan-3-one", "group": "C=O", "series": "Ketones"},
        {"mol": "C6H12O", "iso1": "hexan-2-one", "iso2": "hexan-3-one", "group": "C=O", "series": "Ketones"},
    ]
    chosen = rng.choice(pairs)

    prompt = (
        f"Consider the two compounds {chosen['iso1']} and {chosen['iso2']}.\n\n"
        f"1. State the relationship between {chosen['iso1']} and {chosen['iso2']} in terms of isomerism.\n"
        f"2. Write down the molecular formula shared by both compounds.\n"
        f"3. Write down the condensed structural formula for each compound.\n"
        f"4. State whether these two compounds belong to the same homologous series or different homologous series."
    )
    ans_str = (
        f"1. Positional isomers; 2. {chosen['mol']}; 3. {chosen['iso1']} vs {chosen['iso2']}; "
        f"4. Same homologous series ({chosen['series']})"
    )
    memo = (
        f"1. {chosen['iso1']} and {chosen['iso2']} are positional isomers [1]. They have the same carbon skeleton, "
        f"but the {chosen['group']} functional group is attached at different carbon positions. [1]\n"
        f"2. Molecular formula: {chosen['mol']} [1]\n"
        f"3. Condensed structural formulas:\n"
        f"   - {chosen['iso1']}\n"
        f"   - {chosen['iso2']} [1]\n"
        f"4. They belong to the SAME homologous series ({chosen['series']}). [1]"
    )
    hints = {
        "tier_1": "They have the same functional group on the same chain length, but at different numbered carbons.",
        "tier_2": f"Both share formula {chosen['mol']} and belong to the {chosen['series']}.",
        "tier_3": f"Relationship = Positional isomers. Series = {chosen['series']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="190" height="140" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="115" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#14532d">{chosen["iso1"]}</text>'
        f'<text x="115" y="90" text-anchor="middle" font-size="11" fill="#166534">Position 1 / 2</text>'
        f'<text x="115" y="125" text-anchor="middle" font-size="11" fill="#64748b">{chosen["mol"]}</text>'
        f'<rect x="230" y="20" width="190" height="140" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="325" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#14532d">{chosen["iso2"]}</text>'
        f'<text x="325" y="90" text-anchor="middle" font-size="11" fill="#166534">Position 2 / 3</text>'
        f'<text x="325" y="125" text-anchor="middle" font-size="11" fill="#64748b">{chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "22_positional_isomers_alcohols_and_ketones",
        "subskill": "22_positional_isomers_alcohols_and_ketones",
        "subskill_id": "22_positional_isomers_alcohols_and_ketones",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_positional_isomers_with_functional_isomers"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Positional isomers relationship identified", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Molecular formula", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Condensed structural formulas", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Same homologous series confirmation", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 23. Functional Isomers — Carboxylic Acids and Esters
# ==============================================================================
def builder_23(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_23_func_acid_ester", seed, idx)
    pairs = [
        {"mol": "C2H4O2", "acid": "ethanoic acid", "ester": "methyl methanoate", "acid_cond": "CH3COOH", "ester_cond": "HCOOCH3"},
        {"mol": "C3H6O2", "acid": "propanoic acid", "ester": "ethyl methanoate", "ester2": "methyl ethanoate", "acid_cond": "CH3CH2COOH", "ester_cond": "HCOOCH2CH3"},
        {"mol": "C4H8O2", "acid": "butanoic acid", "ester": "ethyl ethanoate", "ester2": "propyl methanoate", "acid_cond": "CH3(CH2)2COOH", "ester_cond": "CH3COOCH2CH3"},
    ]
    chosen = rng.choice(pairs)

    prompt = (
        f"Consider the molecular formula {chosen['mol']}.\n\n"
        f"1. Define 'functional isomers'.\n"
        f"2. Write down the IUPAC name and condensed structural formula of a carboxylic acid with this formula.\n"
        f"3. Write down the IUPAC name and condensed structural formula of an ester with this formula.\n"
        f"4. State why these two compounds are classified as functional isomers."
    )
    ans_str = (
        f"1. Compounds with the same molecular formula but different functional groups; "
        f"2. {chosen['acid']} ({chosen['acid_cond']}); 3. {chosen['ester']} ({chosen['ester_cond']}); "
        f"4. They share the same molecular formula ({chosen['mol']}) but have different functional groups (carboxyl vs ester)."
    )
    memo = (
        "1. Functional isomers are compounds with the same molecular formula, but different functional groups "
        "(belonging to different homologous series). [2]\n"
        f"2. Carboxylic acid: {chosen['acid']} ({chosen['acid_cond']}) [1]\n"
        f"3. Ester: {chosen['ester']} ({chosen['ester_cond']}) [1]\n"
        f"4. Reason: Both have the molecular formula {chosen['mol']}, but {chosen['acid']} contains a carboxyl group (-COOH), "
        f"while {chosen['ester']} contains an ester group (-COO-). [2]"
    )
    hints = {
        "tier_1": "Carboxylic acids and esters with the same carbon count share the general formula CnH2nO2.",
        "tier_2": f"For {chosen['mol']}: Acid is {chosen['acid']}; Ester is {chosen['ester']}.",
        "tier_3": "Functional isomers = same molecular formula, different functional groups.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="190" height="140" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>'
        f'<text x="115" y="48" text-anchor="middle" font-size="12" font-weight="bold" fill="#991b1b">Carboxylic Acid</text>'
        f'<text x="115" y="75" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{chosen["acid"]}</text>'
        f'<text x="115" y="105" text-anchor="middle" font-size="11" fill="#b91c1c">{chosen["acid_cond"]}</text>'
        f'<text x="115" y="135" text-anchor="middle" font-size="11" fill="#64748b">Group: -COOH</text>'
        f'<rect x="230" y="20" width="190" height="140" rx="6" fill="#fdf4ff" stroke="#a855f7" stroke-width="2"/>'
        f'<text x="325" y="48" text-anchor="middle" font-size="12" font-weight="bold" fill="#6b21a8">Ester</text>'
        f'<text x="325" y="75" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{chosen["ester"]}</text>'
        f'<text x="325" y="105" text-anchor="middle" font-size="11" fill="#7e22ce">{chosen["ester_cond"]}</text>'
        f'<text x="325" y="135" text-anchor="middle" font-size="11" fill="#64748b">Group: -COO-</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "23_functional_isomers_carboxylic_acids_and_esters",
        "subskill": "23_functional_isomers_carboxylic_acids_and_esters",
        "subskill_id": "23_functional_isomers_carboxylic_acids_and_esters",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["confusing_esters_with_ethers_as_isomers"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of functional isomers", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Carboxylic acid name and formula", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Ester name and formula", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Justification based on functional group difference", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 24. Functional Isomers — Aldehydes and Ketones
# ==============================================================================
def builder_24(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_24_func_ald_ket", seed, idx)
    pairs = [
        {"mol": "C3H6O", "aldehyde": "propanal", "ketone": "propanone", "ald_cond": "CH3CH2CHO", "ket_cond": "CH3COCH3"},
        {"mol": "C4H8O", "aldehyde": "butanal", "ketone": "butan-2-one", "ald_cond": "CH3(CH2)2CHO", "ket_cond": "CH3COCH2CH3"},
        {"mol": "C5H10O", "aldehyde": "pentanal", "ketone": "pentan-2-one", "ald_cond": "CH3(CH2)3CHO", "ket_cond": "CH3CO(CH2)2CH3"},
    ]
    chosen = rng.choice(pairs)

    prompt = (
        f"Consider the molecular formula {chosen['mol']}.\n\n"
        f"1. Write down the IUPAC name and condensed formula of the aldehyde with this formula.\n"
        f"2. Write down the IUPAC name and condensed formula of the ketone with this formula.\n"
        f"3. State the term used to describe the isomerism relationship between {chosen['aldehyde']} and {chosen['ketone']}.\n"
        f"4. State the general formula shared by aliphatic aldehydes and ketones."
    )
    ans_str = (
        f"1. {chosen['aldehyde']} ({chosen['ald_cond']}); 2. {chosen['ketone']} ({chosen['ket_cond']}); "
        f"3. Functional isomers; 4. CnH2nO"
    )
    memo = (
        f"1. Aldehyde: {chosen['aldehyde']} ({chosen['ald_cond']}) [1]\n"
        f"2. Ketone: {chosen['ketone']} ({chosen['ket_cond']}) [1]\n"
        f"3. {chosen['aldehyde']} and {chosen['ketone']} are functional isomers [2] because they share the same molecular "
        f"formula ({chosen['mol']}) but have different functional groups (terminal -CHO vs internal C=O).\n"
        "4. Shared general formula: CnH2nO [1]"
    )
    hints = {
        "tier_1": "Aldehydes and ketones with the same carbon count share general formula CnH2nO.",
        "tier_2": f"For {chosen['mol']}: Aldehyde = {chosen['aldehyde']}; Ketone = {chosen['ketone']}.",
        "tier_3": "Relationship = Functional isomers. Formula = CnH2nO.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="190" height="140" rx="6" fill="#fdf2f8" stroke="#db2777" stroke-width="2"/>'
        f'<text x="115" y="48" text-anchor="middle" font-size="12" font-weight="bold" fill="#9d174d">Aldehyde</text>'
        f'<text x="115" y="75" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{chosen["aldehyde"]}</text>'
        f'<text x="115" y="105" text-anchor="middle" font-size="11" fill="#be185d">{chosen["ald_cond"]}</text>'
        f'<text x="115" y="135" text-anchor="middle" font-size="11" fill="#64748b">Terminal -CHO</text>'
        f'<rect x="230" y="20" width="190" height="140" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>'
        f'<text x="325" y="48" text-anchor="middle" font-size="12" font-weight="bold" fill="#9a3412">Ketone</text>'
        f'<text x="325" y="75" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">{chosen["ketone"]}</text>'
        f'<text x="325" y="105" text-anchor="middle" font-size="11" fill="#c2410c">{chosen["ket_cond"]}</text>'
        f'<text x="325" y="135" text-anchor="middle" font-size="11" fill="#64748b">Internal C=O</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "24_functional_isomers_aldehydes_and_ketones",
        "subskill": "24_functional_isomers_aldehydes_and_ketones",
        "subskill_id": "24_functional_isomers_aldehydes_and_ketones",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_aldehydes_and_ketones_as_positional_isomers"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Aldehyde name and condensed formula", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Ketone name and condensed formula", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Functional isomers classification and reasoning", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "General formula CnH2nO", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 25. Isomer Identification from Structural Formulae
# ==============================================================================
def builder_25(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_25_isomer_ident", seed, idx)
    scenarios = [
        {
            "cmpA": "pentan-1-ol", "cmpB": "pentan-2-ol", "cmpC": "2-methylbutan-1-ol",
            "rel_AB": "positional isomers", "rel_AC": "chain isomers", "mol": "C5H12O", "series": "Alcohols"
        },
        {
            "cmpA": "but-1-ene", "cmpB": "but-2-ene", "cmpC": "2-methylprop-1-ene",
            "rel_AB": "positional isomers", "rel_AC": "chain isomers", "mol": "C4H8", "series": "Alkenes"
        },
        {
            "cmpA": "propanoic acid", "cmpB": "methyl ethanoate", "cmpC": "ethyl methanoate",
            "rel_AB": "functional isomers", "rel_AC": "functional isomers", "mol": "C3H6O2", "series": "Carboxylic acid & Esters"
        },
    ]
    chosen = rng.choice(scenarios)

    prompt = (
        f"Three organic compounds A, B, and C all have the same molecular formula {chosen['mol']}:\n"
        f"- Compound A: {chosen['cmpA']}\n"
        f"- Compound B: {chosen['cmpB']}\n"
        f"- Compound C: {chosen['cmpC']}\n\n"
        f"1. Explain why compounds A, B, and C are described as structural isomers.\n"
        f"2. Identify the specific type of isomerism between Compound A and Compound B.\n"
        f"3. Identify the specific type of isomerism between Compound A and Compound C.\n"
        f"4. State which of these compounds, if any, belong to different homologous series."
    )
    ans_str = (
        f"1. They share the same molecular formula ({chosen['mol']}) but have different structural formulae; "
        f"2. {chosen['rel_AB']}; 3. {chosen['rel_AC']}; "
        f"4. {'Compound A is a carboxylic acid while B and C are esters' if 'acid' in chosen['series'].lower() else 'All three belong to the same homologous series (' + chosen['series'] + ')'}."
    )
    memo = (
        f"1. Compounds A, B, and C are structural isomers because they have the identical molecular formula ({chosen['mol']}) "
        "but different structural arrangements of atoms. [2]\n"
        f"2. Compound A ({chosen['cmpA']}) and Compound B ({chosen['cmpB']}) are {chosen['rel_AB']}. [1]\n"
        f"3. Compound A ({chosen['cmpA']}) and Compound C ({chosen['cmpC']}) are {chosen['rel_AC']}. [1]\n"
        f"4. Homologous series check: {'A is a carboxylic acid, while B and C are esters (different homologous series)' if 'acid' in chosen['series'].lower() else 'All three belong to the same homologous series (' + chosen['series'] + ')'}. [1]"
    )
    hints = {
        "tier_1": "Compare chain length, position of functional group, and functional group type.",
        "tier_2": f"Between A and B: {chosen['rel_AB']}. Between A and C: {chosen['rel_AC']}.",
        "tier_3": f"A vs B = {chosen['rel_AB']}. A vs C = {chosen['rel_AC']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="125" height="140" rx="6" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="82" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">Compound A</text>'
        f'<text x="82" y="80" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">{chosen["cmpA"]}</text>'
        f'<rect x="157" y="20" width="125" height="140" rx="6" fill="#fef08a" stroke="#ca8a04"/>'
        f'<text x="219" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">Compound B</text>'
        f'<text x="219" y="80" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">{chosen["cmpB"]}</text>'
        f'<rect x="295" y="20" width="125" height="140" rx="6" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="357" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#991b1b">Compound C</text>'
        f'<text x="357" y="80" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">{chosen["cmpC"]}</text>'
        f'<text x="220" y="145" text-anchor="middle" font-size="11" font-weight="bold" fill="#475569">Formula: {chosen["mol"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "25_isomers_identification_from_structural_formulae",
        "subskill": "25_isomers_identification_from_structural_formulae",
        "subskill_id": "25_isomers_identification_from_structural_formulae",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_chain_positional_and_functional_isomers"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of structural isomers", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Identification of relationship between A and B", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Identification of relationship between A and C", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Homologous series analysis", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


BUILDERS_01_25: Dict[str, Any] = {
    "01_organic_molecular_definitions_and_uniqueness_of_carbon": builder_01,
    "02_hydrocarbons_saturated_vs_unsaturated": builder_02,
    "03_homologous_series_characteristics_and_general_formulae": builder_03,
    "04_alkanes_straight_chain_iupac_naming_c1_c8": builder_04,
    "05_alkanes_branched_chain_iupac_naming": builder_05,
    "06_alkanes_drawing_structural_formulae": builder_06,
    "07_alkenes_straight_chain_iupac_naming_position_of_double_bond": builder_07,
    "08_alkenes_branched_chain_iupac_naming": builder_08,
    "09_alkynes_iupac_naming_and_structures": builder_09,
    "10_haloalkanes_iupac_naming_and_halogen_substituents": builder_10,
    "11_haloalkanes_classification_primary_secondary_tertiary": builder_11,
    "12_alcohols_iupac_naming_hydroxyl_functional_group": builder_12,
    "13_alcohols_classification_primary_secondary_tertiary": builder_13,
    "14_alcohols_polyhydric_diols_and_triols_iupac_naming": builder_14,
    "15_aldehydes_iupac_naming_terminal_carbonyl_group": builder_15,
    "16_ketones_iupac_naming_non_terminal_carbonyl_group": builder_16,
    "17_carboxylic_acids_iupac_naming_carboxyl_group": builder_17,
    "18_esters_iupac_naming_esterification_derivation": builder_18,
    "19_structural_isomers_definition_and_three_types": builder_19,
    "20_chain_isomers_alkanes_and_alkenes": builder_20,
    "21_positional_isomers_alkenes_and_haloalkanes": builder_21,
    "22_positional_isomers_alcohols_and_ketones": builder_22,
    "23_functional_isomers_carboxylic_acids_and_esters": builder_23,
    "24_functional_isomers_aldehydes_and_ketones": builder_24,
    "25_isomers_identification_from_structural_formulae": builder_25,
}
