"""Subskills 47 to 52: Inflation rates, multi-year compounding, disinflation vs deflation, personal inflation baskets, and salary negotiations."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_pct,
)


def generate_47_annual_commodity_inflation_rate(r: random.Random) -> Dict[str, Any]:
    """Calculate the percentage inflation rate from a single commodity price change: (Change / Old) * 100%."""
    old_price = r.choice([12.50, 14.00, 16.50, 18.00])
    hike = r.choice([1.25, 1.50, 1.80, 2.20])
    new_price = old_price + hike
    inflation_rate = (hike / old_price) * 100.0

    correct_ans = f"{_fmt(inflation_rate, 2)}%"
    custom_options = [
        f"{_fmt(inflation_rate, 2)}%",
        f"{_fmt(inflation_rate * 1.25, 2)}%",
        f"{_fmt(inflation_rate * 0.75, 2)}%",
        f"{_fmt(hike, 2)}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"The price of a standard 700 g loaf of brown bread in South Africa increased from {_fmt_curr(old_price)} "
        f"in January of Year 1 to {_fmt_curr(new_price)} in January of Year 2.\n\n"
        f"Calculate the annual percentage inflation rate for brown bread over this period, rounded to two decimal places."
    )
    explanation = (
        f"Step 1: Calculate price increase = {_fmt_curr(new_price)} - {_fmt_curr(old_price)} = {_fmt_curr(hike)} [M].\n"
        f"Step 2: Formula: Inflation Rate = (Change in Price ÷ Original Price) × 100% [M].\n"
        f"Step 3: Substitute: ({_fmt_curr(hike)} ÷ {_fmt_curr(old_price)}) × 100% = {_fmt(inflation_rate, 2)}% [A]."
    )
    return _build_question_payload(
        subskill_id="47_annual_commodity_inflation_rate",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the old price from the new price, divide by the old price, and multiply by 100%.",
        tier_2=f"Price increase is {_fmt_curr(hike)}. Divide by {_fmt_curr(old_price)}.",
        tier_3=f"The annual inflation rate is {_fmt(inflation_rate, 2)}%.",
        r=r,
    )


def generate_48_multi_year_compounded_inflation(r: random.Random) -> Dict[str, Any]:
    """Project future prices across multiple successive annual inflation rates."""
    base_price = r.choice([4500.00, 5000.00, 6000.00])
    r1 = 7.6  # 2007
    r2 = 9.4  # 2008
    r3 = 6.0  # 2009
    r4 = 3.4  # 2010

    p1 = base_price * (1.0 + r1 / 100.0)
    p2 = p1 * (1.0 + r2 / 100.0)
    p3 = p2 * (1.0 + r3 / 100.0)
    p4 = p3 * (1.0 + r4 / 100.0)

    correct_ans = _fmt_curr(p4)
    # Simple addition distractor
    simple_p = base_price * (1.0 + (r1 + r2 + r3 + r4) / 100.0)
    custom_options = [
        _fmt_curr(p4),
        _fmt_curr(simple_p),
        _fmt_curr(p4 * 1.15),
        _fmt_curr(p4 * 0.88),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A desktop computer cost {_fmt_curr(base_price)} at the end of 2006. Over the next four years, national "
        f"CPI inflation was recorded as follows:\n"
        f"• 2007: {_fmt_pct(r1)}\n"
        f"• 2008: {_fmt_pct(r2)}\n"
        f"• 2009: {_fmt_pct(r3)}\n"
        f"• 2010: {_fmt_pct(r4)}\n\n"
        f"Assuming the computer price increased exactly in line with inflation each year, calculate its price at the end of 2010."
    )
    explanation = (
        f"Step 1: End of 2007: {_fmt_curr(base_price)} × (1 + 0,076) = {_fmt_curr(p1)} [M].\n"
        f"Step 2: End of 2008: {_fmt_curr(p1)} × (1 + 0,094) = {_fmt_curr(p2)}; End of 2009: {_fmt_curr(p2)} × (1 + 0,06) = {_fmt_curr(p3)} [M].\n"
        f"Step 3: End of 2010: {_fmt_curr(p3)} × (1 + 0,034) = {_fmt_curr(p4)} [A]."
    )
    return _build_question_payload(
        subskill_id="48_multi_year_compounded_inflation",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Apply each annual inflation percentage successively to the new price, year by year.",
        tier_2=f"Multiply {_fmt_curr(base_price)} by 1,076, then 1,094, then 1,06, then 1,034.",
        tier_3=f"The projected price at the end of 2010 is {_fmt_curr(p4)}.",
        r=r,
    )


def generate_49_disinflation_vs_deflation(r: random.Random) -> Dict[str, Any]:
    """Explain that a decreasing positive inflation rate (disinflation) still means prices are rising."""
    rate_2022 = r.choice([7.8, 8.2, 8.5, 8.9])
    rate_2023 = r.choice([4.8, 5.2, 5.5, 5.8])
    d_spec_49 = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": "National CPI Inflation Rate (Stats SA)",
        "x_label": "Year",
        "y_label": "CPI Inflation Rate (%)",
        "series": [
            {"name": "CPI Inflation", "points": [[2022, rate_2022], [2023, rate_2023]]}
        ],
    }
    correct_ans = "Disinflation: Prices are still increasing, but at a slower pace; prices only decrease if inflation is negative (deflation)"

    custom_options = [
        correct_ans,
        "Deflation: When the inflation rate drops from 8% to 4%, retail prices decrease by 4%",
        "Price freeze: Goods become completely free of price changes when the graph slopes downward",
        "Economic recession: Decreasing inflation rates always mean goods are sold at half price",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the CPI inflation graph showing the national headline inflation rate dropping from {_fmt(rate_2022, 1)}% in 2022 to {_fmt(rate_2023, 1)}% in 2023.\n"
        f"A learner concludes: 'Because the graph is decreasing, food and fuel became cheaper in 2023.'\n\n"
        f"Critique this learner's statement from a Mathematical Literacy perspective."
    )
    explanation = (
        f"Step 1: Inflation measures the rate at which prices rise [M].\n"
        f"Step 2: A positive rate of 5,2% means prices are still 5,2% higher than the previous year (disinflation) [M].\n"
        f"Step 3: Prices only become cheaper if the inflation rate drops below zero (negative inflation or deflation) [A]."
    )
    return _build_question_payload(
        subskill_id="49_disinflation_vs_deflation",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Distinguish between the rate of price increase and the actual price level.",
        tier_2="As long as the inflation percentage is positive, prices continue to climb.",
        tier_3="A declining positive rate is disinflation, not deflation.",
        r=r,
        diagram_spec=d_spec_49,
    )


def generate_50_household_personal_inflation_rate(r: random.Random) -> Dict[str, Any]:
    """Calculate a specific household's weighted personal inflation rate across their monthly expenditure basket."""
    old_expenses = 11872.30
    new_expenses = 13149.30
    increase_rands = new_expenses - old_expenses
    personal_inflation = (increase_rands / old_expenses) * 100.0

    correct_ans = f"{_fmt(personal_inflation, 2)}% (Household expenses rose by {_fmt_curr(increase_rands)})"
    custom_options = [
        correct_ans,
        f"{_fmt(personal_inflation * 1.25, 2)}% (Household expenses rose by {_fmt_curr(increase_rands * 1.25)})",
        f"{_fmt(personal_inflation * 0.75, 2)}% (Household expenses rose by {_fmt_curr(increase_rands * 0.75)})",
        f"6,00% (Matches the national headline CPI target band)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A family in Durban audits their monthly living expenditure basket (housing, transport, food, medical aid, utilities):\n"
        f"• Total monthly expenses in Year 1: {_fmt_curr(old_expenses)}\n"
        f"• Total monthly expenses in Year 2: {_fmt_curr(new_expenses)}\n\n"
        f"Calculate this family's actual personal inflation rate for the year, and compare it to the national CPI rate of 6,0%."
    )
    explanation = (
        f"Step 1: Calculate total monetary increase: {_fmt_curr(new_expenses)} - {_fmt_curr(old_expenses)} = {_fmt_curr(increase_rands)} [M].\n"
        f"Step 2: Personal Inflation = ({_fmt_curr(increase_rands)} ÷ {_fmt_curr(old_expenses)}) × 100% [M].\n"
        f"Step 3: Personal Inflation Rate = {_fmt(personal_inflation, 2)}%, which significantly exceeds national CPI [A]."
    )
    return _build_question_payload(
        subskill_id="50_household_personal_inflation_rate",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the increase in total family expenses and divide by the old total.",
        tier_2=f"Increase = {_fmt_curr(increase_rands)}. Divide by {_fmt_curr(old_expenses)} and multiply by 100%.",
        tier_3=f"The personal inflation rate is {_fmt(personal_inflation, 2)}%.",
        r=r,
    )


def generate_51_salary_negotiation_real_wage_growth(r: random.Random) -> Dict[str, Any]:
    """Evaluate whether an annual salary increase results in real wage growth, stagnation, or a deficit."""
    salary = 16750.00
    salary_increase_pct = 7.5
    salary_hike_rands = (salary_increase_pct / 100.0) * salary
    expense_hike_rands = 1277.00
    net_monthly_impact = salary_hike_rands - expense_hike_rands

    correct_ans = f"Financial position remained roughly equal (Salary hike: {_fmt_curr(salary_hike_rands)} vs Cost increase: {_fmt_curr(expense_hike_rands)}; small deficit of {_fmt_curr(abs(net_monthly_impact))})"
    custom_options = [
        correct_ans,
        f"Massive financial gain of {_fmt_curr(salary_hike_rands)} because living expenses are completely ignored",
        f"Severe deficit of {_fmt_curr(expense_hike_rands)} because 7,5% increase is below 10%",
        f"Worker doubled their purchasing power because 7,5% exceeds national 6,0% inflation",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An employee earns {_fmt_curr(salary)} per month and receives an annual salary increase of {_fmt_pct(salary_increase_pct)}.\n"
        f"During the same year, their essential monthly household living expenses increased by {_fmt_curr(expense_hike_rands)}.\n\n"
        f"Determine the monetary value of the salary increase and evaluate whether the worker's real financial position "
        f"improved, remained unchanged, or worsened."
    )
    explanation = (
        f"Step 1: Calculate salary increase: {_fmt_pct(salary_increase_pct)} × {_fmt_curr(salary)} = {_fmt_curr(salary_hike_rands)} [M].\n"
        f"Step 2: Compare salary increase to expense increase: {_fmt_curr(salary_hike_rands)} - {_fmt_curr(expense_hike_rands)} = {_fmt_curr(net_monthly_impact)} [M].\n"
        f"Step 3: The difference is negligible ({_fmt_curr(abs(net_monthly_impact))}), so financial position remained roughly constant [A]."
    )
    return _build_question_payload(
        subskill_id="51_salary_negotiation_real_wage_growth",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the Rand value of the salary increase and compare it to the increase in living expenses.",
        tier_2=f"Salary increase = {_fmt_curr(salary_hike_rands)}. Expenses increased by {_fmt_curr(expense_hike_rands)}.",
        tier_3=f"Because the two amounts are almost equal ({_fmt_curr(abs(net_monthly_impact))} difference), their financial position stayed about the same.",
        r=r,
    )


def generate_52_required_salary_increase_percentage(r: random.Random) -> Dict[str, Any]:
    """Calculate the exact percentage salary increase required to offset rising expenses."""
    salary = r.choice([15000.00, 16000.00, 18000.00, 20000.00])
    expense_increase = r.choice([1200.00, 1277.00, 1400.00, 1500.00])
    required_pct = (expense_increase / salary) * 100.0

    correct_ans = f"{_fmt(required_pct, 2)}%"
    custom_options = [
        f"{_fmt(required_pct, 2)}%",
        f"{_fmt(required_pct * 1.25, 2)}%",
        f"{_fmt(required_pct * 0.75, 2)}%",
        f"10,76%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An employee currently earns a monthly salary of {_fmt_curr(salary)}.\n"
        f"Over the past year, their essential monthly household living expenses rose by {_fmt_curr(expense_increase)}.\n\n"
        f"Calculate the exact percentage salary increase the employee must negotiate with their employer to cover "
        f"these increased living expenses exactly, leaving their discretionary savings unchanged."
    )
    explanation = (
        f"Step 1: Formula: Required Increase % = (Expense Increase in Rands ÷ Current Salary) × 100% [M].\n"
        f"Step 2: Substitute: ({_fmt_curr(expense_increase)} ÷ {_fmt_curr(salary)}) × 100% [M].\n"
        f"Step 3: Required Salary Increase = {_fmt(required_pct, 2)}% [A]."
    )
    return _build_question_payload(
        subskill_id="52_required_salary_increase_percentage",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the required extra Rand amount by the employee's current salary and multiply by 100%.",
        tier_2=f"Calculate ({_fmt_curr(expense_increase)} ÷ {_fmt_curr(salary)}) × 100%.",
        tier_3=f"The required salary increase is {_fmt(required_pct, 2)}%.",
        r=r,
    )
