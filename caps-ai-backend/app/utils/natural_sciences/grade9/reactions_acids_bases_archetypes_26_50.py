"""Grade 9 Natural Sciences - Reactions of Acids and Bases: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/PDF - Reactions of Acids and bases.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_num(val: float, decimals: int = 1) -> str:
    """Format a decimal using South African comma notation."""
    return f"{val:.{decimals}f}".replace(".", ",")


def _q(
    rng: random.Random,
    code: str,
    subskill: str,
    prompt: str,
    correct: str,
    sol: str,
    marks: int,
    qtype: str,
    tags: List[str],
    tier1: str,
    tier2: str,
    tier3: str,
    options: Optional[List[str]] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    guide = f"Marking Guide ({marks} marks): Award credit for each verified scientific step shown in the solution."
    item: Dict[str, Any] = {
        "id": f"ns9_rab_{code}_{rng.randint(100000, 999999)}",
        "subskill": subskill,
        "question_type": qtype,
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": marks,
        "marking_schema": guide,
        "marking_guide": guide,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks + 1),
        "hints": {"tier_1": tier1, "tier_2": tier2, "tier_3": tier3},
        "misconception_tags": tags,
    }
    if options is not None:
        item["options"] = options
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    return item


def _svg_carbonate_limewater_apparatus(rng: random.Random, acid_label: str, carb_label: str) -> Dict[str, Any]:
    """Parameterized conical flask + delivery tube into clear/milky limewater test tube."""
    bubble_dy = rng.randint(-6, 6)
    tube_y = 148 + bubble_dy
    svg = (
        f'<svg viewBox="0 0 430 220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="220" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<polygon points="75,180 155,180 130,85 100,85" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="85" y="138" width="60" height="40" fill="#e0f2fe" opacity="0.8"/>'
        f'<circle cx="105" cy="168" r="4" fill="#ffffff" stroke="#334155"/>'
        f'<circle cx="122" cy="158" r="3.5" fill="#ffffff" stroke="#334155"/>'
        f'<path d="M 115 85 L 115 40 L 295 40 L 295 {tube_y}" fill="none" stroke="#334155" stroke-width="3"/>'
        f'<rect x="265" y="92" width="60" height="88" rx="8" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="268" y="132" width="54" height="46" rx="4" fill="#cbd5e1" opacity="0.65"/>'
        f'<circle cx="288" cy="{tube_y - 6}" r="3" fill="#ffffff" stroke="#475569"/>'
        f'<text x="115" y="198" font-size="11" fill="#0f172a" text-anchor="middle">{acid_label} + {carb_label}</text>'
        f'<text x="205" y="30" font-size="11" fill="#1d4ed8" text-anchor="middle">Gas X</text>'
        f'<text x="295" y="198" font-size="11" fill="#0f172a" text-anchor="middle">Clear limewater -> milky</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_acid_base_particle_exchange(rng: random.Random, pairs: int, cation_sym: str, anion_sym: str) -> Dict[str, Any]:
    """Parameterized submicroscopic particle model of acid + hydroxide exchange."""
    y_shift = rng.randint(-4, 4)
    nodes = []
    for i in range(pairs):
        y = 58 + i * 42 + y_shift
        nodes.append(
            f'<circle cx="65" cy="{y}" r="11" fill="#ef4444" stroke="#7f1d1d"/>'
            f'<text x="65" y="{y + 4}" font-size="10" fill="#ffffff" text-anchor="middle">H+</text>'
            f'<circle cx="93" cy="{y}" r="13" fill="#22c55e" stroke="#14532d"/>'
            f'<text x="93" y="{y + 4}" font-size="10" fill="#ffffff" text-anchor="middle">{anion_sym}</text>'
            f'<circle cx="155" cy="{y}" r="12" fill="#3b82f6" stroke="#1e3a8a"/>'
            f'<text x="155" y="{y + 4}" font-size="10" fill="#ffffff" text-anchor="middle">{cation_sym}</text>'
            f'<circle cx="183" cy="{y}" r="13" fill="#a855f7" stroke="#581c87"/>'
            f'<text x="183" y="{y + 4}" font-size="10" fill="#ffffff" text-anchor="middle">OH-</text>'
            f'<circle cx="290" cy="{y}" r="12" fill="#3b82f6" stroke="#1e3a8a"/>'
            f'<text x="290" y="{y + 4}" font-size="10" fill="#ffffff" text-anchor="middle">{cation_sym}</text>'
            f'<circle cx="316" cy="{y}" r="13" fill="#22c55e" stroke="#14532d"/>'
            f'<text x="316" y="{y + 4}" font-size="10" fill="#ffffff" text-anchor="middle">{anion_sym}</text>'
            f'<circle cx="372" cy="{y}" r="14" fill="#38bdf8" stroke="#0369a1"/>'
            f'<text x="372" y="{y + 4}" font-size="10" fill="#0f172a" text-anchor="middle">H2O</text>'
        )
    svg = (
        f'<svg viewBox="0 0 430 200" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="200" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="125" y="25" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Reactants ({pairs} pairs)</text>'
        f'<text x="330" y="25" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Products</text>'
        f'<line x1="225" y1="95" x2="255" y2="95" stroke="#0f172a" stroke-width="2.5"/>'
        f'<polygon points="255,95 247,90 247,100" fill="#0f172a"/>'
        f'{"".join(nodes)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_26_metal_carbonate_basic_character_in_aqueous_suspension(rng: random.Random) -> Dict[str, Any]:
    carb, formula, ph = rng.choice([
        ("calcium carbonate (crushed white chalk)", "CaCO3", "8,4"),
        ("sodium carbonate (washing soda)", "Na2CO3", "11,2"),
        ("sodium hydrogen carbonate", "NaHCO3", "8,5"),
    ])
    prompt = (
        f"A learner shakes solid **{carb}** ($\\text{{{formula}}}$) in pure distilled water and places a drop onto universal indicator paper, obtaining **pH {ph}**.\n\n"
        "1. Classify the aqueous suspension/solution as acidic, neutral, or basic [1].\n"
        "2. State what happens to the pH when dilute hydrochloric acid is added drop by drop to this mixture [1]."
    )
    correct = f"Basic (pH {ph} > 7); The pH decreases steadily towards 7 (and below 7 if excess HCl is added)"
    sol = (
        f"**Step 1:** Carbonate salts yield **basic** aqueous mixtures (**pH {ph} > 7**) [1].\n\n"
        "**Step 2:** Adding hydrochloric acid neutralises the carbonate base, causing the **pH to decrease** towards 7 and then below 7 in excess acid [1]."
    )
    return _q(
        rng, "26", "26_metal_carbonate_basic_character_in_aqueous_suspension", prompt, correct, sol, 2, "short_answer",
        ["carbonates_are_neutral_salts_myth"],
        "Compare the measured pH to 7.",
        "Metal carbonates act as bases (pH > 7); adding acid reduces pH.",
        correct,
    )


def arch_27_acid_plus_metal_carbonate_general_word_equation(rng: random.Random) -> Dict[str, Any]:
    acid, carb, salt = rng.choice([
        ("hydrochloric acid", "zinc carbonate", "zinc chloride"),
        ("sulfuric acid", "copper carbonate", "copper sulfate"),
        ("nitric acid", "calcium carbonate", "calcium nitrate"),
    ])
    prompt = (
        "All metal carbonates follow one characteristic general neutralisation pattern when mixed with acids.\n\n"
        "1. Write the **general word equation** for the reaction of an acid with a metal carbonate [2].\n"
        f"2. Apply this rule to write the **specific word equation** for **{acid}** reacting with **{carb}** [2]."
    )
    correct = f"Acid + Metal carbonate -> Salt + Water + Carbon dioxide; {acid.capitalize()} + {carb} -> {salt.capitalize()} + Water + Carbon dioxide"
    sol = (
        "**Step 1:** General word equation: **Acid + Metal carbonate $\\rightarrow$ Salt + Water + Carbon dioxide** [2].\n\n"
        f"**Step 2:** Specific word equation: **{acid.capitalize()} + {carb} $\\rightarrow$ {salt.capitalize()} + Water + Carbon dioxide** [2]."
    )
    return _q(
        rng, "27", "27_acid_plus_metal_carbonate_general_word_equation", prompt, correct, sol, 4, "structured",
        ["carbonate_omits_carbon_dioxide_product_error"],
        "Unlike oxides and hydroxides, carbonates release a third gaseous product.",
        "Acid + Metal carbonate -> Salt + Water + Carbon dioxide.",
        correct,
    )


def arch_28_chalk_calcium_carbonate_hydrochloric_acid_effervescence(rng: random.Random) -> Dict[str, Any]:
    acid_vol = rng.choice([15, 20, 25])
    prompt = (
        f"Crushed white blackboard chalk ($\\text{{CaCO}}_3$) is dropped into a test tube containing **{acid_vol} ml** of dilute hydrochloric acid.\n\n"
        "1. State **two clear macroscopic observations** inside the test tube [2].\n"
        "2. Explain why the gas bubbles are NOT hydrogen gas [2]."
    )
    correct = "Vigorous fizzing/effervescence (gas bubbles form immediately) and the solid chalk dissolves into a clear solution; The reactant is a metal carbonate (CaCO3), not a pure metal, so carbon dioxide is released instead of hydrogen"
    sol = (
        "**Step 1:** Vigorous **effervescence (fizzing)** occurs and the white chalk powder **dissolves** to leave a clear colourless solution [2].\n\n"
        "**Step 2:** **Carbon dioxide ($\\text{CO}_2$)** is released because chalk is a metal carbonate ($\\text{CaCO}_3$); only pure metals (like Mg or Zn) release hydrogen gas ($\\text{H}_2$) with acid [2]."
    )
    return _q(
        rng, "28", "28_chalk_calcium_carbonate_hydrochloric_acid_effervescence", prompt, correct, sol, 4, "structured",
        ["chalk_hcl_produces_hydrogen_gas_myth"],
        "Think carefully about what compound blackboard chalk is made of (CaCO3 vs pure calcium metal).",
        "Fizzing = CO2 gas from a carbonate; pure solid dissolves as soluble CaCl2 forms.",
        correct,
    )


def arch_29_hydrochloric_acid_plus_calcium_carbonate_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    sample = rng.choice(["marble chips", "limestone rock", "powdered eggshells", "white chalk dust"])
    prompt = (
        f"A sample of **{sample}** (composed of calcium carbonate, $\\text{{CaCO}}_3$) reacts with dilute hydrochloric acid ($\\text{{HCl}}$).\n\n"
        "1. Identify the **metal salt** remaining dissolved in solution and write its chemical formula [2].\n"
        "2. Write the complete **balanced chemical equation** for this reaction [2]."
    )
    correct = "Calcium chloride (CaCl2); 2HCl + CaCO3 -> CaCl2 + H2O + CO2"
    sol = (
        "**Step 1:** Removing $\\text{H}_2\\text{O}$ and $\\text{CO}_2$ leaves $Ca^{2+}$ paired with two $Cl^-$ ions to make **calcium chloride ($\\text{CaCl}_2$)** [2].\n\n"
        "**Step 2:** Balanced chemical equation: **$$2\\text{HCl} + \\text{CaCO}_3 \\rightarrow \\text{CaCl}_2 + \\text{H}_2\\text{O} + \\text{CO}_2$$** [2]."
    )
    return _q(
        rng, "29", "29_hydrochloric_acid_plus_calcium_carbonate_balanced_equation", prompt, correct, sol, 4, "structured",
        ["cacl2_missing_coefficient_2_hcl_error"],
        "Calcium has +2 valency, so the salt is CaCl2 (not CaCl).",
        "Need 2 HCl to provide 2 Cl for CaCl2 and 2 H for H2O.",
        correct,
    )


def arch_30_hydrochloric_acid_plus_sodium_carbonate_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice(["washing soda crystals", "soda ash powder", "laboratory sodium carbonate"])
    prompt = (
        f"**Sodium carbonate** ($\\text{{Na}}_2\\text{{CO}}_3$, {context}) reacts completely with dilute hydrochloric acid ($\\text{{HCl}}$).\n\n"
        "Write the **balanced chemical equation** for this reaction, showing all stoichiometric coefficients clearly [3]."
    )
    correct = "2HCl + Na2CO3 -> 2NaCl + H2O + CO2"
    sol = (
        "**Step 1:** Skeleton products are $\\text{NaCl}$, $\\text{H}_2\\text{O}$, and $\\text{CO}_2$ [1].\n\n"
        "**Step 2:** Because $\\text{Na}_2\\text{CO}_3$ supplies **2 Na** atoms, you form **2 NaCl**, which requires **2 HCl** (matching the 2 H atoms in $\\text{H}_2\\text{O}$) [1].\n\n"
        "**Step 3:** Balanced equation: **$$2\\text{HCl} + \\text{Na}_2\\text{CO}_3 \\rightarrow 2\\text{NaCl} + \\text{H}_2\\text{O} + \\text{CO}_2$$** [1]."
    )
    return _q(
        rng, "30", "30_hydrochloric_acid_plus_sodium_carbonate_balanced_equation", prompt, correct, sol, 3, "short_answer",
        ["na2co3_leaves_one_nacl_unbalanced_error"],
        "Notice the subscript 2 in Na2CO3 means two sodium atoms enter the reaction.",
        "2 Na -> 2 NaCl -> requires 2 HCl -> gives 2HCl + Na2CO3 -> 2NaCl + H2O + CO2.",
        correct,
    )


def arch_31_carbon_dioxide_density_pour_into_limewater_technique(rng: random.Random) -> Dict[str, Any]:
    spec = _svg_carbonate_limewater_apparatus(rng, rng.choice(["HCl", "Vinegar"]), rng.choice(["CaCO3", "NaHCO3"]))
    wait_mins = rng.choice([1, 2, 3])
    prompt = (
        f"In the setup shown, acid reacts with a metal carbonate inside the conical flask to generate **Gas X** for {wait_mins} minutes.\n"
        "Notice that even without a stopper and delivery tube, carbon dioxide can actually be **poured gently** out of the mouth of a flask into another flask of clear limewater.\n\n"
        "1. Identify **Gas X** [1].\n"
        "2. Explain the physical property of Gas X that allows it to remain briefly at the bottom of the reaction flask and be poured downward like an invisible liquid [2]."
    )
    correct = "Carbon dioxide (CO2); Carbon dioxide has a higher density than air, so it sinks and pools briefly inside the flask until swirled/poured out without splashing liquid"
    sol = (
        "**Step 1:** Gas X produced from an acid + metal carbonate is **carbon dioxide ($\\text{CO}_2$)** [1].\n\n"
        "**Step 2:** **Carbon dioxide is denser than air** ($\\approx 1{,}98\\text{ kg/m}^3$ vs air $\\approx 1{,}2\\text{ kg/m}^3$), so it settles beneath air inside the flask for a short time and can be tilted gently over into the limewater flask without spilling any acid solution [2]."
    )
    return _q(
        rng, "31", "31_carbon_dioxide_density_pour_into_limewater_technique", prompt, correct, sol, 3, "structured",
        ["co2_rises_like_hydrogen_myth"],
        "Compare the molar mass / density of CO2 (44 g/mol) against air (~29 g/mol) and H2 (2 g/mol).",
        "Unlike buoyant H2, CO2 is heavier/denser than air, so it settles downwards.",
        correct, diagram_spec=spec,
    )


def arch_32_clear_limewater_cloudy_milky_precipitate_test(rng: random.Random) -> Dict[str, Any]:
    tube_label = rng.choice(["Test Tube B", "Flask 2", "Indicator Tube"])
    prompt = (
        f"When carbon dioxide gas is bubbled into **{tube_label}** containing **clear limewater** (aqueous calcium hydroxide, $\\text{{Ca(OH)}}_2$), the colourless solution quickly turns **milky / cloudy white**.\n\n"
        "1. State the common name of the reagent **clear limewater** and explain why its test confirms $\\text{CO}_2$ [2].\n"
        "2. Name the fine **white insoluble solid** (precipitate) responsible for the cloudy appearance [1]."
    )
    correct = "Aqueous calcium hydroxide solution; CO2 reacts specifically with Ca(OH)2 to form an insoluble white precipitate; Calcium carbonate (CaCO3)"
    sol = (
        "**Step 1:** Clear limewater is aqueous **calcium hydroxide ($\\text{Ca(OH)}_2$)**; turning clear limewater milky is the standard diagnostic test for **carbon dioxide** [2].\n\n"
        "**Step 2:** The cloudy white suspension is tiny solid particles of insoluble **calcium carbonate ($\\text{CaCO}_3$)** precipitate ($\\text{Ca(OH)}_2 + \\text{CO}_2 \\rightarrow \\text{CaCO}_3 \\downarrow + \\text{H}_2\\text{O}$) [1]."
    )
    return _q(
        rng, "32", "32_clear_limewater_cloudy_milky_precipitate_test", prompt, correct, sol, 3, "structured",
        ["limewater_is_lemon_juice_myth"],
        "Remember 'limewater' comes from agricultural lime Ca(OH)2, NOT citrus lime juice!",
        "CO2 + Ca(OH)2 -> insoluble white CaCO3 precipitate + H2O.",
        correct,
    )


def arch_33_comparing_gas_evolution_oxides_hydroxides_vs_carbonates(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("Zinc oxide (ZnO)", "Zinc hydroxide (Zn(OH)2)", "Zinc carbonate (ZnCO3)"),
        ("Magnesium oxide (MgO)", "Magnesium hydroxide (Mg(OH)2)", "Magnesium carbonate (MgCO3)"),
        ("Calcium oxide (CaO)", "Calcium hydroxide (Ca(OH)2)", "Calcium carbonate (CaCO3)"),
    ])
    ox, hy, ca = pair
    prompt = (
        f"Dilute hydrochloric acid is added separately to three beakers containing **{ox}**, **{hy}**, and **{ca}**.\n\n"
        "Which beaker(s) produce **gas bubbles (effervescence)** during neutralisation?"
    )
    correct = f"Only {ca} produces gas bubbles (carbon dioxide); {ox} and {hy} form only salt + water with no gas."
    distractors = [
        f"All three produce hydrogen gas because they all contain the metal.",
        f"{hy} and {ca} both release oxygen gas while {ox} stays frozen.",
        f"Only {ox} releases carbon dioxide bubbles because oxides carry extra oxygen.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** {ox} (metal oxide) + HCl -> salt + water (no gas).\n"
        f"**Step 2:** {hy} (metal hydroxide) + HCl -> salt + water (no gas).\n"
        f"**Step 3:** Only the carbonate **{ca}** + HCl -> salt + water + **carbon dioxide gas bubbles** [2]."
    )
    return _q(
        rng, "33", "33_comparing_gas_evolution_oxides_hydroxides_vs_carbonates", prompt, correct, sol, 2, "multiple_choice",
        ["metal_hydroxides_bubble_with_acid_myth"],
        "Ask yourself which functional group supplies carbon (C) to form CO2.",
        "Only carbonates (CO3) contain carbon to liberate CO2 gas with acids.",
        correct, options=options,
    )


def arch_34_variables_control_and_ph_vs_acid_volume_graph_analysis(rng: random.Random) -> Dict[str, Any]:
    vol_base = rng.choice([25, 30, 50])
    prompt = (
        f"A Grade 9 learner pours **{vol_base} ml** of sodium carbonate solution at $22\\,^\\circ\\text{{C}}$ into a flask and measures the **pH** after adding each $5\\text{{ ml}}$ portion of $1\\text{{ M}}$ hydrochloric acid.\n\n"
        "Identify all three variable categories for this fair test:\n"
        "1. Independent variable (what is deliberately changed) [1]\n"
        "2. Dependent variable (what is measured as outcome) [1]\n"
        "3. **Two** controlled variables kept constant [2]"
    )
    correct = f"Independent: Volume of hydrochloric acid added; Dependent: pH of the mixture; Controlled: Starting volume ({vol_base} ml) & concentration of sodium carbonate, concentration of HCl, and temperature"
    sol = (
        "**Step 1:** **Independent variable:** Total volume of hydrochloric acid added (x-axis) [1].\n\n"
        "**Step 2:** **Dependent variable:** Measured pH of the reaction mixture (y-axis) [1].\n\n"
        f"**Step 3:** **Controlled variables:** Initial volume ({vol_base} ml) and concentration of $\\text{{Na}}_2\\text{{CO}}_3$, concentration ($1\\text{{ M}}$) of HCl, and room temperature [2]."
    )
    return _q(
        rng, "34", "34_variables_control_and_ph_vs_acid_volume_graph_analysis", prompt, correct, sol, 4, "structured",
        ["swapped_independent_dependent_ph_variables_error"],
        "What does the investigator choose beforehand vs what responds on the pH meter?",
        "Chosen step-by-step = volume of acid (independent); measured outcome = pH (dependent).",
        correct,
    )


def arch_35_salt_naming_rule_from_parent_acid_hcl_h2so4_hno3(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("hydrochloric acid", "HCl", "potassium oxide", "-chloride", "potassium chloride"),
        ("sulfuric acid", "H2SO4", "magnesium hydroxide", "-sulfate", "magnesium sulfate"),
        ("nitric acid", "HNO3", "calcium carbonate", "-nitrate", "calcium nitrate"),
        ("ethanoic acid (vinegar)", "CH3COOH", "sodium hydroxide", "-ethanoate", "sodium ethanoate"),
    ])
    acid, a_f, base, suffix, salt = case
    prompt = (
        f"Using the standard salt nomenclature rules, name the salt produced when **{acid}** ($\\text{{{a_f}}}$) neutralises **{base}**, and state the general salt ending derived from {acid} [2]."
    )
    correct = f"{salt.capitalize()}; Acids containing {a_f} form {suffix} salts"
    sol = (
        f"**Step 1:** Take the metal name first (**{base.split()[0]}**) [1].\n\n"
        f"**Step 2:** Pair it with the acid ending (**{suffix}** from {acid}) -> **{salt.capitalize()}** [1]."
    )
    return _q(
        rng, "35", "35_salt_naming_rule_from_parent_acid_hcl_h2so4_hno3", prompt, correct, sol, 2, "short_answer",
        ["sulfuric_acid_makes_sulfide_salts_error"],
        "Match: HCl -> chloride, H2SO4 -> sulfate, HNO3 -> nitrate.",
        f"{base.split()[0].capitalize()} + {suffix} = {salt.capitalize()}.",
        correct,
    )


def arch_36_predicting_salt_formula_from_metal_valence_and_anion(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("Magnesium", "Mg^{2+}", "nitrate", "NO_3^-", "Mg(NO3)2", "two nitrate ions needed to balance Mg2+ charge"),
        ("Calcium", "Ca^{2+}", "chloride", "Cl^-", "CaCl2", "two chloride ions needed to balance Ca2+ charge"),
        ("Potassium", "K^+", "sulfate", "SO_4^{2-}", "K2SO4", "two potassium (+1) ions needed to balance one sulfate (-2) ion"),
        ("Sodium", "Na^+", "chloride", "Cl^-", "NaCl", "1:1 ion ratio balances +1 and -1 charges"),
    ])
    metal, m_ion, anion, a_ion, formula, reason = case
    prompt = (
        f"An ionic salt forms between **{metal}** ($\\text{{{m_ion}}}$) and **{anion}** ($\\text{{{a_ion}}}$) ions during neutralisation.\n\n"
        "Deduce the correct neutral chemical formula for this salt and justify the subscript ratio [2]."
    )
    correct = f"{formula}; {reason}"
    sol = (
        f"**Step 1:** Total positive charge must equal total negative charge inside the neutral salt crystal [1].\n\n"
        f"**Step 2:** Therefore **{formula}** is required because {reason} [1]."
    )
    return _q(
        rng, "36", "36_predicting_salt_formula_from_metal_valence_and_anion", prompt, correct, sol, 2, "short_answer",
        ["unbalanced_ionic_charge_salt_formula_error"],
        "Make positive and negative ion charges cancel to zero using cross-balancing.",
        f"Balance {m_ion} and {a_ion} to zero net charge -> {formula}.",
        correct,
    )


def arch_37_sulfuric_acid_neutralisation_with_metal_bases(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("copper(II) oxide", "CuO", "H2SO4 + CuO -> CuSO4 + H2O", "blue copper(II) sulfate"),
        ("magnesium hydroxide", "Mg(OH)2", "H2SO4 + Mg(OH)2 -> MgSO4 + 2H2O", "Epsom salt (magnesium sulfate)"),
        ("sodium carbonate", "Na2CO3", "H2SO4 + Na2CO3 -> Na2SO4 + H2O + CO2", "sodium sulfate with CO2 effervescence"),
    ])
    base, b_f, eq, desc = case
    prompt = (
        f"Dilute **sulfuric acid ($\\text{{H}}_2\\text{{SO}}_4$)** reacts completely with **{base} ($\\text{{{b_f}}}$)**, producing {desc}.\n\n"
        "Write the **balanced chemical equation** for this neutralisation reaction [3]."
    )
    correct = eq
    sol = (
        "**Step 1:** Recall sulfate salts contain the $\\text{SO}_4^{2-}$ group [1].\n\n"
        f"**Step 2:** Balance H, O, and the metal ion across reactants and products -> **$${eq}$$** [2]."
    )
    return _q(
        rng, "37", "37_sulfuric_acid_neutralisation_with_metal_bases", prompt, correct, sol, 3, "short_answer",
        ["h2so4_wrong_stoichiometry_error"],
        "Keep the SO4 sulfate ion intact as a single unit while counting atoms.",
        f"Check H and metal counts to confirm: {eq}.",
        correct,
    )


def arch_38_indigestion_heartburn_and_antacid_tablets(rng: random.Random) -> Dict[str, Any]:
    ingred, form, name = rng.choice([
        ("magnesium hydroxide (Milk of Magnesia)", "Mg(OH)2", "magnesium chloride"),
        ("calcium carbonate (chalk-based antacid)", "CaCO3", "calcium chloride"),
        ("sodium bicarbonate (baking soda relief)", "NaHCO3", "sodium chloride"),
    ])
    prompt = (
        f"A person suffering from painful heartburn and acid indigestion takes an antacid tablet whose active ingredient is **{ingred} ($\\text{{{form}}}$)**.\n\n"
        "1. Name the acid naturally secreted in the human stomach that causes acidity [1].\n"
        f"2. Explain chemically how {ingred.split('(')[0].strip()} relieves the symptoms, and name the dissolved salt formed [3]."
    )
    correct = f"Hydrochloric acid (HCl); Antacid base neutralises excess stomach HCl, raising stomach pH to comfortable levels and forming {name} + water"
    sol = (
        "**Step 1:** Excess **hydrochloric acid ($\\text{HCl}$)** in gastric juice causes acid indigestion [1].\n\n"
        f"**Step 2:** Because **{ingred}** is a mild **base**, it undergoes a **neutralisation reaction** with stomach $\\text{{HCl}}$, lowering acidity (raising pH) and forming harmless **{name}** and water (plus burped $\\text{{CO}}_2$ if a carbonate) [3]."
    )
    return _q(
        rng, "38", "38_indigestion_heartburn_and_antacid_tablets", prompt, correct, sol, 4, "structured",
        ["antacids_contain_strong_acid_myth"],
        "Remember stomach acid is HCl and antacids ('anti-acid') act as safe mild bases.",
        f"HCl + {form} neutralises excess acid, forming {name}.",
        correct,
    )


def arch_39_bee_sting_acidic_vs_wasp_sting_alkaline_remedies(rng: random.Random) -> Dict[str, Any]:
    sting = rng.choice([
        ("bee sting", "acidic (formic/methanoic acid)", "dilute baking soda / bicarbonate of soda paste (a mild base)"),
        ("wasp sting", "basic / alkaline", "dilute vinegar / lemon juice (a mild acid)"),
    ])
    insect, nature, remedy = sting
    prompt = (
        f"While gardening in Limpopo, a hiker remembers Chemistry neutralisation rules when treating insect stings: a **{insect}** injects venom that is **{nature}**.\n\n"
        f"1. State which household remedy should be applied to soothe the **{insect}** — vinegar or baking soda paste [1].\n"
        "2. Explain why applying a very strong chemical like drain cleaner ($\text{NaOH}$) or pool acid ($\text{HCl}$) would be dangerous [1]."
    )
    correct = f"{remedy}; Strong acids or bases are corrosive and would cause severe chemical burns to living skin tissue"
    sol = (
        f"**Step 1:** Because a {insect} is {nature}, it is neutralised using **{remedy}** [1].\n\n"
        "**Step 2:** Concentrated/strong acids or bases are **corrosive** and would burn and damage healthy skin cells [1]."
    )
    return _q(
        rng, "39", "39_bee_sting_acidic_vs_wasp_sting_alkaline_remedies", prompt, correct, sol, 2, "short_answer",
        ["bee_and_wasp_stings_both_acidic_myth"],
        "Remember: Bee -> Acidic (treat with Base = Baking soda); Wasp -> Alkaline (treat with Vinegar/Acid).",
        f"Opposites neutralise safely when dilute: {remedy}.",
        correct,
    )


def arch_40_agricultural_soil_liming_with_calcium_carbonate_or_ash(rng: random.Random) -> Dict[str, Any]:
    region, crop, soil_ph = rng.choice([
        ("Western Cape vineyard", "grape vines", "4,4"),
        ("KwaZulu-Natal midlands farm", "maize", "4,6"),
        ("Mpumalanga citrus orchard", "orange trees", "4,8"),
    ])
    prompt = (
        f"Soil testing on a **{region}** cultivating **{crop}** reveals an acidic soil reading of **pH {soil_ph}**, whereas optimal crop growth requires **pH 6,5**.\n\n"
        "1. Suggest a common inexpensive basic substance farmers spread onto acidic soil to raise its pH [1].\n"
        "2. Name the chemical reaction taking place in the soil moisture [1]."
    )
    correct = "Agricultural lime (calcium carbonate / CaCO3, calcium hydroxide, or wood ash); Acid-base neutralisation reaction"
    sol = (
        "**Step 1:** Farmers spread **agricultural lime** (crushed limestone, **$\\text{CaCO}_3$**, slaked lime, or alkaline wood ash) onto the field [1].\n\n"
        "**Step 2:** The lime base reacts with excess soil acids via **neutralisation**, raising soil pH towards neutral (6,5) so plants absorb nutrients effectively [1]."
    )
    return _q(
        rng, "40", "40_agricultural_soil_liming_with_calcium_carbonate_or_ash", prompt, correct, sol, 2, "short_answer",
        ["adding_acidic_fertiliser_to_fix_acid_soil_error"],
        "To raise low pH (acidic soil), you must add a base.",
        "Agricultural lime (CaCO3) neutralises acidic soils.",
        correct,
    )


def arch_41_acid_mine_drainage_treatment_in_south_africa(rng: random.Random) -> Dict[str, Any]:
    basin, ph_val = rng.choice([
        ("Witwatersrand gold mine basin", "2,8"),
        ("Mpumalanga coalfield tributary", "3,1"),
    ])
    prompt = (
        f"Old mine workings in the **{basin}** release **acid mine drainage (AMD)** containing dissolved sulfuric acid at **pH {ph_val}**, threatening downstream rivers.\n\n"
        "1. Explain chemically how environmental engineers pre-treat AMD water using powdered **limestone ($\\text{{CaCO}}_3$)** or **lime ($\\text{{Ca(OH)}}_2$)** before release [2].\n"
        "2. Why must engineers avoid adding a massive excess of concentrated sodium hydroxide instead? [1]"
    )
    correct = "Lime neutralises the sulfuric acid in AMD, raising river pH towards 7 and precipitating toxic metals; Excess NaOH would overshoot pH above 7 creating caustic alkaline river pollution"
    sol = (
        "**Step 1:** Basic limestone ($\\text{CaCO}_3$) or hydrated lime neutralises $\\text{H}_2\\text{SO}_4$ in AMD, raising the water pH closer to neutral (6,5–7,5) and precipitating harmful dissolved metals [2].\n\n"
        "**Step 2:** Adding excess strong alkali ($\\text{NaOH}$) would turn the river **strongly alkaline (pH > 9)**, which is equally lethal to aquatic organisms [1]."
    )
    return _q(
        rng, "41", "41_acid_mine_drainage_treatment_in_south_africa", prompt, correct, sol, 3, "structured",
        ["alkaline_runoff_is_harmless_myth"],
        "Consider both raising pH up from 3 towards 7 AND avoiding overshooting above 7 into caustic alkali.",
        "Lime gently neutralises H2SO4; overshooting pH with NaOH causes alkaline poisoning.",
        correct,
    )


def arch_42_swimming_pool_ph_regulation_acid_and_soda_ash(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        ("6,2 (too acidic, stinging eyes and corroding metal pumps)", "add soda ash (sodium carbonate, Na2CO3) / sodium bicarbonate", "raise"),
        ("8,2 (too basic, causing cloudy scale and poor chlorine disinfection)", "add dilute hydrochloric pool acid", "lower"),
    ])
    measured, fix, direction = scenario
    prompt = (
        f"A municipal swimming pool tests at **pH {measured}**.\n\n"
        f"State which chemical additive should be used to **{direction} the pH** safely back into the optimal **7,2–7,6** range and explain the chemistry involved [2]."
    )
    correct = f"{fix}; Acid-base neutralisation adjusts H+ concentration back toward neutral 7,2–7,6"
    sol = (
        f"**Step 1:** To {direction} pH {measured} back into 7,2–7,6, pool maintainers **{fix}** [1].\n\n"
        "**Step 2:** This applies **neutralisation** — adding a controlled weak base removes excess acid (raises pH), while pool acid neutralises excess alkalinity (lowers pH) [1]."
    )
    return _q(
        rng, "42", "42_swimming_pool_ph_regulation_acid_and_soda_ash", prompt, correct, sol, 2, "short_answer",
        ["adding_acid_to_acidic_pool_error"],
        "If pH is already too low (<7), add a mild base; if too high (>8), add acid.",
        f"Pool pH {measured.split()[0]} -> need to {direction} pH -> {fix}.",
        correct,
    )


def arch_43_toothpaste_alkaline_neutralisation_of_plaque_acids(rng: random.Random) -> Dict[str, Any]:
    sugar_food = rng.choice(["sugary cool drinks", "sticky sweets", "fruit juice"])
    prompt = (
        f"Oral bacteria break down remnants of **{sugar_food}** on teeth and excrete organic **acids** that dissolve tooth enamel. Most commercial toothpastes are formulated to be **mildly alkaline (pH ~8,5–9)**.\n\n"
        "Explain how brushing with alkaline toothpaste helps prevent cavities [2]."
    )
    correct = "The mild base in toothpaste neutralises mouth plaque acids, raising oral pH back around 7 before acid corrodes the calcium-rich tooth enamel."
    sol = (
        "**Step 1:** Sugar metabolism by plaque bacteria lowers mouth pH (< 5,5), corroding mineral tooth enamel [1].\n\n"
        "**Step 2:** Mildly **basic toothpaste neutralises these acids**, restoring safe neutral pH (~7) and protecting enamel from decay [1]."
    )
    return _q(
        rng, "43", "43_toothpaste_alkaline_neutralisation_of_plaque_acids", prompt, correct, sol, 2, "short_answer",
        ["toothpaste_must_be_acidic_to_clean_myth"],
        "Think about what neutralises bacterial acids without hurting your gums.",
        "Toothpaste is mildly alkaline so it neutralises enamel-attacking acids.",
        correct,
    )


def arch_44_acid_spill_laboratory_safety_and_sodium_bicarbonate_neutralisation(rng: random.Random) -> Dict[str, Any]:
    acid_spilled = rng.choice(["hydrochloric acid", "sulfuric acid"])
    prompt = (
        f"A small bottle of **{acid_spilled}** spills onto a school laboratory bench. Rather than mopping it immediately with bare cloths, the teacher sprinkles dry **sodium hydrogen carbonate ($\\text{{NaHCO}}_3$)** powder onto the puddle.\n\n"
        "1. What visual signal indicates when the acid spill has been completely neutralised? [1]\n"
        "2. Why is dry sodium bicarbonate safer for neutralising an acid spill than pouring concentrated sodium hydroxide ($\text{NaOH}$)? [2]"
    )
    correct = "Fizzing/bubbling of CO2 gas stops completely; Sodium bicarbonate is a weak base with built-in fizz indicator and won't cause exothermic heat surges or caustic alkali burns if added in slight excess"
    sol = (
        "**Step 1:** As long as unreacted acid remains, $\\text{NaHCO}_3$ fizzes vigorously producing $\\text{CO}_2$; once **effervescence (fizzing) stops**, neutralisation is complete [1].\n\n"
        "**Step 2:** Strong $\\text{NaOH}$ releases dangerous **heat** violently and leaves a corrosive alkaline hazard if slightly over-added, whereas weak **sodium bicarbonate** neutralises gently and safely [2]."
    )
    return _q(
        rng, "44", "44_acid_spill_laboratory_safety_and_sodium_bicarbonate_neutralisation", prompt, correct, sol, 3, "structured",
        ["using_strong_caustic_soda_for_acid_spill_error"],
        "Look for two clues: carbonate gas evolution stopping, and why weak powder beats caustic lye.",
        "Stop of CO2 bubbling signals completion; weak NaHCO3 avoids violent heat and caustic overshoot.",
        correct,
    )


def arch_45_corrosive_laboratory_acids_vs_strong_alkalis_handling(rng: random.Random) -> Dict[str, Any]:
    reagent = rng.choice(["concentrated hydrochloric acid", "concentrated sulfuric acid", "solid sodium hydroxide pellets"])
    prompt = (
        f"Why must Grade 9 learners wear safety goggles and handle **{reagent}** only under teacher supervision, even though neutralisation products like $\\text{{NaCl}}$ are safe?"
    )
    correct = "Strong concentrated acids and alkalis are highly corrosive and rapidly damage eyes, skin, and clothing before neutralisation occurs."
    distractors = [
        "Only acids are corrosive; strong bases like NaOH are completely harmless like hand soap.",
        "Safety goggles are worn purely to protect indicator paper strips from splashes.",
        "Concentrated solutions emit invisible toxic argon gas at room temperature.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Both strong acids (pH ~0–1) and strong alkalis (pH ~13–14) are **corrosive** chemicals.\n"
        f"**Step 2:** Contact with **{reagent}** can cause instant severe tissue/eye injury, so protective goggles and supervision are mandatory [2]."
    )
    return _q(
        rng, "45", "45_corrosive_laboratory_acids_vs_strong_alkalis_handling", prompt, correct, sol, 2, "multiple_choice",
        ["bases_are_never_corrosive_myth"],
        "Evaluate whether danger applies only to low pH or to BOTH extremes of the pH scale.",
        "Extreme pH (<2 and >12) are both strongly corrosive -> wear goggles.",
        correct, options=options,
    )


def arch_46_red_cabbage_or_litmus_vs_universal_indicator_titration(rng: random.Random) -> Dict[str, Any]:
    alt_ind = rng.choice(["red litmus paper", "phenolphthalein", "bromothymol blue"])
    prompt = (
        f"Why is **universal indicator** generally preferred over **{alt_ind}** when monitoring the gradual pH shift step-by-step during an acid–base neutralisation investigation?"
    )
    correct = "Universal indicator displays a continuous spectrum of distinct colours for each pH unit from 0 to 14, whereas single-transition indicators only switch once at a narrow threshold."
    distractors = [
        "Universal indicator actually changes the acid into water on its own.",
        "Red litmus dissolves completely in bases and explodes in strong acids.",
        "Universal indicator stays pure green for all acidic and alkaline pH values.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** **{alt_ind.capitalize()}** only undergoes a sharp two-colour transition near a single threshold and cannot tell pH 1 from pH 5.\n"
        "**Step 2:** **Universal indicator** spans multiple colours across pH 0–14, letting learners track pH gradually approaching 7 [2]."
    )
    return _q(
        rng, "46", "46_red_cabbage_or_litmus_vs_universal_indicator_titration", prompt, correct, sol, 2, "multiple_choice",
        ["litmus_measures_exact_ph_number_myth"],
        "Compare narrow two-state indicators with full-spectrum pH indicators.",
        "Universal indicator shows distinct colours across pH 0 to 14.",
        correct, options=options,
    )


def arch_47_submicroscopic_particle_diagram_acid_base_exchange(rng: random.Random) -> Dict[str, Any]:
    cation, anion, salt = rng.choice([
        ("Na+", "Cl-", "sodium chloride (NaCl)"),
        ("K+", "Cl-", "potassium chloride (KCl)"),
        ("Na+", "Br-", "sodium bromide (NaBr)"),
    ])
    pairs = rng.choice([2, 3])
    spec = _svg_acid_base_particle_exchange(rng, pairs, cation, anion)
    prompt = (
        f"The submicroscopic particle diagram models an exact neutralisation involving **{pairs} units** of acid ($\\text{{H}}^+{anion}$) reacting with **{pairs} units** of metal hydroxide ($\\text{{{cation}OH}}^-$).\n\n"
        f"1. Name the dissolved ionic salt whose ions remain paired on the right-hand side [1].\n"
        f"2. State how many neutral water ($\\text{{H}}_2\\text{{O}}$) molecules form from {pairs} acid–hydroxide pairs, and explain why no $\\text{{H}}^+$ or $\\text{{OH}}^-$ remains uncombined [2]."
    )
    correct = f"{salt}; {pairs} water molecules form because each H+ pairs 1:1 with each OH-, conserving all atoms and leaving the mixture neutral (pH 7)"
    sol = (
        f"**Step 1:** The dissolved salt consists of **{cation}** and **{anion}** ions: **{salt}** [1].\n\n"
        f"**Step 2:** Each of the **{pairs} $\\text{{H}}^+$** ions bonds with an **$\\text{{OH}}^-$** ion to produce **{pairs} $\\text{{H}}_2\\text{{O}}$ molecules**, leaving zero excess acid or base (neutral pH 7) [2]."
    )
    return _q(
        rng, "47", "47_submicroscopic_particle_diagram_acid_base_exchange", prompt, correct, sol, 3, "structured",
        ["particle_conservation_broken_in_neutralisation_error"],
        "Count each H+ + OH- -> H2O pair across the reaction arrow.",
        f"{pairs} reactant pairs swap partners cleanly -> {pairs} water molecules + {salt}.",
        correct, diagram_spec=spec,
    )


def arch_48_atomic_conservation_count_check_for_neutralisation_equations(rng: random.Random) -> Dict[str, Any]:
    eq_case = rng.choice([
        ("2HCl + CaCO3 -> CaCl2 + H2O + CO2", {"H": 2, "Cl": 2, "Ca": 1, "C": 1, "O": 3}),
        ("2HCl + Mg(OH)2 -> MgCl2 + 2H2O", {"H": 4, "Cl": 2, "Mg": 1, "O": 2}),
        ("2HCl + Na2CO3 -> 2NaCl + H2O + CO2", {"H": 2, "Cl": 2, "Na": 2, "C": 1, "O": 3}),
    ])
    eq, counts = eq_case
    el = rng.choice(list(counts.keys()))
    n_el = counts[el]
    prompt = (
        f"Examine the neutralisation equation:\n$$\\text{{{eq}}}$$\n\n"
        f"Verify conservation of atoms by counting how many atoms of **{el}** appear on the **reactant (left)** side vs the **product (right)** side, and state whether the equation is balanced [2]."
    )
    correct = f"Balanced; {n_el} atoms of {el} on the left and {n_el} atoms of {el} on the right (identical counts for every element)"
    sol = (
        f"**Step 1:** Inspecting **${eq}$**: on the left there are **{n_el} {el} atom(s)**, and on the right there are **{n_el} {el} atom(s)** [1].\n\n"
        "**Step 2:** Every other element is also conserved across reactants and products, so the equation is **balanced** [1]."
    )
    return _q(
        rng, "48", "48_atomic_conservation_count_check_for_neutralisation_equations", prompt, correct, sol, 2, "short_answer",
        ["coefficient_applies_only_to_first_atom_error"],
        "Multiply coefficients in front of each formula by the atom's subscript.",
        f"Count {el} carefully on both left and right -> {n_el} = {n_el}.",
        correct,
    )


def arch_49_unknown_powder_identification_carbonate_vs_hydroxide_vs_oxide(rng: random.Random) -> Dict[str, Any]:
    mystery = rng.choice([
        ("Powder X", "dissolves with rapid colourless fizzing in HCl that turns limewater milky", "metal carbonate (e.g. CaCO3)"),
        ("Powder Y", "dissolves quietly in HCl with slight warming and zero gas bubbles, and turns water strongly alkaline (pH 13)", "soluble metal hydroxide / alkali (e.g. NaOH)"),
        ("Powder Z", "hardly dissolves in pure water, dissolves smoothly in warm HCl producing a blue-green CuCl2 solution with zero bubbles", "insoluble metal oxide (e.g. CuO)"),
    ])
    label, obs, identity = mystery
    prompt = (
        f"In an identification practical, an unlabelled sample (**{label}**) {obs}.\n\n"
        f"Classify **{label}** as a **metal oxide**, **metal hydroxide**, or **metal carbonate**, explaining how your diagnostic evidence rules out the other two classes [3]."
    )
    correct = f"{identity}; Reasoning matches solubility in water and presence/absence of CO2 effervescence with limewater test"
    sol = (
        f"**Step 1:** Classification: **{identity}** [1].\n\n"
        "**Step 2:** Evidence: carbonates uniquely fizz releasing **$\\text{CO}_2$** (milky limewater); soluble metal hydroxides form strongly alkaline aqueous solutions without bubbles; insoluble metal oxides react quietly with warm acid without evolving any gas [2]."
    )
    return _q(
        rng, "49", "49_unknown_powder_identification_carbonate_vs_hydroxide_vs_oxide", prompt, correct, sol, 3, "short_answer",
        ["failing_to_distinguish_oxide_hydroxide_carbonate_tests"],
        "Check two clues: (1) Are gas bubbles + milky limewater produced? (2) Does it dissolve readily in water?",
        f"Observe '{obs}' -> uniquely identifies a {identity}.",
        correct,
    )


def arch_50_acid_base_multi_reaction_concept_synthesis_classification(rng: random.Random) -> Dict[str, Any]:
    reaction_pairs = [
        ("2HCl + CaO -> CaCl2 + H2O", "Acid + Metal oxide"),
        ("HCl + NaOH -> NaCl + H2O", "Acid + Metal hydroxide"),
        ("2HCl + Na2CO3 -> 2NaCl + H2O + CO2", "Acid + Metal carbonate"),
        ("CO2 + H2O -> H2CO3", "Non-metal oxide dissolving in water (acidic rain/solution formation)"),
    ]
    eq, rtype = rng.choice(reaction_pairs)
    prompt = (
        f"Consider the balanced chemical equation below from Term 2 Matter and Materials:\n"
        f"$$\\text{{{eq}}}$$\n\n"
        "1. Classify the exact reaction pattern represented [1].\n"
        "2. State whether the right-hand ionic compound (if a salt is formed) or solution product contains neutralisation products or acid rain formation [2]."
    )
    correct = f"{rtype}; Correctly identifies products formed (salt + water [+ CO2] or aqueous carbonic acid)"
    sol = (
        f"**Step 1:** Reaction classification: **{rtype}** [1].\n\n"
        "**Step 2:** In metal-base neutralisations, protons combine with oxide/hydroxide/carbonate to yield **salt + water** (plus $\\text{CO}_2$ if carbonate); in $\\text{CO}_2 + \\text{H}_2\\text{O}$, a non-metal oxide hydrates to form an **acidic solution** [2]."
    )
    return _q(
        rng, "50", "50_acid_base_multi_reaction_concept_synthesis_classification", prompt, correct, sol, 3, "short_answer",
        ["confusing_nonmetal_oxide_hydration_with_neutralisation"],
        "Examine the second reactant carefully: water, metal oxide, metal hydroxide, or metal carbonate?",
        f"Match the reactant family in '{eq}' to {rtype}.",
        correct,
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_metal_carbonate_basic_character_in_aqueous_suspension": arch_26_metal_carbonate_basic_character_in_aqueous_suspension,
    "27_acid_plus_metal_carbonate_general_word_equation": arch_27_acid_plus_metal_carbonate_general_word_equation,
    "28_chalk_calcium_carbonate_hydrochloric_acid_effervescence": arch_28_chalk_calcium_carbonate_hydrochloric_acid_effervescence,
    "29_hydrochloric_acid_plus_calcium_carbonate_balanced_equation": arch_29_hydrochloric_acid_plus_calcium_carbonate_balanced_equation,
    "30_hydrochloric_acid_plus_sodium_carbonate_balanced_equation": arch_30_hydrochloric_acid_plus_sodium_carbonate_balanced_equation,
    "31_carbon_dioxide_density_pour_into_limewater_technique": arch_31_carbon_dioxide_density_pour_into_limewater_technique,
    "32_clear_limewater_cloudy_milky_precipitate_test": arch_32_clear_limewater_cloudy_milky_precipitate_test,
    "33_comparing_gas_evolution_oxides_hydroxides_vs_carbonates": arch_33_comparing_gas_evolution_oxides_hydroxides_vs_carbonates,
    "34_variables_control_and_ph_vs_acid_volume_graph_analysis": arch_34_variables_control_and_ph_vs_acid_volume_graph_analysis,
    "35_salt_naming_rule_from_parent_acid_hcl_h2so4_hno3": arch_35_salt_naming_rule_from_parent_acid_hcl_h2so4_hno3,
    "36_predicting_salt_formula_from_metal_valence_and_anion": arch_36_predicting_salt_formula_from_metal_valence_and_anion,
    "37_sulfuric_acid_neutralisation_with_metal_bases": arch_37_sulfuric_acid_neutralisation_with_metal_bases,
    "38_indigestion_heartburn_and_antacid_tablets": arch_38_indigestion_heartburn_and_antacid_tablets,
    "39_bee_sting_acidic_vs_wasp_sting_alkaline_remedies": arch_39_bee_sting_acidic_vs_wasp_sting_alkaline_remedies,
    "40_agricultural_soil_liming_with_calcium_carbonate_or_ash": arch_40_agricultural_soil_liming_with_calcium_carbonate_or_ash,
    "41_acid_mine_drainage_treatment_in_south_africa": arch_41_acid_mine_drainage_treatment_in_south_africa,
    "42_swimming_pool_ph_regulation_acid_and_soda_ash": arch_42_swimming_pool_ph_regulation_acid_and_soda_ash,
    "43_toothpaste_alkaline_neutralisation_of_plaque_acids": arch_43_toothpaste_alkaline_neutralisation_of_plaque_acids,
    "44_acid_spill_laboratory_safety_and_sodium_bicarbonate_neutralisation": arch_44_acid_spill_laboratory_safety_and_sodium_bicarbonate_neutralisation,
    "45_corrosive_laboratory_acids_vs_strong_alkalis_handling": arch_45_corrosive_laboratory_acids_vs_strong_alkalis_handling,
    "46_red_cabbage_or_litmus_vs_universal_indicator_titration": arch_46_red_cabbage_or_litmus_vs_universal_indicator_titration,
    "47_submicroscopic_particle_diagram_acid_base_exchange": arch_47_submicroscopic_particle_diagram_acid_base_exchange,
    "48_atomic_conservation_count_check_for_neutralisation_equations": arch_48_atomic_conservation_count_check_for_neutralisation_equations,
    "49_unknown_powder_identification_carbonate_vs_hydroxide_vs_oxide": arch_49_unknown_powder_identification_carbonate_vs_hydroxide_vs_oxide,
    "50_acid_base_multi_reaction_concept_synthesis_classification": arch_50_acid_base_multi_reaction_concept_synthesis_classification,
}
