"""Senior Phase Earth & Space Astronomy Generator (Grades 7, 8, & 9 Natural Sciences).

Complies with the 6-pillar South African CAPS contract:
- Term & calendar metadata (Term 4 Planet Earth and Beyond)
- Deconstructible compound and elementary sub-drills
- Standardized misconception taxonomy
- Teacher-editable marking schema
- Deterministic 3-tier pre-baked hints
- South African comma decimal convention
"""

import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float, decimals: int = 2) -> str:
    """Formats a float using South African comma decimal convention."""
    if abs(val - round(val)) < 1e-6:
        return str(int(round(val)))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    return f"{prefix}_{seed or 'rnd'}_{idx}"


def _generate_gr7_earth_moon_sun(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 7 NS Term 4: Earth tilt, seasons, moon phases, and tides."""
    hemisphere = r.choice(["Southern Hemisphere", "Northern Hemisphere"])
    month = r.choice(["December", "June"])

    qid = _make_id("ns7_astronomy", seed, idx)

    if mode == "elementary_tides_lunar_phase":
        tide_type = r.choice(["Spring tide", "Neap tide"])
        if tide_type == "Spring tide":
            phases = "New Moon and Full Moon"
            explanation = "The gravitational pull of the Sun and Moon act along the same straight line, producing the highest high tides and lowest low tides."
        else:
            phases = "First Quarter and Third Quarter"
            explanation = "The gravitational pull of the Sun and Moon act at right angles (90 degrees) to each other, resulting in the lowest tidal range."

        prompt = (
            f"Tides on Earth are caused by the gravitational attraction of the Moon and the Sun on the oceans.\n\n"
            f"1. During which TWO phases of the Moon do **{tide_type}s** occur?\n"
            f"2. Explain why the tidal range is at its maximum/minimum during a {tide_type}."
        )
        ans_str = f"1. {phases}; 2. {explanation}"
        memo = (
            f"1. Moon phases for {tide_type} [2]: {phases}. [2]\n"
            f"2. Gravitational alignment explanation [2]: {explanation} [2]"
        )
        hints = {
            "tier_1": "Spring tides occur when Sun, Earth, and Moon are aligned in a straight line. Neap tides occur at 90 degree angles.",
            "tier_2": "New and Full Moon align forces (Spring). Quarter moons cancel part of each other's pull (Neap).",
            "tier_3": f"Phases: {phases}. {explanation}",
        }
        marks = 4
    else:
        # Compound
        if hemisphere == "Southern Hemisphere":
            season = "Summer" if month == "December" else "Winter"
            tilt_dir = "tilted towards the Sun" if month == "December" else "tilted away from the Sun"
            day_length = "longer daylight hours and shorter nights" if month == "December" else "shorter daylight hours and longer nights"
        else:
            season = "Winter" if month == "December" else "Summer"
            tilt_dir = "tilted away from the Sun" if month == "December" else "tilted towards the Sun"
            day_length = "shorter daylight hours and longer nights" if month == "December" else "longer daylight hours and shorter nights"

        prompt = (
            f"The Earth orbits the Sun once every $365{{,}}25$ days with its rotational axis tilted at an angle of $23{{,}}5^\\circ$ relative to its orbital plane.\n\n"
            f"1. State the main cause of the changing seasons on Earth.\n"
            f"2. In {month}, the {hemisphere} is {tilt_dir}.\n"
            f"   a) Identify the season experienced in South Africa ({hemisphere}) during {month}.\n"
            f"   b) Describe the relative length of days compared to nights in the {hemisphere} during this month.\n"
            f"   c) Explain how the angle of the Sun's rays affects the heating of the Earth's surface during this season.\n"
            f"3. Common Misconception: A learner claims that summer occurs because the Earth is physically closer to the Sun in its orbit. State whether this claim is TRUE or FALSE, and provide a scientific reason for your answer."
        )
        ans_str = (
            f"1. The 23.5 degree tilt of Earth's axis as it revolves around the Sun; "
            f"2. a) {season}, b) {day_length}, c) Direct rays concentrate solar energy over smaller area; "
            f"3. FALSE. Earth's distance changes very little; Southern Hemisphere summer occurs when Earth is tilted towards the Sun."
        )
        memo = (
            f"1. Cause of seasons [2]: The tilt of Earth's rotational axis ($23{{,}}5^\\circ$) as the Earth orbits the Sun. [2]\n"
            f"2. {month} conditions [4]:\n"
            f"   a) Season in {hemisphere}: {season} [1]\n"
            f"   b) Daylight length: {day_length} [1]\n"
            f"   c) Solar heating: In {season.lower()}, the Sun's rays strike the surface more directly (at a higher angle), concentrating solar radiation over a smaller surface area, leading to warmer temperatures. [2]\n"
            f"3. Refutation of distance myth [2]: FALSE [1]. The Earth's orbit is nearly circular; in fact, the Earth is closest to the Sun (perihelion) in early January when the Northern Hemisphere is experiencing winter. [1]"
        )
        hints = {
            "tier_1": "Seasons are caused by Earth's 23.5 degree tilt, NOT by distance from the Sun.",
            "tier_2": "When a hemisphere tilts towards the Sun, sunlight strikes more directly and days are longer.",
            "tier_3": f"Season: {season}. Day length: {day_length}. The distance claim is completely FALSE.",
        }
        marks = 8

    return {
        "id": qid,
        "question_id": qid,
        "term": 4,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": [
            "seasons_caused_by_distance_to_sun",
            "spring_tide_season_confusion",
            "confused_solar_with_lunar_eclipse",
        ],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Axis tilt cause of seasons", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Season and daylight duration", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Solar ray concentration angle", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Scientific refutation of distance misconception", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr8_solar_system_beyond(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 8 NS Term 4: Solar system and light year distances."""
    star_name = r.choice(["Proxima Centauri", "Sirius", "Alpha Centauri A", "Vega"])
    dist_ly = r.choice([4.2, 8.6, 4.4, 25.0])
    c_kms = 300000.0  # km/s
    sec_per_year = 365.25 * 24 * 3600
    one_ly_km = c_kms * sec_per_year  # ~ 9.467e12 km
    total_dist_km = dist_ly * one_ly_km

    qid = _make_id("ns8_astronomy", seed, idx)

    if mode == "elementary_light_year_calc":
        prompt = (
            f"Astronomers use the **light year** as a standard unit of measurement for distances beyond our Solar System.\n\n"
            f"1. Define the term *light year*.\n"
            f"2. Misconception Check: Is a light year a unit of time or a unit of distance?\n"
            f"3. The speed of light is approximately $300{{,}}000\\text{{ km/s}}$. Calculate the approximate distance light travels in one year (1 light year) in kilometers."
        )
        ans_str = (
            f"1. Distance light travels in vacuum in one Julian year; "
            f"2. Unit of distance; "
            f"3. ~ 9.46 x 10^12 km"
        )
        memo = (
            f"1. Definition [1]: The distance that light travels in a vacuum in one year ($365{{,}}25$ days). [1]\n"
            f"2. Physical quantity [1]: It is a unit of **distance**, not time. [1]\n"
            f"3. Distance calculation [2]:\n"
            f"   $$\\text{{Distance}} = \\text{{Speed}} \\times \\text{{Time}} = (300{{,}}000\\text{{ km/s}}) \\times (365{{,}}25 \\times 24 \\times 3600\\text{{ s}})$$\n"
            f"   $$\\text{{Distance}} \\approx 9{{,}}46 \\times 10^{{12}}\\text{{ km}}$$ [M+A]"
        )
        hints = {
            "tier_1": "Even though it has the word 'year', a light year measures astronomical distance.",
            "tier_2": "Calculate seconds in a year: 365.25 * 24 * 60 * 60. Then multiply by 300 000 km/s.",
            "tier_3": "1 light year = 9.46 x 10^12 km. It is a unit of distance.",
        }
        marks = 4
    else:
        prompt = (
            f"Our Solar System consists of the Sun, eight planets, dwarf planets, asteroids, and comets.\n\n"
            f"1. Classify the eight planets into two main groups: terrestrial (rocky) planets and gas giants.\n"
            f"2. Name the region located between Mars and Jupiter that contains thousands of rocky fragments.\n"
            f"3. The star **{star_name}** is located ${_fmt_sa(dist_ly)}\\text{{ light years}}$ from Earth.\n"
            f"   a) How many years does light emitted by {star_name} take to reach our eyes on Earth?\n"
            f"   b) If {star_name} were to explode today, explain when astronomers on Earth would observe the explosion."
        )
        ans_str = (
            f"1. Terrestrial: Mercury, Venus, Earth, Mars; Gas giants: Jupiter, Saturn, Uranus, Neptune; "
            f"2. The Asteroid Belt; "
            f"3. a) {dist_ly} years, b) In {dist_ly} years from today"
        )
        memo = (
            f"1. Planet classification [2]:\n"
            f"   - Terrestrial (rocky) planets: Mercury, Venus, Earth, Mars [1]\n"
            f"   - Gas giants: Jupiter, Saturn, Uranus, Neptune [1]\n"
            f"2. Region between Mars & Jupiter [1]: The Asteroid Belt. [1]\n"
            f"3. Distance and light travel time [3]:\n"
            f"   a) Light travel time: ${_fmt_sa(dist_ly)}\\text{{ years}} [1]\n"
            f"   b) Because light travels at finite speed ($300{{,}}000\\text{{ km/s}}$), the light carrying the image of the explosion takes ${_fmt_sa(dist_ly)}\\text{{ years}}$ to traverse space. Thus, observers on Earth will only see the explosion ${_fmt_sa(dist_ly)}\\text{{ years}}$ in the future. [2]"
        )
        hints = {
            "tier_1": "The 4 inner planets are rocky; the 4 outer planets are gas giants.",
            "tier_2": "Between Mars and Jupiter lies the asteroid belt. Looking at distant stars means looking back in time.",
            "tier_3": f"Inner: Mercury, Venus, Earth, Mars. Outer: Jupiter, Saturn, Uranus, Neptune. Light takes {dist_ly} years.",
        }
        marks = 6

    return {
        "id": qid,
        "question_id": qid,
        "term": 4,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 7,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["light_year_time_not_distance", "gas_giant_terrestrial_planet_confusion"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Terrestrial and gas giant groupings", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Asteroid belt identification", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Light year travel time reasoning", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr9_stellar_evolution(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 9 NS Term 4: Birth, life, and death of stars."""
    star_category = r.choice(["Sun-like star (average mass)", "Massive star (high mass)"])

    qid = _make_id("ns9_stellar", seed, idx)

    if mode == "elementary_star_lifecycle_stage":
        prompt = (
            "Stars shine by converting mass into radiant energy in their cores.\n\n"
            "1. State the name of the nuclear reaction that powers stars on the main sequence.\n"
            "2. Identify the element that serves as the primary nuclear fuel, and the element produced during this reaction."
        )
        ans_str = "1. Nuclear fusion; 2. Fuel: Hydrogen; Product: Helium"
        memo = (
            "1. Nuclear reaction [1]: Nuclear fusion. [1]\n"
            "2. Fuel & product [2]: Hydrogen nuclei (protons) fuse together to form Helium nuclei, releasing vast amounts of radiant energy. [2]"
        )
        hints = {
            "tier_1": "In the core of a star, light elements join together under extreme pressure and temperature.",
            "tier_2": "Four hydrogen nuclei fuse to form one helium nucleus.",
            "tier_3": "Nuclear fusion of hydrogen into helium.",
        }
        marks = 3
    else:
        if star_category == "Sun-like star (average mass)":
            end_stages = "Red Giant -> Planetary Nebula -> White Dwarf"
            final_remnant = "White dwarf (and eventually a cold black dwarf)"
        else:
            end_stages = "Red Supergiant -> Supernova explosion -> Neutron Star OR Black Hole"
            final_remnant = "Neutron star or Black hole (if mass is extremely high)"

        prompt = (
            f"Stars are formed inside colossal clouds of interstellar gas and dust called nebulae.\n\n"
            f"1. Describe how gravitational collapse inside a nebula leads to the birth of a **protostar**.\n"
            f"2. What condition must be reached in the core of a protostar for nuclear fusion to ignite and form a stable **main sequence star**?\n"
            f"3. Trace the evolutionary stages of a **{star_category}** after it exhausts hydrogen in its core.\n"
            f"4. Name the final remnant left behind by this star: {final_remnant.split('(')[0].strip()}."
        )
        ans_str = (
            f"1. Gravity pulls hydrogen and dust particles together, increasing density and temperature; "
            f"2. Core temperature must reach ~15 million K; "
            f"3. {end_stages}; "
            f"4. {final_remnant}"
        )
        memo = (
            f"1. Birth of protostar [2]: Gravity causes regions within a giant molecular cloud (nebula) to collapse inwards. As matter gathers tightly, gravitational potential energy transforms into thermal energy, forming a hot, glowing protostar. [2]\n"
            f"2. Ignition of fusion [2]: The core temperature must reach approximately 10 to 15 million Kelvin ($15 \\times 10^6\\text{{ K}}$), where kinetic energy overcomes electrostatic repulsion between protons, igniting nuclear fusion. [2]\n"
            f"3. Life cycle sequence for {star_category} [3]:\n"
            f"   $$\\text{{Nebula}} \\to \\text{{Protostar}} \\to \\text{{Main Sequence}} \\to {end_stages}$$ [3]\n"
            f"4. Final remnant [1]: {final_remnant}. [1]"
        )
        hints = {
            "tier_1": "All stars begin in nebulae. Massive stars end in supernovae, while medium stars like the Sun become white dwarfs.",
            "tier_2": f"Trace the pathway for {star_category}: {end_stages}.",
            "tier_3": f"Core reaches ~15 million K. Sequence: {end_stages}. Remnant: {final_remnant}.",
        }
        marks = 8

    return {
        "id": qid,
        "question_id": qid,
        "term": 4,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": [
            "confused_supernova_with_planetary_nebula",
            "confused_nuclear_fission_with_fusion",
            "white_dwarf_neutron_star_confusion",
        ],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Protostar gravitational formation mechanism", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Core temperature threshold for fusion", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Evolutionary pathway stages", "marks": 3, "editable": True},
                {"id": "mp_4", "desc": "Final stellar remnant classification", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "concepts",
    difficulty: str = "medium",
    count: int = 1,
    grade: str = "8",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Earth and Space Astronomy (Grades 7, 8, & 9)."""
    r = random.Random(seed)
    questions = []

    for i in range(count):
        gr_str = str(grade).strip()
        if gr_str == "7":
            q = _generate_gr7_earth_moon_sun(r, seed, i, mode)
        elif gr_str == "9":
            q = _generate_gr9_stellar_evolution(r, seed, i, mode)
        else:
            q = _generate_gr8_solar_system_beyond(r, seed, i, mode)
        questions.append(q)

    return questions
