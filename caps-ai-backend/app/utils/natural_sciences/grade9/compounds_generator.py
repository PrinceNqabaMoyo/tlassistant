"""Natural Sciences Grade 9 Term 2: Compounds Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 2/01. Compounds.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. first_20_elements_atomic_data: Element symbols, atomic number Z, mass number A, metals vs non-metals.
2. binary_compounds_atomic_ratios: Molecular atomic ratios (CO, CO2, H2O, NH3, NaCl, MgO).
3. systematic_naming_prefixes: Greek prefixes mono-, di-, tri- and naming rules.
4. pure_substances_vs_mixtures: Particulate model distinguishing elements, compounds, and physical mixtures.
5. chemical_formula_derivation: Deriving chemical formulas from combining ratios and constituent elements.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences.natural_sciences_builders import (
    build_atomic_bohr_ns_question,
    build_particle_model_question,
)

TOPIC_NAME = "Compounds"
ORDERED_SUBSKILLS = [
    "first_20_elements_atomic_data",
    "binary_compounds_atomic_ratios",
    "systematic_naming_prefixes",
    "pure_substances_vs_mixtures",
    "chemical_formula_derivation",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_comp"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any]) -> Dict[str, Any]:
    if "marking_guide" not in res and "marking_schema" in res:
        res["marking_guide"] = res["marking_schema"]
    if "marking_schema" not in res and "marking_guide" in res:
        res["marking_schema"] = res["marking_guide"]
    res["topic"] = TOPIC_NAME
    res["grade"] = "9"
    res["term"] = 2
    return res


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "practice",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    if subskill in ("mixed", "auto", "", None):
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]
    elif subskill in ("bohr", "atomic_structure", "bohr_model"):
        return _normalize_res(build_atomic_bohr_ns_question(actual_seed, grade=9, mode=mode))
    elif subskill in ("particles", "particle_model", "states_of_matter"):
        return _normalize_res(build_particle_model_question(actual_seed, grade=9, mode=mode))
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: First 20 Elements Atomic Data
    if chosen_subskill == "first_20_elements_atomic_data":
        elements = [
            ("Hydrogen", "H", 1, 1, "Non-metal"),
            ("Helium", "He", 2, 4, "Non-metal (Noble gas)"),
            ("Carbon", "C", 6, 12, "Non-metal"),
            ("Nitrogen", "N", 7, 14, "Non-metal"),
            ("Oxygen", "O", 8, 16, "Non-metal"),
            ("Sodium", "Na", 11, 23, "Metal (Alkali metal)"),
            ("Magnesium", "Mg", 12, 24, "Metal (Alkaline earth metal)"),
            ("Aluminium", "Al", 13, 27, "Metal"),
            ("Silicon", "Si", 14, 28, "Semi-metal (Metalloid)"),
            ("Sulfur", "S", 16, 32, "Non-metal"),
            ("Chlorine", "Cl", 17, 35, "Non-metal (Halogen)"),
            ("Potassium", "K", 19, 39, "Metal"),
            ("Calcium", "Ca", 20, 40, "Metal"),
            ("Iron", "Fe", 26, 56, "Metal (Transition metal)"),
            ("Copper", "Cu", 29, 64, "Metal (Transition metal)"),
        ]
        el = elements[actual_seed % len(elements)]
        neutrons = el[3] - el[2]
        question_text = (
            "The Periodic Table of Elements organizes elements according to their atomic numbers.\n\n"
            f"Refer to the element **{el[0]}**:\n"
            f"1. State the chemical symbol for {el[0]}.\n"
            f"2. Give the **atomic number (Z)** and the **mass number (A)** of {el[0]}.\n"
            f"3. Calculate the number of **protons, neutrons, and electrons** in a neutral atom of {el[0]}.\n"
            f"4. Classify {el[0]} as a **metal**, **non-metal**, or **semi-metal**."
        )
        sample = (
            f"1. **Symbol:** {el[1]};\n"
            f"2. **Atomic Number (Z):** {el[2]}; **Mass Number (A):** {el[3]};\n"
            f"3. **Subatomic Particles:**\n"
            f"   • Protons = {el[2]} (equal to atomic number Z);\n"
            f"   • Electrons = {el[2]} (in a neutral atom, electrons equal protons);\n"
            f"   • Neutrons = {el[3]} - {el[2]} = {neutrons} (Mass number A minus atomic number Z);\n"
            f"4. **Classification:** {el[4]}."
        )
        marking = (
            f"• 1 mark: Correct symbol ({el[1]}) [1]\n"
            f"• 1 mark: Atomic number ({el[2]}) and mass number ({el[3]}) [1]\n"
            f"• 2 marks: Protons ({el[2]}), electrons ({el[2]}), and neutrons ({neutrons}) [2]\n"
            f"• 1 mark: Classification ({el[4]}) [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": f"Element Atomic Structure: {el[0]}",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 2,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                f"Atomic number Z is the number of protons. For {el[0]}, Z = {el[2]}.",
                "Neutrons = Mass Number (A) - Atomic Number (Z). In neutral atoms, electrons = protons.",
                f"Symbol: {el[1]}. Protons = {el[2]}, Neutrons = {neutrons}, Electrons = {el[2]}. Type: {el[4]}.",
            ],
            "misconception_tags": ["atomic_number_mass_number_inversion", "neutron_calculation_error"],
            "learning_objective_id": "NS9.MM.06.01",
        }

    # Subskill 2: Binary Compounds & Atomic Ratios
    if chosen_subskill == "binary_compounds_atomic_ratios":
        compounds = [
            ("Water", "H₂O", "Hydrogen and Oxygen", "2 : 1", "2 Hydrogen atoms for every 1 Oxygen atom"),
            ("Carbon dioxide", "CO₂", "Carbon and Oxygen", "1 : 2", "1 Carbon atom for every 2 Oxygen atoms"),
            ("Carbon monoxide", "CO", "Carbon and Oxygen", "1 : 1", "1 Carbon atom for every 1 Oxygen atom"),
            ("Ammonia", "NH₃", "Nitrogen and Hydrogen", "1 : 3", "1 Nitrogen atom for every 3 Hydrogen atoms"),
            ("Methane", "CH₄", "Carbon and Hydrogen", "1 : 4", "1 Carbon atom for every 4 Hydrogen atoms"),
            ("Sulfur trioxide", "SO₃", "Sulfur and Oxygen", "1 : 3", "1 Sulfur atom for every 3 Oxygen atoms"),
            ("Copper(II) oxide", "CuO", "Copper and Oxygen", "1 : 1", "1 Copper atom for every 1 Oxygen atom"),
            ("Iron(III) oxide (rust)", "Fe₂O₃", "Iron and Oxygen", "2 : 3", "2 Iron atoms for every 3 Oxygen atoms"),
        ]
        comp = compounds[actual_seed % len(compounds)]
        question_text = (
            f"A chemical compound is formed when atoms of two or more different elements bond in fixed ratios.\n\n"
            f"Consider the chemical formula for **{comp[0]} ({comp[1]})**:\n"
            f"1. Name the **constituent elements** that make up {comp[0]}.\n"
            f"2. State the **exact ratio** of atoms in this compound.\n"
            f"3. Explain what the subscript number in the formula indicates.\n"
            "4. Is it possible to separate this compound into its constituent elements by physical means like filtration? Explain."
        )
        sample = (
            f"1. **Constituent Elements:** {comp[2]};\n"
            f"2. **Atomic Combining Ratio:** {comp[3]} ({comp[4]});\n"
            "3. **Subscript Number:** The subscript indicates the number of atoms of the preceding element present in one molecule of the compound. (If there is no subscript, the number 1 is understood);\n"
            "4. **No**, chemical compounds can only be separated into elements by chemical methods (such as electrolysis or chemical reduction), never by physical separation like filtration."
        )
        marking = (
            f"• 1 mark: Constituent elements ({comp[2]}) [1]\n"
            f"• 1 mark: Correct combining ratio ({comp[3]}) [1]\n"
            "• 1 mark: Subscript definition (number of atoms of that element in the molecule) [1]\n"
            "• 1 mark: Physical separation impossible; requires chemical reaction [1]\n"
            "**Total: 4 marks**"
        )
        return {
            "title": f"Compound Atomic Ratio: {comp[0]}",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 2,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                f"Look at the letters and numbers in {comp[1]}. What elements do they represent?",
                f"Count the atoms of each element in {comp[1]} to find the ratio.",
                f"Elements: {comp[2]}. Ratio: {comp[3]}. Subscripts show atom count. Chemical bonds cannot be broken physically.",
            ],
            "misconception_tags": ["subscript_coefficient_conflation", "compound_physical_separation_error"],
            "learning_objective_id": "NS9.MM.06.02",
        }

    # Subskill 3: Systematic Naming Prefixes
    if chosen_subskill == "systematic_naming_prefixes":
        prefix_items = [
            ("CO", "Carbon monoxide", "mono- means 1 oxygen atom bonded to carbon"),
            ("CO₂", "Carbon dioxide", "di- means 2 oxygen atoms bonded to carbon"),
            ("SO₂", "Sulfur dioxide", "di- means 2 oxygen atoms bonded to sulfur"),
            ("SO₃", "Sulfur trioxide", "tri- means 3 oxygen atoms bonded to sulfur"),
            ("NO₂", "Nitrogen dioxide", "di- means 2 oxygen atoms bonded to nitrogen"),
            ("N₂O", "Dinitrogen monoxide (nitrous oxide)", "di- means 2 nitrogen atoms, mono- means 1 oxygen atom"),
        ]
        target_item = prefix_items[actual_seed % len(prefix_items)]
        question_text = (
            "Chemical compounds formed between non-metals use Greek prefixes to indicate the number of atoms present.\n\n"
            f"1. State the systematic chemical name for the compound with the formula **{target_item[0]}**.\n"
            "2. State the meaning of the prefix prefixes: **mono-**, **di-**, and **tri-**.\n"
            "3. Write the chemical formula for: **Dinitrogen tetroxide**."
        )
        sample = (
            f"1. **Chemical Name:** {target_item[1]};\n"
            "2. **Prefix Meanings:**\n"
            "   • *mono-* = one (1) atom;\n"
            "   • *di-* = two (2) atoms;\n"
            "   • *tri-* = three (3) atoms;\n"
            "3. **Formula:** N₂O₄ (di = 2 N, tetra = 4 O)."
        )
        marking = (
            f"• 1 mark: Correct name ({target_item[1]}) [1]\n"
            "• 2 marks: Correct definitions for mono- (1), di- (2), and tri- (3) [2]\n"
            "• 1 mark: N₂O₄ [1]\n"
            "**Total: 4 marks**"
        )
        return {
            "title": "Systematic Chemical Naming & Prefixes",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 2,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Prefix mono = 1, di = 2, tri = 3, tetra = 4.",
                f"Formula {target_item[0]} has oxygen atoms matching the Greek prefix.",
                f"Name: {target_item[1]}. mono=1, di=2, tri=3. Dinitrogen tetroxide is N₂O₄.",
            ],
            "misconception_tags": ["chemical_prefix_confusion", "inorganic_nomenclature_error"],
            "learning_objective_id": "NS9.MM.06.03",
        }

    # Subskill 4: Pure Substances vs Mixtures (Particle Model)
    if chosen_subskill == "pure_substances_vs_mixtures":
        if actual_seed % 2 == 0:
            return _normalize_res(build_particle_model_question(actual_seed, grade=9, mode=mode))
        question_text = (
            "Matter can be classified as pure substances (elements and compounds) or physical mixtures.\n\n"
            "1. Define the fundamental difference between an **element** and a **compound** at the submicroscopic level.\n"
            "2. Classify each of the following four substances as an **element**, a **compound**, or a **mixture**:\n"
            "   (a) Pure distilled water (H₂O)\n"
            "   (b) Oxygen gas (O₂)\n"
            "   (c) Air (containing nitrogen, oxygen, argon, and carbon dioxide)\n"
            "   (d) Table salt (sodium chloride, NaCl)\n"
            "3. State **two properties** of a mixture that distinguish it from a compound."
        )
        sample = (
            "1. **Element vs Compound:** An element consists of only one type of atom (same atomic number Z) that cannot be broken down chemically; a compound consists of two or more different types of atoms chemically bonded in a fixed ratio;\n"
            "2. **Classifications:**\n"
            "   (a) Distilled water (H₂O): **Compound**;\n"
            "   (b) Oxygen gas (O₂): **Element** (diatomic molecule of one type of atom);\n"
            "   (c) Air: **Mixture** (physically combined gases with variable proportions);\n"
            "   (d) Table salt (NaCl): **Compound**;\n"
            "3. **Mixture Characteristics:**\n"
            "   • Components are physically mixed and retain their original individual properties;\n"
            "   • Components can be separated by physical separation methods (filtration, distillation, evaporation);\n"
            "   • Proportions of components can vary (no fixed chemical ratio)."
        )
        marking = (
            "• 1 mark: Submicroscopic distinction (one atom type vs chemically bonded different atom types) [1]\n"
            "• 2 marks: Four correct classifications (H2O compound, O2 element, Air mixture, NaCl compound) [2]\n"
            "• 1 mark: Mixture properties (retains original properties / physical separation / variable ratio) [1]\n"
            "**Total: 4 marks**"
        )
        return {
            "title": "Elements, Compounds & Mixtures",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 2,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "An element has only 1 symbol on the periodic table; a compound has 2 or more chemically joined together.",
                "Air is a mixture of separate gases. Water is a single chemical compound (H2O).",
                "Element: 1 atom type. Compound: chemically bonded. Air is mixture; H2O & NaCl are compounds; O2 is element.",
            ],
            "misconception_tags": ["diatomic_element_is_compound_myth", "mixture_compound_conflation"],
            "learning_objective_id": "NS9.MM.06.04",
        }

    # Subskill 5: Chemical Formula Derivation
    formula_puzzles = [
        ("Sodium and Chlorine", "Sodium transfers 1 valence electron to chlorine, forming Na⁺ and Cl⁻ ions in a 1:1 ratio", "NaCl", "Sodium chloride"),
        ("Magnesium and Oxygen", "Magnesium loses 2 electrons (Mg²⁺) and oxygen gains 2 electrons (O²⁻) in a 1:1 ratio", "MgO", "Magnesium oxide"),
        ("Aluminium and Oxygen", "Two Al³⁺ ions combine with three O²⁻ ions to balance electrical charges (2 × +3 = +6; 3 × -2 = -6)", "Al₂O₃", "Aluminium oxide"),
        ("Calcium and Chlorine", "One Ca²⁺ ion requires two Cl⁻ ions to balance charge (+2 + 2(-1) = 0)", "CaCl₂", "Calcium chloride"),
    ]
    puz = formula_puzzles[actual_seed % len(formula_puzzles)]
    question_text = (
        f"When atoms react to form ionic or covalent compounds, they combine in definite proportions.\n\n"
        f"Consider the reaction between **{puz[0]}**:\n"
        f"1. State the **chemical formula** of the resulting compound.\n"
        f"2. Write the **systematic chemical name** for this compound.\n"
        "3. Explain why the atoms combine in this specific combining ratio based on electrical balance."
    )
    sample = (
        f"1. **Chemical Formula:** {puz[2]};\n"
        f"2. **Chemical Name:** {puz[3]};\n"
        f"3. **Combining Rationale:** {puz[1]}."
    )
    marking = (
        f"• 1 mark: Correct formula ({puz[2]}) with proper subscripts [1]\n"
        f"• 1 mark: Correct name ({puz[3]}) [1]\n"
        f"• 2 marks: Electrical balance explanation ({puz[1]}) [2]\n"
        "**Total: 4 marks**"
    )
    return {
        "title": f"Formula Derivation: {puz[3]}",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 2,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            f"Think about the combining ratio of {puz[0]}.",
            f"Formula: {puz[2]}. Name: {puz[3]}.",
            f"Formula is {puz[2]}; name is {puz[3]}. Charges balance to neutral zero.",
        ],
        "misconception_tags": ["formula_subscript_balance_error", "ionic_ratio_miscalculation"],
        "learning_objective_id": "NS9.MM.06.05",
    }
