"""Cluster 5: Strip Maps & Road Route Navigation (Subskills 36 to 44).

Covers:
36. Strip map intermediate segment distance addition (N1 / N3 national corridors)
37. Triangular distance chart (matrix table) lookup between major South African cities
38. Highway toll plaza tariff aggregation across toll corridors
39. Route choice trade-off: Toll highway (shorter + tolls) vs Alternative route (longer + extra fuel)
40. Driver fatigue road safety rest stop scheduling (2 hours / 200 km rule)
41. Fuel range calculation and refueling waypoint planning along a route
42. Average speed over distance (ASOD) minimum transit time calculation (speed cameras)
43. Intermediate waypoint distance subtraction along a linear corridor
44. Road directional signage interpretation (speed limits and distance markers)
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    SA_TOWNS,
    _fmt,
    _fmt_curr,
    _build_question_payload,
)


def _gen_map_strip_consecutive_segment_distances_sum(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    d1 = r.randint(120, 160)  # Joburg to Kroonstad
    d2 = r.randint(190, 230)  # Kroonstad to Bloemfontein
    d3 = r.randint(200, 230)  # Bloemfontein to Colesberg
    d4 = r.randint(210, 240)  # Colesberg to Beaufort West
    total_km = d1 + d2 + d3 + d4

    prompt = (
        f"Refer to the national route N1 strip map shown below.\n\n"
        f"{name} examines the map for a road trip from Johannesburg to Beaufort West.\n\n"
        f"Intermediate segment distances recorded on the strip map:\n"
        f"• Johannesburg to Kroonstad: {d1} km\n"
        f"• Kroonstad to Bloemfontein: {d2} km\n"
        f"• Bloemfontein to Colesberg: {d3} km\n"
        f"• Colesberg to Beaufort West: {d4} km\n\n"
        f"Calculate the total road distance (in km) from Johannesburg to Beaufort West along the N1."
    )
    ans = f"{total_km} km"

    s1 = f"Sum all 4 intermediate consecutive highway segment distances: {d1} + {d2} + {d3} + {d4} = {total_km} km."
    s2 = f"✓ [1 Mark: Method – Adding all 4 consecutive segment distances]\nTotal distance = {d1} km + {d2} km + {d3} km + {d4} km."
    s3 = f"✓ [1 Mark: Accuracy – Total road trip distance]\nTotal = {total_km} km."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "National Route N1 Strip Map: Johannesburg to Beaufort West",
        "stops": [
            {"name": "Johannesburg", "km": 0},
            {"name": "Kroonstad", "km": d1},
            {"name": "Bloemfontein", "km": d1 + d2},
            {"name": "Colesberg", "km": d1 + d2 + d3},
            {"name": "Beaufort West", "km": total_km},
        ],
    }

    return _build_question_payload(
        "map_strip_consecutive_segment_distances_sum",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Add all 4 segment distances together: {d1} + {d2} + {d3} + {d4}.",
        tier_2_hint=f"{d1} + {d2} + {d3} + {d4} = {total_km}.",
        tier_3_hint=f"Total distance = {total_km} km.",
        diagram_spec=diagram_spec,
    )


def _gen_map_strip_distance_chart_matrix_reading(r: random.Random) -> Dict[str, Any]:
    cities = ["Bloemfontein", "Cape Town", "Durban", "Johannesburg"]
    matrix = {
        ("Bloemfontein", "Cape Town"): 1004,
        ("Bloemfontein", "Durban"): 634,
        ("Bloemfontein", "Johannesburg"): 398,
        ("Cape Town", "Durban"): 1636,
        ("Cape Town", "Johannesburg"): 1402,
        ("Durban", "Johannesburg"): 568,
    }
    pair = r.choice(list(matrix.keys()))
    city_a, city_b = pair
    dist = matrix[pair]

    prompt = (
        f"Study the intercity road distance grid map and triangular table below:\n\n"
        f"| City | Bloemfontein | Cape Town | Durban | Johannesburg |\n"
        f"| :--- | :---: | :---: | :---: | :---: |\n"
        f"| Bloemfontein | — | 1 004 | 634 | 398 |\n"
        f"| Cape Town | 1 004 | — | 1 636 | 1 402 |\n"
        f"| Durban | 634 | 1 636 | — | 568 |\n"
        f"| Johannesburg | 398 | 1 402 | 568 | — |\n\n"
        f"1. Explain how to read this distance matrix table.\n"
        f"2. Read the table to determine the exact road distance between **{city_a}** and **{city_b}**."
    )
    ans = f"{_fmt(dist)} km"

    s1 = f"Locate '{city_a}' in the row headers and '{city_b}' in the column headers (or vice versa), and read the number at their intersection cell ({_fmt(dist)} km)."
    s2 = f"✓ [1 Mark: Method – Reading cell intersection in triangular matrix]\nIntersection of {city_a} and {city_b} = {_fmt(dist)} km."
    s3 = f"✓ [1 Mark: Accuracy – Distance read from table]\nDistance = {_fmt(dist)} km."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "grid_map",
        "title": "Intercity Road Distance Matrix (km)",
        "columns": cities,
        "rows": cities,
        "landmarks": [
            {"name": f"{city_a} - {city_b}", "cell": f"{dist} km"},
        ],
    }

    return _build_question_payload(
        "map_strip_distance_chart_matrix_reading",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the row for {city_a} and trace across to the column for {city_b}.",
        tier_2_hint=f"Read the value at the intersection: {_fmt(dist)} km.",
        tier_3_hint=f"Distance = {_fmt(dist)} km.",
        diagram_spec=diagram_spec,
    )


def _gen_map_strip_toll_plaza_tariff_aggregation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    t1_cost = r.choice([42.50, 48.00, 56.50])
    t2_cost = r.choice([68.00, 74.50, 82.00])
    t3_cost = r.choice([31.00, 35.50, 40.00])
    total_toll = t1_cost + t2_cost + t3_cost
    p1_km = r.choice([60, 75, 80])
    p2_km = p1_km + r.choice([90, 110, 120])

    prompt = (
        f"{name} is driving a Class 1 light passenger vehicle along a major toll highway.\n"
        f"Along the route, {name} passes through three toll plazas with the following tariffs:\n"
        f"• Plaza 1: {_fmt_curr(t1_cost)}\n"
        f"• Plaza 2: {_fmt_curr(t2_cost)}\n"
        f"• Plaza 3: {_fmt_curr(t3_cost)}\n\n"
        f"Refer to the strip route map below.\n\n"
        f"Calculate the total toll fees {name} will pay for a one-way trip through all three toll plazas."
    )
    ans = _fmt_curr(total_toll)

    s1 = f"Add the tariffs of all three toll plazas along the route: {_fmt_curr(t1_cost)} + {_fmt_curr(t2_cost)} + {_fmt_curr(t3_cost)}."
    s2 = f"✓ [1 Mark: Method – Summing three toll gate fees]\nTotal = {_fmt_curr(t1_cost)} + {_fmt_curr(t2_cost)} + {_fmt_curr(t3_cost)}."
    s3 = f"✓ [1 Mark: Accuracy – Total toll fees in Rands]\nTotal Toll = {_fmt_curr(total_toll)}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Toll Highway Strip Map ({name})",
        "stops": [
            {"name": "Start", "km": 0},
            {"name": f"Plaza 1 ({_fmt_curr(t1_cost)})", "km": p1_km},
            {"name": f"Plaza 2 ({_fmt_curr(t2_cost)})", "km": p2_km},
            {"name": "Terminus", "km": p2_km + 90},
        ],
    }

    return _build_question_payload(
        "map_strip_toll_plaza_tariff_aggregation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Add {_fmt_curr(t1_cost)} + {_fmt_curr(t2_cost)} + {_fmt_curr(t3_cost)}.",
        tier_2_hint=f"Total = {_fmt_curr(t1_cost)} + {_fmt_curr(t2_cost)} + {_fmt_curr(t3_cost)}.",
        tier_3_hint=f"Total toll fees = {_fmt_curr(total_toll)}.",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"Refer to the N3 toll highway corridor strip map below.\n\n"
        f"A motorist drives a standard Class 1 light passenger vehicle from Johannesburg to Durban, passing through 4 toll plazas:\n"
        f"• De Hoek Toll Plaza: R 63,00\n"
        f"• Wilge Toll Plaza: R 86,00\n"
        f"• Tugela Toll Plaza: R 91,00\n"
        f"• Mooi River Toll Plaza: R 62,00\n\n"
        f"Calculate the total toll fees paid for a one-way trip in Rands."
    )
    ans = _fmt_curr(total_tolls)

    s1 = f"Add the tariffs for all 4 toll plazas: R 63,00 + R 86,00 + R 91,00 + R 62,00 = R {_fmt(total_tolls)}."
    s2 = f"✓ [1 Mark: Method – Summing all mainline toll fees]\nTotal Tolls = R 63,00 + R 86,00 + R 91,00 + R 62,00."
    s3 = f"✓ [1 Mark: Accuracy – Total toll fees to 2 decimal places]\nTotal = {_fmt_curr(total_tolls)}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "N3 Mainline Toll Plaza Corridor",
        "stops": [
            {"name": "Johannesburg", "km": 0},
            {"name": "De Hoek (R 63)", "km": 100},
            {"name": "Wilge (R 86)", "km": 210},
            {"name": "Tugela (R 91)", "km": 370},
            {"name": "Mooi River (R 62)", "km": 480},
            {"name": "Durban", "km": 580},
        ],
    }

    return _build_question_payload(
        "map_strip_toll_plaza_tariff_aggregation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Add up all 4 toll plaza fees.",
        tier_2_hint=f"R 63 + R 86 + R 91 + R 62 = R {_fmt(total_tolls)}.",
        tier_3_hint=f"Total = {_fmt_curr(total_tolls)}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_strip_route_choice_toll_highway_vs_alternative(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    d_toll = r.choice([200, 220, 240])
    d_alt = d_toll + r.choice([25, 35, 45])
    toll_fee = r.choice([95.00, 110.00, 130.00])
    fuel_cost_per_km = 1.80  # R1.80 per km

    fuel_toll_route = d_toll * fuel_cost_per_km
    total_toll_route = fuel_toll_route + toll_fee
    fuel_alt_route = d_alt * fuel_cost_per_km

    diff = round(abs(total_toll_route - fuel_alt_route), 2)
    cheaper_route = "Alternative Route (Non-Toll)" if fuel_alt_route < total_toll_route else "Toll Highway"

    prompt = (
        f"{name} is deciding between two routes between two towns:\n"
        f"• Toll Highway: Distance = {d_toll} km, Toll fee = {_fmt_curr(toll_fee)}\n"
        f"• Alternative Regional Route: Distance = {d_alt} km, No tolls (R 0,00)\n\n"
        f"Vehicle fuel running cost is {_fmt_curr(fuel_cost_per_km)} per kilometre on both roads.\n"
        f"Refer to the strip route choice map below.\n\n"
        f"Determine which route is cheaper overall (fuel + toll combined) and calculate the Rand savings."
    )
    ans = f"{cheaper_route} is cheaper by {_fmt_curr(diff)}"

    s1 = f"Calculate total cost for both routes: Toll Route Cost = ({d_toll} km × {_fmt_curr(fuel_cost_per_km)}) + {_fmt_curr(toll_fee)}; Alt Route Cost = {d_alt} km × {_fmt_curr(fuel_cost_per_km)}, then compare."
    s2 = f"✓ [1 Mark: Method – Calculating total cost for both routes and difference]\nToll route = {_fmt_curr(fuel_toll_route)} + {_fmt_curr(toll_fee)} = {_fmt_curr(total_toll_route)}.\nAlt route = {_fmt_curr(fuel_alt_route)}.\nDifference = {_fmt_curr(diff)}."
    s3 = f"✓ [1 Mark: Accuracy – Cheaper route identified with exact Rand savings]\nVerdict: {ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Route Choice Strip Map ({name})",
        "stops": [
            {"name": "Origin", "km": 0},
            {"name": f"Toll Highway ({d_toll} km)", "km": d_toll},
            {"name": f"Alternative ({d_alt} km)", "km": d_alt},
        ],
    }

    return _build_question_payload(
        "map_strip_route_choice_toll_highway_vs_alternative",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Toll route cost: ({d_toll} × {_fmt_curr(fuel_cost_per_km)}) + {_fmt_curr(toll_fee)} = {_fmt_curr(total_toll_route)}.",
        tier_2_hint=f"Alt route cost: {d_alt} × {_fmt_curr(fuel_cost_per_km)} = {_fmt_curr(fuel_alt_route)}.",
        tier_3_hint=f"{ans}.",
        diagram_spec=diagram_spec,
    )

    dist_toll = 500
    fuel_toll = (dist_toll / 100) * rate * petrol_price
    toll_fees = 280.00
    total_route_1 = fuel_toll + toll_fees

    dist_alt = 570
    fuel_alt = (dist_alt / 100) * rate * petrol_price
    total_route_2 = fuel_alt

    diff = round(abs(total_route_1 - total_route_2), 2)
    cheaper_route = "Route 2 (Alternative Backroad)" if total_route_2 < total_route_1 else "Route 1 (Toll Highway)"

    prompt = (
        f"Refer to the route choice comparison diagram below for a business trip:\n\n"
        f"• **Route 1 (National Toll Highway)**: Distance = {dist_toll} km; Toll fees = {_fmt_curr(toll_fees)}\n"
        f"• **Route 2 (Alternative Regional Route)**: Distance = {dist_alt} km; Zero toll fees\n\n"
        f"Both routes are driven in a car using 7,0 litres per 100 km, with petrol at {_fmt_curr(petrol_price)} per litre.\n\n"
        f"1. Calculate the total cost (Fuel + Tolls) for Route 1.\n"
        f"2. Calculate the total cost (Fuel only) for Route 2.\n"
        f"3. Which route is financially cheaper, and by how much?"
    )
    ans = f"Route 1 = {_fmt_curr(total_route_1)}; Route 2 = {_fmt_curr(total_route_2)} — {cheaper_route} is cheaper by {_fmt_curr(diff)}"

    s1 = f"Calculate fuel cost for Route 1 ((500÷100)×7,0 = 35 L × R 24,50 = R 857,50) + Tolls (R 280,00) = R 1 137,50. Calculate fuel for Route 2 ((570÷100)×7,0 = 39,9 L × R 24,50 = R 977,55). Compare totals."
    s2 = f"✓ [1 Mark: Method – Calculating both route totals and finding difference]\nRoute 1 = R 857,50 + R 280,00 = {_fmt_curr(total_route_1)}.\nRoute 2 = {_fmt_curr(total_route_2)}.\nDifference = |{_fmt_curr(total_route_1)} − {_fmt_curr(total_route_2)}| = {_fmt_curr(diff)}."
    s3 = f"✓ [1 Mark: Accuracy – Total costs and cheaper route identification]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Route Choice Corridor Comparison",
        "stops": [
            {"name": "Origin", "km": 0},
            {"name": "Route 1 (Toll Highway)", "km": dist_toll},
            {"name": "Route 2 (Alternative Route)", "km": dist_alt},
        ],
    }

    return _build_question_payload(
        "map_strip_route_choice_toll_highway_vs_alternative",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Route 1 total = {_fmt_curr(total_route_1)}. Route 2 total = {_fmt_curr(total_route_2)}.",
        tier_2_hint=f"Subtract to find savings: {_fmt_curr(total_route_1)} − {_fmt_curr(total_route_2)}.",
        tier_3_hint=f"{ans}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_strip_safety_rest_stop_frequency(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_km = r.choice([650, 750, 850, 920, 1050])
    rule_km = 200
    stops = total_km // rule_km

    prompt = (
        f"Refer to the long-distance highway strip map below for a journey of **{total_km} km** from Johannesburg to Cape Town.\n\n"
        f"South African road safety campaigns (such as Arrive Alive) advise drivers:\n"
        f"'To combat driver fatigue, stop for at least 15 minutes after every 2 hours of driving or every **200 km**.'\n\n"
        f"Calculate the **minimum number of rest stops** {name} must plan during this {total_km} km journey."
    )
    ans = f"{stops} rest stops"

    s1 = f"Divide total distance ({total_km} km) by the recommended rest interval (200 km) and take the integer quotient ({stops} stops before destination)."
    s2 = f"✓ [1 Mark: Method – Dividing total distance by 200 km safety interval]\nStops = {total_km} km ÷ 200 km = {_fmt(round(total_km / rule_km, 2))} → {stops} stops."
    s3 = f"✓ [1 Mark: Accuracy – Minimum recommended rest stops]\nStops required = {stops} rest stops."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Johannesburg to Cape Town Rest Stop Corridor",
        "stops": [
            {"name": "Johannesburg", "km": 0},
            {"name": "Rest Stop 1", "km": 200},
            {"name": "Rest Stop 2", "km": 400},
            {"name": "Rest Stop 3", "km": 600},
            {"name": "Cape Town", "km": total_km},
        ],
    }

    return _build_question_payload(
        "map_strip_safety_rest_stop_frequency",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {total_km} by 200 km.",
        tier_2_hint=f"{total_km} ÷ 200 = {_fmt(round(total_km / 200, 2))}.",
        tier_3_hint=f"Minimum rest stops = {stops} rest stops.",
        diagram_spec=diagram_spec,
    )


def _gen_map_strip_fuel_range_refueling_stop_planning(r: random.Random) -> Dict[str, Any]:
    tank_litres = r.choice([45, 50, 55])
    rate = r.choice([7.0, 7.5, 8.0])
    max_range_km = round((tank_litres / rate) * 100)
    trip_distance_km = 850

    prompt = (
        f"Refer to the 850 km Karoo highway route map below.\n\n"
        f"Vehicle fuel limits:\n"
        f"• Fuel tank capacity: **{tank_litres} litres** (full at departure)\n"
        f"• Highway consumption rate: **{_fmt(rate)} litres per 100 km**\n\n"
        f"Formula: Maximum Driving Range (km) = (Tank Capacity ÷ Consumption Rate) × 100\n\n"
        f"1. Calculate the vehicle's maximum driving range on a full tank (in km).\n"
        f"2. Can the motorist complete the 850 km trip without refueling?"
    )
    ans = f"Maximum range = {max_range_km} km — No, the motorist cannot complete 850 km without refueling (must refuel before {max_range_km} km)."

    s1 = f"Calculate maximum driving range: ({tank_litres} ÷ {_fmt(rate)}) × 100 = {max_range_km} km. Compare with trip length of 850 km."
    s2 = f"✓ [1 Mark: Method – Range formula setup and comparison with trip length]\nRange = ({tank_litres} ÷ {_fmt(rate)}) × 100 = {max_range_km} km.\nComparison: {max_range_km} km < 850 km."
    s3 = f"✓ [1 Mark: Accuracy – Maximum range and refuel necessity verdict]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Karoo Highway Route (850 km)",
        "stops": [
            {"name": "Departure Point", "km": 0},
            {"name": f"Max Range ({max_range_km} km)", "km": max_range_km},
            {"name": "Destination", "km": trip_distance_km},
        ],
    }

    return _build_question_payload(
        "map_strip_fuel_range_refueling_stop_planning",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {tank_litres} by {_fmt(rate)}, then multiply by 100.",
        tier_2_hint=f"Range = ({tank_litres} ÷ {_fmt(rate)}) × 100 = {max_range_km} km. Compare with 850 km.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_strip_average_speed_enforcement_timing(r: random.Random) -> Dict[str, Any]:
    distance_km = r.choice([48, 60, 72, 84])
    speed_limit = 120
    min_time_hours = distance_km / speed_limit
    min_time_mins = round(min_time_hours * 60)

    prompt = (
        f"Refer to the SANRAL Average Speed Over Distance (ASOD) route diagram below spanning **{distance_km} km**.\n\n"
        f"The maximum legal speed limit in this zone is **{speed_limit} km/h**.\n\n"
        f"Calculate the **minimum legal travel time (in minutes)** a driver must take to travel through "
        f"this {distance_km} km zone without exceeding the 120 km/h average speed limit and receiving a speeding fine."
    )
    ans = f"{min_time_mins} minutes"

    s1 = f"Calculate minimum travel time: Distance ÷ Speed Limit = {distance_km} km ÷ {speed_limit} km/h = {_fmt(min_time_hours)} hours. Convert to minutes by multiplying by 60."
    s2 = f"✓ [1 Mark: Method – Time calculation and hour-to-minute conversion]\nTime = ({distance_km} ÷ {speed_limit}) × 60 = {_fmt(min_time_hours)} × 60."
    s3 = f"✓ [1 Mark: Accuracy – Minimum legal duration in minutes]\nMinimum time = {min_time_mins} minutes."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"SANRAL ASOD Zone ({distance_km} km)",
        "stops": [
            {"name": "Camera Gate 1", "km": 0},
            {"name": "Zone Midpoint", "km": distance_km // 2},
            {"name": "Camera Gate 2", "km": distance_km},
        ],
        "scale": f"Speed Limit: {speed_limit} km/h",
    }

    return _build_question_payload(
        "map_strip_average_speed_enforcement_timing",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {distance_km} km by 120 km/h.",
        tier_2_hint=f"({distance_km} ÷ 120) × 60 = {min_time_mins} minutes.",
        tier_3_hint=f"Minimum time = {min_time_mins} minutes.",
        diagram_spec=diagram_spec,
    )


def _gen_map_strip_intermediate_town_distance_subtraction(r: random.Random) -> Dict[str, Any]:
    total_km = r.choice([420, 480, 520, 560])
    part_km = r.choice([160, 180, 210, 240])
    rem_km = total_km - part_km

    prompt = (
        f"Refer to the regional strip map below showing three consecutive towns along a road: Town A, Town B, and Town C.\n\n"
        f"Measurements from the map:\n"
        f"• Total distance from Town A to Town C: **{total_km} km**\n"
        f"• Distance from Town A to Town B: **{part_km} km**\n\n"
        f"Calculate the remaining distance between **Town B and Town C**."
    )
    ans = f"{rem_km} km"

    s1 = f"Subtract the distance of the first segment ({part_km} km) from the total distance ({total_km} km)."
    s2 = f"✓ [1 Mark: Method – Subtraction of intermediate waypoint distance]\nDistance B to C = {total_km} km − {part_km} km."
    s3 = f"✓ [1 Mark: Accuracy – Remaining segment distance]\nDistance = {rem_km} km."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Regional Strip Map: Town A - B - C",
        "stops": [
            {"name": "Town A", "km": 0},
            {"name": "Town B", "km": part_km},
            {"name": "Town C", "km": total_km},
        ],
    }

    return _build_question_payload(
        "map_strip_intermediate_town_distance_subtraction",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Subtract {part_km} km from {total_km} km.",
        tier_2_hint=f"{total_km} − {part_km} = {rem_km}.",
        tier_3_hint=f"Remaining distance = {rem_km} km.",
        diagram_spec=diagram_spec,
    )


def _gen_map_strip_road_sign_speed_limit_and_distance(r: random.Random) -> Dict[str, Any]:
    town1 = "Kimberley"
    town2 = "Bloemfontein"
    d1 = r.choice([45, 60, 75])
    d2 = d1 + r.randint(80, 120)

    prompt = (
        f"Refer to the N8 highway corridor route diagram and signpost below:\n\n"
        f"**[ {town1} : {d1} km ]**\n"
        f"**[ {town2} : {d2} km ]**\n\n"
        f"Assuming both cities lie straight ahead along the same N8 route:\n"
        f"How far is {town2} from {town1}?"
    )
    dist_between = d2 - d1
    ans = f"{dist_between} km"

    s1 = f"Subtract the closer town's distance ({d1} km) from the further town's distance ({d2} km): {d2} − {d1} = {dist_between} km."
    s2 = f"✓ [1 Mark: Method – Subtracting road sign destination distances]\nDistance = {d2} km − {d1} km."
    s3 = f"✓ [1 Mark: Accuracy – Distance between the two towns]\nDistance = {dist_between} km."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "N8 Highway Route Signpost",
        "stops": [
            {"name": "Signpost Location", "km": 0},
            {"name": town1, "km": d1},
            {"name": town2, "km": d2},
        ],
    }

    return _build_question_payload(
        "map_strip_road_sign_speed_limit_and_distance",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Subtract the distance to {town1} ({d1} km) from the distance to {town2} ({d2} km).",
        tier_2_hint=f"{d2} − {d1} = {dist_between} km.",
        tier_3_hint=f"Distance = {dist_between} km.",
        diagram_spec=diagram_spec,
    )
