"""Natural Sciences Senior Phase (Grades 7–9) — Term 4: Planet Earth and Beyond Generator.
Deterministic 6-pillar CAPS question generator covering:
- Grade 7: Sun, Earth and Moon Mechanics (tilt of axis, seasons, solar/lunar eclipses, spring and neap ocean tides).
- Grade 8: Solar System Anatomy (rocky terrestrial planets vs gas giants, asteroid belt), Astronomical Observatories (SALT, MeerKAT, SKA).
- Grade 9: Earth as a System (interconnected spheres), The Lithosphere & South African Mining (mineral extraction, acid mine drainage), Stellar Evolution (nebulae, main sequence, supernovae).
Supports compound exam questions and atomic elementary sub-drills.
Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import (
    fmt_sa,
    make_science_question,
    rng,
)

TOPIC = "natural_sciences_planet_earth_and_beyond"
LO = "ns_senior_planet_earth_beyond"

# ============================================================================
# ARCHETYPE 1: SEASONS, TIDES & ECLIPSES (Grade 7)
# ============================================================================

def _gen_sun_earth_moon_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    tide_type = r.choice(["Spring tides", "Neap tides"])
    
    if tide_type == "Spring tides":
        tide_align = "The Sun, Earth, and Moon are aligned in a straight line (Syzygy) during either New Moon or Full Moon."
        tide_effect = "The combined gravitational attraction of both the Sun and Moon produces the highest high tides and lowest low tides (maximum tidal range)."
    else:
        tide_align = "The Moon is at a right angle (90 degrees) relative to the Sun-Earth line during First Quarter or Third Quarter moon phases."
        tide_effect = "The gravitational pull of the Sun partially cancels that of the Moon, resulting in lower high tides and higher low tides (minimum tidal range)."

    prompt = (
        f"Astronomical movements of the Earth and Moon govern cycles of day and night, seasons, and ocean tides.\n\n"
        f"1. Explain why Earth experiences four distinct seasons during its orbit around the Sun. "
        f"State the angle of tilt of the Earth's rotational axis.\n"
        f"2. During which calendar month does the Southern Hemisphere experience its **Summer Solstice**?\n"
        f"3. Explain the gravitational alignment that causes **{tide_type}** in our coastal oceans, and describe the resulting water levels.\n"
        f"4. Differentiate between a **solar eclipse** and a **lunar eclipse** in terms of which celestial body casts a shadow on which."
    )
    prompt_latex = (
        rf"\textbf{{Astronomical Mechanics: Earth, Moon & Sun}}" "\n\n"
        rf"\text{{1. Orbital tilt and mechanism of seasons (Axial tilt }} \theta \approx 23,5^\circ\text{{)}}" "\n"
        rf"\text{{2. Southern Hemisphere Summer Solstice timing}}" "\n"
        rf"\text{{3. Gravitational alignment for {tide_type}}}" "\n"
        r"\text{4. Solar eclipse vs. Lunar eclipse geometry}"
    )
    answer_latex = (
        r"\text{1. Earth's rotational axis is tilted at } 23{,}5^\circ\text{ relative to its orbital plane. As Earth revolves around the Sun, "
        r"different hemispheres lean towards the Sun (receiving direct, concentrated sunlight for longer daylight hours) or away.}" "\n"
        r"\text{2. December (around 21-22 December).}" "\n"
        rf"\text{{3. Alignment: {tide_align} Effect: {tide_effect}}}" "\n"
        r"\text{4. Solar eclipse: Moon passes between Sun and Earth, casting Moon's shadow on Earth. "
        r"Lunar eclipse: Earth passes between Sun and Moon, casting Earth's shadow across the Full Moon.}"
    )
    sample = (
        "1. Seasons are caused by the 23,5° tilt of Earth's rotational axis combined with its revolution around the Sun. "
        "When a hemisphere is tilted toward the Sun, solar rays strike at a direct, concentrated angle, and daylight hours are longer, creating summer.\n"
        "2. December (approximately 21 December).\n"
        f"3. {tide_align} {tide_effect}\n"
        "4. A solar eclipse occurs when the Moon moves directly between the Sun and the Earth, casting the Moon's shadow onto Earth's surface during the day. "
        "A lunar eclipse occurs when the Earth passes directly between the Sun and the Moon, casting Earth's shadow onto the Moon during the night."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Explain 23,5° axial tilt and revolution causing seasons", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Identify December for Southern Hemisphere Summer Solstice", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurately explain {tide_type} alignment and tidal range", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Accurately contrast solar vs lunar eclipse geometry", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Seasons are not caused by Earth being closer or further from the Sun; they are caused by axial tilt (23,5°).",
        "concept": "Spring tides = Sun, Earth, Moon in a straight line (maximum range). Neap tides = 90° right angle (minimum range).",
        "breakdown": f"Axis tilt = 23,5°. December = Southern summer solstice. {tide_type}: {tide_align[:60]}...",
    }
    return make_science_question(
        prefix="ns_seasons_tides",
        topic=TOPIC,
        subskill="earth_moon_sun_mechanics_and_tides",
        learning_objective_id=f"{LO}_seasons_and_tides",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["believing_distance_from_sun_causes_seasons", "confusing_solar_and_lunar_eclipses"],
        keywords=["seasons", "axial tilt", "solstice", "tides", "eclipse", "spring tide", "neap tide"],
        term=4,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=7,
    )


# ============================================================================
# ARCHETYPE 2: LITHOSPHERE & MINING IN SOUTH AFRICA (Grade 9)
# ============================================================================

MINERALS_SA = [
    {
        "mineral": "Gold (Au)",
        "mining_region": "Witwatersrand Basin / Free State",
        "ore_extraction": "Deep underground shaft mining; ore is crushed and treated with dilute sodium cyanide solution to dissolve gold",
        "environmental_impact": "Acid Mine Drainage (AMD): Oxidation of pyrite minerals in unsealed abandoned shafts generates toxic sulphuric acid and leaches heavy metals into groundwater",
    },
    {
        "mineral": "Iron Ore (Haematite, Fe2O3)",
        "mining_region": "Sishen / Kolomela (Northern Cape)",
        "ore_extraction": "Open-cast (open-pit) surface mining; blasting and heavy mechanical shovel excavation",
        "environmental_impact": "Extensive habitat destruction, massive dust pollution, and depression of local water tables from de-watering open pits",
    },
    {
        "mineral": "Coal",
        "mining_region": "Highveld Basin / Mpumalanga (e.g. eMalahleni)",
        "ore_extraction": "Both open-cast strip mining and underground bord-and-pillar mining",
        "environmental_impact": "Severe air pollution (sulphur dioxide SO2 and greenhouse gases), sinkhole formation from collapsed pillars, and acid runoff contaminating rivers",
    },
]


def _gen_lithosphere_mining_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    min_data = r.choice(MINERALS_SA)
    
    prompt = (
        f"The lithosphere is the rigid outer crust and upper mantle of the Earth containing vital non-renewable mineral resources. "
        f"In South Africa, the mining and refining of **{min_data['mineral']}** is a major industrial sector.\n\n"
        f"1. Name the primary geological province / region in South Africa where {min_data['mineral']} is mined.\n"
        f"2. Describe the primary extraction method used to recover {min_data['mineral']} ore from the ground.\n"
        f"3. Explain the environmental threat of: *'{min_data['environmental_impact']}'*.\n"
        f"4. Propose TWO mandatory environmental rehabilitation measures mining corporations must carry out once a mine ceases active operations."
    )
    prompt_latex = (
        rf"\textbf{{Lithospheric Geology & Mining: {min_data['mineral']} Extraction in South Africa}}" "\n\n"
        rf"\text{{1. Mining region: Geographical location}}" "\n"
        rf"\text{{2. Extraction and beneficiation engineering}}" "\n"
        rf"\text{{3. Environmental hazard analysis: {min_data['environmental_impact'][:70]}...}}" "\n"
        r"\text{4. Post-closure environmental rehabilitation strategies}"
    )
    answer_latex = (
        rf"\text{{1. Geographical region: {min_data['mining_region']}.}}" "\n"
        rf"\text{{2. Method: {min_data['ore_extraction']}.}}" "\n"
        rf"\text{{3. Environmental impact: {min_data['environmental_impact']}}}" "\n"
        r"\text{4. Rehabilitation: Neutralising acidic waters with limestone, sealing shafts/tailings dams, "
        r"re-contouring open pits, replacing topsoil, and replanting indigenous vegetation.}"
    )
    sample = (
        f"1. Primary region: {min_data['mining_region']}.\n"
        f"2. Extraction method: {min_data['ore_extraction']}.\n"
        f"3. Environmental impact: {min_data['environmental_impact']}.\n"
        "4. Mine rehabilitation measures:\n"
        "   - Backfilling open pits and re-contouring spoil heaps to match natural topography.\n"
        "   - Neutralising acid mine drainage with calcium carbonate/lime and planting indigenous vegetation to stabilise topsoil."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct South African mining location for {min_data['mineral']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Accurate mining extraction method described", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Thorough environmental hazard explanation (e.g. AMD or habitat loss)", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Two realistic post-mining ecological rehabilitation solutions", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Think about acid mine drainage (AMD) when pyrite oxidises in water, or open-cast pit rehabilitation.",
        "concept": "Minerals in the lithosphere are non-renewable. Sustainable mining requires environmental impact assessment and topsoil restoration.",
        "breakdown": f"Mineral: {min_data['mineral']}. Region: {min_data['mining_region']}. Hazard: {min_data['environmental_impact'][:80]}...",
    }
    return make_science_question(
        prefix="ns_litho_mine",
        topic=TOPIC,
        subskill="lithosphere_mining_methods_and_environmental_impact",
        learning_objective_id=f"{LO}_lithosphere_mining",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["failing_to_explain_acid_mine_drainage_chemistry", "confusing_open_cast_with_shaft_mining"],
        keywords=["lithosphere", "mining", "acid mine drainage", "rehabilitation", "gold", "coal"],
        term=4,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=7,
    )


# ============================================================================
# ARCHETYPE 3: STELLAR EVOLUTION & TELESCOPES (Grade 8)
# ============================================================================

def _gen_stellar_evolution_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    star_type = r.choice(["Massive star (greater than 8 solar masses)", "Sun-like star (average low/medium mass)"])
    
    if "Massive" in star_type:
        cycle_stages = "Stellar Nebula -> Massive Main Sequence -> Red Supergiant -> Supernova explosion -> Neutron Star or Black Hole"
        final_fate = "Supernova explosion leaving a core that collapses into an ultra-dense Neutron Star or a Black Hole (singularity)."
    else:
        cycle_stages = "Stellar Nebula -> Main Sequence star -> Red Giant -> Planetary Nebula -> White Dwarf -> (Black Dwarf)"
        final_fate = "Red Giant sheds its outer atmospheric layers as a planetary nebula, leaving a dense, cooling White Dwarf core."

    prompt = (
        f"Stars undergo a lifecycle driven by the opposing forces of inward gravitational collapse and outward nuclear fusion pressure.\n\n"
        f"1. Name the dense cloud of interstellar gas and dust where all stars begin their formation.\n"
        f"2. Identify the nuclear reaction taking place in the core of a **main sequence star** that produces its vast energy output.\n"
        f"3. Trace the evolutionary lifecycle stages of a **{star_type}** from birth to its final remnant.\n"
        f"4. Name ONE major world-class astronomical observatory located in the Karoo region of South Africa, and state whether it detects optical light or radio waves."
    )
    prompt_latex = (
        rf"\textbf{{Astrophysics: Stellar Evolution & Observational Astronomy}}" "\n\n"
        rf"\text{{Lifecycle of: {star_type}}}" "\n\n"
        r"\text{1. Stellar nursery; 2. Core nuclear fusion mechanism; 3. Life cycle sequence; 4. South African observatories (SALT / MeerKAT / SKA).}"
    )
    answer_latex = (
        r"\text{1. Stellar Nebula.}" "\n"
        r"\text{2. Nuclear fusion: Hydrogen nuclei fuse under intense pressure and temperature to form Helium (} 4\,{}^1\text{H} \to {}^4\text{He} + \text{energy} \text{).}" "\n"
        rf"\text{{3. Sequence: {cycle_stages}. Final fate: {final_fate}}}" "\n"
        r"\text{4. SALT (Southern African Large Telescope) near Sutherland detects optical light; OR MeerKAT / SKA in the Northern Cape detects radio waves.}"
    )
    sample = (
        "1. Stellar Nebula.\n"
        "2. Nuclear fusion of hydrogen nuclei into helium nuclei.\n"
        f"3. Sequence: {cycle_stages}.\n"
        "4. SALT (Southern African Large Telescope) near Sutherland detects optical visible light (or MeerKAT / SKA in Carnarvon detecting radio waves)."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Identify stellar nebula", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Explain nuclear fusion of hydrogen into helium", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Accurate sequential lifecycle for {star_type}", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Accurately name SALT (optical) or MeerKAT/SKA (radio)", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Stars fuse hydrogen into helium in their cores. SALT is optical; MeerKAT and SKA are radio telescopes.",
        "concept": "Massive stars end in supernovae and black holes; average stars end as white dwarfs.",
        "breakdown": f"Stellar life cycle: {cycle_stages}.",
    }
    return make_science_question(
        prefix="ns_stellar",
        topic=TOPIC,
        subskill="stellar_evolution_and_astronomical_observatories",
        learning_objective_id=f"{LO}_stellar_evolution",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["confusing_nuclear_fusion_with_fission", "confusing_salt_optical_with_meerkat_radio"],
        keywords=["nebula", "nuclear fusion", "supernova", "black hole", "white dwarf", "SALT", "MeerKAT"],
        term=4,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=7,
    )


# ============================================================================
# MAIN DISPATCH ENTRY POINT
# ============================================================================

def generate(seed: Optional[int] = None, grade: int = 8, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    """Generates a fully formed 6-pillar Natural Sciences Planet Earth & Beyond question."""
    r = rng(seed)
    
    if archetype == "sun_earth_moon" or (archetype is None and grade == 7):
        return _gen_sun_earth_moon_question(r, mode=mode)
    elif archetype == "stellar" or (archetype is None and grade == 8):
        return _gen_stellar_evolution_question(r, mode=mode)
    elif archetype == "lithosphere" or (archetype is None and grade == 9):
        return _gen_lithosphere_mining_question(r, mode=mode)
    else:
        choice = r.choice(["sun_earth_moon", "stellar", "lithosphere"])
        if choice == "sun_earth_moon":
            return _gen_sun_earth_moon_question(r, mode=mode)
        elif choice == "stellar":
            return _gen_stellar_evolution_question(r, mode=mode)
        else:
            return _gen_lithosphere_mining_question(r, mode=mode)
