"""Grade 9 Natural Sciences - Reactions of Non-Metals with Oxygen: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/03. Reactions of non metals with oxygen.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .reactions_nonmetals_oxygen_archetypes_01_25 import _q


def arch_26_sulfur_trioxide_formation_industrial_contact(rng: random.Random) -> Dict[str, Any]:
    temp_c = rng.choice(["450 °C", "430 °C", "460 °C"])
    prompt = (
        f"In industrial sulfuric acid plants (around **{temp_c}** over a catalyst), sulfur dioxide reacts further with extra oxygen to yield **sulfur trioxide**.\n\n"
        "1. Write the chemical formula of **sulfur trioxide** [1].\n"
        "2. Write the **balanced chemical equation** for converting $SO_2$ into sulfur trioxide [2]."
    )
    correct = "Formula: SO3; Balanced equation: 2SO2 + O2 -> 2SO3"
    sol = (
        "**Step 1:** *Tri-* specifies **3 oxygen atoms** per sulfur atom: **$\\text{SO}_3$** [1].\n\n"
        "**Step 2:** Balancing oxygen atoms gives **$$2\\text{SO}_2(g) + \\text{O}_2(g) \\rightarrow 2\\text{SO}_3(g)$$** [2]."
    )
    return _q(
        rng, "26", "26_sulfur_trioxide_formation_industrial_contact", prompt, correct, sol, 3, "structured",
        ["sulfur_trioxide_balancing_error"],
        "'tri-' = 3 O atoms -> SO3; put a 2 in front of SO2 and SO3 to supply the extra 2 O atoms.",
        "2SO2 + O2 -> 2SO3.",
        correct,
    )


def arch_27_nonmetal_oxide_water_reaction_carbonic_acid(rng: random.Random) -> Dict[str, Any]:
    drink = rng.choice(["fizzy carbonated sparkling water", "carbonated soda water", "freshly opened lemonade"])
    prompt = (
        f"When carbon dioxide gas is pressurised into pure water—such as in **{drink}**—part of the dissolved gas reacts chemically with water.\n\n"
        "1. Name the **weak acid** formed and write its chemical formula [2].\n"
        "2. Write the balanced synthesis equation combining $CO_2$ and $H_2O$ [1]."
    )
    correct = "Carbonic acid (H2CO3); CO2(g) + H2O(l) -> H2CO3(aq)"
    sol = (
        "**Step 1:** Dissolved carbon dioxide reacts reversibly with water to produce weak **carbonic acid** with formula **$\\text{H}_2\\text{CO}_3$** [2].\n\n"
        "**Step 2:** Equation: **$$\\text{CO}_2(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{CO}_3(aq)$$** [1]."
    )
    return _q(
        rng, "27", "27_nonmetal_oxide_water_reaction_carbonic_acid", prompt, correct, sol, 3, "structured",
        ["carbonic_acid_formula_error"],
        "Add the atoms of CO2 and H2O together directly: H2 + C + O3.",
        "Carbonic acid = H2CO3 -> CO2 + H2O -> H2CO3.",
        correct,
    )


def arch_28_nonmetal_oxide_water_reaction_sulfurous_acid(rng: random.Random) -> Dict[str, Any]:
    vol = rng.choice(["25 mL", "40 mL", "50 mL"])
    prompt = (
        f"A teacher adds **{vol}** of distilled water into a sealed jar freshly filled with choking **sulfur dioxide ($\\text{{SO}}_2$)** gas and swirls it vigorously.\n\n"
        "1. Write the balanced chemical equation forming the dissolved acid [2].\n"
        "2. Name this acid and predict its effect on damp blue litmus paper [2]."
    )
    correct = "SO2 + H2O -> H2SO3; Sulfurous acid; Blue litmus paper turns red (pH < 7)."
    sol = (
        "**Step 1:** $SO_2$ reacts with water: **$$\\text{SO}_2(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{SO}_3(aq)$$** [2].\n\n"
        "**Step 2:** The solution contains acidic **sulfurous acid**, which turns **blue litmus paper red** [2]."
    )
    return _q(
        rng, "28", "28_nonmetal_oxide_water_reaction_sulfurous_acid", prompt, correct, sol, 4, "structured",
        ["sulfurous_vs_sulfuric_acid_error"],
        "Add H2O straight onto SO2: H2 + S + O3.",
        "SO2 + H2O -> H2SO3 (sulfurous acid), turning blue litmus red.",
        correct,
    )


def arch_29_nonmetal_oxide_water_reaction_sulfuric_and_nitric_acids(rng: random.Random) -> Dict[str, Any]:
    oxide_pair = rng.choice([
        ("Sulfur trioxide (SO3)", "Sulfuric acid (H2SO4)", "SO3 + H2O -> H2SO4"),
        ("Nitrogen dioxide (NO2) oxidising in moist clouds", "Nitric acid (HNO3)", "dissolves and oxidises in water droplets to form strong nitric acid (HNO3)"),
    ])
    nm_ox, acid_res, rxn = oxide_pair
    prompt = (
        f"When industrial pollutant **{nm_ox}** reaches moist cloud droplets in the upper atmosphere, a strong acid forms.\n\n"
        "Name the **strong acid** produced, write its chemical formula, and explain how this lowers cloud pH sharply [3]."
    )
    correct = f"{acid_res}; {nm_ox} reacts with water ({rxn}), releasing high H+ concentration and dropping rainfall pH down to ~3,8–4,5."
    sol = (
        f"**Step 1:** Reaction produces **{acid_res}** ({rxn}) [2].\n\n"
        "**Step 2:** Unlike weak carbonic acid, strong acids ionise completely in raindrops, driving rain pH below 5,0 [1]."
    )
    return _q(
        rng, "29", "29_nonmetal_oxide_water_reaction_sulfuric_and_nitric_acids", prompt, correct, sol, 3, "short_answer",
        ["strong_acid_rain_species_confusion"],
        "Distinguish SO2 (-> H2SO3) from SO3 (-> H2SO4) and NO2 (-> HNO3).",
        f"Produces {acid_res}.",
        correct,
    )


def arch_30_nonmetal_oxides_litmus_and_universal_indicator_test(rng: random.Random) -> Dict[str, Any]:
    gas_tested = rng.choice(["sulfur dioxide (SO2)", "carbon dioxide (CO2)", "diphosphorus pentoxide (P2O5)"])
    prompt = (
        f"A sample of **{gas_tested}** is bubbled through distilled water containing a few drops of neutral green **Universal Indicator**.\n\n"
        "What indicator colour shift and pH range should learners observe?"
    )
    correct = "Green (neutral pH 7) shifts to yellow, orange, or red (acidic pH < 7)."
    options = [
        correct,
        "Green shifts immediately to deep purple/violet (strong alkali, pH 13).",
        "Universal Indicator freezes solid and turns bright turquoise.",
        "Blue litmus stays blue and red litmus turns bright royal blue.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Non-metal oxides react with water to form **acidic** solutions (pH < 7).\n"
        "**Step 2:** On the Universal Indicator spectrum, acids change green pH 7 to **yellow, orange, or red** [2]."
    )
    return _q(
        rng, "30", "30_nonmetal_oxides_litmus_and_universal_indicator_test", prompt, correct, sol, 2, "multiple_choice",
        ["universal_indicator_acid_color_inversion"],
        "Do dissolved non-metal oxides create acids or bases?",
        "Non-metal oxides -> Acid -> yellow/orange/red (pH < 7).",
        correct, options=options,
    )


def arch_31_comparing_acidic_nonmetal_oxide_vs_basic_metal_oxide_solutions(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("Sulfur + Oxygen", "Magnesium + Oxygen"),
        ("Carbon + Oxygen", "Calcium + Oxygen"),
    ])
    nm_rxn, m_rxn = pair
    prompt = (
        f"Contrast the aqueous solutions produced by burning **({nm_rxn})** versus **({m_rxn})** and mixing each product with water.\n\n"
        "Compare BOTH reactions across:\n"
        "1. General oxide class [1]\n"
        "2. Resulting pH relative to 7 [2]\n"
        "3. Action on red and blue litmus paper [2]"
    )
    correct = f"1. ({nm_rxn}) forms non-metal oxide; ({m_rxn}) forms metal oxide. 2. Non-metal oxide -> acidic (pH < 7); Metal oxide -> basic (pH > 7). 3. Non-metal oxide turns blue litmus red; Metal oxide turns red litmus blue."
    sol = (
        f"**Step 1:** **{nm_rxn}** produces a **non-metal oxide**; **{m_rxn}** produces a **metal oxide** [1].\n\n"
        "**Step 2:** Non-metal oxides yield **acidic** solutions (**$\\text{pH} < 7$**), whereas metal oxides yield **basic** solutions (**$\\text{pH} > 7$**) [2].\n\n"
        "**Step 3:** Non-metal oxide solution turns **blue litmus red**; metal oxide solution turns **red litmus blue** [2]."
    )
    return _q(
        rng, "31", "31_comparing_acidic_nonmetal_oxide_vs_basic_metal_oxide_solutions", prompt, correct, sol, 5, "structured",
        ["metal_vs_nonmetal_oxide_acidity_confusion"],
        "Sort the two reactions cleanly: Non-metal oxide = Acid; Metal oxide = Base.",
        "pH < 7 (blue -> red) vs pH > 7 (red -> blue).",
        correct,
    )


def arch_32_blowing_exhaled_breath_straw_limewater_and_indicator(rng: random.Random) -> Dict[str, Any]:
    reagent = rng.choice([
        ("bromothymol blue indicator water (initially blue/green)", "shifts to bright yellow", "exhaled CO2 dissolves into weak carbonic acid (H2CO3), lowering pH below 6,0"),
        ("clear limewater solution", "turns milky/cloudy white", "exhaled CO2 precipitates insoluble white calcium carbonate (CaCO3)"),
    ])
    liq, change, exp = reagent
    prompt = (
        f"During an investigation, a learner uses a clean drinking straw to bubble exhaled air gently through **{liq}**.\n\n"
        "State the expected colour/visual change and explain the chemistry driving it [3]."
    )
    correct = f"The liquid {change}; Because {exp}."
    sol = (
        f"**Step 1:** Cellular respiration releases **$CO_2$** in exhaled breath.\n\n"
        f"**Step 2:** Bubbling it through the liquid causes it to **{change}** because **{exp}** [3]."
    )
    return _q(
        rng, "32", "32_blowing_exhaled_breath_straw_limewater_and_indicator", prompt, correct, sol, 3, "short_answer",
        ["exhaled_co2_indicator_reaction_error"],
        "Exhaled breath is rich in carbon dioxide, a non-metal oxide.",
        f"{change}: {exp}.",
        correct,
    )


def arch_33_acid_rain_coal_power_stations_mpumalanga_emissions(rng: random.Random) -> Dict[str, Any]:
    region = rng.choice(["Mpumalanga Highveld (Witbank / eMalahleni)", "Waterberg coalfields (Lephalale)"])
    prompt = (
        f"Coal mined in the **{region}** often contains small percentages of **sulfur impurities** alongside carbon.\n\n"
        "Trace the **three-step chemical pathway** showing how burning impure coal inside a power station leads to acid rain falling far downwind [4]."
    )
    correct = "1. Sulfur impurity combusts: S + O2 -> SO2 gas escapes up chimneys. 2. Wind carries SO2 into moist clouds where it oxidises and dissolves (SO2 + H2O -> H2SO3 / SO3 + H2O -> H2SO4). 3. Acidified droplets fall as acid rain with pH < 5."
    sol = (
        "**Step 1 (Combustion):** Sulfur impurities react with hot oxygen: **$\\text{S} + \\text{O}_2 \\rightarrow \\text{SO}_2$** [1].\n\n"
        "**Step 2 (Atmospheric oxidation & hydration):** Wind disperses $\\text{SO}_2$ into humid clouds where it reacts with water vapour/oxygen forming **sulfurous acid ($H_2SO_3$)** and **sulfuric acid ($H_2SO_4$)** [2].\n\n"
        "**Step 3 (Precipitation):** Rainwater falls with abnormally acidic pH (typically pH 3,5–4,8) hundreds of kilometres downwind [1]."
    )
    return _q(
        rng, "33", "33_acid_rain_coal_power_stations_mpumalanga_emissions", prompt, correct, sol, 4, "structured",
        ["acid_rain_sulfur_pathway_gap"],
        "Link three stages: burning sulfur in furnace -> reaction in clouds -> acidic rainfall.",
        "S + O2 -> SO2 -> dissolves/oxidises in cloud water -> H2SO3/H2SO4 rain.",
        correct,
    )


def arch_34_acid_rain_nitrogen_oxides_transport_emissions(rng: random.Random) -> Dict[str, Any]:
    city = rng.choice(["Johannesburg N1 corridor", "Cape Town CBD", "Durban N3 freight route"])
    prompt = (
        f"Heavy petrol and diesel road traffic along the **{city}** emits little sulfur compared to coal plants, yet still contributes strongly to acid rain.\n\n"
        "Name the non-metal oxide pollutants formed inside hot vehicle engines and the acid they generate in rain [2]."
    )
    correct = "Nitrogen oxides (NO and NO2 formed when atmospheric N2 and O2 react at high engine temperatures); Dissolve/oxidise in rain to form dilute Nitric acid (HNO3)."
    sol = (
        "**Step 1:** High piston combustion temperatures force air's nitrogen and oxygen to bond into **nitrogen oxides ($NO$ and $NO_2$)** [1].\n\n"
        "**Step 2:** In moist clouds these convert into **nitric acid ($\\text{HNO}_3$)**, acidifying rainfall alongside sulfuric pollutants [1]."
    )
    return _q(
        rng, "34", "34_acid_rain_nitrogen_oxides_transport_emissions", prompt, correct, sol, 2, "short_answer",
        ["nox_acid_rain_omission"],
        "Think about the 78% nitrogen and 21% oxygen drawn into every hot engine cylinder.",
        "Nitrogen oxides (NO / NO2) -> Nitric acid (HNO3).",
        correct,
    )


def arch_35_acid_rain_soil_nutrient_leaching_and_aluminium_toxicity(rng: random.Random) -> Dict[str, Any]:
    crop = rng.choice(["Mpumalanga pine plantations", "Highveld maize crops", "indigenous Drakensberg forests"])
    prompt = (
        f"Prolonged acid rain falling over **{crop}** weakens trees and stunts agricultural yields even before touching leaves directly.\n\n"
        "State **two distinct chemical impacts** that acidified soil water has on plant roots and minerals [2]."
    )
    correct = "1. Leaches essential mineral nutrients (calcium, magnesium, potassium ions) out below root reach; 2. Dissolves natural aluminium minerals into toxic Al3+ ions that damage fine roots and block nutrient uptake."
    sol = (
        "**Step 1:** Excess $H^+$ ions wash vital soil minerals (**calcium, magnesium, potassium**) out of topsoil into groundwater (**leaching**) [1].\n\n"
        "**Step 2:** Low soil pH mobilises toxic soluble **aluminium ions ($Al^{3+}$)** from clay soils, poisoning root tips and reducing drought/frost resilience [1]."
    )
    return _q(
        rng, "35", "35_acid_rain_soil_nutrient_leaching_and_aluminium_toxicity", prompt, correct, sol, 2, "short_answer",
        ["acid_rain_burns_skin_myth"],
        "Consider what happens to soil minerals (good nutrients vs locked-up toxic aluminium) when soil pH drops.",
        "1. Nutrient leaching (Ca/Mg lost); 2. Toxic Al3+ root poisoning.",
        correct,
    )


def arch_36_acid_rain_freshwater_lake_acidification_fish_loss(rng: random.Random) -> Dict[str, Any]:
    ph_val = rng.choice(["4,3", "4,5", "4,1"])
    prompt = (
        f"Industrial acid runoff drops the water pH of a freshwater trout dam from 6,8 down to **{ph_val}**.\n\n"
        "Explain why aquatic fish, frog eggs, and river invertebrates perish when lake pH drops below 5,0 [2]."
    )
    correct = "Most fish eggs fail to hatch below pH 5; acidic water irritates/clogs delicate fish gills with mucus and disrupts blood salt balance while leached aluminium damages gill membranes."
    sol = (
        "**Step 1:** Sensitive amphibian/fish **eggs and fry die** when aquatic pH falls below ~5,0, breaking reproduction cycles [1].\n\n"
        "**Step 2:** Acidic water plus dissolved aluminium **coagulates mucus over fish gills**, blocking oxygen uptake and upsetting ion osmoregulation [1]."
    )
    return _q(
        rng, "36", "36_acid_rain_freshwater_lake_acidification_fish_loss", prompt, correct, sol, 2, "short_answer",
        ["aquatic_acidification_mechanism"],
        "Think about reproduction (eggs/tadpoles) and respiration across fish gills.",
        "Eggs fail to hatch + mucus/acid damages gills and kills prey food webs.",
        correct,
    )


def arch_37_acid_rain_corrosion_of_limestone_marble_buildings(rng: random.Random) -> Dict[str, Any]:
    monument = rng.choice(["historic carved marble monument", "limestone civic cathedral facade", "calcium carbonate concrete bridge"])
    prompt = (
        f"Over several decades, crisp decorative carvings on a **{monument}** become pitted and blurred under urban acid rain.\n\n"
        "1. Name the chemical compound making up marble and limestone rock [1].\n"
        "2. Write the word equation explaining why dilute sulfuric acid in rain dissolves the stone surface [2]."
    )
    correct = "Calcium carbonate (CaCO3); Sulfuric acid + Calcium carbonate -> Calcium sulfate + Carbon dioxide + Water (acid-carbonate erosion)."
    sol = (
        "**Step 1:** Marble and limestone consist primarily of basic **calcium carbonate ($\\text{CaCO}_3$)** [1].\n\n"
        "**Step 2:** Acid rain neutralises and dissolves the carbonate stone: **Sulfuric acid + Calcium carbonate $\\rightarrow$ Calcium sulfate + Carbon dioxide + Water** [2]."
    )
    return _q(
        rng, "37", "37_acid_rain_corrosion_of_limestone_marble_buildings", prompt, correct, sol, 3, "structured",
        ["limestone_acid_rain_mechanism"],
        "What basic salt makes up limestone and marble, and how do acids react with metal carbonates?",
        "Calcium carbonate (CaCO3) reacts with acid rain -> salt + CO2 + water.",
        correct,
    )


def arch_38_agricultural_lime_soil_and_lake_remediation(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice(["an acidified citrus orchard soil", "an acidified mountain farm dam"])
    prompt = (
        f"Farmers spread crushed powdered **agricultural lime ($\\text{{CaCO}}_3$)** onto **{target}** damaged by long-term acid deposition.\n\n"
        "Why does agricultural lime restore soil/water health chemically?"
    )
    correct = "Calcium carbonate is a basic metal carbonate that reacts with excess acid via neutralisation (Acid + Carbonate -> Salt + Water + CO2), raising pH safely back toward 6,5–7."
    options = [
        correct,
        "Lime is a concentrated acid that dissolves excess rainwater away.",
        "Powdered lime turns acidic sulfur dioxide back into pure yellow sulfur rocks.",
        "Agricultural lime lowers soil pH further to pH 1 so plants absorb stronger acids.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** **Agricultural lime ($\\text{CaCO}_3$)** behaves as a **base**, NOT an acid.\n"
        "**Step 2:** Neutralisation consumes free hydrogen ions (**Acid + Carbonate $\\rightarrow$ Salt + Water + $CO_2$**), restoring optimal crop/aquatic pH (~6,5–7,0) [2]."
    )
    return _q(
        rng, "38", "38_agricultural_lime_soil_and_lake_remediation", prompt, correct, sol, 2, "multiple_choice",
        ["lime_is_an_acid_myth"],
        "Confuse 'lime' (basic calcium carbonate) with acidic citrus 'limes'? Avoid that trap!",
        "Lime (CaCO3) = base that neutralises soil/lake acid back toward pH 7.",
        correct, options=options,
    )


def arch_39_scrubber_flue_gas_desulfurisation_power_stations(rng: random.Random) -> Dict[str, Any]:
    c_pipe = rng.choice(["#64748b", "#475569"])
    svg = (
        f'<svg viewBox="0 0 380 155" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="155" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="18" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Flue Gas Desulfurisation ("Scrubber") Tower</text>'
        f'<rect x="145" y="34" width="90" height="106" rx="4" fill="#fff" stroke="{c_pipe}" stroke-width="2"/>'
        f'<path d="M 35,108 L 145,108" stroke="#ef4444" stroke-width="5"/><text x="86" y="98" font-size="8" font-weight="bold" fill="#b91c1c" text-anchor="middle">Dirty gas (SO2)</text>'
        f'<path d="M 190,34 L 190,22" stroke="#16a34a" stroke-width="4"/><text x="275" y="36" font-size="8" font-weight="bold" fill="#15803d">Cleaned exhaust</text>'
        f'<line x1="155" y1="54" x2="225" y2="54" stroke="#0284c7" stroke-width="2"/>'
        f'<line x1="168" y1="58" x2="162" y2="82" stroke="#38bdf8" stroke-dasharray="2,2"/>'
        f'<line x1="190" y1="58" x2="190" y2="82" stroke="#38bdf8" stroke-dasharray="2,2"/>'
        f'<line x1="212" y1="58" x2="218" y2="82" stroke="#38bdf8" stroke-dasharray="2,2"/>'
        f'<text x="295" y="60" font-size="8" fill="#0369a1" text-anchor="middle">CaCO3 / CaO slurry spray</text>'
        f'<rect x="147" y="122" width="86" height="16" fill="#cbd5e1"/><text x="190" y="133" font-size="7.5" fill="#1e293b" text-anchor="middle">Solid CaSO3 / gypsum</text>'
        f'</svg>'
    )
    prompt = (
        "Inspect the industrial smokestack scrubber diagram fitted onto a coal power plant.\n\n"
        "1. Which acidic non-metal oxide gas is targeted before leaving the chimney? [1]\n"
        "2. Explain chemically why spraying powdered **calcium carbonate ($\\text{CaCO}_3$)** or lime slurry removes this gas [2]."
    )
    correct = "Sulfur dioxide (SO2); Basic CaCO3/CaO chemically neutralises acidic SO2 inside the tower, trapping sulfur as solid calcium sulfite/gypsum instead of acid rain gas."
    sol = (
        "**Step 1:** The scrubber targets acidic **sulfur dioxide ($\\text{SO}_2$)** from coal combustion [1].\n\n"
        "**Step 2:** Spraying basic limestone/lime slurry causes an **acid-base neutralisation reaction**, locking sulfur harmlessly into solid **calcium sulfite / calcium sulfate (gypsum)** used in plasterboard rather than polluting clouds [2]."
    )
    return _q(
        rng, "39", "39_scrubber_flue_gas_desulfurisation_power_stations", prompt, correct, sol, 3, "structured",
        ["flue_gas_scrubber_chemistry_error"],
        "Check the acidic input gas vs basic carbonate spray.",
        "Acidic SO2 neutralised by basic CaCO3/CaO spray -> solid gypsum.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_40_mass_conservation_in_carbon_combustion_open_vs_closed(rng: random.Random) -> Dict[str, Any]:
    c_mass = rng.choice([12, 18, 24, 30])
    o_mass = int(c_mass * 32 / 12)
    tot_mass = c_mass + o_mass
    prompt = (
        f"In a closed rigid oxygen flask, **{c_mass} g** of pure carbon reacts completely with **{o_mass} g** of oxygen gas to produce carbon dioxide.\n\n"
        "1. State the exact total mass of $CO_2$ formed inside the sealed flask [1].\n"
        "2. Explain why burning the same **{c_mass} g** of pure charcoal on an open braai leaves virtually no solid ash behind, making it look as if mass vanished [2]."
    )
    correct = f"{tot_mass} g of CO2; In an open braai, the gaseous CO2 product escapes upward into surrounding air, whereas total mass of all reactants and products remains strictly conserved."
    sol = (
        f"**Step 1:** By conservation of mass: $m(\\text{{CO}}_2) = {c_mass}\\text{{ g}} + {o_mass}\\text{{ g}} = {tot_mass}\\text{{ g}}$ [1].\n\n"
        "**Step 2:** On an open braai, carbon turns into **gaseous $\\text{CO}_2$ that disperses invisibly** into the atmosphere—atoms did not vanish, they became an unweighed gas [2]."
    )
    return _q(
        rng, "40", "40_mass_conservation_in_carbon_combustion_open_vs_closed", prompt, correct, sol, 3, "calculation",
        ["mass_destroyed_during_burning_myth"],
        "Add the reacting C and O2 masses; remember CO2 is a gas, unlike solid MgO ash.",
        f"{c_mass} + {o_mass} = {tot_mass} g; open-air CO2 escapes unseen.",
        correct,
    )


def arch_41_balancing_nonmetal_combustion_equations_set(rng: random.Random) -> Dict[str, Any]:
    task = rng.choice([
        ("P + O2 -> P2O5", "4P + 5O2 -> 2P2O5", "4 P, 10 O"),
        ("H2 + O2 -> H2O", "2H2 + O2 -> 2H2O", "4 H, 2 O"),
        ("C + O2 -> CO (incomplete combustion)", "2C + O2 -> 2CO", "2 C, 2 O"),
        ("S + O2 -> SO3 (catalytic excess O2)", "2S + 3O2 -> 2SO3", "2 S, 6 O"),
    ])
    unbal, bal, counts = task
    prompt = (
        f"Balance the non-metal oxidation equation cleanly without changing any chemical formula subscripts:\n"
        f"$$\\text{{{unbal}}}$$\n\n"
        "Write the full balanced equation and confirm the atom counts on both sides [3]."
    )
    correct = f"{bal}; Conserved atoms on both sides: {counts}"
    sol = (
        f"**Step 1:** Adjusted coefficients give balanced equation: **$$\\text{{{bal}}}$$** [2].\n\n"
        f"**Step 2:** Atom check: **{counts}** on reactants = **{counts}** on products [1]."
    )
    return _q(
        rng, "41", "41_balancing_nonmetal_combustion_equations_set", prompt, correct, sol, 3, "structured",
        ["nonmetal_balancing_subscript_change_error"],
        "Count oxygen atoms on both sides first and use coefficients only.",
        f"Balanced: {bal} ({counts}).",
        correct,
    )


def arch_42_group_14_and_16_valency_comparison_co2_vs_so2(rng: random.Random) -> Dict[str, Any]:
    el_pair = rng.choice([
        ("Carbon (Group 14) -> CO2", "Silicon (Group 14) -> SiO2"),
        ("Sulfur (Group 16) -> SO2", "Selenium (Group 16) -> SeO2"),
    ])
    known, pred = el_pair
    prompt = (
        f"Elements within the same vertical Periodic Table group often form oxides with matching formulas.\n"
        f"Given **{known}**, predict the expected dioxide formula of **{pred.split(' -> ')[0]}** in the same group and explain why [2]."
    )
    target_elem, target_form = pred.split(" -> ")
    correct = f"{target_form}; Elements in the same Periodic Table group share identical outer-electron bonding valency pattern."
    sol = (
        f"**Step 1:** Since {target_elem} shares the same Periodic Table group as {known.split()[0]}, it displays matching oxide stoichiometry: **$\\text{{{target_form}}}$** [1].\n\n"
        "**Step 2:** Vertical group neighbours share the same valence electron count and bonding capacity [1]."
    )
    return _q(
        rng, "42", "42_group_14_and_16_valency_comparison_co2_vs_so2", prompt, correct, sol, 2, "short_answer",
        ["periodic_table_group_formula_prediction_error"],
        "Swap the non-metal symbol while preserving the Periodic Group's 1:2 stoichiometry.",
        f"{target_elem} -> {target_form}.",
        correct,
    )


def arch_43_diatomic_nonmetal_reactants_h2_n2_o2_recognition(rng: random.Random) -> Dict[str, Any]:
    bad, good = rng.choice([
        ("H + O2 -> HO", "2H2 + O2 -> 2H2O"),
        ("N + O -> NO2", "N2 + 2O2 -> 2NO2"),
        ("C2 + O2 -> C2O2", "C + O2 -> CO2"),
    ])
    prompt = (
        f"When writing non-metal combustion equations, students sometimes confuse monatomic solids (C, S, P) with naturally diatomic gases ($H_2, N_2, O_2$).\n\n"
        f"Identify every incorrect reactant/product formula in `$\\text{{{bad}}}$` and write the true balanced equation [3]."
    )
    correct = f"Corrected balanced equation: {good}"
    sol = (
        "**Step 1:** Hydrogen, nitrogen, and oxygen gases always enter equations as **diatomic molecules ($H_2, N_2, O_2$)**, whereas solid C/S/P write as single atoms (C, S, P) [1].\n\n"
        f"**Step 2:** True balanced equation: **$$\\text{{{good}}}$$** [2]."
    )
    return _q(
        rng, "43", "43_diatomic_nonmetal_reactants_h2_n2_o2_recognition", prompt, correct, sol, 3, "structured",
        ["diatomic_nonmetal_formula_confusion"],
        "Remember: H2, N2, O2 are diatomic gases; C, S, P are monatomic in Grade 9 equations.",
        f"Corrected balanced equation: {good}.",
        correct,
    )


def arch_44_identifying_acid_rain_ph_drop_bar_chart_analysis(rng: random.Random) -> Dict[str, Any]:
    ph_clean = rng.choice([5.6, 5.7])
    ph_suburb = rng.choice([5.0, 5.1])
    ph_ind = rng.choice([4.1, 4.2, 4.3])
    ph_smelter = rng.choice([3.7, 3.8])
    bars = [
        ("Clean Coast", ph_clean, "#16a34a"),
        ("Suburban", ph_suburb, "#eab308"),
        ("Coal Belt", ph_ind, "#f97316"),
        ("Smelter", ph_smelter, "#dc2626"),
    ]
    bar_svg = ""
    for i, (lbl, val, col) in enumerate(bars):
        h = int((val / 7.0) * 86)
        x = 50 + i * 78
        y = 122 - h
        val_s = str(val).replace(".", ",")
        bar_svg += (
            f'<rect x="{x}" y="{y}" width="38" height="{h}" fill="{col}" rx="2"/>'
            f'<text x="{x+19}" y="{y-4}" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">{val_s}</text>'
            f'<text x="{x+19}" y="135" font-size="7.5" fill="#334155" text-anchor="middle">{lbl}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 380 155" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="155" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="18" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Measured Rainwater pH Across Sampling Zones</text>'
        f'<line x1="40" y1="28" x2="40" y2="122" stroke="#475569" stroke-width="1.5"/>'
        f'<line x1="40" y1="122" x2="360" y2="122" stroke="#475569" stroke-width="1.5"/>'
        f'<line x1="40" y1="60" x2="360" y2="60" stroke="#94a3b8" stroke-dasharray="3,3"/>'
        f'<text x="348" y="56" font-size="7" fill="#64748b" text-anchor="end">pH 5,0 threshold</text>'
        f'<text x="20" y="78" font-size="8" fill="#475569" transform="rotate(-90 20 78)" text-anchor="middle">Rain pH</text>'
        f'{bar_svg}'
        f'</svg>'
    )
    diff = round(ph_clean - ph_smelter, 1)
    diff_s = str(diff).replace(".", ",")
    smelt_s = str(ph_smelter).replace(".", ",")
    prompt = (
        "Inspect the bar graph showing average rainwater pH measured at four monitoring stations.\n\n"
        f"1. Which station recorded the **most acidic** rainfall, and by how many pH units is it lower than Clean Coast? [2]\n"
        "2. Caution: does a lower bar mean weaker acid or **stronger** acid? Explain [1]."
    )
    correct = f"Smelter (pH {smelt_s}), which is {diff_s} pH units lower than Clean Coast; Lower pH bar indicates STRONGER acidity (higher acid concentration)."
    sol = (
        f"**Step 1:** **Smelter** has the lowest reading (**pH {smelt_s}**); difference $= {str(ph_clean).replace('.', ',')} - {smelt_s} = {diff_s}$ pH units [2].\n\n"
        "**Step 2:** Because acidity increases as pH drops toward 1, the **shortest pH bar** corresponds to the **strongest acid rain** [1]."
    )
    return _q(
        rng, "44", "44_identifying_acid_rain_ph_drop_bar_chart_analysis", prompt, correct, sol, 3, "calculation",
        ["lower_ph_means_weaker_acid_myth"],
        "Remember: lower pH number means MORE acidic, NOT weaker!",
        f"Lowest pH = Smelter ({smelt_s}); difference = {diff_s}.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_45_unpolluted_rainwater_natural_weak_carbonic_acidity(rng: random.Random) -> Dict[str, Any]:
    ph_nat = rng.choice(["5,6", "5,7"])
    prompt = (
        f"Even on a remote island with zero coal factories or vehicles, pure unpolluted rainwater naturally measures slightly acidic at **pH {ph_nat}** rather than pH 7,0.\n\n"
        "Explain which natural atmospheric non-metal oxide produces this mild acidity [2]."
    )
    correct = "Natural atmospheric carbon dioxide (CO2) dissolves into falling raindrops to form weak carbonic acid (CO2 + H2O -> H2CO3), lowering clean rain slightly below 7 to ~pH 5,6."
    sol = (
        "**Step 1:** Natural air always contains ~0,04% **carbon dioxide ($\\text{CO}_2$)** [1].\n\n"
        f"**Step 2:** $CO_2$ dissolves in raindrops forming **weak carbonic acid ($H_2CO_3$)**, establishing clean rain's baseline at **pH {ph_nat}** (industrial acid rain drops below 5,0 from $SO_2/NO_2$) [1]."
    )
    return _q(
        rng, "45", "45_unpolluted_rainwater_natural_weak_carbonic_acidity", prompt, correct, sol, 2, "short_answer",
        ["clean_rain_is_ph7_myth"],
        "Think about trace CO2 always present naturally in dry air.",
        "Natural CO2 + H2O -> weak H2CO3 (~pH 5,6).",
        correct,
    )


def arch_46_macroscopic_submicroscopic_symbolic_sulfur_combustion(rng: random.Random) -> Dict[str, Any]:
    aspect = rng.choice([
        ("Seeing yellow powder melt and burn with a vivid blue flame", "Macroscopic level"),
        ("Imagining one yellow sulfur atom colliding with O=O to form a bent SO2 molecule", "Submicroscopic level"),
        ("Writing S(s) + O2(g) -> SO2(g)", "Symbolic level"),
    ])
    obs, lvl = aspect
    prompt = (
        "Scientists examine sulfur combustion across three representation levels: **macroscopic**, **submicroscopic**, and **symbolic**.\n\n"
        f"Classify the following chemistry statement and state one feature at ONE of the other two levels:\n*\"{obs}.\"* [2]"
    )
    correct = f"Classification: {lvl}; Other levels link observations (blue flame/choking smell), particles (1 S atom bonding with 2 O atoms), and formulas (S + O2 -> SO2)."
    sol = (
        f"**Step 1:** *\"{obs}\"* belongs to the **{lvl}** [1].\n\n"
        "**Step 2:** Complement levels include Macroscopic (vivid blue flame, pungent colourless gas), Submicroscopic (1 S + $O_2$ -> bent $SO_2$), and Symbolic ($S + O_2 \\rightarrow SO_2$) [1]."
    )
    return _q(
        rng, "46", "46_macroscopic_submicroscopic_symbolic_sulfur_combustion", prompt, correct, sol, 2, "short_answer",
        ["three_levels_sulfur_classification_error"],
        "Distinguish direct sight/smell (macro) vs atom particles (submicro) vs formulas (symbolic).",
        f"'{obs}' = {lvl}.",
        correct,
    )


def arch_47_comparing_gas_tests_o2_h2_co2_diagnostic_key(rng: random.Random) -> Dict[str, Any]:
    gas = rng.choice([
        ("Carbon dioxide (CO2)", "turns clear limewater milky white", "burning splint goes out"),
        ("Oxygen (O2)", "relights a glowing wooden splint", "supports combustion vigorously"),
        ("Hydrogen (H2)", "burns with a sharp squeaky pop at a lighted splint", "forms tiny moisture droplets"),
    ])
    name, test_obs, extra = gas
    prompt = (
        "Three unlabelled glass jars hold pure gases collected in laboratory combustion experiments: oxygen, hydrogen, and carbon dioxide.\n\n"
        f"State the **standard diagnostic laboratory test and positive observation** used to confirm **{name}** [2]."
    )
    correct = f"For {name}: {test_obs} ({extra})."
    sol = f"**Step 1 & 2:** Confirmatory identification for **{name}**: **{test_obs}** ({extra}) [2]."
    return _q(
        rng, "47", "47_comparing_gas_tests_o2_h2_co2_diagnostic_key", prompt, correct, sol, 2, "short_answer",
        ["gas_identification_test_confusion"],
        "Match each gas carefully: glowing splint = O2, burning splint pop = H2, limewater = CO2.",
        f"{name} -> {test_obs}.",
        correct,
    )


def arch_48_catalytic_converters_reducing_co_and_nox_emissions(rng: random.Random) -> Dict[str, Any]:
    metal_cat = rng.choice(["platinum and rhodium mined in South Africa's Bushveld", "platinum-palladium honeycomb"])
    prompt = (
        f"Modern vehicle exhaust systems contain a **catalytic converter** coated in **{metal_cat}**.\n\n"
        "Name the **two harmful gaseous non-metal oxides** converted inside the honeycomb and the **two harmless exhaust gases** emitted cleanly instead [2]."
    )
    correct = "Harmful pollutants converted: toxic Carbon monoxide (CO) and smog-forming Nitrogen oxides (NO/NO2); Converted into less harmful Carbon dioxide (CO2) and harmless Nitrogen gas (N2)."
    sol = (
        "**Step 1:** Catalytic metals oxidise deadly **carbon monoxide (CO)** into **$CO_2$** and reduce nitrogen oxides (**$NO_x$**) back into atmospheric **$N_2$** [2]."
    )
    return _q(
        rng, "48", "48_catalytic_converters_reducing_co_and_nox_emissions", prompt, correct, sol, 2, "short_answer",
        ["catalytic_converter_products_confusion"],
        "Think of CO gaining oxygen -> CO2, and NO/NO2 losing oxygen -> N2.",
        "Converts toxic CO & NOx -> CO2 & harmless N2.",
        correct,
    )


def arch_49_controlled_investigation_ph_drop_bubbling_nonmetal_oxide(rng: random.Random) -> Dict[str, Any]:
    gas_nm = rng.choice(["carbon dioxide", "sulfur dioxide"])
    prompt = (
        f"A learner tests whether dissolved **{gas_nm}** produces an acidic solution by bubbling the gas into 50 mL of pure distilled water while monitoring a digital pH meter.\n\n"
        "State:\n"
        "1. The starting pH of pure water before bubbling [1]\n"
        "2. How the pH meter reading changes as bubbling continues [1]\n"
        "3. One essential safety/control step to ensure accurate pH comparison [1]"
    )
    correct = "1. Starting pH = 7,0 (neutral distilled water); 2. pH steadily drops below 7 (toward pH 3–5); 3. Use clean neutral distilled water (not tap water) and rinse the probe with distilled water between readings."
    sol = (
        "**Step 1:** Pure neutral distilled water begins at **$\\text{pH} = 7,0$** [1].\n\n"
        f"**Step 2:** As {gas_nm} reacts with water forming acid, **pH decreases below 7** [1].\n\n"
        "**Step 3:** Use pure **distilled water** (tap water buffers pH) and work inside a **fume cupboard** for $SO_2$ [1]."
    )
    return _q(
        rng, "49", "49_controlled_investigation_ph_drop_bubbling_nonmetal_oxide", prompt, correct, sol, 3, "structured",
        ["experimental_control_water_purity_omission"],
        "What is pure distilled water's pH, and why avoid tap water containing dissolved minerals?",
        "Starts at 7,0 -> drops < 7; use distilled water + rinsed pH probe.",
        correct,
    )


def arch_50_comprehensive_nonmetal_oxides_and_acid_rain_synthesis(rng: random.Random) -> Dict[str, Any]:
    fuel_src = rng.choice(["coal-fired station emitting C + S", "industrial sulfur burner alongside carbon fuel"])
    prompt = (
        f"In an integrated Term 2 chemistry test evaluating combustion from a **{fuel_src}**:\n\n"
        "1. Write balanced chemical equations for **carbon** and **sulfur** burning completely in oxygen [2].\n"
        "2. Name one non-metal oxide product whose formula is NOT a dioxide ($\\text{H}_2\\text{O}$ or $\\text{P}_2\\text{O}_5$) [1].\n"
        "3. Describe the laboratory limewater test for $CO_2$ and explain how industrial $SO_2$ triggers limestone erosion downstream [3]."
    )
    correct = "1. C + O2 -> CO2 and S + O2 -> SO2; 2. Water / dihydrogen monoxide (H2O) or diphosphorus pentoxide (P2O5); 3. CO2 turns clear limewater milky via CaCO3 precipitate; SO2 oxidises/dissolves into sulfuric acid rain that dissolves CaCO3 stone."
    sol = (
        "**Step 1:** Balanced equations: **$\\text{C} + \\text{O}_2 \\rightarrow \\text{CO}_2$** and **$\\text{S} + \\text{O}_2 \\rightarrow \\text{SO}_2$** [2].\n\n"
        "**Step 2:** Not all non-metal oxides are dioxides—e.g. **water / dihydrogen monoxide ($\\text{H}_2\\text{O}$)** or **diphosphorus pentoxide ($\\text{P}_2\\text{O}_5$)** [1].\n\n"
        "**Step 3:** $CO_2$ turns clear limewater **milky white** ($\\text{CaCO}_3$ precipitate), while atmospheric $\\text{SO}_2$ converts into **acid rain ($H_2SO_3/H_2SO_4$)** dissolving carbonate buildings and acidifying dams [3]."
    )
    return _q(
        rng, "50", "50_comprehensive_nonmetal_oxides_and_acid_rain_synthesis", prompt, correct, sol, 6, "structured",
        ["nonmetal_oxides_comprehensive_error"],
        "Combine balanced C/S equations, non-dioxide counterexamples, limewater test, and acid-rain impact.",
        "C+O2->CO2; S+O2->SO2; H2O/P2O5; limewater -> CaCO3; acid rain dissolves limestone.",
        correct,
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_sulfur_trioxide_formation_industrial_contact": arch_26_sulfur_trioxide_formation_industrial_contact,
    "27_nonmetal_oxide_water_reaction_carbonic_acid": arch_27_nonmetal_oxide_water_reaction_carbonic_acid,
    "28_nonmetal_oxide_water_reaction_sulfurous_acid": arch_28_nonmetal_oxide_water_reaction_sulfurous_acid,
    "29_nonmetal_oxide_water_reaction_sulfuric_and_nitric_acids": arch_29_nonmetal_oxide_water_reaction_sulfuric_and_nitric_acids,
    "30_nonmetal_oxides_litmus_and_universal_indicator_test": arch_30_nonmetal_oxides_litmus_and_universal_indicator_test,
    "31_comparing_acidic_nonmetal_oxide_vs_basic_metal_oxide_solutions": arch_31_comparing_acidic_nonmetal_oxide_vs_basic_metal_oxide_solutions,
    "32_blowing_exhaled_breath_straw_limewater_and_indicator": arch_32_blowing_exhaled_breath_straw_limewater_and_indicator,
    "33_acid_rain_coal_power_stations_mpumalanga_emissions": arch_33_acid_rain_coal_power_stations_mpumalanga_emissions,
    "34_acid_rain_nitrogen_oxides_transport_emissions": arch_34_acid_rain_nitrogen_oxides_transport_emissions,
    "35_acid_rain_soil_nutrient_leaching_and_aluminium_toxicity": arch_35_acid_rain_soil_nutrient_leaching_and_aluminium_toxicity,
    "36_acid_rain_freshwater_lake_acidification_fish_loss": arch_36_acid_rain_freshwater_lake_acidification_fish_loss,
    "37_acid_rain_corrosion_of_limestone_marble_buildings": arch_37_acid_rain_corrosion_of_limestone_marble_buildings,
    "38_agricultural_lime_soil_and_lake_remediation": arch_38_agricultural_lime_soil_and_lake_remediation,
    "39_scrubber_flue_gas_desulfurisation_power_stations": arch_39_scrubber_flue_gas_desulfurisation_power_stations,
    "40_mass_conservation_in_carbon_combustion_open_vs_closed": arch_40_mass_conservation_in_carbon_combustion_open_vs_closed,
    "41_balancing_nonmetal_combustion_equations_set": arch_41_balancing_nonmetal_combustion_equations_set,
    "42_group_14_and_16_valency_comparison_co2_vs_so2": arch_42_group_14_and_16_valency_comparison_co2_vs_so2,
    "43_diatomic_nonmetal_reactants_h2_n2_o2_recognition": arch_43_diatomic_nonmetal_reactants_h2_n2_o2_recognition,
    "44_identifying_acid_rain_ph_drop_bar_chart_analysis": arch_44_identifying_acid_rain_ph_drop_bar_chart_analysis,
    "45_unpolluted_rainwater_natural_weak_carbonic_acidity": arch_45_unpolluted_rainwater_natural_weak_carbonic_acidity,
    "46_macroscopic_submicroscopic_symbolic_sulfur_combustion": arch_46_macroscopic_submicroscopic_symbolic_sulfur_combustion,
    "47_comparing_gas_tests_o2_h2_co2_diagnostic_key": arch_47_comparing_gas_tests_o2_h2_co2_diagnostic_key,
    "48_catalytic_converters_reducing_co_and_nox_emissions": arch_48_catalytic_converters_reducing_co_and_nox_emissions,
    "49_controlled_investigation_ph_drop_bubbling_nonmetal_oxide": arch_49_controlled_investigation_ph_drop_bubbling_nonmetal_oxide,
    "50_comprehensive_nonmetal_oxides_and_acid_rain_synthesis": arch_50_comprehensive_nonmetal_oxides_and_acid_rain_synthesis,
}
