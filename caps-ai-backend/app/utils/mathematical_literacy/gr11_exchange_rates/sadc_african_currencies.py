"""SADC regional currencies and cross-rate conversions (Subskills 10-18) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Common Monetary Area (CMA) 1:1 parity rule (Namibia NAD, Eswatini SZL, Lesotho LSL)."""
    name = r.choice(SA_NAMES)
    cma_country, curr_name, curr_symbol = r.choice([
        ("Namibia", "Namibian Dollar", "N$ "),
        ("Eswatini (Swaziland)", "Swazi Lilangeni", "E "),
        ("Lesotho", "Lesotho Loti", "L "),
    ])
    rand_amount = r.choice([1500, 2800, 4200, 5500, 7000])
    ans_str = f"{curr_symbol}{_fmt(rand_amount)},00"

    prompt = (
        f"{name} is travelling on holiday to {cma_country}. "
        f"Under the Common Monetary Area (CMA) agreement with South Africa, the {curr_name} is pegged "
        f"at an exchange rate of 1:1 with the South African Rand (1 ZAR = 1 {curr_symbol.strip()}).\n"
        f"If {name} converts {_fmt_curr(rand_amount)} into {curr_name}, how much {curr_name} will {name} receive?"
    )
    explanation = (
        f"Step 1: Identify the Common Monetary Area (CMA) parity rule:\n"
        f"Currencies in the CMA (Namibia, Lesotho, Eswatini) trade at an exact 1:1 ratio with the South African Rand. [1 mark]\n"
        f"Step 2: Apply the 1:1 conversion factor:\n"
        f"{rand_amount} \\times 1 = {rand_amount}. [1 mark]\n"
        f"Step 3: State the final amount with the appropriate currency symbol:\n"
        f"\\text{{Amount received}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{curr_symbol}{_fmt(round(rand_amount * 1.15, 2))}",
        f"{curr_symbol}{_fmt(round(rand_amount * 0.85, 2))}",
        f"{curr_symbol}{_fmt(round(rand_amount / 18.5, 2))}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_10",
        prompt,
        ans_str,
        options,
        explanation,
        f"The exchange rate between the Rand and {curr_name} is 1:1.",
        f"{rand_amount} Rands = {rand_amount} in {curr_name}.",
        f"Amount = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Convert Rands to Botswana Pula (BWP) given P 1 = R x."""
    name = r.choice(SA_NAMES)
    rate = round(r.uniform(1.35, 1.45), 2)  # P 1 = R 1,40
    rand_amount = r.choice([2500, 3500, 4800, 6000, 8500])
    pula_amount = round(rand_amount / rate, 2)
    ans_str = f"P {_fmt(pula_amount)}"

    prompt = (
        f"{name} is taking a wildlife photographic safari to the Okavango Delta in Botswana and converts "
        f"{_fmt_curr(rand_amount)} into Botswana Pula (BWP).\n"
        f"If the exchange rate is P 1,00 = {_fmt_curr(rate)},\n"
        f"calculate how many Botswana Pula (P) {name} will receive.\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Set up the conversion:\n"
        f"\\text{{BWP Amount}} = \\text{{ZAR Amount}} \\div \\text{{Rate per Pula}}. [1 mark]\n"
        f"Step 2: Divide {_fmt_curr(rand_amount)} by {_fmt(rate)}:\n"
        f"{rand_amount} \\div {_fmt(rate)} = {rand_amount / rate:.4f} [1 mark]\n"
        f"Step 3: State the final amount in Pula:\n"
        f"\\text{{Pula received}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"P {_fmt(round(rand_amount * rate, 2))}",
        f"P {_fmt(round(rand_amount / (rate + 0.2), 2))}",
        f"P {_fmt(round(rand_amount / (rate - 0.2), 2))}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_11",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the Rand amount by {_fmt(rate)}.",
        f"Calculate {rand_amount} ÷ {_fmt(rate)}.",
        f"Pula received = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Convert Botswana Pula (BWP) to Rands given P 1 = R x."""
    name = r.choice(SA_NAMES)
    rate = round(r.uniform(1.35, 1.45), 2)
    pula_val = r.choice([350, 500, 750, 1200, 1800, 2500])
    rand_val = round(pula_val * rate, 2)
    ans_str = _fmt_curr(rand_val)

    prompt = (
        f"A craft market trader in Gaborone sells a traditional woven basket for P {_fmt(pula_val)}.\n"
        f"{name} wants to know the equivalent price in South African Rands (ZAR).\n"
        f"Using the exchange rate of P 1,00 = {_fmt_curr(rate)},\n"
        f"calculate the cost of the basket in Rands.\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Identify that foreign Pula is converted to Rands by multiplying:\n"
        f"\\text{{ZAR Price}} = \\text{{BWP Price}} \\times \\text{{Rate}}. [1 mark]\n"
        f"Step 2: Multiply {pula_val} by {_fmt(rate)}:\n"
        f"{pula_val} \\times {_fmt(rate)} = {pula_val * rate:.2f} [1 mark]\n"
        f"Step 3: State the final Rand price:\n"
        f"\\text{{Price in ZAR}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(pula_val / rate, 2)),
        _fmt_curr(round(pula_val * (rate + 0.3), 2)),
        _fmt_curr(round(pula_val * (rate - 0.3), 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_12",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the Pula amount by {_fmt(rate)}.",
        f"Calculate {pula_val} × {_fmt(rate)}.",
        f"Cost in Rands = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Convert Rands to Zambian Kwacha (ZMW) given R 1 = ZMW y."""
    name = r.choice(SA_NAMES)
    kwacha_per_rand = round(r.uniform(1.35, 1.65), 2)
    rand_amount = r.choice([1500, 2400, 3600, 5000, 7500])
    kwacha_amount = round(rand_amount * kwacha_per_rand, 2)
    ans_str = f"ZMW {_fmt(kwacha_amount)}"

    prompt = (
        f"{name} is travelling to Livingstone, Zambia to visit Victoria Falls and converts {_fmt_curr(rand_amount)} into Zambian Kwacha (ZMW).\n"
        f"The exchange bureau advertises the rate as: R 1,00 = ZMW {_fmt(kwacha_per_rand)}.\n"
        f"Calculate the amount of Zambian Kwacha that {name} will receive.\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Note that the rate is quoted per Rand (R 1,00 = ZMW {_fmt(kwacha_per_rand)}):\n"
        f"To find total Kwacha, multiply the Rand amount by the Kwacha per Rand rate. [1 mark]\n"
        f"Step 2: Multiply the values:\n"
        f"{rand_amount} \\times {_fmt(kwacha_per_rand)} = {rand_amount * kwacha_per_rand:.2f} [1 mark]\n"
        f"Step 3: State the final Kwacha received:\n"
        f"\\text{{Kwacha received}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"ZMW {_fmt(round(rand_amount / kwacha_per_rand, 2))}",
        f"ZMW {_fmt(round(rand_amount * (kwacha_per_rand + 0.3), 2))}",
        f"ZMW {_fmt(round(rand_amount * (kwacha_per_rand - 0.3), 2))}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_13",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the Rand amount by {_fmt(kwacha_per_rand)}.",
        f"Calculate {rand_amount} × {_fmt(kwacha_per_rand)}.",
        f"Amount = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Convert Zambian Kwacha (ZMW) to Rands given R 1 = ZMW y."""
    name = r.choice(SA_NAMES)
    kwacha_per_rand = round(r.uniform(1.35, 1.65), 2)
    kwacha_val = r.choice([800, 1200, 1800, 2500, 4000])
    rand_val = round(kwacha_val / kwacha_per_rand, 2)
    ans_str = _fmt_curr(rand_val)

    prompt = (
        f"A hotel room in Lusaka, Zambia costs ZMW {_fmt(kwacha_val)} per night.\n"
        f"If the exchange rate is R 1,00 = ZMW {_fmt(kwacha_per_rand)},\n"
        f"determine the cost of the hotel room in South African Rands (ZAR).\n"
        f"*(Round to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Set up the conversion to Rands:\n"
        f"\\text{{ZAR Amount}} = \\text{{Kwacha Amount}} \\div \\text{{Kwacha per Rand}}. [1 mark]\n"
        f"Step 2: Divide {kwacha_val} by {_fmt(kwacha_per_rand)}:\n"
        f"{kwacha_val} \\div {_fmt(kwacha_per_rand)} = {kwacha_val / kwacha_per_rand:.4f} [1 mark]\n"
        f"Step 3: Round off to 2 decimal places:\n"
        f"\\text{{Cost in Rands}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(kwacha_val * kwacha_per_rand, 2)),
        _fmt_curr(round(kwacha_val / (kwacha_per_rand + 0.2), 2)),
        _fmt_curr(round(kwacha_val / (kwacha_per_rand - 0.2), 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_14",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the Kwacha amount by {_fmt(kwacha_per_rand)}.",
        f"Calculate {kwacha_val} ÷ {_fmt(kwacha_per_rand)}.",
        f"Rand cost = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Convert Rands to Mozambican Metical (MZN) given R 1 = MZN y."""
    name = r.choice(SA_NAMES)
    metical_per_rand = round(r.uniform(3.30, 3.70), 2)
    rand_amount = r.choice([1200, 2000, 3500, 5000])
    metical_amount = round(rand_amount * metical_per_rand, 2)
    ans_str = f"MT {_fmt(metical_amount)}"

    prompt = (
        f"{name} is taking a beach holiday in Ponta do Ouro, Mozambique and exchanges {_fmt_curr(rand_amount)} into Mozambican Meticais (MZN).\n"
        f"The border exchange bureau quotes the rate as: R 1,00 = MT {_fmt(metical_per_rand)}.\n"
        f"Calculate the amount in Mozambican Meticais that {name} will receive.\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Set up the calculation (multiply Rand amount by Metical per Rand rate):\n"
        f"\\text{{MZN Amount}} = {rand_amount} \\times {_fmt(metical_per_rand)}. [1 mark]\n"
        f"Step 2: Perform multiplication:\n"
        f"{rand_amount} \\times {_fmt(metical_per_rand)} = {rand_amount * metical_per_rand:.2f} [1 mark]\n"
        f"Step 3: State the final Metical amount:\n"
        f"\\text{{Amount received}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"MT {_fmt(round(rand_amount / metical_per_rand, 2))}",
        f"MT {_fmt(round(rand_amount * (metical_per_rand + 0.5), 2))}",
        f"MT {_fmt(round(rand_amount * (metical_per_rand - 0.5), 2))}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_15",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the Rand amount by {_fmt(metical_per_rand)}.",
        f"Calculate {rand_amount} × {_fmt(metical_per_rand)}.",
        f"Amount in MZN = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Cross-border road trip toll and fuel cost in local SADC currency vs ZAR."""
    name = r.choice(SA_NAMES)
    pula_rate = 1.40  # P 1 = R 1,40
    pula_fuel = r.choice([450, 600, 750, 900])
    pula_tolls = r.choice([80, 120, 150])
    total_pula = pula_fuel + pula_tolls
    total_rand = round(total_pula * pula_rate, 2)
    ans_str = _fmt_curr(total_rand)

    prompt = (
        f"{name} drove a delivery vehicle from Pretoria to Francistown, Botswana.\n"
        f"During the trip inside Botswana, {name} paid:\n"
        f"• P {_fmt(pula_fuel)} for diesel fuel\n"
        f"• P {_fmt(pula_tolls)} for road transit fees and tolls\n\n"
        f"If the exchange rate was P 1,00 = R 1,40, calculate the total cost of these travel expenses in South African Rands (ZAR)."
    )
    explanation = (
        f"Step 1: Calculate total expenses in Botswana Pula:\n"
        f"\\text{{Total Pula}} = {pula_fuel} + {pula_tolls} = {total_pula}\\text{{ Pula}}. [1 mark]\n"
        f"Step 2: Convert total Pula to Rands using P 1,00 = R 1,40:\n"
        f"\\text{{Total ZAR}} = {total_pula} \\times 1,40 = {total_rand:.2f} [1 mark]\n"
        f"Step 3: State the final total in Rands:\n"
        f"\\text{{Total Rand cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(total_pula / pula_rate, 2)),
        _fmt_curr(round((pula_fuel * pula_rate) + pula_tolls, 2)),
        _fmt_curr(round(total_rand + 150, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_16",
        prompt,
        ans_str,
        options,
        explanation,
        "Add the Pula expenses, then multiply the sum by 1,40.",
        f"Total Pula = {total_pula}. Total ZAR = {total_pula} × 1,40.",
        f"Total cost = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Multi-currency cross rate via Rand intermediate (e.g., converting BWP to USD via ZAR)."""
    name = r.choice(SA_NAMES)
    pula_to_zar = 1.40  # P 1 = R 1,40
    usd_to_zar = 18.20  # $1 = R 18,20
    pula_amount = r.choice([3500, 5000, 7000, 10000])

    # Convert Pula to Rands
    zar_amount = pula_amount * pula_to_zar
    # Convert Rands to USD
    usd_amount = round(zar_amount / usd_to_zar, 2)
    ans_str = _fmt_curr(usd_amount, "$")

    prompt = (
        f"A safari operator in Botswana needs to pay an American equipment supplier in US Dollars ($).\n"
        f"The operator has P {_fmt(pula_amount)} (Botswana Pula).\n"
        f"Given the following exchange rates against the South African Rand:\n"
        f"• P 1,00 = R 1,40\n"
        f"• $1,00 = R 18,20\n\n"
        f"Calculate the equivalent amount in US Dollars ($) by first converting the Pula to Rands.\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Convert Botswana Pula to South African Rands:\n"
        f"\\text{{ZAR Amount}} = {pula_amount} \\times 1,40 = {_fmt_curr(zar_amount)}. [1 mark]\n"
        f"Step 2: Convert the Rand amount to US Dollars by dividing by 18,20:\n"
        f"\\text{{USD Amount}} = {_fmt(zar_amount)} \\div 18,20 = {zar_amount / usd_to_zar:.4f} [1 mark]\n"
        f"Step 3: Round off to 2 decimal places:\n"
        f"\\text{{Amount in USD}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(pula_amount / (pula_to_zar * usd_to_zar), 2), "$"),
        _fmt_curr(round(pula_amount * pula_to_zar * usd_to_zar, 2), "$"),
        _fmt_curr(round(usd_amount * 1.15, 2), "$"),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_17",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply Pula by 1,40 to get Rands, then divide the Rands by 18,20 to get Dollars.",
        f"Rands = {pula_amount} × 1,40 = {_fmt_curr(zar_amount)}. USD = {_fmt(zar_amount)} ÷ 18,20.",
        f"USD amount = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Cross-rate conversion between EUR and USD using direct exchange ratio."""
    name = r.choice(SA_NAMES)
    eur_usd_rate = round(r.uniform(1.06, 1.12), 4)  # €1 = $ 1,0850
    eur_amount = r.choice([250, 400, 650, 800, 1200, 1500])
    usd_val = round(eur_amount * eur_usd_rate, 2)
    ans_str = _fmt_curr(usd_val, "$")

    prompt = (
        f"While transiting through an international airport, {name} wants to convert {_fmt_curr(eur_amount, '€')} into US Dollars ($).\n"
        f"The direct cross-rate quoted on the electronic exchange board is:\n"
        f"€1,00 = $ {_fmt(eur_usd_rate, places=4)}.\n"
        f"Calculate the amount in US Dollars ($) that {name} will receive.\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: State the direct cross-rate formula:\n"
        f"\\text{{USD Amount}} = \\text{{EUR Amount}} \\times (\\text{{USD per EUR rate}}). [1 mark]\n"
        f"Step 2: Multiply the Euro amount by the rate:\n"
        f"{eur_amount} \\times {_fmt(eur_usd_rate, places=4)} = {eur_amount * eur_usd_rate:.4f} [1 mark]\n"
        f"Step 3: Round off to 2 decimal places:\n"
        f"\\text{{Amount in USD}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(eur_amount / eur_usd_rate, 2), "$"),
        _fmt_curr(round(usd_val + 25.0, 2), "$"),
        _fmt_curr(round(usd_val - 25.0, 2), "$"),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_18",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the Euro amount by {_fmt(eur_usd_rate, places=4)}.",
        f"Calculate {eur_amount} × {_fmt(eur_usd_rate, places=4)}.",
        f"Amount in USD = {ans_str}.",
        r,
        difficulty="medium",
    )
