"""Estimation techniques, currency strength, and macroeconomic impacts (Subskills 19-27) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Mental estimation of Rand cost using rounded benchmark exchange rate."""
    name = r.choice(SA_NAMES)
    exact_rate = round(r.uniform(18.60, 19.40), 2)
    benchmark_rate = 20.0  # Common South African rule-of-thumb benchmark for USD
    usd_price = r.choice([15, 25, 40, 50, 75, 120])
    est_cost = int(round(usd_price * benchmark_rate))
    ans_str = f"R {_fmt(est_cost)},00"

    prompt = (
        f"While browsing an international airport duty-free catalogue, {name} wants to quickly mentally estimate "
        f"the South African Rand cost of a souvenir priced at {_fmt_curr(usd_price, '$')}.\n"
        f"The actual exchange rate is $1,00 = {_fmt_curr(exact_rate)}, but {name} rounds the rate up to a convenient benchmark of $1,00 ≈ R 20,00.\n"
        f"Calculate {name}'s estimated cost in Rands using this rounded benchmark rate."
    )
    explanation = (
        f"Step 1: Identify the rounded benchmark rate used for estimation:\n"
        f"\\text{{Benchmark rate}} = \\text{{R }} 20,00\\text{{ per Dollar}}. [1 mark]\n"
        f"Step 2: Multiply the dollar price by 20:\n"
        f"\\text{{Estimated Cost}} = {usd_price} \\times 20 = {est_cost}. [1 mark]\n"
        f"Step 3: State the estimated Rand cost:\n"
        f"\\text{{Estimated cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(usd_price * exact_rate, 2)),
        _fmt_curr(round(usd_price * 15.0, 2)),
        _fmt_curr(round(usd_price * 25.0, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_19",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply the dollar price by the rounded benchmark rate of R 20,00.",
        f"Calculate {usd_price} × 20.",
        f"Estimated cost = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Calculating estimation error (difference between estimated and accurate conversion)."""
    name = r.choice(SA_NAMES)
    exact_rate = 18.50
    benchmark_rate = 20.0
    usd_price = r.choice([30, 50, 80, 100, 150])
    est_rand = usd_price * benchmark_rate
    actual_rand = usd_price * exact_rate
    error_rand = round(est_rand - actual_rand, 2)
    ans_str = _fmt_curr(error_rand)

    prompt = (
        f"{name} bought a pair of running shoes overseas for {_fmt_curr(usd_price, '$')}.\n"
        f"Before purchasing, {name} estimated the cost using $1,00 ≈ R 20,00.\n"
        f"However, the credit card was billed using the actual rate of $1,00 = R 18,50.\n"
        f"Calculate the estimation difference (error) in Rands between {name}'s estimate and the actual cost."
    )
    explanation = (
        f"Step 1: Calculate the estimated cost and actual cost:\n"
        f"\\text{{Estimated}} = {usd_price} \\times 20 = {_fmt_curr(est_rand)}\n"
        f"\\text{{Actual}} = {usd_price} \\times 18,50 = {_fmt_curr(actual_rand)}. [1 mark]\n"
        f"Step 2: Subtract actual cost from estimated cost:\n"
        f"\\text{{Difference}} = {est_rand} - {actual_rand} = {error_rand:.2f} [1 mark]\n"
        f"Step 3: State the final estimation difference:\n"
        f"\\text{{Estimation error}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(error_rand * 1.5, 2)),
        _fmt_curr(round(error_rand * 0.5, 2)),
        _fmt_curr(round(usd_price * 1.5, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_20",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate estimated cost and actual cost, then subtract them.",
        f"Estimated: {usd_price} × 20 = {_fmt_curr(est_rand)}. Actual: {usd_price} × 18,50 = {_fmt_curr(actual_rand)}.",
        f"Difference = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Identifying stronger vs weaker currency from standard rate quotation."""
    name = r.choice(SA_NAMES)
    currency_pair = r.choice([
        ("British Pound (GBP)", "£1,00 = R 23,45", "British Pound (GBP)", "Rand (ZAR)"),
        ("Euro (EUR)", "€1,00 = R 20,15", "Euro (EUR)", "Rand (ZAR)"),
        ("US Dollar (USD)", "$1,00 = R 18,75", "US Dollar (USD)", "Rand (ZAR)"),
    ])
    c_name, rate_str, stronger, weaker = currency_pair
    ans_str = stronger

    prompt = (
        f"{name} is studying an international finance report that displays the following exchange rate:\n"
        f"{rate_str}.\n"
        f"According to standard economic definitions, which of the two currencies is the stronger currency?"
    )
    explanation = (
        f"Step 1: State the curriculum definition of currency strength:\n"
        f"A currency is defined as 'stronger' in an exchange pair if one single unit of that currency "
        f"exchanges for more than one unit of the other currency. [1 mark]\n"
        f"Step 2: Evaluate the rate:\n"
        f"Here, 1 unit of {stronger} buys more than 1 unit of {weaker} (over 18–24 Rands). [1 mark]\n"
        f"Step 3: Conclude which currency is stronger:\n"
        f"\\text{{Stronger currency}} = {ans_str}. [1 mark]"
    )
    distractors = [
        weaker,
        "Both currencies have equal strength",
        "Neither currency is stronger without knowing inflation",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_21",
        prompt,
        ans_str,
        options,
        explanation,
        "The currency where 1 unit buys multiple units of the other is the stronger currency.",
        f"Since 1 unit of {c_name} equals several Rands, {c_name} is stronger.",
        f"Stronger currency = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Identifying stronger vs weaker currency when rate is expressed as R 1 = Foreign y."""
    foreign_name = "Mozambican Metical (MZN)"
    rate_str = "R 1,00 = MT 3,45"
    ans_str = "South African Rand (ZAR)"

    prompt = (
        f"A currency conversion table at a regional border post displays the rate:\n"
        f"{rate_str}.\n"
        f"Which of the two currencies is the stronger currency?"
    )
    explanation = (
        f"Step 1: Recall the definition of currency strength:\n"
        f"If 1 unit of Currency A buys more than 1 unit of Currency B, then Currency A is stronger. [1 mark]\n"
        f"Step 2: Apply to this quotation:\n"
        f"1 South African Rand buys 3,45 Mozambican Meticais. Since 1 Rand > 1 Metical, the Rand is stronger. [1 mark]\n"
        f"Step 3: State the answer:\n"
        f"\\text{{Stronger currency}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "Mozambican Metical (MZN)",
        "Both currencies are equal in strength",
        "Cannot be determined without GDP data",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_22",
        prompt,
        ans_str,
        options,
        explanation,
        "Since 1 Rand buys 3,45 Meticais, 1 Rand is worth more than 1 Metical.",
        "The Rand is the stronger currency.",
        f"Answer = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Currency appreciation: Calculate percentage strengthening of the Rand over a period."""
    # Note: Rand strengthening against USD means rate goes down (fewer Rands needed per Dollar)
    # E.g. from R 19,00 to R 17,10
    old_rate = 19.00
    new_rate = round(r.choice([17.10, 17.48, 17.86, 18.05]), 2)
    change = round(old_rate - new_rate, 2)
    pct_change = round((change / old_rate) * 100, 1)
    ans_str = f"{_fmt(pct_change)}%"

    prompt = (
        f"Over a six-month period, positive economic growth caused the South African Rand to strengthen against the US Dollar.\n"
        f"The exchange rate shifted from $1,00 = {_fmt_curr(old_rate)} down to $1,00 = {_fmt_curr(new_rate)}.\n"
        f"Calculate the percentage decrease in the Rand price of a US Dollar (the rate of appreciation).\n"
        f"*(Formula: \\text{{Percentage Change}} = \\frac{{\\text{{Old Rate}} - \\text{{New Rate}}}}{{\\text{{Old Rate}}}} \\times 100\\%. Round to 1 decimal place.)*"
    )
    explanation = (
        f"Step 1: Calculate the change in exchange rate:\n"
        f"\\text{{Decrease}} = {old_rate} - {new_rate} = {change:.2f}\\text{{ Rands per Dollar}}. [1 mark]\n"
        f"Step 2: Divide by the original rate and multiply by 100%:\n"
        f"\\text{{Percentage Change}} = \\frac{{{change:.2f}}}{{{old_rate}}} \\times 100\\% [1 mark]\n"
        f"Step 3: State the final percentage:\n"
        f"\\text{{Appreciation rate}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round((change / new_rate) * 100, 1))}%",
        f"{_fmt(round(pct_change * 1.5, 1))}%",
        f"{_fmt(round(pct_change * 0.5, 1))}%",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_23",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract new rate from old rate, divide by old rate, and multiply by 100.",
        f"Change = {old_rate} - {new_rate} = {change:.2f}. ({change:.2f} ÷ {old_rate}) × 100.",
        f"Percentage = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Currency depreciation: Calculate percentage weakening of the Rand over a period."""
    old_rate = 17.50
    new_rate = round(r.choice([18.90, 19.25, 19.60, 20.30]), 2)
    change = round(new_rate - old_rate, 2)
    pct_deprec = round((change / old_rate) * 100, 1)
    ans_str = f"{_fmt(pct_deprec)}%"

    prompt = (
        f"During an international market crisis, the South African Rand weakened against the Euro.\n"
        f"The exchange rate increased from €1,00 = {_fmt_curr(old_rate)} to €1,00 = {_fmt_curr(new_rate)}.\n"
        f"Calculate the percentage depreciation of the Rand against the Euro.\n"
        f"*(Formula: \\text{{Percentage Change}} = \\frac{{\\text{{New Rate}} - \\text{{Old Rate}}}}{{\\text{{Old Rate}}}} \\times 100\\%. Round to 1 decimal place.)*"
    )
    explanation = (
        f"Step 1: Calculate the increase in the exchange rate:\n"
        f"\\text{{Increase}} = {new_rate} - {old_rate} = {change:.2f}\\text{{ Rands per Euro}}. [1 mark]\n"
        f"Step 2: Divide the change by the original rate and multiply by 100%:\n"
        f"\\text{{Percentage Depreciation}} = \\frac{{{change:.2f}}}{{{old_rate}}} \\times 100\\% [1 mark]\n"
        f"Step 3: State the resulting percentage:\n"
        f"\\text{{Depreciation}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round((change / new_rate) * 100, 1))}%",
        f"{_fmt(round(pct_deprec + 3.0, 1))}%",
        f"{_fmt(round(pct_deprec - 2.5, 1))}%",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_24",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate the increase, divide by the initial rate, and multiply by 100.",
        f"Increase = {new_rate} - {old_rate} = {change:.2f}. ({change:.2f} ÷ {old_rate}) × 100.",
        f"Percentage depreciation = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Impact of currency depreciation on the Rand cost of an imported barrel of crude oil."""
    barrel_usd = 80.0
    rate_1 = 17.50
    rate_2 = 19.20
    cost_1 = round(barrel_usd * rate_1, 2)
    cost_2 = round(barrel_usd * rate_2, 2)
    diff = round(cost_2 - cost_1, 2)
    ans_str = _fmt_curr(diff)

    prompt = (
        f"Crude oil is priced globally in US Dollars at $ {_fmt(barrel_usd)} per barrel.\n"
        f"When the exchange rate is $1,00 = {_fmt_curr(rate_1)}, calculate the cost in Rands.\n"
        f"If the Rand weakens to $1,00 = {_fmt_curr(rate_2)}, by how much does the Rand price of one barrel of crude oil increase?"
    )
    explanation = (
        f"Step 1: Calculate the barrel cost at both exchange rates:\n"
        f"\\text{{Cost 1}} = 80 \\times 17,50 = {_fmt_curr(cost_1)}\n"
        f"\\text{{Cost 2}} = 80 \\times 19,20 = {_fmt_curr(cost_2)}. [1 mark]\n"
        f"Step 2: Subtract the original cost from the new cost:\n"
        f"\\text{{Increase}} = {cost_2} - {cost_1} = {diff:.2f} [1 mark]\n"
        f"Step 3: State the final increase in Rands:\n"
        f"\\text{{Price increase}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(cost_1),
        _fmt_curr(cost_2),
        _fmt_curr(round(diff * 1.5, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_25",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply the barrel price by both rates and find the difference.",
        f"Cost at {rate_1} = {_fmt_curr(cost_1)}. Cost at {rate_2} = {_fmt_curr(cost_2)}.",
        f"Increase = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Impact of currency depreciation on a South African exporter's Rand revenue."""
    name = r.choice(SA_NAMES)
    export_boxes = 5000
    price_per_box_eur = 12.0  # Citrus export
    rate_1 = 19.00
    rate_2 = 21.00

    total_eur = export_boxes * price_per_box_eur
    rev_1 = total_eur * rate_1
    rev_2 = total_eur * rate_2
    gain = round(rev_2 - rev_1, 2)
    ans_str = _fmt_curr(gain)

    prompt = (
        f"{name}'s citrus export farm in the Limpopo Valley exports {export_boxes:,} boxes of oranges to the European Union "
        f"at a fixed contractual price of € {_fmt(price_per_box_eur)} per box.\n"
        f"Originally, the farm budgeted revenue at an exchange rate of €1,00 = {_fmt_curr(rate_1)}.\n"
        f"By harvest shipment date, the Rand weakened to €1,00 = {_fmt_curr(rate_2)}.\n"
        f"Calculate the additional revenue in South African Rands (ZAR) gained by the farm due to the weakening of the Rand."
    )
    explanation = (
        f"Step 1: Calculate total contract value in Euros:\n"
        f"\\text{{Total Euros}} = {export_boxes:,} \\times 12 = {total_eur:,}\\text{{ EUR}}. [1 mark]\n"
        f"Step 2: Calculate revenue in Rands at both exchange rates:\n"
        f"\\text{{Revenue 1}} = {total_eur:,} \\times 19,00 = {_fmt_curr(rev_1)}\n"
        f"\\text{{Revenue 2}} = {total_eur:,} \\times 21,00 = {_fmt_curr(rev_2)} [1 mark]\n"
        f"Step 3: Subtract to determine the extra revenue gained:\n"
        f"\\text{{Gain}} = {rev_2:,.0f} - {rev_1:,.0f} = {gain:.2f} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(gain / 10, 2)),
        _fmt_curr(round(gain * 1.25, 2)),
        _fmt_curr(round(total_eur * (rate_2 - rate_1), 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_26",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate total Euros, then multiply by the rate difference (21 - 19 = R 2).",
        f"Total EUR = {total_eur:,}. Extra Rands = {total_eur:,} × 2,00.",
        f"Additional revenue = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Evaluating macroeconomic statements on strong vs weak Rand winners and losers."""
    statements = [
        (
            "A weaker South African Rand makes imported petroleum and electronics more expensive for local consumers.",
            "True",
            "When the Rand is weak, importers need more Rands to buy each US Dollar needed to pay foreign suppliers, increasing domestic retail prices."
        ),
        (
            "A weaker South African Rand makes South African goods cheaper and more attractive for foreign buyers.",
            "True",
            "Foreign buyers need fewer units of their foreign currency to purchase South African products, boosting local export competitiveness."
        ),
        (
            "A stronger South African Rand is always beneficial for South African fruit and mining exporters.",
            "False",
            "A stronger Rand reduces the Rand revenue exporters receive when converting their foreign earnings back into local currency."
        ),
        (
            "A stronger South African Rand makes overseas holidays cheaper for South African tourists.",
            "True",
            "With a stronger Rand, South African tourists receive more foreign currency for each Rand exchanged, lowering travel costs."
        ),
    ]
    stmt, correctness, reason = r.choice(statements)
    ans_str = correctness

    prompt = (
        f"Consider the following macroeconomic statement regarding exchange rates:\n"
        f"\"{stmt}\"\n\n"
        f"Is this statement True or False according to economic principles taught in Mathematical Literacy?"
    )
    explanation = (
        f"Step 1: Analyse the mechanism described in the statement. [1 mark]\n"
        f"Step 2: Reason: {reason} [1 mark]\n"
        f"Step 3: Conclude whether the statement is True or False:\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "False" if correctness == "True" else "True",
        "Undetermined without knowing prime interest rates",
        "Applies only to government bonds",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_27",
        prompt,
        ans_str,
        options,
        explanation,
        "Consider how exchange rate shifts impact the purchasing power of exporters, importers, and tourists.",
        reason,
        f"Answer = {ans_str}.",
        r,
        difficulty="medium",
    )
