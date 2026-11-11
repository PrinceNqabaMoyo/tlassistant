"""Subskills 41 to 46: Compass Directions, Bearings, Building Elevations & Geographic Coordinates.
Covers 8-point compass directions, 3-figure bearings, highway overhead lane signage,
architectural elevation view orientations (North/South/East/West), Southern hemisphere solar design,
and South African latitude/longitude coordinates (degrees, minutes, seconds).
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Identifying cardinal and intercardinal compass directions between two points."""
    direction_pairs = [
        ("Bloemfontein", "Johannesburg", "North-North-East (approx. North-East)"),
        ("Johannesburg", "Durban", "South-East"),
        ("Cape Town", "Bloemfontein", "North-East"),
        ("Bloemfontein", "Cape Town", "South-West"),
        ("Johannesburg", "Polokwane", "North-East (approx. North)"),
        ("Durban", "Johannesburg", "North-West"),
    ]
    city_from, city_to, correct_dir = r.choice(direction_pairs)

    prompt = (
        f"A pilot flies directly from {city_from} to {city_to} across South Africa.\n\n"
        f"Using an 8-point compass rose (North, North-East, East, South-East, South, South-West, West, North-West):\n"
        f"In which general compass direction is the plane travelling?"
    )

    correct_ans = correct_dir
    explanation = (
        f"1. On a standard map of South Africa, {city_to} is situated {correct_dir} of {city_from}."
    )
    t1 = "Imagine a compass rose centered on the departure city and look towards the destination."
    t2 = f"From {city_from} looking to {city_to} is {correct_dir}."
    t3 = f"Direction = {correct_ans}."

    all_dirs = ["North-East", "South-East", "South-West", "North-West", "North", "South"]
    other_dirs = [d for d in all_dirs if d not in correct_dir][:3]
    custom_opts = [correct_ans] + other_dirs

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_41",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Subskill 42: Determining 3-figure compass bearings."""
    bearings = [
        ("due North", "000° (or 360°)"),
        ("due East", "090°"),
        ("due South", "180°"),
        ("due West", "270°"),
        ("North-East", "045°"),
        ("South-East", "135°"),
        ("South-West", "225°"),
        ("North-West", "315°"),
    ]
    direction_name, correct_bearing = r.choice(bearings)

    prompt = (
        f"A sea rescue boat steers along a course heading {direction_name}.\n\n"
        f"Recall that 3-figure bearings are measured clockwise from True North (000°).\n"
        f"State the 3-figure bearing for {direction_name}."
    )

    correct_ans = correct_bearing
    explanation = (
        f"1. Bearings start at North (000°) and increase clockwise:\n"
        f"   • East = 090°, South = 180°, West = 270°.\n"
        f"2. {direction_name} corresponds to {correct_bearing}."
    )
    t1 = "Measure clockwise from North at 000° in increments of 45°."
    t2 = f"{direction_name} is at {correct_bearing}."
    t3 = f"Bearing = {correct_ans}."

    other_bearings = [b[1] for b in bearings if b[1] != correct_bearing][:3]
    custom_opts = [correct_ans] + other_bearings

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_42",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Subskill 43: Reading highway directional overhead lane signage."""
    prompt = (
        f"A driver traveling along the N1 freeway near Midrand encounters an overhead gantry sign:\n"
        f"• Left 2 lanes: [N1 North] towards Pretoria / Polokwane\n"
        f"• Right 2 lanes: [N1 South] towards Johannesburg / Bloemfontein\n\n"
        f"The driver is travelling from Centurion to OR Tambo International Airport via the R21 / N1 South.\n"
        f"Which lane group should the driver occupy to continue towards Johannesburg / N1 South?"
    )

    correct_ans = "The right 2 lanes (N1 South towards Johannesburg)"
    explanation = (
        f"1. The overhead signboard assigns the right 2 lanes to N1 South towards Johannesburg.\n"
        f"2. Occupying the right lanes allows the driver to proceed southwards."
    )
    t1 = "Match the destination with the direction indicated on the overhead gantry sign."
    t2 = "N1 South leads towards Johannesburg in the right 2 lanes."
    t3 = f"Correct lane: {correct_ans}."

    custom_opts = [
        correct_ans,
        "The left 2 lanes (N1 North towards Pretoria)",
        "Any lane, because all lanes go to Johannesburg",
        "The emergency breakdown shoulder lane on the far left",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_43",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Interpreting building elevation views: identifying elevations from a floor plan."""
    wall_dir = r.choice(["South", "North", "East", "West"])
    opposite = {"South": "North", "North": "South", "East": "West", "West": "East"}[wall_dir]

    d_spec_44 = {
        "diagram_role": "context",
        "kind": "elevation_compass",
        "title": f"Building Elevation Compass ({wall_dir} Wall)",
        "wall_direction": wall_dir,
        "north_facing_wall": wall_dir,
        "target_dir": opposite,
        "compass": wall_dir,
    }

    prompt = (
        f"Refer to the building elevation compass scheme.\n"
        f"If an observer is standing outside a house looking directly at the '{wall_dir} Elevation', "
        f"in which compass direction is the observer facing?"
    )

    correct_ans = f"Facing {opposite} (looking towards the {wall_dir}-facing wall)"
    explanation = (
        f"1. The '{wall_dir} Elevation' is the side of the building that faces {wall_dir} towards the outside.\n"
        f"2. A person standing outside looking directly at this wall must be looking {opposite}."
    )
    t1 = f"A {wall_dir} Elevation faces {wall_dir}; to see it from the outside, you must look in the opposite direction ({opposite})."
    t2 = f"Opposite of {wall_dir} is {opposite}."
    t3 = f"Observer orientation: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Facing {wall_dir}",
        "Facing East" if wall_dir in ("North", "South") else "Facing North",
        "Facing West" if wall_dir in ("North", "South") else "Facing South",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_44",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_44,
    )


def gen_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Subskill 45: Solar orientation in South Africa: determining which rooms get maximum winter sunlight."""
    prompt = (
        f"In the Southern Hemisphere (including South Africa), the sun rises in the east and tracks "
        f"across the northern sky at midday, before setting in the west.\n\n"
        f"An architect designs an eco-friendly passive solar home in the Free State.\n"
        f"Which side of the house should have the largest windows and main living areas to capture "
        f"maximum natural heat and sunlight during cold winter months?"
    )

    correct_ans = "The North-facing side"
    explanation = (
        f"1. Because South Africa is in the Southern Hemisphere, the sun is positioned to the North during the day.\n"
        f"2. In winter, the sun's midday elevation angle is lower in the northern sky, allowing maximum warmth to penetrate North-facing windows."
    )
    t1 = "In South Africa, the sun tracks across the northern sky."
    t2 = "North-facing rooms receive the most winter sunlight in the Southern hemisphere."
    t3 = f"Orientation: {correct_ans}."

    custom_opts = [
        correct_ans,
        "The South-facing side",
        "The West-facing side (to avoid afternoon glare)",
        "The East-facing side only",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_45",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Subskill 46: Interpreting latitude and longitude coordinates on a South African map."""
    places = [
        ("Cape Town", "33° 55' 31\" S", "18° 25' 26\" E"),
        ("Johannesburg", "26° 12' 16\" S", "28° 02' 44\" E"),
        ("Durban", "29° 51' 29\" S", "31° 01' 55\" E"),
        ("Bloemfontein", "29° 07' 00\" S", "26° 13' 00\" E"),
    ]
    city, lat, lon = r.choice(places)

    prompt = (
        f"A GPS reading for {city} gives coordinates: {lat}, {lon}.\n\n"
        f"Which of the following statements correctly interprets these geographic coordinates?"
    )

    correct_ans = f"Latitude is {lat} (South of the Equator); Longitude is {lon} (East of the Greenwich Prime Meridian)"
    explanation = (
        f"1. Latitude measures position North or South of the Equator. South Africa lies entirely in the Southern Hemisphere ('S').\n"
        f"2. Longitude measures position East or West of the Prime Meridian. South Africa lies entirely East ('E') of Greenwich.\n"
        f"3. Correct interpretation: {correct_ans}."
    )
    t1 = "Latitude = South of Equator; Longitude = East of Prime Meridian."
    t2 = f"{lat} is Latitude; {lon} is Longitude."
    t3 = f"Interpretation: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Latitude is {lon} (East of Equator); Longitude is {lat} (South of Meridian)",
        f"Both coordinates represent longitude East of the Equator",
        f"Latitude is {lat} (North of the Equator); Longitude is {lon} (West of Greenwich)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_46",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )
