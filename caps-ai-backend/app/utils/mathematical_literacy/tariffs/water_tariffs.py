"""Stepped / Sliding-Scale Water Tariffs Subskills (Subskills 19 to 27).

19. fin_tar_water_free_basic_water_allowance
20. fin_tar_water_two_tier_stepped_billing
21. fin_tar_water_three_tier_stepped_billing
22. fin_tar_water_drought_level_restriction_tariffs
23. fin_tar_water_convert_litres_to_kilolitres_billing
24. fin_tar_water_step_rate_table_reading_threshold
25. fin_tar_water_daily_consumption_per_person
26. fin_tar_water_dripping_tap_leak_wastage_cost
27. fin_tar_water_jojo_tank_rainwater_savings
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import SA_NAMES, _build_options, _fmt, _fmt_curr, _make_q


def _gen_fin_tar_water_free_basic_water_allowance(r: random.Random) -> Dict[str, Any]:
    """Calculate water cost where the first 6 kL is free basic water and excess is billed at a tier rate."""
    name = r.choice(SA_NAMES)
    total_kl = r.choice([12, 15, 18, 22, 25])
    free_kl = 6.0
    excess_rate = round(r.choice([8.50, 9.75, 11.20, 12.80]), 2)

    billable_kl = total_kl - free_kl
    cost = round(billable_kl * excess_rate, 2)
    ans_str = _fmt_curr(cost)

    prompt = (
        f"{name}'s municipality provides a **Free Basic Water allowance of 6 kL per household per month** (billed at R 0,00).\n"
        f"Any consumption above 6 kL is billed at **{_fmt_curr(excess_rate)} per kL**.\n\n"
        f"If {name}'s household consumes **{total_kl} kL** of water in a month, calculate the **total water charge**."
    )
    sol = (
        f"Step 1: Deduct the 6 kL free basic water allowance:\n"
        f"• Free Allowance = 6 kL @ R 0,00 = R 0,00\n"
        f"• Billable Volume = {total_kl} kL - 6 kL = {billable_kl} kL\n\n"
        f"Step 2: Method setup – multiply billable volume by tariff rate:\n"
        f"• Total Cost = {billable_kl} kL × {_fmt_curr(excess_rate)} "
        f"✓ [1 Mark: Method – subtracting 6 kL free allowance and multiplying remainder by rate per kL]\n\n"
        f"Step 3: Calculate charge:\n"
        f"Total Cost = {ans_str} ✓ [1 Mark: Accuracy – correct water charge in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating ({total_kl} - 6) × {_fmt_curr(excess_rate)}",
        f"1 Mark: Accuracy – correct charge {ans_str}"
    ]
    hints = {
        "tier_1": f"The first 6 kL is free! Subtract 6 from {total_kl} kL.",
        "tier_2": f"Multiply the remaining {billable_kl} kL by {_fmt_curr(excess_rate)}.",
        "tier_3": f"({total_kl} - 6) × {excess_rate:.2f} = {cost:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_water_free_basic_water_allowance", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_water_two_tier_stepped_billing(r: random.Random) -> Dict[str, Any]:
    """Calculate domestic water charges across two stepped tiers."""
    name = r.choice(SA_NAMES)
    total_kl = r.choice([14, 16, 18, 20, 24])
    tier1_limit = 10
    rate1 = 6.80
    rate2 = 12.50

    t1_kl = tier1_limit
    t2_kl = total_kl - tier1_limit

    cost_t1 = round(t1_kl * rate1, 2)
    cost_t2 = round(t2_kl * rate2, 2)
    total_cost = round(cost_t1 + cost_t2, 2)
    ans_str = _fmt_curr(total_cost)

    prompt = (
        f"{name}'s household consumed **{total_kl} kL** of water in a month.\n"
        f"The municipal sliding-scale water tariff is structured as follows:\n\n"
        f"| Step | Consumption Tier | Tariff Rate (R/kL) |\n"
        f"| :--- | :---: | :---: |\n"
        f"| Step 1 | 0 – 10 kL | {_fmt_curr(rate1)} / kL |\n"
        f"| Step 2 | > 10 kL | {_fmt_curr(rate2)} / kL |\n\n"
        f"Calculate the **total water charge** for the month."
    )
    sol = (
        f"Step 1: Partition consumption into the two tiers:\n"
        f"• Step 1 (First 10 kL) = 10 kL\n"
        f"• Step 2 (Remaining) = {total_kl} - 10 = {t2_kl} kL\n\n"
        f"Step 2: Method setup – calculate cost for each tier:\n"
        f"• Step 1 Cost = 10 × {_fmt_curr(rate1)} = {_fmt_curr(cost_t1)}\n"
        f"• Step 2 Cost = {t2_kl} × {_fmt_curr(rate2)} = {_fmt_curr(cost_t2)}\n"
        f"• Total Cost = {_fmt_curr(cost_t1)} + {_fmt_curr(cost_t2)} "
        f"✓ [1 Mark: Method – splitting into 10 kL @ {_fmt_curr(rate1)} and {t2_kl} kL @ {_fmt_curr(rate2)}]\n\n"
        f"Step 3: Calculate sum:\n"
        f"Total Cost = {ans_str} ✓ [1 Mark: Accuracy – correct water bill in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating (10 × {_fmt_curr(rate1)}) + ({t2_kl} × {_fmt_curr(rate2)})",
        f"1 Mark: Accuracy – correct cost {ans_str}"
    ]
    hints = {
        "tier_1": f"The first 10 kL is charged at {_fmt_curr(rate1)}; the remaining {t2_kl} kL is charged at {_fmt_curr(rate2)}.",
        "tier_2": f"Calculate: (10 × {rate1}) + ({t2_kl} × {rate2}).",
        "tier_3": f"{cost_t1:.2f} + {cost_t2:.2f} = {total_cost:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_water_two_tier_stepped_billing", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_water_three_tier_stepped_billing(r: random.Random) -> Dict[str, Any]:
    """Calculate water charges spanning three stepped tariff blocks."""
    name = r.choice(SA_NAMES)
    total_kl = r.choice([26, 28, 30, 32, 35])
    # Step 1: 0 - 6 kL @ R 0.00 (free)
    # Step 2: 6.1 - 20 kL (14 kL) @ R 9.50
    # Step 3: > 20 kL @ R 18.20
    rate2 = 9.50
    rate3 = 18.20

    t1_kl = 6
    t2_kl = 14
    t3_kl = total_kl - 20

    cost_t1 = 0.00
    cost_t2 = round(t2_kl * rate2, 2)
    cost_t3 = round(t3_kl * rate3, 2)
    total_cost = round(cost_t1 + cost_t2 + cost_t3, 2)
    ans_str = _fmt_curr(total_cost)

    prompt = (
        f"{name}'s household uses **{total_kl} kL** of water in a month.\n"
        f"The municipal sliding scale charges:\n\n"
        f"| Step | Range | Tariff (R/kL) |\n"
        f"| :--- | :---: | :---: |\n"
        f"| Step 1 | 0 – 6 kL | R 0,00 (Free) |\n"
        f"| Step 2 | 6,1 – 20 kL | {_fmt_curr(rate2)} / kL |\n"
        f"| Step 3 | Above 20 kL | {_fmt_curr(rate3)} / kL |\n\n"
        f"Calculate the **total water bill** for {name}'s household."
    )
    sol = (
        f"Step 1: Divide the {total_kl} kL into the three steps:\n"
        f"• Step 1: First 6 kL @ R 0,00 = R 0,00\n"
        f"• Step 2: Next 14 kL (20 - 6) @ {_fmt_curr(rate2)} = {_fmt_curr(cost_t2)}\n"
        f"• Step 3: Remaining {t3_kl} kL ({total_kl} - 20) @ {_fmt_curr(rate3)} = {_fmt_curr(cost_t3)}\n\n"
        f"Step 2: Method setup – sum charges across all steps:\n"
        f"• Total Cost = R 0,00 + {_fmt_curr(cost_t2)} + {_fmt_curr(cost_t3)} "
        f"✓ [1 Mark: Method – correctly apportioning consumption across all 3 steps]\n\n"
        f"Step 3: Calculate sum:\n"
        f"Total Cost = {ans_str} ✓ [1 Mark: Accuracy – correct water total in Rands]"
    )
    rubric = [
        f"1 Mark: Method – evaluating (14 × {_fmt_curr(rate2)}) + ({t3_kl} × {_fmt_curr(rate3)})",
        f"1 Mark: Accuracy – correct total {ans_str}"
    ]
    hints = {
        "tier_1": f"The first 6 kL is free. The next 14 kL costs {_fmt_curr(rate2)}/kL. The remaining {t3_kl} kL costs {_fmt_curr(rate3)}/kL.",
        "tier_2": f"Calculate: (14 × {rate2}) + ({t3_kl} × {rate3}).",
        "tier_3": f"{cost_t2:.2f} + {cost_t3:.2f} = {total_cost:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_water_three_tier_stepped_billing", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_water_drought_level_restriction_tariffs(r: random.Random) -> Dict[str, Any]:
    """Compare water bill under standard tariffs vs emergency Level 3 drought restriction penalty tariffs."""
    name = r.choice(SA_NAMES)
    kl_used = r.choice([15, 20, 25, 30])
    normal_flat_rate = 10.50
    drought_flat_rate = 22.80

    normal_cost = round(kl_used * normal_flat_rate, 2)
    drought_cost = round(kl_used * drought_flat_rate, 2)
    diff = round(drought_cost - normal_cost, 2)
    ans_str = _fmt_curr(diff)

    prompt = (
        f"Due to critical dam levels, the municipality implements Level 3 drought restrictions:\n"
        f"• **Normal Tariff**: {_fmt_curr(normal_flat_rate)} per kL\n"
        f"• **Level 3 Drought Restriction Tariff**: {_fmt_curr(drought_flat_rate)} per kL\n\n"
        f"If {name}'s household uses **{kl_used} kL** of water during a drought month, "
        f"calculate **how much more** {name} will pay under the drought restriction tariff compared to normal."
    )
    sol = (
        f"Step 1: Calculate water bill under both tariffs:\n"
        f"• Normal Bill = {kl_used} × {_fmt_curr(normal_flat_rate)} = {_fmt_curr(normal_cost)}\n"
        f"• Drought Bill = {kl_used} × {_fmt_curr(drought_flat_rate)} = {_fmt_curr(drought_cost)}\n\n"
        f"Step 2: Method setup – calculate the penalty difference:\n"
        f"• Difference = Drought Bill - Normal Bill\n"
        f"• Difference = {_fmt_curr(drought_cost)} - {_fmt_curr(normal_cost)} "
        f"✓ [1 Mark: Method – evaluating both tariff totals and setting up difference]\n\n"
        f"Step 3: Calculate difference:\n"
        f"Difference = {ans_str} ✓ [1 Mark: Accuracy – correct cost increase in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating ({kl_used} × {_fmt_curr(drought_flat_rate)}) - ({kl_used} × {_fmt_curr(normal_flat_rate)})",
        f"1 Mark: Accuracy – correct difference {ans_str}"
    ]
    hints = {
        "tier_1": f"Work out the cost under normal tariff: {kl_used} × {_fmt_curr(normal_flat_rate)}.",
        "tier_2": f"Work out the cost under drought tariff: {kl_used} × {_fmt_curr(drought_flat_rate)}.",
        "tier_3": f"{drought_cost:.2f} - {normal_cost:.2f} = {diff:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_water_drought_level_restriction_tariffs", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_water_convert_litres_to_kilolitres_billing(r: random.Random) -> Dict[str, Any]:
    """Convert household consumption in litres to kilolitres and compute municipal charge."""
    name = r.choice(SA_NAMES)
    litres = r.choice([14000, 18500, 22000, 25500, 30000])
    rate_per_kl = round(r.choice([9.20, 11.50, 13.80, 15.00]), 2)

    kl = litres / 1000
    cost = round(kl * rate_per_kl, 2)
    ans_str = _fmt_curr(cost)

    prompt = (
        f"{name}'s smart flow meter records total household water consumption of **{_fmt(litres)} litres** for the month.\n"
        f"The municipal tariff is charged at **{_fmt_curr(rate_per_kl)} per kilolitre (kL)**.\n\n"
        f"1. Convert the consumption from litres to kilolitres ($1\\text{{ kL}} = 1\\ 000\\text{{ litres}}$).\n"
        f"2. Calculate the **total water bill**."
    )
    sol = (
        f"Step 1: Convert litres to kilolitres:\n"
        f"• Kilolitres = {litres} L ÷ 1 000 = {_fmt(kl)} kL\n\n"
        f"Step 2: Method setup – multiply kilolitres by tariff rate:\n"
        f"• Cost = {_fmt(kl)} kL × {_fmt_curr(rate_per_kl)} "
        f"✓ [1 Mark: Method – dividing litres by 1 000 and multiplying by rate per kL]\n\n"
        f"Step 3: Calculate total cost:\n"
        f"Cost = {ans_str} ✓ [1 Mark: Accuracy – correct water cost in Rands]"
    )
    rubric = [
        f"1 Mark: Method – converting {litres} L to {_fmt(kl)} kL and multiplying by {_fmt_curr(rate_per_kl)}",
        f"1 Mark: Accuracy – correct cost {ans_str}"
    ]
    hints = {
        "tier_1": f"Divide {_fmt(litres)} by 1 000 to get kilolitres ({_fmt(kl)} kL).",
        "tier_2": f"Multiply {_fmt(kl)} kL by {_fmt_curr(rate_per_kl)}.",
        "tier_3": f"{kl} × {rate_per_kl:.2f} = {cost:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_water_convert_litres_to_kilolitres_billing", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_water_step_rate_table_reading_threshold(r: random.Random) -> Dict[str, Any]:
    """Identify the highest tariff tier triggered by a given monthly consumption."""
    name = r.choice(SA_NAMES)
    kl_used = r.choice([8.5, 17.2, 24.8, 33.5, 48.0])

    if kl_used <= 9.0:
        ans_str = "Step 1 (0 – 9 kL)"
        distractors = ["Step 2 (9,1 – 25 kL)", "Step 3 (25,1 – 30 kL)", "Step 4 (> 30 kL)"]
    elif kl_used <= 25.0:
        ans_str = "Step 2 (9,1 – 25 kL)"
        distractors = ["Step 1 (0 – 9 kL)", "Step 3 (25,1 – 30 kL)", "Step 4 (> 30 kL)"]
    elif kl_used <= 30.0:
        ans_str = "Step 3 (25,1 – 30 kL)"
        distractors = ["Step 1 (0 – 9 kL)", "Step 2 (9,1 – 25 kL)", "Step 4 (> 30 kL)"]
    else:
        ans_str = "Step 4 (Above 30 kL)"
        distractors = ["Step 1 (0 – 9 kL)", "Step 2 (9,1 – 25 kL)", "Step 3 (25,1 – 30 kL)"]

    prompt = (
        f"{name}'s water meter records a monthly consumption of **{_fmt(kl_used)} kL**.\n"
        f"The municipal tariff structure has the following tiers:\n"
        f"• Step 1: 0 – 9 kL\n"
        f"• Step 2: 9,1 – 25 kL\n"
        f"• Step 3: 25,1 – 30 kL\n"
        f"• Step 4: Above 30 kL\n\n"
        f"Identify the **highest tariff step (bracket)** reached by {name}'s consumption."
    )
    sol = (
        f"Step 1: Compare {kl_used} kL against the municipal step thresholds:\n"
        f"• 0 to 9 kL: Step 1\n"
        f"• 9,1 to 25 kL: Step 2\n"
        f"• 25,1 to 30 kL: Step 3\n"
        f"• Above 30 kL: Step 4\n\n"
        f"Step 2: Method setup – locate the interval containing {_fmt(kl_used)} kL:\n"
        f"• {_fmt(kl_used)} kL falls into {ans_str}.\n"
        f"✓ [1 Mark: Method – matching numerical kilolitre consumption to tariff tier interval]\n\n"
        f"Step 3: Final Answer:\n"
        f"{ans_str} ✓ [1 Mark: Accuracy – correct tariff step identified]"
    )
    rubric = [
        "1 Mark: Method – locating interval containing given consumption",
        f"1 Mark: Accuracy – identifying {ans_str}"
    ]
    hints = {
        "tier_1": f"Look at the four brackets to see where {_fmt(kl_used)} kL lies.",
        "tier_2": "Find the range whose lower and upper bounds enclose this volume.",
        "tier_3": f"{_fmt(kl_used)} kL falls into {ans_str}."
    }
    return _make_q(
        "fin_tar_water_step_rate_table_reading_threshold",
        prompt, ans_str, sol, rubric, hints, 2, options=[ans_str] + distractors, r=r
    )


def _gen_fin_tar_water_daily_consumption_per_person(r: random.Random) -> Dict[str, Any]:
    """Calculate per capita daily water usage in litres."""
    name = r.choice(SA_NAMES)
    people = r.choice([3, 4, 5, 6])
    days = 30
    total_kl = r.choice([15, 18, 21, 24, 27])

    total_litres = total_kl * 1000
    daily_per_person = round(total_litres / (people * days), 1)
    ans_str = f"{_fmt(daily_per_person)} litres/person/day"

    prompt = (
        f"{name}'s household consists of **{people} people** and consumed a total of **{total_kl} kL** "
        f"of water during a **30-day month**.\n\n"
        f"Calculate the **average water consumption per person per day (in litres)**.\n"
        f"Use the formula: $$\\text{{Daily Litres per Person}} = \\frac{{\\text{{Total kL}} \\times 1\\ 000}}{{\\text{{Number of People}} \\times \\text{{Days}}}}$$"
    )
    sol = (
        f"Step 1: Convert total kilolitres to litres:\n"
        f"• Total Litres = {total_kl} kL × 1 000 = {_fmt(total_litres)} litres\n\n"
        f"Step 2: Method setup – divide by total person-days ({people} people × {days} days):\n"
        f"• Total Person-Days = {people} × {days} = {people * days} person-days\n"
        f"• Per Person Daily = {_fmt(total_litres)} ÷ {people * days} "
        f"✓ [1 Mark: Method – dividing total litres by (people × days)]\n\n"
        f"Step 3: Calculate daily per capita consumption:\n"
        f"Per Person Daily = {ans_str} ✓ [1 Mark: Accuracy – correct daily litres per person]"
    )
    rubric = [
        f"1 Mark: Method – dividing ({total_kl} × 1 000) by ({people} × {days})",
        f"1 Mark: Accuracy – correct rate {ans_str}"
    ]
    hints = {
        "tier_1": f"Convert {total_kl} kL to litres: {total_kl} × 1 000 = {_fmt(total_litres)} litres.",
        "tier_2": f"Divide by the number of people ({people}) and then divide by {days} days.",
        "tier_3": f"{total_litres} ÷ ({people} × {days}) = {daily_per_person}, giving {ans_str}."
    }
    return _make_q("fin_tar_water_daily_consumption_per_person", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_water_dripping_tap_leak_wastage_cost(r: random.Random) -> Dict[str, Any]:
    """Calculate the monthly cost of water lost from a leaking tap billed at top-tier tariff."""
    name = r.choice(SA_NAMES)
    litres_per_day = r.choice([25, 30, 40, 50, 60])
    days = 30
    top_tier_rate_per_kl = round(r.choice([24.50, 28.00, 32.50, 36.00]), 2)

    total_litres_wasted = litres_per_day * days
    kl_wasted = total_litres_wasted / 1000
    wasted_cost = round(kl_wasted * top_tier_rate_per_kl, 2)
    ans_str = _fmt_curr(wasted_cost)

    prompt = (
        f"{name}'s garden tap has a persistent leak, dripping **{litres_per_day} litres of water every day**.\n"
        f"Because the household already exceeds its normal consumption baseline, this wasted water is billed "
        f"at the top municipal punitive tariff rate of **{_fmt_curr(top_tier_rate_per_kl)} per kL**.\n\n"
        f"Calculate the **monetary cost of this wasted water** over a **30-day month**."
    )
    sol = (
        f"Step 1: Calculate total water volume wasted in litres and convert to kilolitres:\n"
        f"• Total Litres Wasted = {litres_per_day} L/day × {days} days = {_fmt(total_litres_wasted)} litres\n"
        f"• Kilolitres Wasted = {_fmt(total_litres_wasted)} ÷ 1 000 = {_fmt(kl_wasted)} kL\n\n"
        f"Step 2: Method setup – multiply kilolitres by top-tier tariff:\n"
        f"• Cost of Wastage = {_fmt(kl_wasted)} kL × {_fmt_curr(top_tier_rate_per_kl)} "
        f"✓ [1 Mark: Method – converting wasted litres to kL and multiplying by tariff rate]\n\n"
        f"Step 3: Calculate monetary cost:\n"
        f"Cost of Wastage = {ans_str} ✓ [1 Mark: Accuracy – correct wastage cost in Rands]"
    )
    rubric = [
        f"1 Mark: Method – calculating (({litres_per_day} × {days}) / 1 000) × {_fmt_curr(top_tier_rate_per_kl)}",
        f"1 Mark: Accuracy – correct wastage cost {ans_str}"
    ]
    hints = {
        "tier_1": f"Multiply {litres_per_day} litres by {days} days to find total litres lost.",
        "tier_2": f"Divide by 1 000 to convert to kL ({_fmt(kl_wasted)} kL), then multiply by {_fmt_curr(top_tier_rate_per_kl)}.",
        "tier_3": f"{kl_wasted} × {top_tier_rate_per_kl:.2f} = {wasted_cost:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_water_dripping_tap_leak_wastage_cost", prompt, ans_str, sol, rubric, hints, 2, r=r)


def _gen_fin_tar_water_jojo_tank_rainwater_savings(r: random.Random) -> Dict[str, Any]:
    """Calculate annual municipal water savings from harvesting rainwater with a JoJo tank."""
    name = r.choice(SA_NAMES)
    annual_harvest_kl = r.choice([35, 45, 50, 60, 75])
    muni_rate = round(r.choice([14.50, 16.80, 18.50, 21.00]), 2)

    annual_savings = round(annual_harvest_kl * muni_rate, 2)
    ans_str = _fmt_curr(annual_savings)

    prompt = (
        f"{name} installs a 5 000 L JoJo rainwater harvesting tank. Over the course of a year, "
        f"{name} harvests and uses **{annual_harvest_kl} kL** of rainwater for garden irrigation and toilet flushing, "
        f"displacing municipal tap water billed at an average of **{_fmt_curr(muni_rate)} per kL**.\n\n"
        f"Calculate {name}'s **total annual financial savings** on municipal water charges."
    )
    sol = (
        f"Step 1: Identify volume of municipal water saved and unit tariff:\n"
        f"• Rainwater harvested = {annual_harvest_kl} kL\n"
        f"• Municipal tariff rate = {_fmt_curr(muni_rate)} per kL\n\n"
        f"Step 2: Method setup – multiply harvested volume by municipal rate:\n"
        f"• Annual Savings = Harvested kL × Tariff per kL\n"
        f"• Annual Savings = {annual_harvest_kl} × {_fmt_curr(muni_rate)} "
        f"✓ [1 Mark: Method – multiplying displaced water volume by municipal tariff]\n\n"
        f"Step 3: Calculate total savings:\n"
        f"Annual Savings = {ans_str} ✓ [1 Mark: Accuracy – correct annual savings in Rands]"
    )
    rubric = [
        f"1 Mark: Method – multiplying {annual_harvest_kl} by {_fmt_curr(muni_rate)}",
        f"1 Mark: Accuracy – correct annual savings {ans_str}"
    ]
    hints = {
        "tier_1": f"Multiply the kilolitres of rainwater harvested ({annual_harvest_kl} kL) by the municipal tariff ({_fmt_curr(muni_rate)}).",
        "tier_2": f"Calculate: {annual_harvest_kl} × {muni_rate}.",
        "tier_3": f"{annual_harvest_kl} × {muni_rate:.2f} = {annual_savings:.2f}, giving {ans_str}."
    }
    return _make_q("fin_tar_water_jojo_tank_rainwater_savings", prompt, ans_str, sol, rubric, hints, 2, r=r)
