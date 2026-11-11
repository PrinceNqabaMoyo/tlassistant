"""Subskills 25 to 32: Toll Plazas, Multi-Modal Transport Economics & Minibus Taxi Pricing.
Covers SANRAL toll plaza tariffs, journey budgeting, long-distance bus schedules, ticket discounts,
train vs coach comparisons, solo driver vs bus vs carpooling, minibus taxi route operating budgets,
and taxi passenger fare determination with 30% profit margin.
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


def gen_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Subskill 25: Calculating total toll plaza fees along a national highway route (Class 1 light vehicles)."""
    # N3 Toll Plazas (Johannesburg to Durban)
    tolls = [
        ("De Hoek", 63.00),
        ("Wilge", 88.00),
        ("Tugela", 94.00),
        ("Mooi River", 66.00),
    ]
    total_tolls = sum(t[1] for t in tolls)

    table_data = {
        "headers": ["Toll Plaza", "Highway", "Class 1 (Light Motor Vehicles)"],
        "rows": [
            [t[0], "N3", _fmt_curr(t[1])] for t in tolls
        ]
    }

    prompt = (
        f"A motorist is driving from Johannesburg to Durban on the N3 toll road in a standard sedan "
        f"(Class 1 vehicle).\n\n"
        f"Refer to the SANRAL Toll Plaza Tariff Table below.\n"
        f"Calculate the total toll plaza fees for a one-way trip."
    )

    correct_ans = _fmt_curr(total_tolls)
    explanation = (
        f"1. Sum of all toll plazas = R 63,00 + R 88,00 + R 94,00 + R 66,00 = {correct_ans}."
    )
    t1 = "Add together the Class 1 fee for all four toll plazas along the route."
    t2 = f"Calculation: 63 + 88 + 94 + 66 = {_fmt_curr(total_tolls)}."
    t3 = f"Total toll fees = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_25",
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


def gen_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Subskill 26: Total private vehicle journey cost = Fuel cost + Toll fees + Wear/tear maintenance."""
    dist_km = r.choice([550, 600, 650])
    fuel_cost = r.choice([950.0, 1100.0, 1250.0])
    toll_fees = 311.00  # N3 total
    wear_tear_rate = 1.80  # R/km for maintenance and tyre wear
    wear_tear_cost = round(dist_km * wear_tear_rate, 2)

    total_trip_cost = round(fuel_cost + toll_fees + wear_tear_cost, 2)

    prompt = (
        f"A family travels a distance of {_fmt(dist_km)} km on holiday.\n"
        f"• Fuel purchases = {_fmt_curr(fuel_cost)}\n"
        f"• Highway toll plaza fees = {_fmt_curr(toll_fees)}\n"
        f"• Vehicle wear, tyre wear, and servicing allowance = {_fmt_curr(wear_tear_rate)} per km\n\n"
        f"Calculate the total actual cost of the trip."
    )

    correct_ans = _fmt_curr(total_trip_cost)
    explanation = (
        f"1. Wear and tear cost = {_fmt(dist_km)} km × {_fmt_curr(wear_tear_rate)} = {_fmt_curr(wear_tear_cost)}.\n"
        f"2. Total Cost = {_fmt_curr(fuel_cost)} (fuel) + {_fmt_curr(toll_fees)} (tolls) + "
        f"{_fmt_curr(wear_tear_cost)} (wear & tear) = {correct_ans}."
    )
    t1 = "Multiply distance by the wear and tear rate, then add fuel purchases and toll fees."
    t2 = f"Wear & tear: {dist_km} × {wear_tear_rate} = {_fmt_curr(wear_tear_cost)}. Add fuel and tolls."
    t3 = f"Total journey cost = {correct_ans}."

    # Misconceptions: forgetting tolls or wear & tear
    custom_opts = [
        correct_ans,
        _fmt_curr(fuel_cost + toll_fees),
        _fmt_curr(fuel_cost + wear_tear_cost),
        _fmt_curr(total_trip_cost * 1.15),
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_26",
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


def gen_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Subskill 27: Long-distance bus booking schedule: departure/arrival times, duration, seat availability."""
    table_data = {
        "headers": ["Bus Service", "Departure", "Arrival", "Duration", "Fare (per person)", "Seats Available"],
        "rows": [
            ["Coach 1 (Express)", "07:30", "13:00", "5 h 30 min", "R 360,00", "14"],
            ["Coach 2 (Midday)", "11:15", "17:45", "6 h 30 min", "R 320,00", "8"],
            ["Coach 3 (Night)", "21:00", "03:15", "6 h 15 min", "R 280,00", "22"],
            ["Coach 4 (Saver)", "14:00", "21:00", "7 h 00 min", "R 260,00", "4"],
        ]
    }

    prompt = (
        f"A student needs to travel from Johannesburg to Bloemfontein. She wants to arrive before "
        f"18:00 and spend no more than R 350,00 on the ticket.\n\n"
        f"Refer to the bus booking timetable below.\n"
        f"Which bus service meets both of her requirements?"
    )

    correct_ans = "Coach 2 (Midday)"
    explanation = (
        f"1. Arrival before 18:00: Coach 1 (13:00) and Coach 2 (17:45) qualify.\n"
        f"2. Budget max R 350,00: Coach 1 is R 360,00 (over budget). Coach 2 is R 320,00 (within budget).\n"
        f"3. Coach 2 satisfies both criteria."
    )
    t1 = "Check which bus options arrive before 18:00, then filter by the fare under R 350,00."
    t2 = "Coach 1 arrives at 13:00 but costs R 360. Coach 2 arrives at 17:45 and costs R 320."
    t3 = f"Best choice: {correct_ans}."

    custom_opts = [
        correct_ans,
        "Coach 1 (Express)",
        "Coach 3 (Night)",
        "Coach 4 (Saver)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_27",
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


def gen_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Subskill 28: Bus ticket costing: single vs return fare with child and pensioner discounts."""
    single_fare = r.choice([340.0, 380.0, 420.0])
    return_discount_pct = 10.0  # 10% off return ticket
    # Full return fare = 2 * single * (1 - 0.10)
    return_fare_adult = round(2 * single_fare * 0.90, 2)

    # Pensioner discount = 20% off adult return fare
    pensioner_fare = round(return_fare_adult * 0.80, 2)
    total_cost = round(return_fare_adult + pensioner_fare, 2)

    prompt = (
        f"A luxury bus company offers tickets between Durban and Pretoria:\n"
        f"• Single one-way adult fare: {_fmt_curr(single_fare)}\n"
        f"• Return adult ticket: 10% discount on two single tickets\n"
        f"• Pensioner return ticket: 20% discount on the adult return ticket\n\n"
        f"Calculate the total cost for 1 adult and 1 pensioner purchasing return tickets."
    )

    correct_ans = _fmt_curr(total_cost)
    explanation = (
        f"1. Adult return ticket = 2 × {_fmt_curr(single_fare)} × 0,90 = {_fmt_curr(return_fare_adult)}.\n"
        f"2. Pensioner return ticket = {_fmt_curr(return_fare_adult)} × 0,80 = {_fmt_curr(pensioner_fare)}.\n"
        f"3. Total = {_fmt_curr(return_fare_adult)} + {_fmt_curr(pensioner_fare)} = {correct_ans}."
    )
    t1 = "Find adult return ticket with 10% discount, then apply 20% discount for the pensioner return ticket."
    t2 = f"Adult return = {_fmt_curr(return_fare_adult)}. Pensioner = {_fmt_curr(pensioner_fare)}."
    t3 = f"Combined ticket cost = {correct_ans}."

    custom_opts = [
        correct_ans,
        _fmt_curr(2 * return_fare_adult),
        _fmt_curr(4 * single_fare),
        _fmt_curr(total_cost * 1.15),
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_28",
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


def gen_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Subskill 29: Passenger train vs long-distance bus: schedule, duration, and ticket cost comparison."""
    # Bus: 6 h, R 350; Train: 8.5 h, R 220
    bus_time_h, bus_cost = 6.0, 350.0
    train_time_h, train_cost = 8.5, 220.0
    time_saved_h = train_time_h - bus_time_h
    cost_diff = bus_cost - train_cost

    prompt = (
        f"A commuter compares travel from Polokwane to Johannesburg by train vs bus:\n"
        f"• Long-distance Bus: Travel time = {_fmt_time(bus_time_h)}, Fare = {_fmt_curr(bus_cost)}\n"
        f"• Shosholoza Meyl Train: Travel time = {_fmt_time(train_time_h)}, Fare = {_fmt_curr(train_cost)}\n\n"
        f"1. How much money is saved by choosing the train?\n"
        f"2. How much time is saved by choosing the bus?"
    )

    correct_ans = f"Save {_fmt_curr(cost_diff)} on train; Save {_fmt_time(time_saved_h)} on bus"
    explanation = (
        f"1. Cost saving = {_fmt_curr(bus_cost)} − {_fmt_curr(train_cost)} = {_fmt_curr(cost_diff)}.\n"
        f"2. Time saving = {_fmt_time(train_time_h)} − {_fmt_time(bus_time_h)} = {_fmt_time(time_saved_h)}."
    )
    t1 = "Subtract train fare from bus fare for money saved, and bus time from train time for time saved."
    t2 = f"Money difference = {_fmt_curr(cost_diff)}. Time difference = {_fmt_time(time_saved_h)}."
    t3 = f"Comparison: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Save {_fmt_curr(cost_diff + 50)} on train; Save {_fmt_time(time_saved_h)} on bus",
        f"Save {_fmt_curr(cost_diff)} on bus; Save {_fmt_time(time_saved_h)} on train",
        f"Save {_fmt_curr(cost_diff)} on train; Save {_fmt_time(time_saved_h + 1)} on bus",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_29",
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


def gen_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Subskill 30: Cost comparison: 1 person travelling by car vs bus vs shared car with 4 passengers."""
    dist_km = 600
    car_total_cost = 2520.00  # R 4,20/km * 600 km (fuel + tolls + maintenance)
    bus_ticket = 450.00       # R 450 per person

    # Option 1: Solo car
    solo_car = car_total_cost
    # Option 2: Solo bus
    solo_bus = bus_ticket
    # Option 3: Shared car (4 people sharing total car cost)
    shared_car_per_person = round(car_total_cost / 4.0, 2)

    prompt = (
        f"A group of 4 friends is planning a trip from Johannesburg to Durban (600 km one-way).\n"
        f"• Total vehicle operating cost (fuel, tolls, wear & tear) = {_fmt_curr(car_total_cost)}.\n"
        f"• Bus ticket price = {_fmt_curr(bus_ticket)} per passenger.\n\n"
        f"1. What is the cost per person if each friend takes the bus?\n"
        f"2. What is the cost per person if the 4 friends share the car and split all costs equally?\n"
        f"3. How much does each person save by carpooling instead of taking the bus?"
    )

    saving = round(solo_bus - shared_car_per_person, 2)
    cheaper_mode = "carpooling" if shared_car_per_person < solo_bus else "bus"
    correct_ans = f"Bus: {_fmt_curr(solo_bus)}, Carpool: {_fmt_curr(shared_car_per_person)} (Save: -{_fmt_curr(abs(saving))})" if saving < 0 else f"Bus: {_fmt_curr(solo_bus)}, Carpool: {_fmt_curr(shared_car_per_person)} (Save: {_fmt_curr(saving)})"

    explanation = (
        f"1. Bus cost per person = {_fmt_curr(solo_bus)}.\n"
        f"2. Shared car cost per person = {_fmt_curr(car_total_cost)} ÷ 4 = {_fmt_curr(shared_car_per_person)}.\n"
        f"3. Difference = {_fmt_curr(solo_bus)} − {_fmt_curr(shared_car_per_person)} = {_fmt_curr(saving)}."
    )
    t1 = "Divide the car total cost by 4 and compare with the individual bus ticket."
    t2 = f"Carpool = {_fmt_curr(car_total_cost)} ÷ 4 = {_fmt_curr(shared_car_per_person)}. Bus = {_fmt_curr(solo_bus)}."
    t3 = f"Cost breakdown: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Bus: {_fmt_curr(solo_bus)}, Carpool: {_fmt_curr(car_total_cost / 2)} (Save: R 150,00)",
        f"Bus: {_fmt_curr(solo_bus * 4)}, Carpool: {_fmt_curr(car_total_cost)} (Save: R 300,00)",
        f"Bus: {_fmt_curr(solo_bus)}, Carpool: {_fmt_curr(shared_car_per_person + 100)} (Save: R 80,00)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_30",
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


def gen_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Subskill 31: Minibus taxi operator trip budget: fuel + tolls + driver allowance for a single inter-town run."""
    name = r.choice(SA_NAMES)
    dist_km = r.choice([167, 185, 210])
    fuel_litres = r.choice([22.0, 25.0, 28.0])
    petrol_price = 23.45
    fuel_cost = round(fuel_litres * petrol_price, 2)

    toll_fee = r.choice([48.0, 65.0])
    driver_daily = 350.0

    total_trip_budget = round(fuel_cost + toll_fee + driver_daily, 2)

    prompt = (
        f"{name} operates a minibus taxi route covering {_fmt(dist_km)} km per trip.\n"
        f"His direct expenses for the trip are:\n"
        f"• Fuel: {_fmt(fuel_litres, 1)} Litres of petrol at {_fmt_curr(petrol_price)} per litre\n"
        f"• Toll plaza fee: {_fmt_curr(toll_fee)}\n"
        f"• Driver trip wage allowance: {_fmt_curr(driver_daily)}\n\n"
        f"Calculate the total cash budget needed to operate one single trip."
    )

    correct_ans = _fmt_curr(total_trip_budget)
    explanation = (
        f"1. Fuel cost = {_fmt(fuel_litres, 1)} L × {_fmt_curr(petrol_price)}/L = {_fmt_curr(fuel_cost)}.\n"
        f"2. Total trip budget = {_fmt_curr(fuel_cost)} + {_fmt_curr(toll_fee)} + {_fmt_curr(driver_daily)} = {correct_ans}."
    )
    t1 = "Multiply litres of petrol by petrol price, then add the toll fee and driver allowance."
    t2 = f"Fuel = {_fmt_curr(fuel_cost)}. Total = {fuel_cost} + {toll_fee} + {driver_daily}."
    t3 = f"Trip budget = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_31",
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


def gen_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Subskill 32: Minibus taxi passenger fare pricing with 30% profit margin over total operating costs."""
    operating_cost = r.choice([700.0, 750.0, 840.0, 900.0])
    passengers = r.choice([12, 14, 15])
    profit_margin_pct = 30.0

    cost_per_pass = operating_cost / passengers
    fare_with_profit = cost_per_pass * 1.30
    # Round to nearest whole 5 or 10 Rands as authentic SA taxi practice
    rounded_fare = int(round(fare_with_profit / 5.0) * 5)

    prompt = (
        f"A taxi operator calculates that his total operating cost to run a trip between two towns "
        f"is {_fmt_curr(operating_cost)}.\n"
        f"• The minibus carries an average of {passengers} passengers.\n"
        f"• The operator aims to make a 30% profit margin above costs.\n\n"
        f"1. Calculate the base operating cost per passenger.\n"
        f"2. Add 30% profit margin to find the fare.\n"
        f"3. Round off the fare to the nearest R 5 for cash convenience."
    )

    correct_ans = f"Base: {_fmt_curr(cost_per_pass)} -> Fare: {_fmt_curr(rounded_fare)}"
    explanation = (
        f"1. Cost per passenger = {_fmt_curr(operating_cost)} ÷ {passengers} = {_fmt_curr(cost_per_pass)}.\n"
        f"2. Fare with 30% profit = {_fmt_curr(cost_per_pass)} × 1,30 = {_fmt_curr(fare_with_profit)}.\n"
        f"3. Rounded to nearest R 5 = {_fmt_curr(rounded_fare)}."
    )
    t1 = "Divide operating cost by passengers, multiply by 1,30 for 30% profit, then round to nearest R 5."
    t2 = f"Base = {_fmt_curr(cost_per_pass)}. Fare = {_fmt_curr(fare_with_profit)} -> round to {_fmt_curr(rounded_fare)}."
    t3 = f"Taxi fare = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Base: {_fmt_curr(cost_per_pass)} -> Fare: {_fmt_curr(int(cost_per_pass))}",
        f"Base: {_fmt_curr(cost_per_pass * 1.3)} -> Fare: {_fmt_curr(rounded_fare + 15)}",
        f"Base: {_fmt_curr(cost_per_pass)} -> Fare: {_fmt_curr(rounded_fare - 15)}",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_32",
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
