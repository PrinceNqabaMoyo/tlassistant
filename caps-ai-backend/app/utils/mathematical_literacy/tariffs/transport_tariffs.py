"""Transport & Commuter Tariffs Subskills (Subskills 36 to 44).

36. fin_tar_trans_zone_distance_single_ticket
37. fin_tar_trans_single_vs_monthly_ticket_savings
38. fin_tar_trans_cost_per_trip_on_commuter_pass
39. fin_tar_trans_weekly_clipcard_vs_daily_return
40. fin_tar_trans_scholar_student_uniform_discount
41. fin_tar_trans_minibus_taxi_fare_route_table
42. fin_tar_trans_e_toll_highway_gantry_charges
43. fin_tar_trans_fuel_cost_vs_public_transport
44. fin_tar_trans_luggage_excess_baggage_charge
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_fin_tar_trans_zone_distance_single_ticket(r: random.Random) -> Dict[str, Any]:
    """Read a distance zone train tariff table to determine the cost of a single trip."""
    name = r.choice(SA_NAMES)
    distance_km = r.choice([12, 18, 25, 34, 45, 58])

    if distance_km <= 19:
        fare = 4.00
        zone = "Zone 1 (1 – 19 km)"
    elif distance_km <= 29:
        fare = 5.00
        zone = "Zone 2 (20 – 29 km)"
    elif distance_km <= 39:
        fare = 6.00
        zone = "Zone 3 (30 – 39 km)"
    elif distance_km <= 49:
        fare = 7.50
        zone = "Zone 4 (40 – 49 km)"
    else:
        fare = 9.50
        zone = "Zone 5 (> 50 km)"

    ans_str = _fmt_curr(fare)

    prompt = (
        f"{name} travels by train every morning over a distance of **{distance_km} km**.\n"
        f"Metrorail passenger fare schedule is structured as follows:\n\n"
        f"| Zone | Distance Range | Single Ticket | Return Ticket |\n"
        f"| :---: | :---: | :---: | :---: |\n"
        f"| Zone 1 | 1 – 19 km | R 4,00 | R 7,50 |\n"
        f"| Zone 2 | 20 – 29 km | R 5,00 | R 9,50 |\n"
        f"| Zone 3 | 30 – 39 km | R 6,00 | R 11,50 |\n"
        f"| Zone 4 | 40 – 49 km | R 7,50 | R 14,50 |\n"
        f"| Zone 5 | > 50 km | R 9,50 | R 18,50 |\n\n"
        f"Determine the cost of a **single ticket** for {name}'s {distance_km} km journey."
    )
    sol = (
        f"Step 1: Locate the journey distance in the fare schedule:\n"
        f"• Distance = {distance_km} km, which falls into **{zone}**.\n\n"
        f"Step 2: Method setup – read single ticket column for that zone:\n"
        f"• Single Ticket Fare = {_fmt_curr(fare)}\n"
        f"✓ [1 Mark: Method – matching {distance_km} km to correct zone in fare table]\n\n"
        f"Step 3: Final Fare:\n"
        f"Cost = {ans_str} ✓ [1 Mark: Accuracy – correct ticket price in Rands]"
    )
    rubric = [
        f"1 Mark: Method – identifying {zone} from table for {distance_km} km",
        f"1 Mark: Accuracy – correct ticket price {ans_str}"
    ]
    hints = {
        "tier_1": f"Look at the distance range column to find where {distance_km} km fits.",
        "tier_2": f"Find the corresponding Single Ticket fare for that zone.",
        "tier_3": f"For {distance_km} km, the fare is {ans_str}."
    }
    return _make_q("fin_tar_trans_zone_distance_single_ticket", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_trans_single_vs_monthly_ticket_savings(r: random.Random) -> Dict[str, Any]:
    """Calculate monthly savings of buying a monthly commuter ticket instead of daily single tickets."""
    name = r.choice(SA_NAMES)
    single_fare = 4.00
    monthly_pass = 81.50
    # 2 trips per day, 5 days per week, 4 weeks in a school month = 40 trips
    total_trips = 40

    total_single_cost = round(total_trips * single_fare, 2)  # R 160.00
    savings = round(total_single_cost - monthly_pass, 2)      # R 78.50
    ans_str = _fmt_curr(savings)

    prompt = (
        f"{name} travels by train to school and back every day (2 trips per day) for 5 days a week "
        f"over a 4-week month (a total of **{total_trips} trips**).\n"
        f"• **Single Ticket**: {_fmt_curr(single_fare)} per trip\n"
        f"• **Monthly Ticket Pass**: {_fmt_curr(monthly_pass)} (unlimited travel for the calendar month)\n\n"
        f"1. Calculate the total cost if {name} buys individual single tickets for all {total_trips} trips.\n"
        f"2. Calculate **how much cheaper** it is to buy the monthly ticket instead."
    )
    sol = (
        f"Step 1: Calculate total cost using single tickets:\n"
        f"• Total Single Tickets = {total_trips} trips × {_fmt_curr(single_fare)} = {_fmt_curr(total_single_cost)}\n\n"
        f"Step 2: Method setup – subtract monthly pass cost from single ticket total:\n"
        f"• Savings = Single Tickets Total - Monthly Pass\n"
        f"• Savings = {_fmt_curr(total_single_cost)} - {_fmt_curr(monthly_pass)} "
        f"✓ [1 Mark: Method – multiplying {total_trips} by {_fmt_curr(single_fare)} and subtracting monthly pass price]\n\n"
        f"Step 3: Calculate savings:\n"
        f"Savings = {ans_str} ✓ [1 Mark: Accuracy – correct monthly savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating ({total_trips} × {_fmt_curr(single_fare)}) - {_fmt_curr(monthly_pass)}",
        f"1 Mark: Accuracy – correct savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Multiply {total_trips} trips by the single ticket price of {_fmt_curr(single_fare)}.",
        "tier_2": f"Subtract the monthly ticket price ({_fmt_curr(monthly_pass)}) from that total.",
        "tier_3": f"{total_single_cost:.2f} - {monthly_pass:.2f} = {savings:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_trans_single_vs_monthly_ticket_savings", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_trans_cost_per_trip_on_commuter_pass(r: random.Random) -> Dict[str, Any]:
    """Calculate the effective cost per trip on a monthly commuter train pass."""
    name = r.choice(SA_NAMES)
    monthly_price = round(r.choice([81.50, 97.00, 112.00, 123.00, 140.00]), 2)
    trips = r.choice([40, 44, 48])

    cost_per_trip = round(monthly_price / trips, 2)
    ans_str = _fmt_curr(cost_per_trip)

    prompt = (
        f"{name} purchases a monthly commuter train pass for **{_fmt_curr(monthly_price)}** "
        f"and uses it for a total of **{trips} trips** during the month.\n\n"
        f"Calculate the **effective cost per individual trip** for {name}, rounded to the nearest cent.\n"
        f"Use the formula: $$\\text{{Cost per Trip}} = \\frac{{\\text{{Monthly Pass Price}}}}{{\\text{{Total Number of Trips}}}}$$"
    )
    sol = (
        f"Step 1: Identify monthly price and total trips completed:\n"
        f"• Monthly Ticket Cost = {_fmt_curr(monthly_price)}\n"
        f"• Trips Made = {trips}\n\n"
        f"Step 2: Method setup – divide monthly price by number of trips:\n"
        f"• Cost per Trip = {_fmt_curr(monthly_price)} ÷ {trips}\n"
        f"• Cost per Trip = {monthly_price} ÷ {trips} "
        f"✓ [1 Mark: Method – dividing total monthly pass price by {trips} trips]\n\n"
        f"Step 3: Calculate unit cost per trip:\n"
        f"Cost per Trip = {ans_str} ✓ [1 Mark: Accuracy – correct cost per trip in Rands]"
    )
    rubric = [
        f"1 Mark: Method – dividing {_fmt_curr(monthly_price)} by {trips}",
        f"1 Mark: Accuracy – correct unit cost {ans_str}"
    ]
    hints = {
        "tier_1": f"Divide the ticket price of {_fmt_curr(monthly_price)} by {trips} trips.",
        "tier_2": f"Calculate: {monthly_price} ÷ {trips}.",
        "tier_3": f"{monthly_price:.2f} ÷ {trips} = {cost_per_trip:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_trans_cost_per_trip_on_commuter_pass", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_trans_weekly_clipcard_vs_daily_return(r: random.Random) -> Dict[str, Any]:
    """Compare a 10-trip weekly clip-card vs buying daily return tickets."""
    name = r.choice(SA_NAMES)
    return_fare = round(r.choice([14.50, 16.00, 18.50, 21.00]), 2)
    weekly_clipcard = round(r.choice([62.00, 70.00, 78.50, 88.00]), 2)
    days_per_week = 5

    # Buying return ticket each day for 5 days
    daily_total = round(return_fare * days_per_week, 2)
    savings = round(daily_total - weekly_clipcard, 2)
    ans_str = _fmt_curr(savings)

    prompt = (
        f"{name} commutes by municipal bus for 5 days a week (Monday to Friday).\n"
        f"• **Daily Return Ticket**: {_fmt_curr(return_fare)} per day\n"
        f"• **Weekly Clip-Card (10 trips)**: {_fmt_curr(weekly_clipcard)} per week\n\n"
        f"Calculate **how much money** {name} saves each week by buying the weekly clip-card instead of daily return tickets."
    )
    sol = (
        f"Step 1: Calculate the weekly cost using daily return tickets:\n"
        f"• Daily Return Total = 5 days × {_fmt_curr(return_fare)} = {_fmt_curr(daily_total)}\n\n"
        f"Step 2: Method setup – subtract weekly clip-card cost:\n"
        f"• Savings = Daily Total - Weekly Clip-Card\n"
        f"• Savings = {_fmt_curr(daily_total)} - {_fmt_curr(weekly_clipcard)} "
        f"✓ [1 Mark: Method – multiplying daily return fare by 5 and subtracting clip-card price]\n\n"
        f"Step 3: Calculate savings:\n"
        f"Savings = {ans_str} ✓ [1 Mark: Accuracy – correct weekly savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating (5 × {_fmt_curr(return_fare)}) - {_fmt_curr(weekly_clipcard)}",
        f"1 Mark: Accuracy – correct savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Work out the cost of 5 daily return tickets: 5 × {_fmt_curr(return_fare)} = {_fmt_curr(daily_total)}.",
        "tier_2": f"Subtract the weekly clip-card price ({_fmt_curr(weekly_clipcard)}) from that sum.",
        "tier_3": f"{daily_total:.2f} - {weekly_clipcard:.2f} = {savings:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_trans_weekly_clipcard_vs_daily_return", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_trans_scholar_student_uniform_discount(r: random.Random) -> Dict[str, Any]:
    """Calculate the discounted ticket price for a scholar travelling in school uniform."""
    name = r.choice(SA_NAMES)
    full_price = round(r.choice([81.50, 97.00, 112.00, 125.00, 140.00]), 2)
    discount_pct = 20

    discount_amt = round(full_price * (discount_pct / 100), 2)
    concession_price = round(full_price - discount_amt, 2)
    ans_str = _fmt_curr(concession_price)

    prompt = (
        f"{name} is a high school learner purchasing a monthly commuter train pass with a normal price of **{_fmt_curr(full_price)}**.\n"
        f"The railway operator offers a **20% scholar discount** for learners travelling in school uniform with a student card.\n\n"
        f"Calculate the **discounted price** {name} will pay for the monthly ticket."
    )
    sol = (
        f"Step 1: Calculate the discount amount:\n"
        f"• Discount = 20% of {_fmt_curr(full_price)} = 0,20 × {full_price} = {_fmt_curr(discount_amt)}\n\n"
        f"Step 2: Method setup – subtract discount from full ticket price:\n"
        f"• Concession Price = Full Price - Discount\n"
        f"• Concession Price = {_fmt_curr(full_price)} - {_fmt_curr(discount_amt)} "
        f"✓ [1 Mark: Method – calculating 20% discount and subtracting from base ticket price]\n\n"
        f"Step 3: Calculate discounted fare:\n"
        f"Discounted Price = {ans_str} ✓ [1 Mark: Accuracy – correct concession price in Rands]"
    )
    rubric = [
        f"1 Mark: Method – evaluating {_fmt_curr(full_price)} × 0,80 (or {_fmt_curr(full_price)} - 20% discount)",
        f"1 Mark: Accuracy – correct discounted fare {ans_str}"
    ]
    hints = {
        "tier_1": f"Calculate 20% of {_fmt_curr(full_price)} to find the discount amount.",
        "tier_2": f"Subtract the discount ({_fmt_curr(discount_amt)}) from the full price ({_fmt_curr(full_price)}).",
        "tier_3": f"{full_price:.2f} × 0,80 = {concession_price:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_trans_scholar_student_uniform_discount", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_trans_minibus_taxi_fare_route_table(r: random.Random) -> Dict[str, Any]:
    """Calculate the weekly travel cost using a South African minibus taxi fare table."""
    name = r.choice(SA_NAMES)
    routes = [
        ("Soweto (Baragwanath) to Johannesburg CBD", 16.00),
        ("Alexandra to Sandton", 14.50),
        ("Mamelodi to Pretoria Central", 18.00),
        ("Mitchells Plain to Cape Town Station", 22.00),
        ("Umlazi to Durban Central", 17.50),
    ]
    route_name, one_way_fare = r.choice(routes)
    trips_per_week = 10  # 2 trips/day * 5 work days

    weekly_fare = round(one_way_fare * trips_per_week, 2)
    ans_str = _fmt_curr(weekly_fare)

    prompt = (
        f"{name} travels to work by minibus taxi on the route: **{route_name}**.\n"
        f"The one-way taxi fare is **{_fmt_curr(one_way_fare)}** per trip.\n\n"
        f"If {name} commutes to work and back (2 trips per day) for **5 days a week** (a total of 10 trips),\n"
        f"calculate {name}'s **total weekly taxi transport expenditure**."
    )
    sol = (
        f"Step 1: Identify one-way fare and total weekly trips:\n"
        f"• Fare per trip = {_fmt_curr(one_way_fare)}\n"
        f"• Trips per week = 2 trips/day × 5 days = 10 trips\n\n"
        f"Step 2: Method setup – multiply one-way fare by 10 trips:\n"
        f"• Weekly Total = 10 × {_fmt_curr(one_way_fare)} "
        f"✓ [1 Mark: Method – multiplying one-way fare by 10 trips per week]\n\n"
        f"Step 3: Calculate total:\n"
        f"Weekly Total = {ans_str} ✓ [1 Mark: Accuracy – correct weekly taxi fare in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying 10 by {_fmt_curr(one_way_fare)}",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": f"{name} makes 2 trips each day for 5 days = 10 trips per week.",
        "tier_2": f"Multiply 10 by the one-way fare of {_fmt_curr(one_way_fare)}.",
        "tier_3": f"10 × {one_way_fare:.2f} = {weekly_fare:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_trans_minibus_taxi_fare_route_table", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_trans_e_toll_highway_gantry_charges(r: random.Random) -> Dict[str, Any]:
    """Calculate highway toll gantry fees with standard rate vs registered e-tag discount."""
    name = r.choice(SA_NAMES)
    gantries_passed = r.choice([4, 6, 8, 10])
    standard_gantry_fee = 4.25
    etag_discount_pct = 48  # 48% discount for registered e-tag users

    total_standard = round(gantries_passed * standard_gantry_fee, 2)
    etag_fee_per_gantry = round(standard_gantry_fee * (1 - etag_discount_pct / 100), 2)
    total_etag = round(gantries_passed * etag_fee_per_gantry, 2)
    savings = round(total_standard - total_etag, 2)
    ans_str = _fmt_curr(savings)

    prompt = (
        f"{name} drives through **{gantries_passed} highway toll gantries** on a journey.\n"
        f"• The **Standard Non-Registered Toll Tariff** is {_fmt_curr(standard_gantry_fee)} per gantry.\n"
        f"• Vehicles with a registered **e-tag** receive a **48% discount**, paying only {_fmt_curr(etag_fee_per_gantry)} per gantry.\n\n"
        f"Calculate **how much money** {name} saves on this journey by using a registered e-tag."
    )
    sol = (
        f"Step 1: Calculate the total toll cost for both options:\n"
        f"• Standard Total = {gantries_passed} × {_fmt_curr(standard_gantry_fee)} = {_fmt_curr(total_standard)}\n"
        f"• E-tag Total = {gantries_passed} × {_fmt_curr(etag_fee_per_gantry)} = {_fmt_curr(total_etag)}\n\n"
        f"Step 2: Method setup – calculate the savings:\n"
        f"• Savings = Standard Total - E-tag Total\n"
        f"• Savings = {_fmt_curr(total_standard)} - {_fmt_curr(total_etag)} "
        f"✓ [1 Mark: Method – evaluating both toll totals for {gantries_passed} gantries and finding difference]\n\n"
        f"Step 3: Calculate savings:\n"
        f"Savings = {ans_str} ✓ [1 Mark: Accuracy – correct toll savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating ({gantries_passed} × {_fmt_curr(standard_gantry_fee)}) - ({gantries_passed} × {_fmt_curr(etag_fee_per_gantry)})",
        f"1 Mark: Accuracy – correct savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Work out the standard fee: {gantries_passed} × {_fmt_curr(standard_gantry_fee)} = {_fmt_curr(total_standard)}.",
        "tier_2": f"Work out the e-tag fee: {gantries_passed} × {_fmt_curr(etag_fee_per_gantry)} = {_fmt_curr(total_etag)}.",
        "tier_3": f"{total_standard:.2f} - {total_etag:.2f} = {savings:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_trans_e_toll_highway_gantry_charges", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_trans_fuel_cost_vs_public_transport(r: random.Random) -> Dict[str, Any]:
    """Compare the monthly cost of driving a private car (fuel + parking) vs public transport."""
    name = r.choice(SA_NAMES)
    km_per_day = 30
    days = 22
    total_km = km_per_day * days  # 660 km

    fuel_consumption_per_100km = 8.0  # 8 L / 100 km
    petrol_price_per_litre = round(r.choice([22.50, 23.80, 24.50]), 2)
    monthly_parking = 350.00

    litres_needed = (total_km / 100) * fuel_consumption_per_100km
    total_fuel_cost = round(litres_needed * petrol_price_per_litre, 2)
    total_car_cost = round(total_fuel_cost + monthly_parking, 2)

    public_transport_monthly_pass = round(r.choice([650.00, 720.00, 800.00]), 2)
    savings = round(total_car_cost - public_transport_monthly_pass, 2)
    ans_str = _fmt_curr(savings)

    prompt = (
        f"{name} commutes to work ({km_per_day} km return each day) for **22 working days** a month (total distance: **{total_km} km**).\n"
        f"• **Private Car**:\n"
        f"  - Fuel economy: 8,0 litres per 100 km\n"
        f"  - Fuel price: {_fmt_curr(petrol_price_per_litre)} per litre\n"
        f"  - Monthly parking bay fee: {_fmt_curr(monthly_parking)}\n"
        f"• **Public Transport (Rea Vaya / Train Pass)**: {_fmt_curr(public_transport_monthly_pass)} per month\n\n"
        f"Calculate **how much money** {name} will save each month by choosing public transport instead of driving."
    )
    sol = (
        f"Step 1: Calculate total private car costs:\n"
        f"• Total Litres = ({total_km} km ÷ 100) × 8,0 L = {litres_needed:.1f} litres\n"
        f"• Total Fuel Cost = {litres_needed:.1f} L × {_fmt_curr(petrol_price_per_litre)} = {_fmt_curr(total_fuel_cost)}\n"
        f"• Total Car Expense = {_fmt_curr(total_fuel_cost)} + {_fmt_curr(monthly_parking)} = {_fmt_curr(total_car_cost)}\n\n"
        f"Step 2: Method setup – subtract public transport pass from car cost:\n"
        f"• Savings = Total Car Expense - Public Transport Pass\n"
        f"• Savings = {_fmt_curr(total_car_cost)} - {_fmt_curr(public_transport_monthly_pass)} "
        f"✓ [1 Mark: Method – evaluating total driving costs (fuel + parking) and subtracting public pass]\n\n"
        f"Step 3: Calculate monthly savings:\n"
        f"Savings = {ans_str} ✓ [1 Mark: Accuracy – correct monthly savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – evaluating car total ({_fmt_curr(total_car_cost)}) minus public pass ({_fmt_curr(public_transport_monthly_pass)})",
        f"1 Mark: Accuracy – correct savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Find total fuel used: ({total_km} / 100) × 8,0 = {litres_needed:.1f} litres.",
        "tier_2": f"Find car total: ({litres_needed:.1f} × {_fmt_curr(petrol_price_per_litre)}) + {_fmt_curr(monthly_parking)} = {_fmt_curr(total_car_cost)}.",
        "tier_3": f"{total_car_cost:.2f} - {public_transport_monthly_pass:.2f} = {savings:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_trans_fuel_cost_vs_public_transport", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_trans_luggage_excess_baggage_charge(r: random.Random) -> Dict[str, Any]:
    """Calculate additional luggage fees for baggage exceeding the free bus passenger allowance."""
    name = r.choice(SA_NAMES)
    actual_mass_kg = r.choice([26, 28, 32, 35, 40])
    free_allowance_kg = 20
    excess_rate_per_kg = round(r.choice([8.50, 10.00, 12.50]), 2)

    excess_kg = actual_mass_kg - free_allowance_kg
    excess_fee = round(excess_kg * excess_rate_per_kg, 2)
    ans_str = _fmt_curr(excess_fee)

    prompt = (
        f"{name} is travelling on a long-distance intercity coach from Johannesburg to Durban. "
        f"{name}'s luggage weighs **{actual_mass_kg} kg**.\n"
        f"The bus company allows **20 kg of baggage free of charge**. "
        f"Any baggage exceeding 20 kg is charged at an excess rate of **{_fmt_curr(excess_rate_per_kg)} per extra kilogram**.\n\n"
        f"Calculate the **excess luggage charge** {name} must pay."
    )
    sol = (
        f"Step 1: Calculate excess baggage mass:\n"
        f"• Free allowance = 20 kg\n"
        f"• Excess Mass = {actual_mass_kg} kg - 20 kg = {excess_kg} kg\n\n"
        f"Step 2: Method setup – multiply excess mass by tariff per kg:\n"
        f"• Excess Fee = {excess_kg} kg × {_fmt_curr(excess_rate_per_kg)} "
        f"✓ [1 Mark: Method – subtracting 20 kg free allowance and multiplying remainder by rate per kg]\n\n"
        f"Step 3: Calculate fee:\n"
        f"Excess Fee = {ans_str} ✓ [1 Mark: Accuracy – correct baggage fee in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating ({actual_mass_kg} - 20) × {_fmt_curr(excess_rate_per_kg)}",
        f"1 Mark: Accuracy – correct fee {ans_str}"
    ]
    hints = {
        "tier_1": f"Subtract the free 20 kg allowance from {actual_mass_kg} kg: {actual_mass_kg} - 20 = {excess_kg} kg.",
        "tier_2": f"Multiply the extra {excess_kg} kg by {_fmt_curr(excess_rate_per_kg)}.",
        "tier_3": f"{excess_kg} × {excess_rate_per_kg:.2f} = {excess_fee:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_trans_luggage_excess_baggage_charge", prompt, ans_str, sol, rubric, hints, 2, r=r)
