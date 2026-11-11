"""Grade 9 Natural Sciences - Compounds: Archetypes 26 to 50.
Grounded strictly in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 2/01. Compounds.md.

Covers:
- Nomenclature rules: Type 1 (Metal + Non-metal, -ide suffix)
- Nomenclature rules: Type 2 (Non-metal + Non-metal, Greek prefixes mono-, di-, tri-, tetra-)
- Common vs systematic names (water, ammonia, methane)
- Transition metals and Roman numerals (e.g. Iron(II) vs Iron(III))
- Subscripts, atom counting, combining ratios (valencies)
- Group combinations: Grp 1 + Grp 17 (1:1), Grp 2 + Grp 16 (1:1), Grp 2 + Grp 17 (1:2), Grp 1 + Grp 16 (2:1), Al2O3 (2:3)
- Polyatomic ions with brackets: Ca(OH)2, Al2(SO4)3, Mg(NO3)2
- Ball-and-stick molecular models and master synthesis challenge
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Binary Compound Nomenclature (26 - 34)
# ==============================================================================

def arch_26_naming_metal_and_nonmetal_compounds_ide_suffix(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        ("NaCl", "Sodium", "Chlorine", "Chloride", "Sodium chloride"),
        ("MgO", "Magnesium", "Oxygen", "Oxide", "Magnesium oxide"),
        ("CaS", "Calcium", "Sulfur", "Sulfide", "Calcium sulfide"),
        ("LiF", "Lithium", "Fluorine", "Fluoride", "Lithium fluoride"),
        ("KBr", "Potassium", "Bromine", "Bromide", "Potassium bromide"),
        ("ZnS", "Zinc", "Sulfur", "Sulfide", "Zinc sulfide"),
    ]
    form, metal, nm, mod_nm, full_name = rng.choice(compounds)

    prompt = (
        f"In Type 1 binary chemical nomenclature, compounds containing a metal and a non-metal follow strict naming rules.\n\n"
        f"Consider the chemical formula **{form}**:\n\n"
        f"1. State the general rule for naming the metal element in a metal + non-metal compound.\n"
        f"2. State how the name of the non-metal element ({nm}) changes its ending suffix.\n"
        f"3. Write the correct systematic chemical name for **{form}** ({full_name})."
    )
    sol = (
        f"**Step 1:** The metal element is written **first and its name remains completely unchanged** ({metal}) [1 Mark: Metal rule].\n\n"
        f"**Step 2:** The non-metal element is written second, and its ending is changed to the suffix **'-ide'** ({nm} $\\rightarrow$ **{mod_nm}**) [1 Mark: Non-metal suffix].\n\n"
        f"**Step 3:** The complete systematic name for {form} is **{full_name}** [1 Mark: Systematic name]."
    )
    return {
        "id": f"ns9_comp_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Metal name unchanged ({metal}); Non-metal suffix changes to '-ide' ({mod_nm}); Systematic name: {full_name}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "26_naming_metal_and_nonmetal_compounds_ide_suffix",
        "misconception_tags": ["metal_nonmetal_naming_rules"],
        "hints": {
            "tier_1": "Metal comes first and keeps its name. Non-metal ends in -ide.",
            "tier_2": f"{metal} + {nm} -> {full_name}.",
            "tier_3": f"Metal unchanged ({metal}); suffix '-ide' ({mod_nm}); {full_name}."
        }
    }


def arch_27_naming_metal_oxides_chlorides_and_sulfides(rng: random.Random) -> Dict[str, Any]:
    items = [
        ("Magnesium ribbon burning in oxygen gas", "Magnesium", "Oxygen", "MgO", "Magnesium oxide"),
        ("Calcium metal reacting with chlorine gas", "Calcium", "Chlorine", "CaCl2", "Calcium chloride"),
        ("Iron filings heated strongly with yellow sulfur", "Iron", "Sulfur", "FeS", "Iron sulfide"),
        ("Aluminum reacting with oxygen to form a protective coat", "Aluminum", "Oxygen", "Al2O3", "Aluminum oxide"),
        ("Lithium reacting with chlorine gas", "Lithium", "Chlorine", "LiCl", "Lithium chloride"),
    ]
    reaction, metal, nm, formula, sys_name = rng.choice(items)

    prompt = (
        f"A laboratory synthesis reaction is described:\n"
        f"*{reaction}*.\n\n"
        f"1. Identify the constituent metal and non-metal elements.\n"
        f"2. Write the correct systematic chemical name for the compound formed ({sys_name}).\n"
        f"3. Write the chemical formula for this compound ({formula})."
    )
    sol = (
        f"**Step 1:** Metal: **{metal}**; Non-metal: **{nm}** [1 Mark: Element identification].\n\n"
        f"**Step 2:** Systematic name: **{sys_name}** [1 Mark: Systematic name].\n\n"
        f"**Step 3:** Chemical formula: **{formula}** [1 Mark: Chemical formula]."
    )
    return {
        "id": f"ns9_comp_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Metal: {metal}, Non-metal: {nm}; Systematic name: {sys_name}; Formula: {formula}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "27_naming_metal_oxides_chlorides_and_sulfides",
        "misconception_tags": ["binary_metal_compound_naming"],
        "hints": {
            "tier_1": f"Combine {metal} and {nm} with an -ide ending.",
            "tier_2": f"Name is {sys_name}, formula is {formula}.",
            "tier_3": f"{metal}, {nm}; {sys_name}; {formula}."
        }
    }


def arch_28_naming_nonmetal_compounds_greek_prefixes_mono_di_tri(rng: random.Random) -> Dict[str, Any]:
    prefixes = [
        (1, "mono-", "CO", "Carbon monoxide"),
        (2, "di-", "CO2", "Carbon dioxide"),
        (3, "tri-", "SO3", "Sulfur trioxide"),
        (4, "tetra-", "CCl4", "Carbon tetrachloride"),
    ]
    n, prefix, ex_form, ex_name = rng.choice(prefixes)

    prompt = (
        f"In Type 2 binary nomenclature (compounds containing only non-metals), Greek prefixes indicate the number of atoms of each element.\n\n"
        f"1. List the Greek numerical prefixes for numbers 1, 2, 3, and 4.\n"
        f"2. What Greek prefix represents {n} atom(s) ({prefix})?\n"
        f"3. When is the prefix 'mono-' omitted from the first element's name (e.g. why do we write 'Carbon dioxide' and not 'Monocarbon dioxide')?"
    )
    sol = (
        f"**Step 1:** Greek prefixes: **1 = mono-**, **2 = di-**, **3 = tri-**, **4 = tetra-** [1 Mark: Prefixes 1-4].\n\n"
        f"**Step 2:** Prefix for {n}: **{prefix}** (as in {ex_form}, {ex_name}) [1 Mark: Specific prefix].\n\n"
        f"**Step 3:** The prefix 'mono-' is **never used on the first element** in a compound name by scientific convention; if there is only one atom of the first element, its plain name is written alone [1 Mark: Omission rule for first element]."
    )
    return {
        "id": f"ns9_comp_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"1=mono-, 2=di-, 3=tri-, 4=tetra-; Prefix for {n} is {prefix}; 'mono-' is omitted on the first element by convention",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "28_naming_nonmetal_compounds_greek_prefixes_mono_di_tri",
        "misconception_tags": ["greek_prefixes_binary_nomenclature"],
        "hints": {
            "tier_1": "mono=1, di=2, tri=3, tetra=4.",
            "tier_2": "Never put 'mono-' on the very first element.",
            "tier_3": f"mono, di, tri, tetra; {prefix}; 'mono-' is omitted on the first element."
        }
    }


def arch_29_carbon_and_oxygen_compounds_monoxide_vs_dioxide(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("CO", "Carbon monoxide", 1, 1, "toxic, colorless, odorless gas produced by incomplete combustion in limited oxygen", "binds irreversibly to hemoglobin in red blood cells causing suffocation"),
        ("CO2", "Carbon dioxide", 1, 2, "non-toxic, greenhouse gas produced by complete combustion and cellular respiration", "used by green plants for photosynthesis and turns clear limewater milky"),
    ]
    form, name, n_c, n_o, nature, role = rng.choice(cases)

    prompt = (
        f"Carbon and oxygen can chemically combine in different ratios to form different compounds.\n\n"
        f"Consider the gas **{form}**:\n\n"
        f"1. Write the systematic chemical name for **{form}** ({name}).\n"
        f"2. State the exact atomic ratio of carbon to oxygen atoms in {form}.\n"
        f"3. Explain why {name} ({form}) has radically different biological and chemical properties compared to other carbon-oxygen compounds ({role.split(' and ')[0]})."
    )
    sol = (
        f"**Step 1:** Systematic chemical name: **{name}** [1 Mark: Name].\n\n"
        f"**Step 2:** Atomic ratio: **{n_c} carbon atom to {n_o} oxygen atom{'s' if n_o > 1 else ''}** ($1 : {n_o}$) [1 Mark: Atomic ratio].\n\n"
        f"**Step 3:** The different ratio creates a **completely different molecule with different chemical bonds and structures**; {nature} ({role}) [1 Mark: Radical property difference]."
    )
    return {
        "id": f"ns9_comp_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{name}; 1 C : {n_o} O; Different combining ratio creates a completely different chemical structure with different biological effects ({role.split(' and ')[0]})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "29_carbon_and_oxygen_compounds_monoxide_vs_dioxide",
        "misconception_tags": ["carbon_monoxide_vs_dioxide_nomenclature"],
        "hints": {
            "tier_1": f"CO is carbon monoxide (1 O). CO2 is carbon dioxide (2 O).",
            "tier_2": f"Name is {name}, ratio is 1:{n_o}.",
            "tier_3": f"{name}; 1:{n_o}; different molecular structure and biological behavior."
        }
    }


def arch_30_sulfur_and_oxygen_compounds_dioxide_vs_trioxide(rng: random.Random) -> Dict[str, Any]:
    oxides = [
        ("SO2", "Sulfur dioxide", 1, 2, "a choking gas emitted by burning coal that reacts with moisture in air to form sulfurous acid ($H_2SO_3$)"),
        ("SO3", "Sulfur trioxide", 1, 3, "a dense gas that reacts vigorously with atmospheric water vapor to form strong sulfuric acid ($H_2SO_4$), causing acid rain"),
    ]
    form, name, n_s, n_o, env_impact = rng.choice(oxides)

    prompt = (
        f"Sulfur emissions from coal-fired power stations and mineral smelters react with oxygen to produce sulfur oxides.\n\n"
        f"Consider the chemical formula **{form}**:\n\n"
        f"1. Write the systematic chemical name for **{form}** using the correct Greek prefix.\n"
        f"2. How many sulfur atoms and how many oxygen atoms are present in one molecule of {form}?\n"
        f"3. Describe the environmental impact of {form} when it dissolves in atmospheric rain clouds."
    )
    sol = (
        f"**Step 1:** Systematic name: **{name}** [1 Mark: Name].\n\n"
        f"**Step 2:** Atoms per molecule: **{n_s} sulfur atom and {n_o} oxygen atoms** [1 Mark: Atom count].\n\n"
        f"**Step 3:** Environmental impact: {env_impact}, contributing to **acid rain** which damages soils, acidifies rivers/lakes, and corrodes buildings [1 Mark: Acid rain impact]."
    )
    return {
        "id": f"ns9_comp_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{name}; 1 sulfur atom and {n_o} oxygen atoms; Dissolves in clouds to form acid rain which damages ecosystems and structures",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "30_sulfur_and_oxygen_compounds_dioxide_vs_trioxide",
        "misconception_tags": ["sulfur_oxides_nomenclature_acid_rain"],
        "hints": {
            "tier_1": f"Prefix for {n_o} oxygens is {'di-' if n_o == 2 else 'tri-'}.",
            "tier_2": f"Name is {name}.",
            "tier_3": f"{name}; 1 S and {n_o} O; forms acid rain."
        }
    }


def arch_31_nitrogen_oxides_dinitrogen_monoxide_and_tetroxide(rng: random.Random) -> Dict[str, Any]:
    n_oxides = [
        ("N2O", "Dinitrogen monoxide", 2, 1, "laughing gas (anesthetic and motor racing oxidizer)"),
        ("NO2", "Nitrogen dioxide", 1, 2, "pungent brown toxic smog gas produced by vehicle exhaust"),
        ("N2O4", "Dinitrogen tetroxide", 2, 4, "colorless liquid used as a powerful rocket propellant oxidizer"),
    ]
    formula, name, n_n, n_o, application = rng.choice(n_oxides)

    prompt = (
        f"Nitrogen and oxygen form a diverse family of non-metal oxides ($NO_x$).\n\n"
        f"Consider the compound with chemical formula **{formula}**:\n\n"
        f"1. State the number of nitrogen atoms and oxygen atoms in a single molecule of {formula}.\n"
        f"2. Write down the systematic chemical name for **{formula}** ({name}).\n"
        f"3. Note a distinctive property or real-world application of this compound ({application.split(' (')[0]})."
    )
    sol = (
        f"**Step 1:** In {formula}: **{n_n} nitrogen atom{'s' if n_n > 1 else ''} and {n_o} oxygen atom{'s' if n_o > 1 else ''}** [1 Mark: Atom counts].\n\n"
        f"**Step 2:** Systematic name: **{name}** [1 Mark: Systematic name].\n\n"
        f"**Step 3:** Property/use: **{application}** [1 Mark: Real-world property]."
    )
    return {
        "id": f"ns9_comp_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{n_n} N atoms and {n_o} O atoms; {name}; {application}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "31_nitrogen_oxides_dinitrogen_monoxide_and_tetroxide",
        "misconception_tags": ["nitrogen_oxides_nomenclature"],
        "hints": {
            "tier_1": f"Subscripts tell you: {n_n} N and {n_o} O.",
            "tier_2": f"Prefixes: {name}.",
            "tier_3": f"{n_n} N and {n_o} O; {name}; {application}."
        }
    }


def arch_32_common_names_vs_systematic_names_water_ammonia_methane(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        ("Water", "Dihydrogen monoxide", "H2O", "essential liquid for all biological life", 2, 1),
        ("Ammonia", "Nitrogen trihydride", "NH3", "pungent household cleaning and agricultural fertilizer chemical", 1, 3),
        ("Methane", "Carbon tetrahydride", "CH4", "main component of natural gas fuel used for cooking and heating", 1, 4),
    ]
    common, systematic, formula, use, n1, n2 = rng.choice(compounds)

    prompt = (
        f"Certain chemical compounds are almost universally called by their traditional **common names** rather than their formal systematic chemical names.\n\n"
        f"Consider **{common}**:\n\n"
        f"1. Write its standard chemical formula ({formula}).\n"
        f"2. Write its formal systematic chemical name based on Greek numerical prefixes ({systematic}).\n"
        f"3. Explain why scientists and the general public continue to use traditional common names like '{common}' in everyday life."
    )
    sol = (
        f"**Step 1:** Chemical formula: **{formula}** [1 Mark: Formula].\n\n"
        f"**Step 2:** Systematic chemical name: **{systematic}** [1 Mark: Systematic name].\n\n"
        f"**Step 3:** Common names are retained because they are **deeply entrenched in history, simple, universally recognized, and convenient** across societies and industries [1 Mark: Common name justification]."
    )
    return {
        "id": f"ns9_comp_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{formula}; {systematic}; Historical familiarity, simplicity, and universal recognition in daily language and industry",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "32_common_names_vs_systematic_names_water_ammonia_methane",
        "misconception_tags": ["common_vs_systematic_names"],
        "hints": {
            "tier_1": f"Formula for {common} is {formula}.",
            "tier_2": f"Systematic name is {systematic}.",
            "tier_3": f"{formula}; {systematic}; convenience and historical familiarity."
        }
    }


def arch_33_halogens_group_17_compounds_with_metals(rng: random.Random) -> Dict[str, Any]:
    halides = [
        ("Sodium ($Na$)", "Chlorine ($Cl_2$)", "NaCl", "Sodium chloride", "table salt"),
        ("Potassium ($K$)", "Bromine ($Br_2$)", "KBr", "Potassium bromide", "photographic film and medicinal sedative"),
        ("Lithium ($Li$)", "Fluorine ($F_2$)", "LiF", "Lithium fluoride", "optical glass coatings"),
        ("Calcium ($Ca$)", "Chlorine ($Cl_2$)", "CaCl2", "Calcium chloride", "desiccant and road de-icer"),
    ]
    metal, halogen, formula, salt_name, use = rng.choice(halides)

    prompt = (
        f"The elements of **Group 17** are named the **Halogens**, a word derived from Greek meaning 'salt-formers'.\n\n"
        f"Consider the reaction between **{metal}** and **{halogen}**:\n\n"
        f"1. Why are Group 17 elements called 'salt-formers' (halogens)?\n"
        f"2. Write down the chemical formula of the salt formed ({formula}).\n"
        f"3. Name the salt formed ({salt_name}) and state its ending suffix."
    )
    sol = (
        f"**Step 1:** Halogens are called 'salt-formers' because they **readily react with metals to produce ionic salts** [1 Mark: Salt-former explanation].\n\n"
        f"**Step 2:** Chemical formula: **{formula}** [1 Mark: Formula].\n\n"
        f"**Step 3:** Name: **{salt_name}**; the suffix is **'-ide'** [1 Mark: Name and suffix]."
    )
    return {
        "id": f"ns9_comp_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Readily react with metals to produce salts; Formula: {formula}; Name: {salt_name} (suffix '-ide')",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "33_halogens_group_17_compounds_with_metals",
        "misconception_tags": ["halogen_salt_formation"],
        "hints": {
            "tier_1": "Halogen means salt-former. Halide salts end in -ide.",
            "tier_2": f"Salt is {salt_name} ({formula}).",
            "tier_3": f"React with metals to form salts; {formula}; {salt_name} ('-ide')."
        }
    }


def arch_34_transition_metal_compounds_iron_ii_vs_iron_iii(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Iron(II) oxide", "FeO", "+2", "Iron(III) oxide", "Fe2O3", "+3", "rust (reddish-brown solid)"),
        ("Copper(I) oxide", "Cu2O", "+1", "Copper(II) oxide", "CuO", "+2", "black solid used in pigments"),
        ("Iron(II) chloride", "FeCl2", "+2", "Iron(III) chloride", "FeCl3", "+3", "etching printed circuit boards"),
    ]
    name1, form1, val1, name2, form2, val2, app = rng.choice(pairs)

    prompt = (
        f"Certain transition metals can form more than one compound with the same non-metal.\n"
        f"Example: **{form1}** ({name1}) and **{form2}** ({name2}).\n\n"
        f"1. What do the Roman numerals (e.g. (II) or (III)) in a chemical name indicate?\n"
        f"2. State the valency (charge) of the metal in {name1} and in {name2}.\n"
        f"3. Explain why writing simply 'iron oxide' or 'copper oxide' without Roman numerals is ambiguous in scientific communication."
    )
    sol = (
        f"**Step 1:** The Roman numerals indicate the **valency or electrical charge (oxidation state)** of the transition metal ion in that specific compound [1 Mark: Roman numeral meaning].\n\n"
        f"**Step 2:** In {name1}: valency is **{val1}**; In {name2}: valency is **{val2}** [1 Mark: Valencies].\n\n"
        f"**Step 3:** It is ambiguous because the metal can form **two completely distinct chemical compounds with different ratios of atoms, formulas ({form1} vs {form2}), and chemical properties**; the Roman numeral specifies exactly which compound is meant [1 Mark: Ambiguity reason]."
    )
    return {
        "id": f"ns9_comp_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Roman numerals indicate the valency/charge of the metal ion; {val1} in {name1}, {val2} in {name2}; Ambiguous because multiple different compounds exist with different formulas ({form1} vs {form2})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "34_transition_metal_compounds_iron_ii_vs_iron_iii",
        "misconception_tags": ["roman_numerals_valency_transition_metals"],
        "hints": {
            "tier_1": "Roman numerals tell you the positive charge on the metal.",
            "tier_2": f"(II) means +2, (III) means +3.",
            "tier_3": f"Valency/charge of metal; {val1} and {val2}; ambiguous because {form1} and {form2} are different substances."
        }
    }


# ==============================================================================
# CLUSTER 5: Chemical Formula Derivation & Ratios (35 - 42)
# ==============================================================================

def arch_35_interpreting_subscripts_in_chemical_formulas(rng: random.Random) -> Dict[str, Any]:
    formulas = [
        ("H2O", "water", "2 hydrogen atoms and 1 oxygen atom", 2, "H", 1, "O"),
        ("CO2", "carbon dioxide", "1 carbon atom and 2 oxygen atoms", 1, "C", 2, "O"),
        ("NH3", "ammonia", "1 nitrogen atom and 3 hydrogen atoms", 1, "N", 3, "H"),
        ("CH4", "methane", "1 carbon atom and 4 hydrogen atoms", 1, "C", 4, "H"),
        ("Al2O3", "aluminum oxide", "2 aluminum atoms and 3 oxygen atoms", 2, "Al", 3, "O"),
    ]
    form, name, desc, n1, el1, n2, el2 = rng.choice(formulas)

    prompt = (
        f"A chemical formula contains element symbols and small subscript numbers.\n\n"
        f"Consider the chemical formula **{form}** ({name}):\n\n"
        f"1. What is the role of a **subscript number** written to the lower right of an element symbol?\n"
        f"2. When no subscript is written after an element symbol (such as {el1 if n1 == 1 else el2}), what number is implied?\n"
        f"3. Breakdown the exact atom counts indicated by the formula **{form}**."
    )
    sol = (
        f"**Step 1:** A subscript indicates the **exact number of atoms of that element** present in one molecule or formula unit of the compound [1 Mark: Subscript role].\n\n"
        f"**Step 2:** When no subscript is written, the number **1** is scientifically implied [1 Mark: Implied 1].\n\n"
        f"**Step 3:** Breakdown for {form}: **{desc}** [1 Mark: Breakdown]."
    )
    return {
        "id": f"ns9_comp_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Subscript indicates number of atoms of preceding element; Number 1 is implied when absent; Breakdown: {desc}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "35_interpreting_subscripts_in_chemical_formulas",
        "misconception_tags": ["subscript_interpretation_atom_counting"],
        "hints": {
            "tier_1": "Subscripts apply to the element immediately before them.",
            "tier_2": "No number means 1.",
            "tier_3": f"Tells number of atoms; number 1 is implied; {desc}."
        }
    }


def arch_36_counting_atoms_in_simple_molecular_formulas(rng: random.Random) -> Dict[str, Any]:
    molecules = [
        ("Glucose", "C6H12O6", 6, 12, 6, 24),
        ("Ethanol", "C2H6O", 2, 6, 1, 9),
        ("Sulfuric acid", "H2SO4", 2, 1, 4, 7),
        ("Nitric acid", "HNO3", 1, 1, 3, 5),
        ("Baking soda (sodium bicarbonate)", "NaHCO3", 1, 1, 1, 6),
    ]
    name, form, c1, c2, c3, total = rng.choice(molecules)

    prompt = (
        f"Consider the chemical formula for **{name}**: **{form}**.\n\n"
        f"1. How many different chemical elements make up this compound?\n"
        f"2. Count the number of atoms of each individual element present in one molecule/formula unit of {form}.\n"
        f"3. Calculate the total number of atoms combined in a single unit of {form} ({total})."
    )
    sol = (
        f"**Step 1:** There are **{'3' if len(form) > 5 else '3'} different elements** combined in this compound [1 Mark: Element count].\n\n"
        f"**Step 2:** Individual atom counts from subscripts: {form} contains **{c1}**, **{c2}**, and **{c3}** atoms [1 Mark: Individual counts].\n\n"
        f"**Step 3:** Total atoms = ${c1} + {c2} + {c3} =$ **{total} total atoms** [1 Mark: Total calculation]."
    )
    return {
        "id": f"ns9_comp_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"3 different elements; Individual atom counts: {c1}, {c2}, {c3}; Total = {total} atoms",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "36_counting_atoms_in_simple_molecular_formulas",
        "misconception_tags": ["atom_counting_in_formulas"],
        "hints": {
            "tier_1": f"Add the subscripts in {form}.",
            "tier_2": f"Counts: {c1} + {c2} + {c3} = {total}.",
            "tier_3": f"3 elements; {c1}, {c2}, {c3}; {total} total atoms."
        }
    }


def arch_37_combining_ratios_of_group_1_and_group_17_elements(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Sodium ($Na$)", 1, "+1", "Chlorine ($Cl$)", 7, "-1", "NaCl", "Sodium chloride"),
        ("Potassium ($K$)", 1, "+1", "Bromine ($Br$)", 7, "-1", "KBr", "Potassium bromide"),
        ("Lithium ($Li$)", 1, "+1", "Fluorine ($F$)", 7, "-1", "LiF", "Lithium fluoride"),
        ("Potassium ($K$)", 1, "+1", "Iodine ($I$)", 7, "-1", "KI", "Potassium iodide"),
    ]
    m_name, m_val, m_ch, nm_name, nm_val, nm_ch, form, full_name = rng.choice(pairs)

    prompt = (
        f"Group 1 alkali metals react with Group 17 halogens to form ionic salts.\n"
        f"Example: **{m_name}** reacting with **{nm_name}**.\n\n"
        f"1. What is the valency (combining power) of Group 1 metals ({m_ch}) and Group 17 halogens ({nm_ch})?\n"
        f"2. In what combining ratio do atoms of Group 1 and Group 17 combine?\n"
        f"3. Write the chemical formula ({form}) and name ({full_name}) of the compound formed."
    )
    sol = (
        f"**Step 1:** Group 1 metals have a valency of **1** (lose 1 electron to form ${m_ch}$ ions); Group 17 halogens have a valency of **1** (gain 1 electron to form ${nm_ch}$ ions) [1 Mark: Valencies].\n\n"
        f"**Step 2:** They combine in a **1 : 1 ratio** because one electron lost by the metal is accepted by one halogen atom [1 Mark: 1:1 ratio].\n\n"
        f"**Step 3:** Formula: **{form}**; Name: **{full_name}** [1 Mark: Formula and name]."
    )
    return {
        "id": f"ns9_comp_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Valencies are 1 ({m_ch}) and 1 ({nm_ch}); Combining ratio is 1:1; Formula: {form}, Name: {full_name}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "37_combining_ratios_of_group_1_and_group_17_elements",
        "misconception_tags": ["group1_group17_combining_ratio"],
        "hints": {
            "tier_1": "Group 1 loses 1 electron, Group 17 gains 1 electron -> 1:1 ratio.",
            "tier_2": f"Formula is {form}.",
            "tier_3": f"Valency 1 and 1; 1:1 ratio; {form} ({full_name})."
        }
    }


def arch_38_combining_ratios_of_group_2_and_group_16_elements(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Magnesium ($Mg$)", 2, "+2", "Oxygen ($O$)", 6, "-2", "MgO", "Magnesium oxide"),
        ("Calcium ($Ca$)", 2, "+2", "Oxygen ($O$)", 6, "-2", "CaO", "Calcium oxide (quicklime)"),
        ("Magnesium ($Mg$)", 2, "+2", "Sulfur ($S$)", 6, "-2", "MgS", "Magnesium sulfide"),
        ("Calcium ($Ca$)", 2, "+2", "Sulfur ($S$)", 6, "-2", "CaS", "Calcium sulfide"),
    ]
    m_name, m_val, m_ch, nm_name, nm_val, nm_ch, form, full_name = rng.choice(pairs)

    prompt = (
        f"Group 2 alkaline earth metals react with Group 16 non-metals (chalcogens).\n"
        f"Example: **{m_name}** reacting with **{nm_name}**.\n\n"
        f"1. What is the valency (combining power) of Group 2 metals ({m_ch}) and Group 16 non-metals ({nm_ch})?\n"
        f"2. Explain why they combine in a **1 : 1 atomic ratio** rather than a 2:2 ratio in their simplest chemical formula.\n"
        f"3. Write the correct chemical formula ({form}) and name ({full_name}) for this compound."
    )
    sol = (
        f"**Step 1:** Group 2 metals have valency **2** (lose 2 electrons, ${m_ch}$); Group 16 non-metals have valency **2** (gain 2 electrons, ${nm_ch}$) [1 Mark: Valencies].\n\n"
        f"**Step 2:** They combine in a **1 : 1 ratio** because the 2 electrons lost by one metal atom are exactly accepted by one non-metal atom; chemical formulas are always simplified to the lowest whole-number ratio (simplifying 2:2 to 1:1) [1 Mark: Simplest 1:1 ratio].\n\n"
        f"**Step 3:** Formula: **{form}**; Name: **{full_name}** [1 Mark: Formula and name]."
    )
    return {
        "id": f"ns9_comp_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Valencies are 2 ({m_ch}) and 2 ({nm_ch}); 1:1 ratio because 2 electrons transferred and formula is simplified to lowest terms; Formula: {form}, Name: {full_name}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "38_combining_ratios_of_group_2_and_group_16_elements",
        "misconception_tags": ["group2_group16_ratio_simplification"],
        "hints": {
            "tier_1": "+2 and -2 cancel out directly to give a 1:1 ratio.",
            "tier_2": f"Formula is {form}, not Mg2O2 or Ca2O2.",
            "tier_3": f"Valency 2 and 2; 1:1 ratio simplified; {form} ({full_name})."
        }
    }


def arch_39_combining_ratios_of_group_2_and_group_17_elements(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Magnesium ($Mg$)", "+2", "Chlorine ($Cl$)", "-1", "MgCl2", "Magnesium chloride"),
        ("Calcium ($Ca$)", "+2", "Chlorine ($Cl$)", "-1", "CaCl2", "Calcium chloride"),
        ("Magnesium ($Mg$)", "+2", "Bromine ($Br$)", "-1", "MgBr2", "Magnesium bromide"),
        ("Calcium ($Ca$)", "+2", "Fluorine ($F$)", "-1", "CaF2", "Calcium fluoride"),
    ]
    m_name, m_ch, nm_name, nm_ch, form, full_name = rng.choice(pairs)

    prompt = (
        f"Consider the reaction between a Group 2 metal ({m_name}) and a Group 17 halogen ({nm_name}).\n\n"
        f"1. State the charge on the metal ion ({m_ch}) and on the halide ion ({nm_ch}).\n"
        f"2. How many halogen atoms are required to balance the charge of one metal ion?\n"
        f"3. Write the correct chemical formula ({form}) and systematic name ({full_name}) of the compound."
    )
    sol = (
        f"**Step 1:** The metal forms a **{m_ch} ion**; each halogen forms a **{nm_ch} ion** [1 Mark: Ion charges].\n\n"
        f"**Step 2:** Exactly **two halogen atoms** are required to balance one metal ion ($1 \\times (+2) + 2 \\times (-1) = 0$), giving a **1 : 2 combining ratio** [1 Mark: 1:2 ratio explanation].\n\n"
        f"**Step 3:** Chemical formula: **{form}**; Name: **{full_name}** [1 Mark: Formula and name]."
    )
    return {
        "id": f"ns9_comp_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Metal is {m_ch}, Halide is {nm_ch}; Two halogen atoms needed (1:2 ratio); Formula: {form}, Name: {full_name}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "39_combining_ratios_of_group_2_and_group_17_elements",
        "misconception_tags": ["group2_group17_one_to_two_ratio"],
        "hints": {
            "tier_1": f"One +2 ion needs two -1 ions to balance to zero.",
            "tier_2": f"Formula is {form}.",
            "tier_3": f"{m_ch} and {nm_ch}; two halogen atoms; {form} ({full_name})."
        }
    }


def arch_40_combining_ratios_of_group_1_and_group_16_elements(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Sodium ($Na$)", "+1", "Oxygen ($O$)", "-2", "Na2O", "Sodium oxide"),
        ("Potassium ($K$)", "+1", "Oxygen ($O$)", "-2", "K2O", "Potassium oxide"),
        ("Lithium ($Li$)", "+1", "Oxygen ($O$)", "-2", "Li2O", "Lithium oxide"),
        ("Sodium ($Na$)", "+1", "Sulfur ($S$)", "-2", "Na2S", "Sodium sulfide"),
        ("Potassium ($K$)", "+1", "Sulfur ($S$)", "-2", "K2S", "Potassium sulfide"),
    ]
    m_name, m_ch, nm_name, nm_ch, form, full_name = rng.choice(pairs)

    prompt = (
        f"Consider the chemical reaction between a Group 1 metal ({m_name}) and a Group 16 non-metal ({nm_name}).\n\n"
        f"1. State the charge on the metal ion ({m_ch}) and on the non-metal ion ({nm_ch}).\n"
        f"2. How many Group 1 metal atoms are needed to combine with a single Group 16 atom to form an electrically neutral compound?\n"
        f"3. Write the chemical formula ({form}) and systematic name ({full_name}) for this compound."
    )
    sol = (
        f"**Step 1:** The metal ion has a charge of **{m_ch}**; the non-metal ion has a charge of **{nm_ch}** [1 Mark: Ion charges].\n\n"
        f"**Step 2:** Exactly **two metal atoms** are needed per non-metal atom ($2 \\times (+1) + 1 \\times (-2) = 0$), giving a **2 : 1 combining ratio** [1 Mark: 2:1 ratio].\n\n"
        f"**Step 3:** Chemical formula: **{form}**; Name: **{full_name}** [1 Mark: Formula and name]."
    )
    return {
        "id": f"ns9_comp_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Metal is {m_ch}, Non-metal is {nm_ch}; Two metal atoms needed (2:1 ratio); Formula: {form}, Name: {full_name}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "40_combining_ratios_of_group_1_and_group_16_elements",
        "misconception_tags": ["group1_group16_two_to_one_ratio"],
        "hints": {
            "tier_1": f"You need two +1 ions to balance one -2 ion.",
            "tier_2": f"Formula is {form}.",
            "tier_3": f"{m_ch} and {nm_ch}; two metal atoms; {form} ({full_name})."
        }
    }


def arch_41_aluminum_oxide_combining_ratio_two_to_three(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Aluminum metal ($Al$, Group 13) reacts with oxygen gas ($O_2$, Group 16) to form a tough protective ceramic coating of aluminum oxide.\n\n"
        "1. State the valency (charge) of an aluminum ion ($Al^{3+}$) and an oxide ion ($O^{2-}$).\n"
        "2. Using the lowest common multiple of the charges (6), explain why aluminum and oxygen combine in a **2 : 3 atomic ratio**.\n"
        "3. Write the correct chemical formula for aluminum oxide."
    )
    sol = (
        f"**Step 1:** Aluminum ion has a charge of **+3** ($Al^{{3+}}$); Oxide ion has a charge of **-2** ($O^{{2-}}$) [1 Mark: Ion charges].\n\n"
        f"**Step 2:** The lowest common multiple of 3 and 2 is 6. Two aluminum ions provide $+6$ ($2 \\times +3 = +6$), and three oxide ions provide $-6$ ($3 \\times -2 = -6$), achieving exact electrical neutrality [1 Mark: 2:3 ratio derivation].\n\n"
        f"**Step 3:** The correct chemical formula is **Al2O3** [1 Mark: Formula]."
    )
    return {
        "id": f"ns9_comp_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Al is +3, O is -2; LCM is 6: 2 Al(+3) = +6 and 3 O(-2) = -6 for neutrality (2:3 ratio); Formula is Al2O3",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "41_aluminum_oxide_combining_ratio_two_to_three",
        "misconception_tags": ["aluminum_oxide_valency_ratio"],
        "hints": {
            "tier_1": "Cross the valencies: Al valency 3 goes to O; O valency 2 goes to Al.",
            "tier_2": "Formula is Al2O3.",
            "tier_3": "+3 and -2; LCM is 6 (2 Al to 3 O); Al2O3."
        }
    }


def arch_42_formula_units_in_crystal_lattices_nacl_mgo(rng: random.Random) -> Dict[str, Any]:
    lattices = [
        ("Sodium chloride", "NaCl", "Na+", "Cl-", "1 : 1", 1, 1),
        ("Magnesium oxide", "MgO", "Mg2+", "O2-", "1 : 1", 1, 1),
        ("Calcium chloride", "CaCl2", "Ca2+", "Cl-", "1 : 2", 1, 2),
        ("Sodium oxide", "Na2O", "Na+", "O2-", "2 : 1", 2, 1),
    ]
    name, form, cat, an, ratio, n_c, n_a = rng.choice(lattices)

    prompt = (
        f"In solid ionic compounds like **{name}** (${form}$), atoms do not exist as independent molecules.\n\n"
        f"1. Explain what a **formula unit** means in solid-state chemistry.\n"
        f"2. In a macroscopic grain of {name} containing $1\\text{{ million}}$ {cat} ions, how many {an} ions are present in the crystal lattice?\n"
        f"3. Why is it technically incorrect to refer to 'a molecule of {name}'?"
    )
    n_other = f"{n_a} million" if n_c == 1 else f"{n_c} million"
    expected_an = f"{n_a} million"

    sol = (
        f"**Step 1:** A **formula unit** is the lowest whole-number ratio of ions represented in an ionic compound ($n({cat}) : n({an}) = {ratio}$) [1 Mark: Formula unit definition].\n\n"
        f"**Step 2:** Because the ratio is {ratio}, 1 million {cat} ions correspond to **{expected_an} {an} ions** in the crystal [1 Mark: Ion calculation].\n\n"
        f"**Step 3:** It is incorrect to say 'molecule' because {name} is a **continuous three-dimensional crystal lattice** with no separate, individual molecular boundaries [1 Mark: Lattice vs molecule distinction]."
    )
    return {
        "id": f"ns9_comp_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Formula unit = simplest ratio of ions in ionic crystal; {expected_an} {an} ions; Incorrect because it forms an infinite giant crystal lattice, not discrete molecules",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "42_formula_units_in_crystal_lattices_nacl_mgo",
        "misconception_tags": ["formula_unit_vs_molecule_concept"],
        "hints": {
            "tier_1": f"Ratio is {ratio}. Ionic compounds don't have separate molecules.",
            "tier_2": f"1 million {cat} means {expected_an} {an}.",
            "tier_3": f"Simplest whole-number ratio; {expected_an}; giant crystal lattice not separate molecules."
        }
    }


# ==============================================================================
# CLUSTER 6: Advanced Formulas, Polyatomic Ions & Master Synthesis (43 - 50)
# ==============================================================================

def arch_43_counting_atoms_with_brackets_hydroxide_compounds(rng: random.Random) -> Dict[str, Any]:
    hydroxides = [
        ("Calcium hydroxide", "Ca(OH)2", "slaked lime used in mortar and soil treatment", 1, 2, 2, 5),
        ("Magnesium hydroxide", "Mg(OH)2", "milk of magnesia antacid medicine", 1, 2, 2, 5),
        ("Barium hydroxide", "Ba(OH)2", "laboratory reagent", 1, 2, 2, 5),
    ]
    name, form, app, n_m, n_o, n_h, total = rng.choice(hydroxides)

    prompt = (
        f"Chemical formulas often use brackets when polyatomic groups appear more than once.\n"
        f"Consider **{name}**: **{form}** ({app}).\n\n"
        f"1. What does the subscript '2' outside the bracket $(OH)_2$ signify?\n"
        f"2. Count the number of atoms of each individual element in one formula unit of {form}:\n"
        f"   - Metal atoms:\n"
        f"   - Oxygen atoms:\n"
        f"   - Hydrogen atoms:\n"
        f"3. State the total number of atoms in a single formula unit of {form} ({total})."
    )
    sol = (
        f"**Step 1:** The subscript '2' multiplies **everything inside the brackets by 2** (meaning two complete hydroxide groups are present) [1 Mark: Bracket rule].\n\n"
        f"**Step 2:** Atom counts:\n"
        f"- Metal = **{n_m} atom**\n"
        f"- Oxygen = **{n_o} atoms** ($2 \\times 1$)\n"
        f"- Hydrogen = **{n_h} atoms** ($2 \\times 1$) [1 Mark: Subatomic counts].\n\n"
        f"**Step 3:** Total atoms = ${n_m} + {n_o} + {n_h} =$ **{total} total atoms** [1 Mark: Total count]."
    )
    return {
        "id": f"ns9_comp_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Subscript 2 doubles everything inside brackets; {n_m} metal, {n_o} oxygen, {n_h} hydrogen; Total = {total} atoms",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "43_counting_atoms_with_brackets_hydroxide_compounds",
        "misconception_tags": ["brackets_in_chemical_formulas"],
        "hints": {
            "tier_1": "Multiply every atom inside the brackets by the subscript outside.",
            "tier_2": f"O = {n_o}, H = {n_h}, total = {total}.",
            "tier_3": f"Multiplies inside by 2; {n_m} metal, {n_o} O, {n_h} H; {total} total atoms."
        }
    }


def arch_44_counting_atoms_with_brackets_nitrate_and_sulfate(rng: random.Random) -> Dict[str, Any]:
    complex_salts = [
        ("Magnesium nitrate", "Mg(NO3)2", 1, 2, 6, 9, "1 Mg, 2 N, 6 O"),
        ("Calcium nitrate", "Ca(NO3)2", 1, 2, 6, 9, "1 Ca, 2 N, 6 O"),
        ("Aluminum sulfate", "Al2(SO4)3", 2, 3, 12, 17, "2 Al, 3 S, 12 O"),
        ("Copper(II) nitrate", "Cu(NO3)2", 1, 2, 6, 9, "1 Cu, 2 N, 6 O"),
    ]
    name, form, n1, n2, n3, total, breakdown = rng.choice(complex_salts)

    prompt = (
        f"Consider the ionic compound **{name}**: **{form}**.\n\n"
        f"1. How many polyatomic groups are enclosed within the brackets?\n"
        f"2. Provide the exact atom counts for each individual element in one formula unit of {form}.\n"
        f"3. Calculate the total number of atoms in a single formula unit of {form} ({total})."
    )
    sol = (
        f"**Step 1:** There are **{form[-1]} polyatomic groups** (indicated by subscript {form[-1]} outside the brackets) [1 Mark: Bracket groups].\n\n"
        f"**Step 2:** Breakdown: **{breakdown}** [1 Mark: Breakdown].\n\n"
        f"**Step 3:** Total atoms = ${n1} + {n2} + {n3} =$ **{total} total atoms** [1 Mark: Total calculation]."
    )
    return {
        "id": f"ns9_comp_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{form[-1]} polyatomic groups; {breakdown}; Total = {total} atoms",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "44_counting_atoms_with_brackets_nitrate_and_sulfate",
        "misconception_tags": ["polyatomic_bracket_multiplication"],
        "hints": {
            "tier_1": f"For {form}: multiply subscripts inside by the outside subscript {form[-1]}.",
            "tier_2": f"Breakdown is {breakdown}.",
            "tier_3": f"{form[-1]} groups; {breakdown}; {total} total atoms."
        }
    }


def arch_45_chemical_formulas_from_element_valencies(rng: random.Random) -> Dict[str, Any]:
    valency_pairs = [
        ("Potassium ($K$, valency 1)", "Sulfur ($S$, valency 2)", "K2S", "Potassium sulfide"),
        ("Magnesium ($Mg$, valency 2)", "Nitrogen ($N$, valency 3)", "Mg3N2", "Magnesium nitride"),
        ("Aluminum ($Al$, valency 3)", "Chlorine ($Cl$, valency 1)", "AlCl3", "Aluminum chloride"),
        ("Calcium ($Ca$, valency 2)", "Oxygen ($O$, valency 2)", "CaO", "Calcium oxide"),
    ]
    elem1, elem2, form, full_name = rng.choice(valency_pairs)

    prompt = (
        f"Using valency rules (cross-over method), determine the chemical formula for the compound formed between:\n"
        f"- **{elem1}**\n"
        f"- **{elem2}**\n\n"
        f"1. Explain how the cross-over method is used with the valencies to find the subscripts.\n"
        f"2. Write down the correct chemical formula for the compound formed ({form}).\n"
        f"3. Write the systematic chemical name for this compound ({full_name})."
    )
    sol = (
        f"**Step 1:** In the cross-over method, the **valency of the first element becomes the subscript of the second element**, and the valency of the second element becomes the subscript of the first element, simplifying where possible [1 Mark: Cross-over method].\n\n"
        f"**Step 2:** Chemical formula: **{form}** [1 Mark: Chemical formula].\n\n"
        f"**Step 3:** Systematic name: **{full_name}** [1 Mark: Name]."
    )
    return {
        "id": f"ns9_comp_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Cross-over method exchanges valencies as subscripts; Formula: {form}; Systematic name: {full_name}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "45_chemical_formulas_from_element_valencies",
        "misconception_tags": ["valency_crossover_formula_derivation"],
        "hints": {
            "tier_1": "Swap the valencies to become subscripts, then simplify if needed.",
            "tier_2": f"Formula is {form}.",
            "tier_3": f"Cross-over method; {form}; {full_name}."
        }
    }


def arch_46_evaluating_molecular_models_ball_and_stick(rng: random.Random) -> Dict[str, Any]:
    models = [
        ("Water ($H_2O$)", 1, 2, "bent", "#ef4444", "#94a3b8", "one central oxygen atom (red) bonded to two hydrogen atoms (grey)"),
        ("Carbon dioxide ($CO_2$)", 1, 2, "linear", "#1e293b", "#ef4444", "one central carbon atom (black) double-bonded to two oxygen atoms (red)"),
        ("Methane ($CH_4$)", 1, 4, "tetrahedral", "#1e293b", "#94a3b8", "one central carbon atom (black) bonded to four hydrogen atoms (grey)"),
    ]
    name, n_central, n_outer, geom, c_cent, c_out, desc = rng.choice(models)
    uid = f"MOD-{rng.randint(100, 999)}"

    svg = (
        f'<svg viewBox="0 0 320 150" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="300" height="130" rx="6" fill="#f8fafc"/>'
        f'<text x="160" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Ball-and-Stick Model: {name.split(" (")[0]}</text>'
        f'<text x="295" y="25" font-family="sans-serif" font-size="8" fill="#94a3b8" text-anchor="end">{uid}</text>'
        # Central atom
        f'<line x1="160" y1="80" x2="110" y2="80" stroke="#64748b" stroke-width="4"/>'
        f'<line x1="160" y1="80" x2="210" y2="80" stroke="#64748b" stroke-width="4"/>'
        f'<circle cx="160" cy="80" r="16" fill="{c_cent}" stroke="#0f172a" stroke-width="1.5"/>'
        f'<circle cx="110" cy="80" r="12" fill="{c_out}" stroke="#0f172a" stroke-width="1.5"/>'
        f'<circle cx="210" cy="80" r="12" fill="{c_out}" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="160" y="125" font-family="sans-serif" font-size="9" fill="#475569" text-anchor="middle">Balls represent atoms; Sticks represent chemical bonds</text>'
        f'</svg>'
    )

    prompt = (
        f"Examine the 3D ball-and-stick molecular model diagram representing a molecule of **{name}**.\n\n"
        f"1. In a ball-and-stick model, what do the spheres (balls) represent, and what do the connecting rods (sticks) represent?\n"
        f"2. Based on the model, state the total number of atoms in this molecule.\n"
        f"3. State one strength and one limitation of using physical ball-and-stick models to represent chemical molecules."
    )
    total_atoms = n_central + n_outer

    sol = (
        f"**Step 1:** The spheres represent **atoms** of elements; the connecting sticks represent **chemical covalent bonds** [1 Mark: Model components].\n\n"
        f"**Step 2:** Total atoms = **{total_atoms} atoms** ({desc}) [1 Mark: Atom count].\n\n"
        f"**Step 3:** **Strength:** It gives an intuitive, clear 3D visualization of molecular geometry and bonding angles; **Limitation:** Atoms are not hard solid spheres, bonds are not rigid sticks, and relative scale/space-filling is inaccurate [1 Mark: Strength and limitation]."
    )
    return {
        "id": f"ns9_comp_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Balls = atoms, Sticks = chemical bonds; Total = {total_atoms} atoms; Strength = visualizes 3D shape/angles, Limitation = atoms are not rigid solid balls and scale is distorted",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "46_evaluating_molecular_models_ball_and_stick",
        "misconception_tags": ["ball_and_stick_model_evaluation"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Balls = atoms, rods = bonds.",
            "tier_2": f"Total atoms = {total_atoms}.",
            "tier_3": "Balls=atoms, sticks=bonds; total atoms; 3D visualization vs unrealistic rigid stick representation."
        }
    }


def arch_47_misconceptions_mixture_formula_vs_compound_formula(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A student writes in an exam that the chemical formula for air is '$N_{78}O_{21}Ar_1$' because air contains 78% nitrogen, 21% oxygen, and 1% argon.\n\n"
        f"1. Explain why writing a single chemical formula for air is scientifically incorrect.\n"
        f"2. What is the fundamental difference between the composition of a **mixture** (like air) and a **chemical compound**?\n"
        f"3. How should the composition of air be correctly represented scientifically?"
    )
    sol = (
        f"**Step 1:** Writing a chemical formula is incorrect because **chemical formulas are reserved exclusively for pure chemical compounds** whose atoms are joined by chemical bonds in fixed ratios; air is a physical mixture, not a compound [1 Mark: Formulas for compounds only].\n\n"
        f"**Step 2:** In a **compound**, elements are chemically bonded in fixed, unchanging ratios; in a **mixture**, independent substances are physically mingled in variable proportions without chemical bonds [1 Mark: Mixture vs compound composition].\n\n"
        f"**Step 3:** Air should be represented as a **mixture of separate chemical formulas**: $N_2$ ($78\\%$), $O_2$ ($21\\%$), $Ar$ ($1\\%$), and trace $CO_2$ [1 Mark: Correct scientific representation]."
    )
    return {
        "id": f"ns9_comp_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Formulas only represent pure compounds with chemical bonds, not mixtures; Compounds have fixed ratios and chemical bonds, mixtures have variable ratios and no bonds; Represented as separate formulas (N2, O2, Ar)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "47_misconceptions_mixture_formula_vs_compound_formula",
        "misconception_tags": ["mixture_cannot_have_chemical_formula"],
        "hints": {
            "tier_1": "Air is a mixture of separate gases, not a single bonded compound.",
            "tier_2": "Only pure chemical compounds have chemical formulas.",
            "tier_3": "Formulas are for pure compounds only; mixture vs compound; list gases separately (N2, O2, Ar)."
        }
    }


def arch_48_misconceptions_co_vs_co_cobalt_vs_carbon_monoxide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A student accidentally writes the symbol for the element cobalt as '**CO**' instead of '**Co**'.\n\n"
        f"1. What chemical substance does '**CO**' (with both letters capitalized) scientifically represent?\n"
        f"2. What chemical substance does '**Co**' (with lowercase 'o') represent?\n"
        f"3. Contrast the properties of these two substances (state of matter and classification as element vs compound) to demonstrate why strict capitalization rules are essential in chemistry."
    )
    sol = (
        f"**Step 1:** **CO** represents the chemical compound **carbon monoxide** (one carbon atom bonded to one oxygen atom) [1 Mark: Carbon monoxide].\n\n"
        f"**Step 2:** **Co** represents the metallic chemical **element cobalt** (Atomic Number 27) [1 Mark: Element cobalt].\n\n"
        f"**Step 3:** **Co** is a solid, shiny magnetic metallic element; **CO** is a colorless, odorless, highly toxic poisonous gas and a compound. Confusing them in medicine or industry could lead to lethal consequences [1 Mark: Property contrast & capitalization importance]."
    )
    return {
        "id": f"ns9_comp_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "CO = Carbon monoxide (toxic gas compound); Co = Cobalt (solid metal element); Co is a solid magnetic metal, CO is a deadly toxic gas; capitalization prevents dangerous errors",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "48_misconceptions_co_vs_co_cobalt_vs_carbon_monoxide",
        "misconception_tags": ["capitalization_rules_chemical_symbols"],
        "hints": {
            "tier_1": "Uppercase followed by lowercase = one element (Co = cobalt). Two uppercase = two elements (CO = carbon monoxide).",
            "tier_2": "Co is a metal. CO is a poisonous gas.",
            "tier_3": "CO is carbon monoxide compound; Co is cobalt element; solid metal vs toxic gas."
        }
    }


def arch_49_everyday_household_compounds_salt_baking_soda_vinegar(rng: random.Random) -> Dict[str, Any]:
    household = [
        ("Table salt", "NaCl", "Sodium chloride", "food seasoning and preservation"),
        ("Baking soda", "NaHCO3", "Sodium bicarbonate (sodium hydrogen carbonate)", "baking leavening agent and odor neutralizer"),
        ("Vinegar (active acid)", "CH3COOH", "Ethanoic acid (acetic acid)", "salad dressing and cleaning"),
        ("Rust", "Fe2O3", "Iron(III) oxide", "corrosion product on weathered iron roofs and gates"),
    ]
    common_name, formula, sys_name, everyday_use = rng.choice(household)

    prompt = (
        f"Chemical compounds are encountered constantly in everyday domestic life.\n"
        f"Consider the household substance **{common_name}**:\n\n"
        f"1. Write its standard chemical formula ({formula}).\n"
        f"2. Write its scientific systematic chemical name ({sys_name}).\n"
        f"3. State its common domestic application in the home ({everyday_use})."
    )
    sol = (
        f"**Step 1:** Chemical formula: **{formula}** [1 Mark: Formula].\n\n"
        f"**Step 2:** Systematic chemical name: **{sys_name}** [1 Mark: Systematic name].\n\n"
        f"**Step 3:** Domestic application: **{everyday_use}** [1 Mark: Domestic application]."
    )
    return {
        "id": f"ns9_comp_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Formula: {formula}; Systematic name: {sys_name}; Domestic application: {everyday_use}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "49_everyday_household_compounds_salt_baking_soda_vinegar",
        "misconception_tags": ["everyday_household_compounds"],
        "hints": {
            "tier_1": f"Chemical formula for {common_name} is {formula}.",
            "tier_2": f"Scientific name is {sys_name}.",
            "tier_3": f"{formula}; {sys_name}; {everyday_use}."
        }
    }


def arch_50_compounds_master_synthesis_and_classification_challenge(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Complete the comprehensive Grade 9 Natural Sciences Compounds master synthesis challenge:\n\n"
        "1. **Element vs Compound vs Mixture:** Classify each of the following: (a) Brass (copper + zinc), (b) Table sugar ($C_{12}H_{22}O_{11}$), and (c) Liquid bromine ($Br_2$).\n"
        "2. **Periodic Table Location:** Identify the Group number and Period number for Sodium ($Na$, $Z=11$).\n"
        "3. **Chemical Nomenclature:** Write the systematic chemical names for (a) $MgCl_2$ and (b) $SO_3$.\n"
        "4. **Formula Derivation:** Derive the chemical formula for the compound formed between Aluminum ($Al^{3+}$) and Oxygen ($O^{2-}$)."
    )
    sol = (
        "**Step 1:** Classifications:\n"
        "- (a) Brass is a **mixture (alloy)** of copper and zinc.\n"
        "- (b) Table sugar ($C_{12}H_{22}O_{11}$) is a **chemical compound**.\n"
        "- (c) Liquid bromine ($Br_2$) is a **diatomic element** [1 Mark: Classifications].\n\n"
        "**Step 2:** Sodium ($Na$, $Z=11$, electron arrangement 2, 8, 1) is in **Group 1** (1 valence electron) and **Period 3** (3 occupied energy levels) [1 Mark: Group 1, Period 3].\n\n"
        "**Step 3:** Systematic names:\n"
        "- (a) $MgCl_2$ = **Magnesium chloride** (metal + non-metal, -ide suffix).\n"
        "- (b) $SO_3$ = **Sulfur trioxide** (non-metal + non-metal, Greek prefix tri-) [1 Mark: Systematic names].\n\n"
        "**Step 4:** Using the cross-over of valencies: $Al$ has valency 3, $O$ has valency 2. The formula is **Al2O3** [1 Mark: Al2O3 formula]."
    )
    return {
        "id": f"ns9_comp_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Brass=mixture, Sugar=compound, Bromine=element; Sodium is Group 1, Period 3; MgCl2=Magnesium chloride, SO3=Sulfur trioxide; Aluminum oxide formula is Al2O3",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "term": 2,
        "subskill": "50_compounds_master_synthesis_and_classification_challenge",
        "misconception_tags": ["compounds_master_synthesis"],
        "hints": {
            "tier_1": "Alloys are mixtures. Br2 is diatomic element. Sodium has 3 shells (Period 3) and 1 valence electron (Group 1).",
            "tier_2": "MgCl2 = Magnesium chloride, SO3 = Sulfur trioxide. Al2O3.",
            "tier_3": "Brass=mixture, Sugar=compound, Br2=element; Grp 1, Per 3; Magnesium chloride, Sulfur trioxide; Al2O3."
        }
    }


# ==============================================================================
# DISPATCH DICT (26 - 50)
# ==============================================================================

BUILDERS_26_50 = {
    "26_naming_metal_and_nonmetal_compounds_ide_suffix": arch_26_naming_metal_and_nonmetal_compounds_ide_suffix,
    "27_naming_metal_oxides_chlorides_and_sulfides": arch_27_naming_metal_oxides_chlorides_and_sulfides,
    "28_naming_nonmetal_compounds_greek_prefixes_mono_di_tri": arch_28_naming_nonmetal_compounds_greek_prefixes_mono_di_tri,
    "29_carbon_and_oxygen_compounds_monoxide_vs_dioxide": arch_29_carbon_and_oxygen_compounds_monoxide_vs_dioxide,
    "30_sulfur_and_oxygen_compounds_dioxide_vs_trioxide": arch_30_sulfur_and_oxygen_compounds_dioxide_vs_trioxide,
    "31_nitrogen_oxides_dinitrogen_monoxide_and_tetroxide": arch_31_nitrogen_oxides_dinitrogen_monoxide_and_tetroxide,
    "32_common_names_vs_systematic_names_water_ammonia_methane": arch_32_common_names_vs_systematic_names_water_ammonia_methane,
    "33_halogens_group_17_compounds_with_metals": arch_33_halogens_group_17_compounds_with_metals,
    "34_transition_metal_compounds_iron_ii_vs_iron_iii": arch_34_transition_metal_compounds_iron_ii_vs_iron_iii,
    "35_interpreting_subscripts_in_chemical_formulas": arch_35_interpreting_subscripts_in_chemical_formulas,
    "36_counting_atoms_in_simple_molecular_formulas": arch_36_counting_atoms_in_simple_molecular_formulas,
    "37_combining_ratios_of_group_1_and_group_17_elements": arch_37_combining_ratios_of_group_1_and_group_17_elements,
    "38_combining_ratios_of_group_2_and_group_16_elements": arch_38_combining_ratios_of_group_2_and_group_16_elements,
    "39_combining_ratios_of_group_2_and_group_17_elements": arch_39_combining_ratios_of_group_2_and_group_17_elements,
    "40_combining_ratios_of_group_1_and_group_16_elements": arch_40_combining_ratios_of_group_1_and_group_16_elements,
    "41_aluminum_oxide_combining_ratio_two_to_three": arch_41_aluminum_oxide_combining_ratio_two_to_three,
    "42_formula_units_in_crystal_lattices_nacl_mgo": arch_42_formula_units_in_crystal_lattices_nacl_mgo,
    "43_counting_atoms_with_brackets_hydroxide_compounds": arch_43_counting_atoms_with_brackets_hydroxide_compounds,
    "44_counting_atoms_with_brackets_nitrate_and_sulfate": arch_44_counting_atoms_with_brackets_nitrate_and_sulfate,
    "45_chemical_formulas_from_element_valencies": arch_45_chemical_formulas_from_element_valencies,
    "46_evaluating_molecular_models_ball_and_stick": arch_46_evaluating_molecular_models_ball_and_stick,
    "47_misconceptions_mixture_formula_vs_compound_formula": arch_47_misconceptions_mixture_formula_vs_compound_formula,
    "48_misconceptions_co_vs_co_cobalt_vs_carbon_monoxide": arch_48_misconceptions_co_vs_co_cobalt_vs_carbon_monoxide,
    "49_everyday_household_compounds_salt_baking_soda_vinegar": arch_49_everyday_household_compounds_salt_baking_soda_vinegar,
    "50_compounds_master_synthesis_and_classification_challenge": arch_50_compounds_master_synthesis_and_classification_challenge,
}
