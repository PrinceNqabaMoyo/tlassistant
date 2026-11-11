"""Grade 8 Natural Sciences - Looking into Space: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr8/Term 4/03. Looking into space.md
Focus:
Early viewing (naked eye, pupil aperture limits, indigenous African starlore - Isilimela/Pleiades, Inkosazana/Sirius,
constellations as celestial maps), Telescopes as light buckets (aperture, area proportional to D^2, comparison math,
angular resolution, magnification misconception), Optical telescopes (refractors, Lippershey & Galileo discoveries,
chromatic aberration, physical limits of refractors, reflectors, Newton's invention, reflector advantages,
Newtonian vs Cassegrain), SALT (Sutherland Karoo site, 11-meter segmented hexagonal array, fixed altitude tracker,
spectroscopy, light pollution & Astronomy Geographic Advantage Act).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_naked_eye_astronomy_pupil_aperture_limitations(rng: random.Random) -> Dict[str, Any]:
    pupil_mm = rng.choice(["5 mm to 7 mm", "approximately 6 to 8 mm in pitch darkness"])
    prompt = (
        f"For thousands of years, humans studied the night sky using only the naked human eye, whose dilated pupil aperture reaches {pupil_mm}.\n\n"
        "What fundamental optical limitation does this narrow pupil aperture impose on human night-sky observation?"
    )
    correct = "It collects only a minute fraction of the photons emitted by distant celestial bodies, making faint nebulae and distant stars completely invisible."
    options = [
        correct,
        "It causes human retinas to emit ultraviolet radiation that repels distant starlight.",
        "It inverts all distant objects so that stars appear upside down.",
        "It freezes all light waves into solid particles that bounce off the cornea."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Eye as an optical aperture:\n"
        "The human eye has an entrance pupil diameter of only ~5–8 mm.\n"
        "Step 2: Photon collection limitation:\n"
        "Light gathering depends on aperture area (A = πr²). Because human eyes capture very few photons per second, our perception is limited to bright stars (apparent magnitude < 6). Telescopes overcome this limitation by acting as giant light buckets."
    )
    return {
        "id": f"ns8_tel_01_{rng.randint(100000, 999999)}",
        "subskill": "01_naked_eye_astronomy_pupil_aperture_limitations",
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
            "tier_1": "Why can't we see dim stars with our eyes alone?",
            "tier_2": "Our small pupil collects too few photons from faint objects.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["naked_eye_aperture_photon_limit"]
    }


def arch_02_indigenous_starlore_pleiades_isilimela_planting(rng: random.Random) -> Dict[str, Any]:
    lang, name, season = rng.choice([
        ("isiXhosa", "Isilimela", "the agricultural ploughing and planting season"),
        ("isiZulu", "Isilimela", "the time to dig the soil and sow crops"),
        ("Sesotho", "Selemela", "the beginning of the agricultural year and spring planting")
    ])
    prompt = (
        f"In indigenous South African astronomical starlore, the open star cluster known Westernly as the Pleiades (the Seven Sisters) is named **{name}** in {lang}.\n\n"
        f"What vital seasonal and cultural milestone was signaled by the morning rising of **{name}** in June?"
    )
    correct = f"It signaled the arrival of winter/spring and the start of {season}."
    options = [
        correct,
        "It signaled an immediate total solar eclipse requiring people to stay indoors for a month.",
        "It signaled that the ocean tides were permanently drying up along the coast.",
        "It signaled the arrival of snowstorms that would destroy all crops."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Indigenous cultural astronomy:\n"
        f"In {lang} tradition, {name} (the Pleiades) is intrinsically linked to agriculture (the root 'lima' means to cultivate or plough).\n"
        "Step 2: Seasonal calendar:\n"
        f"Its heliacal rising on the eastern horizon just before sunrise in June served as a reliable celestial calendar marker for {season}."
    )
    return {
        "id": f"ns8_tel_02_{rng.randint(100000, 999999)}",
        "subskill": "02_indigenous_starlore_pleiades_isilimela_planting",
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
            "tier_1": f"What does the root of {name} relate to in farming?",
            "tier_2": f"It marks {season}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["indigenous_starlore_agricultural_calendar"]
    }


def arch_03_indigenous_starlore_sirius_inkosazana_harvest(rng: random.Random) -> Dict[str, Any]:
    star_name = rng.choice(["Sirius (the brightest star in the sky)", "Canopus (the second brightest star)"])
    if "Sirius" in star_name:
        indig_name = "Inkosazana (the Lady of the Heavens)"
        role = "associated with agricultural fertility and autumn harvest celebrations"
    else:
        indig_name = "Naka (the Horn Star) in Sotho/Tswana starlore"
        role = "observed carefully in winter dawn skies to forecast weather and grazing conditions"
    prompt = (
        f"Indigenous observers across Southern Africa closely monitored **{star_name}**, known traditionally as **{indig_name}**.\n\n"
        f"How did traditional communities utilize the seasonal appearance of **{indig_name}**?"
    )
    correct = f"It was {role}."
    options = [
        correct,
        "It was used as a weapon to reflect sunlight and set enemy boats on fire.",
        "It was considered an artificial lightbulb suspended from a weather balloon.",
        "It was ignored because indigenous people never looked at the stars."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Traditional African celestial knowledge:\n"
        f"Prominent bright stars like {star_name} carried rich cultural meaning and practical ecological value.\n"
        f"Step 2: Practical function:\n"
        f"{indig_name} was {role}."
    )
    return {
        "id": f"ns8_tel_03_{rng.randint(100000, 999999)}",
        "subskill": "03_indigenous_starlore_sirius_inkosazana_harvest",
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
            "tier_1": f"How was {indig_name} used in traditional society?",
            "tier_2": f"It was {role[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["indigenous_starlore_seasonal_forecasting"]
    }


def arch_04_constellations_definition_and_celestial_mapping(rng: random.Random) -> Dict[str, Any]:
    const = rng.choice(["Orion the Hunter", "Scorpius the Scorpion", "Crux the Southern Cross"])
    prompt = (
        f"Ancient cultures mapped the celestial sphere by grouping prominent stars into recognizable patterns called **constellations**, such as {const}.\n\n"
        "In physical reality, are the individual stars that form a constellation physically bound close together in outer space?"
    )
    correct = "No; constellations are chance 2D optical alignments of stars viewed from Earth, though the individual stars are actually located at wildly different 3D distances from us."
    options = [
        correct,
        "Yes; all stars in a constellation are physically glued together by solid ice ropes in deep space.",
        "Yes; every constellation is a single gigantic star that broke into pieces last century.",
        "Yes; the stars in a constellation all orbit a single central rocky asteroid together."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Nature of constellations:\n"
        "Constellations are arbitrary visual asterisms and sky-mapping conventions.\n"
        "Step 2: 3D perspective:\n"
        "Stars appearing near each other on the 2D dome of the sky often have immense depth separation. For example, in Orion, Bellatrix is ~250 light years away while Betelgeuse is ~640 light years away. They do not form a gravitationally bound cluster."
    )
    return {
        "id": f"ns8_tel_04_{rng.randint(100000, 999999)}",
        "subskill": "04_constellations_definition_and_celestial_mapping",
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
            "tier_1": "Are stars in a constellation at the same distance from Earth?",
            "tier_2": "No, they are chance line-of-sight alignments at vastly different distances.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["constellations_3d_depth_misconception"]
    }


def arch_05_telescope_primary_function_light_gathering_bucket(rng: random.Random) -> Dict[str, Any]:
    analogy = "a giant bucket collecting falling raindrops in a storm"
    prompt = (
        f"Astronomers often compare an astronomical telescope to **{analogy}**.\n\n"
        "What is the **primary physical function** of an astronomical telescope?"
    )
    correct = "To collect and concentrate as many faint photons of light as possible from distant celestial objects onto a detector or eyepiece."
    options = [
        correct,
        "To physically pull distant stars closer to Earth using magnetic gravitational beams.",
        "To illuminate distant planets by firing powerful searchlight beams into deep space.",
        "To magnify empty black space so it appears bright white."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Primary purpose of telescopes:\n"
        "Many people assume telescopes exist primarily to magnify images.\n"
        "Step 2: Light-gathering power:\n"
        "A telescope's primary function is light collection. Distant objects are faint because their photons spread out across billions of kilometers. A large aperture acts as a 'light bucket', gathering enough photons to make faint objects detectable."
    )
    return {
        "id": f"ns8_tel_05_{rng.randint(100000, 999999)}",
        "subskill": "05_telescope_primary_function_light_gathering_bucket",
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
            "tier_1": "What does a bucket collect?",
            "tier_2": "It collects photons of light.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["telescope_function_light_bucket_vs_magnification"]
    }


def arch_06_light_gathering_power_area_diameter_squared_rule(rng: random.Random) -> Dict[str, Any]:
    factor = rng.choice([2, 3, 4, 5])
    power_increase = factor ** 2
    prompt = (
        f"The light-gathering power (LGP) of a telescope depends directly on the surface area of its primary aperture (Area = π·(D/2)²).\n\n"
        f"If an astronomer doubles or increases the aperture diameter of a telescope by a factor of **{factor}**, by what factor does its light-gathering power increase?"
    )
    correct = f"It increases by a factor of {power_increase} (proportional to D²)."
    options = [
        correct,
        f"It increases by a factor of {factor} (proportional to D).",
        f"It increases by a factor of {factor * 2}.",
        f"It decreases to 1/{power_increase} of its original capacity."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Formula for circular aperture area:\n"
        "A = π × (D / 2)² ∝ D².\n"
        f"Step 2: Calculate for factor {factor}:\n"
        f"LGP_ratio = (D_new / D_old)² = ({factor})² = {power_increase}.\n"
        f"Increasing aperture by {factor}× increases light-collecting power by {power_increase}×."
    )
    return {
        "id": f"ns8_tel_06_{rng.randint(100000, 999999)}",
        "subskill": "06_light_gathering_power_area_diameter_squared_rule",
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
            "tier_1": "Light-gathering power is proportional to diameter SQUARED (D²).",
            "tier_2": f"Square the factor {factor}: {factor}² = {power_increase}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["light_gathering_power_diameter_squared_rule"]
    }


def arch_07_human_eye_vs_telescope_aperture_comparison_math(rng: random.Random) -> Dict[str, Any]:
    eye_d_mm = 5
    tel_d_mm = rng.choice([50, 100, 200])
    ratio = (tel_d_mm / eye_d_mm) ** 2
    prompt = (
        f"A human eye has a dark-adapted pupil diameter of {eye_d_mm} mm. A backyard amateur telescope has an aperture diameter of {tel_d_mm} mm.\n\n"
        f"Using the ratio of areas (D_tel / D_eye)², how many times more light does this telescope collect compared to the human eye?"
    )
    correct = f"{int(ratio):,} times more light."
    options = [
        correct,
        f"{int(tel_d_mm / eye_d_mm)} times more light.",
        f"{int(ratio * 2):,} times more light.",
        f"{int(tel_d_mm * eye_d_mm)} times more light."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Formula:\n"
        "Ratio = (D_telescope / D_eye)²\n"
        f"Step 2: Substitute values ({tel_d_mm} mm / {eye_d_mm} mm):\n"
        f"Ratio = ({tel_d_mm / eye_d_mm:.0f})² = {int(ratio):,}.\n"
        f"The telescope gathers {int(ratio):,} times more light than the human eye."
    )
    return {
        "id": f"ns8_tel_07_{rng.randint(100000, 999999)}",
        "subskill": "07_human_eye_vs_telescope_aperture_comparison_math",
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
            "tier_1": f"Divide {tel_d_mm} by {eye_d_mm}, then square the result.",
            "tier_2": f"({tel_d_mm / eye_d_mm:.0f})² = {int(ratio):,}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["aperture_area_ratio_calculation"]
    }


def arch_08_angular_resolution_and_rayleigh_criterion_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Beyond collecting light, telescopes provide **angular resolution**.\n\n"
        "What does the angular resolution of a telescope measure?"
    )
    correct = "The ability to distinguish two closely spaced celestial objects as separate, distinct points of light rather than a single blurred blob."
    options = [
        correct,
        "The speed at which the telescope motor rotates to follow the Moon.",
        "The total weight of the glass mirrors in kilograms.",
        "The amount of electrical power required to operate the computer cooling fans."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Angular resolution definition:\n"
        "Resolution refers to sharpness and fine detail.\n"
        "Step 2: Physical criterion (Rayleigh criterion θ ≈ 1,22 λ / D):\n"
        "A telescope with superior resolution can separate two tight binary stars or resolve fine details on planetary surfaces (like rings or craters) that appear as a single blurry smear to smaller apertures."
    )
    return {
        "id": f"ns8_tel_08_{rng.randint(100000, 999999)}",
        "subskill": "08_angular_resolution_and_rayleigh_criterion_concept",
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
            "tier_1": "What does resolving power allow an observer to separate?",
            "tier_2": "Two closely spaced points of light.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["angular_resolution_resolving_power"]
    }


def arch_09_magnification_vs_light_gathering_power_misconception(rng: random.Random) -> Dict[str, Any]:
    power = rng.choice(["1 000× magnification", "500× magnification", "extreme 800× magnification"])
    prompt = (
        f"A commercial toy telescope advertising '{power}' on its box is often disappointing to amateur stargazers.\n\n"
        "Why is excessive magnification useless on a small-aperture telescope?"
    )
    correct = "Because magnifying an image does not add any new light or detail; without a large aperture to collect photons and resolve detail, high magnification merely magnifies a dim, blurry, dark smear."
    options = [
        correct,
        "Because high magnification turns all stars into dangerous green laser beams.",
        "Because telescopes lose all their glass when magnified beyond 50 times.",
        "Because the law of physics prohibits any telescope from magnifying more than 10 times."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Magnification vs Aperture:\n"
        "Magnification (M = f_obj / f_eye) simply spreads the collected light over a larger area on the retina.\n"
        "Step 2: Empty magnification:\n"
        "If the objective aperture is small (e.g. 50 mm), it collects very few photons and has poor resolution. High magnification spreads this minimal light thinly, producing an unusable, dark, blurry image ('empty magnification')."
    )
    return {
        "id": f"ns8_tel_09_{rng.randint(100000, 999999)}",
        "subskill": "09_magnification_vs_light_gathering_power_misconception",
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
            "tier_1": "Does magnification add more light or new details?",
            "tier_2": "No, it just spreads existing light over a bigger area.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["magnification_vs_aperture_misconception"]
    }


def arch_10_refracting_telescope_optics_objective_and_eyepiece(rng: random.Random) -> Dict[str, Any]:
    lens_x = rng.choice([60, 70, 80])
    focal_x = 260
    svg = (
        f'<svg viewBox="0 0 500 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="500" height="220" fill="#0B132B"/>'
        f'<rect x="40" y="80" width="420" height="60" rx="4" fill="#1E293B" stroke="#475569" stroke-width="2"/>'
        f'<ellipse cx="{lens_x}" cy="110" rx="6" ry="26" fill="#38BDF8" opacity="0.8"/>'
        f'<text x="{lens_x}" y="70" fill="#38BDF8" font-size="11" text-anchor="middle">Objective Lens (Convex)</text>'
        f'<line x1="20" y1="95" x2="{lens_x}" y2="95" stroke="#FDE047" stroke-width="2"/>'
        f'<line x1="20" y1="125" x2="{lens_x}" y2="125" stroke="#FDE047" stroke-width="2"/>'
        f'<line x1="{lens_x}" y1="95" x2="{focal_x}" y2="110" stroke="#FDE047" stroke-width="1.5"/>'
        f'<line x1="{lens_x}" y1="125" x2="{focal_x}" y2="110" stroke="#FDE047" stroke-width="1.5"/>'
        f'<ellipse cx="440" cy="110" rx="4" ry="16" fill="#38BDF8" opacity="0.8"/>'
        f'<text x="440" y="70" fill="#38BDF8" font-size="11" text-anchor="middle">Eyepiece</text>'
        f'</svg>'
    )
    prompt = (
        "A **refracting telescope** uses glass optical components to form images.\n\n"
        "What are the two primary glass lenses in a refractor, and what is the optical function of each?"
    )
    correct = "A large convex objective lens at the front that gathers and bends (refracts) light to a focal point, and a small eyepiece lens at the back that magnifies the focused image."
    options = [
        correct,
        "A flat glass window that heats the air inside the tube, and a mirror that reflects the observer's face.",
        "Two concave mirrors that bounce radio signals across an internal antenna wire.",
        "A magnetic lens that deflects cosmic rays away from the observer's eyes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Refractor optical components:\n"
        "1. Objective Lens: large double-convex lens at the front; refracts incoming parallel light rays, bringing them to a focus.\n"
        "2. Eyepiece Lens: smaller magnifying lens positioned near the focal plane that presents an enlarged, virtual image to the human eye."
    )
    return {
        "id": f"ns8_tel_10_{rng.randint(100000, 999999)}",
        "subskill": "10_refracting_telescope_optics_objective_and_eyepiece",
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
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "What lens sits at the front, and what sits at the back?",
            "tier_2": "Objective lens in front to collect light; eyepiece in back to magnify.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["refracting_telescope_lens_functions"]
    }


def arch_11_hans_lippershey_and_galileo_telescope_history(rng: random.Random) -> Dict[str, Any]:
    year_p, year_g = 1608, 1609
    prompt = (
        f"In {year_p}, Dutch spectacle-maker Hans Lippershey applied for a patent for a 'looker' spyglass. In {year_g}, Italian scientist **Galileo Galilei** built his own improved version.\n\n"
        "Why is Galileo celebrated as a pioneer of astronomy even though he did not invent the first optical spyglass?"
    )
    correct = "Because Galileo was the first person to turn an optical telescope upward toward the night sky, systematically record scientific observations, and publish revolutionary astronomical discoveries."
    options = [
        correct,
        "Because Galileo personally walked to the Moon to install the first telescope mirror.",
        "Because Galileo proved that the Sun orbits around the Earth once every 24 hours.",
        "Because Galileo manufactured the glass lenses using molten lava from Mount Vesuvius."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Invention vs Astronomical Application:\n"
        "Lippershey and Dutch spectacle-makers created the optical spyglass for terrestrial and military use (spotting enemy ships at sea).\n"
        "Step 2: Galileo's contribution:\n"
        "In 1609, Galileo realized the device's astronomical potential, grinding his own precision lenses and publishing his observations in 'Sidereus Nuncius' (The Starry Messenger) in 1610."
    )
    return {
        "id": f"ns8_tel_11_{rng.randint(100000, 999999)}",
        "subskill": "11_hans_lippershey_and_galileo_telescope_history",
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
            "tier_1": "What did Galileo do with the telescope that changed history?",
            "tier_2": "He pointed it at the night sky and systematically recorded celestial discoveries.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["galileo_telescope_astronomy_pioneer"]
    }


def arch_12_galileo_astronomical_discoveries_jupiter_moons(rng: random.Random) -> Dict[str, Any]:
    disc = rng.choice([
        ("the four largest moons of Jupiter (Io, Europa, Ganymede, Callisto)", "proved that not all celestial bodies orbit the Earth, dealing a devastating blow to the geocentric model"),
        ("the phases of Venus (crescent to gibbous)", "proved conclusively that Venus must orbit the Sun rather than the Earth"),
        ("craters and rugged mountains on Earth's Moon", "proved that celestial bodies are imperfect, rocky worlds like Earth rather than flawless divine spheres"),
        ("dark sunspots moving across the Sun's surface", "proved that the Sun rotates on its own axis and is dynamic rather than pristine and immutable")
    ])
    feat, significance = disc
    prompt = (
        f"In 1610, Galileo made revolutionary telescopic observations, discovering **{feat}**.\n\n"
        f"What was the profound cosmological significance of this specific discovery?"
    )
    correct = f"It {significance}."
    options = [
        correct,
        "It proved that the Earth is completely flat and balanced on the back of a giant turtle.",
        "It proved that all planets are hollow containers made of pure glass.",
        "It proved that the stars are small lightbulbs suspended from a solid wooden dome."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Galileo's observation:\n"
        f"Galileo discovered {feat}.\n"
        "Step 2: Cosmological impact:\n"
        f"This finding {significance}, providing direct empirical evidence that supported Nicolaus Copernicus's heliocentric model."
    )
    return {
        "id": f"ns8_tel_12_{rng.randint(100000, 999999)}",
        "subskill": "12_galileo_astronomical_discoveries_jupiter_moons",
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
            "tier_1": f"How did discovering {feat[:25]} challenge old ideas?",
            "tier_2": f"It {significance[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["galileo_telescopic_discoveries_heliocentrism"]
    }


def arch_13_chromatic_aberration_lens_dispersion_defect(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Early refracting telescopes suffered severely from an optical defect known as **chromatic aberration**.\n\n"
        "What causes chromatic aberration in glass lenses, and how does it affect astronomical observations?"
    )
    correct = "Glass refracts different wavelengths (colors) of light by different amounts (dispersion), causing different colors to focus at different points and creating blurry, rainbow-colored halos around bright objects."
    options = [
        correct,
        "Telescope mirrors get covered in condensation, turning all stars completely green.",
        "The observer's eyeball changes color when exposed to cold nighttime air.",
        "Glass lenses absorb all visible photons and emit dangerous radioactive microwaves."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Optical dispersion:\n"
        "When white light passes through a glass lens, blue light refracts more strongly than red light (refractive index n varies with wavelength λ).\n"
        "Step 2: Chromatic aberration effect:\n"
        "Blue light comes to a focus closer to the lens than red light. The result is an image surrounded by distracting colored halos (fringes) that cannot be brought into crisp focus simultaneously."
    )
    return {
        "id": f"ns8_tel_13_{rng.randint(100000, 999999)}",
        "subskill": "13_chromatic_aberration_lens_dispersion_defect",
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
            "tier_1": "What happens when white light bends through glass (like a prism)?",
            "tier_2": "Different colors focus at different distances, causing rainbow halos.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["chromatic_aberration_dispersion_lens_defect"]
    }


def arch_14_physical_limits_of_giant_refracting_telescopes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The world's largest operational refracting telescope is the 40-inch (1,02 meter) refractor at Yerkes Observatory, built in 1897. No larger refractor has ever been constructed.\n\n"
        "What engineering and physical limitations prevent astronomers from building larger glass refracting lenses?"
    )
    correct = "Lenses can only be supported along their outer rims, causing heavy glass to sag under its own gravity; furthermore, thick glass absorbs light and cannot be cast without internal bubbles."
    options = [
        correct,
        "There is no more silica sand left on Earth to manufacture any additional glass lenses.",
        "Glass lenses dissolve into water vapor whenever they are pointed toward the stars.",
        "International space treaties ban any telescope larger than one meter in diameter."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mechanical support limits:\n"
        "Because light must pass entirely through a lens, it can only be held at the edges. A lens larger than 1 meter weighs tons and sags under its own weight, distorting the optical figure.\n"
        "Step 2: Optical limits:\n"
        "Casting massive thick glass blocks without internal bubbles or thermal strains is extraordinarily difficult, and thick glass absorbs significant amounts of starlight."
    )
    return {
        "id": f"ns8_tel_14_{rng.randint(100000, 999999)}",
        "subskill": "14_physical_limits_of_giant_refracting_telescopes",
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
            "tier_1": "Can a lens be supported from behind like a mirror?",
            "tier_2": "No, light must pass through, so edge-support makes heavy glass sag.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["refractor_physical_size_engineering_limits"]
    }


def arch_15_reflecting_telescope_optics_concave_primary_mirror(rng: random.Random) -> Dict[str, Any]:
    mirror_x = rng.choice([40, 50, 60])
    focal_x = 240
    svg = (
        f'<svg viewBox="0 0 500 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="500" height="220" fill="#0B132B"/>'
        f'<rect x="30" y="70" width="440" height="80" rx="4" fill="#1E293B" stroke="#475569" stroke-width="2"/>'
        f'<path d="M {mirror_x} 75 Q {mirror_x + 15} 110 {mirror_x} 145" fill="none" stroke="#38BDF8" stroke-width="5"/>'
        f'<text x="{mirror_x}" y="60" fill="#38BDF8" font-size="11" text-anchor="middle">Concave Primary Mirror</text>'
        f'<line x1="460" y1="85" x2="{mirror_x + 10}" y2="85" stroke="#FDE047" stroke-width="2"/>'
        f'<line x1="460" y1="135" x2="{mirror_x + 10}" y2="135" stroke="#FDE047" stroke-width="2"/>'
        f'<line x1="{mirror_x + 10}" y1="85" x2="{focal_x}" y2="110" stroke="#FDE047" stroke-width="1.5"/>'
        f'<line x1="{mirror_x + 10}" y1="135" x2="{focal_x}" y2="110" stroke="#FDE047" stroke-width="1.5"/>'
        f'<rect x="{focal_x}" y="100" width="16" height="20" fill="#F59E0B" transform="rotate(45 {focal_x} 110)"/>'
        f'<text x="{focal_x}" y="150" fill="#F59E0B" font-size="11" text-anchor="middle">Flat Secondary Mirror</text>'
        f'</svg>'
    )
    prompt = (
        "A **reflecting telescope** replaces glass objective lenses with curved optical mirrors.\n\n"
        "What type of primary mirror is situated at the base of the telescope tube, and how does it manipulate incoming starlight?"
    )
    correct = "A curved concave mirror (parabolic or spherical) that reflects incoming parallel starlight forward to a common focal point."
    options = [
        correct,
        "A flat bathroom mirror that reflects light straight back out of the tube without focusing it.",
        "A convex rear-view car mirror that spreads light rays apart in all directions.",
        "A transparent plastic sheet that polarizes cosmic microwave radiation."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Primary mirror geometry:\n"
        "The primary mirror at the bottom of the tube is concave (curved inward like a bowl).\n"
        "Step 2: Reflection and convergence:\n"
        "By the law of reflection (angle of incidence = angle of reflection), parallel rays striking the curved concave surface reflect inward, converging at a focal point."
    )
    return {
        "id": f"ns8_tel_15_{rng.randint(100000, 999999)}",
        "subskill": "15_reflecting_telescope_optics_concave_primary_mirror",
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
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "What shape of mirror focuses incoming light rays?",
            "tier_2": "A concave mirror.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["reflecting_telescope_concave_primary_mirror"]
    }


def arch_16_isaac_newton_invention_of_reflecting_telescope(rng: random.Random) -> Dict[str, Any]:
    year = 1668
    prompt = (
        f"In {year}, English physicist **Sir Isaac Newton** designed and built the first operational reflecting telescope (the Newtonian reflector).\n\n"
        "What specific optical flaw in refracting telescopes was Newton trying to overcome by inventing the reflector?"
    )
    correct = "Chromatic aberration; because reflection obeys the law of reflection identically for all wavelengths, mirrors reflect all colors equally without color dispersion."
    options = [
        correct,
        "Sound reverberation caused by supersonic planes flying over London.",
        "The gravitational pull of Jupiter disrupting the telescope's wooden tripod.",
        "Telescopes catching fire when observing the Moon at night."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Newton's experiments on light:\n"
        "Newton demonstrated with prisms that white light is a mixture of colors, each with a different index of refraction in glass.\n"
        "Step 2: Solution via mirrors:\n"
        "Newton realized that reflection is entirely independent of wavelength—red light and blue light bounce off polished metal mirrors at the exact same angle. Thus, reflecting telescopes completely eliminate chromatic aberration."
    )
    return {
        "id": f"ns8_tel_16_{rng.randint(100000, 999999)}",
        "subskill": "16_isaac_newton_invention_of_reflecting_telescope",
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
            "tier_1": "What color-fringing defect in lenses did Newton eliminate with mirrors?",
            "tier_2": "Chromatic aberration.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["newton_invention_reflector_chromatic_aberration"]
    }


def arch_17_advantages_of_reflectors_over_refracting_telescopes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Today, all major research observatories worldwide (such as SALT, Keck, and the VLT) use reflecting telescopes rather than refractors.\n\n"
        "What major structural advantage allows reflecting mirrors to be built to gargantuan sizes (10+ meters) that lenses cannot achieve?"
    )
    correct = "Mirrors can be supported across their entire back surface to prevent sagging, and only the front reflective surface requires precision optical shaping."
    options = [
        correct,
        "Mirrors weigh 99% less than air and float naturally in the atmosphere.",
        "Mirrors generate their own electricity to power the observatory lights.",
        "Mirrors can be folded up like paper and put into an astronomer's pocket."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Support across rear face:\n"
        "Because starlight reflects off the front aluminized surface, the entire back and sides of a mirror can rest on rigid mechanical supports or motorized actuators (active optics).\n"
        "Step 2: Manufacturing advantage:\n"
        "Only one surface requires optical polishing, and minor imperfections inside the glass substrate are irrelevant because light never passes through the interior."
    )
    return {
        "id": f"ns8_tel_17_{rng.randint(100000, 999999)}",
        "subskill": "17_advantages_of_reflectors_over_refracting_telescopes",
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
            "tier_1": "How are giant mirrors supported from behind?",
            "tier_2": "They can be supported across their entire rear surface to prevent sagging.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["reflector_structural_advantages_over_refractor"]
    }


def arch_18_newtonian_vs_cassegrain_optical_pathways(rng: random.Random) -> Dict[str, Any]:
    desig = rng.choice(["Newtonian reflector", "Cassegrain reflector"])
    if desig == "Newtonian reflector":
        desc = "uses a flat secondary mirror angled at 45° to bounce light out through a hole in the side of the tube near the top"
    else:
        desc = "uses a convex secondary mirror that bounces light straight back through a hole in the center of the primary mirror to an eyepiece at the rear"
    prompt = (
        f"In optical astronomy, reflecting telescopes use different configurations to direct light to the observer. In a **{desig}**, what optical pathway is used?"
    )
    correct = f"It {desc}."
    options = [
        correct,
        "It bounces light through an underground water tunnel directly into the observer's basement.",
        "It uses an optical fiber wrapped around the exterior of the tube thirty times.",
        "It reflects light straight into the ground so it can be absorbed by tree roots."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify configuration:\n"
        f"A {desig} {desc}.\n"
        "Step 2: Practical use:\n"
        "Newtonians are popular for amateur stargazing, while Cassegrain designs provide long focal lengths in compact tubes preferred by large professional observatories."
    )
    return {
        "id": f"ns8_tel_18_{rng.randint(100000, 999999)}",
        "subskill": "18_newtonian_vs_cassegrain_optical_pathways",
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
            "tier_1": f"Where does the secondary mirror direct light in a {desig}?",
            "tier_2": f"It {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["newtonian_vs_cassegrain_optical_design"]
    }


def arch_19_salt_location_sutherland_altitude_and_climate(rng: random.Random) -> Dict[str, Any]:
    altitude = rng.choice(["1 798 meters above sea level", "nearly 1 800 m in altitude"])
    prompt = (
        f"The Southern African Large Telescope (SALT) is perched on a high plateau near Sutherland in the Karoo at {altitude}.\n\n"
        "Why is high elevation combined with a semi-arid climate critical for optical astronomy?"
    )
    correct = "Being above much of the dense, turbulent lower atmosphere reduces atmospheric blurring ('seeing'), while low humidity ensures minimal cloud cover and maximum clear nights."
    options = [
        correct,
        "High elevation brings the telescope physically 50% closer to the distant stars.",
        "The cold temperature turns the telescope glass into superconductive metal.",
        "Being close to sea level ensures thick fog coats the mirror lenses."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: High altitude benefit:\n"
        "At ~1 800 m, the telescope operates above the densest, most humid layers of the troposphere, minimizing light scattering and atmospheric extinction.\n"
        "Step 2: Semi-arid climate benefit:\n"
        "The Karoo provides dry, stable air with over 70% cloudless nights per year, allowing continuous long-exposure astronomical data collection."
    )
    return {
        "id": f"ns8_tel_19_{rng.randint(100000, 999999)}",
        "subskill": "19_salt_location_sutherland_altitude_and_climate",
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
            "tier_1": "What happens to the air at high altitudes in a dry climate?",
            "tier_2": "The air is thinner, clearer, and free from clouds and humidity.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["high_altitude_astronomy_site_benefits"]
    }


def arch_20_salt_hexagonal_primary_mirror_11_meter_array(rng: random.Random) -> Dict[str, Any]:
    num_seg = 91
    diam_m = 11
    prompt = (
        f"Rather than attempting to cast a single fragile 11-meter glass disc, SALT's primary mirror consists of **{num_seg} individual hexagonal mirror segments** tessellated together.\n\n"
        f"What is the effective aperture dimension of this composite mirror, and how are the segments kept in alignment?"
    )
    correct = f"It forms an 11-meter by 9,8-meter hexagonal array; computer-controlled actuators continuously adjust each of the {num_seg} segments to act as a single seamless optical surface."
    options = [
        correct,
        "It forms a 1-meter square mirror; the mirrors are glued permanently with chewing gum.",
        "It forms a circular telescope that floats on oil without any mechanical mounts.",
        "It forms a solid iron sheet that bends whenever an astronomer looks through it."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Segmented mirror architecture:\n"
        f"SALT uses {num_seg} identical 1-meter hexagonal glass-ceramic mirrors arranged in a honeycomb lattice.\n"
        "Step 2: Active optics alignment:\n"
        "Laser alignment and computer-driven capacitive edge sensors adjust piezoelectric actuators beneath each segment several times per second, maintaining sub-micron optical alignment."
    )
    return {
        "id": f"ns8_tel_20_{rng.randint(100000, 999999)}",
        "subskill": "20_salt_hexagonal_primary_mirror_11_meter_array",
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
            "tier_1": "How many hexagonal mirror segments make up SALT's primary mirror?",
            "tier_2": "91 segments acting together as an 11-meter array.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["salt_segmented_mirror_active_optics"]
    }


def arch_21_salt_fixed_altitude_tilt_and_tracker_motion(rng: random.Random) -> Dict[str, Any]:
    tilt = rng.choice(["fixed at 37° from the vertical (zenith)", "fixed at an elevation angle of 53° (37° from zenith)"])
    prompt = (
        f"Unlike conventional telescopes that tilt up and down across all angles, SALT's massive 11-meter primary mirror structure is mounted at a **fixed angle** ({tilt}).\n\n"
        "How does SALT track moving celestial bodies across the sky as the Earth rotates?"
    )
    correct = "The entire building rotates in azimuth (compass direction) to face the target, while a motorized instrument payload tracker moves across the prime focus above the stationary mirror."
    options = [
        correct,
        "The telescope uses giant rocket thrusters to spin the entire mountain in reverse.",
        "Astronomers wait for the Earth to stop spinning before taking a photograph.",
        "The telescope mirror flexes into a concave shape using hydraulic oil pumps."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Cost-effective design (Hobby-Eberly design):\n"
        "Fixing the elevation angle at 37° saved immense structural steel costs.\n"
        "Step 2: Tracking mechanism:\n"
        "SALT rotates horizontally on air bearings (azimuth). Once positioned, the main mirror stays locked, and a robotic tracker payload suspended 13 meters above moves across the focal plane for up to 2 hours tracking the moving star."
    )
    return {
        "id": f"ns8_tel_21_{rng.randint(100000, 999999)}",
        "subskill": "21_salt_fixed_altitude_tilt_and_tracker_motion",
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
            "tier_1": "How does SALT track stars if the main mirror doesn't tilt up and down?",
            "tier_2": "A robotic tracker payload moves across the focal plane above the mirror.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["salt_fixed_altitude_tracker_tracking"]
    }


def arch_22_spectroscopy_starlight_fingerprint_chemical_composition(rng: random.Random) -> Dict[str, Any]:
    element, lines = rng.choice([
        ("Hydrogen", "distinct dark absorption lines at specific wavelengths (Balmer series)"),
        ("Helium", "characteristic spectral lines first discovered in sunlight before being found on Earth"),
        ("Sodium", "a prominent pair of dark absorption lines in the yellow spectrum (Fraunhofer D lines)")
    ])
    prompt = (
        f"Astronomers at observatories like SALT rarely simply 'look' through an eyepiece; instead, they attach a **spectrograph** to disperse starlight into a spectrum.\n\n"
        f"How does analyzing the spectral absorption lines of starlight reveal that a distant star contains **{element}**?"
    )
    correct = f"Every chemical element absorbs and emits specific unique wavelengths of light; identifying {element}'s exact spectral fingerprint confirms its presence and abundance."
    options = [
        correct,
        "By burning physical soil samples retrieved from the star with Bunsen burners.",
        "By smelling the starlight through a special atmospheric chimney.",
        "By measuring the physical temperature of the telescope's steel tripod."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Quantum origin of spectral lines:\n"
        "Electrons in atoms only absorb and emit photons corresponding to transitions between discrete energy levels (E = hf).\n"
        "Step 2: Chemical fingerprints:\n"
        "Because each element possesses a unique electron energy configuration, its spectral lines act as an infallible chemical barcode or fingerprint across interstellar space."
    )
    return {
        "id": f"ns8_tel_22_{rng.randint(100000, 999999)}",
        "subskill": "22_spectroscopy_starlight_fingerprint_chemical_composition",
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
            "tier_1": "What acts like a chemical fingerprint in starlight?",
            "tier_2": "Unique spectral lines absorbed or emitted by each element.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["astronomical_spectroscopy_chemical_fingerprint"]
    }


def arch_23_optical_astronomy_limitations_daylight_and_clouds(rng: random.Random) -> Dict[str, Any]:
    factor = rng.choice(["daytime sunlight", "overcast cloud cover and rainfall", "atmospheric moisture"])
    prompt = (
        f"Ground-based optical telescopes face severe operational constraints, such as {factor}.\n\n"
        "Why does optical astronomy cease completely when daytime sunlight fills the sky?"
    )
    correct = "Sunlight scatters through the atmospheric nitrogen and oxygen molecules (Rayleigh scattering), creating a brilliant blue background sky that overwhelms the faint starlight."
    options = [
        correct,
        "All the stars in the universe turn off their fusion engines every morning.",
        "The Sun absorbs all other stars into its outer atmosphere during the day.",
        "Telescope mirrors melt instantly if exposed to daylight."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Atmospheric light scattering:\n"
        "During the day, intense sunlight undergoes Rayleigh scattering in Earth's atmosphere.\n"
        "Step 2: Signal-to-noise ratio:\n"
        "The brightness of the scattered daytime sky exceeds the light flux of distant stars by many orders of magnitude, drowning out celestial signals. Optical telescopes must operate at night."
    )
    return {
        "id": f"ns8_tel_23_{rng.randint(100000, 999999)}",
        "subskill": "23_optical_astronomy_limitations_daylight_and_clouds",
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
            "tier_1": "What does Rayleigh scattering do to the daytime sky?",
            "tier_2": "It illuminates the air, washing out faint starlight.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["optical_astronomy_daylight_limitations"]
    }


def arch_24_urban_light_pollution_astronomy_impact(rng: random.Random) -> Dict[str, Any]:
    city = rng.choice(["Johannesburg", "Cape Town", "Durban", "Pretoria"])
    prompt = (
        f"In major metropolitan areas such as {city}, residents looking up at night can see only a few dozen bright stars, whereas rural Karoo stargazers see thousands.\n\n"
        "What is this environmental issue called, and what causes it?"
    )
    correct = "Light pollution; caused by excessive, unshielded artificial lighting (streetlights, billboards, buildings) scattering upward into the atmosphere and washing out the night sky."
    options = [
        correct,
        "Cosmic darkening; caused by stars fleeing away from big cities.",
        "Atmospheric depletion; caused by human breathing consuming all nighttime photons.",
        "Electromagnetic silencing; caused by cell phone towers absorbing starlight."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Define light pollution:\n"
        "The inappropriate or excessive use of artificial light.\n"
        "Step 2: Atmospheric skyglow:\n"
        "Upward-directed light from streetlights and commercial facilities scatters off atmospheric aerosols and dust (skyglow), dramatically brightening the background sky and rendering faint astronomical objects invisible."
    )
    return {
        "id": f"ns8_tel_24_{rng.randint(100000, 999999)}",
        "subskill": "24_urban_light_pollution_astronomy_impact",
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
            "tier_1": "What do bright city lights create in the night sky?",
            "tier_2": "Light pollution / skyglow.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["light_pollution_astronomy_impact"]
    }


def arch_25_astronomy_geographic_advantage_act_radio_quiet_karoo(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The Parliament of South Africa passed the **Astronomy Geographic Advantage Act (AGAA)** to establish statutory protection for astronomical sites in the Karoo.\n\n"
        "What specific protective regulations does this law enforce around Sutherland and Carnarvon?"
    )
    correct = "It restricts artificial light pollution near Sutherland and bans radio frequency interference (cell towers, radio broadcasts, high-voltage lines) near the MeerKAT and SKA radio arrays."
    options = [
        correct,
        "It prohibits any tourists or scientists from ever visiting the Northern Cape province.",
        "It requires all residents in South Africa to turn off their lights at 18:00 every evening.",
        "It bans all research into astronomy across all South African universities."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Purpose of the AGAA:\n"
        "To preserve the pristine, world-unique astronomical environment of the Northern Cape.\n"
        "Step 2: Protected domains:\n"
        "1. Optical: Dark skies protection around Sutherland (regulating outdoor lighting).\n"
        "2. Radio: Establishing the Karoo Radio Astronomy Reserve around Carnarvon, maintaining a radio-quiet zone free of cellular, radar, and RF transmissions that would blind sensitive radio telescope receivers."
    )
    return {
        "id": f"ns8_tel_25_{rng.randint(100000, 999999)}",
        "subskill": "25_astronomy_geographic_advantage_act_radio_quiet_karoo",
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
            "tier_1": "What does the AGAA protect against in the Karoo?",
            "tier_2": "Light pollution (Sutherland) and radio frequency interference (Carnarvon).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["agaa_astronomy_reserve_protections"]
    }


BUILDERS_01_25 = {
    "01_naked_eye_astronomy_pupil_aperture_limitations": arch_01_naked_eye_astronomy_pupil_aperture_limitations,
    "02_indigenous_starlore_pleiades_isilimela_planting": arch_02_indigenous_starlore_pleiades_isilimela_planting,
    "03_indigenous_starlore_sirius_inkosazana_harvest": arch_03_indigenous_starlore_sirius_inkosazana_harvest,
    "04_constellations_definition_and_celestial_mapping": arch_04_constellations_definition_and_celestial_mapping,
    "05_telescope_primary_function_light_gathering_bucket": arch_05_telescope_primary_function_light_gathering_bucket,
    "06_light_gathering_power_area_diameter_squared_rule": arch_06_light_gathering_power_area_diameter_squared_rule,
    "07_human_eye_vs_telescope_aperture_comparison_math": arch_07_human_eye_vs_telescope_aperture_comparison_math,
    "08_angular_resolution_and_rayleigh_criterion_concept": arch_08_angular_resolution_and_rayleigh_criterion_concept,
    "09_magnification_vs_light_gathering_power_misconception": arch_09_magnification_vs_light_gathering_power_misconception,
    "10_refracting_telescope_optics_objective_and_eyepiece": arch_10_refracting_telescope_optics_objective_and_eyepiece,
    "11_hans_lippershey_and_galileo_telescope_history": arch_11_hans_lippershey_and_galileo_telescope_history,
    "12_galileo_astronomical_discoveries_jupiter_moons": arch_12_galileo_astronomical_discoveries_jupiter_moons,
    "13_chromatic_aberration_lens_dispersion_defect": arch_13_chromatic_aberration_lens_dispersion_defect,
    "14_physical_limits_of_giant_refracting_telescopes": arch_14_physical_limits_of_giant_refracting_telescopes,
    "15_reflecting_telescope_optics_concave_primary_mirror": arch_15_reflecting_telescope_optics_concave_primary_mirror,
    "16_isaac_newton_invention_of_reflecting_telescope": arch_16_isaac_newton_invention_of_reflecting_telescope,
    "17_advantages_of_reflectors_over_refracting_telescopes": arch_17_advantages_of_reflectors_over_refracting_telescopes,
    "18_newtonian_vs_cassegrain_optical_pathways": arch_18_newtonian_vs_cassegrain_optical_pathways,
    "19_salt_location_sutherland_altitude_and_climate": arch_19_salt_location_sutherland_altitude_and_climate,
    "20_salt_hexagonal_primary_mirror_11_meter_array": arch_20_salt_hexagonal_primary_mirror_11_meter_array,
    "21_salt_fixed_altitude_tilt_and_tracker_motion": arch_21_salt_fixed_altitude_tilt_and_tracker_motion,
    "22_spectroscopy_starlight_fingerprint_chemical_composition": arch_22_spectroscopy_starlight_fingerprint_chemical_composition,
    "23_optical_astronomy_limitations_daylight_and_clouds": arch_23_optical_astronomy_limitations_daylight_and_clouds,
    "24_urban_light_pollution_astronomy_impact": arch_24_urban_light_pollution_astronomy_impact,
    "25_astronomy_geographic_advantage_act_radio_quiet_karoo": arch_25_astronomy_geographic_advantage_act_radio_quiet_karoo,
}
