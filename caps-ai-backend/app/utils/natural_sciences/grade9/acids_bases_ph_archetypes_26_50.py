"""Grade 9 Natural Sciences - Acids, Bases and the pH Value: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/04. Acids bases and the pH value.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .acids_bases_ph_archetypes_01_25 import _q


def arch_26_agricultural_soil_ph_testing_and_crop_preferences(rng: random.Random) -> Dict[str, Any]:
    crop_case = rng.choice([
        ("Mpumalanga blueberries / proteas", "prefer acidic soil (pH 4,8–5,5)", "too alkaline at pH 7,8 -> lowers iron nutrient absorption causing yellow chlorotic leaves"),
        ("Free State maize / lucerne pasture", "thrive best near pH 6,2–7,0", "acidified down to pH 4,6 -> damages root bacteria and locks out phosphorus"),
    ])
    crop, pref, issue = crop_case
    prompt = (
        f"Commercial farmers growing **{crop}** regularly measure topsoil pH before planting.\n"
        f"This crop is known to **{pref}**.\n\n"
        f"Explain what agricultural problem develops when soil is **{issue.split(' -> ')[0]}**, and name the general type of soil conditioner needed [2]."
    )
    correct = f"Soil outside optimal range reduces mineral availability ({issue.split(' -> ')[1]}); Add agricultural lime (base) if overly acidic or compost/sulfur amendment if overly alkaline."
    sol = (
        f"**Step 1:** Outside its optimal pH band, nutrient solubility alters sharply (**{issue}** ) [1].\n\n"
        "**Step 2:** Acidic soils are adjusted upward with basic **agricultural lime**, whereas alkaline soils are gently acidified using elemental sulfur/organic compost [1]."
    )
    return _q(
        rng, "26", "26_agricultural_soil_ph_testing_and_crop_preferences", prompt, correct, sol, 2, "short_answer",
        ["soil_ph_crop_nutrition_error"],
        "Soil pH controls how cleanly roots absorb minerals like iron and phosphorus.",
        f"{issue}; adjust with base (lime) or acidifying sulfur.",
        correct,
    )


def arch_27_biological_human_body_ph_compartment_variation(rng: random.Random) -> Dict[str, Any]:
    organ, ph_v, role = rng.choice([
        ("Human stomach gastric juice", "pH 1,5–2,0 (strongly acidic)", "kills swallowed pathogens and activates pepsin enzyme to digest proteins"),
        ("Healthy human arterial blood plasma", "pH 7,35–7,45 (tightly regulated slightly alkaline)", "maintains enzyme folding and oxygen transport"),
        ("Human skin acid mantle", "pH ~5,5 (mildly acidic)", "inhibits harmful skin bacteria while protecting lipid moisture barrier"),
        ("Small intestine pancreatic fluid", "pH ~7,8–8,2 (weakly basic)", "neutralises stomach acid chyme and activates digestive enzymes"),
    ])
    prompt = (
        f"Inside the human body, **{organ}** maintains a strict physiological pH of **{ph_v}**.\n\n"
        f"Explain why {organ.lower()} requires this exact pH range instead of uniform pH 7 everywhere [2]."
    )
    correct = f"{organ} needs {ph_v} specifically because it {role}."
    sol = f"**Step 1 & 2:** Biological enzymes and barriers are compartment-tuned: {organ} operates at **{ph_v}** so it **{role}** [2]."
    return _q(
        rng, "27", "27_biological_human_body_ph_compartment_variation", prompt, correct, sol, 2, "short_answer",
        ["body_fluids_all_ph7_myth"],
        "Think about the biological function of that organ or fluid.",
        f"{organ}: {ph_v} -> {role}.",
        correct,
    )


def arch_28_hair_shampoo_ph_5_5_and_cuticle_chemistry(rng: random.Random) -> Dict[str, Any]:
    ph_shamp = rng.choice(["5,5", "5,4", "5,6"])
    prompt = (
        f"A cosmetic label on gentle conditioning shampoo highlights **\"pH Balanced: pH {ph_shamp}\"**.\n\n"
        "1. Is pH 5,5 mildly acidic, neutral, or mildly basic? [1]\n"
        "2. Explain why mildly acidic shampoo leaves hair smoother and shinier than strongly alkaline soap (pH 10) [2]."
    )
    correct = f"Mildly acidic (below pH 7); Mildly acidic pH {ph_shamp} matches natural hair/scalp oils and keeps microscopic keratin hair cuticles tightly flat, whereas harsh alkaline soaps swell cuticles causing tangles and frizz."
    sol = (
        f"**Step 1:** Because {ph_shamp} < 7,0, the shampoo is **mildly acidic** [1].\n\n"
        "**Step 2:** Mildly acidic shampoos mirror the scalp's natural mantle (~5,5), laying outer **hair cuticles flat** for shine, whereas high-alkali soaps lift cuticles and dry out hair [2]."
    )
    return _q(
        rng, "28", "28_hair_shampoo_ph_5_5_and_cuticle_chemistry", prompt, correct, sol, 3, "structured",
        ["ph_balanced_means_exactly_7_myth"],
        "Remember 'pH balanced' for hair/skin matches ~5,5, NOT strictly pH 7.",
        f"pH {ph_shamp} = mildly acidic, keeping hair cuticles flat and smooth.",
        correct,
    )


def arch_29_bases_vs_alkalis_solubility_distinction(rng: random.Random) -> Dict[str, Any]:
    pair_chem = rng.choice([
        ("Sodium hydroxide (NaOH) vs Copper(II) oxide (CuO)", "NaOH dissolves easily (an alkali); CuO does not dissolve in water (an insoluble base)"),
        ("Potassium hydroxide (KOH) vs Iron(III) oxide (Fe2O3)", "KOH is water-soluble (an alkali); Fe2O3 is insoluble in water (an insoluble base)"),
    ])
    pair_name, exp = pair_chem
    prompt = (
        f"Compare **{pair_name}**.\n\n"
        "1. Define the precise distinction between a **base** and an **alkali** [2].\n"
        f"2. Identify which compound in the pair is an alkali and which is strictly an insoluble base [1]."
    )
    correct = f"A base is any substance that neutralises an acid (metal oxides, hydroxides, carbonates); An alkali is specifically a soluble base dissolved in water; {exp}."
    sol = (
        "**Step 1:** Every **alkali** is a **water-soluble base** (forming $OH^-$ ions in aqueous solution), whereas many metal oxides/carbonates are **insoluble bases** [2].\n\n"
        f"**Step 2:** In this pair: **{exp}** [1]."
    )
    return _q(
        rng, "29", "29_bases_vs_alkalis_solubility_distinction", prompt, correct, sol, 3, "structured",
        ["all_bases_are_soluble_alkalis_myth"],
        "Think of subsets: 'All alkalis are bases, but not all bases dissolve in water.'",
        f"Alkali = soluble base. {exp}.",
        correct,
    )


def arch_30_non_edible_safety_rule_never_taste_unknown_chemicals(rng: random.Random) -> Dict[str, Any]:
    beaker_desc = rng.choice(["clear colourless liquid on a lab bench", "white powder inside a mystery lab vial"])
    prompt = (
        f"Knowing that acids taste sour and bases taste bitter, a careless learner suggests tasting a drop of an unlabelled **{beaker_desc}** to identify it.\n\n"
        "Why is tasting NEVER allowed in science laboratories, and what safe testing sequence must be followed instead? [2]"
    )
    correct = "Unknown laboratory chemicals may be intensely corrosive (causing permanent tongue/oesophagus burns) or lethal poisons even in tiny drops; Instead test safely using acid-base indicators (litmus/Universal Indicator) or calibrated pH meters while wearing goggles."
    sol = (
        "**Step 1:** Concentrated acids, caustic alkalis, and toxic laboratory reagents can **burn mucous membranes or poison fatally** on ingestion [1].\n\n"
        "**Step 2:** Always identify acidity/basicity chemically via **litmus strips, Universal Indicator, or a digital pH meter**—never by tasting or smelling directly [1]."
    )
    return _q(
        rng, "30", "30_non_edible_safety_rule_never_taste_unknown_chemicals", prompt, correct, sol, 2, "short_answer",
        ["tasting_lab_chemicals_hazard"],
        "Sour/bitter properties refer to known foods only; never test chemicals orally.",
        "Poison/corrosive burn hazard -> always test safely with indicators/pH meter.",
        correct,
    )


def arch_31_golden_dilution_rule_acid_into_water_exothermic(rng: random.Random) -> Dict[str, Any]:
    acid_c = rng.choice(["concentrated sulfuric acid (H2SO4)", "concentrated hydrochloric acid (HCl)"])
    prompt = (
        f"A lab technician needs to prepare dilute solution starting from **{acid_c}** and cold distilled water.\n\n"
        "State the **golden safety rule for diluting concentrated acid**, and explain thermodynamically what happens if performed in reverse [3]."
    )
    correct = "ALWAYS add concentrated acid slowly to water (never pour water into concentrated acid); Acid dissolution is strongly exothermic, so pouring small water droplets onto dense acid flashes the water into steam causing violent boiling and splashing concentrated acid out."
    sol = (
        "**Step 1:** Golden rule: **Always add acid slowly to water** while stirring gently (*\"Do as you oughta, add acid to water\"*) [1].\n\n"
        "**Step 2:** Mixing acid and water is intensely **exothermic** [1]. Water floats atop denser acid and flashes into **superheated steam**, violently splattering concentrated acid across face and hands if poured in reverse [1]."
    )
    return _q(
        rng, "31", "31_golden_dilution_rule_acid_into_water_exothermic", prompt, correct, sol, 3, "structured",
        ["water_to_acid_is_safe_myth"],
        "Think about the large heat released (exothermic) and whether acid or water is denser.",
        "Always add ACID into WATER slowly; reverse flashes water to steam and splatters boiling acid.",
        correct,
    )


def arch_32_sulfuric_acid_dehydrating_sugar_skin_hazard(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice(["cotton lab-coat sleeve cellulose", "white table sugar sucrose", "unprotected skin tissue"])
    prompt = (
        f"Why does accidental contact with concentrated sulfuric acid ($\\text{{H}}_2\\text{{SO}}_4$) turn **{target}** rapidly black and charred even without an open fire?\n\n"
        "Identify the additional chemical hazard property of concentrated $\\text{H}_2\\text{SO}_4$ alongside its low pH [2]."
    )
    correct = "Concentrated sulfuric acid is a powerful exothermic dehydrating agent that aggressively strips chemically bound water (H and O atoms) out of carbohydrates/proteins, leaving black carbon char."
    sol = (
        f"**Step 1:** Concentrated $\\text{{H}}_2\\text{{SO}}_4$ acts as a ferocious **dehydrating agent**, tearing H and O atoms in a 2:1 water ratio out of organic **{target}** [1].\n\n"
        "**Step 2:** Removing water elements leaves elemental **black carbon charring** alongside severe exothermic thermal chemical burns [1]."
    )
    return _q(
        rng, "32", "32_sulfuric_acid_dehydrating_sugar_skin_hazard", prompt, correct, sol, 2, "short_answer",
        ["sulfuric_acid_charring_confusion"],
        "Besides releasing H+ ions, concentrated H2SO4 loves water so fiercely it rips H2O out of molecules.",
        "Powerful exothermic dehydrating agent leaving black carbon char.",
        correct,
    )


def arch_33_essential_laboratory_ppe_goggles_coat_gloves(rng: random.Random) -> Dict[str, Any]:
    task = rng.choice(["pouring 2 M hydrochloric acid", "dissolving caustic sodium hydroxide pellets"])
    prompt = (
        f"Before beginning a Grade 9 practical **{task}**, learners assemble mandatory **Personal Protective Equipment (PPE)**.\n\n"
        "List **three essential PPE items** and match each item to the exact anatomical hazard it protects against [3]."
    )
    correct = "1. Chemical splash safety goggles (protects sensitive eye corneas from permanent blindness); 2. Lab coat / apron (protects torso skin and uniform from corrosive holes); 3. Chemical-resistant nitrile gloves (shields hands from burns)."
    sol = (
        "**Step 1:** **Safety goggles** shield eyes from droplets/splashes causing corneal blindness [1].\n\n"
        "**Step 2:** **Lab coat / apron** protects skin and clothes from corrosive holes [1].\n\n"
        "**Step 3:** **Nitrile/rubber gloves** (plus closed-toe shoes) prevent skin burns on fingers and feet [1]."
    )
    return _q(
        rng, "33", "33_essential_laboratory_ppe_goggles_coat_gloves", prompt, correct, sol, 3, "structured",
        ["ppe_protection_rationale_omission"],
        "Protect eyes first, then torso/clothes, then hands/feet.",
        "Goggles (eyes), Lab coat (body/clothes), Gloves (hands).",
        correct,
    )


def arch_34_emergency_chemical_splash_skin_and_eye_first_aid(rng: random.Random) -> Dict[str, Any]:
    chem = rng.choice(["dilute hydrochloric acid", "concentrated sodium hydroxide alkali"])
    prompt = (
        f"A learner accidentally splashes several drops of **{chem}** onto their bare forearm.\n\n"
        "1. State the **immediate emergency first-aid response** [1].\n"
        "2. Explain why you must **NOT** pour strong base (or strong acid) straight onto the skin burn to \"neutralise\" it [2]."
    )
    correct = "Immediately flush continuously under cold running tap water for 15–20 minutes and alert the educator; Never pour a neutralising reagent on skin because neutralisation is exothermic and releases extra burn heat while risking over-neutralisation burn."
    sol = (
        "**Step 1:** Immediately place the affected limb under **continuous cool running water for 15–20 minutes** (or emergency eye-wash if near face) to dilute and wash away every trace [1].\n\n"
        "**Step 2:** Do NOT attempt chemical neutralisation on bare skin—acid-base neutralisation releases **exothermic heat** that deepens tissue burns and risks replacing an acid burn with an alkali burn [2]."
    )
    return _q(
        rng, "34", "34_emergency_chemical_splash_skin_and_eye_first_aid", prompt, correct, sol, 3, "structured",
        ["neutralize_acid_burns_with_strong_base_myth"],
        "Water dilutes and cools harmlessly; strong chemicals react exothermically on skin.",
        "Flush 15–20 min with cool running water; NEVER add opposite strong chemical on skin.",
        correct,
    )


def arch_35_concentration_vs_strength_careful_distinction(rng: random.Random) -> Dict[str, Any]:
    comp = rng.choice([
        ("0,01 M hydrochloric acid (very dilute strong acid)", "4,0 M ethanoic acid vinegar (concentrated weak acid)"),
        ("dilute laboratory sulfuric acid", "glacial concentrated vinegar"),
    ])
    strong_dil, weak_conc = comp
    prompt = (
        "Grade 9 students often confuse **acid strength** with **solution concentration**.\n\n"
        f"Distinguish between **{strong_dil}** and **{weak_conc}** by defining **strong vs weak** (ionisation extent) versus **dilute vs concentrated** (amount of solute per litre) [3]."
    )
    correct = "Strength describes what fraction of acid molecules split/ionise into H+ ions in water (HCl = strong, 100%; ethanoic = weak, partial); Concentration measures total solute dissolved per volume of water (dilute = low moles/litre; concentrated = high moles/litre)."
    sol = (
        "**Step 1:** **Strength** is fixed by molecular nature: strong acids (e.g. HCl) ionise almost completely in water, whereas weak acids (ethanoic acid) only partially ionise [2].\n\n"
        "**Step 2:** **Concentration** refers purely to how much solute is dissolved per unit volume of water—so you can have a dilute strong acid or a concentrated weak acid [1]."
    )
    return _q(
        rng, "35", "35_concentration_vs_strength_careful_distinction", prompt, correct, sol, 3, "structured",
        ["strong_acid_equals_concentrated_myth"],
        "Ask: Is 'weak vs strong' about molecular splitting, and 'dilute vs concentrated' about water ratio?",
        "Strength = ionisation %; Concentration = solute amount per volume.",
        correct,
    )


def arch_36_combining_multiple_indicators_unknown_solution_deduction(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        ("Sample P", "Blue litmus -> Red", "Bromothymol blue -> Yellow", "Phenolphthalein -> Colourless", "Acidic (pH < 6,0)", "#dc2626", "#facc15", "#e2e8f0"),
        ("Sample Q", "Red litmus -> Red (no change)", "Bromothymol blue -> Green", "Phenolphthalein -> Colourless", "Neutral (pH ~ 7,0)", "#ef4444", "#16a34a", "#e2e8f0"),
        ("Sample R", "Red litmus -> Blue", "Bromothymol blue -> Blue", "Phenolphthalein -> Bright Pink", "Basic / Alkaline (pH > 8,2)", "#2563eb", "#2563eb", "#ec4899"),
    ])
    s_name, l_txt, b_txt, p_txt, verdict, c1, c2, c3 = scenario
    svg = (
        f'<svg viewBox="0 0 380 140" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="20" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">White Ceramic Spot Plate Test: {s_name}</text>'
        f'<circle cx="75" cy="70" r="24" fill="{c1}" stroke="#475569" stroke-width="1.5"/>'
        f'<text x="75" y="108" font-size="8" font-weight="bold" fill="#334155" text-anchor="middle">Litmus</text>'
        f'<text x="75" y="122" font-size="7.5" fill="#475569" text-anchor="middle">{l_txt}</text>'
        f'<circle cx="190" cy="70" r="24" fill="{c2}" stroke="#475569" stroke-width="1.5"/>'
        f'<text x="190" y="108" font-size="8" font-weight="bold" fill="#334155" text-anchor="middle">Bromothymol</text>'
        f'<text x="190" y="122" font-size="7.5" fill="#475569" text-anchor="middle">{b_txt.split("-> ")[1]}</text>'
        f'<circle cx="305" cy="70" r="24" fill="{c3}" stroke="#475569" stroke-width="1.5"/>'
        f'<text x="305" y="108" font-size="8" font-weight="bold" fill="#334155" text-anchor="middle">Phenolphthalein</text>'
        f'<text x="305" y="122" font-size="7.5" fill="#475569" text-anchor="middle">{p_txt.split("-> ")[1]}</text>'
        f'</svg>'
    )
    prompt = (
        f"Inspect the spot-plate test results for **{s_name}** across three separate chemical indicators:\n"
        f"- {l_txt}\n- {b_txt}\n- {p_txt}\n\n"
        f"Deduce whether **{s_name}** is acidic, neutral, or basic (alkaline), justifying from ALL three tests [3]."
    )
    correct = f"{verdict}; Confirmed consistently by all three tests ({l_txt}; {b_txt}; {p_txt})."
    sol = (
        f"**Step 1:** {l_txt} narrows the nature; {b_txt} distinguishes acidic/neutral/basic cleanly; {p_txt} confirms whether pH exceeds 8,2 [2].\n\n"
        f"**Step 2:** Unambiguous deduction: **{s_name}** is **{verdict}** [1]."
    )
    return _q(
        rng, "36", "36_combining_multiple_indicators_unknown_solution_deduction", prompt, correct, sol, 3, "structured",
        ["multi_indicator_logic_error"],
        "Cross-check all three spot colours against Bromothymol (Y/G/B) and Phenolphthalein (Clear/Pink).",
        f"Deduction: {verdict}.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_37_strong_acid_dilution_ph_rise_toward_7(rng: random.Random) -> Dict[str, Any]:
    start_ph = rng.choice(["1,0", "1,5", "2,0"])
    prompt = (
        f"A learner measures **10 mL** of hydrochloric acid at **pH {start_ph}**, then slowly adds **990 mL** of pure distilled water (pH 7,0).\n\n"
        "Predict whether the solution pH rises, drops, or turns alkaline (> 7), and explain why [2]."
    )
    correct = "The pH rises upward toward 7 (around pH 3–4) because diluting lowers H+ concentration, yet it NEVER exceeds pH 7 (pure water cannot turn an acid into a base)."
    options = [
        correct,
        "Adding so much neutral water crosses pH 7 and turns the flask strongly alkaline (pH 10).",
        "The pH drops down below zero to pH -2 because water multiplies acidity.",
        "Adding pure water leaves the exact pH unchanged forever.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Diluting acid spreads existing $H^+$ ions over 100× more volume, raising pH closer to neutral 7.\n"
        "**Step 2:** Because pure water contains no excess hydroxide base, the mixture stays acidic below 7,0 asymptote [2]."
    )
    return _q(
        rng, "37", "37_strong_acid_dilution_ph_rise_toward_7", prompt, correct, sol, 2, "multiple_choice",
        ["diluting_acid_makes_base_myth"],
        "Can adding neutral pH 7 water turn an acid into a basic alkali?",
        "pH rises toward 7,0 but stays acidic (< 7).",
        correct, options=options,
    )


def arch_38_strong_base_dilution_ph_drop_toward_7(rng: random.Random) -> Dict[str, Any]:
    start_ph = rng.choice(["13,0", "12,5", "13,5"])
    prompt = (
        f"A technician adds **500 mL** of pure distilled water into **50 mL** of sodium hydroxide solution initially at **pH {start_ph}**.\n\n"
        "State how the pH reading changes and state its mathematical limit if diluted infinitely with pure water [2]."
    )
    correct = "pH decreases downward toward 7,0 as OH- ions spread out in larger volume; Asymptotic limit is pH 7,0 (stays basic >= 7, never turns acidic)."
    sol = (
        "**Step 1:** Diluting lowers hydroxide ($OH^-$) concentration, so the alkaline pH **drops toward 7,0** [1].\n\n"
        "**Step 2:** No matter how much pure water is added, pH approaches **7,0** as a lower boundary and never crosses below 7 into acidity [1]."
    )
    return _q(
        rng, "38", "38_strong_base_dilution_ph_drop_toward_7", prompt, correct, sol, 2, "short_answer",
        ["diluting_base_makes_acid_myth"],
        "Adding neutral pH 7 water moves any extreme pH back toward 7 without crossing it.",
        "Base pH drops toward 7,0 limit without ever crossing < 7.",
        correct,
    )


def arch_39_neutral_salt_solutions_nacl_vs_distilled_water_ph(rng: random.Random) -> Dict[str, Any]:
    salt = rng.choice(["pure sodium chloride (table salt, NaCl)", "potassium nitrate (KNO3)"])
    prompt = (
        f"A learner dissolves a teaspoon of **{salt}** into neutral distilled water and tests the clear saltwater using Universal Indicator.\n\n"
        "Predict the indicator colour and pH value, correcting the common mistake that 'every chemical makes pH leave 7' [2]."
    )
    correct = "Green colour (pH 7,0 neutral); Neutral salts formed from strong acid + strong base maintain exact H+ = OH- balance so pH stays 7,0."
    sol = (
        f"**Step 1:** **{salt}** is a neutral ionic salt; dissolving it keeps water's $H^+ = OH^-$ balance undisturbed [1].\n\n"
        "**Step 2:** Therefore the solution stays **neutral at pH 7,0**, displaying **green** in Universal Indicator [1]."
    )
    return _q(
        rng, "39", "39_neutral_salt_solutions_nacl_vs_distilled_water_ph", prompt, correct, sol, 2, "short_answer",
        ["table_salt_water_acidic_myth"],
        "Is table salt (NaCl) acidic, basic, or neutral?",
        "Neutral salt -> Green (pH 7,0).",
        correct,
    )


def arch_40_carbonated_soft_drink_vs_milk_vs_coffee_acidity_comparison(rng: random.Random) -> Dict[str, Any]:
    bev = rng.choice([
        ("Cola fizzy soft drink (pH ~2,6)", "Black filter coffee (pH ~5,0)", "Cola (~2,6) is over 100x more acidic and accelerates tooth enamel erosion"),
        ("Fresh cow's milk (pH ~6,6)", "Sour fermented amasi / yogurt (pH ~4,4)", "Fermented amasi (~4,4) has higher lactic acid acidity, turning blue litmus red"),
    ])
    b1, b2, insight = bev
    prompt = (
        f"Compare two common refrigerator beverages: **{b1}** vs **{b2}**.\n\n"
        "State which beverage sits closer to strong acidity on the pH scale and explain one everyday effect of that acidity [2]."
    )
    correct = insight
    sol = (
        f"**Step 1 & 2:** Checking pH position (< 7 acidic): **{insight}** [2]."
    )
    return _q(
        rng, "40", "40_carbonated_soft_drink_vs_milk_vs_coffee_acidity_comparison", prompt, correct, sol, 2, "short_answer",
        ["beverage_ph_comparison_error"],
        "Remember lower pH = higher acidity.",
        insight,
        correct,
    )


def arch_41_testing_solids_requires_dissolving_in_distilled_water(rng: random.Random) -> Dict[str, Any]:
    solid = rng.choice(["dry white citric acid crystals", "dry solid baking soda powder (NaHCO3)"])
    prompt = (
        f"A student presses completely **dry** red and blue litmus strips onto a dry pile of **{solid}** on a dry saucer, and neither paper changes colour!\n\n"
        "Explain why dry solids fail to trigger dry litmus paper, and state the missing laboratory preparation step [2]."
    )
    correct = "pH requires mobile H+ or OH- ions dissolved in aqueous water; Dissolve a small pinch of the solid in pure distilled water (or dampen the litmus strip with distilled water) before testing."
    sol = (
        "**Step 1:** Solid ionic/acid crystals trap molecules rigidly so free **$H^+$ or $OH^-$ ions cannot move** to react with the indicator dye [1].\n\n"
        "**Step 2:** Always **dissolve the solid in distilled water** (or use distilled-water moistened paper) so ions ionise and flow freely [1]."
    )
    return _q(
        rng, "41", "41_testing_solids_requires_dissolving_in_distilled_water", prompt, correct, sol, 2, "short_answer",
        ["dry_solids_test_with_dry_litmus_error"],
        "What does 'aqueous' (pH measurement of aqueous solutions) actually require?",
        "Dissolve in distilled water so H+/OH- ions become mobile.",
        correct,
    )


def arch_42_universal_indicator_paper_dipping_spot_tile_technique(rng: random.Random) -> Dict[str, Any]:
    bad_action = rng.choice(["dips the entire roll of Universal Indicator paper into the stock acid bottle", "uses the same unwashed dropper between vinegar and baking soda"])
    prompt = (
        f"During an indicator practical, a learner **{bad_action}**.\n\n"
        "Identify why this violates good laboratory technique and state the proper white-tile dropper procedure [2]."
    )
    correct = "Direct immersion contaminates the entire stock bottle/reagent strip with dyes and acid/base impurities; Always place short 1 cm paper strips on a clean white tile and transfer one drop using a clean rinsed glass rod or dedicated dropper."
    sol = (
        "**Step 1:** Dipping stock paper/unrinsed droppers cross-contaminates reagents and corrupts subsequent pH measurements [1].\n\n"
        "**Step 2:** Cut **1 cm indicator strips onto a clean white ceramic tile**, touching **one clean drop** per solution with a rinsed glass rod/dropper [1]."
    )
    return _q(
        rng, "42", "42_universal_indicator_paper_dipping_spot_tile_technique", prompt, correct, sol, 2, "short_answer",
        ["reagent_bottle_contamination_error"],
        "How do you prevent contaminating a whole stock bottle when testing pH?",
        "Transfer 1 drop via rinsed rod/dropper onto 1 cm strips on a white tile.",
        correct,
    )


def arch_43_reading_swimming_pool_comparator_color_chart(rng: random.Random) -> Dict[str, Any]:
    sample_case = rng.choice([
        ("6,6 (Yellow-Orange)", "#f59e0b", "Too low/acidic; add basic soda ash (Na2CO3) to raise toward 7,4"),
        ("7,4 (Coral Red)", "#ef4444", "Optimal balanced swimming pool pH; no pH chemical adjustment needed"),
        ("8,2 (Bright Magenta-Purple)", "#c026d3", "Too high/alkaline; add measured hydrochloric pool acid to lower toward 7,4"),
    ])
    lbl, s_col, action = sample_case
    svg = (
        f'<svg viewBox="0 0 360 135" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="360" height="135" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="180" y="18" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Pool Water Phenol-Red Comparator Kit</text>'
        f'<rect x="35" y="34" width="46" height="62" rx="4" fill="#f59e0b"/><text x="58" y="112" font-size="8" fill="#334155" text-anchor="middle">6,6</text>'
        f'<rect x="95" y="34" width="46" height="62" rx="4" fill="#fb923c"/><text x="118" y="112" font-size="8" fill="#334155" text-anchor="middle">7,0</text>'
        f'<rect x="155" y="34" width="46" height="62" rx="4" fill="#ef4444"/><text x="178" y="112" font-size="8" fill="#16a34a" font-weight="bold" text-anchor="middle">7,4 Ideal</text>'
        f'<rect x="215" y="34" width="46" height="62" rx="4" fill="#c026d3"/><text x="238" y="112" font-size="8" fill="#334155" text-anchor="middle">8,2</text>'
        f'<rect x="285" y="34" width="52" height="62" rx="4" fill="{s_col}" stroke="#0f172a" stroke-width="2.5"/>'
        f'<text x="311" y="112" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Sample</text>'
        f'</svg>'
    )
    prompt = (
        "Examine the swimming pool phenol-red comparator kit showing four calibrated colour blocks alongside the **Sample** tube.\n\n"
        "1. Read the closest pH value matching the **Sample** tube [1].\n"
        "2. State whether the water is ideal, too acidic, or too alkaline, and recommend the right chemical adjustment [2]."
    )
    correct = f"Closest match: pH {lbl}; {action}."
    sol = (
        f"**Step 1:** Matching the rightmost Sample block to the standard blocks gives **pH {lbl}** [1].\n\n"
        f"**Step 2:** {action} [2]."
    )
    return _q(
        rng, "43", "43_reading_swimming_pool_comparator_color_chart", prompt, correct, sol, 3, "structured",
        ["pool_comparator_chart_reading_error"],
        "Compare the colour of the outlined 'Sample' tube to 6,6 / 7,0 / 7,4 / 8,2.",
        f"Sample matches {lbl}: {action}.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_44_toothpaste_alkaline_mouth_ph_protection(rng: random.Random) -> Dict[str, Any]:
    snack = rng.choice(["sweet cooldrink and toffees", "sugary biscuits before bed"])
    prompt = (
        f"After eating **{snack}**, mouth bacteria convert sugar into organic **lactic acid**, dropping saliva pH down to ~**5,2**.\n\n"
        "1. Explain why brushing with mildly **alkaline toothpaste (pH ~8,5)** protects tooth enamel [2].\n"
        "2. State what happens to calcium-based enamel if mouth pH stays below 5,5 overnight [1]."
    )
    correct = "Mildly alkaline toothpaste neutralises bacterial acids in plaque, raising mouth pH safely back to ~7; Below pH 5,5, acid demineralises and dissolves outer tooth enamel causing cavities."
    sol = (
        "**Step 1:** Toothpaste contains mild bases (e.g. calcium carbonate, mild alkaline buffers) that **neutralise bacterial lactic acid** back to harmless neutral pH [2].\n\n"
        "**Step 2:** Leaving acid below pH 5,5 overnight **dissolves enamel mineral crystals**, producing dental cavities [1]."
    )
    return _q(
        rng, "44", "44_toothpaste_alkaline_mouth_ph_protection", prompt, correct, sol, 3, "structured",
        ["toothpaste_acidic_myth"],
        "Think about neutralisation: acid from plaque bacteria vs mild alkaline toothpaste.",
        "Alkaline toothpaste neutralises mouth acids above pH 5,5 enamel-erosion threshold.",
        correct,
    )


def arch_45_acidic_cleansers_vinegar_vs_alkaline_bleach_kitchen_safety(rng: random.Random) -> Dict[str, Any]:
    chore = rng.choice([
        ("removing chalky white calcium carbonate limescale inside an electric kettle", "Weak acid (vinegar / lemon citric acid)", "acids dissolve carbonate limescale into soluble salt + CO2 bubbles"),
        ("dissolving oily grease buildup on a kitchen oven tray", "Alkaline cleaner (soap / ammonia / caustic baking soda)", "bases react with fats/oils to emulsify and lift grease cleanly"),
    ])
    task, agent, reason = chore
    prompt = (
        f"For **{task}**, state whether an **acidic** or **alkaline** household cleaner works best, name an example, and explain why (**and warn never to mix bleach with acidic cleaners**) [3]."
    )
    correct = f"{agent} works best because {reason}; NEVER mix chlorine bleach with acidic cleaners because the reaction releases deadly toxic chlorine gas (Cl2)."
    sol = (
        f"**Step 1:** Choose **{agent}** because **{reason}** [2].\n\n"
        "**Step 2:** **Critical kitchen rule:** mixing sodium hypochlorite **bleach with acids** (like vinegar or toilet descaler) liberates toxic **chlorine gas** [1]."
    )
    return _q(
        rng, "45", "45_acidic_cleansers_vinegar_vs_alkaline_bleach_kitchen_safety", prompt, correct, sol, 3, "structured",
        ["mixing_bleach_and_acid_safety_error"],
        "Think: carbonates dissolve in acid, grease cuts in base; bleach + acid = toxic gas!",
        f"{agent}; NEVER mix bleach + acid (releases Cl2 gas).",
        correct,
    )


def arch_46_constructing_ph_data_table_and_axis_variable_selection(rng: random.Random) -> Dict[str, Any]:
    exp_case = rng.choice([
        ("recording pH as teaspoons of vinegar are stirred incrementally into 25 mL baking soda water",
         "Number of teaspoons of vinegar added (x-axis)", "pH of mixture measured on probe (y-axis)"),
        ("recording pH across five fruit juices diluted to different water volumes",
         "Volume of distilled water added (x-axis)", "Solution pH reading (y-axis)"),
    ])
    desc, ind_v, dep_v = exp_case
    prompt = (
        f"A Grade 9 group conducts an experiment **{desc}** and prepares to plot a line graph.\n\n"
        "State which quantity goes on the **horizontal x-axis** (independent variable) and which goes on the **vertical y-axis** (dependent variable) [2]."
    )
    correct = f"Horizontal x-axis (independent): {ind_v}; Vertical y-axis (dependent): {dep_v}."
    sol = (
        "**Step 1:** Standard graphing convention puts the deliberately changed **independent variable** on the **x-axis** and the responding **dependent measurement** on the **y-axis** [1].\n\n"
        f"**Step 2:** Plot **{ind_v}** vs **{dep_v}** [1]."
    )
    return _q(
        rng, "46", "46_constructing_ph_data_table_and_axis_variable_selection", prompt, correct, sol, 2, "short_answer",
        ["graph_axes_independent_dependent_swap"],
        "Remember MIX / DRY: Manipulated Independent on X-axis; Dependent Responding on Y-axis.",
        f"x-axis: {ind_v}; y-axis: {dep_v}.",
        correct,
    )


def arch_47_bar_graph_soil_ph_remediation_or_stream_monitoring(rng: random.Random) -> Dict[str, Any]:
    p_a = rng.choice([4.4, 4.6])
    p_b = rng.choice([5.5, 5.7])
    p_c = rng.choice([6.8, 7.0])
    p_d = rng.choice([8.5, 8.7])
    bars = [
        ("Plot A (Bog)", p_a, "#dc2626"),
        ("Plot B (Pine)", p_b, "#eab308"),
        ("Plot C (Maize)", p_c, "#16a34a"),
        ("Plot D (Alkali)", p_d, "#2563eb"),
    ]
    bar_svg = ""
    for i, (lbl, val, col) in enumerate(bars):
        h = int((val / 10.0) * 86)
        x = 50 + i * 78
        y = 122 - h
        vs = str(val).replace(".", ",")
        bar_svg += (
            f'<rect x="{x}" y="{y}" width="38" height="{h}" fill="{col}" rx="2"/>'
            f'<text x="{x+19}" y="{y-4}" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">{vs}</text>'
            f'<text x="{x+19}" y="135" font-size="7" fill="#334155" text-anchor="middle">{lbl}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 380 155" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="155" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="18" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Measured Soil pH Across Four Farm Plots</text>'
        f'<line x1="40" y1="28" x2="40" y2="122" stroke="#475569" stroke-width="1.5"/>'
        f'<line x1="40" y1="122" x2="360" y2="122" stroke="#475569" stroke-width="1.5"/>'
        f'<line x1="40" y1="62" x2="360" y2="62" stroke="#16a34a" stroke-dasharray="3,3"/>'
        f'<text x="20" y="78" font-size="8" fill="#475569" transform="rotate(-90 20 78)" text-anchor="middle">Soil pH</text>'
        f'{bar_svg}'
        f'</svg>'
    )
    pa_s = str(p_a).replace(".", ",")
    pd_s = str(p_d).replace(".", ",")
    span = round(p_d - p_a, 1)
    span_s = str(span).replace(".", ",")
    prompt = (
        "Inspect the soil monitoring bar graph comparing four South African farm plots.\n\n"
        "1. Identify which plot is **most acidic** and which plot is **alkaline (> 7)** [2].\n"
        f"2. Calculate the pH span between Plot D (pH {pd_s}) and Plot A (pH {pa_s}) [1]."
    )
    correct = f"Most acidic: Plot A (pH {pa_s}); Alkaline: Plot D (pH {pd_s}); Span = {span_s} pH units."
    sol = (
        f"**Step 1:** Lowest bar **Plot A (pH {pa_s})** is most acidic; **Plot D (pH {pd_s})** lies above 7,0 and is alkaline [2].\n\n"
        f"**Step 2:** Span $= {pd_s} - {pa_s} = {span_s}$ pH units [1]."
    )
    return _q(
        rng, "47", "47_bar_graph_soil_ph_remediation_or_stream_monitoring", prompt, correct, sol, 3, "calculation",
        ["soil_bar_chart_reading_error"],
        "Lowest bar = lowest pH = most acidic; calculate difference D - A.",
        f"Plot A most acidic ({pa_s}); Plot D alkaline ({pd_s}); span = {span_s}.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_48_ion_model_excess_h_plus_vs_oh_minus_particle_diagram(rng: random.Random) -> Dict[str, Any]:
    n_acid_h = rng.randint(4, 6)
    n_neut = rng.randint(2, 4)
    n_base_oh = rng.randint(4, 6)
    configs = [
        ("Acidic (pH < 7)", f"contains an excess of hydrogen ions ({n_acid_h} H+ vs 1 OH-)", f"{n_acid_h} H+ : 1 OH-", " ".join(["H+"] * n_acid_h), "H+  OH-", "#fee2e2", "#dc2626", "#991b1b"),
        ("Neutral (pH = 7)", f"contains equal numbers of H+ and OH- ions ({n_neut} each)", f"{n_neut} H+ : {n_neut} OH-", " ".join(["H+"] * n_neut), " ".join(["OH-"] * n_neut), "#dcfce7", "#16a34a", "#166534"),
        ("Basic / Alkaline (pH > 7)", f"contains an excess of hydroxide ions ({n_base_oh} OH- vs 1 H+)", f"1 H+ : {n_base_oh} OH-", "H+  OH-", " ".join(["OH-"] * n_base_oh), "#dbeafe", "#2563eb", "#1e3a8a"),
    ]
    rng.shuffle(configs)
    boxes = []
    for idx, cfg in enumerate(configs):
        b_label = f"Beaker {idx + 1}"
        x = 20 + idx * 119
        xc = x + 51
        _, _, ratio_txt, top_row, bot_row, fill_c, stroke_c, txt_c = cfg
        boxes.append(
            f'<rect x="{x}" y="30" width="102" height="90" rx="4" fill="{fill_c}" stroke="{stroke_c}"/>'
            f'<text x="{xc}" y="45" font-size="8.5" font-weight="bold" fill="{txt_c}" text-anchor="middle">{b_label}</text>'
            f'<text x="{xc}" y="68" font-size="8" fill="#991b1b" text-anchor="middle">{top_row}</text>'
            f'<text x="{xc}" y="88" font-size="8" fill="#1e3a8a" text-anchor="middle">{bot_row}</text>'
            f'<text x="{xc}" y="110" font-size="7.5" fill="#475569" text-anchor="middle">{ratio_txt}</text>'
        )
    pick_i = rng.randint(0, 2)
    b_name = f"Beaker {pick_i + 1}"
    verdict, exp = configs[pick_i][0], configs[pick_i][1]
    svg = (
        '<svg viewBox="0 0 380 140" xmlns="http://www.w3.org/2000/svg">'
        '<rect width="380" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        '<text x="190" y="18" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Submicroscopic Ion Ratios in Three Solutions</text>'
        + "".join(boxes) +
        '</svg>'
    )
    prompt = (
        "Inspect the ion ratio diagram showing relative counts of $H^+$ and $OH^-$ ions in three solutions.\n\n"
        f"Classify **{b_name}** as acidic, neutral, or basic, justifying from its ion count [2]."
    )
    correct = f"{verdict}; {b_name} {exp}."
    sol = f"**Step 1 & 2:** Inspecting particle totals shows **{b_name}** {exp}, making it **{verdict}** [2]."
    return _q(
        rng, "48", "48_ion_model_excess_h_plus_vs_oh_minus_particle_diagram", prompt, correct, sol, 2, "short_answer",
        ["h_plus_oh_minus_ion_balance_confusion"],
        "Excess H+ = acidic; Equal = neutral; Excess OH- = basic.",
        f"{b_name}: {verdict}.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_49_identifying_mislabeled_laboratory_bottles_using_indicators(rng: random.Random) -> Dict[str, Any]:
    bottles = ["Hydrochloric acid (pH 1)", "Sodium chloride water (pH 7)", "Ammonia base (pH 11)"]
    rng.shuffle(bottles)
    prompt = (
        "Three lost labels fell off reagent bottles **W, X, and Y** (known to contain hydrochloric acid pH 1, pure NaCl salt water pH 7, and ammonia base pH 11).\n"
        "- Bottle W turns **Universal Indicator dark red** and **blue litmus red**.\n"
        "- Bottle X turns **Universal Indicator emerald green** and leaves **both red and blue litmus unchanged**.\n"
        "- Bottle Y turns **Universal Indicator dark blue** and **phenolphthalein pink**.\n\n"
        "Match each bottle (**W, X, Y**) to its chemical identity [3]."
    )
    correct = "W = Hydrochloric acid (pH 1); X = Sodium chloride water (pH 7); Y = Ammonia base (pH 11)"
    sol = (
        "**Step 1:** W -> red Universal Indicator & red litmus -> **Hydrochloric acid (pH 1)** [1].\n\n"
        "**Step 2:** X -> green Universal Indicator & zero litmus shift -> **Sodium chloride water (pH 7)** [1].\n\n"
        "**Step 3:** Y -> blue Universal Indicator & pink phenolphthalein -> **Ammonia base (pH 11)** [1]."
    )
    return _q(
        rng, "49", "49_identifying_mislabeled_laboratory_bottles_using_indicators", prompt, correct, sol, 3, "structured",
        ["unknown_bottle_indicator_deduction_error"],
        "Match dark red -> strong acid, emerald green -> neutral, pink phenolphthalein -> base.",
        "W=HCl, X=NaCl, Y=NH3.",
        correct,
    )


def arch_50_comprehensive_ph_indicators_and_safety_synthesis(rng: random.Random) -> Dict[str, Any]:
    acid_c = rng.choice(["concentrated H2SO4", "concentrated HCl"])
    prompt = (
        f"In a complete practical synthesis involving **pH, indicators, and diluting {acid_c}**:\n\n"
        "1. Arrange **pH 2, pH 7, pH 9, pH 13** as strong acid, neutral, weak base, or strong base [2].\n"
        "2. State the colour of **bromothymol blue** at pH 2 vs pH 7 vs pH 13 [2].\n"
        f"3. State the exact golden dilution rule for **{acid_c}** and immediate skin-splash first aid [2]."
    )
    correct = "1. pH 2=strong acid, pH 7=neutral, pH 9=weak base, pH 13=strong base; 2. Bromothymol blue: yellow (pH 2), green (pH 7), blue (pH 13); 3. Add acid slowly to water (never water to acid); flush splashes continuously under cold running tap water for 15–20 min."
    sol = (
        "**Step 1:** Classifications: pH 2 (strong acid), pH 7 (neutral), pH 9 (weak base), pH 13 (strong base) [2].\n\n"
        "**Step 2:** Bromothymol blue: **Yellow** (acid pH 2), **Green** (neutral pH 7), **Blue** (base pH 13) [2].\n\n"
        "**Step 3:** **Always add acid slowly to water** while stirring; if spilled on skin, **flush immediately with running cold water for 15–20 min** [2]."
    )
    return _q(
        rng, "50", "50_comprehensive_ph_indicators_and_safety_synthesis", prompt, correct, sol, 6, "structured",
        ["ph_synthesis_assessment_error"],
        "Tie together pH boundaries, bromothymol Y/G/B, acid-to-water rule, and water flushing.",
        "1. Acid/Neutral/Weak base/Strong base; 2. Yellow/Green/Blue; 3. Acid -> water; 15–20 min rinse.",
        correct,
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_agricultural_soil_ph_testing_and_crop_preferences": arch_26_agricultural_soil_ph_testing_and_crop_preferences,
    "27_biological_human_body_ph_compartment_variation": arch_27_biological_human_body_ph_compartment_variation,
    "28_hair_shampoo_ph_5_5_and_cuticle_chemistry": arch_28_hair_shampoo_ph_5_5_and_cuticle_chemistry,
    "29_bases_vs_alkalis_solubility_distinction": arch_29_bases_vs_alkalis_solubility_distinction,
    "30_non_edible_safety_rule_never_taste_unknown_chemicals": arch_30_non_edible_safety_rule_never_taste_unknown_chemicals,
    "31_golden_dilution_rule_acid_into_water_exothermic": arch_31_golden_dilution_rule_acid_into_water_exothermic,
    "32_sulfuric_acid_dehydrating_sugar_skin_hazard": arch_32_sulfuric_acid_dehydrating_sugar_skin_hazard,
    "33_essential_laboratory_ppe_goggles_coat_gloves": arch_33_essential_laboratory_ppe_goggles_coat_gloves,
    "34_emergency_chemical_splash_skin_and_eye_first_aid": arch_34_emergency_chemical_splash_skin_and_eye_first_aid,
    "35_concentration_vs_strength_careful_distinction": arch_35_concentration_vs_strength_careful_distinction,
    "36_combining_multiple_indicators_unknown_solution_deduction": arch_36_combining_multiple_indicators_unknown_solution_deduction,
    "37_strong_acid_dilution_ph_rise_toward_7": arch_37_strong_acid_dilution_ph_rise_toward_7,
    "38_strong_base_dilution_ph_drop_toward_7": arch_38_strong_base_dilution_ph_drop_toward_7,
    "39_neutral_salt_solutions_nacl_vs_distilled_water_ph": arch_39_neutral_salt_solutions_nacl_vs_distilled_water_ph,
    "40_carbonated_soft_drink_vs_milk_vs_coffee_acidity_comparison": arch_40_carbonated_soft_drink_vs_milk_vs_coffee_acidity_comparison,
    "41_testing_solids_requires_dissolving_in_distilled_water": arch_41_testing_solids_requires_dissolving_in_distilled_water,
    "42_universal_indicator_paper_dipping_spot_tile_technique": arch_42_universal_indicator_paper_dipping_spot_tile_technique,
    "43_reading_swimming_pool_comparator_color_chart": arch_43_reading_swimming_pool_comparator_color_chart,
    "44_toothpaste_alkaline_mouth_ph_protection": arch_44_toothpaste_alkaline_mouth_ph_protection,
    "45_acidic_cleansers_vinegar_vs_alkaline_bleach_kitchen_safety": arch_45_acidic_cleansers_vinegar_vs_alkaline_bleach_kitchen_safety,
    "46_constructing_ph_data_table_and_axis_variable_selection": arch_46_constructing_ph_data_table_and_axis_variable_selection,
    "47_bar_graph_soil_ph_remediation_or_stream_monitoring": arch_47_bar_graph_soil_ph_remediation_or_stream_monitoring,
    "48_ion_model_excess_h_plus_vs_oh_minus_particle_diagram": arch_48_ion_model_excess_h_plus_vs_oh_minus_particle_diagram,
    "49_identifying_mislabeled_laboratory_bottles_using_indicators": arch_49_identifying_mislabeled_laboratory_bottles_using_indicators,
    "50_comprehensive_ph_indicators_and_safety_synthesis": arch_50_comprehensive_ph_indicators_and_safety_synthesis,
}
