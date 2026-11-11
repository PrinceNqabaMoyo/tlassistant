"""
Grade 8 Natural Sciences - Term 2: Chemical Reactions (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/PDF - Chemical reactions.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Physical vs Chemical Changes & Signs of Reaction (01 - 08)
# ==============================================================================

def arch_01_physical_vs_chemical_change_definition(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In chemistry, matter can undergo two fundamentally different kinds of change: physical changes and chemical changes.\n\n"
        f"1. Define a **physical change** and explain whether it is generally easy or difficult to reverse.\n"
        f"2. Define a **chemical change (chemical reaction)** and state what happens to the chemical identity of the substances.\n"
        f"3. In which type of change are new chemical bonds formed and original chemical bonds broken?"
    )
    sol = (
        f"**Step 1:** A physical change is a change in the state, shape, or appearance of a substance **without creating any new chemical substances**; it is **easily reversible** (e.g. melting ice or dissolving sugar) [1 Mark: Physical change].\n\n"
        f"**Step 2:** A chemical change is a process where **one or more new substances with completely different chemical properties are formed**; it is usually difficult or impossible to reverse [1 Mark: Chemical change].\n\n"
        f"**Step 3:** New chemical bonds are formed and original bonds are broken during a **chemical change** [1 Mark: Bond breaking/making]."
    )
    return {
        "id": f"ns8_chem_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Physical change: no new substances, easily reversible; Chemical change: new substances formed with new properties; Chemical change breaks/forms bonds",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "01_physical_vs_chemical_change_definition",
        "misconception_tags": ["physical_vs_chemical_change_definitions"],
        "hints": {
            "tier_1": "Physical change = same substance (reversible). Chemical change = brand new substance.",
            "tier_2": "Chemical bonds only break and reform in chemical changes.",
            "tier_3": "No new substance vs new substance formed; bonds change only in chemical change."
        }
    }


def arch_02_classifying_everyday_changes_physical_vs_chemical(rng: random.Random) -> Dict[str, Any]:
    changes = [
        ("Frying an egg in a hot pan", "Chemical change", "proteins denature and permanently cross-link, changing color and texture irreversibly"),
        ("Dissolving table salt in a glass of water", "Physical change", "no new chemical substance is formed; water can be evaporated to recover original salt crystals"),
        ("Burning a wooden matchstick", "Chemical change", "wood reacts with oxygen to form ash, smoke, carbon dioxide, and water vapor"),
        ("Melting candle wax over gentle heat", "Physical change", "wax changes from solid to liquid without changing its chemical composition, solidifying when cooled"),
        ("Milk turning sour on a warm day", "Chemical change", "lactose sugar is fermented by bacteria into lactic acid, changing taste and curdling proteins"),
        ("Shredding a sheet of paper into small strips", "Physical change", "only the size and shape changed; cellulose molecules remain chemically unaltered"),
    ]
    event, cat, reason = rng.choice(changes)

    prompt = (
        f"Consider the everyday event: **'{event}'**.\n\n"
        f"1. Classify this event as either a **physical change** or a **chemical change**.\n"
        f"2. Provide two scientific reasons supporting your classification ({reason}).\n"
        f"3. Can this process be easily reversed by simple cooling or physical methods?"
    )
    rev_ans = "No" if cat == "Chemical change" else "Yes"
    sol = (
        f"**Step 1:** It is a **{cat}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Reasons: {reason} [1 Mark: Supporting explanation].\n\n"
        f"**Step 3:** **{rev_ans}**, because {cat.lower()}s are {'difficult or impossible to reverse by physical methods' if rev_ans == 'No' else 'easily reversible by physical methods (like evaporation or cooling)'} [1 Mark: Reversibility]."
    )
    return {
        "id": f"ns8_chem_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{cat}; {reason}; {rev_ans}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "02_classifying_everyday_changes_physical_vs_chemical",
        "misconception_tags": ["classifying_physical_chemical_events"],
        "hints": {
            "tier_1": f"Can you undo '{event}' easily?",
            "tier_2": f"If a new chemical formed, it's a chemical change. {event} is a {cat}.",
            "tier_3": f"{cat}; {reason}; {rev_ans}."
        }
    }


def arch_03_signs_of_chemical_reaction_color_and_gas(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("Dropping an effervescent antacid tablet into water", "vigorous bubbling and fizzing without any heating", "carbon dioxide gas produced"),
        ("Adding clear sodium hydroxide to bright blue copper sulfate solution", "formation of a dark royal blue gelatinous precipitate", "copper hydroxide solid formed"),
        ("Heating pink cobalt chloride paper", "turns bright blue upon losing water of crystallization", "chemical hydration state changed"),
    ]
    setup, visual, product = rng.choice(examples)

    prompt = (
        f"When **{setup}**, scientists observe **{visual}** ({product}).\n\n"
        f"1. What are the two major visual signs of a chemical reaction mentioned here?\n"
        f"2. How does gas production during a chemical reaction differ fundamentally from boiling water?\n"
        f"3. Name two other sensory signs (such as smell or temperature) that can indicate a chemical reaction."
    )
    sol = (
        f"**Step 1:** Visual signs include **color change** and **formation of gas bubbles (effervescence)** [1 Mark: Visual signs].\n\n"
        f"**Step 2:** In boiling water, bubbles are steam formed by a physical phase change when heated to $100^\\circ\\text{{C}}$; in a chemical reaction, bubbles are **brand new chemical gas molecules formed at room temperature without boiling** [1 Mark: Boiling vs Reaction gas].\n\n"
        f"**Step 3:** Other signs: **temperature change (heating or cooling)**, **release of an odor/smell**, **sound/explosion**, or **emission of light** [1 Mark: Other signs]."
    )
    return {
        "id": f"ns8_chem_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Color change and gas bubbles; Boiling is physical phase change while reaction gas is a new chemical substance formed; Odor and temperature change",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "03_signs_of_chemical_reaction_color_and_gas",
        "misconception_tags": ["signs_of_chemical_reactions"],
        "hints": {
            "tier_1": "Look for color change, bubbles, smell, or heat.",
            "tier_2": "Boiling is just water turning to steam; chemical bubbles are a new gas.",
            "tier_3": "Color change / gas bubbles; new substance vs phase change; odor / heat change."
        }
    }


def arch_04_signs_of_chemical_reaction_precipitate(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        ("Lead nitrate solution mixed with potassium iodide solution", "bright golden-yellow solid precipitate", "Lead iodide ($PbI_2$)"),
        ("Silver nitrate solution mixed with sodium chloride solution", "curdy white solid precipitate", "Silver chloride ($AgCl$)"),
        ("Barium chloride solution mixed with sodium sulfate solution", "dense white cloudy precipitate", "Barium sulfate ($BaSO_4$)"),
    ]
    reactants, appearance, precipitate_name = rng.choice(reactions)

    prompt = (
        f"Two clear, colorless liquid solutions are poured together in a test tube: **{reactants}**.\n\n"
        f"Instantly, the liquid turns cloudy and a **{appearance}** settles to the bottom of the tube.\n\n"
        f"1. What is the scientific term for an insoluble solid that forms from the reaction of two solutions?\n"
        f"2. Name the insoluble solid formed in this experiment ({precipitate_name}).\n"
        f"3. Why is the formation of a precipitate conclusive proof of a chemical change?"
    )
    sol = (
        f"**Step 1:** The insoluble solid is called a **precipitate** [1 Mark: Term].\n\n"
        f"**Step 2:** The precipitate is **{precipitate_name}** [1 Mark: Precipitate identity].\n\n"
        f"**Step 3:** A precipitate proves a chemical change because a **brand new chemical compound with completely different solubility properties** has been produced from soluble starting reactants [1 Mark: Proof of chemical change]."
    )
    return {
        "id": f"ns8_chem_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Precipitate; {precipitate_name}; Forms a brand new insoluble compound not present before",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "04_signs_of_chemical_reaction_precipitate",
        "misconception_tags": ["precipitate_formation_sign"],
        "hints": {
            "tier_1": "An insoluble solid falling out of solution is a precipitate.",
            "tier_2": f"In this reaction, the solid is {precipitate_name}.",
            "tier_3": f"Precipitate; {precipitate_name}; brand new substance formed."
        }
    }


def arch_05_signs_of_chemical_reaction_temperature_and_light(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Burning magnesium ribbon in air", "dazzling, blinding white light and intense heat", "Magnesium oxide powder"),
        ("Mixing hydrochloric acid with sodium hydroxide solution", "beaker becomes noticeably hot to the touch with no flame", "Neutralisation salt solution"),
        ("Dissolving ammonium nitrate crystals in water (instant cold pack)", "temperature drops rapidly from 22 °C to 5 °C", "Endothermic physical/chemical dissolution"),
    ]
    setup, energy_sign, product = rng.choice(scenarios)

    prompt = (
        f"In a chemistry laboratory demonstration: **{setup}** ({energy_sign}).\n\n"
        f"1. Does this reaction release energy to the surroundings or absorb energy from the surroundings?\n"
        f"2. What is the scientific term for a reaction that releases thermal energy to its surroundings?\n"
        f"3. What is the term for a reaction that absorbs thermal energy, making the surroundings cold?"
    )
    is_exo = "drops" not in energy_sign
    action = "releases energy (exothermic)" if is_exo else "absorbs energy (endothermic)"

    sol = (
        f"**Step 1:** This process **{action}** [1 Mark: Energy direction].\n\n"
        f"**Step 2:** A reaction that releases heat energy is called **exothermic** [1 Mark: Exothermic term].\n\n"
        f"**Step 3:** A reaction that absorbs heat energy is called **endothermic** [1 Mark: Endothermic term]."
    )
    return {
        "id": f"ns8_chem_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{action}; Exothermic; Endothermic",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "05_signs_of_chemical_reaction_temperature_and_light",
        "misconception_tags": ["exothermic_endothermic_signs"],
        "hints": {
            "tier_1": "Exo = exits (releases heat); Endo = enters (absorbs heat).",
            "tier_2": "Getting hot is exothermic; getting cold is endothermic.",
            "tier_3": f"{action}; Exothermic; Endothermic."
        }
    }


def arch_06_eggshell_and_vinegar_investigation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In the 'naked egg' experiment, a raw egg with an intact shell is submerged in a beaker of white vinegar (acetic acid) for 4 days:\n\n"
        f"1. What is the main chemical compound that makes up the hard eggshell?\n"
        f"2. What immediate visual sign is observed on the surface of the eggshell within minutes of pouring vinegar?\n"
        f"3. After 4 days, what has happened to the hard eggshell, and what holds the egg together?\n"
        f"4. Name the gas produced during this reaction and describe how to test it."
    )
    sol = (
        f"**Step 1:** The eggshell is made of **calcium carbonate ($CaCO_3$)** [1 Mark: Eggshell composition].\n\n"
        f"**Step 2:** Tiny **bubbles of gas (effervescence)** appear rapidly covering the surface of the eggshell [1 Mark: Immediate sign].\n\n"
        f"**Step 3:** The hard shell **completely dissolves (reacts away)**, leaving only the flexible semi-permeable egg membrane holding the raw egg together [1 Mark: Outcome].\n\n"
        f"**Step 4:** The gas is **carbon dioxide ($CO_2$)**; test by bubbling through **clear limewater**, which turns **milky/cloudy white** [1 Mark: Gas test]."
    )
    return {
        "id": f"ns8_chem_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Calcium carbonate; Bubbles of gas on shell surface; Shell dissolves leaving flexible membrane; Carbon dioxide gas tested with limewater",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "term": 2,
        "subskill": "06_eggshell_and_vinegar_investigation",
        "misconception_tags": ["eggshell_vinegar_acid_carbonate"],
        "hints": {
            "tier_1": "Eggshells are calcium carbonate; vinegar is an acid.",
            "tier_2": "Acid + carbonate produces CO2 bubbles and dissolves the shell.",
            "tier_3": "Calcium carbonate; gas bubbles; shell dissolves leaving membrane; CO2 turns limewater milky."
        }
    }


def arch_07_exothermic_vs_endothermic_reactions(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        ("Combustion of wood in a campfire", "Exothermic", "heat and light energy are released into the surrounding air, warming campers"),
        ("Photosynthesis in green plant leaves", "Endothermic", "chlorophyll absorbs sunlight radiant energy to convert carbon dioxide and water into glucose"),
        ("Thermal decomposition of calcium carbonate in a lime kiln", "Endothermic", "continuous high heat input is required to break chemical bonds into calcium oxide and CO2"),
        ("Reaction between magnesium ribbon and hydrochloric acid", "Exothermic", "temperature of the acid solution rises by over 25 °C"),
    ]
    rxn, cat, desc = rng.choice(reactions)

    prompt = (
        f"Consider the chemical process: **{rxn}** ({desc}).\n\n"
        f"1. Classify this reaction as **exothermic** or **endothermic**.\n"
        f"2. Explain what happens to the temperature of the immediate surroundings during an {cat.lower()} reaction.\n"
        f"3. In terms of chemical bonds, explain why some reactions release net energy while others absorb net energy."
    )
    sol = (
        f"**Step 1:** It is classified as **{cat}** [1 Mark: Classification].\n\n"
        f"**Step 2:** In an {cat.lower()} reaction, the temperature of the surroundings **{'rises / increases' if cat == 'Exothermic' else 'drops / decreases (or requires continuous heat input)'}** [1 Mark: Temperature effect].\n\n"
        f"**Step 3:** If the energy released when forming new bonds in the products is **greater** than the energy needed to break bonds in reactants, the reaction is exothermic; if bond-breaking requires more energy than bond-forming releases, it is endothermic [1 Mark: Bond energy explanation]."
    )
    return {
        "id": f"ns8_chem_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{cat}; Surroundings temperature {'increases' if cat == 'Exothermic' else 'decreases'}; Depends on balance between bond-breaking energy and bond-forming energy",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "07_exothermic_vs_endothermic_reactions",
        "misconception_tags": ["exothermic_vs_endothermic"],
        "hints": {
            "tier_1": f"Does {rxn.split(' in ')[0].split(' of ')[0]} give off heat or soak up heat?",
            "tier_2": "Exo = gives out heat (gets hot); Endo = takes in heat (gets cold).",
            "tier_3": f"{cat}; temperature {'rises' if cat == 'Exothermic' else 'drops'}; bond energy balance."
        }
    }


def arch_08_reversibility_physical_vs_chemical(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner states: *'Since ice melting can be reversed by putting water in the freezer, burning a piece of paper should be reversible by putting the ash and smoke in a freezer.'*\n\n"
        f"1. Is the learner's reasoning correct? (Yes or No)\n"
        f"2. Explain why melting ice is easily reversible while burning paper is practically irreversible.\n"
        f"3. Contrast the rearrangement of chemical bonds in melting ice with that in burning paper."
    )
    sol = (
        f"**Step 1:** **No**, the learner's reasoning is completely false [1 Mark: Evaluation].\n\n"
        f"**Step 2:** Melting ice is a **physical change** where water molecules remain chemically identical ($H_2O$); cooling simply slows them down so attractive forces re-lock them. Burning paper is a **chemical change** where cellulose reacted with oxygen to form new gases ($CO_2, H_2O$) and ash, which cannot recombine simply by cooling [1 Mark: Reversibility explanation].\n\n"
        f"**Step 3:** In melting ice, **no chemical bonds are broken or formed** (only weak intermolecular forces change). In burning paper, strong **covalent bonds are broken and completely new chemical bonds are created** [1 Mark: Bond contrast]."
    )
    return {
        "id": f"ns8_chem_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "No; Melting is physical (same molecules) while burning is chemical (new compounds formed); Melting changes intermolecular forces, burning breaks/forms chemical bonds",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "08_reversibility_physical_vs_chemical",
        "misconception_tags": ["reversibility_physical_vs_chemical"],
        "hints": {
            "tier_1": "You cannot un-burn a piece of paper by freezing the smoke!",
            "tier_2": "Physical changes are reversible; chemical reactions form new permanent substances.",
            "tier_3": "No; physical change vs permanent chemical bonds broken/made."
        }
    }


# ==============================================================================
# CLUSTER 2: Reactants, Products & Word Equations (09 - 17)
# ==============================================================================

def arch_09_reactants_and_products_definition_left_right(rng: random.Random) -> Dict[str, Any]:
    equations = [
        ("Carbon + Oxygen -> Carbon dioxide", "Carbon and Oxygen", "Carbon dioxide"),
        ("Hydrogen + Oxygen -> Water", "Hydrogen and Oxygen", "Water"),
        ("Iron + Sulfur -> Iron sulfide", "Iron and Sulfur", "Iron sulfide"),
        ("Methane + Oxygen -> Carbon dioxide + Water", "Methane and Oxygen", "Carbon dioxide and Water"),
    ]
    eq, reacts, prods = rng.choice(equations)

    prompt = (
        f"Consider the chemical equation:\n"
        f"**{eq}**\n\n"
        f"1. Define the term **reactants** and identify the reactants in this equation.\n"
        f"2. Define the term **products** and identify the products in this equation.\n"
        f"3. What does the arrow ($\\rightarrow$) in the middle of a chemical equation mean?"
    )
    sol = (
        f"**Step 1:** Reactants are the **starting substances present before a chemical reaction takes place** (written on the left of the arrow): **{reacts}** [1 Mark: Reactants].\n\n"
        f"**Step 2:** Products are the **new substances formed/produced as a result of the chemical reaction** (written on the right of the arrow): **{prods}** [1 Mark: Products].\n\n"
        f"**Step 3:** The arrow means **'reacts to form'** (or 'yields / produces'); it indicates the direction of chemical change [1 Mark: Arrow meaning]."
    )
    return {
        "id": f"ns8_chem_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Reactants = starting substances ({reacts}); Products = new substances formed ({prods}); Arrow means 'reacts to form' or 'yields'",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "09_reactants_and_products_definition_left_right",
        "misconception_tags": ["reactants_products_definition"],
        "hints": {
            "tier_1": "Left side = reactants; Right side = products. Arrow = yields.",
            "tier_2": f"Reactants are {reacts}; Products are {prods}.",
            "tier_3": f"Reactants on left ({reacts}); Products on right ({prods}); arrow = yields/produces."
        }
    }


def arch_10_interpreting_word_equations(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        ("When silvery magnesium ribbon burns in oxygen gas, white magnesium oxide powder is formed.", "Magnesium + Oxygen -> Magnesium oxide"),
        ("When iron filings are strongly heated with yellow sulfur powder, black iron sulfide is produced.", "Iron + Sulfur -> Iron sulfide"),
        ("When copper metal is heated in sulfur vapor, black copper sulfide forms.", "Copper + Sulfur -> Copper sulfide"),
        ("When calcium metal is dropped into water, calcium hydroxide solution and hydrogen gas are produced.", "Calcium + Water -> Calcium hydroxide + Hydrogen"),
    ]
    narrative, word_eq = rng.choice(reactions)

    prompt = (
        f"A laboratory experiment is described as follows:\n"
        f"*'{narrative}'*\n\n"
        f"1. Write down the complete **word equation** for this chemical reaction.\n"
        f"2. Clearly identify the reactant(s) and the product(s).\n"
        f"3. Why do scientists use chemical equations instead of writing long descriptive paragraphs?"
    )
    parts = word_eq.split(" -> ")
    r_list = parts[0]
    p_list = parts[1]

    sol = (
        f"**Step 1:** Word equation: **{word_eq}** [1 Mark: Word equation].\n\n"
        f"**Step 2:** Reactants: **{r_list}**; Product(s): **{p_list}** [1 Mark: Identification].\n\n"
        f"**Step 3:** Equations provide a **standardized, concise, and universal scientific shorthand** that clearly shows reactants turning into products and the conservation of atoms across language barriers [1 Mark: Purpose of equations]."
    )
    return {
        "id": f"ns8_chem_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Word equation: {word_eq}; Reactants: {r_list}, Products: {p_list}; Concise, universal scientific shorthand",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "10_interpreting_word_equations",
        "misconception_tags": ["word_equation_translation"],
        "hints": {
            "tier_1": "Put starting chemicals on the left, an arrow, then the end chemicals on the right.",
            "tier_2": f"Equation: {word_eq}.",
            "tier_3": f"{word_eq}; Reactants: {r_list}; Products: {p_list}."
        }
    }


def arch_11_writing_word_equations_combustion(rng: random.Random) -> Dict[str, Any]:
    fuels = [
        ("Methane (natural gas)", "Methane + Oxygen -> Carbon dioxide + Water"),
        ("Carbon (charcoal / coal)", "Carbon + Oxygen -> Carbon dioxide"),
        ("Hydrogen gas", "Hydrogen + Oxygen -> Water"),
        ("Wax (paraffin hydrocarbon)", "Wax + Oxygen -> Carbon dioxide + Water"),
    ]
    fuel_name, eq = rng.choice(fuels)

    prompt = (
        f"Combustion is the rapid chemical reaction of a fuel with oxygen gas, releasing energy.\n\n"
        f"Consider the complete combustion of **{fuel_name}**.\n\n"
        f"1. What gas from the air is always an essential reactant in any combustion reaction?\n"
        f"2. Write the balanced **word equation** for the combustion of {fuel_name} ({eq}).\n"
        f"3. What dangerous toxic gas is produced if combustion occurs with insufficient oxygen (incomplete combustion)?"
    )
    sol = (
        f"**Step 1:** The essential gas reactant is **oxygen ($O_2$)** [1 Mark: Oxygen reactant].\n\n"
        f"**Step 2:** Word equation: **{eq}** [1 Mark: Word equation].\n\n"
        f"**Step 3:** Incomplete combustion produces deadly **carbon monoxide ($CO$)** gas [1 Mark: Carbon monoxide]."
    )
    return {
        "id": f"ns8_chem_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Oxygen; {eq}; Carbon monoxide (CO)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "11_writing_word_equations_combustion",
        "misconception_tags": ["combustion_word_equations"],
        "hints": {
            "tier_1": "Burning always needs oxygen.",
            "tier_2": f"Fuel + Oxygen -> Products. Here: {eq}.",
            "tier_3": f"Oxygen; {eq}; Carbon monoxide."
        }
    }


def arch_12_writing_word_equations_metal_synthesis(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Magnesium ribbon burned in air", "Magnesium + Oxygen -> Magnesium oxide"),
        ("Iron wool burned in pure oxygen", "Iron + Oxygen -> Iron oxide"),
        ("Copper turnings heated with sulfur", "Copper + Sulfur -> Copper sulfide"),
        ("Zinc powder heated with sulfur", "Zinc + Sulfur -> Zinc sulfide"),
    ]
    exp, word_eq = rng.choice(metals)

    prompt = (
        f"When a metal chemically reacts directly with a non-metal, a synthesis reaction occurs:\n"
        f"**{exp}**.\n\n"
        f"1. Write the **word equation** for this synthesis reaction ({word_eq}).\n"
        f"2. State the reactants and product in this reaction.\n"
        f"3. How does the suffix of the non-metal's name change when naming the product compound?"
    )
    parts = word_eq.split(" -> ")
    sol = (
        f"**Step 1:** Word equation: **{word_eq}** [1 Mark: Word equation].\n\n"
        f"**Step 2:** Reactants: **{parts[0]}**; Product: **{parts[1]}** [1 Mark: Identification].\n\n"
        f"**Step 3:** The non-metal takes the suffix **'-ide'** (e.g. oxygen becomes oxide, sulfur becomes sulfide) [1 Mark: -ide suffix]."
    )
    return {
        "id": f"ns8_chem_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{word_eq}; Reactants: {parts[0]}, Product: {parts[1]}; Suffix changes to '-ide'",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "12_writing_word_equations_metal_synthesis",
        "misconception_tags": ["metal_synthesis_reactions"],
        "hints": {
            "tier_1": "Metal + Non-metal -> Metal non-metal-ide.",
            "tier_2": f"Word equation: {word_eq}.",
            "tier_3": f"{word_eq}; Reactants: {parts[0]}; Product: {parts[1]}; '-ide' suffix."
        }
    }


def arch_13_writing_word_equations_acid_carbonate(rng: random.Random) -> Dict[str, Any]:
    carbonates = [
        ("Calcium carbonate (limestone / chalk) reacting with hydrochloric acid", "Calcium carbonate + Hydrochloric acid -> Calcium chloride + Carbon dioxide + Water"),
        ("Sodium bicarbonate (baking soda) reacting with vinegar (acetic acid)", "Sodium bicarbonate + Acetic acid -> Sodium acetate + Carbon dioxide + Water"),
        ("Copper carbonate reacting with sulfuric acid", "Copper carbonate + Sulfuric acid -> Copper sulfate + Carbon dioxide + Water"),
    ]
    desc, eq = rng.choice(carbonates)

    prompt = (
        f"The reaction between an acid and a metal carbonate is a classic effervescent reaction:\n"
        f"**{desc}**.\n\n"
        f"1. What three general classes of products are always formed when an acid reacts with a metal carbonate?\n"
        f"2. Write the complete **word equation** for this specific reaction ({eq}).\n"
        f"3. What visible sign in the reaction flask indicates that gas is forming?"
    )
    sol = (
        f"**Step 1:** The products are always a **salt**, **carbon dioxide**, and **water** [1 Mark: General products].\n\n"
        f"**Step 2:** Word equation: **{eq}** [1 Mark: Word equation].\n\n"
        f"**Step 3:** Rapid bubbling, fizzing, and frothing (**effervescence**) indicate that gas is being produced [1 Mark: Effervescence sign]."
    )
    return {
        "id": f"ns8_chem_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Salt, Carbon dioxide, and Water; {eq}; Effervescence / rapid bubbling",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "13_writing_word_equations_acid_carbonate",
        "misconception_tags": ["acid_carbonate_reactions"],
        "hints": {
            "tier_1": "Acid + Carbonate -> Salt + Carbon dioxide + Water.",
            "tier_2": f"Equation: {eq}.",
            "tier_3": f"Salt + Carbon dioxide + Water; {eq}; bubbling/effervescence."
        }
    }


def arch_14_writing_word_equations_decomposition(rng: random.Random) -> Dict[str, Any]:
    decomps = [
        ("Hydrogen peroxide ($H_2O_2$) decomposing into water and oxygen gas in the presence of manganese dioxide catalyst", "Hydrogen peroxide -> Water + Oxygen"),
        ("Thermal decomposition of copper carbonate when heated", "Copper carbonate -> Copper oxide + Carbon dioxide"),
        ("Electrolysis of water using an electric current", "Water -> Hydrogen + Oxygen"),
    ]
    setup, word_eq = rng.choice(decomps)

    prompt = (
        f"In a decomposition reaction, a single compound breaks down into simpler substances:\n"
        f"**{setup}**.\n\n"
        f"1. Write the **word equation** for this decomposition reaction ({word_eq}).\n"
        f"2. How does a decomposition reaction differ in structure from a synthesis reaction?\n"
        f"3. How many reactants are on the left side of the arrow in a pure decomposition reaction?"
    )
    sol = (
        f"**Step 1:** Word equation: **{word_eq}** [1 Mark: Word equation].\n\n"
        f"**Step 2:** In synthesis, multiple reactants combine into one product; in decomposition, **one single reactant breaks apart into multiple simpler products** [1 Mark: Decomposition vs Synthesis].\n\n"
        f"**Step 3:** There is only **one single reactant** on the left side [1 Mark: Single reactant]."
    )
    return {
        "id": f"ns8_chem_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{word_eq}; Single reactant breaks into multiple products; Exactly 1 reactant",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "14_writing_word_equations_decomposition",
        "misconception_tags": ["decomposition_word_equations"],
        "hints": {
            "tier_1": "Decomposition means 1 reactant breaks down into 2 or more products.",
            "tier_2": f"Equation: {word_eq}.",
            "tier_3": f"{word_eq}; 1 reactant splits into multiple products; 1 reactant."
        }
    }


def arch_15_interpreting_subscripts_vs_coefficients(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("2H_2O", "the '2' in front is a coefficient, the '2' below is a subscript", 2, 4, 2),
        ("3CO_2", "the '3' in front is a coefficient, the '2' below is a subscript", 3, 3, 6),
        ("2NH_3", "the '2' in front is a coefficient, the '3' below is a subscript", 2, 2, 6),
    ]
    code, desc, n_molecules, n_e1, n_e2 = rng.choice(examples)

    prompt = (
        f"Consider the chemical expression: **${code}$** ({desc}).\n\n"
        f"1. Explain what the **large coefficient in front** represents.\n"
        f"2. Explain what the **small subscript number** represents.\n"
        f"3. Calculate the total number of molecules and the total number of each type of atom represented by ${code}$."
    )
    sol = (
        f"**Step 1:** The coefficient in front represents the **number of separate, individual molecules** (here, {n_molecules} molecules) [1 Mark: Coefficient].\n\n"
        f"**Step 2:** The subscript represents the **number of atoms of that specific element chemically bonded together** inside each single molecule [1 Mark: Subscript].\n\n"
        f"**Step 3:** There are **{n_molecules} molecules** in total, containing **{n_e1} atoms of the first element** and **{n_e2} atoms of the second element** (total atoms = {n_e1 + n_e2}) [1 Mark: Calculations]."
    )
    return {
        "id": f"ns8_chem_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Coefficient = number of separate molecules; Subscript = number of bonded atoms in one molecule; Total: {n_molecules} molecules, {n_e1} and {n_e2} atoms",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "15_interpreting_subscripts_vs_coefficients",
        "misconception_tags": ["subscripts_vs_coefficients_in_equations"],
        "hints": {
            "tier_1": "Big number in front = how many molecules. Little subscript = how many atoms inside.",
            "tier_2": f"Multiply the coefficient by subscripts to get total atoms.",
            "tier_3": f"Coefficient = molecules; Subscript = bonded atoms per molecule; {n_molecules} molecules ({n_e1} and {n_e2} atoms)."
        }
    }


def arch_16_particle_diagram_reactants_to_products(rng: random.Random) -> Dict[str, Any]:
    c_carb = rng.choice(["#1e293b", "#0f172a", "#334155"])
    c_ox = rng.choice(["#ef4444", "#dc2626", "#e11d48"])
    uid = f"FIG-{rng.randint(100, 999)}"
    svg = (
        f'<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="340" height="140" rx="6" fill="#f8fafc"/>'
        f'<text x="180" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Reaction: C + O₂ → CO₂</text>'
        f'<text x="340" y="25" font-family="sans-serif" font-size="8" fill="#94a3b8" text-anchor="end">{uid}</text>'
        # Reactants box
        f'<rect x="25" y="38" width="130" height="90" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>'
        f'<text x="90" y="52" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Reactants</text>'
        f'<circle cx="55" cy="85" r="14" fill="{c_carb}" stroke="#0f172a"/>'
        f'<text x="55" y="89" font-family="sans-serif" font-size="9" fill="#ffffff" text-anchor="middle">C</text>'
        f'<circle cx="100" cy="85" r="12" fill="{c_ox}" stroke="#0f172a"/>'
        f'<circle cx="120" cy="85" r="12" fill="{c_ox}" stroke="#0f172a"/>'
        # Arrow
        f'<path d="M 165,85 L 195,85 M 190,80 L 197,85 L 190,90" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        # Products box
        f'<rect x="205" y="38" width="130" height="90" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>'
        f'<text x="270" y="52" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Products</text>'
        f'<circle cx="270" cy="85" r="14" fill="{c_carb}" stroke="#0f172a"/>'
        f'<circle cx="250" cy="85" r="12" fill="{c_ox}" stroke="#0f172a"/>'
        f'<circle cx="290" cy="85" r="12" fill="{c_ox}" stroke="#0f172a"/>'
        f'<text x="270" y="89" font-family="sans-serif" font-size="9" fill="#ffffff" text-anchor="middle">C</text>'
        f'<text x="180" y="145" font-family="sans-serif" font-size="9" fill="#64748b" text-anchor="middle">Atoms rearranged into a new compound</text>'
        f'</svg>'
    )

    prompt = (
        f"Examine the particle model diagram showing the reaction between carbon and oxygen.\n\n"
        f"1. How many carbon atoms and how many oxygen atoms are on the **reactants side**?\n"
        f"2. How many carbon atoms and how many oxygen atoms are on the **products side**?\n"
        f"3. Explain how this particle model diagram proves that a chemical reaction has occurred, and that atoms were conserved."
    )
    sol = (
        f"**Step 1:** Reactants side: **1 carbon atom** and **2 oxygen atoms** (1 diatomic $O_2$ molecule) [1 Mark: Reactant counts].\n\n"
        f"**Step 2:** Products side: **1 carbon atom** and **2 oxygen atoms** (bonded in 1 $CO_2$ molecule) [1 Mark: Product counts].\n\n"
        f"**Step 3:** A reaction occurred because the atoms **rearranged and formed new chemical bonds** to create a new compound ($CO_2$); atoms were conserved because the **total number and types of atoms are identical** before and after the reaction [1 Mark: Proof of reaction and conservation]."
    )
    return {
        "id": f"ns8_chem_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Reactants: 1 C, 2 O; Products: 1 C, 2 O; Proves reaction because atoms rearranged into new compound, conserved because atom counts are equal",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "16_particle_diagram_reactants_to_products",
        "misconception_tags": ["particle_diagram_rearrangement"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Count the black circles and red circles on each side.",
            "tier_2": "1 C and 2 O on both sides = conservation of atoms.",
            "tier_3": "1 C, 2 O on reactants; 1 C, 2 O on products; atoms rearranged into new compound."
        }
    }


def arch_17_identifying_leftover_reactants_limiting_excess(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "Making sandwiches: 10 slices of bread and 3 cheese slices (each sandwich needs 2 bread + 1 cheese)",
            "3 cheese sandwiches made, 4 slices of bread leftover",
            "Cheese is limiting, Bread is in excess",
            "Cheese runs out first, stopping further sandwich production"
        ),
        (
            "Combustion of coal: a 100 g lump of coal is burned in a sealed jar containing only 5 g of oxygen gas",
            "Oxygen gas is consumed quickly, leaving most of the black coal unburned",
            "Oxygen is limiting, Coal is in excess",
            "Oxygen is exhausted first, extinguishing the flame"
        ),
    ]
    setup, outcome, roles, reason = rng.choice(scenarios)

    prompt = (
        f"In chemistry, reactions stop when one of the reactants is completely used up.\n\n"
        f"Consider this analogy / scenario:\n"
        f"**{setup}** ({outcome}).\n\n"
        f"1. Identify which reactant is the **limiting reactant** and which is in **excess**.\n"
        f"2. Explain what a **limiting reactant** is in a chemical reaction.\n"
        f"3. What happens to the rate of product formation once the limiting reactant is completely consumed?"
    )
    sol = (
        f"**Step 1:** {roles} [1 Mark: Identification].\n\n"
        f"**Step 2:** The limiting reactant is the substance that is **completely consumed first in the reaction**, thereby determining and limiting the maximum amount of product that can be formed [1 Mark: Definition].\n\n"
        f"**Step 3:** The chemical reaction **stops completely** (product formation drops to zero) [1 Mark: Reaction stops]."
    )
    return {
        "id": f"ns8_chem_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{roles}; Limiting reactant is used up first and limits product; Reaction stops completely",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "17_identifying_leftover_reactants_limiting_excess",
        "misconception_tags": ["limiting_and_excess_reactants"],
        "hints": {
            "tier_1": "The one that runs out first is limiting; what's left over is excess.",
            "tier_2": "When the limiting reactant is gone, the reaction stops.",
            "tier_3": f"{roles}; limiting runs out first; reaction stops."
        }
    }


# ==============================================================================
# CLUSTER 3: Rearrangement of Atoms & Conservation of Mass (18 - 25)
# ==============================================================================

def arch_18_chemical_reaction_as_atomic_rearrangement(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"At a sub-microscopic level, a chemical reaction is defined as a **rearrangement of atoms**.\n\n"
        f"1. Explain what must happen to the original chemical bonds between atoms in the reactants before new products can form.\n"
        f"2. What happens to the separated atoms after the original bonds are broken?\n"
        f"3. Do any atoms turn into different elements during a standard chemical reaction? Explain."
    )
    sol = (
        f"**Step 1:** The chemical bonds holding atoms together in the reactants must be **broken** (requiring energy input) [1 Mark: Bond breaking].\n\n"
        f"**Step 2:** The freed atoms **recombine and form new chemical bonds** in different arrangements, producing the product compounds [1 Mark: Bond forming].\n\n"
        f"**Step 3:** **No**, atoms never change into different elements during chemical reactions; their atomic nuclei and proton numbers remain completely unchanged (only electrons and bonds rearrange) [1 Mark: Element permanence]."
    )
    return {
        "id": f"ns8_chem_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Bonds in reactants must be broken; Atoms recombine forming new bonds in products; No, atoms never change elements (only rearrange)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "18_chemical_reaction_as_atomic_rearrangement",
        "misconception_tags": ["atomic_rearrangement_concept"],
        "hints": {
            "tier_1": "Old bonds break, atoms swap partners, new bonds form.",
            "tier_2": "Atoms never change identity; a carbon atom stays carbon forever.",
            "tier_3": "Bonds break; new bonds form; atoms do not change into other elements."
        }
    }


def arch_19_bond_breaking_endothermic_vs_bond_making_exothermic(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Energy is intimately involved in every chemical bond transformation.\n\n"
        f"1. Is **breaking chemical bonds** an endothermic (energy-absorbing) process or an exothermic (energy-releasing) process? Explain using an analogy (e.g. pulling magnets apart).\n"
        f"2. Is **forming new chemical bonds** an endothermic or exothermic process?\n"
        f"3. When is an overall chemical reaction classified as **exothermic**?"
    )
    sol = (
        f"**Step 1:** Breaking bonds is **endothermic (requires/absorbs energy)**; just like pulling two attracting magnets apart requires work and effort, energy must be put in to break the attraction holding atoms together [1 Mark: Bond breaking].\n\n"
        f"**Step 2:** Forming new chemical bonds is **exothermic (releases energy)** [1 Mark: Bond making].\n\n"
        f"**Step 3:** A reaction is overall exothermic when the **energy released during new bond formation is greater than the energy required to break the original bonds** [1 Mark: Net exothermic condition]."
    )
    return {
        "id": f"ns8_chem_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Breaking bonds is endothermic (absorbs energy); Forming bonds is exothermic (releases energy); Exothermic when bond-forming energy exceeds bond-breaking energy",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "19_bond_breaking_endothermic_vs_bond_making_exothermic",
        "misconception_tags": ["bond_breaking_vs_forming_energy"],
        "hints": {
            "tier_1": "Takes energy to break bonds; releases energy when new bonds snap together.",
            "tier_2": "BEND: Breaking is ENDothermic. MEXO: Making is EXOthermic.",
            "tier_3": "Breaking = endothermic; Forming = exothermic; exothermic when forming energy > breaking energy."
        }
    }


def arch_20_law_of_conservation_of_atoms(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The **Law of Conservation of Atoms** is a universal invariant in all standard chemical reactions.\n\n"
        f"1. State the Law of Conservation of Atoms.\n"
        f"2. In the reaction $C + O_2 \\rightarrow CO_2$, explain how this law is satisfied.\n"
        f"3. Why is it impossible for a chemical reaction starting with pure carbon and oxygen to produce a compound containing nitrogen?"
    )
    sol = (
        f"**Step 1:** The Law of Conservation of Atoms states that **atoms cannot be created or destroyed in a chemical reaction**; the total number and type of atoms remain strictly identical before and after the reaction [1 Mark: Law definition].\n\n"
        f"**Step 2:** On the reactants side there is 1 carbon and 2 oxygen atoms; on the product side there is 1 carbon and 2 oxygen atoms ($1 = 1$ and $2 = 2$), so all atoms are conserved [1 Mark: Verification].\n\n"
        f"**Step 3:** Because atoms cannot be created from nothing, if nitrogen atoms were not present in the starting reactants, **no nitrogen atoms can appear in the products** [1 Mark: Element conservation]."
    )
    return {
        "id": f"ns8_chem_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Atoms cannot be created or destroyed; Same number of C and O atoms on both sides; No nitrogen in reactants so cannot appear in products",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "20_law_of_conservation_of_atoms",
        "misconception_tags": ["conservation_of_atoms_law"],
        "hints": {
            "tier_1": "You cannot create new atoms out of thin air.",
            "tier_2": "What goes in must equal what comes out.",
            "tier_3": "Atoms neither created nor destroyed; equal atom counts; cannot create new elements."
        }
    }


def arch_21_law_of_conservation_of_mass_closed_system(rng: random.Random) -> Dict[str, Any]:
    m1 = rng.choice([25, 30, 45])
    m2 = rng.choice([15, 20, 35])
    total_m = m1 + m2

    prompt = (
        f"In a sealed laboratory reaction flask (a closed system):\n"
        f"- Mass of Solution A = **${m1}\\text{{ g}}**\n"
        f"- Mass of Solution B = **${m2}\\text{{ g}}**\n\n"
        f"When mixed together, an intense reaction occurs with bubbling, color change, and a solid precipitate.\n\n"
        f"1. State the **Law of Conservation of Mass**.\n"
        f"2. Calculate the expected total mass of the reaction flask and products after the reaction is complete.\n"
        f"3. Explain why this law holds true in terms of atoms."
    )
    sol = (
        f"**Step 1:** The Law of Conservation of Mass states that **in a closed system, the total mass of the products must equal the total mass of the reactants** [1 Mark: Law statement].\n\n"
        f"**Step 2:** Total mass = ${m1} + {m2} = \\mathbf{{{total_m}\\text{{ g}}}}$ [1 Mark: Mass calculation].\n\n"
        f"**Step 3:** The law holds true because every individual atom present in the reactants is still present in the products; since **no atoms were created or destroyed, the total mass cannot change** [1 Mark: Atomic basis of mass conservation]."
    )
    return {
        "id": f"ns8_chem_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Total mass of reactants equals total mass of products; Exactly {total_m} g; All atoms are conserved so total mass remains constant",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "21_law_of_conservation_of_mass_closed_system",
        "misconception_tags": ["conservation_of_mass_closed_system"],
        "hints": {
            "tier_1": f"Add the masses together: {m1} + {m2}.",
            "tier_2": "Mass cannot disappear in a sealed flask.",
            "tier_3": f"Mass of reactants = mass of products; exactly {total_m} g; atoms conserved."
        }
    }


def arch_22_mass_loss_in_open_vessel_gas_escape(rng: random.Random) -> Dict[str, Any]:
    m_start = rng.choice([150, 200, 250])
    gas_m = rng.choice([2, 4, 6])
    m_end = m_start - gas_m

    prompt = (
        f"A student places an open beaker containing vinegar on a digital scale (mass = ${m_start}\\text{{ g}}$). An antacid tablet is dropped in.\n\n"
        f"Vigorous fizzing and foaming occur. When the reaction finishes, the balance reads **${m_end}\\text{{ g}}$** (a loss of ${gas_m}\\text{{ g}}$).\n\n"
        f"1. Did this reaction violate the Law of Conservation of Mass? (Yes or No)\n"
        f"2. Explain why the digital scale measured a loss of ${gas_m}\\text{{ g}}$.\n"
        f"3. How could the student modify the experimental setup to prove that mass was actually conserved?"
    )
    sol = (
        f"**Step 1:** **No**, the Law of Conservation of Mass was not violated [1 Mark: Yes/No].\n\n"
        f"**Step 2:** The reaction took place in an **open system**; carbon dioxide gas ($CO_2$) was produced and **escaped into the surrounding room air**, carrying ${gas_m}\\text{{ g}}$ of mass away from the scale [1 Mark: Gas escape explanation].\n\n"
        f"**Step 3:** The student should conduct the experiment in a **closed system** (e.g. inside a tightly sealed flask or flask with a balloon stretched over the mouth to trap all escaping gas) [1 Mark: Closed system solution]."
    )
    return {
        "id": f"ns8_chem_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"No; Carbon dioxide gas escaped into room air ({gas_m} g lost); Conduct in sealed flask (closed system) to trap gas",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "22_mass_loss_in_open_vessel_gas_escape",
        "misconception_tags": ["mass_loss_open_system_misconception"],
        "hints": {
            "tier_1": "The gas flew away into the room, taking its weight with it.",
            "tier_2": "Seal the flask with a stopper or balloon to keep the gas in.",
            "tier_3": "No violation; gas escaped into air; use closed system / sealed flask."
        }
    }


def arch_23_counting_atoms_reactant_side_vs_product_side(rng: random.Random) -> Dict[str, Any]:
    equations = [
        ("2Mg + O_2 -> 2MgO", "Magnesium oxide synthesis", [("Mg", 2, 2), ("O", 2, 2)]),
        ("2H_2 + O_2 -> 2H_2O", "Water synthesis", [("H", 4, 4), ("O", 2, 2)]),
        ("CH_4 + 2O_2 -> CO_2 + 2H_2O", "Methane combustion", [("C", 1, 1), ("H", 4, 4), ("O", 4, 4)]),
    ]
    eq, name, atom_counts = rng.choice(equations)
    breakdown_text = "; ".join([f"{elem}: {r} on reactants vs {p} on products" for elem, r, p in atom_counts])

    prompt = (
        f"Consider the balanced chemical equation for **{name}**:\n"
        f"**${eq}$**\n\n"
        f"1. Count the number of atoms of each element on the **reactants side** (left of arrow).\n"
        f"2. Count the number of atoms of each element on the **products side** (right of arrow).\n"
        f"3. Is this chemical equation correctly balanced? Explain using your counts."
    )
    sol = (
        f"**Step 1 & 2:** Atom counts: **{breakdown_text}** [2 Marks: Reactant & Product counts].\n\n"
        f"**Step 3:** **Yes, it is perfectly balanced** because the number of atoms of every element on the left exactly equals the number on the right [1 Mark: Balanced conclusion]."
    )
    return {
        "id": f"ns8_chem_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{breakdown_text}; Yes, equation is balanced because atom counts are equal",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "23_counting_atoms_reactant_side_vs_product_side",
        "misconception_tags": ["counting_atoms_balanced_equations"],
        "hints": {
            "tier_1": "Multiply big coefficients by subscripts to count each atom.",
            "tier_2": f"Counts: {breakdown_text}.",
            "tier_3": f"{breakdown_text}; balanced because left equals right."
        }
    }


def arch_24_particle_model_synthesis_of_water(rng: random.Random) -> Dict[str, Any]:
    c_h, c_o = "#f8fafc", "#ef4444"
    h_r = rng.choice([10, 11])
    o_r = rng.choice([15, 16])
    uid = f"FIG-{rng.randint(100, 999)}"

    svg = (
        f'<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="340" height="140" rx="6" fill="#f8fafc"/>'
        f'<text x="180" y="25" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Water Synthesis: 2H₂ + O₂ → 2H₂O</text>'
        f'<text x="340" y="25" font-family="sans-serif" font-size="8" fill="#94a3b8" text-anchor="end">{uid}</text>'
        # Reactants: 2 H2 molecules + 1 O2 molecule
        f'<rect x="20" y="38" width="140" height="90" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>'
        f'<text x="90" y="52" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Reactants (2H₂ + O₂)</text>'
        # H2 molecule 1
        f'<circle cx="45" cy="75" r="{h_r}" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="62" cy="75" r="{h_r}" fill="{c_h}" stroke="#0f172a"/>'
        # H2 molecule 2
        f'<circle cx="45" cy="105" r="{h_r}" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="62" cy="105" r="{h_r}" fill="{c_h}" stroke="#0f172a"/>'
        # O2 molecule
        f'<circle cx="110" cy="90" r="{o_r}" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="135" cy="90" r="{o_r}" fill="{c_o}" stroke="#0f172a"/>'
        # Arrow
        f'<path d="M 170,85 L 195,85 M 190,80 L 197,85 L 190,90" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        # Products: 2 H2O molecules
        f'<rect x="205" y="38" width="140" height="90" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>'
        f'<text x="275" y="52" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Products (2H₂O)</text>'
        # H2O 1
        f'<circle cx="245" cy="90" r="{o_r}" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="233" cy="77" r="{h_r}" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="257" cy="77" r="{h_r}" fill="{c_h}" stroke="#0f172a"/>'
        # H2O 2
        f'<circle cx="305" cy="90" r="{o_r}" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="293" cy="77" r="{h_r}" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="317" cy="77" r="{h_r}" fill="{c_h}" stroke="#0f172a"/>'
        f'</svg>'
    )

    prompt = (
        f"Examine the particle model diagram representing the formation of water ($2H_2 + O_2 \\rightarrow 2H_2O$).\n\n"
        f"1. How many hydrogen atoms and how many oxygen atoms are present on the reactants side?\n"
        f"2. How many water molecules are formed on the products side?\n"
        f"3. Explain why one molecule of oxygen ($O_2$) requires two molecules of hydrogen ($2H_2$) to react completely."
    )
    sol = (
        f"**Step 1:** There are **4 hydrogen atoms** (two $H_2$ pairs) and **2 oxygen atoms** (one $O_2$ pair) on the reactants side [1 Mark: Reactant counts].\n\n"
        f"**Step 2:** **2 water molecules ($2H_2O$)** are formed [1 Mark: Product molecules].\n\n"
        f"**Step 3:** Each water molecule requires 1 oxygen atom and 2 hydrogen atoms ($H_2O$); since an $O_2$ molecule releases 2 oxygen atoms when broken, it needs **$2 \\times 2 = 4$ hydrogen atoms (two $H_2$ molecules)** to bond with both oxygen atoms [1 Mark: Ratio explanation]."
    )
    return {
        "id": f"ns8_chem_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "4 H atoms and 2 O atoms; 2 water molecules; Each O atom needs 2 H atoms, so 1 O2 molecule requires 2 H2 molecules (4 H atoms)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "24_particle_model_synthesis_of_water",
        "misconception_tags": ["particle_model_water_synthesis"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Count white circles (hydrogen) and red circles (oxygen).",
            "tier_2": "4 white and 2 red make two H2O molecules.",
            "tier_3": "4 H and 2 O atoms; 2 H2O molecules; 1 O2 provides 2 O atoms needing 4 H atoms."
        }
    }


def arch_25_particle_model_combustion_of_methane(rng: random.Random) -> Dict[str, Any]:
    c_c = rng.choice(["#1e293b", "#0f172a", "#334155"])
    c_h = "#f8fafc"
    c_o = rng.choice(["#ef4444", "#dc2626", "#ea580c"])
    uid = f"FIG-{rng.randint(100, 999)}"

    svg = (
        f'<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="340" height="140" rx="6" fill="#f8fafc"/>'
        f'<text x="180" y="24" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Methane Combustion: CH₄ + 2O₂ → CO₂ + 2H₂O</text>'
        f'<text x="340" y="24" font-family="sans-serif" font-size="8" fill="#94a3b8" text-anchor="end">{uid}</text>'
        # Reactants box
        f'<rect x="18" y="36" width="145" height="92" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>'
        f'<text x="90" y="50" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Reactants (CH₄ + 2O₂)</text>'
        # CH4 molecule
        f'<circle cx="50" cy="85" r="14" fill="{c_c}" stroke="#0f172a"/>'
        f'<circle cx="36" cy="72" r="7" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="64" cy="72" r="7" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="36" cy="98" r="7" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="64" cy="98" r="7" fill="{c_h}" stroke="#0f172a"/>'
        # 2 O2 molecules
        f'<circle cx="110" cy="70" r="10" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="127" cy="70" r="10" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="110" cy="100" r="10" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="127" cy="100" r="10" fill="{c_o}" stroke="#0f172a"/>'
        # Arrow
        f'<path d="M 172,85 L 193,85 M 188,80 L 195,85 L 188,90" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        # Products box
        f'<rect x="202" y="36" width="145" height="92" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>'
        f'<text x="275" y="50" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Products (CO₂ + 2H₂O)</text>'
        # CO2
        f'<circle cx="240" cy="85" r="13" fill="{c_c}" stroke="#0f172a"/>'
        f'<circle cx="222" cy="85" r="10" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="258" cy="85" r="10" fill="{c_o}" stroke="#0f172a"/>'
        # 2 H2O
        f'<circle cx="305" cy="70" r="10" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="295" cy="62" r="7" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="315" cy="62" r="7" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="305" cy="105" r="10" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="295" cy="97" r="7" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="315" cy="97" r="7" fill="{c_h}" stroke="#0f172a"/>'
        f'</svg>'
    )

    prompt = (
        f"Examine the particle model diagram representing the combustion of methane gas ($CH_4 + 2O_2 \\rightarrow CO_2 + 2H_2O$).\n\n"
        f"1. How many total atoms are present on the reactants side?\n"
        f"2. How many total atoms are present on the products side?\n"
        f"3. Explain why two molecules of oxygen gas ($2O_2$) are required to burn one molecule of methane completely."
    )
    sol = (
        f"**Step 1:** Reactants side: 1 C + 4 H + 4 O = **9 total atoms** [1 Mark: Reactant total].\n\n"
        f"**Step 2:** Products side: 1 C + 2 O (in $CO_2$) + 4 H + 2 O (in $2H_2O$) = **9 total atoms** [1 Mark: Product total].\n\n"
        f"**Step 3:** Burning 1 carbon atom requires **2 oxygen atoms** (forming $CO_2$), and burning 4 hydrogen atoms requires another **2 oxygen atoms** (forming $2H_2O$). This totals **4 oxygen atoms**, which requires exactly two diatomic oxygen molecules ($2O_2$) [1 Mark: Stoichiometric balance]."
    )
    return {
        "id": f"ns8_chem_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "9 atoms on reactants; 9 atoms on products; 1 C needs 2 O (for CO2) and 4 H need 2 O (for 2H2O), totaling 4 O atoms (2O2 molecules)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "25_particle_model_combustion_of_methane",
        "misconception_tags": ["particle_model_methane_combustion"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Count every circle in the left box and in the right box.",
            "tier_2": "Left has 9 atoms; Right has 9 atoms.",
            "tier_3": "9 atoms on reactants; 9 atoms on products; 4 O atoms needed (2 for CO2, 2 for H2O)."
        }
    }
