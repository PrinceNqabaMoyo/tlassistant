"""Natural Sciences Grade 8 Term 4: Beyond the Solar System Generator.

Strictly grounded in curriculum_docs_auto/NaturalSciences_Gr8/Syllabus.md.
Covers:
- milky_way_galaxy_structure: Spiral galaxy structure, galactic core, position of Sun in outer spiral arm.
- astronomical_distance_units: Definition of light years, light hours, light minutes; scale conversion calculations.
- nearest_stars_proxima_centauri: Sun as nearest star, Proxima Centauri / Alpha Centauri (4.2 light years), Southern Cross pointers.
- galaxies_types_and_universe_scale: Spiral, elliptical, and irregular galaxies; scale of observable universe.
- nebulae_and_stellar_nurseries: Interstellar clouds of gas and hydrogen collapsing under gravity to birth stars.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


SUBSKILLS = [
    "milky_way_galaxy_structure",
    "astronomical_distance_units",
    "nearest_stars_proxima_centauri",
    "galaxies_types_and_universe_scale",
    "nebulae_and_stellar_nurseries",
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _build_milky_way(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    skies = [
        "On clear, dark winter nights in the Karoo semi-desert of South Africa",
        "From the high-altitude plateau of Sutherland in the Northern Cape",
        "Looking upwards from the Drakensberg mountain highlands away from city light pollution"
    ]
    prompt = (
        f"{rng.choice(skies)}, a breathtaking hazy band of dense starlight stretches across the celestial sphere.\n\n"
        f"1. Name the galaxy that our Solar System is part of.\n"
        f"2. What geometric shape and structure does our galaxy have?\n"
        f"3. Describe the location of our Sun within our galaxy (e.g. at the exact center, or in an outer spiral arm).\n"
        f"4. Name the fundamental force of nature that holds the billions of stars and dust clouds together in the galaxy."
    )
    sample_answer = (
        "1. The Milky Way Galaxy.\n"
        "2. A barred spiral galaxy (a rotating flat disc with curved spiral arms radiating from a central bulge).\n"
        "3. The Sun is located towards the outer edge, approximately two-thirds of the way out from the center in one of the spiral arms (the Orion Arm).\n"
        "4. Gravity (gravitational force of attraction)."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Galaxy name: Milky Way [1 mark].\n"
        "2. Structure: Spiral / barred spiral shape with curved spiral arms [1 mark].\n"
        "3. Solar location: Outer spiral arm (Orion Arm) / roughly two-thirds out from the center [1 mark].\n"
        "4. Binding force: Gravity [1 mark]."
    )
    return {
        "id": _make_id("ns8_milky_way", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "milky_way_galaxy_structure",
        "question_family_id": "milky_way_galaxy_structure",
        "curriculum_reference": "Natural Sciences Gr8 Term 4 > Beyond the Solar System > The Milky Way Galaxy",
        "hints": {
            "tier_1": "We live inside the Milky Way Galaxy.",
            "tier_2": "Our galaxy is shaped like a spinning spiral disc, not a sphere.",
            "tier_3": "The Sun sits in an outer spiral arm held together by gravity."
        },
        "misconception_tags": ["sun_at_galactic_center_misconception"]
    }


def _build_astronomical_units(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    years = rng.choice([2, 4, 8, 10])
    distance_km = years * 10
    prompt = (
        f"Because distances in deep interstellar space are enormous, astronomers define the **light year** as a unit of measurement.\n\n"
        f"1. Define what a **light year** is in scientific terms.\n"
        f"2. Given that 1 light year is approximately $10\\text{{ trillion km}}$ ($10\\,000\\,000\\,000\\,000\\text{{ km}}$), "
        f"calculate the distance in trillions of kilometers to a star located **{years} light years** from Earth.\n"
        f"3. Explain why astronomers describe looking at distant stars as 'looking back in time'."
    )
    sample_answer = (
        "1. A light year is the total distance that light travels in a vacuum in one Earth year (approx. 9,46 trillion km or ~10 trillion km).\n"
        f"2. Distance = {years} light years x 10 trillion km/ly = {distance_km} trillion kilometers ({distance_km * 10**12:,} km).\n"
        f"3. Because light takes {years} years to travel across space to reach Earth, the light entering our eyes or telescopes today left the star {years} years ago, revealing what the star looked like in the past."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Light year definition: Distance light travels in one Julian year (distance unit, not time unit) [1 mark].\n"
        f"2. Calculation: {years} x 10 = {distance_km} trillion km [1 mark].\n"
        "3. Looking back in time: Light took years to travel across vast distances; we see the star as it existed when the light was emitted [2 marks]."
    )
    return {
        "id": _make_id("ns8_light_year", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "astronomical_distance_units",
        "question_family_id": "astronomical_distance_units",
        "curriculum_reference": "Natural Sciences Gr8 Term 4 > Beyond the Solar System > Astronomical distance units",
        "hints": {
            "tier_1": "A light year is a measure of distance, NOT time.",
            "tier_2": f"Multiply {years} by 10 trillion km.",
            "tier_3": f"Distance is {distance_km} trillion km; we see past light."
        },
        "misconception_tags": ["light_year_is_a_unit_of_time_misconception"]
    }


def _build_nearest_stars(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    dist = rng.choice(["4,24", "approx. 4,2", "4,22"])
    prompt = (
        f"Astronomers distinguish between the nearest star to Earth and the nearest star system outside our Solar System located {dist} light years away.\n\n"
        "1. Name the star that is closest to planet Earth.\n"
        "2. Outside of our Solar System, which star (part of the Alpha Centauri system) is closest to our Sun, and approximately how many light years away is it?\n"
        "3. In the night sky of the Southern Hemisphere, which famous constellation contains stars that point directly towards Alpha Centauri?"
    )
    sample_answer = (
        "1. The Sun.\n"
        "2. Proxima Centauri (Alpha Centauri system), approximately 4,2 light years away.\n"
        "3. The Southern Cross (Crux) — specifically, the two Pointers (Alpha and Beta Centauri)."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        "1. Nearest star to Earth: The Sun [1 mark].\n"
        "2. Nearest star system: Proxima Centauri / Alpha Centauri at approx. 4,2 light years [1 mark].\n"
        "3. Southern sky constellation: Southern Cross / Crux (and its Pointers) [1 mark]."
    )
    return {
        "id": _make_id("ns8_near_stars", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "nearest_stars_proxima_centauri",
        "question_family_id": "nearest_stars_proxima_centauri",
        "curriculum_reference": "Natural Sciences Gr8 Term 4 > Beyond the Solar System > Our nearest stars",
        "hints": {
            "tier_1": "The Sun is a star right next to us.",
            "tier_2": "The nearest star outside our solar system is Proxima Centauri at 4.2 light years.",
            "tier_3": "The Southern Cross and its Pointers mark this in the southern sky."
        },
        "misconception_tags": ["sun_is_not_a_star_misconception"]
    }


def _build_galaxies_universe_scale(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    shapes = [
        ("Spiral galaxy", "Flat rotating disk with curved spiral arms rich in interstellar gas and newly forming stars (like the Milky Way and Andromeda)"),
        ("Elliptical galaxy", "Egg-shaped or smooth spherical collection of older stars with very little interstellar gas or new star formation"),
        ("Irregular galaxy", "Asymmetrical galaxy with no definite geometric structure, often caused by gravitational collisions (like the Magellanic Clouds)")
    ]
    g_type, g_desc = rng.choice(shapes)
    prompt = (
        f"Astronomers classify galaxies into distinct morphological shapes.\n\n"
        f"Which type of galaxy is characterized by: *{g_desc}*?"
    )
    correct_ans = g_type
    distractors = [t for t, d in shapes if t != g_type]
    distractors.append("Planetary nebula")
    options = [correct_ans] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Analyze galactic characteristics:\n"
        f"{g_desc}.\n\n"
        f"Step 2: Match to Hubble classification:\n"
        f"This defines a **{correct_ans}**."
    )
    return {
        "id": _make_id("ns8_gal_types", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "galaxies_types_and_universe_scale",
        "question_family_id": "galaxies_types_and_universe_scale",
        "curriculum_reference": "Natural Sciences Gr8 Term 4 > Beyond the Solar System > Types of galaxies",
        "hints": {
            "tier_1": "The three main galaxy shapes are spiral, elliptical, and irregular.",
            "tier_2": "Spiral galaxies have rotating arms; elliptical galaxies are egg-shaped; irregular galaxies have no shape.",
            "tier_3": f"The answer is {correct_ans}."
        },
        "misconception_tags": ["all_galaxies_are_spiral_misconception"]
    }


def _build_nebulae_nurseries(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    neb = rng.choice(["the Orion Nebula (M42)", "the Eagle Nebula (Pillars of Creation)", "the Carina Nebula (NGC 3372)", "the Lagoon Nebula (M8)"])
    prompt = (
        f"In deep interstellar space, massive glowing clouds of gas and cosmic dust such as {neb} are observed by optical and infrared space telescopes.\n\n"
        "1. What is the scientific name for these giant interstellar clouds of dust and gas?\n"
        "2. Which abundant chemical gas makes up the majority of matter inside these stellar nurseries?\n"
        "3. Explain how gravitational force causes a star (such as our Sun) to form inside one of these clouds.\n"
        "4. Name the nuclear process ignited at the core of a newly born star that produces enormous heat and light."
    )
    sample_answer = (
        "1. A nebula (plural: nebulae).\n"
        "2. Hydrogen gas (H2).\n"
        "3. Mutual gravitational attraction pulls gas and dust particles closer together. As the cloud collapses and condenses, density, pressure, and core temperature rise dramatically until a protostar forms.\n"
        "4. Nuclear fusion (conversion of hydrogen nuclei into helium)."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Name: Nebula [1 mark].\n"
        "2. Element: Hydrogen gas [1 mark].\n"
        "3. Gravitational collapse mechanism: Gravity pulls matter together, increasing density and temperature [1 mark].\n"
        "4. Nuclear ignition: Nuclear fusion of hydrogen into helium [1 mark]."
    )
    return {
        "id": _make_id("ns8_nebula", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "nebulae_and_stellar_nurseries",
        "question_family_id": "nebulae_and_stellar_nurseries",
        "curriculum_reference": "Natural Sciences Gr8 Term 4 > Beyond the Solar System > Stellar nurseries and nebulae",
        "hints": {
            "tier_1": "Stars are born in huge gas clouds called nebulae.",
            "tier_2": "Gravity squeezes hydrogen until nuclear fusion begins.",
            "tier_3": "Nebula -> Hydrogen -> Gravitational collapse -> Nuclear fusion."
        },
        "misconception_tags": ["stars_burn_with_oxygen_misconception"]
    }


def generate(archetype: Optional[str] = None, seed: Optional[int] = None, count: int = 1, **kwargs) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    results = []
    for idx in range(count):
        target = archetype or rng.choice(SUBSKILLS)
        if target == "milky_way_galaxy_structure":
            item = _build_milky_way(rng, seed, idx)
        elif target == "astronomical_distance_units":
            item = _build_astronomical_units(rng, seed, idx)
        elif target == "nearest_stars_proxima_centauri":
            item = _build_nearest_stars(rng, seed, idx)
        elif target == "galaxies_types_and_universe_scale":
            item = _build_galaxies_universe_scale(rng, seed, idx)
        elif target == "nebulae_and_stellar_nurseries":
            item = _build_nebulae_nurseries(rng, seed, idx)
        else:
            item = _build_milky_way(rng, seed, idx)
        results.append(item)
    return results


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)
