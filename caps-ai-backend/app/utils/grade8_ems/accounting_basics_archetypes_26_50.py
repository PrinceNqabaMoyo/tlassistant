"""Grade 8 EMS — Accounting Concepts Archetypes 26–50.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 2/01. Accounting concepts.md.
Covers budgets, savings, commercial banking, financial records, transactions, compliance & synthesis.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List
from xml.sax.saxutils import escape as _xml_escape

from app.utils.ems_namelist import AREAS, NAMES, SUPPLIERS
from app.utils.grade8_ems.accounting_basics_archetypes_01_25 import (
    _BANKS,
    _make_mcq,
    _make_rubric,
    _make_table,
    _make_typed,
    _svg_ledger_card,
    fmt_r,
    get_ems_scenario,
)


def _svg_bank_intermediation(savers_area: str, bank: str, biz: str, deposit_amt: int, loan_amt: int) -> str:
    """Render Paper & Ink Financial Intermediation flow SVG."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 165" width="100%" style="max-width:540px;font-family:Arial,sans-serif;">'
        '<rect x="4" y="4" width="532" height="157" rx="8" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.5"/>'
        '<rect x="16" y="40" width="146" height="82" rx="6" fill="#EFF6FF" stroke="#1D4ED8" stroke-width="1.5"/>'
        '<text x="89" y="64" font-size="11" font-weight="bold" text-anchor="middle" fill="#1E3A8A">Household Savers</text>'
        f'<text x="89" y="82" font-size="10" text-anchor="middle" fill="#334155">{_xml_escape(savers_area)}</text>'
        f'<text x="89" y="102" font-size="11" font-weight="bold" text-anchor="middle" fill="#0F172A">Deposits: {_xml_escape(fmt_r(deposit_amt))}</text>'
        '<line x1="164" y1="81" x2="196" y2="81" stroke="#0F766E" stroke-width="2.5"/>'
        '<polygon points="196,76 206,81 196,86" fill="#0F766E"/>'
        '<rect x="208" y="34" width="124" height="94" rx="6" fill="#13519C"/>'
        f'<text x="270" y="68" font-size="12" font-weight="bold" text-anchor="middle" fill="#FFFFFF">{_xml_escape(bank)}</text>'
        '<text x="270" y="88" font-size="10" text-anchor="middle" fill="#DBEAFE">Commercial Bank</text>'
        '<text x="270" y="106" font-size="9" text-anchor="middle" fill="#BFDBFE">(Intermediary)</text>'
        '<line x1="334" y1="81" x2="366" y2="81" stroke="#1D4ED8" stroke-width="2.5"/>'
        '<polygon points="366,76 376,81 366,86" fill="#1D4ED8"/>'
        '<rect x="378" y="40" width="146" height="82" rx="6" fill="#ECFDF5" stroke="#047857" stroke-width="1.5"/>'
        f'<text x="451" y="64" font-size="11" font-weight="bold" text-anchor="middle" fill="#065F46">{_xml_escape(biz[:20])}</text>'
        '<text x="451" y="82" font-size="10" text-anchor="middle" fill="#334155">Business Expansion</text>'
        f'<text x="451" y="102" font-size="11" font-weight="bold" text-anchor="middle" fill="#0F172A">Loan: {_xml_escape(fmt_r(loan_amt))}</text>'
        '<text x="270" y="146" font-size="10" text-anchor="middle" fill="#475569">Interest paid to savers &lt; Interest charged on business loans</text>'
        '</svg>'
    )


def _b26_business_budget_definition_purpose(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    est_rev = rng.randint(25, 60) * 1000
    est_exp = rng.randint(18, 45) * 1000
    prompt = (
        f"Before the start of next quarter, {s['entrepreneur']} prepares a written forecast for {s['business']} in {s['area']} "
        f"estimating cash receipts of {fmt_r(est_rev)} and cash expenses of {fmt_r(est_exp)}. "
        f"What is the primary purpose of this business budget?"
    )
    ans = "To estimate future income and expenditure so {s['business']} can schedule spending and avoid cash shortfalls"
    opts = [
        "To estimate future income and expenditure so {s['business']} can schedule spending and avoid cash shortfalls",
        "To replace the need for issuing receipts and keeping financial records",
        "To calculate exact past net worth after the year has already closed",
        "To eliminate all fixed costs such as rent and staff salaries permanently",
    ]
    exp = f"A business budget estimates expected income ({fmt_r(est_rev)}) and expenses ({fmt_r(est_exp)}) in advance to control spending, spot deficits early, and guide financial decisions."
    return _make_mcq(
        rng,
        subskill="26_business_budget_definition_purpose",
        title="Purpose of a Business Budget",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Notice budgets look FORWARD into next quarter rather than backward.",
            "tier_2": "A budget forecasts estimated income and expenses to manage cash flow responsibly.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_budget_forecast_with_past_records"],
        question_family_id="budget_purpose",
    )


def _b27_cash_budget_surplus_or_deficit_calc(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    open_bank = rng.randint(4, 15) * 1000
    receipts = rng.randint(25, 55) * 1000
    payments = rng.randint(20, 48) * 1000
    closing = open_bank + receipts - payments
    ans = fmt_r(closing)

    card_svg = _svg_ledger_card(
        f"{s['business']} — Monthly Cash Budget",
        f"Area: {s['area']} | Owner: {s['entrepreneur']}",
        [
            ("Opening Bank Balance", fmt_r(open_bank)),
            ("Budgeted Cash Receipts", fmt_r(receipts)),
            ("Budgeted Cash Payments", fmt_r(payments)),
        ],
    )
    prompt = (
        f"Examine the Monthly Cash Budget summary for {s['business']}. "
        f"Calculate the projected Closing Bank Balance at the end of the month (Opening Bank + Budgeted Receipts - Budgeted Payments)."
    )
    steps = [
        f"Total cash available = Opening Bank ({fmt_r(open_bank)}) + Budgeted Receipts ({fmt_r(receipts)}) = {fmt_r(open_bank + receipts)}.",
        f"Subtract Budgeted Cash Payments: {fmt_r(open_bank + receipts)} - {fmt_r(payments)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="27_cash_budget_surplus_or_deficit_calc",
        title="Projected Closing Cash Budget Balance",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{closing}", str(closing)],
        steps=steps,
        hints={
            "tier_1": "Add Opening Bank Balance and Budgeted Receipts first.",
            "tier_2": "Then subtract Budgeted Cash Payments to find the Closing Bank Balance.",
            "tier_3": f"{fmt_r(open_bank)} + {fmt_r(receipts)} - {fmt_r(payments)} = {ans}.",
        },
        misconception_tags=["ignores_opening_cash_balance_in_budget"],
        question_family_id="cash_budget_calc",
        diagram_spec={"kind": "inline_svg", "svg": card_svg, "diagram_role": "context"},
    )


def _b28_personal_vs_business_budget(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    rent = rng.randint(3, 8) * 1000
    food = rng.randint(2, 5) * 1000
    luxury = rng.randint(1, 3) * 1000
    prompt = (
        f"{owner} lives in {s['area']} and manages both a household budget (rent {fmt_r(rent)}, groceries {fmt_r(food)}, streaming luxury {fmt_r(luxury)}) "
        f"and the business budget for {s['business']}. Explain THREE practical reasons why keeping a household budget separate from a business budget prevents cash crisis."
    )
    sample = (
        f"1. Protects business working capital by stopping {owner} from spending shop cash on household luxuries ({fmt_r(luxury)}) without recording Drawings.\n"
        f"2. Enables accurate tracking of whether {s['business']} is profitable on its own, separate from family living costs ({fmt_r(rent + food)}).\n"
        f"3. Ensures essential fixed bills (business rent and household necessities) are prioritised ahead of wants."
    )
    pts = [
        "Separates owner's personal spending/wants from business working capital.",
        "Allows accurate measurement of true business profitability vs household expenditure.",
        "Helps prioritise essential needs/fixed obligations before non-essential wants.",
    ]
    return _make_rubric(
        rng,
        subskill="28_personal_vs_business_budget",
        title="Personal vs Business Budget Separation",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about what happens if shop cash pays for household groceries without tracking.",
            "tier_2": "Mention separating entity cash flows, measuring true profit, and prioritising needs over wants.",
            "tier_3": sample,
        },
        misconception_tags=["mixes_personal_and_business_finances"],
        question_family_id="budget_separation_rubric",
        marks=3,
    )


def _b29_savings_definition_purpose(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    rev = rng.randint(15, 40) * 1000
    save_amt = rng.randint(2, 6) * 1000
    prompt = (
        f"After paying all expenses out of {fmt_r(rev)} monthly income, {s['entrepreneur']} sets aside {fmt_r(save_amt)} "
        f"into an interest-bearing reserve rather than spending it immediately. In financial literacy, what is this {fmt_r(save_amt)} called and why is it held?"
    )
    ans = "Savings — income not spent immediately, reserved for emergencies, future capital, or expansion"
    opts = [
        "Savings — income not spent immediately, reserved for emergencies, future capital, or expansion",
        "Creditors Control — short-term debt owed to suppliers",
        "Operating Expense — money consumed on utility bills",
        "Bank Overdraft — borrowing money from the bank above account funds",
    ]
    exp = f"Savings is the portion of income ({fmt_r(save_amt)}) not spent on current consumption, set aside for emergencies, equipment replacement, or expanding {s['business']} without expensive debt."
    return _make_mcq(
        rng,
        subskill="29_savings_definition_purpose",
        title="Definition & Purpose of Savings",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Unspent income set aside for future use or emergencies has a specific financial term.",
            "tier_2": "Savings protect against unexpected shocks and reduce reliance on borrowed capital.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_savings_with_expenses"],
        question_family_id="savings_concept",
    )


def _b30_savings_compound_interest_comparison(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    principal = rng.randint(10, 40) * 1000
    rate = rng.choice([6, 8, 9, 10])
    interest = int(principal * rate / 100)
    total = principal + interest
    ans = fmt_r(total)
    prompt = (
        f"Instead of hiding {fmt_r(principal)} cash in a metal box at {s['business']}, {s['entrepreneur']} deposits it into a {bank} 1-year savings account earning {rate}% interest per year. "
        f"Calculate the total amount {s['entrepreneur']} will have in the bank after 1 year."
    )
    steps = [
        f"Calculate 1 year's interest: {fmt_r(principal)} x {rate}% = {fmt_r(interest)}.",
        f"Total after 1 year = Principal + Interest = {fmt_r(principal)} + {fmt_r(interest)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="30_savings_compound_interest_comparison",
        title="Calculate Bank Savings Growth",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{total}", str(total)],
        steps=steps,
        hints={
            "tier_1": f"First find {rate}% of {fmt_r(principal)}.",
            "tier_2": "Add the interest earned to the original principal deposit.",
            "tier_3": f"{fmt_r(principal)} + {fmt_r(interest)} = {ans}.",
        },
        misconception_tags=["forgets_to_add_principal_to_interest"],
        question_family_id="savings_interest_calc",
    )


def _b31_banking_role_modern_economy(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    daily_cash = rng.randint(4, 15) * 1000
    bank = rng.choice(_BANKS)
    prompt = (
        f"{s['business']} in {s['area']} takes in about {fmt_r(daily_cash)} per day in cash. "
        f"Advise {s['entrepreneur']} on FOUR practical reasons why depositing takings daily into a commercial account at {bank} is essential for a modern business."
    )
    sample = (
        f"1. Security: Keeping {fmt_r(daily_cash)}/day in a bank protects cash against theft, robbery, and fire.\n"
        f"2. Audit trail: Bank statements create an independent record of receipts and payments for financial control.\n"
        f"3. Convenient electronic payments: Enables EFTs and debit orders to pay suppliers and utilities safely.\n"
        f"4. Credit & interest access: Builds a banking history to qualify for loans and earn interest on positive balances."
    )
    pts = [
        "Protects cash against theft, robbery, and fire on business premises.",
        "Provides reliable financial records via monthly bank statements.",
        "Allows safe electronic payments (EFTs, debit orders, card machines).",
        "Builds creditworthiness for loans and earns interest on surplus deposits.",
    ]
    return _make_rubric(
        rng,
        subskill="31_banking_role_modern_economy",
        title="Why Modern Businesses Use Commercial Banks",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Consider physical risk, bookkeeping records, payment convenience, and future credit.",
            "tier_2": "Cover safety from theft/fire, bank statements, EFTs/debit orders, and loan access/interest.",
            "tier_3": sample,
        },
        misconception_tags=["ignores_non_security_benefits_of_banking"],
        question_family_id="banking_importance_rubric",
    )


def _b32_banking_services_cheque_and_current_acct(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    fee = rng.randint(8, 25) * 10
    prompt = (
        f"{s['business']} uses its business current account at {bank} (monthly fee {fmt_r(fee)}) for daily receipts and supplier payments. "
        f"Which combination lists standard services provided through a business current account?"
    )
    ans = "EFT payments, debit orders, stop orders, bank overdraft facilities, and monthly bank statements"
    opts = [
        "EFT payments, debit orders, stop orders, bank overdraft facilities, and monthly bank statements",
        "Issuing municipal property rates notices and collecting SARS income tax directly",
        "Setting minimum wages under the Basic Conditions of Employment Act",
        "Recording physical stock counts inside warehouse storerooms",
    ]
    exp = f"Commercial banks such as {bank} offer current account services including EFTs, debit orders, stop orders, overdraft facilities, and bank statements to support day-to-day operations."
    return _make_mcq(
        rng,
        subskill="32_banking_services_cheque_and_current_acct",
        title="Commercial Banking Services",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Separate banking services from government tax/labour law roles or internal stock counting.",
            "tier_2": "Banks handle EFTs, debit/stop orders, overdrafts, and bank statements.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_banking_with_government_regulation"],
        question_family_id="banking_services",
    )


def _b33_debit_order_vs_stop_order(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    rent_amt = rng.randint(5, 14) * 1000
    elec_base = rng.randint(15, 45) * 100
    ask_stop = rng.choice([True, False])
    if ask_stop:
        prompt = (
            f"{s['business']} instructs its bank to automatically pay a FIXED amount of {fmt_r(rent_amt)} on the 1st of every month to the landlord's account. "
            f"What banking payment instruction is this?"
        )
        ans = "Stop order (fixed recurring instruction initiated by the account holder)"
        exp = f"A stop order is set up by the account holder ({s['business']}) instructing the bank to pay a fixed amount ({fmt_r(rent_amt)}) on a set recurring date."
    else:
        prompt = (
            f"{s['business']} signs a mandate allowing the mobile telecom company to pull the monthly bill (which varies between {fmt_r(elec_base)} and {fmt_r(elec_base + 450)}) directly from the business bank account. "
            f"What banking payment method is this?"
        )
        ans = "Debit order (variable or fixed amount collected by a third party with account holder permission)"
        exp = f"A debit order authorises a third-party creditor to withdraw varying billed amounts (~{fmt_r(elec_base)}) directly from {s['business']}'s account."
    opts = [
        "Stop order (fixed recurring instruction initiated by the account holder)",
        "Debit order (variable or fixed amount collected by a third party with account holder permission)",
        "Bank overdraft (short-term negative bank balance)",
        "Petty cash voucher (internal office cash receipt)",
    ]
    return _make_mcq(
        rng,
        subskill="33_debit_order_vs_stop_order",
        title="Debit Order vs Stop Order",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Check who initiates the payment and whether the Rand amount can change each month.",
            "tier_2": "Stop order = account holder instructs fixed payment; Debit order = creditor pulls variable/agreed bill with mandate.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_debit_order_and_stop_order"],
        question_family_id="debit_vs_stop_order",
    )


def _b34_atm_eft_online_banking_services(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(3, 19) * 1000
    prompt = (
        f"Instead of carrying {fmt_r(amt)} in cash across {s['area']} to pay {sup}, {s['entrepreneur']} logs into the business banking app and transfers {fmt_r(amt)} directly into {sup}'s account. "
        f"What transaction method was used, and what is its key advantage?"
    )
    ans = "Electronic Funds Transfer (EFT) — faster, lowers cash-theft risk, and leaves a digital bank trail"
    opts = [
        "Electronic Funds Transfer (EFT) — faster, lowers cash-theft risk, and leaves a digital bank trail",
        "Cash Float transfer — increases coins kept in the shop till",
        "Mortgage Bond — creates a 20-year debt secured by property",
        "Lay-buy payment — allows customers to take goods before paying anything",
    ]
    exp = f"Paying {sup} {fmt_r(amt)} via banking app is an Electronic Funds Transfer (EFT). It eliminates cash-in-transit robbery risk and creates an immediate verifiable record."
    return _make_mcq(
        rng,
        subskill="34_atm_eft_online_banking_services",
        title="Electronic Funds Transfer (EFT) & Digital Banking",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Think of the standard electronic bank-to-bank payment method used on banking apps.",
            "tier_2": "EFT transfers funds electronically without handling physical notes.",
            "tier_3": ans,
        },
        misconception_tags=["confuses_eft_with_physical_cash"],
        question_family_id="eft_digital_banking",
    )


def _b35_bank_loan_and_credit_facility(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    loan_amt = rng.randint(40, 120) * 1000
    rate = rng.choice([11, 12, 14])
    prompt = (
        f"{s['business']} wants to buy extra delivery equipment costing {fmt_r(loan_amt)} and approaches {bank} for a business loan at {rate}% annual interest. "
        f"Evaluate ONE major benefit and TWO financial risks of financing expansion using a bank loan rather than waiting to save cash."
    )
    sample = (
        f"Benefit: Enables immediate purchase of productive equipment ({fmt_r(loan_amt)}) so {s['business']} can serve more customers and earn extra revenue right away.\n"
        f"Risk 1: Mandatory interest charges ({rate}% p.a.) increase operating expenses and reduce Net Profit.\n"
        f"Risk 2: Fixed monthly loan repayments must still be paid during slow trading months, risking cash-flow strain or asset repossession."
    )
    pts = [
        "Benefit: Immediate access to capital to buy productive assets and grow revenue sooner.",
        "Risk 1: Interest cost adds an ongoing financial expense that lowers Net Profit.",
        "Risk 2: Fixed repayment obligation creates cash-flow risk if monthly sales drop.",
    ]
    return _make_rubric(
        rng,
        subskill="35_bank_loan_and_credit_facility",
        title="Evaluating Bank Loans for Expansion",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Weigh speed of business growth against the cost and repayment commitment of debt.",
            "tier_2": "Include immediate productive capacity (benefit) + interest expense and rigid repayments (risks).",
            "tier_3": sample,
        },
        misconception_tags=["ignores_interest_and_repayment_risk_of_loans"],
        question_family_id="bank_loan_evaluation",
        marks=3,
    )


def _b36_economic_importance_of_banks(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    dep_amt = rng.randint(150, 400) * 1000
    loan_amt = rng.randint(60, 140) * 1000
    svg = _svg_bank_intermediation(s["area"], bank, s["business"], dep_amt, loan_amt)
    prompt = (
        f"Refer to the financial intermediation model involving households in {s['area']}, {bank}, and {s['business']}. "
        f"How does {bank} stimulate wider economic growth in this system?"
    )
    ans = "By pooling household savings deposits and channelling loans to businesses for investment, production, and job creation"
    opts = [
        "By pooling household savings deposits and channelling loans to businesses for investment, production, and job creation",
        "By printing new bank notes whenever private businesses run low on cash",
        "By banning households from withdrawing savings during profitable trading periods",
        "By paying higher interest rates to depositors than it charges borrowers on loans",
    ]
    exp = f"{bank} acts as a financial intermediary: pooling {fmt_r(dep_amt)} of household deposits and lending {fmt_r(loan_amt)} to businesses like {s['business']} to buy capital goods and create jobs."
    return _make_mcq(
        rng,
        subskill="36_economic_importance_of_banks",
        title="Economic Role of Commercial Banks",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Trace the arrows from savers through the bank to productive enterprises.",
            "tier_2": "Banks channel idle savings into business loans that fund investment and jobs.",
            "tier_3": ans,
        },
        misconception_tags=["thinks_commercial_banks_print_money"],
        question_family_id="economic_role_banks",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def _b37_financial_records_definition_examples(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    year = rng.choice([2024, 2025, 2026])
    prompt = (
        f"A bookkeeper is organising the official financial records of {s['business']} for the {year} financial year. "
        f"Which set consists ONLY of official financial records?"
    )
    ans = "Source documents (receipts, invoices), Cash Journals (CRJ & CPJ), General Ledger, and Bank Statements"
    opts = [
        "Source documents (receipts, invoices), Cash Journals (CRJ & CPJ), General Ledger, and Bank Statements",
        "Staff lunch menus, shop window posters, and customer parking tickets",
        "Supplier price brochures, verbal promises from friends, and product colour samples",
        "Newspaper weather forecasts, social media likes, and employee birthday lists",
    ]
    exp = f"Financial records are documented proof of every money transaction in {s['business']} ({year}), including source documents, journals, ledgers, trial balances, financial statements, and bank statements."
    return _make_mcq(
        rng,
        subskill="37_financial_records_definition_examples",
        title="Identifying Financial Records",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Look for formal accounting documents that verify monetary transactions.",
            "tier_2": "Receipts, invoices, journals, ledgers, and bank statements are official financial records.",
            "tier_3": ans,
        },
        misconception_tags=["includes_marketing_material_as_financial_records"],
        question_family_id="financial_records_id",
    )


def _b38_financial_transactions_definition(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(15, 65) * 100
    prompt = (
        f"Which event at {s['business']} in {s['area']} qualifies as a recordable Financial Transaction?"
    )
    ans = f"Paying {fmt_r(amt)} via EFT to a supplier for stationery delivered today"
    opts = [
        f"Paying {fmt_r(amt)} via EFT to a supplier for stationery delivered today",
        f"Asking three suppliers in {s['area']} to email price quotations for stationery",
        "Interviewing two job applicants for a cashier vacancy starting next month",
        "Rearranging existing display shelves inside the shop without buying anything",
    ]
    exp = f"A financial transaction involves an exchange measured in money ({fmt_r(amt)}) between two parties that changes Assets, Owner's Equity, or Liabilities. Quotations, interviews, and shelf-tidying involve no Rand exchange."
    return _make_mcq(
        rng,
        subskill="38_financial_transactions_definition",
        title="What Counts as a Financial Transaction?",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Ask: Did money, goods, or a legal debt actually change hands in Rands?",
            "tier_2": "Only events changing Assets, Owner's Equity, or Liabilities (measurable in Rands) are financial transactions.",
            "tier_3": ans,
        },
        misconception_tags=["records_quotations_or_interviews_as_transactions"],
        question_family_id="financial_transaction_def",
    )


def _b39_financial_vs_non_financial_events_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    wage_amt = rng.randint(12, 28) * 100
    sale_amt = rng.randint(4, 15) * 100
    headers = ["Business Event", "Financial Transaction? (Yes/No)", "Accounting Element Impact"]
    e1 = f"Paid weekly wages of {fmt_r(wage_amt)} to staff."
    e2 = f"Received price brochure from {rng.choice(SUPPLIERS)}."
    e3 = f"Received {fmt_r(sale_amt)} cash for services rendered."
    e4 = "Cleaned the shop reception area before opening."

    table_rows = [
        [(e1, "given", False), ("Yes", "required", True), ("Assets decrease; Owner's Equity decreases", "required", True)],
        [(e2, "given", False), ("No", "required", True), ("No monetary exchange occurred", "required", True)],
        [(e3, "given", False), ("Yes", "required", True), ("Assets increase; Owner's Equity increases", "required", True)],
        [(e4, "given", False), ("No", "required", True), ("No monetary exchange occurred", "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": "Money was paid out -> Yes.",
        "t0_r0_c2": f"Bank (-{fmt_r(wage_amt)}) and Expense Wages (-OE).",
        "t0_r1_c1": "Receiving a brochure creates no debt or payment -> No.",
        "t0_r1_c2": "No monetary exchange occurred.",
        "t0_r2_c1": "Cash received from client -> Yes.",
        "t0_r2_c2": f"Bank (+{fmt_r(sale_amt)}) and Current Income (+OE).",
        "t0_r3_c1": "Routine cleaning without external payment -> No.",
        "t0_r3_c2": "No monetary exchange occurred.",
    }
    prompt = f"Audit the four events at {s['business']} in {s['area']}. Indicate in the table whether each event is a Financial Transaction (Yes/No) and state its accounting impact."
    return _make_table(
        rng,
        subskill="39_financial_vs_non_financial_events_table",
        title="Financial vs Non-Financial Events Audit",
        prompt=prompt,
        journal_type="financial_events_audit",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Only events involving an actual exchange of money, goods, or credit count as Yes.",
            "tier_2": "Yes events affect Assets, OE, or Liabilities; No events have no monetary exchange.",
            "tier_3": "1: Yes (-A, -OE) | 2: No (No exchange) | 3: Yes (+A, +OE) | 4: No (No exchange).",
        },
        misconception_tags=["treats_operational_chores_as_transactions"],
        question_family_id="financial_events_table",
    )


def _b40_purpose_of_keeping_financial_records(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    bank = rng.choice(_BANKS)
    prompt = (
        f"{s['entrepreneur']} says: 'I run a small cash business in {s['area']}, so keeping receipts and books is a waste of time as long as there is cash in my pocket.' "
        f"Give FOUR reasons why {s['entrepreneur']} MUST keep accurate financial records."
    )
    sample = (
        "1. Determine true profit or loss accurately rather than guessing from pocket cash.\n"
        "2. Comply with legal tax obligations (SARS income tax and VAT reporting).\n"
        f"3. Provide credible financial evidence when applying for a business loan at {bank}.\n"
        "4. Prevent or detect employee theft, fraud, and unpaid customer debts."
    )
    pts = [
        "Calculates true Net Profit or Net Loss accurately.",
        "Required for SARS tax compliance and legal obligations.",
        f"Supports bank loan applications and credit checks (e.g. {bank}).",
        "Detects cash theft, fraud, and billing errors early.",
    ]
    return _make_rubric(
        rng,
        subskill="40_purpose_of_keeping_financial_records",
        title="Importance of Keeping Financial Records",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about profit measurement, tax authorities, banks, and internal control.",
            "tier_2": "Address profit calculation, SARS compliance, loan applications, and fraud prevention.",
            "tier_3": sample,
        },
        misconception_tags=["equates_cash_on_hand_with_profit"],
        question_family_id="purpose_financial_records",
    )


def _b41_cash_vs_credit_transaction_id(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    sup = rng.choice(SUPPLIERS)
    amt = rng.randint(4, 20) * 1000
    is_credit = rng.choice([True, False])
    if is_credit:
        prompt = (
            f"{s['business']} receives new stock worth {fmt_r(amt)} from {sup} today with an invoice marked 'Payable in 30 days'. "
            f"Identify the transaction type and the liability account created."
        )
        ans = "Credit transaction — increases Creditors Control (Current Liability)"
        exp = f"Because payment is deferred for 30 days rather than paid today, it is a credit transaction creating a liability to {sup} in Creditors Control ({fmt_r(amt)})."
    else:
        prompt = (
            f"{s['business']} buys stock worth {fmt_r(amt)} from {sup} and pays the full amount immediately by debit card / EFT. "
            f"Identify the transaction type and the payment account affected."
        )
        ans = "Cash transaction — decreases Bank (Current Asset) immediately"
        exp = f"Immediate payment by card or EFT reduces the Bank balance ({fmt_r(amt)}) immediately, so this is a cash transaction."
    opts = [
        "Credit transaction — increases Creditors Control (Current Liability)",
        "Cash transaction — decreases Bank (Current Asset) immediately",
        "Credit transaction — increases Debtors Control (Long-term Liability)",
        "Non-financial event — creates no entry in the books",
    ]
    return _make_mcq(
        rng,
        subskill="41_cash_vs_credit_transaction_id",
        title="Cash vs Credit Transactions",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Check whether money leaves the bank today or is promised in 30 days.",
            "tier_2": "Pay immediately = Cash (Bank); buy on 30-day invoice = Credit (Creditors Control).",
            "tier_3": ans,
        },
        misconception_tags=["confuses_card_eft_with_credit_account"],
        question_family_id="cash_vs_credit",
    )


def _b42_sole_trader_concept_and_entity_rule(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    car_amt = rng.randint(15, 45) * 100
    prompt = (
        f"{owner} is the sole trader owning {s['business']} in {s['area']}. {owner} uses the business bank card to pay {fmt_r(car_amt)} for their child's school fees and claims: "
        f"'Since I own 100% of {s['business']}, this is a business expense.' Why is {owner} incorrect?"
    )
    ans = "Under the Business Entity Rule, personal and business finances must be kept separate, so personal spending is Drawings"
    opts = [
        "Under the Business Entity Rule, personal and business finances must be kept separate, so personal spending is Drawings",
        "Sole traders are legally banned from ever withdrawing money from their own business",
        "School fees paid by the owner must be recorded as a Long-term Liability of the business",
        "Personal spending increases the Fixed Assets of the sole trader's enterprise",
    ]
    exp = f"According to the Business Entity Rule, the owner and the business are separate accounting entities. Paying {fmt_r(car_amt)} for personal school fees must be recorded as Drawings, not a business expense."
    return _make_mcq(
        rng,
        subskill="42_sole_trader_concept_and_entity_rule",
        title="Sole Trader & Business Entity Rule",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Accounting keeps the business's transactions completely separate from the owner's family spending.",
            "tier_2": "Recall the Business Entity Rule: personal expenses paid with business cash are Drawings.",
            "tier_3": ans,
        },
        misconception_tags=["violates_business_entity_rule"],
        question_family_id="business_entity_rule",
    )


def _b43_sole_trader_profit_retention_vs_drawings(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    open_cap = rng.randint(80, 150) * 1000
    add_cap = rng.randint(10, 30) * 1000
    profit = rng.randint(25, 65) * 1000
    drawings = rng.randint(8, 22) * 1000
    closing_oe = open_cap + add_cap + profit - drawings
    ans = fmt_r(closing_oe)
    prompt = (
        f"For the year ended 28 February, {s['business']} began with Owner's Equity of {fmt_r(open_cap)}. "
        f"During the year, {s['entrepreneur']} contributed additional capital of {fmt_r(add_cap)}, the business made a Net Profit of {fmt_r(profit)}, "
        f"and {s['entrepreneur']} took Drawings of {fmt_r(drawings)}. Calculate the closing Owner's Equity."
    )
    steps = [
        f"Opening Equity + Additional Capital = {fmt_r(open_cap)} + {fmt_r(add_cap)} = {fmt_r(open_cap + add_cap)}.",
        f"Add Net Profit: {fmt_r(open_cap + add_cap)} + {fmt_r(profit)} = {fmt_r(open_cap + add_cap + profit)}.",
        f"Subtract Drawings: {fmt_r(open_cap + add_cap + profit)} - {fmt_r(drawings)} = {ans}.",
    ]
    return _make_typed(
        rng,
        subskill="43_sole_trader_profit_retention_vs_drawings",
        title="Closing Owner's Equity with Additional Capital",
        prompt=prompt,
        correct_ans=ans,
        acceptable_answers=[ans, f"R{closing_oe}", str(closing_oe)],
        steps=steps,
        hints={
            "tier_1": "Start with Opening Equity, add anything that grows the owner's stake, and subtract personal withdrawals.",
            "tier_2": "Closing OE = Opening OE + Additional Capital + Net Profit - Drawings.",
            "tier_3": f"Closing Owner's Equity = {ans}.",
        },
        misconception_tags=["omits_additional_capital_or_drawings"],
        question_family_id="closing_oe_multi",
    )


def _b44_legal_compliance_sars_vat_tax(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    retention_years = 5
    turnover = rng.randint(350, 950) * 1000
    prompt = (
        f"{s['business']} in {s['area']} generated annual turnover of {fmt_r(turnover)}. "
        f"Why does South African law require {s['entrepreneur']} to retain source documents, bank statements, and ledgers for at least {retention_years} years?"
    )
    ans = f"For South African Revenue Service (SARS) income tax/VAT verification and legal audit compliance"
    opts = [
        "For South African Revenue Service (SARS) income tax/VAT verification and legal audit compliance",
        "To guarantee customers can return perishable groceries after five years",
        "So commercial banks can confiscate old stationery at the end of five years",
        "Because Accounting Equations only balance once five years of paper records exist",
    ]
    exp = f"Under South African tax legislation, businesses earning revenue such as {fmt_r(turnover)} must retain complete financial records for at least {retention_years} years for SARS tax audits and legal verification."
    return _make_mcq(
        rng,
        subskill="44_legal_compliance_sars_vat_tax",
        title="SARS Tax Compliance & Record Retention",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Think about the national tax authority that inspects business earnings and expenses.",
            "tier_2": "SARS requires financial proof to verify declared income, expenses, and taxes over 5 years.",
            "tier_3": ans,
        },
        misconception_tags=["ignores_legal_tax_retention_purpose"],
        question_family_id="sars_compliance",
    )


def _b45_fraud_prevention_internal_control(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    cash_missing = rng.randint(5, 19) * 100
    prompt = (
        f"While reviewing {s['business']}'s end-of-week cash count in {s['area']}, {s['entrepreneur']} discovers that till totals show {fmt_r(cash_missing)} more in sales "
        f"than the cash actually deposited into the bank. Explain TWO ways proper internal financial controls help prevent and detect fraud like cash skimming."
    )
    sample = (
        f"1. Independent cross-checking: Comparing pre-numbered till rolls/receipts against bank deposit slips immediately exposes missing sums ({fmt_r(cash_missing)}).\n"
        "2. Separation of duties & sequential numbering: Having one person handle cash and another reconcile bank statements stops employees from hiding altered or voided slips."
    )
    pts = [
        f"Cross-checking source documents (till rolls/receipts) against bank statements detects missing cash ({fmt_r(cash_missing)}).",
        "Sequential numbering and separation of duties deter tampering or hiding fraudulent entries.",
    ]
    return _make_rubric(
        rng,
        subskill="45_fraud_prevention_internal_control",
        title="Fraud Prevention & Internal Control",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Think about comparing two independent records and dividing cash vs recording duties.",
            "tier_2": "Mention matching till/receipt totals with bank deposits and using sequential numbering or duty separation.",
            "tier_3": sample,
        },
        misconception_tags=["misses_cross_verification_principle"],
        question_family_id="fraud_prevention_rubric",
        marks=2,
    )


def _b46_accounting_terminology_matching_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    pairs = [
        ("Resources contributed by the owner to start the business", "Capital"),
        ("Money or stock taken by the owner for personal family use", "Drawings"),
        ("Suppliers to whom the business owes money for credit purchases", "Creditors Control"),
        ("Customers who owe the business money for goods bought on credit", "Debtors Control"),
        ("Unfavourable bank balance where more is spent than held in account", "Bank Overdraft"),
        ("Cash kept in the till to give change to customers", "Cash Float"),
        ("Total assets minus total liabilities representing the owner's stake", "Owner's Equity"),
    ]
    chosen = rng.sample(pairs, 4)
    headers = ["Accounting Description", "Correct Accounting Term"]
    table_rows = [[(desc, "given", False), (term, "required", True)] for desc, term in chosen]
    cell_hints = {
        f"t0_r{idx}_c1": f"Identify the exact accounting term matching description #{idx + 1}."
        for idx in range(len(chosen))
    }
    prompt = f"Complete the terminology table below for {s['business']} by writing the exact Accounting Term beside each definition."
    return _make_table(
        rng,
        subskill="46_accounting_terminology_matching_table",
        title="Accounting Terminology Matching Table",
        prompt=prompt,
        journal_type="terminology_match",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "Read every keyword: 'owner personal use', 'customers owe', 'till change', 'owe suppliers'.",
            "tier_2": "Recall standard Grade 8 terms: Capital, Drawings, Creditors Control, Debtors Control, Bank Overdraft, Cash Float, Owner's Equity.",
            "tier_3": "; ".join(f"{t}" for _, t in chosen),
        },
        misconception_tags=["confuses_standard_accounting_terms"],
        question_family_id="terminology_table",
    )


def _b47_calculate_missing_asset_or_liability_table(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    veh = rng.randint(80, 160) * 1000
    equip = rng.randint(15, 45) * 1000
    stock = rng.randint(10, 30) * 1000
    bank = rng.randint(5, 25) * 1000
    loan = rng.randint(30, 80) * 1000
    cred = rng.randint(6, 20) * 1000

    tot_fixed = veh + equip
    tot_curr = stock + bank
    tot_assets = tot_fixed + tot_curr
    tot_liab = loan + cred
    net_worth = tot_assets - tot_liab

    headers = ["Category / Item", "Amount (R)"]
    table_rows = [
        [(f"Vehicles ({fmt_r(veh)}) + Equipment ({fmt_r(equip)}) -> Total Fixed Assets", "given", False), (fmt_r(tot_fixed), "required", True)],
        [(f"Trading Stock ({fmt_r(stock)}) + Bank ({fmt_r(bank)}) -> Total Current Assets", "given", False), (fmt_r(tot_curr), "required", True)],
        [("Total Assets (Fixed + Current)", "given", False), (fmt_r(tot_assets), "required", True)],
        [(f"Bank Loan ({fmt_r(loan)}) + Creditors ({fmt_r(cred)}) -> Total Liabilities", "given", False), (fmt_r(tot_liab), "required", True)],
        [("Owner's Equity / Net Worth (Assets - Liabilities)", "given", False), (fmt_r(net_worth), "required", True)],
    ]
    cell_hints = {
        "t0_r0_c1": f"{fmt_r(veh)} + {fmt_r(equip)}",
        "t0_r1_c1": f"{fmt_r(stock)} + {fmt_r(bank)}",
        "t0_r2_c1": "Add Total Fixed Assets and Total Current Assets.",
        "t0_r3_c1": f"{fmt_r(loan)} + {fmt_r(cred)}",
        "t0_r4_c1": "Total Assets minus Total Liabilities.",
    }
    prompt = f"Complete the Net Worth calculation table below for {s['business']} in {s['area']} using the balances provided in each row."
    return _make_table(
        rng,
        subskill="47_calculate_missing_asset_or_liability_table",
        title="Net Worth Statement Calculation Table",
        prompt=prompt,
        journal_type="net_worth_table",
        headers=headers,
        table_rows=table_rows,
        cell_hints=cell_hints,
        hints={
            "tier_1": "First group Fixed Assets and Current Assets separately, then add them to get Total Assets.",
            "tier_2": "Subtract Total Liabilities from Total Assets to get Owner's Equity (Net Worth).",
            "tier_3": f"Fixed: {fmt_r(tot_fixed)}, Current: {fmt_r(tot_curr)}, Assets: {fmt_r(tot_assets)}, Liab: {fmt_r(tot_liab)}, OE: {fmt_r(net_worth)}.",
        },
        misconception_tags=["adds_liabilities_instead_of_subtracting_for_net_worth"],
        question_family_id="net_worth_table",
    )


def _b48_true_false_concepts_audit(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    amt = rng.randint(5, 25) * 100
    statements = [
        (
            f"A trainee bookkeeper at {s['business']} writes: 'Because {s['entrepreneur']} took {fmt_r(amt)} cash out for groceries, Drawings is an Operating Expense that lowers Net Profit.' Evaluate this claim.",
            "False — Drawings reduces Owner's Equity directly, NOT Net Profit (it is not an expense)",
            "Drawings represents personal withdrawals by the owner and reduces Owner's Equity directly; expenses are costs incurred to generate business income.",
        ),
        (
            f"A trainee bookkeeper at {s['business']} writes: 'Our {fmt_r(amt * 10)} Bank Overdraft is a Current Asset because it involves a Bank account.' Evaluate this claim.",
            "False — a Bank Overdraft means the business owes money to the bank, making it a Current Liability",
            "Only a favourable/positive Bank balance is a Current Asset; an unfavourable Bank Overdraft is a short-term debt (Current Liability).",
        ),
        (
            f"A trainee bookkeeper at {s['business']} writes: 'Trading Stock worth {fmt_r(amt * 10)} is a Fixed Asset because shelves stay in the shop all year.' Evaluate this claim.",
            "False — Trading Stock is bought for short-term resale and is a Current Asset",
            "Trading Stock is held to be sold within 12 months (Current Asset), whereas the shop shelves themselves (Equipment) are Fixed Assets.",
        ),
    ]
    prompt, ans, exp = rng.choice(statements)
    opts = [
        ans,
        "True — the trainee applied the standard South African accounting rule accurately",
        "False — the transaction should be recorded as Additional Capital",
        "True — all bank-related and stock items belong under Owner's Equity",
    ]
    return _make_mcq(
        rng,
        subskill="48_true_false_concepts_audit",
        title="Accounting Statement Audit (True/False)",
        prompt=prompt,
        options=opts,
        correct_ans=ans,
        explanation=exp,
        hints={
            "tier_1": "Test the trainee's reasoning against the exact definition of the accounting element.",
            "tier_2": "Watch out for common misconceptions: Drawings vs Expense, Overdraft vs Bank, Stock vs Equipment.",
            "tier_3": ans,
        },
        misconception_tags=["accepts_common_bookkeeping_misconception"],
        question_family_id="statement_audit_tf",
    )


def _b49_case_study_profit_and_savings_advice(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    inc = rng.randint(18, 42) * 1000
    exp = rng.randint(11, 22) * 1000
    if exp >= inc:
        exp = inc - 4000
    profit = inc - exp
    drawings = profit + rng.randint(1, 3) * 1000
    prompt = (
        f"{owner} operates {s['business']} in {s['area']}. Last month, Total Income was {fmt_r(inc)} and Total Expenses were {fmt_r(exp)}. "
        f"However, {owner} took Drawings of {fmt_r(drawings)} for personal expenses and saved R0 for emergencies. "
        f"Calculate the Net Profit and advise {owner} on why this withdrawal habit threatens the survival of {s['business']}."
    )
    sample = (
        f"Net Profit = {fmt_r(inc)} - {fmt_r(exp)} = {fmt_r(profit)}.\n"
        f"Threat 1 (Capital erosion): Drawings ({fmt_r(drawings)}) exceed Net Profit ({fmt_r(profit)}) by {fmt_r(drawings - profit)}, eating into the business's original Capital and working cash.\n"
        f"Threat 2 (Zero buffer): Without monthly savings, {s['business']} will be forced into costly debt/bank overdraft if equipment breaks or sales drop."
    )
    pts = [
        f"Correctly calculates Net Profit as {fmt_r(profit)} ({fmt_r(inc)} - {fmt_r(exp)}).",
        f"Identifies that Drawings ({fmt_r(drawings)}) exceed Net Profit, shrinking Owner's Equity / Capital.",
        "Explains that zero savings leaves the business vulnerable to emergencies or costly debt.",
    ]
    return _make_rubric(
        rng,
        subskill="49_case_study_profit_and_savings_advice",
        title="Case Study: Profit vs Excessive Drawings",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "First compute Net Profit (Income - Expenses) and compare it to Drawings.",
            "tier_2": "When Drawings > Profit, Owner's Equity shrinks instead of growing.",
            "tier_3": sample,
        },
        misconception_tags=["ignores_drawings_exceeding_profit"],
        question_family_id="case_study_drawings",
        marks=3,
    )


def _b50_comprehensive_net_worth_and_records_synthesis(rng: random.Random) -> Dict[str, Any]:
    s = get_ems_scenario(rng)
    owner = s["entrepreneur"]
    assets = rng.randint(120, 260) * 1000
    liab = rng.randint(35, 95) * 1000
    oe = assets - liab
    inc = rng.randint(45, 90) * 1000
    exp = rng.randint(25, 50) * 1000
    profit = inc - exp
    svg = _svg_ledger_card(
        f"{s['business']} — Annual Financial Snapshot",
        f"Owner: {owner} ({s['area']})",
        [
            ("Total Assets (A)", fmt_r(assets)),
            ("Total Liabilities (L)", fmt_r(liab)),
            ("Annual Income", fmt_r(inc)),
            ("Annual Expenses", fmt_r(exp)),
        ],
    )
    prompt = (
        f"Inspect the Annual Financial Snapshot for {s['business']} (owned by {owner} in {s['area']}). "
        f"(a) Calculate Net Worth (Owner's Equity). (b) Calculate Annual Net Profit. "
        f"(c) State ONE reason why {owner} needs verified financial records to present these results to a bank."
    )
    sample = (
        f"(a) Net Worth (Owner's Equity) = Assets - Liabilities = {fmt_r(assets)} - {fmt_r(liab)} = {fmt_r(oe)}.\n"
        f"(b) Annual Net Profit = Income - Expenses = {fmt_r(inc)} - {fmt_r(exp)} = {fmt_r(profit)}.\n"
        f"(c) Commercial banks require verified source documents, ledgers, and statements to confirm true profitability ({fmt_r(profit)}) and solvency before approving a loan."
    )
    pts = [
        f"Correctly calculates Owner's Equity = {fmt_r(oe)} ({fmt_r(assets)} - {fmt_r(liab)}).",
        f"Correctly calculates Net Profit = {fmt_r(profit)} ({fmt_r(inc)} - {fmt_r(exp)}).",
        "Explains that verified financial records prove solvency and repayment ability for credit/loans.",
    ]
    return _make_rubric(
        rng,
        subskill="50_comprehensive_net_worth_and_records_synthesis",
        title="Comprehensive Net Worth, Profit & Records Synthesis",
        prompt=prompt,
        sample_answer=sample,
        marking_points=pts,
        hints={
            "tier_1": "Use A - L = OE for part (a) and Income - Expenses = Profit for part (b).",
            "tier_2": "Part (c) focuses on proof of creditworthiness and legal compliance for external lenders.",
            "tier_3": sample,
        },
        misconception_tags=["mixes_balance_sheet_net_worth_with_profit"],
        question_family_id="comprehensive_synthesis",
        marks=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


ARCHETYPES_26_50 = {
    "26_business_budget_definition_purpose": _b26_business_budget_definition_purpose,
    "27_cash_budget_surplus_or_deficit_calc": _b27_cash_budget_surplus_or_deficit_calc,
    "28_personal_vs_business_budget": _b28_personal_vs_business_budget,
    "29_savings_definition_purpose": _b29_savings_definition_purpose,
    "30_savings_compound_interest_comparison": _b30_savings_compound_interest_comparison,
    "31_banking_role_modern_economy": _b31_banking_role_modern_economy,
    "32_banking_services_cheque_and_current_acct": _b32_banking_services_cheque_and_current_acct,
    "33_debit_order_vs_stop_order": _b33_debit_order_vs_stop_order,
    "34_atm_eft_online_banking_services": _b34_atm_eft_online_banking_services,
    "35_bank_loan_and_credit_facility": _b35_bank_loan_and_credit_facility,
    "36_economic_importance_of_banks": _b36_economic_importance_of_banks,
    "37_financial_records_definition_examples": _b37_financial_records_definition_examples,
    "38_financial_transactions_definition": _b38_financial_transactions_definition,
    "39_financial_vs_non_financial_events_table": _b39_financial_vs_non_financial_events_table,
    "40_purpose_of_keeping_financial_records": _b40_purpose_of_keeping_financial_records,
    "41_cash_vs_credit_transaction_id": _b41_cash_vs_credit_transaction_id,
    "42_sole_trader_concept_and_entity_rule": _b42_sole_trader_concept_and_entity_rule,
    "43_sole_trader_profit_retention_vs_drawings": _b43_sole_trader_profit_retention_vs_drawings,
    "44_legal_compliance_sars_vat_tax": _b44_legal_compliance_sars_vat_tax,
    "45_fraud_prevention_internal_control": _b45_fraud_prevention_internal_control,
    "46_accounting_terminology_matching_table": _b46_accounting_terminology_matching_table,
    "47_calculate_missing_asset_or_liability_table": _b47_calculate_missing_asset_or_liability_table,
    "48_true_false_concepts_audit": _b48_true_false_concepts_audit,
    "49_case_study_profit_and_savings_advice": _b49_case_study_profit_and_savings_advice,
    "50_comprehensive_net_worth_and_records_synthesis": _b50_comprehensive_net_worth_and_records_synthesis,
}
