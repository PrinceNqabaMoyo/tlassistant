"""Subskills 47 to 52: Purchasing Power Parity (PPP), Inflation, and Economic Impacts (LB pages 240, 249)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def gen_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Exrate 47: Big Mac Index: Calculating implied PPP exchange rate."""
    sa_price = round(r.uniform(42.50, 49.50), 2)
    us_price = round(r.uniform(5.15, 5.85), 2)

    implied_rate = round(sa_price / us_price, 4)

    prompt = (
        f"Under the Purchasing Power Parity (PPP) theory, an identical good should cost the same in different countries "
        f"when prices are converted at the implied exchange rate.\n\n"
        f"• Price of a Big Mac in South Africa: {_fmt_curr(sa_price)}\n"
        f"• Price of a Big Mac in the United States: ${us_price:.2f}\n\n"
        f"Calculate the implied PPP exchange rate (in Rands per US Dollar), rounded to two decimal places."
    )
    correct_ans = f"1 USD = R {_fmt(round(implied_rate, 2), 2)}"
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Implied PPP Rate = South African Price ÷ US Price\n"
        f"Step 2: Substitution [1 Mark]: {sa_price:.2f} ÷ {us_price:.2f} = {implied_rate:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Divide the South African price (in Rands) by the foreign price."
    t2 = f"{sa_price:.2f} ÷ {us_price:.2f} = {implied_rate:.2f}."
    t3 = f"Implied rate = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_47", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Exrate 48: Big Mac Index: Determining whether the Rand is undervalued or overvalued."""
    implied_rate = 8.50
    actual_rate = 18.50

    prompt = (
        f"A Big Mac costs R 42,50 in South Africa and $5,00 in the United States.\n"
        f"• Implied PPP Exchange Rate: 1 USD = R 8,50 (42,50 ÷ 5,00)\n"
        f"• Actual Market Exchange Rate: 1 USD = R 18,50\n\n"
        f"Comparing the implied PPP rate to the actual market exchange rate, is the South African Rand "
        f"undervalued or overvalued against the US Dollar?"
    )
    correct_ans = "Undervalued (the actual market rate gives far fewer Dollars per Rand than purchasing power suggests)"
    custom_opts = [
        correct_ans,
        "Overvalued (the Rand is trading at a premium compared to its real domestic purchasing power)",
        "At exact Purchasing Power Parity (fair economic equilibrium)",
        "Inconvertible due to statutory currency pegging rules",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Comparison [1 Mark]: The actual market rate (R 18,50) is higher than the PPP rate (R 8,50).\n"
        f"Step 2: Interpretation [1 Mark]: You have to pay R 18,50 in the market for $1, but only R 8,50 worth of goods buys the same basket.\n"
        f"Step 3: Conclusion [1 Mark]: The Rand is undervalued."
    )
    t1 = "When the actual market rate requires more Rands per Dollar than the PPP rate, the Rand is undervalued."
    t2 = "It costs fewer Rands (R 8,50) to buy a burger than the market charges for a dollar (R 18,50)."
    t3 = f"The Rand is {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_48", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Exrate 49: Calculating percentage undervaluation/overvaluation of the Rand."""
    implied_rate = 9.20
    actual_rate = 18.40

    # Formula: (Implied Rate - Actual Rate) / Actual Rate * 100%
    diff = implied_rate - actual_rate
    pct = round((diff / actual_rate) * 100.0, 2)

    prompt = (
        f"The Big Mac Index reports:\n"
        f"• Implied PPP exchange rate: 1 USD = R {_fmt(implied_rate, 2)}\n"
        f"• Actual market exchange rate: 1 USD = R {_fmt(actual_rate, 2)}\n\n"
        f"Calculate the percentage by which the South African Rand is undervalued against the US Dollar, "
        f"using the standard formula:\n"
        f"Percentage = ((Implied Rate - Actual Rate) ÷ Actual Rate) × 100%"
    )
    correct_ans = f"{_fmt(pct, 2)}%"
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: (({implied_rate:.2f} - {actual_rate:.2f}) ÷ {actual_rate:.2f}) × 100%\n"
        f"Step 2: Difference [1 Mark]: ({diff:.2f} ÷ {actual_rate:.2f}) × 100% = {diff / actual_rate * 100.0:.4f}%\n"
        f"Step 3: Solution [1 Mark]: {correct_ans} (negative sign indicates undervaluation)"
    )
    t1 = "Subtract the actual market rate from the implied rate, divide by the actual rate, and multiply by 100."
    t2 = f"({implied_rate:.2f} - {actual_rate:.2f}) ÷ {actual_rate:.2f} = {diff / actual_rate:.4f}."
    t3 = f"Multiply by 100 to get {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_49", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Exrate 50: Currency depreciation: Calculating percentage weakening of Rand against USD."""
    rate_jan = round(r.uniform(17.20, 17.80), 2)
    rate_dec = round(rate_jan + r.uniform(1.40, 2.20), 2)

    diff = rate_dec - rate_jan
    pct_depr = round((diff / rate_jan) * 100.0, 2)

    prompt = (
        f"At the start of the year, the exchange rate was 1 USD = R {_fmt(rate_jan, 2)}.\n"
        f"By the end of the year, the exchange rate moved to 1 USD = R {_fmt(rate_dec, 2)}.\n\n"
        f"Calculate the percentage increase in the Rand price of the US Dollar (the Rand's depreciation), "
        f"rounded to two decimal places."
    )
    correct_ans = f"{_fmt(pct_depr, 2)}%"
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Absolute increase [1 Mark]: {rate_dec:.2f} - {rate_jan:.2f} = R {diff:.2f}\n"
        f"Step 2: Percentage formula [1 Mark]: ({diff:.2f} ÷ {rate_jan:.2f}) × 100% = {diff / rate_jan * 100.0:.4f}%\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Percentage increase = (New Rate - Old Rate) ÷ Old Rate × 100%."
    t2 = f"({rate_dec:.2f} - {rate_jan:.2f}) ÷ {rate_jan:.2f} = {diff:.2f} ÷ {rate_jan:.2f}."
    t3 = f"Percentage depreciation = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_50", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Exrate 51: Impact of Rand depreciation on South African importers."""
    prompt = (
        f"When the South African Rand weakens (depreciates) against major foreign currencies (such as the US Dollar and Euro):\n\n"
        f"What is the direct economic effect on South African businesses that import crude oil, electronics, and vehicle components?"
    )
    correct_ans = "Imported goods become more expensive in Rands, increasing production costs and driving domestic inflation higher"
    custom_opts = [
        correct_ans,
        "Imported goods become significantly cheaper in Rands, lowering consumer retail prices",
        "Importers pay zero customs tariffs because the currency depreciation absorbs all transport costs",
        "There is zero financial effect because international trade contracts are settled in gold bullion",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Economic mechanics [1 Mark]: Importers must pay foreign suppliers in foreign currency.\n"
        f"Step 2: Currency impact [1 Mark]: When the Rand weakens, each Dollar or Euro costs more Rands.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "Think about whether you need more Rands or fewer Rands to buy $1 when the Rand weakens."
    t2 = "More Rands per Dollar means the importer pays more for goods bought from abroad."
    t3 = f"The correct economic effect is: {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_51", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Exrate 52: Impact of Rand depreciation on South African exporters."""
    sector = r.choice(["Western Cape fruit and wine farming", "Mpumalanga citrus orchards", "Limpopo platinum and chrome mining"])

    prompt = (
        f"Consider a South African business operating in {sector} that exports products to Europe and the UK.\n\n"
        f"If the South African Rand depreciates against the British Pound and Euro, how does this affect "
        f"the business's revenue when converted back into South African Rands?"
    )
    correct_ans = "Revenue in Rands increases, because each Pound or Euro earned from exports converts into more Rands"
    custom_opts = [
        correct_ans,
        "Revenue in Rands decreases, because foreign buyers pay fewer Pounds and Euros",
        "Revenue remains strictly identical because exchange rates only apply to cash banknotes at retail branches",
        "The business is forced to close because export earnings are taxed at 100% under Reserve Bank rules",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Exporter perspective [1 Mark]: The exporter receives foreign currency payments (e.g. GBP or EUR).\n"
        f"Step 2: Conversion to ZAR [1 Mark]: When the Rand weakens, each unit of foreign currency is worth more Rands.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "An exporter earns foreign currency and exchanges it for Rands."
    t2 = "If 1 Pound rises from R 22 to R 24, the exporter gets R 2 more per Pound earned."
    t3 = f"The correct effect is: {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_52", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )
