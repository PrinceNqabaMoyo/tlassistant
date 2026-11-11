"""Cluster 4: Rounding Off & Real-World Rounding Contexts (9 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_num_rnd_standard_nearest_whole_number(r: random.Random) -> Dict[str, Any]:
    val = round(r.uniform(12.1, 88.9), 1)
    rounded = round(val)
    ans_str = str(rounded)

    prompt = (
        f"A weather station records a relative humidity index of **{_fmt(val, 1)}\\%**.\n\n"
        f"Round this measurement off to the **nearest whole number** according to standard mathematical rounding rules."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• To round to the nearest whole number, look at the first digit after the decimal point (the tenths digit):\n"
        f"  - If the digit is $5, 6, 7, 8, 9$, round **UP** to the next integer.\n"
        f"  - If the digit is $0, 1, 2, 3, 4$, keep the integer as is (**round down**).\n\n"
        f"**Step 2: Method Setup & Rounding**\n"
        f"• Value: {_fmt(val, 1)}.\n"
        f"• First decimal digit: {str(val).split('.')[1][0]}.\n"
        f"• Rounded whole number = **{rounded}**.\n"
        f"✓ **[1 Mark: Method – inspecting tenths digit and applying whole number rounding rule]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct whole integer]**"
    )
    return _make_q(
        subskill="num_rnd_standard_nearest_whole_number",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – nearest whole number rounding rule", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Look at the digit after the decimal point in {_fmt(val, 1)}.",
            "tier_2": f"If 5 or more, round up. If 4 or less, round down.",
            "tier_3": f"Nearest whole number = {ans_str}."
        },
        r=r
    )

def _gen_num_rnd_standard_decimal_places_two_dp(r: random.Random) -> Dict[str, Any]:
    # e.g. 14.5678 -> 14.57
    val = round(r.uniform(10.123, 99.876), 4)
    rounded = round(val, 2)
    ans_str = _fmt(rounded, 2)

    prompt = (
        f"In a financial calculation, the raw decimal answer is **{_fmt(val, 4)}**.\n\n"
        f"Round this value off to **strictly two decimal places (2 d.p.)**."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• To round to 2 decimal places, inspect the 3rd decimal digit (thousandths):\n"
        f"  - If $\\ge 5$, increase the 2nd decimal digit by 1.\n"
        f"  - If $< 5$, leave the 2nd decimal digit unchanged.\n\n"
        f"**Step 2: Method Setup & Rounding**\n"
        f"• Value: {_fmt(val, 4)}.\n"
        f"• 3rd decimal digit: {str(val).split('.')[1][2]}.\n"
        f"• Rounded to 2 d.p.: **{ans_str}**.\n"
        f"✓ **[1 Mark: Method – inspecting 3rd decimal place and rounding 2nd digit]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct value rounded to 2 decimal places]**"
    )
    return _make_q(
        subskill="num_rnd_standard_decimal_places_two_dp",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 2 decimal places rounding rule", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Inspect the 3rd digit after the comma in {_fmt(val, 4)}.",
            "tier_2": f"If the 3rd digit is 5 or more, round up.",
            "tier_3": f"Rounded to 2 decimal places = {ans_str}."
        },
        r=r
    )

def _gen_num_rnd_context_round_up_passengers_transport(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    passengers = r.choice([38, 44, 52, 65, 78])
    taxi_capacity = 15  # standard 15-seater minibus taxi
    raw_div = passengers / taxi_capacity
    taxis_needed = math.ceil(raw_div)
    ans_str = f"{taxis_needed} taxis"

    prompt = (
        f"{name} is coordinating commuter transport for a church choir of **{passengers} people** travelling from Soweto to Pretoria.\n\n"
        f"Each licensed minibus taxi can carry a maximum legal capacity of **{taxi_capacity} passengers**.\n\n"
        f"Calculate the **minimum number of taxis** that must be hired to transport everyone safely without overloading."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• In real-world transport contexts, you cannot leave remaining passengers behind or hire a fraction of a vehicle.\n"
        f"• Therefore, any fractional remainder must be **rounded UP** to the next whole vehicle:\n"
        f"  $$\\text{{Taxis}} = \\left\\lceil \\frac{{\\text{{Passengers}}}}{{\\text{{Capacity}}}} \\right\\rceil$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\frac{{{passengers}}}{{{taxi_capacity}}} = {raw_div:.2f}$.\n"
        f"• Since {passengers % taxi_capacity} passengers still require seats, round up to **{taxis_needed} taxis**.\n"
        f"✓ **[1 Mark: Method – dividing passenger count by taxi capacity and rounding UP in context]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct whole number of taxis]**"
    )
    custom_opts = [
        f"{taxis_needed} taxis",
        f"{taxis_needed - 1} taxis",
        f"{raw_div:.1f} taxis".replace(".", ","),
        f"{taxis_needed + 1} taxis"
    ]
    return _make_q(
        subskill="num_rnd_context_round_up_passengers_transport",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – passenger ÷ capacity rounded UP", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide {passengers} by {taxi_capacity}: {passengers} ÷ {taxi_capacity} = {raw_div:.2f}.",
            "tier_2": f"You cannot leave remaining passengers behind, so you must round UP to the next whole taxi.",
            "tier_3": f"Taxis needed = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_rnd_context_round_up_materials_paint(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_litres_needed = round(r.choice([11.2, 12.8, 16.4, 21.5, 26.2]), 1)
    tin_size = 5  # sold only in 5 L tins
    tins_needed = math.ceil(total_litres_needed / tin_size)
    ans_str = f"{tins_needed} tins"

    prompt = (
        f"{name} calculates that repainting the interior walls of a community centre requires **{_fmt(total_litres_needed, 1)} litres of PVA paint**.\n\n"
        f"The hardware store sells this specific paint **only in sealed 5-litre tins**.\n\n"
        f"Calculate the **minimum number of 5 L tins** {name} must buy to ensure there is enough paint to complete the job."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Hardware stores do not open sealed paint tins to sell partial litres.\n"
        f"• To ensure all walls receive sufficient paint without running out, the number of tins must be **rounded UP** to the next whole tin:\n"
        f"  $$\\text{{Tins Needed}} = \\left\\lceil \\frac{{\\text{{Litres Needed}}}}{{5}} \\right\\rceil$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\frac{{{total_litres_needed}}}{{5}} = {total_litres_needed / 5:.2f}$.\n"
        f"• Rounding UP in context gives **{tins_needed} tins**.\n"
        f"✓ **[1 Mark: Method – dividing litres by 5 and rounding UP in context]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct whole number of tins]**"
    )
    custom_opts = [
        f"{tins_needed} tins",
        f"{tins_needed - 1} tins",
        f"{total_litres_needed / 5:.1f} tins".replace(".", ","),
        f"{tins_needed + 2} tins"
    ]
    return _make_q(
        subskill="num_rnd_context_round_up_materials_paint",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – litres ÷ 5 rounded UP", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide {_fmt(total_litres_needed, 1)} by 5.",
            "tier_2": f"{total_litres_needed} ÷ 5 = {total_litres_needed / 5:.2f}. You cannot buy partial tins, so round UP.",
            "tier_3": f"Tins needed = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_rnd_context_round_down_affordability(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    budget = round(r.choice([120.00, 150.00, 200.00, 250.00]), 2)
    unit_price = round(r.choice([16.50, 18.00, 22.50, 24.00]), 2)
    max_items = math.floor(budget / unit_price)
    ans_str = f"{max_items} items"

    prompt = (
        f"{name} has a strict budget of **{_fmt_curr(budget)}** in cash.\n\n"
        f"Speciality snack pies cost **{_fmt_curr(unit_price)} each**.\n\n"
        f"Calculate the **maximum whole number of pies** {name} can afford to buy without exceeding the cash budget."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• In affordability contexts, you cannot buy items on credit if you do not have enough cash to cover the next whole item.\n"
        f"• Therefore, the division result must be **rounded DOWN** to the nearest whole integer:\n"
        f"  $$\\text{{Items Afforded}} = \\left\\lfloor \\frac{{\\text{{Budget}}}}{{\\text{{Unit Price}}}} \\right\\rfloor$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\frac{{{_fmt(budget)}}}{{{_fmt(unit_price)}}} = {budget / unit_price:.2f}$.\n"
        f"• Rounding DOWN gives **{max_items} items** (Total cost = ${max_items} \\times {_fmt(unit_price)} = {_fmt(max_items * unit_price)}$, leaving ${_fmt(budget - max_items * unit_price)}$ change).\n"
        f"✓ **[1 Mark: Method – dividing budget by unit price and rounding DOWN in context]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct whole number of items]**"
    )
    custom_opts = [
        f"{max_items} items",
        f"{max_items + 1} items",
        f"{budget / unit_price:.1f} items".replace(".", ","),
        f"{max_items - 1} items"
    ]
    return _make_q(
        subskill="num_rnd_context_round_down_affordability",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – budget ÷ price rounded DOWN", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide {_fmt_curr(budget)} by {_fmt_curr(unit_price)}.",
            "tier_2": f"{budget} ÷ {unit_price} = {budget / unit_price:.2f}. You cannot buy a partial pie or spend more cash than you have, so round DOWN.",
            "tier_3": f"Maximum items = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_rnd_context_round_down_containers_packed(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_eggs = r.choice([250, 320, 410, 530])
    eggs_per_carton = 12  # dozen
    full_cartons = total_eggs // eggs_per_carton
    ans_str = f"{full_cartons} cartons"

    prompt = (
        f"{name}'s layer poultry enterprise collects **{total_eggs} fresh eggs** from the nesting boxes.\n\n"
        f"The eggs are packed into standard retail egg cartons holding **12 eggs each** (1 dozen).\n\n"
        f"Calculate the **number of complete, full cartons** that can be packed for market sale."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Retailers only accept completely full, sealed cartons for sale.\n"
        f"• Any remaining loose eggs cannot form a full carton, so the division result must be **rounded DOWN** to the nearest whole integer:\n"
        f"  $$\\text{{Full Cartons}} = \\left\\lfloor \\frac{{\\text{{Total Eggs}}}}{{12}} \\right\\rfloor$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\frac{{{total_eggs}}}{{12}} = {total_eggs / 12:.2f}$.\n"
        f"• ${full_cartons} \\times 12 = {full_cartons * 12}$ eggs packed, with ${total_eggs % 12}$ loose eggs remaining.\n"
        f"• Therefore, exactly **{full_cartons} full cartons** can be packed.\n"
        f"✓ **[1 Mark: Method – dividing egg count by 12 and rounding DOWN to full units]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct whole number of full cartons]**"
    )
    custom_opts = [
        f"{full_cartons} cartons",
        f"{full_cartons + 1} cartons",
        f"{total_eggs / 12:.1f} cartons".replace(".", ","),
        f"{full_cartons - 2} cartons"
    ]
    return _make_q(
        subskill="num_rnd_context_round_down_containers_packed",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – eggs ÷ 12 rounded DOWN", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide {total_eggs} by 12.",
            "tier_2": f"{total_eggs} ÷ 12 = {total_eggs / 12:.2f}. Since only full cartons count, take the whole integer.",
            "tier_3": f"Full cartons = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_rnd_south_african_cash_rounding_cents(r: random.Random) -> Dict[str, Any]:
    int_rands = r.choice([45, 68, 112, 175, 240])
    cents = r.choice([23, 47, 62, 89, 94])
    raw_total = round(int_rands + cents / 100.0, 2)
    # In South Africa, 1c and 2c coins were discontinued. Retail stores round cash transactions
    # to the nearest 10c (or 5c):
    # Standard SA practice: 1c, 2c -> down to 0c; 3c, 4c, 5c, 6c, 7c -> to 5c (or round to nearest 10c)
    # Nearest 10 cents:
    last_digit = cents % 10
    if last_digit in [1, 2]:
        rounded_cents = cents - last_digit
    elif last_digit in [3, 4, 5, 6, 7]:
        rounded_cents = (cents // 10) * 10 + 5
    else:  # 8, 9
        rounded_cents = (cents // 10 + 1) * 10
    rounded_cash = round(int_rands + rounded_cents / 100.0, 2)
    ans_str = _fmt_curr(rounded_cash)

    prompt = (
        f"In South African retail stores, 1-cent and 2-cent coins are no longer in circulation. Cash purchases are rounded to the nearest **5 cents** at the till.\n\n"
        f"A customer's till slip calculates a raw total of **{_fmt_curr(raw_total)}**.\n\n"
        f"Calculate the **final rounded cash amount** the customer must pay in coins and notes."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• For physical cash transactions, amounts ending in:\n"
        f"  - 1c or 2c round down to 0c.\n"
        f"  - 3c, 4c, 6c, 7c round to the nearest 5c.\n"
        f"  - 8c or 9c round up to the next 10c.\n\n"
        f"**Step 2: Method Setup & Rounding**\n"
        f"• Raw total: {_fmt_curr(raw_total)} (cents ending in {last_digit}c).\n"
        f"• Rounded to nearest 5c: **{ans_str}**.\n"
        f"✓ **[1 Mark: Method – applying South African 5c cash rounding rule]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct rounded cash total in Rands]**"
    )
    custom_opts = [
        ans_str,
        _fmt_curr(raw_total),
        _fmt_curr(round(int_rands + (cents // 10) * 0.10, 2)),
        _fmt_curr(round(int_rands + (cents // 10 + 1) * 0.10, 2))
    ]
    return _make_q(
        subskill="num_rnd_south_african_cash_rounding_cents",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – SA 5c cash rounding rule", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Look at the last digit of the cents ({last_digit}c).",
            "tier_2": f"Amounts ending in 1c/2c round down to 0c; 3c–7c round to 5c; 8c/9c round up to 10c.",
            "tier_3": f"Rounded cash amount = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_rnd_distance_nearest_kilometre(r: random.Random) -> Dict[str, Any]:
    dist_km = round(r.uniform(142.3, 485.8), 1)
    rounded = round(dist_km)
    ans_str = f"{rounded} km"

    prompt = (
        f"A GPS navigation trip meter records a road journey distance between Kimberley and Bloemfontein as **{_fmt(dist_km, 1)} km**.\n\n"
        f"Round this travel distance to the **nearest kilometre** for an official travel logbook claim."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• To round to the nearest whole kilometre, check the tenths digit:\n"
        f"  - If $\\ge 5$, round up.\n"
        f"  - If $< 5$, round down.\n\n"
        f"**Step 2: Method Setup & Rounding**\n"
        f"• Distance: {_fmt(dist_km, 1)} km.\n"
        f"• Tenths digit is {str(dist_km).split('.')[1]}.\n"
        f"• Nearest whole kilometre: **{rounded} km**.\n"
        f"✓ **[1 Mark: Method – rounding distance to nearest whole unit]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct distance with units]**"
    )
    return _make_q(
        subskill="num_rnd_distance_nearest_kilometre",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – nearest whole km rounding", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Inspect the tenths digit in {_fmt(dist_km, 1)} km.",
            "tier_2": f"If 5 or more, round up. Otherwise round down.",
            "tier_3": f"Nearest km = {ans_str}."
        },
        r=r
    )

def _gen_num_rnd_significant_figures_scientific(r: random.Random) -> Dict[str, Any]:
    raw_val = round(r.uniform(124.5, 985.4), 1)
    # Round to 1 significant figure
    s = str(int(raw_val))
    first_digit = int(s[0])
    second_digit = int(s[1])
    if second_digit >= 5:
        first_digit += 1
    rounded_1sig = first_digit * (10 ** (len(s) - 1))
    ans_str = str(rounded_1sig)

    prompt = (
        f"In a demographic research survey, an initial population sample size is measured as **{_fmt(raw_val, 1)}**.\n\n"
        f"Round this number off to **1 significant figure (1 s.f.)** for high-level order-of-magnitude estimation."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• One significant figure retains only the first non-zero digit on the left:\n"
        f"  - Inspect the second digit.\n"
        f"  - If $\\ge 5$, round the first digit up.\n"
        f"  - Replace all subsequent whole number place values with zeroes.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• Value: {_fmt(raw_val, 1)}.\n"
        f"• First digit: {s[0]}; Second digit: {s[1]}.\n"
        f"• Since {s[1]} {'is $\\ge 5$, round up' if second_digit >= 5 else 'is $< 5$, round down'} $\\to$ **{rounded_1sig}**.\n"
        f"✓ **[1 Mark: Method – identifying 1st significant digit and rounding based on 2nd digit]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct number rounded to 1 significant figure]**"
    )
    custom_opts = [
        ans_str,
        str(int(raw_val)),
        str(first_digit * (10 ** (len(s) - 2))),
        str((first_digit + 2) * (10 ** (len(s) - 1)))
    ]
    return _make_q(
        subskill="num_rnd_significant_figures_scientific",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 1 significant figure rule", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Look at the first two digits of {int(raw_val)}.",
            "tier_2": f"Keep only the first digit and replace the rest with zeroes.",
            "tier_3": f"1 significant figure = {ans_str}."
        },
        options=custom_opts,
        r=r
    )
