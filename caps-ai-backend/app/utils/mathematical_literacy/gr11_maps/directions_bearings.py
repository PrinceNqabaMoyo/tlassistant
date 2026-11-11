"""Subskills 10 to 18: Directions, Bearings, Alphanumeric Grids & Navigation for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: Cardinal and inter-cardinal compass directions between two locations."""
    directions = [
        ("North-East", "East and North"),
        ("North-West", "West and North"),
        ("South-East", "East and South"),
        ("South-West", "West and South"),
        ("North", "directly upward towards the top of the map"),
        ("South", "directly downward towards the bottom of the map"),
        ("East", "directly to the right"),
        ("West", "directly to the left"),
    ]
    dir_name, dir_desc = r.choice(directions)
    town_a = r.choice(["Bloemfontein", "Kimberley", "Polokwane", "Nelspruit", "Mthatha"])
    town_b = r.choice(["Durban", "Cape Town", "Pretoria", "Upington", "Gqeberha"])

    prompt = (
        f"On a provincial road map where North points directly to the top edge of the page, "
        f"{town_b} is located {dir_desc} relative to {town_a}.\n"
        f"In which compass direction should a driver travel from {town_a} to reach {town_b}?"
    )

    correct_ans = dir_name
    all_dirs = ["North-East", "North-West", "South-East", "South-West", "North", "South", "East", "West"]
    distractors = [d for d in all_dirs if d != dir_name][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Orient using standard compass directions [1 mark].\n"
        f"Top = North, Bottom = South, Right = East, Left = West.\n"
        f"Step 2: Relate {dir_desc} to compass points [1 mark].\n"
        f"Moving {dir_desc} corresponds to {dir_name}.\n"
        f"Step 3: Stated direction [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="10",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Use the compass rose: North is up, South is down, East is right, West is left.",
        tier_2=f"Moving {dir_desc} corresponds to {dir_name}.",
        tier_3=f"Direction: {dir_name}.",
        r=r,
    )


def generate_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Subskill 11: Opposite direction of return travel."""
    opposite_pairs = [
        ("North-East", "South-West"),
        ("North-West", "South-East"),
        ("South-East", "North-West"),
        ("South-West", "North-East"),
        ("North", "South"),
        ("South", "North"),
        ("East", "West"),
        ("West", "East"),
    ]
    outbound, inbound = r.choice(opposite_pairs)
    town_a = "Johannesburg"
    town_b = "Durban"

    prompt = (
        f"A sales representative travels from {town_a} to {town_b} in a general {outbound} direction.\n"
        f"When returning from {town_b} back to {town_a} along the same route, in which general compass direction "
        f"will the representative be travelling?"
    )

    correct_ans = inbound
    all_dirs = ["North-East", "North-West", "South-East", "South-West", "North", "South", "East", "West"]
    distractors = [d for d in all_dirs if d not in (outbound, inbound)][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Understand reverse bearings and directions [1 mark].\n"
        f"A return journey along the same trajectory is rotated by 180°.\n"
        f"Step 2: Invert the cardinal components [1 mark].\n"
        f"The opposite of {outbound} is {inbound}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="11",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The return journey travels in the exact 180° opposite direction.",
        tier_2=f"The opposite of {outbound} is {inbound}.",
        tier_3=f"Return direction: {inbound}.",
        r=r,
    )


def generate_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Subskill 12: Alphanumeric grid coordinate lookup on a street map with diagram_spec."""
    cols = ["A", "B", "C", "D", "E"]
    rows = ["1", "2", "3", "4"]

    target_col = r.choice(["B", "C", "D"])
    target_row = r.choice(["2", "3"])
    target_cell = f"{target_col}{target_row}"

    facility = r.choice(["District Hospital", "Police Station", "Public Library", "Fire Station", "Post Office"])

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "grid_map",
        "title": "Township Street Grid Map",
        "columns": cols,
        "rows": rows,
        "facility": facility,
        "coordinate": target_cell,
    }

    prompt = (
        f"On a municipal town planning grid map, columns are lettered A through E from left to right, "
        f"and rows are numbered 1 through 4 from top to bottom. "
        f"The {facility} is situated in column {target_col} and row {target_row}.\n"
        f"What is the alphanumeric grid reference for the {facility}?"
    )

    correct_ans = target_cell
    wrong_1 = f"{target_row}{target_col}"  # inverted
    wrong_2 = f"{cols[cols.index(target_col) - 1]}{target_row}"
    wrong_3 = f"{target_col}{int(target_row) + 1}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State standard alphanumeric convention [1 mark].\n"
        f"Grid references are given as (Column Letter)(Row Number).\n"
        f"Step 2: Combine coordinates [1 mark].\n"
        f"Column {target_col} and Row {target_row} combine to form {target_cell}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="12",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Alphanumeric grid references write the column letter first, followed by the row number.",
        tier_2=f"Column is {target_col} and Row is {target_row}.",
        tier_3=f"Grid reference = {target_cell}.",
        r=r,
        diagram_spec=diagram_spec,
    )


def generate_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Identify facility located at given alphanumeric grid coordinates."""
    facility_map = {
        "A1": "Sports Stadium",
        "B2": "Community Health Clinic",
        "C3": "Secondary School",
        "D4": "Shopping Centre",
    }
    target_coord, target_facility = r.choice(list(facility_map.items()))

    table_desc = "\n".join([f"• Grid {coord}: {fac}" for coord, fac in facility_map.items()])
    prompt = (
        f"A tourist guide map features an index of key facilities:\n"
        f"{table_desc}\n\n"
        f"Which facility is located in grid square **{target_coord}**?"
    )

    correct_ans = target_facility
    options, _ = _build_options(correct_ans, r, custom_options=list(facility_map.values()))

    explanation = (
        f"Step 1: Locate the requested grid coordinate in the map index [1 mark].\n"
        f"Target coordinate: {target_coord}.\n"
        f"Step 2: Read the corresponding facility name [1 mark].\n"
        f"Grid square {target_coord} contains the {target_facility}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="13",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Read the index or table row matching the given grid coordinate.",
        tier_2=f"Look for grid reference {target_coord}.",
        tier_3=f"Facility: {target_facility}.",
        r=r,
    )


def generate_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Subskill 14: Step-by-step turn-by-turn navigation directions."""
    name = r.choice(SA_NAMES)
    street_1 = "Mandela Avenue"
    street_2 = "Sisulu Street"
    street_3 = "Tambo Road"
    destination = "Municipal Clinic"

    prompt = (
        f"{name} is giving driving directions from the community hall to the {destination}:\n"
        f"\"Exit the gate, turn right onto {street_1} heading East for 500 m. "
        f"At the traffic circle, take the 3rd exit heading South onto {street_2} for 800 m. "
        f"Turn left onto {street_3} heading East. The {destination} is on your right after 200 m.\"\n"
        f"At the intersection of {street_2} and {street_3}, which way does {name} turn and in which compass direction does {name} travel?"
    )

    correct_ans = f"Turn left heading East onto {street_3}"
    wrong_1 = f"Turn right heading West onto {street_3}"
    wrong_2 = f"Turn left heading South onto {street_1}"
    wrong_3 = f"Continue straight heading North onto {street_2}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Extract the specific instruction for that intersection [1 mark].\n"
        f"The instruction states: 'Turn left onto {street_3} heading East'.\n"
        f"Step 2: Confirm orientation [1 mark].\n"
        f"Travelling South on {street_2}, a left turn points towards the East.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="14",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Follow the sentence describing the intersection of Sisulu Street and Tambo Road.",
        tier_2=f"It says: 'Turn left onto {street_3} heading East'.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Subskill 15: Compass bearing estimation in degrees."""
    bearing_data = r.choice([
        ("North", "000° (or 360°)"),
        ("North-East", "045°"),
        ("East", "090°"),
        ("South-East", "135°"),
        ("South", "180°"),
        ("South-West", "225°"),
        ("West", "270°"),
        ("North-West", "315°"),
    ])
    cardinal, bearing_deg = bearing_data

    prompt = (
        f"In maritime and aviation navigation across South Africa, compass bearings are measured clockwise "
        f"from True North (000°).\n"
        f"What is the standard 3-figure degree bearing corresponding to travelling due **{cardinal}**?"
    )

    correct_ans = bearing_deg
    all_bearings = ["000° (or 360°)", "045°", "090°", "135°", "180°", "225°", "270°", "315°"]
    distractors = [b for b in all_bearings if b != bearing_deg][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Recall bearing conventions [1 mark].\n"
        f"Bearings start at North (000°) and increase clockwise through 360°.\n"
        f"Step 2: Match {cardinal} [1 mark].\n"
        f"Due {cardinal} is {bearing_deg}.\n"
        f"Step 3: Stated bearing [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="15",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Bearings start at North (0°) and turn clockwise: East is 90°, South is 180°, West is 270°.",
        tier_2=f"{cardinal} corresponds to {bearing_deg}.",
        tier_3=f"Bearing = {bearing_deg}.",
        r=r,
    )


def generate_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Subskill 16: Relative position description combining distance and direction."""
    name = r.choice(SA_NAMES)
    town_a = r.choice(["Kimberley", "Polokwane", "Nelspruit", "George"])
    town_b = r.choice(["Kuruman", "Makhado", "Barberton", "Knysna"])
    dist_km = r.choice([45, 60, 75, 90, 110])
    cardinal = r.choice(["North-West", "South-East", "North-East", "South-West"])

    prompt = (
        f"Refer to the regional map shown in the diagram. Town B ({town_b}) and Town A ({town_a}) are marked {_fmt(dist_km)} km apart.\n"
        f"Identify the compass direction of Town B relative to Town A."
    )

    correct_ans = f"Bearing {cardinal}"
    all_dirs = ["Bearing North-West", "Bearing South-East", "Bearing North-East", "Bearing South-West"]
    options, _ = _build_options(correct_ans, r, custom_options=all_dirs)

    explanation = (
        f"Step 1: Identify reference starting point [1 mark].\n"
        f"The observer stands at Town A (the origin).\n"
        f"Step 2: State distance and direction to Town B [1 mark].\n"
        f"Town B lies {_fmt(dist_km)} km in the direction {cardinal}.\n"
        f"Step 3: Stated sentence [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "bearing_map",
        "title": f"Regional Map: {town_a} to {town_b} ({dist_km} km)",
        "towns": [town_a, town_b],
        "bearing_deg": 45,
        "target_dir": cardinal,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="16",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Make sure the perspective starts from Town A looking towards Town B.",
        tier_2=f"Town B is {_fmt(dist_km)} km bearing {cardinal} from Town A.",
        tier_3=f"Correct description: {correct_ans}.",
        r=r,
    )


def generate_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Subskill 17: GPS coordinate format interpretation (Latitude & Longitude in South Africa)."""
    # South African coordinates: Latitude is South (22° S to 35° S), Longitude is East (16° E to 33° E)
    lat_deg = r.choice([26, 29, 33])
    lat_min = r.choice([12, 34, 55])
    long_deg = r.choice([18, 25, 28, 31])
    long_min = r.choice([15, 22, 48])

    coord_str = f"{lat_deg}° {lat_min}' S; {long_deg}° {long_min}' E"

    prompt = (
        f"A cellular emergency vehicle receives a GPS coordinate pin for an accident in South Africa: "
        f"**{coord_str}**.\n"
        f"In geography and navigation, what do the 'S' and 'E' represent in this South African coordinate?"
    )

    correct_ans = (
        f"{lat_deg}° {lat_min}' South of the Equator (Latitude) and {long_deg}° {long_min}' East of the Greenwich Meridian (Longitude)"
    )
    wrong_1 = f"{lat_deg}° {lat_min}' South of Johannesburg and {long_deg}° {long_min}' East of Pretoria"
    wrong_2 = f"{lat_deg}° {lat_min}' Seconds and {long_deg}° {long_min}' Elevation above sea level"
    wrong_3 = f"{lat_deg}° {lat_min}' Speed in km/h and {long_deg}° {long_min}' Engine capacity"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand geographic latitude and longitude conventions [1 mark].\n"
        f"Latitude measures angular distance North or South of the Equator.\n"
        f"Longitude measures angular distance East or West of the Prime (Greenwich) Meridian.\n"
        f"Step 2: Apply to South African geographic location [1 mark].\n"
        f"South Africa lies entirely in the Southern and Eastern Hemispheres.\n"
        f"Step 3: Stated interpretation [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "bearing_map",
        "title": f"GPS Coordinate Grid ({lat_deg}°S, {long_deg}°E)",
        "points": [{"name": "GPS Location", "lat": lat_deg, "long": long_deg}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="17",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="In GPS coordinates, S means South of the Equator (Latitude) and E means East of the Prime Meridian (Longitude).",
        tier_2="South Africa is located in the Southern and Eastern hemispheres.",
        tier_3=f"Interpretation: {correct_ans}.",
        r=r,
    )


def generate_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Subskill 18: Shortest grid walking distance along streets (Manhattan metric)."""
    name = r.choice(SA_NAMES)
    blocks_east = r.choice([3, 4, 5])
    blocks_south = r.choice([2, 3, 4])
    block_len_m = 120  # length of one street block in metres

    total_blocks = blocks_east + blocks_south
    total_dist_m = total_blocks * block_len_m

    prompt = (
        f"{name} walks from home to the community clinic in an urban township laid out in a grid pattern. "
        f"To reach the clinic, {name} must walk {_fmt(blocks_east)} blocks East and {_fmt(blocks_south)} blocks South. "
        f"Every street block has an identical length of {_fmt(block_len_m)} metres.\n"
        f"Assuming {name} only walks along the streets, calculate the shortest total walking distance in metres."
    )

    correct_ans = f"{_fmt(total_dist_m)} metres"
    wrong_1 = f"{_fmt(block_len_m * blocks_east)} metres"
    wrong_2 = f"{_fmt(total_dist_m + 200)} metres"
    wrong_3 = f"{_fmt(total_dist_m * 2)} metres"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate total blocks walked along the street grid [1 mark].\n"
        f"Total blocks = {blocks_east} East + {blocks_south} South = {total_blocks} blocks.\n"
        f"Step 2: Multiply by block length [1 mark].\n"
        f"Total distance = {total_blocks} × {_fmt(block_len_m)} m = {_fmt(total_dist_m)} metres.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="18",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the number of blocks in both directions, then multiply by the length of one block.",
        tier_2=f"Total blocks = {blocks_east} + {blocks_south} = {total_blocks}. Multiply by {block_len_m} m.",
        tier_3=f"Distance = {_fmt(total_dist_m)} metres.",
        r=r,
    )
