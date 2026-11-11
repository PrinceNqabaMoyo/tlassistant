"""Grade 7 Natural Sciences: Term 3 - Sources of Energy (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/01. Sources of energy.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _clean_options(correct: str, distractors: List[str], rng: random.Random) -> List[str]:
    opts = [correct] + [d for d in distractors if d != correct][:3]
    rng.shuffle(opts)
    return opts


# 01. Concept of an energy source
def arch_01_concept_of_energy_source(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("petrol stored in a car's fuel tank", "chemical potential energy", "make the engine run and move the vehicle"),
        ("coal supplied to a thermal power station", "chemical potential energy", "boil water into high-pressure steam to spin turbines"),
        ("food digested by an active human athlete", "chemical potential energy", "power muscular movement and maintain body temperature"),
        ("water held behind a high mountain dam wall", "gravitational potential energy", "drive hydroelectric turbines as it falls downstream"),
    ]
    substance, energy_form, purpose = rng.choice(examples)
    prompt = (
        f"In Natural Sciences, we define an **energy source** as any substance, system, or organism "
        f"that stores energy which can be released to make something happen.\n\n"
        f"Consider **{substance}**.\n"
        f"Which type of stored energy does this source contain, and what useful action does it perform?"
    )
    correct = f"It stores {energy_form} that is released to {purpose}."
    distractors = [
        f"It stores nuclear kinetic energy that is destroyed to {purpose}.",
        f"It contains zero energy until electrical current from a wall plug enters it.",
        f"It stores magnetic potential energy that cools down the system without doing work.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Step 1: Scientific Definition:**\n"
        f"An energy source stores energy internally (often as chemical or potential energy).\n\n"
        f"**Step 2: Specific Application:**\n"
        f"{substance.capitalize()} contains **{energy_form}**. When utilized, this energy is converted to **{purpose}**."
    )
    return {
        "id": f"ns7_en_01_{rng.randint(100000, 999999)}",
        "subskill": "01_concept_of_energy_source",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_01",
        "hints": {
            "tier_1": "Recall that fuels and food store chemical energy in their bonds.",
            "tier_2": "Energy sources store potential energy that converts into motion, heat, or electricity.",
            "tier_3": f"Identify the option describing {energy_form}.",
        },
        "misconception_tags": ["energy_created_from_nothing", "energy_fuel_identity_confusion"],
    }


# 02. Renewable definition and criterion
def arch_02_renewable_definition_and_criterion(rng: random.Random) -> Dict[str, Any]:
    timescales = [
        ("solar radiation from the Sun", "the Sun's nuclear fusion processes will continue for billions of years"),
        ("wind kinetic energy", "atmospheric heating by the Sun continuously sets air masses into motion"),
        ("falling water in a river catchment", "the natural hydrological cycle continuously evaporates and replenishes rainwater"),
        ("biogas from livestock manure", "livestock continuously generate biological organic waste every day"),
    ]
    source_name, natural_cycle = rng.choice(timescales)
    prompt = (
        f"A Grade 7 science class investigates sustainable energy options in South Africa.\n\n"
        f"Why is **{source_name}** classified scientifically as a **renewable energy source**?"
    )
    correct = f"It is replenished naturally by Earth's cycles and will not be permanently depleted over human timescales."
    distractors = [
        "It can be extracted once from deep underground rock formations and never needs replacing.",
        "It generates 100% free electricity without requiring any machinery or turbines.",
        "It is manufactured artificially in chemical laboratories from non-organic minerals.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Step 1: Understand Renewable Energy:**\n"
        f"Renewable resources are replenished naturally by ongoing natural cycles (e.g. sunlight, water cycle, biological digestion).\n\n"
        f"**Step 2: Analysis of {source_name}:**\n"
        f"Because {natural_cycle}, it cannot be permanently exhausted by human consumption."
    )
    return {
        "id": f"ns7_en_02_{rng.randint(100000, 999999)}",
        "subskill": "02_renewable_definition_and_criterion",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_02",
        "hints": {
            "tier_1": "Think about whether this resource will run out when we use it today.",
            "tier_2": "Renewable means nature replaces it at the same or faster rate than we consume it.",
            "tier_3": "Select the option emphasizing natural ongoing replenishment.",
        },
        "misconception_tags": ["renewable_means_recyclable_plastic", "infinite_energy_confusion"],
    }


# 03. Non-renewable definition and criterion
def arch_03_nonrenewable_definition_and_criterion(rng: random.Random) -> Dict[str, Any]:
    minerals = [
        ("bituminous coal seams in Mpumalanga", "hundreds of millions of years"),
        ("crude petroleum oil beneath offshore seabed formations", "tens of millions of years"),
        ("uranium ore deposits in the Karoo rocks", "geological planetary formation eras"),
        ("methane-rich underground natural gas pockets", "millions of years"),
    ]
    mineral_name, duration = rng.choice(minerals)
    prompt = (
        f"Engineers monitor South Africa's reserves of **{mineral_name}**.\n\n"
        f"What is the primary scientific reason for classifying this resource as **non-renewable**?"
    )
    correct = f"It takes {duration} to form, so it is consumed far faster than nature can replace it."
    distractors = [
        "It releases zero chemical energy when ignited or combusted.",
        "It is toxic to touch and therefore banned from industrial power generation.",
        "It dissolves completely whenever it comes into contact with atmospheric moisture.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Step 1: Definition of Non-renewable Resource:**\n"
        f"A non-renewable resource exists in finite amounts on Earth. Natural geological formation requires {duration}.\n\n"
        f"**Step 2: Rate of Consumption vs Rate of Formation:**\n"
        f"Humans consume these reserves in decades, whereas nature takes millions of years to make them. Hence, they will eventually run out."
    )
    return {
        "id": f"ns7_en_03_{rng.randint(100000, 999999)}",
        "subskill": "03_nonrenewable_definition_and_criterion",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_03",
        "hints": {
            "tier_1": "Consider the geological time needed to create fossil fuels and uranium.",
            "tier_2": "If we use up all the deposits today, can Earth remake them before next century?",
            "tier_3": f"Notice the formation timescale of {duration}.",
        },
        "misconception_tags": ["nonrenewable_means_non_reusable_object", "fossil_fuel_replenishment_myth"],
    }


# 04. Classify solar and wind energy
def arch_04_classify_solar_and_wind_energy(rng: random.Random) -> Dict[str, Any]:
    provinces = [
        ("Upington in the Northern Cape", "solar photovoltaic panels", "radiant light from the Sun"),
        ("Jeffreys Bay in the Eastern Cape", "utility-scale wind turbines", "moving air currents"),
        ("De Aar in the Karoo", "concentrated solar collectors", "direct sunlight"),
        ("Vredendal in the Western Cape", "onshore wind generators", "coastal kinetic wind energy"),
    ]
    location, tech, energy_type = rng.choice(provinces)
    prompt = (
        f"At **{location}**, engineers installed **{tech}** that harness **{energy_type}** to supply electricity to the national grid.\n\n"
        f"How should this energy source be categorized, and why?"
    )
    correct = f"Renewable, because {energy_type} is inexhaustible and continually available via natural cycles."
    distractors = [
        f"Non-renewable, because {tech} degrade after 25 years and cannot harness energy anymore.",
        f"Non-renewable, because the electrical current produced exhausts local atmospheric oxygen.",
        f"Neither renewable nor non-renewable, because electricity from weather does not count as real power.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Classification:**\n"
        f"Both solar and wind rely on natural environmental energy flows driven by the Sun.\n"
        f"Because {energy_type} cannot be depleted permanently, it is strictly **Renewable**."
    )
    return {
        "id": f"ns7_en_04_{rng.randint(100000, 999999)}",
        "subskill": "04_classify_solar_and_wind_energy",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_04",
        "hints": {
            "tier_1": "Will the Sun stop shining or the wind stop blowing because we generated power today?",
            "tier_2": "Equipment lifespan does not change whether the source itself is renewable.",
            "tier_3": "Choose the option categorizing it as Renewable due to natural cycles.",
        },
        "misconception_tags": ["hardware_wear_confused_with_source_depletion"],
    }


# 05. Classify coal and petroleum
def arch_05_classify_coal_and_petroleum(rng: random.Random) -> Dict[str, Any]:
    fuels = [
        ("Highveld bituminous coal", "mined in Witbank (eMalahleni)", "solid fossil fuel"),
        ("Sasol synthetic crude and imported petroleum oil", "refined in Secunda and Durban", "liquid hydrocarbon fuel"),
        ("Anthracite coal", "extracted from underground deposits in KwaZulu-Natal", "high-carbon solid fuel"),
        ("Automotive diesel fuel", "distilled from crude petroleum", "refined liquid fuel"),
    ]
    name, origin, state = rng.choice(fuels)
    prompt = (
        f"Consider **{name}**, which is {origin} and utilized as a {state}.\n\n"
        f"State whether this energy resource is **renewable** or **non-renewable**, and give the correct scientific reason."
    )
    correct = f"Non-renewable, because it formed over millions of years from ancient organic remains and exists in limited supply."
    distractors = [
        "Renewable, because new deposits form underground whenever rain falls on mining heaps.",
        "Renewable, because burning fossil fuels recycles carbon atoms instantly back into combustible oil.",
        "Non-renewable, because it produces electrical current only during daytime hours.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Step 1: Identify origin:**\n"
        f"{name} is derived from fossilized organic matter formed millions of years ago.\n\n"
        f"**Step 2: Classification:**\n"
        f"Because the existing underground reserves are finite and take geological epochs to form, it is **Non-renewable**."
    )
    return {
        "id": f"ns7_en_05_{rng.randint(100000, 999999)}",
        "subskill": "05_classify_coal_and_petroleum",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_05",
        "hints": {
            "tier_1": "Recall how coal and crude oil were created.",
            "tier_2": "Fossil fuels take millions of years of heat and pressure to form.",
            "tier_3": "Select Non-renewable based on finite supply and ancient organic origins.",
        },
        "misconception_tags": ["fossil_fuels_regenerate_in_soil", "infinite_coal_myth"],
    }


# 06. Classify natural gas and methane
def arch_06_classify_natural_gas_and_methane(rng: random.Random) -> Dict[str, Any]:
    contexts = [
        ("deep geological rock reservoirs in the Karoo basin", "mined natural gas (fossil methane)", "Non-renewable", "geological time (>100 million years)"),
        ("an anaerobic agricultural biogas digester on a Free State dairy farm", "biogas (biological methane)", "Renewable", "ongoing daily breakdown of cattle manure"),
    ]
    origin, label, classification, reason = rng.choice(contexts)
    prompt = (
        f"Methane gas (\\(\\text{{CH}}_4\\)) is an efficient combustible fuel.\n\n"
        f"A sample of methane is obtained from **{origin}** as **{label}**.\n"
        f"How is this specific source of methane classified?"
    )
    correct = f"{classification}, because its replenishment depends on {reason}."
    distractor_cat = "Renewable" if classification == "Non-renewable" else "Non-renewable"
    distractors = [
        f"{distractor_cat}, because all gaseous fuels are legally classified as identical regardless of origin.",
        f"{distractor_cat}, because methane molecules cannot be burned in oxygen.",
        f"{classification}, but only if the temperature underground stays below freezing point.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Critical Scientific Distinction:**\n"
        f"- Methane from geological deposits (natural gas) took millions of years to form -> **Non-renewable**.\n"
        f"- Methane produced in biodigesters from animal/plant waste is produced continuously -> **Renewable**.\n\n"
        f"Therefore, {label} from {origin} is **{classification}** because replenishment relies on {reason}."
    )
    return {
        "id": f"ns7_en_06_{rng.randint(100000, 999999)}",
        "subskill": "06_classify_natural_gas_and_methane",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_06",
        "hints": {
            "tier_1": "Pay attention to where this methane comes from: deep underground or a farm digester?",
            "tier_2": "Fossil gas is finite; farm biogas is continuously generated by animal waste.",
            "tier_3": f"This source is {classification}.",
        },
        "misconception_tags": ["gas_is_always_fossil", "methane_cannot_be_renewable"],
    }


# 07. Classify nuclear uranium fuel
def arch_07_classify_nuclear_uranium_fuel(rng: random.Random) -> Dict[str, Any]:
    isotopes = [
        ("Uranium ore", "Koeberg Nuclear Power Station near Cape Town"),
        ("Enriched uranium fuel rods", "a commercial nuclear reactor core"),
    ]
    fuel, facility = rng.choice(isotopes)
    prompt = (
        f"**{fuel}** is used at **{facility}** to generate electricity via nuclear fission.\n\n"
        f"Although a very small mass of uranium releases a vast amount of energy, why is uranium classified as a **non-renewable** resource?"
    )
    correct = "Earth has a finite quantity of uranium mineral deposits that cannot be regenerated naturally once mined and used."
    distractors = [
        "Uranium fuel rods dissolve into steam during the first ten minutes of operation.",
        "Nuclear energy emits excessive quantities of black smoke and soot into the air.",
        "Uranium is an artificial plastic polymer synthesized from crude petroleum oil.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Scientific Explanation:**\n"
        f"Uranium is a naturally occurring heavy metallic element (atomic number 92) found in Earth's crust.\n"
        f"Because the planet contains a strictly **finite supply** of uranium ore that does not replenish, it is classified as **Non-renewable**."
    )
    return {
        "id": f"ns7_en_07_{rng.randint(100000, 999999)}",
        "subskill": "07_classify_nuclear_uranium_fuel",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_07",
        "hints": {
            "tier_1": "Is uranium an element mined from rocks, or does it grow like a plant?",
            "tier_2": "It is an element mined from the Earth, so its total quantity is finite.",
            "tier_3": "Choose the answer stating uranium has a finite mineral supply.",
        },
        "misconception_tags": ["nuclear_energy_is_renewable_myth", "uranium_infinite_resource"],
    }


# 08. Classify biofuels wood and manure
def arch_08_classify_biofuels_wood_and_manure(rng: random.Random) -> Dict[str, Any]:
    bio_types = [
        ("firewood harvested from managed forestry plantations", "trees can be replanted and grown repeatedly over decades"),
        ("sugarcane bagasse burned in boilers at KwaZulu-Natal sugar mills", "new sugarcane crops are planted and harvested every season"),
        ("biodiesel manufactured from sunflower seed oil", "sunflower crops can be cultivated annually"),
        ("cattle manure converted to combustible gas in an agricultural digester", "livestock produce manure continuously every day"),
    ]
    bio_source, repl_reason = rng.choice(bio_types)
    prompt = (
        f"In rural and agricultural communities in South Africa, **{bio_source}** is utilized for thermal heating and cooking.\n\n"
        f"Under what condition is this biomass fuel classified as a **renewable** energy source?"
    )
    correct = f"It is renewable provided that {repl_reason} at a rate equal to or greater than its consumption."
    distractors = [
        "It is always non-renewable because all solid fuels release smoke when ignited.",
        "It is renewable only if it is converted into electrical batteries before being burned.",
        "It is non-renewable because living organisms cannot store chemical potential energy.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Biomass Sustainability Condition:**\n"
        f"Biofuels originate from living organisms. They are **renewable** if harvested sustainably—meaning {repl_reason}.\n"
        f"If trees are cut down faster than they are replanted (deforestation), the supply diminishes."
    )
    return {
        "id": f"ns7_en_08_{rng.randint(100000, 999999)}",
        "subskill": "08_classify_biofuels_wood_and_manure",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_08",
        "hints": {
            "tier_1": "Can humans grow more crops or trees to replace what was burned?",
            "tier_2": "Biomass is renewable when replanting keeps pace with consumption.",
            "tier_3": f"Select the option highlighting sustainable replenishment: {repl_reason}.",
        },
        "misconception_tags": ["wood_is_always_nonrenewable", "biofuel_cannot_be_exhausted"],
    }


# 09. Fossil fuel formation coal swamps
def arch_09_fossil_fuel_formation_coal_swamps(rng: random.Random) -> Dict[str, Any]:
    geological_eras = [
        ("Carboniferous era (~300 million years ago)", "ancient giant fern and tree swamps", "Mpumalanga Highveld"),
        ("Permian period (~260 million years ago)", "dense prehistoric wetlands", "Waterberg basin in Limpopo"),
    ]
    era, vegetation, region = rng.choice(geological_eras)
    prompt = (
        f"Geologists study the vast coal reserves in the **{region}** of South Africa.\n\n"
        f"Which sequence accurately describes how **coal deposits** formed from {era}?"
    )
    correct = (
        "Dead swamp vegetation died -> buried in oxygen-poor water preventing decay -> "
        "covered by sediment layers -> immense heat and pressure converted peat into coal."
    )
    distractors = [
        "Volcanic lava poured over dinosaur skeletons -> cooled instantly into black rocks on the surface.",
        "Ocean salt water reacted with sandy desert dunes over two centuries -> crystallized into carbon coal.",
        "Rainwater dissolved atmospheric nitrogen into mud -> turned into black minerals after severe lightning strikes.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Stages of Coal Formation:**\n"
        f"1. **Vegetation dies:** In {vegetation}, dead plants sank into stagnant, oxygen-poor swamp water, forming peat.\n"
        f"2. **Sedimentation:** Mud, sand, and silt buried the plant matter over millions of years.\n"
        f"3. **Heat and Pressure:** Deep tectonic compression and geothermal heat drove out moisture and volatile gases, transforming peat into lignite, bituminous coal, and anthracite."
    )
    return {
        "id": f"ns7_en_09_{rng.randint(100000, 999999)}",
        "subskill": "09_fossil_fuel_formation_coal_swamps",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_09",
        "hints": {
            "tier_1": "Coal formed from ancient plant life in swamps, not dinosaurs.",
            "tier_2": "Look for the key environmental conditions: waterlogged bogs, lack of oxygen, burial, heat, and pressure.",
            "tier_3": "Choose the sequential stages from dead swamp vegetation to compressed coal.",
        },
        "misconception_tags": ["coal_formed_from_dinosaurs", "coal_formed_by_volcanoes"],
    }


# 10. Fossil fuel formation crude oil marine
def arch_10_fossil_fuel_formation_crude_oil_marine(rng: random.Random) -> Dict[str, Any]:
    sea_sites = [
        ("offshore Outeniqua basin south of Mossel Bay", "microscopic plankton and algae in ancient warm oceans"),
        ("the west coast Orange basin offshore deposits", "prehistoric marine microorganisms settling on ocean floors"),
    ]
    site, organisms = rng.choice(sea_sites)
    prompt = (
        f"South Africa explores offshore petroleum reserves in the **{site}**.\n\n"
        f"What was the original biological source of **crude petroleum oil**, and how did it form?"
    )
    correct = (
        f"Dead {organisms} settled on ancient sea beds, were covered by silt and mud, "
        f"and were converted into liquid hydrocarbons under intense geothermal heat and pressure over millions of years."
    )
    distractors = [
        "Giant terrestrial mammals were trapped inside limestone caves and melted into oil during volcanic eruptions.",
        "Deep ocean seawater chemically reacted with salt crystals to produce flammable oily liquids over the last decade.",
        "Sunlight decomposed plastic waste floating in oceans during prehistoric ice ages into crude oil.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Formation of Petroleum (Crude Oil):**\n"
        f"Unlike coal (which came from land plants), crude oil formed primarily from {organisms}.\n"
        f"Sedimentation in anoxic (oxygen-depleted) marine environments prevented decomposition. Over millions of years, heat and pressure transformed the organic matter into liquid hydrocarbons."
    )
    return {
        "id": f"ns7_en_10_{rng.randint(100000, 999999)}",
        "subskill": "10_fossil_fuel_formation_crude_oil_marine",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_10",
        "hints": {
            "tier_1": "Distinguish coal (land plants/swamps) from crude oil (marine organisms/plankton).",
            "tier_2": "Microscopic sea life died, settled in mud, and was transformed by pressure and heat.",
            "tier_3": "Select the option stating marine plankton and algae transformed over millions of years.",
        },
        "misconception_tags": ["oil_from_dead_dinosaurs_alone", "oil_is_melted_coal"],
    }


# 11. Fossil fuel formation natural gas
def arch_11_fossil_fuel_formation_natural_gas(rng: random.Random) -> Dict[str, Any]:
    geological_contexts = [
        ("deep shale rock strata in the Karoo", "methane molecules trapped inside microscopic rock pores"),
        ("sandstone reservoirs beneath the continental shelf", "gas pockets trapped beneath impermeable cap rock layers"),
    ]
    locale, trap = rng.choice(geological_contexts)
    prompt = (
        f"Geologists drilling in **{locale}** locate reserves of **natural gas**.\n\n"
        f"Which statement best explains why natural gas is found in these geological formations?"
    )
    correct = (
        f"Extreme heat and pressure deeper underground broke down ancient organic matter into lighter gaseous hydrocarbons (chiefly methane), "
        f"which migrated upward until sealed by impermeable rock ({trap})."
    )
    distractors = [
        "Air from the atmosphere was sucked underground through open caves during severe thunderstorms.",
        "Underground rivers dissolved granite rocks, releasing pure oxygen gas that turned into methane.",
        "Plant roots pumped carbon dioxide down to the Earth's molten core, where it solidified into gas pockets.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Origin of Geological Natural Gas:**\n"
        f"Natural gas forms alongside coal and crude oil when organic sediments experience even higher temperatures and pressures.\n"
        f"Being buoyant and light, the gas rises until trapped under non-porous (impermeable) rock layers, creating {trap}."
    )
    return {
        "id": f"ns7_en_11_{rng.randint(100000, 999999)}",
        "subskill": "11_fossil_fuel_formation_natural_gas",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_11",
        "hints": {
            "tier_1": "Think about what happens to organic matter under extreme heat deep in the crust.",
            "tier_2": "Gas is light and rises until stopped by an impermeable layer of rock.",
            "tier_3": "Choose the option explaining organic breakdown under high heat trapped by impermeable cap rock.",
        },
        "misconception_tags": ["gas_is_trapped_air", "gas_forms_without_organic_matter"],
    }


# 12. Geological time scale of fossil fuels
def arch_12_geological_time_scale_fossil_fuels(rng: random.Random) -> Dict[str, Any]:
    rates = [
        (300, 150, "Coal seams in Mpumalanga took approximately 300 million years to form, but South Africa could exhaust its accessible reserves in under 150 years."),
        (100, 50, "Offshore petroleum reservoirs took over 100 million years to accumulate, but global industrial extraction depletes them within decades."),
    ]
    form_millions, cons_years, statement = rng.choice(rates)
    prompt = (
        f"A scientific study notes: '{statement}'\n\n"
        f"What fundamental lesson does this comparison illustrate about fossil fuels?"
    )
    correct = "The rate of human consumption is hundreds of thousands of times faster than the geological rate of natural formation."
    distractors = [
        "Fossil fuels will naturally double in volume inside the mines every 50 years.",
        "Human extraction of coal accelerates the rate at which Earth forms new oil.",
        "Geological time and human historical time operate on identical calendars.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Rate Analysis:**\n"
        f"- Formation timescale: ~{form_millions} 000 000 years (millions of years).\n"
        f"- Consumption timescale: ~{cons_years} to 200 years (a few human lifetimes).\n\n"
        f"Conclusion: We are consuming stored solar energy from millions of years in just a few generations. Hence, fossil fuels are finite and non-renewable."
    )
    return {
        "id": f"ns7_en_12_{rng.randint(100000, 999999)}",
        "subskill": "12_geological_time_scale_fossil_fuels",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_12",
        "hints": {
            "tier_1": "Compare millions of years with 100 to 200 years.",
            "tier_2": "Which process happens much faster: making coal or burning coal?",
            "tier_3": "Human consumption is drastically faster than geological formation.",
        },
        "misconception_tags": ["geological_time_confused_with_human_time", "resource_permanence_illusion"],
    }


# 13. South Africa coal dependence reasons
def arch_13_south_africa_coal_dependence_reasons(rng: random.Random) -> Dict[str, Any]:
    proportions = [
        ("roughly 80% to 85%", "Kendal, Duvha, Matla, and Medupi power stations"),
        ("over 80%", "Kusile, Lethabo, and Tutuka power stations"),
    ]
    percentage, stations = rng.choice(proportions)
    prompt = (
        f"In South Africa, **{percentage}** of national electricity has historically been generated from coal "
        f"at major facilities such as **{stations}**.\n\n"
        f"What is the historical and geographic reason for this heavy dependence on coal?"
    )
    correct = "South Africa possesses vast, easily accessible shallow coal deposits that provided an abundant, cheap energy source."
    distractors = [
        "South Africa has zero sunshine and no wind anywhere in the country.",
        "International laws strictly forbid African countries from using solar power.",
        "Coal power stations require no water or maintenance to run continuously.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Historical & Geological Context:**\n"
        f"South Africa has extensive coal fields (Highveld, Waterberg) with thick, shallow seams close to the surface.\n"
        f"This made coal mining cheap and accessible, leading the country to build its industrial power infrastructure around coal."
    )
    return {
        "id": f"ns7_en_13_{rng.randint(100000, 999999)}",
        "subskill": "13_south_africa_coal_dependence_reasons",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_13",
        "hints": {
            "tier_1": "Consider what natural resource South Africa has in huge quantities underground in Mpumalanga.",
            "tier_2": "Cheap, abundant domestic coal reserves led to the development of coal-fired grid infrastructure.",
            "tier_3": "Select the option stating SA has vast, easily accessible shallow coal fields.",
        },
        "misconception_tags": ["sa_lacks_renewable_resources", "coal_was_imported_to_sa"],
    }


# 14. Eskom thermal power stations process
def arch_14_eskom_thermal_power_stations_process(rng: random.Random) -> Dict[str, Any]:
    stations = ["Kendal Power Station in Mpumalanga", "Medupi Power Station in Lephalale, Limpopo", "Kusile Power Station near eMalahleni"]
    station = rng.choice(stations)
    prompt = (
        f"At **{station}**, pulverized coal is fed into giant boilers.\n\n"
        f"Which sequence correctly traces the energy transformations inside a coal-fired power station?"
    )
    correct = (
        "Chemical potential energy in coal -> Thermal energy in steam -> "
        "Kinetic energy in spinning turbine -> Electrical energy in generator."
    )
    distractors = [
        "Electrical energy in coal -> Nuclear radiation in water -> Chemical energy in wires -> Light energy.",
        "Gravitational energy in coal -> Light energy in furnace -> Sound energy in turbine -> Heat in generator.",
        "Chemical potential energy in coal -> Electrical energy in boiler -> Kinetic energy in generator -> Steam.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Energy Transformation Chain in a Thermal Power Station:**\n"
        f"1. Coal burns: Chemical potential energy -> Thermal (heat) energy.\n"
        f"2. Water boils into high-pressure steam: Heat -> Thermal energy of steam.\n"
        f"3. Steam pushes turbine blades: Thermal -> Mechanical / Kinetic energy.\n"
        f"4. Turbine rotates magnets inside generator coils: Kinetic energy -> **Electrical energy**."
    )
    return {
        "id": f"ns7_en_14_{rng.randint(100000, 999999)}",
        "subskill": "14_eskom_thermal_power_stations_process",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_14",
        "hints": {
            "tier_1": "Start with the energy stored in coal bonds, and end with the electricity leaving the station.",
            "tier_2": "Coal burns (heat) -> boils steam -> spins turbine (motion) -> generator produces electricity.",
            "tier_3": "Chemical -> Thermal -> Kinetic -> Electrical.",
        },
        "misconception_tags": ["coal_directly_produces_electricity", "generator_burns_coal"],
    }


# 15. Crude oil fractionation products
def arch_15_crude_oil_fractionation_products(rng: random.Random) -> Dict[str, Any]:
    products = [
        ("Petrol (gasoline)", "fueling spark-ignition motor car engines"),
        ("Diesel", "powering heavy transport trucks, buses, and tractors"),
        ("Paraffin (kerosene)", "domestic heating, cooking stoves, and jet aircraft aviation fuel"),
        ("Bitumen (asphalt)", "surfacing and paving national tar roads"),
    ]
    prod, use = rng.choice(products)
    prompt = (
        f"Crude oil is a dark, sticky liquid mixture of hydrocarbons extracted from underground.\n"
        f"At an oil refinery (e.g., in Durban or Cape Town), it is separated into useful fuels.\n\n"
        f"Which refined petroleum product is specifically used for **{use}**?"
    )
    correct = prod
    distractors = [p[0] for p in products if p[0] != prod]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Petroleum Refining (Fractional Distillation):**\n"
        f"Crude oil is heated in a fractionating column. Fractions separate by boiling point:\n"
        f"- Refinery gases (LPG for cooking)\n"
        f"- Petrol (cars)\n"
        f"- Paraffin / Kerosene (jet fuel, domestic lamps/stoves)\n"
        f"- Diesel (heavy vehicles)\n"
        f"- Bitumen (road tarring)\n\n"
        f"The fraction for {use} is **{prod}**."
    )
    return {
        "id": f"ns7_en_15_{rng.randint(100000, 999999)}",
        "subskill": "15_crude_oil_fractionation_products",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "ns7_sources_15",
        "hints": {
            "tier_1": "Recall everyday fuels derived from crude petroleum oil.",
            "tier_2": f"Think about which fuel is associated with {use}.",
            "tier_3": f"The answer is {prod}.",
        },
        "misconception_tags": ["petrol_and_diesel_are_different_elements", "paraffin_is_not_oil"],
    }


# 16. Natural gas methane properties
def arch_16_natural_gas_methane_properties(rng: random.Random) -> Dict[str, Any]:
    uses = [
        ("domestic gas stoves and geysers", "burns with a clean blue flame, producing carbon dioxide and water vapor"),
        ("compressed natural gas (CNG) municipal buses", "releases significantly less particulate soot and sulfur than diesel"),
        ("gas turbine peaking power plants", "can be ignited rapidly to supply electricity during sudden peak demand spikes"),
    ]
    use_context, advantage = rng.choice(uses)
    prompt = (
        f"Natural gas is composed primarily of **methane** (\\(\\text{{CH}}_4\\)) and is used in **{use_context}**.\n\n"
        f"What is a major combustion property and environmental advantage of natural gas compared to raw coal?"
    )
    correct = f"It {advantage}, releasing higher energy per kilogram with far less ash and sulfur."
    distractors = [
        "It burns without consuming any oxygen from the surrounding air.",
        "It generates cold air instead of heat when it reacts chemically with fire.",
        "It is completely non-flammable and only produces power through magnetic waves.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Properties of Methane / Natural Gas:**\n"
        f"Methane is a simple hydrocarbon gas (\\(\\text{{CH}}_4\\)). When combusted:\n"
        f"$$\\text{{CH}}_4 + 2\\text{{O}}_2 \\rightarrow \\text{{CO}}_2 + 2\\text{{H}}_2\\text{{O}} + \\text{{Energy}}$$\n"
        f"Because it lacks sulfur and mineral impurities, it {advantage}."
    )
    return {
        "id": f"ns7_en_16_{rng.randint(100000, 999999)}",
        "subskill": "16_natural_gas_methane_properties",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_16",
        "hints": {
            "tier_1": "Recall that natural gas burns much cleaner than dirty coal.",
            "tier_2": "Methane produces water and carbon dioxide, with minimal soot and zero ash.",
            "tier_3": f"Identify the option describing how it {advantage}.",
        },
        "misconception_tags": ["natural_gas_is_100_percent_emission_free", "natural_gas_is_air"],
    }


# 17. Uranium atomic properties and symbol
def arch_17_uranium_atomic_properties_and_symbol(rng: random.Random) -> Dict[str, Any]:
    elements = [
        ("Uranium", "U", 92, "nuclear fuel in fission reactors"),
        ("Uranium-235", "U", 92, "the fissionable isotope used in nuclear power fuel rods"),
    ]
    name, symbol, atomic_num, role = rng.choice(elements)
    prompt = (
        f"Nuclear power stations utilize **{name}** as their primary fuel.\n\n"
        f"Identify the chemical symbol, atomic number, and nature of {name} on the Periodic Table."
    )
    correct = f"Symbol: **{symbol}**, Atomic Number: **{atomic_num}**; it is a heavy radioactive metal element."
    distractors = [
        f"Symbol: **Ur**, Atomic Number: **46**; it is a light non-metal noble gas.",
        f"Symbol: **Un**, Atomic Number: **102**; it is an organic plant carbohydrate.",
        f"Symbol: **Ra**, Atomic Number: **88**; it is an alkali metal found in table salt.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Periodic Table Facts for Uranium:**\n"
        f"- Name: {name}\n"
        f"- Symbol: **{symbol}**\n"
        f"- Atomic number: **{atomic_num}** (meaning each uranium atom has 92 protons in its nucleus)\n"
        f"- Classification: Actinoid / heavy metal with unstable radioactive nuclei."
    )
    return {
        "id": f"ns7_en_17_{rng.randint(100000, 999999)}",
        "subskill": "17_uranium_atomic_properties_and_symbol",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_17",
        "hints": {
            "tier_1": "Look at the Periodic Table for element number 92.",
            "tier_2": "The chemical symbol for Uranium is a single capital letter U.",
            "tier_3": "Symbol is U, atomic number is 92.",
        },
        "misconception_tags": ["uranium_symbol_is_ur", "uranium_is_a_compound"],
    }


# 18. Nuclear fission energy release
def arch_18_nuclear_fission_energy_release(rng: random.Random) -> Dict[str, Any]:
    isotopes = ["uranium-235 nucleus", "heavy atomic nucleus of uranium"]
    target = rng.choice(isotopes)
    prompt = (
        f"In a nuclear power reactor, energy is liberated through a process called **nuclear fission**.\n\n"
        f"What happens to the {target} during nuclear fission?"
    )
    correct = "The nucleus absorbs a neutron and splits into smaller nuclei, releasing a tremendous amount of thermal energy."
    distractors = [
        "Two small hydrogen nuclei collide at extreme speed and fuse into one larger nucleus.",
        "The outer electrons freeze into solid crystals, releasing cold gravitational energy.",
        "The atom dissolves completely in water without releasing any heat or radiation.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Definition of Nuclear Fission:**\n"
        f"- Fission means 'splitting apart'.\n"
        f"- When a {target} splits into smaller fragment nuclei, the strong nuclear binding forces release vast amounts of **thermal energy**.\n"
        f"- (Nuclear fusion is the opposite: smaller nuclei combining, as occurs inside the Sun)."
    )
    return {
        "id": f"ns7_en_18_{rng.randint(100000, 999999)}",
        "subskill": "18_nuclear_fission_energy_release",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_18",
        "hints": {
            "tier_1": "Recall what the word 'fission' means: splitting or combining?",
            "tier_2": "Fission is the splitting of a heavy nucleus; fusion is joining small nuclei.",
            "tier_3": "The nucleus splits apart, releasing immense thermal energy.",
        },
        "misconception_tags": ["fission_confused_with_fusion", "nuclear_reaction_is_chemical_combustion"],
    }


# 19. Koeberg nuclear power station context
def arch_19_koeberg_nuclear_power_station_context(rng: random.Random) -> Dict[str, Any]:
    aspects = [
        ("approximately 28 km north of Cape Town on the Atlantic coast", "cold seawater from the Atlantic Ocean to cool its steam condensers"),
        ("Duynefontein near Cape Town", "two pressurized water reactors (PWR) supplying electricity to the Western Cape"),
    ]
    location, feature = rng.choice(aspects)
    prompt = (
        f"**Koeberg Power Station** is the only commercial nuclear power station on the African continent.\n"
        f"It is situated {location}.\n\n"
        f"Why was Koeberg constructed right on the coastline, and what key resource does it utilize for operation?"
    )
    correct = f"It was built on the coast to use {feature}."
    distractors = [
        "It was built on the coast to harvest sea salt to burn directly in its nuclear reactors.",
        "It was built on the coast so that nuclear fuel could be dumped into fishing harbors every week.",
        "It was built on the coast because nuclear reactors can only operate underwater in high tides.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Koeberg Power Station Facts:**\n"
        f"1. **Location:** Duynefontein, ~28 km north of Cape Town, on the Atlantic coast.\n"
        f"2. **Cooling:** Nuclear thermal stations produce huge amounts of steam. Koeberg pumps in billions of liters of {feature} before returning it cleanly to the ocean.\n"
        f"3. **Contribution:** Provides ~5% of South Africa's national electricity grid power."
    )
    return {
        "id": f"ns7_en_19_{rng.randint(100000, 999999)}",
        "subskill": "19_koeberg_nuclear_power_station_context",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_19",
        "hints": {
            "tier_1": "Think about why a power station needs enormous volumes of cold water.",
            "tier_2": "Thermal power stations need cold water to condense hot steam back into liquid.",
            "tier_3": "It utilizes cold seawater for steam condenser cooling.",
        },
        "misconception_tags": ["koeberg_uses_sea_salt_fuel", "nuclear_stations_do_not_need_cooling"],
    }


# 20. Nuclear power advantages emissions
def arch_20_nuclear_power_advantages_emissions(rng: random.Random) -> Dict[str, Any]:
    comparisons = [
        ("a 1 000 MW coal-fired power station", "millions of tonnes of carbon dioxide and particulate fly ash annually"),
        ("standard fossil thermal generation", "greenhouse gases that cause the enhanced greenhouse effect"),
    ]
    fossil_ref, pollution = rng.choice(comparisons)
    prompt = (
        f"When debating energy policy, proponents highlight the environmental benefits of nuclear power compared to {fossil_ref}.\n\n"
        f"What is the single greatest environmental advantage of generating electricity in a nuclear reactor during normal operation?"
    )
    correct = "It does not burn fossil fuel and releases zero carbon dioxide or greenhouse gases during operation."
    distractors = [
        "It creates free pure drinking water that completely eliminates droughts in the region.",
        "It consumes nuclear waste from other industries and turns it into gold.",
        "It guarantees that uranium fuel rods will last for millions of years without replacement.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Environmental Advantage of Nuclear Power:**\n"
        f"In a nuclear reactor, heat comes from nuclear fission, not chemical combustion of carbon.\n"
        f"Unlike coal stations which emit {pollution}, nuclear reactors produce **no \\(\\text{{CO}}_2\\), sulfur dioxide, or smoke** from their cooling towers (only harmless water vapor)."
    )
    return {
        "id": f"ns7_en_20_{rng.randint(100000, 999999)}",
        "subskill": "20_nuclear_power_advantages_emissions",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_20",
        "hints": {
            "tier_1": "Does nuclear fission involve burning carbon or releasing smoke?",
            "tier_2": "Nuclear reactions do not burn fossil carbon, so no carbon dioxide is released.",
            "tier_3": "It emits zero carbon dioxide or greenhouse gases during normal electricity generation.",
        },
        "misconception_tags": ["cooling_tower_steam_is_smoke", "nuclear_plants_emit_carbon_dioxide"],
    }


# 21. Nuclear power disadvantages radioactive waste
def arch_21_nuclear_power_disadvantages_radioactive_waste(rng: random.Random) -> Dict[str, Any]:
    concerns = [
        ("Vaalputs radioactive waste disposal facility in the Northern Cape", "spent nuclear fuel rods remain dangerously radioactive for thousands of years"),
        ("nuclear power plant decommissioning", "handling and storing hazardous high-level radioactive waste safely over millennia"),
    ]
    facility, challenge = rng.choice(concerns)
    prompt = (
        f"Environmental groups raise serious concerns regarding nuclear energy expansion, citing challenges at **{facility}**.\n\n"
        f"What is a primary disadvantage and long-term hazard of using nuclear fuel?"
    )
    correct = f"It produces spent radioactive waste that remains hazardous to living organisms and the environment for thousands of years."
    distractors = [
        "It emits thick black soot that settles over nearby farming valleys every morning.",
        "It produces acid rain that immediately dissolves metal car bodies in surrounding towns.",
        "It consumes all the oxygen in the provincial atmosphere, suffocating nearby wildlife.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Disadvantages of Nuclear Power:**\n"
        f"1. **Radioactive Waste:** Used fuel rods contain highly radioactive fission byproducts that emit damaging ionizing radiation for thousands of years ({challenge}).\n"
        f"2. **Accident Risks:** Catastrophic reactor meltdowns (e.g. Chernobyl, Fukushima) can contaminate vast areas.\n"
        f"3. **High Capital Cost:** Extremely expensive to construct and decommission safely."
    )
    return {
        "id": f"ns7_en_21_{rng.randint(100000, 999999)}",
        "subskill": "21_nuclear_power_disadvantages_radioactive_waste",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_21",
        "hints": {
            "tier_1": "What happens to nuclear fuel after it has been used in a reactor?",
            "tier_2": "Spent fuel cannot just be thrown in a standard landfill because of radiation.",
            "tier_3": "It produces radioactive waste that remains dangerous for thousands of years.",
        },
        "misconception_tags": ["nuclear_waste_degrades_in_days", "nuclear_plants_explode_like_bombs"],
    }


# 22. Natural greenhouse effect mechanism
def arch_22_natural_greenhouse_effect_mechanism(rng: random.Random) -> Dict[str, Any]:
    planets = [
        ("Earth", "an average global temperature of ~15 °C rather than a frozen -18 °C", "support liquid oceans and flourishing life"),
        ("our planet", "retaining thermal energy in the troposphere", "preventing extreme freezing temperatures at night"),
    ]
    p_name, temp_stat, purpose = rng.choice(planets)
    prompt = (
        f"Without the **natural greenhouse effect**, {p_name} would have {temp_stat}.\n\n"
        f"How does the natural greenhouse effect maintain temperatures suitable for life on Earth?"
    )
    correct = (
        "Short-wave solar radiation warms Earth's surface, which then emits longer-wave infrared (heat) radiation; "
        "atmospheric greenhouse gases absorb and re-radiate this heat, keeping the planet warm."
    )
    distractors = [
        "The atmosphere creates a solid sheet of ice in space that reflects all incoming sunlight away from Earth.",
        "Greenhouse gases burn continuously with open fires in the upper atmosphere, generating fresh heat.",
        "The Sun sends hot microwave beams that are trapped inside the Earth's molten liquid core.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**The Natural Greenhouse Effect Mechanism:**\n"
        f"1. **Solar Influx:** Solar radiation passes through the atmosphere and is absorbed by Earth's land and oceans.\n"
        f"2. **Infrared Emission:** The warmed Earth re-emits thermal energy as infrared radiation.\n"
        f"3. **Absorption:** Atmospheric gases (\\(\\text{{H}}_2\\text{{O}}, \\text{{CO}}_2, \\text{{CH}}_4\\)) absorb and re-emit this heat in all directions, to {purpose}."
    )
    return {
        "id": f"ns7_en_22_{rng.randint(100000, 999999)}",
        "subskill": "22_natural_greenhouse_effect_mechanism",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_22",
        "hints": {
            "tier_1": "Solar light warms Earth, then Earth radiates heat outward.",
            "tier_2": "Greenhouse gases absorb infrared heat and reflect it back toward the surface.",
            "tier_3": "Short-wave solar radiation warms the surface; outgoing infrared heat is absorbed and re-radiated.",
        },
        "misconception_tags": ["greenhouse_effect_is_purely_evil", "greenhouse_gases_trap_light_not_heat"],
    }


# 23. Greenhouse gases identification
def arch_23_greenhouse_gases_identification(rng: random.Random) -> Dict[str, Any]:
    gas_sets = [
        ("Carbon dioxide (\\(\\text{{CO}}_2\\)), Methane (\\(\\text{{CH}}_4\\)), and Water vapor (\\(\\text{{H}}_2\\text{{O}}\\))", True),
        ("Nitrogen (\\(\\text{{N}}_2\\)), Oxygen (\\(\\text{{O}}_2\\)), and Argon (\\(\\text{{Ar}}\\))", False),
    ]
    prompt = (
        "Greenhouse gases are atmospheric gases that possess the physical property of absorbing and re-emitting infrared radiation.\n\n"
        "Which of the following groups consists strictly of **greenhouse gases**?"
    )
    correct = "Carbon dioxide, Methane, Water vapor, and Nitrous oxide."
    distractors = [
        "Nitrogen gas, Oxygen gas, and Argon.",
        "Pure Helium, Neon gas, and Hydrogen gas.",
        "Carbon monoxide, pure Gold dust, and Nitrogen gas.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Greenhouse Gases vs Primary Atmospheric Gases:**\n"
        f"- Nitrogen (\\(\\sim 78\\%\\)) and Oxygen (\\(\\sim 21\\%\\)) make up 99% of the atmosphere but are **not** greenhouse gases because their diatomic molecules do not readily absorb infrared radiation.\n"
        f"- **Greenhouse gases include:** Water vapor (\\(\\text{{H}}_2\\text{{O}}\\)), Carbon dioxide (\\(\\text{{CO}}_2\\)), Methane (\\(\\text{{CH}}_4\\)), and Nitrous oxide (\\(\\text{{N}}_2\\text{{O}}\\))."
    )
    return {
        "id": f"ns7_en_23_{rng.randint(100000, 999999)}",
        "subskill": "23_greenhouse_gases_identification",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_23",
        "hints": {
            "tier_1": "Recall the main gas released when coal and petrol are burned.",
            "tier_2": "The two main ones mentioned in the curriculum are carbon dioxide and methane.",
            "tier_3": "Carbon dioxide, Methane, Water vapor, and Nitrous oxide.",
        },
        "misconception_tags": ["oxygen_and_nitrogen_are_greenhouse_gases", "water_vapor_is_not_greenhouse_gas"],
    }


# 24. Enhanced greenhouse effect fossil combustion
def arch_24_enhanced_greenhouse_effect_fossil_combustion(rng: random.Random) -> Dict[str, Any]:
    sources = [
        ("burning millions of tonnes of coal in power stations and petrol in motor vehicles", "carbon dioxide (\\(\\text{{CO}}_2\\))"),
        ("flaring gas at oil refineries and combusting fossil fuels across heavy industry", "excess greenhouse gases"),
    ]
    activity, gas = rng.choice(sources)
    prompt = (
        f"Human industrial activity, especially **{activity}**, releases vast quantities of **{gas}** into the atmosphere.\n\n"
        f"How does this create the **enhanced greenhouse effect** (global warming)?"
    )
    correct = (
        "Excess greenhouse gases trap more outgoing infrared heat in the atmosphere than normal, "
        "reducing heat escape into space and causing average global temperatures to rise."
    )
    distractors = [
        "The extra gases block all sunlight from reaching Earth, plunging the planet into permanent darkness.",
        "The burning fuels deplete Earth's gravity, allowing the atmosphere to float away into outer space.",
        "The carbon dioxide chemically dissolves atmospheric ozone, letting gamma rays boil the surface rocks.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Mechanism of Enhanced Greenhouse Effect:**\n"
        f"1. **Baseline:** The natural greenhouse effect maintains a livable climate.\n"
        f"2. **Excess Emissions:** By {activity}, humans release billions of tonnes of {gas}.\n"
        f"3. **Thermal Imbalance:** With higher gas concentrations, less heat escapes into space and more heat is radiated back to Earth, driving global warming."
    )
    return {
        "id": f"ns7_en_24_{rng.randint(100000, 999999)}",
        "subskill": "24_enhanced_greenhouse_effect_fossil_combustion",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_24",
        "hints": {
            "tier_1": "What happens when you add more blanket layers on a bed?",
            "tier_2": "More greenhouse gases act like a thicker blanket, trapping more heat.",
            "tier_3": "More heat is trapped, reducing escape into space and raising global temperatures.",
        },
        "misconception_tags": ["ozone_hole_confused_with_greenhouse_effect", "global_warming_caused_by_sun_heating_up"],
    }


# 25. Global warming consequences South Africa
def arch_25_global_warming_consequences_south_africa(rng: random.Random) -> Dict[str, Any]:
    impacts = [
        ("the agricultural sector in the Western Cape and Karoo", "prolonged severe droughts, water scarcity, and heat stress on food crops"),
        ("coastal cities such as Durban and Cape Town", "sea-level rise, coastal erosion, and intensified storm surges damaging infrastructure"),
        ("biodiversity in the Succulent Karoo and Fynbos biomes", "habitat loss, shifts in rainfall patterns, and heightened extinction risk for endemic plant species"),
    ]
    sector, consequence = rng.choice(impacts)
    prompt = (
        f"Climatologists warn that rising atmospheric temperatures from burning fossil fuels impact South Africa severely.\n\n"
        f"What is a direct consequence of global warming on **{sector}**?"
    )
    correct = f"It leads to {consequence}."
    distractors = [
        "It causes permanent sub-zero polar blizzards across all northern provinces year-round.",
        "It accelerates the natural replenishment of underground coal seams within five years.",
        "It cools down ocean waters so drastically that tropical coral reefs grow in Antarctica.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Impacts of Global Warming on South Africa:**\n"
        f"Southern Africa is warming at roughly twice the global average rate.\n"
        f"Key consequences for {sector} include: **{consequence}**.\n"
        f"This underscores the urgent need to transition to sustainable, low-carbon energy sources."
    )
    return {
        "id": f"ns7_en_25_{rng.randint(100000, 999999)}",
        "subskill": "25_global_warming_consequences_south_africa",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_25",
        "hints": {
            "tier_1": "Consider real weather challenges South Africa faces: rainfall, heat, and droughts.",
            "tier_2": "Warmer climates increase evaporation, leading to harsher droughts and coastal sea rise.",
            "tier_3": f"Identify the option describing {consequence}.",
        },
        "misconception_tags": ["global_warming_has_no_local_impact", "global_warming_causes_permanent_ice_age"],
    }
