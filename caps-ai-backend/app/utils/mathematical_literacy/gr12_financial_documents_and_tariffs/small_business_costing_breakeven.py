"""Subskills 41 to 46: Small Business Costing, Pricing & Break-Even Analysis.
Covers start-up vs operating vs production cost classifications, batch unit costing,
markup & selling price derivation, break-even quantity, profit at volume, and target profit sales targets.
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


def gen_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Classifying small business cost categories."""
    item = r.choice([
        ("Commercial industrial dough mixer purchased once upfront", "Start-up / Capital cost"),
        ("Monthly rental fee for bakery kitchen premises", "Fixed operating cost"),
        ("Flour, sugar, butter, and yeast ingredients per batch", "Variable production cost"),
        ("Monthly comprehensive public liability insurance premium", "Fixed operating cost"),
        ("Custom branded cake boxes and ribbons per cake sold", "Variable production cost"),
        ("Shopfitting display shelves and glass counter installation", "Start-up / Capital cost"),
    ])
    cost_name, correct_cat = item

    prompt = (
        f"A small home confectionery and bakery business incurs the following business expense:\n"
        f"'{cost_name}'.\n\n"
        f"In financial planning and cost accounting, how is this expenditure correctly classified?"
    )

    correct_ans = correct_cat
    custom_opts = [
        "Start-up / Capital cost",
        "Fixed operating cost",
        "Variable production cost",
        "Tax-deductible personal drawing",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"1. Start-up costs are once-off initial investments in machinery, equipment, or fittings.\n"
        f"2. Fixed operating costs recur every month regardless of production volume (e.g. rent, insurance).\n"
        f"3. Variable production costs increase or decrease directly with the number of units produced (e.g. ingredients, packaging).\n"
        f"4. '{cost_name}' is correctly classified as: {correct_ans}."
    )
    t1 = "Consider whether this cost occurs only once, recurs monthly, or changes with each cake baked."
    t2 = "Fixed costs stay constant each month; variable costs rise with production."
    t3 = f"Classification: {correct_ans}."

    return _build_question_payload(
        "gr12_tariffs_subskill_41",
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


def gen_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Subskill 42: Calculating unit cost of production from batch ingredients and packaging."""
    batch_yield = r.choice([24, 30, 48, 60])
    ingredients_cost = r.choice([180.0, 240.0, 360.0])
    packaging_per_unit = 2.50

    unit_ingred_cost = round(ingredients_cost / batch_yield, 2)
    total_unit_cost = round(unit_ingred_cost + packaging_per_unit, 2)

    prompt = (
        f"A small craft producer bakes a batch yielding exactly {batch_yield} gourmet muffins.\n"
        f"The raw ingredients for the whole batch cost {_fmt_curr(ingredients_cost)}.\n"
        f"In addition, each individual muffin is packaged in a bio-degradable container costing {_fmt_curr(packaging_per_unit)}.\n\n"
        f"Calculate the total unit cost of production per muffin (in Rands)."
    )

    correct_ans = _fmt_curr(total_unit_cost)
    explanation = (
        f"1. Ingredient cost per muffin = {_fmt_curr(ingredients_cost)} ÷ {batch_yield} = {_fmt_curr(unit_ingred_cost)}.\n"
        f"2. Add packaging cost per unit = {_fmt_curr(unit_ingred_cost)} + {_fmt_curr(packaging_per_unit)} = {_fmt_curr(total_unit_cost)}."
    )
    t1 = f"Divide the batch ingredients cost ({_fmt_curr(ingredients_cost)}) by {batch_yield}."
    t2 = f"Add the {_fmt_curr(packaging_per_unit)} packaging fee to the ingredient unit cost."
    t3 = f"Unit cost = ({ingredients_cost} ÷ {batch_yield}) + {packaging_per_unit} = {_fmt_curr(total_unit_cost)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_42",
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


def gen_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Subskill 43: Determining selling price from unit cost and target markup percentage."""
    unit_cost = r.choice([15.00, 22.50, 35.00, 48.00])
    markup_pct = r.choice([40, 50, 60, 75])

    markup_rand = round(unit_cost * (markup_pct / 100.0), 2)
    selling_price = round(unit_cost + markup_rand, 2)

    prompt = (
        f"A manufacturer produces a handcrafted ceramic mug at a unit cost of {_fmt_curr(unit_cost)}.\n"
        f"To ensure business profitability and sustainability, the owner applies a {markup_pct}% markup on cost.\n\n"
        f"Calculate the selling price of the ceramic mug."
    )

    correct_ans = _fmt_curr(selling_price)
    explanation = (
        f"1. Markup amount = Unit Cost ({_fmt_curr(unit_cost)}) × {markup_pct}% = {_fmt_curr(markup_rand)}.\n"
        f"2. Selling Price = Unit Cost ({_fmt_curr(unit_cost)}) + Markup ({_fmt_curr(markup_rand)}) = {_fmt_curr(selling_price)}.\n"
        f"3. Alternatively: Selling Price = {_fmt_curr(unit_cost)} × (1 + {markup_pct}/100) = {_fmt_curr(selling_price)}."
    )
    t1 = f"Calculate {markup_pct}% of the unit cost ({_fmt_curr(unit_cost)})."
    t2 = f"Add the markup amount to {_fmt_curr(unit_cost)}."
    t3 = f"Selling price = {_fmt_curr(unit_cost)} × {1 + markup_pct/100} = {_fmt_curr(selling_price)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_43",
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


def gen_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Break-even quantity determination using unit contribution margin."""
    fixed_costs = r.choice([4800.0, 6000.0, 7500.0, 9000.0])
    selling_price = 45.00
    variable_cost = 20.00
    contribution_margin = selling_price - variable_cost  # R25,00

    breakeven_units = int(round(fixed_costs / contribution_margin))

    prompt = (
        f"A small entrepreneur produces and sells T-shirts with the following monthly cost structure:\n"
        f"• Fixed monthly operating costs (rent, equipment hire, utilities): {_fmt_curr(fixed_costs)}\n"
        f"• Variable production cost per T-shirt (blank shirt, printing ink): {_fmt_curr(variable_cost)}\n"
        f"• Selling price per T-shirt: {_fmt_curr(selling_price)}\n\n"
        f"Calculate the break-even quantity (number of T-shirts that must be sold each month to cover all costs)."
    )

    correct_ans = f"{breakeven_units} units"
    explanation = (
        f"1. Contribution margin per unit = Selling Price ({_fmt_curr(selling_price)}) - Variable Cost ({_fmt_curr(variable_cost)})\n"
        f"   = {_fmt_curr(contribution_margin)} per unit.\n"
        f"2. Break-even quantity = Fixed Operating Costs ÷ Contribution Margin\n"
        f"   = {_fmt_curr(fixed_costs)} ÷ {_fmt_curr(contribution_margin)} = {breakeven_units} units."
    )
    t1 = f"Subtract variable cost ({_fmt_curr(variable_cost)}) from selling price ({_fmt_curr(selling_price)}) to find contribution margin."
    t2 = f"Divide total fixed costs ({_fmt_curr(fixed_costs)}) by the contribution margin ({_fmt_curr(contribution_margin)})."
    t3 = f"Break-even quantity = {fixed_costs} ÷ {contribution_margin} = {breakeven_units} units."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_44",
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


def gen_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Subskill 45: Monthly profit calculation at a specified sales volume."""
    fixed_costs = 5500.00
    selling_price = 65.00
    variable_cost = 25.00
    units_sold = r.choice([200, 250, 300, 350])

    total_revenue = units_sold * selling_price
    total_cost = fixed_costs + (units_sold * variable_cost)
    profit = round(total_revenue - total_cost, 2)

    d_spec_45 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Workshop Monthly Financials ({units_sold} Units Sold)",
        "categories": ["Total Revenue", "Total Cost", "Net Profit"],
        "series": [
            {"name": "Amount", "values": [total_revenue, total_cost, profit]}
        ],
    }

    prompt = (
        f"Refer to the monthly financial statement of a bespoke leather-goods workshop with fixed monthly costs of R 5 500,00.\n"
        f"Each leather wallet costs R 25,00 in raw materials and sells for R 65,00.\n\n"
        f"During August, the workshop made and sold {units_sold} wallets.\n"
        f"Calculate the net profit earned by the workshop for the month."
    )

    correct_ans = _fmt_curr(profit)
    explanation = (
        f"1. Total Revenue = {units_sold} units × R 65,00 = {_fmt_curr(total_revenue)}.\n"
        f"2. Total Variable Cost = {units_sold} units × R 25,00 = {_fmt_curr(units_sold * variable_cost)}.\n"
        f"3. Total Cost = Fixed Costs (R 5 500,00) + Variable Costs ({_fmt_curr(units_sold * variable_cost)}) = {_fmt_curr(total_cost)}.\n"
        f"4. Net Profit = Total Revenue ({_fmt_curr(total_revenue)}) - Total Cost ({_fmt_curr(total_cost)}) = {_fmt_curr(profit)}."
    )
    t1 = f"Calculate Total Revenue: {units_sold} × R 65,00."
    t2 = f"Calculate Total Cost: R 5 500 + ({units_sold} × R 25,00)."
    t3 = f"Net Profit = Revenue - Total Cost = {_fmt_curr(profit)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_45",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_45,
    )


def gen_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Subskill 46: Required sales volume to achieve a specific target profit."""
    fixed_costs = 6000.00
    selling_price = 50.00
    variable_cost = 18.00
    contrib = selling_price - variable_cost  # R32,00
    target_profit = r.choice([4800.0, 6400.0, 8000.0, 9600.0])

    required_units = int(round((fixed_costs + target_profit) / contrib))

    prompt = (
        f"A caterer sells pre-packed lunchboxes:\n"
        f"• Selling price per lunchbox: {_fmt_curr(selling_price)}\n"
        f"• Variable cost of ingredients & container: {_fmt_curr(variable_cost)}\n"
        f"• Fixed monthly kitchen lease & utility bills: {_fmt_curr(fixed_costs)}\n\n"
        f"How many lunchboxes must the caterer sell in a month to achieve a target net profit of {_fmt_curr(target_profit)}?"
    )

    correct_ans = f"{required_units} units"
    explanation = (
        f"1. Contribution margin per unit = Selling Price ({_fmt_curr(selling_price)}) - Variable Cost ({_fmt_curr(variable_cost)}) = {_fmt_curr(contrib)}.\n"
        f"2. Total required gross margin = Fixed Costs ({_fmt_curr(fixed_costs)}) + Target Profit ({_fmt_curr(target_profit)}) = {_fmt_curr(fixed_costs + target_profit)}.\n"
        f"3. Required sales volume = {_fmt_curr(fixed_costs + target_profit)} ÷ {_fmt_curr(contrib)} = {required_units} units."
    )
    t1 = f"Add the target profit ({_fmt_curr(target_profit)}) to the fixed costs ({_fmt_curr(fixed_costs)})."
    t2 = f"Subtract variable cost from selling price: {selling_price} - {variable_cost} = {_fmt_curr(contrib)}."
    t3 = f"Required units = ({fixed_costs} + {target_profit}) ÷ {contrib} = {required_units} units."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_46",
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
