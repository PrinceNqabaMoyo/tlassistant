"""Fundile Learning — Grade 11 & 12 Accounting: Debtors Age Analysis & Internal Control Generator.
NSC Accounting Paper 1 & Paper 2 Standard (10-15 marks).
100% deterministic zero-LLM question generator conforming to the 6-Pillar Contract.

Archetypes sourced from curriculum_docs_auto/Accounting_Gr12/Debtors age analysis.md:
- Preparation of Debtors Age Analysis table (Current / 30 Days / 60 Days / 90+ Days)
- Calculation of total overdue debt and percentage overdue
- Identification of delinquent debtors exceeding credit limits or credit terms (e.g. 30 days)
- Internal control & credit management recommendations (charging interest, stopping credit, legal action)
- Impact on cash flow and bad debts provision

Supports compound (12 marks) and elementary sub-drills:
- elementary_age_breakdown (5 marks)
- elementary_credit_limit_check (3 marks)
- elementary_internal_control_advice (4 marks)
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


SA_DEBTORS = [
    ("M. Zulu", 15000),
    ("T. Ndlovu", 25000),
    ("C. Van der Merwe", 40000),
    ("B. Adams", 12000),
    ("S. Pillay", 30000),
    ("N. Khumalo", 20000),
    ("F. Botha", 35000),
    ("P. Dlamini", 18000),
]


# --------------------------------------------------------------------------- #
# Sub-drill 1: Debtors Age Analysis Table Fill & Overdue Calc (5 marks)
# --------------------------------------------------------------------------- #
def _build_age_breakdown(r: random.Random) -> Dict[str, Any]:
    ent = generate_sa_enterprise(r, form="Public Company")
    company = ent.get("business_name") or "Apex Retailers Ltd"
    year = r.choice([2024, 2025, 2026])
    month = r.choice(["April", "May", "June", "September", "October"])

    # Pick 4 debtors
    debtors_sample = r.sample(SA_DEBTORS, 4)
    rows_data = []
    headers = ["Debtor", "Credit Limit", "Total Balance", "Current", "30 Days", "60 Days", "90+ Days"]

    total_balance = 0
    total_current = 0
    total_30 = 0
    total_60 = 0
    total_90 = 0

    table_rows = []
    correct_map = {}

    for rix, (name, limit) in enumerate(debtors_sample):
        # Generate ages
        curr = r.randint(15, 60) * 100
        d30 = r.randint(10, 45) * 100
        d60 = r.randint(5, 30) * 100 if r.random() > 0.3 else 0
        d90 = r.randint(5, 25) * 100 if r.random() > 0.4 else 0
        tot = curr + d30 + d60 + d90

        total_balance += tot
        total_current += curr
        total_30 += d30
        total_60 += d60
        total_90 += d90

        row = [
            {"coordinate": f"t0_r{rix}_c0", "value": name, "type": "given", "editable": False},
            {"coordinate": f"t0_r{rix}_c1", "value": f"R{_fmt(limit)}", "type": "given", "editable": False},
            {"coordinate": f"t0_r{rix}_c2", "value": str(tot), "type": "given", "editable": False},
            {"coordinate": f"t0_r{rix}_c3", "value": str(curr), "type": "required", "editable": True},
            {"coordinate": f"t0_r{rix}_c4", "value": str(d30), "type": "required", "editable": True},
            {"coordinate": f"t0_r{rix}_c5", "value": str(d60), "type": "required", "editable": True},
            {"coordinate": f"t0_r{rix}_c6", "value": str(d90), "type": "required", "editable": True},
        ]
        table_rows.append(row)
        correct_map[f"t0_r{rix}_c3"] = str(curr)
        correct_map[f"t0_r{rix}_c4"] = str(d30)
        correct_map[f"t0_r{rix}_c5"] = str(d60)
        correct_map[f"t0_r{rix}_c6"] = str(d90)

    # Totals row
    tot_row_idx = len(debtors_sample)
    table_rows.append([
        {"coordinate": f"t0_r{tot_row_idx}_c0", "value": "TOTAL", "type": "given", "editable": False},
        {"coordinate": f"t0_r{tot_row_idx}_c1", "value": "-", "type": "must_be_empty", "editable": False},
        {"coordinate": f"t0_r{tot_row_idx}_c2", "value": str(total_balance), "type": "required", "editable": True},
        {"coordinate": f"t0_r{tot_row_idx}_c3", "value": str(total_current), "type": "required", "editable": True},
        {"coordinate": f"t0_r{tot_row_idx}_c4", "value": str(total_30), "type": "required", "editable": True},
        {"coordinate": f"t0_r{tot_row_idx}_c5", "value": str(total_60), "type": "required", "editable": True},
        {"coordinate": f"t0_r{tot_row_idx}_c6", "value": str(total_90), "type": "required", "editable": True},
    ])
    correct_map[f"t0_r{tot_row_idx}_c2"] = str(total_balance)
    correct_map[f"t0_r{tot_row_idx}_c3"] = str(total_current)
    correct_map[f"t0_r{tot_row_idx}_c4"] = str(total_30)
    correct_map[f"t0_r{tot_row_idx}_c5"] = str(total_60)
    correct_map[f"t0_r{tot_row_idx}_c6"] = str(total_90)

    overdue_amount = total_60 + total_90
    overdue_pct = round(overdue_amount / total_balance * 100, 1) if total_balance > 0 else 0.0

    prompt = (
        f"You are reviewing the debtors ledger of **{company}** for the month ended {month} {year}.\n"
        f"The credit term granted to debtors is strictly **30 days**.\n\n"
        f"**Required:**\n"
        f"1. Complete the Debtors Age Analysis totals row.\n"
        f"2. Calculate the total amount overdue (debts outstanding for 60 days or longer).\n"
        f"3. Calculate the percentage of total debtors' balances that is overdue (round to 1 decimal place)."
    )

    correct_map["overdue_amount"] = str(overdue_amount)
    correct_map["overdue_pct"] = str(overdue_pct)

    return {
        "id": _make_id("debtors_age_breakdown"),
        "question_type": "tabular_fill",
        "question_text": prompt,
        "correct_answer": correct_map,
        "sample_answer": f"Total Overdue: R{_fmt(overdue_amount)} ({overdue_pct}% of total)",
        "table_schema": {"headers": headers, "rows": table_rows},
        "marks": 5,
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 8,
        "learning_objective_id": "acct12_debtors_age_analysis",
        "mode": "elementary_age_breakdown",
        "misconception_tags": ["included_30_days_in_overdue", "overdue_percentage_base_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Column totals for Current, 30d, 60d, 90d+", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Total debtors balance calculation", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Overdue amount (60d + 90d+)", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Overdue percentage calculation", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Debts are overdue if they exceed the 30-day credit period (i.e. 60 days and 90+ days).",
            "tier_2": "Overdue amount = (Total 60 days + Total 90+ days). Percentage = Overdue ÷ Total Balance × 100.",
            "tier_3": f"Overdue = R{_fmt(total_60)} + R{_fmt(total_90)} = R{_fmt(overdue_amount)}. Overdue % = {overdue_pct}%.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 2: Credit Limit Check & Delinquent Identification (3 marks)
# --------------------------------------------------------------------------- #
def _build_credit_limit_check(r: random.Random) -> Dict[str, Any]:
    debtor_name, limit = r.choice(SA_DEBTORS)
    curr = r.randint(5, 15) * 1000
    d30 = r.randint(4, 12) * 1000
    d60 = r.randint(3, 10) * 1000
    d90 = r.randint(2, 8) * 1000
    total = curr + d30 + d60 + d90

    exceeds_limit = total > limit
    excess = total - limit if exceeds_limit else 0

    prompt = (
        f"Debtor **{debtor_name}** has an authorized credit limit of **R{_fmt(limit)}**.\n"
        f"The age analysis shows:\n"
        f"• Current: R{_fmt(curr)}\n"
        f"• 30 days: R{_fmt(d30)}\n"
        f"• 60 days: R{_fmt(d60)}\n"
        f"• 90+ days: R{_fmt(d90)}\n"
        f"• Total balance: R{_fmt(total)}\n\n"
        f"**Required:**\n"
        f"1. Has {debtor_name} exceeded the authorized credit limit? If yes, by how much?\n"
        f"2. Identify the proportion of this debtor's balance that has been outstanding beyond 30 days."
    )

    overdue_debt = d60 + d90
    overdue_pct = round(overdue_debt / total * 100, 1)

    correct = {
        "exceeds": "Yes" if exceeds_limit else "No",
        "excess_amount": str(excess),
        "overdue_percentage": f"{overdue_pct}%",
    }

    return {
        "id": _make_id("debtor_credit_limit"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": f"Exceeded: {'Yes by R' + _fmt(excess) if exceeds_limit else 'No'}; Overdue: {overdue_pct}%",
        "marks": 3,
        "term": 3,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "learning_objective_id": "acct12_credit_limits",
        "mode": "elementary_credit_limit_check",
        "misconception_tags": ["confused_credit_limit_with_terms", "forgot_90_days_in_overdue"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification of credit limit status", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Calculation of excess amount", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Calculation of proportion overdue", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": f"Compare Total Balance (R{_fmt(total)}) to Credit Limit (R{_fmt(limit)}).",
            "tier_2": "Debts beyond 30 days = 60 days + 90+ days.",
            "tier_3": f"Balance R{_fmt(total)} {'exceeds' if exceeds_limit else 'is within'} limit R{_fmt(limit)} by R{_fmt(excess)}. Overdue = {overdue_pct}%.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 3: Internal Control & Remedial Advice (4 marks)
# --------------------------------------------------------------------------- #
def _build_internal_control_advice(r: random.Random) -> Dict[str, Any]:
    debtor_name, limit = r.choice(SA_DEBTORS)
    days_choice = r.choice(["60", "90+"])

    prompt = (
        f"Debtor **{debtor_name}** has failed to make any payment for the past {days_choice} days, "
        f"despite several phone calls and reminder statements sent by the credit controller.\n\n"
        f"**Required:** Provide **TWO** distinct internal control actions and **TWO** credit management "
        f"policies that the business should immediately implement regarding {debtor_name}."
    )

    remedies = [
        "Stop all further credit sales to this debtor immediately (freeze the account).",
        "Charge interest on overdue accounts at a specified rate (e.g. prime + 2%).",
        "Issue a final letter of demand requesting settlement within 7 days.",
        "Hand the account over to collection attorneys or a debt collection agency.",
        "Offer a small settlement discount for immediate full settlement.",
        "Request the debtor sign an acknowledgement of debt (AOD) with a monthly repayment plan.",
    ]

    return {
        "id": _make_id("debtor_control_advice"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": {
            "action_1": remedies[0],
            "action_2": remedies[1],
            "action_3": remedies[2],
            "action_4": remedies[3],
        },
        "sample_answer": f"1. Freeze credit; 2. Charge interest; 3. Letter of demand; 4. Hand over to collectors.",
        "marks": 4,
        "term": 3,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "learning_objective_id": "acct12_debtor_internal_control",
        "mode": "elementary_internal_control_advice",
        "misconception_tags": ["vague_unactionable_advice", "confused_bad_debts_with_recovery"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "First valid internal control action", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Second valid internal control action", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Third valid credit policy measure", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Fourth valid credit policy measure", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Consider what happens to the debtor's buying ability when their account is overdue.",
            "tier_2": "Effective controls: freeze account, charge interest, letter of demand, legal hand-over.",
            "tier_3": "Valid points: Stop credit sales, charge overdue interest, send final demand, hand over to attorneys.",
        },
    }


# --------------------------------------------------------------------------- #
# COMPOUND: Full Debtors Age Analysis & Control Question (12 marks)
# --------------------------------------------------------------------------- #
def _build_compound(r: random.Random) -> List[Dict[str, Any]]:
    return [
        _build_age_breakdown(r),
        _build_credit_limit_check(r),
        _build_internal_control_advice(r),
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
        "elementary_age_breakdown": _build_age_breakdown,
        "elementary_credit_limit_check": _build_credit_limit_check,
        "elementary_internal_control_advice": _build_internal_control_advice,
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
