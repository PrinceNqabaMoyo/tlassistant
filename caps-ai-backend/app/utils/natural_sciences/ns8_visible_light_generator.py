"""Natural Sciences Grade 8 Term 3: Visible Light Generator.

Strictly grounded in curriculum_docs_auto/NaturalSciences_Gr8/Syllabus.md.
Covers:
- light_radiation_speed_and_propagation: Rectilinear propagation, speed of light (300,000 km/s), solar transit time calculation (500 s).
- spectrum_of_visible_light_dispersion: Dispersion through triangular glass prism into ROYGBIV spectrum; frequency vs refraction.
- opaque_transparent_translucent_shadows: Transmission vs shadow casting; pinhole camera image inversion.
- absorption_reflection_color_perception: Why objects appear coloured; absorption of frequencies vs thermal heating.
- laws_of_reflection_and_refraction: Law of reflection (angle i = angle r); refraction when changing optical media (towards/away from normal).

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations
import math

import random
from typing import Any, Dict, List, Optional


SUBSKILLS = [
    "light_radiation_speed_and_propagation",
    "spectrum_of_visible_light_dispersion",
    "opaque_transparent_translucent_shadows",
    "absorption_reflection_color_perception",
    "laws_of_reflection_and_refraction",
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _build_light_speed_propagation(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    targets = [
        ("the Sun to Earth", 150000000, "sunlight", 500, "8 minutes and 20 seconds"),
        ("the Sun to Mars", 228000000, "solar rays", 760, "12 minutes and 40 seconds"),
        ("Earth to the Moon", 384000, "reflected moonlight", 1.28, "1,28 seconds")
    ]
    dest, dist, ray_name, sec, min_str = rng.choice(targets)
    prompt = (
        f"Light travels as radiant electromagnetic energy in straight lines (rectilinear propagation) through the vacuum of space at 300 000 km/s.\n\n"
        f"1. State the constant speed of light in a vacuum ($v$) in kilometers per second (km/s).\n"
        f"2. The average distance from {dest} is approximately ${dist:,}\\text{{ km}}$. "
        f"Calculate the time taken for {ray_name} to cross this distance.\n"
        f"3. Express this calculated time in appropriate minutes and seconds."
    )
    sample_answer = (
        f"1. Speed of light: 300 000 km/s\n"
        f"2. Time calculation:\n"
        f"t = Distance / Speed = {dist:,} km / 300 000 km/s = {sec} seconds\n"
        f"3. Time in minutes/seconds: {min_str}"
    )
    sol = (
        f"Marking Rubric (4 marks total):\n"
        f"1. Speed of light: 300 000 km/s [1 mark].\n"
        f"2. Formula application: $t = \\frac{{d }}{{v }}$ [1 mark].\n"
        f"3. Calculated seconds: {sec} seconds [1 mark].\n"
        f"4. Conversion: {min_str} [1 mark]."
    )
    return {
        "id": _make_id("ns8_light_speed", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "light_radiation_speed_and_propagation",
        "question_family_id": "light_radiation_speed_and_propagation",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Visible Light > Speed of light calculations",
        "hints": {
            "tier_1": "Use the formula: Time = Distance / Speed.",
            "tier_2": "Divide 150 000 000 km by 300 000 km/s.",
            "tier_3": "Time = 500 seconds, which is 8 minutes and 20 seconds."
        },
        "misconception_tags": ["speed_of_light_equals_sound_misconception"]
    }


def _build_spectrum_dispersion(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    colors = "Red, Orange, Yellow, Green, Blue, Indigo, Violet"
    setups = [
        "A narrow beam of white sunlight passes through an equilateral triangular glass prism in a darkened laboratory.",
        "A focused beam of bright white halogen light strikes the surface of an optical glass prism during a physics demonstration.",
        "Direct natural sunlight passes through the edge of a beveled glass aquarium tank in a school science laboratory."
    ]
    prompt = (
        f"{rng.choice(setups)} As it exits the medium, the beam fans out into a vibrant spectrum of colours resembling a rainbow.\n\n"
        f"1. What is the scientific term for the separation of white light into its component spectral colours?\n"
        f"2. List the seven colours of the visible spectrum in order from lowest frequency (longest wavelength) to highest frequency (shortest wavelength).\n"
        f"3. Which colour undergoes the greatest refraction (bending) as it passes through the prism, and why?"
    )
    sample_answer = (
        "1. Dispersion of light.\n"
        f"2. {colors} (ROYGBIV).\n"
        "3. Violet light undergoes the greatest refraction because it has the highest frequency and shortest wavelength, which causes it to slow down the most in glass."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Term: Dispersion of light [1 mark].\n"
        f"2. Sequence: {colors} [2 marks for complete order; 1 mark if 1 error].\n"
        "3. Maximum bending: Violet bends the most because of its higher frequency / shorter wavelength [1 mark]."
    )
    return {
        "id": _make_id("ns8_dispersion", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "spectrum_of_visible_light_dispersion",
        "question_family_id": "spectrum_of_visible_light_dispersion",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Visible Light > Dispersion and the visible spectrum",
        "hints": {
            "tier_1": "Remember the acronym ROYGBIV for the visible rainbow colours.",
            "tier_2": "The prism separates light because each colour slows down and bends by a different amount.",
            "tier_3": "Violet bends the most; red bends the least."
        },
        "misconception_tags": ["prism_creates_colour_chemicals_misconception"]
    }


def _build_shadows_pinhole(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    src = rng.choice(["a lit wax candle flame", "a bright miniature incandescent lamp", "an optical projection light source", "a focused white LED torch"])
    d = rng.choice([20, 25, 30, 35])
    prompt = (
        f"In an optical investigation, a learner constructs a simple pinhole camera from an opaque shoe box with a tiny pinhole "
        f"at one end and a translucent tracing paper screen at the opposite end. Placed at a distance of {d} cm from {src} in a dark room:\n\n"
        "1. Describe the orientation of the image formed on the tracing paper screen (upright or inverted).\n"
        "2. Explain using the rectilinear propagation of light (light travels in straight lines) why this image orientation occurs.\n"
        "3. Predict what happens to the sharpness and brightness of the image if the pinhole is enlarged into a wide 1 cm hole."
    )
    sample_answer = (
        "1. The image is inverted (upside down and left-to-right reversed).\n"
        "2. Because light travels in straight lines, rays from the top of the candle flame travel downwards through the tiny hole to the bottom of the screen, and rays from the bottom of the candle travel upwards to the top of the screen.\n"
        "3. The image becomes much brighter because more light enters, but it becomes extremely blurry / out of focus because overlapping rays from many angles strike the screen."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Orientation: Inverted / upside down [1 mark].\n"
        "2. Ray geometry: Straight line propagation means top rays hit the bottom and bottom rays hit the top [2 marks].\n"
        "3. Enlarged pinhole prediction: Brighter but blurry / loss of sharpness [1 mark]."
    )
    return {
        "id": _make_id("ns8_pinhole", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "opaque_transparent_translucent_shadows",
        "question_family_id": "opaque_transparent_translucent_shadows",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Visible Light > Pinhole camera and shadow formation",
        "hints": {
            "tier_1": "Light travels in straight lines through the tiny pinhole.",
            "tier_2": "Rays cross over at the pinhole, inverting the image on the screen.",
            "tier_3": "The image is upside down; making the hole bigger makes it brighter but blurry."
        },
        "misconception_tags": ["pinhole_inverts_due_to_gravity_misconception"]
    }


def _build_color_perception(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    cases = [
        {"object": "a ripe red tomato", "reflects": "red light frequencies", "absorbs": "all other frequencies (orange, yellow, green, blue, violet)"},
        {"object": "a green leaf", "reflects": "green light frequencies", "absorbs": "red, blue, and other light frequencies"},
        {"object": "a blue school blazer", "reflects": "blue light frequencies", "absorbs": "red, orange, yellow, and green frequencies"}
    ]
    c = rng.choice(cases)
    prompt = (
        f"When white sunlight falls onto **{c['object']}**, our eyes perceive it as having a distinct colour.\n\n"
        f"1. Explain scientifically why the object appears to have this colour in terms of light absorption and reflection.\n"
        f"2. If this object is placed in a completely dark room and illuminated exclusively with monochromatic blue light, what colour will it appear to human observers?\n"
        f"3. Explain why wearing a black T-shirt outdoors on a sunny summer day in South Africa makes a person feel much hotter than wearing a white T-shirt."
    )
    sample_answer = (
        f"1. The object absorbs {c['absorbs']} and reflects {c['reflects']} into our eyes.\n"
        "2. If illuminated only with blue light, it will appear blue if it reflects blue, or black if it absorbs blue.\n"
        "3. A black T-shirt absorbs all frequencies of visible light and converts the radiant light energy into thermal heat energy. A white T-shirt reflects all frequencies of light and therefore stays significantly cooler."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        f"1. Colour mechanism: Reflects {c['reflects']} and absorbs {c['absorbs']} [2 marks].\n"
        "2. Monochromatic illumination prediction: Explains visual outcome based on reflection vs absorption [1 mark].\n"
        "3. Thermal absorption: Black absorbs all light frequencies converting them to heat; white reflects radiant energy [1 mark]."
    )
    return {
        "id": _make_id("ns8_color_percept", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "absorption_reflection_color_perception",
        "question_family_id": "absorption_reflection_color_perception",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Visible Light > Light absorption, reflection, and colour",
        "hints": {
            "tier_1": "You only see the colour that bounces off the object into your eye.",
            "tier_2": "All other colours of light are absorbed by the pigments.",
            "tier_3": "Black absorbs all light and heats up; white reflects all light."
        },
        "misconception_tags": ["objects_create_their_own_light_misconception"]
    }


def _build_reflection_refraction(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    angle_i = rng.choice([30, 45, 60])
    prompt = (
        f"A light ray in air strikes the surface of a flat glass mirror at an angle of incidence of **{angle_i}°** to the normal.\n\n"
        f"1. State the Law of Reflection.\n"
        f"2. What is the angle of reflection ($\\theta_r$) for this ray?\n"
        f"3. When a ray of light passes from air into a rectangular glass block, explain whether it bends **towards the normal** or **away from the normal**, and state the scientific reason for this directional change."
    )
    sample_answer = (
        "1. The Law of Reflection states that the angle of incidence is equal to the angle of reflection (Angle i = Angle r), and both rays lie in the same plane.\n"
        f"2. Angle of reflection = {angle_i}°.\n"
        "3. It bends towards the normal because glass has a higher optical density than air, which causes the light ray to slow down upon entering the glass."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Law of Reflection statement: Angle of incidence equals angle of reflection [1 mark].\n"
        f"2. Calculation: $\\theta_r = {angle_i}^\\circ$ [1 mark].\n"
        "3. Direction of refraction: Bends towards the normal [1 mark].\n"
        "4. Refraction cause: Light travels slower in optically denser medium (glass) than in air [1 mark]."
    )
    refr_angle = round(math.degrees(math.asin(math.sin(math.radians(angle_i)) / 1.52)), 1)
    return {
        "id": _make_id("ns8_refl_refr", seed, idx),
        "question_type": "paragraph",
        "modality": "optics",
        "optics_spec": {
            "type": "interface_refraction",
            "medium_1": {"name": "Air", "refractive_index": 1.0},
            "medium_2": {"name": "Crown Glass", "refractive_index": 1.52},
            "angle_incidence_deg": angle_i,
            "angle_refraction_deg": refr_angle,
            "critical_angle_deg": 41.1,
            "normal_line": True,
            "boundary_label": "Air / Crown Glass Interface",
        },
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "laws_of_reflection_and_refraction",
        "question_family_id": "laws_of_reflection_and_refraction",
        "curriculum_reference": "Natural Sciences Gr8 Term 3 > Visible Light > Reflection and refraction",
        "hints": {
            "tier_1": "Angle of incidence always equals angle of reflection.",
            "tier_2": "When light slows down entering a denser material, it bends towards the normal.",
            "tier_3": f"Angle of reflection is {angle_i}°; bends towards normal in glass."
        },
        "misconception_tags": ["angle_measured_from_surface_not_normal_misconception"]
    }


def generate(archetype: Optional[str] = None, seed: Optional[int] = None, count: int = 1, **kwargs) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    results = []
    for idx in range(count):
        target = archetype or rng.choice(SUBSKILLS)
        if target == "light_radiation_speed_and_propagation":
            item = _build_light_speed_propagation(rng, seed, idx)
        elif target == "spectrum_of_visible_light_dispersion":
            item = _build_spectrum_dispersion(rng, seed, idx)
        elif target == "opaque_transparent_translucent_shadows":
            item = _build_shadows_pinhole(rng, seed, idx)
        elif target == "absorption_reflection_color_perception":
            item = _build_color_perception(rng, seed, idx)
        elif target == "laws_of_reflection_and_refraction":
            item = _build_reflection_refraction(rng, seed, idx)
        else:
            item = _build_light_speed_propagation(rng, seed, idx)
        results.append(item)
    return results


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)
