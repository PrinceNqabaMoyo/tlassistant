"""Grade 7 Natural Sciences: Term 3 - Sources of Energy (Archetypes 26 to 50).
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


# 26. Solar energy photovoltaic conversion
def arch_26_solar_energy_photovoltaic_conversion(rng: random.Random) -> Dict[str, Any]:
    capacities = [("a school rooftop solar installation", "15 kW"), ("a rural clinic off-grid power setup", "8 kW")]
    app, size = rng.choice(capacities)
    prompt = (
        f"A community installs **solar photovoltaic (PV) panels** for **{app}** ({size}).\n\n"
        f"Which direct energy transformation takes place inside a photovoltaic cell when sunlight shines on it?"
    )
    correct = "Radiant light energy from the Sun is converted directly into electrical energy."
    distractors = [
        "Thermal heat energy boils water inside the panel to turn a miniature mechanical turbine.",
        "Sound energy from wind vibration is converted into chemical battery acid.",
        "Nuclear fission inside silicon crystals converts uranium atoms into magnetic current.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Photovoltaic Energy Conversion:**\n"
        f"Photovoltaic (PV) cells contain semiconductor materials (such as silicon).\n"
        f"When sunlight (radiant energy) strikes the semiconductor, it excites electrons, generating an electric current directly.\n"
        f"Therefore: **Radiant energy -> Electrical energy** (no steam or turbines involved)."
    )
    return {
        "id": f"ns7_en_26_{rng.randint(100000, 999999)}",
        "subskill": "26_solar_energy_photovoltaic_conversion",
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
        "learning_objective_id": "ns7_sources_26",
        "hints": {
            "tier_1": "Recall what 'photo' and 'voltaic' mean.",
            "tier_2": "'Photo' relates to light; 'voltaic' relates to electricity (voltage).",
            "tier_3": "Radiant light energy is converted directly into electrical energy.",
        },
        "misconception_tags": ["solar_panels_boil_water_internally", "pv_panels_need_heat_not_light"],
    }


# 27. Solar thermal water heaters
def arch_27_solar_thermal_water_heaters(rng: random.Random) -> Dict[str, Any]:
    colors = [
        ("matte black absorber tubes and dark collector plates", "black surfaces absorb maximum solar radiation without reflecting it"),
        ("dark-coated copper pipes mounted inside an insulated glass-topped box", "dark materials absorb heat efficiently while glass creates a greenhouse trap"),
    ]
    feature, scientific_reason = rng.choice(colors)
    prompt = (
        f"A domestic **solar water heater (solar geyser)** uses **{feature}** on the house roof.\n\n"
        f"What energy conversion occurs, and why is this design feature essential for heating water?"
    )
    correct = f"Radiant energy from the Sun is absorbed and converted into thermal (heat) energy in the water; {scientific_reason}."
    distractors = [
        "Electrical energy is extracted from moonlight to chill water into ice.",
        "Chemical potential energy is created by dissolving metal pipes into the household water supply.",
        "Nuclear energy is triggered inside the water molecules to generate radioactive steam.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Solar Thermal Principles:**\n"
        f"1. **Conversion:** Radiant energy (sunlight) -> Thermal energy (heat in water).\n"
        f"2. **Design:** Solar thermal systems differ from PV panels: they heat water directly instead of generating electrical current.\n"
        f"3. **Absorption:** {scientific_reason.capitalize()}."
    )
    return {
        "id": f"ns7_en_27_{rng.randint(100000, 999999)}",
        "subskill": "27_solar_thermal_water_heaters",
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
        "learning_objective_id": "ns7_sources_27",
        "hints": {
            "tier_1": "Distinguish between a solar PV panel (makes electricity) and a solar geyser (heats water).",
            "tier_2": "Dark colors absorb radiant heat energy best.",
            "tier_3": f"Radiant energy becomes thermal energy; {scientific_reason}.",
        },
        "misconception_tags": ["solar_geysers_make_electricity", "white_surfaces_absorb_heat_better"],
    }


# 28. Solar potential Northern Cape
def arch_28_solar_potential_northern_cape(rng: random.Random) -> Dict[str, Any]:
    towns = [
        ("Upington in the Northern Cape", "over 300 days of cloudless sunshine per year and extremely high solar irradiance"),
        ("Kathu and De Aar in the semi-arid Karoo/Northern Cape", "high altitude, minimal cloud cover, and intense solar radiation levels"),
    ]
    town, reason = rng.choice(towns)
    prompt = (
        f"South Africa has constructed massive solar power parks near **{town}**.\n\n"
        f"Why is the Northern Cape province geographically ideal for large-scale utility solar energy generation?"
    )
    correct = f"It receives {reason}, maximizing energy capture per square meter."
    distractors = [
        "It has dense tropical rain clouds that shield panels from strong wind damage.",
        "It is surrounded by deep oceans that reflect sunlight directly onto the land.",
        "It has extensive underground coal mines that heat up solar panels from below.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Geographical Suitability:**\n"
        f"The Northern Cape is a semi-arid, high-sunshine region with some of the highest solar irradiance levels in the world.\n"
        f"Because it receives {reason}, solar PV and concentrated solar power (CSP) stations operate at peak efficiency."
    )
    return {
        "id": f"ns7_en_28_{rng.randint(100000, 999999)}",
        "subskill": "28_solar_potential_northern_cape",
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
        "learning_objective_id": "ns7_sources_28",
        "hints": {
            "tier_1": "What is the weather like in the Northern Cape and Karoo?",
            "tier_2": "Lots of sunshine, few clouds, and high solar radiation.",
            "tier_3": "Choose the option mentioning high solar irradiance and cloudless sunshine.",
        },
        "misconception_tags": ["all_regions_have_identical_solar_potential", "solar_parks_need_rain"],
    }


# 29. Wind energy turbine mechanism
def arch_29_wind_energy_turbine_mechanism(rng: random.Random) -> Dict[str, Any]:
    components = [
        ("aerodynamic rotor blades connected to a gearbox and generator", "kinetic energy of air -> kinetic energy of spinning shaft -> electrical energy"),
        ("a horizontal-axis turbine nacelle housing an electrical generator", "wind kinetic energy -> mechanical rotation -> electrical energy"),
    ]
    turbine_setup, energy_chain = rng.choice(components)
    prompt = (
        f"A modern wind turbine features **{turbine_setup}** mounted atop an 80-meter tower.\n\n"
        f"What is the correct sequence of energy transformations that occurs when wind blows across the turbine?"
    )
    correct = f"{energy_chain.capitalize()}."
    distractors = [
        "Thermal heat in wind -> Nuclear fission in rotor -> Chemical energy in tower -> Sound energy.",
        "Electrical energy in air -> Gravitational potential energy in blades -> Heat in generator.",
        "Light energy from sun -> Chemical energy in rotor -> Kinetic energy in generator.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Wind Turbine Energy Flow:**\n"
        f"1. Wind is moving air: **Kinetic energy**.\n"
        f"2. Wind pushes angled rotor blades, making them spin: **Mechanical / Rotational kinetic energy**.\n"
        f"3. Shaft turns magnets inside copper wire coils in the generator: **Electrical energy**.\n"
        f"Result: {energy_chain}."
    )
    return {
        "id": f"ns7_en_29_{rng.randint(100000, 999999)}",
        "subskill": "29_wind_energy_turbine_mechanism",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": f"{energy_chain.capitalize()}.",
        "sample_answer": f"{energy_chain.capitalize()}.",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_29",
        "hints": {
            "tier_1": "Wind is air in motion, which means kinetic energy.",
            "tier_2": "Motion turns the generator, which outputs electricity.",
            "tier_3": "Kinetic energy -> Mechanical rotation -> Electrical energy.",
        },
        "misconception_tags": ["wind_turbines_create_wind", "turbines_burn_wind"],
    }


# 30. Wind energy geographic location coastal
def arch_30_wind_energy_geographic_location_coastal(rng: random.Random) -> Dict[str, Any]:
    sites = [
        ("Cookhouse, Kouga, and Jeffreys Bay in the Eastern Cape", "strong, consistent onshore oceanic breeze regimes created by sea-land thermal gradients"),
        ("Darling and Vredenburg along the Western Cape coastline", "reliable coastal wind corridors driven by South Atlantic high-pressure systems"),
    ]
    location, climatic_reason = rng.choice(sites)
    prompt = (
        f"South Africa has established major commercial wind energy farms at **{location}**.\n\n"
        f"Why are these coastal and near-coastal regions chosen rather than sheltered inland valleys?"
    )
    correct = f"They experience {climatic_reason}, providing the sustained wind speeds required to turn turbines economically."
    distractors = [
        "Coastal soil contains high amounts of electricity that travel directly up the tower foundations.",
        "Wind turbines cannot operate in areas that have trees or vegetation of any kind.",
        "Inland valleys are legally reserved exclusively for burning crude petroleum oil.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Siting Requirements for Wind Farms:**\n"
        f"Wind turbines require minimum cut-in speeds (~12-15 km/h) and optimal sustained speeds to produce power.\n"
        f"Coastal areas like {location} experience {climatic_reason}, ensuring steady, predictable output."
    )
    return {
        "id": f"ns7_en_30_{rng.randint(100000, 999999)}",
        "subskill": "30_wind_energy_geographic_location_coastal",
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
        "learning_objective_id": "ns7_sources_30",
        "hints": {
            "tier_1": "Where in South Africa is it famously windy?",
            "tier_2": "Coastal provinces like Eastern and Western Cape have strong, steady ocean winds.",
            "tier_3": "Choose the option explaining strong, consistent coastal wind regimes.",
        },
        "misconception_tags": ["wind_turbines_work_anywhere_equally", "wind_is_stronger_in_caves"],
    }


# 31. Wind energy advantages and disadvantages
def arch_31_wind_energy_advantages_and_disadvantages(rng: random.Random) -> Dict[str, Any]:
    tradeoffs = [
        ("Clean, free, renewable fuel with zero greenhouse gas emissions during generation", "Intermittent supply (does not blow continuously) and visual/noise impact on local residents"),
        ("Zero water required for electricity generation (conserving scarce freshwater)", "Potential hazard to migratory birds/bats and aesthetic alterations to rural landscapes"),
    ]
    pro, con = rng.choice(tradeoffs)
    prompt = (
        f"Environmental scientists evaluate the trade-offs of expanding wind power in South Africa.\n\n"
        f"Which pair correctly identifies one major **advantage** and one major **disadvantage** of wind energy?"
    )
    correct = f"Advantage: {pro} | Disadvantage: {con}."
    distractors = [
        f"Advantage: Emits coal smoke to fertilize plants | Disadvantage: Requires millions of liters of diesel daily.",
        f"Advantage: Works 100% identically underwater | Disadvantage: Freezes the entire country into ice.",
        f"Advantage: {pro} | Disadvantage: Generates hazardous radioactive nuclear waste.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Wind Energy Trade-off Analysis:**\n"
        f"- **Advantages:** Renewable, zero fuel costs, zero greenhouse gas emissions, uses no water for cooling.\n"
        f"- **Disadvantages:** Intermittency (wind does not blow on demand), low energy density requiring large land areas, noise, visual changes, bird collision risk.\n\n"
        f"Correct pairing: **Advantage: {pro} | Disadvantage: {con}**."
    )
    return {
        "id": f"ns7_en_31_{rng.randint(100000, 999999)}",
        "subskill": "31_wind_energy_advantages_and_disadvantages",
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
        "learning_objective_id": "ns7_sources_31",
        "hints": {
            "tier_1": "Recall: wind is clean and renewable, but what happens when the wind stops blowing?",
            "tier_2": "Wind produces no greenhouse emissions, but its supply is intermittent.",
            "tier_3": f"Advantage: {pro} | Disadvantage: {con}.",
        },
        "misconception_tags": ["wind_turbines_emit_radiation", "wind_power_has_zero_drawbacks"],
    }


# 32. Hydropower gravitational potential conversion
def arch_32_hydropower_gravitational_potential_conversion(rng: random.Random) -> Dict[str, Any]:
    heights = [(50, "a dam wall 50 meters high"), (90, "a mountain reservoir drop of 90 meters")]
    h, desc = rng.choice(heights)
    prompt = (
        f"In a hydroelectric generating station, water flows from {desc} through penstock pipes to turn turbines.\n\n"
        f"What is the primary energy transformation that occurs as the water descends and passes through the turbine generator?"
    )
    correct = "Gravitational potential energy of stored water -> Kinetic energy of moving water -> Electrical energy in generator."
    distractors = [
        "Chemical potential energy in water molecules -> Thermal combustion -> Light energy in wires.",
        "Nuclear energy of oxygen atoms -> Sound energy -> Gravitational potential energy.",
        "Electrical energy in the reservoir -> Kinetic energy in the river -> Heat in the dam wall.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Hydroelectric Energy Chain:**\n"
        f"1. Water stored at elevation: **Gravitational potential energy** (\\(E_p = mgh\\)).\n"
        f"2. Water falls down the penstock pipe: Converted to **Kinetic energy** (motion).\n"
        f"3. Moving water strikes turbine runner blades, spinning the generator rotor: **Electrical energy**."
    )
    return {
        "id": f"ns7_en_32_{rng.randint(100000, 999999)}",
        "subskill": "32_hydropower_gravitational_potential_conversion",
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
        "learning_objective_id": "ns7_sources_32",
        "hints": {
            "tier_1": "Water at high elevation stores what kind of potential energy?",
            "tier_2": "Water at a height has gravitational potential energy, which becomes kinetic as it falls.",
            "tier_3": "Gravitational potential -> Kinetic -> Electrical.",
        },
        "misconception_tags": ["water_has_chemical_combustion_energy", "hydro_needs_boiling_water"],
    }


# 33. Gariep Dam hydroelectric scheme
def arch_33_gariep_dam_hydroelectric_scheme(rng: random.Random) -> Dict[str, Any]:
    capacities = [
        ("Gariep Dam on the Orange River (Gariep River)", "360 MW across four generator units", "South Africa's largest hydroelectric power station"),
        ("Vanderkloof Dam downstream on the Orange River", "240 MW across two generator units", "a major peaking hydroelectric facility"),
    ]
    station, spec, role = rng.choice(capacities)
    prompt = (
        f"**{station}** has an installed capacity of **{spec}** and serves as **{role}**.\n\n"
        f"Why is hydroelectricity from this dam particularly valuable to the national electricity grid during peak demand hours?"
    )
    correct = "Hydroelectric turbines can be started and synchronized to full power in minutes, providing rapid response to sudden electricity shortages."
    distractors = [
        "It boils all river water into steam, permanently warming the surrounding province.",
        "It burns coal inside the water to triple the water pressure.",
        "It only generates power when national electricity has already been completely switched off.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Role of Hydroelectric Schemes (Gariep / Vanderkloof):**\n"
        f"- Thermal coal power stations take hours or days to start up from cold.\n"
        f"- Hydro stations simply open water control gates: water rushes in and spins turbines to full output in **2 to 3 minutes**.\n"
        f"- This makes hydro ideal for 'peaking power' (breakfast and evening dinner peak demand spikes)."
    )
    return {
        "id": f"ns7_en_33_{rng.randint(100000, 999999)}",
        "subskill": "33_gariep_dam_hydroelectric_scheme",
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
        "learning_objective_id": "ns7_sources_33",
        "hints": {
            "tier_1": "How fast can you open a water valve compared to heating up a massive coal boiler?",
            "tier_2": "Water flows immediately, allowing rapid start-up during peak demand.",
            "tier_3": "Hydroelectric turbines can be started and synchronized to full power in minutes.",
        },
        "misconception_tags": ["hydro_takes_days_to_start", "gariep_burns_coal"],
    }


# 34. Pumped storage schemes Drakensberg
def arch_34_pumped_storage_schemes_drakensberg(rng: random.Random) -> Dict[str, Any]:
    schemes = [
        ("Drakensberg Pumped Storage Scheme", "Driekloof (upper reservoir) and Sterkfontein / Kilburn (lower reservoir)"),
        ("Ingula Pumped Storage Scheme near Ladysmith/Van Reenen", "Bedford (upper reservoir) and Bramhoek (lower reservoir)"),
    ]
    scheme_name, reservoirs = rng.choice(schemes)
    prompt = (
        f"South Africa operates the **{scheme_name}** featuring **{reservoirs}**.\n\n"
        f"How does a **pumped-storage hydroelectric scheme** act like a giant rechargeable grid battery?"
    )
    correct = (
        "During low-demand nighttime hours, surplus electricity pumps water to the upper reservoir; "
        "during daytime peak demand, water rushes back down through turbines to generate power."
    )
    distractors = [
        "It stores millions of car batteries underwater to prevent them from catching fire.",
        "It extracts hydrogen from water using coal fires and burns the water repeatedly.",
        "Water is boiled into gas and pumped into outer space to cool the Earth's climate.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Working of Pumped-Storage Schemes:**\n"
        f"1. **Pumping Mode (Off-peak / Night):** Cheap, excess base electricity pumps water uphill from lower to upper reservoir (storing gravitational potential energy).\n"
        f"2. **Generation Mode (Peak hours):** Water is released downhill, driving pump-turbines as generators to feed high-value electricity back into the grid."
    )
    return {
        "id": f"ns7_en_34_{rng.randint(100000, 999999)}",
        "subskill": "34_pumped_storage_schemes_drakensberg",
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
        "learning_objective_id": "ns7_sources_34",
        "hints": {
            "tier_1": "Think about storing water at the top when electricity is cheap, and dropping it when power is needed.",
            "tier_2": "Pumps water uphill at night; releases water downhill through turbines at peak times.",
            "tier_3": "Surplus nighttime power pumps water up; peak demand releases water down to generate power.",
        },
        "misconception_tags": ["pumped_storage_generates_free_excess_energy", "pumping_requires_no_power"],
    }


# 35. Hydropower advantages and limitations
def arch_35_hydropower_advantages_and_limitations(rng: random.Random) -> Dict[str, Any]:
    aspects = [
        ("Zero fuel costs and no direct greenhouse gas emissions during generation", "South Africa is a water-scarce country with limited perennial rivers, making hydro vulnerable to severe droughts"),
        ("Clean, renewable power with long plant lifespans (>50 years)", "Flooding of river valleys for dam reservoirs disrupts river ecosystems, fish migration, and human settlements"),
    ]
    benefit, limitation = rng.choice(aspects)
    prompt = (
        f"In assessing energy resources for South Africa, why cannot conventional hydropower replace all coal power stations across the country?\n\n"
        f"Select the statement that correctly states a key **advantage** and a fundamental **limitation** for South Africa."
    )
    correct = f"Advantage: {benefit} | Limitation: {limitation}."
    distractors = [
        f"Advantage: Unlimited water everywhere in Karoo | Limitation: Hydroelectricity produces radioactive clouds.",
        f"Advantage: Requires zero rain or rivers to work | Limitation: Dam water catches fire when turbines turn.",
        f"Advantage: {benefit} | Limitation: Water turbines emit toxic sulfur dioxide gases.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Hydropower Balance Sheet in South Africa:**\n"
        f"- **Advantage:** {benefit}.\n"
        f"- **Limitation:** South Africa is a semi-arid, water-scarce country with an average rainfall (~450 mm/yr) well below global averages. {limitation}."
    )
    return {
        "id": f"ns7_en_35_{rng.randint(100000, 999999)}",
        "subskill": "35_hydropower_advantages_and_limitations",
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
        "learning_objective_id": "ns7_sources_35",
        "hints": {
            "tier_1": "Is South Africa a wet or water-scarce country?",
            "tier_2": "SA is water-stressed with limited perennial rivers, so hydro cannot power the whole country.",
            "tier_3": f"Advantage: {benefit} | Limitation: {limitation}.",
        },
        "misconception_tags": ["south_africa_has_unlimited_hydro_potential", "hydro_dam_produces_co2"],
    }


# 36. Biofuel definition and feedstocks
def arch_36_biofuel_definition_and_feedstocks(rng: random.Random) -> Dict[str, Any]:
    crops = [
        ("sugarcane cultivated in KwaZulu-Natal", "fermenting sucrose sugars into bioethanol liquid fuel"),
        ("maize grain harvested in the Free State maize triangle", "converting starches into ethanol fuel additives"),
        ("sunflower and canola crops in the Western Cape", "extracting biological vegetable oils for biodiesel production"),
        ("sweet sorghum grown in arid rural regions", "producing bioethanol from drought-resistant energy crops"),
    ]
    crop, process = rng.choice(crops)
    prompt = (
        f"A **biofuel** is any combustible fuel derived directly from recently living biological matter (biomass).\n\n"
        f"In South African agriculture, **{crop}** is considered a potential feedstock for **{process}**.\n"
        f"Why are biofuels categorized as renewable?"
    )
    correct = "The plants can be cultivated and regrown season after season through agriculture."
    distractors = [
        "They form underground over millions of years inside diamond mines.",
        "They do not contain any carbon atoms and therefore cannot burn in air.",
        "They emit zero heat when combusted, cooling the vehicle engine.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Definition of Biofuel:**\n"
        f"Biofuels are derived from living or recently deceased biological material.\n"
        f"Because {crop} can be grown repeatedly through agricultural cycles, it is **Renewable**."
    )
    return {
        "id": f"ns7_en_36_{rng.randint(100000, 999999)}",
        "subskill": "36_biofuel_definition_and_feedstocks",
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
        "learning_objective_id": "ns7_sources_36",
        "hints": {
            "tier_1": "Can farmers plant new crops every season?",
            "tier_2": "Because crops can be replanted annually, the resource is renewable.",
            "tier_3": "Plants can be cultivated and regrown season after season.",
        },
        "misconception_tags": ["biofuels_are_fossil_fuels", "biofuel_cannot_burn"],
    }


# 37. Biogas anaerobic digester process
def arch_37_biogas_anaerobic_digester_process(rng: random.Random) -> Dict[str, Any]:
    wastes = [
        ("fresh cattle manure from a dairy milking parlour", "anaerobic bacteria (microorganisms that thrive in the absence of oxygen)"),
        ("organic kitchen vegetable scraps and pig slurry", "decomposing microorganisms inside an airtight sealed digester tank"),
    ]
    organic_matter, agent = rng.choice(wastes)
    prompt = (
        f"On an agricultural farm, **{organic_matter}** is fed into an airtight biodigester.\n\n"
        f"How do **{agent}** convert this organic waste into combustible **biogas**?"
    )
    correct = (
        "They break down complex organic compounds in an oxygen-free environment, "
        "releasing a combustible gas mixture rich in methane (\\(\\text{{CH}}_4\\))."
    )
    distractors = [
        "They set the manure on fire underwater using microscopic spark plugs.",
        "They freeze the organic matter into solid blocks of coal over three days.",
        "They combine nitrogen with rock salt to create pressurized helium gas.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Anaerobic Digestion Process:**\n"
        f"1. **Anaerobic Conditions:** 'Anaerobic' means without free oxygen (\\(\\text{{O}}_2\\)).\n"
        f"2. **Microbial Action:** Bacteria ferment and decompose proteins, carbohydrates, and fats in {organic_matter}.\n"
        f"3. **Biogas Output:** The primary product is **biogas**, consisting of \\(\\sim 60\\%\\) methane (\\(\\text{{CH}}_4\\)) and \\(\\sim 40\\%\\) carbon dioxide (\\(\\text{{CO}}_2\\)), which burns cleanly."
    )
    return {
        "id": f"ns7_en_37_{rng.randint(100000, 999999)}",
        "subskill": "37_biogas_anaerobic_digester_process",
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
        "learning_objective_id": "ns7_sources_37",
        "hints": {
            "tier_1": "Recall what 'anaerobic' means.",
            "tier_2": "Anaerobic means without oxygen. Bacteria break down waste to make methane gas.",
            "tier_3": "Decomposition in oxygen-free conditions releases methane-rich combustible gas.",
        },
        "misconception_tags": ["digesters_require_open_air", "biogas_is_pure_oxygen"],
    }


# 38. Biogas case study farm manure benefits
def arch_38_biogas_case_study_farm_manure_benefits(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Fair Oaks Dairy Farm", "milks 30 000 cows daily", "half a million liters of diesel"),
        ("a commercial South African feedlot", "manages 12 000 beef cattle", "thousands of liters of diesel fuel for generators and tractors"),
    ]
    farm, scale, savings = rng.choice(cases)
    prompt = (
        f"In a textbook case study, **{farm}** ({scale}) installed a large anaerobic digester system.\n"
        f"The farm collects daily manure, extracts biogas, and powers its tractors, milk coolers, and delivery trucks, saving **{savings}** annually.\n\n"
        f"What additional environmental and agricultural benefit does the farm achieve?"
    )
    correct = "The leftover digested slurry serves as an odorless, nutrient-rich organic fertilizer for crop fields, leaving zero waste."
    distractors = [
        "The farm completely stops producing milk and only sells coal briquettes.",
        "The manure dissolves into plastic bags that can be sold to supermarkets.",
        "The process permanently prevents cows from generating any digestive gases.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Multiple Benefits of Biogas on Farms:**\n"
        f"1. **Clean Energy:** Generates renewable electricity and vehicle fuel, replacing {savings}.\n"
        f"2. **Odor Reduction:** Anaerobic digestion breaks down foul-smelling compounds in fresh manure.\n"
        f"3. **Nutrient Recycling:** The digested byproduct ('digestate') retains nitrogen, phosphorus, and potassium, serving as a superior organic crop fertilizer.\n"
        f"4. **Climate:** Captures methane that would otherwise vent into the atmosphere as a potent greenhouse gas."
    )
    return {
        "id": f"ns7_en_38_{rng.randint(100000, 999999)}",
        "subskill": "38_biogas_case_study_farm_manure_benefits",
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
        "learning_objective_id": "ns7_sources_38",
        "hints": {
            "tier_1": "What happens to the leftover solids after gas is extracted?",
            "tier_2": "The remaining digested material makes excellent, low-odor fertilizer.",
            "tier_3": "Leftover slurry is used as an odorless organic fertilizer, achieving zero waste.",
        },
        "misconception_tags": ["digester_waste_is_toxic", "biogas_destroys_soil_nutrients"],
    }


# 39. Bioethanol vs petroleum comparison
def arch_39_bioethanol_vs_petroleum_comparison(rng: random.Random) -> Dict[str, Any]:
    blends = [("E10 fuel (10% bioethanol blended with 90% petrol)", "reducing overall crude oil imports and carbon emissions"),
              ("bioethanol blended into automotive petrol", "lowering fossil fuel consumption in transport")]
    blend, benefit = rng.choice(blends)
    prompt = (
        f"South Africa explores mandatory blending of **{blend}** for **{benefit}**.\n\n"
        f"What major ethical and socioeconomic concern arises when expanding agricultural biofuel production?"
    )
    correct = "The 'food vs fuel' conflict: using arable farmland and maize/sugarcane crops for fuel could drive up staple food prices and threaten food security."
    distractors = [
        "Bioethanol makes car engines completely silent, causing pedestrians to walk into traffic.",
        "Growing maize and sugarcane absorbs 100% of all oxygen in the southern hemisphere.",
        "Bioethanol liquid instantly turns into solid ice at standard summer temperatures.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**The Biofuel Debate: Food vs Fuel:**\n"
        f"- Advantage: Biofuels are renewable and emit less net lifecycle carbon than pure fossil petroleum.\n"
        f"- Major concern: Arable land, fresh water, and staple crops (maize, sugarcane) are diverted from feeding people to feeding vehicles, risking food shortages and inflating food prices."
    )
    return {
        "id": f"ns7_en_39_{rng.randint(100000, 999999)}",
        "subskill": "39_bioethanol_vs_petroleum_comparison",
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
        "learning_objective_id": "ns7_sources_39",
        "hints": {
            "tier_1": "Think about what else maize and sugarcane are used for.",
            "tier_2": "If farmers grow crops for car fuel instead of food, what happens to food prices?",
            "tier_3": "Food vs fuel conflict: using farmland for fuel can increase food prices and reduce food security.",
        },
        "misconception_tags": ["biofuels_have_no_negative_consequences", "biofuels_are_toxic_to_engines"],
    }


# 40. Wood as energy source sustainability
def arch_40_wood_as_energy_source_sustainability(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("a community cutting down indigenous forests faster than seedlings can mature", "Non-renewable (deforestation causes permanent loss of woodland and topsoil erosion)"),
        ("a managed woodlot where three saplings are planted and nurtured for every mature tree harvested", "Renewable (rate of tree regrowth exceeds the rate of wood consumption)"),
    ]
    practice, verdict = rng.choice(scenarios)
    prompt = (
        f"Wood is widely used in rural South Africa for cooking and space heating.\n\n"
        f"Consider **{practice}**.\n"
        f"How is wood classified in this specific scenario?"
    )
    correct = f"It functions as **{verdict}**."
    distractors = [
        "It functions as a nuclear fission fuel because trees contain uranium atoms.",
        "It is always 100% non-renewable because trees take millions of years to grow.",
        "It functions as crude petroleum oil because leaves contain green chlorophyll.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Sustainability of Wood as Fuel:**\n"
        f"Wood is biological biomass. Its classification depends strictly on harvest practices:\n"
        f"- If replanted sustainably: **Renewable**.\n"
        f"- If harvested through uncontrolled deforestation: **Non-renewable**.\n\n"
        f"In this scenario: **{verdict}**."
    )
    return {
        "id": f"ns7_en_40_{rng.randint(100000, 999999)}",
        "subskill": "40_wood_as_energy_source_sustainability",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": f"It functions as **{verdict}**.",
        "sample_answer": f"It functions as **{verdict}**.",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_sources_40",
        "hints": {
            "tier_1": "Look at whether trees are being replaced faster or slower than they are cut down.",
            "tier_2": "Regrowth keeps it renewable; deforestation makes it non-renewable.",
            "tier_3": f"Identify {verdict}.",
        },
        "misconception_tags": ["wood_is_always_renewable_regardless_of_deforestation"],
    }


# 41. Indoor air pollution wood coal braziers
def arch_41_indoor_air_pollution_wood_coal_braziers(rng: random.Random) -> Dict[str, Any]:
    appliances = [
        ("an unventilated coal brazier (imbawula)", "carbon monoxide (\\(\\text{{CO}}\\)) and fine particulate soot", "severe respiratory illness and fatal poisoning"),
        ("an indoor open wood fire inside a closed room during cold winter nights", "toxic smoke containing carbon monoxide and particulates", "asphyxiation and chronic lung damage"),
    ]
    app, pollutants, hazard = rng.choice(appliances)
    prompt = (
        f"During winter in informal settlements and rural homes, people often warm living spaces using **{app}**.\n\n"
        f"Why is burning coal or wood inside a closed, unventilated room extremely dangerous to human health?"
    )
    correct = f"Incomplete combustion releases {pollutants}, which causes {hazard} in unventilated spaces."
    distractors = [
        "It releases pure oxygen which makes the air so cold that occupants freeze instantly.",
        "It releases radioactive gamma waves that melt the metal furniture in the room.",
        "It attracts wild animals that are drawn into homes by magnetic heat waves.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Hazards of Indoor Solid Fuel Combustion:**\n"
        f"1. **Incomplete Combustion:** In closed rooms with limited oxygen, carbon burns incompletely: \\(2\\text{{C}} + \\text{{O}}_2 \\rightarrow 2\\text{{CO}}\\).\n"
        f"2. **Carbon Monoxide (\\(\\text{{CO}}\\)):** An odorless, colorless, lethal gas that binds tightly to hemoglobin, preventing oxygen delivery to the brain and heart ({hazard}).\n"
        f"3. **Particulates:** Soot damages lung tissue and exacerbates asthma and pneumonia."
    )
    return {
        "id": f"ns7_en_41_{rng.randint(100000, 999999)}",
        "subskill": "41_indoor_air_pollution_wood_coal_braziers",
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
        "learning_objective_id": "ns7_sources_41",
        "hints": {
            "tier_1": "Recall the dangerous invisible gas produced by incomplete combustion in closed rooms.",
            "tier_2": "Carbon monoxide is an odorless, deadly gas formed when fuel burns without enough oxygen.",
            "tier_3": "Incomplete combustion releases carbon monoxide and soot, causing severe illness or fatal poisoning.",
        },
        "misconception_tags": ["smoke_is_harmless_if_warm", "carbon_monoxide_has_a_strong_smell"],
    }


# 42. Acid rain causes coal combustion
def arch_42_acid_rain_causes_coal_combustion(rng: random.Random) -> Dict[str, Any]:
    gases = [
        ("sulfur impurities inside coal", "sulfur dioxide (\\(\\text{{SO}}_2\\))", "dilute sulfuric acid (\\(\\text{{H}}_2\\text{{SO}}_4\\))"),
        ("high combustion temperatures in coal boilers", "nitrogen oxides (\\(\\text{{NO}}_x\\))", "dilute nitric acid (\\(\\text{{HNO}}_3\\))"),
    ]
    origin, gas, acid = rng.choice(gases)
    prompt = (
        f"Coal mined in South Africa contains **{origin}**. When burned in coal power stations, it produces **{gas}**.\n\n"
        f"How does this emission lead to the formation of **acid rain**?"
    )
    correct = f"The {gas} reacts chemically with atmospheric water vapor and oxygen to form {acid}, which falls as acidic precipitation."
    distractors = [
        f"The {gas} freezes into solid alkaline crystals that neutralize all clouds.",
        f"The {gas} reacts with sunlight to produce radioactive lead bullets.",
        f"The {gas} dissolves Earth's gravity, allowing ocean water to float into clouds.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Chemistry of Acid Rain:**\n"
        f"1. Coal contains sulfur and nitrogen impurities: burning releases {gas}.\n"
        f"2. Atmospheric reaction:\n"
        f"$$\\text{{SO}}_2 + \\text{{H}}_2\\text{{O}} \\rightarrow \\text{{H}}_2\\text{{SO}}_3 \\quad \\text{{and}} \\quad 2\\text{{SO}}_2 + \\text{{O}}_2 + 2\\text{{H}}_2\\text{{O}} \\rightarrow 2\\text{{H}}_2\\text{{SO}}_4$$\n"
        f"3. Result: Rain with a low pH (<5.0) containing {acid}."
    )
    return {
        "id": f"ns7_en_42_{rng.randint(100000, 999999)}",
        "subskill": "42_acid_rain_causes_coal_combustion",
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
        "learning_objective_id": "ns7_sources_42",
        "hints": {
            "tier_1": "What happens when sulfur gases mix with rainwater in the clouds?",
            "tier_2": "Sulfur dioxide reacts with moisture to form dilute sulfuric acid.",
            "tier_3": f"Gases react with atmospheric water vapor to form {acid}.",
        },
        "misconception_tags": ["acid_rain_caused_by_carbon_dioxide_alone", "acid_rain_burns_skin_instantly"],
    }


# 43. Acid rain impact environment materials
def arch_43_acid_rain_impact_environment_materials(rng: random.Random) -> Dict[str, Any]:
    targets = [
        ("freshwater ecosystems such as streams and dams in Mpumalanga", "acidifying water bodies, which leaches toxic aluminum from soils and kills fish eggs and aquatic insects"),
        ("historic buildings, limestone monuments, and bridge metalwork", "chemically corroding calcium carbonate in stone and accelerating iron and steel rusting"),
        ("forests and agricultural soil", "leaching essential mineral nutrients (calcium, magnesium) from the soil and damaging protective waxy leaf layers"),
    ]
    subject, damage = rng.choice(targets)
    prompt = (
        f"Regions downwind of major industrial coal-burning clusters experience acidic precipitation.\n\n"
        f"What is a verified detrimental effect of acid rain on **{subject}**?"
    )
    correct = f"It causes damage by {damage}."
    distractors = [
        "It turns all natural rivers into pure petrol that can be used directly in motor cars.",
        "It causes concrete structures to grow five times their original size every month.",
        "It eliminates all weeds permanently without harming any agricultural crops.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Environmental & Structural Damage from Acid Rain:**\n"
        f"Acid rain (pH < 5) damages both natural and built environments:\n"
        f"- For {subject}: **{damage.capitalize()}**.\n"
        f"- This demonstrates the indirect environmental cost of relying heavily on unscrubbed coal combustion."
    )
    return {
        "id": f"ns7_en_43_{rng.randint(100000, 999999)}",
        "subskill": "43_acid_rain_impact_environment_materials",
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
        "learning_objective_id": "ns7_sources_43",
        "hints": {
            "tier_1": "Recall how acid affects aquatic life, limestone rocks, and metals.",
            "tier_2": "Acids dissolve calcium carbonate (stone) and make water toxic to aquatic organisms.",
            "tier_3": f"Identify the option describing how it {damage}.",
        },
        "misconception_tags": ["acid_rain_only_harms_plants", "acid_rain_does_not_affect_metals"],
    }


# 44. Energy source comparison table cost reliability
def arch_44_energy_source_comparison_table_cost_reliability(rng: random.Random) -> Dict[str, Any]:
    sources = [
        ("Coal thermal power", "High (burns fuel on demand 24/7)", "Very high (greenhouse gases, acid rain, fly ash)", "Reliable continuous baseload, but high pollution and non-renewable"),
        ("Solar photovoltaic", "Intermittent (daylight and sunny weather only)", "Very low during operation (zero fuel emissions)", "Zero operational fuel emissions, but requires storage for nighttime supply"),
        ("Wind power", "Intermittent (dependent on wind velocity)", "Very low during operation (zero fuel emissions)", "Clean renewable power, but fluctuates with weather patterns"),
        ("Nuclear power", "High (operates continuously for months between refueling)", "Zero greenhouse gases; long-term radioactive waste", "Continuous zero-carbon baseload, but costly and produces hazardous waste"),
    ]
    src, rel, env, summary = rng.choice(sources)
    prompt = (
        f"Consider the evaluation criteria for **{src}**:\n"
        f"- **Reliability:** {rel}\n"
        f"- **Environmental Impact:** {env}\n\n"
        f"Which statement best summarizes the strategic trade-off of this energy source?"
    )
    correct = summary
    distractors = [
        "It provides infinite free power 24/7 with zero cost and zero machinery.",
        "It cannot generate electrical current under any circumstances.",
        "It should be banned completely because all energy sources are identical in impact.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Energy Mix Evaluation:**\n"
        f"No single energy source is perfect in isolation:\n"
        f"- {src} provides: **{summary}**.\n"
        f"A balanced national energy mix blends baseload reliability with low-carbon renewable generation."
    )
    return {
        "id": f"ns7_en_44_{rng.randint(100000, 999999)}",
        "subskill": "44_energy_source_comparison_table_cost_reliability",
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
        "learning_objective_id": "ns7_sources_44",
        "hints": {
            "tier_1": "Consider both reliability (when does it work?) and environmental impact.",
            "tier_2": "Look at the summary that balances both points accurately.",
            "tier_3": f"The correct summary is: {summary}.",
        },
        "misconception_tags": ["a_single_perfect_energy_source_exists", "all_renewables_are_dispatchable"],
    }


# 45. Baseload vs intermittent power grid
def arch_45_baseload_vs_intermittent_power_grid(rng: random.Random) -> Dict[str, Any]:
    concepts = [
        ("Baseload power", "the minimum continuous electrical power that must be supplied to the grid 24 hours a day to run hospitals, factories, and homes"),
        ("Intermittent (variable) power", "energy generation that varies unpredictably based on weather conditions (e.g. cloud cover or changing wind speeds)"),
    ]
    term, defn = rng.choice(concepts)
    prompt = (
        f"Electrical grid operators must balance supply and demand every second.\n\n"
        f"In power system planning, what does the term **{term}** mean?"
    )
    correct = defn
    distractors = [
        "Power that is only generated when lightning strikes transmission pylons.",
        "Electricity stored exclusively in portable smartphone batteries.",
        "Current that flows backward through home appliances to cool them down.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Grid Power Terminology:**\n"
        f"- **Baseload:** {defn if term.startswith('Base') else 'The minimum constant load required 24/7.'}\n"
        f"- **Intermittent / Variable:** Power sources (solar, wind) that fluctuate with sunlight and wind conditions.\n"
        f"- Therefore, **{term}** means: {defn}."
    )
    return {
        "id": f"ns7_en_45_{rng.randint(100000, 999999)}",
        "subskill": "45_baseload_vs_intermittent_power_grid",
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
        "learning_objective_id": "ns7_sources_45",
        "hints": {
            "tier_1": "Consider what 'base' or 'intermittent' suggests in regular English.",
            "tier_2": "Baseload is the constant foundation; intermittent means variable/on-and-off.",
            "tier_3": f"{defn}.",
        },
        "misconception_tags": ["grid_can_run_without_baseload_or_storage", "solar_panels_generate_baseload_at_night"],
    }


# 46. Energy conservation in households
def arch_46_energy_conservation_in_households(rng: random.Random) -> Dict[str, Any]:
    measures = [
        ("fitting an insulating thermal geyser blanket and setting the thermostat to 55-60 °C", "electric geysers account for 30% to 40% of typical home electricity consumption"),
        ("replacing old incandescent light bulbs with high-efficiency LED bulbs", "LEDs use up to 80% less electricity to produce the same lumens of light"),
        ("switching off appliances at the wall plug rather than leaving them in standby mode", "standby mode continuously draws 'vampire' electrical power"),
        ("using thick roof ceiling insulation (fiberglass or cellulose)", "reduces heat loss in winter and heat gain in summer, lowering heating/cooling energy needs"),
    ]
    action, rationale = rng.choice(measures)
    prompt = (
        f"To reduce strain on the national grid and decrease fossil fuel emissions, households practice **energy conservation**.\n\n"
        f"Why is **{action}** an effective energy-saving strategy?"
    )
    correct = f"Because {rationale}, significantly cutting wasted electrical energy."
    distractors = [
        "Because it transforms household water pipes into gold conduits.",
        "Because it makes electricity flow through the air without wiring.",
        "Because it causes electrical meters to spin backward automatically.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Principles of Energy Conservation:**\n"
        f"Conservation means avoiding waste and using less energy to achieve the same task.\n"
        f"- Action: {action}.\n"
        f"- Rationale: {rationale.capitalize()}."
    )
    return {
        "id": f"ns7_en_46_{rng.randint(100000, 999999)}",
        "subskill": "46_energy_conservation_in_households",
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
        "learning_objective_id": "ns7_sources_46",
        "hints": {
            "tier_1": "Think about why this measure reduces monthly electricity usage.",
            "tier_2": "Look for the scientific reason explaining reduced electrical waste.",
            "tier_3": f"Because {rationale}.",
        },
        "misconception_tags": ["standby_mode_uses_zero_power", "geysers_use_minimal_power"],
    }


# 47. Renewable energy myths and facts
def arch_47_renewable_energy_myths_and_facts(rng: random.Random) -> Dict[str, Any]:
    myths = [
        ("Renewable energy is impossible to integrate because it can never supply power at night or during calm weather",
         "Fact: Battery storage systems, pumped storage hydro, and diversified geographic grids store energy to supply power seamlessly during lulls."),
        ("Manufacturing solar panels and wind turbines consumes more energy than they will ever generate during their lifetime",
         "Fact: Modern solar panels pay back their manufacturing energy debt within 1 to 3 years of operation, generating clean power for 25+ years."),
        ("Clean energy technologies are vastly more expensive than fossil fuels under all circumstances",
         "Fact: Levelized cost of utility-scale solar PV and onshore wind has dropped significantly below new coal power generation."),
    ]
    myth, fact = rng.choice(myths)
    prompt = (
        f"In debates about South Africa's energy transition, misconceptions often circulate.\n\n"
        f"Consider the claim: *\"{myth}\"*\n"
        f"How does scientific and engineering evidence refute this claim?"
    )
    correct = fact
    distractors = [
        "Evidence confirms the claim is 100% correct and renewable energy should be abandoned completely.",
        "Evidence shows that wind turbines generate power by burning coal inside their rotor blades.",
        "Evidence proves that solar panels only work if placed directly inside volcanic lava.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Debunking Energy Myths:**\n"
        f"- Claim: *\"{myth}\"*\n"
        f"- Scientific reality: **{fact}**\n"
        f"Rigorous lifecycle analysis proves that renewable systems provide a net positive energy and environmental benefit."
    )
    return {
        "id": f"ns7_en_47_{rng.randint(100000, 999999)}",
        "subskill": "47_renewable_energy_myths_and_facts",
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
        "learning_objective_id": "ns7_sources_47",
        "hints": {
            "tier_1": "Consider modern solutions like battery energy storage systems (BESS).",
            "tier_2": "Look for the factual statement backed by engineering reality.",
            "tier_3": f"{fact}.",
        },
        "misconception_tags": ["renewables_cannot_support_modern_grids", "energy_payback_myth"],
    }


# 48. Misconception clean infinite vs renewable
def arch_48_misconception_clean_infinite_vs_renewable(rng: random.Random) -> Dict[str, Any]:
    distinctions = [
        ("Uranium nuclear power", "is clean regarding carbon emissions (zero greenhouse gases during generation), but is non-renewable because uranium ore deposits on Earth are finite"),
        ("Burning firewood from unmanaged deforestation", "is biological and can be renewable in principle, but is not clean when burned (emits particulate soot and carbon dioxide)"),
    ]
    src, distinction = rng.choice(distinctions)
    prompt = (
        f"Learners sometimes confuse the term **'clean energy'** (low/zero emissions) with **'renewable energy'** (naturally replenished).\n\n"
        f"How does **{src}** illustrate the scientific difference between these two concepts?"
    )
    correct = f"It {distinction}."
    distractors = [
        "It shows that clean energy and renewable energy are identical scientific synonyms with zero difference.",
        "It proves that all renewable fuels are non-combustible and produce zero heat.",
        "It demonstrates that non-renewable resources can be cloned in kitchen microwaves.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Critical Distinction in Energy Classification:**\n"
        f"- **Renewable:** Defined by replenishment rate (replenished by natural cycles vs finite stock).\n"
        f"- **Clean / Low-Carbon:** Defined by emission profile (low or zero pollution / greenhouse gases).\n\n"
        f"{src} {distinction}."
    )
    return {
        "id": f"ns7_en_48_{rng.randint(100000, 999999)}",
        "subskill": "48_misconception_clean_infinite_vs_renewable",
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
        "learning_objective_id": "ns7_sources_48",
        "hints": {
            "tier_1": "Can a fuel be zero-emission but still have a finite supply?",
            "tier_2": "Uranium emits no carbon dioxide, but mineral ore reserves are finite.",
            "tier_3": f"It {distinction}.",
        },
        "misconception_tags": ["clean_energy_always_equals_renewable", "nuclear_is_renewable"],
    }


# 49. Misconception nuclear vs fossil smoke
def arch_49_misconception_nuclear_vs_fossil_smoke(rng: random.Random) -> Dict[str, Any]:
    stations = [
        ("Koeberg Nuclear Power Station", "white plume billowing from large cooling towers", "condensed water vapor (steam) from the cooling circuit"),
        ("a thermal power plant cooling tower", "white cloud emitted into the sky", "clean evaporated water steam, not smoke or carbon dioxide"),
    ]
    plant, visual, reality = rng.choice(stations)
    prompt = (
        f"A common misconception is that the **{visual}** at **{plant}** is dangerous toxic smoke or carbon pollution.\n\n"
        f"What is that white plume in reality?"
    )
    correct = f"It is {reality}; it contains no carbon emissions or toxic smoke."
    distractors = [
        "It is pure uranium gas that spreads radioactivity over the entire continent.",
        "It is concentrated carbon dioxide gas that has turned white due to extreme freezing.",
        "It is powdered coal dust that escaped through emergency exhaust pipes.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Cooling Tower Science:**\n"
        f"Thermal and nuclear power stations use cooling towers to condense steam back into water.\n"
        f"The white plume seen rising from cooling towers is simply **{reality}**, exactly like steam rising from a domestic boiling kettle."
    )
    return {
        "id": f"ns7_en_49_{rng.randint(100000, 999999)}",
        "subskill": "49_misconception_nuclear_vs_fossil_smoke",
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
        "learning_objective_id": "ns7_sources_49",
        "hints": {
            "tier_1": "What happens when hot water evaporates into cool air?",
            "tier_2": "Cooling towers release pure evaporated water (steam/clouds), not smoke.",
            "tier_3": f"It is {reality}.",
        },
        "misconception_tags": ["cooling_tower_steam_is_smoke", "cooling_towers_emit_radiation"],
    }


# 50. Sources of energy comprehensive diagnostic
def arch_50_sources_of_energy_comprehensive_diagnostic(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A South African municipality transitions from coal-powered electricity to a hybrid solar PV and pumped-storage hydro network",
         "Non-renewable fossil fuels with high greenhouse gas emissions -> Renewable resources with zero operating carbon emissions",
         "Substantial reduction in local air pollution and greenhouse emissions, though requiring initial capital investment for storage"),
        ("An agricultural farming district converts diesel irrigation pumps to solar panels and biogas digesters",
         "Non-renewable imported petroleum fuels -> Renewable locally generated solar and agricultural biomass",
         "Eliminates diesel fuel costs, lowers carbon footprint, and recycles manure into clean fertilizer"),
    ]
    transition, classification_shift, outcome = rng.choice(scenarios)
    prompt = (
        f"**Comprehensive Energy Transition Diagnostic:**\n\n"
        f"Scenario: **{transition}**.\n\n"
        f"Which analysis correctly categorizes the shift in energy resources and its principal environmental outcome?"
    )
    correct = f"Shift: {classification_shift}. Primary Outcome: {outcome}."
    distractors = [
        "Shift: Renewable resources -> Non-renewable minerals. Primary Outcome: Increased sulfur dioxide and soot emissions.",
        "Shift: Nuclear fission -> Chemical combustion of plastic. Primary Outcome: Complete depletion of atmospheric nitrogen.",
        "Shift: No shift occurred because all energy systems operate under identical physics. Primary Outcome: Zero change.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Comprehensive Diagnostic Analysis:**\n"
        f"1. **Resource Classification:** {classification_shift}.\n"
        f"2. **Environmental & Practical Impact:** {outcome}.\n"
        f"This synthesis connects energy classification, operational mechanics, and long-term environmental sustainability."
    )
    return {
        "id": f"ns7_en_50_{rng.randint(100000, 999999)}",
        "subskill": "50_sources_of_energy_comprehensive_diagnostic",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "ns7_sources_50",
        "hints": {
            "tier_1": "Identify what is being replaced (fossil fuels) and what replaces it (renewables).",
            "tier_2": "Look for the option showing the shift from non-renewable to renewable.",
            "tier_3": f"Shift: {classification_shift}. Primary Outcome: {outcome}.",
        },
        "misconception_tags": ["energy_transitions_have_no_benefits", "all_energy_resources_are_equivalent"],
    }
