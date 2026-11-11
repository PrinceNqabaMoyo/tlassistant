"""Grade 7 Natural Sciences: Term 4 - Historical Development of Astronomy Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 4/02. Historical development of astronomy.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "indigenous_african_astronomy_and_star_lore",
    "galileo_and_the_telescope_revolution",
    "optical_vs_radio_telescopes",
    "south_african_large_telescope_salt",
    "square_kilometre_array_ska_karoo"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 4/02. Historical development of astronomy.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_indigenous_astronomy(rng: random.Random) -> Dict[str, Any]:
    lores = [
        ("the Pleiades star cluster (known as 'Isilimela' in isiXhosa / isiZulu and 'Selemela' in Sesotho)", "the onset of the agricultural plowing and planting season in spring"),
        ("the Southern Cross (Crux) and its two pointer stars (Alpha and Beta Centauri)", "a celestial navigational compass indicating true south across the African veld at night"),
        ("the morning star (Venus / 'iKhwezi')", "signalling the approaching dawn for rural herders and early morning travelers")
    ]
    celest, role = rng.choice(lores)
    prompt = (
        f"In indigenous South African astronomical knowledge systems, **{celest}** was traditionally used as a celestial calendar for:\n\n"
        f"Which practical cultural or agricultural purpose?"
    )
    correct_opt = f"Signalling {role}."
    options = [
        correct_opt,
        "Determining which minerals to mine in deep shafts.",
        "Predicting modern satellite internet coverage.",
        "Guaranteed warning of undersea tsunamis in the Atlantic ocean."
    ]
    rng.shuffle(options)
    sol = (
        f"Indigenous Knowledge Systems (IKS) in Astronomy:\n"
        f"Long before modern telescopes, African indigenous communities observed patterns in celestial movements "
        f"to manage agriculture, navigation, and ceremonies.\n\n"
        f"Conclusion: {celest} was used for signalling {role}."
    )
    return {
        "id": f"ns7_astro_iks_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "indigenous_african_astronomy_and_star_lore",
        "question_family_id": "indigenous_african_astronomy_and_star_lore",
        "hints": {
            "tier_1": "Think about traditional farming and seasonal stars like Isilimela (Pleiades).",
            "tier_2": "Stars were used to mark planting seasons and guide night navigation.",
            "tier_3": f"It was used for signalling {role}."
        },
        "misconception_tags": ["iks_astronomy_dismissal_bias"]
    }

def _build_galileo_revolution(rng: random.Random) -> Dict[str, Any]:
    intros = [
        "In 1609, Italian astronomer **Galileo Galilei** turned an optical refracting telescope toward the planets.",
        "During the scientific revolution of the 17th century, **Galileo Galilei** used optical lenses to observe the night sky.",
        "When **Galileo Galilei** constructed his astronomical telescope in 1609, he made pioneering celestial observations."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"Which major observational discovery provided definitive evidence supporting Nicolaus Copernicus's heliocentric (Sun-centred) model of the solar system?"
    )
    correct_opt = "He discovered four large moons orbiting Jupiter, proving that not all celestial bodies revolve around the Earth."
    options = [
        correct_opt,
        "He discovered human footprints and artificial roads on the Moon.",
        "He proved that the Sun is made of solid cold granite.",
        "He showed that Earth is completely stationary at the exact center of the universe."
    ]
    rng.shuffle(options)
    sol = (
        "Galilean Discoveries (1609-1610):\n"
        "Galileo discovered the four largest moons of Jupiter (Io, Europa, Ganymede, Callisto). "
        "This disproved the ancient geocentric Ptolemaic model (which held that everything revolved strictly around Earth) "
        "and provided empirical proof supporting Copernicus's heliocentric model."
    )
    return {
        "id": f"ns7_astro_gal_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "galileo_and_the_telescope_revolution",
        "question_family_id": "galileo_and_the_telescope_revolution",
        "hints": {
            "tier_1": "Think about Jupiter's moons.",
            "tier_2": "Seeing moons orbit Jupiter proved that not everything revolves around Earth.",
            "tier_3": "He discovered Jupiter's moons, proving bodies can orbit other planets."
        },
        "misconception_tags": ["geocentric_galileo_confusion"]
    }

def _build_optical_vs_radio(rng: random.Random) -> Dict[str, Any]:
    intros = [
        "Astronomers modernly employ multiple types of telescopes operating across the electromagnetic spectrum.",
        "When scanning distant galaxies and celestial bodies, scientists utilize both optical and radio telescopes.",
        "In modern astronomical observatories, different telescope designs capture different wavelengths of electromagnetic radiation."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"Which statement correctly distinguishes an **optical telescope** from a **radio telescope**?"
    )
    correct_opt = "Optical telescopes collect visible light rays using glass lenses or mirrors; radio telescopes collect long-wavelength radio waves using curved metal dish antennae."
    options = [
        correct_opt,
        "Optical telescopes listen to radio music; radio telescopes shoot visible laser beams into deep space.",
        "Radio telescopes can only operate inside dark underwater submarines.",
        "Both telescopes collect only audible sound waves made by exploding stars."
    ]
    rng.shuffle(options)
    sol = (
        "Types of Astronomical Telescopes:\n"
        "- Optical Telescopes: Capture visible electromagnetic light using glass refractive lenses or primary parabolic mirrors.\n"
        "- Radio Telescopes: Detect invisible, long-wavelength radio emissions from celestial objects using curved parabolic metal dishes."
    )
    return {
        "id": f"ns7_astro_types_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "optical_vs_radio_telescopes",
        "question_family_id": "optical_vs_radio_telescopes",
        "hints": {
            "tier_1": "Optical = visible light; Radio = radio wave frequencies.",
            "tier_2": "Optical uses lenses/mirrors; radio uses metal dish antennae.",
            "tier_3": "Optical collects visible light; radio collects radio waves."
        },
        "misconception_tags": ["radio_telescope_sound_wave_myth"]
    }

def _build_salt_sutherland(rng: random.Random) -> Dict[str, Any]:
    intros = [
        "The **Southern African Large Telescope (SALT)** situated in the Northern Cape is the largest single optical telescope in the Southern Hemisphere.",
        "In astronomical science, South Africa hosts the giant **SALT (Southern African Large Telescope)** observatory plateau.",
        "Engineers and astrophysicists selected the semi-arid Karoo plateau to construct the primary mirror array of **SALT**."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"Give at least THREE geographical and atmospheric reasons why Sutherland in the Karoo was selected as the optimal location for this world-class optical observatory. (4 marks)"
    )
    sample_answer = (
        "1. Dark skies with minimal light pollution: Sutherland has a tiny population and strict lighting bylaws, ensuring dark skies free from city glare.\n"
        "2. Arid climate and low cloud cover: The Karoo has very low rainfall, resulting in cloudless nights for over 75% of the year.\n"
        "3. High elevation: Sutherland sits at approximately 1 800 metres above sea level, placing the telescope above low-lying atmospheric haze and moisture.\n"
        "4. Clean, stable air: Stable atmospheric conditions ensure minimal optical distortion (atmospheric seeing)."
    )
    sol = (
        "Marking Rubric (4 marks total, any 4 points):\n"
        "1. Absence of city light pollution / dark skies (1 mark).\n"
        "2. Dry Karoo climate / high number of cloudless clear nights (1 mark).\n"
        "3. High altitude (1 800 m) above atmospheric moisture and haze (1 mark).\n"
        "4. Stable, unpolluted atmosphere reducing twinkling/distortion (1 mark)."
    )
    return {
        "id": f"ns7_astro_salt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "south_african_large_telescope_salt",
        "question_family_id": "south_african_large_telescope_salt",
        "hints": {
            "tier_1": "Why is the Karoo good for looking at stars through a giant mirror?",
            "tier_2": "Think about darkness, lack of city lights, clear cloudless skies, and high elevation.",
            "tier_3": "Mention zero light pollution, cloudless Karoo nights, high altitude, and clean stable air."
        },
        "misconception_tags": ["telescope_city_center_fallacy"]
    }

def _build_ska_karoo(rng: random.Random) -> Dict[str, Any]:
    intros = [
        "Near Carnarvon in the Northern Cape, South Africa's 64-dish **MeerKAT radio telescope array** is fully operational and gathering world-class astrophysics data as the core precursor to the international **Square Kilometre Array (SKA-Mid)**.",
        "In the radio-quiet Karoo Astronomy Advantage Area, the completed and operational **MeerKAT telescope array** represents the first phase of the global **Square Kilometre Array (SKA)**.",
        "Astronomers worldwide currently observe pulsars, cosmic magnetism, and distant hydrogen gas using South Africa's operational 64-antenna **MeerKAT array**, the operational cornerstone of the **Square Kilometre Array (SKA)**."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"What is the primary scientific purpose and architectural design of the **Square Kilometre Array (SKA)**?"
    )
    correct_opt = "The world's largest and most sensitive radio telescope array, combining thousands of interconnected antennae to explore the early universe."
    options = [
        correct_opt,
        "A nuclear weapons testing site hidden under the desert sands.",
        "A commercial space airport designed for luxury passenger flights to Mars.",
        "A coal-burning power station that supplies electricity to deep-space probes."
    ]
    rng.shuffle(options)
    sol = (
        "The Square Kilometre Array (SKA) Project:\n"
        "The SKA is a massive international scientific mega-project co-hosted by South Africa (Karoo) and Australia. "
        "It connects thousands of mid-frequency radio dish antennae to create an effective collecting area of one square kilometre, "
        "enabling scientists to study the formation of the first stars, dark energy, and cosmic magnetism."
    )
    return {
        "id": f"ns7_astro_ska_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "square_kilometre_array_ska_karoo",
        "question_family_id": "square_kilometre_array_ska_karoo",
        "hints": {
            "tier_1": "It is an international radio telescope project in the Karoo.",
            "tier_2": "It uses thousands of dish antennae to study the early universe.",
            "tier_3": "The world's largest radio telescope array exploring the early universe."
        },
        "misconception_tags": ["ska_optical_confusion"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "indigenous_african_astronomy_and_star_lore": _build_indigenous_astronomy,
        "galileo_and_the_telescope_revolution": _build_galileo_revolution,
        "optical_vs_radio_telescopes": _build_optical_vs_radio,
        "south_african_large_telescope_salt": _build_salt_sutherland,
        "square_kilometre_array_ska_karoo": _build_ska_karoo
    }
    if target in builders:
        return [builders[target](rng) for _ in range(count)]
    for k, fn in builders.items():
        if target and target in k:
            return [fn(rng) for _ in range(count)]
    res = []
    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        res.append(builders[sub](rng))
    return res
