"""Subskills 9 to 24: Bank Buying and Selling Rates (BSR & BBR) Direct Conversions (LB pages 244-245)."""
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


def gen_subskill_09(r: random.Random) -> Dict[str, Any]:
    """Exrate 09: Converting ZAR to USD notes using Bank Selling Rate (BSR)."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)
    bsr = round(r.uniform(18.60, 19.30), 4)
    bbr = round(bsr - r.uniform(0.70, 0.95), 4)
    zar_amount = r.choice([15000, 20000, 25000, 30000, 45000])

    prompt = (
        f"{name} goes to {bank['name']} in Johannesburg with {_fmt_curr(zar_amount)} to purchase US Dollars ($).\n\n"
        f"The bank exchange board shows for US Dollars:\n"
        f"• Bank Buying Rate (BBR): 1 USD = R {_fmt(bbr, 4)}\n"
        f"• Bank Selling Rate (BSR): 1 USD = R {_fmt(bsr, 4)}\n\n"
        f"Excluding bank fees, calculate how many US Dollars {name} can purchase, rounded to two decimal places."
    )
    usd_val = round(zar_amount / bsr, 2)
    correct_ans = _fmt_foreign(usd_val, "$")
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Identify correct rate [1 Mark]: Bank sells USD to client, so use BSR = R {_fmt(bsr, 4)}.\n"
        f"Step 2: Conversion [1 Mark]: {zar_amount} ÷ {bsr:.4f} = {zar_amount / bsr:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "The bank sells foreign currency to the client, so use the Bank Selling Rate (BSR)."
    t2 = f"Divide the Rand amount ({_fmt_curr(zar_amount)}) by the BSR (R {_fmt(bsr, 4)})."
    t3 = f"{zar_amount} ÷ {bsr:.4f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_09", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Exrate 10: Converting ZAR to GBP (£) notes using BSR."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)
    bsr = round(r.uniform(23.80, 24.60), 4)
    bbr = round(bsr - r.uniform(0.90, 1.25), 4)
    zar_amount = r.choice([18000, 22000, 28000, 35000])

    prompt = (
        f"{name} is travelling to London and exchanges {_fmt_curr(zar_amount)} for British Pounds (£) at {bank['name']}.\n\n"
        f"Exchange rates:\n"
        f"• BBR: 1 GBP = R {_fmt(bbr, 4)}\n"
        f"• BSR: 1 GBP = R {_fmt(bsr, 4)}\n\n"
        f"Without bank commission, calculate how many British Pounds (£) {name} receives, rounded to two decimal places."
    )
    gbp_val = round(zar_amount / bsr, 2)
    correct_ans = _fmt_foreign(gbp_val, "£")
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Identify rate [1 Mark]: Use BSR = R {_fmt(bsr, 4)} because bank sells foreign notes.\n"
        f"Step 2: Division [1 Mark]: {zar_amount} ÷ {bsr:.4f} = {zar_amount / bsr:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "When converting ZAR into British Pounds, divide by the Bank Selling Rate."
    t2 = f"Divide {zar_amount} by {bsr:.4f}."
    t3 = f"{zar_amount} ÷ {bsr:.4f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_10", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Exrate 11: Converting ZAR to EUR (€) notes using BSR."""
    name = r.choice(SA_NAMES)
    bsr = round(r.uniform(20.40, 21.20), 4)
    bbr = round(bsr - r.uniform(0.80, 1.10), 4)
    zar_amount = r.choice([12000, 16000, 24000, 32000])

    prompt = (
        f"{name} exchanges {_fmt_curr(zar_amount)} into Euros (€) for a trip to France.\n"
        f"The bank board displays:\n"
        f"• Bank Buying Rate (BBR): 1 EUR = R {_fmt(bbr, 4)}\n"
        f"• Bank Selling Rate (BSR): 1 EUR = R {_fmt(bsr, 4)}\n\n"
        f"Calculate the Euro amount {name} receives before fees, rounded to two decimal places."
    )
    eur_val = round(zar_amount / bsr, 2)
    correct_ans = _fmt_foreign(eur_val, "€")
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Foreign Amount = ZAR ÷ BSR\n"
        f"Step 2: Calculation [1 Mark]: {zar_amount} ÷ {bsr:.4f} = {zar_amount / bsr:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "The bank sells Euros to the customer, so divide by BSR."
    t2 = f"Calculate {zar_amount} ÷ {bsr:.4f}."
    t3 = f"The result is {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_11", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Exrate 12: Converting ZAR to BWP where quote is 1 ZAR = x BWP (BSR)."""
    name = r.choice(SA_NAMES)
    bsr_pula = round(r.uniform(0.7050, 0.7250), 4)
    bbr_pula = round(bsr_pula + r.uniform(0.0250, 0.0450), 4)
    zar_amount = r.choice([3500, 5000, 7500, 9000])

    prompt = (
        f"A bank in South Africa quotes rates for the Botswana Pula (BWP) based on 1 Rand:\n"
        f"• Bank Buying Rate (BBR): 1 ZAR = {bbr_pula:.4f} BWP\n"
        f"• Bank Selling Rate (BSR): 1 ZAR = {bsr_pula:.4f} BWP\n\n"
        f"Note: When quoting Pula per 1 Rand, the bank gives fewer Pula per Rand when selling Pula to a customer.\n"
        f"{name} exchanges {_fmt_curr(zar_amount)} to Pula. Calculate the amount in BWP {name} receives."
    )
    bwp_val = round(zar_amount * bsr_pula, 2)
    correct_ans = _fmt_foreign(bwp_val, "P ")
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Rate selection [1 Mark]: The bank is selling Pula, giving {bsr_pula:.4f} Pula per Rand.\n"
        f"Step 2: Calculation [1 Mark]: {zar_amount} × {bsr_pula:.4f} = {zar_amount * bsr_pula:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "When the exchange rate is given as foreign currency per 1 Rand, multiply the Rand amount by the selling rate."
    t2 = f"Multiply {zar_amount} by {bsr_pula:.4f}."
    t3 = f"{zar_amount} × {bsr_pula:.4f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_12", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Exrate 13: Converting ZAR to Japanese Yen (¥) using BSR."""
    name = r.choice(SA_NAMES)
    bsr = round(r.uniform(0.1240, 0.1340), 4)
    zar_amount = r.choice([10000, 15000, 20000])

    prompt = (
        f"{name} visits Japan and purchases Japanese Yen (¥) notes in South Africa.\n"
        f"The Bank Selling Rate is: 1 JPY = R {_fmt(bsr, 4)}.\n\n"
        f"Calculate how many Japanese Yen (¥) {name} receives for {_fmt_curr(zar_amount)}, rounded to the nearest Yen."
    )
    yen_val = round(zar_amount / bsr)
    correct_ans = _fmt_foreign(yen_val, "¥", places=0)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Japanese Yen = ZAR ÷ BSR\n"
        f"Step 2: Calculation [1 Mark]: {zar_amount} ÷ {bsr:.4f} = {zar_amount / bsr:.2f}\n"
        f"Step 3: Rounding [1 Mark]: Rounded to whole Yen = {correct_ans}"
    )
    t1 = "Divide the Rand amount by the BSR per Yen."
    t2 = f"Calculate {zar_amount} ÷ {bsr:.4f}."
    t3 = f"Round to the nearest whole Yen: {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_13", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Exrate 14: Converting ZAR to Australian Dollars (A$) using BSR."""
    name = r.choice(SA_NAMES)
    bsr = round(r.uniform(12.30, 12.85), 4)
    zar_amount = r.choice([14000, 18500, 25000])

    prompt = (
        f"{name} exchanges {_fmt_curr(zar_amount)} into Australian Dollars (A$) for an overseas study programme.\n"
        f"The Bank Selling Rate is: 1 AUD = R {_fmt(bsr, 4)}.\n\n"
        f"Calculate the amount of Australian Dollars {name} receives, rounded to two decimal places."
    )
    aud_val = round(zar_amount / bsr, 2)
    correct_ans = _fmt_foreign(aud_val, "A$")
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Rate [1 Mark]: 1 AUD = R {_fmt(bsr, 4)}\n"
        f"Step 2: Substitution [1 Mark]: {zar_amount} ÷ {bsr:.4f} = {zar_amount / bsr:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Divide the Rand amount by the Australian Dollar BSR."
    t2 = f"{zar_amount} ÷ {bsr:.4f}."
    t3 = f"Result = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_14", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Exrate 15: Determining total ZAR required to purchase a specific amount of foreign currency."""
    tour_group = r.choice(["school rugby team", "netball squad", "choir ensemble", "science olympiad delegation"])
    foreign_target = r.choice([3500, 4800, 6000, 8500])
    bsr = round(r.uniform(18.65, 19.45), 4)

    prompt = (
        f"A South African {tour_group} requires ${foreign_target} (USD) for an overseas trip.\n"
        f"A commercial bank quotes the Bank Selling Rate as: 1 USD = R {_fmt(bsr, 4)}.\n\n"
        f"Calculate the base amount in South African Rands (ZAR) required to purchase ${foreign_target}, "
        f"rounded to the nearest cent (excluding fees)."
    )
    zar_req = round(foreign_target * bsr, 2)
    correct_ans = _fmt_curr(zar_req)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Cost in ZAR = Required Foreign Amount × BSR\n"
        f"Step 2: Substitution [1 Mark]: {foreign_target} × {bsr:.4f} = {foreign_target * bsr:.4f}\n"
        f"Step 3: Solution [1 Mark]: Base Rand cost = {correct_ans}"
    )
    t1 = "To find the cost of a fixed foreign sum in Rands, multiply by the Bank Selling Rate."
    t2 = f"Multiply ${foreign_target} by {bsr:.4f}."
    t3 = f"{foreign_target} × {bsr:.4f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_15", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Exrate 16: Calculating the bank's profit spread between BSR and BBR."""
    code = r.choice(["USD", "GBP", "EUR"])
    names = {"USD": "US Dollar ($)", "GBP": "British Pound (£)", "EUR": "Euro (€)"}
    bsr = round(r.uniform(18.80, 24.50), 4)
    bbr = round(bsr - r.uniform(0.75, 1.20), 4)
    spread = round(bsr - bbr, 4)

    prompt = (
        f"A South African commercial bank quotes the following rates for {names[code]}:\n"
        f"• Bank Selling Rate (BSR): R {_fmt(bsr, 4)}\n"
        f"• Bank Buying Rate (BBR): R {_fmt(bbr, 4)}\n\n"
        f"Calculate the bank's profit spread (difference between BSR and BBR) per unit of foreign currency."
    )
    correct_ans = _fmt_curr(spread)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Spread = Bank Selling Rate - Bank Buying Rate\n"
        f"Step 2: Substitution [1 Mark]: {bsr:.4f} - {bbr:.4f} = {spread:.4f}\n"
        f"Step 3: Solution [1 Mark]: Spread per foreign unit = {correct_ans}"
    )
    t1 = "Spread is the gap between the selling rate and buying rate."
    t2 = f"Subtract BBR ({bbr:.4f}) from BSR ({bsr:.4f})."
    t3 = f"{bsr:.4f} - {bbr:.4f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_16", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Exrate 17: Converting leftover USD notes back to ZAR using BBR."""
    name = r.choice(SA_NAMES)
    bbr = round(r.uniform(17.80, 18.40), 4)
    usd_left = r.choice([240, 350, 520, 780, 950])

    prompt = (
        f"{name} returns from New York with ${usd_left} in leftover US Dollar banknotes.\n"
        f"{name} visits a bank counter to exchange these notes for South African Rands.\n"
        f"The Bank Buying Rate (BBR) is: 1 USD = R {_fmt(bbr, 4)}.\n\n"
        f"Calculate how much {name} receives in Rands (before bank fees), rounded to the nearest cent."
    )
    zar_val = round(usd_left * bbr, 2)
    correct_ans = _fmt_curr(zar_val)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Rate [1 Mark]: The bank buys foreign notes from the traveler, so use BBR = R {_fmt(bbr, 4)}.\n"
        f"Step 2: Multiplication [1 Mark]: {usd_left} × {bbr:.4f} = {usd_left * bbr:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "When selling foreign notes to the bank, the bank uses the Bank Buying Rate (BBR)."
    t2 = f"Multiply the foreign currency amount (${usd_left}) by BBR (R {_fmt(bbr, 4)})."
    t3 = f"{usd_left} × {bbr:.4f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_17", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Exrate 18: Converting leftover GBP (£) notes back to ZAR using BBR."""
    name = r.choice(SA_NAMES)
    bbr = round(r.uniform(22.80, 23.60), 4)
    gbp_left = r.choice([180, 260, 340, 480, 620])

    prompt = (
        f"{name} returns from the United Kingdom with £{gbp_left} in cash notes.\n"
        f"At the bureau de change, the Bank Buying Rate is: 1 GBP = R {_fmt(bbr, 4)}.\n\n"
        f"Calculate the gross amount in Rands {name} receives for these notes (before fees)."
    )
    zar_val = round(gbp_left * bbr, 2)
    correct_ans = _fmt_curr(zar_val)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Identification [1 Mark]: Use BBR = R {_fmt(bbr, 4)}.\n"
        f"Step 2: Calculation [1 Mark]: {gbp_left} × {bbr:.4f} = {gbp_left * bbr:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Multiply the British Pounds by the Bank Buying Rate."
    t2 = f"{gbp_left} × {bbr:.4f}."
    t3 = f"Total = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_18", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Exrate 19: Converting leftover EUR (€) notes back to ZAR using BBR."""
    name = r.choice(SA_NAMES)
    bbr = round(r.uniform(19.40, 20.10), 4)
    eur_left = r.choice([150, 280, 420, 560, 750])

    prompt = (
        f"{name} brings back €{eur_left} in Euro notes after a family holiday in Spain.\n"
        f"The local bank buys Euro banknotes at the Bank Buying Rate of: 1 EUR = R {_fmt(bbr, 4)}.\n\n"
        f"Calculate the gross Rand payout before deductions."
    )
    zar_val = round(eur_left * bbr, 2)
    correct_ans = _fmt_curr(zar_val)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: ZAR = Euros × BBR\n"
        f"Step 2: Calculation [1 Mark]: {eur_left} × {bbr:.4f} = {eur_left * bbr:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Multiply the Euro notes by the Bank Buying Rate."
    t2 = f"{eur_left} × {bbr:.4f}."
    t3 = f"Gross Rand value = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_19", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Exrate 20: Converting leftover BWP notes back to ZAR using BBR (1 ZAR = y BWP)."""
    name = r.choice(SA_NAMES)
    bbr_pula = round(r.uniform(0.7400, 0.7700), 4)
    pula_amount = r.choice([1800, 2600, 3500, 4800])

    prompt = (
        f"{name} returns from Francistown with {pula_amount} Botswana Pula (BWP) in banknotes.\n"
        f"A South African bank quotes the Bank Buying Rate as: 1 ZAR = {bbr_pula:.4f} BWP.\n\n"
        f"Note: Since the rate expresses Pula per Rand, {name} must divide by the rate to find the Rand value.\n"
        f"Calculate the Rand amount {name} receives, rounded to the nearest cent."
    )
    zar_val = round(pula_amount / bbr_pula, 2)
    correct_ans = _fmt_curr(zar_val)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Identify quote convention [1 Mark]: 1 ZAR = {bbr_pula:.4f} BWP.\n"
        f"Step 2: Division [1 Mark]: {pula_amount} ÷ {bbr_pula:.4f} = {pula_amount / bbr_pula:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "When the rate is given as BWP per 1 Rand, divide the Pula amount by the rate."
    t2 = f"Calculate {pula_amount} ÷ {bbr_pula:.4f}."
    t3 = f"Payout = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_20", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Exrate 21: Converting leftover Australian Dollars (A$) back to ZAR using BBR."""
    name = r.choice(SA_NAMES)
    bbr = round(r.uniform(11.60, 12.10), 4)
    aud_left = r.choice([250, 450, 680, 840])

    prompt = (
        f"{name} returns from Melbourne with A${aud_left} in cash notes.\n"
        f"The bank buys Australian Dollars at BBR: 1 AUD = R {_fmt(bbr, 4)}.\n\n"
        f"Calculate the gross Rand value of these notes."
    )
    zar_val = round(aud_left * bbr, 2)
    correct_ans = _fmt_curr(zar_val)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Formula [1 Mark]: Gross ZAR = AUD × BBR\n"
        f"Step 2: Substitution [1 Mark]: {aud_left} × {bbr:.4f} = {aud_left * bbr:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Multiply the AUD amount by the Bank Buying Rate."
    t2 = f"{aud_left} × {bbr:.4f}."
    t3 = f"Value = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_21", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Exrate 22: Converting foreign Travellers' Cheques to ZAR using Travellers' Cheque BBR."""
    name = r.choice(SA_NAMES)
    notes_bbr = round(r.uniform(22.80, 23.30), 4)
    tc_bbr = round(notes_bbr + r.uniform(0.20, 0.35), 4)
    cheque_amount = r.choice([1500, 2200, 3000, 4500])

    prompt = (
        f"{name} cashes £{cheque_amount} in British Pound Travellers' Cheques at a commercial bank.\n\n"
        f"Bank Exchange Rate Schedule for GBP:\n"
        f"• Bank Buying Rate (Banknotes): 1 GBP = R {_fmt(notes_bbr, 4)}\n"
        f"• Bank Buying Rate (Travellers' Cheques): 1 GBP = R {_fmt(tc_bbr, 4)}\n\n"
        f"Calculate the gross Rand amount the bank pays for the Travellers' Cheques."
    )
    zar_val = round(cheque_amount * tc_bbr, 2)
    correct_ans = _fmt_curr(zar_val)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Identify correct line [1 Mark]: Travellers' Cheques BBR = R {_fmt(tc_bbr, 4)}.\n"
        f"Step 2: Calculation [1 Mark]: {cheque_amount} × {tc_bbr:.4f} = {cheque_amount * tc_bbr:.4f}\n"
        f"Step 3: Solution [1 Mark]: Gross payout = {correct_ans}"
    )
    t1 = "Select the Travellers' Cheques buying rate, not the cash banknotes rate."
    t2 = f"Multiply £{cheque_amount} by the TC buying rate (R {_fmt(tc_bbr, 4)})."
    t3 = f"{cheque_amount} × {tc_bbr:.4f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_22", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Exrate 23: Comparing payout between cash notes BBR vs travellers' cheques/draft BBR."""
    amount = r.choice([2000, 3000, 4000])
    notes_bbr = round(r.uniform(18.00, 18.30), 4)
    tc_bbr = round(notes_bbr + 0.28, 4)

    prompt = (
        f"A customer has ${amount} (USD) and can cash it either as cash banknotes or as Travellers' Cheques.\n"
        f"• Cash notes BBR: 1 USD = R {_fmt(notes_bbr, 4)}\n"
        f"• Travellers' Cheques BBR: 1 USD = R {_fmt(tc_bbr, 4)}\n\n"
        f"Calculate how many more Rands the customer receives by cashing Travellers' Cheques instead of banknotes."
    )
    diff = round(amount * (tc_bbr - notes_bbr), 2)
    correct_ans = _fmt_curr(diff)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Difference in rate [1 Mark]: {tc_bbr:.4f} - {notes_bbr:.4f} = R {tc_bbr - notes_bbr:.4f} per Dollar\n"
        f"Step 2: Multiply by amount [1 Mark]: {amount} × {tc_bbr - notes_bbr:.4f} = {amount * (tc_bbr - notes_bbr):.4f}\n"
        f"Step 3: Solution [1 Mark]: Additional Rands = {correct_ans}"
    )
    t1 = "Find the difference between the two exchange rates and multiply by the dollar amount."
    t2 = f"Subtract {notes_bbr:.4f} from {tc_bbr:.4f}, then multiply by {amount}."
    t3 = f"The gain is {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_23", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Exrate 24: Re-exchanging foreign currency after a trip: calculating financial loss from spread."""
    name = r.choice(SA_NAMES)
    amount = r.choice([500, 800, 1200])
    bsr = round(r.uniform(23.90, 24.50), 4)
    bbr = round(bsr - r.uniform(0.95, 1.30), 4)

    prompt = (
        f"{name} bought £{amount} in notes before a trip at a Bank Selling Rate of 1 GBP = R {_fmt(bsr, 4)}.\n"
        f"However, the trip was cancelled. {name} immediately returned to the bank and sold the unused £{amount} "
        f"back at the Bank Buying Rate of 1 GBP = R {_fmt(bbr, 4)}.\n\n"
        f"Calculate the total financial loss (in Rands) caused solely by the bank's buy-sell spread (excluding commission)."
    )
    cost = amount * bsr
    payout = amount * bbr
    loss = round(cost - payout, 2)
    correct_ans = _fmt_curr(loss)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Initial cost to buy [1 Mark]: {amount} × {bsr:.4f} = {_fmt_curr(cost)}\n"
        f"Step 2: Payout when sold back [1 Mark]: {amount} × {bbr:.4f} = {_fmt_curr(payout)}\n"
        f"Step 3: Loss from spread [1 Mark]: {_fmt_curr(cost)} - {_fmt_curr(payout)} = {correct_ans}"
    )
    t1 = "Calculate what was paid to buy the pounds, then what was received when selling them back."
    t2 = f"Loss = {amount} × ({bsr:.4f} - {bbr:.4f})."
    t3 = f"Financial loss = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_24", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )
