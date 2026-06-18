"""
vat_generator.py — Grade 12 Term 2
====================================
Value Added Tax (Grade 12 level) question generator.

Archetype classes covered:
  1. VAT control account (T-account)
  2. VAT payable/receivable calculation
  3. VAT on transactions analysis (increase/decrease effect)
  4. VAT inclusive/exclusive calculations
  5. Zero-rated goods in mixed sales
  6. VAT on bad debts / discount allowed
  7. VAT on drawings / donations
  8. Debit/credit side classification
  9. True/False VAT concepts (MCQ)
 10. Fill-in-the-blank (word bank)
 11. Voluntary registration reasoning
 12. Ethics of misusing VAT collections
 13. Creditors allowance VAT effect
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

VAT_RATE = 0.15


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    r.seed() if seed is None else r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _rm(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _money(x: float) -> str:
    return f"R {x:,.2f}"


_BUSINESSES = [
    "Zaba Stores", "Mphati Enterprises", "Nomhle Traders",
    "Chuckle Traders", "Trendy Suppliers", "Mizi Stores",
    "Coastal Trading", "Metro Wholesale", "Summit Retailers",
    "Delta Distributors",
]


def _make_mcq(*, prompt, options, correct_index, explanation):
    return {
        "id": _make_id("acct12_vat_mcq"), "question_type": "mcq",
        "prompt": prompt, "options": options,
        "correct_index": int(correct_index), "explanation": explanation,
        "expected_answer_type": "mcq", "marks": 2,
        "guidelines": [explanation], "visual_aid_key": "vat_gr12",
    }


def _make_typed(*, prompt, sample_answer, grading_rubric=None):
    gr = grading_rubric or []
    return {
        "id": _make_id("acct12_vat_typed"), "question_type": "typed",
        "prompt": prompt, "sample_answer": sample_answer,
        "expected_answer_type": "text", "grading_rubric": gr,
        "marks": 4 if len(gr) >= 2 else 2,
        "guidelines": [f"Include: {', '.join(gr)}"] if gr else [],
        "visual_aid_key": "vat_gr12",
    }


def _make_calc(*, prompt, correct_answer, unit="R", working_formula=""):
    return {
        "id": _make_id("acct12_vat_calc"), "question_type": "calc",
        "prompt": prompt, "correct_value": correct_answer,
        "correct_answer": correct_answer, "unit": unit,
        "working_formula": working_formula, "expected_answer_type": "number",
        "marks": 3, "correct_map": {"answer": correct_answer},
        "rubric_map": {"answer": working_formula},
        "guidelines": [working_formula] if working_formula else [],
        "visual_aid_key": "vat_gr12",
    }


# ---------------------------------------------------------------------------
# VAT payable/receivable
# ---------------------------------------------------------------------------

def _gen_vat_payable(r: random.Random):
    biz = r.choice(_BUSINESSES)
    opening_bal = _rm(r.choice([-1, 1]) * r.randint(2, 10) * 1000)
    bal_label = "due by SARS" if opening_bal > 0 else "owed to SARS"

    purchases_excl = _rm(r.randint(300, 800) * 1000)
    vat_input = _rm(purchases_excl * VAT_RATE)

    sales_incl = _rm(r.randint(500, 1200) * 1000)
    vat_output = _rm(sales_incl * 15 / 115)

    drawings_vat = _rm(r.randint(500, 3000))
    bad_debts_vat = _rm(r.randint(1000, 5000))
    discount_vat = _rm(r.randint(500, 4000))

    # VAT control: debit side vs credit side
    # Debit: opening (if SARS owes us), input VAT, bad debts VAT
    # Credit: output VAT, drawings VAT, discount cancellation
    debit_total = abs(opening_bal) * (1 if opening_bal > 0 else 0) + vat_input + bad_debts_vat
    credit_total = abs(opening_bal) * (1 if opening_bal < 0 else 0) + vat_output + drawings_vat + discount_vat

    result = _rm(credit_total - debit_total)
    result_label = "payable to SARS" if result > 0 else "receivable from SARS"

    return _make_calc(
        prompt=(
            f"{biz}: Calculate the VAT amount payable to or receivable from SARS.\n\n"
            f"• Opening balance: {_money(abs(opening_bal))} ({bal_label})\n"
            f"• Purchases (VAT exclusive): {_money(purchases_excl)}\n"
            f"• Sales (VAT inclusive): {_money(sales_incl)}\n"
            f"• VAT on drawings: {_money(drawings_vat)}\n"
            f"• VAT on bad debts written off: {_money(bad_debts_vat)}\n"
            f"• VAT on discount allowed (to be cancelled): {_money(discount_vat)}"
        ),
        correct_answer=abs(result), unit="R",
        working_formula=(
            f"Output = {_money(vat_output)} + {_money(drawings_vat)} + {_money(discount_vat)}"
            + (f" + {_money(abs(opening_bal))}" if opening_bal < 0 else "") + ". "
            f"Input = {_money(vat_input)} + {_money(bad_debts_vat)}"
            + (f" + {_money(abs(opening_bal))}" if opening_bal > 0 else "") + ". "
            f"Result = {_money(abs(result))} ({result_label})"
        ),
    )


# ---------------------------------------------------------------------------
# VAT inclusive/exclusive calculations
# ---------------------------------------------------------------------------

def _gen_vat_inclusive_calc(r: random.Random):
    biz = r.choice(_BUSINESSES)
    inclusive = _rm(r.randint(1000, 50000))
    vat_amt = _rm(inclusive * 15 / 115)
    exclusive = _rm(inclusive - vat_amt)

    direction = r.choice(["extract", "add"])
    if direction == "extract":
        return _make_calc(
            prompt=(
                f"{biz}: An invoice totals {_money(inclusive)} (VAT inclusive). "
                f"Calculate the VAT amount."
            ),
            correct_answer=vat_amt, unit="R",
            working_formula=f"{_money(inclusive)} × 15/115 = {_money(vat_amt)}",
        )
    else:
        return _make_calc(
            prompt=(
                f"{biz}: Goods cost {_money(exclusive)} (VAT exclusive). "
                f"Calculate the VAT-inclusive amount."
            ),
            correct_answer=inclusive, unit="R",
            working_formula=f"{_money(exclusive)} × 115/100 = {_money(inclusive)}",
        )


def _gen_vat_with_trade_discount(r: random.Random):
    """VAT calculation with trade discount."""
    biz = r.choice(_BUSINESSES)
    invoice_incl = _rm(r.randint(10000, 50000))
    discount_pct = r.choice([5, 10, 15])

    net_excl = _rm(invoice_incl * 100 / 115 * (100 - discount_pct) / 100)
    vat = _rm(net_excl * VAT_RATE)

    return _make_calc(
        prompt=(
            f"{biz}: Bought merchandise on credit. The invoice totalled {_money(invoice_incl)} "
            f"(VAT inclusive). A trade discount of {discount_pct}% was incorrectly "
            f"omitted from the invoice.\n\n"
            f"Calculate the correct VAT amount after applying the trade discount."
        ),
        correct_answer=vat, unit="R",
        working_formula=(
            f"Excl before discount = {_money(invoice_incl)} × 100/115 = {_money(_rm(invoice_incl * 100 / 115))}. "
            f"Net excl = × {100 - discount_pct}/100 = {_money(net_excl)}. "
            f"VAT = {_money(net_excl)} × 15% = {_money(vat)}"
        ),
    )


# ---------------------------------------------------------------------------
# Zero-rated in mixed sales
# ---------------------------------------------------------------------------

def _gen_zero_rated_mixed(r: random.Random):
    biz = r.choice(_BUSINESSES)
    total_sales_excl = _rm(r.randint(500, 1500) * 1000)
    zero_rated_excl = _rm(r.randint(50, 300) * 1000)
    standard_excl = _rm(total_sales_excl - zero_rated_excl)
    vat_on_sales = _rm(standard_excl * VAT_RATE)

    return _make_calc(
        prompt=(
            f"{biz}: Total sales (VAT exclusive) = {_money(total_sales_excl)}, "
            f"including zero-rated goods of {_money(zero_rated_excl)}.\n\n"
            f"Calculate the VAT amount on goods sold."
        ),
        correct_answer=vat_on_sales, unit="R",
        working_formula=(
            f"Standard-rated = {_money(total_sales_excl)} − {_money(zero_rated_excl)} "
            f"= {_money(standard_excl)}. "
            f"VAT = {_money(standard_excl)} × 15% = {_money(vat_on_sales)}"
        ),
    )


# ---------------------------------------------------------------------------
# VAT on bad debts / discount
# ---------------------------------------------------------------------------

def _gen_vat_on_bad_debts(r: random.Random):
    biz = r.choice(_BUSINESSES)
    bad_debts_incl = _rm(r.randint(5000, 50000))
    vat = _rm(bad_debts_incl * 15 / 115)

    return _make_calc(
        prompt=(
            f"{biz}: Debtors' accounts totalling {_money(bad_debts_incl)} (VAT inclusive) "
            f"were written off as bad debts. Calculate the VAT amount that can be "
            f"claimed back from SARS."
        ),
        correct_answer=vat, unit="R",
        working_formula=f"{_money(bad_debts_incl)} × 15/115 = {_money(vat)}",
    )


def _gen_vat_on_discount(r: random.Random):
    biz = r.choice(_BUSINESSES)
    total_discount = _rm(r.randint(5000, 30000))
    vat = _rm(total_discount * 15 / 115)

    type_disc = r.choice(["allowed", "received"])
    if type_disc == "allowed":
        effect = "decrease the amount payable to SARS"
        explanation = "SARS allows the business to claim back the VAT portion of discount allowed"
    else:
        effect = "increase the amount payable to SARS"
        explanation = "Discount received cancels part of the input VAT claimed"

    return _make_calc(
        prompt=(
            f"{biz}: Total discount {type_disc} = {_money(total_discount)}. "
            f"Calculate the VAT amount on the discount {type_disc}."
        ),
        correct_answer=vat, unit="R",
        working_formula=(
            f"{_money(total_discount)} × 15/115 = {_money(vat)}. "
            f"Effect: {effect}"
        ),
    )


# ---------------------------------------------------------------------------
# VAT on drawings / donations
# ---------------------------------------------------------------------------

def _gen_vat_on_drawings(r: random.Random):
    biz = r.choice(_BUSINESSES)
    cost_excl = _rm(r.randint(2000, 15000))
    vat = _rm(cost_excl * VAT_RATE)

    item_type = r.choice(["drawings", "donations"])
    if item_type == "drawings":
        prompt = (
            f"The owner of {biz} took trading stock costing {_money(cost_excl)} "
            f"(VAT exclusive) for personal use. Calculate the VAT on this transaction."
        )
    else:
        prompt = (
            f"{biz} donated trading stock costing {_money(cost_excl)} "
            f"(VAT exclusive) to a local charity. Calculate the output VAT."
        )

    return _make_calc(
        prompt=prompt,
        correct_answer=vat, unit="R",
        working_formula=f"{_money(cost_excl)} × 15% = {_money(vat)}",
    )


# ---------------------------------------------------------------------------
# Transaction analysis (increase/decrease effect)
# ---------------------------------------------------------------------------

def _gen_transaction_effect(r: random.Random):
    biz = r.choice(_BUSINESSES)
    scenarios = [
        {
            "desc": f"Received discount of {_money(17250.0)} when settling a supplier's account",
            "calc": f"{_money(17250.0)} × 15/115 = {_money(2250.0)}",
            "amount": 2250.0,
            "effect": "Increase (cancels input VAT previously claimed)",
        },
        {
            "desc": f"Merchandise of {_money(130000.0)} (VAT exclusive, including zero-rated items of {_money(9200.0)}) sold on credit",
            "calc": f"({_money(130000.0)} − {_money(9200.0)}) × 15% = {_money(18120.0)}",
            "amount": 18120.0,
            "effect": "Increase (output VAT collected)",
        },
        {
            "desc": f"Owner took stock costing {_money(5200.0)} (VAT exclusive) for private use",
            "calc": f"{_money(5200.0)} × 15% = {_money(780.0)}",
            "amount": 780.0,
            "effect": "Increase (output VAT on drawings)",
        },
    ]

    chosen = r.choice(scenarios)
    return _make_calc(
        prompt=(
            f"{biz}: {chosen['desc']}.\n\n"
            f"Calculate the VAT amount and state its effect on the amount payable to SARS."
        ),
        correct_answer=chosen["amount"], unit="R",
        working_formula=f"{chosen['calc']}. Effect: {chosen['effect']}",
    )


# ---------------------------------------------------------------------------
# Concepts
# ---------------------------------------------------------------------------

def _gen_vat_concepts_mcq(r: random.Random):
    qs = [
        {
            "prompt": "EFT payments by debtors should be recorded in the CRJ only after:",
            "options": [
                "Receiving proof of payment or an entry on the bank statement",
                "The debtor confirms by phone",
                "The end of the financial year",
                "The bank reconciliation is completed",
            ],
            "correct": 0,
            "explanation": "EFT payments must be verified with proof or bank statement before recording.",
        },
        {
            "prompt": "Output VAT is classified as:",
            "options": [
                "A current liability (owed to SARS)",
                "A current asset (owed by SARS)",
                "An expense",
                "Revenue",
            ],
            "correct": 0,
            "explanation": "Output VAT is collected on behalf of SARS and must be paid over — it is a current liability.",
        },
        {
            "prompt": "VAT on bad debts will:",
            "options": [
                "Decrease the amount payable to SARS",
                "Increase the amount payable to SARS",
                "Have no effect on VAT payable",
                "Increase input VAT payable",
            ],
            "correct": 0,
            "explanation": "Bad debts reduce output VAT previously collected, so less is owed to SARS.",
        },
        {
            "prompt": "A business with turnover below R1 000 000 that registers for VAT is called:",
            "options": [
                "A voluntary registration",
                "A compulsory registration",
                "An exempt business",
                "A zero-rated vendor",
            ],
            "correct": 0,
            "explanation": "Businesses with turnover below R1 million can voluntarily register for VAT.",
        },
    ]
    chosen = r.choice(qs)
    return _make_mcq(
        prompt=chosen["prompt"], options=chosen["options"],
        correct_index=chosen["correct"], explanation=chosen["explanation"],
    )


def _gen_voluntary_registration(r: random.Random):
    return _make_typed(
        prompt=(
            "A business owner's annual turnover is less than R1 000 000 but "
            "they decided to register for VAT. Give ONE reason why."
        ),
        sample_answer=(
            "The business can claim back input VAT on purchases and expenses. "
            "If the business expects to grow beyond R1 000 000, early registration "
            "avoids penalties. It also shows responsible citizenship — collecting "
            "tax for SARS to improve the economy."
        ),
        grading_rubric=[
            "Can claim input VAT on purchases",
            "Preparation for future growth or responsible citizenship",
        ],
    )


def _gen_ethics_vat_misuse(r: random.Random):
    biz = r.choice(_BUSINESSES)
    return _make_typed(
        prompt=(
            f"The owner of {biz} uses VAT collections to pay business expenses "
            f"and does not have sufficient cash to make VAT payments on time. "
            f"State TWO points advising the owner."
        ),
        sample_answer=(
            "1. This is illegal — using VAT money for business expenses constitutes "
            "tax evasion and can result in penalties, fines, or criminal charges from SARS. "
            "2. The business is acting as an agent of SARS — the money does not belong to "
            "the business. The owner should budget properly and keep VAT funds separate."
        ),
        grading_rubric=[
            "Identified as illegal / tax evasion / penalties",
            "VAT money belongs to SARS — agent relationship",
            "Budget / separate funds advice",
        ],
    )


# ---------------------------------------------------------------------------
# Main entry
# ---------------------------------------------------------------------------

_GENERATORS = [
    _gen_vat_payable,
    _gen_vat_inclusive_calc,
    _gen_vat_with_trade_discount,
    _gen_zero_rated_mixed,
    _gen_vat_on_bad_debts,
    _gen_vat_on_discount,
    _gen_vat_on_drawings,
    _gen_transaction_effect,
    _gen_vat_concepts_mcq,
    _gen_voluntary_registration,
    _gen_ethics_vat_misuse,
]


def generate_questions(
    *, subskill="mixed", difficulty="easy", question_type="mixed",
    count=1, seed=None, mode="",
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    questions = []
    for _ in range(count):
        q = r.choice(_GENERATORS)(r)
        q["difficulty"] = difficulty
        q["mode"] = mode
        questions.append(q)
    return questions
