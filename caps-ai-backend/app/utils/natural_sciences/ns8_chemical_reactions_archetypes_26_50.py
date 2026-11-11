"""
Grade 8 Natural Sciences - Term 2: Chemical Reactions (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/PDF - Chemical reactions.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Balancing Chemical Equations (26 - 34)
# ==============================================================================

def arch_26_why_equations_must_be_balanced(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In chemistry, every symbolic chemical equation must be correctly balanced before it can be used for calculations.\n\n"
        f"1. What fundamental scientific law dictates that chemical equations must be balanced?\n"
        f"2. Explain what it means to say an equation is 'balanced' in terms of atoms.\n"
        f"3. In the unbalanced equation $H_2 + O_2 \\rightarrow H_2O$, identify which element is not balanced and state how many atoms are missing on the product side."
    )
    sol = (
        f"**Step 1:** The **Law of Conservation of Mass (or Conservation of Atoms)** [1 Mark: Scientific law].\n\n"
        f"**Step 2:** An equation is balanced when the **total number of atoms of each individual element on the reactants side (left) is exactly equal to the total number on the products side (right)** [1 Mark: Definition].\n\n"
        f"**Step 3:** **Oxygen** is unbalanced; there are 2 oxygen atoms on the left ($O_2$) but only 1 oxygen atom on the right ($H_2O$), so **1 oxygen atom is missing** on the product side [1 Mark: Unbalanced identification]."
    )
    return {
        "id": f"ns8_chem_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Law of Conservation of Mass/Atoms; Equal number of each element's atoms on both sides; Oxygen is unbalanced (2 on left vs 1 on right)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "26_why_equations_must_be_balanced",
        "misconception_tags": ["why_equations_must_be_balanced"],
        "hints": {
            "tier_1": "Atoms cannot vanish. Left must equal right.",
            "tier_2": "Look at oxygen in H2 + O2 -> H2O: 2 on the left, 1 on the right.",
            "tier_3": "Law of Conservation of Mass/Atoms; equal atom counts; oxygen has 2 on left, 1 on right."
        }
    }


def arch_27_balancing_synthesis_reactions_magnesium_oxide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Silvery magnesium ribbon burns with a blinding white light in oxygen gas to form white magnesium oxide powder.\n\n"
        "Consider the unbalanced chemical equation:\n"
        "$$\\text{Mg} + \\text{O}_2 \\rightarrow \\text{MgO}$$\n\n"
        "1. Explain why this equation as written is not yet balanced.\n"
        "2. Write the fully balanced chemical equation using whole-number stoichiometric coefficients.\n"
        "3. Verify that your balanced equation satisfies the Law of Conservation of Atoms."
    )
    sol = (
        f"**Step 1:** The reactants have 2 oxygen atoms ($O_2$) while the product has only 1 oxygen atom ($MgO$), violating atom conservation [1 Mark: Unbalanced reason].\n\n"
        f"**Step 2:** Balanced equation: $$\\mathbf{{2\\text{{Mg}} + \\text{{O}}_2 \\rightarrow 2\\text{{MgO}}}}$$ [1 Mark: Balanced equation].\n\n"
        f"**Step 3:** Verification: Reactants have $2\\text{{ Mg}}$ and $2\\text{{ O}}$; Products have $2\\text{{ Mg}}$ and $2\\text{{ O}}$. Both sides are equal ($2=2$ and $2=2$) [1 Mark: Verification]."
    )
    return {
        "id": f"ns8_chem_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Oxygen is unbalanced (2 on left, 1 on right); 2Mg + O2 -> 2MgO; Left has 2 Mg, 2 O and Right has 2 Mg, 2 O",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "27_balancing_synthesis_reactions_magnesium_oxide",
        "misconception_tags": ["balancing_magnesium_combustion"],
        "hints": {
            "tier_1": "You need 2 MgO to balance the 2 oxygens, which requires 2 Mg in front.",
            "tier_2": "Coefficients: 2, 1, 2.",
            "tier_3": "2Mg + O2 -> 2MgO; 2 Mg and 2 O on both sides."
        }
    }


def arch_28_balancing_synthesis_reactions_water(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Hydrogen gas burns explosively in oxygen gas to form liquid water:\n"
        "$$\\text{H}_2 + \\text{O}_2 \\rightarrow \\text{H}_2\\text{O}$$\n\n"
        "1. Write the correct balanced chemical equation for the synthesis of water.\n"
        "2. How many molecules of hydrogen gas ($H_2$) are needed to react completely with $1$ molecule of oxygen gas ($O_2$)?\n"
        "3. How many water molecules are produced from this reaction?"
    )
    sol = (
        f"**Step 1:** Balanced equation: $$\\mathbf{{2\\text{{H}}_2 + \\text{{O}}_2 \\rightarrow 2\\text{{H}}_2\\text{{O}}}}$$ [1 Mark: Balanced equation].\n\n"
        f"**Step 2:** Exactly **$2$ molecules of hydrogen gas ($2H_2$)** are needed per $1$ molecule of $O_2$ [1 Mark: Hydrogen molecules].\n\n"
        f"**Step 3:** Exactly **$2$ molecules of water ($2H_2O$)** are formed [1 Mark: Water molecules]."
    )
    return {
        "id": f"ns8_chem_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "2H2 + O2 -> 2H2O; 2 molecules of H2; 2 molecules of H2O produced",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "28_balancing_synthesis_reactions_water",
        "misconception_tags": ["balancing_water_synthesis"],
        "hints": {
            "tier_1": "Put a 2 in front of H2 and a 2 in front of H2O.",
            "tier_2": "2H2 + O2 -> 2H2O.",
            "tier_3": "2H2 + O2 -> 2H2O; 2 H2 molecules; 2 H2O molecules."
        }
    }


def arch_29_balancing_synthesis_reactions_iron_sulfide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When iron filings and sulfur powder are heated, they react to produce iron(II) sulfide:\n"
        "$$\\text{Fe} + \\text{S} \\rightarrow \\text{FeS}$$\n\n"
        "1. Is this equation already balanced as written? Show atom counts for iron and sulfur.\n"
        "2. What is the stoichiometric ratio of iron atoms to sulfur atoms in this reaction?\n"
        "3. If 50 iron atoms react with 50 sulfur atoms, how many formula units of iron sulfide ($FeS$) are formed?"
    )
    sol = (
        f"**Step 1:** **Yes, it is already balanced**; Reactants have 1 Fe and 1 S; Products have 1 Fe and 1 S [1 Mark: Balanced verification].\n\n"
        f"**Step 2:** The ratio is **$1 : 1$** (one iron atom reacts with one sulfur atom) [1 Mark: Ratio].\n\n"
        f"**Step 3:** Exactly **$50$ units of iron sulfide ($FeS$)** are formed [1 Mark: Product units]."
    )
    return {
        "id": f"ns8_chem_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Yes, already balanced (1 Fe, 1 S on each side); 1:1 ratio; 50 units of FeS formed",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "29_balancing_synthesis_reactions_iron_sulfide",
        "misconception_tags": ["one_to_one_stoichiometry"],
        "hints": {
            "tier_1": "Check atom counts on left and right: Fe is 1, S is 1.",
            "tier_2": "It's a 1 to 1 reaction.",
            "tier_3": "Already balanced; 1:1 ratio; 50 units."
        }
    }


def arch_30_balancing_combustion_carbon_and_carbon_monoxide(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("Complete combustion of carbon", "C + O_2 -> CO_2", "sufficient oxygen available", "carbon dioxide ($CO_2$)"),
        ("Incomplete combustion of carbon", "2C + O_2 -> 2CO", "limited oxygen supply", "toxic carbon monoxide ($CO$)"),
    ]
    t_name, eq, cond, prod = rng.choice(types)

    prompt = (
        f"The combustion of carbon fuel (coal / charcoal) depends on the amount of oxygen available:\n"
        f"**{t_name}** ({cond}).\n\n"
        f"1. Write the balanced chemical equation for this reaction ({eq}).\n"
        f"2. Show atom counts on both sides to verify that it is balanced.\n"
        f"3. Explain why {prod} is formed instead of other products under these conditions."
    )
    sol = (
        f"**Step 1:** Balanced equation: $$\\mathbf{{{eq}}}$$ [1 Mark: Equation].\n\n"
        f"**Step 2:** Atom counts: Reactants and products both have identical counts of carbon and oxygen atoms [1 Mark: Atom counts].\n\n"
        f"**Step 3:** When oxygen is {'abundant, carbon atoms can fully bond with 2 oxygen atoms each forming non-toxic CO2' if 'Complete' in t_name else 'limited/scarce, there are not enough oxygen atoms to form CO2, so each carbon atom bonds with only 1 oxygen atom forming toxic CO'} [1 Mark: Explanation]."
    )
    return {
        "id": f"ns8_chem_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{eq}; Atom counts equal on both sides; Formed because oxygen is {cond.split(' ')[0]}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "30_balancing_combustion_carbon_and_carbon_monoxide",
        "misconception_tags": ["complete_vs_incomplete_combustion_balancing"],
        "hints": {
            "tier_1": f"Equation for {t_name}: {eq}.",
            "tier_2": "Complete makes CO2; incomplete makes CO.",
            "tier_3": f"{eq}; equal atom counts; formed due to {cond}."
        }
    }


def arch_31_balancing_decomposition_hydrogen_peroxide(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Hydrogen peroxide decomposes into water and oxygen gas in the presence of a catalyst:\n"
        "$$\\text{H}_2\\text{O}_2 \\rightarrow \\text{H}_2\\text{O} + \\text{O}_2$$\n\n"
        "1. Write the fully balanced chemical equation for the decomposition of hydrogen peroxide.\n"
        "2. How many molecules of hydrogen peroxide must decompose to release $1$ molecule of oxygen gas ($O_2$)?\n"
        "3. State the role of the catalyst (manganese dioxide) in this reaction."
    )
    sol = (
        f"**Step 1:** Balanced equation: $$\\mathbf{{2\\text{{H}}_2\\text{{O}}_2 \\rightarrow 2\\text{{H}}_2\\text{{O}} + \\text{{O}}_2}}$$ [1 Mark: Balanced equation].\n\n"
        f"**Step 2:** Exactly **$2$ molecules of $H_2O_2$** are required to produce $1$ molecule of $O_2$ [1 Mark: Molecule count].\n\n"
        f"**Step 3:** The catalyst **speeds up the chemical reaction** without being chemically changed or consumed in the process [1 Mark: Catalyst definition]."
    )
    return {
        "id": f"ns8_chem_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "2H2O2 -> 2H2O + O2; 2 molecules of H2O2; Catalyst speeds up the reaction without being consumed",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "31_balancing_decomposition_hydrogen_peroxide",
        "misconception_tags": ["balancing_peroxide_decomposition"],
        "hints": {
            "tier_1": "2H2O2 produces 2H2O and 1 O2.",
            "tier_2": "A catalyst speeds up the reaction without being used up.",
            "tier_3": "2H2O2 -> 2H2O + O2; 2 molecules; catalyst speeds up reaction."
        }
    }


def arch_32_balancing_metal_acid_reaction_zinc_hydrochloric(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Zinc granules react with dilute hydrochloric acid to produce zinc chloride and flammable hydrogen gas:\n"
        "$$\\text{Zn} + \\text{HCl} \\rightarrow \\text{ZnCl}_2 + \\text{H}_2$$\n\n"
        "1. Write the fully balanced chemical equation for this reaction.\n"
        "2. What single coefficient must be added to balance the equation?\n"
        "3. Describe the laboratory test used to confirm that the gas formed is hydrogen."
    )
    sol = (
        f"**Step 1:** Balanced equation: $$\\mathbf{{\\text{{Zn}} + 2\\text{{HCl}} \\rightarrow \\text{{ZnCl}}_2 + \\text{{H}}_2}}$$ [1 Mark: Balanced equation].\n\n"
        f"**Step 2:** A coefficient of **$2$ in front of $HCl$** balances both the $H$ and $Cl$ atoms [1 Mark: Coefficient].\n\n"
        f"**Step 3:** Bring a **burning wooden splint** near the mouth of the test tube: the gas burns with a distinctive **'pop' sound** [1 Mark: Hydrogen pop test]."
    )
    return {
        "id": f"ns8_chem_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Zn + 2HCl -> ZnCl2 + H2; Coefficient of 2 in front of HCl; Burning splint makes a 'pop' sound",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "32_balancing_metal_acid_reaction_zinc_hydrochloric",
        "misconception_tags": ["metal_acid_balancing"],
        "hints": {
            "tier_1": "You have 2 Cl and 2 H on the right, so put a 2 in front of HCl.",
            "tier_2": "Hydrogen burns with a 'pop'.",
            "tier_3": "Zn + 2HCl -> ZnCl2 + H2; 2 in front of HCl; burning splint pop test."
        }
    }


def arch_33_balancing_rusting_reaction_iron_oxygen(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When iron metal rusts in air, it reacts with oxygen to form reddish-brown iron(III) oxide:\n"
        "$$\\text{Fe} + \\text{O}_2 \\rightarrow \\text{Fe}_2\\text{O}_3$$\n\n"
        "1. Balance this chemical equation using whole-number coefficients.\n"
        "2. State the final coefficients in order from left to right (Fe, O2, Fe2O3).\n"
        "3. How many total iron atoms and total oxygen atoms are present on each side of the balanced equation?"
    )
    sol = (
        f"**Step 1:** Balanced equation: $$\\mathbf{{4\\text{{Fe}} + 3\\text{{O}}_2 \\rightarrow 2\\text{{Fe}}_2\\text{{O}}_3}}$$ [1 Mark: Equation].\n\n"
        f"**Step 2:** Coefficients: **4, 3, 2** [1 Mark: Coefficients].\n\n"
        f"**Step 3:** Total atoms on each side: **4 iron atoms** ($4\\text{{ Fe}}$) and **6 oxygen atoms** ($3 \\times 2 = 6\\text{{ O}}$) [1 Mark: Atom totals]."
    )
    return {
        "id": f"ns8_chem_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "4Fe + 3O2 -> 2Fe2O3; Coefficients: 4, 3, 2; 4 Fe atoms and 6 O atoms on each side",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "33_balancing_rusting_reaction_iron_oxygen",
        "misconception_tags": ["balancing_iron_oxide_rusting"],
        "hints": {
            "tier_1": "Find the lowest common multiple of 2 and 3 for oxygen (6).",
            "tier_2": "3 O2 gives 6 oxygens, 2 Fe2O3 gives 6 oxygens, so you need 4 Fe.",
            "tier_3": "4Fe + 3O2 -> 2Fe2O3; 4, 3, 2; 4 Fe and 6 O on each side."
        }
    }


def arch_34_common_mistakes_changing_subscripts_vs_coefficients(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A student attempts to balance $H_2 + O_2 \\rightarrow H_2O$ by changing the formula of water to $H_2O_2$:\n"
        "$$\\text{H}_2 + \\text{O}_2 \\rightarrow \\text{H}_2\\text{O}_2$$\n\n"
        "1. Why is changing chemical subscripts strictly forbidden when balancing chemical equations?\n"
        "2. What chemical compound did the student inadvertently write instead of water, and how do their properties differ?\n"
        "3. What is the only number that a chemist is allowed to adjust when balancing an equation?"
    )
    sol = (
        f"**Step 1:** Changing a subscript changes the **chemical formula and identity of the substance**; subscripts define how atoms are bonded in a specific molecule [1 Mark: Subscript rule].\n\n"
        f"**Step 2:** The student wrote **hydrogen peroxide ($H_2O_2$)**, a toxic, corrosive bleaching chemical, instead of harmless drinking water ($H_2O$) [1 Mark: Chemical identity error].\n\n"
        f"**Step 3:** Chemists are only allowed to change the **coefficients in front of the chemical formulas** (which change the number of molecules, not their identity) [1 Mark: Coefficients only]."
    )
    return {
        "id": f"ns8_chem_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Changing subscripts changes the chemical identity/substance; Wrote hydrogen peroxide (toxic bleach) instead of water; Only stoichiometric coefficients in front can be changed",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "34_common_mistakes_changing_subscripts_vs_coefficients",
        "misconception_tags": ["never_change_subscripts_rule"],
        "hints": {
            "tier_1": "Never touch the small subscript numbers! You create a completely different chemical.",
            "tier_2": "H2O2 is bleach, not water. Only change big numbers in front (coefficients).",
            "tier_3": "Subscripts define identity; H2O2 is toxic bleach; only change coefficients."
        }
    }


# ==============================================================================
# CLUSTER 5: Real-World Reactions & Indigenous Technologies (35 - 42)
# ==============================================================================

def arch_35_fermentation_definition_and_microorganisms(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Fermentation is an ancient biochemical reaction used by humans for thousands of years.\n\n"
        f"1. Define the chemical process of **fermentation**.\n"
        f"2. Write the word equation for the fermentation of glucose by yeast.\n"
        f"3. Name the microscopic single-celled fungus responsible for this fermentation reaction."
    )
    sol = (
        f"**Step 1:** Fermentation is the **anaerobic chemical breakdown of sugars (carbohydrates) by microorganisms** (such as yeast or bacteria) to produce alcohol, acids, and carbon dioxide [1 Mark: Definition].\n\n"
        f"**Step 2:** Word equation: **Glucose $\\rightarrow$ Alcohol (Ethanol) + Carbon dioxide** [1 Mark: Word equation].\n\n"
        f"**Step 3:** The microorganism is **yeast** (a microscopic single-celled fungus) [1 Mark: Yeast microorganism]."
    )
    return {
        "id": f"ns8_chem_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Anaerobic breakdown of sugars by microorganisms; Glucose -> Alcohol + Carbon dioxide; Yeast",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "35_fermentation_definition_and_microorganisms",
        "misconception_tags": ["fermentation_definition"],
        "hints": {
            "tier_1": "Sugar breaks down into alcohol and carbon dioxide gas.",
            "tier_2": "Microorganism: yeast.",
            "tier_3": "Anaerobic sugar breakdown; Glucose -> Alcohol + CO2; Yeast."
        }
    }


def arch_36_indigenous_brewing_umqombothi_and_ginger_beer(rng: random.Random) -> Dict[str, Any]:
    beverages = [
        ("Umqombothi (traditional African sorghum beer)", "crushed maize, sorghum malt, water, and wild yeasts", "a creamy, nutrient-rich beverage with a low alcohol content (~3%)"),
        ("Traditional homemade ginger beer", "sugar, ginger root, cream of tartar, water, and baker's yeast", "a naturally carbonated, effervescent fermented drink"),
    ]
    name, ingredients, desc = rng.choice(beverages)

    prompt = (
        f"Indigenous communities across South Africa have practiced biotechnology for generations:\n"
        f"**{name}** ({ingredients}).\n\n"
        f"1. What biological/chemical reaction takes place during the brewing of {name.split(' (')[0]}?\n"
        f"2. What gas is produced during fermentation that creates the foam, head, or fizz in the beverage?\n"
        f"3. Explain why indigenous brewing was historically an important source of nutrition (B-vitamins and minerals) in African societies."
    )
    sol = (
        f"**Step 1:** The reaction is **fermentation** (conversion of starches/sugars by yeast into alcohol and carbon dioxide) [1 Mark: Reaction].\n\n"
        f"**Step 2:** The gas produced is **carbon dioxide ($CO_2$)** [1 Mark: Gas].\n\n"
        f"**Step 3:** Live yeast cells and fermented malted grains are rich in **B-complex vitamins, amino acids, and essential minerals**, providing valuable dietary nutrition beyond simple hydration [1 Mark: Nutritional value]."
    )
    return {
        "id": f"ns8_chem_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Fermentation; Carbon dioxide (CO2); Yeast and malted grain provide B-vitamins, minerals, and nutrients",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "36_indigenous_brewing_umqombothi_and_ginger_beer",
        "misconception_tags": ["indigenous_fermentation_technology"],
        "hints": {
            "tier_1": "Yeast ferments the sorghum/sugar into alcohol and CO2.",
            "tier_2": "CO2 makes the bubbles and foam.",
            "tier_3": "Fermentation; Carbon dioxide; Yeast provides B-vitamins and nutrition."
        }
    }


def arch_37_fermentation_in_baking_bread(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When baking bread, baker's yeast ($Saccharomyces\\ cerevisiae$) is mixed with flour, warm water, and a pinch of sugar.\n\n"
        f"1. Explain why the bread dough rises and expands when left in a warm place for an hour.\n"
        f"2. What happens to the alcohol (ethanol) produced by the yeast when the bread is baked in a hot oven?\n"
        f"3. Why are there numerous small holes (spongy texture) visible when you slice into a loaf of baked bread?"
    )
    sol = (
        f"**Step 1:** Yeast undergoes fermentation, feeding on sugar and releasing **carbon dioxide gas ($CO_2$)**; the trapped gas bubbles get trapped in the elastic gluten network, causing the dough to swell and rise [1 Mark: Dough rising].\n\n"
        f"**Step 2:** The high temperature of the oven causes the alcohol to **evaporate completely into the air** [1 Mark: Alcohol evaporation].\n\n"
        f"**Step 3:** The holes are the **permanent pockets left behind by expanding carbon dioxide gas bubbles** as the bread dough baked and solidified [1 Mark: Spongy bread texture]."
    )
    return {
        "id": f"ns8_chem_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "CO2 gas bubbles expand the dough; Alcohol evaporates completely in hot oven; Holes are pockets left by trapped CO2 gas bubbles",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "37_fermentation_in_baking_bread",
        "misconception_tags": ["bread_fermentation_co2"],
        "hints": {
            "tier_1": "Yeast makes carbon dioxide bubbles that blow up the dough like little balloons.",
            "tier_2": "The alcohol evaporates away in the hot oven.",
            "tier_3": "CO2 gas rises the dough; alcohol evaporates; holes left by trapped CO2 bubbles."
        }
    }


def arch_38_fermentation_in_dairy_amasi_and_yoghurt(rng: random.Random) -> Dict[str, Any]:
    dairy = [
        ("Amasi (traditional South African sour milk)", "raw or pasteurised milk naturally fermented in a calabash or clay pot", "lactic acid curdles milk proteins into thick curds and watery whey"),
        ("Yoghurt", "milk fermented using Lactobacillus bulgaricus and Streptococcus thermophilus cultures", "produces a creamy, tangy spoonable dairy product"),
    ]
    name, method, desc = rng.choice(dairy)

    prompt = (
        f"In dairy fermentation: **{name}** ({method}).\n\n"
        f"1. What type of microorganism is responsible for dairy fermentation (bacteria or yeast)?\n"
        f"2. What milk sugar is consumed during this process, and what acid is produced that gives the sour/tangy taste?\n"
        f"3. Why was fermentation historically an essential indigenous technique for preserving milk before refrigeration?"
    )
    sol = (
        f"**Step 1:** **Lactic acid bacteria** are responsible [1 Mark: Bacteria].\n\n"
        f"**Step 2:** Bacteria consume **lactose (milk sugar)** and convert it into **lactic acid** [1 Mark: Lactose to lactic acid].\n\n"
        f"**Step 3:** The production of lactic acid **lowers the pH (makes it acidic)**, which kills or prevents the growth of harmful food-spoiling pathogens and dangerous bacteria, effectively preserving the milk safely for days without refrigeration [1 Mark: Preservation mechanism]."
    )
    return {
        "id": f"ns8_chem_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Bacteria (lactic acid bacteria); Lactose converted to lactic acid; Acidic pH kills harmful bacteria, preserving milk without refrigeration",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "38_fermentation_in_dairy_amasi_and_yoghurt",
        "misconception_tags": ["dairy_fermentation_preservation"],
        "hints": {
            "tier_1": "Lactic acid bacteria turn milk sugar (lactose) into lactic acid.",
            "tier_2": "Acid stops bad bacteria from growing, preserving the milk.",
            "tier_3": "Bacteria; lactose to lactic acid; acidic pH preserves milk."
        }
    }


def arch_39_indigenous_metal_smelting_iron_and_copper(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Centuries before European colonization, indigenous African metallurgists operated clay bloomery furnaces across Southern Africa (e.g. Mapungubwe, Phalaborwa, and Melville Koppies).\n\n"
        f"1. Explain what **metal smelting** is in terms of chemical reactions.\n"
        f"2. What raw fuel was burned in the furnace to provide both extreme heat and the carbon monoxide reducing gas?\n"
        f"3. Write a word equation summarizing the extraction of iron from iron ore (iron oxide) using carbon monoxide gas."
    )
    sol = (
        f"**Step 1:** Smelting is a **chemical reduction reaction** in which a metal ore (metal compound) is heated with a reducing agent to extract pure molten metal from the rock [1 Mark: Smelting definition].\n\n"
        f"**Step 2:** **Charcoal** (produced by slowly burning selected indigenous hardwood trees) [1 Mark: Charcoal fuel].\n\n"
        f"**Step 3:** Word equation: **Iron oxide + Carbon monoxide $\\rightarrow$ Iron + Carbon dioxide** [1 Mark: Word equation]."
    )
    return {
        "id": f"ns8_chem_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Chemical reduction extracting metal from mineral ore; Charcoal fuel; Iron oxide + Carbon monoxide -> Iron + Carbon dioxide",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "39_indigenous_metal_smelting_iron_and_copper",
        "misconception_tags": ["indigenous_smelting_reactions"],
        "hints": {
            "tier_1": "Smelting extracts pure metal from rocks using charcoal and air bellows.",
            "tier_2": "Iron oxide + Carbon monoxide -> Iron + Carbon dioxide.",
            "tier_3": "Chemical reduction of ore; charcoal; Iron oxide + Carbon monoxide -> Iron + Carbon dioxide."
        }
    }


def arch_40_combustion_of_fossil_fuels_coal_and_paraffin(rng: random.Random) -> Dict[str, Any]:
    fuels = [
        ("Coal burned in South African coal-fired power stations (Eskom)", "releases vast heat energy to boil water into high-pressure steam for turbines"),
        ("Paraffin (kerosene) burned in household heaters and wick lamps", "combusts to provide domestic warmth and illumination"),
    ]
    fuel, context = rng.choice(fuels)

    prompt = (
        f"Fossil fuels supply the majority of South Africa's electrical and domestic energy: **{fuel}** ({context}).\n\n"
        f"1. What two major chemical products are released into the atmosphere during the combustion of fossil fuels?\n"
        f"2. Which of these gases is the principal greenhouse gas responsible for global climate change?\n"
        f"3. Name one harmful pollutant gas produced when coal containing sulfur impurities is burned."
    )
    sol = (
        f"**Step 1:** Combustion produces **carbon dioxide ($CO_2$)** and **water vapor ($H_2O$)** [1 Mark: Two combustion products].\n\n"
        f"**Step 2:** **Carbon dioxide ($CO_2$)** is the primary greenhouse gas [1 Mark: Greenhouse gas].\n\n"
        f"**Step 3:** Burning sulfur impurities produces **sulfur dioxide ($SO_2$)**, which dissolves in cloud moisture to form harmful **acid rain** [1 Mark: Sulfur dioxide / Acid rain]."
    )
    return {
        "id": f"ns8_chem_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Carbon dioxide and water vapor; Carbon dioxide (CO2); Sulfur dioxide (causes acid rain)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "40_combustion_of_fossil_fuels_coal_and_paraffin",
        "misconception_tags": ["fossil_fuel_combustion_environment"],
        "hints": {
            "tier_1": "Burning fossil fuels makes CO2 and water.",
            "tier_2": "CO2 causes global warming; sulfur causes acid rain.",
            "tier_3": "Carbon dioxide and water vapor; CO2 greenhouse gas; sulfur dioxide (acid rain)."
        }
    }


def arch_41_rusting_corrosion_conditions_water_and_oxygen(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Rusting is an expensive and destructive form of chemical corrosion that affects iron and steel structures.\n\n"
        f"1. Name the **two essential substances** that must BOTH be present for iron to rust.\n"
        f"2. Write the word equation for the chemical reaction of rusting.\n"
        f"3. Why do metal objects rust significantly faster in coastal cities (like Durban or Cape Town) than in inland dry areas (like Johannesburg)?"
    )
    sol = (
        f"**Step 1:** The two essential substances are **oxygen (air)** and **water (moisture)** [1 Mark: Essential conditions].\n\n"
        f"**Step 2:** Word equation: **Iron + Oxygen + Water $\\rightarrow$ Hydrated iron(III) oxide (Rust)** [1 Mark: Word equation].\n\n"
        f"**Step 3:** Coastal air contains high levels of **salt (sodium chloride spray)** and humidity; dissolved salt ions act as an electrolyte that speeds up the transfer of electrons, accelerating the rusting reaction [1 Mark: Coastal salt effect]."
    )
    return {
        "id": f"ns8_chem_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Oxygen and Water; Iron + Oxygen + Water -> Hydrated iron oxide (rust); Salt spray and high humidity accelerate electron transfer (rusting)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "41_rusting_corrosion_conditions_water_and_oxygen",
        "misconception_tags": ["rusting_conditions_and_salt"],
        "hints": {
            "tier_1": "Iron needs BOTH water and oxygen to rust. Neither alone is enough.",
            "tier_2": "Sea salt accelerates rusting greatly.",
            "tier_3": "Oxygen and water; Iron + Oxygen + Water -> Hydrated iron oxide; salt spray speeds reaction."
        }
    }


def arch_42_rust_prevention_methods_painting_galvanising(rng: random.Random) -> Dict[str, Any]:
    methods = [
        ("Painting metal gates and car bodies", "forms an airtight, watertight barrier layer over the iron surface"),
        ("Galvanising corrugated iron roofing sheets", "coating iron with a layer of zinc metal, which protects physically and sacrifices itself"),
        ("Oiling or greasing bicycle chains and machine gears", "creates a water-repellent protective film while allowing moving parts to slide smoothly"),
    ]
    m_name, m_mech = rng.choice(methods)

    prompt = (
        f"Preventing rust saves billions of rands annually in infrastructure repair.\n\n"
        f"Consider the protection method: **{m_name}** ({m_mech}).\n\n"
        f"1. How does this method prevent iron from rusting?\n"
        f"2. Explain what **galvanising** is and why zinc still protects iron even if the zinc coating is scratched.\n"
        f"3. Name two other common rust-prevention methods."
    )
    sol = (
        f"**Step 1:** It creates a **physical barrier** that prevents oxygen and moisture from coming into direct contact with the iron metal [1 Mark: Barrier protection].\n\n"
        f"**Step 2:** Galvanising is coating iron with **zinc**; zinc is more reactive than iron, so even when scratched, the zinc oxidises preferentially (**sacrificial protection**), protecting the underlying iron from corroding [1 Mark: Galvanising / Sacrificial protection].\n\n"
        f"**Step 3:** Other methods: painting, oiling/greasing, electroplating with chromium/tin, or alloying into stainless steel [1 Mark: Other methods]."
    )
    return {
        "id": f"ns8_chem_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Barrier prevents water and oxygen contact; Zinc is more reactive and corrodes preferentially (sacrificial protection); Painting, oiling, stainless steel",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "42_rust_prevention_methods_painting_galvanising",
        "misconception_tags": ["rust_prevention_mechanisms"],
        "hints": {
            "tier_1": "Keep water and oxygen away from the iron.",
            "tier_2": "Zinc sacrifices itself to save the iron (galvanising).",
            "tier_3": "Barrier blocks air/water; zinc sacrificial protection; painting/greasing/stainless steel."
        }
    }


# ==============================================================================
# CLUSTER 6: Scientific Inquiry & Master Challenges (43 - 50)
# ==============================================================================

def arch_43_testing_reaction_products_gases_summary(rng: random.Random) -> Dict[str, Any]:
    tests = [
        ("Hydrogen ($H_2$)", "bring a burning wooden splint near the mouth of the tube", "burns with a distinctive 'pop' sound"),
        ("Oxygen ($O_2$)", "insert a glowing wooden splint into the tube", "the glowing splint relights (bursts into flame)"),
        ("Carbon dioxide ($CO_2$)", "bubble the gas through clear limewater", "the limewater turns milky / cloudy white"),
    ]
    gas, method, result = rng.choice(tests)

    prompt = (
        f"Identifying unknown gases released during chemical reactions is a fundamental laboratory competency.\n\n"
        f"Consider the identification of: **{gas}**.\n\n"
        f"1. Describe the exact experimental test used to identify {gas.split(' ')[0]} ({method}).\n"
        f"2. State the positive observation that confirms the presence of {gas.split(' ')[0]}.\n"
        f"3. State the test and positive result for one of the other two common laboratory gases."
    )
    sol = (
        f"**Step 1:** Test procedure: **{method}** [1 Mark: Test procedure].\n\n"
        f"**Step 2:** Positive observation: **{result}** [1 Mark: Positive result].\n\n"
        f"**Step 3:** Other gas test: Oxygen relights a glowing splint; Hydrogen burns with a 'pop'; Carbon dioxide turns clear limewater milky [1 Mark: Other gas test]."
    )
    return {
        "id": f"ns8_chem_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{method}; {result}; Another gas test (e.g. oxygen relights glowing splint, CO2 turns limewater milky)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "43_testing_reaction_products_gases_summary",
        "misconception_tags": ["gas_testing_competency"],
        "hints": {
            "tier_1": "Hydrogen pops, Oxygen relights, CO2 turns limewater milky.",
            "tier_2": f"For {gas}: {method} -> {result}.",
            "tier_3": f"{method}; {result}; other gas test."
        }
    }


def arch_44_investigating_temperature_change_exothermic_reaction(rng: random.Random) -> Dict[str, Any]:
    t_start = rng.choice([20, 21, 22])
    delta_t = rng.choice([15, 18, 22])
    t_end = t_start + delta_t

    prompt = (
        f"A student measures the temperature change during a chemical reaction between vinegar and steel wool (iron):\n"
        f"- Initial temperature of vinegar = **${t_start}^\\circ\\text{{C}}**\n"
        f"- Maximum temperature reached after 10 minutes = **${t_end}^\\circ\\text{{C}}**\n\n"
        f"1. Calculate the temperature change ($\\Delta T$) during this reaction.\n"
        f"2. Is this reaction **exothermic** or **endothermic**? Justify your answer using the temperature data.\n"
        f"3. Where did the thermal energy that warmed the beaker come from?"
    )
    sol = (
        f"**Step 1:** $\\Delta T = \\text{{Final temp}} - \\text{{Initial temp}} = {t_end} - {t_start} = \\mathbf{{{delta_t}^\\circ\\text{{C}}}}$ [1 Mark: Delta T calculation].\n\n"
        f"**Step 2:** The reaction is **exothermic** because the temperature of the solution and surroundings increased by ${delta_t}^\\circ\\text{{C}}$ [1 Mark: Exothermic justification].\n\n"
        f"**Step 3:** The thermal energy came from **chemical potential energy stored in the chemical bonds** of the reactants, which was released as new, more stable bonds formed in the products [1 Mark: Chemical potential energy source]."
    )
    return {
        "id": f"ns8_chem_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Delta T = {delta_t}°C; Exothermic because temperature increased; Released from chemical potential energy stored in bonds",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "44_investigating_temperature_change_exothermic_reaction",
        "misconception_tags": ["temperature_change_exothermic_experiment"],
        "hints": {
            "tier_1": f"Subtract temperatures: {t_end} - {t_start}.",
            "tier_2": "Temperature rose, so heat was released (exothermic).",
            "tier_3": f"{delta_t}°C; Exothermic; chemical potential energy in bonds."
        }
    }


def arch_45_investigating_rusting_factors_fair_test(rng: random.Random) -> Dict[str, Any]:
    rust_col = rng.choice(["#ea580c", "#c2410c", "#d97706"])
    nail_y = rng.choice([95, 100, 105])

    svg = (
        f'<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="340" height="180" rx="6" fill="#f8fafc"/>'
        f'<text x="180" y="28" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Rusting Experiment: 3 Conditions</text>'
        # Tube 1: Air + Water (Rusts)
        f'<rect x="35" y="45" width="60" height="110" rx="4" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>'
        f'<rect x="37" y="90" width="56" height="63" fill="#67e8f9" opacity="0.6"/>'
        f'<rect x="62" y="{nail_y - 30}" width="6" height="50" fill="{rust_col}"/>'
        f'<text x="65" y="170" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">Tube 1: RUST</text>'
        f'<text x="65" y="183" font-family="sans-serif" font-size="8" fill="#475569" text-anchor="middle">Air + Water</text>'
        # Tube 2: Dry air (Silica gel)
        f'<rect x="150" y="45" width="60" height="110" rx="4" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>'
        f'<rect x="152" y="130" width="56" height="23" fill="#cbd5e1"/>'
        f'<rect x="177" y="70" width="6" height="50" fill="#64748b"/>'
        f'<text x="180" y="170" font-family="sans-serif" font-size="10" font-weight="bold" fill="#16a34a" text-anchor="middle">Tube 2: NO RUST</text>'
        f'<text x="180" y="183" font-family="sans-serif" font-size="8" fill="#475569" text-anchor="middle">Dry air (Silica)</text>'
        # Tube 3: Boiled water + Oil seal
        f'<rect x="265" y="45" width="60" height="110" rx="4" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>'
        f'<rect x="267" y="65" width="56" height="88" fill="#67e8f9" opacity="0.6"/>'
        f'<rect x="267" y="65" width="56" height="15" fill="#fef08a"/>'
        f'<rect x="292" y="90" width="6" height="50" fill="#64748b"/>'
        f'<text x="295" y="170" font-family="sans-serif" font-size="10" font-weight="bold" fill="#16a34a" text-anchor="middle">Tube 3: NO RUST</text>'
        f'<text x="295" y="183" font-family="sans-serif" font-size="8" fill="#475569" text-anchor="middle">Boiled water + Oil</text>'
        f'</svg>'
    )

    prompt = (
        f"A classic fair-test investigation into iron rusting uses three test tubes:\n"
        f"- **Tube 1:** Iron nail exposed to both air and tap water.\n"
        f"- **Tube 2:** Iron nail in dry air with silica gel drying beads and a rubber stopper.\n"
        f"- **Tube 3:** Iron nail in boiled water covered with an oil layer.\n\n"
        f"1. In which test tube(s) will the iron nail rust after 5 days?\n"
        f"2. Why does the nail in Tube 2 NOT rust?\n"
        f"3. Why was the water in Tube 3 boiled before adding oil, and why does that nail NOT rust?"
    )
    sol = (
        f"**Step 1:** The nail will **only rust in Tube 1** [1 Mark: Tube 1 rusts].\n\n"
        f"**Step 2:** Tube 2 contains **no water/moisture** (the silica gel absorbs all water vapor); iron cannot rust without moisture [1 Mark: Tube 2 explanation].\n\n"
        f"**Step 3:** Boiling the water **removes all dissolved oxygen gas**, and the oil layer **blocks oxygen from the air from dissolving back in**; iron cannot rust without oxygen [1 Mark: Tube 3 explanation]."
    )
    return {
        "id": f"ns8_chem_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Only Tube 1 rusts; Tube 2 lacks water/moisture; Boiling removes dissolved oxygen and oil blocks air",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "45_investigating_rusting_factors_fair_test",
        "misconception_tags": ["rusting_experiment_fair_test"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Iron needs BOTH water and oxygen. Tube 2 lacks water; Tube 3 lacks oxygen.",
            "tier_2": "Only Tube 1 has both water and oxygen.",
            "tier_3": "Only Tube 1 rusts; Tube 2 has no water; Tube 3 has no oxygen (boiled + oil seal)."
        }
    }


def arch_46_evaluating_chemical_reaction_rate_factors(rng: random.Random) -> Dict[str, Any]:
    factors = [
        ("Temperature", "Warm vinegar reacts much faster with baking soda than ice-cold vinegar", "particles move faster with higher kinetic energy, colliding more frequently and energetically"),
        ("Surface area / Particle size", "Powdered calcium carbonate reacts much faster with acid than a solid marble chunk of the same mass", "powder exposes vastly more surface atoms to collide with acid particles simultaneously"),
        ("Concentration", "Concentrated hydrochloric acid reacts more vigorously with zinc than dilute acid", "higher concentration means more reactant particles per unit volume, increasing collision frequency"),
    ]
    f_name, scenario, explanation = rng.choice(factors)

    prompt = (
        f"The speed (rate) of a chemical reaction is influenced by several physical factors.\n\n"
        f"Consider: **{scenario}**.\n\n"
        f"1. Which factor affecting reaction rates is being demonstrated ({f_name})?\n"
        f"2. Explain why this factor increases the reaction speed using the particle model of matter ({explanation}).\n"
        f"3. Name two other factors that can increase the rate of a chemical reaction."
    )
    sol = (
        f"**Step 1:** The factor is **{f_name}** [1 Mark: Factor identification].\n\n"
        f"**Step 2:** {explanation.capitalize()} [1 Mark: Particle model explanation].\n\n"
        f"**Step 3:** Other factors: Temperature, Surface area (particle size), Concentration, or Adding a catalyst [1 Mark: Other factors]."
    )
    return {
        "id": f"ns8_chem_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{f_name}; {explanation}; Temperature, surface area, concentration, catalyst",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "46_evaluating_chemical_reaction_rate_factors",
        "misconception_tags": ["factors_affecting_reaction_rate"],
        "hints": {
            "tier_1": f"Think about {f_name.lower()} and collision rate.",
            "tier_2": "More collisions = faster reaction.",
            "tier_3": f"{f_name}; {explanation}; temperature, surface area, concentration, catalyst."
        }
    }


def arch_47_chemical_reactions_in_daily_cleaning_and_safety(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Household cleaning chemicals must be handled with extreme care to avoid accidental dangerous chemical reactions.\n\n"
        f"A prominent safety label on household bleach (sodium hypochlorite) warns: **'NEVER MIX WITH AMMONIA OR ACIDIC TOILET CLEANERS'**.\n\n"
        f"1. Why is it extremely hazardous to mix bleach with an acid (like hydrochloric acid or toilet cleaner)? Name the toxic gas formed.\n"
        f"2. Why is it hazardous to mix bleach with ammonia-based cleaners? Name the toxic fumes produced.\n"
        f"3. State two essential laboratory or domestic safety precautions when working with reactive cleaning chemicals."
    )
    sol = (
        f"**Step 1:** Mixing bleach with acid causes an immediate chemical reaction releasing **toxic, choking chlorine gas ($Cl_2$)**, which can burn the lungs and cause suffocation [1 Mark: Chlorine gas danger].\n\n"
        f"**Step 2:** Mixing bleach with ammonia produces **deadly chloramine vapours ($NH_2Cl$)**, which cause severe respiratory damage and eye irritation [1 Mark: Chloramine fumes].\n\n"
        f"**Step 3:** Safety precautions (any two): (1) Work in a well-ventilated area or outdoors; (2) Wear safety goggles and rubber gloves; (3) Never mix different commercial cleaning products together; (4) Rinse thoroughly with plenty of water [1 Mark: Safety precautions]."
    )
    return {
        "id": f"ns8_chem_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Releases toxic chlorine gas (Cl2); Releases toxic chloramine vapours; Work in well-ventilated area, wear gloves/goggles, never mix cleaners",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "47_chemical_reactions_in_daily_cleaning_and_safety",
        "misconception_tags": ["chemical_cleaning_safety"],
        "hints": {
            "tier_1": "Mixing bleach with acid produces deadly chlorine gas.",
            "tier_2": "Mixing bleach with ammonia produces toxic chloramine.",
            "tier_3": "Toxic chlorine gas; toxic chloramine vapors; good ventilation and gloves/goggles."
        }
    }


def arch_48_misconceptions_mass_destroyed_when_ash_forms(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner burns a $1\\text{{ kg}}$ log of dry firewood in a fireplace. When the fire burns out, only $50\\text{{ g}}$ of grey ash remains.\n\n"
        f"The learner concludes: *'This proves that $950\\text{{ g}}$ of matter was destroyed and converted into pure nothingness, proving mass is not conserved in fire.'*\n\n"
        f"1. Is the learner's conclusion correct? (Yes or No)\n"
        f"2. Explain what actually happened to the missing $950\\text{{ g}}$ of matter.\n"
        f"3. How could this combustion reaction be conducted to scientifically prove that the total mass of reactants exactly equals the total mass of products?"
    )
    sol = (
        f"**Step 1:** **No**, the learner's conclusion is completely false [1 Mark: Evaluation].\n\n"
        f"**Step 2:** The wood reacted with oxygen to produce **invisible carbon dioxide gas ($CO_2$) and water vapor ($H_2O$)**, which escaped up the chimney into the atmosphere; the missing $950\\text{{ g}}$ is in the gas phase in the air [1 Mark: Gas escape explanation].\n\n"
        f"**Step 3:** Conduct the experiment in a **closed system** (a large, sealed chamber with enough oxygen); weighing the chamber before and after burning will show that total mass is **strictly conserved** [1 Mark: Closed system proof]."
    )
    return {
        "id": f"ns8_chem_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "No; Missing mass escaped as invisible gases (CO2 and water vapor) up the chimney; Conduct in a sealed closed chamber to prove mass is conserved",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "48_misconceptions_mass_destroyed_when_ash_forms",
        "misconception_tags": ["ash_mass_loss_misconception"],
        "hints": {
            "tier_1": "Matter is never destroyed. Smoke and steam went up the chimney.",
            "tier_2": "Capture all the smoke and gases in a sealed box to prove mass is saved.",
            "tier_3": "No; escaped as CO2 and water vapor into air; test in sealed closed system."
        }
    }


def arch_49_scientific_inquiry_identifying_mystery_reaction(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "Mystery Reaction 1",
            "A silvery metal ribbon is placed in clear hydrochloric acid",
            "Vigorous fizzing occurs; a gas is collected that explodes with a 'pop' when tested with a burning splint; beaker gets hot",
            "Metal + Acid reaction producing Hydrogen gas and heat",
            "Exothermic synthesis / displacement"
        ),
        (
            "Mystery Reaction 2",
            "A green solid powder is heated in a dry test tube",
            "The powder turns black; a gas is released that turns clear limewater milky; no flame observed",
            "Thermal decomposition of metal carbonate producing Carbon dioxide gas",
            "Endothermic decomposition"
        ),
        (
            "Mystery Reaction 3",
            "A piece of shiny iron wire is left in moist salty air for a week",
            "The wire turns flaky reddish-brown and gains mass; no gas released",
            "Rusting / Corrosion (Iron + Oxygen + Water -> Hydrated iron oxide)",
            "Exothermic slow oxidation / synthesis"
        ),
    ]
    name, setup, obs, nature, cat = rng.choice(scenarios)

    prompt = (
        f"A laboratory researcher conducts investigations on **{name}**:\n"
        f"- **Experimental Setup:** {setup}\n"
        f"- **Observations:** {obs}\n\n"
        f"1. Identify the chemical reaction occurring ({nature.split(' (')[0]}).\n"
        f"2. Name any gas product formed and state the observation that proves its identity.\n"
        f"3. Classify the reaction as either **exothermic** or **endothermic** ({cat.split(' ')[0]})."
    )
    gas_info = "Hydrogen gas (burning splint pop)" if "pop" in obs else ("Carbon dioxide gas (limewater milky)" if "limewater" in obs else "No gas released (atmospheric oxygen absorbed)")

    sol = (
        f"**Step 1:** Reaction: **{nature}** [1 Mark: Reaction identification].\n\n"
        f"**Step 2:** Gas identification: **{gas_info}** [1 Mark: Gas identification].\n\n"
        f"**Step 3:** Classification: **{cat}** [1 Mark: Energy classification]."
    )
    return {
        "id": f"ns8_chem_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{nature}; {gas_info}; {cat.split(' ')[0]}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "49_scientific_inquiry_identifying_mystery_reaction",
        "misconception_tags": ["mystery_reaction_inquiry"],
        "hints": {
            "tier_1": f"Look at the gas test: {obs.split(';')[1] if ';' in obs else obs}.",
            "tier_2": f"Reaction is {nature}.",
            "tier_3": f"{nature}; {gas_info}; {cat.split(' ')[0]}."
        }
    }


def arch_50_chemical_reactions_master_synthesis_challenge(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Complete the comprehensive Grade 8 Chemical Reactions master synthesis challenge:\n\n"
        "1. **Physical vs Chemical:** Classify (a) boiling water into steam and (b) rusting of an iron gate as physical or chemical changes.\n"
        "2. **Balancing Equation:** Balance the combustion equation: $\\text{CH}_4 + \\text{O}_2 \\rightarrow \\text{CO}_2 + \\text{H}_2\\text{O}$.\n"
        "3. **Conservation of Mass:** If $16\\text{ g}$ of methane ($CH_4$) reacts completely with $64\\text{ g}$ of oxygen ($O_2$), and produces $44\\text{ g}$ of carbon dioxide ($CO_2$), calculate the mass of water ($H_2O$) produced in a closed system.\n"
        "4. **Indigenous Application:** Name the biochemical reaction used to brew traditional African beer (*umqombothi*), stating the gas released."
    )
    water_mass = (16 + 64) - 44

    sol = (
        f"**Step 1:** (a) Boiling water is a **physical change**; (b) Rusting iron is a **chemical change** [1 Mark: Physical vs Chemical].\n\n"
        f"**Step 2:** Balanced equation: $$\\mathbf{{\\text{{CH}}_4 + 2\\text{{O}}_2 \\rightarrow \\text{{CO}}_2 + 2\\text{{H}}_2\\text{{O}}}}$$ [1 Mark: Balanced equation].\n\n"
        f"**Step 3:** By Conservation of Mass: Total reactants mass = $16 + 64 = 80\\text{{ g}}$. Therefore, Total products mass must = $80\\text{{ g}}$. Mass of water = $80 - 44 = \\mathbf{{{water_mass}\\text{{ g}}}}$ [1 Mark: Conservation calculation].\n\n"
        f"**Step 4:** The reaction is **fermentation**, which releases **carbon dioxide gas ($CO_2$)** [1 Mark: Fermentation & CO2]."
    )
    return {
        "id": f"ns8_chem_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Boiling is physical, rusting is chemical; CH4 + 2O2 -> CO2 + 2H2O; Water mass = {water_mass} g; Fermentation releases carbon dioxide",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "term": 2,
        "subskill": "50_chemical_reactions_master_synthesis_challenge",
        "misconception_tags": ["chemical_reactions_master_synthesis"],
        "hints": {
            "tier_1": "Boiling = physical, rusting = chemical. Total mass in = total mass out.",
            "tier_2": f"80 g in total. 80 - 44 = {water_mass} g water. Brewing uses fermentation.",
            "tier_3": f"Boiling=physical, rusting=chemical; CH4 + 2O2 -> CO2 + 2H2O; {water_mass} g; Fermentation (CO2)."
        }
    }
