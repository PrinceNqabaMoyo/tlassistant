"""Grade 8 Natural Sciences - Beyond the Solar System: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr8/Term 4/01. Beyond the solar system.md
Focus:
Milky Way Galaxy (definition, band in night sky, Greek/Roman naming, morphology, dimensions, star count,
spiral arms vs central bulge vs dust lanes, Sun's position in Orion arm, orbital velocity and cosmic year, Sagittarius A*),
Units of measurement (speed of light, light seconds, light minutes, light hours, light years, lookback time),
Stellar neighbourhood (Proxima Centauri, Alpha Centauri system, Southern Cross pointers, interstellar travel times,
stellar parallax, luminosity vs apparent brightness).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_galaxy_definition_gravitationally_bound_system(rng: random.Random) -> Dict[str, Any]:
    comp = rng.choice([
        "billions of stars, planetary systems, gas clouds, and dust",
        "hundreds of billions of stars, interstellar gas, and cosmic dust"
    ])
    prompt = (
        f"In astronomy, a **galaxy** is a massive cosmic structure containing {comp}.\n\n"
        "What fundamental force binds all these constituents together into a single cohesive system?"
    )
    correct = "The mutual gravitational attraction acting among all the mass in the galaxy."
    options = [
        correct,
        "Electrostatic repulsion between oppositely charged planetary atmospheres.",
        "Magnetic fields anchored to the surface of individual rocky asteroids.",
        "Nuclear strong forces operating continuously across billions of kilometers of vacuum."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Definition of a galaxy:\n"
        "A galaxy is a massive collection of stars, stellar remnants, interstellar gas, dust, and dark matter.\n"
        "Step 2: Cohesive force:\n"
        "Gravity is the long-range attractive force that holds all stellar and interstellar material together in orbit around a common center of mass."
    )
    return {
        "id": f"ns8_bss_01_{rng.randint(100000, 999999)}",
        "subskill": "01_galaxy_definition_gravitationally_bound_system",
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
            "tier_1": "What fundamental cosmic force pulls massive objects toward one another?",
            "tier_2": "Gravity binds stars and gas clouds into galaxies.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["galaxy_definition_gravitational_binding"]
    }


def arch_02_milky_way_band_appearance_internal_perspective(rng: random.Random) -> Dict[str, Any]:
    loc = rng.choice(["a dark-sky area in the Karoo", "the Sutherland observatory ridge", "a rural reserve in Limpopo"])
    prompt = (
        f"On a clear, moonless night in {loc}, observers can see a luminous, hazy band of diffuse light stretching across the sky, split by dark dusty rifts.\n\n"
        "Why does our galaxy appear as a narrow band across our night sky rather than a circular disc surrounding us uniformly?"
    )
    correct = "Because our Solar System is located inside the flattened galactic disc, causing us to view the millions of distant stars edge-on through the plane of the disc."
    options = [
        correct,
        "Because the Milky Way is shaped like an ultra-thin straight electrical wire stretching from Earth to the Moon.",
        "Because our atmosphere reflects light from city street lamps into a narrow illuminated streak.",
        "Because the Sun is located completely outside all galaxies, looking into a distant cosmic tube."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Galactic geometry:\n"
        "The Milky Way is a flattened disc with a central bulge.\n"
        "Step 2: Internal observer perspective:\n"
        "Because Earth orbits a star inside this disc, looking through the plane of the disc aligns millions of distant stars along our line of sight, appearing as a dense, milky band across the sky."
    )
    return {
        "id": f"ns8_bss_02_{rng.randint(100000, 999999)}",
        "subskill": "02_milky_way_band_appearance_internal_perspective",
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
            "tier_1": "Where is our Solar System situated relative to the galaxy's disk?",
            "tier_2": "We are inside the disk, viewing it edge-on.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["milky_way_sky_band_edge_on_perspective"]
    }


def arch_03_milky_way_historical_naming_greek_roman(rng: random.Random) -> Dict[str, Any]:
    culture, term, meaning = rng.choice([
        ("Ancient Greek", "Galaxies Kuklos", "Milky Circle"),
        ("Ancient Roman (Latin)", "Via Lactea", "Milky Road or Milky Way")
    ])
    prompt = (
        f"Historical civilizations coined poetic names for the luminous celestial band visible in the night sky. In {culture} mythology and astronomy, it was named **{term}**.\n\n"
        f"What is the literal translation of **{term}**, and what visual impression inspired it?"
    )
    correct = f"It translates literally to '{meaning}', inspired by the appearance of spilled milk or a luminous milky trail across the heavens."
    options = [
        correct,
        f"It translates literally to 'Burning Fire', inspired by active volcanic eruptions on the Moon.",
        f"It translates literally to 'Golden Bridge', inspired by ancient metal suspension bridges.",
        f"It translates literally to 'Frozen Ocean', inspired by polar icebergs in Antarctica."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Historical linguistic origin:\n"
        f"The {culture} phrase '{term}' translates to '{meaning}'.\n"
        "Step 2: Mythological explanation:\n"
        "Ancient peoples observed the faint, white glow of unresolved stars and likened it to milk spilled across the dome of the heavens."
    )
    return {
        "id": f"ns8_bss_03_{rng.randint(100000, 999999)}",
        "subskill": "03_milky_way_historical_naming_greek_roman",
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
            "tier_1": f"What does '{term}' literally mean?",
            "tier_2": f"It translates to '{meaning}'.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["milky_way_etymology_historical_naming"]
    }


def arch_04_milky_way_morphology_disk_bulge_and_halo(rng: random.Random) -> Dict[str, Any]:
    analogies = [
        ("two fried eggs glued back-to-back", "a central spherical bulge surrounded by a thin, flat rotating disc"),
        ("a flat spinning plate with a spherical central knob", "a central stellar bulge surrounded by a wide disc with spiral arms")
    ]
    analogy, struct_desc = rng.choice(analogies)
    prompt = (
        f"Astronomers often describe the overall 3D shape of the Milky Way Galaxy using the physical analogy of {analogy}.\n\n"
        "What are the primary structural components that make up this morphology?"
    )
    correct = f"A dense central galactic bulge, a broad flattened rotating disc containing spiral arms, and an outer spherical halo."
    options = [
        correct,
        "A solid hollow iron sphere containing oceans of liquid water on its interior surface.",
        "A completely flat 2D rectangle with sharp corners suspended in empty space.",
        "A single massive star surrounded by eight concentric rings of solid concrete."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Structure of spiral galaxies:\n"
        "The Milky Way consists of three main anatomical regions:\n"
        "1. Central Bulge: a dense concentration of older stars.\n"
        "2. Galactic Disc: flattened region (~100 times wider than thick) housing spiral arms, gas, dust, and young stars.\n"
        "3. Galactic Halo: sparse spherical distribution of globular clusters and dark matter."
    )
    return {
        "id": f"ns8_bss_04_{rng.randint(100000, 999999)}",
        "subskill": "04_milky_way_morphology_disk_bulge_and_halo",
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
            "tier_1": "Recall the three main regions of a spiral galaxy.",
            "tier_2": "Central bulge, flat disk with spiral arms, and outer halo.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["milky_way_morphology_bulge_disk_halo"]
    }


def arch_05_milky_way_dimensions_diameter_and_aspect_ratio(rng: random.Random) -> Dict[str, Any]:
    diam_ly = rng.choice(["100 000 light years", "approximately 100 000 to 120 000 light years"])
    thickness_ly = rng.choice(["1 000 light years", "about 1 000 light years"])
    prompt = (
        f"The disc of our Milky Way Galaxy measures {diam_ly} in diameter, while its stellar disc thickness is only {thickness_ly}.\n\n"
        "What is the approximate ratio of the galaxy's diameter to its disc thickness, illustrating how extraordinarily thin it is?"
    )
    correct = "Approximately 100 : 1 (the galaxy is roughly 100 times wider than it is thick)."
    options = [
        correct,
        "Approximately 1 : 1 (the galaxy is a perfect solid sphere as thick as it is wide).",
        "Approximately 10 000 : 1 (the disc has the proportions of a single atom).",
        "Approximately 2 : 1 (the galaxy is egg-shaped with thickness half its width)."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Calculate aspect ratio:\n"
        "Diameter = 100 000 ly; Thickness = 1 000 ly.\n"
        "Step 2: Divide diameter by thickness:\n"
        "Ratio = 100 000 / 1 000 = 100 : 1.\n"
        "The galactic disc is roughly 100 times wider than it is thick, much like a thin coin or compact disc."
    )
    return {
        "id": f"ns8_bss_05_{rng.randint(100000, 999999)}",
        "subskill": "05_milky_way_dimensions_diameter_and_aspect_ratio",
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
            "tier_1": "Divide 100 000 by 1 000.",
            "tier_2": "100 000 / 1 000 = 100.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["milky_way_dimensions_aspect_ratio"]
    }


def arch_06_milky_way_star_count_estimation(rng: random.Random) -> Dict[str, Any]:
    notation = rng.choice(["200 × 10⁹", "between 100 billion and 400 billion"])
    prompt = (
        f"Astronomers estimate that the Milky Way Galaxy contains approximately {notation} stars, with our Sun being merely one ordinary member.\n\n"
        "Which statement correctly conveys this staggering number in standard numerical terms?"
    )
    correct = "200 billion stars (200 000 000 000 stars)."
    options = [
        correct,
        "200 million stars (200 000 000 stars).",
        "200 thousand stars (200 000 stars).",
        "200 trillion stars (200 000 000 000 000 stars)."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand exponential scale:\n"
        "10⁹ is one billion (1 000 000 000).\n"
        "Step 2: Multiply by 200:\n"
        "200 × 10⁹ = 200 billion stars = 200 000 000 000 stars."
    )
    return {
        "id": f"ns8_bss_06_{rng.randint(100000, 999999)}",
        "subskill": "06_milky_way_star_count_estimation",
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
            "tier_1": "What does 10⁹ represent?",
            "tier_2": "10⁹ is a billion.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["milky_way_star_count_orders_of_magnitude"]
    }


def arch_07_milky_way_spiral_arms_composition_young_blue_stars(rng: random.Random) -> Dict[str, Any]:
    arm = rng.choice(["Perseus Arm", "Scutum-Centaurus Arm", "Sagittarius Arm"])
    prompt = (
        f"When observing spiral galaxies, including major arms of the Milky Way such as the {arm}, the spiral arms appear distinctly **bluish** in color.\n\n"
        "What astrophysical factor causes the spiral arms to glow with a predominantly blue hue?"
    )
    correct = "Spiral arms are active sites of star formation containing massive, hot, short-lived young stars that radiate high-energy blue photons."
    options = [
        correct,
        "Spiral arms are filled with cold liquid water oceans floating weightlessly in space.",
        "Spiral arms are illuminated by blue neon signs built by alien civilizations.",
        "Spiral arms contain only dead white dwarf stars undergoing radioactive decay."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Stellar color and temperature:\n"
        "Hotter stars (surface temperatures > 10 000 K) emit predominantly in the blue and ultraviolet spectrum.\n"
        "Step 2: Spiral arm dynamics:\n"
        "Spiral arms act as gravitational density waves compressing interstellar gas clouds, triggering rapid star formation. Massive O and B stars burn intensely blue and illuminate the arms before dying young."
    )
    return {
        "id": f"ns8_bss_07_{rng.randint(100000, 999999)}",
        "subskill": "07_milky_way_spiral_arms_composition_young_blue_stars",
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
            "tier_1": "What kind of stars are blue (hot/young or cool/old)?",
            "tier_2": "Hot, massive, young stars.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["spiral_arms_blue_star_formation"]
    }


def arch_08_milky_way_central_bulge_older_red_orange_stars(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In contrast to the bluish spiral arms, the **central bulge** of the Milky Way Galaxy glows with a distinctly warm **yellowish-orange** color.\n\n"
        "Why is the galactic bulge dominated by yellowish and reddish light?"
    )
    correct = "The bulge consists predominantly of older, cooler stars (red giants and low-mass stars) where active star formation has long ceased."
    options = [
        correct,
        "The bulge is on fire due to endless coal combustion in vacuum.",
        "The bulge contains huge clouds of rusting iron dust heated by Earth's sunlight.",
        "The bulge reflects yellow sodium streetlights from major metropolitan cities on Earth."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Stellar populations:\n"
        "Population II stars reside in the galactic bulge and halo.\n"
        "Step 2: Spectral color:\n"
        "Most gas and dust has been swept or consumed, so new massive blue stars cannot form. The remaining stellar population consists of long-lived, low-mass stars and evolved red giants, whose lower surface temperatures (~3 000–5 000 K) emit reddish-orange light."
    )
    return {
        "id": f"ns8_bss_08_{rng.randint(100000, 999999)}",
        "subskill": "08_milky_way_central_bulge_older_red_orange_stars",
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
            "tier_1": "What stars produce orange/red light?",
            "tier_2": "Older, cooler stars (red giants and K/M dwarfs).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["central_bulge_older_stars_color"]
    }


def arch_09_milky_way_dust_lanes_interstellar_extinction(rng: random.Random) -> Dict[str, Any]:
    feature = rng.choice(["the Great Rift", "the Coalsack Nebula in the Southern Cross", "dark dust lanes"])
    prompt = (
        f"When looking toward the bright band of the Milky Way, observers see dramatic dark streaks and patches, such as {feature}, where no stars appear to exist.\n\n"
        "What are these dark lanes actually made of?"
    )
    correct = "Dense interstellar clouds of microscopic cosmic dust and cold molecular gas that absorb and scatter visible light from background stars."
    options = [
        correct,
        "Physical empty holes or tunnels punched completely through the galaxy by rogue black holes.",
        "Flocks of millions of space bats blocking the light of the stars.",
        "Opaque sheets of black volcanic rock floating between planets."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Interstellar extinction:\n"
        "Space between stars is permeated by the interstellar medium (ISM).\n"
        "Step 2: Dust grains:\n"
        "Microscopic silicate and carbon dust grains absorb and scatter optical light (interstellar reddening and extinction). The stars behind these clouds are not missing; their visible light is simply blocked by dense dust lanes."
    )
    return {
        "id": f"ns8_bss_09_{rng.randint(100000, 999999)}",
        "subskill": "09_milky_way_dust_lanes_interstellar_extinction",
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
            "tier_1": "Are these real empty gaps in space or clouds of dust?",
            "tier_2": "Dense clouds of interstellar dust absorbing background starlight.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["interstellar_dust_lanes_extinction"]
    }


def arch_10_sun_location_in_orion_local_spur(rng: random.Random) -> Dict[str, Any]:
    arm_name = "Orion Arm (also called the Local Arm or Orion Spur)"
    prompt = (
        "Our Sun is not located at the centre of the Milky Way Galaxy, nor is it at the outer rim.\n\n"
        f"In which spiral structure is our Solar System located, and at approximately what distance from the galactic centre?"
    )
    correct = f"In the {arm_name}, located approximately halfway out (about 26 000 to 28 000 light years) from the galactic centre."
    options = [
        correct,
        "Directly inside the supermassive black hole at the absolute physical center of the galaxy.",
        "On the extreme outermost edge of the galaxy, 500 000 light years away in empty intergalactic space.",
        "In the Sagittarius Arm, exactly 10 light days from the core."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify Sun's spiral arm:\n"
        "The Solar System resides within a minor spiral structure called the Orion Arm (or Local Spur), situated between the Perseus Arm and Sagittarius Arm.\n"
        "Step 2: Distance from centre:\n"
        "The Sun is located roughly halfway out from the galactic center, at a distance of ~8 kiloparsecs (~26 000–28 000 light years)."
    )
    return {
        "id": f"ns8_bss_10_{rng.randint(100000, 999999)}",
        "subskill": "10_sun_location_in_orion_local_spur",
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
            "tier_1": "What is the name of our local spiral arm?",
            "tier_2": "The Orion Arm, located roughly halfway out from the core.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sun_location_orion_arm_halfway"]
    }


def arch_11_sun_galactic_orbital_velocity_250_km_s(rng: random.Random) -> Dict[str, Any]:
    speed_km_s = rng.choice([250, 220, 230])
    prompt = (
        f"Just as the Earth orbits the Sun, our entire Solar System orbits around the centre of the Milky Way Galaxy at an immense speed of approximately **{speed_km_s} km/s** (nearly 900 000 km/h).\n\n"
        "Why do human beings on Earth feel no physical sensation of this colossal orbital velocity?"
    )
    correct = "Because the Earth, the atmosphere, and everything on the planet share the exact same steady velocity in the frictionless vacuum of space, without abrupt acceleration."
    options = [
        correct,
        "Because the speed of the Sun is canceled out by the rotation of the Moon.",
        "Because our bodies are glued to the ground by special electromagnetic magnets in the soil.",
        "Because the Solar System is actually stationary and does not move at all."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Physics of uniform motion:\n"
        "According to Newton's First Law of Motion, observers cannot feel constant uniform velocity; human senses only perceive acceleration (changes in speed or direction).\n"
        "Step 2: Shared reference frame:\n"
        "Everything in the Solar System shares the same orbital motion through the vacuum of space, experiencing negligible net acceleration relative to one another."
    )
    return {
        "id": f"ns8_bss_11_{rng.randint(100000, 999999)}",
        "subskill": "11_sun_galactic_orbital_velocity_250_km_s",
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
            "tier_1": "Do humans feel constant speed or do we only feel acceleration?",
            "tier_2": "We only feel acceleration; constant velocity in a shared frame is imperceptible.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["galactic_orbital_speed_uniform_motion"]
    }


def arch_12_sun_cosmic_year_orbital_period_225_million_years(rng: random.Random) -> Dict[str, Any]:
    period = rng.choice(["225 to 250 million Earth years", "approximately 230 million years"])
    prompt = (
        f"Even traveling at 250 km/s, the vast scale of the Milky Way means it takes our Sun **{period}** to complete one full revolution around the galactic centre—a duration known as one **cosmic year** (or galactic year).\n\n"
        "What prominent creatures walked the Earth when our Solar System was last at this current position in the galaxy?"
    )
    correct = "Early dinosaurs (during the Triassic period), before mammals or birds had evolved."
    options = [
        correct,
        "Modern humans using computers and smartphones.",
        "Advanced spacefaring human civilizations during the Roman Empire.",
        "No living organisms existed because the Earth had not yet formed."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Cosmic Year duration:\n"
        "One galactic orbit takes ~225–250 million years.\n"
        "Step 2: Geologic timeline comparison:\n"
        "225 million years ago was the early Mesozoic Era (Triassic Period), when the first dinosaurs appeared on the supercontinent Pangaea. The Sun has completed only ~20–25 orbits since the Earth formed 4,5 billion years ago."
    )
    return {
        "id": f"ns8_bss_12_{rng.randint(100000, 999999)}",
        "subskill": "12_sun_cosmic_year_orbital_period_225_million_years",
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
            "tier_1": "What period of Earth history was 225 million years ago?",
            "tier_2": "The age of the dinosaurs (Triassic).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["cosmic_year_geological_timescale"]
    }


def arch_13_sagittarius_a_star_supermassive_black_hole_center(rng: random.Random) -> Dict[str, Any]:
    mass_suns = rng.choice(["approximately 4 million", "about 4,1 million"])
    prompt = (
        f"At the very heart of the Milky Way lies a compact, enigmatic astronomical radio source designated **Sagittarius A*** (Sgr A*), possessing a mass {mass_suns} times that of our Sun.\n\n"
        "What type of celestial object is Sagittarius A*?"
    )
    correct = "A supermassive black hole whose extreme gravitational field governs the orbits of surrounding inner stars."
    options = [
        correct,
        "A giant planet made entirely of solid diamonds orbiting Mercury.",
        "A cluster of ordinary incandescent lightbulbs placed on an artificial satellite.",
        "A superheated hollow comet filled with pure steam."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Galactic centre dynamics:\n"
        "Observations tracking the orbits of stars (such as star S2) orbiting the exact center of our galaxy revealed a non-luminous mass of 4 million solar masses packed into a region smaller than our solar system.\n"
        "Step 2: Identification:\n"
        "Sagittarius A* is a supermassive black hole, photographed in 2022 by the Event Horizon Telescope."
    )
    return {
        "id": f"ns8_bss_13_{rng.randint(100000, 999999)}",
        "subskill": "13_sagittarius_a_star_supermassive_black_hole_center",
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
            "tier_1": "What object with 4 million solar masses resides at the center of the galaxy?",
            "tier_2": "A supermassive black hole.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sagittarius_a_star_black_hole"]
    }


def arch_14_speed_of_light_constant_300000_km_s(rng: random.Random) -> Dict[str, Any]:
    speed = rng.choice(["300 000 km/s", "3 × 10⁸ m/s"])
    prompt = (
        f"In physics and astronomy, the speed of light in a vacuum is denoted by the constant **c** and equals approximately **{speed}**.\n\n"
        "What makes the speed of light a cosmic speed limit according to modern physics?"
    )
    correct = "Nothing in the universe with mass can accelerate to or exceed the speed of light in a vacuum; light travels faster than any other physical signal."
    options = [
        correct,
        "Light travels slower than sound waves in air on a hot summer afternoon.",
        "Spaceships powered by gasoline easily travel at ten times the speed of light.",
        "Light stops completely whenever it encounters empty space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: State speed of light:\n"
        "c ≈ 300 000 km/s = 3 × 10⁸ m/s.\n"
        "Step 2: Cosmic constant:\n"
        "Under Einstein's theory of relativity, the speed of light in vacuum is the invariant upper speed limit for the transmission of all matter, energy, and information."
    )
    return {
        "id": f"ns8_bss_14_{rng.randint(100000, 999999)}",
        "subskill": "14_speed_of_light_constant_300000_km_s",
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
            "tier_1": "Can anything travel faster than the speed of light in a vacuum?",
            "tier_2": "No, it is the cosmic speed limit (300 000 km/s).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["speed_of_light_fundamental_constant"]
    }


def arch_15_light_second_and_moon_distance_travel_time(rng: random.Random) -> Dict[str, Any]:
    dist_km = rng.choice([384400, 390000, 380000])
    time_s = dist_km / 300000.0
    prompt = (
        f"The Moon orbits Earth at an average distance of approximately {dist_km:,} km. Light travels at 300 000 km/s.\n\n"
        f"Using the relationship time = distance / speed, how many **light seconds** away is the Moon from Earth?"
    )
    correct = f"Approximately {time_s:.2f} seconds (about 1,3 light seconds)."
    options = [
        correct,
        f"Approximately {time_s * 60:.1f} minutes.",
        f"Approximately {time_s * 3600:.0f} hours.",
        "Exactly 0 seconds because light travels instantaneously across any distance."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Formula:\n"
        f"time = distance / speed_of_light\n"
        f"Step 2: Calculation:\n"
        f"t = {dist_km:,} km / 300 000 km/s = {time_s:.2f} seconds ≈ 1,3 light seconds.\n"
        "When Apollo astronauts talked to Mission Control, radio signals (traveling at the speed of light) took ~1,3 seconds each way."
    )
    return {
        "id": f"ns8_bss_15_{rng.randint(100000, 999999)}",
        "subskill": "15_light_second_and_moon_distance_travel_time",
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
            "tier_1": "Divide ~384 400 km by 300 000 km/s.",
            "tier_2": "The result is approximately 1,3 seconds.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["light_second_moon_communication_delay"]
    }


def arch_16_light_minute_and_sun_earth_distance_8_minutes(rng: random.Random) -> Dict[str, Any]:
    dist_km = rng.choice([149600000, 150000000])
    mins = (dist_km / 300000.0) / 60.0
    prompt = (
        f"The average distance from the Sun to the Earth is approximately {dist_km:,} km (1 Astronomical Unit). Light travels at 300 000 km/s.\n\n"
        "How long does it take for a photon of sunlight to travel from the surface of the Sun to Earth?"
    )
    correct = f"Approximately 8,3 minutes (about 500 seconds / 8 minutes and 20 seconds)."
    options = [
        correct,
        "Exactly 8 hours and 20 minutes.",
        "Exactly 8 days.",
        "0,001 seconds (instantaneous)."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Calculate travel time in seconds:\n"
        f"t = 150 000 000 km / 300 000 km/s = 500 seconds.\n"
        "Step 2: Convert to minutes:\n"
        "500 s / 60 s/min = 8,33 minutes (8 minutes and 20 seconds).\n"
        "When we look at the Sun, we are seeing it as it existed over 8 minutes ago."
    )
    return {
        "id": f"ns8_bss_16_{rng.randint(100000, 999999)}",
        "subskill": "16_light_minute_and_sun_earth_distance_8_minutes",
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
            "tier_1": "Divide 500 seconds by 60.",
            "tier_2": "It takes approximately 8,3 minutes (8 minutes 20 seconds).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["light_travel_time_sun_to_earth"]
    }


def arch_17_light_hour_and_solar_system_outer_boundary(rng: random.Random) -> Dict[str, Any]:
    planet, dist_au, hours = rng.choice([
        ("Jupiter", 5.2, "about 43 light minutes"),
        ("Saturn", 9.5, "about 1,3 light hours"),
        ("Neptune", 30.0, "about 4,1 light hours"),
        ("Pluto", 39.5, "about 5,5 light hours")
    ])
    prompt = (
        f"Outer planetary probes operating at {planet} ({dist_au} AU from the Sun) communicate via radio signals traveling at the speed of light.\n\n"
        f"Approximately how long does a radio signal take to reach Earth from **{planet}**?"
    )
    correct = f"Approximately {hours}."
    options = [
        correct,
        "Less than 1 millisecond.",
        "Approximately 42 years.",
        "Exactly 3 weeks."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Calculate distance in light time:\n"
        f"1 AU = 8,3 light minutes.\n"
        f"At {dist_au} AU, distance in light time = {dist_au} × 8,3 minutes ≈ {hours}.\n"
        "This latency requires deep space probes to perform operations autonomously."
    )
    return {
        "id": f"ns8_bss_17_{rng.randint(100000, 999999)}",
        "subskill": "17_light_hour_and_solar_system_outer_boundary",
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
            "tier_1": f"Think about communication delay with {planet}.",
            "tier_2": f"It takes {hours}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["outer_planet_light_travel_latency"]
    }


def arch_18_light_year_definition_and_kilometer_distance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A **light year** is the foundational unit used by astronomers to express distances between stars.\n\n"
        "What is the precise definition of a light year, and approximately how many kilometers does it equal?"
    )
    correct = "The total distance light travels through a vacuum in one Earth year, equal to approximately 9,46 trillion kilometers (9,5 × 10¹² km)."
    options = [
        correct,
        "The time it takes the Earth to orbit the Sun once at the speed of sound.",
        "The brightness of a star measured from one astronomical unit away.",
        "The total lifespan of an average yellow dwarf star like the Sun."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Light year definition:\n"
        "Distance = speed × time\n"
        "Step 2: Calculate for 1 year (365,25 days = 31 557 600 seconds):\n"
        "Distance = 300 000 km/s × 31 557 600 s ≈ 9,46 × 10¹² km (roughly 9,5 trillion kilometers).\n"
        "Note: A light year is a measure of DISTANCE, not time."
    )
    return {
        "id": f"ns8_bss_18_{rng.randint(100000, 999999)}",
        "subskill": "18_light_year_definition_and_kilometer_distance",
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
            "tier_1": "Is a light year a measure of time or distance?",
            "tier_2": "It is the distance light travels in one year (~9,5 trillion km).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["light_year_distance_vs_time_misconception"]
    }


def arch_19_lookback_time_astronomical_time_machine_concept(rng: random.Random) -> Dict[str, Any]:
    star_name, dist_ly = rng.choice([
        ("Betelgeuse", 640),
        ("Rigel", 860),
        ("Deneb", 2600),
        ("Sirius", 8.6)
    ])
    prompt = (
        f"Astronomers observe the bright star **{star_name}**, which is located **{dist_ly} light years** from Earth.\n\n"
        f"Why is looking at {star_name} through a telescope scientifically equivalent to looking back into the past?"
    )
    correct = f"Because the light arriving at our eyes right now left {star_name} {dist_ly} years ago; we are seeing what it looked like {dist_ly} years in the past."
    options = [
        correct,
        f"Because telescopes bend spacetime to transport human observers physically into {star_name}'s past.",
        f"Because {star_name} moves backwards along its orbit every night.",
        "Because stars in the sky only reflect historical sunlight from Earth's ancient past."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Finite speed of light:\n"
        f"Light from an object {dist_ly} light years away takes exactly {dist_ly} years to travel across space to Earth.\n"
        "Step 2: Lookback time:\n"
        f"We never see the universe as it is right now, but as it was when the photons were emitted—{dist_ly} years ago in the case of {star_name}."
    )
    return {
        "id": f"ns8_bss_19_{rng.randint(100000, 999999)}",
        "subskill": "19_lookback_time_astronomical_time_machine_concept",
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
            "tier_1": f"How long did the light take to reach us from {star_name}?",
            "tier_2": f"It took {dist_ly} years, so we see it as it was {dist_ly} years ago.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lookback_time_finite_speed_of_light"]
    }


def arch_20_proxima_centauri_closest_star_distance_4_point_2_ly(rng: random.Random) -> Dict[str, Any]:
    dist_ly = rng.choice(["4,24 light years", "approximately 4,2 light years"])
    prompt = (
        f"Excluding our Sun, the closest known star to Earth is **Proxima Centauri**, located {dist_ly} away.\n\n"
        "What type of star is Proxima Centauri, and can it be seen with the unaided naked eye?"
    )
    correct = "It is a faint, low-mass red dwarf star that is far too dim to be seen without a telescope."
    options = [
        correct,
        "It is a brilliant blue hypergiant easily visible as the brightest star in the sky.",
        "It is a dead neutron star that emits zero visible light or radiation.",
        "It is an artificial space station built by astronauts in 1969."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Proxima Centauri properties:\n"
        "Located 4,24 light years (40 trillion km) away.\n"
        "Step 2: Stellar type and visibility:\n"
        "Despite its proximity, it is a small, cool red dwarf (spectral class M) with an apparent magnitude of 11,05—well below the naked-eye limit of magnitude 6. A telescope is required to observe it."
    )
    return {
        "id": f"ns8_bss_20_{rng.randint(100000, 999999)}",
        "subskill": "20_proxima_centauri_closest_star_distance_4_point_2_ly",
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
            "tier_1": "Is Proxima Centauri a red dwarf or a giant star?",
            "tier_2": "It is a faint red dwarf invisible to the naked eye.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["proxima_centauri_red_dwarf_invisibility"]
    }


def arch_21_alpha_centauri_triple_star_system_members(rng: random.Random) -> Dict[str, Any]:
    comp_star = rng.choice(["Alpha Centauri A", "Alpha Centauri B", "Proxima Centauri"])
    prompt = (
        f"The nearest stellar system to our Sun is the **Alpha Centauri** triple star system.\n\n"
        f"Which members constitute this three-star gravitational system, and how does **{comp_star}** fit into it?"
    )
    correct = "A central binary pair of bright Sun-like stars (Alpha Centauri A and B) orbited at a great distance by the small red dwarf Proxima Centauri."
    options = [
        correct,
        "Three identical white dwarf stars that collide with each other every twenty-four hours.",
        "A black hole orbited by two ringed gas giant planets.",
        "Three giant burning planets orbiting inside the Sun's outer corona."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Structure of Alpha Centauri system:\n"
        "1. Alpha Centauri A: yellow dwarf star (spectral class G2V, slightly larger than the Sun).\n"
        "2. Alpha Centauri B: orange dwarf star (spectral class K1V).\n"
        "They form a close binary pair orbiting each other every ~80 years.\n"
        "3. Proxima Centauri (Alpha Centauri C): small red dwarf orbiting the central pair at a distance of ~0,2 light years."
    )
    return {
        "id": f"ns8_bss_21_{rng.randint(100000, 999999)}",
        "subskill": "21_alpha_centauri_triple_star_system_members",
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
            "tier_1": "How many stars make up the Alpha Centauri system?",
            "tier_2": "Three stars: binary pair A and B plus the red dwarf Proxima Centauri.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["alpha_centauri_triple_system_structure"]
    }


def arch_22_southern_cross_and_pointers_celestial_navigation(rng: random.Random) -> Dict[str, Any]:
    pointer1, pointer2 = "Alpha Centauri", "Beta Centauri (Hadar)"
    prompt = (
        "In the Southern Hemisphere sky, the **Southern Cross (Crux)** and the two bright **Pointers** are iconic celestial landmarks.\n\n"
        f"Which two bright stars serve as the Pointers, and how do they assist in finding true South?"
    )
    correct = f"The Pointers are {pointer1} and {pointer2}; extending a line through them and intersecting the long axis of the Southern Cross identifies the South Celestial Pole."
    options = [
        correct,
        "The Pointers are Sirius and Vega; they point directly toward the North Star (Polaris).",
        "The Pointers are Mars and Venus; they follow the direction of the trade winds.",
        "The Pointers are two artificial satellites placed in orbit by the South African Navy."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify the Pointers:\n"
        f"The two bright stars pointing toward Crux are {pointer1} and {pointer2}.\n"
        "Step 2: Celestial navigation method:\n"
        "1. Extend the long axis of Crux 4,5 times.\n"
        "2. Draw a perpendicular bisector between Alpha and Beta Centauri.\n"
        "3. The intersection point marks the South Celestial Pole, directly above true geographic South."
    )
    return {
        "id": f"ns8_bss_22_{rng.randint(100000, 999999)}",
        "subskill": "22_southern_cross_and_pointers_celestial_navigation",
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
            "tier_1": "What are the names of the two pointer stars?",
            "tier_2": "Alpha Centauri and Beta Centauri.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["southern_cross_pointers_navigation"]
    }


def arch_23_interstellar_travel_times_chemical_rocket_vs_light(rng: random.Random) -> Dict[str, Any]:
    speed_km_s = rng.choice([17, 15, 20])
    prompt = (
        f"A human interstellar robotic probe traveling at a typical chemical rocket speed of {speed_km_s} km/s (~60 000 km/h) is sent toward our nearest star, Proxima Centauri (4,24 light years away).\n\n"
        "Approximately how long would it take this spacecraft to reach Proxima Centauri?"
    )
    correct = "Approximately 70 000 to 80 000 years."
    options = [
        correct,
        "Approximately 4,24 years.",
        "Approximately 8 months.",
        "Approximately 2 weeks."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Calculate total distance:\n"
        "4,24 ly = 4,24 × 9,46 × 10¹² km ≈ 40 × 10¹² km.\n"
        f"Step 2: Calculate travel time at {speed_km_s} km/s:\n"
        f"Time = 40 × 10¹² km / {speed_km_s} km/s ≈ 2,35 × 10¹² seconds.\n"
        "Convert to years (3,15 × 10⁷ seconds/year):\n"
        "Time ≈ 75 000 years!\n"
        "This demonstrates the immense challenge of interstellar travel with chemical propulsion."
    )
    return {
        "id": f"ns8_bss_23_{rng.randint(100000, 999999)}",
        "subskill": "23_interstellar_travel_times_chemical_rocket_vs_light",
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
            "tier_1": "Could a conventional spacecraft reach Proxima Centauri in a human lifetime?",
            "tier_2": "No, it takes over 70 000 years.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["interstellar_distances_scale_challenge"]
    }


def arch_24_stellar_parallax_nearby_star_distance_measurement(rng: random.Random) -> Dict[str, Any]:
    baseline = rng.choice(["6 months apart (across Earth's 300 million km orbit diameter)", "half a year apart from opposite sides of Earth's orbit"])
    prompt = (
        f"Astronomers use the geometric method of **stellar parallax** by photographing a nearby star against distant background stars {baseline}.\n\n"
        "What fundamental geometric principle allows this apparent shift to reveal the star's exact distance?"
    )
    correct = "Triangulation: the apparent angular shift of the foreground star against the background baseline allows direct trigonometric calculation of distance."
    options = [
        correct,
        "The star moves physically through space because it is repelled by the Earth's magnetic poles.",
        "The telescope lenses expand and contract due to temperature changes between summer and winter.",
        "Light rays bend due to the gravitational pull of passing airplanes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Parallax concept:\n"
        "Hold a finger in front of your face and close one eye, then the other; the finger appears to jump relative to the background.\n"
        "Step 2: Astronomical application:\n"
        "Earth's orbit around the Sun provides a baseline of 2 AU (300 million km). Nearby stars display a tiny apparent angular shift (parallax angle p) relative to distant background stars, where distance d = 1 / p."
    )
    return {
        "id": f"ns8_bss_24_{rng.randint(100000, 999999)}",
        "subskill": "24_stellar_parallax_nearby_star_distance_measurement",
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
            "tier_1": "What geometric technique measures distance via angle and baseline?",
            "tier_2": "Triangulation / stellar parallax.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["stellar_parallax_triangulation_distance"]
    }


def arch_25_apparent_brightness_vs_intrinsic_stellar_luminosity(rng: random.Random) -> Dict[str, Any]:
    star1, star2 = rng.choice([
        ("Sirius (8,6 light years away)", "Rigel (860 light years away)"),
        ("Alpha Centauri (4,3 light years away)", "Deneb (2 600 light years away)")
    ])
    prompt = (
        f"When viewing the night sky, {star1} appears brighter to our eyes than {star2}, even though {star2} actually radiates thousands of times more total energy.\n\n"
        "What fundamental astronomical distinction explains this observation?"
    )
    correct = "The distinction between apparent brightness (how bright an object appears from Earth, governed by the inverse-square law of distance) and intrinsic luminosity (actual total energy output)."
    options = [
        correct,
        "Distant stars only emit dark matter photons which cannot be detected by human retinas.",
        "Earth's atmosphere absorbs 99,9% of light from all stars located beyond 10 light years.",
        "Nearby stars have higher gravitational pull which magnifies their photons through space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Define terms:\n"
        "Intrinsic Luminosity: the total radiant power emitted by a star (in Watts).\n"
        "Apparent Brightness: radiant flux received per unit area on Earth (b = L / (4πd²)).\n"
        "Step 2: Effect of distance:\n"
        "A low-luminosity star very close to Earth can easily appear brighter in our night sky than a hyper-luminous supergiant star hundreds of light years away."
    )
    return {
        "id": f"ns8_bss_25_{rng.randint(100000, 999999)}",
        "subskill": "25_apparent_brightness_vs_intrinsic_stellar_luminosity",
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
            "tier_1": "What is the difference between total light emitted and light received?",
            "tier_2": "Apparent brightness depends heavily on distance (inverse-square law).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["apparent_brightness_vs_intrinsic_luminosity"]
    }


BUILDERS_01_25 = {
    "01_galaxy_definition_gravitationally_bound_system": arch_01_galaxy_definition_gravitationally_bound_system,
    "02_milky_way_band_appearance_internal_perspective": arch_02_milky_way_band_appearance_internal_perspective,
    "03_milky_way_historical_naming_greek_roman": arch_03_milky_way_historical_naming_greek_roman,
    "04_milky_way_morphology_disk_bulge_and_halo": arch_04_milky_way_morphology_disk_bulge_and_halo,
    "05_milky_way_dimensions_diameter_and_aspect_ratio": arch_05_milky_way_dimensions_diameter_and_aspect_ratio,
    "06_milky_way_star_count_estimation": arch_06_milky_way_star_count_estimation,
    "07_milky_way_spiral_arms_composition_young_blue_stars": arch_07_milky_way_spiral_arms_composition_young_blue_stars,
    "08_milky_way_central_bulge_older_red_orange_stars": arch_08_milky_way_central_bulge_older_red_orange_stars,
    "09_milky_way_dust_lanes_interstellar_extinction": arch_09_milky_way_dust_lanes_interstellar_extinction,
    "10_sun_location_in_orion_local_spur": arch_10_sun_location_in_orion_local_spur,
    "11_sun_galactic_orbital_velocity_250_km_s": arch_11_sun_galactic_orbital_velocity_250_km_s,
    "12_sun_cosmic_year_orbital_period_225_million_years": arch_12_sun_cosmic_year_orbital_period_225_million_years,
    "13_sagittarius_a_star_supermassive_black_hole_center": arch_13_sagittarius_a_star_supermassive_black_hole_center,
    "14_speed_of_light_constant_300000_km_s": arch_14_speed_of_light_constant_300000_km_s,
    "15_light_second_and_moon_distance_travel_time": arch_15_light_second_and_moon_distance_travel_time,
    "16_light_minute_and_sun_earth_distance_8_minutes": arch_16_light_minute_and_sun_earth_distance_8_minutes,
    "17_light_hour_and_solar_system_outer_boundary": arch_17_light_hour_and_solar_system_outer_boundary,
    "18_light_year_definition_and_kilometer_distance": arch_18_light_year_definition_and_kilometer_distance,
    "19_lookback_time_astronomical_time_machine_concept": arch_19_lookback_time_astronomical_time_machine_concept,
    "20_proxima_centauri_closest_star_distance_4_point_2_ly": arch_20_proxima_centauri_closest_star_distance_4_point_2_ly,
    "21_alpha_centauri_triple_star_system_members": arch_21_alpha_centauri_triple_star_system_members,
    "22_southern_cross_and_pointers_celestial_navigation": arch_22_southern_cross_and_pointers_celestial_navigation,
    "23_interstellar_travel_times_chemical_rocket_vs_light": arch_23_interstellar_travel_times_chemical_rocket_vs_light,
    "24_stellar_parallax_nearby_star_distance_measurement": arch_24_stellar_parallax_nearby_star_distance_measurement,
    "25_apparent_brightness_vs_intrinsic_stellar_luminosity": arch_25_apparent_brightness_vs_intrinsic_stellar_luminosity,
}
