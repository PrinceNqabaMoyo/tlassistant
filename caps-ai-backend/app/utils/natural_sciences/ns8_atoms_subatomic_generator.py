"""Natural Sciences Grade 8 Term 2: Atoms and Subatomic Structure Generator.

Strictly grounded in curriculum_docs_auto/NaturalSciences_Gr8/Syllabus.md.
Covers:
- subatomic_particles_and_charges: Protons (+1, nucleus), Neutrons (0, nucleus), Electrons (-1, orbital cloud).
- atomic_number_and_neutrality: Protons = Electrons in neutral atoms; atomic mass = protons + neutrons.
- first_twenty_elements_and_symbols: Standard IUPAC chemical symbols and positions for the first 20 elements.
- elements_compounds_diatomic_molecules: Diatomic molecules (H2, N2, O2, Cl2) vs chemical compounds (H2O, CO2, NaCl).
- decomposition_of_compounds_electrolysis: Chemical vs physical breakdown, electrolysis of CuCl2 and thermal decomposition.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


SUBSKILLS = [
    "subatomic_particles_and_charges",
    "atomic_number_and_neutrality",
    "first_twenty_elements_and_symbols",
    "elements_compounds_diatomic_molecules",
    "decomposition_of_compounds_electrolysis",
]

ELEMENTS_FIRST_20 = [
    {"z": 1, "name": "Hydrogen", "symbol": "H", "mass": 1, "p": 1, "n": 0, "e": 1},
    {"z": 2, "name": "Helium", "symbol": "He", "mass": 4, "p": 2, "n": 2, "e": 2},
    {"z": 3, "name": "Lithium", "symbol": "Li", "mass": 7, "p": 3, "n": 4, "e": 3},
    {"z": 6, "name": "Carbon", "symbol": "C", "mass": 12, "p": 6, "n": 6, "e": 6},
    {"z": 7, "name": "Nitrogen", "symbol": "N", "mass": 14, "p": 7, "n": 7, "e": 7},
    {"z": 8, "name": "Oxygen", "symbol": "O", "mass": 16, "p": 8, "n": 8, "e": 8},
    {"z": 11, "name": "Sodium", "symbol": "Na", "mass": 23, "p": 11, "n": 12, "e": 11},
    {"z": 12, "name": "Magnesium", "symbol": "Mg", "mass": 24, "p": 12, "n": 12, "e": 12},
    {"z": 13, "name": "Aluminium", "symbol": "Al", "mass": 27, "p": 13, "n": 14, "e": 13},
    {"z": 17, "name": "Chlorine", "symbol": "Cl", "mass": 35, "p": 17, "n": 18, "e": 17},
    {"z": 20, "name": "Calcium", "symbol": "Ca", "mass": 40, "p": 20, "n": 20, "e": 20},
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _build_subatomic_particles(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    particles = [
        {"name": "Proton", "charge": "+1 (positive)", "location": "inside the central nucleus", "mass": "1 atomic mass unit (amu)"},
        {"name": "Neutron", "charge": "0 (neutral / no charge)", "location": "inside the central nucleus", "mass": "1 atomic mass unit (amu)"},
        {"name": "Electron", "charge": "-1 (negative)", "location": "in orbital shells orbiting the nucleus", "mass": "negligible (approx. 1/1836 amu)"}
    ]
    p = rng.choice(particles)
    prompt = (
        f"In atomic theory, atoms are composed of three sub-atomic particles.\n\n"
        f"Which sub-atomic particle possesses a charge of **{p['charge']}** and is located **{p['location']}**?"
    )
    correct_ans = p["name"]
    distractors = [x["name"] for x in particles if x["name"] != correct_ans]
    distractors.append("Positron")
    options = [correct_ans] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Recall the three sub-atomic particles:\n"
        f"1. Protons: Positive charge (+1), located in the nucleus.\n"
        f"1. Neutrons: Neutral (0 charge), located in the nucleus.\n"
        f"2. Electrons: Negative charge (-1), located in orbitals around the nucleus.\n\n"
        f"Step 2: Match:\n"
        f"The particle with {p['charge']} located {p['location']} is the **{correct_ans}**."
    )
    return {
        "id": _make_id("ns8_atom_sub", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "subatomic_particles_and_charges",
        "question_family_id": "subatomic_particles_and_charges",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Atoms > Sub-atomic particles",
        "hints": {
            "tier_1": "Recall the charges: Protons = positive, Neutrons = neutral, Electrons = negative.",
            "tier_2": "Protons and neutrons sit in the central nucleus; electrons orbit in the empty space.",
            "tier_3": f"The answer is {correct_ans}."
        },
        "misconception_tags": ["confuses_electrons_with_protons"]
    }


def _build_atomic_number_neutrality(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    elem = rng.choice(ELEMENTS_FIRST_20)
    prompt = (
        f"Consider a neutral atom of **{elem['name']}** with atomic number $Z = {elem['z']}$ and mass number $A = {elem['mass']}$.\n\n"
        f"1. State the number of protons contained in the nucleus.\n"
        f"2. State the number of electrons orbiting the nucleus.\n"
        f"3. State the number of neutrons contained in the nucleus.\n"
        f"4. Explain why this atom has an overall electrical charge of zero (is neutral)."
    )
    sample_answer = (
        f"1. Protons: {elem['p']}\n"
        f"2. Electrons: {elem['e']}\n"
        f"3. Neutrons: {elem['n']} (Mass number - Atomic number = {elem['mass']} - {elem['z']} = {elem['n']})\n"
        f"4. The atom is neutral because the number of positively charged protons ({elem['p']}) exactly equals the number of negatively charged electrons ({elem['e']}), so the opposite charges cancel out completely."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        f"1. Protons: {elem['p']} [1 mark].\n"
        f"2. Electrons: {elem['e']} [1 mark].\n"
        f"3. Neutrons: {elem['n']} [1 mark].\n"
        "4. Electrical neutrality: Number of positive protons equals number of negative electrons ($N_{p^+} = N_{e^-}$) [1 mark]."
    )
    return {
        "id": _make_id("ns8_atom_neut", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "atomic_number_and_neutrality",
        "question_family_id": "atomic_number_and_neutrality",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Atoms > Atomic number and neutrality",
        "hints": {
            "tier_1": "Atomic number (Z) = number of protons = number of electrons in a neutral atom.",
            "tier_2": "Number of neutrons = Mass number (A) minus Atomic number (Z).",
            "tier_3": f"Protons: {elem['p']}, Electrons: {elem['e']}, Neutrons: {elem['n']}."
        },
        "misconception_tags": ["neutrons_equal_mass_number_misconception"]
    }


def _build_first_twenty_elements(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    elem = rng.choice(ELEMENTS_FIRST_20)
    prompt = (
        f"On the Periodic Table of Elements, every chemical element is represented by a unique standardized chemical symbol.\n\n"
        f"What is the correct chemical symbol and atomic number ($Z$) for the element **{elem['name']}**?"
    )
    correct_ans = f"Symbol: {elem['symbol']} (Atomic number Z = {elem['z']})"
    distractors = [
        f"Symbol: {elem['name'][:2].capitalize()} (Atomic number Z = {elem['z'] + 2})",
        f"Symbol: {elem['symbol'].lower()} (Atomic number Z = {elem['mass']})",
        f"Symbol: {elem['name'][0]} (Atomic number Z = {max(1, elem['z'] - 1)})"
    ]
    options = [correct_ans] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Recall the IUPAC chemical symbol for {elem['name']}:\n"
        f"The chemical symbol is **{elem['symbol']}**.\n\n"
        f"Step 2: Identify atomic number:\n"
        f"{elem['name']} has atomic number $Z = {elem['z']}$."
    )
    return {
        "id": _make_id("ns8_elem_sym", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "first_twenty_elements_and_symbols",
        "question_family_id": "first_twenty_elements_and_symbols",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Atoms > First 20 elements",
        "hints": {
            "tier_1": "Remember that chemical symbols always start with a capital letter.",
            "tier_2": f"Think of the position of {elem['name']} on the Periodic Table.",
            "tier_3": f"The answer is {correct_ans}."
        },
        "misconception_tags": ["lowercase_chemical_symbol_misconception"]
    }


def _build_elements_compounds_diatomic(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    examples = [
        ("water ($H_2O$)", "salt water solution"),
        ("carbon dioxide ($CO_2$)", "unfiltered air"),
        ("table salt ($NaCl$)", "a mixture of sand and table salt")
    ]
    comp, mix = rng.choice(examples)
    prompt = (
        f"Chemical substances are classified as elements, diatomic molecules, compounds, or mixtures.\n\n"
        f"1. Define the term **element** in terms of atoms.\n"
        f"2. Explain what a **diatomic molecule** is, and give two examples.\n"
        f"3. Explain the difference between a **compound** (such as {comp}) and a **mixture** (such as {mix})."
    )
    sample_answer = (
        "1. An element is a pure substance made up of only one kind of atom that cannot be broken down into simpler substances by chemical reactions.\n"
        "2. A diatomic molecule consists of two identical atoms chemically bonded together (e.g., Oxygen gas: O2, Nitrogen gas: N2, Hydrogen gas: H2, or Chlorine gas: Cl2).\n"
        "3. In a compound, two or more different elements are chemically bonded in a fixed ratio and can only be separated by chemical means. In a mixture, substances are physically mingled in variable proportions without chemical bonds and can be separated by physical separation methods (like evaporation)."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Element definition: Pure substance composed of identical atoms [1 mark].\n"
        "2. Diatomic molecule definition and 2 examples: Molecule composed of two bonded identical atoms (O2, N2, H2, Cl2) [1 mark].\n"
        "3. Compound vs Mixture: Compounds have chemically bonded atoms in fixed ratios (separated chemically) [1 mark]; mixtures are physically combined in variable ratios (separated physically) [1 mark]."
    )
    return {
        "id": _make_id("ns8_elem_comp", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "elements_compounds_diatomic_molecules",
        "question_family_id": "elements_compounds_diatomic_molecules",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Atoms > Elements, compounds, and diatomic molecules",
        "hints": {
            "tier_1": "Elements have one type of atom; compounds have different atoms bonded chemically.",
            "tier_2": "Diatomic means two atoms: O2, N2, H2.",
            "tier_3": "Compounds require chemical reactions to break down; mixtures are separated physically."
        },
        "misconception_tags": ["confuses_compound_with_mixture"]
    }


def _build_decomposition_electrolysis(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    volts = rng.choice([6, 9, 12])
    settings = [
        "In a school chemistry laboratory practical",
        "During a physical sciences electrochemistry investigation",
        "In a laboratory workstation demonstration"
    ]
    prompt = (
        f"{rng.choice(settings)}, learners set up an electrolysis apparatus containing a blue solution of "
        f"copper(II) chloride ($CuCl_2$) connected to a {volts} V DC battery via inert carbon electrodes.\n\n"
        f"1. Define the process of **electrolysis**.\n"
        f"2. State what observable substance deposits at the negative cathode electrode.\n"
        f"3. Name the pungent, bleaching gas that bubbles off at the positive anode electrode.\n"
        f"4. Write the word equation for this decomposition reaction."
    )
    sample_answer = (
        "1. Electrolysis is the chemical decomposition of a compound into simpler substances using an electric current.\n"
        "2. Reddish-brown copper metal (Cu) deposits at the cathode.\n"
        "3. Chlorine gas (Cl2).\n"
        "4. Copper(II) chloride -> Copper + Chlorine gas"
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Electrolysis definition: Chemical decomposition using electrical energy [1 mark].\n"
        "2. Cathode deposit: Reddish-brown metallic copper [1 mark].\n"
        "3. Anode gas: Chlorine gas [1 mark].\n"
        "4. Word equation: Copper(II) chloride -> Copper + Chlorine [1 mark]."
    )
    diag_electrolysis = {
        "image_type": "electrolytic_cell_apparatus",
        "state": "static",
        "view": "exam",
        "diagram_role": "context",
    }

    return {
        "id": _make_id("ns8_electrolysis", seed, idx),
        "question_type": "paragraph",
        "modality": "diagram",
        "diagram_spec": diag_electrolysis,
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "decomposition_of_compounds_electrolysis",
        "question_family_id": "decomposition_of_compounds_electrolysis",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Atoms > Decomposition of compounds",
        "hints": {
            "tier_1": "Electro- means electricity, -lysis means splitting or decomposing.",
            "tier_2": "CuCl2 splits into copper metal and chlorine gas.",
            "tier_3": "Copper deposits at the cathode; chlorine gas bubbles at the anode."
        },
        "misconception_tags": ["electrolysis_is_physical_change_misconception"]
    }


def generate(archetype: Optional[str] = None, seed: Optional[int] = None, count: int = 1, **kwargs) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    results = []
    for idx in range(count):
        target = archetype or rng.choice(SUBSKILLS)
        if target == "subatomic_particles_and_charges":
            item = _build_subatomic_particles(rng, seed, idx)
        elif target == "atomic_number_and_neutrality":
            item = _build_atomic_number_neutrality(rng, seed, idx)
        elif target == "first_twenty_elements_and_symbols":
            item = _build_first_twenty_elements(rng, seed, idx)
        elif target == "elements_compounds_diatomic_molecules":
            item = _build_elements_compounds_diatomic(rng, seed, idx)
        elif target == "decomposition_of_compounds_electrolysis":
            item = _build_decomposition_electrolysis(rng, seed, idx)
        else:
            item = _build_subatomic_particles(rng, seed, idx)
        results.append(item)
    return results


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)
