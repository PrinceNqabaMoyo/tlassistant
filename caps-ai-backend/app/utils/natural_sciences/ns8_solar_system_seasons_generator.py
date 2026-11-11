"""Natural Sciences Grade 7-8 Term 4: Solar System, Seasons & Celestial Mechanics Generator.

Covers:
1. solar_system_diagram: 3-layer anti-leak solar system visual plate with pin identification.
2. seasons_axial_tilt: Earth's 23.5° axial tilt, direct vs indirect solar rays, revolution vs rotation.
3. solar_vs_lunar_eclipses: Celestial alignment (Sun-Moon-Earth vs Sun-Earth-Moon), umbra vs penumbra.
4. planetary_order: 8 planets in order, asteroid belt, terrestrial vs gas giant characteristics.
5. ocean_tides_mechanics: Spring tides (syzygy, New/Full Moon) vs Neap tides (quadrature, quarter moons).

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences.natural_sciences_builders import build_solar_system_question

SUBSKILLS = [
    "solar_system_diagram",
    "seasons_axial_tilt",
    "solar_vs_lunar_eclipses",
    "planetary_order",
    "ocean_tides_mechanics",
]


def _fmt_sa(val: float | int, decimals: int = 1) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_seasons_and_eclipses(r: random.Random, seed: Optional[int], idx: int, mode: str, target_topic: Optional[str] = None) -> Dict[str, Any]:
    """Celestial mechanics: Seasons, eclipses, planetary order, and ocean tides."""
    topic = target_topic or r.choice(["seasons_axial_tilt", "solar_vs_lunar_eclipses", "planetary_order", "ocean_tides_mechanics"])
    qid = _make_id("ns8_astronomy", seed, idx)

    if topic == "seasons_axial_tilt":
        provinces_cities = [
            ("Gauteng (Pretoria)", "December (summer)", "June (winter)"),
            ("KwaZulu-Natal (Durban)", "January (summer)", "July (winter)"),
            ("Western Cape (Cape Town)", "December (summer)", "June (winter)"),
            ("Eastern Cape (Gqeberha)", "December (summer)", "June (winter)"),
            ("Limpopo (Polokwane)", "January (summer)", "July (winter)")
        ]
        city, sum_m, win_m = r.choice(provinces_cities)
        prompt = (
            f"Learners at a school in {city} record local weather patterns, noting warm conditions in {sum_m} and cold conditions in {win_m}.\n\n"
            "1. State the exact angle of tilt of the Earth's rotational axis relative to its orbital plane.\n"
            f"2. Explain why {city} experiences summer in {sum_m}, referring to axial tilt and the angle of solar rays.\n"
            "3. State what causes day and night on Earth."
        )
        ans_str = (
            "1. 23.5 degrees; "
            "2. In December/January, the Southern Hemisphere is tilted towards the Sun, receiving more direct perpendicular solar rays and experiencing longer daylight hours; "
            "3. The rotation of the Earth on its own axis every 24 hours."
        )
        memo = (
            "1. Axial tilt angle: **23.5°** (or 23.5 degrees). [1]\n"
            f"2. Summer explanation [3]: During summer in {city}, the Southern Hemisphere is tilted towards the Sun [1]. "
            "Solar radiant rays strike the Earth at a steep, nearly perpendicular angle, concentrating thermal energy over a smaller surface area [1]. "
            "Additionally, daylight hours are longer than night hours, allowing more solar energy to accumulate [1].\n"
            "3. Day and night cause [1]: Earth's continuous **rotation on its own axis** once every 24 hours (one side faces the Sun while the other faces away). [1]"
        )
        hints = {
            "tier_1": "The tilt angle is about twenty-three and a half degrees. Tilting towards the sun gives direct sun and longer days.",
            "tier_2": "Tilt = 23.5°. Direct rays + longer days in summer. Rotation causes day and night.",
            "tier_3": "1. 23.5°. 2. Southern hemisphere is tilted towards the sun, receiving direct rays and longer daylight. 3. Rotation on its axis.",
        }
        marks = 5
        misconceptions = ["distance_from_sun_causes_seasons_misconception", "confused_rotation_with_revolution"]
    elif topic == "solar_vs_lunar_eclipses":
        observatories = [
            "South African Astronomical Observatory (SAAO) in Sutherland",
            "Boyden Observatory outside Bloemfontein",
            "HartRAO Radio Astronomy Observatory in Gauteng",
            "Astronomers at the Cape Town Planetarium"
        ]
        obs = r.choice(observatories)
        prompt = (
            f"{obs} documents celestial events where the Sun, Earth, and Moon align in a straight line in space.\n\n"
            "1. State the sequential order of celestial bodies during a **solar eclipse**.\n"
            "2. State the sequential order of celestial bodies during a **lunar eclipse**.\n"
            "3. Distinguish between the **umbra** and the **penumbra** of an astronomical shadow.\n"
            "4. Explain why a solar eclipse only occurs during the New Moon phase."
        )
        ans_str = (
            "1. Sun - Moon - Earth; "
            "2. Sun - Earth - Moon; "
            "3. Umbra is the dark central region of complete shadow; Penumbra is the lighter outer region of partial shadow; "
            "4. Only during New Moon is the Moon positioned directly between the Sun and Earth."
        )
        memo = (
            "1. Solar eclipse alignment: **Sun — Moon — Earth** (Moon is in the middle). [1]\n"
            "2. Lunar eclipse alignment: **Sun — Earth — Moon** (Earth is in the middle). [1]\n"
            "3. Shadow regions [2]:\n"
            "   - **Umbra**: The completely dark, innermost conical shadow where all direct sunlight is blocked [1].\n"
            "   - **Penumbra**: The lighter, outer region of partial shadow where only a portion of the Sun's light is obscured [1].\n"
            "4. New Moon rationale [2]: During the New Moon phase, the Moon is positioned between the Earth and the Sun [1], "
            "which is the only geometric configuration where its shadow can fall onto the Earth's surface [1]."
        )
        hints = {
            "tier_1": "Solar eclipse = Moon in the middle. Lunar eclipse = Earth in the middle. Umbra is total shadow.",
            "tier_2": "Solar: Sun-Moon-Earth. Lunar: Sun-Earth-Moon. Umbra = complete darkness; Penumbra = partial shadow.",
            "tier_3": "1. Sun-Moon-Earth. 2. Sun-Earth-Moon. 3. Umbra = complete shadow; Penumbra = partial shadow. 4. Moon is between Sun and Earth.",
        }
        marks = 6
        misconceptions = ["solar_lunar_eclipse_order_inversion", "confused_umbra_with_penumbra"]
    elif topic == "ocean_tides_mechanics":
        coastal_spots = [
            "Durban harbour along the Indian Ocean",
            "Table Bay harbour in Cape Town",
            "Port of Ngqura in Gqeberha",
            "Mossel Bay coastline in the Western Cape",
            "Richards Bay harbour along the KwaZulu-Natal coast"
        ]
        harbour = r.choice(coastal_spots)
        prompt = (
            f"Maritime navigators at {harbour} closely monitor tidal heights driven by the gravitational pull of the Moon and the Sun on Earth's oceans.\n\n"
            "1. Explain what causes **spring tides** and name the two Moon phases during which spring tides occur.\n"
            "2. Explain what causes **neap tides** and name the two Moon phases during which neap tides occur.\n"
            "3. State whether high tides are higher during spring tides or neap tides, and give a reason for your answer."
        )
        ans_str = (
            "1. Spring tides occur when Sun, Earth, and Moon align in a straight line, combining gravitational pull (New Moon and Full Moon); "
            "2. Neap tides occur when Moon is at right angles to Sun-Earth line, partially cancelling gravitational pull (First and Third Quarter Moon); "
            "3. High tides are higher during spring tides because the gravitational forces of Sun and Moon reinforce each other."
        )
        memo = (
            "1. Spring tides [3]: Occur when the Sun, Earth, and Moon align in a straight line [1]. "
            "Their combined gravitational forces produce the greatest tidal range (extra-high high tides and extra-low low tides) [1]. "
            "Occurs during **New Moon** and **Full Moon** [1].\n"
            "2. Neap tides [3]: Occur when the Moon is at a 90° right angle to the Sun-Earth line [1]. "
            "The gravitational pulls partially cancel each other out, producing lower high tides and higher low tides [1]. "
            "Occurs during **First Quarter** and **Third Quarter** [1].\n"
            f"3. Comparison [2]: High tides at {harbour} are **higher during spring tides** [1] because the solar and lunar gravitational pulls reinforce each other along the same axis [1]."
        )
        hints = {
            "tier_1": "Spring tides = combined gravity (straight line). Neap tides = right angles (partial cancellation).",
            "tier_2": "Spring tides happen at New and Full Moon. Neap tides happen at quarter moons.",
            "tier_3": "1. Spring tides: aligned gravity at New/Full Moon. 2. Neap tides: 90° angle at quarter moons. 3. Spring high tides are higher.",
        }
        marks = 8
        misconceptions = ["confuses_spring_tides_with_spring_season", "neap_tides_misconception"]
    else:  # planetary_order
        topic = "planetary_order"
        missions = [
            ("the South African National Space Agency (SANSA)", "robotic space probes"),
            ("planetary scientists analyzing interplanetary flybys", "deep space orbiters"),
            ("an astronomical research team studying orbital dynamics", "telescopic survey data")
        ]
        agency, tool = r.choice(missions)
        prompt = (
            f"In an astronomy project conducted with {agency}, learners examine {tool} tracking our solar system.\n\n"
            "1. List the eight major planets in chronological order starting closest to the Sun.\n"
            "2. Name the region separating the rocky terrestrial planets from the gas giant planets.\n"
            "3. State TWO major physical differences between terrestrial planets (e.g. Earth, Mars) and gas giants (e.g. Jupiter, Saturn)."
        )
        ans_str = (
            "1. Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune; "
            "2. Asteroid Belt; "
            "3. Terrestrial planets are small, dense, and composed of solid rock and metal; Gas giants are massive, low-density, composed of hydrogen and helium, and have ring systems."
        )
        memo = (
            "1. Planetary order from the Sun [4]:\n"
            "   Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune. [4]\n"
            "   (0.5 marks per planet in correct sequence).\n"
            "2. Separation region: **Asteroid Belt**. [1]\n"
            "3. Terrestrial vs Gas Giant differences (any 2) [2]:\n"
            "   - Composition: Terrestrial planets have solid rocky/metallic surfaces [1]; gas giants are fluid spheres of hydrogen and helium with no solid surface [1].\n"
            "   - Size and density: Terrestrial planets are smaller and much denser; gas giants are massive with very low average densities [1].\n"
            "   - Ring systems: Gas giants have planetary rings; terrestrial planets do not [1]."
        )
        hints = {
            "tier_1": "Use the mnemonic: My Very Educated Mother Just Served Us Noodles. Asteroids lie between Mars and Jupiter.",
            "tier_2": "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune. Rocky inner planets vs gas giant outer planets.",
            "tier_3": "1. Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune. 2. Asteroid Belt. 3. Rocky/solid vs gaseous/hydrogen.",
        }
        marks = 7
        misconceptions = ["pluto_included_as_major_planet", "planetary_order_error"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 4,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 8,
        "mode": mode,
        "subskill": topic,
        "question_family_id": topic,
        "question_type": "short_answer",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "canonical_solution": memo,
        "solution": memo,
        "marks": marks,
        "total_marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Scientific facts (axial tilt / alignment / planetary sequence)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Astronomical mechanism explanation", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Comparative distinction or environmental cause", "marks": marks - 5, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master entry point for Grade 7-8 Solar System, Moon & Seasons."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []
    raw_grade = str(kwargs.get("grade", 8)).replace("grade_", "").replace("g", "").strip()
    gr_int = int(raw_grade) if raw_grade.isdigit() else 8

    base_seed = seed if seed is not None else r.randint(1, 1_000_000_000)
    target_sub = str(subskill or "").strip().lower()

    for i in range(count):
        sub_seed = base_seed + i * 17
        sub_r = random.Random(sub_seed)

        if target_sub in SUBSKILLS:
            cur_sub = target_sub
        else:
            cur_sub = SUBSKILLS[i % len(SUBSKILLS)]

        if cur_sub == "solar_system_diagram":
            q = build_solar_system_question(sub_seed, grade=gr_int, mode=mode)
        else:
            q = _generate_seasons_and_eclipses(sub_r, sub_seed, i, mode, target_topic=cur_sub)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
