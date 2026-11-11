"""Grade 8 Natural Sciences - The Solar System: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr8/Term 4/01. The Solar System.md
Focus:
Uranus (axial tilt, ice giant), Neptune (winds, Triton), Kuiper Belt, Dwarf planets (IAU definition, Pluto, Ceres, Eris),
Oort cloud, Comets (anatomy, tails, solar wind, Halley's comet), Habitable zone (Goldilocks, liquid water, atmosphere,
greenhouse effect, magnetosphere, ozone), Planetary trends (Keplerian periods, inverse-square temperatures, gravity),
Exploration probes, Exoplanets, and Diagnostic Autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_uranus_extreme_axial_tilt_and_seasons(rng: random.Random) -> Dict[str, Any]:
    tilt = rng.choice(["97,8°", "approximately 98°", "about 98 degrees"])
    prompt = (
        f"The planet Uranus possesses an extreme axial tilt of {tilt}, meaning its axis of rotation is tilted almost parallel to its orbital plane.\n\n"
        "What extreme seasonal condition does this unique orientation create on Uranus?"
    )
    correct = "Each pole experiences 42 years of continuous, unbroken daylight in summer followed by 42 years of continuous darkness in winter."
    options = [
        correct,
        "Uranus has zero seasonal variation because its axis points straight upright at 0°.",
        "Both poles receive equal sunlight every 24 hours just like Earth's equator.",
        "Uranus instantly freezes solid into metallic hydrogen every afternoon."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Axial tilt and seasons:\n"
        "Uranus's orbital period is 84 Earth years. Because its tilt is ~98°, its rotational axis lies almost directly in the orbital plane.\n"
        "Step 2: Polar illumination:\n"
        "For half of its orbit (42 years), one pole points almost directly at the Sun enjoying continuous summer sunlight, while the opposite pole faces away into 42 years of pitch-black winter."
    )
    return {
        "id": f"ns8_sol_26_{rng.randint(100000, 999999)}",
        "subskill": "26_uranus_extreme_axial_tilt_and_seasons",
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
            "tier_1": "Uranus rotates almost on its side.",
            "tier_2": "With an 84-year orbit, half the orbit is 42 years of sunlight or darkness at the poles.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["uranus_axial_tilt_seasonality"]
    }


def arch_27_uranus_ice_giant_composition_and_methane(rng: random.Random) -> Dict[str, Any]:
    gas = rng.choice(["methane gas", "atmospheric methane (CH4)"])
    prompt = (
        f"Astronomers classify Uranus and Neptune as 'ice giants' rather than gas giants. In Uranus's upper atmosphere, {gas} is abundant.\n\n"
        "Why does this gas cause Uranus to appear distinctly cyan (pale blue-green)?"
    )
    correct = "Methane absorbs red light wavelengths from incoming sunlight and scatters the remaining blue and green wavelengths back into space."
    options = [
        correct,
        "Methane emits bright green ultraviolet lasers from underground volcanic fissures.",
        "Uranus is coated in an ocean of blue liquid copper sulfate.",
        "Methane absorbs blue light completely, reflecting only red and infrared light."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric absorption:\n"
        "Methane gas in the upper atmosphere strongly absorbs photons in the red and infrared spectrum.\n"
        "Step 2: Scattered light:\n"
        "The unabsorbed blue and green wavelengths are scattered and reflected outward, giving Uranus its characteristic pale cyan appearance."
    )
    return {
        "id": f"ns8_sol_27_{rng.randint(100000, 999999)}",
        "subskill": "27_uranus_ice_giant_composition_and_methane",
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
            "tier_1": "What color wavelength does methane absorb?",
            "tier_2": "It absorbs red light and reflects blue-green light.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ice_giant_color_methane_absorption"]
    }


def arch_28_neptune_supersonic_winds_and_great_dark_spot(rng: random.Random) -> Dict[str, Any]:
    wind_speed = rng.choice(["2 000 km/h", "over 2 100 km/h", "nearly supersonic speeds exceeding 2 000 km/h"])
    prompt = (
        f"Despite being located over 4,5 billion kilometers from the Sun where solar heating is minimal, Neptune possesses the most violent winds in the solar system, reaching {wind_speed}.\n\n"
        "What famous colossal storm system was observed on Neptune by the Voyager 2 spacecraft in 1989?"
    )
    correct = "The Great Dark Spot, an Earth-sized anticyclonic storm system in Neptune's southern atmosphere."
    options = [
        correct,
        "The Great White Eye, a permanent continent of frozen carbon dioxide.",
        "The Caloris Basin, an ancient volcanic crater filled with sulfur.",
        "The Valles Marineris canyon system carved by surface rivers."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Neptune's violent atmosphere:\n"
        "Neptune radiates 2,6 times more internal heat than it receives from the Sun, driving extreme supersonic jet streams.\n"
        "Step 2: Voyager 2 observations:\n"
        "In 1989, Voyager 2 photographed the Great Dark Spot, a dynamic Earth-sized atmospheric storm comparable to Jupiter's Great Red Spot."
    )
    return {
        "id": f"ns8_sol_28_{rng.randint(100000, 999999)}",
        "subskill": "28_neptune_supersonic_winds_and_great_dark_spot",
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
            "tier_1": "Think of the giant dark storm observed by Voyager 2.",
            "tier_2": "It is named the Great Dark Spot.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["neptune_atmospheric_dynamics_storm"]
    }


def arch_29_neptune_moon_triton_retrograde_orbit_geysers(rng: random.Random) -> Dict[str, Any]:
    substance = rng.choice(["nitrogen gas and dark hydrocarbon dust", "liquid nitrogen geysers"])
    prompt = (
        f"Neptune's largest moon, **Triton**, is unique among all large moons in the solar system because it orbits Neptune in a **retrograde direction** (opposite to the planet's rotation). In addition, Voyager 2 detected active cryovolcanic plumes spewing {substance}.\n\n"
        "What do planetary scientists conclude about the origin of Triton from its retrograde orbit?"
    )
    correct = "Triton did not form in place around Neptune; it was an independent icy dwarf planet gravitationally captured from the Kuiper Belt."
    options = [
        correct,
        "Triton was blasted off the surface of Earth during the dinosaur extinction.",
        "Triton was ejected from the center of the Sun during a coronal mass ejection.",
        "Triton formed identically to Earth's Moon via a direct collision between Mars and Jupiter."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Retrograde orbit mechanics:\n"
        "Bodies that condense from a planet's primordial accretion disk orbit in a prograde direction. A retrograde orbit is a definitive signature of gravitational capture.\n"
        "Step 2: Kuiper Belt origin:\n"
        "Triton's icy composition, density, and retrograde orbit indicate it was captured from the Kuiper Belt, explaining its active cryovolcanism powered by tidal flexing."
    )
    return {
        "id": f"ns8_sol_29_{rng.randint(100000, 999999)}",
        "subskill": "29_neptune_moon_triton_retrograde_orbit_geysers",
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
            "tier_1": "Why would a moon orbit backward around its host planet?",
            "tier_2": "It was captured from elsewhere (the Kuiper Belt).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["triton_retrograde_capture_origin"]
    }


def arch_30_kuiper_belt_location_and_icy_composition(rng: random.Random) -> Dict[str, Any]:
    dist = rng.choice(["30 to 50 AU", "roughly 30 to 55 AU"])
    prompt = (
        f"Beyond the orbit of Neptune lies a vast, doughnut-shaped region of the solar system spanning approximately {dist} from the Sun, known as the **Kuiper Belt**.\n\n"
        "What is the predominant composition of the millions of celestial bodies inhabiting the Kuiper Belt?"
    )
    correct = "Frozen volatile ices (water ice, methane, ammonia, and nitrogen) mixed with silicate rock."
    options = [
        correct,
        "Pure molten iron-nickel magma and liquid lava oceans.",
        "Dense clouds of gaseous helium under immense thermonuclear pressure.",
        "Thick layers of organic soil, grass, and liquid salt water."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Kuiper Belt location:\n"
        "Extends from Neptune's orbit (30 AU) outwards to ~50 AU.\n"
        "Step 2: Composition:\n"
        "At temperatures below 40 K (-233 °C), volatiles like water, methane, and ammonia freeze solid, forming icy planetesimals, comets, and dwarf planets."
    )
    return {
        "id": f"ns8_sol_30_{rng.randint(100000, 999999)}",
        "subskill": "30_kuiper_belt_location_and_icy_composition",
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
            "tier_1": "In the deep freeze beyond Neptune, what do volatiles like water and methane form?",
            "tier_2": "They form frozen volatile ices.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["kuiper_belt_icy_composition"]
    }


def arch_31_pluto_dwarf_planet_reclassification_criteria(rng: random.Random) -> Dict[str, Any]:
    year = rng.choice(["In August 2006", "In 2006"])
    prompt = (
        f"{year}, the International Astronomical Union (IAU) reclassified Pluto from a major planet to a **dwarf planet**.\n\n"
        "Which of the three official planetary criteria did Pluto fail to satisfy?"
    )
    correct = "Pluto has not cleared the neighborhood around its orbit; its mass is dwarfed by the collective mass of other Kuiper Belt objects sharing its zone."
    options = [
        correct,
        "Pluto does not orbit the Sun directly, but orbits Neptune as a captured moon.",
        "Pluto is completely flat and disc-shaped rather than rounded by gravity.",
        "Pluto does not possess any moons or natural satellites in its system."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Review IAU planet criteria:\n"
        "1. Must orbit the Sun directly (Pluto satisfies).\n"
        "2. Must have sufficient mass for hydrostatic equilibrium/spherical shape (Pluto satisfies).\n"
        "3. Must have cleared its orbital neighborhood.\n"
        "Step 2: Pluto's failure:\n"
        "Pluto shares its orbital zone with thousands of Kuiper Belt objects and its mass is only a tiny fraction of the surrounding debris. Thus, it is classified as a dwarf planet."
    )
    return {
        "id": f"ns8_sol_31_{rng.randint(100000, 999999)}",
        "subskill": "31_pluto_dwarf_planet_reclassification_criteria",
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
            "tier_1": "Did Pluto clear its orbital pathway of other objects?",
            "tier_2": "No, it shares its neighborhood with many Kuiper Belt objects.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["pluto_reclassification_cleared_neighborhood"]
    }


def arch_32_iau_planet_definition_three_conditions(rng: random.Random) -> Dict[str, Any]:
    items = [
        ("Criterion 1", "It must orbit around the Sun directly (not be a satellite of another planet)."),
        ("Criterion 2", "It must possess sufficient mass so that its own gravity produces a nearly round, spherical shape (hydrostatic equilibrium)."),
        ("Criterion 3", "It must have cleared the neighborhood around its orbit of other significant debris.")
    ]
    crit_num, crit_text = rng.choice(items)
    prompt = (
        "According to the official definition adopted by the International Astronomical Union (IAU), a celestial body in our solar system is a full planet only if it meets three distinct conditions.\n\n"
        f"Which statement accurately describes **{crit_num}**?"
    )
    correct = crit_text
    options = [
        correct,
        "It must possess a breathable nitrogen-oxygen atmosphere and liquid surface oceans.",
        "It must possess at least two large moons to stabilize its rotational axial tilt.",
        "It must possess an active magnetic field strong enough to deflect the solar wind."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The 3 IAU planetary criteria:\n"
        "1. Orbits the Sun directly.\n"
        "2. Hydrostatic equilibrium (nearly round/spherical shape).\n"
        "3. Has gravitationally cleared its orbital neighborhood.\n"
        f"Step 2: Specific criterion:\n"
        f"{crit_num} is: {crit_text}"
    )
    return {
        "id": f"ns8_sol_32_{rng.randint(100000, 999999)}",
        "subskill": "32_iau_planet_definition_three_conditions",
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
            "tier_1": "Recall the official IAU planetary criteria.",
            "tier_2": "The 3 conditions involve orbiting the Sun, spherical shape, and clearing the orbital path.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["iau_planet_definition_criteria"]
    }


def arch_33_dwarf_planets_examples_ceres_erisa_makemake(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Ceres", "the asteroid belt between Mars and Jupiter", "the only dwarf planet located in the inner solar system's asteroid belt"),
        ("Eris", "the distant scattered disc beyond the Kuiper Belt", "the massive icy dwarf planet whose discovery precipitated the 2006 IAU planet redefinition"),
        ("Makemake", "the Kuiper Belt", "an extremely cold, bright Kuiper Belt dwarf planet coated in methane and ethane ice")
    ]
    name, loc, desc = rng.choice(cases)
    prompt = (
        f"The recognized dwarf planet **{name}** is a notable member of our solar system.\n\n"
        f"Where is **{name}** located, and what is its primary astronomical significance?"
    )
    correct = f"Located in {loc}; it is {desc}."
    options = [
        correct,
        f"Located in orbit around Mercury; it is the hottest volcanic moon in the solar system.",
        f"Located inside the Sun's core; it provides fuel for thermonuclear fusion reactions.",
        f"Located in Earth's upper stratosphere; it reflects sunlight to create the auroras."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify dwarf planet location and facts:\n"
        f"{name} is located in {loc}.\n"
        f"Step 2: Significance:\n"
        f"It is {desc}."
    )
    return {
        "id": f"ns8_sol_33_{rng.randint(100000, 999999)}",
        "subskill": "33_dwarf_planets_examples_ceres_erisa_makemake",
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
            "tier_1": f"Where does {name} orbit?",
            "tier_2": f"Consider {loc}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["dwarf_planets_locations_and_examples"]
    }


def arch_34_oort_cloud_spherical_reservoir_long_period_comets(rng: random.Random) -> Dict[str, Any]:
    au_range = rng.choice(["2 000 to 100 000 AU", "up to 50 000 or 100 000 AU"])
    prompt = (
        f"At the outermost boundary of the Sun's gravitational influence lies the **Oort Cloud**, a theoretical spherical shell extending {au_range} from the Sun.\n\n"
        "What major category of celestial objects originates from the Oort Cloud?"
    )
    correct = "Long-period comets with orbital periods ranging from thousands to millions of years, arriving from any inclination."
    options = [
        correct,
        "Short-period comets like Halley's Comet that stay strictly in the ecliptic plane.",
        "Dense iron-nickel asteroids that form the inner terrestrial planets.",
        "High-energy solar flares and coronal mass ejections."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Oort Cloud structure:\n"
        "Unlike the disc-shaped Kuiper Belt, the Oort Cloud is a massive spherical reservoir of icy planetesimals.\n"
        "Step 2: Origin of long-period comets:\n"
        "Gravitational nudges from passing stars perturb icy bodies in the Oort Cloud, sending them falling toward the inner solar system as long-period comets with orbits of 10 000+ years and random orbital inclinations."
    )
    return {
        "id": f"ns8_sol_34_{rng.randint(100000, 999999)}",
        "subskill": "34_oort_cloud_spherical_reservoir_long_period_comets",
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
            "tier_1": "Is the Oort Cloud the source of short-period or long-period comets?",
            "tier_2": "Long-period comets with orbital periods of thousands to millions of years.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["oort_cloud_long_period_comet_origin"]
    }


def arch_35_comet_anatomy_nucleus_coma_and_tails(rng: random.Random) -> Dict[str, Any]:
    part, defn = rng.choice([
        ("nucleus", "the solid, central 'dirty snowball' core composed of rock, dust, and frozen water/gases (a few km wide)"),
        ("coma", "the glowing, spherical envelope of gas and dust surrounding the nucleus, formed when solar heat sublimates ice"),
        ("tail", "the extended streams of illuminated gas and dust stretching millions of kilometers away from the Sun")
    ])
    prompt = (
        "As a comet approaches the inner solar system, solar radiation transforms its structure.\n\n"
        f"Which statement accurately describes the comet's **{part}**?"
    )
    correct = defn
    options = [
        correct,
        "A rigid iron shell that shields the interior against thermonuclear decay.",
        "A subterranean river of liquid mercury flowing between impact craters.",
        "An artificial solar sail deployed by human spacecraft to steer the comet."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Comet anatomy:\n"
        "A comet consists of a central solid nucleus, an expanding gaseous coma, and elongated tails.\n"
        f"Step 2: Define {part}:\n"
        f"The {part} is {defn}."
    )
    return {
        "id": f"ns8_sol_35_{rng.randint(100000, 999999)}",
        "subskill": "35_comet_anatomy_nucleus_coma_and_tails",
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
            "tier_1": f"What is the physical structure of a comet's {part}?",
            "tier_2": f"Review the anatomy: {defn[:40]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["comet_anatomy_parts_definition"]
    }


def arch_36_comet_ion_tail_vs_dust_tail_physics(rng: random.Random) -> Dict[str, Any]:
    tail_type = rng.choice(["ion (gas) tail", "dust tail"])
    if tail_type == "ion (gas) tail":
        correct = "Composed of ionized gases; straight, glowing bluish, driven directly outward by the solar wind."
        distractor1 = "Composed of heavy dust grains; gently curved, yellowish-white, driven by solar radiation pressure."
    else:
        correct = "Composed of microscopic dust particles; gently curved along the comet's orbital path, driven by solar radiation pressure."
        distractor1 = "Composed of ionized gases; straight, glowing bluish, driven directly outward by the solar wind."
    prompt = (
        f"When observing an active comet, two distinct tails are clearly visible: an ion (gas) tail and a dust tail.\n\n"
        f"What physical characteristics and forces govern the **{tail_type}**?"
    )
    options = [
        correct,
        distractor1,
        "Composed of molten iron dripping downwards toward the Earth's magnetic north pole.",
        "Composed of pure nitrogen snow frozen into rigid crystalline sheets by cosmic rays."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Ion tail physics:\n"
        "Composed of ionized gases (CO+, N2+). Interacts directly with the solar wind's magnetic field, pushing it straight outward and glowing blue due to fluorescence.\n"
        "Step 2: Dust tail physics:\n"
        "Composed of heavier dust grains pushed by solar radiation pressure (photons). Because dust particles carry momentum, the dust tail curves along the comet's orbital path."
    )
    return {
        "id": f"ns8_sol_36_{rng.randint(100000, 999999)}",
        "subskill": "36_comet_ion_tail_vs_dust_tail_physics",
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
            "tier_1": f"Is the {tail_type} pushed by solar wind (straight) or radiation pressure (curved)?",
            "tier_2": "Ion tail is straight and blue; dust tail is curved and white/yellow.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["comet_ion_tail_vs_dust_tail_physics"]
    }


def arch_37_comet_tail_orientation_away_from_sun(rng: random.Random) -> Dict[str, Any]:
    sun_x = rng.choice([60, 70, 80])
    comet_x = 280
    stroke_color = rng.choice(["#F59E0B", "#D97706", "#B45309"])
    svg = (
        f'<svg viewBox="0 0 500 240" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="500" height="240" fill="#0B132B"/>'
        f'<circle cx="{sun_x}" cy="120" r="35" fill="{stroke_color}"/>'
        f'<text x="{sun_x}" y="125" fill="#FFFFFF" font-size="12" text-anchor="middle" font-weight="bold">SUN</text>'
        f'<path d="M 120 40 Q 280 120 460 160" fill="none" stroke="#60A5FA" stroke-dasharray="4,4" stroke-width="2"/>'
        f'<circle cx="{comet_x}" cy="120" r="10" fill="#E2E8F0"/>'
        f'<text x="{comet_x}" y="105" fill="#E2E8F0" font-size="11" text-anchor="middle">Comet Nucleus</text>'
        f'<line x1="{comet_x}" y1="120" x2="450" y2="120" stroke="#38BDF8" stroke-width="4" stroke-linecap="round"/>'
        f'<text x="365" y="140" fill="#38BDF8" font-size="11" text-anchor="middle">Comet Tail</text>'
        f'</svg>'
    )
    prompt = (
        "As a comet orbits the Sun, its tails do NOT trail behind its direction of motion like exhaust behind an airplane.\n\n"
        "What fundamental rule dictates the orientation of a comet's tails at all points in its orbit?"
    )
    correct = "A comet's tails always point directly away from the Sun, driven outward by solar wind and solar radiation pressure, even when the comet is traveling away from the Sun."
    options = [
        correct,
        "A comet's tails always point directly toward the Sun, pulled inward by gravitational attraction.",
        "A comet's tails always trail backwards strictly along its path of motion through friction with empty space.",
        "A comet's tails point toward the North Star regardless of the Sun's position."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Driver of comet tails:\n"
        "The tails are formed by solar radiation pressure and the high-speed solar wind streaming radially outward from the Sun.\n"
        "Step 2: Tail orientation:\n"
        "Because the solar wind flows outward from the Sun, comet tails always point away from the Sun. When moving away from the Sun, a comet actually travels tail-first!"
    )
    return {
        "id": f"ns8_sol_37_{rng.randint(100000, 999999)}",
        "subskill": "37_comet_tail_orientation_away_from_sun",
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
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Do comet tails follow behind the comet like smoke behind a car?",
            "tier_2": "No, solar wind blows them outward away from the Sun.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["comet_tail_orientation_solar_wind_direction"]
    }


def arch_38_halley_comet_periodic_orbit_76_years(rng: random.Random) -> Dict[str, Any]:
    years = rng.choice(["75 to 76 years", "approximately 76 years"])
    prompt = (
        f"**Halley's Comet** is the most famous periodic comet in recorded human history, returning to view from Earth every {years} (last seen in 1986, next expected in 2061).\n\n"
        "Why was English astronomer Edmond Halley's prediction of its return in 1758 so historically monumental for physics?"
    )
    correct = "It proved that comets are bound members of the solar system governed by Isaac Newton's laws of universal gravitation, rather than random atmospheric omens."
    options = [
        correct,
        "It proved that the Earth is stationary at the exact center of the universe.",
        "It proved that comets are made of solid gold that can be mined with telescopes.",
        "It proved that stars are only a few hundred kilometers away from Earth."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Historical context:\n"
        "Prior to Edmond Halley, comets were widely viewed as unpredictable, supernatural omens in Earth's atmosphere.\n"
        "Step 2: Application of Newtonian mechanics:\n"
        "Halley applied Newton's laws of gravitation to historical comet sightings (1531, 1607, 1682) and predicted its return in 1758, confirming that gravitational laws govern orbital motion throughout the solar system."
    )
    return {
        "id": f"ns8_sol_38_{rng.randint(100000, 999999)}",
        "subskill": "38_halley_comet_periodic_orbit_76_years",
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
            "tier_1": "What law of physics did Halley use to calculate the comet's return?",
            "tier_2": "Newton's laws of universal gravitation.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["halley_comet_periodic_orbit_physics"]
    }


def arch_39_circumstellar_habitable_zone_goldilocks_concept(rng: random.Random) -> Dict[str, Any]:
    star_type = rng.choice(["our Sun (a yellow G-type star)", "a solar-type star"])
    prompt = (
        f"In astronomy, the circumstellar **habitable zone** (often called the 'Goldilocks Zone') around {star_type} is of prime importance in the search for extraterrestrial life.\n\n"
        "What defines the precise physical boundaries of this habitable zone?"
    )
    correct = "The range of orbital distances where radiant solar energy allows planetary surface temperatures suitable for water to remain in a liquid state."
    options = [
        correct,
        "The zone where planetary gravity is exactly 9,8 m/s² regardless of planetary mass.",
        "The region where spaceships can fly without needing rocket fuel.",
        "The region where stars emit zero ultraviolet or infrared radiation."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Habitable zone definition:\n"
        "Neither too hot (water boils into steam) nor too cold (water freezes into ice).\n"
        "Step 2: Physical condition:\n"
        "The habitable zone is strictly defined by the range of distances where stellar flux sustains surface temperatures that permit stable liquid water under atmospheric pressure."
    )
    return {
        "id": f"ns8_sol_39_{rng.randint(100000, 999999)}",
        "subskill": "39_circumstellar_habitable_zone_goldilocks_concept",
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
            "tier_1": "What physical substance is the Goldilocks zone based upon?",
            "tier_2": "Liquid water on a planet's surface.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["habitable_zone_liquid_water_criterion"]
    }


def arch_40_liquid_water_as_essential_solvent_for_life(rng: random.Random) -> Dict[str, Any]:
    property_name = rng.choice(["universal solvent capability", "high specific heat capacity"])
    if property_name == "universal solvent capability":
        desc = "its ability to dissolve a vast range of biochemical nutrients and facilitate cellular metabolic chemical reactions"
    else:
        desc = "its ability to absorb and release huge amounts of thermal energy with minimal temperature change, stabilizing global planetary climates"
    prompt = (
        "Liquid water is widely regarded by biologists and astrobiologists as an indispensable prerequisite for living organisms.\n\n"
        f"How does water's **{property_name}** specifically support life on Earth?"
    )
    correct = desc
    options = [
        correct,
        "by creating radioactive decay products that power photosynthetic chlorophyll cells",
        "by eliminating planetary gravity so organisms can float weightlessly across continents",
        "by blocking all visible sunlight so the ground remains pitch black and cool"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Importance of {property_name}:\n"
        f"Water's chemical structure (polarity and hydrogen bonding) gives it extraordinary properties.\n"
        f"Step 2: Biological function:\n"
        f"{property_name} provides {desc}."
    )
    return {
        "id": f"ns8_sol_40_{rng.randint(100000, 999999)}",
        "subskill": "40_liquid_water_as_essential_solvent_for_life",
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
            "tier_1": "What does this special property of water do?",
            "tier_2": f"It provides {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["water_properties_supporting_life"]
    }


def arch_41_earth_atmosphere_composition_oxygen_nitrogen(rng: random.Random) -> Dict[str, Any]:
    gas = rng.choice(["Nitrogen (N2)", "Oxygen (O2)"])
    if gas == "Nitrogen (N2)":
        pct = "78%"
        role = "dilutes oxygen to prevent explosive runaway fires and provides essential nitrogen for amino acids and proteins"
    else:
        pct = "21%"
        role = "supports aerobic cellular respiration and forms the stratospheric ozone layer shielding against UV radiation"
    prompt = (
        f"Earth's unique atmosphere sustains complex multicellular life.\n\n"
        f"What approximate percentage of clean, dry air is made up of **{gas}**, and what is its primary biological/atmospheric role?"
    )
    correct = f"Approximately {pct}; it {role}."
    options = [
        correct,
        f"Approximately 5%; it causes global oceans to evaporate into space every summer.",
        f"Approximately 95%; it turns all rocks into pure molten iron ore.",
        f"Approximately 50%; it freezes all living organisms instantly at room temperature."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Earth atmospheric proportions:\n"
        "Nitrogen: ~78%, Oxygen: ~21%, Argon: ~0,93%, Carbon dioxide: ~0,04%.\n"
        f"Step 2: Role of {gas}:\n"
        f"{gas} accounts for {pct} and {role}."
    )
    return {
        "id": f"ns8_sol_41_{rng.randint(100000, 999999)}",
        "subskill": "41_earth_atmosphere_composition_oxygen_nitrogen",
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
            "tier_1": f"Recall the abundance of {gas} in Earth's air (78% vs 21%).",
            "tier_2": f"{gas} makes up {pct} of the atmosphere.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["earth_atmospheric_gas_ratios"]
    }


def arch_42_earth_greenhouse_effect_regulating_temperature(rng: random.Random) -> Dict[str, Any]:
    temp_diff = rng.choice(["33 °C", "approximately 33 degrees Celsius"])
    prompt = (
        f"Without its natural greenhouse effect, Earth's average surface temperature would be approximately -18 °C instead of its current life-sustaining +15 °C—a crucial difference of {temp_diff}.\n\n"
        "How do natural greenhouse gases (such as water vapor and carbon dioxide) achieve this warming?"
    )
    correct = "They allow visible shortwave sunlight to pass through to warm the surface, but absorb and re-radiate infrared thermal energy emitted by the Earth."
    options = [
        correct,
        "They generate internal nuclear fission heat directly inside individual gas molecules.",
        "They completely block all incoming visible light from reaching the planetary ground.",
        "They reflect solar wind particles into polar orbit to create friction."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Incoming solar radiation:\n"
        "Sunlight arrives mostly as shortwave visible and ultraviolet radiation, passing transparently through greenhouse gases.\n"
        "Step 2: Re-radiation and absorption:\n"
        "Earth's surface absorbs sunlight and re-radiates it as longer-wavelength infrared (thermal) radiation. Greenhouse gases absorb this infrared energy and radiate it in all directions, trapping heat in the lower atmosphere."
    )
    return {
        "id": f"ns8_sol_42_{rng.randint(100000, 999999)}",
        "subskill": "42_earth_greenhouse_effect_regulating_temperature",
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
            "tier_1": "What type of radiation do greenhouse gases trap?",
            "tier_2": "Infrared (heat) radiation emitted by Earth's surface.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["natural_greenhouse_effect_mechanism"]
    }


def arch_43_earth_magnetosphere_shielding_solar_wind(rng: random.Random) -> Dict[str, Any]:
    core_state = rng.choice(["convection currents in the liquid iron-nickel outer core", "the geodynamo of molten outer core metals"])
    prompt = (
        f"Earth possesses a powerful magnetic field (magnetosphere) generated by {core_state}.\n\n"
        "Why is this magnetosphere critically indispensable for preserving life on Earth?"
    )
    correct = "It deflects the high-speed charged particles of the solar wind, preventing them from stripping away our atmosphere and bombarding surface DNA with lethal radiation."
    options = [
        correct,
        "It prevents the Earth from falling into the Sun by pushing against solar gravity.",
        "It stops tectonic plates from moving and causing volcanic eruptions.",
        "It creates artificial gravity that holds human beings down on the ground."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Solar wind threat:\n"
        "The Sun continuously emits a stream of energetic protons and electrons (solar wind).\n"
        "Step 2: Magnetospheric shield:\n"
        "Lorentz forces deflect these charged particles around Earth (creating the Van Allen belts and auroras). Without this shield, our atmosphere would be stripped away into space (as happened to Mars)."
    )
    return {
        "id": f"ns8_sol_43_{rng.randint(100000, 999999)}",
        "subskill": "43_earth_magnetosphere_shielding_solar_wind",
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
            "tier_1": "What dangerous stream from the Sun does the magnetic field deflect?",
            "tier_2": "The solar wind (charged particles).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["earth_magnetosphere_solar_wind_shield"]
    }


def arch_44_ozone_layer_filtering_harmful_ultraviolet(rng: random.Random) -> Dict[str, Any]:
    layer = rng.choice(["stratosphere", "lower to middle stratosphere (20-30 km altitude)"])
    prompt = (
        f"Located in the {layer}, the ozone layer consists of molecules composed of three oxygen atoms (O3).\n\n"
        "What specific protective function does the ozone layer provide for living organisms on Earth?"
    )
    correct = "It absorbs high-energy ultraviolet radiation (UV-B and UV-C), which causes severe DNA damage, skin cancers, and cataract blindness."
    options = [
        correct,
        "It absorbs carbon dioxide to prevent plants from performing excessive photosynthesis.",
        "It traps incoming meteors and transforms them into harmless liquid rainwater.",
        "It generates electrical lightning to power global wireless communication networks."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Ozone chemistry:\n"
        "Stratospheric ozone (O3) dissociates upon absorbing ultraviolet photons (UV-C and UV-B).\n"
        "Step 2: Biological protection:\n"
        "High-energy UV breaks chemical bonds in DNA and cellular proteins. By filtering out >98% of harmful solar UV, the ozone layer made terrestrial life possible."
    )
    return {
        "id": f"ns8_sol_44_{rng.randint(100000, 999999)}",
        "subskill": "44_ozone_layer_filtering_harmful_ultraviolet",
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
            "tier_1": "What dangerous solar rays does ozone absorb?",
            "tier_2": "Ultraviolet (UV) radiation.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ozone_layer_uv_filtering"]
    }


def arch_45_planetary_orbital_periods_keplerian_distance_trend(rng: random.Random) -> Dict[str, Any]:
    planet_pair = rng.choice([
        ("Mercury (0,39 AU)", "Earth (1,0 AU)", "88 Earth days", "365,25 days"),
        ("Earth (1,0 AU)", "Jupiter (5,2 AU)", "1 Earth year", "11,86 Earth years"),
        ("Jupiter (5,2 AU)", "Neptune (30,1 AU)", "11,86 Earth years", "164,8 Earth years")
    ])
    p1, p2, t1, t2 = planet_pair
    prompt = (
        f"Comparing two planets in our solar system: {p1} has an orbital period of {t1}, while {p2} has an orbital period of {t2}.\n\n"
        "What fundamental orbital mechanics principle explains why planets farther from the Sun have significantly longer orbital periods?"
    )
    correct = "Farther planets have larger orbital circumferences to traverse AND experience weaker solar gravitational pull, causing them to travel at slower orbital speeds."
    options = [
        correct,
        "Farther planets are heavier, so they sink into space fabric and cannot roll as fast.",
        "Farther planets experience high solar friction because outer space is filled with dense nitrogen gas.",
        "Farther planets spin much faster on their axes, which pulls them backwards in orbit."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Kepler's Third Law (T² ∝ r³):\n"
        "Two compounding factors lengthen orbital periods as distance increases:\n"
        "1. Orbital perimeter is proportional to radius (C = 2πr).\n"
        "2. Gravitational force weakens with distance squared, so orbital speed (v = sqrt(GM/r)) decreases with distance.\n"
        "Step 2: Conclusion:\n"
        "Farther planets travel a longer track at a slower speed, resulting in vastly longer orbital periods."
    )
    return {
        "id": f"ns8_sol_45_{rng.randint(100000, 999999)}",
        "subskill": "45_planetary_orbital_periods_keplerian_distance_trend",
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
            "tier_1": "Think about both orbital distance and orbital velocity.",
            "tier_2": "Longer orbital distance + slower speed = longer year.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["kepler_third_law_orbital_period_trend"]
    }


def arch_46_planetary_temperatures_inverse_square_solar_flux(rng: random.Random) -> Dict[str, Any]:
    dist_factor = rng.choice([2, 3])
    flux_drop = dist_factor ** 2
    prompt = (
        f"The intensity of solar radiation follows the **inverse-square law**. If a spacecraft travels from 1 AU to {dist_factor} AU from the Sun, the distance has increased by a factor of {dist_factor}.\n\n"
        f"By what factor does the intensity of solar energy received per square meter decrease?"
    )
    correct = f"It decreases by a factor of {flux_drop} (down to 1/{flux_drop} of the original value)."
    options = [
        correct,
        f"It decreases by a factor of {dist_factor} (down to 1/{dist_factor} of the original value).",
        f"It increases by a factor of {flux_drop} because space concentrates solar rays.",
        f"It remains exactly identical because sunlight travels at the speed of light."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: State inverse-square law:\n"
        "Solar intensity I ∝ 1 / d².\n"
        f"Step 2: Calculate for distance factor {dist_factor}:\n"
        f"I_new / I_old = 1 / ({dist_factor})² = 1 / {flux_drop}.\n"
        f"The solar radiation intensity drops to 1/{flux_drop} (a factor of {flux_drop})."
    )
    return {
        "id": f"ns8_sol_46_{rng.randint(100000, 999999)}",
        "subskill": "46_planetary_temperatures_inverse_square_solar_flux",
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
            "tier_1": "Use the inverse-square formula: 1 / d².",
            "tier_2": f"If d is multiplied by {dist_factor}, d² is {flux_drop}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["inverse_square_law_solar_radiation"]
    }


def arch_47_planetary_mass_and_surface_gravity_comparison(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice([60, 70, 80])
    # Weight on Moon is ~1/6th, on Jupiter is ~2.5x
    w_earth = mass * 9.8
    w_moon = w_earth / 6.0
    prompt = (
        f"An astronaut has a mass of {mass} kg, resulting in a weight of approximately {w_earth:.0f} N on Earth.\n\n"
        "If this astronaut lands on the Moon (surface gravity ~1,6 m/s², roughly 1/6th of Earth's), what happens to their **mass** and **weight**?"
    )
    correct = f"Their mass remains exactly {mass} kg, but their weight decreases to approximately {w_moon:.0f} N."
    options = [
        correct,
        f"Their mass drops to 0 kg, but their weight increases to {w_earth * 6:.0f} N.",
        f"Both their mass and weight drop to 0 kg because there is zero gravity on the Moon.",
        f"Their mass drops to {mass / 6:.1f} kg while their weight remains {w_earth:.0f} N."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Distinguish mass vs weight:\n"
        "Mass is the amount of matter in an object (measured in kg) and is invariant across the universe.\n"
        f"Astronaut mass on Moon = {mass} kg.\n"
        "Step 2: Calculate weight on Moon:\n"
        f"Weight = m * g = {mass} kg * 1,62 m/s² ≈ {w_moon:.0f} N (approx 1/6 of Earth weight)."
    )
    return {
        "id": f"ns8_sol_47_{rng.randint(100000, 999999)}",
        "subskill": "47_planetary_mass_and_surface_gravity_comparison",
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
            "tier_1": "Does mass ever change when moving between planets?",
            "tier_2": "Mass stays constant; only weight changes with gravity.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mass_vs_weight_surface_gravity"]
    }


def arch_48_space_exploration_probes_voyager_curiosity_new_horizons(rng: random.Random) -> Dict[str, Any]:
    probes = [
        ("Voyager 1 and 2", "exploration of outer giant planets (Jupiter, Saturn, Uranus, Neptune) and crossing into interstellar space"),
        ("New Horizons", "first historic close-up flyby reconnaissance of Pluto and Kuiper Belt object Arrokoth"),
        ("Curiosity and Perseverance", "robotic surface rover investigation of Martian geology, past water, and biosignatures in Jezero Crater")
    ]
    probe_name, mission = rng.choice(probes)
    prompt = (
        f"Uncrewed robotic spacecraft have revolutionized our knowledge of the solar system.\n\n"
        f"What was the primary scientific achievement of the **{probe_name}** mission?"
    )
    correct = mission
    options = [
        correct,
        "Landing the first human astronauts on the core of the Sun.",
        "Mining commercial diamonds from the rings of Saturn to sell on Earth.",
        "Detonating nuclear weapons to alter the orbit of Neptune."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify mission objectives:\n"
        f"{probe_name} was designed for planetary exploration.\n"
        f"Step 2: Milestone achievement:\n"
        f"The primary scientific contribution was: {mission}."
    )
    return {
        "id": f"ns8_sol_48_{rng.randint(100000, 999999)}",
        "subskill": "48_space_exploration_probes_voyager_curiosity_new_horizons",
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
            "tier_1": f"What target did {probe_name} explore?",
            "tier_2": f"Review the key accomplishment: {mission[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["space_exploration_probes_milestones"]
    }


def arch_49_exoplanets_detection_habitable_zones_other_stars(rng: random.Random) -> Dict[str, Any]:
    method, desc = rng.choice([
        ("the transit method", "detecting periodic minute dips in a host star's brightness when a planet passes directly across its stellar disc"),
        ("the radial velocity (Doppler) method", "measuring subtle periodic wobbles in a star's spectral lines caused by the gravitational tug of an orbiting planet")
    ])
    prompt = (
        "Astronomers have now confirmed thousands of **exoplanets** (planets orbiting stars beyond our solar system).\n\n"
        f"How does **{method}** detect these distant worlds?"
    )
    correct = desc
    options = [
        correct,
        "Sending astronauts in chemical rocket ships to land on each exoplanet surface.",
        "Listening for radio voice transmissions from intelligent alien civilizations.",
        "Capturing high-resolution smartphone photographs through ordinary optical microscopes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Exoplanet detection methods:\n"
        "Exoplanets are too dim and close to their bright host stars to photograph directly with ease.\n"
        f"Step 2: Mechanism of {method}:\n"
        f"{method} operates by {desc}."
    )
    return {
        "id": f"ns8_sol_49_{rng.randint(100000, 999999)}",
        "subskill": "49_exoplanets_detection_habitable_zones_other_stars",
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
            "tier_1": f"How does {method} observe the star?",
            "tier_2": f"It relies on {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["exoplanet_detection_methods"]
    }


def arch_50_solar_system_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    body, trait, fact = rng.choice([
        ("Mercury", "extreme surface temperature swings (-180 °C to 430 °C)", "absence of a substantial atmosphere to trap heat"),
        ("Venus", "highest mean surface temperature in the solar system (~465 °C)", "dense runaway carbon dioxide greenhouse atmosphere"),
        ("Titan", "liquid hydrocarbon lakes and dense nitrogen atmosphere", "cryogenic surface temperatures (-179 °C) allowing liquid methane"),
        ("Europa", "subsurface liquid water ocean under cracked ice crust", "tidal heating from Jupiter's immense gravitational forces")
    ])
    prompt = (
        f"**Comprehensive Planetary Diagnostic:**\n"
        f"In analyzing celestial bodies across the solar system, scientists observe that **{body}** displays **{trait}**.\n\n"
        f"What underlying physical mechanism accounts for this specific phenomenon on {body}?"
    )
    correct = fact
    options = [
        correct,
        "nuclear fusion detonations occurring continuously on its outer surface crust",
        "human industrial pollution from ancient space stations orbiting the Sun",
        "electromagnetic friction caused by Earth's communication satellites"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Target body and feature:\n"
        f"{body} exhibits {trait}.\n"
        f"Step 2: Physical causation:\n"
        f"The scientific cause is: {fact}."
    )
    return {
        "id": f"ns8_sol_50_{rng.randint(100000, 999999)}",
        "subskill": "50_solar_system_comprehensive_diagnostic_autopsy",
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
            "tier_1": f"What causes {trait} on {body}?",
            "tier_2": f"The cause is {fact[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["solar_system_diagnostic_autopsy"]
    }


BUILDERS_26_50 = {
    "26_uranus_extreme_axial_tilt_and_seasons": arch_26_uranus_extreme_axial_tilt_and_seasons,
    "27_uranus_ice_giant_composition_and_methane": arch_27_uranus_ice_giant_composition_and_methane,
    "28_neptune_supersonic_winds_and_great_dark_spot": arch_28_neptune_supersonic_winds_and_great_dark_spot,
    "29_neptune_moon_triton_retrograde_orbit_geysers": arch_29_neptune_moon_triton_retrograde_orbit_geysers,
    "30_kuiper_belt_location_and_icy_composition": arch_30_kuiper_belt_location_and_icy_composition,
    "31_pluto_dwarf_planet_reclassification_criteria": arch_31_pluto_dwarf_planet_reclassification_criteria,
    "32_iau_planet_definition_three_conditions": arch_32_iau_planet_definition_three_conditions,
    "33_dwarf_planets_examples_ceres_erisa_makemake": arch_33_dwarf_planets_examples_ceres_erisa_makemake,
    "34_oort_cloud_spherical_reservoir_long_period_comets": arch_34_oort_cloud_spherical_reservoir_long_period_comets,
    "35_comet_anatomy_nucleus_coma_and_tails": arch_35_comet_anatomy_nucleus_coma_and_tails,
    "36_comet_ion_tail_vs_dust_tail_physics": arch_36_comet_ion_tail_vs_dust_tail_physics,
    "37_comet_tail_orientation_away_from_sun": arch_37_comet_tail_orientation_away_from_sun,
    "38_halley_comet_periodic_orbit_76_years": arch_38_halley_comet_periodic_orbit_76_years,
    "39_circumstellar_habitable_zone_goldilocks_concept": arch_39_circumstellar_habitable_zone_goldilocks_concept,
    "40_liquid_water_as_essential_solvent_for_life": arch_40_liquid_water_as_essential_solvent_for_life,
    "41_earth_atmosphere_composition_oxygen_nitrogen": arch_41_earth_atmosphere_composition_oxygen_nitrogen,
    "42_earth_greenhouse_effect_regulating_temperature": arch_42_earth_greenhouse_effect_regulating_temperature,
    "43_earth_magnetosphere_shielding_solar_wind": arch_43_earth_magnetosphere_shielding_solar_wind,
    "44_ozone_layer_filtering_harmful_ultraviolet": arch_44_ozone_layer_filtering_harmful_ultraviolet,
    "45_planetary_orbital_periods_keplerian_distance_trend": arch_45_planetary_orbital_periods_keplerian_distance_trend,
    "46_planetary_temperatures_inverse_square_solar_flux": arch_46_planetary_temperatures_inverse_square_solar_flux,
    "47_planetary_mass_and_surface_gravity_comparison": arch_47_planetary_mass_and_surface_gravity_comparison,
    "48_space_exploration_probes_voyager_curiosity_new_horizons": arch_48_space_exploration_probes_voyager_curiosity_new_horizons,
    "49_exoplanets_detection_habitable_zones_other_stars": arch_49_exoplanets_detection_habitable_zones_other_stars,
    "50_solar_system_comprehensive_diagnostic_autopsy": arch_50_solar_system_comprehensive_diagnostic_autopsy,
}
