"""Natural Sciences (Grades 8–9) — Chemical Reactions & Equations (Deterministic 6-Pillar Generator).
Covers balancing chemical equations, acid-base neutralisation, combustion of metals/non-metals, and the Law of Conservation of Matter.
Supports full compound exam questions and atomic elementary sub-drills for adaptive regression.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import (
    make_science_question,
    rng,
)

TOPIC = "natural_sciences_chemical_reactions"
LO = "ns_chemical_reactions"

# Canonical CAPS reaction catalogue
REACTIONS_DB = [
    {
        "id": "combustion_mg",
        "name": "Combustion of Magnesium metal",
        "type": "Reaction of a metal with oxygen (Combustion)",
        "reactants_words": "Magnesium + Oxygen",
        "products_words": "Magnesium oxide",
        "unbalanced": r"\text{Mg} + \text{O}_2 \to \text{MgO}",
        "balanced": r"2\text{Mg} + \text{O}_2 \to 2\text{MgO}",
        "coefficients": [2, 1, 2],
        "atom_count": "Reactants: 2 Mg, 2 O | Products: 2 Mg, 2 O",
        "observation": "Magnesium burns with a brilliant, blinding white flame leaving behind a white powdery ash (magnesium oxide).",
        "ph_effect": "Magnesium oxide is a metal oxide (basic). When dissolved in water, it turns red litmus paper blue.",
    },
    {
        "id": "combustion_fe",
        "name": "Combustion / Rusting of Iron",
        "type": "Reaction of a metal with oxygen",
        "reactants_words": "Iron + Oxygen",
        "products_words": "Iron(III) oxide (Rust)",
        "unbalanced": r"\text{Fe} + \text{O}_2 \to \text{Fe}_2\text{O}_3",
        "balanced": r"4\text{Fe} + 3\text{O}_2 \to 2\text{Fe}_2\text{O}_3",
        "coefficients": [4, 3, 2],
        "atom_count": "Reactants: 4 Fe, 6 O | Products: 4 Fe, 6 O",
        "observation": "Iron glows reddish-orange and forms a reddish-brown brittle solid (iron oxide).",
        "ph_effect": "Iron oxide is an insoluble basic metal oxide.",
    },
    {
        "id": "combustion_c",
        "name": "Combustion of Carbon",
        "type": "Reaction of a non-metal with oxygen",
        "reactants_words": "Carbon + Oxygen",
        "products_words": "Carbon dioxide",
        "unbalanced": r"\text{C} + \text{O}_2 \to \text{CO}_2",
        "balanced": r"\text{C} + \text{O}_2 \to \text{CO}_2",
        "coefficients": [1, 1, 1],
        "atom_count": "Reactants: 1 C, 2 O | Products: 1 C, 2 O",
        "observation": "Carbon burns with an orange glow and produces a colourless gas that turns clear limewater milky.",
        "ph_effect": "Carbon dioxide dissolves in water to form carbonic acid (turns blue litmus red, pH ~ 5-6).",
    },
    {
        "id": "neutralisation_hcl_naoh",
        "name": "Neutralisation of Hydrochloric acid and Sodium hydroxide",
        "type": "Acid-Base Neutralisation",
        "reactants_words": "Hydrochloric acid + Sodium hydroxide",
        "products_words": "Sodium chloride (table salt) + Water",
        "unbalanced": r"\text{HCl} + \text{NaOH} \to \text{NaCl} + \text{H}_2\text{O}",
        "balanced": r"\text{HCl} + \text{NaOH} \to \text{NaCl} + \text{H}_2\text{O}",
        "coefficients": [1, 1, 1, 1],
        "atom_count": "Reactants: 2 H, 1 Cl, 1 Na, 1 O | Products: 2 H, 1 Cl, 1 Na, 1 O",
        "observation": "A clear, neutral solution of table salt dissolved in water is formed; the temperature increases (exothermic reaction).",
        "ph_effect": "The pH neutralises towards pH 7 (universal indicator turns green).",
    },
    {
        "id": "acid_carbonate_caco3",
        "name": "Reaction of Hydrochloric acid with Calcium carbonate",
        "type": "Reaction of an acid with a metal carbonate",
        "reactants_words": "Hydrochloric acid + Calcium carbonate",
        "products_words": "Calcium chloride + Water + Carbon dioxide",
        "unbalanced": r"\text{HCl} + \text{CaCO}_3 \to \text{CaCl}_2 + \text{H}_2\text{O} + \text{CO}_2",
        "balanced": r"2\text{HCl} + \text{CaCO}_3 \to \text{CaCl}_2 + \text{H}_2\text{O} + \text{CO}_2",
        "coefficients": [2, 1, 1, 1, 1],
        "atom_count": "Reactants: 2 H, 2 Cl, 1 Ca, 1 C, 3 O | Products: 2 H, 2 Cl, 1 Ca, 1 C, 3 O",
        "observation": "Vigorous effervescence (bubbles of gas); the gas produced turns clear limewater milky.",
        "ph_effect": "The strongly acidic solution (pH 1-2) increases in pH towards neutral as acid is consumed.",
    },
]

PH_SUBSTANCES = [
    {"substance": "Hydrochloric acid (stomach acid)", "ph": 1.5, "nature": "Strong acid", "color": "Red"},
    {"substance": "Lemon juice (citric acid)", "ph": 2.5, "nature": "Weak acid", "color": "Orange-red"},
    {"substance": "Pure distilled water", "ph": 7.0, "nature": "Neutral", "color": "Green"},
    {"substance": "Baking soda solution (sodium bicarbonate)", "ph": 8.5, "nature": "Weak base / alkali", "color": "Blue-green"},
    {"substance": "Soapy water", "ph": 9.5, "nature": "Base / alkali", "color": "Blue"},
    {"substance": "Drain cleaner (sodium hydroxide)", "ph": 13.5, "nature": "Strong base / alkali", "color": "Purple / Violet"},
]


# --------------------------------------------------------------------------- #
# Sub-Drill: Balancing Atoms
# --------------------------------------------------------------------------- #
def _build_balancing_drill(r: random.Random, difficulty: str) -> Dict[str, Any]:
    rxn = r.choice(REACTIONS_DB)

    prompt = (
        f"Consider the unbalanced chemical symbol equation:\n\n"
        f"$${rxn['unbalanced']}$$\n\n"
        f"1. Balance this chemical equation by providing the correct integer balancing coefficients.\n"
        f"2. Verify that the Law of Conservation of Matter holds by writing down the total number of each type of atom on both sides."
    )

    sample_answer = (
        f"Balanced Equation:\n"
        f"$${rxn['balanced']}$$\n\n"
        f"Conservation of Matter Verification:\n"
        f"{rxn['atom_count']}"
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correctly balanced chemical equation: {rxn['balanced']}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Correct atom counts on reactant and product sides", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "changed_chemical_subscripts", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Never alter the small subscript numbers inside chemical formulas; only place whole numbers (coefficients) in front.",
        "concept": "The Law of Conservation of Matter states that atoms cannot be created or destroyed in a chemical reaction. The count of each element on the left must equal the right.",
        "breakdown": f"Balanced equation: $${rxn['balanced']}$$. Verification: {rxn['atom_count']}.",
    }

    return make_science_question(
        prefix="ns_chem_bal",
        topic=TOPIC,
        subskill="balancing_equations_elementary",
        learning_objective_id=f"{LO}_balancing",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rxn["balanced"],
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["altered_chemical_subscripts_to_balance", "unbalanced_atom_counts"],
        keywords=["balancing equations", "chemical symbols", "reactants", "products", "conservation of matter"],
        term=2,
        caps_weight_percent=25,
        suggested_duration_mins=3,
        mode="elementary_balancing_atoms",
        difficulty="medium",
        marks=3,
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: pH Scale & Indicator Identification
# --------------------------------------------------------------------------- #
def _build_ph_drill(r: random.Random, difficulty: str) -> Dict[str, Any]:
    sub = r.choice(PH_SUBSTANCES)

    prompt = (
        f"A laboratory sample of **{sub['substance']}** is measured to have a $\\text{{pH}}$ value of **{sub['ph']}**.\n\n"
        f"1. Classify this substance as an **acid**, a **base/alkali**, or **neutral**.\n"
        f"2. Is it a strong or weak substance?\n"
        f"3. What color would Universal Indicator turn when added to this solution?"
    )

    ans_latex = rf"\text{{Classification: }} {sub['nature']}, \quad \text{{Universal Indicator Color: }} {sub['color']}"

    sample_answer = (
        f"1. Classification: {sub['nature']}\n"
        f"2. Explanation: Substances with pH < 7 are acidic, pH = 7 is neutral, and pH > 7 are basic/alkaline.\n"
        f"3. Universal Indicator Color: {sub['color']}"
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct acid/base/neutral classification: {sub['nature']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Reference to pH position on 0-14 scale", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct Universal Indicator color: {sub['color']}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Recall the standard pH scale running from 0 to 14.",
        "concept": "pH 0–2: Strong acid (Red); pH 3–6: Weak acid (Orange/Yellow); pH 7: Neutral (Green); pH 8–11: Weak base (Blue); pH 12–14: Strong base (Purple).",
        "breakdown": f"pH {sub['ph']} falls in the {sub['nature'].lower()} range and turns Universal Indicator {sub['color'].lower()}.",
    }

    return make_science_question(
        prefix="ns_chem_ph",
        topic=TOPIC,
        subskill="ph_scale_elementary",
        learning_objective_id=f"{LO}_ph_scale",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["inverted_ph_scale_direction", "confused_acid_and_base_color"],
        keywords=["pH scale", "acids", "bases", "neutral", "universal indicator", "litmus"],
        term=2,
        caps_weight_percent=20,
        suggested_duration_mins=2,
        mode="elementary_ph_scale_identification",
        difficulty="easy",
        marks=3,
    )


# --------------------------------------------------------------------------- #
# Sub-Drill: Reactants & Products Identification
# --------------------------------------------------------------------------- #
def _build_reactants_products_drill(r: random.Random, difficulty: str) -> Dict[str, Any]:
    rxn = r.choice(REACTIONS_DB)

    prompt = (
        f"Consider the following chemical reaction description:\n"
        f"$$\\text{{{rxn['reactants_words']}}} \\longrightarrow \\text{{{rxn['products_words']}}}$$\n\n"
        f"1. Name the **reactants** in this reaction.\n"
        f"2. Name the **products** in this reaction.\n"
        f"3. Classify the reaction type (e.g. combustion of a metal, combustion of a non-metal, neutralisation, acid-carbonate)."
    )

    sample_answer = (
        f"1. Reactants (starting substances on the left of the arrow): {rxn['reactants_words']}\n"
        f"2. Products (new substances formed on the right of the arrow): {rxn['products_words']}\n"
        f"3. Reaction Type: {rxn['type']}"
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct reactants identified: {rxn['reactants_words']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct products identified: {rxn['products_words']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct reaction classification: {rxn['type']}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Reactants are the starting substances (before the arrow); products are what is produced (after the arrow).",
        "concept": "Reactants $\\to$ Products. Chemical reactions rearrange atoms to form new chemical bonds.",
        "breakdown": f"Reactants: {rxn['reactants_words']}. Products: {rxn['products_words']}. Type: {rxn['type']}.",
    }

    return make_science_question(
        prefix="ns_chem_rp",
        topic=TOPIC,
        subskill="reactants_products_elementary",
        learning_objective_id=f"{LO}_reactants_products",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=rf"\text{{Reactants: }} {rxn['reactants_words']}, \quad \text{{Products: }} {rxn['products_words']}",
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["swapped_reactants_and_products", "confused_word_and_symbol_equation"],
        keywords=["reactants", "products", "word equation", "chemical change"],
        term=2,
        caps_weight_percent=15,
        suggested_duration_mins=2,
        mode="elementary_reactants_products_identification",
        difficulty="easy",
        marks=3,
    )


# --------------------------------------------------------------------------- #
# Compound: Authentic CAPS Exam Standard Chemical Reaction Analysis (8 Marks)
# --------------------------------------------------------------------------- #
def _build_compound_reaction(r: random.Random, difficulty: str) -> Dict[str, Any]:
    rxn = r.choice(REACTIONS_DB)

    prompt = (
        f"A Grade 9 Natural Sciences laboratory practical investigates the reaction between **{rxn['reactants_words']}**.\n\n"
        f"1. Write down a balanced chemical symbol equation for this reaction. Include correct integer coefficients.\n"
        f"2. Classify this reaction type (e.g. combustion of a metal, combustion of a non-metal, neutralisation, acid-carbonate).\n"
        f"3. Describe ONE key visible observation during or after this reaction takes place.\n"
        f"4. State the Law of Conservation of Matter, and demonstrate that it is satisfied by providing an atom count of each element on both sides of the balanced equation."
    )

    sample_answer = (
        f"1. Balanced Chemical Symbol Equation:\n"
        f"   $${rxn['balanced']}$$\n\n"
        f"2. Reaction Classification:\n"
        f"   {rxn['type']}\n\n"
        f"3. Observable Evidence:\n"
        f"   {rxn['observation']}\n\n"
        f"4. Law of Conservation of Matter:\n"
        f"   *Matter cannot be created or destroyed in a chemical reaction; atoms are simply rearranged.*\n"
        f"   Atom Count:\n"
        f"   - {rxn['atom_count']}\n"
        f"   Since the number of each type of atom is identical on both sides, mass is conserved."
    )

    ans_latex = rf"{rxn['balanced']}, \quad \text{{Type: }} {rxn['type']}, \quad \text{{Atoms: }} {rxn['atom_count']}"

    marking_schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct chemical formulas of reactants and products: {rxn['unbalanced']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct balancing coefficients: {rxn['balanced']}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Correct reaction classification: {rxn['type']}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Accurate observable evidence (light, color change, gas, precipitate)", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Correct statement of the Law of Conservation of Matter", "marks": 1, "editable": True},
            {"id": "mp6", "desc": "Atom count demonstration on reactant and product sides", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "changed_subscripts_to_balance", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "First write down the correct formulas for the reactants and products, then count atoms on each side before balancing with coefficients.",
        "concept": (
            "1. Balance equations by placing coefficients in front: never change subscripts (e.g. write $2\\text{MgO}$, never $\\text{Mg}_2\\text{O}_2$).\n"
            "2. Total mass is conserved because no atoms appear or disappear: count atoms on both sides."
        ),
        "breakdown": (
            f"1. Balanced: $${rxn['balanced']}$$\n"
            f"2. Type: {rxn['type']}\n"
            f"3. Observation: {rxn['observation']}\n"
            f"4. {rxn['atom_count']}"
        ),
    }

    return make_science_question(
        prefix="ns_chem_compound",
        topic=TOPIC,
        subskill="chemical_reactions_compound",
        learning_objective_id=f"{LO}_compound_reaction",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=[
            "altered_chemical_subscripts_to_balance",
            "confused_reactants_and_products",
            "violated_conservation_of_matter",
        ],
        keywords=["chemical reaction", "balanced equation", "conservation of matter", "neutralisation", "combustion", "atoms"],
        term=2,
        caps_weight_percent=35,
        suggested_duration_mins=12,
        mode="compound",
        difficulty="hard",
        marks=8,
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_reaction,
    "elementary_balancing_atoms": _build_balancing_drill,
    "elementary_ph_scale_identification": _build_ph_drill,
    "elementary_reactants_products_identification": _build_reactants_products_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 8-9 Natural Sciences Chemical Reaction questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_reaction)

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
