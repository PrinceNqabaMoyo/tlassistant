"""Natural Sciences Grade 8 Term 4: Looking into Space Generator.

Strictly grounded in curriculum_docs_auto/NaturalSciences_Gr8/Syllabus.md.
Covers:
- optical_telescopes_refraction_reflection: Refracting (lenses) vs reflecting (mirrors) optical telescopes.
- radio_telescopes_and_ska: Radio waves, large metal dishes, Square Kilometre Array (SKA) in the Karoo.
- south_african_large_telescope_salt: SALT at Sutherland; atmospheric requirements (darkness, zero light pollution).
- space_telescopes_vs_ground_telescopes: Hubble Space Telescope advantages over ground-based observatories.
- constellations_and_indigenous_skylore: Southern Cross (Crux) celestial navigation, Orion, Isilimela (Pleiades) planting calendar.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


SUBSKILLS = [
    "optical_telescopes_refraction_reflection",
    "radio_telescopes_and_ska",
    "south_african_large_telescope_salt",
    "space_telescopes_vs_ground_telescopes",
    "constellations_and_indigenous_skylore",
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _build_optical_telescopes(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    ap = rng.choice([150, 200, 250, 300])
    prompt = (
        f"Optical telescopes with apertures such as {ap} mm collect and focus visible light to produce magnified images of distant celestial objects.\n\n"
        "1. Distinguish between a **refracting telescope** and a **reflecting telescope** by stating the primary optical component used by each to gather and focus light.\n"
        "2. Explain why all modern ultra-large research telescopes (such as SALT) are constructed using curved mirrors rather than heavy glass lenses.\n"
        "3. Name the two primary functions of any astronomical telescope (Hint: light gathering and magnification)."
    )
    sample_answer = (
        "1. A refracting telescope uses curved glass lenses to refract (bend) light. A reflecting telescope uses curved (concave) mirrors to reflect and focus light.\n"
        "2. Huge glass lenses sag under their own weight, absorb light, and suffer from chromatic aberration (color blurring). Mirrors can be supported from behind across their entire back surface and produce clear, distortion-free images.\n"
        "3. Two functions: To gather a large amount of faint light from distant objects (light-gathering power), and to magnify the angular size of distant objects (magnification)."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Refractor vs Reflector: Refractor uses lenses; reflector uses mirrors [1 mark].\n"
        "2. Why large telescopes use mirrors: Lenses sag under heavy weight, crack, or suffer from chromatic aberration; mirrors can be supported easily from underneath [2 marks].\n"
        "3. Telescope functions: Light gathering and magnification [1 mark]."
    )
    return {
        "id": _make_id("ns8_opt_tele", seed, idx),
        "question_type": "paragraph",
        "diagram_spec": {
            "image_type": "optical_telescopes",
            "master": "optical_telescopes",
            "diagram_id": "optical_telescopes",
            "view": "textbook",
            "diagram_role": "context",
            "allowViewSwitch": False,
            "pins": [],
        },
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "optical_telescopes_refraction_reflection",
        "question_family_id": "optical_telescopes_refraction_reflection",
        "curriculum_reference": "Natural Sciences Gr8 Term 4 > Looking into Space > Optical telescopes",
        "hints": {
            "tier_1": "Refract = bend through glass lens; Reflect = bounce off curved mirror.",
            "tier_2": "Giant lenses are too heavy and bend out of shape.",
            "tier_3": "Refractor uses lenses; reflector uses mirrors; mirrors can be supported from behind."
        },
        "misconception_tags": ["all_telescopes_use_glass_lenses_misconception"]
    }


def _build_radio_ska(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    array_detail = rng.choice(["thousands of mid-frequency dishes", "hundreds of linked parabolic antennas", "a vast aperture synthesis network"])
    prompt = (
        f"South Africa is co-hosting the **Square Kilometre Array (SKA)** comprising {array_detail}, "
        "located in the Karoo region near Carnarvon in the Northern Cape.\n\n"
        "1. What form of electromagnetic radiation does the SKA detect (visible light or radio waves)?\n"
        "2. State two significant advantages radio telescopes have over optical telescopes when studying deep space.\n"
        "3. Why was the remote Karoo semi-desert selected as the ideal scientific location for the SKA core site?"
    )
    sample_answer = (
        "1. Radio waves (invisible radio frequency radiation).\n"
        "2. Two advantages:\n"
        "- Radio waves pass directly through dense cosmic dust and gas clouds that completely block visible light.\n"
        "- Radio telescopes can operate 24 hours a day during daylight and through cloudy weather without being blinded by sunlight.\n"
        "3. The Karoo is an officially declared Radio Astronomy Reserve with minimal human population, meaning there is near-zero radio frequency interference from mobile phones, television broadcasts, power lines, and aircraft."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Radiation type: Radio waves [1 mark].\n"
        "2. Two advantages: Penetrates interstellar dust/clouds, and can observe during daytime and cloudy conditions [2 marks].\n"
        "3. Karoo site selection: Radio quietness / free from human electromagnetic interference (cellphones, TV, radio broadcasts) [1 mark]."
    )
    return {
        "id": _make_id("ns8_radio_ska", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "radio_telescopes_and_ska",
        "question_family_id": "radio_telescopes_and_ska",
        "curriculum_reference": "Natural Sciences Gr8 Term 4 > Looking into Space > Radio telescopes and the SKA",
        "hints": {
            "tier_1": "The SKA detects invisible radio signals from deep space.",
            "tier_2": "Radio waves can pass through dust and work day and night.",
            "tier_3": "The Karoo is isolated with no cellphone or radio interference."
        },
        "misconception_tags": ["radio_telescopes_detect_sound_misconception"]
    }


def _build_salt_observatory(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    elev = rng.choice(["at an altitude of 1 798 metres", "situated on a remote plateau 1 800 metres", "at high elevation in the Roggeveld Mountains"])
    prompt = (
        f"The **Southern African Large Telescope (SALT)** located near Sutherland in the Northern Cape {elev} is the largest single optical telescope in the Southern Hemisphere.\n\n"
        "1. What type of primary mirror does SALT possess (a single giant circular glass lens, or a hexagonal segmented mirror array)?\n"
        "2. State three specific geographic and atmospheric conditions present at Sutherland that make it one of the premier astronomical observation sites in the world."
    )
    sample_answer = (
        "1. A hexagonal segmented mirror array (consisting of 91 interlocking hexagonal mirror segments forming a giant 11-meter primary mirror).\n"
        "2. Three ideal conditions at Sutherland:\n"
        "- High altitude (approx. 1800 m above sea level) with a thin, clear atmosphere.\n"
        "- Cloudless skies with very low annual rainfall and extremely low humidity.\n"
        "- Zero urban light pollution and minimal air pollution due to vast distances from major industrial cities."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Mirror type: Hexagonal segmented mirror array (91 hexagonal mirrors) [1 mark].\n"
        "2. Condition 1: High altitude / dry thin air [1 mark].\n"
        "3. Condition 2: Cloudless, clear night skies with low rainfall [1 mark].\n"
        "4. Condition 3: Absence of urban light pollution / remote rural darkness [1 mark]."
    )
    return {
        "id": _make_id("ns8_salt_obs", seed, idx),
        "question_type": "paragraph",
        "diagram_spec": {
            "image_type": "optical_telescopes",
            "master": "optical_telescopes",
            "diagram_id": "optical_telescopes",
            "view": "textbook",
            "diagram_role": "context",
            "allowViewSwitch": False,
            "pins": [],
        },
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "total_marks": 4,
        "subskill": "south_african_large_telescope_salt",
        "question_family_id": "south_african_large_telescope_salt",
        "curriculum_reference": "Natural Sciences Gr8 Term 4 > Looking into Space > The Southern African Large Telescope",
        "hints": {
            "tier_1": "SALT is located in Sutherland in the Karoo.",
            "tier_2": "Telescopes need dark skies, high altitudes, and clear dry weather.",
            "tier_3": "Segmented hexagonal mirrors; clear, dry, cloudless skies without city lights."
        },
        "misconception_tags": ["salt_built_in_cape_town_misconception"]
    }


def _build_space_telescopes(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    tel_ex = rng.choice(["the Hubble Space Telescope (HST) and James Webb Space Telescope (JWST)", "space observatories such as the Hubble Space Telescope in low Earth orbit", "orbiting infrared observatories such as the James Webb Space Telescope at Lagrange Point 2"])
    prompt = (
        f"Despite the construction of massive ground-based observatories like SALT, space agencies place astronomical telescopes "
        f"(such as {tel_ex}) in orbit around Earth or in outer space.\n\n"
        "1. Explain the primary optical disadvantage that ground-based telescopes suffer from that space telescopes completely avoid (atmospheric distortion/turbulence).\n"
        "2. Name one form of electromagnetic radiation (e.g. gamma rays, X-rays, or certain ultraviolet/infrared bands) that cannot be studied from Earth's surface because Earth's atmosphere absorbs it.\n"
        "3. State one major technical disadvantage of operating a telescope in outer space compared to on the ground."
    )
    sample_answer = (
        "1. Atmospheric distortion and turbulence ('twinkling'): Earth's shifting thermal air currents blur and distort incoming starlight, reducing optical resolution. Space telescopes sit outside the atmosphere and capture crystal-clear images.\n"
        "2. Gamma rays, X-rays, or most ultraviolet and far-infrared radiation are absorbed and blocked by the ozone layer and atmospheric gases.\n"
        "3. Extremely expensive to launch, impossible or exceedingly difficult to repair or upgrade physically when hardware fails."
    )
    sol = (
        "Marking Rubric (3 marks total):\n"
        "1. Atmospheric distortion: Air turbulence blurs starlight; space has zero atmosphere and no twinkle blurring [1 mark].\n"
        "2. Blocked radiation: X-rays / Gamma rays / UV / infrared absorbed by Earth's atmosphere [1 mark].\n"
        "3. Space disadvantage: Immense launch cost and inability to repair easily [1 mark]."
    )
    return {
        "id": _make_id("ns8_space_tele", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "total_marks": 3,
        "subskill": "space_telescopes_vs_ground_telescopes",
        "question_family_id": "space_telescopes_vs_ground_telescopes",
        "curriculum_reference": "Natural Sciences Gr8 Term 4 > Looking into Space > Space telescopes",
        "hints": {
            "tier_1": "Stars twinkle because Earth's moving air blurs the light.",
            "tier_2": "In space there is no air, so images are perfectly sharp.",
            "tier_3": "Earth blocks X-rays/UV; space telescopes are hard to fix if they break."
        },
        "misconception_tags": ["space_telescopes_are_closer_to_stars_misconception"]
    }


def _build_constellations_skylore(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    cases = [
        {
            "name": "The Southern Cross (Crux)",
            "navigation": "Used for centuries to determine True South: an imaginary line extended 4.5 times through its long axis points directly towards the South Celestial Pole",
            "lore": "Known in Sotho and Tswana indigenous astronomy as Dithutlwa (the Giraffes)"
        },
        {
            "name": "The Pleiades (Seven Sisters / Isilimela)",
            "navigation": "An open star cluster visible in the eastern sky before sunrise in June",
            "lore": "In Xhosa and Zulu agricultural traditions, known as Isilimela (the digging/plowing stars), signaling the start of the winter plowing and agricultural calendar"
        },
        {
            "name": "Orion (The Hunter)",
            "navigation": "Prominent equatorial constellation featuring Orion's Belt (the Three Kings / Drie Konings)",
            "lore": "In Khoikhoi tradition, the stars of Orion's Belt were seen as three zebras hunted by the great hunter"
        }
    ]
    c = rng.choice(cases)
    prompt = (
        f"Throughout African history, people observed the night skies for seasonal navigation and cultural calendars.\n\n"
        f"Consider the constellation/asterism **{c['name']}**:\n"
        f"1. Explain how this star group is used for practical navigation or seasonal calendar determination ({c['navigation']}).\n"
        f"2. Describe its significance in South African indigenous star lore ({c['lore']})."
    )
    sample_answer = (
        f"1. Practical application: {c['navigation']}.\n"
        f"2. Indigenous significance: {c['lore']}."
    )
    sol = (
        "Marking Rubric (2 marks total):\n"
        f"1. Practical/Navigational use: {c['navigation']} [1 mark].\n"
        f"2. Indigenous star lore: {c['lore']} [1 mark]."
    )
    return {
        "id": _make_id("ns8_skylore", seed, idx),
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "constellations_and_indigenous_skylore",
        "question_family_id": "constellations_and_indigenous_skylore",
        "curriculum_reference": "Natural Sciences Gr8 Term 4 > Looking into Space > Constellations and indigenous astronomy",
        "hints": {
            "tier_1": "Recall how ancient sailors found South using the Southern Cross.",
            "tier_2": "Isilimela (Pleiades) marks the planting season in Xhosa/Zulu culture.",
            "tier_3": f"{c['name']} is used for: {c['navigation']}."
        },
        "misconception_tags": ["constellations_are_physically_connected_stars_misconception"]
    }


def generate(archetype: Optional[str] = None, seed: Optional[int] = None, count: int = 1, **kwargs) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    results = []
    for idx in range(count):
        target = archetype or rng.choice(SUBSKILLS)
        if target == "optical_telescopes_refraction_reflection":
            item = _build_optical_telescopes(rng, seed, idx)
        elif target == "radio_telescopes_and_ska":
            item = _build_radio_ska(rng, seed, idx)
        elif target == "south_african_large_telescope_salt":
            item = _build_salt_observatory(rng, seed, idx)
        elif target == "space_telescopes_vs_ground_telescopes":
            item = _build_space_telescopes(rng, seed, idx)
        elif target == "constellations_and_indigenous_skylore":
            item = _build_constellations_skylore(rng, seed, idx)
        else:
            item = _build_optical_telescopes(rng, seed, idx)
        results.append(item)
    return results


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)
