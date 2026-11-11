"""Natural Sciences Grade 8 Term 2: Chemical Reactions Generator.

Strictly grounded in curriculum_docs_auto/NaturalSciences_Gr8/Syllabus.md.
Covers:
- reactants_products_and_chemical_change: Chemical change vs physical change; properties of products differ from reactants.
- atomic_rearrangement_bond_breaking: Conservation of mass/atoms; bond breaking and bond forming during reactions.
- word_equations_representation: Standard word equations for synthesis and oxidation reactions (Mg + O2, Fe + S).
- fermentation_indigenous_knowledge: Traditional African fermentation (umqombothi, sorghum beer) producing CO2 and ethanol.
- carbon_dioxide_limewater_precipitation: Calcium carbonate formation and acid-carbonate reactions (vinegar + eggshell).

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


SUBSKILLS = [
    "reactants_products_and_chemical_change",
    "atomic_rearrangement_bond_breaking",
    "word_equations_representation",
    "fermentation_indigenous_knowledge",
    "carbon_dioxide_limewater_precipitation",
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _build_reactants_products(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    reactions = [
        {
            "name": "Combustion of Magnesium ribbon in oxygen",
            "equation": "Magnesium + Oxygen -> Magnesium oxide",
            "reactants": "Magnesium (shiny grey metal) and Oxygen gas",
            "product": "Magnesium oxide (white powdery solid ash)",
            "evidence": "Blinding white light emission and dramatic change in physical texture to white powder",
            "target": "Magnesium and Oxygen"
        },
        {
            "name": "Heating Iron filings with Sulfur powder",
            "equation": "Iron + Sulfur -> Iron sulfide",
            "reactants": "Iron filings (magnetic grey) and Sulfur (yellow powder)",
            "product": "Iron sulfide (black, non-magnetic crystalline solid)",
            "evidence": "Glowing red heat glow and loss of magnetic properties in the product",
            "target": "Iron and Sulfur"
        },
        {
            "name": "Reaction of Zinc with Hydrochloric acid",
            "equation": "Zinc + Hydrochloric acid -> Zinc chloride + Hydrogen gas",
            "reactants": "Zinc metal and Hydrochloric acid solution",
            "product": "Zinc chloride salt and Hydrogen gas bubbles",
            "evidence": "Rapid effervescence (bubbling) and temperature increase",
            "target": "Zinc and Hydrochloric acid"
        }
    ]
    r = rng.choice(reactions)
    prompt = (
        f"In a science laboratory, a teacher demonstrates the following reaction:\n"
        f"$$\\text{{{r['equation']}}}$$\n\n"
        f"1. Identify the **reactants** in this chemical reaction.\n"
        f"2. Identify the **product(s)**.\n"
        f"3. State one observable piece of evidence that proves a chemical reaction took place rather than a simple physical mixture."
    )
    sample_answer = (
        f"1. Reactants: {r['reactants']}.\n"
        f"2. Product: {r['product']}.\n"
        f"3. Observable evidence: {r['evidence']}."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        f"1. Reactants: Correctly identifies starting substances ({r['reactants']}) [1 mark].\n"
        f"2. Products: Correctly identifies new substance formed ({r['product']}) [1 mark].\n"
        f"3. Evidence: Cites valid indicators of chemical change (new physical properties, light/heat energy release, gas effervescence) [1 mark]."
    )
    return {
        "id": _make_id("ns8_chem_react", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "reactants_products_and_chemical_change",
        "question_family_id": "reactants_products_and_chemical_change",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Chemical Reactions > Reactants and products",
        "hints": {
            "tier_1": "Reactants are the starting substances on the left; products are the new substances on the right.",
            "tier_2": "Look for color change, heat/light emission, or gas bubbles.",
            "tier_3": f"Reactants: {r['target']}."
        },
        "misconception_tags": ["confuses_reactants_with_products"]
    }


def _build_atomic_rearrangement(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    scenarios = [
        ("methane gas and oxygen gas to produce carbon dioxide and water vapor", "\\text{CH}_4 + 2\\text{O}_2 \\rightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O}"),
        ("hydrogen gas and chlorine gas reacting to form hydrogen chloride gas", "\\text{H}_2 + \\text{Cl}_2 \\rightarrow 2\\text{HCl}"),
        ("solid carbon reacting with excess oxygen gas to produce carbon dioxide", "\\text{C} + \\text{O}_2 \\rightarrow \\text{CO}_2")
    ]
    name, eq = rng.choice(scenarios)
    prompt = (
        f"During a chemical reaction between {name}:\n\n"
        f"$${eq}$$\n\n"
        f"According to the Law of Conservation of Mass and atomic theory:\n"
        f"1. What happens to the existing chemical bonds between atoms in the reactant molecules?\n"
        f"2. Are any new chemical atoms created, or are any existing atoms destroyed, during this reaction?\n"
        f"3. Explain why the total mass of the products must exactly equal the total mass of the reactants in a closed container."
    )
    sample_answer = (
        "1. Existing chemical bonds in the reactant molecules absorb energy and break apart.\n"
        "2. No atoms are created and no atoms are destroyed; the existing atoms simply rearrange into new combinations with new chemical bonds.\n"
        "3. Because all atoms from the reactants are conserved and present in the products, the total number and type of atoms remain identical, meaning the total mass is strictly conserved."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        "1. Bond dynamics: Bonds break in reactants and new bonds form in products [1 mark].\n"
        "2. Atom conservation: No atoms created or destroyed; atoms are rearranged [1 mark].\n"
        "3. Conservation of mass: Same number and type of atoms on both sides means mass of reactants equals mass of products [1 mark]."
    )
    return {
        "id": _make_id("ns8_atom_rearr", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "atomic_rearrangement_bond_breaking",
        "question_family_id": "atomic_rearrangement_bond_breaking",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Chemical Reactions > Atomic rearrangement and conservation of mass",
        "hints": {
            "tier_1": "Think about whether atoms can appear out of nowhere or disappear.",
            "tier_2": "Chemical reactions rearrange atoms; they never destroy or create them.",
            "tier_3": "Mass is conserved because the exact same atoms are present before and after."
        },
        "misconception_tags": ["atoms_destroyed_in_reaction_misconception"]
    }


def _build_word_equations(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    equations = [
        {
            "desc": "Burning solid carbon (charcoal) in oxygen gas to form carbon dioxide gas",
            "correct": "Carbon + Oxygen -> Carbon dioxide",
            "distractors": [
                "Carbon dioxide -> Carbon + Oxygen",
                "Carbon + Hydrogen -> Carbon hydride",
                "Carbon + Nitrogen -> Cyanide gas"
            ]
        },
        {
            "desc": "Rusting of iron metal in the presence of oxygen and moisture to form iron oxide",
            "correct": "Iron + Oxygen -> Iron oxide",
            "distractors": [
                "Iron oxide -> Iron + Oxygen",
                "Iron + Carbon dioxide -> Iron carbonate",
                "Iron + Hydrogen -> Iron hydride"
            ]
        },
        {
            "desc": "Synthesis of water from hydrogen gas burning in oxygen gas",
            "correct": "Hydrogen + Oxygen -> Water",
            "distractors": [
                "Water -> Hydrogen + Oxygen",
                "Hydrogen + Carbon -> Hydrocarbon",
                "Hydrogen + Nitrogen -> Ammonia"
            ]
        }
    ]
    eq = rng.choice(equations)
    prompt = (
        f"Represent the following chemical change as a standard chemical word equation:\n\n"
        f"\"{eq['desc']}\""
    )
    options = [eq["correct"]] + eq["distractors"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify reactants (starting substances):\n"
        f"The description states the reactants combine together.\n\n"
        f"Step 2: Identify product:\n"
        f"The product formed is written on the right side of the arrow.\n\n"
        f"Step 3: Correct word equation:\n"
        f"$$\\text{{{eq['correct']}}}$$"
    )
    return {
        "id": _make_id("ns8_word_eq", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": eq["correct"],
        "sample_answer": eq["correct"],
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "word_equations_representation",
        "question_family_id": "word_equations_representation",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Chemical Reactions > Writing word equations",
        "hints": {
            "tier_1": "Reactants on the left, an arrow pointing right, and products on the right.",
            "tier_2": "The arrow indicates 'reacts to form' or 'produces'.",
            "tier_3": f"The correct equation is {eq['correct']}."
        },
        "misconception_tags": ["reversed_equation_arrow_misconception"]
    }


def _build_fermentation_ik(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    ik_cases = [
        "In South African indigenous knowledge systems, traditional brewing of sorghum beer (umqombothi) has been practiced for centuries using sprouted sorghum malt, maize meal, and natural yeast.",
        "Traditional South African culinary heritage utilizes fermented ginger beer (gemmer) crafted from sugar, fresh ginger root, cream of tartar, and active baker's yeast.",
        "In traditional baking heritage across Southern African households, fermented steam bread (dombolo) relies on live yeast cultures to aerate dough through anaerobic metabolism."
    ]
    chosen_ik = rng.choice(ik_cases)
    prompt = (
        f"{chosen_ik}\n\n"
        f"1. Identify the biochemical reaction responsible for this process.\n"
        f"2. Name the biological organism (micro-organism) that drives this reaction.\n"
        f"3. Name the two chemical products produced when yeast breaks down plant sugars anaerobically."
    )
    sample_answer = (
        "1. Alcoholic fermentation (anaerobic respiration).\n"
        "2. Yeast (Saccharomyces cerevisiae).\n"
        "3. Ethanol (alcohol) and carbon dioxide gas (CO2)."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        "1. Reaction type: Alcoholic fermentation / anaerobic respiration [1 mark].\n"
        "2. Organism: Yeast [1 mark].\n"
        "3. Products: Ethanol and carbon dioxide gas [1 mark]."
    )
    return {
        "id": _make_id("ns8_ferment_ik", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "fermentation_indigenous_knowledge",
        "question_family_id": "fermentation_indigenous_knowledge",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Chemical Reactions > Indigenous knowledge and fermentation",
        "hints": {
            "tier_1": "Think of the process that turns sugar into alcohol without oxygen.",
            "tier_2": "Yeast carries out fermentation, making bubbles of gas and alcohol.",
            "tier_3": "Fermentation produces ethanol and carbon dioxide gas."
        },
        "misconception_tags": ["fermentation_requires_oxygen_misconception"]
    }


def _build_co2_limewater_precipitation(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    reactions = [
        "A learner places crushed eggshells (composed primarily of calcium carbonate, CaCO3) into a beaker of household white vinegar (acetic acid).",
        "A science student adds marble chips (calcium carbonate, CaCO3) to dilute hydrochloric acid in a side-arm test tube.",
        "A learner drops a piece of natural chalk (calcium carbonate, CaCO3) into a test tube containing dilute nitric acid."
    ]
    chosen_rxn = rng.choice(reactions)
    prompt = (
        f"{chosen_rxn} Effervescence occurs immediately, and the gas produced is bubbled through a delivery tube into clear limewater.\n\n"
        f"1. What observable gas test confirms the identity of the gas as carbon dioxide?\n"
        f"2. Write the word equation for the reaction of calcium carbonate with acid.\n"
        f"3. Name the chemical compound responsible for turning the clear limewater milky white."
    )
    sample_answer = (
        "1. The clear limewater turns milky / cloudy white when carbon dioxide is bubbled through it.\n"
        "2. Calcium carbonate + Acid -> Calcium salt + Carbon dioxide + Water\n"
        "3. Calcium carbonate precipitate (CaCO3)."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        "1. Observation: Clear limewater turns milky / cloudy white [1 mark].\n"
        "2. Word equation: Calcium carbonate + Acid -> Salt + Carbon dioxide + Water [1 mark].\n"
        "3. Precipitate: Insoluble calcium carbonate (CaCO3) formed from calcium hydroxide and CO2 [1 mark]."
    )
    return {
        "id": _make_id("ns8_co2_precip", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "carbon_dioxide_limewater_precipitation",
        "question_family_id": "carbon_dioxide_limewater_precipitation",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Chemical Reactions > Carbon dioxide limewater reaction",
        "hints": {
            "tier_1": "Eggshells are carbonate; carbonate + acid always produces carbon dioxide gas.",
            "tier_2": "Limewater is calcium hydroxide; with CO2 it forms white calcium carbonate.",
            "tier_3": "Limewater turns milky white due to calcium carbonate precipitate."
        },
        "misconception_tags": ["acid_carbonate_produces_hydrogen_misconception"]
    }


def generate(archetype: Optional[str] = None, seed: Optional[int] = None, count: int = 1, **kwargs) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    results = []
    for idx in range(count):
        target = archetype or rng.choice(SUBSKILLS)
        if target == "reactants_products_and_chemical_change":
            item = _build_reactants_products(rng, seed, idx)
        elif target == "atomic_rearrangement_bond_breaking":
            item = _build_atomic_rearrangement(rng, seed, idx)
        elif target == "word_equations_representation":
            item = _build_word_equations(rng, seed, idx)
        elif target == "fermentation_indigenous_knowledge":
            item = _build_fermentation_ik(rng, seed, idx)
        elif target == "carbon_dioxide_limewater_precipitation":
            item = _build_co2_limewater_precipitation(rng, seed, idx)
        else:
            item = _build_reactants_products(rng, seed, idx)
        results.append(item)
    return results


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)
