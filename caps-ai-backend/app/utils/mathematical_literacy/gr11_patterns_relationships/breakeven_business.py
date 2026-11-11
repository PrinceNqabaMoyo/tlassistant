"""Subskills 37 to 44: Break-Even Analysis, Business Cost & Revenue Modelling for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def _gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Formulate Total Cost formula C = Fixed Cost + (Variable Cost x n)."""
    name = r.choice(SA_NAMES)
    item = r.choice(["hot dogs", "muffins", "t-shirts", "beaded necklaces", "wooden toys", "fruit smoothies"])
    fixed_cost = r.choice([450, 600, 750, 900, 1200, 1500, 1800, 2400])
    var_cost = r.choice([12, 15, 18, 20, 25, 30, 35, 40, 45, 50])

    prompt = (
        f"{name} starts a small business selling {item}. {name} pays a fixed stall rental fee of "
        f"{_fmt_curr(fixed_cost)} per month and each {item[:-1] if item.endswith('s') else item} costs "
        f"{_fmt_curr(var_cost)} in ingredients/materials to produce. "
        f"Which formula correctly expresses the Total Cost (C in Rands) to produce 'n' units?"
    )

    correct_ans = f"C = {_fmt(fixed_cost)} + {_fmt(var_cost)} × n"
    custom_opts = [
        f"C = {_fmt(fixed_cost)} + {_fmt(var_cost)} × n",
        f"C = ({_fmt(fixed_cost)} + {_fmt(var_cost)}) × n",
        f"C = {_fmt(var_cost)} + {_fmt(fixed_cost)} × n",
        f"C = {_fmt(fixed_cost)} × {_fmt(var_cost)} × n",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify fixed and variable costs [1 mark].\n"
        f"Fixed cost = {_fmt_curr(fixed_cost)} (does not depend on n).\n"
        f"Variable cost per unit = {_fmt_curr(var_cost)} × n.\n"
        f"Step 2: Combine components [1 mark].\n"
        f"Total Cost C = Fixed Cost + (Variable Cost × n) = {_fmt(fixed_cost)} + {_fmt(var_cost)} × n.\n"
        f"Step 3: Correct formula [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="37",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Total Cost is made up of a fixed portion that is paid regardless of production plus a variable cost per item produced.",
        tier_2=f"The fixed stall rental is {_fmt_curr(fixed_cost)}, and every unit adds {_fmt_curr(var_cost)}.",
        tier_3=f"Write C = Fixed + (Variable × n), which gives C = {_fmt(fixed_cost)} + {_fmt(var_cost)} × n.",
        r=r,
    )


def _gen_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: Formulate Total Revenue/Income formula I = Selling Price x n."""
    name = r.choice(SA_NAMES)
    item = r.choice(["cupcakes", "school badges", "fruit cups", "printed mugs", "car washes"])
    selling_price = r.choice([25, 30, 35, 40, 50, 60, 75, 80, 100])

    prompt = (
        f"{name} sells {item} at a community market for {_fmt_curr(selling_price)} each. "
        f"Which formula correctly calculates the Total Income (I in Rands) from selling 'n' items?"
    )

    correct_ans = f"I = {_fmt(selling_price)} × n"
    custom_opts = [
        f"I = {_fmt(selling_price)} × n",
        f"I = {_fmt(selling_price)} + n",
        f"I = n / {_fmt(selling_price)}",
        f"I = {_fmt(selling_price)} / n",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify price per unit [1 mark].\n"
        f"Selling price = {_fmt_curr(selling_price)} per item.\n"
        f"Step 2: Multiply by number of units n [1 mark].\n"
        f"Total Income I = Selling Price × n = {_fmt(selling_price)} × n.\n"
        f"Step 3: Selected formula [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="38",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Income is directly proportional to the number of items sold.",
        tier_2="Multiply the unit price by the number of units n.",
        tier_3=f"The formula is I = {_fmt(selling_price)} × n.",
        r=r,
    )


def _gen_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Read Break-Even Point (units and Rands) from Cartesian graph with diagram_spec."""
    name = r.choice(SA_NAMES)
    item = r.choice(["artisan bread", "embroidered caps", "beaded bracelets", "leather keyrings"])

    # Choose clean intersection numbers
    n_be = r.choice([40, 50, 60, 75, 80, 100, 120, 150])
    selling_price = r.choice([30, 40, 50, 60, 80])
    rev_be = n_be * selling_price
    var_cost = round(selling_price * r.choice([0.4, 0.5, 0.6]))
    fixed_cost = n_be * (selling_price - var_cost)

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "cartesian_system",
        "title": f"Break-Even Analysis for {item.title()}",
        "x_label": "Number of Items Sold (n)",
        "y_label": "Amount in Rands (R)",
        "x_range": [0, int(n_be * 1.8)],
        "y_range": [0, int(rev_be * 1.8)],
        "lines": [
            {
                "label": "Total Cost (C)",
                "points": [[0, fixed_cost], [n_be, rev_be], [int(n_be * 1.8), fixed_cost + var_cost * int(n_be * 1.8)]],
                "color": "#ef4444",
            },
            {
                "label": "Total Income (I)",
                "points": [[0, 0], [n_be, rev_be], [int(n_be * 1.8), selling_price * int(n_be * 1.8)]],
                "color": "#10b981",
            },
        ],
        "points_of_interest": [
            {"x": n_be, "y": rev_be, "label": f"Break-Even Point ({n_be}; {_fmt_curr(rev_be)})"}
        ],
    }

    prompt = (
        f"Refer to the accompanying break-even graph for {name}'s business selling {item}. "
        f"The red line represents Total Cost and the green line represents Total Income. "
        f"What is the break-even point for this business (number of units and corresponding total amount)?"
    )

    correct_ans = f"{_fmt(n_be)} units and {_fmt_curr(rev_be)}"
    wrong_1 = f"{_fmt(n_be)} units and {_fmt_curr(fixed_cost)}"
    wrong_2 = f"{_fmt(int(n_be * 1.5))} units and {_fmt_curr(rev_be)}"
    wrong_3 = f"{_fmt(int(n_be * 0.75))} units and {_fmt_curr(int(rev_be * 0.75))}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Locate the intersection of the Total Cost line and the Total Income line [1 mark].\n"
        f"The two lines cross exactly at x = {_fmt(n_be)} units and y = {_fmt_curr(rev_be)}.\n"
        f"Step 2: Interpret break-even coordinates [1 mark].\n"
        f"At this point, Total Cost equals Total Income, meaning profit is R 0,00.\n"
        f"Step 3: Stated break-even point [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="39",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The break-even point is where the Total Cost line intersects the Total Income line.",
        tier_2=f"Look at the x-axis for the number of units and the y-axis for the amount in Rands where the red and green lines cross.",
        tier_3=f"The intersection point is ({_fmt(n_be)}; {_fmt_curr(rev_be)}), so the break-even is {_fmt(n_be)} units at {_fmt_curr(rev_be)}.",
        r=r,
        diagram_spec=diagram_spec,
    )


def _gen_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: Calculate break-even quantity algebraically: n = Fixed / (Price - Variable)."""
    name = r.choice(SA_NAMES)
    item = r.choice(["craft burgers", "scented candles", "canvas tote bags", "leather sandals", "picnic baskets"])

    n_be = r.choice([30, 40, 50, 60, 75, 80, 100, 120, 150, 200])
    margin = r.choice([15, 20, 25, 30, 40, 50])
    fixed_cost = n_be * margin
    var_cost = r.choice([20, 25, 30, 35, 45, 50, 60])
    selling_price = var_cost + margin

    prompt = (
        f"{name} produces {item}. The business has monthly fixed costs of {_fmt_curr(fixed_cost)} (rent and equipment). "
        f"Each {item[:-1] if item.endswith('s') else item} costs {_fmt_curr(var_cost)} to make and sells for "
        f"{_fmt_curr(selling_price)}. "
        f"Calculate the minimum number of units {name} must sell per month to break even."
    )

    correct_ans = f"{_fmt(n_be)} units"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Calculate contribution margin per unit [1 mark].\n"
        f"Margin = Selling Price - Variable Cost = {_fmt_curr(selling_price)} - {_fmt_curr(var_cost)} = {_fmt_curr(margin)}.\n"
        f"Step 2: Apply break-even formula [1 mark].\n"
        f"Break-even quantity = Fixed Costs ÷ Margin = {_fmt_curr(fixed_cost)} ÷ {_fmt_curr(margin)} = {_fmt(n_be)}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="40",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Break-even quantity = Fixed Costs ÷ (Selling Price - Variable Cost per unit).",
        tier_2=f"Each item earns a margin of {_fmt_curr(selling_price)} - {_fmt_curr(var_cost)} = {_fmt_curr(margin)} towards fixed costs.",
        tier_3=f"Divide {_fmt_curr(fixed_cost)} by {_fmt_curr(margin)} to get {_fmt(n_be)} units.",
        r=r,
    )


def _gen_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Identify Profit, Loss, or Break-even zone based on sales volume."""
    name = r.choice(SA_NAMES)
    item = r.choice(["handmade soaps", "pottery bowls", "knitted scarves", "wooden cutting boards"])

    n_be = r.choice([50, 80, 100, 120, 150])
    margin = r.choice([20, 25, 30, 40])
    fixed_cost = n_be * margin
    var_cost = 30
    price = var_cost + margin

    # Ask about volume below or above break-even
    scenario = r.choice(["below", "above", "exact"])
    if scenario == "below":
        test_units = int(n_be * r.choice([0.6, 0.7, 0.8]))
        zone_desc = "Operating at a Loss (Income < Cost)"
    elif scenario == "above":
        test_units = int(n_be * r.choice([1.25, 1.4, 1.5]))
        zone_desc = "Operating at a Profit (Income > Cost)"
    else:
        test_units = n_be
        zone_desc = "Break-Even (Income = Cost, Profit = R 0,00)"

    prompt = (
        f"{name}'s business breaks even when selling exactly {_fmt(n_be)} {item} per month. "
        f"In July, {name} sold {_fmt(test_units)} {item}. "
        f"Which statement correctly describes {name}'s financial position for July?"
    )

    correct_ans = zone_desc
    custom_opts = [
        "Operating at a Loss (Income < Cost)",
        "Operating at a Profit (Income > Cost)",
        "Break-Even (Income = Cost, Profit = R 0,00)",
        "Insolvent with negative revenue",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Compare actual sales volume to the break-even point [1 mark].\n"
        f"Actual sales = {_fmt(test_units)} units; Break-even point = {_fmt(n_be)} units.\n"
        f"Step 2: Determine profitability region [1 mark].\n"
        f"{'Since actual sales are below break-even, Total Cost exceeds Total Income, resulting in a loss.' if scenario == 'below' else 'Since actual sales exceed break-even, Total Income exceeds Total Cost, resulting in a profit.' if scenario == 'above' else 'Actual sales exactly equal break-even, so income equals cost.'}\n"
        f"Step 3: Stated conclusion [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="41",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Sales below the break-even volume generate a loss; sales above generate a profit.",
        tier_2=f"Compare {_fmt(test_units)} units sold with the break-even volume of {_fmt(n_be)} units.",
        tier_3=f"Since {_fmt(test_units)} is {scenario} {_fmt(n_be)}, the business is: {zone_desc}.",
        r=r,
    )


def _gen_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Subskill 42: Calculate exact Profit or Loss in Rands at a specific production volume."""
    name = r.choice(SA_NAMES)
    item = r.choice(["leather belts", "printed hoodies", "school satchels", "solar lamps"])

    n_be = r.choice([40, 50, 60, 80, 100])
    margin = r.choice([25, 30, 40, 50, 60])
    fixed_cost = n_be * margin
    var_cost = r.choice([35, 40, 50, 60])
    price = var_cost + margin

    # Volume sold: either profitable or loss
    is_profit = r.choice([True, False])
    if is_profit:
        n_sold = n_be + r.choice([15, 20, 25, 30, 40, 50])
    else:
        n_sold = max(5, n_be - r.choice([10, 15, 20, 25]))

    income = n_sold * price
    cost = fixed_cost + n_sold * var_cost
    diff = income - cost

    prompt = (
        f"{name} manufactures {item}. The monthly fixed costs are {_fmt_curr(fixed_cost)}, "
        f"the variable cost per unit is {_fmt_curr(var_cost)}, and each unit sells for {_fmt_curr(price)}. "
        f"If {name} produces and sells {_fmt(n_sold)} units this month, calculate the net profit or loss."
    )

    if diff >= 0:
        correct_ans = f"Profit of {_fmt_curr(diff)}"
        wrong_1 = f"Loss of {_fmt_curr(diff)}"
        wrong_2 = f"Profit of {_fmt_curr(diff + fixed_cost)}"
        wrong_3 = f"Loss of {_fmt_curr(abs(diff - 500))}"
    else:
        correct_ans = f"Loss of {_fmt_curr(abs(diff))}"
        wrong_1 = f"Profit of {_fmt_curr(abs(diff))}"
        wrong_2 = f"Loss of {_fmt_curr(abs(diff) + 400)}"
        wrong_3 = f"Profit of {_fmt_curr(abs(diff) + 600)}"

    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate Total Income and Total Cost [1 mark].\n"
        f"Total Income = {_fmt(n_sold)} × {_fmt_curr(price)} = {_fmt_curr(income)}.\n"
        f"Total Cost = {_fmt_curr(fixed_cost)} + ({_fmt(n_sold)} × {_fmt_curr(var_cost)}) = {_fmt_curr(cost)}.\n"
        f"Step 2: Calculate difference [1 mark].\n"
        f"Difference = Income - Cost = {_fmt_curr(income)} - {_fmt_curr(cost)} = {_fmt_curr(diff)}.\n"
        f"Step 3: Conclude profit/loss [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "break_even",
        "title": f"Business Break-Even Analysis ({item})",
        "fixed_cost": 5000,
        "selling_price": 25,
        "cost_line": {"slope": 15, "intercept": 5000},
        "income_line": {"slope": 25, "intercept": 0},
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="42",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Profit / Loss = Total Income - Total Cost.",
        tier_2=f"Calculate Income ({_fmt(n_sold)} × {_fmt_curr(price)}) and Cost ({_fmt_curr(fixed_cost)} + {_fmt(n_sold)} × {_fmt_curr(var_cost)}).",
        tier_3=f"Income is {_fmt_curr(income)} and Cost is {_fmt_curr(cost)}, giving a {correct_ans.lower()}.",
        r=r,
    )


def _gen_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Subskill 43: Calculate units needed to achieve a target profit: n = (Fixed + Target) / Margin."""
    name = r.choice(SA_NAMES)
    item = r.choice(["baskets", "cushions", "coffee mugs", "wooden clocks", "beaded hats"])

    margin = r.choice([20, 25, 30, 40, 50])
    fixed_cost = r.choice([1200, 1500, 2000, 2400, 3000, 3600])
    target_profit = r.choice([1000, 1500, 2000, 2500, 3000, 4000])

    # Ensure integer n
    total_required = fixed_cost + target_profit
    # Adjust target_profit so total_required is divisible by margin
    remainder = total_required % margin
    if remainder != 0:
        target_profit += (margin - remainder)
        total_required = fixed_cost + target_profit

    n_target = total_required // margin
    var_cost = r.choice([15, 20, 25, 35, 45])
    selling_price = var_cost + margin

    prompt = (
        f"{name} runs a craft shop making {item}. Fixed monthly costs are {_fmt_curr(fixed_cost)}, "
        f"the cost to produce each {item[:-1] if item.endswith('s') else item} is {_fmt_curr(var_cost)}, "
        f"and the selling price is {_fmt_curr(selling_price)}. "
        f"How many units must {name} produce and sell in a month to achieve a target net profit of {_fmt_curr(target_profit)}?"
    )

    correct_ans = f"{_fmt(n_target)} units"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Calculate contribution margin per unit [1 mark].\n"
        f"Margin = Selling Price - Variable Cost = {_fmt_curr(selling_price)} - {_fmt_curr(var_cost)} = {_fmt_curr(margin)}.\n"
        f"Step 2: Add fixed costs to target profit [1 mark].\n"
        f"Total required contribution = {_fmt_curr(fixed_cost)} + {_fmt_curr(target_profit)} = {_fmt_curr(total_required)}.\n"
        f"Step 3: Divide by unit margin [1 mark].\n"
        f"Units required = {_fmt_curr(total_required)} ÷ {_fmt_curr(margin)} = {_fmt(n_target)} units ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="43",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Required units = (Fixed Costs + Target Profit) ÷ Unit Contribution Margin.",
        tier_2=f"Margin per unit is {_fmt_curr(selling_price)} - {_fmt_curr(var_cost)} = {_fmt_curr(margin)}. Total amount to cover is {_fmt_curr(fixed_cost)} + {_fmt_curr(target_profit)} = {_fmt_curr(total_required)}.",
        tier_3=f"Divide {_fmt_curr(total_required)} by {_fmt_curr(margin)} to get {_fmt(n_target)} units.",
        r=r,
    )


def _gen_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Impact of price increase on break-even point: change in break-even quantity."""
    name = r.choice(SA_NAMES)
    item = r.choice(["gym bags", "reusable water bottles", "desk organisers", "chef aprons"])

    fixed_cost = r.choice([2400, 3000, 3600, 4800, 6000])
    var_cost = r.choice([20, 25, 30, 40])
    old_margin = r.choice([20, 25, 30, 40])
    # Ensure fixed_cost is divisible by old_margin
    fixed_cost = (fixed_cost // old_margin) * old_margin
    old_price = var_cost + old_margin
    old_be = fixed_cost // old_margin

    # New higher price
    price_increase = r.choice([10, 15, 20, 25])
    new_price = old_price + price_increase
    new_margin = old_margin + price_increase

    # Adjust fixed_cost so it is divisible by new_margin as well if possible, or calculate exact integer
    # Let's pick clean pairs
    combos = [
        (3000, 30, 50, 100, 60, 40),
        (2400, 20, 40, 120, 60, 60),
        (3600, 30, 60, 120, 60, 60),
        (4800, 40, 60, 120, 80, 40),
        (1800, 15, 30, 120, 60, 60),
        (4000, 25, 50, 160, 80, 80),
    ]
    fixed_cost, old_margin, new_margin, old_be, new_be, diff = r.choice(combos)
    old_price = var_cost + old_margin
    new_price = var_cost + new_margin
    price_increase = new_price - old_price

    prompt = (
        f"{name}'s business has fixed monthly costs of {_fmt_curr(fixed_cost)} and a variable production cost of "
        f"{_fmt_curr(var_cost)} per {item[:-1] if item.endswith('s') else item}. "
        f"Originally, the item sold for {_fmt_curr(old_price)}. {name} increases the selling price by "
        f"{_fmt_curr(price_increase)} to {_fmt_curr(new_price)}. "
        f"By how many units does the monthly break-even point decrease?"
    )

    correct_ans = f"Decreases by {_fmt(diff)} units"
    custom_opts = [
        f"Decreases by {_fmt(diff)} units",
        f"Increases by {_fmt(diff)} units",
        f"Decreases by {_fmt(new_be)} units",
        f"Decreases by {_fmt(old_be)} units",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate original break-even quantity [1 mark].\n"
        f"Original margin = {_fmt_curr(old_price)} - {_fmt_curr(var_cost)} = {_fmt_curr(old_margin)}.\n"
        f"Original break-even = {_fmt_curr(fixed_cost)} ÷ {_fmt_curr(old_margin)} = {_fmt(old_be)} units.\n"
        f"Step 2: Calculate new break-even quantity [1 mark].\n"
        f"New margin = {_fmt_curr(new_price)} - {_fmt_curr(var_cost)} = {_fmt_curr(new_margin)}.\n"
        f"New break-even = {_fmt_curr(fixed_cost)} ÷ {_fmt_curr(new_margin)} = {_fmt(new_be)} units.\n"
        f"Step 3: Calculate decrease [1 mark].\n"
        f"Difference = {_fmt(old_be)} - {_fmt(new_be)} = {_fmt(diff)} units ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="44",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the break-even quantity at both prices and find the difference.",
        tier_2=f"Old BE = {_fmt_curr(fixed_cost)} ÷ {_fmt_curr(old_margin)} = {_fmt(old_be)}. New BE = {_fmt_curr(fixed_cost)} ÷ {_fmt_curr(new_margin)} = {_fmt(new_be)}.",
        tier_3=f"The difference is {_fmt(old_be)} - {_fmt(new_be)} = {_fmt(diff)} units decrease.",
        r=r,
    )
