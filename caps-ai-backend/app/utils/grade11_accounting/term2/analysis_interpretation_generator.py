"""
analysis_interpretation_generator.py — Grade 11 Term 2
=======================================================
Partnership: Analysis and Interpretation of Financial Statements.

Archetype classes covered:
  1. Profitability ratios (GP%, NP%, OpExp%, OpProfit%)
  2. Liquidity ratios (current, acid test)
  3. Stock management (turnover rate, holding period)
  4. Debtors collection period / creditors payment period
  5. Solvency ratio
  6. Debt-equity ratio (gearing)
  7. Partner's earnings
  8. Return on partner's equity
  9. Return on equity for business
 10. Interest rate back-calculation
 11. Salary increase % calculation
 12. Vehicle profitability analysis
 13. Asset carrying value & disposal
 14. Liquidity/solvency commentary
 15. Loan eligibility with gearing
 16. Partnership concepts (MCQ)
 17. Internal control for fixed assets
 18. Ethics of asset misuse
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from ...sole_trader.core import fmt_money as _fmt_money
from ...sole_trader.core import make_id as _make_id
from ...sole_trader.core import round_money as _round_money
from ...sole_trader.journal_question import make_journal as _make_journal
from ...sole_trader.journal_table import build_prefixed_row as _build_prefixed_row
from ...sole_trader.journal_table import journal_editable_cols_by_difficulty as _journal_editable_cols_by_difficulty



# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _round_money(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _money(x: float) -> str:
    return f"R {x:,.2f}"


def _pct(x: float, dp: int = 1) -> str:
    return f"{round(x, dp)}%"


# ---------------------------------------------------------------------------
# Pools
# ---------------------------------------------------------------------------

_BUSINESS_NAMES = [
    "On-The-Move Couriers", "Highveld Trading", "Cape Traders",
    "Westside Partners", "Summit Wholesale", "Valley Enterprises",
    "Metro Distributors", "Sunrise Suppliers", "Eastgate Stores",
]

_PARTNER_FIRST = ["Jacob", "Thabo", "Maria", "Sarah", "Bongani", "Sipho", "Refilwe"]
_PARTNER_LAST = ["Morris", "Jabulani", "Naidoo", "Khan", "Mokoena", "Zulu", "Pillay"]


def _partner_name(r: random.Random) -> str:
    return f"{r.choice(_PARTNER_FIRST)} {r.choice(_PARTNER_LAST)}"


# ---------------------------------------------------------------------------
# Question factories
# ---------------------------------------------------------------------------


def _mk_journal_table(
    *,
    prompt: str,
    journal_type: str,
    headers: List[str],
    values_rows: List[List[Optional[str]]],
    difficulty: str,
    mode: str,
    base_editable_cols: List[int],
    force_editable_cols: Optional[List[int]] = None,
    title_fields: Optional[List[Dict[str, Any]]] = None,
    archetype_key: str = "",
    rubric_map: Optional[Dict[str, Dict[str, Any]]] = None,
    dependency_map: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    diff = str(difficulty or "easy").strip().lower()
    mode_norm = str(mode or "").strip().lower()

    if force_editable_cols is not None:
        editable_cols = [int(c) for c in force_editable_cols]
    else:
        editable_cols = _journal_editable_cols_by_difficulty(
            difficulty=diff,
            base_editable_cols=base_editable_cols,
            total_cols=len(headers),
            mode=mode_norm,
        )

    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, Any] = {}
    for rix, vals in enumerate(values_rows):
        editable_set = set(int(c) for c in editable_cols)
        display = [
            ("" if int(cix) in editable_set else ("" if v0 is None else str(v0)))
            for cix, v0 in enumerate(vals)
        ]
        rows.append(_build_prefixed_row(table_index=0, row_index=rix, values=display, editable_cols=editable_cols))
        for cix, v0 in enumerate(vals):
            correct_map[f"t0_r{int(rix)}_c{int(cix)}"] = "" if v0 is None else str(v0)

    out = _make_journal(
        prompt=prompt,
        journal_type=journal_type,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        guidelines=[
            "Use the correct row labels and structure.",
            "Calculate the ratios and percentages correctly.",
        ],
        table_variant="grade_project",
        title_fields=title_fields,
        rubric_map=rubric_map,
        dependency_map=dependency_map,
    )
    out["id"] = _make_id("acct11_anal_tbl_gen")
    out["expected_answer_type"] = "journal"
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    return out


def _make_mcq(*, prompt: str, options: List[str], correct_index: int,
              explanation: str) -> Dict[str, Any]:
    return {
        "id": _make_id("acct11_anal_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "expected_answer_type": "mcq",
        "marks": 2,
        "guidelines": [explanation],
        "visual_aid_key": "analysis_interpretation",
    }


def _make_typed(*, prompt: str, sample_answer: str,
                grading_rubric: Optional[List[str]] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("acct11_anal_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer_type": "text",
        "grading_rubric": grading_rubric or [],
        "marks": 4 if grading_rubric and len(grading_rubric) >= 2 else 2,
        "guidelines": [f"Ensure your answer includes: {', '.join(grading_rubric)}"] if grading_rubric else [],
        "visual_aid_key": "analysis_interpretation",
    }


def _make_calc(*, prompt: str, correct_answer: float, unit: str = "R",
               working_formula: str = "") -> Dict[str, Any]:
    return {
        "id": _make_id("acct11_anal_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": correct_answer,
        "correct_answer": correct_answer,
        "unit": unit,
        "working_formula": working_formula,
        "expected_answer_type": "number",
        "marks": 3,
        "correct_map": {"answer": correct_answer},
        "rubric_map": {"answer": working_formula},
        "guidelines": [working_formula] if working_formula else [],
        "visual_aid_key": "analysis_interpretation",
    }


# ---------------------------------------------------------------------------
# Profitability ratios
# ---------------------------------------------------------------------------



def _make_liquidity_ratios_table(r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    year = r.choice([2023, 2024])
    
    trading_stock = _round_money(r.randint(20, 80) * 1000)
    debtors = _round_money(r.randint(15, 60) * 1000)
    bank = _round_money(r.randint(5, 40) * 1000)
    current_assets = _round_money(trading_stock + debtors + bank)
    
    creditors = _round_money(r.randint(10, 40) * 1000)
    bank_od = 0 if bank > 0 else _round_money(r.randint(10, 30) * 1000)
    current_liab = _round_money(creditors + bank_od)

    cr_ratio = round(current_assets / current_liab, 1) if current_liab > 0 else 0
    at_ratio = round((debtors + bank) / current_liab, 1) if current_liab > 0 else 0

    headers = ["Financial Indicator", "Calculation", f"Ratio for {year}"]
    rows = [
        ["Current ratio", f"{current_assets} : {current_liab}", f"{cr_ratio} : 1"],
        ["Acid test ratio", f"{debtors + bank} : {current_liab}", f"{at_ratio} : 1"],
    ]

    prompt = f"""{biz}

#### REQUIRED:
Calculate the liquidity ratios for the year ended 28 February {year}. Show your calculation and express the final answer as a ratio (e.g. X : 1).

#### INFORMATION:
The following appeared in the Balance Sheet of {biz} for the year ended 28 February {year}:
• Trading stock: {_money(trading_stock)}
• Debtors control: {_money(debtors)}
• Bank (favourable): {_money(bank)}
• Creditors control: {_money(creditors)}"""

    return _mk_journal_table(
        prompt=prompt,
        journal_type="analysis_liquidity_table",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2],
        title_fields=[{"label": biz, "value": "Liquidity Indicators"}],
        archetype_key="g11_analysis_liquidity",
    )

def _make_profitability_indicators_table(r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    year = r.choice([2023, 2024])
    
    sales = _round_money(r.randint(2000, 8000) * 1000)
    cost_of_sales = _round_money(sales * r.uniform(0.45, 0.75))
    gp = _round_money(sales - cost_of_sales)
    gp_pct = round(gp / sales * 100, 1)
    
    op_exp = _round_money(sales * r.uniform(0.20, 0.45))
    op_exp_pct = round(op_exp / sales * 100, 1)
    
    net_profit = _round_money(sales * r.uniform(0.05, 0.20))
    np_pct = round(net_profit / sales * 100, 1)

    headers = ["Financial Indicator", f"Value for {year}"]
    rows = [
        ["Gross profit % on sales", f"{gp_pct}%"],
        ["Operating expenses % on sales", f"{op_exp_pct}%"],
        ["Net profit % on sales", f"{np_pct}%"],
    ]

    prompt = f"""{biz}

#### REQUIRED:
Calculate the profitability indicators as a percentage of sales (rounded to one decimal place).

#### INFORMATION:
{biz} had the following figures for the year ended 28 February {year}:
• Sales: {_money(sales)}
• Cost of sales: {_money(cost_of_sales)}
• Operating expenses: {_money(op_exp)}
• Net profit: {_money(net_profit)}"""

    return _mk_journal_table(
        prompt=prompt,
        journal_type="analysis_profitability_table",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1],
        title_fields=[{"label": biz, "value": "Profitability Indicators"}],
        archetype_key="g11_analysis_profitability",
    )

def _make_solvency_and_risk_table(r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    year = r.choice([2023, 2024])
    
    total_assets = _round_money(r.randint(1000, 3000) * 1000)
    current_liab = _round_money(r.randint(100, 400) * 1000)
    ncl = _round_money(r.randint(300, 800) * 1000)
    total_liab = current_liab + ncl
    
    equity = _round_money(total_assets - total_liab)
    
    solvency_ratio = round(total_assets / total_liab, 1) if total_liab > 0 else 0
    debt_equity_ratio = round(ncl / equity, 1) if equity > 0 else 0

    headers = ["Financial Indicator", "Calculation", f"Ratio for {year}"]
    rows = [
        ["Solvency ratio", f"{total_assets} : {total_liab}", f"{solvency_ratio} : 1"],
        ["Debt-equity ratio", f"{ncl} : {equity}", f"{debt_equity_ratio} : 1"],
    ]

    prompt = f"""{biz}

#### REQUIRED:
Calculate the solvency and risk (gearing) ratios for the year ended 28 February {year}. Show your calculation and express the final answer as a ratio (e.g. X : 1).

#### INFORMATION:
The following appeared in the Balance Sheet of {biz} for the year ended 28 February {year}:
• Total assets: {_money(total_assets)}
• Owner's equity: {_money(equity)}
• Non-current liabilities: {_money(ncl)}
• Current liabilities: {_money(current_liab)}"""

    return _mk_journal_table(
        prompt=prompt,
        journal_type="analysis_solvency_risk_table",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2],
        title_fields=[{"label": biz, "value": "Solvency & Risk Indicators"}],
        archetype_key="g11_analysis_solvency_risk",
    )


def _make_partner_returns_table(r: random.Random, difficulty: str = "easy", mode: str = "") -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    year = r.choice([2023, 2024])
    
    p1 = _partner_name(r)
    p2 = _partner_name(r)
    
    # Partner 1
    int_cap_1 = _round_money(r.randint(30, 60) * 1000)
    sal_1 = _round_money(r.randint(120, 200) * 1000)
    profit_1 = _round_money(r.randint(5, 50) * 1000)
    earnings_1 = int_cap_1 + sal_1 + profit_1
    
    eq_start_1 = _round_money(r.randint(300, 500) * 1000)
    eq_end_1 = _round_money(r.randint(350, 600) * 1000)
    avg_eq_1 = (eq_start_1 + eq_end_1) / 2
    return_1 = round(earnings_1 / avg_eq_1 * 100, 1) if avg_eq_1 > 0 else 0
    
    # Partner 2
    int_cap_2 = _round_money(r.randint(30, 60) * 1000)
    sal_2 = _round_money(r.randint(120, 200) * 1000)
    profit_2 = _round_money(r.randint(5, 50) * 1000)
    earnings_2 = int_cap_2 + sal_2 + profit_2
    
    eq_start_2 = _round_money(r.randint(300, 500) * 1000)
    eq_end_2 = _round_money(r.randint(350, 600) * 1000)
    avg_eq_2 = (eq_start_2 + eq_end_2) / 2
    return_2 = round(earnings_2 / avg_eq_2 * 100, 1) if avg_eq_2 > 0 else 0
    
    total_net_profit = earnings_1 + earnings_2
    total_avg_eq = avg_eq_1 + avg_eq_2
    return_biz = round(total_net_profit / total_avg_eq * 100, 1) if total_avg_eq > 0 else 0

    headers = ["Financial Indicator", "Calculation", f"Percentage for {year}"]
    rows = [
        [f"Return on equity: {p1}", f"{earnings_1} / {avg_eq_1} * 100", f"{return_1}%"],
        [f"Return on equity: {p2}", f"{earnings_2} / {avg_eq_2} * 100", f"{return_2}%"],
        ["Return on equity: Business", f"{total_net_profit} / {total_avg_eq} * 100", f"{return_biz}%"],
    ]

    prompt = f"""{biz}

#### REQUIRED:
Calculate the return on average owner's equity for each partner and for the business as a whole. Show your calculation and express the final answer as a percentage (rounded to one decimal place).

#### INFORMATION:
The following information relates to the partners of {biz} for the year ended 28 February {year}:
    
**{p1}**
• Interest on capital: {_money(int_cap_1)}
• Salary: {_money(sal_1)}
• Share of remaining profit: {_money(profit_1)}
• Owner's equity (start of year): {_money(eq_start_1)}
• Owner's equity (end of year): {_money(eq_end_1)}

**{p2}**
• Interest on capital: {_money(int_cap_2)}
• Salary: {_money(sal_2)}
• Share of remaining profit: {_money(profit_2)}
• Owner's equity (start of year): {_money(eq_start_2)}
• Owner's equity (end of year): {_money(eq_end_2)}"""

    return _mk_journal_table(
        prompt=prompt,
        journal_type="analysis_partner_returns_table",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[1, 2],
        title_fields=[{"label": biz, "value": "Partner Returns"}],
        archetype_key="g11_analysis_partner_returns",
    )

def _gen_gross_profit_pct(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    sales = _round_money(r.randint(2000, 8000) * 1000)
    cost_of_sales = _round_money(sales * r.uniform(0.45, 0.75))
    gp = _round_money(sales - cost_of_sales)
    gp_pct = round(gp / sales * 100, 1)

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the gross profit percentage on sales.\n\n"
            f"#### INFORMATION:\n"
            f"The following information was extracted from the financial statements "
            f"of {biz} for the year ended 28 February 2024:\n"
            f"• Sales: {_money(sales)}\n"
            f"• Cost of sales: {_money(cost_of_sales)}"
        ),
        correct_answer=gp_pct,
        unit="%",
        working_formula=(
            f"GP = {_money(sales)} − {_money(cost_of_sales)} = {_money(gp)}. "
            f"GP% = {_money(gp)} ÷ {_money(sales)} × 100 = {gp_pct}%"
        ),
    )


def _gen_net_profit_pct(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    sales = _round_money(r.randint(2000, 8000) * 1000)
    net_profit = _round_money(sales * r.uniform(0.05, 0.20))
    np_pct = round(net_profit / sales * 100, 1)

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the net profit percentage on sales.\n\n"
            f"#### INFORMATION:\n"
            f"{biz} had net sales of {_money(sales)} and net profit of "
            f"{_money(net_profit)} for the year."
        ),
        correct_answer=np_pct,
        unit="%",
        working_formula=f"{_money(net_profit)} ÷ {_money(sales)} × 100 = {np_pct}%",
    )


def _gen_operating_expenses_pct(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    sales = _round_money(r.randint(2000, 8000) * 1000)
    op_exp = _round_money(sales * r.uniform(0.20, 0.45))
    pct = round(op_exp / sales * 100, 1)

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate operating expenses as a percentage of sales.\n\n"
            f"#### INFORMATION:\n"
            f"Sales = {_money(sales)}, Operating expenses = {_money(op_exp)}."
        ),
        correct_answer=pct,
        unit="%",
        working_formula=f"{_money(op_exp)} ÷ {_money(sales)} × 100 = {pct}%",
    )


# ---------------------------------------------------------------------------
# Liquidity ratios
# ---------------------------------------------------------------------------

def _gen_current_ratio(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    trading_stock = _round_money(r.randint(20, 80) * 1000)
    debtors = _round_money(r.randint(15, 60) * 1000)
    bank = _round_money(r.randint(5, 40) * 1000)
    current_assets = _round_money(trading_stock + debtors + bank)
    creditors = _round_money(r.randint(10, 40) * 1000)
    bank_od = 0 if bank > 0 else _round_money(r.randint(10, 30) * 1000)
    current_liab = _round_money(creditors + bank_od)

    ratio = round(current_assets / current_liab, 1) if current_liab > 0 else 0

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the current ratio (express as X : 1).\n\n"
            f"#### INFORMATION:\n"
            f"The following appeared in the Balance Sheet of {biz}:\n"
            f"• Trading stock: {_money(trading_stock)}\n"
            f"• Debtors control: {_money(debtors)}\n"
            f"• Bank (favourable): {_money(bank)}\n"
            f"• Creditors control: {_money(creditors)}"
        ),
        correct_answer=ratio,
        unit=": 1",
        working_formula=(
            f"Current assets = {_money(trading_stock)} + {_money(debtors)} + {_money(bank)} = "
            f"{_money(current_assets)}. Ratio = {_money(current_assets)} : {_money(current_liab)} = {ratio} : 1"
        ),
    )


def _gen_acid_test_ratio(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    trading_stock = _round_money(r.randint(20, 80) * 1000)
    debtors = _round_money(r.randint(15, 60) * 1000)
    bank = _round_money(r.randint(5, 40) * 1000)
    creditors = _round_money(r.randint(10, 40) * 1000)

    liquid_assets = _round_money(debtors + bank)
    ratio = round(liquid_assets / creditors, 1) if creditors > 0 else 0

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the acid test ratio.\n\n"
            f"#### INFORMATION:\n"
            f"From {biz}'s Balance Sheet:\n"
            f"• Trading stock: {_money(trading_stock)}\n"
            f"• Debtors: {_money(debtors)}\n"
            f"• Bank: {_money(bank)}\n"
            f"• Creditors: {_money(creditors)}"
        ),
        correct_answer=ratio,
        unit=": 1",
        working_formula=(
            f"Liquid = {_money(debtors)} + {_money(bank)} = {_money(liquid_assets)}. "
            f"Ratio = {_money(liquid_assets)} : {_money(creditors)} = {ratio} : 1"
        ),
    )


# ---------------------------------------------------------------------------
# Stock management
# ---------------------------------------------------------------------------

def _gen_stock_turnover_rate(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    opening = _round_money(r.randint(10, 50) * 1000)
    closing = _round_money(r.randint(12, 55) * 1000)
    cost_of_sales = _round_money(r.randint(400, 1200) * 1000)
    avg = _round_money((opening + closing) / 2)
    turnover = round(cost_of_sales / avg, 1) if avg > 0 else 0

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the stock turnover rate (times per year).\n\n"
            f"#### INFORMATION:\n"
            f"Opening stock = {_money(opening)}, Closing stock = {_money(closing)}, "
            f"Cost of sales = {_money(cost_of_sales)}."
        ),
        correct_answer=turnover,
        unit="times",
        working_formula=(
            f"Avg stock = ½({_money(opening)} + {_money(closing)}) = {_money(avg)}. "
            f"Rate = {_money(cost_of_sales)} ÷ {_money(avg)} = {turnover} times"
        ),
    )


# ---------------------------------------------------------------------------
# Debtors / creditors period
# ---------------------------------------------------------------------------

def _gen_debtors_collection(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    deb_open = _round_money(r.randint(20, 60) * 1000)
    deb_close = _round_money(r.randint(18, 55) * 1000)
    credit_sales = _round_money(r.randint(800, 3000) * 1000)
    avg = _round_money((deb_open + deb_close) / 2)
    days = round(avg / credit_sales * 365)

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the average debtors' collection period in days.\n\n"
            f"#### INFORMATION:\n"
            f"Debtors at start = {_money(deb_open)}, "
            f"Debtors at end = {_money(deb_close)}, "
            f"Credit sales = {_money(credit_sales)}."
        ),
        correct_answer=float(days),
        unit="days",
        working_formula=(
            f"Avg debtors = ½({_money(deb_open)} + {_money(deb_close)}) = {_money(avg)}. "
            f"Period = {_money(avg)} ÷ {_money(credit_sales)} × 365 = {days} days"
        ),
    )


def _gen_creditors_payment(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    cred_open = _round_money(r.randint(15, 45) * 1000)
    cred_close = _round_money(r.randint(12, 50) * 1000)
    credit_purch = _round_money(r.randint(600, 2500) * 1000)
    avg = _round_money((cred_open + cred_close) / 2)
    days = round(avg / credit_purch * 365)

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the average creditors' payment period in days.\n\n"
            f"#### INFORMATION:\n"
            f"Creditors at start = {_money(cred_open)}, "
            f"Creditors at end = {_money(cred_close)}, "
            f"Credit purchases = {_money(credit_purch)}."
        ),
        correct_answer=float(days),
        unit="days",
        working_formula=(
            f"Avg creditors = ½({_money(cred_open)} + {_money(cred_close)}) = {_money(avg)}. "
            f"Period = {_money(avg)} ÷ {_money(credit_purch)} × 365 = {days} days"
        ),
    )


# ---------------------------------------------------------------------------
# Solvency & gearing
# ---------------------------------------------------------------------------

def _gen_solvency_ratio(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    total_assets = _round_money(r.randint(800, 3000) * 1000)
    total_liab = _round_money(total_assets * r.uniform(0.2, 0.6))
    ratio = round(total_assets / total_liab, 1) if total_liab > 0 else 0

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the solvency ratio.\n\n"
            f"#### INFORMATION:\n"
            f"Total assets = {_money(total_assets)}, "
            f"Total liabilities = {_money(total_liab)}."
        ),
        correct_answer=ratio,
        unit=": 1",
        working_formula=f"{_money(total_assets)} : {_money(total_liab)} = {ratio} : 1",
    )


def _gen_debt_equity_ratio(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    ncl = _round_money(r.randint(100, 500) * 1000)
    equity = _round_money(r.randint(500, 1500) * 1000)
    ratio = round(ncl / equity, 1) if equity > 0 else 0

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the debt-equity ratio.\n\n"
            f"#### INFORMATION:\n"
            f"Non-current liabilities = {_money(ncl)}, "
            f"Total owner's equity = {_money(equity)}."
        ),
        correct_answer=ratio,
        unit=": 1",
        working_formula=f"{_money(ncl)} : {_money(equity)} = {ratio} : 1",
    )


# ---------------------------------------------------------------------------
# Partner's earnings & return
# ---------------------------------------------------------------------------

def _gen_partner_earnings(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    p1 = _partner_name(r)
    int_cap = _round_money(r.randint(30, 60) * 1000)
    salary = _round_money(r.randint(100, 200) * 1000)
    bonus = _round_money(r.choice([0, 5000, 10000, 15000]))
    profit_share = _round_money(r.randint(1, 20) * 1000)
    total = _round_money(int_cap + salary + bonus + profit_share)

    items = f"• Interest on capital: {_money(int_cap)}\n• Salary: {_money(salary)}\n"
    if bonus > 0:
        items += f"• Bonus: {_money(bonus)}\n"
    items += f"• Share of remaining profit: {_money(profit_share)}"

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the total earnings of {p1} from {biz} "
            f"for the year ended 28 February 2024.\n\n"
            f"#### INFORMATION:\n{items}"
        ),
        correct_answer=total,
        unit="R",
        working_formula=(
            f"{_money(int_cap)} + {_money(salary)}"
            + (f" + {_money(bonus)}" if bonus > 0 else "")
            + f" + {_money(profit_share)} = {_money(total)}"
        ),
    )


def _gen_return_on_partner_equity(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    p1 = _partner_name(r)
    earnings = _round_money(r.randint(150, 300) * 1000)
    cap_start = _round_money(r.randint(300, 600) * 1000)
    cap_end = _round_money(cap_start + r.randint(-20, 50) * 1000)
    ca_start = _round_money(r.randint(-60, 10) * 1000)
    ca_end = _round_money(r.randint(-10, 30) * 1000)

    eq_start = cap_start + ca_start
    eq_end = cap_end + ca_end
    avg_eq = _round_money((eq_start + eq_end) / 2)
    roe = round(earnings / avg_eq * 100, 1) if avg_eq > 0 else 0

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the percentage return earned by {p1} from {biz}.\n\n"
            f"#### INFORMATION:\n"
            f"• Earnings: {_money(earnings)}\n"
            f"• Capital at start: {_money(cap_start)}, Capital at end: {_money(cap_end)}\n"
            f"• Current account at start: {_money(ca_start)}, at end: {_money(ca_end)}"
        ),
        correct_answer=roe,
        unit="%",
        working_formula=(
            f"Avg equity = ½({_money(eq_start)} + {_money(eq_end)}) = {_money(avg_eq)}. "
            f"Return = {_money(earnings)} ÷ {_money(avg_eq)} × 100 = {roe}%"
        ),
    )


# ---------------------------------------------------------------------------
# Interest rate / salary increase back-calculation
# ---------------------------------------------------------------------------

def _gen_interest_rate_backcalc(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    p1 = _partner_name(r)
    capital = _round_money(r.choice([300, 400, 420, 500, 600]) * 1000)
    rate = r.choice([8, 9, 10, 11, 12])
    interest = _round_money(capital * rate / 100)

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the interest rate agreed upon.\n\n"
            f"#### INFORMATION:\n"
            f"{p1}'s capital contribution to {biz} is {_money(capital)}. "
            f"Interest on capital for the year amounted to {_money(interest)}."
        ),
        correct_answer=float(rate),
        unit="%",
        working_formula=f"{_money(interest)} ÷ {_money(capital)} × 100 = {rate}%",
    )


def _gen_salary_increase_pct(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    old_salary = _round_money(r.choice([100, 120, 130, 144, 150]) * 1000)
    increase_pct = r.choice([8, 10, 12, 15])
    new_salary = _round_money(old_salary * (1 + increase_pct / 100))

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the percentage increase.\n\n"
            f"#### INFORMATION:\n"
            f"A partner in {biz} earned a salary of {_money(old_salary)} last year, "
            f"which was increased to {_money(new_salary)} this year."
        ),
        correct_answer=float(increase_pct),
        unit="%",
        working_formula=(
            f"({_money(new_salary)} − {_money(old_salary)}) ÷ {_money(old_salary)} × 100 = {increase_pct}%"
        ),
    )


# ---------------------------------------------------------------------------
# Asset disposal
# ---------------------------------------------------------------------------

def _gen_asset_disposal(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    asset = r.choice(["vehicle", "delivery van", "bakkie"])
    cost = _round_money(r.choice([80, 100, 120, 150, 180, 200, 240]) * 1000)
    acc_dep = _round_money(cost * r.uniform(0.2, 0.6))
    carrying = _round_money(cost - acc_dep)
    sell_price = _round_money(carrying * r.uniform(0.7, 1.4))
    result = _round_money(sell_price - carrying)
    result_type = "profit" if result >= 0 else "loss"

    return _make_calc(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Calculate the {result_type} on disposal.\n\n"
            f"#### INFORMATION:\n"
            f"A {asset} from {biz} was sold.\n"
            f"Cost price: {_money(cost)}.\n"
            f"Accumulated depreciation: {_money(acc_dep)}.\n"
            f"Selling price: {_money(sell_price)}."
        ),
        correct_answer=abs(result),
        unit="R",
        working_formula=(
            f"Carrying value = {_money(cost)} − {_money(acc_dep)} = {_money(carrying)}. "
            f"{result_type.title()} = {_money(sell_price)} − {_money(carrying)} = {_money(abs(result))}"
        ),
    )


# ---------------------------------------------------------------------------
# Commentary / typed
# ---------------------------------------------------------------------------

def _gen_liquidity_commentary(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    cr_prev = round(r.uniform(0.5, 1.2), 1)
    cr_curr = round(r.uniform(2.5, 5.5), 1)
    at_prev = round(r.uniform(0.4, 0.8), 1)
    at_curr = round(r.uniform(1.5, 3.5), 1)

    return _make_typed(
        prompt=(
            f"{biz}\n\n#### REQUIRED:\n"
            f"Comment on the liquidity position and explain possible reasons for the change.\n\n"
            f"#### INFORMATION:\n"
            f"The liquidity ratios of {biz} changed as follows:\n"
            f"• Current ratio: {cr_prev}:1 → {cr_curr}:1\n"
            f"• Acid test ratio: {at_prev}:1 → {at_curr}:1"
        ),
        sample_answer=(
            f"The current ratio improved from {cr_prev}:1 to {cr_curr}:1 (norm 2:1), "
            f"and the acid test improved from {at_prev}:1 to {at_curr}:1 (norm 1:1). "
            f"This indicates a much stronger ability to meet short-term obligations. "
            f"Possible reasons: bank overdraft eliminated, debtors decreased, "
            f"creditors decreased, trading stock increased."
        ),
        grading_rubric=[
            "Compares ratios to norms (2:1 and 1:1)",
            "Notes improvement/deterioration direction",
            "Provides valid reasons for the change",
            "Comments on ability to meet short-term debts",
        ],
    )


def _gen_partnership_concepts_mcq(r: random.Random) -> Dict[str, Any]:
    questions = [
        {
            "prompt": "List ONE advantage of a partnership as a form of ownership.",
            "options": [
                "Partners combine skills and capital",
                "Partners have limited liability",
                "A partnership pays company tax",
                "A partnership has perpetual succession",
            ],
            "correct": 0,
            "explanation": "Partnerships benefit from combined skills, abilities and capital of multiple partners.",
        },
        {
            "prompt": "What does a debit balance on a partner's current account indicate?",
            "options": [
                "The partner owes the business money (withdrawn more than earned)",
                "The business owes the partner money",
                "The partner has a favourable bank balance",
                "The partner's capital has increased",
            ],
            "correct": 0,
            "explanation": "A debit balance means the partner has withdrawn more than their earnings — they owe the business.",
        },
        {
            "prompt": "When a partner takes trading stock for personal use, the transaction is recorded as:",
            "options": [
                "Drawings",
                "A distribution of profit",
                "Additional salary",
                "A loan from the partnership",
            ],
            "correct": 0,
            "explanation": "Taking stock for personal use is drawings, recorded as: Dr Drawings / Cr Trading stock.",
        },
        {
            "prompt": "A partnership does NOT pay income tax because:",
            "options": [
                "It is not a legal entity — each partner is taxed individually",
                "Partnerships are exempt from all taxes",
                "Only companies pay income tax",
                "Profits are distributed before tax is calculated",
            ],
            "correct": 0,
            "explanation": "A partnership is not a separate legal entity. Each partner is taxed on their share of the profit.",
        },
    ]
    chosen = r.choice(questions)
    return _make_mcq(
        prompt=chosen["prompt"],
        options=chosen["options"],
        correct_index=chosen["correct"],
        explanation=chosen["explanation"],
    )


def _gen_internal_control_assets(r: random.Random) -> Dict[str, Any]:
    return _make_typed(
        prompt="Suggest TWO control measures that a business should implement for fixed assets.",
        sample_answer=(
            "1. Assets not in use should be locked away securely. "
            "2. Maintain a detailed asset register and perform physical asset counts regularly. "
            "3. Vehicle keys should be kept in a secure location with a responsible person. "
            "4. Install tracker systems on vehicles."
        ),
        grading_rubric=[
            "Physical security/storage of assets",
            "Regular physical verification against asset register",
        ],
    )


def _gen_loan_eligibility(r: random.Random) -> Dict[str, Any]:
    biz = r.choice(_BUSINESS_NAMES)
    ncl = _round_money(r.randint(200, 500) * 1000)
    equity = _round_money(r.randint(600, 1200) * 1000)
    loan = _round_money(r.choice([200, 300, 400, 500]) * 1000)

    ratio_before = round(ncl / equity, 2) if equity > 0 else 0
    ratio_after = round((ncl + loan) / equity, 2) if equity > 0 else 0

    would_grant = ratio_after < 1.0

    return _make_calc(
        prompt=(
            f"{biz}: Non-current liabilities = {_money(ncl)}, "
            f"Owner's equity = {_money(equity)}. "
            f"The partners want a loan of {_money(loan)} to purchase new vehicles. "
            f"Calculate the debt-equity ratio if the loan is granted."
        ),
        correct_answer=ratio_after,
        unit=": 1",
        working_formula=(
            f"New NCL = {_money(ncl)} + {_money(loan)} = {_money(ncl + loan)}. "
            f"Ratio = {_money(ncl + loan)} : {_money(equity)} = {ratio_after}:1. "
            f"{'Below' if ratio_after < 1 else 'Above'} 1:1 norm."
        ),
    )


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

_GENERATORS = [
    _make_liquidity_ratios_table,
    _make_profitability_indicators_table,
    _make_solvency_and_risk_table,
    _make_partner_returns_table,
    _gen_gross_profit_pct,
    _gen_net_profit_pct,
    _gen_operating_expenses_pct,
    _gen_current_ratio,
    _gen_acid_test_ratio,
    _gen_stock_turnover_rate,
    _gen_debtors_collection,
    _gen_creditors_payment,
    _gen_solvency_ratio,
    _gen_debt_equity_ratio,
    _gen_partner_earnings,
    _gen_return_on_partner_equity,
    _gen_interest_rate_backcalc,
    _gen_salary_increase_pct,
    _gen_asset_disposal,
    _gen_liquidity_commentary,
    _gen_partnership_concepts_mcq,
    _gen_internal_control_assets,
    _gen_loan_eligibility,
]


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "",
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    questions: List[Dict[str, Any]] = []

    for _ in range(count):
        gen = r.choice(_GENERATORS)
        q = gen(r)
        q["difficulty"] = difficulty
        q["mode"] = mode
        questions.append(q)

    return questions
