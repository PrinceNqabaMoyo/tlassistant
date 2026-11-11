"""Subskills 1 to 8: Foreign Exchange Tables and Rate Conventions (LB pages 240-243)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_BANKS,
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_foreign,
)


def gen_subskill_01(r: random.Random) -> Dict[str, Any]:
    """Exrate 01: Table lookup & identifying BSR vs BBR for a foreign banknote purchase."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)
    curr_code = r.choice(["USD", "GBP", "EUR"])
    curr_map = {
        "USD": ("US Dollar ($)", 18.25, 18.98),
        "GBP": ("British Pound (£)", 23.40, 24.35),
        "EUR": ("Euro (€)", 19.90, 20.85),
    }
    c_name, bbr, bsr = curr_map[curr_code]

    prompt = (
        f"{name} is planning an overseas holiday and visits {bank['name']} in South Africa to buy "
        f"{c_name} cash banknotes before travelling.\n\n"
        f"The bank foreign exchange rate board displays:\n"
        f"• Bank Buying Rate (BBR): R {bbr:.2f}\n"
        f"• Bank Selling Rate (BSR): R {bsr:.2f}\n\n"
        f"Which rate will {bank['name']} use for this transaction, and why?"
    )
    correct_ans = f"Bank Selling Rate (BSR) of R {bsr:.2f}, because the bank is selling foreign currency to {name}"
    custom_opts = [
        correct_ans,
        f"Bank Buying Rate (BBR) of R {bbr:.2f}, because {name} is buying currency from the bank",
        f"Bank Buying Rate (BBR) of R {bbr:.2f}, because the bank buys South African Rands from {name}",
        f"Average mid-market rate of R {(bbr + bsr) / 2:.2f}, because banks do not apply retail spreads for travelers",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Identify perspective [1 Mark]: Exchange rates are always defined from the BANK's perspective.\n"
        f"Step 2: Bank action [1 Mark]: {bank['name']} is selling {c_name} notes to the customer.\n"
        f"Step 3: Conclusion [1 Mark]: The bank applies the Bank Selling Rate (BSR) of R {bsr:.2f}."
    )
    t1 = "Always consider the transaction from the bank's viewpoint, not the traveler's viewpoint."
    t2 = "When a customer wants foreign cash, the bank is SELLING foreign currency to them."
    t3 = f"The bank applies the Bank Selling Rate (BSR), which is R {bsr:.2f}."

    table_data = {
        "title": f"{bank['name']} - Retail Foreign Exchange Board",
        "headers": ["Currency", "Bank Buying Rate (BBR)", "Bank Selling Rate (BSR)"],
        "rows": [
            [c_name, f"R {bbr:.2f}", f"R {bsr:.2f}"],
            ["Botswana Pula (BWP)", "P 0,7450", "P 0,7120"],
        ],
    }

    return _build_question_payload(
        "exrate_gr12_01", prompt, correct_ans, opts, expl, t1, t2, t3, r, table_data=table_data, difficulty="easy"
    )


def gen_subskill_02(r: random.Random) -> Dict[str, Any]:
    """Exrate 02: Direct quote interpretation: 1 Foreign Unit = x ZAR."""
    name = r.choice(SA_NAMES)
    rate = round(r.uniform(18.10, 19.40), 4)
    amount_foreign = r.choice([350, 480, 650, 820, 1200])

    prompt = (
        f"A South African commercial bank quotes the exchange rate for US Dollars as: 1 USD = R {_fmt(rate, 4)}.\n\n"
        f"{name} purchases an online software license priced at ${amount_foreign} (USD).\n"
        f"Calculate the equivalent cost in South African Rands (ZAR), rounded to the nearest cent."
    )
    zar_val = round(amount_foreign * rate, 2)
    correct_ans = _fmt_curr(zar_val)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Cost in ZAR = Foreign Amount × Exchange Rate\n"
        f"Step 2: Substitution [1 Mark]: {amount_foreign} × {rate:.4f} = {amount_foreign * rate:.4f}\n"
        f"Step 3: Rounding [1 Mark]: {correct_ans}"
    )
    t1 = "Direct quote means 1 foreign unit is worth a certain amount of Rands."
    t2 = f"Multiply the foreign currency amount (${amount_foreign}) by the rate (R {_fmt(rate, 4)})."
    t3 = f"Calculate {amount_foreign} × {rate:.4f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_02", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_03(r: random.Random) -> Dict[str, Any]:
    """Exrate 03: Indirect quote interpretation: 1 ZAR = y Foreign Units."""
    name = r.choice(SA_NAMES)
    pula_rate = round(r.uniform(0.7100, 0.7450), 4)
    rand_amount = r.choice([2500, 3200, 4500, 6000, 8500])

    prompt = (
        f"A foreign exchange bureau in Mahikeng quotes: 1 ZAR = {pula_rate:.4f} BWP (Botswana Pula).\n\n"
        f"{name} is travelling to Gaborone and exchanges {_fmt_curr(rand_amount)} into Botswana Pula.\n"
        f"Calculate how many Botswana Pula {name} receives, rounded to two decimal places."
    )
    bwp_val = round(rand_amount * pula_rate, 2)
    correct_ans = _fmt_foreign(bwp_val, "P ")
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Identification [1 Mark]: Rate gives Pula per 1 Rand: 1 ZAR = {pula_rate:.4f} BWP.\n"
        f"Step 2: Fraction method [1 Mark]: {rand_amount} × {pula_rate:.4f} = {rand_amount * pula_rate:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Check whether the quote is Rands per Pula or Pula per Rand."
    t2 = f"Here 1 Rand gives {pula_rate:.4f} Pula, so multiply R {rand_amount} by {pula_rate:.4f}."
    t3 = f"Pula = {rand_amount} × {pula_rate:.4f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_03", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_04(r: random.Random) -> Dict[str, Any]:
    """Exrate 04: Calculating reciprocal exchange rate."""
    code = r.choice(["USD", "EUR", "GBP"])
    names = {"USD": "US Dollar", "EUR": "Euro", "GBP": "British Pound"}
    rate = round(r.uniform(18.0, 24.5), 2)

    prompt = (
        f"The exchange rate between the South African Rand (ZAR) and the {names[code]} ({code}) is given as:\n"
        f"1 {code} = R {_fmt(rate, 2)}\n\n"
        f"Calculate the reciprocal exchange rate: the value of 1 ZAR in {code}, rounded to 4 decimal places."
    )
    reciprocal = round(1.0 / rate, 4)
    correct_ans = f"{reciprocal:.4f} {code}"
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Value of 1 ZAR in {code} = 1 ÷ (Exchange Rate in ZAR)\n"
        f"Step 2: Substitution [1 Mark]: 1 ÷ {rate:.2f} = {1.0 / rate:.6f}\n"
        f"Step 3: Rounding [1 Mark]: Rounded to 4 decimal places = {correct_ans}"
    )
    t1 = "The reciprocal rate of 1 Foreign = R x is found by calculating 1 ÷ x."
    t2 = f"Divide 1 by {rate:.2f}."
    t3 = f"1 ÷ {rate:.2f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_04", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_05(r: random.Random) -> Dict[str, Any]:
    """Exrate 05: Common Monetary Area (CMA) 1:1 parity rule."""
    country, currency, code = r.choice([
        ("Namibia", "Namibian Dollar", "NAD"),
        ("Eswatini", "Lilangeni", "SZL"),
        ("Lesotho", "Loti", "LSL"),
    ])
    amount = r.choice([1500, 2400, 3800, 5200])

    prompt = (
        f"Under the Common Monetary Area (CMA) multilateral agreement between South Africa and neighboring countries, "
        f"the {currency} ({code}) is pegged to the South African Rand (ZAR).\n\n"
        f"A traveler from {country} arrives in Durban with {code} {_fmt(amount, 0)} in cash.\n"
        f"What is the equivalent value in South African Rands (ZAR), and what exchange rate applies?"
    )
    correct_ans = f"{_fmt_curr(amount)}, at an exchange parity rate of 1 : 1"
    custom_opts = [
        correct_ans,
        f"{_fmt_curr(amount * 1.15)}, at an exchange rate of 1 : 1,15",
        f"{_fmt_curr(amount * 0.85)}, after deducting standard 15% currency conversion loss",
        f"{_fmt_curr(amount - 85.0)}, after standard bank minimum bureau commission",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: CMA Parity Rule [1 Mark]: Member states of the Common Monetary Area peg their currencies at 1:1.\n"
        f"Step 2: Conversion [1 Mark]: 1 {code} = R 1,00.\n"
        f"Step 3: Solution [1 Mark]: {code} {_fmt(amount, 0)} = {correct_ans}."
    )
    t1 = "Namibia, Lesotho, and Eswatini belong to the Common Monetary Area (CMA) with South Africa."
    t2 = "Their currencies trade at a fixed 1 to 1 ratio with the South African Rand."
    t3 = f"The value is exactly equal: {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_05", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_06(r: random.Random) -> Dict[str, Any]:
    """Exrate 06: Explaining non-traded / zero-quote currency entries."""
    bank = r.choice(SA_BANKS)

    prompt = (
        f"On {bank['name']}'s foreign currency board, the retail exchange rate for Nigerian Naira (NGN) banknotes "
        f"is listed as '0,00' for both Buying and Selling.\n\n"
        f"What is the mathematical and commercial reason for this entry on the retail foreign exchange board?"
    )
    correct_ans = "The bank does not physically trade or stock cash banknotes for that currency at retail counters"
    custom_opts = [
        correct_ans,
        "The currency has collapsed completely and possesses zero monetary purchasing power globally",
        "The currency has an exchange rate identical to the South African Rand (1 : 1 parity)",
        "The South African Reserve Bank bans all wire transfers to and from that nation",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Reading exchange tables [1 Mark]: An entry of 0,00 indicates an untraded retail cash facility.\n"
        f"Step 2: Commercial context [1 Mark]: Retail branches do not physically buy or sell cash notes of certain restricted currencies.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "Look at the curriculum textbook note on why some currencies display 0,00 in cash tables."
    t2 = "It means retail counters do not hold cash banknotes for that specific currency."
    t3 = f"The correct reason is: {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_06", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_07(r: random.Random) -> Dict[str, Any]:
    """Exrate 07: Estimation of foreign price in ZAR using rounded exchange rate."""
    item = r.choice([
        ("digital camera", 429.0, "$", "USD", 18.78, 19.0),
        ("wool winter coat", 135.0, "£", "GBP", 23.65, 24.0),
        ("designer backpack", 185.0, "€", "EUR", 20.32, 20.0),
    ])
    prod, f_price, sym, code, exact_rate, round_rate = item

    prompt = (
        f"A South African traveler in an overseas airport sees a {prod} priced at {sym}{_fmt(f_price, 2)} ({code}).\n"
        f"The exact exchange rate is 1 {code} = R {_fmt(exact_rate, 2)}.\n\n"
        f"The traveler estimates the cost in Rands by rounding the exchange rate to the nearest whole Rand (R {_fmt(round_rate, 0)}).\n"
        f"Calculate the estimated price in South African Rands."
    )
    est_zar = round(f_price * round_rate, 2)
    correct_ans = _fmt_curr(est_zar)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Rounded rate [1 Mark]: 1 {code} ≈ R {_fmt(round_rate, 0)}\n"
        f"Step 2: Estimation calculation [1 Mark]: {f_price:.2f} × {round_rate:.0f} = {f_price * round_rate:.2f}\n"
        f"Step 3: Solution [1 Mark]: Estimated price = {correct_ans}"
    )
    t1 = "Multiply the foreign price by the rounded exchange rate."
    t2 = f"Calculate {f_price} × {round_rate:.0f}."
    t3 = f"The estimated Rand cost is {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_07", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_08(r: random.Random) -> Dict[str, Any]:
    """Exrate 08: Absolute and percentage difference between estimate and exact calculation."""
    f_price = r.choice([250.0, 320.0, 450.0, 580.0])
    exact_rate = round(r.uniform(18.55, 19.45), 2)
    round_rate = round(exact_rate)

    exact_zar = round(f_price * exact_rate, 2)
    est_zar = round(f_price * round_rate, 2)
    diff = round(abs(est_zar - exact_zar), 2)

    prompt = (
        f"An online shopper considers a gadget costing ${f_price:.2f} (USD).\n"
        f"• Exact rate: 1 USD = R {_fmt(exact_rate, 2)}\n"
        f"• Estimated rate (rounded to nearest Rand): 1 USD = R {_fmt(round_rate, 0)}\n\n"
        f"Calculate the absolute difference (in Rands) between the quick estimate and the exact conversion."
    )
    correct_ans = _fmt_curr(diff)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Exact cost [1 Mark]: {f_price:.2f} × {exact_rate:.2f} = {_fmt_curr(exact_zar)}\n"
        f"Step 2: Estimated cost [1 Mark]: {f_price:.2f} × {round_rate} = {_fmt_curr(est_zar)}\n"
        f"Step 3: Absolute difference [1 Mark]: |{_fmt_curr(est_zar)} - {_fmt_curr(exact_zar)}| = {correct_ans}"
    )
    t1 = "Compute both the exact Rand value and the estimated Rand value."
    t2 = f"Exact = {f_price} × {exact_rate:.2f}; Estimated = {f_price} × {round_rate}."
    t3 = f"Subtract the smaller from the larger to find the difference: {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_08", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )
