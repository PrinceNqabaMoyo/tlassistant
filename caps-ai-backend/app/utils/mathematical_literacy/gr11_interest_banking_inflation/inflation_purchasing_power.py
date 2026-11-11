"""Inflation, consumer price index (CPI), and purchasing power erosion (Subskills 45-52) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Predict the future price of a basket of groceries after 1 year of inflation."""
    name = r.choice(SA_NAMES)
    current_cost = r.choice([850, 1200, 1500, 2200, 2800])
    inflation_rate = r.choice([5.0, 5.5, 6.0, 6.5, 7.0])
    price_increase = round(current_cost * (inflation_rate / 100.0), 2)
    future_cost = round(current_cost + price_increase, 2)
    ans_str = _fmt_curr(future_cost)

    prompt = (
        f"{name}'s household spends {_fmt_curr(current_cost)} on a monthly grocery basket.\n"
        f"If the projected annual food inflation rate for the coming year is {_fmt(inflation_rate)}%,\n"
        f"calculate the expected cost of the exact same grocery basket one year later."
    )
    explanation = (
        f"Step 1: Calculate the inflation increase amount:\n"
        f"\\text{{Increase}} = {current_cost} \\times {inflation_rate/100:.3f} = {_fmt_curr(price_increase)}. [1 mark]\n"
        f"Step 2: Add the increase to the original cost:\n"
        f"\\text{{Future Cost}} = {current_cost} + {_fmt(price_increase)} = {future_cost:.2f} [1 mark]\n"
        f"Step 3: State the final projected cost:\n"
        f"\\text{{Projected cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(price_increase),
        _fmt_curr(round(current_cost * 1.15, 2)),
        _fmt_curr(round(future_cost - 50, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_45",
        prompt,
        ans_str,
        options,
        explanation,
        f"Calculate {_fmt(inflation_rate)}% of the current cost and add it to the cost.",
        f"Increase = {current_cost} × {inflation_rate/100}. Future cost = {current_cost} + increase.",
        f"Future cost = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Compounded multi-year price projection under constant annual inflation rate."""
    current_price = 120.0  # e.g. 2 kg chicken pieces
    inflation_rate = 6.0   # 6% per annum
    years = 3
    # A = P(1 + i)^n
    factor = (1.0 + (inflation_rate / 100.0)) ** years
    future_price = round(current_price * factor, 2)
    ans_str = _fmt_curr(future_price)

    prompt = (
        f"A standard food item currently costs {_fmt_curr(current_price)} at the supermarket.\n"
        f"Assuming an average annual inflation rate of {_fmt(inflation_rate)}% compounded each year for {years} consecutive years,\n"
        f"predict the price of this item at the end of {years} years.\n"
        f"*(Formula: A = P(1 + i)^n. Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: State the compound inflation formula:\n"
        f"A = P(1 + i)^n, \\text{{ where }} P = {current_price}, i = 0,06, n = {years}. [1 mark]\n"
        f"Step 2: Substitute values:\n"
        f"A = {current_price}(1 + 0,06)^3 = {current_price}(1,06)^3 \\approx {current_price} \\times {factor:.6f} [1 mark]\n"
        f"Step 3: State the rounded future price:\n"
        f"\\text{{Future price}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(current_price * (1.0 + 0.06 * years), 2)),  # Simple interest
        _fmt_curr(round(future_price + 15, 2)),
        _fmt_curr(round(future_price - 10, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_46",
        prompt,
        ans_str,
        options,
        explanation,
        f"Calculate {current_price} × (1,06)^3.",
        f"A = {current_price} × (1,06)^3.",
        f"Projected price = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Compounded price projection with variable annual inflation rates across consecutive years."""
    name = r.choice(SA_NAMES)
    base_car_price = 150000.0
    rate_yr1 = 5.0   # 5% in Year 1
    rate_yr2 = 7.5   # 7,5% in Year 2

    price_yr1 = round(base_car_price * (1.0 + rate_yr1 / 100.0), 2)
    price_yr2 = round(price_yr1 * (1.0 + rate_yr2 / 100.0), 2)
    ans_str = _fmt_curr(price_yr2)

    prompt = (
        f"A popular entry-level motor vehicle is priced at {_fmt_curr(base_car_price)} in 2024.\n"
        f"The automotive industry forecasts that the car's price will increase due to inflation by:\n"
        f"• {_fmt(rate_yr1)}% during 2025\n"
        f"• {_fmt(rate_yr2)}% during 2026\n\n"
        f"Calculate the projected price of a new model of the car at the end of 2026."
    )
    explanation = (
        f"Step 1: Calculate the price at the end of Year 1 (2025):\n"
        f"\\text{{Price 2025}} = 150\\,000 + (150\\,000 \\times 0,05) = {_fmt_curr(price_yr1)}. [1 mark]\n"
        f"Step 2: Calculate the price at the end of Year 2 (2026) using the Year 1 price:\n"
        f"\\text{{Price 2026}} = {_fmt(price_yr1)} + ({_fmt(price_yr1)} \\times 0,075) = {price_yr2:,.2f} [1 mark]\n"
        f"Step 3: State the final projected price:\n"
        f"\\text{{Projected car price}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(base_car_price * (1.0 + (rate_yr1 + rate_yr2) / 100.0), 2)),  # Added percentage directly
        _fmt_curr(round(price_yr2 + 5000, 2)),
        _fmt_curr(round(price_yr1, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_47",
        prompt,
        ans_str,
        options,
        explanation,
        "Increase by 5% first to find the 2025 price, then increase that new price by 7,5%.",
        f"2025: 150 000 × 1,05 = {_fmt_curr(price_yr1)}. 2026: {_fmt(price_yr1)} × 1,075.",
        f"Final price = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Calculate the historical rate of inflation between two years."""
    old_price = 160.0
    new_price = 176.0
    increase = new_price - old_price  # 16
    inflation_pct = round((increase / old_price) * 100, 1)
    ans_str = f"{_fmt(inflation_pct)}%"

    prompt = (
        f"A 10 kg bag of maize meal cost {_fmt_curr(old_price)} in January 2023 and {_fmt_curr(new_price)} in January 2024.\n"
        f"Calculate the annual rate of inflation for this product over the one-year period.\n"
        f"*(Formula: \\text{{Inflation Rate}} = \\frac{{\\text{{New Price}} - \\text{{Old Price}}}}{{\\text{{Old Price}}}} \\times 100\\%.)*"
    )
    explanation = (
        f"Step 1: Calculate the price increase:\n"
        f"\\text{{Increase}} = 176 - 160 = {_fmt_curr(increase)}. [1 mark]\n"
        f"Step 2: Divide the increase by the original price and multiply by 100%:\n"
        f"\\text{{Rate}} = \\frac{{{increase}}}{{160}} \\times 100\\% = {increase/160:.2f} \\times 100\\% [1 mark]\n"
        f"Step 3: State the final inflation rate:\n"
        f"\\text{{Inflation rate}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round((increase / new_price) * 100, 1))}%",
        f"{_fmt(round(inflation_pct * 1.5, 1))}%",
        f"{_fmt(round(inflation_pct - 2.5, 1))}%",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_48",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract the old price from the new price, divide by the old price, and multiply by 100.",
        f"(176 - 160) ÷ 160 × 100 = {increase} ÷ 160 × 100.",
        f"Inflation rate = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Real wage growth vs nominal wage growth (wage increase % minus inflation %)."""
    name = r.choice(SA_NAMES)
    wage_increase_pct = 5.0
    cpi_inflation_pct = 6.8
    real_growth_pct = round(wage_increase_pct - cpi_inflation_pct, 1)
    ans_str = f"Decreased by {abs(real_growth_pct):.1f}%"

    prompt = (
        f"{name} received a {_fmt(wage_increase_pct)}% annual salary increase at work.\n"
        f"However, Statistics South Africa announced an annual consumer inflation (CPI) rate of {_fmt(cpi_inflation_pct)}% for the same year.\n"
        f"Determine how {name}'s real purchasing power has changed, and by what percentage.\n"
        f"*(Formula: \\text{{Real Change}} = \\text{{Wage Increase \\%}} - \\text{{Inflation \\%}}.)*"
    )
    explanation = (
        f"Step 1: Set up the real purchasing power formula:\n"
        f"\\text{{Real Change}} = {_fmt(wage_increase_pct)}\\% - {_fmt(cpi_inflation_pct)}\\%. [1 mark]\n"
        f"Step 2: Subtract the inflation rate from the wage increase:\n"
        f"{_fmt(wage_increase_pct)} - {_fmt(cpi_inflation_pct)} = {real_growth_pct:.1f}\\%. [1 mark]\n"
        f"Step 3: Interpret the negative sign:\n"
        f"Because the result is negative, real buying power decreased:\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Increased by {abs(real_growth_pct):.1f}%",
        f"Increased by {_fmt(wage_increase_pct)}%",
        "Remained unchanged",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_49",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract inflation from the wage increase. If inflation is higher, real purchasing power drops.",
        f"5,0% - 6,8% = -1,8%.",
        f"Outcome = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Consumer Price Index (CPI) basket analysis: identifying the item with highest inflation increase."""
    table_data = [
        ("White Bread (700 g)", 15.00, 18.00),     # +20%
        ("Sunflower Oil (2 L)", 75.00, 84.00),     # +12%
        ("Full Cream Milk (2 L)", 32.00, 36.80),   # +15%
        ("Eggs (tray of 30)", 60.00, 69.00),       # +15%
    ]
    # White bread has (18 - 15) / 15 = 20%
    ans_str = "White Bread (700 g) with a 20,0% increase"

    prompt = (
        f"Consider the table below showing prices for selected grocery items between 2023 and 2024:\n\n"
        f"| Item | 2023 Price | 2024 Price |\n"
        f"| :--- | :--- | :--- |\n"
        f"| White Bread (700 g) | R 15,00 | R 18,00 |\n"
        f"| Sunflower Oil (2 L) | R 75,00 | R 84,00 |\n"
        f"| Full Cream Milk (2 L) | R 32,00 | R 36,80 |\n"
        f"| Eggs (tray of 30) | R 60,00 | R 69,00 |\n\n"
        f"Which grocery item experienced the highest percentage rate of price inflation?"
    )
    explanation = (
        f"Step 1: Calculate the percentage inflation for each item:\n"
        f"- Bread: (18 - 15) ÷ 15 × 100 = 20,0%\n"
        f"- Oil: (84 - 75) ÷ 75 × 100 = 12,0%\n"
        f"- Milk: (36,80 - 32) ÷ 32 × 100 = 15,0%\n"
        f"- Eggs: (69 - 60) ÷ 60 × 100 = 15,0%. [1 mark]\n"
        f"Step 2: Compare the percentage increases: 20,0% is the highest. [1 mark]\n"
        f"Step 3: State the item with the highest rate:\n"
        f"\\text{{Item}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "Sunflower Oil (2 L) with a 12,0% increase",
        "Full Cream Milk (2 L) with a 15,0% increase",
        "Eggs (tray of 30) with a 15,0% increase",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_50",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the percentage increase for each item: (New - Old) ÷ Old × 100.",
        "Bread has (3 ÷ 15) × 100 = 20%, which is higher than Oil (12%) and Milk/Eggs (15%).",
        f"Highest inflation = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Purchasing power erosion: How much less fuel can be bought with fixed R 1 000 after inflation."""
    name = r.choice(SA_NAMES)
    old_petrol_price = 20.0  # R 20/litre
    new_petrol_price = 25.0  # R 25/litre
    fixed_budget = 1000.0

    litres_old = fixed_budget / old_petrol_price  # 50 L
    litres_new = fixed_budget / new_petrol_price  # 40 L
    litres_lost = round(litres_old - litres_new, 1)
    ans_str = f"{_fmt(litres_lost)} litres less"

    prompt = (
        f"{name} has a fixed monthly petrol budget of {_fmt_curr(fixed_budget)}.\n"
        f"In Year 1, petrol cost {_fmt_curr(old_petrol_price)} per litre.\n"
        f"In Year 2, inflation pushed the petrol price up to {_fmt_curr(new_petrol_price)} per litre.\n\n"
        f"Calculate how many fewer litres of petrol {name} can purchase in Year 2 with the exact same R 1 000 budget."
    )
    explanation = (
        f"Step 1: Calculate litres bought in Year 1:\n"
        f"\\text{{Litres Year 1}} = 1\\,000 \\div 20,00 = {litres_old:.0f}\\text{{ L}}. [1 mark]\n"
        f"Step 2: Calculate litres bought in Year 2:\n"
        f"\\text{{Litres Year 2}} = 1\\,000 \\div 25,00 = {litres_new:.0f}\\text{{ L}}. [1 mark]\n"
        f"Step 3: Subtract Year 2 volume from Year 1 volume:\n"
        f"{litres_old:.0f} - {litres_new:.0f} = {litres_lost:.0f}\\text{{ litres}}.\n"
        f"\\text{{Purchasing power erosion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{litres_new:.0f} litres less",
        f"{_fmt(litres_lost + 5)} litres less",
        f"{_fmt(litres_lost - 2)} litres less",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_51",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide R 1 000 by both prices and subtract the results.",
        f"Year 1 = 1 000 ÷ 20 = 50 L. Year 2 = 1 000 ÷ 25 = 40 L. Difference = 10 L.",
        f"Volume lost = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Depreciating asset (motor vehicle) vs inflation: resale value reduction vs rising replacement cost."""
    initial_car_cost = 180000.0
    deprec_rate = 15.0  # 15% depreciation per year
    inflation_rate = 6.0  # 6% inflation per year

    # After 1 year:
    resale_val = initial_car_cost * (1.0 - deprec_rate / 100.0)  # 153 000
    new_car_cost = initial_car_cost * (1.0 + inflation_rate / 100.0)  # 190 800
    gap = round(new_car_cost - resale_val, 2)
    ans_str = _fmt_curr(gap)

    prompt = (
        f"A motorist bought a new car for {_fmt_curr(initial_car_cost)}.\n"
        f"Over the first year:\n"
        f"• The market resale value of the motorist's used car depreciated by {_fmt(deprec_rate)}%.\n"
        f"• The cost of a brand new replacement model increased by {_fmt(inflation_rate)}% due to inflation.\n\n"
        f"Calculate the difference (gap) between the price of a new car and the trade-in value of the used car after 1 year."
    )
    explanation = (
        f"Step 1: Calculate the depreciated resale trade-in value of the used car:\n"
        f"\\text{{Resale}} = 180\\,000 - (180\\,000 \\times 0,15) = 180\\,000 - 27\\,000 = {_fmt_curr(resale_val)}. [1 mark]\n"
        f"Step 2: Calculate the inflated price of a brand new replacement car:\n"
        f"\\text{{New Car}} = 180\\,000 + (180\\,000 \\times 0,06) = 180\\,000 + 10\\,800 = {_fmt_curr(new_car_cost)}. [1 mark]\n"
        f"Step 3: Subtract the resale value from the new car price:\n"
        f"\\text{{Gap}} = {_fmt(new_car_cost)} - {_fmt(resale_val)} = {gap:,.2f} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(resale_val),
        _fmt_curr(new_car_cost),
        _fmt_curr(round(gap - 10000, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_52",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the 15% depreciated value of the old car and the 6% inflated price of the new car, then find the gap.",
        f"Used = {_fmt_curr(resale_val)}. New = {_fmt_curr(new_car_cost)}. Gap = {_fmt_curr(gap)}.",
        f"Upgrade gap = {ans_str}.",
        r,
        difficulty="hard",
    )
