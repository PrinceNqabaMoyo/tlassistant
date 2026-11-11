"""Basic currency conversions and direct rate applications (Subskills 1-9) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_1(r: random.Random) -> Dict[str, Any]:
    """Convert Rands (ZAR) to US Dollars (USD) given $1 = R x."""
    name = r.choice(SA_NAMES)
    rate = round(r.uniform(17.80, 19.20), 2)
    rand_amount = r.choice([2500, 3500, 5000, 7500, 10000, 12500, 15000])
    usd_amount = round(rand_amount / rate, 2)
    ans_str = _fmt_curr(usd_amount, "$")

    prompt = (
        f"{name} is planning a vacation to the United States and has saved {_fmt_curr(rand_amount)} for spending money.\n"
        f"If the current exchange rate is $1,00 = {_fmt_curr(rate)},\n"
        f"calculate how many US Dollars ($) {name} will receive.\n"
        f"*(Round off your answer to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Identify that converting from Rands to Dollars requires division by the exchange rate:\n"
        f"\\text{{USD Amount}} = \\text{{ZAR Amount}} \\div \\text{{Exchange Rate}}. [1 mark]\n"
        f"Step 2: Substitute given values:\n"
        f"\\text{{USD Amount}} = {rand_amount} \\div {_fmt(rate)} = {rand_amount / rate:.4f} [1 mark]\n"
        f"Step 3: Round off to 2 decimal places:\n"
        f"\\text{{Final amount}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(rand_amount * rate, 2), "$"),
        _fmt_curr(round(rand_amount / (rate + 1.0), 2), "$"),
        _fmt_curr(round(rand_amount / (rate - 1.0), 2), "$"),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_1",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the Rand amount by the exchange rate of {_fmt_curr(rate)}.",
        f"Calculate {rand_amount} ÷ {_fmt(rate)}.",
        f"Result = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_2(r: random.Random) -> Dict[str, Any]:
    """Convert US Dollars (USD) to Rands (ZAR) given $1 = R x."""
    name = r.choice(SA_NAMES)
    rate = round(r.uniform(17.80, 19.20), 2)
    usd_val = r.choice([85, 120, 175, 250, 380, 450, 600])
    rand_val = round(usd_val * rate, 2)
    ans_str = _fmt_curr(rand_val)

    prompt = (
        f"{name} is shopping online and finds an imported camera lens advertised for {_fmt_curr(usd_val, '$')}.\n"
        f"Using the exchange rate of $1,00 = {_fmt_curr(rate)},\n"
        f"determine the price of the camera lens in South African Rands (ZAR).\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: State the relationship:\n"
        f"To convert foreign currency (USD) to Rands, multiply by the exchange rate. [1 mark]\n"
        f"Step 2: Multiply the dollar price by the exchange rate:\n"
        f"\\text{{ZAR Price}} = {usd_val} \\times {_fmt(rate)} = {usd_val * rate:.2f} [1 mark]\n"
        f"Step 3: State the final Rand price:\n"
        f"\\text{{Price in Rands}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(usd_val / rate, 2)),
        _fmt_curr(round(usd_val * (rate + 1.5), 2)),
        _fmt_curr(round(usd_val * (rate - 1.5), 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_2",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the dollar price by the exchange rate of {_fmt_curr(rate)}.",
        f"Calculate {usd_val} × {_fmt(rate)}.",
        f"Price = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_3(r: random.Random) -> Dict[str, Any]:
    """Convert Rands (ZAR) to British Pounds (GBP) given £1 = R x."""
    name = r.choice(SA_NAMES)
    rate = round(r.uniform(22.80, 24.50), 2)
    rand_amount = r.choice([4500, 6000, 8000, 12000, 15000, 20000])
    gbp_amount = round(rand_amount / rate, 2)
    ans_str = _fmt_curr(gbp_amount, "£")

    prompt = (
        f"{name} is travelling to London for an academic conference and converts {_fmt_curr(rand_amount)} into British Pounds (GBP).\n"
        f"The exchange rate on the day is £1,00 = {_fmt_curr(rate)}.\n"
        f"Calculate the amount in British Pounds that {name} receives.\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Identify that converting Rands to British Pounds requires division:\n"
        f"\\text{{GBP Amount}} = \\text{{ZAR Amount}} \\div \\text{{Exchange Rate}}. [1 mark]\n"
        f"Step 2: Divide {_fmt_curr(rand_amount)} by {_fmt(rate)}:\n"
        f"{rand_amount} \\div {_fmt(rate)} = {rand_amount / rate:.4f} [1 mark]\n"
        f"Step 3: State the final rounded amount in Pounds:\n"
        f"\\text{{Amount received}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(rand_amount * rate, 2), "£"),
        _fmt_curr(round(rand_amount / (rate + 1.2), 2), "£"),
        _fmt_curr(round(rand_amount / (rate - 1.2), 2), "£"),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_3",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the Rand total by {_fmt(rate)}.",
        f"Calculate {rand_amount} ÷ {_fmt(rate)}.",
        f"Amount in GBP = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_4(r: random.Random) -> Dict[str, Any]:
    """Convert British Pounds (GBP) to Rands (ZAR) given £1 = R x."""
    name = r.choice(SA_NAMES)
    rate = round(r.uniform(22.80, 24.50), 2)
    gbp_amount = r.choice([40, 75, 120, 180, 250, 320, 500])
    rand_amount = round(gbp_amount * rate, 2)
    ans_str = _fmt_curr(rand_amount)

    prompt = (
        f"A family relative living in the United Kingdom sends {name} a gift of {_fmt_curr(gbp_amount, '£')}.\n"
        f"When depositing the cheque into a South African bank account, the bank uses an exchange rate of £1,00 = {_fmt_curr(rate)}.\n"
        f"How much will this gift be worth in South African Rands?\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: State the conversion rule:\n"
        f"\\text{{ZAR Amount}} = \\text{{GBP Amount}} \\times \\text{{Exchange Rate}}. [1 mark]\n"
        f"Step 2: Multiply the pound value by the exchange rate:\n"
        f"{gbp_amount} \\times {_fmt(rate)} = {gbp_amount * rate:.2f} [1 mark]\n"
        f"Step 3: Write down the final Rand value:\n"
        f"\\text{{Rand value}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(gbp_amount / rate, 2)),
        _fmt_curr(round(gbp_amount * (rate + 2.0), 2)),
        _fmt_curr(round(gbp_amount * (rate - 2.0), 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_4",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the pound amount by {_fmt(rate)}.",
        f"Calculate {gbp_amount} × {_fmt(rate)}.",
        f"Value in ZAR = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_5(r: random.Random) -> Dict[str, Any]:
    """Convert Rands (ZAR) to Euros (EUR) given €1 = R x."""
    name = r.choice(SA_NAMES)
    rate = round(r.uniform(19.50, 21.20), 2)
    rand_amount = r.choice([3500, 5000, 7500, 10000, 14000, 18000])
    eur_amount = round(rand_amount / rate, 2)
    ans_str = _fmt_curr(eur_amount, "€")

    prompt = (
        f"{name} is booking accommodation for a holiday in France that costs {_fmt_curr(rand_amount)} in South African Rands.\n"
        f"The travel booking system requires payment in Euros (€) at an exchange rate of €1,00 = {_fmt_curr(rate)}.\n"
        f"Calculate the equivalent cost in Euros.\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: State the conversion method:\n"
        f"\\text{{EUR Amount}} = \\text{{ZAR Amount}} \\div \\text{{Exchange Rate}}. [1 mark]\n"
        f"Step 2: Divide {_fmt_curr(rand_amount)} by {_fmt(rate)}:\n"
        f"{rand_amount} \\div {_fmt(rate)} = {rand_amount / rate:.4f} [1 mark]\n"
        f"Step 3: Round off to 2 decimal places:\n"
        f"\\text{{Cost in Euros}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(rand_amount * rate, 2), "€"),
        _fmt_curr(round(rand_amount / (rate + 1.0), 2), "€"),
        _fmt_curr(round(rand_amount / (rate - 1.0), 2), "€"),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_5",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the Rand cost by {_fmt(rate)}.",
        f"Calculate {rand_amount} ÷ {_fmt(rate)}.",
        f"Cost in EUR = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_6(r: random.Random) -> Dict[str, Any]:
    """Convert Euros (EUR) to Rands (ZAR) given €1 = R x."""
    name = r.choice(SA_NAMES)
    rate = round(r.uniform(19.50, 21.20), 2)
    eur_val = r.choice([65, 110, 160, 220, 350, 480])
    rand_val = round(eur_val * rate, 2)
    ans_str = _fmt_curr(rand_val)

    prompt = (
        f"{name} ordered specialised laboratory glassware from Germany priced at {_fmt_curr(eur_val, '€')}.\n"
        f"If the exchange rate is €1,00 = {_fmt_curr(rate)},\n"
        f"calculate the cost of this glassware in South African Rands (ZAR).\n"
        f"*(Round to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: State the conversion rule:\n"
        f"\\text{{ZAR Amount}} = \\text{{EUR Amount}} \\times \\text{{Exchange Rate}}. [1 mark]\n"
        f"Step 2: Multiply the Euro price by the exchange rate:\n"
        f"{eur_val} \\times {_fmt(rate)} = {eur_val * rate:.2f} [1 mark]\n"
        f"Step 3: State the final Rand cost:\n"
        f"\\text{{Total Rand cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(eur_val / rate, 2)),
        _fmt_curr(round(eur_val * (rate + 1.5), 2)),
        _fmt_curr(round(eur_val * (rate - 1.5), 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_6",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the Euro price by {_fmt(rate)}.",
        f"Calculate {eur_val} × {_fmt(rate)}.",
        f"Rand cost = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_7(r: random.Random) -> Dict[str, Any]:
    """Convert Rands to Japanese Yen (JPY) given R 1 = ¥ y."""
    name = r.choice(SA_NAMES)
    # R 1 = approx 8.00 JPY (or 1 JPY = R 0.125)
    yen_per_rand = round(r.uniform(7.50, 8.50), 2)
    rand_amount = r.choice([1500, 2500, 4000, 6000, 8000, 10000])
    yen_amount = int(round(rand_amount * yen_per_rand))
    ans_str = f"¥ {_fmt(yen_amount)}"

    prompt = (
        f"{name} is travelling to Tokyo, Japan. A foreign exchange bureau quotes the exchange rate as:\n"
        f"R 1,00 = ¥ {_fmt(yen_per_rand)} (Japanese Yen).\n"
        f"Calculate how many Japanese Yen {name} will receive in exchange for {_fmt_curr(rand_amount)}.\n"
        f"*(Round to the nearest whole Yen.)*"
    )
    explanation = (
        f"Step 1: Note that the rate is quoted per Rand (R 1,00 = ¥ {_fmt(yen_per_rand)}):\n"
        f"To find total Yen, multiply the Rand amount by the Yen per Rand rate. [1 mark]\n"
        f"Step 2: Multiply the values:\n"
        f"{rand_amount} \\times {_fmt(yen_per_rand)} = {rand_amount * yen_per_rand:.1f} [1 mark]\n"
        f"Step 3: Round off to the nearest whole Yen:\n"
        f"\\text{{Yen received}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"¥ {_fmt(int(round(rand_amount / yen_per_rand)))}",
        f"¥ {_fmt(int(round(rand_amount * (yen_per_rand + 1.0))))}",
        f"¥ {_fmt(int(round(rand_amount * (yen_per_rand - 1.0))))}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_7",
        prompt,
        ans_str,
        options,
        explanation,
        f"Multiply the Rand amount by {_fmt(yen_per_rand)}.",
        f"Calculate {rand_amount} × {_fmt(yen_per_rand)}.",
        f"Total Yen = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_8(r: random.Random) -> Dict[str, Any]:
    """Convert Rands to Australian Dollars (AUD) given A$1 = R x."""
    name = r.choice(SA_NAMES)
    rate = round(r.uniform(11.80, 12.80), 2)
    rand_amount = r.choice([3000, 4500, 6000, 9000, 12000, 15000])
    aud_amount = round(rand_amount / rate, 2)
    ans_str = _fmt_curr(aud_amount, "A$")

    prompt = (
        f"{name} is visiting relatives in Sydney, Australia and exchanges {_fmt_curr(rand_amount)} into Australian Dollars (AUD).\n"
        f"The exchange rate is given as A$1,00 = {_fmt_curr(rate)}.\n"
        f"Calculate how many Australian Dollars {name} will receive.\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Set up the division:\n"
        f"\\text{{AUD Amount}} = \\text{{ZAR Amount}} \\div \\text{{Exchange Rate}}. [1 mark]\n"
        f"Step 2: Divide {_fmt_curr(rand_amount)} by {_fmt(rate)}:\n"
        f"{rand_amount} \\div {_fmt(rate)} = {rand_amount / rate:.4f} [1 mark]\n"
        f"Step 3: State the rounded answer in AUD:\n"
        f"\\text{{Amount received}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(rand_amount * rate, 2), "A$"),
        _fmt_curr(round(rand_amount / (rate + 1.0), 2), "A$"),
        _fmt_curr(round(rand_amount / (rate - 1.0), 2), "A$"),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_8",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide the Rand amount by {_fmt(rate)}.",
        f"Calculate {rand_amount} ÷ {_fmt(rate)}.",
        f"Total AUD = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_9(r: random.Random) -> Dict[str, Any]:
    """Reciprocal rate conversion: Calculate R 1 = ... Foreign from $1 = R x (1 ÷ x)."""
    rate = round(r.uniform(17.50, 19.50), 2)
    reciprocal = round(1.0 / rate, 4)
    ans_str = f"$ {_fmt(reciprocal, places=4)}"

    prompt = (
        f"A financial newspaper quotes the exchange rate between the South African Rand and the US Dollar as:\n"
        f"$1,00 = {_fmt_curr(rate)}.\n"
        f"Express this exchange rate in terms of how many US Dollars one South African Rand is worth (R 1,00 = $ ...).\n"
        f"*(Round off your answer to 4 decimal places.)*"
    )
    explanation = (
        f"Step 1: Understand reciprocal exchange rates:\n"
        f"If \\$1,00 = \\text{{R }} {_fmt(rate)}, then \\text{{R }} 1,00 = \\$ (1 \\div {_fmt(rate)}). [1 mark]\n"
        f"Step 2: Perform the reciprocal division:\n"
        f"1 \\div {_fmt(rate)} = {1.0 / rate:.6f} [1 mark]\n"
        f"Step 3: Round off to 4 decimal places:\n"
        f"\\text{{Reciprocal rate}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"$ {_fmt(round(1.0 / (rate + 1.0), 4), places=4)}",
        f"$ {_fmt(round(1.0 / (rate - 1.0), 4), places=4)}",
        f"$ {_fmt(round(rate / 100.0, 4), places=4)}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_9",
        prompt,
        ans_str,
        options,
        explanation,
        f"Divide 1 by {_fmt(rate)}.",
        f"Calculate 1 ÷ {_fmt(rate)}.",
        f"R 1,00 = {ans_str}.",
        r,
        difficulty="medium",
    )
