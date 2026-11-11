"""Grade 8 Natural Sciences: Term 1 - Photosynthesis and Respiration (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 1/01. Photosynthesis and respiration.md.
Focus: Cellular respiration, energy release, breathing distinction, equations, mitochondria, limewater tests, seed germination investigations, and ecological gas balance.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Cellular respiration definition and energy release
def arch_26_cellular_respiration_definition_and_energy_release(rng: random.Random) -> Dict[str, Any]:
    organisms = [
        ("a running cheetah (*Acinonyx jubatus*) sprinting across the savanna", "fueling explosive muscle contractions"),
        ("a growing maize seedling pushing its shoot upward through soil", "synthesizing new cell components and driving mitosis"),
        ("a human student reading a science textbook", "powering continuous active transport and nerve impulse transmission in the brain"),
    ]
    organism, use = rng.choice(organisms)
    prompt = (
        f"Consider {organism}. Cells break down food molecules to release chemical potential energy for {use}.\n\n"
        f"What biological process breaks down glucose in living cells to release usable energy for the life processes?"
    )
    correct = "Cellular respiration"
    options = [
        correct,
        "Mechanical sedimentation",
        "Geological tectonic subduction",
        "Passive crystallization",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define the energy-releasing process in living cells:\n"
        f"- Cellular respiration is the biochemical process occurring inside living cells where glucose is broken down in the presence of oxygen to release usable energy (ATP) for the seven life processes.\n\n"
        f"**Step 2:** The process is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_26_{rng.randint(100000, 999999)}",
        "subskill": "26_cellular_respiration_definition_and_energy_release",
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
            "tier_1": "Recall the life process that releases energy from food.",
            "tier_2": "It is cellular respiration, which occurs in all living cells.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["respiration_definition_misconception"],
    }


# 27. Distinguishing cellular respiration from breathing
def arch_27_distinguishing_cellular_respiration_from_breathing(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Many learners incorrectly believe that 'breathing' and 'respiration' are the exact same thing.\n\n"
        f"What is the fundamental scientific difference between **breathing (ventilation)** and **cellular respiration**?"
    )
    correct = (
        "Breathing is the mechanical physical process of moving air in and out of the lungs (or gills), "
        "whereas cellular respiration is the chemical reaction occurring inside every cell's mitochondria to release energy from glucose."
    )
    options = [
        correct,
        "Breathing takes place only in plants, while respiration takes place only in dead fossils.",
        "Breathing releases nuclear energy, while respiration absorbs sunlight in leaves.",
        "There is zero difference; scientists use the two words purely as artistic poetry.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish mechanical gas exchange from intracellular metabolism:\n"
        f"- Breathing (ventilation): muscular, mechanical pumping of air across respiratory surfaces (lungs/tracheae).\n"
        f"- Cellular respiration: microscopic biochemical oxidation of glucose inside mitochondria yielding ATP energy.\n"
        f"- Plants and bacteria respire continuously without ever 'breathing' with lungs.\n\n"
        f"**Step 2:** The core distinction is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_27_{rng.randint(100000, 999999)}",
        "subskill": "27_distinguishing_cellular_respiration_from_breathing",
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
            "tier_1": "Does a tree breathe with lungs? No, but does it respire? Yes.",
            "tier_2": "Breathing is physical air movement; cellular respiration is a chemical reaction inside cells.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["breathing_vs_respiration_confusion"],
    }


# 28. Cellular respiration word equation and symbols
def arch_28_cellular_respiration_word_equation_and_symbols(rng: random.Random) -> Dict[str, Any]:
    equations = [
        ("glucose + oxygen -> carbon dioxide + water + energy", True),
        ("carbon dioxide + water + sunlight -> glucose + oxygen", False),
        ("starch + carbon dioxide -> oxygen + water", False),
        ("glucose + carbon dioxide -> oxygen + water + energy", False),
    ]
    correct = equations[0][0]
    options = [eq[0] for eq in equations]
    rng.shuffle(options)
    prompt = (
        f"Which of the following represents the correct word equation for **aerobic cellular respiration** "
        f"occurring in living plant and animal cells?"
    )
    sol = (
        f"**Step 1:** Identify the reactants and products of cellular respiration:\n"
        f"- Reactants: glucose ($\text{{C}}_6\text{{H}}_{{12}}\text{{O}}_6$) + oxygen ($\text{{O}}_2$)\n"
        f"- Products: carbon dioxide ($\text{{CO}}_2$) + water ($\text{{H}}_2\text{{O}}$) + energy (ATP and heat)\n\n"
        f"**Step 2:** The correct word equation is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_28_{rng.randint(100000, 999999)}",
        "subskill": "28_cellular_respiration_word_equation_and_symbols",
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
            "tier_1": "What fuel is burned with oxygen to release energy, CO2, and water?",
            "tier_2": "Glucose and oxygen react to produce carbon dioxide, water, and energy.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["respiration_equation_error"],
    }


# 29. Cellular respiration reactants glucose and oxygen
def arch_29_cellular_respiration_reactants_glucose_and_oxygen(rng: random.Random) -> Dict[str, Any]:
    animals = [
        ("an eagle soaring in the Drakensberg mountains", "eating small mammals and inhaling atmospheric air"),
        ("a fish swimming in the Vaal River", "ingesting aquatic invertebrates and absorbing dissolved oxygen through gills"),
        ("an oak tree growing in a botanical garden", "utilizing glucose made in leaves and absorbing soil/air oxygen"),
    ]
    organism, source_desc = rng.choice(animals)
    prompt = (
        f"To carry out cellular respiration, {organism} requires two raw chemical reactants: **glucose** and **oxygen**, "
        f"obtained by {source_desc}.\n\n"
        f"What is the specific biochemical role of **oxygen** in aerobic cellular respiration?"
    )
    correct = (
        "Oxygen acts as the chemical oxidant that allows glucose molecules to be completely broken down "
        "to release the maximum amount of stored chemical energy."
    )
    options = [
        correct,
        "Oxygen serves as a green pigment to make animal blood turn into emerald liquid.",
        "Oxygen creates solid nitrogen blocks inside the heart to stop blood circulation.",
        "Oxygen cools the cells down to -200 degrees Celsius to freeze waste proteins.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the biochemical role of oxygen:\n"
        f"- Oxygen is required to oxidize glucose fully into $\text{{CO}}_2$ and $\text{{H}}_2\text{{O}}$.\n"
        f"- Without oxygen, complete chemical energy extraction cannot proceed (cells would undergo limited anaerobic fermentation).\n\n"
        f"**Step 2:** The role of oxygen is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_29_{rng.randint(100000, 999999)}",
        "subskill": "29_cellular_respiration_reactants_glucose_and_oxygen",
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
            "tier_1": "Why do aerobic organisms die if deprived of oxygen for several minutes?",
            "tier_2": "Oxygen is needed to oxidize glucose and unlock energy for vital life processes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["oxygen_role_respiration_misconception"],
    }


# 30. Cellular respiration products co2 water and energy
def arch_30_cellular_respiration_products_co2_water_and_energy(rng: random.Random) -> Dict[str, Any]:
    products = [
        ("carbon dioxide (CO2)", "a waste gas that diffuses out of cells into blood/air to be excreted"),
        ("water (H2O)", "a harmless chemical by-product that joins cellular fluids or is excreted via lungs, sweat, or kidneys"),
        ("energy (ATP + heat)", "usable chemical energy driving cellular work plus thermal energy maintaining body warmth in endotherms"),
    ]
    product_name, description = rng.choice(products)
    prompt = (
        f"During aerobic cellular respiration, glucose is decomposed into three output products: "
        f"carbon dioxide, water, and energy.\n\n"
        f"What is the physiological fate or role of **{product_name}** in the organism?"
    )
    correct = f"It serves as {description}."
    options = [
        correct,
        "It turns immediately into radioactive radon gas that dissolves all bone tissue.",
        "It freezes inside muscles to form permanent stone armor plates.",
        "It travels to the outer skin to produce electric lighting for nocturnal vision.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Detail the outputs of cellular respiration:\n"
        f"- Carbon dioxide: metabolic waste exhaled or diffused through stomata.\n"
        f"- Water: metabolic water used by the cell or excreted.\n"
        f"- Energy: ATP powers active transport, protein synthesis, and muscle contraction, while thermal energy maintains warmth.\n\n"
        f"**Step 2:** For {product_name}: **{correct}**."
    )
    return {
        "id": f"ns8_pr_30_{rng.randint(100000, 999999)}",
        "subskill": "30_cellular_respiration_products_co2_water_and_energy",
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
            "tier_1": f"Think about what happens to {product_name} after respiration occurs.",
            "tier_2": f"It serves as {description}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["respiration_products_fate_misconception"],
    }


# 31. Mitochondria as the cellular powerhouse of respiration
def arch_31_mitochondria_as_the_cellular_powerhouse_of_respiration(rng: random.Random) -> Dict[str, Any]:
    cell_types = [
        ("flight muscle cells of an active bee (*Apis mellifera*)", "thousands of tightly packed mitochondria", "supply immense energy for rapid wing flapping"),
        ("cardiac muscle cells in the human heart", "dense networks of mitochondria", "power continuous non-stop contraction over a lifetime"),
        ("root tip cells of an active acacia tree", "numerous mitochondria", "provide energy for active absorption of soil mineral ions"),
    ]
    cell_type, organelle_feature, reason = rng.choice(cell_types)
    prompt = (
        f"Microscopic examination reveals that {cell_type} contain {organelle_feature} to {reason}.\n\n"
        f"Why are **mitochondria** scientifically referred to as the 'powerhouses of the cell'?"
    )
    correct = (
        "They are the specialized cellular organelles where aerobic respiration takes place, "
        "generating the vast majority of the cell's usable chemical energy."
    )
    options = [
        correct,
        "They manufacture heavy iron ingots and coal for cellular furnaces.",
        "They generate radioactive nuclear fission to disintegrate unwanted bacteria.",
        "They store green chlorophyll pigments to produce food in the dark.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define the organelle of cellular respiration:\n"
        f"- Mitochondria contain the respiratory enzymes and inner folded membranes (cristae) required for aerobic respiration.\n"
        f"- Cells with high metabolic demands ({cell_type}) possess thousands of mitochondria to meet high energy requirements.\n\n"
        f"**Step 2:** The reason is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_31_{rng.randint(100000, 999999)}",
        "subskill": "31_mitochondria_as_the_cellular_powerhouse_of_respiration",
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
            "tier_1": "Which cell organelle is responsible for releasing energy in cellular respiration?",
            "tier_2": "Mitochondria release energy from glucose during respiration.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mitochondria_powerhouse_misconception"],
    }


# 32. Continuous nature of respiration day and night
def arch_32_continuous_nature_of_respiration_day_and_night(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Consider a healthy green potted plant on a windowsill.\n\n"
        f"During which periods does this plant carry out **photosynthesis**, "
        f"and during which periods does it carry out **cellular respiration**?"
    )
    correct = (
        "Photosynthesis occurs only during daylight hours when light is available; "
        "cellular respiration occurs **continuously 24 hours a day (both day and night)**."
    )
    options = [
        correct,
        "Photosynthesis occurs day and night, while respiration only occurs for 5 minutes at sunset.",
        "Plants only respire during the day and die completely every night at 22:00.",
        "Plants never respire at any time; only animals carry out cellular respiration.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare temporal activity of photosynthesis vs respiration:\n"
        f"- Photosynthesis requires radiant light energy -> active strictly during daylight hours.\n"
        f"- Cellular respiration is essential to sustain all 7 life processes -> active continuously every second, day and night, in all living cells.\n"
        f"- If a plant stopped respiring at night, its cells would rapidly die from lack of energy.\n\n"
        f"**Step 2:** The true statement is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_32_{rng.randint(100000, 999999)}",
        "subskill": "32_continuous_nature_of_respiration_day_and_night",
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
            "tier_1": "Can a living plant survive if it stops producing energy at night?",
            "tier_2": "Respiration must occur continuously 24 hours a day to keep cells alive.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["plants_only_photosynthesise_misconception"],
    }


# 33. Clear limewater test for carbon dioxide milky precipitate (with dynamic SVG)
def arch_33_clear_limewater_test_for_carbon_dioxide_milky_precipitate(rng: random.Random) -> Dict[str, Any]:
    test_context = rng.choice([
        ("exhaled air from a human learner", "straw bubbled into limewater"),
        ("gas extracted from a flask of germinating pea seeds", "delivery tube leading into limewater"),
    ])
    liquid_color = rng.choice(["#f1f5f9", "#e2e8f0", "#cbd5e1"])

    svg = (
        f'<svg viewBox="0 0 380 230" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="190" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Limewater Test for CO2: {test_context[0]}</text>'
        f'<rect x="155" y="60" width="70" height="130" fill="{liquid_color}" stroke="#334155" stroke-width="2" rx="4" />'
        f'<rect x="156" y="100" width="68" height="88" fill="#e2e8f0" fill-opacity="0.8" />'
        f'<line x1="190" y1="40" x2="190" y2="160" stroke="#0284c7" stroke-width="3" />'
        f'<circle cx="190" cy="140" r="3" fill="#ffffff" stroke="#94a3b8" />'
        f'<circle cx="185" cy="120" r="4" fill="#ffffff" stroke="#94a3b8" />'
        f'<circle cx="195" cy="105" r="3" fill="#ffffff" stroke="#94a3b8" />'
        f'<text x="190" y="180" font-size="10" fill="#475569" font-weight="bold" text-anchor="middle">Milky / Cloudy</text>'
        f'<line x1="230" y1="130" x2="280" y2="130" stroke="#0f172a" stroke-width="1.5" />'
        f'<text x="285" y="133" font-size="10" fill="#0f172a">CaCO3 precipitate</text>'
        f'<text x="190" y="215" font-size="10" fill="#0f172a" text-anchor="middle">Clear Limewater turns milky/cloudy -> Proves CO2 gas</text>'
        f'</svg>'
    )

    prompt = (
        f"In an investigation testing for cellular respiration products, {test_context[0]} is introduced via a "
        f"{test_context[1]} into a test tube of **clear limewater** [calcium hydroxide solution, Ca(OH)2].\n\n"
        f"What diagnostic chemical change occurs, and what does this observation prove?"
    )
    correct = (
        "The clear limewater turns **milky (cloudy white)** due to the formation of an insoluble "
        "calcium carbonate precipitate, proving that carbon dioxide is released during respiration."
    )
    options = [
        correct,
        "The clear limewater turns neon blue and freezes into solid ice, proving oxygen is present.",
        "The limewater dissolves the glass test tube into water, proving hydrochloric acid is present.",
        "The limewater bursts into bright purple flames, proving hydrogen gas was created.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall the limewater chemical reaction:\n"
        f"- Clear limewater is an aqueous solution of calcium hydroxide: $\text{{Ca(OH)}}_2$.\n"
        f"- When $\\text{{CO}}_2$ bubbles through, it reacts: $\\text{{Ca(OH)}}_2 + \\text{{CO}}_2 \\rightarrow \\text{{CaCO}}_3 \\downarrow + \\text{{H}}_2\\text{{O}}$.\n"
        f"- Insoluble calcium carbonate ($\text{{CaCO}}_3$) forms microscopic white precipitate particles, turning the liquid milky/cloudy.\n\n"
        f"**Step 2:** The observation and proof: **{correct}**."
    )
    return {
        "id": f"ns8_pr_33_{rng.randint(100000, 999999)}",
        "subskill": "33_clear_limewater_test_for_carbon_dioxide_milky_precipitate",
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
            "tier_1": "What happens to clear limewater when you blow exhaled breath through a straw?",
            "tier_2": "It turns cloudy/milky because of carbon dioxide.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["limewater_test_milky_misconception"],
    }


# 34. Bromothymol blue indicator respiration colour shift
def arch_34_bromothymol_blue_indicator_respiration_colour_shift(rng: random.Random) -> Dict[str, Any]:
    duration_mins = rng.choice([15, 30, 45])
    prompt = (
        f"Bromothymol blue (BTB) is a pH indicator that is **blue** in neutral/alkaline conditions and turns **yellow** "
        f"when an acid is present. "
        f"A learner places several live germinating bean seeds on moist cotton wool above a small beaker of blue BTB solution inside a sealed jar. "
        f"After {duration_mins} minutes, the indicator turns distinctly **yellow**.\n\n"
        f"What chemical reaction caused the BTB solution to change from blue to yellow?"
    )
    correct = (
        "The respiring seeds released carbon dioxide (CO2), which dissolved in the indicator solution "
        "to form weak carbonic acid (H2CO3), lowering the pH and turning the indicator yellow."
    )
    options = [
        correct,
        "The seeds absorbed all blue food colouring from the air, leaving yellow behind.",
        "The seeds produced hydrochloric acid from their roots that splashed into the beaker.",
        "The seeds absorbed nitrogen gas which turned the water into alkaline bleach.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the chemistry of the BTB indicator:\n"
        f"- Cellular respiration produces $\text{{CO}}_2$ gas.\n"
        f"- Dissolving $\text{{CO}}_2$ in water produces carbonic acid: $\text{{CO}}_2 + \text{{H}}_2\text{{O}} \rightleftharpoons \text{{H}}_2\text{{CO}}_3$.\n"
        f"- The acidic pH shifts bromothymol blue from blue to yellow.\n\n"
        f"**Step 2:** The cause is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_34_{rng.randint(100000, 999999)}",
        "subskill": "34_bromothymol_blue_indicator_respiration_colour_shift",
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
            "tier_1": "What acid forms when carbon dioxide dissolves in water?",
            "tier_2": "CO2 forms carbonic acid, making the solution acidic and turning BTB yellow.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["btb_indicator_acidity_misconception"],
    }


# 35. Germinating seeds respiration investigation setup
def arch_35_germinating_seeds_respiration_investigation_setup(rng: random.Random) -> Dict[str, Any]:
    seeds = rng.choice(["germinating mung beans", "germinating sunflower seeds", "germinating green peas"])
    prompt = (
        f"In an investigation to measure cellular respiration in plants, scientists typically choose **{seeds}** "
        f"rather than fully grown green leafy plants.\n\n"
        f"Why are germinating seeds ideal specimens for investigating cellular respiration without confusing experimental results?"
    )
    correct = (
        "Germinating seeds respire at extremely high metabolic rates and do not yet possess green leaves or chlorophyll, "
        "ensuring they carry out respiration without any simultaneous photosynthesis confounding the gas measurements."
    )
    options = [
        correct,
        "Because germinating seeds are non-living minerals that do not consume any oxygen.",
        "Because seeds release liquid gold instead of carbon dioxide.",
        "Because fully grown plants never carry out cellular respiration under any conditions.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand why germinating seeds are chosen:\n"
        f"- Rapid cell division and growth during germination require large amounts of ATP -> very high cellular respiration rate.\n"
        f"- Seeds lack leaves and chlorophyll -> zero photosynthesis occurs.\n"
        f"- This isolates cellular respiration cleanly without competing gas exchange reactions.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_35_{rng.randint(100000, 999999)}",
        "subskill": "35_germinating_seeds_respiration_investigation_setup",
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
            "tier_1": "Do seeds underground have green leaves to photosynthesise?",
            "tier_2": "Seeds only respire and do not photosynthesise, preventing mixed gas signals.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["germinating_seeds_respiration_advantage_misconception"],
    }


# 36. Vacuum flask heat production experiment in germination (with dynamic SVG)
def arch_36_vacuum_flask_heat_production_experiment_in_germination(rng: random.Random) -> Dict[str, Any]:
    t_start = 20
    t_live = rng.randint(27, 34)
    t_dead = rng.choice([20, 21])

    svg = (
        f'<svg viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="210" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Heat Energy from Respiration in Vacuum Flasks</text>'
        f'<rect x="50" y="60" width="130" height="130" fill="#f8fafc" stroke="#3b82f6" stroke-width="2" rx="6" />'
        f'<text x="115" y="85" font-size="11" fill="#1e3a8a" font-weight="bold" text-anchor="middle">Flask A (Live Seeds)</text>'
        f'<text x="115" y="115" font-size="14" fill="#dc2626" font-weight="bold" text-anchor="middle">{t_live}&#176;C</text>'
        f'<text x="115" y="145" font-size="10" fill="#15803d" text-anchor="middle">Active respiration</text>'
        f'<rect x="240" y="60" width="130" height="130" fill="#f8fafc" stroke="#64748b" stroke-width="2" rx="6" />'
        f'<text x="305" y="85" font-size="11" fill="#334155" font-weight="bold" text-anchor="middle">Flask B (Boiled Seeds)</text>'
        f'<text x="305" y="115" font-size="14" fill="#2563eb" font-weight="bold" text-anchor="middle">{t_dead}&#176;C</text>'
        f'<text x="305" y="145" font-size="10" fill="#64748b" text-anchor="middle">Zero respiration</text>'
        f'<text x="210" y="215" font-size="10" fill="#0f172a" text-anchor="middle">Temperature rise in Flask A proves cellular respiration releases thermal energy (heat)</text>'
        f'</svg>'
    )

    prompt = (
        f"Two vacuum flasks with inserted thermometers are set up at an initial temperature of {t_start} °C:\n"
        f"- **Flask A:** Contains live germinating peas (thermometer rises to {t_live} °C after 24 hours).\n"
        f"- **Flask B:** Contains boiled, sterilized dead peas (thermometer remains at {t_dead} °C).\n\n"
        f"What biological principle does the temperature increase in Flask A demonstrate?"
    )
    correct = (
        "Cellular respiration is an exergonic metabolic process that releases chemical energy, "
        "part of which is dissipated as thermal energy (heat)."
    )
    options = [
        correct,
        "Living peas produce friction by jumping around inside the vacuum flask.",
        "Boiled peas absorb all heat from the universe to freeze the thermometer.",
        "Vacuum flasks produce electrical currents that microwave living organic seeds.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the energy transfer in cellular respiration:\n"
        f"- During cellular respiration, breaking the chemical bonds of glucose releases energy.\n"
        f"- While much energy is captured in ATP, energy conversions are not 100% efficient; excess energy is released as heat.\n"
        f"- The insulated vacuum flask traps this heat, raising the temperature from {t_start} °C to {t_live} °C in Flask A.\n"
        f"- Flask B contains dead seeds with denatured enzymes -> no respiration -> temperature stays at {t_dead} °C.\n\n"
        f"**Step 2:** The demonstrated principle is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_36_{rng.randint(100000, 999999)}",
        "subskill": "36_vacuum_flask_heat_production_experiment_in_germination",
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
            "tier_1": "What happens to some of the energy released during cellular chemical reactions?",
            "tier_2": "Part of the chemical energy is released as heat, raising the temperature.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["respiration_heat_energy_misconception"],
    }


# 37. Control setup in respiration boiled sterilized seeds
def arch_37_control_setup_in_respiration_boiled_sterilized_seeds(rng: random.Random) -> Dict[str, Any]:
    antiseptic = rng.choice(["mild bleach / disinfectant solution", "formalin antiseptic rinse"])
    prompt = (
        f"In the vacuum flask respiration experiment, Flask B contains boiled peas that were soaked in {antiseptic}.\n\n"
        f"Why was it scientifically necessary to both **boil** the seeds and **sterilize** them with disinfectant in the control flask?"
    )
    correct = (
        "Boiling kills the seeds to halt plant respiration; sterilizing kills surface bacteria and fungal microbes "
        "so that microbial respiration does not produce heat and create false positive results."
    )
    options = [
        correct,
        "Boiling makes the peas taste sweeter for the laboratory technicians.",
        "Disinfectant adds extra oxygen molecules into the dead seeds to revive them.",
        "Boiling changes the peas from plants into small mammal embryos.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand experimental control validity:\n"
        f"- Boiled seeds have dead cells: proves plant respiration ceased.\n"
        f"- However, dead organic matter is readily decomposed by bacteria and fungi, which respire and emit heat.\n"
        f"- Soaking in {antiseptic} eliminates decomposers, ensuring zero biological respiration occurs in the control flask.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_37_{rng.randint(100000, 999999)}",
        "subskill": "37_control_setup_in_respiration_boiled_sterilized_seeds",
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
            "tier_1": "What organisms would grow on dead, moist peas if they weren't disinfected?",
            "tier_2": "Bacteria and fungi would respire and produce heat, ruining the control.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["control_flask_disinfection_misconception"],
    }


# 38. Comparing gas composition inhaled vs exhaled air
def arch_38_comparing_gas_composition_inhaled_vs_exhaled_air(rng: random.Random) -> Dict[str, Any]:
    gases = [
        ("oxygen", "approximately 21%", "approximately 16%", "used up by cells during aerobic cellular respiration"),
        ("carbon dioxide", "approximately 0.04%", "approximately 4%", "produced as a metabolic waste product by cellular respiration and exhaled"),
    ]
    gas_name, inhaled_val, exhaled_val, reason = rng.choice(gases)
    prompt = (
        f"Consider the composition of human inhaled atmospheric air versus exhaled air:\n"
        f"- Inhaled air contains {inhaled_val} of **{gas_name}**.\n"
        f"- Exhaled air contains {exhaled_val} of **{gas_name}**.\n\n"
        f"What biological process in the body's tissues accounts for this measured change?"
    )
    correct = f"Cellular respiration, because {gas_name} is {reason}."
    options = [
        correct,
        f"Photosynthesis in the stomach, because stomach acid produces emerald chlorophyll.",
        f"Geological erosion in the trachea, because wind wears away lung tissue.",
        f"Mechanical digestion in the kidneys, because kidneys absorb all atmospheric gases.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare inhaled vs exhaled gas percentages:\n"
        f"- Oxygen: drops from ~21% to ~16% (consumed by mitochondria in respiration).\n"
        f"- Carbon dioxide: increases ~100-fold from ~0.04% to ~4% (released as a product of respiration).\n"
        f"- Nitrogen: remains unchanged (~78%) because it is chemically inert in respiration.\n\n"
        f"**Step 2:** The explanation for {gas_name} is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_38_{rng.randint(100000, 999999)}",
        "subskill": "38_comparing_gas_composition_inhaled_vs_exhaled_air",
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
            "tier_1": f"Why does the level of {gas_name} change when air passes through the lungs?",
            "tier_2": f"Cells consume oxygen and produce carbon dioxide during cellular respiration.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["inhaled_exhaled_air_respiration_misconception"],
    }


# 39. Energy needs comparing active exercise vs resting respiration
def arch_39_energy_needs_comparing_active_exercise_vs_resting_respiration(rng: random.Random) -> Dict[str, Any]:
    exercise_type = rng.choice([
        ("sprinting 400 metres on an athletics track", "breathing rate and pulse rate increase dramatically"),
        ("swimming 10 laps of an Olympic pool", "heart rate doubles and body temperature rises"),
        ("cycling vigorously up a steep mountain pass", "deep rapid panting and heavy perspiration occur"),
    ])
    prompt = (
        f"When an individual engages in {exercise_type[0]}, {exercise_type[1]}.\n\n"
        f"Why does strenuous physical exercise cause cellular respiration, breathing rate, and heart rate to accelerate?"
    )
    correct = (
        "Contracting muscle cells consume ATP energy rapidly; the cardiovascular and respiratory systems must "
        "deliver more oxygen and glucose to cells and remove excess carbon dioxide faster."
    )
    options = [
        correct,
        "Exercise causes muscles to freeze, so the heart pumps boiling water to melt them.",
        "Breathing fast allows the body to absorb sunlight through the bronchial tubes.",
        "The lungs expand during exercise to store large amounts of solid food.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the physiological demands of exercise:\n"
        f"- Working muscle fibers require enormous amounts of ATP.\n"
        f"- Cellular respiration rate must increase rapidly to meet this ATP demand.\n"
        f"- Increased respiration consumes more $\text{{O}}_2$ and generates more $\text{{CO}}_2$.\n"
        f"- Breathing accelerates to increase $\text{{O}}_2$ intake and $\text{{CO}}_2$ clearance; heart rate accelerates to transport these gases via blood.\n\n"
        f"**Step 2:** The physiological reason is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_39_{rng.randint(100000, 999999)}",
        "subskill": "39_energy_needs_comparing_active_exercise_vs_resting_respiration",
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
            "tier_1": "What two things do muscles need more of when working hard?",
            "tier_2": "Muscles need more oxygen and glucose for faster respiration, and need to clear CO2.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["exercise_respiration_rate_misconception"],
    }


# 40. Interdependence photosynthesis and respiration carbon cycle (with dynamic SVG)
def arch_40_interdependence_photosynthesis_and_respiration_carbon_cycle(rng: random.Random) -> Dict[str, Any]:
    animal_example = rng.choice(["Herbivore (Zebra)", "Consumer (Springbok)", "Primary Consumer (Cattle)"])
    plant_example = rng.choice(["Acacia Tree", "Savanna Grass", "Indigenous Shrub"])
    plant_color = rng.choice(["#15803d", "#16a34a", "#059669"])

    svg = (
        f'<svg viewBox="0 0 420 240" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="210" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Interdependence: Gas \u0026 Energy Cycle</text>'
        f'<rect x="40" y="60" width="130" height="90" fill="#dcfce7" stroke="{plant_color}" stroke-width="2" rx="6" />'
        f'<text x="105" y="85" font-size="11" fill="#14532d" font-weight="bold" text-anchor="middle">{plant_example}</text>'
        f'<text x="105" y="105" font-size="10" fill="#166534" text-anchor="middle">Photosynthesis</text>'
        f'<rect x="250" y="60" width="130" height="90" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="6" />'
        f'<text x="315" y="85" font-size="11" fill="#78350f" font-weight="bold" text-anchor="middle">{animal_example}</text>'
        f'<text x="315" y="105" font-size="10" fill="#92400e" text-anchor="middle">Respiration</text>'
        f'<path d="M 170 80 Q 210 60 250 80" fill="none" stroke="#2563eb" stroke-width="2" />'
        f'<text x="210" y="65" font-size="10" fill="#1d4ed8" font-weight="bold" text-anchor="middle">O2 + Glucose &gt;&gt;</text>'
        f'<path d="M 250 130 Q 210 150 170 130" fill="none" stroke="#dc2626" stroke-width="2" />'
        f'<text x="210" y="150" font-size="10" fill="#b91c1c" font-weight="bold" text-anchor="middle">&lt;&lt; CO2 + H2O</text>'
        f'<text x="210" y="210" font-size="10" fill="#334155" text-anchor="middle">Products of photosynthesis become reactants of respiration, and vice versa</text>'
        f'</svg>'
    )

    prompt = (
        f"In natural ecosystems, **photosynthesis** (performed by producers like {plant_example}) and "
        f"**cellular respiration** (performed by all organisms including {animal_example}) are interdependent.\n\n"
        f"How does this cyclical relationship sustain the balance of atmospheric gases on Earth?"
    )
    correct = (
        "The products of photosynthesis (glucose and oxygen) serve as the essential reactants for cellular respiration, "
        "while the products of respiration (carbon dioxide and water) serve as the raw reactants for photosynthesis."
    )
    options = [
        correct,
        "Photosynthesis destroys all atmospheric gases, while respiration creates brand new nitrogen atoms.",
        "Both processes use up oxygen, leaving zero oxygen for any organisms in the future.",
        "Respiration creates sunlight energy that leaves use to build granite rocks.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the reciprocal chemical cycles:\n"
        f"- Photosynthesis: $\text{{CO}}_2 + \text{{H}}_2\text{{O}} + \text{{light}} \rightarrow \text{{glucose}} + \text{{O}}_2$.\n"
        f"- Respiration: $\text{{glucose}} + \text{{O}}_2 \rightarrow \text{{CO}}_2 + \text{{H}}_2\text{{O}} + \text{{energy}}$.\n"
        f"- The inputs of one are precisely the outputs of the other, forming a balanced global carbon and oxygen cycle.\n\n"
        f"**Step 2:** The fundamental relationship is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_40_{rng.randint(100000, 999999)}",
        "subskill": "40_interdependence_photosynthesis_and_respiration_carbon_cycle",
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
            "tier_1": "What gas does photosynthesis release, and what gas does respiration release?",
            "tier_2": "The outputs of one process are the inputs of the other.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["gas_balance_interdependence_misconception"],
    }


# 41. Day vs night net gas exchange in plants
def arch_41_day_vs_night_net_gas_exchange_in_plants(rng: random.Random) -> Dict[str, Any]:
    time_period = rng.choice([
        ("during bright midday sunlight", "rate of photosynthesis is much higher than rate of respiration", "net uptake of carbon dioxide and net release of oxygen"),
        ("in the middle of a pitch-black night", "photosynthesis ceases completely while cellular respiration continues", "net uptake of oxygen and net release of carbon dioxide"),
    ])
    prompt = (
        f"Consider a healthy tree {time_period[0]}. Under these conditions, {time_period[1]}.\n\n"
        f"What is the **net overall gas exchange** between the plant and the surrounding atmosphere?"
    )
    correct = f"There is a {time_period[2]}."
    options = [
        correct,
        "The plant stops interacting with atmospheric gases completely.",
        "The tree absorbs pure nitrogen and releases liquid methane.",
        "The tree transforms into a solid stone statue until dawn.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare rates of photosynthesis vs respiration:\n"
        f"- In bright sunlight: Photosynthesis rate >> Respiration rate -> net consumption of $\text{{CO}}_2$ and net release of $\text{{O}}_2$.\n"
        f"- In darkness: Photosynthesis = 0, Respiration > 0 -> plant absorbs $\text{{O}}_2$ and releases $\text{{CO}}_2$.\n\n"
        f"**Step 2:** Under the described condition: **{correct}**."
    )
    return {
        "id": f"ns8_pr_41_{rng.randint(100000, 999999)}",
        "subskill": "41_day_vs_night_net_gas_exchange_in_plants",
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
            "tier_1": f"Is photosynthesis active {time_period[0]}?",
            "tier_2": f"Under these conditions: {time_period[2]}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["net_gas_exchange_day_night_misconception"],
    }


# 42. Compensation point rate photosynthesis equals respiration
def arch_42_compensation_point_rate_photosynthesis_equals_respiration(rng: random.Random) -> Dict[str, Any]:
    times = ["at early dawn when the sun barely appears above the horizon", "at dusk as the sun sets and light intensity dims"]
    time_of_day = rng.choice(times)
    prompt = (
        f"A plant physiologist monitors a leaf {time_of_day}. "
        f"At this specific low light intensity, the rate of photosynthesis exactly equals the rate of cellular respiration.\n\n"
        f"What is this physiological state called, and what is the resulting overall gas exchange balance with the environment?"
    )
    correct = (
        "The **compensation point**; at this point, all CO2 produced by respiration is used up in photosynthesis, "
        "and all O2 produced by photosynthesis is used in respiration, resulting in **zero net gas exchange**."
    )
    options = [
        correct,
        "The freezing point; the leaf turns into solid ice crystals and ceases all life.",
        "The boiling point; the sap vaporizes and explodes the trunk.",
        "The extinction threshold; the plant permanently loses all genes.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define the compensation point:\n"
        f"- The light compensation point occurs when photosynthetic carbon fixation exactly balances respiratory carbon release.\n"
        f"- Rate of $\text{{CO}}_2$ uptake = Rate of $\text{{CO}}_2$ release.\n"
        f"- Rate of $\text{{O}}_2$ release = Rate of $\text{{O}}_2$ uptake.\n"
        f"- Net gas exchange between leaf and air is zero.\n\n"
        f"**Step 2:** The state and result: **{correct}**."
    )
    return {
        "id": f"ns8_pr_42_{rng.randint(100000, 999999)}",
        "subskill": "42_compensation_point_rate_photosynthesis_equals_respiration",
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
            "tier_1": "What happens when food production rate matches food consumption rate exactly?",
            "tier_2": "At the compensation point, gas production and consumption balance with zero net exchange.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["compensation_point_misconception"],
    }


# 43. Greenhouse effect and deforestation upsetting gas balance
def arch_43_greenhouse_effect_and_deforestation_upsetting_gas_balance(rng: random.Random) -> Dict[str, Any]:
    factors = [
        ("massive widespread deforestation of tropical rainforests", "removes billions of photosynthetic trees that act as natural carbon sinks"),
        ("combustion of fossil fuels (coal, oil, gas) in power plants and vehicles", "releases vast quantities of ancient locked carbon into the atmosphere as CO2"),
    ]
    factor, consequence = rng.choice(factors)
    prompt = (
        f"Human activities such as {factor} ({consequence}) "
        f"are disrupting the global balance between photosynthesis and respiration.\n\n"
        f"What is the major ecological consequence of this imbalance on global climate?"
    )
    correct = (
        "Atmospheric carbon dioxide levels rise steadily, trapping excess heat in the atmosphere "
        "via the enhanced greenhouse effect and driving accelerated global climate change."
    )
    options = [
        correct,
        "The Earth loses all atmospheric gravity and drifts into the asteroid belt.",
        "Oxygen levels rise to 90%, causing spontaneous lightning storms in oceans.",
        "All plants on Earth stop growing roots and turn into flying birds.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the disruption of the carbon cycle:\n"
        f"- Photosynthesis absorbs $\text{{CO}}_2$; respiration and fossil fuel combustion release $\text{{CO}}_2$.\n"
        f"- Deforestation reduces $\text{{CO}}_2$ uptake capacity while fossil fuel burning dramatically increases emissions.\n"
        f"- Excess $\text{{CO}}_2$ accumulates as a greenhouse gas, trapping outgoing infrared radiation and causing global warming.\n\n"
        f"**Step 2:** The ecological consequence is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_43_{rng.randint(100000, 999999)}",
        "subskill": "43_greenhouse_effect_and_deforestation_upsetting_gas_balance",
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
            "tier_1": "What happens when trees are cut down and more CO2 is released into the air?",
            "tier_2": "CO2 accumulates, enhancing the greenhouse effect and driving global warming.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["greenhouse_gas_balance_misconception"],
    }


# 44. Biological adaptation sea slug Elysia chlorotica kleptoplasty
def arch_44_biological_adaptation_sea_slug_elysia_chlorotica_kleptoplasty(rng: random.Random) -> Dict[str, Any]:
    slug_name = "*Elysia chlorotica* (the eastern emerald elysia sea slug)"
    alga_name = "*Vaucheria litorea* (green intertidal alga)"
    prompt = (
        f"The marine sea slug {slug_name} feeds on {alga_name}. "
        f"Remarkably, the slug does not digest the algal chloroplasts; instead, it incorporates them into its own gut cells, "
        f"turns brilliant green, and can survive for months in sunlight without eating any food.\n\n"
        f"What biological adaptation allows this animal to manufacture its own food?"
    )
    correct = (
        "Kleptoplasty: the slug retains functional, stolen chloroplasts from its algal food, "
        "allowing the animal to carry out photosynthesis and live on solar energy."
    )
    options = [
        correct,
        "The slug converts seawater directly into solid gold coins using sound vibrations.",
        "The slug has no cells or organs and is a non-living plastic organism.",
        "The slug hibernates by freezing solid inside ocean icebergs.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze this extraordinary biological adaptation:\n"
        f"- Chloroplasts are normally unique to plants and algae.\n"
        f"- {slug_name} practices kleptoplasty (chloroplast symbiosis).\n"
        f"- It captures and maintains intact chloroplasts from consumed algae inside its digestive cells.\n"
        f"- In sunlight, these chloroplasts continue photosynthesising, supplying the slug with glucose.\n\n"
        f"**Step 2:** The adaptation is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_44_{rng.randint(100000, 999999)}",
        "subskill": "44_biological_adaptation_sea_slug_elysia_chlorotica_kleptoplasty",
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
            "tier_1": "What plant organelle does this sea slug steal from green algae to make food?",
            "tier_2": "It retains functional chloroplasts, allowing it to photosynthesise like a plant.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["sea_slug_chloroplast_adaptation_misconception"],
    }


# 45. Aquatic photosynthesis phytoplankton ocean oxygen production
def arch_45_aquatic_photosynthesis_phytoplankton_ocean_oxygen_production(rng: random.Random) -> Dict[str, Any]:
    percent_o2 = rng.choice(["50% to 70%", "more than half"])
    prompt = (
        f"Marine biologists estimate that microscopic single-celled photosynthetic organisms called **phytoplankton** "
        f"(such as diatoms and cyanobacteria) in the surface waters of the world's oceans produce {percent_o2} "
        f"of all the oxygen in Earth's atmosphere.\n\n"
        f"Why is marine phytoplankton considered the critical ecological foundation of global biosphere respiration?"
    )
    correct = (
        "They generate the majority of planetary oxygen through aquatic photosynthesis and form the primary producer base "
        "supporting all marine food webs."
    )
    options = [
        correct,
        "They absorb all sunlight so that underwater volcanoes cannot erupt.",
        "They produce salt crystals to prevent the ocean from turning into fresh milk.",
        "They are microscopic animals that eat carbon dioxide using tiny mechanical teeth.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recognize the global importance of oceanic photosynthesis:\n"
        f"- Phytoplankton cover vast ocean surfaces (71% of Earth).\n"
        f"- Despite their microscopic size, their immense collective biomass produces {percent_o2} of Earth's oxygen.\n"
        f"- They simultaneously absorb enormous quantities of atmospheric carbon dioxide, acting as a massive global carbon sink.\n\n"
        f"**Step 2:** The fundamental significance is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_45_{rng.randint(100000, 999999)}",
        "subskill": "45_aquatic_photosynthesis_phytoplankton_ocean_oxygen_production",
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
            "tier_1": "Where does over half of Earth's breathable oxygen come from: land trees or ocean phytoplankton?",
            "tier_2": "Ocean phytoplankton generate over half of Earth's oxygen through photosynthesis.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ocean_phytoplankton_oxygen_misconception"],
    }


# 46. Comparing photosynthesis and respiration master matrix
def arch_46_comparing_photosynthesis_and_respiration_master_matrix(rng: random.Random) -> Dict[str, Any]:
    comparisons = [
        ("Energy conversion", "Photosynthesis traps radiant light energy into chemical potential energy; Respiration releases chemical energy from glucose as ATP and heat."),
        ("Raw materials (reactants)", "Photosynthesis requires carbon dioxide and water; Respiration requires glucose and oxygen."),
        ("Primary products", "Photosynthesis produces glucose and oxygen; Respiration produces carbon dioxide, water, and energy."),
        ("Cellular organelle", "Photosynthesis takes place in chloroplasts; Respiration takes place in mitochondria."),
    ]
    category, comparison_statement = rng.choice(comparisons)
    prompt = (
        f"Consider the biological comparison between **Photosynthesis** and **Cellular Respiration** "
        f"regarding **{category}**.\n\n"
        f"Which statement accurately contrasts the two processes?"
    )
    correct = comparison_statement
    options = [
        correct,
        f"Both processes take place exclusively in the nucleus of dead bone cells.",
        f"Photosynthesis occurs only in outer space, while respiration occurs only in the Earth's molten core.",
        f"Both processes convert pure granite rock into liquid water with zero chemical reactions.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare Photosynthesis vs Cellular Respiration for {category}:\n"
        f"- {comparison_statement}\n\n"
        f"**Step 2:** The accurate scientific statement is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_46_{rng.randint(100000, 999999)}",
        "subskill": "46_comparing_photosynthesis_and_respiration_master_matrix",
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
            "tier_1": f"Think carefully about how Photosynthesis and Respiration differ in {category}.",
            "tier_2": f"{comparison_statement}",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["photosynthesis_vs_respiration_matrix_misconception"],
    }


# 47. Evaluating experimental error in gas collection
def arch_47_evaluating_experimental_error_in_gas_collection(rng: random.Random) -> Dict[str, Any]:
    errors = [
        ("counting bubbles of varying sizes instead of measuring actual gas volume in a graduated syringe", "bubbles differ in volume, introducing significant measurement inaccuracy into rate calculations"),
        ("failing to allow an aquatic plant 5 minutes to adjust to a new light distance before counting", "the plant has not reached photosynthetic equilibrium at the new light intensity"),
        ("forgetting to use a transparent water shield between a hot incandescent lamp and the plant beaker", "heat from the lamp warms the water, introducing temperature as an uncontrolled confounding variable"),
    ]
    error_desc, reason = rng.choice(errors)
    prompt = (
        f"In an investigation measuring the rate of photosynthesis in pondweed by counting bubbles, a learner makes the following experimental error: "
        f"**{error_desc}**.\n\n"
        f"Why does this error compromise the validity or reliability of the experimental results?"
    )
    correct = f"Because {reason}."
    options = [
        correct,
        "Because it causes the laboratory building to lose gravity and float.",
        "Because it makes the plant turn into an animal within 10 seconds.",
        "Because experiments with pondweed are illegal under national agricultural laws.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Critically evaluate the experimental design flaw:\n"
        f"- Error: {error_desc}.\n"
        f"- Impact on scientific rigor: {reason}.\n"
        f"- A fair test requires all variables except the independent variable to be strictly controlled, and measurement methods must be standardized.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_47_{rng.randint(100000, 999999)}",
        "subskill": "47_evaluating_experimental_error_in_gas_collection",
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
            "tier_1": f"How does {error_desc} distort the data?",
            "tier_2": f"Because {reason}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["photosynthesis_experimental_error_misconception"],
    }


# 48. Food security greenhouse enrichment with carbon dioxide
def arch_48_food_security_greenhouse_enrichment_with_carbon_dioxide(rng: random.Random) -> Dict[str, Any]:
    crops = [
        ("commercial greenhouse tomatoes (*Solanum lycopersicum*) in the Western Cape", 30),
        ("hydroponic sweet bell peppers in Gauteng", 25),
        ("commercial greenhouse cucumbers in KwaZulu-Natal", 35),
    ]
    crop, yield_boost = rng.choice(crops)
    ppm_level = rng.choice([800, 1000, 1200])
    prompt = (
        f"A commercial horticultural farmer pumping carbon dioxide into sealed glass greenhouses "
        f"maintains CO2 levels at {ppm_level} ppm (roughly triple atmospheric levels). "
        f"This increases the harvest yield of {crop} by up to {yield_boost}%.\n\n"
        f"What biological mechanism explains this dramatic increase in crop yield?"
    )
    correct = (
        f"At {ppm_level} ppm, carbon dioxide is no longer a limiting factor; the rate of photosynthesis accelerates, "
        f"allowing plants to synthesize more glucose, starch, and structural biomass in a shorter time."
    )
    options = [
        correct,
        "Carbon dioxide acts as an insecticide that poisons all plant roots so they cannot produce leaves.",
        "High carbon dioxide turns plant leaves into solid gold foil that attracts more rain clouds.",
        "Carbon dioxide creates intense radioactive warmth that forces plants to mutate into giant trees.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Apply the principle of limiting factors to modern agriculture:\n"
        f"- Normal atmospheric $\text{{CO}}_2$ is ~420 ppm, which often limits maximum photosynthetic rate in bright sun.\n"
        f"- Enriched greenhouse atmosphere ({ppm_level} ppm) elevates carbon fixation rates.\n"
        f"- More glucose is produced -> converted to starch and cellulose -> resulting in a {yield_boost}% increase in fruit and crop yield.\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_48_{rng.randint(100000, 999999)}",
        "subskill": "48_food_security_greenhouse_enrichment_with_carbon_dioxide",
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
            "tier_1": "What happens when you remove a limiting factor like CO2 for crop plants?",
            "tier_2": "More CO2 allows faster photosynthesis and higher glucose production for growth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["greenhouse_enrichment_limiting_factor_misconception"],
    }


# 49. Respiration in microorganisms yeast fermentation preview
def arch_49_respiration_in_microorganisms_yeast_fermentation_preview(rng: random.Random) -> Dict[str, Any]:
    applications = [
        ("bread dough rising in traditional South African baking (e.g. roosterkoek or vetkoek)", "carbon dioxide bubbles trapped in gluten dough expand upon baking, creating a soft, aerated texture"),
        ("traditional sorghum beer brewing (umqombothi)", "yeast ferment sugars to produce ethanol (alcohol) and carbon dioxide gas in the absence of oxygen"),
    ]
    application, details = rng.choice(applications)
    prompt = (
        f"Baker's yeast (*Saccharomyces cerevisiae*) is a single-celled fungus that carries out respiration. "
        f"In {application}, {details}.\n\n"
        f"What is this specific form of respiration in the absence of oxygen called, and what are its chemical products?"
    )
    correct = (
        "Anaerobic respiration (alcoholic fermentation); glucose is broken down into **ethanol (alcohol)**, "
        "**carbon dioxide**, and a small amount of usable energy."
    )
    options = [
        correct,
        "Aerobic photosynthesis; carbon dioxide is turned into hydrochloric acid and molten iron.",
        "Nuclear fusion; hydrogen atoms are fused into helium gas under high pressure.",
        "Geological petrification; glucose is converted into solid granite stone.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define alcoholic fermentation in yeast:\n"
        f"- When oxygen is absent (anaerobic conditions), yeast respires via fermentation.\n"
        f"- Equation: $\text{{glucose}} \rightarrow \text{{ethanol}} + \text{{carbon dioxide}} + \text{{energy}}$.\n"
        f"- $\text{{CO}}_2$ causes bread dough to rise, while ethanol is utilized in beverage brewing.\n\n"
        f"**Step 2:** The process and products: **{correct}**."
    )
    return {
        "id": f"ns8_pr_49_{rng.randint(100000, 999999)}",
        "subskill": "49_respiration_in_microorganisms_yeast_fermentation_preview",
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
            "tier_1": "What gas makes bread dough rise and bubble?",
            "tier_2": "Yeast carries out anaerobic fermentation, releasing CO2 and ethanol.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["yeast_fermentation_anaerobic_misconception"],
    }


# 50. Synthetic case study sealed terrarium gas and energy balance
def arch_50_synthetic_case_study_sealed_terrarium_gas_and_energy_balance(rng: random.Random) -> Dict[str, Any]:
    years_sealed = rng.choice([12, 15, 20])
    prompt = (
        f"A hobbyist botanist planted a small spider plant and moss in a large glass carboy (sealed airtight with a cork and wax) "
        f"over {years_sealed} years ago. The bottle has remained 100% airtight ever since, receiving only indirect sunlight on a windowsill. "
        f"The plants inside remain lush, green, and healthy.\n\n"
        f"How can a closed biological ecosystem survive for {years_sealed} years without opening for fresh air or new water?"
    )
    correct = (
        "The system is a closed ecological cycle: water recycles continuously via transpiration and condensation; "
        "photosynthesis uses CO2 and produces O2 in daylight, while respiration consumes O2 and recycles CO2 continuously, "
        "powered exclusively by an external input of radiant solar energy."
    )
    options = [
        correct,
        "The plant learned to live without any chemical atoms or molecules by using psychic energy.",
        "Glass bottles naturally manufacture fresh air and water from ultraviolet moonlight.",
        "The plants died on day one and were replaced by microscopic synthetic plastic replicas.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze matter and energy flows in a closed ecological system:\n"
        f"- Matter (water, carbon, oxygen, nitrogen) is 100% recycled internally:\n"
        f"  - $\text{{H}}_2\text{{O}}$: transpires, condenses on glass walls, and waters roots.\n"
        f"  - Gases: $\text{{O}}_2$ produced by photosynthesis is used in respiration; $\text{{CO}}_2$ released by plant/soil microbes is used in photosynthesis.\n"
        f"- Energy is NOT recycled; it flows through the system (continuous input of radiant solar energy).\n\n"
        f"**Step 2:** The biological explanation is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_case_study_sealed_terrarium_gas_and_energy_balance",
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
            "tier_1": "Can matter be recycled in a closed jar if sunlight keeps entering?",
            "tier_2": "Photosynthesis and respiration recycle oxygen and carbon dioxide, while water recycles continuously.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["sealed_terrarium_matter_energy_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "26_cellular_respiration_definition_and_energy_release": arch_26_cellular_respiration_definition_and_energy_release,
    "27_distinguishing_cellular_respiration_from_breathing": arch_27_distinguishing_cellular_respiration_from_breathing,
    "28_cellular_respiration_word_equation_and_symbols": arch_28_cellular_respiration_word_equation_and_symbols,
    "29_cellular_respiration_reactants_glucose_and_oxygen": arch_29_cellular_respiration_reactants_glucose_and_oxygen,
    "30_cellular_respiration_products_co2_water_and_energy": arch_30_cellular_respiration_products_co2_water_and_energy,
    "31_mitochondria_as_the_cellular_powerhouse_of_respiration": arch_31_mitochondria_as_the_cellular_powerhouse_of_respiration,
    "32_continuous_nature_of_respiration_day_and_night": arch_32_continuous_nature_of_respiration_day_and_night,
    "33_clear_limewater_test_for_carbon_dioxide_milky_precipitate": arch_33_clear_limewater_test_for_carbon_dioxide_milky_precipitate,
    "34_bromothymol_blue_indicator_respiration_colour_shift": arch_34_bromothymol_blue_indicator_respiration_colour_shift,
    "35_germinating_seeds_respiration_investigation_setup": arch_35_germinating_seeds_respiration_investigation_setup,
    "36_vacuum_flask_heat_production_experiment_in_germination": arch_36_vacuum_flask_heat_production_experiment_in_germination,
    "37_control_setup_in_respiration_boiled_sterilized_seeds": arch_37_control_setup_in_respiration_boiled_sterilized_seeds,
    "38_comparing_gas_composition_inhaled_vs_exhaled_air": arch_38_comparing_gas_composition_inhaled_vs_exhaled_air,
    "39_energy_needs_comparing_active_exercise_vs_resting_respiration": arch_39_energy_needs_comparing_active_exercise_vs_resting_respiration,
    "40_interdependence_photosynthesis_and_respiration_carbon_cycle": arch_40_interdependence_photosynthesis_and_respiration_carbon_cycle,
    "41_day_vs_night_net_gas_exchange_in_plants": arch_41_day_vs_night_net_gas_exchange_in_plants,
    "42_compensation_point_rate_photosynthesis_equals_respiration": arch_42_compensation_point_rate_photosynthesis_equals_respiration,
    "43_greenhouse_effect_and_deforestation_upsetting_gas_balance": arch_43_greenhouse_effect_and_deforestation_upsetting_gas_balance,
    "44_biological_adaptation_sea_slug_elysia_chlorotica_kleptoplasty": arch_44_biological_adaptation_sea_slug_elysia_chlorotica_kleptoplasty,
    "45_aquatic_photosynthesis_phytoplankton_ocean_oxygen_production": arch_45_aquatic_photosynthesis_phytoplankton_ocean_oxygen_production,
    "46_comparing_photosynthesis_and_respiration_master_matrix": arch_46_comparing_photosynthesis_and_respiration_master_matrix,
    "47_evaluating_experimental_error_in_gas_collection": arch_47_evaluating_experimental_error_in_gas_collection,
    "48_food_security_greenhouse_enrichment_with_carbon_dioxide": arch_48_food_security_greenhouse_enrichment_with_carbon_dioxide,
    "49_respiration_in_microorganisms_yeast_fermentation_preview": arch_49_respiration_in_microorganisms_yeast_fermentation_preview,
    "50_synthetic_case_study_sealed_terrarium_gas_and_energy_balance": arch_50_synthetic_case_study_sealed_terrarium_gas_and_energy_balance,
}
