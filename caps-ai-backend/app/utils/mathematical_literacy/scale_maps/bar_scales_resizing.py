"""Cluster 2: Bar Scales & Map Resizing Accuracy (Subskills 10 to 17).

Covers:
10. Real distance calculation using graphic bar scale ratios
11. Converting a graphical bar scale to an equivalent number scale (1 : x)
12. Resilience of bar scales under photocopying, resizing, and digital display
13. Invalidation of numeric scales under document enlargement or reduction
14. Contour line intervals and elevation height above sea level
15. Average gradient calculation (Vertical Rise ÷ Horizontal Distance)
16. Map inset scale comparison (regional overview vs detailed city centre)
17. Winding distance measurement methods (string and paper-edge ticking)
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


def _gen_map_bar_scale_segment_measurement_reading(r: random.Random) -> Dict[str, Any]:
    bar_len_cm = r.choice([2.0, 2.5, 3.0])  # Length of graphic bar on paper
    bar_km = r.choice([5, 10, 20, 50])      # Real distance represented by the bar
    segments = r.choice([3, 4, 5, 6])
    map_measured_cm = round(bar_len_cm * segments, 1)
    real_distance_km = round((map_measured_cm / bar_len_cm) * bar_km, 1)

    prompt = (
        f"Refer to the graphic bar scale shown below from a regional tourism map.\n\n"
        f"Scale Bar Information:\n"
        f"• The printed bar scale measures exactly **{_fmt(bar_len_cm)} cm** long per segment with a ruler.\n"
        f"• The label at the end of each segment indicates **{bar_km} km** in real life.\n\n"
        f"A tourist measures the distance between a game reserve gate and a mountain lodge on the map "
        f"and finds it measures **{_fmt(map_measured_cm)} cm**.\n\n"
        f"Using the bar scale ratio, calculate the actual real-world distance in **kilometres (km)**."
    )
    ans = f"{_fmt(real_distance_km)} km"

    s1 = f"Set up a direct proportion with the bar scale: {_fmt(bar_len_cm)} cm on paper represents {bar_km} km in real life. Divide the measured map distance ({_fmt(map_measured_cm)} cm) by the bar length ({_fmt(bar_len_cm)} cm) and multiply by {bar_km} km."
    s2 = f"✓ [1 Mark: Method – Setting up bar scale proportion]\nReal distance = ({_fmt(map_measured_cm)} cm ÷ {_fmt(bar_len_cm)} cm) × {bar_km} km."
    s3 = f"✓ [1 Mark: Accuracy – Calculated real distance]\nDistance = {_fmt(real_distance_km)} km."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": "Tourism Map Graphic Bar Scale",
        "segment_length_cm": bar_len_cm,
        "segment_value_km": bar_km,
        "total_segments": segments,
        "scale": f"{_fmt(bar_len_cm)} cm represents {bar_km} km",
    }

    return _build_question_payload(
        "map_bar_scale_segment_measurement_reading",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"How many {_fmt(bar_len_cm)} cm segments fit into {_fmt(map_measured_cm)} cm? ({_fmt(map_measured_cm)} ÷ {_fmt(bar_len_cm)} = {segments}).",
        tier_2_hint=f"Multiply the number of segments ({segments}) by {bar_km} km.",
        tier_3_hint=f"Distance = {_fmt(real_distance_km)} km.",
        diagram_spec=diagram_spec,
    )


def _gen_map_bar_scale_ratio_conversion_to_number_scale(r: random.Random) -> Dict[str, Any]:
    bar_cm = r.choice([2.0, 4.0, 5.0])
    bar_km = r.choice([10, 20, 25, 50])
    real_cm = bar_km * 100_000
    scale_denominator = int(real_cm / bar_cm)

    prompt = (
        f"Refer to the graphic bar scale shown below.\n\n"
        f"When measured with a plastic ruler, a segment measuring **{_fmt(bar_cm)} cm** represents an actual distance of **{bar_km} km**.\n\n"
        f"Convert this graphical bar scale into an equivalent **number scale** in the standard ratio format **1 : x**."
    )
    ans = f"1 : {_fmt(scale_denominator)}"

    s1 = f"Convert the real distance to the same unit as the measurement (centimetres): {bar_km} km × 100 000 = {_fmt(real_cm)} cm. Divide by the bar measurement ({_fmt(bar_cm)} cm) to find the scale ratio: {_fmt(real_cm)} ÷ {_fmt(bar_cm)} = {_fmt(scale_denominator)}."
    s2 = f"✓ [1 Mark: Method – Converting km to cm and reducing ratio to 1 : x]\nReal cm = {bar_km} km × 100 000 = {_fmt(real_cm)} cm.\nScale x = {_fmt(real_cm)} ÷ {_fmt(bar_cm)} = {_fmt(scale_denominator)}."
    s3 = f"✓ [1 Mark: Accuracy – Equivalent number scale]\nNumber scale = 1 : {_fmt(scale_denominator)}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": "Graphic Bar Scale Conversion",
        "segment_length_cm": bar_cm,
        "segment_value_km": bar_km,
        "total_segments": 4,
        "scale": f"1 : {_fmt(scale_denominator)}",
    }

    return _build_question_payload(
        "map_bar_scale_ratio_conversion_to_number_scale",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Convert {bar_km} km to cm: {bar_km} × 100 000 = {_fmt(real_cm)} cm.",
        tier_2_hint=f"Divide {_fmt(real_cm)} cm by {_fmt(bar_cm)} cm to find 1 cm on the map.",
        tier_3_hint=f"Scale = 1 : {_fmt(scale_denominator)}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_bar_scale_resizing_photocopy_advantage(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    resize_pct = r.choice([50, 75, 125, 150, 200])
    prompt = (
        f"{name} is photocopying a regional municipal map and enlarges or reduces the page by {resize_pct}%.\n"
        f"The original map printed on the paper features BOTH a number ratio scale (1 : 50 000) AND a graphic bar scale.\n\n"
        f"Refer to the graphic bar scale diagram below.\n\n"
        f"Why is the **graphic bar scale** still accurate and valid on the resized photocopy, while the number ratio scale is no longer accurate?"
    )
    ans = "The graphic bar scale physically changes size in the exact same proportion as the resized map, so 1 segment continues to represent the exact same real-world distance."
    opts = [
        "The graphic bar scale physically changes size in the exact same proportion as the resized map, so 1 segment continues to represent the exact same real-world distance.",
        "A bar scale is protected by copyright law from changing dimensions.",
        "Number scales only work in the Southern Hemisphere.",
        "The photocopier automatically detects and recalibrates the bar scale.",
    ]

    s1 = f"Understand the geometric proportionality of graphic bar scales during reprographic resizing (reduction/enlargement)."
    s2 = f"✓ [1 Mark: Method – Identifying proportional resizing of graphical bar elements]\nThe graphic bar expands or contracts by the same {resize_pct}% scale factor as the map image."
    s3 = f"✓ [1 Mark: Accuracy – Correct technical reason]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Resizing Bar Scale ({name}: {resize_pct}%)",
        "segment_length_cm": 2,
        "segment_value_km": 1.0,
        "total_segments": 5,
        "scale": f"Resized to {resize_pct}%",
    }

    return _build_question_payload(
        "map_bar_scale_resizing_photocopy_advantage",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What happens to the bar scale on the paper when you photocopy and resize it?",
        tier_2_hint="The bar scale shrinks or grows with the rest of the map, keeping the proportion identical.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Understand geometric similarity and scaling invariance: graphical elements scale homothetically under magnification, preserving relative ratio, whereas static printed text does not dynamically update."
    s2 = f"✓ [1 Mark: Method – Explaining proportional enlargement of bar scale vs static text of number scale]\nThe graphic bar expands at the identical percentage as roads and boundaries. The text '1:50 000' remains unchanged despite physical expansion."
    s3 = f"✓ [1 Mark: Accuracy – Correct technical justification]\nAdvantage: {ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": "Scale Resilience Comparison: Bar Scale vs Number Scale",
        "segment_length_cm": 2.0,
        "segment_value_km": 1.0,
        "total_segments": 4,
        "scale": "1 : 50 000 (A4 original)",
    }

    return _build_question_payload(
        "map_bar_scale_resizing_photocopy_advantage",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What happens to a picture of a line when you enlarge a picture? The line gets longer.",
        tier_2_hint="The bar scale expands together with the map, so it still measures correctly.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_number_scale_distortion_under_magnification(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    orig_scale = r.choice([10_000, 20_000, 50_000])
    mag_factor = r.choice([2, 3, 4])
    new_scale = orig_scale // mag_factor

    prompt = (
        f"{name} uses a magnifying projector to display a 1 : {_fmt(orig_scale)} building site plan on a wall at {mag_factor}× magnification.\n\n"
        f"Refer to the scale distortion diagram below.\n\n"
        f"If the drawing on the wall is {mag_factor} times larger than the original paper plan, what is the new effective number scale on the wall?"
    )
    ans = f"1 : {_fmt(new_scale)}"
    opts = [
        f"1 : {_fmt(new_scale)}",
        f"1 : {_fmt(orig_scale * mag_factor)}",
        f"1 : {_fmt(orig_scale)}",
        f"1 : {_fmt(new_scale * 2)}",
    ]

    s1 = f"Magnifying by {mag_factor}× makes 1 cm represent fewer real-life units: Divide scale denominator by {mag_factor}."
    s2 = f"✓ [1 Mark: Method – Dividing scale denominator by magnification factor]\nNew scale denominator = {_fmt(orig_scale)} ÷ {mag_factor} = {_fmt(new_scale)}."
    s3 = f"✓ [1 Mark: Accuracy – New effective number scale]\nEffective scale = 1 : {_fmt(new_scale)}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Magnification Analysis ({name}: {mag_factor}x)",
        "segment_length_cm": 2,
        "segment_value_km": round(orig_scale / 100000, 2),
        "total_segments": 4,
        "scale": f"1 : {_fmt(orig_scale)} magnified to 1 : {_fmt(new_scale)}",
    }

    return _build_question_payload(
        "map_number_scale_distortion_under_magnification",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"When an image is enlarged {mag_factor}×, features look bigger, so the scale denominator decreases.",
        tier_2_hint=f"Divide {_fmt(orig_scale)} by {mag_factor}.",
        tier_3_hint=f"New scale is 1 : {_fmt(new_scale)}.",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"Refer to the route diagram below representing two towns on an A4 map with a scale of 1 : 50 000 (True Real Distance = **2,5 km**).\n\n"
        f"The map is enlarged onto A3 paper by 141%. On the enlarged A3 sheet, the distance between the towns now measures **{_fmt(enlarged_cm)} cm**.\n\n"
        f"If a learner mistakenly applies the printed number scale '1 : 50 000' to the enlarged measurement ({_fmt(enlarged_cm)} cm):\n"
        f"1. What erroneous real distance will the learner calculate?\n"
        f"2. How much does this error overestimate the true 2,5 km distance?"
    )
    diff = round(erroneous_km - real_km, 2)
    ans = f"Calculated = {_fmt(erroneous_km)} km (Error: overestimates true distance by {_fmt(diff)} km)"

    s1 = f"Calculate the distorted result using 1 : 50 000 on {_fmt(enlarged_cm)} cm: ({_fmt(enlarged_cm)} × 50 000) ÷ 100 000 = {_fmt(erroneous_km)} km. Compare with true distance ({real_km} km)."
    s2 = f"✓ [1 Mark: Method – Calculating erroneous distance with distorted measurement]\nErroneous km = ({_fmt(enlarged_cm)} × 50 000) ÷ 100 000 = {_fmt(erroneous_km)} km.\nDiscrepancy = {_fmt(erroneous_km)} km − 2,5 km = {_fmt(diff)} km."
    s3 = f"✓ [1 Mark: Accuracy – Erroneous distance and overestimation difference]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Magnified Route Diagram",
        "stops": [
            {"name": "Town 1", "km": 0},
            {"name": "Town 2", "km": real_km},
        ],
        "scale": "1 : 50 000",
    }

    return _build_question_payload(
        "map_number_scale_distortion_under_magnification",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Multiply {_fmt(enlarged_cm)} by 50 000, then divide by 100 000 to get km.",
        tier_2_hint=f"Erroneous distance = {_fmt(erroneous_km)} km. Subtract the true 2,5 km.",
        tier_3_hint=f"{ans}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_contour_lines_and_elevation_height(r: random.Random) -> Dict[str, Any]:
    base_elevation = r.choice([1000, 1200, 1400, 1500])
    interval = r.choice([20, 50, 100])
    lines_crossed = r.choice([3, 4, 5, 6])
    final_elevation = base_elevation + (lines_crossed * interval)

    prompt = (
        f"Refer to the topographic elevation profile shown below.\n\n"
        f"Elevation Information:\n"
        f"• Base foot index contour: {base_elevation} m above sea level.\n"
        f"• Contour vertical spacing: {interval} m per line.\n"
        f"• Summit route: ascends across {lines_crossed} consecutive contour lines to reach the trigonometrical beacon.\n\n"
        f"Calculate the elevation of the beacon at the summit above sea level in metres."
    )
    ans = f"{final_elevation} m above sea level"

    s1 = f"Multiply the number of contour intervals crossed ({lines_crossed}) by the vertical interval ({interval} m) and add to base elevation ({base_elevation} m)."
    s2 = f"✓ [1 Mark: Method – Vertical climb and base elevation sum]\nClimb = {lines_crossed} × {interval} m = {lines_crossed * interval} m.\nTotal elevation = {base_elevation} m + {lines_crossed * interval} m."
    s3 = f"✓ [1 Mark: Accuracy – Summit elevation in metres]\nSummit elevation = {final_elevation} m above sea level."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Topographic Profile ({base_elevation}m Base)",
        "height_m": final_elevation,
        "width_m": 400,
        "label": f"Summit {final_elevation} m",
    }

    return _build_question_payload(
        "map_contour_lines_and_elevation_height",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Each contour line adds {interval} m.",
        tier_2_hint=f"Climb = {lines_crossed} × {interval} = {lines_crossed * interval} m. Add to {base_elevation} m.",
        tier_3_hint=f"{base_elevation} + {lines_crossed * interval} = {final_elevation} m above sea level.",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"Refer to the topographic contour elevation diagram shown below.\n\n"
        f"Contour Details:\n"
        f"• The index contour line at the foot of the hill is labelled **{base_elevation} m** above sea level.\n"
        f"• The vertical contour interval on the map is **{contour_interval} m** between each consecutive line.\n"
        f"• A hiker walks uphill and crosses **{rings} consecutive contour lines** to reach a trigonometric beacon at the summit.\n\n"
        f"Calculate the elevation of the trigonometric beacon at the summit above sea level in metres."
    )
    ans = f"{peak_elevation} m above sea level"

    s1 = f"Multiply the number of contour intervals crossed ({rings}) by the contour vertical interval ({contour_interval} m), then add to the base contour height ({base_elevation} m)."
    s2 = f"✓ [1 Mark: Method – Elevation rise calculation and base addition]\nElevation gain = {rings} lines × {contour_interval} m = {rings * contour_interval} m.\nSummit elevation = {base_elevation} m + {rings * contour_interval} m."
    s3 = f"✓ [1 Mark: Accuracy – Total summit elevation]\nElevation = {peak_elevation} m above sea level."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": "Topographic Hill Elevation Profile",
        "elevation": base_elevation,
        "height_m": peak_elevation,
        "width_m": rings * 100,
        "contour_interval": contour_interval,
        "label": f"Summit Beacon ({peak_elevation} m)",
        "side": "East Aspect",
    }

    return _build_question_payload(
        "map_contour_lines_and_elevation_height",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Each contour line crossed adds {contour_interval} m of height.",
        tier_2_hint=f"Total height climbed = {rings} × {contour_interval} = {rings * contour_interval} m.",
        tier_3_hint=f"Summit elevation = {base_elevation} + {rings * contour_interval} = {peak_elevation} m.",
        diagram_spec=diagram_spec,
    )


def _gen_map_gradient_slope_vertical_rise_horizontal_distance(r: random.Random) -> Dict[str, Any]:
    vertical_rise_m = r.choice([50, 100, 150, 200])
    ratio = r.choice([10, 15, 20, 25, 30])
    horizontal_dist_m = vertical_rise_m * ratio

    prompt = (
        f"Refer to the road incline elevation profile below evaluated by a civil engineer.\n\n"
        f"Measurements from the topographic map:\n"
        f"• Vertical rise (height difference between bottom and top): **{vertical_rise_m} m**\n"
        f"• Horizontal real-world distance between the points: **{horizontal_dist_m} m**\n\n"
        f"Formula: Gradient = Vertical Rise ÷ Horizontal Distance (expressed as 1 : x)\n\n"
        f"Calculate the average gradient (steepness) of the slope in the standard ratio format **1 : x**."
    )
    ans = f"1 : {ratio}"

    s1 = f"Divide horizontal distance ({horizontal_dist_m} m) by vertical rise ({vertical_rise_m} m) to determine the gradient ratio 1 : x (meaning 1 metre rise for every x metres of horizontal travel)."
    s2 = f"✓ [1 Mark: Method – Gradient ratio setup]\nGradient = {vertical_rise_m} ÷ {horizontal_dist_m} = 1 ÷ ({horizontal_dist_m} ÷ {vertical_rise_m}) = 1 : {ratio}."
    s3 = f"✓ [1 Mark: Accuracy – Standard 1 : x gradient ratio]\nGradient = 1 : {ratio}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": "Road Incline Profile",
        "elevation": vertical_rise_m,
        "height_m": vertical_rise_m,
        "width_m": horizontal_dist_m,
        "label": f"Slope 1 : {ratio}",
        "side": "West Incline",
    }

    return _build_question_payload(
        "map_gradient_slope_vertical_rise_horizontal_distance",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide the horizontal distance ({horizontal_dist_m} m) by vertical rise ({vertical_rise_m} m).",
        tier_2_hint=f"{horizontal_dist_m} ÷ {vertical_rise_m} = {ratio}.",
        tier_3_hint=f"Gradient = 1 : {ratio}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_inset_scale_comparison_overview_vs_detail(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    town = r.choice(["Graaff-Reinet", "Oudtshoorn", "Stellenbosch", "Kruger National Park"])
    detail_km = r.choice([1.0, 2.0, 2.5])
    prompt = (
        f"{name} is studying a tourist map of the Western Cape which includes a small magnified inset map of {town}.\n\n"
        f"Refer to the inset bar scale below.\n\n"
        f"What is the primary cartographic purpose of including an enlarged inset map on a regional overview map?"
    )
    ans = "To provide a higher level of detail (street names, tourist landmarks) for a congested area that would be too small to read on the main overview map."
    opts = [
        "To provide a higher level of detail (street names, tourist landmarks) for a congested area that would be too small to read on the main overview map.",
        "To show what the town will look like 50 years in the future.",
        "To indicate that the town is under municipal quarantine.",
        "To correct printing errors made on the overview map.",
    ]

    s1 = f"Understand the functional cartographic purpose of inset maps (locational detail in congested geographic zones)."
    s2 = f"✓ [1 Mark: Method – Explaining spatial detail vs regional context trade-off]\nInset maps zoom into complex nodes at a larger scale."
    s3 = f"✓ [1 Mark: Accuracy – Correct purpose of inset map]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Tourist Inset Bar Scale ({town})",
        "segment_length_cm": 2,
        "segment_value_km": detail_km,
        "total_segments": 4,
        "scale": f"1 segment = {_fmt(detail_km)} km ({town})",
    }

    return _build_question_payload(
        "map_inset_scale_comparison_overview_vs_detail",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Why do city maps zoom into the city centre in a corner box?",
        tier_2_hint="The inset provides clear detail for busy areas without needing the entire map to be huge.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Divide the larger scale denominator (1 500 000) by the smaller scale denominator (15 000): 1 500 000 ÷ 15 000 = {factor}."
    s2 = f"✓ [1 Mark: Method – Comparing scale denominators as magnification ratio]\nMagnification factor = 1 500 000 ÷ 15 000."
    s3 = f"✓ [1 Mark: Accuracy – Relative scale magnification]\nRatio = {factor} times more magnified."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": "Atlas Overview vs Inset Scale Bar",
        "segment_length_cm": 2,
        "segment_value_km": 30,
        "total_segments": 4,
        "scale": "Overview 1 : 1 500 000 | Inset 1 : 15 000",
    }

    return _build_question_payload(
        "map_inset_scale_comparison_overview_vs_detail",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Divide 1 500 000 by 15 000.",
        tier_2_hint=f"1 500 000 ÷ 15 000 = {factor}.",
        tier_3_hint=f"{factor} times more magnified.",
        diagram_spec=diagram_spec,
    )


def _gen_map_winding_distance_using_string_or_paper_edge(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    route = r.choice(["Baviaanskloof Pass", "Sani Pass", "Swartberg Pass", "Chapman's Peak Drive"])
    string_cm = r.choice([14.5, 16.0, 18.5, 22.0, 25.5])
    bar_scale_cm = 2.0
    bar_scale_km = r.choice([1.0, 2.0, 5.0])
    real_km = round((string_cm / bar_scale_cm) * bar_scale_km, 1)

    prompt = (
        f"{name} uses a piece of flexible string to trace the winding path of {route} on a topographical map.\n"
        f"When {name} straightens the string against a ruler, the length is {_fmt(string_cm)} cm.\n\n"
        f"Refer to the graphic bar scale below, where a {_fmt(bar_scale_cm)} cm segment represents {_fmt(bar_scale_km)} km.\n\n"
        f"Calculate the actual real-life distance along the pass in kilometres."
    )
    ans = f"{_fmt(real_km)} km"

    s1 = f"Divide string length ({_fmt(string_cm)} cm) by bar segment length ({_fmt(bar_scale_cm)} cm) and multiply by real distance per segment ({_fmt(bar_scale_km)} km)."
    s2 = f"✓ [1 Mark: Method – String length conversion using bar scale]\nSegments = {_fmt(string_cm)} ÷ {_fmt(bar_scale_cm)} = {_fmt(round(string_cm / bar_scale_cm, 2))}.\nDistance = {_fmt(round(string_cm / bar_scale_cm, 2))} × {_fmt(bar_scale_km)} km."
    s3 = f"✓ [1 Mark: Accuracy – Real winding distance in km]\nActual distance = {_fmt(real_km)} km."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Winding Pass Scale ({route})",
        "segment_length_cm": bar_scale_cm,
        "segment_value_km": bar_scale_km,
        "total_segments": 5,
        "scale": f"{_fmt(bar_scale_cm)} cm = {_fmt(bar_scale_km)} km",
    }

    return _build_question_payload(
        "map_winding_distance_using_string_or_paper_edge",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"How many {_fmt(bar_scale_cm)} cm segments fit into {_fmt(string_cm)} cm?",
        tier_2_hint=f"Segments = {_fmt(string_cm)} ÷ {_fmt(bar_scale_cm)}. Multiply by {_fmt(bar_scale_km)} km.",
        tier_3_hint=f"Distance = {_fmt(real_km)} km.",
        diagram_spec=diagram_spec,
    )

    s1 = f"Recall standard physical measurement techniques for non-linear, curvilinear map features using string or edge-ticking."
    s2 = f"✓ [1 Mark: Method – Explaining piece of string or paper-edge ticking procedure]\nA flexible string conforms to twists and bends, converting curved path length into a single linear length that can be placed against a bar scale."
    s3 = f"✓ [1 Mark: Accuracy – Correct practical measurement method]\nMethod: {ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Winding River Route Map",
        "stops": [
            {"name": "River Source", "km": 0},
            {"name": "Bend A", "km": 15},
            {"name": "Bend B", "km": 32},
            {"name": "River Mouth", "km": 50},
        ],
        "scale": "1 : 50 000",
    }

    return _build_question_payload(
        "map_winding_distance_using_string_or_paper_edge",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="How can you follow a curving line using a straight measuring tool?",
        tier_2_hint="Use a piece of flexible string or paper edge to trace the curves, then straighten it against the scale.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )
