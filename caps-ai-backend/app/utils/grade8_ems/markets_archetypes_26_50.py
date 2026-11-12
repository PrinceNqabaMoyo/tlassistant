"""Grade 8 EMS — The Markets Archetypes 26–50.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 4/02. The markets.md.
Covers Factor Market, Labour Market, Financial Markets (JSE Capital & Money Market), Overdrafts & Price Signals.
Zero-LLM, deterministic via rng: random.Random, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import NAMES, SUPPLIERS
from app.utils.grade8_ems.markets_archetypes_01_25 import (
    _BANKS,
    _make_mcq,
    _make_rubric,
    _make_table,
    _make_typed,
    fmt_r,
    get_ems_scenario,
    svg_circular_markets,
    svg_market_card,
)


def _b26_factor_market_definition_services(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    wage = rng.randint(6, 15) * 1000
    prompt = (
        f"In the Factor Market, {s['business']} in {s['area']} pays {fmt_r(wage)}/month to skilled technicians from local households. "
        f"Economically, what is actually being bought and sold in the Factor Market?"
    )
    ans = "The productive SERVICES of factors of production (labour, land, capital, entrepreneurship) supplied by households"
    opts = [
        "The productive SERVICES of factors of production (labour, land, capital, entrepreneurship) supplied by households",
        "Legal ownership of human employees as permanent company property",
        "Finished bread, clothing, and household appliances for direct consumption",
        "VAT refunds paid directly by the municipal water department",
    ]
    exp = f"In the Factor Market, businesses buy the *productive services* of land, labour ({fmt_r(wage)}/month), capital, and entrepreneurship from households — not workers themselves."
    return _make_mcq(
        rng,
        subskill="26_factor_market_definition_services",
        title="What Is Traded in the Factor Market?",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Businesses hire workers' skills/time, not ownership of people!",
            "tier_2": "Factor Markets trade the productive SERVICES of the 4 factors of production.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_factor_services_with_consumer_goods"],
        question_family_id="factor_market_def",
    )


def _b27_four_factors_and_remuneration_match(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(5, 25) * 1000
    pairs = [
        ("Natural Resources / Land", "Rent", f"leases workshop floor space in {s['area']} for {fmt_r(amt)}/month"),
        ("Labour", "Salaries and Wages", f"pays shop assistants {fmt_r(amt)}/month for working"),
        ("Capital", "Interest", f"pays {fmt_r(amt)}/year to the bank for borrowed machinery funds"),
        ("Entrepreneurship", "Profit", f"earns {fmt_r(amt)} net reward after taking risk to combine all inputs"),
    ]
    factor, remun, desc = rng.choice(pairs)
    prompt = f"{s['business']} {desc}. Identify the Factor of Production and its exact Factor Market remuneration:"
    ans = f"{factor} -> {remun}"
    opts = [f"{f} -> {r}" for f, r, _ in pairs]
    exp = f"In the Factor Market, {factor} earns {remun}."
    return _make_mcq(
        rng,
        subskill="27_four_factors_and_remuneration_match",
        title="Factor Market Remuneration Pairing",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Match the 4 factor payments: Rent, Salaries/Wages, Interest, Profit.",
            "tier_2": "Land->Rent | Labour->Salaries/Wages | Capital->Interest | Entrepreneurship->Profit.",
            "tier_3": ans,
        },
        misconception_tags=["swaps_interest_rent_and_profit"],
        question_family_id="factor_remuneration_mcq",
    )


def _b28_factor_market_remuneration_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    rows_pool = [
        ("Natural Resources / Land", "Rent", "Seller (Household/Landlord)"),
        ("Labour", "Salaries & Wages", "Seller (Workers/Households)"),
        ("Capital", "Interest", "Seller (Savers/Lenders)"),
        ("Entrepreneurship", "Profit", "Seller / Risk-taking Owner"),
    ]
    rng.shuffle(rows_pool)
    headers = ["Factor of Production", "Remuneration Paid by Businesses", "Household Market Role"]
    table_rows = [[(f, "given", False), (r, "required", True), (rl, "required", True)] for f, r, rl in rows_pool]
    cell_hints = {}
    for idx, (f, r, _) in enumerate(rows_pool):
        cell_hints[f"t0_r{idx}_c1"] = f"Name the exact economic payment for {f}."
        cell_hints[f"t0_r{idx}_c2"] = f"Are households Buyers or Sellers in the Factor Market?"
    prompt = f"Complete the Factor Market remuneration table below for productive inputs hired by {s['business']}."
    return _make_table(
        rng,
        subskill="28_factor_market_remuneration_table",
        title="Factor Market Remuneration Table",
        prompt=prompt,
        journal_type="factor_remuneration_table",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Remember Households OWN and SELL factors in the Factor Market!",
            "tier_2": "Land->Rent, Labour->Salaries & Wages, Capital->Interest, Entrepreneurship->Profit.",
            "tier_3": " | ".join(f"{f}: {r}" for f, r, _ in rows_pool),
        },
        misconception_tags=["confuses_factor_remuneration_labels"],
        question_family_id="factor_remun_table",
    )


def _b29_labour_market_vacancy_channels(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    salary = rng.randint(8, 22) * 1000
    prompt = (
        f"{s['business']} needs a qualified bookkeeper in {s['area']} offering {fmt_r(salary)}/month. "
        f"How does the Labour Market typically bring employers (demand) and job seekers (supply) together?"
    )
    ans = "Through vacancy advertisements (newspapers, online job portals), recruitment agencies, CV applications, and interviews"
    opts = [
        "Through vacancy advertisements (newspapers, online job portals), recruitment agencies, CV applications, and interviews",
        "Through buying shares on the Johannesburg Stock Exchange (JSE)",
        "Through handing out free bread at weekend flea markets",
        "Through commercial bank overdraft facilities",
    ]
    exp = f"The Labour Market operates through recruitment channels (online job boards, newspapers, agencies, interviews) to match job seekers with vacant positions ({fmt_r(salary)}/month)."
    return _make_mcq(
        rng,
        subskill="29_labour_market_vacancy_channels",
        title="How the Labour Market Matches Workers & Employers",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Think about how businesses announce open jobs and workers apply for them.",
            "tier_2": "Vacancy adverts, recruitment agencies, and interviews form Labour Market mechanisms.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_labour_market_with_financial_exchange"],
        question_family_id="labour_market_matching",
    )


def _b30_wages_vs_salaries_distinction(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    hr_rate = rng.randint(45, 95)
    sal_amt = rng.randint(14, 32) * 1000
    ask_wage = rng.choice([True, False])
    if ask_wage:
        prompt = (
            f"Casual warehouse packers at {s['business']} are paid {fmt_r(hr_rate)} per hour every Friday based on actual hours worked. "
            f"How is this type of labour remuneration classified?"
        )
        ans = "Wages — variable pay calculated hourly/daily/weekly, common for unskilled or semi-skilled work"
        exp = f"Hourly/weekly variable remuneration ({fmt_r(hr_rate)}/hr paid Fridays) is classified as Wages."
    else:
        prompt = (
            f"The qualified accountant at {s['business']} receives a fixed amount of {fmt_r(sal_amt)} on the 25th of every month regardless of exact hours. "
            f"How is this type of labour remuneration classified?"
        )
        ans = "Salaries — fixed monthly pay, common for skilled, managerial, or professional employees"
        exp = f"Fixed monthly remuneration ({fmt_r(sal_amt)}/month) for skilled/professional staff is a Salary."
    opts = [
        "Wages — variable pay calculated hourly/daily/weekly, common for unskilled or semi-skilled work",
        "Salaries — fixed monthly pay, common for skilled, managerial, or professional employees",
        "Dividends — profit share paid to external stock market shareholders",
        "Trade Credit — 30-day supplier credit terms",
    ]
    return _make_mcq(
        rng,
        subskill="30_wages_vs_salaries_distinction",
        title="Wages vs Salaries in the Labour Market",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Compare hourly/weekly variable pay against fixed monthly pay.",
            "tier_2": "Wages = hourly/weekly (often unskilled/semi-skilled); Salaries = fixed monthly (often skilled).",
            "tier_3": ans,
        },
        misconception_tags=["treats_wages_and_salaries_as_identical"],
        question_family_id="wages_vs_salaries",
    )


def _b31_wage_vs_overtime_calculation(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    worker = rng.choice(NAMES)
    rate = rng.choice([60, 80, 100, 120])
    norm_hrs = 40
    ot_hrs = rng.choice([4, 6, 8])
    norm_pay = norm_hrs * rate
    ot_rate = int(rate * 1.5)
    ot_pay = ot_hrs * ot_rate
    total = norm_pay + ot_pay
    ans = fmt_r(total)
    prompt = (
        f"In {s['area']}'s Labour Market, {worker} earns a normal wage of {fmt_r(rate)} per hour for a 40-hour week at {s['business']}. "
        f"This week {worker} works {ot_hrs} overtime hours paid at 1,5 times the normal hourly rate ({fmt_r(ot_rate)}/hr). "
        f"Calculate {worker}'s total gross weekly wage."
    )
    steps = [
        f"Normal pay = 40 hrs x {fmt_r(rate)} = {fmt_r(norm_pay)}.",
        f"Overtime pay = {ot_hrs} hrs x {fmt_r(ot_rate)} = {fmt_r(ot_pay)}.",
        f"Total weekly wage = {fmt_r(norm_pay)} + {fmt_r(ot_pay)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="31_wage_vs_overtime_calculation",
        title="Calculate Weekly Wage with Overtime",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{total}", str(total)],
        steps=steps,
        hints={
            "tier_1": "Split hours into 40 normal hours and overtime hours.",
            "tier_2": f"(40 x {fmt_r(rate)}) + ({ot_hrs} x {fmt_r(ot_rate)}).",
            "tier_3": f"Total gross weekly wage = {ans}.",
        },
        misconception_tags=["applies_normal_rate_to_overtime_hours"],
        question_family_id="wage_overtime_calc",
    )


def _b32_monthly_salary_vs_weekly_wage_compare(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    annual_sal = rng.choice([144, 168, 192, 216, 240]) * 1000
    monthly = int(annual_sal / 12)
    ans = fmt_r(monthly)
    prompt = (
        f"Comparing job offers in {s['area']}'s Labour Market, a technician is offered an annual Salary of {fmt_r(annual_sal)} per year by {s['business']}. "
        f"Calculate the technician's gross MONTHLY salary (assume 12 equal months)."
    )
    steps = [
        f"Monthly Salary = Annual Salary / 12.",
        f"{fmt_r(annual_sal)} / 12 = {ans} per month.",
    ]
    return _make_typed(
        rng,
        subskill="32_monthly_salary_vs_weekly_wage_compare",
        title="Convert Annual Salary to Monthly Pay",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{monthly}", str(monthly)],
        steps=steps,
        hints={
            "tier_1": "How many months are in a financial year?",
            "tier_2": f"Divide {fmt_r(annual_sal)} by 12.",
            "tier_3": f"Monthly salary = {ans}.",
        },
        misconception_tags=["divides_annual_salary_by_52_or_10"],
        question_family_id="annual_to_monthly_salary",
    )


def _b33_labour_market_unskilled_skilled_demand(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sal = rng.randint(32, 60) * 1000
    wage = rng.randint(4, 7) * 1000
    prompt = (
        f"In South Africa's Labour Market, a qualified electrical engineer may earn {fmt_r(sal)}/month while an unskilled labourer earns {fmt_r(wage)}/month. "
        f"Using supply and demand reasoning, explain TWO reasons why scarce skilled labour earns higher pay than abundant unskilled labour."
    )
    sample = (
        f"1. Scarce supply vs high demand: Few workers hold scarce engineering/technical qualifications while employers compete strongly to hire them, pushing pay up to {fmt_r(sal)}.\n"
        f"2. Training investment & productivity: Skilled roles require years of costly education/apprenticeships and generate high value output per worker, whereas large numbers of job seekers compete for unskilled positions ({fmt_r(wage)})."
    )
    pts = [
        "Explains scarcity of supply vs strong employer demand driving skilled salaries higher.",
        "Identifies training/education investment & higher marginal productivity vs high competition among unskilled job seekers.",
    ]
    return _make_rubric(
        rng,
        subskill="33_labour_market_unskilled_skilled_demand",
        title="Skilled vs Unskilled Pay Gap in SA Labour Market",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Apply supply and demand: rare skills vs many job seekers competing for the same entry job.",
            "tier_2": "Cover scarce supply vs high demand + years of training/productivity.",
            "tier_3": sample,
        },
        misconception_tags=["ignores_supply_and_demand_in_labour_pay"],
        question_family_id="labour_pay_gap_rubric",
        marks=2,
    )


def _b34_financial_markets_role_in_economy(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap_need = rng.randint(80, 250) * 1000
    prompt = (
        f"{s['business']} wants to raise {fmt_r(cap_need)} to buy automated machinery, while savers in {s['area']} have surplus money to invest. "
        f"Which economic arena connects surplus funds from savers/investors to deficit borrowers/businesses?"
    )
    ans = "The Financial Markets (comprising the Capital Market and Money Market)"
    opts = [
        "The Financial Markets (comprising the Capital Market and Money Market)",
        "Weekend Farmer & Craft Markets",
        "Municipal Traffic Licensing Departments",
        "Retail Grocery Chains",
    ]
    exp = f"Financial Markets bridge surplus savers and borrowing enterprises needing funds ({fmt_r(cap_need)}) via long-term Capital Markets and short-term Money Markets."
    return _make_mcq(
        rng,
        subskill="34_financial_markets_role_in_economy",
        title="Role of Financial Markets",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Which category of market specifically channels money/funding rather than groceries or crafts?",
            "tier_2": "Financial Markets include the Capital Market (long-term) and Money Market (short-term).",
            "tier_3": ans,
        },
        misconception_tags=["confuses_financial_markets_with_goods_markets"],
        question_family_id="financial_markets_role",
    )


def _b35_capital_market_long_term_funding(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(500, 1500) * 1000
    years = rng.choice([5, 10, 15])
    prompt = (
        f"A fast-growing firm linked to {s['business']} needs {fmt_r(amt)} for {years} years to construct a new factory building. "
        f"In which branch of Financial Markets are long-term funds (> 1 year) raised through shares and long-term loans?"
    )
    ans = "The Capital Market"
    opts = [
        "The Capital Market",
        "The Money Market",
        "The Flea Market",
        "The Retail Goods Market",
    ]
    exp = f"Long-term funding ({years} years, {fmt_r(amt)}) for buildings, infrastructure, and share capital takes place in the Capital Market."
    return _make_mcq(
        rng,
        subskill="35_capital_market_long_term_funding",
        title="Capital Market (Long-term Funding)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Check the time horizon: 5–15 years (> 1 year) vs < 1 year.",
            "tier_2": "Long-term (>1 year) = Capital Market; short-term (<1 year) = Money Market.",
            "tier_3": "The Capital Market.",
        },
        misconception_tags=["confuses_capital_market_and_money_market"],
        question_family_id="capital_market_def",
    )


def _b36_jse_and_public_company_shares(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cap_m = rng.randint(15, 85)
    prompt = (
        f"Suppose a successful South African retail group based near {s['area']} converts into a public company (Ltd) and lists on the **Johannesburg Stock Exchange (JSE)** to raise R{cap_m} million. "
        f"What does the JSE enable this company to issue and trade?"
    )
    ans = "Company Shares (equity ownership units) sold to public investors in the Capital Market"
    opts = [
        "Company Shares (equity ownership units) sold to public investors in the Capital Market",
        "30-day supplier invoices for vegetable crates",
        "Daily bank overdraft limits for spaza till floats",
        "Weekly hourly wage packets for casual workers",
    ]
    exp = f"The Johannesburg Stock Exchange (JSE) is South Africa's central Capital Market exchange where listed public companies issue and trade shares (R{cap_m} million here) to raise long-term capital."
    return _make_mcq(
        rng,
        subskill="36_jse_and_public_company_shares",
        title="The JSE & Public Company Shares",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Think about what investors buy when putting long-term money into JSE-listed companies.",
            "tier_2": "Public companies list on the JSE to raise Capital by issuing Shares.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_jse_issues_bank_overdrafts"],
        question_family_id="jse_shares",
    )


def _b37_shareholders_dividends_and_stakeholders(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    investor = rng.choice(NAMES)
    shares = rng.randint(200, 900)
    prompt = (
        f"{investor} from {s['area']} buys {shares} shares in a profitable JSE-listed company, becoming a **shareholder** (part-owner and stakeholder). "
        f"What is the profit payout distributed by the company to shareholders called?"
    )
    ans = "Dividends"
    opts = ["Dividends", "Bank Overdraft Fees", "Weekly Wages", "Trade Credit"]
    exp = f"Shareholders ({investor} with {shares} shares) are part-owners who receive a portion of after-tax company profits called Dividends."
    return _make_mcq(
        rng,
        subskill="37_shareholders_dividends_and_stakeholders",
        title="Shareholders & Dividends",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "It is NOT interest on a bank deposit — shareholders own part of the company's equity.",
            "tier_2": "A share of company profit paid to shareholders is called Dividends.",
            "tier_3": "Dividends.",
        },
        misconception_tags=["confuses_dividends_with_bank_interest_or_wages"],
        question_family_id="shareholders_dividends",
    )


def _b38_dividend_income_calculation(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    investor = rng.choice(NAMES)
    shares = rng.choice([250, 400, 500, 600, 800])
    div_per_share = rng.choice([4, 5, 6, 8])
    total_div = shares * div_per_share
    ans = fmt_r(total_div)
    svg = svg_market_card(
        "JSE DIVIDEND DISTRIBUTION STATEMENT",
        f"Shareholder: {investor} ({s['area']})",
        [
            ("Shares Held in Retail Group Ltd", f"{shares} shares"),
            ("Declared Annual Dividend per Share", fmt_r(div_per_share)),
            ("Total Dividend Payout Due", "R ???"),
        ],
    )
    prompt = (
        f"Inspect {investor}'s JSE Dividend Distribution Statement. "
        f"Calculate the Total Dividend Payout (`R ???`) earned across all {shares} shares."
    )
    steps = [
        f"Shares held = {shares}; Dividend per share = {fmt_r(div_per_share)}.",
        f"Total Dividend Payout = {shares} x {fmt_r(div_per_share)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="38_dividend_income_calculation",
        title="Calculate JSE Shareholder Dividend Payout",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{total_div}", str(total_div)],
        steps=steps,
        hints={
            "tier_1": "Multiply number of shares owned by the dividend declared per share.",
            "tier_2": f"{shares} x {fmt_r(div_per_share)}.",
            "tier_3": f"Total Dividend = {ans}.",
        },
        misconception_tags=["divides_shares_by_dividend_rate"],
        question_family_id="dividend_payout_calc",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b39_money_market_short_term_instruments(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(8, 25) * 1000
    prompt = (
        f"To cover a temporary 45-day cash gap before December holiday receipts arrive, {s['business']} arranges a {fmt_r(amt)} bank overdraft facility "
        f"and negotiates 30-day trade credit with {s['supplier']}. Which market provides these short-term (< 1 year) credit arrangements?"
    )
    ans = "The Money Market"
    opts = [
        "The Money Market",
        "The Capital Stock Market (JSE)",
        "The Craft & Flea Market",
        "The Tangible Consumer Goods Market",
    ]
    exp = f"Short-term financing instruments (bank overdrafts, 30/60-day trade credit, short-term bank loans under 12 months, {fmt_r(amt)}) operate in the Money Market."
    return _make_mcq(
        rng,
        subskill="39_money_market_short_term_instruments",
        title="Money Market (Short-term Financing)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice the short 30–45 day period (< 1 year).",
            "tier_2": "Short-term liquidity & credit (overdrafts, 30/60-day trade credit) = Money Market.",
            "tier_3": "The Money Market.",
        },
        misconception_tags=["places_overdraft_and_trade_credit_in_capital_market"],
        question_family_id="money_market_def",
    )


def _b40_capital_vs_money_market_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    headers = ["Financial Market Branch", "Time Horizon", "Key Instruments / Examples", "Typical Purpose"]
    table_rows = [
        [("Capital Market", "given", False), ("Long-term (> 1 year)", "required", True), ("JSE Shares, Mortgage Bonds, Long-term Loans", "required", True), ("Expansion, factories & long-term capital", "required", True)],
        [("Money Market", "given", False), ("Short-term (<= 1 year)", "required", True), ("Bank Overdrafts, 30/60-day Trade Credit, Short Loans", "required", True), ("Temporary working capital & cash flow gaps", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": "Long-term (> 1 year)",
        "t0_r0_c2": "JSE Shares, Mortgage Bonds, Long-term Loans",
        "t0_r0_c3": "Expansion, factories & long-term capital",
        "t0_r1_c1": "Short-term (<= 1 year)",
        "t0_r1_c2": "Bank Overdrafts, 30/60-day Trade Credit, Short Loans",
        "t0_r1_c3": "Temporary working capital & cash flow gaps",
    }
    prompt = f"Compare the Capital Market and Money Market in the table below for {s['business']}'s financing study."
    return _make_table(
        rng,
        subskill="40_capital_vs_money_market_table",
        title="Capital Market vs Money Market Comparison Table",
        prompt=prompt,
        journal_type="financial_market_comparison",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Separate long-term (> 1 year, JSE shares) from short-term (<= 1 year, overdrafts/trade credit).",
            "tier_2": "Capital Market builds long-term assets; Money Market manages temporary cash gaps.",
            "tier_3": "Capital Market = Long-term / JSE Shares / Expansion | Money Market = Short-term / Overdraft & Trade Credit / Working capital.",
        },
        misconception_tags=["swaps_capital_and_money_market_horizons"],
        question_family_id="capital_vs_money_table",
    )


def _b41_trade_credit_30_60_days_cashflow(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(15, 45) * 1000
    days = rng.choice([30, 60])
    prompt = (
        f"{sup} grants {s['business']} {days}-day **trade credit** worth {fmt_r(amt)} on wholesale stock deliveries. "
        f"Explain TWO cash-flow benefits of {days}-day trade credit AND ONE consequence if {s['business']} fails to pay {sup} on time."
    )
    sample = (
        f"Benefits: (1) Allows {s['business']} to sell the {fmt_r(amt)} stock to customers BEFORE paying {sup}, using sales cash to settle the invoice; (2) Usually interest-free within the agreed {days} days.\n"
        f"Late-payment consequence: {sup} may charge penalty interest, freeze credit supplies, or damage {s['business']}'s credit record."
    )
    pts = [
        f"Benefit 1: Stock can be sold for cash during the {days} days before paying {sup}.",
        f"Benefit 2: Acts as short-term interest-free Money Market finance during {days}-day terms.",
        "Consequence: Late payment triggers penalty interest, lost supplier credit, or damaged creditworthiness.",
    ]
    return _make_rubric(
        rng,
        subskill="41_trade_credit_30_60_days_cashflow",
        title="Trade Credit in the Money Market",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about selling inventory first vs paying on delivery, plus credit penalties.",
            "tier_2": "Cover cash-flow timing, zero initial interest, and late-payment penalties/credit freeze.",
            "tier_3": sample,
        },
        misconception_tags=["assumes_trade_credit_means_free_goods_forever"],
        question_family_id="trade_credit_rubric",
        marks=3,
    )


def _b42_bank_overdraft_definition_and_limit(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    limit = rng.randint(15, 40) * 1000
    prompt = (
        f"{bank} approves a {fmt_r(limit)} **Bank Overdraft** facility on {s['business']}'s business current account. "
        f"Which description accurately defines how a Bank Overdraft works?"
    )
    ans = f"A pre-approved short-term facility letting {s['business']} withdraw more money than is in the account (down to -{fmt_r(limit)}), repayable on short notice"
    opts = [
        f"A pre-approved short-term facility letting {s['business']} withdraw more money than is in the account (down to -{fmt_r(limit)}), repayable on short notice",
        f"Free grant money donated by {bank} that never needs to be repaid",
        f"A 20-year Mortgage Bond secured by factory real estate",
        f"Ownership shares issued on the Johannesburg Stock Exchange",
    ]
    exp = f"A Bank Overdraft allows {s['business']} to drop below R0 up to {fmt_r(limit)} to cover short-term cash dips, functioning as flexible Money Market credit."
    return _make_mcq(
        rng,
        subskill="42_bank_overdraft_definition_and_limit",
        title="Understanding a Bank Overdraft Facility",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Over-draft literally means drawing MORE than the positive balance currently in Bank.",
            "tier_2": "It is a short-term current liability up to an agreed bank limit.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_bank_overdraft_is_free_bank_cash"],
        question_family_id="bank_overdraft_def",
    )


def _b43_bank_overdraft_daily_interest_rule(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    limit = 30000
    drawn = rng.choice([7300, 14600, 21900])
    rate = rng.choice([10, 15, 20])
    days = rng.choice([10, 15, 20])
    interest = int(round(drawn * (rate / 100.0) * (days / 365.0)))
    ans = fmt_r(interest)
    prompt = (
        f"{s['business']} holds an approved {fmt_r(limit)} overdraft limit at {bank}, but only overdraws its account by {fmt_r(drawn)} for {days} days "
        f"at an annual interest rate of {rate}% (calculated daily ONLY on the actual overdrawn amount, using a 365-day year). "
        f"Calculate the overdraft interest charged."
    )
    steps = [
        f"Key Money Market rule: Interest applies ONLY to the actual overdrawn balance ({fmt_r(drawn)}), NOT the unused {fmt_r(limit)} limit.",
        f"Interest = {fmt_r(drawn)} x {rate}% x ({days} / 365) = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="43_bank_overdraft_daily_interest_rule",
        title="Calculate Daily Bank Overdraft Interest",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{interest}", str(interest)],
        steps=steps,
        hints={
            "tier_1": "Do NOT calculate interest on the R30 000 limit — use ONLY the actual overdrawn R balance!",
            "tier_2": f"Overdrawn balance x ({rate}/100) x ({days}/365).",
            "tier_3": f"Overdraft interest = {ans}.",
        },
        misconception_tags=["charges_interest_on_entire_overdraft_limit"],
        question_family_id="overdraft_interest_calc",
    )


def _b44_compare_overdraft_vs_long_term_loan(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    van_cost = rng.randint(140, 260) * 1000
    wages_dip = rng.randint(6, 15) * 1000
    prompt = (
        f"{s['business']} in {s['area']} faces two distinct needs: (A) covering a 10-day {fmt_r(wages_dip)} cash shortfall before customer EFTs clear, "
        f"and (B) buying a {fmt_r(van_cost)} delivery van for 5 years. Advise {s['entrepreneur']} on which financing choice fits each need: Bank Overdraft (Money Market) vs 5-Year Loan (Capital Market)."
    )
    sample = (
        f"Need (A) — 10-day {fmt_r(wages_dip)} dip: Use a Money Market **Bank Overdraft** because interest is charged daily only for the 10 days overdrawn and pays off automatically as customer EFTs arrive.\n"
        f"Need (B) — {fmt_r(van_cost)} 5-year van: Use a Capital Market **5-Year Term Loan** because matching long-term asset life with steady monthly repayments avoids sudden overdraft recall risk."
    )
    pts = [
        f"Matches 10-day {fmt_r(wages_dip)} gap -> Bank Overdraft (Money Market flexibility, daily interest only while overdrawn).",
        f"Matches {fmt_r(van_cost)} delivery van -> 5-Year Loan (Capital Market, predictable multi-year repayments).",
    ]
    return _make_rubric(
        rng,
        subskill="44_compare_overdraft_vs_long_term_loan",
        title="Overdraft vs 5-Year Loan Financing Decision",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Match short-term temporary dips to Money Market and 5-year assets to Capital Market.",
            "tier_2": "A = Overdraft (flexible short-term); B = Long-term Loan (matches 5-year vehicle life).",
            "tier_3": sample,
        },
        misconception_tags=["recommends_overdraft_to_buy_long_term_vehicles"],
        question_family_id="overdraft_vs_loan_rubric",
        marks=2,
    )


def _b45_supply_demand_shortage_price_signal(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    eq_p = rng.randint(25, 65)
    low_p = eq_p - rng.randint(8, 15)
    qd = rng.randint(120, 200)
    qs = rng.randint(45, 85)
    svg = svg_market_card(
        f"{s['area']} Produce Market — Price Signal",
        f"Vendor: {s['business']}",
        [
            ("Current Asking Price", fmt_r(low_p)),
            ("Quantity Demanded by Buyers", f"{qd} baskets"),
            ("Quantity Supplied by Sellers", f"{qs} baskets"),
            ("Market Condition", f"Shortage of {qd - qs} baskets"),
        ],
    )
    prompt = (
        f"Examine the Price Signal summary for {s['area']} Produce Market. At {fmt_r(low_p)}, buyers demand {qd} baskets "
        f"while sellers supply only {qs} baskets (a shortage of {qd - qs}). How will market price adjust toward equilibrium?"
    )
    ans = "Market price will RISE — reducing excess demand and encouraging sellers to supply more until quantity demanded equals quantity supplied"
    opts = [
        "Market price will RISE — reducing excess demand and encouraging sellers to supply more until quantity demanded equals quantity supplied",
        "Market price will FALL to R0 automatically",
        "Quantity supplied will shrink further to zero",
        "Buyers will become sellers inside the Factor Market",
    ]
    exp = f"A shortage of {qd - qs} baskets at {fmt_r(low_p)} pushes market price upward toward equilibrium ({fmt_r(eq_p)}) until demand equals supply."
    return _make_mcq(
        rng,
        subskill="45_supply_demand_shortage_price_signal",
        title="Market Shortage & Upward Price Signal",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "When more buyers want goods than exist on stalls (shortage), competition pushes price which way?",
            "tier_2": "Excess demand / shortage causes market price to RISE.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_shortage_lowers_market_price"],
        question_family_id="market_shortage_signal",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b46_supply_demand_surplus_clearance(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    crates_left = rng.randint(30, 85)
    prompt = (
        f"At the end of Saturday's farmer market in {s['area']}, warm weather causes unsold tomatoes (a surplus of {crates_left} crates) where supply far exceeds demand. "
        f"How does lowering the market price clear this surplus?"
    )
    ans = "Lower prices attract more household buyers and reduce excess supply until the surplus clears"
    opts = [
        "Lower prices attract more household buyers and reduce excess supply until the surplus clears",
        "Doubling prices forces households to purchase extra crates immediately",
        "High prices always increase household demand for perishable vegetables",
        "Raising wages in the Factor Market freezes tomato prices",
    ]
    exp = f"When supply exceeds demand ({crates_left} surplus crates), price drops entice buyers to purchase more so the excess stock clears instead of spoiling."
    return _make_mcq(
        rng,
        subskill="46_supply_demand_surplus_clearance",
        title="Market Surplus & Downward Price Adjustment",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Think of late-afternoon farmer market markdowns when stalls have extra unsold produce.",
            "tier_2": "A surplus puts downward pressure on price, increasing quantity demanded.",
            "tier_3": ans,
        },
        misconception_tags=["claims_raising_price_clears_unsold_surplus"],
        question_family_id="market_surplus_clearance",
    )


def _b47_circular_flow_factor_market_trace(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    spend = rng.randint(30, 75) * 1000
    fac_income = rng.randint(25, 65) * 1000
    svg = svg_circular_markets(s["area"], s["business"], fmt_r(spend), fmt_r(fac_income))
    prompt = (
        f"Examine the bottom Factor Market loop between {s['area']} Households and {s['business']}. "
        f"What does the {fmt_r(fac_income)} money flow leaving {s['business']} toward Households represent?"
    )
    ans = f"Factor remuneration ({fmt_r(fac_income)} in Wages, Salaries, Rent, Interest, and Profit) paid to households for supplying productive factors"
    opts = [
        f"Factor remuneration ({fmt_r(fac_income)} in Wages, Salaries, Rent, Interest, and Profit) paid to households for supplying productive factors",
        f"Consumer purchases of bread and electricity by households",
        f"Bank overdraft fees charged to wholesalers",
        f"Unpaid credit invoices owed to foreign importers",
    ]
    exp = f"In the bottom Factor Market loop, businesses pay {fmt_r(fac_income)} in factor remuneration (Wages, Rent, Interest, Profit) back to Households who own the factors of production."
    return _make_mcq(
        rng,
        subskill="47_circular_flow_factor_market_trace",
        title="Circular Flow: Factor Market Income Loop",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look at the bottom box labelled Factor Market.",
            "tier_2": "Businesses pay Rent, Wages, Interest, and Profit to Households in the Factor Market.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_factor_income_with_retail_sales_revenue"],
        question_family_id="circular_factor_flow",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b48_spot_financial_market_misconceptions(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(10, 45) * 1000
    statements = [
        (
            f"A student writes: 'The Johannesburg Stock Exchange (JSE) belongs to the Money Market because companies borrow 30-day overdrafts of {fmt_r(amt)} there.' Evaluate this claim.",
            "False — the JSE is a Capital Market trading long-term company shares, NOT 30-day bank overdrafts",
            "Bank overdrafts (30 days) belong to the Money Market at commercial banks; the JSE is South Africa's long-term Capital Market for shares.",
        ),
        (
            f"A student writes: 'If {s['business']} has a {fmt_r(amt)} overdraft limit at FNB, FNB charges interest on the full {fmt_r(amt)} every day even if the business uses only R2 000.' Evaluate this claim.",
            "False — overdraft interest is calculated daily ONLY on the actual overdrawn balance, not the unused limit",
            "Overdraft facilities charge daily interest strictly on the overdrawn amount used (R2 000), saving interest when unutilised.",
        ),
    ]
    prompt, ans, exp = rng.choice(statements)
    opts = [
        ans,
        "True — every commercial bank limit incurs full interest regardless of usage",
        "True — JSE shares mature every 30 days inside the Money Market",
        "False — overdrafts pay Dividends rather than Interest",
    ]
    return _make_mcq(
        rng,
        subskill="48_spot_financial_market_misconceptions",
        title="Financial Market Concept Audit (True/False)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Test the student's statement against JSE/Capital vs Money Market/Overdraft rules.",
            "tier_2": "JSE = Capital Market; Overdraft interest = daily on ACTUAL overdrawn balance only.",
            "tier_3": ans,
        },
        misconception_tags=["accepts_jse_or_overdraft_limit_misconception"],
        question_family_id="financial_market_audit",
    )


def _b49_case_study_sa_entrepreneur_markets(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    wages = rng.randint(4, 10) * 1000
    od = rng.randint(10, 25) * 1000
    prompt = (
        f"{s['entrepreneur']} operates a clothing enterprise in {s['area']}: (1) buys bulk cotton fabric rolls from a textile warehouse, "
        f"(2) sells finished school uniforms directly to township parents and online, (3) hires three seamstresses earning {fmt_r(wages)}/month, "
        f"and (4) uses a {fmt_r(od)} bank overdraft during back-to-school stock buildup. "
        f"Identify ALL FOUR specific markets involved in steps (1) to (4)."
    )
    sample = (
        "1. Bulk fabric from warehouse: **Wholesale Goods Market** (buying inputs in bulk).\n"
        "2. Uniforms direct to parents & online: **Retail Goods Market** (both physical and virtual).\n"
        f"3. Hiring seamstresses ({fmt_r(wages)}/month): **Labour Market** (within the Factor Market).\n"
        f"4. Bank overdraft ({fmt_r(od)}): **Money Market** (within Financial Markets)."
    )
    pts = [
        "1. Identifies Wholesale Market (bulk fabric supply).",
        "2. Identifies Retail Goods Market (physical & virtual consumer sales).",
        "3. Identifies Labour Market / Factor Market (hiring seamstresses).",
        f"4. Identifies Money Market / Financial Market (short-term {fmt_r(od)} overdraft).",
    ]
    return _make_rubric(
        rng,
        subskill="49_case_study_sa_entrepreneur_markets",
        title="Case Study: One Business Across Four Markets",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Label each numbered link separately: Wholesale, Retail, Labour (Factor), and Money Market.",
            "tier_2": "Bulk = Wholesale; Parents = Retail; Staff = Labour Market; Overdraft = Money Market.",
            "tier_3": sample,
        },
        misconception_tags=["misses_how_single_firm_spans_goods_factor_and_money_markets"],
        question_family_id="four_markets_case_study",
    )


def _b50_comprehensive_markets_capstone(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    shares_cap = rng.randint(2, 8) * 100000
    od_amt = rng.randint(15, 45) * 1000
    wage_tot = rng.randint(18, 42) * 1000
    svg = svg_market_card(
        f"{s['business']} — Market Ecosystem Summary",
        f"Location: {s['area']} | Owner: {s['entrepreneur']}",
        [
            ("JSE Share Capital Raised (Long-term)", fmt_r(shares_cap)),
            ("Bank Overdraft Used (Short-term)", fmt_r(od_amt)),
            ("Monthly Staff Salaries & Wages", fmt_r(wage_tot)),
            ("Goods & Services Sold", "Retail + Virtual Online"),
        ],
    )
    prompt = (
        f"Inspect the Market Ecosystem Summary for {s['business']}. "
        f"(a) Classify the JSE Share Capital ({fmt_r(shares_cap)}) and Bank Overdraft ({fmt_r(od_amt)}) into Capital Market vs Money Market, stating the reward paid in each. "
        f"(b) Explain why {s['business']} is a BUYER in the Factor Market ({fmt_r(wage_tot)}) yet a SELLER in the Goods & Services Market."
    )
    sample = (
        f"(a) JSE Share Capital ({fmt_r(shares_cap)}) operates in the **Capital Market** (long-term; shareholders earn **Dividends**). "
        f"Bank Overdraft ({fmt_r(od_amt)}) operates in the **Money Market** (short-term; bank charges daily **Interest** only on the overdrawn amount).\n"
        f"(b) In the Factor Market, {s['business']} BUYS labour services ({fmt_r(wage_tot)}) from households to produce; "
        "in the Goods & Services Market, it SELLS finished goods/services back to households physically and virtually."
    )
    pts = [
        f"Classifies JSE Share Capital ({fmt_r(shares_cap)}) as Capital Market with Dividends reward.",
        f"Classifies Bank Overdraft ({fmt_r(od_amt)}) as Money Market with daily Interest cost.",
        "Explains business buys productive inputs in Factor Market and sells outputs in Goods & Services Market.",
    ]
    return _make_rubric(
        rng,
        subskill="50_comprehensive_markets_capstone",
        title="Comprehensive Markets Ecosystem Capstone",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Link JSE vs Overdraft to Capital vs Money Market, then explain the firm's opposite roles in Factor vs Goods Markets.",
            "tier_2": "Capital Market->JSE/Dividends; Money Market->Overdraft/Interest; Firm buys Factor services and sells Consumer goods.",
            "tier_3": sample,
        },
        misconception_tags=["disconnects_financial_markets_from_factor_and_goods_markets"],
        question_family_id="markets_capstone",
        marks=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


ARCHETYPES_26_50 = {
    "26_factor_market_definition_services": _b26_factor_market_definition_services,
    "27_four_factors_and_remuneration_match": _b27_four_factors_and_remuneration_match,
    "28_factor_market_remuneration_table": _b28_factor_market_remuneration_table,
    "29_labour_market_vacancy_channels": _b29_labour_market_vacancy_channels,
    "30_wages_vs_salaries_distinction": _b30_wages_vs_salaries_distinction,
    "31_wage_vs_overtime_calculation": _b31_wage_vs_overtime_calculation,
    "32_monthly_salary_vs_weekly_wage_compare": _b32_monthly_salary_vs_weekly_wage_compare,
    "33_labour_market_unskilled_skilled_demand": _b33_labour_market_unskilled_skilled_demand,
    "34_financial_markets_role_in_economy": _b34_financial_markets_role_in_economy,
    "35_capital_market_long_term_funding": _b35_capital_market_long_term_funding,
    "36_jse_and_public_company_shares": _b36_jse_and_public_company_shares,
    "37_shareholders_dividends_and_stakeholders": _b37_shareholders_dividends_and_stakeholders,
    "38_dividend_income_calculation": _b38_dividend_income_calculation,
    "39_money_market_short_term_instruments": _b39_money_market_short_term_instruments,
    "40_capital_vs_money_market_table": _b40_capital_vs_money_market_table,
    "41_trade_credit_30_60_days_cashflow": _b41_trade_credit_30_60_days_cashflow,
    "42_bank_overdraft_definition_and_limit": _b42_bank_overdraft_definition_and_limit,
    "43_bank_overdraft_daily_interest_rule": _b43_bank_overdraft_daily_interest_rule,
    "44_compare_overdraft_vs_long_term_loan": _b44_compare_overdraft_vs_long_term_loan,
    "45_supply_demand_shortage_price_signal": _b45_supply_demand_shortage_price_signal,
    "46_supply_demand_surplus_clearance": _b46_supply_demand_surplus_clearance,
    "47_circular_flow_factor_market_trace": _b47_circular_flow_factor_market_trace,
    "48_spot_financial_market_misconceptions": _b48_spot_financial_market_misconceptions,
    "49_case_study_sa_entrepreneur_markets": _b49_case_study_sa_entrepreneur_markets,
    "50_comprehensive_markets_capstone": _b50_comprehensive_markets_capstone,
}
