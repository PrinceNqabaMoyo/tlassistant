"""Subskills 41 to 46: Speed, distance, time, decimal time conversions, rest stops, and journey fuel."""
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
    _fmt_frac,
    _fmt_pct,
)


def generate_41_decimal_hours_to_hours_and_minutes(r: random.Random) -> Dict[str, Any]:
    """Convert decimal hours into hours and minutes without rounding errors."""
    hours_int = r.choice([1, 2, 3, 4])
    # decimal fraction e.g. 0.2, 0.25, 0.4, 0.6, 0.75, 0.8
    frac, mins = r.choice([
        (0.2, 12),
        (0.25, 15),
        (0.3, 18),
        (0.4, 24),
        (0.5, 30),
        (0.6, 36),
        (0.7, 42),
        (0.75, 45),
        (0.8, 48),
    ])
    dec_val = hours_int + frac

    correct_ans = f"{_fmt(dec_val, 2)} hours = {hours_int} hours {mins} minutes"

    # Common misconception: treating decimal part as minutes directly (e.g. 2,4 hours = 2 hours 40 minutes)
    misconception_mins = int(frac * 100)
    custom_options = [
        correct_ans,
        f"{_fmt(dec_val, 2)} hours = {hours_int} hours {misconception_mins} minutes",
        f"{_fmt(dec_val, 2)} hours = {hours_int + 1} hours {mins} minutes",
        f"{_fmt(dec_val, 2)} hours = {hours_int} hours {int(mins / 2)} minutes",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A GPS navigation application estimates the travel time for a delivery vehicle to be {_fmt(dec_val, 2)} hours.\n\n"
        f"Convert this decimal time value into **hours and minutes**.\n"
        f"(Show clearly how the decimal portion is converted)."
    )
    explanation = (
        f"Step 1: Separate the whole hours: {hours_int} whole hours [M].\n"
        f"Step 2: Multiply the decimal portion by 60 minutes: {_fmt(frac, 2)} × 60 = {mins} minutes [M].\n"
        f"Step 3: {_fmt(dec_val, 2)} hours = {hours_int} hours {mins} minutes [A]."
    )
    return _build_question_payload(
        subskill_id="41_decimal_hours_to_hours_and_minutes",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the decimal portion after the comma by 60 to convert to minutes.",
        tier_2=f"Whole hours = {hours_int}. Minutes = {_fmt(frac, 2)} × 60 = {mins}.",
        tier_3=f"{hours_int} hours {mins} minutes.",
        r=r,
    )


def generate_42_hours_and_minutes_to_decimal_hours(r: random.Random) -> Dict[str, Any]:
    """Convert hours and minutes into decimal hours for scientific and speed formula calculations."""
    h = r.choice([2, 3, 4, 5])
    mins, dec_frac = r.choice([
        (15, 0.25),
        (18, 0.30),
        (24, 0.40),
        (30, 0.50),
        (36, 0.60),
        (42, 0.70),
        (45, 0.75),
        (48, 0.80),
    ])
    dec_val = h + dec_frac

    correct_ans = f"{h} hours {mins} minutes = {_fmt(dec_val, 2)} hours ({h} + {mins}/60)"

    custom_options = [
        correct_ans,
        f"{h} hours {mins} minutes = {_fmt(h + (mins / 100), 2)} hours",
        f"{h} hours {mins} minutes = {_fmt(dec_val + 0.5, 2)} hours",
        f"{h} hours {mins} minutes = {_fmt(dec_val - 0.2, 2)} hours",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A commercial freight truck takes {h} hours and {mins} minutes to travel between Kimberley and Bloemfontein.\n\n"
        f"Convert this duration into **decimal hours** (hours in decimal form) so that it can be used in a speed calculation."
    )
    explanation = (
        f"Step 1: Keep whole hours: {h} hours [M].\n"
        f"Step 2: Divide the minutes by 60: {mins} ÷ 60 = {_fmt(dec_frac, 2)} hours [M].\n"
        f"Step 3: Sum: {h} + {_fmt(dec_frac, 2)} = {_fmt(dec_val, 2)} hours [A]."
    )
    return _build_question_payload(
        subskill_id="42_hours_and_minutes_to_decimal_hours",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the minutes by 60, then add the result to the whole hours.",
        tier_2=f"{mins} ÷ 60 = {_fmt(dec_frac, 2)}. Total = {h} + {_fmt(dec_frac, 2)}.",
        tier_3=f"{_fmt(dec_val, 2)} hours.",
        r=r,
    )


def generate_43_average_speed_calculation(r: random.Random) -> Dict[str, Any]:
    """Calculate average speed in km/h given distance and journey time in hours and minutes."""
    dist_km = r.choice([320, 360, 420, 480])
    h = r.choice([3, 4, 5])
    mins, frac = r.choice([(15, 0.25), (30, 0.50), (45, 0.75)])
    time_h = h + frac

    avg_speed = round(dist_km / time_h, 1)

    correct_ans = f"Time = {_fmt(time_h, 2)} hours; Average Speed = {dist_km} km ÷ {_fmt(time_h, 2)} h = {_fmt(avg_speed, 1)} km/h"

    # Misconception: dividing by h.mins (e.g. 3.30 instead of 3.5)
    misconception_time = h + (mins / 100.0)
    misconception_speed = round(dist_km / misconception_time, 1)

    custom_options = [
        correct_ans,
        f"Time = {_fmt(misconception_time, 2)} hours; Average Speed = {_fmt(misconception_speed, 1)} km/h",
        f"Time = {h} hours; Average Speed = {_fmt(dist_km / h, 1)} km/h",
        f"Time = {_fmt(time_h, 2)} hours; Average Speed = {_fmt(avg_speed * 1.2, 1)} km/h",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A family travels a distance of {dist_km} km from Pretoria to Nelspruit (Mbombela).\n"
        f"The total journey duration is {h} hours and {mins} minutes.\n\n"
        f"Formula: Average Speed = Distance (km) ÷ Time (hours)\n\n"
        f"Calculate the average speed of the vehicle in km/h, rounded to 1 decimal place."
    )
    explanation = (
        f"Step 1: Convert journey time to decimal hours: {h} + ({mins} ÷ 60) = {_fmt(time_h, 2)} hours [M].\n"
        f"Step 2: Substitute into speed formula: {dist_km} km ÷ {_fmt(time_h, 2)} h [M].\n"
        f"Step 3: Average Speed = {_fmt(avg_speed, 1)} km/h [A]."
    )
    return _build_question_payload(
        subskill_id="43_average_speed_calculation",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Convert hours and minutes to decimal hours first ({mins} ÷ 60), then divide distance by decimal time.",
        tier_2=f"Time = {h} + {frac} = {_fmt(time_h, 2)} h. Speed = {dist_km} ÷ {_fmt(time_h, 2)}.",
        tier_3=f"Average Speed = {_fmt(avg_speed, 1)} km/h.",
        r=r,
    )


def generate_44_travel_time_with_rest_stops(r: random.Random) -> Dict[str, Any]:
    """Calculate total travel time including mandatory driver rest stops along the highway."""
    total_distance_km = 600
    avg_driving_speed_kmh = 100  # 100 km/h
    # Driving time = 600 / 100 = 6 hours
    driving_hours = total_distance_km / avg_driving_speed_kmh  # 6.0 h

    # Rest stop rule: one 20-minute stop every 200 km (at 200 km and 400 km = 2 stops)
    num_stops = 2
    stop_mins = 20
    total_rest_mins = num_stops * stop_mins  # 40 mins

    total_trip_mins = int(driving_hours * 60) + total_rest_mins  # 400 mins = 6h 40m
    trip_h = total_trip_mins // 60
    trip_m = total_trip_mins % 60

    correct_ans = f"Driving = 6 hours; Rest = {total_rest_mins} min (2 stops); Total Travel Time = {trip_h} hours {trip_m} minutes"

    custom_options = [
        correct_ans,
        f"Driving = 6 hours; Rest = 60 min (3 stops); Total Travel Time = 7 hours 0 minutes",
        f"Driving = 6 hours; Rest = 0 min; Total Travel Time = 6 hours 0 minutes",
        f"Driving = 5 hours; Rest = {total_rest_mins} min; Total Travel Time = 5 hours {trip_m} minutes",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A tourist drives {total_distance_km} km along the N1 highway from Johannesburg to Beaufort West.\n"
        f"• The vehicle maintains an average driving speed of {avg_driving_speed_kmh} km/h while moving\n"
        f"• Road safety regulations recommend taking a {stop_mins}-minute rest stop for every 200 km driven\n\n"
        f"Calculate:\n"
        f"1. The pure driving time in hours\n"
        f"2. The number of recommended rest stops and total rest time\n"
        f"3. The total journey time from departure to arrival in hours and minutes"
    )
    explanation = (
        f"Step 1: Pure driving time = {total_distance_km} km ÷ {avg_driving_speed_kmh} km/h = 6 hours [M].\n"
        f"Step 2: Rest stops occur at 200 km and 400 km (2 stops): 2 × {stop_mins} min = {total_rest_mins} minutes [M].\n"
        f"Step 3: Total travel time = 6 hours + {total_rest_mins} minutes = {trip_h} hours {trip_m} minutes [A]."
    )
    return _build_question_payload(
        subskill_id="44_travel_time_with_rest_stops",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find pure driving time (600 ÷ 100), count stops before reaching destination, and add them together.",
        tier_2=f"Driving = 6 hours. Stops at 200 km and 400 km = 2 × 20 min = 40 min.",
        tier_3=f"Total Travel Time = {trip_h} hours {trip_m} minutes.",
        r=r,
    )


def generate_45_estimated_arrival_with_traffic_slowdown(r: random.Random) -> Dict[str, Any]:
    """Calculate the delay caused by reducing speed through a roadworks construction zone."""
    zone_dist_km = 30
    normal_speed = 100.0  # 100 km/h
    reduced_speed = 60.0  # 60 km/h

    normal_time_mins = (zone_dist_km / normal_speed) * 60.0   # 18 mins
    reduced_time_mins = (zone_dist_km / reduced_speed) * 60.0 # 30 mins
    delay_mins = int(reduced_time_mins - normal_time_mins)    # 12 mins

    correct_ans = f"Normal = {int(normal_time_mins)} min; Reduced = {int(reduced_time_mins)} min; Delay = {delay_mins} minutes"

    custom_options = [
        correct_ans,
        f"Normal = 20 min; Reduced = 40 min; Delay = 20 minutes",
        f"Normal = {int(normal_time_mins)} min; Reduced = 60 min; Delay = 42 minutes",
        f"Normal = 15 min; Reduced = 25 min; Delay = 10 minutes",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A motorist encounters a {zone_dist_km} km resurfacing roadworks zone along the N3 toll route.\n"
        f"• The normal speed limit is {int(normal_speed)} km/h\n"
        f"• The temporary reduced speed limit through the roadworks is {int(reduced_speed)} km/h\n\n"
        f"Calculate the time in minutes taken to travel through this {zone_dist_km} km zone at normal speed versus reduced speed, "
        f"and state the resulting travel time delay in minutes."
    )
    explanation = (
        f"Step 1: Normal time = ({zone_dist_km} ÷ {int(normal_speed)}) × 60 = {int(normal_time_mins)} minutes [M].\n"
        f"Step 2: Reduced time = ({zone_dist_km} ÷ {int(reduced_speed)}) × 60 = {int(reduced_time_mins)} minutes [M].\n"
        f"Step 3: Delay = {int(reduced_time_mins)} min - {int(normal_time_mins)} min = {delay_mins} minutes [A]."
    )
    return _build_question_payload(
        subskill_id="45_estimated_arrival_with_traffic_slowdown",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate Time = (Distance ÷ Speed) × 60 for both speeds, then subtract the two times.",
        tier_2=f"Normal = (30 ÷ 100) × 60 = 18 min. Reduced = (30 ÷ 60) × 60 = 30 min. Delay = 30 - 18.",
        tier_3=f"Delay = {delay_mins} minutes.",
        r=r,
    )


def generate_46_fuel_consumption_during_journey(r: random.Random) -> Dict[str, Any]:
    """Calculate total fuel consumed and total fuel expenditure for a road trip given consumption rate."""
    dist_km = r.choice([450, 520, 600, 680])
    rate_per_100km = r.choice([6.8, 7.2, 7.5, 8.0])  # litres per 100 km
    petrol_price_per_litre = 23.50  # R 23.50 per litre

    litres_consumed = round((dist_km / 100.0) * rate_per_100km, 2)
    fuel_cost = round(litres_consumed * petrol_price_per_litre, 2)

    correct_ans = f"Fuel = {_fmt(litres_consumed, 2)} ℓ; Total Fuel Cost = {_fmt_curr(fuel_cost)}"

    custom_options = [
        correct_ans,
        f"Fuel = {_fmt(litres_consumed * 1.5, 2)} ℓ; Total Fuel Cost = {_fmt_curr(fuel_cost * 1.5)}",
        f"Fuel = {_fmt(dist_km * rate_per_100km, 1)} ℓ; Total Fuel Cost = {_fmt_curr(dist_km * petrol_price_per_litre)}",
        f"Fuel = {_fmt(litres_consumed / 2, 2)} ℓ; Total Fuel Cost = {_fmt_curr(fuel_cost / 2)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} drives a hatchback over a distance of {dist_km} km for a holiday trip.\n"
        f"• The vehicle's manufacturer stated fuel consumption is {_fmt(rate_per_100km, 1)} litres per 100 km\n"
        f"• Unleaded petrol costs {_fmt_curr(petrol_price_per_litre)} per litre\n\n"
        f"1. Calculate the total volume of fuel consumed in litres (ℓ), rounded to 2 decimal places.\n"
        f"2. Calculate the total cost of petrol for this trip."
    )
    explanation = (
        f"Step 1: Fuel consumed = ({dist_km} ÷ 100) × {_fmt(rate_per_100km, 1)} = {_fmt(litres_consumed, 2)} ℓ [M].\n"
        f"Step 2: Total cost = {_fmt(litres_consumed, 2)} ℓ × {_fmt_curr(petrol_price_per_litre)} [M].\n"
        f"Step 3: Total Fuel Cost = {_fmt_curr(fuel_cost)} [A]."
    )
    return _build_question_payload(
        subskill_id="46_fuel_consumption_during_journey",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide distance by 100 and multiply by the consumption rate, then multiply by price per litre.",
        tier_2=f"Fuel = ({dist_km} ÷ 100) × {rate_per_100km} = {_fmt(litres_consumed, 2)} ℓ. Cost = {_fmt(litres_consumed, 2)} × {_fmt_curr(petrol_price_per_litre)}.",
        tier_3=f"Fuel = {_fmt(litres_consumed, 2)} ℓ; Total Cost = {_fmt_curr(fuel_cost)}.",
        r=r,
    )
