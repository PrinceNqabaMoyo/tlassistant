"""Telephone & Cellular Tariffs Subskills (Subskills 28 to 35).

28. fin_tar_phone_contract_subscription_plus_extras
29. fin_tar_phone_per_second_billing_call_cost
30. fin_tar_phone_in_network_vs_cross_network_rate
31. fin_tar_phone_airtime_balance_deductions
32. fin_tar_phone_data_bundle_vs_out_of_bundle_cost
33. fin_tar_phone_sms_bundle_unit_cost_comparison
34. fin_tar_phone_airtime_depletion_call_duration
35. fin_tar_phone_peak_vs_off_peak_call_rate
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_fin_tar_phone_contract_subscription_plus_extras(r: random.Random) -> Dict[str, Any]:
    """Calculate monthly cell phone bill: Subscription + mandatory itemised billing + extra usage."""
    name = r.choice(SA_NAMES)
    sub_fee = round(r.choice([99.00, 129.00, 149.00, 199.00]), 2)
    itemised_billing = 22.00
    cli_charge = 9.50  # Caller line identity
    extra_calls = round(r.choice([35.50, 48.20, 62.00, 75.80]), 2)

    total_bill = round(sub_fee + itemised_billing + cli_charge + extra_calls, 2)
    ans_str = _fmt_curr(total_bill)

    prompt = (
        f"{name} has a monthly cellular contract with the following charges:\n"
        f"• **Monthly Subscription**: {_fmt_curr(sub_fee)}\n"
        f"• **Mandatory Itemised Billing**: {_fmt_curr(itemised_billing)}\n"
        f"• **Caller Line Identity (CLI)**: {_fmt_curr(cli_charge)}\n"
        f"• **Out-of-bundle call charges**: {_fmt_curr(extra_calls)}\n\n"
        f"Calculate the **total cell phone bill** for {name} for this month."
    )
    sol = (
        f"Step 1: Identify all line items on the cellular invoice:\n"
        f"• Subscription = {_fmt_curr(sub_fee)}\n"
        f"• Itemised billing = {_fmt_curr(itemised_billing)}\n"
        f"• CLI = {_fmt_curr(cli_charge)}\n"
        f"• Out-of-bundle usage = {_fmt_curr(extra_calls)}\n\n"
        f"Step 2: Method setup – sum all contract and usage charges:\n"
        f"• Total Bill = {_fmt_curr(sub_fee)} + {_fmt_curr(itemised_billing)} + {_fmt_curr(cli_charge)} + {_fmt_curr(extra_calls)} "
        f"✓ [1 Mark: Method – summing subscription, billing fees, and out-of-bundle usage]\n\n"
        f"Step 3: Calculate total:\n"
        f"Total Bill = {ans_str} ✓ [1 Mark: Accuracy – correct cell phone bill in Rands]"
    )
    rubric = [
        f"1 Mark: Method – summing {_fmt_curr(sub_fee)}, {_fmt_curr(itemised_billing)}, {_fmt_curr(cli_charge)}, and {_fmt_curr(extra_calls)}",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": "Add up every charge listed on the statement.",
        "tier_2": f"Calculate: {sub_fee:.2f} + {itemised_billing:.2f} + {cli_charge:.2f} + {extra_calls:.2f}.",
        "tier_3": f"Sum = {total_bill:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_phone_contract_subscription_plus_extras", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_phone_per_second_billing_call_cost(r: random.Random) -> Dict[str, Any]:
    """Calculate the cost of a phone call using per-second billing rate."""
    name = r.choice(SA_NAMES)
    minutes = r.choice([3, 4, 5, 6])
    seconds = r.choice([15, 20, 30, 45])
    total_seconds = (minutes * 60) + seconds
    rate_per_min = 1.80  # R 1.80 per 60 seconds = R 0.03 per second

    call_cost = round(total_seconds * (rate_per_min / 60), 2)
    ans_str = _fmt_curr(call_cost)

    prompt = (
        f"{name} makes a phone call that lasts **{minutes} minutes and {seconds} seconds**.\n"
        f"The cellular network uses per-second billing at a tariff rate of **{_fmt_curr(rate_per_min)} per minute (60 seconds)**.\n\n"
        f"1. Convert the total call duration to seconds: $$\\text{{Seconds}} = ({minutes} \\times 60) + {seconds}$$\n"
        f"2. Calculate the **total cost of the call in Rands**."
    )
    sol = (
        f"Step 1: Convert call duration into total seconds:\n"
        f"• Total Seconds = ({minutes} × 60) + {seconds} = {minutes * 60} + {seconds} = {total_seconds} seconds\n\n"
        f"Step 2: Method setup – calculate per-second rate and multiply by duration:\n"
        f"• Rate per second = {_fmt_curr(rate_per_min)} ÷ 60 = R {rate_per_min / 60:.4f}/sec\n"
        f"• Call Cost = {total_seconds} seconds × (R {rate_per_min / 60:.4f}) "
        f"✓ [1 Mark: Method – converting time to {total_seconds} seconds and multiplying by per-second rate]\n\n"
        f"Step 3: Calculate total cost:\n"
        f"Call Cost = {ans_str} ✓ [1 Mark: Accuracy – correct call cost in Rands]"
    )
    rubric = [
        f"1 Mark: Method – evaluating (({minutes} × 60 + {seconds}) / 60) × {_fmt_curr(rate_per_min)}",
        f"1 Mark: Accuracy – correct call cost {ans_str}"
    ]
    hints = {
        "tier_1": f"Convert {minutes} minutes {seconds} seconds into total seconds: ({minutes} × 60) + {seconds} = {total_seconds} s.",
        "tier_2": f"Divide {total_seconds} by 60, then multiply by {_fmt_curr(rate_per_min)}.",
        "tier_3": f"({total_seconds} / 60) × {rate_per_min} = {call_cost:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_phone_per_second_billing_call_cost", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_phone_in_network_vs_cross_network_rate(r: random.Random) -> Dict[str, Any]:
    """Compare call costs between in-network calls and cross-network calls."""
    name = r.choice(SA_NAMES)
    duration_min = r.choice([6, 8, 10, 12, 15])
    in_network_rate = 0.99
    cross_network_rate = 1.75

    in_net_cost = round(duration_min * in_network_rate, 2)
    cross_net_cost = round(duration_min * cross_network_rate, 2)
    savings = round(cross_net_cost - in_net_cost, 2)
    ans_str = _fmt_curr(savings)

    prompt = (
        f"{name} is planning a phone call lasting **{duration_min} minutes**.\n"
        f"The network charges:\n"
        f"• **Same-network calls**: {_fmt_curr(in_network_rate)} per minute\n"
        f"• **Cross-network calls (other networks)**: {_fmt_curr(cross_network_rate)} per minute\n\n"
        f"Calculate **how much money** {name} saves if the call is made to a friend on the same network "
        f"instead of a different network."
    )
    sol = (
        f"Step 1: Calculate the call cost on both networks:\n"
        f"• Same Network = {duration_min} × {_fmt_curr(in_network_rate)} = {_fmt_curr(in_net_cost)}\n"
        f"• Cross Network = {duration_min} × {_fmt_curr(cross_network_rate)} = {_fmt_curr(cross_net_cost)}\n\n"
        f"Step 2: Method setup – calculate savings:\n"
        f"• Savings = Cross Network Cost - Same Network Cost\n"
        f"• Savings = {_fmt_curr(cross_net_cost)} - {_fmt_curr(in_net_cost)} "
        f"✓ [1 Mark: Method – evaluating both rates for {duration_min} minutes and finding difference]\n\n"
        f"Step 3: Calculate savings:\n"
        f"Savings = {ans_str} ✓ [1 Mark: Accuracy – correct savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating ({duration_min} × {_fmt_curr(cross_network_rate)}) - ({duration_min} × {_fmt_curr(in_network_rate)})",
        f"1 Mark: Accuracy – correct savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Work out cross-network cost: {duration_min} × {_fmt_curr(cross_network_rate)}.",
        "tier_2": f"Work out same-network cost: {duration_min} × {_fmt_curr(in_network_rate)}.",
        "tier_3": f"{cross_net_cost:.2f} - {in_net_cost:.2f} = {savings:.2f}, giving {ans_str}."
    }
    d_spec = {
        "diagram_role": "context",
        "kind": "double_bar_graph",
        "title": f"Call Cost Comparison ({duration_min} minutes)",
        "categories": ["In-Network", "Cross-Network"],
        "values": [in_net_cost, cross_net_cost],
    }
    return _make_q("fin_tar_phone_in_network_vs_cross_network_rate", prompt, ans_str, sol, rubric, hints, 2, r=r, diagram_spec=d_spec)


def _gen_fin_tar_phone_airtime_balance_deductions(r: random.Random) -> Dict[str, Any]:
    """Track remaining airtime after deducting call charges, international SMSs, and MMSs."""
    name = r.choice(SA_NAMES)
    start_airtime = 150.00
    calls_spent = round(r.choice([45.50, 52.00, 64.80, 72.50]), 2)
    intl_sms_count = r.choice([3, 4, 5])
    intl_sms_rate = 1.25
    mms_count = r.choice([2, 4])
    mms_rate = 0.80

    intl_sms_cost = round(intl_sms_count * intl_sms_rate, 2)
    mms_cost = round(mms_count * mms_rate, 2)
    total_deductions = round(calls_spent + intl_sms_cost + mms_cost, 2)
    remaining_airtime = round(start_airtime - total_deductions, 2)
    ans_str = _fmt_curr(remaining_airtime)

    prompt = (
        f"{name} starts the month with **{_fmt_curr(start_airtime)}** worth of airtime credit.\n"
        f"During the month, {name} uses:\n"
        f"• **Voice calls**: {_fmt_curr(calls_spent)}\n"
        f"• **{intl_sms_count} International SMSs** at {_fmt_curr(intl_sms_rate)} each\n"
        f"• **{mms_count} MMS messages** at {_fmt_curr(mms_rate)} each\n"
        f"*(Note: 30 local SMSs were sent but were covered by a free monthly bundle).*\n\n"
        f"Calculate {name}'s **remaining airtime balance** at the end of the month."
    )
    sol = (
        f"Step 1: Calculate the billable usage costs:\n"
        f"• Voice calls = {_fmt_curr(calls_spent)}\n"
        f"• International SMSs = {intl_sms_count} × {_fmt_curr(intl_sms_rate)} = {_fmt_curr(intl_sms_cost)}\n"
        f"• MMSs = {mms_count} × {_fmt_curr(mms_rate)} = {_fmt_curr(mms_cost)}\n"
        f"• Total Usage = {_fmt_curr(calls_spent)} + {_fmt_curr(intl_sms_cost)} + {_fmt_curr(mms_cost)} = {_fmt_curr(total_deductions)}\n\n"
        f"Step 2: Method setup – deduct usage from starting airtime:\n"
        f"• Remaining = {_fmt_curr(start_airtime)} - {_fmt_curr(total_deductions)} "
        f"✓ [1 Mark: Method – summing chargeable usage and subtracting from starting balance]\n\n"
        f"Step 3: Calculate remaining balance:\n"
        f"Remaining Airtime = {ans_str} ✓ [1 Mark: Accuracy – correct remaining airtime in Rands]"
    )
    rubric = [
        f"1 Mark: Method – subtracting ({_fmt_curr(calls_spent)} + {_fmt_curr(intl_sms_cost)} + {_fmt_curr(mms_cost)}) from {_fmt_curr(start_airtime)}",
        f"1 Mark: Accuracy – correct remainder {ans_str}"
    ]
    hints = {
        "tier_1": f"Calculate the cost of the international SMSs and MMSs, then add them to the call costs ({_fmt_curr(calls_spent)}).",
        "tier_2": f"Subtract the total usage from the starting {_fmt_curr(start_airtime)}.",
        "tier_3": f"{start_airtime} - {total_deductions:.2f} = {remaining_airtime:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_phone_airtime_balance_deductions", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_phone_data_bundle_vs_out_of_bundle_cost(r: random.Random) -> Dict[str, Any]:
    """Compare upfront data bundle pricing against out-of-bundle pay-as-you-go rates."""
    name = r.choice(SA_NAMES)
    bundle_size_mb = 1000  # 1 GB = 1 000 MB
    bundle_price = 85.00
    out_of_bundle_rate_per_mb = 0.29  # R 0.29 per MB

    oob_total = round(bundle_size_mb * out_of_bundle_rate_per_mb, 2)
    savings = round(oob_total - bundle_price, 2)
    ans_str = _fmt_curr(savings)

    prompt = (
        f"{name} needs **1 000 MB (1 GB)** of mobile data for school projects.\n"
        f"• **Option 1 (Upfront Data Bundle)**: {_fmt_curr(bundle_price)} for 1 000 MB\n"
        f"• **Option 2 (Out-of-Bundle Pay-As-You-Go)**: {_fmt_curr(out_of_bundle_rate_per_mb)} per MB\n\n"
        f"Calculate **how much money** {name} saves by purchasing the upfront data bundle instead of using out-of-bundle data."
    )
    sol = (
        f"Step 1: Calculate the cost under out-of-bundle rates:\n"
        f"• Out-of-Bundle Cost = 1 000 MB × {_fmt_curr(out_of_bundle_rate_per_mb)}/MB = {_fmt_curr(oob_total)}\n\n"
        f"Step 2: Method setup – calculate savings:\n"
        f"• Savings = Out-of-Bundle Cost - Bundle Price\n"
        f"• Savings = {_fmt_curr(oob_total)} - {_fmt_curr(bundle_price)} "
        f"✓ [1 Mark: Method – calculating out-of-bundle total and subtracting bundle price]\n\n"
        f"Step 3: Calculate savings:\n"
        f"Savings = {ans_str} ✓ [1 Mark: Accuracy – correct savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating (1 000 × {_fmt_curr(out_of_bundle_rate_per_mb)}) - {_fmt_curr(bundle_price)}",
        f"1 Mark: Accuracy – correct savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Work out the out-of-bundle price: 1 000 MB × {_fmt_curr(out_of_bundle_rate_per_mb)} = {_fmt_curr(oob_total)}.",
        "tier_2": f"Subtract the bundle price ({_fmt_curr(bundle_price)}) from that total.",
        "tier_3": f"{oob_total:.2f} - {bundle_price:.2f} = {savings:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_phone_data_bundle_vs_out_of_bundle_cost", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_phone_sms_bundle_unit_cost_comparison(r: random.Random) -> Dict[str, Any]:
    """Calculate the unit cost per SMS in a bulk bundle and determine whether it is cheaper than standard rate."""
    name = r.choice(SA_NAMES)
    bundle_sms_count = r.choice([100, 125, 150, 200])
    bundle_cost = round(r.choice([55.00, 68.75, 78.75, 95.00]), 2)
    standard_rate = 0.60

    unit_cost = round(bundle_cost / bundle_sms_count, 2)
    is_cheaper = unit_cost < standard_rate

    if is_cheaper:
        ans_str = f"Yes, cheaper at {_fmt_curr(unit_cost)} per SMS"
        distractors = [
            f"No, more expensive at {_fmt_curr(unit_cost)} per SMS",
            f"Same price as standard {_fmt_curr(standard_rate)} rate",
            "Cannot be determined without call records"
        ]
    else:
        ans_str = f"No, more expensive at {_fmt_curr(unit_cost)} per SMS"
        distractors = [
            f"Yes, cheaper at {_fmt_curr(unit_cost)} per SMS",
            f"Same price as standard {_fmt_curr(standard_rate)} rate",
            "Cannot be determined without call records"
        ]

    prompt = (
        f"{name}'s network offers an optional SMS bundle: **{bundle_sms_count} SMSs for {_fmt_curr(bundle_cost)}**.\n"
        f"The standard ad-hoc SMS rate is **{_fmt_curr(standard_rate)} per SMS**.\n\n"
        f"1. Calculate the cost per SMS in the bundle: $$\\text{{Unit Cost}} = {_fmt_curr(bundle_cost)} \\div {bundle_sms_count}$$\n"
        f"2. Determine whether this bundle is a better (cheaper) deal than the standard rate."
    )
    sol = (
        f"Step 1: Calculate unit cost per SMS in the bundle:\n"
        f"• Unit Cost = {_fmt_curr(bundle_cost)} ÷ {bundle_sms_count} = {_fmt_curr(unit_cost)} per SMS\n\n"
        f"Step 2: Method setup – compare unit cost with standard rate ({_fmt_curr(standard_rate)}):\n"
        f"• Bundle unit cost = {_fmt_curr(unit_cost)} vs Standard rate = {_fmt_curr(standard_rate)}\n"
        f"✓ [1 Mark: Method – dividing bundle cost by {bundle_sms_count} and comparing with standard rate]\n\n"
        f"Step 3: Final verdict:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct comparison verdict]"
    )
    rubric = [
        f"1 Mark: Method – dividing {_fmt_curr(bundle_cost)} by {bundle_sms_count} and comparing to {_fmt_curr(standard_rate)}",
        f"1 Mark: Accuracy – {ans_str}"
    ]
    hints = {
        "tier_1": f"Divide the bundle price ({_fmt_curr(bundle_cost)}) by the number of messages ({bundle_sms_count}).",
        "tier_2": f"Compare that cost per SMS to the standard {_fmt_curr(standard_rate)} rate.",
        "tier_3": f"The answer is: {ans_str}."
    }
    return _make_q(
        "fin_tar_phone_sms_bundle_unit_cost_comparison",
        prompt, ans_str, sol, rubric, hints, 2, options=[ans_str] + distractors, r=r
    )


def _gen_fin_tar_phone_airtime_depletion_call_duration(r: random.Random) -> Dict[str, Any]:
    """Calculate call duration in hours and minutes supported by a given airtime balance."""
    name = r.choice(SA_NAMES)
    total_airtime = 140.00
    first_tier_minutes = 5
    tier1_rate = 1.95
    tier2_rate = 1.55

    cost_tier1 = round(first_tier_minutes * tier1_rate, 2)  # R 9.75
    rem_airtime = round(total_airtime - cost_tier1, 2)        # R 130.25

    rem_minutes = int(round(rem_airtime / tier2_rate))
    total_minutes = first_tier_minutes + rem_minutes

    hours = total_minutes // 60
    minutes = total_minutes % 60
    ans_str = f"{hours} hour(s) and {minutes} minutes"

    prompt = (
        f"{name} has **{_fmt_curr(total_airtime)}** in airtime credit and makes a continuous cross-network phone call.\n"
        f"The network tariff charges:\n"
        f"• **First 5 minutes**: {_fmt_curr(tier1_rate)} per minute\n"
        f"• **Thereafter**: {_fmt_curr(tier2_rate)} per minute\n\n"
        f"Calculate the **maximum duration of the call (in hours and minutes)**, rounded to the nearest minute, "
        f"before the airtime runs out completely."
    )
    sol = (
        f"Step 1: Calculate cost of the first 5 minutes:\n"
        f"• First 5 minutes = 5 × {_fmt_curr(tier1_rate)} = {_fmt_curr(cost_tier1)}\n"
        f"• Remaining airtime = {_fmt_curr(total_airtime)} - {_fmt_curr(cost_tier1)} = {_fmt_curr(rem_airtime)}\n\n"
        f"Step 2: Method setup – divide remaining airtime by tier 2 rate and convert to hours:\n"
        f"• Remaining minutes = {_fmt_curr(rem_airtime)} ÷ {_fmt_curr(tier2_rate)} = {rem_airtime / tier2_rate:.2f} ≈ {rem_minutes} minutes\n"
        f"• Total minutes = 5 + {rem_minutes} = {total_minutes} minutes\n"
        f"• Hours and minutes: {total_minutes} ÷ 60 = {hours} hr and {minutes} min\n"
        f"✓ [1 Mark: Method – subtracting tier 1 cost, dividing by tier 2 rate, and converting minutes to hours and minutes]\n\n"
        f"Step 3: Final duration:\n"
        f"Duration = {ans_str} ✓ [1 Mark: Accuracy – correct time in hours and minutes]"
    )
    rubric = [
        f"1 Mark: Method – evaluating 5 + (({total_airtime} - {cost_tier1}) / {tier2_rate}) and converting to hours/mins",
        f"1 Mark: Accuracy – correct duration {ans_str}"
    ]
    hints = {
        "tier_1": f"First subtract the cost of the first 5 minutes (5 × {_fmt_curr(tier1_rate)} = {_fmt_curr(cost_tier1)}).",
        "tier_2": f"Divide the remaining {_fmt_curr(rem_airtime)} by {_fmt_curr(tier2_rate)} to get additional minutes, then add 5.",
        "tier_3": f"Total time = {total_minutes} minutes, which equals {ans_str}."
    }
    return _make_q("fin_tar_phone_airtime_depletion_call_duration", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_phone_peak_vs_off_peak_call_rate(r: random.Random) -> Dict[str, Any]:
    """Compare phone call costs between peak hours and off-peak hours."""
    name = r.choice(SA_NAMES)
    minutes = r.choice([15, 20, 25, 30])
    peak_rate = 2.10
    off_peak_rate = 1.15

    peak_cost = round(minutes * peak_rate, 2)
    off_peak_cost = round(minutes * off_peak_rate, 2)
    savings = round(peak_cost - off_peak_cost, 2)
    ans_str = _fmt_curr(savings)

    prompt = (
        f"{name} needs to make a **{minutes}-minute** business phone call.\n"
        f"The telecommunications tariff schedule lists:\n"
        f"• **Peak Rate (07:00 – 20:00 weekdays)**: {_fmt_curr(peak_rate)} per minute\n"
        f"• **Off-Peak Rate (Evenings and weekends)**: {_fmt_curr(off_peak_rate)} per minute\n\n"
        f"Calculate **how much money** {name} saves by waiting until off-peak hours to make this call."
    )
    sol = (
        f"Step 1: Calculate call cost under peak and off-peak rates:\n"
        f"• Peak Cost = {minutes} × {_fmt_curr(peak_rate)} = {_fmt_curr(peak_cost)}\n"
        f"• Off-Peak Cost = {minutes} × {_fmt_curr(off_peak_rate)} = {_fmt_curr(off_peak_cost)}\n\n"
        f"Step 2: Method setup – calculate the difference (savings):\n"
        f"• Savings = Peak Cost - Off-Peak Cost\n"
        f"• Savings = {_fmt_curr(peak_cost)} - {_fmt_curr(off_peak_cost)} "
        f"✓ [1 Mark: Method – evaluating {minutes} minutes at both rates and finding difference]\n\n"
        f"Step 3: Calculate savings:\n"
        f"Savings = {ans_str} ✓ [1 Mark: Accuracy – correct savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating ({minutes} × {_fmt_curr(peak_rate)}) - ({minutes} × {_fmt_curr(off_peak_rate)})",
        f"1 Mark: Accuracy – correct savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Work out the peak cost: {minutes} × {_fmt_curr(peak_rate)}.",
        "tier_2": f"Work out the off-peak cost: {minutes} × {_fmt_curr(off_peak_rate)}.",
        "tier_3": f"{peak_cost:.2f} - {off_peak_cost:.2f} = {savings:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_phone_peak_vs_off_peak_call_rate", prompt, ans_str, sol, rubric, hints, 2, r=r)
