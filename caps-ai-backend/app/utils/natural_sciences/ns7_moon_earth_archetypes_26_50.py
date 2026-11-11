"""Grade 7 Natural Sciences - Relationship of the Moon to the Earth: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr7/Term 4/01. Relationship of the moon to the earth.md
Focus: Lunar eclipses (alignment, refraction, Blood Moon), orbital plane tilt (5 degrees), gravity, mass vs weight,
calculations on Earth and Moon, ocean tides (bulges, spring vs neap tides, tide charts, marine ecology, diagnostic autopsy).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_lunar_eclipse_alignment_order(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During a lunar eclipse, the Full Moon gradually dims and turns a coppery red color.\n\n"
        "What is the precise celestial alignment required for a lunar eclipse to occur?"
    )
    correct = "Sun -> Earth -> Moon (Earth passes directly between the Sun and the Moon)"
    options = [
        correct,
        "Sun -> Moon -> Earth (the Moon passes between the Sun and Earth)",
        "Earth -> Sun -> Moon (the Sun passes between Earth and the Moon)",
        "Moon -> Earth -> Sun (the Moon is on the far opposite side of the Sun)"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand lunar eclipse mechanics:\n"
        "A lunar eclipse occurs when Earth blocks sunlight from reaching the Moon.\n"
        "Step 2: Celestial order:\n"
        "The Earth must be in the middle: Sun -> Earth -> Moon. This only happens during the Full Moon phase."
    )
    r_sun = rng.choice([28, 30, 32])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 120" width="100%" height="120"><circle cx="40" cy="60" r="{r_sun}" fill="#f59e0b"/><text x="40" y="65" text-anchor="middle" fill="#ffffff" font-size="11">Sun</text><circle cx="180" cy="60" r="22" fill="#3b82f6"/><text x="180" y="65" text-anchor="middle" fill="#ffffff" font-size="11">Earth</text><circle cx="300" cy="60" r="10" fill="#b91c1c"/><text x="300" y="85" text-anchor="middle" fill="#b91c1c" font-size="11">Moon</text><line x1="70" y1="60" x2="158" y2="60" stroke="#f59e0b" stroke-dasharray="4"/><line x1="202" y1="60" x2="290" y2="60" stroke="#3b82f6" stroke-dasharray="4"/></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_26_{rng.randint(100000, 999999)}",
        "subskill": "26_lunar_eclipse_alignment_order",
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
            "tier_1": "Which body casts its shadow onto the Moon?",
            "tier_2": "Earth is in the middle, blocking sunlight from the Moon.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lunar_eclipse_alignment_confusion"]
    }


def arch_27_lunar_eclipse_earth_shadow_types(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("total lunar eclipse", "the Moon passes entirely through Earth's dark umbral shadow cone"),
        ("partial lunar eclipse", "only a portion of the Moon enters Earth's dark umbral shadow cone"),
        ("penumbral lunar eclipse", "the Moon passes only through the faint outer penumbra shadow of Earth")
    ]
    name, condition = rng.choice(types)
    prompt = (
        f"Which type of eclipse occurs when {condition}?"
    )
    correct = name.capitalize()
    options = ["Total lunar eclipse", "Partial lunar eclipse", "Penumbral lunar eclipse", "Total solar eclipse"]
    options = [o.capitalize() for o in options]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand Earth's shadow regions:\n"
        f"- Umbra: complete direct sunlight blockage.\n"
        f"- Penumbra: partial sunlight blockage.\n"
        f"Step 2: Conclusion: When {condition}, it is a {correct}."
    )
    return {
        "id": f"ns7_moon_27_{rng.randint(100000, 999999)}",
        "subskill": "27_lunar_eclipse_earth_shadow_types",
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
            "tier_1": "Does the entire Moon or part enter the umbra?",
            "tier_2": "Umbra entry means either total or partial depending on coverage.",
            "tier_3": f"Answer is: {correct}"
        },
        "misconception_tags": ["eclipse_type_classification_error"]
    }


def arch_28_lunar_eclipse_red_blood_moon_refraction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During a total lunar eclipse, the Moon does not disappear completely; instead, it glows a distinctive deep red or coppery color (a 'Blood Moon').\n\n"
        "What physical process in Earth's atmosphere causes this reddish glow on the eclipsed Moon?"
    )
    correct = "Sunlight passing through Earth's atmosphere has its shorter blue wavelengths scattered away, while longer red wavelengths refract (bend) around Earth onto the Moon."
    options = [
        correct,
        "Active lunar volcanoes erupt red hot lava across the entire surface during the eclipse.",
        "The Moon's iron rocks rust and glow due to sudden contact with oxygen from space.",
        "Artificial city lights from Earth project red warning beacons onto the Moon."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand atmospheric refraction and Rayleigh scattering:\n"
        "Earth's atmosphere scatters blue light strongly. Red light has longer wavelengths and penetrates through.\n"
        "Step 2: Red light bending:\n"
        "The reddish sunset and sunrise light around Earth's perimeter is refracted into Earth's shadow, casting a copper glow on the Moon."
    )
    return {
        "id": f"ns7_moon_28_{rng.randint(100000, 999999)}",
        "subskill": "28_lunar_eclipse_red_blood_moon_refraction",
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
            "tier_1": "Think about why sunsets on Earth appear red.",
            "tier_2": "Earth's atmosphere refracts red sunlight into the shadow cone.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["blood_moon_mythological_misconception", "refraction_scattering_confusion"]
    }


def arch_29_lunar_eclipse_night_hemisphere_visibility(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Unlike a solar eclipse, which is only visible from a very narrow path, a total lunar eclipse "
        "can be viewed by observers across more than half the globe.\n\n"
        "Why can anyone on the night side of Earth see a lunar eclipse?"
    )
    correct = "Earth itself casts a shadow far larger than the Moon, so the Moon is physically darkened for anyone facing it on Earth's night hemisphere."
    options = [
        correct,
        "The Moon moves down into Earth's atmosphere where all people can touch it.",
        "Radio towers broadcast lunar eclipse holograms into every country's sky.",
        "A lunar eclipse only happens at noon when everyone is awake."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Compare shadow sizes:\n"
        "- In a solar eclipse, the Moon's tiny umbra covers only a narrow strip (100-200 km) on Earth.\n"
        "- In a lunar eclipse, Earth is ~4x wider than the Moon. Earth's shadow engulfs the whole Moon.\n"
        "Step 2: Visibility:\n"
        "Because the Moon itself dims in space, every observer who has the Moon in their night sky can see it."
    )
    return {
        "id": f"ns7_moon_29_{rng.randint(100000, 999999)}",
        "subskill": "29_lunar_eclipse_night_hemisphere_visibility",
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
            "tier_1": "Is Earth bigger than the Moon?",
            "tier_2": "The entire night side of Earth faces the eclipsed Moon.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["solar_vs_lunar_eclipse_geographic_visibility_confusion"]
    }


def arch_30_eclipse_scarcity_orbital_plane_tilt(rng: random.Random) -> Dict[str, Any]:
    tilt_deg = rng.choice(["about 5 degrees", "approximately 5°"])
    prompt = (
        "A New Moon occurs every 29.5 days, and a Full Moon also occurs once each month. "
        "However, solar and lunar eclipses do NOT happen every month.\n\n"
        f"What astronomical tilt ({tilt_deg}) explains why eclipses are relatively rare events?"
    )
    correct = "The Moon's orbital plane around Earth is tilted at approximately 5° relative to Earth's orbital plane around the Sun (the ecliptic)."
    options = [
        correct,
        "Earth's equator is tilted at 90° to the Moon's magnetic poles.",
        "The Sun shuts off its light rays for two weeks every lunar cycle.",
        "The Moon changes its orbital direction from clockwise to anticlockwise every week."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand orbital planes:\n"
        "Earth orbits the Sun on the ecliptic plane. The Moon orbits Earth on a plane tilted by about 5 degrees.\n"
        "Step 2: Why eclipses don't happen every month:\n"
        "Most months, the Moon passes just above or below the Sun-Earth line. Eclipses can only occur when the Moon crosses the orbital plane at the nodes during New or Full Moon."
    )
    return {
        "id": f"ns7_moon_30_{rng.randint(100000, 999999)}",
        "subskill": "30_eclipse_scarcity_orbital_plane_tilt",
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
            "tier_1": "Think about whether the Moon's path is flat with Earth's orbit or tilted.",
            "tier_2": "A 5° tilt means the Moon usually passes above or below the shadow.",
            "tier_3": f"Correct option: {correct}"
        },
        "misconception_tags": ["coplanar_orbit_fallacy"]
    }


def arch_31_gravity_definition_non_contact_attraction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Gravity is the invisible force that governs the motion of celestial bodies across the universe.\n\n"
        "Which statement provides the accurate scientific definition of gravity in Grade 7 Natural Sciences?"
    )
    correct = "Gravity is a non-contact pulling force of attraction that exists between any two objects that have mass."
    options = [
        correct,
        "Gravity is a contact pushing force caused by atmospheric wind pressure pushing down on objects.",
        "Gravity is an electrostatic repulsion force between negatively charged electrons.",
        "Gravity is a magnetic force that only attracts metals like iron and nickel."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Recall force classification:\n"
        "Forces can be contact (friction, tension) or non-contact (gravity, magnetism, electrostatic).\n"
        "Step 2: Define gravity:\n"
        "Gravity is strictly an attractive (pulling), non-contact force that acts between any bodies possessing mass."
    )
    return {
        "id": f"ns7_moon_31_{rng.randint(100000, 999999)}",
        "subskill": "31_gravity_definition_non_contact_attraction",
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
            "tier_1": "Does gravity push or pull? Does it require physical contact?",
            "tier_2": "Gravity is a non-contact attractive (pulling) force.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["gravity_as_pushing_force_fallacy", "gravity_is_magnetic_confusion"]
    }


def arch_32_gravity_factors_mass_and_distance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "According to the laws of gravitational force, which two factors determine the strength of the gravitational attraction between two objects?"
    )
    correct = "The mass of the two objects and the distance between their centres."
    options = [
        correct,
        "The surface temperature and atmospheric color of the objects.",
        "The rotational speed and electrical charge of the objects.",
        "The chemical pH value and volume of liquid on the objects."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: State gravitational dependencies:\n"
        "- Mass: Greater mass produces greater gravitational force.\n"
        "- Distance: Greater distance weakens the gravitational force.\n"
        "Step 2: Conclusion: Mass and distance are the two fundamental factors."
    )
    return {
        "id": f"ns7_moon_32_{rng.randint(100000, 999999)}",
        "subskill": "32_gravity_factors_mass_and_distance",
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
            "tier_1": "Heavier objects pull more; closer objects pull more.",
            "tier_2": "Mass and distance.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["gravity_factors_confusion"]
    }


def arch_33_gravity_keeps_moon_in_orbit(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Moon moves at a high forward orbital speed (~1 km/s) around Earth. "
        "What would happen to the Moon if Earth's gravitational pull suddenly ceased to exist?"
    )
    correct = "The Moon would fly off in a straight line into deep space at constant speed."
    options = [
        correct,
        "The Moon would immediately plummet straight down and crash into Earth's core.",
        "The Moon would stop instantly in place and hover motionlessly in the sky.",
        "The Moon would shatter into millions of tiny rings around Earth."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Newton's First Law of Motion (Inertia):\n"
        "An object in motion continues in a straight line at constant velocity unless acted upon by a net force.\n"
        "Step 2: Role of gravity:\n"
        "Earth's gravity continuously pulls the Moon inward, curving its straight-line inertia into an orbital circle. Without gravity, it flies off along a tangent."
    )
    return {
        "id": f"ns7_moon_33_{rng.randint(100000, 999999)}",
        "subskill": "33_gravity_keeps_moon_in_orbit",
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
            "tier_1": "Think about swinging a ball on a string: what happens if the string snaps?",
            "tier_2": "The Moon's inertia carries it forward in a straight line.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["orbital_motion_inertia_misconception"]
    }


def arch_34_mass_concept_invariance_kg(rng: random.Random) -> Dict[str, Any]:
    m_val = rng.randint(45, 80)
    prompt = (
        f"A Grade 7 learner has a mass of {m_val} kg measured on Earth. "
        "The learner travels in a spacecraft to the surface of the Moon.\n\n"
        "What will the learner's mass be on the surface of the Moon?"
    )
    correct = f"Exactly {m_val} kg, because mass is the amount of matter in an object and does not change with location."
    options = [
        correct,
        f"{m_val // 6} kg, because lunar gravity is only one-sixth of Earth's gravity.",
        "0 kg, because there is zero gravity and total weightlessness on the Moon.",
        f"{m_val * 6} kg, because space suits multiply body mass by six."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Define mass:\n"
        f"Mass is the quantity of matter in an object, measured in kilograms (kg).\n"
        f"Step 2: Apply invariance property:\n"
        f"Mass is constant anywhere in the universe. The learner still has {m_val} kg on the Moon."
    )
    return {
        "id": f"ns7_moon_34_{rng.randint(100000, 999999)}",
        "subskill": "34_mass_concept_invariance_kg",
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
            "tier_1": "Does the number of atoms in your body change when you travel to the Moon?",
            "tier_2": "Mass in kg stays constant regardless of gravity.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["confusing_mass_with_weight", "mass_changes_with_gravity_fallacy"]
    }


def arch_35_weight_concept_gravitational_force_newtons(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In everyday language, people often say 'I weigh 60 kilograms'. "
        "In scientific terminology, why is this statement technically incorrect?"
    )
    correct = "Kilograms measure mass (amount of matter). Weight is a gravitational pulling force and must be measured in Newtons (N)."
    options = [
        correct,
        "Kilograms can only measure volumes of liquid like milk and water.",
        "Weight must always be recorded in degrees Celsius or Fahrenheit.",
        "People have zero weight while standing on the surface of the Earth."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Contrast mass and weight:\n"
        "- Mass: Amount of matter, SI unit is kilogram (kg).\n"
        "- Weight: Gravitational force exerted on that mass (W = mg), SI unit is Newton (N).\n"
        "Step 2: Conclusion: A 60 kg person has a mass of 60 kg and a weight of about 600 N on Earth."
    )
    return {
        "id": f"ns7_moon_35_{rng.randint(100000, 999999)}",
        "subskill": "35_weight_concept_gravitational_force_newtons",
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
            "tier_1": "What is the SI unit of force?",
            "tier_2": "Mass is in kg; force (weight) is in Newtons.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["everyday_mass_weight_unit_confusion"]
    }


def arch_36_weight_calculation_earth_gravity(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([40, 50, 60, 70, 80])
    w = m * 10
    prompt = (
        f"A crate on Earth has a mass of {m} kg. Using the standard Grade 7 approximation for Earth's gravitational acceleration "
        f"(g = 10 N/kg), calculate the weight of the crate on Earth."
    )
    correct = f"{w} N"
    options = [f"{w} N", f"{m} N", f"{m // 10} N", f"{w * 10} N"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify formula:\n"
        f"Weight = Mass × Gravitational field strength (W = m × g)\n"
        f"Step 2: Substitute values:\n"
        f"W = {m} kg × 10 N/kg = {w} N"
    )
    return {
        "id": f"ns7_moon_36_{rng.randint(100000, 999999)}",
        "subskill": "36_weight_calculation_earth_gravity",
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
            "tier_1": "Use the formula: Weight = mass × 10.",
            "tier_2": f"Multiply {m} by 10.",
            "tier_3": f"The answer is {correct}."
        },
        "misconception_tags": ["weight_formula_calculation_error"]
    }


def arch_37_weight_calculation_moon_gravity(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([30, 48, 60, 72, 90])
    g_moon = 1.6
    w_moon = round(m * g_moon, 1)
    w_str = f"{w_moon} N" if w_moon != int(w_moon) else f"{int(w_moon)} N"
    prompt = (
        f"The Moon's gravitational field strength is approximately 1.6 N/kg (about 1/6th of Earth's gravity). "
        f"Calculate the weight of an astronaut with a mass of {m} kg on the Moon."
    )
    correct = w_str
    options = [w_str, f"{m * 10} N", f"{m} N", f"{round(m / 1.6, 1)} N"]
    rng.shuffle(options)
    sol = (
        f"Step 1: Formula:\n"
        f"Weight on Moon = Mass × g_moon\n"
        f"Step 2: Calculation:\n"
        f"W_moon = {m} kg × 1.6 N/kg = {correct}."
    )
    return {
        "id": f"ns7_moon_37_{rng.randint(100000, 999999)}",
        "subskill": "37_weight_calculation_moon_gravity",
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
            "tier_1": "Multiply mass by 1.6 N/kg.",
            "tier_2": f"{m} × 1.6.",
            "tier_3": f"Result is {correct}."
        },
        "misconception_tags": ["lunar_weight_calculation_error"]
    }


def arch_38_weight_comparison_earth_vs_moon_ratio(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Because the Moon has only about 1% of Earth's mass and a smaller radius, "
        "its surface gravitational pull is roughly one-sixth (1/6) that of Earth.\n\n"
        "If a geological rock specimen weighs 360 N on Earth, what will it weigh on the surface of the Moon?"
    )
    correct = "60 N (360 N ÷ 6)"
    options = [
        correct,
        "360 N (weight never changes)",
        "2 160 N (360 N × 6)",
        "0 N (zero gravity on the Moon)"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Apply the 1/6 ratio:\n"
        "Weight on Moon = Weight on Earth ÷ 6\n"
        "Step 2: Calculate:\n"
        "360 N ÷ 6 = 60 N."
    )
    return {
        "id": f"ns7_moon_38_{rng.randint(100000, 999999)}",
        "subskill": "38_weight_comparison_earth_vs_moon_ratio",
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
            "tier_1": "Divide Earth's weight by 6.",
            "tier_2": "360 / 6 = 60.",
            "tier_3": f"Correct answer is {correct}."
        },
        "misconception_tags": ["weight_ratio_multiplication_inversion_error"]
    }


def arch_39_bathroom_scale_vs_beam_balance_physics(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "An astronaut tests two measuring instruments on the Moon: a spring bathroom scale and an equal-arm beam balance with standard brass kilogram weights.\n\n"
        "What will the two instruments show on the Moon compared to their readings on Earth?"
    )
    correct = "The spring scale reads 1/6th of the Earth value (measures weight), while the beam balance balances at the exact same value (compares masses equally affected by gravity)."
    options = [
        correct,
        "Both instruments read exactly zero on the Moon.",
        "Both instruments read six times higher on the Moon.",
        "The spring scale stays the same, but the beam balance flips upside down."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand spring balance mechanism:\n"
        "A spring measures force (compression or tension). With 1/6th gravity, the force is 1/6th, so it registers 1/6th the compression.\n"
        "Step 2: Understand beam balance mechanism:\n"
        "A beam balance compares gravity on the unknown object with gravity on standard masses. Both sides experience the exact same 1/6th gravity, so they balance identically."
    )
    return {
        "id": f"ns7_moon_39_{rng.randint(100000, 999999)}",
        "subskill": "39_bathroom_scale_vs_beam_balance_physics",
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
            "tier_1": "Springs measure force directly; balances compare masses.",
            "tier_2": "Does lunar gravity affect both sides of a balance equally?",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["balance_scale_physics_misconception"]
    }


def arch_40_astronaut_motion_reduced_gravity(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Apollo astronauts on the Moon found that running normally was difficult and instead used a 'kangaroo hop' or bounding gait.\n\n"
        "Why did astronauts jump much higher and stay in the air longer on the Moon?"
    )
    correct = "The Moon's lower gravitational acceleration (1.6 N/kg) pulls them back down much more slowly than Earth's gravity (9.8 N/kg)."
    options = [
        correct,
        "The astronauts' heavy space suits were equipped with anti-gravity thrusters.",
        "The Moon's magnetic field pushed up on their copper boots.",
        "Space suit air leaks propelled the astronauts upwards like balloons."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand gravitational acceleration on projectile motion:\n"
        "When jumping upward, gravity decelerates the jumper. On the Moon, downward acceleration is only 1.6 m/s² compared to 9.8 m/s² on Earth.\n"
        "Step 2: Effect:\n"
        "It takes longer for gravity to stop the upward velocity, allowing the astronaut to rise higher and hang in the air longer."
    )
    return {
        "id": f"ns7_moon_40_{rng.randint(100000, 999999)}",
        "subskill": "40_astronaut_motion_reduced_gravity",
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
            "tier_1": "Weaker gravity means slower downward acceleration.",
            "tier_2": "Lower gravitational pull allows higher, longer bounds.",
            "tier_3": f"Correct option is: {correct}"
        },
        "misconception_tags": ["projectile_motion_under_reduced_gravity"]
    }


def arch_41_ocean_tides_gravitational_pull_cause(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Coastal waters rise and fall in a predictable rhythmic cycle known as ocean tides.\n\n"
        "What is the primary physical cause of ocean tides on Earth?"
    )
    correct = "The gravitational pull of the Moon (and to a lesser extent the Sun) acting on Earth's oceans."
    options = [
        correct,
        "Whales and giant marine animals swimming together towards the coast.",
        "Undersea earthquakes constantly lifting and lowering the seabed.",
        "The heat of the midday Sun boiling seawater to expand its volume."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify tidal driving force:\n"
        "The Moon's gravity pulls on Earth's oceans. Because water is fluid, it bulges outward toward the Moon.\n"
        "Step 2: Secondary contributor:\n"
        "The Sun also exerts gravitational pull, contributing about 44% of the tidal force of the Moon."
    )
    return {
        "id": f"ns7_moon_41_{rng.randint(100000, 999999)}",
        "subskill": "41_ocean_tides_gravitational_pull_cause",
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
            "tier_1": "Which celestial body is closest and exerts the strongest tidal gravitational pull?",
            "tier_2": "The Moon's gravitational pull on ocean water.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["tide_origin_misconception"]
    }


def arch_42_two_high_and_two_low_tides_daily(rng: random.Random) -> Dict[str, Any]:
    locations = ["Cape Town harbour", "Durban beachfront", "Port Elizabeth harbour", "Saldanha Bay"]
    loc = rng.choice(locations)
    prompt = (
        f"At {loc}, fishermen observe that there are approximately two high tides and two low tides every 24 hours.\n\n"
        "Why are there TWO tidal bulges (high tides) on opposite sides of Earth simultaneously?"
    )
    correct = "One bulge forms on the side facing the Moon (direct gravitational pull), while a second bulge forms on the far side (inertia as Earth is pulled toward the Moon away from the water)."
    options = [
        correct,
        "The Moon splits into two gravitational halves at opposite ends of the world.",
        "The Sun pushes water from the front and the wind pushes water from the back.",
        "High tides only occur when ships pump out ballast water twice per day."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Near-side bulge:\n"
        "The ocean closest to the Moon experiences the strongest gravitational pull and bulges toward the Moon.\n"
        "Step 2: Far-side bulge:\n"
        "Earth's solid core is pulled toward the Moon more strongly than the far-side water, leaving an inertial bulge behind on the opposite hemisphere."
    )
    return {
        "id": f"ns7_moon_42_{rng.randint(100000, 999999)}",
        "subskill": "42_two_high_and_two_low_tides_daily",
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
            "tier_1": "Water bulges toward the Moon AND on the exact opposite side.",
            "tier_2": "Near side is gravitational pull; far side is inertia.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["single_bulge_tide_myth"]
    }


def arch_43_tidal_cycle_period_24_hours_50_minutes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "If a high tide occurs at 08:00 on Monday morning, the next morning's high tide will not be at 08:00, "
        "but approximately 50 minutes later at 08:50.\n\n"
        "Why does the tidal cycle take approximately 24 hours and 50 minutes (a lunar day) rather than exactly 24 hours?"
    )
    correct = "As Earth rotates in 24 hours, the Moon also advances in its orbit, requiring Earth to rotate an extra ~50 minutes to realign with the Moon."
    options = [
        correct,
        "Water in the ocean expands and contracts due to clock battery drainage.",
        "Earth slows down its rotation speed by 50 minutes every single day.",
        "Tidal waves hit undersea mountains that delay them by 50 minutes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Combine rotation and revolution:\n"
        "In 24 hours, Earth completes one 360° rotation.\n"
        "Step 2: Moon's progress:\n"
        "During those 24 hours, the Moon has orbited ~12° forward along its monthly path. Earth needs about 50 extra minutes of rotation to catch up with the Moon's new position."
    )
    return {
        "id": f"ns7_moon_43_{rng.randint(100000, 999999)}",
        "subskill": "43_tidal_cycle_period_24_hours_50_minutes",
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
            "tier_1": "Does the Moon stay frozen in one spot while Earth spins?",
            "tier_2": "The Moon advances forward in its orbit, adding ~50 minutes to the alignment.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lunar_day_vs_solar_day_confusion"]
    }


def arch_44_spring_tides_syzygy_alignment(rng: random.Random) -> Dict[str, Any]:
    phases = ["New Moon", "Full Moon"]
    p = rng.choice(phases)
    prompt = (
        f"During a {p}, the Sun, Earth, and Moon are aligned in a straight line (syzygy).\n\n"
        "What type of tide occurs during this straight-line alignment, and what happens to the gravitational forces?"
    )
    correct = "Spring tide: The gravitational pulls of the Sun and Moon combine together, reinforcing each other."
    options = [
        correct,
        "Neap tide: The gravitational pull of the Sun completely cancels the Moon's gravity.",
        "Equinox tide: Gravitational forces drop to zero across the oceans.",
        "Dormant tide: Oceans cease moving entirely for 48 hours."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify alignment:\n"
        "Sun, Moon, and Earth in a straight line (at New Moon or Full Moon).\n"
        "Step 2: Combine gravitational vectors:\n"
        "Because the tidal forces act along the same axis, their pulls add together, producing extreme 'Spring tides'."
    )
    rx_bulge = rng.choice([28, 30, 32])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 120" width="100%" height="120"><circle cx="40" cy="60" r="25" fill="#f59e0b"/><text x="40" y="65" text-anchor="middle" fill="#ffffff" font-size="10">Sun</text><circle cx="170" cy="60" r="18" fill="#3b82f6"/><text x="170" y="65" text-anchor="middle" fill="#ffffff" font-size="10">Earth</text><ellipse cx="170" cy="60" rx="{rx_bulge}" ry="20" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3"/><circle cx="280" cy="60" r="10" fill="#64748b"/><text x="280" y="65" text-anchor="middle" fill="#ffffff" font-size="10">Moon</text><text x="170" y="110" text-anchor="middle" fill="#0284c7" font-size="11">Aligned Gravitational Pulls (Spring Tide)</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_44_{rng.randint(100000, 999999)}",
        "subskill": "44_spring_tides_syzygy_alignment",
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
            "tier_1": "Straight line alignment adds the Sun and Moon's pulls.",
            "tier_2": "This produces high spring tides at New and Full Moon.",
            "tier_3": f"Correct answer is {correct}."
        },
        "misconception_tags": ["spring_tides_season_misconception"]
    }


def arch_45_spring_tides_maximum_tidal_range(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During a spring tide, what characterizes the water levels at high tide and low tide?"
    )
    correct = "Extra-high high tides and extra-low low tides (maximum tidal range)."
    options = [
        correct,
        "Very small differences between high tide and low tide (minimum tidal range).",
        "High tide and low tide occur at the exact same water height with no current.",
        "Water stays permanently at the low-water mark for an entire week."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Understand spring tide range:\n"
        "'Spring' comes from the German 'springen' (to leap up).\n"
        "Step 2: Effect on water levels:\n"
        "The combined gravitational pull pulls more water into high bulges (extra high high tide) and draws water away from the sides (extra low low tide). This is the maximum tidal range."
    )
    return {
        "id": f"ns7_moon_45_{rng.randint(100000, 999999)}",
        "subskill": "45_spring_tides_maximum_tidal_range",
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
            "tier_1": "Does spring tide mean bigger tidal range or smaller?",
            "tier_2": "Spring tides have the largest difference between high and low.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["spring_tide_water_level_confusion"]
    }


def arch_46_neap_tides_quadrature_right_angle(rng: random.Random) -> Dict[str, Any]:
    q_phases = ["First Quarter", "Third Quarter"]
    qp = rng.choice(q_phases)
    prompt = (
        f"During the {qp} phase, the Sun and Moon form a 90° right angle relative to Earth (quadrature).\n\n"
        "What type of tide occurs during this perpendicular alignment?"
    )
    correct = "Neap tide: The Sun's gravitational pull partially counteracts (cancels) the Moon's gravitational pull."
    options = [
        correct,
        "Spring tide: The perpendicular angle doubles the height of the tides.",
        "Tsunami tide: The 90° angle causes massive undersea whirlpools.",
        "Stagnant tide: Ocean water drains completely into underwater caves."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Analyze 90° alignment:\n"
        "The Moon pulls ocean water in one direction, while the Sun pulls at 90° to it.\n"
        "Step 2: Resulting cancellation:\n"
        "The Sun's pull partially offsets the Moon's bulge, resulting in weaker 'Neap tides'."
    )
    r_earth = rng.choice([19, 20, 21])
    spec = {
        "kind": "inline_svg",
        "svg": f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 200" width="100%" height="150"><circle cx="140" cy="140" r="{r_earth}" fill="#3b82f6"/><text x="140" y="145" text-anchor="middle" fill="#ffffff" font-size="10">Earth</text><circle cx="140" cy="30" r="10" fill="#64748b"/><text x="140" y="15" text-anchor="middle" fill="#64748b" font-size="10">Moon (Quarter)</text><circle cx="20" cy="140" r="18" fill="#f59e0b"/><text x="20" y="145" text-anchor="middle" fill="#ffffff" font-size="9">Sun</text><line x1="140" y1="120" x2="140" y2="45" stroke="#64748b" stroke-dasharray="3"/><line x1="120" y1="140" x2="42" y2="140" stroke="#f59e0b" stroke-dasharray="3"/><path d="M 130 130 L 130 140 L 140 140" fill="none" stroke="#ef4444" stroke-width="2"/><text x="190" y="180" text-anchor="middle" fill="#ef4444" font-size="11">90° Angle (Neap Tide)</text></svg>',
        "diagram_role": "context"
    }
    return {
        "id": f"ns7_moon_46_{rng.randint(100000, 999999)}",
        "subskill": "46_neap_tides_quadrature_right_angle",
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
            "tier_1": "Right angle alignment causes partial cancellation.",
            "tier_2": "Occurs at First and Third Quarter phases; called Neap tides.",
            "tier_3": f"The answer is {correct}."
        },
        "misconception_tags": ["neap_tide_alignment_confusion"]
    }


def arch_47_neap_tides_minimum_tidal_range(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During a neap tide, what characterizes coastal water levels compared to other times of the month?"
    )
    correct = "Lower high tides and higher low tides (minimum tidal range)."
    options = [
        correct,
        "Record-breaking high tides flooding streets along with dry harbours at low tide.",
        "Zero water movement with identical high and low tide times.",
        "Tides that reverse direction and flow inland for 12 hours straight."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Deduce neap tide effect:\n"
        "Because gravitational forces partially counteract each other at 90°, the high tide bulge is lower than average, and the low tide trough is higher than average.\n"
        "Step 2: Conclusion:\n"
        "Neap tides exhibit the minimum difference (range) between high and low water."
    )
    return {
        "id": f"ns7_moon_47_{rng.randint(100000, 999999)}",
        "subskill": "47_neap_tides_minimum_tidal_range",
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
            "tier_1": "Neap tides have subdued water height differences.",
            "tier_2": "Minimum tidal range: lower high tides, higher low tides.",
            "tier_3": f"Choose: {correct}"
        },
        "misconception_tags": ["neap_tide_range_confusion"]
    }


def arch_48_tide_table_interpretation_and_predictions(rng: random.Random) -> Dict[str, Any]:
    t_high = f"{rng.randint(2, 3)}.{rng.randint(0, 4)} m"
    t_low = f"0.{rng.randint(3, 7)} m"
    h_time = f"0{rng.randint(4, 9)}:{rng.randint(10, 50)}"
    l_time = f"{rng.randint(11, 15)}:{rng.randint(10, 50)}"
    prompt = (
        f"A maritime port authority issues the following tidal data for Table Bay Harbour:\n\n"
        f"- High Tide: {h_time} (Water height: {t_high})\n"
        f"- Low Tide: {l_time} (Water height: {t_low})\n\n"
        "What is the tidal range (difference between high and low water) for this period?"
    )
    diff = round(float(t_high.replace(" m", "")) - float(t_low.replace(" m", "")), 2)
    correct = f"{diff} m"
    options = [f"{diff} m", f"{round(diff + 0.8, 2)} m", f"{round(diff - 0.5, 2)} m", f"{t_high}"]
    options = list(dict.fromkeys(options))[:4]
    rng.shuffle(options)
    sol = (
        f"Step 1: Define tidal range:\n"
        f"Tidal range = High Tide height - Low Tide height\n"
        f"Step 2: Calculate:\n"
        f"Range = {t_high} - {t_low} = {correct}."
    )
    return {
        "id": f"ns7_moon_48_{rng.randint(100000, 999999)}",
        "subskill": "48_tide_table_interpretation_and_predictions",
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
            "tier_1": "Subtract the low tide height from the high tide height.",
            "tier_2": f"{t_high} minus {t_low}.",
            "tier_3": f"Correct value is {correct}."
        },
        "misconception_tags": ["tidal_range_subtraction_error"]
    }


def arch_49_coastal_tides_maritime_and_ecological_impact(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("deep-draft container ships entering shallow river harbours like East London", "entering at high tide to ensure sufficient water depth under the keel"),
        ("traditional coastal harvesters collecting mussels and limpets on rocky shores", "foraging at spring low tide when the intertidal zone is exposed"),
        ("rock pool organisms such as sea anemones and barnacles", "closing shells tightly at low tide to avoid desiccation (drying out)")
    ]
    who, reason = rng.choice(scenarios)
    prompt = (
        f"In South African coastal environments, {who} coordinate their activities by {reason}.\n\n"
        "Why is understanding the tidal cycle essential for coastal navigation and marine life?"
    )
    correct = "Tides dramatically change water depth and expose the intertidal zone twice each day, governing harbour accessibility and marine survival."
    options = [
        correct,
        "Tides alter the chemical salt composition of seawater into pure fresh drinking water.",
        "Tides cause ocean fish to turn into birds every full moon.",
        "Tides stop all currents and make ocean water boil at high tide."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Identify ecological and economic impacts of tides:\n"
        "- Marine life in the intertidal zone experiences alternating submersion and air exposure.\n"
        "- Commercial ships require deep water at high tide to navigate narrow or shallow channels safely without running aground."
    )
    return {
        "id": f"ns7_moon_49_{rng.randint(100000, 999999)}",
        "subskill": "49_coastal_tides_maritime_and_ecological_impact",
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
            "tier_1": "How does water depth change at high tide vs low tide?",
            "tier_2": "Shipping needs depth; intertidal marine life adapts to exposure.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["intertidal_ecology_misconception"]
    }


def arch_50_moon_earth_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    misconceptions = [
        ("Misconception: 'The Moon shines because it burns burning gases like the Sun.'", "Correction: The Moon is a non-luminous rocky body that only reflects sunlight."),
        ("Misconception: 'Phases of the Moon are caused by Earth's shadow covering the Moon.'", "Correction: Phases are caused by the changing visible angle of the Moon's sunlit hemisphere as it orbits Earth; Earth's shadow causes eclipses."),
        ("Misconception: 'There is zero gravity on the Moon because astronauts bounce.'", "Correction: The Moon has gravity (1.6 N/kg, roughly 1/6th of Earth's), which pulls astronauts down more slowly."),
        ("Misconception: 'Spring tides only occur in the spring season of the year.'", "Correction: Spring tides occur twice every month (at New and Full Moon) all year round when Sun and Moon align.")
    ]
    misc, corr = rng.choice(misconceptions)
    prompt = (
        f"A learner in a Grade 7 Natural Sciences examination makes the following assertion:\n\n"
        f"**{misc}**\n\n"
        "Evaluate this assertion. Which scientific correction provides the accurate explanation?"
    )
    correct = corr
    distractors = [c for m, c in misconceptions if c != corr]
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Diagnostic Evaluation:\n"
        f"{misc}\n\n"
        f"Scientific Reality:\n"
        f"{corr}"
    )
    return {
        "id": f"ns7_moon_50_{rng.randint(100000, 999999)}",
        "subskill": "50_moon_earth_comprehensive_diagnostic_autopsy",
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
            "tier_1": "Identify the scientific flaw in the student's statement.",
            "tier_2": "Carefully check the definitions of light, phases, gravity, and tides.",
            "tier_3": f"Correct option is: {correct}"
        },
        "misconception_tags": ["comprehensive_lunar_diagnostic_error"]
    }
