"""Subskills 33 to 40: Fuel Consumption Mechanics, Driving Range & Alternative Powertrains.
Covers trip fuel volume calculations, journey fuel cost, pump-to-odometer consumption rates,
full-tank driving range, refueling stop planning with safety reserves,
urban vs open-road consumption disparities, payload/trailer impact, and EV vs ICE cost per km.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    FUEL_PRICE_PETROL,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Subskill 33: Calculating fuel needed for a trip given consumption rate in litres per 100 km."""
    dist_km = r.choice([450, 520, 680, 850])
    rate_per_100 = r.choice([6.5, 7.2, 8.0, 9.5])  # L / 100 km

    # Litres = (distance / 100) * rate
    litres_needed = round((dist_km / 100.0) * rate_per_100, 1)

    prompt = (
        f"A sedan has a manufacturer fuel consumption rating of {_fmt(rate_per_100, 1)} Litres per 100 km.\n"
        f"The driver plans a journey of {_fmt(dist_km)} km.\n\n"
        f"Formula: Fuel Needed (Litres) = (Distance in km ÷ 100) × Consumption Rate (L/100 km)\n"
        f"Calculate the total volume of fuel needed for the trip (to 1 decimal place)."
    )

    correct_ans = f"{_fmt(litres_needed, 1)} L"
    explanation = (
        f"1. Formula: Litres = ({_fmt(dist_km)} ÷ 100) × {_fmt(rate_per_100, 1)}.\n"
        f"2. Calculation: {_fmt(dist_km / 100.0, 2)} × {_fmt(rate_per_100, 1)} = {correct_ans}."
    )
    t1 = "Divide the journey distance by 100, then multiply by the fuel consumption rate."
    t2 = f"Calculation: ({dist_km} ÷ 100) × {rate_per_100}."
    t3 = f"Fuel needed = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_33",
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


def gen_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Subskill 34: Calculating total fuel cost given distance, fuel rate (L/100 km), and petrol price."""
    dist_km = r.choice([500, 620, 750, 900])
    rate_per_100 = r.choice([7.0, 7.5, 8.2, 9.0])
    petrol_price = r.choice([22.50, 23.45, 24.10])

    litres = (dist_km / 100.0) * rate_per_100
    fuel_cost = round(litres * petrol_price, 2)

    prompt = (
        f"A light delivery vehicle covers a delivery route of {_fmt(dist_km)} km.\n"
        f"• Fuel consumption rate: {_fmt(rate_per_100, 1)} L/100 km\n"
        f"• Petrol price: {_fmt_curr(petrol_price)} per litre\n\n"
        f"1. Calculate the total litres of petrol consumed.\n"
        f"2. Calculate the total cost of petrol for the trip."
    )

    correct_ans = f"{_fmt(litres, 1)} L ({_fmt_curr(fuel_cost)})"
    explanation = (
        f"1. Litres consumed = ({_fmt(dist_km)} ÷ 100) × {_fmt(rate_per_100, 1)} = {_fmt(litres, 1)} L.\n"
        f"2. Fuel cost = {_fmt(litres, 1)} L × {_fmt_curr(petrol_price)} = {correct_ans}."
    )
    t1 = "Calculate total litres (Distance ÷ 100 × rate), then multiply by petrol price."
    t2 = f"Litres = {_fmt(litres, 1)} L. Cost = {_fmt(litres, 1)} × {_fmt_curr(petrol_price)}."
    t3 = f"Total fuel cost = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(litres, 1)} L ({_fmt_curr(fuel_cost * 1.15)})",
        f"{_fmt(litres * 1.2, 1)} L ({_fmt_curr(fuel_cost * 1.2)})",
        f"{_fmt(litres, 1)} L ({_fmt_curr(dist_km * petrol_price / 10)})",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_34",
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


def gen_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Subskill 35: Calculating actual vehicle fuel consumption rate from odometer distance and litres filled."""
    odo_start = r.choice([42500, 58100, 84300])
    dist_travelled = r.choice([480, 520, 600, 650])
    odo_end = odo_start + dist_travelled
    litres_filled = r.choice([36.0, 41.5, 48.0, 52.0])

    # Rate per 100 km = (litres / dist) * 100
    actual_rate = round((litres_filled / dist_travelled) * 100.0, 2)

    prompt = (
        f"A driver tests his car's actual fuel consumption:\n"
        f"• Starting odometer reading = {odo_start:,} km\n"
        f"• Ending odometer reading = {odo_end:,} km\n"
        f"• Litres of fuel needed to refill the tank to full = {_fmt(litres_filled, 1)} L\n\n"
        f"Formula: Consumption Rate (L/100 km) = (Litres Filled ÷ Distance Travelled in km) × 100\n"
        f"Calculate the actual fuel consumption rate in L/100 km (to 2 decimal places)."
    ).replace(",", " ")

    correct_ans = f"{_fmt(actual_rate, 2)} L/100 km"
    explanation = (
        f"1. Distance travelled = {odo_end:,} km − {odo_start:,} km = {dist_travelled} km.\n"
        f"2. Consumption Rate = ({_fmt(litres_filled, 1)} ÷ {dist_travelled}) × 100 = {correct_ans}."
    ).replace(",", " ")
    t1 = "Find distance travelled by subtracting odometer readings, then divide litres by distance and multiply by 100."
    t2 = f"Distance = {dist_travelled} km. Rate = ({litres_filled} ÷ {dist_travelled}) × 100."
    t3 = f"Rate = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_35",
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


def gen_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Subskill 36: Vehicle driving range: maximum distance possible on a full fuel tank."""
    tank_capacity = r.choice([45.0, 50.0, 60.0, 75.0])  # Litres
    rate_per_100 = r.choice([6.0, 7.5, 8.0, 10.0])      # L/100 km

    # Range = (tank_capacity / rate_per_100) * 100
    max_range_km = int(round((tank_capacity / rate_per_100) * 100.0))

    prompt = (
        f"A crossover SUV has a fuel tank capacity of {_fmt(tank_capacity)} Litres and an "
        f"average fuel consumption of {_fmt(rate_per_100, 1)} L/100 km.\n\n"
        f"Formula: Driving Range (km) = (Fuel Tank Capacity ÷ Consumption Rate) × 100\n"
        f"Calculate the maximum theoretical driving distance on a full tank of fuel."
    )

    correct_ans = f"{_fmt(max_range_km)} km"
    explanation = (
        f"1. Range = ({_fmt(tank_capacity)} ÷ {_fmt(rate_per_100, 1)}) × 100 = {_fmt(tank_capacity / rate_per_100 * 100, 1)} km.\n"
        f"2. Rounded to whole kilometres: {correct_ans}."
    )
    t1 = "Divide fuel tank capacity by consumption rate, then multiply by 100."
    t2 = f"({tank_capacity} ÷ {rate_per_100}) × 100 = {max_range_km}."
    t3 = f"Maximum range = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_36",
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


def gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Refueling stop planning along a route based on tank capacity and safety reserve."""
    dist_total_km = r.choice([850, 950, 1050, 1150])
    tank_litres = r.choice([45.0, 50.0, 55.0, 60.0])
    rate_per_100 = 8.0  # L/100 km
    reserve_litres = 10.0  # 10 L safety reserve
    usable_litres = tank_litres - reserve_litres
    safe_range_km = int((usable_litres / rate_per_100) * 100)

    d_spec_37 = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Route Planning: {dist_total_km} km (Safe Range: {safe_range_km} km)",
        "stops": [
            {"name": "Pretoria", "km": 0},
            {"name": "Refuel Stop", "km": safe_range_km},
            {"name": "Beaufort West", "km": dist_total_km},
        ],
    }

    prompt = (
        f"Refer to the route plan from Pretoria to Beaufort West ({dist_total_km} km).\n"
        f"• Fuel tank capacity: {_fmt(tank_litres, 0)} Litres\n"
        f"• Average fuel consumption: 8,0 L/100 km\n"
        f"• The driver insists on maintaining a 10-Litre emergency safety reserve at all times.\n\n"
        f"1. How many usable litres of fuel are available between fills?\n"
        f"2. What is the safe driving range in km before stopping to refuel?\n"
        f"3. What is the minimum number of refueling stops required during the {dist_total_km} km journey?"
    )

    stops_needed = math.ceil(dist_total_km / safe_range_km) - 1  # 950 / 500 = 1.9 -> 1 stop on the way
    correct_ans = f"Safe range: {safe_range_km} km ({stops_needed} stop on the road)"
    explanation = (
        f"1. Usable fuel = 50 L − 10 L = 40 Litres.\n"
        f"2. Safe range = (40 ÷ 8,0) × 100 = {safe_range_km} km.\n"
        f"3. Stops required: With a full tank at start, after {safe_range_km} km (e.g. at 500 km), "
        f"1 refill is required to complete the remaining 450 km. Total stops = {stops_needed}."
    )
    t1 = "Subtract 10 L reserve from 50 L, find safe range with 40 L, then calculate how many stops are needed."
    t2 = f"Usable = 40 L. Safe range = 500 km. Stops = 1."
    t3 = f"Refueling plan: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Safe range: 625 km (0 stops on the road)",
        f"Safe range: {safe_range_km} km (2 stops on the road)",
        f"Safe range: 400 km (3 stops on the road)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_37",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_37,
    )


def gen_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: City driving vs highway driving: comparing fuel consumption rates."""
    city_rate = r.choice([9.2, 9.8, 10.5])
    highway_rate = r.choice([6.2, 6.5, 7.0])
    monthly_city_km = 800
    monthly_hwy_km = 1200
    petrol_price = 23.45

    city_litres = (monthly_city_km / 100.0) * city_rate
    hwy_litres = (monthly_hwy_km / 100.0) * highway_rate
    total_litres = round(city_litres + hwy_litres, 1)
    total_cost = round(total_litres * petrol_price, 2)

    prompt = (
        f"A commuter's monthly driving is divided into city commuting and highway travel:\n"
        f"• City traffic: {_fmt(monthly_city_km)} km at {_fmt(city_rate, 1)} L/100 km\n"
        f"• Highway travel: {_fmt(monthly_hwy_km)} km at {_fmt(highway_rate, 1)} L/100 km\n"
        f"• Petrol price: {_fmt_curr(petrol_price)} per litre\n\n"
        f"1. Calculate the total litres of petrol consumed in the month.\n"
        f"2. Calculate the total monthly fuel expenditure."
    )

    correct_ans = f"{_fmt(total_litres, 1)} L ({_fmt_curr(total_cost)})"
    explanation = (
        f"1. City litres = ({monthly_city_km} ÷ 100) × {_fmt(city_rate, 1)} = {_fmt(city_litres, 1)} L.\n"
        f"2. Highway litres = ({monthly_hwy_km} ÷ 100) × {_fmt(highway_rate, 1)} = {_fmt(hwy_litres, 1)} L.\n"
        f"3. Total litres = {_fmt(city_litres, 1)} + {_fmt(hwy_litres, 1)} = {_fmt(total_litres, 1)} L.\n"
        f"4. Monthly cost = {_fmt(total_litres, 1)} × {_fmt_curr(petrol_price)} = {correct_ans}."
    )
    t1 = "Calculate litres for city and highway separately, add them together, and multiply by petrol price."
    t2 = f"City: {_fmt(city_litres, 1)} L. Hwy: {_fmt(hwy_litres, 1)} L. Total: {_fmt(total_litres, 1)} L."
    t3 = f"Fuel bill = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(total_litres * 1.15, 1)} L ({_fmt_curr(total_cost * 1.15)})",
        f"{_fmt(total_litres, 1)} L ({_fmt_curr(total_cost * 0.85)})",
        f"{_fmt(total_litres - 20, 1)} L ({_fmt_curr(total_cost - 450)})",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_38",
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


def gen_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Cargo payload impact: percentage increase in fuel consumption due to trailer."""
    base_rate = r.choice([7.5, 8.0, 8.5])  # L/100 km
    trailer_penalty_pct = r.choice([20, 25, 30])  # % increase
    towing_rate = round(base_rate * (1 + trailer_penalty_pct / 100.0), 2)
    dist_km = 600
    petrol_price = 23.45

    cost_base = (dist_km / 100.0) * base_rate * petrol_price
    cost_towing = (dist_km / 100.0) * towing_rate * petrol_price
    extra_cost = round(cost_towing - cost_base, 2)

    prompt = (
        f"A bakkie has a normal fuel consumption rate of {_fmt(base_rate, 1)} L/100 km.\n"
        f"When towing a fully loaded camping trailer, its fuel consumption increases by {trailer_penalty_pct}%.\n"
        f"• Journey distance = {_fmt(dist_km)} km\n"
        f"• Petrol price = {_fmt_curr(petrol_price)} per litre\n\n"
        f"1. Calculate the towing fuel consumption rate in L/100 km.\n"
        f"2. Calculate the extra fuel cost incurred over the {_fmt(dist_km)} km journey because of towing."
    )

    correct_ans = f"Rate: {_fmt(towing_rate, 2)} L/100 km (Extra Cost: {_fmt_curr(extra_cost)})"
    explanation = (
        f"1. Towing rate = {_fmt(base_rate, 1)} × (1 + {trailer_penalty_pct}/100) = {_fmt(towing_rate, 2)} L/100 km.\n"
        f"2. Normal fuel cost = ({dist_km} ÷ 100) × {_fmt(base_rate, 1)} × {_fmt_curr(petrol_price)} = {_fmt_curr(cost_base)}.\n"
        f"3. Towing fuel cost = ({dist_km} ÷ 100) × {_fmt(towing_rate, 2)} × {_fmt_curr(petrol_price)} = {_fmt_curr(cost_towing)}.\n"
        f"4. Extra cost = {_fmt_curr(cost_towing)} − {_fmt_curr(cost_base)} = {_fmt_curr(extra_cost)}."
    )
    t1 = "Add percentage increase to base fuel rate. Calculate fuel cost with and without trailer, and subtract."
    t2 = f"New rate = {_fmt(towing_rate, 2)} L/100 km. Extra cost = {_fmt_curr(extra_cost)}."
    t3 = f"Towing impact: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Rate: {_fmt(towing_rate, 2)} L/100 km (Extra Cost: {_fmt_curr(cost_towing)})",
        f"Rate: {_fmt(towing_rate + 1.5, 2)} L/100 km (Extra Cost: {_fmt_curr(extra_cost * 1.5)})",
        f"Rate: {_fmt(towing_rate, 2)} L/100 km (Extra Cost: {_fmt_curr(extra_cost / 2)})",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_39",
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


def gen_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: Electric vehicle (EV) vs internal combustion engine (ICE) energy cost per km."""
    # ICE petrol car: 7.5 L/100 km at R 23,45/L -> (7.5 * 23.45) / 100 = R 1,76/km
    ice_cost_per_km = 1.76

    # EV: 16 kWh/100 km at domestic electricity tariff of R 2,80/kWh -> (16 * 2.80) / 100 = R 0,45/km
    ev_cost_per_km = 0.45

    annual_km = 20000
    ice_annual = annual_km * ice_cost_per_km
    ev_annual = annual_km * ev_cost_per_km
    annual_saving = round(ice_annual - ev_annual, 2)

    prompt = (
        f"A fleet manager compares energy running costs for 20 000 km of annual driving:\n"
        f"• Petrol Car: {_fmt_curr(ice_cost_per_km)} per km\n"
        f"• Electric Vehicle (EV): 16 kWh per 100 km at an electricity tariff of R 2,80 per kWh\n\n"
        f"1. Calculate the EV energy cost per kilometre in Rands.\n"
        f"2. Calculate the annual energy expenditure for both vehicles over 20 000 km.\n"
        f"3. Determine the annual energy savings by operating the EV."
    )

    correct_ans = f"EV: {_fmt_curr(ev_cost_per_km)}/km (Annual Savings: {_fmt_curr(annual_saving)})"
    explanation = (
        f"1. EV cost per km = (16 kWh × R 2,80) ÷ 100 km = R 44,80 ÷ 100 = {_fmt_curr(ev_cost_per_km)}/km.\n"
        f"2. Petrol car annual = 20 000 × {_fmt_curr(ice_cost_per_km)} = {_fmt_curr(ice_annual)}.\n"
        f"3. EV annual = 20 000 × {_fmt_curr(ev_cost_per_km)} = {_fmt_curr(ev_annual)}.\n"
        f"4. Savings = {_fmt_curr(ice_annual)} − {_fmt_curr(ev_annual)} = {_fmt_curr(annual_saving)}."
    )
    t1 = "Calculate EV cost per km by multiplying 16 kWh by electricity tariff and dividing by 100."
    t2 = f"EV = {_fmt_curr(ev_cost_per_km)}/km. Petrol = {_fmt_curr(ice_cost_per_km)}/km. Multiply by 20 000 and subtract."
    t3 = f"EV comparison: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"EV: {_fmt_curr(ev_cost_per_km * 2)}/km (Annual Savings: {_fmt_curr(annual_saving / 2)})",
        f"EV: {_fmt_curr(ev_cost_per_km)}/km (Annual Savings: {_fmt_curr(annual_saving + 5000)})",
        f"EV: {_fmt_curr(ev_cost_per_km)}/km (Annual Savings: {_fmt_curr(ev_annual)})",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_40",
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
