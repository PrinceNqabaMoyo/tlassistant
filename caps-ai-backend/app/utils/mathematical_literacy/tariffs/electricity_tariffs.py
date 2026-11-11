"""Stepped / Sliding-Scale Electricity Tariffs Subskills (Subskills 10 to 18).

10. fin_tar_elec_single_block_consumption
11. fin_tar_elec_two_tier_stepped_calculation
12. fin_tar_elec_three_tier_stepped_calculation
13. fin_tar_elec_fixed_service_charge_plus_stepped
14. fin_tar_elec_cents_to_rands_conversion
15. fin_tar_elec_prepaid_electricity_token_units
16. fin_tar_elec_seasonal_summer_vs_winter_tariff
17. fin_tar_elec_appliance_energy_consumption_cost
18. fin_tar_elec_average_unit_cost_comparison
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_fin_tar_elec_single_block_consumption(r: random.Random) -> Dict[str, Any]:
    """Calculate domestic electricity cost where consumption falls completely within Block 1."""
    name = r.choice(SA_NAMES)
    kwh = r.choice([80, 95, 110, 125, 140, 148])
    rate_cents = 129.05  # Standard Cape Town Block 1 tariff from textbook Activity 4-5

    total_cents = round(kwh * rate_cents, 2)
    total_rands = round(total_cents / 100, 2)
    ans_str = _fmt_curr(total_rands)

    prompt = (
        f"{name}'s household uses **{kwh} kWh** of electricity in a month.\n"
        f"The municipal domestic electricity tariff schedule states:\n\n"
        f"| Block Number | Consumption Range | Tariff (cents per kWh, incl. VAT) |\n"
        f"| :--- | :---: | :---: |\n"
        f"| Block 1 | 0 – 150 kWh | 129,05 c |\n"
        f"| Block 2 | 150,1 – 350 kWh | 134,65 c |\n"
        f"| Block 3 | 350,1 – 600 kWh | 159,81 c |\n\n"
        f"Calculate {name}'s **electricity bill in Rands** for this month."
    )
    sol = (
        f"Step 1: Determine applicable tariff block:\n"
        f"• Consumption = {kwh} kWh, which falls entirely in **Block 1** (0 – 150 kWh).\n"
        f"• Applicable rate = 129,05 cents per kWh = R 1,2905 per kWh\n\n"
        f"Step 2: Method setup – multiply consumption by Block 1 tariff:\n"
        f"• Total Cents = {kwh} × 129,05 c = {_fmt(total_cents)} c\n"
        f"• Total Rands = {_fmt(total_cents)} ÷ 100 "
        f"✓ [1 Mark: Method – multiplying {kwh} kWh by 129,05 c and converting to Rands]\n\n"
        f"Step 3: Calculate final cost in Rands:\n"
        f"Bill = {ans_str} ✓ [1 Mark: Accuracy – correct electricity cost in Rands]"
    )
    rubric = [
        f"1 Mark: Method – evaluating ({kwh} × 129,05) / 100",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": f"Since {kwh} is less than 150 kWh, all units are charged at 129,05 cents per kWh.",
        "tier_2": f"Multiply {kwh} by 129,05 cents, then divide by 100 to convert to Rands.",
        "tier_3": f"({kwh} × 129,05) ÷ 100 = {total_rands:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_elec_single_block_consumption", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_elec_two_tier_stepped_calculation(r: random.Random) -> Dict[str, Any]:
    """Calculate domestic electricity cost crossing from Block 1 into Block 2."""
    name = r.choice(SA_NAMES)
    total_kwh = r.choice([180, 200, 225, 250, 280, 310])
    block1_limit = 150
    rate1 = 1.30  # R 1.30 per kWh
    rate2 = 1.65  # R 1.65 per kWh

    b1_kwh = block1_limit
    b2_kwh = total_kwh - block1_limit

    cost_b1 = round(b1_kwh * rate1, 2)
    cost_b2 = round(b2_kwh * rate2, 2)
    total_bill = round(cost_b1 + cost_b2, 2)
    ans_str = _fmt_curr(total_bill)

    prompt = (
        f"{name}'s household consumes **{total_kwh} kWh** of electricity during the month.\n"
        f"The municipal stepped electricity tariff structure is as follows:\n\n"
        f"| Tariff Step | Block Range | Rate (R/kWh) |\n"
        f"| :--- | :---: | :---: |\n"
        f"| Block 1 | First 150 kWh | {_fmt_curr(rate1)} per kWh |\n"
        f"| Block 2 | Remaining units above 150 kWh | {_fmt_curr(rate2)} per kWh |\n\n"
        f"Calculate the **total electricity cost (in Rands)** for the month."
    )
    sol = (
        f"Step 1: Partition consumption into stepped blocks:\n"
        f"• Block 1 (First 150 kWh) = 150 kWh\n"
        f"• Block 2 (Remaining) = {total_kwh} - 150 = {b2_kwh} kWh\n\n"
        f"Step 2: Method setup – calculate cost for each block:\n"
        f"• Block 1 Cost = 150 × {_fmt_curr(rate1)} = {_fmt_curr(cost_b1)}\n"
        f"• Block 2 Cost = {b2_kwh} × {_fmt_curr(rate2)} = {_fmt_curr(cost_b2)}\n"
        f"• Total Bill = {_fmt_curr(cost_b1)} + {_fmt_curr(cost_b2)} "
        f"✓ [1 Mark: Method – splitting into 150 kWh @ {_fmt_curr(rate1)} and {b2_kwh} kWh @ {_fmt_curr(rate2)}]\n\n"
        f"Step 3: Calculate sum:\n"
        f"Total Bill = {ans_str} ✓ [1 Mark: Accuracy – correct total in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating (150 × {_fmt_curr(rate1)}) + ({b2_kwh} × {_fmt_curr(rate2)})",
        f"1 Mark: Accuracy – correct bill {ans_str}"
    ]
    hints = {
        "tier_1": f"The first 150 kWh is charged at {_fmt_curr(rate1)}; the remaining {b2_kwh} kWh is charged at {_fmt_curr(rate2)}.",
        "tier_2": f"Calculate (150 × {rate1}) + ({b2_kwh} × {rate2}).",
        "tier_3": f"{cost_b1:.2f} + {cost_b2:.2f} = {total_bill:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_elec_two_tier_stepped_calculation", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_elec_three_tier_stepped_calculation(r: random.Random) -> Dict[str, Any]:
    """Calculate domestic electricity cost spanning three consecutive stepped blocks."""
    name = r.choice(SA_NAMES)
    total_kwh = r.choice([380, 420, 460, 500, 550])

    # Block 1: 0 - 150 kWh @ R 1.25
    # Block 2: 151 - 350 kWh (200 kWh) @ R 1.60
    # Block 3: > 350 kWh @ R 2.10
    rate1, rate2, rate3 = 1.25, 1.60, 2.10
    b1_kwh = 150
    b2_kwh = 200
    b3_kwh = total_kwh - 350

    c1 = round(b1_kwh * rate1, 2)
    c2 = round(b2_kwh * rate2, 2)
    c3 = round(b3_kwh * rate3, 2)
    total_cost = round(c1 + c2 + c3, 2)
    ans_str = _fmt_curr(total_cost)

    prompt = (
        f"{name}'s household consumed **{total_kwh} kWh** of electricity in a month.\n"
        f"The stepped block tariff is charged as follows:\n\n"
        f"| Step | Consumption Block | Tariff Rate |\n"
        f"| :--- | :---: | :---: |\n"
        f"| Block 1 | 0 – 150 kWh | {_fmt_curr(rate1)} / kWh |\n"
        f"| Block 2 | 151 – 350 kWh | {_fmt_curr(rate2)} / kWh |\n"
        f"| Block 3 | Above 350 kWh | {_fmt_curr(rate3)} / kWh |\n\n"
        f"Calculate the **total cost of electricity** for the month."
    )
    sol = (
        f"Step 1: Break down {total_kwh} kWh into the three blocks:\n"
        f"• Block 1 = 150 kWh (at {_fmt_curr(rate1)})\n"
        f"• Block 2 = 350 - 150 = 200 kWh (at {_fmt_curr(rate2)})\n"
        f"• Block 3 = {total_kwh} - 350 = {b3_kwh} kWh (at {_fmt_curr(rate3)})\n\n"
        f"Step 2: Method setup – calculate cost for each tier and sum:\n"
        f"• Block 1: 150 × {_fmt_curr(rate1)} = {_fmt_curr(c1)}\n"
        f"• Block 2: 200 × {_fmt_curr(rate2)} = {_fmt_curr(c2)}\n"
        f"• Block 3: {b3_kwh} × {_fmt_curr(rate3)} = {_fmt_curr(c3)}\n"
        f"• Total = {_fmt_curr(c1)} + {_fmt_curr(c2)} + {_fmt_curr(c3)} "
        f"✓ [1 Mark: Method – calculating each of the 3 stepped tiers correctly]\n\n"
        f"Step 3: Calculate total bill:\n"
        f"Total Bill = {ans_str} ✓ [1 Mark: Accuracy – correct total in Rands]"
    )
    rubric = [
        f"1 Mark: Method – evaluating ({b1_kwh} × {_fmt_curr(rate1)}) + ({b2_kwh} × {_fmt_curr(rate2)}) + ({b3_kwh} × {_fmt_curr(rate3)})",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": f"Divide the {total_kwh} kWh into: 150 kWh in Block 1, 200 kWh in Block 2, and {b3_kwh} kWh in Block 3.",
        "tier_2": f"Multiply each block by its respective rate, then sum the three amounts.",
        "tier_3": f"{c1:.2f} + {c2:.2f} + {c3:.2f} = {total_cost:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_elec_three_tier_stepped_calculation", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_elec_fixed_service_charge_plus_stepped(r: random.Random) -> Dict[str, Any]:
    """Calculate total electricity cost: Fixed network/service fee + consumption charges."""
    name = r.choice(SA_NAMES)
    kwh = r.choice([220, 260, 310, 350, 420])
    fixed_charge = round(r.choice([145.00, 180.50, 215.54, 250.00]), 2)
    rate_per_kwh = round(r.choice([1.45, 1.55, 1.68]), 2)

    usage_cost = round(kwh * rate_per_kwh, 2)
    total_bill = round(fixed_charge + usage_cost, 2)
    ans_str = _fmt_curr(total_bill)

    prompt = (
        f"{name}'s municipal electricity account charges a **monthly basic service fee of {_fmt_curr(fixed_charge)}** "
        f"plus a consumption tariff of **{_fmt_curr(rate_per_kwh)} per kWh**.\n\n"
        f"If {name}'s household uses **{kwh} kWh** in a month, calculate the **total electricity charges** payable.\n"
        f"Use the formula: $$\\text{{Total}} = \\text{{Basic Service Fee}} + (\\text{{Consumption (kWh)}} \\times \\text{{Rate per kWh}})$$"
    )
    sol = (
        f"Step 1: Calculate energy usage charge:\n"
        f"• Consumption Charge = {kwh} kWh × {_fmt_curr(rate_per_kwh)} = {_fmt_curr(usage_cost)}\n\n"
        f"Step 2: Method setup – add fixed service fee to consumption cost:\n"
        f"• Total Bill = Fixed Fee + Consumption Charge\n"
        f"• Total Bill = {_fmt_curr(fixed_charge)} + {_fmt_curr(usage_cost)} "
        f"✓ [1 Mark: Method – multiplying {kwh} by {_fmt_curr(rate_per_kwh)} and adding fixed service fee]\n\n"
        f"Step 3: Calculate total:\n"
        f"Total Bill = {ans_str} ✓ [1 Mark: Accuracy – correct total in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating {_fmt_curr(fixed_charge)} + ({kwh} × {_fmt_curr(rate_per_kwh)})",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": f"Multiply {kwh} kWh by {_fmt_curr(rate_per_kwh)} to get the consumption cost.",
        "tier_2": f"Add the fixed basic service fee of {_fmt_curr(fixed_charge)}.",
        "tier_3": f"{fixed_charge:.2f} + ({kwh} × {rate_per_kwh:.2f}) = {total_bill:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_elec_fixed_service_charge_plus_stepped", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_elec_cents_to_rands_conversion(r: random.Random) -> Dict[str, Any]:
    """Convert electricity calculated in cents to Rands and cents."""
    kwh = r.choice([160, 210, 275, 340, 420])
    rate_cents = round(r.choice([135.40, 142.80, 155.60, 168.25]), 2)
    cents_total = round(kwh * rate_cents, 2)
    rands_total = round(cents_total / 100, 2)
    ans_str = _fmt_curr(rands_total)

    prompt = (
        f"A household consumes **{kwh} kWh** of electricity at a tariff of **{_fmt(rate_cents)} cents per kWh**.\n\n"
        f"1. Calculate the total cost in cents.\n"
        f"2. Convert the total cost to **Rands and cents**, rounded to the nearest cent."
    )
    sol = (
        f"Step 1: Calculate total cost in cents:\n"
        f"• Total Cents = {kwh} × {_fmt(rate_cents)} c = {_fmt(cents_total)} cents\n\n"
        f"Step 2: Method setup – convert cents to Rands by dividing by 100:\n"
        f"• Cost in Rands = {_fmt(cents_total)} c ÷ 100 "
        f"✓ [1 Mark: Method – multiplying kWh by cents tariff and dividing by 100]\n\n"
        f"Step 3: Express in Rands:\n"
        f"Cost in Rands = {ans_str} ✓ [1 Mark: Accuracy – correct amount in Rands]"
    )
    rubric = [
        f"1 Mark: Method – dividing ({kwh} × {rate_cents}) by 100",
        f"1 Mark: Accuracy – correct Rands {ans_str}"
    ]
    hints = {
        "tier_1": f"Multiply {kwh} by {_fmt(rate_cents)} cents.",
        "tier_2": "Divide the cents by 100 to convert to Rands.",
        "tier_3": f"({kwh} × {rate_cents}) ÷ 100 = {rands_total:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_elec_cents_to_rands_conversion", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_elec_prepaid_electricity_token_units(r: random.Random) -> Dict[str, Any]:
    """Calculate how many kWh units of prepaid electricity are received for a given cash budget."""
    name = r.choice(SA_NAMES)
    budget = r.choice([200, 300, 400, 500, 600])
    rate_per_kwh = round(r.choice([1.60, 1.80, 2.00, 2.25]), 2)

    kwh_units = round(budget / rate_per_kwh, 2)
    ans_str = f"{_fmt(kwh_units)} kWh"

    prompt = (
        f"{name} purchases prepaid electricity at a supermarket vending terminal for **{_fmt_curr(budget)}**.\n"
        f"The prepaid electricity tariff rate is **{_fmt_curr(rate_per_kwh)} per kWh** (VAT inclusive).\n\n"
        f"Calculate the **number of electricity units (kWh)** that will be printed on {name}'s recharge voucher token.\n"
        f"Use the formula: $$\\text{{Units (kWh)}} = \\frac{{\\text{{Amount Paid (R)}}}}{{\\text{{Tariff Rate (R/kWh)}}}}$$"
    )
    sol = (
        f"Step 1: Identify purchase budget and unit tariff:\n"
        f"• Amount paid = {_fmt_curr(budget)}\n"
        f"• Tariff rate = {_fmt_curr(rate_per_kwh)} per kWh\n\n"
        f"Step 2: Method setup – divide budget by rate per kWh:\n"
        f"• Units = {_fmt_curr(budget)} ÷ {_fmt_curr(rate_per_kwh)}\n"
        f"• Units = {budget} ÷ {rate_per_kwh} "
        f"✓ [1 Mark: Method – dividing total spend by price per kWh]\n\n"
        f"Step 3: Calculate units:\n"
        f"Units = {ans_str} ✓ [1 Mark: Accuracy – correct units in kWh]"
    )
    rubric = [
        f"1 Mark: Method – dividing {budget} by {_fmt_curr(rate_per_kwh)}",
        f"1 Mark: Accuracy – correct units {ans_str}"
    ]
    hints = {
        "tier_1": f"Divide the budget of {_fmt_curr(budget)} by the cost per unit ({_fmt_curr(rate_per_kwh)}).",
        "tier_2": f"Calculate: {budget} ÷ {rate_per_kwh}.",
        "tier_3": f"{budget} ÷ {rate_per_kwh:.2f} = {kwh_units:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_elec_prepaid_electricity_token_units", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_elec_seasonal_summer_vs_winter_tariff(r: random.Random) -> Dict[str, Any]:
    """Compare electricity costs under winter high-demand tariffs vs summer low-demand tariffs."""
    name = r.choice(SA_NAMES)
    kwh = r.choice([450, 500, 600, 700])
    summer_rate = 1.45
    winter_rate = 1.95

    summer_cost = round(kwh * summer_rate, 2)
    winter_cost = round(kwh * winter_rate, 2)
    diff = round(winter_cost - summer_cost, 2)
    ans_str = _fmt_curr(diff)

    prompt = (
        f"Eskom applies seasonal tariffs for domestic consumers:\n"
        f"• **Summer (Low-Demand Season)**: {_fmt_curr(summer_rate)} per kWh\n"
        f"• **Winter (High-Demand Season)**: {_fmt_curr(winter_rate)} per kWh\n\n"
        f"If {name}'s household uses **{kwh} kWh** of electricity, calculate **how much more money** "
        f"the electricity will cost in winter than in summer."
    )
    sol = (
        f"Step 1: Calculate the bill for both seasons:\n"
        f"• Summer Bill = {kwh} × {_fmt_curr(summer_rate)} = {_fmt_curr(summer_cost)}\n"
        f"• Winter Bill = {kwh} × {_fmt_curr(winter_rate)} = {_fmt_curr(winter_cost)}\n\n"
        f"Step 2: Method setup – calculate the difference:\n"
        f"• Difference = Winter Bill - Summer Bill\n"
        f"• Difference = {_fmt_curr(winter_cost)} - {_fmt_curr(summer_cost)} "
        f"✓ [1 Mark: Method – evaluating both seasonal tariffs and determining difference]\n\n"
        f"Step 3: Calculate difference:\n"
        f"Difference = {ans_str} ✓ [1 Mark: Accuracy – correct seasonal cost difference in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating ({kwh} × {_fmt_curr(winter_rate)}) - ({kwh} × {_fmt_curr(summer_rate)})",
        f"1 Mark: Accuracy – correct difference {ans_str}"
    ]
    hints = {
        "tier_1": f"Work out summer cost: {kwh} × {_fmt_curr(summer_rate)}.",
        "tier_2": f"Work out winter cost: {kwh} × {_fmt_curr(winter_rate)}.",
        "tier_3": f"{winter_cost:.2f} - {summer_cost:.2f} = {diff:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_elec_seasonal_summer_vs_winter_tariff", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_elec_appliance_energy_consumption_cost(r: random.Random) -> Dict[str, Any]:
    """Calculate the operational electricity cost of running a household appliance."""
    name = r.choice(SA_NAMES)
    appliance = r.choice([
        ("electric heater", 2.0, "2 000 W (2 kW)"),
        ("air conditioner", 1.5, "1 500 W (1,5 kW)"),
        ("tumble dryer", 2.5, "2 500 W (2,5 kW)"),
        ("pool pump", 0.75, "750 W (0,75 kW)")
    ])
    app_name, power_kw, rating_text = appliance
    hours_per_day = r.choice([3, 4, 5, 6])
    days = 30
    tariff_rate = round(r.choice([1.75, 1.95, 2.10, 2.25]), 2)

    total_kwh = round(power_kw * hours_per_day * days, 2)
    monthly_cost = round(total_kwh * tariff_rate, 2)
    ans_str = _fmt_curr(monthly_cost)

    prompt = (
        f"{name} runs an **{app_name}** rated at **{rating_text}** for **{hours_per_day} hours each day** over a **30-day month**.\n"
        f"The electricity tariff rate is **{_fmt_curr(tariff_rate)} per kWh**.\n\n"
        f"Calculate the **monthly electricity running cost** of this appliance.\n"
        f"Use the formulas:\n"
        f"1. $$\\text{{Energy Consumed (kWh)}} = \\text{{Power (kW)}} \\times \\text{{Hours per day}} \\times \\text{{Days}}$$\n"
        f"2. $$\\text{{Cost}} = \\text{{Energy Consumed (kWh)}} \\times \\text{{Tariff Rate (R/kWh)}}$$\n"
    )
    sol = (
        f"Step 1: Calculate total energy consumed in kWh:\n"
        f"• Energy = {power_kw} kW × {hours_per_day} hours/day × {days} days = {_fmt(total_kwh)} kWh\n\n"
        f"Step 2: Method setup – multiply total kWh by tariff rate:\n"
        f"• Monthly Cost = {_fmt(total_kwh)} kWh × {_fmt_curr(tariff_rate)} "
        f"✓ [1 Mark: Method – evaluating total energy in kWh and multiplying by tariff rate]\n\n"
        f"Step 3: Calculate monthly cost:\n"
        f"Monthly Cost = {ans_str} ✓ [1 Mark: Accuracy – correct monthly running cost in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating ({power_kw} × {hours_per_day} × {days}) × {_fmt_curr(tariff_rate)}",
        f"1 Mark: Accuracy – correct running cost {ans_str}"
    ]
    hints = {
        "tier_1": f"First find total kWh used: {power_kw} kW × {hours_per_day} hrs × {days} days.",
        "tier_2": f"Multiply that energy ({_fmt(total_kwh)} kWh) by {_fmt_curr(tariff_rate)}.",
        "tier_3": f"{total_kwh} × {tariff_rate:.2f} = {monthly_cost:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_elec_appliance_energy_consumption_cost", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_elec_average_unit_cost_comparison(r: random.Random) -> Dict[str, Any]:
    """Calculate the effective average cost per kWh from a total electricity invoice."""
    name = r.choice(SA_NAMES)
    kwh = r.choice([350, 420, 500, 650, 800])
    total_bill = round(r.choice([525.00, 680.40, 825.00, 1105.00, 1420.00]), 2)

    avg_cost = round(total_bill / kwh, 2)
    ans_str = f"{_fmt_curr(avg_cost)}/kWh"

    prompt = (
        f"{name}'s municipal electricity account reflects a total charge of **{_fmt_curr(total_bill)}** "
        f"(including fixed fees and VAT) for **{kwh} kWh** of electricity consumed.\n\n"
        f"Calculate the **effective average cost per kilowatt hour (R/kWh)** paid by {name}.\n"
        f"Use the formula: $$\\text{{Average Cost per kWh}} = \\frac{{\\text{{Total Electricity Bill (R)}}}}{{\\text{{Total Energy Consumed (kWh)}}}}$$"
    )
    sol = (
        f"Step 1: Identify total bill and consumption:\n"
        f"• Total Bill = {_fmt_curr(total_bill)}\n"
        f"• Energy Consumed = {kwh} kWh\n\n"
        f"Step 2: Method setup – divide total bill by total kWh:\n"
        f"• Average Cost = {_fmt_curr(total_bill)} ÷ {kwh}\n"
        f"• Average Cost = {total_bill} ÷ {kwh} "
        f"✓ [1 Mark: Method – dividing total electricity bill by total kWh consumed]\n\n"
        f"Step 3: Calculate unit rate:\n"
        f"Average Cost = {ans_str} ✓ [1 Mark: Accuracy – correct average rate per kWh]"
    )
    rubric = [
        f"1 Mark: Method – dividing {_fmt_curr(total_bill)} by {kwh}",
        f"1 Mark: Accuracy – correct average cost {ans_str}"
    ]
    hints = {
        "tier_1": f"Divide the total bill ({_fmt_curr(total_bill)}) by the total units ({kwh} kWh).",
        "tier_2": f"Calculate: {total_bill:.2f} ÷ {kwh}.",
        "tier_3": f"{total_bill:.2f} ÷ {kwh} = {avg_cost:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_elec_average_unit_cost_comparison", prompt, ans_str, sol, rubric, hints, 2, r=r)
