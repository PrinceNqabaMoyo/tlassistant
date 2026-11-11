"""Grade 9 Natural Sciences - The Earth as a System: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 4/01. The earth as a system.md
Focus:
Cascading event impacts (volcanic eruptions across all 4 spheres: atmospheric cooling, acid rain, fertile soil;
subsea earthquakes & tsunamis; tropical cyclones; deforestation & soil erosion; disruption of water cycle),
Anthropogenic disruptions & feedbacks (fossil fuel carbon flux, enhanced greenhouse effect, ice-albedo positive feedback,
cloud negative feedback, ocean acidification, cryosphere sea level rise, acid mine drainage, wetlands as biofilters,
desertification, permafrost methane feedback, eutrophication, plastic pollution),
Systems science & history (Biosphere 2 experiment, Gaia hypothesis, Planetary boundaries,
Eduard Suess & Vladimir Vernadsky, Satellite remote sensing, Comprehensive Diagnostic Autopsy).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_volcanic_eruption_lithosphere_to_atmosphere_cooling(rng: random.Random) -> Dict[str, Any]:
    volcano, year, drop = rng.choice([
        ("Mount Pinatubo in the Philippines", 1991, "0,5 °C globally for nearly two years"),
        ("Mount Tambora in Indonesia", 1815, "over 1 °C, resulting in the famous 1816 'Year Without a Summer'")
    ])
    prompt = (
        f"The massive volcanic eruption of **{volcano}** in {year} originated in the lithosphere but caused a global atmospheric temperature drop of {drop}.\n\n"
        "What specific atmospheric mechanism caused this global cooling effect following the eruption?"
    )
    correct = "Sulfur dioxide (SO2) gas injected into the stratosphere reacted with moisture to form reflective sulfate aerosols that bounced incoming solar radiation back into space."
    options = [
        correct,
        "The volcano absorbed all heat from the Earth's core, cooling the continents.",
        "Volcanic ash froze the clouds into solid nitrogen snow that fell across the tropics.",
        "The eruption blew a hole in the atmosphere that allowed outer space cold air to rush in."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Volcanic aerosol production:\n"
        "Explosive eruptions inject millions of tonnes of SO2 directly into the stable stratosphere.\n"
        "Step 2: Stratospheric optical scattering:\n"
        "SO2 reacts with water vapor to form microscopic sulfuric acid (H2SO4) aerosol droplets. These aerosols remain suspended for 1–3 years, increasing planetary albedo by scattering incoming sunlight and causing global surface cooling."
    )
    return {
        "id": f"ns9_eas_26_{rng.randint(100000, 999999)}",
        "subskill": "26_volcanic_eruption_lithosphere_to_atmosphere_cooling",
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
        "hints": {
            "tier_1": "What reflective chemical droplets form in the stratosphere from volcanic gas?",
            "tier_2": "Sulfate aerosols that reflect sunlight back to space.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["volcanic_stratospheric_sulfate_aerosol_cooling"]
    }


def arch_27_volcanic_eruption_hydrosphere_acid_rain_cascade(rng: random.Random) -> Dict[str, Any]:
    gases = rng.choice(["sulfur dioxide (SO2) and hydrogen chloride (HCl)", "sulfur oxides and volcanic halogens"])
    prompt = (
        f"During major volcanic eruptions, enormous volumes of {gases} enter atmospheric storm clouds.\n\n"
        "How does this lithosphere-atmosphere emission trigger a harmful cascade into the hydrosphere and freshwater biosphere?"
    )
    correct = "The volcanic gases dissolve into condensed cloud droplets to form acid precipitation (pH < 4), which falls into lakes and rivers, causing acute acidification that kills aquatic fish, amphibians, and invertebrates."
    options = [
        correct,
        "The volcanic gases turn all freshwater rivers into solid glass instantly.",
        "The volcanic gases cause ocean water to evaporate into pure alcohol.",
        "The volcanic gases make rivers glow in the dark without changing chemical pH."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Acid gas dissolution:\n"
        "SO2 + H2O → H2SO3; 2H2SO3 + O2 → 2H2SO4 (sulfuric acid); HCl dissolves to form hydrochloric acid.\n"
        "Step 2: Hydrosphere cascade:\n"
        "Acid rain lowers the pH of lakes and streams below 4,5, mobilizing toxic aluminum ions from soil and causing catastrophic fish kills and biodiversity loss in aquatic biomes."
    )
    return {
        "id": f"ns9_eas_27_{rng.randint(100000, 999999)}",
        "subskill": "27_volcanic_eruption_hydrosphere_acid_rain_cascade",
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
        "hints": {
            "tier_1": "What happens when volcanic sulfur gas dissolves in cloud water?",
            "tier_2": "It forms acid rain, acidifying lakes and streams.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["volcanic_acid_rain_hydrosphere_cascade"]
    }


def arch_28_volcanic_eruption_biosphere_habitat_destruction_and_soil(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Volcanic eruptions represent a classic ecological paradox for the biosphere: they cause immediate devastation, yet create long-term agricultural fertility.\n\n"
        "Why do civilizations historically establish dense farming settlements around the slopes of active volcanoes despite the catastrophic risks?"
    )
    correct = "Because weathered volcanic ash and basaltic rock break down into extraordinarily fertile soils (andosols) rich in bioavailable minerals like potassium, phosphorus, calcium, and magnesium."
    options = [
        correct,
        "Because volcanic heat keeps crops warm so they never require water or sunlight.",
        "Because active volcanoes emit free gold and diamond nuggets directly into topsoil.",
        "Because volcanic radiation causes vegetables to grow to the size of automobiles."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Immediate destruction:\n"
        "Pyroclastic flows, toxic gases, and heavy tephra bury and incinerate immediate ecosystems.\n"
        "Step 2: Long-term pedogenesis:\n"
        "Volcanic tephra is rich in unweathered volcanic glass and minerals. As rainfall and pioneer vegetation weather the ash, it develops high cation exchange capacity and exceptional moisture retention, producing some of the most productive agricultural soils on Earth."
    )
    return {
        "id": f"ns9_eas_28_{rng.randint(100000, 999999)}",
        "subskill": "28_volcanic_eruption_biosphere_habitat_destruction_and_soil",
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
        "hints": {
            "tier_1": "Why is volcanic soil so good for farming?",
            "tier_2": "Weathered ash is rich in essential nutrients like potassium and phosphorus.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["volcanic_andosols_pedogenesis_fertility"]
    }


def arch_29_subsea_earthquake_lithosphere_tsunami_hydrosphere_cascade(rng: random.Random) -> Dict[str, Any]:
    mag = rng.choice(["magnitude 9,1 megathrust earthquake", "massive subsea tectonic fault rupture"])
    prompt = (
        f"A {mag} occurs along an oceanic subduction zone in the lithosphere.\n\n"
        "How does this sudden lithospheric displacement trigger a multi-sphere cascade into the hydrosphere and terrestrial biosphere?"
    )
    correct = "Sudden vertical displacement of the seafloor displaces the entire overlying water column, generating high-speed tsunami waves across the hydrosphere that inundate coastal lands, destroying mangroves and depositing saline sand into topsoils."
    options = [
        correct,
        "The earthquake shakes the atmosphere until all clouds turn into liquid gasoline.",
        "The earthquake makes all ocean water evaporate instantly into deep space.",
        "The earthquake turns marine fish into terrestrial birds that fly away."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Lithosphere trigger:\n"
        "Elastic rebound along a subsea fault thrusts the seabed vertically by several meters.\n"
        "Step 2: Hydrosphere transmission:\n"
        "The displaced water column forms long-wavelength tsunami waves traveling at jet-airliner speeds (>700 km/h) in deep water.\n"
        "Step 3: Biosphere & Lithosphere impact:\n"
        "Upon shoaling at coasts, wave heights surge, leveling coastal ecosystems (biosphere) and salinizing agricultural soils (lithosphere)."
    )
    return {
        "id": f"ns9_eas_29_{rng.randint(100000, 999999)}",
        "subskill": "29_subsea_earthquake_lithosphere_tsunami_hydrosphere_cascade",
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
        "hints": {
            "tier_1": "What does a vertical seabed shift create in the ocean?",
            "tier_2": "A tsunami wave that inundates coastal ecosystems.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["tsunami_megathrust_multisphere_cascade"]
    }


def arch_30_tropical_cyclone_hydrosphere_atmosphere_biosphere_impact(rng: random.Random) -> Dict[str, Any]:
    cyclone = rng.choice(["Tropical Cyclone Idai (2019)", "Tropical Cyclone Freddy (2023)"])
    prompt = (
        f"**{cyclone}** devastated parts of Mozambique, Zimbabwe, and Malawi, serving as a powerful case study of Earth sphere interactions.\n\n"
        "What specific energetic and physical linkages among the hydrosphere, atmosphere, and biosphere occur during such a cyclone?"
    )
    correct = "Warm ocean waters (>26,5 °C) supply immense latent heat to power an atmospheric low-pressure vortex; torrential rains and coastal storm surges drown terrestrial habitats and trigger destructive soil mudslides."
    options = [
        correct,
        "Cold Antarctic icebergs float into the tropics, generating volcanic eruptions on the beaches.",
        "The cyclone is generated by underground nuclear explosions triggered by marine mammals.",
        "The cyclone sucks all water out of the Indian Ocean, leaving a dry rock canyon."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Hydrosphere energy source:\n"
        "Thermal energy from ocean waters >26,5 °C drives high evaporation.\n"
        "Step 2: Atmospheric storm engine:\n"
        "Latent heat of condensation intensifies the low-pressure vortex, generating sustained destructive winds.\n"
        "Step 3: Terrestrial biosphere/lithosphere destruction:\n"
        "Catastrophic flooding drowns crops, spreads cholera waterborne pathogens, and washes away fertile topsoil."
    )
    return {
        "id": f"ns9_eas_30_{rng.randint(100000, 999999)}",
        "subskill": "30_tropical_cyclone_hydrosphere_atmosphere_biosphere_impact",
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
        "hints": {
            "tier_1": "What fuels a tropical cyclone?",
            "tier_2": "Warm ocean water providing latent heat to the atmospheric vortex.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["tropical_cyclone_energy_cascade"]
    }


def arch_31_deforestation_biosphere_to_lithosphere_erosion_cascade(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When humans clear large tracts of natural forest (clear-cutting in the biosphere), severe consequences cascade immediately into the lithosphere and hydrosphere.\n\n"
        "Why does removing tree canopy and roots cause catastrophic soil erosion and river siltation?"
    )
    correct = "Tree roots physically anchor topsoil and canopies intercept heavy raindrops; without them, raindrop impact dislodges soil particles and unhindered runoff washes fertile topsoil into streams, causing severe river siltation."
    options = [
        correct,
        "Tree roots produce magnetic fields that hold tectonic plates together.",
        "Without trees, soil turns into molten lava within twenty-four hours.",
        "Cutting down trees causes earthworms to multiply until they consume all the rocks."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Canopy protection and root binding:\n"
        "Canopies dissipate the kinetic energy of falling raindrops. Intertwined root networks mechanically bind soil aggregates.\n"
        "Step 2: Erosion cascade:\n"
        "Deforestation leaves topsoil exposed. Raindrop splash erodes topsoil, runoff carves deep gullies (dongas), and washed sediment fills river beds (siltation), causing flash floods and suffocating fish gills."
    )
    return {
        "id": f"ns9_eas_31_{rng.randint(100000, 999999)}",
        "subskill": "31_deforestation_biosphere_to_lithosphere_erosion_cascade",
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
        "hints": {
            "tier_1": "What do tree roots and canopies do to protect soil?",
            "tier_2": "Canopies absorb raindrop impact; roots bind the topsoil.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["deforestation_soil_erosion_cascade"]
    }


def arch_32_deforestation_impact_on_hydrological_cycle_drought(rng: random.Random) -> Dict[str, Any]:
    region = rng.choice(["the Congo Basin rainforest", "the Amazon Basin", "the indigenous coastal forests of Southern Africa"])
    prompt = (
        f"Widespread deforestation in large biomes such as {region} significantly disrupts regional weather and precipitation.\n\n"
        "Why does large-scale forest loss lead to severe regional droughts and reduced precipitation?"
    )
    correct = "Trees recycle enormous volumes of groundwater into the atmosphere via evapotranspiration; eliminating trees cuts off this atmospheric moisture supply, drastically suppressing cloud formation and rainfall."
    options = [
        correct,
        "Trees act as giant suction pumps that drink all rain before it can hit the ground.",
        "Without trees, air pressure increases to ten times normal atmospheric levels.",
        "Trees emit radioactive rays that freeze moisture into invisible space clouds."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The biotic pump:\n"
        "Forests act as giant biotic moisture pumps. A single large mature tree can transpire over 500 liters of water per day.\n"
        "Step 2: Rainfall suppression:\n"
        "When millions of trees are cleared, atmospheric humidity drops precipitously. Fewer convective clouds develop, converting once-lush rainforest ecosystems into arid scrubland or desert (savannization)."
    )
    return {
        "id": f"ns9_eas_32_{rng.randint(100000, 999999)}",
        "subskill": "32_deforestation_impact_on_hydrological_cycle_drought",
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
        "hints": {
            "tier_1": "What happens to atmospheric humidity when trees that transpire are removed?",
            "tier_2": "Atmospheric moisture drops, causing reduced cloud formation and drought.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["deforestation_evapotranspiration_drought"]
    }


def arch_33_anthropogenic_fossil_fuel_combustion_carbon_flux(rng: random.Random) -> Dict[str, Any]:
    tons = rng.choice(["over 35 billion tonnes", "approximately 36 to 40 billion metric tons"])
    prompt = (
        f"Human industrial activity combusts fossil fuels, releasing {tons} of carbon dioxide into the atmosphere each year.\n\n"
        "In systems science terms, how does this human activity dramatically alter the natural carbon cycle balance?"
    )
    correct = "It rapidly transfers carbon stored for hundreds of millions of years in the deep lithosphere into the active atmospheric reservoir at a rate hundreds of times faster than natural geological outgassing."
    options = [
        correct,
        "It removes all carbon from the Earth system and launches it into lunar orbit.",
        "It converts atmospheric carbon dioxide into pure solid gold on mountaintops.",
        "It stops plant photosynthesis by making all leaves completely opaque."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Slow vs fast carbon cycle:\n"
        "Naturally, carbon in the lithosphere cycles over tens of millions of years via volcanism and silicate weathering.\n"
        "Step 2: Anthropogenic perturbation:\n"
        "By burning coal, petroleum, and natural gas in just two centuries, humans short-circuited the slow geological cycle, overloading the atmosphere with CO2 faster than oceans and forests can reabsorb it."
    )
    return {
        "id": f"ns9_eas_33_{rng.randint(100000, 999999)}",
        "subskill": "33_anthropogenic_fossil_fuel_combustion_carbon_flux",
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
        "hints": {
            "tier_1": "What reservoir is fossil fuel carbon taken from, and where is it dumped?",
            "tier_2": "From the deep lithosphere into the atmosphere.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["fossil_fuel_carbon_flux_perturbation"]
    }


def arch_34_enhanced_greenhouse_effect_and_global_warming_feedback(rng: random.Random) -> Dict[str, Any]:
    conc = rng.choice(["from ~280 ppm pre-industrial to over 420 ppm today", "by roughly 50% above historical pre-industrial levels"])
    prompt = (
        f"Atmospheric carbon dioxide concentrations have risen {conc} due to human activity.\n\n"
        "How does this create the **enhanced greenhouse effect** and drive global climate change?"
    )
    correct = "Higher greenhouse gas concentrations trap additional outgoing longwave infrared radiation, shifting Earth's radiative equilibrium and forcing global mean temperatures to rise."
    options = [
        correct,
        "It causes sunlight to shine twenty-four hours a day across the entire globe.",
        "It stops the Earth from revolving around the Sun.",
        "It cools the planet by blocking visible light from reaching the ground."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Radiative forcing:\n"
        "Greenhouse gases absorb infrared radiation in specific spectral bands.\n"
        "Step 2: Enhanced greenhouse effect:\n"
        "Adding billions of tonnes of CO2 increases optical thickness in the infrared spectrum. Less heat escapes to space directly, elevating surface and tropospheric temperatures until a new, warmer radiative equilibrium is established."
    )
    return {
        "id": f"ns9_eas_34_{rng.randint(100000, 999999)}",
        "subskill": "34_enhanced_greenhouse_effect_and_global_warming_feedback",
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
        "hints": {
            "tier_1": "What does more CO2 do to outgoing heat radiation?",
            "tier_2": "It traps more outgoing infrared radiation, warming the surface.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["enhanced_greenhouse_effect_radiative_forcing"]
    }


def arch_35_ice_albedo_feedback_loop_positive_amplification(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In climate systems science, the melting of Arctic sea ice is a classic example of a **positive feedback loop**.\n\n"
        "How does the **ice-albedo feedback mechanism** operate to accelerate global warming?"
    )
    correct = "Warming temperatures melt bright reflective white ice (high albedo ~80%), exposing dark open ocean water (low albedo ~10%); the darker ocean absorbs more solar heat, causing further warming and even more ice to melt."
    options = [
        correct,
        "Melting ice releases giant icebergs that reflect more sunlight, rapidly freezing the entire planet.",
        "Melting ice makes the ocean water salty enough to turn into pure stone.",
        "Melting ice absorbs all greenhouse gases, completely ending global warming."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Albedo definition:\n"
        "Albedo is the fraction of solar radiation reflected by a surface (fresh snow ~0,8–0,9; open water ~0,06–0,10).\n"
        "Step 2: Positive feedback amplification:\n"
        "Warming → Ice melts → Surface darkens (albedo drops) → More solar energy absorbed → More warming. This self-reinforcing loop accelerates polar warming (Arctic amplification)."
    )
    return {
        "id": f"ns9_eas_35_{rng.randint(100000, 999999)}",
        "subskill": "35_ice_albedo_feedback_loop_positive_amplification",
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
        "hints": {
            "tier_1": "Does white ice or dark ocean water reflect more sunlight?",
            "tier_2": "White ice reflects ~80%; dark ocean absorbs ~90%, accelerating warming.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ice_albedo_positive_feedback_loop"]
    }


def arch_36_cloud_cover_feedback_negative_stabilizing_loop(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "While some feedbacks amplify warming, others act as **negative feedback loops** that promote planetary stability.\n\n"
        "How can increased cloud cover act as a negative (stabilizing) feedback loop in response to rising temperatures?"
    )
    correct = "Higher temperatures increase ocean evaporation, forming more dense, low-altitude white clouds that reflect incoming sunlight back into space, reducing solar heating and counteracting temperature rise."
    options = [
        correct,
        "Low clouds produce nuclear lasers that destroy all greenhouse molecules.",
        "Clouds absorb all oxygen from the atmosphere so water stops evaporating.",
        "Clouds cause the Earth to move physically farther away from the Sun."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Negative feedback definition:\n"
        "A feedback loop that dampens or counteracts an initial perturbation, driving the system back toward equilibrium.\n"
        "Step 2: Low cloud mechanism:\n"
        "Warming → More evaporation → More low stratocumulus clouds → Higher planetary albedo → More sunlight reflected to space → Cooling effect that stabilizes temperature."
    )
    return {
        "id": f"ns9_eas_36_{rng.randint(100000, 999999)}",
        "subskill": "36_cloud_cover_feedback_negative_stabilizing_loop",
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
        "hints": {
            "tier_1": "How do bright low clouds affect incoming sunlight?",
            "tier_2": "They reflect sunlight back to space, creating a cooling effect.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["cloud_albedo_negative_feedback_stabilization"]
    }


def arch_37_ocean_acidification_co2_dissolution_coral_bleaching(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The world's oceans (hydrosphere) absorb roughly 30% of anthropogenic CO2 emitted into the atmosphere, causing **ocean acidification**.\n\n"
        "What chemical reaction occurs in seawater, and why is ocean acidification devastating to marine organisms in the biosphere?"
    )
    correct = "Dissolved CO2 forms carbonic acid, releasing hydrogen ions that bind with carbonate ions (CO3²⁻), depriving corals, molluscs, and shell-building plankton of the building blocks needed to form calcium carbonate shells."
    options = [
        correct,
        "Dissolved CO2 turns ocean water into pure sulfuric acid that dissolves all metal ship hulls.",
        "Dissolved CO2 eliminates all gravity in the ocean so fish float into the air.",
        "Dissolved CO2 turns seawater into solid ice cubes across the tropics."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Chemical reactions:\n"
        "CO2 + H2O ⇌ H2CO3 ⇌ H⁺ + HCO3⁻.\n"
        "Excess H⁺ ions react with carbonate: H⁺ + CO3²⁻ ⇌ HCO3⁻ (bicarbonate).\n"
        "Step 2: Biological devastation:\n"
        "By depleting free carbonate ions, calcifying organisms (stony corals, clams, pteropods) cannot synthesize calcium carbonate (CaCO3). In acidic water, existing shells literally begin to dissolve."
    )
    return {
        "id": f"ns9_eas_37_{rng.randint(100000, 999999)}",
        "subskill": "37_ocean_acidification_co2_dissolution_coral_bleaching",
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
        "hints": {
            "tier_1": "What ions do shell-building marine creatures need that acidification depletes?",
            "tier_2": "Carbonate ions needed to make calcium carbonate shells.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ocean_acidification_carbonate_ion_depletion"]
    }


def arch_38_cryosphere_melting_sea_level_rise_coastal_flooding(rng: random.Random) -> Dict[str, Any]:
    contrib = rng.choice([
        ("thermal expansion of ocean water", "water naturally expands in volume as its temperature increases"),
        ("melting of land-based continental ice sheets (Greenland and Antarctica)", "adding massive volumes of new liquid water into the global ocean basin")
    ])
    name, mechanism = contrib
    prompt = (
        "Global sea levels are currently rising at an accelerating rate of ~3,7 mm per year.\n\n"
        f"How does **{name}** contribute to global sea level rise?"
    )
    correct = f"By {mechanism}."
    options = [
        correct,
        "By compressing the sea floor downward into the Earth's mantle.",
        "By evaporating all water into space so coasts get submerged by air.",
        "By causing the Moon to pull the oceans closer through gravitational waves."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Two primary drivers of sea level rise:\n"
        "1. Thermal expansion: Warming ocean water expands (~50% of observed rise).\n"
        "2. Land ice melt: Glaciers and ice sheets melting into the ocean (~50%).\n"
        f"Step 2: {name} mechanism:\n"
        f"{name} drives sea level rise by {mechanism}. Note: Melting floating sea ice does NOT raise sea levels (Archimedes' principle)."
    )
    return {
        "id": f"ns9_eas_38_{rng.randint(100000, 999999)}",
        "subskill": "38_cryosphere_melting_sea_level_rise_coastal_flooding",
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
        "hints": {
            "tier_1": f"How does {name} raise ocean levels?",
            "tier_2": f"It operates by {mechanism[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sea_level_rise_mechanisms_thermal_expansion_land_ice"]
    }


def arch_39_acid_mine_drainage_pyrite_oxidation_hydrosphere_hazard(rng: random.Random) -> Dict[str, Any]:
    mining_area = rng.choice(["the Witwatersrand gold basin in Gauteng", "the Mpumalanga Highveld coalfields"])
    prompt = (
        f"In South Africa, abandoned mining operations across {mining_area} produce **Acid Mine Drainage (AMD)**.\n\n"
        "What chemical reaction in exposed mine rocks generates AMD, and what makes it severely toxic to the hydrosphere and biosphere?"
    )
    correct = "Iron pyrite (FeS2) exposed to air and water oxidizes to produce highly corrosive sulfuric acid (H2SO4), which leaches toxic heavy metals (uranium, arsenic, lead) into freshwater aquifers and streams."
    options = [
        correct,
        "Gold nuggets react with oxygen to produce pure cyanide gas that evaporates.",
        "Underground coal seams catch fire and turn all river water into boiling oil.",
        "Miners dump household detergents into boreholes to wash underground tunnels."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Pyrite oxidation chemistry:\n"
        "4FeS2 + 15O2 + 14H2O → 4Fe(OH)3 + 8SO4²⁻ + 16H⁺ (assisted by Acidithiobacillus bacteria).\n"
        "Step 2: Ecological toxicity:\n"
        "The resulting drainage has a pH as low as 2–3. This extreme acidity dissolves toxic heavy metals (Al, As, Cd, Pb, U) out of host rocks, sterilizing aquatic food webs and contaminating drinking water supplies."
    )
    return {
        "id": f"ns9_eas_39_{rng.randint(100000, 999999)}",
        "subskill": "39_acid_mine_drainage_pyrite_oxidation_hydrosphere_hazard",
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
        "hints": {
            "tier_1": "What mineral oxidizes to form sulfuric acid in mine tailings?",
            "tier_2": "Iron pyrite (FeS2), producing sulfuric acid and leaching heavy metals.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["acid_mine_drainage_pyrite_oxidation"]
    }


def arch_40_wetlands_as_natural_hydrosphere_biosphere_biofilters(rng: random.Random) -> Dict[str, Any]:
    wetland = rng.choice(["the iSimangaliso Wetland Park in KwaZulu-Natal", "the Seekoeivlei Nature Reserve in the Free State", "an indigenous riverine wetland"])
    prompt = (
        f"Ecologists often refer to wetlands, such as **{wetland}**, as the 'kidneys of the Earth system'.\n\n"
        "What ecological services do wetland ecosystems perform at the intersection of the hydrosphere and biosphere?"
    )
    correct = "They absorb excess floodwaters like giant sponges to prevent erosion, trap suspended sediments, and utilize plant and microbial action to filter out agricultural toxins and excess nutrients."
    options = [
        correct,
        "They generate volcanic lava that fills in ocean trenches.",
        "They suck all oxygen out of the air to stop lightning storms.",
        "They turn freshwater rivers into salty oceans within twenty-four hours."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Hydrological regulation:\n"
        "Wetlands slow water velocity, attenuating peak flood waves and recharging groundwater aquifers during droughts.\n"
        "Step 2: Biogeochemical biofiltration:\n"
        "Dense emergent vegetation (reeds, sedges) traps silt. Microbial biofilms on root surfaces uptake excess nitrates and phosphates, preventing eutrophication downstream."
    )
    return {
        "id": f"ns9_eas_40_{rng.randint(100000, 999999)}",
        "subskill": "40_wetlands_as_natural_hydrosphere_biosphere_biofilters",
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
        "hints": {
            "tier_1": "Why are wetlands called 'kidneys of the landscape'?",
            "tier_2": "They filter toxins, trap sediment, and absorb floodwaters.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["wetlands_ecosystem_services_biofilters"]
    }


def arch_41_desertification_overgrazing_and_soil_degradation(rng: random.Random) -> Dict[str, Any]:
    region = rng.choice(["the semi-arid Karoo and communal rangelands", "the Sahel transition zone", "drylands in the Northern Cape"])
    prompt = (
        f"In semi-arid drylands such as {region}, unsustainable agricultural practices can lead to **desertification**.\n\n"
        "How does overgrazing by livestock trigger a devastating cascade across the biosphere and lithosphere?"
    )
    correct = "Livestock strip protective perennial vegetation and trample soil into hard crusts; without plant cover, rain cannot infiltrate, wind and water scour away topsoil, and productive land turns into barren desert."
    options = [
        correct,
        "Livestock breathe out radioactive gases that scorch the grass.",
        "Overgrazing causes earthquakes that shatter bedrock into fine dust.",
        "Livestock drink all underground magma, causing the land to sink."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Vegative stripping and compaction:\n"
        "Excess livestock consume palatable grass species down to the roots and their hooves compact the soil.\n"
        "Step 2: Soil crusting and erosion:\n"
        "Compacted soil loses permeability. Rain runs off instead of infiltrating, stripping topsoil via sheet erosion. The soil loses organic humus and seed banks, permanently transforming dryland savanna into barren desert."
    )
    return {
        "id": f"ns9_eas_41_{rng.randint(100000, 999999)}",
        "subskill": "41_desertification_overgrazing_and_soil_degradation",
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
        "hints": {
            "tier_1": "What happens when livestock eat all the grass and compact the soil?",
            "tier_2": "Rain cannot soak in, topsoil erodes, and land turns into desert.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["desertification_overgrazing_soil_erosion"]
    }


def arch_42_permafrost_thawing_methane_release_positive_feedback(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Across Arctic tundra regions, vast expanses of soil remain permanently frozen as **permafrost**.\n\n"
        "Why is the thawing of Arctic permafrost considered a critical global tipping point and positive feedback loop?"
    )
    correct = "Thawing permafrost allows anaerobic microbes to decompose centuries-old organic matter, releasing massive volumes of potent methane (CH4) and CO2 that accelerate global warming, triggering further thawing."
    options = [
        correct,
        "Thawing permafrost causes polar bears to turn into marine fish.",
        "Thawing permafrost turns all frozen soil into solid diamond crystals.",
        "Thawing permafrost makes Earth's magnetic poles rotate in reverse."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Carbon reservoir in permafrost:\n"
        "Permafrost contains ~1 500 billion tonnes of organic carbon—roughly twice the amount in the current atmosphere.\n"
        "Step 2: Positive feedback mechanism:\n"
        "Warming → Permafrost thaws → Microbes decompose un-thawed peat → Methane (CH4, 28× more potent greenhouse gas than CO2 over 100 years) is released → More atmospheric warming."
    )
    return {
        "id": f"ns9_eas_42_{rng.randint(100000, 999999)}",
        "subskill": "42_permafrost_thawing_methane_release_positive_feedback",
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
        "hints": {
            "tier_1": "What potent greenhouse gas is released when Arctic permafrost thaws?",
            "tier_2": "Methane (CH4) from anaerobic decomposition, accelerating warming.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["permafrost_thaw_methane_positive_feedback"]
    }


def arch_43_eutrophication_fertilizer_runoff_algal_blooms_hypoxia(rng: random.Random) -> Dict[str, Any]:
    lake = rng.choice(["the Hartbeespoort Dam in North West", "the Roodeplaat Dam near Pretoria", "a freshwater agricultural reservoir"])
    prompt = (
        f"Water bodies in South Africa, such as **{lake}**, suffer severely from **eutrophication**.\n\n"
        "What sequence of cross-sphere events leads from agricultural fertilizer application to massive fish kills in aquatic ecosystems?"
    )
    correct = "Excess nitrates and phosphates wash from agricultural fields into water (hydrosphere), sparking explosive algal blooms (biosphere); when the algae die, decomposing bacteria consume all dissolved oxygen (hypoxia), suffocating fish."
    options = [
        correct,
        "Fertilizers freeze water into solid ice that crushes fish beneath the surface.",
        "Algae produce radioactive lasers that blind all water organisms.",
        "Fertilizer turns water into gasoline that ignites whenever sunlight strikes it."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Nutrient enrichment:\n"
        "Agricultural fertilizer runoff (N and P) and untreated sewage enrich water.\n"
        "Step 2: Algal bloom & hypoxia:\n"
        "Phytoplankton multiply exponentially (algal bloom), blocking light. When nutrients deplete, the algae die. Aerobic bacteria decompose the dead biomass, consuming dissolved oxygen (BOD surges). Dissolved oxygen plummets (<2 mg/L), causing mass fish suffocation."
    )
    return {
        "id": f"ns9_eas_43_{rng.randint(100000, 999999)}",
        "subskill": "43_eutrophication_fertilizer_runoff_algal_blooms_hypoxia",
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
        "hints": {
            "tier_1": "What do decomposing bacteria consume after an algal bloom dies?",
            "tier_2": "Dissolved oxygen, causing hypoxia and fish kills.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["eutrophication_hypoxia_dead_zones"]
    }


def arch_44_plastic_pollution_marine_hydrosphere_food_web_crisis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Millions of tonnes of non-biodegradable synthetic plastics enter the global hydrosphere every year.\n\n"
        "How does plastic debris degrade in the oceans, and how does it threaten organisms across the marine biosphere?"
    )
    correct = "Ultraviolet solar radiation and wave mechanical action break plastics down into microscopic particles (microplastics); marine filter-feeders and fish ingest them, causing physical digestive blockages and biomagnifying toxic chemical pollutants up the food chain."
    options = [
        correct,
        "Plastic melts into natural organic sugar that feeds marine life safely.",
        "Plastic turns into pure oxygen bubbles that aerate the deep ocean trenches.",
        "Plastics dissolve completely into pure water within two weeks of entering the ocean."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Photodegradation & Fragmentation:\n"
        "UV radiation and wave action break polymers into microplastics (<5 mm).\n"
        "Step 2: Trophic biomagnification:\n"
        "Plastics adsorb persistent organic pollutants (POPs, PCBs, DDT). Zooplankton and fish mistake them for food. Ingestion causes starvation through pseudo-satiety, internal lacerations, and toxic chemical bioaccumulation reaching top marine predators and humans."
    )
    return {
        "id": f"ns9_eas_44_{rng.randint(100000, 999999)}",
        "subskill": "44_plastic_pollution_marine_hydrosphere_food_web_crisis",
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
        "hints": {
            "tier_1": "What do plastics break down into in the ocean?",
            "tier_2": "Microplastics that organisms ingest, blocking digestion and concentrating toxins.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["microplastics_marine_food_web_bioaccumulation"]
    }


def arch_45_biosphere_2_experiment_closed_system_challenges(rng: random.Random) -> Dict[str, Any]:
    location = "the Arizona desert in the United States"
    year = 1991
    prompt = (
        f"In {year}, eight human researchers entered **Biosphere 2**, a sealed 1,27-hectare airtight glass-and-steel facility in {location}, attempting to live for two years in a closed ecological system.\n\n"
        "What critical biogeochemical failure occurred inside Biosphere 2, demonstrating how exquisitely complex Earth's natural systems are?"
    )
    correct = "Atmospheric oxygen dropped dangerously from 21% to 14% while carbon dioxide skyrocketed, as soil microbes consumed oxygen faster than plants could produce it, and uncured concrete absorbed CO2."
    options = [
        correct,
        "The gravity inside the dome doubled, pinning all the researchers to the floor.",
        "All the researchers turned into plant roots due to excessive photosynthesis.",
        "The artificial atmosphere turned into liquid methane, freezing all tropical biomes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The Biosphere 2 experiment:\n"
        "Designed to test whether a closed artificial ecosystem could support human life for space colonization.\n"
        "Step 2: Biogeochemical decoupling:\n"
        "Rich compost-laden soils fueled rampant bacterial respiration, consuming oxygen far faster than greenhouse vegetation could replenish it. Furthermore, fresh alkaline concrete chemically reacted with CO2 (carbonation), preventing the normal carbon-oxygen balance and forcing outside oxygen injections to save the crew."
    )
    return {
        "id": f"ns9_eas_45_{rng.randint(100000, 999999)}",
        "subskill": "45_biosphere_2_experiment_closed_system_challenges",
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
        "hints": {
            "tier_1": "What gas plummeted dangerously inside Biosphere 2?",
            "tier_2": "Oxygen dropped from 21% to 14% due to microbial respiration.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["biosphere_2_closed_ecological_system_failure"]
    }


def arch_46_gaia_hypothesis_planetary_homeostasis_concept(rng: random.Random) -> Dict[str, Any]:
    pioneers = "James Lovelock and Lynn Margulis"
    prompt = (
        f"In the 1970s, scientists {pioneers} formulated the **Gaia hypothesis** regarding the Earth system.\n\n"
        "What core concept does the Gaia hypothesis propose regarding life and the abiotic environment?"
    )
    correct = "The biosphere and abiotic spheres (atmosphere, hydrosphere, lithosphere) interact as a single, self-regulating complex system that actively maintains planetary homeostasis and conditions suitable for life."
    options = [
        correct,
        "Earth is an artificial mechanical clock wound up by extraterrestrial astronauts every century.",
        "Living organisms have zero effect on the chemical composition of air, oceans, or rocks.",
        "The planet Earth is physically expanding into a gas giant like Jupiter."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Gaia hypothesis core thesis:\n"
        "Earth is not merely an inert rock with life clinging to its crust.\n"
        "Step 2: Self-regulating homeostasis:\n"
        "Biotic feedback mechanisms (e.g. marine algae producing dimethyl sulfide to seed reflective clouds, plants regulating atmospheric CO2 and O2, biological fixation regulating salinity) maintain stable global temperatures and chemical balances favorable for life."
    )
    return {
        "id": f"ns9_eas_46_{rng.randint(100000, 999999)}",
        "subskill": "46_gaia_hypothesis_planetary_homeostasis_concept",
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
        "hints": {
            "tier_1": "What does the Gaia hypothesis say about life regulating the planet?",
            "tier_2": "Life and the abiotic spheres form a self-regulating, homeostatic system.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["gaia_hypothesis_planetary_homeostasis"]
    }


def arch_47_planetary_boundaries_safe_operating_space_for_humanity(rng: random.Random) -> Dict[str, Any]:
    boundary = rng.choice([
        ("Climate change", "CO2 concentration exceeding 350 ppm and radiative forcing exceeding 1,0 W/m²"),
        ("Biosphere integrity (biodiversity extinction rate)", "species extinction rates exceeding 10 times the natural background rate"),
        ("Biogeochemical flows (nitrogen and phosphorus cycles)", "excessive industrial fertilizer application overloading water bodies")
    ])
    name, metric = boundary
    prompt = (
        "In 2009, Earth systems scientists introduced the **Planetary Boundaries framework**, defining nine environmental thresholds that delineate a 'safe operating space for humanity'.\n\n"
        f"Which threshold metric defines the planetary boundary for **{name}**?"
    )
    correct = f"It is defined by {metric}."
    options = [
        correct,
        "It is defined by the total number of mobile phone towers operating worldwide.",
        "It is defined by the depth of gold mines in South Africa.",
        "It is defined by the speed at which the Moon orbits around the Earth."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Planetary boundaries framework:\n"
        f"Identifies nine key Earth system processes.\n"
        f"Step 2: {name} threshold:\n"
        f"For {name}, the critical boundary threshold is {metric}. Crossing these tipping points risks non-linear, irreversible environmental transitions."
    )
    return {
        "id": f"ns9_eas_47_{rng.randint(100000, 999999)}",
        "subskill": "47_planetary_boundaries_safe_operating_space_for_humanity",
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
        "hints": {
            "tier_1": f"What metric measures the boundary for {name}?",
            "tier_2": f"It is defined by {metric[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["planetary_boundaries_safe_operating_space"]
    }


def arch_48_eduard_suess_and_vladimir_vernadsky_biosphere_pioneers(rng: random.Random) -> Dict[str, Any]:
    scientist, year, contribution = rng.choice([
        ("Austrian geologist Eduard Suess", 1875, "first coined the term 'biosphere' to describe the zone on Earth's surface where life dwells"),
        ("Russian mineralogist Vladimir Vernadsky", 1926, "published 'The Biosphere', revolutionizing systems science by showing that life is a powerful geological force driving global chemistry")
    ])
    prompt = (
        f"Historical development of Earth systems science was shaped by pioneering thinkers. In {year}, **{scientist}** made a landmark contribution.\n\n"
        f"What was {scientist}'s fundamental scientific contribution?"
    )
    correct = f"He {contribution}."
    options = [
        correct,
        "He invented the first nuclear submarine to navigate through solid bedrock.",
        "He claimed that the Earth is hollow and filled with giant dinosaurs.",
        "He proved that trees do not require water to perform photosynthesis."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Historical milestone:\n"
        f"In {year}, {scientist} advanced our conceptualization of the biosphere.\n"
        f"Step 2: Core legacy:\n"
        f"He {contribution}."
    )
    return {
        "id": f"ns9_eas_48_{rng.randint(100000, 999999)}",
        "subskill": "48_eduard_suess_and_vladimir_vernadsky_biosphere_pioneers",
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
        "hints": {
            "tier_1": f"What did {scientist} pioneer?",
            "tier_2": f"He {contribution[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["biosphere_historical_pioneers_suess_vernadsky"]
    }


def arch_49_remote_sensing_satellites_monitoring_earth_system(rng: random.Random) -> Dict[str, Any]:
    sensor, application = rng.choice([
        ("Infrared radiometers (e.g. MODIS)", "measuring sea surface temperatures and detecting forest wildfires across biomes"),
        ("Synthetic Aperture Radar (SAR)", "penetrating cloud cover to map ice sheet elevation loss and tectonic fault slip"),
        ("Multi-spectral optical imagers (e.g. Landsat/Sentinel)", "calculating Normalized Difference Vegetation Index (NDVI) to track deforestation and crop health")
    ])
    prompt = (
        "Modern Earth systems scientists monitor dynamic interactions across all four spheres using orbital **remote sensing satellites**.\n\n"
        f"How does **{sensor}** specifically advance our observation of the Earth system?"
    )
    correct = f"By {application}."
    options = [
        correct,
        "By firing laser beams to drill water wells in arid deserts.",
        "By vacuuming plastic out of the middle of the Pacific Ocean.",
        "By broadcasting radio music to communicate with subterranean earthworms."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Remote sensing methodology:\n"
        f"Satellites capture reflected and emitted electromagnetic radiation across specific spectral bands.\n"
        f"Step 2: {sensor} role:\n"
        f"{sensor} monitors Earth processes by {application}."
    )
    return {
        "id": f"ns9_eas_49_{rng.randint(100000, 999999)}",
        "subskill": "49_remote_sensing_satellites_monitoring_earth_system",
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
        "hints": {
            "tier_1": f"How is {sensor} used in Earth observation?",
            "tier_2": f"It operates by {application[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["satellite_remote_sensing_earth_monitoring"]
    }


def arch_50_earth_as_a_system_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    phenomenon, primary_sphere, target_sphere, mechanism = rng.choice([
        ("Volcanic winter cooling", "Lithosphere (volcano)", "Atmosphere", "sulfate aerosols reflecting incoming solar radiation"),
        ("Karst cave dissolution", "Atmosphere & Hydrosphere (acid rain/groundwater)", "Lithosphere", "carbonic acid chemically dissolving limestone bedrock"),
        ("Eutrophic hypoxia", "Lithosphere & Biosphere (fertilizer runoff)", "Hydrosphere", "bacterial decomposition of algal blooms consuming dissolved oxygen"),
        ("Ice-albedo amplification", "Atmosphere (warming air)", "Hydrosphere (cryosphere ice)", "melting reflective ice exposing dark heat-absorbing ocean water")
    ])
    prompt = (
        f"**Comprehensive Earth Systems Diagnostic:**\n"
        f"Scientists analyzing global environmental cascades observe **{phenomenon}**.\n\n"
        f"Which cross-sphere interaction and underlying physical mechanism drives {phenomenon}?"
    )
    correct = f"Originates from {primary_sphere} and affects {target_sphere} through {mechanism}."
    options = [
        correct,
        "Originates from outer space aliens firing gravitational disruptors at Earth's core.",
        "Originates from human smartphones broadcasting excessive microwave energy.",
        "Originates from nuclear decay occurring exclusively on the surface of the Moon."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Diagnostic phenomenon: {phenomenon}.\n"
        f"Step 2: Sphere interaction pathways:\n"
        f"The primary driver connects {primary_sphere} to {target_sphere} via {mechanism}."
    )
    return {
        "id": f"ns9_eas_50_{rng.randint(100000, 999999)}",
        "subskill": "50_earth_as_a_system_comprehensive_diagnostic_autopsy",
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
        "hints": {
            "tier_1": f"Which spheres are involved in {phenomenon}?",
            "tier_2": f"It connects {primary_sphere} to {target_sphere} through {mechanism[:30]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["earth_systems_diagnostic_autopsy"]
    }


BUILDERS_26_50 = {
    "26_volcanic_eruption_lithosphere_to_atmosphere_cooling": arch_26_volcanic_eruption_lithosphere_to_atmosphere_cooling,
    "27_volcanic_eruption_hydrosphere_acid_rain_cascade": arch_27_volcanic_eruption_hydrosphere_acid_rain_cascade,
    "28_volcanic_eruption_biosphere_habitat_destruction_and_soil": arch_28_volcanic_eruption_biosphere_habitat_destruction_and_soil,
    "29_subsea_earthquake_lithosphere_tsunami_hydrosphere_cascade": arch_29_subsea_earthquake_lithosphere_tsunami_hydrosphere_cascade,
    "30_tropical_cyclone_hydrosphere_atmosphere_biosphere_impact": arch_30_tropical_cyclone_hydrosphere_atmosphere_biosphere_impact,
    "31_deforestation_biosphere_to_lithosphere_erosion_cascade": arch_31_deforestation_biosphere_to_lithosphere_erosion_cascade,
    "32_deforestation_impact_on_hydrological_cycle_drought": arch_32_deforestation_impact_on_hydrological_cycle_drought,
    "33_anthropogenic_fossil_fuel_combustion_carbon_flux": arch_33_anthropogenic_fossil_fuel_combustion_carbon_flux,
    "34_enhanced_greenhouse_effect_and_global_warming_feedback": arch_34_enhanced_greenhouse_effect_and_global_warming_feedback,
    "35_ice_albedo_feedback_loop_positive_amplification": arch_35_ice_albedo_feedback_loop_positive_amplification,
    "36_cloud_cover_feedback_negative_stabilizing_loop": arch_36_cloud_cover_feedback_negative_stabilizing_loop,
    "37_ocean_acidification_co2_dissolution_coral_bleaching": arch_37_ocean_acidification_co2_dissolution_coral_bleaching,
    "38_cryosphere_melting_sea_level_rise_coastal_flooding": arch_38_cryosphere_melting_sea_level_rise_coastal_flooding,
    "39_acid_mine_drainage_pyrite_oxidation_hydrosphere_hazard": arch_39_acid_mine_drainage_pyrite_oxidation_hydrosphere_hazard,
    "40_wetlands_as_natural_hydrosphere_biosphere_biofilters": arch_40_wetlands_as_natural_hydrosphere_biosphere_biofilters,
    "41_desertification_overgrazing_and_soil_degradation": arch_41_desertification_overgrazing_and_soil_degradation,
    "42_permafrost_thawing_methane_release_positive_feedback": arch_42_permafrost_thawing_methane_release_positive_feedback,
    "43_eutrophication_fertilizer_runoff_algal_blooms_hypoxia": arch_43_eutrophication_fertilizer_runoff_algal_blooms_hypoxia,
    "44_plastic_pollution_marine_hydrosphere_food_web_crisis": arch_44_plastic_pollution_marine_hydrosphere_food_web_crisis,
    "45_biosphere_2_experiment_closed_system_challenges": arch_45_biosphere_2_experiment_closed_system_challenges,
    "46_gaia_hypothesis_planetary_homeostasis_concept": arch_46_gaia_hypothesis_planetary_homeostasis_concept,
    "47_planetary_boundaries_safe_operating_space_for_humanity": arch_47_planetary_boundaries_safe_operating_space_for_humanity,
    "48_eduard_suess_and_vladimir_vernadsky_biosphere_pioneers": arch_48_eduard_suess_and_vladimir_vernadsky_biosphere_pioneers,
    "49_remote_sensing_satellites_monitoring_earth_system": arch_49_remote_sensing_satellites_monitoring_earth_system,
    "50_earth_as_a_system_comprehensive_diagnostic_autopsy": arch_50_earth_as_a_system_comprehensive_diagnostic_autopsy,
}
