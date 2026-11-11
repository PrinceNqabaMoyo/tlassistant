"""Subskills 19 to 27: Travel Time, Speed, Fuel Consumption & Journey Costing for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Subskill 19: Travel time calculation: t = d / v in hours and minutes."""
    name = r.choice(SA_NAMES)
    speed_kmh = r.choice([80, 90, 100, 120])
    # Pick distance with clean minutes (e.g. 2.25 h, 2.5 h, 3.25 h, 3.5 h)
    time_hours_float = r.choice([2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 4.0, 4.5])
    dist_km = int(speed_kmh * time_hours_float)

    h = int(time_hours_float)
    m = int(round((time_hours_float - h) * 60))

    prompt = (
        f"{name} drives a delivery bakkie along the N3 highway from Johannesburg towards Durban. "
        f"The travel distance is {_fmt(dist_km)} km and the vehicle maintains a constant average speed of "
        f"{_fmt(speed_kmh)} km/h with no stops.\n"
        f"Calculate the total travel time in hours and minutes."
    )

    correct_ans = f"{h} hours and {m} minutes" if m > 0 else f"{h} hours"
    wrong_1 = f"{h + 1} hours and {m} minutes"
    wrong_2 = f"{h} hours and {m + 15} minutes"
    wrong_3 = f"{h - 1} hours and {m} minutes"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State the time formula [1 mark].\n"
        f"\\text{{Time}} = \\frac{{\\text{{Distance}}}}{{\\text{{Speed}}}} = \\frac{{{dist_km}}}{{{speed_kmh}}} = {_fmt(time_hours_float)} \\text{{ hours}}.\n"
        f"Step 2: Convert decimal fraction of an hour to minutes [1 mark].\n"
        f"{_fmt(time_hours_float - h)} \\text{{ hours}} \\times 60 \\text{{ min/hour}} = {m} \\text{{ minutes}}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="19",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Time = Distance ÷ Speed. Multiply the decimal part of the hour by 60 to find minutes.",
        tier_2=f"{dist_km} ÷ {speed_kmh} = {_fmt(time_hours_float)} hours. {h} hours and ({time_hours_float - h} × 60) minutes.",
        tier_3=f"Travel time: {correct_ans}.",
        r=r,
    )


def generate_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Subskill 20: Arrival time calculation including rest stops."""
    name = r.choice(SA_NAMES)
    dep_h = r.choice([6, 7, 8])
    dep_m = r.choice([0, 15, 30])
    drive_h = r.choice([3, 4])
    drive_m = r.choice([15, 30, 45])
    rest_m = r.choice([30, 45, 60])

    # Total minutes from midnight
    total_dep_mins = dep_h * 60 + dep_m
    total_journey_mins = drive_h * 60 + drive_m + rest_m
    arr_mins = total_dep_mins + total_journey_mins

    arr_h = (arr_mins // 60) % 24
    arr_m = arr_mins % 60
    arr_str = f"{arr_h:02d}:{arr_m:02d}"

    prompt = (
        f"{name} departs on a family holiday road trip at {dep_h:02d}:{dep_m:02d}. "
        f"The actual driving time is {drive_h} hours and {drive_m} minutes. "
        f"Along the route, the family takes a scheduled rest and meal stop of {rest_m} minutes at a petrol station.\n"
        f"At what time will the family arrive at their destination?"
    )

    correct_ans = arr_str
    wrong_1 = f"{(arr_h + 1) % 24:02d}:{arr_m:02d}"
    wrong_2 = f"{arr_h:02d}:{(arr_m + 15) % 60:02d}"
    wrong_3 = f"{(arr_h - 1) % 24:02d}:{arr_m:02d}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate total elapsed journey duration [1 mark].\n"
        f"Driving = {drive_h} h {drive_m} min; Rest stop = {rest_m} min.\n"
        f"Total duration = {drive_h} h + ({drive_m} + {rest_m}) min = {drive_h} h {drive_m + rest_m} min = "
        f"{drive_h + (drive_m + rest_m) // 60} h {(drive_m + rest_m) % 60} min.\n"
        f"Step 2: Add total duration to departure time ({dep_h:02d}:{dep_m:02d}) [1 mark].\n"
        f"{dep_h:02d}:{dep_m:02d} + {total_journey_mins // 60} h {total_journey_mins % 60} min = {arr_str}.\n"
        f"Step 3: Stated arrival time [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="20",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add driving time and rest time to the departure time.",
        tier_2=f"Total trip time = {drive_h} h {drive_m} min + {rest_m} min. Add to {dep_h:02d}:{dep_m:02d}.",
        tier_3=f"Arrival time = {arr_str}.",
        r=r,
    )


def generate_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Average speed calculation: v = d / t (distinguishing driving vs elapsed time)."""
    name = r.choice(SA_NAMES)
    dist_km = r.choice([320, 360, 400, 450, 480])
    driving_hours = r.choice([4.0, 4.5, 5.0])
    rest_hours = 0.5  # 30 min rest

    speed_driving = round(dist_km / driving_hours, 1)
    speed_overall = round(dist_km / (driving_hours + rest_hours), 1)

    prompt = (
        f"{name} travels a total distance of {_fmt(dist_km)} km. "
        f"The journey takes {driving_hours} hours of actual driving plus a 30-minute ({_fmt(rest_hours)} hour) lunch break "
        f"(total elapsed trip time = {_fmt(driving_hours + rest_hours)} hours).\n"
        f"Calculate {name}'s average speed while the vehicle was ACTUALLY DRIVING in km/h."
    )

    correct_ans = f"{_fmt(speed_driving, 1)} km/h"
    wrong_1 = f"{_fmt(speed_overall, 1)} km/h"  # divided by total time instead of driving time
    wrong_2 = f"{_fmt(speed_driving + 15.0, 1)} km/h"
    wrong_3 = f"{_fmt(speed_driving - 10.0, 1)} km/h"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify the correct time value to use [1 mark].\n"
        f"The question asks for speed while 'actually driving', so use driving time ({driving_hours} h), excluding the break.\n"
        f"Step 2: Apply the speed formula [1 mark].\n"
        f"Average Driving Speed = Distance ÷ Driving Time = {_fmt(dist_km)} km ÷ {driving_hours} h = {_fmt(speed_driving, 1)} km/h.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="21",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Speed = Distance ÷ Time. Divide by the driving time alone, excluding the rest stop.",
        tier_2=f"Divide {_fmt(dist_km)} km by {driving_hours} hours.",
        tier_3=f"Average driving speed = {_fmt(speed_driving, 1)} km/h.",
        r=r,
    )


def generate_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Subskill 22: Required average speed to arrive by appointment deadline."""
    name = r.choice(SA_NAMES)
    dist_km = r.choice([180, 210, 240, 260])
    avail_hours = r.choice([2.0, 2.5, 3.0])

    req_speed = round(dist_km / avail_hours, 1)

    prompt = (
        f"{name} has an important job interview in a city {_fmt(dist_km)} km away. "
        f"Due to morning traffic delays, {name} only has {_fmt(avail_hours)} hours remaining before the interview starts.\n"
        f"What minimum constant average speed (in km/h) must {name} maintain to arrive exactly on time?"
    )

    correct_ans = f"{_fmt(req_speed, 1)} km/h"
    wrong_1 = f"{_fmt(req_speed + 15.0, 1)} km/h"
    wrong_2 = f"{_fmt(req_speed - 12.0, 1)} km/h"
    wrong_3 = f"{_fmt(dist_km * 0.5, 1)} km/h"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State speed formula [1 mark].\n"
        f"Required Speed = Distance ÷ Available Time = {_fmt(dist_km)} km ÷ {_fmt(avail_hours)} h.\n"
        f"Step 2: Perform division [1 mark].\n"
        f"Speed = {_fmt(dist_km / avail_hours, 1)} km/h.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="22",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the distance by the remaining time to find the required speed.",
        tier_2=f"{_fmt(dist_km)} km ÷ {_fmt(avail_hours)} hours = {_fmt(req_speed, 1)} km/h.",
        tier_3=f"Required speed = {_fmt(req_speed, 1)} km/h.",
        r=r,
    )


def generate_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Subskill 23: Fuel consumption calculation in litres from rate (L/100 km)."""
    name = r.choice(SA_NAMES)
    dist_km = r.choice([350, 420, 500, 560, 640])
    rate_per_100 = r.choice([6.5, 7.0, 7.5, 8.0, 8.5])

    fuel_litres = round((dist_km / 100) * rate_per_100, 1)

    prompt = (
        f"{name}'s car has a fuel consumption rate of {_fmt(rate_per_100, 1)} litres per 100 km. "
        f"{name} plans to drive a distance of {_fmt(dist_km)} km.\n"
        f"Calculate the total volume of petrol (in litres) the car will consume for this trip."
    )

    correct_ans = f"{_fmt(fuel_litres, 1)} litres"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: State the fuel consumption formula [1 mark].\n"
        f"\\text{{Fuel}} = \\left( \\frac{{\\text{{Distance}}}}{{100}} \\right) \\times \\text{{Rate}} = "
        f"\\left( \\frac{{{dist_km}}}{{100}} \\right) \\times {_fmt(rate_per_100, 1)}.\n"
        f"Step 2: Calculate litres [1 mark].\n"
        f"{dist_km / 100} × {_fmt(rate_per_100, 1)} = {_fmt(fuel_litres, 1)} litres.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="23",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the distance by 100, then multiply by the rate in litres per 100 km.",
        tier_2=f"({_fmt(dist_km)} ÷ 100) × {_fmt(rate_per_100, 1)}.",
        tier_3=f"Fuel needed = {_fmt(fuel_litres, 1)} litres.",
        r=r,
    )


def generate_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Subskill 24: Fuel cost calculation in Rands: Litres * Price/L."""
    name = r.choice(SA_NAMES)
    fuel_litres = r.choice([35.0, 40.0, 45.0, 50.0, 55.0])
    price_per_l = r.choice([22.50, 23.20, 24.10, 24.80])

    total_cost = round(fuel_litres * price_per_l, 2)

    prompt = (
        f"{name} calculates that a round-trip road journey will require {_fmt(fuel_litres, 1)} litres of petrol. "
        f"The current petrol price at the filling station is {_fmt_curr(price_per_l)} per litre.\n"
        f"Calculate the total fuel cost for the trip in Rands."
    )

    correct_ans = _fmt_curr(total_cost)
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Multiply litres by price per litre [1 mark].\n"
        f"Cost = {_fmt(fuel_litres, 1)} L × {_fmt_curr(price_per_l)}/L [1 mark].\n"
        f"Step 2: Perform multiplication [1 mark].\n"
        f"Cost = {_fmt_curr(total_cost)}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="24",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the total litres required by the price per litre.",
        tier_2=f"{_fmt(fuel_litres, 1)} L × {_fmt_curr(price_per_l)}.",
        tier_3=f"Total cost = {_fmt_curr(total_cost)}.",
        r=r,
    )


def generate_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Subskill 25: Fuel efficiency comparison between two vehicles over a long trip."""
    name = r.choice(SA_NAMES)
    dist_km = r.choice([500, 600, 800])
    price_l = 23.50

    rate_a = 6.0   # sedan
    rate_b = 10.0  # bakkie

    litres_a = (dist_km / 100) * rate_a
    litres_b = (dist_km / 100) * rate_b

    cost_a = litres_a * price_l
    cost_b = litres_b * price_l
    savings = round(cost_b - cost_a, 2)

    prompt = (
        f"{name} is deciding between two vehicles for a {_fmt(dist_km)} km holiday trip:\n"
        f"• Sedan: Fuel consumption of {_fmt(rate_a, 1)} L/100 km\n"
        f"• Bakkie: Fuel consumption of {_fmt(rate_b, 1)} L/100 km\n"
        f"Petrol costs {_fmt_curr(price_l)} per litre. "
        f"How much money in Rands will {name} save on fuel by choosing the Sedan instead of the Bakkie?"
    )

    correct_ans = _fmt_curr(savings)
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Calculate litres for both vehicles [1 mark].\n"
        f"Sedan = ({dist_km} ÷ 100) × {_fmt(rate_a, 1)} = {litres_a} L.\n"
        f"Bakkie = ({dist_km} ÷ 100) × {_fmt(rate_b, 1)} = {litres_b} L.\n"
        f"Step 2: Calculate fuel costs [1 mark].\n"
        f"Sedan Cost = {litres_a} L × {_fmt_curr(price_l)} = {_fmt_curr(cost_a)}.\n"
        f"Bakkie Cost = {litres_b} L × {_fmt_curr(price_l)} = {_fmt_curr(cost_b)}.\n"
        f"Step 3: Calculate savings [1 mark].\n"
        f"Savings = {_fmt_curr(cost_b)} - {_fmt_curr(cost_a)} = {_fmt_curr(savings)} ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="25",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the fuel cost for both vehicles and find the difference.",
        tier_2=f"Sedan cost = {_fmt_curr(cost_a)}; Bakkie cost = {_fmt_curr(cost_b)}.",
        tier_3=f"Savings = {_fmt_curr(savings)}.",
        r=r,
    )


def generate_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Subskill 26: Number of refuelling stops required based on tank capacity."""
    name = r.choice(SA_NAMES)
    trip_km = r.choice([1100, 1250, 1400])
    tank_l = 55
    reserve_l = 10
    usable_l = tank_l - reserve_l  # 45 L usable
    rate = 7.5  # L/100 km

    # Range per full usable tank: (45 / 7.5) * 100 = 600 km
    range_km = (usable_l / rate) * 100

    # Stops needed starting with full tank: trip_km / range_km
    # If trip is 1250 km and range is 600 km:
    # 0 km: full. At ~600 km: stop 1. At ~1200 km: stop 2. Total 2 refuelling stops.
    stops = math.floor(trip_km / range_km)

    prompt = (
        f"{name} drives a car with a 55-litre fuel tank on a long journey of {_fmt(trip_km)} km. "
        f"The car consumes fuel at a rate of 7,5 litres per 100 km. "
        f"Safety rules recommend refuelling whenever the tank drops to a 10-litre reserve (using 45 litres between fill-ups).\n"
        f"Starting the journey with a completely full tank, what is the minimum number of refuelling stops {name} must make along the route?"
    )

    correct_ans = f"{stops} refuelling stops"
    wrong_1 = f"{stops + 1} refuelling stops"
    wrong_2 = f"{max(1, stops - 1)} refuelling stops"
    wrong_3 = f"{stops + 2} refuelling stops"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate driving range on a usable tank (45 L) [1 mark].\n"
        f"Range = (45 L ÷ 7,5 L/100 km) × 100 km = {_fmt(range_km, 0)} km per tank.\n"
        f"Step 2: Determine refuelling intervals along the {_fmt(trip_km)} km journey [1 mark].\n"
        f"Starting full, the car can travel to {_fmt(range_km, 0)} km before the first stop, and to {_fmt(2 * range_km, 0)} km after the second stop.\n"
        f"Step 3: Stated number of stops [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="26",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the maximum distance the car can travel on 45 litres, then see how many stops are needed to complete the trip.",
        tier_2=f"Range per tank is (45 ÷ 7,5) × 100 = {_fmt(range_km, 0)} km.",
        tier_3=f"A trip of {_fmt(trip_km)} km requires {stops} refuelling stops.",
        r=r,
    )


def generate_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Subskill 27: Carpooling cost sharing (fuel + toll fees per passenger)."""
    name = r.choice(SA_NAMES)
    num_passengers = r.choice([3, 4, 5])
    fuel_cost = r.choice([840, 960, 1120, 1200])
    toll_cost = r.choice([160, 240, 280, 320])

    total_cost = fuel_cost + toll_cost
    per_person = round(total_cost / num_passengers, 2)

    prompt = (
        f"{num_passengers} university students carpool together from Pretoria to Durban. "
        f"The total fuel expense for the round-trip is {_fmt_curr(fuel_cost)} and the total toll plaza fees "
        f"amount to {_fmt_curr(toll_cost)}.\n"
        f"If all travel expenses are shared equally among all {num_passengers} students, "
        f"how much must each student contribute in Rands?"
    )

    correct_ans = _fmt_curr(per_person)
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Calculate total combined travel expenses [1 mark].\n"
        f"Total Cost = Fuel + Tolls = {_fmt_curr(fuel_cost)} + {_fmt_curr(toll_cost)} = {_fmt_curr(total_cost)}.\n"
        f"Step 2: Divide equally among {num_passengers} students [1 mark].\n"
        f"Cost per person = {_fmt_curr(total_cost)} ÷ {num_passengers} = {_fmt_curr(per_person)}.\n"
        f"Step 3: Stated contribution [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="27",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add fuel and toll costs together, then divide by the number of students.",
        tier_2=f"Total = {_fmt_curr(fuel_cost)} + {_fmt_curr(toll_cost)} = {_fmt_curr(total_cost)}. Divide by {num_passengers}.",
        tier_3=f"Per student = {_fmt_curr(per_person)}.",
        r=r,
    )
