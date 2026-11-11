"""Cluster 1: Number Scales & Real Distance Calculations (Subskills 1 to 9).

Covers:
1. Metric unit conversion foundation (1 km = 1 000 m = 100 000 cm)
2. Real-world distance in kilometres from map measurement and number scale (1 : x)
3. Real-world distance in metres from site plan measurement (1 : 200, 1 : 500)
4. Inverse calculation: drawing distance on map from real kilometres
5. Inverse calculation: drawing length on site plan from real metres
6. Determining number scale ratio (1 : x) from map and real measurements
7. Large-scale vs small-scale map comparison (detail vs geographic extent)
8. Official South African 1 : 50 000 topographic map series conversion
9. Straight-line ('as the crow flies') vs winding route distance comparison
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


def _gen_map_scale_unit_conversion_constants(r: random.Random) -> Dict[str, Any]:
    km_val = r.choice([2.5, 4.0, 7.2, 12.0, 15.5])
    cm_val = int(km_val * 100_000)

    prompt = (
        f"Study the metric conversion bar scale shown below.\n\n"
        f"Conversion facts:\n"
        f"• 1 kilometre (km) = 1 000 metres (m)\n"
        f"• 1 metre (m) = 100 centimetres (cm)\n"
        f"• Therefore: 1 km = 1 000 × 100 = 100 000 cm\n\n"
        f"Convert **{_fmt(km_val)} km** from the bar scale into centimetres (cm)."
    )
    ans = f"{_fmt(cm_val)} cm"

    s1 = f"Multiply the distance in kilometres ({_fmt(km_val)} km) by 100 000 (since 1 km = 100 000 cm)."
    s2 = f"✓ [1 Mark: Method – Multiplying by 100 000 conversion factor]\nCentimetres = {_fmt(km_val)} × 100 000."
    s3 = f"✓ [1 Mark: Accuracy – Value in centimetres]\nDistance = {_fmt(cm_val)} cm."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": "Metric Conversion Bar Scale",
        "segment_length_cm": 2,
        "segment_value_km": km_val,
        "total_segments": 4,
        "scale": f"1 cm represents {_fmt(km_val / 2)} km",
    }

    return _build_question_payload(
        "map_scale_unit_conversion_constants",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="1 km = 100 000 cm.",
        tier_2_hint=f"Multiply {_fmt(km_val)} by 100 000.",
        tier_3_hint=f"{_fmt(km_val)} × 100 000 = {_fmt(cm_val)} cm.",
        diagram_spec=diagram_spec,
    )


def _gen_map_scale_real_distance_from_cm_km(r: random.Random) -> Dict[str, Any]:
    town1 = r.choice(["Kuils River", "Beaufort West", "Colesberg", "Bloemfontein", "Johannesburg"])
    town2 = r.choice(["George", "Kimberley", "Polokwane", "Durban", "East London"])
    while town2 == town1:
        town2 = "Mthatha"

    scale_val = r.choice([250_000, 500_000, 1_000_000, 2_000_000, 3_750_000])
    map_cm = r.choice([6.0, 8.5, 12.0, 15.0, 18.0])
    real_cm = map_cm * scale_val
    real_km = round(real_cm / 100_000.0, 1)

    prompt = (
        f"Refer to the regional map route between {town1} and {town2} below.\n\n"
        f"Route scale ratio: 1 : {_fmt(scale_val)}.\n"
        f"Ruler distance between towns: {_fmt(map_cm)} cm.\n\n"
        f"Calculate the actual real-life distance between the two towns in **kilometres (km)**."
    )
    ans = f"{_fmt(real_km)} km"

    s1 = f"Multiply map distance ({_fmt(map_cm)} cm) by the scale factor ({_fmt(scale_val)}) to get real centimetres, then divide by 100 000 to convert to kilometres."
    s2 = f"✓ [1 Mark: Method – Scaling and unit conversion to km]\nReal cm = {_fmt(map_cm)} cm × {_fmt(scale_val)} = {_fmt(real_cm)} cm.\nReal km = {_fmt(real_cm)} cm ÷ 100 000."
    s3 = f"✓ [1 Mark: Accuracy – Real distance in km]\nReal distance = {_fmt(real_km)} km."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Regional Route: {town1} to {town2}",
        "stops": [
            {"name": town1, "km": 0},
            {"name": town2, "km": real_km},
        ],
        "scale": f"1 : {_fmt(scale_val)}",
    }

    return _build_question_payload(
        "map_scale_real_distance_from_cm_km",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"1 cm on the map equals {_fmt(scale_val)} cm in reality.",
        tier_2_hint=f"Real cm = {_fmt(map_cm)} × {_fmt(scale_val)} = {_fmt(real_cm)} cm. Divide by 100 000.",
        tier_3_hint=f"{_fmt(real_cm)} ÷ 100 000 = {_fmt(real_km)} km.",
        diagram_spec=diagram_spec,
    )

    scale_val = r.choice([250_000, 500_000, 1_000_000, 2_000_000, 3_750_000])
    map_cm = r.choice([6.0, 8.5, 12.0, 15.0, 18.0])
    real_cm = map_cm * scale_val
    real_km = round(real_cm / 100_000.0, 1)

    prompt = (
        f"Refer to the regional map route between {town1} and {town2} below.\n\n"
        f"The distance measures **{_fmt(map_cm)} cm** on the map drawn to a scale of **1 : {_fmt(scale_val)}**.\n\n"
        f"Calculate the actual real-life distance between the two towns in **kilometres (km)**."
    )
    ans = f"{_fmt(real_km)} km"

    s1 = f"Multiply map distance ({_fmt(map_cm)} cm) by the scale factor ({_fmt(scale_val)}) to get real centimetres, then divide by 100 000 to convert to kilometres."
    s2 = f"✓ [1 Mark: Method – Scaling and unit conversion to km]\nReal cm = {_fmt(map_cm)} cm × {_fmt(scale_val)} = {_fmt(real_cm)} cm.\nReal km = {_fmt(real_cm)} cm ÷ 100 000."
    s3 = f"✓ [1 Mark: Accuracy – Real distance in km]\nReal distance = {_fmt(real_km)} km."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Regional Map Route: {town1} to {town2}",
        "stops": [
            {"name": town1, "km": 0},
            {"name": town2, "km": real_km},
        ],
        "scale": f"1 : {_fmt(scale_val)}",
    }

    return _build_question_payload(
        "map_scale_real_distance_from_cm_km",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"1 cm on the map equals {_fmt(scale_val)} cm in reality.",
        tier_2_hint=f"Real cm = {_fmt(map_cm)} × {_fmt(scale_val)} = {_fmt(real_cm)} cm. Divide by 100 000.",
        tier_3_hint=f"{_fmt(real_cm)} ÷ 100 000 = {_fmt(real_km)} km.",
        diagram_spec=diagram_spec,
    )


def _gen_map_scale_real_distance_from_cm_metres(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    feature = r.choice(["sports field", "school hall", "swimming pool complex", "parking area"])
    scale_val = r.choice([200, 250, 400, 500])
    map_cm = r.choice([7.5, 10.0, 12.5, 15.0, 18.0])
    real_cm = map_cm * scale_val
    real_m = round(real_cm / 100.0, 1)

    prompt = (
        f"Refer to the civil site plan below showing the layout of the school {feature}.\n\n"
        f"{name} measures the length of the {feature} on the plan with a ruler and records **{_fmt(map_cm)} cm**.\n"
        f"The site plan scale ratio is **1 : {scale_val}**.\n\n"
        f"Calculate the actual real-life length of the {feature} in **metres (m)**."
    )
    ans = f"{_fmt(real_m)} m"

    s1 = f"Multiply map distance ({_fmt(map_cm)} cm) by scale factor ({scale_val}) to get real centimetres, then divide by 100 to convert to metres."
    s2 = f"✓ [1 Mark: Method – Multiplying by scale factor and dividing by 100]\nReal cm = {_fmt(map_cm)} cm × {scale_val} = {_fmt(real_cm)} cm.\nReal m = {_fmt(real_cm)} cm ÷ 100."
    s3 = f"✓ [1 Mark: Accuracy – Real-world distance in metres]\nReal length = {_fmt(real_m)} m."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "title": f"Site Layout Plan: {feature.title()}",
        "shape": "rectangle",
        "length": real_m,
        "width": round(real_m * 0.6, 1),
        "unit": "m",
        "scale": f"1 : {scale_val}",
    }

    return _build_question_payload(
        "map_scale_real_distance_from_cm_metres",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Scale 1 : {scale_val} means 1 cm on paper equals {scale_val} cm in real life.",
        tier_2_hint=f"Real cm = {_fmt(map_cm)} × {scale_val} = {_fmt(real_cm)} cm. Convert to metres by dividing by 100.",
        tier_3_hint=f"{_fmt(real_cm)} ÷ 100 = {_fmt(real_m)} m.",
        diagram_spec=diagram_spec,
    )


def _gen_map_scale_inverse_drawing_length_from_km(r: random.Random) -> Dict[str, Any]:
    real_km = r.choice([40, 60, 75, 120, 150, 200])
    scale_val = r.choice([500_000, 1_000_000, 2_000_000])
    real_cm = real_km * 100_000
    map_cm = round(real_cm / scale_val, 1)

    prompt = (
        f"Refer to the provincial road map route between two towns shown below, with an actual straight-line distance of **{real_km} km**.\n\n"
        f"A cartographer is drawing this route to a scale of **1 : {_fmt(scale_val)}**.\n\n"
        f"Determine the distance (in cm) that the cartographer must draw on the map to represent this distance."
    )
    ans = f"{_fmt(map_cm)} cm"

    s1 = f"Convert real-life distance from km to cm (multiply by 100 000), then divide by the scale factor ({_fmt(scale_val)})."
    s2 = f"✓ [1 Mark: Method – Converting km to cm and dividing by scale factor]\nReal distance in cm = {real_km} km × 100 000 = {_fmt(real_cm)} cm.\nMap distance = {_fmt(real_cm)} cm ÷ {_fmt(scale_val)}."
    s3 = f"✓ [1 Mark: Accuracy – Distance on map in cm]\nMap distance = {_fmt(map_cm)} cm."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Provincial Road Map Route",
        "stops": [
            {"name": "Town A", "km": 0},
            {"name": "Town B", "km": real_km},
        ],
        "scale": f"1 : {_fmt(scale_val)}",
    }

    return _build_question_payload(
        "map_scale_inverse_drawing_length_from_km",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Convert {real_km} km to cm first: {real_km} × 100 000 = {_fmt(real_cm)} cm.",
        tier_2_hint=f"Divide the real centimetres by the scale factor {_fmt(scale_val)}.",
        tier_3_hint=f"{_fmt(real_cm)} ÷ {_fmt(scale_val)} = {_fmt(map_cm)} cm.",
        diagram_spec=diagram_spec,
    )


def _gen_map_scale_inverse_drawing_length_from_metres(r: random.Random) -> Dict[str, Any]:
    real_m = r.choice([25, 40, 50, 75, 100])
    scale_val = r.choice([200, 250, 500])
    real_cm = real_m * 100
    drawing_cm = round(real_cm / scale_val, 1)

    prompt = (
        f"Refer to the park layout plan diagram below showing a community soccer field.\n\n"
        f"An architectural student is drawing the plan to a scale of **1 : {scale_val}**.\n"
        f"The real-life width of the soccer field is **{real_m} m**.\n\n"
        f"Calculate the width (in cm) that must be drawn on the paper."
    )
    ans = f"{_fmt(drawing_cm)} cm"

    s1 = f"Convert real metres to centimetres ({real_m} m × 100 = {real_cm} cm), then divide by scale factor ({scale_val})."
    s2 = f"✓ [1 Mark: Method – Unit conversion to cm and dividing by scale ratio]\nReal cm = {real_m} m × 100 = {real_cm} cm.\nDrawing width = {real_cm} cm ÷ {scale_val}."
    s3 = f"✓ [1 Mark: Accuracy – Drawing width in cm]\nDrawing width = {_fmt(drawing_cm)} cm."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "title": "Park Layout: Community Soccer Field",
        "shape": "rectangle",
        "length": real_m,
        "width": round(real_m * 0.6),
        "unit": "m",
        "scale": f"1 : {scale_val}",
    }

    return _build_question_payload(
        "map_scale_inverse_drawing_length_from_metres",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Convert {real_m} m to cm: {real_m} × 100 = {real_cm} cm.",
        tier_2_hint=f"Divide {real_cm} cm by {scale_val}.",
        tier_3_hint=f"{real_cm} ÷ {scale_val} = {_fmt(drawing_cm)} cm.",
        diagram_spec=diagram_spec,
    )


def _gen_map_scale_ratio_determination_from_measurements(r: random.Random) -> Dict[str, Any]:
    map_cm = r.choice([4.0, 5.0, 8.0, 10.0])
    real_km = r.choice([20, 25, 40, 50, 100])
    real_cm = real_km * 100_000
    scale_val = int(real_cm / map_cm)

    prompt = (
        f"Refer to the map measurement diagram below showing two towns that are an actual distance of **{real_km} km** apart.\n\n"
        f"When measured on the map with a ruler, the distance between the two towns is **{_fmt(map_cm)} cm**.\n\n"
        f"Determine the **number scale** of this map in the standard format 1 : x."
    )
    ans = f"1 : {_fmt(scale_val)}"

    s1 = f"Convert real distance to centimetres ({real_km} km × 100 000 = {_fmt(real_cm)} cm), then divide by map distance ({_fmt(map_cm)} cm) to find the scale denominator x."
    s2 = f"✓ [1 Mark: Method – Unit matching and scale denominator division]\nReal distance in cm = {real_km} × 100 000 = {_fmt(real_cm)} cm.\nScale ratio x = {_fmt(real_cm)} ÷ {_fmt(map_cm)} = {_fmt(scale_val)}."
    s3 = f"✓ [1 Mark: Accuracy – Number scale in 1 : x format]\nNumber scale = 1 : {_fmt(scale_val)}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Inter-Town Map Measurement",
        "stops": [
            {"name": "Town 1", "km": 0},
            {"name": "Town 2", "km": real_km},
        ],
        "scale": f"1 cm represents {int(real_km / map_cm)} km",
    }

    return _build_question_payload(
        "map_scale_ratio_determination_from_measurements",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Convert {real_km} km to cm: {real_km} × 100 000 = {_fmt(real_cm)} cm.",
        tier_2_hint=f"Divide the real cm by the map cm: {_fmt(real_cm)} ÷ {_fmt(map_cm)}.",
        tier_3_hint=f"The scale is 1 : {_fmt(scale_val)}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_scale_large_scale_vs_small_scale_comparison(r: random.Random) -> Dict[str, Any]:
    city = r.choice(["Durban", "Cape Town", "Johannesburg", "Pretoria", "Gqeberha"])
    s_small = r.choice([5000, 10000, 20000])
    s_large = r.choice([2000000, 5000000, 10000000])

    prompt = (
        f"Refer to the cartographic scale comparison diagram and notes below for two different maps of South Africa:\n"
        f"• Map A has a scale of 1 : {_fmt(s_small)} (City street guide of {city})\n"
        f"• Map B has a scale of 1 : {_fmt(s_large)} (Continental map of Southern Africa)\n\n"
        f"Which map is classified as a **Large-Scale Map**, and why?"
    )
    ans = f"Map A (1 : {_fmt(s_small)}) is a Large-Scale Map — It has a smaller scale denominator, showing a smaller geographic area in much greater detail."
    opts = [
        f"Map A (1 : {_fmt(s_small)}) is a Large-Scale Map — It has a smaller scale denominator, showing a smaller geographic area in much greater detail.",
        f"Map B (1 : {_fmt(s_large)}) is a Large-Scale Map — Because {_fmt(s_large)} is a much larger number than {_fmt(s_small)}.",
        "Both maps have identical scale properties because both are printed on paper.",
        "Map A is small-scale because it only shows one city.",
    ]

    s1 = f"Understand cartographic terminology: Scale is a fraction (1 / x). A smaller denominator (1/{_fmt(s_small)}) is a larger fraction than 1/{_fmt(s_large)}. Therefore 1:{_fmt(s_small)} is a Large-Scale Map with high detail."
    s2 = f"✓ [1 Mark: Method – Explaining fraction size and level of detail]\nLarge-scale = small area + large detail (small denominator). Small-scale = large area + little detail (large denominator)."
    s3 = f"✓ [1 Mark: Accuracy – Selection of Map A and cartographic justification]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Scale Comparison ({city})",
        "segment_length_cm": 2,
        "segment_value_km": round(s_small / 100000, 2),
        "total_segments": 4,
        "scale": f"Map A (1 : {_fmt(s_small)}) vs Map B (1 : {_fmt(s_large)})",
    }

    return _build_question_payload(
        "map_scale_large_scale_vs_small_scale_comparison",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Remember that scale is a fraction: 1/{_fmt(s_small)} is much bigger than 1/{_fmt(s_large)}.",
        tier_2_hint="A large-scale map shows a smaller area with high detail, like a street guide.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Understand cartographic terminology: Scale is a fraction (1 / x). A smaller denominator (1/10 000 = 0,0001) is a larger fraction than 1/5 000 000 (0,0000002). Therefore 1:10 000 is a Large-Scale Map with high detail."
    s2 = f"✓ [1 Mark: Method – Explaining fraction size and level of detail]\nLarge-scale = small area + large detail (small denominator). Small-scale = large area + little detail (large denominator)."
    s3 = f"✓ [1 Mark: Accuracy – Selection of Map A and cartographic justification]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": "Cartographic Scale Comparison",
        "segment_length_cm": 2,
        "segment_value_km": 0.2,
        "total_segments": 4,
        "scale": "Map A (1 : 10 000) vs Map B (1 : 5 000 000)",
    }

    return _build_question_payload(
        "map_scale_large_scale_vs_small_scale_comparison",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Remember that scale is a fraction: 1/10 000 is much bigger than 1/5 000 000.",
        tier_2_hint="A large-scale map shows a smaller area with high detail, like a street guide.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_scale_topographic_standard_fifty_thousand(r: random.Random) -> Dict[str, Any]:
    feature = r.choice(["Trigonometrical Beacon", "River Bridge", "Railway Station", "Windmill", "Church"])
    dist_cm = r.choice([3.0, 4.5, 6.0, 8.0, 10.0])
    real_km = round((dist_cm * 50_000) / 100_000.0, 2)

    prompt = (
        f"On a standard South African 1 : 50 000 topographical map sheet, the distance between a farmhouse "
        f"and a {feature} measures {_fmt(dist_cm)} cm (refer to the topographical graphic scale below).\n\n"
        f"Calculate the actual straight-line distance in kilometres (km)."
    )
    ans = f"{_fmt(real_km)} km"

    s1 = f"On a 1 : 50 000 map, 1 cm represents 50 000 cm = 500 m = 0,5 km. Multiply {_fmt(dist_cm)} cm by 0,5 km/cm."
    s2 = f"✓ [1 Mark: Method – Applying standard 1:50 000 ratio]\nDistance (km) = {_fmt(dist_cm)} cm × 0,5 km/cm."
    s3 = f"✓ [1 Mark: Accuracy – Real distance in km]\nDistance = {_fmt(real_km)} km."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Topographical Sheet ({feature})",
        "segment_length_cm": 2,
        "segment_value_km": 1.0,
        "total_segments": 4,
        "scale": f"1 : 50 000 ({_fmt(dist_cm)} cm reading)",
    }

    return _build_question_payload(
        "map_scale_topographic_standard_fifty_thousand",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="On a 1 : 50 000 map, 1 cm = 0,5 km.",
        tier_2_hint=f"Multiply {_fmt(dist_cm)} by 0,5 km.",
        tier_3_hint=f"{_fmt(dist_cm)} × 0,5 = {_fmt(real_km)} km.",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"Refer to the official South African 1 : 50 000 topographic scale bar below.\n\n"
        f"Rule for 1 : 50 000 Topographic Maps:\n"
        f"• 1 cm on map = 50 000 cm = 500 m = 0,5 km\n"
        f"• Therefore: 2 cm on map = 1 km in real life\n\n"
        f"A hiker measures a straight-line trail on a 1 : 50 000 topographic sheet and finds it measures **{_fmt(cm_measured)} cm**.\n\n"
        f"Calculate the actual real-life distance in **kilometres (km)**."
    )
    ans = f"{_fmt(km_distance)} km"

    s1 = f"On a 1 : 50 000 topographic map, each 1 cm equals 0,5 km (or 500 m). Multiply the measured map distance ({_fmt(cm_measured)} cm) by 0,5 km/cm."
    s2 = f"✓ [1 Mark: Method – Using 1 cm = 0,5 km topographic conversion factor]\nReal distance = {_fmt(cm_measured)} cm × 0,5 km/cm."
    s3 = f"✓ [1 Mark: Accuracy – Distance in kilometres]\nReal distance = {_fmt(km_distance)} km."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": "Official South African 1 : 50 000 Topographic Sheet Scale",
        "segment_length_cm": 2,
        "segment_value_km": 1.0,
        "total_segments": 4,
        "scale": "1 : 50 000 (2 cm = 1 km)",
    }

    return _build_question_payload(
        "map_scale_topographic_standard_fifty_thousand",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="On a 1 : 50 000 map, every 1 cm equals 0,5 km.",
        tier_2_hint=f"Multiply {_fmt(cm_measured)} by 0,5.",
        tier_3_hint=f"{_fmt(cm_measured)} × 0,5 = {_fmt(km_distance)} km.",
        diagram_spec=diagram_spec,
    )


def _gen_map_scale_straight_line_vs_winding_road_distance(r: random.Random) -> Dict[str, Any]:
    straight_km = r.choice([45, 60, 80, 100])
    factor = r.choice([1.25, 1.30, 1.35, 1.40])
    road_km = round(straight_km * factor)

    prompt = (
        f"Refer to the route map below of a mountainous area in the Western Cape:\n"
        f"• The straight-line direct distance ('as the crow flies') between Town A and Town B is **{straight_km} km**.\n"
        f"• The actual road route winds through mountain passes and around ravines, making the road journey **{road_km} km**.\n\n"
        f"1. Why is the actual driving distance longer than the straight-line map measurement?\n"
        f"2. How much further is the driving distance compared to the straight-line distance?"
    )
    diff = road_km - straight_km
    ans = f"Driving distance is {diff} km longer — Roads must navigate natural obstacles (mountains, rivers, valleys) with bends and detours rather than following a straight line."
    opts = [
        f"Driving distance is {diff} km longer — Roads must navigate natural obstacles (mountains, rivers, valleys) with bends and detours rather than following a straight line.",
        f"Driving distance is {diff} km longer — The car's speedometer runs 30% faster in mountains.",
        f"Driving distance is {diff + 10} km longer — South African maps have an automatic 20 km road tax.",
        "Both distances are mathematically identical because both start and end at the same towns.",
    ]

    s1 = f"Differentiate between Euclidean straight-line distance and topological road network distance navigating geographic contours."
    s2 = f"✓ [1 Mark: Method – Subtracting straight-line distance from road distance and terrain rationale]\nDifference = {road_km} km − {straight_km} km = {diff} km. Mountain topography forces roads to follow contours and switchbacks."
    s3 = f"✓ [1 Mark: Accuracy – Difference and geographic explanation]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Western Cape Mountain Pass Route Map",
        "stops": [
            {"name": "Town A", "km": 0},
            {"name": "Pass Summit", "km": round(straight_km * 0.6)},
            {"name": "Town B", "km": road_km},
        ],
        "straight_distance_km": straight_km,
    }

    return _build_question_payload(
        "map_scale_straight_line_vs_winding_road_distance",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Why cannot cars drive in a direct straight line through mountains and valleys?",
        tier_2_hint=f"Subtract straight distance ({straight_km} km) from road distance ({road_km} km): {road_km} − {straight_km} = {diff} km.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )
