"""Natural Sciences Grade 9 Term 4: Birth, Life and Death of a Star Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 3/07. Birth life and the death of a star.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. stellar_nebulae_and_gravitational_collapse: Stellar nurseries, gravitational contraction of hydrogen/dust, protostar formation.
2. nuclear_fusion_stellar_engine: Core thermonuclear fusion (4^1H -> ^4He + Energy) and hydrostatic equilibrium.
3. star_color_surface_temperature_relationship: Color-temperature scale (Red cool 3000 K -> Yellow 6000 K -> Blue hot 25000 K).
4. lifecycle_of_medium_stars_our_sun: Sun lifecycle: Nebula -> Main Sequence -> Red Giant -> Planetary Nebula -> White Dwarf.
5. massive_star_death_supernova_black_hole: High-mass star evolution: Red Supergiant -> Supernova -> Neutron Star or Black Hole.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Birth, life and the death of a star"
ORDERED_SUBSKILLS = [
    "stellar_nebulae_and_gravitational_collapse",
    "nuclear_fusion_stellar_engine",
    "star_color_surface_temperature_relationship",
    "lifecycle_of_medium_stars_our_sun",
    "massive_star_death_supernova_black_hole",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_bld"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any], term: int = 4) -> Dict[str, Any]:
    if "marking_guide" not in res and "marking_schema" in res:
        res["marking_guide"] = res["marking_schema"]
    elif "marking_schema" not in res and "marking_guide" in res:
        res["marking_schema"] = res["marking_guide"]
    res["grade"] = "9"
    res["term"] = term
    return res


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "practice",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    if subskill in ("mixed", "auto", "", None):
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: Stellar Nebulae and Gravitational Collapse
    if chosen_subskill == "stellar_nebulae_and_gravitational_collapse":
        question_text = (
            "Stars are not permanent fixtures of the cosmos; they are born, evolve, and eventually die over billions of years.\n\n"
            "1. Define a **stellar nebula** and identify the two primary chemical elements that constitute interstellar gas clouds.\n"
            "2. Describe the physical mechanism of **gravitational collapse** that causes a nebula to begin transforming into a star.\n"
            "3. Explain what a **protostar** is, and describe how its central core temperature increases as it contracts.\n"
            "4. What critical core temperature (in Kelvin or degrees Celsius) must a protostar achieve before true stellar life begins?"
        )
        sample = (
            "1. **Stellar Nebula Definition & Composition:** A colossal interstellar cloud of gas and dust in space acting as a stellar nursery. "
            "It is composed predominantly of **Hydrogen (approx 74%)** and **Helium (approx 24%)**, with trace cosmic dust particles;\n"
            "2. **Gravitational Collapse Mechanism:** A shockwave (from a nearby supernova or galactic collision) compresses the gas cloud. "
            "As density increases, the mutual gravitational attraction between gas atoms pulls particles closer together. "
            "Gravitational potential energy is converted into kinetic energy and intense thermal heat as the core compresses;\n"
            "3. **Protostar Formation:** A protostar is an early, dense embryonic mass of gas that has not yet initiated nuclear fusion. "
            "As gravity continues to compress the gas into an ever-smaller volume, particle collisions become increasingly frequent and violent, causing central core temperature and pressure to skyrocket;\n"
            "4. **Ignition Threshold Temperature:** The core must reach approximately **10 to 15 million Kelvin (15 000 000 °C)** for electrostatic repulsion between positively charged hydrogen protons to be overcome, igniting thermonuclear fusion."
        )
        marking = (
            "• 2 marks: Nebula defined (gas/dust cloud in space) [1], composed of Hydrogen and Helium [1]\n"
            "• 2 marks: Mutual gravitational pull compresses gas [1], converts gravitational potential energy into heat [1]\n"
            "• 1 mark: Protostar defined as hot condensing gas core before fusion [1]\n"
            "• 1 mark: Ignition threshold of 10 to 15 million Kelvin [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Stellar Nurseries: Nebulae & Protostar Gravitational Collapse",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Nebulae are clouds of hydrogen and helium gas.",
                "Gravity pulls gas together, heating the core into a protostar.",
                "Nuclear fusion starts when the core reaches 15 million Kelvin.",
            ],
            "misconception_tags": ["stars_burn_by_chemical_fire_myth", "stars_exist_forever_myth"],
            "learning_objective_id": "NS9.PE.24.01",
        })

    # Subskill 2: Nuclear Fusion Stellar Engine
    if chosen_subskill == "nuclear_fusion_stellar_engine":
        question_text = (
            "The powerhouse that fuels all main sequence stars is nuclear fusion in the stellar core.\n\n"
            "1. State the fundamental nuclear fusion reaction equation representing the conversion of hydrogen into helium inside a main sequence star:\n"
            "   *4 ¹H → ⁴He + Energy*.\n"
            "2. Explain the origin of the colossal **energy released** during this nuclear reaction (refer to mass defect and Einstein's equation, E = mc²).\n"
            "3. Contrast **nuclear fusion** occurring in stars with **chemical combustion** (such as burning coal or wood on Earth).\n"
            "4. Explain the principle of **Hydrostatic Equilibrium**: How does a stable star balance the opposing forces of gravity and thermal radiation pressure?"
        )
        sample = (
            "1. **Nuclear Fusion Equation:**\n"
            "   **4 ¹H → ⁴He + Energy**  (Four hydrogen nuclei / protons fuse to form one helium nucleus, releasing energy);\n"
            "2. **Origin of Energy (Mass Defect):** The final mass of one helium-4 nucleus is slightly less (about 0.7% lighter) than the total mass of the four original hydrogen protons. "
            "This tiny lost mass (mass defect, Δm) is directly converted into enormous radiant electromagnetic energy according to Einstein's mass-energy equation, **E = Δm · c²** (where c is the speed of light);\n"
            "3. **Nuclear Fusion vs Chemical Combustion:**\n"
            "   • **Chemical Combustion:** Only rearranges outer atomic electrons and breaks chemical molecular bonds; atomic nuclei remain unchanged; produces modest energy;\n"
            "   • **Nuclear Fusion:** Alchemically alters the atomic nucleus itself, converting mass into energy; releases millions of times more energy per kilogram than any chemical fuel;\n"
            "4. **Hydrostatic Equilibrium:** A star maintains stable size through an exact balance of two opposing forces:\n"
            "   • **Inward Force:** Immense gravity attempting to crush the star inward;\n"
            "   • **Outward Force:** Colossal thermal radiation pressure produced by core nuclear fusion pushing outward.\n"
            "As long as fuel lasts, these two forces cancel out in perfect equilibrium."
        )
        marking = (
            "• 1 mark: Reaction equation: 4 ¹H → ⁴He + Energy [1]\n"
            "• 2 marks: Mass defect (helium is lighter than 4 protons) [1], mass converted to energy via E = mc² [1]\n"
            "• 1 mark: Nuclear alters nuclei releasing millions of times more energy than chemical electron bonds [1]\n"
            "• 2 marks: Inward gravitational pull [1] balanced by outward thermal radiation pressure (hydrostatic equilibrium) [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Thermonuclear Fusion Engine & Hydrostatic Equilibrium",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Stars fuse 4 hydrogen nuclei into 1 helium nucleus.",
                "Energy comes from lost mass using E = mc².",
                "Hydrostatic equilibrium means inward gravity equals outward radiation pressure.",
            ],
            "misconception_tags": ["stars_burn_oxygen_and_coal_myth", "fusion_destroys_energy_myth"],
            "learning_objective_id": "NS9.PE.24.02",
        })

    # Subskill 3: Star Color Surface Temperature Relationship
    if chosen_subskill == "star_color_surface_temperature_relationship":
        stars_data = [
            ("Betelgeuse (Red Supergiant in Orion)", "Red", "Cool", "3 000 K", "Lowest surface temperature among visible stars"),
            ("Our Sun (G-type yellow dwarf)", "Yellow", "Medium", "5 800 K", "Moderate surface temperature sustaining Earth life"),
            ("Sirius A (White star in Canis Major)", "White", "Hot", "9 940 K", "Very hot luminous main sequence star"),
            ("Rigel (Blue-white Supergiant in Orion)", "Blue", "Extremely hot", "25 000 K", "Fiercely hot star radiating intense ultraviolet radiation"),
        ]
        s_target = stars_data[actual_seed % len(stars_data)]
        question_text = (
            "When stargazers observe the night sky, stars exhibit subtle colours ranging from deep red to brilliant blue.\n\n"
            "1. State what physical property of a star directly determines its visible colour.\n"
            "2. Complete the star colour and surface temperature progression from **coolest to hottest**:\n"
            "   *Red → Orange → Yellow → White → Blue*.\n"
            f"3. Classify the star **{s_target[0]}**:\n"
            f"   • State its characteristic visible colour: *{s_target[1]}*.\n"
            f"   • State its approximate surface temperature category: *{s_target[2]} (approx {s_target[3]})*.\n"
            "4. Why does everyday domestic intuition (where red faucet taps denote hot and blue denotes cold) reverse the actual physics of stellar temperatures?"
        )
        sample = (
            "1. **Physical Property:** A star's color is directly governed by its **surface temperature** (blackbody thermal radiation / Wien's Law);\n"
            "2. **Color-Temperature Sequence (Coolest to Hottest):**\n"
            "   1. **Red:** Coolest stars (~3 000 K)\n"
            "   2. **Orange:** Cool stars (~4 500 K)\n"
            "   3. **Yellow:** Medium stars (~5 800 K, like our Sun)\n"
            "   4. **White:** Hot stars (~10 000 K)\n"
            "   5. **Blue:** Extremely hot stars (~20 000 to 40 000 K);\n"
            f"3. **Star Classification ({s_target[0]}):** Color: **{s_target[1]}**; Temperature: **{s_target[2]}** (~{s_target[3]});\n"
            "4. **Domestic Intuition vs Physics:** In domestic plumbing, red symbolizes hot water and blue cold water. "
            "In thermodynamics, however, as an object heats up, its thermal peak shifts to shorter, higher-energy wavelengths: glowing dull red first, then yellow, white, and finally radiant blue (highest energy photons)."
        )
        marking = (
            "• 1 mark: Surface temperature dictates color [1]\n"
            "• 2 marks: Correct progression from Red (coolest) to Blue (hottest) [2]\n"
            f"• 2 marks: Color ({s_target[1]}) [1], Temperature range ({s_target[3]}) [1]\n"
            "• 1 mark: Physics: higher temperature emits shorter wavelength blue light (highest energy) [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": f"Star Colour vs Temperature: {s_target[0].split(' (')[0]}",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Red is the COOLEST star (~3000 K).",
                "Yellow is medium (~6000 K, like our Sun).",
                "Blue is the HOTTEST star (>20000 K). Physics is the opposite of bathroom tap colors!",
            ],
            "misconception_tags": ["red_stars_are_the_hottest_myth", "blue_stars_are_frozen_myth"],
            "learning_objective_id": "NS9.PE.24.03",
        })

    # Subskill 4: Lifecycle of Medium Stars (Our Sun)
    if chosen_subskill == "lifecycle_of_medium_stars_our_sun":
        question_text = (
            "Our Sun is a medium-sized yellow dwarf star with an estimated total lifespan of approximately 10 billion years.\n\n"
            "1. State the **current stage** of our Sun's life cycle and its current estimated age (approx 4.6 billion years).\n"
            "2. Describe what will occur to the Sun in approximately 5 billion years when its core hydrogen fuel is completely exhausted:\n"
            "   • What stage does it expand into? (Red Giant)\n"
            "   • What happens to inner planets like Mercury, Venus, and Earth?\n"
            "3. Explain what a **planetary nebula** is and how the dying Sun will form one.\n"
            "4. Describe the final remnant core left behind: What is a **White Dwarf**, what is it composed of, and what does it eventually become?"
        )
        sample = (
            "1. **Current Solar Stage & Age:** The Sun is in the **Main Sequence** stage, stably fusing hydrogen into helium in its core. "
            "It is approximately **4.6 billion years old** (about halfway through its 10-billion-year lifespan);\n"
            "2. **Hydrogen Exhaustion & Red Giant Stage:**\n"
            "   • When core hydrogen runs out, core fusion ceases, gravity compresses the core, and surrounding hydrogen shells ignite;\n"
            "   • The Sun's outer layers expand hundreds of times outwards into a colossal **Red Giant**;\n"
            "   • The expanding red giant will completely swallow Mercury and Venus, and vaporize Earth's oceans and biosphere, leaving Earth an incinerated cinder;\n"
            "3. **Planetary Nebula Formation:** The unstable pulsating Red Giant gently expels its entire glowing outer atmosphere into deep space as an expanding, luminescent ring of gas called a **Planetary Nebula**, enriching space with carbon and oxygen;\n"
            "4. **White Dwarf Remnant:**\n"
            "   • The remaining exposed stellar core contracts into a **White Dwarf** (an Earth-sized, scorching ball of carbon and oxygen with immense density where a teaspoon weighs tons);\n"
            "   • Because no fusion occurs, it slowly cools over tens of billions of years into a cold, dark, inert **Black Dwarf**."
        )
        marking = (
            "• 2 marks: Main Sequence [1], 4.6 billion years old (approx halfway) [1]\n"
            "• 2 marks: Expands into a Red Giant [1], engulfs inner planets/Earth [1]\n"
            "• 1 mark: Outer gas layers ejected as expanding planetary nebula [1]\n"
            "• 2 marks: White Dwarf (dense Earth-sized carbon core) [1], cools to Black Dwarf [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": "Solar Lifecycle: Main Sequence to Red Giant & White Dwarf",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Our Sun is a 4.6 billion-year-old Main Sequence star.",
                "In 5 billion years, it will swell into a Red Giant and swallow the inner planets.",
                "It will shed a planetary nebula and end as an Earth-sized White Dwarf.",
            ],
            "misconception_tags": ["the_sun_will_explode_as_a_supernova_myth", "the_sun_will_become_a_black_hole_myth"],
            "learning_objective_id": "NS9.PE.24.04",
        })

    # Subskill 5: Massive Star Death: Supernova and Black Hole
    question_text = (
        "Stars with masses greater than 8 to 20 times the mass of our Sun experience violent, cataclysmic deaths.\n\n"
        "1. Contrast the lifespan of a **massive blue supergiant star** with that of our medium-mass Sun, explaining why massive stars live for only millions of years rather than billions.\n"
        "2. Explain what causes the catastrophic explosion of a **Type II Supernova** when iron forms in the stellar core.\n"
        "3. Explain why astronomers say that **'we are made of stardust'**: What happens to elements heavier than iron (such as gold, iodine, and uranium) during a supernova?\n"
        "4. Differentiate between the two possible remnants of a supernova:\n"
        "   • A **Neutron Star (Pulsar)**\n"
        "   • A **Black Hole**"
    )
    sample = (
        "1. **Lifespan Contrast:** Massive blue stars live for only **a few tens of millions of years** (compared to the Sun's 10 billion years). "
        "Their immense gravitational weight exerts crushing pressures on their cores, forcing them to burn through their nuclear fuel at a hyper-accelerated rate;\n"
        "2. **Supernova Core Collapse:** Massive stars fuse progressively heavier elements (C, O, Ne, Mg, Si) until an **iron core (Fe)** forms. "
        "Fusing iron absorbs energy rather than releasing it, immediately starving the star of outward radiation pressure. "
        "Gravity crushes the core in a fraction of a second; the outer layers collapse onto the rigid core and rebound in a colossal **Supernova explosion** that outshines a whole galaxy;\n"
        "3. **'We are Stardust' (Cosmic Nucleosynthesis):** The extraordinary heat and neutron flux during a supernova explosion synthesize all elements heavier than iron (gold, silver, platinum, uranium) "
        "and blasts them across space. These shockwaves seed new nebulae, meaning the carbon, oxygen, calcium in our bones, and iron in our blood originated in ancient stellar explosions;\n"
        "4. **Remnants:**\n"
        "   • **Neutron Star:** Formed if core mass is 1.4–3 solar masses; protons and electrons are crushed together into pure neutrons (a 20 km city-sized sphere spinning rapidly as a Pulsar);\n"
        "   • **Black Hole:** Formed if core mass exceeds 3 solar masses; gravity is so overwhelming that the core collapses to an infinitesimal point of infinite density (singularity) where gravity is so strong that not even light can escape."
    )
    marking = (
        "• 1 mark: Massive stars live short lives (millions of years) because they burn fuel hyper-fast [1]\n"
        "• 2 marks: Iron fusion absorbs energy [1], radiation pressure fails, core collapses and rebounds as supernova [1]\n"
        "• 2 marks: Heavy elements (gold, uranium) forged in supernova [1], blasted into space to seed planets/human atoms [1]\n"
        "• 2 marks: Neutron star (city-sized sphere of pure neutrons) [1] vs Black hole (singularity where not even light escapes) [1]\n"
        "**Total: 7 marks**"
    )
    return _normalize_res({
        "title": "Massive Star Cataclysms: Supernovae, Neutron Stars & Black Holes",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 4,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            "Massive stars burn fuel fast and live short lives.",
            "When the core makes iron, fusion stops and the star explodes as a Supernova.",
            "Supernovae forge heavy elements like gold. The leftover core becomes a Neutron Star or Black Hole.",
        ],
        "misconception_tags": ["all_stars_become_black_holes_myth", "black_holes_are_giant_vacuum_cleaners_in_space_myth"],
        "learning_objective_id": "NS9.PE.24.05",
    })
