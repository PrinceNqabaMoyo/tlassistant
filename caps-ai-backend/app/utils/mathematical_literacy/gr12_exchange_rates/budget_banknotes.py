"""Subskills 33 to 40: Fixed ZAR Budget, Banknote Denominations, and Change (LB pages 247-248)."""
from __future__ import annotations

import math
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


def gen_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Exrate 33: Determining maximum foreign currency purchased with a fixed ZAR budget after commission."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)
    zar_budget = r.choice([5000, 7500, 10000, 12000])
    bsr = round(r.uniform(18.40, 19.10), 4)

    # In LB p.247 example 2: commission is calculated on available budget first: R5000 * 1.85% = R92.50
    # Available to purchase = R5000 - R92.50 = R4907.50
    comm = max(zar_budget * bank["comm_rate"], bank["min_fee"])
    avail_zar = zar_budget - comm
    usd_raw = avail_zar / bsr

    prompt = (
        f"{name} has a fixed budget of {_fmt_curr(zar_budget)} to buy US Dollars ($) at {bank['name']}.\n\n"
        f"Bank Conditions:\n"
        f"• Bank Selling Rate (BSR): 1 USD = R {_fmt(bsr, 4)}\n"
        f"• Commission: {bank['comm_rate'] * 100:.2f}% (minimum fee {_fmt_curr(bank['min_fee'])})\n\n"
        f"1. First deduct the bank commission from the total budget.\n"
        f"2. Calculate the theoretical maximum amount of US Dollars ($) that can be bought (before banknote rounding), "
        f"rounded to two decimal places."
    )
    correct_ans = _fmt_foreign(usd_raw, "$")
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Calculate commission [1 Mark]: max({_fmt_curr(zar_budget)} × {bank['comm_rate'] * 100:.2f}%, {_fmt_curr(bank['min_fee'])}) = {_fmt_curr(comm)}\n"
        f"Step 2: Available Rand amount [1 Mark]: {_fmt_curr(zar_budget)} - {_fmt_curr(comm)} = {_fmt_curr(avail_zar)}\n"
        f"Step 3: Foreign currency [1 Mark]: {_fmt_curr(avail_zar)} ÷ {bsr:.4f} = {correct_ans}"
    )
    t1 = "Deduct the bank commission from the total Rand budget first."
    t2 = f"Commission = {_fmt_curr(comm)}; Available = {_fmt_curr(avail_zar)}."
    t3 = f"Divide available Rand by BSR: {_fmt_curr(avail_zar)} ÷ {bsr:.4f} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_33", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Exrate 34: Banknote denomination rounding: rounding down to nearest 10 foreign units."""
    name = r.choice(SA_NAMES)
    raw_usd = round(r.uniform(415.50, 785.80), 2)
    rounded_down = int(math.floor(raw_usd / 10.0) * 10)

    prompt = (
        f"A calculation shows that {name}'s available funds can purchase ${raw_usd:.2f} (USD).\n\n"
        f"South African commercial banks only issue foreign cash in whole banknotes and round DOWN "
        f"to the nearest 10 Dollars.\n\n"
        f"Determine the exact amount of US Dollars in banknotes that the bank will issue to {name}."
    )
    correct_ans = f"${rounded_down}"
    custom_opts = [
        correct_ans,
        f"${rounded_down + 10}",
        f"${int(round(raw_usd))}",
        f"${rounded_down - 10}",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Bank rule [1 Mark]: Banks do not issue foreign cents/coins; banknotes are rounded down to nearest 10.\n"
        f"Step 2: Floor calculation [1 Mark]: ${raw_usd:.2f} rounded DOWN to nearest multiple of 10.\n"
        f"Step 3: Solution [1 Mark]: Banknote amount = {correct_ans}."
    )
    t1 = "Banks only dispense banknotes in multiples of 10 or 20, never fractional cents."
    t2 = f"Take the whole tens part below {raw_usd:.2f}."
    t3 = f"The bank issues {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_34", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Exrate 35: Banknote denomination rounding: rounding down to nearest 20 foreign units."""
    name = r.choice(SA_NAMES)
    raw_gbp = round(r.uniform(325.40, 895.60), 2)
    rounded_down = int(math.floor(raw_gbp / 20.0) * 20)

    prompt = (
        f"{name}'s converted funds equal £{raw_gbp:.2f} (GBP).\n"
        f"The bureau stocks British Pounds strictly in denominations of £20 and £50 banknotes, "
        f"so transactions are rounded DOWN to the nearest multiple of £20.\n\n"
        f"What is the maximum amount of British Pounds in banknotes {name} will receive?"
    )
    correct_ans = f"£{rounded_down}"
    custom_opts = [
        correct_ans,
        f"£{rounded_down + 20}",
        f"£{int(round(raw_gbp))}",
        f"£{rounded_down - 20}",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Denomination constraint [1 Mark]: Round down to nearest multiple of £20.\n"
        f"Step 2: Calculation [1 Mark]: floor({raw_gbp:.2f} ÷ 20) × 20 = {rounded_down}\n"
        f"Step 3: Solution [1 Mark]: Banknote allocation = {correct_ans}."
    )
    t1 = "Round down to the nearest multiple of 20."
    t2 = f"Find the largest multiple of 20 less than or equal to {raw_gbp:.2f}."
    t3 = f"The amount is {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_35", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )


def gen_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Exrate 36: Calculating exact Rand change returned after purchasing rounded banknote bundle."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)
    zar_tendered = r.choice([5000, 6000, 8000, 10000])
    bsr = round(r.uniform(18.50, 19.20), 4)

    # 1. Commission on tendered budget
    comm = max(zar_tendered * bank["comm_rate"], bank["min_fee"])
    avail_zar = zar_tendered - comm
    usd_raw = avail_zar / bsr
    usd_notes = int(math.floor(usd_raw / 10.0) * 10)

    actual_cost_notes = usd_notes * bsr
    total_spent = actual_cost_notes + comm
    change_zar = round(zar_tendered - total_spent, 2)

    prompt = (
        f"{name} hands {_fmt_curr(zar_tendered)} in cash to the teller at {bank['name']} to buy US Dollars.\n\n"
        f"Transaction Details:\n"
        f"• Bank Selling Rate (BSR): 1 USD = R {_fmt(bsr, 4)}\n"
        f"• Bank commission: {_fmt_curr(comm)}\n"
        f"• Banknotes issued: ${usd_notes} (rounded down to nearest 10 Dollars)\n\n"
        f"Calculate the exact change in South African Rands (ZAR) returned to {name}."
    )
    correct_ans = _fmt_curr(change_zar)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Cost of foreign banknotes [1 Mark]: ${usd_notes} × {bsr:.4f} = {_fmt_curr(actual_cost_notes)}\n"
        f"Step 2: Total deduction [1 Mark]: {_fmt_curr(actual_cost_notes)} + {_fmt_curr(comm)} (fee) = {_fmt_curr(total_spent)}\n"
        f"Step 3: Change returned [1 Mark]: {_fmt_curr(zar_tendered)} - {_fmt_curr(total_spent)} = {correct_ans}"
    )
    t1 = "Find the actual Rand cost of the issued notes, add the commission, and subtract from the tendered amount."
    t2 = f"Notes cost = {_fmt_curr(actual_cost_notes)}, Fee = {_fmt_curr(comm)}, Total spent = {_fmt_curr(total_spent)}."
    t3 = f"Change = {_fmt_curr(zar_tendered)} - {_fmt_curr(total_spent)} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_36", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Exrate 37: Selling foreign currency to achieve a targeted minimum ZAR amount (rounding UP)."""
    name = r.choice(SA_NAMES)
    target_zar = r.choice([10000, 15000, 20000])
    bbr = round(r.uniform(22.80, 23.40), 4)

    # Raw pounds needed: target_zar / bbr
    raw_pounds = target_zar / bbr
    # Must round UP to nearest 10 notes to ensure at least target_zar is reached
    rounded_up_pounds = int(math.ceil(raw_pounds / 10.0) * 10)

    prompt = (
        f"A visiting tourist, {name}, needs at least {_fmt_curr(target_zar)} in cash to pay a local safari lodge in Rands.\n"
        f"The bank buys British Pounds at BBR: 1 GBP = R {_fmt(bbr, 4)}.\n\n"
        f"The tourist only carries whole £10 banknotes. Determine the minimum amount of British Pounds "
        f"(rounded UP to the nearest £10) that {name} must exchange to receive at least {_fmt_curr(target_zar)}."
    )
    correct_ans = f"£{rounded_up_pounds}"
    custom_opts = [
        correct_ans,
        f"£{rounded_up_pounds - 10}",
        f"£{rounded_up_pounds + 10}",
        f"£{int(round(raw_pounds))}",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Raw pounds required [1 Mark]: {_fmt_curr(target_zar)} ÷ {bbr:.4f} = £{raw_pounds:.2f}\n"
        f"Step 2: Rounding requirement [1 Mark]: Must round UP to nearest £10 note so payout meets or exceeds the target.\n"
        f"Step 3: Solution [1 Mark]: ceil({raw_pounds:.2f} ÷ 10) × 10 = {correct_ans} (payout = {_fmt_curr(rounded_up_pounds * bbr)})"
    )
    t1 = "Divide the target Rand amount by the Bank Buying Rate."
    t2 = f"{target_zar} ÷ {bbr:.4f} = £{raw_pounds:.2f}."
    t3 = f"Round UP to the nearest multiple of 10: {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_37", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Exrate 38: Evaluating fee impact on small vs large transactions (regressive nature of minimum fees)."""
    min_fee = 85.0
    small_tx = 1000.0
    large_tx = 50000.0

    eff_small = round((min_fee / small_tx) * 100.0, 2)
    eff_large = round((min_fee / large_tx) * 100.0, 2)

    prompt = (
        f"A bank charges a minimum foreign exchange fee of {_fmt_curr(min_fee)}.\n\n"
        f"Calculate the effective percentage cost of this minimum fee on a small transaction of {_fmt_curr(small_tx)}, "
        f"and explain why minimum fees disproportionately disadvantage small transactions."
    )
    correct_ans = f"{_fmt(eff_small, 2)}% effective cost, making small transactions disproportionately expensive"
    custom_opts = [
        correct_ans,
        f"{_fmt(eff_large, 2)}% effective cost, making small transactions highly economical",
        f"1,85% fixed flat fee, with no proportional difference between transaction sizes",
        f"Zero effective cost, because minimum fees are fully refunded by the Reserve Bank",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Effective percentage [1 Mark]: ({min_fee:.2f} ÷ {small_tx:.2f}) × 100% = {_fmt(eff_small, 2)}%\n"
        f"Step 2: Proportional analysis [1 Mark]: A fixed {_fmt_curr(min_fee)} fee represents a massive {_fmt(eff_small, 2)}% slice of a small {_fmt_curr(small_tx)} exchange.\n"
        f"Step 3: Conclusion [1 Mark]: {correct_ans}."
    )
    t1 = "Calculate (Minimum Fee ÷ Transaction Amount) × 100%."
    t2 = f"({min_fee} ÷ {small_tx}) × 100% = {_fmt(eff_small, 2)}%."
    t3 = f"The result is {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_38", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Exrate 39: Comparing airport forex bureau (0% comm, wider spread) vs bank branch (narrower spread + fee)."""
    amount = 2000
    # Airport Bureau: BSR = 19.65, Commission = 0
    bsr_airport = 19.65
    cost_airport = amount * bsr_airport

    # Bank Branch: BSR = 18.90, Commission = 1.85%
    bsr_bank = 18.90
    base_bank = amount * bsr_bank
    comm_bank = base_bank * 0.0185
    cost_bank = base_bank + comm_bank

    diff = round(abs(cost_airport - cost_bank), 2)
    cheaper = "Bank Branch" if cost_bank < cost_airport else "Airport Bureau"

    prompt = (
        f"A traveler compares two options to buy ${amount} (USD) in cash:\n\n"
        f"• Option A (Airport Bureau): 0% commission, but BSR is 1 USD = R {_fmt(bsr_airport, 2)}\n"
        f"• Option B (City Bank Branch): 1,85% commission, but BSR is 1 USD = R {_fmt(bsr_bank, 2)}\n\n"
        f"Calculate the difference in total Rands payable and determine which option is cheaper."
    )
    correct_ans = f"{cheaper} is cheaper by {_fmt_curr(diff)}"
    custom_opts = [
        correct_ans,
        f"{'Airport Bureau' if cheaper == 'Bank Branch' else 'Bank Branch'} is cheaper by {_fmt_curr(diff)}",
        f"Both options cost exactly the same total Rand amount of {_fmt_curr(cost_airport)}",
        f"{cheaper} is cheaper by {_fmt_curr(diff * 1.5)}",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Option A cost [1 Mark]: {amount} × {bsr_airport:.2f} = {_fmt_curr(cost_airport)}\n"
        f"Step 2: Option B cost [1 Mark]: ({amount} × {bsr_bank:.2f}) + 1,85% fee = {_fmt_curr(base_bank)} + {_fmt_curr(comm_bank)} = {_fmt_curr(cost_bank)}\n"
        f"Step 3: Comparison [1 Mark]: |{_fmt_curr(cost_airport)} - {_fmt_curr(cost_bank)}| = {_fmt_curr(diff)} ({correct_ans})"
    )
    t1 = "Calculate total cost for Option A (no fee) and Option B (rate + 1.85% fee)."
    t2 = f"Option A = {_fmt_curr(cost_airport)}, Option B = {_fmt_curr(cost_bank)}."
    t3 = f"Difference = {_fmt_curr(diff)}; {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_39", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Exrate 40: Comprehensive budget allocation: forex cash, fees, and contingency in ZAR."""
    total_fund = r.choice([30000, 40000, 50000])
    forex_pct = 70
    fee_pct = 2
    contingency_pct = 28

    contingency_zar = total_fund * (contingency_pct / 100.0)

    prompt = (
        f"A family plans an overseas vacation with a total saved fund of {_fmt_curr(total_fund)}.\n"
        f"Their financial plan allocates:\n"
        f"• {forex_pct}% for purchasing foreign currency cash\n"
        f"• {fee_pct}% set aside for bank transaction commissions and card fees\n"
        f"• Remaining {contingency_pct}% retained in their South African bank account as emergency contingency\n\n"
        f"Calculate the amount in Rands retained for emergency contingency."
    )
    correct_ans = _fmt_curr(contingency_zar)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Identify percentage [1 Mark]: Contingency = {contingency_pct}%\n"
        f"Step 2: Calculation [1 Mark]: {_fmt_curr(total_fund)} × {contingency_pct}% = {_fmt_curr(contingency_zar)}\n"
        f"Step 3: Solution [1 Mark]: Contingency reserve = {correct_ans}"
    )
    t1 = f"Multiply the total fund ({_fmt_curr(total_fund)}) by {contingency_pct}%."
    t2 = f"{total_fund} × 0,{contingency_pct}."
    t3 = f"Contingency amount = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_40", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="easy"
    )
