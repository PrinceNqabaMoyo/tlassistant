"""Grade 9 Natural Sciences - The Atmosphere: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 4/04. The atmosphere.md
Focus:
Greenhouse gases (water vapor, CO2 residence time, methane sources, nitrous oxide), Enhanced greenhouse effect & global warming,
Fossil fuel carbon cycle imbalance, Deforestation, Keeling curve, Ocean acidification chemistry & marine calcifiers,
Polar ice melting & sea level rise physics, Positive feedback loops (ice-albedo, permafrost thaw), Southern African climate impacts
(droughts, coastal storm surges), Eskom Highveld emissions hotspot, Carbon footprint, Renewable energy transition (solar & wind),
Energy efficiency, Carbon capture, Spekboom reforestation, Paris Agreement (1,5 °C target), Air Quality Index (PM2.5/PM10),
Photochemical smog (tropospheric ozone), Acid rain chemistry (SO2/NOx), Comprehensive Diagnostic Autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_water_vapor_most_abundant_natural_greenhouse_gas(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "While political discussions focus on carbon dioxide, **water vapor (H2O)** is mathematically the most abundant greenhouse gas in Earth's atmosphere.\n\n"
        "What atmospheric characteristics distinguish water vapor from non-condensable greenhouse gases like CO2?"
    )
    correct = "Water vapor accounts for ~60% of natural greenhouse warming, but has a very short atmospheric residence time (~9 days) controlled by temperature and the hydrological cycle, acting as an amplifying feedback rather than an initial climate forcing."
    options = [
        correct,
        "Water vapor stays in the atmosphere for ten million years without ever raining.",
        "Water vapor is an artificial chemical manufactured exclusively inside nuclear reactors.",
        "Water vapor freezes the planet by reflecting 100% of all solar energy into space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Radiative contribution of water vapor:\n"
        "H2O vapor contributes ~60% of natural atmospheric infrared absorption.\n"
        "Step 2: Clausius-Clapeyron relation:\n"
        "Air's water-holding capacity increases ~7% per 1 °C warming. When CO2 warms the planet, more water evaporates, doubling the initial warming (positive water vapor feedback)."
    )
    return {
        "id": f"ns9_atm_26_{rng.randint(100000, 999999)}",
        "subskill": "26_water_vapor_most_abundant_natural_greenhouse_gas",
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
            "tier_1": "Does water vapor stay in the air for centuries or just days?",
            "tier_2": "Short residence time (~9 days), acting as a natural temperature-driven feedback.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["water_vapor_greenhouse_feedback"]
    }


def arch_27_carbon_dioxide_atmospheric_residence_time_and_sources(rng: random.Random) -> Dict[str, Any]:
    curr_ppm = rng.choice([418, 420, 422])
    pre_ind = 280
    prompt = (
        f"Atmospheric carbon dioxide (CO2) concentrations have surged from **{pre_ind} ppm** in pre-industrial times to over **{curr_ppm} ppm** today.\n\n"
        "Why is carbon dioxide considered the primary driver of long-term anthropogenic climate change despite being less abundant than water vapor?"
    )
    correct = "CO2 has an exceptionally long atmospheric residence time (hundreds to thousands of years), accumulating steadily and setting the baseline global temperature that controls how much water vapor the atmosphere can hold."
    options = [
        correct,
        "CO2 is radioactive and explodes when exposed to atmospheric oxygen.",
        "CO2 falls out of the air as solid dry ice every single afternoon.",
        "CO2 is completely non-existent in nature and was invented in 1990."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric lifetime of CO2:\n"
        "Unlike water vapor which precipitates out in days, a pulse of emitted CO2 equilibrates between atmosphere, ocean mixed layer, and terrestrial biosphere over centuries; ~20% remains airborne for millennia.\n"
        "Step 2: Control knob of climate:\n"
        "Non-condensable CO2 acts as the planetary thermal thermostat."
    )
    return {
        "id": f"ns9_atm_27_{rng.randint(100000, 999999)}",
        "subskill": "27_carbon_dioxide_atmospheric_residence_time_and_sources",
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
            "tier_1": "How long does carbon dioxide persist in the atmosphere?",
            "tier_2": "Centuries to millennia, accumulating steadily to drive warming.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["co2_atmospheric_residence_time"]
    }


def arch_28_methane_potent_short_lived_greenhouse_gas_sources(rng: random.Random) -> Dict[str, Any]:
    gwp_factor = rng.choice([28, 30, 32])
    prompt = (
        f"**Methane (CH4)** is a potent greenhouse gas with a 100-year Global Warming Potential (GWP) roughly **{gwp_factor} times greater** than that of carbon dioxide.\n\n"
        "What are the major anthropogenic and agricultural sources of methane emissions into the atmosphere?"
    )
    correct = "Enteric fermentation in ruminant livestock (cattle belching), anaerobic decomposition in flooded rice paddies, fugitive leakage from coal mines and natural gas pipelines, and organic decay in municipal landfills."
    options = [
        correct,
        "Solar photovoltaic panels absorbing sunlight on house rooftops.",
        "Wind turbines rotating their blades in coastal winds.",
        "Electric vehicles charging their lithium batteries at night."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Global Warming Potential of CH4:\n"
        f"Over 100 years, GWP = ~{gwp_factor} (over 20 years, GWP > 80).\n"
        "Step 2: Methanogenesis sources:\n"
        "Methanogenic archaea produce CH4 in anoxic environments: ruminant guts, wetland soils, flooded rice paddies, municipal waste dumps, and coal seam venting."
    )
    return {
        "id": f"ns9_atm_28_{rng.randint(100000, 999999)}",
        "subskill": "28_methane_potent_short_lived_greenhouse_gas_sources",
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
            "tier_1": "What agricultural and waste processes release methane gas?",
            "tier_2": "Cattle enteric fermentation, flooded rice paddies, coal mines, and landfills.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["methane_sources_global_warming_potential"]
    }


def arch_29_nitrous_oxide_agricultural_fertilizers_and_emissions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "**Nitrous oxide (N2O)**, commonly known as laughing gas, is an extremely potent greenhouse gas with a GWP nearly 273 times that of CO2.\n\n"
        "What human activity is the primary contributor to rising atmospheric nitrous oxide emissions?"
    )
    correct = "Excessive application of synthetic nitrogen chemical fertilizers and livestock manure to agricultural soils, where soil bacteria convert nitrogen compounds to N2O gas through microbial nitrification and denitrification."
    options = [
        correct,
        "Purifying tap water with chlorine tablets in municipal water treatment plants.",
        "Manufacturing glass bottles from molten quartz sand.",
        "Constructing wooden furniture from pine timber."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Soil microbial nitrogen cycle:\n"
        "Nitrogen fertilizers (NH4NO3, urea) increase soil reactive nitrogen.\n"
        "Step 2: Denitrification emissions:\n"
        "Soil bacteria in warm, wet soils convert nitrate into N2O: NO3⁻ → NO2⁻ → NO → N2O → N2.\n"
        "N2O persists in the atmosphere for ~114 years and also contributes to stratospheric ozone depletion."
    )
    return {
        "id": f"ns9_atm_29_{rng.randint(100000, 999999)}",
        "subskill": "29_nitrous_oxide_agricultural_fertilizers_and_emissions",
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
            "tier_1": "What farming input releases nitrous oxide into the atmosphere?",
            "tier_2": "Synthetic nitrogen fertilizers and manure broken down by soil bacteria.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["nitrous_oxide_fertilizer_denitrification"]
    }


def arch_30_enhanced_greenhouse_effect_anthropogenic_global_warming(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In climate science, it is vital to distinguish between the **natural greenhouse effect** and the **enhanced greenhouse effect**.\n\n"
        "What is the precise scientific difference between these two phenomena?"
    )
    correct = "The natural greenhouse effect is the life-sustaining baseline warming (+33 °C) caused by natural trace gases; the enhanced greenhouse effect is the additional, unnatural warming caused by human activities elevating greenhouse gas concentrations beyond natural levels."
    options = [
        correct,
        "The natural effect warms the Earth, while the enhanced effect causes the Earth to enter an Ice Age.",
        "The natural effect occurs only on Mars, while the enhanced effect occurs only on Venus.",
        "Both terms are 100% identical with zero distinction in science."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Natural greenhouse effect:\n"
        "Equilibrium warming maintaining Earth at ~15 °C (preventing a frozen -18 °C globe).\n"
        "Step 2: Enhanced (anthropogenic) effect:\n"
        "Industrial emissions of CO2, CH4, and N2O increase the optical thickness of the atmosphere in infrared absorption bands, trapping excess outgoing heat and causing global warming."
    )
    return {
        "id": f"ns9_atm_30_{rng.randint(100000, 999999)}",
        "subskill": "30_enhanced_greenhouse_effect_anthropogenic_global_warming",
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
            "tier_1": "Which effect is natural for life and which is human-caused global warming?",
            "tier_2": "Natural = vital baseline (+33 °C); Enhanced = extra warming from human emissions.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["natural_vs_enhanced_greenhouse_effect"]
    }


def arch_31_fossil_fuel_combustion_carbon_cycle_imbalance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Fossil fuels (coal, petroleum, natural gas) represent carbon that was captured by ancient organisms and sequestered deep underground over hundreds of millions of years.\n\n"
        "How has industrial combustion of fossil fuels created a profound imbalance in the global **carbon cycle**?"
    )
    correct = "Humans are burning and releasing ancient geological carbon back into the atmosphere in just a few decades—at rates hundreds of times faster than natural geological carbon sinks (sedimentation and rock weathering) can absorb it."
    options = [
        correct,
        "Fossil fuel combustion turns carbon into liquid gold that sinks into the mantle.",
        "Burning fossil fuels removes all carbon dioxide from the air, starving plants of food.",
        "Combustion freezes carbon atoms into indestructible diamond crystals that float in clouds."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Geological carbon reservoir:\n"
        "Slow carbon cycle stores carbon in coal, oil, and limestone over ~100–300 million years.\n"
        "Step 2: Anthropogenic rate mismatch:\n"
        "Fossil fuel combustion releases ~37 billion tonnes of CO2 annually. Natural sinks (oceans, terrestrial plants) only reabsorb ~55%, leaving an annual airborne surplus of ~45% accumulating in the atmosphere."
    )
    return {
        "id": f"ns9_atm_31_{rng.randint(100000, 999999)}",
        "subskill": "31_fossil_fuel_combustion_carbon_cycle_imbalance",
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
            "tier_1": "How does the rate of fossil fuel burning compare to natural carbon sequestration?",
            "tier_2": "Humans release geological carbon hundreds of times faster than sinks can absorb it.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["fossil_fuel_carbon_cycle_flux_imbalance"]
    }


def arch_32_deforestation_loss_of_photosynthetic_carbon_sinks(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Deforestation—the large-scale clearing and burning of forests for agriculture and timber—is responsible for ~10% to 15% of global greenhouse emissions.\n\n"
        "What two-fold impact does deforestation have on atmospheric carbon dioxide concentrations?"
    )
    correct = "Combustion and decomposition of cleared trees immediately release stored biomass carbon as CO2 gas into the atmosphere, while simultaneously destroying living tree canopies that would otherwise absorb CO2 through ongoing photosynthesis."
    options = [
        correct,
        "Deforestation causes tree roots to turn into coal beneath the soil.",
        "Clearing forests increases rainfall and cools the global atmosphere by 10 °C.",
        "Cutting down trees prevents oxygen from leaking out of the Earth into space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Direct emissions source:\n"
        "Biomass contains ~50% carbon by dry weight. Felling and burning oxidizes cellulose/lignin: (C6H10O5)n + O2 → CO2 + H2O.\n"
        "Step 2: Sink destruction:\n"
        "Forests act as active carbon sinks (photosynthetic drawdown: 6CO2 + 6H2O → C6H12O6 + 6O2). Destroying forests permanently impairs biospheric sequestration."
    )
    return {
        "id": f"ns9_atm_32_{rng.randint(100000, 999999)}",
        "subskill": "32_deforestation_loss_of_photosynthetic_carbon_sinks",
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
            "tier_1": "What happens to stored carbon when trees burn, and what happens to future CO2 absorption?",
            "tier_2": "Releases stored carbon immediately and eliminates future photosynthetic drawdown.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["deforestation_carbon_source_and_sink_loss"]
    }


def arch_33_keeling_curve_exponential_co2_rise_since_industrial_era(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Initiated in 1958 at Mauna Loa Observatory in Hawaii, the famous **Keeling Curve** provides the gold standard observational record of atmospheric CO2.\n\n"
        "What two distinct patterns characterize the empirical data of the Keeling Curve?"
    )
    correct = "A steady, monotonic long-term upward rise driven by fossil fuel emissions, superimposed with an annual seasonal sawtooth oscillation caused by the growth and decay of Northern Hemisphere land vegetation."
    options = [
        correct,
        "A flat horizontal line proving that atmospheric CO2 has remained exactly 100 ppm forever.",
        "A random chaotic scribble caused by volcanic ash interfering with sensors.",
        "A steep downward curve showing that CO2 is disappearing from the planet."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Long-term trend:\n"
        "Rising from ~315 ppm in 1958 to >420 ppm today due to cumulative anthropogenic fossil emissions.\n"
        "Step 2: Seasonal breathing of the biosphere:\n"
        "Northern Hemisphere spring/summer photosynthesizes massively (landmass bias), drawing CO2 down ~6 ppm. In autumn/winter, microbial respiration and leaf decay return CO2, creating the annual sawtooth oscillation."
    )
    return {
        "id": f"ns9_atm_33_{rng.randint(100000, 999999)}",
        "subskill": "33_keeling_curve_exponential_co2_rise_since_industrial_era",
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
            "tier_1": "What two trends appear on the Keeling Curve (long-term rise + seasonal zigzag)?",
            "tier_2": "Long-term upward trend from fossil fuels + annual sawtooth from seasonal vegetation.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["keeling_curve_trend_and_seasonal_cycle"]
    }


def arch_34_ocean_acidification_carbonic_acid_and_marine_calcifiers(rng: random.Random) -> Dict[str, Any]:
    organism = rng.choice(["coral reefs (calcium carbonate skeletons)", "planktonic pteropods ('sea butterflies') and shellfish (mussels, oysters)"])
    prompt = (
        f"Approximately 30% of anthropogenic CO2 emissions are absorbed by oceans, causing **ocean acidification**.\n\n"
        f"What chemical reaction occurs when CO2 dissolves in seawater, and how does it harm **{organism}**?"
    )
    correct = "CO2 reacts with water to form carbonic acid (CO2 + H2O → H2CO3), releasing hydrogen ions (H+) that lower ocean pH and consume carbonate ions (CO3²⁻), making it difficult or impossible for marine organisms to build and maintain calcium carbonate (CaCO3) shells."
    options = [
        correct,
        "CO2 turns seawater into solid ice cubes that crush swimming marine animals.",
        "CO2 evaporates all ocean water into outer space, leaving dry salt beds.",
        "CO2 makes coral reefs grow ten times faster by turning into metallic iron."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Aqueous carbonate chemistry:\n"
        "CO2(aq) + H2O ⇌ H2CO3 ⇌ H⁺ + HCO3⁻.\n"
        "Excess H⁺ ions react with dissolved carbonate: H⁺ + CO3²⁻ ⇌ HCO3⁻.\n"
        "Step 2: Calcification saturation state:\n"
        "Depletion of free CO3²⁻ drops the calcium carbonate saturation state (Ω < 1), causing existing aragonite and calcite shells of marine calcifiers to dissolve."
    )
    return {
        "id": f"ns9_atm_34_{rng.randint(100000, 999999)}",
        "subskill": "34_ocean_acidification_carbonic_acid_and_marine_calcifiers",
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
            "tier_1": "What acid forms when CO2 dissolves in water and what does it do to shells?",
            "tier_2": "Forms carbonic acid, lowering pH and depleting carbonate ions needed for shells.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ocean_acidification_carbonate_depletion"]
    }


def arch_35_polar_ice_sheet_melting_and_sea_level_rise_physics(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Global warming causes sea level rise through two primary physical mechanisms.\n\n"
        "What are the two main drivers of global sea level rise, and why does melting Arctic sea ice NOT raise sea levels significantly?"
    )
    correct = "Thermal expansion of warming ocean water and the melting of land-based glaciers and ice sheets (Greenland and Antarctica); floating sea ice is already displacing its own mass in water (Archimedes' principle), so its melting does not add new volume."
    options = [
        correct,
        "Underwater volcanoes pushing the ocean floor up, and human ships taking up too much room.",
        "Rainfall falling from outer space into the Atlantic Ocean.",
        "Melting sea ice adds 100 meters of water because ice is denser than liquid ocean water."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Thermal expansion (steric sea level rise):\n"
        "As ocean water absorbs heat, its density decreases and volume expands (~40% of observed sea level rise).\n"
        "Step 2: Land ice vs Sea ice (eustatic rise):\n"
        "Melting land-based ice sheets (Antarctica, Greenland) transfers new mass to oceans. Floating sea ice already displaces a volume of water equal to its mass (Archimedes' principle); when it melts, the volume of resulting meltwater exactly equals the displaced volume."
    )
    return {
        "id": f"ns9_atm_35_{rng.randint(100000, 999999)}",
        "subskill": "35_polar_ice_sheet_melting_and_sea_level_rise_physics",
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
            "tier_1": "What two factors raise sea levels and why doesn't floating sea ice add volume?",
            "tier_2": "Thermal expansion + land ice melting; floating ice already displaces its mass.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sea_level_rise_thermal_expansion_land_ice"]
    }


def arch_36_positive_climate_feedback_ice_albedo_feedback_loop(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In climate dynamics, the **ice-albedo feedback loop** is a prime example of a self-reinforcing positive feedback.\n\n"
        "How does the reduction of polar sea ice accelerate planetary warming?"
    )
    correct = "Rising temperatures melt highly reflective white ice (albedo ~0,85), exposing dark open ocean water (albedo ~0,08); the dark water absorbs significantly more solar radiation as heat, which warms the ocean and melts even more ice in a continuous loop."
    options = [
        correct,
        "Melting ice releases frozen volcanic steam that extinguishes the Sun's rays.",
        "Melting ice freezes ocean water into dry ice, cooling the planet down instantly.",
        "Open ocean water reflects 100% of sunlight back into space, reversing global warming."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Initial perturbation:\n"
        "Atmospheric warming causes polar sea ice retreat.\n"
        "Step 2: Albedo alteration and feedback loop:\n"
        "Bright ice (α ≈ 0,85) reflects solar insolation. Dark seawater (α ≈ 0,08) absorbs ~92% of insolation. Higher ocean heat content accelerates basal ice melt, amplifying initial warming (positive feedback loop)."
    )
    return {
        "id": f"ns9_atm_36_{rng.randint(100000, 999999)}",
        "subskill": "36_positive_climate_feedback_ice_albedo_feedback_loop",
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
            "tier_1": "What happens when bright ice is replaced by dark ocean water?",
            "tier_2": "Dark ocean absorbs more solar heat (lower albedo), accelerating further ice melt.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ice_albedo_positive_feedback_loop"]
    }


def arch_37_positive_climate_feedback_permafrost_thaw_methane_release(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Across high-latitude Arctic and Siberian tundras, vast expanses of **permafrost** (permanently frozen soil) are thawing as global temperatures rise.\n\n"
        "Why is permafrost thaw considered a dangerous 'tipping point' positive feedback in the climate system?"
    )
    correct = "Permafrost holds massive deposits of ancient frozen organic matter; when it thaws, anaerobic microbes decompose the organic carbon, venting vast pulses of methane (CH4) and CO2 into the atmosphere, causing further warming and more thawing."
    options = [
        correct,
        "Thawing permafrost turns into solid rock that covers the entire Northern Hemisphere.",
        "Thawing permafrost absorbs all atmospheric oxygen, causing birds to stop flying.",
        "Thawed permafrost freezes atmospheric carbon dioxide into diamond mountain peaks."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Carbon inventory in permafrost:\n"
        "Global permafrost soils contain ~1 400 to 1 600 billion tonnes of carbon—roughly double the carbon currently in the atmosphere.\n"
        "Step 2: Thaw and feedback:\n"
        "Deep thaw allows microbial respiration. Waterlogged collapse features (thermokarst lakes) foster anaerobic methanogenesis, releasing CH4 and reinforcing global warming independently of direct human emissions."
    )
    return {
        "id": f"ns9_atm_37_{rng.randint(100000, 999999)}",
        "subskill": "37_positive_climate_feedback_permafrost_thaw_methane_release",
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
            "tier_1": "What gas do microbes release when frozen tundra soil thaws?",
            "tier_2": "Anaerobic decay releases methane and CO2, amplifying global warming.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["permafrost_thaw_methane_feedback"]
    }


def arch_38_droughts_and_heatwaves_southern_african_climate_impacts(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Climate modeling demonstrates that Southern Africa is a climate change hotspot, warming at approximately **twice the global average rate**.\n\n"
        "What regional climate impacts are already impacting South Africa's agriculture, water security, and biomes?"
    )
    correct = "Increasing frequency and severity of multi-year droughts (e.g. Cape Town 'Day Zero' and Eastern Cape droughts), heatwaves, delayed summer rains, and reduced river runoff stressing commercial crop yields and livestock farming."
    options = [
        correct,
        "Widespread glaciation with permanent snowdrifts covering Durban and Pretoria.",
        "Continuous 24-hour tropical rainstorms that flood the entire Kalahari Desert into a sea.",
        "Average temperatures dropping by 15 °C across all nine provinces."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Regional warming amplification:\n"
        "Interior subtropical continental Southern Africa warms ~1,5–2× faster than global mean.\n"
        "Step 2: Hydroclimatic consequences:\n"
        "Poleward expansion of subtropical high-pressure belts shifts mid-latitude storm tracks south. High temperatures increase potential evapotranspiration, intensifying soil moisture deficits, crop failures, and municipal water crises."
    )
    return {
        "id": f"ns9_atm_38_{rng.randint(100000, 999999)}",
        "subskill": "38_droughts_and_heatwaves_southern_african_climate_impacts",
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
            "tier_1": "What happens to droughts and water security in Southern Africa under climate change?",
            "tier_2": "More frequent and severe droughts, heatwaves, and water supply shortages.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["southern_africa_climate_change_droughts"]
    }


def arch_39_coastal_erosion_and_storm_surges_cape_and_durban(rng: random.Random) -> Dict[str, Any]:
    city = rng.choice(["Durban and the KwaZulu-Natal coastline", "Cape Town and False Bay coastal settlements"])
    prompt = (
        f"Along South Africa's vulnerable coastlines, such as around **{city}**, sea level rise interacts with severe marine storms.\n\n"
        "What coastal hazards are intensified when rising sea levels coincide with spring high tides and severe storm surges?"
    )
    correct = "Severe beach and dune erosion, undermining of coastal roads, railways, and seaside homes, saltwater intrusion into coastal freshwater aquifers, and destructive flooding of low-lying estuarine settlements."
    options = [
        correct,
        "Beaches expand by ten kilometers into the ocean, creating new farmland.",
        "Ocean water turns into fresh tap water that can be bottled and sold.",
        "Coral reefs grow into towering mountain ranges that block all ocean waves."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Coastal dynamics:\n"
        "Rising mean sea level elevates the baseline for storm wave action.\n"
        "Step 2: Storm surge impacts:\n"
        "Cut-off lows and intense cold fronts generate low barometric pressure and onshore gale-force winds. The resulting storm surge overtops coastal dunes, battering municipal infrastructure (e.g. railway lines and seawalls) and salinizing coastal aquifers."
    )
    return {
        "id": f"ns9_atm_39_{rng.randint(100000, 999999)}",
        "subskill": "39_coastal_erosion_and_storm_surges_cape_and_durban",
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
            "tier_1": "What happens to coastal roads and dunes during storm surges on rising seas?",
            "tier_2": "Beach erosion, infrastructure damage, and saltwater flooding of low-lying areas.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["coastal_erosion_storm_surge_sea_level"]
    }


def arch_40_eskom_coal_fired_power_stations_highveld_emissions_hotspot(rng: random.Random) -> Dict[str, Any]:
    station = rng.choice(["Kendal", "Kusile", "Medupi", "Matla", "Duvha"])
    prompt = (
        f"South Africa's **Mpumalanga Highveld** (home to massive Eskom coal-fired power stations like {station}) is globally documented as an air pollution hotspot.\n\n"
        "What major atmospheric pollutants are emitted in vast quantities from coal combustion at these stations, and what health risks do they cause?"
    )
    correct = "Sulfur dioxide (SO2), nitrogen oxides (NOx), fine fly-ash particulate matter (PM2.5), and carbon dioxide (CO2); causing severe asthma, chronic bronchitis, and premature cardiovascular deaths in local communities."
    options = [
        correct,
        "Pure medical oxygen and drinking water vapor that improves lung health in children.",
        "Harmless liquid nitrogen that cleans the atmosphere of all vehicle dust.",
        "Scented floral perfume that neutralizes all industrial bad odors."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Emissions from coal power stations:\n"
        "Combustion of Highveld bituminous coal (which contains ~1–2% sulfur and ~30% ash) generates SO2, NOx, and fine fly ash.\n"
        "Step 2: Public health epidemiology:\n"
        "Thermal inversions trap pollutants in the Highveld Priority Area airshed. Inhaled PM2.5 and SO2 irritate respiratory tracts, causing elevated rates of childhood asthma, COPD, and cardiovascular mortality."
    )
    return {
        "id": f"ns9_atm_40_{rng.randint(100000, 999999)}",
        "subskill": "40_eskom_coal_fired_power_stations_highveld_emissions_hotspot",
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
            "tier_1": "What toxic gases and particles are emitted by coal-fired power stations?",
            "tier_2": "SO2, NOx, fine particulate matter (PM2.5), and CO2 causing respiratory disease.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["eskom_coal_emissions_highveld_airshed"]
    }


def arch_41_carbon_footprint_measurement_individual_and_national(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In environmental science, an individual's or nation's climate impact is quantified as their **carbon footprint**.\n\n"
        "How is a carbon footprint defined and measured, and why is South Africa's per capita carbon footprint relatively high for a developing nation?"
    )
    correct = "It is the total amount of greenhouse gases emitted directly and indirectly by human activities, measured in tonnes of CO2 equivalent (tCO2e); South Africa's is high because ~80% of our national electricity is generated by burning domestic coal."
    options = [
        correct,
        "It is the shoe size of people who walk to work instead of taking the bus.",
        "It is the weight of charcoal burned in a weekend family barbecue braai.",
        "It is the number of trees planted in urban city parks each calendar year."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Carbon footprint definition:\n"
        "Calculated as mass of greenhouse gas emissions converted via GWP to CO2 equivalents: Total = Σ (Gas_i × GWP_i) in tCO2e.\n"
        "Step 2: South African context:\n"
        "South Africa emits ~7 to 8 tonnes of CO2 per capita per year—higher than the global average—due to an energy grid overwhelmingly dependent on carbon-intensive coal combustion."
    )
    return {
        "id": f"ns9_atm_41_{rng.randint(100000, 999999)}",
        "subskill": "41_carbon_footprint_measurement_individual_and_national",
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
            "tier_1": "What unit measures a carbon footprint and why is SA's footprint high?",
            "tier_2": "Measured in tonnes of CO2 equivalent; high because our grid relies on coal.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["carbon_footprint_measurement_definition"]
    }


def arch_42_renewable_energy_transition_south_african_solar_and_wind(rng: random.Random) -> Dict[str, Any]:
    prov = rng.choice([("Northern Cape", "exceptional solar irradiance exceeding 2 500 kWh/m² per year, ideal for utility-scale photovoltaic (PV) and concentrated solar power (CSP)"), ("Eastern and Western Cape", "strong coastal wind corridors providing high capacity factors for commercial wind turbine farms")])
    prov_name, adv = prov
    prompt = (
        f"South Africa's **Just Energy Transition** aims to decarbonize the electricity grid by deploying renewable energy.\n\n"
        f"What natural geographical advantage makes the **{prov_name}** an ideal location for renewable power generation?"
    )
    correct = f"Its {adv}."
    options = [
        correct,
        "It has subterranean uranium geysers that erupt boiling water into turbines.",
        "It is located outside Earth's atmosphere where sunlight is ten times stronger.",
        "It has zero wind and zero sun, making it completely immune to bad weather."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Renewable resource endowment of {prov_name}:\n"
        f"South Africa possesses world-class solar and wind resource potential.\n"
        f"Step 2: Geographical benefit:\n"
        f"The {prov_name} features {adv}, enabling low-cost zero-carbon electricity generation."
    )
    return {
        "id": f"ns9_atm_42_{rng.randint(100000, 999999)}",
        "subskill": "42_renewable_energy_transition_south_african_solar_and_wind",
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
            "tier_1": f"Why build renewable energy in the {prov_name}?",
            "tier_2": f"Its {adv[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["renewable_energy_transition_geography_sa"]
    }


def arch_43_energy_efficiency_led_lighting_and_building_insulation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Demand-side **energy efficiency** is widely recognized as the cheapest and fastest way to reduce greenhouse gas emissions.\n\n"
        "How does replacing traditional incandescent light bulbs with **Light Emitting Diodes (LEDs)** dramatically lower electricity demand and carbon emissions?"
    )
    correct = "Incandescent bulbs waste ~90% of electrical energy as heat, whereas LEDs convert up to 80% to 90% of electricity directly into visible light, consuming a fraction of the wattage and reducing the amount of coal that must be burned at power stations."
    options = [
        correct,
        "LEDs generate their own coal fuel from air molecules inside the glass bulb.",
        "LEDs absorb carbon dioxide from household air and turn it into solid sugar.",
        "LEDs operate without any electric current by harnessing moonlight."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Energy efficiency comparison:\n"
        "• Incandescent bulb (60 W): 90% thermal waste, 10% luminous efficacy (~15 lm/W).\n"
        "• LED bulb (8–10 W): High quantum efficiency (>100 lm/W), producing equal lumens for ~85% less wattage.\n"
        "Step 2: Emission mitigation:\n"
        "In a coal-dominated grid (producing ~1 kg CO2 per kWh), saving 50 W per light bulb directly prevents kilograms of coal combustion."
    )
    return {
        "id": f"ns9_atm_43_{rng.randint(100000, 999999)}",
        "subskill": "43_energy_efficiency_led_lighting_and_building_insulation",
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
            "tier_1": "Why do LEDs use so much less power than incandescent bulbs?",
            "tier_2": "Incandescents waste 90% as heat; LEDs convert up to 90% directly into light.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["energy_efficiency_led_emissions_reduction"]
    }


def arch_44_carbon_capture_and_geological_storage_technologies(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "**Carbon Capture and Storage (CCS)** is an engineered mitigation technology aimed at decarbonizing heavy industries (such as steel, cement, and petrochemicals).\n\n"
        "What sequential technological process defines Carbon Capture and Storage?"
    )
    correct = "Capturing CO2 from industrial flue gas emissions using chemical solvents (amines), compressing it into a dense supercritical liquid, transporting it via pipeline, and permanently injecting it thousands of meters underground into deep saline aquifers or depleted oil/gas reservoirs."
    options = [
        correct,
        "Catching CO2 with giant butterfly nets and releasing it on the surface of the Moon.",
        "Freezing CO2 into ice cubes and dropping them into domestic swimming pools.",
        "Mixing CO2 with drinking water and pumping it through household municipal kitchen taps."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Capture:\n"
        "Post-combustion chemical absorption using amine solvents strips CO2 from flue gas.\n"
        "Step 2: Compression and transport:\n"
        "CO2 is compressed above critical point (P > 7,38 MPa, T > 31,1 °C) into supercritical phase.\n"
        "Step 3: Geological sequestration:\n"
        "Injected into permeable sandstone formations beneath thick, impermeable shale caprocks at depths >800 m, where mineralization and capillary trapping permanently isolate the carbon."
    )
    return {
        "id": f"ns9_atm_44_{rng.randint(100000, 999999)}",
        "subskill": "44_carbon_capture_and_geological_storage_technologies",
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
            "tier_1": "How is CO2 captured and where is it permanently stored?",
            "tier_2": "Captured from flue gas, compressed, and injected deep underground into saline aquifers.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["carbon_capture_geological_sequestration"]
    }


def arch_45_reforestation_and_ecosystem_restoration_carbon_sinks(rng: random.Random) -> Dict[str, Any]:
    plant = "Spekboom (Portulacaria afra)"
    prompt = (
        f"In South Africa's Eastern Cape, ecological restoration projects are planting vast areas of indigenous **{plant}**.\n\n"
        f"What extraordinary physiological and carbon sequestration capability makes **{plant}** a 'miracle plant' for climate change mitigation?"
    )
    correct = "It can switch between C3 photosynthesis and Crassulacean Acid Metabolism (CAM) during drought, allowing it to photosynthesize and sequester up to 4 to 10 tonnes of carbon per hectare annually even in semi-arid, harsh conditions."
    options = [
        correct,
        "It absorbs nitrogen from the air and emits pure liquid petroleum from its leaves.",
        "It grows to 100 meters tall in three days and turns into solid steel timber.",
        "It consumes atmospheric ozone and turns it into drinkable fruit juice."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Physiology of {plant}:\n"
        "Indigenous succulent shrub in the Albany Thicket biome.\n"
        "Step 2: C3/CAM flexibility:\n"
        "Under moisture stress, it opens stomata at night (CAM mode) to minimize transpiration while fixing carbon as malate, then uses sunlight during the day with closed stomata. It sequesters carbon at rates comparable to tropical rainforests despite growing in semi-arid degraded lands."
    )
    return {
        "id": f"ns9_atm_45_{rng.randint(100000, 999999)}",
        "subskill": "45_reforestation_and_ecosystem_restoration_carbon_sinks",
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
            "tier_1": "What makes Spekboom so effective at carbon sequestration in dry areas?",
            "tier_2": "Switches to CAM photosynthesis, sequestering up to 4–10 tonnes of CO2/ha/yr in droughts.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["spekboom_cam_carbon_sequestration"]
    }


def arch_46_paris_agreement_and_cop_international_climate_treaties(rng: random.Random) -> Dict[str, Any]:
    target_c = rng.choice(["well below 2 °C and pursuing efforts to limit it to 1,5 °C", "to 1,5 °C above pre-industrial levels"])
    prompt = (
        f"Under the landmark 2015 **Paris Agreement** on climate change, nearly 200 nations committed to a global mitigation goal.\n\n"
        f"What temperature threshold did nations pledge to hold the increase in global average temperature to, and what mechanism tracks each country's pledge?"
    )
    correct = f"To hold global warming {target_c}; tracked through publicly registered, progressively ambitious Nationally Determined Contributions (NDCs) updated every five years."
    options = [
        correct,
        "To allow temperatures to rise by 10 °C to melt all polar ice caps for shipping routes.",
        "To cool the planet to -50 °C by building giant refrigerators at the North Pole.",
        "To abolish all sovereign nations and place the atmosphere under military control."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Paris Agreement primary treaty objective (Article 2):\n"
        f"Hold warming {target_c}.\n"
        "Step 2: Implementation architecture:\n"
        "Nations submit Nationally Determined Contributions (NDCs) detailing domestic emission targets, subject to the 'ratchet mechanism' requiring more stringent commitments at each global stocktake."
    )
    return {
        "id": f"ns9_atm_46_{rng.randint(100000, 999999)}",
        "subskill": "46_paris_agreement_and_cop_international_climate_treaties",
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
            "tier_1": "What is the global warming target in the Paris Agreement (1,5 °C / 2 °C)?",
            "tier_2": "Well below 2 °C, pursuing 1,5 °C, tracked via Nationally Determined Contributions (NDCs).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["paris_agreement_temperature_target_ndcs"]
    }


def arch_47_air_quality_index_particulate_matter_pm25_and_pm10(rng: random.Random) -> Dict[str, Any]:
    pm_type, diam = rng.choice([
        ("PM2.5", "fine inhalable particles with aerodynamic diameters smaller than 2,5 micrometers (< 2,5 µm) that penetrate deep into lung alveoli and cross into the bloodstream"),
        ("PM10", "coarse inhalable particles with diameters smaller than 10 micrometers (< 10 µm) that lodge in the upper respiratory tract, bronchi, and lungs")
    ])
    prompt = (
        "The Air Quality Index (AQI) monitors hazardous air pollution, with particular attention to **Particulate Matter**.\n\n"
        f"What physical size and health danger defines **{pm_type}**?"
    )
    correct = f"It refers to {diam}."
    options = [
        correct,
        "It refers to giant boulders larger than ten meters that fall out of passing clouds.",
        "It refers to harmless water droplets that moisturize the throat and prevent all coughing.",
        "It refers to radio waves emitted by television broadcasting towers."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Size definition of {pm_type}:\n"
        f"Aerodynamic diameter.\n"
        f"Step 2: Health impact:\n"
        f"It refers to {diam}."
    )
    return {
        "id": f"ns9_atm_47_{rng.randint(100000, 999999)}",
        "subskill": "47_air_quality_index_particulate_matter_pm25_and_pm10",
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
            "tier_1": f"How small are {pm_type} particles and where do they penetrate?",
            "tier_2": f"It refers to {diam[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["particulate_matter_size_health_impact"]
    }


def arch_48_photochemical_smog_tropospheric_ozone_and_nox(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "On hot sunny days, major cities with heavy vehicle traffic suffer from brown, irritating **photochemical smog**.\n\n"
        "What chemical reactions form hazardous ground-level (tropospheric) ozone in photochemical smog?"
    )
    correct = "Vehicle exhaust emissions of nitrogen oxides (NOx) and volatile organic compounds (VOCs) react in the presence of intense solar ultraviolet light; photolysis of NO2 releases free oxygen atoms that combine with O2 to form harmful ground-level ozone (O3)."
    options = [
        correct,
        "Stratospheric ozone sinks to the ground because it becomes heavy in cold weather.",
        "Trees produce ground-level ozone to protect themselves from insect pests.",
        "Household refrigerators leak liquid freon that turns into brown smoke on city streets."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Primary precursor emissions:\n"
        "Internal combustion engines emit NO, NO2, and unburned hydrocarbons (VOCs).\n"
        "Step 2: Photochemical synthesis:\n"
        "NO2 + hν (solar UV) → NO + O.\n"
        "O + O2 → O3 (tropospheric ozone).\n"
        "Unlike protective stratospheric ozone, ground-level ozone is a powerful oxidizing secondary pollutant causing lung inflammation, eye irritation, and agricultural crop necrosis."
    )
    return {
        "id": f"ns9_atm_48_{rng.randint(100000, 999999)}",
        "subskill": "48_photochemical_smog_tropospheric_ozone_and_nox",
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
            "tier_1": "What two vehicle pollutants react with sunlight to make ground-level ozone smog?",
            "tier_2": "Nitrogen oxides (NOx) and volatile organic compounds (VOCs) under sunlight.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["photochemical_smog_ground_level_ozone"]
    }


def arch_49_acid_rain_sulfur_dioxide_and_nitrogen_oxides_chemistry(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Industrial air pollution from coal power stations and smelters generates **acid precipitation** (acid rain) with a pH well below 5,0.\n\n"
        "What chemical reaction turns sulfur dioxide (SO2) gas into sulfuric acid (H2SO4) in rain clouds, and what ecological damage results?"
    )
    correct = "Sulfur dioxide is oxidized and dissolves in cloud droplets (2SO2 + O2 + 2H2O → 2H2SO4); the resulting acid rain leaches vital nutrient cations (Ca²⁺, Mg²⁺) from forest soils, mobilizes toxic aluminum into freshwater streams, and corrodes stone monuments."
    options = [
        correct,
        "Sulfur dioxide freezes into solid sugar crystals that feed freshwater fish.",
        "Sulfur dioxide turns cloud rain into pure milk that purifies forest ecosystems.",
        "Sulfur dioxide reacts with helium to produce indestructible plastic coatings on trees."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric oxidation of SO2:\n"
        "Gas-phase oxidation by hydroxyl radicals (•OH) or aqueous oxidation by H2O2 in cloud droplets: SO2 + H2O → H2SO3; SO3 + H2O → H2SO4.\n"
        "Step 2: Terrestrial and aquatic impacts:\n"
        "Acid rain (pH < 4,5) displaces essential base cations from soil clays into runoff, starves tree roots, and solubilizes toxic Al³⁺ ions that asphyxiate fish."
    )
    return {
        "id": f"ns9_atm_49_{rng.randint(100000, 999999)}",
        "subskill": "49_acid_rain_sulfur_dioxide_and_nitrogen_oxides_chemistry",
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
            "tier_1": "What acid forms when SO2 dissolves in cloud water and how does it damage soil?",
            "tier_2": "Forms sulfuric acid, leaching soil nutrients (Ca, Mg) and poisoning rivers.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["acid_rain_sulfuric_acid_leaching"]
    }


def arch_50_the_atmosphere_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    layer_case = rng.choice([
        ("Troposphere", "temperature decreases with altitude (-6,5 °C/km), contains 80% of mass and all weather", "convective overturning driven by surface solar heating"),
        ("Stratosphere", "temperature increases with altitude due to ozone UV absorption", "stable thermal inversion providing calm air for commercial jet flight"),
        ("Mesosphere", "temperature plummets to -90 °C (coldest layer), burning up incoming space meteoroids", "hypersonic ram pressure ablation of space debris")
    ])
    layer_name, thermal_char, mech = layer_case
    prompt = (
        f"An atmospheric scientist reviews data from an atmospheric sounding probe ascending through the **{layer_name}**.\n\n"
        f"What distinctive thermal profile and physical phenomenon identify the **{layer_name}**?"
    )
    correct = f"Its {thermal_char}, characterized by {mech}."
    distractors = [
        "A layer where air pressure increases to ten atmospheres and turns into liquid iron.",
        "A layer with zero gravity where air molecules freeze into solid gold bricks.",
        "A layer filled with flammable methane gas that burns continuously in sunlight."
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Thermal structure of {layer_name}:\n"
        f"Characterized by: {thermal_char}.\n"
        f"Step 2: Key physical mechanism:\n"
        f"Driven by: {mech}."
    )
    return {
        "id": f"ns9_atm_50_{rng.randint(100000, 999999)}",
        "subskill": "50_the_atmosphere_comprehensive_diagnostic_autopsy",
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
            "tier_1": f"Recall the thermal profile of the {layer_name}.",
            "tier_2": f"Its {thermal_char[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["atmosphere_comprehensive_thermal_autopsy"]
    }


BUILDERS_26_50 = {
    "26_water_vapor_most_abundant_natural_greenhouse_gas": arch_26_water_vapor_most_abundant_natural_greenhouse_gas,
    "27_carbon_dioxide_atmospheric_residence_time_and_sources": arch_27_carbon_dioxide_atmospheric_residence_time_and_sources,
    "28_methane_potent_short_lived_greenhouse_gas_sources": arch_28_methane_potent_short_lived_greenhouse_gas_sources,
    "29_nitrous_oxide_agricultural_fertilizers_and_emissions": arch_29_nitrous_oxide_agricultural_fertilizers_and_emissions,
    "30_enhanced_greenhouse_effect_anthropogenic_global_warming": arch_30_enhanced_greenhouse_effect_anthropogenic_global_warming,
    "31_fossil_fuel_combustion_carbon_cycle_imbalance": arch_31_fossil_fuel_combustion_carbon_cycle_imbalance,
    "32_deforestation_loss_of_photosynthetic_carbon_sinks": arch_32_deforestation_loss_of_photosynthetic_carbon_sinks,
    "33_keeling_curve_exponential_co2_rise_since_industrial_era": arch_33_keeling_curve_exponential_co2_rise_since_industrial_era,
    "34_ocean_acidification_carbonic_acid_and_marine_calcifiers": arch_34_ocean_acidification_carbonic_acid_and_marine_calcifiers,
    "35_polar_ice_sheet_melting_and_sea_level_rise_physics": arch_35_polar_ice_sheet_melting_and_sea_level_rise_physics,
    "36_positive_climate_feedback_ice_albedo_feedback_loop": arch_36_positive_climate_feedback_ice_albedo_feedback_loop,
    "37_positive_climate_feedback_permafrost_thaw_methane_release": arch_37_positive_climate_feedback_permafrost_thaw_methane_release,
    "38_droughts_and_heatwaves_southern_african_climate_impacts": arch_38_droughts_and_heatwaves_southern_african_climate_impacts,
    "39_coastal_erosion_and_storm_surges_cape_and_durban": arch_39_coastal_erosion_and_storm_surges_cape_and_durban,
    "40_eskom_coal_fired_power_stations_highveld_emissions_hotspot": arch_40_eskom_coal_fired_power_stations_highveld_emissions_hotspot,
    "41_carbon_footprint_measurement_individual_and_national": arch_41_carbon_footprint_measurement_individual_and_national,
    "42_renewable_energy_transition_south_african_solar_and_wind": arch_42_renewable_energy_transition_south_african_solar_and_wind,
    "43_energy_efficiency_led_lighting_and_building_insulation": arch_43_energy_efficiency_led_lighting_and_building_insulation,
    "44_carbon_capture_and_geological_storage_technologies": arch_44_carbon_capture_and_geological_storage_technologies,
    "45_reforestation_and_ecosystem_restoration_carbon_sinks": arch_45_reforestation_and_ecosystem_restoration_carbon_sinks,
    "46_paris_agreement_and_cop_international_climate_treaties": arch_46_paris_agreement_and_cop_international_climate_treaties,
    "47_air_quality_index_particulate_matter_pm25_and_pm10": arch_47_air_quality_index_particulate_matter_pm25_and_pm10,
    "48_photochemical_smog_tropospheric_ozone_and_nox": arch_48_photochemical_smog_tropospheric_ozone_and_nox,
    "49_acid_rain_sulfur_dioxide_and_nitrogen_oxides_chemistry": arch_49_acid_rain_sulfur_dioxide_and_nitrogen_oxides_chemistry,
    "50_the_atmosphere_comprehensive_diagnostic_autopsy": arch_50_the_atmosphere_comprehensive_diagnostic_autopsy,
}
