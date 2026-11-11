"""Grade 9 Natural Sciences: Term 4 - Birth, Life and Death of a Star Archetypes (01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/04. Birth life and the death of a star.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict


def arch_01_stellar_nebulae_composition_hydrogen_helium(rng: random.Random) -> Dict[str, Any]:
    h_pct = rng.choice([73, 74, 75])
    he_pct = rng.choice([23, 24, 25])
    dust_pct = 100 - (h_pct + he_pct)
    prompt = (
        f"Astronomers observe vast interstellar clouds of cold gas and dust known as nebulae, spanning dozens of light years.\n\n"
        f"If a typical stellar nebula has an elemental breakdown of approximately {h_pct}% of its first main constituent, "
        f"{he_pct}% of its second constituent, and {dust_pct}% microscopic cosmic dust, what are these two primary chemical elements?"
    )
    correct = "Hydrogen and Helium"
    options = [
        correct,
        "Oxygen and Carbon Dioxide",
        "Nitrogen and Silicon",
        "Iron and Uranium"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Interstellar gas composition:\n"
        "Nebulae are primordial cosmic clouds formed mostly during the Big Bang.\n"
        "Step 2: Dominant elements:\n"
        f"Approximately {h_pct}% is Hydrogen (H) and {he_pct}% is Helium (He), with trace heavier elements in cosmic dust."
    )
    return {
        "id": f"ns9_star_01_{rng.randint(100000, 999999)}",
        "subskill": "01_stellar_nebulae_composition_hydrogen_helium",
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
            "tier_1": "What are the two lightest, most abundant elements in the universe?",
            "tier_2": "The simplest element with one proton, plus the second simplest noble gas.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["nebula_chemical_composition"]
    }


def arch_02_gravitational_contraction_and_fragmentation(rng: random.Random) -> Dict[str, Any]:
    trigger = rng.choice([
        "a shockwave from a nearby supernova compressing the cloud",
        "passage through a galactic spiral arm with increased gravitational density",
        "a collision between two interstellar molecular clouds"
    ])
    prompt = (
        f"A massive interstellar nebula begins to form new stars after being disturbed by {trigger}.\n\n"
        "What fundamental force drives the contraction of this gas cloud, and what happens to its internal density and temperature as it contracts?"
    )
    correct = "Gravity pulls gas particles toward the center of mass, causing the density to increase and gravitational potential energy to convert into thermal kinetic energy (heating up)."
    options = [
        correct,
        "Centrifugal force pushes particles outward, cooling the core down to absolute zero.",
        "Electrostatic repulsion expands the cloud into a diffuse vacuum.",
        "Magnetic levitation holds the cloud completely frozen and motionless."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Driving physical force:\n"
        "Gravity is the mutual attractive force between all matter in the gas cloud.\n"
        "Step 2: Thermodynamic conversion:\n"
        "As gravity pulls gas atoms closer, gravitational potential energy is converted into kinetic energy, increasing particle collisions and elevating core temperature."
    )
    return {
        "id": f"ns9_star_02_{rng.randint(100000, 999999)}",
        "subskill": "02_gravitational_contraction_and_fragmentation",
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
            "tier_1": "Which universal attractive force pulls masses together in space?",
            "tier_2": "Gravity contracts the cloud, compressing atoms together and raising temperatures.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["gravitational_collapse_energy_conversion"]
    }


def arch_03_protostar_formation_and_accretion_disk(rng: random.Random) -> Dict[str, Any]:
    rotation_speed = rng.choice(["slowly rotating", "drifting and rotating", "gradually spinning"])
    prompt = (
        f"As a {rotation_speed} clump of contracting interstellar gas collapses under its own gravity, conservation of angular momentum causes it to flatten.\n\n"
        "What two distinct cosmic structures emerge at this evolutionary stage?"
    )
    correct = "A central embryonic protostar forming at the dense core, surrounded by a flattened rotating protoplanetary accretion disk from which planets may form."
    options = [
        correct,
        "A black hole at the center surrounded by a ring of frozen ice cubes.",
        "A red giant star with zero surrounding gas or dust.",
        "A planetary nebula with a cooled white dwarf."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Core formation:\n"
        "The dense central sphere of contracting gas forms a protostar.\n"
        "Step 2: Conservation of angular momentum:\n"
        "Spinning material flattens into a circumstellar/protoplanetary disk where dust grains coalesce into planetesimals."
    )
    return {
        "id": f"ns9_star_03_{rng.randint(100000, 999999)}",
        "subskill": "03_protostar_formation_and_accretion_disk",
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
            "tier_1": "What is the baby star called at the center, and what surrounds it?",
            "tier_2": "Protostar in the center, and an accretion disk forming planets.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["protostar_accretion_disk_structure"]
    }


def arch_04_core_temperature_ignition_threshold(rng: random.Random) -> Dict[str, Any]:
    temp_target = rng.choice(["10 million °C (10 000 000 °C)", "10 to 15 million Kelvin", "15 million degrees Celsius"])
    prompt = (
        "A contracting protostar glows due to gravitational friction and compression, but it is not yet officially classified as a true main sequence star.\n\n"
        "What critical core temperature must the protostar reach before sustained thermonuclear fusion of hydrogen begins?"
    )
    correct = temp_target
    wrong_options = [
        "100 degrees Celsius",
        "5 000 degrees Celsius",
        "1 billion Kelvin"
    ]
    options = [correct] + wrong_options
    rng.shuffle(options)
    sol = (
        "Step 1: Coulomb repulsion barrier:\n"
        "Positively charged hydrogen protons naturally repel each other electrically.\n"
        "Step 2: Thermal threshold:\n"
        f"At approximately {temp_target}, proton thermal velocities are high enough to overcome electrostatic repulsion, allowing the strong nuclear force to fuse protons together."
    )
    return {
        "id": f"ns9_star_04_{rng.randint(100000, 999999)}",
        "subskill": "04_core_temperature_ignition_threshold",
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
            "tier_1": "Does nuclear fusion require thousands or millions of degrees?",
            "tier_2": "The core must reach at least 10 to 15 million degrees Celsius.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["thermonuclear_fusion_ignition_temperature"]
    }


def arch_05_thermonuclear_fusion_hydrogen_to_helium(rng: random.Random) -> Dict[str, Any]:
    protons = 4
    prompt = (
        f"Inside the core of our Sun, intense heat and pressure fuse {protons} hydrogen nuclei (protons) into a heavier nucleus.\n\n"
        "What element is produced by this core nuclear fusion reaction, and what explains the tremendous release of energy?"
    )
    correct = "Helium is formed; a small fraction of the mass is converted directly into radiant energy according to Einstein's mass-energy equivalence (E = mc²)."
    options = [
        correct,
        "Uranium is formed by splitting hydrogen atoms apart in nuclear fission.",
        "Water vapor is formed through combustion with atmospheric oxygen.",
        "Lead is formed through radioactive alpha decay."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Fusion reaction product:\n"
        "Four hydrogen nuclei (1H) fuse through the proton-proton chain into one helium nucleus (4He).\n"
        "Step 2: Mass defect and energy:\n"
        "The mass of 4He is approximately 0.7% less than the sum of 4 individual protons. The missing mass (mass defect) is released as energy: E = Δm · c²."
    )
    return {
        "id": f"ns9_star_05_{rng.randint(100000, 999999)}",
        "subskill": "05_thermonuclear_fusion_hydrogen_to_helium",
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
            "tier_1": "What element comes right after hydrogen on the periodic table?",
            "tier_2": "Hydrogen fuses into Helium, converting mass deficit into energy.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["nuclear_fusion_vs_fission_and_products"]
    }


def arch_06_hydrostatic_equilibrium_outward_radiation_inward_gravity(rng: random.Random) -> Dict[str, Any]:
    status = rng.choice(["stable main sequence star", "star during its main lifetime", "stable adult star"])
    prompt = (
        f"For a {status} like the Sun, the star maintains a constant size and spherical shape for billions of years.\n\n"
        "What state of balance describes this stability, and which two opposing forces are equal in magnitude?"
    )
    correct = "Hydrostatic equilibrium: the inward pull of gravitational contraction is precisely balanced by the outward radiation pressure generated by core nuclear fusion."
    options = [
        correct,
        "Thermal convection equilibrium: magnetic attraction matches wind speed.",
        "Chemical equilibrium: evaporation matches condensation of liquid oceans.",
        "Mechanical inertia: friction between planetary orbits stops the star from moving."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Equilibrium condition:\n"
        "Hydrostatic equilibrium is the fundamental stability state of all main sequence stars.\n"
        "Step 2: Balance of forces:\n"
        "Inward force: Gravity trying to collapse the star's immense mass.\n"
        "Outward force: Thermal and radiation pressure produced by thermonuclear fusion in the core."
    )
    return {
        "id": f"ns9_star_06_{rng.randint(100000, 999999)}",
        "subskill": "06_hydrostatic_equilibrium_outward_radiation_inward_gravity",
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
            "tier_1": "What pulls inward and what pushes outward in a star?",
            "tier_2": "Inward gravity equals outward radiation pressure from fusion.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hydrostatic_equilibrium_stellar_stability"]
    }


def arch_07_main_sequence_definition_and_stability(rng: random.Random) -> Dict[str, Any]:
    fraction_lifetime = rng.choice(["roughly 90%", "approximately 85–90%", "nearly 90%"])
    prompt = (
        f"Astronomers classify stars into various evolutionary phases. Stars spend {fraction_lifetime} of their active lives in the **main sequence** phase.\n\n"
        "What core nuclear activity defines a star as being on the main sequence?"
    )
    correct = "Fusing hydrogen into helium within its core under stable hydrostatic equilibrium."
    options = [
        correct,
        "Fusing iron into uranium during a supernova explosion.",
        "Cooling down without producing any nuclear energy.",
        "Ejecting its atmosphere as a planetary nebula."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Main sequence definition:\n"
        "A star is on the main sequence strictly as long as it is fusing hydrogen into helium in its core.\n"
        "Step 2: Longevity:\n"
        "Because hydrogen is the most abundant fuel, this phase represents the vast majority of the star's lifespan."
    )
    return {
        "id": f"ns9_star_07_{rng.randint(100000, 999999)}",
        "subskill": "07_main_sequence_definition_and_stability",
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
            "tier_1": "What primary nuclear fuel powers stars during their longest life stage?",
            "tier_2": "Hydrogen fusing into helium in the core.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["main_sequence_core_fusion_definition"]
    }


def arch_08_star_mass_and_lifespan_inverse_relationship(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "It might seem intuitive that a star with ten times more hydrogen fuel would live ten times longer than a smaller star.\n\n"
        "Why do massive, heavy stars actually have vastly shorter lifespans (millions of years) compared to low-mass stars (billions or trillions of years)?"
    )
    correct = "Massive stars possess intense gravitational pressure at their cores, creating extreme core temperatures that force them to consume their hydrogen fuel at exponentially higher rates."
    options = [
        correct,
        "Massive stars leak all their hydrogen into space through giant black holes.",
        "Massive stars do not have any hydrogen fuel and rely entirely on burning coal.",
        "Smaller stars have more gravity, which slows down time and preserves their fuel."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mass-luminosity relation:\n"
        "Luminosity scales roughly with the cube or fourth power of mass (L ∝ M^3.5).\n"
        "Step 2: Fuel burn rate:\n"
        "A star with 10 times the Sun's mass has 10 times more fuel, but burns it thousands of times faster, living only ~20 million years instead of ~10 billion years."
    )
    return {
        "id": f"ns9_star_08_{rng.randint(100000, 999999)}",
        "subskill": "08_star_mass_and_lifespan_inverse_relationship",
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
            "tier_1": "Does a bigger star burn fuel faster or slower?",
            "tier_2": "Much higher core temperature forces massive stars to consume fuel exponentially faster.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["star_mass_lifespan_inverse_relationship"]
    }


def arch_09_sun_as_main_sequence_yellow_dwarf(rng: random.Random) -> Dict[str, Any]:
    current_age = rng.choice(["4.5 to 4.6 billion years", "approximately 4.6 billion years"])
    total_life = rng.choice(["about 10 billion years", "around 10 to 11 billion years"])
    prompt = (
        f"Our Sun is a medium-sized main sequence star (spectral type G2V). Scientific radiometric dating indicates its current age is {current_age}.\n\n"
        f"What is its expected total main sequence lifetime, and what stage of life is the Sun in today?"
    )
    correct = f"Its total main sequence lifetime is {total_life}; the Sun is currently roughly halfway through its stable main sequence life."
    options = [
        correct,
        "Its total lifetime is 100 million years; the Sun is a dying red supergiant.",
        "Its total lifetime is 1 billion years; the Sun will die next year.",
        "Its total lifetime is infinite; the Sun will never change or exhaust its fuel."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Total lifespan:\n"
        f"A 1 solar-mass star has enough core hydrogen to sustain fusion for {total_life}.\n"
        "Step 2: Current status:\n"
        f"At {current_age}, the Sun is middle-aged (~46% through its main sequence stage), providing stable solar irradiance for life on Earth."
    )
    return {
        "id": f"ns9_star_09_{rng.randint(100000, 999999)}",
        "subskill": "09_sun_as_main_sequence_yellow_dwarf",
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
            "tier_1": "How long does a Sun-like star last, and how old is our Sun?",
            "tier_2": "Total ~10 billion years, and it is roughly halfway through.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sun_lifespan_and_current_age"]
    }


def arch_10_star_color_and_surface_temperature_law(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When viewing the night sky through binoculars or a telescope, stars exhibit noticeably distinct colors ranging from deep red to brilliant blue.\n\n"
        "What physical property of a star determines its visible color, and which color corresponds to the hottest surface temperature?"
    )
    correct = "Surface temperature determines color; blue and white stars are the hottest (10 000 K to over 30 000 K), while red stars are the coolest (around 3 000 K)."
    options = [
        correct,
        "Distance from Earth determines color; red stars are nearest and blue stars are farthest.",
        "Chemical rust determines color; red stars have rusted iron surfaces.",
        "Surface temperature determines color; red stars are the hottest and blue stars are the coldest."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Wien's displacement law / blackbody radiation:\n"
        "Peak emission wavelength is inversely proportional to absolute surface temperature (λ_peak ∝ 1/T).\n"
        "Step 2: Temperature scale:\n"
        "Hotter objects emit higher-energy, shorter-wavelength blue light (10 000–30 000+ K).\n"
        "Cooler objects emit lower-energy, longer-wavelength red light (2 500–3 500 K). Yellow stars like our Sun are intermediate (~5 800 K)."
    )
    return {
        "id": f"ns9_star_10_{rng.randint(100000, 999999)}",
        "subskill": "10_star_color_and_surface_temperature_law",
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
            "tier_1": "Think of a gas flame: is the blue part or the red part hotter?",
            "tier_2": "Blue is hottest (>10 000 K), yellow is medium (~6 000 K), red is coolest (~3 000 K).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["star_color_temperature_inversion_misconception"]
    }


def arch_11_rigel_vs_betelgeuse_color_comparison(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the prominent constellation of Orion, two brilliant supergiant stars stand out: **Rigel** (at Orion's foot/shoulder depending on hemisphere) and **Betelgeuse** (at Orion's armpit/shoulder).\n\n"
        "How do Rigel and Betelgeuse compare in terms of visible color and surface temperature?"
    )
    correct = "Rigel is a blue-white supergiant with a searing surface temperature exceeding 11 000 K, whereas Betelgeuse is a red supergiant with a much cooler surface temperature of about 3 500 K."
    options = [
        correct,
        "Both Rigel and Betelgeuse are yellow stars identical in temperature to our Sun.",
        "Betelgeuse is a blue star with a temperature of 50 000 K, while Rigel is a red dwarf at 1 000 K.",
        "Rigel is red because it is made of copper, while Betelgeuse is blue because it is made of liquid water."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Rigel:\n"
        "Rigel (Beta Orionis) is a blue-white B-type supergiant; surface temperature ~12 000 K.\n"
        "Step 2: Betelgeuse:\n"
        "Betelgeuse (Alpha Orionis) is an evolved M-type red supergiant; surface temperature ~3 500 K (cool surface, but vast radiating surface area gives immense luminosity)."
    )
    return {
        "id": f"ns9_star_11_{rng.randint(100000, 999999)}",
        "subskill": "11_rigel_vs_betelgeuse_color_comparison",
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
            "tier_1": "Recall which Orion star is blue and which is red.",
            "tier_2": "Rigel = blue (hot >11 000 K); Betelgeuse = red (cool ~3 500 K).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["orion_stars_rigel_betelgeuse_temperature"]
    }


def arch_12_light_year_definition_and_astronomical_distance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In popular culture, people sometimes misuse the term 'light year' as a measurement of time.\n\n"
        "What is the exact scientific definition of a **light year**, and what type of physical quantity does it measure?"
    )
    correct = "A light year is a unit of astronomical distance; it is the total distance that light travels through a vacuum in one Julian year (approx. 9.46 trillion km or 9.46 × 10¹² km)."
    options = [
        correct,
        "A light year is a unit of time representing 365 leap years on Mercury.",
        "A light year is the speed of light divided by the mass of the Earth.",
        "A light year is the brightness of a star measured in lumens per square meter."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Scientific definition:\n"
        "Distance = Speed × Time.\n"
        "Speed of light c ≈ 300 000 km/s (299 792 458 m/s).\n"
        "1 year = 365.25 days × 24 h × 3 600 s = 31 557 600 seconds.\n"
        "Step 2: Calculation:\n"
        "Distance = 299 792.458 km/s × 31 557 600 s ≈ 9.46 × 10¹² km (approx 9.5 trillion kilometers)."
    )
    return {
        "id": f"ns9_star_12_{rng.randint(100000, 999999)}",
        "subskill": "12_light_year_definition_and_astronomical_distance",
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
            "tier_1": "Is a light year a measure of time or a measure of distance?",
            "tier_2": "It is a distance: the distance light travels in one year (~9.5 trillion km).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["light_year_time_vs_distance_confusion"]
    }


def arch_13_light_speed_and_lookback_time_concept(rng: random.Random) -> Dict[str, Any]:
    dist_ly = rng.choice([500, 640, 1000, 1500])
    prompt = (
        f"A telescope in Sutherland observes a distant star located {dist_ly} light years away from Earth.\n\n"
        "When astronomers gaze at this star tonight, which statement accurately describes what they are seeing?"
    )
    correct = f"They are observing the star as it existed {dist_ly} years ago in the past, because its light took {dist_ly} years to traverse interstellar space to reach Earth."
    options = [
        correct,
        f"They are seeing the star in real-time as it looks at this exact second today.",
        f"They are predicting how the star will look {dist_ly} years into the future.",
        "They are observing a virtual simulation generated by the telescope lens."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Finite speed of light:\n"
        "Light travels at c ≈ 300 000 km/s. It is not instantaneous.\n"
        "Step 2: Lookback time:\n"
        f"Light emitted from an object {dist_ly} light years away takes exactly {dist_ly} years to travel across space. Looking out into deep space is literally looking back into cosmic history."
    )
    return {
        "id": f"ns9_star_13_{rng.randint(100000, 999999)}",
        "subskill": "13_light_speed_and_lookback_time_concept",
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
            "tier_1": "Does light travel instantaneously across space?",
            "tier_2": "Because light takes time to travel, seeing a star 500 ly away means seeing it 500 years ago.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lookback_time_finite_speed_of_light"]
    }


def arch_14_proxima_centauri_distance_calculation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The closest known star system to our Solar System is Alpha Centauri, whose closest member is the red dwarf **Proxima Centauri**, situated approximately 4.24 light years away.\n\n"
        "If an astronaut on Earth sends a laser communications signal traveling at the speed of light toward Proxima Centauri, how long will it take for the signal to reach the star?"
    )
    correct = "4.24 years"
    options = [
        correct,
        "4.24 minutes",
        "4.24 seconds",
        "42.4 days"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Definition of light travel time:\n"
        "By definition, light travels a distance of 1 light year in exactly 1 Earth year.\n"
        "Step 2: Calculation:\n"
        "Time = Distance / Speed = 4.24 light years / (1 light year per year) = 4.24 years."
    )
    return {
        "id": f"ns9_star_14_{rng.randint(100000, 999999)}",
        "subskill": "14_proxima_centauri_distance_calculation",
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
            "tier_1": "How long does light take to travel 1 light year?",
            "tier_2": "1 light year takes 1 year; therefore 4.24 light years takes 4.24 years.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["astronomical_distance_time_conversion"]
    }


def arch_15_stellar_winds_and_protoplanetary_disk_clearing(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Once nuclear fusion ignites in the core of a newly born star, the star begins blowing a powerful outward stream of charged particles known as a **stellar wind**.\n\n"
        "What critical effect does this stellar wind have on the surrounding protoplanetary disk?"
    )
    correct = "It sweeps and blows away the remaining unaccreted gas and light dust particles out of the stellar system, halting further planetary growth and leaving the newly formed planets orbiting the clear star."
    options = [
        correct,
        "It pulls all planets directly into the star's core to be incinerated.",
        "It turns all gas into solid iron armor plating around the star.",
        "It causes the star to instantly cool down and freeze into solid ice."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Stellar wind nature:\n"
        "A continuous outflow of plasma (electrons, protons) accelerated by the star's radiation and magnetic fields.\n"
        "Step 2: Clearing action:\n"
        "The wind applies radiation pressure on gas and dust grains, clearing the circumstellar envelope over ~3–10 million years."
    )
    return {
        "id": f"ns9_star_15_{rng.randint(100000, 999999)}",
        "subskill": "15_stellar_winds_and_protoplanetary_disk_clearing",
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
            "tier_1": "What does a strong wind do to loose dust and gas?",
            "tier_2": "It blows the residual light gas and dust away from the new planets.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["stellar_wind_protoplanetary_clearing"]
    }


def arch_16_orion_nebula_southern_sky_observation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When viewed by stargazers located in South Africa (Southern Hemisphere), the constellation of Orion appears inverted or 'upside down' compared to northern sky maps.\n\n"
        "Where is the famous **Orion Nebula** (M42) situated within this constellation when viewed from the Southern Hemisphere?"
    )
    correct = "Within Orion's 'sword' (which appears above the three belt stars in the Southern Hemisphere), visible as a fuzzy, faint jewel-like patch to the naked eye."
    options = [
        correct,
        "Directly inside the center of our Moon's craters.",
        "At the exact position of the South Celestial Pole.",
        "In the belt itself, replacing the central star Alnilam."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Southern perspective:\n"
        "In the Southern Hemisphere, Orion is inverted: the sword hangs 'above' the belt.\n"
        "Step 2: Orion Nebula location:\n"
        "The middle 'star' of Orion's sword is actually the Orion Nebula (M42), a famous nearby stellar nursery roughly 1 344 light years away."
    )
    return {
        "id": f"ns9_star_16_{rng.randint(100000, 999999)}",
        "subskill": "16_orion_nebula_southern_sky_observation",
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
            "tier_1": "Is the nebula in Orion's belt, sword, or shield?",
            "tier_2": "In Orion's sword, which lies above the belt when viewed from South Africa.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["southern_hemisphere_constellation_orientation"]
    }


def arch_17_pillars_of_creation_stellar_nursery(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "One of the most celebrated astronomical images captured by the Hubble and James Webb Space Telescopes depicts the **Pillars of Creation** in the Eagle Nebula (M16).\n\n"
        "What are the towering 'pillars' composed of, and what important astronomical process is occurring inside them?"
    )
    correct = "Dense columns of interstellar hydrogen gas and cosmic dust that act as active stellar nurseries where new protostars are condensing and being born."
    options = [
        correct,
        "Columns of frozen nitrogen ice left behind by ancient comets.",
        "Solid stone pillars carved by ancient extraterrestrial civilizations.",
        "Streams of exhaust smoke from launching space shuttles."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Composition:\n"
        "The pillars are composed of cold interstellar molecular hydrogen gas mixed with microscopic dust grains.\n"
        "Step 2: Astronomical significance:\n"
        "The gas is actively condensing under gravity into compact globules forming brand new protostars."
    )
    return {
        "id": f"ns9_star_17_{rng.randint(100000, 999999)}",
        "subskill": "17_pillars_of_creation_stellar_nursery",
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
            "tier_1": "What are nebulae made of and what gets born there?",
            "tier_2": "Hydrogen gas and dust columns where new stars are born.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["stellar_nursery_pillars_of_creation"]
    }


def arch_18_corona_australis_star_forming_region(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In Southern Hemisphere astronomy, the **Corona Australis** (Southern Crown) molecular cloud complex is an important astronomical target.\n\n"
        "Why is Corona Australis of particular interest to astrophysicists studying stellar evolution?"
    )
    correct = "It is one of the closest active star-forming regions to Earth (approx. 430 light years away), enabling high-resolution telescope observations of young protostars and protoplanetary disks."
    options = [
        correct,
        "It contains the only black hole located inside our solar system.",
        "It is a region where stars are made entirely of liquid mercury.",
        "It is the exact location where our Sun was born 100 years ago."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Proximity:\n"
        "Located ~420–430 light years away in the southern constellation Corona Australis.\n"
        "Step 2: Astrophysical value:\n"
        "Its close distance allows astronomers using telescopes to observe young stellar objects (Coronet cluster) breaking through their birth clouds."
    )
    return {
        "id": f"ns9_star_18_{rng.randint(100000, 999999)}",
        "subskill": "18_corona_australis_star_forming_region",
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
            "tier_1": "Why is a nearby star nursery useful to astronomers with telescopes?",
            "tier_2": "Because it is close to Earth, allowing detailed study of young protostars.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["corona_australis_stellar_nursery"]
    }


def arch_19_low_mass_star_hydrogen_exhaustion_core_contraction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "After billions of years of stable life on the main sequence, a medium-mass star like our Sun eventually runs out of hydrogen fuel in its core.\n\n"
        "When core hydrogen fusion ceases, what immediate physical change occurs in the star's core?"
    )
    correct = "Without outward radiation pressure from fusion, the helium core contracts rapidly under gravity and heats up dramatically."
    options = [
        correct,
        "The core instantly freezes into a block of dry ice and stops spinning.",
        "The core turns into a supermassive black hole within three seconds.",
        "The core expands outward until it disappears completely."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Loss of hydrostatic balance:\n"
        "Core hydrogen is exhausted; fusion stops; outward radiation pressure drops.\n"
        "Step 2: Core collapse:\n"
        "Gravity dominates, pulling the helium core inward. As the core contracts, gravitational energy raises its temperature until helium fusion can ignite."
    )
    return {
        "id": f"ns9_star_19_{rng.randint(100000, 999999)}",
        "subskill": "19_low_mass_star_hydrogen_exhaustion_core_contraction",
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
            "tier_1": "If outward pressure stops, what does inward gravity do to the core?",
            "tier_2": "Gravity causes the core to contract and heat up.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["core_hydrogen_exhaustion_contraction"]
    }


def arch_20_red_giant_expansion_and_cooling(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "While the contracting core of an aging medium star heats up, the energy ignites hydrogen fusion in a surrounding shell, pushing the outer envelope outward.\n\n"
        "What happens to the star's outer layers during this **Red Giant** phase?"
    )
    correct = "The outer envelope expands to hundreds of times its original radius and cools down to roughly 3 000 K, shifting its color to red."
    options = [
        correct,
        "The outer layers contract into an invisible pinprick and turn ultra-violet.",
        "The outer layers solidify into a hard rock crust like the Earth.",
        "The outer layers freeze into diamond crystals while maintaining the same size."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Shell fusion and expansion:\n"
        "Intense heat from shell fusion pushes the outer atmosphere outward to enormous dimensions (e.g. the Sun will expand past Mercury, Venus, and possibly Earth).\n"
        "Step 2: Surface cooling:\n"
        "As energy is distributed over a vastly larger surface area, surface temperature drops from ~5 800 K to ~3 000 K, shifting emitted light from yellow to red."
    )
    return {
        "id": f"ns9_star_20_{rng.randint(100000, 999999)}",
        "subskill": "20_red_giant_expansion_and_cooling",
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
            "tier_1": "Why is it called a 'Giant' and why is it 'Red'?",
            "tier_2": "Giant because it expands hugely; Red because its surface cools down.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["red_giant_expansion_and_cooling"]
    }


def arch_21_helium_fusion_triple_alpha_process(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When the contracting core of a red giant reaches an astonishing temperature of approximately 100 million Kelvin (100 000 000 K), a new nuclear stage ignites.\n\n"
        "What nuclear reaction occurs in the core at this extreme temperature, and what element is synthesized?"
    )
    correct = "Helium nuclei fuse together (triple-alpha process) to synthesize Carbon (and Oxygen)."
    options = [
        correct,
        "Carbon nuclei split into hydrogen atoms through nuclear fission.",
        "Uranium atoms fuse into gold particles.",
        "Hydrogen and oxygen combine through chemical combustion to form water."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Ignition temperature:\n"
        "Helium nuclei (alpha particles, 2 protons + 2 neutrons) require ~100 million K to overcome greater electrostatic repulsion (charge +2).\n"
        "Step 2: Triple-alpha process:\n"
        "Three 4He nuclei fuse sequentially: 4He + 4He ⇌ 8Be; 8Be + 4He → 12C + γ (Carbon-12), with subsequent capture forming 16O (Oxygen-16)."
    )
    return {
        "id": f"ns9_star_21_{rng.randint(100000, 999999)}",
        "subskill": "21_helium_fusion_triple_alpha_process",
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
            "tier_1": "What do helium atoms fuse into inside a red giant core?",
            "tier_2": "Three helium nuclei fuse into a Carbon nucleus.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["helium_fusion_carbon_synthesis"]
    }


def arch_22_planetary_nebula_outer_envelope_ejection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Despite its misleading historical name given by early astronomers who thought it looked like Uranus or Neptune through small telescopes, a **planetary nebula** has nothing to do with planets.\n\n"
        "What is a planetary nebula in reality?"
    )
    correct = "An expanding, glowing shell of ionized gas and dust gently puffed off and ejected into interstellar space by a dying low-to-medium mass red giant star."
    options = [
        correct,
        "A dense cloud of rocky asteroids colliding to form a new rocky planet.",
        "A giant planet whose atmosphere has frozen into solid liquid methane.",
        "The violent explosion of a high-mass star destroying an entire galaxy."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Historical naming misconception:\n"
        "William Herschel termed them 'planetary nebulae' in the 1780s because their round greenish disks resembled Uranus in primitive telescopes.\n"
        "Step 2: Physical reality:\n"
        "Pulsations and radiation pressure in an asymptotic giant star gently blow off its outer layers (~60% of its mass) into space, forming a glowing ionized gas ring."
    )
    return {
        "id": f"ns9_star_22_{rng.randint(100000, 999999)}",
        "subskill": "22_planetary_nebula_outer_envelope_ejection",
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
            "tier_1": "Does a planetary nebula involve planets, or dying star gases?",
            "tier_2": "It is an ejected glowing envelope of gas from a dying red giant.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["planetary_nebula_misleading_name"]
    }


def arch_23_white_dwarf_dense_carbon_oxygen_core(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "After the outer layers of a dying medium-mass star are ejected as a planetary nebula, what dense remnant remains exposed at the center?\n\n"
        "What is this remnant called, and does it produce new energy via nuclear fusion?"
    )
    correct = "A **white dwarf**; it has ceased all nuclear fusion and glows solely from residual, leftover thermal heat accumulated over billions of years."
    options = [
        correct,
        "A protostar; it fuses hydrogen into helium at a rapid rate.",
        "A red supergiant; it continues explosive silicon fusion indefinitely.",
        "A black hole; it immediately devours all surrounding stars."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Remnant identity:\n"
        "The exposed inert core of carbon and oxygen is known as a white dwarf.\n"
        "Step 2: Thermal state:\n"
        "Core mass cannot reach the ~600 million K required to ignite carbon fusion. Nuclear fusion is permanently shut down; the white dwarf slowly radiates its stored heat into space."
    )
    return {
        "id": f"ns9_star_23_{rng.randint(100000, 999999)}",
        "subskill": "23_white_dwarf_dense_carbon_oxygen_core",
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
            "tier_1": "What is the small hot white core left behind after a red giant sheds its gas?",
            "tier_2": "A white dwarf, which has no fusion and only radiates leftover heat.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["white_dwarf_residual_cooling"]
    }


def arch_24_white_dwarf_density_and_size_comparison(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A white dwarf star exhibits extreme physical properties that defy everyday earthly experience.\n\n"
        "How do the physical size and density of a typical white dwarf compare to familiar astronomical bodies?"
    )
    correct = "It has a volume roughly the size of planet Earth, but packs the mass of the entire Sun; a single teaspoon of white dwarf material would weigh several tonnes on Earth."
    options = [
        correct,
        "It is the size of Jupiter and weighs less than a feather.",
        "It is the size of the Milky Way galaxy but contains only two atoms.",
        "It is hollow inside like a tennis ball with zero density."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Size comparison:\n"
        "A white dwarf radius is comparable to Earth's (~6 000–7 000 km).\n"
        "Step 2: Density comparison:\n"
        "It packs ~0.6 to 1.0 solar masses into this Earth-sized volume. Density is ~10⁶ g/cm³ (one million times the density of water), supported by electron degeneracy pressure."
    )
    return {
        "id": f"ns9_star_24_{rng.randint(100000, 999999)}",
        "subskill": "24_white_dwarf_density_and_size_comparison",
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
            "tier_1": "How big is a white dwarf (Earth-sized or Sun-sized) and how heavy is it?",
            "tier_2": "Earth-sized in volume, Sun-sized in mass; extraordinarily dense.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["white_dwarf_extreme_density"]
    }


def arch_25_black_dwarf_ultimate_cooling_endpoint(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Because a white dwarf has no internal nuclear energy source, it must continuously radiate its stored thermal heat into the cold vacuum of space.\n\n"
        "What theoretical cold, dark corpse will a white dwarf eventually become after hundreds of billions of years of cooling?"
    )
    correct = "A **black dwarf**; however, none currently exist in our universe because the universe (13.8 billion years old) is far too young for any white dwarf to have cooled completely."
    options = [
        correct,
        "A red supergiant that reignites into a new sun.",
        "A bright pulsar emitting visible green radio pulses.",
        "A quasar shining brighter than a trillion stars."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Cooling trajectory:\n"
        "White dwarfs radiate heat via electromagnetic radiation. Cooling to near absolute zero takes ~10¹⁴ to 10¹⁵ years.\n"
        "Step 2: Cosmic age reality:\n"
        "Because the universe is only ~13.8 billion years old, all white dwarfs ever created are still warm; black dwarfs remain purely theoretical endpoints."
    )
    return {
        "id": f"ns9_star_25_{rng.randint(100000, 999999)}",
        "subskill": "25_black_dwarf_ultimate_cooling_endpoint",
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
            "tier_1": "What happens when a white object stops glowing and turns cold and dark?",
            "tier_2": "It becomes a black dwarf (though none exist yet because the universe is too young).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["black_dwarf_theoretical_endpoint"]
    }


BUILDERS_01_25 = {
    "01_stellar_nebulae_composition_hydrogen_helium": arch_01_stellar_nebulae_composition_hydrogen_helium,
    "02_gravitational_contraction_and_fragmentation": arch_02_gravitational_contraction_and_fragmentation,
    "03_protostar_formation_and_accretion_disk": arch_03_protostar_formation_and_accretion_disk,
    "04_core_temperature_ignition_threshold": arch_04_core_temperature_ignition_threshold,
    "05_thermonuclear_fusion_hydrogen_to_helium": arch_05_thermonuclear_fusion_hydrogen_to_helium,
    "06_hydrostatic_equilibrium_outward_radiation_inward_gravity": arch_06_hydrostatic_equilibrium_outward_radiation_inward_gravity,
    "07_main_sequence_definition_and_stability": arch_07_main_sequence_definition_and_stability,
    "08_star_mass_and_lifespan_inverse_relationship": arch_08_star_mass_and_lifespan_inverse_relationship,
    "09_sun_as_main_sequence_yellow_dwarf": arch_09_sun_as_main_sequence_yellow_dwarf,
    "10_star_color_and_surface_temperature_law": arch_10_star_color_and_surface_temperature_law,
    "11_rigel_vs_betelgeuse_color_comparison": arch_11_rigel_vs_betelgeuse_color_comparison,
    "12_light_year_definition_and_astronomical_distance": arch_12_light_year_definition_and_astronomical_distance,
    "13_light_speed_and_lookback_time_concept": arch_13_light_speed_and_lookback_time_concept,
    "14_proxima_centauri_distance_calculation": arch_14_proxima_centauri_distance_calculation,
    "15_stellar_winds_and_protoplanetary_disk_clearing": arch_15_stellar_winds_and_protoplanetary_disk_clearing,
    "16_orion_nebula_southern_sky_observation": arch_16_orion_nebula_southern_sky_observation,
    "17_pillars_of_creation_stellar_nursery": arch_17_pillars_of_creation_stellar_nursery,
    "18_corona_australis_star_forming_region": arch_18_corona_australis_star_forming_region,
    "19_low_mass_star_hydrogen_exhaustion_core_contraction": arch_19_low_mass_star_hydrogen_exhaustion_core_contraction,
    "20_red_giant_expansion_and_cooling": arch_20_red_giant_expansion_and_cooling,
    "21_helium_fusion_triple_alpha_process": arch_21_helium_fusion_triple_alpha_process,
    "22_planetary_nebula_outer_envelope_ejection": arch_22_planetary_nebula_outer_envelope_ejection,
    "23_white_dwarf_dense_carbon_oxygen_core": arch_23_white_dwarf_dense_carbon_oxygen_core,
    "24_white_dwarf_density_and_size_comparison": arch_24_white_dwarf_density_and_size_comparison,
    "25_black_dwarf_ultimate_cooling_endpoint": arch_25_black_dwarf_ultimate_cooling_endpoint,
}
