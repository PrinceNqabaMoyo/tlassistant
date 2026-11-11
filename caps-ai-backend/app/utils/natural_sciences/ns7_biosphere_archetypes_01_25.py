"""Grade 7 Natural Sciences: Term 1 - The Biosphere (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/01. The Biosphere.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Biosphere definition and scope
def arch_01_biosphere_definition_and_scope(rng: random.Random) -> Dict[str, Any]:
    scopes = [
        ("the global ecological zone where all living organisms interact with abiotic components across Earth", "The Biosphere"),
        ("the continuous blanket of gases and air enclosing the Earth", "The Atmosphere"),
        ("the combined reservoir of liquid water, ice caps, and underground water tables", "The Hydrosphere"),
        ("the brittle rocky outer crust and upper mantle forming continents and sea floors", "The Lithosphere"),
    ]
    desc, term = rng.choice(scopes)
    prompt = f"In South African Natural Sciences, which term specifically designates {desc}?"
    correct = term
    options = [term] + [s[1] for s in scopes if s[1] != term]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall the primary spheres of Earth:\n"
        f"- Biosphere: The global zone of all life on Earth interacting with non-living elements.\n"
        f"- Atmosphere: The gaseous envelope.\n"
        f"- Hydrosphere: All water reserves.\n"
        f"- Lithosphere: The solid rocky crust and upper mantle.\n\n"
        f"**Step 2:** {desc} defines **{term}**."
    )
    return {
        "id": f"ns7_bio_01_{rng.randint(100000, 999999)}",
        "subskill": "01_biosphere_definition_and_scope",
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
            "tier_1": "Recall the Greek roots: 'Bio' means life, 'Hydro' means water, 'Litho' means stone, 'Atmo' means air.",
            "tier_2": "Look at the key elements in the definition: living organisms vs rocks vs water vs air.",
            "tier_3": f"The term matching this definition is {term}.",
        },
        "misconception_tags": ["sphere_interchange_error"],
    }


# 02. Atmosphere composition and function
def arch_02_atmosphere_composition_and_function(rng: random.Random) -> Dict[str, Any]:
    gas_data = [
        ("Nitrogen (N2)", "approximately 78%", "diluting oxygen to prevent rapid combustion and providing an essential nutrient for plant growth via fixation"),
        ("Oxygen (O2)", "approximately 21%", "supporting cellular respiration in aerobic organisms and supporting combustion"),
        ("Carbon dioxide (CO2)", "approximately 0.04%", "acting as the carbon source for green plant photosynthesis and contributing to natural greenhouse heat trapping"),
        ("Ozone (O3)", "trace amounts in the stratosphere", "absorbing harmful high-energy ultraviolet (UV) solar radiation that damages DNA in living cells"),
    ]
    gas, percentage, role = rng.choice(gas_data)
    prompt = (
        f"In Earth's atmosphere, which gas accounts for {percentage} and has the primary ecological role of {role}?"
    )
    correct = gas
    options = [gas] + [g[0] for g in gas_data if g[0] != gas]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review atmospheric gas proportions and roles:\n"
        f"- Nitrogen: ~78% of dry air.\n"
        f"- Oxygen: ~21% of dry air, essential for respiration.\n"
        f"- Carbon dioxide: ~0.04% of dry air, essential for photosynthesis.\n"
        f"- Ozone: stratospheric gas shielding against UV rays.\n\n"
        f"**Step 2:** The gas described ({percentage}; {role}) is **{gas}**."
    )
    return {
        "id": f"ns7_bio_02_{rng.randint(100000, 999999)}",
        "subskill": "02_atmosphere_composition_and_function",
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
            "tier_1": "Recall the major percentages in air: 78% is nitrogen, 21% is oxygen, and 0.04% is carbon dioxide.",
            "tier_2": "Match the percentage and biological purpose directly to the gas.",
            "tier_3": f"The answer is {gas}.",
        },
        "misconception_tags": ["atmospheric_gas_confusion"],
    }


# 03. Hydrosphere distribution and water cycle
def arch_03_hydrosphere_distribution_and_water_cycle(rng: random.Random) -> Dict[str, Any]:
    stages = [
        ("Evaporation", "Liquid surface water from dams, oceans, and rivers gains thermal energy and turns into invisible water vapour gas."),
        ("Transpiration", "Plants absorb water through roots and release water vapour into the atmosphere through microscopic leaf stomata."),
        ("Condensation", "Rising water vapour cools at higher altitudes and transforms into tiny liquid water droplets forming clouds."),
        ("Precipitation", "Water droplets in clouds become too heavy to remain suspended and fall back to the ground as rain, hail, or snow."),
        ("Infiltration and Percolation", "Rainwater seeps down through soil layers and porous rock to replenish underground aquifers and groundwater reserves."),
    ]
    term, desc = rng.choice(stages)
    prompt = (
        f"Within the water cycle that sustains Earth's hydrosphere, which physical process occurs when {desc.lower()}?"
    )
    correct = term
    options = [term] + [s[0] for s in stages if s[0] != term]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the water cycle stage:\n"
        f"- Evaporation: liquid water to vapour by heat.\n"
        f"- Transpiration: water vapour release through plant leaves.\n"
        f"- Condensation: vapour cooling into clouds.\n"
        f"- Precipitation: rain/snow falling to surface.\n"
        f"- Infiltration: water soaking into soil/aquifers.\n\n"
        f"**Step 2:** The described process is **{term}**."
    )
    return {
        "id": f"ns7_bio_03_{rng.randint(100000, 999999)}",
        "subskill": "03_hydrosphere_distribution_and_water_cycle",
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
            "tier_1": "Consider whether water is changing phase (liquid to gas, gas to liquid) or moving through living tissue.",
            "tier_2": "Pay close attention to whether the process involves plants (transpiration), cloud formation (condensation), or falling rain (precipitation).",
            "tier_3": f"The stage described is {term}.",
        },
        "misconception_tags": ["water_cycle_stage_confusion"],
    }


# 04. Lithosphere soil and mineral foundation
def arch_04_lithosphere_soil_and_mineral_foundation(rng: random.Random) -> Dict[str, Any]:
    depth_a = rng.randint(15, 30)
    depth_b = rng.randint(35, 60)
    depth_c = rng.randint(70, 110)
    horizons = [
        ("Topsoil (Horizon A)", f"0 to {depth_a} cm", "dark, rich in decomposed organic humus and microorganisms, essential for root development and crop cultivation"),
        ("Subsoil (Horizon B)", f"{depth_a} to {depth_b} cm", "lighter colour, richer in accumulated clays and leached mineral salts with very little organic matter"),
        ("Weathered parent rock (Horizon C)", f"{depth_b} to {depth_c} cm", "partially disintegrated bedrock chunks undergoing initial mechanical and chemical weathering"),
        ("Solid bedrock (Horizon R)", f"below {depth_c} cm", "unweathered solid foundation rock forming the continuous crust of the lithosphere"),
    ]
    target_layer, range_cm, description = rng.choice(horizons)
    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 240' width='100%' height='240'>"
        f"<rect width='400' height='240' fill='#F5F0EB' rx='8'/>"
        f"<rect x='30' y='20' width='340' height='40' fill='#4E3629'/>"
        f"<text x='40' y='45' fill='#FFFFFF' font-size='12' font-weight='bold'>Topsoil (Horizon A): 0-{depth_a} cm</text>"
        f"<rect x='30' y='65' width='340' height='50' fill='#A06535'/>"
        f"<text x='40' y='95' fill='#FFFFFF' font-size='12' font-weight='bold'>Subsoil (Horizon B): {depth_a}-{depth_b} cm</text>"
        f"<rect x='30' y='120' width='340' height='55' fill='#C89D7C'/>"
        f"<text x='40' y='152' fill='#2C2C2C' font-size='12' font-weight='bold'>Parent Rock (Horizon C): {depth_b}-{depth_c} cm</text>"
        f"<rect x='30' y='180' width='340' height='45' fill='#7A7A7A'/>"
        f"<text x='40' y='208' fill='#FFFFFF' font-size='12' font-weight='bold'>Bedrock (Horizon R): &gt;{depth_c} cm</text>"
        f"</svg>"
    )
    prompt = (
        f"In the lithosphere, soil horizons develop through weathering and biological action. "
        f"Identify the soil horizon that spans {range_cm} and is characterized as {description}."
    )
    correct = target_layer
    options = [target_layer] + [h[0] for h in horizons if h[0] != target_layer]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze soil horizons in the lithosphere:\n"
        f"- Topsoil (Horizon A): Humus-rich, 0 to {depth_a} cm, vital for plant roots.\n"
        f"- Subsoil (Horizon B): Mineral and clay accumulation, {depth_a} to {depth_b} cm.\n"
        f"- Horizon C: Weathered rock fragments, {depth_b} to {depth_c} cm.\n"
        f"- Bedrock (Horizon R): Solid unweathered rock.\n\n"
        f"**Step 2:** The horizon described is **{target_layer}**."
    )
    return {
        "id": f"ns7_bio_04_{rng.randint(100000, 999999)}",
        "subskill": "04_lithosphere_soil_and_mineral_foundation",
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
            "tier_1": "Recall which layer contains the most humus and dark organic matter.",
            "tier_2": "Horizon A is nearest the surface, Horizon B sits beneath it, and Horizon C is deeper near bedrock.",
            "tier_3": f"The correct layer is {target_layer}.",
        },
        "misconception_tags": ["soil_horizon_reversal"],
    }


# 05. Interlocking spheres ecological interaction
def arch_05_interlocking_spheres_ecological_interaction(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "An acacia tree in the Kruger National Park absorbs mineral nitrates dissolved in groundwater from soil, absorbs sunlight and atmospheric carbon dioxide, and releases water vapour through its leaves.",
            "Biosphere (tree) interacting with Lithosphere (soil nitrates), Hydrosphere (groundwater), and Atmosphere (carbon dioxide and water vapour)",
        ),
        (
            "A Cape clawless otter digs into riverbed gravel to catch freshwater crabs and surfaces into the air to breathe oxygen.",
            "Biosphere (otter and crabs) interacting with Lithosphere (gravel), Hydrosphere (river water), and Atmosphere (oxygen gas)",
        ),
        (
            "Volcanic lava in an ocean ridge cools into new basalt rock, releasing steam and sulfurous gases that marine chemosynthetic bacteria use as nutrients.",
            "Lithosphere (basalt rock and volcanic vent) interacting with Hydrosphere (ocean water), Atmosphere (volcanic gases), and Biosphere (bacteria)",
        ),
    ]
    scene, answer = rng.choice(scenarios)
    prompt = (
        f"Read the following ecological observation:\n"
        f"\"{scene}\"\n\n"
        f"Which statement correctly traces how Earth's four spheres interlock in this scenario?"
    )
    correct = answer
    distractors = [
        "Only the Biosphere is involved because living organisms operate completely independently of abiotic factors.",
        "Only the Atmosphere and Hydrosphere interact; the Lithosphere plays no role in supporting living organisms.",
        "The Biosphere is replaced by non-living matter whenever organisms absorb water or gases.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Break down each component of the observation:\n"
        f"- Organisms represent the Biosphere.\n"
        f"- Water and aquatic medium represent the Hydrosphere.\n"
        f"- Soil, stones, gravel, and rock represent the Lithosphere.\n"
        f"- Ambient air and dissolved gases represent the Atmosphere.\n\n"
        f"**Step 2:** Therefore, the interaction is correctly described as: **{answer}**."
    )
    return {
        "id": f"ns7_bio_05_{rng.randint(100000, 999999)}",
        "subskill": "05_interlocking_spheres_ecological_interaction",
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
            "tier_1": "Identify which parts of the scenario belong to air, water, rock/soil, and living organisms.",
            "tier_2": "Living things rely simultaneously on all three abiotic spheres for survival.",
            "tier_3": f"The correct interaction is: {answer}.",
        },
        "misconception_tags": ["sphere_isolation_misconception"],
    }


# 06. Distinguish living, nonliving, dead matter
def arch_06_distinguish_living_nonliving_dead_matter(rng: random.Random) -> Dict[str, Any]:
    items = [
        ("A fallen dried protea leaf on the forest floor", "Once-living (dead organic matter)", "it was once part of an active organism performing life processes, but its cells have permanently ceased metabolism"),
        ("A piece of granite rock found on Table Mountain", "Non-living (abiotic matter)", "it was formed by geological magma cooling and has never possessed cells or life processes"),
        ("An active nitrogen-fixing bacterium in root nodules", "Living organism", "it actively carries out all seven life processes including cellular respiration, growth, and reproduction"),
        ("A wooden dining table made from indigenous stinkwood", "Once-living (dead organic matter)", "it is composed of xylem tissue from a tree that was once alive and metabolizing"),
        ("Pure river sand composed of tiny quartz crystals", "Non-living (abiotic matter)", "it consists of mineral silica crystals that have never been part of an organism"),
    ]
    item_name, category, reasoning = rng.choice(items)
    prompt = (
        f"Natural Sciences classifies objects as living organisms, once-living (dead) matter, or non-living abiotic matter. "
        f"How should '{item_name}' be classified, and what is the scientific justification?"
    )
    correct = f"{category} — because {reasoning}"
    distractors = [
        f"Living organism — because '{item_name}' absorbs solar radiation and changes temperature daily.",
        f"Non-living (abiotic matter) — because once an object stops moving it permanently converts into a geological mineral.",
        f"Once-living (dead organic matter) — because all substances on Earth originated from ancient bacteria millions of years ago.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Apply CAPS biological classification rules:\n"
        f"- Living: exhibits all 7 life processes (MRS GREN).\n"
        f"- Once-living (dead): was once alive or produced by living tissue, but life processes have ceased.\n"
        f"- Non-living: abiotic mineral or element that was never alive.\n\n"
        f"**Step 2:** '{item_name}' is classified as **{category}** because {reasoning}."
    )
    return {
        "id": f"ns7_bio_06_{rng.randint(100000, 999999)}",
        "subskill": "06_distinguish_living_nonliving_dead_matter",
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
            "tier_1": "Ask: Was this object ever part of a living plant or animal, or is it pure mineral?",
            "tier_2": "Dead wood, dried leaves, and bone are once-living; rocks, water, and sand are non-living.",
            "tier_3": f"The correct answer is: {correct}.",
        },
        "misconception_tags": ["dead_vs_nonliving_confusion"],
    }


# 07. Life process movement plants vs animals
def arch_07_life_process_movement_plants_vs_animals(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("a cheetah chasing a gazelle across the savanna", "Locomotion: whole-body movement from one location to another powered by muscular and skeletal systems"),
        ("a sunflower head turning slowly from east to west following the arc of the sun", "Phototropism: directional growth movement of plant parts in response to the light stimulus"),
        ("the roots of a maize seedling growing downward into moist soil", "Geotropism (gravitropism): directional growth movement oriented toward gravitational pull"),
        ("a fly catching leaf of a sundew plant curling inwards when touched by an insect", "Thigmonasty: rapid turgor-driven movement of specialized plant organs in response to tactile contact"),
    ]
    example, explanation = rng.choice(cases)
    prompt = (
        f"Movement is one of the seven life processes of living organisms. "
        f"Consider the observation of {example}. "
        f"Which statement scientifically explains how movement operates in this organism?"
    )
    correct = explanation
    options = [explanation] + [c[1] for c in cases if c[1] != explanation]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare movement in plants and animals:\n"
        f"- Animals display locomotion (moving their whole body from place to place).\n"
        f"- Plants do not display locomotion, but exhibit movement through differential growth (tropisms) or turgor pressure changes (nastic movements).\n\n"
        f"**Step 2:** The observation of {example} represents **{explanation}**."
    )
    return {
        "id": f"ns7_bio_07_{rng.randint(100000, 999999)}",
        "subskill": "07_life_process_movement_plants_vs_animals",
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
            "tier_1": "Recall whether plants can move even though they are rooted in the soil.",
            "tier_2": "Plants show movement by growing towards or away from stimuli like light or gravity.",
            "tier_3": f"The correct explanation is: {explanation}.",
        },
        "misconception_tags": ["plants_cannot_move_misconception"],
    }


# 08. Life process cellular respiration vs breathing
def arch_08_life_process_cellular_respiration_vs_breathing(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Cellular respiration", "A biochemical reaction inside every living cell (mitochondria) where glucose is broken down with oxygen to release energy (ATP), carbon dioxide, and water."),
        ("Breathing (ventilation)", "The physical mechanical process of inhaling air into lungs and exhaling air out of the body to exchange gases."),
    ]
    target, correct_def = rng.choice(pairs)
    alt = pairs[1] if target == pairs[0][0] else pairs[0]
    prompt = (
        f"Learners often confuse breathing with cellular respiration. "
        f"What is the accurate scientific definition of '{target}' in living organisms?"
    )
    correct = correct_def
    options = [
        correct_def,
        alt[1],
        "The absorption of water by plant roots to maintain turgor pressure inside vascular bundles.",
        "The conversion of oxygen into sunlight inside plant chloroplasts during night-time hours.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Clarify the distinction:\n"
        f"- Breathing = physical pumping of air in and out of respiratory organs (lungs, gills).\n"
        f"- Cellular respiration = chemical reaction in cells releasing energy from food molecules (glucose + O2 -> CO2 + H2O + energy).\n\n"
        f"**Step 2:** The definition of '{target}' is: **{correct_def}**."
    )
    return {
        "id": f"ns7_bio_08_{rng.randint(100000, 999999)}",
        "subskill": "08_life_process_cellular_respiration_vs_breathing",
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
            "tier_1": "Remember that cellular respiration is a chemical reaction occurring inside cells, while breathing is mechanical.",
            "tier_2": "Plants do not breathe with lungs, yet every plant cell performs cellular respiration.",
            "tier_3": f"The answer is: {correct_def}.",
        },
        "misconception_tags": ["breathing_respiration_conflation"],
    }


# 09. Life process sensitivity and stimulus response
def arch_09_life_process_sensitivity_and_stimulus_response(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("A learner touches a hot stove plate and immediately jerks their hand away before feeling severe pain.", "Thermal and pain stimuli detected by skin receptors triggering an involuntary reflex response"),
        ("An earthworm exposed to bright light on garden soil burrowing rapidly into dark moist earth.", "Light (phototactic) stimulus detected by light-sensitive epidermal cells triggering negative phototaxis"),
        ("A chameleon changing skin pigmentation and turning sideways toward a predator.", "Visual threat stimulus processed by the nervous system triggering a defensive camouflaging response"),
        ("A dog salivating when smelling meat being cooked in the kitchen.", "Chemical odour stimulus detected by olfactory sensory cells triggering an anticipatory digestive response"),
    ]
    scenario, mechanism = rng.choice(examples)
    prompt = (
        f"Sensitivity (irritability) is the life process enabling organisms to detect and respond to environmental changes. "
        f"Analyze this observation: \"{scenario}\"\n\n"
        f"Which option accurately identifies the stimulus and the biological response?"
    )
    correct = mechanism
    options = [mechanism] + [e[1] for e in examples if e[1] != mechanism]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define stimulus and response:\n"
        f"- Stimulus: A detectable change in the internal or external environment.\n"
        f"- Response: The action or adjustment made by the organism.\n\n"
        f"**Step 2:** In the given scenario, the mechanism is: **{mechanism}**."
    )
    return {
        "id": f"ns7_bio_09_{rng.randint(100000, 999999)}",
        "subskill": "09_life_process_sensitivity_and_stimulus_response",
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
            "tier_1": "Separate the cause (stimulus) from the effect (response).",
            "tier_2": "Identify what environmental change the sensory organs detected.",
            "tier_3": f"The correct stimulus-response mechanism is: {mechanism}.",
        },
        "misconception_tags": ["stimulus_response_inversion"],
    }


# 10. Life process growth and development
def arch_10_life_process_growth_and_development(rng: random.Random) -> Dict[str, Any]:
    days = rng.randint(7, 21)
    seed_mass_initial = rng.randint(2, 5)
    seed_mass_final = seed_mass_initial * rng.randint(4, 9)
    prompt = (
        f"A bean seed with an initial dry mass of {seed_mass_initial} g is planted in moist soil. "
        f"After {days} days, the resulting seedling has developed green leaves, stems, and fibrous roots with a dry mass of {seed_mass_final} g. "
        f"Why is biological growth defined as an 'irreversible increase in size and dry biomass' rather than merely swelling with water?"
    )
    correct = "Because it involves cell division (mitosis) and the permanent synthesis of new cellular structures and organic molecules from nutrients."
    options = [
        correct,
        "Because any object that absorbs liquid water has permanently grown into a larger organism.",
        "Because bean plants only grow during night hours when solar energy is absent.",
        "Because seed growth reverses completely back to the original seed mass if watering is stopped for one day.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall the scientific definition of growth in living organisms:\n"
        f"- True growth requires cell division (mitosis) and the building of new protoplasm, tissues, and cellular structures.\n"
        f"- Merely soaking up water (imbibition) is a reversible physical process, not true biological growth.\n\n"
        f"**Step 2:** The dry mass increased from {seed_mass_initial} g to {seed_mass_final} g due to cell division and organic synthesis."
    )
    return {
        "id": f"ns7_bio_10_{rng.randint(100000, 999999)}",
        "subskill": "10_life_process_growth_and_development",
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
            "tier_1": "Consider what happens inside cells during growth (cell division).",
            "tier_2": "Contrast true growth with a dry sponge swelling when placed in water.",
            "tier_3": "True growth requires the creation of new cells and organic biomass.",
        },
        "misconception_tags": ["water_absorption_as_growth"],
    }


# 11. Life process reproduction species survival
def arch_11_life_process_reproduction_species_survival(rng: random.Random) -> Dict[str, Any]:
    modes = [
        ("Sexual reproduction", "Involves the fusion of male and female gametes (sperm/pollen and egg/ovule), producing genetically varied offspring."),
        ("Asexual reproduction", "Involves a single parent organism producing offspring through cell division (budding, runners, binary fission) without gamete fusion, producing genetically identical clones."),
    ]
    target_mode, target_desc = rng.choice(modes)
    other_mode, other_desc = (modes[1] if target_mode == modes[0][0] else modes[0])
    prompt = (
        f"Reproduction is essential for the continuous survival of a species on Earth. "
        f"Which statement scientifically distinguishes '{target_mode}' from '{other_mode}'?"
    )
    correct = f"'{target_mode}' {target_desc.lower()}"
    options = [
        correct,
        f"'{target_mode}' is only found in non-living abiotic crystals.",
        f"'{target_mode}' prevents any offspring from inheriting characteristics from parent organisms.",
        f"'{target_mode}' requires three parent organisms belonging to different animal phyla.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare reproductive strategies:\n"
        f"- Sexual reproduction: Two gametes fuse, creating genetic variation in offspring.\n"
        f"- Asexual reproduction: Single parent produces genetically identical clones without gamete fusion.\n\n"
        f"**Step 2:** '{target_mode}' is accurately described: **{correct}**."
    )
    return {
        "id": f"ns7_bio_11_{rng.randint(100000, 999999)}",
        "subskill": "11_life_process_reproduction_species_survival",
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
            "tier_1": "Count how many parents and whether sex cells (gametes) are involved.",
            "tier_2": "Sexual reproduction generates variation; asexual reproduction creates clones.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["reproduction_mode_confusion"],
    }


# 12. Life process excretion vs egestion
def arch_12_life_process_excretion_vs_egestion(rng: random.Random) -> Dict[str, Any]:
    wastes = [
        ("Urea in urine excreted by mammalian kidneys", "Excretion: elimination of metabolic waste produced inside body cells from biochemical reactions"),
        ("Carbon dioxide exhaled from lungs during expiration", "Excretion: elimination of toxic metabolic waste produced by cellular respiration"),
        ("Excess water and mineral salts expelled through sweat glands", "Excretion: elimination of metabolic waste and thermal control byproduct"),
        ("Undigested food residues expelled as faeces from the anus", "Egestion (defaecation): removal of undigested dietary material that never entered body cells or participated in metabolism"),
    ]
    substance, classification = rng.choice(wastes)
    prompt = (
        f"Grade 7 learners frequently confuse excretion with egestion. "
        f"How should the removal of '{substance}' be scientifically classified?"
    )
    correct = classification
    options = [classification] + [w[1] for w in wastes if w[1] != classification]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Contrast excretion and egestion:\n"
        f"- Excretion = removal of wastes produced BY cellular metabolism (e.g. urea, CO2, sweat salts).\n"
        f"- Egestion = expulsion of unabsorbed food through the gut that never crossed cell membranes into metabolic pathways.\n\n"
        f"**Step 2:** '{substance}' is classified as: **{classification}**."
    )
    return {
        "id": f"ns7_bio_12_{rng.randint(100000, 999999)}",
        "subskill": "12_life_process_excretion_vs_egestion",
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
            "tier_1": "Ask: Was this waste made inside cells by a chemical reaction, or is it just undigested food?",
            "tier_2": "Undigested food passing out as faeces is egestion; metabolic wastes like urea and CO2 are excretion.",
            "tier_3": f"The correct classification is: {classification}.",
        },
        "misconception_tags": ["egestion_excretion_conflation"],
    }


# 13. Life process nutrition autotrophs vs heterotrophs
def arch_13_life_process_nutrition_autotrophs_vs_heterotrophs(rng: random.Random) -> Dict[str, Any]:
    organisms = [
        ("A yellowwood tree in the Knysna forest", "Autotroph (producer)", "synthesises organic glucose from inorganic carbon dioxide and water using radiant solar energy trapped by chlorophyll"),
        ("An African leopard hunting in the bushveld", "Heterotroph (carnivorous consumer)", "ingests other living organisms to obtain pre-formed organic nutrients and chemical energy"),
        ("A dung beetle rolling and consuming herbivore droppings", "Heterotroph (detritivore / decomposer)", "digests organic nutrient molecules obtained from waste products of other organisms"),
        ("Phytoplankton drifting in the Benguela current", "Autotroph (primary producer)", "uses photosynthesis in surface sunlit waters to manufacture carbohydrates from dissolved inorganic carbon"),
    ]
    org, group, reason = rng.choice(organisms)
    prompt = (
        f"Nutrition is the life process by which organisms obtain energy and nutrients. "
        f"Classify '{org}' as an autotroph or a heterotroph, and state the scientific reason."
    )
    correct = f"{group}: It {reason}."
    distractors = [
        f"{'Heterotroph' if 'Autotroph' in group else 'Autotroph'}: It absorbs mineral soil rocks directly into its cells without needing food or sunlight.",
        f"{group}: It creates new energy out of nothing, violating thermodynamic conservation laws.",
        f"{'Heterotroph' if 'Autotroph' in group else 'Autotroph'}: It converts atmospheric nitrogen directly into gold and silver to sustain metabolic life.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define nutritional classifications:\n"
        f"- Autotrophs (producers): Make their own organic food from inorganic compounds (e.g. plants, algae via photosynthesis).\n"
        f"- Heterotrophs (consumers): Must consume other organisms or organic matter for nutrition.\n\n"
        f"**Step 2:** '{org}' is classified as: **{group}** because {reason}."
    )
    return {
        "id": f"ns7_bio_13_{rng.randint(100000, 999999)}",
        "subskill": "13_life_process_nutrition_autotrophs_vs_heterotrophs",
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
            "tier_1": "Recall: 'Auto' means self (self-feeding), 'Hetero' means other (feeding on others).",
            "tier_2": "Can this organism perform photosynthesis, or must it eat other living or dead things?",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["plant_food_absorption_misconception"],
    }


# 14. Identify missing life process scenario
def arch_14_identify_missing_life_process_scenario(rng: random.Random) -> Dict[str, Any]:
    processes = [
        ("Movement", "The organism changes position or orientates body parts toward external stimuli."),
        ("Respiration", "The organism releases cellular energy from nutrient molecules through biochemical oxidation."),
        ("Sensitivity", "The organism detects changes in light, temperature, or chemical signals in its environment."),
        ("Growth", "The organism increases its cell number and permanent dry biomass over time."),
        ("Reproduction", "The organism generates offspring to ensure the continuation of its species."),
        ("Excretion", "The organism eliminates harmful chemical byproducts of cellular metabolism."),
        ("Nutrition", "The organism takes in raw materials or manufactures organic food for fuel and tissue building."),
    ]
    target, target_def = rng.choice(processes)
    present = [p[0] for p in processes if p[0] != target]
    rng.shuffle(present)
    prompt = (
        f"The mnemonic 'MRS GREN' represents all seven life processes essential to living organisms. "
        f"A learner lists six processes: {', '.join(present[:6])}.\n\n"
        f"Which life process is missing from the list, and what is its biological function?"
    )
    correct = f"{target} — {target_def}"
    distractors = [
        "Photosynthesis — The process whereby all organisms on Earth produce honey.",
        "Combustion — The burning of body parts to generate body warmth.",
        "Precipitation — The condensation of internal fluids into rain clouds.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall the seven life processes in MRS GREN:\n"
        f"M - Movement, R - Respiration, S - Sensitivity, G - Growth, R - Reproduction, E - Excretion, N - Nutrition.\n\n"
        f"**Step 2:** Comparing the learner's list reveals that **{target}** is omitted.\n"
        f"Function: {target_def}"
    )
    return {
        "id": f"ns7_bio_14_{rng.randint(100000, 999999)}",
        "subskill": "14_identify_missing_life_process_scenario",
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
            "tier_1": "Spell out MRS GREN letter by letter and cross off the ones already listed.",
            "tier_2": "Look for the letter in MRS GREN that does not appear in the six given processes.",
            "tier_3": f"The missing life process is {target}.",
        },
        "misconception_tags": ["mrs_gren_omission_error"],
    }


# 15. Requirement energy solar to chemical
def arch_15_requirement_energy_solar_to_chemical(rng: random.Random) -> Dict[str, Any]:
    efficiencies = rng.randint(1, 5)
    prompt = (
        f"The primary source of energy for almost all life on planet Earth is radiant energy from the Sun. "
        f"In South African ecosystems, green plants capture approximately {efficiencies}% of incident sunlight during photosynthesis. "
        f"What is the ultimate fate of this radiant energy as it flows through the biosphere?"
    )
    correct = "It is transformed into chemical potential energy stored in glucose bonds, passed along food chains, and eventually dissipated as metabolic heat energy."
    options = [
        correct,
        "It cycles indefinitely in a closed loop between plants and herbivores without ever losing any heat.",
        "It is transformed into nuclear uranium atoms inside plant roots to stabilize soil lithosphere.",
        "It is reflected directly back into space as gamma radiation without entering any biological food chains.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace energy flow in the biosphere:\n"
        f"- Solar radiant energy is trapped by chlorophyll in plants.\n"
        f"- Converted to chemical potential energy in carbohydrates (glucose).\n"
        f"- Consumers ingest this chemical energy and use it for metabolic work.\n"
        f"- Energy is non-cyclical: it dissipates to the environment as low-grade heat.\n\n"
        f"**Step 2:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_15_{rng.randint(100000, 999999)}",
        "subskill": "15_requirement_energy_solar_to_chemical",
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
            "tier_1": "Remember that energy flows through ecosystems while nutrients cycle.",
            "tier_2": "Sunlight is converted into chemical energy (glucose) and lost as heat.",
            "tier_3": f"The correct answer is: {correct}.",
        },
        "misconception_tags": ["energy_cycling_misconception"],
    }


# 16. Requirement gases oxygen carbon dioxide roles
def arch_16_requirement_gases_oxygen_carbon_dioxide_roles(rng: random.Random) -> Dict[str, Any]:
    gases = [
        ("Oxygen", "cellular respiration in aerobic organisms", "combining with glucose in mitochondria to release ATP energy and producing water and carbon dioxide as byproducts"),
        ("Carbon dioxide", "photosynthesis in autotrophic plants and algae", "acting as the inorganic carbon source assembled into glucose sugars in chloroplasts using solar energy"),
    ]
    gas_name, process, details = rng.choice(gases)
    alt_gas = gases[1] if gas_name == gases[0][0] else gases[0]
    prompt = (
        f"Gases from the atmosphere are vital requirements for sustaining life in the biosphere. "
        f"Which statement correctly details the biological role of {gas_name}?"
    )
    correct = f"It is required for {process}, {details}."
    distractors = [
        f"It is required for {alt_gas[1]}, {alt_gas[2]}.",
        "It acts as a solid building block for bones and teeth without taking part in cellular reactions.",
        "It is a toxic waste product that must never enter the cells of any plant or animal.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Differentiate the metabolic roles of atmospheric gases:\n"
        f"- Oxygen is utilized in cellular respiration to release energy from glucose.\n"
        f"- Carbon dioxide is fixed in photosynthesis to manufacture carbohydrates.\n\n"
        f"**Step 2:** For {gas_name}, the correct role is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_16_{rng.randint(100000, 999999)}",
        "subskill": "16_requirement_gases_oxygen_carbon_dioxide_roles",
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
            "tier_1": "Oxygen is needed to release energy from food; carbon dioxide is needed to build food in plants.",
            "tier_2": "Respiration uses O2; photosynthesis uses CO2.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["gas_role_inversion"],
    }


# 17. Requirement water biological functions
def arch_17_requirement_water_biological_functions(rng: random.Random) -> Dict[str, Any]:
    functions = [
        ("Universal solvent and transport medium", "dissolving mineral salts, sugars, and amino acids to transport them through plant xylem/phloem or animal blood"),
        ("Turgor pressure and structural support", "filling plant cell vacuoles to push against cell walls, keeping herbaceous stems and leaves upright and crisp"),
        ("Biochemical reactant in metabolic pathways", "acting as an essential reactant split during the light-dependent stage of photosynthesis (photolysis)"),
        ("Thermoregulation and evaporative cooling", "absorbing large amounts of heat due to high specific heat capacity and cooling surfaces through sweat or transpiration"),
    ]
    target_func, explanation = rng.choice(functions)
    prompt = (
        f"Water is a fundamental requirement for sustaining all known living organisms. "
        f"Which option correctly links the water function '{target_func}' with its biological explanation?"
    )
    correct = explanation
    options = [explanation] + [f[1] for f in functions if f[1] != explanation]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review biological functions of water:\n"
        f"- Solvent/transport: dissolves nutrients and metabolic wastes.\n"
        f"- Turgor pressure: keeps plant cells firm and stems upright.\n"
        f"- Reactant: split in photosynthesis and hydrolysis reactions.\n"
        f"- Thermoregulation: buffers temperature changes and cools via evaporation.\n\n"
        f"**Step 2:** '{target_func}' corresponds to: **{explanation}**."
    )
    return {
        "id": f"ns7_bio_17_{rng.randint(100000, 999999)}",
        "subskill": "17_requirement_water_biological_functions",
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
            "tier_1": "Match the named role (solvent, turgor, reactant, or cooling) directly to its biological mechanism.",
            "tier_2": "Think about how plants wilt when they lose water (turgor pressure) or how sweating cools animals.",
            "tier_3": f"The correct match is: {explanation}.",
        },
        "misconception_tags": ["water_function_confusion"],
    }


# 18. Requirement soil nutrients nitrogen phosphorus potassium
def arch_18_requirement_soil_nutrients_nitrogen_phosphorus_potassium(rng: random.Random) -> Dict[str, Any]:
    nutrients = [
        ("Nitrogen (N)", "synthesis of amino acids and proteins, and component of chlorophyll molecules", "stunted growth with yellowing of older leaves (chlorosis)"),
        ("Phosphorus (P)", "ATP energy transfer molecules and nucleic acid (DNA/RNA) structure, promoting healthy root development", "poor root systems and purplish discoloration on leaves"),
        ("Potassium (K)", "regulating stomatal opening/closing and activating enzymes for protein and carbohydrate synthesis", "curling and brown scorch marks along leaf margins and weak stems"),
    ]
    nutrient, role, deficiency = rng.choice(nutrients)
    prompt = (
        f"Plants absorb essential primary macronutrients (NPK) from soil water in the lithosphere. "
        f"Which nutrient is specifically required for {role}, with its deficiency causing {deficiency}?"
    )
    correct = nutrient
    options = [nutrient] + [n[0] for n in nutrients if n[0] != nutrient]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review primary plant macronutrients (NPK):\n"
        f"- Nitrogen (N): Protein and chlorophyll synthesis; deficiency causes chlorosis (yellow leaves).\n"
        f"- Phosphorus (P): ATP and root growth; deficiency causes purpling and stunted roots.\n"
        f"- Potassium (K): Stomatal regulation and enzyme activation; deficiency causes leaf edge scorch.\n\n"
        f"**Step 2:** The nutrient required is **{nutrient}**."
    )
    return {
        "id": f"ns7_bio_18_{rng.randint(100000, 999999)}",
        "subskill": "18_requirement_soil_nutrients_nitrogen_phosphorus_potassium",
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
            "tier_1": "Remember NPK: N for green leafy growth, P for strong roots, K for flowers/fruits and disease resistance.",
            "tier_2": "Look at the deficiency symptom described (yellowing vs purpling vs scorched margins).",
            "tier_3": f"The nutrient is {nutrient}.",
        },
        "misconception_tags": ["npk_nutrient_deficiency_confusion"],
    }


# 19. Requirement temperature range and enzyme limits
def arch_19_requirement_temperature_range_and_enzyme_limits(rng: random.Random) -> Dict[str, Any]:
    temp_c = rng.choice([48, 52, 55, 60])
    prompt = (
        f"Most living organisms are restricted to an active temperature range between approximately 0°C and 45°C. "
        f"What happens at the cellular level when a typical terrestrial organism is subjected to prolonged temperatures above {temp_c}°C?"
    )
    correct = "Metabolic enzymes and cellular proteins undergo irreversible denaturation, causing biological chemical reactions to cease permanently."
    options = [
        correct,
        "Enzymes multiply infinitely, causing cellular respiration to operate at supersonic speed without consuming oxygen.",
        "The organism's cells convert all water into solid ice crystals through spontaneous freezing.",
        "DNA molecules change into chlorophyll so the animal can survive by photosynthesising.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand temperature effects on cellular enzymes:\n"
        f"- Below 0°C: Cytoplasm freezes, water crystals rupture cell membranes, enzyme activity slows to near zero.\n"
        f"- Optimum (20°C - 37°C): Highest rate of enzyme-substrate collisions and metabolic reactions.\n"
        f"- Above 45°C: High thermal kinetic energy disrupts hydrogen and ionic bonds holding enzyme tertiary structures together, causing denaturation.\n\n"
        f"**Step 2:** At {temp_c}°C, enzymes denature irreversibly, stopping life-sustaining reactions."
    )
    return {
        "id": f"ns7_bio_19_{rng.randint(100000, 999999)}",
        "subskill": "19_requirement_temperature_range_and_enzyme_limits",
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
            "tier_1": "Recall what happens to proteins (like egg white) when heated strongly.",
            "tier_2": "Enzymes lose their specific 3D shape (denature) and can no longer catalyze biochemical reactions.",
            "tier_3": f"The correct answer is: {correct}.",
        },
        "misconception_tags": ["enzyme_denaturation_misconception"],
    }


# 20. Scientific investigation aim and hypothesis
def arch_20_scientific_investigation_aim_and_hypothesis(rng: random.Random) -> Dict[str, Any]:
    factors = [
        ("the presence of sunlight", "seedling height in millimetres", "sunlight provides the radiant energy required for photosynthesis and healthy stem growth"),
        ("the volume of water provided daily", "the percentage of seeds germinating", "water is necessary to activate metabolic enzymes and soften the seed coat"),
        ("the concentration of nitrogen fertilizer in soil", "the total number of green leaves formed", "nitrogen is an essential component of amino acids and chlorophyll"),
    ]
    manipulated, measured, rationale = rng.choice(factors)
    prompt = (
        f"A Grade 7 learner designs an experiment to investigate the requirements for plant growth. "
        f"The learner formulates the aim: 'To determine the effect of {manipulated} on {measured}.' "
        f"Which statement represents a scientifically valid and testable hypothesis for this investigation?"
    )
    correct = f"If {manipulated} is increased, then {measured} will increase because {rationale}."
    distractors = [
        "Plants are living organisms that look pretty when placed in a sunny garden bed.",
        f"Can {manipulated} affect {measured}?",
        "All seeds on Earth will germinate immediately regardless of whether any water or light exists.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review rules for a scientific hypothesis in CAPS Natural Sciences:\n"
        f"- Must be a testable statement predicting the relationship between independent and dependent variables.\n"
        f"- Best phrased as: 'If [independent variable], then [dependent variable] because [scientific reason].'\n"
        f"- A question is an aim/problem statement, not a hypothesis.\n\n"
        f"**Step 2:** The valid hypothesis is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_20_{rng.randint(100000, 999999)}",
        "subskill": "20_scientific_investigation_aim_and_hypothesis",
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
            "tier_1": "A hypothesis is a testable predictive statement, never a question.",
            "tier_2": "Look for the 'If... then... because...' structure linking the tested factor to the outcome.",
            "tier_3": f"The correct hypothesis is: {correct}.",
        },
        "misconception_tags": ["hypothesis_formulation_error"],
    }


# 21. Scientific investigation identifying variables
def arch_21_scientific_investigation_identifying_variables(rng: random.Random) -> Dict[str, Any]:
    setups = [
        ("amount of daily light exposure (0 hrs vs 6 hrs vs 12 hrs)", "shoot height measured in mm after 14 days", "soil type, seed species, ambient temperature, and water volume"),
        ("ambient temperature (5°C vs 20°C vs 35°C)", "number of days taken for radicle emergence", "seed variety, light conditions, moisture levels, and container dimensions"),
        ("daily volume of liquid water (0 ml vs 10 ml vs 30 ml)", "percentage of germinated bean seeds", "room temperature, seed type, dark environment, and cotton wool substrate"),
    ]
    indep, dep, controlled = rng.choice(setups)
    var_types = ["Independent variable", "Dependent variable", "Controlled (fixed) variables"]
    target_type = rng.choice(var_types)
    if target_type == "Independent variable":
        correct_ans = indep
        explanation_part = f"the factor deliberately changed/manipulated by the investigator ({indep})"
    elif target_type == "Dependent variable":
        correct_ans = dep
        explanation_part = f"the factor measured to assess the effect ({dep})"
    else:
        correct_ans = controlled
        explanation_part = f"the factors kept strictly constant to ensure a fair test ({controlled})"

    prompt = (
        f"In a plant growth investigation, a learner tests {indep}, records {dep}, and keeps {controlled} constant. "
        f"Which experimental parameter represents the **{target_type}**?"
    )
    options = [indep, dep, controlled, "The personal opinion of the learner"]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define experimental variables:\n"
        f"- Independent variable = what is changed ({indep}).\n"
        f"- Dependent variable = what is measured ({dep}).\n"
        f"- Controlled variables = what is kept constant ({controlled}).\n\n"
        f"**Step 2:** The {target_type} is: **{correct_ans}** ({explanation_part})."
    )
    return {
        "id": f"ns7_bio_21_{rng.randint(100000, 999999)}",
        "subskill": "21_scientific_investigation_identifying_variables",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Independent = I change; Dependent = I measure; Controlled = keep constant.",
            "tier_2": f"Identify what {target_type} means in scientific inquiry.",
            "tier_3": f"The answer is: {correct_ans}.",
        },
        "misconception_tags": ["variable_identification_confusion"],
    }


# 22. Scientific investigation control group necessity
def arch_22_scientific_investigation_control_group_necessity(rng: random.Random) -> Dict[str, Any]:
    tested_factor = rng.choice([
        ("water", "Set A receives standard watering, while Set B receives no water at all"),
        ("light", "Set A is placed on a sunny windowsill, while Set B is kept inside a light-tight cupboard"),
        ("air (carbon dioxide)", "Set A receives normal atmospheric air, while Set B is placed under a bell jar with sodium hydroxide to absorb carbon dioxide"),
    ])
    factor_name, treatment = tested_factor
    prompt = (
        f"In an investigation testing whether {factor_name} is necessary for plant life, a learner sets up two identical pots of seedlings: "
        f"{treatment}. "
        f"Why is it scientifically essential to include Set A (the control group)?"
    )
    correct = "To serve as a baseline for comparison, confirming that any observed differences in Set B are caused solely by the absence of the tested factor."
    options = [
        correct,
        "To ensure that the investigator has double the number of plants to eat at the end of the term.",
        "To prove that plants do not require any abiotic factors to survive.",
        "To make the experiment take twice as long so it fills more class time.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the role of a control test in scientific investigations:\n"
        f"- The control group receives all normal conditions (the baseline).\n"
        f"- The experimental group lacks only the single tested variable.\n"
        f"- Comparing the experimental group against the control allows the investigator to conclude with certainty that any failure or change was caused by that specific factor.\n\n"
        f"**Step 2:** Set A provides the baseline comparison: **{correct}**."
    )
    return {
        "id": f"ns7_bio_22_{rng.randint(100000, 999999)}",
        "subskill": "22_scientific_investigation_control_group_necessity",
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
            "tier_1": "Ask: How does the scientist know the plant died from lack of water and not from bad soil or disease?",
            "tier_2": "A control group provides a baseline to compare results against.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["control_group_misunderstanding"],
    }


# 23. Scientific investigation seed germination data
def arch_23_scientific_investigation_seed_germination_data(rng: random.Random) -> Dict[str, Any]:
    n_seeds = rng.choice([20, 25, 40, 50])
    germ_wet_warm = int(n_seeds * rng.choice([0.85, 0.90, 0.95]))
    germ_wet_cold = int(n_seeds * rng.choice([0.20, 0.25, 0.30]))
    germ_dry_warm = 0

    pct_warm = round((germ_wet_warm / n_seeds) * 100)
    pct_cold = round((germ_wet_cold / n_seeds) * 100)

    prompt = (
        f"A learner placed {n_seeds} bean seeds in each of three petri dishes under different conditions for 7 days:\n"
        f"- Dish 1 (Moist cotton wool at 22°C): {germ_wet_warm} seeds germinated ({pct_warm}%)\n"
        f"- Dish 2 (Moist cotton wool at 4°C): {germ_wet_cold} seeds germinated ({pct_cold}%)\n"
        f"- Dish 3 (Dry cotton wool at 22°C): {germ_dry_warm} seeds germinated (0%)\n\n"
        f"What valid conclusion can be drawn from these experimental results?"
    )
    correct = "Seed germination requires moisture, and the rate of germination is significantly increased by favourable warmth."
    options = [
        correct,
        "Seeds germinate best in completely dry soil kept in a refrigerator.",
        "Temperature has zero effect on living processes in germinating seeds.",
        "Water prevents seeds from germinating because it suffocates plant embryo cells.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the data across the dishes:\n"
        f"- Dish 1 vs Dish 3: Dry cotton wool resulted in 0% germination, proving water/moisture is an essential requirement.\n"
        f"- Dish 1 vs Dish 2: 22°C gave {pct_warm}% germination compared to only {pct_cold}% at 4°C, proving warmth accelerates germination.\n\n"
        f"**Step 2:** Conclusion: **{correct}**."
    )
    return {
        "id": f"ns7_bio_23_{rng.randint(100000, 999999)}",
        "subskill": "23_scientific_investigation_seed_germination_data",
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
            "tier_1": "Look at which dishes produced germination and which produced none.",
            "tier_2": "Dish 3 had no water (0% germination); Dish 2 was cold (low germination); Dish 1 had both water and warmth (high germination).",
            "tier_3": f"The valid conclusion is: {correct}.",
        },
        "misconception_tags": ["data_interpretation_error"],
    }


# 24. Scientific investigation light vs dark plant growth
def arch_24_scientific_investigation_light_vs_dark_plant_growth(rng: random.Random) -> Dict[str, Any]:
    height_light = rng.randint(80, 110)
    height_dark = rng.randint(130, 170)
    prompt = (
        f"Two identical pots of bean seedlings were grown for 14 days with equal water and soil. "
        f"Pot A was grown on a sunny windowsill; it developed thick stems with dark green leaves and grew to a height of {height_light} mm. "
        f"Pot B was grown inside a dark cupboard; it grew to {height_dark} mm but had thin, pale yellow, spindly stems that collapsed easily. "
        f"Why was seedling B taller than seedling A, yet unhealthy and pale?"
    )
    correct = "Seedling B underwent etiolation (rapid stem elongation in search of light), but could not synthesise chlorophyll or produce glucose without sunlight."
    options = [
        correct,
        "Seedling B grew taller because darkness is the primary energy source that feeds healthy plant cells.",
        "Seedling A was stunted because sunlight destroys all plant cells and bleaches stems yellow.",
        "Seedling B absorbed black pigment from the dark cupboard which made it twice as strong as seedling A.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand plant responses to darkness (etiolation):\n"
        f"- In the dark, seedlings rapidly elongate their internodes (etiolation) trying to reach sunlight before their seed food reserves run out.\n"
        f"- Chlorophyll synthesis requires radiant light energy; without light, stems and leaves remain pale yellow (chlorotic).\n"
        f"- While seedling B reached {height_dark} mm (taller than A at {height_light} mm), it lacked mechanical strength and could not photosynthesise.\n\n"
        f"**Step 2:** The explanation is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_24_{rng.randint(100000, 999999)}",
        "subskill": "24_scientific_investigation_light_vs_dark_plant_growth",
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
            "tier_1": "Think about why a plant in a cupboard stretches upwards (searching for light).",
            "tier_2": "Remember why leaves are green (chlorophyll requires light to form).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["height_equals_health_misconception"],
    }


# 25. Scientific investigation evaluating fair test
def arch_25_scientific_investigation_evaluating_fair_test(rng: random.Random) -> Dict[str, Any]:
    flaws = [
        ("A learner used fertile garden loam in Pot 1 (sunny window) but dry river sand in Pot 2 (dark cupboard)", "Soil type was not kept constant, introducing a confounding variable that invalidates the effect of light"),
        ("A learner watered Pot 1 with 50 ml water daily but forgot to water Pot 2 for 10 days", "Water volume was not controlled, making it impossible to determine whether the difference was caused by light or drought"),
        ("A learner tested 1 bean seed in Pot 1 and 20 maize seeds in Pot 2", "Both seed species and sample size differed, meaning genetic and species variations confounded the results"),
        ("A learner placed Pot 1 in a warm 25°C classroom and Pot 2 inside a freezing 2°C refrigerator", "Temperature varied drastically alongside light exposure, invalidating the single-variable test condition"),
    ]
    investigation, flaw_explanation = rng.choice(flaws)
    prompt = (
        f"In an investigation testing whether sunlight is necessary for plant growth, evaluate the following experimental setup:\n"
        f"\"{investigation}.\"\n\n"
        f"Why is this NOT a fair scientific test?"
    )
    correct = f"It is unfair because {flaw_explanation.lower()}."
    distractors = [
        "It is unfair because scientific investigations must always be performed outdoors in direct rain.",
        "It is a completely fair test because scientists are encouraged to change as many variables at once as possible.",
        "It is unfair because plants should never be placed in pots or observed by learners.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall the principle of a fair test in science:\n"
        f"- Only ONE independent variable may be changed at a time.\n"
        f"- All other variables must be strictly controlled (fixed).\n\n"
        f"**Step 2:** In this setup: {flaw_explanation}.\n"
        f"Therefore, the test is invalid."
    )
    return {
        "id": f"ns7_bio_25_{rng.randint(100000, 999999)}",
        "subskill": "25_scientific_investigation_evaluating_fair_test",
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
            "tier_1": "A fair test changes ONLY one factor at a time.",
            "tier_2": "Look for the extra factor that was changed accidentally besides the tested factor.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fair_test_confounding_variable"],
    }
