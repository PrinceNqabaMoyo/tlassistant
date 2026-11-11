"""Grade 8 Natural Sciences: Term 3 - Visible Light Archetypes (26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/04. Visible light.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_26_refraction_direction_when_entering_optically_rarer_medium(rng: random.Random) -> Dict[str, Any]:
    transition = rng.choice([
        ("water into air", "water", "air", "speeds up"),
        ("crown glass into air", "glass", "air", "speeds up"),
        ("perspex into air", "perspex", "air", "speeds up"),
    ])
    prompt = (
        f"A submerged light source directs a narrow beam of light from {transition[1]} obliquely across the boundary into {transition[2]} (an optically rarer medium).\n\n"
        f"In which direction does the refracted light ray bend relative to the imaginary normal line, and why?"
    )
    correct_opt = f"It bends **away from the normal**, because light {transition[3]} upon entering the optically rarer medium ($\\theta_r > \\theta_i$)."
    options = [
        correct_opt,
        "It bends **towards the normal**, because entering air always attracts light rays toward the vertical.",
        "It continues straight without any deviation because light rays never bend when emerging into air.",
        "It stops at the water surface and reflects downward as pure liquid heat.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Refraction Entering an Optically Rarer Medium:**\n"
        f"- When light passes from an optically denser medium ({transition[1]}) to an optically rarer medium ({transition[2]}):\n"
        f"  1. The speed of light increases ($v_2 > v_1$).\n"
        f"  2. The ray bends **away from the normal** line.\n"
        f"  3. The angle of refraction is greater than the angle of incidence ($\\theta_r > \\theta_i$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_26_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "26_refraction_direction_when_entering_optically_rarer_medium",
        "question_family_id": "26_refraction_direction_when_entering_optically_rarer_medium",
        "hints": {
            "tier_1": "When light speeds up entering an optically rarer medium, does it bend toward or away from normal?",
            "tier_2": "Speeding up = bends away from the normal (angle of refraction > angle of incidence).",
            "tier_3": "Bends away from the normal because light speeds up.",
        },
        "misconception_tags": ["rarer_medium_bends_towards_normal"],
    }


def arch_27_perpendicular_incidence_light_ray_entering_at_zero_degrees_to_normal(rng: random.Random) -> Dict[str, Any]:
    medium = rng.choice(["a flat glass block", "a calm swimming pool of water", "a perspex prism surface"])
    prompt = (
        f"A ray of light traveling in air strikes the surface of {medium} perpendicularly "
        f"(at an angle of incidence of **$0^\\circ$ to the normal**).\n\n"
        f"What happens to the speed and the direction of the light ray as it enters the new medium?"
    )
    correct_opt = "Its speed decreases, but its direction does not bend at all; it passes straight through along the normal line."
    options = [
        correct_opt,
        "Its speed stays constant, but its direction bends by 90 degrees along the glass surface.",
        "Both its speed and its direction remain completely unaltered.",
        "It splits into seven colours and reflects backwards into the light source.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Perpendicular Incidence (Normal Incidence):**\n"
        f"- When a light ray strikes a boundary at $0^\\circ$ to the normal (perpendicular to the surface, $90^\\circ$ glancing angle):\n"
        f"  - The speed decreases because the optical density of the medium is higher ($v = c / n$).\n"
        f"  - However, because all parts of the wavefront strike the interface simultaneously, no side of the wavefront is slowed ahead of another.\n"
        f"  - Therefore, the angle of refraction is $0^\\circ$, and the ray travels straight through without any directional bending.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_27_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "27_perpendicular_incidence_light_ray_entering_at_zero_degrees_to_normal",
        "question_family_id": "27_perpendicular_incidence_light_ray_entering_at_zero_degrees_to_normal",
        "hints": {
            "tier_1": "Does a ray entering at 0° to the normal bend sideways?",
            "tier_2": "Normal incidence means no change in direction, though speed still decreases.",
            "tier_3": "Speed decreases, but direction does not bend at all.",
        },
        "misconception_tags": ["perpendicular_rays_bend_misconception"],
    }


def arch_28_apparent_depth_illusion_of_submerged_objects_due_to_refraction(rng: random.Random) -> Dict[str, Any]:
    obj = rng.choice(["a coin at the bottom of a water cup", "a fish swimming in a clear pond", "the tiled floor of a swimming pool"])
    prompt = (
        f"When looking down into water, {obj} always appears significantly shallower (closer to the water surface) than it actually is.\n\n"
        f"Which optical explanation accounts for this **apparent depth** phenomenon?"
    )
    correct_opt = "Light rays reflecting off the submerged object refract away from the normal upon exiting water into air; our brain projects these diverging rays straight back, perceiving a virtual object closer to the surface."
    options = [
        correct_opt,
        "Water pressure physically pushes the atoms of the object closer to the surface.",
        "Reflected sound waves create an optical mirage that lifts the physical bottom of the pool.",
        "The eye lens inverts the colors of water, creating an illusion of reduced distance.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Apparent Depth Mechanism:**\n"
        f"- Light rays traveling from water into air bend away from the normal line (from denser to rarer medium).\n"
        f"- The human brain assumes that light always travels along straight, unbending lines.\n"
        f"- Tracing the refracted rays straight back into the water produces a virtual intersection at a shallower depth.\n"
        f"- Hence, submerged objects appear to be at an apparent depth that is roughly three-quarters of their real physical depth ($d_\\text{{apparent}} \\approx d_\\text{{real}} / 1{{,}}33$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_28_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "28_apparent_depth_illusion_of_submerged_objects_due_to_refraction",
        "question_family_id": "28_apparent_depth_illusion_of_submerged_objects_due_to_refraction",
        "hints": {
            "tier_1": "What happens to light rays leaving water and entering the air to your eyes?",
            "tier_2": "Rays bend away from the normal, making the object appear higher up than it actually is.",
            "tier_3": "Light refracts away from normal as it exits water; brain projects rays straight back.",
        },
        "misconception_tags": ["apparent_depth_caused_by_water_pressure"],
    }


def arch_29_apparent_bending_of_pencil_or_straw_submerged_in_water(rng: random.Random) -> Dict[str, Any]:
    item = rng.choice(["a straight wooden pencil", "a plastic drinking straw", "a glass stirring rod"])
    prompt = (
        f"When {item} is placed into a clear glass tumbler of water at an angle, "
        f"it appears to be sharply broken or bent at the boundary line between the air and water.\n\n"
        f"Why does this apparent bending occur?"
    )
    correct_opt = "Light rays coming from the submerged portion of the object bend away from the normal as they exit the water into air, shifting the apparent position of the submerged section relative to the portion in air."
    options = [
        correct_opt,
        "Water chemically dissolves the surface molecules of the object, physically bending its crystalline matrix.",
        "The glass container absorbs the central portion of the object and rotates it by 45 degrees.",
        "Surface tension pushes the top portion of the object in reverse direction.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Apparent Bending of a Submerged Straw/Pencil:**\n"
        f"- Light from the portion of the object in the air travels straight to the observer's eye.\n"
        f"- Light from the submerged portion travels through water and refracts (bends away from the normal) at the water-air interface.\n"
        f"- The observer's eye projects these bent rays straight back, making the submerged portion appear displaced upwards and sideways.\n"
        f"- This optical discontinuity at the surface creates the distinct visual illusion of a bent or broken object.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_29_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "29_apparent_bending_of_pencil_or_straw_submerged_in_water",
        "question_family_id": "29_apparent_bending_of_pencil_or_straw_submerged_in_water",
        "hints": {
            "tier_1": "Do rays from the underwater portion take a straight path or do they bend at the water surface?",
            "tier_2": "Rays from the underwater portion bend upon exiting, creating an apparent displacement.",
            "tier_3": "Light from submerged portion refracts away from normal at surface, displacing its perceived position.",
        },
        "misconception_tags": ["physical_bending_misconception"],
    }


def arch_30_mirages_and_atmospheric_refraction_of_sunlight(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"On a scorching hot summer day in South Africa, drivers traveling along long asphalt highways "
        f"frequently observe what appears to be a pool of shimmering water on the road in the distance.\n\n"
        f"What causes this road **mirage** to appear?"
    )
    correct_opt = "Intensely heated tarmac creates a layer of hot, optically rarer air near the ground; descending light rays from the blue sky refract continuously upwards into drivers' eyes, creating the illusion of reflected water."
    options = [
        correct_opt,
        "Subterranean pipes regularly release steam that condenses onto the asphalt during hot days.",
        "The sun's ultraviolet rays chemically liquify the tar surface temporarily.",
        "Drivers experience collective hallucinations caused by solar radiation affecting the inner ear.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Physics of Highway Mirages:**\n"
        f"- Dark asphalt absorbs intense sunlight and heats the air layer immediately above it.\n"
        f"- Hot air is less dense (optically rarer) than the cooler, denser air above it.\n"
        f"- Light rays traveling downward from the blue sky gradually speed up and bend continuously away from the normal.\n"
        f"- Eventually, total internal reflection/refraction curves the rays back upwards toward a driver's eyes.\n"
        f"- The driver's brain assumes straight-line travel and interprets the blue sky light as a puddle of water reflecting on the ground.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_30_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "30_mirages_and_atmospheric_refraction_of_sunlight",
        "question_family_id": "30_mirages_and_atmospheric_refraction_of_sunlight",
        "hints": {
            "tier_1": "What happens to the optical density of air when it gets very hot near the ground?",
            "tier_2": "Hot air near the ground is less dense, bending sky light rays upwards into the driver's eyes.",
            "tier_3": "Hot air near tarmac refracts sky light upwards, creating the illusion of a water puddle.",
        },
        "misconception_tags": ["mirage_as_hallucination_misconception"],
    }


def arch_31_colour_perception_via_selective_reflection_and_absorption(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("a ripe red strawberry", "red light frequencies", "all other frequencies (orange, yellow, green, blue, violet)"),
        ("a fresh green leaf", "green light frequencies", "red, orange, blue, and violet frequencies"),
        ("a bright yellow sunflower", "yellow light frequencies", "blue and violet light frequencies"),
        ("a blue school blazer", "blue light frequencies", "red, orange, yellow, and green frequencies"),
    ])
    prompt = (
        f"When white sunlight (containing all spectral colours) falls upon **{case[0]}**, "
        f"human observers perceive it as having its characteristic colour.\n\n"
        f"Which statement scientifically explains why this object appears to have this colour?"
    )
    correct_opt = f"The pigments in the object absorb {case[2]} and reflect {case[1]} into our eyes."
    options = [
        correct_opt,
        f"The object contains radioactive isotopes that manufacture new {case[1]} from internal atoms.",
        "The object absorbs all light completely, and our eyes invent colour to fill the empty visual gap.",
        f"The object reflects every spectral frequency equally, but human retinas filter out everything except {case[1]}.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Colour Perception Mechanics:**\n"
        f"- White light contains all colours of the visible spectrum.\n"
        f"- When white light strikes an opaque object, chemical pigments selectively absorb certain wavelengths and reflect others.\n"
        f"- We only perceive the wavelengths that are **reflected** into our eyes.\n"
        f"- For {case[0]}, it reflects {case[1]} and absorbs {case[2]}.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_31_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "31_colour_perception_via_selective_reflection_and_absorption",
        "question_family_id": "31_colour_perception_via_selective_reflection_and_absorption",
        "hints": {
            "tier_1": "Do we see the colour that an object absorbs or the colour that it reflects?",
            "tier_2": "We see the reflected colour; all other colours are absorbed by pigments.",
            "tier_3": f"Reflects {case[1]} and absorbs {case[2]}.",
        },
        "misconception_tags": ["objects_create_their_own_light_misconception"],
    }


def arch_32_why_white_objects_reflect_all_colours_and_stay_cooler(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In sunny hot regions of South Africa, people are encouraged to wear white clothing and paint "
        f"building roofs white to keep cool.\n\n"
        f"Why do white surfaces stay significantly cooler than darker surfaces under direct sunlight?"
    )
    correct_opt = "White surfaces reflect virtually all frequencies of visible light, absorbing very little radiant energy to convert into thermal energy."
    options = [
        correct_opt,
        "White surfaces absorb all light and convert it into cold ice crystals.",
        "White surfaces emit invisible air currents that blow hot air away from buildings.",
        "White surfaces attract cosmic rays that cancel out the thermal energy of the Sun.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Why White Surfaces Stay Cooler:**\n"
        f"- White light is a combination of all spectral colours.\n"
        f"- An object appears white because it reflects almost all incident visible wavelengths equally with minimal absorption.\n"
        f"- Since minimal radiant light energy is absorbed, very little is converted into thermal energy (heat).\n"
        f"- Consequently, white clothing and roofs remain much cooler in sunny weather.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_32_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "32_why_white_objects_reflect_all_colours_and_stay_cooler",
        "question_family_id": "32_why_white_objects_reflect_all_colours_and_stay_cooler",
        "hints": {
            "tier_1": "Does white reflect all colours or absorb all colours?",
            "tier_2": "White reflects all visible light frequencies, absorbing almost no radiant heat energy.",
            "tier_3": "Reflects all frequencies of light, absorbing very little energy.",
        },
        "misconception_tags": ["white_absorbs_light_misconception"],
    }


def arch_33_why_black_objects_absorb_all_colours_and_convert_to_heat(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Solar water heating panels on South African rooftops are painted with a matte black finish.\n\n"
        f"Why is black the optimal colour choice for solar thermal heating collectors?"
    )
    correct_opt = "Black surfaces absorb all frequencies of visible light with negligible reflection, converting the absorbed radiant energy into thermal energy."
    options = [
        correct_opt,
        "Black surfaces attract electricity from lightning clouds directly into water tanks.",
        "Black surfaces reflect sunlight back into space at double intensity.",
        "Black surfaces emit cool light rays that protect water from boiling too quickly.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Why Black Surfaces Absorb Heat:**\n"
        f"- An object appears black because it absorbs almost all wavelengths of visible light and reflects almost nothing back to the eye.\n"
        f"- Absorbed radiant energy excites the atoms in the material, increasing their kinetic energy and raising the temperature.\n"
        f"- This maximizes solar energy collection, making matte black the ideal coating for solar water heaters and solar panels.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_33_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "33_why_black_objects_absorb_all_colours_and_convert_to_heat",
        "question_family_id": "33_why_black_objects_absorb_all_colours_and_convert_to_heat",
        "hints": {
            "tier_1": "What happens to light striking a black surface: reflection or absorption?",
            "tier_2": "Black absorbs all visible frequencies and converts radiant light energy to heat.",
            "tier_3": "Absorbs all frequencies of visible light, converting radiant energy into thermal energy.",
        },
        "misconception_tags": ["black_as_reflection_misconception"],
    }


def arch_34_perceiving_coloured_objects_under_monochromatic_red_illumination(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice([
        ("a pure red apple", "red", "it reflects the incoming red light into our eyes"),
        ("a pure green leaf", "black", "it absorbs the incoming red light and has no green light available to reflect"),
        ("a pure blue book", "black", "it absorbs the incoming red light and has no blue light available to reflect"),
        ("a pure white sheet of paper", "red", "it reflects all incoming light, which in this case is pure red light"),
    ])
    prompt = (
        f"In a completely darkened photography darkroom, the room is illuminated exclusively by **monochromatic red light**.\n\n"
        f"What colour will **{target[0]}** appear to an observer, and why?"
    )
    correct_opt = f"It will appear **{target[1]}**, because {target[2]}."
    wrong_color = "yellow" if target[1] != "yellow" else "blue"
    options = [
        correct_opt,
        f"It will appear **{wrong_color}**, because red illumination alters the molecular structure of pigments.",
        "It will become completely invisible and transparent like air.",
        "It will glow with bright violet light due to chromatic excitation.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Illumination under Monochromatic Red Light:**\n"
        f"- An object can only reflect light wavelengths that are actually present in the illuminating light source.\n"
        f"- Monochromatic red light contains only red wavelengths.\n"
        f"- {target[0]}: {target[2]}.\n"
        f"- Therefore, it appears **{target[1]}**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_34_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "34_perceiving_coloured_objects_under_monochromatic_red_illumination",
        "question_family_id": "34_perceiving_coloured_objects_under_monochromatic_red_illumination",
        "hints": {
            "tier_1": f"Can {target[0]} reflect red light, or does it absorb red light?",
            "tier_2": f"If it reflects red, it looks red. If it absorbs red, it looks black.",
            "tier_3": f"It will appear {target[1]} because {target[2]}.",
        },
        "misconception_tags": ["objects_maintain_white_light_colour_under_monochromatic_light"],
    }


def arch_35_perceiving_coloured_objects_under_monochromatic_blue_illumination(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice([
        ("a pure blue blazer", "blue", "it reflects the incoming blue light into our eyes"),
        ("a pure red tomato", "black", "it absorbs the incoming blue light and has no red light available to reflect"),
        ("a pure yellow banana", "black", "it absorbs blue light and has no red/green wavelengths available to reflect"),
        ("a pure white mug", "blue", "it reflects all incident wavelengths, which in this case is pure blue light"),
    ])
    prompt = (
        f"In a science laboratory illuminated exclusively with **monochromatic blue light**, "
        f"a learner examines **{target[0]}**.\n\n"
        f"What colour does this object appear, and what is the scientific reason?"
    )
    correct_opt = f"It appears **{target[1]}**, because {target[2]}."
    wrong_color = "green" if target[1] != "green" else "orange"
    options = [
        correct_opt,
        f"It appears **{wrong_color}**, because blue light combines with chemical pigments to form an emulsion.",
        "It becomes luminous and emits fluorescent flashes.",
        "It retains its natural daylight colour because pigments have inherent color memory.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Illumination under Monochromatic Blue Light:**\n"
        f"- The only wavelengths available in the room are blue.\n"
        f"- An object that absorbs blue (such as a red or yellow object) reflects zero light, appearing **black**.\n"
        f"- An object that reflects blue (such as blue clothing or a white object) reflects blue light, appearing **blue**.\n"
        f"- For {target[0]}: {target[2]}.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_35_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "35_perceiving_coloured_objects_under_monochromatic_blue_illumination",
        "question_family_id": "35_perceiving_coloured_objects_under_monochromatic_blue_illumination",
        "hints": {
            "tier_1": f"Does {target[0]} reflect blue light or absorb blue light?",
            "tier_2": f"If it absorbs blue, no light reflects into the eye (looks black).",
            "tier_3": f"It appears {target[1]} because {target[2]}.",
        },
        "misconception_tags": ["color_constancy_misconception"],
    }


def arch_36_perceiving_coloured_objects_under_monochromatic_green_illumination(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice([
        ("a pure green pepper", "green", "it reflects the incoming green light into our eyes"),
        ("a pure red cricket ball", "black", "it absorbs green light and has no red light to reflect"),
        ("a pure blue pen", "black", "it absorbs green light and has no blue light to reflect"),
        ("a white laboratory coat", "green", "it reflects all incident light, reflecting the green light into our eyes"),
    ])
    prompt = (
        f"A theatre technician uses a pure **green spotlight** in a dark auditorium to illuminate **{target[0]}** on stage.\n\n"
        f"What colour does the audience perceive this object to be, and why?"
    )
    correct_opt = f"The audience perceives it as **{target[1]}**, because {target[2]}."
    wrong_color = "red" if target[1] != "red" else "yellow"
    options = [
        correct_opt,
        f"The audience perceives it as **{wrong_color}**, because green illumination reverses color frequencies.",
        "The object turns into a shadow without mass.",
        "The audience perceives it in its normal daylight colour because human eyes compensate automatically.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Illumination under Monochromatic Green Light:**\n"
        f"- Monochromatic green light delivers only green photons.\n"
        f"- {target[0]}: {target[2]}.\n"
        f"- Thus, it appears **{target[1]}**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_36_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "36_perceiving_coloured_objects_under_monochromatic_green_illumination",
        "question_family_id": "36_perceiving_coloured_objects_under_monochromatic_green_illumination",
        "hints": {
            "tier_1": f"Can {target[0]} reflect green light, or does it absorb green light?",
            "tier_2": f"If it absorbs green and reflects nothing, it appears black.",
            "tier_3": f"It appears {target[1]} because {target[2]}.",
        },
        "misconception_tags": ["monochromatic_lighting_confusion"],
    }


def arch_37_function_of_transparent_coloured_optical_filters(rng: random.Random) -> Dict[str, Any]:
    filter_color = rng.choice([
        ("red transparent filter", "red light", "all other colours (orange, yellow, green, blue, indigo, violet)"),
        ("green transparent filter", "green light", "all other colours (red, orange, yellow, blue, indigo, violet)"),
        ("blue transparent filter", "blue light", "all other colours (red, orange, yellow, green, indigo, violet)"),
    ])
    prompt = (
        f"When white light is directed through a sheet of **{filter_color[0]}**, "
        f"the light emerging on the other side is exclusively {filter_color[1]}.\n\n"
        f"How does a transparent coloured filter operate on white light?"
    )
    correct_opt = f"It transmits {filter_color[1]} while absorbing {filter_color[2]}."
    options = [
        correct_opt,
        f"It adds chemical red dyes to photons as they pass through the plastic.",
        "It speeds up light waves to three times the speed of sound.",
        "It turns white light into acoustic sound vibrations.",
    ]
    rng.shuffle(options)
    sol = (
        f"**How Optical Filters Work:**\n"
        f"- A coloured filter is a transparent material containing selective dyes.\n"
        f"- It allows only wavelengths of its own colour to pass through (**transmission**).\n"
        f"- All other visible spectral wavelengths are **absorbed** by the filter material.\n"
        f"- Therefore, a {filter_color[0]} transmits {filter_color[1]} and absorbs {filter_color[2]}.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_37_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "37_function_of_transparent_coloured_optical_filters",
        "question_family_id": "37_function_of_transparent_coloured_optical_filters",
        "hints": {
            "tier_1": f"What colour does a {filter_color[0]} let through, and what does it absorb?",
            "tier_2": f"It transmits {filter_color[1]} and absorbs all other colours.",
            "tier_3": f"Transmits {filter_color[1]} while absorbing {filter_color[2]}.",
        },
        "misconception_tags": ["filter_adds_color_dye_to_light_misconception"],
    }


def arch_38_primary_colours_of_light_red_green_blue_additive_mixing(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In colour science and electronic display technologies (such as television and smartphone screens), "
        f"colours are created using the **additive mixing of light**.\n\n"
        f"What are the three **primary colours of light**, and what colour of light is produced when all three are shone together at equal intensity onto a white screen?"
    )
    correct_opt = "Primary colours: Red, Green, and Blue (RGB); mixing all three produces White light."
    options = [
        correct_opt,
        "Primary colours: Red, Yellow, and Blue; mixing all three produces Black pigment.",
        "Primary colours: Cyan, Magenta, and Yellow; mixing all three produces Ultraviolet radiation.",
        "Primary colours: Orange, Green, and Purple; mixing all three produces Infrared warmth.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Primary Colours of Light (Additive Colour Mixing):**\n"
        f"- The primary colours of light are **Red, Green, and Blue** (RGB).\n"
        f"- They correspond to the three types of cone photoreceptors in the human retina.\n"
        f"- Unlike paint pigments (subtractive), adding light waves together combines radiant energy.\n"
        f"- Combining equal intensities of Red + Green + Blue light produces **White light**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_38_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "38_primary_colours_of_light_red_green_blue_additive_mixing",
        "question_family_id": "38_primary_colours_of_light_red_green_blue_additive_mixing",
        "hints": {
            "tier_1": "What are the primary colours of light (think of computer screens: RGB)?",
            "tier_2": "Red, Green, Blue are the primary colours of light; together they form White.",
            "tier_3": "Primary colours: Red, Green, Blue (RGB); together they produce White light.",
        },
        "misconception_tags": ["confusing_pigment_and_light_primaries"],
    }


def arch_39_secondary_colours_of_light_cyan_magenta_yellow_formation(rng: random.Random) -> Dict[str, Any]:
    combo = rng.choice([
        ("Red light and Green light", "Yellow light"),
        ("Red light and Blue light", "Magenta light (bright pinkish-purple)"),
        ("Green light and Blue light", "Cyan light (bright turquoise-blue)"),
    ])
    prompt = (
        f"When two primary colours of light overlap on a screen, they form a **secondary colour of light**.\n\n"
        f"What secondary colour of light is formed when **{combo[0]}** are mixed together at equal brightness?"
    )
    correct_opt = f"**{combo[1]}**."
    wrong_sec = "Black" if "Yellow" not in combo[1] else "Dark Brown"
    options = [
        correct_opt,
        f"{wrong_sec}, because mixing different colours of light cancels out the brightness.",
        "Infrared heat with no visible glow.",
        "Pure White light, regardless of which two colours are combined.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Secondary Colours of Light (Additive Combinations):**\n"
        f"- Red + Green = **Yellow**\n"
        f"- Red + Blue = **Magenta**\n"
        f"- Green + Blue = **Cyan**\n"
        f"- For {combo[0]}: forms {combo[1]}.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_39_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "39_secondary_colours_of_light_cyan_magenta_yellow_formation",
        "question_family_id": "39_secondary_colours_of_light_cyan_magenta_yellow_formation",
        "hints": {
            "tier_1": f"What colour does {combo[0]} make in additive light mixing?",
            "tier_2": "R+G=Yellow, R+B=Magenta, G+B=Cyan.",
            "tier_3": f"{combo[1]}.",
        },
        "misconception_tags": ["additive_subtractive_mixing_confusion"],
    }


def arch_40_structure_of_human_eye_cornea_pupil_iris_lens_retina(rng: random.Random) -> Dict[str, Any]:
    part = rng.choice([
        ("Cornea", "transparent outer protective layer that performs the majority of light refraction"),
        ("Iris", "coloured muscular ring that regulates the amount of light entering the eye by adjusting pupil size"),
        ("Pupil", "central aperture through which light enters the interior of the eyeball"),
        ("Crystalline Lens", "flexible transparent biconvex structure that fine-focuses light rays onto the retina"),
        ("Retina", "light-sensitive inner lining at the back of the eyeball containing photoreceptor rods and cones"),
    ])
    prompt = (
        f"In the biology and physics of vision, the human eye functions like a biological camera.\n\n"
        f"Which statement correctly identifies the anatomical function of the **{part[0]}**?"
    )
    correct_opt = f"The {part[0]} is the {part[1]}."
    options = [
        correct_opt,
        f"The {part[0]} is the acoustic membrane that detects high-frequency sound waves in the eye.",
        f"The {part[0]} is the bone that vibrates to produce visible light flashes in darkness.",
        f"The {part[0]} is the muscle that pumps blood directly into the optic nerve.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Anatomy of the Human Eye in Optics:**\n"
        f"- **Cornea:** Transparent curved front surface; does most initial focusing/refraction.\n"
        f"- **Iris:** Coloured diaphragm that dilates or constricts to control pupil diameter.\n"
        f"- **Pupil:** Aperture letting light into the eye.\n"
        f"- **Lens:** Convex lens adjusted by ciliary muscles to focus objects onto the retina.\n"
        f"- **Retina:** Screen containing rods and cones that convert light into nerve signals.\n"
        f"- **Optic Nerve:** Transmits electrical nerve impulses to the visual cortex of the brain.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_40_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "40_structure_of_human_eye_cornea_pupil_iris_lens_retina",
        "question_family_id": "40_structure_of_human_eye_cornea_pupil_iris_lens_retina",
        "hints": {
            "tier_1": f"What is the optical role of the {part[0]}?",
            "tier_2": f"The {part[0]} is the {part[1][:40]}...",
            "tier_3": f"The {part[0]} is the {part[1]}.",
        },
        "misconception_tags": ["eye_organ_function_confusion"],
    }


def arch_41_function_of_retina_photoreceptor_cells_rods_and_cones(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The retina at the back of the human eyeball contains two specialized types of photoreceptor cells: **rods** and **cones**.\n\n"
        f"What is the functional difference between rods and cones in human vision?"
    )
    correct_opt = "Rods are highly sensitive in dim light and detect black, white, and movement; cones operate in bright light and are responsible for sharp detail and colour vision (red, green, and blue sensitive)."
    options = [
        correct_opt,
        "Rods detect colour in daylight, while cones only detect sound waves at night.",
        "Rods are located in the cornea, while cones are located in the ear canal.",
        "Rods and cones perform identical functions, differing only in their physical length.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Rods vs Cones Photoreceptors:**\n"
        f"- **Rods (~120 million per eye):** Extremely sensitive to low light levels. Do not detect colour; responsible for night/scotopic vision, peripheral vision, and motion detection.\n"
        f"- **Cones (~6 million per eye):** Require bright light. Concentrated in the fovea centralis; responsible for high visual acuity and colour perception via three varieties sensitive to red, green, and blue wavelengths.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_41_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "41_function_of_retina_photoreceptor_cells_rods_and_cones",
        "question_family_id": "41_function_of_retina_photoreceptor_cells_rods_and_cones",
        "hints": {
            "tier_1": "Which cells detect colour: rods or cones?",
            "tier_2": "Cones = Colour (bright light); Rods = night vision / black and white (dim light).",
            "tier_3": "Rods detect dim light / black & white; cones detect colour in bright light.",
        },
        "misconception_tags": ["rods_cones_function_inversion"],
    }


def arch_42_convex_converging_lenses_and_focal_point_properties(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A magnifying glass uses a **convex (converging) lens** that is thicker in the middle than at the edges.\n\n"
        f"What happens to parallel rays of light when they pass through a convex lens?"
    )
    correct_opt = "The light rays bend inwards (converge) and meet at a single real focal point ($F$) on the principal axis behind the lens."
    options = [
        correct_opt,
        "The light rays bend outwards (diverge) and spread further apart into space.",
        "The light rays stop completely and reflect backwards as parallel heat rays.",
        "The light rays pass through without bending because glass lenses cannot refract light.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Convex (Converging) Lens Optics:**\n"
        f"- A convex lens is thicker at its center than at its edges.\n"
        f"- As parallel incident rays enter and leave the curved glass surfaces, refraction bends them toward the principal axis.\n"
        f"- The rays converge to intersect at a common point called the **principal focal point** ($F$).\n"
        f"- Because real light rays intersect here, this is a **real focus** (which can ignite dry paper when focusing sunlight).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_42_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "42_convex_converging_lenses_and_focal_point_properties",
        "question_family_id": "42_convex_converging_lenses_and_focal_point_properties",
        "hints": {
            "tier_1": "Do convex lenses converge (bring together) or diverge (spread out) light rays?",
            "tier_2": "Convex lenses converge light rays inwards to meet at a focal point.",
            "tier_3": "Light rays bend inwards (converge) and meet at a real focal point.",
        },
        "misconception_tags": ["convex_lens_diverges_misconception"],
    }


def arch_43_concave_diverging_lenses_and_focal_properties(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A **concave (diverging) lens** is thinner in the middle and thicker at the outer edges.\n\n"
        f"What happens to a parallel beam of light rays when it passes through a concave lens?"
    )
    correct_opt = "The light rays bend outwards (diverge), spreading apart as if they originated from a virtual focal point situated in front of the lens."
    options = [
        correct_opt,
        "The light rays converge inwards to a real focus point where they ignite paper.",
        "The light rays are absorbed 100% and converted into radio waves.",
        "The light rays rotate 90 degrees and travel vertically along the glass surface.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Concave (Diverging) Lens Optics:**\n"
        f"- A concave lens is curved inwards (thinner at the center than at the edges).\n"
        f"- When parallel light rays enter, refraction bends them away from the principal axis (**divergence**).\n"
        f"- The rays spread apart; when traced backwards, they appear to originate from an imaginary point called the **virtual focal point**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_43_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "43_concave_diverging_lenses_and_focal_properties",
        "question_family_id": "43_concave_diverging_lenses_and_focal_properties",
        "hints": {
            "tier_1": "Do concave lenses spread rays apart or bring them together?",
            "tier_2": "Concave lenses diverge (spread apart) parallel light rays.",
            "tier_3": "Light rays bend outwards (diverge), spreading apart from a virtual focus.",
        },
        "misconception_tags": ["concave_lens_converges_misconception"],
    }


def arch_44_correcting_short_sightedness_myopia_using_concave_lenses(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner diagnosed with **short-sightedness (myopia)** can see nearby objects clearly, "
        f"but distant objects (like the classroom chalkboard) appear blurry.\n\n"
        f"Why does this vision defect occur, and what type of optical lens is prescribed to correct it?"
    )
    correct_opt = "The eyeball is too long (or the eye lens refracts too strongly), focusing light in front of the retina; it is corrected using **concave (diverging) lenses** to spread rays slightly before they enter the eye."
    options = [
        correct_opt,
        "The eyeball is too short, focusing light behind the retina; it is corrected using convex lenses.",
        "The retina has zero rod cells; it is corrected by wearing polarized sunglasses indoors.",
        "The cornea is opaque; it is corrected by wearing glass prisms that invert visual rays.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Short-Sightedness (Myopia):**\n"
        f"- **Defect:** Light rays from distant objects are brought to a focus **in front of the retina** because the eyeball is too elongated or the lens is too curved.\n"
        f"- **Correction:** A **concave (diverging) lens** is placed in front of the eye. It slightly diverges incoming parallel rays before they enter the cornea, allowing the eye's lens to focus them precisely onto the retina.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_44_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "44_correcting_short_sightedness_myopia_using_concave_lenses",
        "question_family_id": "44_correcting_short_sightedness_myopia_using_concave_lenses",
        "hints": {
            "tier_1": "Where do light rays focus in myopia: in front of or behind the retina?",
            "tier_2": "In myopia, light focuses in front of retina; concave diverging lenses correct this.",
            "tier_3": "Focuses in front of retina; corrected using concave (diverging) lenses.",
        },
        "misconception_tags": ["myopia_hyperopia_lens_inversion"],
    }


def arch_45_correcting_long_sightedness_hyperopia_using_convex_lenses(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"An adult diagnosed with **long-sightedness (hyperopia)** can see distant mountains sharply, "
        f"but struggles to read small print in a book held close to the face.\n\n"
        f"Why does this vision defect occur, and what type of optical lens is used to correct it?"
    )
    correct_opt = "The eyeball is too short (or the eye lens is too flat), focusing light behind the retina; it is corrected using **convex (converging) lenses** to provide additional converging power."
    options = [
        correct_opt,
        "The eyeball is too long, focusing light in front of the retina; it is corrected using concave lenses.",
        "The optic nerve is disconnected; it is corrected using flat plane mirrors.",
        "The pupil is permanently closed; it is corrected using laser eye patches.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Long-Sightedness (Hyperopia):**\n"
        f"- **Defect:** Light rays from nearby objects reach the retina before converging, focusing **behind the retina** because the eyeball is too short or the lens cannot become convex enough.\n"
        f"- **Correction:** A **convex (converging) lens** provides extra convergence before light reaches the cornea, bringing the focal point forward onto the retina surface.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_45_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "45_correcting_long_sightedness_hyperopia_using_convex_lenses",
        "question_family_id": "45_correcting_long_sightedness_hyperopia_using_convex_lenses",
        "hints": {
            "tier_1": "Where do rays focus in hyperopia: in front of or behind the retina?",
            "tier_2": "In hyperopia, light focuses behind the retina; convex converging lenses correct it.",
            "tier_3": "Focuses behind retina; corrected using convex (converging) lenses.",
        },
        "misconception_tags": ["hyperopia_corrected_with_concave_misconception"],
    }


def arch_46_misconception_eyes_emit_light_rays_to_see_objects(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In ancient times, philosophers believed in the 'extramission theory'—that the human eye shoots out "
        f"invisible visual rays to touch and detect objects in the surrounding world.\n\n"
        f"Which simple, everyday observation definitively disproves this theory and confirms that light enters the eye from objects?"
    )
    correct_opt = "In a pitch-black room with zero light sources, humans cannot see anything at all, proving that our eyes cannot emit light and rely entirely on external light entering them."
    options = [
        correct_opt,
        "Wearing sunglasses turns all objects inside out.",
        "Laser pointers can only illuminate mirrors and cannot shine on wood.",
        "Eyes emit infrared rays that can be felt by thermometer sensors on the forehead.",
    ]
    rng.shuffle(options)
    sol = (
        f"**The Physics of Seeing (Intromission vs Extramission):**\n"
        f"- If our eyes emitted visual rays, we would be able to see clearly in total darkness simply by opening our eyes.\n"
        f"- In reality, in a lightproof room with no light sources, we are completely blind.\n"
        f"- Vision occurs exclusively by the **intromission** process: light emitted by a luminous source or reflected off a non-luminous object enters the eye through the pupil and strikes the retina.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_46_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "46_misconception_eyes_emit_light_rays_to_see_objects",
        "question_family_id": "46_misconception_eyes_emit_light_rays_to_see_objects",
        "hints": {
            "tier_1": "Can you see anything if you are in a completely dark room?",
            "tier_2": "In total darkness, eyes see nothing, disproving that eyes emit visual rays.",
            "tier_3": "In a pitch-black room with zero light, humans cannot see anything at all.",
        },
        "misconception_tags": ["extramission_theory_of_vision"],
    }


def arch_47_misconception_light_travels_only_a_short_distance_before_running_out(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner suggests: 'Light only travels a few kilometers before it gets tired, loses all its energy, and disappears into nothingness.'\n\n"
        f"Which astronomical evidence proves that light travels indefinitely across the vacuum of space unless absorbed by matter?"
    )
    correct_opt = "Light from distant stars and galaxies has traveled across billions of trillions of kilometers through the vacuum of space for billions of years to reach our eyes and telescopes on Earth."
    options = [
        correct_opt,
        "The Sun must be refueled every evening with coal to restart its light beam.",
        "Laser beams circle the Earth five times every second without needing power.",
        "Light rays turn into heavy gold atoms when they stop moving in space.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Indefinite Propagation of Light in Vacuum:**\n"
        f"- Light is radiant electromagnetic energy; it does not experience friction or mechanical fatigue.\n"
        f"- In a vacuum with no matter to absorb or scatter it, light travels indefinitely at $c = 300{{,}}000\\text{{ km/s}}$ without losing speed.\n"
        f"- Starlight from galaxies billions of light-years away reaches our telescopes unchanged in fundamental nature.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_47_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "47_misconception_light_travels_only_a_short_distance_before_running_out",
        "question_family_id": "47_misconception_light_travels_only_a_short_distance_before_running_out",
        "hints": {
            "tier_1": "How far has starlight traveled to reach our eyes at night?",
            "tier_2": "Starlight travels billions of light years through vacuum without running out of energy.",
            "tier_3": "Light from distant stars travels billions of light years across space to reach Earth.",
        },
        "misconception_tags": ["light_fatigue_distance_misconception"],
    }


def arch_48_misconception_colours_exist_as_matter_inside_objects_in_the_dark(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A student claims: 'A red apple is still red in a pitch-black locked safe with zero light, because redness is a physical substance painted inside the atoms of the apple.'\n\n"
        f"Why is this claim scientifically inaccurate?"
    )
    correct_opt = "Colour is not a standalone physical substance; it is a perceptual sensation that requires light wavelengths to be reflected into an eye. In total darkness, zero light wavelengths exist to be reflected, so the object has no visible colour."
    options = [
        correct_opt,
        "In total darkness, all atoms turn into transparent liquid hydrogen.",
        "The apple turns permanently green whenever a safe door is locked.",
        "Redness only exists when sound waves vibrate the fruit's skin.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Nature of Colour:**\n"
        f"- Colour is an optical and perceptual phenomenon, not a material entity.\n"
        f"- An object merely possesses chemical pigments with specific electronic absorption and reflection bands.\n"
        f"- Without incident light photons to reflect and reach a photoreceptor, no colour sensation can occur.\n"
        f"- In total darkness, there is absence of light, meaning no colour exists.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_48_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "48_misconception_colours_exist_as_matter_inside_objects_in_the_dark",
        "question_family_id": "48_misconception_colours_exist_as_matter_inside_objects_in_the_dark",
        "hints": {
            "tier_1": "Can colour exist without any light to reflect off the object?",
            "tier_2": "Colour is a sensation produced by reflected light; without light, no colour exists.",
            "tier_3": "Colour requires reflected light wavelengths; in total darkness, no colour exists.",
        },
        "misconception_tags": ["color_as_inherent_material_substance"],
    }


def arch_49_experimental_design_variables_in_light_and_optics_investigations(rng: random.Random) -> Dict[str, Any]:
    investigation = rng.choice([
        ("investigating how the angle of incidence affects the angle of reflection on a plane mirror",
         "Angle of incidence (degrees to normal)",
         "Angle of reflection (degrees to normal)",
         "Type of mirror, light wavelength/colour, and alignment of normal line"),
        ("investigating how the distance between an opaque object and a light source affects the size of its shadow",
         "Distance between light source and opaque object",
         "Height and width of shadow cast on screen",
         "Light source intensity, screen distance, and object dimensions"),
        ("investigating how the optical density of different transparent liquids affects the angle of refraction",
         "Type of transparent liquid (water, oil, glycerol)",
         "Angle of refraction in the liquid",
         "Angle of incidence in air, container shape, and light colour"),
    ])
    prompt = (
        f"In a Grade 8 Natural Sciences practical investigation: '{investigation[0]}'.\n\n"
        f"Which option correctly identifies the **Independent Variable**, **Dependent Variable**, and a **Controlled Variable**?"
    )
    correct_opt = f"Independent: {investigation[1]} | Dependent: {investigation[2]} | Controlled: {investigation[3]}"
    wrong_swap = f"Independent: {investigation[2]} | Dependent: {investigation[1]} | Controlled: {investigation[3]}"
    options = [
        correct_opt,
        wrong_swap,
        f"Independent: {investigation[3]} | Dependent: {investigation[1]} | Controlled: {investigation[2]}",
        f"Independent: Room temperature | Dependent: Atmospheric humidity | Controlled: {investigation[1]}",
    ]
    rng.shuffle(options)
    sol = (
        f"**Variables in the Optics Investigation:**\n"
        f"- **Independent Variable (deliberately changed by investigator):** {investigation[1]}.\n"
        f"- **Dependent Variable (measured response):** {investigation[2]}.\n"
        f"- **Controlled Variable (kept constant for fair testing):** {investigation[3]}.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_49_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "49_experimental_design_variables_in_light_and_optics_investigations",
        "question_family_id": "49_experimental_design_variables_in_light_and_optics_investigations",
        "hints": {
            "tier_1": "What is changed (independent), and what is measured (dependent)?",
            "tier_2": f"Independent: {investigation[1]}; Dependent: {investigation[2]}.",
            "tier_3": f"Independent: {investigation[1]} | Dependent: {investigation[2]} | Controlled: {investigation[3]}.",
        },
        "misconception_tags": ["variable_identification_error"],
    }


def arch_50_visible_light_comprehensive_diagnostic_evaluation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Evaluate the following optical statements synthesizing the behavior of **visible light**:\n\n"
        f"Which statement is entirely **scientifically correct** in every detail?"
    )
    correct_opt = (
        "Light travels in straight lines at 300 000 km/s in a vacuum, refracts towards the normal when slowing down in denser media, "
        "and white light disperses into ROYGBIV because higher frequencies like violet slow down and bend the most."
    )
    options = [
        correct_opt,
        (
            "Light requires a material medium to propagate, accelerates upon entering glass, "
            "and human eyes send out visual rays to detect objects."
        ),
        (
            "Plane mirrors form real, inverted reflections; white objects absorb all radiation; "
            "and red light refracts more than violet light in a prism."
        ),
        (
            "A pinhole camera forms an upright projection because light curves around apertures, "
            "and primary colours of light are red, yellow, and blue."
        ),
    ]
    rng.shuffle(options)
    sol = (
        f"**Comprehensive Optics Summary:**\n"
        f"- Light is radiant electromagnetic energy traveling in straight lines at $c = 300{{,}}000\\text{{ km/s}}$ in a vacuum.\n"
        f"- In plane mirrors, reflections are virtual, upright, same size, and laterally inverted.\n"
        f"- When light enters an optically denser medium (air into glass), it slows down and refracts towards the normal.\n"
        f"- In a prism, dispersion separates white light into ROYGBIV because violet has the shortest wavelength and bends the most.\n"
        f"- Primary colours of light are Red, Green, and Blue (RGB), which combine to produce white light.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_light_50_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "50_visible_light_comprehensive_diagnostic_evaluation",
        "question_family_id": "50_visible_light_comprehensive_diagnostic_evaluation",
        "hints": {
            "tier_1": "Recall: Light travels in straight lines; violet bends most; slowing down bends towards normal.",
            "tier_2": "Speed is 300,000 km/s; slows in denser medium (bends towards normal); violet bends most in ROYGBIV.",
            "tier_3": "Light travels in straight lines at 300 000 km/s, refracts towards normal in denser media, violet bends most.",
        },
        "misconception_tags": ["optics_core_principles_confusion"],
    }
