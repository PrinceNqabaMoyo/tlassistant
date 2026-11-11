"""
Grade 10 Accounting: Analysis and Interpretation of Financial Statements (Sole Trader)
Strictly aligned with South African National Curriculum Standards for Grade 10 Accounting (Term 3/4).
No partnership or company ratios are included.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "profitability_ratios_table",
    "liquidity_ratios_table",
    "solvency_ratio_and_net_assets",
    "return_on_owners_equity",
    "profitability_and_markup_commentary",
    "liquidity_and_working_capital_commentary",
    "comprehensive_sole_trader_financial_analysis",
]

TRADERS = [
    ("Khumalo Sports Emporium", "B. Khumalo"),
    ("Jacaranda Home Decor", "M. Pretorius"),
    ("Coastal Cycling Traders", "A. Naidoo"),
    ("Savanna Outdoor Gear", "D. Molefe"),
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_profitability_ratios(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    sales = 600000
    cos = 400000
    gp = sales - cos
    op_exp = r.choice([120000, 132000, 150000])
    op_profit = gp - op_exp
    net_profit = op_profit - 12000

    gp_on_sales = round((gp / sales) * 100, 1)
    gp_on_cos = round((gp / cos) * 100, 1)
    op_exp_on_sales = round((op_exp / sales) * 100, 1)
    net_prof_on_sales = round((net_profit / sales) * 100, 1)

    headers = ["Profitability Indicator", "Formula", "Calculated Percentage (%)"]
    rows = [
        ["% Gross profit on sales", "(Gross Profit ÷ Sales) × 100", "{r0_c2}"],
        ["% Gross profit on cost of sales (Mark-up %)", "(Gross Profit ÷ Cost of Sales) × 100", "{r1_c2}"],
        ["% Operating expenses on sales", "(Operating Expenses ÷ Sales) × 100", "{r2_c2}"],
        ["% Net profit on sales", "(Net Profit ÷ Sales) × 100", "{r3_c2}"],
    ]
    correct_map = {
        "r0_c2": gp_on_sales,
        "r1_c2": gp_on_cos,
        "r2_c2": op_exp_on_sales,
        "r3_c2": net_prof_on_sales,
    }
    worked = (
        f"**Profitability Indicators ({firm})**\n\n"
        f"- **% Gross profit on sales**: `(R{gp:,} ÷ R{sales:,}) × 100 = {gp_on_sales}%`\n"
        f"- **% Mark-up achieved**: `(R{gp:,} ÷ R{cos:,}) × 100 = {gp_on_cos}%`\n"
        f"- **% Operating expenses on sales**: `(R{op_exp:,} ÷ R{sales:,}) × 100 = {op_exp_on_sales}%`\n"
        f"- **% Net profit on sales**: `(R{net_profit:,} ÷ R{sales:,}) × 100 = {net_prof_on_sales}%`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "profitability_ratios_table",
        "question_text": (
            f"**{firm}** reported the following figures for the year:\n"
            f"- Sales: **R{sales:,}**\n"
            f"- Cost of sales: **R{cos:,}** (Gross profit: **R{gp:,}**)\n"
            f"- Operating expenses: **R{op_exp:,}**\n"
            f"- Net profit for the year: **R{net_profit:,}**\n\n"
            f"Calculate the four profitability percentages (rounded to 1 decimal place)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "All profitability ratios express profit or expenses as a percentage of Sales, except Mark-up % which uses Cost of Sales as the denominator.",
            "Divide each numerator by the denominator shown in the Formula column and multiply by 100.",
            worked,
        ),
    }


def _gen_liquidity_ratios(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    curr_liab = r.choice([40000, 50000, 60000])
    inv = curr_liab * r.choice([1.2, 1.4, 1.5])
    inv = int(inv)
    rec_and_cash = int(curr_liab * r.choice([1.0, 1.2, 1.3]))
    curr_assets = inv + rec_and_cash

    curr_ratio_x = round(curr_assets / curr_liab, 2)
    acid_ratio_x = round((curr_assets - inv) / curr_liab, 2)
    net_wc = curr_assets - curr_liab

    headers = ["Liquidity Measure", "Formula", "Answer"]
    rows = [
        ["Current Assets (Total)", "Inventories + Receivables + Cash", "{r0_c2}"],
        ["Net Working Capital (R)", "Current Assets - Current Liabilities", "{r1_c2}"],
        ["Current Ratio (enter X in X : 1)", "Current Assets : Current Liabilities", "{r2_c2}"],
        ["Acid-Test Ratio (enter X in X : 1)", "(Current Assets - Inventories) : Current Liabilities", "{r3_c2}"],
    ]
    correct_map = {
        "r0_c2": curr_assets,
        "r1_c2": net_wc,
        "r2_c2": curr_ratio_x,
        "r3_c2": acid_ratio_x,
    }
    worked = (
        f"**Liquidity Analysis ({firm})**\n\n"
        f"- **Current Assets**: `R{inv:,} + R{rec_and_cash:,} = R{curr_assets:,}`\n"
        f"- **Net Working Capital**: `R{curr_assets:,} - R{curr_liab:,} = R{net_wc:,}`\n"
        f"- **Current Ratio**: `R{curr_assets:,} : R{curr_liab:,} = {curr_ratio_x} : 1`\n"
        f"- **Acid-Test Ratio**: `(R{curr_assets:,} - R{inv:,}) : R{curr_liab:,} = {acid_ratio_x} : 1`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "liquidity_ratios_table",
        "question_text": (
            f"**{firm}** has **Inventories of R{inv:,}**, **Trade receivables and Cash of R{rec_and_cash:,}**, "
            f"and **Current liabilities of R{curr_liab:,}**. Complete the liquidity table."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Liquidity measures a sole trader's ability to pay off short-term debts (Current Liabilities) as they fall due.",
            "Remember to deduct Inventories from Current Assets when calculating the Acid-Test Ratio numerator.",
            worked,
        ),
    }


def _gen_solvency_ratio(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    non_curr_liab = r.choice([120000, 150000, 180000])
    curr_liab = r.choice([60000, 50000, 70000])
    tot_liab = non_curr_liab + curr_liab
    mult = r.choice([2.2, 2.5, 2.8, 3.0])
    tot_assets = int(tot_liab * mult)
    net_assets = tot_assets - tot_liab

    headers = ["Solvency Indicator", "Calculation / Formula", "Answer"]
    rows = [
        ["Total Liabilities (R)", "Non-Current Liabilities + Current Liabilities", "{r0_c2}"],
        ["Net Assets / Owner's Equity (R)", "Total Assets - Total Liabilities", "{r1_c2}"],
        ["Solvency Ratio (enter X in X : 1)", "Total Assets : Total Liabilities", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c2": tot_liab,
        "r1_c2": net_assets,
        "r2_c2": mult,
    }
    worked = (
        f"**Solvency Analysis ({firm})**\n\n"
        f"- **Total Liabilities**: `R{non_curr_liab:,} + R{curr_liab:,} = R{tot_liab:,}`\n"
        f"- **Net Assets (Owner's Equity)**: `R{tot_assets:,} - R{tot_liab:,} = R{net_assets:,}`\n"
        f"- **Solvency Ratio**: `R{tot_assets:,} ÷ R{tot_liab:,} = {mult} : 1`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "solvency_ratio_and_net_assets",
        "question_text": (
            f"**{firm}** has **Total Assets of R{tot_assets:,}**, **Non-Current Liabilities of R{non_curr_liab:,}**, "
            f"and **Current Liabilities of R{curr_liab:,}**. Calculate the solvency figures in the table."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Solvency measures whether Total Assets exceed Total Liabilities over the long term.",
            "Sum Non-Current and Current Liabilities first, then divide Total Assets by Total Liabilities.",
            worked,
        ),
    }


def _gen_return_on_owners_equity(r: random.Random) -> Dict[str, Any]:
    firm, owner = r.choice(TRADERS)
    open_eq = r.choice([400000, 500000, 600000])
    close_eq = open_eq + 100000
    avg_eq = (open_eq + close_eq) // 2
    roe_pct = r.choice([16.0, 18.0, 20.0, 22.0])
    net_profit = int(avg_eq * (roe_pct / 100))

    headers = ["Return on Owner's Equity (Sole Trader)", "Formula", "Answer"]
    rows = [
        ["Average Owner's Equity (R)", "(Opening Equity + Closing Equity) ÷ 2", "{r0_c2}"],
        ["% Return on Average Owner's Equity (%)", "(Net Profit ÷ Average Owner's Equity) × 100", "{r1_c2}"],
        ["Interest rate on alternative fixed deposit investment (%)", "Benchmark bank fixed deposit rate", "8.5%"],
    ]
    correct_map = {
        "r0_c2": avg_eq,
        "r1_c2": roe_pct,
    }
    worked = (
        f"**Return on Owner's Equity ({firm} — {owner})**\n\n"
        f"- **Average Owner's Equity**: `(R{open_eq:,} + R{close_eq:,}) ÷ 2 = R{avg_eq:,}`\n"
        f"- **% Return on Owner's Equity**: `(R{net_profit:,} ÷ R{avg_eq:,}) × 100 = {roe_pct}%`\n"
        f"- Since `{roe_pct}%` exceeds the fixed deposit rate of `8.5%`, {owner} earned a favourable return on capital invested."
    )
    return {
        "question_type": "table_fill",
        "subskill": "return_on_owners_equity",
        "question_text": (
            f"**{owner}**, owner of **{firm}**, had **Opening Owner's Equity of R{open_eq:,}** and **Closing Owner's Equity of R{close_eq:,}**. "
            f"Net profit for the year was **R{net_profit:,}**. Calculate the Average Owner's Equity and the % Return on Average Owner's Equity."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Return on Owner's Equity compares Net Profit to the average capital employed by the sole trader during the year.",
            "Average the opening and closing equity balances first, then divide Net Profit by that average and multiply by 100.",
            worked,
        ),
    }


def _gen_profitability_commentary(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    target_mu = 60
    actual_mu = r.choice([48, 52, 54])
    exp_prev = 24.5
    exp_curr = 19.8

    headers = ["Indicator", "Previous Year", "Current Year", "Target / Benchmark", "Evaluation (Improved / Declined / Below Target)"]
    rows = [
        ["Mark-up % achieved on Cost of Sales", "58%", f"{actual_mu}%", f"{target_mu}%", "{r0_c4}"],
        ["% Operating expenses on sales", f"{exp_prev}%", f"{exp_curr}%", "22.0%", "{r1_c4}"],
        ["% Net profit on sales", "12.2%", "15.4%", "14.0%", "{r2_c4}"],
    ]
    correct_map = {
        "r0_c4": "Below Target",
        "r1_c4": "Improved",
        "r2_c4": "Improved",
    }
    worked = (
        f"**Profitability & Mark-up Evaluation ({firm})**\n\n"
        f"- **Mark-up % (`{actual_mu}%` vs target `{target_mu}%`)**: **Below Target** (likely due to trade discounts granted, seasonal clearance sales, or stock theft).\n"
        f"- **% Operating expenses on sales (`{exp_prev}%` to `{exp_curr}%`)**: **Improved** (better cost control reduced expenses relative to turnover).\n"
        f"- **% Net profit on sales (`12.2%` to `15.4%`)**: **Improved** (exceeded the `14.0%` benchmark)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "profitability_and_markup_commentary",
        "question_text": (
            f"Evaluate the profitability trends of **{firm}** by entering **Improved**, **Declined**, or **Below Target** in the final column."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "A lower operating expense percentage on sales is an improvement because less revenue is consumed by overheads.",
            "Compare the achieved mark-up against the target mark-up, and compare current year expense/profit ratios against the previous year.",
            worked,
        ),
    }


def _gen_liquidity_commentary(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    headers = ["Liquidity Scenario", "Current Ratio", "Acid-Test Ratio", "Diagnostic Conclusion (Healthy Liquidity / Overstocked in Inventory / Cash Flow Strain)"]
    rows = [
        ["Year 1", "2.1 : 1", "1.1 : 1", "{r0_c3}"],
        ["Year 2", "3.4 : 1", "0.5 : 1", "{r1_c3}"],
        ["Year 3", "0.8 : 1", "0.4 : 1", "{r2_c3}"],
    ]
    correct_map = {
        "r0_c3": "Healthy Liquidity",
        "r1_c3": "Overstocked in Inventory",
        "r2_c3": "Cash Flow Strain",
    }
    worked = (
        f"**Liquidity Diagnostic Commentary ({firm})**\n\n"
        f"- **Year 1 (`2.1 : 1` and `1.1 : 1`)**: **Healthy Liquidity** — sufficient liquid assets to cover immediate debts without excess idle stock.\n"
        f"- **Year 2 (`3.4 : 1` and `0.5 : 1`)**: **Overstocked in Inventory** — high current ratio but low acid-test ratio shows working capital is tied up in slow-moving trading stock.\n"
        f"- **Year 3 (`0.8 : 1` and `0.4 : 1`)**: **Cash Flow Strain** — current assets are insufficient to cover current liabilities."
    )
    return {
        "question_type": "table_fill",
        "subskill": "liquidity_and_working_capital_commentary",
        "question_text": (
            f"Analyse the three liquidity scenarios for **{firm}** and classify each year as **Healthy Liquidity**, "
            f"**Overstocked in Inventory**, or **Cash Flow Strain**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Compare the Current Ratio with the Acid-Test Ratio to see how much of Current Assets is tied up in Trading Stock.",
            "When Current Ratio is high (3.4:1) but Acid-Test is below 1:1 (0.5:1), the business is holding too much inventory.",
            worked,
        ),
    }


def _gen_comprehensive_analysis(r: random.Random) -> Dict[str, Any]:
    firm, owner = r.choice(TRADERS)
    sales = 800000
    cos = 500000
    gp = 300000
    ca = 180000
    inv = 90000
    cl = 90000

    mu = round((gp / cos) * 100, 1)
    gp_margin = round((gp / sales) * 100, 1)
    curr_r = round(ca / cl, 1)
    acid_r = round((ca - inv) / cl, 1)

    headers = ["Financial Indicator", "Calculation Data", "Calculated Result"]
    rows = [
        ["Mark-up % achieved (%)", f"Gross Profit R{gp:,} on Cost of Sales R{cos:,}", "{r0_c2}"],
        ["Gross profit % on sales (%)", f"Gross Profit R{gp:,} on Sales R{sales:,}", "{r1_c2}"],
        ["Current Ratio (enter X in X : 1)", f"Current Assets R{ca:,} : Current Liabilities R{cl:,}", "{r2_c2}"],
        ["Acid-Test Ratio (enter X in X : 1)", f"(R{ca:,} - Inventory R{inv:,}) : R{cl:,}", "{r3_c2}"],
    ]
    correct_map = {
        "r0_c2": mu,
        "r1_c2": gp_margin,
        "r2_c2": curr_r,
        "r3_c2": acid_r,
    }
    worked = (
        f"**Comprehensive Sole Trader Financial Analysis ({firm} — {owner})**\n\n"
        f"- **Mark-up %**: `(R{gp:,} ÷ R{cos:,}) × 100 = {mu}%`\n"
        f"- **Gross Profit Margin**: `(R{gp:,} ÷ R{sales:,}) × 100 = {gp_margin}%`\n"
        f"- **Current Ratio**: `R{ca:,} ÷ R{cl:,} = {curr_r} : 1`\n"
        f"- **Acid-Test Ratio**: `(R{ca:,} - R{inv:,}) ÷ R{cl:,} = {acid_r} : 1`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "comprehensive_sole_trader_financial_analysis",
        "question_text": (
            f"Complete the comprehensive financial ratio summary table for **{firm}** (owner: {owner})."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Ensure you use Cost of Sales as denominator for Mark-up % and Sales as denominator for Gross Profit %.",
            "For the liquidity ratios, divide by Current Liabilities (`R90,000`).",
            worked,
        ),
    }


_BUILDERS = {
    "profitability_ratios_table": _gen_profitability_ratios,
    "liquidity_ratios_table": _gen_liquidity_ratios,
    "solvency_ratio_and_net_assets": _gen_solvency_ratio,
    "return_on_owners_equity": _gen_return_on_owners_equity,
    "profitability_and_markup_commentary": _gen_profitability_commentary,
    "liquidity_and_working_capital_commentary": _gen_liquidity_commentary,
    "comprehensive_sole_trader_financial_analysis": _gen_comprehensive_analysis,
}


def generate_questions(
    count: int = 1,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    r = random.Random(seed)
    out: List[Dict[str, Any]] = []
    for i in range(count):
        chosen = subskill if (subskill and subskill in _BUILDERS) else r.choice(SUBSKILLS)
        q = _BUILDERS[chosen](r)
        q["subskill"] = chosen
        q["topic"] = "Analysis and Interpretation of Financial Statements"
        q["grade"] = "10"
        out.append(q)
    return out
