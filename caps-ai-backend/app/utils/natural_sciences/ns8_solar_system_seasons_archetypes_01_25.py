"""Grade 8 Natural Sciences - The Solar System: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr8/Term 4/01. The Solar System.md
Focus: The Sun (mass, structure, sunspots, pinhole safety), Solar system scale (AU), Terrestrial vs Gas giants,
Mercury, Venus (runaway greenhouse, retrograde rotation), Earth, Mars (Olympus Mons, water),
Asteroid belt, meteors/meteorites, impact craters, Jupiter (Great Red Spot, Galilean moons), Saturn (rings, Titan).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_sun_mass_and_gravitational_dominance(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice(["99.8%", "over 99.8%", "about 99.86%"])
    prompt = (
        f"The Sun contains approximately {pct} of all the total mass in our solar system.\n\n"
        "What is the crucial physical consequence of this enormous concentration of solar mass?"
    )
    correct = "The Sun's immense gravitational pull dominates the solar system, holding all planets, asteroids, and comets in stable orbits."
    options = [
        correct,
        "The Sun causes all planets to stop spinning on their internal axes.",
        "The Sun's mass pushes planets away in straight lines into interstellar space.",
        "The Sun's mass absorbs all cosmic radio waves, making space pitch black."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand gravitational force proportional to mass:\n"
        "Gravitational force depends directly on mass (F = G*M*m/r²).\n"
        "Step 2: Dominance of the Sun:\n"
        "Because the Sun possesses 99.8% of solar system mass, its gravitational field establishes the orbital framework for all planets and minor bodies."
    )
    return {
        "id": f"ns8_sol_01_{rng.randint(100000, 999999)}",
        "subskill": "01_sun_mass_and_gravitational_dominance",
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
            "tier_1": "What does a massive object exert across space?",
            "tier_2": "The Sun's gravity holds all planets in orbit.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["solar_mass_and_gravity_dominance"]
    }


def arch_02_sun_structure_photosphere_and_corona(rng: random.Random) -> Dict[str, Any]:
    layers = [
        ("photosphere", "the visible bright surface layer of the Sun from which visible sunlight radiates", "approximately 5 500 °C"),
        ("corona", "the tenuous, halo-like outer atmosphere visible during total solar eclipses", "over 1 000 000 °C")
    ]
    name, defn, temp = rng.choice(layers)
    prompt = (
        f"In solar physics, {defn} has an average temperature of {temp}.\n\n"
        f"Which layer of the Sun does this describe?"
    )
    correct = name.capitalize()
    options = ["Photosphere", "Corona", "Chromosphere", "Core"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify solar atmospheric layers:\n"
        f"- Core: Central fusion engine (~15 million °C).\n"
        f"- Photosphere: Visible surface layer (~5 500 °C).\n"
        f"- Chromosphere: Reddish middle layer.\n"
        f"- Corona: Outermost ethereal atmosphere (> 1 million °C).\n"
        f"Step 2: Conclusion: {defn} refers to the {correct}."
    )
    return {
        "id": f"ns8_sol_02_{rng.randint(100000, 999999)}",
        "subskill": "02_sun_structure_photosphere_and_corona",
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
            "tier_1": "Is it the visible glowing surface or the thin outer halo?",
            "tier_2": f"Visible surface is photosphere; outer halo is corona.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["solar_layers_identification_error"]
    }


def arch_03_sunspots_magnetic_activity_and_cycle(rng: random.Random) -> Dict[str, Any]:
    cycle_yrs = rng.choice(["11-year", "roughly 11-year"])
    prompt = (
        f"The number of sunspots visible on the solar photosphere fluctuates over a {cycle_yrs} solar cycle.\n\n"
        "Why do sunspots appear darker than the rest of the solar surface?"
    )
    correct = "Intense local magnetic fields inhibit the upward convection of hot plasma, making sunspots about 1 500 °C cooler than surrounding regions."
    options = [
        correct,
        "Sunspots are solid islands of burnt black rock floating on liquid fire.",
        "Sunspots are holes where the Sun has completely run out of nuclear fuel.",
        "Sunspots are shadows cast by the planet Mercury orbiting very close."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand sunspot physics:\n"
        "Concentrated magnetic field lines choke convection currents of hot gas rising from the interior.\n"
        "Step 2: Contrast effect:\n"
        "The cooler surface (~4 000 K vs 5 800 K) emits less light, appearing dark only by contrast with the blinding surrounding photosphere."
    )
    return {
        "id": f"ns8_sol_03_{rng.randint(100000, 999999)}",
        "subskill": "03_sunspots_magnetic_activity_and_cycle",
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
            "tier_1": "Are sunspots hotter or cooler than the rest of the Sun?",
            "tier_2": "Magnetic fields cool the gas, making them look dark by contrast.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sunspot_temperature_contrast_confusion"]
    }


def arch_04_safe_solar_observation_pinhole_projection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Grade 8 learners want to observe sunspots and solar features during a school science project.\n\n"
        "Which method is safe for observing the Sun?"
    )
    correct = "Projecting the Sun's image through a pinhole camera or telescope eyepiece onto a white cardboard screen without looking through the optics."
    options = [
        correct,
        "Looking directly at the Sun through ordinary dark sunglasses.",
        "Staring directly through a regular optical telescope with the naked eye.",
        "Looking through a CD, DVD, or exposed photographic film."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Danger of direct solar viewing:\n"
        "Concentrated solar rays deliver lethal thermal energy to the retina, causing irreversible blindness (solar retinopathy).\n"
        "Step 2: Safe method:\n"
        "Indirect projection (using a pinhole box or telescope projection screen) allows safe observation without any light entering the human eye directly."
    )
    return {
        "id": f"ns8_sol_04_{rng.randint(100000, 999999)}",
        "subskill": "04_safe_solar_observation_pinhole_projection",
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
            "tier_1": "Never look directly through lenses or sunglasses at the Sun.",
            "tier_2": "Indirect projection onto a screen is safe.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["sunglasses_safe_for_sun_observation_myth"]
    }


def arch_05_solar_system_scale_and_astronomical_units(rng: random.Random) -> Dict[str, Any]:
    au_km = 150000000
    prompt = (
        f"Because distances in our solar system are so vast, astronomers use the **Astronomical Unit (AU)**, "
        f"defined as the average distance from Earth to the Sun (~{au_km:,} km).\n\n"
        "If Jupiter orbits at approximately 5.2 AU from the Sun, what does this value represent?"
    )
    correct = "Jupiter is 5.2 times farther from the Sun than Earth is (roughly 780 million kilometres)."
    options = [
        correct,
        "Jupiter takes 5.2 hours to complete one full rotation.",
        "Jupiter has 5.2 times more moons than all other planets combined.",
        "Jupiter travels at 5.2 kilometres per second through space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand 1 AU definition:\n"
        "1 AU = Distance between Earth and Sun ≈ 150 million km.\n"
        "Step 2: Multiply ratio:\n"
        "5.2 AU = 5.2 × 150 million km = 780 million km, meaning Jupiter is 5.2 times farther from the Sun than Earth."
    )
    return {
        "id": f"ns8_sol_05_{rng.randint(100000, 999999)}",
        "subskill": "05_solar_system_scale_and_astronomical_units",
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
            "tier_1": "1 AU is the Earth-Sun distance.",
            "tier_2": "5.2 AU means 5.2 times that distance.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["astronomical_unit_definition_error"]
    }


def arch_06_terrestrial_vs_gas_giant_planets_contrast(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Astronomers divide the eight major planets of our solar system into **terrestrial planets** and **gas giants**.\n\n"
        "What are the defining physical characteristics of the four inner terrestrial planets?"
    )
    correct = "They are relatively small, rocky bodies with solid surfaces, high densities, few or no moons, and no planetary ring systems."
    options = [
        correct,
        "They are massive spheres of hydrogen gas with no solid surfaces and dozens of moons.",
        "They are made entirely of liquid nitrogen and frozen methane with rings.",
        "They are miniature stars undergoing active nuclear fusion in their cores."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Characterize terrestrial planets (Mercury, Venus, Earth, Mars):\n"
        "- Solid rocky crust and silicate mantle.\n"
        "- High density (~4-5.5 g/cm³).\n"
        "- Small diameters, few moons, zero rings.\n"
        "Step 2: Contrast with gas giants:\n"
        "Gas giants (Jupiter, Saturn, Uranus, Neptune) are massive, gaseous/icy, low-density worlds with extensive ring and moon systems."
    )
    return {
        "id": f"ns8_sol_06_{rng.randint(100000, 999999)}",
        "subskill": "06_terrestrial_vs_gas_giant_planets_contrast",
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
            "tier_1": "Terra means Earth: rocky, solid ground.",
            "tier_2": "Small, rocky, dense, solid surface.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["terrestrial_vs_gas_giant_classification"]
    }


def arch_07_inner_planets_order_and_characteristics(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "What is the correct order of the four **inner rocky planets** starting closest to the Sun?"
    )
    correct = "Mercury -> Venus -> Earth -> Mars"
    options = [
        "Mercury -> Venus -> Earth -> Mars",
        "Venus -> Mercury -> Mars -> Earth",
        "Mercury -> Earth -> Venus -> Mars",
        "Mars -> Earth -> Venus -> Mercury"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Memorize planetary order outward from the Sun:\n"
        "1. Mercury (0.39 AU)\n"
        "2. Venus (0.72 AU)\n"
        "3. Earth (1.0 AU)\n"
        "4. Mars (1.52 AU)"
    )
    return {
        "id": f"ns8_sol_07_{rng.randint(100000, 999999)}",
        "subskill": "07_inner_planets_order_and_characteristics",
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
            "tier_1": "Remember: My Very Educated Mother (Mercury, Venus, Earth, Mars).",
            "tier_2": "Mercury is first, Mars is fourth.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["planetary_order_inversion_error"]
    }


def arch_08_outer_planets_order_and_characteristics(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "What is the correct order of the four **outer gas and ice giant planets** starting from the Asteroid Belt outward?"
    )
    correct = "Jupiter -> Saturn -> Uranus -> Neptune"
    options = [
        "Jupiter -> Saturn -> Uranus -> Neptune",
        "Saturn -> Jupiter -> Neptune -> Uranus",
        "Jupiter -> Uranus -> Saturn -> Neptune",
        "Neptune -> Uranus -> Saturn -> Jupiter"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Sequence the outer planets:\n"
        "5. Jupiter (5.2 AU - largest gas giant)\n"
        "6. Saturn (9.5 AU - ringed gas giant)\n"
        "7. Uranus (19.2 AU - tilted ice giant)\n"
        "8. Neptune (30.1 AU - blue ice giant)"
    )
    return {
        "id": f"ns8_sol_08_{rng.randint(100000, 999999)}",
        "subskill": "08_outer_planets_order_and_characteristics",
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
            "tier_1": "Just Served Us Nachos (Jupiter, Saturn, Uranus, Neptune).",
            "tier_2": "Jupiter is fifth; Neptune is eighth.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["outer_planet_sequence_error"]
    }


def arch_09_mercury_surface_temperature_extremes_craters(rng: random.Random) -> Dict[str, Any]:
    t_day = "430 °C"
    t_night = "-180 °C"
    prompt = (
        f"Mercury is the closest planet to the Sun. By day, surface temperatures reach {t_day}, "
        f"yet by night temperatures drop dramatically to {t_night}.\n\n"
        "Why does Mercury experience such severe temperature swings despite being closest to the Sun?"
    )
    correct = "Mercury has virtually no atmosphere to trap daytime heat or distribute thermal energy across its surface, and it rotates very slowly."
    options = [
        correct,
        "Mercury orbits a black hole that freezes the planet every six hours.",
        "Mercury is made entirely of dry ice that evaporates and refreezes.",
        "The Sun switches off its light whenever Mercury is on its night side."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Role of atmosphere in climate:\n"
        "Atmospheres moderate temperatures by greenhouse trapping and convective circulation.\n"
        "Step 2: Apply to Mercury:\n"
        "Mercury's small gravity cannot retain an atmosphere. Direct solar baking reaches 430 °C, but heat instantly radiates into space at night, plunging the ground to -180 °C."
    )
    return {
        "id": f"ns8_sol_09_{rng.randint(100000, 999999)}",
        "subskill": "09_mercury_surface_temperature_extremes_craters",
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
            "tier_1": "What blanket does Mercury lack to hold in warmth at night?",
            "tier_2": "Mercury has no atmosphere to hold heat.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mercury_atmosphere_assumption"]
    }


def arch_10_venus_runaway_greenhouse_effect_atmosphere(rng: random.Random) -> Dict[str, Any]:
    t_ven = "approximately 465 °C"
    prompt = (
        f"Although Mercury is closer to the Sun, **Venus is the hottest planet in the entire solar system** ({t_ven}), "
        "hot enough to melt lead metal.\n\n"
        "What atmospheric condition causes Venus to be hotter than Mercury?"
    )
    correct = "A runaway greenhouse effect caused by a dense atmosphere composed of 96% carbon dioxide with clouds of corrosive sulfuric acid."
    options = [
        correct,
        "Intense volcanic radioactivity in Venus's iron core that emits boiling plasma.",
        "Venus is physically colliding with the Sun's outer corona every month.",
        "Venus has a surface covered with burning liquid petrol oceans."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Compare distance vs atmosphere:\n"
        "Mercury is closer to the Sun, but has no atmosphere.\n"
        "Step 2: Runaway greenhouse mechanism on Venus:\n"
        "Venus has an atmosphere 90 times denser than Earth's, composed of 96% CO₂. Incoming solar heat is completely trapped, creating a blistering 465 °C surface."
    )
    return {
        "id": f"ns8_sol_10_{rng.randint(100000, 999999)}",
        "subskill": "10_venus_runaway_greenhouse_effect_atmosphere",
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
            "tier_1": "What gas traps heat efficiently? Carbon dioxide.",
            "tier_2": "Runaway greenhouse effect with 96% CO₂ atmosphere.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["closest_planet_must_be_hottest_myth"]
    }


def arch_11_venus_retrograde_rotation_direction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Most planets in our solar system rotate from west to east on their axes. "
        "Venus, however, exhibits unusual **retrograde rotation**.\n\n"
        "What does retrograde rotation mean for an imaginary observer on the surface of Venus?"
    )
    correct = "The planet spins clockwise (east to west), meaning the Sun would appear to rise in the west and set in the east."
    options = [
        correct,
        "The planet spins upside down at the speed of light.",
        "The planet stops spinning entirely and floats motionless.",
        "The planet reverses its orbital direction around the Sun every year."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Normal planetary rotation:\n"
        "Most planets spin counter-clockwise (west to east).\n"
        "Step 2: Venus's retrograde spin:\n"
        "Venus rotates clockwise on its axis (likely inverted by a massive early protoplanetary impact), causing the Sun to rise in the west and set in the east."
    )
    return {
        "id": f"ns8_sol_11_{rng.randint(100000, 999999)}",
        "subskill": "11_venus_retrograde_rotation_direction",
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
            "tier_1": "Retrograde means backward/opposite to normal.",
            "tier_2": "The Sun rises in the west and sets in the east.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["retrograde_rotation_definition_error"]
    }


def arch_12_earth_habitable_characteristics_water_life(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Earth is known as the 'Blue Planet' and is the only known celestial body in the universe "
        "harbouring living organisms.\n\n"
        "Which unique combination of features makes Earth uniquely capable of supporting life?"
    )
    correct = "Abundant liquid surface water, an oxygen-rich atmosphere with protective ozone, a magnetic shield, and a stable habitable-zone orbit."
    options = [
        correct,
        "Zero gravity, freezing methane oceans, and dense carbon monoxide clouds.",
        "Active surface volcanoes covering 100% of the crust and boiling sulfuric rain.",
        "A surface made entirely of pure polished glass with no rock or dust."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify life-sustaining ingredients:\n"
        "- Solvent: Liquid water covering ~71% of surface.\n"
        "- Atmosphere: 78% N₂, 21% O₂, protective O₃ layer.\n"
        "- Shield: Geodynamo magnetic field deflecting solar wind.\n"
        "- Orbit: 1 AU distance in the circumstellar habitable zone."
    )
    return {
        "id": f"ns8_sol_12_{rng.randint(100000, 999999)}",
        "subskill": "12_earth_habitable_characteristics_water_life",
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
            "tier_1": "What allows plants and animals to thrive on Earth?",
            "tier_2": "Liquid water, oxygen atmosphere, magnetic shield, habitable zone.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["planetary_habitability_factors"]
    }


def arch_13_mars_iron_oxide_surface_and_atmosphere(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Mars is famously nicknamed the 'Red Planet'. What chemical compound in Martian surface dust "
        "gives Mars its characteristic reddish rusty color?"
    )
    correct = "Iron oxide (rust), covering the fine regolith and carried by global dust storms."
    options = [
        correct,
        "Red food coloring sprayed by robotic exploration landers.",
        "Copper sulfate crystals reacting with volcanic chlorine.",
        "Organic red tree leaves decomposed over millions of years."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Chemical cause of red coloration:\n"
        "Martian soil is rich in iron minerals that have oxidized (weathered) into iron(III) oxide (Fe₂O₃), common rust.\n"
        "Step 2: Atmospheric suspension:\n"
        "Wind storms kick this fine rusty dust into the thin CO₂ atmosphere, giving the sky a butterscotch-pink hue."
    )
    return {
        "id": f"ns8_sol_13_{rng.randint(100000, 999999)}",
        "subskill": "13_mars_iron_oxide_surface_and_atmosphere",
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
            "tier_1": "What gives rusted metal its reddish-orange color?",
            "tier_2": "Iron oxide (rust).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mars_red_color_origin_error"]
    }


def arch_14_mars_geological_features_olympus_mons(rng: random.Random) -> Dict[str, Any]:
    h_km = "22 kilometres"
    prompt = (
        f"Mars is home to **Olympus Mons**, a colossal shield volcano towering approximately {h_km} high "
        "(nearly three times the height of Mount Everest).\n\n"
        "Why were volcanoes on Mars able to grow so vastly larger than any volcano on Earth?"
    )
    correct = "Mars has much lower surface gravity and stationary tectonic plates, allowing lava to erupt repeatedly in the exact same spot over millions of years."
    options = [
        correct,
        "Mars was created by artificial alien construction equipment.",
        "Volcanoes on Mars are made of lightweight foam rather than solid rock.",
        "Earth has no magma or volcanic activity in its geological history."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Lower gravity:\n"
        "Mars's gravity is 38% of Earth's, allowing towering volcanic structures to support their own weight without collapsing.\n"
        "Step 2: Lack of plate tectonics:\n"
        "On Earth, moving crustal plates drift over hotspots (creating chains like Hawaii). On Mars, stationary crust stayed over magma plumes for eons, building a mega-volcano."
    )
    return {
        "id": f"ns8_sol_14_{rng.randint(100000, 999999)}",
        "subskill": "14_mars_geological_features_olympus_mons",
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
            "tier_1": "Why does a lack of moving plates make one volcano grow massive?",
            "tier_2": "Stationary crust and lower surface gravity.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["martian_volcanism_mechanics"]
    }


def arch_15_mars_search_for_water_and_microbial_life(rng: random.Random) -> Dict[str, Any]:
    probes = ["the Curiosity rover", "the Perseverance rover", "Mars orbital reconnaissance satellites"]
    mission = rng.choice(probes)
    prompt = (
        f"Data sent back by {mission} reveal dry river valleys, ancient lake beds (Jezero crater), "
        "and water ice frozen in polar ice caps and sub-surface permafrost on Mars.\n\n"
        "Why can pure liquid water not exist stably on the open surface of Mars today?"
    )
    correct = "Mars's atmospheric pressure is too low (less than 1% of Earth's); liquid water would immediately boil away or freeze into ice."
    options = [
        correct,
        "Water is chemically banned by toxic Martian carbon monoxide.",
        "The Sun burns ten times brighter on Mars, evaporating all liquids instantly.",
        "The Martian core absorbs all moisture like an electromagnetic sponge."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Phase diagram of water:\n"
        "Liquid water requires adequate ambient atmospheric pressure to remain in liquid phase.\n"
        "Step 2: Mars surface conditions:\n"
        "At ~6 millibars of atmospheric pressure, the boiling point of water is near 0 °C. Liquid water sublimates or boils away almost instantaneously."
    )
    return {
        "id": f"ns8_sol_15_{rng.randint(100000, 999999)}",
        "subskill": "15_mars_search_for_water_and_microbial_life",
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
            "tier_1": "Does Mars have a thick atmosphere or a very thin atmosphere?",
            "tier_2": "Extremely low atmospheric pressure causes water to boil or freeze.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["liquid_water_on_mars_stability"]
    }


def arch_16_asteroid_belt_location_between_mars_and_jupiter(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Between the orbits of Mars and Jupiter lies a vast toroidal region populated by millions "
        "of irregularly shaped rocky remnants known as the **Asteroid Belt**.\n\n"
        "Why did the rocky material in the Asteroid Belt never coalesce into a single large planet?"
    )
    correct = "The colossal gravitational tidal forces of nearby giant planet Jupiter continuously stirred up the rocks, preventing them from clumping together."
    options = [
        correct,
        "The Sun's solar wind melted all the rocks into liquid mercury.",
        "There were only three small pebbles in the entire Asteroid Belt.",
        "The Moon's gravity pulled the asteroids into a flat sheet."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Planetesimal accretion:\n"
        "During early solar system formation, dust clumped into planetesimals.\n"
        "Step 2: Jupiter's gravitational resonance:\n"
        "Jupiter's enormous gravity accelerated asteroid velocities, causing destructive collisions rather than gentle accretion into a planet."
    )
    return {
        "id": f"ns8_sol_16_{rng.randint(100000, 999999)}",
        "subskill": "16_asteroid_belt_location_between_mars_and_jupiter",
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
            "tier_1": "Which massive neighbouring planet disrupted planet formation?",
            "tier_2": "Jupiter's massive gravity prevented accretion.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["asteroid_belt_origin_destroyed_planet_myth"]
    }


def arch_17_asteroid_composition_and_origin_leftovers(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "What are asteroids, and what are they primarily composed of?"
    )
    correct = "Rocky, metallic, and carbonaceous bodies left over from the formation of the solar system 4.6 billion years ago."
    options = [
        correct,
        "Giant balls of burning radioactive gas floating in deep space.",
        "Pieces of wooden trees ejected from alien planets.",
        "Man-made scrap metal discarded from old communication satellites."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Composition of asteroids:\n"
        "Asteroids are categorized into C-type (carbonaceous), S-type (silicate rocky), and M-type (metallic iron-nickel).\n"
        "Step 2: Origin: Pristine primitive building blocks left over from the primordial solar nebula."
    )
    return {
        "id": f"ns8_sol_17_{rng.randint(100000, 999999)}",
        "subskill": "17_asteroid_composition_and_origin_leftovers",
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
            "tier_1": "Are asteroids made of rock/metal or burning gas?",
            "tier_2": "Rocky, metallic, and carbon-rich remnants.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["asteroid_physical_composition_error"]
    }


def arch_18_meteoroid_meteor_meteorite_distinctions(rng: random.Random) -> Dict[str, Any]:
    terms = [
        ("meteoroid", "a small rocky or metallic fragment traveling through outer space"),
        ("meteor", "the luminous streak of light produced when a space fragment burns up in Earth's atmosphere"),
        ("meteorite", "a surviving portion of a space rock that hits Earth's solid ground")
    ]
    term, defn = rng.choice(terms)
    prompt = (
        f"In astronomical terminology, what is the precise term for **{defn}**?"
    )
    correct = term.capitalize()
    options = ["Meteoroid", "Meteor", "Meteorite", "Asteroid"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Distinguish the three related stages:\n"
        f"1. In space: Meteoroid.\n"
        f"2. In atmosphere (streak of light): Meteor.\n"
        f"3. On the ground: Meteorite.\n"
        f"Step 2: Conclusion: {defn} defines a {correct}."
    )
    return {
        "id": f"ns8_sol_18_{rng.randint(100000, 999999)}",
        "subskill": "18_meteoroid_meteor_meteorite_distinctions",
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
            "tier_1": "Space -> air -> ground (meteoroid -> meteor -> meteorite).",
            "tier_2": f"Matches: {correct}.",
            "tier_3": f"Answer is: {correct}"
        },
        "misconception_tags": ["meteoroid_meteor_meteorite_terminology_confusion"]
    }


def arch_19_impact_craters_mechanics_and_energy(rng: random.Random) -> Dict[str, Any]:
    craters = [
        ("the Vredefort Crater in the Free State, South Africa", "the largest and oldest verified meteorite impact crater on Earth (~300 km wide)"),
        ("the Tswaing Crater near Pretoria", "a remarkably well-preserved circular meteorite impact crater with a central salt lake")
    ]
    c_name, c_desc = rng.choice(craters)
    prompt = (
        f"In South African geology, **{c_name}** is {c_desc}.\n\n"
        "Why is an impact crater typically 10 to 20 times wider than the meteorite that created it?"
    )
    correct = "The meteorite arrives at hypervelocity (15-70 km/s), causing kinetic energy to explode like nuclear dynamite, vaporizing rock and excavating a massive crater."
    options = [
        correct,
        "The meteorite slowly dissolves in groundwater like a giant bath bomb.",
        "Meteorites expand and inflate like balloons after landing on Earth.",
        "Wind blows dirt around the meteorite over millions of years."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Kinetic energy formula:\n"
        "KE = 1/2 m v².\n"
        "Step 2: Hypervelocity shockwave:\n"
        "Because velocity v is extreme (~20 km/s), the kinetic energy released upon impact causes an instantaneous catastrophic explosion that excavates a crater far larger than the impactor."
    )
    return {
        "id": f"ns8_sol_19_{rng.randint(100000, 999999)}",
        "subskill": "19_impact_craters_mechanics_and_energy",
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
            "tier_1": "Does a meteorite hit at high speed? Think kinetic energy explosion.",
            "tier_2": "Hypervelocity explosive shockwaves blast open a huge crater.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["crater_size_equals_meteorite_size_fallacy"]
    }


def arch_20_jupiter_size_mass_and_fast_rotation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Jupiter is by far the largest planet in our solar system, with a mass more than double "
        "that of all other seven planets combined.\n\n"
        "Remarkably, how long does it take for this colossal gas giant to complete one rotation on its axis?"
    )
    correct = "Approximately 9 hours and 55 minutes (the shortest day of any planet in the solar system)."
    options = [
        correct,
        "Exactly 365.25 days.",
        "Approximately 240 days.",
        "Exactly 100 hours."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Jupiter's physical scale:\n"
        "11 times Earth's diameter, 318 times Earth's mass.\n"
        "Step 2: Rapid rotation:\n"
        "Despite its colossal girth, Jupiter spins faster than any other planet, rotating once every 9.9 hours. This rapid spin flattens the planet noticeably at its poles (oblateness)."
    )
    return {
        "id": f"ns8_sol_20_{rng.randint(100000, 999999)}",
        "subskill": "20_jupiter_size_mass_and_fast_rotation",
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
            "tier_1": "Does Jupiter spin faster or slower than Earth?",
            "tier_2": "Jupiter has the fastest rotation in the solar system (~10 hours).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["large_planet_rotates_slowly_fallacy"]
    }


def arch_21_jupiter_great_red_spot_atmospheric_storm(rng: random.Random) -> Dict[str, Any]:
    diam = "larger than planet Earth"
    prompt = (
        f"Jupiter's atmosphere displays a famous feature known as the **Great Red Spot**, "
        f"which is {diam} and has been observed continuously for over 300 years.\n\n"
        "What is the physical nature of the Great Red Spot?"
    )
    correct = "A giant anticyclonic high-pressure storm with swirling winds exceeding 400 km/h."
    options = [
        correct,
        "A solid red continent of copper rising out of an ocean.",
        "An active nuclear crater caused by an exploding moon.",
        "A gigantic lake of red strawberry syrup."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify Great Red Spot:\n"
        "It is not a solid feature, because Jupiter has no solid surface.\n"
        "Step 2: Meteorological nature:\n"
        "It is a persistent anticyclonic atmospheric storm rotating counter-clockwise, driven by internal heat and atmospheric shearing jets."
    )
    return {
        "id": f"ns8_sol_21_{rng.randint(100000, 999999)}",
        "subskill": "21_jupiter_great_red_spot_atmospheric_storm",
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
            "tier_1": "Is Jupiter a rocky planet or a gas giant?",
            "tier_2": "A giant swirling storm in a gaseous atmosphere.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["great_red_spot_solid_surface_error"]
    }


def arch_22_jupiter_galilean_moons_io_europa_ganymede_callisto(rng: random.Random) -> Dict[str, Any]:
    moons = [
        ("Io", "the most volcanically active body in the solar system, with hundreds of erupting sulfur volcanoes"),
        ("Europa", "covered by an icy shell concealing a vast global liquid water ocean that may harbor life"),
        ("Ganymede", "the largest moon in the solar system, even larger than the planet Mercury, with its own magnetic field")
    ]
    moon, feature = rng.choice(moons)
    prompt = (
        f"Among Jupiter's four Galilean moons, **{moon}** is famous for being {feature}.\n\n"
        "What powers the intense geological activity and liquid oceans inside these icy outer moons?"
    )
    correct = "Tidal flexing: Gravitational tidal tugs from massive Jupiter and neighboring moons constantly knead and heat their interiors."
    options = [
        correct,
        "Nuclear power stations built by ancient civilizations.",
        "Heat radiated by nearby passing comets.",
        "Direct solar burning of their surface snow."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The puzzle of outer solar system heat:\n"
        "Jupiter is far from the Sun; sunlight is weak.\n"
        "Step 2: Tidal heating mechanism:\n"
        "Orbital resonance causes continuous gravitational stretching and squeezing (tidal friction), generating massive internal geothermal heat."
    )
    return {
        "id": f"ns8_sol_22_{rng.randint(100000, 999999)}",
        "subskill": "22_jupiter_galilean_moons_io_europa_ganymede_callisto",
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
            "tier_1": "Think about gravitational stretching and squeezing.",
            "tier_2": "Tidal flexing from Jupiter's massive gravity.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["tidal_heating_mechanism_confusion"]
    }


def arch_23_saturn_ring_system_composition_ice_rock(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Saturn boasts the most spectacular and extensive ring system in the solar system, "
        "spanning up to 280 000 km across but only tens of metres thick.\n\n"
        "What are Saturn's rings primarily made of?"
    )
    correct = "Billions of individual pieces of water ice, rock, and dust, ranging in size from tiny grains to house-sized boulders."
    options = [
        correct,
        "A single solid sheet of polished sheet metal spinning around the equator.",
        "Dense clouds of toxic glowing neon gas.",
        "Solid glass rings created by ancient volcanic eruptions."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Physical state of planetary rings:\n"
        "A solid ring would shatter due to differential gravitational tidal forces.\n"
        "Step 2: Composition:\n"
        "Saturn's rings are over 99% pure water ice fragments in independent Keplerian orbits around the planet."
    )
    r_sat = rng.choice([26, 28, 30])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 160" width="100%" height="130"><ellipse cx="150" cy="80" rx="100" ry="25" fill="none" stroke="#fef08a" stroke-width="6"/><circle cx="150" cy="80" r="{r_sat}" fill="#eab308"/><ellipse cx="150" cy="80" rx="100" ry="25" fill="none" stroke="#fde047" stroke-width="2" stroke-dasharray="2"/><text x="150" y="130" text-anchor="middle" font-size="10" fill="#854d0e">Saturn & Ice Ring System</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns8_sol_23_{rng.randint(100000, 999999)}",
        "subskill": "23_saturn_ring_system_composition_ice_rock",
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
        "diagram_spec": spec,
        "hints": {
            "tier_1": "Are the rings one solid sheet or millions of ice chunks?",
            "tier_2": "Billions of water ice particles and rocky debris.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["saturn_rings_solid_plate_fallacy"]
    }


def arch_24_saturn_low_average_density_buoyancy(rng: random.Random) -> Dict[str, Any]:
    density_val = "0.687 g/cm³"
    prompt = (
        f"Saturn is the second-largest planet in the solar system, yet its average density is only {density_val} "
        "(less than the density of liquid water, which is 1.0 g/cm³).\n\n"
        "What popular scientific thought-experiment illustrates this remarkable property?"
    )
    correct = "If there were a bathtub of water large enough to hold it, Saturn would float."
    options = [
        correct,
        "Saturn would instantly sink to the bottom like an iron anvil.",
        "Saturn would dissolve into saltwater in five seconds.",
        "Saturn would cause water to boil into burning plasma."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Principle of buoyancy (Archimedes' Principle):\n"
        "Objects with an average density less than water (< 1.0 g/cm³) float.\n"
        "Step 2: Apply to Saturn:\n"
        "Composed mostly of light hydrogen and helium gas, Saturn's density (0.69 g/cm³) is less than water, meaning it would float."
    )
    return {
        "id": f"ns8_sol_24_{rng.randint(100000, 999999)}",
        "subskill": "24_saturn_low_average_density_buoyancy",
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
            "tier_1": "What happens to things less dense than water?",
            "tier_2": "They float on water.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["saturn_density_buoyancy_fallacy"]
    }


def arch_25_saturn_moon_titan_nitrogen_atmosphere_methane(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Saturn's largest moon, **Titan**, is the only moon in the solar system with a dense, substantial atmosphere.\n\n"
        "What extraordinary surface features did the Cassini-Huygens probe discover on Titan?"
    )
    correct = "Lakes, rivers, and rain of liquid methane and ethane, cycling in a cryogenic hydrological cycle at -179 °C."
    options = [
        correct,
        "Cities of alien humanoids swimming in hot tropical water lagoons.",
        "Rivers of boiling molten iron flowing into sulfur volcanoes.",
        "Completely dry flat rock with zero liquids or clouds."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Titan's atmosphere:\n"
        "95% nitrogen with orange hydrocarbon smog.\n"
        "Step 2: Hydrocarbon cycle:\n"
        "At -179 °C, methane exists at its triple point. Titan has active methane rainfall, rivers, and lakes (Kraken Mare), mirroring Earth's water cycle at cryogenic temperatures."
    )
    return {
        "id": f"ns8_sol_25_{rng.randint(100000, 999999)}",
        "subskill": "25_saturn_moon_titan_nitrogen_atmosphere_methane",
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
            "tier_1": "Does Titan have lakes of water or lakes of liquid methane?",
            "tier_2": "Lakes and rivers of liquid hydrocarbons (methane/ethane).",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["titan_surface_liquid_composition"]
    }


BUILDERS_01_25 = {
    "01_sun_mass_and_gravitational_dominance": arch_01_sun_mass_and_gravitational_dominance,
    "02_sun_structure_photosphere_and_corona": arch_02_sun_structure_photosphere_and_corona,
    "03_sunspots_magnetic_activity_and_cycle": arch_03_sunspots_magnetic_activity_and_cycle,
    "04_safe_solar_observation_pinhole_projection": arch_04_safe_solar_observation_pinhole_projection,
    "05_solar_system_scale_and_astronomical_units": arch_05_solar_system_scale_and_astronomical_units,
    "06_terrestrial_vs_gas_giant_planets_contrast": arch_06_terrestrial_vs_gas_giant_planets_contrast,
    "07_inner_planets_order_and_characteristics": arch_07_inner_planets_order_and_characteristics,
    "08_outer_planets_order_and_characteristics": arch_08_outer_planets_order_and_characteristics,
    "09_mercury_surface_temperature_extremes_craters": arch_09_mercury_surface_temperature_extremes_craters,
    "10_venus_runaway_greenhouse_effect_atmosphere": arch_10_venus_runaway_greenhouse_effect_atmosphere,
    "11_venus_retrograde_rotation_direction": arch_11_venus_retrograde_rotation_direction,
    "12_earth_habitable_characteristics_water_life": arch_12_earth_habitable_characteristics_water_life,
    "13_mars_iron_oxide_surface_and_atmosphere": arch_13_mars_iron_oxide_surface_and_atmosphere,
    "14_mars_geological_features_olympus_mons": arch_14_mars_geological_features_olympus_mons,
    "15_mars_search_for_water_and_microbial_life": arch_15_mars_search_for_water_and_microbial_life,
    "16_asteroid_belt_location_between_mars_and_jupiter": arch_16_asteroid_belt_location_between_mars_and_jupiter,
    "17_asteroid_composition_and_origin_leftovers": arch_17_asteroid_composition_and_origin_leftovers,
    "18_meteoroid_meteor_meteorite_distinctions": arch_18_meteoroid_meteor_meteorite_distinctions,
    "19_impact_craters_mechanics_and_energy": arch_19_impact_craters_mechanics_and_energy,
    "20_jupiter_size_mass_and_fast_rotation": arch_20_jupiter_size_mass_and_fast_rotation,
    "21_jupiter_great_red_spot_atmospheric_storm": arch_21_jupiter_great_red_spot_atmospheric_storm,
    "22_jupiter_galilean_moons_io_europa_ganymede_callisto": arch_22_jupiter_galilean_moons_io_europa_ganymede_callisto,
    "23_saturn_ring_system_composition_ice_rock": arch_23_saturn_ring_system_composition_ice_rock,
    "24_saturn_low_average_density_buoyancy": arch_24_saturn_low_average_density_buoyancy,
    "25_saturn_moon_titan_nitrogen_atmosphere_methane": arch_25_saturn_moon_titan_nitrogen_atmosphere_methane,
}

