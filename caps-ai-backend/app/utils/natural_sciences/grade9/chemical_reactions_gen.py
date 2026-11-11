"""Natural Sciences Grade 9 Term 2: Chemical Reactions Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 2/01. Chemical reactions.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. law_of_conservation_of_atoms: Atom counting on reactant vs product sides and mass conservation.
2. balancing_synthesis_reactions: Balancing fundamental synthesis equations (H2+O2, C+O2, Mg+O2, Fe+O2).
3. subscripts_vs_coefficients: Differentiating molecular subscripts from stoichiometric coefficients.
4. macroscopic_reaction_evidence: Identifying observable signs of chemical change vs physical change.
5. particle_reaction_modeling: Submicroscopic bond rearrangement modeling (reactants -> products).
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences.natural_sciences_builders import (
    build_chemical_bonding_ns_question,
)

TOPIC_NAME = "Chemical reactions"
ORDERED_SUBSKILLS = [
    "law_of_conservation_of_atoms",
    "balancing_synthesis_reactions",
    "subscripts_vs_coefficients",
    "macroscopic_reaction_evidence",
    "particle_reaction_modeling",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_rxn"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any]) -> Dict[str, Any]:
    if "title" not in res:
        res["title"] = "Particle Reaction Modeling & Chemical Bonding"
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
    elif subskill in ("bonding", "chemical_bonding", "molecules"):
        return _normalize_res(build_chemical_bonding_ns_question(actual_seed, grade=9, mode=mode))
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: Law of Conservation of Atoms
    if chosen_subskill == "law_of_conservation_of_atoms":
        reactions = [
            (
                "Combustion of Hydrogen gas in Oxygen",
                "2H₂ + O₂ → 2H₂O",
                "Reactants: 4 Hydrogen atoms (2 × 2) and 2 Oxygen atoms (1 × 2). Products: 4 Hydrogen atoms (2 × 2) and 2 Oxygen atoms (2 × 1). Total: 6 atoms on both sides.",
                "4 Hydrogen and 2 Oxygen",
                "4 Hydrogen and 2 Oxygen",
            ),
            (
                "Combustion of Magnesium ribbon in Oxygen",
                "2Mg + O₂ → 2MgO",
                "Reactants: 2 Magnesium atoms and 2 Oxygen atoms. Products: 2 Magnesium atoms and 2 Oxygen atoms. Total: 4 atoms on both sides.",
                "2 Magnesium and 2 Oxygen",
                "2 Magnesium and 2 Oxygen",
            ),
            (
                "Combustion of Carbon in Oxygen",
                "C + O₂ → CO₂",
                "Reactants: 1 Carbon atom and 2 Oxygen atoms. Products: 1 Carbon atom and 2 Oxygen atoms. Total: 3 atoms on both sides.",
                "1 Carbon and 2 Oxygen",
                "1 Carbon and 2 Oxygen",
            ),
            (
                "Oxidation of Iron forming Rust",
                "4Fe + 3O₂ → 2Fe₂O₃",
                "Reactants: 4 Iron atoms and 6 Oxygen atoms (3 × 2). Products: 4 Iron atoms (2 × 2) and 6 Oxygen atoms (2 × 3). Total: 10 atoms on both sides.",
                "4 Iron and 6 Oxygen",
                "4 Iron and 6 Oxygen",
            ),
        ]
        rx = reactions[actual_seed % len(reactions)]
        question_text = (
            f"The Law of Conservation of Matter states that matter cannot be created or destroyed in a chemical reaction.\n\n"
            f"Consider the balanced chemical equation for the **{rx[0]}**:\n"
            f"$$\\text{{{rx[1]}}}$$\n\n"
            "1. Count and state the total number of atoms of each element on the **reactants side**.\n"
            "2. Count and state the total number of atoms of each element on the **products side**.\n"
            "3. State what happens to the individual atoms during this chemical reaction.\n"
            "4. If 48 g of magnesium reacts completely with 32 g of oxygen, calculate the mass of magnesium oxide formed."
        )
        sample = (
            f"1. **Reactants Atoms:** {rx[3]};\n"
            f"2. **Products Atoms:** {rx[4]};\n"
            "3. **Atomic Rearrangement:** Chemical bonds between reactant atoms are broken and atoms are rearranged to form new chemical bonds in the products. No atoms are created, destroyed, or lost;\n"
            "4. **Total Mass Calculation:**\n"
            "   $$\\text{Total Mass of Products} = \\text{Total Mass of Reactants} = 48\\text{ g} + 32\\text{ g} = 80\\text{ g}$$"
        )
        marking = (
            f"• 1 mark: Reactant atoms accurately counted ({rx[3]}) [1]\n"
            f"• 1 mark: Product atoms accurately counted ({rx[4]}) [1]\n"
            "• 1 mark: Atoms are rearranged / bonds broken and remade / conservation stated [1]\n"
            "• 1 mark: Mass calculation: 48 g + 32 g = 80 g [1]\n"
            "**Total: 4 marks**"
        )
        return {
            "title": f"Conservation of Atoms: {rx[0]}",
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
                "Multiply stoichiometric coefficients by the chemical formula subscripts to count atoms.",
                "The Law of Conservation of Matter means mass of reactants equals mass of products.",
                f"Reactants: {rx[3]}. Products: {rx[4]}. Atoms are rearranged. 48 g + 32 g = 80 g.",
            ],
            "misconception_tags": ["atoms_destroyed_during_reaction_myth", "subscript_coefficient_multiplication_error"],
            "learning_objective_id": "NS9.MM.07.01",
        }

    # Subskill 2: Balancing Synthesis Reactions
    if chosen_subskill == "balancing_synthesis_reactions":
        unbalanced_eqs = [
            (
                "Combustion of Magnesium",
                "Mg + O₂ → MgO",
                "2Mg + O₂ → 2MgO",
                "Reactants have 2 Oxygen atoms but product has only 1. Place coefficient 2 in front of MgO, then place coefficient 2 in front of Mg.",
                "2, 1, 2",
            ),
            (
                "Synthesis of Water",
                "H₂ + O₂ → H₂O",
                "2H₂ + O₂ → 2H₂O",
                "Reactants have 2 Oxygen atoms; placing coefficient 2 in front of H₂O gives 2 Oxygen atoms and 4 Hydrogen atoms. Place coefficient 2 in front of H₂.",
                "2, 1, 2",
            ),
            (
                "Combustion of Iron",
                "Fe + O₂ → Fe₂O₃",
                "4Fe + 3O₂ → 2Fe₂O₃",
                "Oxygen has 2 atoms on left and 3 on right; find lowest common multiple of 6 (place 3 before O₂ and 2 before Fe₂O₃). This gives 4 Iron atoms on right, so place 4 before Fe.",
                "4, 3, 2",
            ),
            (
                "Oxidation of Copper",
                "Cu + O₂ → CuO",
                "2Cu + O₂ → 2CuO",
                "Reactants have 2 Oxygen atoms; placing coefficient 2 before CuO balances oxygen, then place 2 before Cu to balance copper.",
                "2, 1, 2",
            ),
        ]
        ueq = unbalanced_eqs[actual_seed % len(unbalanced_eqs)]
        question_text = (
            "Chemical equations must be balanced so that the number of atoms of each element is equal on both sides.\n\n"
            f"Consider the unbalanced chemical equation for the **{ueq[0]}**:\n"
            f"$$\\text{{{ueq[1]}}}$$\n\n"
            "1. Write the **fully balanced chemical equation** using the smallest whole-number coefficients.\n"
            "2. State the **stoichiometric ratio** of coefficients (left to right).\n"
            "3. Explain step-by-step why the equation is not balanced in its original form."
        )
        sample = (
            f"1. **Balanced Chemical Equation:**\n"
            f"   $$\\text{{{ueq[2]}}}$$\n"
            f"2. **Coefficients Ratio:** {ueq[4]};\n"
            f"3. **Balancing Step Explanation:** {ueq[3]}"
        )
        marking = (
            f"• 2 marks: Correct balanced equation ({ueq[2]}) with proper coefficients [2]\n"
            f"• 1 mark: Ratio of coefficients ({ueq[4]}) [1]\n"
            f"• 1 mark: Stepwise explanation of balancing ({ueq[3]}) [1]\n"
            "**Total: 4 marks**"
        )
        return {
            "title": f"Balancing Equations: {ueq[0]}",
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
                "You can only change the big numbers in front (coefficients). Never change the small subscript numbers inside formulas!",
                f"Count atoms on each side of {ueq[1]} and equalize them.",
                f"Balanced: {ueq[2]}. Ratio: {ueq[4]}. {ueq[3]}",
            ],
            "misconception_tags": ["altering_subscripts_to_balance_error", "unbalanced_chemical_equation_error"],
            "learning_objective_id": "NS9.MM.07.02",
        }

    # Subskill 3: Subscripts vs Coefficients
    if chosen_subskill == "subscripts_vs_coefficients":
        question_text = (
            "Chemical notation uses both subscript numbers and large coefficient numbers in front of formulas.\n\n"
            "1. Explain the fundamental difference between **subscripts** and **coefficients** in chemical notation.\n"
            "2. Distinguish clearly between the chemical meaning of **2H** and **H₂**.\n"
            "3. Distinguish clearly between the chemical meaning of **2H₂O** and **H₂O₂**.\n"
            "4. Why is it strictly forbidden to change formula subscripts when balancing a chemical equation?"
        )
        sample = (
            "1. **Subscripts vs Coefficients:**\n"
            "   • **Subscripts:** Small numbers written below the line indicating how many atoms of that element are chemically bonded together inside one molecule or formula unit;\n"
            "   • **Coefficients:** Large whole numbers placed in front of a formula indicating how many separate molecules or formula units take part in the reaction;\n"
            "2. **2H vs H₂:**\n"
            "   • **2H:** Represents two separate, unbonded individual hydrogen atoms;\n"
            "   • **H₂:** Represents one diatomic molecule of hydrogen consisting of two hydrogen atoms chemically bonded together;\n"
            "3. **2H₂O vs H₂O₂:**\n"
            "   • **2H₂O:** Represents two separate molecules of water (each containing 2 H and 1 O);\n"
            "   • **H₂O₂:** Represents one molecule of hydrogen peroxide (a completely different chemical compound containing 2 H and 2 O);\n"
            "4. Changing subscripts alters the chemical identity of the substance into an entirely different or non-existent chemical compound, violating chemical reality."
        )
        marking = (
            "• 2 marks: Accurate distinction between subscripts (atoms inside molecule) [1] and coefficients (number of molecules) [1]\n"
            "• 1 mark: 2H (2 separate atoms) vs H2 (1 bonded diatomic molecule) [1]\n"
            "• 1 mark: 2H2O (2 water molecules) vs H2O2 (1 hydrogen peroxide molecule) [1]\n"
            "• 1 mark: Subscript change alters chemical identity of the substance [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Subscripts vs Coefficients in Chemical Notation",
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
                "Subscripts are small numbers inside formulas. Coefficients are the big numbers in front.",
                "Changing a subscript changes what the substance is (e.g. H2O is water, H2O2 is toxic hydrogen peroxide).",
                "Subscripts show atoms bonded in a molecule. Coefficients show number of molecules. Changing subscripts changes the compound.",
            ],
            "misconception_tags": ["subscript_coefficient_conflation", "formula_altering_misconception"],
            "learning_objective_id": "NS9.MM.07.03",
        }

    # Subskill 4: Macroscopic Evidence of Reactions
    if chosen_subskill == "macroscopic_reaction_evidence":
        scenarios = [
            (
                "Adding dilute hydrochloric acid to sodium carbonate chalk powder, resulting in vigorous bubbling and gas release",
                "Chemical change (effervescence / gas production)",
                "Carbon dioxide gas is produced from the chemical rearrangement of atoms; this gas was not present before",
                "Gas evolution / effervescence",
            ),
            (
                "Melting solid ice cubes into liquid water in a glass beaker on a warm day",
                "Physical change (phase change)",
                "No new chemical substance is formed; water molecules (H₂O) merely gain kinetic energy and change state",
                "State change (melting) with zero chemical bond cleavage",
            ),
            (
                "Burning steel wool in a Bunsen burner flame, producing glowing sparks and leaving behind a brittle reddish-brown solid",
                "Chemical change (combustion / oxidation)",
                "Iron chemically combines with atmospheric oxygen to form a new compound, iron oxide",
                "Color change, heat/light release, and formation of a new chemical compound",
            ),
            (
                "Mixing clear solutions of silver nitrate and sodium chloride, forming an immediate cloudy white solid precipitate",
                "Chemical change (precipitation reaction)",
                "Insoluble silver chloride solid particles form and precipitate out of solution",
                "Precipitate formation",
            ),
        ]
        scen = scenarios[actual_seed % len(scenarios)]
        question_text = (
            f"Scientists differentiate between physical changes and chemical changes based on macroscopic observations.\n\n"
            f"Consider the scenario: **{scen[0]}**.\n"
            "1. Classify this event as a **chemical change** or a **physical change**.\n"
            "2. State **two observable macroscopic signs** that indicate a chemical reaction has taken place.\n"
            f"3. Explain the scientific reason for your classification in terms of the formation of new substances."
        )
        sample = (
            f"1. **Classification:** {scen[1]};\n"
            f"2. **Signs of Chemical Reaction:** {scen[3]} (or temperature change / permanent color change / effervescence / precipitate);\n"
            f"3. **Scientific Reason:** {scen[2]}."
        )
        marking = (
            f"• 1 mark: Correct classification ({scen[1]}) [1]\n"
            "• 2 marks: Two valid signs of chemical change (gas evolution, precipitate, permanent color change, heat/light) [2]\n"
            f"• 1 mark: Explanation relating to formation of new chemical substances ({scen[2]}) [1]\n"
            "**Total: 4 marks**"
        )
        return {
            "title": "Macroscopic Signs of Chemical Change",
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
                "Does this process make an entirely new chemical substance, or is it just changing shape or state?",
                "Think about bubbling (gas), temperature changes, light emission, or precipitates.",
                f"Classification: {scen[1]}. Signs: {scen[3]}. Reason: {scen[2]}.",
            ],
            "misconception_tags": ["phase_change_is_chemical_reaction_myth", "observable_reaction_signs_confusion"],
            "learning_objective_id": "NS9.MM.07.04",
        }

    # Subskill 5: Particle Reaction Modeling
    return _normalize_res(build_chemical_bonding_ns_question(actual_seed, grade=9, mode=mode))
