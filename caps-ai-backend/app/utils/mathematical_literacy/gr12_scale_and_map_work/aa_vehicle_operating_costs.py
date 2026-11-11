"""Subskills 17 to 24: Automobile Association (AA) Vehicle Operating Rates & TOVC Mechanics.
Covers AA fixed cost table lookups, running cost factors (A, B, C), Total Operating Vehicle Cost (TOVC),
cents to Rands per km conversions, journey operating cost, fuel-only vs full wear-and-tear comparison,
SARS company travel allowance reimbursement, and petrol hike sensitivity analysis.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    AA_FIXED_COST_TABLE,
    AA_RUNNING_COST_TABLE,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Subskill 17: Looking up AA Fixed Cost (c/km) using vehicle purchase price and annual mileage brackets."""
    price_brackets = [
        ("R100k-R150k", "R125 000", "20 001 - 30 000 km", "20k-30k", 118),
        ("R150k-R200k", "R180 000", "< 20 000 km", "<20k", 175),
        ("R200k-R250k", "R225 000", "> 30 000 km", ">30k", 150),
        ("R250k-R350k", "R303 000", "> 30 000 km", ">30k", 190),
        ("R350k-R500k", "R420 000", "20 001 - 30 000 km", "20k-30k", 290),
    ]
    p_bracket, purchase_val, mileage_label, km_key, fixed_c = r.choice(price_brackets)

    table_data = {
        "headers": ["Vehicle Purchase Price", "< 20 000 km/yr", "20 001 - 30 000 km/yr", "> 30 000 km/yr"],
        "rows": [
            ["R100 001 - R150 000", "135 c/km", "118 c/km", "95 c/km"],
            ["R150 001 - R200 000", "175 c/km", "145 c/km", "120 c/km"],
            ["R200 001 - R250 000", "215 c/km", "180 c/km", "150 c/km"],
            ["R250 001 - R350 000", "265 c/km", "224 c/km", "190 c/km"],
            ["R350 001 - R500 000", "340 c/km", "290 c/km", "245 c/km"],
        ]
    }

    prompt = (
        f"A motorist owns a vehicle purchased for {purchase_val} and travels an average of "
        f"{mileage_label} per year.\n\n"
        f"Refer to the Automobile Association (AA) Fixed Cost Table below.\n"
        f"Determine the vehicle's Fixed Cost rate in cents per kilometre (c/km)."
    )

    correct_ans = f"{fixed_c} c/km"
    explanation = (
        f"1. Locate row '{p_bracket}' corresponding to purchase price {purchase_val}.\n"
        f"2. Locate column '{mileage_label}'.\n"
        f"3. The intersecting fixed cost value is {correct_ans}."
    )
    t1 = "Find the row matching the vehicle purchase price and the column matching annual mileage."
    t2 = f"Row: {purchase_val}, Column: {mileage_label}."
    t3 = f"Fixed cost = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_17",
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


def gen_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Subskill 18: Looking up AA Running Cost factors: Fuel factor A, Service B, Tyre C based on engine cc."""
    engine_choices = [
        ("1300cc", "1 300 cc", 7.15, 18.50, 14.20),
        ("1600cc", "1 600 cc", 8.03, 22.73, 16.70),
        ("2000cc", "2 000 cc", 9.45, 28.10, 22.40),
        ("2700cc", "2 700 cc (Minibus)", 10.96, 35.97, 31.70),
    ]
    code, label, a, b, c = r.choice(engine_choices)

    table_data = {
        "headers": ["Engine Capacity (cc)", "Fuel Factor (A)", "Service & Repair (B)", "Tyre Cost (C)"],
        "rows": [
            ["1 201 - 1 500 cc", "7,15", "18,50 c/km", "14,20 c/km"],
            ["1 501 - 1 800 cc", "8,03", "22,73 c/km", "16,70 c/km"],
            ["1 801 - 2 200 cc", "9,45", "28,10 c/km", "22,40 c/km"],
            ["2 501 - 3 000 cc", "10,96", "35,97 c/km", "31,70 c/km"],
        ]
    }

    prompt = (
        f"A commercial fleet operates vehicles with an engine capacity of {label}.\n\n"
        f"Refer to the AA Running Costs Table below.\n"
        f"Identify the values for Fuel Factor (A), Service/Repair factor (B in c/km), and Tyre factor (C in c/km)."
    )

    correct_ans = f"A = {_fmt(a)}, B = {_fmt(b)} c/km, C = {_fmt(c)} c/km"
    explanation = (
        f"1. Locate the row corresponding to {label}.\n"
        f"2. Values: Fuel factor A = {_fmt(a)}, Service B = {_fmt(b)} c/km, Tyre C = {_fmt(c)} c/km."
    )
    t1 = "Read across the row matching the vehicle engine capacity."
    t2 = f"Values for {label}: A = {_fmt(a)}, B = {_fmt(b)}, C = {_fmt(c)}."
    t3 = f"Running factors: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"A = {_fmt(a + 1.2)}, B = {_fmt(b)} c/km, C = {_fmt(c)} c/km",
        f"A = {_fmt(a)}, B = {_fmt(b + 5)}, C = {_fmt(c - 2)} c/km",
        f"A = {_fmt(a)}, B = {_fmt(c)} c/km, C = {_fmt(b)} c/km",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_18",
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


def gen_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Subskill 19: Calculating Total Operating Vehicle Cost (TOVC in c/km) using the AA formula."""
    fixed_c = r.choice([118.0, 145.0, 180.0, 224.0])
    a = r.choice([8.03, 9.45, 10.96])
    b = r.choice([22.73, 28.10, 35.97])
    c = r.choice([16.70, 22.40, 31.70])
    fuel_price_r = r.choice([21.50, 22.80, 23.45])

    # Formula: TOVC = Fixed + (A * fuel_price_r) + B + C
    fuel_component = round(a * fuel_price_r, 2)
    tovc_ckm = round(fixed_c + fuel_component + b + c, 2)

    prompt = (
        f"A vehicle has the following AA cost parameters:\n"
        f"• Fixed cost = {_fmt(fixed_c)} c/km\n"
        f"• Fuel factor (A) = {_fmt(a)}\n"
        f"• Service & repair (B) = {_fmt(b)} c/km\n"
        f"• Tyre cost (C) = {_fmt(c)} c/km\n"
        f"• Current petrol price = {_fmt_curr(fuel_price_r)} per litre\n\n"
        f"Formula: TOVC (c/km) = Fixed Cost + (A × Fuel Price in Rands) + B + C\n"
        f"Calculate the Total Operating Vehicle Cost in cents per kilometre (c/km)."
    )

    correct_ans = f"{_fmt(tovc_ckm)} c/km"
    explanation = (
        f"1. Fuel cost component = A × Fuel Price = {_fmt(a)} × {_fmt(fuel_price_r)} = {_fmt(fuel_component)} c/km.\n"
        f"2. TOVC = {_fmt(fixed_c)} + {_fmt(fuel_component)} + {_fmt(b)} + {_fmt(c)} = {correct_ans}."
    )
    t1 = "Multiply fuel factor A by petrol price in Rands, then add Fixed cost, B, and C."
    t2 = f"Fuel component = {fuel_component} c/km. Total = {fixed_c} + {fuel_component} + {b} + {c}."
    t3 = f"TOVC = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_19",
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


def gen_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Subskill 20: Converting TOVC from cents per km to Rands per km."""
    tovc_c = r.choice([285.45, 342.18, 421.87, 510.60])
    tovc_r = round(tovc_c / 100.0, 2)

    prompt = (
        f"A delivery van's calculated Total Operating Vehicle Cost is {_fmt(tovc_c)} c/km.\n\n"
        f"Given that 100 cents = R 1,00:\n"
        f"Convert this operating cost into Rands per kilometre (R/km), rounded to 2 decimal places."
    )

    correct_ans = f"R {_fmt(tovc_r)}/km"
    explanation = (
        f"1. Divide cents by 100: {_fmt(tovc_c)} c/km ÷ 100 = R {_fmt(tovc_r)}/km.\n"
        f"2. Result: {correct_ans}."
    )
    t1 = "Divide the cents per kilometre value by 100 to convert to Rands."
    t2 = f"{tovc_c} ÷ 100 = {tovc_r}."
    t3 = f"Cost = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"R {_fmt(tovc_r * 10)}/km",
        f"R {_fmt(tovc_r / 10)}/km",
        f"R {_fmt(tovc_c)}/km",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_20",
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


def gen_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Total operating cost of a specific journey (Distance x TOVC)."""
    dist_km = r.choice([450, 560, 680, 1004])
    rate_r_per_km = r.choice([3.45, 3.80, 4.20, 4.65])
    total_cost = round(dist_km * rate_r_per_km, 2)

    prompt = (
        f"A company representative drives {_fmt(dist_km)} km for client consultations.\n"
        f"The audited vehicle operating cost is {_fmt_curr(rate_r_per_km)} per kilometre (including fuel and wear & tear).\n\n"
        f"Using the formula: Total Cost = Distance (km) × Cost per km,\n"
        f"calculate the total actual vehicle operating cost for this journey."
    )

    correct_ans = _fmt_curr(total_cost)
    explanation = (
        f"1. Total Cost = {_fmt(dist_km)} km × {_fmt_curr(rate_r_per_km)}/km = {correct_ans}."
    )
    t1 = "Multiply the journey distance in kilometres by the rate per kilometre."
    t2 = f"Calculation: {dist_km} × {rate_r_per_km}."
    t3 = f"Operating cost = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_21",
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


def gen_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Subskill 22: Fuel-only cost vs total operating cost (wear and tear depreciation comparison)."""
    dist_km = r.choice([600, 800, 1000])
    # Fuel only: 8 L/100 km at R 23,45/L = R 1,88/km
    fuel_rate_km = 1.88
    full_tovc_km = 4.20

    fuel_cost = round(dist_km * fuel_rate_km, 2)
    total_cost = round(dist_km * full_tovc_km, 2)
    wear_tear_diff = round(total_cost - fuel_cost, 2)

    prompt = (
        f"A motorist undertakes a {_fmt(dist_km)} km road trip.\n"
        f"• Fuel-only rate = {_fmt_curr(fuel_rate_km)} per km\n"
        f"• Full operating rate (including depreciation, tyres, service) = {_fmt_curr(full_tovc_km)} per km\n\n"
        f"1. Calculate the fuel-only cost.\n"
        f"2. Calculate the full operating cost.\n"
        f"3. Determine how much additional cost is incurred through vehicle wear, tear, and depreciation."
    )

    correct_ans = f"Fuel: {_fmt_curr(fuel_cost)}, Total: {_fmt_curr(total_cost)} (Wear & Tear: {_fmt_curr(wear_tear_diff)})"
    explanation = (
        f"1. Fuel cost = {_fmt(dist_km)} km × {_fmt_curr(fuel_rate_km)} = {_fmt_curr(fuel_cost)}.\n"
        f"2. Full cost = {_fmt(dist_km)} km × {_fmt_curr(full_tovc_km)} = {_fmt_curr(total_cost)}.\n"
        f"3. Wear & tear = {_fmt_curr(total_cost)} − {_fmt_curr(fuel_cost)} = {_fmt_curr(wear_tear_diff)}."
    )
    t1 = "Calculate fuel cost and full operating cost, then subtract fuel from total."
    t2 = f"Fuel = {_fmt_curr(fuel_cost)}. Full = {_fmt_curr(total_cost)}. Difference = {_fmt_curr(wear_tear_diff)}."
    t3 = f"Cost comparison: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Fuel: {_fmt_curr(fuel_cost)}, Total: {_fmt_curr(total_cost)} (Wear & Tear: {_fmt_curr(fuel_cost)})",
        f"Fuel: {_fmt_curr(fuel_cost * 1.15)}, Total: {_fmt_curr(total_cost)} (Wear & Tear: {_fmt_curr(wear_tear_diff - 100)})",
        f"Fuel: {_fmt_curr(fuel_cost)}, Total: {_fmt_curr(total_cost * 1.10)} (Wear & Tear: {_fmt_curr(wear_tear_diff + 200)})",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_22",
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


def gen_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Subskill 23: Company travel allowance reimbursement: SARS gazetted rate vs actual vehicle cost."""
    dist_km = r.choice([350, 480, 620])
    sars_rate = 4.84  # Standard SARS travel allowance rate R 4,84/km
    actual_tovc = r.choice([3.85, 4.10, 4.25])

    reimbursement = round(dist_km * sars_rate, 2)
    actual_cost = round(dist_km * actual_tovc, 2)
    surplus = round(reimbursement - actual_cost, 2)

    prompt = (
        f"An employer reimburses an employee for business travel at the gazetted SARS rate of "
        f"{_fmt_curr(sars_rate)} per kilometre.\n"
        f"The employee travels {_fmt(dist_km)} km for work. Her vehicle's actual operating cost is "
        f"{_fmt_curr(actual_tovc)} per km.\n\n"
        f"1. Calculate the total reimbursement received from the employer.\n"
        f"2. Calculate the actual vehicle operating cost incurred.\n"
        f"3. Determine the employee's financial gain (surplus) from the reimbursement."
    )

    correct_ans = f"Reimbursed: {_fmt_curr(reimbursement)}, Actual: {_fmt_curr(actual_cost)} (Surplus: {_fmt_curr(surplus)})"
    explanation = (
        f"1. Reimbursement = {_fmt(dist_km)} km × {_fmt_curr(sars_rate)}/km = {_fmt_curr(reimbursement)}.\n"
        f"2. Actual cost = {_fmt(dist_km)} km × {_fmt_curr(actual_tovc)}/km = {_fmt_curr(actual_cost)}.\n"
        f"3. Surplus = {_fmt_curr(reimbursement)} − {_fmt_curr(actual_cost)} = {_fmt_curr(surplus)}."
    )
    t1 = "Multiply distance by SARS rate for reimbursement, and distance by actual rate for costs. Subtract for surplus."
    t2 = f"Reimbursed = {_fmt_curr(reimbursement)}, Cost = {_fmt_curr(actual_cost)}, Surplus = {_fmt_curr(surplus)}."
    t3 = f"Results: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Reimbursed: {_fmt_curr(reimbursement)}, Actual: {_fmt_curr(actual_cost)} (Surplus: {_fmt_curr(surplus * 1.5)})",
        f"Reimbursed: {_fmt_curr(actual_cost)}, Actual: {_fmt_curr(reimbursement)} (Surplus: -{_fmt_curr(surplus)})",
        f"Reimbursed: {_fmt_curr(reimbursement)}, Actual: {_fmt_curr(actual_cost)} (Surplus: {_fmt_curr(surplus / 2)})",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_23",
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


def gen_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Subskill 24: Percentage change in vehicle operating cost following a petrol price increase."""
    tovc_old = 350.0  # c/km
    factor_a = 8.03
    petrol_increase_r = r.choice([1.20, 1.50, 1.80, 2.10])  # increase in Rands per litre

    # Increase in TOVC in cents = factor_a * petrol_increase_r
    increase_c = round(factor_a * petrol_increase_r, 2)
    tovc_new = round(tovc_old + increase_c, 2)
    pct_increase = round((increase_c / tovc_old) * 100.0, 1)

    prompt = (
        f"A sedan's baseline operating cost is {_fmt(tovc_old, 2)} c/km, with a Fuel Factor A = {_fmt(factor_a)}.\n"
        f"The Department of Mineral Resources and Energy announces a petrol price hike of "
        f"{_fmt_curr(petrol_increase_r)} per litre.\n\n"
        f"1. Calculate the increase in vehicle operating cost in c/km (Increase = A × Petrol Price Hike).\n"
        f"2. Calculate the new total operating cost (TOVC) in c/km.\n"
        f"3. Calculate the percentage increase in total operating costs (to 1 decimal place)."
    )

    correct_ans = f"+{_fmt(increase_c)} c/km -> {_fmt(tovc_new)} c/km (+{_fmt(pct_increase, 1)}%)"
    explanation = (
        f"1. Cost increase = {_fmt(factor_a)} × {_fmt(petrol_increase_r)} = {_fmt(increase_c)} c/km.\n"
        f"2. New TOVC = {_fmt(tovc_old)} + {_fmt(increase_c)} = {_fmt(tovc_new)} c/km.\n"
        f"3. % Increase = ({_fmt(increase_c)} ÷ {_fmt(tovc_old)}) × 100% = {_fmt(pct_increase, 1)}%."
    )
    t1 = "Multiply factor A by the petrol hike. Add to old TOVC, then calculate % increase."
    t2 = f"Increase = {increase_c} c/km. New = {tovc_new} c/km. % = {pct_increase}%."
    t3 = f"Impact: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"+{_fmt(increase_c * 2)} c/km -> {_fmt(tovc_old + increase_c * 2)} c/km (+{_fmt(pct_increase * 2, 1)}%)",
        f"+{_fmt(increase_c)} c/km -> {_fmt(tovc_new)} c/km (+{_fmt(pct_increase + 3, 1)}%)",
        f"+{_fmt(increase_c / 2)} c/km -> {_fmt(tovc_old + increase_c / 2)} c/km (+{_fmt(pct_increase / 2, 1)}%)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_24",
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
