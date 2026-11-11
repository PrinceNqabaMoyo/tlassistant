"""
Grade 7 Natural Sciences - Term 2: The Periodic Table of Elements (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/04. The Periodic Table of Elements.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Elements, Atoms & History (01 - 08)
# ==============================================================================

def arch_01_element_definition_pure_substance(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("pure copper metal wire", "Copper (Cu)", "cannot be broken down into anything simpler by chemical heating or electrolysis"),
        ("pure oxygen gas inside a diving cylinder", "Oxygen (O2)", "consists only of oxygen atoms and cannot be decomposed chemically"),
        ("pure gold ingot in a bank vault", "Gold (Au)", "contains exclusively gold atoms and cannot be separated into simpler chemical substances"),
    ]
    sub, elem, reason = rng.choice(examples)

    prompt = (
        f"Consider the pure substance: **{sub}**.\n\n"
        f"1. Define what an **element** is in chemistry.\n"
        f"2. Explain why {elem} is classified as an element rather than a chemical compound."
    )
    sol = (
        f"**Step 1:** An element is a **pure substance that cannot be broken down (decomposed)** into simpler substances by any chemical methods [1 Mark: Definition].\n\n"
        f"**Step 2:** {reason} [1 Mark: Explanation]."
    )
    return {
        "id": f"ns7_pt_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Pure substance that cannot be broken down by chemical methods; {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "01_element_definition_pure_substance",
        "misconception_tags": ["element_definition"],
        "hints": {
            "tier_1": "Can an element be split into simpler chemicals?",
            "tier_2": "An element is the simplest pure chemical substance.",
            "tier_3": "Cannot be broken down chemically into simpler substances."
        }
    }


def arch_02_atom_as_building_block_of_element(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"All the countless materials in our world are built from microscopic building blocks.\n\n"
        f"1. Name the smallest indivisible particle of an element that retains the chemical identity of that element.\n"
        f"2. How many different kinds of atoms are present in a pure sample of an element (such as pure sulfur)?\n"
        f"3. Explain why atoms are described as the 'building blocks of all matter'."
    )
    sol = (
        f"**Step 1:** The smallest particle is an **atom** [1 Mark: Atom].\n\n"
        f"**Step 2:** A pure element contains **only ONE kind of atom** [1 Mark: Purity].\n\n"
        f"**Step 3:** Atoms combine together in endless combinations and ratios to construct every compound, molecule, and physical material in the universe [1 Mark: Building blocks concept]."
    )
    return {
        "id": f"ns7_pt_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Atom; only ONE kind of atom; all matter is composed of combinations of atoms",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "02_atom_as_building_block_of_element",
        "misconception_tags": ["atoms_and_elements"],
        "hints": {
            "tier_1": "Elements are made of atoms.",
            "tier_2": "An element has only one type of atom.",
            "tier_3": "Atom; only one kind; atoms combine to build all matter."
        }
    }


def arch_03_periodic_table_mendeleev_history(rng: random.Random) -> Dict[str, Any]:
    years = [1869, 1872]
    yr = rng.choice(years)

    prompt = (
        f"In the late 19th century (circa {yr}), a Russian chemist revolutionized how elements are organized.\n\n"
        f"1. Name the brilliant Russian scientist who created the first widely accepted Periodic Table: **Dmitri Mendeleev**.\n"
        f"2. Mendeleev left intentional blank gaps in his table. Explain why he left these gaps.\n"
        f"3. How was Mendeleev's table proven correct years later?"
    )
    sol = (
        f"**Step 1:** The scientist was **Dmitri Mendeleev** [1 Mark: Scientist].\n\n"
        f"**Step 2:** He predicted that **undiscovered elements** existed to fill those positions and match the chemical patterns of those groups [1 Mark: Gaps].\n\n"
        f"**Step 3:** When new elements (like gallium and germanium) were later discovered, their actual atomic weights and physical properties matched his predictions almost exactly [1 Mark: Proof]."
    )
    return {
        "id": f"ns7_pt_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Dmitri Mendeleev; left gaps for yet-undiscovered elements; newly discovered elements matched his predictions",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "03_periodic_table_mendeleev_history",
        "misconception_tags": ["mendeleev_periodic_table"],
        "hints": {
            "tier_1": "The Russian scientist was Mendeleev.",
            "tier_2": "He predicted undiscovered elements.",
            "tier_3": "Dmitri Mendeleev; gaps for undiscovered elements; predictions confirmed."
        }
    }


def arch_04_atomic_number_definition_protons(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Carbon", 6),
        ("Nitrogen", 7),
        ("Oxygen", 8),
        ("Sodium", 11),
        ("Magnesium", 12),
        ("Chlorine", 17),
    ]
    elem, z = rng.choice(elements)

    prompt = (
        f"On the modern Periodic Table, elements are arranged in strict order of increasing **atomic number**.\n\n"
        f"For example, the element **{elem}** has an atomic number of **{z}**.\n\n"
        f"1. Define what the **atomic number** ($Z$) of an element represents inside its atoms.\n"
        f"2. How many positively charged protons are in the nucleus of a single {elem} atom?\n"
        f"3. Can two different chemical elements ever share the exact same atomic number? Explain."
    )
    sol = (
        f"**Step 1:** The atomic number is the **number of protons** found in the nucleus of an atom of that element [1 Mark: Definition].\n\n"
        f"**Step 2:** A {elem} atom contains exactly **{z} protons** [1 Mark: Proton count].\n\n"
        f"**Step 3:** **No.** Every element has a unique number of protons; changing the proton number changes the element entirely [1 Mark: Uniqueness]."
    )
    return {
        "id": f"ns7_pt_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Number of protons in the nucleus; {z} protons; No, atomic number is unique to each element",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "04_atomic_number_definition_protons",
        "misconception_tags": ["atomic_number_protons"],
        "hints": {
            "tier_1": "Atomic number = number of protons in the nucleus.",
            "tier_2": f"Atomic number {z} means {z} protons.",
            "tier_3": f"Number of protons; {z}; No, each element has a unique atomic number."
        }
    }


def arch_05_chemical_symbol_capitalization_rules(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Cobalt (element Co)", "Carbon monoxide (gas CO)", "Co", "CO"),
        ("Silicon (element Si)", "Sulfur and Iodine compound (SI)", "Si", "SI"),
    ]
    elem_desc, comp_desc, sym_elem, sym_comp = rng.choice(pairs)

    prompt = (
        f"Chemical symbols follow strict international IUPAC capitalization rules.\n\n"
        f"A student accidentally writes **{sym_comp}** instead of **{sym_elem}**.\n\n"
        f"1. State the rule for writing chemical symbols that consist of two letters.\n"
        f"2. Contrast the meaning of **{sym_elem}** ({elem_desc}) with **{sym_comp}** ({comp_desc})."
    )
    sol = (
        f"**Step 1:** The first letter must ALWAYS be **capitalized (uppercase)** and the second letter must ALWAYS be **lowercase** [1 Mark: Rule].\n\n"
        f"**Step 2:** **{sym_elem}** represents a single chemical element ({elem_desc}), whereas **{sym_comp}** represents a compound containing two different elements [1 Mark: Distinction]."
    )
    return {
        "id": f"ns7_pt_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"First letter uppercase, second letter lowercase; {sym_elem} is one element whereas {sym_comp} is two elements",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "05_chemical_symbol_capitalization_rules",
        "misconception_tags": ["symbol_capitalization_rules"],
        "hints": {
            "tier_1": "First letter is capital, second letter is small.",
            "tier_2": "Two capital letters mean two different elements.",
            "tier_3": "First uppercase, second lowercase; Co is cobalt, CO is carbon monoxide."
        }
    }


def arch_06_latin_origin_symbols_iron_copper(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Iron", "Fe", "Ferrum"),
        ("Copper", "Cu", "Cuprum"),
    ]
    name, symbol, latin = rng.choice(metals)

    prompt = (
        f"The chemical symbol for **{name}** is **{symbol}**, which does not start with the letter '{name[0]}'.\n\n"
        f"1. State the ancient Latin name from which the symbol **{symbol}** is derived: **{latin}**.\n"
        f"2. Why do scientists worldwide use standard Latin-derived symbols rather than English or local language letters?"
    )
    sol = (
        f"**Step 1:** The Latin name is **{latin}** [1 Mark: Latin root].\n\n"
        f"**Step 2:** Chemical symbols provide a **universal international scientific language** understood by scientists of all countries and languages without confusion [1 Mark: Universal notation]."
    )
    return {
        "id": f"ns7_pt_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{latin}; provides universal international scientific communication across all languages",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "06_latin_origin_symbols_iron_copper",
        "misconception_tags": ["latin_element_symbols"],
        "hints": {
            "tier_1": f"Iron is Ferrum, Copper is Cuprum.",
            "tier_2": "Universal symbols allow scientists everywhere to communicate.",
            "tier_3": f"{latin}; universal language."
        }
    }


def arch_07_latin_origin_symbols_sodium_potassium(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Sodium", "Na", "Natrium"),
        ("Potassium", "K", "Kalium"),
    ]
    name, symbol, latin = rng.choice(metals)

    prompt = (
        f"The alkali metal **{name}** has the chemical symbol **{symbol}**.\n\n"
        f"1. Name the historical Latin or German word from which **{symbol}** originates: **{latin}**.\n"
        f"2. Write the chemical symbol for the other common alkali metal in this pair ({'Potassium (K)' if name == 'Sodium' else 'Sodium (Na)'})."
    )
    other_sym = "K" if name == "Sodium" else "Na"
    sol = (
        f"**Step 1:** The root word is **{latin}** [1 Mark: Root].\n\n"
        f"**Step 2:** The symbol is **{other_sym}** [1 Mark: Symbol]."
    )
    return {
        "id": f"ns7_pt_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{latin}; {other_sym}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "07_latin_origin_symbols_sodium_potassium",
        "misconception_tags": ["sodium_potassium_symbols"],
        "hints": {
            "tier_1": "Sodium is Na (Natrium), Potassium is K (Kalium).",
            "tier_2": f"{name} is {symbol} from {latin}.",
            "tier_3": f"{latin}; {other_sym}."
        }
    }


def arch_08_latin_origin_symbols_gold_silver_lead(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Gold", "Au", "Aurum (meaning 'shining dawn')"),
        ("Silver", "Ag", "Argentum"),
        ("Lead", "Pb", "Plumbum (origin of the word 'plumber')"),
    ]
    name, symbol, latin = rng.choice(metals)

    prompt = (
        f"Precious and heavy metals were known since antiquity:\n"
        f"Element: **{name}**.\n\n"
        f"1. State the correct chemical symbol for {name}: **{symbol}**.\n"
        f"2. Name the Latin word from which this symbol was taken: **{latin.split()[0]}**."
    )
    sol = (
        f"**Step 1:** The chemical symbol is **{symbol}** [1 Mark: Symbol].\n\n"
        f"**Step 2:** The Latin origin is **{latin.split()[0]}** ({latin}) [1 Mark: Latin root]."
    )
    return {
        "id": f"ns7_pt_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{symbol}; {latin.split()[0]}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "08_latin_origin_symbols_gold_silver_lead",
        "misconception_tags": ["gold_silver_lead_symbols"],
        "hints": {
            "tier_1": "Gold = Au, Silver = Ag, Lead = Pb.",
            "tier_2": f"{name} is {symbol}.",
            "tier_3": f"{symbol}; {latin.split()[0]}."
        }
    }


# ==============================================================================
# CLUSTER 2: The First 20 Elements (09 - 15)
# ==============================================================================

def arch_09_first_twenty_elements_names_symbols_1_5(rng: random.Random) -> Dict[str, Any]:
    group_1_5 = [
        (1, "Hydrogen", "H", "gas", "Non-metal"),
        (2, "Helium", "He", "gas", "Non-metal (noble gas)"),
        (3, "Lithium", "Li", "solid", "Metal (alkali metal)"),
        (4, "Beryllium", "Be", "solid", "Metal"),
        (5, "Boron", "B", "solid", "Semi-metal (metalloid)"),
    ]
    z, name, sym, state, cat = rng.choice(group_1_5)

    prompt = (
        f"In the first five elements of the Periodic Table:\n"
        f"Consider the element with **atomic number {z}**.\n\n"
        f"1. Name the element.\n"
        f"2. Write its chemical symbol.\n"
        f"3. Classify it as a metal, non-metal, or semi-metal ({cat})."
    )
    sol = (
        f"**Step 1:** Element name: **{name}** [1 Mark: Name].\n\n"
        f"**Step 2:** Chemical symbol: **{sym}** [1 Mark: Symbol].\n\n"
        f"**Step 3:** Classification: **{cat}** [1 Mark: Classification]."
    )
    return {
        "id": f"ns7_pt_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name}; {sym}; {cat}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "09_first_twenty_elements_names_symbols_1_5",
        "misconception_tags": ["first_five_elements"],
        "hints": {
            "tier_1": "1: H, 2: He, 3: Li, 4: Be, 5: B.",
            "tier_2": f"Atomic number {z} is {name} ({sym}).",
            "tier_3": f"{name}; {sym}; {cat}."
        }
    }


def arch_10_first_twenty_elements_names_symbols_6_10(rng: random.Random) -> Dict[str, Any]:
    group_6_10 = [
        (6, "Carbon", "C", "solid non-metal"),
        (7, "Nitrogen", "N", "gas non-metal"),
        (8, "Oxygen", "O", "gas non-metal"),
        (9, "Fluorine", "F", "gas non-metal / halogen"),
        (10, "Neon", "Ne", "noble gas non-metal"),
    ]
    z, name, sym, desc = rng.choice(group_6_10)

    prompt = (
        f"Among elements 6 through 10 of the Periodic Table:\n"
        f"Consider the element with **atomic number {z}** ({desc}).\n\n"
        f"1. Name this element.\n"
        f"2. State its chemical symbol.\n"
        f"3. How many protons are inside its atomic nucleus?"
    )
    sol = (
        f"**Step 1:** Name: **{name}** [1 Mark: Name].\n\n"
        f"**Step 2:** Symbol: **{sym}** [1 Mark: Symbol].\n\n"
        f"**Step 3:** The nucleus contains exactly **{z} protons** [1 Mark: Protons]."
    )
    return {
        "id": f"ns7_pt_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name}; {sym}; {z} protons",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "10_first_twenty_elements_names_symbols_6_10",
        "misconception_tags": ["elements_6_to_10"],
        "hints": {
            "tier_1": "6: C, 7: N, 8: O, 9: F, 10: Ne.",
            "tier_2": f"Atomic number {z} is {name}.",
            "tier_3": f"{name}; {sym}; {z} protons."
        }
    }


def arch_11_first_twenty_elements_names_symbols_11_15(rng: random.Random) -> Dict[str, Any]:
    group_11_15 = [
        (11, "Sodium", "Na", "Metal"),
        (12, "Magnesium", "Mg", "Metal"),
        (13, "Aluminium", "Al", "Metal"),
        (14, "Silicon", "Si", "Semi-metal (metalloid)"),
        (15, "Phosphorus", "P", "Non-metal"),
    ]
    z, name, sym, cat = rng.choice(group_11_15)

    prompt = (
        f"In Period 3 of the Periodic Table (elements 11 to 15):\n"
        f"Consider the element with **atomic number {z}**.\n\n"
        f"1. Identify the name of this element.\n"
        f"2. Write its chemical symbol.\n"
        f"3. Classify it as a metal, semi-metal, or non-metal."
    )
    sol = (
        f"**Step 1:** Element name: **{name}** [1 Mark: Name].\n\n"
        f"**Step 2:** Chemical symbol: **{sym}** [1 Mark: Symbol].\n\n"
        f"**Step 3:** Classification: **{cat}** [1 Mark: Classification]."
    )
    return {
        "id": f"ns7_pt_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name}; {sym}; {cat}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "11_first_twenty_elements_names_symbols_11_15",
        "misconception_tags": ["elements_11_to_15"],
        "hints": {
            "tier_1": "11: Na, 12: Mg, 13: Al, 14: Si, 15: P.",
            "tier_2": f"Atomic number {z} is {name} ({sym}).",
            "tier_3": f"{name}; {sym}; {cat}."
        }
    }


def arch_12_first_twenty_elements_names_symbols_16_20(rng: random.Random) -> Dict[str, Any]:
    group_16_20 = [
        (16, "Sulfur", "S", "Non-metal"),
        (17, "Chlorine", "Cl", "Non-metal (halogen)"),
        (18, "Argon", "Ar", "Non-metal (noble gas)"),
        (19, "Potassium", "K", "Metal (alkali metal)"),
        (20, "Calcium", "Ca", "Metal (alkaline earth metal)"),
    ]
    z, name, sym, cat = rng.choice(group_16_20)

    prompt = (
        f"Examine elements 16 through 20 on the Periodic Table:\n"
        f"Consider the element with **atomic number {z}**.\n\n"
        f"1. Name this element.\n"
        f"2. State its chemical symbol.\n"
        f"3. Classify it as a metal or non-metal."
    )
    sol = (
        f"**Step 1:** Name: **{name}** [1 Mark: Name].\n\n"
        f"**Step 2:** Symbol: **{sym}** [1 Mark: Symbol].\n\n"
        f"**Step 3:** Classification: **{cat}** [1 Mark: Category]."
    )
    return {
        "id": f"ns7_pt_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name}; {sym}; {cat}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "12_first_twenty_elements_names_symbols_16_20",
        "misconception_tags": ["elements_16_to_20"],
        "hints": {
            "tier_1": "16: S, 17: Cl, 18: Ar, 19: K, 20: Ca.",
            "tier_2": f"Atomic number {z} is {name} ({sym}).",
            "tier_3": f"{name}; {sym}; {cat}."
        }
    }


def arch_13_identifying_element_from_atomic_number(rng: random.Random) -> Dict[str, Any]:
    candidates = [
        (3, "Lithium", "Li", "Alkali Metal", 6.94),
        (6, "Carbon", "C", "Non-metal", 12.01),
        (8, "Oxygen", "O", "Non-metal", 16.00),
        (12, "Magnesium", "Mg", "Alkaline Earth Metal", 24.31),
        (13, "Aluminium", "Al", "Metal", 26.98),
        (17, "Chlorine", "Cl", "Halogen Non-metal", 35.45),
        (20, "Calcium", "Ca", "Metal", 40.08),
    ]
    z, name, sym, cat, mass = rng.choice(candidates)

    svg = (
        f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<rect x="25" y="25" width="150" height="150" fill="#f8fafc" stroke="#334155" stroke-width="3" rx="8"/>'
        f'<text x="40" y="55" font-family="sans-serif" font-size="16" font-weight="bold" fill="#64748b">{z}</text>'
        f'<text x="100" y="115" font-family="sans-serif" font-size="44" font-weight="bold" fill="#0f172a" text-anchor="middle">{sym}</text>'
        f'<text x="100" y="145" font-family="sans-serif" font-size="14" fill="#334155" text-anchor="middle">{name}</text>'
        f'<text x="100" y="165" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">{mass}</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"Periodic table tile for element {name} ({sym})",
        "diagram_role": "context"
    }

    prompt = (
        f"An element tile from the Periodic Table displays:\n"
        f"- Atomic number: **{z}**\n"
        f"- Symbol: **{sym}**\n\n"
        f"1. Name the element represented by this tile.\n"
        f"2. How many protons are present in each atom of this element?\n"
        f"3. State the group of elements to which it belongs ({cat})."
    )
    sol = (
        f"**Step 1:** The element is **{name}** [1 Mark: Name].\n\n"
        f"**Step 2:** It has **{z} protons** in its nucleus [1 Mark: Protons].\n\n"
        f"**Step 3:** It belongs to the **{cat}** category [1 Mark: Category]."
    )
    return {
        "id": f"ns7_pt_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name}; {z} protons; {cat}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "13_identifying_element_from_atomic_number",
        "misconception_tags": ["element_tile_reading"],
        "hints": {
            "tier_1": f"Symbol is {sym}, atomic number is {z}.",
            "tier_2": f"That element is {name}.",
            "tier_3": f"{name}; {z} protons; {cat}."
        }
    }


def arch_14_periods_definition_horizontal_rows(rng: random.Random) -> Dict[str, Any]:
    period_data = [
        (1, 2, "Hydrogen and Helium"),
        (2, 8, "Lithium to Neon"),
        (3, 8, "Sodium to Argon"),
    ]
    p_num, count, members = rng.choice(period_data)

    prompt = (
        f"On the Periodic Table, elements are arranged in rows and columns.\n\n"
        f"1. What is the scientific name given to the **horizontal rows** on the Periodic Table?\n"
        f"2. How many periods are there in total on the standard table?\n"
        f"3. How many elements are located in **Period {p_num}** ({members})?"
    )
    sol = (
        f"**Step 1:** The horizontal rows are called **periods** [1 Mark: Terminology].\n\n"
        f"**Step 2:** There are **7 periods** in total [1 Mark: Total periods].\n\n"
        f"**Step 3:** Period {p_num} contains exactly **{count} elements** ({members}) [1 Mark: Count]."
    )
    return {
        "id": f"ns7_pt_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Periods; 7 periods in total; {count} elements in Period {p_num}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "14_periods_definition_horizontal_rows",
        "misconception_tags": ["periods_vs_groups"],
        "hints": {
            "tier_1": "Horizontal rows are periods; vertical columns are groups.",
            "tier_2": f"There are 7 periods. Period {p_num} has {count} elements.",
            "tier_3": f"Periods; 7 periods; {count} elements."
        }
    }


def arch_15_groups_definition_vertical_columns(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Elements with similar chemical behaviours are organized into vertical columns.\n\n"
        f"1. What is the scientific name given to the **vertical columns** on the Periodic Table?\n"
        f"2. How many groups are there across the standard Periodic Table (1 to 18)?\n"
        f"3. Explain why elements in the exact same group behave similarly during chemical reactions."
    )
    sol = (
        f"**Step 1:** Vertical columns are called **groups** (or chemical families) [1 Mark: Terminology].\n\n"
        f"**Step 2:** There are **18 groups** in total [1 Mark: Number of groups].\n\n"
        f"**Step 3:** Elements in the same group have the **same number of outer (valence) electrons**, which governs their bonding and chemical reactivity [1 Mark: Chemical similarity]."
    )
    return {
        "id": f"ns7_pt_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Groups; 18 groups; same number of outer valence electrons",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "15_groups_definition_vertical_columns",
        "misconception_tags": ["groups_and_valence_electrons"],
        "hints": {
            "tier_1": "Vertical columns are groups (1 to 18).",
            "tier_2": "Elements in a group have the same number of outer electrons.",
            "tier_3": "Groups; 18; same number of valence electrons."
        }
    }


# ==============================================================================
# CLUSTER 3: Metals, Non-Metals & Semi-Metals (16 - 25)
# ==============================================================================

def arch_16_metals_position_on_periodic_table(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The elements are broadly classified into metals, non-metals, and semi-metals.\n\n"
        f"1. Where are the **metals** located on the Periodic Table (left side, right side, or along the zigzag line)?\n"
        f"2. Approximately what percentage of all known chemical elements are metals (about 75-80%, or 20%)?\n"
        f"3. Name the only metal element that is liquid at standard room temperature."
    )
    sol = (
        f"**Step 1:** Metals occupy the **left-hand side, centre, and bottom** of the Periodic Table [1 Mark: Position].\n\n"
        f"**Step 2:** Approximately **75% to 80%** (the vast majority) of all known elements are metals [1 Mark: Abundance].\n\n"
        f"**Step 3:** The only liquid metal is **mercury ($Hg$)** [1 Mark: Mercury]."
    )
    return {
        "id": f"ns7_pt_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Left side and centre; approximately 75-80%; Mercury (Hg)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "16_metals_position_on_periodic_table",
        "misconception_tags": ["metals_location_and_proportion"],
        "hints": {
            "tier_1": "Metals are on the left and middle; most elements are metals.",
            "tier_2": "The liquid metal is mercury.",
            "tier_3": "Left side and centre; ~75-80%; Mercury."
        }
    }


def arch_17_non_metals_position_on_periodic_table(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Non-metals make up the elements essential for organic life on Earth.\n\n"
        f"1. Where are the non-metals situated on the Periodic Table?\n"
        f"2. Name the single non-metal element located on the far top-left corner of the table.\n"
        f"3. Name the group of non-metals located on the far right column (Group 18)."
    )
    sol = (
        f"**Step 1:** Non-metals are situated on the **upper right-hand side** of the Periodic Table [1 Mark: Position].\n\n"
        f"**Step 2:** The exception on the top-left is **Hydrogen ($H$)** [1 Mark: Hydrogen].\n\n"
        f"**Step 3:** Group 18 consists of the **noble gases** (inert gases) [1 Mark: Noble gases]."
    )
    return {
        "id": f"ns7_pt_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Upper right side; Hydrogen (H); Noble gases (Group 18)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "17_non_metals_position_on_periodic_table",
        "misconception_tags": ["hydrogen_non_metal_position"],
        "hints": {
            "tier_1": "Non-metals are on the upper right, except Hydrogen on top left.",
            "tier_2": "Group 18 is the noble gases.",
            "tier_3": "Upper right; Hydrogen; Noble gases."
        }
    }


def arch_18_semi_metals_zigzag_border_elements(rng: random.Random) -> Dict[str, Any]:
    metalloids = [
        ("Boron (B)", "Silicon (Si)"),
        ("Silicon (Si)", "Germanium (Ge)"),
        ("Germanium (Ge)", "Arsenic (As)"),
    ]
    m1, m2 = rng.choice(metalloids)

    svg = (
        f'<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:6px;">'
        f'<rect x="20" y="20" width="110" height="130" fill="#bfdbfe" rx="4"/>'
        f'<text x="75" y="85" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">METALS</text>'
        f'<rect x="190" y="20" width="110" height="130" fill="#bbf7d0" rx="4"/>'
        f'<text x="245" y="85" font-family="sans-serif" font-size="13" font-weight="bold" fill="#065f46" text-anchor="middle">NON-METALS</text>'
        f'<path d="M 140,20 L 165,20 L 165,60 L 140,60 L 140,100 L 165,100 L 165,140 L 140,140 L 140,160" fill="none" stroke="#ef4444" stroke-width="3"/>'
        f'<rect x="135" y="65" width="50" height="20" rx="3" fill="#fef08a" stroke="#ca8a04"/>'
        f'<text x="160" y="79" font-family="sans-serif" font-size="9" font-weight="bold" fill="#854d0e" text-anchor="middle">{m1.split()[0]}</text>'
        f'<rect x="135" y="105" width="50" height="20" rx="3" fill="#fed7aa" stroke="#ea580c"/>'
        f'<text x="160" y="119" font-family="sans-serif" font-size="9" font-weight="bold" fill="#9a3412" text-anchor="middle">{m2.split()[0]}</text>'
        f'<text x="160" y="185" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">Semi-metals on border</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": "Zigzag staircase line dividing metals from non-metals",
        "diagram_role": "context"
    }

    prompt = (
        f"A distinct zigzag 'staircase' line runs through the p-block of the Periodic Table.\n\n"
        f"1. What is the special name given to the elements lying directly along this border line (**semi-metals** or **metalloids**)?\n"
        f"2. Name TWO specific semi-metal elements ({m1} and {m2}).\n"
        f"3. Explain why they are described as 'semi-metals'."
    )
    sol = (
        f"**Step 1:** They are called **semi-metals (or metalloids)** [1 Mark: Terminology].\n\n"
        f"**Step 2:** Two examples: **{m1}** and **{m2}** [1 Mark: Examples].\n\n"
        f"**Step 3:** They exhibit an intermediate blend of both metallic and non-metallic properties (e.g. they look shiny like metals but are brittle and act as electrical semiconductors) [1 Mark: Intermediate properties]."
    )
    return {
        "id": f"ns7_pt_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Semi-metals / metalloids; {m1} and {m2}; possess intermediate properties between metals and non-metals",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "18_semi_metals_zigzag_border_elements",
        "misconception_tags": ["metalloids_zigzag_border"],
        "hints": {
            "tier_1": "Elements on the zigzag line are semi-metals or metalloids.",
            "tier_2": "Silicon and Boron are semi-metals.",
            "tier_3": f"Semi-metals; {m1} and {m2}; have properties of both."
        }
    }


def arch_19_physical_properties_metals_lustre(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("pure copper pipe", "reddish-brown lustrous shine", "dull brown oxide coating"),
        ("aluminium foil", "bright silvery metallic shine", "dull grey oxide film"),
        ("silver cutlery", "brilliant white reflective lustre", "black tarnish patina"),
    ]
    item, shiny_desc, dull_desc = rng.choice(metals)

    prompt = (
        f"When freshly polished or scratched with emery paper, a {item} displays a distinctive shine.\n\n"
        f"1. What scientific term describes the shiny surface appearance of metals: **metallic lustre**.\n"
        f"2. Why do many metals gradually lose their lustre and become dull ({dull_desc}) when left exposed to air?\n"
        f"3. Contrast the lustre of metals with the appearance of non-metal solids like carbon charcoal or sulfur."
    )
    sol = (
        f"**Step 1:** The shine is called **metallic lustre** [1 Mark: Terminology].\n\n"
        f"**Step 2:** Metals react slowly with oxygen in the atmosphere to form a thin surface layer of metal oxide ({dull_desc}) that loses its reflective shine [1 Mark: Oxidation].\n\n"
        f"**Step 3:** Solid non-metals are **dull** and have no metallic lustre; they do not reflect light in a mirror-like shine [1 Mark: Contrast]."
    )
    return {
        "id": f"ns7_pt_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Metallic lustre; oxygen in air forms a dull surface oxide layer; non-metals are dull with no shine",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "19_physical_properties_metals_lustre",
        "misconception_tags": ["metallic_lustre_and_oxidation"],
        "hints": {
            "tier_1": "The shine of metals is called metallic lustre.",
            "tier_2": "Air oxidizes metals to form a dull coating. Non-metals are dull.",
            "tier_3": "Metallic lustre; surface oxidation; non-metals are dull."
        }
    }


def arch_20_physical_properties_metals_conduction(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Copper", "electrical transmission wiring and circuit board traces"),
        ("Aluminium", "overhead high-voltage power lines and cookware pots"),
        ("Silver", "ultra-high-precision electronics and delicate scientific contacts"),
    ]
    m_name, m_use = rng.choice(metals)

    prompt = (
        f"The element **{m_name}** is prized in technology for: '{m_use}'.\n\n"
        f"1. Name the TWO types of conduction for which metals are world-class performers:\n"
        f"   - Conduction of electricity.\n"
        f"   - Conduction of heat (thermal conduction).\n"
        f"2. Explain why metals conduct electricity so efficiently (free/delocalised electrons)."
    )
    sol = (
        f"**Step 1:** Metals excel at both **electrical conduction** and **thermal (heat) conduction** [1 Mark: Conduction types].\n\n"
        f"**Step 2:** Metals have a sea of **delocalised (free) valence electrons** that can move rapidly throughout the metallic crystal lattice carrying electric charge [1 Mark: Delocalised electrons]."
    )
    return {
        "id": f"ns7_pt_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Electrical conduction and thermal conduction; free/delocalised electrons move freely through metallic lattice",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "20_physical_properties_metals_conduction",
        "misconception_tags": ["metallic_conduction_free_electrons"],
        "hints": {
            "tier_1": "Metals conduct heat and electricity.",
            "tier_2": "They have free (delocalised) electrons.",
            "tier_3": "Electrical and thermal conduction; delocalised electrons carry charge."
        }
    }


def arch_21_physical_properties_metals_malleability(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A blacksmith hammers a red-hot bar of iron repeatedly with a heavy mallet, flattening it into a broad sheet.\n"
        f"In contrast, when a block of solid sulfur is struck with the same mallet, it shatters into powder.\n\n"
        f"1. Name the property of metals demonstrated by the hammered iron.\n"
        f"2. Name the opposing property demonstrated by the shattering sulfur.\n"
        f"3. Explain why layers of atoms in a metal can slide past each other without breaking the metallic bond."
    )
    sol = (
        f"**Step 1:** The property of iron is **malleability** [1 Mark: Malleability].\n\n"
        f"**Step 2:** The property of sulfur is **brittleness** [1 Mark: Brittleness].\n\n"
        f"**Step 3:** The sea of delocalised electrons is flexible and holds metal ions together even when atomic layers slide over one another under impact [1 Mark: Atomic explanation]."
    )
    return {
        "id": f"ns7_pt_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Malleability; Brittleness; flexible delocalised electron sea allows atomic layers to slide without breaking bonds",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "21_physical_properties_metals_malleability",
        "misconception_tags": ["malleability_vs_brittleness"],
        "hints": {
            "tier_1": "Metals bend/flatten (malleable); non-metals shatter (brittle).",
            "tier_2": "Electron sea allows layers to slide.",
            "tier_3": "Malleability; Brittleness; layers slide in electron sea."
        }
    }


def arch_22_physical_properties_metals_ductility(rng: random.Random) -> Dict[str, Any]:
    weights = [
        ("pure gold", 1, 2000),
        ("copper", 5, 500),
    ]
    elem, mass_g, length_m = rng.choice(weights)

    prompt = (
        f"A single gram of {elem} can be stretched into a wire over {length_m} metres long without snapping.\n\n"
        f"1. What is the specific term for the ability of a material to be pulled into long, thin wires: **ductility**.\n"
        f"2. Contrast ductility with malleability.\n"
        f"3. Name ONE non-metal solid and state whether it is ductile."
    )
    sol = (
        f"**Step 1:** The property is **ductility** [1 Mark: Definition].\n\n"
        f"**Step 2:** Ductility is the ability to be drawn into **wires**, whereas malleability is the ability to be hammered into **flat sheets** [1 Mark: Contrast].\n\n"
        f"**Step 3:** Non-metal: **Sulfur / Carbon / Phosphorus**; it is **NOT ductile** (brittle, snaps/crumbles immediately) [1 Mark: Non-metal property]."
    )
    return {
        "id": f"ns7_pt_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Ductility; ductility forms wires whereas malleability forms sheets; non-metals like sulfur are not ductile (brittle)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "22_physical_properties_metals_ductility",
        "misconception_tags": ["ductility_wires"],
        "hints": {
            "tier_1": "Ductility = wires. Malleability = sheets.",
            "tier_2": "Non-metals are brittle, not ductile.",
            "tier_3": "Ductility; wires vs sheets; non-metals are not ductile."
        }
    }


def arch_23_physical_properties_metals_melting_points(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Iron", 1538, "Sulfur", 115),
        ("Copper", 1085, "Phosphorus", 44),
        ("Aluminium", 660, "Oxygen", -218),
    ]
    m_name, m_mp, nm_name, nm_mp = rng.choice(metals)

    prompt = (
        f"Compare the melting points of two elements:\n"
        f"- Metal: {m_name} (melting point ${m_mp}^\\circ\\text{{C}}$)\n"
        f"- Non-metal: {nm_name} (melting point ${nm_mp}^\\circ\\text{{C}}$)\n\n"
        f"1. In general, how do the melting and boiling points of metals compare to those of non-metals?\n"
        f"2. Explain why metals have such high melting points (strong metallic bonds holding atoms together)."
    )
    sol = (
        f"**Step 1:** Metals generally have **much higher melting and boiling points** than non-metals [1 Mark: General comparison].\n\n"
        f"**Step 2:** Metals possess **strong metallic bonding** (strong electrostatic attractions between positive metal ions and the sea of delocalised electrons), requiring massive thermal energy to break apart [1 Mark: Bond strength]."
    )
    return {
        "id": f"ns7_pt_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Metals have much higher melting points than non-metals; strong metallic bonds require high thermal energy to break",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "23_physical_properties_metals_melting_points",
        "misconception_tags": ["metallic_melting_points"],
        "hints": {
            "tier_1": "Metals melt at very high temperatures.",
            "tier_2": "Strong metallic bonds hold metal atoms tightly.",
            "tier_3": "Metals have higher melting points; strong metallic bonds."
        }
    }


def arch_24_liquid_elements_mercury_and_bromine(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Out of more than 100 known elements on the Periodic Table, only TWO exist as liquids at standard room temperature ($25^\\circ\\text{{C}}$).\n\n"
        f"1. Name the only **metal** that is a liquid at room temperature.\n"
        f"2. Name the only **non-metal** that is a liquid at room temperature.\n"
        f"3. State the chemical symbol for each of these two elements."
    )
    sol = (
        f"**Step 1:** The liquid metal is **mercury** [1 Mark: Metal].\n\n"
        f"**Step 2:** The liquid non-metal is **bromine** [1 Mark: Non-metal].\n\n"
        f"**Step 3:** Chemical symbols: Mercury is **Hg**; Bromine is **Br** [1 Mark: Symbols]."
    )
    return {
        "id": f"ns7_pt_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Mercury (Hg) is the liquid metal; Bromine (Br) is the liquid non-metal",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "24_liquid_elements_mercury_and_bromine",
        "misconception_tags": ["two_liquid_elements"],
        "hints": {
            "tier_1": "Mercury is the silvery liquid metal. Bromine is the red-brown liquid non-metal.",
            "tier_2": "Symbols: Hg and Br.",
            "tier_3": "Mercury (Hg) and Bromine (Br)."
        }
    }


def arch_25_density_comparison_metals_vs_non_metals(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Lead (metal)", 11.3, "Sulfur (non-metal)", 2.0),
        ("Gold (metal)", 19.3, "Carbon/graphite (non-metal)", 2.2),
        ("Iron (metal)", 7.8, "Phosphorus (non-metal)", 1.8),
    ]
    m_name, m_d, nm_name, nm_d = rng.choice(pairs)

    prompt = (
        f"Compare the densities of two solid elements:\n"
        f"- {m_name}: density ${str(m_d).replace('.', ',')}\\text{{ g/cm}}^3$\n"
        f"- {nm_name}: density ${str(nm_d).replace('.', ',')}\\text{{ g/cm}}^3$\n\n"
        f"1. In general, how does the density of metals compare to the density of non-metals?\n"
        f"2. Explain this difference in terms of the packing of atoms inside the solid."
    )
    sol = (
        f"**Step 1:** Metals generally have **significantly higher densities** than non-metals [1 Mark: Density comparison].\n\n"
        f"**Step 2:** Metal atoms have heavier atomic masses and are packed together in tightly ordered, closely spaced crystalline lattices, giving more mass per unit volume [1 Mark: Atomic packing]."
    )
    return {
        "id": f"ns7_pt_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Metals have much higher densities; metal atoms are heavier and closely packed in tight crystal lattices",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "25_density_comparison_metals_vs_non_metals",
        "misconception_tags": ["metal_density_packing"],
        "hints": {
            "tier_1": "Metals feel much heavier for their size than non-metals.",
            "tier_2": "Metals have higher density because atoms are heavy and tightly packed.",
            "tier_3": "Metals have higher density; tightly packed heavy atoms."
        }
    }
