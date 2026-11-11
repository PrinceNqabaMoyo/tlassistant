"""Subskills 25 to 32: Public Transport, Commuter Economics & Logistics Tariffs.
Covers taxi vs bus vs train comparisons, clipcard percentage savings, break-even commuter trips,
e-hailing surge multipliers, vehicle operating cost/km, volumetric courier weight, toll fees, and delivery contracts.
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Subskill 25: Minibus taxi vs municipal bus commuter fare comparison for monthly work travel."""
    name = r.choice(SA_NAMES)
    work_days = 22
    total_trips = work_days * 2  # return trip daily = 44 trips

    taxi_single = 18.00
    bus_single = 14.50

    cost_taxi = total_trips * taxi_single
    cost_bus = total_trips * bus_single
    diff = round(cost_taxi - cost_bus, 2)

    prompt = (
        f"{name} travels between Soweto and Johannesburg CBD for work, completing 2 trips per day over {work_days} work days ({total_trips} trips in total).\n\n"
        f"The two transit options are:\n"
        f"• Minibus Taxi: {_fmt_curr(taxi_single)} per single trip\n"
        f"• Municipal Bus: {_fmt_curr(bus_single)} per single trip\n\n"
        f"Calculate how much {name} saves in a month by commuting by bus instead of minibus taxi."
    )

    correct_ans = _fmt_curr(diff)
    explanation = (
        f"1. Total monthly trips = {work_days} days × 2 = {total_trips} trips.\n"
        f"2. Monthly taxi cost = {total_trips} × {_fmt_curr(taxi_single)} = {_fmt_curr(cost_taxi)}.\n"
        f"3. Monthly bus cost = {total_trips} × {_fmt_curr(bus_single)} = {_fmt_curr(cost_bus)}.\n"
        f"4. Monthly savings = {_fmt_curr(cost_taxi)} - {_fmt_curr(cost_bus)} = {_fmt_curr(diff)}."
    )
    t1 = f"Calculate the total cost of {total_trips} trips for taxi and bus."
    t2 = f"Taxi: {total_trips} × {_fmt_curr(taxi_single)}; Bus: {total_trips} × {_fmt_curr(bus_single)}."
    t3 = f"Savings = {_fmt_curr(cost_taxi)} - {_fmt_curr(cost_bus)} = {_fmt_curr(diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_25",
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


def gen_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Subskill 26: Bus ticket pricing: single ticket vs 10-trip weekly clipcard (percentage savings)."""
    single_fare = 22.00
    clipcard_price = 176.00  # for 10 trips (i.e. R17,60 per trip)

    single_10_cost = 10 * single_fare  # R220,00
    saving_rand = single_10_cost - clipcard_price  # R44,00
    saving_pct = round((saving_rand / single_10_cost) * 100, 1)

    prompt = (
        f"A municipal bus service charges R 22,00 for a single trip ticket.\n"
        f"Commuters can alternatively buy a 10-trip weekly clipcard for R 176,00.\n\n"
        f"Calculate the percentage savings obtained by purchasing the 10-trip clipcard instead of 10 individual single tickets."
    )

    correct_ans = f"{_fmt(saving_pct, 1)}%"
    explanation = (
        f"1. Cost of 10 single tickets = 10 × R 22,00 = R 220,00.\n"
        f"2. Cost of 10-trip clipcard = R 176,00.\n"
        f"3. Rand savings = R 220,00 - R 176,00 = R 44,00.\n"
        f"4. Percentage savings = (R 44,00 ÷ R 220,00) × 100% = {correct_ans}."
    )
    t1 = "Find the total cost of 10 single tickets: 10 × R 22,00 = R 220,00."
    t2 = "Calculate the difference between 10 single tickets and the clipcard price."
    t3 = f"Percentage = (44 ÷ 220) × 100% = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_26",
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
    """Subskill 27: Break-even commuter trips: minimum trips to justify an unlimited monthly pass."""
    single_ticket = r.choice([25.00, 28.00, 32.00])
    monthly_pass = r.choice([750.00, 840.00, 960.00])

    min_trips = int((monthly_pass / single_ticket) + 0.999)  # ceiling

    prompt = (
        f"A rapid transit bus network offers an unlimited monthly commuter pass for {_fmt_curr(monthly_pass)}.\n"
        f"Individual single-ride tickets cost {_fmt_curr(single_ticket)} each.\n\n"
        f"What is the minimum number of single trips a commuter must take in a month "
        f"to make purchasing the unlimited monthly pass cheaper than paying per trip?"
    )

    correct_ans = f"{min_trips} trips"
    explanation = (
        f"1. Divide the monthly pass price by the single ticket fare:\n"
        f"   {_fmt_curr(monthly_pass)} ÷ {_fmt_curr(single_ticket)} = {monthly_pass / single_ticket:.2f} trips.\n"
        f"2. Since partial trips cannot be taken, round up to the next whole number.\n"
        f"3. At {min_trips - 1} trips, cost is {_fmt_curr((min_trips - 1) * single_ticket)} (cheaper to buy singles).\n"
        f"4. At {min_trips} trips, cost is {_fmt_curr(min_trips * single_ticket)} (pass saves money). Minimum trips = {min_trips} trips."
    )
    t1 = f"Divide the pass price ({_fmt_curr(monthly_pass)}) by the single ticket price ({_fmt_curr(single_ticket)})."
    t2 = "Round up to the nearest whole number to ensure the pass is cheaper."
    t3 = f"Calculate: ceil({monthly_pass} / {single_ticket}) = {min_trips} trips."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_27",
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


def gen_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Subskill 28: E-hailing / metered taxi fare calculation with surge multiplier."""
    name = r.choice(SA_NAMES)
    km = r.randint(14, 26)
    mins = r.randint(22, 38)
    surge = r.choice([1.2, 1.4, 1.5])

    base_fare = 15.00
    per_km = 8.50
    per_min = 1.20

    subtotal = base_fare + (km * per_km) + (mins * per_min)
    total_fare = round(subtotal * surge, 2)

    prompt = (
        f"{name} took an e-hailing ride during peak evening rush hour with a {surge}x surge pricing multiplier.\n"
        f"The standard fare formula before surge is:\n"
        f"• Base Fare: {_fmt_curr(base_fare)}\n"
        f"• Distance rate: {_fmt_curr(per_km)} per kilometre ({km} km travelled)\n"
        f"• Time rate: {_fmt_curr(per_min)} per minute ({mins} minutes duration)\n\n"
        f"Calculate the total ride fare charged to {name}."
    )

    correct_ans = _fmt_curr(total_fare)
    explanation = (
        f"1. Base fare = {_fmt_curr(base_fare)}.\n"
        f"2. Distance charge = {km} km × {_fmt_curr(per_km)} = {_fmt_curr(km * per_km)}.\n"
        f"3. Time charge = {mins} min × {_fmt_curr(per_min)} = {_fmt_curr(mins * per_min)}.\n"
        f"4. Subtotal before surge = {_fmt_curr(base_fare)} + {_fmt_curr(km * per_km)} + {_fmt_curr(mins * per_min)} = {_fmt_curr(subtotal)}.\n"
        f"5. Total after {surge}x surge = {_fmt_curr(subtotal)} × {surge} = {_fmt_curr(total_fare)}."
    )
    t1 = f"Calculate standard fare: {base_fare} + ({km} × {per_km}) + ({mins} × {per_min})."
    t2 = f"Multiply the subtotal ({_fmt_curr(subtotal)}) by the surge multiplier ({surge})."
    t3 = f"Total = {_fmt_curr(subtotal)} × {surge} = {_fmt_curr(total_fare)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_28",
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


def gen_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Subskill 29: Vehicle operating cost per kilometre based on fuel, maintenance & toll."""
    dist_km = r.choice([350, 420, 500])
    fuel_consumption = 7.5  # 7.5 litres per 100 km
    petrol_price = 23.50    # R23,50 per litre
    maint_per_km = 0.85     # R0,85 per km
    toll_fees = 112.00      # toll plaza fees

    fuel_litres = (dist_km / 100.0) * fuel_consumption
    fuel_cost = round(fuel_litres * petrol_price, 2)
    maint_cost = round(dist_km * maint_per_km, 2)
    total_trip_cost = round(fuel_cost + maint_cost + toll_fees, 2)
    cost_per_km = round(total_trip_cost / dist_km, 2)

    prompt = (
        f"A company sales representative drove a vehicle {dist_km} km on a regional business trip.\n"
        f"Vehicle running parameters are:\n"
        f"• Fuel consumption: 7,5 litres per 100 km\n"
        f"• Fuel price: R 23,50 per litre\n"
        f"• Maintenance & tyres allowance: R 0,85 per km\n"
        f"• Toll plaza receipts: R 112,00\n\n"
        f"Calculate the total operating cost of this trip (in Rands)."
    )

    correct_ans = _fmt_curr(total_trip_cost)
    explanation = (
        f"1. Total fuel used = ({dist_km} ÷ 100) × 7,5 L = {fuel_litres:.2f} litres.\n"
        f"2. Total fuel cost = {fuel_litres:.2f} L × R 23,50 = {_fmt_curr(fuel_cost)}.\n"
        f"3. Maintenance cost = {dist_km} km × R 0,85/km = {_fmt_curr(maint_cost)}.\n"
        f"4. Toll fees = {_fmt_curr(toll_fees)}.\n"
        f"5. Total trip operating cost = {_fmt_curr(fuel_cost)} + {_fmt_curr(maint_cost)} + {_fmt_curr(toll_fees)} = {_fmt_curr(total_trip_cost)}."
    )
    t1 = f"Calculate fuel required: ({dist_km} / 100) × 7,5 litres, then multiply by R 23,50."
    t2 = f"Add maintenance ({dist_km} × R 0,85) and toll fees ({_fmt_curr(toll_fees)})."
    t3 = f"Total = {_fmt_curr(fuel_cost)} + {_fmt_curr(maint_cost)} + {_fmt_curr(toll_fees)} = {_fmt_curr(total_trip_cost)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_29",
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


def gen_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Subskill 30: Volumetric (dimensional) courier weight vs actual mass tariff."""
    # Box dimensions in cm
    l = r.choice([40, 50, 60])
    w = r.choice([30, 40, 50])
    h = r.choice([25, 30, 35])
    actual_mass_kg = r.choice([5.0, 7.5, 9.0])
    courier_rate_per_kg = 28.00

    vol_mass_kg = round((l * w * h) / 5000.0, 2)
    chargeable_mass = max(actual_mass_kg, vol_mass_kg)
    total_courier_fee = round(chargeable_mass * courier_rate_per_kg, 2)

    prompt = (
        f"A courier company charges R 28,00 per kilogram (or part thereof) based on the greater of actual mass "
        f"or volumetric mass calculated using the industry formula:\n"
        f"Volumetric Mass (kg) = (Length in cm × Width in cm × Height in cm) ÷ 5 000\n\n"
        f"A parcel has dimensions {l} cm × {w} cm × {h} cm and an actual scale mass of {_fmt(actual_mass_kg)} kg.\n"
        f"Calculate the courier fee for delivering this parcel."
    )

    correct_ans = _fmt_curr(total_courier_fee)
    explanation = (
        f"1. Calculate volumetric mass = ({l} × {w} × {h}) ÷ 5 000 = {l * w * h} ÷ 5 000 = {_fmt(vol_mass_kg)} kg.\n"
        f"2. Compare with actual mass ({_fmt(actual_mass_kg)} kg):\n"
        f"   Chargeable mass is the higher value = {_fmt(chargeable_mass)} kg.\n"
        f"3. Total courier fee = {_fmt(chargeable_mass)} kg × R 28,00/kg = {_fmt_curr(total_courier_fee)}."
    )
    t1 = f"Compute volumetric mass: ({l} × {w} × {h}) ÷ 5 000."
    t2 = f"Identify the higher value between volumetric mass ({_fmt(vol_mass_kg)} kg) and actual mass ({_fmt(actual_mass_kg)} kg)."
    t3 = f"Multiply chargeable mass ({_fmt(chargeable_mass)} kg) by R 28,00 = {_fmt_curr(total_courier_fee)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_30",
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
    """Subskill 31: Highway toll plaza fees across multiple gantries on an interprovincial route."""
    name = r.choice(SA_NAMES)
    vehicle_class = "Class 1 (Light Motor Vehicle)"

    # Authentic SANRAL N1 toll plazas
    tolls = [
        ("Grasmere Toll Plaza", 24.50),
        ("Vaal Toll Plaza", 79.00),
        ("Kroonstad Toll Plaza", 47.00),
        ("Verkeerdevlei Toll Plaza", 71.50),
    ]
    total_one_way = sum(cost for _, cost in tolls)
    total_return = round(total_one_way * 2, 2)

    prompt = (
        f"{name} drove a Class 1 passenger car on a return trip between Johannesburg and Bloemfontein on the N1.\n"
        f"The SANRAL toll fees per one-way direction are:\n"
        f"• Grasmere Plaza: R 24,50\n"
        f"• Vaal Plaza: R 79,00\n"
        f"• Kroonstad Plaza: R 47,00\n"
        f"• Verkeerdevlei Plaza: R 71,50\n\n"
        f"Calculate the total toll plaza fees paid for the entire return journey."
    )

    correct_ans = _fmt_curr(total_return)
    explanation = (
        f"1. One-way toll total = R 24,50 + R 79,00 + R 47,00 + R 71,50 = {_fmt_curr(total_one_way)}.\n"
        f"2. Return trip passes all four plazas twice: {_fmt_curr(total_one_way)} × 2 = {_fmt_curr(total_return)}."
    )
    t1 = "Sum the individual toll fees for one direction."
    t2 = "Multiply the one-way sum by 2 for the complete return trip."
    t3 = f"Total = {_fmt_curr(total_one_way)} × 2 = {_fmt_curr(total_return)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_31",
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


def gen_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Subskill 32: Delivery fleet route logistics: comparing fixed vehicle lease vs contractor cost."""
    deliveries = r.choice([180, 220, 260])

    # Option A: In-house van lease R 6 500/month + R 12,00 fuel/maintenance per delivery
    cost_a = round(6500.0 + (deliveries * 12.0), 2)

    # Option B: Third-party courier contractor at flat R 42,00 per delivery
    cost_b = round(deliveries * 42.0, 2)

    diff = round(abs(cost_a - cost_b), 2)
    cheaper = "Option A (In-house lease)" if cost_a < cost_b else "Option B (Third-party courier)"

    prompt = (
        f"A pharmacy completes {deliveries} prescription home deliveries each month.\n"
        f"The business is comparing two logistics options:\n"
        f"• Option A (Leased Van): Fixed monthly lease of R 6 500,00 plus R 12,00 running cost per delivery\n"
        f"• Option B (Third-Party Courier): Flat fee of R 42,00 per delivery with zero monthly fixed costs\n\n"
        f"Calculate how much the pharmacy saves each month by choosing the cheaper delivery option."
    )

    correct_ans = _fmt_curr(diff)
    explanation = (
        f"1. Option A cost = R 6 500,00 + ({deliveries} × R 12,00) = R 6 500,00 + R {deliveries * 12:.2f} = {_fmt_curr(cost_a)}.\n"
        f"2. Option B cost = {deliveries} × R 42,00 = {_fmt_curr(cost_b)}.\n"
        f"3. Difference = |{_fmt_curr(cost_a)} - {_fmt_curr(cost_b)}| = {_fmt_curr(diff)}.\n"
        f"   {cheaper} is cheaper by {_fmt_curr(diff)}."
    )
    t1 = f"Calculate Option A: R 6 500 + ({deliveries} × R 12)."
    t2 = f"Calculate Option B: {deliveries} × R 42."
    t3 = f"Find savings: |{_fmt_curr(cost_a)} - {_fmt_curr(cost_b)}| = {_fmt_curr(diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_32",
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
