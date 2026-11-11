"""Cluster 4: Travel Distance, Speed, Time & Fuel Economics (Subskills 27 to 35).

Covers:
27. Travel time calculation from distance and speed (Time = Distance ÷ Speed)
28. Fractional decimal hours conversion to hours and minutes (0,4 h = 24 min, not 40 min)
29. Average speed determination (Speed = Distance ÷ Time)
30. Departure and arrival clock time estimation including rest stops
31. Fuel consumption calculation using Litres per 100 km rate
32. Total fuel cost calculation based on prevailing fuel pump price per litre
33. Fuel economy comparison between two vehicles over an identical route
34. Comprehensive road trip budget (fuel, toll plazas, refreshments)
35. Carpooling cost-sharing per passenger vs commercial public bus fares
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    SA_TOWNS,
    _fmt,
    _fmt_curr,
    _build_question_payload,
)


def _gen_map_travel_time_calculation_distance_speed(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    distance_km = r.choice([360, 400, 440, 480, 550, 600])
    speed_kmh = r.choice([80, 100, 110, 120])
    raw_hours = distance_km / speed_kmh
    whole_hours = int(raw_hours)
    rem_mins = round((raw_hours - whole_hours) * 60)

    prompt = (
        f"Refer to the road travel route diagram below.\n\n"
        f"{name} drives from Johannesburg to a holiday destination at an average speed of **{speed_kmh} km/h**.\n"
        f"The total driving distance is **{distance_km} km**.\n\n"
        f"Formula: Time = Distance ÷ Average Speed\n\n"
        f"Calculate the travel time in hours and minutes."
    )
    ans = f"{whole_hours} hours {rem_mins} minutes"

    s1 = f"Divide total distance ({distance_km} km) by average speed ({speed_kmh} km/h) to get decimal hours ({_fmt(round(raw_hours, 3))} hours). Convert fractional hours to minutes by multiplying by 60."
    s2 = f"✓ [1 Mark: Method – Distance divided by speed and converting decimal to minutes]\nTime = {distance_km} ÷ {speed_kmh} = {_fmt(round(raw_hours, 2))} hours.\nMinutes = {_fmt(round(raw_hours - whole_hours, 2))} × 60 = {rem_mins} minutes."
    s3 = f"✓ [1 Mark: Accuracy – Travel time in hours and minutes]\nTime = {whole_hours} hours {rem_mins} minutes."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Holiday Road Trip Corridor",
        "stops": [
            {"name": "Johannesburg", "km": 0},
            {"name": "Destination", "km": distance_km},
        ],
        "scale": f"Speed: {speed_kmh} km/h",
    }

    return _build_question_payload(
        "map_travel_time_calculation_distance_speed",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide distance ({distance_km} km) by speed ({speed_kmh} km/h).",
        tier_2_hint=f"{distance_km} ÷ {speed_kmh} = {_fmt(round(raw_hours, 2))} hours. Multiply the decimal part by 60 for minutes.",
        tier_3_hint=f"Time = {whole_hours} hours {rem_mins} minutes.",
        diagram_spec=diagram_spec,
    )


def _gen_map_travel_time_fractional_hours_to_hours_minutes(r: random.Random) -> Dict[str, Any]:
    whole_h = r.randint(2, 5)
    dec_part = r.choice([0.15, 0.25, 0.35, 0.40, 0.45, 0.65, 0.75, 0.85])
    total_dec = whole_h + dec_part
    mins = round(dec_part * 60)

    prompt = (
        f"Refer to the travel route duration diagram below.\n\n"
        f"A calculator display shows a travel duration of **{_fmt(total_dec)} hours**.\n\n"
        f"A common student mistake is to write '{whole_h} hours {int(dec_part * 100)} minutes'.\n\n"
        f"Convert **{_fmt(total_dec)} hours** into exact **hours and minutes**, and explain why the decimal "
        f"cannot simply be read as minutes."
    )
    ans = f"{whole_h} hours {mins} minutes — Because there are 60 minutes in an hour, not 100; so {dec_part} must be multiplied by 60 ({dec_part} × 60 = {mins} min)."
    opts = [
        f"{whole_h} hours {mins} minutes — Because there are 60 minutes in an hour, not 100; so {dec_part} must be multiplied by 60 ({dec_part} × 60 = {mins} min).",
        f"{whole_h} hours {int(dec_part * 100)} minutes — Decimal points match minutes directly.",
        f"{whole_h + 1} hours {mins} minutes — Minutes must be rounded up to the next full hour.",
        f"{whole_h} hours {mins // 2} minutes — Minutes are divided by 2 for daylight saving time.",
    ]

    s1 = f"Multiply the decimal fraction ({dec_part}) by 60 minutes (the base-60 sexagesimal system of time) rather than treating it as a base-10 percentage."
    s2 = f"✓ [1 Mark: Method – Multiplying fractional hours by 60]\nMinutes = {dec_part} × 60 = {mins} minutes."
    s3 = f"✓ [1 Mark: Accuracy – Converted hours and minutes with base-60 rationale]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Travel Route Duration Indicator",
        "stops": [
            {"name": "Start", "km": 0},
            {"name": "Midpoint", "km": 100},
            {"name": "Destination", "km": 200},
        ],
        "scale": f"Total Duration: {_fmt(total_dec)} hours",
    }

    return _build_question_payload(
        "map_travel_time_fractional_hours_to_hours_minutes",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Multiply the decimal part ({dec_part}) by 60.",
        tier_2_hint=f"{dec_part} × 60 = {mins} minutes.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_travel_average_speed_calculation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    distance_km = r.choice([270, 315, 360, 420, 450, 495])
    hours = r.choice([3.0, 3.5, 4.0, 4.5, 5.0])
    speed = round(distance_km / hours, 1)

    prompt = (
        f"Refer to the delivery van route diagram below.\n\n"
        f"{name} drives a delivery van across a distance of **{distance_km} km** in **{_fmt(hours)} hours**.\n\n"
        f"Formula: Average Speed = Total Distance ÷ Total Time\n\n"
        f"Calculate {name}'s average driving speed in **kilometres per hour (km/h)**."
    )
    ans = f"{_fmt(speed)} km/h"

    s1 = f"Divide the total distance ({distance_km} km) by the travel time ({_fmt(hours)} hours)."
    s2 = f"✓ [1 Mark: Method – Speed formula substitution]\nSpeed = {distance_km} km ÷ {_fmt(hours)} h."
    s3 = f"✓ [1 Mark: Accuracy – Average speed in km/h]\nSpeed = {_fmt(speed)} km/h."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Delivery Van Transit Route",
        "stops": [
            {"name": "Dispatch Depot", "km": 0},
            {"name": "Client Delivery Hub", "km": distance_km},
        ],
        "scale": f"Time: {_fmt(hours)} hours",
    }

    return _build_question_payload(
        "map_travel_average_speed_calculation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide distance ({distance_km}) by time ({_fmt(hours)}).",
        tier_2_hint=f"{distance_km} ÷ {_fmt(hours)} = {_fmt(speed)}.",
        tier_3_hint=f"Speed = {_fmt(speed)} km/h.",
        diagram_spec=diagram_spec,
    )


def _gen_map_travel_arrival_time_with_rest_stops(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    dep_h = r.randint(5, 8)
    dep_m = r.choice([0, 15, 30, 45])
    drive_h = r.randint(3, 5)
    drive_m = r.choice([15, 30, 45])
    rest_m = r.choice([30, 45, 60])

    total_m_added = (drive_h * 60) + drive_m + rest_m
    dep_total_m = (dep_h * 60) + dep_m
    arrival_total_m = dep_total_m + total_m_added
    arr_h = arrival_total_m // 60
    arr_m = arrival_total_m % 60

    prompt = (
        f"Refer to the road trip corridor itinerary below.\n\n"
        f"{name} plans a road trip from Pretoria to Durban:\n"
        f"• Departure time: **{dep_h:02d}:{dep_m:02d}** in the morning\n"
        f"• Actual driving time: **{drive_h} hours and {drive_m} minutes**\n"
        f"• Scheduled rest and refueling stops: **{rest_m} minutes** in total\n\n"
        f"Determine {name}'s estimated arrival time in Durban using the 24-hour clock format (hh:mm)."
    )
    ans = f"{arr_h:02d}:{arr_m:02d}"

    s1 = f"Add the driving duration ({drive_h} h {drive_m} min) and rest stop duration ({rest_m} min) to the departure time ({dep_h:02d}:{dep_m:02d})."
    s2 = f"✓ [1 Mark: Method – Adding driving time and rest stops to departure time]\nTotal trip duration = {drive_h} h {drive_m} min + {rest_m} min = {total_m_added // 60} h {total_m_added % 60} min.\nArrival = {dep_h:02d}:{dep_m:02d} + {total_m_added // 60} h {total_m_added % 60} min."
    s3 = f"✓ [1 Mark: Accuracy – Final arrival time in 24-hour format]\nArrival time = {arr_h:02d}:{arr_m:02d}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Pretoria to Durban Highway Itinerary",
        "stops": [
            {"name": "Pretoria (Dep)", "km": 0},
            {"name": "Harrismith Rest Stop", "km": 280},
            {"name": "Durban (Arr)", "km": 580},
        ],
        "scale": f"Departure: {dep_h:02d}:{dep_m:02d}",
    }

    return _build_question_payload(
        "map_travel_arrival_time_with_rest_stops",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Add driving time ({drive_h} h {drive_m} min) and rest time ({rest_m} min) together first.",
        tier_2_hint=f"Add total duration ({total_m_added // 60} h {total_m_added % 60} min) to departure time of {dep_h:02d}:{dep_m:02d}.",
        tier_3_hint=f"Arrival time = {arr_h:02d}:{arr_m:02d}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_fuel_consumption_litres_per_hundred_km(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    distance_km = r.choice([350, 420, 480, 550, 620, 750])
    consumption_rate = r.choice([6.2, 6.8, 7.5, 8.0, 8.5, 9.2])
    litres_needed = round((distance_km / 100.0) * consumption_rate, 2)

    prompt = (
        f"Refer to the fuel consumption graph below for a journey across the Free State.\n\n"
        f"{name} is planning a {distance_km} km journey.\n"
        f"• Highway fuel consumption rate: **{_fmt(consumption_rate)} litres per 100 km**.\n\n"
        f"Formula: Fuel (Litres) = (Distance ÷ 100) × Fuel Consumption Rate\n\n"
        f"Calculate the total volume of fuel (in litres) required for this journey (rounded to 2 decimal places)."
    )
    ans = f"{_fmt(litres_needed)} litres"

    s1 = f"Divide total distance ({distance_km} km) by 100 to find the number of 100 km segments, then multiply by the consumption rate ({_fmt(consumption_rate)} L/100 km)."
    s2 = f"✓ [1 Mark: Method – Fuel formula substitution]\nFuel = ({distance_km} ÷ 100) × {_fmt(consumption_rate)} = {_fmt(distance_km / 100)} × {_fmt(consumption_rate)}."
    s3 = f"✓ [1 Mark: Accuracy – Total litres of fuel]\nFuel required = {_fmt(litres_needed)} litres."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": "Fuel Consumption Rate Graph",
        "lines": [{
            "label": f"{_fmt(consumption_rate)} L / 100 km",
            "points": [[0, 0], [100, consumption_rate], [distance_km, litres_needed]],
        }],
        "points_of_interest": [
            {"x": distance_km, "y": litres_needed, "label": f"{_fmt(litres_needed)} L"},
        ],
        "x_range": [0, distance_km + 50],
        "y_range": [0, round(litres_needed + 10)],
        "x_label": "Distance (km)",
        "y_label": "Fuel Consumed (Litres)",
    }

    return _build_question_payload(
        "map_fuel_consumption_litres_per_hundred_km",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {distance_km} by 100 = {_fmt(distance_km / 100)}.",
        tier_2_hint=f"Multiply {_fmt(distance_km / 100)} by {_fmt(consumption_rate)}.",
        tier_3_hint=f"Fuel required = {_fmt(litres_needed)} litres.",
        diagram_spec=diagram_spec,
    )


def _gen_map_fuel_total_cost_calculation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    litres = r.choice([42.5, 48.0, 52.5, 55.0, 60.0])
    petrol_price = r.choice([23.85, 24.20, 24.50, 25.10, 25.45])
    total_cost = round(litres * petrol_price, 2)

    prompt = (
        f"Refer to the fuel cost relationship graph below for a journey from Bloemfontein to East London.\n\n"
        f"{name} fills up the tank before driving.\n"
        f"The journey requires a total of **{_fmt(litres)} litres** of Unleaded 95 petrol.\n"
        f"The fuel pump price at the garage is **{_fmt_curr(petrol_price)} per litre**.\n\n"
        f"Calculate the total cost of fuel for this journey in Rands."
    )
    ans = _fmt_curr(total_cost)

    s1 = f"Multiply the volume of fuel ({_fmt(litres)} litres) by the pump price per litre ({_fmt_curr(petrol_price)})."
    s2 = f"✓ [1 Mark: Method – Multiplying litres by price per litre]\nCost = {_fmt(litres)} litres × {_fmt_curr(petrol_price)}."
    s3 = f"✓ [1 Mark: Accuracy – Total Rand cost to 2 decimal places]\nTotal Cost = {_fmt_curr(total_cost)}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": "Fuel Expenditure Cost Curve",
        "lines": [{
            "label": f"{_fmt_curr(petrol_price)} / L",
            "points": [[0, 0], [10, round(10 * petrol_price, 2)], [litres, total_cost]],
        }],
        "points_of_interest": [
            {"x": litres, "y": total_cost, "label": _fmt_curr(total_cost)},
        ],
        "x_range": [0, round(litres + 10)],
        "y_range": [0, round(total_cost + 100)],
        "x_label": "Fuel Volume (Litres)",
        "y_label": "Total Cost (R)",
    }

    return _build_question_payload(
        "map_fuel_total_cost_calculation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Multiply {_fmt(litres)} litres by {_fmt_curr(petrol_price)}.",
        tier_2_hint=f"{_fmt(litres)} × {_fmt(petrol_price)}.",
        tier_3_hint=f"Total cost = {_fmt_curr(total_cost)}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_fuel_economy_comparison_two_vehicles(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    dist_km = r.choice([240, 300, 360, 420, 500])
    fuel_rate_A = r.choice([6.5, 7.0, 7.5])   # litres per 100 km (small hatchback)
    fuel_rate_B = r.choice([9.5, 10.0, 11.5])  # litres per 100 km (large SUV)
    litres_A = round((dist_km / 100.0) * fuel_rate_A, 2)
    litres_B = round((dist_km / 100.0) * fuel_rate_B, 2)
    fuel_saved = round(litres_B - litres_A, 2)

    prompt = (
        f"{name} is planning a road trip of {_fmt(dist_km)} km and compares the fuel consumption of two vehicles.\n"
        f"• Vehicle A (Hatchback) has a fuel consumption rate of {_fmt(fuel_rate_A)} L per 100 km.\n"
        f"• Vehicle B (SUV) has a fuel consumption rate of {_fmt(fuel_rate_B)} L per 100 km.\n\n"
        f"Refer to the route fuel profile below.\n\n"
        f"Calculate how many litres of fuel {name} will save by driving Vehicle A instead of Vehicle B for this trip."
    )
    ans = f"{_fmt(fuel_saved)} litres"

    s1 = f"Calculate fuel needed for each vehicle: Fuel = (Distance ÷ 100) × Rate per 100 km, then subtract."
    s2 = f"✓ [1 Mark: Method – Calculating consumption for both vehicles and difference]\nVehicle A = ({_fmt(dist_km)} ÷ 100) × {_fmt(fuel_rate_A)} = {_fmt(litres_A)} L.\nVehicle B = ({_fmt(dist_km)} ÷ 100) × {_fmt(fuel_rate_B)} = {_fmt(litres_B)} L.\nDifference = {_fmt(litres_B)} − {_fmt(litres_A)}."
    s3 = f"✓ [1 Mark: Accuracy – Total fuel saved in litres]\nFuel saved = {_fmt(fuel_saved)} litres."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Route Fuel Profile ({name}: {_fmt(dist_km)} km)",
        "stops": [
            {"name": "Departure", "km": 0},
            {"name": "Destination", "km": dist_km},
        ],
    }

    return _build_question_payload(
        "map_fuel_economy_comparison_two_vehicles",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find fuel for Vehicle A: ({_fmt(dist_km)} ÷ 100) × {_fmt(fuel_rate_A)} = {_fmt(litres_A)} L.",
        tier_2_hint=f"Find fuel for Vehicle B: ({_fmt(dist_km)} ÷ 100) × {_fmt(fuel_rate_B)} = {_fmt(litres_B)} L.",
        tier_3_hint=f"{_fmt(litres_B)} − {_fmt(litres_A)} = {_fmt(fuel_saved)} litres.",
        diagram_spec=diagram_spec,
    )

    litres_sedan = (distance_km / 100) * rate_sedan  # 36 L
    cost_sedan = litres_sedan * price_per_l          # R 882.00

    litres_suv = (distance_km / 100) * rate_suv      # 57 L
    cost_suv = litres_suv * price_per_l              # R 1 396.50

    diff_cost = cost_suv - cost_sedan                # R 514.50

    prompt = (
        f"Refer to the return trip route diagram below.\n\n"
        f"A family compares the fuel costs of driving two different cars for a {distance_km} km return trip:\n"
        f"• Car A (Hatchback): 6,0 litres per 100 km\n"
        f"• Car B (4x4 SUV): 9,5 litres per 100 km\n\n"
        f"Assume a fixed petrol price of {_fmt_curr(price_per_l)} per litre.\n\n"
        f"1. Calculate the fuel cost for Car A.\n"
        f"2. Calculate the fuel cost for Car B.\n"
        f"3. How much money will the family save by choosing Car A instead of Car B?"
    )
    ans = f"Car A: {_fmt_curr(cost_sedan)}; Car B: {_fmt_curr(cost_suv)} — Savings = {_fmt_curr(diff_cost)}"

    s1 = f"Calculate litres and cost for Car A ((600÷100)×6,0 = 36 L × R 24,50 = R 882,00) and Car B ((600÷100)×9,5 = 57 L × R 24,50 = R 1 396,50), then subtract to find savings."
    s2 = f"✓ [1 Mark: Method – Calculating both fuel costs and subtracting]\nCar A = 36 L × R 24,50 = R 882,00.\nCar B = 57 L × R 24,50 = R 1 396,50.\nSavings = R 1 396,50 − R 882,00."
    s3 = f"✓ [1 Mark: Accuracy – Individual costs and total savings]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Comparison Route ({distance_km} km Return Trip)",
        "stops": [
            {"name": "Home Base", "km": 0},
            {"name": "Holiday Destination", "km": distance_km // 2},
            {"name": "Return Home", "km": distance_km},
        ],
        "scale": f"Fuel: {_fmt_curr(price_per_l)} / L",
    }

    return _build_question_payload(
        "map_fuel_economy_comparison_two_vehicles",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Car A needs 36 litres; Car B needs 57 litres.",
        tier_2_hint=f"Cost A = 36 × R 24,50 = {_fmt_curr(cost_sedan)}; Cost B = 57 × R 24,50 = {_fmt_curr(cost_suv)}.",
        tier_3_hint=f"Savings = {_fmt_curr(diff_cost)}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_travel_total_trip_budget_fuel_tolls(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    fuel_cost = r.choice([850.0, 920.0, 1050.0, 1150.0])
    tolls_cost = r.choice([210.0, 265.0, 315.0, 380.0])
    meals_cost = r.choice([150.0, 200.0, 250.0])
    total_budget = fuel_cost + tolls_cost + meals_cost

    prompt = (
        f"Refer to the N3 highway corridor route diagram below.\n\n"
        f"{name} prepares an itemised road trip budget for travelling between Johannesburg and Durban:\n"
        f"• Projected fuel cost: {_fmt_curr(fuel_cost)}\n"
        f"• Highway toll plaza fees (De Hoek, Wilge, Tugela, Mooi River): {_fmt_curr(tolls_cost)}\n"
        f"• Refreshments and meals at roadside service stops: {_fmt_curr(meals_cost)}\n\n"
        f"Calculate the total road trip expenditure budget in Rands."
    )
    ans = _fmt_curr(total_budget)

    s1 = f"Sum all three cost components: Fuel ({_fmt_curr(fuel_cost)}) + Tolls ({_fmt_curr(tolls_cost)}) + Meals ({_fmt_curr(meals_cost)})."
    s2 = f"✓ [1 Mark: Method – Adding fuel, tolls, and refreshments]\nTotal = {_fmt_curr(fuel_cost)} + {_fmt_curr(tolls_cost)} + {_fmt_curr(meals_cost)}."
    s3 = f"✓ [1 Mark: Accuracy – Total trip budget]\nTotal Cost = {_fmt_curr(total_budget)}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Johannesburg to Durban N3 Corridor",
        "stops": [
            {"name": "Johannesburg", "km": 0},
            {"name": "Wilge Toll Plaza", "km": 160},
            {"name": "Tugela Plaza", "km": 370},
            {"name": "Durban", "km": 580},
        ],
        "scale": f"Tolls: {_fmt_curr(tolls_cost)}",
    }

    return _build_question_payload(
        "map_travel_total_trip_budget_fuel_tolls",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Add fuel, toll fees, and food together.",
        tier_2_hint=f"{_fmt_curr(fuel_cost)} + {_fmt_curr(tolls_cost)} + {_fmt_curr(meals_cost)}.",
        tier_3_hint=f"Total = {_fmt_curr(total_budget)}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_travel_carpooling_vs_bus_cost_per_person(r: random.Random) -> Dict[str, Any]:
    passengers = 4
    total_car_cost = r.choice([1200.0, 1400.0, 1600.0, 1800.0])
    car_per_person = round(total_car_cost / passengers, 2)
    bus_ticket = r.choice([420.0, 450.0, 480.0, 520.0])

    prompt = (
        f"Refer to the travel corridor route diagram below between Pretoria and Polokwane.\n\n"
        f"A group of {passengers} friends plan to travel together:\n"
        f"• Option 1 (Carpooling): Total cost of fuel and highway tolls for one car is {_fmt_curr(total_car_cost)}, shared equally among all {passengers} passengers.\n"
        f"• Option 2 (Intercity Bus): A commercial bus ticket costs {_fmt_curr(bus_ticket)} per person.\n\n"
        f"1. Calculate the cost per person for carpooling in Option 1.\n"
        f"2. Which option is cheaper per person and by how much?"
    )
    diff = abs(bus_ticket - car_per_person)
    cheaper = "Option 1 (Carpooling)" if car_per_person < bus_ticket else "Option 2 (Intercity Bus)"
    ans = f"Carpooling cost per person = {_fmt_curr(car_per_person)} — {cheaper} is cheaper by {_fmt_curr(diff)} per person"

    s1 = f"Divide total car cost ({_fmt_curr(total_car_cost)}) by {passengers} passengers ({_fmt_curr(car_per_person)}), then compare with bus ticket ({_fmt_curr(bus_ticket)})."
    s2 = f"✓ [1 Mark: Method – Dividing carpool cost by passengers and finding difference]\nCost per person = {_fmt_curr(total_car_cost)} ÷ {passengers} = {_fmt_curr(car_per_person)}.\nDifference = |{_fmt_curr(bus_ticket)} − {_fmt_curr(car_per_person)}| = {_fmt_curr(diff)}."
    s3 = f"✓ [1 Mark: Accuracy – Per-person carpool cost and comparison verdict]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": "Pretoria to Polokwane Highway Corridor",
        "stops": [
            {"name": "Pretoria", "km": 0},
            {"name": "Nyl Plaza", "km": 140},
            {"name": "Polokwane", "km": 260},
        ],
        "scale": f"Carpool Total: {_fmt_curr(total_car_cost)}",
    }

    return _build_question_payload(
        "map_travel_carpooling_vs_bus_cost_per_person",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {_fmt_curr(total_car_cost)} by {passengers} to get carpool cost per person.",
        tier_2_hint=f"{_fmt_curr(total_car_cost)} ÷ {passengers} = {_fmt_curr(car_per_person)}. Compare with bus fare {_fmt_curr(bus_ticket)}.",
        tier_3_hint=f"{ans}.",
        diagram_spec=diagram_spec,
    )
