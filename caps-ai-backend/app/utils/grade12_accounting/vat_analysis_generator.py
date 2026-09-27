"""Fundile Learning — Grades 10, 11 & 12 Accounting: Value Added Tax (VAT) Calculation & Analysis Generator.
NSC Accounting Paper 1 & Paper 2 Standard (10-15 marks).
100% deterministic zero-LLM question generator conforming to the 6-Pillar Contract.

Archetypes sourced from curriculum_docs_auto/Accounting_Gr12/Value added tax.md:
- 15% Standard VAT calculation (Inclusive * 15/115, Exclusive * 15/100)
- Classification of Output VAT vs Input VAT
- Analysis of transactions affecting VAT owed to/receivable from SARS:
  * Cash/credit sales, drawings of stock, bad debts recovered (Output VAT / increases owed)
  * Cash/credit purchases, equipment bought (Input VAT / decreases owed)
  * Returns by debtors, discount allowed, bad debts written off (decreases Output VAT)
  * Returns to suppliers, discount received (decreases Input VAT / increases owed)
- Calculation of net amount payable to SARS or refundable by SARS
- Ethical & legal implications of VAT evasion, non-registration, falsified invoices

Supports compound (12 marks) and elementary sub-drills:
- elementary_vat_calc (3 marks): Inclusive vs Exclusive conversions
- elementary_vat_schedule (5 marks): 2D tabular schedule of transactions affecting SARS
- elementary_vat_ethical (4 marks): VAT ethics, invoice basis, and SARS deadlines
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from ..sa_naming_engine import generate_sa_enterprise


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    r.seed(int(seed) if seed is not None else None)
    return r


def _fmt(val: float | int) -> str:
    rounded = int(round(val))
    return f"{rounded:,}".replace(",", " ")


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


# --------------------------------------------------------------------------- #
# Sub-drill 1: VAT Conversions (3 marks)
# --------------------------------------------------------------------------- #
def _build_vat_calc(r: random.Random) -> Dict[str, Any]:
    ent = generate_sa_enterprise(r, form="Sole Trader")
    biz = ent.get("business_name") or "Sipho's General Dealer"

    # Inclusive item
    excl_base = r.randint(20, 150) * 100
    vat_1 = int(round(excl_base * 0.15))
    incl_val = excl_base + vat_1

    # Exclusive item
    excl_val = r.randint(30, 200) * 100
    vat_2 = int(round(excl_val * 0.15))

    # VAT amount given, find inclusive
    vat_3 = r.randint(15, 90) * 100
    excl_3 = int(round(vat_3 / 0.15))
    incl_3 = excl_3 + vat_3

    prompt = (
        f"**{biz}** is a registered VAT vendor in South Africa. The standard VAT rate is **15%**.\n\n"
        f"**Calculate the missing values for each independent transaction:**\n"
        f"1. Goods sold for **R{_fmt(incl_val)}** (VAT inclusive). Calculate the VAT amount.\n"
        f"2. Equipment purchased for **R{_fmt(excl_val)}** (VAT exclusive). Calculate the VAT amount.\n"
        f"3. An invoice shows VAT charged as **R{_fmt(vat_3)}**. Calculate the total VAT inclusive price."
    )

    correct = {
        "vat_from_inclusive": str(vat_1),
        "vat_from_exclusive": str(vat_2),
        "inclusive_from_vat": str(incl_3),
    }

    return {
        "id": _make_id("vat_calc"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": f"1. R{_fmt(vat_1)}; 2. R{_fmt(vat_2)}; 3. R{_fmt(incl_3)}",
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 8,
        "suggested_duration_mins": 5,
        "learning_objective_id": "acct_vat_conversions",
        "mode": "elementary_vat_calc",
        "misconception_tags": ["net_vs_gross_confusion", "used_15_percent_on_inclusive"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "VAT from inclusive (Amount * 15/115)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "VAT from exclusive (Amount * 15/100)", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Inclusive from VAT (VAT * 115/15)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "VAT inclusive includes 115%. To extract VAT, multiply by 15/115. For VAT exclusive, multiply by 15/100.",
            "tier_2": "Item 1: R{_fmt(incl_val)} * 15/115. Item 2: R{_fmt(excl_val)} * 0.15. Item 3: R{_fmt(vat_3)} * 115/15.",
            "tier_3": f"1. R{_fmt(vat_1)}; 2. R{_fmt(vat_2)}; 3. R{_fmt(incl_3)}.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 2: VAT Transaction Schedule (5 marks)
# --------------------------------------------------------------------------- #
def _build_vat_schedule(r: random.Random) -> Dict[str, Any]:
    ent = generate_sa_enterprise(r, form="Public Company")
    company = ent.get("business_name") or "Vanguard Trading Ltd"
    year = r.choice([2024, 2025, 2026])

    # Sales (Output VAT)
    cash_sales = r.randint(40, 100) * 2300  # multiple of 2300 ensures clean 15/115
    vat_cash_sales = int(cash_sales * 15 / 115)

    credit_sales = r.randint(30, 80) * 2300
    vat_credit_sales = int(credit_sales * 15 / 115)

    # Purchases (Input VAT)
    purchases_excl = r.randint(25, 60) * 2000
    vat_purchases = int(purchases_excl * 0.15)

    # Debtors returns (decreases Output VAT)
    returns_debtors = r.randint(2, 8) * 2300
    vat_returns_debtors = int(returns_debtors * 15 / 115)

    # Drawings of stock (Output VAT)
    drawings_excl = r.randint(5, 15) * 1000
    vat_drawings = int(drawings_excl * 0.15)

    # Net VAT calculation
    net_vat = (vat_cash_sales + vat_credit_sales + vat_drawings) - (vat_purchases + vat_returns_debtors)
    is_payable = net_vat >= 0
    status = "Payable to SARS" if is_payable else "Refundable from SARS"

    prompt = (
        f"**{company}** is registered for VAT on the invoice basis. All amounts include VAT at 15% unless stated.\n"
        f"Transactions for the two-month period ended 30 April {year}:\n\n"
        f"1. Cash sales of merchandise: R{_fmt(cash_sales)}\n"
        f"2. Credit sales of merchandise: R{_fmt(credit_sales)}\n"
        f"3. Trading stock purchased for cash: R{_fmt(purchases_excl)} (VAT EXCLUSIVE)\n"
        f"4. Goods returned by debtors (credit notes issued): R{_fmt(returns_debtors)}\n"
        f"5. Trading stock taken by owner for personal use: R{_fmt(drawings_excl)} (VAT EXCLUSIVE)\n\n"
        f"**Required:** Complete the schedule showing the VAT amount for each transaction and calculate "
        f"the net amount payable to or refundable from SARS."
    )

    headers = ["Transaction", "VAT Output (+)", "VAT Input (-)", "Net Effect on SARS"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "1. Cash sales", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": str(vat_cash_sales), "type": "required", "editable": True},
            {"coordinate": "t0_r0_c2", "value": "-", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r0_c3", "value": f"+{vat_cash_sales}", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "2. Credit sales", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": str(vat_credit_sales), "type": "required", "editable": True},
            {"coordinate": "t0_r1_c2", "value": "-", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r1_c3", "value": f"+{vat_credit_sales}", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "3. Purchases (excl.)", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": "-", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r2_c2", "value": str(vat_purchases), "type": "required", "editable": True},
            {"coordinate": "t0_r2_c3", "value": f"-{vat_purchases}", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "4. Debtors returns", "type": "given", "editable": False},
            {"coordinate": "t0_r3_c1", "value": f"-{vat_returns_debtors}", "type": "required", "editable": True},
            {"coordinate": "t0_r3_c2", "value": "-", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r3_c3", "value": f"-{vat_returns_debtors}", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r4_c0", "value": "5. Drawings of stock", "type": "given", "editable": False},
            {"coordinate": "t0_r4_c1", "value": str(vat_drawings), "type": "required", "editable": True},
            {"coordinate": "t0_r4_c2", "value": "-", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r4_c3", "value": f"+{vat_drawings}", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r5_c0", "value": "NET AMOUNT OWED TO / (REFUNDABLE FROM) SARS", "type": "given", "editable": False},
            {"coordinate": "t0_r5_c1", "value": "-", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r5_c2", "value": "-", "type": "must_be_empty", "editable": False},
            {"coordinate": "t0_r5_c3", "value": str(abs(net_vat)), "type": "required", "editable": True},
        ],
    ]

    correct_map = {
        "t0_r0_c1": str(vat_cash_sales),
        "t0_r0_c3": f"+{vat_cash_sales}",
        "t0_r1_c1": str(vat_credit_sales),
        "t0_r1_c3": f"+{vat_credit_sales}",
        "t0_r2_c2": str(vat_purchases),
        "t0_r2_c3": f"-{vat_purchases}",
        "t0_r3_c1": f"-{vat_returns_debtors}",
        "t0_r3_c3": f"-{vat_returns_debtors}",
        "t0_r4_c1": str(vat_drawings),
        "t0_r4_c3": f"+{vat_drawings}",
        "t0_r5_c3": str(abs(net_vat)),
        "status": status,
    }

    return {
        "id": _make_id("vat_schedule"),
        "question_type": "tabular_fill",
        "question_text": prompt,
        "correct_answer": correct_map,
        "sample_answer": f"Net VAT: R{_fmt(abs(net_vat))} ({status})",
        "table_schema": {"headers": headers, "rows": rows},
        "marks": 5,
        "term": 1,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 8,
        "learning_objective_id": "acct_vat_schedule",
        "mode": "elementary_vat_schedule",
        "misconception_tags": ["input_output_vat_inversion", "drawings_treated_as_input_vat", "omitted_vat_from_returns"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Output VAT on sales and drawings", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Input VAT on purchases", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Adjustment for debtors returns", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Net VAT amount and classification (payable/refundable)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Output VAT is collected on sales and drawings (owed to SARS). Input VAT is paid on purchases (claimable from SARS).",
            "tier_2": "Sales: Amount * 15/115. Purchases (excl): Amount * 0.15. Drawings (excl): Amount * 0.15. Returns: decreases Output VAT.",
            "tier_3": f"Net VAT = Total Output (R{_fmt(vat_cash_sales + vat_credit_sales + vat_drawings - vat_returns_debtors)}) - Input (R{_fmt(vat_purchases)}) = R{_fmt(net_vat)} ({status}).",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 3: VAT Ethics & Invoicing (4 marks)
# --------------------------------------------------------------------------- #
def _build_vat_ethical(r: random.Random) -> Dict[str, Any]:
    ent = generate_sa_enterprise(r, form="Sole Trader")
    owner = ent.get("owner_name") or "Mr. Dlamini"
    biz = ent.get("business_name") or "Dlamini Spaza & Wholesale"

    prompt = (
        f"**Scenario:**\n"
        f"**{owner}**, owner of **{biz}**, had an annual turnover of R1 450 000 this year. "
        f"He tells his bookkeeper that he does not want to register for VAT because 'it will make my prices "
        f"15% higher than competitors, and paying money to SARS reduces my profit.' Furthermore, when selling "
        f"large orders for cash, he offers customers a 10% discount if they agree not to ask for a tax invoice.\n\n"
        f"**Required:**\n"
        f"1. Explain why {owner} is legally obligated to register for VAT in South Africa.\n"
        f"2. Explain why his statement 'paying VAT to SARS reduces my profit' is conceptually incorrect.\n"
        f"3. Comment on the ethical and legal implications of offering discounts for transactions without a tax invoice."
    )

    return {
        "id": _make_id("vat_ethics"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": {
            "point_1": "Turnover exceeds the compulsory threshold of R1 000 000 per year; registration is mandatory by law.",
            "point_2": "The business acts merely as an agent collecting VAT on behalf of SARS; VAT is not an expense of the business.",
            "point_3": "Failing to issue invoices and record cash sales is tax evasion (illegal fraud) and contravenes the Tax Administration Act.",
        },
        "sample_answer": "1. Turnover > R1m (compulsory). 2. Business is an agent; VAT is not an expense. 3. Tax evasion / fraud.",
        "marks": 4,
        "term": 1,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "learning_objective_id": "acct_vat_ethics",
        "mode": "elementary_vat_ethical",
        "misconception_tags": ["vat_treated_as_business_expense", "confused_voluntary_compulsory_threshold"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Compulsory registration threshold (> R1 000 000)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Agency role of business (not an expense)", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Tax evasion / legal consequences", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Internal control failure of unrecorded cash", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Recall the two thresholds: voluntary (R50 000) vs compulsory (R1 000 000).",
            "tier_2": "Whose money is VAT? Does it belong to the owner, or is the business merely collecting on behalf of SARS?",
            "tier_3": "Compulsory threshold is R1 000 000. VAT collected from customers belongs to SARS. Selling without tax invoices is criminal tax evasion.",
        },
    }


# --------------------------------------------------------------------------- #
# COMPOUND: Full VAT Exam Question (12 marks)
# --------------------------------------------------------------------------- #
def _build_compound(r: random.Random) -> List[Dict[str, Any]]:
    return [
        _build_vat_calc(r),
        _build_vat_schedule(r),
        _build_vat_ethical(r),
    ]


# --------------------------------------------------------------------------- #
# PUBLIC API
# --------------------------------------------------------------------------- #
def generate(
    seed: Optional[int] = None,
    count: int = 1,
    mode: str = "compound",
    subskill: str = "mixed",
    difficulty: str = "medium",
    **kwargs,
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    questions: List[Dict[str, Any]] = []

    builders = {
        "elementary_vat_calc": _build_vat_calc,
        "elementary_vat_schedule": _build_vat_schedule,
        "elementary_vat_ethical": _build_vat_ethical,
    }

    for _ in range(count):
        sub_r = _rng(r.randint(1, 1_000_000_000))
        if mode == "compound":
            questions.extend(_build_compound(sub_r))
        elif mode in builders:
            questions.append(builders[mode](sub_r))
        else:
            questions.extend(_build_compound(sub_r))

    return questions
