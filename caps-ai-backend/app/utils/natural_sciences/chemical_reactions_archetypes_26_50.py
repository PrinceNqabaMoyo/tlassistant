"""Physical Sciences Grade 10 Term 3 — Reactions in Aqueous Solution.
Archetypes 26 to 50: Qualitative anion tests (CO3^2-), distinguishing protocols,
unknown salt identification, ion exchange driving forces, gas-forming reactions,
acid-base neutralisation, proton transfer, redox electron transfer, oxidation states,
oxidising/reducing agents, displacement reactions, precipitation stoichiometry,
antacid tablet analysis, and capstone synthesis.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import fmt_sa, make_science_question

TOPIC = "natural_sciences_chemical_reactions"
LO = "ps10_reactions_in_aqueous_solution"


# --------------------------------------------------------------------------- #
# Subskill 26: Qualitative Test for Carbonate Anion
# --------------------------------------------------------------------------- #
def arch_26_qualitative_test_for_carbonate_anion(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    salt_name = rng.choice(["sodium carbonate", "potassium carbonate", "calcium carbonate", "magnesium carbonate"])

    prompt = (
        f"A learner is provided with a sample of **{salt_name}** to verify that it contains carbonate ions ($\\text{{CO}}_3^{{2-}}$).\n\n"
        f"1. Name the reagent added directly to the solid or aqueous sample to initiate the test.\n"
        f"2. Describe the immediate visible observation when this reagent is added.\n"
        f"3. Name the gas produced in this reaction.\n"
        f"4. Describe the standard confirmatory chemical test used to identify this gas, including the observable result and the balanced chemical equation."
    )

    eq_gas = r"\text{Ca(OH)}_2(aq) + \text{CO}_2(g) \to \text{CaCO}_3(s) + \text{H}_2\text{O}(\ell)"
    ans_latex = rf"\text{{Gas: }}\text{{CO}}_2(g); \quad \text{{Limewater turns milky: }} {eq_gas}"

    sample_answer = (
        f"1. Reagent: **Dilute hydrochloric acid** ($\\text{{HCl}}$) or dilute nitric acid ($\\text{{HNO}}_3$).\n"
        f"2. Observation: **Vigorous effervescence / bubbling** (evolution of gas).\n"
        f"3. Gas produced: **Carbon dioxide gas** ($\\text{{CO}}_2$).\n"
        f"4. Confirmatory test: Bubble the gas through **clear limewater** (aqueous calcium hydroxide, $\\text{{Ca(OH)}}_2$).\n"
        f"   - Observable result: The clear limewater turns **milky / cloudy** due to the formation of a white precipitate of calcium carbonate ($\\text{{CaCO}}_3$).\n"
        f"   - Balanced equation:\n"
        f"     $${eq_gas}$$"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Correct reagent: dilute acid (HCl or HNO3)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Observation: vigorous effervescence / bubbling", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Gas identified: carbon dioxide / CO2", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Confirmatory test: bubble through clear limewater which turns milky/cloudy", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Balanced equation for limewater test: {eq_gas}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Acids react with carbonates to produce a common greenhouse gas.",
        "concept": "Carbonates release CO₂ gas with acid. CO₂ turns limewater milky by precipitating insoluble CaCO₃.",
        "breakdown": "Add dilute acid -> effervescence of CO₂. Bubble through limewater (Ca(OH)₂) -> turns milky (CaCO₃ precipitate).",
    }

    return make_science_question(
        prefix="ps10_aq_test_carb",
        topic=TOPIC,
        subskill="26_qualitative_test_for_carbonate_anion",
        learning_objective_id=f"{LO}_test_carbonate",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_limewater_with_lime_juice", "forgot_effervescence_observation"],
        keywords=["carbonate test", "carbon dioxide", "limewater", "effervescence", "calcium carbonate"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 27: Distinguishing Carbonate from Sulphate
# --------------------------------------------------------------------------- #
def arch_27_distinguishing_carbonate_from_sulphate(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cation_name, cat_sym = rng.choice([
        ("sodium", r"\text{Na}"),
        ("potassium", r"\text{K}"),
        ("ammonium", r"\text{NH}_4"),
    ])
    reagent_name, reagent_f = rng.choice([
        ("barium chloride", r"\text{BaCl}_2"),
        ("barium nitrate", r"\text{Ba(NO}_3)_2"),
    ])

    carb_f = rf"{cat_sym}_2\text{{CO}}_3" if "NH" not in cat_sym else r"(\text{NH}_4)_2\text{CO}_3"
    so4_f = rf"{cat_sym}_2\text{{SO}}_4" if "NH" not in cat_sym else r"(\text{NH}_4)_2\text{SO}_4"

    prompt = (
        f"Two unlabelled test tubes, **Tube A** and **Tube B**, contain separate colourless solutions of "
        f"**{cation_name} carbonate** (${carb_f}$) and **{cation_name} sulphate** (${so4_f}$).\n\n"
        f"A learner adds aqueous **{reagent_name}** (${reagent_f}$) to both test tubes. "
        f"A white precipitate forms in both tubes.\n\n"
        f"1. Write down the chemical formulas of the white precipitates in Tube A and Tube B.\n"
        f"2. Describe the next chemical step required to distinguish which tube contains the carbonate and which contains the sulphate.\n"
        f"3. State the expected observations for both tubes after this step.\n"
        f"4. Write down the balanced chemical equation for the reaction that occurs when acid is added to the carbonate precipitate."
    )

    eq_dissolve = r"\text{BaCO}_3(s) + 2\text{HNO}_3(aq) \to \text{Ba(NO}_3)_2(aq) + \text{H}_2\text{O}(\ell) + \text{CO}_2(g)"
    ans_latex = (
        r"\text{Precipitates: }\text{BaCO}_3(s)\text{ and }\text{BaSO}_4(s); \quad "
        r"\text{Add dilute }\text{HNO}_3; \quad \text{BaCO}_3\text{ dissolves with effervescence; }\text{BaSO}_4\text{ remains}"
    )

    sample_answer = (
        f"1. Precipitates: **$\\text{{BaCO}}_3(s)$** (barium carbonate) and **$\\text{{BaSO}}_4(s)$** (barium sulphate).\n"
        f"2. Add a few drops of **dilute nitric acid** ($\\text{{HNO}}_3$) to each test tube.\n"
        f"3. Expected observations:\n"
        f"   - **Carbonate tube**: The white precipitate dissolves with vigorous effervescence (bubbles of $\\text{{CO}}_2$ gas), leaving a clear colourless solution.\n"
        f"   - **Sulphate tube**: The white precipitate remains insoluble and unchanged (no reaction).\n"
        f"4. Equation for dissolving barium carbonate:\n"
        f"   $${eq_dissolve}$$"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Correct formulas for both precipitates: BaCO3 and BaSO4", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Step described: add dilute nitric acid (HNO3)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Observation for carbonate: precipitate dissolves with effervescence", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Observation for sulphate: precipitate remains unchanged / insoluble", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Balanced equation: {eq_dissolve}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Both barium carbonate and barium sulphate form white precipitates, but only one dissolves in acid.",
        "concept": "BaCO₃ reacts with acid to form soluble Ba²⁺, water, and CO₂. BaSO₄ is insoluble in dilute acid.",
        "breakdown": "Precipitates: BaCO₃ and BaSO₄. Add dilute HNO₃: BaCO₃ dissolves with bubbles; BaSO₄ stays solid.",
    }

    return make_science_question(
        prefix="ps10_aq_dist_carb_so4",
        topic=TOPIC,
        subskill="27_distinguishing_carbonate_from_sulphate",
        learning_objective_id=f"{LO}_dist_carb_so4",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["suggested_sulfuric_acid_for_testing_sulphate", "thought_baso4_dissolves_in_acid"],
        keywords=["distinguishing test", "barium carbonate", "barium sulphate", "nitric acid", "effervescence"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 28: Distinguishing Carbonate from Chloride
# --------------------------------------------------------------------------- #
def arch_28_distinguishing_carbonate_from_chloride(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    metal_name, cat_sym = rng.choice([
        ("sodium", r"\text{Na}"),
        ("potassium", r"\text{K}"),
        ("lithium", r"\text{Li}"),
    ])

    prompt = (
        f"A technician has two unlabelled bottles containing aqueous **{metal_name} chloride** (${cat_sym}\\text{{Cl}}$) and "
        f"**{metal_name} carbonate** (${cat_sym}_2\\text{{CO}}_3$).\n\n"
        f"When aqueous **silver nitrate** ($\\text{{AgNO}}_3$) is added to samples of both solutions, "
        f"both produce a white precipitate.\n\n"
        f"1. Write down the formulas of the white precipitates formed in the chloride and carbonate solutions.\n"
        f"2. What reagent should be added to distinguish between the two precipitates?\n"
        f"3. State what will be observed for each solution upon addition of this reagent.\n"
        f"4. Write down the balanced chemical equation for the reaction that takes place in the tube that changes."
    )

    eq_dissolve = r"\text{Ag}_2\text{CO}_3(s) + 2\text{HNO}_3(aq) \to 2\text{AgNO}_3(aq) + \text{H}_2\text{O}(\ell) + \text{CO}_2(g)"
    ans_latex = (
        r"\text{Precipitates: }\text{AgCl}(s)\text{ and }\text{Ag}_2\text{CO}_3(s); \quad "
        r"\text{Add dilute }\text{HNO}_3; \quad \text{Ag}_2\text{CO}_3\text{ dissolves with gas; }\text{AgCl}\text{ remains unchanged}"
    )

    sample_answer = (
        f"1. Precipitates formed: **$\\text{{AgCl}}(s)$** (silver chloride) and **$\\text{{Ag}}_2\\text{{CO}}_3(s)$** (silver carbonate).\n"
        f"2. Reagent to distinguish: **Dilute nitric acid** ($\\text{{HNO}}_3$).\n"
        f"3. Observations:\n"
        f"   - **Silver chloride (AgCl)**: Precipitate remains insoluble / unchanged.\n"
        f"   - **Silver carbonate (Ag₂CO₃)**: Precipitate dissolves with effervescence (bubbles of $\\text{{CO}}_2$ gas), yielding a clear colourless solution.\n"
        f"4. Balanced equation:\n"
        f"   $${eq_dissolve}$$"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Correct formulas for both precipitates: AgCl and Ag2CO3", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct reagent: dilute nitric acid (HNO3)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Observation for chloride: AgCl precipitate remains unchanged", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Observation for carbonate: Ag2CO3 dissolves with effervescence", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Balanced equation: {eq_dissolve}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Both Ag⁺ + Cl⁻ and Ag⁺ + CO₃²⁻ form white precipitates. Which one dissolves in acid with effervescence?",
        "concept": "AgCl is insoluble in nitric acid. Ag₂CO₃ dissolves in nitric acid forming soluble silver nitrate, water, and CO₂ gas.",
        "breakdown": "Precipitates: AgCl and Ag₂CO₃. Add dilute HNO₃: Ag₂CO₃ effervesces and dissolves; AgCl remains unchanged.",
    }

    return make_science_question(
        prefix="ps10_aq_dist_carb_cl",
        topic=TOPIC,
        subskill="28_distinguishing_carbonate_from_chloride",
        learning_objective_id=f"{LO}_dist_carb_cl",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["suggested_hcl_to_test_chloride", "forgot_silver_carbonate_formula"],
        keywords=["distinguishing test", "silver chloride", "silver carbonate", "nitric acid", "effervescence"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 29: Unknown Salt Identification Protocol (Flowchart Analysis)
# --------------------------------------------------------------------------- #
def arch_29_unknown_salt_identification_protocol(rng: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    unknown_salts = [
        {"salt": "Copper(II) sulphate", "formula": r"\text{CuSO}_4", "cation_test": "Add NaOH(aq) -> light blue precipitate formed", "anion_test": "Add BaCl2(aq) -> white precipitate formed, which does not dissolve in dilute HNO3", "cation": "Cu²⁺", "anion": "SO₄²⁻"},
        {"salt": "Iron(III) chloride", "formula": r"\text{FeCl}_3", "cation_test": "Add NaOH(aq) -> reddish-brown precipitate formed", "anion_test": "Add AgNO3(aq) -> white precipitate formed, which does not dissolve in dilute HNO3", "cation": "Fe³⁺", "anion": "Cl⁻"},
        {"salt": "Barium chloride", "formula": r"\text{BaCl}_2", "cation_test": "Flame test -> pale green flame; add Na2SO4 -> white precipitate formed", "anion_test": "Add AgNO3(aq) -> white precipitate formed, which does not dissolve in dilute HNO3", "cation": "Ba²⁺", "anion": "Cl⁻"},
    ]
    u = rng.choice(unknown_salts)

    prompt = (
        f"A white/coloured crystalline solid **Salt X** is analysed through systematic qualitative tests:\n\n"
        f"- **Test 1 (Cation Analysis)**: {u['cation_test']}.\n"
        f"- **Test 2 (Anion Analysis)**: {u['anion_test']}.\n\n"
        f"1. Identify the cation present in Salt X (name and symbol with charge).\n"
        f"2. Identify the anion present in Salt X (name and symbol with charge).\n"
        f"3. Write down the chemical name and formula of **Salt X**.\n"
        f"4. Write down the balanced **net ionic equation** for the precipitate formed in Test 2."
    )

    net_eq = (
        r"\text{Ba}^{2+}(aq) + \text{SO}_4^{2-}(aq) \to \text{BaSO}_4(s)"
        if "SO_4" in u["formula"]
        else r"\text{Ag}^+(aq) + \text{Cl}^-(aq) \to \text{AgCl}(s)"
    )

    ans_latex = rf"\text{{Salt X: }}{u['salt']} ({u['formula']}); \quad \text{{Net Ionic: }}{net_eq}"

    sample_answer = (
        f"1. Cation: **{u['cation']}** (e.g. {u['salt'].split()[0]}).\n"
        f"2. Anion: **{u['anion']}** (e.g. {u['salt'].split()[1]}).\n"
        f"3. Chemical name: **{u['salt']}**; Chemical formula: **${u['formula']}$**.\n"
        f"4. Net ionic equation for Test 2:\n"
        f"   $${net_eq}$$"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct cation identified with charge: {u['cation']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct anion identified with charge: {u['anion']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct salt name: {u['salt']}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct chemical formula: {u['formula']}", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Correct net ionic equation: {net_eq}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Combine the cation observation (colour with NaOH/flame) and the anion observation (reagent + acid).",
        "concept": "Blue precipitate indicates Cu²⁺; reddish-brown indicates Fe³⁺. Insoluble Ba precipitate indicates SO₄²⁻; insoluble Ag precipitate indicates Cl⁻.",
        "breakdown": f"Test 1 confirms {u['cation']}. Test 2 confirms {u['anion']}. Salt X is {u['salt']} ({u['formula']}).",
    }

    return make_science_question(
        prefix="ps10_aq_unknown_salt",
        topic=TOPIC,
        subskill="29_unknown_salt_identification_protocol",
        learning_objective_id=f"{LO}_unknown_salt",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["wrong_salt_formula_balancing", "mismatched_cation_anion_identity"],
        keywords=["qualitative analysis", "unknown salt", "anion test", "cation test", "precipitate"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 30: Ion Exchange Reaction General Form & Driving Forces
# --------------------------------------------------------------------------- #
def arch_30_ion_exchange_reaction_general_form(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    focus = rng.choice([
        {"name": "precipitation", "desc": "formation of an insoluble solid crystal lattice"},
        {"name": "gas formation", "desc": "evolution of an insoluble or volatile gas such as CO2 or SO2"},
        {"name": "neutralisation / water formation", "desc": "formation of stable neutral water molecules from H+ and OH-"},
    ])

    prompt = (
        f"Many chemical reactions occurring in aqueous solution are classified as **ion exchange reactions**.\n\n"
        f"1. Write down the general symbolic equation representing an ion exchange reaction.\n"
        f"2. Define an **ion exchange reaction** in terms of ion movement.\n"
        f"3. Name the THREE distinct physical or chemical **driving forces** that allow ion exchange reactions to proceed.\n"
        f"4. Focus specifically on **{focus['name']}**: explain why the {focus['desc']} drives the reaction forward to completion."
    )

    ans_latex = r"\text{AB}(aq) + \text{CD}(aq) \to \text{AD} + \text{CB}; \quad \text{Driving forces: (1) Precipitation, (2) Gas formation, (3) Water formation}"

    sample_answer = (
        f"1. General equation:\n"
        f"   $$\\text{{AB}}(aq) + \\text{{CD}}(aq) \\to \\text{{AD}} + \\text{{CB}}$$\n"
        f"2. Definition: An ion exchange reaction is a type of reaction where the positive ions swap their respective negative partners due to a driving force.\n"
        f"3. The THREE driving forces are:\n"
        f"   - **Precipitation** (formation of an insoluble solid)\n"
        f"   - **Gas formation** (formation of an insoluble or volatile gas)\n"
        f"   - **Formation of water / weak electrolyte** (neutralisation of H⁺ and OH⁻)\n"
        f"4. Driving force of {focus['name']}:\n"
        f"   The {focus['desc']} effectively removes ions from the aqueous phase so that they cannot easily recombine in the reverse direction, driving the equilibrium forward."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "General equation: AB + CD -> AD + CB", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Definition: positive ions exchange negative partners due to a driving force", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Three driving forces named: precipitate, gas, and water/neutralisation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "One valid illustrative chemical equation for each driving force", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "What makes an ion exchange reaction go forward? Removing ions from solution via a solid, gas, or water molecule.",
        "concept": "Reactions in aqueous solution occur spontaneously only if products remove free ions from solution.",
        "breakdown": "General form: AB + CD -> AD + CB. 3 driving forces: Precipitation, Gas formation, Neutralisation (water formation).",
    }

    return make_science_question(
        prefix="ps10_aq_ion_exch_gen",
        topic=TOPIC,
        subskill="30_ion_exchange_reaction_general_form",
        learning_objective_id=f"{LO}_ion_exchange_general",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_ion_exchange_with_redox", "omitted_driving_forces"],
        keywords=["ion exchange", "driving force", "precipitation", "gas formation", "neutralisation"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 31: Gas-Forming Reactions — Carbonate and Acid
# --------------------------------------------------------------------------- #
def arch_31_gas_forming_reactions_carbonate_acid(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    cases = [
        {"acid": "hydrochloric acid", "acid_f": r"\text{HCl}", "carb": "calcium carbonate", "carb_f": r"\text{CaCO}_3", "salt_f": r"\text{CaCl}_2", "salt_name": "calcium chloride"},
        {"acid": "nitric acid", "acid_f": r"\text{HNO}_3", "carb": "sodium carbonate", "carb_f": r"\text{Na}_2\text{CO}_3", "salt_f": r"2\text{NaNO}_3", "salt_name": "sodium nitrate"},
        {"acid": "sulphuric acid", "acid_f": r"\text{H}_2\text{SO}_4", "carb": "magnesium carbonate", "carb_f": r"\text{MgCO}_3", "salt_f": r"\text{MgSO}_4", "salt_name": "magnesium sulphate"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"A laboratory demonstration investigates gas formation by reacting **{c['carb']}** (${c['carb_f']}$) "
        f"with dilute **{c['acid']}** (${c['acid_f']}$).\n\n"
        f"1. Write down a balanced chemical equation for this reaction. Include state symbols.\n"
        f"2. Name the salt formed in this reaction.\n"
        f"3. Explain why this reaction is classified as an **ion exchange reaction**.\n"
        f"4. What is the driving force that ensures this reaction goes to completion?"
    )

    if c["carb_f"] == r"\text{CaCO}_3":
        eq = r"\text{CaCO}_3(s) + 2\text{HCl}(aq) \to \text{CaCl}_2(aq) + \text{H}_2\text{O}(\ell) + \text{CO}_2(g)"
    elif c["carb_f"] == r"\text{Na}_2\text{CO}_3":
        eq = r"\text{Na}_2\text{CO}_3(s) + 2\text{HNO}_3(aq) \to 2\text{NaNO}_3(aq) + \text{H}_2\text{O}(\ell) + \text{CO}_2(g)"
    else:
        eq = r"\text{MgCO}_3(s) + \text{H}_2\text{SO}_4(aq) \to \text{MgSO}_4(aq) + \text{H}_2\text{O}(\ell) + \text{CO}_2(g)"

    ans_latex = rf"{eq}; \quad \text{{Salt: }}{c['salt_name']}; \quad \text{{Driving force: Gas formation (}}\text{{CO}}_2\text{{)}} \text{{ and water formation}}"

    sample_answer = (
        f"1. Balanced equation:\n"
        f"   $${eq}$$\n"
        f"2. Salt formed: **{c['salt_name']}**.\n"
        f"3. It is an ion exchange reaction because the metal cation and hydrogen ion exchange their anion partners (carbonate and acid anion).\n"
        f"4. Driving force: The **formation of a gas (CO₂)** that escapes from solution and the **formation of water (H₂O)** remove ions from the solution, driving the reaction to completion."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct balanced equation with state symbols: {eq}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Correct salt name: {c['salt_name']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Identification of gas formation (CO2) and water formation as driving forces", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Acid + Metal Carbonate -> Salt + Water + Carbon dioxide.",
        "concept": "Carbonate + Acid produces effervescence. Escaping CO₂ gas prevents the reverse reaction from occurring.",
        "breakdown": f"Balanced equation: {eq}. Salt is {c['salt_name']}. The driving force is the formation of CO₂(g) and H₂O(l).",
    }

    return make_science_question(
        prefix="ps10_aq_gas_carb",
        topic=TOPIC,
        subskill="31_gas_forming_reactions_carbonate_acid",
        learning_objective_id=f"{LO}_gas_carbonate",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["omitted_water_in_carbonate_acid_reaction", "unbalanced_acid_coefficient"],
        keywords=["gas forming reaction", "carbonate", "acid", "carbon dioxide", "effervescence"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 32: Gas-Forming Reactions — Hydrogen Carbonates
# --------------------------------------------------------------------------- #
def arch_32_gas_forming_reactions_hydrogen_carbonate(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    salt_name, formula, salt_res = rng.choice([
        ("sodium hydrogen carbonate", r"\text{NaHCO}_3", r"\text{NaCl}"),
        ("potassium hydrogen carbonate", r"\text{KHCO}_3", r"\text{KCl}"),
    ])

    prompt = (
        f"A laboratory sample of **{salt_name}** (${formula}$) is reacted with dilute hydrochloric acid ($\\text{{HCl}}$). "
        f"Vigorous fizzing occurs.\n\n"
        f"1. Write down the balanced chemical equation for the reaction of {salt_name} with hydrochloric acid. Include state symbols.\n"
        f"2. Explain why only $1\\text{{ mol}}$ of $\\text{{HCl}}$ is required per mole of ${formula}$, whereas $2\\text{{ mol}}$ of $\\text{{HCl}}$ are required per mole of the corresponding neutral carbonate.\n"
        f"3. Name the gas evolved and describe its observable effect on a burning wooden splint."
    )

    eq = rf"{formula}(s) + \text{{HCl}}(aq) \to {salt_res}(aq) + \text{{H}}_2\text{{O}}(\ell) + \text{{CO}}_2(g)"
    ans_latex = rf"{eq}; \quad \text{{Gas: }}\text{{CO}}_2(g)\text{{ extinguishes burning splint}}"

    sample_answer = (
        f"1. Balanced equation:\n"
        f"   $${eq}$$\n"
        f"2. Explanation:\n"
        f"   The hydrogen carbonate ion ($\\text{{HCO}}_3^-$) already contains one hydrogen atom. It requires only ONE additional $\\text{{H}}^+$ ion from $\\text{{HCl}}$ to form $\\text{{H}}_2\\text{{CO}}_3$ (which decomposes into $\\text{{H}}_2\\text{{O}}$ and $\\text{{CO}}_2$).\n"
        f"   In contrast, the carbonate ion ($\\text{{CO}}_3^{{2-}}$) has a charge of -2 and contains no hydrogen, requiring TWO $\\text{{H}}^+$ ions to form $\\text{{H}}_2\\text{{CO}}_3$.\n"
        f"3. Gas evolved: **Carbon dioxide** ($\\text{{CO}}_2$). It extinguishes a burning wooden splint because it does not support combustion."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct balanced equation with state symbols: {eq}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Explanation: HCO3- already has 1 H+, needing only 1 H+; CO3^2- needs 2 H+", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Gas named (CO2) and splint test: extinguishes flame", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Compare the formulas of HCO₃⁻ and CO₃²⁻.",
        "concept": "HCO₃⁻ + H⁺ -> H₂O + CO₂ (1:1 molar ratio).",
        "breakdown": f"Balanced equation: {eq}. 1 mole of HCl reacts with 1 mole of NaHCO₃. CO₂ extinguishes a flame.",
    }

    return make_science_question(
        prefix="ps10_aq_gas_hcarb",
        topic=TOPIC,
        subskill="32_gas_forming_reactions_hydrogen_carbonate",
        learning_objective_id=f"{LO}_gas_hcarbonate",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["used_2_moles_of_acid_for_nahco3", "confused_splint_pop_with_extinguishing"],
        keywords=["sodium hydrogen carbonate", "baking soda", "effervescence", "carbon dioxide", "splint test"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 33: Gas-Forming Reactions — Sulphites and Sulphides
# --------------------------------------------------------------------------- #
def arch_33_gas_forming_reactions_sulphite_and_sulphide(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    rxn_case = rng.choice([
        {
            "name": "sodium sulphite and hydrochloric acid",
            "reactants": r"\text{Na}_2\text{SO}_3(s) + 2\text{HCl}(aq)",
            "products": r"2\text{NaCl}(aq) + \text{H}_2\text{O}(\ell) + \text{SO}_2(g)",
            "gas": "sulphur dioxide (SO₂)",
            "gas_smell": "choking / pungent, suffocating smell of burning sulphur",
            "gas_test": "turns acidified potassium dichromate paper from orange to green",
        },
        {
            "name": "iron(II) sulphide and hydrochloric acid",
            "reactants": r"\text{FeS}(s) + 2\text{HCl}(aq)",
            "products": r"\text{FeCl}_2(aq) + \text{H}_2\text{S}(g)",
            "gas": "hydrogen sulphide (H₂S)",
            "gas_smell": "characteristic foul odour of rotten eggs",
            "gas_test": "turns moist lead(II) acetate paper black (due to PbS)",
        },
    ])

    prompt = (
        f"Consider the gas-forming reaction between **{rxn_case['name']}**.\n\n"
        f"1. Write down the balanced chemical symbol equation for this reaction. Include state symbols.\n"
        f"2. Name and write the formula of the gas evolved.\n"
        f"3. Describe the characteristic odour/smell of this gas.\n"
        f"4. State ONE chemical test to identify this gas."
    )

    eq = rf"{rxn_case['reactants']} \to {rxn_case['products']}"
    ans_latex = rf"{eq}; \quad \text{{Gas: }}{rxn_case['gas']}"

    sample_answer = (
        f"1. Balanced equation:\n"
        f"   $${eq}$$\n"
        f"2. Gas evolved: **{rxn_case['gas']}**.\n"
        f"3. Characteristic odour: **{rxn_case['gas_smell']}**.\n"
        f"4. Chemical identification test: {rxn_case['gas_test']}."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct balanced equation with state symbols: {eq}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Gas named and formula: {rxn_case['gas']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate odour description: {rxn_case['gas_smell']}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Sulphites release sulphur dioxide gas (SO₂); sulphides release hydrogen sulphide gas (H₂S).",
        "concept": "SO₃²⁻ + 2H⁺ -> H₂O + SO₂(g). S²⁻ + 2H⁺ -> H₂S(g).",
        "breakdown": f"Balanced equation: {eq}. Gas evolved: {rxn_case['gas']} ({rxn_case['gas_smell']}).",
    }

    return make_science_question(
        prefix="ps10_aq_gas_s_cpds",
        topic=TOPIC,
        subskill="33_gas_forming_reactions_sulphite_and_sulphide",
        learning_objective_id=f"{LO}_gas_sulphite_sulphide",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_sulphite_so2_with_sulphide_h2s", "omitted_water_in_sulphite_reaction"],
        keywords=["gas forming reaction", "sulphite", "sulphide", "sulphur dioxide", "hydrogen sulphide"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 34: Acid-Base Definitions — Arrhenius & Brønsted-Lowry
# --------------------------------------------------------------------------- #
def arch_34_acid_base_definitions_arrhenius_and_bronsted(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    example_case = rng.choice([
        {"sub": "ammonia gas (NH3)", "class": "Brønsted-Lowry base", "reason": "it accepts a proton from water to form NH4+, but does not contain OH- in its own formula"},
        {"sub": "hydrogen chloride gas (HCl)", "class": "both an Arrhenius and Brønsted-Lowry acid", "reason": "it donates a proton to water, producing H3O+ ions in aqueous solution"},
        {"sub": "potassium hydroxide (KOH)", "class": "both an Arrhenius and Brønsted-Lowry base", "reason": "it dissociates to release OH- ions which accept protons to form water"},
    ])

    prompt = (
        f"Acids and bases can be defined according to different models in chemistry.\n\n"
        f"1. Define an **acid** according to the **Arrhenius model**.\n"
        f"2. Define a **base** according to the **Arrhenius model**.\n"
        f"3. Define an **acid** according to the **Brønsted-Lowry model**.\n"
        f"4. Define a **base** according to the **Brønsted-Lowry model**.\n"
        f"5. Consider **{example_case['sub']}**: classify it according to these models and explain why ({example_case['reason']})."
    )

    ans_latex = (
        rf"\text{{Arrhenius: produces }}\text{{H}}^+\text{{ / }}\text{{OH}}^-; \quad "
        rf"\text{{Brønsted-Lowry: proton donor/acceptor; }} \quad {example_case['sub']} \text{{ is a }} {example_case['class']}"
    )

    sample_answer = (
        f"1. Arrhenius Acid: A substance that produces hydrogen ions ($\\text{{H}}^+$) or hydronium ions ($\\text{{H}}_3\\text{{O}}^+$) when dissolved in water.\n"
        f"2. Arrhenius Base: A substance that produces hydroxide ions ($\\text{{OH}}^-$) when dissolved in water.\n"
        f"3. Brønsted-Lowry Acid: A substance (molecule or ion) that donates a proton ($\\text{{H}}^+$ ion).\n"
        f"4. Brønsted-Lowry Base: A substance (molecule or ion) that accepts a proton ($\\text{{H}}^+$ ion).\n"
        f"5. Classification of {example_case['sub']}: It acts as a **{example_case['class']}** because {example_case['reason']}."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Arrhenius acid: produces H+ / H3O+ in water", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Arrhenius base: produces OH- in water", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Brønsted-Lowry acid: proton (H+) donor", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Brønsted-Lowry base: proton (H+) acceptor", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Explanation of why Brønsted-Lowry is broader (not limited to aqueous OH-)", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Arrhenius focuses on ions produced in water; Brønsted-Lowry focuses on proton transfer.",
        "concept": "Arrhenius = H⁺ and OH⁻ in water. Brønsted-Lowry = Proton donor and proton acceptor.",
        "breakdown": "State all 4 definitions and explain that Brønsted-Lowry explains reactions without OH⁻ (e.g. NH₃).",
    }

    return make_science_question(
        prefix="ps10_aq_ab_defs",
        topic=TOPIC,
        subskill="34_acid_base_definitions_arrhenius_and_bronsted",
        learning_objective_id=f"{LO}_ab_definitions",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["swapped_proton_donor_and_acceptor", "confused_arrhenius_and_bronsted_models"],
        keywords=["Arrhenius", "Brønsted-Lowry", "acid", "base", "proton donor", "proton acceptor"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 35: Acid-Base Proton Transfer Mechanism
# --------------------------------------------------------------------------- #
def arch_35_acid_base_proton_transfer_mechanism(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    acid_case = rng.choice([
        {"acid": r"\text{HCl}", "name": "hydrochloric acid", "base": r"\text{H}_2\text{O}", "conj_acid": r"\text{H}_3\text{O}^+", "conj_base": r"\text{Cl}^-"},
        {"acid": r"\text{HNO}_3", "name": "nitric acid", "base": r"\text{H}_2\text{O}", "conj_acid": r"\text{H}_3\text{O}^+", "conj_base": r"\text{NO}_3^-"},
        {"acid": r"\text{H}_2\text{O}", "name": "water", "base": r"\text{NH}_3", "conj_acid": r"\text{NH}_4^+", "conj_base": r"\text{OH}^-"},
    ])

    prompt = (
        f"Consider the reaction of **{acid_case['name']}** in aqueous medium:\n"
        f"$${acid_case['acid']} + {acid_case['base']} \\rightleftharpoons {acid_case['conj_acid']} + {acid_case['conj_base']}$$\n\n"
        f"1. Describe the microscopic **proton transfer** taking place in this reaction.\n"
        f"2. Identify the Brønsted-Lowry acid and Brønsted-Lowry base in the forward reaction.\n"
        f"3. Explain what a **hydronium ion** ($\\text{{H}}_3\\text{{O}}^+$) is and why bare protons ($\\text{{H}}^+$) do not exist freely in aqueous solution."
    )

    ans_latex = (
        rf"\text{{Acid: }}{acid_case['acid']}, \quad \text{{Base: }}{acid_case['base']}; \quad "
        rf"\text{{Proton transfer from }}{acid_case['acid']}\text{{ to }}{acid_case['base']}"
    )

    sample_answer = (
        f"1. A proton ($\\text{{H}}^+$ ion) is transferred from the acid (${acid_case['acid']}$) to the base (${acid_case['base']}$).\n"
        f"2. Forward reaction:\n"
        f"   - **Brønsted-Lowry acid**: ${acid_case['acid']}$ (proton donor).\n"
        f"   - **Brønsted-Lowry base**: ${acid_case['base']}$ (proton acceptor).\n"
        f"3. A hydronium ion ($\\text{{H}}_3\\text{{O}}^+$) is a water molecule bonded to a proton via a coordinate (dative) covalent bond. "
        f"A bare $\\text{{H}}^+$ is simply a bare atomic nucleus with an enormous charge density; it immediately associates with a lone pair on a polar water molecule."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Proton transferred from {acid_case['acid']} to {acid_case['base']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct acid identified: {acid_case['acid']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct base identified: {acid_case['base']}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Hydronium ion explained: bare H+ has immense charge density and binds to water lone pair", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Which species gives away H⁺, and which species receives it?",
        "concept": "Acid = proton donor; Base = proton acceptor. Free H⁺ ions cannot exist alone in water and bind to form H₃O⁺.",
        "breakdown": f"{acid_case['acid']} donates H⁺ to {acid_case['base']}. Hydronium is H₃O⁺.",
    }

    return make_science_question(
        prefix="ps10_aq_proton_trans",
        topic=TOPIC,
        subskill="35_acid_base_proton_transfer_mechanism",
        learning_objective_id=f"{LO}_proton_transfer",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["assumed_bare_h_plus_exists_in_water", "reversed_donor_acceptor_roles"],
        keywords=["proton transfer", "hydronium ion", "Brønsted-Lowry", "dative covalent bond", "acid-base"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 36: Acid-Hydroxide Neutralisation Equations
# --------------------------------------------------------------------------- #
def arch_36_acid_hydroxide_neutralisation_equations(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    reactions = [
        {"acid": "hydrochloric acid", "acid_f": r"\text{HCl}", "base": "sodium hydroxide", "base_f": r"\text{NaOH}", "eq": r"\text{HCl}(aq) + \text{NaOH}(aq) \to \text{NaCl}(aq) + \text{H}_2\text{O}(\ell)", "salt": "sodium chloride"},
        {"acid": "sulphuric acid", "acid_f": r"\text{H}_2\text{SO}_4", "base": "potassium hydroxide", "base_f": r"\text{KOH}", "eq": r"\text{H}_2\text{SO}_4(aq) + 2\text{KOH}(aq) \to \text{K}_2\text{SO}_4(aq) + 2\text{H}_2\text{O}(\ell)", "salt": "potassium sulphate"},
        {"acid": "nitric acid", "acid_f": r"\text{HNO}_3", "base": "calcium hydroxide", "base_f": r"\text{Ca(OH)}_2", "eq": r"2\text{HNO}_3(aq) + \text{Ca(OH)}_2(aq) \to \text{Ca(NO}_3)_2(aq) + 2\text{H}_2\text{O}(\ell)", "salt": "calcium nitrate"},
    ]
    r_item = rng.choice(reactions)

    prompt = (
        f"A neutralisation reaction takes place between aqueous **{r_item['acid']}** (${r_item['acid_f']}$) "
        f"and aqueous **{r_item['base']}** (${r_item['base_f']}$).\n\n"
        f"1. Write down a balanced chemical symbol equation for this neutralisation reaction. Include state symbols.\n"
        f"2. Name the salt produced.\n"
        f"3. State whether the reaction is exothermic or endothermic, and describe what happens to the temperature of the solution."
    )

    ans_latex = rf"{r_item['eq']}; \quad \text{{Salt: }}{r_item['salt']}; \quad \text{{Exothermic (temperature increases)}}"

    sample_answer = (
        f"1. Balanced chemical equation:\n"
        f"   $${r_item['eq']}$$\n"
        f"2. Salt produced: **{r_item['salt']}**.\n"
        f"3. The neutralisation reaction is **exothermic**; thermal energy is released and the temperature of the solution increases."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct balanced chemical equation with state symbols: {r_item['eq']}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Correct chemical name of salt: {r_item['salt']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Stated exothermic and temperature increases", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Acid + Metal Hydroxide -> Salt + Water.",
        "concept": "Neutralisation releases heat (exothermic). Ensure stoichiometric coefficients balance diprotic acids or dihydroxide bases.",
        "breakdown": f"Equation: {r_item['eq']}. Salt: {r_item['salt']}. Reaction is exothermic.",
    }

    return make_science_question(
        prefix="ps10_aq_neutral_eq",
        topic=TOPIC,
        subskill="36_acid_hydroxide_neutralisation_equations",
        learning_objective_id=f"{LO}_neutral_equations",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["unbalanced_acid_base_stoichiometry", "thought_neutralisation_was_endothermic"],
        keywords=["neutralisation", "acid", "hydroxide", "salt", "exothermic", "temperature change"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 37: Acid-Hydroxide Net Ionic Equation
# --------------------------------------------------------------------------- #
def arch_37_acid_hydroxide_net_ionic_equation(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    acid, base = rng.choice([
        (r"\text{HCl}(aq)", r"\text{NaOH}(aq)"),
        (r"\text{HNO}_3(aq)", r"\text{KOH}(aq)"),
        (r"\text{HCl}(aq)", r"\text{LiOH}(aq)"),
    ])

    prompt = (
        f"A strong monoprotic acid (${acid}$) neutralises a strong soluble metal hydroxide (${base}$).\n\n"
        f"1. Write down the full ionic equation for this reaction.\n"
        f"2. Identify the spectator ions.\n"
        f"3. Derive and write down a **net ionic equation** for the neutralisation reaction.\n"
        f"4. State why all strong acid-strong base neutralisation reactions yield an identical net ionic equation."
    )

    full_eq = r"\text{H}^+(aq) + \text{Cl}^-(aq) + \text{Na}^+(aq) + \text{OH}^-(aq) \to \text{Na}^+(aq) + \text{Cl}^-(aq) + \text{H}_2\text{O}(\ell)"
    net_eq = r"\text{H}^+(aq) + \text{OH}^-(aq) \to \text{H}_2\text{O}(\ell)"
    ans_latex = net_eq

    sample_answer = (
        f"1. Full ionic equation:\n"
        f"   $${full_eq}$$\n"
        f"2. Spectator ions: **Na⁺** and **Cl⁻** (or the corresponding metal cation and acid anion).\n"
        f"3. Net ionic equation:\n"
        f"   $${net_eq}$$\n"
        f"4. Explanation:\n"
        f"   All strong acids and strong bases dissociate/ionise completely in water. The spectator ions remain dissolved and unchanged; "
        f"the only actual chemical reaction occurring is the combination of hydrogen ions and hydroxide ions to form neutral water molecules."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Correct full ionic equation with state symbols", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct spectator ions identified", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct net ionic equation: {net_eq}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Explanation: all strong acid-base reactions reduce to H+ + OH- -> H2O", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Which ions remain dissolved on both sides? Cancel them out.",
        "concept": "Strong acid + strong base always reduces to H⁺(aq) + OH⁻(aq) -> H₂O(l).",
        "breakdown": f"Net ionic equation is {net_eq}. All strong acid-base neutralisations share this identical net equation.",
    }

    return make_science_question(
        prefix="ps10_aq_net_neutral",
        topic=TOPIC,
        subskill="37_acid_hydroxide_net_ionic_equation",
        learning_objective_id=f"{LO}_net_neutralisation",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["included_spectators_in_neutralisation_net_ionic", "wrote_water_as_dissociated"],
        keywords=["net ionic equation", "neutralisation", "spectator ions", "water formation", "strong acid"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 38: Acid-Metal Oxide Reactions
# --------------------------------------------------------------------------- #
def arch_38_acid_metal_oxide_reactions(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    oxide_case = rng.choice([
        {
            "name": "copper(II) oxide and sulphuric acid",
            "oxide": r"\text{CuO}(s)",
            "oxide_col": "black powder",
            "acid": r"\text{H}_2\text{SO}_4(aq)",
            "eq": r"\text{CuO}(s) + \text{H}_2\text{SO}_4(aq) \to \text{CuSO}_4(aq) + \text{H}_2\text{O}(\ell)",
            "salt": "copper(II) sulphate",
            "sol_col": "bright blue solution",
        },
        {
            "name": "magnesium oxide and hydrochloric acid",
            "oxide": r"\text{MgO}(s)",
            "oxide_col": "white powder",
            "acid": r"2\text{HCl}(aq)",
            "eq": r"\text{MgO}(s) + 2\text{HCl}(aq) \to \text{MgCl}_2(aq) + \text{H}_2\text{O}(\ell)",
            "salt": "magnesium chloride",
            "sol_col": "clear colourless solution",
        },
    ])

    prompt = (
        f"A learner adds solid **{oxide_case['oxide_col']}** (${oxide_case['oxide']}$) to warm dilute "
        f"${oxide_case['acid']}$.\n\n"
        f"1. Write down a balanced chemical equation for this reaction. Include state symbols.\n"
        f"2. Name the salt produced.\n"
        f"3. Describe the visible observations as the reaction proceeds.\n"
        f"4. Classify metal oxides as acidic, basic, or neutral."
    )

    ans_latex = rf"{oxide_case['eq']}; \quad \text{{Salt: }}{oxide_case['salt']}; \quad \text{{Basic metal oxide}}"

    sample_answer = (
        f"1. Balanced equation:\n"
        f"   $${oxide_case['eq']}$$\n"
        f"2. Salt produced: **{oxide_case['salt']}**.\n"
        f"3. Observations: The solid {oxide_case['oxide_col']} dissolves, forming a **{oxide_case['sol_col']}**.\n"
        f"4. Metal oxides are **basic oxides** (they react with acids to form salt and water, acting as chemical bases)."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct balanced equation with state symbols: {oxide_case['eq']}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Correct salt name: {oxide_case['salt']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate observations (dissolves to {oxide_case['sol_col']}) and classification as basic oxide", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Acid + Metal Oxide -> Salt + Water.",
        "concept": "Metal oxides are basic. Copper(II) oxide is black and dissolves to form a blue CuSO₄ solution.",
        "breakdown": f"Balanced equation: {oxide_case['eq']}. Salt: {oxide_case['salt']}. Metal oxides are basic.",
    }

    return make_science_question(
        prefix="ps10_aq_metal_oxide",
        topic=TOPIC,
        subskill="38_acid_metal_oxide_reactions",
        learning_objective_id=f"{LO}_metal_oxide",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["claimed_hydrogen_gas_is_formed_with_oxide", "confused_basic_and_acidic_oxides"],
        keywords=["metal oxide", "basic oxide", "copper oxide", "neutralisation", "acid"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 39: Acid-Metal Carbonate Neutralisation in Antacids
# --------------------------------------------------------------------------- #
def arch_39_acid_metal_carbonate_neutralisation(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    tablet_mass = round(rng.uniform(0.5, 1.2), 2)
    purity_pct = rng.choice([60, 75, 80, 85])

    prompt = (
        f"An antacid tablet with a mass of **{fmt_sa(tablet_mass)}\\text{{ g}}** contains calcium carbonate ($\\text{{CaCO}}_3$) "
        f"as the active medicinal ingredient. It neutralises excess hydrochloric acid ($\\text{{HCl}}$) in stomach acid.\n\n"
        f"1. Write down a balanced chemical equation for the neutralisation of hydrochloric acid by calcium carbonate.\n"
        f"2. Explain why antacids containing carbonates may cause burping / belching after consumption.\n"
        f"3. Name an alternative active base used in antacids (such as milk of magnesia) that neutralises stomach acid WITHOUT releasing gas."
    )

    eq = r"\text{CaCO}_3(s) + 2\text{HCl}(aq) \to \text{CaCl}_2(aq) + \text{H}_2\text{O}(\ell) + \text{CO}_2(g)"
    ans_latex = rf"{eq}; \quad \text{{Alternative: }}\text{{Mg(OH)}}_2\text{{ (magnesium hydroxide)}}"

    sample_answer = (
        f"1. Balanced chemical equation:\n"
        f"   $${eq}$$\n"
        f"2. Explanation:\n"
        f"   The reaction produces carbon dioxide gas ($\\text{{CO}}_2$). As the gas builds up pressure inside the stomach, "
        f"it is released upwards through the oesophagus, causing burping/belching.\n"
        f"3. Alternative base: **Magnesium hydroxide** ($\\text{{Mg(OH)}}_2$) or **aluminium hydroxide** ($\\text{{Al(OH)}}_3$). "
        f"These react to form salt and water only ($\\text{{Mg(OH)}}_2 + 2\\text{{HCl}} \\to \\text{{MgCl}}_2 + 2\\text{{H}}_2\\text{{O}}$) with zero gas production."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct balanced equation: {eq}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Reason for burping: production of carbon dioxide gas builds pressure", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Alternative base: magnesium hydroxide / aluminium hydroxide", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Which gas is produced when carbonates react with acid?",
        "concept": "CaCO₃ + 2HCl -> CaCl₂ + H₂O + CO₂(g). Hydroxide bases like Mg(OH)₂ do not produce gas.",
        "breakdown": f"Balanced equation: {eq}. CO₂ causes belching. Alternative antacid: Mg(OH)₂.",
    }

    return make_science_question(
        prefix="ps10_aq_antacid_chem",
        topic=TOPIC,
        subskill="39_acid_metal_carbonate_neutralisation",
        learning_objective_id=f"{LO}_antacid_neutralisation",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_carbonate_and_hydroxide_antacid_products", "unbalanced_calcium_carbonate_equation"],
        keywords=["antacid", "calcium carbonate", "neutralisation", "stomach acid", "magnesium hydroxide", "carbon dioxide"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 40: Redox Definition as Electron Transfer
# --------------------------------------------------------------------------- #
def arch_40_redox_definition_electron_transfer(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    example_half = rng.choice([
        {"eq": r"\text{Mg}(s) \to \text{Mg}^{2+}(aq) + 2e^-", "type": "oxidation", "desc": "loss of 2 electrons (oxidation state increases from 0 to +2)"},
        {"eq": r"\text{Cu}^{2+}(aq) + 2e^- \to \text{Cu}(s)", "type": "reduction", "desc": "gain of 2 electrons (oxidation state decreases from +2 to 0)"},
        {"eq": r"2\text{Cl}^-(aq) \to \text{Cl}_2(aq) + 2e^-", "type": "oxidation", "desc": "loss of 2 electrons (oxidation state increases from -1 to 0)"},
        {"eq": r"\text{Fe}^{3+}(aq) + e^- \to \text{Fe}^{2+}(aq)", "type": "reduction", "desc": "gain of 1 electron (oxidation state decreases from +3 to +2)"},
    ])

    prompt = (
        f"In aqueous chemistry, redox reactions form a fundamental class of chemical change.\n\n"
        f"1. What does the acronym **redox** stand for?\n"
        f"2. Define the term **oxidation** in terms of electron transfer.\n"
        f"3. Define the term **reduction** in terms of electron transfer.\n"
        f"4. State the mnemonic acronym commonly used by chemists to remember these definitions.\n"
        f"5. Consider the half-reaction $${example_half['eq']}$$.\n"
        f"   Classify this half-reaction as **oxidation** or **reduction** and justify by referring to electron transfer."
    )

    ans_latex = rf"\text{{Redox: Reduction-Oxidation; }} \quad {example_half['eq']} \text{{ is }} {example_half['type']}"

    sample_answer = (
        f"1. Redox stands for **reduction-oxidation**.\n"
        f"2. Oxidation is the **loss of electrons** by a chemical species.\n"
        f"3. Reduction is the **gain of electrons** by a chemical species.\n"
        f"4. Mnemonic: **OIL RIG** (Oxidation Is Loss, Reduction Is Gain).\n"
        f"5. The half-reaction $${example_half['eq']}$$ represents **{example_half['type']}** because it involves the {example_half['desc']}."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Redox = reduction-oxidation stated", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Oxidation defined as loss of electrons", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Reduction defined as gain of electrons", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Mnemonic OIL RIG stated", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Conservation of electrons: electrons lost by one must be gained by another", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Remember the mnemonic: OIL RIG.",
        "concept": "Oxidation Is Loss, Reduction Is Gain of electrons. Electrons are transferred directly from one species to another.",
        "breakdown": "Define oxidation (loss of e⁻), reduction (gain of e⁻), OIL RIG, and state that electron conservation requires simultaneous transfer.",
    }

    return make_science_question(
        prefix="ps10_aq_redox_def",
        topic=TOPIC,
        subskill="40_redox_definition_electron_transfer",
        learning_objective_id=f"{LO}_redox_definition",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["swapped_oxidation_and_reduction_electron_roles", "thought_electrons_can_float_freely"],
        keywords=["redox", "oxidation", "reduction", "electron transfer", "OIL RIG"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 41: Identifying Oxidation Numbers in Aqueous Ions
# --------------------------------------------------------------------------- #
def arch_41_identifying_oxidation_numbers_in_aqueous_ions(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    species = [
        {"formula": r"\text{Fe}^{3+}(aq)", "target": "Fe", "ox": "+3", "rule": "Monoatomic ion has oxidation number equal to its ionic charge"},
        {"formula": r"\text{SO}_4^{2-}(aq)", "target": "S", "ox": "+6", "rule": "Sum of oxidation states in polyatomic ion equals charge (-2): S + 4(-2) = -2 => S = +6"},
        {"formula": r"\text{NO}_3^-(aq)", "target": "N", "ox": "+5", "rule": "Sum of oxidation states equals -1: N + 3(-2) = -1 => N = +5"},
        {"formula": r"\text{MnO}_4^-(aq)", "target": "Mn", "ox": "+7", "rule": "Sum of oxidation states equals -1: Mn + 4(-2) = -1 => Mn = +7"},
        {"formula": r"\text{Cr}_2\text{O}_7^{2-}(aq)", "target": "Cr", "ox": "+6", "rule": "Sum of oxidation states equals -2: 2Cr + 7(-2) = -2 => 2Cr = +12 => Cr = +6"},
    ]
    sp = rng.choice(species)

    prompt = (
        f"Consider the aqueous ion **${sp['formula']}$**.\n\n"
        f"1. Determine the oxidation number of the **{sp['target']}** atom in this ion.\n"
        f"2. Show all working steps using the standard oxidation number rules (e.g. oxygen is usually $-2$ in compounds).\n"
        f"3. State the oxidation number of an uncombined neutral element (such as solid $\\text{{Fe}}(s)$ or gaseous $\\text{{O}}_2(g)$)."
    )

    ans_latex = rf"\text{{Oxidation number of }}{sp['target']} = {sp['ox']}; \quad \text{{Free element}} = 0"

    sample_answer = (
        f"1. The oxidation number of {sp['target']} in ${sp['formula']}$ is **{sp['ox']}**.\n"
        f"2. Working steps:\n"
        f"   - {sp['rule']}.\n"
        f"3. The oxidation number of any uncombined neutral element in its elemental form is always **0**."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct oxidation number for {sp['target']}: {sp['ox']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Correct mathematical working using oxygen as -2 and setting sum equal to ion charge", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Oxidation number of free uncombined element is 0", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "In a polyatomic ion, the sum of all oxidation numbers must equal the charge of the ion.",
        "concept": "Oxygen is -2. Multiply by the number of oxygen atoms, add the unknown atom's oxidation number, and set equal to the overall ionic charge.",
        "breakdown": f"For {sp['formula']}: {sp['rule']}. Final answer: {sp['ox']}.",
    }

    return make_science_question(
        prefix="ps10_aq_ox_numbers",
        topic=TOPIC,
        subskill="41_identifying_oxidation_numbers_in_aqueous_ions",
        learning_objective_id=f"{LO}_oxidation_numbers",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["set_polyatomic_ion_sum_to_zero", "omitted_sign_in_oxidation_number"],
        keywords=["oxidation number", "oxidation state", "polyatomic ion", "sulphate", "nitrate", "charge"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 42: Oxidising and Reducing Agents Identification
# --------------------------------------------------------------------------- #
def arch_42_oxidising_and_reducing_agents_identification(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    reactions = [
        {
            "eq": r"\text{Zn}(s) + \text{Cu}^{2+}(aq) \to \text{Zn}^{2+}(aq) + \text{Cu}(s)",
            "ox_agent": r"\text{Cu}^{2+}(aq)",
            "red_agent": r"\text{Zn}(s)",
            "ox_species": r"\text{Zn}(s)",
            "red_species": r"\text{Cu}^{2+}(aq)",
        },
        {
            "eq": r"\text{Mg}(s) + 2\text{H}^+(aq) \to \text{Mg}^{2+}(aq) + \text{H}_2(g)",
            "ox_agent": r"\text{H}^+(aq)",
            "red_agent": r"\text{Mg}(s)",
            "ox_species": r"\text{Mg}(s)",
            "red_species": r"\text{H}^+(aq)",
        },
        {
            "eq": r"\text{Cl}_2(aq) + 2\text{Br}^-(aq) \to 2\text{Cl}^-(aq) + \text{Br}_2(aq)",
            "ox_agent": r"\text{Cl}_2(aq)",
            "red_agent": r"\text{Br}^-(aq)",
            "ox_species": r"\text{Br}^-(aq)",
            "red_species": r"\text{Cl}_2(aq)",
        },
    ]
    r_item = rng.choice(reactions)

    prompt = (
        f"Consider the aqueous redox reaction:\n"
        f"$${r_item['eq']}$$\n\n"
        f"1. Define the term **oxidising agent** in terms of electron transfer.\n"
        f"2. Define the term **reducing agent** in terms of electron transfer.\n"
        f"3. From the equation above, identify:\n"
        f"   - The species that is **oxidised**\n"
        f"   - The species that is **reduced**\n"
        f"   - The **oxidising agent**\n"
        f"   - The **reducing agent**"
    )

    ans_latex = (
        rf"\text{{Oxidised: }}{r_item['ox_species']}; \quad \text{{Reduced: }}{r_item['red_species']}; \quad "
        rf"\text{{Oxidising Agent: }}{r_item['ox_agent']}; \quad \text{{Reducing Agent: }}{r_item['red_agent']}"
    )

    sample_answer = (
        f"1. An oxidising agent is a substance that accepts electrons (causes another substance to be oxidised while it undergoes reduction itself).\n"
        f"2. A reducing agent is a substance that donates electrons (causes another substance to be reduced while it undergoes oxidation itself).\n"
        f"3. Identification:\n"
        f"   - Species oxidised: **${r_item['ox_species']}$** (loses electrons; oxidation state increases).\n"
        f"   - Species reduced: **${r_item['red_species']}$** (gains electrons; oxidation state decreases).\n"
        f"   - Oxidising agent: **${r_item['ox_agent']}$**.\n"
        f"   - Reducing agent: **${r_item['red_agent']}$**."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Oxidising agent defined as electron acceptor / undergoes reduction", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Reducing agent defined as electron donor / undergoes oxidation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct species oxidised: {r_item['ox_species']}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct species reduced: {r_item['red_species']}", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Correct agents: Oxidising = {r_item['ox_agent']}, Reducing = {r_item['red_agent']}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "The substance that is oxidised acts as the reducing agent; the substance that is reduced acts as the oxidising agent.",
        "concept": "Oxidation = loses electrons -> reducing agent. Reduction = gains electrons -> oxidising agent.",
        "breakdown": f"{r_item['ox_species']} loses e⁻ (oxidised, reducing agent). {r_item['red_species']} gains e⁻ (reduced, oxidising agent).",
    }

    return make_science_question(
        prefix="ps10_aq_agents_redox",
        topic=TOPIC,
        subskill="42_oxidising_and_reducing_agents_identification",
        learning_objective_id=f"{LO}_redox_agents",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["swapped_oxidising_and_reducing_agents", "confused_species_oxidised_with_oxidising_agent"],
        keywords=["oxidising agent", "reducing agent", "electron transfer", "oxidation", "reduction"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 43: Metal Displacement Redox Reactions
# --------------------------------------------------------------------------- #
def arch_43_metal_displacement_redox_reactions(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    system = rng.choice([
        {"metal": "zinc", "metal_s": r"\text{Zn}", "ion": r"\text{Zn}^{2+}", "salt": "copper(II) sulphate", "salt_f": r"\text{CuSO}_4", "disp_metal": "copper", "disp_s": r"\text{Cu}", "disp_ion": r"\text{Cu}^{2+}", "color": "blue", "dep_color": "reddish-brown"},
        {"metal": "magnesium", "metal_s": r"\text{Mg}", "ion": r"\text{Mg}^{2+}", "salt": "copper(II) chloride", "salt_f": r"\text{CuCl}_2", "disp_metal": "copper", "disp_s": r"\text{Cu}", "disp_ion": r"\text{Cu}^{2+}", "color": "blue-green", "dep_color": "reddish-brown"},
        {"metal": "iron", "metal_s": r"\text{Fe}", "ion": r"\text{Fe}^{2+}", "salt": "copper(II) sulphate", "salt_f": r"\text{CuSO}_4", "disp_metal": "copper", "disp_s": r"\text{Cu}", "disp_ion": r"\text{Cu}^{2+}", "color": "blue", "dep_color": "reddish-brown"},
    ])

    prompt = (
        f"A strip of shiny {system['metal']} metal (${system['metal_s']}$) is placed into a beaker containing a {system['color']} aqueous solution "
        f"of {system['salt']} (${system['salt_f']}$). After several minutes, a {system['dep_color']} coating forms on the {system['metal']}, "
        f"and the {system['color']} colour of the solution fades.\n\n"
        f"1. Write down the oxidation half-reaction.\n"
        f"2. Write down the reduction half-reaction.\n"
        f"3. Write down an overall balanced net ionic equation.\n"
        f"4. Explain the observable changes: why does the solution fade and why does a {system['dep_color']} solid deposit?"
    )

    ox_half = rf"{system['metal_s']}(s) \to {system['ion']}(aq) + 2e^-"
    red_half = rf"{system['disp_ion']}(aq) + 2e^- \to {system['disp_s']}(s)"
    net_eq = rf"{system['metal_s']}(s) + {system['disp_ion']}(aq) \to {system['ion']}(aq) + {system['disp_s']}(s)"

    ans_latex = rf"\text{{Net: }}{net_eq}"

    sample_answer = (
        f"1. Oxidation half-reaction:\n"
        f"   $${ox_half}$$\n"
        f"2. Reduction half-reaction:\n"
        f"   $${red_half}$$\n"
        f"3. Overall net ionic equation:\n"
        f"   $${net_eq}$$\n"
        f"4. Explanation of observations:\n"
        f"   - The {system['color']} colour fades because {system['disp_metal']} ions (${system['disp_ion']}$), which give the solution its colour, are consumed as they are reduced to metallic {system['disp_metal']}.\n"
        f"   - The {system['dep_color']} solid deposit is pure {system['disp_metal']} metal (${system['disp_s']}(s)$) depositing onto the {system['metal']} strip."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct oxidation half-reaction: {ox_half}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct reduction half-reaction: {red_half}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct overall net ionic equation: {net_eq}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Reason for {system['color']} fading: {system['disp_ion']} ions consumed", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Reason for {system['dep_color']} solid: {system['disp_s']} metal deposits", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": f"{system['metal'].capitalize()} is more reactive than {system['disp_metal']}. {system['metal'].capitalize()} loses electrons to {system['disp_metal']} ions.",
        "concept": "More reactive metal oxidises (loses electrons). Less reactive metal cation reduces (gains electrons).",
        "breakdown": f"Write both half-reactions, combine for net ionic equation {net_eq}.",
    }

    return make_science_question(
        prefix="ps10_aq_metal_disp",
        topic=TOPIC,
        subskill="43_metal_displacement_redox_reactions",
        learning_objective_id=f"{LO}_metal_displacement",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["reversed_metal_reactivity_roles", "omitted_electrons_in_half_reactions"],
        keywords=["metal displacement", "redox", "zinc", "copper sulphate", "half reactions"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 44: Halogen Displacement Redox Reactions
# --------------------------------------------------------------------------- #
def arch_44_halogen_displacement_redox_reactions(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    halogen_sys = rng.choice([
        {"added": "chlorine water", "added_f": r"\text{Cl}_2(aq)", "salt": "potassium iodide", "salt_f": r"\text{KI}(aq)", "anion": r"\text{I}^-", "prod": r"\text{I}_2", "col": "dark brown / purple", "red_half": r"\text{Cl}_2(aq) + 2e^- \to 2\text{Cl}^-(aq)", "ox_half": r"2\text{I}^-(aq) \to \text{I}_2(aq) + 2e^-", "net": r"\text{Cl}_2(aq) + 2\text{I}^-(aq) \to 2\text{Cl}^-(aq) + \text{I}_2(aq)", "stronger": "chlorine", "weaker": "iodine"},
        {"added": "chlorine water", "added_f": r"\text{Cl}_2(aq)", "salt": "potassium bromide", "salt_f": r"\text{KBr}(aq)", "anion": r"\text{Br}^-", "prod": r"\text{Br}_2", "col": "reddish-orange / yellow-orange", "red_half": r"\text{Cl}_2(aq) + 2e^- \to 2\text{Cl}^-(aq)", "ox_half": r"2\text{Br}^-(aq) \to \text{Br}_2(aq) + 2e^-", "net": r"\text{Cl}_2(aq) + 2\text{Br}^-(aq) \to 2\text{Cl}^-(aq) + \text{Br}_2(aq)", "stronger": "chlorine", "weaker": "bromine"},
        {"added": "bromine water", "added_f": r"\text{Br}_2(aq)", "salt": "sodium iodide", "salt_f": r"\text{NaI}(aq)", "anion": r"\text{I}^-", "prod": r"\text{I}_2", "col": "dark brown / purple", "red_half": r"\text{Br}_2(aq) + 2e^- \to 2\text{Br}^-(aq)", "ox_half": r"2\text{I}^-(aq) \to \text{I}_2(aq) + 2e^-", "net": r"\text{Br}_2(aq) + 2\text{I}^-(aq) \to 2\text{Br}^-(aq) + \text{I}_2(aq)", "stronger": "bromine", "weaker": "iodine"},
    ])

    prompt = (
        f"A learner adds **{halogen_sys['added']}** (${halogen_sys['added_f']}$) to a colourless solution of "
        f"**{halogen_sys['salt']}** (${halogen_sys['salt_f']}$).\n"
        f"The mixture turns {halogen_sys['col']} immediately due to the liberation of elemental ${halogen_sys['prod']}$.\n\n"
        f"1. Write down the oxidation half-reaction.\n"
        f"2. Write down the reduction half-reaction.\n"
        f"3. Write down a balanced overall net ionic equation.\n"
        f"4. State which halogen is more reactive (a stronger oxidising agent): {halogen_sys['stronger']} or {halogen_sys['weaker']}? "
        f"Explain by referring to Group 17 periodic trends."
    )

    ans_latex = rf"\text{{Net: }}{halogen_sys['net']}; \quad \text{{{halogen_sys['stronger'].capitalize()} is a stronger oxidising agent than {halogen_sys['weaker']}}}"

    sample_answer = (
        f"1. Oxidation half-reaction:\n"
        f"   $${halogen_sys['ox_half']}$$\n"
        f"2. Reduction half-reaction:\n"
        f"   $${halogen_sys['red_half']}$$\n"
        f"3. Overall net ionic equation:\n"
        f"   $${halogen_sys['net']}$$\n"
        f"4. {halogen_sys['stronger'].capitalize()} is the **stronger oxidising agent** (more reactive non-metal).\n"
        f"   Explanation: {halogen_sys['stronger'].capitalize()} is higher up Group 17, having a smaller atomic radius and higher electronegativity than {halogen_sys['weaker']}. "
        f"Consequently, {halogen_sys['stronger']} has a stronger attraction for electrons and pulls electrons away from {halogen_sys['weaker']} ions."
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct oxidation half-reaction: {halogen_sys['ox_half']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct reduction half-reaction: {halogen_sys['red_half']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct overall net ionic equation: {halogen_sys['net']}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Stated {halogen_sys['stronger']} is stronger oxidising agent", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Reason: smaller atomic radius / higher electronegativity attracts electrons more strongly", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": f"{halogen_sys['stronger'].capitalize()} gains electrons to become anions; {halogen_sys['weaker']} ions lose electrons.",
        "concept": "Reactivity of halogens decreases down Group 17. Higher halogens displace lower halide ions.",
        "breakdown": f"Half-reactions: {halogen_sys['ox_half']} and {halogen_sys['red_half']}. Net: {halogen_sys['net']}.",
    }

    return make_science_question(
        prefix="ps10_aq_hal_disp",
        topic=TOPIC,
        subskill="44_halogen_displacement_redox_reactions",
        learning_objective_id=f"{LO}_halogen_displacement",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["wrote_single_atom_i_instead_of_diatomic_i2", "swapped_oxidised_and_reduced_halogens"],
        keywords=["halogen displacement", "chlorine", "iodine", "redox", "electronegativity", "Group 17"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 45: Metal-Acid Redox Reactions
# --------------------------------------------------------------------------- #
def arch_45_metal_acid_redox_reactions(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    metal_case = rng.choice([
        {"metal": "magnesium", "sym": r"\text{Mg}", "ion": r"\text{Mg}^{2+}", "charge": 2},
        {"metal": "zinc", "sym": r"\text{Zn}", "ion": r"\text{Zn}^{2+}", "charge": 2},
        {"metal": "iron", "sym": r"\text{Fe}", "ion": r"\text{Fe}^{2+}", "charge": 2},
    ])

    prompt = (
        f"A piece of **{metal_case['metal']} ribbon** (${metal_case['sym']}$) is dropped into a test tube of "
        f"dilute hydrochloric acid ($\\text{{HCl}}$). Rapid effervescence occurs as hydrogen gas ($\\text{{H}}_2$) is released.\n\n"
        f"1. Write down the balanced full molecular equation for this reaction.\n"
        f"2. Write down the oxidation half-reaction.\n"
        f"3. Write down the reduction half-reaction.\n"
        f"4. State the test used to confirm the presence of the hydrogen gas produced."
    )

    mol_eq = rf"{metal_case['sym']}(s) + 2\text{{HCl}}(aq) \to {metal_case['sym']}\text{{Cl}}_2(aq) + \text{{H}}_2(g)"
    ox_half = rf"{metal_case['sym']}(s) \to {metal_case['ion']}(aq) + 2e^-"
    red_half = r"2\text{H}^+(aq) + 2e^- \to \text{H}_2(g)"

    ans_latex = rf"{mol_eq}; \quad \text{{Test: Burning wooden splint gives a 'squeaky pop' sound}}"

    sample_answer = (
        f"1. Molecular equation:\n"
        f"   $${mol_eq}$$\n"
        f"2. Oxidation half-reaction:\n"
        f"   $${ox_half}$$\n"
        f"3. Reduction half-reaction:\n"
        f"   $${red_half}$$\n"
        f"4. Hydrogen test: Bring a **burning wooden splint** to the mouth of the test tube. The gas ignites with a characteristic **'squeaky pop' sound**."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct balanced molecular equation: {mol_eq}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct oxidation half-reaction: {ox_half}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct reduction half-reaction: {red_half}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Hydrogen gas test: burning splint produces squeaky pop sound", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Metal + Acid -> Salt + Hydrogen gas.",
        "concept": "Active metal loses electrons (oxidised). H⁺ ions gain electrons (reduced). Hydrogen gas pops with a flame.",
        "breakdown": f"Balanced: {mol_eq}. Half reactions: {ox_half} and {red_half}. Squeaky pop test confirms H₂.",
    }

    return make_science_question(
        prefix="ps10_aq_metal_acid",
        topic=TOPIC,
        subskill="45_metal_acid_redox_reactions",
        learning_objective_id=f"{LO}_metal_acid",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["claimed_chlorine_gas_is_formed", "omitted_charges_in_half_reaction"],
        keywords=["metal acid reaction", "hydrogen gas", "squeaky pop", "oxidation", "reduction", "half reactions"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 46: Distinguishing Ion Exchange from Redox
# --------------------------------------------------------------------------- #
def arch_46_distinguishing_ion_exchange_from_redox(rng: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    pairs = [
        {
            "rxn1": r"\text{AgNO}_3(aq) + \text{NaCl}(aq) \to \text{AgCl}(s) + \text{NaNO}_3(aq)",
            "type1": "Ion exchange (Precipitation)",
            "reason1": "All oxidation numbers remain unchanged (Ag: +1, Cl: -1, Na: +1, N: +5, O: -2)",
            "rxn2": r"\text{Zn}(s) + 2\text{HCl}(aq) \to \text{ZnCl}_2(aq) + \text{H}_2(g)",
            "type2": "Redox (Electron transfer)",
            "reason2": "Oxidation numbers change: Zn goes from 0 to +2 (oxidised), H goes from +1 to 0 (reduced)",
        },
        {
            "rxn1": r"\text{HCl}(aq) + \text{NaOH}(aq) \to \text{NaCl}(aq) + \text{H}_2\text{O}(\ell)",
            "type1": "Ion exchange (Neutralisation)",
            "reason1": "All oxidation numbers remain unchanged (H: +1, Cl: -1, Na: +1, O: -2)",
            "rxn2": r"\text{Cl}_2(aq) + 2\text{KBr}(aq) \to 2\text{KCl}(aq) + \text{Br}_2(aq)",
            "type2": "Redox (Electron transfer)",
            "reason2": "Oxidation numbers change: Cl goes from 0 to -1 (reduced), Br goes from -1 to 0 (oxidised)",
        },
    ]
    p = rng.choice(pairs)

    prompt = (
        f"Consider the two chemical reactions below:\n\n"
        f"- **Reaction 1**: $${p['rxn1']}$$\n"
        f"- **Reaction 2**: $${p['rxn2']}$$\n\n"
        f"1. Classify **Reaction 1** as either an **ion exchange reaction** or a **redox reaction**.\n"
        f"2. Classify **Reaction 2** as either an **ion exchange reaction** or a **redox reaction**.\n"
        f"3. Explain how a chemist uses **oxidation numbers** to determine whether a reaction is a redox reaction or an ion exchange reaction."
    )

    ans_latex = rf"\text{{Reaction 1: }}{p['type1']}; \quad \text{{Reaction 2: }}{p['type2']}"

    sample_answer = (
        f"1. Reaction 1 is an **{p['type1']}** ({p['reason1']}).\n"
        f"2. Reaction 2 is a **{p['type2']}** ({p['reason2']}).\n"
        f"3. Explanation:\n"
        f"   - In an **ion exchange reaction**, ions merely swap partners; the oxidation state of every element remains constant before and after the reaction.\n"
        f"   - In a **redox reaction**, electrons are transferred between species; at least one element increases in oxidation number (oxidation) while another decreases in oxidation number (reduction)."
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Reaction 1 classified correctly: {p['type1']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Reaction 2 classified correctly: {p['type2']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Criterion: ion exchange has zero change in oxidation numbers", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Criterion: redox involves changes in oxidation numbers due to electron transfer", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Check if any oxidation numbers change from reactants to products.",
        "concept": "If oxidation states change, it is redox. If oxidation states stay identical throughout, it is ion exchange.",
        "breakdown": f"Reaction 1: {p['type1']} (no ox state change). Reaction 2: {p['type2']} (ox states change).",
    }

    return make_science_question(
        prefix="ps10_aq_dist_ix_redox",
        topic=TOPIC,
        subskill="46_distinguishing_ion_exchange_from_redox",
        learning_objective_id=f"{LO}_dist_ix_redox",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["assumed_all_reactions_in_water_are_redox", "confused_charge_swap_with_electron_transfer"],
        keywords=["ion exchange", "redox", "oxidation numbers", "precipitation", "electron transfer"],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        mode="compound",
        difficulty=difficulty,
        marks=4,
    )


# --------------------------------------------------------------------------- #
# Subskill 47: Stoichiometry — Precipitation Mass Calculation
# --------------------------------------------------------------------------- #
def arch_47_stoichiometry_precipitation_mass_calculation(rng: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    vol_cm3 = rng.choice([50, 100, 150, 200, 250])
    conc = round(rng.uniform(0.1, 0.4), 2)
    # BaCl2(aq) + Na2SO4(aq) -> BaSO4(s) + 2NaCl(aq)
    # Molar mass of BaSO4 = 137.33 + 32.06 + 4(16.00) = 233.39 g/mol
    m_baso4 = 233.39
    vol_dm3 = vol_cm3 / 1000.0
    moles = round(conc * vol_dm3, 4)
    mass_ppt = round(moles * m_baso4, 2)

    prompt = (
        f"A learner mixes **{vol_cm3}\\text{{ cm}}^3** of a **${fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** "
        f"barium chloride solution ($\\text{{BaCl}}_2$) with excess sodium sulphate solution ($\\text{{Na}}_2\\text{{SO}}_4$).\n\n"
        f"1. Write down the balanced chemical equation for the precipitation reaction.\n"
        f"2. Calculate the number of moles of $\\text{{BaCl}}_2$ present in the initial solution.\n"
        f"3. Calculate the maximum theoretical mass of dry barium sulphate precipitate ($\\text{{BaSO}}_4$) that can be formed.\n"
        f"   *(Molar masses: $\\text{{Ba}} = 137{{,}}3\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, "
        f"$\\text{{S}} = 32{{,}}1\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, $\\text{{O}} = 16{{,}}0\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)*"
    )

    ans_latex = (
        rf"n(\text{{BaCl}}_2) = {fmt_sa(moles)}\text{{ mol}}; \quad "
        rf"m(\text{{BaSO}}_4) = {fmt_sa(mass_ppt)}\text{{ g}}"
    )

    sample_answer = (
        f"1. Balanced equation:\n"
        f"   $$\\text{{BaCl}}_2(aq) + \\text{{Na}}_2\\text{{SO}}_4(aq) \\to \\text{{BaSO}}_4(s) + 2\\text{{NaCl}}(aq)$$\n"
        f"2. Moles of BaCl₂:\n"
        f"   $$V = \\frac{{{vol_cm3}}}{{1000}} = {fmt_sa(vol_dm3)}\\text{{ dm}}^3$$\n"
        f"   $$n = c \\times V = {fmt_sa(conc)} \\times {fmt_sa(vol_dm3)} = {fmt_sa(moles)}\\text{{ mol}}$$\n"
        f"3. Mass of BaSO₄ precipitate:\n"
        f"   - Molar ratio: $n(\\text{{BaSO}}_4) = n(\\text{{BaCl}}_2) = {fmt_sa(moles)}\\text{{ mol}}$\n"
        f"   - Molar mass $M(\\text{{BaSO}}_4) = 137{{,}}3 + 32{{,}}1 + 4(16{{,}}0) = 233{{,}}4\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$\n"
        f"   - Mass $m = n \\times M = {fmt_sa(moles)} \\times 233{{,}}4 = {fmt_sa(mass_ppt)}\\text{{ g}}$"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Correct balanced chemical equation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Conversion of volume to dm³: {fmt_sa(vol_dm3)} dm³", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct moles of BaCl2 calculated: {fmt_sa(moles)} mol", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Molar mass of BaSO4 calculated (233,4 g/mol)", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Final mass of BaSO4 precipitate: {fmt_sa(mass_ppt)} g", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "omitted_volume_conversion_to_dm3", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Convert cm³ to dm³ by dividing by 1000 before using n = c × V.",
        "concept": "1 mole of BaCl₂ yields 1 mole of BaSO₄. Mass = n × M.",
        "breakdown": f"n = {fmt_sa(conc)} × {fmt_sa(vol_dm3)} = {fmt_sa(moles)} mol. Mass = {fmt_sa(moles)} × 233,4 = {fmt_sa(mass_ppt)} g.",
    }

    return make_science_question(
        prefix="ps10_aq_stoich_ppt",
        topic=TOPIC,
        subskill="47_stoichiometry_precipitation_mass_calculation",
        learning_objective_id=f"{LO}_stoich_precipitation",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["failed_cm3_to_dm3_conversion", "incorrect_molar_mass_calculation"],
        keywords=["stoichiometry", "precipitation mass", "barium sulphate", "concentration", "molar mass"],
        term=3,
        caps_weight_percent=25,
        suggested_duration_mins=6,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 48: Stoichiometry — Limiting Reagent in Precipitation
# --------------------------------------------------------------------------- #
def arch_48_stoichiometry_limiting_reagent_in_precipitation(rng: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    vol_pb = rng.choice([80, 100, 120])  # cm3
    c_pb = round(rng.uniform(0.15, 0.25), 2)   # mol/dm3
    vol_ki = rng.choice([140, 160, 180])  # cm3
    c_ki = round(rng.uniform(0.16, 0.24), 2)   # mol/dm3

    vol_pb_dm3 = vol_pb / 1000.0
    vol_ki_dm3 = vol_ki / 1000.0
    n_pb = round(c_pb * vol_pb_dm3, 4)
    n_ki = round(c_ki * vol_ki_dm3, 4)

    n_ki_needed = round(2.0 * n_pb, 4)
    if n_ki < n_ki_needed:
        limiting = "KI"
        limiting_name = "potassium iodide (KI)"
        n_pbi2 = round(n_ki / 2.0, 4)
    else:
        limiting = r"\text{Pb(NO}_3)_2"
        limiting_name = "lead(II) nitrate (Pb(NO3)2)"
        n_pbi2 = n_pb

    m_pbi2 = 461.0
    mass_pbi2 = round(n_pbi2 * m_pbi2, 2)

    prompt = (
        f"A learner mixes **{vol_pb}\\text{{ cm}}^3** of **${fmt_sa(c_pb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** "
        f"lead(II) nitrate solution ($\\text{{Pb(NO}}_3)_2$) with **{vol_ki}\\text{{ cm}}^3** of "
        f"**${fmt_sa(c_ki)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** potassium iodide solution ($\\text{{KI}}$).\n"
        f"A bright yellow precipitate of lead(II) iodide ($\\text{{PbI}}_2$) forms.\n\n"
        f"1. Write down the balanced chemical equation for the precipitation reaction.\n"
        f"2. Calculate the initial number of moles of $\\text{{Pb(NO}}_3)_2$ and $\\text{{KI}}$.\n"
        f"3. Identify the **limiting reactant**, showing all relevant stoichiometric calculations.\n"
        f"4. Calculate the mass of dry $\\text{{PbI}}_2$ precipitate formed.\n"
        f"   *(Molar masses: $\\text{{Pb}} = 207{{,}}2\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, $\\text{{I}} = 126{{,}}9\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)*"
    )

    ans_latex = (
        rf"\text{{Limiting Reactant: }}{limiting}; \quad "
        rf"n(\text{{PbI}}_2) = {fmt_sa(n_pbi2)}\text{{ mol}}; \quad "
        rf"m(\text{{PbI}}_2) = {fmt_sa(mass_pbi2)}\text{{ g}}"
    )

    sample_answer = (
        f"1. Balanced equation:\n"
        f"   $$\\text{{Pb(NO}}_3)_2(aq) + 2\\text{{KI}}(aq) \\to \\text{{PbI}}_2(s) + 2\\text{{KNO}}_3(aq)$$\n"
        f"2. Initial moles:\n"
        f"   - $n(\\text{{Pb(NO}}_3)_2) = c \\times V = {fmt_sa(c_pb)} \\times {fmt_sa(vol_pb_dm3)} = {fmt_sa(n_pb)}\\text{{ mol}}$\n"
        f"   - $n(\\text{{KI}}) = c \\times V = {fmt_sa(c_ki)} \\times {fmt_sa(vol_ki_dm3)} = {fmt_sa(n_ki)}\\text{{ mol}}$\n"
        f"3. Limiting Reactant determination:\n"
        f"   - From stoichiometry, $1\\text{{ mol of Pb(NO}}_3)_2$ requires $2\\text{{ mol of KI}}$.\n"
        f"   - For ${fmt_sa(n_pb)}\\text{{ mol of Pb(NO}}_3)_2$, we require $2 \\times {fmt_sa(n_pb)} = {fmt_sa(n_ki_needed)}\\text{{ mol of KI}}$.\n"
        f"   - Comparing available KI (${fmt_sa(n_ki)}\\text{{ mol}}$) to required KI (${fmt_sa(n_ki_needed)}\\text{{ mol}}$), "
        f"**{limiting_name} is the limiting reactant**.\n"
        f"4. Mass of PbI₂ precipitate:\n"
        f"   - $n(\\text{{PbI}}_2) = {fmt_sa(n_pbi2)}\\text{{ mol}}$\n"
        f"   - $M(\\text{{PbI}}_2) = 207{{,}}2 + 2(126{{,}}9) = 461{{,}}0\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$\n"
        f"   - $m = n \\times M = {fmt_sa(n_pbi2)} \\times 461{{,}}0 = {fmt_sa(mass_pbi2)}\\text{{ g}}$"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Correct balanced chemical equation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct initial moles: Pb(NO3)2 = {fmt_sa(n_pb)} mol and KI = {fmt_sa(n_ki)} mol", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Correct stoichiometric comparison identifying KI as limiting reactant", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct moles of precipitate: {fmt_sa(n_pbi2)} mol", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Final mass of PbI2 precipitate: {fmt_sa(mass_pbi2)} g", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Compare the moles of KI needed (2 × n(Pb(NO₃)₂)) to the actual moles of KI available.",
        "concept": "The reactant that runs out first limits the amount of product that can form.",
        "breakdown": f"KI produces only {fmt_sa(n_pbi2)} mol of PbI₂. Mass = {fmt_sa(n_pbi2)} × 461,0 = {fmt_sa(mass_pbi2)} g.",
    }

    return make_science_question(
        prefix="ps10_aq_limiting_ppt",
        topic=TOPIC,
        subskill="48_stoichiometry_limiting_reagent_in_precipitation",
        learning_objective_id=f"{LO}_limiting_reagent",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["identified_larger_volume_as_excess_without_moles", "forgot_1_to_2_mole_ratio"],
        keywords=["limiting reactant", "lead iodide", "precipitation", "stoichiometry", "excess reagent"],
        term=3,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode="compound",
        difficulty=difficulty,
        marks=6,
    )


# --------------------------------------------------------------------------- #
# Subskill 49: Stoichiometry — Antacid Tablet Gas Volume at STP
# --------------------------------------------------------------------------- #
def arch_49_stoichiometry_antacid_tablet_gas_volume(rng: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    tablet_mass = round(rng.uniform(0.40, 0.80), 2)
    vol_co2_cm3 = rng.choice([80, 95, 112, 125, 140])
    vol_co2_dm3 = vol_co2_cm3 / 1000.0
    vm = 22.4  # dm3/mol at STP
    n_co2 = round(vol_co2_dm3 / vm, 5)
    # Molar mass of CaCO3 = 40.08 + 12.01 + 3(16.00) = 100.09 g/mol
    m_caco3_molar = 100.09
    mass_caco3 = round(n_co2 * m_caco3_molar, 3)
    purity = round((mass_caco3 / tablet_mass) * 100.0, 1)

    prompt = (
        f"An antacid tablet with a total mass of **{fmt_sa(tablet_mass)}\\text{{ g}}** is crushed and reacted with excess "
        f"dilute hydrochloric acid ($\\text{{HCl}}$).\n"
        f"The carbon dioxide gas ($\\text{{CO}}_2$) evolved is collected and measured to be "
        f"**{vol_co2_cm3}\\text{{ cm}}^3** at standard temperature and pressure (STP).\n\n"
        f"1. Write down the balanced chemical equation for the reaction.\n"
        f"2. Calculate the number of moles of $\\text{{CO}}_2$ gas collected at STP ($V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$).\n"
        f"3. Calculate the mass of pure calcium carbonate ($\\text{{CaCO}}_3$) present in the tablet.\n"
        f"   *(Molar mass of $\\text{{CaCO}}_3 = 100{{,}}1\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)*\n"
        f"4. Calculate the percentage purity (% by mass) of $\\text{{CaCO}}_3$ in the antacid tablet."
    )

    ans_latex = (
        rf"n(\text{{CO}}_2) = {fmt_sa(n_co2)}\text{{ mol}}; \quad "
        rf"m(\text{{CaCO}}_3) = {fmt_sa(mass_caco3)}\text{{ g}}; \quad "
        rf"\text{{Purity}} = {fmt_sa(purity)}\%"
    )

    sample_answer = (
        f"1. Balanced chemical equation:\n"
        f"   $$\\text{{CaCO}}_3(s) + 2\\text{{HCl}}(aq) \\to \\text{{CaCl}}_2(aq) + \\text{{H}}_2\\text{{O}}(\\ell) + \\text{{CO}}_2(g)$$\n"
        f"2. Moles of CO₂ gas collected:\n"
        f"   $$V = \\frac{{{vol_co2_cm3}}}{{1000}} = {fmt_sa(vol_co2_dm3)}\\text{{ dm}}^3$$\n"
        f"   $$n = \\frac{{V}}{{V_m}} = \\frac{{{fmt_sa(vol_co2_dm3)}}}{{22{{,}}4}} = {fmt_sa(n_co2)}\\text{{ mol}}$$\n"
        f"3. Mass of pure CaCO₃:\n"
        f"   - From equation, $n(\\text{{CaCO}}_3) = n(\\text{{CO}}_2) = {fmt_sa(n_co2)}\\text{{ mol}}$\n"
        f"   - $m = n \\times M = {fmt_sa(n_co2)} \\times 100{{,}}1 = {fmt_sa(mass_caco3)}\\text{{ g}}$\n"
        f"4. Percentage purity:\n"
        f"   $$\\% \\text{{ Purity}} = \\frac{{m(\\text{{pure CaCO}}_3)}}{{m(\\text{{tablet}})}} \\times 100 = \\frac{{{fmt_sa(mass_caco3)}}}{{{fmt_sa(tablet_mass)}}} \\times 100 = {fmt_sa(purity)}\\%$$"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Correct balanced chemical equation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct moles of CO2 calculated at STP: {fmt_sa(n_co2)} mol", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct mass of pure CaCO3 calculated: {fmt_sa(mass_caco3)} g", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Correct percentage purity: {fmt_sa(purity)}%", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Use n = V / Vm where V is in dm³ and Vm = 22,4 dm³·mol⁻¹.",
        "concept": "1 mole of CO₂ gas corresponds to 1 mole of CaCO₃ in the antacid tablet. % Purity = (pure mass / total tablet mass) × 100.",
        "breakdown": f"n(CO₂) = {fmt_sa(vol_co2_dm3)} / 22,4 = {fmt_sa(n_co2)} mol. Mass of CaCO₃ = {fmt_sa(mass_caco3)} g. Purity = {fmt_sa(purity)}%.",
    }

    return make_science_question(
        prefix="ps10_aq_antacid_purity",
        topic=TOPIC,
        subskill="49_stoichiometry_antacid_tablet_gas_volume",
        learning_objective_id=f"{LO}_antacid_purity",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["forgot_to_convert_cm3_to_dm3_for_vm", "inverted_purity_fraction"],
        keywords=["antacid tablet", "molar volume STP", "percentage purity", "calcium carbonate", "gas stoichiometry"],
        term=3,
        caps_weight_percent=25,
        suggested_duration_mins=6,
        mode="compound",
        difficulty=difficulty,
        marks=5,
    )


# --------------------------------------------------------------------------- #
# Subskill 50: Aqueous Reactions Capstone Synthesis Rider
# --------------------------------------------------------------------------- #
def arch_50_aqueous_reactions_capstone_synthesis(rng: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    conc = round(rng.uniform(0.2, 0.5), 1)

    prompt = (
        f"A laboratory practical explores chemical reactions in aqueous solutions through a comprehensive multi-stage experiment:\n\n"
        f"- **Stage 1**: Solid **calcium chloride** ($\\text{{CaCl}}_2$) is dissolved in distilled water to make a "
        f"**${fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** solution. The solution conducts electricity brightly.\n"
        f"- **Stage 2**: A few drops of aqueous **silver nitrate** ($\\text{{AgNO}}_3$) are added to a portion of the Stage 1 solution. "
        f"A dense white precipitate forms.\n"
        f"- **Stage 3**: A strip of clean **zinc metal** is placed into a separate beaker containing aqueous **copper(II) sulphate**.\n\n"
        f"1. Write down the dissociation equation for solid calcium chloride in water.\n"
        f"2. Explain why the electrical conductivity of a ${fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}\\ \\text{{CaCl}}_2$ solution "
        f"is greater than that of an equimolar ${fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}\\ \\text{{NaCl}}$ solution.\n"
        f"3. Write down the **net ionic equation** for the precipitation reaction in Stage 2.\n"
        f"4. Classify the reaction in Stage 3 as either an **ion exchange reaction** or a **redox reaction**, and write down the oxidation half-reaction."
    )

    diss_eq = r"\text{CaCl}_2(s) \to \text{Ca}^{2+}(aq) + 2\text{Cl}^-(aq)"
    net_ppt = r"\text{Ag}^+(aq) + \text{Cl}^-(aq) \to \text{AgCl}(s)"
    ox_half = r"\text{Zn}(s) \to \text{Zn}^{2+}(aq) + 2e^-"

    ans_latex = (
        rf"\text{{Dissociation: }}{diss_eq}; \quad "
        rf"\text{{Net ionic: }}{net_ppt}; \quad "
        rf"\text{{Stage 3 is Redox: }}{ox_half}"
    )

    sample_answer = (
        f"1. Dissociation equation:\n"
        f"   $${diss_eq}$$\n"
        f"2. Explanation of conductivity:\n"
        f"   Equimolar CaCl₂ produces 3 moles of ions (1 Ca²⁺ + 2 Cl⁻) per mole of formula units, whereas NaCl produces only 2 moles of ions (1 Na⁺ + 1 Cl⁻). "
        f"Furthermore, Ca²⁺ has a +2 charge compared to +1 for Na⁺. The higher ion concentration and charge density in CaCl₂ provide superior electrical conductivity.\n"
        f"3. Net ionic equation for Stage 2:\n"
        f"   $${net_ppt}$$\n"
        f"4. Stage 3 classification:\n"
        f"   It is a **redox reaction** (electron transfer from zinc to copper(II) ions).\n"
        f"   Oxidation half-reaction: $${ox_half}$$"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct dissociation equation: {diss_eq}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Explanation of CaCl2 vs NaCl conductivity based on ion count (3 vs 2) and charge density", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Correct net ionic equation: {net_ppt}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Stage 3 classified as redox reaction", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Correct oxidation half-reaction: {ox_half}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Address each stage step by step: Stage 1 = Dissociation, Stage 2 = Precipitation, Stage 3 = Redox.",
        "concept": "CaCl₂ yields 3 ions vs 2 for NaCl. Ag⁺ + Cl⁻ precipitates AgCl. Zinc displacing copper is redox.",
        "breakdown": "Dissociation: CaCl₂ -> Ca²⁺ + 2Cl⁻. Net ppt: Ag⁺ + Cl⁻ -> AgCl. Stage 3 is redox: Zn -> Zn²⁺ + 2e⁻.",
    }

    return make_science_question(
        prefix="ps10_aq_capstone",
        topic=TOPIC,
        subskill="50_aqueous_reactions_capstone_synthesis",
        learning_objective_id=f"{LO}_capstone",
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans_latex,
        sample_answer=sample_answer,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_ion_exchange_and_redox_in_synthesis", "omitted_state_symbols_in_capstone"],
        keywords=["capstone", "dissociation", "conductivity", "precipitation", "redox", "half reactions"],
        term=3,
        caps_weight_percent=30,
        suggested_duration_mins=8,
        mode="compound",
        difficulty=difficulty,
        marks=6,
    )


# --------------------------------------------------------------------------- #
# Export Mapping for Archetypes 26 to 50
# --------------------------------------------------------------------------- #
BUILDERS_26_50 = {
    "26_qualitative_test_for_carbonate_anion": arch_26_qualitative_test_for_carbonate_anion,
    "27_distinguishing_carbonate_from_sulphate": arch_27_distinguishing_carbonate_from_sulphate,
    "28_distinguishing_carbonate_from_chloride": arch_28_distinguishing_carbonate_from_chloride,
    "29_unknown_salt_identification_protocol": arch_29_unknown_salt_identification_protocol,
    "30_ion_exchange_reaction_general_form": arch_30_ion_exchange_reaction_general_form,
    "31_gas_forming_reactions_carbonate_acid": arch_31_gas_forming_reactions_carbonate_acid,
    "32_gas_forming_reactions_hydrogen_carbonate": arch_32_gas_forming_reactions_hydrogen_carbonate,
    "33_gas_forming_reactions_sulphite_and_sulphide": arch_33_gas_forming_reactions_sulphite_and_sulphide,
    "34_acid_base_definitions_arrhenius_and_bronsted": arch_34_acid_base_definitions_arrhenius_and_bronsted,
    "35_acid_base_proton_transfer_mechanism": arch_35_acid_base_proton_transfer_mechanism,
    "36_acid_hydroxide_neutralisation_equations": arch_36_acid_hydroxide_neutralisation_equations,
    "37_acid_hydroxide_net_ionic_equation": arch_37_acid_hydroxide_net_ionic_equation,
    "38_acid_metal_oxide_reactions": arch_38_acid_metal_oxide_reactions,
    "39_acid_metal_carbonate_neutralisation": arch_39_acid_metal_carbonate_neutralisation,
    "40_redox_definition_electron_transfer": arch_40_redox_definition_electron_transfer,
    "41_identifying_oxidation_numbers_in_aqueous_ions": arch_41_identifying_oxidation_numbers_in_aqueous_ions,
    "42_oxidising_and_reducing_agents_identification": arch_42_oxidising_and_reducing_agents_identification,
    "43_metal_displacement_redox_reactions": arch_43_metal_displacement_redox_reactions,
    "44_halogen_displacement_redox_reactions": arch_44_halogen_displacement_redox_reactions,
    "45_metal_acid_redox_reactions": arch_45_metal_acid_redox_reactions,
    "46_distinguishing_ion_exchange_from_redox": arch_46_distinguishing_ion_exchange_from_redox,
    "47_stoichiometry_precipitation_mass_calculation": arch_47_stoichiometry_precipitation_mass_calculation,
    "48_stoichiometry_limiting_reagent_in_precipitation": arch_48_stoichiometry_limiting_reagent_in_precipitation,
    "49_stoichiometry_antacid_tablet_gas_volume": arch_49_stoichiometry_antacid_tablet_gas_volume,
    "50_aqueous_reactions_capstone_synthesis": arch_50_aqueous_reactions_capstone_synthesis,
}
