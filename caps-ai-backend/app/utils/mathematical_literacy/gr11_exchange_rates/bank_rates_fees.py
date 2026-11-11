"""Bank foreign exchange tables, buying vs selling rates, and transaction fees (Subskills 37-44) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Distinguish between Bank Buying Rate (BBR) and Bank Selling Rate (BSR) from customer perspective."""
    name = r.choice(SA_NAMES)
    action = r.choice(["buy_usd", "sell_leftover_usd"])

    if action == "buy_usd":
        question_text = (
            f"{name} is going on vacation to New York and visits a South African commercial bank "
            f"to exchange South African Rands into US Dollars ($).\n"
            f"Which rate will the bank use for this transaction?"
        )
        ans_str = "Bank Selling Rate (BSR)"
        reason = (
            "From the bank's perspective, the bank is SELLING foreign currency (US Dollars) to the customer in exchange for Rands."
        )
        distractor_alt = "Bank Buying Rate (BBR)"
    else:
        question_text = (
            f"{name} returns to South Africa from an overseas trip with $ 300,00 leftover cash and visits "
            f"a bank to exchange the US Dollars back into South African Rands.\n"
            f"Which rate will the bank use for this transaction?"
        )
        ans_str = "Bank Buying Rate (BBR)"
        reason = (
            "From the bank's perspective, the bank is BUYING the foreign currency (US Dollars) from the customer."
        )
        distractor_alt = "Bank Selling Rate (BSR)"

    prompt = (
        f"{question_text}\n"
        f"Choose between Bank Selling Rate (BSR) or Bank Buying Rate (BBR)."
    )
    explanation = (
        f"Step 1: Always adopt the BANK'S perspective when deciding between BBR and BSR. [1 mark]\n"
        f"Step 2: Reason: {reason} [1 mark]\n"
        f"Step 3: State the correct rate:\n"
        f"\\text{{Applicable rate}} = {ans_str}. [1 mark]"
    )
    distractors = [
        distractor_alt,
        "Mid-market interbank rate without margin",
        "South African Reserve Bank repo rate",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_37",
        prompt,
        ans_str,
        options,
        explanation,
        "Think from the bank's point of view: is the bank buying foreign currency or selling it?",
        reason,
        f"Rate = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Customer buying foreign currency from a South African bank using Bank Selling Rate (BSR)."""
    name = r.choice(SA_NAMES)
    bbr = 18.20  # Bank buys at 18,20
    bsr = 18.95  # Bank sells at 18,95
    usd_needed = r.choice([500, 800, 1000, 1200, 1500])
    cost_rand = round(usd_needed * bsr, 2)
    ans_str = _fmt_curr(cost_rand)

    prompt = (
        f"A South African commercial bank displays the following foreign exchange rates for the US Dollar ($):\n"
        f"• Bank Buying Rate (BBR): $1,00 = {_fmt_curr(bbr)}\n"
        f"• Bank Selling Rate (BSR): $1,00 = {_fmt_curr(bsr)}\n\n"
        f"{name} wants to buy {_fmt_curr(usd_needed, '$')} from the bank for an upcoming business trip.\n"
        f"Calculate the total amount in South African Rands (ZAR) that {name} must pay the bank (excluding commission)."
    )
    explanation = (
        f"Step 1: Identify that the bank is SELLING Dollars to {name}, so the Bank Selling Rate (BSR) applies:\n"
        f"\\text{{Rate}} = {_fmt_curr(bsr)}. [1 mark]\n"
        f"Step 2: Multiply the required dollars by the BSR:\n"
        f"\\text{{Rand Cost}} = {usd_needed} \\times {_fmt(bsr)} = {cost_rand:.2f} [1 mark]\n"
        f"Step 3: State the final Rand cost:\n"
        f"\\text{{Total cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(usd_needed * bbr, 2)),
        _fmt_curr(round(usd_needed / bsr, 2)),
        _fmt_curr(round(cost_rand + 250, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_38",
        prompt,
        ans_str,
        options,
        explanation,
        f"The bank is selling dollars, so multiply by the Bank Selling Rate ({_fmt_curr(bsr)}).",
        f"Calculate {usd_needed} × {_fmt(bsr)}.",
        f"Total Rand cost = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Customer selling leftover foreign currency back to the bank using Bank Buying Rate (BBR)."""
    name = r.choice(SA_NAMES)
    bbr = 22.80  # Bank buys GBP at 22,80
    bsr = 23.90  # Bank sells GBP at 23,90
    gbp_leftover = r.choice([150, 250, 350, 450, 600])
    rand_received = round(gbp_leftover * bbr, 2)
    ans_str = _fmt_curr(rand_received)

    prompt = (
        f"{name} returned from the United Kingdom with {_fmt_curr(gbp_leftover, '£')} in cash.\n"
        f"The bank's exchange desk quotes the following rates for the British Pound (£):\n"
        f"• Bank Buying Rate (BBR): £1,00 = {_fmt_curr(bbr)}\n"
        f"• Bank Selling Rate (BSR): £1,00 = {_fmt_curr(bsr)}\n\n"
        f"Calculate how much in South African Rands (ZAR) {name} will receive when selling the pounds back to the bank."
    )
    explanation = (
        f"Step 1: Identify that the bank is BUYING the pounds from {name}, so the Bank Buying Rate (BBR) applies:\n"
        f"\\text{{Rate}} = {_fmt_curr(bbr)}. [1 mark]\n"
        f"Step 2: Multiply the leftover pounds by the BBR:\n"
        f"\\text{{ZAR Received}} = {gbp_leftover} \\times {_fmt(bbr)} = {rand_received:.2f} [1 mark]\n"
        f"Step 3: State the final Rand payout:\n"
        f"\\text{{Amount received}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(gbp_leftover * bsr, 2)),
        _fmt_curr(round(gbp_leftover / bbr, 2)),
        _fmt_curr(round(rand_received - 150, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_39",
        prompt,
        ans_str,
        options,
        explanation,
        f"The bank is buying the pounds from the customer, so use the BBR ({_fmt_curr(bbr)}).",
        f"Calculate {gbp_leftover} × {_fmt(bbr)}.",
        f"Amount received = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Calculate the bank's profit spread / margin between BSR and BBR on a transaction."""
    bbr = 18.25
    bsr = 19.10
    spread_per_unit = round(bsr - bbr, 2)
    amount_usd = 1000.0
    total_spread_profit = round(amount_usd * spread_per_unit, 2)
    ans_str = _fmt_curr(total_spread_profit)

    prompt = (
        f"A bank buys US Dollars at BBR = {_fmt_curr(bbr)} and sells US Dollars at BSR = {_fmt_curr(bsr)}.\n"
        f"The difference between the Bank Selling Rate and Bank Buying Rate is the bank's trading margin (spread).\n"
        f"Calculate the bank's gross spread profit in Rands on trading $ 1 000,00."
    )
    explanation = (
        f"Step 1: Calculate the spread per US Dollar:\n"
        f"\\text{{Spread}} = \\text{{BSR}} - \\text{{BBR}} = {bsr} - {bbr} = {_fmt(spread_per_unit)}\\text{{ Rands/Dollar}}. [1 mark]\n"
        f"Step 2: Multiply the spread by $ 1 000:\n"
        f"\\text{{Gross Spread Profit}} = 1\\,000 \\times {_fmt(spread_per_unit)} = {total_spread_profit:.2f} [1 mark]\n"
        f"Step 3: State the final profit:\n"
        f"\\text{{Spread profit}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(spread_per_unit),
        _fmt_curr(round(total_spread_profit * 1.5, 2)),
        _fmt_curr(round(bsr * amount_usd, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_40",
        prompt,
        ans_str,
        options,
        explanation,
        "Find the difference between BSR and BBR, then multiply by 1 000.",
        f"Spread = {bsr} - {bbr} = {_fmt(spread_per_unit)}. Profit = 1 000 × {_fmt(spread_per_unit)}.",
        f"Profit = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Foreign exchange commission calculation with percentage rate and minimum fee."""
    name = r.choice(SA_NAMES)
    comm_rate_pct = 2.25
    min_fee = 95.0
    rand_val = r.choice([2000, 3500, 6000, 8500, 12000])
    calculated_comm = round(rand_val * (comm_rate_pct / 100.0), 2)
    actual_comm = max(min_fee, calculated_comm)
    ans_str = _fmt_curr(actual_comm)

    prompt = (
        f"A Bureau de Change charges a foreign exchange commission of 2,25% on all currency transactions, "
        f"subject to a minimum fee of {_fmt_curr(min_fee)}.\n"
        f"{name} exchanges South African Rands valued at {_fmt_curr(rand_val)}.\n"
        f"Calculate the commission fee in Rands that {name} will be charged."
    )
    explanation = (
        f"Step 1: Calculate the percentage commission:\n"
        f"\\text{{Commission}} = {rand_val} \\times 2,25\\% = {rand_val} \\times 0,0225 = {_fmt_curr(calculated_comm)}. [1 mark]\n"
        f"Step 2: Compare against the minimum fee of {_fmt_curr(min_fee)}:\n"
        + (f"Since {_fmt_curr(calculated_comm)} < {_fmt_curr(min_fee)}, the minimum fee of {_fmt_curr(min_fee)} applies.\n" if calculated_comm < min_fee else f"Since {_fmt_curr(calculated_comm)} \\ge {_fmt_curr(min_fee)}, the calculated fee of {_fmt_curr(calculated_comm)} applies.\n")
        + f"[1 mark]\n"
        f"Step 3: State the final commission payable:\n"
        f"\\text{{Commission}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(min_fee if actual_comm != min_fee else calculated_comm),
        _fmt_curr(round(rand_val * 0.05, 2)),
        _fmt_curr(round(actual_comm + 50.0, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_41",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate 2,25% of the transaction value and apply the minimum fee if the result is lower.",
        f"2,25% of {rand_val} = {_fmt_curr(calculated_comm)}. Compare with minimum {_fmt_curr(min_fee)}.",
        f"Commission fee = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Total Rand payment required when purchasing foreign currency (Foreign × BSR + Commission)."""
    name = r.choice(SA_NAMES)
    bsr = 18.80
    usd_amount = 600.0
    comm_pct = 2.0  # 2% commission
    base_cost = round(usd_amount * bsr, 2)
    comm_cost = round(base_cost * (comm_pct / 100.0), 2)
    total_cost = round(base_cost + comm_cost, 2)
    ans_str = _fmt_curr(total_cost)

    prompt = (
        f"{name} goes to a South African bank to purchase {_fmt_curr(usd_amount, '$')} for an overseas journey.\n"
        f"The bank's terms are:\n"
        f"• Bank Selling Rate (BSR): $1,00 = {_fmt_curr(bsr)}\n"
        f"• Administration commission fee: 2,0% on the total Rand purchase price\n\n"
        f"Calculate the total amount in South African Rands that {name} must pay the bank."
    )
    explanation = (
        f"Step 1: Calculate the base Rand cost using the BSR:\n"
        f"\\text{{Base Cost}} = 600 \\times 18,80 = {_fmt_curr(base_cost)}. [1 mark]\n"
        f"Step 2: Calculate the 2,0% commission fee:\n"
        f"\\text{{Commission}} = {_fmt(base_cost)} \\times 0,02 = {_fmt_curr(comm_cost)}. [1 mark]\n"
        f"Step 3: Add base cost and commission to get total Rand payment:\n"
        f"\\text{{Total}} = {_fmt(base_cost)} + {_fmt(comm_cost)} = {total_cost:.2f} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(base_cost),
        _fmt_curr(round(base_cost - comm_cost, 2)),
        _fmt_curr(round(total_cost + 120, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_42",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply dollars by BSR to get base cost, find 2% commission, then add together.",
        f"Base = 600 × 18,80 = {_fmt_curr(base_cost)}. Commission = 2% of {_fmt(base_cost)} = {_fmt_curr(comm_cost)}.",
        f"Total cost = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Net foreign currency received after deducting a fixed administrative fee."""
    name = r.choice(SA_NAMES)
    bsr = 20.00  # €1 = R 20,00
    flat_fee_zar = 120.0
    rand_tendered = 5000.0
    net_rand_for_fx = rand_tendered - flat_fee_zar
    eur_received = round(net_rand_for_fx / bsr, 2)
    ans_str = _fmt_curr(eur_received, "€")

    prompt = (
        f"{name} hands over {_fmt_curr(rand_tendered)} in cash at an exchange counter to buy Euros (€).\n"
        f"The exchange counter charges a flat administrative transaction fee of {_fmt_curr(flat_fee_zar)}, "
        f"which is subtracted from the Rand amount before conversion.\n"
        f"If the Bank Selling Rate is €1,00 = {_fmt_curr(bsr)},\n"
        f"calculate how many Euros (€) {name} actually receives.\n"
        f"*(Round off to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Subtract the flat fee from the tendered cash:\n"
        f"\\text{{Net Rands}} = 5\\,000 - 120 = {_fmt_curr(net_rand_for_fx)}. [1 mark]\n"
        f"Step 2: Convert the remaining Rands to Euros using the BSR:\n"
        f"\\text{{Euros Received}} = {_fmt(net_rand_for_fx)} \\div 20,00 = {eur_received:.2f} [1 mark]\n"
        f"Step 3: State the final Euro amount received:\n"
        f"\\text{{Amount received}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(rand_tendered / bsr, 2), "€"),
        _fmt_curr(round(eur_received - 10, 2), "€"),
        _fmt_curr(round(eur_received + 15, 2), "€"),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_43",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract the R 120 fee from R 5 000 first, then divide by 20,00.",
        f"Net Rands = 5 000 - 120 = {_fmt_curr(net_rand_for_fx)}. Euros = {_fmt(net_rand_for_fx)} ÷ 20.",
        f"Euros received = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Net Rand proceeds from converting foreign cash at an airport bureau after flat fee + percentage."""
    name = r.choice(SA_NAMES)
    bbr = 18.00  # $1 = R 18,00
    usd_tendered = 400.0
    flat_fee = 75.0
    comm_pct = 1.5

    gross_zar = round(usd_tendered * bbr, 2)
    comm_zar = round(gross_zar * (comm_pct / 100.0), 2)
    total_deductions = flat_fee + comm_zar
    net_zar = round(gross_zar - total_deductions, 2)
    ans_str = _fmt_curr(net_zar)

    prompt = (
        f"{name} arrives at OR Tambo International Airport with {_fmt_curr(usd_tendered, '$')} to exchange into Rands.\n"
        f"The airport foreign exchange kiosk uses the following schedule:\n"
        f"• Bank Buying Rate (BBR): $1,00 = {_fmt_curr(bbr)}\n"
        f"• Kiosk administrative service charge: {_fmt_curr(flat_fee)} flat fee\n"
        f"• Commission: 1,5% on the gross Rand value\n\n"
        f"Calculate the net amount in South African Rands that {name} receives in cash."
    )
    explanation = (
        f"Step 1: Calculate the gross Rand value:\n"
        f"\\text{{Gross Rands}} = 400 \\times 18,00 = {_fmt_curr(gross_zar)}. [1 mark]\n"
        f"Step 2: Calculate the 1,5% commission and add the flat fee:\n"
        f"\\text{{Commission}} = {_fmt(gross_zar)} \\times 0,015 = {_fmt_curr(comm_zar)}\n"
        f"\\text{{Total deductions}} = {_fmt(comm_zar)} + 75,00 = {_fmt_curr(total_deductions)}. [1 mark]\n"
        f"Step 3: Subtract total deductions from gross Rands:\n"
        f"\\text{{Net Rands}} = {_fmt(gross_zar)} - {_fmt(total_deductions)} = {net_zar:.2f} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(gross_zar),
        _fmt_curr(round(gross_zar - flat_fee, 2)),
        _fmt_curr(round(gross_zar - comm_zar, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    d_spec = {
        "kind": "bar_graph",
        "title": f"Foreign Currency Conversion ({name})",
        "categories": ["Gross ZAR", "Fees & Comm", "Net Payout"],
        "values": [gross_zar, flat_fee + comm_zar, net_zar],
    }
    return _build_question_payload(
        "subskill_44",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate gross Rands (400 × 18), subtract 1,5% commission and R 75 flat fee.",
        f"Gross = {_fmt_curr(gross_zar)}. Deductions = {_fmt_curr(comm_zar)} + R 75 = {_fmt_curr(total_deductions)}.",
        f"Net payout = {ans_str}.",
        r,
        diagram_spec=d_spec,
        difficulty="hard",
    )

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
