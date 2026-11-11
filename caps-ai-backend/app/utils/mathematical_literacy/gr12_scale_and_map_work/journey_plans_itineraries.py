"""Subskills 47 to 52: Multi-Stop Logistics, Journey Plans, Rental Break-Evens & Team Transport.
Covers 2-day long-haul route splits, freight multi-drop delivery schedules, holiday travel budgets,
car rental tariff comparisons, break-even driving distances, and group charter optimization.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _fmt_time,
    _build_options,
    _build_question_payload,
)


def gen_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: 2-Day travel itinerary: route distance split, overnight accommodation stop, driving hours."""
    total_dist = 1400  # JHB to CPT
    # Stop at Colesberg (approx 650 km from JHB, 750 km to CPT)
    day1_dist = 650
    day2_dist = total_dist - day1_dist  # 750 km

    speed1 = 100  # km/h
    speed2 = 100  # km/h
    day1_driving_h = day1_dist / speed1  # 6.5 h
    day2_driving_h = day2_dist / speed2  # 7.5 h

    hotel_b_and_b = r.choice([950.0, 1100.0, 1250.0])

    prompt = (
        f"A family drives 1 400 km from Johannesburg to Cape Town, splitting the journey over 2 days:\n"
        f"• Day 1: Johannesburg to Colesberg ({day1_dist} km at an average speed of {speed1} km/h)\n"
        f"• Overnight stay at a B&B in Colesberg costing {_fmt_curr(hotel_b_and_b)}\n"
        f"• Day 2: Colesberg to Cape Town ({day2_dist} km at an average speed of {speed2} km/h)\n\n"
        f"1. Calculate the pure driving time for Day 1 in hours and minutes.\n"
        f"2. Calculate the pure driving time for Day 2 in hours and minutes.\n"
        f"3. State the overnight accommodation cost."
    )

    correct_ans = f"Day 1: {_fmt_time(day1_driving_h)}, Day 2: {_fmt_time(day2_driving_h)} (B&B: {_fmt_curr(hotel_b_and_b)})"
    explanation = (
        f"1. Day 1 driving time = {day1_dist} ÷ {speed1} = {_fmt(day1_driving_h, 1)} h = {_fmt_time(day1_driving_h)}.\n"
        f"2. Day 2 driving time = {day2_dist} ÷ {speed2} = {_fmt(day2_driving_h, 1)} h = {_fmt_time(day2_driving_h)}.\n"
        f"3. Accommodation cost = {_fmt_curr(hotel_b_and_b)}."
    )
    t1 = "Divide distance by speed for each day, then convert decimal hours to hours and minutes."
    t2 = f"Day 1 = {day1_dist} ÷ 100 = {_fmt_time(day1_driving_h)}. Day 2 = {day2_dist} ÷ 100 = {_fmt_time(day2_driving_h)}."
    t3 = f"Itinerary: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Day 1: 6 h 50 min, Day 2: 7 h 50 min (B&B: {_fmt_curr(hotel_b_and_b)})",
        f"Day 1: {_fmt_time(day1_driving_h)}, Day 2: {_fmt_time(day2_driving_h)} (B&B: {_fmt_curr(hotel_b_and_b * 1.5)})",
        f"Day 1: 5 h 30 min, Day 2: 8 h 30 min (B&B: {_fmt_curr(hotel_b_and_b)})",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_47",
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


def gen_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Commercial freight delivery route: multi-drop sequence, offload times, and driver rest regulation."""
    # 3 drops: Depot -> Client A (80 km) -> Client B (60 km) -> Client C (90 km) -> Depot (110 km)
    # Total driving distance = 340 km
    total_dist = 340
    driving_speed = 80  # km/h
    driving_time_h = total_dist / driving_speed  # 4.25 h = 4 h 15 min
    offload_per_drop_mins = 30  # 3 drops * 30 min = 90 min = 1.5 h
    mandatory_rest_mins = 45   # 45 min rest
    total_duty_mins = int(driving_time_h * 60) + (3 * offload_per_drop_mins) + mandatory_rest_mins

    duty_h = total_duty_mins // 60
    duty_m = total_duty_mins % 60

    prompt = (
        f"A distribution truck departs the central warehouse on a regional delivery run:\n"
        f"• Total driving distance across all client deliveries = {total_dist} km at an average speed of {driving_speed} km/h\n"
        f"• 3 scheduled customer deliveries, requiring 30 minutes each for unloading and invoice signing\n"
        f"• South African transport regulations require 1 mandatory 45-minute driver rest break\n\n"
        f"Calculate the total duty shift duration from departure to return (in hours and minutes)."
    )

    correct_ans = f"{duty_h} h {duty_m:02d} min"
    explanation = (
        f"1. Driving time = {total_dist} km ÷ {driving_speed} km/h = {_fmt(driving_time_h, 2)} h = {int(driving_time_h * 60)} minutes.\n"
        f"2. Offloading time = 3 × 30 minutes = 90 minutes.\n"
        f"3. Rest break = 45 minutes.\n"
        f"4. Total shift duration = {int(driving_time_h * 60)} + 90 + 45 = {total_duty_mins} minutes = {correct_ans}."
    )
    t1 = "Convert driving time to minutes, add offloading minutes for 3 drops, and add the 45-minute rest break."
    t2 = f"Driving: {int(driving_time_h * 60)} min. Drops: 90 min. Break: 45 min. Total: {total_duty_mins} min."
    t3 = f"Shift time = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{duty_h - 1} h {duty_m:02d} min",
        f"{duty_h} h {(duty_m + 30) % 60:02d} min",
        f"{duty_h + 1} h {duty_m:02d} min",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_48",
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


def gen_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Comprehensive holiday travel budget: fuel + tolls + accommodation + meals + emergency."""
    fuel_exp = r.choice([2400.0, 2650.0, 2900.0])
    toll_exp = 622.0  # Return tolls
    hotel_exp = r.choice([4500.0, 5200.0, 6000.0])
    meals_exp = r.choice([2200.0, 2500.0, 2800.0])
    subtotal = fuel_exp + toll_exp + hotel_exp + meals_exp
    emergency_buffer_pct = 10.0  # 10% emergency buffer
    total_budget = round(subtotal * 1.10, 2)

    prompt = (
        f"A family prepares a detailed holiday travel budget for an 8-day trip to the South Coast:\n"
        f"• Estimated return fuel: {_fmt_curr(fuel_exp)}\n"
        f"• SANRAL highway toll fees (return): {_fmt_curr(toll_exp)}\n"
        f"• Self-catering cottage accommodation: {_fmt_curr(hotel_exp)}\n"
        f"• Groceries, meals, and activities: {_fmt_curr(meals_exp)}\n"
        f"• Emergency contingency fund: 10% added to the subtotal\n\n"
        f"Calculate the subtotal of planned expenses and the total required budget including the 10% emergency fund."
    )

    correct_ans = f"Subtotal: {_fmt_curr(subtotal)} -> Total Budget: {_fmt_curr(total_budget)}"
    explanation = (
        f"1. Subtotal = {_fmt_curr(fuel_exp)} + {_fmt_curr(toll_exp)} + {_fmt_curr(hotel_exp)} + {_fmt_curr(meals_exp)} = {_fmt_curr(subtotal)}.\n"
        f"2. Emergency fund (10%) = {_fmt_curr(subtotal)} × 0,10 = {_fmt_curr(subtotal * 0.10)}.\n"
        f"3. Total Budget = {_fmt_curr(subtotal)} × 1,10 = {_fmt_curr(total_budget)}."
    )
    t1 = "Sum all 4 basic expenses to find the subtotal, then add 10% for the emergency contingency buffer."
    t2 = f"Subtotal = {_fmt_curr(subtotal)}. Total = {_fmt_curr(subtotal)} × 1,10."
    t3 = f"Holiday budget: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Subtotal: {_fmt_curr(subtotal)} -> Total Budget: {_fmt_curr(subtotal)}",
        f"Subtotal: {_fmt_curr(subtotal)} -> Total Budget: {_fmt_curr(total_budget * 1.10)}",
        f"Subtotal: {_fmt_curr(subtotal - toll_exp)} -> Total Budget: {_fmt_curr((subtotal - toll_exp) * 1.10)}",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_49",
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


def gen_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: Rental vehicle quotation comparison: Option A (unlimited km) vs Option B (low rate + per km)."""
    days = 4
    planned_km = r.choice([600, 750, 900])

    # Option A: R 650/day, unlimited km
    daily_a = 650.0
    cost_a = days * daily_a  # R 2 600

    # Option B: R 380/day + R 2,20 per km
    daily_b = 380.0
    rate_per_km = 2.20
    cost_b = round(days * daily_b + (planned_km * rate_per_km), 2)

    diff = round(abs(cost_a - cost_b), 2)
    cheaper_opt = "Package A (Unlimited)" if cost_a < cost_b else "Package B (Per-km)"

    prompt = (
        f"A business traveler needs to hire a car for {days} days to travel an estimated {_fmt(planned_km)} km:\n"
        f"• Package A: {_fmt_curr(daily_a)} per day with unlimited free kilometres.\n"
        f"• Package B: {_fmt_curr(daily_b)} per day plus {_fmt_curr(rate_per_km)} for every kilometre driven.\n\n"
        f"1. Calculate the total rental cost for Package A.\n"
        f"2. Calculate the total rental cost for Package B.\n"
        f"3. Which package is cheaper, and by how much?"
    )

    correct_ans = f"Package A: {_fmt_curr(cost_a)}, Package B: {_fmt_curr(cost_b)} ({cheaper_opt} is cheaper by {_fmt_curr(diff)})"
    explanation = (
        f"1. Package A cost = {days} × {_fmt_curr(daily_a)} = {_fmt_curr(cost_a)}.\n"
        f"2. Package B cost = ({days} × {_fmt_curr(daily_b)}) + ({_fmt(planned_km)} × {_fmt_curr(rate_per_km)}) "
        f"= {_fmt_curr(days * daily_b)} + {_fmt_curr(planned_km * rate_per_km)} = {_fmt_curr(cost_b)}.\n"
        f"3. Comparison: {cheaper_opt} saves {_fmt_curr(diff)}."
    )
    t1 = "Multiply Package A daily rate by days. For Package B, multiply daily rate by days and add km rate times distance."
    t2 = f"A: {cost_a}. B: {days * daily_b} + {planned_km * rate_per_km} = {cost_b}."
    t3 = f"Results: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Package A: {_fmt_curr(cost_a)}, Package B: {_fmt_curr(cost_b)} (Package A is cheaper by {_fmt_curr(diff + 150)})",
        f"Package A: {_fmt_curr(cost_a + 500)}, Package B: {_fmt_curr(cost_b)} (Package B is cheaper by {_fmt_curr(diff)})",
        f"Package A: {_fmt_curr(cost_a)}, Package B: {_fmt_curr(days * daily_b)} (Package B is cheaper by R 1 080,00)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_50",
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


def gen_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: Break-even driving distance between two car rental packages."""
    # Break-even equation: Cost_A = Cost_B
    # days * daily_A = days * daily_B + (x * rate_per_km)
    # x = days * (daily_A - daily_B) / rate_per_km
    days = 3
    daily_a = 600.0  # unlimited
    daily_b = 350.0  # low rate
    rate_per_km = 2.50

    daily_diff = daily_a - daily_b  # R 250
    total_fixed_diff = days * daily_diff  # R 750
    breakeven_km = int(round(total_fixed_diff / rate_per_km))  # 300 km

    prompt = (
        f"A tourist compares two 3-day rental options from Cape Town International Airport:\n"
        f"• Package 1: {_fmt_curr(daily_a)} per day (unlimited kilometres)\n"
        f"• Package 2: {_fmt_curr(daily_b)} per day plus {_fmt_curr(rate_per_km)} per kilometre\n\n"
        f"Formula: Break-even Distance (km) = [Days × (Package 1 Rate − Package 2 Rate)] ÷ Rate per km\n"
        f"Calculate the exact driving distance at which both rental packages cost the exact same amount."
    )

    correct_ans = f"{breakeven_km} km"
    explanation = (
        f"1. Cost Difference for 3 days = 3 × ({_fmt_curr(daily_a)} − {_fmt_curr(daily_b)}) = 3 × R 250,00 = {_fmt_curr(total_fixed_diff)}.\n"
        f"2. Break-even distance = {_fmt_curr(total_fixed_diff)} ÷ {_fmt_curr(rate_per_km)}/km = {correct_ans}.\n"
        f"3. Verification: At {breakeven_km} km, Package 1 = 3 × R 600 = R 1 800. Package 2 = (3 × R 350) + (300 × R 2,50) = R 1 050 + R 750 = R 1 800."
    )
    t1 = "Find total difference in daily base charges for 3 days, then divide by the per-kilometre rate."
    t2 = f"Total daily difference = 3 × (600 - 350) = R 750. Divide by R 2,50."
    t3 = f"Break-even distance = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_51",
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


def gen_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Choosing optimal transport mode for a sporting team: minibus vs individual cars vs coach."""
    team_members = 15
    dist_round_trip_km = 400

    # Option 1: 4 individual cars (4 people per car, 4th has 3): 4 cars * (400 km * R 3,80/km)
    car_rate_km = 3.80
    cost_cars = round(4 * (dist_round_trip_km * car_rate_km), 2)  # R 6 080

    # Option 2: 15-seater Quantum hire (R 1 800 hire fee + 400 km * R 23,45/L * 11 L/100 km)
    minibus_hire = 1800.0
    minibus_fuel = (dist_round_trip_km / 100.0) * 11.0 * 23.45  # 4 * 11 * 23.45 = R 1 031.80
    cost_minibus = round(minibus_hire + minibus_fuel, 2)  # R 2 831.80

    # Option 3: Chartered 22-seater luxury coach (flat package R 5 500)
    cost_coach = 5500.0

    cost_per_person_minibus = round(cost_minibus / team_members, 2)
    saving_vs_cars = round(cost_cars - cost_minibus, 2)

    prompt = (
        f"A high school soccer team of 15 players travels 400 km (return) to an away tournament.\n"
        f"Three travel arrangements are evaluated:\n"
        f"• Mode 1 (Private Cars): 4 private parent cars at an audited operating cost of {_fmt_curr(car_rate_km)}/km = {_fmt_curr(cost_cars)}\n"
        f"• Mode 2 (Minibus Hire): Hiring a 15-seater minibus ({_fmt_curr(minibus_hire)} daily rental + {_fmt_curr(minibus_fuel)} fuel) = {_fmt_curr(cost_minibus)}\n"
        f"• Mode 3 (Chartered Coach): Chartered 22-seater coach at a fixed package price of {_fmt_curr(cost_coach)}\n\n"
        f"1. Which arrangement is the most cost-effective for the school?\n"
        f"2. What is the cost per player using this optimal arrangement?\n"
        f"3. How much total money is saved compared to using 4 private cars?"
    )

    correct_ans = f"Mode 2 Minibus ({_fmt_curr(cost_per_person_minibus)}/player; Save {_fmt_curr(saving_vs_cars)})"
    explanation = (
        f"1. Minibus total = {_fmt_curr(cost_minibus)} is cheaper than Coach ({_fmt_curr(cost_coach)}) and Private Cars ({_fmt_curr(cost_cars)}).\n"
        f"2. Cost per player = {_fmt_curr(cost_minibus)} ÷ 15 = {_fmt_curr(cost_per_person_minibus)}.\n"
        f"3. Total savings vs cars = {_fmt_curr(cost_cars)} − {_fmt_curr(cost_minibus)} = {_fmt_curr(saving_vs_cars)}."
    )
    t1 = "Compare total costs for all 3 modes, divide the lowest by 15 players, and subtract from private car total."
    t2 = f"Minibus = {_fmt_curr(cost_minibus)}. Per player = {_fmt_curr(cost_per_person_minibus)}. Savings = {_fmt_curr(saving_vs_cars)}."
    t3 = f"Optimal choice: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Mode 3 Coach ({_fmt_curr(cost_coach / 15)}/player; Save R 580,00)",
        f"Mode 1 Private Cars ({_fmt_curr(cost_cars / 15)}/player; Save R 0,00)",
        f"Mode 2 Minibus ({_fmt_curr(cost_per_person_minibus * 1.5)}/player; Save {_fmt_curr(saving_vs_cars / 2)})",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_52",
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
