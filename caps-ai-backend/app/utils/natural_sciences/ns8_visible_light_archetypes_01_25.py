"""Grade 8 Natural Sciences: Term 3 - Visible Light Archetypes (01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/04. Visible light.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_01_definition_of_light_as_radiant_electromagnetic_energy(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice([
        ("sunlight crossing the vast vacuum of outer space", "transfers energy without requiring any physical atoms"),
        ("laser signals sent between ground stations and orbital satellites", "travels through empty space to transmit information"),
        ("radiation emitted by distant stars in galaxies", "reaches our eyes across billions of kilometres of empty space"),
    ])
    prompt = (
        f"Consider {context[0]}, which {context[1]}.\n\n"
        f"Which statement provides the accurate scientific definition of **visible light** and its mode of propagation?"
    )
    correct_opt = "A form of energy transferred by electromagnetic radiation that can travel through a vacuum and is detectable by the human eye."
    options = [
        correct_opt,
        "A stream of acoustic sound vibrations that requires a dense material medium like air or water to propagate.",
        "A chemical liquid that evaporates into clouds to produce colours during daylight hours.",
        "A mechanical pressure wave generated exclusively by electrical power lines.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Definition of Visible Light:**\n"
        f"- Light is radiant electromagnetic energy transferred by electromagnetic waves.\n"
        f"- Unlike sound, light does **not** require a physical medium; it travels freely through the vacuum of space.\n"
        f"- Visible light occupies the narrow wavelength band ($400 - 700\\text{{ nm}}$) that stimulates photoreceptor cells in the human retina.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_01_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "01_definition_of_light_as_radiant_electromagnetic_energy",
        "question_family_id": "01_definition_of_light_as_radiant_electromagnetic_energy",
        "hints": {
            "tier_1": "Can light travel through a vacuum, and what kind of wave is it?",
            "tier_2": "Light is electromagnetic radiation that travels through empty space and is visible to our eyes.",
            "tier_3": "Electromagnetic radiation that travels through a vacuum and is detectable by the human eye.",
        },
        "misconception_tags": ["light_requires_medium_misconception"],
    }


def arch_02_rectilinear_propagation_of_light_in_straight_lines(rng: random.Random) -> Dict[str, Any]:
    phenomenon = rng.choice([
        ("sunbeams shining through narrow gaps in tree canopies or dusty windows", "forming sharp, straight shafts of illumination"),
        ("laser pointers shone across a darkened classroom", "projecting an unbending straight beam onto the far wall"),
        ("sharp shadows cast on a wall when standing in front of a point light source", "showing crisp edges where straight rays are blocked"),
    ])
    prompt = (
        f"In everyday optics, observations such as {phenomenon[0]} ({phenomenon[1]}) provide clear evidence of a core property of light.\n\n"
        f"What is the scientific term for the principle that light travels in **straight lines** through a uniform medium?"
    )
    correct_opt = "Rectilinear propagation of light."
    options = [
        correct_opt,
        "Circular orbital convection.",
        "Random Brownian dispersion.",
        "Curvilinear gravitational winding.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Rectilinear Propagation of Light:**\n"
        f"- In a uniform, homogeneous medium, light travels along straight lines.\n"
        f"- This foundational property is known as **rectilinear propagation**.\n"
        f"- It explains why shadows have sharp boundaries, why pinhole cameras invert pictures, and why we cannot see around opaque corners without reflective surfaces.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_02_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "02_rectilinear_propagation_of_light_in_straight_lines",
        "question_family_id": "02_rectilinear_propagation_of_light_in_straight_lines",
        "hints": {
            "tier_1": "What Latin-derived scientific term means 'moving in a straight line'?",
            "tier_2": "The straight-line travel of light is termed rectilinear propagation.",
            "tier_3": "Rectilinear propagation of light.",
        },
        "misconception_tags": ["light_curves_around_objects_freely"],
    }


def arch_03_speed_of_light_in_vacuum_and_travel_time_calculations(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        ("the Sun to Earth", 150000000, 500, "8 minutes and 20 seconds"),
        ("the Sun to Mars", 228000000, 760, "12 minutes and 40 seconds"),
        ("the Sun to Jupiter", 778000000, 2593, "43 minutes and 13 seconds"),
    ])
    dist_km = scenario[1]
    sec = scenario[2]
    time_str = scenario[3]
    prompt = (
        f"Light travels through the vacuum of space at a constant speed of $300{{,}}000\\text{{ km/s}}$.\n"
        f"The average distance from {scenario[0]} is approximately ${dist_km:,}\\text{{ km}}$.\n\n"
        f"Calculate the time taken for sunlight to travel this distance, and choose the correct time in minutes and seconds."
    )
    correct_opt = f"Approximately ${sec}\\text{{ seconds}}$ (about {time_str})."
    wrong_sec = sec * 10
    options = [
        correct_opt,
        f"Approximately ${wrong_sec}\\text{{ seconds}}$ (about {round(wrong_sec / 60, 1)} minutes).",
        "Instantaneously (0 seconds), because radiant light covers cosmic space with zero elapsed time.",
        f"Approximately ${round(dist_km / 1000, 1)}\\text{{ seconds}}$ (about {round(dist_km / 60000, 1)} minutes).",
    ]
    rng.shuffle(options)
    sol = (
        f"**Speed of Light Travel Time Calculation:**\n"
        f"- Formula: $t = \\frac{{\\text{{distance}}}}{{\\text{{speed}}}} = \\frac{{d}}{{v}}$\n"
        f"- Substituting values:\n"
        f"  $$t = \\frac{{{dist_km:,}\\text{{ km}}}}{{300{{,}}000\\text{{ km/s}}}} = {sec}\\text{{ seconds}}$$\n"
        f"- Converting seconds to minutes: ${sec} \\div 60 = {time_str}$.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_03_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "03_speed_of_light_in_vacuum_and_travel_time_calculations",
        "question_family_id": "03_speed_of_light_in_vacuum_and_travel_time_calculations",
        "hints": {
            "tier_1": f"Divide distance ({dist_km:,} km) by speed of light (300,000 km/s).",
            "tier_2": f"Time = {dist_km:,} / 300,000 = {sec} seconds.",
            "tier_3": f"Approximately {sec} seconds ({time_str}).",
        },
        "misconception_tags": ["light_speed_is_infinite_misconception"],
    }


def arch_04_distinguishing_luminous_versus_non_luminous_celestial_and_terrestrial_objects(rng: random.Random) -> Dict[str, Any]:
    obj_pair = rng.choice([
        ("the Sun and burning campfires", "the Moon, mirrors, and school textbooks"),
        ("lit incandescent lamps and glowing fireflies", "planets, polished chrome, and plastic chairs"),
        ("hot molten lava and active computer screens", "clouds, asteroids, and cardboard boxes"),
    ])
    prompt = (
        f"In optical classification, objects are divided into luminous and non-luminous sources.\n\n"
        f"Which statement correctly distinguishes between **luminous** and **non-luminous** objects?"
    )
    correct_opt = f"Luminous objects (such as {obj_pair[0]}) generate and emit their own light, whereas non-luminous objects (such as {obj_pair[1]}) do not produce light and can only be seen when reflecting light from a luminous source."
    options = [
        correct_opt,
        f"Non-luminous objects produce their own internal light, while luminous objects absorb all incoming radiation completely.",
        f"The Moon is a luminous source that generates light through internal nuclear fusion, while the Sun is non-luminous.",
        "All solid objects are naturally luminous, whereas gases and liquids are always non-luminous.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Luminous vs Non-Luminous Objects:**\n"
        f"- **Luminous Objects:** Produce and radiate their own visible light (e.g. the Sun, stars, burning candles, LEDs, glow-worms).\n"
        f"- **Non-Luminous Objects:** Do not produce light. They are only visible because they reflect light rays originating from an external luminous source into our eyes (e.g. the Moon, tables, books, mirrors).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_04_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "04_distinguishing_luminous_versus_non_luminous_celestial_and_terrestrial_objects",
        "question_family_id": "04_distinguishing_luminous_versus_non_luminous_celestial_and_terrestrial_objects",
        "hints": {
            "tier_1": "Does the Moon generate its own light or reflect sunlight?",
            "tier_2": "Luminous produces its own light; non-luminous reflects light from elsewhere.",
            "tier_3": "Luminous emit their own light; non-luminous reflect external light.",
        },
        "misconception_tags": ["moon_is_luminous_misconception"],
    }


def arch_05_scientific_ray_diagram_conventions_and_beam_types(rng: random.Random) -> Dict[str, Any]:
    beam_type = rng.choice([
        ("parallel beam", "rays remain parallel and equidistant, like light from a distant star or searchlight"),
        ("diverging beam", "rays spread outward away from a single focal point, like light from a torch bulb"),
        ("converging beam", "rays travel toward one another and meet at a single focal point, like sunlight focused by a magnifying lens"),
    ])
    prompt = (
        f"In optical science, ray representations model the paths of light rays.\n\n"
        f"What is a **{beam_type[0]}**, and what standard convention is used to represent it in ray drawings?"
    )
    correct_opt = f"A beam where {beam_type[1]}; drawn as straight lines with arrowheads pointing in the direction of energy propagation."
    options = [
        correct_opt,
        f"A beam where {beam_type[1]}; drawn as zigzag curves without arrowheads to show wave motion.",
        "A collection of circular ripples with no specified direction of motion.",
        "A series of dashed boxes representing atomic mass units in the air.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Optical Ray Conventions:**\n"
        f"- A **ray** is represented as a single straight line with an arrowhead indicating direction.\n"
        f"- A collection of rays is called a **beam**:\n"
        f"  - **Parallel beam:** Rays travel parallel to one another.\n"
        f"  - **Diverging beam:** Rays spread out from a point.\n"
        f"  - **Converging beam:** Rays come together to intersect at a point.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_05_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "05_scientific_ray_diagram_conventions_and_beam_types",
        "question_family_id": "05_scientific_ray_diagram_conventions_and_beam_types",
        "hints": {
            "tier_1": f"How do rays travel in a {beam_type[0]}?",
            "tier_2": "Rays are straight lines with arrowheads showing the direction of propagation.",
            "tier_3": f"{beam_type[1]}; drawn with straight lines and arrowheads.",
        },
        "misconception_tags": ["ray_arrow_omission_misconception"],
    }


def arch_06_pinhole_camera_inverted_image_formation_mechanism(rng: random.Random) -> Dict[str, Any]:
    obj = rng.choice(["a lit candle flame", "a bright green tree outside the window", "a daylight outdoor flagpole"])
    prompt = (
        f"A learner constructs a simple pinhole camera (a lightproof box with a tiny pinhole at one end and a translucent screen at the other). "
        f"When pointed towards {obj}, an inverted (upside down) projection forms on the screen.\n\n"
        f"Which optical principle and ray geometry explains why this projection is upside down?"
    )
    correct_opt = "Because light travels in straight lines, rays from the top of the object pass through the tiny hole to the bottom of the screen, and rays from the bottom pass straight through to the top of the screen."
    options = [
        correct_opt,
        "Earth's gravitational field pulls heavier light rays downward inside the box, causing the projection to flip.",
        "The translucent wax paper contains microscopic prisms that actively invert visual wavefronts.",
        "Light rays curve in smooth loops when passing through circular apertures.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Mechanism of Pinhole Projection Inversion:**\n"
        f"- Light exhibits rectilinear propagation (travels strictly in straight lines).\n"
        f"- Rays from the top of {obj} travel straight through the pinhole and land at the bottom of the screen.\n"
        f"- Rays from the base travel straight through and land at the top of the screen.\n"
        f"- Rays from the left land on the right, and rays from the right land on the left.\n"
        f"- As a result, the resulting projection is completely inverted (upside down and laterally reversed).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_06_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "06_pinhole_camera_inverted_image_formation_mechanism",
        "question_family_id": "06_pinhole_camera_inverted_image_formation_mechanism",
        "hints": {
            "tier_1": "Follow the path of a straight light ray from the top of the object through the pinhole.",
            "tier_2": "Rays travel straight through the hole, crossing over to invert the projection.",
            "tier_3": "Straight rays from the top land at the bottom; straight rays from the bottom land at the top.",
        },
        "misconception_tags": ["pinhole_inverts_due_to_gravity_misconception"],
    }


def arch_07_pinhole_camera_image_size_variation_with_object_distance(rng: random.Random) -> Dict[str, Any]:
    movement = rng.choice([
        ("moved closer to the illuminated object", "increases in size (becomes larger)"),
        ("moved further away from the illuminated object", "decreases in size (becomes smaller)"),
    ])
    prompt = (
        f"A student observing an outdoor scene with a pinhole camera watches the projection formed on the wax paper screen.\n\n"
        f"When the pinhole camera is {movement[0]}, what happens to the size of the projected reproduction on the screen?"
    )
    correct_opt = f"The projection {movement[1]}, because the angle subtended by the light rays entering the pinhole changes proportionally."
    options = [
        correct_opt,
        f"The projection disappears completely whenever the camera moves.",
        f"The size remains perfectly unchanged regardless of distance because the pinhole has fixed dimensions.",
        f"The projection turns upright and shrinks to zero width.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Pinhole Camera Scaling:**\n"
        f"- Moving closer to an object increases the angular spread of rays entering the pinhole.\n"
        f"- The divergent rays travel across the fixed camera depth and strike a wider area of the screen $\\rightarrow$ Projection becomes **larger**.\n"
        f"- Conversely, moving further away decreases the entrance angle $\\rightarrow$ Projection becomes **smaller**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_07_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "07_pinhole_camera_image_size_variation_with_object_distance",
        "question_family_id": "07_pinhole_camera_image_size_variation_with_object_distance",
        "hints": {
            "tier_1": f"What happens to the size when the camera is {movement[0]}?",
            "tier_2": "Closer = larger projection; farther = smaller projection.",
            "tier_3": f"The projection {movement[1]}.",
        },
        "misconception_tags": ["pinhole_size_distance_invariance_misconception"],
    }


def arch_08_pinhole_camera_aperture_size_effect_on_sharpness_and_brightness(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner investigating a pinhole camera enlarges the pinhole aperture from a tiny $0{{,}}5\\text{{ mm}}$ pinprick "
        f"to a wide $10\\text{{ mm}}$ hole using a craft knife.\n\n"
        f"How does enlarging the aperture affect the **brightness** and **sharpness** of the projection formed on the screen?"
    )
    correct_opt = "The projection becomes much brighter because more total light enters, but it becomes blurry and out of focus because overlapping rays from many angles strike each point on the screen."
    options = [
        correct_opt,
        "The projection becomes completely black and unviewable because wide holes destroy light rays.",
        "The projection becomes extremely sharp and much dimmer because larger holes focus light better.",
        "The projection flips upright and turns into a 3D hologram.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Aperture Size in Pinhole Optics:**\n"
        f"- **Tiny Pinhole:** Allows only a single narrow ray from each point of the object to reach a specific point on the screen $\\rightarrow$ Sharp focus, but dim.\n"
        f"- **Large Hole:** Admits many rays from each point of the object, which land at slightly different positions on the screen $\\rightarrow$ Much brighter, but blurry (overlapping circles of confusion).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_08_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "08_pinhole_camera_aperture_size_effect_on_sharpness_and_brightness",
        "question_family_id": "08_pinhole_camera_aperture_size_effect_on_sharpness_and_brightness",
        "hints": {
            "tier_1": "More light enters through a bigger hole, but can it focus cleanly?",
            "tier_2": "Bigger hole = more light (brighter) but overlapping rays (blurry / loss of sharpness).",
            "tier_3": "Brighter but blurry and out of focus.",
        },
        "misconception_tags": ["large_aperture_improves_focus_misconception"],
    }


def arch_09_transparent_translucent_and_opaque_material_classification(rng: random.Random) -> Dict[str, Any]:
    sample = rng.choice([
        ("clear window glass, clean air, and pure water", "transparent", "transmits almost all light without scattering, allowing objects behind to be seen clearly"),
        ("frosted bathroom glass, tracing paper, and paraffin wax", "translucent", "transmits some light but scatters rays in all directions, so objects behind cannot be seen clearly"),
        ("solid sheet iron, thick cardboard, and clay brick", "opaque", "absorbs or reflects all light, allowing zero light transmission and casting a dark shadow"),
    ])
    prompt = (
        f"Materials interact with light in distinct ways based on their optical properties.\n"
        f"Materials such as **{sample[0]}** are scientifically classified as **{sample[1]}**.\n\n"
        f"Which statement defines the optical behavior of **{sample[1]}** materials?"
    )
    correct_opt = f"They {sample[2]}."
    options = [
        correct_opt,
        "They amplify light energy, doubling the speed of light when passing through.",
        "They spontaneously emit nuclear radiation when exposed to darkness.",
        "They turn into mirror surfaces when touched by human hands.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Optical Classification of Materials:**\n"
        f"- **Transparent:** Transmits light with minimal scattering; objects are seen clearly (e.g. clear glass, water, air).\n"
        f"- **Translucent:** Transmits light partially, scattering rays; objects behind appear blurred (e.g. frosted glass, tissue paper).\n"
        f"- **Opaque:** Completely prevents light from passing through; absorbs or reflects all rays, casting shadows (e.g. metals, wood, stone).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_09_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "09_transparent_translucent_and_opaque_material_classification",
        "question_family_id": "09_transparent_translucent_and_opaque_material_classification",
        "hints": {
            "tier_1": f"How does light interact with {sample[1]} materials?",
            "tier_2": f"{sample[1].capitalize()} materials {sample[2][:40]}...",
            "tier_3": f"{sample[2]}.",
        },
        "misconception_tags": ["confusing_translucent_and_transparent"],
    }


def arch_10_formation_of_shadows_by_opaque_objects_in_straight_rays(rng: random.Random) -> Dict[str, Any]:
    src = rng.choice(["a single point-source LED lamp", "a small flashlight bulb", "a sharp spotlight"])
    prompt = (
        f"When an opaque wooden sphere is placed in front of {src}, a dark, sharply defined shadow is cast onto a screen behind it.\n\n"
        f"Which fundamental law of optics accounts for the formation of shadows by opaque obstacles?"
    )
    correct_opt = "Rectilinear propagation; because light travels in straight lines and cannot bend around opaque obstacles, an area of darkness is formed where rays are blocked."
    options = [
        correct_opt,
        "Law of Conservation of Momentum; light bounces backwards into the power source.",
        "Diffraction around obstacles; light bends around the sphere to create darkness behind it.",
        "Total internal absorption; the opaque object radiates cold dark waves onto the screen.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Shadow Formation Mechanism:**\n"
        f"- Light travels in straight lines (rectilinear propagation).\n"
        f"- When straight-line rays encounter an opaque object, they are either absorbed or reflected and cannot pass through.\n"
        f"- Light rays passing immediately past the edges continue straight, leaving an unilluminated dark region (shadow) behind the object.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_10_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "10_formation_of_shadows_by_opaque_objects_in_straight_rays",
        "question_family_id": "10_formation_of_shadows_by_opaque_objects_in_straight_rays",
        "hints": {
            "tier_1": "Can light rays bend around corners in normal situations?",
            "tier_2": "Light travels in straight lines; an opaque object blocks straight rays, creating darkness behind.",
            "tier_3": "Light travels in straight lines and cannot bend around opaque obstacles.",
        },
        "misconception_tags": ["shadow_as_emitted_darkness_misconception"],
    }


def arch_11_shadow_umbra_and_penumbra_zones_from_extended_sources(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When an opaque object is illuminated by an **extended light source** (a broad light source like the Sun or a fluorescent tube), "
        f"the resulting shadow exhibits two distinct regions: the **umbra** and the **penumbra**.\n\n"
        f"What is the difference between the umbra and penumbra regions?"
    )
    correct_opt = "The umbra is the central zone of complete darkness where all light from the source is blocked; the penumbra is the surrounding outer zone of partial shadow where only part of the light source is blocked."
    options = [
        correct_opt,
        "The umbra is the brightest region, while the penumbra is the cold invisible region.",
        "The umbra and penumbra are identical in darkness, differing only in magnetic polarity.",
        "The umbra is formed only by red light, while the penumbra is formed only by violet light.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Umbra vs Penumbra:**\n"
        f"- **Umbra:** The innermost, completely dark region of a shadow where an observer would be unable to see any part of the light source.\n"
        f"- **Penumbra:** The fuzzy outer boundary region of partial shadow where an observer can see part of the light source but not all of it.\n"
        f"- Point sources produce only an umbra (sharp shadow); extended sources produce both an umbra and a penumbra (soft-edged shadow).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_11_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "11_shadow_umbra_and_penumbra_zones_from_extended_sources",
        "question_family_id": "11_shadow_umbra_and_penumbra_zones_from_extended_sources",
        "hints": {
            "tier_1": "Which part of the shadow is completely dark, and which is partial shadow?",
            "tier_2": "Umbra = total shadow (complete darkness); Penumbra = partial shadow.",
            "tier_3": "Umbra is complete darkness; penumbra is partial shadow.",
        },
        "misconception_tags": ["umbra_penumbra_inversion"],
    }


def arch_12_solar_and_lunar_eclipses_as_large_scale_shadow_phenomena(rng: random.Random) -> Dict[str, Any]:
    eclipse = rng.choice([
        ("solar eclipse", "the Moon passes directly between the Sun and Earth", "the Moon's shadow is cast onto the Earth"),
        ("lunar eclipse", "the Earth passes directly between the Sun and the Moon", "the Earth's shadow is cast onto the full Moon"),
    ])
    prompt = (
        f"Astronomical eclipses are large-scale natural manifestations of shadows.\n"
        f"During a **{eclipse[0]}**, {eclipse[1]}.\n\n"
        f"How does the rectilinear propagation of light explain what happens during a **{eclipse[0]}**?"
    )
    correct_opt = f"Sunlight traveling in straight lines is blocked by the intermediate celestial body, so that {eclipse[2]}."
    options = [
        correct_opt,
        "The Sun spontaneously shuts down its nuclear reactions for several minutes.",
        "The Earth reverses its rotation, casting night onto the wrong side of the globe.",
        "Cosmic dust clouds condense into a solid black asteroid between the orbits.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Physics of Eclipses:**\n"
        f"- Eclipses occur because light travels in straight lines through the vacuum of space.\n"
        f"- In a **Solar Eclipse:** The Moon passes directly between the Sun and Earth, casting its umbra and penumbra onto Earth.\n"
        f"- In a **Lunar Eclipse:** The Earth passes between the Sun and Moon, casting Earth's giant shadow over the Moon.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_12_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "12_solar_and_lunar_eclipses_as_large_scale_shadow_phenomena",
        "question_family_id": "12_solar_and_lunar_eclipses_as_large_scale_shadow_phenomena",
        "hints": {
            "tier_1": f"Which celestial body blocks the sunlight during a {eclipse[0]}?",
            "tier_2": f"Straight sunlight rays are blocked, so {eclipse[2]}.",
            "tier_3": f"Sunlight in straight lines is blocked, so {eclipse[2]}.",
        },
        "misconception_tags": ["eclipse_celestial_alignment_confusion"],
    }


def arch_13_dispersion_of_white_light_through_triangular_prism(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When a narrow beam of white sunlight enters a transparent triangular glass prism, "
        f"it fans out upon exiting into a brilliant continuous band of spectrum colours.\n\n"
        f"What is the scientific term for the splitting of white light into its constituent colours?"
    )
    correct_opt = "Dispersion of light."
    options = [
        correct_opt,
        "Sublimation of photons.",
        "Triboelectric charging.",
        "Specular polarization.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Dispersion of Light:**\n"
        f"- White light is a composite mixture of electromagnetic waves of different frequencies and wavelengths.\n"
        f"- When entering glass, each colour slows down to a slightly different speed, causing them to bend (refract) by different angles.\n"
        f"- This spreading of white light into its constituent spectral colours is termed **dispersion**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_13_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "13_dispersion_of_white_light_through_triangular_prism",
        "question_family_id": "13_dispersion_of_white_light_through_triangular_prism",
        "hints": {
            "tier_1": "What is the term for white light splitting into rainbow colours?",
            "tier_2": "The separation of white light by a prism is called dispersion.",
            "tier_3": "Dispersion of light.",
        },
        "misconception_tags": ["prism_creates_colour_chemicals_misconception"],
    }


def arch_14_visible_spectrum_sequence_of_seven_spectral_colours_roygbiv(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The visible spectrum produced by the dispersion of white sunlight contains seven distinct traditional colours.\n\n"
        f"Which list gives these seven colours in the correct order from **longest wavelength (lowest frequency)** to **shortest wavelength (highest frequency)**?"
    )
    correct_opt = "Red, Orange, Yellow, Green, Blue, Indigo, Violet (ROYGBIV)"
    options = [
        correct_opt,
        "Violet, Indigo, Blue, Green, Yellow, Orange, Red (VIBGYOR)",
        "Red, Green, Blue, Cyan, Magenta, Yellow, White",
        "Orange, Red, Green, Violet, Blue, Indigo, Yellow",
    ]
    rng.shuffle(options)
    sol = (
        f"**The Visible Spectrum (ROYGBIV):**\n"
        f"- From longest wavelength / lowest frequency to shortest wavelength / highest frequency:\n"
        f"  1. **Red** (~700 nm)\n"
        f"  2. **Orange**\n"
        f"  3. **Yellow**\n"
        f"  4. **Green**\n"
        f"  5. **Blue**\n"
        f"  6. **Indigo**\n"
        f"  7. **Violet** (~400 nm)\n"
        f"- The acronym **ROYGBIV** helps memorize this canonical order.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_14_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "14_visible_spectrum_sequence_of_seven_spectral_colours_roygbiv",
        "question_family_id": "14_visible_spectrum_sequence_of_seven_spectral_colours_roygbiv",
        "hints": {
            "tier_1": "Recall the famous mnemonic acronym ROYGBIV.",
            "tier_2": "Red has the longest wavelength; Violet has the shortest.",
            "tier_3": "Red, Orange, Yellow, Green, Blue, Indigo, Violet (ROYGBIV).",
        },
        "misconception_tags": ["spectrum_order_inversion"],
    }


def arch_15_wavelength_frequency_and_refraction_angle_relationship_in_dispersion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During dispersion through an optical glass prism, different colours of light bend by different amounts.\n\n"
        f"What is the physical relationship between a colour's **wavelength**, its **frequency**, and the degree to which it **refracts (bends)** in glass?"
    )
    correct_opt = "Higher frequency (shorter wavelength) light slows down more in glass and refracts the most, while lower frequency (longer wavelength) light refracts the least."
    options = [
        correct_opt,
        "Longer wavelength light always bends the most because heavier waves have more inertia.",
        "All frequencies bend by the exact same angle because the speed of light is identical in all media.",
        "Refraction depends solely on the brightness of the room and is independent of wavelength.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Wavelength, Frequency, and Refraction:**\n"
        f"- In a vacuum, all light travels at $c = 300{{,}}000\\text{{ km/s}}$.\n"
        f"- In a dense medium like glass, shorter wavelength / higher frequency waves (violet/blue) interact more strongly with glass atoms and slow down more than long wavelength waves (red).\n"
        f"- The greater the decrease in speed, the greater the angle of deviation (refraction).\n"
        f"- Hence: Violet slows down the most and bends the most; Red slows down the least and bends the least.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_15_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "15_wavelength_frequency_and_refraction_angle_relationship_in_dispersion",
        "question_family_id": "15_wavelength_frequency_and_refraction_angle_relationship_in_dispersion",
        "hints": {
            "tier_1": "Which colour slows down more in glass: violet or red?",
            "tier_2": "Higher frequency (violet) slows down more and refracts the most.",
            "tier_3": "Higher frequency / shorter wavelength slows down more and refracts most.",
        },
        "misconception_tags": ["red_refracts_most_misconception"],
    }


def arch_16_why_violet_light_refracts_most_and_red_light_refracts_least(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When white sunlight splits through a triangular perspex prism, red light appears on the upper edge "
        f"of the spread beam while violet light appears on the opposite extreme.\n\n"
        f"Why does **violet light bend the most** while **red light bends the least**?"
    )
    correct_opt = "Violet light has the shortest wavelength and highest frequency of visible light, causing it to experience the greatest reduction in speed in perspex."
    options = [
        correct_opt,
        "Red light has no energy, so it passes through the prism without noticing the perspex medium.",
        "Violet light is magnetically attracted to the silicon atoms in the glass prism.",
        "Red light is heavier than violet light and pushes through the prism in a rigid straight line.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Extreme Colours of Dispersion:**\n"
        f"- **Violet:** Shortest visible wavelength ($\\sim 400\\text{{ nm}}$), highest frequency $\\rightarrow$ Slowest speed in glass $\\rightarrow$ **Maximum refraction (most bent)**.\n"
        f"- **Red:** Longest visible wavelength ($\\sim 700\\text{{ nm}}$), lowest frequency $\\rightarrow$ Fastest speed in glass $\\rightarrow$ **Minimum refraction (least bent)**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_16_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "16_why_violet_light_refracts_most_and_red_light_refracts_least",
        "question_family_id": "16_why_violet_light_refracts_most_and_red_light_refracts_least",
        "hints": {
            "tier_1": "Does violet or red have the shorter wavelength?",
            "tier_2": "Violet has the shortest wavelength and slows down the most, bending the most.",
            "tier_3": "Violet has shortest wavelength and highest frequency, slowing down the most.",
        },
        "misconception_tags": ["dispersion_frequency_inversion"],
    }


def arch_17_formation_of_natural_rainbows_by_atmospheric_water_droplets(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"After a thunderstorm on a sunny afternoon, a magnificent rainbow is often seen in the sky.\n\n"
        f"What sequence of optical processes occurs inside individual spherical raindrops to produce a natural rainbow?"
    )
    correct_opt = "Refraction (and dispersion) as sunlight enters the droplet, internal reflection off the back curved surface, and further refraction as light exits back into the air."
    options = [
        correct_opt,
        "Water droplets emit coloured chemical dyes into the atmosphere that stain the air molecules.",
        "Direct nuclear fusion inside water droplets producing multi-coloured miniature explosions.",
        "Total absorption of all light rays except green, which transforms into other colours in the clouds.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Rainbow Formation Mechanics:**\n"
        f"1. **Entry Refraction:** Sunlight enters a raindrop, slows down, and undergoes dispersion (splitting into ROYGBIV).\n"
        f"2. **Internal Reflection:** The separated rays hit the back surface of the water drop and reflect internally.\n"
        f"3. **Exit Refraction:** As the rays exit back into the air, they refract again, spreading further into an observer's eyes.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_17_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "17_formation_of_natural_rainbows_by_atmospheric_water_droplets",
        "question_family_id": "17_formation_of_natural_rainbows_by_atmospheric_water_droplets",
        "hints": {
            "tier_1": "What happens when light enters, hits the back, and exits a water droplet?",
            "tier_2": "Refraction at entry, reflection at back, refraction at exit.",
            "tier_3": "Refraction and dispersion upon entry, internal reflection, and refraction upon exit.",
        },
        "misconception_tags": ["rainbow_chemical_dye_misconception"],
    }


def arch_18_specular_regular_reflection_versus_diffuse_reflection(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("a polished flat silver mirror", "specular (regular) reflection", "a rough painted concrete wall", "diffuse reflection"),
        ("still calm lake water", "specular (regular) reflection", "a page of a printed science textbook", "diffuse reflection"),
        ("a polished chrome bumper", "specular (regular) reflection", "a wooden school desk", "diffuse reflection"),
    ])
    prompt = (
        f"When parallel rays of light strike **{pair[0]}**, they undergo **{pair[1]}**.\n"
        f"When parallel rays strike **{pair[2]}**, they undergo **{pair[3]}**.\n\n"
        f"What is the difference between specular and diffuse reflection?"
    )
    correct_opt = "Specular reflection occurs on smooth surfaces where parallel rays reflect parallel, forming a clear reflected likeness; diffuse reflection occurs on microscopically rough surfaces where parallel rays scatter in all directions."
    options = [
        correct_opt,
        "Specular reflection destroys light rays, while diffuse reflection doubles their speed.",
        "Diffuse reflection only happens in vacuum space, while specular reflection requires water.",
        "Specular reflection violates the Law of Reflection, while diffuse reflection obeys it.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Specular vs Diffuse Reflection:**\n"
        f"- **Specular (Regular) Reflection:** Surface is flat and smooth on a microscopic scale. All parallel incident rays reflect at identical angles, remaining parallel $\\rightarrow$ Forms a clear reflected likeness (mirrors, calm water).\n"
        f"- **Diffuse Reflection:** Surface is rough or uneven microscopically. While the Law of Reflection holds locally at every point, varying surface normals scatter rays in all directions $\\rightarrow$ No reflected likeness is formed, but the surface is visible from any viewing angle.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_18_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "18_specular_regular_reflection_versus_diffuse_reflection",
        "question_family_id": "18_specular_regular_reflection_versus_diffuse_reflection",
        "hints": {
            "tier_1": "Why can you see your face in a mirror but not in a sheet of white paper?",
            "tier_2": "Smooth surface = specular (parallel rays stay parallel). Rough surface = diffuse (rays scatter).",
            "tier_3": "Specular reflects parallel rays parallel; diffuse scatters rays in all directions.",
        },
        "misconception_tags": ["diffuse_reflection_violates_law_of_reflection"],
    }


def arch_19_why_diffuse_reflection_allows_rough_objects_to_be_seen_from_all_angles(rng: random.Random) -> Dict[str, Any]:
    obj = rng.choice(["a wooden teacher desk", "a printed textbook page", "an unpolished clay brick"])
    prompt = (
        f"Unlike a flat mirror which only reflects light toward specific viewing angles, {obj} "
        f"can be clearly seen by students sitting anywhere in the classroom.\n\n"
        f"Why does **diffuse reflection** allow non-luminous rough objects to be seen from any position in a room?"
    )
    correct_opt = "Microscopic irregularities on the surface scatter incident light rays in every possible direction, sending some reflected light toward every part of the room."
    options = [
        correct_opt,
        "The object becomes luminous and begins producing its own internal photons.",
        "Light waves curve around the room using atmospheric sound waves.",
        "The object absorbs all light and glows exclusively in ultraviolet frequencies.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Why Diffuse Reflection Enables Omnidirectional Visibility:**\n"
        f"- Most natural objects have microscopic ridges, pits, and textures.\n"
        f"- When a beam of light strikes the rough surface, rays hit surface facets facing in countless different orientations.\n"
        f"- Each ray reflects according to its local normal, scattering light omnidirectionally.\n"
        f"- Therefore, some reflected light enters the eye of any observer in the room regardless of their vantage point.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_19_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "19_why_diffuse_reflection_allows_rough_objects_to_be_seen_from_all_angles",
        "question_family_id": "19_why_diffuse_reflection_allows_rough_objects_to_be_seen_from_all_angles",
        "hints": {
            "tier_1": "In how many directions does a rough surface scatter light?",
            "tier_2": "Microscopic irregularities scatter light in all directions, reaching eyes everywhere.",
            "tier_3": "Scatters incident light rays in every direction, sending light toward all observers.",
        },
        "misconception_tags": ["objects_only_visible_from_reflection_angle"],
    }


def arch_20_law_of_reflection_angle_of_incidence_equals_angle_of_reflection(rng: random.Random) -> Dict[str, Any]:
    angle_i = rng.choice([25, 30, 40, 45, 50, 60])
    prompt = (
        f"A ray of light traveling in air strikes a flat plane mirror at an angle of incidence of **${angle_i}^\\circ$** to the normal.\n\n"
        f"According to the **Law of Reflection**, what is the angle of reflection ($\\theta_r$)?"
    )
    correct_opt = f"Exactly ${angle_i}^\\circ$, because the angle of incidence always equals the angle of reflection ($\\theta_i = \\theta_r$)."
    comp_angle = 90 - angle_i
    options = [
        correct_opt,
        f"${comp_angle}^\\circ$, because the angle of reflection is the complement to $90^\\circ$.",
        f"${angle_i * 2}^\\circ$, because reflection doubles the angle of the light ray.",
        "0°, because light rays always bounce perpendicular to the mirror surface.",
    ]
    rng.shuffle(options)
    sol = (
        f"**The Law of Reflection:**\n"
        f"1. The angle of incidence equals the angle of reflection:\n"
        f"   $$\\theta_i = \\theta_r$$\n"
        f"   For an angle of incidence of ${angle_i}^\\circ$:\n"
        f"   $$\\theta_r = {angle_i}^\\circ$$\n"
        f"2. The incident ray, the reflected ray, and the normal line at the point of incidence all lie in the same geometric plane.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_20_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "20_law_of_reflection_angle_of_incidence_equals_angle_of_reflection",
        "question_family_id": "20_law_of_reflection_angle_of_incidence_equals_angle_of_reflection",
        "hints": {
            "tier_1": "What does the Law of Reflection state about the two angles?",
            "tier_2": f"Angle of incidence = angle of reflection. So if i = {angle_i}°, then r = {angle_i}°.",
            "tier_3": f"Exactly {angle_i}°.",
        },
        "misconception_tags": ["angle_of_reflection_not_equal_to_incidence"],
    }


def arch_21_measuring_angles_of_incidence_and_reflection_relative_to_normal(rng: random.Random) -> Dict[str, Any]:
    glancing_angle = rng.choice([20, 30, 35, 40])
    actual_i = 90 - glancing_angle
    prompt = (
        f"A light ray strikes a plane mirror such that the angle between the incident ray and the **surface of the mirror** is **${glancing_angle}^\\circ$**.\n\n"
        f"What is the **angle of incidence** ($\\theta_i$) for this ray?"
    )
    correct_opt = f"${actual_i}^\\circ$, because the angle of incidence must be referenced to the imaginary **normal line** ($90^\\circ$ to the surface): $90^\\circ - {glancing_angle}^\\circ = {actual_i}^\\circ$."
    options = [
        correct_opt,
        f"${glancing_angle}^\\circ$, because the angle of incidence is assumed along the glass surface.",
        f"${180 - glancing_angle}^\\circ$, because angles in reflection must add up to $180^\\circ$.",
        f"${glancing_angle * 2}^\\circ$, because rays reflect symmetrically about the horizon.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Measuring Angles from the Normal:**\n"
        f"- In optics, angles of incidence and reflection are **always evaluated relative to the normal** (a perpendicular reference line at $90^\\circ$ to the reflecting surface).\n"
        f"- The angle between the ray and the mirror surface is called the glancing angle.\n"
        f"- Therefore:\n"
        f"  $$\\theta_i = 90^\\circ - \\text{{glancing angle}} = 90^\\circ - {glancing_angle}^\\circ = {actual_i}^\\circ$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_21_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "21_measuring_angles_of_incidence_and_reflection_relative_to_normal",
        "question_family_id": "21_measuring_angles_of_incidence_and_reflection_relative_to_normal",
        "hints": {
            "tier_1": "Is the angle of incidence referenced to the mirror surface or to the normal line?",
            "tier_2": f"It is evaluated relative to the normal (90° line). Subtract {glancing_angle}° from 90°.",
            "tier_3": f"Angle of incidence is {actual_i}°.",
        },
        "misconception_tags": ["angle_measured_from_surface_not_normal_misconception"],
    }


def arch_22_plane_mirror_image_characteristics_virtual_upright_same_size(rng: random.Random) -> Dict[str, Any]:
    obj_h = rng.choice([15, 20, 25, 30])
    dist_m = rng.choice([0.5, 1.0, 1.5, 2.0])
    d_str = f"{dist_m}".replace(".", ",")
    prompt = (
        f"A student of height $1{{,}}5\\text{{ m}}$ places a candle of height ${obj_h}\\text{{ cm}}$ exactly ${d_str}\\text{{ m}}$ in front of a flat plane mirror.\n\n"
        f"Which set of characteristics correctly describes the reflected representation formed by this plane mirror?"
    )
    correct_opt = f"Virtual, upright, the exact same size (${obj_h}\\text{{ cm}}$), and situated ${d_str}\\text{{ m}}$ behind the mirror surface."
    options = [
        correct_opt,
        f"Real, inverted (upside down), magnified to double height, and formed on the glass surface.",
        f"Virtual, upside down, diminished to half height, and situated 0 m from the observer.",
        f"Real, upright, three times smaller, and projected onto the wall behind the candle.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Properties of a Plane Mirror Reflection:**\n"
        f"1. **Virtual:** Cannot be projected onto a physical screen because rays only appear to diverge from behind the mirror.\n"
        f"2. **Upright (Erect):** The top of the object remains at the top.\n"
        f"3. **Same Size (Magnification = 1):** Height matches the object (${obj_h}\\text{{ cm}}$).\n"
        f"4. **Equal Distance:** Distance of virtual reflection behind mirror equals object distance in front (${d_str}\\text{{ m}}$).\n"
        f"5. **Laterally Inverted:** Left and right are reversed.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_22_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "22_plane_mirror_image_characteristics_virtual_upright_same_size",
        "question_family_id": "22_plane_mirror_image_characteristics_virtual_upright_same_size",
        "hints": {
            "tier_1": "Is your face in a bathroom mirror upside down, bigger, smaller, or the exact same size?",
            "tier_2": "In a plane mirror, it is virtual, upright, same size, and at equal distance.",
            "tier_3": f"Virtual, upright, same size ({obj_h} cm), and {d_str} m behind.",
        },
        "misconception_tags": ["plane_mirror_magnification_misconception"],
    }


def arch_23_plane_mirror_lateral_inversion_and_perpendicular_distance(rng: random.Random) -> Dict[str, Any]:
    word = rng.choice(["AMBULANCE", "POLICE", "EMERGENCY"])
    prompt = (
        f"Emergency vehicles such as ambulances often have the word '**{word}**' written in reverse lettering across the vehicle front.\n\n"
        f"Why is this text printed in reverse, and what optical term describes this reversal in a plane mirror?"
    )
    correct_opt = f"Due to **lateral inversion** in plane mirrors, left and right are reversed; drivers looking in their rear-view mirrors see the word '{word}' oriented correctly."
    options = [
        correct_opt,
        "Due to chromatic dispersion, the letters appear coloured when viewed from moving cars.",
        "Due to vertical refraction, the lettering rotates 180 degrees clockwise in sunlight.",
        "It is an accidental printing mistake that emergency services cannot afford to correct.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Lateral Inversion in Plane Mirrors:**\n"
        f"- When an object faces a flat mirror, light from the right side of the object reflects back on the right side of the visual field.\n"
        f"- To an observer facing the mirror, this produces a left-to-right reversal known as **lateral inversion**.\n"
        f"- By printing '{word}' laterally reversed on the vehicle bonnet, the mirror reflection in a preceding driver's rear-view mirror is reversed again, allowing it to be read normally and rapidly.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_23_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "23_plane_mirror_lateral_inversion_and_perpendicular_distance",
        "question_family_id": "23_plane_mirror_lateral_inversion_and_perpendicular_distance",
        "hints": {
            "tier_1": "What happens to your left hand when you wave at yourself in a mirror?",
            "tier_2": "Plane mirrors produce lateral inversion (left-right reversal).",
            "tier_3": f"Lateral inversion reverses left and right, making '{word}' appear readable in rear-view mirrors.",
        },
        "misconception_tags": ["mirror_inverts_top_and_bottom_misconception"],
    }


def arch_24_definition_and_physical_cause_of_light_refraction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When a ray of light passes obliquely from air into a rectangular block of transparent glass, "
        f"it changes direction at the boundary surface.\n\n"
        f"What is this bending phenomenon called, and what is its fundamental **physical cause**?"
    )
    correct_opt = "Refraction; caused by a change in the speed of light as it passes between optical media of different densities."
    options = [
        correct_opt,
        "Reflection; caused by light bouncing backwards off the front glass surface.",
        "Combustion; caused by heat generated as light burns through glass molecules.",
        "Diffusion; caused by air escaping from the interior structure of the glass block.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Definition and Cause of Refraction:**\n"
        f"- **Refraction** is the bending or change in direction of a light wave when it crosses a boundary between two transparent media at an oblique angle.\n"
        f"- **Physical Cause:** Light travels at different speeds in different materials (e.g. $300{{,}}000\\text{{ km/s}}$ in air vs $\\sim 200{{,}}000\\text{{ km/s}}$ in glass).\n"
        f"- When one side of a wavefront enters the slower medium first, it slows down while the other side continues at higher speed, pivoting the ray.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_24_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "24_definition_and_physical_cause_of_light_refraction",
        "question_family_id": "24_definition_and_physical_cause_of_light_refraction",
        "hints": {
            "tier_1": "What happens to the speed of light when it enters glass from air?",
            "tier_2": "Light slows down in glass, causing the ray to bend. This is refraction.",
            "tier_3": "Refraction; caused by change in speed between media of different optical densities.",
        },
        "misconception_tags": ["refraction_caused_by_bouncing_misconception"],
    }


def arch_25_refraction_direction_when_entering_optically_denser_medium(rng: random.Random) -> Dict[str, Any]:
    transition = rng.choice([
        ("air into water", "air", "water", "slower"),
        ("air into crown glass", "air", "glass", "slower"),
        ("water into diamond", "water", "diamond", "slower"),
    ])
    prompt = (
        f"A ray of light traveling obliquely through {transition[1]} enters {transition[2]} (an optically denser medium).\n\n"
        f"In which direction does the light ray bend relative to the imaginary normal line, and why?"
    )
    correct_opt = f"It bends **towards the normal**, because light travels {transition[3]} in the optically denser medium ($\\theta_r < \\theta_i$)."
    options = [
        correct_opt,
        "It bends **away from the normal**, because entering a denser medium accelerates light rays.",
        "It does not bend at all, continuing in the identical direction regardless of angle.",
        "It reverses direction and reflects straight back into the light source.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Rules of Refraction (Entering Optically Denser Medium):**\n"
        f"- When passing from an optically rarer medium ({transition[1]}) into an optically denser medium ({transition[2]}):\n"
        f"  1. The speed of light decreases ($v_2 < v_1$).\n"
        f"  2. The ray bends **towards the normal** line.\n"
        f"  3. The angle of refraction is smaller than the angle of incidence ($\\theta_r < \\theta_i$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_25_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "25_refraction_direction_when_entering_optically_denser_medium",
        "question_family_id": "25_refraction_direction_when_entering_optically_denser_medium",
        "hints": {
            "tier_1": "When light slows down entering a denser material, does it bend toward or away from normal?",
            "tier_2": "Slowing down = bends towards the normal.",
            "tier_3": "Bends towards the normal because it travels slower.",
        },
        "misconception_tags": ["denser_medium_bends_away_from_normal"],
    }
