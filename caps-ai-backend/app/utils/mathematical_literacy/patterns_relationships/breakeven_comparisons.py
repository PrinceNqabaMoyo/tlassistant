"""Cluster 5: Two-Graph Comparisons & Break-Even Analysis (Subskills 37 to 44)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)

# --------------------------------------------------------------------------- #
# Subskill 37: Point of Intersection Coordinates
# --------------------------------------------------------------------------- #
def _gen_pat_comp_identify_intersection_point(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_identify_intersection_point"
    name = r.choice(SA_NAMES)
    intersect_x = r.choice([50, 100, 150, 200])  # e.g. minutes or km
    intersect_y = r.choice([250, 300, 350, 400])  # total cost
    correct_ans = f"({intersect_x}; {intersect_y})"

    prompt = (
        f"{name} plots two competing cellular phone plans on the same Cartesian coordinate system.\n"
        f"The two linear graphs cross each other at exactly {intersect_x} minutes on the horizontal axis "
        f"and R {intersect_y} on the vertical axis.\n\n"
        f"Write down the coordinates of this **point of intersection** in standard $(x; y)$ format."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The point of intersection represents the common $(x; y)$ coordinate where both graphs have identical values.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Read horizontal coordinate $x = {intersect_x}$ and vertical coordinate $y = {intersect_y}$.\n"
        f"Combine as an ordered pair $({intersect_x}; {intersect_y})$. ✓ [1 Mark: Method – constructing ordered pair from axes values]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate coordinate pair]"
    )

    d1 = f"({intersect_y}; {intersect_x})"  # reversed
    d2 = f"({intersect_x}; 0)"
    d3 = f"(0; {intersect_y})"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    bep_diag = {
        "kind": "break_even",
        "fixed_cost": 150,
        "variable_cost": 1,
        "selling_price": 2,
        "show_bep_coords": True,
        "caption": f"Linear Plans Point of Intersection ({intersect_x}; {intersect_y})",
    }

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Write horizontal x first, then vertical y: (x; y).",
        tier_2=f"x = {intersect_x}, y = {intersect_y}.",
        tier_3=f"Intersection point = {correct_ans}.",
        r=r,
        diagram_spec=bep_diag,
    )

# --------------------------------------------------------------------------- #
# Subskill 38: Meaning of Intersection Point
# --------------------------------------------------------------------------- #
def _gen_pat_comp_meaning_of_intersection_point(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_meaning_of_intersection_point"
    name = r.choice(SA_NAMES)
    minutes = r.choice([100, 150, 200])
    cost = r.choice([250, 300, 350])
    correct_ans = f"Both cellular plans cost the exact same amount (R {cost}) at {minutes} call minutes"

    prompt = (
        f"{name} compares a Prepaid plan and a Contract plan. Their cost graphs intersect at the coordinate point $({minutes}; {cost})$.\n\n"
        f"What is the practical real-world meaning of this **point of intersection**?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The point of intersection is where the two graphs share the identical $x$ and $y$ values.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"At {minutes} minutes of calling, both options result in the exact same total bill of R {cost}. "
        f"This is the break-even point of equal cost. ✓ [1 Mark: Method – interpreting intersection as point of equality]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate practical interpretation]"
    )

    custom = [
        correct_ans,
        f"The Prepaid plan is always cheaper by R {cost}",
        f"The Contract plan becomes free after {minutes} minutes",
        f"Neither plan can be used beyond {minutes} minutes",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="At the intersection point, the y-value (cost) is identical for both graphs.",
        tier_2=f"At {minutes} minutes, both options cost R {cost}.",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 39: Contract vs Prepaid Cheaper Option
# --------------------------------------------------------------------------- #
def _gen_pat_comp_contract_vs_prepaid_cheaper_option(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_contract_vs_prepaid_cheaper_option"
    name = r.choice(SA_NAMES)
    # Plan A: Prepaid R2/min (no monthly fee) -> cost = 2*m
    # Plan B: Contract R100 monthly fee + R1/min -> cost = 100 + m
    # Intersection at m = 100 mins (both cost R200)
    minutes_usage = r.choice([40, 60, 140, 180])

    if minutes_usage < 100:
        cheaper_plan = "Option A (Prepaid)"
        cost_a = 2.0 * minutes_usage
        cost_b = 100.0 + 1.0 * minutes_usage
        reason = f"At {minutes_usage} minutes (below intersection of 100 min), Option A costs R {int(cost_a)} while Option B costs R {int(cost_b)}"
    else:
        cheaper_plan = "Option B (Contract)"
        cost_a = 2.0 * minutes_usage
        cost_b = 100.0 + 1.0 * minutes_usage
        reason = f"At {minutes_usage} minutes (above intersection of 100 min), Option B costs R {int(cost_b)} while Option A costs R {int(cost_a)}"

    correct_ans = cheaper_plan

    prompt = (
        f"{name} is deciding between two cell phone tariffs:\n"
        f"  • Option A (Prepaid): R 2,00 per minute (no fixed monthly fee)\n"
        f"  • Option B (Contract): R 100,00 fixed monthly fee + R 1,00 per minute\n"
        f"(The two plans intersect at 100 minutes, where both cost R 200,00).\n\n"
        f"If {name} expects to make **{minutes_usage} minutes** of calls per month, which option is cheaper?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate the monthly cost under each plan for {minutes_usage} minutes of usage and compare.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Option A Cost}} = 2,00 \\times {minutes_usage} = \\text{{R }}{_fmt(cost_a)}$$\n"
        f"$$\\text{{Option B Cost}} = 100,00 + (1,00 \\times {minutes_usage}) = \\text{{R }}{_fmt(cost_b)}$$ ✓ [1 Mark: Method – evaluating both formulas for specified usage]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ({reason}) ✓ [1 Mark: Accuracy – correct decision]"
    )

    custom = ["Option A (Prepaid)", "Option B (Contract)", "Both cost the same", "Neither is available"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the cost for each option at the given minutes.",
        tier_2=f"Option A = R {_fmt(cost_a)}, Option B = R {_fmt(cost_b)}.",
        tier_3=f"The cheaper option is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 40: Car Rental Plan Comparison
# --------------------------------------------------------------------------- #
def _gen_pat_comp_car_rental_plan_comparison(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_car_rental_plan_comparison"
    name = r.choice(SA_NAMES)
    flat_fee = r.choice([250, 300, 350])
    rate_a = 2.00
    rate_b = 3.50
    # Break-even: flat_fee + rate_a * x = rate_b * x => x = flat_fee / (rate_b - rate_a) = flat_fee / 1.5
    break_even_km = round(flat_fee / (rate_b - rate_a))
    test_km = break_even_km + r.choice([40, 60, 80])

    cost_a = flat_fee + rate_a * test_km
    cost_b = rate_b * test_km
    cheaper = "Option A" if cost_a < cost_b else "Option B"
    correct_ans = f"{cheaper} is cheaper for {_fmt(test_km)} km (Option A: R {_fmt(cost_a)}, Option B: R {_fmt(cost_b)})"

    prompt = (
        f"{name} is comparing two car rental options for a trip of {_fmt(test_km)} km:\n"
        f"• Option A: Flat fee of R {flat_fee} plus R {_fmt(rate_a)} per km\n"
        f"• Option B: No flat fee (R 0), but R {_fmt(rate_b)} per km\n\n"
        f"Refer to the car rental comparison graph below.\n\n"
        f"Determine which option is cheaper for a {_fmt(test_km)} km trip and calculate the total cost for both options."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate cost for each option at x = {test_km} km and compare.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Cost A = R {flat_fee} + ({rate_a} × {test_km}) = R {_fmt(cost_a)}.\n"
        f"Cost B = {rate_b} × {test_km} = R {_fmt(cost_b)}. ✓ [1 Mark: Method – evaluating both cost functions]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct comparison]"
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Car Rental Comparison ({name}: {test_km} km)",
        "lines": [
            {"points": [[0, flat_fee], [test_km, cost_a]], "label": "Option A"},
            {"points": [[0, 0], [test_km, cost_b]], "label": "Option B"},
        ],
    }

    custom = [
        correct_ans,
        f"Option B is cheaper for {_fmt(test_km)} km",
        "Both options have identical total cost",
        "Neither option is viable",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the cost for each option at the given distance.",
        tier_2=f"Option A = {flat_fee} + ({rate_a} × {test_km}); Option B = {rate_b} × {test_km}.",
        tier_3=f"{correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

    if p1 < p2:
        cheaper = "Plan 1 (Unlimited km)"
        diff = p2 - p1
    else:
        cheaper = "Plan 2 (Base + km rate)"
        diff = p1 - p2

    correct_ans = cheaper

    prompt = (
        f"{name} compares two car rental packages for a 1-day trip of {km} km:\n"
        f"  • Plan 1: Flat rate of R 500,00 per day with unlimited free kilometres\n"
        f"  • Plan 2: Base fee of R 250,00 per day plus R 1,50 per kilometre driven\n\n"
        f"Which package is cheaper for driving {km} km?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate the total cost for driving {km} km under both packages.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Plan 1 Cost}} = \\text{{R 500,00}}$$\n"
        f"$$\\text{{Plan 2 Cost}} = 250,00 + (1,50 \\times {km}) = 250,00 + {_fmt(1.5 * km)} = \\text{{R }}{_fmt(p2)}$$ ✓ [1 Mark: Method – calculating both options]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** (saves R {_fmt(diff)}) ✓ [1 Mark: Accuracy – correct comparison choice]"
    )

    custom = ["Plan 1 (Unlimited km)", "Plan 2 (Base + km rate)", "Both cost exactly R 500", "Neither package is suitable"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the cost of Plan 2: R 250 + (R 1,50 × km).",
        tier_2=f"Plan 1 = R 500,00; Plan 2 = R {_fmt(p2)}.",
        tier_3=f"The cheaper package is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 41: Break-even Units (Income = Cost)
# --------------------------------------------------------------------------- #
def _gen_pat_comp_breakeven_units_income_equals_cost(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_breakeven_units_income_equals_cost"
    name = r.choice(SA_NAMES)
    fixed_cost = r.choice([600, 800, 1000, 1200])
    var_cost = r.choice([10, 15, 20])
    sell_price = var_cost + r.choice([10, 20, 25])  # ensures positive margin
    margin = sell_price - var_cost
    # ensure clean division
    while fixed_cost % margin != 0:
        fixed_cost = margin * r.choice([25, 40, 50])
    breakeven_n = fixed_cost // margin
    correct_ans = f"{breakeven_n} items"

    prompt = (
        f"{name} operates a small school tuckshop business selling homemade muffins:\n"
        f"  • Fixed setup costs (oven rental & stall): {_fmt_curr(fixed_cost)}\n"
        f"  • Variable ingredient cost per muffin: {_fmt_curr(var_cost)}\n"
        f"  • Selling price per muffin: {_fmt_curr(sell_price)}\n\n"
        f"Calculate the **break-even quantity** (number of muffins {name} must sell so that Total Income equals Total Cost).\n\n"
        f"**Formula**: $\\text{{Break-even}} = \\frac{{\\text{{Fixed Costs}}}}{{\\text{{Selling Price}} - \\text{{Variable Cost}}}}$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Break-even occurs where $\\text{{Total Income}} = \\text{{Total Cost}}$, meaning profit is exactly zero.\n"
        f"$$\\text{{Selling Price}} \\times n = \\text{{Fixed Cost}} + (\\text{{Variable Cost}} \\times n)$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Profit margin per muffin}} = {_fmt_curr(sell_price)} - {_fmt_curr(var_cost)} = {_fmt_curr(margin)}$$\n"
        f"$$n = \\frac{{{fixed_cost}}}{{{margin}}}$$ ✓ [1 Mark: Method – dividing fixed cost by profit margin per unit]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$n = {breakeven_n}\\text{{ items}}$$ ✓ [1 Mark: Accuracy – accurate break-even quantity]"
    )

    d1 = f"{breakeven_n + 10} items"
    d2 = f"{breakeven_n - 5} items"
    d3 = f"{fixed_cost // sell_price} items"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    bep_diag = {
        "kind": "break_even",
        "fixed_cost": fixed_cost,
        "variable_cost": var_cost,
        "selling_price": sell_price,
        "show_bep_coords": False,
        "caption": "Cost vs. Income Break-Even Analysis",
    }

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the variable cost from selling price to find profit per item.",
        tier_2=f"Margin = {_fmt_curr(sell_price)} - {_fmt_curr(var_cost)} = {_fmt_curr(margin)}. Divide {fixed_cost} by {margin}.",
        tier_3=f"Break-even = {correct_ans}.",
        r=r,
        diagram_spec=bep_diag,
    )

# --------------------------------------------------------------------------- #
# Subskill 42: Profit or Loss Calculation
# --------------------------------------------------------------------------- #
def _gen_pat_comp_profit_or_loss_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_profit_or_loss_calculation"
    name = r.choice(SA_NAMES)
    fixed_cost = 500.00
    var_cost = 15.00
    sell_price = 35.00
    # break-even is 500 / 20 = 25 items
    sold = r.choice([15, 20, 35, 40, 50])
    income = sold * sell_price
    cost = fixed_cost + sold * var_cost
    diff = income - cost

    if diff >= 0:
        correct_ans = f"Profit of {_fmt_curr(diff)}"
    else:
        correct_ans = f"Loss of {_fmt_curr(abs(diff))}"

    prompt = (
        f"{name} produces and sells hand-crafted bracelets:\n"
        f"  • Total Cost formula: $\\text{{Cost}} = 500 + (15 \\times n)$\n"
        f"  • Total Income formula: $\\text{{Income}} = 35 \\times n$\n\n"
        f"Calculate the **profit or loss** made if {name} manufactures and sells **{sold} bracelets**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"$\\text{{Profit/Loss}} = \\text{{Total Income}} - \\text{{Total Cost}}$. "
        f"A positive result indicates a profit; a negative result indicates a loss.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Income}} = 35 \\times {sold} = \\text{{R }}{_fmt(income)}$$\n"
        f"$$\\text{{Cost}} = 500 + (15 \\times {sold}) = 500 + {_fmt(sold * var_cost)} = \\text{{R }}{_fmt(cost)}$$\n"
        f"$$\\text{{Difference}} = {_fmt(income)} - {_fmt(cost)} = {_fmt(diff)}$$ ✓ [1 Mark: Method – evaluating income minus cost]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate currency difference and label]"
    )

    d1 = f"Loss of {_fmt_curr(diff)}" if diff >= 0 else f"Profit of {_fmt_curr(abs(diff))}"  # inverted
    d2 = _fmt_curr(income)
    d3 = _fmt_curr(cost)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Profit/Loss = Income - Total Cost.",
        tier_2=f"Income = {_fmt_curr(income)}, Cost = {_fmt_curr(cost)}.",
        tier_3=f"Result = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 43: Income Formula and Origin Graph
# --------------------------------------------------------------------------- #
def _gen_pat_comp_income_formula_and_graph(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_income_formula_and_graph"
    name = r.choice(SA_NAMES)
    selling_price = r.choice([25, 30, 40, 50])
    items = r.choice([50, 80, 100, 120])
    total_income = selling_price * items
    correct_ans = f"R {_fmt(total_income)}"

    prompt = (
        f"{name} runs a small business selling handmade crafts at R {selling_price} each.\n"
        f"Refer to the business income graph below (Income = {selling_price} × items sold).\n\n"
        f"Calculate the total income when {items} craft items are sold."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Income is directly proportional to units sold: Income = Price × Quantity.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Income = R {selling_price} × {items} = R {_fmt(total_income)}. ✓ [1 Mark: Method – linear income evaluation]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct Rand income]"
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Business Income Profile ({name}: R{selling_price}/unit)",
        "lines": [{"points": [[0, 0], [items, total_income]], "label": "Income Line"}],
    }

    custom = [correct_ans, f"R {_fmt(total_income + selling_price)}", f"R {_fmt(total_income - selling_price)}", f"R {_fmt(total_income // 2)}"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Multiply selling price (R {selling_price}) by items sold ({items}).",
        tier_2=f"Income = {selling_price} × {items}.",
        tier_3=f"Total income = {correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} sells baked meat pies at a weekend market stall for R {price} each.\n\n"
        f"Which formula and starting coordinate correctly represent the **Total Income** line on a break-even graph?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Income is direct proportion: selling zero pies yields zero Rands income. "
        f"Therefore, the income line must pass through the origin $(0; 0)$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Income}} = \\text{{Price per pie}} \\times n = {price}n$$\n"
        f"At $n = 0$, $\\text{{Income}} = 0$. The graph starts at $(0; 0)$. ✓ [1 Mark: Method – defining income direct proportion from origin]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct equation and origin coordinate]"
    )

    custom = [
        correct_ans,
        f"Income = {price} + n (starts at (0; {price}))",
        f"Income = {price} × n (starts at (0; {price}))",
        f"Income = n / {price} (starts at (0; 0))",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="If you sell zero items, you earn zero Rands: starts at (0; 0).",
        tier_2=f"Income = {price} × n.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 44: Production Cost Formula and Y-Intercept
# --------------------------------------------------------------------------- #
def _gen_pat_comp_production_cost_formula_and_graph(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_production_cost_formula_and_graph"
    name = r.choice(SA_NAMES)
    fixed_cost = r.choice([400, 500, 600, 800])
    var_cost = r.choice([12, 15, 18, 20])
    items = r.choice([30, 40, 50, 60])
    total_cost = fixed_cost + var_cost * items
    correct_ans = f"R {_fmt(total_cost)}"

    prompt = (
        f"{name} bakes and sells artisan pies. Production costs follow the cost graph below:\n"
        f"Formula: Total Cost = R {fixed_cost} (fixed equipment) + (R {var_cost} × pies produced)\n\n"
        f"Calculate the total production cost to bake {items} pies."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Total Cost = Fixed Cost + (Variable Cost per unit × Number of Units).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Total Cost = R {fixed_cost} + ({var_cost} × {items}) = R {fixed_cost} + R {var_cost * items} = R {_fmt(total_cost)}. "
        f"✓ [1 Mark: Method – substituting into linear cost equation]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct total production cost]"
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Artisan Bakery Production Cost ({name})",
        "lines": [{"points": [[0, fixed_cost], [items, total_cost]], "label": "Total Cost Line"}],
    }

    custom = [correct_ans, f"R {_fmt(total_cost + var_cost)}", f"R {_fmt(total_cost - fixed_cost)}", f"R {_fmt(total_cost + 100)}"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Add fixed cost (R {fixed_cost}) to variable cost ({var_cost} × {items}).",
        tier_2=f"Cost = {fixed_cost} + ({var_cost} × {items}).",
        tier_3=f"Total cost = {correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} sets up a market stall with fixed stall rent of R {overhead}.\n"
        f"Each item made has a material cost of R {var_cost}.\n\n"
        f"Which formula and starting coordinate correctly represent the **Total Cost** line on a break-even graph?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Total Cost is composed of fixed overhead plus variable production cost.\n"
        f"Even if zero items are produced ($n = 0$), the fixed stall rent of R {overhead} must still be paid.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total Cost}} = \\text{{Fixed Overhead}} + (\\text{{Variable Cost}} \\times n) = {overhead} + ({var_cost} \\times n)$$\n"
        f"At $n = 0$, $\\text{{Cost}} = {overhead}$. The vertical intercept is $(0; {overhead})$. "
        f"✓ [1 Mark: Method – constructing cost equation and identifying non-zero y-intercept]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct equation and y-intercept coordinate]"
    )

    custom = [
        correct_ans,
        f"Cost = {var_cost} × n (starts at (0; 0))",
        f"Cost = ({overhead} + {var_cost}) × n (starts at (0; 0))",
        f"Cost = {overhead} × n (starts at (0; {overhead}))",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Cost includes fixed overhead even before producing any items: starts at (0; overhead).",
        tier_2=f"Cost = {overhead} + {var_cost}n.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )
