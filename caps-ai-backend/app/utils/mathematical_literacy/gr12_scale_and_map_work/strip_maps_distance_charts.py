"""Subskills 09 to 16: Strip Road Maps, Distance Matrices & Travel Duration Mechanics.
Covers inter-city distance charts, incremental strip map markers, alternative route comparisons,
travel time calculations, decimal hours conversion to hours and minutes,
ETA scheduling with scheduled rest stops, and target arrival speed requirements.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    SA_TOWNS,
    _fmt,
    _fmt_curr,
    _fmt_time,
    _build_options,
    _build_question_payload,
)


def gen_subskill_09(r: random.Random) -> Dict[str, Any]:
    """Subskill 09: Reading a South African inter-city distance matrix chart."""
    city_pairs = [
        ("Johannesburg", "Bloemfontein", 398),
        ("Johannesburg", "Durban", 568),
        ("Cape Town", "Bloemfontein", 1004),
        ("Durban", "Cape Town", 1663),
        ("Johannesburg", "Polokwane", 318),
        ("Pretoria", "Nelspruit", 335),
    ]
    city_a, city_b, dist_km = r.choice(city_pairs)

    table_data = {
        "headers": ["From / To", "Bloemfontein", "Cape Town", "Durban", "Johannesburg", "Polokwane"],
        "rows": [
            ["Bloemfontein", "—", "1 004 km", "635 km", "398 km", "716 km"],
            ["Cape Town", "1 004 km", "—", "1 663 km", "1 400 km", "1 718 km"],
            ["Durban", "635 km", "1 663 km", "—", "568 km", "886 km"],
            ["Johannesburg", "398 km", "1 400 km", "568 km", "—", "318 km"],
            ["Polokwane", "716 km", "1 718 km", "886 km", "318 km", "—"],
        ]
    }

    prompt = (
        f"Refer to the South African inter-city distance table below.\n\n"
        f"Find the driving distance between {city_a} and {city_b} in kilometres (km)."
    )

    correct_ans = f"{_fmt(dist_km)} km"
    explanation = (
        f"1. Locate row '{city_a}' and column '{city_b}' (or vice versa).\n"
        f"2. The intersection value is {correct_ans}."
    )
    t1 = f"Look along the table row for '{city_a}' and the column for '{city_b}'."
    t2 = f"The value at the intersection is {dist_km} km."
    t3 = f"Distance = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_09",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="easy",
    )


def gen_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: Summing incremental distance markers along a provincial strip map."""
    leg1 = r.choice([48, 52, 65])
    leg2 = r.choice([36, 42, 45])
    leg3 = r.choice([74, 80, 85])
    leg4 = r.choice([29, 34, 38])
    total_dist = leg1 + leg2 + leg3 + leg4

    d_spec_10 = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"N1 National Route ({total_dist} km)",
        "stops": [
            {"name": "Town A", "km": 0},
            {"name": "Town B", "km": leg1},
            {"name": "Town C", "km": leg1 + leg2},
            {"name": "Town D", "km": leg1 + leg2 + leg3},
            {"name": "Town E", "km": total_dist},
        ],
    }

    prompt = (
        f"Refer to the strip road map along the N1 national route from Town A to Town E.\n"
        f"The distance between consecutive waypoints is:\n"
        f"• Town A to Town B: {leg1} km\n"
        f"• Town B to Town C: {leg2} km\n"
        f"• Town C to Town D: {leg3} km\n"
        f"• Town D to Town E: {leg4} km\n\n"
        f"Calculate the total driving distance between Town A and Town E in kilometres (km)."
    )

    correct_ans = f"{_fmt(total_dist)} km"
    explanation = (
        f"1. Total distance = {leg1} + {leg2} + {leg3} + {leg4} = {correct_ans}."
    )
    t1 = "Add together all the incremental distance legs along the route."
    t2 = f"Calculation: {leg1} + {leg2} + {leg3} + {leg4}."
    t3 = f"Total distance = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_10",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_10,
    )


def gen_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Subskill 11: Comparing route distances between two destination options."""
    # Route 1: National Highway N1 (longer distance, freeway)
    route_a_km = r.choice([420, 450, 480])
    # Route 2: Regional R-route bypass (shorter distance, secondary road)
    route_b_km = route_a_km - r.randint(25, 45)
    diff_km = route_a_km - route_b_km

    prompt = (
        f"A sales representative plans a trip between two regional commercial hubs.\n"
        f"• Route A (via N-highway): {_fmt(route_a_km)} km\n"
        f"• Route B (via R-scenic bypass): {_fmt(route_b_km)} km\n\n"
        f"1. Which route is shorter in distance?\n"
        f"2. By how many kilometres is it shorter?"
    )

    correct_ans = f"Route B is shorter by {diff_km} km"
    explanation = (
        f"1. Compare distances: Route B ({_fmt(route_b_km)} km) < Route A ({_fmt(route_a_km)} km).\n"
        f"2. Difference = {_fmt(route_a_km)} km − {_fmt(route_b_km)} km = {diff_km} km.\n"
        f"3. Result: {correct_ans}."
    )
    t1 = "Subtract the smaller distance from the larger distance."
    t2 = f"{route_a_km} - {route_b_km} = {diff_km} km."
    t3 = f"Comparison: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Route A is shorter by {diff_km} km",
        f"Route B is shorter by {diff_km + 10} km",
        f"Route A is shorter by {diff_km + 10} km",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_11",
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


def gen_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Subskill 12: Identifying intermediate towns and junction intersections on a strip road map."""
    towns = ["Kroonstad", "Ventersburg", "Winburg", "Verkeerdevlei"]
    chosen_junction = "Winburg"
    distance_to_junction = r.choice([145, 160, 180])

    d_spec_12 = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"N1 Highway Section to {chosen_junction} ({distance_to_junction} km)",
        "stops": [
            {"name": "Start", "km": 0},
            {"name": chosen_junction, "km": distance_to_junction},
        ],
    }

    prompt = (
        f"Refer to the strip road map between Johannesburg and Bloemfontein along the N1 south.\n"
        f"A driver wishes to turn onto the N5 highway towards Harrismith.\n"
        f"The junction intersection is at {chosen_junction}, located "
        f"{distance_to_junction} km from the start of the section.\n\n"
        f"Identify the major junction town on the strip map and state the distance to it."
    )

    correct_ans = f"{chosen_junction} ({distance_to_junction} km)"
    explanation = (
        f"1. On the N1 strip map, the N5 junction connects at {chosen_junction}.\n"
        f"2. The distance from the section start to the interchange is {distance_to_junction} km."
    )
    t1 = "Locate the town with the junction interchange and its corresponding distance."
    t2 = f"Town: {chosen_junction}, Distance: {distance_to_junction} km."
    t3 = f"Intersection: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Kroonstad ({distance_to_junction} km)",
        f"Ventersburg ({distance_to_junction - 45} km)",
        f"{chosen_junction} ({distance_to_junction + 30} km)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_12",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_12,
    )


def gen_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Estimating travel time given strip map distance and average speed."""
    dist_km = r.choice([270, 360, 450, 540])
    speed_kmh = r.choice([90, 100, 120])
    time_hours = dist_km / speed_kmh
    time_str = _fmt_time(time_hours)

    prompt = (
        f"A family travels a distance of {_fmt(dist_km)} km along the N3 freeway from Gauteng to KZN.\n"
        f"The driver maintains an average speed of {speed_kmh} km/h (excluding stops).\n\n"
        f"Using the formula: Time = Distance ÷ Speed,\n"
        f"calculate the driving time."
    )

    correct_ans = time_str
    explanation = (
        f"1. Time = Distance ÷ Speed = {_fmt(dist_km)} km ÷ {speed_kmh} km/h = {_fmt(time_hours, 2)} hours.\n"
        f"2. Converted to hours and minutes: {time_str}."
    )
    t1 = "Divide distance by speed to find time in hours."
    t2 = f"{dist_km} ÷ {speed_kmh} = {time_hours:.2f} hours."
    t3 = f"Driving time = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_13",
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


def gen_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Subskill 14: Converting travel time decimal hours to hours and minutes."""
    h = r.choice([2, 3, 4, 5])
    m = r.choice([12, 18, 24, 36, 42, 48, 54])
    decimal_hours = round(h + (m / 60.0), 2)
    correct_mins = int(round((decimal_hours - int(decimal_hours)) * 60))

    prompt = (
        f"A GPS navigation trip calculation indicates that a journey will take {_fmt(decimal_hours, 2)} hours.\n\n"
        f"Convert this decimal time into exact hours and minutes."
    )

    correct_ans = f"{int(decimal_hours)} hours {correct_mins} minutes"
    explanation = (
        f"1. Whole hours = {int(decimal_hours)} hours.\n"
        f"2. Decimal fraction = {_fmt(decimal_hours - int(decimal_hours), 2)}.\n"
        f"3. Multiply fraction by 60: {_fmt(decimal_hours - int(decimal_hours), 2)} × 60 = {correct_mins} minutes.\n"
        f"4. Result: {correct_ans}."
    )
    t1 = "Take the decimal part of the hours and multiply by 60 to get minutes."
    t2 = f"Fraction = {round(decimal_hours - int(decimal_hours), 2)}. Multiply by 60."
    t3 = f"Time = {correct_ans}."

    # Misconception: reading decimal directly as minutes (e.g. 3.45 h as 3 h 45 min)
    raw_dec_mins = int(round((decimal_hours - int(decimal_hours)) * 100))
    custom_opts = [
        correct_ans,
        f"{int(decimal_hours)} hours {raw_dec_mins} minutes",
        f"{int(decimal_hours)} hours {correct_mins + 10} minutes",
        f"{int(decimal_hours) + 1} hours {correct_mins} minutes",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_14",
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


def gen_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Subskill 15: ETA calculation: departure time + driving duration + scheduled 20-min rest stops."""
    dep_hour = r.choice([6, 7, 8])
    dep_min = r.choice([0, 15, 30])
    driving_hours = r.choice([3.5, 4.0, 4.5])
    num_stops = r.choice([1, 2])
    stop_mins = num_stops * 20

    total_trip_mins = int(driving_hours * 60) + stop_mins
    arr_total_mins = dep_hour * 60 + dep_min + total_trip_mins

    arr_hour = (arr_total_mins // 60) % 24
    arr_min = arr_total_mins % 60
    eta_str = f"{arr_hour:02d}:{arr_min:02d}"

    prompt = (
        f"A long-distance coach departs at {dep_hour:02d}:{dep_min:02d} for a cross-provincial trip.\n"
        f"• Driving time = {_fmt(driving_hours, 1)} hours\n"
        f"• The itinerary includes {num_stops} scheduled rest stop(s) of 20 minutes each.\n\n"
        f"Calculate the Estimated Time of Arrival (ETA) in 24-hour time format."
    )

    correct_ans = eta_str
    explanation = (
        f"1. Driving time in minutes: {_fmt(driving_hours, 1)} × 60 = {int(driving_hours * 60)} minutes.\n"
        f"2. Rest stop time: {num_stops} × 20 = {stop_mins} minutes.\n"
        f"3. Total journey duration = {int(driving_hours * 60)} + {stop_mins} = {total_trip_mins} minutes "
        f"({total_trip_mins // 60} h {total_trip_mins % 60} min).\n"
        f"4. Add to departure {dep_hour:02d}:{dep_min:02d} -> ETA = {eta_str}."
    )
    t1 = "Convert driving hours to minutes, add rest stops, then add total minutes to departure time."
    t2 = f"Total duration = {total_trip_mins} minutes. Add to {dep_hour:02d}:{dep_min:02d}."
    t3 = f"ETA = {correct_ans}."

    # Misconceptions: forgetting rest stops, or adding directly
    no_stop_mins = dep_hour * 60 + dep_min + int(driving_hours * 60)
    no_stop_eta = f"{(no_stop_mins // 60) % 24:02d}:{no_stop_mins % 60:02d}"
    custom_opts = [
        correct_ans,
        no_stop_eta,
        f"{(arr_hour + 1) % 24:02d}:{arr_min:02d}",
        f"{arr_hour:02d}:{(arr_min + 15) % 60:02d}",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_15",
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


def gen_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Subskill 16: Required average speed to arrive at destination by a fixed appointment time."""
    dist_km = r.choice([240, 280, 320])
    target_hours = r.choice([2.5, 3.0, 3.2, 3.5])
    req_speed = round(dist_km / target_hours, 1)

    prompt = (
        f"A commercial field technician needs to travel {_fmt(dist_km)} km to reach a site by 11:30.\n"
        f"Departure is at 08:00, leaving exactly {_fmt(target_hours, 1)} hours of travel time.\n\n"
        f"Using the formula: Average Speed = Distance ÷ Time,\n"
        f"calculate the minimum average driving speed (in km/h) required to arrive on time (to 1 decimal place)."
    )

    correct_ans = f"{_fmt(req_speed, 1)} km/h"
    explanation = (
        f"1. Distance = {_fmt(dist_km)} km, Time = {_fmt(target_hours, 1)} hours.\n"
        f"2. Speed = {_fmt(dist_km)} ÷ {_fmt(target_hours, 1)} = {correct_ans}."
    )
    t1 = "Divide the total distance by the available travel time."
    t2 = f"{dist_km} ÷ {target_hours} = {req_speed} km/h."
    t3 = f"Required speed = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_16",
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
