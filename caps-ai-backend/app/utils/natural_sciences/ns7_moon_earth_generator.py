"""Grade 7 Natural Sciences: Term 4 - Relationship of the Moon to the Earth Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the moon to the earth.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "moon_orbit_and_revolution_period",
    "lunar_phases_sequence_and_causes",
    "ocean_tides_spring_and_neap",
    "lunar_and_solar_eclipses_mechanics",
    "gravity_and_weight_on_the_moon"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the moon to the earth.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_moon_orbit(rng: random.Random) -> Dict[str, Any]:
    intros = [
        "The Moon is Earth's only natural satellite, gravitationally bound in an elliptical path.",
        "Night sky observers across southern Africa record the Moon's orbital movement against background constellations.",
        "Astronomers measure the cyclical phases of the Moon as it completes its orbit around the Earth."
    ]
    prompt = (
        f"{rng.choice(intros)}\n\n"
        f"Approximately how long does it take for the Moon to complete ONE full orbit (revolution) around the Earth, "
        "and does the Moon emit its own light?"
    )
    correct_opt = "Approximately 28 days (one month): The Moon does not emit light; it reflects sunlight."
    options = [
        correct_opt,
        "Exactly 365.25 days: The Moon burns nuclear fuel like a small star.",
        "Exactly 24 hours: The Moon generates light from hot volcanic magma.",
        "Approximately 12 hours: The Moon is completely transparent to cosmic rays."
    ]
    rng.shuffle(options)
    sol = (
        "Moon Orbital Mechanics:\n"
        "1. The Moon revolves around Earth in an elliptical orbit taking approximately 27.3 to 29.5 days (~28 days / 1 lunar cycle).\n"
        "2. The Moon is a non-luminous rocky body that does not generate its own light; it reflects light from the Sun."
    )
    return {
        "id": f"ns7_moon_orb_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "moon_orbit_and_revolution_period",
        "question_family_id": "moon_orbit_and_revolution_period",
        "hints": {
            "tier_1": "Think about the word 'month' which comes from 'moon'.",
            "tier_2": "The Moon takes ~28 days to orbit and reflects sunlight.",
            "tier_3": "Approximately 28 days, and it reflects sunlight."
        },
        "misconception_tags": ["moon_luminous_body_fallacy"]
    }

def _build_lunar_phases(rng: random.Random) -> Dict[str, Any]:
    phases = [
        ("New Moon", "the Moon is situated between the Earth and the Sun, with its unlit dark side facing Earth", "zero illumination visible from Earth"),
        ("First Quarter", "half of the visible lunar surface is illuminated on the western side one week after New Moon", "half disc illuminated"),
        ("Full Moon", "the Earth is situated between the Sun and Moon, with the fully illuminated lunar surface facing Earth", "complete illuminated disc visible"),
        ("Third (Last) Quarter", "half of the visible lunar surface is illuminated on the eastern side three weeks after New Moon", "waning half disc illuminated")
    ]
    phase_name, desc, view = rng.choice(phases)
    prompt = f"Which phase of the Moon occurs when {desc}?"
    correct_opt = phase_name
    distractors = [p[0] for p in phases if p[0] != phase_name]
    options = [correct_opt] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand lunar phases cause:\n"
        f"Lunar phases are caused by changing angles between Earth, Moon, and Sun as the Moon orbits Earth.\n\n"
        f"Conclusion: '{desc}' describes the {phase_name}."
    )
    return {
        "id": f"ns7_moon_phase_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "lunar_phases_sequence_and_causes",
        "question_family_id": "lunar_phases_sequence_and_causes",
        "hints": {
            "tier_1": "Is the illuminated face completely visible (Full), invisible (New), or half visible (Quarter)?",
            "tier_2": "Look at the alignment of Earth, Moon, and Sun.",
            "tier_3": f"This corresponds to the {phase_name}."
        },
        "misconception_tags": ["earth_shadow_moon_phases_myth"]
    }

def _build_ocean_tides(rng: random.Random) -> Dict[str, Any]:
    tides = [
        ("Spring tides (highest high tides and lowest low tides)", "the Sun, Moon, and Earth align in a straight line (syzygy) during New Moon and Full Moon, combining their gravitational pulls"),
        ("Neap tides (lowest tidal range with moderate high and low tides)", "the Sun and Moon are positioned at right angles (90°) relative to Earth during First and Third Quarter moons, partially cancelling each other's gravitational pull")
    ]
    tide_type, cause = rng.choice(tides)
    prompt = f"What causes **{tide_type}** in Earth's oceans?"
    correct_opt = f"They occur because {cause}."
    alt_tide = tides[1] if tide_type == tides[0][0] else tides[0]
    options = [
        correct_opt,
        f"They occur because {alt_tide[1]}.",
        "They are caused strictly by undersea earthquakes and volcanic eruptions.",
        "They are caused by strong municipal water pumping stations in coastal cities."
    ]
    rng.shuffle(options)
    sol = (
        f"Tidal Mechanics:\n"
        f"- Spring tides: Occur twice a month at New/Full Moon when Sun and Moon gravity combine in line -> maximum tidal range.\n"
        f"- Neap tides: Occur twice a month at Quarter Moons when Sun and Moon pull at 90° -> minimum tidal range.\n\n"
        f"Conclusion: {tide_type} occurs because {cause}."
    )
    return {
        "id": f"ns7_moon_tide_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "ocean_tides_spring_and_neap",
        "question_family_id": "ocean_tides_spring_and_neap",
        "hints": {
            "tier_1": "Spring tides have the biggest tidal range; neap tides have the smallest.",
            "tier_2": "Spring tides align in a line (New/Full Moon); neap tides pull at 90 degrees.",
            "tier_3": f"{tide_type} occurs because {cause}."
        },
        "misconception_tags": ["spring_season_spring_tide_confusion"]
    }

def _build_eclipses(rng: random.Random) -> Dict[str, Any]:
    eclipses = [
        ("A Solar Eclipse", "the Moon passes directly between the Earth and the Sun, casting a shadow (umbra/penumbra) on Earth and blocking sunlight", "Daytime during New Moon"),
        ("A Lunar Eclipse", "the Earth passes directly between the Sun and the Moon, casting Earth's shadow across the lunar surface", "Nighttime during Full Moon")
    ]
    ecl_type, mech, timing = rng.choice(eclipses)
    prompt = f"Explain the astronomical geometry of **{ecl_type}**."
    correct_opt = f"{ecl_type} occurs when {mech} ({timing})."
    alt_ecl = eclipses[1] if ecl_type == eclipses[0][0] else eclipses[0]
    options = [
        correct_opt,
        f"{ecl_type} occurs when {alt_ecl[1]} ({alt_ecl[2]}).",
        "It occurs when the Sun explodes and shrinks for two hours.",
        "It happens when clouds completely cover all seven continents simultaneously."
    ]
    rng.shuffle(options)
    sol = (
        f"Eclipse Mechanics:\n"
        f"- Solar Eclipse: Sun - Moon - Earth. The Moon casts its shadow on Earth.\n"
        f"- Lunar Eclipse: Sun - Earth - Moon. The Earth casts its shadow on the Moon.\n\n"
        f"Conclusion: {ecl_type} occurs when {mech}."
    )
    return {
        "id": f"ns7_moon_ecl_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "lunar_and_solar_eclipses_mechanics",
        "question_family_id": "lunar_and_solar_eclipses_mechanics",
        "hints": {
            "tier_1": "Which body is in the middle: the Moon (solar eclipse) or the Earth (lunar eclipse)?",
            "tier_2": "Solar eclipse = Moon blocks the Sun; Lunar eclipse = Earth shadows the Moon.",
            "tier_3": f"{ecl_type} occurs when {mech}."
        },
        "misconception_tags": ["solar_lunar_eclipse_inversion"]
    }

def _build_gravity_and_weight(rng: random.Random) -> Dict[str, Any]:
    earth_mass = rng.choice([60, 72, 84, 90])
    prompt = (
        f"An astronaut has a mass of {earth_mass} kg on Earth. The Moon has approximately 1/6th of Earth's gravity.\n\n"
        f"What will the astronaut's **mass** and approximate **weight** be on the surface of the Moon? (Take Earth gravity g = 10 N/kg)."
    )
    earth_wt = earth_mass * 10
    moon_wt = earth_wt / 6
    correct_opt = f"Mass: {earth_mass} kg (unchanged) | Weight: approximately {moon_wt:.0f} N (1/6th of Earth weight)"
    options = [
        correct_opt,
        f"Mass: {earth_mass/6:.1f} kg | Weight: {earth_wt} N",
        f"Mass: 0 kg | Weight: 0 N (zero gravity exists on the Moon)",
        f"Mass: {earth_mass * 6} kg | Weight: {moon_wt:.0f} N"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand Mass vs Weight:\n"
        f"- Mass is the amount of matter in an object, measured in kilograms (kg). It never changes regardless of location: Mass = {earth_mass} kg.\n"
        f"- Weight is the gravitational force acting on that mass, measured in Newtons (N): W = m × g.\n\n"
        f"Step 2: Calculate Moon Weight:\n"
        f"Earth weight = {earth_mass} kg × 10 N/kg = {earth_wt} N.\n"
        f"Moon weight = {earth_wt} / 6 = approximately {moon_wt:.0f} N."
    )
    return {
        "id": f"ns7_moon_wt_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "gravity_and_weight_on_the_moon",
        "question_family_id": "gravity_and_weight_on_the_moon",
        "hints": {
            "tier_1": "Mass is the amount of matter and never changes. Weight is gravitational force.",
            "tier_2": f"Mass stays the same ({earth_mass} kg); weight is divided by 6.",
            "tier_3": f"Mass is {earth_mass} kg and weight is ~{moon_wt:.0f} N."
        },
        "misconception_tags": ["mass_weight_confusion", "moon_zero_gravity_myth"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "moon_orbit_and_revolution_period": _build_moon_orbit,
        "lunar_phases_sequence_and_causes": _build_lunar_phases,
        "ocean_tides_spring_and_neap": _build_ocean_tides,
        "lunar_and_solar_eclipses_mechanics": _build_eclipses,
        "gravity_and_weight_on_the_moon": _build_gravity_and_weight
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
