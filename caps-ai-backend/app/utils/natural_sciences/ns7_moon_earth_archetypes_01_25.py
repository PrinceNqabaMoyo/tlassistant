"""Grade 7 Natural Sciences - Relationship of the Moon to the Earth: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the moon to the earth.md
Focus: Moon revolution, synchronous rotation, near vs far side, distance, regolith, atmosphere absence, temperature,
lunar phases (New Moon through Waning Crescent, causes, sequence), and solar eclipses (alignment, shadows, angular size, safety).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_moon_revolution_period(rng: random.Random) -> Dict[str, Any]:
    intros = [
        "The Moon orbits Earth along a nearly circular, slightly elliptical path held by gravity.",
        "Astronomers tracking lunar positions across the celestial sphere record its orbital period.",
        "In our solar system, the Moon is Earth's only natural satellite in continuous orbit."
    ]
    days = rng.choice(["27.3", "28", "29.5"])
    prompt = (
        f"{rng.choice(intros)}\n\n"
        "Approximately how long does it take for the Moon to complete ONE full orbit (revolution) around the Earth?"
    )
    correct = f"Approximately {days} days (about one month)"
    options = [
        correct,
        "Exactly 365.25 days (one solar year)",
        "Exactly 24 hours (one solar day)",
        "Approximately 12 hours (half a day)"
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand lunar revolution:\n"
        f"The Moon revolves around Earth in approximately 27.3 to 29.5 days (~28 days, or roughly one month).\n"
        f"Step 2: Conclusion:\n"
        f"The correct period is {correct}."
    )
    return {
        "id": f"ns7_moon_01_{rng.randint(100000, 999999)}",
        "subskill": "01_moon_revolution_period",
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
            "tier_1": "Think about the word 'month', which originates from the word 'moon'.",
            "tier_2": "The Moon's orbit takes about four weeks.",
            "tier_3": f"Choose {correct}."
        },
        "misconception_tags": ["confusing_rotation_with_revolution", "lunar_orbital_period_error"]
    }


def arch_02_moon_synchronous_rotation(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("telescope observers in South Africa", "only ever observe the familiar 'near side' of the Moon"),
        ("photographers in Pretoria", "never see the features on the Moon's opposite hemisphere from Earth"),
        ("stargazers in the Karoo", "observe the same craters and maria night after night")
    ]
    who, obs = rng.choice(scenarios)
    prompt = (
        f"When {who} look up, they {obs}.\n\n"
        "What is the scientific explanation for why the same side of the Moon always faces the Earth?"
    )
    correct = "The Moon's period of rotation on its axis equals its period of revolution around Earth (synchronous rotation)."
    options = [
        correct,
        "The Moon does not rotate at all on its axis as it travels through space.",
        "Earth's magnetic field locks the Moon so it cannot turn.",
        "The far side of the Moon is permanently cloaked in complete darkness and invisible."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify tidal locking / synchronous rotation:\n"
        "The Moon rotates on its own axis in exactly the same time it takes to orbit Earth (~27.3 days).\n"
        "Step 2: Effect:\n"
        "Because the rate of rotation matches the rate of revolution, the same hemisphere (the near side) faces Earth continuously."
    )
    return {
        "id": f"ns7_moon_02_{rng.randint(100000, 999999)}",
        "subskill": "02_moon_synchronous_rotation",
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
            "tier_1": "Does the Moon rotate in the same amount of time that it orbits?",
            "tier_2": "Equal rotation and revolution periods cause synchronous rotation.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["moon_does_not_rotate_fallacy", "dark_side_of_moon_myth"]
    }


def arch_03_near_side_vs_far_side_observation(rng: random.Random) -> Dict[str, Any]:
    probes = [
        ("the Soviet Luna 3 probe in 1959", "first photographic images"),
        ("modern lunar reconnaissance orbiters", "detailed topographical elevation maps"),
        ("the Clementine spacecraft", "high-resolution multispectral surveys")
    ]
    mission, data_type = rng.choice(probes)
    prompt = (
        f"Until {mission} returned {data_type}, humans had never observed the far side of the Moon.\n\n"
        "How does the far side of the Moon differ topographically and visually from the near side?"
    )
    correct = "The far side is densely covered in impact craters with very few dark volcanic maria (seas)."
    options = [
        correct,
        "The far side is entirely covered with liquid oceans of water.",
        "The far side has massive active volcanoes and lush vegetation.",
        "The far side is identical in maria coverage and topography to the near side."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Recall lunar topography:\n"
        "The near side features large dark basaltic plains called maria ('seas').\n"
        "Step 2: Compare with far side:\n"
        "The far side has a thicker crust, heavily cratered highlands, and almost no large maria."
    )
    return {
        "id": f"ns7_moon_03_{rng.randint(100000, 999999)}",
        "subskill": "03_near_side_vs_far_side_observation",
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
            "tier_1": "Think about whether the far side has smooth dark plains or rugged craters.",
            "tier_2": "The far side is heavily cratered with very few maria.",
            "tier_3": f"Correct option is: {correct}"
        },
        "misconception_tags": ["far_side_is_permanently_dark", "moon_surface_uniformity_error"]
    }


def arch_04_moon_distance_and_elliptical_orbit(rng: random.Random) -> Dict[str, Any]:
    dist_val = rng.choice(["384 400 km", "approximately 384 000 km", "roughly 30 Earth diameters"])
    prompt = (
        "The Moon orbits Earth at an average distance of approximately 384 400 kilometres.\n\n"
        "Because the Moon's orbit is an ellipse rather than a perfect circle, what happens to its distance from Earth?"
    )
    correct = "The distance varies between perigee (closest approach ~363 300 km) and apogee (farthest point ~405 500 km)."
    options = [
        correct,
        "The distance remains constant to within one metre throughout the entire year.",
        "The Moon spirals twice as far away during every winter season.",
        "The Moon collides with Earth's atmosphere once every lunar cycle."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand elliptical orbits:\n"
        "Planetary and lunar orbits are elliptical. In an ellipse, the distance between the primary body and satellite changes.\n"
        "Step 2: Identify perigee and apogee:\n"
        "Perigee is the closest orbital point and apogee is the farthest orbital point."
    )
    return {
        "id": f"ns7_moon_04_{rng.randint(100000, 999999)}",
        "subskill": "04_moon_distance_and_elliptical_orbit",
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
            "tier_1": "Does an ellipse have varying distances?",
            "tier_2": "Recall the terms perigee (near) and apogee (far).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["circular_orbit_assumption", "fixed_lunar_distance_error"]
    }


def arch_05_moon_surface_regolith_and_craters(rng: random.Random) -> Dict[str, Any]:
    minerals = rng.choice(["fine dust and broken rock fragments", "powdery rock called regolith", "crushed mineral debris"])
    prompt = (
        f"The surface of the Moon is covered in a layer of {minerals}.\n\n"
        "How does lunar soil (regolith) differ fundamentally from fertile soil found on Earth?"
    )
    correct = "Lunar regolith contains zero organic matter (humus), water, or living microorganisms."
    options = [
        correct,
        "Lunar regolith contains rich compost and earthworms.",
        "Lunar regolith is made entirely of compressed plastic and metal scrap.",
        "Lunar regolith has high moisture and clay minerals identical to garden loam."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Analyze terrestrial soil:\n"
        "Soil on Earth consists of weathered mineral rock, water, air, and decomposed organic matter (humus).\n"
        "Step 2: Contrast with lunar soil:\n"
        "The Moon has no living organisms, no liquid water, and no organic decomposition. Regolith is purely fragmented rock debris."
    )
    return {
        "id": f"ns7_moon_05_{rng.randint(100000, 999999)}",
        "subskill": "05_moon_surface_regolith_and_craters",
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
            "tier_1": "Are there plants or decomposing matter on the Moon?",
            "tier_2": "Without life or water, there is no organic humus.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lunar_soil_organic_matter_confusion"]
    }


def arch_06_moon_absence_of_atmosphere(rng: random.Random) -> Dict[str, Any]:
    consequences = [
        ("footprints left by Apollo astronauts remaining preserved for millions of years", "no wind or liquid water erosion"),
        ("the lunar sky appearing pitch black even during daytime", "no atmospheric gas particles to scatter sunlight"),
        ("sound being unable to travel across the lunar surface", "sound requires a physical medium like air to propagate")
    ]
    obs, cause = rng.choice(consequences)
    prompt = (
        f"On the Moon, {obs}.\n\n"
        "What key feature of the Moon explains this phenomenon?"
    )
    correct = f"The Moon has virtually no atmosphere ({cause})."
    options = [
        correct,
        "The Moon has a magnetic field ten times stronger than Earth.",
        "The Moon is made entirely of liquid mercury.",
        "The Moon rotates at supersonic speed."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify the underlying characteristic:\n"
        f"Because of its small mass and low gravity, the Moon could not retain an atmosphere.\n"
        f"Step 2: Connect to observation:\n"
        f"{obs} occurs directly because {cause}."
    )
    return {
        "id": f"ns7_moon_06_{rng.randint(100000, 999999)}",
        "subskill": "06_moon_absence_of_atmosphere",
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
            "tier_1": "Consider what Earth has that traps air and creates weather.",
            "tier_2": "The Moon lacks an atmosphere.",
            "tier_3": f"Correct answer is: {correct}"
        },
        "misconception_tags": ["moon_atmosphere_assumption", "weather_on_the_moon_fallacy"]
    }


def arch_07_moon_temperature_extremes(rng: random.Random) -> Dict[str, Any]:
    t_day = rng.choice(["+120 °C", "+130 °C", "+100 °C"])
    t_night = rng.choice(["-130 °C", "-170 °C", "-180 °C"])
    prompt = (
        f"On the Moon, daytime temperatures soar to over {t_day}, while night temperatures plummet to below {t_night}.\n\n"
        "Why does the Moon experience such violent temperature extremes compared to Earth?"
    )
    correct = "The lack of an atmosphere means there is no air blanket to trap heat at night or reflect excess solar radiation by day."
    options = [
        correct,
        "The Moon is ten times closer to the Sun during the daytime than at night.",
        "The core of the Moon completely freezes and melts every 24 hours.",
        "Intense volcanic eruptions heat the Moon by day and ocean currents cool it at night."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand atmospheric insulation:\n"
        "Earth's atmosphere acts as an insulating blanket (greenhouse effect) that moderates temperature.\n"
        "Step 2: Apply to the Moon:\n"
        "Without an atmosphere, incoming solar radiation directly bakes the surface, and heat immediately radiates into space at night."
    )
    return {
        "id": f"ns7_moon_07_{rng.randint(100000, 999999)}",
        "subskill": "07_moon_temperature_extremes",
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
            "tier_1": "What protects Earth from extreme hot days and freezing nights?",
            "tier_2": "Earth's atmosphere regulates temperature; the Moon has none.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["atmosphere_insulation_misunderstanding"]
    }


def arch_08_lunar_phases_cause_geometry(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "As the Moon orbits Earth over roughly 29.5 days, its apparent shape in the sky changes continuously.\n\n"
        "What is the true scientific cause of the phases of the Moon?"
    )
    correct = "The changing angle between Earth, the Moon, and the Sun alters the proportion of the illuminated lunar hemisphere visible from Earth."
    options = [
        correct,
        "Earth's shadow falls onto the Moon and gradually covers it each month.",
        "Clouds in Earth's upper atmosphere block parts of the Moon from view.",
        "The Moon physically expands and contracts like an inflatable sphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Dispel common eclipse misconception:\n"
        "Phases are NOT caused by Earth's shadow (that is an eclipse).\n"
        "Step 2: True cause:\n"
        "Half of the Moon is always illuminated by the Sun. As the Moon orbits Earth, observers on Earth see varying fractions of this lit hemisphere."
    )
    return {
        "id": f"ns7_moon_08_{rng.randint(100000, 999999)}",
        "subskill": "08_lunar_phases_cause_geometry",
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
            "tier_1": "Remember: Earth's shadow causes eclipses, NOT monthly phases.",
            "tier_2": "Phases depend on how much of the lit side we can see as the Moon circles Earth.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["phases_caused_by_earth_shadow_fallacy"]
    }


def arch_09_lunar_phase_new_moon(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice(["0°", "near conjunction", "between Earth and Sun"])
    prompt = (
        f"During a certain lunar phase ({angle}), the Moon lies directly between the Earth and the Sun, "
        "with its illuminated hemisphere turned completely toward the Sun.\n\n"
        "Which phase of the Moon does this describe?"
    )
    correct = "New Moon"
    options = ["New Moon", "Full Moon", "First Quarter", "Third Quarter"]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify celestial positions:\n"
        "Sun -> Moon -> Earth.\n"
        "Step 2: Determine visibility:\n"
        "The side facing Earth receives no direct sunlight and appears dark. This phase is the New Moon."
    )
    r_moon = rng.choice([68, 70, 72])
    stroke_c = rng.choice(["#64748b", "#94a3b8", "#475569"])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="160"><circle cx="100" cy="100" r="{r_moon}" fill="#1e293b" stroke="{stroke_c}" stroke-width="3"/><text x="100" y="105" text-anchor="middle" fill="#94a3b8" font-size="14" font-family="sans-serif">Unlit (Dark)</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_09_{rng.randint(100000, 999999)}",
        "subskill": "09_lunar_phase_new_moon",
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
            "tier_1": "When the unlit side faces us, we see no lit Moon in the sky.",
            "tier_2": "The Moon between Earth and Sun is the start of the lunar cycle.",
            "tier_3": "The phase is New Moon."
        },
        "misconception_tags": ["new_moon_visibility_error"]
    }


def arch_10_lunar_phase_waxing_crescent(rng: random.Random) -> Dict[str, Any]:
    frac = rng.choice(["less than half", "a thin sliver", "about 25%"])
    prompt = (
        f"A few days after New Moon, observers in the western sky after sunset notice {frac} "
        "of the Moon's visible disc illuminated, growing larger each subsequent evening.\n\n"
        "What is the precise term for this phase?"
    )
    correct = "Waxing Crescent"
    options = ["Waxing Crescent", "Waning Crescent", "Waxing Gibbous", "Third Quarter"]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand terminology:\n"
        "- 'Waxing' means growing in illuminated area.\n"
        "- 'Crescent' means less than half illuminated.\n"
        "Step 2: Conclusion: A growing thin sliver is a Waxing Crescent."
    )
    r_moon = rng.choice([68, 70, 72])
    col = rng.choice(["#f8fafc", "#f1f5f9", "#e2e8f0"])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="160"><circle cx="100" cy="100" r="{r_moon}" fill="#1e293b"/><path d="M 100 30 A 70 70 0 0 1 100 170 A 45 70 0 0 0 100 30" fill="{col}"/><text x="100" y="195" text-anchor="middle" fill="#64748b" font-size="12" font-family="sans-serif">Waxing Crescent</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_10_{rng.randint(100000, 999999)}",
        "subskill": "10_lunar_phase_waxing_crescent",
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
            "tier_1": "Waxing means growing; waning means shrinking.",
            "tier_2": "Less than half illuminated is a crescent.",
            "tier_3": "Correct answer: Waxing Crescent."
        },
        "misconception_tags": ["waxing_vs_waning_confusion"]
    }


def arch_11_lunar_phase_first_quarter(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Approximately 7 days (one week) following a New Moon, the Moon has completed one-quarter of its monthly orbit. "
        "From Earth, exactly half of the visible lunar disc appears illuminated.\n\n"
        "What is the official name of this lunar phase?"
    )
    correct = "First Quarter"
    options = ["First Quarter", "Third Quarter", "Full Moon", "Waxing Gibbous"]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify orbital fraction:\n"
        "One week into the 28-day orbit is 1/4 of the cycle.\n"
        "Step 2: Visual appearance:\n"
        "Half of the visible face is illuminated. Because it marks the first quarter of the orbit, it is named the First Quarter."
    )
    r_moon = rng.choice([68, 70, 72])
    col = rng.choice(["#f8fafc", "#f1f5f9", "#e2e8f0"])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="160"><circle cx="100" cy="100" r="{r_moon}" fill="#1e293b"/><path d="M 100 30 A 70 70 0 0 1 100 170 Z" fill="{col}"/><text x="100" y="195" text-anchor="middle" fill="#64748b" font-size="12" font-family="sans-serif">First Quarter (Half Lit)</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_11_{rng.randint(100000, 999999)}",
        "subskill": "11_lunar_phase_first_quarter",
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
            "tier_1": "It occurs one week after New Moon.",
            "tier_2": "One quarter through the cycle with half the disc lit.",
            "tier_3": "The phase is First Quarter."
        },
        "misconception_tags": ["quarter_vs_half_disc_naming_confusion"]
    }


def arch_12_lunar_phase_waxing_gibbous(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Between the First Quarter and Full Moon, more than half but not quite all of the Moon's visible disc is illuminated, "
        "and the illuminated portion continues to increase each night.\n\n"
        "Which term accurately identifies this phase?"
    )
    correct = "Waxing Gibbous"
    options = ["Waxing Gibbous", "Waning Gibbous", "Waxing Crescent", "First Quarter"]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand 'gibbous':\n"
        "'Gibbous' means swollen or hump-backed, referring to more than half but less than fully illuminated.\n"
        "Step 2: Understand 'waxing':\n"
        "Because the lit portion is growing towards Full Moon, it is Waxing Gibbous."
    )
    r_moon = rng.choice([68, 70, 72])
    col = rng.choice(["#f8fafc", "#f1f5f9", "#e2e8f0"])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="160"><circle cx="100" cy="100" r="{r_moon}" fill="#1e293b"/><path d="M 100 30 A 70 70 0 0 1 100 170 A 30 70 0 0 1 100 30" fill="{col}"/><text x="100" y="195" text-anchor="middle" fill="#64748b" font-size="12" font-family="sans-serif">Waxing Gibbous</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_12_{rng.randint(100000, 999999)}",
        "subskill": "12_lunar_phase_waxing_gibbous",
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
            "tier_1": "More than half lit is gibbous.",
            "tier_2": "Growing towards full means waxing.",
            "tier_3": "Correct answer: Waxing Gibbous."
        },
        "misconception_tags": ["gibbous_phase_terminology_error"]
    }


def arch_13_lunar_phase_full_moon(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Approximately 14 days after New Moon, Earth is situated between the Sun and the Moon. "
        "The entire near side of the Moon faces the Sun directly and is fully illuminated.\n\n"
        "What phase is this, and at what approximate time does it rise?"
    )
    correct = "Full Moon; it rises around sunset and sets around sunrise."
    options = [
        correct,
        "New Moon; it rises at solar noon and sets at sunset.",
        "Third Quarter; it rises at midnight and sets at midday.",
        "First Quarter; it rises at 09:00 and sets at 21:00."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify phase alignment:\n"
        "Sun -> Earth -> Moon. The side facing Earth is 100% illuminated, which is the Full Moon.\n"
        "Step 2: Determine rising time:\n"
        "Because the Moon is opposite the Sun, as the Sun sets in the west, the Full Moon rises in the east."
    )
    r_moon = rng.choice([68, 70, 72])
    col = rng.choice(["#f8fafc", "#f1f5f9", "#fef08a"])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="160"><circle cx="100" cy="100" r="{r_moon}" fill="{col}" stroke="#e2e8f0" stroke-width="2"/><text x="100" y="105" text-anchor="middle" fill="#0f172a" font-weight="bold" font-size="14" font-family="sans-serif">Full Disc Lit</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_13_{rng.randint(100000, 999999)}",
        "subskill": "13_lunar_phase_full_moon",
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
            "tier_1": "When the entire disc shines bright all night, what phase is it?",
            "tier_2": "Full Moon rises when the Sun sets.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["full_moon_timing_misconception"]
    }


def arch_14_lunar_phase_waning_gibbous(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Following Full Moon, the illuminated fraction visible from Earth begins to decrease, "
        "although more than half of the disc remains illuminated.\n\n"
        "What is the term for this decreasing, more-than-half illuminated phase?"
    )
    correct = "Waning Gibbous"
    options = ["Waning Gibbous", "Waxing Gibbous", "Waning Crescent", "Third Quarter"]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand 'waning':\n"
        "'Waning' means decreasing or shrinking in visible illumination.\n"
        "Step 2: Understand 'gibbous':\n"
        "More than half lit is gibbous. Hence, a shrinking more-than-half phase is Waning Gibbous."
    )
    r_moon = rng.choice([68, 70, 72])
    col = rng.choice(["#f8fafc", "#f1f5f9", "#e2e8f0"])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="160"><circle cx="100" cy="100" r="{r_moon}" fill="#1e293b"/><path d="M 100 30 A 70 70 0 0 0 100 170 A 30 70 0 0 0 100 30" fill="{col}"/><text x="100" y="195" text-anchor="middle" fill="#64748b" font-size="12" font-family="sans-serif">Waning Gibbous</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_14_{rng.randint(100000, 999999)}",
        "subskill": "14_lunar_phase_waning_gibbous",
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
            "tier_1": "Decreasing lit area means waning.",
            "tier_2": "More than half lit is gibbous.",
            "tier_3": "Correct answer: Waning Gibbous."
        },
        "misconception_tags": ["waning_phase_identification_error"]
    }


def arch_15_lunar_phase_third_quarter(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "About 21 days (three weeks) after New Moon, the Moon has completed three-quarters of its orbit around Earth. "
        "Exactly half of the disc is lit, but on the opposite side to the First Quarter.\n\n"
        "What is this phase called?"
    )
    correct = "Third (Last) Quarter"
    options = ["Third (Last) Quarter", "First Quarter", "New Moon", "Waning Crescent"]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify timing in orbital cycle:\n"
        "Three weeks into the 4-week cycle marks 3/4 (Third Quarter).\n"
        "Step 2: Visual appearance:\n"
        "Half of the disc is illuminated, and the phase rises around midnight. This is the Third Quarter."
    )
    r_moon = rng.choice([68, 70, 72])
    col = rng.choice(["#f8fafc", "#f1f5f9", "#e2e8f0"])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="160"><circle cx="100" cy="100" r="{r_moon}" fill="#1e293b"/><path d="M 100 30 A 70 70 0 0 0 100 170 Z" fill="{col}"/><text x="100" y="195" text-anchor="middle" fill="#64748b" font-size="12" font-family="sans-serif">Third Quarter</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_15_{rng.randint(100000, 999999)}",
        "subskill": "15_lunar_phase_third_quarter",
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
            "tier_1": "Three weeks after New Moon is the 3rd quarter of the cycle.",
            "tier_2": "Half the disc is lit before fading to crescent.",
            "tier_3": "Third (Last) Quarter."
        },
        "misconception_tags": ["first_vs_third_quarter_confusion"]
    }


def arch_16_lunar_phase_waning_crescent(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Just a few days before the next New Moon, only a narrow crescent of light is visible on the Moon, "
        "seen in the eastern sky shortly before sunrise.\n\n"
        "What is the name of this final phase in the monthly cycle?"
    )
    correct = "Waning Crescent"
    options = ["Waning Crescent", "Waxing Crescent", "Third Quarter", "New Moon"]
    rng.shuffle(options)
    sol = (
        "Step 1: Determine whether illumination is increasing or decreasing:\n"
        "It is decreasing toward New Moon, so it is 'waning'.\n"
        "Step 2: Determine shape:\n"
        "A thin sliver is a 'crescent'. Therefore, it is a Waning Crescent."
    )
    r_moon = rng.choice([68, 70, 72])
    col = rng.choice(["#f8fafc", "#f1f5f9", "#e2e8f0"])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="160"><circle cx="100" cy="100" r="{r_moon}" fill="#1e293b"/><path d="M 100 30 A 70 70 0 0 0 100 170 A 45 70 0 0 1 100 30" fill="{col}"/><text x="100" y="195" text-anchor="middle" fill="#64748b" font-size="12" font-family="sans-serif">Waning Crescent</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_16_{rng.randint(100000, 999999)}",
        "subskill": "16_lunar_phase_waning_crescent",
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
            "tier_1": "Shrinking sliver visible before dawn.",
            "tier_2": "Waning means decreasing; crescent is thin curve.",
            "tier_3": "Waning Crescent."
        },
        "misconception_tags": ["waxing_vs_waning_crescent_confusion"]
    }


def arch_17_lunar_phase_full_cycle_sequence(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Which of the following represents the correct chronological sequence of lunar phases "
        "starting from New Moon?"
    )
    correct = "New Moon -> Waxing Crescent -> First Quarter -> Waxing Gibbous -> Full Moon -> Waning Gibbous -> Third Quarter -> Waning Crescent"
    options = [
        correct,
        "New Moon -> Waxing Gibbous -> First Quarter -> Waxing Crescent -> Full Moon -> Waning Crescent -> Third Quarter -> Waning Gibbous",
        "Full Moon -> Waxing Crescent -> First Quarter -> New Moon -> Waning Gibbous -> Third Quarter -> Waning Crescent",
        "New Moon -> First Quarter -> Waxing Crescent -> Full Moon -> Third Quarter -> Waxing Gibbous -> Waning Crescent"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Chronological order of phases:\n"
        "1. New Moon (0 days)\n"
        "2. Waxing Crescent (~3.5 days)\n"
        "3. First Quarter (~7 days)\n"
        "4. Waxing Gibbous (~10.5 days)\n"
        "5. Full Moon (~14 days)\n"
        "6. Waning Gibbous (~17.5 days)\n"
        "7. Third Quarter (~21 days)\n"
        "8. Waning Crescent (~24.5 days)"
    )
    return {
        "id": f"ns7_moon_17_{rng.randint(100000, 999999)}",
        "subskill": "17_lunar_phase_full_cycle_sequence",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "hints": {
            "tier_1": "First wax from crescent to gibbous to full, then wane.",
            "tier_2": "Crescent comes before quarter, gibbous comes after quarter.",
            "tier_3": f"Correct sequence: {correct}"
        },
        "misconception_tags": ["phase_order_inversion_error"]
    }


def arch_18_lunar_illumination_reflected_sunlight(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Moon shines brightly in the night sky. Which statement correctly explains why the Moon is luminous to our eyes?"
    )
    correct = "The Moon is a non-luminous body that does not produce its own light; it reflects sunlight striking its rocky surface."
    options = [
        correct,
        "The Moon generates light through nuclear fusion in its hot core, acting as a mini star.",
        "The Moon glows due to bioluminescent algae growing in lunar craters.",
        "The Moon stores electrical charges during the day and emits phosphorescent light at night."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Classify celestial bodies by light emission:\n"
        "- Luminous bodies (like the Sun and stars) generate their own light via nuclear fusion.\n"
        "- Non-luminous bodies (like planets and moons) only reflect light from luminous sources.\n"
        "Step 2: Conclusion: Moonlight is simply reflected sunlight."
    )
    return {
        "id": f"ns7_moon_18_{rng.randint(100000, 999999)}",
        "subskill": "18_lunar_illumination_reflected_sunlight",
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
            "tier_1": "Does a rock in space burn nuclear fuel?",
            "tier_2": "The Moon reflects sunlight.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["moon_generates_its_own_light_fallacy"]
    }


def arch_19_relative_positions_sun_earth_moon(rng: random.Random) -> Dict[str, Any]:
    alignments = [
        ("Sun -> Moon -> Earth in a straight line", "New Moon", "Solar Eclipse possible"),
        ("Sun -> Earth -> Moon in a straight line", "Full Moon", "Lunar Eclipse possible"),
        ("Sun-Earth line at 90° right angle to Earth-Moon line", "First or Third Quarter", "Neap Tides")
    ]
    geom, phase_name, event = rng.choice(alignments)
    prompt = (
        f"When celestial bodies are aligned such that {geom}, what primary lunar phase occurs?"
    )
    correct = phase_name
    options = [phase_name, "Full Moon" if phase_name != "Full Moon" else "New Moon", "First Quarter" if "Quarter" not in phase_name else "Waxing Crescent", "Third Quarter" if "Quarter" not in phase_name else "Waxing Gibbous"]
    options = list(dict.fromkeys(options))[:4]
    rng.shuffle(options)
    sol = (
        f"Step 1: Analyze geometry:\n"
        f"{geom}.\n"
        f"Step 2: Identify phase:\n"
        f"This geometric configuration produces the {phase_name} ({event})."
    )
    return {
        "id": f"ns7_moon_19_{rng.randint(100000, 999999)}",
        "subskill": "19_relative_positions_sun_earth_moon",
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
            "tier_1": "Consider which body sits in the middle.",
            "tier_2": "Moon between Earth and Sun is New Moon; Earth between is Full Moon.",
            "tier_3": f"The answer is {correct}."
        },
        "misconception_tags": ["geometric_alignment_confusion"]
    }


def arch_20_solar_eclipse_alignment_order(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During a solar eclipse, daytime temporarily turns into twilight. "
        "What is the exact order of alignment of the Sun, Earth, and Moon during a solar eclipse?"
    )
    correct = "Sun -> Moon -> Earth (the Moon passes directly between the Sun and Earth)"
    options = [
        correct,
        "Sun -> Earth -> Moon (the Earth passes between the Sun and Moon)",
        "Earth -> Sun -> Moon (the Sun passes between Earth and the Moon)",
        "Moon -> Sun -> Earth (the Sun is at the end of the line)"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand solar eclipse definition:\n"
        "A solar eclipse occurs when the Moon blocks sunlight from reaching parts of Earth.\n"
        "Step 2: Deduce alignment:\n"
        "For the Moon to block the Sun, it must be positioned directly in the middle: Sun -> Moon -> Earth. This can only happen at New Moon."
    )
    r_sun = rng.choice([28, 30, 32])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 120" width="100%" height="120"><circle cx="40" cy="60" r="{r_sun}" fill="#f59e0b"/><text x="40" y="65" text-anchor="middle" fill="#ffffff" font-size="11">Sun</text><circle cx="180" cy="60" r="10" fill="#64748b"/><text x="180" y="85" text-anchor="middle" fill="#64748b" font-size="11">Moon</text><circle cx="300" cy="60" r="22" fill="#3b82f6"/><text x="300" y="65" text-anchor="middle" fill="#ffffff" font-size="11">Earth</text><line x1="70" y1="60" x2="170" y2="60" stroke="#f59e0b" stroke-dasharray="4"/><line x1="190" y1="60" x2="278" y2="60" stroke="#64748b" stroke-dasharray="4"/></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_20_{rng.randint(100000, 999999)}",
        "subskill": "20_solar_eclipse_alignment_order",
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
            "tier_1": "Which object blocks the Sun from our view on Earth?",
            "tier_2": "The Moon must be in the middle.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["solar_vs_lunar_eclipse_alignment_swap"]
    }


def arch_21_solar_eclipse_umbra_penumbra_shadows(rng: random.Random) -> Dict[str, Any]:
    shadow_parts = [
        ("umbra", "the dark, central, fully blocked cone of shadow where all direct sunlight is obstructed", "a total solar eclipse"),
        ("penumbra", "the lighter, outer region of partial shadow where only a portion of the Sun is obscured", "a partial solar eclipse")
    ]
    term, defn, effect = rng.choice(shadow_parts)
    prompt = (
        f"In optical shadow mechanics during an eclipse, {defn} produces {effect}.\n\n"
        f"What is the scientific name for this specific shadow cone?"
    )
    correct = term.capitalize()
    options = ["Umbra", "Penumbra", "Antumbra", "Corona"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Distinguish shadow zones:\n"
        f"- The Umbra is the dark central shadow where light is completely blocked (causing total eclipse).\n"
        f"- The Penumbra is the surrounding partial shadow where only part of the Sun is blocked (causing partial eclipse).\n"
        f"Step 2: Conclusion: {defn} refers to the {correct}."
    )
    return {
        "id": f"ns7_moon_21_{rng.randint(100000, 999999)}",
        "subskill": "21_solar_eclipse_umbra_penumbra_shadows",
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
            "tier_1": "Umbra is complete shadow; penumbra is partial shadow.",
            "tier_2": f"Notice whether all light is blocked or only part.",
            "tier_3": f"The term is {correct}."
        },
        "misconception_tags": ["umbra_penumbra_confusion"]
    }


def arch_22_solar_eclipse_angular_size_ratio(rng: random.Random) -> Dict[str, Any]:
    factor = rng.choice(["approximately 400 times", "about 400x"])
    prompt = (
        f"The Sun is {factor} larger in physical diameter than the Moon. "
        "Yet, during a total solar eclipse, the Moon appears almost the exact same angular size in our sky and completely blocks the Sun.\n\n"
        "What remarkable geometric ratio makes this possible?"
    )
    correct = "The Sun is also approximately 400 times farther away from Earth than the Moon, making their apparent angular sizes nearly identical."
    options = [
        correct,
        "The Moon's gravity bends the Sun's light to magnify the Moon by 400 times.",
        "Earth's atmosphere magnifies the Moon while shrinking the Sun.",
        "The Sun shrinks to 1/400th of its volume whenever the Moon passes in front of it."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand angular size:\n"
        "Angular size depends on both physical diameter and distance from the observer.\n"
        "Step 2: Calculate the ratio:\n"
        "Sun diameter / Moon diameter ≈ 400. Sun distance / Moon distance ≈ 400.\n"
        "Because both ratios match, their apparent sizes in the sky are both about 0.5 degrees."
    )
    return {
        "id": f"ns7_moon_22_{rng.randint(100000, 999999)}",
        "subskill": "22_solar_eclipse_angular_size_ratio",
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
            "tier_1": "Think about how distant objects appear smaller.",
            "tier_2": "The Sun is 400 times wider but also 400 times farther.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["angular_size_vs_physical_size_confusion"]
    }


def arch_23_total_vs_partial_solar_eclipse_zones(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During a solar eclipse, observers in Musina experience a total solar eclipse, "
        "while observers simultaneously in Durban only experience a partial eclipse.\n\n"
        "What explains this difference in observation between two locations on Earth?"
    )
    correct = "Musina falls within the narrow Moon's umbra shadow, whereas Durban falls within the broader penumbra shadow."
    options = [
        correct,
        "The Moon only moves over northern South Africa and skips the coast.",
        "Durban has more ocean water which repels the eclipse shadow.",
        "Earth's rotation stops completely over Musina during totality."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Analyze shadow footprint:\n"
        "The Moon's umbra cone tapers to a small point on Earth's surface (typically 100-250 km wide).\n"
        "Step 2: Compare zones:\n"
        "Locations inside this narrow track (umbra) see a total eclipse. Locations outside in the penumbra see only a partial eclipse."
    )
    return {
        "id": f"ns7_moon_23_{rng.randint(100000, 999999)}",
        "subskill": "23_total_vs_partial_solar_eclipse_zones",
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
            "tier_1": "Recall the two parts of the shadow: umbra and penumbra.",
            "tier_2": "Total eclipse is inside the umbra; partial is in the penumbra.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["eclipse_visibility_uniformity_fallacy"]
    }


def arch_24_solar_eclipse_path_of_totality(rng: random.Random) -> Dict[str, Any]:
    speed_kmh = rng.choice(["around 1 700 km/h", "over 1 600 km/h", "thousands of kilometres per hour"])
    prompt = (
        f"The Moon's umbral shadow sweeps rapidly across Earth's surface at {speed_kmh}.\n\n"
        "What is this narrow geographical track called, and how long does totality typically last at any single spot?"
    )
    correct = "Path of Totality; totality typically lasts between a few seconds and about 7.5 minutes."
    options = [
        correct,
        "Tropic of Capricorn; totality lasts for exactly 24 consecutive hours.",
        "Equatorial Trench; totality lasts for three full weeks.",
        "Geostationary Belt; totality lasts for 365 days."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Recall astronomical terms:\n"
        "The strip of land traced by the umbra is called the 'Path of Totality'.\n"
        "Step 2: Duration:\n"
        "Because the Moon and Earth are both in rapid motion, the shadow moves quickly, limiting totality to a maximum of ~7.5 minutes (often 2-4 minutes)."
    )
    return {
        "id": f"ns7_moon_24_{rng.randint(100000, 999999)}",
        "subskill": "24_solar_eclipse_path_of_totality",
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
            "tier_1": "Path of totality is the track of the dark umbra.",
            "tier_2": "Totality is brief: only a few minutes.",
            "tier_3": f"Correct option is: {correct}"
        },
        "misconception_tags": ["eclipse_duration_overestimation"]
    }


def arch_25_solar_eclipse_safety_and_pinhole_projection(rng: random.Random) -> Dict[str, Any]:
    devices = [
        ("a pinhole projector box", "indirect projection onto a white cardboard screen"),
        ("certified ISO 12312-2 solar eclipse glasses", "specialised optical polymer filters blocking 99.999% of sunlight"),
        ("a colander projecting multiple small sun crescents on the ground", "safe pinhole optics")
    ]
    device, tech = rng.choice(devices)
    prompt = (
        f"A natural sciences class uses {device} to observe an eclipse via {tech}.\n\n"
        "Why is it extremely dangerous to look directly at the Sun during a partial solar eclipse with the naked eye or regular sunglasses?"
    )
    correct = "Intense ultraviolet and infrared solar rays can permanently burn retinal photoreceptor cells in the eye without causing immediate pain."
    options = [
        correct,
        "The Moon releases toxic radiation particles that enter the eye pupils.",
        "Earth's magnetic field reverses during an eclipse, pulling the optic nerve.",
        "Looking at an eclipse causes temporary freezing of tear ducts with no retinal risk."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand retinal damage (solar retinopathy):\n"
        "The retina has no pain receptors. Concentrated solar rays focus on the fovea, burning light-sensing cells.\n"
        "Step 2: Proper safety:\n"
        "Standard sunglasses do NOT block sufficient infrared/UV rays. Only certified solar filters or indirect pinhole projectors are safe."
    )
    return {
        "id": f"ns7_moon_25_{rng.randint(100000, 999999)}",
        "subskill": "25_solar_eclipse_safety_and_pinhole_projection",
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
            "tier_1": "Can the retina feel pain when burned?",
            "tier_2": "Retinal burns cause permanent blindness; standard sunglasses are unsafe.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sunglasses_safe_for_solar_eclipse_myth"]
    }
