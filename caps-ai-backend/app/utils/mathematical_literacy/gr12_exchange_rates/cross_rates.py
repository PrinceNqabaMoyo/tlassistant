"""Subskills 41 to 46: Cross-Rates and Multi-Currency International Travel (LB pages 248-249)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_foreign,
)


def gen_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Exrate 41: Cross-rate calculation: Converting USD to GBP via ZAR rates."""
    name = r.choice(SA_NAMES)
    usd_amount = r.choice([1500, 2000, 2500, 3000])
    usd_bsr = round(r.uniform(18.20, 18.80), 4)
    gbp_bsr = round(r.uniform(23.40, 24.20), 4)

    # In LB p.248 question 1.3.6:
    # $2000 x R9.2454 = R18 490.80
    # R18 490.80 / R14.4375 = £1 280.75
    zar_mid = usd_amount * usd_bsr
    gbp_res = round(zar_mid / gbp_bsr, 2)

    prompt = (
        f"{name} has ${usd_amount} (USD) and wishes to convert this amount into British Pounds (£) "
        f"at a South African foreign exchange counter.\n\n"
        f"Bank Exchange Rates:\n"
        f"• 1 USD = R {_fmt(usd_bsr, 4)}\n"
        f"• 1 GBP = R {_fmt(gbp_bsr, 4)}\n\n"
        f"Using cross-currency conversion via the South African Rand, calculate how many British Pounds (£) "
        f"{name} receives, rounded to two decimal places."
    )
    correct_ans = _fmt_foreign(gbp_res, "£")
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Convert USD to ZAR [1 Mark]: ${usd_amount} × {usd_bsr:.4f} = {_fmt_curr(zar_mid)}\n"
        f"Step 2: Convert ZAR to GBP [1 Mark]: {_fmt_curr(zar_mid)} ÷ {gbp_bsr:.4f} = {gbp_res:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Convert the Dollars to Rands first, then convert that Rand amount into Pounds."
    t2 = f"Rands = ${usd_amount} × {usd_bsr:.4f} = {_fmt_curr(zar_mid)}. Pounds = {_fmt_curr(zar_mid)} ÷ {gbp_bsr:.4f}."
    t3 = f"Pounds received = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_41", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Exrate 42: Cross-rate calculation: Converting EUR to USD via ZAR rates."""
    name = r.choice(SA_NAMES)
    eur_amount = r.choice([1200, 1800, 2400, 3000])
    eur_bsr = round(r.uniform(20.10, 20.80), 4)
    usd_bsr = round(r.uniform(18.30, 18.90), 4)

    zar_mid = eur_amount * eur_bsr
    usd_res = round(zar_mid / usd_bsr, 2)

    prompt = (
        f"{name} wants to convert €{eur_amount} (EUR) into US Dollars ($) via a South African bank.\n\n"
        f"Bank Quote Rates:\n"
        f"• 1 EUR = R {_fmt(eur_bsr, 4)}\n"
        f"• 1 USD = R {_fmt(usd_bsr, 4)}\n\n"
        f"Calculate the equivalent amount in US Dollars ($), rounded to two decimal places."
    )
    correct_ans = _fmt_foreign(usd_res, "$")
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Convert EUR to ZAR [1 Mark]: €{eur_amount} × {eur_bsr:.4f} = {_fmt_curr(zar_mid)}\n"
        f"Step 2: Convert ZAR to USD [1 Mark]: {_fmt_curr(zar_mid)} ÷ {usd_bsr:.4f} = {usd_res:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Multiply the Euros by the Euro-Rand rate, then divide by the Dollar-Rand rate."
    t2 = f"Rands = €{eur_amount} × {eur_bsr:.4f} = {_fmt_curr(zar_mid)}. Dollars = {_fmt_curr(zar_mid)} ÷ {usd_bsr:.4f}."
    t3 = f"Total = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_42", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Exrate 43: Cross-rate calculation: Converting GBP to EUR via ZAR rates."""
    name = r.choice(SA_NAMES)
    gbp_amount = r.choice([800, 1200, 1600, 2000])
    gbp_bsr = round(r.uniform(23.60, 24.40), 4)
    eur_bsr = round(r.uniform(20.20, 20.90), 4)

    zar_mid = gbp_amount * gbp_bsr
    eur_res = round(zar_mid / eur_bsr, 2)

    prompt = (
        f"{name} is travelling from London to Frankfurt and converts £{gbp_amount} (GBP) into Euros (€) at a forex desk.\n\n"
        f"Exchange Rates:\n"
        f"• 1 GBP = R {_fmt(gbp_bsr, 4)}\n"
        f"• 1 EUR = R {_fmt(eur_bsr, 4)}\n\n"
        f"Calculate how many Euros (€) {name} receives, rounded to two decimal places."
    )
    correct_ans = _fmt_foreign(eur_res, "€")
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Convert GBP to ZAR [1 Mark]: £{gbp_amount} × {gbp_bsr:.4f} = {_fmt_curr(zar_mid)}\n"
        f"Step 2: Convert ZAR to EUR [1 Mark]: {_fmt_curr(zar_mid)} ÷ {eur_bsr:.4f} = {eur_res:.4f}\n"
        f"Step 3: Solution [1 Mark]: {correct_ans}"
    )
    t1 = "Convert British Pounds to Rands, then convert Rands to Euros."
    t2 = f"Rands = £{gbp_amount} × {gbp_bsr:.4f} = {_fmt_curr(zar_mid)}. Euros = {_fmt_curr(zar_mid)} ÷ {eur_bsr:.4f}."
    t3 = f"Total Euros = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_43", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Exrate 44: Multi-leg travel itinerary across 3 currencies converted to total ZAR."""
    name = r.choice(SA_NAMES)
    # 3 legs: UK flight (£450), Europe hotel (€620), US internal train ($280)
    gbp_amt = 450.0
    eur_amt = 620.0
    usd_amt = 280.0

    gbp_rate = 23.80
    eur_rate = 20.40
    usd_rate = 18.60

    zar_gbp = gbp_amt * gbp_rate
    zar_eur = eur_amt * eur_rate
    zar_usd = usd_amt * usd_rate
    total_zar = round(zar_gbp + zar_eur + zar_usd, 2)

    prompt = (
        f"{name} compiles an overseas travel itinerary with expenses across three currencies:\n"
        f"• UK Domestic Flight: £{gbp_amt:.0f} (Exchange rate: 1 GBP = R {_fmt(gbp_rate, 2)})\n"
        f"• Continental Hotel: €{eur_amt:.0f} (Exchange rate: 1 EUR = R {_fmt(eur_rate, 2)})\n"
        f"• US Transit Rail Pass: ${usd_amt:.0f} (Exchange rate: 1 USD = R {_fmt(usd_rate, 2)})\n\n"
        f"Calculate the TOTAL cost of these expenses in South African Rands (ZAR)."
    )
    correct_ans = _fmt_curr(total_zar)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Individual conversions [1 Mark]:\n"
        f"  • UK Flight: £{gbp_amt:.0f} × {gbp_rate:.2f} = {_fmt_curr(zar_gbp)}\n"
        f"  • Continental Hotel: €{eur_amt:.0f} × {eur_rate:.2f} = {_fmt_curr(zar_eur)}\n"
        f"  • US Rail Pass: ${usd_amt:.0f} × {usd_rate:.2f} = {_fmt_curr(zar_usd)}\n"
        f"Step 2: Sum [1 Mark]: {_fmt_curr(zar_gbp)} + {_fmt_curr(zar_eur)} + {_fmt_curr(zar_usd)}\n"
        f"Step 3: Solution [1 Mark]: Total = {correct_ans}"
    )
    t1 = "Convert each expense to Rands by multiplying each foreign amount by its respective exchange rate."
    t2 = f"Flight = {_fmt_curr(zar_gbp)}, Hotel = {_fmt_curr(zar_eur)}, Rail = {_fmt_curr(zar_usd)}."
    t3 = f"Total = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_44", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Exrate 45: Comparing cash forex purchase in SA vs ATM debit card withdrawals overseas (LB p.248)."""
    usd_total = 3000
    bsr = 18.80
    base_zar = usd_total * bsr

    # Option 1: Buy all notes at bank upfront: commission 1.68%
    comm_upfront = round(base_zar * 0.0168, 2)

    # Option 2: Withdraw 6 times from US ATMs at $500 each: fee R45 per withdrawal
    num_withdrawals = 6
    fee_per_wd = 45.0
    total_atm_fees = round(num_withdrawals * fee_per_wd, 2)

    diff = round(abs(comm_upfront - total_atm_fees), 2)
    cheaper = "ATM withdrawals overseas" if total_atm_fees < comm_upfront else "Upfront bank purchase"

    prompt = (
        f"A traveler needs $3 000 (USD) in cash during an overseas trip and evaluates two fee options:\n\n"
        f"• Option 1: Buy all $3 000 in notes at an ABSA branch before leaving. "
        f"The bank charges a 1,68% commission on the Rand value ({_fmt_curr(base_zar)} at 1 USD = R {_fmt(bsr, 2)}).\n"
        f"• Option 2: Use an ATM debit card in the US to make 6 separate cash withdrawals of $500 each, "
        f"at a flat fee of R 45,00 per international ATM withdrawal.\n\n"
        f"Calculate the difference in total fees between the two options and state which method is cheaper."
    )
    correct_ans = f"{cheaper} is cheaper by {_fmt_curr(diff)}"
    custom_opts = [
        correct_ans,
        f"{'Upfront bank purchase' if cheaper == 'ATM withdrawals overseas' else 'ATM withdrawals overseas'} is cheaper by {_fmt_curr(diff)}",
        f"Both methods charge exactly the same fee of {_fmt_curr(comm_upfront)}",
        f"{cheaper} is cheaper by {_fmt_curr(diff * 1.5)}",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Option 1 upfront commission [1 Mark]: 1,68% of {_fmt_curr(base_zar)} = {_fmt_curr(comm_upfront)}\n"
        f"Step 2: Option 2 ATM fees [1 Mark]: {num_withdrawals} withdrawals × R {fee_per_wd:.2f} = {_fmt_curr(total_atm_fees)}\n"
        f"Step 3: Comparison [1 Mark]: |{_fmt_curr(comm_upfront)} - {_fmt_curr(total_atm_fees)}| = {_fmt_curr(diff)} ({correct_ans})"
    )
    t1 = "Calculate the upfront bank commission, then multiply the number of ATM withdrawals by the per-withdrawal fee."
    t2 = f"Upfront fee = {_fmt_curr(comm_upfront)}; ATM fees = {num_withdrawals} × R 45 = {_fmt_curr(total_atm_fees)}."
    t3 = f"Difference = {_fmt_curr(diff)}; {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_45", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Exrate 46: International credit card swipe fee (e.g. 2.75% transaction fee) vs preloaded forex card."""
    spend_usd = r.choice([1200, 1500, 2000, 2500])
    bsr = round(r.uniform(18.50, 19.00), 4)
    base_zar = spend_usd * bsr

    # Credit card charges 2.75% currency conversion fee on swipe
    swipe_fee_pct = 2.75
    swipe_fee_zar = round(base_zar * (swipe_fee_pct / 100.0), 2)

    prompt = (
        f"A South African traveler swipes their standard credit card overseas for purchases totalling ${spend_usd} (USD).\n"
        f"The card issuer converts the transaction at 1 USD = R {_fmt(bsr, 4)} and levies an international "
        f"currency conversion fee of {swipe_fee_pct:.2f}% on the Rand amount.\n\n"
        f"Calculate the international transaction fee charged to the card in Rands, rounded to two decimal places."
    )
    correct_ans = _fmt_curr(swipe_fee_zar)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Base Rand amount [1 Mark]: ${spend_usd} × {bsr:.4f} = {_fmt_curr(base_zar)}\n"
        f"Step 2: Fee calculation [1 Mark]: {_fmt_curr(base_zar)} × {swipe_fee_pct:.2f}% = {swipe_fee_zar:.4f}\n"
        f"Step 3: Solution [1 Mark]: Fee = {correct_ans}"
    )
    t1 = "Find the base value in Rands first, then multiply by 2,75%."
    t2 = f"Base Rand value = ${spend_usd} × {bsr:.4f} = {_fmt_curr(base_zar)}."
    t3 = f"Fee = {_fmt_curr(base_zar)} × 0,0275 = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_46", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )
