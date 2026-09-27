"""Fundile Learning - Grade 12 Accounting Financial Indicators Generator.
NSC Accounting Paper 1 Exam Standard: Analysis & Interpretation of Financial Statements.
100% deterministic zero-LLM question generator conforming to the 6-Pillar Contract.

Features:
- Exam Ceiling (mode='compound', 12 marks):
  Calculate and interpret key financial indicators for a public company:
  * Current Ratio (x : 1) and Acid-Test Ratio (x : 1)
  * Debtors Collection Period (days) and Creditors Payment Period (days)
  * Debt-Equity Ratio (x : 1) and financial risk/gearing commentary
  * Return on Shareholders' Equity (ROSHE %) compared against alternate investment benchmarks (8% - 9%)
  * Earnings Per Share (EPS in cents) and Dividends Per Share (DPS in cents)
  * Multi-part interpretive analysis on liquidity, gearing risk, and shareholder satisfaction.
- 2D tabular schema with cell coordinates t0_r{rix}_c{cix} and cell types:
  'required', 'given', 'must_be_empty'.
- Deduction rules: {"rule": "must_be_empty_filled", "penalty": -1}.
- Misconception tags:
  'included_inventory_in_acid_test'
  'inverted_debt_equity_ratio'
  'used_closing_equity_instead_of_average'
  'confused_eps_and_dps'
  'inverted_working_capital_days'
- Adaptive scaffolding sub-drills (3-4 marks each):
  * 'elementary_acid_test' (3 marks)
  * 'elementary_debt_equity' (4 marks)
  * 'elementary_roshe_calc' (4 marks)
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional, Tuple

from ..sa_naming_engine import generate_sa_enterprise


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int) -> str:
    """Format integer/float as South African currency spacing without decimal."""
    rounded = int(round(val))
    return f"{rounded:,}".replace(",", " ")


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _pick_company(r: random.Random) -> str:
    ent = generate_sa_enterprise(r, form="Public Company")
    return ent.get("business_name") or "Khumalo Holdings Ltd"


# ============================================================================
# SUB-DRILL 1: Elementary Acid-Test Ratio (3 Marks)
# ============================================================================
def _build_acid_test_drill(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    year = r.choice([2024, 2025, 2026])

    # Current Assets components
    inv = r.randint(35, 70) * 10000       # R350k - R700k
    debtors = r.randint(25, 55) * 10000   # R250k - R550k
    cash = r.randint(5, 25) * 10000       # R50k - R250k
    curr_assets = inv + debtors + cash

    # Current Liabilities
    curr_liab = r.randint(30, 65) * 10000  # R300k - R650k

    liquid_assets = curr_assets - inv  # debtors + cash
    ratio_val = round(liquid_assets / curr_liab, 2)
    ratio_str = f"{ratio_val:.2f} : 1"

    is_liquid = ratio_val >= 1.0
    liquidity_status = "liquid" if is_liquid else "illiquid / under liquidity pressure"
    evaluation = (
        f"The acid-test ratio is {ratio_str}. Since this is "
        f"{'greater than or equal to' if is_liquid else 'lower than'} the recommended norm of 1.0 : 1, "
        f"the business {'is able' if is_liquid else 'may struggle'} to settle its immediate short-term obligations "
        f"without being forced to sell inventory."
    )

    prompt = (
        f"The following current asset and current liability balances relate to **{company}** "
        f"as at 28 February {year}:\n\n"
        f"• Inventories (Trading stock & consumables): R{_fmt_sa(inv)}\n"
        f"• Trade and other receivables (Debtors): R{_fmt_sa(debtors)}\n"
        f"• Cash and cash equivalents: R{_fmt_sa(cash)}\n"
        f"• Total Current Assets: R{_fmt_sa(curr_assets)}\n"
        f"• Total Current Liabilities: R{_fmt_sa(curr_liab)}\n\n"
        f"**Required:**\n"
        f"1. Calculate the **Acid-Test Ratio** (express as x : 1, rounded to two decimal places).\n"
        f"2. Comment on whether the business can pay its short-term debts without relying on the sale of stock."
    )

    headers = ["Acid-Test Ratio Calculation & Interpretation", "Response"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "Liquid Assets (Current Assets - Inventories)", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": str(liquid_assets), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "Acid-Test Ratio (x : 1)", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": ratio_str, "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "Liquidity Assessment (compare to 1.0 : 1 norm)", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": liquidity_status, "type": "required", "editable": True},
        ],
    ]

    correct_map = {
        "t0_r0_c1": str(liquid_assets),
        "t0_r1_c1": ratio_str,
        "t0_r2_c1": liquidity_status,
    }

    cell_hints = {
        "t0_r0_c1": f"Liquid Assets = Current Assets (R{_fmt_sa(curr_assets)}) - Inventories (R{_fmt_sa(inv)}) = R{_fmt_sa(liquid_assets)}.",
        "t0_r1_c1": f"Acid-Test Ratio = Liquid Assets / Current Liabilities = R{_fmt_sa(liquid_assets)} / R{_fmt_sa(curr_liab)} = {ratio_str}.",
        "t0_r2_c1": f"Compare against 1.0 : 1 norm. The company is {liquidity_status}.",
    }

    return {
        "id": _make_id("acct12_ind_acid"),
        "title": "Liquidity - Acid-Test Ratio",
        "topic": "Financial Indicators",
        "subskill": "elementary_acid_test",
        "mode": "elementary_acid_test",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "marks": 3,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "ideal_answer": f"Acid-test ratio = {ratio_str}; Status: {liquidity_status}",
        "sample_answer": f"Liquid assets: R{_fmt_sa(liquid_assets)} / R{_fmt_sa(curr_liab)} = {ratio_str}. {evaluation}",
        "misconception_tags": [
            "included_inventory_in_acid_test",
            "inverted_acid_test_ratio",
        ],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_liquid_assets", "desc": f"Liquid assets calculated excluding inventory: R{_fmt_sa(liquid_assets)}", "marks": 1, "editable": True},
                {"id": "mp_ratio_val", "desc": f"Correct acid-test ratio: {ratio_str}", "marks": 1, "editable": True},
                {"id": "mp_interp", "desc": f"Valid commentary referencing 1.0 : 1 norm ({liquidity_status})", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "included_inventory_in_acid_test", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Acid-test ratio excludes inventory because inventory cannot be converted into cash immediately.",
            "tier2_directional_rule": "Formula: (Current Assets - Inventories) : Current Liabilities. Express as x : 1.",
            "tier3_worked_step": f"(R{_fmt_sa(curr_assets)} - R{_fmt_sa(inv)}) / R{_fmt_sa(curr_liab)} = R{_fmt_sa(liquid_assets)} / R{_fmt_sa(curr_liab)} = {ratio_str}.",
        },
    }


# ============================================================================
# SUB-DRILL 2: Elementary Debt-Equity Ratio & Gearing (4 Marks)
# ============================================================================
def _build_debt_equity_drill(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    year = r.choice([2024, 2025, 2026])

    # Shareholders' equity: R2.4m - R6.0m
    equity = r.randint(24, 60) * 100000
    # Non-current liabilities (Loan): between 25% and 80% of equity
    loan_pct = r.choice([0.25, 0.35, 0.45, 0.60, 0.75, 1.20])
    loan = int(round(equity * loan_pct))

    de_val = round(loan / equity, 2)
    de_str = f"{de_val:.2f} : 1"

    is_low_geared = de_val < 1.0
    gearing_type = "low geared (favourable gearing)" if is_low_geared else "high geared (unfavourable gearing)"
    risk_level = "low financial risk" if is_low_geared else "high financial risk"
    loan_advice = (
        "The company can safely consider an additional loan because equity substantially exceeds borrowed capital."
        if is_low_geared
        else "The company should NOT take additional loans as debt service commitments are already elevated."
    )

    prompt = (
        f"You are provided with extracts from the Balance Sheet of **{company}** as at 28 February {year}:\n\n"
        f"• Ordinary share capital: R{_fmt_sa(int(equity * 0.75))}\n"
        f"• Retained income: R{_fmt_sa(int(equity * 0.25))}\n"
        f"• Total Ordinary Shareholders' Equity: R{_fmt_sa(equity)}\n"
        f"• Non-current liabilities (Long-term Loan at 11.5% p.a.): R{_fmt_sa(loan)}\n\n"
        f"**Required:**\n"
        f"1. Calculate the **Debt-Equity Ratio** (express as x : 1, rounded to two decimal places).\n"
        f"2. Classify the company's gearing status ({'low geared' if is_low_geared else 'high geared'}).\n"
        f"3. Evaluate the level of financial risk.\n"
        f"4. Advise the directors whether the company should secure an additional loan for business expansion."
    )

    headers = ["Debt-Equity & Gearing Analysis", "Finding / Evaluation"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "Debt-Equity Ratio (x : 1)", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": de_str, "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "Gearing Classification (Low geared / High geared)", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": "Low geared" if is_low_geared else "High geared", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "Financial Risk Assessment", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": risk_level, "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "Recommendation on Additional Loan", "type": "given", "editable": False},
            {"coordinate": "t0_r3_c1", "value": loan_advice, "type": "required", "editable": True},
        ],
    ]

    correct_map = {
        "t0_r0_c1": de_str,
        "t0_r1_c1": "Low geared" if is_low_geared else "High geared",
        "t0_r2_c1": risk_level,
        "t0_r3_c1": loan_advice,
    }

    cell_hints = {
        "t0_r0_c1": f"Debt-Equity Ratio = Non-current Liabilities / Shareholders' Equity = R{_fmt_sa(loan)} / R{_fmt_sa(equity)} = {de_str}.",
        "t0_r1_c1": f"Since ratio ({de_val:.2f} : 1) is {'< 1.0 : 1' if is_low_geared else '> 1.0 : 1'}, the company is {'Low geared' if is_low_geared else 'High geared'}.",
        "t0_r2_c1": f"Level of financial risk is {risk_level}.",
        "t0_r3_c1": loan_advice,
    }

    return {
        "id": _make_id("acct12_ind_de"),
        "title": "Solvency & Risk - Debt-Equity Ratio",
        "topic": "Financial Indicators",
        "subskill": "elementary_debt_equity",
        "mode": "elementary_debt_equity",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "marks": 4,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "ideal_answer": f"Debt-Equity = {de_str}; {gearing_type}; {risk_level}",
        "sample_answer": f"R{_fmt_sa(loan)} : R{_fmt_sa(equity)} = {de_str}. The company is {gearing_type} with {risk_level}. {loan_advice}",
        "misconception_tags": [
            "inverted_debt_equity_ratio",
            "confused_gearing_definition",
        ],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_de_ratio", "desc": f"Correct Debt-Equity ratio calculation: {de_str}", "marks": 1, "editable": True},
                {"id": "mp_de_gear", "desc": f"Accurate gearing classification: {'Low geared' if is_low_geared else 'High geared'}", "marks": 1, "editable": True},
                {"id": "mp_de_risk", "desc": f"Accurate financial risk assessment: {risk_level}", "marks": 1, "editable": True},
                {"id": "mp_de_advice", "desc": "Justified advice on borrowing further capital", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "inverted_debt_equity_ratio", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Debt-Equity measures financial risk: how much borrowed money (debt) is used versus owners' money (equity).",
            "tier2_directional_rule": "Formula: Non-current liabilities : Ordinary shareholders' equity. Below 1.0 : 1 is low geared (favourable).",
            "tier3_worked_step": f"R{_fmt_sa(loan)} / R{_fmt_sa(equity)} = {de_str}. Gearing is {'low' if is_low_geared else 'high'}.",
        },
    }


# ============================================================================
# SUB-DRILL 3: Elementary % Return on Shareholders' Equity (4 Marks)
# ============================================================================
def _build_roshe_drill(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    year = r.choice([2024, 2025, 2026])

    # Shareholders' equity opening: R2.8m - R5.5m
    equity_open = r.randint(28, 55) * 100000
    equity_close = equity_open + r.randint(30, 90) * 10000
    avg_equity = (equity_open + equity_close) / 2.0

    # Net profit after tax target ROSHE: 14% to 24%
    target_pct = r.uniform(0.14, 0.24)
    net_profit_after_tax = int(round(avg_equity * target_pct))
    actual_roshe = round((net_profit_after_tax / avg_equity) * 100.0, 1)

    # Benchmark: alternative bank fixed deposit rate (e.g. 8.0% - 9.0%)
    fd_rate = r.choice([7.5, 8.0, 8.5, 9.0])
    diff_pct = round(actual_roshe - fd_rate, 1)
    is_favourable = actual_roshe > fd_rate

    verdict = (
        f"Shareholders should be satisfied with the return of {actual_roshe:.1f}% as it exceeds "
        f"the alternative risk-free fixed deposit return of {fd_rate:.1f}% by {diff_pct:.1f} percentage points."
        if is_favourable
        else f"Shareholders will NOT be satisfied as {actual_roshe:.1f}% is lower than alternative investment returns."
    )

    prompt = (
        f"You are provided with financial information relating to **{company}** for the year ended 28 February {year}:\n\n"
        f"• Net profit after tax for the year: R{_fmt_sa(net_profit_after_tax)}\n"
        f"• Ordinary shareholders' equity on 1 March {year-1} (Opening balance): R{_fmt_sa(equity_open)}\n"
        f"• Ordinary shareholders' equity on 28 February {year} (Closing balance): R{_fmt_sa(equity_close)}\n"
        f"• Current interest rate on alternative fixed deposits at commercial banks: {fd_rate:.1f}% p.a.\n\n"
        f"**Required:**\n"
        f"1. Calculate the **Average Shareholders' Equity** for the year.\n"
        f"2. Calculate the **% Return on Average Shareholders' Equity (ROSHE)** (round to 1 decimal place).\n"
        f"3. Compare this return to the alternative fixed deposit benchmark and state whether shareholders should be satisfied."
    )

    headers = ["Return on Shareholders' Equity Analysis", "Calculated Value"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "Average Shareholders' Equity (R)", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": str(int(avg_equity)), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "% Return on Average Shareholders' Equity (% ROSHE)", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": f"{actual_roshe:.1f}%", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "Benchmark Comparison vs Fixed Deposit", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": f"Exceeds {fd_rate:.1f}% fixed deposit by {diff_pct:.1f}%", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "Shareholder Satisfaction Conclusion", "type": "given", "editable": False},
            {"coordinate": "t0_r3_c1", "value": "Satisfied" if is_favourable else "Dissatisfied", "type": "required", "editable": True},
        ],
    ]

    correct_map = {
        "t0_r0_c1": str(int(avg_equity)),
        "t0_r1_c1": f"{actual_roshe:.1f}%",
        "t0_r2_c1": f"Exceeds {fd_rate:.1f}% fixed deposit by {diff_pct:.1f}%" if is_favourable else f"Below {fd_rate:.1f}%",
        "t0_r3_c1": "Satisfied" if is_favourable else "Dissatisfied",
    }

    cell_hints = {
        "t0_r0_c1": f"Average Equity = (Opening R{_fmt_sa(equity_open)} + Closing R{_fmt_sa(equity_close)}) / 2 = R{_fmt_sa(int(avg_equity))}.",
        "t0_r1_c1": f"% ROSHE = (Net Profit after Tax / Average Equity) * 100 = (R{_fmt_sa(net_profit_after_tax)} / R{_fmt_sa(int(avg_equity))}) * 100 = {actual_roshe:.1f}%.",
        "t0_r2_c1": f"Compare {actual_roshe:.1f}% with bank fixed deposit rate of {fd_rate:.1f}%.",
        "t0_r3_c1": f"Shareholders are {'Satisfied' if is_favourable else 'Dissatisfied'}.",
    }

    return {
        "id": _make_id("acct12_ind_roshe"),
        "title": "Return on Investment - % ROSHE",
        "topic": "Financial Indicators",
        "subskill": "elementary_roshe_calc",
        "mode": "elementary_roshe_calc",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "marks": 4,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "ideal_answer": f"% ROSHE = {actual_roshe:.1f}%; Shareholders {'satisfied' if is_favourable else 'dissatisfied'}",
        "sample_answer": f"Average Equity = R{_fmt_sa(int(avg_equity))}. ROSHE = {actual_roshe:.1f}%. {verdict}",
        "misconception_tags": [
            "used_closing_equity_instead_of_average",
            "used_profit_before_tax_for_roshe",
        ],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_avg_equity", "desc": f"Average shareholders' equity calculated: R{_fmt_sa(int(avg_equity))}", "marks": 1, "editable": True},
                {"id": "mp_roshe_formula", "desc": "Formula substitution: NPAT / Average Equity * 100", "marks": 1, "editable": True},
                {"id": "mp_roshe_val", "desc": f"Correct ROSHE percentage: {actual_roshe:.1f}%", "marks": 1, "editable": True},
                {"id": "mp_roshe_eval", "desc": f"Comparison to {fd_rate:.1f}% fixed deposit and satisfaction verdict", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "used_closing_equity_instead_of_average", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "ROSHE evaluates how effectively directors used shareholders' funds to generate net profits.",
            "tier2_directional_rule": "Always use Net Profit AFTER Tax divided by AVERAGE equity (Opening + Closing) / 2.",
            "tier3_worked_step": f"Average Equity = R{_fmt_sa(int(avg_equity))}. ROSHE = (R{_fmt_sa(net_profit_after_tax)} / R{_fmt_sa(int(avg_equity))}) * 100 = {actual_roshe:.1f}%.",
        },
    }


# ============================================================================
# EXAM CEILING (MODE: COMPOUND - 12 MARKS): Comprehensive Financial Analysis
# ============================================================================
def _build_compound_financial_indicators(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    year = r.choice([2024, 2025, 2026])

    # 1. Shares & Earnings
    shares_in_issue = r.choice([500_000, 600_000, 800_000, 1_000_000])

    # 2. Income Statement Extracts
    sales = r.randint(60, 110) * 100000  # R6.0m - R11.0m
    credit_sales_pct = r.choice([0.75, 0.80, 0.85])
    credit_sales = int(round(sales * credit_sales_pct))

    cos = int(round(sales * r.choice([0.60, 0.65, 0.70])))
    credit_purchases = int(round(cos * 0.75))

    operating_profit = int(round(sales * r.choice([0.16, 0.18, 0.20])))
    loan_interest_rate = 0.11
    loan_open = r.randint(12, 24) * 100000
    loan_close = loan_open - r.randint(1, 4) * 100000
    interest_expense = int(round(loan_open * loan_interest_rate))

    profit_before_tax = operating_profit - interest_expense
    tax_expense = int(round(profit_before_tax * 0.27))
    npat = profit_before_tax - tax_expense

    # Dividends
    interim_div = int(round(npat * r.choice([0.20, 0.25])))
    final_div = int(round(npat * r.choice([0.25, 0.30])))
    total_dividends = interim_div + final_div

    # 3. Balance Sheet Extracts
    equity_open = r.randint(40, 70) * 100000
    equity_close = equity_open + (npat - total_dividends)
    avg_equity = (equity_open + equity_close) / 2.0

    # Working capital components
    inv_open = r.randint(60, 110) * 10000
    inv_close = r.randint(65, 120) * 10000

    debtors_open = r.randint(40, 75) * 10000
    debtors_close = r.randint(45, 80) * 10000
    avg_debtors = (debtors_open + debtors_close) / 2.0

    cash_close = r.randint(10, 30) * 10000

    total_curr_assets = inv_close + debtors_close + cash_close

    creditors_open = r.randint(35, 65) * 10000
    creditors_close = r.randint(40, 75) * 10000
    avg_creditors = (creditors_open + creditors_close) / 2.0

    sars_close = r.randint(30, 80) * 1000
    div_close = final_div
    total_curr_liab = creditors_close + sars_close + div_close

    # 4. Computed Indicators for Current Year (2026)
    # Current Ratio (x : 1)
    cr_curr = round(total_curr_assets / total_curr_liab, 1)
    cr_prev = round(cr_curr + r.choice([-0.2, 0.2, 0.3]), 1)

    # Acid-Test Ratio (x : 1)
    liquid_curr = total_curr_assets - inv_close
    acid_curr = round(liquid_curr / total_curr_liab, 1)
    acid_prev = round(acid_curr + r.choice([-0.1, 0.1, 0.2]), 1)

    # Debtors Collection Period (days)
    debtors_days_curr = int(round((avg_debtors / credit_sales) * 365))
    debtors_days_prev = debtors_days_curr + r.choice([-4, 5, 8])

    # Creditors Payment Period (days)
    creditors_days_curr = int(round((avg_creditors / credit_purchases) * 365))
    creditors_days_prev = creditors_days_curr + r.choice([-6, 7, 10])

    # Debt-Equity Ratio (x : 1)
    de_curr = round(loan_close / equity_close, 2)
    de_prev = round(de_curr + r.choice([-0.05, 0.08, 0.12]), 2)

    # % ROSHE
    roshe_curr = round((npat / avg_equity) * 100.0, 1)
    roshe_prev = round(roshe_curr + r.choice([-2.1, 1.8, 2.5]), 1)

    # EPS (in cents)
    eps_curr = round((npat / shares_in_issue) * 100.0, 1)
    eps_prev = round(eps_curr * 0.9, 1)

    # DPS (in cents)
    dps_curr = round((total_dividends / shares_in_issue) * 100.0, 1)
    dps_prev = round(dps_curr * 0.9, 1)

    fd_benchmark = 8.5  # Fixed deposit interest rate

    prompt = (
        f"You are provided with financial information relating to **{company}** for the year ended 28 February {year}.\n\n"
        f"**1. Extracts from Financial Statements for the year ended 28 February {year}:**\n"
        f"• Total Sales (Turnover): R{_fmt_sa(sales)} (Credit sales: R{_fmt_sa(credit_sales)})\n"
        f"• Cost of sales: R{_fmt_sa(cos)} (Credit purchases: R{_fmt_sa(credit_purchases)})\n"
        f"• Operating profit: R{_fmt_sa(operating_profit)}\n"
        f"• Interest on loan: R{_fmt_sa(interest_expense)}\n"
        f"• Net profit after tax: R{_fmt_sa(npat)}\n"
        f"• Dividends declared: Interim R{_fmt_sa(interim_div)}; Final R{_fmt_sa(final_div)} (Total R{_fmt_sa(total_dividends)})\n"
        f"• Number of ordinary shares in issue: {shares_in_issue:,} shares\n\n"
        f"**2. Balance Sheet Details (Comparative figures):**\n"
        f"• Ordinary Shareholders' Equity: 1 March {year-1}: R{_fmt_sa(equity_open)}; 28 Feb {year}: R{_fmt_sa(equity_close)}\n"
        f"• Non-current liabilities (Loan): 28 Feb {year}: R{_fmt_sa(loan_close)}\n"
        f"• Current Assets (28 Feb {year}): Total R{_fmt_sa(total_curr_assets)} (Inventories: R{_fmt_sa(inv_close)})\n"
        f"• Trade Debtors: 1 March {year-1}: R{_fmt_sa(debtors_open)}; 28 Feb {year}: R{_fmt_sa(debtors_close)}\n"
        f"• Current Liabilities (28 Feb {year}): Total R{_fmt_sa(total_curr_liab)}\n"
        f"• Trade Creditors: 1 March {year-1}: R{_fmt_sa(creditors_open)}; 28 Feb {year}: R{_fmt_sa(creditors_close)}\n\n"
        f"**3. Additional Market Information:**\n"
        f"• Commercial bank fixed deposit rate: {fd_benchmark}%\n"
        f"• Credit terms: Debtors 30 days; Creditors 60 days\n\n"
        f"**Required:**\n"
        f"1. Complete the table of Financial Indicators for 28 February {year} (Column 2).\n"
        f"2. Answer the interpretive questions regarding liquidity, gearing risk, and shareholder returns."
    )

    headers = [
        "Financial Indicator",
        f"28 Feb {year-1}",
        f"28 Feb {year} (Calculate)",
        "Curriculum Norm / Benchmark",
    ]

    table_rows = [
        # (Description, prev_val, curr_val, benchmark, is_header, is_required)
        ("LIQUIDITY INDICATORS", "", "", "", True, False),
        ("Current Ratio", f"{cr_prev:.1f} : 1", f"{cr_curr:.1f} : 1", "2.0 : 1", False, True),
        ("Acid-Test Ratio", f"{acid_prev:.1f} : 1", f"{acid_curr:.1f} : 1", "1.0 : 1", False, True),
        ("Debtors Collection Period", f"{debtors_days_prev} days", f"{debtors_days_curr} days", "30 days", False, True),
        ("Creditors Payment Period", f"{creditors_days_prev} days", f"{creditors_days_curr} days", "60 days", False, True),
        ("SOLVENCY & GEARING INDICATOR", "", "", "", True, False),
        ("Debt-Equity Ratio", f"{de_prev:.2f} : 1", f"{de_curr:.2f} : 1", "< 1.0 : 1 (Low Risk)", False, True),
        ("PROFITABILITY & RETURN INDICATORS", "", "", "", True, False),
        ("Return on Shareholders' Equity (% ROSHE)", f"{roshe_prev:.1f}%", f"{roshe_curr:.1f}%", f"{fd_benchmark:.1f}% (Fixed Deposit)", False, True),
        ("Earnings Per Share (EPS)", f"{eps_prev:.1f} cents", f"{eps_curr:.1f} cents", "Growth expected", False, True),
        ("Dividends Per Share (DPS)", f"{dps_prev:.1f} cents", f"{dps_curr:.1f} cents", "Payout policy", False, True),
    ]

    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for rix, (desc, p_val, c_val, b_val, is_hdr, is_req) in enumerate(table_rows):
        coord_c0 = f"t0_r{rix}_c0"
        coord_c1 = f"t0_r{rix}_c1"
        coord_c2 = f"t0_r{rix}_c2"
        coord_c3 = f"t0_r{rix}_c3"

        if is_hdr:
            rows.append([
                {"coordinate": coord_c0, "value": desc, "type": "given", "editable": False},
                {"coordinate": coord_c1, "value": "", "type": "must_be_empty", "editable": True},
                {"coordinate": coord_c2, "value": "", "type": "must_be_empty", "editable": True},
                {"coordinate": coord_c3, "value": "", "type": "must_be_empty", "editable": True},
            ])
            correct_map[coord_c1] = ""
            correct_map[coord_c2] = ""
            correct_map[coord_c3] = ""
            cell_hints[coord_c2] = "Section header: leave blank."
        else:
            rows.append([
                {"coordinate": coord_c0, "value": desc, "type": "given", "editable": False},
                {"coordinate": coord_c1, "value": p_val, "type": "given", "editable": False},
                {"coordinate": coord_c2, "value": c_val if not is_req else "", "type": "required" if is_req else "given", "editable": True if is_req else False},
                {"coordinate": coord_c3, "value": b_val, "type": "given", "editable": False},
            ])
            correct_map[coord_c2] = c_val.replace(" ", "")
            cell_hints[coord_c2] = f"{desc} = {c_val}."

    # Pedagogical hints for key cells
    cell_hints["t0_r1_c2"] = f"Current Ratio = Current Assets (R{_fmt_sa(total_curr_assets)}) / Current Liabilities (R{_fmt_sa(total_curr_liab)}) = {cr_curr:.1f} : 1."
    cell_hints["t0_r2_c2"] = f"Acid-Test Ratio = (Current Assets R{_fmt_sa(total_curr_assets)} - Inventory R{_fmt_sa(inv_close)}) / Current Liabilities R{_fmt_sa(total_curr_liab)} = {acid_curr:.1f} : 1."
    cell_hints["t0_r3_c2"] = f"Debtors Collection = (Average Debtors R{_fmt_sa(int(avg_debtors))} / Credit Sales R{_fmt_sa(credit_sales)}) * 365 = {debtors_days_curr} days."
    cell_hints["t0_r4_c2"] = f"Creditors Payment = (Average Creditors R{_fmt_sa(int(avg_creditors))} / Credit Purchases R{_fmt_sa(credit_purchases)}) * 365 = {creditors_days_curr} days."
    cell_hints["t0_r6_c2"] = f"Debt-Equity Ratio = Non-current Liabilities R{_fmt_sa(loan_close)} / Shareholders' Equity R{_fmt_sa(equity_close)} = {de_curr:.2f} : 1."
    cell_hints["t0_r8_c2"] = f"% ROSHE = (NPAT R{_fmt_sa(npat)} / Average Equity R{_fmt_sa(int(avg_equity))}) * 100 = {roshe_curr:.1f}%."
    cell_hints["t0_r9_c2"] = f"EPS = (NPAT R{_fmt_sa(npat)} / {shares_in_issue:,} shares) * 100 = {eps_curr:.1f} cents."
    cell_hints["t0_r10_c2"] = f"DPS = (Total Dividends R{_fmt_sa(total_dividends)} / {shares_in_issue:,} shares) * 100 = {dps_curr:.1f} cents."

    # Commentary answers
    liquidity_commentary = (
        f"Liquidity is {'sound' if acid_curr >= 1.0 else 'under slight pressure'} with acid-test at {acid_curr:.1f} : 1. "
        f"Debtors take {debtors_days_curr} days to pay (target 30 days), while the company pays creditors in {creditors_days_curr} days (target 60 days), "
        f"maintaining a positive working capital cash cycle."
    )
    gearing_commentary = (
        f"The company is low geared with a Debt-Equity ratio of {de_curr:.2f} : 1 (well below the 1.0 : 1 threshold). "
        f"Financial risk is low and the company can safely borrow further capital if needed."
    )
    return_commentary = (
        f"The % ROSHE of {roshe_curr:.1f}% significantly exceeds the alternative fixed deposit rate of {fd_benchmark:.1f}% "
        f"(by {roshe_curr - fd_benchmark:.1f} percentage points). Shareholders should be well satisfied with this return."
    )

    marking_points = [
        {"id": "mp_cr", "desc": f"Current ratio calculated: {cr_curr:.1f} : 1", "marks": 1, "editable": True},
        {"id": "mp_acid", "desc": f"Acid-test ratio calculated: {acid_curr:.1f} : 1", "marks": 1, "editable": True},
        {"id": "mp_debtors_days", "desc": f"Debtors collection period: {debtors_days_curr} days", "marks": 1, "editable": True},
        {"id": "mp_creditors_days", "desc": f"Creditors payment period: {creditors_days_curr} days", "marks": 1, "editable": True},
        {"id": "mp_de", "desc": f"Debt-equity ratio: {de_curr:.2f} : 1", "marks": 1, "editable": True},
        {"id": "mp_roshe", "desc": f"Return on average equity (% ROSHE): {roshe_curr:.1f}%", "marks": 2, "editable": True},
        {"id": "mp_eps", "desc": f"Earnings per share (EPS): {eps_curr:.1f} cents", "marks": 1, "editable": True},
        {"id": "mp_dps", "desc": f"Dividends per share (DPS): {dps_curr:.1f} cents", "marks": 1, "editable": True},
        {"id": "mp_comm_liq", "desc": "Liquidity commentary comparing debtors/creditors cycle to norms", "marks": 1, "editable": True},
        {"id": "mp_comm_gear", "desc": f"Gearing commentary evaluating Debt-Equity ratio ({de_curr:.2f}:1) and financial risk", "marks": 1, "editable": True},
        {"id": "mp_comm_ret", "desc": f"Investment return commentary comparing ROSHE ({roshe_curr:.1f}%) to {fd_benchmark}% fixed deposit", "marks": 1, "editable": True},
    ]

    marking_schema = {
        "total_marks": 12,
        "marking_points": marking_points,
        "deductions": [
            {"rule": "must_be_empty_filled", "penalty": -1},
            {"rule": "included_inventory_in_acid_test", "penalty": -1},
            {"rule": "used_closing_equity_instead_of_average", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    return {
        "id": _make_id("acct12_ind_compound"),
        "title": "Comprehensive Financial Indicator Analysis (Exam Standard)",
        "topic": "Financial Indicators",
        "subskill": "financial_indicators",
        "mode": "compound",
        "difficulty": "hard",
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 20,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 12,
        "ideal_answer": f"CR: {cr_curr:.1f}:1; Acid: {acid_curr:.1f}:1; ROSHE: {roshe_curr:.1f}%; Debt-Equity: {de_curr:.2f}:1; EPS: {eps_curr:.1f}c; DPS: {dps_curr:.1f}c",
        "sample_answer": (
            f"Table completed. Interpretations:\n"
            f"• Liquidity: {liquidity_commentary}\n"
            f"• Gearing & Risk: {gearing_commentary}\n"
            f"• Return: {return_commentary}"
        ),
        "misconception_tags": [
            "included_inventory_in_acid_test",
            "inverted_debt_equity_ratio",
            "used_closing_equity_instead_of_average",
            "confused_eps_and_dps",
        ],
        "marking_schema": marking_schema,
        "hints": {
            "tier1_location": "Calculate the ratios systematically by category: Liquidity, Solvency/Gearing, and Profitability/Return.",
            "tier2_directional_rule": (
                "Remember: Acid-Test excludes inventory; Debtors & Creditors periods use 365 days; "
                "Debt-Equity is Non-current Liabilities : Equity; ROSHE uses AVERAGE Equity."
            ),
            "tier3_worked_step": (
                f"CR = {cr_curr:.1f}:1. Acid = {acid_curr:.1f}:1. Debtors = {debtors_days_curr}d. Creditors = {creditors_days_curr}d. "
                f"Debt-Equity = {de_curr:.2f}:1. ROSHE = {roshe_curr:.1f}%. EPS = {eps_curr:.1f}c. DPS = {dps_curr:.1f}c."
            ),
        },
    }


# ============================================================================
# MASTER DISPATCHER
# ============================================================================
BUILDERS = {
    "compound": _build_compound_financial_indicators,
    "financial_indicators": _build_compound_financial_indicators,
    "elementary_acid_test": _build_acid_test_drill,
    "elementary_debt_equity": _build_debt_equity_drill,
    "elementary_roshe_calc": _build_roshe_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Accounting Financial Indicator questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_financial_indicators)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}


def generate_questions(
    subskill: str = "mixed",
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Adapter for compatibility with multi-item registry generators."""
    res = generate(subskill=subskill, difficulty=difficulty, count=count, seed=seed, mode=mode, **kwargs)
    return res["questions"]
