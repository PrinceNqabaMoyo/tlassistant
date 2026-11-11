"""
Grade 7 Natural Sciences - Term 2: Acids, Bases and Neutral Substances (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/03. Acids bases and neutral substances.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Neutralisation Reactions & Applications (26 - 33)
# ==============================================================================

def arch_26_strong_vs_weak_bases_ph_comparison(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Sodium hydroxide (drain cleaner)", 13, "Baking soda solution", 9),
        ("Potassium hydroxide solution", 14, "Household cloudy ammonia", 11),
        ("Sodium hydroxide solution", 12, "Calcium hydroxide in limewater", 9),
    ]
    s_base, s_ph, w_base, w_ph = rng.choice(pairs)

    prompt = (
        f"Compare two alkaline solutions:\n"
        f"- Base M: {s_base} (pH {s_ph})\n"
        f"- Base N: {w_base} (pH {w_ph})\n\n"
        f"1. Which substance is the **stronger base**? Justify using pH values.\n"
        f"2. Explain what 'base strength' means in terms of how completely the base dissociates to release hydroxide ions ($OH^-$)."
    )
    sol = (
        f"**Step 1:** **Base M ({s_base})** is the stronger base because a higher pH ({s_ph} vs {w_ph}) indicates a much higher concentration of free hydroxide ions ($OH^-$) [1 Mark: Strength & pH].\n\n"
        f"**Step 2:** A strong base **dissociates completely (100%)** in water to release all its $OH^-$ ions, whereas a weak base only partially ionises/dissociates in solution [1 Mark: Dissociation definition]."
    )
    return {
        "id": f"ns7_ab_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Base M ({s_base}); higher pH indicates higher OH- concentration; complete vs partial dissociation",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "26_strong_vs_weak_bases_ph_comparison",
        "misconception_tags": ["base_strength_ph"],
        "hints": {
            "tier_1": "Higher pH (closer to 14) means stronger base.",
            "tier_2": "Strong bases dissociate completely to release hydroxide ions.",
            "tier_3": f"Base M ({s_base}); complete vs partial dissociation."
        }
    }


def arch_27_neutralisation_reaction_word_equation(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        ("Hydrochloric acid", "Sodium hydroxide", "Sodium chloride (table salt)", "Water"),
        ("Hydrochloric acid", "Potassium hydroxide", "Potassium chloride", "Water"),
        ("Sulfuric acid", "Sodium hydroxide", "Sodium sulfate", "Water"),
        ("Nitric acid", "Sodium hydroxide", "Sodium nitrate", "Water"),
    ]
    acid_n, base_n, salt_n, water_n = rng.choice(reactions)

    prompt = (
        f"When an acid reacts chemically with a base, they cancel each other out in a **neutralisation** reaction.\n\n"
        f"1. Write the universal word equation that describes all acid-base neutralisation reactions.\n"
        f"2. Complete the specific word equation for the reaction between **{acid_n}** and **{base_n}**:\n"
        f"   {acid_n} + {base_n} $\\rightarrow$ [Salt] + [Liquid]."
    )
    sol = (
        f"**Step 1:** Universal word equation:\n"
        f"$$\\textbf{{Acid + Base }} \\rightarrow \\textbf{{ Salt + Water}} \\text{{ [1 Mark: Universal equation]}}$$\n\n"
        f"**Step 2:** Specific reaction:\n"
        f"$$\\text{{{acid_n} + {base_n}}} \\rightarrow \\mathbf{{{salt_n} + {water_n}}} \\text{{ [1 Mark: Products]}}$$"
    )
    return {
        "id": f"ns7_ab_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Acid + Base -> Salt + Water; {salt_n} + {water_n}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "27_neutralisation_reaction_word_equation",
        "misconception_tags": ["neutralisation_word_equation"],
        "hints": {
            "tier_1": "Acid + Base gives a salt and water.",
            "tier_2": f"{acid_n} + {base_n} forms {salt_n} and {water_n}.",
            "tier_3": f"Acid + Base -> Salt + Water; {salt_n} + {water_n}."
        }
    }


def arch_28_neutralisation_ph_change_curve(rng: random.Random) -> Dict[str, Any]:
    start_ph = rng.choice([1, 2])
    end_ph = rng.choice([12, 13])

    svg = (
        f'<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<line x1="50" y1="170" x2="350" y2="170" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="50" y1="170" x2="50" y2="20" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="200" y="195" font-family="sans-serif" font-size="11" fill="#1e293b" text-anchor="middle">Volume of base added (mL)</text>'
        f'<text x="20" y="95" font-family="sans-serif" font-size="11" fill="#1e293b" text-anchor="middle" transform="rotate(-90 20 95)">pH Value</text>'
        f'<line x1="45" y1="95" x2="350" y2="95" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>'
        f'<text x="40" y="98" font-family="sans-serif" font-size="10" font-weight="bold" fill="#22c55e" text-anchor="end">pH 7</text>'
        f'<path d="M 50,155 Q 180,150 200,95 T 350,35" fill="none" stroke="#2563eb" stroke-width="3"/>'
        f'<circle cx="200" cy="95" r="5" fill="#22c55e"/>'
        f'<text x="215" y="95" font-family="sans-serif" font-size="10" font-weight="bold" fill="#22c55e">Neutral point (pH 7)</text>'
        f'<text x="60" y="145" font-family="sans-serif" font-size="10" fill="#ef4444">Initial pH: {start_ph}</text>'
        f'<text x="320" y="25" font-family="sans-serif" font-size="10" fill="#8b5cf6" text-anchor="end">Final pH: {end_ph}</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"pH titration curve starting at pH {start_ph} and rising to pH {end_ph}",
        "diagram_role": "context"
    }

    prompt = (
        f"A chemist adds sodium hydroxide alkali drop by drop to a beaker of hydrochloric acid (initial pH {start_ph}).\n\n"
        f"1. Describe what happens to the pH of the acidic solution as alkali is gradually added.\n"
        f"2. What is the pH value at the exact point of complete neutralisation?\n"
        f"3. Explain why the pH eventually levels off near {end_ph} if excess alkali is added."
    )
    sol = (
        f"**Step 1:** The pH **rises (increases)** steadily towards 7 as hydroxide ions neutralise hydrogen ions [1 Mark: Trend].\n\n"
        f"**Step 2:** At complete neutralisation, the pH is exactly **7,0 (neutral)** [1 Mark: Equivalence point].\n\n"
        f"**Step 3:** Once all acid has reacted, any further alkali added remains unreacted in solution, making the mixture strongly basic (pH near {end_ph}) [1 Mark: Excess base]."
    )
    return {
        "id": f"ns7_ab_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"pH increases towards 7; pH = 7,0 at neutral point; excess base leaves unreacted OH- ions raising pH to {end_ph}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "28_neutralisation_ph_change_curve",
        "misconception_tags": ["ph_curve_neutralisation"],
        "hints": {
            "tier_1": "Adding base raises the pH towards 7.",
            "tier_2": "Neutral point is pH 7. Excess base raises pH above 7.",
            "tier_3": f"pH rises; pH 7 at neutral point; excess base raises pH to {end_ph}."
        }
    }


def arch_29_antacids_relieving_stomach_hyperacidity(rng: random.Random) -> Dict[str, Any]:
    antacids = [
        ("Milk of Magnesia (magnesium hydroxide)", "magnesium chloride salt and water"),
        ("Baking soda / Eno (sodium bicarbonate)", "sodium chloride salt, water, and carbon dioxide gas"),
        ("Calcium carbonate tablets (Tums)", "calcium chloride salt, water, and carbon dioxide gas"),
    ]
    remedy, products = rng.choice(antacids)

    prompt = (
        f"Human gastric juice contains dilute hydrochloric acid ($HCl$) with a pH between 1,5 and 2,0 to digest proteins and kill bacteria.\n"
        f"When too much stomach acid is produced, a person suffers from painful indigestion (heartburn).\n\n"
        f"1. Explain how taking an antacid like **{remedy}** relieves heartburn.\n"
        f"2. Name the chemical products formed in the stomach: {products}.\n"
        f"3. Explain why a strong laboratory base like sodium hydroxide ($NaOH$) can NEVER be used as an antacid medicine."
    )
    sol = (
        f"**Step 1:** The antacid is a mild base that **neutralises** the excess hydrochloric acid, bringing stomach pH back to a comfortable level [1 Mark: Neutralisation mechanism].\n\n"
        f"**Step 2:** Chemical products: **{products}** [1 Mark: Products].\n\n"
        f"**Step 3:** Sodium hydroxide is a **strongly caustic base** that would burn and dissolve the delicate mucosal lining of the esophagus and stomach, causing severe internal chemical burns [1 Mark: Caustic hazard]."
    )
    return {
        "id": f"ns7_ab_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Neutralises excess stomach acid; {products}; NaOH is strongly caustic and burns stomach tissue",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "29_antacids_relieving_stomach_hyperacidity",
        "misconception_tags": ["antacid_neutralisation_principle"],
        "hints": {
            "tier_1": "Antacids are mild bases that neutralise excess stomach acid.",
            "tier_2": "Strong bases like NaOH would destroy the stomach lining.",
            "tier_3": "Neutralises acid; produces salt and water; NaOH is too caustic."
        }
    }


def arch_30_treating_insect_stings_bee_vs_wasp(rng: random.Random) -> Dict[str, Any]:
    stings = [
        ("A honeybee sting is acidic (containing formic/methanoic acid and peptide toxins)", "baking soda paste (sodium bicarbonate, a mild base)", "a mild base neutralises the acidic sting poison"),
        ("A common wasp sting is basic / alkaline", "dilute vinegar or lemon juice (a mild acid)", "a mild acid neutralises the alkaline sting venom"),
    ]
    sting_info, remedy, rationale = rng.choice(stings)

    prompt = (
        f"Applying chemistry to outdoor first aid:\n"
        f"Fact: '{sting_info}'.\n\n"
        f"1. Recommend a safe household substance to apply to this sting: **{remedy}**.\n"
        f"2. Explain the scientific principle behind this first-aid treatment.\n"
        f"3. Why would applying vinegar to a bee sting worsen the irritation?"
    )
    sol = (
        f"**Step 1:** Recommended first-aid remedy: **{remedy}** [1 Mark: Remedy].\n\n"
        f"**Step 2:** Scientific principle: {rationale.capitalize()} in a **neutralisation** reaction, relieving pain and tissue swelling [1 Mark: Neutralisation].\n\n"
        f"**Step 3:** Vinegar is acidic; adding more acid to an already acidic bee sting increases the acid concentration and worsens tissue irritation [1 Mark: Incompatibility]."
    )
    return {
        "id": f"ns7_ab_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{remedy}; {rationale}; vinegar adds more acid to an acidic sting, worsening pain",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "30_treating_insect_stings_bee_vs_wasp",
        "misconception_tags": ["bee_vs_wasp_sting_chemistry"],
        "hints": {
            "tier_1": "Neutralise an acid with a base, and neutralise a base with an acid.",
            "tier_2": f"Treatment: {remedy}.",
            "tier_3": f"{remedy}; {rationale}."
        }
    }


def arch_31_agricultural_lime_treating_acid_soils(rng: random.Random) -> Dict[str, Any]:
    crops = [
        ("maize / corn in Mpumalanga", 4.5, 6.5),
        ("wheat in the Western Cape Overberg", 4.8, 6.8),
        ("sugarcane in KwaZulu-Natal", 5.0, 6.5),
    ]
    crop, cur_ph, opt_ph = rng.choice(crops)

    prompt = (
        f"A commercial farmer tests the soil and finds a pH of {cur_ph}, which is too acidic for {crop} (optimum pH {opt_ph}).\n"
        f"The agricultural advisor instructs the farmer to spread **agricultural lime (calcium carbonate / slaked lime)** over the fields.\n\n"
        f"1. Explain why agricultural lime corrects the soil condition.\n"
        f"2. State what happens to soil pH after liming (increases towards 7, or decreases).\n"
        f"3. Name the chemical reaction occurring in the moist topsoil."
    )
    sol = (
        f"**Step 1:** Agricultural lime is a **base (alkaline)** that neutralises excess hydrogen ions in acidic soil [1 Mark: Liming function].\n\n"
        f"**Step 2:** The soil pH **increases** from {cur_ph} towards {opt_ph} [1 Mark: pH increase].\n\n"
        f"**Step 3:** The reaction is **neutralisation** (acid + carbonate/base $\\rightarrow$ salt + water + $CO_2$) [1 Mark: Neutralisation]."
    )
    return {
        "id": f"ns7_ab_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Lime is alkaline and neutralises soil acidity; soil pH increases towards neutral; neutralisation reaction",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "31_agricultural_lime_treating_acid_soils",
        "misconception_tags": ["soil_liming_chemistry"],
        "hints": {
            "tier_1": "Lime is a base. Bases raise the pH of acidic soil.",
            "tier_2": "Soil pH increases; this is a neutralisation reaction.",
            "tier_3": "Lime is basic and neutralises acid; pH increases; neutralisation."
        }
    }


def arch_32_acid_mine_drainage_neutralisation_slaked_lime(rng: random.Random) -> Dict[str, Any]:
    ph_raw = rng.choice([2.5, 3.0])

    prompt = (
        f"Acid mine drainage decanting from an old mine shaft has a measured pH of {str(ph_raw).replace('.', ',')} and carries toxic dissolved heavy metals.\n"
        f"Engineers pump the acidic water into a treatment plant and dose it with **slaked lime (calcium hydroxide, $Ca(OH)_2$)**.\n\n"
        f"1. Explain how slaked lime changes the pH of the contaminated mine water.\n"
        f"2. What happens to the dissolved toxic heavy metals (iron, manganese, aluminium) as the water becomes neutral or slightly alkaline?"
    )
    sol = (
        f"**Step 1:** Slaked lime is an alkali that neutralises the sulfuric acid, raising the water pH from {str(ph_raw).replace('.', ',')} up to neutral (pH 7-8) [1 Mark: pH correction].\n\n"
        f"**Step 2:** At neutral/alkaline pH, dissolved heavy metal ions react to form **insoluble metal hydroxide precipitates (sludge)** that sink to the bottom and are filtered out [1 Mark: Precipitation]."
    )
    return {
        "id": f"ns7_ab_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Neutralises acid and raises pH to 7-8; heavy metals precipitate out as solid insoluble sludge",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "32_acid_mine_drainage_neutralisation_slaked_lime",
        "misconception_tags": ["amd_treatment_precipitation"],
        "hints": {
            "tier_1": "Slaked lime is basic; it neutralises sulfuric acid.",
            "tier_2": "Raising pH causes toxic heavy metals to precipitate as solid sludge.",
            "tier_3": "Raises pH to neutral; heavy metals precipitate out."
        }
    }


def arch_33_toothpaste_preventing_dental_decay(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Tooth enamel consists of calcium hydroxyapatite, which dissolves when mouth pH drops below 5,5.\n\n"
        f"1. How do bacteria living in dental plaque produce acids in our mouth?\n"
        f"2. Explain how brushing with toothpaste (which has a pH of 8 to 9) prevents tooth decay.\n"
        f"3. Name the chemical reaction that occurs between oral plaque acid and alkaline toothpaste."
    )
    sol = (
        f"**Step 1:** Bacteria ferment leftover dietary sugars from food, producing **organic acids (lactic acid)** as metabolic waste [1 Mark: Bacterial fermentation].\n\n"
        f"**Step 2:** Toothpaste is **mildly alkaline / basic**, so it **neutralises** the harmful mouth acids and raises mouth pH safely above 5,5 [1 Mark: Neutralisation role].\n\n"
        f"**Step 3:** The reaction is **neutralisation** [1 Mark: Reaction type]."
    )
    return {
        "id": f"ns7_ab_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Bacteria ferment food sugars into acid; alkaline toothpaste neutralises mouth acid raising pH above 5.5; neutralisation",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "33_toothpaste_preventing_dental_decay",
        "misconception_tags": ["toothpaste_neutralisation"],
        "hints": {
            "tier_1": "Bacteria turn sugar into acid. Toothpaste is a base.",
            "tier_2": "Alkaline toothpaste neutralises the acid.",
            "tier_3": "Ferment sugars into acid; toothpaste neutralises acid; neutralisation."
        }
    }


# ==============================================================================
# CLUSTER 5: Environmental Acidity & Chemical Reactions (34 - 42)
# ==============================================================================

def arch_34_acid_rain_causes_emissions_so2_nox(rng: random.Random) -> Dict[str, Any]:
    pollutants = [
        ("Sulfur dioxide ($SO_2$)", "burning low-grade coal in coal-fired power stations", "sulfuric acid ($H_2SO_4$)"),
        ("Nitrogen oxides ($NO_x$)", "high-temperature combustion in vehicle engines and aircraft", "nitric acid ($HNO_3$)"),
    ]
    gas, source, acid_formed = rng.choice(pollutants)

    prompt = (
        f"Unpolluted clean rainwater has a slightly acidic pH of about 5,6 due to dissolved natural carbon dioxide ($CO_2$).\n"
        f"In industrialized regions (e.g. Mpumalanga Highveld), rainwater pH frequently drops below 4,0 as **acid rain**.\n\n"
        f"1. Name the pollutant gas emitted from {source}: **{gas}**.\n"
        f"2. Name the strong mineral acid formed when this gas dissolves in cloud water droplets: **{acid_formed}**.\n"
        f"3. Write the chemical formula for {gas}."
    )
    sol = (
        f"**Step 1:** Pollutant gas: **{gas}** [1 Mark: Gas].\n\n"
        f"**Step 2:** Acid formed: **{acid_formed}** [1 Mark: Acid].\n\n"
        f"**Step 3:** The gas dissolves in atmospheric moisture and reacts with oxygen to form {acid_formed}, drastically lowering rain pH [1 Mark: Chemistry]."
    )
    return {
        "id": f"ns7_ab_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{gas}; {acid_formed}; reacts with atmospheric moisture",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "34_acid_rain_causes_emissions_so2_nox",
        "misconception_tags": ["acid_rain_gases"],
        "hints": {
            "tier_1": "Coal emissions make sulfur dioxide, car engines make nitrogen oxides.",
            "tier_2": f"Gas is {gas}; forms {acid_formed}.",
            "tier_3": f"{gas}; {acid_formed}."
        }
    }


def arch_35_acid_rain_effects_ecosystems_and_stonework(rng: random.Random) -> Dict[str, Any]:
    targets = [
        ("historic marble and limestone statues ($CaCO_3$)", "acid rain chemically dissolves calcium carbonate stone, eroding fine facial features and lettering"),
        ("freshwater mountain streams and lakes", "acidifies water and leaches toxic aluminium ions from soil into water, suffocating fish and killing amphibians"),
        ("pine and indigenous forest trees", "damages waxy leaf cuticles and strips vital soil nutrients like magnesium and calcium, causing forest dieback"),
    ]
    target, impact = rng.choice(targets)

    prompt = (
        f"Acid rain causes widespread ecological and structural devastation.\n\n"
        f"Consider the impact on: **{target}**.\n\n"
        f"1. Explain the scientific mechanism of damage: {impact}.\n"
        f"2. Suggest ONE engineering or environmental policy strategy to reduce acid rain emissions."
    )
    sol = (
        f"**Step 1:** Mechanism: {impact.capitalize()} [1 Mark: Mechanism].\n\n"
        f"**Step 2:** Policy/engineering (any one): install **flue-gas desulfurisation scrubbers** on coal power station smokestacks, transition to renewable energy (solar/wind), or mandate catalytic converters on vehicles [1 Mark: Remediation]."
    )
    return {
        "id": f"ns7_ab_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{impact}; smokestack scrubbers or transition to renewable energy",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "35_acid_rain_effects_ecosystems_and_stonework",
        "misconception_tags": ["acid_rain_destruction"],
        "hints": {
            "tier_1": "Acid dissolves carbonate stone and kills fish.",
            "tier_2": "Fit smokestack scrubbers or switch to clean renewable energy.",
            "tier_3": f"{impact}; install scrubbers or use renewable energy."
        }
    }


def arch_36_baking_powder_reaction_producing_co2(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Baking powder is a dry mixture containing sodium bicarbonate (a base) and tartaric acid / cream of tartar (a dry acid).\n\n"
        f"1. Explain why baking powder can be stored safely as a dry powder in a tin for months without reacting.\n"
        f"2. What happens the instant liquid (water or milk) is mixed into the dry flour and baking powder batter?\n"
        f"3. Name the gas produced that causes cake batter to rise, creating a light and spongy texture."
    )
    sol = (
        f"**Step 1:** In dry solid form, the molecules are locked in crystal lattices and cannot move or collide to react [1 Mark: Dry stability].\n\n"
        f"**Step 2:** Adding water dissolves the acid and base into solution, freeing ions to collide and undergo an immediate **acid-base neutralisation reaction** [1 Mark: Liquid activation].\n\n"
        f"**Step 3:** The reaction produces bubbles of **carbon dioxide gas ($CO_2$)** that expand when baked, making the cake rise [1 Mark: Gas]."
    )
    return {
        "id": f"ns7_ab_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Dry crystals cannot move to react; water dissolves molecules allowing acid-base reaction; carbon dioxide gas (CO2)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "36_baking_powder_reaction_producing_co2",
        "misconception_tags": ["baking_powder_activation"],
        "hints": {
            "tier_1": "Solids cannot react until dissolved in liquid.",
            "tier_2": "The gas that makes cakes rise is carbon dioxide.",
            "tier_3": "Dry molecules cannot collide; water dissolves them to react; carbon dioxide (CO2)."
        }
    }


def arch_37_acid_reaction_with_metals_hydrogen_gas(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Magnesium ribbon ($Mg$)", "Hydrochloric acid ($HCl$)", "Magnesium chloride ($MgCl_2$)", "rapid vigorous fizzing and heat"),
        ("Zinc granules ($Zn$)", "Sulfuric acid ($H_2SO_4$)", "Zinc sulfate ($ZnSO_4$)", "steady bubbling of gas"),
        ("Iron filings ($Fe$)", "Hydrochloric acid ($HCl$)", "Iron(II) chloride ($FeCl_2$)", "slow bubbling of gas"),
    ]
    metal_n, acid_n, salt_n, observation = rng.choice(metals)

    prompt = (
        f"A learner adds a piece of {metal_n} to a test tube containing dilute {acid_n}.\n\n"
        f"1. Describe the visible observation inside the test tube: {observation}.\n"
        f"2. Name the flammable gas produced in this reaction.\n"
        f"3. Describe the standard laboratory test used to confirm the identity of this gas (the 'pop test')."
    )
    sol = (
        f"**Step 1:** Observation: **{observation.capitalize()}** [1 Mark: Observation].\n\n"
        f"**Step 2:** The gas produced is **hydrogen gas ($H_2$)** [1 Mark: Gas identification].\n\n"
        f"**Step 3:** Bring a burning wooden splint near the mouth of the test tube; hydrogen gas ignites with a characteristic **squeaky 'pop' sound** [1 Mark: Pop test]."
    )
    return {
        "id": f"ns7_ab_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{observation}; Hydrogen gas (H2); burning splint makes a squeaky pop sound",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "37_acid_reaction_with_metals_hydrogen_gas",
        "misconception_tags": ["hydrogen_pop_test"],
        "hints": {
            "tier_1": "Acid + Metal produces hydrogen gas.",
            "tier_2": "The test for hydrogen is the burning splint pop test.",
            "tier_3": f"{observation}; Hydrogen gas; squeaky pop test."
        }
    }


def arch_38_acid_reaction_with_carbonates_co2_gas(rng: random.Random) -> Dict[str, Any]:
    carbonates = [
        ("Calcium carbonate (marble chips / chalk)", "Hydrochloric acid", "Calcium chloride", "Water"),
        ("Sodium bicarbonate (baking soda)", "Ethanoic acid (vinegar)", "Sodium acetate", "Water"),
        ("Copper carbonate powder", "Sulfuric acid", "Copper sulfate", "Water"),
    ]
    carb, acid_n, salt_n, water_n = rng.choice(carbonates)

    prompt = (
        f"When dilute {acid_n} is poured onto **{carb}**, vigorous effervescence occurs.\n\n"
        f"1. Write the general word equation for an acid reacting with a metal carbonate.\n"
        f"2. Name the gas released during this effervescence.\n"
        f"3. Describe the standard chemical test to confirm this gas (bubbling through clear limewater)."
    )
    sol = (
        f"**Step 1:** General word equation:\n"
        f"$$\\textbf{{Acid + Metal Carbonate }} \\rightarrow \\textbf{{ Salt + Water + Carbon Dioxide}} \\text{{ [1 Mark: Word equation]}}$$\n\n"
        f"**Step 2:** The gas released is **carbon dioxide ($CO_2$)** [1 Mark: Gas identification].\n\n"
        f"**Step 3:** Bubble the gas through clear limewater (calcium hydroxide); the limewater turns **milky / cloudy white** due to insoluble calcium carbonate precipitate [1 Mark: Limewater test]."
    )
    return {
        "id": f"ns7_ab_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Acid + Metal Carbonate -> Salt + Water + Carbon Dioxide; Carbon dioxide (CO2); turns clear limewater milky/cloudy",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "38_acid_reaction_with_carbonates_co2_gas",
        "misconception_tags": ["carbonate_co2_limewater_test"],
        "hints": {
            "tier_1": "Acid + Carbonate makes salt, water, and carbon dioxide.",
            "tier_2": "The test for CO2 is bubbling through limewater to turn it milky.",
            "tier_3": "Acid + Carbonate -> Salt + Water + CO2; CO2 turns limewater milky."
        }
    }


def arch_39_safety_diluting_acids_rule_acid_to_water(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In chemistry laboratories, teachers teach the critical 'AAA' safety rule for diluting concentrated acids:\n"
        f"'**Always Add Acid** to water, never add water to acid.'\n\n"
        f"1. Explain the scientific reason why pouring water into concentrated sulfuric acid is extremely dangerous.\n"
        f"2. Why does pouring acid slowly down the side of a glass beaker into a large volume of water prevent accidents?"
    )
    sol = (
        f"**Step 1:** Diluting concentrated acid is an **extremely exothermic reaction** (releases intense heat). If water is poured into acid, the small drop of water instantly boils to steam, causing boiling acid to violently splash and spit into the student's face [1 Mark: Boiling/splattering danger].\n\n"
        f"**Step 2:** When acid is added slowly to a large body of water, the large volume of water absorbs and dissipates the heat safely without boiling [1 Mark: Heat dissipation]."
    )
    return {
        "id": f"ns7_ab_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Reaction is intensely exothermic; adding water to acid boils water instantly spitting acid; adding acid to water dissipates heat safely",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "39_safety_diluting_acids_rule_acid_to_water",
        "misconception_tags": ["always_add_acid_rule"],
        "hints": {
            "tier_1": "Diluting acid releases a lot of heat (exothermic).",
            "tier_2": "Water added to acid boils instantly and splashes acid out.",
            "tier_3": "Exothermic reaction; water boils and spits acid; large water body absorbs heat safely."
        }
    }


def arch_40_first_aid_acid_and_base_spills(rng: random.Random) -> Dict[str, Any]:
    duration = rng.choice([15, 20])
    substance = rng.choice(["concentrated hydrochloric acid", "caustic sodium hydroxide solution"])

    prompt = (
        f"A laboratory learner accidentally knocks over a bottle of {substance}, splashing liquid onto their forearm.\n\n"
        f"1. What is the immediate, non-negotiable first-aid action that must be taken?\n"
        f"2. For how long must the affected skin be flushed under cold running tap water (at least {duration} minutes)?\n"
        f"3. Why should you NEVER attempt to neutralise an acid spill on skin by pouring a concentrated base over it?"
    )
    sol = (
        f"**Step 1:** Immediately flush the affected skin area under a **continuous stream of cold running tap water** [1 Mark: Water flushing].\n\n"
        f"**Step 2:** Flush for at least **{duration} minutes** continuously [1 Mark: Duration].\n\n"
        f"**Step 3:** Neutralisation reactions are **strongly exothermic**; pouring a base on an acid spill generates intense heat that causes severe thermal burns on top of the chemical burns [1 Mark: Thermal burn danger]."
    )
    return {
        "id": f"ns7_ab_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Flush immediately with cold running water for at least {duration} minutes; neutralisation is exothermic and generates intense heat causing thermal burns",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "40_first_aid_acid_and_base_spills",
        "misconception_tags": ["chemical_burn_first_aid"],
        "hints": {
            "tier_1": "Flush with plenty of cold water immediately.",
            "tier_2": f"Flush for {duration} minutes. Neutralising generates heat.",
            "tier_3": f"Flush with cold water for {duration} mins; neutralisation causes thermal burns."
        }
    }


def arch_41_neutralisation_experiment_indicator_colour_endpoint(rng: random.Random) -> Dict[str, Any]:
    indicators = [
        ("Bromothymol blue", "Yellow in acid", "Blue in base", "Green", "#22c55e"),
        ("Litmus solution", "Red in acid", "Blue in base", "Purple", "#8b5cf6"),
    ]
    ind_name, in_acid, in_base, end_color, col_hex = rng.choice(indicators)

    svg = (
        f'<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<path d="M 150,40 L 150,70 L 120,150 Q 115,160 125,160 L 235,160 Q 245,160 240,150 L 210,70 L 210,40 Z" fill="none" stroke="#334155" stroke-width="2"/>'
        f'<path d="M 125,158 L 235,158 Q 242,158 238,150 L 222,110 L 138,110 L 122,150 Q 118,158 125,158 Z" fill="{col_hex}" opacity="0.8"/>'
        f'<text x="180" y="140" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">{end_color} (Endpoint)</text>'
        f'<text x="180" y="185" font-family="sans-serif" font-size="10" fill="#334155" text-anchor="middle">Flask at neutralisation point</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"Neutralisation endpoint showing {end_color} colour with {ind_name}",
        "diagram_role": "context"
    }

    prompt = (
        f"In a quantitative neutralisation experiment, a learner titrates hydrochloric acid with sodium hydroxide using **{ind_name}** indicator.\n\n"
        f"- Colour in initial acid: {in_acid}\n"
        f"- Colour in excess base: {in_base}\n\n"
        f"1. What colour does the solution turn at the exact neutralisation endpoint ({end_color} or otherwise)?\n"
        f"2. Explain what the sudden colour change indicates about the relative amounts of $H^+$ and $OH^-$ ions in the flask."
    )
    sol = (
        f"**Step 1:** The solution turns **{end_color.lower()}** at the neutral point [1 Mark: Endpoint colour].\n\n"
        f"**Step 2:** The colour change indicates that all hydrogen ions ($H^+$) from the acid have been exactly neutralised by hydroxide ions ($OH^-$) from the base, leaving a neutral solution [1 Mark: Ion equivalence]."
    )
    return {
        "id": f"ns7_ab_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{end_color}; all H+ ions have been neutralised by OH- ions into water",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "41_neutralisation_experiment_indicator_colour_endpoint",
        "misconception_tags": ["titration_endpoint_indicator"],
        "hints": {
            "tier_1": f"Bromothymol blue turns {end_color.lower()} at pH 7.",
            "tier_2": "The endpoint means H+ equals OH-.",
            "tier_3": f"{end_color}; H+ and OH- are balanced."
        }
    }


def arch_42_citrus_farming_fruit_acidity_ripening(rng: random.Random) -> Dict[str, Any]:
    fruits = [
        ("Valencia oranges in the Sundays River Valley (Eastern Cape)", 2.8, 3.8),
        ("Grapefruits in Nkwalini (KwaZulu-Natal)", 2.5, 3.5),
        ("Lemons in Citrusdal (Western Cape)", 2.0, 2.6),
    ]
    orchard, unripe_ph, ripe_ph = rng.choice(fruits)

    prompt = (
        f"Citrus export farmers monitor the ripening of fruit:\n"
        f"'{orchard}'.\n\n"
        f"- Unripe fruit: pH {str(unripe_ph).replace('.', ',')}\n"
        f"- Ripe fruit ready for picking: pH {str(ripe_ph).replace('.', ',')}\n\n"
        f"1. As the fruit ripens on the tree, does its acidity **increase** or **decrease**? Justify using pH data.\n"
        f"2. Name the primary acid found in citrus fruits."
    )
    sol = (
        f"**Step 1:** Acidity **decreases** as fruit ripens because the pH value increases from {str(unripe_ph).replace('.', ',')} to {str(ripe_ph).replace('.', ',')} (higher pH means lower acid concentration) [1 Mark: pH trend].\n\n"
        f"**Step 2:** The primary acid is **citric acid** [1 Mark: Acid name]."
    )
    return {
        "id": f"ns7_ab_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Acidity decreases (pH increases from {str(unripe_ph).replace('.', ',')} to {str(ripe_ph).replace('.', ',')}); Citric acid",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "42_citrus_farming_fruit_acidity_ripening",
        "misconception_tags": ["ph_increase_means_less_acidic"],
        "hints": {
            "tier_1": "As pH goes up, acidity goes down.",
            "tier_2": "Citrus fruits contain citric acid.",
            "tier_3": "Acidity decreases; Citric acid."
        }
    }


# ==============================================================================
# CLUSTER 6: Practical Cleaning & Real-World Acidity (43 - 50)
# ==============================================================================

def arch_43_swimming_pool_water_ph_maintenance(rng: random.Random) -> Dict[str, Any]:
    readings = [
        (8.2, "too alkaline / basic", "pool acid (dilute hydrochloric acid)", "lowers pH back to 7,4"),
        (6.5, "too acidic", "soda ash (sodium carbonate, a base)", "raises pH back to 7,4"),
    ]
    cur_ph, condition, remedy, chemical_role = rng.choice(readings)

    prompt = (
        f"The ideal pH range for swimming pool water is strictly between 7,2 and 7,6 to ensure chlorine disinfects effectively and prevent eye stinging.\n\n"
        f"A test kit reveals a pool water pH of **{str(cur_ph).replace('.', ',')}**.\n\n"
        f"1. Is the pool water {condition}?\n"
        f"2. What chemical should the homeowner add to the pool: **{remedy}**?\n"
        f"3. Explain how this added chemical brings the water back into the safe 7,2 - 7,6 range."
    )
    sol = (
        f"**Step 1:** The pool water is **{condition}** [1 Mark: Diagnosis].\n\n"
        f"**Step 2:** The homeowner should add **{remedy}** [1 Mark: Treatment].\n\n"
        f"**Step 3:** The added chemical undergoes a neutralisation adjustment that {chemical_role} [1 Mark: pH adjustment]."
    )
    return {
        "id": f"ns7_ab_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{condition}; {remedy}; {chemical_role}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "43_swimming_pool_water_ph_maintenance",
        "misconception_tags": ["swimming_pool_ph_balance"],
        "hints": {
            "tier_1": "Target is 7.2 to 7.6. If too high add acid; if too low add soda ash.",
            "tier_2": f"Current pH {cur_ph} is {condition}.",
            "tier_3": f"{condition}; {remedy}; {chemical_role}."
        }
    }


def arch_44_vinegar_as_descaling_agent_kettles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In areas with 'hard water', electric kettles develop a hard white crust of limescale (calcium carbonate, $CaCO_3$) on heating elements.\n\n"
        f"1. Explain why boiling dilute vinegar (ethanoic acid) inside the kettle easily removes this limescale.\n"
        f"2. Name the gas produced that fizzes during this descaling cleaning process.\n"
        f"3. State the universal reaction type: $\\text{{Acid}} + \\text{{Metal Carbonate}} \\rightarrow \\text{{Salt}} + \\text{{Water}} + \\text{{Carbon Dioxide}}$."
    )
    sol = (
        f"**Step 1:** The ethanoic acid in vinegar reacts chemically with insoluble calcium carbonate limescale, converting it into soluble calcium acetate salt and water that washes away easily [1 Mark: Descaling chemistry].\n\n"
        f"**Step 2:** The fizzing gas is **carbon dioxide ($CO_2$)** [1 Mark: Gas].\n\n"
        f"**Step 3:** The reaction type is **acid-carbonate reaction** (neutralisation) [1 Mark: Reaction type]."
    )
    return {
        "id": f"ns7_ab_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Vinegar reacts with calcium carbonate to form soluble salt and water; carbon dioxide gas (CO2); acid-carbonate reaction",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "44_vinegar_as_descaling_agent_kettles",
        "misconception_tags": ["descaling_kettle_chemistry"],
        "hints": {
            "tier_1": "Vinegar is an acid; limescale is a carbonate.",
            "tier_2": "Acid dissolves carbonate, releasing CO2.",
            "tier_3": "Dissolves insoluble carbonate into soluble salt; CO2 gas; acid-carbonate reaction."
        }
    }


def arch_45_rust_removal_with_phosphoric_acid(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Commercial rust converter sprays used on rusted iron security gates contain dilute **phosphoric acid ($H_3PO_4$)**.\n\n"
        f"1. Rust is chemically hydrated iron(III) oxide ($Fe_2O_3$). Explain how phosphoric acid chemically transforms reddish, flaky rust into a stable, black protective barrier coating.\n"
        f"2. Name the black chemical substance formed on the iron surface (iron(III) phosphate).\n"
        f"3. Explain why this black coating prevents further rusting from taking place."
    )
    sol = (
        f"**Step 1:** Phosphoric acid reacts chemically with porous iron oxide, converting it into an insoluble, tightly adhering **iron(III) phosphate** layer [1 Mark: Reaction].\n\n"
        f"**Step 2:** The black compound is **iron(III) phosphate ($FePO_4$)** [1 Mark: Compound].\n\n"
        f"**Step 3:** The dense black layer seals the underlying iron metal, blocking water and oxygen from contacting the raw iron surface [1 Mark: Rust prevention]."
    )
    return {
        "id": f"ns7_ab_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Converts rust into iron(III) phosphate; iron(III) phosphate; acts as a barrier sealing iron from moisture and oxygen",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "45_rust_removal_with_phosphoric_acid",
        "misconception_tags": ["rust_conversion_chemistry"],
        "hints": {
            "tier_1": "Phosphoric acid turns reddish rust into black iron phosphate.",
            "tier_2": "The black phosphate seals the metal against water and air.",
            "tier_3": "Converts iron oxide to iron phosphate; blocks oxygen and water."
        }
    }


def arch_46_comparing_cleaning_agents_acidic_vs_alkaline(rng: random.Random) -> Dict[str, Any]:
    cleaners = [
        ("Oven cleaner / caustic degreaser", "Strong base / alkali (NaOH, pH 13)", "greasy, burnt animal fats and baked-on oils"),
        ("Toilet bowl descaler cleaner", "Strong acid (HCl / sulfamic acid, pH 1-2)", "mineral limescale, rust rings, and hard-water deposits"),
    ]
    c1, c2 = cleaners[0], cleaners[1]

    prompt = (
        f"Different household cleaning tasks require specific chemical properties:\n"
        f"- Product A: {c1[0]} ({c1[1]})\n"
        f"- Product B: {c2[0]} ({c2[1]})\n\n"
        f"1. Explain why Product A is chosen to clean {c1[2]}.\n"
        f"2. Explain why Product B is chosen to clean {c2[2]}.\n"
        f"3. Explain why mixing toilet bowl cleaner with bleach produces lethal chlorine gas and must never be done."
    )
    sol = (
        f"**Step 1:** Product A is alkaline; bases react with and **saponify/dissolve fats, grease, and oils** into soluble soap [1 Mark: Alkaline cleaner].\n\n"
        f"**Step 2:** Product B is acidic; acids chemically **react with and dissolve alkaline mineral carbonates** and rust stains [1 Mark: Acid cleaner].\n\n"
        f"**Step 3:** Acid reacts with the sodium hypochlorite in bleach to release toxic, choking **chlorine gas ($Cl_2$)**, which can cause fatal lung injury [1 Mark: Hazardous mixing]."
    )
    return {
        "id": f"ns7_ab_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Bases dissolve fats and grease; acids dissolve mineral limescale; mixing acid with bleach releases toxic chlorine gas",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "46_comparing_cleaning_agents_acidic_vs_alkaline",
        "misconception_tags": ["bleach_acid_mixing_danger"],
        "hints": {
            "tier_1": "Bases clean grease; acids clean limescale.",
            "tier_2": "Never mix bleach and acid: it makes toxic chlorine gas.",
            "tier_3": "Bases dissolve grease; acids dissolve limescale; releases chlorine gas."
        }
    }


def arch_47_evaluating_experimental_reliability_indicators(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During a practical science assessment on testing household acids and bases with indicators:\n\n"
        f"1. Why should learners place their spot plate or test tubes against a clean **white tile or white paper background**?\n"
        f"2. Why must learners rinse their dropper pipette thoroughly with distilled water between sampling different liquids?\n"
        f"3. Why should every test be repeated at least three times?"
    )
    sol = (
        f"**Step 1:** A white background provides maximum contrast to clearly and accurately observe subtle colour changes in indicator solutions [1 Mark: Visual contrast].\n\n"
        f"**Step 2:** Rinsing prevents cross-contamination of acids into bases or vice versa, which would neutralise samples and invalidate test results [1 Mark: Contamination control].\n\n"
        f"**Step 3:** Repeating trials verifies consistency and ensures **reliability / repeatability** of experimental results [1 Mark: Scientific inquiry]."
    )
    return {
        "id": f"ns7_ab_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "White background gives contrast to see color changes; rinsing prevents cross-contamination; repeating ensures reliability",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "47_evaluating_experimental_reliability_indicators",
        "misconception_tags": ["indicator_testing_reliability"],
        "hints": {
            "tier_1": "White background lets you see true color. Rinsing stops contamination.",
            "tier_2": "Repeating trials ensures reliability.",
            "tier_3": "White tile provides contrast; rinsing avoids cross-contamination; repeats ensure reliability."
        }
    }


def arch_48_investigating_ph_of_common_beverages(rng: random.Random) -> Dict[str, Any]:
    drinks = [
        ("Cola fizzy drink", 2.5, "Strongly acidic", "contains phosphoric and carbonic acid; erodes tooth enamel"),
        ("Fresh orange juice", 3.5, "Acidic", "contains citric and ascorbic acid"),
        ("Fresh cow's milk", 6.6, "Very weakly acidic / near neutral", "contains lactic acid and proteins"),
        ("Pure tap water", 7.0, "Neutral", "equal H+ and OH- ions"),
    ]
    rng.shuffle(drinks)
    d1, d2 = drinks[0], drinks[1]

    prompt = (
        f"A learner measures the pH of common beverages:\n"
        f"- Beverage 1: {d1[0]} (pH {str(d1[1]).replace('.', ',')})\n"
        f"- Beverage 2: {d2[0]} (pH {str(d2[1]).replace('.', ',')})\n\n"
        f"1. Which of these two beverages is more acidic? Justify using the pH numbers.\n"
        f"2. Explain why frequent sipping of acidic fizzy drinks causes tooth erosion even if they are 'sugar-free'."
    )
    more_acidic = d1[0] if d1[1] < d2[1] else d2[0]
    sol = (
        f"**Step 1:** **{more_acidic}** is more acidic because it has the lower pH value ({str(min(d1[1], d2[1])).replace('.', ',')} vs {str(max(d1[1], d2[1])).replace('.', ',')}) [1 Mark: Comparison].\n\n"
        f"**Step 2:** Fizzy drinks contain carbonic and phosphoric acids that lower oral pH below 5,5, directly chemically dissolving calcium minerals in tooth enamel even without bacterial sugar fermentation [1 Mark: Acid erosion]."
    )
    return {
        "id": f"ns7_ab_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{more_acidic}; low pH directly dissolves tooth enamel minerals",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "48_investigating_ph_of_common_beverages",
        "misconception_tags": ["beverage_acidity_tooth_decay"],
        "hints": {
            "tier_1": "Lower pH means more acidic.",
            "tier_2": "Acids dissolve calcium in tooth enamel directly.",
            "tier_3": f"{more_acidic}; direct acid erosion."
        }
    }


def arch_49_troubleshooting_indicator_test_anomalies(rng: random.Random) -> Dict[str, Any]:
    anomalies = [
        ("When testing commercial chlorine bleach with red litmus paper, the paper briefly turns blue and then immediately turns completely white.", "Chlorine bleach is an oxidizing agent that destroys the dye molecules (bleaches them white), destroying the indicator."),
        ("When testing dry baking soda powder with dry red litmus paper, no colour change occurs at all.", "Litmus paper requires water/moisture to dissolve the solid base and release OH- ions to trigger the chemical colour change."),
    ]
    observation, explanation = rng.choice(anomalies)

    prompt = (
        f"A science learner encounters an unexpected result during a practical indicator test:\n"
        f"'{observation}'.\n\n"
        f"1. Provide the scientific explanation for this anomaly: {explanation}.\n"
        f"2. How should the student modify their procedure to perform a valid test?"
    )
    sol = (
        f"**Step 1:** Explanation: {explanation} [1 Mark: Anomaly explanation].\n\n"
        f"**Step 2:** Modification: Either dissolve the dry powder in water / moisten the litmus paper first, or use a digital pH meter rather than dye-based indicators [1 Mark: Corrective action]."
    )
    return {
        "id": f"ns7_ab_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{explanation}; dissolve sample in water or use digital pH probe",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "49_troubleshooting_indicator_test_anomalies",
        "misconception_tags": ["indicator_limitations_bleach_dry"],
        "hints": {
            "tier_1": "Bleach bleaches dyes white; dry powder needs water to react.",
            "tier_2": f"Explanation: {explanation}.",
            "tier_3": f"{explanation}; moisten paper or dissolve powder."
        }
    }


def arch_50_comprehensive_acid_base_neutral_classification_matrix(rng: random.Random) -> Dict[str, Any]:
    matrix = [
        {"sample": "Sample 1", "litmus": "Blue litmus turns red", "cabbage": "Red/pink", "ph": 2, "class": "Strong Acid"},
        {"sample": "Sample 2", "litmus": "Neither litmus changes colour", "cabbage": "Purple", "ph": 7, "class": "Neutral"},
        {"sample": "Sample 3", "litmus": "Red litmus turns blue", "cabbage": "Green/Yellow", "ph": 12, "class": "Strong Base"},
    ]
    rng.shuffle(matrix)

    tbl = (
        "| Sample | Litmus Test | Red Cabbage Indicator | Measured pH |\n"
        "| :--- | :--- | :--- | :---: |\n"
    )
    for m in matrix:
        tbl += f"| {m['sample']} | {m['litmus']} | {m['cabbage']} | {m['ph']} |\n"

    acid_s = [m for m in matrix if m["class"] == "Strong Acid"][0]["sample"]
    neut_s = [m for m in matrix if m["class"] == "Neutral"][0]["sample"]
    base_s = [m for m in matrix if m["class"] == "Strong Base"][0]["sample"]

    prompt = (
        f"A laboratory analyst compiles diagnostic data for three unknown samples:\n\n"
        f"{tbl}\n"
        f"Classify each sample as a **Strong Acid**, a **Strong Base**, or **Neutral**:\n"
        f"1. {acid_s}\n"
        f"2. {neut_s}\n"
        f"3. {base_s}"
    )
    sol = (
        f"**Step 1:** **{acid_s}** is a **Strong Acid** (turns blue litmus red, red cabbage turns pink/red, pH 2) [1 Mark].\n\n"
        f"**Step 2:** **{neut_s}** is **Neutral** (no litmus change, purple cabbage, pH 7) [1 Mark].\n\n"
        f"**Step 3:** **{base_s}** is a **Strong Base** (turns red litmus blue, cabbage turns yellow/green, pH 12) [1 Mark]."
    )
    return {
        "id": f"ns7_ab_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{acid_s}: Strong Acid; {neut_s}: Neutral; {base_s}: Strong Base",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "50_comprehensive_acid_base_neutral_classification_matrix",
        "misconception_tags": ["multi_indicator_classification_matrix"],
        "hints": {
            "tier_1": "pH 2 is acid, pH 7 is neutral, pH 12 is base.",
            "tier_2": f"{acid_s} is Strong Acid, {neut_s} is Neutral, {base_s} is Strong Base.",
            "tier_3": f"{acid_s}: Strong Acid; {neut_s}: Neutral; {base_s}: Strong Base."
        }
    }
