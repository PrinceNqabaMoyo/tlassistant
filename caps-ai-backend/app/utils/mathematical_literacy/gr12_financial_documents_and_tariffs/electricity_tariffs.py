"""Subskills 9 to 16: Domestic & Commercial Electricity Tariffs.
Covers Incline Block Tariffs (IBT), prepaid vs conventional meter comparisons,
Time-of-Use (TOU) commercial rates, prepaid token receipts, appliance consumption costing,
and NERSA annual tariff percentage adjustments.
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    VAT_RATE,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_09(r: random.Random) -> Dict[str, Any]:
    """Subskill 09: Interpreting Incline Block Tariff (IBT) structure for domestic electricity."""
    name = r.choice(SA_NAMES)
    total_kwh = r.randint(420, 580)

    prompt = (
        f"A South African municipal electricity department uses a two-tier Incline Block Tariff (IBT) for domestic prepaid meters:\n\n"
        f"• Block 1: 0 to 350 kWh @ 185,50 cents per kWh (excl. VAT)\n"
        f"• Block 2: > 350 kWh @ 248,20 cents per kWh (excl. VAT)\n\n"
        f"If {name}'s household purchases and consumes a total of {total_kwh} kWh in a calendar month,\n"
        f"how many kWh are charged at the higher Block 2 rate?"
    )

    kwh_in_block_2 = total_kwh - 350
    correct_ans = f"{kwh_in_block_2} kWh"
    explanation = (
        f"1. In an Incline Block Tariff (IBT), Block 1 covers the initial 350 kWh (0 to 350 kWh).\n"
        f"2. Any units consumed exceeding 350 kWh are billed in Block 2.\n"
        f"3. Units in Block 2 = {total_kwh} kWh - 350 kWh = {kwh_in_block_2} kWh."
    )
    t1 = "Subtract the Block 1 limit (350 kWh) from the total kWh consumed."
    t2 = f"Block 1 accounts for 350 kWh. The remaining units ({total_kwh} - 350) fall in Block 2."
    t3 = f"Calculate: {total_kwh} - 350 = {kwh_in_block_2} kWh."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_09",
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


def gen_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: Calculating monthly prepaid electricity cost across two IBT blocks."""
    name = r.choice(SA_NAMES)
    total_kwh = r.randint(400, 550)

    # Rates in Rand/kWh excl VAT
    r_b1 = 1.85
    r_b2 = 2.45

    cost_b1 = round(350 * r_b1, 2)
    kwh_b2 = total_kwh - 350
    cost_b2 = round(kwh_b2 * r_b2, 2)
    total_excl = round(cost_b1 + cost_b2, 2)
    total_incl = round(total_excl * (1 + VAT_RATE), 2)

    prompt = (
        f"{name}'s household used {total_kwh} kWh of prepaid electricity in July.\n"
        f"The municipal domestic IBT rates (excl. VAT) are:\n"
        f"• Block 1 (0 to 350 kWh): {_fmt_curr(r_b1)} per kWh\n"
        f"• Block 2 (> 350 kWh): {_fmt_curr(r_b2)} per kWh\n\n"
        f"Calculate the total cost of electricity including 15% VAT."
    )

    correct_ans = _fmt_curr(total_incl)
    explanation = (
        f"1. Block 1 cost: 350 kWh × {_fmt_curr(r_b1)} = {_fmt_curr(cost_b1)}.\n"
        f"2. Block 2 volume: {total_kwh} - 350 = {kwh_b2} kWh.\n"
        f"3. Block 2 cost: {kwh_b2} kWh × {_fmt_curr(r_b2)} = {_fmt_curr(cost_b2)}.\n"
        f"4. Total excl. VAT = {_fmt_curr(cost_b1)} + {_fmt_curr(cost_b2)} = {_fmt_curr(total_excl)}.\n"
        f"5. Total incl. 15% VAT = {_fmt_curr(total_excl)} × 1,15 = {_fmt_curr(total_incl)}."
    )
    t1 = "Calculate the cost of the first 350 kWh at Block 1 rate."
    t2 = f"Calculate the remaining {kwh_b2} kWh at Block 2 rate and add both amounts."
    t3 = f"Total = ({cost_b1} + {cost_b2}) × 1,15 = {_fmt_curr(total_incl)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_10",
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


def gen_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Subskill 11: Conventional post-paid electricity bill with basic network charge."""
    name = r.choice(SA_NAMES)
    kwh = r.randint(450, 700)
    basic_fee = r.choice([185.00, 210.00, 235.00])
    unit_rate = r.choice([2.15, 2.30, 2.45])

    energy_charge = round(kwh * unit_rate, 2)
    subtotal_excl = round(basic_fee + energy_charge, 2)
    total_incl = round(subtotal_excl * (1 + VAT_RATE), 2)

    prompt = (
        f"{name} has a post-paid conventional electricity meter.\n"
        f"The monthly municipal account includes:\n"
        f"• Basic monthly network and service fee: {_fmt_curr(basic_fee)} (excl. VAT)\n"
        f"• Energy consumption charge: {_fmt_curr(unit_rate)} per kWh (excl. VAT)\n\n"
        f"If {name} used {kwh} kWh of electricity during the month,\n"
        f"calculate the total electricity account payable (including 15% VAT)."
    )

    correct_ans = _fmt_curr(total_incl)
    explanation = (
        f"1. Energy consumption charge = {kwh} kWh × {_fmt_curr(unit_rate)} = {_fmt_curr(energy_charge)}.\n"
        f"2. Subtotal excl. VAT = Basic fee ({_fmt_curr(basic_fee)}) + Energy charge ({_fmt_curr(energy_charge)}) = {_fmt_curr(subtotal_excl)}.\n"
        f"3. Total incl. 15% VAT = {_fmt_curr(subtotal_excl)} × 1,15 = {_fmt_curr(total_incl)}."
    )
    t1 = f"Multiply {kwh} kWh by {_fmt_curr(unit_rate)} to find the energy charge."
    t2 = f"Add the fixed basic fee ({_fmt_curr(basic_fee)}) to the energy charge."
    t3 = f"Total = ({basic_fee} + {energy_charge}) × 1,15 = {_fmt_curr(total_incl)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_11",
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


def gen_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Subskill 12: Cost comparison between prepaid and conventional meter."""
    name = r.choice(SA_NAMES)
    kwh = 300  # low consumption household

    # Prepaid: flat R2,40/kWh, no fixed fee
    cost_prepaid_excl = round(kwh * 2.40, 2)
    cost_prepaid_incl = round(cost_prepaid_excl * 1.15, 2)

    # Conventional: R195 fixed fee + R1,85/kWh
    cost_conv_excl = round(195.00 + (kwh * 1.85), 2)
    cost_conv_incl = round(cost_conv_excl * 1.15, 2)

    diff = round(abs(cost_conv_incl - cost_prepaid_incl), 2)
    cheaper_option = "Prepaid meter" if cost_prepaid_incl < cost_conv_incl else "Conventional meter"

    prompt = (
        f"{name} is deciding between two electricity metering options for an apartment using 300 kWh/month:\n\n"
        f"Option A (Prepaid Meter):\n"
        f"• Fixed monthly fee: R 0,00\n"
        f"• Energy charge: R 2,40 per kWh (excl. VAT)\n\n"
        f"Option B (Conventional Meter):\n"
        f"• Fixed monthly network fee: R 195,00 (excl. VAT)\n"
        f"• Energy charge: R 1,85 per kWh (excl. VAT)\n\n"
        f"Calculate how much {name} saves each month by choosing the cheaper option (incl. 15% VAT)."
    )

    correct_ans = _fmt_curr(diff)
    explanation = (
        f"1. Option A (Prepaid): 300 kWh × R 2,40 = R 720,00 excl. VAT.\n"
        f"   Incl. 15% VAT = R 720,00 × 1,15 = {_fmt_curr(cost_prepaid_incl)}.\n"
        f"2. Option B (Conventional): R 195,00 + (300 × R 1,85) = R 195,00 + R 555,00 = R 750,00 excl. VAT.\n"
        f"   Incl. 15% VAT = R 750,00 × 1,15 = {_fmt_curr(cost_conv_incl)}.\n"
        f"3. Difference = {_fmt_curr(cost_conv_incl)} - {_fmt_curr(cost_prepaid_incl)} = {_fmt_curr(diff)}.\n"
        f"   {cheaper_option} is cheaper by {_fmt_curr(diff)}."
    )
    t1 = "Calculate total cost incl. VAT for both Option A and Option B for 300 kWh."
    t2 = "Option A has zero fixed fee; Option B adds R 195,00 fixed fee before VAT."
    t3 = f"Savings = |{_fmt_curr(cost_conv_incl)} - {_fmt_curr(cost_prepaid_incl)}| = {_fmt_curr(diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_12",
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


def gen_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Time-of-Use (TOU) electricity tariff for a small workshop."""
    biz_name = r.choice(["Bongani Carpentry", "Mokoena Bakery", "Lindiwe Laundromat", "Khaya Auto Repair"])
    kwh_peak = r.randint(180, 260)
    kwh_std = r.randint(320, 440)
    kwh_offpeak = r.randint(220, 310)

    rate_peak = 3.80
    rate_std = 2.10
    rate_offpeak = 1.30

    cost_p = kwh_peak * rate_peak
    cost_s = kwh_std * rate_std
    cost_op = kwh_offpeak * rate_offpeak
    total_excl = round(cost_p + cost_s + cost_op, 2)
    total_incl = round(total_excl * (1 + VAT_RATE), 2)

    prompt = (
        f"{biz_name} operates on a commercial Time-of-Use (TOU) electricity tariff (excl. VAT):\n"
        f"• Peak Hours: {_fmt_curr(rate_peak)}/kWh ({kwh_peak} kWh consumed)\n"
        f"• Standard Hours: {_fmt_curr(rate_std)}/kWh ({kwh_std} kWh consumed)\n"
        f"• Off-Peak Hours: {_fmt_curr(rate_offpeak)}/kWh ({kwh_offpeak} kWh consumed)\n\n"
        f"Calculate the total electricity charge payable including 15% VAT."
    )

    correct_ans = _fmt_curr(total_incl)
    explanation = (
        f"1. Peak cost: {kwh_peak} kWh × {_fmt_curr(rate_peak)} = {_fmt_curr(cost_p)}.\n"
        f"2. Standard cost: {kwh_std} kWh × {_fmt_curr(rate_std)} = {_fmt_curr(cost_s)}.\n"
        f"3. Off-Peak cost: {kwh_offpeak} kWh × {_fmt_curr(rate_offpeak)} = {_fmt_curr(cost_op)}.\n"
        f"4. Total excl. VAT = {_fmt_curr(cost_p)} + {_fmt_curr(cost_s)} + {_fmt_curr(cost_op)} = {_fmt_curr(total_excl)}.\n"
        f"5. Total incl. 15% VAT = {_fmt_curr(total_excl)} × 1,15 = {_fmt_curr(total_incl)}."
    )
    t1 = "Calculate the energy cost for each time bracket (Peak, Standard, Off-Peak)."
    t2 = "Sum all three cost brackets to find total cost before VAT."
    t3 = f"Total = ({cost_p} + {cost_s} + {cost_op}) × 1,15 = {_fmt_curr(total_incl)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_13",
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


def gen_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Subskill 14: Reverse calculation: determining kWh purchased from a prepaid token receipt."""
    name = r.choice(SA_NAMES)
    amount_paid = r.choice([300.0, 450.0, 500.0, 600.0])
    tariff_incl_vat = r.choice([2.30, 2.50, 2.76, 2.85])

    units_purchased = round(amount_paid / tariff_incl_vat, 1)

    prompt = (
        f"{name} purchased a prepaid electricity token at a supermarket for exactly {_fmt_curr(amount_paid)}.\n"
        f"The cash receipt displays the following tariff information:\n"
        f"• Effective Tariff (including 15% VAT): {_fmt_curr(tariff_incl_vat)} per kWh\n"
        f"• Free Basic Electricity (FBE): None allocated\n\n"
        f"Calculate the number of kilowatt-hours (kWh) credited to {name}'s meter (rounded to 1 decimal place)."
    )

    correct_ans = f"{_fmt(units_purchased, 1)} kWh"
    explanation = (
        f"1. When the tariff is already inclusive of VAT, divide total payment by the tariff rate.\n"
        f"2. Units (kWh) = Total Amount Paid ÷ Tariff per kWh.\n"
        f"3. Units = {_fmt_curr(amount_paid)} ÷ {_fmt_curr(tariff_incl_vat)} = {_fmt(units_purchased, 1)} kWh."
    )
    t1 = "Divide the total purchase amount by the tariff rate per kWh."
    t2 = f"Both amounts already include VAT, so no VAT conversion is necessary: {amount_paid} ÷ {tariff_incl_vat}."
    t3 = f"Calculate: {amount_paid} ÷ {tariff_incl_vat} = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_14",
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


def gen_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Subskill 15: Appliance running cost calculation: Power rating (kW) x hours x tariff."""
    appliance = r.choice([
        ("geyser (water heater)", 3.0, 4),
        ("oil heater", 2.0, 6),
        ("tumble dryer", 2.5, 3),
        ("air conditioning unit", 1.8, 8),
    ])
    app_name, kw, hrs_per_day = appliance
    days = 30
    tariff_c_per_kwh = r.choice([235, 250, 275])  # cents

    total_kwh = kw * hrs_per_day * days
    cost_rands = round(total_kwh * (tariff_c_per_kwh / 100.0), 2)

    prompt = (
        f"A domestic {app_name} has an electric power rating of {kw} kW and operates for {hrs_per_day} hours per day.\n"
        f"The municipal electricity tariff is {tariff_c_per_kwh} cents per kWh (incl. VAT).\n\n"
        f"Calculate the total cost to run this appliance over a 30-day month."
    )

    correct_ans = _fmt_curr(cost_rands)
    explanation = (
        f"1. Daily energy consumption = {kw} kW × {hrs_per_day} hours = {kw * hrs_per_day} kWh.\n"
        f"2. Monthly energy consumption (30 days) = {kw * hrs_per_day} kWh/day × 30 days = {total_kwh} kWh.\n"
        f"3. Convert tariff cents to Rands: {tariff_c_per_kwh}c = R {tariff_c_per_kwh / 100:.2f}.\n"
        f"4. Total cost = {total_kwh} kWh × R {tariff_c_per_kwh / 100:.2f} = {_fmt_curr(cost_rands)}."
    )
    t1 = "Calculate total energy in kWh: Power (kW) × Hours per day × 30 days."
    t2 = f"Convert tariff from cents to Rands by dividing by 100: {tariff_c_per_kwh}c = R {tariff_c_per_kwh / 100:.2f}."
    t3 = f"Calculate: {total_kwh} kWh × R {tariff_c_per_kwh / 100:.2f} = {_fmt_curr(cost_rands)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_15",
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


def gen_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Subskill 16: Percentage increase in household electricity bill following NERSA tariff hike."""
    name = r.choice(SA_NAMES)
    old_bill = r.choice([1250.0, 1480.0, 1650.0, 1920.0])
    hike_pct = r.choice([12.74, 14.15, 15.63, 18.65])

    increase_amount = round(old_bill * (hike_pct / 100.0), 2)
    new_bill = round(old_bill + increase_amount, 2)

    prompt = (
        f"Following the National Energy Regulator of South Africa (NERSA) tariff approval,\n"
        f"the municipal electricity tariff increased by {hike_pct}% from 1 July.\n"
        f"Before the increase, {name}'s monthly electricity bill for an average 500 kWh was {_fmt_curr(old_bill)}.\n\n"
        f"Assuming the household maintains the exact same consumption, calculate the new monthly electricity bill."
    )

    correct_ans = _fmt_curr(new_bill)
    explanation = (
        f"1. Calculate the Rand increase: {_fmt_curr(old_bill)} × {hike_pct}% = {_fmt_curr(increase_amount)}.\n"
        f"2. Add the increase to the original bill: {_fmt_curr(old_bill)} + {_fmt_curr(increase_amount)} = {_fmt_curr(new_bill)}.\n"
        f"3. Alternatively, multiply by (1 + {hike_pct}/100) = {_fmt_curr(old_bill)} × {1 + hike_pct/100:.4f} = {_fmt_curr(new_bill)}."
    )
    t1 = f"Calculate {hike_pct}% of the current bill ({_fmt_curr(old_bill)})."
    t2 = f"Add the increase amount to {_fmt_curr(old_bill)}."
    t3 = f"New bill = {_fmt_curr(old_bill)} × (1 + {hike_pct / 100}) = {_fmt_curr(new_bill)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_16",
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
