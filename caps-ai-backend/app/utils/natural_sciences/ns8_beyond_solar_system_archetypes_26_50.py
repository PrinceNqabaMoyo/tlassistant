"""Grade 8 Natural Sciences - Beyond the Solar System: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr8/Term 4/01. Beyond the solar system.md
Focus:
Galaxy types (Hubble classification, spirals, barred spirals, ellipticals, irregulars, lenticulars),
Local cosmic neighborhood (Magellanic Clouds, Andromeda, Milky Way-Andromeda merger, Local Group, Virgo Cluster,
Laniakea Supercluster, Cosmic Web), Large-scale universe (Observable universe, 93-billion ly scale, Hubble expansion,
cosmological redshift, Big Bang, CMBR, Dark matter, Gravitational lensing, Dark energy, Galaxy Zoo citizen science,
SALT telescope in Sutherland, Comprehensive Diagnostic Autopsy).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_hubble_galaxy_classification_system_overview(rng: random.Random) -> Dict[str, Any]:
    cat = rng.choice(["spiral", "elliptical", "irregular"])
    if cat == "spiral":
        desc = "flattened rotating discs with pinwheel-like spiral arms rich in gas and young stars"
    elif cat == "elliptical":
        desc = "smooth, oval or spherical shapes dominated by older stars with minimal gas or active star formation"
    else:
        desc = "chaotic, asymmetric shapes lacking central symmetry, often resulting from gravitational tidal collisions"
    prompt = (
        "In 1926, astronomer Edwin Hubble organized galaxies into a famous classification sequence based on their visual appearance.\n\n"
        f"Which statement accurately describes the characteristics of **{cat} galaxies** in this system?"
    )
    correct = desc
    options = [
        correct,
        "hollow cylindrical tubes of pure solid ice floating in intergalactic space",
        "single giant stars surrounded by millions of artificial metallic rings",
        "microscopic atoms floating inside planetary atmospheres"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Hubble classification system:\n"
        "Galaxies are classified by morphology into Ellipticals (E0–E7), Spirals (S), Barred Spirals (SB), and Irregulars (Irr).\n"
        f"Step 2: Define {cat} galaxies:\n"
        f"{cat.capitalize()} galaxies are {desc}."
    )
    return {
        "id": f"ns8_bss_26_{rng.randint(100000, 999999)}",
        "subskill": "26_hubble_galaxy_classification_system_overview",
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
            "tier_1": f"What is the key visual feature of a {cat} galaxy?",
            "tier_2": f"It has {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hubble_galaxy_classification_overview"]
    }


def arch_27_spiral_galaxies_morphology_and_star_formation(rng: random.Random) -> Dict[str, Any]:
    ex = rng.choice(["the Whirlpool Galaxy (M51)", "the Pinwheel Galaxy (M101)", "the Andromeda Galaxy (M31)"])
    prompt = (
        f"Classic **spiral galaxies**, such as {ex}, display winding luminous arms extending outward from a central nucleus.\n\n"
        "What physical condition within the spiral arms makes them vibrant engines of ongoing star birth?"
    )
    correct = "High concentrations of cool, dense interstellar molecular gas and cosmic dust compressed by gravitational density waves."
    options = [
        correct,
        "Extremely high temperatures exceeding 100 million degrees that boil all space atoms.",
        "A total lack of any matter, leaving empty vacuum where stars appear out of nothing.",
        "Intense magnetic currents flowing between human radio towers on Earth."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Ingredients for star formation:\n"
        "Stars condense from cold molecular gas clouds (mostly hydrogen and helium) mixed with interstellar dust.\n"
        "Step 2: Role of spiral arms:\n"
        "Spiral density waves compress these clouds as they pass through, causing gravitational collapse that sparks the ignition of thousands of new stars (H II regions like the Orion Nebula)."
    )
    return {
        "id": f"ns8_bss_27_{rng.randint(100000, 999999)}",
        "subskill": "27_spiral_galaxies_morphology_and_star_formation",
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
            "tier_1": "What raw materials do new stars need to form?",
            "tier_2": "Dense molecular gas and dust clouds compressed by gravity.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["spiral_galaxy_star_formation_mechanism"]
    }


def arch_28_barred_spiral_galaxies_milky_way_classification(rng: random.Random) -> Dict[str, Any]:
    bar_len = rng.choice(["roughly 27 000 light years", "approximately 25 000 to 28 000 light years"])
    prompt = (
        f"Modern infrared space telescopes (such as Spitzer) revealed that our Milky Way is specifically a **barred spiral galaxy** (type SBbc), featuring a central stellar bar spanning {bar_len}.\n\n"
        "How does a barred spiral galaxy differ structurally from an ordinary, unbarred spiral galaxy?"
    )
    correct = "Its spiral arms do not emerge directly from the round spherical core, but instead attach to the two opposing ends of a straight, elongated central bar of stars."
    options = [
        correct,
        "It is permanently surrounded by a solid cage of iron prison bars constructed by ancient extraterrestrials.",
        "Its spiral arms spin in opposite directions simultaneously, cancelling out all galaxy rotation.",
        "It contains zero stars and consists entirely of invisible black holes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Barred spiral anatomy:\n"
        "In a barred spiral galaxy (designated SB in the Hubble scheme), stars and gas in the central bulge form an elongated bar-shaped structure.\n"
        "Step 2: Spiral arm origin:\n"
        "The major spiral arms sweep out from the endpoints of this central bar rather than originating symmetrically from a spherical core."
    )
    return {
        "id": f"ns8_bss_28_{rng.randint(100000, 999999)}",
        "subskill": "28_barred_spiral_galaxies_milky_way_classification",
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
            "tier_1": "Where do the spiral arms attach in a barred spiral galaxy?",
            "tier_2": "To the ends of an elongated central bar of stars.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["barred_spiral_morphology_difference"]
    }


def arch_29_elliptical_galaxies_characteristics_and_stellar_population(rng: random.Random) -> Dict[str, Any]:
    ex = rng.choice(["Messier 87 (M87) in the Virgo Cluster", "Messier 49", "Messier 60"])
    prompt = (
        f"Giant **elliptical galaxies**, such as {ex}, are among the most massive cosmic structures in the universe, containing trillions of stars.\n\n"
        "Why do elliptical galaxies have virtually zero ongoing star formation?"
    )
    correct = "They have exhausted or ejected nearly all their cool interstellar gas and dust, leaving only ancient, long-lived stars."
    options = [
        correct,
        "Their internal temperatures are below absolute zero, so atoms cannot move.",
        "They are surrounded by dark energy shields that destroy any new stars immediately.",
        "Their stars orbit so rapidly that centrifugal force ejects all hydrogen into outer space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Composition of elliptical galaxies:\n"
        "Ellipticals are dominated by Population II stars (old red and yellow low-mass stars).\n"
        "Step 2: Lack of star formation:\n"
        "Past galactic collisions and supermassive black hole feedback swept away cool interstellar molecular gas. Without dense, cold gas clouds, new star birth cannot take place."
    )
    return {
        "id": f"ns8_bss_29_{rng.randint(100000, 999999)}",
        "subskill": "29_elliptical_galaxies_characteristics_and_stellar_population",
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
            "tier_1": "What essential material is missing in elliptical galaxies?",
            "tier_2": "Cold interstellar gas and dust needed to make new stars.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["elliptical_galaxy_star_formation_cessation"]
    }


def arch_30_irregular_galaxies_chaotic_structure_and_gas_content(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Approximately 3% of known galaxies are classified as **irregular galaxies** (such as the Magellanic Clouds).\n\n"
        "What geological or physical process typically produces the chaotic, asymmetrical appearance of irregular galaxies?"
    )
    correct = "Gravitational tidal distortion and disturbance caused by close encounters or collisions with larger neighboring galaxies."
    options = [
        correct,
        "Nuclear detonations triggered simultaneously by planetary civilizations.",
        "Erosion caused by interstellar winds blowing from Earth's atmosphere.",
        "Sudden evaporation of the galaxy's supermassive central star."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Irregular galaxy definition:\n"
        "Galaxies lacking distinct rotational symmetry, bulges, or organized spiral arms.\n"
        "Step 2: Gravitational tidal forces:\n"
        "Most irregulars were once normal spiral or dwarf galaxies whose structures were gravitationally warped and disrupted by the strong tidal gravitational pull of nearby massive galaxies."
    )
    return {
        "id": f"ns8_bss_30_{rng.randint(100000, 999999)}",
        "subskill": "30_irregular_galaxies_chaotic_structure_and_gas_content",
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
            "tier_1": "What disrupts a galaxy's neat shape?",
            "tier_2": "Gravitational tidal interactions with larger companion galaxies.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["irregular_galaxy_tidal_disruption"]
    }


def arch_31_lenticular_galaxies_intermediate_lens_structure(rng: random.Random) -> Dict[str, Any]:
    code = rng.choice(["S0", "SB0 (barred lenticular)"])
    prompt = (
        f"In the Hubble sequence, **lenticular galaxies** (designated **{code}**) occupy a transitional position between elliptical and spiral galaxies.\n\n"
        "What combination of structural features characterizes a lenticular galaxy?"
    )
    correct = "A distinct central bulge and a flattened circular disc like a spiral, but completely lacking prominent spiral arms or ongoing star formation."
    options = [
        correct,
        "A triangular solid body made of polished crystalline glass that focuses cosmic laser beams.",
        "A sphere that inverts inside-out every million years due to magnetic polarity reversals.",
        "A ring of identical stars that travel in straight perpendicular lines across space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify transitional status:\n"
        "Lenticular means 'lens-shaped'. They possess a central bulge and a stellar disc (like spirals).\n"
        "Step 2: Lack of spiral arms:\n"
        "Because they have consumed or lost most interstellar gas, they show no spiral arm structure and have negligible star formation, resembling 'armless spirals' or 'discy ellipticals'."
    )
    return {
        "id": f"ns8_bss_31_{rng.randint(100000, 999999)}",
        "subskill": "31_lenticular_galaxies_intermediate_lens_structure",
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
            "tier_1": "Lenticular galaxies have a disk but what do they lack?",
            "tier_2": "They lack spiral arms and ongoing star formation.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lenticular_galaxy_transitional_morphology"]
    }


def arch_32_large_and_small_magellanic_clouds_satellite_galaxies(rng: random.Random) -> Dict[str, Any]:
    cloud, dist_ly = rng.choice([
        ("Large Magellanic Cloud (LMC)", "approximately 160 000 light years"),
        ("Small Magellanic Cloud (SMC)", "approximately 200 000 light years")
    ])
    prompt = (
        f"Visible only from the Southern Hemisphere as luminous detached celestial clouds, the **{cloud}** is located {dist_ly} away.\n\n"
        "What astronomical relationship does this object have with our Milky Way Galaxy?"
    )
    correct = "It is a satellite dwarf irregular galaxy gravitationally bound to and orbiting the Milky Way."
    options = [
        correct,
        "It is a weather storm cloud of water vapor suspended in Earth's upper stratosphere.",
        "It is a distant quasar situated at the outermost edge of the observable universe.",
        "It is an optical reflection of Antarctica projected onto the dome of the sky."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identification of Magellanic Clouds:\n"
        "Named after Portuguese explorer Ferdinand Magellan (1519), the LMC and SMC are prominent naked-eye features of southern skies.\n"
        "Step 2: Satellite dynamics:\n"
        "They are dwarf irregular galaxies orbiting the Milky Way, connected by a tidal bridge of gas known as the Magellanic Stream."
    )
    return {
        "id": f"ns8_bss_32_{rng.randint(100000, 999999)}",
        "subskill": "32_large_and_small_magellanic_clouds_satellite_galaxies",
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
            "tier_1": "Are the Magellanic Clouds clouds of water or satellite galaxies?",
            "tier_2": "Satellite dwarf galaxies orbiting the Milky Way.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["magellanic_clouds_satellite_dwarf_galaxies"]
    }


def arch_33_andromeda_galaxy_m31_distance_and_characteristics(rng: random.Random) -> Dict[str, Any]:
    dist_ly = rng.choice(["2,5 million light years", "approximately 2,5 million light years"])
    prompt = (
        f"The **Andromeda Galaxy (Messier 31)** is located {dist_ly} from Earth and is the most distant object visible to the naked human eye.\n\n"
        "How does the Andromeda Galaxy compare in size and structure to our Milky Way?"
    )
    correct = "It is a larger spiral galaxy containing roughly 1 trillion stars, making it the most massive member of our Local Group."
    options = [
        correct,
        "It is a tiny asteroid orbiting just beyond Mars containing zero stars.",
        "It is a dead black hole with a diameter smaller than the Moon.",
        "It is a spherical ball of incandescent gas located inside our Solar System."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Andromeda scale:\n"
        "At 2,5 million light years away, Andromeda spans ~220 000 light years in diameter.\n"
        "Step 2: Comparison:\n"
        "Like the Milky Way, it is a spiral galaxy, but it contains approximately 1 trillion stars (~2 to 3 times more stars than the Milky Way) and dominates the Local Group."
    )
    return {
        "id": f"ns8_bss_33_{rng.randint(100000, 999999)}",
        "subskill": "33_andromeda_galaxy_m31_distance_and_characteristics",
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
            "tier_1": "Is Andromeda a spiral galaxy larger or smaller than the Milky Way?",
            "tier_2": "It is a larger spiral galaxy with about 1 trillion stars.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["andromeda_scale_and_structure"]
    }


def arch_34_milky_way_andromeda_future_collision_merger(rng: random.Random) -> Dict[str, Any]:
    time_bn = rng.choice(["4 to 5 billion years", "approximately 4,5 billion years"])
    prompt = (
        f"Measurements show that the Andromeda Galaxy and the Milky Way are hurtling toward each other at ~110 km/s, destined to collide in **{time_bn}**.\n\n"
        "During this titanic galactic collision, why will individual stars almost NEVER collide with one another?"
    )
    correct = "Because the physical distances between individual stars in a galaxy are unimaginably vast compared to the physical diameters of the stars themselves."
    options = [
        correct,
        "Because stars are made of pure energy and pass through each other like ghostly light beams.",
        "Because magnetic repulsion between solar flares pushes all stars away before they touch.",
        "Because the collision will be deflected by astronauts using nuclear rocket propulsion."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Stellar sparsity analogy:\n"
        "If stars were scaled to the size of tennis balls, the nearest star would be thousands of kilometers away!\n"
        "Step 2: Collision mechanics:\n"
        "Galactic collisions are mergers of interstellar gas and gravitational fields. Interstellar gas clouds collide and ignite massive starbursts, but stellar collisions are virtually zero. The two galaxies will eventually merge into a single giant elliptical galaxy ('Milkomeda')."
    )
    return {
        "id": f"ns8_bss_34_{rng.randint(100000, 999999)}",
        "subskill": "34_milky_way_andromeda_future_collision_merger",
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
            "tier_1": "Think about the vast empty space between stars.",
            "tier_2": "Interstellar space is so vast that individual stars pass right by each other.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["galactic_collision_star_sparsity"]
    }


def arch_35_local_group_gravitationally_bound_galaxy_cluster(rng: random.Random) -> Dict[str, Any]:
    count = rng.choice(["over 54", "more than 50", "around 54 to 80"])
    prompt = (
        f"Astronomers designate our immediate cosmic neighbourhood the **Local Group**, a gravitationally bound cluster spanning ~10 million light years and containing {count} galaxies.\n\n"
        "Which three galaxies are the dominant major spirals anchoring the mass of the Local Group?"
    )
    correct = "The Andromeda Galaxy (M31), the Milky Way Galaxy, and the Triangulum Galaxy (M33)."
    options = [
        correct,
        "The Sun, Jupiter, and Saturn.",
        "The Sombrero Galaxy, the Whirlpool Galaxy, and the Cartwheel Galaxy.",
        "Alpha Centauri A, Alpha Centauri B, and Proxima Centauri."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Structure of the Local Group:\n"
        "The Local Group contains ~54–80 galaxies, most of which are dwarf spheroidal and irregular satellite galaxies.\n"
        "Step 2: Dominant trio:\n"
        "Over 95% of the total mass is contained in three spiral galaxies: Andromeda (M31), the Milky Way, and Triangulum (M33)."
    )
    return {
        "id": f"ns8_bss_35_{rng.randint(100000, 999999)}",
        "subskill": "35_local_group_gravitationally_bound_galaxy_cluster",
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
            "tier_1": "Which three spiral galaxies dominate our Local Group?",
            "tier_2": "Andromeda, Milky Way, and Triangulum.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["local_group_dominant_spiral_galaxies"]
    }


def arch_36_virgo_cluster_dense_galaxy_concentration(rng: random.Random) -> Dict[str, Any]:
    dist_mly = rng.choice([54, 50, 55])
    gal_count = rng.choice(["1 000 to 2 000 galaxies", "over 1 300 galaxies"])
    prompt = (
        f"Located approximately {dist_mly} million light years from Earth, the **Virgo Cluster** is a gargantuan concentration containing {gal_count}.\n\n"
        "What role does the massive Virgo Cluster play in the larger architecture of our region of the universe?"
    )
    correct = "It forms the dense gravitational heart of the Virgo Supercluster, exerting powerful gravitational attraction on surrounding galaxy groups (including our Local Group)."
    options = [
        correct,
        "It acts as a cosmic mirror reflecting the light of the Sun back to Mars.",
        "It is an artificial space laboratory built to shelter stars from solar flares.",
        "It is a single supergiant star that exploded during the reign of ancient Egypt."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Virgo Cluster scale:\n"
        f"Located ~{dist_mly} million light years away, housing 1 000–2 000 galaxies dominated by giant ellipticals (like M87).\n"
        "Step 2: Gravitational dominance:\n"
        "The Virgo Cluster is the primary gravitational center of our surrounding supercluster, causing the 'Virgocentric flow' where nearby groups are gravitationally drawn toward it."
    )
    return {
        "id": f"ns8_bss_36_{rng.randint(100000, 999999)}",
        "subskill": "36_virgo_cluster_dense_galaxy_concentration",
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
            "tier_1": "Is the Virgo Cluster the gravitational heart of our local supercluster?",
            "tier_2": "Yes, it houses 1 000-2 000 galaxies at the heart of our supercluster.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["virgo_cluster_gravitational_center"]
    }


def arch_37_laniakea_supercluster_our_cosmic_home(rng: random.Random) -> Dict[str, Any]:
    diam_mly = rng.choice(["520 million light years", "approximately 500 million light years"])
    prompt = (
        f"In 2014, astronomers mapped our home supercluster, naming it **Laniakea** (Hawaiian for 'immense heaven'), spanning {diam_mly} and containing ~100 000 galaxies.\n\n"
        "What gravitational feature defines the boundary of Laniakea?"
    )
    correct = "The watershed of gravitational flow: all 100 000 galaxies within Laniakea's boundary are flowing inward toward a central gravitational anomaly called the Great Attractor."
    options = [
        correct,
        "A physical wall of solid diamond separating our galaxy from outer space.",
        "A zone where gravity ceases to exist and all stars travel in circles.",
        "A perimeter marked by communication satellites launched from South Africa."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Definition of Laniakea:\n"
        "Defined by gravitational velocity stream-lines (analogous to water flow in a continental river basin).\n"
        "Step 2: Great Attractor:\n"
        "All galaxies within Laniakea's 520-million-light-year basin are moving toward a common gravitational center called the Great Attractor."
    )
    return {
        "id": f"ns8_bss_37_{rng.randint(100000, 999999)}",
        "subskill": "37_laniakea_supercluster_our_cosmic_home",
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
            "tier_1": "What defines Laniakea like a river drainage basin?",
            "tier_2": "The inward flow of galaxies toward the Great Attractor.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["laniakea_supercluster_gravitational_watershed"]
    }


def arch_38_cosmic_web_filaments_walls_and_giant_voids(rng: random.Random) -> Dict[str, Any]:
    comp_obj = rng.choice(["soapy foam with thin bubble walls", "a complex biological neural network of brain cells"])
    prompt = (
        f"When cosmologists map millions of galaxies on the largest cosmic scales, the overall architecture resembles {comp_obj}, known as the **Cosmic Web**.\n\n"
        "What two primary structural components constitute the Cosmic Web?"
    )
    correct = "Dense interconnected filaments and walls populated by galaxy clusters, surrounding enormous, virtually empty cosmic voids."
    options = [
        correct,
        "Concentric solid rings made of concrete spaced exactly 1 AU apart.",
        "A single straight line of stars connecting the North Star to Earth.",
        "A flat chessboard grid where each square holds exactly one star."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Cosmic Web structure:\n"
        "Gravity amplified tiny density fluctuations from the early universe.\n"
        "Step 2: Components:\n"
        "Matter collapsed along intersecting sheets and filaments (where galaxy superclusters thrive), leaving colossal empty regions (voids spanning 100+ million light years) containing almost zero galaxies."
    )
    return {
        "id": f"ns8_bss_38_{rng.randint(100000, 999999)}",
        "subskill": "38_cosmic_web_filaments_walls_and_giant_voids",
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
            "tier_1": "What are the two main parts of the cosmic web?",
            "tier_2": "Luminous filaments of galaxies and enormous dark empty voids.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["cosmic_web_filaments_and_voids"]
    }


def arch_39_observable_universe_definition_and_event_horizon(rng: random.Random) -> Dict[str, Any]:
    age_gyr = rng.choice(["13,8 billion years", "approximately 13,8 billion years"])
    prompt = (
        f"Because the universe has an age of approximately {age_gyr} and light travels at a finite speed, humans can only observe a finite portion called the **observable universe**.\n\n"
        "Why can we NOT see objects located beyond the boundary of the observable universe?"
    )
    correct = "Because light emitted by objects beyond that boundary has not had enough time to travel across space to reach Earth since the Big Bang began."
    options = [
        correct,
        "Because outer space is blocked by a giant physical wall built by ancient aliens.",
        "Because our telescopes lack electrical batteries to magnify beyond that point.",
        "Because objects outside the boundary are completely made of invisible liquid nitrogen."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Finite age and speed of light:\n"
        "The universe is ~13,8 billion years old; light speed c is 300 000 km/s.\n"
        "Step 2: Particle horizon:\n"
        "Any celestial body whose light requires more than 13,8 billion years to reach us lies beyond our cosmological horizon. We cannot observe it because its photons are still in transit."
    )
    return {
        "id": f"ns8_bss_39_{rng.randint(100000, 999999)}",
        "subskill": "39_observable_universe_definition_and_event_horizon",
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
            "tier_1": "Why can't we see farther than light has traveled since the Big Bang?",
            "tier_2": "The light hasn't had enough time to reach us yet.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["observable_universe_particle_horizon"]
    }


def arch_40_observable_universe_scale_93_billion_light_years(rng: random.Random) -> Dict[str, Any]:
    diam_gly = rng.choice(["93 billion light years", "approximately 93 billion light years"])
    gal_estimate = rng.choice(["up to 2 trillion (2 × 10¹²)", "estimated between 100 billion and 2 trillion"])
    prompt = (
        f"While the universe is 13,8 billion years old, the current diameter of the observable universe is **{diam_gly}**, containing {gal_estimate} galaxies.\n\n"
        "Why is the diameter of the observable universe 93 billion light years instead of just 27,6 billion light years (2 × 13,8)?"
    )
    correct = "Because the fabric of space itself has been expanding continuously during the 13,8 billion years that the light was traveling, stretching the distance to the emitting objects."
    options = [
        correct,
        "Because light accelerates to thousands of times its normal speed when passing through black holes.",
        "Because astronomers multiplied the number by four to account for metric conversions.",
        "Because telescopes curve light rays to make space appear four times wider."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Cosmological expansion:\n"
        "Space is not a static stage; space itself expands according to General Relativity.\n"
        "Step 2: Comoving distance:\n"
        "When light left distant objects 13 billion years ago, they were close. As light traveled toward us, cosmological expansion carried those objects much farther away, placing the current edge of the observable universe at a radius of ~46,5 billion light years (diameter ~93 billion ly)."
    )
    return {
        "id": f"ns8_bss_40_{rng.randint(100000, 999999)}",
        "subskill": "40_observable_universe_scale_93_billion_light_years",
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
            "tier_1": "What happened to the space between galaxies while light was traveling?",
            "tier_2": "The space itself expanded continuously.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["expansion_of_space_observable_universe_scale"]
    }


def arch_41_cosmic_expansion_hubble_law_space_stretching(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In 1929, Edwin Hubble published observations proving that almost all distant galaxies are receding away from the Milky Way, with recession speed proportional to distance (Hubble's Law).\n\n"
        "What fundamental insight about the universe does Hubble's Law reveal?"
    )
    correct = "The universe is expanding: space itself is stretching between galaxies like raisins in a rising loaf of baking bread."
    options = [
        correct,
        "The Milky Way is repelling other galaxies using an enormous electro-gravitational beam.",
        "All other galaxies are rushing toward a massive collision with Earth next month.",
        "The universe is shrinking and collapsing toward an instant gravitational crunch."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Hubble's Law:\n"
        "v = H₀ × d (Recession velocity = Hubble constant × distance).\n"
        "Step 2: Expanding space:\n"
        "Galaxies are not flying through pre-existing empty space like shrapnel from an explosion; space itself is expanding in all directions, causing the separation distance between unbound clusters to increase uniformly."
    )
    return {
        "id": f"ns8_bss_41_{rng.randint(100000, 999999)}",
        "subskill": "41_cosmic_expansion_hubble_law_space_stretching",
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
            "tier_1": "What is expanding: galaxies moving through space, or space itself stretching?",
            "tier_2": "Space itself is stretching between galaxies.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hubble_law_cosmic_expansion"]
    }


def arch_42_cosmological_redshift_stretching_light_waves(rng: random.Random) -> Dict[str, Any]:
    color_shift = rng.choice(["redshift", "cosmological redshift"])
    prompt = (
        f"When astronomers analyze the spectral absorption lines of distant galaxies, they observe a pronounced **{color_shift}** (lines shifted toward longer wavelengths).\n\n"
        "What causes this shift in the wavelengths of light coming from distant galaxies?"
    )
    correct = "As photons travel across expanding space over billions of years, their wavelengths are physically stretched by the expansion of the fabric of spacetime."
    options = [
        correct,
        "Distant stars burn red coal rather than white-hot hydrogen gas.",
        "Cosmic dust paints all light red as it passes through the solar system.",
        "Telescope mirrors absorb blue light and convert it into red paint."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Cosmological redshift vs Doppler effect:\n"
        "While Doppler shift occurs when an emitter moves through space, cosmological redshift occurs because the space through which light travels is actively expanding.\n"
        "Step 2: Wavelength stretching:\n"
        "As spacetime stretches, the wavelength λ of the photon stretches proportionally, moving light toward the longer, red end of the spectrum (z = Δλ / λ₀)."
    )
    return {
        "id": f"ns8_bss_42_{rng.randint(100000, 999999)}",
        "subskill": "42_cosmological_redshift_stretching_light_waves",
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
            "tier_1": "What happens to the wavelength of light as the space it travels through stretches?",
            "tier_2": "The wavelength lengthens (shifts toward red).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["cosmological_redshift_space_stretching"]
    }


def arch_43_big_bang_origin_13_point_8_billion_years(rng: random.Random) -> Dict[str, Any]:
    years_ago = rng.choice(["13,8 billion years ago", "approximately 13,8 billion years ago"])
    prompt = (
        f"Modern astrophysical evidence indicates that our universe began {years_ago} in a monumental event known as the **Big Bang**.\n\n"
        "Which statement accurately describes what the Big Bang actually was?"
    )
    correct = "The rapid expansion of space, time, and matter outward from an unimaginably hot, dense initial state, creating the universe itself."
    options = [
        correct,
        "A conventional bomb exploding inside an already existing, infinitely large empty room.",
        "Two rocky planets colliding together to create all the stars in one afternoon.",
        "A nuclear rocket collision that occurred in orbit around Mars."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Nature of the Big Bang:\n"
        "The Big Bang was not an explosion OF matter INTO pre-existing empty space.\n"
        "Step 2: Creation of spacetime:\n"
        "It was the sudden expansion OF space itself, originating from a singularity of near-infinite density and temperature ~13,8 billion years ago, which created time, space, and fundamental energy/particles."
    )
    return {
        "id": f"ns8_bss_43_{rng.randint(100000, 999999)}",
        "subskill": "43_big_bang_origin_13_point_8_billion_years",
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
            "tier_1": "Did the Big Bang explode into empty space or did it create space itself?",
            "tier_2": "It was the rapid expansion of space and time itself from a hot, dense state.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["big_bang_nature_expansion_of_space"]
    }


def arch_44_cosmic_microwave_background_radiation_relic_glow(rng: random.Random) -> Dict[str, Any]:
    temp = rng.choice(["2,7 Kelvin (-270,45 °C)", "approximately 2,7 Kelvin"])
    prompt = (
        f"The **Cosmic Microwave Background (CMB)** radiation is a faint glow of microwave energy filling all of space, cooled to a temperature of {temp}.\n\n"
        "Why is the CMB radiation considered the most decisive observational proof of the Big Bang?"
    )
    correct = "It is the ancient thermal afterglow emitted approximately 380 000 years after the Big Bang when the cooling universe first became transparent to light."
    options = [
        correct,
        "It is microwave radiation produced by home kitchen appliances on Earth bouncing off the clouds.",
        "It is radar signals transmitted by aliens living on the surface of Jupiter.",
        "It is heat radiating from molten lava rivers on the Moon."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Recombination era:\n"
        "For ~380 000 years after the Big Bang, the universe was a dense, opaque plasma of free electrons and protons.\n"
        "Step 2: Cosmic afterglow:\n"
        "Once temperatures cooled to ~3 000 K, electrons bound to protons to form neutral hydrogen, allowing photons to decouple and travel freely. Over 13,8 billion years of cosmic expansion, this bright flash has stretched into cold microwave radiation at 2,725 K."
    )
    return {
        "id": f"ns8_bss_44_{rng.randint(100000, 999999)}",
        "subskill": "44_cosmic_microwave_background_radiation_relic_glow",
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
            "tier_1": "What relic glow from the early universe fills all of space?",
            "tier_2": "The Cosmic Microwave Background (CMB).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["cmbr_big_bang_relic_proof"]
    }


def arch_45_dark_matter_invisible_mass_holding_galaxies(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice(["85%", "over 80%"])
    prompt = (
        f"Astronomers calculate that approximately {pct} of all the matter in the universe consists of **dark matter**.\n\n"
        "Why is this mysterious substance termed 'dark matter', and how do scientists know it exists if it cannot be seen?"
    )
    correct = "It emits, absorbs, and reflects zero electromagnetic radiation (light), but its existence is proven by its immense gravitational pull on rotating galaxies and light paths."
    options = [
        correct,
        "It is black paint floating in space that absorbs all laser pointers from Earth.",
        "It is composed of dead trees and dark volcanic ash drifted from prehistoric Earth.",
        "It is an illusion caused by dirt on the lenses of astronomical telescopes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Flat rotation curves (Vera Rubin):\n"
        "Stars at the outer edges of spiral galaxies orbit at the same high speed as inner stars, which would cause galaxies to fly apart unless held by a massive invisible halo of mass.\n"
        "Step 2: Gravitational evidence:\n"
        "Because dark matter does not interact with the electromagnetic force, it emits no light; however, its mass exerts strong gravitational pull detectable via orbital speeds and gravitational lensing."
    )
    return {
        "id": f"ns8_bss_45_{rng.randint(100000, 999999)}",
        "subskill": "45_dark_matter_invisible_mass_holding_galaxies",
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
            "tier_1": "Does dark matter emit light or does it only exert gravity?",
            "tier_2": "It emits no light, but exerts massive gravitational influence.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["dark_matter_gravitational_evidence"]
    }


def arch_46_gravitational_lensing_bending_light_around_mass(rng: random.Random) -> Dict[str, Any]:
    lens_x = rng.choice([250, 240, 260])
    stroke_w = rng.choice([2, 3])
    svg = (
        f'<svg viewBox="0 0 500 240" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="500" height="240" fill="#0B132B"/>'
        f'<circle cx="50" cy="120" r="12" fill="#FDE047"/>'
        f'<text x="50" y="95" fill="#FDE047" font-size="11" text-anchor="middle">Distant Galaxy</text>'
        f'<circle cx="{lens_x}" cy="120" r="28" fill="#475569"/>'
        f'<text x="{lens_x}" y="170" fill="#94A3B8" font-size="11" text-anchor="middle">Massive Cluster (Lens)</text>'
        f'<circle cx="450" cy="120" r="10" fill="#38BDF8"/>'
        f'<text x="450" y="95" fill="#38BDF8" font-size="11" text-anchor="middle">Observer (Earth)</text>'
        f'<path d="M 50 120 Q {lens_x} 40 450 120" fill="none" stroke="#F59E0B" stroke-width="{stroke_w}"/>'
        f'<path d="M 50 120 Q {lens_x} 200 450 120" fill="none" stroke="#F59E0B" stroke-width="{stroke_w}"/>'
        f'<text x="250" y="30" fill="#F59E0B" font-size="11" text-anchor="middle">Bent Light Path</text>'
        f'</svg>'
    )
    prompt = (
        "Albert Einstein's General Theory of Relativity predicts the phenomenon of **gravitational lensing**.\n\n"
        "How does a massive galaxy cluster act as a gravitational lens for light coming from a more distant background galaxy?"
    )
    correct = "The intense mass of the intervening cluster warps spacetime around it, bending the light rays from the background galaxy into magnified arcs or multiple images."
    options = [
        correct,
        "The cluster acts like an ordinary glass mirror, bouncing the light straight back to its original source.",
        "The cluster absorbs the photons and fires them out in straight radioactive beams toward Earth.",
        "The cluster polarizes radio waves to create static interference on terrestrial radios."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: General Relativity principle:\n"
        "Mass warps spacetime. Photons travel along geodesics (straightest possible paths through curved spacetime).\n"
        "Step 2: Gravitational lens effect:\n"
        "When light passes near a massive cosmic object (like a galaxy cluster), the curved spacetime bends the path of light, creating magnified, distorted arcs (Einstein rings) visible to observers on Earth."
    )
    return {
        "id": f"ns8_bss_46_{rng.randint(100000, 999999)}",
        "subskill": "46_gravitational_lensing_bending_light_around_mass",
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
            "tier_1": "Does massive gravity bend the spacetime through which light travels?",
            "tier_2": "Yes, curving light rays into magnified arcs and multiple images.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["gravitational_lensing_spacetime_curvature"]
    }


def arch_47_dark_energy_accelerating_universal_expansion(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice(["68%", "roughly 68%"])
    prompt = (
        f"In 1998, observations of distant Type Ia supernovae revealed that the expansion of the universe is not slowing down under gravity, but is accelerating. Cosmologists attribute this to **dark energy**, which constitutes approximately {pct} of the universe.\n\n"
        "What fundamental effect does dark energy exert on the universe on cosmic scales?"
    )
    correct = "It acts as a repulsive pressure across empty space, causing the expansion rate of the universe to accelerate over time."
    options = [
        correct,
        "It acts as attractive gravity, pulling all galaxies together into a rapid Big Crunch.",
        "It turns off the nuclear fusion in all stars, causing instant planetary ice ages.",
        "It generates electrical currents that disrupt mobile phone networks on Earth."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Discovery of accelerated expansion:\n"
        "Distant standard-candle Type Ia supernovae were fainter than expected in a decelerating universe.\n"
        "Step 2: Role of dark energy:\n"
        "Dark energy is a smooth, pervasive energy component of the vacuum that exerts negative pressure, driving an ever-accelerating expansion of the cosmos."
    )
    return {
        "id": f"ns8_bss_47_{rng.randint(100000, 999999)}",
        "subskill": "47_dark_energy_accelerating_universal_expansion",
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
            "tier_1": "Does dark energy speed up or slow down cosmic expansion?",
            "tier_2": "It drives the accelerated expansion of the universe.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["dark_energy_accelerated_expansion"]
    }


def arch_48_galaxy_zoo_citizen_science_crowdsourced_astronomy(rng: random.Random) -> Dict[str, Any]:
    proj = "Galaxy Zoo"
    count = rng.choice(["hundreds of thousands of volunteers", "over 300 000 citizen science volunteers"])
    prompt = (
        f"The groundbreaking astronomy project **{proj}** enlisted {count} worldwide to inspect digital images from robotic sky surveys.\n\n"
        "What specific task did these citizen scientists perform, and why was human eyesight superior to computers in this research?"
    )
    correct = "They classified the morphological shapes of over a million distant galaxies; human eyes excelled at recognizing subtle visual patterns and oddities that early algorithms missed."
    options = [
        correct,
        "They mined asteroids remotely using handheld joysticks connected to orbiting spacecraft.",
        "They calculated the trajectory of Apollo 11 using manual pencil and paper.",
        "They constructed physical glass telescope mirrors in their home workshops."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Galaxy Zoo citizen science:\n"
        "Launched in 2007 with images from the Sloan Digital Sky Survey (SDSS).\n"
        "Step 2: Human pattern recognition:\n"
        "Volunteers classified galaxy shapes (spiral arms, smooth ellipticals, mergers). Human visual cortex excels at pattern matching and spotting unexpected anomalies (like Hanny's Voorwerp), advancing machine learning training sets."
    )
    return {
        "id": f"ns8_bss_48_{rng.randint(100000, 999999)}",
        "subskill": "48_galaxy_zoo_citizen_science_crowdsourced_astronomy",
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
            "tier_1": "What did volunteers classify in Galaxy Zoo?",
            "tier_2": "The shapes and morphologies of distant galaxies.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["galaxy_zoo_citizen_science_morphology"]
    }


def arch_49_salt_telescope_sutherland_dark_sky_advantage(rng: random.Random) -> Dict[str, Any]:
    town = "Sutherland in the Northern Cape Karoo"
    mirror_diam = rng.choice(["11 meters across", "an 11-meter hexagonal primary mirror array"])
    prompt = (
        f"South Africa hosts the **Southern African Large Telescope (SALT)** located near {town}, featuring {mirror_diam}.\n\n"
        "What key environmental conditions in the Karoo make Sutherland an ideal world-class astronomical site?"
    )
    correct = "Extremely dark skies free from urban light pollution, very low humidity and cloud cover, and clean, high-altitude atmospheric stability."
    options = [
        correct,
        "Frequent tropical downpours and rainstorms that wash cosmic dust off the telescope lenses.",
        "High levels of city neon streetlights that illuminate the mirrors at midnight.",
        "Location at sea level surrounded by dense coastal sea spray and fog."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Astronomical seeing requirements:\n"
        "Optical observatories require minimal atmospheric turbulence, clear skies, and darkness.\n"
        "Step 2: Sutherland advantage:\n"
        "Located at 1 798 m altitude in the semi-arid Karoo, Sutherland provides over 300 clear nights per year with negligible light pollution, protected by the Astronomy Geographic Advantage Act."
    )
    return {
        "id": f"ns8_bss_49_{rng.randint(100000, 999999)}",
        "subskill": "49_salt_telescope_sutherland_dark_sky_advantage",
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
            "tier_1": "Why build giant telescopes in the Karoo?",
            "tier_2": "Dark, unpolluted, dry skies with stable air.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["salt_observatory_sutherland_dark_sky"]
    }


def arch_50_beyond_solar_system_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    obj, trait, cause = rng.choice([
        ("Spiral galaxy arms", "intense blue coloration", "rapid formation of short-lived, hot massive young stars"),
        ("Elliptical galaxies", "predominantly yellow-red coloration", "absence of cold gas, leaving only ancient long-lived cool stars"),
        ("Cosmic microwave background", "temperature cooled to 2,7 Kelvin", "stretching of radiation wavelengths by 13,8 billion years of cosmic expansion"),
        ("Distant galaxy spectra", "redshifted absorption lines", "expansion of intervening space stretching light waves during transit")
    ])
    prompt = (
        f"**Comprehensive Cosmic Diagnostic:**\n"
        f"Astronomers analyzing deep space observe that **{obj}** consistently exhibit **{trait}**.\n\n"
        f"What underlying physical mechanism accounts for this observed phenomenon?"
    )
    correct = cause
    options = [
        correct,
        "deliberate radio signaling by extraterrestrial spacecraft in low Earth orbit",
        "artificial colored filters installed inside commercial smartphone cameras",
        "the gravitational pull of the Moon refracting light across the horizon"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Diagnostic phenomenon:\n"
        f"{obj} display {trait}.\n"
        f"Step 2: Fundamental astrophysical cause:\n"
        f"This occurs because of: {cause}."
    )
    return {
        "id": f"ns8_bss_50_{rng.randint(100000, 999999)}",
        "subskill": "50_beyond_solar_system_comprehensive_diagnostic_autopsy",
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
            "tier_1": f"What causes {trait} in {obj}?",
            "tier_2": f"Review the astrophysics: {cause[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["beyond_solar_system_diagnostic_autopsy"]
    }


BUILDERS_26_50 = {
    "26_hubble_galaxy_classification_system_overview": arch_26_hubble_galaxy_classification_system_overview,
    "27_spiral_galaxies_morphology_and_star_formation": arch_27_spiral_galaxies_morphology_and_star_formation,
    "28_barred_spiral_galaxies_milky_way_classification": arch_28_barred_spiral_galaxies_milky_way_classification,
    "29_elliptical_galaxies_characteristics_and_stellar_population": arch_29_elliptical_galaxies_characteristics_and_stellar_population,
    "30_irregular_galaxies_chaotic_structure_and_gas_content": arch_30_irregular_galaxies_chaotic_structure_and_gas_content,
    "31_lenticular_galaxies_intermediate_lens_structure": arch_31_lenticular_galaxies_intermediate_lens_structure,
    "32_large_and_small_magellanic_clouds_satellite_galaxies": arch_32_large_and_small_magellanic_clouds_satellite_galaxies,
    "33_andromeda_galaxy_m31_distance_and_characteristics": arch_33_andromeda_galaxy_m31_distance_and_characteristics,
    "34_milky_way_andromeda_future_collision_merger": arch_34_milky_way_andromeda_future_collision_merger,
    "35_local_group_gravitationally_bound_galaxy_cluster": arch_35_local_group_gravitationally_bound_galaxy_cluster,
    "36_virgo_cluster_dense_galaxy_concentration": arch_36_virgo_cluster_dense_galaxy_concentration,
    "37_laniakea_supercluster_our_cosmic_home": arch_37_laniakea_supercluster_our_cosmic_home,
    "38_cosmic_web_filaments_walls_and_giant_voids": arch_38_cosmic_web_filaments_walls_and_giant_voids,
    "39_observable_universe_definition_and_event_horizon": arch_39_observable_universe_definition_and_event_horizon,
    "40_observable_universe_scale_93_billion_light_years": arch_40_observable_universe_scale_93_billion_light_years,
    "41_cosmic_expansion_hubble_law_space_stretching": arch_41_cosmic_expansion_hubble_law_space_stretching,
    "42_cosmological_redshift_stretching_light_waves": arch_42_cosmological_redshift_stretching_light_waves,
    "43_big_bang_origin_13_point_8_billion_years": arch_43_big_bang_origin_13_point_8_billion_years,
    "44_cosmic_microwave_background_radiation_relic_glow": arch_44_cosmic_microwave_background_radiation_relic_glow,
    "45_dark_matter_invisible_mass_holding_galaxies": arch_45_dark_matter_invisible_mass_holding_galaxies,
    "46_gravitational_lensing_bending_light_around_mass": arch_46_gravitational_lensing_bending_light_around_mass,
    "47_dark_energy_accelerating_universal_expansion": arch_47_dark_energy_accelerating_universal_expansion,
    "48_galaxy_zoo_citizen_science_crowdsourced_astronomy": arch_48_galaxy_zoo_citizen_science_crowdsourced_astronomy,
    "49_salt_telescope_sutherland_dark_sky_advantage": arch_49_salt_telescope_sutherland_dark_sky_advantage,
    "50_beyond_solar_system_comprehensive_diagnostic_autopsy": arch_50_beyond_solar_system_comprehensive_diagnostic_autopsy,
}
