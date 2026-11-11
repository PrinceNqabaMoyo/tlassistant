"""Grade 7 Natural Sciences - Relationship of the Sun to the Earth: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the sun to the Earth.md
Focus: Sun characteristics, distance, light travel time, Earth rotation, day/night cycle, apparent solar motion,
shadows, revolution, leap year, elliptical orbit, axial tilt (23.5°), direct vs indirect light, solstices, equinoxes.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_sun_characteristics_star_fusion(rng: random.Random) -> Dict[str, Any]:
    comp = rng.choice(["hydrogen and helium gases", "hydrogen being fused into helium", "ionized hydrogen and helium plasma"])
    prompt = (
        f"The Sun is the central star of our solar system, composed predominantly of {comp}.\n\n"
        "What fundamental nuclear process within the Sun's core produces its enormous output of heat and light energy?"
    )
    correct = "Nuclear fusion, where hydrogen nuclei fuse together under extreme pressure and temperature to form helium."
    options = [
        correct,
        "Combustion of massive underground coal deposits.",
        "Chemical reaction between liquid petroleum and oxygen gas.",
        "Frictional heating caused by asteroids crashing onto the solar surface."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify the Sun's nature:\n"
        "The Sun is a medium-sized star (yellow dwarf).\n"
        "Step 2: Energy production mechanism:\n"
        "The Sun generates energy through nuclear fusion in its dense core, fusing hydrogen into helium and converting mass into radiant energy."
    )
    return {
        "id": f"ns7_sun_01_{rng.randint(100000, 999999)}",
        "subskill": "01_sun_characteristics_star_fusion",
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
            "tier_1": "Stars do not burn fuel with oxygen like campfires.",
            "tier_2": "Hydrogen atoms fuse together into helium.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sun_chemical_burning_fallacy"]
    }


def arch_02_sun_distance_and_light_travel_time(rng: random.Random) -> Dict[str, Any]:
    speed_km_s = 300000
    dist_million_km = rng.choice([149.6, 150.0, 152.0])
    prompt = (
        f"The average distance from the Earth to the Sun is approximately {dist_million_km} million kilometres (1 Astronomical Unit). "
        f"Given that light travels at roughly {speed_km_s} km/s through space, approximately how long does sunlight take to reach Earth?"
    )
    correct = "Approximately 8.3 minutes (about 500 seconds)"
    options = [
        correct,
        "Instantaneously (0.00 seconds)",
        "Exactly 24 hours",
        "Approximately 365.25 days"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Calculate travel time:\n"
        "Time = Distance ÷ Speed = 150 000 000 km ÷ 300 000 km/s = 500 seconds.\n"
        "Step 2: Convert to minutes:\n"
        "500 seconds ÷ 60 ≈ 8.33 minutes (about 8 minutes and 20 seconds)."
    )
    return {
        "id": f"ns7_sun_02_{rng.randint(100000, 999999)}",
        "subskill": "02_sun_distance_and_light_travel_time",
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
            "tier_1": "Divide 150 million km by light speed (300 000 km/s).",
            "tier_2": "500 seconds is just over 8 minutes.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["instantaneous_light_travel_myth"]
    }


def arch_03_earth_rotation_axis_poles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Earth rotates continuously in space. What is Earth's axis of rotation, and where does it emerge on Earth's surface?"
    )
    correct = "An imaginary line passing straight through Earth's centre between the Geographic North Pole and South Pole."
    options = [
        correct,
        "A solid steel rod physically anchoring Earth to the Moon's core.",
        "An imaginary line running along the Equator from South America to Africa.",
        "A magnetic laser beam connecting Earth to the centre of the Sun."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Define planetary axis:\n"
        "An axis is the imaginary line about which a body rotates.\n"
        "Step 2: Location:\n"
        "Earth's axis passes through the centre of the planet, intersecting the surface at the Geographic North Pole and South Pole."
    )
    return {
        "id": f"ns7_sun_03_{rng.randint(100000, 999999)}",
        "subskill": "03_earth_rotation_axis_poles",
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
            "tier_1": "Think about spinning a globe: what two opposite points does the spindle touch?",
            "tier_2": "The North and South poles.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["physical_axis_misconception"]
    }


def arch_04_earth_rotation_period_24_hours(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice(["360°", "one complete turn", "a full circle"])
    prompt = (
        f"How long does it take for Earth to complete {angle} of rotation on its internal axis?"
    )
    correct = "24 hours (1 solar day)"
    options = [
        "24 hours (1 solar day)",
        "365.25 days (1 year)",
        "28 days (1 month)",
        "12 hours (half a day)"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify rotational period:\n"
        "Earth spins on its axis once every 24 hours.\n"
        "Step 2: Conclusion: One complete 360° rotation constitutes one solar day."
    )
    return {
        "id": f"ns7_sun_04_{rng.randint(100000, 999999)}",
        "subskill": "04_earth_rotation_period_24_hours",
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
            "tier_1": "How many hours are in one day?",
            "tier_2": "Rotation defines the 24-hour day.",
            "tier_3": f"Answer is: {correct}"
        },
        "misconception_tags": ["rotation_vs_revolution_duration_confusion"]
    }


def arch_05_earth_rotation_direction_west_to_east(rng: random.Random) -> Dict[str, Any]:
    perspectives = [
        ("looking down from above the North Pole", "anticlockwise (counter-clockwise)"),
        ("from the viewpoint of an astronaut in space above the equator", "from west to east")
    ]
    p_view, direction = rng.choice(perspectives)
    prompt = (
        f"In which direction does the Earth rotate on its axis ({p_view})?"
    )
    correct = "From west to east (anticlockwise when viewed from above the North Pole)."
    options = [
        correct,
        "From east to west (clockwise when viewed from above the North Pole).",
        "From south to north along lines of longitude.",
        "From north to south towards the Antarctic."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Determine rotational direction:\n"
        "Earth rotates from west to east.\n"
        "Step 2: Effect on apparent celestial motion:\n"
        "Because Earth spins west-to-east, celestial bodies (Sun, Moon, stars) appear to rise in the east and set in the west."
    )
    return {
        "id": f"ns7_sun_05_{rng.randint(100000, 999999)}",
        "subskill": "05_earth_rotation_direction_west_to_east",
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
            "tier_1": "If the Sun appears to move east to west, which way must Earth spin?",
            "tier_2": "Earth spins opposite to the apparent motion: from west to east.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["earth_rotation_direction_inversion"]
    }


def arch_06_day_and_night_cycle_cause(rng: random.Random) -> Dict[str, Any]:
    cities = ["Bloemfontein", "Mbombela", "Kimberley", "Gqeberha"]
    city = rng.choice(cities)
    prompt = (
        f"A family in {city} experiences continuous cycles of daylight followed by nighttime darkness.\n\n"
        "What is the scientific cause of the day and night cycle on Earth?"
    )
    correct = "Earth is a spherical, opaque body rotating on its axis, so only the half facing the Sun receives light at any one moment."
    options = [
        correct,
        "The Sun burns brightly for 12 hours and then switches off to cool down.",
        "Earth's orbital distance from the Sun doubles every night.",
        "Dense space clouds pass between Earth and the Sun every evening."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify optical and geometric properties:\n"
        "Earth is an opaque sphere.\n"
        "Step 2: Explain day/night mechanics:\n"
        "As Earth rotates, the hemisphere turned toward the Sun experiences day. The hemisphere turned away experiences night."
    )
    r_earth = rng.choice([38, 40, 42])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 160" width="100%" height="140"><circle cx="160" cy="80" r="{r_earth}" fill="#1e293b"/><path d="M 160 40 A 40 40 0 0 0 160 120 Z" fill="#38bdf8"/><line x1="20" y1="80" x2="100" y2="80" stroke="#f59e0b" stroke-width="2"/><text x="40" y="70" fill="#f59e0b" font-size="11">Sunlight</text><text x="135" y="85" fill="#0f172a" font-size="10" font-weight="bold">Day</text><text x="175" y="85" fill="#94a3b8" font-size="10">Night</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_sun_06_{rng.randint(100000, 999999)}",
        "subskill": "06_day_and_night_cycle_cause",
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
            "tier_1": "Can light pass through a solid sphere?",
            "tier_2": "Rotation brings each side into and out of sunlight.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["sun_extinguishes_at_night_myth"]
    }


def arch_07_apparent_motion_sun_east_to_west(rng: random.Random) -> Dict[str, Any]:
    time_of_day = rng.choice(["sunrise", "midday", "sunset"])
    prompt = (
        "Each day, the Sun appears to rise in the eastern horizon, arc across the sky, and set in the western horizon.\n\n"
        "Why is this movement described as an **apparent motion** rather than real motion?"
    )
    correct = "The Sun is relatively stationary at the centre of the solar system; Earth's west-to-east rotation creates the illusion that the Sun moves."
    options = [
        correct,
        "The Sun is physically racing across the sky on a giant orbital track around Earth.",
        "The Sun moves because of gravitational attraction from migrating birds.",
        "Earth does not move at all in space, so the Sun's motion must be real."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Distinguish apparent vs actual motion:\n"
        "Apparent motion is motion as perceived by an observer within a moving reference frame (Earth).\n"
        "Step 2: Identify true motion:\n"
        "Earth rotates eastward, making celestial objects appear to drift westward."
    )
    return {
        "id": f"ns7_sun_07_{rng.randint(100000, 999999)}",
        "subskill": "07_apparent_motion_sun_east_to_west",
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
            "tier_1": "Think about looking out of a moving bus window: do trees move or does the bus move?",
            "tier_2": "Earth rotates eastward, causing apparent westward solar motion.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["geocentric_apparent_motion_fallacy"]
    }


def arch_08_solar_noon_shadow_length_and_direction(rng: random.Random) -> Dict[str, Any]:
    pole_h = rng.choice(["a 1-metre vertical stick (gnomon)", "a vertical flagpole", "a fence post"])
    prompt = (
        f"A science class sets up {pole_h} in Pretoria on a sunny day.\n\n"
        "At what time of day will the stick cast its **shortest shadow**, and why?"
    )
    correct = "At solar noon (midday), because the Sun reaches its highest elevation (altitude) in the sky."
    options = [
        correct,
        "At sunrise, because the Sun's rays are brightest.",
        "At sunset, because the temperature is coolest.",
        "At midnight, because there is no light to make a shadow."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Analyze shadow geometry:\n"
        "Shadow length is inversely related to solar elevation angle.\n"
        "Step 2: Apply to solar noon:\n"
        "At solar noon, the Sun is at its maximum daily altitude above the horizon, casting the shortest possible shadow of the day."
    )
    return {
        "id": f"ns7_sun_08_{rng.randint(100000, 999999)}",
        "subskill": "08_solar_noon_shadow_length_and_direction",
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
            "tier_1": "When is the Sun directly overhead or highest?",
            "tier_2": "Highest Sun produces the shortest shadow at midday.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["shadow_length_solar_altitude_misconception"]
    }


def arch_09_shadow_diurnal_progression_morning_to_evening(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "As the Sun progresses across the sky from morning to evening, how do the **length** and **direction** of an outdoor shadow change?"
    )
    correct = "Shadows start long and point west in the morning, become shortest at noon, and grow long pointing east in the late afternoon."
    options = [
        correct,
        "Shadows start short in the morning, become longest at noon, and disappear at sunset.",
        "Shadows always point directly towards the Sun regardless of the time of day.",
        "Shadows remain completely stationary all day long."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Direction of shadow:\n"
        "A shadow always points in the exact opposite direction of the light source (Sun in east -> shadow in west; Sun in west -> shadow in east).\n"
        "Step 2: Length of shadow:\n"
        "Low Sun angle at dawn/dusk creates long shadows; high Sun angle at noon creates short shadows."
    )
    h_gnomon = rng.choice([48, 50, 52])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 140" width="100%" height="130"><line x1="20" y1="110" x2="320" y2="110" stroke="#475569" stroke-width="2"/><line x1="170" y1="110" x2="170" y2="{110 - h_gnomon}" stroke="#0f172a" stroke-width="4"/><text x="170" y="{100 - h_gnomon}" text-anchor="middle" font-size="10">Stick</text><rect x="60" y="110" width="110" height="6" fill="#64748b"/><text x="100" y="130" font-size="10" fill="#64748b">Morning Shadow (West)</text><rect x="170" y="110" width="110" height="6" fill="#94a3b8"/><text x="200" y="130" font-size="10" fill="#94a3b8">Afternoon Shadow (East)</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_sun_09_{rng.randint(100000, 999999)}",
        "subskill": "09_shadow_diurnal_progression_morning_to_evening",
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
            "tier_1": "Where does a shadow point relative to the Sun?",
            "tier_2": "Opposite the Sun: morning Sun in east means shadow in west.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["shadow_direction_vs_sun_position_confusion"]
    }


def arch_10_time_zones_and_longitudinal_rotation(rng: random.Random) -> Dict[str, Any]:
    deg_per_hour = 15
    prompt = (
        f"Because Earth completes a 360° rotation in 24 hours, it rotates through 15° of longitude every single hour "
        f"(360° ÷ 24 = {deg_per_hour}°/hour).\n\n"
        "What global system was established based on this rotational rate?"
    )
    correct = "Standard global time zones, spaced roughly 15° of longitude (1 hour) apart."
    options = [
        correct,
        "The international metric measurement system for kilograms and metres.",
        "The periodic table of chemical elements.",
        "The classification system for plant and animal kingdoms."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Calculate rotational speed in degrees:\n"
        "360 degrees ÷ 24 hours = 15 degrees per hour.\n"
        "Step 2: Practical application:\n"
        "The world is divided into 24 standard time zones, each approximately 15° of longitude wide."
    )
    return {
        "id": f"ns7_sun_10_{rng.randint(100000, 999999)}",
        "subskill": "10_time_zones_and_longitudinal_rotation",
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
            "tier_1": "What system changes your clock when you fly to another country?",
            "tier_2": "Time zones are based on 15 degrees longitude per hour.",
            "tier_3": f"Correct option is: {correct}"
        },
        "misconception_tags": ["time_zones_arbitrary_convention_fallacy"]
    }


def arch_11_earth_revolution_period_365_days(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In addition to rotating on its axis, Earth revolves in an orbit around the Sun.\n\n"
        "What is the exact astronomical period required for Earth to complete ONE full revolution around the Sun?"
    )
    correct = "Approximately 365.25 days (365 days and 6 hours / 1 solar year)"
    options = [
        correct,
        "Exactly 24 hours",
        "Exactly 30 days",
        "Exactly 100 days"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Distinguish rotation from revolution:\n"
        "- Rotation: 1 day (24 hours) on its own axis.\n"
        "- Revolution: 1 year around the Sun.\n"
        "Step 2: Precise value:\n"
        "Earth takes 365.2422 days (~365.25 days, or 365 days and 6 hours) to complete one revolution."
    )
    return {
        "id": f"ns7_sun_11_{rng.randint(100000, 999999)}",
        "subskill": "11_earth_revolution_period_365_days",
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
            "tier_1": "Revolution is the journey around the Sun.",
            "tier_2": "Takes one year (365 and 1/4 days).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["rotation_revolution_confusion"]
    }


def arch_12_leap_year_astronomical_basis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the Gregorian calendar, an extra leap day (29 February) is added to the year every four years, "
        "making a leap year 366 days long.\n\n"
        "What astronomical fact necessitates the leap year system?"
    )
    correct = "Earth's revolution takes about 365.25 days; accumulating four 0.25 days (6 hours) equals 1 full extra day every 4 years."
    options = [
        correct,
        "The Sun stops emitting light for 24 hours every leap year.",
        "Earth spins on its axis 50% slower during February.",
        "The Moon passes behind Jupiter once every four years."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Account for the fraction:\n"
        "A standard calendar year has 365 days, but an astronomical year is 365.25 days.\n"
        "Step 2: Accumulation:\n"
        "0.25 day/year × 4 years = 1.0 day. Adding 29 February every 4 years prevents calendar seasons from drifting out of alignment."
    )
    return {
        "id": f"ns7_sun_12_{rng.randint(100000, 999999)}",
        "subskill": "12_leap_year_astronomical_basis",
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
            "tier_1": "What happens to the 0.25 (1/4) of a day each year?",
            "tier_2": "4 × 0.25 = 1 extra day added every four years.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["leap_year_mechanism_misunderstanding"]
    }


def arch_13_earth_orbit_elliptical_perihelion_aphelion(rng: random.Random) -> Dict[str, Any]:
    p_dist = "147 million km"
    a_dist = "152 million km"
    prompt = (
        f"Earth's orbit around the Sun is slightly elliptical. Earth is closest to the Sun ({p_dist}) at **perihelion** "
        f"in early January, and farthest from the Sun ({a_dist}) at **aphelion** in early July.\n\n"
        "What does this orbital eccentricity demonstrate about Earth's distance from the Sun?"
    )
    correct = "The distance varies slightly throughout the year, but the difference (about 3%) is too small to cause Earth's seasons."
    options = [
        correct,
        "Earth crashes into the Sun's atmosphere every January.",
        "The variation in distance is the sole reason why we have winter and summer.",
        "Earth's orbit is a hyperbola that never closes into a loop."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Examine orbital distances:\n"
        "Perihelion (~147 million km) occurs in January; Aphelion (~152 million km) occurs in July.\n"
        "Step 2: Conclude effect on climate:\n"
        "The 3% distance difference causes only minor solar intensity variations; it does NOT cause the seasons."
    )
    return {
        "id": f"ns7_sun_13_{rng.randint(100000, 999999)}",
        "subskill": "13_earth_orbit_elliptical_perihelion_aphelion",
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
            "tier_1": "Notice that Earth is closest to the Sun in January (Southern Hemisphere summer, Northern winter).",
            "tier_2": "Distance variation does NOT cause the seasons.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["seasons_caused_by_distance_myth"]
    }


def arch_14_distance_to_sun_not_cause_of_seasons_debunk(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A common misconception states: 'It is summer because Earth is closer to the Sun, and winter because Earth is farther away.'\n\n"
        "Which fact completely disproves this misconception?"
    )
    correct = "When it is summer in South Africa (Southern Hemisphere), it is simultaneously freezing winter in Europe (Northern Hemisphere)."
    options = [
        correct,
        "The Sun burns out completely every December and restarts in January.",
        "Earth is entirely flat and has no opposite hemispheres.",
        "Space temperatures are identical everywhere at all times."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Reason by contradiction:\n"
        "If distance from the Sun caused seasons, the entire planet would experience summer at the same time and winter at the same time.\n"
        "Step 2: Empirical observation:\n"
        "The Northern and Southern Hemispheres have opposite seasons simultaneously. This proves distance is not the cause."
    )
    return {
        "id": f"ns7_sun_14_{rng.randint(100000, 999999)}",
        "subskill": "14_distance_to_sun_not_cause_of_seasons_debunk",
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
            "tier_1": "Do South Africa and England experience winter at the same time?",
            "tier_2": "Opposite hemispheres experience opposite seasons simultaneously.",
            "tier_3": f"Correct option is: {correct}"
        },
        "misconception_tags": ["distance_from_sun_seasons_fallacy"]
    }


def arch_15_earth_axial_tilt_angle_23_5_degrees(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice(["23.5°", "approximately 23.5 degrees"])
    prompt = (
        f"Earth's axis of rotation is not perpendicular to its orbital plane around the Sun, "
        f"but is tilted at an angle of {angle}.\n\n"
        "What is the direct consequence of this 23.5° axial tilt as Earth orbits the Sun?"
    )
    correct = "It causes the cycle of the seasons by altering which hemisphere is tilted toward or away from the Sun."
    options = [
        correct,
        "It causes Earth to lose its magnetic field once every 10 years.",
        "It causes oceans to drain into the South Pole during winter.",
        "It prevents the Moon from completing any orbits around Earth."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify axial tilt:\n"
        "Earth's rotational axis is tilted 23.5° from the perpendicular to its orbital plane.\n"
        "Step 2: Effect:\n"
        "This tilt ensures that during different parts of the year, different hemispheres receive direct or indirect sunlight, producing the seasons."
    )
    return {
        "id": f"ns7_sun_15_{rng.randint(100000, 999999)}",
        "subskill": "15_earth_axial_tilt_angle_23_5_degrees",
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
            "tier_1": "What is the primary cause of seasons on Earth?",
            "tier_2": "The 23.5 degree axial tilt.",
            "tier_3": f"Answer is: {correct}"
        },
        "misconception_tags": ["axial_tilt_significance_error"]
    }


def arch_16_axial_parallelism_polar_star_orientation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Throughout Earth's entire 365.25-day journey around the Sun, its tilted rotational axis "
        "remains pointed in the exact same direction in deep space (towards the star Polaris in the north).\n\n"
        "What is this important astronomical property called?"
    )
    correct = "Axial parallelism (the axis stays parallel to itself as Earth orbits)."
    options = [
        correct,
        "Axial tumbling (the axis spins like a tossed coin every week).",
        "Orbital inversion (Earth flips completely upside down every month).",
        "Solar locking (the North Pole always points directly at the Sun)."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand axis stability:\n"
        "Like a spinning gyroscope, Earth's axis resists directional change.\n"
        "Step 2: Consequence for seasons:\n"
        "Because the axis remains parallel, in June the Northern Hemisphere tilts toward the Sun, while six months later in December the Southern Hemisphere tilts toward the Sun."
    )
    return {
        "id": f"ns7_sun_16_{rng.randint(100000, 999999)}",
        "subskill": "16_axial_parallelism_polar_star_orientation",
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
            "tier_1": "Does Earth's tilt point in a fixed direction or wobble wildly?",
            "tier_2": "The axis stays parallel to itself: axial parallelism.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["axial_parallelism_misunderstanding"]
    }


def arch_17_angle_of_incidence_direct_vs_indirect_sunlight(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a classroom experiment, a flashlight is shone directly at 90° onto a cardboard surface, "
        "and then tilted at a steep 30° angle.\n\n"
        "How does the concentration of light energy per square centimetre change when the beam is tilted?"
    )
    correct = "When tilted, the same amount of light energy spreads out over a larger surface area, resulting in lower energy concentration (indirect light)."
    options = [
        correct,
        "When tilted, the light beam compresses into a tiny laser point of intense heat.",
        "When tilted, light particles lose their speed and turn into ice crystals.",
        "Tilting the flashlight has zero effect on the illuminated surface area."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Direct light (90°):\n"
        "Light strikes perpendicularly, concentrating energy on a small surface area -> high heating.\n"
        "Step 2: Indirect light (tilted/oblique):\n"
        "Light spreads across a larger surface area -> less heat per unit area. This explains why winter is colder than summer."
    )
    beam_w = rng.choice([38, 40, 42])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" width="100%" height="130"><line x1="20" y1="110" x2="300" y2="110" stroke="#64748b" stroke-width="2"/><rect x="40" y="105" width="{beam_w}" height="10" fill="#f59e0b"/><text x="40" y="95" font-size="10" fill="#f59e0b">90° Direct (Concentrated)</text><rect x="180" y="105" width="{beam_w * 2}" height="10" fill="#fde68a"/><text x="180" y="95" font-size="10" fill="#d97706">30° Oblique (Spread Out)</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_sun_17_{rng.randint(100000, 999999)}",
        "subskill": "17_angle_of_incidence_direct_vs_indirect_sunlight",
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
            "tier_1": "Does spreading light over a wider area make it hotter or cooler?",
            "tier_2": "Spread out (indirect) light delivers less heat per unit area.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["angle_of_incidence_heating_effect"]
    }


def arch_18_solar_energy_concentration_per_unit_surface_area(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Why is midday solar radiation significantly warmer in summer than in winter at the same South African latitude?"
    )
    correct = "In summer, the Sun climbs higher in the sky, striking the ground at a steeper, more direct angle with higher solar energy concentration."
    options = [
        correct,
        "In summer, the Sun burns twice as much hydrogen fuel per second than in winter.",
        "In summer, Earth's ozone layer opens up to let boiling gases through.",
        "In summer, underground magma rises to heat the soil from below."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand seasonal solar angle:\n"
        "In summer, the hemisphere is tilted towards the Sun, so the Sun rises higher in the sky.\n"
        "Step 2: Concentration effect:\n"
        "Steeper solar rays deliver more concentrated energy per square metre and travel through less atmospheric thickness, maximizing surface warming."
    )
    return {
        "id": f"ns7_sun_18_{rng.randint(100000, 999999)}",
        "subskill": "18_solar_energy_concentration_per_unit_surface_area",
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
            "tier_1": "Consider how high the Sun is in the sky in summer vs winter.",
            "tier_2": "Higher Sun angle delivers more direct, concentrated energy.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["seasonal_sun_altitude_misconception"]
    }


def arch_19_seasonal_temperature_variations_mechanism(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Which two factors together primarily determine the seasonal temperature differences on Earth?"
    )
    correct = "The angle of incoming sunlight (direct vs indirect) and the duration of daylight hours."
    options = [
        correct,
        "The changing distance to the Sun and the speed of ocean currents.",
        "The phases of the Moon and the frequency of volcanic eruptions.",
        "The number of sunspots and Earth's atmospheric pressure changes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Factor 1 - Angle of sunlight:\n"
        "Direct rays provide concentrated heating in summer; oblique rays provide spread-out heating in winter.\n"
        "Step 2: Factor 2 - Daylight duration:\n"
        "Longer summer days allow more hours of solar heating, while short winter days allow less."
    )
    return {
        "id": f"ns7_sun_19_{rng.randint(100000, 999999)}",
        "subskill": "19_seasonal_temperature_variations_mechanism",
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
            "tier_1": "Think about Sun angle and how long the Sun shines each day.",
            "tier_2": "Angle of light and length of days.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["seasons_dual_factor_confusion"]
    }


def arch_20_day_length_variations_summer_vs_winter(rng: random.Random) -> Dict[str, Any]:
    city = rng.choice(["Johannesburg", "Cape Town", "Durban", "Upington"])
    prompt = (
        f"In {city} during December (summer), daylight lasts for approximately 14 hours. "
        "In June (winter), daylight lasts for only about 10 hours.\n\n"
        "What causes daylight hours to be longer in summer than in winter?"
    )
    correct = "The Southern Hemisphere tilts toward the Sun in December, keeping southern locations in sunlight for more than half of each 24-hour rotation."
    options = [
        correct,
        "Earth rotates much slower during summer months (a 36-hour day).",
        "The Sun physically slows down its travel speed across summer skies.",
        "Street lights in cities keep the sky artificially illuminated until 21:00."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand tilt relative to daylight circle (terminator):\n"
        "When a hemisphere tilts toward the Sun, the illuminated portion of its latitude circle is greater than the unlit portion.\n"
        "Step 2: Conclusion: More than 12 hours are spent in daylight during summer."
    )
    return {
        "id": f"ns7_sun_20_{rng.randint(100000, 999999)}",
        "subskill": "20_day_length_variations_summer_vs_winter",
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
            "tier_1": "Does rotation speed change, or does the tilt change exposure time?",
            "tier_2": "Tilting towards the Sun puts more of the latitude circle in light.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["day_length_rotation_speed_fallacy"]
    }


def arch_21_southern_hemisphere_summer_solstice_december(rng: random.Random) -> Dict[str, Any]:
    day_num = rng.choice(["21 December", "around 21-22 December"])
    prompt = (
        f"On or {day_num}, the Southern Hemisphere experiences its **summer solstice**.\n\n"
        "What astronomical occurrence defines this day in South Africa?"
    )
    correct = "The Southern Hemisphere is tilted at its maximum angle toward the Sun, producing the longest day and shortest night of the year."
    options = [
        correct,
        "The day when Earth is farthest from the Sun in deep space.",
        "The day when day and night are exactly equal at 12 hours each.",
        "The day with the lowest midday Sun altitude and coldest temperatures."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Define summer solstice:\n"
        "Solstice occurs when one hemisphere has its maximum tilt toward the Sun.\n"
        "Step 2: Apply to Southern Hemisphere:\n"
        "Around 21 December, the Southern Hemisphere tilts directly towards the Sun, giving South Africa its longest daylight period of the year."
    )
    return {
        "id": f"ns7_sun_21_{rng.randint(100000, 999999)}",
        "subskill": "21_southern_hemisphere_summer_solstice_december",
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
            "tier_1": "December in South Africa is summer.",
            "tier_2": "Summer solstice is the longest daylight day of the year.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["summer_solstice_hemisphere_inversion_error"]
    }


def arch_22_southern_hemisphere_winter_solstice_june(rng: random.Random) -> Dict[str, Any]:
    day_num = rng.choice(["21 June", "around 20-21 June"])
    prompt = (
        f"On {day_num}, observers in South Africa record the **winter solstice**.\n\n"
        "What characterizes the winter solstice in the Southern Hemisphere?"
    )
    correct = "The Southern Hemisphere is tilted farthest away from the Sun, resulting in the shortest day and longest night of the year."
    options = [
        correct,
        "The day when the Sun never sets anywhere in South Africa.",
        "The day when daytime lasts for 18 consecutive hours in Pretoria.",
        "The day when Earth passes through the Sun's core."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify winter solstice:\n"
        "In June, the Southern Hemisphere tilts away from the Sun.\n"
        "Step 2: Effect on day length:\n"
        "This produces the lowest solar altitude at solar noon and the shortest period of daylight in South Africa."
    )
    return {
        "id": f"ns7_sun_22_{rng.randint(100000, 999999)}",
        "subskill": "22_southern_hemisphere_winter_solstice_june",
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
            "tier_1": "June is winter in the Southern Hemisphere.",
            "tier_2": "Winter solstice has the shortest day and longest night.",
            "tier_3": f"Answer: {correct}"
        },
        "misconception_tags": ["winter_solstice_misunderstanding"]
    }


def arch_23_vernal_autumnal_equinoxes_equal_day_night(rng: random.Random) -> Dict[str, Any]:
    dates = [
        ("around 21 March", "autumn equinox in the Southern Hemisphere"),
        ("around 23 September", "spring (vernal) equinox in the Southern Hemisphere")
    ]
    dt, eq_name = rng.choice(dates)
    prompt = (
        f"Twice each year ({dt}), Earth experiences an **equinox** ({eq_name}).\n\n"
        "What does the Latin root 'equinox' mean, and what is true about day and night everywhere on Earth on this date?"
    )
    correct = "Equinox means 'equal night'; day and night are approximately equal in length (12 hours each) all over the world."
    options = [
        correct,
        "Equinox means 'extreme darkness'; the entire planet experiences 24 hours of black night.",
        "Equinox means 'equal heat'; every city has the exact same temperature of 25 °C.",
        "Equinox means 'double day'; there are two sunrises in 24 hours."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Etymology:\n"
        "'Equi' (equal) + 'nox' (night) = equal night.\n"
        "Step 2: Orbital geometry:\n"
        "At the equinoxes, Earth's axis tilts neither toward nor away from the Sun. The terminator passes through both poles, giving 12 hours of day and 12 hours of night globally."
    )
    return {
        "id": f"ns7_sun_23_{rng.randint(100000, 999999)}",
        "subskill": "23_vernal_autumnal_equinoxes_equal_day_night",
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
            "tier_1": "What does 'equi' sound like? Equal.",
            "tier_2": "12 hours of day and 12 hours of night.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["equinox_equal_day_night_definition"]
    }


def arch_24_tropic_of_capricorn_zenith_sun(rng: random.Random) -> Dict[str, Any]:
    lat = "23.5° South"
    prompt = (
        f"The Tropic of Capricorn is an imaginary line of latitude situated at {lat}, passing through northern South Africa (Limpopo).\n\n"
        "What special astronomical event happens at the Tropic of Capricorn at solar noon on 21 December?"
    )
    correct = "The Sun passes directly overhead at the zenith (90° vertical angle), casting no shadow directly beneath vertical objects."
    options = [
        correct,
        "The Sun freezes in place and stays visible for 48 consecutive hours.",
        "Earth's magnetic poles permanently swap places along this line.",
        "Oceans completely boil away for 10 minutes at noon."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify Tropic of Capricorn latitude:\n"
        "Located at 23.5° S.\n"
        "Step 2: Solar position at December Solstice:\n"
        "Because Earth's tilt is 23.5°, on 21 December the Sun's vertical rays strike 23.5° S directly overhead (zenith) at solar noon."
    )
    return {
        "id": f"ns7_sun_24_{rng.randint(100000, 999999)}",
        "subskill": "24_tropic_of_capricorn_zenith_sun",
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
            "tier_1": "The latitude 23.5° S matches Earth's 23.5° tilt.",
            "tier_2": "The Sun is directly overhead (90°) at noon on 21 December.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["tropic_of_capricorn_significance_error"]
    }


def arch_25_tropic_of_cancer_zenith_sun(rng: random.Random) -> Dict[str, Any]:
    lat = "23.5° North"
    prompt = (
        f"The Tropic of Cancer is situated at {lat}.\n\n"
        "On which date does the Sun reach its zenith (directly overhead at 90°) at solar noon on the Tropic of Cancer?"
    )
    correct = "Around 21 June (the Northern Hemisphere summer solstice and Southern Hemisphere winter solstice)."
    options = [
        correct,
        "Around 21 December (the Southern Hemisphere summer solstice).",
        "Around 21 March (the autumnal equinox).",
        "On 1 January every new year."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand Northern Hemisphere summer solstice:\n"
        "On 21 June, Earth's North Pole tilts directly toward the Sun.\n"
        "Step 2: Subsolar point:\n"
        "The Sun's perpendicular vertical rays strike 23.5° N (Tropic of Cancer) directly overhead."
    )
    return {
        "id": f"ns7_sun_25_{rng.randint(100000, 999999)}",
        "subskill": "25_tropic_of_cancer_zenith_sun",
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
            "tier_1": "When is it summer in the Northern Hemisphere?",
            "tier_2": "June is Northern summer solstice.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["tropic_of_cancer_date_confusion"]
    }
