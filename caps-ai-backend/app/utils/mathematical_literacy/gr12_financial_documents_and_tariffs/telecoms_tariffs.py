"""Subskills 17 to 24: Telecommunications, Mobile Data & Broadband Tariffs.
Covers per-second vs per-minute billing, in-bundle vs out-of-bundle minutes,
data package comparisons, contract break-even points, 24-month total device cost, and international roaming.
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


def gen_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Subskill 17: Prepaid call costs: per-second billing vs per-minute rounding."""
    call_secs = r.randint(65, 115)  # e.g. 1 min 25 secs
    rate_per_sec = 0.025  # R1,50 per minute = R0,025 per sec
    rate_per_min = 1.50

    cost_per_second = round(call_secs * rate_per_sec, 2)
    # Per-minute billing rounds up to next full minute (2 minutes)
    minutes_rounded = 2 if call_secs <= 120 else 3
    cost_per_minute = round(minutes_rounded * rate_per_min, 2)
    diff = round(cost_per_minute - cost_per_second, 2)

    d_spec_17 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Prepaid Call Cost Comparison ({call_secs} seconds)",
        "categories": ["Plan A (Per-Second)", "Plan B (Per-Minute)"],
        "series": [
            {"name": "Cost", "values": [cost_per_second, cost_per_minute]}
        ],
    }

    prompt = (
        f"Refer to the prepaid call cost comparison for a phone call lasting {call_secs} seconds.\n"
        f"• Plan A (Per-Second Billing): R 0,025 per second (no rounding up)\n"
        f"• Plan B (Per-Minute Billing): R 1,50 per minute (or part thereof, rounded up to the next full minute)\n\n"
        f"How much more does the call cost on Plan B than on Plan A?"
    )

    correct_ans = _fmt_curr(diff)
    explanation = (
        f"1. Plan A (Per-Second): {call_secs} seconds × R 0,025/sec = {_fmt_curr(cost_per_second)}.\n"
        f"2. Plan B (Per-Minute): {call_secs} seconds rounds up to {minutes_rounded} full minutes.\n"
        f"   Cost = {minutes_rounded} min × R 1,50/min = {_fmt_curr(cost_per_minute)}.\n"
        f"3. Difference = {_fmt_curr(cost_per_minute)} - {_fmt_curr(cost_per_second)} = {_fmt_curr(diff)}."
    )
    t1 = f"Multiply {call_secs} by R 0,025 to find Plan A cost."
    t2 = f"Round {call_secs} seconds up to {minutes_rounded} minutes and multiply by R 1,50 for Plan B."
    t3 = f"Subtract Plan A from Plan B: {_fmt_curr(cost_per_minute)} - {_fmt_curr(cost_per_second)} = {_fmt_curr(diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_17",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_17,
    )


def gen_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Subskill 18: Monthly cellphone contract with inclusive minutes plus out-of-bundle usage."""
    name = r.choice(SA_NAMES)
    monthly_sub = r.choice([299.0, 399.0, 499.0])
    inclusive_mins = r.choice([150, 200, 250])
    actual_mins = inclusive_mins + r.randint(35, 75)
    oob_rate = 1.65  # out-of-bundle rate per min

    extra_mins = actual_mins - inclusive_mins
    extra_cost = round(extra_mins * oob_rate, 2)
    total_bill = round(monthly_sub + extra_cost, 2)

    prompt = (
        f"{name} is on a contract with a monthly subscription of {_fmt_curr(monthly_sub)} that includes {inclusive_mins} voice minutes.\n"
        f"Any additional minutes used beyond the included allowance are charged at an out-of-bundle rate of {_fmt_curr(oob_rate)} per minute.\n\n"
        f"During September, {name} made {actual_mins} minutes of calls.\n"
        f"Calculate {name}'s total monthly bill (assuming all prices include VAT)."
    )

    correct_ans = _fmt_curr(total_bill)
    explanation = (
        f"1. Extra out-of-bundle minutes = {actual_mins} - {inclusive_mins} = {extra_mins} minutes.\n"
        f"2. Cost of extra minutes = {extra_mins} min × {_fmt_curr(oob_rate)} = {_fmt_curr(extra_cost)}.\n"
        f"3. Total bill = Subscription ({_fmt_curr(monthly_sub)}) + Extra calls ({_fmt_curr(extra_cost)}) = {_fmt_curr(total_bill)}."
    )
    t1 = "Find the excess minutes by subtracting inclusive minutes from total minutes."
    t2 = f"Multiply the {extra_mins} excess minutes by {_fmt_curr(oob_rate)}."
    t3 = f"Add the subscription fee: {_fmt_curr(monthly_sub)} + {_fmt_curr(extra_cost)} = {_fmt_curr(total_bill)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_18",
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


def gen_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Subskill 19: Mobile data costs: 30-day bundle vs punitive out-of-bundle rates."""
    data_mb = r.randint(1200, 1800)  # e.g. 1 500 MB
    bundle_cost = 149.00  # 2 GB bundle (2048 MB)
    oob_rate_per_mb = 0.29  # 29c per MB

    oob_cost = round(data_mb * oob_rate_per_mb, 2)
    diff = round(oob_cost - bundle_cost, 2)

    prompt = (
        f"A smartphone user consumes {data_mb} MB of data in a month.\n"
        f"The mobile network charges an out-of-bundle rate of 29 cents (R 0,29) per MB if no bundle is loaded.\n"
        f"Alternatively, a 30-day 2 GB (2 048 MB) bundle can be purchased upfront for R 149,00.\n\n"
        f"Calculate how much money the user saves by buying the 2 GB bundle instead of paying out-of-bundle rates."
    )

    correct_ans = _fmt_curr(diff)
    explanation = (
        f"1. Out-of-bundle cost = {data_mb} MB × R 0,29/MB = {_fmt_curr(oob_cost)}.\n"
        f"2. Upfront 2 GB bundle cost = {_fmt_curr(bundle_cost)}.\n"
        f"3. Savings = {_fmt_curr(oob_cost)} - {_fmt_curr(bundle_cost)} = {_fmt_curr(diff)}."
    )
    t1 = f"Calculate the out-of-bundle cost: {data_mb} MB × R 0,29."
    t2 = f"Subtract the fixed bundle price ({_fmt_curr(bundle_cost)}) from the out-of-bundle cost."
    t3 = f"Savings = {_fmt_curr(oob_cost)} - {_fmt_curr(bundle_cost)} = {_fmt_curr(diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_19",
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


def gen_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Subskill 20: Comparing two cellular contracts for a given monthly call volume."""
    name = r.choice(SA_NAMES)
    mins = r.choice([160, 220, 280])

    # Package 1: R150 subscription + R1,20 per minute
    # Package 2: R280 subscription + R0,60 per minute
    c1 = round(150.0 + (mins * 1.20), 2)
    c2 = round(280.0 + (mins * 0.60), 2)
    diff = round(abs(c1 - c2), 2)
    cheaper = "Package 1" if c1 < c2 else "Package 2"

    prompt = (
        f"{name} makes an average of {mins} minutes of calls per month and is evaluating two contract packages:\n\n"
        f"• Package 1: Monthly fee R 150,00 plus R 1,20 per minute\n"
        f"• Package 2: Monthly fee R 280,00 plus R 0,60 per minute\n\n"
        f"Calculate the monthly difference in cost between the two packages."
    )

    correct_ans = _fmt_curr(diff)
    explanation = (
        f"1. Package 1: R 150,00 + ({mins} × R 1,20) = R 150,00 + R {mins * 1.20:.2f} = {_fmt_curr(c1)}.\n"
        f"2. Package 2: R 280,00 + ({mins} × R 0,60) = R 280,00 + R {mins * 0.60:.2f} = {_fmt_curr(c2)}.\n"
        f"3. Difference = |{_fmt_curr(c1)} - {_fmt_curr(c2)}| = {_fmt_curr(diff)}.\n"
        f"   {cheaper} is cheaper by {_fmt_curr(diff)}."
    )
    t1 = f"Calculate the total cost for Package 1: R 150,00 + ({mins} × R 1,20)."
    t2 = f"Calculate the total cost for Package 2: R 280,00 + ({mins} × R 0,60)."
    t3 = f"Find the difference: |{_fmt_curr(c1)} - {_fmt_curr(c2)}| = {_fmt_curr(diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_20",
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


def gen_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Finding break-even call minutes between two contract packages."""
    # Package A: R120 + R1,50/min
    # Package B: R270 + R0,75/min
    # 120 + 1.50*x = 270 + 0.75*x => 0.75*x = 150 => x = 200 minutes
    sub_a, rate_a = 120.0, 1.50
    sub_b, rate_b = 270.0, 0.75
    break_even_mins = int(round((sub_b - sub_a) / (rate_a - rate_b)))

    prompt = (
        f"Consider two mobile contract options:\n"
        f"• Contract A: R 120,00 monthly fee + R 1,50 per call minute\n"
        f"• Contract B: R 270,00 monthly fee + R 0,75 per call minute\n\n"
        f"At how many call minutes per month will both contracts cost exactly the same amount (the break-even point)?"
    )

    correct_ans = f"{break_even_mins} minutes"
    explanation = (
        f"1. Set up the equation: Total Cost A = Total Cost B.\n"
        f"   R 120,00 + 1,50m = R 270,00 + 0,75m.\n"
        f"2. Rearrange terms: 1,50m - 0,75m = R 270,00 - R 120,00.\n"
        f"   0,75m = 150,00.\n"
        f"3. Solve for m: m = 150 ÷ 0,75 = {break_even_mins} minutes."
    )
    t1 = "Set the cost equations equal to each other: 120 + 1,50m = 270 + 0,75m."
    t2 = "Group the minute variables on the left and the fixed fees on the right: (1,50 - 0,75)m = 270 - 120."
    t3 = f"Divide the difference in monthly fees (150) by the difference in rates (0,75): m = {break_even_mins} minutes."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_21",
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


def gen_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Subskill 22: Home fibre broadband tariffs: uncapped packages vs capped with top-ups."""
    name = r.choice(SA_NAMES)
    uncapped_fee = 799.00  # 50 Mbps uncapped
    capped_fee = 499.00    # 50 Mbps 200 GB cap
    topup_rate = 45.00     # R45 per 20 GB top-up bundle

    used_gb = r.choice([360, 400, 440])  # usage in GB
    excess_gb = used_gb - 200
    topup_bundles_needed = int((excess_gb + 19) // 20)  # ceiling division
    capped_total = capped_fee + (topup_bundles_needed * topup_rate)
    diff = round(capped_total - uncapped_fee, 2)

    prompt = (
        f"{name}'s household requires a 50 Mbps fibre internet line and consumed {used_gb} GB last month.\n\n"
        f"The internet service provider offers two billing structures:\n"
        f"• Package X (Uncapped): Fixed R 799,00 per month with no data limits\n"
        f"• Package Y (Capped): R 499,00 per month including 200 GB data. Additional data costs R 45,00 per 20 GB bundle\n\n"
        f"Calculate how much extra {name} would pay on Package Y compared to Package X for consuming {used_gb} GB."
    )

    correct_ans = _fmt_curr(diff)
    explanation = (
        f"1. Package X total = {_fmt_curr(uncapped_fee)}.\n"
        f"2. Package Y: Excess data = {used_gb} GB - 200 GB = {excess_gb} GB.\n"
        f"   Number of 20 GB top-up bundles needed = {excess_gb} ÷ 20 = {topup_bundles_needed} bundles.\n"
        f"   Top-up cost = {topup_bundles_needed} × R 45,00 = {_fmt_curr(topup_bundles_needed * topup_rate)}.\n"
        f"   Package Y total = R 499,00 + {_fmt_curr(topup_bundles_needed * topup_rate)} = {_fmt_curr(capped_total)}.\n"
        f"3. Difference = {_fmt_curr(capped_total)} - {_fmt_curr(uncapped_fee)} = {_fmt_curr(diff)}."
    )
    t1 = f"Calculate excess data beyond 200 GB: {used_gb} - 200 = {excess_gb} GB."
    t2 = f"Determine required 20 GB bundles ({topup_bundles_needed}) and add top-up cost to R 499,00."
    t3 = f"Calculate difference: {_fmt_curr(capped_total)} - {_fmt_curr(uncapped_fee)} = {_fmt_curr(diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_22",
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
    """Subskill 23: Total cost of a 24-month smartphone contract including handset, line rental & insurance."""
    name = r.choice(SA_NAMES)
    phone_model = r.choice(["Samsung Galaxy A54", "iPhone 13", "Xiaomi Redmi Note 12", "Oppo Reno 8"])
    monthly_plan = r.choice([399.0, 449.0, 529.0])
    insurance = 89.00
    once_off_sim = 150.00

    total_24m = round((monthly_plan + insurance) * 24 + once_off_sim, 2)

    prompt = (
        f"{name} signs a 24-month contract for a {phone_model}.\n"
        f"The contract schedule itemises the following expenses:\n"
        f"• Monthly plan fee (device + voice & data bundle): {_fmt_curr(monthly_plan)}\n"
        f"• Monthly comprehensive device insurance: {_fmt_curr(insurance)}\n"
        f"• Once-off SIM and connection activation fee: {_fmt_curr(once_off_sim)}\n\n"
        f"Calculate the total financial commitment for {name} over the entire 24-month contract term."
    )

    correct_ans = _fmt_curr(total_24m)
    explanation = (
        f"1. Total monthly payment = Plan ({_fmt_curr(monthly_plan)}) + Insurance ({_fmt_curr(insurance)}) = {_fmt_curr(monthly_plan + insurance)}.\n"
        f"2. Total over 24 months = {_fmt_curr(monthly_plan + insurance)} × 24 = {_fmt_curr((monthly_plan + insurance) * 24)}.\n"
        f"3. Add once-off fee = {_fmt_curr((monthly_plan + insurance) * 24)} + {_fmt_curr(once_off_sim)} = {_fmt_curr(total_24m)}."
    )
    t1 = f"Add the monthly plan fee ({_fmt_curr(monthly_plan)}) and monthly insurance ({_fmt_curr(insurance)})."
    t2 = f"Multiply monthly total by 24 months, then add the once-off fee ({_fmt_curr(once_off_sim)})."
    t3 = f"Total = [({monthly_plan} + {insurance}) × 24] + {once_off_sim} = {_fmt_curr(total_24m)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_23",
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


def gen_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Subskill 24: International roaming data and voice tariff calculation."""
    name = r.choice(SA_NAMES)
    destination = r.choice(["United Kingdom", "United States", "Mauritius", "Australia"])
    roam_data_mb = r.randint(150, 350)
    roam_calls_mins = r.randint(12, 28)

    rate_data_per_mb = 2.50  # R2,50 per MB
    rate_calls_per_min = 18.00  # R18,00 per min

    cost_data = round(roam_data_mb * rate_data_per_mb, 2)
    cost_calls = round(roam_calls_mins * rate_calls_per_min, 2)
    total_roam = round(cost_data + cost_calls, 2)

    prompt = (
        f"{name} travelled to {destination} for a week with international roaming activated on a South African SIM:\n"
        f"• Roaming Data Rate: {_fmt_curr(rate_data_per_mb)} per MB ({roam_data_mb} MB used)\n"
        f"• Roaming Voice Calls: {_fmt_curr(rate_calls_per_min)} per minute ({roam_calls_mins} minutes spoken)\n\n"
        f"Calculate {name}'s total international roaming bill for the trip."
    )

    correct_ans = _fmt_curr(total_roam)
    explanation = (
        f"1. Roaming data cost = {roam_data_mb} MB × {_fmt_curr(rate_data_per_mb)} = {_fmt_curr(cost_data)}.\n"
        f"2. Roaming calls cost = {roam_calls_mins} min × {_fmt_curr(rate_calls_per_min)} = {_fmt_curr(cost_calls)}.\n"
        f"3. Total roaming bill = {_fmt_curr(cost_data)} + {_fmt_curr(cost_calls)} = {_fmt_curr(total_roam)}."
    )
    t1 = f"Multiply roaming data MB by {_fmt_curr(rate_data_per_mb)}."
    t2 = f"Multiply roaming call minutes by {_fmt_curr(rate_calls_per_min)}."
    t3 = f"Sum both charges: {_fmt_curr(cost_data)} + {_fmt_curr(cost_calls)} = {_fmt_curr(total_roam)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_24",
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
