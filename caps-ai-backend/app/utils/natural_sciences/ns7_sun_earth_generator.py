"""Grade 7 Natural Sciences: Term 4 - Relationship of the Sun to the Earth Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the sun to the Earth.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "earth_rotation_day_and_night",
    "earth_revolution_and_year_length",
    "axial_tilt_and_seasons_mechanics",
    "solstices_and_equinoxes_southern_hemisphere",
    "solar_energy_driving_earth_climate"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the sun to the Earth.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_earth_rotation(rng: random.Random) -> Dict[str, Any]:
    cities = [
        "Cape Town and Durban",
        "Johannesburg and Upington",
        "Polokwane and Port Elizabeth"
    ]
    prompt = (
        f"Learners in {rng.choice(cities)} experience the regular progression from dawn to daylight, sunset, and night.\n\n"
        f"What astronomical motion causes the cycle of **day and night** on Earth, "
        f"and how long does one complete cycle take?"
    )
    correct_opt = "Earth's rotation on its own internal axis once every 24 hours."
    options = [
        correct_opt,
        "Earth's orbital revolution around the Sun once every 365.25 days.",
        "The Sun physically travelling in a circle around the equator every 12 hours.",
        "The Moon passing in front of the Sun once every 28 days."
    ]
    rng.shuffle(options)
    sol = (
        "Day and Night Mechanics:\n"
        "Earth spins (rotates) from west to east on its imaginary axis. It takes 24 hours (1 day) to complete "
        "one 360° rotation. The side facing the Sun experiences daylight, while the side facing away experiences darkness (night)."
    )
    return {
        "id": f"ns7_sun_rot_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "earth_rotation_day_and_night",
        "question_family_id": "earth_rotation_day_and_night",
        "hints": {
            "tier_1": "Rotation on its axis causes day/night; revolution around the sun causes years.",
            "tier_2": "Rotation takes 24 hours.",
            "tier_3": "Earth rotating on its axis once every 24 hours."
        },
        "misconception_tags": ["rotation_revolution_confusion"]
    }

def _build_earth_revolution(rng: random.Random) -> Dict[str, Any]:
    intros = [
        "While spinning once every 24 hours on its axis, Earth also journeys continuously along its orbital path around the Sun.",
        "Civil calendars organize our yearly schedule based on the Earth's complete orbit around the Sun.",
        "Astronomical observations reveal that Earth's orbital period around the Sun is slightly more than 365 days."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"How long does it take for Earth to complete ONE full **revolution (orbit)** around the Sun, "
        f"and why do we have a leap year every four years?"
    )
    correct_opt = "365 and 1/4 days (365.25 days): The four quarter-days add up to one extra day (February 29) every four years."
    options = [
        correct_opt,
        "Exactly 300 days: The leap year compensates for summer holidays.",
        "24 hours: Earth completes one orbit around the Sun every single day.",
        "28 days: Earth matches the exact revolution period of the Moon."
    ]
    rng.shuffle(options)
    sol = (
        "Revolution and Leap Years:\n"
        "1. Earth takes 365 days, 5 hours, 48 minutes, and 46 seconds (~365.25 days) to orbit the Sun.\n"
        "2. A calendar year has 365 days. The leftover ~0.25 days (6 hours) per year accumulates to 24 hours (1 full day) every 4 years, added as February 29 (Leap Year)."
    )
    return {
        "id": f"ns7_sun_rev_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "earth_revolution_and_year_length",
        "question_family_id": "earth_revolution_and_year_length",
        "hints": {
            "tier_1": "How many days in a normal year plus leap year compensation?",
            "tier_2": "It takes 365.25 days; four quarters equal one extra leap day.",
            "tier_3": "365 and 1/4 days, producing a leap year every 4 years."
        },
        "misconception_tags": ["leap_year_calendar_myth"]
    }

def _build_axial_tilt_seasons(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        "South African families celebrate December holidays on sunny beaches while European countries experience freezing winter snow",
        "Free State maize farmers experience peak summer heat in December while North American farms are frozen in winter",
        "South Africa experiences long daylight hours and high solar temperatures in December, contrasted with short chilly days in June"
    ]
    prompt = (
        f"Consider the seasonal observation that {rng.choice(scenarios)}.\n\n"
        f"Explain scientifically why South Africa experiences **summer** in December and **winter** in June. "
        f"Reference Earth's axial tilt and angle of sunlight in your answer. (4 marks)"
    )
    sample_answer = (
        "1. Earth's axis is tilted at an angle of 23.5° relative to its orbital plane around the Sun.\n"
        "2. In December (Summer in SA): The Southern Hemisphere is tilted towards the Sun. Sunlight strikes South Africa at a steep, direct angle (concentrating heat energy over a smaller surface area), and daylight hours are longer than night.\n"
        "3. In June (Winter in SA): The Southern Hemisphere is tilted away from the Sun. Sunlight strikes at a shallow, slanted angle (spreading solar energy over a much larger area), and daylight hours are shorter."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Earth's axis is tilted at 23.5° as it orbits the Sun (1 mark).\n"
        "2. Summer (Dec): Southern Hemisphere tilts toward Sun -> direct, concentrated sunlight and longer days (2 marks).\n"
        "3. Winter (June): Southern Hemisphere tilts away from Sun -> slanted, spread-out sunlight and shorter days (1 mark)."
    )
    return {
        "id": f"ns7_sun_tilt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "axial_tilt_and_seasons_mechanics",
        "question_family_id": "axial_tilt_and_seasons_mechanics",
        "hints": {
            "tier_1": "Seasons are caused by Earth's 23.5 degree tilt, NOT distance from the Sun.",
            "tier_2": "When tilted toward the sun, rays strike directly (summer); when tilted away, rays are slanted (winter).",
            "tier_3": "Explain 23.5 degree tilt, direct concentrated rays in December, and slanted rays in June."
        },
        "misconception_tags": ["seasons_distance_to_sun_fallacy"]
    }

def _build_solstices_equinoxes(rng: random.Random) -> Dict[str, Any]:
    events = [
        ("Summer Solstice in South Africa (around 21 December)", "the longest day and shortest night of the year in the Southern Hemisphere, with the Sun directly overhead at the Tropic of Capricorn"),
        ("Winter Solstice in South Africa (around 21 June)", "the shortest day and longest night of the year in the Southern Hemisphere, with the Sun directly overhead at the Tropic of Cancer in the north"),
        ("Autumn Equinox in South Africa (around 21 March)", "day and night are of equal duration (12 hours day, 12 hours night) as the Sun is directly overhead at the Equator"),
        ("Spring Equinox in South Africa (around 22 September)", "day and night are of equal duration (12 hours each) worldwide as the Sun crosses the Equator heading south")
    ]
    ev_name, desc = rng.choice(events)
    prompt = f"Which seasonal astronomical event in South Africa is defined as:\n'{desc}'?"
    correct_opt = ev_name
    distractors = [e[0] for e in events if e[0] != ev_name]
    options = [correct_opt] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand solstices and equinoxes:\n"
        f"- Solstice ('sun stands still'): Extreme day length (Dec 21 = longest day; June 21 = shortest day in SA).\n"
        f"- Equinox ('equal night'): Exactly 12 hours day and 12 hours night (March 21 and Sept 22).\n\n"
        f"Conclusion: '{desc}' defines {ev_name}."
    )
    return {
        "id": f"ns7_sun_solst_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "solstices_and_equinoxes_southern_hemisphere",
        "question_family_id": "solstices_and_equinoxes_southern_hemisphere",
        "hints": {
            "tier_1": "Equinox = equal day and night; Solstice = extreme day length.",
            "tier_2": "Dec 21 is summer solstice in SA; June 21 is winter solstice.",
            "tier_3": f"This event is {ev_name}."
        },
        "misconception_tags": ["hemisphere_solstice_inversion"]
    }

def _build_solar_energy_climate(rng: random.Random) -> Dict[str, Any]:
    phenomena = [
        "summer afternoon convection thunderstorms over Gauteng and the Highveld",
        "gale-force southeasterly winds blowing across False Bay in the Western Cape",
        "the warm Agulhas ocean current flowing southward along the eastern coast of South Africa"
    ]
    prompt = (
        f"Meteorologists study climate phenomena such as {rng.choice(phenomena)}.\n\n"
        f"Why is solar radiation from the Sun considered the primary engine driving Earth's weather, winds, and ocean currents?"
    )
    correct_opt = "Unequal heating of Earth's surface (warm equator vs cold poles) causes density and pressure differences that drive atmospheric winds and ocean currents."
    options = [
        correct_opt,
        "Solar radiation pushes the continents like physical conveyor belts across the oceans.",
        "The Sun burns liquid oxygen in the clouds to create thunderstorms.",
        "Solar energy stops rain by evaporating all water from the oceans permanently."
    ]
    rng.shuffle(options)
    sol = (
        "Solar Energy and Global Climate Systems:\n"
        "Because Earth is curved, equatorial regions receive direct, intense solar heating, whereas polar regions receive "
        "spread-out, slanted sunlight. This thermal gradient creates warm, rising air at the equator and cold, sinking air at the poles, "
        "generating global atmospheric wind belts and driving major ocean conveyor currents."
    )
    return {
        "id": f"ns7_sun_clim_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "solar_energy_driving_earth_climate",
        "question_family_id": "solar_energy_driving_earth_climate",
        "hints": {
            "tier_1": "Think about how unequal heating of the equator vs poles creates wind.",
            "tier_2": "Warm air rises at equator and cool air sinks at poles, creating winds and currents.",
            "tier_3": "Unequal heating causes pressure and density differences driving winds and currents."
        },
        "misconception_tags": ["uniform_solar_heating_myth"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    if "solar_system" in target:
        from app.utils.natural_sciences import ns8_solar_system_seasons_generator as ns8_solar
        return ns8_solar.generate(subskill=subskill, count=count, seed=seed, **kwargs)
    builders = {
        "earth_rotation_day_and_night": _build_earth_rotation,
        "earth_revolution_and_year_length": _build_earth_revolution,
        "axial_tilt_and_seasons_mechanics": _build_axial_tilt_seasons,
        "solstices_and_equinoxes_southern_hemisphere": _build_solstices_equinoxes,
        "solar_energy_driving_earth_climate": _build_solar_energy_climate
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
