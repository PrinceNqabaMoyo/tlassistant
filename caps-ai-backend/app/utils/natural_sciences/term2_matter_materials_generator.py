"""Natural Sciences Senior Phase (Grades 7–9) — Term 2: Matter and Materials Generator.
Deterministic 6-pillar CAPS question generator covering:
- Grade 7: Physical Properties of Materials, Separation of Mixtures (filtration, distillation, chromatography), Acids & Bases (pH scale, litmus).
- Grade 8: Atomic Structure (protons, neutrons, electrons, atomic number), Particle Model of Matter (kinetic energy, diffusion, phase changes).
- Grade 9: Chemical Formulae, Reactions of Metals & Non-metals with Oxygen, Acid-Base Neutralisation, Acid-Metal Reactions.
Supports compound exam questions and atomic elementary sub-drills.
Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import (
    fmt_sa,
    make_science_question,
    rng,
)

TOPIC = "natural_sciences_matter_and_materials"
LO = "ns_senior_matter_and_materials"

# ============================================================================
# ARCHETYPE 1: SEPARATION OF MIXTURES (Grade 7)
# ============================================================================

MIXTURES_DATA = [
    {
        "mixture": "Sand, salt (sodium chloride), and water",
        "methods": "Filtration followed by Evaporation / Crystallisation",
        "explanation": "Sand is insoluble and is trapped on the filter paper as residue. Salt dissolves in water forming a solution (filtrate). Heating the filtrate evaporates water, leaving salt crystals behind.",
        "apparatus": "Filter funnel, filter paper, conical flask, evaporating dish, Bunsen burner, tripod and wire gauze.",
    },
    {
        "mixture": "Ethanol (boiling point 78 °C) and water (boiling point 100 °C)",
        "methods": "Fractional Distillation",
        "explanation": "Ethanol has a lower boiling point (78 °C) than water (100 °C). It boils first, vaporises, rises up the fractionating column, and condenses into a separate beaker via the Liebig condenser.",
        "apparatus": "Round-bottom flask, fractionating column, thermometer, Liebig condenser, cooling water tubes, receiving conical flask.",
    },
    {
        "mixture": "Iron filings, powdered sulphur, and dry sand",
        "methods": "Magnetic separation followed by solvent extraction or sedimentation",
        "explanation": "Iron is ferromagnetic and is separated immediately using a magnet wrapped in plastic. Sand and sulphur remain.",
        "apparatus": "Bar magnet, Petri dish, plastic film barrier.",
    },
    {
        "mixture": "Water-soluble food dyes (black ink sample)",
        "methods": "Paper Chromatography",
        "explanation": "Different dye pigments have different solubilities in the solvent and different affinities for the chromatography paper. More soluble pigments travel faster and further up the paper.",
        "apparatus": "Chromatography paper strip, capillary tube, beaker, solvent (water or ethanol), pencil baseline, watch glass cover.",
    },
]


def _gen_separating_mixtures_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    mix = r.choice(MIXTURES_DATA)
    
    prompt = (
        f"A laboratory technician presents Grade 7 learners with an unseparated mixture containing: **{mix['mixture']}**.\n\n"
        f"1. Name the scientific separation technique(s) required to isolate the pure components from this mixture.\n"
        f"2. Explain the physical property difference (e.g. solubility, boiling point, magnetism, particle size) that makes this separation possible.\n"
        f"3. List THREE key pieces of laboratory apparatus required to carry out this separation safely.\n"
        f"4. Describe the step-by-step procedure the learners must follow to obtain the dry, purified components."
    )
    prompt_latex = (
        rf"\textbf{{Physical Separation of Mixtures: {mix['mixture']}}}" "\n\n"
        rf"\text{{1. Separation method(s): Required technique}}" "\n"
        rf"\text{{2. Underlying physical property difference}}" "\n"
        rf"\text{{3. Laboratory apparatus specifications}}" "\n"
        rf"\text{{4. Step-by-step procedure: Isolation and purification}}"
    )
    answer_latex = (
        rf"\text{{1. Method: {mix['methods']}.}}" "\n"
        rf"\text{{2. Physical property: Based on difference in {mix['explanation'][:90]}...}}" "\n"
        rf"\text{{3. Apparatus: {mix['apparatus']}.}}" "\n"
        rf"\text{{4. Procedure: {mix['explanation']}}}"
    )
    sample = (
        f"1. Technique(s): {mix['methods']}.\n"
        f"2. Underlying physical property: {mix['explanation']}\n"
        f"3. Required apparatus: {mix['apparatus']}.\n"
        f"4. Step-by-step procedure: Follow {mix['methods']} by carefully setting up apparatus, collecting residue/filtrate/distillate as described above."
    )
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Correct separation technique named", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Accurate physical property difference identified", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Appropriate laboratory apparatus listed", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Logically ordered, valid experimental procedure", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Think about whether the components dissolve, have different boiling temperatures, or are magnetic.",
        "concept": "Mixtures are physically combined substances separated by exploiting differences in physical properties (boiling point, solubility, density).",
        "breakdown": f"Mixture: {mix['mixture']}. Method: {mix['methods']}.",
    }
    return make_science_question(
        prefix="ns_sep_mix",
        topic=TOPIC,
        subskill="separation_of_mixtures_laboratory_methodology",
        learning_objective_id=f"{LO}_separating_mixtures",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["confusing_filtrate_with_residue", "confusing_evaporation_with_distillation"],
        keywords=["filtration", "distillation", "chromatography", "solubility", "boiling point"],
        term=2,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=6,
    )


# ============================================================================
# ARCHETYPE 2: ATOMIC STRUCTURE & PERIODIC TABLE (Grade 8)
# ============================================================================

ELEMENTS_DB = [
    {"name": "Lithium", "symbol": "Li", "z": 3, "a": 7, "group": 1, "period": 2, "state": "Solid metal"},
    {"name": "Carbon", "symbol": "C", "z": 6, "a": 12, "group": 14, "period": 2, "state": "Solid non-metal"},
    {"name": "Nitrogen", "symbol": "N", "z": 7, "a": 14, "group": 15, "period": 2, "state": "Gas (diatomic non-metal)"},
    {"name": "Oxygen", "symbol": "O", "z": 8, "a": 16, "group": 16, "period": 2, "state": "Gas (diatomic non-metal)"},
    {"name": "Sodium", "symbol": "Na", "z": 11, "a": 23, "group": 1, "period": 3, "state": "Alkali metal"},
    {"name": "Magnesium", "symbol": "Mg", "z": 12, "a": 24, "group": 2, "period": 3, "state": "Alkaline earth metal"},
    {"name": "Aluminium", "symbol": "Al", "z": 13, "a": 27, "group": 13, "period": 3, "state": "Metal"},
    {"name": "Chlorine", "symbol": "Cl", "z": 17, "a": 35, "group": 17, "period": 3, "state": "Halogen gas"},
    {"name": "Calcium", "symbol": "Ca", "z": 20, "a": 40, "group": 2, "period": 4, "state": "Alkaline earth metal"},
]


def _gen_atomic_structure_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    el = r.choice(ELEMENTS_DB)
    protons = el["z"]
    electrons = el["z"]
    neutrons = el["a"] - el["z"]
    
    prompt = (
        f"Consider an electrically neutral atom of the element **{el['name']}** with atomic number (Z) = {el['z']} "
        f"and mass number (A) = {el['a']}.\n\n"
        f"1. Write the standard chemical notation ($^{{A}}_{{Z}}\\text{{X}}$) for this atom.\n"
        f"2. Determine the exact number of:\n"
        f"   (a) Protons in the nucleus\n"
        f"   (b) Neutrons in the nucleus\n"
        f"   (c) Electrons orbiting in electron energy levels (shells)\n"
        f"3. State the electrical charge and exact location of each of the three subatomic particles.\n"
        f"4. Explain why a neutral atom carries an overall electrical charge of zero."
    )
    prompt_latex = (
        rf"\textbf{{Subatomic Particle Analysis: {el['name']}}}" "\n\n"
        rf"\text{{Standard Nuclide Notation: }}^{{{el['a']}}}_{{{el['z']}}}\text{{{el['symbol']}}}" "\n"
        r"\text{Calculate proton count } (p), \text{ neutron count } (n = A - Z), \text{ and electron count } (e)." "\n"
        r"\text{State subatomic charges, spatial locations, and electrical neutrality.}"
    )
    answer_latex = (
        rf"\text{{1. Notation: }}^{{{el['a']}}}_{{{el['z']}}}\text{{{el['symbol']}}}" "\n"
        rf"\text{{2. (a) Protons }} = {protons}, \quad \text{{(b) Neutrons }} = {neutrons}\text{{ (from }} {el['a']} - {el['z']}), \quad \text{{(c) Electrons }} = {electrons}" "\n"
        r"\text{3. Protons: } +1\text{ charge (nucleus); Neutrons: neutral } 0\text{ (nucleus); Electrons: } -1\text{ (orbiting shells).}" "\n"
        r"\text{4. The number of positively charged protons equals the number of negatively charged electrons, canceling each other out.}"
    )
    sample = (
        f"1. Notation: ^{el['a']}_{el['z']}{el['symbol']}\n"
        f"2. (a) Protons = {protons}\n"
        f"   (b) Neutrons = {neutrons} ({el['a']} - {el['z']})\n"
        f"   (c) Electrons = {electrons}\n"
        "3. Protons have a +1 charge and reside in the central nucleus; Neutrons have 0 charge and reside in the nucleus; Electrons have a -1 charge and orbit in energy shells.\n"
        f"4. A neutral atom has equal numbers of positive protons ({protons} x +1 = +{protons}) and negative electrons ({electrons} x -1 = -{electrons}), resulting in a net charge of zero."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Accurate standard nuclide notation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct protons ({protons})", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct neutrons ({neutrons} via A - Z)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct electrons ({electrons})", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Correct charges and locations of all 3 particles", "marks": 2, "editable": True},
            {"id": "mp6", "desc": "Scientific explanation of overall electrical neutrality", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Atomic number Z = number of protons. Mass number A = protons + neutrons.",
        "concept": "Neutrons = A - Z. In a neutral atom, electrons = protons.",
        "breakdown": f"For {el['name']}: Z = {el['z']} protons; A - Z = {el['a']} - {el['z']} = {neutrons} neutrons; electrons = {el['z']}.",
    }
    return make_science_question(
        prefix="ns_atom",
        topic=TOPIC,
        subskill="atomic_structure_and_subatomic_calculations",
        learning_objective_id=f"{LO}_atomic_structure",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["calculating_neutrons_incorrectly", "confusing_atomic_number_with_mass_number"],
        keywords=["protons", "neutrons", "electrons", "nucleus", "atomic number", "mass number"],
        term=2,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=7,
    )


# ============================================================================
# ARCHETYPE 3: ACIDS, BASES & CHEMICAL REACTIONS (Grade 9)
# ============================================================================

ACID_BASE_PAIRS = [
    {
        "acid": "Hydrochloric acid",
        "acid_formula": r"\text{HCl}",
        "base": "Sodium hydroxide",
        "base_formula": r"\text{NaOH}",
        "salt": "Sodium chloride",
        "salt_formula": r"\text{NaCl}",
        "word_eq": "Hydrochloric acid + Sodium hydroxide -> Sodium chloride + Water",
        "balanced": r"\text{HCl} + \text{NaOH} \to \text{NaCl} + \text{H}_2\text{O}",
        "ph_indicator": "Bromothymol blue turns from yellow (acid) to green at neutral pH ~ 7.",
    },
    {
        "acid": "Sulphuric acid",
        "acid_formula": r"\text{H}_2\text{SO}_4",
        "base": "Magnesium hydroxide",
        "base_formula": r"\text{Mg(OH)}_2",
        "salt": "Magnesium sulphate",
        "salt_formula": r"\text{MgSO}_4",
        "word_eq": "Sulphuric acid + Magnesium hydroxide -> Magnesium sulphate + Water",
        "balanced": r"\text{H}_2\text{SO}_4 + \text{Mg(OH)}_2 \to \text{MgSO}_4 + 2\text{H}_2\text{O}",
        "ph_indicator": "Universal indicator turns green (neutral pH 7) at complete neutralisation.",
    },
    {
        "acid": "Nitric acid",
        "acid_formula": r"\text{HNO}_3",
        "base": "Potassium hydroxide",
        "base_formula": r"\text{KOH}",
        "salt": "Potassium nitrate",
        "salt_formula": r"\text{KNO}_3",
        "word_eq": "Nitric acid + Potassium hydroxide -> Potassium nitrate + Water",
        "balanced": r"\text{HNO}_3 + \text{KOH} \to \text{KNO}_3 + \text{H}_2\text{O}",
        "ph_indicator": "Phenolphthalein turns from pink (basic) to colourless as acid neutralises the base.",
    },
]


def _gen_acid_base_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    rx = r.choice(ACID_BASE_PAIRS)
    
    prompt = (
        f"A laboratory experiment involves reacting **{rx['acid']}** ({rx['acid_formula']}) with **{rx['base']}** ({rx['base_formula']}).\n\n"
        f"1. Classify this type of chemical reaction.\n"
        f"2. Write the complete **word equation** for this reaction.\n"
        f"3. Write the **balanced chemical equation** including all chemical formulae.\n"
        f"4. State the expected colour change when testing the resulting neutral salt solution with litmus paper.\n"
        f"5. What general name is given to the family of ionic compounds formed when an acid reacts with a base?"
    )
    prompt_latex = (
        rf"\textbf{{Acid-Base Neutralisation Chemistry}}" "\n\n"
        rf"\text{{Reactants: {rx['acid']} ({rx['acid_formula']}) + {rx['base']} ({rx['base_formula']})}}" "\n\n"
        r"\text{1. Reaction classification; 2. Word equation; 3. Balanced symbolic equation;}" "\n"
        r"\text{4. Indicator response; 5. Compound taxonomy.}"
    )
    answer_latex = (
        r"\text{1. Neutralisation reaction.}" "\n"
        rf"\text{{2. {rx['word_eq']}}}" "\n"
        rf"\text{{3. {rx['balanced']}}}" "\n"
        r"\text{4. Neither red nor blue litmus changes colour (neutral solution remains neutral).}" "\n"
        r"\text{5. A Salt (ionic compound consisting of a metal cation and non-metal anion).}"
    )
    sample = (
        f"1. Neutralisation reaction.\n"
        f"2. Word equation: {rx['word_eq']}\n"
        f"3. Balanced chemical equation: {rx['balanced']}\n"
        "4. Red litmus remains red and blue litmus remains blue because the resulting solution has a neutral pH of 7.\n"
        "5. A Salt."
    )
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Identify neutralisation reaction", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Accurate word equation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Accurate balanced chemical equation with correct coefficients", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Correct litmus behaviour at neutral pH 7", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Identify class of compound as a salt", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "An acid plus a base always yields a salt and water: Acid + Base -> Salt + Water.",
        "concept": "Neutralisation occurs when H+ ions from acid combine with OH- ions from base to form neutral H2O molecules.",
        "breakdown": f"Salt formed from {rx['acid']} and {rx['base']} is {rx['salt']}.",
    }
    return make_science_question(
        prefix="ns_acid_base",
        topic=TOPIC,
        subskill="acid_base_neutralisation_and_equation_balancing",
        learning_objective_id=f"{LO}_acid_base_reactions",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["failing_to_balance_water_coefficient", "confusing_neutralisation_with_precipitation"],
        keywords=["acid", "base", "neutralisation", "salt", "litmus", "pH"],
        term=2,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=6,
    )


# ============================================================================
# MAIN DISPATCH ENTRY POINT
# ============================================================================

def generate(seed: Optional[int] = None, grade: int = 8, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    """Generates a fully formed 6-pillar Natural Sciences Matter & Materials question."""
    r = rng(seed)
    
    if archetype == "separation" or (archetype is None and grade == 7):
        return _gen_separating_mixtures_question(r, mode=mode)
    elif archetype == "atomic_structure" or (archetype is None and grade == 8):
        return _gen_atomic_structure_question(r, mode=mode)
    elif archetype == "acid_base" or (archetype is None and grade == 9):
        return _gen_acid_base_question(r, mode=mode)
    else:
        choice = r.choice(["separation", "atomic_structure", "acid_base"])
        if choice == "separation":
            return _gen_separating_mixtures_question(r, mode=mode)
        elif choice == "atomic_structure":
            return _gen_atomic_structure_question(r, mode=mode)
        else:
            return _gen_acid_base_question(r, mode=mode)
