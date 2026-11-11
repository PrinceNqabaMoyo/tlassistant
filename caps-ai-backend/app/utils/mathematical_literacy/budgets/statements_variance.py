"""Cluster 5: Income & Expenditure Statements & Variance Analysis (8 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_budg_stmt_actual_vs_budgeted_variance(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    categories = [
        ("Electricity", round(r.choice([800.00, 950.00, 1100.00]), 2), r.choice([120.00, 180.00, 250.00])),
        ("Groceries", round(r.choice([3200.00, 3600.00, 4000.00]), 2), r.choice([250.00, 380.00, 450.00])),
        ("Petrol / Fuel", round(r.choice([1400.00, 1600.00, 1800.00]), 2), r.choice([150.00, 220.00, 300.00])),
        ("Cell Data", round(r.choice([350.00, 450.00, 500.00]), 2), r.choice([50.00, 80.00, 100.00]))
    ]
    cat_name, budgeted, delta = r.choice(categories)
    is_over = r.choice([True, False])
    if is_over:
        actual = round(budgeted + delta, 2)
        variance_label = "Unfavourable (Over budget)"
        ans_str = f"Over budget by {_fmt_curr(delta)}"
    else:
        actual = round(budgeted - delta, 2)
        variance_label = "Favourable (Under budget)"
        ans_str = f"Under budget by {_fmt_curr(delta)}"

    prompt = (
        f"{name}'s financial record for the month of October shows the following figures for **{cat_name}**:\n\n"
        f"• Budgeted amount: **{_fmt_curr(budgeted)}**\n"
        f"• Actual amount spent: **{_fmt_curr(actual)}**\n\n"
        f"1. Calculate the monetary variance between actual expenditure and budgeted expenditure.\n"
        f"2. Indicate whether this variance is **Over budget** or **Under budget**, including the exact amount."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Expenditure variance analysis assesses whether spending adhered to financial planning:\n"
        f"  $$\\text{{Variance}} = |\\text{{Actual Spent}} - \\text{{Budgeted}}|$$\n"
        f"• For an expenditure item:\n"
        f"  - If $\\text{{Actual}} > \\text{{Budgeted}}$, the household spent more than planned (**Over budget / Unfavourable**).\n"
        f"  - If $\\text{{Actual}} < \\text{{Budgeted}}$, money was saved (**Under budget / Favourable**).\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Variance}} = |\\text{{{_fmt_curr(actual)}}} - \\text{{{_fmt_curr(budgeted)}}}| = \\text{{{_fmt_curr(delta)}}}$.\n"
        f"• Since actual spending ({_fmt_curr(actual)}) was {'higher' if is_over else 'lower'} than budgeted ({_fmt_curr(budgeted)}), the outcome is **{ans_str}**.\n"
        f"✓ **[1 Mark: Method – subtracting budgeted from actual and interpreting over/under direction]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct over/under status and Rand value]**"
    )
    custom_opts = [
        f"Over budget by {_fmt_curr(delta)}",
        f"Under budget by {_fmt_curr(delta)}",
        f"Over budget by {_fmt_curr(round(delta * 1.2, 2))}",
        f"Under budget by {_fmt_curr(round(delta * 1.2, 2))}"
    ]
    return _make_q(
        subskill="budg_stmt_actual_vs_budgeted_variance",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – |actual - budgeted|", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Subtract the smaller amount from the larger amount: |{_fmt_curr(actual)} - {_fmt_curr(budgeted)}| = {_fmt_curr(delta)}.",
            "tier_2": f"If actual expenditure is greater than budget, it is over budget. If less, under budget.",
            "tier_3": f"Variance outcome: {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_budg_stmt_running_balance_ledger(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    opening_balance = round(r.choice([3500.00, 4200.00, 5000.00, 6200.00]), 2)
    salary_credit = round(r.choice([14000.00, 16500.00, 18000.00]), 2)
    rent_debit = round(r.choice([4800.00, 5200.00, 5600.00]), 2)
    groceries_debit = round(r.choice([1650.00, 1850.00, 2100.00]), 2)
    closing_balance = round(opening_balance + salary_credit - rent_debit - groceries_debit, 2)
    ans_str = _fmt_curr(closing_balance)

    table_md = (
        f"| Date | Transaction Description | Debit (-) | Credit (+) | Running Balance |\n"
        f"| :--- | :--- | :--- | :--- | :--- |\n"
        f"| 01 Nov | Opening Balance | | | {_fmt_curr(opening_balance)} |\n"
        f"| 25 Nov | Salary Electronic Transfer | | {_fmt_curr(salary_credit)} | {_fmt_curr(opening_balance + salary_credit)} |\n"
        f"| 26 Nov | Rent Debit Order | {_fmt_curr(rent_debit)} | | {_fmt_curr(opening_balance + salary_credit - rent_debit)} |\n"
        f"| 28 Nov | Supermarket Card Purchase | {_fmt_curr(groceries_debit)} | | **[ ? ]** |\n"
    )

    prompt = (
        f"The extract below is from {name}'s retail bank statement for November:\n\n"
        f"{table_md}\n\n"
        f"Calculate the **Final Closing Running Balance** on 28 November."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• In a bank statement ledger:\n"
        f"  - **Credits (+)** represent incoming deposits that increase the account balance.\n"
        f"  - **Debits (-)** represent outgoing payments and purchases that decrease the account balance.\n"
        f"  $$\\text{{Closing Balance}} = \\text{{Previous Balance}} - \\text{{Debit Amount}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• Balance on 26 Nov = $\\text{{{_fmt_curr(opening_balance + salary_credit - rent_debit)}}}$.\n"
        f"• Debit on 28 Nov = $\\text{{{_fmt_curr(groceries_debit)}}}$.\n"
        f"• $\\text{{Final Balance}} = \\text{{{_fmt_curr(opening_balance + salary_credit - rent_debit)}}} - \\text{{{_fmt_curr(groceries_debit)}}} = \\text{{{_fmt_curr(closing_balance)}}}$.\n"
        f"✓ **[1 Mark: Method – subtracting debit transaction from previous running balance]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct closing bank balance in Rands]**"
    )
    return _make_q(
        subskill="budg_stmt_running_balance_ledger",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – previous balance - debit", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Look at the balance on 26 Nov ({_fmt_curr(opening_balance + salary_credit - rent_debit)}) and subtract the 28 Nov debit of {_fmt_curr(groceries_debit)}.",
            "tier_2": f"{_fmt_curr(opening_balance + salary_credit - rent_debit)} - {_fmt_curr(groceries_debit)}.",
            "tier_3": f"Closing balance = {_fmt_curr(closing_balance)}."
        },
        r=r
    )

def _gen_budg_stmt_reconciliation_discrepancy(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    cash_book_balance = round(r.choice([8450.00, 9200.00, 10500.00]), 2)
    unrecorded_bank_fee = round(r.choice([115.00, 145.00, 175.00]), 2)
    unrecorded_interest = round(r.choice([25.00, 35.00, 45.00]), 2)
    # Reconciled bank balance = Cash book balance - bank fee + interest
    reconciled_balance = round(cash_book_balance - unrecorded_bank_fee + unrecorded_interest, 2)
    ans_str = _fmt_curr(reconciled_balance)

    prompt = (
        f"{name} performs a monthly bank reconciliation at the end of July:\n\n"
        f"• Personal budget cash book closing balance: **{_fmt_curr(cash_book_balance)}**\n"
        f"• Upon inspecting the official bank statement, {name} discovers two unrecorded transactions:\n"
        f"  1. Monthly bank service fees and electronic transaction charges: **{_fmt_curr(unrecorded_bank_fee)}**\n"
        f"  2. Positive credit interest earned on the savings balance: **{_fmt_curr(unrecorded_interest)}**\n\n"
        f"Calculate {name}'s **Corrected (Reconciled) Bank Account Balance**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Bank reconciliation updates the internal budget record for automated bank fees and interest not yet recorded in the personal cash log:\n"
        f"  $$\\text{{Reconciled Balance}} = \\text{{Cash Book Balance}} - \\text{{Bank Charges}} + \\text{{Interest Earned}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Reconciled Balance}} = \\text{{{_fmt_curr(cash_book_balance)}}} - \\text{{{_fmt_curr(unrecorded_bank_fee)}}} + \\text{{{_fmt_curr(unrecorded_interest)}}} = \\text{{{_fmt_curr(reconciled_balance)}}}$.\n"
        f"✓ **[1 Mark: Method – subtracting unrecorded bank fees and adding interest earned]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct reconciled balance in Rands]**"
    )
    return _make_q(
        subskill="budg_stmt_reconciliation_discrepancy",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – cash_book - bank_fee + interest", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Subtract the bank fees ({_fmt_curr(unrecorded_bank_fee)}) from {_fmt_curr(cash_book_balance)} and add interest ({_fmt_curr(unrecorded_interest)}).",
            "tier_2": f"{cash_book_balance} - {unrecorded_bank_fee} + {unrecorded_interest} = {reconciled_balance}.",
            "tier_3": f"Reconciled balance = {_fmt_curr(reconciled_balance)}."
        },
        r=r
    )

def _gen_budg_stmt_monthly_cash_flow_statement(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    salary_inflow = round(r.choice([16000.00, 18500.00, 21000.00]), 2)
    side_business_inflow = round(r.choice([2500.00, 3200.00, 4000.00]), 2)
    total_inflows = round(salary_inflow + side_business_inflow, 2)

    living_outflow = round(r.choice([11000.00, 12500.00, 13500.00]), 2)
    debt_outflow = round(r.choice([2200.00, 2800.00, 3400.00]), 2)
    total_outflows = round(living_outflow + debt_outflow, 2)

    net_cash_flow = round(total_inflows - total_outflows, 2)
    ans_str = _fmt_curr(net_cash_flow)

    prompt = (
        f"{name} prepares a monthly Cash Flow Statement for June:\n\n"
        f"**Cash Inflows (Receipts):**\n"
        f"• Net salary: **{_fmt_curr(salary_inflow)}**\n"
        f"• Weekend craft market sales: **{_fmt_curr(side_business_inflow)}**\n\n"
        f"**Cash Outflows (Disbursements):**\n"
        f"• Living expenses paid: **{_fmt_curr(living_outflow)}**\n"
        f"• Study loan & debt payments: **{_fmt_curr(debt_outflow)}**\n\n"
        f"1. Calculate the total cash inflows and total cash outflows.\n"
        f"2. Calculate the **Net Cash Flow** for the month of June."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Net Cash Flow represents the actual surplus or deficit of physical cash moving into and out of an individual's possession:\n"
        f"  $$\\text{{Net Cash Flow}} = \\sum \\text{{Cash Inflows}} - \\sum \\text{{Cash Outflows}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Total Inflows}} = \\text{{{_fmt_curr(salary_inflow)}}} + \\text{{{_fmt_curr(side_business_inflow)}}} = \\text{{{_fmt_curr(total_inflows)}}}$.\n"
        f"• $\\text{{Total Outflows}} = \\text{{{_fmt_curr(living_outflow)}}} + \\text{{{_fmt_curr(debt_outflow)}}} = \\text{{{_fmt_curr(total_outflows)}}}$.\n"
        f"• $\\text{{Net Cash Flow}} = \\text{{{_fmt_curr(total_inflows)}}} - \\text{{{_fmt_curr(total_outflows)}}} = \\text{{{_fmt_curr(net_cash_flow)}}}$.\n"
        f"✓ **[1 Mark: Method – summing inflows, summing outflows, and subtracting total outflows from total inflows]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct net cash flow in Rands]**"
    )
    return _make_q(
        subskill="budg_stmt_monthly_cash_flow_statement",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total inflows - total outflows", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Inflows = {_fmt_curr(salary_inflow)} + {_fmt_curr(side_business_inflow)} = {_fmt_curr(total_inflows)}. Outflows = {_fmt_curr(living_outflow)} + {_fmt_curr(debt_outflow)} = {_fmt_curr(total_outflows)}.",
            "tier_2": f"Subtract total outflows from total inflows: {_fmt_curr(total_inflows)} - {_fmt_curr(total_outflows)}.",
            "tier_3": f"Net cash flow = {_fmt_curr(net_cash_flow)}."
        },
        r=r
    )

def _gen_budg_stmt_bank_charges_fee_schedule(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    monthly_fee = round(r.choice([60.00, 75.00, 89.00]), 2)
    atm_withdrawals_count = r.choice([3, 4, 5])
    atm_fee_per_tx = round(r.choice([12.00, 14.50, 16.00]), 2)
    total_atm_fees = round(atm_withdrawals_count * atm_fee_per_tx, 2)
    debit_order_count = r.choice([4, 5, 6])
    debit_order_fee = round(r.choice([4.50, 5.00, 5.50]), 2)
    total_debit_fees = round(debit_order_count * debit_order_fee, 2)
    grand_bank_charges = round(monthly_fee + total_atm_fees + total_debit_fees, 2)
    ans_str = _fmt_curr(grand_bank_charges)

    prompt = (
        f"{name}'s cheque account fee pricing guide includes the following charges:\n\n"
        f"• Fixed monthly account administration fee: **{_fmt_curr(monthly_fee)}**\n"
        f"• Own-bank ATM cash withdrawal fee: **{_fmt_curr(atm_fee_per_tx)} per withdrawal**\n"
        f"• Electronic debit order processing fee: **{_fmt_curr(debit_order_fee)} per debit order**\n\n"
        f"During September, {name} makes **{atm_withdrawals_count} ATM cash withdrawals** and has **{debit_order_count} electronic debit orders** processed.\n\n"
        f"Calculate {name}'s **Total Bank Charges** for September."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Total bank charges combine fixed monthly maintenance and variable transaction-based fees:\n"
        f"  $$\\text{{Total Bank Charges}} = \\text{{Monthly Admin}} + (\\text{{ATM Fee}} \\times \\text{{Count}}) + (\\text{{Debit Fee}} \\times \\text{{Count}})$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{ATM Fees}} = \\text{{{_fmt_curr(atm_fee_per_tx)}}} \\times {atm_withdrawals_count} = \\text{{{_fmt_curr(total_atm_fees)}}}$.\n"
        f"• $\\text{{Debit Order Fees}} = \\text{{{_fmt_curr(debit_order_fee)}}} \\times {debit_order_count} = \\text{{{_fmt_curr(total_debit_fees)}}}$.\n"
        f"• $\\text{{Total Charges}} = \\text{{{_fmt_curr(monthly_fee)}}} + \\text{{{_fmt_curr(total_atm_fees)}}} + \\text{{{_fmt_curr(total_debit_fees)}}} = \\text{{{_fmt_curr(grand_bank_charges)}}}$.\n"
        f"✓ **[1 Mark: Method – multiplying transaction rates by volumes and adding monthly base fee]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total bank charges in Rands]**"
    )
    return _make_q(
        subskill="budg_stmt_bank_charges_fee_schedule",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – monthly fee + (ATM fee × count) + (debit fee × count)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"ATM charges = {_fmt_curr(atm_fee_per_tx)} × {atm_withdrawals_count} = {_fmt_curr(total_atm_fees)}. Debit fees = {_fmt_curr(debit_order_fee)} × {debit_order_count} = {_fmt_curr(total_debit_fees)}.",
            "tier_2": f"Add the base monthly fee ({_fmt_curr(monthly_fee)}) + ATM fees + debit fees.",
            "tier_3": f"Total bank fees = {_fmt_curr(grand_bank_charges)}."
        },
        r=r
    )

def _gen_budg_stmt_interest_earned_on_savings(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    balance = round(r.choice([15000.00, 18000.00, 24000.00, 30000.00]), 2)
    annual_rate_pct = r.choice([6.0, 7.5, 8.0, 8.5])
    # Monthly simple interest: I = P * r * (1/12)
    monthly_interest = round(balance * (annual_rate_pct / 100.0) / 12, 2)
    ans_str = _fmt_curr(monthly_interest)

    prompt = (
        f"{name} maintains a positive balance of **{_fmt_curr(balance)}** in a 32-day notice bank savings deposit.\n\n"
        f"The bank pays a simple interest rate of **{_fmt(annual_rate_pct)}% per annum (p.a.)**.\n\n"
        f"Calculate the **interest income earned for one month**, rounded to 2 decimal places."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Monthly simple interest is calculated using the standard formula:\n"
        f"  $$I = P \\times \\frac{{r}}{{100}} \\times \\frac{{1}}{{12}}$$\n"
        f"  where $P$ is principal balance, $r$ is annual percentage rate, and $t = \\frac{{1}}{{12}}$ year.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• Annual interest = $\\text{{{_fmt_curr(balance)}}} \\times \\frac{{{_fmt(annual_rate_pct)}}}{{100}} = \\text{{{_fmt_curr(balance * annual_rate_pct / 100)}}}$.\n"
        f"• Monthly interest = $\\frac{{\\text{{{_fmt_curr(balance * annual_rate_pct / 100)}}}}}{{12}} = \\text{{{_fmt_curr(monthly_interest)}}}$.\n"
        f"✓ **[1 Mark: Method – multiplying balance by annual rate and dividing by 12 months]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct monthly interest earned in Rands]**"
    )
    return _make_q(
        subskill="budg_stmt_interest_earned_on_savings",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – balance × (annual_rate ÷ 100) ÷ 12", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Calculate annual interest: {_fmt_curr(balance)} × {_fmt(annual_rate_pct)}% = {_fmt_curr(balance * annual_rate_pct / 100)}.",
            "tier_2": f"Divide the annual interest by 12 months.",
            "tier_3": f"Monthly interest earned = {_fmt_curr(monthly_interest)}."
        },
        r=r
    )

def _gen_budg_stmt_vat_inclusive_adjustment(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    exclusive_cost = round(r.choice([1200.00, 1500.00, 1800.00, 2200.00]), 2)
    vat_rate = 15  # 15% in South Africa
    vat_amount = round(exclusive_cost * 0.15, 2)
    inclusive_cost = round(exclusive_cost + vat_amount, 2)
    ans_str = _fmt_curr(inclusive_cost)

    prompt = (
        f"{name} receives a quotation of **{_fmt_curr(exclusive_cost)} exclusive of VAT** for laptop repair and servicing required for personal studies.\n\n"
        f"In South Africa, Value Added Tax (VAT) is charged at a standard statutory rate of **15%**.\n\n"
        f"Calculate the **final VAT-inclusive expenditure** that {name} must budget to settle the invoice."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• South African VAT is 15%. To convert a VAT-exclusive price to a VAT-inclusive price:\n"
        f"  $$\\text{{VAT Amount}} = \\text{{Exclusive Price}} \\times 15\\%$$\n"
        f"  $$\\text{{VAT Inclusive Price}} = \\text{{Exclusive Price}} + \\text{{VAT Amount}} = \\text{{Exclusive Price}} \\times 1,15$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{VAT (15\\%)}} = \\text{{{_fmt_curr(exclusive_cost)}}} \\times 0,15 = \\text{{{_fmt_curr(vat_amount)}}}$.\n"
        f"• $\\text{{VAT Inclusive Price}} = \\text{{{_fmt_curr(exclusive_cost)}}} + \\text{{{_fmt_curr(vat_amount)}}} = \\text{{{_fmt_curr(inclusive_cost)}}}$.\n"
        f"✓ **[1 Mark: Method – calculating 15% VAT and adding to exclusive price (or multiplying by 1,15)]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct VAT-inclusive expenditure in Rands]**"
    )
    return _make_q(
        subskill="budg_stmt_vat_inclusive_adjustment",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – exclusive price × 1,15", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Multiply the exclusive price {_fmt_curr(exclusive_cost)} by 1,15 (or calculate 15% VAT and add it).",
            "tier_2": f"VAT = {_fmt_curr(exclusive_cost)} × 0,15 = {_fmt_curr(vat_amount)}. Add to {_fmt_curr(exclusive_cost)}.",
            "tier_3": f"Total VAT inclusive = {_fmt_curr(inclusive_cost)}."
        },
        r=r
    )

def _gen_budg_stmt_unexpected_medical_impact(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    doctor_bill = round(r.choice([1650.00, 1850.00, 2200.00]), 2)
    scheme_coverage_pct = r.choice([60, 70, 75, 80])
    covered_amount = round(doctor_bill * (scheme_coverage_pct / 100.0), 2)
    shortfall = round(doctor_bill - covered_amount, 2)
    ans_str = _fmt_curr(shortfall)

    prompt = (
        f"{name} visits a specialist medical doctor and receives an account of **{_fmt_curr(doctor_bill)}**.\n\n"
        f"{name}'s medical scheme policy covers **{scheme_coverage_pct}%** of the total medical tariff.\n\n"
        f"The remaining balance (co-payment shortfall) must be paid out of {name}'s personal monthly pocket budget.\n\n"
        f"Calculate the **out-of-pocket medical co-payment** that {name} must pay."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• The member's out-of-pocket shortfall is the portion not paid by the medical scheme:\n"
        f"  $$\\text{{Member Share (\\%)}} = 100\\% - {scheme_coverage_pct}\\% = {100 - scheme_coverage_pct}\\%$$\n"
        f"  $$\\text{{Out-of-Pocket Payment}} = \\text{{Doctor Bill}} \\times \\left( \\frac{{{100 - scheme_coverage_pct}}}{{100}} \\right)$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Scheme Covered}} = \\text{{{_fmt_curr(doctor_bill)}}} \\times \\frac{{{scheme_coverage_pct}}}{{100}} = \\text{{{_fmt_curr(covered_amount)}}}$.\n"
        f"• $\\text{{Out-of-Pocket Shortfall}} = \\text{{{_fmt_curr(doctor_bill)}}} - \\text{{{_fmt_curr(covered_amount)}}} = \\text{{{_fmt_curr(shortfall)}}}$.\n"
        f"✓ **[1 Mark: Method – finding covered amount and subtracting from total bill, or multiplying bill by (100 - coverage)%]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct out-of-pocket medical co-payment in Rands]**"
    )
    return _make_q(
        subskill="budg_stmt_unexpected_medical_impact",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – doctor bill × (1 - coverage_rate)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"The medical scheme pays {scheme_coverage_pct}%. Therefore, {name} pays {100 - scheme_coverage_pct}%.",
            "tier_2": f"Calculate {100 - scheme_coverage_pct}% of {_fmt_curr(doctor_bill)}: {_fmt_curr(doctor_bill)} × {100 - scheme_coverage_pct} ÷ 100.",
            "tier_3": f"Out-of-pocket co-payment = {_fmt_curr(shortfall)}."
        },
        r=r
    )
