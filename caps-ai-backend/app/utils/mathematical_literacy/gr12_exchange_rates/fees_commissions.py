"""Subskills 25 to 32: Bank Transaction Fees and Commission Structures (LB pages 245-247)."""
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
)


def gen_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Exrate 25: Calculating percentage commission when commission exceeds minimum threshold."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)
    comm_pct = bank["comm_rate"] * 100
    rand_val = r.choice([25000, 32000, 48000, 60000])

    prompt = (
        f"{name} exchanges South African Rands into foreign currency valued at {_fmt_curr(rand_val)} at {bank['name']}.\n\n"
        f"Bank Fee Schedule:\n"
        f"• Commission: {comm_pct:.2f}% of the Rand value\n"
        f"• Minimum fee: {_fmt_curr(bank['min_fee'])}\n"
        f"• Maximum fee: {_fmt_curr(bank['max_fee'])}\n\n"
        f"Calculate the commission fee that will be paid on this transaction."
    )
    calc_fee = rand_val * bank["comm_rate"]
    applied_fee = min(max(calc_fee, bank["min_fee"]), bank["max_fee"])
    correct_ans = _fmt_curr(applied_fee)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Calculate percentage fee [1 Mark]: {comm_pct:.2f}% of {_fmt_curr(rand_val)} = {_fmt_curr(calc_fee)}\n"
        f"Step 2: Check limits [1 Mark]: {_fmt_curr(calc_fee)} is between minimum {_fmt_curr(bank['min_fee'])} and maximum {_fmt_curr(bank['max_fee'])}.\n"
        f"Step 3: Solution [1 Mark]: Commission fee = {correct_ans}"
    )
    t1 = f"Multiply the transaction amount ({_fmt_curr(rand_val)}) by {comm_pct:.2f}% (or {bank['comm_rate']:.4f})."
    t2 = f"Compare the calculated value with the minimum ({_fmt_curr(bank['min_fee'])}) and maximum ({_fmt_curr(bank['max_fee'])})."
    t3 = f"The fee is {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_25", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Exrate 26: Applying minimum commission fee clause when calculated percentage is below threshold."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)
    comm_pct = bank["comm_rate"] * 100
    # Choose small Rand value so that comm < min_fee
    rand_val = r.choice([1500, 2200, 2800, 3200])

    calc_fee = rand_val * bank["comm_rate"]
    prompt = (
        f"{name} exchanges a small sum of {_fmt_curr(rand_val)} into foreign notes at {bank['name']}.\n\n"
        f"Fee Structure:\n"
        f"• Commission: {comm_pct:.2f}% of Rand value\n"
        f"• Minimum fee: {_fmt_curr(bank['min_fee'])}\n\n"
        f"Calculate the exact fee that will be charged for this transaction."
    )
    correct_ans = _fmt_curr(bank["min_fee"])
    custom_opts = [
        correct_ans,
        _fmt_curr(calc_fee),
        _fmt_curr(bank["min_fee"] + calc_fee),
        _fmt_curr(calc_fee * 2),
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Calculate raw percentage [1 Mark]: {_fmt_curr(rand_val)} × {comm_pct:.2f}% = {_fmt_curr(calc_fee)}\n"
        f"Step 2: Apply minimum fee condition [1 Mark]: {_fmt_curr(calc_fee)} is less than the minimum fee of {_fmt_curr(bank['min_fee'])}.\n"
        f"Step 3: Solution [1 Mark]: The minimum fee applies: {correct_ans}."
    )
    t1 = "Calculate the percentage fee first, then compare with the minimum fee."
    t2 = f"{comm_pct:.2f}% of {_fmt_curr(rand_val)} = {_fmt_curr(calc_fee)}, which is smaller than {_fmt_curr(bank['min_fee'])}."
    t3 = f"The bank charges the minimum fee: {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_26", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Exrate 27: Applying maximum commission cap clause when calculated percentage exceeds upper limit."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)
    comm_pct = bank["comm_rate"] * 100
    # Choose large Rand value so that comm > max_fee
    rand_val = r.choice([75000, 90000, 110000, 125000])

    calc_fee = rand_val * bank["comm_rate"]
    prompt = (
        f"{name} exchanges {_fmt_curr(rand_val)} for an extended overseas business assignment.\n\n"
        f"{bank['name']} charges:\n"
        f"• Commission rate: {comm_pct:.2f}%\n"
        f"• Minimum fee: {_fmt_curr(bank['min_fee'])}\n"
        f"• Maximum fee: {_fmt_curr(bank['max_fee'])}\n\n"
        f"Calculate the bank fee charged on this transaction."
    )
    correct_ans = _fmt_curr(bank["max_fee"])
    custom_opts = [
        correct_ans,
        _fmt_curr(calc_fee),
        _fmt_curr(bank["min_fee"]),
        _fmt_curr(calc_fee - bank["max_fee"]),
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    expl = (
        f"Step 1: Calculate raw percentage [1 Mark]: {_fmt_curr(rand_val)} × {comm_pct:.2f}% = {_fmt_curr(calc_fee)}\n"
        f"Step 2: Apply maximum cap [1 Mark]: {_fmt_curr(calc_fee)} exceeds the maximum cap of {_fmt_curr(bank['max_fee'])}.\n"
        f"Step 3: Solution [1 Mark]: Fee is capped at: {correct_ans}."
    )
    t1 = "Calculate the percentage fee and compare with the maximum cap."
    t2 = f"{comm_pct:.2f}% of {_fmt_curr(rand_val)} = {_fmt_curr(calc_fee)}, which exceeds {_fmt_curr(bank['max_fee'])}."
    t3 = f"The bank caps the fee at {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_27", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )


def gen_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Exrate 28: Total ZAR payable to the bank when purchasing a fixed foreign amount (Forex in ZAR + Commission)."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)
    foreign_amt = r.choice([1500, 2000, 2500, 3000])
    bsr = round(r.uniform(18.50, 19.20), 4)

    base_zar = foreign_amt * bsr
    comm = max(base_zar * bank["comm_rate"], bank["min_fee"])
    total_zar = round(base_zar + comm, 2)

    prompt = (
        f"{name} visits {bank['name']} to buy ${foreign_amt} (USD) in banknotes for a holiday.\n\n"
        f"Transaction Details:\n"
        f"• Bank Selling Rate (BSR): 1 USD = R {_fmt(bsr, 4)}\n"
        f"• Commission: {bank['comm_rate'] * 100:.2f}% of Rand value (minimum fee {_fmt_curr(bank['min_fee'])})\n\n"
        f"Calculate the TOTAL amount in South African Rands (ZAR) that {name} must pay to the bank."
    )
    correct_ans = _fmt_curr(total_zar)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Base Rand cost [1 Mark]: {foreign_amt} × {bsr:.4f} = {_fmt_curr(base_zar)}\n"
        f"Step 2: Commission [1 Mark]: max({_fmt_curr(base_zar)} × {bank['comm_rate'] * 100:.2f}%, {_fmt_curr(bank['min_fee'])}) = {_fmt_curr(comm)}\n"
        f"Step 3: Total payable [1 Mark]: {_fmt_curr(base_zar)} + {_fmt_curr(comm)} = {correct_ans}"
    )
    t1 = "Total cost = Base Rand cost of foreign currency + Commission fee."
    t2 = f"Base cost = ${foreign_amt} × {bsr:.4f} = {_fmt_curr(base_zar)}. Fee = {_fmt_curr(comm)}."
    t3 = f"Total = {_fmt_curr(base_zar)} + {_fmt_curr(comm)} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_28", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Exrate 29: Net ZAR received from the bank when selling foreign notes (Forex in ZAR - Commission)."""
    name = r.choice(SA_NAMES)
    bank = r.choice(SA_BANKS)
    foreign_amt = r.choice([400, 650, 850, 1100])
    bbr = round(r.uniform(22.80, 23.40), 4)

    gross_zar = foreign_amt * bbr
    comm = max(gross_zar * bank["comm_rate"], bank["min_fee"])
    net_zar = round(gross_zar - comm, 2)

    d_spec_29 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Forex Conversion: GBP to ZAR ({bank['name']})",
        "categories": ["Gross ZAR Value", "Bank Commission", "Net ZAR Payout"],
        "series": [
            {"name": "Amount", "values": [round(gross_zar, 2), round(comm, 2), net_zar]}
        ],
    }

    prompt = (
        f"Refer to the forex exchange rate slip for {name} selling £{foreign_amt} to {bank['name']}.\n\n"
        f"Bank Exchange Conditions:\n"
        f"• Bank Buying Rate (BBR): 1 GBP = R {_fmt(bbr, 4)}\n"
        f"• Commission: {bank['comm_rate'] * 100:.2f}% (minimum fee {_fmt_curr(bank['min_fee'])})\n\n"
        f"Calculate the NET amount in Rands that {name} will receive after the bank fee is deducted."
    )
    correct_ans = _fmt_curr(net_zar)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Gross Rand value [1 Mark]: {foreign_amt} × {bbr:.4f} = {_fmt_curr(gross_zar)}\n"
        f"Step 2: Bank fee [1 Mark]: max({_fmt_curr(gross_zar)} × {bank['comm_rate'] * 100:.2f}%, {_fmt_curr(bank['min_fee'])}) = {_fmt_curr(comm)}\n"
        f"Step 3: Net payout [1 Mark]: {_fmt_curr(gross_zar)} - {_fmt_curr(comm)} = {correct_ans}"
    )
    t1 = "When selling foreign notes, the bank deducts commission from your payout."
    t2 = f"Gross = £{foreign_amt} × {bbr:.4f} = {_fmt_curr(gross_zar)}. Commission = {_fmt_curr(comm)}."
    t3 = f"Net = {_fmt_curr(gross_zar)} - {_fmt_curr(comm)} = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_29", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard",
        diagram_spec=d_spec_29,
    )


def gen_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Exrate 30: Comparing total transaction cost between two South African commercial banks."""
    name = r.choice(SA_NAMES)
    foreign_amt = r.choice([2000, 3000, 4000])
    bsr = round(r.uniform(18.70, 19.10), 4)
    base_zar = foreign_amt * bsr

    # Bank 1: ABSA (1.68%, min R85)
    comm1 = max(base_zar * 0.0168, 85.0)
    total1 = base_zar + comm1

    # Bank 2: Standard Bank (1.85%, min R70)
    comm2 = max(base_zar * 0.0185, 70.0)
    total2 = base_zar + comm2

    diff = round(abs(total1 - total2), 2)
    cheaper_bank = "ABSA Bank" if total1 < total2 else "Standard Bank"

    prompt = (
        f"{name} wants to purchase ${foreign_amt} (USD) and compares two banks at the same BSR of 1 USD = R {_fmt(bsr, 4)}:\n\n"
        f"• Bank A (ABSA): Commission of 1,68% (minimum fee R 85,00)\n"
        f"• Bank B (Standard Bank): Commission of 1,85% (minimum fee R 70,00)\n\n"
        f"Calculate how much {name} saves by choosing the cheaper bank for this transaction."
    )
    correct_ans = _fmt_curr(diff)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Base Rand cost [1 Mark]: ${foreign_amt} × {bsr:.4f} = {_fmt_curr(base_zar)}\n"
        f"Step 2: Compare fees [1 Mark]: Bank A fee = {_fmt_curr(comm1)}; Bank B fee = {_fmt_curr(comm2)}\n"
        f"Step 3: Difference/Savings [1 Mark]: |{_fmt_curr(comm1)} - {_fmt_curr(comm2)}| = {correct_ans} (saving with {cheaper_bank})"
    )
    t1 = "Calculate the commission fee for both banks on the same base Rand amount."
    t2 = f"Bank A fee = {_fmt_curr(comm1)}, Bank B fee = {_fmt_curr(comm2)}."
    t3 = f"Savings = |{_fmt_curr(comm1)} - {_fmt_curr(comm2)}| = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_30", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Exrate 31: Calculating effective commission percentage including fixed handling charge."""
    rand_val = r.choice([15000, 20000, 25000])
    comm_pct = 1.85
    fixed_fee = r.choice([95.0, 110.0, 125.0])

    comm_val = rand_val * (comm_pct / 100.0)
    total_fee = comm_val + fixed_fee
    effective_pct = round((total_fee / rand_val) * 100.0, 2)

    prompt = (
        f"A commercial bureau charges a {comm_pct:.2f}% commission plus a fixed handling charge of {_fmt_curr(fixed_fee)} "
        f"on every foreign exchange transaction.\n\n"
        f"A customer exchanges {_fmt_curr(rand_val)}.\n"
        f"Calculate the effective total fee percentage paid on this transaction, rounded to two decimal places."
    )
    correct_ans = f"{_fmt(effective_pct, 2)}%"
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Total fees in Rands [1 Mark]: ({comm_pct:.2f}% × {_fmt_curr(rand_val)}) + {_fmt_curr(fixed_fee)} = {_fmt_curr(comm_val)} + {_fmt_curr(fixed_fee)} = {_fmt_curr(total_fee)}\n"
        f"Step 2: Effective percentage formula [1 Mark]: (Total Fees ÷ Base Value) × 100%\n"
        f"Step 3: Solution [1 Mark]: ({total_fee:.2f} ÷ {rand_val}) × 100% = {correct_ans}"
    )
    t1 = "Sum the percentage commission and the fixed handling fee."
    t2 = f"Total fee = {_fmt_curr(comm_val)} + {_fmt_curr(fixed_fee)} = {_fmt_curr(total_fee)}."
    t3 = f"Effective % = ({total_fee:.2f} ÷ {rand_val}) × 100% = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_31", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="hard"
    )


def gen_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Exrate 32: Traveler's cheque fee calculation vs cash note fee calculation."""
    rand_val = r.choice([20000, 30000, 40000])
    # Cash notes: 1.85% min R70; TC: 1.71% min R80
    cash_rate, cash_min = 0.0185, 70.0
    tc_rate, tc_min = 0.0171, 80.0

    cash_fee = max(rand_val * cash_rate, cash_min)
    tc_fee = max(rand_val * tc_rate, tc_min)
    diff = round(abs(cash_fee - tc_fee), 2)

    prompt = (
        f"A bank charges the following fees on foreign exchange:\n"
        f"• Banknotes: 1,85% commission (minimum fee R 70,00)\n"
        f"• Travellers' Cheques: 1,71% commission (minimum fee R 80,00)\n\n"
        f"For a transaction of {_fmt_curr(rand_val)}, calculate the difference in fees between purchasing banknotes and Travellers' Cheques."
    )
    correct_ans = _fmt_curr(diff)
    opts, _ = _build_options(correct_ans, r)

    expl = (
        f"Step 1: Banknote fee [1 Mark]: max({_fmt_curr(rand_val)} × 1,85%, R 70,00) = {_fmt_curr(cash_fee)}\n"
        f"Step 2: Travellers' Cheque fee [1 Mark]: max({_fmt_curr(rand_val)} × 1,71%, R 80,00) = {_fmt_curr(tc_fee)}\n"
        f"Step 3: Difference [1 Mark]: |{_fmt_curr(cash_fee)} - {_fmt_curr(tc_fee)}| = {correct_ans}"
    )
    t1 = "Calculate the fee for banknotes, then for Travellers' Cheques, and find the difference."
    t2 = f"Banknotes = {_fmt_curr(cash_fee)}, Travellers' Cheques = {_fmt_curr(tc_fee)}."
    t3 = f"Difference = {correct_ans}."

    return _build_question_payload(
        "exrate_gr12_32", prompt, correct_ans, opts, expl, t1, t2, t3, r, difficulty="medium"
    )
