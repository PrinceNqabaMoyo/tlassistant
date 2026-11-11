"""Cluster 3: Personal & Household Monthly Budgets (10 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_budg_hh_monthly_tabular_total_income(r: random.Random) -> Dict[str, Any]:
    name1 = r.choice(SA_NAMES)
    name2 = r.choice([n for n in SA_NAMES if n != name1])
    sal1 = round(r.choice([14500.00, 16200.00, 18000.00, 19500.00]), 2)
    sal2 = round(r.choice([11200.00, 12800.00, 13500.00, 15000.00]), 2)
    csg = 530.00 * r.choice([1, 2])  # Child support grant R530 per child
    flatlet = round(r.choice([2500.00, 2800.00, 3200.00]), 2)
    total_inc = round(sal1 + sal2 + csg + flatlet, 2)
    ans_str = _fmt_curr(total_inc)

    table_md = (
        f"| Income Stream | Earner / Source | Monthly Amount |\n"
        f"| :--- | :--- | :--- |\n"
        f"| Basic Net Salary | {name1} | {_fmt_curr(sal1)} |\n"
        f"| Basic Net Salary | {name2} | {_fmt_curr(sal2)} |\n"
        f"| SASSA Child Support Grant | Department of Social Development | {_fmt_curr(csg)} |\n"
        f"| Garden Cottage Rental | Tenant | {_fmt_curr(flatlet)} |\n"
    )

    prompt = (
        f"The table below displays the planned monthly household income streams for the family of {name1} and {name2}:\n\n"
        f"{table_md}\n\n"
        f"Calculate the **Total Monthly Household Income**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Total monthly household income is the sum of all individual net salaries, government social grants, and investment/rental inflows:\n"
        f"  $$\\text{{Total Income}} = \\text{{Salary 1}} + \\text{{Salary 2}} + \\text{{Social Grants}} + \\text{{Rental Income}}$$\n\n"
        f"**Step 2: Method Setup & Summation**\n"
        f"• $\\text{{Total Income}} = \\text{{{_fmt_curr(sal1)}}} + \\text{{{_fmt_curr(sal2)}}} + \\text{{{_fmt_curr(csg)}}} + \\text{{{_fmt_curr(flatlet)}}} = \\text{{{_fmt_curr(total_inc)}}}$.\n"
        f"✓ **[1 Mark: Method – correctly identifying all 4 income lines and summing them]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total household income in Rands]**"
    )
    return _make_q(
        subskill="budg_hh_monthly_tabular_total_income",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – sum of all 4 tabular income entries", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Add together all the figures in the 'Monthly Amount' column.",
            "tier_2": f"{_fmt_curr(sal1)} + {_fmt_curr(sal2)} + {_fmt_curr(csg)} + {_fmt_curr(flatlet)}.",
            "tier_3": f"Total income = {_fmt_curr(total_inc)}."
        },
        r=r
    )

def _gen_budg_hh_monthly_tabular_total_expenses(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    rent = round(r.choice([4800.00, 5200.00, 5600.00]), 2)
    groceries = round(r.choice([3200.00, 3600.00, 4100.00]), 2)
    transport = round(r.choice([1600.00, 1800.00, 2100.00]), 2)
    electricity_water = round(r.choice([950.00, 1100.00, 1250.00]), 2)
    cell_data = round(r.choice([450.00, 550.00, 650.00]), 2)
    funeral_policy = round(r.choice([280.00, 320.00, 380.00]), 2)
    total_exp = round(rent + groceries + transport + electricity_water + cell_data + funeral_policy, 2)
    ans_str = _fmt_curr(total_exp)

    table_md = (
        f"| Expenditure Category | Expense Description | Budgeted Amount |\n"
        f"| :--- | :--- | :--- |\n"
        f"| Housing | Accommodation rent | {_fmt_curr(rent)} |\n"
        f"| Food | Groceries & fresh food | {_fmt_curr(groceries)} |\n"
        f"| Transport | Minibus taxi & bus fares | {_fmt_curr(transport)} |\n"
        f"| Utilities | Water & prepaid electricity | {_fmt_curr(electricity_water)} |\n"
        f"| Communication | Cellphone contracts & data | {_fmt_curr(cell_data)} |\n"
        f"| Insurance | Family funeral policy | {_fmt_curr(funeral_policy)} |\n"
    )

    prompt = (
        f"The table below details {name}'s budgeted monthly living expenses:\n\n"
        f"{table_md}\n\n"
        f"Calculate {name}'s **Total Monthly Budgeted Expenditure**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Total monthly budgeted expenditure represents the grand total of all planned living expenses:\n"
        f"  $$\\text{{Total Expenditure}} = \\sum \\text{{All Budgeted Line Items}}$$\n\n"
        f"**Step 2: Method Setup & Summation**\n"
        f"• $\\text{{Total Expenditure}} = \\text{{{_fmt_curr(rent)}}} + \\text{{{_fmt_curr(groceries)}}} + \\text{{{_fmt_curr(transport)}}} + \\text{{{_fmt_curr(electricity_water)}}} + \\text{{{_fmt_curr(cell_data)}}} + \\text{{{_fmt_curr(funeral_policy)}}} = \\text{{{_fmt_curr(total_exp)}}}$.\n"
        f"✓ **[1 Mark: Method – correctly summing all 6 budgeted expense categories]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total expenditure in Rands]**"
    )
    return _make_q(
        subskill="budg_hh_monthly_tabular_total_expenses",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – summing all 6 expense lines", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Add up every budgeted item in the rightmost column.",
            "tier_2": f"{_fmt_curr(rent)} + {_fmt_curr(groceries)} + {_fmt_curr(transport)} + {_fmt_curr(electricity_water)} + {_fmt_curr(cell_data)} + {_fmt_curr(funeral_policy)}.",
            "tier_3": f"Total expenditure = {_fmt_curr(total_exp)}."
        },
        r=r
    )

def _gen_budg_hh_monthly_surplus_deficit_verdict(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_income = round(r.choice([14000.00, 16500.00, 18000.00, 21000.00]), 2)
    # Determine whether surplus or deficit
    is_surplus = r.choice([True, False])
    delta = round(r.choice([850.00, 1200.00, 1450.00, 1900.00, 2300.00]), 2)
    if is_surplus:
        total_exp = round(total_income - delta, 2)
        verdict = "Surplus"
        ans_str = f"Surplus of {_fmt_curr(delta)}"
    else:
        total_exp = round(total_income + delta, 2)
        verdict = "Deficit"
        ans_str = f"Deficit of {_fmt_curr(delta)}"

    prompt = (
        f"{name}'s household budget report shows:\n\n"
        f"• Total Monthly Net Income: **{_fmt_curr(total_income)}**\n"
        f"• Total Monthly Expenditure: **{_fmt_curr(total_exp)}**\n\n"
        f"1. Calculate the difference between total monthly income and total monthly expenditure.\n"
        f"2. Indicate whether the budget is running at a **Surplus** or a **Deficit**, including the exact monetary amount."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Net Balance is calculated as:\n"
        f"  $$\\text{{Net Balance}} = \\text{{Total Income}} - \\text{{Total Expenditure}}$$\n"
        f"• If $\\text{{Income}} > \\text{{Expenditure}}$, there is money left over, representing a **Surplus**.\n"
        f"• If $\\text{{Expenditure}} > \\text{{Income}}$, costs exceed available funds, representing a **Deficit**.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Balance}} = \\text{{{_fmt_curr(total_income)}}} - \\text{{{_fmt_curr(total_exp)}}} = "
        f"{'+' if is_surplus else '-'}\\text{{{_fmt_curr(delta)}}}$.\n"
        f"• Since {'income exceeds expenditure' if is_surplus else 'expenditure exceeds income'}, this represents a **{verdict}** of **{_fmt_curr(delta)}**.\n"
        f"✓ **[1 Mark: Method – subtracting total expenditure from total income]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct financial verdict (Surplus/Deficit) and Rand value]**"
    )
    custom_options = [
        f"Surplus of {_fmt_curr(delta)}",
        f"Deficit of {_fmt_curr(delta)}",
        f"Surplus of {_fmt_curr(round(delta * 1.1, 2))}",
        f"Deficit of {_fmt_curr(round(delta * 1.1, 2))}"
    ]
    return _make_q(
        subskill="budg_hh_monthly_surplus_deficit_verdict",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – income - expenditure", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Subtract total expenses ({_fmt_curr(total_exp)}) from total income ({_fmt_curr(total_income)}).",
            "tier_2": f"If positive, it is a Surplus. If negative, it is a Deficit.",
            "tier_3": f"Final outcome: {ans_str}."
        },
        options=custom_options,
        r=r
    )

def _gen_budg_hh_balanced_budget_savings_allocation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_income = round(r.choice([15000.00, 17500.00, 19200.00, 22000.00]), 2)
    rent = round(r.choice([4500.00, 5200.00, 5800.00]), 2)
    groceries = round(r.choice([3200.00, 3600.00, 4000.00]), 2)
    transport = round(r.choice([1800.00, 2100.00]), 2)
    utilities = round(r.choice([950.00, 1100.00]), 2)
    insurance = round(r.choice([550.00, 650.00]), 2)
    total_living_exp = round(rent + groceries + transport + utilities + insurance, 2)
    savings_allocation = round(total_income - total_living_exp, 2)
    ans_str = _fmt_curr(savings_allocation)

    prompt = (
        f"{name} practices balanced budgeting, ensuring that every Rand earned is allocated such that:\n\n"
        f"$$\\text{{Total Income}} = \\text{{Total Living Expenses}} + \\text{{Emergency Savings}}$$\n\n"
        f"{name}'s monthly net income is **{_fmt_curr(total_income)}**.\n"
        f"The itemised living expenses for the month are:\n"
        f"• Housing Rent: **{_fmt_curr(rent)}**\n"
        f"• Food & Groceries: **{_fmt_curr(groceries)}**\n"
        f"• Commuter Transport: **{_fmt_curr(transport)}**\n"
        f"• Water & Electricity: **{_fmt_curr(utilities)}**\n"
        f"• Insurance Policies: **{_fmt_curr(insurance)}**\n\n"
        f"Calculate the **remaining amount allocated to Emergency Savings** to create a perfectly balanced budget."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• In a balanced budget, total income equals total expenses plus savings:\n"
        f"  $$\\text{{Emergency Savings}} = \\text{{Total Income}} - \\sum \\text{{Living Expenses}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Total Living Expenses}} = \\text{{{_fmt_curr(rent)}}} + \\text{{{_fmt_curr(groceries)}}} + \\text{{{_fmt_curr(transport)}}} + \\text{{{_fmt_curr(utilities)}}} + \\text{{{_fmt_curr(insurance)}}} = \\text{{{_fmt_curr(total_living_exp)}}}$.\n"
        f"• $\\text{{Savings Allocation}} = \\text{{{_fmt_curr(total_income)}}} - \\text{{{_fmt_curr(total_living_exp)}}} = \\text{{{_fmt_curr(savings_allocation)}}}$.\n"
        f"✓ **[1 Mark: Method – summing living expenses and subtracting from total net income]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct savings allocation in Rands]**"
    )
    return _make_q(
        subskill="budg_hh_balanced_budget_savings_allocation",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – income - total living expenses", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Sum all 5 living expenses ({_fmt_curr(total_living_exp)}) and subtract from net income ({_fmt_curr(total_income)}).",
            "tier_2": f"{_fmt_curr(total_income)} - {_fmt_curr(total_living_exp)}.",
            "tier_3": f"Emergency savings allocation = {_fmt_curr(savings_allocation)}."
        },
        r=r
    )

def _gen_budg_hh_expense_fraction_of_income(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    income = round(r.choice([16000.00, 18000.00, 20000.00, 22500.00]), 2)
    # Rent benchmark typically ~25% to 35%
    rent_pct = r.choice([25.0, 28.0, 30.0, 32.5, 35.0])
    rent = round((rent_pct / 100.0) * income, 2)
    calc_pct = round((rent / income) * 100, 1)
    ans_str = f"{_fmt(calc_pct)}%"

    prompt = (
        f"Financial planners advise that housing costs should ideally not exceed 30% of a household's net income.\n\n"
        f"{name}'s net monthly income is **{_fmt_curr(income)}**, and {name} pays **{_fmt_curr(rent)}** per month for apartment rent.\n\n"
        f"Calculate what **percentage of net monthly income** is spent on rent, rounded to 1 decimal place."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• The percentage of income allocated to a specific expense is given by:\n"
        f"  $$\\text{{Percentage}} = \\left( \\frac{{\\text{{Expense Amount}}}}{{\\text{{Net Income}}}} \\right) \\times 100\\%$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Percentage}} = \\left( \\frac{{{_fmt(rent)}}}{{{_fmt(income)}}} \\right) \\times 100\\% = {calc_pct:.4f}\\% \\approx {_fmt(calc_pct)}\\%$.\n"
        f"✓ **[1 Mark: Method – dividing rent by net income and multiplying by 100]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct percentage rounded to 1 decimal place]**"
    )
    return _make_q(
        subskill="budg_hh_expense_fraction_of_income",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (rent ÷ income) × 100", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide the rent ({_fmt_curr(rent)}) by total income ({_fmt_curr(income)}) and multiply by 100.",
            "tier_2": f"({rent} ÷ {income}) × 100 = {calc_pct}%.",
            "tier_3": f"Rent percentage = {ans_str}."
        },
        r=r
    )

def _gen_budg_hh_annual_inflation_adjustment(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    cpi_rate = r.choice([5.5, 6.0, 6.5, 7.0, 7.5])  # percentage
    current_food = round(r.choice([3200.00, 3600.00, 4000.00, 4400.00]), 2)
    inflation_increase = round(current_food * (cpi_rate / 100.0), 2)
    new_food_budget = round(current_food + inflation_increase, 2)
    ans_str = _fmt_curr(new_food_budget)

    prompt = (
        f"{name}'s household currently spends **{_fmt_curr(current_food)} per month** on food groceries.\n\n"
        f"According to Statistics South Africa (Stats SA), annual food price inflation (CPI) is expected to increase grocery costs by **{_fmt(cpi_rate)}%** next year.\n\n"
        f"Calculate the **new monthly grocery budget** required to maintain the exact same standard of living after the inflation increase."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Inflation increases the cost of living over time:\n"
        f"  $$\\text{{Inflation Increase}} = \\text{{Current Cost}} \\times \\frac{{\\text{{Inflation Rate}}}}{{100}}$$\n"
        f"  $$\\text{{New Budget}} = \\text{{Current Cost}} + \\text{{Inflation Increase}}$$\n"
        f"• Alternatively, multiply by $(1 + \\frac{{\\text{{rate}}}}{{100}})$.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Increase}} = \\text{{{_fmt_curr(current_food)}}} \\times \\frac{{{_fmt(cpi_rate)}}}{{100}} = \\text{{{_fmt_curr(inflation_increase)}}}$.\n"
        f"• $\\text{{New Monthly Budget}} = \\text{{{_fmt_curr(current_food)}}} + \\text{{{_fmt_curr(inflation_increase)}}} = \\text{{{_fmt_curr(new_food_budget)}}}$.\n"
        f"✓ **[1 Mark: Method – calculating inflation percentage and adding to original cost]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct inflation-adjusted budget in Rands]**"
    )
    return _make_q(
        subskill="budg_hh_annual_inflation_adjustment",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – original × (1 + inflation_rate ÷ 100)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Calculate {_fmt(cpi_rate)}% of {_fmt_curr(current_food)}, then add it to {_fmt_curr(current_food)}.",
            "tier_2": f"Increase = {_fmt_curr(current_food)} × 0,{str(cpi_rate).replace('.', '')[:2]} = {_fmt_curr(inflation_increase)}. New budget = {_fmt_curr(new_food_budget)}.",
            "tier_3": f"New grocery budget = {_fmt_curr(new_food_budget)}."
        },
        r=r
    )

def _gen_budg_hh_income_drop_rebalancing(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    original_income = round(r.choice([18000.00, 20000.00, 22000.00]), 2)
    drop_pct = r.choice([15, 20, 25])
    lost_income = round(original_income * (drop_pct / 100.0), 2)
    new_income = round(original_income - lost_income, 2)
    essential_fixed = round(original_income * 0.55, 2)
    current_variable = round(original_income * 0.35, 2)
    savings = round(original_income * 0.10, 2)
    # The family pauses savings and must cut variable expenses to match new income
    required_cuts = round(lost_income, 2)
    ans_str = _fmt_curr(required_cuts)

    prompt = (
        f"{name}'s company reduces operational hours, causing {name}'s monthly net income of **{_fmt_curr(original_income)}** to drop by **{drop_pct}%**.\n\n"
        f"1. Calculate the monetary reduction in {name}'s monthly income.\n"
        f"2. To keep the budget balanced without incurring debt, calculate the **total amount of expenses {name} must cut from monthly spending**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• When household income decreases, total expenditure must decrease by an equal amount to avoid falling into debt or running a deficit:\n"
        f"  $$\\text{{Required Expenditure Cut}} = \\text{{Income Reduction}} = \\text{{Original Income}} \\times \\frac{{\\text{{Percentage Drop}}}}{{100}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Income Reduction}} = \\text{{{_fmt_curr(original_income)}}} \\times \\frac{{{drop_pct}}}{{100}} = \\text{{{_fmt_curr(lost_income)}}}$.\n"
        f"• $\\text{{Required Expenditure Cuts}} = \\text{{{_fmt_curr(lost_income)}}}$.\n"
        f"✓ **[1 Mark: Method – multiplying original income by drop percentage]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct expenditure cut amount in Rands]**"
    )
    return _make_q(
        subskill="budg_hh_income_drop_rebalancing",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – original income × drop_pct ÷ 100", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Calculate {drop_pct}% of {_fmt_curr(original_income)}.",
            "tier_2": f"{_fmt_curr(original_income)} × ({drop_pct} ÷ 100) = {_fmt_curr(lost_income)}.",
            "tier_3": f"Required spending reduction = {_fmt_curr(lost_income)}."
        },
        r=r
    )

def _gen_budg_hh_emergency_unforeseen_expense(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    monthly_surplus = round(r.choice([1400.00, 1600.00, 1800.00, 2000.00]), 2)
    emergency_fund = round(r.choice([6000.00, 7500.00, 9000.00]), 2)
    repair_cost = round(r.choice([3200.00, 3800.00, 4200.00, 4800.00]), 2)
    # The monthly surplus is used first, and the rest is drawn from emergency fund
    from_surplus = min(monthly_surplus, repair_cost)
    from_fund = round(repair_cost - from_surplus, 2)
    remaining_fund = round(emergency_fund - from_fund, 2)
    ans_str = _fmt_curr(remaining_fund)

    prompt = (
        f"{name}'s household had an accumulated emergency fund savings balance of **{_fmt_curr(emergency_fund)}**.\n\n"
        f"In August, a home geyser burst, requiring an unexpected repair cost of **{_fmt_curr(repair_cost)}**.\n\n"
        f"{name} uses August's monthly budget surplus of **{_fmt_curr(monthly_surplus)}** first, and covers the remaining repair cost from the emergency fund.\n\n"
        f"Calculate the **remaining balance in the emergency savings fund** after paying for the geyser repair."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• The unexpected expense is first partially offset by the current month's surplus:\n"
        f"  $$\\text{{Amount drawn from fund}} = \\text{{Repair Cost}} - \\text{{Monthly Surplus}}$$\n"
        f"• The remaining emergency fund balance is:\n"
        f"  $$\\text{{Remaining Fund}} = \\text{{Initial Fund}} - \\text{{Amount drawn from fund}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Drawn from fund}} = \\text{{{_fmt_curr(repair_cost)}}} - \\text{{{_fmt_curr(monthly_surplus)}}} = \\text{{{_fmt_curr(from_fund)}}}$.\n"
        f"• $\\text{{Remaining Fund}} = \\text{{{_fmt_curr(emergency_fund)}}} - \\text{{{_fmt_curr(from_fund)}}} = \\text{{{_fmt_curr(remaining_fund)}}}$.\n"
        f"✓ **[1 Mark: Method – subtracting monthly surplus from repair cost, then subtracting that shortfall from initial fund]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct remaining emergency fund balance in Rands]**"
    )
    return _make_q(
        subskill="budg_hh_emergency_unforeseen_expense",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – emergency fund - (repair - surplus)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"The surplus pays {_fmt_curr(monthly_surplus)}. The rest ({_fmt_curr(repair_cost)} - {_fmt_curr(monthly_surplus)} = {_fmt_curr(from_fund)}) comes from savings.",
            "tier_2": f"Subtract {_fmt_curr(from_fund)} from the emergency fund of {_fmt_curr(emergency_fund)}.",
            "tier_3": f"Remaining emergency fund = {_fmt_curr(remaining_fund)}."
        },
        r=r
    )

def _gen_budg_hh_two_earner_shared_contributions(r: random.Random) -> Dict[str, Any]:
    name1 = r.choice(SA_NAMES)
    name2 = r.choice([n for n in SA_NAMES if n != name1])
    inc1 = round(r.choice([16000.00, 18000.00, 20000.00]), 2)
    inc2 = round(r.choice([12000.00, 14000.00, 15000.00]), 2)
    combined_inc = round(inc1 + inc2, 2)
    shared_expenses = round(r.choice([14000.00, 16000.00, 17500.00]), 2)
    # Proportional contribution: (Inc1 / Combined) * Shared expenses
    contrib1 = round((inc1 / combined_inc) * shared_expenses, 2)
    ans_str = _fmt_curr(contrib1)

    prompt = (
        f"{name1} and {name2} share a household. They decide to contribute to their monthly shared living expenses of **{_fmt_curr(shared_expenses)}** strictly in proportion to their respective net monthly incomes:\n\n"
        f"• {name1}'s net income: **{_fmt_curr(inc1)}**\n"
        f"• {name2}'s net income: **{_fmt_curr(inc2)}**\n\n"
        f"Calculate **{name1}'s fair monthly contribution** toward the shared household expenses, rounded to 2 decimal places."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• In proportional contribution budgeting, each partner's share is based on their fraction of total household income:\n"
        f"  $$\\text{{Contribution}} = \\left( \\frac{{\\text{{Partner Income}}}}{{\\text{{Combined Household Income}}}} \\right) \\times \\text{{Shared Expenses}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Combined Income}} = \\text{{{_fmt_curr(inc1)}}} + \\text{{{_fmt_curr(inc2)}}} = \\text{{{_fmt_curr(combined_inc)}}}$.\n"
        f"• $\\text{{{name1}'s Fraction}} = \\frac{{{_fmt(inc1)}}}{{{_fmt(combined_inc)}}}$.\n"
        f"• $\\text{{{name1}'s Share}} = \\left( \\frac{{{_fmt(inc1)}}}{{{_fmt(combined_inc)}}} \\right) \\times \\text{{{_fmt_curr(shared_expenses)}}} = \\text{{{_fmt_curr(contrib1)}}}$.\n"
        f"✓ **[1 Mark: Method – finding combined income and calculating proportional share]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct proportional contribution in Rands]**"
    )
    return _make_q(
        subskill="budg_hh_two_earner_shared_contributions",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (inc1 ÷ combined) × shared_expenses", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Add both incomes ({_fmt_curr(inc1)} + {_fmt_curr(inc2)} = {_fmt_curr(combined_inc)}).",
            "tier_2": f"Multiply {_fmt_curr(shared_expenses)} by ({inc1} ÷ {combined_inc}).",
            "tier_3": f"{name1}'s contribution = {_fmt_curr(contrib1)}."
        },
        r=r
    )

def _gen_budg_hh_zero_based_budgeting(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    income = round(r.choice([16500.00, 18500.00, 21000.00]), 2)
    living_exp = round(income * 0.60, 2)
    debt_repay = round(income * 0.20, 2)
    retire_annuity = round(income * 0.10, 2)
    allocated_subtotal = round(living_exp + debt_repay + retire_annuity, 2)
    emergency_target = round(income - allocated_subtotal, 2)
    ans_str = _fmt_curr(emergency_target)

    prompt = (
        f"In **Zero-Based Budgeting (ZBB)**, every Rand of income is deliberately assigned a specific job so that:\n\n"
        f"$$\\text{{Net Income}} - \\text{{Living Expenses}} - \\text{{Debt Repayments}} - \\text{{Retirement}} - \\text{{Emergency Savings}} = \\text{{R 0,00}}$$\n\n"
        f"{name}'s net monthly income is **{_fmt_curr(income)}**.\n"
        f"{name} has already allocated:\n"
        f"• Living expenses: **{_fmt_curr(living_exp)}**\n"
        f"• Debt reduction: **{_fmt_curr(debt_repay)}**\n"
        f"• Retirement annuity: **{_fmt_curr(retire_annuity)}**\n\n"
        f"Calculate the **final remaining amount that must be assigned to Emergency Savings** to achieve a true zero balance."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Under zero-based budgeting, $\\text{{Income}} - \\text{{All Allocations}} = 0$. Therefore:\n"
        f"  $$\\text{{Remaining Allocation}} = \\text{{Net Income}} - (\\text{{Living Expenses}} + \\text{{Debt}} + \\text{{Retirement}})$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Allocated Subtotal}} = \\text{{{_fmt_curr(living_exp)}}} + \\text{{{_fmt_curr(debt_repay)}}} + \\text{{{_fmt_curr(retire_annuity)}}} = \\text{{{_fmt_curr(allocated_subtotal)}}}$.\n"
        f"• $\\text{{Emergency Savings}} = \\text{{{_fmt_curr(income)}}} - \\text{{{_fmt_curr(allocated_subtotal)}}} = \\text{{{_fmt_curr(emergency_target)}}}$.\n"
        f"✓ **[1 Mark: Method – summing existing allocations and subtracting from total net income]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct remaining allocation in Rands]**"
    )
    return _make_q(
        subskill="budg_hh_zero_based_budgeting",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – income - (living + debt + retirement)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Sum the 3 allocated items ({_fmt_curr(living_exp)} + {_fmt_curr(debt_repay)} + {_fmt_curr(retire_annuity)} = {_fmt_curr(allocated_subtotal)}).",
            "tier_2": f"Subtract that subtotal from net income ({_fmt_curr(income)}).",
            "tier_3": f"Emergency savings assignment = {_fmt_curr(emergency_target)}."
        },
        r=r
    )
