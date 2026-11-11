"""Cluster 2: Order of Operations & Calculator Operations (8 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_num_op_bodmas_brackets_multiplication_addition(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    base_fee = r.choice([150, 200, 250, 300])
    hourly_rate = r.choice([45, 50, 65, 80])
    hours_day1 = r.choice([4, 5, 6])
    hours_day2 = r.choice([2, 3, 4])
    total_hours = hours_day1 + hours_day2
    total_cost = base_fee + (hourly_rate * total_hours)
    ans_str = _fmt_curr(total_cost)

    prompt = (
        f"{name} hires equipment for home garden landscaping. The rental invoice is calculated using the formula:\n\n"
        f"$$\\text{{Total Cost}} = \\text{{{_fmt_curr(base_fee)}}} + \\text{{{_fmt_curr(hourly_rate)}}} \\times ({hours_day1} + {hours_day2})$$\n\n"
        f"Applying the standard mathematical **Order of Operations (BODMAS / PEMDAS)**, calculate the total cost in Rands."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• According to BODMAS:\n"
        f"  1. **B**rackets must be evaluated first: $({hours_day1} + {hours_day2}) = {total_hours}$.\n"
        f"  2. **M**ultiplication is performed next: $\\text{{{_fmt_curr(hourly_rate)}}} \\times {total_hours} = \\text{{{_fmt_curr(hourly_rate * total_hours)}}}$.\n"
        f"  3. **A**ddition is performed last: $\\text{{{_fmt_curr(base_fee)}}} + \\text{{{_fmt_curr(hourly_rate * total_hours)}}} = \\text{{{_fmt_curr(total_cost)}}}$.\n\n"
        f"**Step 2: Method Setup & Stepwise Calculation**\n"
        f"• Brackets: ${hours_day1} + {hours_day2} = {total_hours}$.\n"
        f"• Multiplication: ${hourly_rate} \\times {total_hours} = {hourly_rate * total_hours}$.\n"
        f"• Addition: ${base_fee} + {hourly_rate * total_hours} = {total_cost}$.\n"
        f"✓ **[1 Mark: Method – evaluating brackets first, then multiplying before adding]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct final total in Rands]**"
    )
    return _make_q(
        subskill="num_op_bodmas_brackets_multiplication_addition",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – BODMAS order of operations", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Add the numbers inside the brackets first: {hours_day1} + {hours_day2} = {total_hours}.",
            "tier_2": f"Multiply {_fmt_curr(hourly_rate)} by {total_hours} to get {_fmt_curr(hourly_rate * total_hours)}, then add {_fmt_curr(base_fee)}.",
            "tier_3": f"Total cost = {_fmt_curr(total_cost)}."
        },
        r=r
    )

def _gen_num_op_bodmas_division_fraction_bar(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_sales = r.choice([14500, 16800, 19200, 22400])
    expenses = r.choice([3500, 4200, 4800, 5600])
    partners = r.choice([2, 3, 4])
    net_profit = total_sales - expenses
    share_per_partner = round(net_profit / partners, 2)
    ans_str = _fmt_curr(share_per_partner)

    prompt = (
        f"{name} and partners share the total market stall profit equally. The calculation formula is:\n\n"
        f"$$\\text{{Share per Partner}} = \\frac{{\\text{{{_fmt_curr(total_sales)}}} - \\text{{{_fmt_curr(expenses)}}}}}{{{partners}}}$$\n\n"
        f"Calculate each partner's share in Rands, observing the rule that a horizontal fraction bar groups the entire numerator."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• The horizontal fraction bar acts as a grouping symbol (brackets) for the entire numerator:\n"
        f"  $$\\text{{Numerator}} = \\text{{{_fmt_curr(total_sales)}}} - \\text{{{_fmt_curr(expenses)}}} = \\text{{{_fmt_curr(net_profit)}}}$$\n"
        f"• The subtraction must be completed before dividing by the number of partners ({partners}).\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Numerator}} = {total_sales} - {expenses} = {net_profit}$.\n"
        f"• $\\text{{Division}} = \\frac{{{net_profit}}}{{{partners}}} = {_fmt(share_per_partner)}$.\n"
        f"✓ **[1 Mark: Method – evaluating the numerator subtraction before dividing by {partners}]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct share per partner in Rands]**"
    )
    return _make_q(
        subskill="num_op_bodmas_division_fraction_bar",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (numerator subtraction) ÷ denominator", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Subtract expenses from sales first: {_fmt_curr(total_sales)} - {_fmt_curr(expenses)} = {_fmt_curr(net_profit)}.",
            "tier_2": f"Divide {_fmt_curr(net_profit)} by {partners} partners.",
            "tier_3": f"Share per partner = {_fmt_curr(share_per_partner)}."
        },
        r=r
    )

def _gen_num_op_consecutive_discounts_order(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    original_price = round(r.choice([1200.00, 1500.00, 1800.00, 2000.00]), 2)
    trade_disc_pct = r.choice([10, 15, 20])
    cash_disc_pct = 5
    after_trade = round(original_price * (1 - trade_disc_pct / 100.0), 2)
    final_price = round(after_trade * (1 - cash_disc_pct / 100.0), 2)
    ans_str = _fmt_curr(final_price)

    prompt = (
        f"{name} purchases wholesale stock with an original list price of **{_fmt_curr(original_price)}**.\n\n"
        f"The wholesaler offers:\n"
        f"1. A **{trade_disc_pct}% trade discount** deducted from the list price.\n"
        f"2. An additional **5% prompt cash settlement discount** applied to the remaining reduced balance.\n\n"
        f"Calculate the **final cash price** {name} pays."
    )
    sol = (
        f"**Step 1: Mathematical & Financial Concept**\n"
        f"• Consecutive percentage discounts are applied sequentially, not added together:\n"
        f"  - First calculate the price after the {trade_disc_pct}% trade discount.\n"
        f"  - Then apply the 5% cash settlement discount to that new lower balance.\n\n"
        f"**Step 2: Method Setup & Sequential Calculations**\n"
        f"• $\\text{{Price after trade discount}} = \\text{{{_fmt_curr(original_price)}}} \\times (1 - 0,{trade_disc_pct}) = \\text{{{_fmt_curr(after_trade)}}}$.\n"
        f"• $\\text{{Final price after 5\\% cash discount}} = \\text{{{_fmt_curr(after_trade)}}} \\times (1 - 0,05) = \\text{{{_fmt_curr(final_price)}}}$.\n"
        f"✓ **[1 Mark: Method – applying consecutive discounts sequentially]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct final discounted price in Rands]**"
    )
    return _make_q(
        subskill="num_op_consecutive_discounts_order",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – sequential discount calculation", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Do not add the percentages! First find {trade_disc_pct}% off {_fmt_curr(original_price)} = {_fmt_curr(after_trade)}.",
            "tier_2": f"Take 5% off the new price {_fmt_curr(after_trade)}: {_fmt_curr(after_trade)} × 0,95 = {_fmt_curr(final_price)}.",
            "tier_3": f"Final price = {_fmt_curr(final_price)}."
        },
        r=r
    )

def _gen_num_op_calculator_memory_chain_totals(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    items = [
        ("loafs of brown bread", 3, 16.50),
        ("2-litre cartons of fresh milk", 2, 34.00),
        ("500 g tubs of margarine", 2, 28.50),
        ("packets of tea bags", 1, 42.00)
    ]
    subtotal = round(sum(qty * price for _, qty, price in items), 2)
    ans_str = _fmt_curr(subtotal)

    prompt = (
        f"{name} buys groceries at the local supermarket:\n\n"
        f"• 3 loaves of brown bread at **R 16,50 each**\n"
        f"• 2 cartons of milk (2 L) at **R 34,00 each**\n"
        f"• 2 tubs of margarine (500 g) at **R 28,50 each**\n"
        f"• 1 box of tea bags at **R 42,00 each**\n\n"
        f"Calculate the **total till slip amount** for these items."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Calculate the subtotal for each item (Quantity $\\times$ Unit Price), then add all subtotals together:\n"
        f"  $$\\text{{Total}} = (3 \\times 16,50) + (2 \\times 34,00) + (2 \\times 28,50) + (1 \\times 42,00)$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• Bread: $3 \\times 16,50 = 49,50$.\n"
        f"• Milk: $2 \\times 34,00 = 68,00$.\n"
        f"• Margarine: $2 \\times 28,50 = 57,00$.\n"
        f"• Tea: $1 \\times 42,00 = 42,00$.\n"
        f"• Grand Total = $49,50 + 68,00 + 57,00 + 42,00 = \\text{{{_fmt_curr(subtotal)}}}$.\n"
        f"✓ **[1 Mark: Method – multiplying each quantity by unit price and summing]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total purchase amount in Rands]**"
    )
    return _make_q(
        subskill="num_op_calculator_memory_chain_totals",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – sum of (quantity × unit price)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Multiply each item quantity by its unit price, then add the products together.",
            "tier_2": "Bread = R 49,50; Milk = R 68,00; Margarine = R 57,00; Tea = R 42,00.",
            "tier_3": f"Grand total = {_fmt_curr(subtotal)}."
        },
        r=r
    )

def _gen_num_op_fraction_addition_subtraction_practical(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    rent_frac = (1, 4)  # 1/4
    food_frac = (1, 3)  # 1/3
    # 1 - (1/4 + 1/3) = 1 - 7/12 = 5/12
    ans_str = "5/12"

    prompt = (
        f"{name} allocates a monthly salary as follows:\n\n"
        f"• **\\frac{{1}}{{4}}** of the salary is spent on housing rent.\n"
        f"• **\\frac{{1}}{{3}}** of the salary is spent on groceries and food.\n\n"
        f"What **fraction of the salary** remains for all other living expenses and savings?"
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• The whole salary is represented by $1$.\n"
        f"• Find a common denominator to add the fractions spent: $\\text{{LCM}}(4, 3) = 12$.\n"
        f"• Subtract the combined fraction from $1$.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• Rent: $\\frac{{1}}{{4}} = \\frac{{3}}{{12}}$.\n"
        f"• Food: $\\frac{{1}}{{3}} = \\frac{{4}}{{12}}$.\n"
        f"• Total spent: $\\frac{{3}}{{12}} + \\frac{{4}}{{12}} = \\frac{{7}}{{12}}$.\n"
        f"• Remaining fraction: $1 - \\frac{{7}}{{12}} = \\frac{{12}}{{12}} - \\frac{{7}}{{12}} = \\frac{{5}}{{12}}$.\n"
        f"✓ **[1 Mark: Method – finding common denominator 12 and subtracting sum from 1]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct remaining fraction]**"
    )
    custom_opts = ["5/12", "7/12", "1/12", "2/7"]
    return _make_q(
        subskill="num_op_fraction_addition_subtraction_practical",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 1 - (1/4 + 1/3) with LCM 12", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Convert both fractions to twelfths: 1/4 = 3/12 and 1/3 = 4/12.",
            "tier_2": "Add them: 3/12 + 4/12 = 7/12. Subtract from 12/12.",
            "tier_3": f"Remaining fraction = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_op_mixed_number_multiplication(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    batches = 2.5  # 2 1/2
    sugar_per_batch = 1.75  # 1 3/4 cups
    total_sugar = round(batches * sugar_per_batch, 3)
    # 2.5 * 1.75 = 4.375 = 4 3/8 cups
    ans_str = "4,375 cups"

    prompt = (
        f"{name} is baking traditional South African koeksisters for a church bazaar. A single recipe batch requires **1\\frac{{3}}{{4}} cups of sugar**.\n\n"
        f"{name} plans to prepare **2\\frac{{1}}{{2}} batches** of the recipe.\n\n"
        f"Calculate the **total amount of sugar needed**, expressed as a decimal number of cups."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Convert mixed numbers to improper fractions or decimal equivalents:\n"
        f"  $$1\\frac{{3}}{{4}} = 1,75\\text{{ cups}}$$\n"
        f"  $$2\\frac{{1}}{{2}} = 2,5\\text{{ batches}}$$\n"
        f"• Total sugar = $\\text{{Batches}} \\times \\text{{Sugar per batch}}$.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Total Sugar}} = 2,5 \\times 1,75 = {_fmt(total_sugar, 3)}\\text{{ cups}}$.\n"
        f"✓ **[1 Mark: Method – multiplying batch quantity by recipe ingredient requirement]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct decimal cups]**"
    )
    custom_opts = [
        "4,375 cups",
        "3,250 cups",
        "4,250 cups",
        "5,125 cups"
    ]
    return _make_q(
        subskill="num_op_mixed_number_multiplication",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 2,5 × 1,75", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Convert 1 3/4 to 1,75 and 2 1/2 to 2,5.",
            "tier_2": "Multiply 2,5 × 1,75.",
            "tier_3": f"Total sugar = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_op_reciprocal_unit_rate(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    coverage_rate = r.choice([8, 10, 12])  # m^2 per litre
    # Reciprocal: litres per m^2 = 1 / coverage_rate
    litres_per_m2 = round(1.0 / coverage_rate, 3)
    ans_str = f"{_fmt(litres_per_m2, 3)} L/m²"

    prompt = (
        f"A tin of wall primer paint specifies a coverage rate of **{coverage_rate} m² per litre**.\n\n"
        f"Calculate the **reciprocal rate** (the volume of paint required to cover **1 m²** of wall area), rounded to 3 decimal places."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• The reciprocal rate inverts the relationship from $\\text{{area per unit volume}}$ to $\\text{{volume per unit area}}$:\n"
        f"  $$\\text{{Rate per m}}^2 = \\frac{{1}}{{\\text{{Coverage Rate}}}} = \\frac{{1}}{{{coverage_rate}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\frac{{1}}{{{coverage_rate}}} = {1 / coverage_rate:.4f} \\approx {_fmt(litres_per_m2, 3)}\\text{{ L/m}}^2$.\n"
        f"✓ **[1 Mark: Method – calculating reciprocal 1 divided by coverage rate]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct unit rate with units]**"
    )
    return _make_q(
        subskill="num_op_reciprocal_unit_rate",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 1 ÷ coverage rate", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide 1 by {coverage_rate}.",
            "tier_2": f"1 ÷ {coverage_rate} = {1/coverage_rate:.4f}.",
            "tier_3": f"Rate per m² = {ans_str}."
        },
        r=r
    )

def _gen_num_op_estimation_mental_rounding_check(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    exact_price = round(r.choice([49.50, 48.90, 51.20]), 2)
    quantity = r.choice([19, 21, 29])
    rounded_price = round(exact_price / 10) * 10
    rounded_qty = round(quantity / 10) * 10
    estimated_total = int(rounded_price * rounded_qty)
    ans_str = f"R {estimated_total:,}".replace(",", " ")

    prompt = (
        f"{name} intends to buy **{quantity} hardware brackets** priced at **{_fmt_curr(exact_price)} each**.\n\n"
        f"Before tapping a debit card, {name} performs a quick mental estimation by rounding the price to the nearest **R 10** and the quantity to the nearest **10 units**.\n\n"
        f"Calculate {name}'s **mental estimated total**."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Mental estimation uses rounded numbers to establish a reasonable expected total and prevent overcharging:\n"
        f"  - Round {_fmt_curr(exact_price)} to the nearest R 10 $\\to$ {_fmt_curr(rounded_price)}.\n"
        f"  - Round {quantity} to the nearest 10 $\\to$ {rounded_qty}.\n"
        f"  $$\\text{{Estimated Total}} = {_fmt_curr(rounded_price)} \\times {rounded_qty}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• ${rounded_price} \\times {rounded_qty} = {estimated_total}$.\n"
        f"✓ **[1 Mark: Method – rounding price and quantity to nearest tens and multiplying]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct mental estimate in Rands]**"
    )
    custom_opts = [
        ans_str,
        f"R {exact_price * quantity:,.2f}".replace(",", " ").replace(".", ","),
        f"R {estimated_total + 200:,}".replace(",", " "),
        f"R {estimated_total - 200:,}".replace(",", " ")
    ]
    return _make_q(
        subskill="num_op_estimation_mental_rounding_check",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – estimated price × estimated quantity", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Round {_fmt_curr(exact_price)} to {_fmt_curr(rounded_price)} and {quantity} to {rounded_qty}.",
            "tier_2": f"Multiply {rounded_price} × {rounded_qty}.",
            "tier_3": f"Estimated total = {ans_str}."
        },
        options=custom_opts,
        r=r
    )
