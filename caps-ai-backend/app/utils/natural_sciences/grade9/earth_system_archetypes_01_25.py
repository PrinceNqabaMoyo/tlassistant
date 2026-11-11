"""Grade 9 Natural Sciences - The Earth as a System: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 4/01. The earth as a system.md
Focus:
The four spheres (Biosphere, Hydrosphere, Atmosphere, Lithosphere: definitions, domains, scales),
Earth as a closed matter system & open energy system, Biogeochemical cycles (matter conservation, water cycle,
carbon cycle, nitrogen cycle, phosphorus cycle), Pairwise sphere interactions (Lithosphere-Hydrosphere weathering & caves,
Lithosphere-Atmosphere volcanic gases & aeolian dust, Lithosphere-Biosphere pedogenesis & fossil fuels,
Hydrosphere-Atmosphere evaporation & currents, Hydrosphere-Biosphere aquatic life & transpiration,
Atmosphere-Biosphere photosynthesis, ozone layer UV shield, and greenhouse temperature stability).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_four_spheres_definitions_and_core_domains(rng: random.Random) -> Dict[str, Any]:
    sphere, domain, defn = rng.choice([
        ("Biosphere", "all life on Earth", "plants, animals, fungi, bacteria, and humans from deep ocean trenches to the upper troposphere"),
        ("Hydrosphere", "all water on Earth", "oceans, ice caps, glaciers, groundwater, lakes, rivers, and atmospheric moisture in liquid, solid, or vapor states"),
        ("Atmosphere", "the gaseous blanket around Earth", "nitrogen, oxygen, argon, carbon dioxide, and trace gases held in place by Earth's gravity"),
        ("Lithosphere", "the rigid rocky outer shell", "the crust and uppermost solid mantle forming continents, ocean floors, rocks, and soils")
    ])
    prompt = (
        f"Planet Earth is scientifically modeled as four interacting global subsystems or 'spheres'.\n\n"
        f"Which statement accurately defines the **{sphere}** and its domain?"
    )
    correct = f"It represents {domain}, encompassing {defn}."
    options = [
        correct,
        f"It represents only artificial human-made concrete structures built since the year 1900.",
        f"It represents pure outer space located beyond the orbit of the Moon.",
        f"It represents an imaginary cloud of antimatter surrounding the Sun."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The four Earth spheres:\n"
        "1. Biosphere = all living organisms.\n"
        "2. Hydrosphere = all water.\n"
        "3. Atmosphere = all gases/air.\n"
        "4. Lithosphere = rigid rock and soil.\n"
        f"Step 2: Specific definition:\n"
        f"The {sphere} represents {domain}, encompassing {defn}."
    )
    return {
        "id": f"ns9_eas_01_{rng.randint(100000, 999999)}",
        "subskill": "01_four_spheres_definitions_and_core_domains",
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
            "tier_1": f"What does the root of {sphere} mean?",
            "tier_2": f"It encompasses {domain}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["four_earth_spheres_definitions"]
    }


def arch_02_biosphere_vertical_limits_and_photic_zone(rng: random.Random) -> Dict[str, Any]:
    depth_m = rng.choice(["top 200 meters", "upper 200 m (the sunlit epipelagic photic zone)"])
    prompt = (
        f"Although the biosphere extends from deep rock fractures to high altitudes, the vast majority of life is concentrated in a remarkably thin layer, including the {depth_m} of the oceans.\n\n"
        "Why is marine biological life overwhelmingly concentrated in this shallow ocean layer?"
    )
    correct = "Because sunlight can only penetrate the upper 200 meters, enabling photosynthetic phytoplankton to generate the primary organic food energy that supports marine food webs."
    options = [
        correct,
        "Because water below 200 meters turns into solid boiling granite magma.",
        "Because fish cannot swim if the water pressure is less than 5 000 atmospheres.",
        "Because ocean water below 200 meters contains zero hydrogen or oxygen atoms."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Sunlight penetration:\n"
        "Water absorbs light rapidly. Photons in the blue-green spectrum penetrate deepest, but virtually zero solar light reaches below 200 m (the photic zone).\n"
        "Step 2: Primary productivity:\n"
        "Photosynthesis by diatoms and phytoplankton requires solar photons. Over 90% of marine organisms live in or depend directly on this sunlit upper 200-meter biosphere layer."
    )
    return {
        "id": f"ns9_eas_02_{rng.randint(100000, 999999)}",
        "subskill": "02_biosphere_vertical_limits_and_photic_zone",
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
            "tier_1": "What essential energy source drives photosynthesis in the upper ocean?",
            "tier_2": "Sunlight penetrates only the top 200 meters (the photic zone).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["biosphere_marine_photic_zone_limits"]
    }


def arch_03_hydrosphere_water_distribution_oceans_vs_freshwater(rng: random.Random) -> Dict[str, Any]:
    fresh_pct = rng.choice(["approximately 2,5% to 3%", "less than 3%"])
    prompt = (
        f"Water covers about 70% of Earth's surface, totaling 1,4 billion cubic kilometers. However, {fresh_pct} of this vast hydrosphere is fresh water.\n\n"
        "Where is the vast majority of Earth's scarce freshwater physically stored?"
    )
    correct = "Locked in frozen polar ice caps and continental glaciers (such as in Antarctica and Greenland) and as deep underground aquifers."
    options = [
        correct,
        "Stored in commercial swimming pools across major world cities.",
        "Floating as liquid steam clouds inside volcanic calderas.",
        "Flowing as pure freshwater rivers across the floor of the Pacific Ocean."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Hydrosphere water breakdown:\n"
        "Oceans (saline): ~97,2%.\n"
        "Freshwater: ~2,8%.\n"
        "Step 2: Freshwater breakdown:\n"
        "Of that ~2,8% freshwater, ~68,7% is locked in glaciers and ice sheets, ~30,1% is groundwater, and only ~1,2% is surface water (lakes, rivers, atmosphere)."
    )
    return {
        "id": f"ns9_eas_03_{rng.randint(100000, 999999)}",
        "subskill": "03_hydrosphere_water_distribution_oceans_vs_freshwater",
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
            "tier_1": "Is most freshwater in rivers or locked in polar ice and groundwater?",
            "tier_2": "Over 99% of freshwater is locked in ice caps/glaciers and deep aquifers.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hydrosphere_freshwater_distribution"]
    }


def arch_04_atmosphere_composition_and_gravitational_envelope(rng: random.Random) -> Dict[str, Any]:
    gas, pct, role = rng.choice([
        ("Nitrogen (N2)", "78%", "chemically unreactive diluent that prevents explosive burning and supplies raw nitrogen for biological proteins"),
        ("Oxygen (O2)", "21%", "essential gas for aerobic cellular respiration in organisms and generator of the protective ozone layer"),
        ("Argon (Ar)", "0,93%", "inert noble gas produced by the radioactive decay of potassium-40 in Earth's crust"),
        ("Carbon dioxide (CO2)", "0,04% (approx 420 ppm)", "key trace gas absorbed in photosynthesis and principal natural greenhouse regulator")
    ])
    prompt = (
        "Earth's atmosphere is a mixture of gases held bound to the planet by gravity.\n\n"
        f"What approximate percentage of clean, dry air is composed of **{gas}**, and what is its primary role in the Earth system?"
    )
    correct = f"Approximately {pct}; it is the {role}."
    options = [
        correct,
        f"Approximately 50%; it causes rocks to melt into liquid magma.",
        f"Approximately 5%; it evaporates all ocean water into outer space.",
        f"Approximately 0,0001%; it makes up all clouds in the stratosphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric gas proportions:\n"
        "Nitrogen: 78%, Oxygen: 21%, Argon: ~0,93%, CO2: ~0,04%.\n"
        f"Step 2: Role of {gas}:\n"
        f"{gas} accounts for {pct} and serves as the {role}."
    )
    return {
        "id": f"ns9_eas_04_{rng.randint(100000, 999999)}",
        "subskill": "04_atmosphere_composition_and_gravitational_envelope",
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
            "tier_1": f"Recall the proportion of {gas} in air.",
            "tier_2": f"{gas} makes up {pct} of the atmosphere.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["atmospheric_gas_composition_and_roles"]
    }


def arch_05_lithosphere_crust_and_upper_rigid_mantle(rng: random.Random) -> Dict[str, Any]:
    depth_km = rng.choice(["about 100 km", "roughly 70 to 150 km"])
    prompt = (
        f"The **lithosphere** is the mechanically rigid, brittle outer shell of Planet Earth, extending to a depth of {depth_km}.\n\n"
        "Which geological layers combine to form the lithosphere, and how does it move over the deeper mantle?"
    )
    correct = "The entire solid crust (continental and oceanic) plus the brittle uppermost solid mantle, broken into tectonic plates that float atop the semi-fluid asthenosphere."
    options = [
        correct,
        "Only the loose organic topsoil layer where agricultural plants grow.",
        "The liquid iron outer core that generates Earth's magnetic field.",
        "A solid unbroken sphere of diamond that never moves or cracks."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Definition of the lithosphere:\n"
        "The lithosphere ('rock sphere') includes the continental crust (granitic, ~35 km thick), oceanic crust (basaltic, ~7 km thick), and the uppermost rigid mantle.\n"
        "Step 2: Plate tectonics:\n"
        "It is segmented into major and minor tectonic plates that glide slowly (cm/year) over the ductile, plastic asthenosphere driven by mantle convection."
    )
    return {
        "id": f"ns9_eas_05_{rng.randint(100000, 999999)}",
        "subskill": "05_lithosphere_crust_and_upper_rigid_mantle",
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
            "tier_1": "Does the lithosphere include only the crust or also the upper mantle?",
            "tier_2": "It includes the entire crust plus the uppermost rigid mantle.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lithosphere_crust_and_mantle_distinction"]
    }


def arch_06_earth_closed_system_for_matter_principle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In physical sciences and systems theory, Earth is classified as a **closed system with respect to matter**.\n\n"
        "What is the crucial environmental consequence of Earth being a closed system for matter?"
    )
    correct = "Because essentially no new matter enters or leaves Earth (except negligible meteorites), all resources are finite, and all chemical atoms must be recycled indefinitely through biogeochemical cycles."
    options = [
        correct,
        "New water molecules and oxygen atoms arrive daily from the Sun via the solar wind.",
        "All toxic industrial waste naturally leaves Earth by floating out into interstellar space.",
        "Earth's total mass doubles every single year as new rocks grow from sunlight."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Closed system definition:\n"
        "A closed system exchanges energy with its surroundings, but does not exchange matter.\n"
        "Step 2: Matter conservation:\n"
        "Earth's matter is finite. The water you drink today contains atoms once drunk by dinosaurs. Because waste products cannot leave the planet, pollution accumulates unless neutralized by natural cycles."
    )
    return {
        "id": f"ns9_eas_06_{rng.randint(100000, 999999)}",
        "subskill": "06_earth_closed_system_for_matter_principle",
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
            "tier_1": "Does matter enter or leave Earth in large amounts?",
            "tier_2": "No, Earth is closed to matter, meaning atoms must be continuously recycled.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["closed_matter_system_conservation"]
    }


def arch_07_earth_open_system_for_energy_solar_flux(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In stark contrast to matter, Earth functions as an **open system with respect to energy**.\n\n"
        "How does energy flow through the Earth system from outer space and back?"
    )
    correct = "Earth continuously receives shortwave radiant energy (sunlight) from the Sun, drives internal biological and atmospheric processes, and radiates an equal amount of longwave infrared heat back into space."
    options = [
        correct,
        "Earth absorbs sunlight and traps 100% of it forever inside rocks, causing the planet to glow like a star.",
        "Earth generates all its own energy from internal coal fires, transmitting light to the Sun.",
        "Energy cannot pass through the vacuum of space, so Earth is completely isolated from all cosmic energy."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Open system for energy:\n"
        "Energy enters, undergoes transformations, and exits.\n"
        "Step 2: Planetary energy balance:\n"
        "Incoming solar flux (~1 361 W/m² at top of atmosphere) drives photosynthesis, winds, ocean currents, and the water cycle. To maintain stable temperatures, Earth re-radiates an equal amount of energy as infrared radiation into the cosmic heat sink."
    )
    return {
        "id": f"ns9_eas_07_{rng.randint(100000, 999999)}",
        "subskill": "07_earth_open_system_for_energy_solar_flux",
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
            "tier_1": "Does energy enter and leave Earth?",
            "tier_2": "Yes: solar radiant energy enters, and infrared heat radiation leaves.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["open_energy_system_flux_balance"]
    }


def arch_08_biogeochemical_cycles_conservation_of_atoms(rng: random.Random) -> Dict[str, Any]:
    element = rng.choice(["carbon", "nitrogen", "phosphorus", "water"])
    prompt = (
        f"The continuous movement of {element} through the lithosphere, hydrosphere, atmosphere, and biosphere is called a **biogeochemical cycle**.\n\n"
        "What fundamental scientific law governs all biogeochemical cycles on Earth?"
    )
    correct = "The Law of Conservation of Matter: matter can neither be created nor destroyed, only rearranged into different chemical compounds across the spheres."
    options = [
        correct,
        "The Law of Planetary Inflation: matter expands into empty space whenever temperatures drop.",
        "The Law of Biological Dissolution: living organisms consume atoms until they cease to exist.",
        "The Law of Gravitational Evaporation: heavy elements turn into sunlight over time."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Law of Conservation of Matter:\n"
        "Atoms are neither created nor destroyed in chemical and biological reactions.\n"
        "Step 2: Biogeochemical cycling:\n"
        f"The total quantity of {element} on Earth remains constant. Atoms cycle endlessly through abiotic reservoirs (rocks, oceans, air) and biotic tissues (plants, animals, microbes)."
    )
    return {
        "id": f"ns9_eas_08_{rng.randint(100000, 999999)}",
        "subskill": "08_biogeochemical_cycles_conservation_of_atoms",
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
            "tier_1": "Can atoms be created or destroyed on Earth?",
            "tier_2": "No, matter is conserved and recycled across spheres.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["biogeochemical_cycles_conservation_of_matter"]
    }


def arch_09_water_cycle_cross_sphere_matter_exchange(rng: random.Random) -> Dict[str, Any]:
    step, from_s, to_s, desc = rng.choice([
        ("Evaporation", "Hydrosphere (oceans)", "Atmosphere", "solar thermal energy transforms liquid surface water into invisible water vapor"),
        ("Transpiration", "Biosphere (plant leaves)", "Atmosphere", "water drawn up through plant roots evaporates into air through microscopic leaf stomata"),
        ("Precipitation", "Atmosphere (clouds)", "Lithosphere & Hydrosphere", "condensed cloud droplets fall as rain, snow, or hail onto land and oceans"),
        ("Infiltration / Percolation", "Lithosphere surface", "Hydrosphere (groundwater aquifers)", "rainwater soaks into soil and porous rock strata")
    ])
    prompt = (
        "The hydrological (water) cycle is a primary engine of cross-sphere matter exchange.\n\n"
        f"Which statement accurately describes the water cycle process of **{step}**?"
    )
    correct = f"It moves water from the {from_s} to the {to_s} when {desc}."
    options = [
        correct,
        f"It permanently destroys water molecules by splitting them into nuclear fuel.",
        f"It moves rocks from the center of the Earth directly into the clouds.",
        f"It converts liquid water into solid diamond crystals on mountaintops."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify water cycle phase:\n"
        f"{step} is a key transition step.\n"
        f"Step 2: Sphere transfer:\n"
        f"It moves water from the {from_s} to the {to_s} as {desc}."
    )
    return {
        "id": f"ns9_eas_09_{rng.randint(100000, 999999)}",
        "subskill": "09_water_cycle_cross_sphere_matter_exchange",
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
            "tier_1": f"Where does {step} move water from and to?",
            "tier_2": f"From {from_s} to {to_s}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["water_cycle_sphere_interactions"]
    }


def arch_10_carbon_cycle_transfers_between_all_four_spheres(rng: random.Random) -> Dict[str, Any]:
    transfer, from_sph, to_sph, mechanism = rng.choice([
        ("Photosynthesis", "Atmosphere", "Biosphere", "green plants fix gaseous carbon dioxide into glucose organic molecules"),
        ("Cellular Respiration", "Biosphere", "Atmosphere", "organisms oxidize organic sugars to release energy, exhaling CO2 gas"),
        ("Fossilization", "Biosphere", "Lithosphere", "un-decomposed organic matter buried under sediment transforms over millions of years into coal and oil"),
        ("Combustion", "Lithosphere", "Atmosphere", "burning fossil fuels rapidly oxidizes ancient buried carbon into atmospheric CO2")
    ])
    prompt = (
        "Carbon is the chemical backbone of organic life and cycles continuously through all four Earth spheres.\n\n"
        f"What cross-sphere carbon transfer occurs during **{transfer}**?"
    )
    correct = f"Carbon moves from the {from_sph} to the {to_sph} as {mechanism}."
    options = [
        correct,
        f"Carbon transforms into pure liquid helium in the clouds.",
        f"Carbon leaves Earth completely and enters the Sun's core.",
        f"Carbon is permanently destroyed and replaced by iron atoms."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify process: {transfer}.\n"
        f"Step 2: Sphere pathway:\n"
        f"Carbon moves from the {from_sph} to the {to_sph} when {mechanism}."
    )
    return {
        "id": f"ns9_eas_10_{rng.randint(100000, 999999)}",
        "subskill": "10_carbon_cycle_transfers_between_all_four_spheres",
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
            "tier_1": f"Where does {transfer} take carbon from, and where does it go?",
            "tier_2": f"From {from_sph} to {to_sph}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["carbon_cycle_inter_sphere_transfers"]
    }


def arch_11_nitrogen_cycle_atmospheric_fixation_to_biosphere(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Nitrogen gas (N2) comprises 78% of Earth's atmosphere, yet plants and animals cannot absorb it directly from the air to build proteins.\n\n"
        "How is atmospheric nitrogen converted into a usable form for living organisms in the biosphere?"
    )
    correct = "Nitrogen-fixing bacteria (such as Rhizobium living in legume root nodules and free-living soil bacteria) and lightning fix N2 into usable nitrates (NO3⁻) and ammonium (NH4⁺)."
    options = [
        correct,
        "Earthworms breathe nitrogen gas and exhale solid chunks of pure protein into the soil.",
        "Plant leaves absorb nitrogen gas through transpiration and turn it into diamond crystals.",
        "Sunlight melts nitrogen gas into liquid oil that falls as rain."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The triple bond challenge:\n"
        "N2 has an extremely strong triple covalent bond (N≡N) that eukaryotic cells cannot break.\n"
        "Step 2: Biological and abiotic fixation:\n"
        "1. Biological fixation: Diazotrophic bacteria possessing the nitrogenase enzyme fix N2 into ammonium and nitrates.\n"
        "2. Atmospheric fixation: High-energy lightning breaks N2 bonds, reacting with oxygen to form nitrates washed down by rain."
    )
    return {
        "id": f"ns9_eas_11_{rng.randint(100000, 999999)}",
        "subskill": "11_nitrogen_cycle_atmospheric_fixation_to_biosphere",
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
            "tier_1": "What biological organisms fix nitrogen in soil and root nodules?",
            "tier_2": "Nitrogen-fixing bacteria (and lightning).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["nitrogen_fixation_biological_mechanism"]
    }


def arch_12_phosphorus_cycle_sedimentary_rock_to_living_cells(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Unlike carbon, nitrogen, and water, the **phosphorus cycle** is unique among major biogeochemical cycles.\n\n"
        "What fundamental atmospheric difference distinguishes the phosphorus cycle from other nutrient cycles?"
    )
    correct = "The phosphorus cycle has NO significant gaseous or atmospheric phase; phosphorus is stored primarily in lithospheric rocks and sediments, cycling through soil, water, and organisms."
    options = [
        correct,
        "Phosphorus gas makes up 90% of the stratosphere and is absorbed during breathing.",
        "Phosphorus only exists inside the core of the Sun and never touches Earth rocks.",
        "Phosphorus cannot form chemical bonds with oxygen or hydrogen."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Sedimentary reservoir:\n"
        "The primary reservoir of phosphorus is phosphate rock in the lithosphere.\n"
        "Step 2: Absence of gas phase:\n"
        "Phosphorus compounds do not form stable atmospheric gases under normal Earth conditions. Weathering releases phosphate (PO4³⁻) into soil and water, which plants absorb, animals consume, and decomposers return to sediment."
    )
    return {
        "id": f"ns9_eas_12_{rng.randint(100000, 999999)}",
        "subskill": "12_phosphorus_cycle_sedimentary_rock_to_living_cells",
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
            "tier_1": "Does phosphorus exist as a common gas in the atmosphere?",
            "tier_2": "No, it has no atmospheric phase; it is stored in sedimentary rocks.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["phosphorus_cycle_sedimentary_no_gas"]
    }


def arch_13_lithosphere_hydrosphere_river_weathering_erosion(rng: random.Random) -> Dict[str, Any]:
    landmark = rng.choice(["the Blyde River Canyon in Mpumalanga", "the Fish River Canyon", "the Tugela Gorge in KwaZulu-Natal"])
    prompt = (
        f"Spectacular landscape features such as **{landmark}** demonstrate continuous interaction between the lithosphere and hydrosphere.\n\n"
        "What physical processes occur when flowing river water interacts with lithospheric bedrock?"
    )
    correct = "Hydraulic action, abrasion by sediment, and chemical dissolution weather and carve bedrock (erosion), transporting rock fragments downstream to deposit sedimentary layers."
    options = [
        correct,
        "River water cools rocks until they freeze into solid ice sheets that float away.",
        "Bedrock absorbs all water molecules until rivers completely vanish from continents.",
        "River water turns rocks into radioactive gas that floats into the upper stratosphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mechanical and chemical weathering:\n"
        "Flowing water exerts shear stress (hydraulic action), carries abrasive sand/pebbles that carve rock, and dissolves soluble minerals.\n"
        "Step 2: Erosion and sedimentation:\n"
        "The disintegrated lithospheric rock is transported downstream as suspended sediment and deposited in floodplains and ocean deltas, illustrating the rock cycle."
    )
    return {
        "id": f"ns9_eas_13_{rng.randint(100000, 999999)}",
        "subskill": "13_lithosphere_hydrosphere_river_weathering_erosion",
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
            "tier_1": "How does flowing water shape rock canyons?",
            "tier_2": "Through hydraulic action, abrasion, and erosion.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lithosphere_hydrosphere_erosion_weathering"]
    }


def arch_14_lithosphere_hydrosphere_groundwater_karst_cave_formation(rng: random.Random) -> Dict[str, Any]:
    cave = rng.choice(["the Cango Caves in Oudtshoorn", "the Sterkfontein Caves in the Cradle of Humankind", "the Sudwala Caves in Mpumalanga"])
    prompt = (
        f"South Africa's famous **{cave}** were formed by a profound chemical interaction between groundwater (hydrosphere) and limestone/dolomite rock (lithosphere).\n\n"
        "What chemical reaction dissolves subterranean rock to carve vast underground cavern systems?"
    )
    correct = "Rainwater absorbs atmospheric carbon dioxide to form weak carbonic acid (H2CO3), which seeps underground and chemically dissolves calcium carbonate (CaCO3) in limestone rock."
    options = [
        correct,
        "Underground rivers boil rock using nuclear thermal decay until hollow spaces form.",
        "Earthquakes shake rock until the center becomes hollow and filled with air.",
        "Plant roots eat the rock using digestive enzymes and spit out empty caves."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Carbonic acid formation:\n"
        "CO2(g) + H2O(l) ⇌ H2CO3(aq).\n"
        "Step 2: Limestone dissolution:\n"
        "CaCO3(s) + H2CO3(aq) ⇌ Ca²⁺(aq) + 2HCO3⁻(aq).\n"
        "Over millions of years, acidic groundwater dissolves fractures into vast subterranean chambers, later re-precipitating calcite as stalactites and stalagmites."
    )
    return {
        "id": f"ns9_eas_14_{rng.randint(100000, 999999)}",
        "subskill": "14_lithosphere_hydrosphere_groundwater_karst_cave_formation",
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
            "tier_1": "What acid dissolves limestone underground?",
            "tier_2": "Weak carbonic acid formed from rainwater and carbon dioxide.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["karst_topography_carbonic_acid_dissolution"]
    }


def arch_15_lithosphere_atmosphere_volcanic_gas_injection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During major explosive volcanic eruptions (events originating in the lithosphere), gargantuan volumes of volcanic gases are injected into the atmosphere.\n\n"
        "Which gases are released in the greatest abundance during volcanic outgassing, and how did early volcanism shape Earth's primordial atmosphere?"
    )
    correct = "Water vapor, carbon dioxide, sulfur dioxide, and nitrogen; volcanic outgassing billions of years ago produced Earth's early secondary atmosphere and oceans."
    options = [
        correct,
        "Pure breathable oxygen and ozone gas; early volcanoes produced 100% of modern oxygen.",
        "Radioactive uranium gas and liquid mercury vapor that poisoned all ancient rocks.",
        "Gaseous gold and silver vapors that condensed into modern metal mines."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Volcanic volatile composition:\n"
        "Magma contains dissolved volatiles: ~70–90% H2O, ~10–20% CO2, and ~1–5% SO2/H2S/N2.\n"
        "Step 2: Evolutionary impact:\n"
        "Primordial volcanic outgassing 4 billion years ago created Earth's early atmosphere (steam, CO2, N2). As the planet cooled, steam condensed to form the primordial hydrosphere (oceans)."
    )
    return {
        "id": f"ns9_eas_15_{rng.randint(100000, 999999)}",
        "subskill": "15_lithosphere_atmosphere_volcanic_gas_injection",
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
            "tier_1": "What gases erupt from volcanoes (steam, CO2, sulfur)?",
            "tier_2": "Water vapor, carbon dioxide, sulfur dioxide, and nitrogen.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["volcanic_outgassing_atmospheric_evolution"]
    }


def arch_16_lithosphere_atmosphere_aeolian_wind_erosion_dust_transport(rng: random.Random) -> Dict[str, Any]:
    desert = rng.choice(["the Sahara Desert", "the Kalahari and Namib Deserts"])
    prompt = (
        f"Atmospheric winds sweep across arid regions like {desert}, lifting millions of tonnes of mineral dust into the troposphere.\n\n"
        "How does this lithosphere-atmosphere interaction directly benefit the distant biosphere and hydrosphere?"
    )
    correct = "Airborne dust carries essential mineral nutrients (especially iron and phosphorus) across oceans, fertilizing marine phytoplankton blooms and replenishing nutrient-depleted soils (e.g. in the Amazon basin)."
    options = [
        correct,
        "Desert dust blocks all sunlight permanently, turning the Atlantic Ocean into solid ice.",
        "Desert dust transforms ocean salt water into fresh orange juice for marine mammals.",
        "Desert dust causes the atmosphere to collapse into a vacuum above the desert."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Aeolian transport:\n"
        "Winds scour fine silt and clay from dried lake beds (e.g. the Bodélé Depression).\n"
        "Step 2: Cross-sphere fertilization:\n"
        "Dust plumes travel thousands of kilometers. When dust settles over oceans, bioavailable iron stimulates marine phytoplankton photosynthesis (hydrosphere-biosphere), and phosphorus deposits enrich rainforest vegetation."
    )
    return {
        "id": f"ns9_eas_16_{rng.randint(100000, 999999)}",
        "subskill": "16_lithosphere_atmosphere_aeolian_wind_erosion_dust_transport",
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
            "tier_1": "What nutrients does desert dust carry to oceans and forests?",
            "tier_2": "Iron and phosphorus that fertilize phytoplankton and soil.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["aeolian_dust_nutrient_fertilization"]
    }


def arch_17_lithosphere_biosphere_pedogenesis_soil_formation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Soil is the quintessential interface where all four spheres converge. The process of soil formation is known scientifically as **pedogenesis**.\n\n"
        "How do biological organisms (biosphere) actively interact with weathered mineral rock (lithosphere) to create fertile soil?"
    )
    correct = "Lichens and plant roots secrete organic acids that chemically break down rock, while decaying organic matter (humus) and burrowing earthworms enrich the mineral fragments with nutrients, aerating the soil structure."
    options = [
        correct,
        "Animals drop rocks from tree branches to crush boulders into fine dust.",
        "Soil is produced exclusively by artificial fertilizers manufactured in factories.",
        "Earthworms melt stone into molten magma that cools into fertile topsoil."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Physical and biological weathering:\n"
        "Pioneer organisms like lichens and mosses adhere to bare rock, secreting chelating organic acids that dissolve minerals.\n"
        "Step 2: Humus integration:\n"
        "When organisms die, decomposers (bacteria and fungi) break down tissues into humus, binding with weathered silicates to form nutrient-rich topsoil with pore spaces holding water (hydrosphere) and air (atmosphere)."
    )
    return {
        "id": f"ns9_eas_17_{rng.randint(100000, 999999)}",
        "subskill": "17_lithosphere_biosphere_pedogenesis_soil_formation",
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
            "tier_1": "How do plants and lichens help make soil from rock?",
            "tier_2": "Organic acids break down minerals, and decaying tissues form humus.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["pedogenesis_soil_formation_biological_weathering"]
    }


def arch_18_lithosphere_biosphere_fossil_fuel_formation_coal_oil(rng: random.Random) -> Dict[str, Any]:
    fuel, precursor, env = rng.choice([
        ("Coal", "ancient terrestrial swamp forests (giant ferns and club mosses)", "stagnant anoxic swamp waters that prevented decomposition"),
        ("Crude oil and natural gas", "microscopic marine phytoplankton and zooplankton", "shallow ancient ocean basins where dead plankton sank into anoxic mud")
    ])
    prompt = (
        f"**{fuel}** is an essential lithospheric mineral resource formed through a multi-million-year interaction with the prehistoric biosphere.\n\n"
        f"From what biological organisms did **{fuel}** originate, and under what conditions was it transformed into rock?"
    )
    correct = f"Originated from {precursor}; under {env}, heat and extreme pressure over millions of years compressed the organic carbon into {fuel}."
    options = [
        correct,
        "Originated from volcanic lava that absorbed sunlight during dinosaur times.",
        "Originated from iron meteorites that crashed into polar ice sheets.",
        "Originated from lightning strikes that solidified ocean salt into black rock."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Biological origin of {fuel}:\n"
        f"{fuel} is fossilized solar energy stored in chemical bonds of {precursor}.\n"
        "Step 2: Geological transformation:\n"
        f"Buried rapidly under {env}, lack of oxygen prevented aerobic decay. Intense tectonic pressure and geothermal heat drove off water and volatiles, leaving concentrated carbon deposits in sedimentary rock strata."
    )
    return {
        "id": f"ns9_eas_18_{rng.randint(100000, 999999)}",
        "subskill": "18_lithosphere_biosphere_fossil_fuel_formation_coal_oil",
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
            "tier_1": f"What ancient living things formed {fuel}?",
            "tier_2": f"Formed from {precursor[:35]} under heat and pressure.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["fossil_fuel_formation_biosphere_origin"]
    }


def arch_19_hydrosphere_atmosphere_evaporation_precipitation_dynamics(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The interaction between the hydrosphere and atmosphere drives all global weather and storm systems.\n\n"
        "How does solar radiant energy power the continuous thermodynamic engine between oceans and the atmosphere?"
    )
    correct = "Solar radiation heats the ocean surface, causing evaporation that transfers both water vapor and latent heat into the atmosphere; when water vapor condenses into clouds, latent heat is released, powering storm winds."
    options = [
        correct,
        "The atmosphere pumps cold liquid nitrogen into the oceans to freeze tropical fish.",
        "Ocean waves push the atmosphere upward, creating a permanent vacuum above continents.",
        "Clouds absorb all magnetic energy from Earth's core and convert it into lightning."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Latent heat of vaporization:\n"
        "Evaporation requires immense energy (~2,26 × 10⁶ J/kg). Water vapor carries this energy as latent heat into the atmosphere.\n"
        "Step 2: Condensation and energy release:\n"
        "As air rises and cools, water vapor condenses into cloud droplets, releasing latent heat of condensation. This warming expands the surrounding air, lowering pressure and fueling tropical cyclones and weather systems."
    )
    return {
        "id": f"ns9_eas_19_{rng.randint(100000, 999999)}",
        "subskill": "19_hydrosphere_atmosphere_evaporation_precipitation_dynamics",
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
            "tier_1": "What heat energy does water vapor release when it condenses into clouds?",
            "tier_2": "Latent heat, which powers atmospheric winds and storms.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["latent_heat_hydrosphere_atmosphere_dynamics"]
    }


def arch_20_hydrosphere_atmosphere_ocean_currents_climate_regulation(rng: random.Random) -> Dict[str, Any]:
    current_pair = ("the warm Agulhas Current (east coast of South Africa)", "the cold Benguela Current (west coast)")
    prompt = (
        f"South Africa's coastal climates are dramatically shaped by two contrasting ocean currents: {current_pair[0]} and {current_pair[1]}.\n\n"
        "How do these oceanic hydrosphere currents interact with the atmosphere to create different coastal climates?"
    )
    correct = "The warm Agulhas Current warms the overlying air and increases evaporation, producing humid subtropical weather and high summer rainfall on the east coast, while the cold Benguela Current chills the air, causing atmospheric stability and arid desert conditions on the west coast."
    options = [
        correct,
        "Both currents pump boiling steam into the atmosphere, causing permanent hurricanes across the entire country.",
        "The Benguela current causes daily blizzards of snow across Durban and Cape Town.",
        "Ocean currents have zero effect on atmospheric temperatures or rainfall."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Agulhas Current (Warm):\n"
        "Flows southward from equatorial tropics along the east coast (KZN). High sea surface temperatures evaporate copious moisture, fueling moist onshore breezes and summer rain.\n"
        "Step 2: Benguela Current (Cold):\n"
        "Flows northward from Antarctic sub-polar regions with coastal upwelling along the west coast. Cold water cools the lower atmosphere, creating temperature inversions that inhibit cloud formation and produce the arid Namib and coastal Karoo climates."
    )
    return {
        "id": f"ns9_eas_20_{rng.randint(100000, 999999)}",
        "subskill": "20_hydrosphere_atmosphere_ocean_currents_climate_regulation",
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
            "tier_1": "What climate does the warm Agulhas current create vs the cold Benguela current?",
            "tier_2": "Agulhas brings humid warm rain (east); Benguela brings cold arid conditions (west).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ocean_currents_coastal_climate_impact"]
    }


def arch_21_hydrosphere_biosphere_aquatic_habitats_and_hydration(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Water makes up approximately 70% to 90% of the body mass of living organisms and provides habitat for millions of marine and freshwater species.\n\n"
        "What unique physical property of water allows aquatic organisms to survive beneath frozen lake and river surfaces during winter?"
    )
    correct = "Water expands upon freezing and reaches maximum density at +4 °C, causing ice to float on top as an insulating blanket while liquid water remains at +4 °C below."
    options = [
        correct,
        "Ice sinks directly to the lake bed and heats the water through nuclear decay.",
        "Fish turn into solid rock until the ice melts in the spring.",
        "Water contains high amounts of antifreeze alcohol produced by aquatic plants."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Density anomaly of water:\n"
        "Unlike most substances which become denser as they solidify, water's hydrogen bonds form an open hexagonal crystal lattice in ice, making ice ~9% less dense than liquid water.\n"
        "Step 2: Ecological insulation:\n"
        "Water reaches peak density at 3,98 °C (~4 °C). Ice floats on the surface, insulating the liquid water beneath from freezing temperatures and preserving aquatic ecosystems."
    )
    return {
        "id": f"ns9_eas_21_{rng.randint(100000, 999999)}",
        "subskill": "21_hydrosphere_biosphere_aquatic_habitats_and_hydration",
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
            "tier_1": "Does ice float or sink?",
            "tier_2": "Ice floats because it is less dense, insulating the liquid water below.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["water_density_anomaly_aquatic_survival"]
    }


def arch_22_hydrosphere_biosphere_transpiration_leaf_water_loss(rng: random.Random) -> Dict[str, Any]:
    biome = rng.choice(["the Amazon rainforest", "the Knysna indigenous forest", "a dense pine plantation in Mpumalanga"])
    prompt = (
        f"In dense vegetation zones such as {biome}, plants draw massive volumes of groundwater through their roots and release it into the atmosphere via **transpiration**.\n\n"
        "How does biological transpiration actively influence regional rainfall and atmospheric humidity?"
    )
    correct = "Transpiring vegetation pumps vast quantities of moisture into the lower atmosphere (creating 'flying rivers'), increasing cloud formation and generating localized convective rainfall."
    options = [
        correct,
        "Transpiration sucks all moisture out of the air, causing permanent drought in forests.",
        "Plants release toxic chlorine gas through their leaves that drives away clouds.",
        "Transpiration freezes soil water into permanent ice sheets beneath tree roots."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Transpiration pull:\n"
        "Over 95% of water absorbed by plant roots evaporates through leaf stomata into the air.\n"
        "Step 2: Biotic pump effect:\n"
        "In rainforests, evapotranspiration supplies up to 50% of the moisture for regional rainfall. Deforestation breaks this cycle, dramatically reducing rainfall and causing prolonged droughts."
    )
    return {
        "id": f"ns9_eas_22_{rng.randint(100000, 999999)}",
        "subskill": "22_hydrosphere_biosphere_transpiration_leaf_water_loss",
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
            "tier_1": "What does transpiration add to the atmosphere?",
            "tier_2": "Water vapor, which forms clouds and generates rainfall.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["transpiration_evapotranspiration_rainfall"]
    }


def arch_23_atmosphere_biosphere_photosynthesis_and_respiration(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The global chemical composition of Earth's atmosphere is maintained in dynamic equilibrium through two complementary biological processes: **photosynthesis** and **cellular respiration**.\n\n"
        "How do these two metabolic pathways balance oxygen and carbon dioxide levels in the atmosphere?"
    )
    correct = "Photosynthesis absorbs atmospheric CO2 and releases O2 using solar energy, while cellular respiration consumes O2 to break down food and returns CO2 back into the atmosphere."
    options = [
        correct,
        "Both processes consume 100% of atmospheric oxygen, turning the air into pure nitrogen.",
        "Photosynthesis produces toxic carbon monoxide, while respiration produces liquid nitrogen.",
        "Animals produce oxygen through breathing, while plants only consume oxygen at all times."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Chemical equations:\n"
        "Photosynthesis: 6CO2 + 6H2O + light → C6H12O6 + 6O2.\n"
        "Respiration: C6H12O6 + 6O2 → 6CO2 + 6H2O + ATP (energy).\n"
        "Step 2: Atmospheric homeostasis:\n"
        "Together, autotrophs and heterotrophs maintain Earth's oxygen at ~21% and carbon dioxide at trace levels (~0,04%), preserving planetary habitability."
    )
    return {
        "id": f"ns9_eas_23_{rng.randint(100000, 999999)}",
        "subskill": "23_atmosphere_biosphere_photosynthesis_and_respiration",
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
            "tier_1": "What gas does photosynthesis take in and release? What about respiration?",
            "tier_2": "Photosynthesis takes CO2 and releases O2; respiration takes O2 and releases CO2.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["photosynthesis_respiration_gas_exchange_balance"]
    }


def arch_24_atmosphere_biosphere_stratospheric_ozone_dna_shield(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Located in the stratosphere, the **ozone layer (O3)** is a vital atmospheric component for the survival of the terrestrial biosphere.\n\n"
        "What specific protective function does stratospheric ozone perform that enabled life to colonize land?"
    )
    correct = "It absorbs harmful high-energy solar ultraviolet radiation (UV-B and UV-C), preventing fatal DNA damage, cellular mutations, and lethal tissue burning in terrestrial organisms."
    options = [
        correct,
        "It traps heat so the surface of Earth remains hotter than the surface of Venus.",
        "It reflects incoming meteors by creating an invisible solid magnetic wall.",
        "It generates electrical power that charges the batteries of human electronics."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Photochemical ozone cycle (Chapman cycle):\n"
        "O3 molecules absorb UV-C and UV-B photons and photodissociate into O2 + O, dissipating the radiation harmlessly as heat.\n"
        "Step 2: Terrestrial life colonization:\n"
        "Before the ozone layer formed ~600 million years ago, lethal UV radiation restricted life to oceans. The formation of the ozone shield allowed complex multicellular organisms to emerge and thrive on bare land."
    )
    return {
        "id": f"ns9_eas_24_{rng.randint(100000, 999999)}",
        "subskill": "24_atmosphere_biosphere_stratospheric_ozone_dna_shield",
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
            "tier_1": "What dangerous rays from the Sun does the ozone layer absorb?",
            "tier_2": "Ultraviolet (UV) radiation that damages DNA.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ozone_shield_uv_dna_protection"]
    }


def arch_25_atmosphere_biosphere_greenhouse_effect_temperature_stability(rng: random.Random) -> Dict[str, Any]:
    gases = rng.choice(["water vapor, carbon dioxide, and methane", "natural greenhouse gases (H2O, CO2, CH4)"])
    prompt = (
        f"The atmosphere contains {gases} that produce Earth's natural greenhouse effect.\n\n"
        "How does the natural greenhouse effect maintain temperatures necessary for living organisms in the biosphere?"
    )
    correct = "It absorbs longwave infrared thermal radiation emitted by Earth's warmed surface and re-radiates it in all directions, maintaining an average global temperature of +15 °C rather than a frozen -18 °C."
    options = [
        correct,
        "It creates nuclear explosions in the clouds that heat the ground directly.",
        "It reflects all incoming visible sunlight away into space to keep Earth cool.",
        "It stops all wind from blowing so heat cannot escape across the equator."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Greenhouse gas physics:\n"
        "Greenhouse gases are transparent to shortwave solar radiation, but absorb outgoing longwave infrared radiation emitted by Earth.\n"
        "Step 2: Temperature moderation:\n"
        "Without the natural greenhouse effect, Earth's average surface temperature would plummet to -18 °C, freezing global oceans solid and rendering multicellular life impossible."
    )
    return {
        "id": f"ns9_eas_25_{rng.randint(100000, 999999)}",
        "subskill": "25_atmosphere_biosphere_greenhouse_effect_temperature_stability",
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
            "tier_1": "What would Earth's temperature be without the natural greenhouse effect?",
            "tier_2": "About -18 °C (frozen); natural greenhouse gases keep it at a comfortable +15 °C.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["natural_greenhouse_effect_temperature_regulation"]
    }


BUILDERS_01_25 = {
    "01_four_spheres_definitions_and_core_domains": arch_01_four_spheres_definitions_and_core_domains,
    "02_biosphere_vertical_limits_and_photic_zone": arch_02_biosphere_vertical_limits_and_photic_zone,
    "03_hydrosphere_water_distribution_oceans_vs_freshwater": arch_03_hydrosphere_water_distribution_oceans_vs_freshwater,
    "04_atmosphere_composition_and_gravitational_envelope": arch_04_atmosphere_composition_and_gravitational_envelope,
    "05_lithosphere_crust_and_upper_rigid_mantle": arch_05_lithosphere_crust_and_upper_rigid_mantle,
    "06_earth_closed_system_for_matter_principle": arch_06_earth_closed_system_for_matter_principle,
    "07_earth_open_system_for_energy_solar_flux": arch_07_earth_open_system_for_energy_solar_flux,
    "08_biogeochemical_cycles_conservation_of_atoms": arch_08_biogeochemical_cycles_conservation_of_atoms,
    "09_water_cycle_cross_sphere_matter_exchange": arch_09_water_cycle_cross_sphere_matter_exchange,
    "10_carbon_cycle_transfers_between_all_four_spheres": arch_10_carbon_cycle_transfers_between_all_four_spheres,
    "11_nitrogen_cycle_atmospheric_fixation_to_biosphere": arch_11_nitrogen_cycle_atmospheric_fixation_to_biosphere,
    "12_phosphorus_cycle_sedimentary_rock_to_living_cells": arch_12_phosphorus_cycle_sedimentary_rock_to_living_cells,
    "13_lithosphere_hydrosphere_river_weathering_erosion": arch_13_lithosphere_hydrosphere_river_weathering_erosion,
    "14_lithosphere_hydrosphere_groundwater_karst_cave_formation": arch_14_lithosphere_hydrosphere_groundwater_karst_cave_formation,
    "15_lithosphere_atmosphere_volcanic_gas_injection": arch_15_lithosphere_atmosphere_volcanic_gas_injection,
    "16_lithosphere_atmosphere_aeolian_wind_erosion_dust_transport": arch_16_lithosphere_atmosphere_aeolian_wind_erosion_dust_transport,
    "17_lithosphere_biosphere_pedogenesis_soil_formation": arch_17_lithosphere_biosphere_pedogenesis_soil_formation,
    "18_lithosphere_biosphere_fossil_fuel_formation_coal_oil": arch_18_lithosphere_biosphere_fossil_fuel_formation_coal_oil,
    "19_hydrosphere_atmosphere_evaporation_precipitation_dynamics": arch_19_hydrosphere_atmosphere_evaporation_precipitation_dynamics,
    "20_hydrosphere_atmosphere_ocean_currents_climate_regulation": arch_20_hydrosphere_atmosphere_ocean_currents_climate_regulation,
    "21_hydrosphere_biosphere_aquatic_habitats_and_hydration": arch_21_hydrosphere_biosphere_aquatic_habitats_and_hydration,
    "22_hydrosphere_biosphere_transpiration_leaf_water_loss": arch_22_hydrosphere_biosphere_transpiration_leaf_water_loss,
    "23_atmosphere_biosphere_photosynthesis_and_respiration": arch_23_atmosphere_biosphere_photosynthesis_and_respiration,
    "24_atmosphere_biosphere_stratospheric_ozone_dna_shield": arch_24_atmosphere_biosphere_stratospheric_ozone_dna_shield,
    "25_atmosphere_biosphere_greenhouse_effect_temperature_stability": arch_25_atmosphere_biosphere_greenhouse_effect_temperature_stability,
}
