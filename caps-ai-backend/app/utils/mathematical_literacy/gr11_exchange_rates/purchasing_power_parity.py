"""Purchasing Power Parity (PPP), the Big Mac Index, and relative buying power (Subskills 28-36) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Compare retail prices of an identical commodity (e.g., smartphone) in SA and USA in ZAR."""
    name = r.choice(SA_NAMES)
    rate = 18.50  # $1 = R 18,50
    us_price_usd = 799.0
    sa_price_zar = 16999.0
    us_price_zar = round(us_price_usd * rate, 2)
    diff = round(sa_price_zar - us_price_zar, 2)
    ans_str = _fmt_curr(diff)

    prompt = (
        f"{name} is deciding whether to buy a new smartphone locally in South Africa or import it from the USA.\n"
        f"• Price in South Africa: {_fmt_curr(sa_price_zar)}\n"
        f"• Price in the USA: {_fmt_curr(us_price_usd, '$')}\n\n"
        f"Using an exchange rate of $1,00 = {_fmt_curr(rate)}, determine how much more expensive the smartphone "
        f"is in South Africa compared to its US price in Rands (excluding import duties)."
    )
    explanation = (
        f"Step 1: Convert the US Dollar price to South African Rands:\n"
        f"\\text{{US Price in ZAR}} = 799 \\times 18,50 = {_fmt_curr(us_price_zar)}. [1 mark]\n"
        f"Step 2: Subtract the converted US price from the South African price:\n"
        f"\\text{{Price difference}} = {sa_price_zar} - {us_price_zar} = {diff:.2f} [1 mark]\n"
        f"Step 3: State the final difference:\n"
        f"\\text{{Difference}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(us_price_zar),
        _fmt_curr(round(diff * 1.25, 2)),
        _fmt_curr(round(diff - 500, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_28",
        prompt,
        ans_str,
        options,
        explanation,
        "Convert the US price to Rands (multiply by 18,50), then subtract from the SA price.",
        f"US price in Rands = 799 × 18,50 = {_fmt_curr(us_price_zar)}. Difference = {sa_price_zar} - {_fmt(us_price_zar)}.",
        f"Difference = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Big Mac Index: Calculating implied purchasing power parity (PPP) rate (Price_SA ÷ Price_US)."""
    sa_price = 49.50  # Rand
    us_price = 5.50   # Dollar
    implied_rate = round(sa_price / us_price, 2)
    ans_str = f"R {_fmt(implied_rate)} : $1,00"

    prompt = (
        f"The 'Big Mac Index' is an informal economic indicator used to compare the purchasing power of different currencies.\n"
        f"Suppose a Big Mac burger costs R 49,50 in South Africa and $ 5,50 in the United States.\n"
        f"Calculate the implied Purchasing Power Parity (PPP) exchange rate (in Rands per Dollar) based on the price of the burger.\n"
        f"*(Formula: \\text{{Implied Rate}} = \\text{{Price in SA}} \\div \\text{{Price in USA}}.)*"
    )
    explanation = (
        f"Step 1: Set up the Big Mac PPP equation:\n"
        f"\\text{{Implied PPP Rate}} = \\frac{{\\text{{Price in Rands}}}}{{\\text{{Price in Dollars}}}}. [1 mark]\n"
        f"Step 2: Divide the South African burger price by the US burger price:\n"
        f"{sa_price} \\div {us_price} = {implied_rate:.2f} [1 mark]\n"
        f"Step 3: Express as an exchange rate quote per 1 US Dollar:\n"
        f"\\text{{Implied PPP rate}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"R {_fmt(round(us_price / sa_price, 4))} : $1,00",
        f"R {_fmt(round(implied_rate * 1.5, 2))} : $1,00",
        f"R {_fmt(round(implied_rate - 2.0, 2))} : $1,00",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_29",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide the price in Rands by the price in Dollars.",
        f"Calculate 49,50 ÷ 5,50.",
        f"Implied PPP rate = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Big Mac Index: Evaluating whether the Rand is undervalued or overvalued against the US Dollar."""
    implied_ppp = 9.00   # Based on Big Mac burger prices: R 9,00 : $1,00
    actual_market = 18.00  # Market exchange rate: R 18,00 : $1,00
    # Because actual market rate (18.00) > implied PPP (9.00), the Rand is undervalued against the Dollar.
    # Calculation: (9.00 - 18.00) / 18.00 = -50%
    valuation_pct = round(((implied_ppp - actual_market) / actual_market) * 100, 1)
    ans_str = f"Undervalued by {abs(valuation_pct):.0f}%"

    prompt = (
        f"According to the Big Mac Index:\n"
        f"• Implied PPP exchange rate: $1,00 = R 9,00\n"
        f"• Actual market exchange rate: $1,00 = R 18,00\n\n"
        f"Using the valuation formula:\n"
        f"\\text{{Valuation}} = \\frac{{\\text{{Implied Rate}} - \\text{{Market Rate}}}}{{\\text{{Market Rate}}}} \\times 100\\%,\n"
        f"determine whether the South African Rand is undervalued or overvalued against the US Dollar, and by what percentage."
    )
    explanation = (
        f"Step 1: Substitute the values into the valuation formula:\n"
        f"\\text{{Valuation}} = \\frac{{9,00 - 18,00}}{{18,00}} \\times 100\\%. [1 mark]\n"
        f"Step 2: Compute the numerator and fraction:\n"
        f"\\frac{{-9,00}}{{18,00}} \\times 100\\% = -0,50 \\times 100\\% = -50\\%. [1 mark]\n"
        f"Step 3: Interpret the negative sign:\n"
        f"A negative valuation means the Rand is undervalued by 50% relative to purchasing power parity:\n"
        f"\\text{{Result}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Overvalued by {abs(valuation_pct):.0f}%",
        "Undervalued by 25%",
        "Overvalued by 50%",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_30",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate (Implied - Market) ÷ Market × 100. A negative result means undervalued.",
        f"(9 - 18) ÷ 18 × 100 = -50%.",
        f"Conclusion = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Relative cost of living: Price of an item as a percentage of monthly salary in SA vs UK."""
    sa_salary = 16000.0  # Rands
    sa_tv_price = 6400.0  # Rands (40% of salary)
    uk_salary = 2400.0   # Pounds
    uk_tv_price = 480.0  # Pounds (20% of salary)

    sa_pct = round((sa_tv_price / sa_salary) * 100, 1)
    uk_pct = round((uk_tv_price / uk_salary) * 100, 1)
    ans_str = f"South Africa ({_fmt(sa_pct)}% vs {_fmt(uk_pct)}%)"

    prompt = (
        f"To compare the true affordability ('buying power') of consumer goods, consider two teachers:\n"
        f"• South African teacher: Earns {_fmt_curr(sa_salary)} per month and buys a television for {_fmt_curr(sa_tv_price)}.\n"
        f"• British teacher: Earns {_fmt_curr(uk_salary, '£')} per month and buys the same television for {_fmt_curr(uk_tv_price, '£')}.\n\n"
        f"In which country does the television require a greater percentage of the teacher's monthly salary?"
    )
    explanation = (
        f"Step 1: Calculate the TV price as a percentage of monthly salary in South Africa:\n"
        f"\\text{{SA Percentage}} = \\frac{{{sa_tv_price}}}{{{sa_salary}}} \\times 100\\% = {_fmt(sa_pct)}\\%. [1 mark]\n"
        f"Step 2: Calculate the TV price as a percentage of monthly salary in the UK:\n"
        f"\\text{{UK Percentage}} = \\frac{{{uk_tv_price}}}{{{uk_salary}}} \\times 100\\% = {_fmt(uk_pct)}\\%. [1 mark]\n"
        f"Step 3: Compare percentages and draw conclusion:\n"
        f"Since {_fmt(sa_pct)}\\% > {_fmt(uk_pct)}\\%, the television is relatively more expensive in South Africa:\n"
        f"\\text{{Result}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"United Kingdom ({_fmt(uk_pct)}% vs {_fmt(sa_pct)}%)",
        "Both countries require the exact same percentage (30%)",
        "Cannot be compared without converting both to US Dollars",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_31",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide each price by its respective country's salary and multiply by 100%.",
        f"SA: ({sa_tv_price} ÷ {sa_salary}) × 100 = {_fmt(sa_pct)}%. UK: ({uk_tv_price} ÷ {uk_salary}) × 100 = {_fmt(uk_pct)}%.",
        f"Answer = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Relative cost of living: Price of an item as a percentage of monthly salary in SA vs Germany (EUR)."""
    sa_salary = 18000.0  # Rands
    sa_laptop = 10800.0  # Rands (60% of salary)
    de_salary = 2800.0   # Euros
    de_laptop = 840.0    # Euros (30% of salary)

    sa_pct = round((sa_laptop / sa_salary) * 100, 1)
    de_pct = round((de_laptop / de_salary) * 100, 1)
    diff_pct = round(sa_pct - de_pct, 1)
    ans_str = f"{_fmt(diff_pct)} percentage points higher in South Africa"

    prompt = (
        f"A laptop is priced at {_fmt_curr(sa_laptop)} in South Africa and {_fmt_curr(de_laptop, '€')} in Germany.\n"
        f"• Average South African monthly income: {_fmt_curr(sa_salary)}\n"
        f"• Average German monthly income: {_fmt_curr(de_salary, '€')}\n\n"
        f"Calculate the difference in percentage points between the income proportions required to buy the laptop."
    )
    explanation = (
        f"Step 1: Calculate the percentage of income in South Africa:\n"
        f"\\text{{SA}} = \\frac{{{sa_laptop}}}{{{sa_salary}}} \\times 100\\% = {_fmt(sa_pct)}\\%. [1 mark]\n"
        f"Step 2: Calculate the percentage of income in Germany:\n"
        f"\\text{{Germany}} = \\frac{{{de_laptop}}}{{{de_salary}}} \\times 100\\% = {_fmt(de_pct)}\\%. [1 mark]\n"
        f"Step 3: Subtract the percentages:\n"
        f"{_fmt(sa_pct)}\\% - {_fmt(de_pct)}\\% = {_fmt(diff_pct)}\\text{{ percentage points}}.\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(diff_pct)} percentage points higher in Germany",
        f"{_fmt(round(diff_pct * 1.5, 1))} percentage points higher in South Africa",
        f"{_fmt(round(diff_pct - 10, 1))} percentage points higher in South Africa",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_32",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate each percentage of income, then subtract the two percentages.",
        f"SA = {_fmt(sa_pct)}%, Germany = {_fmt(de_pct)}%. Difference = {_fmt(diff_pct)}%.",
        f"Result = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Compare annual university tuition in South Africa vs abroad in Rand equivalents."""
    name = r.choice(SA_NAMES)
    rate_gbp = 23.50  # £1 = R 23,50
    sa_tuition_zar = 65000.0
    uk_tuition_gbp = 14500.0
    uk_tuition_zar = round(uk_tuition_gbp * rate_gbp, 2)
    ans_str = _fmt_curr(uk_tuition_zar)

    prompt = (
        f"{name} is comparing annual university tuition fees for an engineering degree:\n"
        f"• University of Cape Town (South Africa): {_fmt_curr(sa_tuition_zar)} per year\n"
        f"• University of Manchester (United Kingdom): {_fmt_curr(uk_tuition_gbp, '£')} per year\n\n"
        f"If the exchange rate is £1,00 = {_fmt_curr(rate_gbp)}, calculate the UK tuition fee converted into South African Rands."
    )
    explanation = (
        f"Step 1: Set up the currency conversion:\n"
        f"\\text{{ZAR Equivalent}} = \\text{{GBP Tuition}} \\times \\text{{Exchange Rate}}. [1 mark]\n"
        f"Step 2: Multiply {uk_tuition_gbp:,.0f} by 23,50:\n"
        f"{uk_tuition_gbp:,.0f} \\times 23,50 = {uk_tuition_zar:,.2f} [1 mark]\n"
        f"Step 3: State the final converted tuition fee:\n"
        f"\\text{{UK tuition in ZAR}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(uk_tuition_gbp / rate_gbp, 2)),
        _fmt_curr(round(uk_tuition_zar + 50000, 2)),
        _fmt_curr(round(uk_tuition_zar - 50000, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_33",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the UK tuition in pounds by {rate_gbp}.",
        f"Calculate {uk_tuition_gbp:,.0f} × {rate_gbp}.",
        f"Tuition in Rands = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Rental accommodation cost comparison in Johannesburg vs London in ZAR."""
    rate_gbp = 23.50
    jhb_rent_zar = 9500.0   # 1-bedroom flat in Johannesburg
    london_rent_gbp = 1200.0  # 1-bedroom flat in London
    london_rent_zar = round(london_rent_gbp * rate_gbp, 2)
    ratio = round(london_rent_zar / jhb_rent_zar, 1)
    ans_str = f"{_fmt(ratio)} times more expensive"

    prompt = (
        f"A young professional compares the monthly rent for a one-bedroom apartment:\n"
        f"• Johannesburg (Rosebank): {_fmt_curr(jhb_rent_zar)} per month\n"
        f"• London (Zone 3): {_fmt_curr(london_rent_gbp, '£')} per month\n\n"
        f"Using an exchange rate of £1,00 = {_fmt_curr(rate_gbp)}, determine how many times more expensive "
        f"the London rent is in Rand value compared to the Johannesburg rent.\n"
        f"*(Round to 1 decimal place.)*"
    )
    explanation = (
        f"Step 1: Convert the London rent into South African Rands:\n"
        f"\\text{{London in ZAR}} = 1\\,200 \\times 23,50 = {_fmt_curr(london_rent_zar)}. [1 mark]\n"
        f"Step 2: Divide the converted London rent by the Johannesburg rent:\n"
        f"\\text{{Ratio}} = \\frac{{{london_rent_zar}}}{{{jhb_rent_zar}}} = {ratio:.2f} [1 mark]\n"
        f"Step 3: State the final comparative factor:\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(ratio * 1.5, 1))} times more expensive",
        f"{_fmt(round(ratio - 1.0, 1))} times more expensive",
        f"{_fmt(round(jhb_rent_zar / london_rent_gbp, 1))} times more expensive",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_34",
        prompt,
        ans_str,
        options,
        explanation,
        "Convert the London rent to Rands, then divide by the Johannesburg rent.",
        f"London rent = 1 200 × 23,50 = {_fmt_curr(london_rent_zar)}. Ratio = {london_rent_zar} ÷ {jhb_rent_zar}.",
        f"Factor = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Calculate the real purchasing power of a holiday allowance across two destinations."""
    name = r.choice(SA_NAMES)
    total_rand_budget = 15000.0
    # Destination 1: Zimbabwe/Zambia (cost per meal in local equivalent = R 80)
    # Destination 2: London (cost per meal = £15, at £1 = R 23,50 -> R 352,50)
    meal_sa_zar = 100.0
    meal_london_gbp = 15.0
    rate_gbp = 23.50
    meal_london_zar = round(meal_london_gbp * rate_gbp, 2)

    meals_sa = int(total_rand_budget // meal_sa_zar)
    meals_london = int(total_rand_budget // meal_london_zar)
    diff_meals = meals_sa - meals_london
    ans_str = f"{diff_meals} fewer meals in London"

    prompt = (
        f"{name} has a food budget of {_fmt_curr(total_rand_budget)} for an upcoming holiday and considers two destinations:\n"
        f"• Local South African coast: Average restaurant meal costs {_fmt_curr(meal_sa_zar)}.\n"
        f"• London (United Kingdom): Average restaurant meal costs {_fmt_curr(meal_london_gbp, '£')} (with exchange rate £1,00 = {_fmt_curr(rate_gbp)}).\n\n"
        f"Calculate how many fewer restaurant meals {name}'s budget will buy in London compared to South Africa."
    )
    explanation = (
        f"Step 1: Calculate meals affordable in South Africa:\n"
        f"\\text{{Meals in SA}} = 15\\,000 \\div 100 = {meals_sa}\\text{{ meals}}. [1 mark]\n"
        f"Step 2: Convert London meal cost to Rands and calculate affordable meals:\n"
        f"\\text{{London meal in ZAR}} = 15 \\times 23,50 = {_fmt_curr(meal_london_zar)}\n"
        f"\\text{{Meals in London}} = 15\\,000 \\div {meal_london_zar:.2f} \\approx {meals_london}\\text{{ meals}}. [1 mark]\n"
        f"Step 3: Subtract meals in London from meals in South Africa:\n"
        f"{meals_sa} - {meals_london} = {diff_meals}\\text{{ meals}}.\n"
        f"\\text{{Purchasing power difference}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{meals_london} fewer meals in London",
        f"{diff_meals + 20} fewer meals in London",
        f"{diff_meals - 15} fewer meals in London",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_35",
        prompt,
        ans_str,
        options,
        explanation,
        "Find number of meals in SA, number of meals in London, and take the difference.",
        f"Meals SA = {meals_sa}. London meal = {_fmt_curr(meal_london_zar)}, meals = {meals_london}.",
        f"Difference = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Analyse the misconception that a weaker currency automatically implies higher domestic prices."""
    prompt = (
        "A student claims: 'Because the Japanese Yen is weaker than the South African Rand (R 1,00 ≈ ¥ 8,00), "
        "goods sold in Japan must automatically be 8 times more expensive for Japanese citizens.'\n\n"
        "Which of the following statements correctly refutes this misconception according to Mathematical Literacy?"
    )
    correct = (
        "False: Exchange rates do not reflect local buying power; Japanese salaries are also paid in Yen and matched to domestic prices."
    )
    distractors = [
        "True: When a currency is weaker, everything in that country is more expensive for everyone.",
        "False: The Japanese Yen is actually stronger because 8 is a larger number than 1.",
        "True: Japanese citizens must convert all their money to Rands before buying food.",
    ]
    options, _ = _build_options(correct, r, [correct] + distractors)
    explanation = (
        "Step 1: Identify the underlying economic principle of purchasing power:\n"
        "Exchange rate units do not dictate domestic affordability. Affordability depends on the ratio of local prices "
        "to local earnings. [1 mark]\n"
        "Step 2: Analyse Japanese incomes:\n"
        "Japanese workers earn hundreds of thousands of Yen per month, so prices denominated in Yen are proportional to domestic earnings. [1 mark]\n"
        "Step 3: Conclude the correct statement:\n"
        f"\\text{{Conclusion}} = {correct}. [1 mark]"
    )
    return _build_question_payload(
        "subskill_36",
        prompt,
        correct,
        options,
        explanation,
        "Consider that local citizens earn their salaries in the local currency.",
        "Affordability is determined by the percentage of local salary required, not the nominal exchange rate number.",
        f"Correct statement = {correct}.",
        r,
        difficulty="medium",
    )
