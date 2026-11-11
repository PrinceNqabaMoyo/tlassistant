"""Grade 7 Natural Sciences: Term 3 - Heat Energy Transfer Archetypes (01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/03. Heat Energy transfer.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_01_heat_versus_temperature_definitions(rng: random.Random) -> Dict[str, Any]:
    concepts = [
        ("Heat", "The transfer of thermal energy from a hotter object to a colder object, measured in Joules (J)", "Temperature", "A measure of the average kinetic energy of the particles in a substance, measured in degrees Celsius (°C)"),
        ("Thermal energy", "The total kinetic and potential energy of all particles within an object, measured in Joules (J)", "Temperature", "The degree of hotness or coldness indicating average particle kinetic energy, measured in degrees Celsius (°C)")
    ]
    term1, def1, term2, def2 = rng.choice(concepts)
    prompt = (
        f"In natural sciences, **{term1}** and **{term2}** describe related but distinct physical properties.\n\n"
        f"Which statement correctly defines **{term1}** and **{term2}**?"
    )
    correct_opt = f"{term1}: {def1}. {term2}: {def2}."
    options = [
        correct_opt,
        f"{term1} and {term2} are identical synonyms measuring the exact same quantity in degrees Celsius.",
        f"{term1}: {def2}. {term2}: {def1}.",
        f"{term1} is created out of nothing whenever an object reaches room temperature."
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1: Define {term1}:**\n"
        f"{term1} is {def1}.\n\n"
        f"**Step 2: Define {term2}:**\n"
        f"{term2} is {def2}.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_01_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "01_heat_versus_temperature_definitions",
        "question_family_id": "01_heat_versus_temperature_definitions",
        "hints": {
            "tier_1": "Recall which quantity is energy transferred and which is a measure of particle motion speed.",
            "tier_2": "Heat is measured in Joules; temperature is measured in degrees Celsius.",
            "tier_3": "Heat is the transfer of thermal energy, while temperature is average kinetic energy of particles."
        },
        "misconception_tags": ["confusing_heat_with_temperature"]
    }


def arch_02_measuring_temperature_degrees_celsius(rng: random.Random) -> Dict[str, Any]:
    liquids = [
        ("pure boiling water at standard atmospheric pressure", "100", "0", "room temperature"),
        ("pure melting ice at sea level", "0", "100", "body temperature"),
        ("normal human body temperature", "37", "0", "boiling point of water"),
        ("comfortable indoor room temperature", "21", "100", "freezing point of water")
    ]
    item, correct_val, fake1, fake2 = rng.choice(liquids)
    prompt = (
        f"A laboratory alcohol thermometer calibrated in degrees Celsius ($^\\circ\\text{{C}}$) is used to measure the temperature of {item}.\n\n"
        f"What is the expected reading on the Celsius scale?"
    )
    correct_opt = f"{correct_val} °C"
    options = [
        correct_opt,
        f"{fake1} °C",
        f"{rng.choice(['273', '50', '80'])} °C",
        f"-{correct_val} °C"
    ]
    options = list(dict.fromkeys(options))
    while len(options) < 4:
        options.append(f"{rng.randint(15, 60)} °C")
    rng.shuffle(options)
    sol = (
        f"**Step 1: Reference standard Celsius fixed points:**\n"
        f"- Freezing/melting point of pure water: $0^\\circ\\text{{C}}$\n"
        f"- Normal body temperature: $37^\\circ\\text{{C}}$\n"
        f"- Boiling point of pure water at sea level: $100^\\circ\\text{{C}}$\n\n"
        f"**Step 2: Apply to {item}:**\n"
        f"The standard accepted value is **{correct_opt}**."
    )
    return {
        "id": f"ns7_ht_02_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "02_measuring_temperature_degrees_celsius",
        "question_family_id": "02_measuring_temperature_degrees_celsius",
        "hints": {
            "tier_1": "Consider standard reference temperatures on the Celsius scale.",
            "tier_2": "Water boils at 100 °C and freezes at 0 °C.",
            "tier_3": f"The temperature of {item} is {correct_val} °C."
        },
        "misconception_tags": ["inaccurate_temperature_benchmarks"]
    }


def arch_03_thermal_energy_and_particle_kinetic_energy(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("water in a kettle being heated from 20 °C to 80 °C", "increase", "vibrate and move faster, with greater average kinetic energy", "move slower and lock into crystals"),
        ("a copper block cooling down from 90 °C to 25 °C", "decrease", "vibrate more slowly, possessing lower average kinetic energy", "speed up and escape into the air"),
        ("air inside a closed balloon placed in hot sunlight", "increase", "move faster and collide with the balloon walls with greater kinetic energy", "stop moving completely")
    ]
    scenario, trend, behavior, opposite = rng.choice(substances)
    prompt = (
        f"Consider {scenario}.\n\n"
        f"According to the particle model of matter, how do the motion and kinetic energy of the particles change as the thermal energy changes?"
    )
    correct_opt = f"The average kinetic energy of the particles {trend}s; the particles {behavior}."
    options = [
        correct_opt,
        f"The average kinetic energy remains unchanged because particles never change their speed.",
        f"The particles {opposite}.",
        f"The particles expand individually in physical size while remaining completely motionless."
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1: Particle Model of Matter:**\n"
        f"Temperature is directly proportional to the average kinetic energy of particles.\n\n"
        f"**Step 2: Connect thermal energy to particle motion:**\n"
        f"When thermal energy causes temperature to {trend}, particles {behavior}.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_03_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "03_thermal_energy_and_particle_kinetic_energy",
        "question_family_id": "03_thermal_energy_and_particle_kinetic_energy",
        "hints": {
            "tier_1": "What does heating do to particle vibration or motion?",
            "tier_2": "Higher thermal energy means higher particle kinetic energy.",
            "tier_3": f"Particles {behavior}."
        },
        "misconception_tags": ["particles_expand_fallacy"]
    }


def arch_04_direction_of_heat_transfer_gradient(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("an ice cube placed into a glass of warm water at 25 °C", "from the warm water (higher temperature) to the ice cube (lower temperature)", "coldness transfers from the ice into the water"),
        ("a hot metal spoon at 80 °C placed into a bowl of cool soup at 20 °C", "from the hot spoon (higher temperature) to the cooler soup (lower temperature)", "cold flows from the soup into the spoon"),
        ("a person with skin temperature 35 °C touching a cold brass doorknob at 15 °C", "from the person's hand (higher temperature) to the brass doorknob (lower temperature)", "cold energy leaves the brass and enters the hand"),
        ("a freshly baked loaf of bread at 95 °C cooling on a kitchen rack at 22 °C", "from the hot bread (higher temperature) to the cooler surrounding air (lower temperature)", "coolness from the air travels inside the bread")
    ]
    situation, correct_dir, wrong_dir = rng.choice(scenarios)
    prompt = (
        f"A student investigates heat transfer in the following situation: **{situation}**.\n\n"
        f"In which direction does thermal energy naturally transfer?"
    )
    correct_opt = f"Thermal energy transfers {correct_dir}."
    options = [
        correct_opt,
        f"Thermal energy transfers {wrong_dir}.",
        "Thermal energy transfers equally in both directions simultaneously without net change.",
        "Thermal energy cannot transfer between two objects with different temperatures."
    ]
    rng.shuffle(options)
    sol = (
        f"**Rule of Thermal Transfer:**\n"
        f"Heat energy ALWAYS spontaneously flows from a region or object of **higher temperature** to one of **lower temperature**.\n"
        f"'Cold' is simply the absence of thermal energy; cold does not flow.\n\n"
        f"**Application:** Thermal energy flows {correct_dir}."
    )
    return {
        "id": f"ns7_ht_04_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "04_direction_of_heat_transfer_gradient",
        "question_family_id": "04_direction_of_heat_transfer_gradient",
        "hints": {
            "tier_1": "Does heat travel from hot to cold or cold to hot?",
            "tier_2": "Thermal energy always moves from higher temperature to lower temperature.",
            "tier_3": f"Heat transfers {correct_dir}."
        },
        "misconception_tags": ["cold_flow_fallacy"]
    }


def arch_05_thermal_equilibrium_concept(rng: random.Random) -> Dict[str, Any]:
    t_hot = rng.choice([60, 70, 80, 90])
    t_cold = rng.choice([10, 15, 20, 25])
    t_eq = (t_hot + t_cold) // 2
    prompt = (
        f"A beaker containing $100\\text{{ cm}}^3$ of hot water at ${t_hot}^\\circ\\text{{C}}$ is mixed thoroughly with $100\\text{{ cm}}^3$ of cold water at ${t_cold}^\\circ\\text{{C}}$ in an insulated container.\n\n"
        f"What happens to the temperature and heat transfer once the mixture reaches **thermal equilibrium**?"
    )
    correct_opt = f"Net heat transfer ceases, and both bodies of water reach an intermediate equal temperature of approximately {t_eq} °C."
    options = [
        correct_opt,
        f"The temperature rises to {t_hot + t_cold} °C because heat combines cumulatively.",
        f"The hot water stays at {t_hot} °C while the cold water drops to 0 °C.",
        f"The water permanently fluctuates between {t_cold} °C and {t_hot} °C without ever settling."
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1: Understand Thermal Equilibrium:**\n"
        f"Thermal equilibrium occurs when two objects or regions in thermal contact reach the exact same temperature.\n\n"
        f"**Step 2: Calculate intermediate temperature:**\n"
        f"For equal masses of identical substance: $T_\\text{{eq}} = \\frac{{{t_hot} + {t_cold}}}{{2}} = {t_eq}^\\circ\\text{{C}}$.\n\n"
        f"**Step 3: State of heat transfer:**\n"
        f"Once thermal equilibrium is established, net heat transfer between them becomes zero.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_05_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "05_thermal_equilibrium_concept",
        "question_family_id": "05_thermal_equilibrium_concept",
        "hints": {
            "tier_1": "What does equilibrium mean for temperature and heat flow?",
            "tier_2": "Heat flows until both are at the same temperature.",
            "tier_3": f"They balance at an equal intermediate temperature (~{t_eq} °C)."
        },
        "misconception_tags": ["temperature_additive_fallacy"]
    }


def arch_06_particle_mechanism_of_conduction_in_solids(rng: random.Random) -> Dict[str, Any]:
    solids = [
        "an iron poker placed in hot coals",
        "a copper rod heated by a Bunsen burner at one end",
        "a stainless steel skewer held over a braai fire"
    ]
    material = rng.choice(solids)
    prompt = (
        f"When one end of {material} is heated, the opposite end eventually becomes hot through **conduction**.\n\n"
        f"Which particle-level process accurately explains how thermal energy travels through the solid?"
    )
    correct_opt = "Particles at the hot end vibrate vigorously and collide with neighbouring particles, transferring kinetic energy along the lattice without particles changing their fixed positions."
    options = [
        correct_opt,
        "Hot particles physically detach from the heated end and flow like a liquid to the cooler end.",
        "Particles expand to tenfold their normal size, pushing heat waves through internal empty spaces.",
        "The solid rod absorbs cold particles from the handle and destroys them in the flame."
    ]
    rng.shuffle(options)
    sol = (
        f"**Conduction Mechanism:**\n"
        f"1. In a solid, particles are closely packed in fixed lattice positions.\n"
        f"2. Heating increases the vibrational kinetic energy of particles at the heated end.\n"
        f"3. These vibrating particles collide with adjacent particles, passing on vibrational energy sequentially.\n"
        f"4. The particles DO NOT move from one end of the solid to the other.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_06_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "06_particle_mechanism_of_conduction_in_solids",
        "question_family_id": "06_particle_mechanism_of_conduction_in_solids",
        "hints": {
            "tier_1": "Can particles in a solid move freely from place to place?",
            "tier_2": "Particles in solids vibrate in fixed positions and collide with neighbours.",
            "tier_3": "Vibrating particles collide and pass kinetic energy along the lattice."
        },
        "misconception_tags": ["particle_migration_in_solids"]
    }


def arch_07_role_of_free_electrons_in_metal_conduction(rng: random.Random) -> Dict[str, Any]:
    metals = ["copper", "silver", "aluminium", "brass"]
    non_metals = ["wood", "glass", "plastic", "rubber"]
    m = rng.choice(metals)
    nm = rng.choice(non_metals)
    prompt = (
        f"Metals such as **{m}** conduct heat far more rapidly than non-metals such as **{nm}**.\n\n"
        f"What microscopic feature of metals accounts for this superior thermal conductivity?"
    )
    correct_opt = "Metals contain a sea of delocalised (free) electrons that can move rapidly through the structure and transfer kinetic energy directly to distant ions."
    options = [
        correct_opt,
        "Metals have no particles and therefore allow heat to pass without any resistance.",
        "Non-metals contain magnetic barriers that repel all forms of thermal vibrations.",
        "Metals create heat internally by spontaneous chemical combustion when touched."
    ]
    rng.shuffle(options)
    sol = (
        f"**Metallic Conduction Advantage:**\n"
        f"- In non-metals, conduction occurs ONLY via slow particle-to-particle lattice vibrations.\n"
        f"- In metals, there are delocalised (free) electrons in addition to lattice vibrations.\n"
        f"- When heated, these free electrons gain kinetic energy and diffuse rapidly through the metal lattice, colliding with distant metal ions and transferring energy very quickly.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_07_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "07_role_of_free_electrons_in_metal_conduction",
        "question_family_id": "07_role_of_free_electrons_in_metal_conduction",
        "hints": {
            "tier_1": "What subatomic particles can wander freely inside metals?",
            "tier_2": "Free or delocalised electrons carry heat energy through the lattice.",
            "tier_3": "Delocalised electrons move quickly and collide with ions throughout the metal."
        },
        "misconception_tags": ["electrons_only_for_electricity"]
    }


def arch_08_comparing_thermal_conductivity_of_different_metals(rng: random.Random) -> Dict[str, Any]:
    metals_ordered = ["Copper", "Aluminium", "Brass", "Iron", "Lead"]
    prompt = (
        f"In a science investigation, identical rods made of copper, aluminium, brass, and iron are heated at one end with equal heat inputs.\n\n"
        f"Which list correctly ranks these metals from **fastest / best thermal conductor** to **slowest / poorest thermal conductor**?"
    )
    correct_opt = "Copper > Aluminium > Brass > Iron"
    options = [
        correct_opt,
        "Iron > Brass > Aluminium > Copper",
        "Brass > Iron > Copper > Aluminium",
        "All four metals conduct heat at the exact same identical rate"
    ]
    rng.shuffle(options)
    sol = (
        f"**Standard Thermal Conductivity Order of Common Metals:**\n"
        f"1. Copper (highest conductivity among everyday metals ~400 W/m·K)\n"
        f"2. Aluminium (~237 W/m·K)\n"
        f"3. Brass (~110 W/m·K)\n"
        f"4. Iron / Steel (~50-80 W/m·K)\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_08_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "08_comparing_thermal_conductivity_of_different_metals",
        "question_family_id": "08_comparing_thermal_conductivity_of_different_metals",
        "hints": {
            "tier_1": "Which metal is famous for high-efficiency heat sinks and cookware bases?",
            "tier_2": "Copper is the best conductor, followed by aluminium.",
            "tier_3": "The ranking is Copper > Aluminium > Brass > Iron."
        },
        "misconception_tags": ["all_metals_equal_conductors"]
    }


def arch_09_wax_melting_pin_drop_conduction_experiment(rng: random.Random) -> Dict[str, Any]:
    distances = [5, 10, 15, 20]
    prompt = (
        f"Four metal pins (A, B, C, D) are attached to a horizontal copper rod using equal blobs of candle wax. "
        f"Pin A is located at 5 cm from the heated end, Pin B at 10 cm, Pin C at 15 cm, and Pin D at 20 cm. "
        f"A spirit burner heats the tip of the rod at 0 cm.\n\n"
        f"In what order will the pins drop off the rod as heat travels along it?"
    )
    correct_opt = "A drops first, then B, then C, and finally D"
    options = [
        correct_opt,
        "D drops first, then C, then B, and finally A",
        "All four pins drop simultaneously at the exact same second",
        "Pin B drops first because heat jumps to the middle before spreading outwards"
    ]
    rng.shuffle(options)
    sol = (
        f"**Conduction Progression:**\n"
        f"Thermal energy travels sequentially from the heat source along the rod.\n"
        f"- Pin A (5 cm) reaches the melting point of wax first -> drops first.\n"
        f"- Pin B (10 cm) receives heat next -> drops second.\n"
        f"- Pin C (15 cm) receives heat next -> drops third.\n"
        f"- Pin D (20 cm) is farthest from heat source -> drops last.\n\n"
        f"**Order:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_09_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "09_wax_melting_pin_drop_conduction_experiment",
        "question_family_id": "09_wax_melting_pin_drop_conduction_experiment",
        "hints": {
            "tier_1": "Does heat arrive at closer pins or farther pins first?",
            "tier_2": "The pin closest to the flame gets hot enough to melt wax first.",
            "tier_3": "Order from closest to farthest: A, then B, then C, then D."
        },
        "misconception_tags": ["instantaneous_conduction_fallacy"]
    }


def arch_10_why_metal_feels_colder_than_wood_at_same_temp(rng: random.Random) -> Dict[str, Any]:
    temp = rng.choice([16, 18, 20, 22])
    prompt = (
        f"A metal spoon and a wooden spoon have both been left on a kitchen counter in a room at ${temp}^\\circ\\text{{C}}$ overnight. "
        f"When a student touches both spoons, the metal spoon feels noticeably colder than the wooden spoon.\n\n"
        f"What is the scientific explanation for this observation?"
    )
    correct_opt = f"Both spoons are at the exact same temperature ({temp} °C), but metal is a much better conductor and conducts heat away from your finger much faster than wood."
    options = [
        correct_opt,
        f"The metal spoon is actually at a colder temperature (around 5 °C) because metals attract cold from the air.",
        "The wooden spoon produces its own internal heat energy through biological metabolism.",
        "Human skin cannot detect temperature differences accurately when touching solid objects."
    ]
    rng.shuffle(options)
    sol = (
        f"**Scientific Analysis:**\n"
        f"1. Both objects have been in the same room overnight, so they are in **thermal equilibrium** with the room at ${temp}^\\circ\\text{{C}}$.\n"
        f"2. Your hand is at body temperature (~$37^\\circ\\text{{C}}$), so heat flows from your hand into the object.\n"
        f"3. Metal is a **good thermal conductor**: it transfers heat away from your skin rapidly, cooling nerve endings in your finger quickly.\n"
        f"4. Wood is a **thermal insulator**: it conducts heat away very slowly, so the skin in contact stays warm.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_10_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "10_why_metal_feels_colder_than_wood_at_same_temp",
        "question_family_id": "10_why_metal_feels_colder_than_wood_at_same_temp",
        "hints": {
            "tier_1": "Are both objects at the same temperature if left in the same room overnight?",
            "tier_2": "Our skin senses the rate of heat loss, not the true temperature.",
            "tier_3": "Metal conducts heat away from the finger much faster than wood."
        },
        "misconception_tags": ["feeling_colder_equals_colder_temp"]
    }


def arch_11_practical_design_of_cooking_pots_and_handles(rng: random.Random) -> Dict[str, Any]:
    pots = [
        ("a stainless steel frying pan with a silicone-covered handle", "stainless steel base conducts heat quickly to food, while the silicone handle insulates your hand from burning"),
        ("a cast iron potjie pot with a wooden or thick heat-resistant handle", "cast iron holds and conducts heat evenly to the stew, while the wood insulates against burns"),
        ("a copper-bottomed saucepan with a bakelite plastic handle", "copper rapidly conducts heat from the stove plate, while bakelite insulates hands from heat")
    ]
    cookware, explanation = rng.choice(pots)
    prompt = (
        f"In household cooking, cookware is engineered using deliberate material combinations, such as **{cookware}**.\n\n"
        f"Why are two different materials chosen for the base and the handle?"
    )
    correct_opt = f"The {explanation}."
    options = [
        correct_opt,
        "The base must insulate heat while the handle must conduct heat to cool down the pot.",
        "Both parts are made of identical metals but painted different colours for appearance.",
        "The handle conducts heat into the cook's hand to provide sensory feedback on boiling temperature."
    ]
    rng.shuffle(options)
    sol = (
        f"**Cookware Engineering Principle:**\n"
        f"- The base requires a **thermal conductor** (copper, aluminium, steel) to quickly and evenly transfer heat from the stove plate into the food.\n"
        f"- The handle requires a **thermal insulator** (plastic, wood, silicone) to prevent heat conduction from reaching the user's hand and causing burns.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_11_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "11_practical_design_of_cooking_pots_and_handles",
        "question_family_id": "11_practical_design_of_cooking_pots_and_handles",
        "hints": {
            "tier_1": "What do we want the base to do vs what do we want the handle to do?",
            "tier_2": "Base should conduct heat to food; handle should insulate hands.",
            "tier_3": f"The {explanation}."
        },
        "misconception_tags": ["uniform_material_usage"]
    }


def arch_12_conduction_in_liquids_and_gases_poor_conductors(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a science demonstration, water at the top of a boiling tube is heated with a flame while an ice cube held down by a metal gauze at the bottom remains frozen. "
        f"Similarly, trapped air inside double-glazed windows stops heat loss.\n\n"
        f"What do these phenomena demonstrate regarding conduction in liquids and gases?"
    )
    correct_opt = "Liquids and gases are generally very poor conductors of heat because their particles are spaced much farther apart than in solids, resulting in far fewer particle collisions."
    options = [
        correct_opt,
        "Liquids and gases conduct heat faster than any solid metal because particles move freely.",
        "Water has zero thermal capacity and can never absorb or transfer heat.",
        "Air absorbs heat and converts it into mechanical gravity waves."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermal Conduction in Fluids:**\n"
        f"1. Conduction depends on direct collisions between tightly packed neighbouring particles.\n"
        f"2. In liquids, particles are less tightly packed than solids; in gases, particles are far apart.\n"
        f"3. Therefore, pure conduction is extremely slow and inefficient in water and gases (air).\n"
        f"4. This is why trapped air is widely used as a thermal insulator.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_12_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "12_conduction_in_liquids_and_gases_poor_conductors",
        "question_family_id": "12_conduction_in_liquids_and_gases_poor_conductors",
        "hints": {
            "tier_1": "How far apart are particles in liquids and gases compared to solids?",
            "tier_2": "Greater distance between particles makes conduction very inefficient.",
            "tier_3": "Liquids and gases are poor conductors because their particles are widely spaced."
        },
        "misconception_tags": ["all_states_conduct_equally"]
    }


def arch_13_particle_mechanism_of_convection_in_fluids(rng: random.Random) -> Dict[str, Any]:
    fluids = ["water in a pot on a stove", "air inside a room with a floor heater", "soup in a saucepan"]
    f = rng.choice(fluids)
    prompt = (
        f"When {f} is heated from below, heat spreads throughout the entire volume predominantly by **convection**.\n\n"
        f"What is the step-by-step mechanism of convection at the particle level?"
    )
    correct_opt = "Heated particles gain kinetic energy, move faster, and spread further apart -> the fluid expands and becomes less dense -> warm less dense fluid rises, while cooler denser fluid sinks to replace it."
    options = [
        correct_opt,
        "Heated particles shrink into tiny dots, become heavier, and sink directly to the bottom where they stay permanently.",
        "Particles vibrate in rigid locked positions and pass heat along like a line of dominoes.",
        "Heat creates electrical lightning sparks between particles that jump instantly across the fluid."
    ]
    rng.shuffle(options)
    sol = (
        f"**Step-by-Step Convection Cycle:**\n"
        f"1. Heating fluid -> particles absorb kinetic energy and move faster.\n"
        f"2. Particles move further apart (fluid expands in volume).\n"
        f"3. Density decreases ($\\text{{density}} = \\frac{{\\text{{mass}}}}{{\\text{{volume}}}}$).\n"
        f"4. Less dense warm fluid rises.\n"
        f"5. Denser, cooler fluid at the top sinks down to take its place, where it is heated in turn.\n"
        f"6. This continuous cyclic movement forms a **convection current**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_13_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "13_particle_mechanism_of_convection_in_fluids",
        "question_family_id": "13_particle_mechanism_of_convection_in_fluids",
        "hints": {
            "tier_1": "What happens to the spacing between particles when a fluid is heated?",
            "tier_2": "Particles spread apart, density decreases, and warm fluid rises.",
            "tier_3": "Heated fluid expands, becomes less dense, and rises, setting up a current."
        },
        "misconception_tags": ["particles_themselves_expand"]
    }


def arch_14_density_changes_driving_convection_currents(rng: random.Random) -> Dict[str, Any]:
    temp_warm = rng.choice([50, 60, 70])
    temp_cool = rng.choice([15, 20, 25])
    prompt = (
        f"A sample of water at ${temp_warm}^\\circ\\text{{C}}$ is placed in contact with water at ${temp_cool}^\\circ\\text{{C}}$.\n\n"
        f"How do the **densities** of the two water samples compare, and how does this difference drive a convection current?"
    )
    correct_opt = f"The water at {temp_warm} °C has a lower density than the water at {temp_cool} °C; because it is less dense, it floats/rises above the denser cooler water."
    options = [
        correct_opt,
        f"The water at {temp_warm} °C has a higher density and sinks heavily to the bottom.",
        "Both samples have identical densities regardless of temperature.",
        f"The water at {temp_cool} °C evaporates immediately because cold water is less dense than steam."
    ]
    rng.shuffle(options)
    sol = (
        f"**Density and Temperature Relationship:**\n"
        f"- When water is heated from {temp_cool} °C to {temp_warm} °C, particles move faster and spread farther apart.\n"
        f"- The volume increases while mass remains constant, so density decreases.\n"
        f"- In a gravitational field, less dense fluids experience an upward buoyant force and rise.\n"
        f"- Denser fluid sinks under gravity.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_14_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "14_density_changes_driving_convection_currents",
        "question_family_id": "14_density_changes_driving_convection_currents",
        "hints": {
            "tier_1": "Does hot water expand or contract compared to cold water?",
            "tier_2": "Hot water expands and has lower density, so it floats upwards.",
            "tier_3": f"Water at {temp_warm} °C is less dense and rises above denser {temp_cool} °C water."
        },
        "misconception_tags": ["hot_fluids_are_heavier"]
    }


def arch_15_potassium_permanganate_convection_experiment(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A single crystal of potassium permanganate is dropped carefully using a drinking straw to the bottom corner of a beaker of cold water. "
        f"A gentle Bunsen burner flame is placed directly beneath that corner.\n\n"
        f"What visible purple path does the dissolving potassium permanganate trace in the water?"
    )
    correct_opt = "A stream of purple water rises vertically above the flame, spreads across the surface, sinks down the cooler opposite side, and flows along the bottom back to the flame."
    options = [
        correct_opt,
        "The purple colour stays strictly at the bottom corner and never moves at all.",
        "The purple dye instantly explodes into steam and shoots out of the beaker in a straight line.",
        "The purple colour sinks deeper into the glass itself without circulating in the water."
    ]
    rng.shuffle(options)
    sol = (
        f"**Convection Demonstration with Potassium Permanganate:**\n"
        f"1. Water at the bottom corner heats up, expands, and decreases in density.\n"
        f"2. The heated water carries the dissolved purple crystals upward towards the surface.\n"
        f"3. At the surface, the water cools as it meets the surrounding air.\n"
        f"4. As it cools, it becomes denser and sinks down the opposite cooler side of the beaker.\n"
        f"5. It flows along the bottom back towards the flame to replace the rising water, completing a visible convection loop.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_15_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "15_potassium_permanganate_convection_experiment",
        "question_family_id": "15_potassium_permanganate_convection_experiment",
        "hints": {
            "tier_1": "What path does a convection current follow in a heated beaker?",
            "tier_2": "Rises above the heat, travels across the surface, sinks on the cold side.",
            "tier_3": "The purple stream rises above the flame, moves across, and sinks on the cooler side."
        },
        "misconception_tags": ["random_diffusion_vs_convection"]
    }


def arch_16_smoke_box_chimney_air_convection_demonstration(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A wooden convection box has a transparent front and two glass chimneys (Chimney 1 and Chimney 2). "
        f"A lit candle is positioned inside the box directly below Chimney 1. "
        f"A piece of smouldering touch paper emitting thick smoke is held above Chimney 2.\n\n"
        f"What happens to the path of the smoke?"
    )
    correct_opt = "Smoke is drawn down through Chimney 2 into the box, moves across the floor toward the candle, and exits upwards through Chimney 1."
    options = [
        correct_opt,
        "Smoke rises immediately away from Chimney 2 into the ceiling and never enters the box.",
        "Smoke enters Chimney 1, blows out the candle flame, and exits through Chimney 2.",
        "The smoke forms a stationary ball hovering between the two chimneys without moving."
    ]
    rng.shuffle(options)
    sol = (
        f"**Convection Box Mechanism:**\n"
        f"1. The lit candle heats the air above it beneath Chimney 1.\n"
        f"2. The warm air expands, becomes less dense, and rises out through Chimney 1.\n"
        f"3. This upward draft lowers the air pressure inside the box.\n"
        f"4. Cooler, denser outside air (carrying the smoke) is sucked down into Chimney 2 to replace the rising air.\n"
        f"5. The smoke travels across the bottom of the box to the candle, warms up, and exits out Chimney 1.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_16_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "16_smoke_box_chimney_air_convection_demonstration",
        "question_family_id": "16_smoke_box_chimney_air_convection_demonstration",
        "hints": {
            "tier_1": "Which chimney has warm rising air?",
            "tier_2": "Air rises above the candle (Chimney 1), pulling cool air down the other chimney.",
            "tier_3": "Smoke is drawn down Chimney 2, moves across the floor, and rises out Chimney 1."
        },
        "misconception_tags": ["smoke_always_rises_freely"]
    }


def arch_17_sea_breeze_daytime_convection_cycle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Along the South African coastline (e.g. Durban, Cape Town) on a sunny summer afternoon, a refreshing **sea breeze** blows inland from the ocean toward the shore.\n\n"
        f"What creates this daytime sea breeze?"
    )
    correct_opt = "Land heats up faster than the ocean, warming the air above it; this warm air expands and rises, and cooler, denser air from above the sea moves in to replace it."
    options = [
        correct_opt,
        "The ocean boils during midday and pushes steam waves onto the dry land.",
        "The spinning of Earth pushes water molecules physically against coastal cliffs.",
        "Land cools down to near freezing during the day, pulling hot sea air towards it."
    ]
    rng.shuffle(options)
    sol = (
        f"**Daytime Sea Breeze Mechanism:**\n"
        f"1. Land has a lower heat capacity than water and heats up much faster under the Sun.\n"
        f"2. Air above the land heats up, expands, becomes less dense, and rises.\n"
        f"3. Air above the cooler ocean remains denser.\n"
        f"4. The cool, dense sea air moves inland across the beach to take the place of the rising air, creating a **sea breeze**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_17_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "17_sea_breeze_daytime_convection_cycle",
        "question_family_id": "17_sea_breeze_daytime_convection_cycle",
        "hints": {
            "tier_1": "Does land or sea heat up faster in the daytime sun?",
            "tier_2": "Land heats faster -> warm air rises over land -> cool air flows in from the sea.",
            "tier_3": "Warm air rises over the heated land, drawing in cooler air from the sea."
        },
        "misconception_tags": ["ocean_heats_faster_than_land"]
    }


def arch_18_land_breeze_nighttime_convection_cycle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"At night along the coastline, the direction of coastal wind reverses, blowing offshore from the land out toward the sea as a **land breeze**.\n\n"
        f"What causes this nighttime wind reversal?"
    )
    correct_opt = "Land cools down much faster than the sea at night; the air over the warmer sea is now less dense and rises, drawing cooler, denser air from the land out to sea."
    options = [
        correct_opt,
        "The Moon's gravity pulls all air away from continents toward deep oceanic trenches.",
        "Plants on land release high-pressure oxygen gusts that blow towards the water.",
        "The ocean freezes completely every night, repelling all surrounding atmosphere."
    ]
    rng.shuffle(options)
    sol = (
        f"**Nighttime Land Breeze Mechanism:**\n"
        f"1. At night without solar radiation, land loses thermal energy and cools down rapidly.\n"
        f"2. Water has a high specific heat capacity and retains its thermal energy much longer, making the sea warmer than the land at night.\n"
        f"3. Air above the warmer sea expands, becomes less dense, and rises.\n"
        f"4. Cooler, denser air from over the land flows out towards the sea to replace it, forming a **land breeze**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_18_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "18_land_breeze_nighttime_convection_cycle",
        "question_family_id": "18_land_breeze_nighttime_convection_cycle",
        "hints": {
            "tier_1": "Which stays warmer at night: the land or the sea?",
            "tier_2": "The sea stays warmer at night, so air rises over the sea.",
            "tier_3": "Air rises over the warmer sea, drawing cooler air from the land out to sea."
        },
        "misconception_tags": ["land_stays_warmer_at_night"]
    }


def arch_19_placement_of_heaters_near_floor(rng: random.Random) -> Dict[str, Any]:
    heaters = ["an electric bar heater", "a hydronic wall radiator", "an oil-filled fin heater"]
    h = rng.choice(heaters)
    prompt = (
        f"In architectural building design, heating appliances like **{h}** are almost always mounted close to the floor rather than near the ceiling.\n\n"
        f"What scientific reason related to heat transfer justifies placing heaters near the floor?"
    )
    correct_opt = "Warm air rises by convection; by placing the heater at floor level, rising warm air circulates through the entire room as cooler air sinks to be reheated."
    options = [
        correct_opt,
        "Floor tiles conduct electric current better than ceiling plaster.",
        "Heat naturally falls downward under gravity, so heaters must be placed low to catch falling heat.",
        "If heaters were mounted on the ceiling, the room's oxygen would turn into nitrogen."
    ]
    rng.shuffle(options)
    sol = (
        f"**Heater Placement & Convection:**\n"
        f"1. A heater warms the air in its immediate vicinity.\n"
        f"2. Warm air expands, becomes less dense, and rises towards the ceiling.\n"
        f"3. Cooler, denser air near the ceiling and upper walls is displaced and sinks towards the floor.\n"
        f"4. Placing the heater low creates an effective, room-wide convection current that warms the living space evenly.\n"
        f"5. (If placed on the ceiling, warm air would stay trapped near the ceiling and the floor would remain cold).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_19_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "19_placement_of_heaters_near_floor",
        "question_family_id": "19_placement_of_heaters_near_floor",
        "hints": {
            "tier_1": "Does warm air rise or sink?",
            "tier_2": "Warm air rises. A floor heater sets up a full convection loop.",
            "tier_3": "Warm air rises, circulating heat through the entire room from floor to ceiling."
        },
        "misconception_tags": ["heat_sinks_downward"]
    }


def arch_20_placement_of_air_conditioners_near_ceiling(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Unlike room heaters, air conditioning cooling units and ventilation cooling vents are mounted high up on walls or in the ceiling.\n\n"
        f"Why are air cooling units placed near the ceiling to cool a room effectively?"
    )
    correct_opt = "Cool air is denser than warm air and sinks naturally toward the floor, displacing warmer air upward into the unit to establish an effective cooling convection current."
    options = [
        correct_opt,
        "Cool air has negative gravity and pushes warm air through the windows.",
        "Ceilings are always made of cold metal that recharges the refrigerant gas.",
        "Air conditioners produce liquid ice crystals that must fall through the air to melt."
    ]
    rng.shuffle(options)
    sol = (
        f"**Cooling Unit Placement & Convection:**\n"
        f"1. An air conditioner chills the air passing through its evaporator coils.\n"
        f"2. Cool air contracts, becomes denser, and sinks toward the floor.\n"
        f"3. As this cold air descends, it pushes warmer, less dense air upwards towards the unit.\n"
        f"4. This sets up a continuous downward-convection loop that cools the occupied zone of the room efficiently.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_20_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "20_placement_of_air_conditioners_near_ceiling",
        "question_family_id": "20_placement_of_air_conditioners_near_ceiling",
        "hints": {
            "tier_1": "Does cold air rise or sink?",
            "tier_2": "Cold air is denser and sinks toward the floor.",
            "tier_3": "Cold air sinks, creating a downward convection current that cools the room."
        },
        "misconception_tags": ["cold_air_rises_fallacy"]
    }


def arch_21_geyser_heating_element_placement_at_bottom(rng: random.Random) -> Dict[str, Any]:
    vol = rng.choice([100, 150, 200])
    prompt = (
        f"In a domestic {vol}-litre electric water geyser, the electrical heating element is located near the bottom of the tank, while the hot water outlet pipe draws water from the very top.\n\n"
        f"Why must the heating element be situated near the bottom of the cylinder?"
    )
    correct_opt = "Heating water at the bottom creates convection currents that circulate and heat the entire tank; if placed at the top, only the top layer would warm up because warm water cannot sink."
    options = [
        correct_opt,
        "Water pressure at the bottom is zero, which prevents electrical short circuits.",
        "Cold water is chemically acidic and would dissolve the metal element if placed at the top.",
        "Placing the element at the bottom makes the water boil into gas immediately to fill the tank."
    ]
    rng.shuffle(options)
    sol = (
        f"**Geyser Heating Mechanism:**\n"
        f"- Water is a very poor thermal conductor.\n"
        f"- Heating at the bottom causes the bottom water to expand, decrease in density, and rise.\n"
        f"- Cooler water at the top sinks down to the element, creating a full convection current that heats the entire {vol} L of water uniformly.\n"
        f"- If the element were at the top, warm water would simply remain at the top, leaving the bottom water cold.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_21_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "21_geyser_heating_element_placement_at_bottom",
        "question_family_id": "21_geyser_heating_element_placement_at_bottom",
        "hints": {
            "tier_1": "Can warm water sink to the bottom on its own?",
            "tier_2": "Warm water rises. The bottom element ensures convection heats the whole tank.",
            "tier_3": "Heating at the bottom drives convection; top placement would leave bottom water cold."
        },
        "misconception_tags": ["water_conducts_heat_freely"]
    }


def arch_22_hot_water_circulation_in_domestic_pipes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a solar thermosiphon water heating system, water circulates between the solar collector on the roof and the storage tank above it without using any mechanical electric water pump.\n\n"
        f"What natural process drives the continuous circulation of water in this system?"
    )
    correct_opt = "Thermosiphon convection: water heated in the solar collector expands, becomes less dense, and naturally rises into the storage tank, drawing cooler water down into the collector."
    options = [
        correct_opt,
        "Capillary action: microscopic cotton fibres inside the copper pipes absorb the water.",
        "Magnetic attraction: sunlight magnetises the water molecules so they pull each other upward.",
        "Nuclear repulsion: water atoms disintegrate into ions that propel themselves through the pipes."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermosiphon Solar Circulation:**\n"
        f"1. Water in the collector tubes absorbs solar thermal radiation.\n"
        f"2. As the water warms, it expands and its density decreases.\n"
        f"3. The warmer, lighter water rises into the top of the geyser tank.\n"
        f"4. Denser, cooler water from the bottom of the tank falls under gravity into the bottom of the collector.\n"
        f"5. This passive, pump-free continuous loop is called **thermosiphon convection**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_22_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "22_hot_water_circulation_in_domestic_pipes",
        "question_family_id": "22_hot_water_circulation_in_domestic_pipes",
        "hints": {
            "tier_1": "How does water move when heated without an electric pump?",
            "tier_2": "Hot water rises into the tank while cooler water sinks into the collector.",
            "tier_3": "Thermosiphon convection driven by density differences."
        },
        "misconception_tags": ["pumps_always_required_for_circulation"]
    }


def arch_23_nature_of_thermal_radiation_infrared_waves(rng: random.Random) -> Dict[str, Any]:
    hot_sources = [
        "a glowing red braai fire element",
        "a hot clothing iron held 10 cm away from your palm",
        "a radiant quartz bar heater glowing orange"
    ]
    source = rng.choice(hot_sources)
    prompt = (
        f"When you hold your hand to the side of {source}, you immediately feel heat on your skin, even though the air between is still and cool.\n\n"
        f"What form of energy transfer is responsible, and what is its scientific nature?"
    )
    correct_opt = "Radiation: heat is transferred by infrared electromagnetic waves that travel at the speed of light in straight lines."
    options = [
        correct_opt,
        "Conduction: air molecules form a solid locked chain transferring vibrations.",
        "Convection: hot air blows sideways into your hand at high speed.",
        "Magnetism: iron particles in the blood are attracted to the electrical plug."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermal Radiation Properties:**\n"
        f"- When holding your hand to the side, convection is ruled out because warm air rises upwards, not sideways.\n"
        f"- Air is a poor thermal conductor, ruling out conduction.\n"
        f"- The heat felt is **thermal radiation**, carried by **infrared electromagnetic waves**.\n"
        f"- Infrared waves travel through air or empty space at the speed of light ($3 \\times 10^8\\text{{ m/s}}$) in straight lines.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_23_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "23_nature_of_thermal_radiation_infrared_waves",
        "question_family_id": "23_nature_of_thermal_radiation_infrared_waves",
        "hints": {
            "tier_1": "Warm air rises, so what transfers heat sideways?",
            "tier_2": "Heat felt sideways from a hot object is radiation.",
            "tier_3": "Thermal radiation travels via infrared electromagnetic waves."
        },
        "misconception_tags": ["heat_only_travels_through_matter"]
    }


def arch_24_heat_transfer_through_vacuum_from_the_sun(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The Sun is separated from Earth by approximately $150\\text{{ million kilometres}}$ of outer space, which is an almost complete vacuum with no particles.\n\n"
        f"Why are conduction and convection completely unable to transfer solar thermal energy to Earth, while radiation succeeds?"
    )
    correct_opt = "Conduction and convection both require material particles to transfer energy, whereas radiation consists of electromagnetic waves that can travel freely through a vacuum."
    options = [
        correct_opt,
        "Conduction and convection occur only inside solid rocks, whereas radiation occurs only in water.",
        "Solar heat turns into sound waves that bounce across space dust.",
        "The Sun sends out microscopic hot pebbles that strike the Earth's atmosphere."
    ]
    rng.shuffle(options)
    sol = (
        f"**Medium Requirements for Heat Transfer:**\n"
        f"- **Conduction**: Requires particles touching in a medium (solids).\n"
        f"- **Convection**: Requires fluid particles free to move (liquids, gases).\n"
        f"- **Vacuum of space**: Contains no particles, so neither conduction nor convection can occur.\n"
        f"- **Radiation**: Electromagnetic radiation (infrared, visible, UV) requires NO medium and travels freely through a vacuum.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_24_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "24_heat_transfer_through_vacuum_from_the_sun",
        "question_family_id": "24_heat_transfer_through_vacuum_from_the_sun",
        "hints": {
            "tier_1": "Do conduction and convection need particles?",
            "tier_2": "Conduction and convection need matter; radiation needs no particles.",
            "tier_3": "Radiation is electromagnetic waves that can cross the vacuum of space."
        },
        "misconception_tags": ["vacuum_can_conduct_heat"]
    }


def arch_25_comparing_medium_requirements_conduction_convection_radiation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A Grade 7 student prepares a revision comparison table of the three mechanisms of thermal energy transfer: **Conduction**, **Convection**, and **Radiation**.\n\n"
        f"Which row in the comparison correctly matches each mechanism to its medium requirement and primary state of matter?"
    )
    correct_opt = "Conduction: requires particles in contact (mostly solids) | Convection: requires mobile fluid particles (liquids & gases) | Radiation: requires no medium (can travel through a vacuum)"
    options = [
        correct_opt,
        "Conduction: requires a vacuum | Convection: requires solid metals | Radiation: requires liquids only",
        "Conduction: occurs only in gases | Convection: occurs only in a vacuum | Radiation: requires continuous metal rods",
        "All three methods require identical solid physical contact between objects"
    ]
    rng.shuffle(options)
    sol = (
        f"**Comparative Summary of Heat Transfer Mechanisms:**\n\n"
        f"| Mechanism | Medium Required? | Main State of Matter |\n"
        f"|---|---|---|\n"
        f"| **Conduction** | Yes (particles in direct contact) | Solids (especially metals) |\n"
        f"| **Convection** | Yes (fluids free to flow) | Liquids and gases |\n"
        f"| **Radiation** | No (travels through vacuum) | Any medium or vacuum (electromagnetic) |\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_25_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "25_comparing_medium_requirements_conduction_convection_radiation",
        "question_family_id": "25_comparing_medium_requirements_conduction_convection_radiation",
        "hints": {
            "tier_1": "Which method is the ONLY one that works in a vacuum?",
            "tier_2": "Conduction is in solids; convection is in fluids; radiation needs no medium.",
            "tier_3": "Conduction: solids | Convection: fluids | Radiation: no medium required."
        },
        "misconception_tags": ["confusing_three_transfer_mechanisms"]
    }
