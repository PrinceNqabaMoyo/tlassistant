from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional, Tuple


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _round2(x: float) -> float:
    return round(float(x) + 1e-9, 2)


def _make_calc(*, prompt: str, correct_value: float, unit: str = "", explanation: str = "", mode: str = "", archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct12_analysis_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_value": float(_round2(correct_value)),
        "unit": unit,
        "expected_answer_type": "number",
    }
    if archetype_key:
        out["meta"] = {"archetype_key": archetype_key}
    if str(mode or "").strip().lower() == "scaffold" and str(explanation).strip():
        out["explanation"] = explanation
    return out


def _make_typed(*, prompt: str, sample_answer: str, mode: str, archetype_key: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "id": _make_id("acct12_analysis_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "expected_answer_type": "text",
    }
    meta: Dict[str, Any] = {}
    if archetype_key:
        meta["archetype_key"] = archetype_key
    if meta:
        out["meta"] = meta
    if str(mode or "").strip().lower() == "scaffold":
        out["sample_answer"] = sample_answer
    return out


def _pick_dataset(r: random.Random) -> Dict[str, Any]:
    """Build a self-contained company scenario with all fields needed by every
    curriculum archetype (Worked Examples 1-5, Q1-Q5)."""

    company = r.choice(["Glebo Ltd", "Winston Ltd", "Bently Ltd", "Nomndeni Loyal Ltd",
                         "South Ltd", "Speedy Ltd", "Kwik Fix Ltd", "Kopano Ltd"])
    year = int(r.choice([2024, 2025, 2023, 2021, 2020, 2011]))
    prev = year - 1
    fy_end_curr = r.choice([f"28 February {year}", f"29 February {year}", f"30 June {year}"])
    fy_end_prev = fy_end_curr.replace(str(year), str(prev))

    # --- Income Statement ---
    sales_curr = float(r.choice([9_000_000, 10_500_000, 8_750_000, 7_200_000]))
    sales_prev = float(r.choice([8_200_000, 9_500_000, 7_800_000, 6_500_000]))
    cost_of_sales_curr = float(r.choice([5_625_000, 7_050_000, 5_250_000, 4_800_000]))
    cost_of_sales_prev = float(r.choice([5_100_000, 6_500_000, 4_900_000, 4_200_000]))
    gross_profit_curr = _round2(sales_curr - cost_of_sales_curr)
    gross_profit_prev = _round2(sales_prev - cost_of_sales_prev)

    operating_expenses_curr = float(r.choice([1_260_000, 1_470_000, 1_890_000, 2_100_000]))
    operating_expenses_prev = float(r.choice([1_558_000, 1_805_000, 2_340_000, 1_625_000]))
    operating_profit_curr = _round2(gross_profit_curr - operating_expenses_curr)
    operating_profit_prev = _round2(gross_profit_prev - operating_expenses_prev)

    interest_on_loan_curr = float(r.choice([158_000, 120_000, 257_400, 93_640]))
    interest_on_loan_prev = float(r.choice([112_000, 96_000, 180_000, 65_000]))

    profit_before_tax_curr = _round2(operating_profit_curr - interest_on_loan_curr)
    profit_before_tax_prev = _round2(operating_profit_prev - interest_on_loan_prev)

    income_tax_curr = float(r.choice([426_000, 350_000, 280_000, 176_240]))
    income_tax_prev = float(r.choice([320_000, 275_000, 210_000, 150_285]))
    net_profit_after_tax_curr = _round2(profit_before_tax_curr - income_tax_curr)
    net_profit_after_tax_prev = _round2(profit_before_tax_prev - income_tax_prev)

    # --- Balance Sheet ---
    total_fixed_assets_curr = float(r.choice([4_326_000, 3_800_000, 5_100_000]))
    financial_assets_curr = float(r.choice([300_000, 550_000, 250_000]))
    non_current_assets_curr = _round2(total_fixed_assets_curr + financial_assets_curr)

    inventories_curr = float(r.choice([1_640_000, 1_200_000, 950_000, 1_400_000]))
    inventories_prev = float(r.choice([1_350_000, 1_100_000, 800_000, 1_250_000]))
    avg_stock = _round2((inventories_curr + inventories_prev) / 2.0)

    trade_debtors_curr = float(r.choice([810_000, 650_000, 520_000, 900_000]))
    trade_debtors_prev = float(r.choice([700_000, 550_000, 480_000, 780_000]))
    avg_debtors = _round2((trade_debtors_curr + trade_debtors_prev) / 2.0)

    sars_income_tax_asset = float(r.choice([0.0, 18_000, 25_000]))
    cash_curr = float(r.choice([107_000, 85_000, 140_000, 92_680]))
    cash_prev = float(r.choice([25_000, 12_340, 900, 45_000]))
    receivables_curr = _round2(trade_debtors_curr + sars_income_tax_asset)
    receivables_prev = _round2(trade_debtors_prev)

    current_assets_curr = _round2(inventories_curr + receivables_curr + cash_curr)
    current_assets_prev = _round2(inventories_prev + receivables_prev + cash_prev)
    total_assets_curr = _round2(non_current_assets_curr + current_assets_curr)

    # Shareholders' equity
    issued_shares_prev = int(r.choice([3_000_000, 2_500_000, 1_100_000, 500_000]))
    # Rights issue: 10 for every 50 owned
    rights_ratio_num = 10
    rights_ratio_den = 50
    new_shares_from_rights = int(issued_shares_prev * rights_ratio_num / rights_ratio_den)
    issued_shares_curr = issued_shares_prev + new_shares_from_rights

    share_capital_prev = float(r.choice([28_800_000, 18_000_000, 2_910_000, 4_500_000]))
    share_capital_increase = float(r.choice([2_970_000, 1_800_000, 990_000, 1_500_000]))
    share_capital_curr = _round2(share_capital_prev + share_capital_increase)
    issue_price_per_share = _round2(share_capital_increase / new_shares_from_rights) if new_shares_from_rights else 0.0

    retained_income_curr = float(r.choice([1_213_000, 950_000, 1_650_000, 1_315_000]))
    retained_income_prev = float(r.choice([900_000, 750_000, 1_200_000, 1_050_000]))

    shareholders_equity_curr = _round2(share_capital_curr + retained_income_curr)
    shareholders_equity_prev = _round2(share_capital_prev + retained_income_prev)
    avg_shareholders_equity = _round2((shareholders_equity_curr + shareholders_equity_prev) / 2.0)

    # Non-current liabilities (Loan)
    loan_curr = float(r.choice([1_980_000, 1_200_000, 650_000, 12_913_000]))
    loan_prev = float(r.choice([2_400_000, 1_500_000, 900_000, 9_400_000]))
    non_current_liabilities_curr = loan_curr
    non_current_liabilities_prev = loan_prev
    avg_loan = _round2((loan_curr + loan_prev) / 2.0)

    # Current liabilities
    trade_creditors_curr = float(r.choice([705_000, 520_000, 320_000, 450_000]))
    trade_creditors_prev = float(r.choice([600_000, 480_000, 280_000, 400_000]))
    avg_creditors = _round2((trade_creditors_curr + trade_creditors_prev) / 2.0)
    sars_tax_liability = float(r.choice([32_000, 45_000, 18_000]))
    shareholders_for_dividends = float(r.choice([275_000, 200_000, 150_000]))
    current_portion_of_loan = float(r.choice([68_000, 120_000, 80_000]))
    bank_overdraft = float(r.choice([0.0, 45_000, 0.0]))
    current_liabilities_curr = _round2(
        trade_creditors_curr + sars_tax_liability + shareholders_for_dividends +
        current_portion_of_loan + bank_overdraft
    )
    current_liabilities_prev = float(r.choice([1_080_000, 850_000, 620_000, 950_000]))

    total_liabilities_curr = _round2(non_current_liabilities_curr + current_liabilities_curr)
    total_assets_curr = _round2(shareholders_equity_curr + total_liabilities_curr)
    non_current_assets_curr = _round2(total_assets_curr - current_assets_curr)

    # Credit sales (for debtors/creditors period calculations)
    credit_sales_curr = _round2(sales_curr * r.choice([0.80, 0.85, 0.90, 0.75]))
    credit_purchases_curr = _round2(cost_of_sales_curr * r.choice([0.85, 0.90, 0.80]))

    # Dividends
    interim_dividends_curr = float(r.choice([90_000, 120_000, 275_000, 180_000]))
    final_dividends_curr = float(r.choice([70_000, 90_000, 0.0, 150_000]))
    total_dividends_curr = _round2(interim_dividends_curr + final_dividends_curr)

    # Rates
    loan_interest_rate_curr = float(r.choice([12.0, 13.0, 14.0, 16.0]))
    loan_interest_rate_prev = float(r.choice([12.0, 13.0, 14.0, 12.0]))
    fd_interest_rate_curr = float(r.choice([7.5, 8.0, 9.2, 10.0]))
    fd_interest_rate_prev = float(r.choice([6.5, 8.0, 9.2, 8.0]))

    # Market price per share
    market_price_curr = float(r.choice([950, 810, 934, 820]))
    market_price_prev = float(r.choice([820, 720, 968, 750]))

    # Majority shareholder (for Q1/Q4 shareholding questions)
    majority_name = r.choice(["Grant Waters", "Njabulo Dlamini", "Thabo Mokoena"])
    majority_shares_prev = int(issued_shares_prev * r.choice([0.54, 0.48, 0.52]))
    majority_shares_from_rights = int(majority_shares_prev * rights_ratio_num / rights_ratio_den)
    majority_shares_curr = majority_shares_prev + majority_shares_from_rights

    # Second shareholder for coalition questions
    second_name = r.choice(["Dunford Cele", "Sipho Nkosi", "Lerato Molefe"])
    second_pct_prev = float(r.choice([16.0, 18.0, 22.0]))
    second_pct_curr = float(r.choice([25.0, 22.0, 27.0]))

    # CEO info
    ceo_name = r.choice(["Shakira Solomon", "Thandi Mkhize", "James Naidoo"])
    ceo_buyback_price_cents = float(r.choice([810, 1200, 750]))
    ceo_buyback_shares = int(r.choice([30_000, 50_000, 20_000]))

    # Fixed assets purchased/sold (for financing strategies)
    fixed_assets_purchased_curr = float(r.choice([8_235_000, 4_500_000, 3_200_000]))
    fixed_assets_purchased_prev = float(r.choice([4_180_000, 2_800_000, 1_900_000]))
    fixed_assets_sold_curr = float(r.choice([710_000, 0.0, 350_000]))

    # Trading stock deficit
    stock_deficit_pct_curr = float(r.choice([6.0, 2.0, 3.0]))
    stock_deficit_pct_prev = float(r.choice([2.0, 1.0, 1.5]))

    return {
        "company": company,
        "year": year,
        "prev_year": prev,
        "fy_end_curr": fy_end_curr,
        "fy_end_prev": fy_end_prev,
        # Income Statement
        "sales_curr": sales_curr,
        "sales_prev": sales_prev,
        "cost_of_sales_curr": cost_of_sales_curr,
        "cost_of_sales_prev": cost_of_sales_prev,
        "gross_profit_curr": gross_profit_curr,
        "gross_profit_prev": gross_profit_prev,
        "operating_expenses_curr": operating_expenses_curr,
        "operating_expenses_prev": operating_expenses_prev,
        "operating_profit_curr": operating_profit_curr,
        "operating_profit_prev": operating_profit_prev,
        "interest_on_loan_curr": interest_on_loan_curr,
        "interest_on_loan_prev": interest_on_loan_prev,
        "profit_before_tax_curr": profit_before_tax_curr,
        "profit_before_tax_prev": profit_before_tax_prev,
        "income_tax_curr": income_tax_curr,
        "income_tax_prev": income_tax_prev,
        "net_profit_after_tax_curr": net_profit_after_tax_curr,
        "net_profit_after_tax_prev": net_profit_after_tax_prev,
        # Balance Sheet
        "total_fixed_assets_curr": total_fixed_assets_curr,
        "financial_assets_curr": financial_assets_curr,
        "non_current_assets_curr": non_current_assets_curr,
        "inventories_curr": inventories_curr,
        "inventories_prev": inventories_prev,
        "avg_stock": avg_stock,
        "trade_debtors_curr": trade_debtors_curr,
        "trade_debtors_prev": trade_debtors_prev,
        "avg_debtors": avg_debtors,
        "sars_income_tax_asset": sars_income_tax_asset,
        "cash_curr": cash_curr,
        "cash_prev": cash_prev,
        "receivables_curr": receivables_curr,
        "receivables_prev": receivables_prev,
        "current_assets_curr": current_assets_curr,
        "current_assets_prev": current_assets_prev,
        "total_assets_curr": total_assets_curr,
        # Equity
        "issued_shares_curr": issued_shares_curr,
        "issued_shares_prev": issued_shares_prev,
        "new_shares_from_rights": new_shares_from_rights,
        "rights_ratio_num": rights_ratio_num,
        "rights_ratio_den": rights_ratio_den,
        "share_capital_curr": share_capital_curr,
        "share_capital_prev": share_capital_prev,
        "share_capital_increase": share_capital_increase,
        "issue_price_per_share": issue_price_per_share,
        "retained_income_curr": retained_income_curr,
        "retained_income_prev": retained_income_prev,
        "shareholders_equity_curr": shareholders_equity_curr,
        "shareholders_equity_prev": shareholders_equity_prev,
        "avg_shareholders_equity": avg_shareholders_equity,
        # Liabilities
        "loan_curr": loan_curr,
        "loan_prev": loan_prev,
        "avg_loan": avg_loan,
        "non_current_liabilities_curr": non_current_liabilities_curr,
        "non_current_liabilities_prev": non_current_liabilities_prev,
        "trade_creditors_curr": trade_creditors_curr,
        "trade_creditors_prev": trade_creditors_prev,
        "avg_creditors": avg_creditors,
        "sars_tax_liability": sars_tax_liability,
        "shareholders_for_dividends": shareholders_for_dividends,
        "current_portion_of_loan": current_portion_of_loan,
        "bank_overdraft": bank_overdraft,
        "current_liabilities_curr": current_liabilities_curr,
        "current_liabilities_prev": current_liabilities_prev,
        "total_liabilities_curr": total_liabilities_curr,
        # Credit / purchases
        "credit_sales_curr": credit_sales_curr,
        "credit_purchases_curr": credit_purchases_curr,
        # Dividends
        "interim_dividends_curr": interim_dividends_curr,
        "final_dividends_curr": final_dividends_curr,
        "total_dividends_curr": total_dividends_curr,
        # Rates
        "loan_interest_rate_curr": loan_interest_rate_curr,
        "loan_interest_rate_prev": loan_interest_rate_prev,
        "fd_interest_rate_curr": fd_interest_rate_curr,
        "fd_interest_rate_prev": fd_interest_rate_prev,
        # Market
        "market_price_curr": market_price_curr,
        "market_price_prev": market_price_prev,
        # Shareholding
        "majority_name": majority_name,
        "majority_shares_prev": majority_shares_prev,
        "majority_shares_from_rights": majority_shares_from_rights,
        "majority_shares_curr": majority_shares_curr,
        "second_name": second_name,
        "second_pct_prev": second_pct_prev,
        "second_pct_curr": second_pct_curr,
        # CEO
        "ceo_name": ceo_name,
        "ceo_buyback_price_cents": ceo_buyback_price_cents,
        "ceo_buyback_shares": ceo_buyback_shares,
        # Fixed assets
        "fixed_assets_purchased_curr": fixed_assets_purchased_curr,
        "fixed_assets_purchased_prev": fixed_assets_purchased_prev,
        "fixed_assets_sold_curr": fixed_assets_sold_curr,
        # Stock deficit
        "stock_deficit_pct_curr": stock_deficit_pct_curr,
        "stock_deficit_pct_prev": stock_deficit_pct_prev,
    }


def _ratio(a: float, b: float) -> float:
    if b == 0:
        return 0.0
    return a / b


###############################################################################
# Calculation helpers — each returns (value, explanation_with_figure_hints)
###############################################################################

def _calc_current_ratio(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    ca = d[f"current_assets_{yk}"]; cl = d[f"current_liabilities_{yk}"]
    v = _ratio(ca, cl)
    return (_round2(v), f"Current ratio = R{ca:,.0f} [Total current assets] / R{cl:,.0f} [Total current liabilities] = {v:.2f} : 1")

def _calc_acid_test(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    cash = d[f"cash_{yk}"]; recv = d[f"receivables_{yk}"]; cl = d[f"current_liabilities_{yk}"]
    quick = cash + recv; v = _ratio(quick, cl)
    return (_round2(v), f"Acid-test = (R{cash:,.0f} [Cash] + R{recv:,.0f} [Receivables]) / R{cl:,.0f} [Current liabilities] = {v:.2f} : 1")

def _calc_debt_equity(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    ncl = d[f"non_current_liabilities_{yk}"]; se = d[f"shareholders_equity_{yk}"]
    v = _ratio(ncl, se)
    return (_round2(v), f"Debt:Equity = R{ncl:,.0f} [Non-current liabilities] / R{se:,.0f} [Shareholders' equity] = {v:.2f} : 1")

def _calc_solvency(d: Dict[str, Any]) -> Tuple[float, str]:
    ta = d["total_assets_curr"]; tl = d["total_liabilities_curr"]
    v = _ratio(ta, tl)
    return (_round2(v), f"Solvency = R{ta:,.0f} [Total assets] / R{tl:,.0f} [Total liabilities] = {v:.2f} : 1")

def _calc_gp_on_cos(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    gp = d[f"gross_profit_{yk}"]; cos = d[f"cost_of_sales_{yk}"]
    v = _ratio(gp, cos) * 100
    return (_round2(v), f"% GP on COS = R{gp:,.0f} [Gross profit] / R{cos:,.0f} [Cost of sales] × 100 = {v:.1f}%")

def _calc_gp_on_sales(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    gp = d[f"gross_profit_{yk}"]; s = d[f"sales_{yk}"]
    v = _ratio(gp, s) * 100
    return (_round2(v), f"% GP on Sales = R{gp:,.0f} [Gross profit] / R{s:,.0f} [Sales] × 100 = {v:.1f}%")

def _calc_oe_on_sales(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    oe = d[f"operating_expenses_{yk}"]; s = d[f"sales_{yk}"]
    v = _ratio(oe, s) * 100
    return (_round2(v), f"% Op Exp on Sales = R{oe:,.0f} [Operating expenses] / R{s:,.0f} [Sales] × 100 = {v:.1f}%")

def _calc_op_on_sales(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    op = d[f"operating_profit_{yk}"]; s = d[f"sales_{yk}"]
    v = _ratio(op, s) * 100
    return (_round2(v), f"% Op Profit on Sales = R{op:,.0f} [Operating profit] / R{s:,.0f} [Sales] × 100 = {v:.1f}%")

def _calc_np_on_sales(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    np_ = d[f"net_profit_after_tax_{yk}"]; s = d[f"sales_{yk}"]
    v = _ratio(np_, s) * 100
    return (_round2(v), f"% NP on Sales = R{np_:,.0f} [NPAT] / R{s:,.0f} [Sales] × 100 = {v:.1f}%")

def _calc_roshe(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    np_ = d[f"net_profit_after_tax_{yk}"]; se = d[f"shareholders_equity_{yk}"]
    v = _ratio(np_, se) * 100
    return (_round2(v), f"ROSHE = R{np_:,.0f} [NPAT] / R{se:,.0f} [Shareholders' equity] × 100 = {v:.2f}%")

def _calc_rotce(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    np_ = d[f"net_profit_after_tax_{yk}"]; interest = d[f"interest_on_loan_{yk}"]
    se = d[f"shareholders_equity_{yk}"]; ncl = d[f"non_current_liabilities_{yk}"]
    num = np_ + interest; den = se + ncl; v = _ratio(num, den) * 100
    return (_round2(v), f"ROTCE = (R{np_:,.0f} [NPAT] + R{interest:,.0f} [Interest]) / (R{se:,.0f} [Equity] + R{ncl:,.0f} [Loan]) × 100 = {v:.2f}%")

def _calc_eps(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    np_ = d[f"net_profit_after_tax_{yk}"]; sh = float(d[f"issued_shares_{yk}"])
    v = _ratio(np_, sh) * 100
    return (_round2(v), f"EPS = R{np_:,.0f} [NPAT] / {sh:,.0f} [Issued shares] × 100 = {v:.2f} cents")

def _calc_dps(d: Dict[str, Any]) -> Tuple[float, str]:
    interim = d["interim_dividends_curr"]; final = d["final_dividends_curr"]
    total = interim + final; sh = float(d["issued_shares_curr"])
    v = _ratio(total, sh) * 100
    return (_round2(v), f"DPS = (R{interim:,.0f} [Interim div] + R{final:,.0f} [Final div]) / {sh:,.0f} [Shares] × 100 = {v:.2f} cents")

def _calc_dpr(d: Dict[str, Any]) -> Tuple[float, str]:
    dps_v, _ = _calc_dps(d); eps_v, _ = _calc_eps(d, "curr")
    v = _ratio(dps_v, eps_v) * 100 if eps_v else 0.0
    return (_round2(v), f"DPR = {dps_v:.2f} [DPS] / {eps_v:.2f} [EPS] × 100 = {v:.1f}%")

def _calc_nav(d: Dict[str, Any], yk: str) -> Tuple[float, str]:
    se = d[f"shareholders_equity_{yk}"]; sh = float(d[f"issued_shares_{yk}"])
    v = _ratio(se, sh) * 100
    return (_round2(v), f"NAV = R{se:,.0f} [Shareholders' equity] / {sh:,.0f} [Shares] × 100 = {v:.2f} cents")

def _calc_stock_turnover(d: Dict[str, Any]) -> Tuple[float, str]:
    cos = d["cost_of_sales_curr"]; avg = d["avg_stock"]
    v = _ratio(cos, avg)
    return (_round2(v), f"Stock turnover = R{cos:,.0f} [COS] / R{avg:,.0f} [Avg stock = (R{d['inventories_prev']:,.0f}+R{d['inventories_curr']:,.0f})/2] = {v:.1f} times")

def _calc_stock_holding(d: Dict[str, Any]) -> Tuple[float, str]:
    sto_v, _ = _calc_stock_turnover(d)
    v = _ratio(365.0, sto_v) if sto_v else 0.0
    return (_round2(v), f"Stock holding period = 365 / {sto_v:.1f} [Stock turnover] = {v:.0f} days")

def _calc_debtors_collection(d: Dict[str, Any]) -> Tuple[float, str]:
    avg_d = d["avg_debtors"]; cs = d["credit_sales_curr"]
    v = _ratio(avg_d, cs) * 365
    return (_round2(v), f"Debtors collection = R{avg_d:,.0f} [Avg debtors] / R{cs:,.0f} [Credit sales] × 365 = {v:.0f} days")

def _calc_creditors_payment(d: Dict[str, Any]) -> Tuple[float, str]:
    avg_c = d["avg_creditors"]; cp = d["credit_purchases_curr"]
    v = _ratio(avg_c, cp) * 365
    return (_round2(v), f"Creditors payment = R{avg_c:,.0f} [Avg creditors] / R{cp:,.0f} [Credit purchases] × 365 = {v:.0f} days")


###############################################################################
# Notes-section reference explanations (from curriculum doc)
###############################################################################

_NOTES: Dict[str, str] = {
    "liquidity": (
        "AREA: Liquidity – ability to pay short-term debts.\n"
        "Ideal current ratio ≥ 1.5:1 to 2:1; Acid-test ≥ 1:1.\n"
        "Low acid-test may indicate poor cash management or excessive stock."
    ),
    "profitability": (
        "AREA: Profitability – profit generation from sales.\n"
        "Key: % GP on COS (mark-up), % Op Exp on sales, % Op Profit on sales, % NP on sales.\n"
        "Decreasing op-exp % with increasing op-profit % = better expense control."
    ),
    "risk_gearing": (
        "AREA: Risk & Gearing – reliance on borrowed funds.\n"
        "Debt-equity ratio: lower = less risk. Solvency ratio: higher = more solvent.\n"
        "Positive gearing: ROTCE > loan interest rate. Negative gearing: ROTCE < loan rate."
    ),
    "earnings_returns": (
        "AREA: Earnings & Returns to shareholders.\n"
        "EPS, DPS, DPR, ROSHE, ROTCE.\n"
        "Compare ROSHE to FD rate: if ROSHE > FD rate, shareholders earn better than risk-free."
    ),
    "share_value": (
        "AREA: Value of shares.\n"
        "NAV per share, Market price, Issue price.\n"
        "Issue price > NAV & market = shareholders benefit. CEO buying below NAV = unethical."
    ),
    "shareholding": (
        "AREA: Shareholding & control.\n"
        ">50% = controlling interest. Coalition concerns: ethics, experience, instability."
    ),
    "working_capital_strategies": (
        "Strategies: sales promotion to reduce stock, offer discount for early debtor payment,\n"
        "charge interest for late payment, hand over long overdue to attorneys,\n"
        "negotiate extended credit with creditors."
    ),
}


###############################################################################
# Calc question builder with i-button hints
###############################################################################

def _make_calc_hint(*, prompt: str, calc_fn, d: Dict[str, Any], yk: str = "curr",
                    unit: str = "", mode: str, archetype_key: str, notes_key: str = "") -> Dict[str, Any]:
    value, expl = calc_fn(d, yk) if yk else calc_fn(d)
    full_expl = expl
    if notes_key and notes_key in _NOTES:
        full_expl += "\n\n--- Notes ---\n" + _NOTES[notes_key]
    out = _make_calc(prompt=prompt, correct_value=value, unit=unit, explanation=full_expl,
                     mode=mode, archetype_key=archetype_key)
    if str(mode or "").strip().lower() == "scaffold":
        out["figure_hints"] = expl
    return out


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
    n = max(1, min(20, int(count) if isinstance(count, int) else 1))
    subskill_norm = str(subskill or "mixed").strip().lower()
    qtype_norm = str(question_type or "mixed").strip().lower()
    mode_norm = str(mode or "").strip().lower()
    d = _pick_dataset(r)

    yr = d["year"]; pyr = d["prev_year"]; co = d["company"]

    # Pre-calculate all indicators for both years
    cr_c, cr_ce = _calc_current_ratio(d, "curr"); cr_p, cr_pe = _calc_current_ratio(d, "prev")
    at_c, at_ce = _calc_acid_test(d, "curr"); at_p, at_pe = _calc_acid_test(d, "prev")
    de_c, de_ce = _calc_debt_equity(d, "curr"); de_p, de_pe = _calc_debt_equity(d, "prev")
    sol_c, sol_ce = _calc_solvency(d)
    gpc_c, gpc_ce = _calc_gp_on_cos(d, "curr"); gpc_p, gpc_pe = _calc_gp_on_cos(d, "prev")
    gps_c, gps_ce = _calc_gp_on_sales(d, "curr"); gps_p, gps_pe = _calc_gp_on_sales(d, "prev")
    oe_c, oe_ce = _calc_oe_on_sales(d, "curr"); oe_p, oe_pe = _calc_oe_on_sales(d, "prev")
    op_c, op_ce = _calc_op_on_sales(d, "curr"); op_p, op_pe = _calc_op_on_sales(d, "prev")
    np_c, np_ce = _calc_np_on_sales(d, "curr"); np_p, np_pe = _calc_np_on_sales(d, "prev")
    ro_c, ro_ce = _calc_roshe(d, "curr"); ro_p, ro_pe = _calc_roshe(d, "prev")
    rt_c, rt_ce = _calc_rotce(d, "curr"); rt_p, rt_pe = _calc_rotce(d, "prev")
    eps_c, eps_ce = _calc_eps(d, "curr"); eps_p, eps_pe = _calc_eps(d, "prev")
    dps_c, dps_ce = _calc_dps(d)
    dpr_c, dpr_ce = _calc_dpr(d)
    nav_c, nav_ce = _calc_nav(d, "curr"); nav_p, nav_pe = _calc_nav(d, "prev")
    sto_c, sto_ce = _calc_stock_turnover(d)
    shp_c, shp_ce = _calc_stock_holding(d)
    dcp_c, dcp_ce = _calc_debtors_collection(d)
    cpp_c, cpp_ce = _calc_creditors_payment(d)

    # =====================================================================
    # CALC POOL — all formula-based calculation archetypes
    # =====================================================================
    calc_pool: List[Dict[str, Any]] = []

    # Liquidity
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the current ratio for {yr}.\nCurrent assets = R{d['current_assets_curr']:,.0f}; Current liabilities = R{d['current_liabilities_curr']:,.0f}",
        calc_fn=_calc_current_ratio, d=d, yk="curr", unit=":1", mode=mode_norm,
        archetype_key="g12_ai_ex1_current_ratio", notes_key="liquidity"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the acid-test ratio for {yr}.\nCash = R{d['cash_curr']:,.0f}; Receivables = R{d['receivables_curr']:,.0f}; Current liabilities = R{d['current_liabilities_curr']:,.0f}",
        calc_fn=_calc_acid_test, d=d, yk="curr", unit=":1", mode=mode_norm,
        archetype_key="g12_ai_ex1_acid_test", notes_key="liquidity"))

    # Profitability
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the % gross profit on cost of sales for {yr}.\nGross profit = R{d['gross_profit_curr']:,.0f}; Cost of sales = R{d['cost_of_sales_curr']:,.0f}",
        calc_fn=_calc_gp_on_cos, d=d, yk="curr", unit="%", mode=mode_norm,
        archetype_key="g12_ai_ex1_gp_on_cos", notes_key="profitability"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the % gross profit on sales for {yr}.\nGross profit = R{d['gross_profit_curr']:,.0f}; Sales = R{d['sales_curr']:,.0f}",
        calc_fn=_calc_gp_on_sales, d=d, yk="curr", unit="%", mode=mode_norm,
        archetype_key="g12_ai_ex1_gp_on_sales", notes_key="profitability"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the % operating expenses on sales for {yr}.\nOperating expenses = R{d['operating_expenses_curr']:,.0f}; Sales = R{d['sales_curr']:,.0f}",
        calc_fn=_calc_oe_on_sales, d=d, yk="curr", unit="%", mode=mode_norm,
        archetype_key="g12_ai_ex2_oe_on_sales", notes_key="profitability"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the % operating profit on sales for {yr}.\nOperating profit = R{d['operating_profit_curr']:,.0f}; Sales = R{d['sales_curr']:,.0f}",
        calc_fn=_calc_op_on_sales, d=d, yk="curr", unit="%", mode=mode_norm,
        archetype_key="g12_ai_ex2_op_on_sales", notes_key="profitability"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the % net profit on sales for {yr}.\nNPAT = R{d['net_profit_after_tax_curr']:,.0f}; Sales = R{d['sales_curr']:,.0f}",
        calc_fn=_calc_np_on_sales, d=d, yk="curr", unit="%", mode=mode_norm,
        archetype_key="g12_ai_ex2_np_on_sales", notes_key="profitability"))

    # Risk & Gearing
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the debt : equity ratio for {yr}.\nNCL = R{d['non_current_liabilities_curr']:,.0f}; Shareholders' equity = R{d['shareholders_equity_curr']:,.0f}",
        calc_fn=_calc_debt_equity, d=d, yk="curr", unit=":1", mode=mode_norm,
        archetype_key="g12_ai_ex3_debt_equity", notes_key="risk_gearing"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the solvency ratio for {yr}.\nTotal assets = R{d['total_assets_curr']:,.0f}; Total liabilities = R{d['total_liabilities_curr']:,.0f}",
        calc_fn=_calc_solvency, d=d, yk="", unit=":1", mode=mode_norm,
        archetype_key="g12_ai_ex3_solvency", notes_key="risk_gearing"))
    calc_pool.append(_make_calc_hint(
        prompt=(f"{co}: Calculate the ROTCE for {yr}.\nNPAT = R{d['net_profit_after_tax_curr']:,.0f}; Interest = R{d['interest_on_loan_curr']:,.0f}; "
                f"Equity = R{d['shareholders_equity_curr']:,.0f}; NCL = R{d['non_current_liabilities_curr']:,.0f}"),
        calc_fn=_calc_rotce, d=d, yk="curr", unit="%", mode=mode_norm,
        archetype_key="g12_ai_ex4_rotce", notes_key="risk_gearing"))

    # Earnings & Returns
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate EPS for {yr} in cents.\nNPAT = R{d['net_profit_after_tax_curr']:,.0f}; Issued shares = {d['issued_shares_curr']:,}",
        calc_fn=_calc_eps, d=d, yk="curr", unit="cents", mode=mode_norm,
        archetype_key="g12_ai_ex4_eps", notes_key="earnings_returns"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate DPS for {yr} in cents.\nInterim div = R{d['interim_dividends_curr']:,.0f}; Final div = R{d['final_dividends_curr']:,.0f}; Shares = {d['issued_shares_curr']:,}",
        calc_fn=_calc_dps, d=d, yk="", unit="cents", mode=mode_norm,
        archetype_key="g12_ai_ex4_dps", notes_key="earnings_returns"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the dividend pay-out rate for {yr}.\n(Use your calculated DPS and EPS.)",
        calc_fn=_calc_dpr, d=d, yk="", unit="%", mode=mode_norm,
        archetype_key="g12_ai_ex4_dpr", notes_key="earnings_returns"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate ROSHE for {yr}.\nNPAT = R{d['net_profit_after_tax_curr']:,.0f}; Equity = R{d['shareholders_equity_curr']:,.0f}",
        calc_fn=_calc_roshe, d=d, yk="curr", unit="%", mode=mode_norm,
        archetype_key="g12_ai_ex4_roshe", notes_key="earnings_returns"))

    # Share value
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate NAV per share for {yr} in cents.\nEquity = R{d['shareholders_equity_curr']:,.0f}; Shares = {d['issued_shares_curr']:,}",
        calc_fn=_calc_nav, d=d, yk="curr", unit="cents", mode=mode_norm,
        archetype_key="g12_ai_ex5_nav", notes_key="share_value"))

    # Working capital management
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate stock turnover rate for {yr}.\nCOS = R{d['cost_of_sales_curr']:,.0f}; Opening stock = R{d['inventories_prev']:,.0f}; Closing stock = R{d['inventories_curr']:,.0f}",
        calc_fn=_calc_stock_turnover, d=d, yk="", unit="times", mode=mode_norm,
        archetype_key="g12_ai_ex5_stock_turnover", notes_key="liquidity"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate the average stock holding period for {yr} in days.",
        calc_fn=_calc_stock_holding, d=d, yk="", unit="days", mode=mode_norm,
        archetype_key="g12_ai_ex5_stock_holding", notes_key="liquidity"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate debtors collection period for {yr}.\nOpening debtors = R{d['trade_debtors_prev']:,.0f}; Closing debtors = R{d['trade_debtors_curr']:,.0f}; Credit sales = R{d['credit_sales_curr']:,.0f}",
        calc_fn=_calc_debtors_collection, d=d, yk="", unit="days", mode=mode_norm,
        archetype_key="g12_ai_ex5_debtors_collection", notes_key="liquidity"))
    calc_pool.append(_make_calc_hint(
        prompt=f"{co}: Calculate creditors payment period for {yr}.\nOpening creditors = R{d['trade_creditors_prev']:,.0f}; Closing creditors = R{d['trade_creditors_curr']:,.0f}; Credit purchases = R{d['credit_purchases_curr']:,.0f}",
        calc_fn=_calc_creditors_payment, d=d, yk="", unit="days", mode=mode_norm,
        archetype_key="g12_ai_ex5_creditors_payment", notes_key="liquidity"))

    # =====================================================================
    # TYPED POOL — interpretation / comment archetypes (Q1-Q5)
    # =====================================================================
    typed_pool: List[Dict[str, Any]] = []

    # --- Q1 / Q5.1: Profitability & expense management ---
    oe_trend = "decreased" if oe_c < oe_p else "increased"
    op_trend = "increased" if op_c > op_p else "decreased"
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): Quote and explain TWO financial indicators which show the company "
                f"manages its expenses more efficiently compared to {pyr}."),
        sample_answer=(
            f"% Operating expenses on sales {oe_trend} from {oe_p:.1f}% to {oe_c:.1f}%.\n"
            f"  [i] {oe_ce}\n"
            f"% Operating profit on sales {op_trend} from {op_p:.1f}% to {op_c:.1f}%.\n"
            f"  [i] {op_ce}\n"
            + ("Expenses are well controlled." if oe_trend == "decreased" and op_trend == "increased"
               else "Expenses are NOT well controlled — review cost management.")
            + f"\n\n{_NOTES['profitability']}"
        ), mode=mode_norm, archetype_key="g12_ai_q5_profitability_expense_management"))

    # --- Q1: Dividend pay-out policy (EPS vs DPS) ---
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): Compare EPS and DPS. Comment on whether the company retained profit. "
                "Calculate the dividend pay-out rate."),
        sample_answer=(
            f"EPS = {eps_c:.2f} cents (if ALL profit declared).\n  [i] {eps_ce}\n"
            f"DPS = {dps_c:.2f} cents (what really happened).\n  [i] {dps_ce}\n"
            f"DPR = {dpr_c:.1f}%.\n  [i] {dpr_ce}\n"
            + (f"DPS < EPS: Company retained {eps_c - dps_c:.2f}c per share."
               if dps_c < eps_c else "DPS ≥ EPS: Retained income may have been used.")
            + f"\n\n{_NOTES['earnings_returns']}"
        ), mode=mode_norm, archetype_key="g12_ai_q1_dividend_payout_policy"))

    # --- Q1 / Q5.3: Earnings & returns (ROSHE vs FD rate) ---
    roshe_vs = "above" if ro_c > d["fd_interest_rate_curr"] else "below"
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): Should shareholders be satisfied with returns? "
                f"Quote EPS and ROSHE. Compare ROSHE to FD rate of {d['fd_interest_rate_curr']}%."),
        sample_answer=(
            f"EPS: {eps_c:.2f} cents.\n  [i] {eps_ce}\n"
            f"ROSHE: {ro_c:.2f}%.\n  [i] {ro_ce}\n"
            f"ROSHE is {roshe_vs} FD rate of {d['fd_interest_rate_curr']}% by {abs(ro_c - d['fd_interest_rate_curr']):.2f}%.\n"
            + ("Shareholders should be satisfied." if roshe_vs == "above"
               else "Shareholders may NOT be satisfied — returns below risk-free alternative.")
            + f"\n\n{_NOTES['earnings_returns']}"
        ), mode=mode_norm, archetype_key="g12_ai_q1_earnings_returns_eps_roshe"))

    # --- Q1: Financing strategies (rights issue) ---
    maj_pct_prev = _round2(d["majority_shares_prev"] / d["issued_shares_prev"] * 100)
    maj_pct_curr = _round2(d["majority_shares_curr"] / d["issued_shares_curr"] * 100)
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): {d['majority_name']} owned {d['majority_shares_prev']:,} shares before the rights issue "
                f"({d['rights_ratio_num']} for every {d['rights_ratio_den']} held). "
                "Calculate the new shareholding % and comment on the impact."),
        sample_answer=(
            f"Before: {d['majority_shares_prev']:,} / {d['issued_shares_prev']:,} = {maj_pct_prev:.2f}%.\n"
            f"Rights shares: {d['majority_shares_from_rights']:,}. After: {d['majority_shares_curr']:,} / {d['issued_shares_curr']:,} = {maj_pct_curr:.2f}%.\n"
            + (f"Still holds majority (>{50}%)." if maj_pct_curr > 50 else "No longer holds majority.")
            + f"\n\n{_NOTES['shareholding']}"
        ), mode=mode_norm, archetype_key="g12_ai_q1_financing_rights_issue"))

    # --- Q2: Liquidity position comment ---
    cr_trend = "improved" if cr_c > cr_p else "declined"
    at_trend = "improved" if at_c > at_p else "declined"
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): Comment on the liquidity position compared to {pyr}. "
                "Quote the current ratio and acid-test ratio."),
        sample_answer=(
            f"Current ratio: {cr_p:.2f}:1 → {cr_c:.2f}:1 ({cr_trend}).\n  [i] {cr_ce}\n"
            f"Acid-test: {at_p:.2f}:1 → {at_c:.2f}:1 ({at_trend}).\n  [i] {at_ce}\n"
            "Higher ratios = better ability to pay short-term debts."
            + f"\n\n{_NOTES['liquidity']}"
        ), mode=mode_norm, archetype_key="g12_ai_q2_liquidity_position_comment"))

    # --- Q3: Working capital concern (acid-test + stock turnover) ---
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): The CEO is concerned about working capital. "
                "Quote TWO financial indicators and explain why the concern is justified."),
        sample_answer=(
            f"Acid-test: {at_p:.2f}:1 → {at_c:.2f}:1.\n  [i] {at_ce}\n"
            + ("Below 1:1 — may struggle to meet short-term debts.\n" if at_c < 1.0 else "")
            + f"Stock turnover: {sto_c:.1f} times.\n  [i] {sto_ce}\n"
            f"Stock holding period: {shp_c:.0f} days.\n  [i] {shp_ce}\n"
            "Too much cash tied up in stock / poor working capital management."
            + f"\n\n{_NOTES['liquidity']}"
        ), mode=mode_norm, archetype_key="g12_ai_q3_liquidity_concern_working_capital"))

    # --- Q3: Risk & gearing — loan objection ---
    de_trend = "increased" if de_c > de_p else "decreased"
    gearing = "positive" if rt_c > d["loan_interest_rate_curr"] else "negative"
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): A shareholder proposed acquiring a new loan. The CEO disagreed. "
                "Explain why you agree with the CEO. Quote TWO financial indicators."),
        sample_answer=(
            f"Debt-equity: {de_p:.2f}:1 → {de_c:.2f}:1 ({de_trend}). "
            + ("High risk." if de_c > 0.5 else "Moderate risk.") + "\n  [i] " + de_ce + "\n"
            f"ROTCE: {rt_p:.2f}% → {rt_c:.2f}%.\n  [i] {rt_ce}\n"
            f"ROTCE of {rt_c:.2f}% vs loan rate {d['loan_interest_rate_curr']}% = {gearing} gearing.\n"
            + ("Loan is NOT used effectively — negative gearing." if gearing == "negative"
               else "Loan is used effectively — but debt-equity already high.")
            + f"\n\n{_NOTES['risk_gearing']}"
        ), mode=mode_norm, archetype_key="g12_ai_q3_risk_gearing_loan_objection"))

    # --- Q4.1: Liquidity — directors happy ---
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): The directors are happy about liquidity. "
                "Quote TWO financial indicators with figures to support this."),
        sample_answer=(
            f"Stock turnover: {sto_c:.1f} times.\n  [i] {sto_ce}\n"
            f"Debtors collection: {dcp_c:.0f} days.\n  [i] {dcp_ce}\n"
            + (f"{dcp_c:.0f} days is within 30-60 day benchmark." if dcp_c <= 60 else f"{dcp_c:.0f} days exceeds benchmark.")
            + f"\n\n{_NOTES['liquidity']}"
        ), mode=mode_norm, archetype_key="g12_ai_q4_liquidity_support_indicators"))

    # --- Q4.2: Share issue price satisfaction ---
    ipp_cents = d["issue_price_per_share"] * 100
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): New shares issued at {ipp_cents:.0f} cents per share. "
                "Are shareholders satisfied? Quote TWO indicators."),
        sample_answer=(
            f"NAV per share: {nav_c:.2f} cents.\n  [i] {nav_ce}\n"
            f"Market price: {d['market_price_curr']} cents.\n"
            f"Issue price of {ipp_cents:.0f}c vs NAV of {nav_c:.2f}c: "
            + ("above NAV — shareholders benefit.\n" if ipp_cents > nav_c else "below NAV — dilution at discount.\n")
            + f"Issue price vs market price of {d['market_price_curr']}c: "
            + ("above market — premium received." if ipp_cents > d["market_price_curr"] else "below market.")
            + f"\n\n{_NOTES['share_value']}"
        ), mode=mode_norm, archetype_key="g12_ai_q4_share_issue_price_satisfaction"))

    # --- Q4.3: Loan repayment decision ---
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): A director feels the loan should be repaid ASAP. "
                "Do you agree? Quote TWO indicators."),
        sample_answer=(
            f"Debt-equity: {de_c:.2f}:1.\n  [i] {de_ce}\n"
            + (f"Low risk ({de_c:.2f}:1) — business can borrow more.\n" if de_c < 0.3 else "")
            + f"ROTCE: {rt_c:.2f}% vs loan rate {d['loan_interest_rate_curr']}%.\n  [i] {rt_ce}\n"
            + (f"Positive gearing — keep the loan, it benefits shareholders." if gearing == "positive"
               else "Negative gearing — repay to reduce losses.")
            + f"\n\n{_NOTES['risk_gearing']}"
        ), mode=mode_norm, archetype_key="g12_ai_q4_loan_repayment_decision"))

    # --- Q4.4: Shareholder dissatisfaction (returns & dividends) ---
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): Shareholders are NOT satisfied with returns and dividends. "
                "Quote TWO indicators with figures."),
        sample_answer=(
            f"ROSHE: {ro_p:.2f}% → {ro_c:.2f}%.\n  [i] {ro_ce}\n"
            f"ROSHE of {ro_c:.2f}% vs FD rate {d['fd_interest_rate_curr']}%: "
            + ("below" if ro_c < d["fd_interest_rate_curr"] else "above") + " alternative.\n"
            f"DPS: {dps_c:.2f} cents.\n  [i] {dps_ce}\n"
            f"EPS: {eps_c:.2f} cents.\n  [i] {eps_ce}\n"
            + ("DPS decreased — shareholders unhappy." if dps_c < eps_c else "")
            + f"\n\n{_NOTES['earnings_returns']}"
        ), mode=mode_norm, archetype_key="g12_ai_q4_shareholder_dissatisfaction_return_dividends"))

    # --- Q4.5.1: Shareholding coalition ---
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): {d['second_name']} ({d['second_pct_curr']}%) and {d['majority_name']} "
                f"plan to combine votes at the AGM. Their combined previous holding was "
                f"{d['second_pct_prev'] + maj_pct_prev:.1f}%, now {d['second_pct_curr'] + maj_pct_curr:.1f}%. "
                "Explain ONE possible reason."),
        sample_answer=(
            f"Combined: {d['second_pct_curr'] + maj_pct_curr:.1f}% "
            + ("> 50% — controlling interest. They can influence major decisions."
               if (d['second_pct_curr'] + maj_pct_curr) > 50 else "< 50% — still minority.")
            + f"\n\n{_NOTES['shareholding']}"
        ), mode=mode_norm, archetype_key="g12_ai_q4_shareholding_coalition_voting_power"))

    # --- Q4.5.2: Concerns about coalition ---
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): As a shareholder, why would you be concerned about "
                f"{d['second_name']} and {d['majority_name']}'s coalition strategy? TWO points."),
        sample_answer=(
            "1. Whether they will use powers to benefit the company or have unethical motives.\n"
            "2. Their past experience in directing a company — skill and knowledge.\n"
            "3. Effect on company if coalition breaks — instability in decision making.\n"
            "4. Quality of their contributions at previous AGMs."
            + f"\n\n{_NOTES['shareholding']}"
        ), mode=mode_norm, archetype_key="g12_ai_q4_shareholding_concerns"))

    # --- Q5.2: Liquidity strategies ---
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): Suggest strategies to improve net working capital. "
                "Quote TWO financial indicators."),
        sample_answer=(
            f"Acid-test: {at_c:.2f}:1.\n  [i] {at_ce}\n"
            f"Debtors collection: {dcp_c:.0f} days.\n  [i] {dcp_ce}\n"
            "Strategies:\n"
            "• Sales promotion to reduce excess stock\n"
            "• Offer discount for early debtor payment / charge interest for late payment\n"
            "• Hand over long overdue accounts to attorneys"
            + f"\n\n{_NOTES['working_capital_strategies']}"
        ), mode=mode_norm, archetype_key="g12_ai_q5_liquidity_strategies_working_capital"))

    # --- Q5.3: Dividend pay-out policy comment ---
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): Comment on the dividend pay-out policy. "
                "Provide TWO reasons why directors may have changed policy."),
        sample_answer=(
            f"DPR: {dpr_c:.1f}%.\n  [i] {dpr_ce}\n"
            + ("DPR > 100% — paying out more than earned. Retained income used.\n" if dpr_c > 100
               else f"DPR of {dpr_c:.1f}% — " + ("high" if dpr_c > 60 else "moderate") + " pay-out.\n")
            + "Reasons: 1) Satisfying shareholders / keep them happy.\n"
            "2) No plans to expand / attract prospective shareholders."
            + f"\n\n{_NOTES['earnings_returns']}"
        ), mode=mode_norm, archetype_key="g12_ai_q5_dividend_payout_comment"))

    # --- Q5.4: CEO buyback ethics ---
    ceo_price = d["ceo_buyback_price_cents"]
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): {d['ceo_name']} wants to buy {d['ceo_buyback_shares']:,} shares at "
                f"R{ceo_price/100:.2f} per share without informing shareholders. React."),
        sample_answer=(
            f"NAV per share: {nav_c:.2f} cents = R{nav_c/100:.2f}.\n  [i] {nav_ce}\n"
            f"Market price: {d['market_price_curr']} cents = R{d['market_price_curr']/100:.2f}.\n"
            f"CEO offer R{ceo_price/100:.2f} vs NAV R{nav_c/100:.2f}: "
            + ("below NAV" if ceo_price < nav_c else "above NAV") + ".\n"
            f"CEO offer vs market R{d['market_price_curr']/100:.2f}: "
            + ("below market" if ceo_price < d["market_price_curr"] else "above market") + ".\n"
            "Unethical — insider trading. Not happy."
            + f"\n\n{_NOTES['share_value']}"
        ), mode=mode_norm, archetype_key="g12_ai_q5_value_shares_buyback_ethics"))

    # --- Q5.5: Risk & gearing comment ---
    typed_pool.append(_make_typed(
        prompt=(f"{co} ({yr}): Comment on the degree of risk and gearing."),
        sample_answer=(
            f"Debt-equity: {de_p:.2f}:1 → {de_c:.2f}:1 ({de_trend}).\n  [i] {de_ce}\n"
            + ("Low risk.\n" if de_c < 0.5 else "High risk.\n")
            + f"ROTCE: {rt_c:.2f}% vs loan rate {d['loan_interest_rate_curr']}%.\n  [i] {rt_ce}\n"
            + (f"ROTCE above loan rate = {gearing} gearing — low risk."
               if gearing == "positive" else f"ROTCE below loan rate = {gearing} gearing — high risk.")
            + f"\n\n{_NOTES['risk_gearing']}"
        ), mode=mode_norm, archetype_key="g12_ai_q5_risk_gearing_comment"))

    # =====================================================================
    # SUBSKILL ROUTING
    # =====================================================================
    _CALC_KEYS: Dict[str, List[int]] = {}
    for _k, _idx in [
        ("current-ratio", [0]), ("current_ratio", [0]),
        ("acid-test", [1]), ("acid_test", [1]),
        ("gp-on-cos", [2]), ("gp_on_cos", [2]), ("mark-up", [2]),
        ("gp-on-sales", [3]), ("gp_on_sales", [3]),
        ("oe-on-sales", [4]), ("oe_on_sales", [4]), ("operating-expenses", [4]),
        ("op-on-sales", [5]), ("op_on_sales", [5]), ("operating-profit", [5]),
        ("np-on-sales", [6]), ("np_on_sales", [6]), ("net-profit", [6]),
        ("debt-equity", [7]), ("debt_equity", [7]),
        ("solvency", [8]),
        ("rotce", [9]),
        ("eps", [10]),
        ("dps", [11]),
        ("dpr", [12]), ("dividend-payout-rate", [12]),
        ("roshe", [13]),
        ("nav", [14]),
        ("stock-turnover", [15]), ("stock_turnover", [15]),
        ("stock-holding", [16]), ("stock_holding", [16]),
        ("debtors-collection", [17]), ("debtors_collection", [17]),
        ("creditors-payment", [18]), ("creditors_payment", [18]),
    ]:
        _CALC_KEYS[_k] = _idx

    pools = {
        "calc": calc_pool,
        "calculations": calc_pool,
        "typed": typed_pool,
        "comments": typed_pool,
        "interpretation": typed_pool,
        "mixed": calc_pool + typed_pool,
    }

    pool = pools.get(subskill_norm, None)
    if pool is None:
        # Check if subskill maps to a specific calc index
        if subskill_norm in _CALC_KEYS:
            idxs = _CALC_KEYS[subskill_norm]
            pool = [calc_pool[i] for i in idxs if i < len(calc_pool)]
        else:
            pool = pools["mixed"]

    if qtype_norm != "mixed":
        if qtype_norm == "calc":
            pool = [q for q in pool if q.get("question_type") == "calc"]
        elif qtype_norm in {"typed", "text"}:
            pool = [q for q in pool if q.get("question_type") == "typed"]

    if not pool:
        pool = pools["mixed"]

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        out.append(r.choice(pool))
    return out
