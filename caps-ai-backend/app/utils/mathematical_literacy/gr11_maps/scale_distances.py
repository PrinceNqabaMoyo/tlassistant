"""Subskills 1 to 9: Map Scale Conversions, Real Distances & Bar Scales for Grade 11 Mathematical Literacy."""
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


def generate_subskill_1(r: random.Random) -> Dict[str, Any]:
    """Subskill 1: 1:50 000 topographic scale conversion: map cm to real km."""
    name = r.choice(SA_NAMES)
    map_cm = r.choice([4.2, 5.0, 6.4, 7.8, 8.5, 9.2, 10.6, 12.0])
    # 1:50 000 -> 1 cm = 50 000 cm = 500 m = 0.5 km
    real_km = round(map_cm * 0.5, 2)

    prompt = (
        f"On a standard South African 1 : 50 000 topographic map, the straight-line distance between two "
        f"trigonometrical beacons measures {_fmt(map_cm)} cm.\n"
        f"Calculate the actual real-world distance between the two beacons in kilometres (km)."
    )

    correct_ans = f"{_fmt(real_km)} km"
    wrong_1 = f"{_fmt(real_km * 10)} km"
    wrong_2 = f"{_fmt(real_km * 2)} km"
    wrong_3 = f"{_fmt(real_km * 0.1)} km"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand scale 1 : 50 000 [1 mark].\n"
        f"1 cm on the map represents 50 000 cm in reality.\n"
        f"50 000 cm = 500 m = 0,5 km (each 1 cm on the map = 0,5 km).\n"
        f"Step 2: Multiply map distance by scale factor in km [1 mark].\n"
        f"Real distance = {_fmt(map_cm)} cm × 0,5 km/cm = {_fmt(real_km)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="1",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="On a 1:50 000 map, 1 cm represents 0,5 km (half a kilometre).",
        tier_2=f"Multiply {_fmt(map_cm)} cm by 0,5 km.",
        tier_3=f"Real distance = {_fmt(real_km)} km.",
        r=r,
    )


def generate_subskill_2(r: random.Random) -> Dict[str, Any]:
    """Subskill 2: 1:10 000 town/street map scale conversion: map cm to real metres/km."""
    name = r.choice(SA_NAMES)
    town = r.choice(["Soweto", "Stellenbosch", "Mthatha", "Rustenburg", "George"])
    map_cm = r.choice([3.5, 4.0, 5.2, 6.5, 7.0, 8.4])
    # 1:10 000 -> 1 cm = 10 000 cm = 100 m = 0.1 km
    real_m = round(map_cm * 100, 1)
    real_km = round(map_cm * 0.1, 2)

    prompt = (
        f"On a 1 : 10 000 street guide map of {town}, the distance between a high school and the local library "
        f"measures {_fmt(map_cm)} cm.\n"
        f"Calculate the actual distance between them in metres (m) and in kilometres (km)."
    )

    correct_ans = f"{_fmt(real_m, 0)} m (or {_fmt(real_km)} km)"
    wrong_1 = f"{_fmt(real_m * 10, 0)} m (or {_fmt(real_km * 10)} km)"
    wrong_2 = f"{_fmt(real_m * 0.1, 1)} m (or {_fmt(real_km * 0.1)} km)"
    wrong_3 = f"{_fmt(real_m * 2, 0)} m (or {_fmt(real_km * 2)} km)"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand scale 1 : 10 000 [1 mark].\n"
        f"1 cm on map = 10 000 cm in reality = 100 metres = 0,1 km.\n"
        f"Step 2: Multiply map measurement by 100 m [1 mark].\n"
        f"Real distance in metres = {_fmt(map_cm)} cm × 100 m/cm = {_fmt(real_m, 0)} m.\n"
        f"In kilometres = {_fmt(real_m, 0)} ÷ 1 000 = {_fmt(real_km)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="2",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="On a 1:10 000 map, 1 cm represents 100 metres (0,1 km).",
        tier_2=f"Multiply {_fmt(map_cm)} cm by 100 to get metres: {_fmt(real_m, 0)} m.",
        tier_3=f"Distance = {_fmt(real_m, 0)} m ({_fmt(real_km)} km).",
        r=r,
    )


def generate_subskill_3(r: random.Random) -> Dict[str, Any]:
    """Subskill 3: 1:500 000 regional road map scale: map cm to real km."""
    name = r.choice(SA_NAMES)
    province = r.choice(["Western Cape", "KwaZulu-Natal", "Mpumalanga", "Free State", "Eastern Cape"])
    map_cm = r.choice([4.6, 5.2, 6.0, 7.4, 8.5, 11.2, 14.0])
    # 1:500 000 -> 1 cm = 500 000 cm = 5 000 m = 5 km
    real_km = round(map_cm * 5.0, 1)

    prompt = (
        f"Refer to the regional map shown in the diagram for {province} with scale 1 : 500 000. "
        f"Two rural service centres are {_fmt(map_cm)} cm apart on the paper.\n"
        f"Calculate the actual straight-line distance between the two centres in kilometres."
    )

    correct_ans = f"{_fmt(real_km, 1)} km"
    wrong_1 = f"{_fmt(real_km * 10, 1)} km"
    wrong_2 = f"{_fmt(real_km * 0.5, 1)} km"
    wrong_3 = f"{_fmt(real_km * 2, 1)} km"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand scale 1 : 500 000 [1 mark].\n"
        f"1 cm on map = 500 000 cm = 5 000 m = 5 km in reality.\n"
        f"Step 2: Multiply map distance by 5 km/cm [1 mark].\n"
        f"Real distance = {_fmt(map_cm)} cm × 5 km/cm = {_fmt(real_km, 1)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Regional Road Map Bar Scale ({province}, 1:500 000)",
        "scale": "1 : 500 000",
        "segment_value_km": 5,
        "total_km": real_km,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="3",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="On a 1:500 000 map, 1 cm represents exactly 5 kilometres.",
        tier_2=f"Multiply {_fmt(map_cm)} cm by 5 km.",
        tier_3=f"Real distance = {_fmt(real_km, 1)} km.",
        r=r,
    )


def generate_subskill_4(r: random.Random) -> Dict[str, Any]:
    """Subskill 4: 1:2 500 000 national map scale: map cm to real km."""
    city_pair = r.choice([
        ("Johannesburg and Durban", 22.8),
        ("Cape Town and Beaufort West", 18.0),
        ("Port Elizabeth and East London", 11.2),
        ("Bloemfontein and Kimberley", 6.8),
    ])
    cities, map_cm = city_pair
    # 1:2 500 000 -> 1 cm = 2 500 000 cm = 25 000 m = 25 km
    real_km = round(map_cm * 25.0, 1)

    prompt = (
        f"On a national map of South Africa with a scale of 1 : 2 500 000, the straight-line distance "
        f"between {cities} measures {_fmt(map_cm)} cm.\n"
        f"Calculate the actual real-world straight-line distance in kilometres."
    )

    correct_ans = f"{_fmt(real_km, 1)} km"
    wrong_1 = f"{_fmt(real_km * 10, 1)} km"
    wrong_2 = f"{_fmt(real_km * 0.1, 1)} km"
    wrong_3 = f"{_fmt(real_km * 2, 1)} km"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand scale 1 : 2 500 000 [1 mark].\n"
        f"1 cm on the map represents 2 500 000 cm in reality.\n"
        f"2 500 000 cm = 25 000 m = 25 km (1 cm on map = 25 km).\n"
        f"Step 2: Multiply map distance by 25 km/cm [1 mark].\n"
        f"Real distance = {_fmt(map_cm)} cm × 25 km/cm = {_fmt(real_km, 1)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="4",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="On a 1:2 500 000 map, 1 cm represents 25 kilometres.",
        tier_2=f"Multiply {_fmt(map_cm)} cm by 25 km.",
        tier_3=f"Distance = {_fmt(real_km, 1)} km.",
        r=r,
    )


def generate_subskill_5(r: random.Random) -> Dict[str, Any]:
    """Subskill 5: Reverse scale calculation: real distance to map length in cm."""
    name = r.choice(SA_NAMES)
    scale = r.choice([50000, 100000, 250000])
    # Real km
    real_km = r.choice([15.0, 20.0, 25.0, 30.0, 45.0, 50.0])

    # map_cm = real_km * 100 000 / scale
    map_cm = round((real_km * 100000) / scale, 1)

    prompt = (
        f"A map has a scale of 1 : {_fmt(scale)}. Two nature reserves are located an actual distance of "
        f"{_fmt(real_km)} km apart in reality.\n"
        f"What distance (in centimetres) will separate these two reserves on the map?"
    )

    correct_ans = f"{_fmt(map_cm, 1)} cm"
    wrong_1 = f"{_fmt(map_cm * 10, 1)} cm"
    wrong_2 = f"{_fmt(map_cm * 0.1, 1)} cm"
    wrong_3 = f"{_fmt(real_km)} cm"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Convert real distance from kilometres to centimetres [1 mark].\n"
        f"{_fmt(real_km)} km = {_fmt(real_km)} × 100 000 cm = {_fmt(real_km * 100000)} cm.\n"
        f"Step 2: Divide by the scale denominator ({_fmt(scale)}) [1 mark].\n"
        f"Map distance = {_fmt(real_km * 100000)} cm ÷ {_fmt(scale)} = {_fmt(map_cm, 1)} cm.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Topographic Map Scale (1:{scale}, Distance {real_km} km)",
        "scale": f"1 : {scale}",
        "segment_value_km": scale / 100000,
        "total_km": real_km,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="5",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Convert km to cm (multiply by 100 000) then divide by the scale factor.",
        tier_2=f"{_fmt(real_km)} km = {_fmt(real_km * 100000)} cm. Divide by {_fmt(scale)}.",
        tier_3=f"Map distance = {_fmt(map_cm, 1)} cm.",
        r=r,
    )


def generate_subskill_6(r: random.Random) -> Dict[str, Any]:
    """Subskill 6: Measure straight-line distance using a graphic bar scale with diagram_spec."""
    name = r.choice(SA_NAMES)
    bar_seg_cm = 2.0
    bar_seg_km = r.choice([5.0, 10.0, 20.0])
    measured_cm = r.choice([6.0, 7.0, 8.0, 9.0, 10.0])

    real_km = round((measured_cm / bar_seg_cm) * bar_seg_km, 1)

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "bar_scale",
        "title": "Road Map Bar Scale",
        "segment_length_cm": bar_seg_cm,
        "segment_value_km": bar_seg_km,
        "measured_map_distance_cm": measured_cm,
    }

    prompt = (
        f"A map includes a graphic bar scale where a {_fmt(bar_seg_cm)} cm bar segment represents "
        f"{_fmt(bar_seg_km)} km in reality. "
        f"{name} measures the distance between two towns on the map with a ruler and gets {_fmt(measured_cm)} cm.\n"
        f"Using the bar scale, calculate the actual straight-line distance between the towns in kilometres."
    )

    correct_ans = f"{_fmt(real_km, 1)} km"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Calculate the value represented by 1 cm on the map [1 mark].\n"
        f"1 cm = {_fmt(bar_seg_km)} km ÷ {_fmt(bar_seg_cm)} cm = {_fmt(bar_seg_km / bar_seg_cm, 1)} km/cm.\n"
        f"Step 2: Multiply by measured map length [1 mark].\n"
        f"Real distance = {_fmt(measured_cm)} cm × {_fmt(bar_seg_km / bar_seg_cm, 1)} km/cm = {_fmt(real_km, 1)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="6",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine how many km 1 cm represents, then multiply by the measured distance in cm.",
        tier_2=f"1 cm represents {_fmt(bar_seg_km / bar_seg_cm, 1)} km. Multiply by {_fmt(measured_cm)} cm.",
        tier_3=f"Distance = {_fmt(real_km, 1)} km.",
        r=r,
        diagram_spec=diagram_spec,
    )


def generate_subskill_7(r: random.Random) -> Dict[str, Any]:
    """Subskill 7: Determine the number scale ratio 1 : n from a known benchmark distance."""
    map_cm = r.choice([4.0, 5.0, 8.0, 10.0])
    real_km = r.choice([20.0, 25.0, 40.0, 50.0])

    # scale_n = real_km * 100 000 / map_cm
    scale_n = int((real_km * 100000) / map_cm)

    prompt = (
        f"A surveyor compares a map distance to a known highway milestone. "
        f"On the map, the distance between two toll gates is exactly {_fmt(map_cm)} cm, "
        f"while road signage confirms the actual distance between them is {_fmt(real_km)} km.\n"
        f"Determine the number scale (in the form 1 : n) of this map."
    )

    correct_ans = f"1 : {_fmt(scale_n)}"
    wrong_1 = f"1 : {_fmt(scale_n * 10)}"
    wrong_2 = f"1 : {_fmt(scale_n // 10)}"
    wrong_3 = f"1 : {_fmt(scale_n * 2)}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Convert both measurements to the exact same unit (centimetres) [1 mark].\n"
        f"Real distance = {_fmt(real_km)} km × 100 000 cm/km = {_fmt(real_km * 100000)} cm.\n"
        f"Step 2: Divide both sides of the ratio by the map measurement ({_fmt(map_cm)} cm) [1 mark].\n"
        f"Scale = {_fmt(map_cm)} : {_fmt(real_km * 100000)} = 1 : ({_fmt(real_km * 100000)} ÷ {_fmt(map_cm)}) = 1 : {_fmt(scale_n)}.\n"
        f"Step 3: Stated scale ratio [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Surveyor Benchmark Scale (1:{scale_n}, Real {real_km} km)",
        "scale": f"1 : {scale_n}",
        "segment_value_km": real_km / 5,
        "total_km": real_km,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="7",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Convert the real distance in km to cm (multiply by 100 000) then divide by the map cm.",
        tier_2=f"{_fmt(real_km)} km = {_fmt(real_km * 100000)} cm. Divide by {_fmt(map_cm)}.",
        tier_3=f"Scale = 1 : {_fmt(scale_n)}.",
        r=r,
    )


def generate_subskill_8(r: random.Random) -> Dict[str, Any]:
    """Subskill 8: As-the-crow-flies vs actual winding road distance comparison."""
    name = r.choice(SA_NAMES)
    straight_km = r.choice([60, 80, 100, 120])
    road_factor = r.choice([1.25, 1.30, 1.35])
    road_km = round(straight_km * road_factor, 1)

    prompt = (
        f"{name} measures the straight-line ('as-the-crow-flies') distance between two mountain towns "
        f"on a map as {_fmt(straight_km)} km. "
        f"Due to mountain passes and river detours, the actual drivable road distance is {int((road_factor - 1)*100)}% "
        f"longer than the straight-line distance.\n"
        f"Calculate the actual road distance in kilometres that a driver will travel."
    )

    correct_ans = f"{_fmt(road_km, 1)} km"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Identify the road detour factor [1 mark].\n"
        f"Road distance is {int((road_factor - 1)*100)}% longer: multiplier = {road_factor}.\n"
        f"Step 2: Multiply straight-line distance by the factor [1 mark].\n"
        f"Actual road distance = {_fmt(straight_km)} km × {road_factor} = {_fmt(road_km, 1)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="8",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the straight-line distance by the given percentage increase factor.",
        tier_2=f"{_fmt(straight_km)} km × {road_factor} = {_fmt(road_km, 1)} km.",
        tier_3=f"Actual road distance = {_fmt(road_km, 1)} km.",
        r=r,
    )


def generate_subskill_9(r: random.Random) -> Dict[str, Any]:
    """Subskill 9: Map resizing and zoom implications on bar scale vs number scale."""
    prompt = (
        f"A tourist views a street map on a smartphone screen and pinches to zoom in, enlarging the visual display "
        f"by 200%. The original map had both a printed ratio '1:25 000' and a graphic bar scale.\n"
        f"Which statement correctly explains why the graphic bar scale is superior to the number scale on resized digital displays?"
    )

    correct_ans = (
        "The bar scale enlarges in exact proportion with the map features on screen and remains 100% accurate, whereas the printed text '1:25 000' becomes completely false and misleading"
    )
    wrong_1 = "The printed number scale automatically recalculates its numbers on the screen while the bar scale disappears"
    wrong_2 = "Both the bar scale and the number scale become completely inaccurate whenever any map is zoomed"
    wrong_3 = "Zooming in on a digital map has zero effect on either scale because smartphone screens are calibrated to satellite orbits"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand graphical resizing behaviour [1 mark].\n"
        f"When an image is zoomed, graphic elements (including the graphic bar scale) scale at the exact same rate as the terrain.\n"
        f"Step 2: Contrast with static numerical text [1 mark].\n"
        f"The text string '1:25 000' remains unchanged text, so 1 cm measured on the zoomed screen no longer equals 25 000 cm in reality.\n"
        f"Step 3: Stated conclusion [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Mobile Street Map Zoom Scale (Zoom {r.choice([150, 200, 250, 300])}%)",
        "scale": "1 : 25 000",
        "segment_value_km": 0.25,
        "total_km": 1.0,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="9",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="A graphic bar scale is an image that grows or shrinks with the map, keeping the same scale.",
        tier_2="Static text ratios like 1:25 000 become invalid when the image is zoomed or resized.",
        tier_3=f"Correct explanation: {correct_ans}.",
        r=r,
    )
