"""Remediates Cluster 5 (strip maps) and Cluster 6 (seating indoor maps) in scale_maps/."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "caps-ai-backend/app/utils/mathematical_literacy/scale_maps"

STRIP_MAPS_CODE = '''"""Cluster 5: Strip Maps & Road Route Navigation (Subskills 36 to 44).

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
        f"Refer to the national route N1 strip map shown below.\\n\\n"
        f"{name} examines the map for a road trip from Johannesburg to Beaufort West.\\n\\n"
        f"Intermediate segment distances recorded on the strip map:\\n"
        f"• Johannesburg to Kroonstad: {d1} km\\n"
        f"• Kroonstad to Bloemfontein: {d2} km\\n"
        f"• Bloemfontein to Colesberg: {d3} km\\n"
        f"• Colesberg to Beaufort West: {d4} km\\n\\n"
        f"Calculate the total road distance (in km) from Johannesburg to Beaufort West along the N1."
    )
    ans = f"{total_km} km"

    s1 = f"Sum all 4 intermediate consecutive highway segment distances: {d1} + {d2} + {d3} + {d4} = {total_km} km."
    s2 = f"✓ [1 Mark: Method – Adding all 4 consecutive segment distances]\\nTotal distance = {d1} km + {d2} km + {d3} km + {d4} km."
    s3 = f"✓ [1 Mark: Accuracy – Total road trip distance]\\nTotal = {total_km} km."

    diagram_spec = {
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
        f"Study the intercity road distance grid map and triangular table below:\\n\\n"
        f"| City | Bloemfontein | Cape Town | Durban | Johannesburg |\\n"
        f"| :--- | :---: | :---: | :---: | :---: |\\n"
        f"| Bloemfontein | — | 1 004 | 634 | 398 |\\n"
        f"| Cape Town | 1 004 | — | 1 636 | 1 402 |\\n"
        f"| Durban | 634 | 1 636 | — | 568 |\\n"
        f"| Johannesburg | 398 | 1 402 | 568 | — |\\n\\n"
        f"1. Explain how to read this distance matrix table.\\n"
        f"2. Read the table to determine the exact road distance between **{city_a}** and **{city_b}**."
    )
    ans = f"{_fmt(dist)} km"

    s1 = f"Locate '{city_a}' in the row headers and '{city_b}' in the column headers (or vice versa), and read the number at their intersection cell ({_fmt(dist)} km)."
    s2 = f"✓ [1 Mark: Method – Reading cell intersection in triangular matrix]\\nIntersection of {city_a} and {city_b} = {_fmt(dist)} km."
    s3 = f"✓ [1 Mark: Accuracy – Distance read from table]\\nDistance = {_fmt(dist)} km."

    diagram_spec = {
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
    tolls = [
        ("De Hoek Toll Plaza", 63.00),
        ("Wilge Toll Plaza", 86.00),
        ("Tugela Toll Plaza", 91.00),
        ("Mooi River Toll Plaza", 62.00),
    ]
    total_tolls = sum(t[1] for t in tolls)

    prompt = (
        f"Refer to the N3 toll highway corridor strip map below.\\n\\n"
        f"A motorist drives a standard Class 1 light passenger vehicle from Johannesburg to Durban, passing through 4 toll plazas:\\n"
        f"• De Hoek Toll Plaza: R 63,00\\n"
        f"• Wilge Toll Plaza: R 86,00\\n"
        f"• Tugela Toll Plaza: R 91,00\\n"
        f"• Mooi River Toll Plaza: R 62,00\\n\\n"
        f"Calculate the total toll fees paid for a one-way trip in Rands."
    )
    ans = _fmt_curr(total_tolls)

    s1 = f"Add the tariffs for all 4 toll plazas: R 63,00 + R 86,00 + R 91,00 + R 62,00 = R {_fmt(total_tolls)}."
    s2 = f"✓ [1 Mark: Method – Summing all mainline toll fees]\\nTotal Tolls = R 63,00 + R 86,00 + R 91,00 + R 62,00."
    s3 = f"✓ [1 Mark: Accuracy – Total toll fees to 2 decimal places]\\nTotal = {_fmt_curr(total_tolls)}."

    diagram_spec = {
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
    petrol_price = 24.50
    rate = 7.0  # L / 100km

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
        f"Refer to the route choice comparison diagram below for a business trip:\\n\\n"
        f"• **Route 1 (National Toll Highway)**: Distance = {dist_toll} km; Toll fees = {_fmt_curr(toll_fees)}\\n"
        f"• **Route 2 (Alternative Regional Route)**: Distance = {dist_alt} km; Zero toll fees\\n\\n"
        f"Both routes are driven in a car using 7,0 litres per 100 km, with petrol at {_fmt_curr(petrol_price)} per litre.\\n\\n"
        f"1. Calculate the total cost (Fuel + Tolls) for Route 1.\\n"
        f"2. Calculate the total cost (Fuel only) for Route 2.\\n"
        f"3. Which route is financially cheaper, and by how much?"
    )
    ans = f"Route 1 = {_fmt_curr(total_route_1)}; Route 2 = {_fmt_curr(total_route_2)} — {cheaper_route} is cheaper by {_fmt_curr(diff)}"

    s1 = f"Calculate fuel cost for Route 1 ((500÷100)×7,0 = 35 L × R 24,50 = R 857,50) + Tolls (R 280,00) = R 1 137,50. Calculate fuel for Route 2 ((570÷100)×7,0 = 39,9 L × R 24,50 = R 977,55). Compare totals."
    s2 = f"✓ [1 Mark: Method – Calculating both route totals and finding difference]\\nRoute 1 = R 857,50 + R 280,00 = {_fmt_curr(total_route_1)}.\\nRoute 2 = {_fmt_curr(total_route_2)}.\\nDifference = |{_fmt_curr(total_route_1)} − {_fmt_curr(total_route_2)}| = {_fmt_curr(diff)}."
    s3 = f"✓ [1 Mark: Accuracy – Total costs and cheaper route identification]\\n{ans}."

    diagram_spec = {
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
        f"Refer to the long-distance highway strip map below for a journey of **{total_km} km** from Johannesburg to Cape Town.\\n\\n"
        f"South African road safety campaigns (such as Arrive Alive) advise drivers:\\n"
        f"'To combat driver fatigue, stop for at least 15 minutes after every 2 hours of driving or every **200 km**.'\\n\\n"
        f"Calculate the **minimum number of rest stops** {name} must plan during this {total_km} km journey."
    )
    ans = f"{stops} rest stops"

    s1 = f"Divide total distance ({total_km} km) by the recommended rest interval (200 km) and take the integer quotient ({stops} stops before destination)."
    s2 = f"✓ [1 Mark: Method – Dividing total distance by 200 km safety interval]\\nStops = {total_km} km ÷ 200 km = {_fmt(round(total_km / rule_km, 2))} → {stops} stops."
    s3 = f"✓ [1 Mark: Accuracy – Minimum recommended rest stops]\\nStops required = {stops} rest stops."

    diagram_spec = {
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
        f"Refer to the 850 km Karoo highway route map below.\\n\\n"
        f"Vehicle fuel limits:\\n"
        f"• Fuel tank capacity: **{tank_litres} litres** (full at departure)\\n"
        f"• Highway consumption rate: **{_fmt(rate)} litres per 100 km**\\n\\n"
        f"Formula: Maximum Driving Range (km) = (Tank Capacity ÷ Consumption Rate) × 100\\n\\n"
        f"1. Calculate the vehicle's maximum driving range on a full tank (in km).\\n"
        f"2. Can the motorist complete the 850 km trip without refueling?"
    )
    ans = f"Maximum range = {max_range_km} km — No, the motorist cannot complete 850 km without refueling (must refuel before {max_range_km} km)."

    s1 = f"Calculate maximum driving range: ({tank_litres} ÷ {_fmt(rate)}) × 100 = {max_range_km} km. Compare with trip length of 850 km."
    s2 = f"✓ [1 Mark: Method – Range formula setup and comparison with trip length]\\nRange = ({tank_litres} ÷ {_fmt(rate)}) × 100 = {max_range_km} km.\\nComparison: {max_range_km} km < 850 km."
    s3 = f"✓ [1 Mark: Accuracy – Maximum range and refuel necessity verdict]\\n{ans}."

    diagram_spec = {
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
        f"Refer to the SANRAL Average Speed Over Distance (ASOD) route diagram below spanning **{distance_km} km**.\\n\\n"
        f"The maximum legal speed limit in this zone is **{speed_limit} km/h**.\\n\\n"
        f"Calculate the **minimum legal travel time (in minutes)** a driver must take to travel through "
        f"this {distance_km} km zone without exceeding the 120 km/h average speed limit and receiving a speeding fine."
    )
    ans = f"{min_time_mins} minutes"

    s1 = f"Calculate minimum travel time: Distance ÷ Speed Limit = {distance_km} km ÷ {speed_limit} km/h = {_fmt(min_time_hours)} hours. Convert to minutes by multiplying by 60."
    s2 = f"✓ [1 Mark: Method – Time calculation and hour-to-minute conversion]\\nTime = ({distance_km} ÷ {speed_limit}) × 60 = {_fmt(min_time_hours)} × 60."
    s3 = f"✓ [1 Mark: Accuracy – Minimum legal duration in minutes]\\nMinimum time = {min_time_mins} minutes."

    diagram_spec = {
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
        f"Refer to the regional strip map below showing three consecutive towns along a road: Town A, Town B, and Town C.\\n\\n"
        f"Measurements from the map:\\n"
        f"• Total distance from Town A to Town C: **{total_km} km**\\n"
        f"• Distance from Town A to Town B: **{part_km} km**\\n\\n"
        f"Calculate the remaining distance between **Town B and Town C**."
    )
    ans = f"{rem_km} km"

    s1 = f"Subtract the distance of the first segment ({part_km} km) from the total distance ({total_km} km)."
    s2 = f"✓ [1 Mark: Method – Subtraction of intermediate waypoint distance]\\nDistance B to C = {total_km} km − {part_km} km."
    s3 = f"✓ [1 Mark: Accuracy – Remaining segment distance]\\nDistance = {rem_km} km."

    diagram_spec = {
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
        f"Refer to the N8 highway corridor route diagram and signpost below:\\n\\n"
        f"**[ {town1} : {d1} km ]**\\n"
        f"**[ {town2} : {d2} km ]**\\n\\n"
        f"Assuming both cities lie straight ahead along the same N8 route:\\n"
        f"How far is {town2} from {town1}?"
    )
    dist_between = d2 - d1
    ans = f"{dist_between} km"

    s1 = f"Subtract the closer town's distance ({d1} km) from the further town's distance ({d2} km): {d2} − {d1} = {dist_between} km."
    s2 = f"✓ [1 Mark: Method – Subtracting road sign destination distances]\\nDistance = {d2} km − {d1} km."
    s3 = f"✓ [1 Mark: Accuracy – Distance between the two towns]\\nDistance = {dist_between} km."

    diagram_spec = {
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
'''

SEATING_MAPS_CODE = '''"""Cluster 6: Seating Plans & Indoor Layout Maps (Subskills 45 to 52).

Covers:
45. Cinema & theatre seating plans: row letter and seat number coordinate grids
46. Sports stadium seating plans: stands (North/South/East/West), gates, and ticket tiers
47. School classroom & exam hall seating grid layout and desk spacing
48. Commercial aeroplane passenger cabin seating (Window, Middle, and Aisle seats)
49. Event banquet hall seating: round table capacity and floor clearance
50. Shopping mall indoor directory floor plans & retail shop navigation
51. Emergency fire evacuation route planning (shortest exit path and stairs rule)
52. Universal accessibility & wheelchair ramp routes on public building maps
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_map_seat_cinema_theatre_grid_row_seat_number(r: random.Random) -> Dict[str, Any]:
    rows = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K"]
    seats_per_row = r.choice([16, 18, 20])
    row_count = len(rows)
    total_seats = row_count * seats_per_row

    chosen_row = r.choice(["D", "E", "F", "G"])
    chosen_seat = r.randint(4, seats_per_row - 2)

    prompt = (
        f"Study the seating plan diagram below for a community theatre:\\n\\n"
        f"• The auditorium has {row_count} rows labelled from Row A (front row) to Row K (back row).\\n"
        f"• Each row contains exactly {seats_per_row} seats numbered consecutively from Seat 1 on the left to Seat {seats_per_row} on the right.\\n\\n"
        f"1. What is the total seating capacity of the auditorium?\\n"
        f"2. A patron's ticket reads: **Row {chosen_row}, Seat {chosen_seat}**. How many seats are to the right of this patron in the same row?"
    )
    seats_to_right = seats_per_row - chosen_seat
    ans = f"Capacity = {total_seats} seats; {seats_to_right} seats to the right"

    s1 = f"Multiply number of rows ({row_count}) by seats per row ({seats_per_row}) = {total_seats}. Subtract patron's seat number ({chosen_seat}) from row total ({seats_per_row}) to find seats to the right: {seats_per_row} − {chosen_seat} = {seats_to_right}."
    s2 = f"✓ [1 Mark: Method – Capacity multiplication and row subtraction]\\nTotal capacity = {row_count} rows × {seats_per_row} seats = {total_seats}.\\nSeats to right = {seats_per_row} − {chosen_seat} = {seats_to_right}."
    s3 = f"✓ [1 Mark: Accuracy – Total capacity and seats to the right]\\n{ans}."

    diagram_spec = {
        "kind": "seating_plan",
        "title": "Auditorium Seating Plan",
        "rows": rows[:5],
        "seats_per_row": seats_per_row,
        "target_seat": f"Row {chosen_row}, Seat {chosen_seat}",
    }

    return _build_question_payload(
        "map_seat_cinema_theatre_grid_row_seat_number",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Total capacity = {row_count} × {seats_per_row}.",
        tier_2_hint=f"Subtract seat {chosen_seat} from total row width {seats_per_row}.",
        tier_3_hint=f"{ans}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_seat_stadium_stands_turnstiles_gate(r: random.Random) -> Dict[str, Any]:
    stand = r.choice(["North Stand (behind goalposts)", "South Stand", "East Stand (Grandstand)", "West Stand"])
    block = r.randint(101, 125)
    gate = r.choice(["Gate 4", "Gate 7", "Gate 12", "Gate 15"])

    prompt = (
        f"Refer to the stadium perimeter gate and seating plan map below.\\n\\n"
        f"A soccer spectator holds an admission ticket for an international match at FNB Stadium:\\n"
        f"**[ Admission: Gate {gate} | Stand: {stand} | Block: {block} | Seat: 42 ]**\\n\\n"
        f"According to the stadium perimeter map, why must the spectator enter strictly through **{gate}**?"
    )
    ans = f"Gate {gate} is the designated perimeter turnstile providing direct, unblocked access to {stand} Block {block}, preventing overcrowding and security bottlenecks in other stadium quadrants."
    opts = [
        f"Gate {gate} is the designated perimeter turnstile providing direct, unblocked access to {stand} Block {block}, preventing overcrowding and security bottlenecks in other stadium quadrants.",
        "Spectators can enter through any gate if they arrive before kickoff.",
        "Gate numbers correspond to the spectator's home street address.",
        "Tickets are only scanned at gates that sell cold drinks.",
    ]

    s1 = f"Understand crowd control logistics and zonal ingress routing in large sporting venues."
    s2 = f"✓ [1 Mark: Method – Explaining perimeter turnstile routing and crowd safety]\\nDesignated gates guide patrons directly to their assigned block, minimizing pedestrian congestion around the outer concourse."
    s3 = f"✓ [1 Mark: Accuracy – Correct crowd management rationale]\\n{ans}"

    diagram_spec = {
        "kind": "floor_plan",
        "title": "FNB Stadium Perimeter Turnstile Map",
        "rooms": [stand, "North Stand", "South Stand", "Concourse", f"Entrance {gate}"],
        "scale": f"Turnstile {gate}",
    }

    return _build_question_payload(
        "map_seat_stadium_stands_turnstiles_gate",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Why do large stadiums have multiple lettered/numbered gates around the outside?",
        tier_2_hint="Specific gates provide direct access to specific stands to manage crowd flow and safety.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_seat_classroom_exam_hall_spacing(r: random.Random) -> Dict[str, Any]:
    rows = r.choice([5, 6, 7, 8])
    desks_per_row = r.choice([4, 5, 6])
    total_desks = rows * desks_per_row
    spacing_m = 1.2

    prompt = (
        f"Refer to the examination hall seating plan layout diagram below.\\n\\n"
        f"• The hall has {rows} rows of single examination desks.\\n"
        f"• Each row contains {desks_per_row} individual desks.\\n"
        f"• All desks are spaced exactly {_fmt(spacing_m)} m apart from each other in all directions.\\n\\n"
        f"1. Calculate the total number of candidates that can write an examination simultaneously in this hall.\\n"
        f"2. Why do examination regulations mandate a minimum spacing of {_fmt(spacing_m)} m between desks?"
    )
    ans = f"{total_desks} candidates — To prevent candidates from reading each other's answer scripts and to allow invigilators to walk freely between rows"
    opts = [
        f"{total_desks} candidates — To prevent candidates from reading each other's answer scripts and to allow invigilators to walk freely between rows",
        f"{total_desks + 10} candidates — Extra desks are kept for invigilators to sit at.",
        f"{total_desks} candidates — Desks must be spaced apart to prevent sound echoing.",
        f"{total_desks - 5} candidates — Five desks are always reserved for latecomers.",
    ]

    s1 = f"Multiply rows ({rows}) by desks per row ({desks_per_row}) = {total_desks}. Explain exam integrity spacing and invigilator circulation."
    s2 = f"✓ [1 Mark: Method – Grid desk multiplication and exam integrity rationale]\\nTotal = {rows} × {desks_per_row} = {total_desks}.\\nSpacing prevents copying and provides inspection aisles."
    s3 = f"✓ [1 Mark: Accuracy – Total candidate capacity and regulation rationale]\\n{ans}."

    diagram_spec = {
        "kind": "floor_plan",
        "title": f"Examination Hall Grid Layout ({total_desks} Desks)",
        "rooms": [f"Row {i + 1} ({desks_per_row} Desks)" for i in range(min(rows, 5))],
        "scale": f"{_fmt(spacing_m)} m Spacing",
    }

    return _build_question_payload(
        "map_seat_classroom_exam_hall_spacing",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Multiply {rows} rows by {desks_per_row} desks.",
        tier_2_hint=f"Total capacity = {rows} × {desks_per_row} = {total_desks}.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_seat_aeroplane_cabin_window_aisle(r: random.Random) -> Dict[str, Any]:
    row_num = r.randint(10, 28)
    seat_letter = r.choice(["A", "B", "C", "D", "E", "F"])

    if seat_letter in ["A", "F"]:
        seat_type = "Window seat"
        explanation = "Seats A (port/left) and F (starboard/right) are situated directly against the outer cabin fuselage with a window."
    elif seat_letter in ["C", "D"]:
        seat_type = "Aisle seat"
        explanation = "Seats C and D flank the central passenger walking aisle, offering direct access without disturbing other passengers."
    else:
        seat_type = "Middle seat"
        explanation = "Seats B and E are positioned in the middle between the window passenger and aisle passenger."

    prompt = (
        f"Refer to the aircraft passenger cabin seating plan below for a Boeing 737 with a standard 3–3 layout:\\n\\n"
        f"**[ Window | Seat A | Seat B | Seat C | AISLE | Seat D | Seat E | Seat F | Window ]**\\n\\n"
        f"A passenger is assigned seat **'{row_num}{seat_letter}'**.\\n\\n"
        f"Identify whether this is a **Window seat, Middle seat, or Aisle seat**, and describe its position in the cabin."
    )
    ans = f"{seat_type} — {explanation}"
    opts = [
        f"{seat_type} — {explanation}",
        "Cockpit jump seat — Reserved for trainee pilots only.",
        "Cargo hold seat — Situating the passenger under the cabin floor.",
        "Emergency exit row with no seating.",
    ]

    s1 = f"Identify standard commercial aircraft seating layout: A/F = Window, B/E = Middle, C/D = Aisle."
    s2 = f"✓ [1 Mark: Method – Identifying letter position relative to cabin layout]\\nSeat letter {seat_letter} corresponds to {seat_type}."
    s3 = f"✓ [1 Mark: Accuracy – Correct seat classification and cabin position]\\n{ans}."

    diagram_spec = {
        "kind": "seating_plan",
        "title": "Boeing 737 Passenger Cabin Layout",
        "rows": [f"Row {row_num}"],
        "seats_per_row": 6,
        "target_seat": f"Seat {row_num}{seat_letter}",
    }

    return _build_question_payload(
        "map_seat_aeroplane_cabin_window_aisle",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Look at where Seat {seat_letter} sits in the diagram above.",
        tier_2_hint=f"A and F are at the windows; C and D are next to the aisle; B and E are in the middle.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_seat_event_banquet_round_tables(r: random.Random) -> Dict[str, Any]:
    tables = r.choice([12, 15, 18, 20])
    chairs_per_table = r.choice([8, 10])
    head_table_guests = r.choice([10, 12])
    total_guests = (tables * chairs_per_table) + head_table_guests

    prompt = (
        f"Refer to the banquet hall seating layout plan below set up for a matric farewell celebration:\\n\\n"
        f"• The room layout features {tables} identical round guest tables, each seating {chairs_per_table} guests.\\n"
        f"• A raised rectangular Head Table seats exactly {head_table_guests} dignitaries.\\n\\n"
        f"Calculate the total maximum seating capacity of the banquet hall."
    )
    ans = f"{total_guests} guests"

    s1 = f"Multiply the number of round tables ({tables}) by chairs per table ({chairs_per_table}) = {tables * chairs_per_table}, then add the head table guests ({head_table_guests})."
    s2 = f"✓ [1 Mark: Method – Multiplying round table capacity and adding head table]\\nRound tables = {tables} × {chairs_per_table} = {tables * chairs_per_table} guests.\\nTotal capacity = {tables * chairs_per_table} + {head_table_guests}."
    s3 = f"✓ [1 Mark: Accuracy – Total hall capacity]\\nTotal = {total_guests} guests."

    diagram_spec = {
        "kind": "floor_plan",
        "title": f"Matric Farewell Banquet Layout ({total_guests} Guests)",
        "rooms": [
            {"name": f"Guest Tables ({tables})", "dimensions": f"{chairs_per_table} per table"},
            {"name": f"Head Table", "dimensions": f"{head_table_guests} guests"},
            {"name": "Dance Floor", "dimensions": "8 m x 6 m"},
            {"name": "Buffet Area", "dimensions": "10 m x 4 m"},
        ],
        "scale": "1 : 100",
    }

    return _build_question_payload(
        "map_seat_event_banquet_round_tables",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the total at round tables: {tables} × {chairs_per_table} = {tables * chairs_per_table}.",
        tier_2_hint=f"Add the {head_table_guests} head table guests: {tables * chairs_per_table} + {head_table_guests}.",
        tier_3_hint=f"Total capacity = {total_guests} guests.",
        diagram_spec=diagram_spec,
    )


def _gen_map_indoor_shopping_mall_directory_navigation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Refer to the shopping centre floor directory plan diagram below.\\n\\n"
        f"A shopper enters at Entrance Gate 3 on the Ground Floor:\\n"
        f"• Entrance Gate 3 leads into the North Atrium.\\n"
        f"• The Pharmacy (Shop G12) is located immediately to the left of Entrance Gate 3.\\n"
        f"• To reach the Supermarket (Shop G45), the directory states: 'Walk straight past the fountain for 80 metres, "
        f"turn 90° right at the central glass elevator, and proceed 50 metres.'\\n\\n"
        f"Based on this floor directory, describe how a shopper standing at Entrance Gate 3 should navigate to the Supermarket."
    )
    ans = "Walk straight along the main concourse past the fountain for 80 metres, turn 90° right at the central glass elevator, and continue 50 metres straight to the Supermarket entrance."
    opts = [
        "Walk straight along the main concourse past the fountain for 80 metres, turn 90° right at the central glass elevator, and continue 50 metres straight to the Supermarket entrance.",
        "Take the escalator up to the roof parking area and walk across the solar panels.",
        "Turn left into the Pharmacy and exit through the staff back door.",
        "Wait at Entrance Gate 3 for a security guard to carry the shopping bags.",
    ]

    s1 = f"Extract sequential waypoints and directions from an indoor commercial floor plan directory."
    s2 = f"✓ [1 Mark: Method – Sequential navigation path synthesis from directory text]\\nFollow straight path past fountain → turn right at landmark elevator → reach target destination."
    s3 = f"✓ [1 Mark: Accuracy – Clear correct navigation route]\\n{ans}"

    diagram_spec = {
        "kind": "floor_plan",
        "title": "Ground Floor Directory Navigation Plan",
        "rooms": [
            {"name": "Entrance Gate 3", "dimensions": "North Atrium"},
            {"name": "Pharmacy G12", "dimensions": "Left of Entrance"},
            {"name": "Central Elevator", "dimensions": "80 m Straight"},
            {"name": "Supermarket G45", "dimensions": "50 m Right Turn"},
        ],
        "scale": "1 : 200",
    }

    return _build_question_payload(
        "map_indoor_shopping_mall_directory_navigation",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Read the exact directions provided on the directory board.",
        tier_2_hint="The path involves walking straight past the fountain, then turning right at the elevator.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_indoor_evacuation_shortest_emergency_exit(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Refer to the building emergency fire evacuation plan diagram below posted in a corridor.\\n\\n"
        f"When the fire alarm bell sounds, which fundamental safety rule regarding vertical transit must occupants strictly obey?"
    )
    ans = "Always use the fire escape stairwells; NEVER use the passenger elevators/lifts (elevators can lose electrical power, become trapped between floors, or act as chimneys drawing smoke)."
    opts = [
        "Always use the fire escape stairwells; NEVER use the passenger elevators/lifts (elevators can lose electrical power, become trapped between floors, or act as chimneys drawing smoke).",
        "Use the fastest passenger elevator to descend to the ground floor as quickly as possible.",
        "Open all windows on the top floor to create an updraft.",
        "Remain seated at your desk until an SMS notification is received.",
    ]

    s1 = f"Understand building fire safety codes and evacuation diagram protocols (SANS 10400-T regulations)."
    s2 = f"✓ [1 Mark: Method – Technical rationale for prohibiting elevators during fire evacuation]\\nElevators present lethal failure hazards during structural fires due to power cuts, sensor activation, and smoke accumulation in elevator shafts."
    s3 = f"✓ [1 Mark: Accuracy – Correct evacuation rule and motivation]\\n{ans}"

    diagram_spec = {
        "kind": "floor_plan",
        "title": "Corridor Emergency Fire Evacuation Plan",
        "rooms": [
            {"name": "Office Corridor", "dimensions": "Active Zone"},
            {"name": "Fire Stairwell 1", "dimensions": "Emergency Exit"},
            {"name": "Fire Stairwell 2", "dimensions": "Emergency Exit"},
            {"name": "Elevator Lobby", "dimensions": "DO NOT USE"},
        ],
        "scale": "SANS 10400-T Standard",
    }

    return _build_question_payload(
        "map_indoor_evacuation_shortest_emergency_exit",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What happens to electric elevators if a building's power cuts during a fire?",
        tier_2_hint="Elevators can trap passengers or fill with smoke; stairwells are protected fire escapes.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_indoor_universal_wheelchair_accessibility(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Refer to the municipal library universal accessibility floor plan below.\\n\\n"
        f"Which architectural feature on the plan allows a wheelchair user to access a raised library reading "
        f"terrace located 1,5 metres above the main ground floor entrance without encountering stairs?"
    )
    ans = "A gently sloped access ramp (with a maximum gradient of 1 : 12 and safety handrails) or an accessible passenger platform lift"
    opts = [
        "A gently sloped access ramp (with a maximum gradient of 1 : 12 and safety handrails) or an accessible passenger platform lift",
        "A steep flight of concrete stairs with non-slip nosing",
        "An overhead rope ladder with climbing harnesses",
        "An outdoor fire escape spiral metal staircase",
    ]

    s1 = f"Identify universal accessibility standards (SANS 10400-S) on public building architectural plans: ramps with gradient ≤ 1:12, elevators, and wide doorways."
    s2 = f"✓ [1 Mark: Method – Identifying step-free architectural access elements]\\nRamps and platform lifts provide barrier-free vertical transit for wheeled mobility devices."
    s3 = f"✓ [1 Mark: Accuracy – Correct accessibility feature identification]\\nFeature: {ans}."

    diagram_spec = {
        "kind": "floor_plan",
        "title": "Municipal Library Universal Accessibility Plan",
        "rooms": [
            {"name": "Ground Floor Entrance", "dimensions": "0,0 m Level"},
            {"name": "Access Ramp", "dimensions": "1 : 12 Gradient"},
            {"name": "Reading Terrace", "dimensions": "+1,5 m Level"},
            {"name": "Main Staircase", "dimensions": "Flight of Stairs"},
        ],
        "scale": "SANS 10400-S Standard",
    }

    return _build_question_payload(
        "map_indoor_universal_wheelchair_accessibility",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="How can a person in a wheelchair move between different floor levels?",
        tier_2_hint="Ramps with gentle slopes and platform lifts allow step-free access.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )
'''

(BASE / "strip_maps_road_routes.py").write_text(STRIP_MAPS_CODE, encoding="utf-8")
(BASE / "seating_indoor_maps.py").write_text(SEATING_MAPS_CODE, encoding="utf-8")
print("Successfully updated strip_maps_road_routes.py and seating_indoor_maps.py")
