"""Cluster 3: Compass Directions & Navigational Bearings (Subskills 18 to 26).

Covers:
18. 8-point compass rose relative direction from Point A to Point B
19. 16-point intermediate compass directions (NNE, ESE, SSW, WNW)
20. True North compass bearings in degrees measured clockwise (0° to 360°)
21. Back-bearing (reciprocal return bearing) calculation (± 180°)
22. Alpha-numeric grid coordinate systems in municipal street guides (e.g. C4)
23. Sequential turn-by-turn cardinal route instructions
24. South African GPS coordinates: Southern Latitude (S) and Eastern Longitude (E)
25. Magnetic declination and True North vs Magnetic North orientation
26. Slope aspect and solar heating: North-facing vs South-facing mountain slopes
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    SA_TOWNS,
    _fmt,
    _build_question_payload,
)


def _gen_map_compass_eight_point_direction_from_a_to_b(r: random.Random) -> Dict[str, Any]:
    scenario = r.choice([
        ("School is situated due North of the Library", "South", "North"),
        ("Clinic is situated North-East of the Police Station", "South-West", "North-East"),
        ("Shopping Mall is situated due West of the Train Station", "East", "West"),
        ("Sports Stadium is situated South-East of the City Hall", "North-West", "South-East"),
        ("Post Office is situated North-West of the Bus Rank", "South-East", "North-West"),
    ])
    relation, from_target_to_origin, from_origin_to_target = scenario

    prompt = (
        f"Refer to the 8-point compass rose map diagram below.\n\n"
        f"Map observation: **{relation}**.\n\n"
        f"In which 8-point compass direction must a visitor travel **FROM the first landmark TO the second landmark**?"
    )
    ans = from_target_to_origin
    opts = [
        from_target_to_origin,
        from_origin_to_target,
        "North-East" if from_target_to_origin != "North-East" else "South-West",
        "North-West" if from_target_to_origin != "North-West" else "South-East",
    ]

    s1 = f"Identify the starting point ('FROM') and destination ('TO'). If Landmark A is {from_origin_to_target} of Landmark B, then travelling FROM A TO B requires moving in the opposite direction: {from_target_to_origin}."
    s2 = f"✓ [1 Mark: Method – Reversing relative compass vector]\nOpposite of {from_origin_to_target} is {from_target_to_origin}."
    s3 = f"✓ [1 Mark: Accuracy – Correct travel direction]\nDirection = {from_target_to_origin}."

    bearing_val = 45 if "North-East" in relation else (135 if "South-East" in relation else (315 if "North-West" in relation else 0))
    diagram_spec = {
        "diagram_role": "context",
        "kind": "compass_rose",
        "title": "8-Point Compass Rose Indicator",
        "bearing_deg": bearing_val,
        "destination": relation.split()[0],
        "compass": "8-point",
    }

    return _build_question_payload(
        "map_compass_eight_point_direction_from_a_to_b",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Pay close attention to 'FROM' which landmark and 'TO' which landmark.",
        tier_2_hint=f"If A is {from_origin_to_target} of B, then travelling from A to B goes {from_target_to_origin}.",
        tier_3_hint=f"Direction: {from_target_to_origin}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_compass_sixteen_point_intermediate_directions(r: random.Random) -> Dict[str, Any]:
    direction_data = r.choice([
        ("halfway between North (N) and North-East (NE)", "North-North-East (NNE)", "East-North-East (ENE)", "North-North-West (NNW)", "East-South-East (ESE)"),
        ("halfway between East (E) and North-East (NE)", "East-North-East (ENE)", "North-North-East (NNE)", "East-South-East (ESE)", "South-South-East (SSE)"),
        ("halfway between South (S) and South-West (SW)", "South-South-West (SSW)", "West-South-West (WSW)", "South-South-East (SSE)", "West-North-West (WNW)"),
        ("halfway between West (W) and North-West (NW)", "West-North-West (WNW)", "North-North-West (NNW)", "West-South-West (WSW)", "North-North-East (NNE)"),
    ])
    description, correct_dir, d1, d2, d3 = direction_data

    prompt = (
        f"Refer to the comprehensive 16-point compass rose diagram shown below used by navigators and pilots.\n\n"
        f"Which 16-point cardinal direction is located **{description}**?"
    )
    ans = correct_dir
    opts = [correct_dir, d1, d2, d3]

    s1 = f"Identify 16-point compass subdivision: the intermediate 3-letter point names place the primary cardinal point (N, S, E, W) first, followed by the secondary inter-cardinal direction (NE, NW, SE, SW)."
    s2 = f"✓ [1 Mark: Method – Identifying 16-point compass quadrant midpoint]\n{description} corresponds to {correct_dir}."
    s3 = f"✓ [1 Mark: Accuracy – Correct 16-point notation]\nDirection = {correct_dir}."

    b_deg = 22.5 if "NNE" in correct_dir else (67.5 if "ENE" in correct_dir else (202.5 if "SSW" in correct_dir else 292.5))
    diagram_spec = {
        "diagram_role": "context",
        "kind": "compass_rose",
        "title": "16-Point Compass Rose Indicator",
        "bearing_deg": b_deg,
        "destination": correct_dir,
        "compass": "16-point",
    }

    return _build_question_payload(
        "map_compass_sixteen_point_intermediate_directions",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="In 16-point compass names, the nearest primary cardinal direction (N, S, E, or W) comes first.",
        tier_2_hint=f"Identify the direction located {description}.",
        tier_3_hint=f"Direction = {correct_dir}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_compass_bearing_degrees_true_north(r: random.Random) -> Dict[str, Any]:
    cardinal_bearing = r.choice([
        ("North-East (NE)", 45, "halfway between North (0°) and East (90°)"),
        ("East (E)", 90, "one quarter turn clockwise from North (0°)"),
        ("South-East (SE)", 135, "halfway between East (90°) and South (180°)"),
        ("South (S)", 180, "one half turn clockwise from North (0°)"),
        ("South-West (SW)", 225, "halfway between South (180°) and West (270°)"),
        ("West (W)", 270, "three-quarters turn clockwise from North (0°)"),
        ("North-West (NW)", 315, "halfway between West (270°) and North (360°)"),
    ])
    card_name, deg, explanation = cardinal_bearing

    prompt = (
        f"Refer to the compass bearing diagram below showing clockwise angles from True North (000°).\n\n"
        f"What is the exact bearing (in degrees) for a direction heading directly **{card_name}**?"
    )
    ans = f"{deg:03d}° (or {deg}°)"

    s1 = f"Recall bearing conventions: True North = 000°, East = 090°, South = 180°, West = 270°. Inter-cardinal points bisect quadrants at intervals of 45°."
    s2 = f"✓ [1 Mark: Method – Clockwise rotation from True North]\n{card_name} is {explanation} = {deg}°."
    s3 = f"✓ [1 Mark: Accuracy – Three-digit bearing angle]\nBearing = {deg:03d}°."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "compass_rose",
        "title": f"True North Bearing: {card_name}",
        "bearing_deg": deg,
        "destination": card_name,
        "compass": "True North 360°",
    }

    return _build_question_payload(
        "map_compass_bearing_degrees_true_north",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Bearings start at North (0°) and measure clockwise.",
        tier_2_hint=f"North = 0°, East = 90°, South = 180°, West = 270°. {card_name} is {explanation}.",
        tier_3_hint=f"Bearing = {deg:03d}°.",
        diagram_spec=diagram_spec,
    )


def _gen_map_compass_back_bearing_reciprocal(r: random.Random) -> Dict[str, Any]:
    forward_bearing = r.choice([35, 60, 85, 120, 145, 210, 240, 290, 315])
    if forward_bearing < 180:
        back_bearing = forward_bearing + 180
        rule_desc = "Since forward bearing is less than 180°, add 180°"
    else:
        back_bearing = forward_bearing - 180
        rule_desc = "Since forward bearing is 180° or greater, subtract 180°"

    prompt = (
        f"Refer to the navigational compass diagram below showing a forward bearing of **{forward_bearing:03d}°** from Camp A to Camp B.\n\n"
        f"At sunset, the hiker needs to turn around and walk directly back along the same path FROM Camp B TO Camp A.\n\n"
        f"Back-Bearing Rule:\n"
        f"• If Forward Bearing < 180°: Back Bearing = Forward Bearing + 180°\n"
        f"• If Forward Bearing ≥ 180°: Back Bearing = Forward Bearing − 180°\n\n"
        f"Calculate the **back-bearing (return bearing)** in degrees."
    )
    ans = f"{back_bearing:03d}°"

    s1 = f"Apply the reciprocal 180° rule: {rule_desc}."
    s2 = f"✓ [1 Mark: Method – Applying reciprocal 180° formula]\nBack bearing = {forward_bearing}° {'+' if forward_bearing < 180 else '−'} 180°."
    s3 = f"✓ [1 Mark: Accuracy – Calculated back-bearing in degrees]\nReturn bearing = {back_bearing:03d}°."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "compass_rose",
        "title": f"Trail Forward Bearing ({forward_bearing:03d}°)",
        "bearing_deg": forward_bearing,
        "destination": "Camp B",
        "compass": "Reciprocal",
    }

    return _build_question_payload(
        "map_compass_back_bearing_reciprocal",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Is {forward_bearing}° greater than or less than 180°?",
        tier_2_hint=f"{rule_desc}: {forward_bearing} {'+' if forward_bearing < 180 else '−'} 180.",
        tier_3_hint=f"Back bearing = {back_bearing:03d}°.",
        diagram_spec=diagram_spec,
    )


def _gen_map_grid_alphanumeric_street_guide_coordinates(r: random.Random) -> Dict[str, Any]:
    col_letter = r.choice(["B", "C", "D", "E"])
    row_num = r.choice([2, 3, 4, 5])
    facility = r.choice(["Public Library", "Police Station", "Post Office", "Fire Station", "Municipal Clinic"])

    prompt = (
        f"Study the excerpt of an index in a Johannesburg municipal street guide map book and grid below:\n\n"
        f"| Landmark Facility | Grid Reference | Page Number |\n"
        f"| :--- | :---: | :---: |\n"
        f"| Central Fire Station | A3 | Page 42 |\n"
        f"| {facility} | **{col_letter}{row_num}** | Page 42 |\n"
        f"| Magistrates Court | D1 | Page 42 |\n"
        f"| Railway Station | B5 | Page 42 |\n\n"
        f"Explain step-by-step how a visitor uses the grid reference **'{col_letter}{row_num}'** on Page 42 "
        f"to find the exact location of the {facility} on the map grid."
    )
    ans = f"Locate Column '{col_letter}' along the horizontal top/bottom margin, locate Row '{row_num}' along the vertical side margin, and find the square where Column {col_letter} and Row {row_num} intersect."
    opts = [
        f"Locate Column '{col_letter}' along the horizontal top/bottom margin, locate Row '{row_num}' along the vertical side margin, and find the square where Column {col_letter} and Row {row_num} intersect.",
        f"Multiply letter {col_letter} by number {row_num} using a scientific calculator.",
        f"Turn to page {row_num} and measure {col_letter} centimetres from the corner.",
        "Add 15% VAT to find the street address.",
    ]

    s1 = f"Explain the Cartesian-style row-and-column intersection convention used in municipal street atlas alpha-numeric grid systems."
    s2 = f"✓ [1 Mark: Method – Identifying column-row intersection protocol]\nLetters represent vertical column strips; numbers represent horizontal row bands. The target landmark lies in their intersecting grid block."
    s3 = f"✓ [1 Mark: Accuracy – Correct procedural explanation]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "grid_map",
        "title": "Municipal Street Guide Grid (Page 42)",
        "columns": ["A", "B", "C", "D", "E"],
        "rows": ["1", "2", "3", "4", "5"],
        "landmarks": [
            {"name": facility, "cell": f"{col_letter}{row_num}"},
            {"name": "Central Fire Station", "cell": "A3"},
            {"name": "Magistrates Court", "cell": "D1"},
            {"name": "Railway Station", "cell": "B5"},
        ],
    }

    return _build_question_payload(
        "map_grid_alphanumeric_street_guide_coordinates",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="How do you read a grid coordinate like B3 on a map or chess board?",
        tier_2_hint=f"Find column {col_letter} on the horizontal margin and row {row_num} on the vertical margin.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_navigational_turn_by_turn_directions(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    heading = r.choice([45, 90, 135, 180, 225, 270, 315])
    dest = r.choice(["Polokwane", "Rustenburg", "Bloemfontein", "Nelspruit", "Kimberley"])

    prompt = (
        f"{name} is navigating a vehicle towards {dest} according to a route compass heading of {heading}°.\n\n"
        f"Refer to the navigational compass below.\n\n"
        f"If {name} is travelling North and turns 90° clockwise at a roundabout, in which cardinal compass direction is {name} now heading?"
    )
    ans = "East (E)"
    opts = ["East (E)", "West (W)", "South (S)", "North-East (NE)"]

    s1 = f"Clockwise 90° turn from North (0° / 360°) leads to East (90°)."
    s2 = f"✓ [1 Mark: Method – Compass rose quadrant rotation]\n0° (North) + 90° clockwise = 90° = East."
    s3 = f"✓ [1 Mark: Accuracy – Final cardinal direction]\nDirection: East (E)."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "compass_rose",
        "title": f"Navigational Heading ({name}: {heading}° to {dest})",
        "bearing_deg": heading,
    }

    return _build_question_payload(
        "map_navigational_turn_by_turn_directions",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="North is up (0°). Turning 90° clockwise points right.",
        tier_2_hint="90° clockwise from North is East.",
        tier_3_hint="New heading is East (E).",
        diagram_spec=diagram_spec,
    )

    s1 = f"Trace the sequential directional changes: Start heading North. Turn 90° right from North → now heading East. Turn 90° left from East → now heading North again."
    s2 = f"✓ [1 Mark: Method – Stepwise cardinal turn tracking]\nStep 1: North\nStep 2: 90° Right = East\nStep 3: 90° Left = North."
    s3 = f"✓ [1 Mark: Accuracy – Final cardinal heading]\nFinal direction: North."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "grid_map",
        "title": "Central Pretoria Navigation Grid",
        "stops": [
            {"name": "Church Square", "step": "Start (Facing North)"},
            {"name": "Madiba St", "step": "Turn 90° Right (East)"},
            {"name": "Thabo Sehume", "step": "Turn 90° Left (North)"},
        ],
        "landmarks": [
            {"name": "Church Square", "cell": "C3"},
            {"name": "Madiba St Corner", "cell": "C1"},
            {"name": "Destination", "cell": "E1"},
        ],
    }

    return _build_question_payload(
        "map_navigational_turn_by_turn_directions",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Turning right from North heads East. What direction do you face if you turn left from East?",
        tier_2_hint="A left turn from East turns you back towards North.",
        tier_3_hint="Final heading is North.",
        diagram_spec=diagram_spec,
    )


def _gen_map_gps_latitude_longitude_south_african_hemisphere(r: random.Random) -> Dict[str, Any]:
    town = r.choice([
        ("Johannesburg", "26° 12' S, 28° 02' E"),
        ("Cape Town", "33° 55' S, 18° 25' E"),
        ("Durban", "29° 51' S, 31° 01' E"),
        ("Bloemfontein", "29° 06' S, 26° 13' E"),
    ])
    town_name, coord = town

    prompt = (
        f"Refer to the GPS coordinate display below.\n\n"
        f"A GPS device displays the geographic coordinates for {town_name} as:\n"
        f"**{coord}**\n\n"
        f"1. What does the letter **'S'** indicate about South Africa's global position?\n"
        f"2. What does the letter **'E'** indicate about South Africa's global position?"
    )
    ans = "'S' means Southern Hemisphere (South of the Equator, 0°); 'E' means Eastern Hemisphere (East of the Greenwich Prime Meridian, 0°)"
    opts = [
        "'S' means Southern Hemisphere (South of the Equator, 0°); 'E' means Eastern Hemisphere (East of the Greenwich Prime Meridian, 0°)",
        "'S' means Standard Time; 'E' means Elevation in metres",
        "'S' means Summer zone; 'E' means Equator line",
        "'S' means Sea level; 'E' means Eskom electricity grid",
    ]

    s1 = f"Understand geographic coordinate conventions: Latitude measures angular distance North or South of the Equator. Longitude measures angular distance East or West of the Prime Meridian."
    s2 = f"✓ [1 Mark: Method – Defining Latitude and Longitude hemispheres for South Africa]\nAll of South Africa lies South of the Equator (S latitude) and East of the Prime Meridian (E longitude)."
    s3 = f"✓ [1 Mark: Accuracy – Correct hemispheric definitions]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "grid_map",
        "title": f"GPS Coordinate Grid: {town_name}",
        "landmarks": [{"name": town_name, "cell": coord}],
        "columns": ["18° E", "26° E", "28° E", "31° E"],
        "rows": ["26° S", "29° S", "33° S"],
    }

    return _build_question_payload(
        "map_gps_latitude_longitude_south_african_hemisphere",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What reference line runs horizontally around the middle of the Earth? The Equator.",
        tier_2_hint="S means South of the Equator; E means East of the Greenwich Meridian.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_magnetic_declination_true_vs_magnetic_north(r: random.Random) -> Dict[str, Any]:
    decl_deg = r.choice([14, 16, 18, 20, 22])
    prompt = (
        f"Refer to the magnetic declination diagram below from the lower margin of a South African 1 : 50 000 topographic sheet.\n\n"
        f"The technical diagram illustrates True North (TN) and Magnetic North (MN) with a declination angle of {decl_deg}° West.\n\n"
        f"Why is Magnetic North NOT in the exact same direction as True North?"
    )
    ans = "True North points to the geographic North Pole (the Earth's axis of rotation), whereas Magnetic North points to the Earth's shifting magnetic pole where a compass needle naturally aligns."
    opts = [
        "True North points to the geographic North Pole (the Earth's axis of rotation), whereas Magnetic North points to the Earth's shifting magnetic pole where a compass needle naturally aligns.",
        "Magnetic North is an imaginary line invented for maritime pirate ships.",
        "True North is only used during daylight hours.",
        "Magnetic North points towards the nearest cellphone cellular tower.",
    ]

    s1 = f"Understand the distinction between Geographic True North (Earth's spin axis) and Geomagnetic North (fluid outer core dynamo alignment)."
    s2 = f"✓ [1 Mark: Method – Explaining geographic rotational axis vs magnetic pole]\nTrue North is fixed at 90°N; Magnetic North wanders due to molten iron movement in Earth's core."
    s3 = f"✓ [1 Mark: Accuracy – Correct scientific reason]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "compass_rose",
        "title": f"Magnetic Declination Angle ({decl_deg}° W)",
        "bearing_deg": decl_deg,
    }

    return _build_question_payload(
        "map_magnetic_declination_true_vs_magnetic_north",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Does a compass needle point to the geographic North Pole or to Earth's magnetic pole?",
        tier_2_hint="True North is the rotational axis, while Magnetic North is where magnetic compass needles point.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Differentiate between geographic True North (axis of rotational spin) and geomagnetic Magnetic North (driven by molten iron currents in the Earth's core)."
    s2 = f"✓ [1 Mark: Method – Explaining geographic rotational axis vs geomagnetic alignment]\nMagnetic compasses align with magnetic field lines, which deviate from geographic True North by the declination angle."
    s3 = f"✓ [1 Mark: Accuracy – Correct scientific distinction]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "compass_rose",
        "title": "True North vs Magnetic North Declination",
        "bearing_deg": 24,
        "destination": "Magnetic North",
        "compass": "Magnetic Declination (24° W of TN)",
    }

    return _build_question_payload(
        "map_magnetic_declination_true_vs_magnetic_north",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Does a compass needle point to the geographic pole or the magnetic pole?",
        tier_2_hint="True North is the geographic rotational pole; Magnetic North is where magnetic compass needles point.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_cardinal_elevation_sun_exposure_aspect(r: random.Random) -> Dict[str, Any]:
    farm_name = r.choice(["Welgevonden", "Baviaanskrans", "Tierkloof", "Elandsfontein"])
    crop = r.choice(["wine grapes", "citrus orchards", "macadamia nuts", "avocados"])
    aspect_bearing = r.choice([0, 90, 180, 270])
    prompt = (
        f"An agricultural farmer at {farm_name} is selecting a hillside slope to establish high-value {crop}.\n\n"
        f"Refer to the slope aspect elevation compass below ({farm_name}: {aspect_bearing}°).\n\n"
        f"In South Africa (Southern Hemisphere), which slope aspect (compass direction of hill face) receives the maximum amount of direct sunlight and solar warmth during the winter months?"
    )
    ans = "North-facing slopes — because South Africa is in the Southern Hemisphere, the midday sun arcs across the northern sky year-round."
    opts = [
        "North-facing slopes — because South Africa is in the Southern Hemisphere, the midday sun arcs across the northern sky year-round.",
        "South-facing slopes — because the sun shines from Antarctica.",
        "East-facing slopes only, because the sun never sets in winter.",
        "All hill slopes receive identical sunlight regardless of orientation.",
    ]

    s1 = f"Apply Southern Hemisphere solar geometry: The sun is positioned in the northern sky, so North-facing slopes capture low-angle winter solar radiation."
    s2 = f"✓ [1 Mark: Method – Identifying Southern Hemisphere solar trajectory]\nSun arcs from East to West via the North in the Southern Hemisphere."
    s3 = f"✓ [1 Mark: Accuracy – North-facing slope selection and justification]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "elevation_compass",
        "title": f"Slope Aspect ({farm_name}: {aspect_bearing}°)",
        "bearing_deg": aspect_bearing,
    }

    return _build_question_payload(
        "map_cardinal_elevation_sun_exposure_aspect",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Where is the sun at midday in the Southern Hemisphere (South Africa)?",
        tier_2_hint="The sun is in the North, so North-facing slopes get the most warmth.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Apply Southern Hemisphere solar geometry to topographic slope aspect: North-facing slopes intercept direct insolation at high angles of incidence, while South-facing slopes remain in the mountain's shade."
    s2 = f"✓ [1 Mark: Method – Southern Hemisphere solar aspect rationale]\nSolar declination in winter places the midday sun to the north of South Africa. North-facing topography receives maximum insolation."
    s3 = f"✓ [1 Mark: Accuracy – Slope A selection and thermal motivation]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "elevation_compass",
        "title": "Drakensberg Mountain Ridge Solar Aspect",
        "north_facing_wall": "Slope A (North-facing)",
        "bearing_deg": 0,
        "compass": "Midday Sun in Northern Sky",
    }

    return _build_question_payload(
        "map_cardinal_elevation_sun_exposure_aspect",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Where is the sun in the sky during midday in winter in South Africa?",
        tier_2_hint="The sun is to the North, so North-facing slopes catch the warm winter sun.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )
