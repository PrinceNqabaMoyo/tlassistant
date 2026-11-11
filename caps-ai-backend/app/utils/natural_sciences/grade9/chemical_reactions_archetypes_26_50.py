"""Grade 9 Natural Sciences - Chemical Reactions: Archetypes 26 to 50.
Grounded strictly in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 2/01. Chemical reactions.md.

Covers:
- Stoichiometric balancing of chemical equations:
  - Synthesis/Combustion of elements: H2 + O2 -> H2O, Mg + O2 -> MgO, Fe + O2 -> Fe2O3, Fe + S -> FeS, C + O2 -> CO2, 2C + O2 -> 2CO
  - Hydrocarbon combustion: CH4 + 2O2 -> CO2 + 2H2O, C3H8 + 5O2 -> 3CO2 + 4H2O
  - Decomposition: 2H2O2 -> 2H2O + O2, CaCO3 -> CaO + CO2, 2KClO3 -> 2KCl + 3O2
  - Metal + Acid: Zn + 2HCl -> ZnCl2 + H2, Mg + 2HCl -> MgCl2 + H2, Fe + 2HCl -> FeCl2 + H2
  - Acid + Base neutralization: HCl + NaOH -> NaCl + H2O
  - Acid + Carbonate: 2HCl + CaCO3 -> CaCl2 + H2O + CO2
- Gas identification tests: H2 (burning splint pop), O2 (glowing splint rekindles), CO2 (limewater milky)
- Common balancing errors: changing subscripts or inserting coefficients inside formulas
- Rate of reaction factors and master synthesis challenge
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Balancing Synthesis & Combustion Reactions (26 - 34)
# ==============================================================================

def arch_26_why_equations_must_be_balanced_stoichiometry(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Chemical reaction equations must always be correctly balanced before they can be used for calculations.\n\n"
        "1. Why must every chemical equation be balanced according to fundamental physical laws?\n"
        "2. What does an unbalanced equation (such as $H_2 + O_2 \\rightarrow H_2O$) falsely imply about matter?\n"
        "3. State the only method that chemists are permitted to use when balancing an equation."
    )
    sol = (
        "**Step 1:** Equations must be balanced to satisfy the **Law of Conservation of Matter/Atoms**, which states that atoms cannot be created or destroyed in chemical reactions [1 Mark: Law of Conservation of Matter].\n\n"
        "**Step 2:** An unbalanced equation falsely implies that **atoms appeared out of nowhere or vanished into nothing**; for example, $H_2 + O_2 \\rightarrow H_2O$ falsely implies that 1 oxygen atom was magically destroyed [1 Mark: False implication].\n\n"
        "**Step 3:** Chemists are only permitted to **adjust the stoichiometric coefficients in front of chemical formulas**; changing subscripts or altering formulas is strictly forbidden [1 Mark: Coefficients only]."
    )
    return {
        "id": f"ns9_cr_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Must satisfy the Law of Conservation of Atoms/Matter; Unbalanced equation falsely implies atoms are created or destroyed; Only adjust stoichiometric coefficients in front of formulas",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "26_why_equations_must_be_balanced_stoichiometry",
        "misconception_tags": ["why_balance_equations_stoichiometry"],
        "hints": {
            "tier_1": "Conservation of mass means left side must equal right side.",
            "tier_2": "Unbalanced equations imply atoms disappeared.",
            "tier_3": "Law of Conservation; implies atoms destroyed; change coefficients only."
        }
    }


def arch_27_balancing_synthesis_hydrogen_and_oxygen_to_water(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Hydrogen gas reacts explosively with oxygen gas to form water:\n"
        "$$\\text{H}_2 + \\text{O}_2 \\rightarrow \\text{H}_2\\text{O}$$\n\n"
        "1. Identify which element is currently unbalanced and explain why.\n"
        "2. Write the fully balanced chemical equation using whole-number coefficients.\n"
        "3. Provide the atom tally for hydrogen and oxygen on both sides to verify that the equation is balanced."
    )
    sol = (
        "**Step 1:** **Oxygen is unbalanced**; there are 2 oxygen atoms on the reactant side ($O_2$) but only 1 oxygen atom on the product side ($H_2O$) [1 Mark: Unbalanced element].\n\n"
        "**Step 2:** Balanced equation: $$\\mathbf{2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 3:** Atom tally verification:\n"
        "- Reactants: $2 \\times 2 = 4\\text{ H}$, $1 \\times 2 = 2\\text{ O}$\n"
        "- Products: $2 \\times 2 = 4\\text{ H}$, $2 \\times 1 = 2\\text{ O}$\n"
        "Both sides have 4 H atoms and 2 O atoms ($4=4$ and $2=2$) [1 Mark: Atom tally]."
    )
    return {
        "id": f"ns9_cr_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Oxygen is unbalanced (2 on left, 1 on right); Balanced equation: 2H2 + O2 -> 2H2O; 4 H and 2 O on both sides",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "27_balancing_synthesis_hydrogen_and_oxygen_to_water",
        "misconception_tags": ["balancing_water_synthesis"],
        "hints": {
            "tier_1": "Put a 2 in front of H2O to balance oxygen, then a 2 in front of H2.",
            "tier_2": "2H2 + O2 -> 2H2O.",
            "tier_3": "Oxygen unbalanced; 2H2 + O2 -> 2H2O; 4 H and 2 O."
        }
    }


def arch_28_balancing_synthesis_magnesium_and_oxygen_to_magnesium_oxide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Silvery magnesium ribbon burns with an intense white flame in oxygen gas to form white magnesium oxide powder:\n"
        "$$\\text{Mg} + \\text{O}_2 \\rightarrow \\text{MgO}$$\n\n"
        "1. Explain why placing a subscript 2 after oxygen in MgO ($MgO_2$) is an incorrect method of balancing this reaction.\n"
        "2. Write the correctly balanced chemical equation using whole-number coefficients.\n"
        "3. How many magnesium atoms and how many oxygen atoms are present on each side of the balanced equation?"
    )
    sol = (
        "**Step 1:** Writing $MgO_2$ is incorrect because it **changes the chemical formula and identity of the product** (magnesium peroxide instead of magnesium oxide); magnesium has a valency of 2 and oxygen has a valency of 2, so the correct formula is strictly $MgO$ [1 Mark: Subscript error].\n\n"
        "**Step 2:** Balanced equation: $$\\mathbf{2\\text{Mg} + \\text{O}_2 \\rightarrow 2\\text{MgO}}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 3:** Atom tally: **2 magnesium atoms and 2 oxygen atoms** are present on each side ($2=2$ and $2=2$) [1 Mark: Atom tally]."
    )
    return {
        "id": f"ns9_cr_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Writing MgO2 changes chemical identity (subscripts are immutable); 2Mg + O2 -> 2MgO; 2 Mg atoms and 2 O atoms on each side",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "28_balancing_synthesis_magnesium_and_oxygen_to_magnesium_oxide",
        "misconception_tags": ["balancing_magnesium_combustion"],
        "hints": {
            "tier_1": "You need 2 MgO to balance O2, requiring 2 Mg on the left.",
            "tier_2": "Equation: 2Mg + O2 -> 2MgO.",
            "tier_3": "Cannot change subscripts; 2Mg + O2 -> 2MgO; 2 Mg and 2 O on both sides."
        }
    }


def arch_29_balancing_synthesis_iron_and_oxygen_to_iron_iii_oxide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When iron metal slowly rusts in air, it reacts with atmospheric oxygen to form reddish-brown iron(III) oxide:\n"
        "$$\\text{Fe} + \\text{O}_2 \\rightarrow \\text{Fe}_2\\text{O}_3$$\n\n"
        "1. Find the lowest common multiple for the oxygen atoms (reactants have 2, products have 3).\n"
        "2. Write the fully balanced chemical equation.\n"
        "3. State the stoichiometric coefficients in order from left to right (Fe, O2, Fe2O3)."
    )
    sol = (
        "**Step 1:** The lowest common multiple of 2 and 3 is **6 oxygen atoms** [1 Mark: LCM].\n\n"
        "**Step 2:** To get 6 oxygens, put 3 in front of $O_2$ and 2 in front of $Fe_2O_3$. This gives $2 \\times 2 = 4\\text{ Fe}$, requiring 4 in front of $Fe$:\n"
        "$$\\mathbf{4\\text{Fe} + 3\\text{O}_2 \\rightarrow 2\\text{Fe}_2\\text{O}_3}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 3:** Coefficients in order: **4, 3, 2** [1 Mark: Coefficients]."
    )
    return {
        "id": f"ns9_cr_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "LCM of oxygen is 6; 4Fe + 3O2 -> 2Fe2O3; Coefficients: 4, 3, 2",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "29_balancing_synthesis_iron_and_oxygen_to_iron_iii_oxide",
        "misconception_tags": ["balancing_iron_oxide_rusting"],
        "hints": {
            "tier_1": "Balance oxygen first using LCM = 6.",
            "tier_2": "3 O2 gives 6 O; 2 Fe2O3 gives 4 Fe and 6 O.",
            "tier_3": "LCM = 6; 4Fe + 3O2 -> 2Fe2O3; 4, 3, 2."
        }
    }


def arch_30_balancing_synthesis_iron_and_sulfur_to_iron_ii_sulfide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When iron filings and sulfur powder are heated in a combustion tube, they react:\n"
        "$$\\text{Fe} + \\text{S} \\rightarrow \\text{FeS}$$\n\n"
        "1. Is this chemical equation already balanced as written? Show the atom counts for iron and sulfur.\n"
        "2. What is the stoichiometric mole ratio of iron to sulfur in this reaction?\n"
        "3. If 100 atoms of iron react completely with 100 atoms of sulfur, how many formula units of iron(II) sulfide ($FeS$) are formed?"
    )
    sol = (
        "**Step 1:** **Yes, it is already balanced**; Reactants have 1 Fe atom and 1 S atom; Products have 1 Fe atom and 1 S atom [1 Mark: Balanced confirmation].\n\n"
        "**Step 2:** The stoichiometric ratio is **1 : 1** (one atom of iron reacts with one atom of sulfur) [1 Mark: Stoichiometric ratio].\n\n"
        "**Step 3:** Exactly **100 formula units of iron(II) sulfide ($FeS$)** are formed [1 Mark: Product count]."
    )
    return {
        "id": f"ns9_cr_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Yes, already balanced (1 Fe and 1 S on each side); Stoichiometric ratio is 1:1; 100 formula units of FeS formed",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "30_balancing_synthesis_iron_and_sulfur_to_iron_ii_sulfide",
        "misconception_tags": ["one_to_one_stoichiometry_synthesis"],
        "hints": {
            "tier_1": "Check atom counts on left and right.",
            "tier_2": "1 Fe and 1 S on each side means it is already balanced.",
            "tier_3": "Yes, already balanced; 1:1 ratio; 100 formula units."
        }
    }


def arch_31_balancing_combustion_carbon_to_carbon_dioxide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Complete combustion of carbon fuel (such as coal or charcoal) occurs when abundant oxygen is available:\n"
        "$$\\text{C} + \\text{O}_2 \\rightarrow \\text{CO}_2$$\n\n"
        "1. Verify that this equation is balanced by providing atom tallies for carbon and oxygen on both sides.\n"
        "2. What is the chemical name and state of the product formed at room temperature?\n"
        "3. Name the universal greenhouse gas test used to confirm the identity of this gas in the lab."
    )
    sol = (
        "**Step 1:** Verification: Left side has **1 carbon atom and 2 oxygen atoms**; Right side has **1 carbon atom and 2 oxygen atoms**. Both sides match ($1=1$ and $2=2$), so it is fully balanced [1 Mark: Verification].\n\n"
        "**Step 2:** The product is **carbon dioxide gas ($CO_2(g)$)** [1 Mark: Product name and state].\n\n"
        "**Step 3:** The test is bubbling the gas through **clear limewater (calcium hydroxide solution)**; it turns **milky/cloudy** white [1 Mark: Limewater test]."
    )
    return {
        "id": f"ns9_cr_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Balanced (1 C and 2 O on each side); Carbon dioxide gas; Bubble through clear limewater (turns milky white)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "31_balancing_combustion_carbon_to_carbon_dioxide",
        "misconception_tags": ["complete_combustion_carbon_balancing"],
        "hints": {
            "tier_1": "C + O2 -> CO2 is already balanced.",
            "tier_2": "Carbon dioxide turns limewater milky.",
            "tier_3": "1 C and 2 O on each side; Carbon dioxide gas; Limewater milky test."
        }
    }


def arch_32_balancing_combustion_carbon_to_carbon_monoxide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Incomplete combustion of carbon fuel occurs when the oxygen supply is limited (e.g. inside an enclosed room with an unvented heater):\n"
        "$$\\text{C} + \\text{O}_2 \\rightarrow \\text{CO}$$\n\n"
        "1. Balance this chemical equation using whole-number coefficients.\n"
        "2. Name the toxic gas produced and explain why it is known as the 'silent killer'.\n"
        "3. Compare the oxygen requirement of this reaction with that of complete combustion."
    )
    sol = (
        "**Step 1:** Balanced equation: $$\\mathbf{2\\text{C} + \\text{O}_2 \\rightarrow 2\\text{CO}}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 2:** The gas is **carbon monoxide ($CO$)**; it is called the 'silent killer' because it is completely **colorless, odorless, tasteless, and non-irritating**, yet binds tightly to hemoglobin in the blood, starving the body of oxygen [1 Mark: Carbon monoxide properties].\n\n"
        "**Step 3:** Incomplete combustion requires **half as much oxygen per mole of carbon** ($0.5\\text{ O}_2$ per C atom) compared to complete combustion ($1.0\\text{ O}_2$ per C atom) [1 Mark: Oxygen comparison]."
    )
    return {
        "id": f"ns9_cr_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "2C + O2 -> 2CO; Carbon monoxide, called silent killer because colorless/odorless/toxic; Requires half as much oxygen per carbon compared to complete combustion",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "32_balancing_combustion_carbon_to_carbon_monoxide",
        "misconception_tags": ["incomplete_combustion_carbon_monoxide"],
        "hints": {
            "tier_1": "You have 2 O on the left and 1 on the right, so put 2 in front of CO, then 2 in front of C.",
            "tier_2": "2C + O2 -> 2CO.",
            "tier_3": "2C + O2 -> 2CO; Carbon monoxide (colorless, odorless, toxic); requires less oxygen."
        }
    }


def arch_33_balancing_combustion_methane_gas_ch4_plus_o2(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Methane gas ($CH_4$), the principal component of natural gas, burns cleanly in a Bunsen burner flame:\n"
        "$$\\text{CH}_4 + \\text{O}_2 \\rightarrow \\text{CO}_2 + \\text{H}_2\\text{O}$$\n\n"
        "1. Write the fully balanced chemical equation for the combustion of methane.\n"
        "2. Step through the balancing sequence: balance carbon, balance hydrogen, and balance oxygen.\n"
        "3. How many molecules of oxygen gas ($O_2$) are required to burn exactly one molecule of methane?"
    )
    sol = (
        "**Step 1:** Balanced equation: $$\\mathbf{\\text{CH}_4 + 2\\text{O}_2 \\rightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O}}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 2:** Balancing sequence:\n"
        "- Carbon: 1 on left, 1 on right (already balanced).\n"
        "- Hydrogen: 4 on left ($CH_4$), so place coefficient 2 in front of $H_2O$ ($2 \\times 2 = 4\\text{ H}$).\n"
        "- Oxygen: Products now have $2\\text{ (in } CO_2) + 2 \\times 1\\text{ (in } 2H_2O) = 4\\text{ O atoms}$. Place coefficient 2 in front of $O_2$ ($2 \\times 2 = 4\\text{ O}$) [1 Mark: Balancing steps].\n\n"
        "**Step 3:** Exactly **2 molecules of oxygen gas ($2O_2$)** are needed per molecule of methane [1 Mark: Oxygen molecules]."
    )
    return {
        "id": f"ns9_cr_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "CH4 + 2O2 -> CO2 + 2H2O; Balance C (1=1), H (put 2 in front of H2O), O (put 2 in front of O2); Exactly 2 molecules of O2",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "33_balancing_combustion_methane_gas_ch4_plus_o2",
        "misconception_tags": ["methane_combustion_balancing"],
        "hints": {
            "tier_1": "Balance C first, then H (put 2 in front of H2O), then count total oxygens on right (4) to balance O2.",
            "tier_2": "CH4 + 2O2 -> CO2 + 2H2O.",
            "tier_3": "CH4 + 2O2 -> CO2 + 2H2O; sequence: C then H then O; 2 O2 molecules."
        }
    }


def arch_34_balancing_combustion_propane_gas_c3h8_plus_o2(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Propane gas ($C_3H_8$), used in gas barbecue grills and camping cylinders, combusts in oxygen:\n"
        "$$\\text{C}_3\\text{H}_8 + \\text{O}_2 \\rightarrow \\text{CO}_2 + \\text{H}_2\\text{O}$$\n\n"
        "1. Write the fully balanced chemical equation for the complete combustion of propane.\n"
        "2. State the coefficients in order from left to right (C3H8, O2, CO2, H2O).\n"
        "3. Show the total atom inventory for carbon, hydrogen, and oxygen on both sides of your balanced equation."
    )
    sol = (
        "**Step 1:** Balanced equation: $$\\mathbf{\\text{C}_3\\text{H}_8 + 5\\text{O}_2 \\rightarrow 3\\text{CO}_2 + 4\\text{H}_2\\text{O}}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 2:** Coefficients in order: **1, 5, 3, 4** [1 Mark: Coefficients].\n\n"
        "**Step 3:** Atom inventory:\n"
        "- Carbon: Left = 3, Right = $3 \\times 1 = 3$\n"
        "- Hydrogen: Left = 8, Right = $4 \\times 2 = 8$\n"
        "- Oxygen: Left = $5 \\times 2 = 10$, Right = $(3 \\times 2) + (4 \\times 1) = 6 + 4 = 10$\n"
        "Both sides equal: 3 C, 8 H, and 10 O [1 Mark: Atom inventory]."
    )
    return {
        "id": f"ns9_cr_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "C3H8 + 5O2 -> 3CO2 + 4H2O; Coefficients: 1, 5, 3, 4; 3 C, 8 H, 10 O on each side",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "34_balancing_combustion_propane_gas_c3h8_plus_o2",
        "misconception_tags": ["propane_combustion_balancing"],
        "hints": {
            "tier_1": "Put 3 in front of CO2 and 4 in front of H2O. Total O on right is 3*2 + 4 = 10.",
            "tier_2": "C3H8 + 5O2 -> 3CO2 + 4H2O.",
            "tier_3": "C3H8 + 5O2 -> 3CO2 + 4H2O; 1, 5, 3, 4; 3 C, 8 H, 10 O."
        }
    }


# ==============================================================================
# CLUSTER 5: Decomposition, Metal-Acid & Neutralization (35 - 42)
# ==============================================================================

def arch_35_balancing_decomposition_hydrogen_peroxide_catalyst(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Hydrogen peroxide decomposes in the presence of a black manganese dioxide ($MnO_2$) catalyst:\n"
        "$$\\text{H}_2\\text{O}_2 \\rightarrow \\text{H}_2\\text{O} + \\text{O}_2$$\n\n"
        "1. Write the fully balanced chemical equation for this decomposition.\n"
        "2. What is the role of manganese dioxide ($MnO_2$) in this reaction, and why is it not written as a reactant in the chemical equation?\n"
        "3. Describe the glowing splint test used to confirm that the gas evolved is oxygen."
    )
    sol = (
        "**Step 1:** Balanced equation: $$\\mathbf{2\\text{H}_2\\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O} + \\text{O}_2}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 2:** Manganese dioxide acts as a **catalyst**; it speeds up the rate of reaction without being chemically changed or consumed. It is written above the arrow rather than as a reactant because it is not consumed in the reaction [1 Mark: Catalyst role].\n\n"
        "**Step 3:** Place a **glowing wooden splint** into the mouth of the test tube: the splint **relights / bursts back into flame** [1 Mark: Oxygen test]."
    )
    return {
        "id": f"ns9_cr_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "2H2O2 -> 2H2O + O2; Catalyst (speeds up reaction without being consumed, not a reactant); Glowing wooden splint relights/rekindles",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "35_balancing_decomposition_hydrogen_peroxide_catalyst",
        "misconception_tags": ["catalytic_decomposition_peroxide"],
        "hints": {
            "tier_1": "Put a 2 in front of H2O2 and a 2 in front of H2O.",
            "tier_2": "Catalysts speed up reactions and are not consumed.",
            "tier_3": "2H2O2 -> 2H2O + O2; catalyst role; glowing splint relights."
        }
    }


def arch_36_balancing_decomposition_calcium_carbonate_thermal(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a lime kiln, limestone (calcium carbonate, $CaCO_3$) is heated strongly to produce quicklime ($CaO$):\n"
        "$$\\text{CaCO}_3 \\rightarrow \\text{CaO} + \\text{CO}_2$$\n\n"
        "1. Is this chemical equation balanced as written? Show the atom counts for Ca, C, and O.\n"
        "2. What type of chemical reaction is this (synthesis, decomposition, or combustion)?\n"
        "3. Name the two products formed and identify their common industrial uses."
    )
    sol = (
        "**Step 1:** **Yes, it is already balanced**; Reactants have 1 Ca, 1 C, and 3 O atoms; Products have 1 Ca, 1 C, and $1 + 2 = 3\\text{ O atoms}$ [1 Mark: Balanced verification].\n\n"
        "**Step 2:** This is a **thermal decomposition reaction** (a single compound broken down into two simpler substances by heat) [1 Mark: Decomposition type].\n\n"
        "**Step 3:** Products: **Calcium oxide (quicklime)** used in cement and steel manufacturing, and **carbon dioxide gas** [1 Mark: Products and uses]."
    )
    return {
        "id": f"ns9_cr_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Yes, already balanced (1 Ca, 1 C, 3 O on each side); Thermal decomposition reaction; Calcium oxide (quicklime for cement) and carbon dioxide gas",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "36_balancing_decomposition_calcium_carbonate_thermal",
        "misconception_tags": ["thermal_decomposition_calcium_carbonate"],
        "hints": {
            "tier_1": "Count Ca, C, and O on both sides.",
            "tier_2": "One compound breaking into two is decomposition.",
            "tier_3": "Already balanced; thermal decomposition; Calcium oxide and CO2."
        }
    }


def arch_37_balancing_decomposition_potassium_chlorate_to_kcl_and_o2(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Potassium chlorate decomposes when heated to produce potassium chloride and oxygen gas:\n"
        "$$\\text{KClO}_3 \\rightarrow \\text{KCl} + \\text{O}_2$$\n\n"
        "1. Write the correctly balanced chemical equation.\n"
        "2. What is the lowest common multiple for the oxygen atoms (3 on left, 2 on right)?\n"
        "3. State the coefficients in order from left to right (KClO3, KCl, O2)."
    )
    sol = (
        "**Step 1:** Balanced equation: $$\\mathbf{2\\text{KClO}_3 \\rightarrow 2\\text{KCl} + 3\\text{O}_2}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 2:** The lowest common multiple of 3 and 2 is **6 oxygen atoms** [1 Mark: LCM].\n\n"
        "**Step 3:** Coefficients in order: **2, 2, 3** [1 Mark: Coefficients]."
    )
    return {
        "id": f"ns9_cr_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "2KClO3 -> 2KCl + 3O2; LCM of oxygen is 6; Coefficients: 2, 2, 3",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "37_balancing_decomposition_potassium_chlorate_to_kcl_and_o2",
        "misconception_tags": ["potassium_chlorate_decomposition_balancing"],
        "hints": {
            "tier_1": "Use LCM = 6 for oxygen: 2 KClO3 gives 6 O, 3 O2 gives 6 O.",
            "tier_2": "2KClO3 -> 2KCl + 3O2.",
            "tier_3": "2KClO3 -> 2KCl + 3O2; LCM is 6; 2, 2, 3."
        }
    }


def arch_38_balancing_metal_acid_zinc_and_hydrochloric_acid(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Zinc metal granules react with dilute hydrochloric acid in an effervescent reaction:\n"
        "$$\\text{Zn} + \\text{HCl} \\rightarrow \\text{ZnCl}_2 + \\text{H}_2$$\n\n"
        "1. Write the correctly balanced chemical equation.\n"
        "2. State the single coefficient needed and specify where it must be placed.\n"
        "3. Identify the salt formed and the gas produced."
    )
    sol = (
        "**Step 1:** Balanced equation: $$\\mathbf{\\text{Zn} + 2\\text{HCl} \\rightarrow \\text{ZnCl}_2 + \\text{H}_2}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 2:** A coefficient of **2 in front of HCl** balances both the 2 chlorine atoms and 2 hydrogen atoms [1 Mark: Coefficient 2 in front of HCl].\n\n"
        "**Step 3:** Salt: **Zinc chloride ($ZnCl_2$)**; Gas: **Hydrogen gas ($H_2$)** [1 Mark: Salt and gas]."
    )
    return {
        "id": f"ns9_cr_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Zn + 2HCl -> ZnCl2 + H2; Coefficient of 2 placed in front of HCl; Salt is Zinc chloride, gas is Hydrogen",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "38_balancing_metal_acid_zinc_and_hydrochloric_acid",
        "misconception_tags": ["zinc_hydrochloric_acid_balancing"],
        "hints": {
            "tier_1": "Put a 2 in front of HCl to balance Cl2 and H2 on the right.",
            "tier_2": "Zn + 2HCl -> ZnCl2 + H2.",
            "tier_3": "Zn + 2HCl -> ZnCl2 + H2; 2 in front of HCl; Zinc chloride and Hydrogen."
        }
    }


def arch_39_balancing_metal_acid_magnesium_and_hydrochloric_acid(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Magnesium ribbon reacts rapidly and exothermically with dilute hydrochloric acid:\n"
        "$$\\text{Mg} + \\text{HCl} \\rightarrow \\text{MgCl}_2 + \\text{H}_2$$\n\n"
        "1. Write the correctly balanced chemical equation.\n"
        "2. What general pattern of metal-acid reactions does this represent ($Metal + Acid \\rightarrow Salt + Hydrogen$)?\n"
        "3. If 1 mole of magnesium reacts completely, how many moles of hydrochloric acid are consumed?"
    )
    sol = (
        "**Step 1:** Balanced equation: $$\\mathbf{\\text{Mg} + 2\\text{HCl} \\rightarrow \\text{MgCl}_2 + \\text{H}_2}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 2:** General reaction rule: **$\\text{Metal} + \\text{Acid} \\rightarrow \\text{Salt} + \\text{Hydrogen gas}$** [1 Mark: General rule].\n\n"
        "**Step 3:** Exactly **2 moles of hydrochloric acid ($2HCl$)** are consumed per 1 mole of magnesium [1 Mark: Molar ratio]."
    )
    return {
        "id": f"ns9_cr_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Mg + 2HCl -> MgCl2 + H2; Metal + Acid -> Salt + Hydrogen gas; Exactly 2 moles of HCl",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "39_balancing_metal_acid_magnesium_and_hydrochloric_acid",
        "misconception_tags": ["magnesium_acid_reaction_pattern"],
        "hints": {
            "tier_1": "Put a 2 in front of HCl.",
            "tier_2": "General rule is Metal + Acid -> Salt + Hydrogen.",
            "tier_3": "Mg + 2HCl -> MgCl2 + H2; Metal + Acid -> Salt + Hydrogen; 2 moles HCl."
        }
    }


def arch_40_balancing_metal_acid_iron_and_hydrochloric_acid(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Iron filings react slowly with hydrochloric acid to produce iron(II) chloride and hydrogen gas:\n"
        "$$\\text{Fe} + \\text{HCl} \\rightarrow \\text{FeCl}_2 + \\text{H}_2$$\n\n"
        "1. Write the balanced chemical equation.\n"
        "2. Write the word equation for this reaction.\n"
        "3. Explain why the rate of reaction is noticeably slower than with magnesium or zinc."
    )
    sol = (
        "**Step 1:** Balanced equation: $$\\mathbf{\\text{Fe} + 2\\text{HCl} \\rightarrow \\text{FeCl}_2 + \\text{H}_2}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 2:** Word equation: **Iron + Hydrochloric acid $\\rightarrow$ Iron(II) chloride + Hydrogen** [1 Mark: Word equation].\n\n"
        "**Step 3:** Iron is **lower in the reactivity series of metals** than magnesium and zinc, so it reacts less vigorously with dilute acids [1 Mark: Reactivity explanation]."
    )
    return {
        "id": f"ns9_cr_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Fe + 2HCl -> FeCl2 + H2; Iron + Hydrochloric acid -> Iron(II) chloride + Hydrogen; Iron is less reactive than zinc and magnesium",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "40_balancing_metal_acid_iron_and_hydrochloric_acid",
        "misconception_tags": ["metal_acid_reactivity_series"],
        "hints": {
            "tier_1": "Put a 2 in front of HCl.",
            "tier_2": "Iron is less reactive than zinc or magnesium.",
            "tier_3": "Fe + 2HCl -> FeCl2 + H2; Iron + Acid -> Salt + Hydrogen; lower reactivity."
        }
    }


def arch_41_balancing_neutralization_hydrochloric_acid_and_sodium_hydroxide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When hydrochloric acid is mixed with sodium hydroxide solution, a neutralization reaction occurs:\n"
        "$$\\text{HCl} + \\text{NaOH} \\rightarrow \\text{NaCl} + \\text{H}_2\\text{O}$$\n\n"
        "1. Verify that this chemical equation is balanced by showing atom counts on both sides.\n"
        "2. State the general word equation for an acid-base neutralization reaction.\n"
        "3. What is the approximate pH of the solution when exact stoichiometric quantities have fully reacted?"
    )
    sol = (
        "**Step 1:** Verification: Left side has **1 H (in HCl) + 1 H (in NaOH) = 2 H, 1 Cl, 1 Na, and 1 O**; Right side has **1 Na, 1 Cl, 2 H, and 1 O**. All atom counts match ($2=2, 1=1, 1=1, 1=1$), so it is balanced [1 Mark: Verification].\n\n"
        "**Step 2:** General equation: **$\\text{Acid} + \\text{Base} \\rightarrow \\text{Salt} + \\text{Water}$** [1 Mark: General equation].\n\n"
        "**Step 3:** The solution has a neutral pH of approximately **pH 7** [1 Mark: pH 7]."
    )
    return {
        "id": f"ns9_cr_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Balanced (2 H, 1 Cl, 1 Na, 1 O on each side); Acid + Base -> Salt + Water; Neutral solution has pH 7",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "41_balancing_neutralization_hydrochloric_acid_and_sodium_hydroxide",
        "misconception_tags": ["acid_base_neutralization_pattern"],
        "hints": {
            "tier_1": "Acid + Base -> Salt + Water.",
            "tier_2": "Neutral pH is 7.",
            "tier_3": "Balanced; Acid + Base -> Salt + Water; pH 7."
        }
    }


def arch_42_balancing_acid_carbonate_calcium_carbonate_and_hydrochloric_acid(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When vinegar or hydrochloric acid is poured onto eggshells or chalk (calcium carbonate, $CaCO_3$):\n"
        "$$\\text{HCl} + \\text{CaCO}_3 \\rightarrow \\text{CaCl}_2 + \\text{H}_2\\text{O} + \\text{CO}_2$$\n\n"
        "1. Write the correctly balanced chemical equation.\n"
        "2. State the general reaction rule: $\\text{Acid} + \\text{Metal carbonate} \\rightarrow \\text{Salt} + \\text{Water} + \\text{Carbon dioxide}$.\n"
        "3. Name the gas causing effervescence, and state how to test for it."
    )
    sol = (
        "**Step 1:** Balanced equation: $$\\mathbf{2\\text{HCl} + \\text{CaCO}_3 \\rightarrow \\text{CaCl}_2 + \\text{H}_2\\text{O} + \\text{CO}_2}$$ [1 Mark: Balanced equation].\n\n"
        "**Step 2:** General rule: **$\\text{Acid} + \\text{Metal Carbonate} \\rightarrow \\text{Salt} + \\text{Water} + \\text{Carbon dioxide}$** [1 Mark: General rule].\n\n"
        "**Step 3:** Gas: **Carbon dioxide ($CO_2$)**; Test: Bubbling through **clear limewater turns it milky/cloudy** [1 Mark: Gas and test]."
    )
    return {
        "id": f"ns9_cr_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "2HCl + CaCO3 -> CaCl2 + H2O + CO2; Acid + Metal Carbonate -> Salt + Water + Carbon dioxide; Carbon dioxide gas (turns limewater milky)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "42_balancing_acid_carbonate_calcium_carbonate_and_hydrochloric_acid",
        "misconception_tags": ["acid_carbonate_reaction_pattern"],
        "hints": {
            "tier_1": "Put a 2 in front of HCl.",
            "tier_2": "Acid + Carbonate -> Salt + Water + CO2.",
            "tier_3": "2HCl + CaCO3 -> CaCl2 + H2O + CO2; general rule; CO2 turns limewater milky."
        }
    }


# ==============================================================================
# CLUSTER 6: Gas Testing, Error Analysis & Master Synthesis (43 - 50)
# ==============================================================================

def arch_43_gas_tests_hydrogen_pop_test_investigation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a laboratory investigation, a test tube collects an unknown gas produced by reacting zinc metal with sulfuric acid.\n\n"
        "1. Describe the exact experimental procedure to test for **hydrogen gas ($H_2$)**.\n"
        "2. What is the positive observation observed during this test?\n"
        "3. Write the balanced chemical equation for the micro-combustion reaction that causes this observation ($H_2 + O_2$)."
    )
    sol = (
        "**Step 1:** Procedure: Bring a **burning wooden splint (with a live flame)** near the open mouth of the inverted test tube collecting the gas [1 Mark: Burning splint procedure].\n\n"
        "**Step 2:** Observation: The gas ignites with a distinctive **sharp 'pop' sound** (squeaky pop) [1 Mark: Squeaky pop observation].\n\n"
        "**Step 3:** Chemical equation: $$\\mathbf{2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}}$$ [1 Mark: Equation]."
    )
    return {
        "id": f"ns9_cr_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Bring a burning wooden splint to the mouth of the test tube; Gas burns with a distinctive 'pop' sound; Equation: 2H2 + O2 -> 2H2O",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "43_gas_tests_hydrogen_pop_test_investigation",
        "misconception_tags": ["hydrogen_gas_test_procedure"],
        "hints": {
            "tier_1": "Hydrogen burns with a pop when touched by a burning flame.",
            "tier_2": "Burning splint -> 'pop' sound.",
            "tier_3": "Burning splint; sharp 'pop' sound; 2H2 + O2 -> 2H2O."
        }
    }


def arch_44_gas_tests_oxygen_glowing_splint_reignition(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A student decomposes hydrogen peroxide with yeast and collects the gas in a test tube.\n\n"
        "1. Describe the exact experimental procedure to test for **oxygen gas ($O_2$)**.\n"
        "2. What is the positive observation confirming that the gas is oxygen?\n"
        "3. Why does the splint behave this way in pure oxygen compared to ordinary air?"
    )
    sol = (
        "**Step 1:** Procedure: Light a wooden splint, blow out the flame leaving only a **glowing red ember**, and immediately insert the **glowing splint** into the test tube [1 Mark: Glowing splint procedure].\n\n"
        "**Step 2:** Observation: The glowing splint **relights / bursts back into a bright yellow flame** [1 Mark: Relighting observation].\n\n"
        "**Step 3:** Pure oxygen has a concentration of $100\\%$ compared to only $21\\%$ in ambient air; the high concentration of oxygen molecules dramatically increases collision rates with carbon in the wood, accelerating combustion until it bursts into active flame [1 Mark: High concentration acceleration]."
    )
    return {
        "id": f"ns9_cr_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Insert a glowing wooden splint (ember) into the test tube; Splint relights/rekindles into flame; 100% oxygen concentration accelerates combustion compared to 21% in air",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "44_gas_tests_oxygen_glowing_splint_reignition",
        "misconception_tags": ["oxygen_gas_test_procedure"],
        "hints": {
            "tier_1": "Oxygen uses a glowing splint (not a burning flame).",
            "tier_2": "Glowing splint relights.",
            "tier_3": "Insert glowing splint; splint relights; pure oxygen accelerates combustion."
        }
    }


def arch_45_gas_tests_carbon_dioxide_limewater_milky(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During fermentation or marble-acid reactions, a colorless gas is produced.\n\n"
        "1. Describe the standard laboratory chemical test for **carbon dioxide gas ($CO_2$)**.\n"
        "2. What positive observation confirms the presence of carbon dioxide?\n"
        "3. Name the white insoluble chemical compound that precipitates out, causing this visual change ($CaCO_3$)."
    )
    sol = (
        "**Step 1:** Procedure: Bubble or pass the gas through a test tube containing **clear limewater (calcium hydroxide solution, $Ca(OH)_2$)** [1 Mark: Limewater procedure].\n\n"
        "**Step 2:** Observation: The clear solution turns **milky / cloudy white** [1 Mark: Milky white observation].\n\n"
        "**Step 3:** The cloudiness is caused by the formation of an insoluble white precipitate of **calcium carbonate ($CaCO_3$)**: $$\\text{Ca(OH)}_2 + \\text{CO}_2 \\rightarrow \\text{CaCO}_3(s) + \\text{H}_2\\text{O}$$ [1 Mark: Calcium carbonate precipitate]."
    )
    return {
        "id": f"ns9_cr_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Bubble gas through clear limewater (calcium hydroxide); Turns milky/cloudy white; Formation of insoluble calcium carbonate (CaCO3) precipitate",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "45_gas_tests_carbon_dioxide_limewater_milky",
        "misconception_tags": ["carbon_dioxide_limewater_test"],
        "hints": {
            "tier_1": "CO2 turns clear limewater milky.",
            "tier_2": "White cloudiness is calcium carbonate.",
            "tier_3": "Bubble through clear limewater; turns milky/cloudy; calcium carbonate (CaCO3)."
        }
    }


def arch_46_common_mistakes_altering_subscripts_to_balance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A student attempting to balance the synthesis of water ($H_2 + O_2 \\rightarrow H_2O$) writes:\n"
        "$$\\text{H}_2 + \\text{O}_2 \\rightarrow \\text{H}_2\\text{O}_2$$\n\n"
        "1. What major chemical error did the student commit?\n"
        "2. What compound did the student inadvertently write instead of water, and how do their domestic properties differ?\n"
        "3. State the correct balanced equation."
    )
    sol = (
        "**Step 1:** The student **altered a subscript** instead of adding a stoichiometric coefficient in front of the formula [1 Mark: Altered subscript].\n\n"
        "**Step 2:** The student wrote **hydrogen peroxide ($H_2O_2$)**, which is a toxic, corrosive, bleaching chemical completely different from harmless drinking water ($H_2O$) [1 Mark: Hydrogen peroxide].\n\n"
        "**Step 3:** Correct balanced equation: $$\\mathbf{2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}}$$ [1 Mark: Correct equation]."
    )
    return {
        "id": f"ns9_cr_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Altered subscripts instead of adding coefficients; Wrote hydrogen peroxide (toxic bleach) instead of water; 2H2 + O2 -> 2H2O",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "46_common_mistakes_altering_subscripts_to_balance",
        "misconception_tags": ["never_alter_subscripts_rule"],
        "hints": {
            "tier_1": "Never change subscripts. H2O2 is hair bleach.",
            "tier_2": "2H2 + O2 -> 2H2O.",
            "tier_3": "Altered subscripts; hydrogen peroxide; 2H2 + O2 -> 2H2O."
        }
    }


def arch_47_common_mistakes_inserting_coefficients_inside_formulas(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A student trying to balance $Mg + HCl \\rightarrow MgCl_2 + H_2$ writes:\n"
        "$$\\text{Mg} + \\text{H}_2\\text{Cl} \\rightarrow \\text{MgCl}_2 + \\text{H}_2$$\n"
        "or inserts a number inside the formula as '$H2Cl$'.\n\n"
        "1. Why is inserting numbers inside a chemical formula or altering element ratios scientifically invalid?\n"
        "2. Where is the only acceptable place to write a coefficient in a chemical equation?\n"
        "3. Write the correct balanced chemical equation."
    )
    sol = (
        "**Step 1:** Inserting numbers inside a formula or changing subscripts creates a **fictitious, non-existent chemical compound** ($H_2Cl$ does not exist in nature); formulas must reflect the true bonding ratios of elements [1 Mark: Non-existent chemical].\n\n"
        "**Step 2:** Coefficients can **only be written directly in front of the entire chemical formula** (e.g. $2HCl$) [1 Mark: In front of formula].\n\n"
        "**Step 3:** Correct balanced equation: $$\\mathbf{\\text{Mg} + 2\\text{HCl} \\rightarrow \\text{MgCl}_2 + \\text{H}_2}$$ [1 Mark: Correct equation]."
    )
    return {
        "id": f"ns9_cr_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Creates non-existent fictitious compound (H2Cl); Coefficients must only be placed directly in front of the entire formula; Mg + 2HCl -> MgCl2 + H2",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "47_common_mistakes_inserting_coefficients_inside_formulas",
        "misconception_tags": ["coefficients_in_front_only"],
        "hints": {
            "tier_1": "Coefficients must be in front of the whole formula: 2HCl.",
            "tier_2": "Mg + 2HCl -> MgCl2 + H2.",
            "tier_3": "Creates non-existent compound; in front only; Mg + 2HCl -> MgCl2 + H2."
        }
    }


def arch_48_evaluating_experimental_reaction_rate_temperature_effect(rng: random.Random) -> Dict[str, Any]:
    temperatures = [
        (20, 120, "slow bubbling"),
        (40, 45, "brisk effervescence"),
        (60, 15, "vigorous bubbling"),
    ]

    prompt = (
        "A group of learners investigates the reaction between zinc and hydrochloric acid at three different temperatures:\n"
        "- **Experiment 1 (20 °C):** Reaction takes 120 seconds to complete.\n"
        "- **Experiment 2 (40 °C):** Reaction takes 45 seconds to complete.\n"
        "- **Experiment 3 (60 °C):** Reaction takes 15 seconds to complete.\n\n"
        "1. Identify the **independent variable** and the **dependent variable** in this experiment.\n"
        "2. State the relationship between temperature and the rate of a chemical reaction.\n"
        "3. Explain this relationship at the particle level (kinetic energy and collision theory)."
    )
    sol = (
        "**Step 1:** **Independent variable:** Temperature of the acid; **Dependent variable:** Time taken for reaction to complete (reaction rate) [1 Mark: Variables].\n\n"
        "**Step 2:** Relationship: As temperature increases, the **rate of the chemical reaction increases** (reaction time decreases) [1 Mark: Relationship].\n\n"
        "**Step 3:** Particle explanation: Higher temperature gives particles **greater kinetic energy, causing them to move faster, collide more frequently, and collide with greater energy exceeding the activation energy threshold**, leading to more successful effective collisions per second [1 Mark: Collision theory]."
    )
    return {
        "id": f"ns9_cr_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "Independent: Temperature, Dependent: Reaction time / rate; As temperature increases, reaction rate increases; Particles move faster with more kinetic energy, producing more frequent and energetic successful collisions",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "48_evaluating_experimental_reaction_rate_temperature_effect",
        "misconception_tags": ["reaction_rate_temperature_collision_theory"],
        "hints": {
            "tier_1": "Higher temperature = faster particles = faster reaction.",
            "tier_2": "Independent = temperature; Dependent = time/rate.",
            "tier_3": "Independent: temp, Dependent: rate; higher temp increases rate; kinetic energy and collision theory."
        }
    }


def arch_49_scientific_inquiry_identifying_reaction_from_data_table(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Adding zinc granules to hydrochloric acid", "Vigorous fizzing", "Burns with a 'pop' sound", "Exothermic (gets warm)", "Metal + Acid reaction (Zn + 2HCl -> ZnCl2 + H2)"),
        ("Adding baking soda to vinegar", "Rapid effervescence", "Extinguishes a flame, turns limewater milky", "Endothermic (gets cold)", "Acid + Carbonate reaction (CH3COOH + NaHCO3 -> CH3COONa + H2O + CO2)"),
        ("Adding yeast to hydrogen peroxide", "Steady stream of gas bubbles", "Relights a glowing splint", "Exothermic (gentle warming)", "Catalytic decomposition (2H2O2 -> 2H2O + O2)"),
    ]
    setup, obs, gas_test, therm, full_rxn = rng.choice(scenarios)

    prompt = (
        f"A laboratory researcher investigates an unknown chemical reaction:\n"
        f"- **Experimental Setup:** {setup}\n"
        f"- **Visual Observation:** {obs}\n"
        f"- **Gas Confirmation Test:** {gas_test}\n"
        f"- **Thermal Measurement:** {therm}\n\n"
        f"1. Identify the gas evolved based on the gas confirmation test ({gas_test.split(' (')[0]}).\n"
        f"2. Classify the reaction as either **exothermic** or **endothermic**.\n"
        f"3. Identify the chemical reaction occurring: **{full_rxn}**."
    )
    gas_name = "Hydrogen gas (H2)" if "pop" in gas_test else ("Oxygen gas (O2)" if "glowing" in gas_test else "Carbon dioxide gas (CO2)")
    cat = "Exothermic" if "Exothermic" in therm else "Endothermic"

    sol = (
        f"**Step 1:** Gas evolved: **{gas_name}** [1 Mark: Gas identification].\n\n"
        f"**Step 2:** Thermal classification: **{cat}** [1 Mark: Energy classification].\n\n"
        f"**Step 3:** Chemical reaction: **{full_rxn}** [1 Mark: Reaction identification]."
    )
    return {
        "id": f"ns9_cr_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": f"{gas_name}; {cat}; {full_rxn}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "49_scientific_inquiry_identifying_reaction_from_data_table",
        "misconception_tags": ["reaction_identification_inquiry"],
        "hints": {
            "tier_1": f"Look at the gas test: {gas_test}.",
            "tier_2": f"Gas is {gas_name}, reaction is {cat}.",
            "tier_3": f"{gas_name}; {cat}; {full_rxn}."
        }
    }


def arch_50_chemical_reactions_master_synthesis_and_balancing_challenge(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Complete the comprehensive Grade 9 Chemical Reactions master synthesis challenge:\n\n"
        "1. **Balancing Equations:** Balance each of the following equations:\n"
        "   - (a) $\\text{Mg} + \\text{O}_2 \\rightarrow \\text{MgO}$\n"
        "   - (b) $\\text{CH}_4 + \\text{O}_2 \\rightarrow \\text{CO}_2 + \\text{H}_2\\text{O}$\n"
        "   - (c) $\\text{Zn} + \\text{HCl} \\rightarrow \\text{ZnCl}_2 + \\text{H}_2$\n"
        "2. **Conservation of Mass:** If $24\\text{ g}$ of magnesium reacts completely with $16\\text{ g}$ of oxygen gas, calculate the mass of magnesium oxide formed.\n"
        "3. **Energy in Reactions:** Explain why a reaction is exothermic if bond-making releases more energy than bond-breaking requires.\n"
        "4. **Gas Identification:** Name the laboratory test and positive result for (a) hydrogen gas and (b) carbon dioxide gas."
    )
    sol = (
        "**Step 1:** Balanced equations:\n"
        "- (a) $$\\mathbf{2\\text{Mg} + \\text{O}_2 \\rightarrow 2\\text{MgO}}$$\n"
        "- (b) $$\\mathbf{\\text{CH}_4 + 2\\text{O}_2 \\rightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O}}$$\n"
        "- (c) $$\\mathbf{\\text{Zn} + 2\\text{HCl} \\rightarrow \\text{ZnCl}_2 + \\text{H}_2}$$ [1 Mark: Balanced equations].\n\n"
        "**Step 2:** Conservation of Mass: $$\\text{Mass of products} = 24\\text{ g} + 16\\text{ g} = \\mathbf{40\\text{ g of MgO}}$$ [1 Mark: 40 g MgO].\n\n"
        "**Step 3:** Energy: Since forming bonds releases energy and breaking bonds absorbs energy, when energy released exceeds energy absorbed, the net excess energy is transferred to the surroundings as heat, making it **exothermic** [1 Mark: Exothermic explanation].\n\n"
        "**Step 4:** Gas tests:\n"
        "- (a) Hydrogen: **Burning splint makes a 'pop' sound**.\n"
        "- (b) Carbon dioxide: **Clear limewater turns milky white** [1 Mark: Gas tests]."
    )
    return {
        "id": f"ns9_cr_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": "2Mg + O2 -> 2MgO; CH4 + 2O2 -> CO2 + 2H2O; Zn + 2HCl -> ZnCl2 + H2; Mass = 40 g MgO; Exothermic because net energy is released; H2: burning splint pops, CO2: limewater turns milky",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "term": 2,
        "subskill": "50_chemical_reactions_master_synthesis_and_balancing_challenge",
        "misconception_tags": ["chemical_reactions_master_synthesis"],
        "hints": {
            "tier_1": "2Mg + O2 -> 2MgO. CH4 + 2O2 -> CO2 + 2H2O. Zn + 2HCl -> ZnCl2 + H2. 24 + 16 = 40 g.",
            "tier_2": "Exothermic = releases heat. Hydrogen pops, CO2 turns limewater milky.",
            "tier_3": "Balanced equations; 40 g; net energy released; pop test and limewater milky."
        }
    }


# ==============================================================================
# DISPATCH DICT (26 - 50)
# ==============================================================================

BUILDERS_26_50 = {
    "26_why_equations_must_be_balanced_stoichiometry": arch_26_why_equations_must_be_balanced_stoichiometry,
    "27_balancing_synthesis_hydrogen_and_oxygen_to_water": arch_27_balancing_synthesis_hydrogen_and_oxygen_to_water,
    "28_balancing_synthesis_magnesium_and_oxygen_to_magnesium_oxide": arch_28_balancing_synthesis_magnesium_and_oxygen_to_magnesium_oxide,
    "29_balancing_synthesis_iron_and_oxygen_to_iron_iii_oxide": arch_29_balancing_synthesis_iron_and_oxygen_to_iron_iii_oxide,
    "30_balancing_synthesis_iron_and_sulfur_to_iron_ii_sulfide": arch_30_balancing_synthesis_iron_and_sulfur_to_iron_ii_sulfide,
    "31_balancing_combustion_carbon_to_carbon_dioxide": arch_31_balancing_combustion_carbon_to_carbon_dioxide,
    "32_balancing_combustion_carbon_to_carbon_monoxide": arch_32_balancing_combustion_carbon_to_carbon_monoxide,
    "33_balancing_combustion_methane_gas_ch4_plus_o2": arch_33_balancing_combustion_methane_gas_ch4_plus_o2,
    "34_balancing_combustion_propane_gas_c3h8_plus_o2": arch_34_balancing_combustion_propane_gas_c3h8_plus_o2,
    "35_balancing_decomposition_hydrogen_peroxide_catalyst": arch_35_balancing_decomposition_hydrogen_peroxide_catalyst,
    "36_balancing_decomposition_calcium_carbonate_thermal": arch_36_balancing_decomposition_calcium_carbonate_thermal,
    "37_balancing_decomposition_potassium_chlorate_to_kcl_and_o2": arch_37_balancing_decomposition_potassium_chlorate_to_kcl_and_o2,
    "38_balancing_metal_acid_zinc_and_hydrochloric_acid": arch_38_balancing_metal_acid_zinc_and_hydrochloric_acid,
    "39_balancing_metal_acid_magnesium_and_hydrochloric_acid": arch_39_balancing_metal_acid_magnesium_and_hydrochloric_acid,
    "40_balancing_metal_acid_iron_and_hydrochloric_acid": arch_40_balancing_metal_acid_iron_and_hydrochloric_acid,
    "41_balancing_neutralization_hydrochloric_acid_and_sodium_hydroxide": arch_41_balancing_neutralization_hydrochloric_acid_and_sodium_hydroxide,
    "42_balancing_acid_carbonate_calcium_carbonate_and_hydrochloric_acid": arch_42_balancing_acid_carbonate_calcium_carbonate_and_hydrochloric_acid,
    "43_gas_tests_hydrogen_pop_test_investigation": arch_43_gas_tests_hydrogen_pop_test_investigation,
    "44_gas_tests_oxygen_glowing_splint_reignition": arch_44_gas_tests_oxygen_glowing_splint_reignition,
    "45_gas_tests_carbon_dioxide_limewater_milky": arch_45_gas_tests_carbon_dioxide_limewater_milky,
    "46_common_mistakes_altering_subscripts_to_balance": arch_46_common_mistakes_altering_subscripts_to_balance,
    "47_common_mistakes_inserting_coefficients_inside_formulas": arch_47_common_mistakes_inserting_coefficients_inside_formulas,
    "48_evaluating_experimental_reaction_rate_temperature_effect": arch_48_evaluating_experimental_reaction_rate_temperature_effect,
    "49_scientific_inquiry_identifying_reaction_from_data_table": arch_49_scientific_inquiry_identifying_reaction_from_data_table,
    "50_chemical_reactions_master_synthesis_and_balancing_challenge": arch_50_chemical_reactions_master_synthesis_and_balancing_challenge,
}
