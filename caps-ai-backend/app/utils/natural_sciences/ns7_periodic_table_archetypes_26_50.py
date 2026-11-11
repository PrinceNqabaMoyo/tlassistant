"""
Grade 7 Natural Sciences - Term 2: The Periodic Table of Elements (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/04. The Periodic Table of Elements.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Non-metals & Semi-metals Properties (26 - 31)
# ==============================================================================

def arch_26_non_metals_physical_states_room_temp(rng: random.Random) -> Dict[str, Any]:
    states = [
        ("gas", "Oxygen, Nitrogen, Chlorine, Hydrogen, Helium", "particles have high kinetic energy with very weak intermolecular forces"),
        ("liquid", "Bromine (Br)", "it is the only non-metal element that is liquid at standard room temperature"),
        ("solid", "Carbon, Sulfur, Phosphorus, Iodine", "particles are packed in crystalline or macromolecular lattices"),
    ]
    target_state, examples, reason = rng.choice(states)

    prompt = (
        f"Unlike metals which are almost all solids at room temperature ($25^\\circ\\text{{C}}$), non-metals exist in all three states of matter.\n\n"
        f"1. Identify the state of matter (solid, liquid, or gas) represented by: **{examples}**.\n"
        f"2. State why non-metals exhibit this diversity of physical states compared to metals."
    )
    sol = (
        f"**Step 1:** These non-metals exist as **{target_state}** at room temperature ($25^\\circ\\text{{C}}$) [1 Mark: State identification].\n\n"
        f"**Step 2:** Non-metals have widely varying intermolecular forces and molecular sizes: {reason} [1 Mark: Reason]."
    )
    return {
        "id": f"ns7_pt_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{target_state.capitalize()}; {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "26_non_metals_physical_states_room_temp",
        "misconception_tags": ["non_metal_states_of_matter"],
        "hints": {
            "tier_1": f"Think about whether {examples.split(',')[0]} is a solid, liquid, or gas at room temperature.",
            "tier_2": f"Bromine is liquid; oxygen is gas; sulfur is solid.",
            "tier_3": f"State: {target_state}."
        }
    }


def arch_27_non_metals_dull_and_brittle_solids(rng: random.Random) -> Dict[str, Any]:
    solids = [
        ("Sulfur (S)", "bright yellow solid", "it lacks free delocalised electrons to reflect light, and when struck, like charges in the crystal lattice align and repel, causing it to shatter"),
        ("Carbon (charcoal/coal)", "black powdery solid", "it absorbs light rather than reflecting it (dull), and mechanical shock shatters the brittle atomic layers"),
        ("Phosphorus (red phosphorus)", "dark reddish-brown powder", "it does not have metallic lustre and fractures easily under mechanical pressure"),
    ]
    name, app, explanation = rng.choice(solids)

    prompt = (
        f"A laboratory sample of **{name}** is examined. It appears as a {app}.\n\n"
        f"1. Describe the visual appearance (lustre) of solid non-metals compared to metals.\n"
        f"2. Predict what happens when a piece of solid {name.split(' ')[0]} is struck with a hammer, and name this mechanical property."
    )
    sol = (
        f"**Step 1:** Solid non-metals are **dull** (lack lustre / do not have a shiny metallic shine) [1 Mark: Appearance].\n\n"
        f"**Step 2:** When struck with a hammer, it **shatters into small pieces/powder** because solid non-metals are **brittle** (they are not malleable) [1 Mark: Brittle property]."
    )
    return {
        "id": f"ns7_pt_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Dull appearance; shatters because it is brittle",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "27_non_metals_dull_and_brittle_solids",
        "misconception_tags": ["brittleness_non_metals"],
        "hints": {
            "tier_1": "Non-metals are the opposite of shiny and malleable.",
            "tier_2": "They look dull and shatter when hit because they are brittle.",
            "tier_3": "Dull appearance; shatters because it is brittle."
        }
    }


def arch_28_non_metals_electrical_insulators_exception_graphite(rng: random.Random) -> Dict[str, Any]:
    non_metals = [
        ("Sulfur", "Sulfur has no free mobile electrons to carry electric charge, acting as an electrical insulator"),
        ("Phosphorus", "Phosphorus electrons are all tightly held in covalent bonds, preventing current flow"),
        ("Chlorine gas", "Gas molecules have neutral charges and no free valence electrons to conduct charge"),
    ]
    nm, nm_exp = rng.choice(non_metals)

    prompt = (
        f"In an electrical circuit experiment, an educator tests the electrical conductivity of various non-metal substances.\n\n"
        f"1. In general, are non-metals good electrical conductors or electrical insulators? Explain why using {nm} as an example.\n"
        f"2. Name the famous exception: the form (allotrope) of carbon that DOES conduct electricity, and state where it is used in daily life."
    )
    sol = (
        f"**Step 1:** Non-metals are **electrical insulators** (poor electrical conductors) [1 Mark]. {nm_exp} [1 Mark: Explanation].\n\n"
        f"**Step 2:** The exception is **graphite** (a form of carbon) [1 Mark: Exception]. It is used in pencil leads or battery electrodes [1 Mark: Application]."
    )
    return {
        "id": f"ns7_pt_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Electrical insulators; graphite conducts electricity and is used in pencil leads / battery electrodes",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "term": 2,
        "subskill": "28_non_metals_electrical_insulators_exception_graphite",
        "misconception_tags": ["graphite_electrical_conduction"],
        "hints": {
            "tier_1": "Almost all non-metals are insulators, but pencil lead is special.",
            "tier_2": "Pencil lead is made of graphite (carbon), which conducts electricity.",
            "tier_3": "Insulators; exception: graphite (used in pencil leads/electrodes)."
        }
    }


def arch_29_carbon_allotropes_diamond_and_graphite(rng: random.Random) -> Dict[str, Any]:
    focus = rng.choice(["diamond", "graphite", "both"])
    prompt = (
        f"Both **diamond** and **graphite** are made of 100% pure carbon atoms, yet they have remarkably different physical properties.\n\n"
        f"1. Contrast the hardness of diamond with that of graphite.\n"
        f"2. State which of these two forms conducts electricity and explain why carbon can exist in these two radically different forms."
    )
    sol = (
        f"**Step 1:** Diamond is **extremely hard** (one of the hardest known natural substances), whereas graphite is **soft and slippery** [1 Mark: Hardness contrast].\n\n"
        f"**Step 2:** **Graphite** conducts electricity (due to delocalised electrons between its slippery hexagonal layers) while diamond is an insulator [1 Mark: Conductivity].\n\n"
        f"**Step 3:** They differ because their carbon atoms are arranged in completely different **crystal structures / bonding patterns** (allotropes) [1 Mark: Structural explanation]."
    )
    return {
        "id": f"ns7_pt_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Diamond is extremely hard; graphite is soft and conducts electricity; difference is due to atomic arrangement",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "29_carbon_allotropes_diamond_and_graphite",
        "misconception_tags": ["carbon_allotropes"],
        "hints": {
            "tier_1": "Diamond cuts glass; graphite rubs off easily on paper.",
            "tier_2": "Graphite conducts electricity; diamond does not. Their atoms are arranged differently.",
            "tier_3": "Diamond hard insulator; graphite soft conductor; arranged in different crystal structures."
        }
    }


def arch_30_semi_metals_semiconductor_properties(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Silicon (Si)", "Atomic number 14", "used in computer microchips and solar cells"),
        ("Boron (B)", "Atomic number 5", "used in heat-resistant borosilicate glassware and ceramics"),
        ("Germanium (Ge)", "Atomic number 32", "used in high-speed transistors and infrared optical systems"),
    ]
    elem, at_num, app = rng.choice(elements)

    prompt = (
        f"Consider the element **{elem}** ({at_num}), which lies directly on the border between metals and non-metals.\n\n"
        f"1. What is the special term used for elements that have properties intermediate between metals and non-metals?\n"
        f"2. Explain what a **semiconductor** is and how temperature affects its electrical conductivity."
    )
    sol = (
        f"**Step 1:** These elements are called **semi-metals** (or **metalloids**) [1 Mark: Term].\n\n"
        f"**Step 2:** A semiconductor is a material that conducts electricity **better than an insulator, but not as well as a true metal** [1 Mark: Definition].\n\n"
        f"**Step 3:** Unlike metals (whose conductivity decreases when heated), a semiconductor conducts electricity **better when its temperature increases** [1 Mark: Temperature effect]."
    )
    return {
        "id": f"ns7_pt_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Semi-metals (metalloids); semiconductor conducts moderately and conductivity increases with temperature",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "30_semi_metals_semiconductor_properties",
        "misconception_tags": ["semi_metal_semiconductor"],
        "hints": {
            "tier_1": "They sit along the zigzag line: semi-metals or metalloids.",
            "tier_2": "A semiconductor conducts electricity moderately well.",
            "tier_3": "Semi-metals (metalloids); semiconductor conductivity increases with heat."
        }
    }


def arch_31_silicon_in_modern_computer_technology(rng: random.Random) -> Dict[str, Any]:
    devices = [
        ("smartphones and laptop CPUs", "microprocessors containing billions of microscopic silicon transistors"),
        ("solar photovoltaic panels", "cells converting sunlight directly into clean electrical energy"),
        ("digital camera image sensors", "converting optical photons into electrical digital signals"),
    ]
    device, role = rng.choice(devices)

    prompt = (
        f"Silicon is the second most abundant element in the Earth's crust and is classified as a semi-metal.\n\n"
        f"1. Why is silicon the preferred material for manufacturing **{device}** ({role})?\n"
        f"2. Why could pure copper or pure sulfur NOT replace silicon in computer microchips?"
    )
    sol = (
        f"**Step 1:** Silicon is a **semiconductor** whose electrical conductivity can be precisely controlled and switched on/off by tiny voltage changes [1 Mark: Semiconductor control].\n\n"
        f"**Step 2:** Copper conducts electricity all the time (cannot be switched off to represent 1s and 0s) and sulfur is a complete insulator (never conducts), making neither suitable for electronic switches [1 Mark: Insulator vs Conductor contrast]."
    )
    return {
        "id": f"ns7_pt_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Silicon is a semiconductor whose conductivity can be precisely controlled; copper always conducts and sulfur never conducts",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "31_silicon_in_modern_computer_technology",
        "misconception_tags": ["silicon_in_electronics"],
        "hints": {
            "tier_1": "Computers need switches that can turn ON and OFF.",
            "tier_2": "Metals are always ON; insulators are always OFF. Semiconductors can be switched.",
            "tier_3": "Silicon can be controlled to switch on and off as a semiconductor."
        }
    }


# ==============================================================================
# CLUSTER 5: Key Element Groups & Periodic Patterns (32 - 37)
# ==============================================================================

def arch_32_group_1_alkali_metals_properties(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Lithium (Li)", 3, "#FF8A80", "floats on water, fizzes steadily producing hydrogen gas"),
        ("Sodium (Na)", 11, "#FFD54F", "melts into a silvery ball on water, dashes rapidly across surface with vigorous fizzing"),
        ("Potassium (K)", 19, "#CE93D8", "ignites instantly on water with a lilac-purple flame, producing crackling sparks"),
    ]
    elem, at_num, col, reaction = rng.choice(metals)

    svg = (
        f'<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border-radius:8px;border:1px solid #cbd5e1;">'
        f'<rect x="20" y="20" width="100" height="200" rx="6" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>'
        f'<text x="70" y="45" font-family="sans-serif" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">Group 1</text>'
        f'<rect x="30" y="60" width="80" height="45" rx="4" fill="{col}" stroke="#e11d48" stroke-width="2"/>'
        f'<text x="70" y="80" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">{elem.split()[0]}</text>'
        f'<text x="70" y="96" font-family="sans-serif" font-size="9" fill="#475569" text-anchor="middle">Z = {at_num}</text>'
        f'<rect x="150" y="30" width="230" height="180" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>'
        f'<text x="265" y="60" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Alkali Metal Storage</text>'
        f'<rect x="210" y="80" width="110" height="110" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
        f'<text x="265" y="115" font-family="sans-serif" font-size="10" fill="#92400e" text-anchor="middle">Liquid Paraffin</text>'
        f'<rect x="235" y="130" width="60" height="40" rx="4" fill="#94a3b8" stroke="#475569" stroke-width="1"/>'
        f'<text x="265" y="155" font-family="sans-serif" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">{elem.split()[0]}</text>'
        f'</svg>'
    )

    prompt = (
        f"The elements in Group 1 of the Periodic Table are known as the **alkali metals**. A sample of **{elem}** (atomic number {at_num}) is studied.\n\n"
        f"1. What unusual physical property do alkali metals have when cut with a scalpel or lab knife?\n"
        f"2. Why must alkali metals like {elem.split()[0]} be stored submerged under liquid paraffin oil rather than exposed in open air?"
    )
    sol = (
        f"**Step 1:** Alkali metals are **extremely soft** and can be easily cut with a butter knife or scalpel [1 Mark: Softness].\n\n"
        f"**Step 2:** They are **extremely reactive** and react vigorously with moisture (water vapour) and oxygen in the air; storing in paraffin oil prevents contact with air and moisture [1 Mark: Storage under oil]."
    )
    return {
        "id": f"ns7_pt_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Very soft (cut with knife); stored in oil because they react violently with moisture and oxygen in air",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "32_group_1_alkali_metals_properties",
        "misconception_tags": ["alkali_metals_softness_storage"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Can you cut these metals with a knife? What makes them react so easily?",
            "tier_2": "They are soft metals. They react rapidly with water and air.",
            "tier_3": "Soft enough to cut with a knife; stored in oil to prevent violent reaction with air and moisture."
        }
    }


def arch_33_group_1_alkali_metals_reactivity_trend(rng: random.Random) -> Dict[str, Any]:
    metals_order = [
        ("Lithium (Li)", "Sodium (Na)", "Potassium (K)"),
        ("Sodium (Na)", "Potassium (K)", "Rubidium (Rb)"),
    ]
    m1, m2, m3 = rng.choice(metals_order)

    prompt = (
        f"Consider the downward sequence of alkali metals in Group 1: **{m1}**, **{m2}**, and **{m3}**.\n\n"
        f"1. How does chemical reactivity change as you move **down** Group 1 from top to bottom?\n"
        f"2. When any of these metals is placed in a trough of water, what two products are formed? (Name the alkaline solution and the flammable gas)."
    )
    sol = (
        f"**Step 1:** Reactivity **increases** down Group 1 (potassium is more reactive than sodium, which is more reactive than lithium) [1 Mark: Reactivity trend].\n\n"
        f"**Step 2:** The reaction produces a **metal hydroxide solution** (alkaline, turns universal indicator purple) and **hydrogen gas** ($H_2$) [2 Marks: Products]."
    )
    return {
        "id": f"ns7_pt_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Reactivity increases down Group 1; products are metal hydroxide and hydrogen gas",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "33_group_1_alkali_metals_reactivity_trend",
        "misconception_tags": ["group_1_reactivity_trend"],
        "hints": {
            "tier_1": "Do they get more or less violent as you go down Group 1?",
            "tier_2": "Reactivity increases downwards. The gas produced burns with a 'pop' (hydrogen).",
            "tier_3": "Reactivity increases down Group 1; produces metal hydroxide and hydrogen gas."
        }
    }


def arch_34_group_2_alkaline_earth_metals(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Magnesium (Mg)", 12, "burns with an intense, blinding white flame to form magnesium oxide powder"),
        ("Calcium (Ca)", 20, "reacts steadily with cold water, producing bubbles of hydrogen and a cloudy white calcium hydroxide suspension"),
        ("Barium (Ba)", 56, "burns with an apple-green flame in fireworks and reacts vigorously with water"),
    ]
    elem, at_num, flame = rng.choice(metals)

    prompt = (
        f"Group 2 elements on the Periodic Table are called the **alkaline earth metals**. An example is **{elem}** (atomic number {at_num}).\n\n"
        f"1. Compare the hardness and reactivity of Group 2 alkaline earth metals to Group 1 alkali metals.\n"
        f"2. Describe the characteristic reaction observed when {elem.split()[0]} is tested ({flame.split(' to ')[0]})."
    )
    sol = (
        f"**Step 1:** Group 2 alkaline earth metals are **harder, denser, and slightly less reactive** than Group 1 alkali metals [1 Mark: Comparison].\n\n"
        f"**Step 2:** {flame} [1 Mark: Characteristic reaction]."
    )
    return {
        "id": f"ns7_pt_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Group 2 metals are harder and less reactive than Group 1; {flame}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "34_group_2_alkaline_earth_metals",
        "misconception_tags": ["alkaline_earth_metals"],
        "hints": {
            "tier_1": "Magnesium and calcium are Group 2 metals.",
            "tier_2": "They are harder than alkali metals and burn brightly.",
            "tier_3": f"Harder and less reactive than Group 1; {elem.split()[0]} {flame}."
        }
    }


def arch_35_group_17_halogens_properties(rng: random.Random) -> Dict[str, Any]:
    halogens = [
        ("Fluorine (F)", "pale yellow gas", "most reactive non-metal on the Periodic Table"),
        ("Chlorine (Cl)", "yellow-green gas", "used as a water disinfectant and bleach"),
        ("Bromine (Br)", "reddish-brown liquid", "readily vaporises into an orange pungent vapour"),
        ("Iodine (I)", "dark purple-black solid", "sublimes into a dense purple gas when gently heated"),
    ]
    elem, appearance, feature = rng.choice(halogens)

    prompt = (
        f"Group 17 (or Group 7) elements are known as the **halogens** (meaning 'salt-makers').\n\n"
        f"1. Describe the state and appearance of **{elem}** at room temperature.\n"
        f"2. Why are the halogens classified as non-metals, and what kind of substances do they readily form when reacted with metals?"
    )
    sol = (
        f"**Step 1:** {elem} exists as a **{appearance}** at standard room temperature [1 Mark: State/Appearance].\n\n"
        f"**Step 2:** Halogens are poor conductors of electricity and heat (non-metals) [1 Mark]. They react readily with metals to form **salts** (e.g. sodium chloride, $NaCl$) [1 Mark: Salt formation]."
    )
    return {
        "id": f"ns7_pt_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{appearance}; non-metals because poor conductors; react with metals to form salts",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "35_group_17_halogens_properties",
        "misconception_tags": ["halogens_salt_makers"],
        "hints": {
            "tier_1": f"Think about chlorine or iodine. What does {elem} look like?",
            "tier_2": "Halogens are non-metals that form salts with metals.",
            "tier_3": f"{elem} is a {appearance}; reacts with metals to form salts."
        }
    }


def arch_36_group_18_noble_gases_inert_nature(rng: random.Random) -> Dict[str, Any]:
    gases = [
        ("Helium (He)", 2, "2 electrons filling its only shell"),
        ("Neon (Ne)", 10, "8 electrons in its outer shell (octet)"),
        ("Argon (Ar)", 18, "8 electrons in its outer shell (octet)"),
        ("Krypton (Kr)", 36, "complete stable outer electron arrangement"),
    ]
    elem, at_num, electron_cfg = rng.choice(gases)

    prompt = (
        f"Group 18 elements on the far right of the Periodic Table are known as the **noble gases** (or inert gases). An example is **{elem}** (atomic number {at_num}).\n\n"
        f"1. What is meant by saying that noble gases are chemically **inert** (unreactive)?\n"
        f"2. Explain why {elem} does not readily bond or react with other chemical elements."
    )
    sol = (
        f"**Step 1:** Chemically inert means they **do not easily react or form chemical bonds** with other elements under normal conditions [1 Mark: Inert definition].\n\n"
        f"**Step 2:** {elem} has a **full, stable outer energy level (shell)** of electrons ({electron_cfg}), so it has no tendency to gain, lose, or share electrons [1 Mark: Full outer shell]."
    )
    return {
        "id": f"ns7_pt_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Inert means chemically unreactive; unreactive because they have full stable outer electron shells",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "36_group_18_noble_gases_inert_nature",
        "misconception_tags": ["noble_gases_inertness"],
        "hints": {
            "tier_1": "Why do noble gases not form compounds easily?",
            "tier_2": "They have full outer electron shells, making them completely stable.",
            "tier_3": "Inert = unreactive; unreactive due to full stable outer electron shells."
        }
    }


def arch_37_noble_gases_practical_applications(rng: random.Random) -> Dict[str, Any]:
    apps = [
        ("Helium (He)", "filling party balloons and weather blimps", "it is much less dense than air and, unlike hydrogen, is completely non-flammable and safe"),
        ("Neon (Ne)", "luminous glowing advertising signs", "it glows with an intense reddish-orange light when high voltage electricity passes through it"),
        ("Argon (Ar)", "filling traditional incandescent light bulbs", "it provides an unreactive inert shield that prevents the hot tungsten filament from burning up in oxygen"),
    ]
    elem, use, reason = rng.choice(apps)

    prompt = (
        f"The chemical inertness of noble gases makes them exceptionally valuable for practical industrial applications.\n\n"
        f"1. Identify the noble gas commonly used for: **{use}**.\n"
        f"2. Explain the scientific reason why this particular noble gas is chosen for this application ({reason.split(' and ')[0]})."
    )
    sol = (
        f"**Step 1:** The noble gas is **{elem}** [1 Mark: Noble gas identification].\n\n"
        f"**Step 2:** Reason: {reason} [1 Mark: Scientific justification]."
    )
    return {
        "id": f"ns7_pt_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{elem}; {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "37_noble_gases_practical_applications",
        "misconception_tags": ["noble_gas_uses"],
        "hints": {
            "tier_1": f"Which noble gas is used for {use}?",
            "tier_2": "Helium for balloons, Neon for signs, Argon for light bulbs.",
            "tier_3": f"{elem}: {reason}."
        }
    }


# ==============================================================================
# CLUSTER 6: Elements vs Compounds & Formulas (38 - 41)
# ==============================================================================

def arch_38_element_vs_compound_distinction(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Pure Oxygen gas ($O_2$)", "Carbon dioxide gas ($CO_2$)", "Oxygen is an element (only oxygen atoms); Carbon dioxide is a compound (carbon chemically bonded to oxygen)"),
        ("Pure Iron metal ($Fe$)", "Iron sulfide ($FeS$)", "Iron is an element (single type of atom); Iron sulfide is a compound formed by chemically bonding iron and sulfur"),
        ("Pure Hydrogen gas ($H_2$)", "Water ($H_2O$)", "Hydrogen is an element; Water is a compound of hydrogen and oxygen atoms in a fixed 2:1 ratio"),
    ]
    sub1, sub2, explanation = rng.choice(pairs)

    prompt = (
        f"Consider two chemical substances: **{sub1}** and **{sub2}**.\n\n"
        f"1. Classify each substance as either an **element** or a **compound**.\n"
        f"2. State the essential difference between an element and a compound in terms of the types of atoms they contain."
    )
    sol = (
        f"**Step 1:** {sub1} is an **element**; {sub2} is a **compound** [1 Mark: Classification].\n\n"
        f"**Step 2:** An element consists of **only one type of atom**, whereas a compound consists of **two or more different elements chemically bonded** in a fixed ratio [1 Mark: Atom difference]."
    )
    return {
        "id": f"ns7_pt_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{sub1} is an element, {sub2} is a compound; elements have one type of atom, compounds have two or more different elements bonded",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "38_element_vs_compound_distinction",
        "misconception_tags": ["element_vs_compound"],
        "hints": {
            "tier_1": "Does it have only one capital letter symbol or more than one?",
            "tier_2": "One type of atom = element; two or more different elements bonded = compound.",
            "tier_3": f"{sub1} is an element, {sub2} is a compound."
        }
    }


def arch_39_interpreting_chemical_formulas_atom_ratios(rng: random.Random) -> Dict[str, Any]:
    formulas = [
        ("H_2O", "Water", [("Hydrogen", 2), ("Oxygen", 1)], 3),
        ("CO_2", "Carbon dioxide", [("Carbon", 1), ("Oxygen", 2)], 3),
        ("NaCl", "Sodium chloride (table salt)", [("Sodium", 1), ("Chlorine", 1)], 2),
        ("CaCO_3", "Calcium carbonate (limestone)", [("Calcium", 1), ("Carbon", 1), ("Oxygen", 3)], 5),
        ("CH_4", "Methane (natural gas)", [("Carbon", 1), ("Hydrogen", 4)], 5),
    ]
    f_code, f_name, components, total_atoms = rng.choice(formulas)
    latex_f = f"${f_code}$"

    details = ", ".join([f"{num} {name} atom(s)" for name, num in components])

    prompt = (
        f"The chemical formula for **{f_name}** is written as **{latex_f}**.\n\n"
        f"1. How many different chemical elements make up this substance?\n"
        f"2. List each element present and state the number of atoms of that element in one molecule/unit of {f_name}.\n"
        f"3. What is the total number of atoms in one formula unit of {f_name}?"
    )
    sol = (
        f"**Step 1:** Number of different elements: **{len(components)}** [1 Mark: Element count].\n\n"
        f"**Step 2:** Atoms present: **{details}** [1 Mark: Breakdown].\n\n"
        f"**Step 3:** Total atoms = **{total_atoms}** atoms [1 Mark: Total count]."
    )
    return {
        "id": f"ns7_pt_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{len(components)} elements; {details}; Total = {total_atoms} atoms",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "39_interpreting_chemical_formulas_atom_ratios",
        "misconception_tags": ["chemical_formula_atom_counting"],
        "hints": {
            "tier_1": "Count capital letters for number of elements; count subscripts for atom numbers.",
            "tier_2": f"If no subscript is written, it means 1 atom of that element.",
            "tier_3": f"{len(components)} elements, {details}, total {total_atoms} atoms."
        }
    }


def arch_40_diatomic_non_metal_molecules(rng: random.Random) -> Dict[str, Any]:
    diatomics = [
        ("Oxygen", "O_2", "two oxygen atoms chemically bonded together"),
        ("Nitrogen", "N_2", "two nitrogen atoms strongly triple-bonded together"),
        ("Hydrogen", "H_2", "two hydrogen atoms sharing a pair of electrons"),
        ("Chlorine", "Cl_2", "two chlorine atoms bonded into a greenish toxic molecule"),
    ]
    elem, formula, desc = rng.choice(diatomics)

    prompt = (
        f"Certain non-metal elements never exist as isolated single atoms in nature under normal conditions, but instead form **diatomic molecules**.\n\n"
        f"1. Explain what the word **diatomic** means in chemistry.\n"
        f"2. Write the chemical formula for pure **{elem} gas** as it naturally occurs.\n"
        f"3. Name two other non-metal elements that also exist naturally as diatomic molecules."
    )
    sol = (
        f"**Step 1:** Diatomic means a molecule consisting of **two atoms of the same element chemically bonded together** [1 Mark: Diatomic definition].\n\n"
        f"**Step 2:** The formula for {elem} gas is **${formula}$** [1 Mark: Formula].\n\n"
        f"**Step 3:** Other diatomic elements include: Hydrogen ($H_2$), Nitrogen ($N_2$), Oxygen ($O_2$), Fluorine ($F_2$), Chlorine ($Cl_2$), Bromine ($Br_2$), or Iodine ($I_2$) [1 Mark: Other examples]."
    )
    return {
        "id": f"ns7_pt_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Diatomic = molecule of two bonded atoms; Formula: {formula}; Examples: N2, H2, O2, Cl2",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "40_diatomic_non_metal_molecules",
        "misconception_tags": ["diatomic_molecules"],
        "hints": {
            "tier_1": "Di means two. Diatomic = two atoms.",
            "tier_2": f"Formula for {elem} gas has a subscript 2.",
            "tier_3": f"Diatomic = two bonded atoms; ${formula}$; examples: $O_2, N_2, H_2, Cl_2$."
        }
    }


def arch_41_gaseous_elements_at_room_temperature(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Out of the first 20 elements on the Periodic Table, several exist as **gases** at room temperature ($25^\\circ\\text{{C}}$).\n\n"
        f"1. Identify how many elements in total exist as gases at room temperature across the entire Periodic Table (approximately 11 elements).\n"
        f"2. Name any **three** gaseous elements from the first 20 elements, stating their chemical symbols.\n"
        f"3. To which chemical family/group do the gaseous elements on the far right column (Column 18) belong?"
    )
    sol = (
        f"**Step 1:** There are **11 elements** that exist as gases at room temperature [1 Mark: Total count].\n\n"
        f"**Step 2:** Any three from: Hydrogen (H), Helium (He), Nitrogen (N), Oxygen (O), Fluorine (F), Neon (Ne), Chlorine (Cl), Argon (Ar) [1 Mark: Three gaseous elements].\n\n"
        f"**Step 3:** Group 18 gaseous elements are called the **noble gases** (inert gases) [1 Mark: Noble gases]."
    )
    return {
        "id": f"ns7_pt_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "11 gaseous elements; examples: H, He, N, O, F, Ne, Cl, Ar; Group 18 are noble gases",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "41_gaseous_elements_at_room_temperature",
        "misconception_tags": ["gaseous_elements_periodic_table"],
        "hints": {
            "tier_1": "Think of gases you breathe: oxygen, nitrogen, and party balloon gas: helium.",
            "tier_2": "There are 11 gases in total on the Periodic Table.",
            "tier_3": "11 elements; H, He, N, O, F, Ne, Cl, Ar; noble gases."
        }
    }


# ==============================================================================
# CLUSTER 7: Real-world Abundance & Metallurgy (42 - 45)
# ==============================================================================

def arch_42_mineral_ores_and_indigenous_metal_smelting(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Iron (Fe)", "hematite or magnetite ores", "smelted in clay furnaces using charcoal fuel and air bellows to make hoe blades, spears, and axes"),
        ("Copper (Cu)", "malachite ore", "melted and cast into ingots, bangles, and trade wire"),
        ("Gold (Au)", "alluvial gold dust in rivers", "hammered and crafted into exquisite ornamental treasures like the Golden Rhinoceros of Mapungubwe"),
    ]
    metal, ore, heritage = rng.choice(metals)

    prompt = (
        f"Long before modern industrial mining, indigenous African societies across Southern Africa had developed sophisticated metallurgical technologies.\n\n"
        f"1. Distinguish between a **native metal** found pure in nature and a **mineral ore**.\n"
        f"2. Explain how ancient metalworkers in Southern Africa processed **{metal.split(' ')[0]}** ({ore}) to produce functional or cultural items ({heritage.split(' to ')[0]})."
    )
    sol = (
        f"**Step 1:** A native metal (like gold) occurs uncombined in pure elemental form; a **mineral ore** is a natural rock or mineral containing a metal compound mixed with rock, from which the pure metal must be chemically extracted [1 Mark: Distinction].\n\n"
        f"**Step 2:** Indigenous metalworkers heated the ore with **charcoal** in specialized clay furnaces, pumping air with leather bellows to reach extreme temperatures (smelting) to chemically reduce and separate the pure molten {metal.split(' ')[0]} [1 Mark: Smelting process]."
    )
    return {
        "id": f"ns7_pt_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Native metal is pure; mineral ore is a compound in rock; indigenous smelting used clay furnaces, charcoal, and bellows to extract {metal.split(' ')[0]}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "42_mineral_ores_and_indigenous_metal_smelting",
        "misconception_tags": ["mineral_ores_smelting_heritage"],
        "hints": {
            "tier_1": "Most metals are trapped in rocks called ores and must be smelted.",
            "tier_2": "African metallurgists used clay bloomery furnaces, charcoal, and bellows.",
            "tier_3": "Native metal is uncombined; ore requires smelting with charcoal in clay furnaces."
        }
    }


def arch_43_abundance_of_elements_in_earth_crust(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Oxygen (O)", 46.6, "non-metal", "forms silicate and oxide rocks like quartz ($SiO_2$)"),
        ("Silicon (Si)", 27.7, "semi-metal", "forms the backbone of silica, granite, and clay minerals"),
        ("Aluminium (Al)", 8.1, "metal", "the most abundant metal in the crust, found in bauxite ore"),
        ("Iron (Fe)", 5.0, "metal", "second most abundant metal, forming abundant reddish hematite minerals"),
    ]
    elem, pct, category, role = rng.choice(elements)

    prompt = (
        f"The Earth's crust is composed of many chemical elements, but just two elements make up nearly $75\\%$ of its total mass.\n\n"
        f"1. Name the single most abundant element in the Earth's crust by mass, and state whether it is a metal, non-metal, or semi-metal.\n"
        f"2. Name the most abundant **metal** in the Earth's crust.\n"
        f"3. Explain why {elem} ({pct}\\%) is so abundant in crustal rocks ({role})."
    )
    sol = (
        f"**Step 1:** The most abundant element in the Earth's crust is **Oxygen** ($~46,6\\%$), which is a **non-metal** [1 Mark: Most abundant element].\n\n"
        f"**Step 2:** The most abundant **metal** in the crust is **Aluminium** ($~8,1\\%$) [1 Mark: Most abundant metal].\n\n"
        f"**Step 3:** {elem} binds readily with other elements: {role} [1 Mark: Geological role]."
    )
    return {
        "id": f"ns7_pt_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Oxygen is most abundant element (non-metal); Aluminium is most abundant metal; {elem} {role}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "43_abundance_of_elements_in_earth_crust",
        "misconception_tags": ["earth_crust_element_abundance"],
        "hints": {
            "tier_1": "What gas combines with silicon to form sand and rocks?",
            "tier_2": "Oxygen is #1; Silicon is #2; Aluminium is the #1 metal.",
            "tier_3": "Oxygen is most abundant (non-metal); Aluminium is most abundant metal."
        }
    }


def arch_44_abundance_of_elements_in_human_body(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Oxygen (O)", 65, "water ($H_2O$) makes up about $60-70\\%$ of human body mass"),
        ("Carbon (C)", 18, "forms the organic molecular backbone of proteins, fats, carbohydrates, and DNA"),
        ("Hydrogen (H)", 10, "present in every water molecule and all organic biomolecules"),
        ("Nitrogen (N)", 3, "essential constituent of amino acids, proteins, and genetic nucleic acids"),
    ]
    elem, pct, role = rng.choice(elements)

    prompt = (
        f"Over $96\\%$ of the human body's mass is made up of just four primary chemical elements (often remembered by the acronym CHON).\n\n"
        f"1. Name the four primary elements represented by **C-H-O-N**.\n"
        f"2. Which of these four elements makes up the highest percentage of body mass (approx. $65\\%$)? Explain why ({role})."
    )
    sol = (
        f"**Step 1:** The four elements are **Carbon**, **Hydrogen**, **Oxygen**, and **Nitrogen** [1 Mark: Four CHON elements].\n\n"
        f"**Step 2:** **Oxygen** makes up the largest percentage (~65%) because human bodies consist mainly of **water ($H_2O$)**, and oxygen atom mass dominates each water molecule [1 Mark: Oxygen explanation]."
    )
    return {
        "id": f"ns7_pt_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Carbon, Hydrogen, Oxygen, Nitrogen; Oxygen is highest (~65%) because our bodies are mostly water (H2O)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "44_abundance_of_elements_in_human_body",
        "misconception_tags": ["human_body_element_composition"],
        "hints": {
            "tier_1": "CHON: C for Carbon, H for Hydrogen, O for Oxygen, N for Nitrogen.",
            "tier_2": "Our bodies are 65% water, which is mostly oxygen by mass.",
            "tier_3": "Carbon, Hydrogen, Oxygen, Nitrogen; Oxygen is highest due to body water content."
        }
    }


def arch_45_transition_metals_overview(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Iron (Fe)", "structural steel in skyscrapers and bridges", "high tensile strength and magnetic properties"),
        ("Copper (Cu)", "electrical wiring and water pipes", "exceptional electrical and thermal conductivity and corrosion resistance"),
        ("Gold (Au)", "high-end electronics and jewelry", "lustrous beauty and complete resistance to tarnishing or corrosion"),
        ("Zinc (Zn)", "galvanising iron to prevent rust", "sacrificial protective coating on steel roofing sheets"),
    ]
    metal, use, reason = rng.choice(metals)

    prompt = (
        f"The large central block of the Periodic Table (between Groups 2 and 13) contains the **transition metals**.\n\n"
        f"1. State two typical physical properties that transition metals share (e.g. hardness, melting point, density).\n"
        f"2. Consider **{metal}**: name its primary practical application ({use}) and explain why its physical properties make it ideal."
    )
    sol = (
        f"**Step 1:** Transition metals are generally **hard, dense, strong**, have **high melting points**, and are **good conductors** of heat and electricity [1 Mark: Properties].\n\n"
        f"**Step 2:** {metal} is used for {use} because of its {reason} [1 Mark: Application]."
    )
    return {
        "id": f"ns7_pt_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Hard, dense, high melting points, good conductors; {metal} is used for {use} due to {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "45_transition_metals_overview",
        "misconception_tags": ["transition_metals"],
        "hints": {
            "tier_1": "Iron, copper, gold, and zinc are transition metals.",
            "tier_2": "They are hard, dense, strong metals with high melting points.",
            "tier_3": f"Hard, dense, high melting point; {metal} used for {use}."
        }
    }


# ==============================================================================
# CLUSTER 8: Scientific Inquiry & Master Challenges (46 - 50)
# ==============================================================================

def arch_46_evaluating_element_data_cards(rng: random.Random) -> Dict[str, Any]:
    cards = [
        ("Carbon", "C", 6, 12.011, "#3b82f6", "Non-metal", "Group 14"),
        ("Magnesium", "Mg", 12, 24.305, "#10b981", "Metal", "Group 2"),
        ("Chlorine", "Cl", 17, 35.45, "#f59e0b", "Non-metal (Halogen)", "Group 17"),
        ("Potassium", "K", 19, 39.098, "#8b5cf6", "Metal (Alkali metal)", "Group 1"),
        ("Silicon", "Si", 14, 28.085, "#ec4899", "Semi-metal", "Group 14"),
    ]
    name, sym, z, mass, color, category, grp = rng.choice(cards)

    svg = (
        f'<svg viewBox="0 0 320 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border-radius:10px;border:2px solid {color};">'
        f'<rect x="10" y="10" width="300" height="200" rx="8" fill="#f8fafc" stroke="{color}" stroke-width="1.5"/>'
        f'<rect x="25" y="25" width="270" height="35" rx="4" fill="{color}"/>'
        f'<text x="160" y="48" font-family="sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">Periodic Table Data Tile</text>'
        f'<text x="45" y="90" font-family="sans-serif" font-size="16" font-weight="bold" fill="#334155">{z}</text>'
        f'<text x="160" y="125" font-family="sans-serif" font-size="38" font-weight="bold" fill="{color}" text-anchor="middle">{sym}</text>'
        f'<text x="160" y="155" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">{name}</text>'
        f'<text x="160" y="180" font-family="sans-serif" font-size="12" fill="#64748b" text-anchor="middle">Atomic Mass: {mass}</text>'
        f'</svg>'
    )

    prompt = (
        f"Examine the chemical data tile for **{name}**.\n\n"
        f"1. State the **atomic number** and the **chemical symbol** of this element.\n"
        f"2. How many protons are present in the nucleus of a single {name} atom?\n"
        f"3. Classify {name} as a metal, non-metal, or semi-metal."
    )
    sol = (
        f"**Step 1:** Atomic number = **{z}**; Chemical symbol = **{sym}** [1 Mark: Number and Symbol].\n\n"
        f"**Step 2:** The atomic number equals the number of protons, so there are **{z} protons** [1 Mark: Proton count].\n\n"
        f"**Step 3:** {name} is classified as a **{category}** [1 Mark: Classification]."
    )
    return {
        "id": f"ns7_pt_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Atomic number: {z}, Symbol: {sym}; {z} protons; Classified as {category}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "46_evaluating_element_data_cards",
        "misconception_tags": ["periodic_table_tile_reading"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": f"Look at the tile: top number is atomic number; big letters are symbol.",
            "tier_2": f"Number of protons = atomic number = {z}.",
            "tier_3": f"Atomic number {z}, symbol {sym}; {z} protons; {category}."
        }
    }


def arch_47_predicting_element_properties_from_position(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Element A is located in Group 1, Period 4 (bottom left of table)", "Metal", "shiny lustrous solid, soft enough to cut with knife, highly reactive with water, good electrical conductor"),
        ("Element B is located in Group 17, Period 2 (top right of table)", "Non-metal", "gas at room temperature, poor electrical conductor (insulator), reactive, forms salts with metals"),
        ("Element C is located along the zigzag line in Group 14, Period 3", "Semi-metal", "solid with intermediate lustre, brittle, acts as a semiconductor with moderate electrical conductivity"),
    ]
    elem_desc, category, expected_props = rng.choice(cases)

    prompt = (
        f"A chemist discovers an unknown element with the following location:\n"
        f"**{elem_desc}**.\n\n"
        f"1. Based purely on its position on the Periodic Table, predict whether this element is a **metal**, **non-metal**, or **semi-metal**.\n"
        f"2. Predict two physical properties you would expect this element to possess (e.g. electrical conductivity, state, malleability)."
    )
    sol = (
        f"**Step 1:** Based on its position, it is classified as a **{category}** [1 Mark: Position classification].\n\n"
        f"**Step 2:** Expected properties: {expected_props} [2 Marks: Property predictions]."
    )
    return {
        "id": f"ns7_pt_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{category}; expected properties: {expected_props}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "47_predicting_element_properties_from_position",
        "misconception_tags": ["periodic_table_predictive_power"],
        "hints": {
            "tier_1": "Left/centre = metals; top right = non-metals; zigzag line = semi-metals.",
            "tier_2": f"This element is in the {category} region of the table.",
            "tier_3": f"{category}; {expected_props}."
        }
    }


def arch_48_misconceptions_element_names_vs_brand_names(rng: random.Random) -> Dict[str, Any]:
    items = [
        ("Steel", "an alloy (mixture) of iron and carbon, not an individual element on the Periodic Table"),
        ("Brass", "an alloy mixture of copper and zinc, not a pure element"),
        ("Water ($H_2O$)", "a chemical compound made of hydrogen and oxygen chemically bonded, not a single element"),
        ("Air", "a homogeneous mixture of several gases (nitrogen, oxygen, argon, carbon dioxide), not a pure element"),
        ("Bronze", "an alloy mixture of copper and tin, not a pure element"),
    ]
    item, explanation = rng.choice(items)

    prompt = (
        f"A learner states: *'Since {item} is widely used in construction and everyday products, it must be listed as an element on the Periodic Table.'*\n\n"
        f"1. Is the learner's statement correct? (Yes or No)\n"
        f"2. Explain why {item} is NOT found as an entry on the Periodic Table of Elements.\n"
        f"3. Name one genuine chemical element that is found on the Periodic Table."
    )
    sol = (
        f"**Step 1:** **No**, the learner's statement is incorrect [1 Mark: True/False evaluation].\n\n"
        f"**Step 2:** {item} is {explanation} [1 Mark: Scientific explanation].\n\n"
        f"**Step 3:** Valid element examples include: Iron ($Fe$), Copper ($Cu$), Gold ($Au$), Oxygen ($O$), Carbon ($C$), or Nitrogen ($N$) [1 Mark: Genuine element]."
    )
    return {
        "id": f"ns7_pt_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"No; {item} is {explanation}; e.g. Iron, Copper, Oxygen",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "48_misconceptions_element_names_vs_brand_names",
        "misconception_tags": ["alloy_compound_vs_element_misconception"],
        "hints": {
            "tier_1": f"Is {item} a pure element made of only one type of atom, or a mixture/compound?",
            "tier_2": f"Only pure single-atom elements are on the Periodic Table. {item} is an alloy/mixture/compound.",
            "tier_3": f"No; {item} is {explanation}."
        }
    }


def arch_49_scientific_inquiry_classifying_mystery_element(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "Element X",
            "Silvery-grey lustrous solid",
            "Light bulb glows brightly (conducts electricity)",
            "Flattens into a thin sheet without cracking (malleable)",
            "Metal",
            "Left or centre of the Periodic Table",
            "#2563eb"
        ),
        (
            "Element Y",
            "Dull yellow solid chunk",
            "Light bulb does not glow (electrical insulator)",
            "Shatters into small powdery fragments (brittle)",
            "Non-metal",
            "Upper right corner of the Periodic Table",
            "#ca8a04"
        ),
        (
            "Element Z",
            "Dark shiny metallic grey crystals",
            "Light bulb glows dimly; bulb glows brighter when sample is gently warmed",
            "Cracks and fractures under heavy hammer blow (brittle)",
            "Semi-metal (metalloid)",
            "Along the zigzag staircase line dividing metals from non-metals",
            "#7c3aed"
        ),
    ]
    elem_code, app, cond, mech, classification, region, col = rng.choice(scenarios)

    svg = (
        f'<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border-radius:8px;border:1px solid #cbd5e1;">'
        f'<rect x="15" y="15" width="350" height="170" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<rect x="25" y="25" width="330" height="30" rx="4" fill="{col}"/>'
        f'<text x="190" y="45" font-family="sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Inquiry Lab: Sample {elem_code}</text>'
        f'<text x="35" y="80" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">Appearance: <tspan font-weight="normal" fill="#475569">{app}</tspan></text>'
        f'<text x="35" y="110" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">Circuit test: <tspan font-weight="normal" fill="#475569">{cond.split("(")[0]}</tspan></text>'
        f'<text x="35" y="140" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">Hammer test: <tspan font-weight="normal" fill="#475569">{mech.split("(")[0]}</tspan></text>'
        f'<text x="190" y="170" font-family="sans-serif" font-size="10" font-style="italic" fill="#64748b" text-anchor="middle">Classify sample into: Metal, Non-metal, or Semi-metal</text>'
        f'</svg>'
    )

    prompt = (
        f"A Natural Sciences learner tests an unknown sample labelled **{elem_code}** in the laboratory:\n\n"
        f"- **Visual Appearance:** {app}\n"
        f"- **Electrical Circuit Test:** {cond}\n"
        f"- **Hammer Impact Test:** {mech}\n\n"
        f"1. Classify {elem_code} as a **metal**, **non-metal**, or **semi-metal (metalloid)**.\n"
        f"2. Provide two pieces of evidence from the test results supporting your classification.\n"
        f"3. In which region of the Periodic Table would you expect to find {elem_code}?"
    )
    sol = (
        f"**Step 1:** {elem_code} is classified as a **{classification}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Evidence: (1) Electrical behavior: {cond}; (2) Mechanical behavior: {mech} [2 Marks: Supporting evidence].\n\n"
        f"**Step 3:** It would be found in the **{region}** [1 Mark: Periodic Table region]."
    )
    return {
        "id": f"ns7_pt_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{classification}; Evidence: {cond} and {mech}; Region: {region}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "term": 2,
        "subskill": "49_scientific_inquiry_classifying_mystery_element",
        "misconception_tags": ["scientific_inquiry_element_classification"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Look at whether it conducts and whether it is malleable or brittle.",
            "tier_2": f"Good conductor + malleable = metal. Insulator + brittle = non-metal. Semiconductor = semi-metal.",
            "tier_3": f"{classification}; Evidence: {cond}, {mech}; Region: {region}."
        }
    }


def arch_50_periodic_table_master_classification_challenge(rng: random.Random) -> Dict[str, Any]:
    quads = [
        ("Copper (Cu)", "Metal", "Left/centre", "electrical wiring"),
        ("Sulfur (S)", "Non-metal", "Upper right", "manufacturing sulfuric acid and vulcanising rubber"),
        ("Silicon (Si)", "Semi-metal", "Zigzag staircase line", "computer microprocessor chips"),
        ("Helium (He)", "Non-metal (Noble gas)", "Far right (Column 18)", "weather balloons and MRI scanners"),
    ]
    e1, e2, e3, e4 = quads

    prompt = (
        f"Complete the comprehensive Periodic Table master classification review for these four elements:\n"
        f"- Element 1: **{e1[0]}**\n"
        f"- Element 2: **{e2[0]}**\n"
        f"- Element 3: **{e3[0]}**\n"
        f"- Element 4: **{e4[0]}**\n\n"
        f"1. Classify each of the four elements as a **metal**, **non-metal**, or **semi-metal**.\n"
        f"2. For each element, identify its general location on the Periodic Table (e.g. left/centre, upper right, zigzag line, or column 18).\n"
        f"3. State one key technological or everyday application for each element."
    )
    sol = (
        f"**Step 1 & 2: Classifications and Locations:**\n"
        f"- **{e1[0]}:** {e1[1]} situated on the **{e1[2]}** [1 Mark].\n"
        f"- **{e2[0]}:** {e2[1]} situated on the **{e2[2]}** [1 Mark].\n"
        f"- **{e3[0]}:** {e3[1]} situated on the **{e3[2]}** [1 Mark].\n"
        f"- **{e4[0]}:** {e4[1]} situated on the **{e4[2]}** [1 Mark].\n\n"
        f"**Step 3: Practical Applications:**\n"
        f"- {e1[0]}: {e1[3]} [1 Mark].\n"
        f"- {e2[0]}: {e2[3]} [1 Mark].\n"
        f"- {e3[0]}: {e3[3]} [1 Mark].\n"
        f"- {e4[0]}: {e4[3]} [1 Mark]."
    )
    return {
        "id": f"ns7_pt_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"1: {e1[1]} ({e1[2]}), 2: {e2[1]} ({e2[2]}), 3: {e3[1]} ({e3[2]}), 4: {e4[1]} ({e4[2]})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 8,
        "term": 2,
        "subskill": "50_periodic_table_master_classification_challenge",
        "misconception_tags": ["master_periodic_table_synthesis"],
        "hints": {
            "tier_1": "Copper is metal; Sulfur is non-metal; Silicon is semi-metal; Helium is noble gas.",
            "tier_2": "Metals are on left/centre, non-metals on upper right, semi-metals along zigzag line, noble gases in column 18.",
            "tier_3": "Cu = metal (left), S = non-metal (right), Si = semi-metal (zigzag), He = noble gas (column 18)."
        }
    }
