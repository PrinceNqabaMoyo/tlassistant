"""Grade 9 Natural Sciences - Chemical Reactions: Archetypes 01 to 25.
Grounded strictly in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 2/01. Chemical reactions.md.

Covers:
- Chemical reactions as formation of new substances with new properties
- Three levels of thinking: Macroscopic, Submicroscopic, Symbolic
- Macroscopic evidence: effervescence, precipitate, temperature change, color change
- Physical vs chemical change, reversibility, and chemical bonding
- Reactants and products, reaction arrow, state symbols ((s), (l), (g), (aq))
- Word equations and particle diagrams showing rearrangement of atoms
- Energy changes: endothermic bond breaking, exothermic bond making
- Limiting vs excess reactants at the particle level
- Subscripts vs coefficients
- Law of Conservation of Atoms and Mass in open vs closed systems
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Foundations & Three Levels of Representation (01 - 09)
# ==============================================================================

def arch_01_chemical_reaction_definition_and_new_substances(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("Combustion of magnesium", "magnesium ribbon + oxygen gas", "white magnesium oxide powder ash", "shiny flexible grey metal turns into a brittle, crumbly white powder with completely different chemical properties"),
        ("Rusting of iron", "iron metal + oxygen + water", "reddish-brown iron(III) oxide (rust)", "strong magnetic grey metal turns into a weak, non-magnetic flaky crumbly powder"),
        ("Thermal decomposition of copper carbonate", "green copper carbonate powder", "black copper oxide powder + carbon dioxide gas", "green solid decomposes into a black solid and a gas that turns limewater milky"),
    ]
    rxn_name, start_mat, end_mat, prop_change = rng.choice(examples)

    prompt = (
        f"In chemistry, a chemical change transforms substances fundamentally.\n\n"
        f"Consider the reaction: **{rxn_name}** ({start_mat} $\\rightarrow$ {end_mat}).\n\n"
        f"1. Define what a **chemical reaction** is in terms of substances and properties.\n"
        f"2. Explain how the macroscopic physical and chemical properties of {end_mat} prove that a true chemical reaction occurred ({prop_change.split(' turns')[0]}).\n"
        f"3. What happened to the chemical bonds between atoms during this process?"
    )
    sol = (
        f"**Step 1:** A **chemical reaction** is a process in which one or more starting substances (reactants) are converted into one or more **new substances (products) with completely new chemical and physical properties** [1 Mark: Definition].\n\n"
        f"**Step 2:** A reaction is proven because {prop_change}; the product is chemically distinct from the starting materials and cannot easily revert [1 Mark: New properties evidence].\n\n"
        f"**Step 3:** The existing chemical bonds in the reactants were **broken**, atoms were rearranged, and **new chemical bonds were formed** to create the products [1 Mark: Bonds broken and formed]."
    )
    return {
        "id": f"ns9_cr_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Chemical reaction = process converting reactants into new substances with new properties; Proven by property change ({prop_change}); Existing bonds broken and new bonds formed",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "01_chemical_reaction_definition_and_new_substances",
        "misconception_tags": ["chemical_reaction_definition_new_substances"],
        "hints": {
            "tier_1": "Chemical reactions form new substances with different properties.",
            "tier_2": "Bonds in reactants break, and new bonds form in products.",
            "tier_3": f"Process forming new substances; {prop_change}; bonds broken and new bonds formed."
        }
    }


def arch_02_three_levels_of_representation_macroscopic_submicroscopic_symbolic(rng: random.Random) -> Dict[str, Any]:
    levels = [
        ("Macroscopic level", "observable phenomena visible to the naked human eye or standard sensors", "seeing effervescent bubbling gas, feeling a beaker become hot, or watching a bright white flame"),
        ("Submicroscopic level", "particle world of individual atoms, ions, and molecules", "visualizing oxygen molecules colliding with magnesium atoms, breaking bonds, and transferring electrons"),
        ("Symbolic level", "chemical shorthand representation using symbols, formulas, and numbers", "writing the chemical equation: 2Mg + O2 -> 2MgO"),
    ]
    lvl_name, lvl_desc, lvl_ex = rng.choice(levels)

    prompt = (
        f"Scientists think about and represent chemical reactions across three distinct levels:\n"
        f"- **Macroscopic level**\n"
        f"- **Submicroscopic level**\n"
        f"- **Symbolic level**\n\n"
        f"1. Explain what is represented at the **{lvl_name}** in science.\n"
        f"2. Give a concrete example of this level for the combustion of magnesium ribbon ({lvl_ex.split(',')[0]}).\n"
        f"3. Why must learners and scientists be able to connect and translate between all three levels?"
    )
    sol = (
        f"**Step 1:** The **{lvl_name}** represents {lvl_desc} [1 Mark: Level definition].\n\n"
        f"**Step 2:** Example: {lvl_ex} [1 Mark: Example].\n\n"
        f"**Step 3:** Connecting all three levels is essential because **submicroscopic atomic rearrangements explain macroscopic laboratory observations**, while the **symbolic level provides the precise universal mathematical language** to calculate and balance reactions [1 Mark: Triplet connection]."
    )
    return {
        "id": f"ns9_cr_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{lvl_name} represents {lvl_desc}; Example: {lvl_ex}; Submicroscopic particles explain macroscopic observations, and symbols provide precise communication",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "02_three_levels_of_representation_macroscopic_submicroscopic_symbolic",
        "misconception_tags": ["three_levels_chemical_representation"],
        "hints": {
            "tier_1": "Macroscopic = visible; Submicroscopic = atoms/molecules; Symbolic = chemical formulas.",
            "tier_2": f"{lvl_name} is about {lvl_desc}.",
            "tier_3": f"{lvl_desc}; {lvl_ex}; links atomic causes to visible observations via formulas."
        }
    }


def arch_03_macroscopic_evidence_of_reaction_gas_precipitate_color_temp(rng: random.Random) -> Dict[str, Any]:
    signs = [
        ("Effervescence / gas production", "Adding zinc metal to hydrochloric acid", "rapid bubbling/fizzing as hydrogen gas is released", "A burning wooden splint at the test tube mouth makes a 'pop' sound"),
        ("Precipitate formation", "Mixing clear lead nitrate and potassium iodide solutions", "a bright yellow insoluble solid (precipitate) clouds the mixture and settles", "The yellow solid is lead iodide, an insoluble ionic crystal"),
        ("Dramatic temperature change (Exothermic)", "Mixing sodium hydroxide solution with hydrochloric acid", "the beaker temperature rises sharply by 15 °C without external heating", "Chemical bond formation releases thermal energy to surroundings"),
        ("Permanent color change", "Heating bright green copper carbonate powder in a dry test tube", "the green powder turns into a deep black solid (copper oxide)", "A new chemical compound with different light absorption is formed"),
    ]
    sign_type, reaction, observation, explanation = rng.choice(signs)

    prompt = (
        f"When investigating chemical changes in a laboratory, scientists look for macroscopic evidence.\n"
        f"Experiment: **{reaction}**.\n\n"
        f"1. State the observable macroscopic sign that indicates a chemical reaction is taking place: **{observation.split(' as')[0]}**.\n"
        f"2. Explain why this observation proves a chemical change occurred rather than a simple physical mixing ({explanation.split(' (')[0]}).\n"
        f"3. Name two other common macroscopic indicators of a chemical reaction."
    )
    sol = (
        f"**Step 1:** Observable sign: **{observation}** ({sign_type}) [1 Mark: Observable sign].\n\n"
        f"**Step 2:** It indicates a chemical reaction because {explanation}; new substances with different physical states, solubilities, or internal energies are formed [1 Mark: Proof of chemical change].\n\n"
        f"**Step 3:** Other indicators: **permanent color change, emission of light/flame, formation of a solid precipitate, or release/absorption of heat** [1 Mark: Any two other indicators]."
    )
    return {
        "id": f"ns9_cr_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{observation}; {explanation}; Other indicators: permanent color change, precipitate formation, temperature change, light emission",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "03_macroscopic_evidence_of_reaction_gas_precipitate_color_temp",
        "misconception_tags": ["macroscopic_reaction_evidence"],
        "hints": {
            "tier_1": "Signs of chemical reaction: gas bubbling, color change, precipitate, heat/light.",
            "tier_2": f"Here, {observation} is seen.",
            "tier_3": f"{observation}; {explanation}; color change, temperature change, precipitate."
        }
    }


def arch_04_physical_change_vs_chemical_change_reversibility_and_bonds(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Boiling water on a stove to produce steam ($H_2O_{(l)} \\rightarrow H_2O_{(g)}$)", "Physical change", "no chemical bonds are broken inside molecules; water molecules remain intact and simply move further apart; easily reversible by cooling/condensation"),
        ("Burning a wooden splint in air to produce ash, smoke, and $CO_2$", "Chemical change", "chemical bonds in cellulose are broken, atoms rearrange with oxygen, and completely new substances are formed; irreversible by simple cooling"),
        ("Dissolving sodium chloride table salt in water", "Physical change", "salt ions separate in water but no new substances are formed; easily reversible by boiling off/evaporating water to recover salt"),
        ("Electrolysis of water using an electric current ($2H_2O \\rightarrow 2H_2 + O_2$)", "Chemical change", "covalent bonds inside water molecules are cleaved, producing new elemental hydrogen and oxygen gases with totally new properties; difficult to reverse physically"),
    ]
    process, change_type, explanation = rng.choice(scenarios)

    prompt = (
        f"Consider the laboratory process:\n"
        f"*{process}*.\n\n"
        f"1. Classify this process as either a **physical change** or a **chemical change**.\n"
        f"2. Explain your classification in terms of **chemical bonds** and whether new substances are formed.\n"
        f"3. Explain the **reversibility** of this process."
    )
    sol = (
        f"**Step 1:** Classification: **{change_type}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Chemical bonds: {explanation.split('; easily')[0].split('; irreversible')[0].split('; difficult')[0]} [1 Mark: Bonding explanation].\n\n"
        f"**Step 3:** Reversibility: {'Easily reversible by physical means (e.g. cooling/evaporating)' if 'Physical' in change_type else 'Difficult or impossible to reverse by simple physical means because new chemical substances were formed'} [1 Mark: Reversibility]."
    )
    return {
        "id": f"ns9_cr_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{change_type}; {explanation.split(';')[0]}; {'Easily reversible physically' if 'Physical' in change_type else 'Not easily reversible physically (chemical change)'}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "04_physical_change_vs_chemical_change_reversibility_and_bonds",
        "misconception_tags": ["physical_vs_chemical_change_criteria"],
        "hints": {
            "tier_1": "Physical changes don't form new substances and are easily reversible.",
            "tier_2": f"This process is a {change_type}.",
            "tier_3": f"{change_type}; bonding explanation; reversibility."
        }
    }


def arch_05_reactants_and_products_identification_left_and_right(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        ("Combustion of methane fuel in a gas burner", "Methane + Oxygen -> Carbon dioxide + Water", "Methane and Oxygen", "Carbon dioxide and Water"),
        ("Neutralization of stomach acid with milk of magnesia", "Hydrochloric acid + Magnesium hydroxide -> Magnesium chloride + Water", "Hydrochloric acid and Magnesium hydroxide", "Magnesium chloride and Water"),
        ("Synthesis of table salt in a fume hood", "Sodium metal + Chlorine gas -> Sodium chloride", "Sodium and Chlorine", "Sodium chloride"),
        ("Rusting of an iron chain outdoors", "Iron + Oxygen + Water -> Hydrated iron(III) oxide (Rust)", "Iron, Oxygen, and Water", "Hydrated iron(III) oxide (Rust)"),
    ]
    context, word_eq, reactants, products = rng.choice(reactions)

    prompt = (
        f"A chemical reaction is described in an experiment:\n"
        f"*{context}*.\n"
        f"Word equation: **{word_eq}**.\n\n"
        f"1. Define the terms **reactant** and **product**.\n"
        f"2. Identify the **reactants** in this reaction, stating which side of the arrow they are written on.\n"
        f"3. Identify the **products** in this reaction, stating which side of the arrow they are written on."
    )
    sol = (
        f"**Step 1:** **Reactants** are the starting substances present before the reaction occurs; **Products** are the new chemical substances formed as a result of the reaction [1 Mark: Definitions].\n\n"
        f"**Step 2:** Reactants: **{reactants}** (written on the **left side** of the arrow) [1 Mark: Reactants and left side].\n\n"
        f"**Step 3:** Products: **{products}** (written on the **right side** of the arrow) [1 Mark: Products and right side]."
    )
    return {
        "id": f"ns9_cr_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Reactants = starting substances, Products = new substances formed; Reactants: {reactants} (left); Products: {products} (right)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "05_reactants_and_products_identification_left_and_right",
        "misconception_tags": ["reactants_and_products_convention"],
        "hints": {
            "tier_1": "Reactants are on the left, products on the right.",
            "tier_2": f"Reactants = {reactants}; Products = {products}.",
            "tier_3": "Definitions; Reactants on left; Products on right."
        }
    }


def arch_06_the_reaction_arrow_yields_meaning_and_direction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In all chemical reaction equations, an arrow ($\\rightarrow$) is written between reactants and products:\n"
        "$$\\text{Reactants} \\rightarrow \\text{Products}$$\n\n"
        "1. What does the reaction arrow ($\\rightarrow$) literally mean in scientific terminology?\n"
        "2. Why is an arrow used instead of an equals sign ($=$) in chemical equations?\n"
        "3. What does a double reversible arrow ($\\rightleftharpoons$) indicate when written in advanced chemical reactions?"
    )
    sol = (
        f"**Step 1:** The arrow means **'reacts to form'**, **'yields'**, or **'produces'**; it indicates the forward direction of chemical change [1 Mark: Arrow meaning].\n\n"
        f"**Step 2:** An arrow is used rather than an equals sign because the **reactants and products are chemically distinct substances with different properties**; they are not identical entities, but rather reactants transform into products [1 Mark: Arrow vs equals sign].\n\n"
        f"**Step 3:** A double reversible arrow ($\\rightleftharpoons$) indicates that the reaction is **reversible**, occurring simultaneously in both the forward and reverse directions (chemical equilibrium) [1 Mark: Reversible arrow]."
    )
    return {
        "id": f"ns9_cr_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Arrow means 'reacts to form' or 'yields' (direction of change); Arrow shows transformation into new substances (not identical mathematical equality); Double arrow indicates a reversible reaction",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "06_the_reaction_arrow_yields_meaning_and_direction",
        "misconception_tags": ["reaction_arrow_scientific_meaning"],
        "hints": {
            "tier_1": "Arrow means 'yields' or 'reacts to produce'.",
            "tier_2": "Reactants are converted into new products, which is why = is not used.",
            "tier_3": "'Reacts to form' / yields; represents transformation into different substances; reversible reaction."
        }
    }


def arch_07_state_symbols_solid_liquid_gas_aqueous_definitions(rng: random.Random) -> Dict[str, Any]:
    symbols = [
        ("(s)", "Solid", "pure solid element or precipitate crystal lattice", "Mg(s), NaCl(s)"),
        ("(l)", "Liquid", "pure substance in liquid state", "H2O(l), Br2(l)"),
        ("(g)", "Gas", "substance in vapor or gaseous phase", "O2(g), CO2(g), H2(g)"),
        ("(aq)", "Aqueous solution", "substance dissolved in water solvent", "HCl(aq), NaCl(aq), NaOH(aq)"),
    ]
    symb, state_name, meaning, examples = rng.choice(symbols)

    prompt = (
        f"Chemical equations often include **state symbols** in brackets after each formula.\n\n"
        f"1. What physical state of matter does the symbol **{symb}** represent ({state_name})?\n"
        f"2. Explain the crucial difference between the state symbol **(l)** and the state symbol **(aq)**.\n"
        f"3. Write out the four standard state symbols and their meanings."
    )
    sol = (
        f"**Step 1:** The symbol **{symb}** represents **{state_name}** ({meaning}) [1 Mark: State symbol].\n\n"
        f"**Step 2:** **(l)** represents a **pure liquid substance** (e.g. pure molten liquid or pure liquid water $H_2O_{{(l)}}$); **(aq)** means **aqueous**, meaning a substance is **dissolved in water to form a solution** (e.g. $NaCl_{{(aq)}}$) [1 Mark: (l) vs (aq) difference].\n\n"
        f"**Step 3:** The four symbols are: **(s) = solid**, **(l) = liquid**, **(g) = gas**, and **(aq) = aqueous solution** [1 Mark: Four state symbols]."
    )
    return {
        "id": f"ns9_cr_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{symb} = {state_name}; (l) is a pure liquid, whereas (aq) is a substance dissolved in water; (s)=solid, (l)=liquid, (g)=gas, (aq)=aqueous",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "07_state_symbols_solid_liquid_gas_aqueous_definitions",
        "misconception_tags": ["state_symbols_liquid_vs_aqueous"],
        "hints": {
            "tier_1": "aq stands for aqueous, meaning dissolved in water.",
            "tier_2": "l = pure liquid, s = solid, g = gas, aq = dissolved in water.",
            "tier_3": f"{symb} = {state_name}; pure liquid vs dissolved in water; s, l, g, aq."
        }
    }


def arch_08_translating_word_equations_to_unbalanced_chemical_equations(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        (
            "Hydrogen gas reacts with oxygen gas to form liquid water",
            "Hydrogen + Oxygen -> Water",
            "H2 + O2 -> H2O",
            "Hydrogen (H2) and Oxygen (O2) are diatomic elements"
        ),
        (
            "Magnesium metal burns in oxygen gas to produce magnesium oxide powder",
            "Magnesium + Oxygen -> Magnesium oxide",
            "Mg + O2 -> MgO",
            "Oxygen (O2) is diatomic, while magnesium oxide has formula MgO"
        ),
        (
            "Carbon solid reacts with oxygen gas to form carbon dioxide gas",
            "Carbon + Oxygen -> Carbon dioxide",
            "C + O2 -> CO2",
            "Carbon is C, oxygen is O2, and carbon dioxide is CO2"
        ),
        (
            "Zinc metal reacts with hydrochloric acid to produce zinc chloride and hydrogen gas",
            "Zinc + Hydrochloric acid -> Zinc chloride + Hydrogen",
            "Zn + HCl -> ZnCl2 + H2",
            "Zinc chloride has formula ZnCl2, and hydrogen gas is diatomic H2"
        ),
    ]
    narrative, word_eq, chem_eq, rule_note = rng.choice(reactions)

    prompt = (
        f"A chemist records a chemical reaction in the laboratory:\n"
        f"*'{narrative}'*.\n\n"
        f"1. Write down the complete **word equation** for this reaction.\n"
        f"2. Translate the word equation into an **unbalanced chemical equation using chemical formulas** ({chem_eq}).\n"
        f"3. Explain why elemental non-metal gases like oxygen or hydrogen must be written with subscript 2 in chemical equations."
    )
    sol = (
        f"**Step 1:** Word equation: **{word_eq}** [1 Mark: Word equation].\n\n"
        f"**Step 2:** Chemical equation: **{chem_eq}** [1 Mark: Chemical equation].\n\n"
        f"**Step 3:** They must be written with subscript 2 because they naturally exist as **diatomic molecules** (pairs of chemically bonded atoms, such as $H_2$ and $O_2$) under standard conditions [1 Mark: Diatomic explanation]."
    )
    return {
        "id": f"ns9_cr_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Word equation: {word_eq}; Chemical equation: {chem_eq}; Written with subscript 2 because they are diatomic molecules (exist in pairs)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "08_translating_word_equations_to_unbalanced_chemical_equations",
        "misconception_tags": ["word_equation_to_symbol_equation"],
        "hints": {
            "tier_1": "Remember that oxygen is O2 and hydrogen is H2.",
            "tier_2": f"Word equation is {word_eq}. Symbols: {chem_eq}.",
            "tier_3": f"{word_eq}; {chem_eq}; diatomic molecules."
        }
    }


def arch_09_particle_model_diagram_rearrangement_of_atoms(rng: random.Random) -> Dict[str, Any]:
    c_c = rng.choice(["#1e293b", "#0f172a", "#334155"])
    c_o = rng.choice(["#ef4444", "#dc2626", "#ea580c"])
    uid = f"FIG-{rng.randint(100, 999)}"

    svg = (
        f'<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="340" height="140" rx="6" fill="#f8fafc"/>'
        f'<text x="180" y="24" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Rearrangement of Atoms: C + O₂ → CO₂</text>'
        f'<text x="340" y="24" font-family="sans-serif" font-size="8" fill="#94a3b8" text-anchor="end">{uid}</text>'
        # Reactants
        f'<rect x="25" y="38" width="130" height="90" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="90" y="52" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Reactants</text>'
        f'<circle cx="55" cy="85" r="14" fill="{c_c}" stroke="#0f172a"/>'
        f'<text x="55" y="89" font-family="sans-serif" font-size="9" fill="#ffffff" text-anchor="middle">C</text>'
        f'<circle cx="100" cy="85" r="12" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="120" cy="85" r="12" fill="{c_o}" stroke="#0f172a"/>'
        f'<text x="100" y="89" font-family="sans-serif" font-size="8" fill="#ffffff" text-anchor="middle">O</text>'
        f'<text x="120" y="89" font-family="sans-serif" font-size="8" fill="#ffffff" text-anchor="middle">O</text>'
        # Arrow
        f'<path d="M 165,85 L 195,85 M 190,80 L 197,85 L 190,90" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        # Products
        f'<rect x="205" y="38" width="130" height="90" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="270" y="52" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Products</text>'
        f'<circle cx="270" cy="85" r="14" fill="{c_c}" stroke="#0f172a"/>'
        f'<circle cx="250" cy="85" r="12" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="290" cy="85" r="12" fill="{c_o}" stroke="#0f172a"/>'
        f'<text x="270" y="89" font-family="sans-serif" font-size="9" fill="#ffffff" text-anchor="middle">C</text>'
        f'<text x="250" y="89" font-family="sans-serif" font-size="8" fill="#ffffff" text-anchor="middle">O</text>'
        f'<text x="290" y="89" font-family="sans-serif" font-size="8" fill="#ffffff" text-anchor="middle">O</text>'
        f'<text x="180" y="145" font-family="sans-serif" font-size="9" fill="#64748b" text-anchor="middle">Bonds broken in O₂; new C-O bonds formed in CO₂</text>'
        f'</svg>'
    )

    prompt = (
        f"Examine the particle model diagram showing the combustion reaction $C + O_2 \\rightarrow CO_2$.\n\n"
        f"1. Name the chemical bonds that must be **broken** in the reactants for this reaction to take place.\n"
        f"2. Name the new chemical bonds that are **formed** in the product.\n"
        f"3. Explain why the total mass of the reactants equals the total mass of the products based on the diagram."
    )
    sol = (
        f"**Step 1:** The chemical bond inside the **diatomic oxygen molecule ($O=O$ covalent double bond)** must be broken [1 Mark: Bonds broken].\n\n"
        f"**Step 2:** Two **new carbon-oxygen bonds ($C=O$)** are formed in the carbon dioxide molecule ($CO_2$) [1 Mark: Bonds formed].\n\n"
        f"**Step 3:** The masses are equal because **no atoms are created or destroyed**; exactly the same 1 carbon atom and 2 oxygen atoms exist before and after the reaction, merely rearranged into a new compound [1 Mark: Conservation of atoms/mass]."
    )
    return {
        "id": f"ns9_cr_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Bonds broken: covalent bond in O2 molecule; Bonds formed: new C-O bonds in CO2; Masses equal because identical atoms are conserved before and after reaction",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "09_particle_model_diagram_rearrangement_of_atoms",
        "misconception_tags": ["particle_diagram_atomic_rearrangement"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "O2 splits apart; then oxygen attaches to carbon.",
            "tier_2": "Bonds in O2 break; new C-O bonds form. Atom count stays at 1 C and 2 O.",
            "tier_3": "O2 bond broken; C-O bonds formed; mass conserved because atom numbers are unchanged."
        }
    }


# ==============================================================================
# CLUSTER 2: Submicroscopic Atomic Rearrangement & Energy Changes (10 - 18)
# ==============================================================================

def arch_10_atomic_rearrangement_concept_no_new_atoms_created(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A common misconception among beginner science students is that chemical reactions create new atoms.\n\n"
        f"1. Explain scientifically what actually happens to atoms during a chemical reaction.\n"
        f"2. Can an atom of carbon ever turn into an atom of gold or oxygen during a chemical reaction? Explain.\n"
        f"3. State the universal scientific law that forbids the creation or destruction of atoms during chemical changes."
    )
    sol = (
        f"**Step 1:** During a chemical reaction, **atoms are merely rearranged**; existing chemical bonds break and new chemical bonds form between the same atoms [1 Mark: Rearrangement of atoms].\n\n"
        f"**Step 2:** **No**; chemical reactions only rearrange outer electrons and chemical bonds; the atomic nucleus (number of protons) is never altered in chemical reactions, so an element's identity cannot change [1 Mark: Element identity fixed].\n\n"
        f"**Step 3:** The law is the **Law of Conservation of Atoms / Law of Conservation of Mass** [1 Mark: Law of Conservation of Atoms]."
    )
    return {
        "id": f"ns9_cr_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Atoms are merely rearranged (bonds break and form); No, atomic nuclei are unaffected in chemical changes so elements cannot transmute; Law of Conservation of Atoms / Mass",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "10_atomic_rearrangement_concept_no_new_atoms_created",
        "misconception_tags": ["atoms_rearranged_not_created"],
        "hints": {
            "tier_1": "Chemical reactions only rearrange existing atoms; they do not change the nucleus.",
            "tier_2": "Carbon cannot change into gold in chemical reactions.",
            "tier_3": "Rearranged only; No (nucleus unchanged); Law of Conservation of Atoms."
        }
    }


def arch_11_bond_breaking_requires_energy_endothermic_step(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Every chemical reaction involves an energy exchange during bond reorganization.\n\n"
        f"1. Does breaking chemical bonds in the reactant molecules **require (absorb) energy** or **release energy**?\n"
        f"2. Use the analogy of separating two strong bar magnets to explain why bond breaking requires energy.\n"
        f"3. What scientific term describes a chemical step or reaction that absorbs thermal energy from its surroundings?"
    )
    sol = (
        f"**Step 1:** Breaking chemical bonds always **requires (absorbs) energy** from the surroundings [1 Mark: Energy absorbed].\n\n"
        f"**Step 2:** Magnet analogy: When two opposite magnetic poles stick tightly together, a person must **exert a pulling force and do work (input energy)** to separate them; similarly, inputting energy is required to overcome the electrostatic attraction between bonded atoms [1 Mark: Magnet analogy].\n\n"
        f"**Step 3:** The scientific term is **endothermic** ($endo = internal/into$, $thermic = heat$) [1 Mark: Endothermic term]."
    )
    return {
        "id": f"ns9_cr_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Bond breaking absorbs (requires) energy; Like pulling magnets apart, work/energy must be inputted to overcome attraction; Endothermic",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "11_bond_breaking_requires_energy_endothermic_step",
        "misconception_tags": ["bond_breaking_requires_energy"],
        "hints": {
            "tier_1": "You have to put energy in to break things apart (like magnets).",
            "tier_2": "Bond breaking is endothermic.",
            "tier_3": "Requires energy; pull magnets apart; endothermic."
        }
    }


def arch_12_bond_making_releases_energy_exothermic_step(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The second fundamental step of any chemical reaction is the formation of new chemical bonds.\n\n"
        f"1. Does the formation of new chemical bonds in product molecules **absorb energy** or **release energy**?\n"
        f"2. Explain why atoms release energy when they form a stable chemical bond in terms of stability.\n"
        f"3. What scientific term describes a chemical step or reaction that releases energy to the surroundings, causing the temperature to rise?"
    )
    sol = (
        f"**Step 1:** Forming new chemical bonds always **releases energy** to the surroundings [1 Mark: Energy released].\n\n"
        f"**Step 2:** Atoms form bonds to achieve a **more stable, lower potential energy state** (often completing full valence shells); the excess potential energy lost by the atoms is released as thermal/radiant energy [1 Mark: Lower energy and stability].\n\n"
        f"**Step 3:** The term is **exothermic** ($exo = exit/out$, $thermic = heat$) [1 Mark: Exothermic term]."
    )
    return {
        "id": f"ns9_cr_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Bond making releases energy; Atoms move to a lower potential energy state (greater stability), releasing excess energy; Exothermic",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "12_bond_making_releases_energy_exothermic_step",
        "misconception_tags": ["bond_making_releases_energy"],
        "hints": {
            "tier_1": "Bond making releases energy as atoms reach a more stable state.",
            "tier_2": "Heat released = exothermic.",
            "tier_3": "Releases energy; lower potential energy / greater stability; exothermic."
        }
    }


def arch_13_exothermic_vs_endothermic_reactions_overall_energy_balance(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (
            "Combustion of magnesium ribbon in air ($2Mg + O_2 \\rightarrow 2MgO$)",
            "Exothermic",
            "blinding white light and intense heat emitted; temperature of surroundings increases",
            "Energy released forming new Mg-O bonds is GREATER than energy absorbed breaking bonds"
        ),
        (
            "Dissolving ammonium nitrate fertilizer in water (instant cold pack)",
            "Endothermic",
            "pack temperature drops rapidly from 22 °C to 4 °C; feels icy cold to touch",
            "Energy absorbed breaking bonds/crystal lattice is GREATER than energy released hydrating ions"
        ),
        (
            "Reaction of vinegar with baking soda ($CH_3COOH + NaHCO_3$)",
            "Endothermic",
            "effervescent fizzing accompanied by a measurable drop in beaker temperature of 4 °C",
            "Energy absorbed breaking reactant bonds exceeds energy released forming product bonds"
        ),
    ]
    name, classification, observation, balance_reason = rng.choice(cases)

    prompt = (
        f"Consider the chemical reaction:\n"
        f"**{name}**.\n"
        f"- Observation: {observation}.\n\n"
        f"1. Classify this reaction as either **exothermic** or **endothermic**.\n"
        f"2. Explain this classification in terms of the energy balance between **bond breaking** and **bond making** ({balance_reason.split(' is ')[0]}).\n"
        f"3. In this reaction, does the temperature of the immediate surroundings increase, decrease, or remain unchanged?"
    )
    temp_dir = "increases (feels hot/warm)" if classification == "Exothermic" else "decreases (feels cold/cool)"

    sol = (
        f"**Step 1:** Classification: **{classification}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Energy balance: **{balance_reason}** [1 Mark: Energy balance].\n\n"
        f"**Step 3:** The temperature of the surroundings **{temp_dir}** [1 Mark: Temperature direction]."
    )
    return {
        "id": f"ns9_cr_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{classification}; {balance_reason}; Temperature {temp_dir}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "13_exothermic_vs_endothermic_reactions_overall_energy_balance",
        "misconception_tags": ["exothermic_vs_endothermic_balance"],
        "hints": {
            "tier_1": "Exothermic releases heat (gets hotter). Endothermic absorbs heat (gets colder).",
            "tier_2": f"Here, {classification} is correct.",
            "tier_3": f"{classification}; {balance_reason}; temperature {temp_dir}."
        }
    }


def arch_14_limiting_reactants_and_excess_reactants_particle_view(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "Making cheese sandwiches: Recipe requires 2 slices of bread + 1 slice of cheese. You have 10 slices of bread and 3 slices of cheese.",
            "Cheese", "Bread",
            3, 4,
            "Cheese runs out first (after making 3 sandwiches), leaving 4 unused slices of bread behind"
        ),
        (
            "Combustion of charcoal: Burning 50 carbon atoms in a sealed jar containing only 10 oxygen molecules ($O_2$). Reaction: $C + O_2 \\rightarrow CO_2$.",
            "Oxygen ($O_2$)", "Carbon ($C$)",
            10, 40,
            "Oxygen runs out after forming 10 CO2 molecules, leaving 40 unreacted carbon atoms in excess"
        ),
        (
            "Synthesis of water: Mixing 10 molecules of hydrogen ($H_2$) with 2 molecules of oxygen ($O_2$). Reaction: $2H_2 + O_2 \\rightarrow 2H_2O$.",
            "Oxygen ($O_2$)", "Hydrogen ($H_2$)",
            4, 6,
            "2 molecules of O2 require only 4 molecules of H2, leaving 6 unreacted H2 molecules in excess"
        ),
    ]
    context, limiting, excess, n_prod, n_left, explanation = rng.choice(scenarios)

    prompt = (
        f"Chemical reactions depend on the stoichiometric availability of reactant particles.\n\n"
        f"Consider the scenario:\n"
        f"*{context}*\n\n"
        f"1. Identify the **limiting reactant** and the **excess reactant**.\n"
        f"2. How many product units are formed ({n_prod}), and how many excess reactant units remain unreacted ({n_left})?\n"
        f"3. Explain why the limiting reactant determines the maximum amount of product that can be formed."
    )
    sol = (
        f"**Step 1:** Limiting reactant: **{limiting}**; Excess reactant: **{excess}** [1 Mark: Reactants identified].\n\n"
        f"**Step 2:** Formed: **{n_prod} product units**; Unreacted leftover: **{n_left} units of {excess}** [1 Mark: Numerical amounts].\n\n"
        f"**Step 3:** The limiting reactant **runs out first**; once it is completely consumed, the chemical reaction must immediately stop because an essential reactant is no longer available [1 Mark: Limiting reactant role]."
    )
    return {
        "id": f"ns9_cr_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Limiting: {limiting}, Excess: {excess}; {n_prod} formed, {n_left} unreacted; Reaction stops when limiting reactant is completely consumed",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "14_limiting_reactants_and_excess_reactants_particle_view",
        "misconception_tags": ["limiting_vs_excess_reactants"],
        "hints": {
            "tier_1": "The reactant that runs out first is limiting.",
            "tier_2": f"Limiting is {limiting}. Leftover is {n_left}.",
            "tier_3": f"Limiting: {limiting}; {n_prod} formed, {n_left} left; reaction stops when limiting runs out."
        }
    }


def arch_15_particle_diagram_counting_reactant_vs_product_molecules(rng: random.Random) -> Dict[str, Any]:
    c_h = "#f8fafc"
    c_o = rng.choice(["#ef4444", "#dc2626", "#ea580c"])
    uid = f"MOD-{rng.randint(100, 999)}"

    svg = (
        f'<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="340" height="140" rx="6" fill="#f8fafc"/>'
        f'<text x="180" y="24" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Synthesis of Water: 2H₂ + O₂ → 2H₂O</text>'
        f'<text x="340" y="24" font-family="sans-serif" font-size="8" fill="#94a3b8" text-anchor="end">{uid}</text>'
        # Reactants box
        f'<rect x="20" y="36" width="140" height="92" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="90" y="50" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Reactants (2H₂ + O₂)</text>'
        # 2 H2 molecules
        f'<circle cx="45" cy="72" r="10" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="62" cy="72" r="10" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="45" cy="102" r="10" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="62" cy="102" r="10" fill="{c_h}" stroke="#0f172a"/>'
        # 1 O2 molecule
        f'<circle cx="115" cy="87" r="14" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="138" cy="87" r="14" fill="{c_o}" stroke="#0f172a"/>'
        # Arrow
        f'<path d="M 168,85 L 192,85 M 187,80 L 194,85 L 187,90" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        # Products box
        f'<rect x="200" y="36" width="140" height="92" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="270" y="50" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Products (2H₂O)</text>'
        # 2 H2O molecules
        f'<circle cx="240" cy="87" r="14" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="228" cy="75" r="9" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="252" cy="75" r="9" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="295" cy="87" r="14" fill="{c_o}" stroke="#0f172a"/>'
        f'<circle cx="283" cy="75" r="9" fill="{c_h}" stroke="#0f172a"/>'
        f'<circle cx="307" cy="75" r="9" fill="{c_h}" stroke="#0f172a"/>'
        f'</svg>'
    )

    prompt = (
        f"Examine the particle model diagram representing the chemical synthesis of water.\n\n"
        f"1. How many molecules of hydrogen ($H_2$) and how many molecules of oxygen ($O_2$) are shown in the reactants box?\n"
        f"2. How many water molecules ($H_2O$) are formed in the products box?\n"
        f"3. Total the number of hydrogen atoms and oxygen atoms on both sides to verify that atoms are conserved."
    )
    sol = (
        f"**Step 1:** Reactants box: **2 molecules of hydrogen ($2H_2$)** and **1 molecule of oxygen ($1O_2$)** [1 Mark: Reactant molecule counts].\n\n"
        f"**Step 2:** Products box: **2 molecules of water ($2H_2O$)** [1 Mark: Product molecule count].\n\n"
        f"**Step 3:** Atom counts on both sides:\n"
        f"- Reactants: $2 \\times 2 = 4\\text{{ H atoms}}$, $1 \\times 2 = 2\\text{{ O atoms}}$\n"
        f"- Products: $2 \\times 2 = 4\\text{{ H atoms}}$, $2 \\times 1 = 2\\text{{ O atoms}}$\n"
        f"Both sides have identical counts (4 H and 2 O), confirming atom conservation [1 Mark: Atom verification]."
    )
    return {
        "id": f"ns9_cr_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Reactants: 2 H2 molecules and 1 O2 molecule; Products: 2 H2O molecules; Conservation: 4 H atoms and 2 O atoms on each side",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "15_particle_diagram_counting_reactant_vs_product_molecules",
        "misconception_tags": ["particle_diagram_molecule_vs_atom_count"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Count the molecules (clusters) and then count individual circles (atoms).",
            "tier_2": "2 H2 + 1 O2 -> 2 H2O.",
            "tier_3": "2 H2, 1 O2; 2 H2O; 4 H and 2 O on both sides."
        }
    }


def arch_16_particle_diagram_identifying_unreacted_excess_atoms(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A closed reaction chamber contains 8 hydrogen gas molecules ($8H_2$) and 3 oxygen gas molecules ($3O_2$).\n"
        f"They react according to: $2H_2 + O_2 \\rightarrow 2H_2O$.\n\n"
        f"1. How many water molecules ($H_2O$) can be formed at most from this mixture?\n"
        f"2. Which reactant is in **excess**, and how many molecules of this excess reactant remain unreacted?\n"
        f"3. Explain why the reaction ceased even though there were still unreacted particles in the container."
    )
    # 3 O2 needs 6 H2, produces 6 H2O; 2 H2 leftover
    sol = (
        f"**Step 1:** Each $O_2$ molecule requires $2H_2$ molecules to produce $2H_2O$. With 3 $O_2$ molecules, exactly $3 \\times 2 = 6\\text{{ molecules of }} H_2$ are consumed, producing **6 water molecules ($6H_2O$)** [1 Mark: Product molecules].\n\n"
        f"**Step 2:** **Hydrogen ($H_2$) is in excess**; leftover hydrogen = $8 - 6 =$ **2 unreacted $H_2$ molecules** [1 Mark: Excess leftover].\n\n"
        f"**Step 3:** The reaction ceased because **oxygen ($O_2$) was the limiting reactant and was completely exhausted**; hydrogen molecules have no oxygen atoms left to react with [1 Mark: Reason reaction stopped]."
    )
    return {
        "id": f"ns9_cr_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "6 water molecules formed; Hydrogen is in excess, with 2 H2 molecules leftover; Reaction stopped because limiting reactant (oxygen) was completely consumed",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "16_particle_diagram_identifying_unreacted_excess_atoms",
        "misconception_tags": ["excess_reactant_calculation"],
        "hints": {
            "tier_1": "3 O2 needs 6 H2. You have 8 H2.",
            "tier_2": "6 H2O made, 2 H2 left over.",
            "tier_3": "6 H2O formed; H2 excess (2 molecules leftover); oxygen was exhausted."
        }
    }


def arch_17_subscripts_indicate_atoms_per_molecule_immutable(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("H2O", "water", "H2O2", "hydrogen peroxide"),
        ("CO", "carbon monoxide", "CO2", "carbon dioxide"),
        ("SO2", "sulfur dioxide", "SO3", "sulfur trioxide"),
    ]
    f1, n1, f2, n2 = rng.choice(examples)

    prompt = (
        f"In chemical equations, numbers appear as either **subscripts** or **coefficients**.\n\n"
        f"1. What does a **subscript** (the small number at the bottom right of an element symbol) signify?\n"
        f"2. Why is changing a subscript strictly forbidden when balancing a chemical equation?\n"
        f"3. Using **{f1}** ({n1}) and **{f2}** ({n2}) as an example, show how changing a subscript alters the substance's chemical identity."
    )
    sol = (
        f"**Step 1:** A **subscript** indicates the **fixed number of atoms of that element chemically bonded** within a single molecule or formula unit [1 Mark: Subscript meaning].\n\n"
        f"**Step 2:** Changing a subscript is forbidden because it **changes the chemical formula and creates a completely different chemical compound**, violating the reality of the reaction [1 Mark: Subscripts immutable].\n\n"
        f"**Step 3:** Example: Changing {f1} to {f2} changes harmless **{n1}** into **{n2}**, which is a totally different substance with different chemical and biological properties [1 Mark: Example comparison]."
    )
    return {
        "id": f"ns9_cr_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Subscript = fixed number of bonded atoms in a molecule; Changing it alters the chemical identity of the substance; Example: {f1} ({n1}) becomes {f2} ({n2})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "17_subscripts_indicate_atoms_per_molecule_immutable",
        "misconception_tags": ["subscript_immutability_rule"],
        "hints": {
            "tier_1": "Never change small subscript numbers!",
            "tier_2": "Changing subscripts creates a new chemical compound.",
            "tier_3": f"Fixed bonded atoms; changes identity; {f1} ({n1}) vs {f2} ({n2})."
        }
    }


def arch_18_coefficients_indicate_number_of_particles_adjustable(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("2H2O", "Water", 2, "2 molecules of water", 4, 2),
        ("3CO2", "Carbon dioxide", 3, "3 molecules of carbon dioxide", 3, 6),
        ("2NH3", "Ammonia", 2, "2 molecules of ammonia", 2, 6),
        ("4Fe", "Iron", 4, "4 individual iron atoms", 4, 0),
    ]
    formula_str, comp_name, coeff, meaning, n_first, n_second = rng.choice(examples)

    prompt = (
        f"Consider the chemical expression: **{formula_str}**.\n\n"
        f"1. What is the large number '{coeff}' written in front of the chemical formula called?\n"
        f"2. What does this coefficient signify at the particle level ({meaning})?\n"
        f"3. Calculate the total number of atoms of each element represented in **{formula_str}**."
    )
    sol = (
        f"**Step 1:** The number is called a **stoichiometric coefficient** (or coefficient) [1 Mark: Coefficient name].\n\n"
        f"**Step 2:** It signifies the **number of separate, independent molecules (or formula units/atoms)** of that substance reacting or produced [1 Mark: Particle meaning].\n\n"
        f"**Step 3:** Total atoms: The coefficient multiplies every subscript in the formula: **{n_first} atoms of the first element** and **{n_second} atoms of the second element** [1 Mark: Atom calculation]."
    )
    return {
        "id": f"ns9_cr_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Stoichiometric coefficient; Represents {meaning}; Total atoms: {n_first} and {n_second}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "18_coefficients_indicate_number_of_particles_adjustable",
        "misconception_tags": ["coefficient_multiplication_rule"],
        "hints": {
            "tier_1": "The big number in front is a coefficient. It multiplies everything that follows.",
            "tier_2": f"There are {meaning}.",
            "tier_3": f"Coefficient; {meaning}; {n_first} and {n_second} atoms."
        }
    }


# ==============================================================================
# CLUSTER 3: Law of Conservation of Mass & Atoms (19 - 25)
# ==============================================================================

def arch_19_law_of_conservation_of_atoms_principle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The Law of Conservation of Atoms is the cornerstone of chemical reaction theory.\n\n"
        f"1. State the **Law of Conservation of Atoms**.\n"
        f"2. How does this law explain why the mass of reactants always equals the mass of products in a closed system?\n"
        f"3. If a student claims that an atom was destroyed when a candle completely burns away to nothing, refute their statement scientifically."
    )
    sol = (
        f"**Step 1:** The **Law of Conservation of Atoms** states that in any chemical reaction, **atoms cannot be created or destroyed**; they can only be rearranged [1 Mark: Law definition].\n\n"
        f"**Step 2:** Because each specific atom has a definite, unchanging mass, and the total number and types of atoms are identical before and after the reaction, the **total mass must remain completely unchanged** [1 Mark: Mass conservation link].\n\n"
        f"**Step 3:** Refutation: No atoms were destroyed; the wax hydrocarbon reacted with atmospheric oxygen to form **invisible carbon dioxide gas ($CO_2$) and water vapor ($H_2O$)**, which escaped into the air. If collected in a closed container, the total mass would be identical [1 Mark: Candle wax explanation]."
    )
    return {
        "id": f"ns9_cr_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Atoms cannot be created or destroyed, only rearranged; Mass is conserved because identical atoms with fixed masses exist before and after; No atoms destroyed in candle: escaped as invisible CO2 gas and water vapor",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "19_law_of_conservation_of_atoms_principle",
        "misconception_tags": ["conservation_of_atoms_principle"],
        "hints": {
            "tier_1": "Atoms can never be created or destroyed in chemical reactions.",
            "tier_2": "The candle burned into invisible gases (CO2 and water vapor).",
            "tier_3": "Cannot be created or destroyed; identical atom masses; escaped as invisible gases."
        }
    }


def arch_20_law_of_conservation_of_mass_closed_system(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        ("Precipitation of barium sulfate", "BaCl2(aq) + Na2SO4(aq) -> BaSO4(s) + 2NaCl(aq)", 150.5, 150.5),
        ("Vinegar and baking soda in a sealed flask with balloon", "CH3COOH + NaHCO3 -> CH3COONa + H2O + CO2", 235.8, 235.8),
        ("Precipitation of silver chloride", "AgNO3(aq) + NaCl(aq) -> AgCl(s) + NaNO3(aq)", 182.4, 182.4),
    ]
    name, eq, m_initial, m_final = rng.choice(reactions)

    prompt = (
        f"An experiment is conducted in a tightly sealed, airtight conical flask (**closed system**):\n"
        f"- **Reaction:** {name} ({eq}).\n"
        f"- **Initial mass of sealed flask + reactants:** {m_initial} g.\n\n"
        f"1. Predict the final mass of the sealed flask + products after the reaction is complete ({m_final} g).\n"
        f"2. Explain why a **closed system** is strictly necessary to experimentally demonstrate the Law of Conservation of Mass.\n"
        f"3. State the Law of Conservation of Mass."
    )
    sol = (
        f"**Step 1:** The final mass is **{m_final} g** (exactly identical to the initial mass) [1 Mark: Final mass].\n\n"
        f"**Step 2:** A closed system is necessary because it **prevents any gaseous reactants or products from entering or escaping** the system; all matter is contained [1 Mark: Closed system necessity].\n\n"
        f"**Step 3:** The **Law of Conservation of Mass** states that in a closed system, the total mass of the products equals the total mass of the reactants ($M_{{reactants}} = M_{{products}}$) [1 Mark: Law of Conservation of Mass]."
    )
    return {
        "id": f"ns9_cr_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Final mass = {m_final} g; Closed system prevents gases from escaping or entering; Total mass of products equals total mass of reactants in a closed system",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "20_law_of_conservation_of_mass_closed_system",
        "misconception_tags": ["conservation_of_mass_closed_system"],
        "hints": {
            "tier_1": "Mass in a closed system never changes.",
            "tier_2": f"Mass is {m_final} g.",
            "tier_3": f"{m_final} g; prevents matter escaping; total mass reactants = total mass products."
        }
    }


def arch_21_apparent_mass_loss_in_open_system_gas_escape(rng: random.Random) -> Dict[str, Any]:
    m_react = rng.choice([120.0, 150.0, 200.0])
    gas_mass = rng.choice([4.4, 8.8, 11.0])
    m_remain = round(m_react - gas_mass, 1)

    prompt = (
        f"A student reacts marble chips (calcium carbonate, $CaCO_3$) with dilute hydrochloric acid ($HCl$) in an **open beaker** placed on an electronic balance:\n"
        f"- **Initial mass of beaker + reactants:** {m_react} g.\n"
        f"- **Final mass of beaker after bubbling ceased:** {m_remain} g.\n\n"
        f"1. Calculate the apparent loss of mass from the beaker ({gas_mass} g).\n"
        f"2. Has matter been destroyed in this reaction, violating the Law of Conservation of Mass? Explain.\n"
        f"3. Name the escaping substance and identify its state of matter."
    )
    sol = (
        f"**Step 1:** Apparent mass loss: $$\\Delta m = {m_react} - {m_remain} = \\mathbf{{{gas_mass}\\text{{ g}}}}$$ [1 Mark: Mass loss calculation].\n\n"
        f"**Step 2:** **No, matter was not destroyed**; the Law of Conservation of Mass still holds, but the beaker was an **open system**, allowing gaseous product to escape into the atmosphere [1 Mark: Gas escape explanation].\n\n"
        f"**Step 3:** The escaping substance is **carbon dioxide gas ($CO_2(g)$)** [1 Mark: Gas identification]."
    )
    return {
        "id": f"ns9_cr_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Mass loss = {gas_mass} g; No, matter was not destroyed because gas escaped from the open system; Escaping substance is carbon dioxide gas (CO2)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "21_apparent_mass_loss_in_open_system_gas_escape",
        "misconception_tags": ["open_system_apparent_mass_loss"],
        "hints": {
            "tier_1": "Subtract the final mass from initial mass.",
            "tier_2": "The lost mass is the gas that bubbled away.",
            "tier_3": f"{gas_mass} g; matter not destroyed (open system); carbon dioxide gas (CO2)."
        }
    }


def arch_22_apparent_mass_gain_in_open_system_oxygen_absorption(rng: random.Random) -> Dict[str, Any]:
    m_mag = rng.choice([2.4, 4.8, 12.0])
    # 2Mg (48) + O2 (32) -> 2MgO (80) -> ratio is 1.667
    m_ox = round(m_mag * (32 / 48), 2)
    m_mgo = round(m_mag + m_ox, 2)

    prompt = (
        f"A chemist heats a {m_mag} g strip of magnesium ribbon in an open crucible over a Bunsen flame. After burning with a brilliant white light, the resulting white magnesium oxide powder is reweighed:\n"
        f"- **Initial mass of magnesium ribbon:** {m_mag} g.\n"
        f"- **Final mass of magnesium oxide powder:** {m_mgo} g.\n\n"
        f"1. Notice that the mass apparently **increased** by {m_ox} g. Did the reaction create new matter?\n"
        f"2. Explain where this additional mass came from.\n"
        f"3. Write the balanced word equation for this reaction, clearly identifying the added reactant."
    )
    sol = (
        f"**Step 1:** **No, new matter was not created**; the Law of Conservation of Mass is fully upheld [1 Mark: No new matter].\n\n"
        f"**Step 2:** The crucible was open to the air, and magnesium atoms chemically reacted with and **absorbed oxygen gas ($O_2$) from the atmosphere**; the added mass is the mass of the oxygen chemically bonded into the solid $MgO$ [1 Mark: Oxygen absorbed from air].\n\n"
        f"**Step 3:** Word equation: **Magnesium + Oxygen $\\rightarrow$ Magnesium oxide** [1 Mark: Word equation]."
    )
    return {
        "id": f"ns9_cr_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"No new matter was created; Added mass came from atmospheric oxygen gas chemically combining with magnesium; Word equation: Magnesium + Oxygen -> Magnesium oxide",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "22_apparent_mass_gain_in_open_system_oxygen_absorption",
        "misconception_tags": ["open_system_apparent_mass_gain"],
        "hints": {
            "tier_1": "Burning in air absorbs oxygen from the atmosphere.",
            "tier_2": "The extra mass is oxygen gas now bonded in the ash.",
            "tier_3": "No matter created; oxygen from air added; Magnesium + Oxygen -> Magnesium oxide."
        }
    }


def arch_23_conservation_of_mass_calculations_finding_unknown_mass(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Combustion of methane", "CH4 + 2O2 -> CO2 + 2H2O", 16.0, 64.0, 44.0, 36.0, "water ($H_2O$)"),
        ("Synthesis of iron sulfide", "Fe + S -> FeS", 56.0, 32.0, 88.0, 88.0, "iron sulfide ($FeS$)"),
        ("Decomposition of calcium carbonate", "CaCO3 -> CaO + CO2", 100.0, 56.0, 44.0, 44.0, "carbon dioxide ($CO_2$)"),
    ]
    name, eq, m_r1, m_r2, m_p1, m_unknown, target = rng.choice(scenarios)

    if "Combustion" in name:
        prompt = (
            f"In a sealed closed system, {m_r1} g of methane reacts completely with {m_r2} g of oxygen gas according to:\n"
            f"$$\\text{{{eq}}}$$\n"
            f"The reaction produces {m_p1} g of carbon dioxide and an unknown mass of {target}.\n\n"
            f"1. State the total mass of the reactants before the reaction takes place.\n"
            f"2. Using the Law of Conservation of Mass, calculate the exact mass of {target} produced ({m_unknown} g).\n"
            f"3. State the governing principle used to solve this calculation."
        )
        total_r = m_r1 + m_r2
        calc_step = f"Total reactants mass = ${m_r1} + {m_r2} = {total_r}\\text{{ g}}$. By conservation of mass: Total products mass must = ${total_r}\\text{{ g}}$. Mass of {target} = ${total_r} - {m_p1} = \\mathbf{{{m_unknown}\\text{{ g}}}}$"
    elif "Synthesis" in name:
        prompt = (
            f"In a sealed crucible, {m_r1} g of iron powder reacts completely with {m_r2} g of sulfur powder to produce {target}.\n"
            f"$$\\text{{{eq}}}$$\n\n"
            f"1. What is the total mass of the reactants?\n"
            f"2. What is the exact mass of {target} produced ({m_unknown} g)?\n"
            f"3. State the governing principle used to solve this calculation."
        )
        total_r = m_r1 + m_r2
        calc_step = f"Total reactants mass = ${m_r1} + {m_r2} = \\mathbf{{{total_r}\\text{{ g}}}}$. Therefore, product mass = $\\mathbf{{{m_unknown}\\text{{ g}}}}$"
    else:
        prompt = (
            f"When {m_r1} g of solid calcium carbonate is strongly heated in a closed system, it decomposes into {m_r2} g of solid calcium oxide and an unknown mass of {target}.\n"
            f"$$\\text{{{eq}}}$$\n\n"
            f"1. State the mass of the starting reactant.\n"
            f"2. Calculate the exact mass of {target} produced ({m_unknown} g).\n"
            f"3. State the governing principle used to solve this calculation."
        )
        total_r = m_r1
        calc_step = f"Total reactant mass = ${total_r}\\text{{ g}}$. Total products mass = ${m_r2} + m({target}) = {total_r}\\text{{ g}}$. Mass of {target} = ${total_r} - {m_r2} = \\mathbf{{{m_unknown}\\text{{ g}}}}$"

    sol = (
        f"**Step 1:** Total mass of starting reactants: **{total_r} g** [1 Mark: Reactants mass].\n\n"
        f"**Step 2:** Calculation: {calc_step} [1 Mark: Mass calculation].\n\n"
        f"**Step 3:** Principle: **Law of Conservation of Mass** (mass of reactants = mass of products) [1 Mark: Governing principle]."
    )
    return {
        "id": f"ns9_cr_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"Reactants total = {total_r} g; Mass of {target} = {m_unknown} g; Law of Conservation of Mass",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "23_conservation_of_mass_calculations_finding_unknown_mass",
        "misconception_tags": ["conservation_of_mass_numerical_calculation"],
        "hints": {
            "tier_1": "Total mass on the left must equal total mass on the right.",
            "tier_2": f"Mass = {m_unknown} g.",
            "tier_3": f"{total_r} g; {m_unknown} g; Law of Conservation of Mass."
        }
    }


def arch_24_atom_tally_inventory_left_hand_vs_right_hand_side(rng: random.Random) -> Dict[str, Any]:
    equations = [
        (
            "Combustion of methane: CH4 + 2O2 -> CO2 + 2H2O",
            "Left: 1 C, 4 H, 4 O; Right: 1 C, 4 H, 4 O",
            1, 4, 4,
            "Balanced"
        ),
        (
            "Synthesis of ammonia: N2 + 3H2 -> 2NH3",
            "Left: 2 N, 6 H; Right: 2 N, 6 H",
            2, 6, 0,
            "Balanced"
        ),
        (
            "Combustion of propane: C3H8 + 5O2 -> 3CO2 + 4H2O",
            "Left: 3 C, 8 H, 10 O; Right: 3 C, 8 H, 10 O",
            3, 8, 10,
            "Balanced"
        ),
    ]
    eq_name, tally_text, n1, n2, n3, status = rng.choice(equations)

    prompt = (
        f"A fundamental skill in balancing equations is conducting a rigorous **atom tally (inventory)** on both sides of the arrow.\n\n"
        f"Consider: **{eq_name}**.\n\n"
        f"1. Conduct an atom tally of each element on the **reactant side (left-hand side)**.\n"
        f"2. Conduct an atom tally of each element on the **product side (right-hand side)**.\n"
        f"3. Compare the left and right sides to confirm whether the equation is currently balanced."
    )
    sol = (
        f"**Step 1:** Reactant side atom tally: {tally_text.split('; ')[0]} [1 Mark: Left tally].\n\n"
        f"**Step 2:** Product side atom tally: {tally_text.split('; ')[1]} [1 Mark: Right tally].\n\n"
        f"**Step 3:** Comparison: The atom counts for every element are **identical on both sides**, confirming the equation is **{status}** [1 Mark: Balance confirmation]."
    )
    return {
        "id": f"ns9_cr_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{tally_text}; Equation is {status} because atom counts match exactly",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "24_atom_tally_inventory_left_hand_vs_right_hand_side",
        "misconception_tags": ["atom_inventory_tally"],
        "hints": {
            "tier_1": "Multiply coefficients by subscripts for each atom on left and right.",
            "tier_2": f"Counts: {tally_text}.",
            "tier_3": f"{tally_text}; {status}."
        }
    }


def arch_25_evaluating_balanced_vs_unbalanced_equations_atom_count(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("H2 + O2 -> H2O", False, "Oxygen is unbalanced: Left has 2 O atoms, Right has only 1 O atom", "2H2 + O2 -> 2H2O"),
        ("2Mg + O2 -> 2MgO", True, "Both sides have 2 Mg atoms and 2 O atoms", "Already balanced"),
        ("Fe + O2 -> Fe2O3", False, "Both Fe and O are unbalanced: Left has 1 Fe and 2 O, Right has 2 Fe and 3 O", "4Fe + 3O2 -> 2Fe2O3"),
        ("Zn + 2HCl -> ZnCl2 + H2", True, "Both sides have 1 Zn atom, 2 H atoms, and 2 Cl atoms", "Already balanced"),
    ]
    eq, is_bal, reason, fix = rng.choice(cases)

    prompt = (
        f"Consider the chemical equation:\n"
        f"$$\\text{{{eq}}}$$\n\n"
        f"1. Is this chemical equation **balanced** or **unbalanced**?\n"
        f"2. Justify your answer by quoting the specific atom counts on the left-hand side and right-hand side ({reason}).\n"
        f"3. Write the fully balanced equation ({fix})."
    )
    sol = (
        f"**Step 1:** The equation is **{'BALANCED' if is_bal else 'UNBALANCED'}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Justification: {reason} [1 Mark: Atom count justification].\n\n"
        f"**Step 3:** Balanced form: **{fix if not is_bal else eq}** [1 Mark: Balanced equation]."
    )
    return {
        "id": f"ns9_cr_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{'Balanced' if is_bal else 'Unbalanced'}; {reason}; {fix if not is_bal else eq}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "25_evaluating_balanced_vs_unbalanced_equations_atom_count",
        "misconception_tags": ["evaluating_balanced_equations"],
        "hints": {
            "tier_1": "Count atoms on both sides. If they don't match, it is unbalanced.",
            "tier_2": f"Status: {'Balanced' if is_bal else 'Unbalanced'}. Reason: {reason}.",
            "tier_3": f"{'Balanced' if is_bal else 'Unbalanced'}; {reason}; {fix if not is_bal else eq}."
        }
    }


# ==============================================================================
# DISPATCH DICT (01 - 25)
# ==============================================================================

BUILDERS_01_25 = {
    "01_chemical_reaction_definition_and_new_substances": arch_01_chemical_reaction_definition_and_new_substances,
    "02_three_levels_of_representation_macroscopic_submicroscopic_symbolic": arch_02_three_levels_of_representation_macroscopic_submicroscopic_symbolic,
    "03_macroscopic_evidence_of_reaction_gas_precipitate_color_temp": arch_03_macroscopic_evidence_of_reaction_gas_precipitate_color_temp,
    "04_physical_change_vs_chemical_change_reversibility_and_bonds": arch_04_physical_change_vs_chemical_change_reversibility_and_bonds,
    "05_reactants_and_products_identification_left_and_right": arch_05_reactants_and_products_identification_left_and_right,
    "06_the_reaction_arrow_yields_meaning_and_direction": arch_06_the_reaction_arrow_yields_meaning_and_direction,
    "07_state_symbols_solid_liquid_gas_aqueous_definitions": arch_07_state_symbols_solid_liquid_gas_aqueous_definitions,
    "08_translating_word_equations_to_unbalanced_chemical_equations": arch_08_translating_word_equations_to_unbalanced_chemical_equations,
    "09_particle_model_diagram_rearrangement_of_atoms": arch_09_particle_model_diagram_rearrangement_of_atoms,
    "10_atomic_rearrangement_concept_no_new_atoms_created": arch_10_atomic_rearrangement_concept_no_new_atoms_created,
    "11_bond_breaking_requires_energy_endothermic_step": arch_11_bond_breaking_requires_energy_endothermic_step,
    "12_bond_making_releases_energy_exothermic_step": arch_12_bond_making_releases_energy_exothermic_step,
    "13_exothermic_vs_endothermic_reactions_overall_energy_balance": arch_13_exothermic_vs_endothermic_reactions_overall_energy_balance,
    "14_limiting_reactants_and_excess_reactants_particle_view": arch_14_limiting_reactants_and_excess_reactants_particle_view,
    "15_particle_diagram_counting_reactant_vs_product_molecules": arch_15_particle_diagram_counting_reactant_vs_product_molecules,
    "16_particle_diagram_identifying_unreacted_excess_atoms": arch_16_particle_diagram_identifying_unreacted_excess_atoms,
    "17_subscripts_indicate_atoms_per_molecule_immutable": arch_17_subscripts_indicate_atoms_per_molecule_immutable,
    "18_coefficients_indicate_number_of_particles_adjustable": arch_18_coefficients_indicate_number_of_particles_adjustable,
    "19_law_of_conservation_of_atoms_principle": arch_19_law_of_conservation_of_atoms_principle,
    "20_law_of_conservation_of_mass_closed_system": arch_20_law_of_conservation_of_mass_closed_system,
    "21_apparent_mass_loss_in_open_system_gas_escape": arch_21_apparent_mass_loss_in_open_system_gas_escape,
    "22_apparent_mass_gain_in_open_system_oxygen_absorption": arch_22_apparent_mass_gain_in_open_system_oxygen_absorption,
    "23_conservation_of_mass_calculations_finding_unknown_mass": arch_23_conservation_of_mass_calculations_finding_unknown_mass,
    "24_atom_tally_inventory_left_hand_vs_right_hand_side": arch_24_atom_tally_inventory_left_hand_vs_right_hand_side,
    "25_evaluating_balanced_vs_unbalanced_equations_atom_count": arch_25_evaluating_balanced_vs_unbalanced_equations_atom_count,
}
