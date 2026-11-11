"""Subskills 01 to 08: Number Scale Calculations, Bar Scales & Map Reductions.
Covers topo sheet scale calculations, architectural plan measurements, map-to-ground conversions,
determining ratio scales 1 : x, converting bar scales to number scales,
comparing large vs small scale detail, and photocopier enlargement/reduction effects.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_01(r: random.Random) -> Dict[str, Any]:
    """Subskill 01: Calculate actual distance in km from map distance in cm using a 1:50 000 topographic scale."""
    map_dist_cm = r.choice([4.2, 5.5, 6.8, 8.4, 11.2])
    scale_denom = 50000  # Standard SA 1:50 000 topographical map

    # Actual cm = map_cm * 50 000; Actual km = Actual cm / 100 000
    actual_km = round((map_dist_cm * scale_denom) / 100000.0, 2)

    d_spec_01 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Topographical Map Segment ({_fmt(map_dist_cm)} cm)",
        "ratio": "1:50000",
        "segments": [{"length_cm": map_dist_cm, "label": f"{_fmt(map_dist_cm)} cm"}],
    }

    prompt = (
        f"Refer to the topographical map segment (scale 1 : 50 000) showing {_fmt(map_dist_cm)} cm between beacons.\n"
        f"Using the 'MA rule' (Map : Actual):\n"
        f"1. Scale = 1 : 50 000\n"
        f"2. 100 000 cm = 1 km\n\n"
        f"Calculate the actual ground distance between the beacon and the dam in kilometres (km)."
    )

    correct_ans = f"{_fmt(actual_km)} km"
    explanation = (
        f"1. Actual distance in cm = {_fmt(map_dist_cm)} cm × 50 000 = {_fmt(int(map_dist_cm * scale_denom))} cm.\n"
        f"2. Convert cm to km: {_fmt(int(map_dist_cm * scale_denom))} cm ÷ 100 000 = {correct_ans}."
    )
    t1 = "Multiply the map distance by 50 000, then divide by 100 000 to convert to km."
    t2 = f"Calculation: ({map_dist_cm} × 50 000) ÷ 100 000."
    t3 = f"Ground distance = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_01",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_01,
    )


def gen_subskill_02(r: random.Random) -> Dict[str, Any]:
    """Subskill 02: Calculate actual distance in metres from map distance in mm on an architectural site plan."""
    map_dist_mm = r.choice([35, 48, 62, 75, 90])
    scale_denom = r.choice([200, 250, 500])

    # mm on plan -> mm in real life -> metres (divide by 1 000)
    actual_m = round((map_dist_mm * scale_denom) / 1000.0, 2)

    d_spec_02 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "scale": f"1:{scale_denom}",
        "title": f"Site Development Plan ({map_dist_mm} mm)",
        "rooms": [{"name": "Boundary Wall", "length_mm": map_dist_mm}],
    }

    prompt = (
        f"Refer to the architectural site development plan (scale ratio 1 : {scale_denom}) where the boundary wall length is {map_dist_mm} mm.\n\n"
        f"Given that 1 m = 1 000 mm:\n"
        f"Calculate the actual real-life length of the boundary wall in metres (m)."
    )

    correct_ans = f"{_fmt(actual_m)} m"
    explanation = (
        f"1. Actual length in mm = {map_dist_mm} mm × {scale_denom} = {_fmt(int(map_dist_mm * scale_denom))} mm.\n"
        f"2. Convert mm to metres: {_fmt(int(map_dist_mm * scale_denom))} mm ÷ 1 000 = {correct_ans}."
    )
    t1 = f"Multiply the blueprint length by {scale_denom}, then divide by 1 000 to get metres."
    t2 = f"Calculation: ({map_dist_mm} × {scale_denom}) ÷ 1 000."
    t3 = f"Actual length = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_02",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_02,
    )


def gen_subskill_03(r: random.Random) -> Dict[str, Any]:
    """Subskill 03: Calculate map measurement in cm from actual ground distance in km."""
    actual_km = r.choice([25.0, 37.5, 45.0, 60.0, 72.0])
    scale_denom = 250000  # 1 : 250 000 regional tourist map

    # actual cm = actual km * 100 000; map_cm = actual cm / 250 000
    actual_cm = actual_km * 100000.0
    map_cm = round(actual_cm / scale_denom, 1)

    d_spec_03 = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Regional Route ({_fmt(actual_km)} km)",
        "scale": "1:250000",
        "stops": [{"name": "Town A", "km": 0}, {"name": "Town B", "km": actual_km}],
        "towns": [{"name": "Town A", "km": 0}, {"name": "Town B", "km": actual_km}],
    }

    prompt = (
        f"Refer to the regional tourism roadmap (scale ratio 1 : 250 000). Two Free State towns are situated {_fmt(actual_km)} km apart in reality.\n\n"
        f"Given that 1 km = 100 000 cm:\n"
        f"Calculate the distance between these two towns on the map in centimetres (cm)."
    )

    correct_ans = f"{_fmt(map_cm, 1)} cm"
    explanation = (
        f"1. Convert actual distance to cm: {_fmt(actual_km)} km × 100 000 = {_fmt(int(actual_cm))} cm.\n"
        f"2. Map distance = {_fmt(int(actual_cm))} cm ÷ 250 000 = {correct_ans}."
    )
    t1 = "Convert actual kilometres to centimetres by multiplying by 100 000, then divide by 250 000."
    t2 = f"Calculation: ({actual_km} × 100 000) ÷ 250 000."
    t3 = f"Map distance = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_03",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_03,
    )


def gen_subskill_04(r: random.Random) -> Dict[str, Any]:
    """Subskill 04: Determine number scale 1 : x given map measurement in cm and known actual distance in km."""
    map_cm = r.choice([3.0, 4.0, 5.0, 6.0])
    actual_km = r.choice([15.0, 20.0, 30.0, 50.0])

    # scale = map_cm : actual_cm -> 1 : (actual_cm / map_cm)
    actual_cm = actual_km * 100000.0
    denom = int(round(actual_cm / map_cm))

    d_spec_04 = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Highway Interchanges ({_fmt(actual_km)} km)",
        "scale": f"1:{denom}",
        "stops": [{"name": "Interchange 1", "km": 0}, {"name": "Interchange 2", "km": actual_km}],
        "towns": [{"name": "Interchange 1", "km": 0}, {"name": "Interchange 2", "km": actual_km}],
    }

    prompt = (
        f"Refer to the provincial road map. The distance between two highway interchanges is {_fmt(map_cm)} cm, while the actual driving distance along this straight stretch is {_fmt(actual_km)} km.\n\n"
        f"Using the 'MA rule' (Map : Actual) and converting both values to centimetres:\n"
        f"Determine the number scale of the map in the form 1 : x."
    )

    correct_ans = f"1 : {_fmt(denom)}"
    explanation = (
        f"1. Map : Actual = {_fmt(map_cm)} cm : {_fmt(actual_km)} km.\n"
        f"2. Convert actual distance to cm: {_fmt(actual_km)} km × 100 000 = {_fmt(int(actual_cm))} cm.\n"
        f"3. Divide both sides by {_fmt(map_cm)}: {_fmt(map_cm)} ÷ {_fmt(map_cm)} = 1, and "
        f"{_fmt(int(actual_cm))} ÷ {_fmt(map_cm)} = {_fmt(denom)}.\n"
        f"4. Scale = {correct_ans}."
    )
    t1 = "Write Map : Actual, convert km to cm (multiply by 100 000), then divide both sides by the map distance."
    t2 = f"Calculation: ({actual_km} × 100 000) ÷ {map_cm} = {denom}."
    t3 = f"Scale = {correct_ans}."

    # Custom options
    custom_opts = [
        correct_ans,
        f"1 : {_fmt(int(denom / 10))}",
        f"1 : {_fmt(int(denom * 2))}",
        f"1 : {_fmt(int(actual_km * 1000))}",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_04",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_04,
    )


def gen_subskill_05(r: random.Random) -> Dict[str, Any]:
    """Subskill 05: Determine number scale from a graphical bar scale."""
    bar_len_cm = r.choice([2.5, 4.0, 5.0])
    bar_rep_km = r.choice([10.0, 20.0, 25.0])

    actual_cm = bar_rep_km * 100000.0
    denom = int(round(actual_cm / bar_len_cm))

    d_spec_05 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Bar Scale ({_fmt(bar_len_cm)} cm = {_fmt(bar_rep_km)} km)",
        "length_cm": bar_len_cm,
        "represents_km": bar_rep_km,
        "segment_value_km": bar_rep_km,
        "bar_km": bar_rep_km,
        "segments": 4,
        "total_km": bar_rep_km,
    }

    prompt = (
        f"Refer to the graphical bar scale of a national park tourist map. A segment of {_fmt(bar_len_cm)} cm represents an actual ground distance of {_fmt(bar_rep_km)} km.\n\n"
        f"1. Express both measurements in centimetres (1 km = 100 000 cm).\n"
        f"2. Divide both sides by the map measurement ({_fmt(bar_len_cm)} cm) to get 1 on the left.\n\n"
        f"Determine the equivalent number scale in the form 1 : x."
    )

    correct_ans = f"1 : {_fmt(denom)}"
    explanation = (
        f"1. Bar scale ratio: {_fmt(bar_len_cm)} cm : {_fmt(bar_rep_km)} km.\n"
        f"2. Convert km to cm: {_fmt(bar_rep_km)} × 100 000 = {_fmt(int(actual_cm))} cm.\n"
        f"3. Divide both sides by {_fmt(bar_len_cm)}: {_fmt(bar_len_cm)} ÷ {_fmt(bar_len_cm)} = 1, and "
        f"{_fmt(int(actual_cm))} ÷ {_fmt(bar_len_cm)} = {_fmt(denom)}.\n"
        f"4. Equivalent number scale = {correct_ans}."
    )
    t1 = "Convert the bar scale km to cm by multiplying by 100 000, then divide by the measured length in cm."
    t2 = f"Calculation: ({bar_rep_km} × 100 000) ÷ {bar_len_cm}."
    t3 = f"Number scale = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"1 : {_fmt(int(denom / 2))}",
        f"1 : {_fmt(int(denom * 2))}",
        f"1 : {_fmt(int(denom / 10))}",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_05",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_05,
    )


def gen_subskill_06(r: random.Random) -> Dict[str, Any]:
    """Subskill 06: Checking map scale accuracy against strip map distance markers."""
    map_cm = 2.4
    marker_1 = r.choice([20, 24])
    marker_2 = r.choice([16, 18])
    marker_3 = r.choice([22, 26])
    total_km = marker_1 + marker_2 + marker_3  # e.g. 58 km

    actual_cm = total_km * 100000.0
    approx_scale_denom = int(round(actual_cm / map_cm))
    # Standard rounded scale e.g. 1 : 2 400 000
    sensible_rounded_denom = int(round(approx_scale_denom / 100000.0) * 100000)

    d_spec_06 = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Route Markers ({total_km} km)",
        "stops": [
            {"name": "Kimberley", "km": 0},
            {"name": "Marker 1", "km": marker_1},
            {"name": "Marker 2", "km": marker_1 + marker_2},
            {"name": "Heuningneskloof", "km": total_km},
        ],
        "towns": [
            {"name": "Kimberley", "km": 0},
            {"name": "Marker 1", "km": marker_1},
            {"name": "Marker 2", "km": marker_1 + marker_2},
            {"name": "Heuningneskloof", "km": total_km},
        ],
    }

    prompt = (
        f"Refer to the strip map between Kimberley and Heuningneskloof showing three consecutive distance markers: {marker_1} km, {marker_2} km, and {marker_3} km.\n"
        f"The straight distance on the map between the two towns is {_fmt(map_cm)} cm.\n\n"
        f"1. Calculate the total marked distance along the route in km.\n"
        f"2. Use the measurement of {_fmt(map_cm)} cm and your total distance to calculate the approximate "
        f"scale of the map, rounded off to the nearest sensible hundred-thousand (1 : x 00 000)."
    )

    correct_ans = f"Total: {total_km} km (Scale 1 : {_fmt(sensible_rounded_denom)})"
    explanation = (
        f"1. Total distance = {marker_1} + {marker_2} + {marker_3} = {total_km} km.\n"
        f"2. Ratio: {_fmt(map_cm)} cm : {total_km} km = {_fmt(map_cm)} cm : {_fmt(int(actual_cm))} cm.\n"
        f"3. Divide by {_fmt(map_cm)}: {_fmt(int(actual_cm))} ÷ {_fmt(map_cm)} = {_fmt(approx_scale_denom)}.\n"
        f"4. Rounded to nearest 100 000: {correct_ans}."
    )
    t1 = "Add the distance markers together to get total km. Convert to cm and divide by 2,4 cm."
    t2 = f"Total = {total_km} km. Ratio: {actual_cm} ÷ {map_cm} = {approx_scale_denom} -> round to 100 000."
    t3 = f"Result: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Total: {total_km} km (Scale 1 : {_fmt(sensible_rounded_denom + 500000)})",
        f"Total: {total_km - 10} km (Scale 1 : {_fmt(sensible_rounded_denom)})",
        f"Total: {total_km} km (Scale 1 : {_fmt(int(sensible_rounded_denom / 2))})",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_06",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_06,
    )


def gen_subskill_07(r: random.Random) -> Dict[str, Any]:
    """Subskill 07: Comparing map scales: distinguishing larger scale vs smaller scale detail."""
    denom_a = r.choice([25000, 50000, 100000])
    denom_b = r.choice([500000, 1000000, 1500000])
    scale_a = f"1 : {_fmt(denom_a)}"
    scale_b = f"1 : {_fmt(denom_b)}"

    d_spec_07 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Comparative Map Scales (Map A {scale_a} vs Map B {scale_b})",
        "scale": f"1:{denom_a}",
        "bar_km": 10.0,
        "segment_value_km": 2.5,
        "segments": 4,
        "total_km": 10.0,
    }

    prompt = (
        f"Refer to the comparative map scale indicators shown in the diagram.\n"
        f"A learner examines two maps of the same district:\n"
        f"• Map A has a scale of {scale_a} (Topographical map)\n"
        f"• Map B has a scale of {scale_b} (Provincial highway overview map)\n\n"
        f"Which map has the LARGER scale, and which map shows MORE detail (such as individual farm boundaries and contour lines)?"
    )

    correct_ans = "Map A has the larger scale and shows more detail"
    explanation = (
        f"1. In scale ratios (1 : x), the smaller the denominator number, the larger the scale.\n"
        f"2. {_fmt(denom_a)} is much smaller than {_fmt(denom_b)}, so {scale_a} is a larger scale.\n"
        f"3. A larger scale map represents a smaller ground area with much greater detail."
    )
    t1 = "Remember: Smaller denominator = larger scale = more detail."
    t2 = f"{_fmt(denom_a)} < {_fmt(denom_b)}, so Map A has the larger scale."
    t3 = f"Conclusion: {correct_ans}."

    custom_opts = [
        correct_ans,
        "Map B has the larger scale and shows more detail",
        "Map A has the larger scale, but Map B shows more detail",
        "Both maps have the same scale because both cover the same district",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_07",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_07,
    )


def gen_subskill_08(r: random.Random) -> Dict[str, Any]:
    """Subskill 08: Scale enlargement and reduction: effect of photocopying on number scale vs bar scale."""
    enlarge_pct = r.choice([150, 200])

    d_spec_08 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Photocopy Bar Scale Enlargement ({enlarge_pct}%)",
        "scale": "1:50000",
        "segment_value_km": 5.0,
        "bar_km": 20.0,
        "segments": 4,
        "total_km": 20.0,
        "ratio": "1:50000",
        "enlargement_percent": enlarge_pct,
    }

    prompt = (
        f"An original map has a number scale of 1 : 50 000 alongside a graphical bar scale. An educator photocopies it with an enlargement of {enlarge_pct}%.\n\n"
        f"Which of the following statements correctly describes what happens to the two scales on the enlarged photocopy?"
    )

    correct_ans = "The bar scale remains accurate, but the number scale 1 : 50 000 is no longer valid"
    explanation = (
        f"1. The bar scale is enlarged in the exact same proportion as the map image, so 1 cm on the new bar scale still represents the correct ground distance.\n"
        f"2. The written number scale '1 : 50 000' is fixed text and does not change automatically. Because the map image is enlarged, 1 cm on the photocopy now represents less ground distance, making the printed number scale inaccurate."
    )
    t1 = "A bar scale resizes with the image; a printed number scale is just text and becomes incorrect."
    t2 = "The bar scale remains accurate; the printed number scale becomes invalid."
    t3 = f"Statement: {correct_ans}."

    custom_opts = [
        correct_ans,
        "Both the bar scale and the number scale remain completely accurate",
        "The number scale remains accurate, but the bar scale becomes invalid",
        "Neither scale is accurate on the enlarged photocopy",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_08",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_08,
    )
