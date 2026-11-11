"""Grade 8 Natural Sciences: Term 1 - Interactions and Interdependence (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 1/02. Interactions and interdependence within the environment.md.
Focus: Ecological levels, abiotic factors, trophic levels, food chains, food webs, ecological pyramids, and symbiotic interactions.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Levels of ecological organisation hierarchy
def arch_01_levels_of_ecological_organisation_hierarchy(rng: random.Random) -> Dict[str, Any]:
    levels = [
        "Individual organism -> Population -> Community -> Ecosystem -> Biosphere",
        "Biosphere -> Community -> Individual organism -> Population -> Ecosystem",
        "Population -> Individual organism -> Ecosystem -> Community -> Biosphere",
        "Community -> Population -> Individual organism -> Biosphere -> Ecosystem",
    ]
    correct = levels[0]
    options = list(levels)
    rng.shuffle(options)
    prompt = (
        f"In ecology, living matter and environmental relationships are organized into hierarchical levels of complexity.\n\n"
        f"Which sequence correctly ranks these ecological levels from the simplest (narrowest) to the most complex (broadest)?"
    )
    sol = (
        f"**Step 1:** Trace the hierarchical levels of ecological organisation:\n"
        f"1. Individual organism (a single living member of a species).\n"
        f"2. Population (all individuals of the same species living together in an area).\n"
        f"3. Community (all interacting populations of different species in an area).\n"
        f"4. Ecosystem (the biotic community interacting with its non-living abiotic environment).\n"
        f"5. Biosphere (all ecosystems on Earth combined).\n\n"
        f"**Step 2:** The correct hierarchical progression is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_01_{rng.randint(100000, 999999)}",
        "subskill": "01_levels_of_ecological_organisation_hierarchy",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Start with one organism, then a group of the same species, then all species together.",
            "tier_2": "Organism -> Population -> Community -> Ecosystem -> Biosphere.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ecological_hierarchy_order_misconception"],
    }


# 02. Population definition and characteristics
def arch_02_population_definition_and_characteristics(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("the herd of Hartmann's mountain zebra (*Equus zebra hartmannae*)", "in the rocky gorges of the Richtersveld Transfrontier Park in 2024"),
        ("the troop of chacma baboons (*Papio ursinus*)", "in the Cape Point Nature Reserve during the current year"),
        ("the colony of African penguins (*Spheniscus demersus*)", "breeding on Boulders Beach in Simon's Town this season"),
    ]
    species_group, location_time = rng.choice(examples)
    prompt = (
        f"Consider {species_group} {location_time}.\n\n"
        f"What is the precise scientific definition of a biological **population**?"
    )
    correct = (
        "A group of organisms of the same species living in a specific geographical area "
        "at a specific point in time, capable of interbreeding with one another."
    )
    options = [
        correct,
        "All the non-living rocks, clouds, and minerals found inside a national park boundary.",
        "A collection of completely different animal and plant species that never reproduce.",
        "All the deceased animal fossils preserved underground since the Jurassic period.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define an ecological population:\n"
        f"- Criteria for a population:\n"
        f"  1. Same species (can interbreed freely producing fertile offspring).\n"
        f"  2. Specific defined habitat area ({location_time}).\n"
        f"  3. Specific defined point in time.\n\n"
        f"**Step 2:** The definition is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_02_{rng.randint(100000, 999999)}",
        "subskill": "02_population_definition_and_characteristics",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Do members of a population belong to the same species or many different species?",
            "tier_2": "A population is organisms of the same species in an area at a specific time.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["population_definition_misconception"],
    }


# 03. Community definition and species assemblage
def arch_03_community_definition_and_species_assemblage(rng: random.Random) -> Dict[str, Any]:
    ecosystems = [
        ("a waterhole in the Kruger National Park", "impala, lions, dung beetles, fever trees, and marsh terrapins interacting"),
        ("a kelp forest off the coast of False Bay", "sea bamboo kelp, cape fur seals, abalone, and rock lobsters interacting"),
        ("a dry Karoo shrubland", "succulent karoo plants, tortoises, bat-eared foxes, and harvester termites interacting"),
    ]
    habitat, assemblage = rng.choice(ecosystems)
    prompt = (
        f"At {habitat}, researchers observe {assemblage}.\n\n"
        f"In ecological science, what term designates all the interacting populations of different species coexisting within a defined habitat?"
    )
    correct = "A biological community"
    options = [
        correct,
        "A single abiotic lithosphere",
        "A homogeneous chemical solution",
        "A solitary clone organism",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish a population from a community:\n"
        f"- Population: one single species.\n"
        f"- Community: all the populations of different species living and interacting in a shared habitat ({habitat}).\n\n"
        f"**Step 2:** The term is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_03_{rng.randint(100000, 999999)}",
        "subskill": "03_community_definition_and_species_assemblage",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What do you call all the different populations living together in one area?",
            "tier_2": "A community consists of multiple interacting populations.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["community_vs_population_confusion"],
    }


# 04. Ecosystem definition biotic and abiotic synthesis
def arch_04_ecosystem_definition_biotic_and_abiotic_synthesis(rng: random.Random) -> Dict[str, Any]:
    biomes = [
        ("the Fynbos biome", "proteas, sunbirds, and soil fungi (biotic)", "winter rainfall, acidic sandstone soils, and fierce coastal winds (abiotic)"),
        ("the Kalahari Savanna", "acacia trees, oryx, and termites (biotic)", "intense solar radiation, high summer temperatures, and deep porous red sands (abiotic)"),
        ("the Knysna Indigenous Forest", "yellowwood trees, loeries, and decomposing bracket fungi (biotic)", "year-round rainfall, shaded forest floor, and damp humus-rich soil (abiotic)"),
    ]
    biome_name, biotic_part, abiotic_part = rng.choice(biomes)
    prompt = (
        f"In {biome_name}, living organisms such as {biotic_part} interact continuously with non-living factors like {abiotic_part}.\n\n"
        f"What is an **ecosystem**?"
    )
    correct = (
        "A dynamic system composed of a biological community of living (biotic) organisms "
        "interacting with each other and with their physical non-living (abiotic) environment."
    )
    options = [
        correct,
        "A collection of only abiotic non-living minerals that contains zero living cells.",
        "An artificial glass greenhouse where all natural environmental factors are permanently banned.",
        "A mathematical formula used exclusively to calculate the weight of diesel fuel.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define an ecosystem:\n"
        f"- An ecosystem unites the biotic component (all living organisms: producers, consumers, decomposers) with the abiotic component (temperature, water, light, soil).\n"
        f"- Matter cycles and energy flows continuously between the biotic and abiotic parts.\n\n"
        f"**Step 2:** The definition is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_04_{rng.randint(100000, 999999)}",
        "subskill": "04_ecosystem_definition_biotic_and_abiotic_synthesis",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does an ecosystem include living things only, or living things plus their physical surroundings?",
            "tier_2": "It includes biotic (living) and abiotic (non-living) components interacting together.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ecosystem_biotic_abiotic_misconception"],
    }


# 05. Biosphere scope and global life zone
def arch_05_biosphere_scope_and_global_life_zone(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The Earth consists of several major spheres: the atmosphere (air), the hydrosphere (water), "
        f"the lithosphere (crust and soil), and the biosphere.\n\n"
        f"What is the **biosphere**?"
    )
    correct = (
        "The global ecological system comprising all life on Earth and all regions of the atmosphere, "
        "hydrosphere, and lithosphere where living organisms exist."
    )
    options = [
        correct,
        "The molten iron core at the center of the Earth where temperatures exceed 5 000 degrees Celsius.",
        "The dead vacuum of empty space extending between Mars and Jupiter.",
        "A synthetic plastic sphere manufactured by engineers to house domestic pets.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define the biosphere:\n"
        f"- The biosphere is the global sum of all ecosystems.\n"
        f"- It encompasses the narrow surface zone of planet Earth supporting life: the lower atmosphere, the oceans and freshwater bodies (hydrosphere), and upper soil layers (lithosphere).\n\n"
        f"**Step 2:** The definition is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_05_{rng.randint(100000, 999999)}",
        "subskill": "05_biosphere_scope_and_global_life_zone",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What does the prefix 'bio-' mean? Life.",
            "tier_2": "The biosphere is the zone of planet Earth where all living things exist.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["biosphere_scope_misconception"],
    }


# 06. Abiotic factors edaphic soil properties
def arch_06_abiotic_factors_edaphic_soil_properties(rng: random.Random) -> Dict[str, Any]:
    soil_types = [
        ("sandy soil (coarse particles, high permeability, low water retention)", "arid semi-desert plants with deep taproots and drought adaptations"),
        ("clay soil (microscopic fine particles, poor drainage, waterlogged when wet)", "wetland reeds and plants capable of tolerating low soil oxygen"),
        ("loam soil (balanced mix of sand, silt, clay, and rich organic humus)", "diverse agricultural crops and dense temperate deciduous trees"),
    ]
    soil_desc, plant_adaptation = rng.choice(soil_types)
    prompt = (
        f"Soil properties—known scientifically as **edaphic factors**—powerfully influence which plant species can thrive in an ecosystem. "
        f"In an area with {soil_desc}, you predominantly find {plant_adaptation}.\n\n"
        f"Which of the following is considered an **edaphic (soil-related) abiotic factor** in an ecosystem?"
    )
    correct = "Soil pH, mineral nutrient content, particle texture, and water-holding capacity"
    options = [
        correct,
        "Predation rate by juvenile hunting leopards",
        "The flight velocity of migrating swallows in autumn",
        "Viral infections spreading among savanna ungulates",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define edaphic abiotic factors:\n"
        f"- Edaphic factors pertain specifically to the physical and chemical characteristics of the soil.\n"
        f"- These include: soil texture (sand/silt/clay ratio), soil pH, organic humus content, aeration, and drainage capacity.\n\n"
        f"**Step 2:** The edaphic abiotic factor is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_06_{rng.randint(100000, 999999)}",
        "subskill": "06_abiotic_factors_edaphic_soil_properties",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What does 'edaphic' refer to in science? Soil.",
            "tier_2": "Edaphic factors include soil texture, pH, and water-holding capacity.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["edaphic_factors_definition_misconception"],
    }


# 07. Abiotic factors physiographic aspect and slope
def arch_07_abiotic_factors_physiographic_aspect_and_slope(rng: random.Random) -> Dict[str, Any]:
    slopes = [
        ("north-facing slopes in South Africa (Southern Hemisphere)", "receive direct intense solar radiation throughout the day", "warmer, drier microclimates dominated by drought-tolerant succulents and grasses"),
        ("south-facing slopes in South Africa (Southern Hemisphere)", "receive much less direct sunlight and remain in shade", "cooler, moister microclimates supporting dense evergreen afro-montane forests and ferns"),
    ]
    slope_desc, solar_feature, veg_result = rng.choice(slopes)
    prompt = (
        f"In the Southern Hemisphere (such as in South Africa's mountain ranges), **aspect** refers to the compass direction "
        f"that a mountain slope faces. {slope_desc.capitalize()} {solar_feature}, resulting in {veg_result}.\n\n"
        f"Why do north-facing and south-facing slopes on the same South African mountain support dramatically different plant communities?"
    )
    correct = (
        "Aspect determines the angle and duration of solar irradiation; north-facing slopes receive more direct sunlight, "
        "causing higher soil evaporation and temperatures, while south-facing slopes are shadier, cooler, and retain moisture."
    )
    options = [
        correct,
        "North-facing slopes are protected by invisible forcefields that block gravitational forces.",
        "Animals carry seeds exclusively towards the northern hemisphere because of magnetic poles.",
        "South-facing slopes have no soil and consist entirely of frozen glacier ice throughout summer.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze physiographic aspect in the Southern Hemisphere:\n"
        f"- The sun is always in the northern sky at our latitude.\n"
        f"- North-facing slopes face the sun -> high solar radiation -> hot, desiccating, low soil moisture -> drought-tolerant xerophytes.\n"
        f"- South-facing slopes are shaded -> cool, humid, high soil moisture -> shade-loving mesophytic forests.\n\n"
        f"**Step 2:** The scientific explanation is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_07_{rng.randint(100000, 999999)}",
        "subskill": "07_abiotic_factors_physiographic_aspect_and_slope",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "In South Africa, which direction does the sun shine from: north or south?",
            "tier_2": "The sun shines from the north, so north-facing slopes are sunnier, hotter, and drier.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["physiographic_aspect_southern_hemisphere_misconception"],
    }


# 08. Abiotic factors light intensity and photoperiod
def arch_08_abiotic_factors_light_intensity_and_photoperiod(rng: random.Random) -> Dict[str, Any]:
    phenomena = [
        ("autumn deciduous leaf drop and winter dormancy in trees", "shortening day length (photoperiod) signalling oncoming winter freezing conditions"),
        ("synchronised spring flowering in Namaqualand wild daisies", "increasing day length and rising temperatures triggering floral bud burst"),
        ("stratification in aquatic lakes", "light intensity diminishing exponentially with water depth, restricting photosynthesis to the euphotic zone"),
    ]
    phenomenon, trigger = rng.choice(phenomena)
    prompt = (
        f"In natural ecosystems, light acts as a critical abiotic regulator, as illustrated by {phenomenon}, "
        f"which is governed by {trigger}.\n\n"
        f"How does **photoperiod (day length)** function as a biological cue for organisms?"
    )
    correct = (
        "Changes in day length provide reliable seasonal signals that trigger developmental events "
        "such as flowering, breeding, migration, or winter dormancy before harsh weather arrives."
    )
    options = [
        correct,
        "Photoperiod changes the chemical elements of the soil from silicon into pure hydrogen gas.",
        "Long days cause animals to lose all cellular DNA and turn into non-living plants.",
        "Short days permanently destroy the Earth's atmosphere until the following spring.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand photoperiodism in living organisms:\n"
        f"- While daily temperature fluctuates unpredictably, day length (photoperiod) is an astronomically precise seasonal indicator.\n"
        f"- Organisms use photoreceptor pigments (like phytochromes in plants or melatonin in animals) to detect photoperiod shifts and coordinate seasonal reproduction and survival strategies.\n\n"
        f"**Step 2:** The biological role is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_08_{rng.randint(100000, 999999)}",
        "subskill": "08_abiotic_factors_light_intensity_and_photoperiod",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What tells plants that winter is coming before it even starts freezing?",
            "tier_2": "Shortening daylight hours (photoperiod) signal the change of seasons.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["photoperiodism_cue_misconception"],
    }


# 09. Abiotic factors temperature and water availability
def arch_09_abiotic_factors_temperature_and_water_availability(rng: random.Random) -> Dict[str, Any]:
    biomes = [
        ("the hyper-arid Namib Desert", "scanty rainfall (<20 mm/year) and scorching daytime heat", "succulents, fog-harvesting beetles, and subterranean burrowing lizards"),
        ("the Afro-alpine zone of the Drakensberg summit", "sub-zero winter temperatures and frequent heavy frosts", "dwarf shrubs, tussock grasses, and freeze-tolerant insects"),
    ]
    biome_name, climatic_extremes, organisms = rng.choice(biomes)
    prompt = (
        f"In {biome_name}, organisms face extreme abiotic conditions: {climatic_extremes}. "
        f"Only specialized species such as {organisms} can survive.\n\n"
        f"Why are **temperature** and **water availability** considered the two primary abiotic determinants of terrestrial biomes on Earth?"
    )
    correct = (
        "Water is essential as a biological solvent and biochemical reactant, while temperature governs cellular enzyme reaction rates; "
        "together they determine primary plant productivity and the distribution of all life."
    )
    options = [
        correct,
        "Temperature and water decide what colour paint the clouds will use in the morning.",
        "They determine the speed at which tectonic plates rotate around the Moon.",
        "Water and temperature are living organisms that eat herbivorous mammals.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze temperature and water as primary climatic drivers:\n"
        f"- Life is water-dependent: all cellular chemistry requires aqueous media.\n"
        f"- Temperature sets the thermodynamic limits of enzymatic catalysis (enzymes denature in extreme heat or slow drastically in freezing cold).\n"
        f"- The combination of mean annual temperature and precipitation dictates biome boundaries across the globe.\n\n"
        f"**Step 2:** The fundamental reason is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_09_{rng.randint(100000, 999999)}",
        "subskill": "09_abiotic_factors_temperature_and_water_availability",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What two factors determine whether an area is a desert or a tropical rainforest?",
            "tier_2": "Rainfall (water) and temperature determine primary plant growth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["temperature_water_biome_determinant_misconception"],
    }


# 10. Producers autotrophs converting solar energy
def arch_10_producers_autotrophs_converting_solar_energy(rng: random.Random) -> Dict[str, Any]:
    producers = [
        ("red grass (*Themeda triandra*) on the Free State highveld", "grazing herbivores like blesbok and cattle"),
        ("phytoplankton algae in coastal ocean currents", "filter-feeding zooplankton, anchovies, and baleen whales"),
        ("sweet thorn trees (*Vachellia karroo*) in the savanna bushveld", "browsing giraffes, kudu, and caterpillars"),
    ]
    plant, dependent_animals = rng.choice(producers)
    prompt = (
        f"Consider {plant}. These organisms form the first trophic level in food chains, sustaining {dependent_animals}.\n\n"
        f"Why are green plants and photosynthetic algae classified ecologically as **producers (autotrophs)**?"
    )
    correct = (
        "They synthesize organic food (glucose and starch) from inorganic substances using radiant light energy, "
        "bringing new chemical potential energy into the ecosystem."
    )
    options = [
        correct,
        "They hunt other living organisms at night using sharp teeth and claws.",
        "They decompose dead plastic garbage into radioactive uranium ore.",
        "They absorb finished cooked meals directly from passing human vehicles.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define ecological producers (autotrophs):\n"
        f"- 'Auto' = self; 'troph' = nourishment.\n"
        f"- Producers are the only trophic level capable of capturing non-biological energy (radiant sunlight) and locking it into organic chemical bonds (glucose).\n"
        f"- All other trophic levels ultimately depend on this primary production for food.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_10_{rng.randint(100000, 999999)}",
        "subskill": "10_producers_autotrophs_converting_solar_energy",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Can plants make their own food, or do they eat other organisms?",
            "tier_2": "Producers manufacture their own food from sunlight, water, and CO2.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["producer_autotroph_definition_misconception"],
    }


# 11. Consumers herbivores primary consumers
def arch_11_consumers_herbivores_primary_consumers(rng: random.Random) -> Dict[str, Any]:
    herbivores = [
        ("a plains zebra (*Equus quagga*)", "feeding exclusively on fibrous grasses in the savanna"),
        ("a desert tortoise (*Stigmochelys pardalis*)", "grazing on wild succulent leaves and Karoo herbs"),
        ("a Cape honeybee (*Apis mellifera capensis*)", "feeding on floral nectar and collecting pollen"),
    ]
    animal, feeding_habit = rng.choice(herbivores)
    prompt = (
        f"Consider {animal}, {feeding_habit}.\n\n"
        f"In an ecological trophic pyramid, what term describes organisms that feed directly and exclusively on producers?"
    )
    correct = "Primary consumers (herbivores)"
    options = [
        correct,
        "Apex tertiary carnivores",
        "Abiotic chemical decomposers",
        "Autotrophic solar producers",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify the consumer level:\n"
        f"- Trophic Level 1: Producers (green plants).\n"
        f"- Trophic Level 2: Primary consumers (herbivores that consume producers directly).\n"
        f"- Examples: {animal}.\n\n"
        f"**Step 2:** The correct designation is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_11_{rng.randint(100000, 999999)}",
        "subskill": "11_consumers_herbivores_primary_consumers",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What is an animal that eats only plants called, and what consumer level is it?",
            "tier_2": "Plant-eaters are herbivores, which are primary consumers.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["primary_consumer_herbivore_misconception"],
    }


# 12. Consumers carnivores secondary and tertiary
def arch_12_consumers_carnivores_secondary_and_tertiary(rng: random.Random) -> Dict[str, Any]:
    predators = [
        ("a praying mantis feeding on a grasshopper (which eats grass)", "secondary consumer (carnivore feeding on primary consumer)"),
        ("a leopard (*Panthera pardus*) preying on a baboon (which preys on insects)", "tertiary consumer (carnivore feeding on secondary consumer)"),
        ("a barn owl preying on a field mouse (which feeds on grain seeds)", "secondary consumer (carnivore feeding on herbivorous primary consumer)"),
    ]
    example, trophic_role = rng.choice(predators)
    prompt = (
        f"Consider the feeding interaction: {example}.\n\n"
        f"How is this hunting animal classified in terms of its trophic level and ecological consumer category?"
    )
    correct = f"It acts as a {trophic_role}."
    options = [
        correct,
        "It acts as an autotrophic producer manufacturing sugars using light.",
        "It acts as an abiotic edaphic mineral soil component.",
        "It acts as an aquatic photosynthetic algae cluster.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace the trophic stages:\n"
        f"- Producer (plant) -> Primary consumer (herbivore) -> Secondary consumer (carnivore that eats herbivores) -> Tertiary consumer (predator eating secondary consumers).\n"
        f"- In this scenario: {example}.\n\n"
        f"**Step 2:** The correct classification is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_12_{rng.randint(100000, 999999)}",
        "subskill": "12_consumers_carnivores_secondary_and_tertiary",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Count the steps from the plant: Plant (1) -> Herbivore (2) -> Carnivore (3).",
            "tier_2": f"It acts as a {trophic_role}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["secondary_tertiary_consumer_confusion"],
    }


# 13. Consumers omnivores and scavengers
def arch_13_consumers_omnivores_and_scavengers(rng: random.Random) -> Dict[str, Any]:
    creatures = [
        ("a spotted hyena (*Crocuta crocuta*) or white-backed vulture", "feeding on the carcasses of animals that were already killed by lions or died naturally", "Scavenger"),
        ("a chacma baboon or warthog (*Phacochoerus africanus*)", "consuming a mixed diet of roots, wild fruits, insects, and small reptiles", "Omnivore"),
    ]
    animal, feeding_habit, classification = rng.choice(creatures)
    prompt = (
        f"Consider {animal}, {feeding_habit}.\n\n"
        f"What specific ecological term designates an organism that exhibits this feeding strategy?"
    )
    correct = classification
    options = [
        correct,
        "Strict herbivorous primary producer",
        "Abiotic geological deposit",
        "Photosynthetic water plant",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define specialised consumer categories:\n"
        f"- Omnivore: eats both plant matter and animal matter (e.g. baboons, humans).\n"
        f"- Scavenger: feeds on dead animal carcasses killed by other predators or by disease/natural causes (e.g. vultures, hyenas).\n\n"
        f"**Step 2:** For {animal}, the term is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_13_{rng.randint(100000, 999999)}",
        "subskill": "13_consumers_omnivores_and_scavengers",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does this animal eat both plants and meat, or does it clean up dead carcasses?",
            "tier_2": f"The correct term for this feeding habit is {classification}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["omnivore_scavenger_distinction_misconception"],
    }


# 14. Decomposers bacteria and fungi nutrient recycling
def arch_14_decomposers_bacteria_and_fungi_nutrient_recycling(rng: random.Random) -> Dict[str, Any]:
    organisms = [
        ("saprophytic shelf fungi and soil bacteria", "a fallen rotten yellowwood log on the forest floor"),
        ("microscopic decomposer bacteria", "dead organic plant detritus and animal excretions in savanna topsoil"),
    ]
    microbes, context = rng.choice(organisms)
    prompt = (
        f"In an indigenous woodland, {microbes} break down {context}.\n\n"
        f"What is the indispensable ecological role of **decomposers** in sustaining an ecosystem?"
    )
    correct = (
        "They break down dead organic matter and animal wastes, releasing locked mineral nutrients "
        "(such as nitrates and phosphates) back into the soil for plants to absorb again."
    )
    options = [
        correct,
        "They absorb sunlight to generate radioactive energy for nocturnal owls.",
        "They hunt live running antelopes and eat them alive on mountain ridges.",
        "They freeze the soil solid to prevent earthworms from crawling around.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the ecological role of decomposers:\n"
        f"- Without decomposers (bacteria and fungi), dead organisms would pile up indefinitely, and vital mineral nutrients (nitrogen, phosphorus) would remain locked up.\n"
        f"- Decomposers secrete digestive enzymes onto dead organic matter, breaking it down into simple inorganic nutrients returned to soil and water.\n\n"
        f"**Step 2:** The indispensable role is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_14_{rng.randint(100000, 999999)}",
        "subskill": "14_decomposers_bacteria_and_fungi_nutrient_recycling",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What would happen to dead leaves and animal corpses if fungi and bacteria did not exist?",
            "tier_2": "Decomposers recycle dead matter into soil nutrients for new plant growth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["decomposer_nutrient_cycle_misconception"],
    }


# 15. Food chain construction and arrow direction energy flow (with dynamic SVG)
def arch_15_food_chain_construction_and_arrow_direction_energy_flow(rng: random.Random) -> Dict[str, Any]:
    chains = [
        ("Savanna Grass", "Locust", "Lizard", "Kestrel Falcon"),
        ("Acacia Leaves", "Impala", "Cheetah", "Vulture"),
        ("Pond Algae", "Mayfly Nymph", "Freshwater Tilapia", "African Fish Eagle"),
    ]
    c1, c2, c3, c4 = rng.choice(chains)
    box_color = rng.choice(["#dcfce7", "#e0f2fe", "#fef3c7"])

    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="220" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Food Chain: Direction of Energy Flow</text>'
        f'<rect x="10" y="70" width="85" height="45" fill="{box_color}" stroke="#15803d" stroke-width="1.5" rx="4" />'
        f'<text x="52" y="97" font-size="9" fill="#14532d" font-weight="bold" text-anchor="middle">{c1}</text>'
        f'<path d="M 100 92 L 120 92" stroke="#dc2626" stroke-width="2.5" marker-end="url(#arrow)" />'
        f'<polygon points="120,92 114,88 114,96" fill="#dc2626" />'
        f'<rect x="125" y="70" width="75" height="45" fill="{box_color}" stroke="#0369a1" stroke-width="1.5" rx="4" />'
        f'<text x="162" y="97" font-size="9" fill="#0369a1" font-weight="bold" text-anchor="middle">{c2}</text>'
        f'<polygon points="205,92 199,88 199,96" fill="#dc2626" />'
        f'<rect x="210" y="70" width="85" height="45" fill="{box_color}" stroke="#b45309" stroke-width="1.5" rx="4" />'
        f'<text x="252" y="97" font-size="9" fill="#78350f" font-weight="bold" text-anchor="middle">{c3}</text>'
        f'<polygon points="300,92 294,88 294,96" fill="#dc2626" />'
        f'<rect x="305" y="70" width="115" height="45" fill="{box_color}" stroke="#991b1b" stroke-width="1.5" rx="4" />'
        f'<text x="362" y="97" font-size="9" fill="#991b1b" font-weight="bold" text-anchor="middle">{c4}</text>'
        f'<text x="220" y="155" font-size="10" fill="#475569" text-anchor="middle">Arrows point from the organism being eaten to the organism that eats it (flow of energy)</text>'
        f'</svg>'
    )

    prompt = (
        f"In a food chain representation such as: **{c1} -> {c2} -> {c3} -> {c4}**, "
        f"what do the arrows scientifically signify, and in which direction must they always point?"
    )
    correct = (
        "The arrows represent the flow of chemical potential energy, pointing from the organism that is eaten "
        "to the consumer that eats it."
    )
    options = [
        correct,
        "The arrows point backwards to show who gave birth to whom.",
        "The arrows point from predator to prey to show which animal runs faster.",
        "The arrows indicate the geographical wind direction across the game reserve.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand arrow conventions in ecological food chains:\n"
        f"- The arrow symbolizes: 'is eaten by' or 'energy transfers to'.\n"
        f"- Therefore: {c1} (energy source) -> {c2} (consumer absorbing energy) -> {c3} -> {c4}.\n"
        f"- The arrow points in the direction of energy flow (into the mouth/body of the consumer).\n\n"
        f"**Step 2:** The scientific meaning is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_15_{rng.randint(100000, 999999)}",
        "subskill": "15_food_chain_construction_and_arrow_direction_energy_flow",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "hints": {
            "tier_1": "Where does the food energy go: into the predator or into the plant?",
            "tier_2": "Arrows point in the direction of energy flow: from eaten to eater.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["food_chain_arrow_direction_misconception"],
    }


# 16. Food web analysis interpreting interconnected chains
def arch_16_food_web_analysis_interpreting_interconnected_chains(rng: random.Random) -> Dict[str, Any]:
    ecosystem = rng.choice([
        ("a bushveld savanna", "acacia trees", "impala and caterpillars", "guinea fowl and leopards"),
        ("a fynbos mountain slope", "protea shrubs", "Cape sugarbirds and beetles", "snakes and black eagles"),
    ])
    prompt = (
        f"In natural ecosystems like {ecosystem[0]}, animals rarely feed on just one single food item. "
        f"For example, {ecosystem[1]} are eaten by {ecosystem[2]}, which in turn are preyed upon by {ecosystem[3]}.\n\n"
        f"Why is a **food web** a far more realistic scientific model of an ecosystem than a single linear **food chain**?"
    )
    correct = (
        "In nature, most organisms eat more than one type of food and are fed upon by multiple predators, "
        "forming an interconnected network of feeding interactions that provides ecological stability."
    )
    options = [
        correct,
        "Because linear food chains are illegal under international environmental conservation treaties.",
        "Because animals change into non-living rocks whenever a single food chain breaks.",
        "Because food webs have zero connections to green plants or sunlight energy.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare food chain vs food web:\n"
        f"- Food chain: oversimplified single linear pathway of energy flow.\n"
        f"- Food web: interconnected network of multiple overlapping food chains.\n"
        f"- Food webs reflect real ecological resilience: if one prey species declines, predators can switch to alternative prey species.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_16_{rng.randint(100000, 999999)}",
        "subskill": "16_food_web_analysis_interpreting_interconnected_chains",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Do lions only ever eat one single species of antelope in their entire lives?",
            "tier_2": "Organisms eat diverse foods, forming an interconnected web rather than a single line.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["food_chain_vs_web_realism_misconception"],
    }


# 17. Trophic levels identifying positions in food webs
def arch_17_trophic_levels_identifying_positions_in_food_webs(rng: random.Random) -> Dict[str, Any]:
    levels = [
        ("Trophic Level 1", "Producers (e.g. green grasses and trees that fix solar energy)"),
        ("Trophic Level 2", "Primary consumers (e.g. herbivorous insects, rodents, and antelopes)"),
        ("Trophic Level 3", "Secondary consumers (e.g. insectivorous birds, frogs, and small carnivores)"),
        ("Trophic Level 4", "Tertiary consumers (e.g. apex predatory eagles, leopards, and lions)"),
    ]
    target_num, target_desc = rng.choice(levels)
    prompt = (
        f"In an ecosystem energy diagram, feeding positions are categorized as numbered **trophic levels**.\n\n"
        f"Which ecological group occupies **{target_num}**?"
    )
    correct = target_desc
    alt_desc = [l[1] for l in levels if l[0] != target_num]
    options = [correct] + alt_desc
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall the standard numbered trophic levels:\n"
        f"- Level 1: Producers (green plants/algae).\n"
        f"- Level 2: Primary consumers (herbivores).\n"
        f"- Level 3: Secondary consumers (carnivores eating herbivores).\n"
        f"- Level 4: Tertiary consumers (top carnivores).\n\n"
        f"**Step 2:** {target_num} corresponds to: **{correct}**."
    )
    return {
        "id": f"ns8_eco_17_{rng.randint(100000, 999999)}",
        "subskill": "17_trophic_levels_identifying_positions_in_food_webs",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Think about which organisms sit at {target_num}: plants at 1, herbivores at 2, etc.",
            "tier_2": f"{target_num} is occupied by {target_desc}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["trophic_level_numbering_misconception"],
    }


# 18. Pyramid of energy and the ten percent energy rule (with dynamic SVG)
def arch_18_pyramid_of_energy_and_the_ten_percent_energy_rule(rng: random.Random) -> Dict[str, Any]:
    producer_energy = rng.choice([100000, 200000, 500000])
    herbivore_energy = producer_energy // 10
    carnivore_energy = herbivore_energy // 10
    apex_energy = carnivore_energy // 10

    svg = (
        f'<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="210" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Pyramid of Energy (10% Transfer Rule)</text>'
        f'<polygon points="210,40 170,75 250,75" fill="#ef4444" stroke="#991b1b" />'
        f'<text x="210" y="65" font-size="9" fill="#ffffff" font-weight="bold" text-anchor="middle">{apex_energy} kJ</text>'
        f'<polygon points="170,75 250,75 290,115 130,115" fill="#f59e0b" stroke="#b45309" />'
        f'<text x="210" y="100" font-size="9" fill="#ffffff" font-weight="bold" text-anchor="middle">{carnivore_energy} kJ</text>'
        f'<polygon points="130,115 290,115 330,155 90,155" fill="#3b82f6" stroke="#1d4ed8" />'
        f'<text x="210" y="140" font-size="9" fill="#ffffff" font-weight="bold" text-anchor="middle">{herbivore_energy} kJ</text>'
        f'<polygon points="90,155 330,155 370,195 50,195" fill="#22c55e" stroke="#15803d" />'
        f'<text x="210" y="180" font-size="10" fill="#ffffff" font-weight="bold" text-anchor="middle">Producers: {producer_energy} kJ</text>'
        f'<text x="210" y="212" font-size="10" fill="#475569" text-anchor="middle">~90% of energy is lost as metabolic heat and waste at each successive level</text>'
        f'</svg>'
    )

    prompt = (
        f"In a savanna grassland ecosystem, primary producers fix {producer_energy} kJ of chemical energy from sunlight. "
        f"According to the ecological **10% energy transfer rule**, approximately how much energy is transferred to the primary consumers (herbivores), "
        f"and why is roughly 90% of the energy lost between trophic levels?"
    )
    correct = (
        f"Approximately {herbivore_energy} kJ is transferred (10%); the remaining ~90% is lost as metabolic heat during cellular respiration, "
        f"movement, undigested excretions, and unconsumed plant parts."
    )
    options = [
        correct,
        f"Exactly {producer_energy} kJ is transferred because energy is 100% indestructible in ecosystems.",
        f"Zero energy is transferred because plants retain all energy forever without being digested.",
        f"Approximately {producer_energy * 2} kJ is created out of nothing by the herbivores.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Apply Lindeman's 10% efficiency rule:\n"
        f"- Energy transfer between trophic levels is roughly 10%:\n"
        f"  - Producers: {producer_energy} kJ\n"
        f"  - Primary consumers (herbivores): {producer_energy} * 0.10 = **{herbivore_energy} kJ**\n"
        f"  - Secondary consumers: {carnivore_energy} kJ\n"
        f"  - Tertiary consumers: {apex_energy} kJ\n"
        f"- The ~90% loss occurs because organisms expend energy on life processes (respiration, muscle movement, heat dissipation) or lose it in feces and uneaten bones/roots.\n\n"
        f"**Step 2:** The answer is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_18_{rng.randint(100000, 999999)}",
        "subskill": "18_pyramid_of_energy_and_the_ten_percent_energy_rule",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "hints": {
            "tier_1": f"Calculate 10% of {producer_energy} kJ.",
            "tier_2": f"10% of {producer_energy} is {herbivore_energy} kJ.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ten_percent_energy_rule_misconception"],
    }


# 19. Pyramid of numbers inverted vs upright
def arch_19_pyramid_of_numbers_inverted_vs_upright(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("a single massive indigenous oak tree supporting 10 000 herbivorous caterpillars, which support 50 small birds, which support 1 sparrowhawk", "an inverted base (1 single producer supporting thousands of primary consumers)"),
        ("a million blades of savanna grass supporting 500 impala, which support 2 cheetahs", "a standard upright pyramid of numbers (many producers supporting fewer consumers)"),
    ]
    case_desc, pyramid_shape = rng.choice(cases)
    prompt = (
        f"Consider the ecological scenario: {case_desc}.\n\n"
        f"What shape does a **pyramid of numbers** take in this specific community, and why?"
    )
    correct = f"It has {pyramid_shape}."
    options = [
        correct,
        "It forms a circular ring that spins continuously due to magnetic fields.",
        "It forms an invisible cloud because numbers cannot be plotted in science.",
        "It takes zero shape because all animals in the community instantly perish.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the counting of individual organisms:\n"
        f"- Unlike pyramids of energy (which are ALWAYS upright), pyramids of numbers simply count individual heads regardless of physical size.\n"
        f"- In a tree ecosystem: 1 single tree (producer) supports thousands of caterpillars -> the base is a narrow point of 1, resulting in an inverted base.\n"
        f"- In a grassland: millions of grass plants support fewer impala -> standard upright pyramid.\n\n"
        f"**Step 2:** For this scenario: **{correct}**."
    )
    return {
        "id": f"ns8_eco_19_{rng.randint(100000, 999999)}",
        "subskill": "19_pyramid_of_numbers_inverted_vs_upright",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Can a single large tree feed thousands of tiny caterpillars? Yes.",
            "tier_2": f"This creates {pyramid_shape}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pyramid_of_numbers_inversion_misconception"],
    }


# 20. Pyramid of biomass dry mass distribution
def arch_20_pyramid_of_biomass_dry_mass_distribution(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Ecologists often construct a **pyramid of biomass** by measuring the total dry organic mass "
        f"of all living organisms at each trophic level (in grams or kilograms per square metre).\n\n"
        f"Why is **dry biomass** measured instead of wet (fresh) body mass in accurate ecological studies?"
    )
    correct = (
        "Water content varies wildly between different organisms and fluctuates daily with hydration, "
        "whereas dry mass measures the actual organic chemical matter and stored energy."
    )
    options = [
        correct,
        "Because water possesses zero weight and cannot be measured on any laboratory scale.",
        "Because wet organisms explode when placed on measuring balances.",
        "Because ecologists are not allowed to touch water under laboratory safety protocols.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand why dry mass is used in biomass pyramids:\n"
        f"- A jellyfish is 95% water; an acacia branch is only 40% water.\n"
        f"- Water contains zero chemical potential energy for nutrition.\n"
        f"- Drying specimens to constant mass removes water variation, revealing the true quantity of organic biological matter (proteins, carbohydrates, lipids).\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_20_{rng.randint(100000, 999999)}",
        "subskill": "20_pyramid_of_biomass_dry_mass_distribution",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does water contain calories or nutritional energy? No.",
            "tier_2": "Dry mass measures true organic matter without the variable weight of water.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["dry_biomass_measurement_misconception"],
    }


# 21. Symbiosis mutualism in South African ecosystems
def arch_21_symbiosis_mutualism_in_south_african_ecosystems(rng: random.Random) -> Dict[str, Any]:
    mutualisms = [
        ("red-billed oxpeckers (*Buphagus erythrorynchus*) and African buffalo (*Syncerus caffer*)", "the oxpecker eats blood-sucking ticks and parasites off the buffalo's hide (gaining nutritious food), while the buffalo is freed from painful, disease-carrying ectoparasites"),
        ("nitrogen-fixing *Rhizobium* bacteria in root nodules of indigenous rooibos legumes", "the bacteria convert atmospheric nitrogen into usable nitrates for the plant, while the plant supplies the bacteria with organic sugars and protective shelter"),
        ("Cape sugarbirds (*Promerops cafer*) and king proteas (*Protea cynaroides*)", "the sugarbird obtains energy-rich nectar to drink, while simultaneously transferring pollen grains on its head feathers to cross-pollinate the protea flowers"),
    ]
    pair, description = rng.choice(mutualisms)
    prompt = (
        f"Consider the ecological relationship between {pair}: {description}.\n\n"
        f"What form of symbiotic relationship (+ / +) does this interaction represent, and why?"
    )
    correct = "Mutualism, because both species derive clear biological benefits from the interaction."
    options = [
        correct,
        "Parasitism, because one organism slowly murders the other for sport.",
        "Commensalism, because one organism benefits while the other is completely destroyed.",
        "Amensalism, because both organisms die within 5 seconds of touching each other.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define mutualism (+/+):\n"
        f"- Mutualism is a close, prolonged symbiotic association in which both participating species gain fitness, survival, or reproductive advantages.\n"
        f"- In this partnership: {description}.\n\n"
        f"**Step 2:** The relationship is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_21_{rng.randint(100000, 999999)}",
        "subskill": "21_symbiosis_mutualism_in_south_african_ecosystems",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Do both species benefit, or does one get harmed?",
            "tier_2": "When both species benefit (+/+), it is called mutualism.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mutualism_symbiosis_misconception"],
    }


# 22. Symbiosis commensalism examples and mechanisms
def arch_22_symbiosis_commensalism_examples_and_mechanisms(rng: random.Random) -> Dict[str, Any]:
    commensalisms = [
        ("remora suckerfish (Echeneidae) attaching to the belly of a ragged-tooth shark", "the remora gains free transportation and feeds on scraps of food dropped by the shark, while the shark is unaffected and neither harmed nor benefited (+ / 0)"),
        ("epiphytic tree orchids growing high on the rough bark of yellowwood trees", "the orchid gains physical support and elevation to access sunlight without taking any sap or nutrients from the tree, while the tree is unaffected (+ / 0)"),
        ("cattle egrets (*Bubulcus ibis*) foraging alongside grazing zebras", "the egret eats insects flushed out of the grass by the moving zebra hooves, while the zebra is neither helped nor harmed (+ / 0)"),
    ]
    pair, details = rng.choice(commensalisms)
    prompt = (
        f"Consider the interaction between {pair}: {details}.\n\n"
        f"What ecological term describes this symbiotic relationship where one species benefits while the other is unaffected (+ / 0)?"
    )
    correct = "Commensalism"
    options = [
        correct,
        "Parasitism",
        "Predation",
        "Mutualism",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define commensalism (+/0):\n"
        f"- Commensalism is a symbiotic relationship where one organism benefits while the other host organism is neither harmed nor helped.\n"
        f"- In this scenario: {details}.\n\n"
        f"**Step 2:** The term is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_22_{rng.randint(100000, 999999)}",
        "subskill": "22_symbiosis_commensalism_examples_and_mechanisms",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "One organism benefits while the other is unaffected (+/0). What is this called?",
            "tier_2": "This relationship is called commensalism.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["commensalism_definition_misconception"],
    }


# 23. Symbiosis parasitism ectoparasites vs endoparasites
def arch_23_symbiosis_parasitism_ectoparasites_vs_endoparasites(rng: random.Random) -> Dict[str, Any]:
    parasites = [
        ("ticks (e.g. the bont tick *Amblyomma hebraeum*) feeding externally on cattle skin", "Ectoparasite (living and feeding on the external surface of the host)"),
        ("tapeworms (*Taenia*) living inside the intestine of a mammal absorbing digested food", "Endoparasite (living and feeding inside the internal organs of the host)"),
        ("flea (*Ctenocephalides*) living in the fur of an African wild dog", "Ectoparasite (living externally on the host's body)"),
        ("roundworms (*Ascaris*) inhabiting the human digestive tract", "Endoparasite (living internally within the host's body)"),
    ]
    example, classification = rng.choice(parasites)
    prompt = (
        f"Consider the parasite: **{example}**.\n\n"
        f"How is this organism classified based on where it lives relative to its host in a parasitic relationship (+ / -)?"
    )
    correct = classification
    options = [
        correct,
        "Autotrophic primary producer converting solar rays to sugar",
        "Free-living decomposer breaking down granite rock",
        "Mutualistic partner that gives the host gold and energy",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish ectoparasites vs endoparasites:\n"
        f"- Parasitism (+/-): the parasite benefits by taking nutrients at the expense of the host, which is harmed.\n"
        f"- Ectoparasites: live on the *outside* of the host (ticks, fleas, lice, mosquitoes).\n"
        f"- Endoparasites: live on the *inside* of the host's body (tapeworms, hookworms, malaria parasites).\n\n"
        f"**Step 2:** For this example: **{correct}**."
    )
    return {
        "id": f"ns8_eco_23_{rng.randint(100000, 999999)}",
        "subskill": "23_symbiosis_parasitism_ectoparasites_vs_endoparasites",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does it live on the outside (ecto-) or on the inside (endo-) of the host?",
            "tier_2": f"It is classified as an {classification.split()[0].lower()}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ectoparasite_endoparasite_distinction_misconception"],
    }


# 24. Predator prey interactions and population cycles (with dynamic SVG)
def arch_24_predator_prey_interactions_and_population_cycles(rng: random.Random) -> Dict[str, Any]:
    prey_peak = rng.randint(450, 550)
    pred_peak = rng.randint(75, 95)
    lag_years = rng.choice([1, 2])

    svg = (
        f'<svg viewBox="0 0 440 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="220" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Predator-Prey Population Oscillations</text>'
        f'<line x1="50" y1="180" x2="400" y2="180" stroke="#64748b" stroke-width="2" />'
        f'<line x1="50" y1="180" x2="50" y2="40" stroke="#64748b" stroke-width="2" />'
        f'<path d="M 60 140 Q 110 50 160 140 T 260 140 T 360 140" fill="none" stroke="#2563eb" stroke-width="2.5" />'
        f'<text x="110" y="45" font-size="10" fill="#1d4ed8" font-weight="bold">Prey (Peak ~{prey_peak})</text>'
        f'<path d="M 80 160 Q 130 90 180 160 T 280 160 T 380 160" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="4,2" />'
        f'<text x="150" y="85" font-size="10" fill="#b91c1c" font-weight="bold">Predator (Peak ~{pred_peak})</text>'
        f'<text x="220" y="205" font-size="10" fill="#475569" text-anchor="middle">Predator peak lags {lag_years} year(s) behind the prey population peak</text>'
        f'</svg>'
    )

    prompt = (
        f"Ecological field data tracking an impala population (prey) and a wild dog pack (predator) over a 20-year period "
        f"reveals coupled cyclical oscillations where the predator population peak consistently lags {lag_years} year(s) behind the prey peak.\n\n"
        f"Why does the predator population peak lag behind the prey population peak?"
    )
    correct = (
        "Predators require time to reproduce and raise offspring after an abundance of prey food becomes available, "
        "and conversely take time to starve and decline after prey numbers crash."
    )
    options = [
        correct,
        "Predators intentionally hibernate for 10 years to let prey play games in safety.",
        "Prey animals transform into predators whenever their population gets too large.",
        "The lunar tidal cycles force all carnivores to stop hunting during odd-numbered years.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the lag phase in predator-prey dynamics:\n"
        f"- When prey population surges, abundant food allows predators to successfully breed, rear litters, and increase in numbers.\n"
        f"- This gestation and maturation creates a demographic time lag ({lag_years} years).\n"
        f"- As predator numbers peak, high predation pressure drives prey numbers down, which subsequently causes predator numbers to crash from starvation.\n\n"
        f"**Step 2:** The reason is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_24_{rng.randint(100000, 999999)}",
        "subskill": "24_predator_prey_interactions_and_population_cycles",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "hints": {
            "tier_1": "Can predators instantly multiply the moment more food arrives, or does reproduction take time?",
            "tier_2": "Breeding and maturation cause a time lag behind the prey peak.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["predator_prey_lag_misconception"],
    }


# 25. Competition intraspecific vs interspecific for resources
def arch_25_competition_intraspecific_vs_interspecific_for_resources(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Two male impala (*Aepyceros melampus*) locking horns in violent combat to defend a breeding territory and mate with a harem of females", "Intraspecific competition", "between individuals of the same species for mates and territory"),
        ("Lions and spotted hyenas fighting over the same freshly killed zebra carcass at a savanna waterhole", "Interspecific competition", "between individuals of two different species for the same limited food resource"),
        ("Seedlings of black wattle trees growing densely packed together, competing for sunlight, soil water, and root space", "Intraspecific competition", "between individuals of the same plant species competing for essential growth resources"),
        ("Cape sugarbirds and malachite sunbirds competing for nectar from the same flowering *Protea* shrubs", "Interspecific competition", "between individuals of different bird species for the same floral food supply"),
    ]
    event, competition_type, justification = rng.choice(scenarios)
    prompt = (
        f"Consider the ecological interaction: **{event}**.\n\n"
        f"How is this form of ecological competition classified, and what is the scientific justification?"
    )
    correct = f"{competition_type}, because it occurs {justification}."
    options = [
        correct,
        f"{competition_type}, because both organisms are non-living abiotic rocks.",
        "Non-biological competition, because animals never compete for resources in nature.",
        "Mutualistic cooperation, because both organisms share the resource with complete peace and zero stress.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish intraspecific from interspecific competition:\n"
        f"- Intraspecific: competition among members of the *same* species (often extremely intense because individuals have identical ecological niches and needs, including mates).\n"
        f"- Interspecific: competition between members of *different* species for overlapping shared resources (food, water, territory).\n\n"
        f"**Step 2:** For this case: **{correct}**."
    )
    return {
        "id": f"ns8_eco_25_{rng.randint(100000, 999999)}",
        "subskill": "25_competition_intraspecific_vs_interspecific_for_resources",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Are the competing organisms of the same species (intra-) or different species (inter-)?",
            "tier_2": f"This is {competition_type.lower()}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["intra_vs_inter_specific_competition_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "01_levels_of_ecological_organisation_hierarchy": arch_01_levels_of_ecological_organisation_hierarchy,
    "02_population_definition_and_characteristics": arch_02_population_definition_and_characteristics,
    "03_community_definition_and_species_assemblage": arch_03_community_definition_and_species_assemblage,
    "04_ecosystem_definition_biotic_and_abiotic_synthesis": arch_04_ecosystem_definition_biotic_and_abiotic_synthesis,
    "05_biosphere_scope_and_global_life_zone": arch_05_biosphere_scope_and_global_life_zone,
    "06_abiotic_factors_edaphic_soil_properties": arch_06_abiotic_factors_edaphic_soil_properties,
    "07_abiotic_factors_physiographic_aspect_and_slope": arch_07_abiotic_factors_physiographic_aspect_and_slope,
    "08_abiotic_factors_light_intensity_and_photoperiod": arch_08_abiotic_factors_light_intensity_and_photoperiod,
    "09_abiotic_factors_temperature_and_water_availability": arch_09_abiotic_factors_temperature_and_water_availability,
    "10_producers_autotrophs_converting_solar_energy": arch_10_producers_autotrophs_converting_solar_energy,
    "11_consumers_herbivores_primary_consumers": arch_11_consumers_herbivores_primary_consumers,
    "12_consumers_carnivores_secondary_and_tertiary": arch_12_consumers_carnivores_secondary_and_tertiary,
    "13_consumers_omnivores_and_scavengers": arch_13_consumers_omnivores_and_scavengers,
    "14_decomposers_bacteria_and_fungi_nutrient_recycling": arch_14_decomposers_bacteria_and_fungi_nutrient_recycling,
    "15_food_chain_construction_and_arrow_direction_energy_flow": arch_15_food_chain_construction_and_arrow_direction_energy_flow,
    "16_food_web_analysis_interpreting_interconnected_chains": arch_16_food_web_analysis_interpreting_interconnected_chains,
    "17_trophic_levels_identifying_positions_in_food_webs": arch_17_trophic_levels_identifying_positions_in_food_webs,
    "18_pyramid_of_energy_and_the_ten_percent_energy_rule": arch_18_pyramid_of_energy_and_the_ten_percent_energy_rule,
    "19_pyramid_of_numbers_inverted_vs_upright": arch_19_pyramid_of_numbers_inverted_vs_upright,
    "20_pyramid_of_biomass_dry_mass_distribution": arch_20_pyramid_of_biomass_dry_mass_distribution,
    "21_symbiosis_mutualism_in_south_african_ecosystems": arch_21_symbiosis_mutualism_in_south_african_ecosystems,
    "22_symbiosis_commensalism_examples_and_mechanisms": arch_22_symbiosis_commensalism_examples_and_mechanisms,
    "23_symbiosis_parasitism_ectoparasites_vs_endoparasites": arch_23_symbiosis_parasitism_ectoparasites_vs_endoparasites,
    "24_predator_prey_interactions_and_population_cycles": arch_24_predator_prey_interactions_and_population_cycles,
    "25_competition_intraspecific_vs_interspecific_for_resources": arch_25_competition_intraspecific_vs_interspecific_for_resources,
}
